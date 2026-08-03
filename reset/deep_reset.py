#!/usr/bin/env python3
"""
deep_reset.py — CIF Deep-Reset orchestrator.

For each project in reset/projects.txt, run the 11 research phases SEQUENTIALLY
through the DeepSeek model and write each phase's raw answer to
data_project/<Project>/NN-<key>.docx (the ingest.py naming contract).

Rules implemented (maintainer spec):
  - Phase 1 (Foundation): the model searches for the project's facts + a concise
    description; project name is injected here (and only here — the prompts follow
    the "state name once" rule).
  - Phase N>1: the phase-N prompt is sent together with the OUTPUT OF ALL PRIOR
    PHASES as context (read back from disk, so a resumed run still has context).
  - 60s pause between phases, 300s (5 min) pause between projects.
  - Loops through every project until all data is produced.
  - Resumable: completed phases are recorded in reset/state/progress.json and
    skipped on re-run (unless --overwrite). Filled projects skipped by default.

After the loop (unless --no-pipeline) it runs `./run.sh build` then `./run.sh sync`
so the freshly-written dossiers are ingested + pushed to Supabase.

Usage:
  python3 reset/deep_reset.py                 # full run (all projects, real delays)
  python3 reset/deep_reset.py --only Aptos    # single project
  python3 reset/deep_reset.py --limit 3       # first 3 eligible projects
  python3 reset/deep_reset.py --no-delay      # skip pauses (testing)
  python3 reset/deep_reset.py --dry-run       # print plan, no API calls, no writes
  python3 reset/deep_reset.py --overwrite     # regenerate phases even if present
  python3 reset/deep_reset.py --no-pipeline   # skip run.sh build/sync afterwards
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import config as C
from deep_client import from_env, DeepError
import normalize

def args_context_budget() -> int:
    import os
    return int(os.environ.get("RESET_MAX_CONTEXT_CHARS", "220000"))


STATE_FILE = C.STATE_DIR / "progress.json"
LOG_FILE = C.STATE_DIR / "reset.log"

SYSTEM_PROMPT = (
    "You are a meticulous crypto-intelligence research analyst working within the "
    "Crypto Intelligence Framework (CIF). Follow the phase template EXACTLY.\n"
    "OUTPUT FORMAT RULES (critical for downstream parsing):\n"
    "- PLAIN TEXT ONLY. Do NOT use Markdown: no '#'/'##'/'###' headers, no '**bold**', "
    "no backticks, no '|' tables. Write section titles as bare lines exactly as the "
    "template shows them (e.g. a line 'Core Insights', not '## Core Insights').\n"
    "- Use the EXACT item labels the template specifies (e.g. 'Insight 1:', 'Principle 1:', "
    "'Factor 1:', 'Entity:', 'Event ID:') — do NOT invent your own labels like 'Knowledge 1:'.\n"
    "- Cite every non-trivial fact with an evidence tag (HIGH/MEDIUM/LOW) AND a real source URL.\n"
    "- For synthesis phases (Knowledge/Behavioral/Validation) that reference earlier phases, "
    "write internal citations in the bracket form 【Phase N — Section】 or 【History — EV-0NN】 "
    "(NOT prose like 'Phase 1 says…'); include at least three per report.\n"
    "- Never fabricate: write 'tidak diketahui' when a fact cannot be verified.\n"
    "- Output ONLY the report content in the requested structure — no preamble, no meta commentary."
)

PROJECT_HEADER_RE = re.compile(r"(?im)^\s*PROJECT:\s*(.+)$")
DATASET_HEADER_RE = re.compile(r"(?im)^\s*[A-Z][A-Z0-9 &/()\-]+\s+—\s+.+$")


def log(msg: str) -> None:
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{ts}] {msg}"
    print(line, flush=True)
    try:
        C.STATE_DIR.mkdir(parents=True, exist_ok=True)
        with open(LOG_FILE, "a", encoding="utf-8") as fh:
            fh.write(line + "\n")
    except OSError:
        pass


def load_state() -> dict:
    if STATE_FILE.exists():
        try:
            return json.loads(STATE_FILE.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return {}
    return {}


def save_state(state: dict) -> None:
    C.STATE_DIR.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps(state, indent=2), encoding="utf-8")


def phase_done(project: str, key: str, overwrite: bool, out_base=None) -> bool:
    """A phase is already done if its file exists non-empty (unless --overwrite)."""
    if overwrite:
        return False
    p = C.phase_path(project, key, out_base)
    return p.exists() and p.stat().st_size >= C.MIN_PHASE_CHARS


def build_context(project: str, upto_index: int, budget: int, out_base=None) -> str:
    """Concatenate prior phase outputs (from disk) as context for phase N. Keeps the
    MOST RECENT phases first and stops once the char budget is reached, so a very long
    dossier can't blow past the model/proxy context limit on an unattended VPS run."""
    chunks = []
    used = 0
    for prev_key in reversed(C.PHASE_ORDER[:upto_index]):
        p = C.phase_path(project, prev_key, out_base)
        if p.exists() and p.stat().st_size > 0:
            title = prev_key.split("-", 1)[1].upper()
            block = f"===== KONTEKS: HASIL FASE {prev_key} ({title}) =====\n{p.read_text(encoding='utf-8').strip()}"
            if budget and used + len(block) > budget and chunks:
                break
            chunks.append(block)
            used += len(block)
    return "\n\n".join(reversed(chunks))


