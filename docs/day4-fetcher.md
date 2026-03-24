# Day 4 — Live Workflow Fetching from Dockstore

## What we built and why

Days 1–3 gave us a fully working Critic pipeline, but it only ran against local
files. Day 4 makes the tool useful in the real world — point it at a Dockstore
identifier or a GitHub URL and it fetches the workflow and runs the full Critic
pipeline against it without any manual downloading.

By the end of Day 4 the full flow looks like this:
```
Dockstore TRS URL         ─┐
GitHub URL                 ├─→ Fetcher → raw .nf content → NextflowParser
Local .nf file            ─┘               → ParsedWorkflow → CriticEngine → GapReport
```

The fetcher lives in `workflow_clinic/core/fetcher.py`.
The tests live in `tests/test_fetcher.py`.
The real-world collection script lives in `scripts/collect_real_results.py`.
The gap reports from real workflows live in `results/`.

---

## New files introduced today
```
workflow_clinic/
└── core/
    ├── __init__.py
    └── fetcher.py          ← FetchedWorkflow dataclass + fetch() router
scripts/
└── collect_real_results.py ← runs Critic against 5 real Dockstore workflows
results/
└── nf-core_*.json          ← real gap reports saved as evidence
```

---

## Why httpx and not requests?

`requests` is the most widely known Python HTTP library but it is synchronous
only. `httpx` is a modern drop-in replacement that is synchronous by default
but also supports async — which matters because Day 5 may need to fetch multiple
workflow files concurrently (modules, subworkflows) without blocking. Switching
from sync to async in httpx is a one-line change; switching away from `requests`
entirely would require a rewrite. We pay nothing extra for this flexibility now.

