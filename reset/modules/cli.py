"""
cli.py — argument parsing and entrypoint wiring.

Kept separate from runner.py so the pipeline can be driven from other code (a test, a
notebook, a future scheduler) without going through argparse.
"""
import argparse
import json
import sys
from datetime import datetime, timezone
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
    ap.add_argument("--audit-json", action="store_true",
                    help="same inspection as --audit but printed as JSON on stdout, for a "
                         "driver script to consume (see reset/run_pipeline_stages.sh). Adds "
                         "the phase-11 split --audit doesn't show: which clean projects still "
                         "need it. Also makes no API calls and writes nothing.")
    ap.add_argument("--redo-phases",
                    help="comma-separated phase numbers to regenerate for the selected "
                         "project(s), e.g. '9,10' or '2,3'. Deletes just those phase files "
                         "first so the resume logic regenerates them; every other phase is "
                         "loaded from disk as context at no API cost.")
    return ap


def _classify(projects: list, output_root: Path) -> tuple:
    """Sorts every project with files on disk into clean / broken / not-started.

    Three outcomes, kept apart because they need different actions: a project where EVERY
    phase is empty simply hasn't been started (the queue will pick it up on the next run and
    it needs no decision), whereas a project with real content in some phases and problems in
    others is the one worth a targeted --redo-phases. Lumping them together buried 5 genuinely
    broken projects under 39 untouched scaffolds.

    Returns (clean, broken, not_started, dirs) where broken is [(name, {phase: [problem]})]
    and dirs maps every classified name to the directory it was read from.
    """
    # Ordered and deduplicated, with the real dataset first. This was a set until 2026-08-08,
    # which made the verdict for any project present in BOTH roots depend on set iteration
    # order -- i.e. on PYTHONHASHSEED, so it changed between runs of the same command. Aptos
    # is the live example: a stale reset/tmp_test/Aptos/ from an old test run sat next to the
    # real data_project/Aptos/, and consecutive audits reported "phases 2,3,9,10 broken" and
    # "phase 9 broken" for it. Harmless while a human read the output; not harmless once a
    # driver script regenerates whatever the audit names.
    #
    # data_project/ wins because that is the dataset that ships, and because the fix command
    # --audit prints is a --commit command, which writes there regardless of what was read.
    roots = [config.DATA_PROJECT_ROOT] + [r for r in (output_root,)
                                          if r != config.DATA_PROJECT_ROOT]
    clean, broken, not_started, dirs = [], [], [], {}
    for name in projects:
        proj_dir = next((r / name for r in roots if (r / name).is_dir()), None)
        if proj_dir is None:
            continue
        dirs[name] = proj_dir
        report = validate.diagnose_project(name, proj_dir)
        bad = {k: v for k, v in report.items() if v != ["ok"]}
        if not bad:
            clean.append(name)
        elif all(v == ["empty"] or v == ["missing"] for v in report.values()):
            not_started.append(name)
        else:
            broken.append((name, bad))
    return clean, broken, not_started, dirs


def _phases_of(bad: dict) -> list:
    """The phase numbers behind a --audit "needs attention" entry, e.g. {"09-behavioral": ...}
    -> [9]. This is what --redo-phases takes."""
    return sorted(int(p.split("-")[0]) for p in bad)


