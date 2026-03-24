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
└── collect_real_results.py ← runs Critic against real Dockstore workflows
results/
└── *.json                  ← real gap reports saved as evidence
```

---

## Why httpx and not requests?

`requests` is the most widely known Python HTTP library but it is synchronous
only. `httpx` is a modern drop-in replacement that is synchronous by default
but also supports async — which matters because a future iteration may need to
fetch multiple workflow files concurrently (modules, subworkflows) without
blocking. Switching from sync to async in httpx is a one-line change; switching
away from `requests` entirely would require a rewrite. We pay nothing extra for
this flexibility now.

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
    source:   str                        # original identifier, for display and report metadata
    filename: str                        # suggested filename (e.g. "main.nf")
    content:  str                        # concatenated text of all .nf files
    files:    list[tuple[str, str]]      # individual (path, content) pairs for reference
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
    return _fetch_dockstore(source, full_repo=full_repo)
elif "github.com" in source or source.startswith("github:"):
    if full_repo:
        return _fetch_github_full(source)
    return _fetch_github(source)
else:
    raise ValueError(...)
```

This pattern — a public router over private implementation functions — keeps
the caller's code simple while allowing each fetcher to grow independently.
Adding a WorkflowHub fetcher in the future means adding one `elif` branch and
one private function; nothing else changes.

---

## The Dockstore fetcher

The Dockstore fetcher in `_fetch_dockstore()` uses the GA4GH TRS v2 API. Its
design went through two rounds of investigation and is worth documenting in
full, because each round uncovered a real architectural constraint.

### Initial design — single primary descriptor

The first implementation made two API calls:

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

### Bugs fixed during initial implementation

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

---

## The false-negative problem — and why the obvious fix was wrong

After implementing the initial fetcher and running it against five real nf-core
workflows, every workflow scored 1.00 with 0 gaps:

```
nf-core/rnaseq    score=1.00  gaps=0
nf-core/sarek     score=1.00  gaps=0
nf-core/methylseq score=1.00  gaps=0
nf-core/atacseq   score=1.00  gaps=0
nf-core/chipseq   score=1.00  gaps=0
```

This is a **false negative**, not a genuine clean bill of health. The root cause
is that `full_repo=True` was silently ignored for Dockstore sources. The router
at the time looked like this:

```python
# BUG: full_repo is never forwarded to _fetch_dockstore
if source.startswith("dockstore:"):
    return _fetch_dockstore(source)
```

Even if `full_repo` had been forwarded, `_fetch_dockstore` only called the
primary descriptor endpoint — which for every modern nf-core DSL2 workflow
returns a bare `main.nf` with zero `process` blocks. All actual process
definitions live in `modules/local/` and `subworkflows/`, none of which are
returned by the primary descriptor endpoint. The parser therefore finds
0 processes → 0 gaps → score 1.00.

### Why GitHub fallback was not the right fix

The obvious workaround — extract `github.com/owner/repo` from the Dockstore
identifier and delegate to `_fetch_github_full` — was considered and rejected
for a principled reason.

Dockstore is not GitHub-only. It registers workflows from:
- GitHub (`github.com/...`)
- GitLab (`gitlab.com/...`)
- Bitbucket (`bitbucket.org/...`)
- Self-hosted Gitea instances

A `dockstore:github.com/nf-core/rnaseq` identifier happens to be GitHub, but
`dockstore:gitlab.com/some/group/workflow` is an equally valid Dockstore source
and the GitHub fallback would silently fetch the wrong repository or fail with
no meaningful error. The correct fix must work for any Dockstore-registered
workflow regardless of its underlying VCS host.

---

## The correct fix — TRS v2 `/files` endpoint

The TRS v2 API already provides exactly what is needed. There are two endpoints
that were unused in the initial implementation:

**List all files in a version:**
```
GET /ga4gh/trs/v2/tools/{id}/versions/{version_id}/NFL/files
```
Returns a list of all registered files with their types:
```json
[
  { "path": "main.nf",                          "file_type": "PRIMARY_DESCRIPTOR" },
  { "path": "modules/local/bwa_mem.nf",         "file_type": "SECONDARY_DESCRIPTOR" },
  { "path": "subworkflows/local/align.nf",      "file_type": "SECONDARY_DESCRIPTOR" },
  { "path": "nextflow.config",                  "file_type": "OTHER" }
]
```

**Fetch a specific secondary file by relative path:**
```
GET /ga4gh/trs/v2/tools/{id}/versions/{version_id}/NFL/descriptor/{relative_path}
```

The fix is to call `/files` first, filter for `.nf` files with type
`PRIMARY_DESCRIPTOR` or `SECONDARY_DESCRIPTOR`, then fetch each one individually
— all within the Dockstore TRS API, with no dependency on any external VCS host.

