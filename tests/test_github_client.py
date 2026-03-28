"""
Tests for GitHubClient.

All HTTP calls are mocked with unittest.mock.patch — no network requests,
no GITHUB_TOKEN required.  The mock pattern mirrors test_fetcher.py:
mock_client_cls.return_value is a single MagicMock used as the context
manager AND for sequencing get/post/put side_effects across calls.
"""

from __future__ import annotations

from unittest.mock import MagicMock, call, patch

import httpx
import pytest

from workflow_clinic.core.github_client import GitHubClient, _label_color


# ── Helpers ───────────────────────────────────────────────────────────────────

def _mock_client() -> MagicMock:
    """Return a mock httpx.Client suitable for use as mock_client_cls.return_value."""
    mock = MagicMock()
    mock.__enter__ = MagicMock(return_value=mock)
    mock.__exit__  = MagicMock(return_value=False)
    return mock


def _resp(data: object, status: int = 200) -> MagicMock:
    """Return a mock httpx.Response with given JSON body and status code."""
    r = MagicMock()
    r.status_code = status
    r.raise_for_status = MagicMock()
    r.json.return_value = data
    return r


def _err_resp(status: int) -> MagicMock:
    """Return a mock response whose raise_for_status raises HTTPStatusError."""
    r = MagicMock()
    r.status_code = status
    fake = MagicMock()
    fake.status_code = status
    r.raise_for_status.side_effect = httpx.HTTPStatusError(
        f"HTTP {status}", request=MagicMock(), response=fake
    )
    return r


# ── _label_color ──────────────────────────────────────────────────────────────

def test_label_color_known_label():
    assert _label_color("workflow-clinic") == "0075ca"

def test_label_color_severity_critical():
    assert _label_color("severity:critical") == "d73a4a"

def test_label_color_unknown_falls_back_to_purple():
    assert _label_color("gap:containerization") == "7057ff"

def test_label_color_no_hash_prefix():
    color = _label_color("workflow-clinic")
    assert not color.startswith("#")
    assert len(color) == 6


# ── create_issue ──────────────────────────────────────────────────────────────

@patch("workflow_clinic.core.github_client.httpx.Client")
def test_create_issue_returns_html_url(mock_cls):
    mock = _mock_client()
    mock_cls.return_value = mock
    mock.post.return_value = _resp(
        {"html_url": "https://github.com/owner/repo/issues/42"}
    )

    client = GitHubClient("tok")
    url = client.create_issue("owner", "repo", "title", "body", [])

    assert url == "https://github.com/owner/repo/issues/42"


@patch("workflow_clinic.core.github_client.httpx.Client")
def test_create_issue_posts_to_correct_endpoint(mock_cls):
    mock = _mock_client()
    mock_cls.return_value = mock
    mock.post.return_value = _resp({"html_url": "https://github.com/o/r/issues/1"})

    GitHubClient("tok").create_issue("o", "r", "t", "b", [])

    posted_url = mock.post.call_args[0][0]
    assert "repos/o/r/issues" in posted_url


@patch("workflow_clinic.core.github_client.httpx.Client")
def test_create_issue_passes_labels(mock_cls):
    mock = _mock_client()
    mock_cls.return_value = mock
    mock.post.return_value = _resp({"html_url": "https://github.com/o/r/issues/1"})

    GitHubClient("tok").create_issue("o", "r", "title", "body", [])

    payload = mock.post.call_args[1]["json"]
    assert "labels" in payload


@patch("workflow_clinic.core.github_client.httpx.Client")
def test_create_issue_calls_ensure_labels_when_labels_given(mock_cls):
    """ensure_labels is invoked before the issue POST when labels are non-empty."""
    mock = _mock_client()
    mock_cls.return_value = mock

    # GET for ensure_labels — no existing labels
    mock.get.return_value = _resp([])
    # POST for label creation, then issue creation
    mock.post.side_effect = [
        _resp({"name": "workflow-clinic"}, status=201),
        _resp({"html_url": "https://github.com/o/r/issues/1"}),
    ]

    url = GitHubClient("tok").create_issue(
        "o", "r", "t", "b", ["workflow-clinic"]
    )
    assert url == "https://github.com/o/r/issues/1"
    # One GET (list labels) + two POSTs (create label + create issue)
    assert mock.get.call_count  == 1
    assert mock.post.call_count == 2


