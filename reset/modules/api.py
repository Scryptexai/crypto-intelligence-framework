"""
api.py — the HTTP client for the research gateway, and nothing else.

The endpoint is OpenAI-compatible /v1/chat/completions despite the ANTHROPIC_* env var
naming -- see extract_text's docstring for how that was established the hard way.

Every function here raises on failure and lets the caller decide about retries; the only
retry policy lives in call_with_retries (transport-level). Content-quality retries are a
separate concern and live in repair.py.
"""
import json
import re
import threading
import time
import urllib.error
import urllib.request

from . import config
from .logs import log


def _reject_truncated(finish_reason, text: str) -> None:
    """Raise when the model stopped because it ran out of output budget, not because it was
    done.

    Nothing used to look at finish_reason at all, which made a max_tokens cut completely
    invisible: the client received a shorter string and treated it as a finished answer.
    Phase 11 is where that hurt most -- its prompt puts CIF SCORE CALCULATION at the very END
    of the report, so the budget runs out precisely on the one section extract_qa.py needs,
    and the failure surfaces as "no CIF Score Calculation block" rather than "the answer was
    cut off". Two self-repair attempts then regenerate a report that gets cut in the same
    place, at ~8 minutes each.

    Raising here routes it into call_with_retries' normal handling and puts the real cause in
    the log, where raising RESET_PHASE11_MAX_TOKENS is an obvious next step.
    """
    if finish_reason in ("length", "max_tokens"):
        raise RuntimeError(
            f"response truncated by the output-token limit (finish_reason={finish_reason!r}, "
            f"got {len(text)} chars). The answer is incomplete, not wrong -- raise "
            f"RESET_MAX_TOKENS (or RESET_PHASE11_MAX_TOKENS for phase 11) and retry.")


def extract_text(body: dict) -> str:
    """Parses the response permissively. Confirmed live, 2026-08-05: this proxy
    (api.hcnsec.cn, a "New API" gateway instance) does NOT implement the Anthropic Messages
    API shape at /v1/messages despite the ANTHROPIC_* env var naming convention -- POSTing
    there got the gateway's own frontend HTML back (its SPA's catch-all route for unmatched
    paths), reproduced identically via a bare curl with a trivial payload, so it was never
    about request size or retries. The real endpoint is OpenAI-compatible
    /v1/chat/completions (see call_deepseek's url), which returns the
    choices[0].message.content shape below. The Anthropic-shape check stays first only as a
    no-cost fallback in case this ever points at a genuinely Anthropic-compatible endpoint
    again."""
    # Anthropic Messages API: {"content": [{"type": "text", "text": "..."}], ...}
    content = body.get("content")
    if isinstance(content, list):
        text = "".join(p.get("text", "") for p in content
                       if isinstance(p, dict) and p.get("type") == "text")
        if text.strip():
            return text
    # OpenAI-style fallback: {"choices": [{"message": {"content": "..."}}]}
    choices = body.get("choices")
    if isinstance(choices, list) and choices:
        msg = choices[0].get("message", {}) if isinstance(choices[0], dict) else {}
        text = msg.get("content", "")
        if isinstance(text, str) and text.strip():
            _reject_truncated(choices[0].get("finish_reason"), text)
            return text
    raise ValueError(f"unrecognized response shape, no text found: {json.dumps(body)[:800]}")


def _read_sse_stream(resp) -> str:
    """Accumulate an OpenAI-style SSE completion into one string.

    Wire format is one `data: {json}` line per chunk, terminated by `data: [DONE]`, with
    blank lines and `:`-prefixed keep-alive comments interleaved. The text lives in
    choices[0].delta.content (streaming) though some gateways send a full `message` object on
    the final chunk instead, so both are accepted.
    """
    parts = []
    finish_reason = None
    for raw_line in resp:
        line = raw_line.decode("utf-8", errors="replace").strip()
        if not line or line.startswith(":"):
            continue  # keep-alive / comment
        if not line.startswith("data:"):
            continue
        payload = line[5:].strip()
        if payload == "[DONE]":
            break
        try:
            chunk = json.loads(payload)
        except json.JSONDecodeError:
            continue  # a partial/garbled frame must not abort a completed generation
        for choice in chunk.get("choices") or []:
            piece = (choice.get("delta") or {}).get("content")
            if piece is None:
                piece = (choice.get("message") or {}).get("content")
            if piece:
                parts.append(piece)
            if choice.get("finish_reason"):
                finish_reason = choice["finish_reason"]
    text = "".join(parts)
    if not text.strip():
        raise RuntimeError("stream ended with no content (no data: chunks carried text)")
    _reject_truncated(finish_reason, text)
    return text


