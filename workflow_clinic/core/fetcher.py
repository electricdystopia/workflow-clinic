"""
Workflow fetcher — resolves a source string (local path, GitHub URL,
or Dockstore TRS identifier) into raw .nf file content.
"""

from __future__ import annotations

import urllib.parse
from dataclasses import dataclass, field
from pathlib import Path

import httpx


@dataclass
class FetchedWorkflow:
    """
    The result of fetching a workflow from any source.
    content holds the concatenated text of all .nf files found.
    files holds each individual (path, content) pair for reference.
    """
    source:   str
    filename: str
    content:  str
    files:    list[tuple[str, str]] = field(default_factory=list)


# ── Constants ─────────────────────────────────────────────────────────────────

_DOCKSTORE_TRS_BASE = "https://dockstore.org/api/ga4gh/trs/v2"
_GITHUB_RAW_BASE    = "https://raw.githubusercontent.com"
_GITHUB_API_BASE    = "https://api.github.com"


# ── Public entry point ────────────────────────────────────────────────────────

def fetch(source: str, full_repo: bool = False) -> FetchedWorkflow:
    """
    Route a source string to the correct fetcher and return a FetchedWorkflow.

    Supported formats:
        dockstore:github.com/owner/repo        → Dockstore TRS API
        https://github.com/owner/repo          → GitHub (full repo if full_repo=True)
        github:owner/repo                      → GitHub shorthand

    When full_repo=True and source is a GitHub URL, fetches ALL .nf files
    from the repository tree rather than just the entry point file.
    This is required for modern nf-core DSL2 workflows where process blocks
    live in modules/ and subworkflows/ rather than main.nf.
    """
    if source.startswith("dockstore:"):
        return _fetch_dockstore(source)
    elif "github.com" in source or source.startswith("github:"):
        if full_repo:
            return _fetch_github_full(source)
        return _fetch_github(source)
    else:
        raise ValueError(
            f"Unrecognised remote source: '{source}'.\n"
            "Expected one of:\n"
            "  dockstore:github.com/owner/repo\n"
            "  https://github.com/owner/repo\n"
            "  github:owner/repo"
        )


# ── Dockstore fetcher ─────────────────────────────────────────────────────────

def _fetch_dockstore(source: str) -> FetchedWorkflow:
    repo_path = source.removeprefix("dockstore:")
    tool_id   = f"#workflow/{repo_path}"
    encoded   = urllib.parse.quote(tool_id, safe="")

    with httpx.Client(timeout=30) as client:
        tool_resp = client.get(f"{_DOCKSTORE_TRS_BASE}/tools/{encoded}")
        tool_resp.raise_for_status()
        tool_data = tool_resp.json()

        versions = tool_data.get("versions", [])
        if not versions:
            raise ValueError(f"No versions found for '{source}' on Dockstore.")

        def _is_release(v: dict) -> bool:
            name = v.get("name", "")
            return (
                not name.startswith("dev")
                and not name.startswith("preview")
                and not name.startswith("TEMPLATE")
                and name != "master"
                and name != "main"
            )

        release_versions = [v for v in versions if _is_release(v)]
        chosen_version   = release_versions[0] if release_versions else versions[0]
        version_name     = chosen_version["name"]
        version_id       = urllib.parse.quote(version_name, safe="")

        desc_url  = (
            f"{_DOCKSTORE_TRS_BASE}/tools/{encoded}"
            f"/versions/{version_id}/NFL/descriptor"
        )
        desc_resp = client.get(desc_url)
        desc_resp.raise_for_status()
        desc_data = desc_resp.json()

        content = desc_data.get("content", "")
        if not content:
            raise ValueError(
                f"Dockstore returned an empty descriptor for '{source}'."
            )

        filename = repo_path.split("/")[-1] + ".nf"
        return FetchedWorkflow(source=source, filename=filename, content=content)


# ── GitHub single-file fetcher (original) ────────────────────────────────────

