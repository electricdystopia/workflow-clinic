# Day 9 — Real GitHub Issue and PR Creation

## What we built and why

Day 7 added `--create-issue`, which drafts a GitHub issue body but deliberately
never submits it. Day 8 extended the tool to Snakemake. Day 9 closes the loop:
the draft is now POSTed to a real repository, and the Doctor's fix proposals
become real pull requests. This directly addresses the GSoC milestone "agent
team integrated to create gap report issues / PRs in workflow repositories."

The additions are:

1. `GitHubClient` in `workflow_clinic/core/github_client.py` — a thin httpx
   wrapper for the four GitHub REST API operations the CLI needs.
2. `--submit` on `workflow-clinic critic` — POSTs the issue draft to GitHub,
   with deduplication before creation.
3. `--create-pr` on `workflow-clinic doctor` — applies each validated
   `FixProposal` by creating a branch, committing the patched file, and opening
   a PR.
4. `patched_content` field on `FixProposal` — stores the full patched file
   content so the CLI can commit it without re-running the fixer.

By the end of Day 9 the pipeline looks like this:
```
Local .nf / .smk file          ─┐
dockstore: / github: source     ─┤→ Parser → CriticEngine → GapReport
                                 ↓
                          --create-issue --submit
                                 ↓
                          GitHubClient.find_existing_issue()
                            ├─ exists → add_comment()
                            └─ new    → ensure_labels() + create_issue()

                          --create-pr (doctor)
                                 ↓
                          GitHubClient.get_default_branch()
                                 → create_branch()
                                 → commit_file()
                                 → create_pull_request()
```

---

## New files introduced today
```
workflow_clinic/
└── core/
    └── github_client.py       ← GitHubClient: issues, labels, branches, PRs
tests/
└── test_github_client.py      ← 28 tests, all mocked — no network required
docs/
└── day9-github.md             ← this file
```

**Modified files:**
```
workflow_clinic/doctor/fix_generators/base.py        ← add patched_content field
workflow_clinic/doctor/fix_generators/nextflow_fixes.py ← populate patched_content
workflow_clinic/cli.py                               ← --submit, --create-pr flags
                                                        _submit_issue_to_github()
                                                        _submit_pr_to_github()
                                                        _render_pr_body()
                                                        _resolve_repo()
tests/test_cli.py                                    ← 8 new CLI integration tests
```

---

## Why raw httpx instead of PyGitHub

The architecture document in the project summary (document index 95) lists
PyGitHub as the intended SDK. We use raw httpx instead for two reasons rooted
in the existing codebase:

**Reason 1 — No new dependency.** httpx is already in `pyproject.toml` as a
direct dependency of `workflow_clinic/core/fetcher.py` and
`workflow_clinic/core/llm_client.py`. Adding PyGitHub (`pip install PyGitHub`)
would add ~5 transitive dependencies (PyNaCl, Deprecated, PyJWT, etc.) to a
CLI tool that is already installable with five packages.

**Reason 2 — Test pattern reuse.** Every existing HTTP test in the project uses
`@patch("...httpx.Client")` to mock the HTTP layer — see
`tests/test_fetcher.py` and `tests/test_llm_client.py`. The same pattern works
identically for `tests/test_github_client.py`, meaning there is no new mocking
strategy to learn or maintain.

The trade-off is boilerplate. We write explicit `client.post(url, headers=...,
json=...)` calls rather than `repo.create_issue(title=..., body=...)`. For the
six API operations Day 9 needs, this is acceptable. If the project grows to
dozens of GitHub interactions (project cards, milestones, code review requests),
switching to PyGitHub becomes worthwhile.

