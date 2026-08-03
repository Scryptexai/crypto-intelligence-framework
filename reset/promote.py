#!/usr/bin/env python3
"""
promote.py — move a VERIFIED staged project from reset/temp/<Project>/ into
data_project/<Project>/ with the correct NN-<key>.docx filenames.

Refuses to promote unless reset/verify.py passes ALL 11 phases, so nothing
half-formed or wrongly-structured ever reaches data_project/ (and therefore
never reaches run.sh/ingest/Supabase). This is the ONLY step that lets the
reset workflow "leave the reset/ folder".

Usage:
  python3 reset/promote.py <Project>            # verify staged, then promote
  python3 reset/promote.py <Project> --force    # promote even if verify fails (NOT recommended)
"""
from __future__ import annotations
import argparse
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import config as C
from verify import verify_project


def promote(project: str, force: bool) -> int:
    staged = C.STAGING_DIR / project
    if not staged.exists():
        print(f"✖ nothing staged at {staged}")
        return 2

    ok = verify_project(project, C.STAGING_DIR)
    if not ok and not force:
        print(f"\n✖ REFUSING to promote {project}: verification failed (use --force to override).")
        return 1

    dest = C.project_dir(project)  # data_project/<Project>
    dest.mkdir(parents=True, exist_ok=True)
    moved = 0
    for key in C.PHASE_ORDER:
        src = staged / f"{key}.docx"
        if src.exists() and src.stat().st_size > 0:
            shutil.copyfile(src, dest / f"{key}.docx")
            moved += 1
    print(f"\n✓ promoted {project}: {moved}/11 phase files -> {dest.relative_to(C.ROOT)}")
    print("  (data_project updated; run ./run.sh build && ./run.sh sync when ready)")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Verify + promote a staged project")
    ap.add_argument("project")
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()
    return promote(args.project, args.force)


if __name__ == "__main__":
    sys.exit(main())