def _fetch_github(source: str) -> FetchedWorkflow:
    owner, repo = _parse_github_source(source)

    with httpx.Client(timeout=30) as client:
        default_branch = _resolve_default_branch(client, owner, repo)

        candidates = ["main.nf", "workflows/main.nf", f"{repo}.nf"]
        for candidate in candidates:
            raw_url = (
                f"{_GITHUB_RAW_BASE}/{owner}/{repo}"
                f"/{default_branch}/{candidate}"
            )
            nf_resp = client.get(raw_url)
            if nf_resp.status_code == 200:
                return FetchedWorkflow(
                    source=source,
                    filename=candidate.split("/")[-1],
                    content=nf_resp.text,
                    files=[(candidate, nf_resp.text)],
                )

        raise ValueError(
            f"Could not find a .nf entry point in {owner}/{repo}. "
            f"Tried: {', '.join(candidates)}"
        )


# ── GitHub full-repo fetcher ──────────────────────────────────────────────────

def _fetch_github_full(source: str) -> FetchedWorkflow:
    """
    Fetch ALL .nf files from a GitHub repository using the Git Tree API.

    This is necessary for modern nf-core DSL2 workflows where main.nf is a
    pure orchestration file and all process blocks live in modules/ and
    subworkflows/. Fetching only main.nf produces 0 processes and therefore
    0 gaps — a false negative.

    The Git Tree API returns the full file list in a single call with
    recursive=1, which is far more efficient than walking directories.
    Each .nf file is then fetched individually via raw.githubusercontent.com.

    Files are concatenated with a path comment header so the parser treats
    them as one continuous source while line numbers remain meaningful per
    file. The combined content is what the parser receives.
    """
    owner, repo = _parse_github_source(source)

    with httpx.Client(timeout=60) as client:
        default_branch = _resolve_default_branch(client, owner, repo)

        # ── Step 1: get full tree ─────────────────────────────────────────────
        # Resolve the branch to a commit SHA first
        branch_resp = client.get(
            f"{_GITHUB_API_BASE}/repos/{owner}/{repo}/branches/{default_branch}",
            headers={"Accept": "application/vnd.github+json"},
        )
        branch_resp.raise_for_status()
        sha = branch_resp.json()["commit"]["sha"]

        tree_resp = client.get(
            f"{_GITHUB_API_BASE}/repos/{owner}/{repo}/git/trees/{sha}",
            params={"recursive": "1"},
            headers={"Accept": "application/vnd.github+json"},
        )
        tree_resp.raise_for_status()
        tree_data = tree_resp.json()

        # ── Step 2: filter for .nf files ─────────────────────────────────────
        nf_paths = [
            item["path"]
            for item in tree_data.get("tree", [])
            if item["type"] == "blob" and item["path"].endswith(".nf")
        ]

        if not nf_paths:
            raise ValueError(
                f"No .nf files found in {owner}/{repo} at {default_branch}."
            )

        # ── Step 3: fetch each .nf file ───────────────────────────────────────
        files: list[tuple[str, str]] = []
        for path in nf_paths:
            raw_url = (
                f"{_GITHUB_RAW_BASE}/{owner}/{repo}/{default_branch}/{path}"
            )
            r = client.get(raw_url)
            if r.status_code == 200:
                files.append((path, r.text))

        if not files:
            raise ValueError(f"Could not fetch any .nf files from {owner}/{repo}.")

        # ── Step 4: concatenate with path headers ─────────────────────────────
        # Each file is preceded by a comment so the combined source is still
        # valid Nextflow and the path is visible in evidence fields.
        chunks = [f"// === FILE: {path} ===\n{content}" for path, content in files]
        combined = "\n\n".join(chunks)

        return FetchedWorkflow(
            source=source,
            filename="main.nf",
            content=combined,
            files=files,
        )


# ── Shared helpers ────────────────────────────────────────────────────────────

def _parse_github_source(source: str) -> tuple[str, str]:
    if source.startswith("github:"):
        owner_repo = source.removeprefix("github:")
    else:
        path_parts = source.replace("https://github.com/", "").split("/")
        owner_repo = "/".join(path_parts[:2])
    owner, repo = owner_repo.split("/", 1)
    return owner, repo


def _resolve_default_branch(client: httpx.Client, owner: str, repo: str) -> str:
    resp = client.get(
        f"{_GITHUB_API_BASE}/repos/{owner}/{repo}",
        headers={"Accept": "application/vnd.github+json"},
    )
    resp.raise_for_status()
    return resp.json().get("default_branch", "main")