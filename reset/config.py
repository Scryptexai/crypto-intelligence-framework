#!/usr/bin/env python3
"""
config.py — central configuration for the CIF Deep-Reset pipeline.
All values overridable via environment variables so the same code runs locally
and on a VPS cron without edits.
"""
from __future__ import annotations
import os
from pathlib import Path

# Repo root = parent of this reset/ folder.
ROOT = Path(__file__).resolve().parent.parent
RESET_DIR = ROOT / "reset"
PHASES_DIR = RESET_DIR / "phases"
STATE_DIR = RESET_DIR / "state"
PROJECTS_FILE = RESET_DIR / "projects.txt"
DATA_PROJECT = ROOT / "data_project"
STAGING_DIR = RESET_DIR / "temp"   # staged outputs live here until verified

# Phase file key order = the ingest.py PHASE_KEYS contract (NN-<key>.docx).
# Phase 11 (Validation & QA) is written to 11-conflict.docx per that contract.
PHASE_ORDER = [
    "01-foundation", "02-entity", "03-history", "04-technology", "05-financial",
    "06-token", "07-ecosystem", "08-market", "09-behavioral", "10-knowledge",
    "11-conflict",
]

# Pacing (seconds). Defaults per maintainer spec: 1 min between phases, 5 min between projects.
PHASE_DELAY_SEC = int(os.environ.get("RESET_PHASE_DELAY_SEC", "60"))
PROJECT_DELAY_SEC = int(os.environ.get("RESET_PROJECT_DELAY_SEC", "300"))

# Behaviour toggles.
SKIP_FILLED = os.environ.get("RESET_SKIP_FILLED", "true").lower() == "true"
OVERWRITE = os.environ.get("RESET_OVERWRITE", "false").lower() == "true"
# When true, run.sh build + sync is invoked after the reset loop finishes.
RUN_PIPELINE = os.environ.get("RESET_RUN_PIPELINE", "true").lower() == "true"
RUN_SYNC = os.environ.get("RESET_RUN_SYNC", "true").lower() == "true"

# A phase answer shorter than this is treated as a failed generation (matches
# ingest.py's MIN_PHASE_CHARS spirit) and retried once.
MIN_PHASE_CHARS = int(os.environ.get("RESET_MIN_PHASE_CHARS", "400"))


def project_dir(project: str, base: Path | None = None) -> Path:
    return (base or DATA_PROJECT) / project


def phase_path(project: str, phase_key: str, base: Path | None = None) -> Path:
    return project_dir(project, base) / f"{phase_key}.docx"


def load_phase_prompt(phase_key: str) -> str:
    return (PHASES_DIR / f"{phase_key}.txt").read_text(encoding="utf-8")


def load_projects() -> list[str]:
    """Read reset/projects.txt — one project per line, '#' comments and inline
    '# ...' tags stripped, blank lines ignored, order preserved."""
    out: list[str] = []
    for raw in PROJECTS_FILE.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        name = line.split("#", 1)[0].strip()  # drop inline "# [empty]" tag
        if name:
            out.append(name)
    return out


def is_project_filled(project: str) -> bool:
    """A project counts as filled when every phase file exists and is non-empty."""
    d = project_dir(project)
    if not d.exists():
        return False
    for key in PHASE_ORDER:
        f = d / f"{key}.docx"
        if not f.exists() or f.stat().st_size == 0:
            return False
    return True
