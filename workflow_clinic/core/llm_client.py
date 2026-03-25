"""
Model-agnostic LLM client.
Reads OLLAMA_MODEL, OPENAI_API_KEY, ANTHROPIC_API_KEY, or GEMINI_API_KEY
from the environment and routes to the correct provider automatically.
"""

from __future__ import annotations

import os
import time
import random
from typing import Callable, TypeVar

import httpx

T = TypeVar("T")


# ── Retry helper ──────────────────────────────────────────────────────────────

def _with_backoff(fn: Callable[[], T], *, max_attempts: int = 4, base_delay: float = 2.0) -> T:
    for attempt in range(max_attempts):
        try:
            return fn()
        except httpx.HTTPStatusError as exc:
            if exc.response.status_code not in (429, 503):
                raise
            if attempt == max_attempts - 1:
                raise
            cap = base_delay * (2 ** attempt)
            delay = random.uniform(0, cap)
            time.sleep(delay)
    raise RuntimeError("unreachable")


# ── Client ────────────────────────────────────────────────────────────────────

class LLMClient:

    def complete(self, prompt: str) -> str:
        if os.getenv("OLLAMA_MODEL"):
            return self._ollama(prompt)
        elif os.getenv("OPENAI_API_KEY"):
            return self._openai(prompt)
        elif os.getenv("ANTHROPIC_API_KEY"):
            return self._anthropic(prompt)
        elif os.getenv("GEMINI_API_KEY"):
            return self._gemini(prompt)
        else:
            raise EnvironmentError(
                "No LLM configured. Options:\n"
                "  export GEMINI_API_KEY=...        (free, no card)\n"
                "  export OLLAMA_MODEL=llama3.2     (fully local)\n"
                "  export OPENAI_API_KEY=...\n"
                "  export ANTHROPIC_API_KEY=..."
            )

    def _ollama(self, prompt: str) -> str:
        model    = os.environ["OLLAMA_MODEL"]
        base_url = os.getenv("OLLAMA_HOST", "http://localhost:11434")

        def _call() -> str:
            resp = httpx.post(
                f"{base_url}/api/generate",
                json={"model": model, "prompt": prompt, "stream": False},
                timeout=120,
            )
            resp.raise_for_status()
            result: str = resp.json()["response"].strip()
            return result

        return _with_backoff(_call)

    def _openai(self, prompt: str) -> str:
        def _call() -> str:
            resp = httpx.post(
                "https://api.openai.com/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {os.environ['OPENAI_API_KEY']}",
                    "Content-Type": "application/json",
                },
                json={
                    "model": "gpt-4o-mini",
                    "messages": [{"role": "user", "content": prompt}],
                    "temperature": 0.1,
                    "max_tokens": 256,
                },
                timeout=30,
            )
            resp.raise_for_status()
            result: str = resp.json()["choices"][0]["message"]["content"].strip()
            return result

        return _with_backoff(_call)

    def _anthropic(self, prompt: str) -> str:
        def _call() -> str:
            resp = httpx.post(
                "https://api.anthropic.com/v1/messages",
                headers={
                    "x-api-key": os.environ["ANTHROPIC_API_KEY"],
                    "anthropic-version": "2023-06-01",
                    "Content-Type": "application/json",
                },
                json={
                    "model": "claude-haiku-4-5-20251001",
                    "max_tokens": 256,
                    "messages": [{"role": "user", "content": prompt}],
                },
                timeout=30,
            )
            resp.raise_for_status()
            result: str = resp.json()["content"][0]["text"].strip()
            return result

        return _with_backoff(_call)

    def _gemini(self, prompt: str) -> str:
        def _call() -> str:
            resp = httpx.post(
                "https://generativelanguage.googleapis.com/v1beta/models"
                "/gemini-2.0-flash:generateContent",
                params={"key": os.environ["GEMINI_API_KEY"]},
                json={"contents": [{"parts": [{"text": prompt}]}]},
                timeout=30,
            )
            resp.raise_for_status()
            result: str = resp.json()["candidates"][0]["content"]["parts"][0]["text"].strip()
            return result

        return _with_backoff(_call)