@patch("workflow_clinic.core.github_client.httpx.Client")
def test_create_issue_skips_ensure_labels_when_labels_empty(mock_cls):
    mock = _mock_client()
    mock_cls.return_value = mock
    mock.post.return_value = _resp({"html_url": "https://github.com/o/r/issues/1"})

    GitHubClient("tok").create_issue("o", "r", "t", "b", [])

    assert mock.get.call_count == 0   # ensure_labels not called


# ── find_existing_issue ───────────────────────────────────────────────────────

@patch("workflow_clinic.core.github_client.httpx.Client")
def test_find_existing_issue_returns_number_on_match(mock_cls):
    mock = _mock_client()
    mock_cls.return_value = mock
    mock.get.return_value = _resp([
        {"number": 7, "title": "[Workflow Clinic] 3 gaps in process ALIGN"},
        {"number": 8, "title": "Unrelated issue"},
    ])

    result = GitHubClient("tok").find_existing_issue("o", "r", "[Workflow Clinic]")

    assert result == 7


@patch("workflow_clinic.core.github_client.httpx.Client")
def test_find_existing_issue_returns_none_when_no_match(mock_cls):
    mock = _mock_client()
    mock_cls.return_value = mock
    mock.get.return_value = _resp([
        {"number": 5, "title": "Totally unrelated issue"},
    ])

    result = GitHubClient("tok").find_existing_issue("o", "r", "[Workflow Clinic]")

    assert result is None


@patch("workflow_clinic.core.github_client.httpx.Client")
def test_find_existing_issue_returns_none_on_empty_list(mock_cls):
    mock = _mock_client()
    mock_cls.return_value = mock
    mock.get.return_value = _resp([])

    assert GitHubClient("tok").find_existing_issue("o", "r", "anything") is None


@patch("workflow_clinic.core.github_client.httpx.Client")
def test_find_existing_issue_queries_open_issues_with_label(mock_cls):
    mock = _mock_client()
    mock_cls.return_value = mock
    mock.get.return_value = _resp([])

    GitHubClient("tok").find_existing_issue("o", "r", "X")

    params = mock.get.call_args[1]["params"]
    assert params["state"]  == "open"
    assert params["labels"] == "workflow-clinic"


# ── add_comment ───────────────────────────────────────────────────────────────

@patch("workflow_clinic.core.github_client.httpx.Client")
def test_add_comment_returns_url(mock_cls):
    mock = _mock_client()
    mock_cls.return_value = mock
    mock.post.return_value = _resp(
        {"html_url": "https://github.com/o/r/issues/7#issuecomment-999"}
    )

    url = GitHubClient("tok").add_comment("o", "r", 7, "body text")

    assert "issuecomment" in url


@patch("workflow_clinic.core.github_client.httpx.Client")
def test_add_comment_posts_to_correct_endpoint(mock_cls):
    mock = _mock_client()
    mock_cls.return_value = mock
    mock.post.return_value = _resp({"html_url": "https://github.com/o/r/issues/3#c1"})

    GitHubClient("tok").add_comment("o", "r", 3, "hello")

    posted_url = mock.post.call_args[0][0]
    assert "issues/3/comments" in posted_url


# ── ensure_labels ─────────────────────────────────────────────────────────────

@patch("workflow_clinic.core.github_client.httpx.Client")
def test_ensure_labels_creates_missing_labels(mock_cls):
    mock = _mock_client()
    mock_cls.return_value = mock
    # GET returns no existing labels
    mock.get.return_value = _resp([])
    mock.post.return_value = _resp({"name": "workflow-clinic"}, status=201)

    GitHubClient("tok").ensure_labels("o", "r", ["workflow-clinic", "severity:critical"])

    assert mock.post.call_count == 2


@patch("workflow_clinic.core.github_client.httpx.Client")
def test_ensure_labels_skips_existing_labels(mock_cls):
    mock = _mock_client()
    mock_cls.return_value = mock
    # GET returns the label already existing
    mock.get.return_value = _resp([{"name": "workflow-clinic"}])

    GitHubClient("tok").ensure_labels("o", "r", ["workflow-clinic"])

    assert mock.post.call_count == 0   # no POST needed


