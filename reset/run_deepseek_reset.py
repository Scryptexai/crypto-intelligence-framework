#!/usr/bin/env python3
"""
reset/run_deepseek_reset.py — automated Track C (DeepSeek methodology) research pipeline.

Runs the 11 Track C phase prompts (reset/phase_NN_<key>.txt, extracted verbatim from
docs/Protocol/Phased-Research-Prompts.md's "Fixed vs. the original DeepSeek run" section — the
prompt set actually used to research Arbitrum, data_project/Arbitrum/) against an Anthropic
Messages-API-compatible endpoint, one project at a time (reset/projects.txt), maintaining the
full conversation as running context so each phase sees everything before it — matching Track C's
actual design: "run phases in one sitting, in the same chat, back to back" (DeepSeek's 1M-token
window is why Track A/B's Context Pack discipline doesn't apply here).

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
"""
import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
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

MAX_TOKENS = int(os.environ.get("RESET_MAX_TOKENS", "8192"))
REQUEST_TIMEOUT_SECONDS = int(os.environ.get("RESET_REQUEST_TIMEOUT_SECS", "900"))
PHASE_SLEEP_SECONDS = int(os.environ.get("RESET_PHASE_SLEEP_SECS", "60"))
PROJECT_SLEEP_SECONDS = int(os.environ.get("RESET_PROJECT_SLEEP_SECS", "300"))
MAX_PHASE_RETRIES = int(os.environ.get("RESET_MAX_RETRIES", "3"))
RETRY_BACKOFF_SECONDS = [30, 90, 180]
MIN_PHASE_CHARS = 400  # matches tools/ingest.py's own MIN_PHASE_CHARS


def log(msg: str) -> None:
    ts = datetime.now(timezone.utc).strftime("%H:%M:%S")
    print(f"[{ts}] {msg}", flush=True)


def log_failure(project: str, num: int, key: str, err: Exception) -> None:
    FAILURES_LOG.parent.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).isoformat()
    with FAILURES_LOG.open("a", encoding="utf-8") as fh:
        fh.write(f"{ts}\t{project}\tphase {num:02d}-{key}\t{err}\n")


def load_projects(path: Path) -> list:
    lines = path.read_text(encoding="utf-8").splitlines()
    return [ln.strip() for ln in lines if ln.strip() and not ln.strip().startswith("#")]


def load_phase_prompt(num: int, key: str) -> str:
    p = RESET_DIR / f"phase_{num:02d}_{key}.txt"
    return p.read_text(encoding="utf-8")


def extract_text(body: dict) -> str:
    """Parses the response permissively -- this proxy claims Anthropic-Messages-API shape via its
    ANTHROPIC_* env var naming convention, but is a third-party endpoint, not Anthropic itself, so
    this tries the documented Anthropic shape first and falls back to an OpenAI-style
    choices[0].message.content shape in case the proxy actually speaks that underneath."""
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


def call_deepseek(messages: list, base_url: str, token: str, model: str) -> str:
    """POST to {base_url}/v1/messages. Raises on any failure (network, timeout, non-200,
    unparseable body) -- caller (call_with_retries) handles retry."""
    url = base_url.rstrip("/") + "/v1/messages"
    payload = {"model": model, "max_tokens": MAX_TOKENS, "messages": messages}
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, method="POST")
    req.add_header("Content-Type", "application/json")
    req.add_header("Authorization", f"Bearer {token}")
    req.add_header("anthropic-version", "2023-06-01")
    try:
        with urllib.request.urlopen(req, timeout=REQUEST_TIMEOUT_SECONDS) as resp:
            raw = resp.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8", errors="replace")[:800]
        raise RuntimeError(f"HTTP {e.code}: {err_body}") from e
    body = json.loads(raw)
    return extract_text(body)


def call_with_retries(messages: list, base_url: str, token: str, model: str, phase_label: str) -> str:
    last_err = None
    for attempt in range(1, MAX_PHASE_RETRIES + 1):
        try:
            return call_deepseek(messages, base_url, token, model)
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


