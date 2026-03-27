# Day 7 — Resource Hints Rules & GitHub Issue Drafting

## What we built and why

Day 6 left the project at 91% coverage, a working Doctor MVP, and a clean CI
pipeline. Day 7 tackles two stretch goals that close visible gaps in what the
tool reports and what it produces.

**Stretch A — Resource hints (RESOURCE-001, RESOURCE-002).**
Every cloud WES platform (AWS Batch, Google Life Sciences, Azure Batch) must
decide which instance type to provision *before* it runs your process. Without
`cpus` and `memory` declarations it falls back to a platform default — usually
either embarrassingly small (causing OOM kills on aligners or variant callers)
or wastefully large (incurring unnecessary cost). Up to Day 6 the Critic already
caught missing containers and hardcoded paths, but said nothing about resource
declarations. These two new rules fill that gap.

**Stretch B — GitHub issue drafting (`--create-issue`).**
A gap report is only as useful as the action it triggers. The long-term goal
(Day 9) is to POST issues and PRs to GitHub automatically. Day 7 builds the
rendering half of that story: a `--create-issue` flag that produces a
publication-ready GitHub issue body — with emoji severity badges, collapsible
per-gap `<details>` blocks, and a label recommendation list — without submitting
anything. The draft can be reviewed, edited, and pasted manually, or piped into
the Day 9 `GitHubClient`.

By the end of Day 7 the pipeline is unchanged in shape but richer in what it
reports and what it emits:

```
.nf file → NextflowParser → ParsedWorkflow
         → CriticEngine (6 rules) → GapReport
         → CLI → terminal / json / markdown
               → GitHub issue draft (--create-issue)
```

---

## New files introduced today

```
workflow_clinic/
└── critic/
    └── rules/
        └── resource_hints.py     ← CpusMissingRule (RESOURCE-001)
                                     MemoryMissingRule (RESOURCE-002)
tests/
└── test_resource_rules.py        ← 31 tests: unit, engine integration, CLI
```

**Modified files:**

```
workflow_clinic/critic/engine.py  ← registers the two new rules in _RULES
workflow_clinic/cli.py            ← critic command gains --create-issue,
                                     --issue-output, _render_github_issue(),
                                     _handle_issue_draft(), _issue_labels()
```

---

## Stretch A: Resource hints rules

### The rules

Both rules live in `workflow_clinic/critic/rules/resource_hints.py`.

**`CpusMissingRule` — RESOURCE-001**

```python
class CpusMissingRule(BaseRule):
    def check(self, process: NextflowProcess, file_path: str) -> Gap | None:
        if process.cpus is not None:
            return None
        return Gap(gap_id="RESOURCE-001", severity=Severity.MINOR, ...)
```

Checks `process.cpus is None`. That field is already populated by the Day 1
parser from the `cpus` directive, so no parser changes are needed. The gap fires
at `MINOR` severity — the workflow will still run on one core, but it cannot
parallelise via `${task.cpus}` and the scheduler cannot pick the right instance
type. `auto_fixable=False` because the correct value is workload-specific and
cannot be inferred from the script alone; that is a future LLM-assisted fixer.

**`MemoryMissingRule` — RESOURCE-002**

```python
class MemoryMissingRule(BaseRule):
    def check(self, process: NextflowProcess, file_path: str) -> Gap | None:
        if process.memory is not None:
            return None
        return Gap(gap_id="RESOURCE-002", severity=Severity.MINOR, ...)
```

Same pattern, same severity. The recommendation deliberately includes the
Nextflow `errorStrategy`/`maxRetries` retry-with-escalation pattern:

```groovy
errorStrategy 'retry'
maxRetries 2
memory { (8.GB * task.attempt).clamp(null, 32.GB) }
```

This is a real community best practice for cloud pipelines: start small, let
the platform retry on OOM, and cap at a sensible ceiling. It is more useful than
a plain "add `memory '8 GB'`" instruction.