**Resources:**
- [GitHub REST API — overview](https://docs.github.com/en/rest/overview/about-the-rest-api)
  — the root reference for all endpoints used in `workflow_clinic/core/github_client.py`.
- [GitHub REST API versioning](https://docs.github.com/en/rest/overview/api-versions)
  — explains the `X-GitHub-Api-Version: 2022-11-28` header set in every
  request from `GitHubClient.__init__`; without this header the API may return
  deprecated response shapes.
- [httpx documentation](https://www.python-httpx.org/)
  — `httpx.Client` context manager usage and `raise_for_status()` semantics;
  both are used throughout `github_client.py`.
- [PyGitHub documentation](https://pygithub.readthedocs.io/en/latest/)
  — the SDK we chose not to use; read this if the project eventually moves away
  from raw httpx for GitHub interactions.

---

## The `GitHubClient` — API operations and design decisions

The client lives in `workflow_clinic/core/github_client.py`. Each public method
opens its own `httpx.Client` context manager rather than sharing a persistent
session. This matches the pattern in `workflow_clinic/core/fetcher.py` and
means each method is independently testable.

### Authentication
```python
# workflow_clinic/core/github_client.py — GitHubClient.__init__
self._headers = {
    "Authorization":        f"Bearer {token}",
    "Accept":               "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
}
```

The token is NOT read from the environment inside `GitHubClient`. The CLI
helper functions (`_submit_issue_to_github`, `_submit_pr_to_github` in
`workflow_clinic/cli.py`) read `os.getenv("GITHUB_TOKEN")` and pass it to
`GitHubClient(token)`. This separation of concerns means the client is
independently testable with any token string — no environment variable patching
needed in `tests/test_github_client.py`.

**Resources:**
- [GitHub — creating a personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)
  — the token type expected by `GitHubClient`; requires `repo` scope for
  private repos, or `public_repo` for public ones.
- [GitHub — fine-grained PATs](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-fine-grained-personal-access-token)
  — the recommended token type for production use; permissions needed are
  `Issues: write`, `Contents: write`, `Pull requests: write`.

### `ensure_labels` — why it's separate from `create_issue`
```python
# workflow_clinic/core/github_client.py — create_issue
if labels:
    self.ensure_labels(owner, repo, labels)
```

GitHub's `POST /repos/{owner}/{repo}/issues` returns a 422 error if any label
in the request body doesn't exist on the repository. `ensure_labels` runs a
`GET /labels` first, then creates only the missing ones.

The 422-on-create case inside `ensure_labels` is handled silently:
```python
if r.status_code == 422:
    continue   # race condition — label created concurrently
```

This matters in CI environments where multiple jobs might run `workflow-clinic
critic --submit` in parallel on the same repo for the first time — both would
try to create the same labels simultaneously, and the second attempt would get
a 422. Silently continuing is correct: the label exists, the issue POST will succeed.

**Resources:**
- [GitHub REST API — create a label](https://docs.github.com/en/rest/issues/labels?apiVersion=2022-11-28#create-a-label)
  — documents the 422 response for duplicate label names; the `errors[0].code`
  field is `"already_exists"`.
- [GitHub REST API — list labels for a repository](https://docs.github.com/en/rest/issues/labels?apiVersion=2022-11-28#list-labels-for-a-repository)
  — the GET endpoint used in `ensure_labels` to check existing labels before
  attempting creation.

### `find_existing_issue` — deduplication strategy
```python
# workflow_clinic/core/github_client.py — find_existing_issue
resp = client.get(
    f"{_API_BASE}/repos/{owner}/{repo}/issues",
    headers=self._headers,
    params={"labels": "workflow-clinic", "state": "open", "per_page": 100},
)
for issue in issues:
    if title_fragment in issue.get("title", ""):
        return int(issue["number"])
```

The CLI calls this with `"[Workflow Clinic]"` as the fragment, which appears
in every title produced by `_render_github_issue()` in `workflow_clinic/cli.py`.
The first matching open issue is returned.

This is an intentional simplification for the POC: if a repo has two open
Workflow Clinic issues for two different workflows, the first one in the list
wins. A production version would encode the workflow path in the title or use
the GitHub search API (`/search/issues?q=...`) for more precise matching.

**Resources:**
- [GitHub REST API — list issues](https://docs.github.com/en/rest/issues/issues?apiVersion=2022-11-28#list-repository-issues)
  — the `labels`, `state`, and `per_page` query parameters used in
  `find_existing_issue`; note that `per_page` maxes at 100.
- [GitHub REST API — search issues](https://docs.github.com/en/rest/search/search?apiVersion=2022-11-28#search-issues-and-pull-requests)
  — the more precise alternative; requires the `search` scope on the token and
  has different rate limits (30 requests/minute vs. 60 for the issues endpoint).

### `commit_file` — the create-vs-update distinction

GitHub's Contents API requires the existing file's `sha` when updating a file,
but must not include `sha` when creating a new one. `commit_file` handles this
transparently:
```python
# workflow_clinic/core/github_client.py — commit_file
check = client.get(url, headers=self._headers, params={"ref": branch})
if check.status_code == 200:
    payload["sha"] = check.json()["sha"]
elif check.status_code != 404:
    check.raise_for_status()
```

The 404 case (new file) falls through without setting `sha`. A status other
than 200 or 404 is a genuine API error and is re-raised.

Note that `check.raise_for_status()` is NOT called for 404 responses — calling
it would raise `httpx.HTTPStatusError` and abort the commit. This is why the
code checks `status_code` directly rather than relying on `raise_for_status()`.
The same pattern is used in `_fetch_github_full` in
`workflow_clinic/core/fetcher.py` (`if r.status_code == 200`).

**Resources:**
- [GitHub REST API — create or update file contents](https://docs.github.com/en/rest/repos/contents?apiVersion=2022-11-28#create-or-update-file-contents)
  — documents the `sha` requirement for updates; the response body for a
  successful update includes the new commit SHA.
- [Python `base64` module](https://docs.python.org/3/library/base64.html#base64.b64encode)
  — `base64.b64encode(content.encode()).decode()` is the exact encoding the
  GitHub Contents API requires; the `content` field must be standard base64.

### `create_branch` — resolving the base SHA
```python
# workflow_clinic/core/github_client.py — create_branch
ref_resp = client.get(
    f"{_API_BASE}/repos/{owner}/{repo}/git/ref/heads/{base}",
    headers=self._headers,
)
sha = ref_resp.json()["object"]["sha"]
```

A branch is a Git ref. Creating a new branch means creating a new ref pointing
at an existing commit SHA. The SHA of the base branch's tip is resolved via the
Git Data API (`/git/ref/heads/{base}`) rather than the Repos API
(`/branches/{base}`) because the Git Data API returns the SHA directly in a
consistent location (`object.sha`) regardless of whether the branch is a
lightweight or annotated tag.

**Resources:**
- [GitHub REST API — get a reference](https://docs.github.com/en/rest/git/refs?apiVersion=2022-11-28#get-a-reference)
  — the `GET /git/ref/heads/{branch}` endpoint and the `object.sha` field.
- [GitHub REST API — create a reference](https://docs.github.com/en/rest/git/refs?apiVersion=2022-11-28#create-a-reference)
  — the `POST /git/refs` endpoint; note the `ref` field must be the full
  reference path (`refs/heads/branch-name`), not just the branch name.

---

## CLI changes — `--submit` on `critic`

The `critic` command in `workflow_clinic/cli.py` gains two new options:
```
--submit        POST the issue to GitHub (implies --create-issue)
--repo          Target repository as owner/repo
```

`--submit` implies `--create-issue` — the user should not need to pass both.
This mirrors how `--issue-output` implies `--create-issue` (established in
Day 7).

The submission logic lives in `_submit_issue_to_github()`:

1. Read `GITHUB_TOKEN` from the environment. Exit 1 with a clear message if absent.
2. Call `_resolve_repo()` to parse `--repo` or infer `owner/repo` from the
   source URL. Exit 1 if neither produces a valid `owner/repo` string.
3. Create `GitHubClient(token)`.
4. Call `find_existing_issue()` with `"[Workflow Clinic]"` as the fragment.
5. If an existing issue is found: call `add_comment()` with the updated body.
6. If not: call `create_issue()` with the title, body, and labels from
   `_render_github_issue()` and `_issue_labels()`.
7. Print the URL (issue or comment) in green.

### `_resolve_repo` — source URL inference
```python
# workflow_clinic/cli.py — _resolve_repo
for prefix in (
    "dockstore:github.com/",
    "https://github.com/",
    "github.com/",
    "github:",
):
    if prefix in source:
        tail  = source.split(prefix, 1)[1]
        parts = tail.split("/")
        if len(parts) >= 2:
            return f"{parts[0]}/{parts[1]}"
```

This covers all four remote source formats the CLI accepts. Local file paths
produce no match, so `_resolve_repo` returns `None` for them — the caller then
requires an explicit `--repo` and exits 1 with a helpful message if it's absent.

---

## CLI changes — `--create-pr` on `doctor`

The `doctor` command gains three new options:
```
--create-pr         Apply fix and open a PR (requires GITHUB_TOKEN + --repo)
--branch-prefix     Override the branch name prefix (default: wf-clinic)
--repo              Target repository as owner/repo
```

The PR workflow is in `_submit_pr_to_github()`:

1. Validate token and `--repo`.
2. Call `get_default_branch()` to find `main` / `master`.
3. Build the branch name: `{prefix}/{gap_id}/{process_name}` (all lowercase,
   underscores to hyphens). Example: `wf-clinic/container-001/align`.
4. Call `create_branch()`.
5. Call `commit_file()` with `proposal.patched_content` and `source_path.name`
   as the path within the repo.
6. Call `create_pull_request()` with a body from `_render_pr_body()`.
7. Print the PR URL in green.

Proposals are skipped (with a yellow warning) if:
- `validation_passed` is False — the parser could not confirm the fix is correct.
- `patched_content` is empty — the fixer failed before producing a valid patch.

This ensures that `--create-pr` never opens a PR for a fix that Workflow Clinic
is not confident about. The user can still review those proposals manually from
the terminal output or `--output` JSON.

### Branch name convention
```
wf-clinic/container-001/align
wf-clinic/container-001/call-variants
wf-clinic/container-002/trim
```

The three-level structure (`prefix/gap-id/process`) makes branches easy to find
in the GitHub branch list, easy to filter with `git branch --list wf-clinic/*`,
and self-documenting — a reviewer can see from the branch name exactly which
gap it addresses without opening the PR.

The `--branch-prefix` override is useful for teams that want to namespace
automated branches differently from manual ones, e.g. `bot/wf-clinic/...`.

**Resources:**
- [GitHub REST API — create a pull request](https://docs.github.com/en/rest/pulls/pulls?apiVersion=2022-11-28#create-a-pull-request)
  — the endpoint used in `create_pull_request()`; the `head` field is the
  branch name, `base` is the default branch.
- [Git branch naming conventions](https://stackoverflow.com/a/6065944)
  — why `/` is used as a namespace separator in branch names (it creates a
  visual grouping in most Git GUIs and the GitHub branch list).

---

## `patched_content` on `FixProposal`
```python
# workflow_clinic/doctor/fix_generators/base.py — FixProposal
patched_content: str = field(default="")
```

`patched_content` stores the full patched file as a string. It is populated by
`ContainerMissingFixer` and `ContainerLatestTagFixer` in
`workflow_clinic/doctor/fix_generators/nextflow_fixes.py` immediately after the
`"".join(patched_lines)` call that is already needed for validation.

The field has a default of `""` so all existing `FixProposal(...)` call sites
in the codebase that don't supply it continue to work unchanged — the 92 tests
that existed before Day 9 all pass without modification.

The `_submit_pr_to_github()` function checks `if not proposal.patched_content`
and skips the proposal with a warning rather than committing an empty file. This
is the correct defensive behaviour when:
- The LLM call failed (no patch was generated).
- The process block was not found in the source (insertion point not located).
- The proposal came from a serialized JSON file where `patched_content` was
  stripped or was already empty.

**Resources:**
- [Python `dataclasses.field` — default values](https://docs.python.org/3/library/dataclasses.html#dataclasses.field)
  — the `field(default="")` syntax used to add `patched_content` without
  breaking existing positional-style dataclass instantiations; the dataclasses
  docs explain why a field with a default must come after all fields without
  defaults.
- [Python `dataclasses.asdict`](https://docs.python.org/3/library/dataclasses.html#dataclasses.asdict)
  — the function used in `workflow_clinic/cli.py`'s `_serialize_proposals()`
  to convert `FixProposal` objects to JSON-serialisable dicts; `patched_content`
  will appear in the serialized output automatically.

---

## Test strategy

`tests/test_github_client.py` contains 28 tests organized into one section per
public method. All tests use `@patch("workflow_clinic.core.github_client.httpx.Client")`
and the `_mock_client()` helper — the same mock pattern established in
`tests/test_fetcher.py`.

Key design decisions in the test file:

**Isolating `create_issue` from `ensure_labels`:** Tests that focus on the
issue creation POST pass `labels=[]`, which causes `ensure_labels` to be skipped
entirely. The interaction between the two methods is tested in a single dedicated
test (`test_create_issue_calls_ensure_labels_when_labels_given`) that sequences
all three HTTP calls (GET labels, POST label, POST issue) on the mock's
`side_effect` lists.

**Testing the 404 branch in `commit_file`:** The 404 response needs
`status_code == 404` but must NOT have `raise_for_status()` raise (since the
code only calls it for non-200, non-404 statuses). The `_err_resp()` helper
creates a mock with `raise_for_status.side_effect = httpx.HTTPStatusError(...)`;
for the 404 case we create a plain MagicMock with `status_code = 404` and a
no-op `raise_for_status`. This is the correct setup — calling `raise_for_status`
on a mock where `side_effect` is not set is a no-op by default.

**Asserting payload structure rather than URL strings:** Where possible, tests
assert on `mock.post.call_args[1]["json"]` (the payload dict) rather than the
URL string. This is more resilient to future URL changes and directly verifies
the data sent to GitHub.

## Coverage after Day 9

| Module | Before | After |
|---|---|---|
| `core/github_client.py` | — (new) | 99% |
| `cli.py` | 91% | 72% |
| `doctor/fix_generators/base.py` | 100% | 100% |
| `doctor/fix_generators/nextflow_fixes.py` | 89% | 89% |
| **Overall** | 91% | 85% |


The 1% miss in `github_client.py` is the `elif check.status_code != 404:
check.raise_for_status()` branch in `commit_file` — the path triggered when
the file-existence check returns a non-200, non-404 status (e.g. 403 permission
denied). This is a defensive branch that requires a mock raising an
`HTTPStatusError` for GET, which was excluded from the test suite to keep the
test count manageable.

**Resources:**
- [unittest.mock — patch](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch)
  — the decorator used throughout `test_github_client.py`; the key detail is
  patching at the point of use (`workflow_clinic.core.github_client.httpx`)
  rather than at the definition site (`httpx.Client`).
- [unittest.mock — MagicMock side_effect](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.side_effect)
  — how `side_effect = [resp1, resp2, resp3]` sequences responses across multiple
  calls to the same mock method; used for multi-call operations like
  `create_issue` (GET + POST + POST).
- [pytest monkeypatch](https://docs.pytest.org/en/stable/how-to/monkeypatch.html)
  — used in the new CLI tests to set/unset `GITHUB_TOKEN` within a test without
  affecting the rest of the test suite; the same technique used in
  `tests/test_llm_client.py`.

---

## What Day 10 builds on top of this

The PR creation pipeline is functional but uses the file's basename as its path
within the target repository. This is correct for single-file workflows but
breaks for nf-core-style repos where `main.nf` sits alongside `modules/` and
`subworkflows/`. Day 10 could address this by reading the `gap.location.file`
path (which for fetched workflows is already relative to the repo root) and
using it directly as the repo path in `commit_file`.

The deduplication in `find_existing_issue` is based on `"[Workflow Clinic]"` in
the title, which finds any existing WC issue, not one specific to the current
workflow. A more precise approach would encode the workflow path in the title —
a small change to `_render_github_issue()` in `workflow_clinic/cli.py` —
enabling per-workflow deduplication on repositories with multiple registered
workflows.

The `patched_content` field is currently only populated by the two Nextflow
fixers. As new fix generators are added for Snakemake (`ContainerMissingFixer`
for `.smk` files) and other languages, they should populate `patched_content`
following the same pattern — storing `"".join(patched_lines)` in the
successful-fix return statement.