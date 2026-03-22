# Day 2 — Rule Engine (Critic, Deterministic)

## What we built and why

Day 1 gave us a structured representation of what's inside a Nextflow workflow.
Day 2 answers the next question: given that representation, what's *wrong* with
it from a cloud-readiness perspective?

The rule engine is the core of the Workflow Critic. It takes a `ParsedWorkflow`
object from the parser, runs every registered rule against each process, and
returns a `GapReport` — a structured, typed document describing every problem
found, where it is, how severe it is, and what to do about it.

By the end of Day 2 the pipeline looks like this:
```
.nf file → NextflowParser → ParsedWorkflow → CriticEngine → GapReport
```

Everything from here — the CLI output, the JSON report, the GitHub issues, the
Doctor's fix proposals — is built on top of that `GapReport`.

---

## New files introduced today
```
workflow_clinic/
├── schema/
│   ├── __init__.py
│   └── gap_report.py        ← Pydantic models: Gap, GapReport, GapSummary
├── critic/
│   ├── __init__.py
│   ├── engine.py            ← CriticEngine: runs all rules, builds GapReport
│   └── rules/
│       ├── __init__.py
│       ├── base.py          ← Abstract BaseRule every rule inherits from
│       ├── containerization.py  ← CONTAINER-001, CONTAINER-002
│       ├── storage.py           ← STORAGE-001
│       └── io_declaration.py    ← IO-001
tests/
└── test_critic_engine.py    ← 17 new tests on top of the 14 from Day 1
```

---

## Why Pydantic for the schema and not dataclasses?

In Day 1 we used Python `dataclasses` for the parser models (`NextflowProcess`,
`ParsedWorkflow`). Here we switch to **Pydantic** for `Gap`, `GapReport`, and
`GapSummary`. The reason is the boundary these models sit at.

Parser models are internal — they are created and consumed entirely inside the
parser module. No one outside needs to validate them or serialize them to JSON.
Dataclasses are enough.

Gap reports are external. They get printed to the terminal, written to files,
sent to GitHub as issue bodies, and eventually fed to the Doctor agent. Pydantic
gives us three things dataclasses don't:

- **Runtime validation** — if a rule accidentally sets `severity` to a string
  that isn't a valid `Severity` enum value, Pydantic raises a clear error
  immediately rather than silently passing bad data downstream.
- **Free JSON serialization** — `report.model_dump(mode="json")` gives us a
  clean, standards-compliant JSON document with no extra code. You saw this
  working in the sanity check at the end of Day 2.
- **Schema documentation** — the Pydantic model *is* the schema. Anyone reading
  `gap_report.py` knows exactly what a gap report contains and what types every
  field must be.