The updated `_fetch_dockstore` signature now accepts `full_repo`:
```python
def _fetch_dockstore(source: str, full_repo: bool = False) -> FetchedWorkflow:
    ...
    if not full_repo:
        # original single-file path via /descriptor
        ...

    # full_repo path: list all registered .nf files via /files
    files_resp = client.get(
        f"{_DOCKSTORE_TRS_BASE}/tools/{encoded}"
        f"/versions/{version_id}/NFL/files"
    )
    file_list = files_resp.json()

    nf_entries = [
        f for f in file_list
        if f.get("path", "").endswith(".nf")
        and f.get("file_type") in ("PRIMARY_DESCRIPTOR", "SECONDARY_DESCRIPTOR")
    ]

    # Fetch each .nf file individually
    files: list[tuple[str, str]] = []
    for entry in nf_entries:
        rel_path     = entry["path"]
        encoded_path = urllib.parse.quote(rel_path, safe="")
        r = client.get(
            f"{_DOCKSTORE_TRS_BASE}/tools/{encoded}"
            f"/versions/{version_id}/NFL/descriptor/{encoded_path}"
        )
        if r.status_code == 200:
            content = r.json().get("content", "")
            if content:
                files.append((rel_path, content))

    chunks   = [f"// === FILE: {path} ===\n{content}" for path, content in files]
    combined = "\n\n".join(chunks)
    return FetchedWorkflow(source=source, filename="main.nf",
                           content=combined, files=files)
```

And the router now correctly forwards `full_repo`:
```python
if source.startswith("dockstore:"):
    return _fetch_dockstore(source, full_repo=full_repo)  # ← was ignoring full_repo
```

**Resources:**
- [GA4GH TRS v2 API specification](https://ga4gh.github.io/tool-registry-service-schemas/GeneratedOpenAPIDoc/)
  — the official spec; `/files` and secondary descriptor endpoints are defined here.
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

`_fetch_github_full()` extends this by using the GitHub Git Tree API
(`/repos/{owner}/{repo}/git/trees/{sha}?recursive=1`) to enumerate all `.nf`
files in one call, then fetches each via `raw.githubusercontent.com`. This path
is used when `full_repo=True` is passed with a direct GitHub source, and serves
as the correct fetcher for non-Dockstore GitHub workflows.

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

## Real-world results

After fixing the fetcher to use the TRS `/files` endpoint with `full_repo=True`,
running `python scripts/collect_real_results.py` against eight workflows
produced meaningful, differentiated results:

| Workflow | Score | Gaps |
|---|---|---|
| nf-core/rnaseq | 1.00 | 0 |
| nf-core/sarek | 1.00 | 0 |
| nf-core/methylseq | 0.00 | 11 |
| nf-core/atacseq | 0.00 | 88 |
| nf-core/chipseq | 0.30 | 4 |
| AAFC-Bioinfo-AAC/metagenomics-nf | 0.00 | 70 |
| bethsheets/workflows-demo | 1.00 | 0 |
| erinyoung/roundabout | 0.00 | 11 |

This is the first time the tool has produced non-trivial results on real
community workflows. The gap breakdown across failing workflows falls into three
clear patterns:

**CONTAINER-001 (missing container)** — processes with no container directive at
all. This is a CRITICAL gap. `erinyoung/roundabout` has one such process
(`circos`) with a container entirely absent.

**CONTAINER-002 (`:latest` tag)** — processes that have a container directive
but pin to `:latest` rather than a specific version or SHA. This is a MAJOR
reproducibility gap. `erinyoung/roundabout` is a clear example:
```
staphb/ncbi-amrfinderplus:latest
staphb/bedtools:latest
ncbi/blast:latest
staphb/plasmidfinder:latest
staphb/prokka:latest
staphb/samtools:latest
```
All six are unpinned. The same tag resolves to different image layers over time,
meaning a workflow run today and a run in six months may produce different
results with no change to the workflow code.

**STORAGE-001 (hardcoded absolute paths)** — processes whose script blocks
reference local absolute paths. The `blastn` process in `erinyoung/roundabout`
uses `/non_*` paths; the `circos` process references `/karyotype.txt`,
`/amrfinder_text.txt`, and seven more local paths. These paths do not exist on
any cloud execution environment and will cause silent or confusing failures when
the workflow is submitted via WES.

### Why rnaseq and sarek score 1.00

nf-core/rnaseq and nf-core/sarek are among the most mature nf-core pipelines
and comply fully with nf-core's own module standards, which mandate pinned
container images and explicit I/O declarations across all modules. Their 1.00
score is a genuine clean bill of health for the gap categories we currently
check, not a false negative. This is confirmed by the fact that community
workflows like `metagenomics-nf` and `roundabout` — which do not follow nf-core
module standards — show substantive gaps.

### A note on false positives in STORAGE-001

The `erinyoung/roundabout` report includes a STORAGE-001 gap on the `prep`
process with evidence `//g, //g`. These are sed substitution expressions
(`s/foo//g`) being matched by the hardcoded-path regex, which catches any
token starting with `/`. This is a known limitation of the current regex
approach: it cannot distinguish between a genuine path (`/data/ref/hg38.fa`)
and an incidental `/` character in a shell expression. Improving the regex to
require a word character after the second `/` (i.e. `/[\w]`) would reduce these
false positives and is a candidate improvement for the rule engine.

---

## What Day 5 builds on top of this

The fetcher now correctly retrieves all `.nf` files registered with Dockstore
for a given workflow version. The next step is to validate how comprehensive
Dockstore's secondary file registration actually is — some older or community
workflows may not register every module as a secondary descriptor, meaning the
`/files` endpoint returns fewer files than actually exist in the repository.
For those cases, the GitHub full-repo fetcher remains available as a fallback
and can be triggered by passing a direct GitHub URL instead of a Dockstore
identifier.

The false-positive issue in STORAGE-001 and the penalty weighting in the
cloud readiness score are both candidates for refinement as the rule engine
matures toward an LLM-assisted critic.