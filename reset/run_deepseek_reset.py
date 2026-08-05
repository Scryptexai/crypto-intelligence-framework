#!/usr/bin/env python3
"""
reset/run_deepseek_reset.py — automated Track C (DeepSeek methodology) research pipeline.

Runs the 11 Track C phase prompts (reset/phase_NN_<key>.txt, extracted verbatim from
docs/Protocol/Phased-Research-Prompts.md's "Fixed vs. the original DeepSeek run" section — the
prompt set actually used to research Arbitrum, data_project/Arbitrum/) against an OpenAI-compatible
/v1/chat/completions endpoint, one project at a time (reset/projects.txt), maintaining the full
conversation as running context so each phase sees everything before it — matching Track C's actual
design: "run phases in one sitting, in the same chat, back to back".

Endpoint note (confirmed live, 2026-08-05): despite the ANTHROPIC_* env var names below, the actual
proxy (api.hcnsec.cn, a "New API" gateway) only implements an OpenAI-shaped /v1/chat/completions
route, not /v1/messages -- posting to /v1/messages got the gateway's own frontend HTML back
(HTTP 200, its SPA's catch-all for unmatched paths), reproducible with a bare curl and a trivial
payload, so it was never about request size. See call_deepseek()/extract_text().

Model note (confirmed live, 2026-08-05): this proxy does not necessarily route "DeepSeek-V4-Pro" to
actual DeepSeek -- a real request came back with response.model = "nvidia/nemotron-3-ultra-550b-a55b".
It's a free/aggregating gateway, not a dedicated DeepSeek endpoint. Per the maintainer's own call:
evaluate by output quality against the real Arbitrum dossier, not by which underlying model the
gateway actually used -- if the fields and depth are comparable, the specific model doesn't matter
for this pipeline's purposes.

Safe by default: every run writes to reset/tmp_test/<Project>/NN-<phasekey>.docx, NOT
data_project/, unless --commit is passed. This script also NEVER runs ./run.sh or ./run.sh sync
itself, in either mode -- assembling the dossier and pushing it to the live database are decisions
a human makes after reading the output, not an automatic side effect of an API call finishing.
Review a test run's output quality first, then re-run with --commit once you trust it, then run
./run.sh and ./run.sh sync yourself from the repo root when you're ready.

Each phase's raw response is saved as plain UTF-8 text in a file named NN-<phasekey>.docx — this
is not a real Word document, and doesn't need to be: tools/extract.py's extract_docx() already
falls back to reading a file straight through when it isn't a real OOXML container (this is
exactly how the real Arbitrum data_project files are saved).

Resumable by design: before calling the API for a phase, it checks whether that phase's output
file already exists (in whichever output root is active) and looks like real content (not
re-running work a crashed/interrupted previous run already finished) — the existing text is
loaded back into the running conversation so later phases still get correct context.

Credentials — read from environment only, NEVER hardcoded or logged:
    ANTHROPIC_BASE_URL     e.g. https://api.hcnsec.cn/
    ANTHROPIC_AUTH_TOKEN   bearer token — this is a dev/test credential; rotate it once e2e
                           testing is done, per the maintainer's own instruction. Never print,
                           log, or commit this value.
    ANTHROPIC_MODEL        e.g. DeepSeek-V4-Pro
Optional tuning (sensible defaults if unset):
    RESET_MAX_TOKENS            default 8192
    RESET_REQUEST_TIMEOUT_SECS  default 900 (long prompts / big responses can be slow)
    RESET_PHASE_SLEEP_SECS      default 60   (gap between phases, same project)
    RESET_PROJECT_SLEEP_SECS    default 300  (gap between projects)
    RESET_MAX_RETRIES           default 3    (retries of the SAME phase before giving up on it)

Usage:
    python3 reset/run_deepseek_reset.py --project Aptos --phases-limit 1   # test one phase, one project
    python3 reset/run_deepseek_reset.py --project Aptos                   # test all 11 phases, one project
    python3 reset/run_deepseek_reset.py --dry-run                         # no real API calls at all
    python3 reset/run_deepseek_reset.py --commit                          # the real run, every project in projects.txt
    python3 reset/run_deepseek_reset.py --commit --parallel 4             # 4 projects at once instead of one at a time

--parallel N runs N projects concurrently (each project is its own independent conversation, so
there's no shared state to corrupt) instead of one at a time. The per-phase/per-project sleep
gaps still apply, just per-thread rather than globally serialized -- this multiplies throughput
by N, so raise it gradually and watch for rate-limit errors in reset/failures.log rather than
jumping straight to a large number.
"""
import argparse
import json
import os
import re
import sys
import threading
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RESET_DIR = ROOT / "reset"
DATA_PROJECT_ROOT = ROOT / "data_project"
FAILURES_LOG = RESET_DIR / "failures.log"