**Resources:**
- [Pydantic v2 documentation](https://docs.pydantic.dev/latest/)
- [Pydantic `BaseModel` reference](https://docs.pydantic.dev/latest/api/base_model/)
  — specifically `model_dump(mode="json")` which we use for serialization.
- [Real Python — Pydantic guide](https://realpython.com/python-pydantic/)

---

## The schema models — what each one does

All models live in `workflow_clinic/schema/gap_report.py`.

**`Severity`** — an enum with four levels: `CRITICAL`, `MAJOR`, `MINOR`, `INFO`.
Using an enum rather than a plain string means a typo like `"CRITCAL"` is caught
at the point the `Gap` is constructed, not somewhere downstream when someone
tries to compare it.

**`GapCategory`** — an enum grouping gaps by type: `CONTAINERIZATION`,
`STORAGE`, `IO_DECLARATION`, `RESOURCE_HINTS`, `REPRODUCIBILITY`, `METADATA`.
These map directly to the six portability blocker categories identified in the
proposal. Only three categories have rules today; the others will be filled in
as the project grows.

**`CodeLocation`** — the file path plus `line_start` and `line_end` from the
parsed process. This is what lets the tool tell a user *exactly* where in their
file a problem is, rather than just that a problem exists.

**`Gap`** — the core unit. One `Gap` = one problem in one process. The fields
that matter most:
- `gap_id`: a stable identifier like `"CONTAINER-001"` that can be used to
  deduplicate GitHub issues and link fixes back to the original finding.
- `evidence`: the offending line(s) verbatim, so the issue body shows the
  user their own code back to them.
- `auto_fixable`: whether the Doctor (Day 5) can attempt a fix. Set to `True`
  only for gaps where we're confident a programmatic fix is safe.

**`GapSummary`** — aggregate counts plus the `cloud_readiness_score`. The score
is computed in `engine.py` using severity penalties (see below). It gives a
single number that can be tracked over time as fixes are applied.

**`GapReport`** — the top-level document. Wraps everything with a timestamp,
the workflow path, and a schema version so future format changes are detectable.

---

## The rule design — BaseRule and why we use inheritance

Every rule in `workflow_clinic/critic/rules/` inherits from `BaseRule` defined
in `workflow_clinic/critic/rules/base.py`. `BaseRule` is an abstract class with
one abstract method:
```python
def check(self, process: NextflowProcess, file_path: str) -> Gap | None:
```

This contract — one process in, one optional gap out — is deliberately simple.
It means:

- Rules are completely independent. `ContainerMissingRule` knows nothing about
  `HardcodedPathRule`. You can add, remove, or reorder rules without touching
  any other rule.
- The engine loop in `engine.py` is trivial — it just calls `rule.check()` for
  every (process, rule) combination and collects the non-None results.
- Testing is trivial — you can test each rule in complete isolation by passing
  it a hand-crafted `NextflowProcess` object.

Adding a new rule in the future means: create a new file in
`workflow_clinic/critic/rules/`, write a class that inherits `BaseRule`,
implement `check()`, and add an instance to the `_RULES` list in `engine.py`.
Nothing else needs to change.

**Resources:**
- [Python `abc` module — Abstract Base Classes](https://docs.python.org/3/library/abc.html)
- [Real Python — Abstract Base Classes](https://realpython.com/python-interface/)
  — explains why `ABC` + `@abstractmethod` is preferable to duck typing when
  you want to enforce an interface across multiple implementations.

---

## The four rules implemented today

All rules live in `workflow_clinic/critic/rules/`.

### CONTAINER-001 — `ContainerMissingRule` (`containerization.py`)
Checks `process.container is None`. If the parser found no container directive,
this fires as `CRITICAL`. It is marked `auto_fixable=True` because the Doctor
can suggest a pinned image based on what the script block calls.

### CONTAINER-002 — `ContainerLatestTagRule` (`containerization.py`)
Only runs if a container directive *exists* (so it never double-fires with
CONTAINER-001). Uses the regex `_RE_HAS_TAG = re.compile(r".+:.+")` to check
whether the image has a non-latest tag. If the tag is `latest` or absent, this
fires as `MAJOR` under `REPRODUCIBILITY` rather than `CONTAINERIZATION` —
because the problem isn't portability, it's reproducibility. The same image
name can resolve to different code over time.

### STORAGE-001 — `HardcodedPathRule` (`storage.py`)
Scans `process.script.raw` with:
```python
_RE_HARDCODED_PATH = re.compile(r'(?<!\$\{)["\']?(/[\w/.\-]+)')
```
The `(?<!\$\{)` is a negative lookbehind — it prevents matching Nextflow
variable substitutions like `${params.reference}` which start with `${` and
are fine. Anything else starting with `/` is a hardcoded path. The evidence
field shows up to 3 matching paths so the issue body doesn't become a wall of
text for badly written scripts.

### IO-001 — `UndeclaredOutputRule` (`io_declaration.py`)
Checks `process.output.raw` — the string we collected from the `output:` block
during parsing. If it's empty (either no block at all, or an empty block),
this fires as `MAJOR`. Without explicit outputs, no downstream process can
consume this process's results and no workflow engine can validate the run.

**Resources:**
- [Negative lookbehind in Python regex](https://docs.python.org/3/library/re.html#re.Pattern.match)
  — the `(?<!...)` syntax used in `_RE_HARDCODED_PATH`.
- [regex101.com](https://regex101.com) — paste `(?<!\$\{)["\']?(/[\w/.\-]+)`
  with a sample script block to see exactly what it matches and misses.
- [Nextflow process output docs](https://www.nextflow.io/docs/latest/process.html#output)
  — explains why output declarations are mandatory for portable pipelines.

---

## The CriticEngine — how it wires everything together

`workflow_clinic/critic/engine.py` is intentionally short. The main loop is:
```python
for process in workflow.processes:
    for rule in self._rules:
        result = rule.check(process, file_path)
        if result is not None:
            gaps.append(result)
```

That's it. The engine doesn't know what any rule does — it just calls `check()`
and collects results. This is the payoff of the `BaseRule` design: the engine
stays simple no matter how many rules are added.

The `_RULES` list at the top of `engine.py` is the single place where rules are
registered. Adding a new rule to the project means adding one line there.

The `CriticEngine.__init__` accepts an optional `rules` argument to allow
injecting a custom list in tests — this means you can test the engine with a
single rule in isolation without running every rule at once.

---

## Cloud readiness score

The score in `GapSummary.cloud_readiness_score` is computed in `_compute_score`
in `engine.py`:
```python
_SEVERITY_PENALTY = {
    Severity.CRITICAL: 0.25,
    Severity.MAJOR:    0.10,
    Severity.MINOR:    0.03,
    Severity.INFO:     0.01,
}

def _compute_score(gaps):
    penalty = sum(_SEVERITY_PENALTY.get(g.severity, 0.0) for g in gaps)
    return round(max(0.0, 1.0 - penalty), 2)
```

Start at 1.0, subtract a fixed penalty per gap based on its severity, floor at
0.0. The `broken.nf` workflow — 2 CRITICAL + 3 MAJOR gaps — scores 0.20, which
is visible in the sanity check output above. A clean workflow scores 1.0.

This is intentionally simple for the POC. A more sophisticated version would
weight by category (missing containers are worse than missing metadata) and
normalise by process count so large workflows aren't unfairly penalised.

---

## Test strategy

Tests live in `tests/test_critic_engine.py`. The structure mirrors Day 1 —
one section per fixture, testing both that gaps fire when they should and that
they stay silent when they shouldn't. The most important tests are the
*negative* ones:

- `test_clean_no_gaps` — the rule engine produces zero gaps on a correct
  workflow. If this ever fails it means a rule is generating false positives,
  which is worse than missing a real gap.
- `test_partial_latest_tag_does_not_fire_on_fastqc` — CONTAINER-002 must not
  fire on a process that has no container at all. CONTAINER-001 handles that
  case; firing both would be a duplicate report.

Coverage after Day 2: 85% overall, 97% on the parser, 100% on the engine and
schema. The 2 missed lines in `storage.py` are the `... (X more)` truncation
branch which only triggers with more than 3 hardcoded paths in a single script
block — an edge case we handle defensively but haven't written a fixture for yet.

**Resources:**
- [pytest documentation](https://docs.pytest.org/en/stable/)
- [Testing with pytest — negative test cases](https://realpython.com/pytest-python-testing/#what-makes-pytest-so-useful)
  — why testing that something does *not* happen is as important as testing
  that it does.

---

## What Day 3 builds on top of this

Day 3 wires the parser and engine into the CLI so `workflow-clinic critic
path/to/workflow.nf` produces a real gap report in the terminal and optionally
writes it as JSON. The `GapReport` model we built today serializes directly
via `model_dump(mode="json")` — the CLI just needs to format and display it.