def build_prompt(project: str, index: int, key: str, out_base=None) -> str:
    """Assemble the full user message for phase `index` (0-based)."""
    phase_prompt = C.load_phase_prompt(key)

    if index == 0:
        # Phase 1: inject the project name into the placeholders.
        return (
            phase_prompt
            .replace("<NAMA PROJECT>", project)
            .replace("<Nama>", project)
            .replace("<NAMA_PROJECT>", project)
        )

    # Phase >1: prepend project identity + all prior phase outputs as context.
    context = build_context(project, index, args_context_budget(), out_base)
    preamble = (
        f"PROYEK YANG SEDANG DIRISET: {project}\n\n"
        f"Di bawah ini adalah hasil fase-fase sebelumnya untuk proyek yang SAMA. "
        f"Gunakan sebagai konteks wajib (jangan mengulang, lanjutkan secara konsisten). "
        f"Mulai output dengan header yang sesuai format fase ini "
        f"(mis. 'PROJECT: {project}' atau '<JUDUL FASE> — {project.upper()}').\n\n"
        f"{context}\n\n"
        f"===== TUGAS FASE SAAT INI =====\n"
    )
    return preamble + phase_prompt


def ensure_header(project: str, text: str) -> str:
    """ingest.validate_phase_content binds a file to its project via a 'PROJECT: <name>'
    line (preferred) or a '<TITLE> — <NAME>' dataset header. Model output often starts
    with a phase-title line like 'PHASE 10 — KNOWLEDGE EXTRACTION', which the dataset-header
    rule would misread as project 'KNOWLEDGE EXTRACTION'. To be unambiguous we require a
    real 'PROJECT: <folder>' line and prepend one when the correct project isn't already
    declared at the top."""
    m = PROJECT_HEADER_RE.search(text[:200])
    if m and re.sub(r"[^a-z0-9]", "", m.group(1).lower()) == re.sub(r"[^a-z0-9]", "", project.lower()):
        return text
    return f"PROJECT: {project}\n\n{text}"


def write_phase(project: str, key: str, text: str, out_base=None) -> Path:
    d = C.project_dir(project, out_base)
    d.mkdir(parents=True, exist_ok=True)
    # Normalize model output to the plain-text shape the CIF extractors expect
    # (strip Markdown, realign item labels) — some proxy backends answer in Markdown.
    text = normalize.normalize(text)
    p = d / f"{key}.docx"
    p.write_text(text, encoding="utf-8")
    return p


def sleep_with_log(seconds: int, why: str, no_delay: bool) -> None:
    if no_delay or seconds <= 0:
        return
    log(f"⏳ waiting {seconds}s ({why})")
    time.sleep(seconds)


def process_phase(client, project: str, index: int, key: str, args) -> bool:
    """Generate one phase. Returns True on success."""
    if phase_done(project, key, args.overwrite, args._out_base):
        log(f"  ↳ {key}: already present, skip")
        return True

    prompt = build_prompt(project, index, key, args._out_base)
    if args.dry_run:
        log(f"  ↳ {key}: DRY-RUN (prompt {len(prompt)} chars) — no API call")
        return True

    for attempt in (1, 2):
        try:
            log(f"  ↳ {key}: generating (attempt {attempt}, prompt {len(prompt)} chars)…")
            answer = client.complete(prompt, system=SYSTEM_PROMPT)
        except DeepError as e:
            log(f"  ✖ {key}: API error: {e}")
            answer = ""
        answer = (answer or "").strip()
        if len(answer) >= C.MIN_PHASE_CHARS:
            answer = ensure_header(project, answer)
            path = write_phase(project, key, answer, args._out_base)
            log(f"  ✓ {key}: wrote {len(answer)} chars -> {path.relative_to(C.ROOT)}")
            return True
        log(f"  ⚠ {key}: answer too short ({len(answer)} chars), retrying")
        time.sleep(10)
    log(f"  ✖ {key}: FAILED after 2 attempts")
    return False


