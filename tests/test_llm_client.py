"""
Tests for the LLM client routing logic.
Actual HTTP calls are mocked — no API key required.
"""

from __future__ import annotations

import os
from unittest.mock import MagicMock, patch

import pytest

from workflow_clinic.core.llm_client import LLMClient


def _mock_response(text: str) -> MagicMock:
    resp = MagicMock()
    resp.raise_for_status = MagicMock()
    return resp


# ── Provider routing ──────────────────────────────────────────────────────────

def test_no_key_raises_environment_error(monkeypatch):
    monkeypatch.delenv("OLLAMA_MODEL",    raising=False)
    monkeypatch.delenv("OPENAI_API_KEY",  raising=False)
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    monkeypatch.delenv("GEMINI_API_KEY",  raising=False)

    with pytest.raises(EnvironmentError, match="No LLM configured"):
        LLMClient().complete("hello")


def test_gemini_is_called_when_key_is_set(monkeypatch):
    monkeypatch.delenv("OLLAMA_MODEL",      raising=False)
    monkeypatch.delenv("OPENAI_API_KEY",    raising=False)
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    monkeypatch.setenv("GEMINI_API_KEY",    "test-key")

    with patch("workflow_clinic.core.llm_client.httpx.post") as mock_post:
        mock_post.return_value.raise_for_status = MagicMock()
        mock_post.return_value.json.return_value = {
            "candidates": [{"content": {"parts": [{"text": "quay.io/tool:1.0"}]}}]
        }
        result = LLMClient().complete("suggest an image")

    assert result == "quay.io/tool:1.0"
    assert "generativelanguage" in mock_post.call_args[0][0]


def test_openai_is_called_when_key_is_set(monkeypatch):
    monkeypatch.delenv("OLLAMA_MODEL",      raising=False)
    monkeypatch.setenv("OPENAI_API_KEY",    "test-key")
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    monkeypatch.delenv("GEMINI_API_KEY",    raising=False)

    with patch("workflow_clinic.core.llm_client.httpx.post") as mock_post:
        mock_post.return_value.raise_for_status = MagicMock()
        mock_post.return_value.json.return_value = {
            "choices": [{"message": {"content": "quay.io/tool:1.0"}}]
        }
        result = LLMClient().complete("suggest an image")

    assert result == "quay.io/tool:1.0"
    assert "openai" in mock_post.call_args[0][0]


def test_anthropic_is_called_when_key_is_set(monkeypatch):
    monkeypatch.delenv("OLLAMA_MODEL",      raising=False)
    monkeypatch.delenv("OPENAI_API_KEY",    raising=False)
    monkeypatch.setenv("ANTHROPIC_API_KEY", "test-key")
    monkeypatch.delenv("GEMINI_API_KEY",    raising=False)

    with patch("workflow_clinic.core.llm_client.httpx.post") as mock_post:
        mock_post.return_value.raise_for_status = MagicMock()
        mock_post.return_value.json.return_value = {
            "content": [{"text": "quay.io/tool:1.0"}]
        }
        result = LLMClient().complete("suggest an image")

    assert result == "quay.io/tool:1.0"
    assert "anthropic" in mock_post.call_args[0][0]


def test_ollama_takes_priority_over_all(monkeypatch):
    monkeypatch.setenv("OLLAMA_MODEL",      "deepseek-coder:6.7b")
    monkeypatch.setenv("OPENAI_API_KEY",    "test-key")
    monkeypatch.setenv("ANTHROPIC_API_KEY", "test-key")
    monkeypatch.setenv("GEMINI_API_KEY",    "test-key")

    with patch("workflow_clinic.core.llm_client.httpx.post") as mock_post:
        mock_post.return_value.raise_for_status = MagicMock()
        # Ollama /api/generate returns {"response": "..."} not OpenAI format
        mock_post.return_value.json.return_value = {"response": "quay.io/tool:1.0"}
        result = LLMClient().complete("suggest an image")

    assert result == "quay.io/tool:1.0"
    assert "11434" in mock_post.call_args[0][0]