PHASES = [
    (1, "foundation"), (2, "entity"), (3, "history"), (4, "technology"),
    (5, "financial"), (6, "token"), (7, "ecosystem"), (8, "market"),
    (9, "behavioral"), (10, "knowledge"), (11, "conflict"),
]

# Phase 11 (Validation & QA) is handled as four smaller, sequential API calls instead of
# appending to the full 10-phase running conversation -- see run_phase_11()'s docstring for the
# full rationale (started as 2 calls, but even the smaller of those two still hit gateway-side
# 504 timeouts -- the bottleneck is generation TIME on a slow backend, not request size, so each
# stage's ASK needed to shrink too, not just its input).
PHASE11_STAGES = [
    ("11a", "phase_11a_audit.txt", [(1, "foundation"), (2, "entity"), (3, "history")]),
    ("11b", "phase_11b_audit.txt", [(4, "technology"), (5, "financial")]),
    ("11c", "phase_11c_audit.txt", [(6, "token"), (7, "ecosystem"), (8, "market")]),
    ("11d", "phase_11d_scoring.txt", [(9, "behavioral"), (10, "knowledge")]),
]

MAX_TOKENS = int(os.environ.get("RESET_MAX_TOKENS", "8192"))
# Phase 11b alone carries almost everything the old single-call Phase 11 produced (the real
# Arbitrum Phase 11 section is ~38.9k chars, ~9.7k tokens estimated -- already over the default
# 8192). Its own constant so phases 1-10 aren't forced to allow bigger (and slower/costlier)
# completions than they need.
PHASE11_MAX_TOKENS = int(os.environ.get("RESET_PHASE11_MAX_TOKENS", "16000"))
REQUEST_TIMEOUT_SECONDS = int(os.environ.get("RESET_REQUEST_TIMEOUT_SECS", "900"))
PHASE_SLEEP_SECONDS = int(os.environ.get("RESET_PHASE_SLEEP_SECS", "60"))
PROJECT_SLEEP_SECONDS = int(os.environ.get("RESET_PROJECT_SLEEP_SECS", "300"))
MAX_PHASE_RETRIES = int(os.environ.get("RESET_MAX_RETRIES", "3"))
RETRY_BACKOFF_SECONDS = [30, 90, 180]
MIN_PHASE_CHARS = 400  # matches tools/ingest.py's own MIN_PHASE_CHARS


_print_lock = threading.Lock()
_failures_lock = threading.Lock()


def log(msg: str) -> None:
    ts = datetime.now(timezone.utc).strftime("%H:%M:%S")
    with _print_lock:
        print(f"[{ts}] {msg}", flush=True)


def log_failure(project: str, num: int, key: str, err: Exception) -> None:
    FAILURES_LOG.parent.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).isoformat()
    with _failures_lock:
        with FAILURES_LOG.open("a", encoding="utf-8") as fh:
            fh.write(f"{ts}\t{project}\tphase {num:02d}-{key}\t{err}\n")


def load_projects(path: Path) -> list:
    lines = path.read_text(encoding="utf-8").splitlines()
    return [ln.strip() for ln in lines if ln.strip() and not ln.strip().startswith("#")]


def load_shared_format_rules() -> str:
    """The doc's "ATURAN FORMAT" block -- citations WAJIB per fact, Evidence Level tags, no
    fabrication, etc. docs/Protocol/Phased-Research-Prompts.md's "Shared rules" section is
    explicit: "Append this block to every phase prompt before sending it." Missing this entirely
    is what produced zero-citation output in an early version of this script (verified live,
    2026-08-03: Aptos test phases had 0 (HIGH)/(MEDIUM)/(LOW) tags vs 24-254 in the real
    data_project/Arbitrum/ phases) -- tools/ingest.py's validate_phase_content() would hard-reject
    that as the exact "empty citations" failure mode the doc's own "Known failure patterns"
    section warns about."""
    return (RESET_DIR / "shared_format_rules.txt").read_text(encoding="utf-8")