def process_project(client, project: str, args, state: dict) -> bool:
    if not args.staging and C.SKIP_FILLED and not args.overwrite and C.is_project_filled(project):
        log(f"▶ {project}: already filled, skip")
        return True

    log(f"▶ {project}: starting {len(C.PHASE_ORDER)}-phase reset")
    state.setdefault(project, {})
    ok_all = True
    for i, key in enumerate(C.PHASE_ORDER):
        if args.max_phases and i >= args.max_phases:
            break
        ok = process_phase(client, project, i, key, args)
        state[project][key] = {
            "status": "done" if ok else "failed",
            "at": datetime.now(timezone.utc).isoformat(),
        }
        save_state(state)
        ok_all = ok_all and ok
        if i < len(C.PHASE_ORDER) - 1:
            sleep_with_log(args.phase_delay, "between phases", args.no_delay)
    log(f"◼ {project}: done (success={ok_all})")
    return ok_all


def run_pipeline(args) -> None:
    if args.no_pipeline or args.dry_run:
        log("pipeline: skipped")
        return
    log("pipeline: ./run.sh build")
    subprocess.run(["bash", "run.sh", "build"], cwd=str(C.ROOT), check=False)
    if C.RUN_SYNC:
        log("pipeline: ./run.sh sync")
        subprocess.run(["bash", "run.sh", "sync"], cwd=str(C.ROOT), check=False)


def main() -> int:
    ap = argparse.ArgumentParser(description="CIF Deep-Reset orchestrator")
    ap.add_argument("--only", help="process only this project (exact name)")
    ap.add_argument("--shard", help="parallel worker split, e.g. 0/4 (this worker = index 0 of 4)")
    ap.add_argument("--limit", type=int, default=0, help="process at most N eligible projects")
    ap.add_argument("--overwrite", action="store_true", help="regenerate phases even if present")
    ap.add_argument("--no-delay", action="store_true", help="skip pauses (testing)")
    ap.add_argument("--dry-run", action="store_true", help="print plan, no API calls / writes")
    ap.add_argument("--no-pipeline", action="store_true", help="skip run.sh build/sync afterwards")
    ap.add_argument("--staging", action="store_true", help="write to reset/temp/<Project> (NOT data_project); never runs pipeline")
    ap.add_argument("--max-phases", type=int, default=0, help="only run the first N phases per project (testing)")
    ap.add_argument("--phase-delay", type=int, default=C.PHASE_DELAY_SEC)
    ap.add_argument("--project-delay", type=int, default=C.PROJECT_DELAY_SEC)
    args = ap.parse_args()

    args._out_base = C.STAGING_DIR if args.staging else None
    if args.staging:
        args.no_pipeline = True  # staging never touches ingest/sync
        C.STAGING_DIR.mkdir(parents=True, exist_ok=True)

    projects = C.load_projects()
    if args.only:
        projects = [p for p in projects if p == args.only]
        if not projects:
            log(f"✖ project '{args.only}' not found in {C.PROJECTS_FILE.name}")
            return 2

    if args.shard:
        try:
            idx, total = (int(x) for x in args.shard.split("/"))
        except ValueError:
            log(f"✖ bad --shard '{args.shard}', expected i/n e.g. 0/4")
            return 2
        projects = [p for i, p in enumerate(projects) if i % total == idx]
        log(f"shard {idx}/{total}: {len(projects)} project(s) assigned to this worker")

    client = None if args.dry_run else from_env()
    state = load_state()

    log(f"=== CIF Deep-Reset: {len(projects)} project(s) in list ===")
    log(f"    phase_delay={args.phase_delay}s project_delay={args.project_delay}s "
        f"skip_filled={C.SKIP_FILLED} overwrite={args.overwrite} dry_run={args.dry_run}")

    processed = 0
    for project in projects:
        if args.limit and processed >= args.limit:
            log(f"reached --limit {args.limit}, stopping")
            break
        if not args.staging and C.SKIP_FILLED and not args.overwrite and C.is_project_filled(project):
            log(f"▶ {project}: already filled, skip")
            continue
        process_project(client, project, args, state)
        processed += 1
        # 5-min gap before the next project (not after the last one).
        remaining = [
            p for p in projects[projects.index(project) + 1:]
            if args.overwrite or not (C.SKIP_FILLED and C.is_project_filled(p))
        ]
        if remaining and not (args.limit and processed >= args.limit):
            sleep_with_log(args.project_delay, "between projects", args.no_delay)

    log(f"=== reset loop finished: {processed} project(s) processed ===")
    run_pipeline(args)
    return 0


if __name__ == "__main__":
    sys.exit(main())
