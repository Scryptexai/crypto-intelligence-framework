"""
pipeline.py — everything that happens AFTER a project's phases are generated and verified:
promotion into data_project/, then the ingest -> build -> extract -> sync chain.

Deliberately drives the existing tools/*.py scripts as subprocesses instead of importing
their internals. That keeps a genuinely independent second gate: tools/ingest.py runs its
own validate_phase_content() against the ASSEMBLED dossier, catching defects that only
appear after assembly, which no amount of per-phase checking here would see.
"""
import os
import subprocess
import sys

from . import config
from .logs import log

# tools/*.py chained after promotion succeeds -- each takes just this project's assembled
# dossier, no repo-wide reprocessing except build_json.py (fast, deterministic, and operating
# on the full examples/CaseStudies/ roster by design).
EXTRACT_SCRIPTS = ["extract_entities.py", "extract_decision_events.py", "extract_knowledge.py",
                   "extract_behavior.py", "extract_qa.py", "extract_events.py"]
# cif_patterns/cif_backtests/cif_decision_events are the OLD AirdropOS-style schema, not part
# of the dedicated CIF Supabase project (uqtvjerhgvwoxiejvrli has only the 13
# intelligence-workspace tables) -- excluded on purpose. "conflicts" is excluded too: nothing
# in EXTRACT_SCRIPTS populates poc/conflicts.json automatically (tools/extract_conflicts.py is
# hand-curated per project), so syncing it here would just re-push whatever is already in that
# file rather than this project's actual conflicts.
SYNC_TABLES = ("projects,entities,knowledge_items,evidence_items,events,"
               "qa_dimensions,qa_phases,behavior_profiles")


def promote_to_data_project(name: str, src_dir) -> None:
    """Copies phases 1-10 (NOT phase 11 -- deliberately deferred) into data_project/<name>/.
    Only called after validate.verify_10_phases() passes."""
    dest_dir = config.DATA_PROJECT_ROOT / name
    dest_dir.mkdir(parents=True, exist_ok=True)
    for num, key in config.PHASES[:10]:
        src = src_dir / f"{num:02d}-{key}.docx"
        if src.exists():
            (dest_dir / f"{num:02d}-{key}.docx").write_text(
                src.read_text(encoding="utf-8"), encoding="utf-8")


def _run(cmd: list) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, cwd=config.ROOT, capture_output=True, text=True)


