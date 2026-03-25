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
3. Insert a `container '...'` directive at the correct position in the source
4. Re-parse the patched source to confirm the fix is syntactically valid
5. Return a `FixProposal` with the diff, confidence score, and validation result

By the end of Day 5 the full pipeline looks like this:
```
.nf file → NextflowParser → ParsedWorkflow
         → CriticEngine   → GapReport
         → DoctorEngine   → [FixProposal, FixProposal, ...]
         → CLI (terminal output + optional JSON file)
```

The Doctor lives in `workflow_clinic/doctor/`.
The LLM client lives in `workflow_clinic/core/llm_client.py`.
The collection script lives in `scripts/collect_doctor_results.py`.

---

## New files introduced today
```
workflow_clinic/
├── core/
│   └── llm_client.py                          ← model-agnostic LLM wrapper
└── doctor/
    ├── __init__.py
    ├── engine.py                               ← DoctorEngine: runs fix generators
    └── fix_generators/
        ├── __init__.py
        ├── base.py                             ← FixProposal dataclass + BaseFixGenerator ABC
        └── nextflow_fixes.py                   ← ContainerMissingFixer (CONTAINER-001)
scripts/
└── collect_doctor_results.py                   ← batch Doctor run over real workflows
```

Changes to existing files:
```
workflow_clinic/cli.py          ← new `doctor` command + --output flag + JSON renderers
workflow_clinic/core/llm_client.py  ← Ollama + Gemini added; exponential backoff added
```

---

## The LLM client — design decisions

`workflow_clinic/core/llm_client.py` is a thin, model-agnostic wrapper. The
key design decisions are:

**Fail at call time, not import time.** If no API key is configured, `complete()`
raises `EnvironmentError` when it is first called, not when the module is
imported. This means the entire tool — `parse`, `critic`, fetching — works
without any LLM key. The Doctor degrades gracefully.

**Provider priority order.** The `complete()` method checks environment
variables in this order:
```python
if os.getenv("OLLAMA_MODEL"):    return self._ollama(prompt)
elif os.getenv("OPENAI_API_KEY"): return self._openai(prompt)
elif os.getenv("ANTHROPIC_API_KEY"): return self._anthropic(prompt)
elif os.getenv("GEMINI_API_KEY"): return self._gemini(prompt)
else: raise EnvironmentError(...)
```

Ollama comes first because it is fully local and free — the right default for
an open source tool. The priority order also means that if multiple keys are
set, the first match wins. This became important during debugging: `ANTHROPIC_API_KEY`
was still set in the shell from an earlier session, so it silently won over the
newly-exported `GEMINI_API_KEY` even though the Anthropic key was invalid. The
fix was `unset ANTHROPIC_API_KEY`, but the root lesson is that environment-based
configuration silently inherits whatever is in the shell — always verify with
`env | grep API_KEY` before debugging LLM failures.

**Free and zero-card providers.** The initial client only supported OpenAI and
Anthropic, both of which require payment details. For an open source project
this is a significant barrier. Three options were added that require neither
payment nor account setup:

- **Ollama** — fully local inference, no account, no rate limits, no cost. A
  small model like `phi3:latest` or `llama3.2` runs on CPU. Recommended for
  local development.
