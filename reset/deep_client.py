#!/usr/bin/env python3
"""
deep_client.py — minimal, dependency-free client for the DeepSeek research model
exposed through an Anthropic-compatible Messages endpoint.

Credentials (env, same names the vendor documents):
    ANTHROPIC_BASE_URL   e.g. https://api.hcnsec.cn/
    ANTHROPIC_AUTH_TOKEN e.g. sk-...
    ANTHROPIC_MODEL      e.g. DeepSeek-V4-Pro

Uses only the Python standard library (urllib) so it runs on a bare VPS with no
pip installs. Handles: long research answers (large max_tokens), generous timeout,
exponential-backoff retries, and both `x-api-key` and `Authorization: Bearer`
auth headers (proxies differ on which they accept).
"""
from __future__ import annotations

import json
import time
import urllib.request
import urllib.error


class DeepError(Exception):
    pass


class DeepClient:
    def __init__(
        self,
        base_url: str,
        token: str,
        model: str,
        *,
        max_tokens: int = 16000,
        timeout: int = 600,
        max_retries: int = 5,
    ):
        if not base_url or not token or not model:
            raise DeepError(
                "Missing credentials — set ANTHROPIC_BASE_URL, ANTHROPIC_AUTH_TOKEN, ANTHROPIC_MODEL."
            )
        self.base_url = base_url.rstrip("/")
        self.token = token
        self.model = model
        self.max_tokens = max_tokens
        self.timeout = timeout
        self.max_retries = max_retries

    @property
    def endpoint(self) -> str:
        return f"{self.base_url}/v1/messages"

    def complete(self, prompt: str, *, system: str | None = None) -> str:
        """Send one user message, return the assistant's text. Retries on transient errors."""
        payload = {
            "model": self.model,
            "max_tokens": self.max_tokens,
            "messages": [{"role": "user", "content": prompt}],
        }
        if system:
            payload["system"] = system
        body = json.dumps(payload).encode("utf-8")
        headers = {
            "content-type": "application/json",
            "anthropic-version": "2023-06-01",
            "x-api-key": self.token,
            "authorization": f"Bearer {self.token}",
        }

        last_err: Exception | None = None
        for attempt in range(1, self.max_retries + 1):
            try:
                req = urllib.request.Request(
                    self.endpoint, data=body, headers=headers, method="POST"
                )
                with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                    data = json.loads(resp.read().decode("utf-8"))
                return self._extract_text(data)
            except urllib.error.HTTPError as e:
                detail = e.read().decode("utf-8", errors="replace")[:500]
                last_err = DeepError(f"HTTP {e.code}: {detail}")
                # 4xx (except 429) won't fix themselves — fail fast.
                if e.code < 500 and e.code != 429:
                    raise last_err
            except (urllib.error.URLError, TimeoutError, ConnectionError, OSError) as e:
                last_err = DeepError(f"network error: {e}")
            except (json.JSONDecodeError, DeepError) as e:
                last_err = DeepError(f"bad response: {e}")

            if attempt < self.max_retries:
                backoff = min(60, 5 * (2 ** (attempt - 1)))
                time.sleep(backoff)
        raise last_err or DeepError("unknown error")

    @staticmethod
    def _extract_text(data: dict) -> str:
        """Anthropic Messages shape: {content:[{type:'text',text:...}]}. Fall back to
        OpenAI-style {choices:[{message:{content}}]} in case the proxy switches format."""
        content = data.get("content")
        if isinstance(content, list):
            parts = [b.get("text", "") for b in content if isinstance(b, dict) and b.get("type") == "text"]
            text = "".join(parts).strip()
            if text:
                return text
        choices = data.get("choices")
        if isinstance(choices, list) and choices:
            msg = choices[0].get("message", {})
            if isinstance(msg, dict) and msg.get("content"):
                return str(msg["content"]).strip()
        raise DeepError(f"no text in response: {json.dumps(data)[:300]}")


def from_env() -> "DeepClient":
    import os
    return DeepClient(
        base_url=os.environ.get("ANTHROPIC_BASE_URL", ""),
        token=os.environ.get("ANTHROPIC_AUTH_TOKEN", ""),
        model=os.environ.get("ANTHROPIC_MODEL", ""),
        max_tokens=int(os.environ.get("DEEP_MAX_TOKENS", "16000")),
        timeout=int(os.environ.get("DEEP_TIMEOUT", "600")),
        max_retries=int(os.environ.get("DEEP_MAX_RETRIES", "5")),
    )
