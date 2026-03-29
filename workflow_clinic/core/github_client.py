"""
GitHubClient — thin httpx wrapper for the GitHub REST API v2022-11-28.

Provides the six operations needed by the Workflow Clinic CLI:

  create_issue        — opens a gap report as a GitHub issue
  find_existing_issue — deduplication check before opening a new issue
  add_comment         — appends an updated report to an existing issue
  ensure_labels       — creates any missing labels on the target repo
  get_default_branch  — resolves the repo's default branch name
  create_branch       — creates a fix branch off the default branch
  commit_file         — writes or updates a file on a branch
  create_pull_request — opens a PR from a fix branch into the base branch

Design decisions
────────────────
We use raw httpx rather than PyGitHub for two reasons:
  1. httpx is already a project dependency (fetcher.py, llm_client.py) —
     adding PyGitHub would double the install footprint for a CLI tool.
  2. The @patch("...httpx.Client") mock pattern used in test_fetcher.py
     applies identically here, keeping the test strategy consistent.

Each public method opens its own httpx.Client context manager rather than
sharing a persistent session.  This matches the fetcher.py pattern and means
each operation is independently testable with a fresh mock.

Authentication: GITHUB_TOKEN environment variable — a classic or fine-grained
PAT with `repo` scope (issues:write + contents:write + pull_requests:write).
The token is NOT read here; the CLI reads it and passes it to __init__.

Error handling: all methods raise httpx.HTTPStatusError on API failures.
The CLI functions (_submit_issue_to_github, _submit_pr_to_github) catch these
and surface them as user-friendly messages rather than tracebacks.
"""

from __future__ import annotations

import base64
from typing import Any

import httpx

_API_BASE = "https://api.github.com"

class GitHubIssuesDisabledError(Exception):
    """Raised when the target repository has Issues disabled (HTTP 410)."""
    def __init__(self, owner: str, repo: str) -> None:
        super().__init__(
            f"Issues are disabled on {owner}/{repo}. "
            "Enable them under Settings → Features → Issues, "
            "or choose a different repository."
        )

    def create_issue(
        self,
        owner: str,
        repo: str,
        title: str,
        body: str,
        labels: list[str],
    ) -> str:
        if labels:
            self.ensure_labels(owner, repo, labels)

        with httpx.Client(timeout=30) as client:
            resp = client.post(
                f"{_API_BASE}/repos/{owner}/{repo}/issues",
                headers=self._headers,
                json={"title": title, "body": body, "labels": labels},
            )
            if resp.status_code == 410:
                raise GitHubIssuesDisabledError(owner, repo)
            resp.raise_for_status()
            return str(resp.json()["html_url"])

    def find_existing_issue(
        self, owner: str, repo: str, title_fragment: str
    ) -> int | None:
        with httpx.Client(timeout=30) as client:
            resp = client.get(
                f"{_API_BASE}/repos/{owner}/{repo}/issues",
                headers=self._headers,
                params={
                    "labels":   "workflow-clinic",
                    "state":    "open",
                    "per_page": 100,
                },
            )
            if resp.status_code == 410:
                raise GitHubIssuesDisabledError(owner, repo)
            resp.raise_for_status()
            issues: list[dict[str, Any]] = resp.json()

        for issue in issues:
            if title_fragment in issue.get("title", ""):
                return int(issue["number"])
        return None

# ── Label colours ─────────────────────────────────────────────────────────────
# GitHub requires a 6-digit hex string without the leading "#".
# Colours are chosen to be visually distinct in the GitHub issue tracker.

_LABEL_COLORS: dict[str, str] = {
    "workflow-clinic":   "0075ca",  # blue  — always present
    "cloud-readiness":   "0e8a16",  # green — always present
    "severity:critical": "d73a4a",  # red
    "severity:major":    "e4e669",  # amber-yellow
    "severity:minor":    "fbca04",  # yellow
    "severity:info":     "cccccc",  # grey
}
_DEFAULT_LABEL_COLOR = "7057ff"     # purple — used for all gap:* labels


def _label_color(name: str) -> str:
    return _LABEL_COLORS.get(name, _DEFAULT_LABEL_COLOR)


# ── GitHubClient ──────────────────────────────────────────────────────────────