def run_ingest_extract_sync(name: str, auto_sync: bool) -> tuple:
    """Chains ingest -> build_json -> extract_* -> (optionally) sync for one project.

    Each stage is a hard gate: a failure stops the chain for THIS project (nothing further
    runs, the database is never touched) and returns (False, reason); the caller moves on to
    the next project regardless, same as a failed quality gate never blocking the queue.

    auto_sync gates ONLY the final database write -- ingest+build+extract always run and are
    safe. Even with --auto-sync, a project reaches sync_supabase.py only after BOTH
    verify_10_phases (raw-phase level) and ingest.py's validator (assembled-dossier level)
    have passed for it specifically.
    """
    dossier_path = config.ROOT / "examples" / "CaseStudies" / f"{name}.md"

    # Phase 11 is deliberately deferred (this chain only fires for --phases-limit 10 runs),
    # but data_project/<name>/11-conflict.docx usually exists as an empty 0-byte scaffold.
    # ingest.py globs *.docx unconditionally, so it WOULD pick that up, detect it as the
    # "conflict" phase, then hard-fail the whole project on near-empty content rather than
    # treating it as absent. Move it aside for this one call (--allow-partial then correctly
    # reports "missing phase(s): conflict") and always restore it afterward.
    conflict_path = config.DATA_PROJECT_ROOT / name / "11-conflict.docx"
    conflict_stash = None
    if (conflict_path.exists()
            and len(conflict_path.read_text(encoding="utf-8").strip()) < config.MIN_PHASE_CHARS):
        conflict_stash = conflict_path.with_suffix(".docx.pending")
        conflict_path.rename(conflict_stash)
    # --force, unconditionally. ingest.py's anti-duplicate guard skips any project whose
    # dossier already exists. That is right for the inbox flow and wrong here: once a phase is
    # regenerated the assembled dossier is stale, and every extractor downstream reads the
    # DOSSIER, not the phase files.
    #
    # Observed on Lido 2026-08-08 and the reason this exists: Phase 9 regenerated cleanly
    # (0 failed checks, 47,772 chars, verify PASS), the run reported success end to end, and
    # poc/behavior.json still had no Lido entry -- ingest had logged "dossier exists /
    # skipped(dup)" and the extractors re-parsed the old file. A silent no-op like that is
    # worse than an error: it looks finished while the data never moves.
    #
    # Rebuilding always, instead of detecting staleness, is deliberate. Timestamps are
    # unreliable (git checkout and rsync rewrite them). Content probing is worse: ingest
    # relocates each phase's "Open Threads" into its own section and reflows prose, so the
    # assembled text is not a substring of its inputs -- a probe-based attempt flagged every
    # healthy project (Lido, Blast, Arbitrum, Aave, Cardano) as stale, while a single mid-file
    # probe had the opposite failure and missed a pure append, the commonest shape of a
    # regenerated fuller phase. Assembly is deterministic and the only date in the output is a
    # month-granular archive filename, so rebuilding an unchanged project reproduces the file
    # byte for byte and creates no git churn.
    try:
        result = _run([sys.executable, "tools/ingest.py", "--type", "data_project",
                       "--input", f"data_project/{name}", "--model", "DeepSeek",
                       "--no-build", "--allow-partial", "--force"])
    finally:
        if conflict_stash is not None and conflict_stash.exists():
            conflict_stash.rename(conflict_path)

    for line in result.stdout.strip().splitlines()[-3:]:
        log(f"  [{name}] ingest: {line}")
    if result.returncode != 0:
        log(f"  [{name}] ✗ ingest.py failed validation -- stopping chain, nothing synced. "
            f"stderr: {result.stderr.strip()[-500:]}")
        return False, "ingest_failed"
    if not dossier_path.exists():
        log(f"  [{name}] ✗ ingest.py exited 0 but {dossier_path} wasn't created -- stopping.")
        return False, "ingest_no_output"

    result = _run([sys.executable, "tools/build_json.py"])
    if result.returncode != 0:
        log(f"  [{name}] ✗ build_json.py failed -- stopping chain. "
            f"stderr: {result.stderr.strip()[-500:]}")
        return False, "build_json_failed"

    for script in EXTRACT_SCRIPTS:
        result = _run([sys.executable, f"tools/{script}", str(dossier_path)])
        if result.returncode != 0:
            log(f"  [{name}] ✗ {script} failed -- stopping chain. "
                f"stderr: {result.stderr.strip()[-500:]}")
            return False, f"{script}_failed"

    log(f"  [{name}] ingest + build + extract complete -- poc/*.json updated.")

    if not auto_sync:
        log(f"  [{name}] --auto-sync not passed -- stopping here (not synced). Run "
            f"'python3 tools/sync_supabase.py' yourself when ready.")
        return True, "ingested_not_synced"

    if not (os.environ.get("SUPABASE_URL") and os.environ.get("SUPABASE_SERVICE_ROLE_KEY")):
        log(f"  [{name}] ✗ --auto-sync passed but SUPABASE_URL/SUPABASE_SERVICE_ROLE_KEY "
            f"aren't both set -- skipping sync (data is safely in poc/*.json).")
        return True, "ingested_not_synced_no_creds"

    result = _run([sys.executable, "tools/sync_supabase.py", "--only", SYNC_TABLES])
    if result.returncode != 0:
        log(f"  [{name}] ✗ sync_supabase.py failed -- stderr: {result.stderr.strip()[-500:]}")
        return False, "sync_failed"
    log(f"  [{name}] ✅ synced to Supabase (tables: {SYNC_TABLES}).")
    return True, "synced"