def call_model(messages: list, base_url: str, token: str, model: str,
               max_tokens: int = None, stream: bool = None) -> str:
    """POST to {base_url}/v1/chat/completions (OpenAI-compatible -- see extract_text's
    docstring for how this was confirmed against the real endpoint, 2026-08-05). Raises on
    any failure (network, timeout, non-200, unparseable body) -- caller handles retry.

    Streaming is ON by default, and that is what makes long phases possible at all. The
    gateway returns HTTP 504 on any NON-streaming request whose generation runs past ~300s
    (measured twice on Lido at 310s and 306s) -- the classic proxy "no bytes received yet"
    timeout, since a non-streaming response sends nothing until the whole completion is
    finished. With stream=true the first token arrives within seconds and data keeps flowing,
    so that idle timer never fires and the generation may take as long as it needs. The client
    still bounds the whole thing with REQUEST_TIMEOUT_SECONDS.

    This is the reason Phase 9 does not need its prompt split: the ceiling was an artifact of
    how the request was sent, not of the phase being too big. Pass stream=False only to
    reproduce the old behaviour.
    """
    if stream is None:
        stream = config.STREAM_RESPONSES
    url = base_url.rstrip("/") + "/v1/chat/completions"
    payload = {"model": model, "max_tokens": max_tokens or config.MAX_TOKENS,
               "messages": messages, "stream": bool(stream)}
    data = json.dumps(payload).encode("utf-8")
    # Debug aid, 2026-08-05: a UA-spoofed Python request to this same URL still got the
    # gateway's fallback HTML back while an equivalent curl succeeded -- dumping the EXACT
    # outgoing body lets that same body be replayed via
    # `curl --data @reset/tmp_test/_last_request.json` to isolate whether this is
    # content/size-specific (curl fails too) or something about how urllib sends the request.
    config.TMP_TEST_ROOT.mkdir(parents=True, exist_ok=True)
    (config.TMP_TEST_ROOT / "_last_request.json").write_bytes(data)
    req = urllib.request.Request(url, data=data, method="POST")
    req.add_header("Content-Type", "application/json")
    req.add_header("Authorization", f"Bearer {token}")
    req.add_header("Accept", "application/json")
    # urllib's default User-Agent is literally "Python-urllib/3.x" -- a string commonly
    # denylisted by WAFs/anti-bot layers on gateways like this one (curl's default UA is not,
    # which was the one concrete difference between a curl POST to this same URL that got real
    # JSON back, 2026-08-05, and this script still getting fallback HTML after the
    # endpoint-path fix alone).
    req.add_header("User-Agent", "curl/8.5.0")
    try:
        with urllib.request.urlopen(req, timeout=config.REQUEST_TIMEOUT_SECONDS) as resp:
            status = resp.status
            if stream:
                ctype = (resp.headers.get("Content-Type") or "").lower()
                if "text/event-stream" in ctype:
                    return _read_sse_stream(resp)
                # Asked for a stream, got a plain body: some gateways ignore the flag. Fall
                # through and parse it as an ordinary JSON response rather than failing.
            raw = resp.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8", errors="replace")[:800]
        raise RuntimeError(f"HTTP {e.code}: {err_body}") from e
    try:
        body = json.loads(raw)
    except json.JSONDecodeError as e:
        # Bare "Expecting value: line 1 column 1 (char 0)" (json's own message) tells you
        # nothing about what the server actually sent -- a 200 with an empty body, an SSE
        # "data: {...}" stream (this script always sends a non-streaming request, but a
        # third-party proxy can still switch to streaming server-side for large responses
        # without being asked), a truncated body, or an HTML error page all produce that exact
        # same message. Surface the real bytes (bounded) so a failure is diagnosable from
        # reset/failures.log instead of needing to be reproduced live.
        snippet = raw[:500] if raw else "(empty body)"
        raise RuntimeError(
            f"HTTP {status} but response body is not valid JSON ({e}); "
            f"body length={len(raw)} chars, first 500 chars: {snippet!r}"
        ) from e
    return extract_text(body)