def load_phase_prompt(num: int, key: str) -> str:
    p = RESET_DIR / f"phase_{num:02d}_{key}.txt"
    body = p.read_text(encoding="utf-8")
    return body.rstrip() + "\n\n" + load_shared_format_rules().rstrip() + "\n"


def extract_text(body: dict) -> str:
    """Parses the response permissively. Confirmed live, 2026-08-05: this proxy (api.hcnsec.cn, a
    "New API" gateway instance) does NOT implement the Anthropic Messages API shape at /v1/messages
    despite the ANTHROPIC_* env var naming convention -- POSTing there got the gateway's own
    frontend HTML back (its SPA's catch-all route for unmatched paths), reproduced identically via
    a bare curl with a trivial payload, so it was never about request size or retries. The real
    endpoint is OpenAI-compatible /v1/chat/completions (see call_deepseek's url), which returns the
    choices[0].message.content shape below. The Anthropic-shape check stays first only as a no-cost
    fallback in case this ever points at a genuinely Anthropic-compatible endpoint again."""
    # Anthropic Messages API: {"content": [{"type": "text", "text": "..."}], ...}
    content = body.get("content")
    if isinstance(content, list):
        text = "".join(p.get("text", "") for p in content if isinstance(p, dict) and p.get("type") == "text")
        if text.strip():
            return text
    # OpenAI-style fallback: {"choices": [{"message": {"content": "..."}}]}
    choices = body.get("choices")
    if isinstance(choices, list) and choices:
        msg = choices[0].get("message", {}) if isinstance(choices[0], dict) else {}
        text = msg.get("content", "")
        if isinstance(text, str) and text.strip():
            return text
    raise ValueError(f"unrecognized response shape, no text found: {json.dumps(body)[:800]}")


def call_deepseek(messages: list, base_url: str, token: str, model: str, max_tokens: int = None) -> str:
    """POST to {base_url}/v1/chat/completions (OpenAI-compatible -- see extract_text's docstring
    for how this was confirmed against the real endpoint, 2026-08-05). Raises on any failure
    (network, timeout, non-200, unparseable body) -- caller (call_with_retries) handles retry."""
    url = base_url.rstrip("/") + "/v1/chat/completions"
    # Explicit stream: false -- without this, some proxies default a very large completion to
    # SSE streaming server-side regardless of client intent; a streamed "data: {...}\n\n" body fed
    # to json.loads() fails with the same opaque "Expecting value: line 1 column 1 (char 0)" this
    # script hit before the real cause (wrong endpoint path, see above) was found.
    payload = {"model": model, "max_tokens": max_tokens or MAX_TOKENS, "messages": messages, "stream": False}
    data = json.dumps(payload).encode("utf-8")
    # Debug aid, 2026-08-05: a UA-spoofed Python request to this same URL still got the gateway's
    # fallback HTML back while an equivalent curl succeeded -- dumping the EXACT outgoing body lets
    # that same body be replayed via `curl --data @reset/tmp_test/_last_request.json` to isolate
    # whether this is content/size-specific (curl fails too on the real body) or something about
    # how urllib itself sends the request (curl succeeds even with the real body).
    (RESET_DIR / "tmp_test").mkdir(parents=True, exist_ok=True)
    (RESET_DIR / "tmp_test" / "_last_request.json").write_bytes(data)
    req = urllib.request.Request(url, data=data, method="POST")
    req.add_header("Content-Type", "application/json")
    req.add_header("Authorization", f"Bearer {token}")
    req.add_header("Accept", "application/json")
    # urllib's default User-Agent is literally "Python-urllib/3.x" -- a string commonly denylisted
    # by WAFs/anti-bot layers on gateways like this one (curl's default UA is not, which is the
    # one concrete difference between a curl POST to this same URL that got real JSON back, 2026-
    # 08-05, and this script still getting the gateway's fallback HTML after the endpoint-path fix
    # alone). Spoofing curl's UA is the cheapest next thing to rule in/out.
    req.add_header("User-Agent", "curl/8.5.0")
    try:
        with urllib.request.urlopen(req, timeout=REQUEST_TIMEOUT_SECONDS) as resp:
            status = resp.status
            raw = resp.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8", errors="replace")[:800]
        raise RuntimeError(f"HTTP {e.code}: {err_body}") from e
    try:
        body = json.loads(raw)
    except json.JSONDecodeError as e:
        # Bare "Expecting value: line 1 column 1 (char 0)" (json's own message) tells you nothing
        # about what the server actually sent -- a 200 with an empty body, an SSE "data: {...}"
        # stream (this script always sends a non-streaming request, but a third-party proxy can
        # still switch to streaming server-side for large responses without being asked), a
        # truncated/interrupted body, or an HTML error page all produce this exact same message.
        # Surface the real bytes (bounded) so a failure is diagnosable from reset/failures.log
        # instead of needing to be reproduced live.
        snippet = raw[:500] if raw else "(empty body)"
        raise RuntimeError(
            f"HTTP {status} but response body is not valid JSON ({e}); "
            f"body length={len(raw)} chars, first 500 chars: {snippet!r}"
        ) from e
    return extract_text(body)


