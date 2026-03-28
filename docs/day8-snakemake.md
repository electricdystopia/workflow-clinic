# Day 8 — Snakemake Parser & Language-Agnostic Rule Porting

## What we built and why

Day 7 completed the six portability-blocker rule categories for Nextflow.
Day 8 proves the architecture generalises — not by adding more rules, but by
adding a second workflow language and showing that every existing rule runs on
it without modification.

The deliverables are:

1. `SnakemakeParser` — a line-by-line state machine for `.smk` files that
   maps Snakemake directives into the shared `NextflowProcess` dataclass so
   every existing Critic rule runs unchanged.
2. `ParserRegistry` — a factory that routes `.nf` → `NextflowParser` and
   `.smk` → `SnakemakeParser` from a single lookup table, wired into the
   three CLI commands.
3. `CONTAINER-003` — one new Snakemake-specific rule for conda environments
   used without a singularity isolation wrapper.
4. A `conda` field added to `NextflowProcess` — always `None` for Nextflow
   processes, so zero existing tests are affected.

By the end of Day 8 the pipeline looks like this:
```
.nf file  ─┐
.smk file  ─┤→ ParserRegistry → WorkflowParser → NextflowProcess (shared)
Snakefile  ─┘                                           │
                                                        ▼
                                             CriticEngine (all 7 rules)
                                                        │
                                                        ▼
                                            GapReport → CLI output
```

---

## New files introduced today
```
workflow_clinic/
├── parsers/
│   ├── snakemake.py     ← SnakemakeParser (state machine for `rule` blocks)
│   └── registry.py      ← ParserRegistry: extension → parser factory
tests/
├── fixtures/snakemake/
│   ├── clean.smk        ← singularity + resources, full I/O — expects 0 gaps
│   ├── broken.smk       ← no singularity, no resources, hardcoded paths
│   └── partial.smk      ← conda without singularity, missing memory
├── test_snakemake_parser.py   ← mirrors test_nextflow_parser.py structure
└── test_critic_snakemake.py   ← engine + CLI integration on Snakemake fixtures
docs/
└── day8-snakemake.md          ← this file
```

**Modified files:**
```
workflow_clinic/parsers/nextflow.py              ← add conda field to NextflowProcess
workflow_clinic/critic/rules/containerization.py ← guard CONTAINER-001; add CONTAINER-003
workflow_clinic/critic/engine.py                 ← register ContainerCondaIsolationRule
workflow_clinic/cli.py                           ← use ParserRegistry in parse/critic/doctor
```

---

## The shared dataclass strategy — why it works

The key design decision is that both parsers write into the same
`NextflowProcess` dataclass defined in
`workflow_clinic/parsers/nextflow.py`. The dataclass is the contract. Every
rule in `workflow_clinic/critic/rules/` reads from that contract and nothing
else — meaning rules written before Day 8 had ever been conceived continue to
work on Snakemake output without a single line changed.

Both workflow languages encode the same information under different keywords:

| Concept         | Nextflow        | Snakemake                   | `NextflowProcess` field |
|---|---|---|---|
| Container image | `container:`    | `singularity:` / `container:` | `container`           |
| CPU count       | `cpus:`         | `threads:`                  | `cpus`                |
| Memory limit    | `memory:`       | `resources: mem_mb`         | `memory`              |
| Conda env       | —               | `conda:`                    | `conda` *(new)*       |
| Input files     | `input:` block  | `input:` block              | `input` (DirectiveBlock) |
| Output files    | `output:` block | `output:` block             | `output`              |
| Script / shell  | `script:` block | `shell:` / `run:` / `script:` | `script`            |

`process.conda` is the only net-new field. It is declared in
`workflow_clinic/parsers/nextflow.py` with a default of `None`, so every
existing `NextflowProcess` object silently carries the field at no cost and
every existing rule is unaffected.