class GitHubClient:

    def __init__(self, token: str) -> None:
        self._headers: dict[str, str] = {
            "Authorization":        f"Bearer {token}",
            "Accept":               "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }

    # ── Issues ────────────────────────────────────────────────────────────────

    def create_issue(
        self,
        owner: str,
        repo: str,
        title: str,
        body: str,
        labels: list[str],
    ) -> str:
        """
        Open a new issue and return its HTML URL.

        Any labels in *labels* that don't already exist on the repo are created
        automatically via ensure_labels() before the issue POST.
        """
        if labels:
            self.ensure_labels(owner, repo, labels)

        with httpx.Client(timeout=30) as client:
            resp = client.post(
                f"{_API_BASE}/repos/{owner}/{repo}/issues",
                headers=self._headers,
                json={"title": title, "body": body, "labels": labels},
            )
            resp.raise_for_status()
            return str(resp.json()["html_url"])

    def find_existing_issue(
        self, owner: str, repo: str, title_fragment: str
    ) -> int | None:
        """
        Return the number of the first open issue whose title contains
        *title_fragment* and carries the 'workflow-clinic' label.

        Used for deduplication: if an issue already exists for this workflow,
        the CLI adds a comment with the updated report instead of opening a
        duplicate.  Returns None if no matching open issue is found.
        """
        with httpx.Client(timeout=30) as client:
            resp = client.get(
                f"{_API_BASE}/repos/{owner}/{repo}/issues",
                headers=self._headers,
                params={
                    "labels":   "workflow-clinic",
                    "state":    "open",
                    "per_page": 100,
                },
            )
            resp.raise_for_status()
            issues: list[dict[str, Any]] = resp.json()

        for issue in issues:
            if title_fragment in issue.get("title", ""):
                return int(issue["number"])
        return None

    def add_comment(
        self, owner: str, repo: str, issue_number: int, body: str
    ) -> str:
        """Post a comment on an existing issue and return the comment's URL."""
        with httpx.Client(timeout=30) as client:
            resp = client.post(
                f"{_API_BASE}/repos/{owner}/{repo}/issues/{issue_number}/comments",
                headers=self._headers,
                json={"body": body},
            )
            resp.raise_for_status()
            return str(resp.json()["html_url"])

    # ── Labels ────────────────────────────────────────────────────────────────

    def ensure_labels(
        self, owner: str, repo: str, labels: list[str]
    ) -> None:
        """
        Create any labels in *labels* that don't already exist on the repo.

        Makes one GET to fetch the current label list, then POSTs only for
        labels that are missing.  Silently ignores 422 responses on POST
        (label created concurrently between the check and the create).
        """
        with httpx.Client(timeout=30) as client:
            resp = client.get(
                f"{_API_BASE}/repos/{owner}/{repo}/labels",
                headers=self._headers,
                params={"per_page": 100},
            )
            resp.raise_for_status()
            existing: set[str] = {lbl["name"] for lbl in resp.json()}

        with httpx.Client(timeout=30) as client:
            for label in labels:
                if label in existing:
                    continue
                r = client.post(
                    f"{_API_BASE}/repos/{owner}/{repo}/labels",
                    headers=self._headers,
                    json={
                        "name":        label,
                        "color":       _label_color(label),
                        "description": "Managed by Workflow Clinic",
                    },
                )
                if r.status_code == 422:
                    continue   # race condition — already exists
                r.raise_for_status()

    # ── Repository metadata ───────────────────────────────────────────────────

    def get_default_branch(self, owner: str, repo: str) -> str:
        """Return the repo's default branch name (e.g. 'main' or 'master')."""
        with httpx.Client(timeout=30) as client:
            resp = client.get(
                f"{_API_BASE}/repos/{owner}/{repo}",
                headers=self._headers,
            )
            resp.raise_for_status()
            return str(resp.json().get("default_branch", "main"))

    # ── Branches & file commits ───────────────────────────────────────────────

    def create_branch(
        self, owner: str, repo: str, base: str, name: str
    ) -> None:
        """
        Create branch *name* pointing at the current tip of *base*.

        Raises httpx.HTTPStatusError (422) if *name* already exists —
        the caller should either delete the old branch or choose a new name.
        """
        with httpx.Client(timeout=30) as client:
            ref_resp = client.get(
                f"{_API_BASE}/repos/{owner}/{repo}/git/ref/heads/{base}",
                headers=self._headers,
            )
            ref_resp.raise_for_status()
            sha: str = ref_resp.json()["object"]["sha"]

        with httpx.Client(timeout=30) as client:
            create_resp = client.post(
                f"{_API_BASE}/repos/{owner}/{repo}/git/refs",
                headers=self._headers,
                json={"ref": f"refs/heads/{name}", "sha": sha},
            )
            create_resp.raise_for_status()

    def commit_file(
        self,
        owner:   str,
        repo:    str,
        branch:  str,
        path:    str,
        content: str,
        message: str,
    ) -> None:
        """
        Create or update *path* on *branch* with *content*.

        GitHub's Contents API requires the existing file's SHA when updating
        an existing file.  This method fetches that SHA automatically — the
        caller never needs to handle the create-vs-update distinction.
        """
        encoded = base64.b64encode(content.encode()).decode()
        url     = f"{_API_BASE}/repos/{owner}/{repo}/contents/{path}"
        payload: dict[str, str] = {
            "message": message,
            "content": encoded,
            "branch":  branch,
        }

        # Check whether the file already exists on the branch.
        # A 200 response means we must supply the current SHA.
        # A 404 means this is a new file — no SHA needed.
        # Any other status is a genuine error.
        with httpx.Client(timeout=30) as client:
            check = client.get(
                url, headers=self._headers, params={"ref": branch}
            )
            if check.status_code == 200:
                payload["sha"] = check.json()["sha"]
            elif check.status_code != 404:
                check.raise_for_status()

        with httpx.Client(timeout=30) as client:
            resp = client.put(url, headers=self._headers, json=payload)
            resp.raise_for_status()

    # ── Pull requests ─────────────────────────────────────────────────────────

    def create_pull_request(
        self,
        owner: str,
        repo:  str,
        head:  str,
        base:  str,
        title: str,
        body:  str,
    ) -> str:
        """Open a pull request from *head* into *base* and return its URL."""
        with httpx.Client(timeout=30) as client:
            resp = client.post(
                f"{_API_BASE}/repos/{owner}/{repo}/pulls",
                headers=self._headers,
                json={
                    "head":  head,
                    "base":  base,
                    "title": title,
                    "body":  body,
                },
            )
            resp.raise_for_status()
            return str(resp.json()["html_url"])