def call_with_retries(messages: list, base_url: str, token: str, model: str, phase_label: str,
                       max_tokens: int = None) -> str:
    last_err = None
    for attempt in range(1, MAX_PHASE_RETRIES + 1):
        try:
            return call_deepseek(messages, base_url, token, model, max_tokens=max_tokens)
        except Exception as e:  # noqa: BLE001 -- deliberately broad, any failure should trigger retry
            last_err = e
            log(f"  ✗ {phase_label} attempt {attempt}/{MAX_PHASE_RETRIES} failed: {e}")
            if attempt < MAX_PHASE_RETRIES:
                backoff = RETRY_BACKOFF_SECONDS[min(attempt - 1, len(RETRY_BACKOFF_SECONDS) - 1)]
                log(f"  retrying {phase_label} in {backoff}s...")
                time.sleep(backoff)
    raise RuntimeError(f"{phase_label} failed after {MAX_PHASE_RETRIES} attempts: {last_err}")


def existing_phase_ok(path: Path) -> bool:
    return path.exists() and len(path.read_text(encoding="utf-8").strip()) >= MIN_PHASE_CHARS


def _prompt_placeholder(num: int, key: str) -> str:
    """Stand-in for a COMPLETED phase's full prompt text once its real output is already in
    context. The instructions themselves add no new information once the phase they produced is
    sitting right below them (unmodified, in full) -- keeping them around just means re-sending
    the same ~2-8k chars of template/rules text on every later call for no benefit. By phase 11
    this was the majority of the payload: summing reset/phase_*.txt + shared_format_rules.txt
    (which gets appended to every single phase prompt) came to ~58k chars of prompt text alone,
    repeated in full for every one of the 10 prior phases. Shrinking old prompts to this marker
    while leaving every real answer untouched cuts phase 11's total request size roughly in half
    without losing a single fact the model actually produced."""
    return f"[Phase {num:02d}-{key} instructions were sent here; see this phase's full output below.]"


def _inject_phase_dataset(prompt: str, proj_dir: Path, phase_specs: list) -> str:
    """Appends the real saved content of the given (num, key) phases after the prompt's own
    instructional text, under a clearly labeled section. The model only ever sees what's
    physically included in the message it's sent -- the prompt's own "CONTEXT DEPENDENCIES"
    section is a description of what to expect, this is the actual data."""
    parts = [prompt.rstrip(), "\n\n---\n\nISI DATASET (baca dan audit seluruh isi berikut):\n"]
    for num, key in phase_specs:
        text = (proj_dir / f"{num:02d}-{key}.docx").read_text(encoding="utf-8")
        parts.append(f"\n=== {num:02d}-{key}.docx ===\n{text}")
    return "".join(parts)


_MANIFEST_RE = re.compile(r"(?is)(CIF MANIFEST v3\.0.*?```.*?```)")


def _extract_manifest_block(text: str) -> tuple:
    """Pulls the 'CIF MANIFEST v3.0' heading + its fenced code block out of Phase 11b's response
    so it can be moved to the front of the assembled Phase 11 file (matching the real Arbitrum
    dossier's structure: CIF VALIDATION REPORT v3.0 -> CIF MANIFEST v3.0 -> everything else) --
    the prompt asks the model to compute it last but WRITE it first in its own response, so this
    is normally a no-op reordering, not a content change. Falls back to (None, text) unchanged
    if the expected fenced-block shape isn't found, rather than guessing at a malformed split."""
    m = _MANIFEST_RE.search(text)
    if not m:
        return None, text
    manifest = m.group(1).strip()
    rest = (text[: m.start()] + text[m.end():]).strip()
    return manifest, rest