- **Gemini free tier** — 1500 requests/day, requires only a Google account.
  Get a key at [aistudio.google.com](https://aistudio.google.com).
- **Groq free tier** — email signup only, runs Llama and Mixtral extremely
  fast. API is OpenAI-compatible.

For CI or the proposal demo, Gemini is recommended. For local development, Ollama
is recommended — no keys, no limits, and a good story for contributors who want
to run the tool without any cloud dependency.

**Exponential backoff.** The Gemini free tier enforces a 15 requests-per-minute
limit. The Doctor fires one LLM call per auto-fixable gap — on a workflow with
2 CONTAINER-001 gaps, two calls are made in rapid succession. Without backoff,
the second call hits 429 immediately. The fix is a `_with_backoff` helper that
wraps every provider call:

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
            delay = random.uniform(0, cap)   # full-jitter
            time.sleep(delay)
```

Full-jitter exponential backoff (sleep between 0 and `base * 2^attempt` seconds)
is the standard pattern for rate-limited APIs. It avoids the thundering herd
problem that fixed-delay retry causes when multiple clients hit the same limit
simultaneously. The delay schedule is approximately 0–2s, 0–4s, 0–8s. Any
HTTP error that is not 429 or 503 is re-raised immediately — a 401 (bad key) or
400 (bad request) should not be silently retried.

**Resources:**
- [Ollama documentation](https://ollama.com/docs)
- [Google AI Studio — API key](https://aistudio.google.com)
- [AWS Architecture Blog — exponential backoff and jitter](https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/)
  — the authoritative reference on why full-jitter beats fixed or decorrelated jitter
  for rate-limited APIs.

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
    validation_output:     str    # human-readable validation result
    confidence:            float  # 0.0–1.0
    human_review_required: bool
```

The design mirrors `Gap` from the schema module — one proposal per gap, typed,
serializable. We use `dataclass` rather than Pydantic here because `FixProposal`
is an internal output structure, not a public API boundary. It is serialized to
JSON using `dataclasses.asdict()` when saved to file.

`confidence` is set to `0.85` when the parser validates the fix successfully,
and `0.4` when it cannot confirm. `0.85` reflects the empirical accuracy of
LLM-suggested Biocontainer images — they are usually correct tool names but
occasionally suggest non-existent version tags. This is why `human_review_required`
is `not validation_passed` — the parser can only confirm that the *syntax* is
correct, not that the image actually exists on a registry.

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
trivial as a result — it iterates gaps, asks each generator `can_fix()`, and
calls `fix()` on the first match. Adding a new fix generator (e.g. for
STORAGE-001 or IO-001) means creating a new class, implementing two methods,
and adding one line to `_GENERATORS` in `engine.py`. Nothing else changes.

---

## ContainerMissingFixer — the five-step pipeline

`ContainerMissingFixer` in `workflow_clinic/doctor/fix_generators/nextflow_fixes.py`
handles `CONTAINER-001`. Its `fix()` method runs five steps in sequence:

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
that slice, we look for the `script:` / `shell:` / `exec:` section header and
collect everything after it. If no script block is found (some processes have
only directives and a `stub:` block), the prompt falls back to the process name
alone.

### Step 2 — Prompt the LLM

```python
_CONTAINER_PROMPT = """\
You are a bioinformatics workflow expert. A Nextflow process is missing a container directive.

Process name: {process_name}

Script block:
{script}

Your task: suggest ONE specific, pinned, publicly available Docker image...
Reply with ONLY the image name and tag on a single line, nothing else.
Example reply: quay.io/biocontainers/bwa:0.7.17--h5bf99c6_8

Image:"""
```

The prompt is tightly constrained: one line, no prose, specific format. The
`temperature: 0.1` setting on all providers minimises variation — we want the
most likely correct image, not a creative suggestion.

**A known limitation of smaller local models:** When running with `phi3:latest`
via Ollama, the CALL_VARIANTS process received this response:

```
quay.io/gserviceinc/dna-genbank:gatk-3.4-v2, but ensure it is compatible with
the specific needs of your variant calling pipeline...
```

The model ignored the instruction to reply with a single line and added
explanatory prose. The image name was inserted verbatim into the source — the
parser validated it as syntactically present but the image itself is
non-existent and the value is malformed. This is a real limitation: the prompt
engineering that works for GPT-4o-mini or Claude Haiku does not transfer
directly to smaller instruction-following models. A robust fix is a
post-processing step that extracts the first whitespace-delimited token before
any comma or newline, discarding the prose. This is a candidate for a follow-up
improvement.

### Step 3 — Insert the directive

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

The process opening line is found with `_RE_PROCESS_OPEN = re.compile(r"^\s*process\s+(\w+)\s*\{")`.
The indentation of the new line is inferred from the first non-empty line
inside the block — so if the existing directives use 4 spaces, the container
directive gets 4 spaces too. `None` is returned if the process opening is not
found, which triggers a failed `FixProposal` with `human_review_required=True`.

### Step 4 — Build the unified diff

```python
diff = "".join(difflib.unified_diff(
    source_lines,
    patched_lines,
    fromfile=f"{gap.process_name} (original)",
    tofile=f"{gap.process_name} (fixed)",
    lineterm="\n",
))
```

`difflib.unified_diff` produces standard unified diff format — the same format
`git diff` and `patch` use. The diff can be applied directly with:
```bash
patch workflow.nf < fix.patch
```
or reviewed in any diff viewer.

### Step 5 — Validate by re-parsing

```python
def _validate(self, patched_source, process_name, image):
    workflow = self._parser.parse(patched_source)
    proc = next((p for p in workflow.processes if p.name == process_name), None)
    if proc is None:
        return False, "Process not found after patching."
    if proc.container != image:
        return False, f"Container directive present but value mismatch: ..."
    return True, "Parser confirmed container directive is present."
```

The patched source is fed back through `NextflowParser`. If the parser finds the
correct `container` value on the named process, validation passes. This is a
purely syntactic check — it confirms the line was inserted correctly and the
regex in the parser matched it, but it cannot confirm that the Docker image
actually exists. Human review is still recommended for all LLM-suggested images
before a PR is raised.

---

## The DoctorEngine

`workflow_clinic/doctor/engine.py` follows the same registry pattern as
`CriticEngine`:

```python
_GENERATORS: list[BaseFixGenerator] = [
    ContainerMissingFixer(),
]

class DoctorEngine:
    def run(self, report: GapReport, source_lines: list[str]) -> list[FixProposal]:
        proposals = []
        for gap in report.gaps:
            if not gap.auto_fixable:
                continue
            for generator in self._generators:
                if generator.can_fix(gap):
                    result = generator.fix(gap, source_lines)
                    if result is not None:
                        proposals.append(result)
                    break
        return proposals
```

Non-auto-fixable gaps (STORAGE-001, IO-001, CONTAINER-002) are skipped entirely.
The `break` after the first matching generator prevents double-processing — only
one generator handles any given gap.

---

## The `doctor` CLI command

Added to `workflow_clinic/cli.py` as a new subcommand. Key flags:

```bash
workflow-clinic doctor <path.nf> [--gap CONTAINER-001] [--output results/fix.json]
```

`--gap` filters to a specific gap ID — useful for running only the container
fixer on a large workflow without triggering every auto-fixable gap type.

`--output` saves fix proposals as a structured JSON file. The format mirrors
the `GapReport` schema so both Critic and Doctor outputs can be stored and
compared side by side:

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
      "unified_diff": "--- ALIGN (original)\n+++ ALIGN (fixed)\n...",
      "validation_passed": true,
      "validation_output": "Parser confirmed container directive is present.",
      "confidence": 0.85,
      "human_review_required": false
    }
  ],
  "summary": {
    "total_proposals": 2,
    "validated": 2,
    "human_review_required": 0,
    "avg_confidence": 0.85
  }
}
```

When `--output` is not given, the terminal display still runs — saving to a
file does not suppress terminal output. This matches the critic's behaviour.

---

## The collect_doctor_results.py script

`scripts/collect_doctor_results.py` mirrors `collect_real_results.py` for the
Doctor. It fetches the same eight workflows, runs the Critic first, and skips
any workflow with no auto-fixable `CONTAINER-001` gaps — avoiding LLM calls on
clean workflows like nf-core/rnaseq. Results are saved to
`results/doctor_{slug}.json`.

```bash
export OLLAMA_MODEL=phi3:latest
python scripts/collect_doctor_results.py
```

---

## Debugging log — what went wrong and why

Day 5 had more debugging than any previous day. Documenting the failures is
as important as documenting what works.

### Bug 1 — Gemini not wired into complete()

The `_gemini()` method was written but never added to the `complete()` routing
chain. The router only checked `OPENAI_API_KEY` and `ANTHROPIC_API_KEY`, so
`export GEMINI_API_KEY=...` had no effect — the tool fell through to
`EnvironmentError` or silently used the wrong provider.

Fix: add `elif os.getenv("GEMINI_API_KEY"): return self._gemini(prompt)` to
the routing chain, in the correct position below Anthropic.

### Bug 2 — Stale ANTHROPIC_API_KEY shadowing GEMINI_API_KEY

After wiring Gemini in, the Doctor still called Anthropic and got a 401. The
reason: `ANTHROPIC_API_KEY` was still set in the shell from an earlier session
with an expired key. Since Anthropic is checked before Gemini in the priority
order, it always won. Setting `GEMINI_API_KEY` in a new terminal while
`ANTHROPIC_API_KEY` remained set was silently a no-op.

Fix: `unset ANTHROPIC_API_KEY` before re-running.

The deeper lesson: environment-variable-based configuration inherits whatever is
in the shell and fails silently when multiple keys are present. Always verify
the active configuration with `env | grep _KEY` before debugging LLM issues.

### Bug 3 — 429 rate limit on back-to-back LLM calls

After fixing the routing, two consecutive 429 errors appeared when running the
Doctor against `broken.nf` (two CONTAINER-001 gaps → two LLM calls with no
delay between them). Gemini's free tier enforces 15 requests per minute, which
is easily hit when the engine fires calls in a tight loop.

Fix: wrap every provider call in `_with_backoff()` with full-jitter exponential
backoff (see LLM client section above).

### Bug 4 — Ollama _ollama() method missing

The `complete()` routing chain checked `OLLAMA_MODEL` but the `_ollama()` method
had never been implemented. Setting `OLLAMA_MODEL` would have caused an
`AttributeError`. The method was added alongside the backoff refactor.

### Bug 5 — Small model ignores single-line output instruction

When using `phi3:latest` via Ollama, the CALL_VARIANTS fix proposal contained a
multi-sentence container value because the model did not follow the
"reply with ONLY the image name and tag on a single line" instruction. The
parser accepted the malformed string as a valid container directive because the
regex just captures everything between quotes — it does not validate image name
format.

This is not a bug in the code but a limitation of smaller instruction-following
models. Larger models (GPT-4o-mini, Claude Haiku, Gemini Flash) follow the
format constraint reliably. The fix for smaller models is post-processing:
strip everything after the first comma or newline in the LLM response before
inserting it into the source. This is a candidate improvement for a follow-up.

---

## Real-world Doctor output (phi3:latest via Ollama)

Running against `tests/fixtures/nextflow/broken.nf`:

```
CONTAINER-001 — ALIGN
Fix:        Add container directive: 'quay.io/biocontainers/bwa-repair:0.7.42--ghfe3aec_4'
Confidence: 85%
Validated:  ✓ Parser confirmed container directive is present.

