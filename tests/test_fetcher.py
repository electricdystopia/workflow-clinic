"""
Tests for the workflow fetcher.
All HTTP calls are mocked — no real network requests are made.
"""

from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest

from workflow_clinic.core.fetcher import fetch, FetchedWorkflow

# ── Minimal fixture content ───────────────────────────────────────────────────

_SAMPLE_NF = """
process ALIGN {
    container 'quay.io/biocontainers/bwa:0.7.17'
    input: path reads
    output: path "*.bam"
    script: "bwa mem ${reads} > aligned.bam"
}
""".strip()


# ── Dockstore fetcher ─────────────────────────────────────────────────────────

def _mock_dockstore_client(content: str = _SAMPLE_NF) -> MagicMock:
    """Build a mock httpx.Client that returns plausible Dockstore responses."""
    tool_response = MagicMock()
    tool_response.json.return_value = {
        "versions": [{"name": "3.14.0"}, {"name": "3.13.0"}]
    }
    tool_response.raise_for_status = MagicMock()

    desc_response = MagicMock()
    desc_response.json.return_value = {"content": content}
    desc_response.raise_for_status = MagicMock()

    mock_client = MagicMock()
    mock_client.__enter__ = MagicMock(return_value=mock_client)
    mock_client.__exit__ = MagicMock(return_value=False)
    mock_client.get.side_effect = [tool_response, desc_response]

    return mock_client


@patch("workflow_clinic.core.fetcher.httpx.Client")
def test_dockstore_returns_fetched_workflow(mock_client_cls):
    mock_client_cls.return_value = _mock_dockstore_client()
    result = fetch("dockstore:github.com/nf-core/rnaseq")
    assert isinstance(result, FetchedWorkflow)


@patch("workflow_clinic.core.fetcher.httpx.Client")
def test_dockstore_content_is_populated(mock_client_cls):
    mock_client_cls.return_value = _mock_dockstore_client()
    result = fetch("dockstore:github.com/nf-core/rnaseq")
    assert "ALIGN" in result.content


@patch("workflow_clinic.core.fetcher.httpx.Client")
def test_dockstore_filename_derived_from_repo(mock_client_cls):
    mock_client_cls.return_value = _mock_dockstore_client()
    result = fetch("dockstore:github.com/nf-core/rnaseq")
    assert result.filename == "rnaseq.nf"


@patch("workflow_clinic.core.fetcher.httpx.Client")
def test_dockstore_source_preserved(mock_client_cls):
    mock_client_cls.return_value = _mock_dockstore_client()
    source = "dockstore:github.com/nf-core/rnaseq"
    result = fetch(source)
    assert result.source == source


@patch("workflow_clinic.core.fetcher.httpx.Client")
def test_dockstore_empty_versions_raises(mock_client_cls):
    tool_response = MagicMock()
    tool_response.json.return_value = {"versions": []}
    tool_response.raise_for_status = MagicMock()

    mock_client = MagicMock()
    mock_client.__enter__ = MagicMock(return_value=mock_client)
    mock_client.__exit__ = MagicMock(return_value=False)
    mock_client.get.return_value = tool_response
    mock_client_cls.return_value = mock_client

    with pytest.raises(ValueError, match="No versions found"):
        fetch("dockstore:github.com/nf-core/rnaseq")


# ── GitHub fetcher ────────────────────────────────────────────────────────────

def _mock_github_client(content: str = _SAMPLE_NF) -> MagicMock:
    """Build a mock httpx.Client that returns plausible GitHub responses."""
    repo_response = MagicMock()
    repo_response.json.return_value = {"default_branch": "master"}
    repo_response.raise_for_status = MagicMock()

    nf_response = MagicMock()
    nf_response.status_code = 200
    nf_response.text = content

    mock_client = MagicMock()
    mock_client.__enter__ = MagicMock(return_value=mock_client)
    mock_client.__exit__ = MagicMock(return_value=False)
    mock_client.get.side_effect = [repo_response, nf_response]

    return mock_client


@patch("workflow_clinic.core.fetcher.httpx.Client")
def test_github_https_url_returns_fetched_workflow(mock_client_cls):
    mock_client_cls.return_value = _mock_github_client()
    result = fetch("https://github.com/nf-core/rnaseq")
    assert isinstance(result, FetchedWorkflow)


@patch("workflow_clinic.core.fetcher.httpx.Client")
def test_github_shorthand_url_works(mock_client_cls):
    mock_client_cls.return_value = _mock_github_client()
    result = fetch("github:nf-core/rnaseq")
    assert isinstance(result, FetchedWorkflow)


@patch("workflow_clinic.core.fetcher.httpx.Client")
def test_github_content_is_populated(mock_client_cls):
    mock_client_cls.return_value = _mock_github_client()
    result = fetch("https://github.com/nf-core/rnaseq")
    assert "ALIGN" in result.content


@patch("workflow_clinic.core.fetcher.httpx.Client")
def test_github_filename_is_main_nf(mock_client_cls):
    mock_client_cls.return_value = _mock_github_client()
    result = fetch("https://github.com/nf-core/rnaseq")
    assert result.filename == "main.nf"


@patch("workflow_clinic.core.fetcher.httpx.Client")
def test_github_all_candidates_fail_raises(mock_client_cls):
    repo_response = MagicMock()
    repo_response.json.return_value = {"default_branch": "main"}
    repo_response.raise_for_status = MagicMock()

    not_found = MagicMock()
    not_found.status_code = 404

    mock_client = MagicMock()
    mock_client.__enter__ = MagicMock(return_value=mock_client)
    mock_client.__exit__ = MagicMock(return_value=False)
    # First call = repo API, then all candidate .nf fetches return 404
    mock_client.get.side_effect = [repo_response, not_found, not_found, not_found]
    mock_client_cls.return_value = mock_client

    with pytest.raises(ValueError, match="Could not find"):
        fetch("https://github.com/some/repo")


# ── Router ────────────────────────────────────────────────────────────────────

def test_unrecognised_source_raises():
    with pytest.raises(ValueError, match="Unrecognised remote source"):
        fetch("ftp://some.random.url/workflow.nf")