def run_phase_11(name: str, base_url: str, token: str, model: str, proj_dir: Path) -> tuple:
    """Phase 11 (Validation & QA) as four smaller, sequential API calls (PHASE11_STAGES) instead
    of one appended to the full 10-phase running conversation.

    History of this function, in order of what was actually tried and why it kept changing:
      1. Single call appending to the full 10-phase conversation -- failed with an opaque JSON
         parse error (turned out to be an HTML fallback page from a misconfigured base URL, see
         point 3 below, but wasn't understood as that yet at the time).
      2. Split into 2 calls (11a: phases 1-5, 11b: phases 6-10 + 11a's Inventory) with fresh,
         narrowly-scoped context per call instead of the growing conversation -- built to address
         a request-SIZE hypothesis that turned out to be wrong for the failures being chased at
         the time (see point 3), but the "fresh context read from disk, not accumulated chat"
         technique itself was sound and is kept here.
      3. Real root cause of the original failures, found by bisecting with curl: the configured
         ANTHROPIC_BASE_URL env var had gotten corrupted (a stray "export" from a copy-paste
         landed on the end of the URL), so every request hit a nonexistent path and the gateway's
         SPA served its own frontend HTML back (HTTP 200) instead of a clean 404 -- nothing to do
         with request size, headers, or the model at all. Fixed by the user re-exporting cleanly.
      4. With the URL fixed, a NEW and real failure appeared: HTTP 504 (gateway timeout) on stage
         11a specifically, reproducible on every retry. Measured cause: the backend model is slow
         (~2-6 tokens/sec observed) and stage 11a's ASK (Dataset Integrity + a complete Inventory
         of every entity/event/tech/financial fact across 5 phases, ex-Cross-phase-Consistency and
         Candidate Conflicts) is a much bigger completion than a single ordinary phase -- and even
         ordinary phases 2/3 were separately observed taking 4+ minutes each. The bottleneck is
         GENERATION TIME on a slow shared backend, not input size -- so the fix is to shrink each
         stage's OUTPUT ask, not (only) its input.

    Current design (4 stages, PHASE11_STAGES): each stage's ask is roughly one ordinary phase's
    worth of output, close to the sizes phases 2/3 already succeed at:
      - 11a: phases 1-3 -> Dataset Integrity (1-3) + Inventory (Entity + Event).
      - 11b: phases 4-5 + 11a's findings -> Dataset Integrity (4-5) + Inventory (Tech +
        Financial) + Cross-phase Consistency (all of 1-5) + Candidate Conflicts (1-5).
      - 11c: phases 6-8 + 11b's findings -> Dataset Integrity (6-8) + Inventory (Token/Ecosystem/
        Market) + Consistency continuation + Candidate Conflicts (6-8).
      - 11d: phases 9-10 + 11c's findings -> Coverage Report, Data Lineage, Dependency Graph, the
        final merged Conflict Register, Evidence Audit, Confidence Assessment, Knowledge
        Stability, Missing Knowledge, CIF Score Calculation, Final Validation Summary, Open
        Threads, and the CIF Manifest.

    Each stage gets a freshly built, narrowly-scoped context read directly from the phase files
    already on disk for ITS OWN phase range, plus only the immediately-preceding stage's response
    (not that stage's prompt, and not any earlier stage's raw response -- each stage's prompt asks
    it to merge forward everything it received, so by the last stage the single carried-forward
    response already contains everything accumulated). No fact from any phase is dropped: every
    stage examines its assigned phases' full raw text; a later stage's link back to earlier phases
    is via the accumulated Inventory/findings text, not by re-sending raw phase text already
    covered by a prior stage.

    Returns (combined_text_or_None, error_or_None).
    """
    # Every stage's own response is kept and concatenated at the end -- each stage only asks for
    # NEW sections (Dataset Integrity/Inventory for its own phase range, etc.), it is not asked to
    # reprint everything accumulated so far, so the assembled document needs all of them, not just
    # the last one (an earlier version of this function kept only the final stage's response,
    # which silently dropped every raw Inventory listing from stages 11a-11c -- exactly the kind
    # of value loss this whole design is meant to avoid).
    # Per-stage resumability: each stage's raw response is saved to its own .tmp file the moment
    # it succeeds. If a later stage then fails (all retries exhausted) and this function gets
    # called again on a subsequent run, already-completed stages are loaded back from disk instead
    # of re-calling the API for them -- otherwise every retry would burn a fresh call (and the
    # matching PHASE_SLEEP_SECONDS wait) re-doing stages that already succeeded, on top of whatever
    # made the failing stage slow/flaky in the first place.
    def stage_tmp_path(key: str) -> Path:
        return proj_dir / f"11-stage-{key}.tmp"

    all_responses = []
    prior_response = None
    prior_stage_label = None
    for stage_key, prompt_file, phase_specs in PHASE11_STAGES:
        tmp_path = stage_tmp_path(stage_key)
        if tmp_path.exists() and len(tmp_path.read_text(encoding="utf-8").strip()) >= MIN_PHASE_CHARS:
            response = tmp_path.read_text(encoding="utf-8")
            log(f"  [{name}] phase {stage_key}: already done, resuming from {tmp_path.name} (no API call)")
        else:
            prompt = (RESET_DIR / prompt_file).read_text(encoding="utf-8").rstrip() \
                + "\n\n" + load_shared_format_rules().rstrip() + "\n"
            prompt = _inject_phase_dataset(prompt, proj_dir, phase_specs)

            if prior_response is None:
                messages = [{"role": "user", "content": prompt}]
            else:
                messages = [
                    {"role": "user", "content": f"[Phase {prior_stage_label} instructions and its "
                                                 f"phase dataset were sent here; see that stage's "
                                                 f"full findings below.]"},
                    {"role": "assistant", "content": prior_response},
                    {"role": "user", "content": prompt},
                ]
            try:
                response = call_with_retries(messages, base_url, token, model, f"{name} phase {stage_key}",
                                              max_tokens=PHASE11_MAX_TOKENS)
            except Exception as e:  # noqa: BLE001
                return None, e
            tmp_path.write_text(response, encoding="utf-8")

        all_responses.append(response)
        prior_response = response
        prior_stage_label = stage_key
        if stage_key != PHASE11_STAGES[-1][0]:
            time.sleep(PHASE_SLEEP_SECONDS)

    # The Manifest only exists in the LAST stage's response (11d is the only stage asked to
    # produce it) -- pull it out and move it to the front, matching the real Arbitrum dossier's
    # structure (CIF VALIDATION REPORT v3.0 -> CIF MANIFEST v3.0 -> everything else).
    manifest, last_rest = _extract_manifest_block(all_responses[-1])
    body_sections = [r.strip() for r in all_responses[:-1]] + [last_rest]
    if manifest:
        combined = f"CIF VALIDATION REPORT v3.0\n\n---\n\n{manifest}\n\n---\n\n" \
                   + "\n\n---\n\n".join(body_sections)
    else:
        combined = "\n\n---\n\n".join(r.strip() for r in all_responses)
    if not re.match(r"(?im)^PROJECT:\s*" + re.escape(name), combined.strip()):
        combined = f"PROJECT: {name}\n\n{combined}"

    # Success -- the stage .tmp files are now folded into the real 11-conflict.docx output and
    # would otherwise sit around as stale/confusing leftovers if this project's Phase 11 were ever
    # re-run (e.g. after a --commit copy or a manual quality re-check).
    for stage_key, _, _ in PHASE11_STAGES:
        stage_tmp_path(stage_key).unlink(missing_ok=True)

    return combined, None


