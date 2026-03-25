# Day 5 — The Workflow Doctor (MVP)

## What we built and why

Day 4 left us with a Critic that could reliably find gaps in real community
workflows and produce a `GapReport`. Day 5 answers the next question: can we
*fix* those gaps automatically?

The Workflow Doctor is the second core component of Workflow Clinic. It takes
a `GapReport` and, for every gap marked `auto_fixable`, attempts to generate a
concrete code change — a unified diff the developer can review and apply. For
`CONTAINER-001` (missing container directive), the fix strategy is:

1. Extract the process's script block from the source
2. Ask an LLM to suggest a specific, pinned public container image for the tools
   used in that script
3. Post-process the LLM response to strip any extraneous prose
4. Insert a `container '...'` directive at the correct position in the source
5. Re-parse the patched source to confirm the fix is syntactically valid
6. Return a `FixProposal` with the diff, confidence score, and validation result

By the end of Day 5 the full pipeline looks like this:

```
.nf file → NextflowParser → ParsedWorkflow
         → CriticEngine   → GapReport
         → DoctorEngine   → [FixProposal, FixProposal, ...]
         → CLI (terminal + optional JSON output)
```

The Doctor lives in `workflow_clinic/doctor/`.
The LLM client lives in `workflow_clinic/core/llm_client.py`.
The CLI command is `workflow-clinic doctor`.
Fix proposals can be saved as JSON with `--output`.

---

## New files introduced today

```
workflow_clinic/
├── core/
│   └── llm_client.py                    ← model-agnostic LLM wrapper with backoff
└── doctor/
    ├── __init__.py
    ├── engine.py                         ← DoctorEngine: runs all fix generators
    └── fix_generators/
        ├── __init__.py
        ├── base.py                       ← FixProposal dataclass + BaseFixGenerator ABC
        └── nextflow_fixes.py             ← ContainerMissingFixer (CONTAINER-001)
scripts/
└── collect_doctor_results.py            ← batch Doctor run against real workflows
tests/
└── test_doctor.py                       ← unit tests with mocked LLM calls
```

---

## The LLM client — design decisions

`workflow_clinic/core/llm_client.py` is a thin, model-agnostic wrapper. The key
design decisions are documented below, along with every bug encountered during
development.

### Fail at call time, not import time

If no API key is configured, `complete()` raises `EnvironmentError` when it is
first called, not when the module is imported. This means the entire tool —
`parse`, `critic`, fetching — works without any LLM key. The Doctor degrades
gracefully rather than breaking the whole CLI on import.

### Provider priority order

```python
def complete(self, prompt: str) -> str:
    if os.getenv("OLLAMA_MODEL"):
        return self._ollama(prompt)
    elif os.getenv("OPENAI_API_KEY"):
        return self._openai(prompt)
    elif os.getenv("ANTHROPIC_API_KEY"):
        return self._anthropic(prompt)
    elif os.getenv("GEMINI_API_KEY"):
        return self._gemini(prompt)
    else:
        raise EnvironmentError(...)
```

Ollama comes first because it is fully local and free — the right default for
an open source tool. The priority order also means that if multiple keys are
set, the first match wins.

### Bugs found and fixed during development

**Bug 1 — Gemini not reachable despite key being set.** The initial version of
`complete()` only checked `OPENAI_API_KEY` and `ANTHROPIC_API_KEY`. Adding
`_gemini()` to the class was not enough — it also needed to be wired into the
routing chain in `complete()`. This was found when `export GEMINI_API_KEY=...`
had no effect and the error still showed a 401 from the Anthropic endpoint.

**Bug 2 — ANTHROPIC_API_KEY silently shadowing GEMINI_API_KEY.** Even after
fixing the router, the doctor kept hitting the Anthropic endpoint and returning
401. The cause was `ANTHROPIC_API_KEY` still set in the shell from an earlier
session, appearing before `GEMINI_API_KEY` in the priority order. The fix was
`unset ANTHROPIC_API_KEY`. The lesson: always verify with `env | grep _KEY`
before debugging LLM failures. The priority order must be documented clearly so
users know which variable wins when multiple are set.