**Resources:**
- [Python dataclasses — field defaults](https://docs.python.org/3/library/dataclasses.html#dataclasses.field)
  — how `field(default=None)` adds an optional attribute to a dataclass without
  breaking existing call sites that don't supply it. This is the exact mechanism
  that makes the `conda` addition backward-compatible.
- [Nextflow DSL2 process syntax](https://www.nextflow.io/docs/latest/process.html)
  — the reference for the Nextflow-side of the mapping table above; useful for
  checking which directives the Day 1 parser already captures.
- [Snakemake rule syntax reference](https://snakemake.readthedocs.io/en/stable/snakefiles/rules.html)
  — the authoritative reference for every keyword parsed in
  `workflow_clinic/parsers/snakemake.py`; read the `singularity`, `conda`,
  `threads`, and `resources` sections in particular.

---

## Why Snakemake uses indentation instead of braces

The Nextflow parser in `workflow_clinic/parsers/nextflow.py` tracks brace
depth to detect process boundaries:
```python
depth += line.count("{") - line.count("}")
if depth <= 0 and i > start:
    return proc, i + 1
```

This works for Groovy-based DSLs. Snakemake is Python-based — its block
structure is defined by indentation, not braces. A Snakemake rule block ends
at the first non-empty, non-comment line that returns to column 0:
```python
# In workflow_clinic/parsers/snakemake.py — _parse_rule()
if line[0] not in (" ", "\t"):
    proc.line_end = i
    return proc, i
```

This one-line check replaces all the brace counting. It is robust across the
two most common Snakemake indent styles (4 spaces and tab) because Python's
`str[0]` picks the first character of the physical line, which must be a space
or tab character for any indented content.

The practical tradeoff: Snakemake shell blocks can contain arbitrary `{` and
`}` characters (shell parameter expansions, awk programs, etc.) — brace-depth
tracking would miscalculate the block boundary on any such line. Indentation
tracking has no such failure mode because those characters only appear inside
the shell content, never at column 0.

**Resources:**
- [Snakemake — rules documentation](https://snakemake.readthedocs.io/en/stable/snakefiles/rules.html#rules)
  — explains the indentation contract for Snakemake rule blocks; the
  "Snakemake files" section shows the top-level layout the parser relies on.
- [Crafting Interpreters — Scanning chapter](https://craftinginterpreters.com/scanning.html)
  — the same resource recommended in `docs/day1-parser.md`; its explanation
  of indentation-sensitive tokenisation (the "line" scanner pattern) directly
  maps to how `_parse_rule` advances the cursor.
- [Python `str` methods — `lstrip` and `[0]` indexing](https://docs.python.org/3/library/stdtypes.html#str.lstrip)
  — `line[0] not in (" ", "\t")` is simpler than `len(line) - len(line.lstrip())
  == 0`; both detect column-0 lines but the former is more readable and avoids
  a length computation on every line.

---

## The `SnakemakeParser` — design decisions in detail

The parser lives in `workflow_clinic/parsers/snakemake.py`.  Five decisions are
worth calling out explicitly.

### Multi-line `singularity:` / `conda:`

Both directives appear in two syntactic forms in real Snakemake files:
```python
# Inline — matched by _RE_SINGULARITY_INLINE in snakemake.py
    singularity: "docker://quay.io/biocontainers/bwa:0.7.17--h5bf99c6_8"

# Multi-line section style — matched by _RE_SINGULARITY_SECTION +
# awaiting_string_for sentinel
    singularity:
        "docker://quay.io/biocontainers/bwa:0.7.17--h5bf99c6_8"
```

The parser handles the two-line form with an `awaiting_string_for` string
sentinel. When a bare `singularity:` section header is detected, the sentinel
is set; the next non-empty, non-comment line is inspected for a quoted string
(`_RE_QUOTED_VALUE`). If it matches, the value is captured. If it does not
(because the next line is actually a new section keyword), the sentinel is
cleared and the line is reprocessed — no directive is silently dropped.

This avoids the more complex approach of peeking ahead by one line, which
requires careful index management and fails at EOF.

**Resources:**
- [Snakemake — `singularity` directive](https://snakemake.readthedocs.io/en/stable/snakefiles/deployment.html#running-jobs-in-containers)
  — shows both inline and multi-line usage in real Snakemake workflows; the
  multi-line form is more common in community workflows on WorkflowHub.
- [Snakemake — `conda` directive](https://snakemake.readthedocs.io/en/stable/snakefiles/deployment.html#integrated-package-management)
  — explains the `conda:` directive, both as a YAML file path and as an inline
  channel specification.

### `shell:` / `run:` / `script:` → `process.script`

All three Snakemake execution directives map to `process.script`:
```python
# In workflow_clinic/parsers/snakemake.py — _parse_rule()
elif sname in ("shell", "run", "script"):
    current_section = "script"
```

This means `STORAGE-001` (hardcoded path detection, defined in
`workflow_clinic/critic/rules/storage.py`) fires on all three execution styles
without any rule-level change. The `run:` block can contain arbitrary Python
code, so `STORAGE-001` may produce more false positives there (a Python string
like `"/usr/bin/python"` is not a workflow portability issue), but that is a
known limitation flagged in `workflow_clinic/critic/rules/storage.py`'s existing
comment about false positives.

**Resources:**
- [Snakemake — `shell` directive](https://snakemake.readthedocs.io/en/stable/snakefiles/rules.html#shell)
- [Snakemake — `run` directive](https://snakemake.readthedocs.io/en/stable/snakefiles/rules.html#python-code-in-rules)
- [Snakemake — `script` directive](https://snakemake.readthedocs.io/en/stable/snakefiles/rules.html#external-scripts)

### `resources: mem_mb` and `resources: mem_gb`

The `resources:` section in Snakemake is a free-form key-value block — any
key is valid, and convention (not enforcement) dictates `mem_mb`:
```python
# In workflow_clinic/parsers/snakemake.py — module-level constants
_RE_MEM_MB   = re.compile(r"^\s+mem_mb\s*[=:]\s*(\d+)")
_RE_MEM_GB   = re.compile(r"^\s+mem_gb\s*[=:]\s*(\d+)")
_RE_RES_CPUS = re.compile(r"^\s+cpus\s*[=:]\s*(\d+)")
```

Both `mem_mb` and `mem_gb` are captured and normalised to a string like
`"8000 MB"`. `MemoryMissingRule` (in `workflow_clinic/critic/rules/resource_hints.py`)
only checks `process.memory is not None`, so the unit string is irrelevant to
whether the gap fires — it only appears in the evidence field of the `Gap`
object.

The regex uses `[=:]` to match both the assignment form (`mem_mb = 8000`) and
the colon form (`mem_mb: 8000`). Both appear in real-world Snakemake files;
Snakemake itself accepts either.

**Resources:**
- [Snakemake — `resources` directive](https://snakemake.readthedocs.io/en/stable/snakefiles/rules.html#resources)
  — documents `mem_mb` as the conventional memory resource key, and explains
  why Snakemake treats all resource keys as user-defined (no schema enforcement).
- [Python `re` — character class `[=:]`](https://docs.python.org/3/library/re.html#re.compile)
  — the `[=:]` pattern in `_RE_MEM_MB` is a character class matching either
  `=` or `:`; [regex101.com](https://regex101.com) is the fastest way to verify
  it against a real `resources:` block.

### `threads:` vs `resources: cpus`

`threads:` is the canonical Snakemake CPU directive; `resources: cpus` is an
alternative that some workflows use. The parser checks `threads:` first at the
section-keyword level and only falls back to `resources: cpus` inside the
resources body if `cpus` is still `None`:
```python
# In workflow_clinic/parsers/snakemake.py — _parse_rule()
m = _RE_THREADS.match(line)
if m:
    proc.cpus = m.group(1)
    ...

# Later, inside the resources body:
mc = _RE_RES_CPUS.match(line)
if mc and proc.cpus is None:   # threads: takes priority
    proc.cpus = mc.group(1)
```

The `proc.cpus is None` guard prevents `resources: cpus` from overwriting a
`threads:` value already captured earlier in the rule.

**Resources:**
- [Snakemake — `threads` directive](https://snakemake.readthedocs.io/en/stable/snakefiles/rules.html#threads)
  — explains that `threads:` is exposed to shell commands as `{threads}` and is
  the preferred way to declare parallelism in Snakemake.

---

## The `ParserRegistry` — the factory pattern

The registry lives in `workflow_clinic/parsers/registry.py`. Its core is a
single dictionary:
```python
_EXT_PARSERS: dict[str, type[WorkflowParser]] = {
    ".nf":        NextflowParser,
    ".smk":       SnakemakeParser,
    ".snakefile": SnakemakeParser,
}
```

Resolution order in `get_parser()` is:
1. Bare filename match (`Snakefile`, `Snakefile.py` — case-insensitive).
2. Extension match (`.nf`, `.smk`, `.snakefile`).
3. Default: `NextflowParser` — preserves all pre-Day-8 CLI behaviour for files
   with unrecognised or missing extensions.

The CLI uses the registry in the `parse`, `critic`, and `doctor` commands for
local file paths (the three `ParserRegistry().get_parser(path).parse_file(path)`
calls in `workflow_clinic/cli.py`). Remote-fetched content continues to use
`NextflowParser` directly because the Dockstore TRS descriptor type `"NFL"`
uniquely identifies the language — no extension inference is needed there.

Adding a third language (WDL) in a future iteration requires four steps:

1. Implement `WdlParser` in `workflow_clinic/parsers/wdl.py`, mapping WDL
   `task` blocks to `NextflowProcess`.
2. Add `".wdl": WdlParser` to `_EXT_PARSERS` in `registry.py`.
3. Add WDL fixtures under `tests/fixtures/wdl/`.
4. Write `tests/test_wdl_parser.py` and `tests/test_critic_wdl.py` mirroring
   the Snakemake test files.

No other files change.

**Resources:**
- [Refactoring Guru — Factory Method pattern](https://refactoring.guru/design-patterns/factory-method/python/example)
  — the `ParserRegistry` is a textbook factory method; this page shows the
  Python implementation with the exact dictionary-dispatch pattern used here.
- [Python `Path.suffix` and `Path.name`](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.suffix)
  — `path.suffix.lower()` and `path.name.lower()` are the two accessors used
  in `get_parser()`; the docs explain that `suffix` returns the empty string
  for bare filenames like `Snakefile`.
- [WDL task syntax](https://docs.openwdl.org/en/stable/WDL/task.html)
  and [CWL CommandLineTool](https://www.commonwl.org/v1.2/CommandLineTool.html)
  — the next two languages to add parsers for; their `task` and
  `CommandLineTool` blocks are the equivalents of Nextflow `process` and
  Snakemake `rule`.

---

## CONTAINER-003 — why it's needed and why it's MAJOR not CRITICAL

The rule lives in `workflow_clinic/critic/rules/containerization.py` as
`ContainerCondaIsolationRule`. It fires when `process.conda is not None` AND
`process.container is None`.

**Why not CRITICAL?** CONTAINER-001 (CRITICAL) covers "no containerisation at
all." CONTAINER-003 covers "some containerisation attempt, but insufficient for
cloud portability." A rule with a conda environment at least declares its
software dependencies — it is meaningfully better than nothing. MAJOR is the
correct severity because the workflow can still run locally but will fail or
produce non-reproducible results on cloud WES platforms:

- WES runners that mandate Docker/Singularity reject `conda:` rules outright.
- Conda environments depend on the host OS's glibc, kernel ABI, and system
  libraries. The same `environment.yaml` can resolve to different dependency
  trees on different cloud images.
- Even a perfectly pinned conda-lock file cannot guarantee reproducibility
  across OS versions — something a Singularity image can.

**The CONTAINER-001 guard — where it lives:**
```python
# workflow_clinic/critic/rules/containerization.py — ContainerMissingRule.check()
if process.conda is not None:
    return None   # defer to CONTAINER-003
```

This is the only line changed in `ContainerMissingRule`. For all Nextflow
processes `process.conda` is always `None` (the field defaulted to `None` when
added to `NextflowProcess`), so the guard is a no-op for Nextflow. The
regression test `test_nextflow_clean_still_scores_perfect_after_day8` in
`tests/test_critic_snakemake.py` enforces this invariant on every CI run.

**Resources:**
- [Snakemake — combining containers and conda](https://snakemake.readthedocs.io/en/stable/snakefiles/deployment.html#ad-hoc-combination-of-conda-package-management-with-containers)
  — Snakemake's own documentation on the `singularity + conda` pattern that
  CONTAINER-003 recommends; the page explicitly states that conda without a
  container is not suitable for reproducible cloud deployment.
- [Biocontainers registry](https://biocontainers.pro/)
  — the recommended source of pinned images that replace or wrap conda
  environments; the recommendation text in CONTAINER-003 links to this.
- [GA4GH WES spec — execution requirements](https://ga4gh.github.io/workflow-execution-service-schemas/docs/)
  — documents that WES implementations are required to support container-based
  execution; a rule using only `conda:` has no compliant execution path.

---

## Fixture design

### `tests/fixtures/snakemake/clean.smk` — expected 0 gaps, score 1.00

Both rules (`ALIGN`, `SORT_BAM`) have:
- Pinned `singularity:` image with a version-tagged Biocontainers URI
- `threads:` declaration
- `resources: mem_mb` declaration
- Explicit `input:` and `output:` blocks with parameterised paths
- `shell:` block using only `{input.*}` / `{output.*}` — no hardcoded paths

This fixture is the regression guard for `clean.nf`: if any new rule generates
a false positive on a conformant workflow, `test_clean_no_gaps` in
`tests/test_critic_snakemake.py` will catch it immediately.

### `tests/fixtures/snakemake/broken.smk` — expected ≤ 0.10 score, 9 gaps

| Rule          | ALIGN         | CALL_VARIANTS |
|---|---|---|
| CONTAINER-001 | ✓ CRITICAL    | ✓ CRITICAL    |
| STORAGE-001   | ✓ MAJOR       | —             |
| IO-001        | ✓ MAJOR       | ✓ MAJOR       |
| RESOURCE-001  | ✓ MINOR       | ✓ MINOR       |
| RESOURCE-002  | ✓ MINOR       | ✓ MINOR       |

Score: `1.0 − 2×0.25 − 3×0.10 − 4×0.03 = 0.08`

`CALL_VARIANTS` has no `output:` block, exactly mirroring `broken.nf` so the
same `IO-001` tests can be ported verbatim.

### `tests/fixtures/snakemake/partial.smk` — expected ≈ 0.62 score, 3 gaps

| Rule          | TRIM                           | FASTQC         |
|---|---|---|
| CONTAINER-003 | ✓ MAJOR (conda, no singularity) | —             |
| CONTAINER-001 | — (suppressed by conda guard)   | ✓ CRITICAL    |
| RESOURCE-002  | ✓ MINOR (no `mem_mb`)           | —             |

`partial.smk` is the most important fixture for CONTAINER-003 correctness:
TRIM proves that `003` fires and `001` does not; FASTQC proves the inverse.
This is the exact same "one good, one bad, one in-between" pattern established
by the three Nextflow fixtures in Day 1.

---

## Test strategy

Tests live in `tests/test_snakemake_parser.py` and `tests/test_critic_snakemake.py`.
They follow the same structural conventions as the Day 1 and Day 2 test files.

`test_snakemake_parser.py` is organised into four sections, one per fixture
plus one for `ParserRegistry` routing:
- **Clean** — asserts exact field values (`assert align.cpus == "4"`, not
  just truthiness) so any regex regression points to the specific field.
- **Broken** — asserts `None` on every field that should be absent.
- **Partial** — the critical `test_partial_conda_captured_on_trim` test;
  verifies that inline `conda:` on a single line is captured correctly.
- **ParserRegistry** — six routing tests including a case-insensitive
  `Snakefile` match and a round-trip comparison between direct instantiation
  and registry-resolved instantiation.

`tests/test_critic_snakemake.py` is organised into five sections:
- **Clean** — 5 negative tests (no false positives).
- **Broken** — 11 tests confirming all applicable rules fire.
- **Partial** — 8 tests verifying CONTAINER-003 / CONTAINER-001 interaction.
- **Regression** — `test_nextflow_clean_still_scores_perfect_after_day8`
  directly instantiates `NextflowParser` on `clean.nf` and asserts 0 gaps.
  This is the sentinel for the CONTAINER-001 modification.
- **CLI smoke tests** — 6 end-to-end tests through `CliRunner` that verify
  `ParserRegistry` is correctly wired into the `parse` and `critic` commands.
  `test_cli_critic_snakemake_json_is_valid` parses the full JSON output with
  `json.loads()`, catching any output-stream pollution (the same technique
  used in `tests/test_cli.py` from Day 3).

**Coverage after Day 8:**
```
workflow_clinic/parsers/snakemake.py   87%
workflow_clinic/parsers/registry.py   100%
workflow_clinic/critic/rules/containerization.py  97%
Overall                                91%
```

The 13% miss in `snakemake.py` is concentrated in two places:
- The `mem_gb` branch (line `proc.memory = f"{int(mg.group(1)) * 1024} MB"`)
  — no fixture currently uses `mem_gb`; adding a `partial.smk` rule with
  `mem_gb = 8` would cover it.
- The `notebook` and `wrapper` section keywords in `_RE_SECTION_HEADER` —
  valid Snakemake execution styles not represented in the current fixtures.

Both are defensive branches handled correctly but not exercised — the same
category as the EOF-without-closing-brace path in `nextflow.py` (flagged in
Day 1's test strategy).

**Resources:**
- [pytest documentation](https://docs.pytest.org/en/stable/)
- [Typer — testing guide](https://typer.tiangolo.com/tutorial/testing/)
  — the `CliRunner` pattern used in the CLI smoke tests in
  `tests/test_critic_snakemake.py`; inherited from Click's test runner.
- [pytest-cov documentation](https://pytest-cov.readthedocs.io/en/latest/)
  — the `--cov-fail-under=80` flag in `.github/workflows/ci.yml` that makes
  uncovered branches a CI failure; the "Miss" column in the coverage report
  shows the exact line numbers of the 13 uncovered lines in `snakemake.py`.

---

## What Day 9 builds on top of this

With two parsers sharing a common dataclass and the registry routing between
them, the remaining GSoC milestone languages follow the same four-step pattern:

1. Implement a parser in `workflow_clinic/parsers/{language}.py` that maps
   language-specific syntax into `NextflowProcess` fields.
2. Add `".{ext}": {Language}Parser` to `_EXT_PARSERS` in
   `workflow_clinic/parsers/registry.py`.
3. Add `clean`, `broken`, and `partial` fixtures under
   `tests/fixtures/{language}/`.
4. Write `tests/test_{language}_parser.py` and
   `tests/test_critic_{language}.py` mirroring the Snakemake test files.

Day 9 also adds the `GitHubClient` in `workflow_clinic/core/github_client.py`
that submits the issue drafts built by `--create-issue` in Day 7. The
`_render_github_issue()` function in `workflow_clinic/cli.py` already returns
`(title, body)` matching the `POST /repos/{owner}/{repo}/issues` request body
— Day 9 adds the HTTP call and a `--submit` flag without touching the rendering
logic.

**Resources:**
- [GA4GH WES spec — supported workflow types](https://ga4gh.github.io/workflow-execution-service-schemas/docs/#tag/Workflow-Runs/operation/RunWorkflow)
  — lists `NFL`, `SMK`, `CWL`, `WDL` as the standardised descriptor type
  strings; the parser registry extension order for Day 9+ follows this list.
- [GitHub REST API — create an issue](https://docs.github.com/en/rest/issues/issues?apiVersion=2022-11-28#create-an-issue)
  — the `title`, `body`, and `labels` fields that `_render_github_issue()` in
  `workflow_clinic/cli.py` already maps to; Day 9's `GitHubClient` will `POST`
  to this endpoint using the `httpx` client already present in the project.
- [PyGitHub documentation](https://pygithub.readthedocs.io/en/latest/)
  — the SDK mentioned in the project architecture doc for GitHub interaction;
  an alternative to raw `httpx` calls for the Day 9 client, depending on
  whether token-scoped authentication or fine-grained PAT support is required.