def run_project(name: str, base_url: str, token: str, model: str, dry_run: bool, phases_limit: int,
                output_root: Path) -> bool:
    """Returns True if every requested phase completed (real or resumed-from-disk), False if a
    phase failed permanently (all retries exhausted) -- in which case later phases for this
    project are skipped (they need this one's output as context) but the run continues to the
    NEXT project rather than aborting everything."""
    def plog(msg: str) -> None:
        log(f"[{name}] {msg}")

    plog("=== starting ===")
    proj_dir = output_root / name
    proj_dir.mkdir(parents=True, exist_ok=True)
    messages: list = []  # running chat history -- Track C's "one continuous chat" methodology

    phases = PHASES[:phases_limit] if phases_limit else PHASES

    for idx, (num, key) in enumerate(phases):
        out_path = proj_dir / f"{num:02d}-{key}.docx"

        if existing_phase_ok(out_path):
            plog(f"phase {num:02d}-{key}: already done, resuming (loading into context, no API call)")
            if num == 11:
                # Phase 11 is self-contained (built from files 01-10 already on disk, not the
                # running `messages` conversation) and nothing later depends on it -- there's no
                # phase 12 that would need it appended to `messages`, unlike phases 1-10.
                continue
            existing_text = out_path.read_text(encoding="utf-8")
            # Already-completed phase: keep the full real output, shrink the prompt that produced
            # it (see _prompt_placeholder's docstring) -- applies whether we're resuming a phase
            # finished in a previous run or one just finished earlier in this same loop.
            messages.append({"role": "user", "content": _prompt_placeholder(num, key)})
            messages.append({"role": "assistant", "content": existing_text})
            continue

        if num == 11:
            plog(f"phase 11-conflict: sending as {len(PHASE11_STAGES)} smaller sequential stages "
                 f"({', '.join(s[0] for s in PHASE11_STAGES)}) -- see run_phase_11()'s docstring for why...")
            if dry_run:
                fake = f"PROJECT: {name}\n\n[DRY RUN -- Phase 11 placeholder, {len(PHASE11_STAGES)}-stage split]\n"
                out_path.write_text(fake, encoding="utf-8")
                plog(f"phase 11-conflict: [dry-run] wrote placeholder -> {out_path}")
                continue
            text, err = run_phase_11(name, base_url, token, model, proj_dir)
            if err is not None:
                plog(f"✗✗ {name} phase 11-conflict permanently failed, giving up on this project "
                     f"for now: {err}")
                log_failure(name, num, key, err)
                plog("(re-run this script later and it will resume from here)")
                return False
            out_path.write_text(text, encoding="utf-8")
            plog(f"phase 11-conflict: done ({len(text)} chars, 2-call split) -> {out_path}")
            continue

        prompt_template = load_phase_prompt(num, key)
        prompt = prompt_template.replace("<NAMA PROJECT>", name) if num == 1 else prompt_template

        plog(f"phase {num:02d}-{key}: sending...")
        messages.append({"role": "user", "content": prompt})

        if dry_run:
            fake = f"PROJECT: {name}\n\n[DRY RUN -- no real API call made for phase {num:02d}-{key}]\n"
            out_path.write_text(fake, encoding="utf-8")
            messages.append({"role": "assistant", "content": fake})
            messages[-2]["content"] = _prompt_placeholder(num, key)
            plog(f"phase {num:02d}-{key}: [dry-run] wrote placeholder -> {out_path}")
        else:
            phase_label = f"{name} phase {num:02d}-{key}"
            try:
                text = call_with_retries(messages, base_url, token, model, phase_label)
            except Exception as e:  # noqa: BLE001
                plog(f"✗✗ {phase_label} permanently failed, giving up on this project for now: {e}")
                log_failure(name, num, key, e)
                plog(f"(later phases for {name} need this one's output, so skipping the rest of "
                     f"{name} -- re-run this script later and it will resume from here)")
                return False
            if not re.match(r"(?im)^PROJECT:\s*" + re.escape(name), text.strip()):
                # Always prepend PROJECT: <Name> -- tools/ingest.py's validate_phase_content()
                # requires it, and the real Arbitrum files have it on every phase regardless of
                # what the prompt asked the model to include.
                text = f"PROJECT: {name}\n\n{text}"
            out_path.write_text(text, encoding="utf-8")
            messages.append({"role": "assistant", "content": text})
            # This phase is now complete -- shrink its just-sent full prompt (still the full
            # instructions, needed for the call that just happened) down to the short marker so
            # it doesn't get re-sent in full on every subsequent phase's request. The real output
            # right above it is untouched.
            messages[-2]["content"] = _prompt_placeholder(num, key)
            plog(f"phase {num:02d}-{key}: done ({len(text)} chars) -> {out_path}")

        if idx < len(phases) - 1:
            plog(f"sleeping {PHASE_SLEEP_SECONDS}s before next phase...")
            time.sleep(PHASE_SLEEP_SECONDS)

    # Deliberately NO automatic ./run.sh / ./run.sh sync call, in either mode -- pushing output
    # (test or real) into the assembled dossier or the live database is a decision a human makes
    # after reading it, never an automatic side effect of an API call finishing. See reset/README.md.
    if output_root == DATA_PROJECT_ROOT:
        plog(f"=== all requested phases done, written to data_project/{name}/. "
             f"Review the content, then run './run.sh' (assemble) and './run.sh sync' (push to "
             f"the database) yourself from the repo root when you're satisfied with it. ===")
    else:
        plog(f"=== all requested phases done -- TEST run, written to "
             f"{output_root}/{name}/ (not the real dataset). Review it, then re-run with "
             f"--commit once you trust the quality. ===")
    return True


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--project", help="process only this one project (ad hoc), ignoring projects.txt")
    ap.add_argument("--projects-limit", type=int, default=0,
                     help="process only the first N projects from projects.txt (0 = all)")
    ap.add_argument("--phases-limit", type=int, default=0,
                     help="process only the first N phases per project (0 = all 11) -- for smoke testing")
    ap.add_argument("--dry-run", action="store_true",
                     help="no real API calls -- exercises file/loop logic only")
    ap.add_argument("--commit", action="store_true",
                     help="write real output into data_project/ (the actual dataset), and stay "
                          "there across the whole run. Off by default -- every run without this "
                          "flag stays confined to reset/tmp_test/, never touches data_project/, "
                          "and never runs ./run.sh or ./run.sh sync. Only pass this once you've "
                          "reviewed a test run's output quality and are ready to commit it.")
    ap.add_argument("--output-root",
                     help="override where <project>/NN-<phasekey>.docx files get written, instead "
                          "of the --commit-based default (reset/tmp_test/, or data_project/ if "
                          "--commit is passed). Rarely needed directly.")
    ap.add_argument("--parallel", type=int, default=1,
                     help="process this many projects concurrently instead of one at a time "
                          "(default 1 = sequential, the original behavior). Each project is an "
                          "independent conversation/thread, so there's no shared state between "
                          "them -- raise gradually and watch reset/failures.log for rate-limit "
                          "errors rather than jumping straight to a large number.")
    args = ap.parse_args()
    if args.output_root:
        output_root = Path(args.output_root).resolve()
    elif args.commit:
        output_root = DATA_PROJECT_ROOT
    else:
        output_root = RESET_DIR / "tmp_test"

    base_url = os.environ.get("ANTHROPIC_BASE_URL")
    token = os.environ.get("ANTHROPIC_AUTH_TOKEN")
    model = os.environ.get("ANTHROPIC_MODEL")
    if not args.dry_run and not (base_url and token and model):
        sys.exit("ANTHROPIC_BASE_URL, ANTHROPIC_AUTH_TOKEN, and ANTHROPIC_MODEL must all be set in "
                  "the environment (never hardcode these in a file). Use --dry-run to test the "
                  "pipeline's control flow without an API key.")

    if args.project:
        projects = [args.project]
    else:
        projects = load_projects(RESET_DIR / "projects.txt")
        if args.projects_limit:
            projects = projects[: args.projects_limit]

    mode = "COMMIT (writing to data_project/, the real dataset)" if output_root == DATA_PROJECT_ROOT \
        else f"TEST (writing to {output_root}, not the real dataset -- pass --commit for a real run)"
    log(f"Starting reset pipeline for {len(projects)} project(s): {', '.join(projects)} -- mode: {mode}"
        + (f" -- parallel={args.parallel}" if args.parallel > 1 else ""))

    if args.parallel > 1:
        with ThreadPoolExecutor(max_workers=args.parallel) as pool:
            futures = {}
            for i, name in enumerate(projects):
                # Small stagger so N threads don't all hit the API in the same instant.
                if i:
                    time.sleep(5)
                futures[pool.submit(run_project, name, base_url, token, model, args.dry_run,
                                     args.phases_limit, output_root)] = name
            for fut in as_completed(futures):
                name = futures[fut]
                try:
                    fut.result()
                except Exception as e:  # noqa: BLE001 -- a thread crashing shouldn't kill the others
                    log(f"[{name}] ✗✗ unexpected exception, this project's thread crashed: {e}")
    else:
        for i, name in enumerate(projects):
            run_project(name, base_url, token, model, args.dry_run, args.phases_limit, output_root)
            if i < len(projects) - 1:
                log(f"sleeping {PROJECT_SLEEP_SECONDS}s before next project...")
                time.sleep(PROJECT_SLEEP_SECONDS)

    log("All projects processed. Check reset/failures.log for anything that needs a manual re-run.")


if __name__ == "__main__":
    main()
