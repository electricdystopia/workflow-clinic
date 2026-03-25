"""
Model-agnostic LLM client.
Reads OLLAMA_MODEL, OPENAI_API_KEY, ANTHROPIC_API_KEY, or GEMINI_API_KEY
from the environment and routes to the correct provider automatically.

Provider priority: OLLAMA → OpenAI → Anthropic → Gemini

If no key is set the client raises a clear error at call time, not at import
time — so the rest of the tool still works without any key.

All providers are wrapped with exponential backoff so transient 429 / 503
errors (common on free-tier APIs when the Doctor fires multiple calls in quick
succession) are retried automatically rather than surfaced as failures.
"""

from __future__ import annotations

import os
import time
import random

import httpx


# ── Retry helper ──────────────────────────────────────────────────────────────

def _with_backoff(fn, *, max_attempts: int = 4, base_delay: float = 2.0):
    """
    Call fn() up to max_attempts times.  On a 429 or 503 response, wait with
    full-jitter exponential backoff before retrying.  Any other HTTP error is
    re-raised immediately.

    Delay schedule (approximate): 1s, 2s, 4s  (randomised ±50%)
    """
    for attempt in range(max_attempts):
        try:
            return fn()
        except httpx.HTTPStatusError as exc:
            if exc.response.status_code not in (429, 503):
                raise
            if attempt == max_attempts - 1:
                raise
            # full-jitter: sleep between 0 and base * 2^attempt seconds
            cap = base_delay * (2 ** attempt)
            delay = random.uniform(0, cap)
            time.sleep(delay)


# ── Client ────────────────────────────────────────────────────────────────────

class LLMClient:

    def complete(self, prompt: str) -> str:
        """
        Send a prompt and return the text response.
        Tries OLLAMA first, then OpenAI, then Anthropic, then Gemini.
        """
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
                "No LLM configured. Set one of:\n"
                "  export GEMINI_API_KEY=...        (free tier, rate-limited)\n"
                "  export OLLAMA_MODEL=llama3.2     (fully local, no limits)\n"
                "  export OPENAI_API_KEY=...\n"
                "  export ANTHROPIC_API_KEY=..."
            )

    # ── Ollama (local) ────────────────────────────────────────────────────────

    def _ollama(self, prompt: str) -> str:
        model = os.environ["OLLAMA_MODEL"]
        base_url = os.getenv("OLLAMA_HOST", "http://localhost:11434")

        def _call():
            resp = httpx.post(
                f"{base_url}/api/generate",
                json={"model": model, "prompt": prompt, "stream": False},
                timeout=120,   # local models can be slow on first load
            )
            resp.raise_for_status()
            return resp.json()["response"].strip()

        return _with_backoff(_call)

    # ── OpenAI ────────────────────────────────────────────────────────────────

    def _openai(self, prompt: str) -> str:
        def _call():
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
            return resp.json()["choices"][0]["message"]["content"].strip()

        return _with_backoff(_call)

    # ── Anthropic ─────────────────────────────────────────────────────────────

    def _anthropic(self, prompt: str) -> str:
        def _call():
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
            return resp.json()["content"][0]["text"].strip()

        return _with_backoff(_call)

    # ── Gemini ────────────────────────────────────────────────────────────────

    def _gemini(self, prompt: str) -> str:
        def _call():
            resp = httpx.post(
                "https://generativelanguage.googleapis.com/v1beta/models"
                "/gemini-2.0-flash:generateContent",
                params={"key": os.environ["GEMINI_API_KEY"]},
                json={"contents": [{"parts": [{"text": prompt}]}]},
                timeout=30,
            )
            resp.raise_for_status()
            return resp.json()["candidates"][0]["content"]["parts"][0]["text"].strip()

        return _with_backoff(_call)