**Bug 3 — 429 rate limits on free-tier APIs.** The Doctor fires one LLM call
per auto-fixable gap. On the Gemini free tier (15 requests/minute), two
back-to-back calls for `broken.nf` hit the rate limit immediately. The fix was
a `_with_backoff` helper using full-jitter exponential backoff:

```python
def _with_backoff(fn, *, max_attempts: int = 4, base_delay: float = 2.0):
    for attempt in range(max_attempts):
        try:
            return fn()
        except httpx.HTTPStatusError as exc:
            if exc.response.status_code not in (429, 503):
                raise
            if attempt == max_attempts - 1:
                raise
            cap = base_delay * (2 ** attempt)
            delay = random.uniform(0, cap)
            time.sleep(delay)
```

Full-jitter (sleep between 0 and `base * 2^attempt` seconds) avoids the
thundering-herd problem that fixed-delay retry causes when multiple processes
hit the same limit simultaneously. Only 429 and 503 are retried; all other HTTP
errors (401 wrong key, 400 bad request) are re-raised immediately so genuine
failures are not silently swallowed.

**Bug 4 — Missing `_ollama` method.** The initial `complete()` checked for
`OLLAMA_MODEL` but `_ollama()` was never implemented, causing an `AttributeError`
for any user with Ollama configured. This was caught before release by reading
the routing logic carefully.

### Free and zero-card providers

The initial client only supported OpenAI and Anthropic. Three options were added
that require neither payment details nor a paid account:

- **Ollama** — fully local inference, no account, no rate limits, no cost.
  Recommended for local development and open-source CI.
