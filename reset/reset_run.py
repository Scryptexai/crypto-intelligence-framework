#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CIF Deep Reset Runner — modular multi-phase research pipeline.

Reads the 11 Track C phase prompts from reset/prompts/*.txt (fixed vs the
original DeepSeek run, see docs/Protocol/Phased-Research-Prompts.md) and the
project list from reset/projects.txt. For every project it calls the
Anthropic-compatible DeepSeek API phase by phase, feeds each phase the output
of the previous phase as context, and writes the raw answer into
`data_project/<Project>/NN-<phasekey>.docx` (plain-text .docx per the repo's
naming contract).

Pacing (default):
  - 60s  pause between phases  (--phase-gap)
  - 300s pause between projects (--project-gap)
  - resumes where it left off; safe to run once per 24h via cron.

Env (required):
  ANTHROPIC_BASE_URL   e.g. https://api.hcnsec.cn/
  ANTHROPIC_AUTH_TOKEN e.g. sk-...
  ANTHROPIC_MODEL      e.g. DeepSeek-V4-Pro

Usage:
  python3 reset/reset_run.py                     # all projects, all phases, resume
  python3 reset/reset_run.py --projects aptos    # one project only
  python3 reset/reset_run.py --phases 1-3        # phases 1..3 only
  python3 reset/reset_run.py --force             # re-run even completed phases
  python3 reset/reset_run.py --dry-run           # print plan, no API calls
  python3 reset/reset_run.py --once              # stop after first project
  python3 reset/reset_run.py --parallel 3        # 3 projects concurrently (optional)
"""
import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROMPTS_DIR = ROOT / "reset" / "prompts"
PROJECTS_FILE = ROOT / "reset" / "projects.txt"
DATA_ROOT = ROOT / "data_project"
STATE_DIR = ROOT / "reset" / "state"
LOG_DIR = ROOT / "reset" / "logs"

# Data_project filename contract: NN-<phasekey>.docx (exact phase keys)
PHASE_KEYS = [
    "foundation", "entity", "history", "technology", "financial", "token",
    "ecosystem", "market", "behavioral", "knowledge", "conflict",
]

API_TIMEOUT = 600          # seconds per request (long research outputs)
DEFAULT_MAX_TOKENS = 32000
DEFAULT_TEMPERATURE = 0.3
MAX_RETRIES = 3
RETRY_BACKOFF = 20         # seconds


# --------------------------------------------------------------------- #
# logging                                                                #
# --------------------------------------------------------------------- #
def log(msg: str):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{ts}] {msg}"
    print(line, flush=True)
    try:
        LOG_DIR.mkdir(parents=True, exist_ok=True)
        with open(LOG_DIR / "reset.log", "a", encoding="utf-8") as fh:
            fh.write(line + "\n")
    except Exception:
        pass


# --------------------------------------------------------------------- #
# API client (Anthropic /v1/messages compatible)                        #
# --------------------------------------------------------------------- #
def call_api(prompt: str, model: str, base_url: str, token: str,
             max_tokens: int, temperature: float) -> dict:
    """Returns {'text': str, 'stop_reason': str|None}. Raises on transport error."""
    url = base_url.rstrip("/") + "/v1/messages"
    payload = {
        "model": model,
        "max_tokens": max_tokens,
        "temperature": temperature,
        "messages": [{"role": "user", "content": prompt}],
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}",
            "anthropic-version": "2023-06-01",
        },
        method="POST",
    )
    last_err = None
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            with urllib.request.urlopen(req, timeout=API_TIMEOUT) as resp:
                body = json.loads(resp.read().decode("utf-8"))
            texts = []
            for blk in body.get("content", []):
                if blk.get("type") == "text":
                    texts.append(blk.get("text", ""))
            return {"text": "\n".join(texts), "stop_reason": body.get("stop_reason")}
        except urllib.error.HTTPError as e:
            detail = e.read().decode("utf-8", "ignore")[:300]
            last_err = f"HTTP {e.code}: {detail}"
        except Exception as e:  # noqa: BLE001
            last_err = str(e)
        if attempt < MAX_RETRIES:
            wait = RETRY_BACKOFF * attempt
            log(f"  ⚠ retry {attempt}/{MAX_RETRIES} setelah {wait}s — {last_err[:120]}")
            time.sleep(wait)
    raise RuntimeError(last_err or "API call failed")


# --------------------------------------------------------------------- #
# prompts                                                                #
# --------------------------------------------------------------------- #
def load_prompts() -> list[dict]:
    """Load prompts in phase order. Returns [{phase, key, text, file}]."""
    out = []
    for i, key in enumerate(PHASE_KEYS, start=1):
        f = PROMPTS_DIR / f"{i:02d}-{key}.txt"
        if not f.exists():
            log(f"  ✗ prompt hilang: {f}")
            continue
        out.append({"phase": i, "key": key, "text": f.read_text(encoding="utf-8").strip(), "file": f})
    return out


def build_prompt(proj: str, phase: dict, prior_output: str | None) -> str:
    text = phase["text"]
    # Project name substitution (Phase 1 template + any placeholder)
    text = text.replace("{PROJECT_NAME}", proj).replace("<NAMA PROJECT>", proj)
    if phase["phase"] == 1:
        return text
    # Phases 2..11: append previous phase output as context (continuous-chat style)
    if prior_output:
        text += (
            "\n\n========================================================\n"
            f"KONTEKS: OUTPUT {phase['phase'] - 1:02d} (dari chat sebelumnya, "
            f"phase {PHASE_KEYS[phase['phase'] - 2]})\n"
            "Gunakan sebagai dasar riset fase ini. JANGAN mengulang isi konteks ini "
            "di output; langsung kerjakan instruksi fase ini dengan konteks tsb.\n"
            "========================================================\n\n"
            f"{prior_output}\n"
        )
    return text


# --------------------------------------------------------------------- #
# state (resume)                                                        #
# --------------------------------------------------------------------- #
def state_file(proj: str) -> Path:
    return STATE_DIR / f"{proj.lower().replace(' ', '_')}.json"


def load_state(proj: str) -> dict:
    sf = state_file(proj)
    if sf.exists():
        try:
            return json.loads(sf.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {"project": proj, "phases": {}}


def save_state(proj: str, st: dict):
    try:
        STATE_DIR.mkdir(parents=True, exist_ok=True)
        state_file(proj).write_text(json.dumps(st, indent=2), encoding="utf-8")
    except Exception as e:
        log(f"  ⚠ gagal simpan state: {e}")


def phase_done(proj: str, phase: int, key: str) -> bool:
    f = DATA_ROOT / proj / f"{phase:02d}-{key}.docx"
    return f.exists() and f.stat().st_size > 200


def phase_output_path(proj: str, phase: int, key: str) -> Path:
    return DATA_ROOT / proj / f"{phase:02d}-{key}.docx"


def load_prior_output(proj: str, phase_no: int) -> str | None:
    """Output fase (phase_no-1) dari disk — agar fase 2..11 selalu dapat
    konteks meski dijalankan per-subset (mis. --phases 2) atau resume."""
    if phase_no <= 1:
        return None
    prev_key = PHASE_KEYS[phase_no - 2]
    f = phase_output_path(proj, phase_no - 1, prev_key)
    try:
        txt = f.read_text(encoding="utf-8").strip()
        return txt if len(txt) > 200 else None
    except Exception:
        return None


# --------------------------------------------------------------------- #
# single phase run                                                      #
# --------------------------------------------------------------------- #
def run_phase(proj: str, phase: dict, prior_output: str | None, cfg: dict) -> dict:
    key, n = phase["key"], phase["phase"]
    out_path = phase_output_path(proj, n, key)
    prompt = build_prompt(proj, phase, prior_output)

    log(f"  → Phase {n:02d}/{len(PHASE_KEYS)} [{key}] — memanggil API…")
    t0 = time.time()
    res = call_api(
        prompt,
        model=cfg["model"],
        base_url=cfg["base_url"],
        token=cfg["token"],
        max_tokens=cfg["max_tokens"],
        temperature=cfg["temperature"],
    )
    text = res["text"].strip()
    dt = time.time() - t0

    if not text:
        raise RuntimeError("API mengembalikan output kosong")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(text + "\n", encoding="utf-8")
    truncated = res.get("stop_reason") == "max_tokens"
    log(f"  ✓ Phase {n:02d} [{key}] → {out_path.name} "
        f"({len(text)} chars, {dt:.0f}s{', TRUNCATED' if truncated else ''})")
    return {"ok": True, "chars": len(text), "seconds": round(dt), "truncated": truncated}


# --------------------------------------------------------------------- #
# full project                                                          #
# --------------------------------------------------------------------- #
def run_project(proj: str, prompts: list[dict], cfg: dict) -> dict:
    state = load_state(proj)
    results = {"project": proj, "phases": []}
    prior_output: str | None = None
    total_phases = len(prompts)
    started_any = False

    for phase in prompts:
        n, key = phase["phase"], phase["key"]
        # Konteks = output fase sebelumnya (dari disk bila ada — mendukung subset/resume)
        disk_prior = load_prior_output(proj, n)
        if disk_prior:
            prior_output = disk_prior

        if not cfg["force"] and phase_done(proj, n, key):
            log(f"  ⏭ Phase {n:02d} [{key}] sudah ada — dilewati (resume)")
            prior_output = phase_output_path(proj, n, key).read_text(encoding="utf-8") if phase_done(proj, n, key) else prior_output
            state["phases"][key] = {"done": True, "ts": time.time()}
            results["phases"].append({"phase": n, "key": key, "status": "skip"})
            continue

        try:
            r = run_phase(proj, phase, prior_output, cfg)
            prior_output = phase_output_path(proj, n, key).read_text(encoding="utf-8")
            state["phases"][key] = {"done": True, "ts": time.time(), **r}
            results["phases"].append({"phase": n, "key": key, "status": "ok", **r})
            started_any = True
        except Exception as e:  # noqa: BLE001
            log(f"  ✗ Phase {n:02d} [{key}] GAGAL: {str(e)[:200]}")
            state["phases"][key] = {"done": False, "error": str(e)[:300], "ts": time.time()}
            results["phases"].append({"phase": n, "key": key, "status": "error", "error": str(e)[:200]})
            # Lanjut ke fase berikutnya; konteks = state terakhir yang berhasil
            continue

        save_state(proj, state)

        # pause antar phase (kecuali phase terakhir)
        if n < total_phases:
            log(f"  ⏳ jeda {cfg['phase_gap']}s sebelum phase {n+1:02d}…")
            time.sleep(cfg["phase_gap"])

    save_state(proj, state)
    return results


# --------------------------------------------------------------------- #
# main                                                                  #
# --------------------------------------------------------------------- #
def main():
    ap = argparse.ArgumentParser(description="CIF Deep Reset Runner")
    ap.add_argument("--projects", help="comma list of projects (default: all from projects.txt)")
    ap.add_argument("--phases", help="phase range, e.g. 1-11 or 1,3,5")
    ap.add_argument("--force", action="store_true", help="re-run completed phases")
    ap.add_argument("--dry-run", action="store_true", help="print plan only")
    ap.add_argument("--once", action="store_true", help="stop after first project")
    ap.add_argument("--parallel", type=int, default=1, help="projects run concurrently (default 1)")
    ap.add_argument("--phase-gap", type=int, default=60, help="pause seconds between phases")
    ap.add_argument("--project-gap", type=int, default=300, help="pause seconds between projects")
    ap.add_argument("--max-tokens", type=int, default=DEFAULT_MAX_TOKENS)
    ap.add_argument("--temperature", type=float, default=DEFAULT_TEMPERATURE)
    args = ap.parse_args()

    base_url = os.environ.get("ANTHROPIC_BASE_URL", "").strip()
    token = os.environ.get("ANTHROPIC_AUTH_TOKEN", "").strip()
    model = os.environ.get("ANTHROPIC_MODEL", "").strip()
    if not (base_url and token and model):
        sys.exit("✖ Set ANTHROPIC_BASE_URL, ANTHROPIC_AUTH_TOKEN, ANTHROPIC_MODEL "
                 "(lihat reset/README.md)")

    cfg = {
        "base_url": base_url, "token": token, "model": model,
        "max_tokens": args.max_tokens, "temperature": args.temperature,
        "phase_gap": args.phase_gap, "project_gap": args.project_gap,
        "force": args.force,
    }

    # projects
    if args.projects:
        projects = [p.strip() for p in args.projects.split(",") if p.strip()]
    else:
        projects = [ln.strip() for ln in PROJECTS_FILE.read_text(encoding="utf-8").splitlines()
                    if ln.strip() and not ln.startswith("#")]
    if not projects:
        sys.exit("✖ Tidak ada project (cek reset/projects.txt)")

    # phases (range filter)
    prompts = load_prompts()
    if args.phases:
        sel = set()
        for part in args.phases.split(","):
            part = part.strip()
            if "-" in part:
                a, b = part.split("-")
                sel.update(range(int(a), int(b) + 1))
            elif part:
                sel.add(int(part))
        prompts = [p for p in prompts if p["phase"] in sel]
    if not prompts:
        sys.exit("✖ Tidak ada prompt (cek reset/prompts/*.txt)")

    log(f"== CIF DEEP RESET — {len(projects)} project · {len(prompts)} phase · model={model} ==")
    log(f"   pacing: {cfg['phase_gap']}s/phase · {cfg['project_gap']}s/project · "
        f"parallel={args.parallel} · force={cfg['force']}")
    if args.dry_run:
        for proj in projects:
            for ph in prompts:
                done = phase_done(proj, ph["phase"], ph["key"])
                print(f"  {'[ada]' if done else '[run]'} {proj} → {ph['phase']:02d}-{ph['key']}.docx")
        return

    # run
    if args.parallel and args.parallel > 1:
        with ThreadPoolExecutor(max_workers=args.parallel) as ex:
            futs = {ex.submit(run_project, proj, prompts, cfg): proj for proj in projects}
            for i, fut in enumerate(as_completed(futs)):
                proj = futs[fut]
                try:
                    r = fut.result()
                    log(f"== Selesai {proj}: {sum(1 for p in r['phases'] if p['status']=='ok')} phase OK ==")
                except Exception as e:  # noqa: BLE001
                    log(f"== {proj} GAGAL: {e} ==")
                if i < len(projects) - 1:
                    log(f"⏳ jeda {cfg['project_gap']}s antar project…")
                    time.sleep(cfg["project_gap"])
                if args.once:
                    break
    else:
        for i, proj in enumerate(projects):
            log(f"\n########## PROJECT {i+1}/{len(projects)}: {proj} ##########")
            try:
                r = run_project(proj, prompts, cfg)
                ok = sum(1 for p in r["phases"] if p["status"] == "ok")
                log(f"== {proj}: {ok}/{len(r['phases'])} phase OK ==")
            except Exception as e:  # noqa: BLE001
                log(f"== {proj} GAGAL TOTAL: {e} ==")
            if i < len(projects) - 1:
                log(f"⏳ jeda {cfg['project_gap']}s sebelum project berikutnya…")
                time.sleep(cfg["project_gap"])
            if args.once:
                log("--once: berhenti setelah project pertama")
                break

    log("== SELESAI ==")


if __name__ == "__main__":
    main()
