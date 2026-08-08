"""
cli.py — argument parsing and entrypoint wiring.

Kept separate from runner.py so the pipeline can be driven from other code (a test, a
notebook, a future scheduler) without going through argparse.
"""
import argparse
import sys
from pathlib import Path

from . import config, runner, validate
from .logs import log

DESCRIPTION = """\
CIF reset pipeline — Track C phased research, self-verifying and self-repairing.

Typical use:
  python3 reset/run_deepseek_reset.py --audit                     what's broken, no API calls
  python3 reset/run_deepseek_reset.py --commit --phases-limit 10  the real run (Phase 11 deferred)
  python3 reset/run_deepseek_reset.py --commit --phases-limit 10 --project Cosmos --redo-phases 2,3
"""


def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(description=DESCRIPTION,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--project", help="process only this one project, ignoring projects.txt")
    ap.add_argument("--projects-limit", type=int, default=0,
                    help="process only the first N projects from projects.txt (0 = all)")
    ap.add_argument("--phases-limit", type=int, default=0,
                    help="process only the first N phases per project (0 = all 11). "
                         "10 is the sanctioned value: Phase 11 deferred, and it enables the "
                         "verify -> promote -> ingest/extract/sync chain.")
    ap.add_argument("--dry-run", action="store_true",
                    help="no real API calls -- exercises file/loop logic only")
    ap.add_argument("--commit", action="store_true",
                    help="write real output into data_project/ (the actual dataset). Off by "
                         "default -- every run without this flag stays confined to "
                         "reset/tmp_test/ and never touches data_project/.")
    ap.add_argument("--output-root",
                    help="override where <project>/NN-<phasekey>.docx files get written, "
                         "instead of the --commit-based default. Rarely needed.")
    ap.add_argument("--parallel", type=int, default=1,
                    help="process this many projects concurrently (default 1). Raise gradually "
                         "and watch reset/failures.log for rate-limit errors.")
    ap.add_argument("--auto-sync", action="store_true",
                    help="only meaningful with --phases-limit 10: after a project passes the "
                         "quality gate and is promoted, also push it to the live CIF Supabase "
                         "database. Requires SUPABASE_URL + SUPABASE_SERVICE_ROLE_KEY.")
    ap.add_argument("--audit", action="store_true",
                    help="diagnose what's already on disk (per project, per phase) and exit. "
                         "Makes no API calls and writes nothing.")
    ap.add_argument("--redo-phases",
                    help="comma-separated phase numbers to regenerate for the selected "
                         "project(s), e.g. '9,10' or '2,3'. Deletes just those phase files "
                         "first so the resume logic regenerates them; every other phase is "
                         "loaded from disk as context at no API cost.")
    return ap


def _audit(projects: list, output_root: Path) -> int:
    """Per-phase verdict for projects that already have files on disk.

    Three outcomes, kept apart because they need different actions: a project where EVERY
    phase is empty simply hasn't been started (the queue will pick it up on the next run and
    it needs no decision), whereas a project with real content in some phases and problems in
    others is the one worth a targeted --redo-phases. Lumping them together buried 5 genuinely
    broken projects under 39 untouched scaffolds.
    """
    roots = {config.DATA_PROJECT_ROOT, output_root}
    clean, broken, not_started = [], [], []
    for name in projects:
        proj_dir = next((r / name for r in roots if (r / name).is_dir()), None)
        if proj_dir is None:
            continue
        report = validate.diagnose_project(name, proj_dir)
        bad = {k: v for k, v in report.items() if v != ["ok"]}
        if not bad:
            clean.append(name)
        elif all(v == ["empty"] or v == ["missing"] for v in report.values()):
            not_started.append(name)
        else:
            broken.append((name, bad))

    if not (clean or broken or not_started):
        print("no projects with files on disk matched the selection")
        return 0

    if clean:
        print(f"✓ {len(clean)} project(s) fully pass all phase checks:")
        print(f"    {', '.join(sorted(clean))}\n")

    if broken:
        print(f"✗ {len(broken)} project(s) need attention:\n")
        for name, bad in sorted(broken):
            phases = ",".join(str(int(p.split('-')[0])) for p in sorted(bad))
            print(f"  {name}")
            for phase, problems in sorted(bad.items()):
                print(f"      {phase:16} {', '.join(problems)}")
            print(f"      -> python3 reset/run_deepseek_reset.py --commit --phases-limit 10 "
                  f"--project '{name}' --redo-phases {phases}\n")

    if not_started:
        print(f"· {len(not_started)} project(s) not started yet (all phases empty) -- the "
              f"normal queue run will pick these up, no action needed.")
    return 0


def _delete_phases(projects: list, output_root: Path, phase_nums: list) -> None:
    """Remove the named phase files so the resume logic regenerates exactly those."""
    keys = {num: key for num, key in config.PHASES}
    for name in projects:
        for root in {config.DATA_PROJECT_ROOT, output_root}:
            proj_dir = root / name
            if not proj_dir.is_dir():
                continue
            for num in phase_nums:
                key = keys.get(num)
                if not key:
                    continue
                target = proj_dir / f"{num:02d}-{key}.docx"
                if target.exists():
                    target.unlink()
                    log(f"[{name}] --redo-phases: removed {target.relative_to(config.ROOT)} "
                        f"(will be regenerated)")


def main(argv=None) -> None:
    args = build_parser().parse_args(argv)

    if args.output_root:
        output_root = Path(args.output_root).resolve()
    elif args.commit:
        output_root = config.DATA_PROJECT_ROOT
    else:
        output_root = config.TMP_TEST_ROOT

    if args.project:
        projects = [args.project]
    else:
        projects = config.load_projects()
        if args.projects_limit:
            projects = projects[: args.projects_limit]

    if args.audit:
        sys.exit(_audit(projects, output_root))

    base_url, token, model = config.load_credentials()
    if not args.dry_run and not (base_url and token and model):
        sys.exit("ANTHROPIC_BASE_URL, ANTHROPIC_AUTH_TOKEN, and ANTHROPIC_MODEL must all be set "
                 "in the environment (never hardcode these in a file). Use --dry-run to test "
                 "the pipeline's control flow without an API key, or --audit to inspect "
                 "existing files without any credentials at all.")

    if args.redo_phases:
        try:
            phase_nums = [int(p.strip()) for p in args.redo_phases.split(",") if p.strip()]
        except ValueError:
            sys.exit(f"--redo-phases expects comma-separated numbers, got: {args.redo_phases!r}")
        _delete_phases(projects, output_root, phase_nums)

    mode = ("COMMIT (writing to data_project/, the real dataset)"
            if output_root == config.DATA_PROJECT_ROOT
            else f"TEST (writing to {output_root}, not the real dataset -- pass --commit for a "
                 f"real run)")
    repair_note = ("self-repair ON" if config.REPAIR_ENABLED else "self-repair OFF")
    log(f"Starting reset pipeline for {len(projects)} project(s): {', '.join(projects)} "
        f"-- mode: {mode} -- {repair_note}"
        + (f" -- parallel={args.parallel}" if args.parallel > 1 else ""))

    runner.run_queue(projects, base_url, token, model, args.dry_run, args.phases_limit,
                     output_root, args.auto_sync, args.parallel)