**Resources:**
- [httpx documentation](https://www.python-httpx.org/)
- [httpx vs requests](https://www.python-httpx.org/compatibility/)
  — explains where httpx is a drop-in and where it differs from requests.

---

## The FetchedWorkflow dataclass

Defined at the top of `workflow_clinic/core/fetcher.py`:
```python
@dataclass
class FetchedWorkflow:
    source:   str   # original identifier, for display and report metadata
    filename: str   # suggested filename (e.g. "main.nf")
    content:  str   # raw file content
```

The fetcher always returns this object regardless of where the workflow came
from. The CLI and parser never need to know whether the content came from
Dockstore, GitHub, or a local file — they just receive a string. This is the
same principle as Day 1's `DirectiveBlock` — hide the complexity of acquisition
behind a clean, typed boundary.

---

## The fetch() router

`fetch()` in `workflow_clinic/core/fetcher.py` is a single public entry point
that inspects the source string and routes to the correct fetcher:
```python
if source.startswith("dockstore:"):
    return _fetch_dockstore(source)
elif "github.com" in source or source.startswith("github:"):
    return _fetch_github(source)
else:
    raise ValueError(...)
```

This pattern — a public router over private implementation functions — keeps
the caller's code simple while allowing each fetcher to grow independently.
Adding a WorkflowHub fetcher in the future means adding one `elif` branch and
one private function, nothing else changes.

---

## The Dockstore fetcher

The Dockstore fetcher in `_fetch_dockstore()` uses the GA4GH TRS v2 API, which
is the same API that Workflow Clinic is ultimately designed to support. Two API
calls are made:

**Call 1 — tool metadata:**
```
GET /ga4gh/trs/v2/tools/{encoded_id}
```
Returns the tool record including all registered versions. The tool ID is
`#workflow/github.com/owner/repo`, URL-encoded. We use `urllib.parse.quote()`
with `safe=""` to encode the `#` and `/` characters correctly.

**Call 2 — primary descriptor:**
```
GET /ga4gh/trs/v2/tools/{id}/versions/{version_id}/NFL/descriptor
```
Returns the raw content of the primary workflow file for that version.

### Two bugs we hit and fixed

**Bug 1 — wrong descriptor type string.** The TRS v2 spec uses `"NFL"` as the
descriptor type identifier for Nextflow, not `"NEXTFLOW"`. Using the wrong
string returned a 400 error from the Dockstore API. This was found by reading
the Dockstore TRS v2 API docs and cross-referencing with the actual API response.

**Bug 2 — dev branches have no descriptor.** Dockstore returns versions in an
unpredictable order and `dev`, `preview`, and `TEMPLATE` branches frequently
have no associated descriptor file, causing another 400. The fix was a version
filter that prefers release tags over branch names:
```python
def _is_release(v: dict) -> bool:
    name = v.get("name", "")
    return (
        not name.startswith("dev")
        and not name.startswith("preview")
        and not name.startswith("TEMPLATE")
        and name != "master"
        and name != "main"
    )
```

**Resources:**
- [GA4GH TRS v2 API specification](https://ga4gh.github.io/tool-registry-service-schemas/GeneratedOpenAPIDoc/)
  — the official spec; the descriptor type strings (`NFL`, `CWL`, `WDL`, etc.)
  are defined here.
- [Dockstore TRS API docs](https://dockstore.org/api/static/swagger-ui/index.html)
  — Dockstore's live Swagger UI; use this to explore endpoints interactively
  and check what a real response looks like before writing code against it.
- [Python urllib.parse.quote](https://docs.python.org/3/library/urllib.parse.html#urllib.parse.quote)
  — explains the `safe=""` argument which is required to encode `/` and `#`.

---

## The GitHub fetcher

`_fetch_github()` makes two API calls:

**Call 1 — repo metadata:**
```
GET https://api.github.com/repos/{owner}/{repo}
```
Resolves the default branch name (`main`, `master`, etc.) so we don't hardcode
it. Different nf-core workflows use different default branches.

**Call 2 — raw file content:**
```
GET https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{candidate}
```
We try three candidate paths in order: `main.nf`, `workflows/main.nf`,
`{repo}.nf`. The first 200 response wins. This covers the most common nf-core
layouts without needing to list directory contents.

---

## Test strategy — mocking HTTP calls

All fetcher tests in `tests/test_fetcher.py` use `unittest.mock.patch` to
replace `httpx.Client` with a mock object. This means:

- Tests run offline and in milliseconds — no network dependency in CI.
- Tests are deterministic — real APIs change; mocks don't.
- Each test controls exactly what the "API" returns, making edge cases like
  empty version lists or 404 responses easy to simulate.

The mock setup pattern used throughout:
```python
@patch("workflow_clinic.core.fetcher.httpx.Client")
def test_something(mock_client_cls):
    mock_client_cls.return_value = _mock_dockstore_client()
    result = fetch("dockstore:github.com/nf-core/rnaseq")
    assert ...
```

`@patch` replaces the `httpx.Client` class inside the fetcher module for the
duration of the test, then restores it automatically. The mock client is
constructed to behave like a context manager (implementing `__enter__` and
`__exit__`) because the fetcher uses `with httpx.Client(...) as client:`.

**Resources:**
- [Python unittest.mock documentation](https://docs.python.org/3/library/unittest.mock.html)
- [unittest.mock.patch](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch)
  — specifically patching at the point of use (`workflow_clinic.core.fetcher.httpx`)
  rather than at the point of definition (`httpx.Client`) — an important
  distinction explained in the docs.
- [Real Python — mocking guide](https://realpython.com/python-mock-library/)

---

## Real-world results and what they revealed

Running `python scripts/collect_real_results.py` against five nf-core workflows
on Dockstore produced this:

| Workflow | Score | Gaps |
|---|---|---|
| nf-core/rnaseq | 1.00 | 0 |
| nf-core/sarek | 1.00 | 0 |
| nf-core/methylseq | 1.00 | 0 |
| nf-core/atacseq | 1.00 | 0 |
| nf-core/chipseq | 1.00 | 0 |

This looks like a perfect result, but it is actually a known limitation of our
current fetcher and an important architectural finding.

### Why all scores are 1.00

The TRS descriptor endpoint returns only the top-level `main.nf` of each
workflow. In modern nf-core workflows (DSL2), `main.nf` is a pure orchestration
file — it calls named subworkflows and imports process modules, but contains no
`process` blocks of its own. All the actual process definitions live in
`modules/local/` and `subworkflows/` subdirectories which we are not yet
fetching.

The parser therefore finds 0 processes → 0 gaps → score 1.00. This is a
**false negative**, not a genuine clean bill of health.

### What this means for Day 5

The fetcher needs to be extended to recursively fetch included files. In
Nextflow DSL2, `include { PROCESS } from './modules/local/process'` statements
declare dependencies on other files. The fetcher needs to:

1. Parse `include` statements from the top-level file
2. Resolve and fetch each included path relative to the repo root
3. Feed all files to the parser together

This is the main architectural work for the next phase. The current single-file
fetcher is sufficient for the POC but will need this extension to produce
meaningful results on real nf-core workflows.

---

## What Day 5 builds on top of this

Day 5 extends the fetcher to resolve `include` statements and fetch the full
module tree, so the Critic runs against the actual process definitions rather
than just the entry point file. The `FetchedWorkflow` dataclass will grow to
hold multiple files, and the parser will be updated to accept a list of sources
rather than a single string.