**Resources:**
- [Nextflow process resource directives](https://www.nextflow.io/docs/latest/process.html#cpus)
  — the `cpus`, `memory`, `disk`, and `time` directives explained, with the
  `task.attempt` escalation pattern documented in the `memory` section.
- [Nextflow error handling](https://www.nextflow.io/docs/latest/process.html#errorstrategy)
  — the `errorStrategy 'retry'` + `maxRetries` pattern used in the recommendation.
- [AWS Batch instance selection](https://docs.aws.amazon.com/batch/latest/userguide/job_definition_parameters.html#ContainerProperties-vcpus)
  — explains exactly how `vcpus` and `memory` in a job definition map to EC2
  instance type selection, which is the cloud consequence of leaving these unset.

### Why two rules instead of one

The design choice to keep `CpusMissingRule` and `MemoryMissingRule` separate
mirrors the same reasoning behind having `ContainerMissingRule` and
`ContainerLatestTagRule` in `workflow_clinic/critic/rules/containerization.py`:
each `gap_id` must map 1-to-1 to a remediation action. When the Day 8+ Doctor
gains resource-hint fixers, `RESOURCE-001` will target a cpus fixer and
`RESOURCE-002` will target a memory fixer — independently, with independent
confidence scores and validation logic. A single `"RESOURCE-001: missing cpus
and memory"` gap_id would require a compound fixer that is harder to test and
harder to partially apply.

### Registering the rules in the engine

`workflow_clinic/critic/engine.py` gains two import lines and two list entries:

```python
from workflow_clinic.critic.rules.resource_hints import (
    CpusMissingRule,
    MemoryMissingRule,
)

_RULES: list[BaseRule] = [
    ContainerMissingRule(),
    ContainerLatestTagRule(),
    HardcodedPathRule(),
    UndeclaredOutputRule(),
    CpusMissingRule(),      # ← new
    MemoryMissingRule(),    # ← new
]
```

Rule order in `_RULES` is the order gaps appear in the report. Container rules
come first (highest severity), resource hints last (lowest severity). This is a
purely cosmetic choice but it makes terminal output and issue bodies read in
a natural priority order.

The key invariant to verify after adding new rules is that `clean.nf` still
scores 1.00. Both `ALIGN` and `SORT_BAM` in `tests/fixtures/nextflow/clean.nf`
have explicit `cpus` and `memory` directives, so neither new rule fires on them.
The test `test_clean_no_gaps` in `tests/test_critic_engine.py` acts as the
sentinel for this invariant.

**Resources:**
- [Python `abc` module — Abstract Base Classes](https://docs.python.org/3/library/abc.html)
  — `BaseRule` in `workflow_clinic/critic/rules/base.py` uses `ABC` and
  `@abstractmethod`; this documents the contract every rule must satisfy.

### Fixture coverage

The three existing fixtures in `tests/fixtures/nextflow/` exercise the new rules
without any modification:

| Fixture | RESOURCE-001 | RESOURCE-002 | Notes |
|---|---|---|---|
| `clean.nf` | silent | silent | Both directives present on both processes |
| `broken.nf` | fires × 2 | fires × 2 | Neither process has cpus or memory |
| `partial.nf` TRIM | silent | fires | Has `cpus 2`, missing `memory` |
| `partial.nf` FASTQC | silent | silent | Has `cpus 1` and `memory '2 GB'` |

`partial.nf` is the most instructive case: TRIM has a `cpus` directive (added
as a known-good field in Day 1) but its memory comment reads `// memory missing`
— the fixture was designed for this exact scenario. FASTQC has both, so neither
rule fires, validating that the rules are genuinely condition-specific rather
than blanket-firing.

---

## Stretch B: GitHub issue drafting

### The `--create-issue` flag

The `critic` command in `workflow_clinic/cli.py` gains two new options:

```python
create_issue: bool = typer.Option(False, "--create-issue", ...)
issue_output: Path | None = typer.Option(None, "--issue-output", ...)
```

`--issue-output PATH` implies `--create-issue` automatically, handled at the
top of the command body:

```python
if issue_output is not None:
    create_issue = True
```

This mirrors the established pattern of `--score` as an early-return shortcut
and `--output` as a write-to-file override. The user should not need to pass
both `--create-issue` and `--issue-output` — specifying a file path is already
an unambiguous declaration of intent.

**Resources:**
- [Typer — options with callbacks](https://typer.tiangolo.com/tutorial/options/)
  — explains `typer.Option` defaults and how flags differ from named arguments.

### The `_render_github_issue` function

`_render_github_issue(report: GapReport) -> tuple[str, str]` in
`workflow_clinic/cli.py` returns `(title, body)`. Separating title from body
matters for Day 9: `GitHubClient.create_issue()` will take them as separate
parameters matching the GitHub REST API's `title` and `body` fields.

**Title construction:** the title is computed from the gap count and affected
process names:

```python
# 0 gaps:   "[Workflow Clinic] No cloud-readiness gaps found (score: 100%)"
# 1 process: "[Workflow Clinic] 3 cloud-readiness gaps in process `ALIGN` (score: 20%)"
# N processes: "[Workflow Clinic] 9 cloud-readiness gaps across 2 processes (score: 20%)"
```

The `[Workflow Clinic]` prefix is intentional — it makes the bot's issues
immediately recognisable in a busy issue tracker and enables GitHub search
filters like `is:issue "[Workflow Clinic]"`.

**Body structure:** the body is designed to be useful to a developer who has
never run the tool themselves. It contains four sections:

1. **Attribution blockquote** — identifies the tool, links to the repo, shows
   the workflow path and generation timestamp. Rendered as a GitHub blockquote
   so it is visually distinguished from the human-authored content that will
   be added later.
2. **Score badge** — a single `🟢 / 🟡 / 🔴` emoji with the numeric score.
   Plain text emoji rather than a badge image because GitHub renders emoji
   reliably in all contexts (issues, PR descriptions, email notifications).
3. **Summary table** — counts per severity level with a one-line description
   of each level's impact. The `auto_fixable` row includes a direct command
   for running the Doctor, reducing friction for users who want to apply fixes.
4. **Per-gap detail** — one `<details><summary>` block per gap. The collapsible
   format is critical: a workflow like `nf-core/atacseq` has 88 gaps; rendering
   them all expanded would produce a page-length wall of text. Collapsed by
   default, each detail block contains the gap's description, evidence verbatim
   in a code fence, and the recommendation in a code fence.

```markdown
<details><summary>🔴 <strong>1. CONTAINER-001 — ALIGN</strong> (CRITICAL)</summary>

**Category:** `containerization`
**Location:** `broken.nf` L1–11
**Auto-fixable:** Yes

**Description:**
Process 'ALIGN' has no container directive...

**Evidence:**
```
(empty)
```

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'
```

</details>
```

**Resources:**
- [GitHub Flavored Markdown — `<details>` and `<summary>`](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/organizing-information-with-collapsed-sections)
  — the collapsible section syntax used for per-gap detail blocks.
- [GitHub REST API — create an issue](https://docs.github.com/en/rest/issues/issues?apiVersion=2022-11-28#create-an-issue)
  — the `title`, `body`, and `labels` fields that `_render_github_issue` maps to.
  Day 9's `GitHubClient.create_issue()` will call this endpoint directly.
- [GitHub search qualifiers](https://docs.github.com/en/search-github/searching-on-github/searching-issues-and-pull-requests)
  — explains `is:issue in:title "[Workflow Clinic]"`, the query Day 9's
  deduplication check will use before opening a new issue.

### The `_issue_labels` helper

`_issue_labels(report: GapReport) -> list[str]` in `workflow_clinic/cli.py`
produces a list of suggested label strings that Day 9 will pass to
`GitHubClient.create_issue()`:

```python
# Always present:
["workflow-clinic", "cloud-readiness"]

# One per severity level that has at least one gap:
["severity:critical", "severity:major", "severity:minor"]

# One per gap category present in the report (de-duplicated):
["gap:containerization", "gap:storage", "gap:resource-hints"]
```

Labels are displayed in the terminal output alongside the issue draft when
`--issue-output` is not set. They are embedded as a comment in the saved file
when it is. The label names follow the GitHub convention of using colons as
namespacing separators (`scope:value`) so they sort and filter cleanly in the
issue tracker.

### Handling mixed output correctly: the `rfind` bug

When `--format json --create-issue` are combined, the output stream contains
a JSON object followed by rich-rendered markdown. An initial test implementation
extracted the JSON with:

```python
json_end = result.output.rfind("}") + 1
data = json.loads(result.output[json_start:json_end])
```

This fails because the RESOURCE-002 recommendation includes a Groovy expression:

```groovy
memory { (8.GB * task.attempt).clamp(null, 32.GB) }
```

The trailing `}` on that line is what `rfind` finds — not the closing brace of
the JSON object. The result is a string that starts as valid JSON and then has
thousands of characters of markdown appended, causing `JSONDecodeError: Extra data`.

The correct fix is `json.JSONDecoder().raw_decode()`, which advances a cursor
through the string and stops *exactly* at the end of the first complete JSON
value, regardless of subsequent content:

```python
json_start = result.output.find("{")
data, _ = json.JSONDecoder().raw_decode(result.output, json_start)
```

The `_` is the end index — the position in the string immediately after the
closing `}` of the JSON object. We discard it here but Day 9's streaming parser
would use it to locate the beginning of the markdown section.

The general lesson: whenever a CLI command mixes structured output with
free-form text on the same stream, use a parser that knows when the structured
section ends rather than a string search heuristic. The same issue would appear
for any recommendation text that contains `{` or `}` — shell `${}` expressions,
Python dicts in evidence fields, WDL `runtime {}` blocks.

**Resources:**
- [Python `json.JSONDecoder.raw_decode`](https://docs.python.org/3/library/json.html#json.JSONDecoder.raw_decode)
  — the exact method used in the fixed test; the docs explain the `idx` argument
  and why `raw_decode` is the right tool for parsing JSON embedded in a larger string.

---

## Test strategy

Tests live in `tests/test_resource_rules.py`. The file is organised into four
classes to make failures immediately locatable:

**`TestCpusMissingRule`** — 8 unit tests on `CpusMissingRule` in complete
isolation. Key tests: `test_fires_on_broken` (2 gaps from `broken.nf`),
`test_silent_on_clean` (0 gaps), `test_fires_on_trim_in_partial` which actually
asserts `None` — TRIM has `cpus 2` and must not fire — and
`test_recommendation_mentions_task_cpus` which checks the recommendation text
for `task.cpus`, ensuring the doc-string quality contract is enforced.

**`TestMemoryMissingRule`** — 8 unit tests mirroring the cpus class. The most
interesting is `test_fires_on_trim_in_partial`: TRIM is the only process in
the fixture set that has `cpus` but not `memory`, making it a precise test that
the two rules are genuinely independent.

**`TestResourceRulesInEngine`** — 9 integration tests running the full
`CriticEngine` (all 6 rules) against the fixtures. The critical ones:
- `test_clean_still_has_no_gaps` — the regression guard. If a new rule
  accidentally fires on `clean.nf`, this test catches it immediately.
- `test_partial_trim_has_resource_002_not_001` — verifies TRIM gets exactly
  one resource gap, not both.
- `test_broken_total_count_includes_resource_gaps` — arithmetic check that
  `total_gaps == critical + major + minor + info`. This would catch any
  severities being double-counted or lost in the score computation.

**`TestCreateIssueFlag`** — 13 CLI integration tests using Typer's `CliRunner`.
All tests run the full `critic` command in-process; no mocking is needed because
the new flag only touches rendering code. Highlights:
- `test_create_issue_notes_it_is_not_submitted` — enforces the safety contract:
  the output must contain wording that makes clear nothing was sent to GitHub.
  This will be kept even after Day 9 adds real submission, because the draft
  path (no `--submit`) must always be explicit about its non-submitting nature.
- `test_issue_output_file_contains_title_comment` — asserts the file begins
  with `<!-- WORKFLOW CLINIC ISSUE DRAFT -->`. This comment is how Day 9's
  `GitHubClient` will recognise a pre-drafted file vs. a manually written one.
- `test_create_issue_includes_resource_001_gaps` and `..._002_gaps` — ensure
  the new MINOR gaps thread all the way through the rendering pipeline and
  appear in the issue body.

**Coverage after Day 7:**

| Module | Coverage |
|---|---|
| `critic/rules/resource_hints.py` | 100% |
| `critic/engine.py` | 100% |
| `cli.py` | ~91% (issue submission path not yet reachable — Day 9) |
| Overall | ≥91% |

---

## What Day 8 builds on top of this

The two new rules complete the six portability-blocker categories originally
scoped in the proposal:

| Category | Rules now implemented |
|---|---|
| Containerization | CONTAINER-001, CONTAINER-002 |
| Storage | STORAGE-001 |
| I/O declaration | IO-001 |
| Resource hints | RESOURCE-001, RESOURCE-002 ← today |
| Reproducibility | (planned: REPRO-001 unpinned conda, REPRO-002 no digest) |
| Metadata | (planned: META-001 no schema, META-002 no license) |

Day 8 adds a second workflow language — Snakemake — and introduces
`workflow_clinic/parsers/registry.py`, the factory that routes `.nf` files to
`NextflowParser` and `.smk` files to `SnakemakeParser`. Because all parsers map
onto the same `ParsedProcess` dataclass shape, every rule written so far —
including today's resource hints — will run unchanged on Snakemake workflows
without any rule-level modifications.

The `--create-issue` draft renderer is also directly reused in Day 9: the
`_render_github_issue` function already returns `(title, body)` exactly matching
the parameters of `GitHubClient.create_issue()`. Day 9's `--submit` flag adds
one additional code path — calling the client — without modifying the rendering
logic at all.