@patch("workflow_clinic.core.github_client.httpx.Client")
def test_ensure_labels_ignores_422_on_create(mock_cls):
    """A 422 during label creation means a race condition — should not raise."""
    mock = _mock_client()
    mock_cls.return_value = mock
    mock.get.return_value = _resp([])
    mock.post.return_value = _resp({}, status=422)
    mock.post.return_value.status_code = 422
    mock.post.return_value.raise_for_status = MagicMock()  # not called

    # Should complete without raising
    GitHubClient("tok").ensure_labels("o", "r", ["workflow-clinic"])


# ── get_default_branch ────────────────────────────────────────────────────────

@patch("workflow_clinic.core.github_client.httpx.Client")
def test_get_default_branch_returns_value(mock_cls):
    mock = _mock_client()
    mock_cls.return_value = mock
    mock.get.return_value = _resp({"default_branch": "develop"})

    branch = GitHubClient("tok").get_default_branch("o", "r")

    assert branch == "develop"


@patch("workflow_clinic.core.github_client.httpx.Client")
def test_get_default_branch_falls_back_to_main(mock_cls):
    mock = _mock_client()
    mock_cls.return_value = mock
    mock.get.return_value = _resp({})   # no default_branch key

    branch = GitHubClient("tok").get_default_branch("o", "r")

    assert branch == "main"


# ── create_branch ─────────────────────────────────────────────────────────────

@patch("workflow_clinic.core.github_client.httpx.Client")
def test_create_branch_resolves_base_sha_then_creates_ref(mock_cls):
    mock = _mock_client()
    mock_cls.return_value = mock
    # First GET: ref lookup for base branch SHA
    mock.get.return_value  = _resp({"object": {"sha": "deadbeef"}})
    mock.post.return_value = _resp({"ref": "refs/heads/wf-clinic/container-001/align"})

    GitHubClient("tok").create_branch("o", "r", "main", "wf-clinic/container-001/align")

    # Verify the POST payload contains the resolved SHA
    posted = mock.post.call_args[1]["json"]
    assert posted["sha"]              == "deadbeef"
    assert posted["ref"].startswith("refs/heads/")


@patch("workflow_clinic.core.github_client.httpx.Client")
def test_create_branch_encodes_branch_name_in_ref(mock_cls):
    mock = _mock_client()
    mock_cls.return_value = mock
    mock.get.return_value  = _resp({"object": {"sha": "abc123"}})
    mock.post.return_value = _resp({})

    GitHubClient("tok").create_branch("o", "r", "main", "feature/my-branch")

    payload = mock.post.call_args[1]["json"]
    assert payload["ref"] == "refs/heads/feature/my-branch"


# ── commit_file ───────────────────────────────────────────────────────────────

@patch("workflow_clinic.core.github_client.httpx.Client")
def test_commit_file_new_file_skips_sha(mock_cls):
    """For a new file (404 on GET), PUT must not include a 'sha' key."""
    mock = _mock_client()
    mock_cls.return_value = mock

    not_found = MagicMock()
    not_found.status_code = 404
    not_found.raise_for_status = MagicMock()   # not called for 404

    mock.get.return_value = not_found
    mock.put.return_value = _resp({"content": {"sha": "newsha"}})

    GitHubClient("tok").commit_file("o", "r", "main", "workflow.nf", "content", "msg")

    put_payload = mock.put.call_args[1]["json"]
    assert "sha" not in put_payload


@patch("workflow_clinic.core.github_client.httpx.Client")
def test_commit_file_existing_file_includes_sha(mock_cls):
    """For an existing file (200 on GET), PUT must include the file's current sha."""
    mock = _mock_client()
    mock_cls.return_value = mock

    exists = MagicMock()
    exists.status_code = 200
    exists.raise_for_status = MagicMock()
    exists.json.return_value = {"sha": "existingsha", "content": "..."}

    mock.get.return_value = exists
    mock.put.return_value = _resp({"content": {"sha": "newsha"}})

    GitHubClient("tok").commit_file("o", "r", "main", "workflow.nf", "content", "msg")

    put_payload = mock.put.call_args[1]["json"]
    assert put_payload["sha"] == "existingsha"