def run_project(name: str, base_url: str, token: str, model: str, dry_run: bool, phases_limit: int,
                output_root: Path) -> bool:
    """Returns True if every requested phase completed (real or resumed-from-disk), False if a
    phase failed permanently (all retries exhausted) -- in which case later phases for this
    project are skipped (they need this one's output as context) but the run continues to the
    NEXT project rather than aborting everything."""
    log(f"=== Project: {name} ===")
    proj_dir = output_root / name
    proj_dir.mkdir(parents=True, exist_ok=True)
    messages: list = []  # running chat history -- Track C's "one continuous chat" methodology

    phases = PHASES[:phases_limit] if phases_limit else PHASES

    for idx, (num, key) in enumerate(phases):
        out_path = proj_dir / f"{num:02d}-{key}.docx"
        prompt_template = load_phase_prompt(num, key)
        prompt = prompt_template.replace("<NAMA PROJECT>", name) if num == 1 else prompt_template

        if existing_phase_ok(out_path):
            log(f"  phase {num:02d}-{key}: already done, resuming (loading into context, no API call)")
            existing_text = out_path.read_text(encoding="utf-8")
            messages.append({"role": "user", "content": prompt})
            messages.append({"role": "assistant", "content": existing_text})
            continue

        log(f"  phase {num:02d}-{key}: sending...")
        messages.append({"role": "user", "content": prompt})

        if dry_run:
            fake = f"PROJECT: {name}\n\n[DRY RUN -- no real API call made for phase {num:02d}-{key}]\n"
            out_path.write_text(fake, encoding="utf-8")
            messages.append({"role": "assistant", "content": fake})
            log(f"  phase {num:02d}-{key}: [dry-run] wrote placeholder -> {out_path}")
        else:
            phase_label = f"{name} phase {num:02d}-{key}"
            try:
                text = call_with_retries(messages, base_url, token, model, phase_label)
            except Exception as e:  # noqa: BLE001
                log(f"  ✗✗ {phase_label} permanently failed, giving up on this project "
                    f"for now: {e}")
                log_failure(name, num, key, e)
                log(f"  (later phases for {name} need this one's output, so skipping the rest of "
                    f"{name} -- re-run this script later and it will resume from here)")
                return False
            if not re.match(r"(?im)^PROJECT:\s*" + re.escape(name), text.strip()):
                # Always prepend PROJECT: <Name> -- tools/ingest.py's validate_phase_content()
                # requires it, and the real Arbitrum files have it on every phase regardless of
                # what the prompt asked the model to include.
                text = f"PROJECT: {name}\n\n{text}"
            out_path.write_text(text, encoding="utf-8")
            messages.append({"role": "assistant", "content": text})
            log(f"  phase {num:02d}-{key}: done ({len(text)} chars) -> {out_path}")

        if idx < len(phases) - 1:
            log(f"  sleeping {PHASE_SLEEP_SECONDS}s before next phase...")
            time.sleep(PHASE_SLEEP_SECONDS)

    # Deliberately NO automatic ./run.sh / ./run.sh sync call, in either mode -- pushing output
    # (test or real) into the assembled dossier or the live database is a decision a human makes
    # after reading it, never an automatic side effect of an API call finishing. See reset/README.md.
    if output_root == DATA_PROJECT_ROOT:
        log(f"=== {name}: all requested phases done, written to data_project/{name}/. "
            f"Review the content, then run './run.sh' (assemble) and './run.sh sync' (push to "
            f"the database) yourself from the repo root when you're satisfied with it. ===")
    else:
        log(f"=== {name}: all requested phases done -- TEST run, written to "
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
    log(f"Starting reset pipeline for {len(projects)} project(s): {', '.join(projects)} -- mode: {mode}")
    for i, name in enumerate(projects):
        run_project(name, base_url, token, model, args.dry_run, args.phases_limit, output_root)
        if i < len(projects) - 1:
            log(f"sleeping {PROJECT_SLEEP_SECONDS}s before next project...")
            time.sleep(PROJECT_SLEEP_SECONDS)

    log("All projects processed. Check reset/failures.log for anything that needs a manual re-run.")


if __name__ == "__main__":
    main()
