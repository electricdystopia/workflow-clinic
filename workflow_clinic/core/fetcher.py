"""
Workflow fetcher — resolves a source string (local path, GitHub URL,
or Dockstore TRS identifier) into raw .nf file content.
"""

from __future__ import annotations

import urllib.parse
from dataclasses import dataclass
from pathlib import Path

import httpx


@dataclass
class FetchedWorkflow:
    """
    The result of fetching a workflow from any source.
    Always contains a filename and the raw .nf content as a string —
    the caller doesn't need to know where it came from.
    """
    source:   str   # original identifier, for display and report metadata
    filename: str   # suggested filename (e.g. "main.nf")
    content:  str   # raw file content


# ── Constants ─────────────────────────────────────────────────────────────────

_DOCKSTORE_TRS_BASE = "https://dockstore.org/api/ga4gh/trs/v2"
_GITHUB_RAW_BASE    = "https://raw.githubusercontent.com"
_GITHUB_API_BASE    = "https://api.github.com"


# ── Public entry point ────────────────────────────────────────────────────────

def fetch(source: str) -> FetchedWorkflow:
    """
    Route a source string to the correct fetcher and return a FetchedWorkflow.

    Supported formats:
        dockstore:github.com/owner/repo        → Dockstore TRS API
        https://github.com/owner/repo          → GitHub raw content
        github:owner/repo                      → GitHub raw content (shorthand)
    """
    if source.startswith("dockstore:"):
        return _fetch_dockstore(source)
    elif "github.com" in source:
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
    """
    Fetch the primary Nextflow descriptor from Dockstore via the TRS v2 API.

    Steps:
      1. GET /tools/{id}              → tool metadata + list of versions
      2. Pick the most recent version
      3. GET /tools/{id}/versions/{version_id}/NEXTFLOW/descriptor
         → raw .nf content
    """
    repo_path = source.removeprefix("dockstore:")
    tool_id   = f"#workflow/{repo_path}"
    encoded   = urllib.parse.quote(tool_id, safe="")

    with httpx.Client(timeout=30) as client:

        # ── Step 1: tool metadata ─────────────────────────────────────────────
        tool_resp = client.get(f"{_DOCKSTORE_TRS_BASE}/tools/{encoded}")
        tool_resp.raise_for_status()
        tool_data = tool_resp.json()

        versions = tool_data.get("versions", [])
        if not versions:
            raise ValueError(f"No versions found for '{source}' on Dockstore.")

        # Dockstore returns versions newest-first
        version_name = versions[0]["name"]
        version_id   = urllib.parse.quote(version_name, safe="")

        # ── Step 2: primary descriptor ────────────────────────────────────────
        desc_url  = (
            f"{_DOCKSTORE_TRS_BASE}/tools/{encoded}"
            f"/versions/{version_id}/NEXTFLOW/descriptor"
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


# ── GitHub fetcher ────────────────────────────────────────────────────────────

def _fetch_github(source: str) -> FetchedWorkflow:
    """
    Fetch main.nf from a public GitHub repository.

    Steps:
      1. GET /repos/{owner}/{repo}    → resolve default branch name
      2. GET raw main.nf from default branch via raw.githubusercontent.com
         Falls back to trying workflows/main.nf if root main.nf is not found.

    Accepts:
        https://github.com/owner/repo[/...]
        github:owner/repo
    """
    # ── Normalise to "owner/repo" ─────────────────────────────────────────────
    if source.startswith("github:"):
        owner_repo = source.removeprefix("github:")
    else:
        # strip protocol and host, take first two path segments
        path_parts = source.replace("https://github.com/", "").split("/")
        owner_repo = "/".join(path_parts[:2])

    owner, repo = owner_repo.split("/", 1)

    with httpx.Client(timeout=30) as client:

        # ── Step 1: resolve default branch ───────────────────────────────────
        repo_resp = client.get(
            f"{_GITHUB_API_BASE}/repos/{owner}/{repo}",
            headers={"Accept": "application/vnd.github+json"},
        )
        repo_resp.raise_for_status()
        default_branch = repo_resp.json().get("default_branch", "main")

        # ── Step 2: fetch main.nf, fall back to workflows/main.nf ────────────
        candidates = ["main.nf", "workflows/main.nf", f"{repo}.nf"]
        for candidate in candidates:
            raw_url  = (
                f"{_GITHUB_RAW_BASE}/{owner}/{repo}"
                f"/{default_branch}/{candidate}"
            )
            nf_resp = client.get(raw_url)
            if nf_resp.status_code == 200:
                return FetchedWorkflow(
                    source=source,
                    filename=candidate.split("/")[-1],
                    content=nf_resp.text,
                )

        raise ValueError(
            f"Could not find a .nf entry point in {owner}/{repo}. "
            f"Tried: {', '.join(candidates)}"
        )