def _audit_json(projects: list, output_root: Path) -> int:
    """--audit's classification as JSON, plus the phase-11 split, for reset/run_pipeline_stages.sh.

    Deliberately recomputed from disk on every call rather than written once to a state file.
    The staged driver runs for a day or more and repairs projects as it goes, so a list frozen
    at the start is wrong by the time the later stages read it -- exactly the drift that makes
    a hardcoded "group B" go stale mid-run.

    phase11_todo encodes the maintainer's rule directly: Phase 11 is only for projects already
    clear on phases 1-10. A project that is broken, or never started, is not in it -- running
    an audit of phases that don't exist yet would produce a confident QA report about nothing.

    "Done" means the audit PARSES, not that a file exists. Until 2026-08-09 this only checked
    length, so a Phase 11 that failed its spec checks and was saved anyway counted as finished:
    the driver skipped it on every later run, and the project could never recover even after
    the underlying bug was fixed. Aave, Aptos and Avalanche all landed in that state. They come
    back as phase11_bad, which the driver regenerates with --redo-phases 11 -- and if a fix
    elsewhere made the existing file parseable after all, they simply move to phase11_done and
    cost nothing.
    """
    clean, broken, not_started, dirs = _classify(projects, output_root)

    from . import specs  # local: pulls tools/extract_*.py in, and only --audit-json needs it

    phase11_done, phase11_todo, phase11_bad = [], [], []
    for name in clean:
        path = dirs[name] / "11-conflict.docx"
        text = path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""
        if len(text.strip()) < config.MIN_PHASE_CHARS:
            phase11_todo.append(name)
            continue
        failed = specs.run_checks(11, "conflict", name, text)
        if failed:
            phase11_bad.append({"project": name,
                                "checks": [c.name for c, _ in failed],
                                "detail": failed[0][1][:200]})
        else:
            phase11_done.append(name)

    # Phase 12 candidates are the projects whose Phase 11 parses -- not merely "clean".
    # The airdrop phase is built on Phases 1-11 in one conversation, so a project whose audit
    # is still broken would be reasoning about a report that is about to be regenerated.
    phase12_done, phase12_todo, phase12_bad = [], [], []
    for name in phase11_done:
        path = dirs[name] / "12-airdrop.docx"
        text = path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""
        if len(text.strip()) < config.MIN_PHASE_CHARS:
            phase12_todo.append(name)
            continue
        failed = specs.run_checks(12, "airdrop", name, text)
        if failed:
            phase12_bad.append({"project": name,
                                "checks": [c.name for c, _ in failed],
                                "detail": failed[0][1][:200]})
        else:
            phase12_done.append(name)

    print(json.dumps({
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "output_root": str(output_root),
        "clean": sorted(clean),
        "broken": [{"project": name, "phases": _phases_of(bad), "problems": bad}
                   for name, bad in sorted(broken)],
        "not_started": sorted(not_started),
        "phase11_done": sorted(phase11_done),
        "phase11_todo": sorted(phase11_todo),
        "phase11_bad": sorted(phase11_bad, key=lambda e: e["project"]),
        "phase12_done": sorted(phase12_done),
        "phase12_todo": sorted(phase12_todo),
        "phase12_bad": sorted(phase12_bad, key=lambda e: e["project"]),
    }, indent=2))
    return 0


def _audit(projects: list, output_root: Path) -> int:
    """Human-readable per-phase verdict for projects that already have files on disk."""
    clean, broken, not_started, _ = _classify(projects, output_root)

    if not (clean or broken or not_started):
        print("no projects with files on disk matched the selection")
        return 0

    if clean:
        print(f"✓ {len(clean)} project(s) fully pass all phase checks:")
        print(f"    {', '.join(sorted(clean))}\n")

    if broken:
        print(f"✗ {len(broken)} project(s) need attention:\n")
        for name, bad in sorted(broken):
            phases = ",".join(str(n) for n in _phases_of(bad))
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
    """Set the named phases aside so the resume logic regenerates exactly those.

    Renamed to <file>.bak rather than deleted. A regeneration can come back WORSE than what
    it replaced -- observed live 2026-08-08, when a prompt change made the model answer Phase
    9 with a 622-char stub, wiping Aave's complete 25KB phase (12 decision events -> 0) with
    no way back except git. phases.run_phase compares the new output against this backup and
    keeps whichever scores better, so a bad regeneration can no longer destroy good data.
    """
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
                    backup = target.with_suffix(".docx.bak")
                    target.replace(backup)
                    log(f"[{name}] --redo-phases: set aside "
                        f"{target.relative_to(config.ROOT)} -> {backup.name} "
                        f"(regenerating; the better of the two is kept)")


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

    if args.audit_json:
        sys.exit(_audit_json(projects, output_root))
    if args.audit:
        sys.exit(_audit(projects, output_root))

    providers = config.load_providers()
    base_url, token, model = providers[0].base_url, providers[0].token, providers[0].model
    if not args.dry_run and not (base_url and token and model):
        sys.exit("ANTHROPIC_BASE_URL, ANTHROPIC_AUTH_TOKEN, and ANTHROPIC_MODEL must all be set "
                 "in the environment (never hardcode these in a file). Use --dry-run to test "
                 "the pipeline's control flow without an API key, or --audit to inspect "
                 "existing files without any credentials at all.")

    chain = " -> ".join(f"{p.name}({p.model})" for p in providers)
    if config.STREAM_RESPONSES:
        mode = ("streaming ON -- every phase goes out as ONE call; the gateway's ~300s "
                "non-streaming ceiling does not apply")
    elif len(providers) > 1 or any(p.heavy_capable for p in providers):
        mode = ("streaming OFF -- heavy phases (9, 11) rely on rotating to a heavy-capable "
                "provider to survive the gateway's ~300s ceiling")
    else:
        mode = ("streaming OFF and no fallback provider -- heavy phases (9, 11) fall back to "
                "the STAGED split, which risks duplicated sections; prefer leaving streaming on")
    log(f"Provider chain: {chain} | {mode}")
    if len(providers) == 1:
        log("  (set DEEPSEEK_API_KEY to add a fallback provider for capacity failures)")

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

    failed = runner.run_queue(projects, providers, args.dry_run, args.phases_limit,
                              output_root, args.auto_sync, args.parallel)
    # Non-zero when any project failed, so a caller can react. Everything already written to
    # disk stays written -- this reports the outcome, it does not undo anything.
    if failed:
        sys.exit(1)