- **Gemini free tier** — 1500 requests/day, requires only a Google account.
  Get a key at [aistudio.google.com](https://aistudio.google.com).
- **Groq free tier** — email signup only, runs Llama and Mixtral extremely fast
  on cloud hardware. The API is OpenAI-compatible.

For an open-source project, Ollama is the right default. Setup is three commands:

```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama pull phi3        # ~2GB, runs on CPU
export OLLAMA_MODEL=phi3
```

`OLLAMA_HOST` defaults to `http://localhost:11434` but can be overridden for a
remote Ollama instance (e.g. a GPU server on the local network) without code
changes. The timeout is 120 seconds because local models can be slow on first
load when weights are paged from disk; subsequent calls on the same model are fast.

**Resources:**
- [Ollama documentation](https://ollama.com/docs)
- [Google AI Studio — API key](https://aistudio.google.com)
- [AWS — exponential backoff and jitter](https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/)
  — the authoritative reference on why full-jitter beats fixed-delay retry.

---

## The FixProposal dataclass

Defined in `workflow_clinic/doctor/fix_generators/base.py`:

```python
@dataclass
class FixProposal:
    gap_id:                str
    process_name:          str
    description:           str    # one-line human summary
    unified_diff:          str    # ready to print or apply with `patch`
    validation_passed:     bool
    validation_output:     str
    confidence:            float  # 0.0–1.0
    human_review_required: bool
```

We use a plain `dataclass` here rather than Pydantic for the same reason the
parser models use dataclasses — `FixProposal` is an internal object produced and
consumed within the doctor pipeline. It crosses the module boundary only when
serialized to JSON for `--output`, handled explicitly with `dataclasses.asdict()`
in the CLI renderer.

`confidence` is set to `0.85` when the parser validates the fix successfully and
`0.4` when it cannot confirm. `0.85` reflects the empirical accuracy of LLM-
suggested Biocontainer images — they are usually the correct tool but
occasionally suggest non-existent version tags. This is why
`human_review_required` is `not validation_passed` — the parser can only confirm
the *syntax* is correct, not that the image exists on a registry.

---

## The BaseFixGenerator pattern

`BaseFixGenerator` in `workflow_clinic/doctor/fix_generators/base.py` is an
abstract class with exactly two methods:

```python
class BaseFixGenerator(ABC):
    @abstractmethod
    def can_fix(self, gap: Gap) -> bool:
        """Return True if this generator handles this gap_id."""

    @abstractmethod
    def fix(self, gap: Gap, source_lines: list[str]) -> FixProposal | None:
        """Generate a fix. Returns None if the attempt fails completely."""
```

This mirrors the `BaseRule` pattern from Day 2. The contract is deliberately
minimal: one gap in, one optional proposal out. The `DoctorEngine` loop is
trivial as a result:

```python
for gap in report.gaps:
    if not gap.auto_fixable:
        continue
    for generator in self._generators:
        if generator.can_fix(gap):
            result = generator.fix(gap, source_lines)
            if result is not None:
                proposals.append(result)
            break
```

Non-auto-fixable gaps are skipped entirely. The `break` after the first matching
generator prevents double-processing. Adding a new fix generator means writing
one class and adding one line to `_GENERATORS` in `engine.py`. Nothing else
changes.

**Resources:**
- [Python `abc` module](https://docs.python.org/3/library/abc.html)

---

## ContainerMissingFixer — the five-step pipeline

`ContainerMissingFixer` in `workflow_clinic/doctor/fix_generators/nextflow_fixes.py`
handles `CONTAINER-001`. Its `fix()` method runs five clearly separated steps.

### Step 1 — Extract the script block

```python
def _extract_script(self, gap: Gap, source_lines: list[str]) -> str:
    start = gap.location.line_start - 1
    end   = gap.location.line_end
    block = source_lines[start:end]
    in_script = False
    script_lines = []
    for line in block:
        if re.match(r"^\s*(script|shell|exec)\s*:\s*$", line):
            in_script = True
            continue
        if in_script:
            script_lines.append(line)
    return "".join(script_lines).strip()
```

The gap's `location.line_start` and `line_end` bound the process block. Within
that slice we look for the `script:` section header and collect everything after
it. Passing the actual shell commands to the LLM is essential — without them,
the model can only guess from the process name, which is ambiguous (`ALIGN`
could mean BWA, Bowtie2, STAR, or something else entirely). If no script block
is found, the prompt falls back to the process name alone.

### Step 2 — Prompt the LLM

```
You are a bioinformatics workflow expert. A Nextflow process is missing a container directive.

Process name: {process_name}

Script block:
{script}

Your task: suggest ONE specific, pinned, publicly available Docker image that
provides all the tools used in this script. Prefer Biocontainers or official
tool images. The image must have a specific version tag — never use :latest.

Reply with ONLY the image name and tag on a single line, nothing else.
Example reply: quay.io/biocontainers/bwa:0.7.17--h5bf99c6_8

Image:
```

`temperature: 0.1` is set on all providers to minimise variation. The prompt is
as constrained as possible: one line, no prose, a concrete format example.

### Step 3 — Post-process the LLM response

Smaller local models often append explanatory prose after the image name despite
the prompt instruction. During testing with phi3, the `CALL_VARIANTS` process
produced:

```
quay.io/gserviceinc/dna-genbank:gatk-3.4-v2, but ensure it is compatible with
the specific needs of your variant calling pipeline...
```

`_clean_image_response()` strips this by finding the first whitespace-delimited
token that contains both `:` and `/` — the minimal pattern for a valid
`registry/image:tag` string:

```python
for token in first_line.split():
    token = token.strip("',\"")
    if ":" in token and "/" in token:
        return token
```

This makes the Doctor usable with small local models without requiring a large
GPU-intensive one just to get clean output. Step 5 (validation) catches any
case where even this heuristic fails.

### Step 4 — Insert the directive

```python
def _insert_container(self, source_lines, process_name, image) -> list[str] | None:
    patched = list(source_lines)
    for i, line in enumerate(patched):
        m = _RE_PROCESS_OPEN.match(line)
        if m and m.group(1) == process_name:
            indent = "    "
            for j in range(i + 1, min(i + 5, len(patched))):
                stripped = patched[j].lstrip()
                if stripped:
                    indent = patched[j][: len(patched[j]) - len(stripped)]
                    break
            directive = f"{indent}container '{image}'\n"
            patched.insert(i + 1, directive)
            return patched
    return None
```

The regex `_RE_PROCESS_OPEN = re.compile(r"^\s*process\s+(\w+)\s*\{")` locates
the opening line of the named process. Inserting immediately after the opening
brace, with indentation inferred from the next non-empty line, means the new
line matches the existing file style rather than imposing a fixed indent.

Returning `None` is correct when the process block is not found — the Critic
found the process at parse time, but the source may have changed or the process
might be at an unexpected offset in a multi-file bundle. We surface this as a
`validation_passed=False` proposal rather than crashing.

### Step 5 — Validate by re-parsing

```python
def _validate(self, patched_source, process_name, image) -> tuple[bool, str]:
    workflow = self._parser.parse(patched_source)
    proc = next((p for p in workflow.processes if p.name == process_name), None)
    if proc is None:
        return False, "Process not found after patching."
    if proc.container != image:
        return False, f"Container directive present but value mismatch: ..."
    return True, "Parser confirmed container directive is present."
```

The patched source is fed back through `NextflowParser`. If the parser finds the
container directive and its value matches exactly what the LLM suggested,
`validation_passed=True`. If the LLM returned prose that slipped through Step 3,
the parser will fail to match the expected value — and we surface that as a low-
confidence proposal requiring human review rather than silently applying a broken
fix.

This is a purely syntactic check. It confirms the line was inserted correctly
but cannot confirm the Docker image actually exists on a registry.

**Resources:**
- [Python `difflib.unified_diff`](https://docs.python.org/3/library/difflib.html#difflib.unified_diff)
  — generates the standard unified diff format used by `git diff` and `patch`.

---

## LLM output quality — what we observed

Running the Doctor against `tests/fixtures/nextflow/broken.nf` with `phi3:latest`
via Ollama produced:

```
CONTAINER-001 — ALIGN
Fix:        Add container directive: 'quay.io/biocontainers/bwa-repair:0.7.42--ghfe3aec_4'
Confidence: 85%
Validated:  ✓ Parser confirmed container directive is present.

CONTAINER-001 — CALL_VARIANTS
Fix:        Add container directive: 'quay.io/gserviceinc/dna-genbank:gatk-3.4-v2'
Confidence: 85%
Validated:  ✓ Parser confirmed container directive is present.
```

**ALIGN:** `quay.io/biocontainers/bwa-repair:0.7.42` is plausible — BWA is the
correct tool for an alignment process and the version tag format matches
Biocontainers conventions. However `bwa-repair` rather than `bwa` suggests phi3
may have hallucinated a nearby package name. Syntactic validation passed but
registry existence is unverified.

**CALL_VARIANTS:** phi3 originally appended a long explanatory sentence after
the image name. `_clean_image_response()` extracted just the image token. The
GATK image reference is plausible — HaplotypeCaller is the tool being called —
but the registry prefix is not a standard Biocontainers path and warrants human
verification before applying.

The `confidence` score is identical for both proposals because it currently
derives from `validation_passed` alone, not from output quality. A future
improvement would additionally check that the extracted token matches the
`registry/image:tag` regex and that the registry domain is a known public one,
before awarding full confidence.

---

## Known limitation — image existence validation

The `_validate` method only checks syntactic correctness via the parser. It
cannot confirm the suggested image actually exists on a registry. The full
project should add a registry check:

```
GET https://biocontainers.pro/api/v1/containers/{tool}/
GET https://hub.docker.com/v2/repositories/{image}/tags/{tag}/
```

A 404 from either API means the image was hallucinated and `confidence` should
drop to `0.0` with `human_review_required=True`. This is marked as a TODO in
`nextflow_fixes.py`.

---

## The `--output` flag and JSON serialization

The `doctor` CLI command accepts `--output` / `-o` to save fix proposals as
JSON, mirroring the `--output` flag on `critic`:

```bash
workflow-clinic doctor tests/fixtures/nextflow/broken.nf \
  --gap CONTAINER-001 \
  --output results/doctor_broken.json
```

The output format mirrors the critic's `GapReport` style so the two report
types are consistent and can be compared side by side:

```json
{
  "schema_version": "0.1.0",
  "generated_at": "2026-03-25T...",
  "workflow_path": "tests/fixtures/nextflow/broken.nf",
  "proposals": [
    {
      "gap_id": "CONTAINER-001",
      "process_name": "ALIGN",
      "description": "Add container directive: 'quay.io/biocontainers/bwa:0.7.17'",
      "unified_diff": "--- ALIGN (original)\n+++ ...",
      "validation_passed": true,
      "validation_output": "Parser confirmed container directive is present.",
      "confidence": 0.85,
      "human_review_required": false
    }
  ],
  "summary": {
    "total_proposals": 2,
    "validated": 1,
    "human_review_required": 1,
    "avg_confidence": 0.63
  }
}
```

`FixProposal` is a plain `dataclass`, so serialization uses `dataclasses.asdict()`
rather than Pydantic's `model_dump`. The helpers `_serialize_proposals` and
`_render_doctor_json` live alongside the critic renderers in `workflow_clinic/cli.py`.

---

## collect_doctor_results.py

`scripts/collect_doctor_results.py` is the batch equivalent of
`scripts/collect_real_results.py` for the Doctor. It fetches each workflow,
runs the Critic, skips workflows with no auto-fixable gaps (avoiding LLM calls
on clean workflows like nf-core/rnaseq), runs the Doctor on the filtered gap
list, and saves proposals to `results/doctor_{slug}.json`.

```bash
export OLLAMA_MODEL=phi3
python scripts/collect_doctor_results.py
```

Only `CONTAINER-001` gaps are passed to the Doctor because that is the only gap
type with a registered fix generator. The filter will be relaxed as additional
generators are added.

---

## Test strategy

Tests live in `tests/test_doctor.py`. All LLM calls are mocked using
`@patch("workflow_clinic.doctor.fix_generators.nextflow_fixes.LLMClient")` —
the same `@patch` pattern used in `tests/test_fetcher.py` to mock `httpx.Client`.
Tests run in CI with no API key and complete in milliseconds.

The most important tests are the negative ones:

- `test_container_fixer_llm_failure_returns_failed_proposal` — if the LLM call
  raises any exception, a `FixProposal` with `confidence=0.0` is returned rather
  than propagating the exception. The Doctor never crashes the CLI.
- `test_container_fixer_unknown_process_returns_failed_proposal` — if the process
  name in the gap doesn't match anything in the source (e.g. a stale gap report),
  the fixer returns a failed proposal rather than silently doing nothing.
- `test_container_fixer_strips_prose_from_llm_response` — verifies that prose
  from a verbose model response is stripped by `_clean_image_response()` before
  the image name is inserted.

The existing 59 tests all continue to pass. The Doctor is purely additive — new
files and a new CLI command with no changes to the parser, rule engine, or schema.

**Resources:**
- [unittest.mock.patch](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch)
  — patching at the point of use (`nextflow_fixes.LLMClient`) rather than at
  the definition site, the same pattern as the fetcher tests.

---

## What Day 6 builds on top of this

Two improvements are clearly the right next steps based on what we observed today.

**Registry validation.** The Doctor validates syntactically — the parser confirms
the directive is present — but not semantically. A Biocontainers registry lookup
(`https://api.biocontainers.pro/ga4gh/trs/v2/tools`) would confirm the suggested
image actually exists before awarding full confidence, turning the Doctor's output
from "plausible" to "verified".

**Prompt hardening for small models.** `_clean_image_response()` is a heuristic.
A more robust approach adds a stronger negative example to the prompt
(`DO NOT add any explanation. Wrong: 'image:tag, but ensure...' Correct: 'image:tag'`)
and validates the extracted token against the `registry/image:tag` regex before
accepting it. This would make the Doctor fully reliable with the smallest local
models without requiring larger GPU-intensive ones.

Day 6 also adds a README, GitHub Actions CI, and the coverage improvements needed
to hit 80%+. The Doctor and Critic pipelines are functionally complete for
Nextflow at this point.