@patch("workflow_clinic.core.github_client.httpx.Client")
def test_commit_file_encodes_content_as_base64(mock_cls):
    import base64
    mock = _mock_client()
    mock_cls.return_value = mock

    not_found = MagicMock()
    not_found.status_code = 404
    not_found.raise_for_status = MagicMock()
    mock.get.return_value = not_found
    mock.put.return_value = _resp({})

    GitHubClient("tok").commit_file(
        "o", "r", "main", "workflow.nf", "hello world", "msg"
    )

    put_payload = mock.put.call_args[1]["json"]
    decoded = base64.b64decode(put_payload["content"]).decode()
    assert decoded == "hello world"


@patch("workflow_clinic.core.github_client.httpx.Client")
def test_commit_file_includes_branch_in_payload(mock_cls):
    mock = _mock_client()
    mock_cls.return_value = mock

    not_found = MagicMock()
    not_found.status_code = 404
    not_found.raise_for_status = MagicMock()
    mock.get.return_value = not_found
    mock.put.return_value = _resp({})

    GitHubClient("tok").commit_file(
        "o", "r", "fix-branch", "workflow.nf", "content", "commit msg"
    )

    put_payload = mock.put.call_args[1]["json"]
    assert put_payload["branch"]  == "fix-branch"
    assert put_payload["message"] == "commit msg"


# ── create_pull_request ───────────────────────────────────────────────────────

@patch("workflow_clinic.core.github_client.httpx.Client")
def test_create_pull_request_returns_url(mock_cls):
    mock = _mock_client()
    mock_cls.return_value = mock
    mock.post.return_value = _resp(
        {"html_url": "https://github.com/o/r/pull/99"}
    )

    url = GitHubClient("tok").create_pull_request(
        "o", "r", "fix-branch", "main", "title", "body"
    )

    assert url == "https://github.com/o/r/pull/99"


@patch("workflow_clinic.core.github_client.httpx.Client")
def test_create_pull_request_payload_fields(mock_cls):
    mock = _mock_client()
    mock_cls.return_value = mock
    mock.post.return_value = _resp({"html_url": "https://github.com/o/r/pull/1"})

    GitHubClient("tok").create_pull_request(
        "o", "r", "feat-branch", "main", "My PR", "PR body text"
    )

    payload = mock.post.call_args[1]["json"]
    assert payload["head"]  == "feat-branch"
    assert payload["base"]  == "main"
    assert payload["title"] == "My PR"
    assert payload["body"]  == "PR body text"


@patch("workflow_clinic.core.github_client.httpx.Client")
def test_create_pull_request_posts_to_correct_endpoint(mock_cls):
    mock = _mock_client()
    mock_cls.return_value = mock
    mock.post.return_value = _resp({"html_url": "https://github.com/o/r/pull/1"})

    GitHubClient("tok").create_pull_request("o", "r", "h", "b", "t", "body")

    posted_url = mock.post.call_args[0][0]
    assert "repos/o/r/pulls" in posted_url


# ── Authorization header ──────────────────────────────────────────────────────

@patch("workflow_clinic.core.github_client.httpx.Client")
def test_authorization_header_is_bearer_token(mock_cls):
    mock = _mock_client()
    mock_cls.return_value = mock
    mock.post.return_value = _resp({"html_url": "https://github.com/o/r/issues/1"})

    GitHubClient("my-secret-token").create_issue("o", "r", "t", "b", [])

    headers = mock.post.call_args[1]["headers"]
    assert headers["Authorization"] == "Bearer my-secret-token"


@patch("workflow_clinic.core.github_client.httpx.Client")
def test_github_api_version_header_is_set(mock_cls):
    mock = _mock_client()
    mock_cls.return_value = mock
    mock.post.return_value = _resp({"html_url": "https://github.com/o/r/issues/1"})

    GitHubClient("tok").create_issue("o", "r", "t", "b", [])

    headers = mock.post.call_args[1]["headers"]
    assert headers.get("X-GitHub-Api-Version") == "2022-11-28"