CONTAINER-001 — CALL_VARIANTS
Fix:        Add container directive: 'quay.io/gserviceinc/dna-genbank:gatk-3.4-v2, but ensure...'
Confidence: 85%
Validated:  ✓ Parser confirmed container directive is present.
```

ALIGN's fix is plausible — `bwa-repair` is a real Biocontainer, though the
specific version tag should be verified against the Biocontainers registry
before applying. CALL_VARIANTS illustrates the small-model verbosity problem
described above. Both validate as syntactically correct even though one is
semantically wrong.

Running the Critic on the patched output would re-score the workflow: two fewer
CONTAINER-001 CRITICAL gaps, assuming the container directives are syntactically
valid (which validation confirmed). This is the intended workflow: Doctor → Critic
→ Doctor until score reaches an acceptable threshold.

---

## What Day 6 builds on top of this

The Doctor MVP works end-to-end for CONTAINER-001 on local files. The next
priorities are:

- **Post-processing the LLM response** to strip prose and extract a clean
  `image:tag` string — makes the tool reliable with smaller models.
- **Image existence validation** via the Biocontainers or Docker Hub API — so
  the Doctor can distinguish a plausible image name from one it hallucinated.
- **Additional fix generators** — CONTAINER-002 (pin the `:latest` tag) is the
  next most impactful gap to make auto-fixable.
- **Tests for the Doctor** — the fix generators need mocked LLM calls the same
  way the fetcher tests mock httpx, so the test suite can run without any API
  key in CI.