# Failures that mean "this endpoint cannot handle a request this big", as opposed to "try
# again in a moment". Retrying the same provider with the same payload cannot fix these -- the
# gateway timeout in particular is deterministic (measured twice on Lido at 310s and 306s for
# an identical request), so burning the full retry budget on it just wastes ~15 minutes before
# arriving at the same place. These rotate to the next provider immediately.
_CAPACITY_FAILURE_RE = re.compile(
    r"HTTP (?:408|413|502|503|504|520|522|524)\b"
    r"|context[_ ]length|maximum context|too many tokens|payload too large|request too large"
    r"|timed? out",
    re.I,
)


def is_capacity_failure(err: Exception) -> bool:
    return bool(_CAPACITY_FAILURE_RE.search(str(err)))


# Providers that have already proven, in THIS run, that they cannot carry a heavy phase.
# "Maximise the free gateway first" means proving its limit -- not re-proving it 21 times.
# Once a heavy call rotates away from a provider on a capacity failure, later heavy calls skip
# it outright: at ~300s per proof that would otherwise burn ~1.75 hours across a 21-project
# repair run to reach the same conclusion each time. Ordinary phases are unaffected and keep
# using the gateway normally, since the demotion is scoped to heavy calls only.
_demoted_for_heavy = set()
_demote_lock = threading.Lock()


def call_with_retries(messages: list, providers, phase_label: str,
                      max_tokens: int = None, heavy: bool = False) -> str:
    """Send `messages`, retrying transient failures and rotating providers on capacity ones.

    `providers` is a config.Provider or an ordered list of them (see config.load_providers).
    The first is always tried first and given the full retry budget for ordinary errors --
    the maintainer's rule is to exhaust the free gateway before spending elsewhere. A
    capacity-class failure short-circuits that budget and moves straight to the next
    provider, because more attempts against an endpoint that cannot fit the request are
    guaranteed to fail the same way.

    A response that arrives intact but in the wrong FORMAT is not retried here -- that is
    repair.py's job, since it needs a corrective instruction appended rather than the same
    request sent again unchanged.
    """
    if isinstance(providers, config.Provider):
        providers = [providers]

    if heavy and len(providers) > 1:
        with _demote_lock:
            usable = [p for p in providers if p.name not in _demoted_for_heavy]
        if usable and usable != providers:
            skipped = [p.name for p in providers if p not in usable]
            log(f"  ↷ {phase_label}: skipping {', '.join(skipped)} for this heavy phase "
                f"(already proven too small earlier in this run)")
            providers = usable

    last_err = None

    for idx, prov in enumerate(providers):
        is_last_provider = idx == len(providers) - 1
        for attempt in range(1, config.MAX_PHASE_RETRIES + 1):
            try:
                return call_model(messages, prov.base_url, prov.token, prov.model,
                                  max_tokens=max_tokens)
            except Exception as e:  # noqa: BLE001 -- any failure is retryable or rotatable
                last_err = e
                log(f"  ✗ {phase_label} [{prov.name}] attempt "
                    f"{attempt}/{config.MAX_PHASE_RETRIES} failed: {e}")

                if is_capacity_failure(e) and not is_last_provider:
                    nxt = providers[idx + 1]
                    log(f"  ↻ {phase_label}: {prov.name} cannot handle a request this size "
                        f"-- rotating to {nxt.name} ({nxt.model}) instead of retrying")
                    if heavy:
                        with _demote_lock:
                            _demoted_for_heavy.add(prov.name)
                    break  # straight to the next provider

                if attempt < config.MAX_PHASE_RETRIES:
                    backoff = config.RETRY_BACKOFF_SECONDS[
                        min(attempt - 1, len(config.RETRY_BACKOFF_SECONDS) - 1)]
                    log(f"  retrying {phase_label} in {backoff}s...")
                    time.sleep(backoff)
                elif not is_last_provider:
                    nxt = providers[idx + 1]
                    log(f"  ↻ {phase_label}: {prov.name} exhausted its retries "
                        f"-- rotating to {nxt.name} ({nxt.model})")

    raise RuntimeError(f"{phase_label} failed on every provider "
                       f"({', '.join(p.name for p in providers)}): {last_err}")
