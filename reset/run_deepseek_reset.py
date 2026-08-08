#!/usr/bin/env python3
"""
run_deepseek_reset.py — entrypoint for the CIF reset pipeline (Track C phased research).

This file is deliberately thin. All logic lives in reset/modules/; see that package's
__init__.py for the layer map and for where to make a given kind of change.

WHAT THIS DOES
    For each project in reset/projects.txt, runs the 11-phase Track C research pipeline as
    one continuous conversation, saving each phase to <output_root>/<Project>/NN-<key>.docx.
    Phases already on disk are loaded as context instead of being re-requested, so a run is
    always resumable and re-running costs nothing for work already done.

    With --phases-limit 10 (the sanctioned mode -- Phase 11 is deferred), a project that
    passes the quality gate is promoted into data_project/ and chained through
    ingest -> build_json -> extract_* -> optionally Supabase, each stage a hard gate.

THREE LAYERS OF QUALITY CONTROL
    1. Per-phase, at generation time (modules/specs.py + modules/repair.py)
       Every phase is checked against the REAL downstream parsers the moment it arrives. On
       failure the output is sent back with a precise corrective instruction and regenerated,
       up to RESET_MAX_REPAIR_ATTEMPTS times. This is the self-healing loop: format drift is
       fixed during the run instead of surfacing days later as an empty database table.
    2. Per-project, after all 10 phases exist (modules/validate.py)
       verify_10_phases runs phases 2/3/9/10 through extract_entities / extract_events /
       extract_decision_events / extract_knowledge. Zero rows anywhere = not promoted.
    3. Per-project, after assembly (tools/ingest.py, driven by modules/pipeline.py)
       ingest.py re-validates the ASSEMBLED dossier (PROJECT header, citation density,
       duplicate content). Only then can anything reach the database.

CREDENTIALS — environment only, NEVER hardcoded or logged:
    ANTHROPIC_BASE_URL     e.g. https://api.hcnsec.cn/   (OpenAI-compatible endpoint despite
    ANTHROPIC_AUTH_TOKEN   bearer token                   the ANTHROPIC_* naming -- see
    ANTHROPIC_MODEL        e.g. DeepSeek-V4-Pro           modules/api.py's extract_text)
    SUPABASE_URL           only needed for --auto-sync
    SUPABASE_SERVICE_ROLE_KEY  the SERVICE ROLE key, not the publishable/anon one: RLS is on
                           with no write policies, so an anon key silently writes nothing.

OPTIONAL TUNING (sensible defaults if unset):
    RESET_MAX_TOKENS            14000  (raised from 8192: Phase 9's real average output is
                                        ~7769 tokens, which was truncating at the old ceiling)
    RESET_PHASE11_MAX_TOKENS    16000
    RESET_REQUEST_TIMEOUT_SECS  900
    RESET_PHASE_SLEEP_SECS      60     gap between phases of one project
    RESET_PROJECT_SLEEP_SECS    300    gap between projects
    RESET_MAX_RETRIES           3      transport-level retries of the same request
    RESET_MAX_REPAIR_ATTEMPTS   2      corrective regenerations when output fails its spec
    RESET_DISABLE_REPAIR        set to 1 to turn the self-repair loop off entirely

USAGE
    python3 reset/run_deepseek_reset.py --audit
        What's already on disk and what's wrong with it, per phase. No API calls, no
        credentials needed, writes nothing. Start here.

    python3 reset/run_deepseek_reset.py --commit --phases-limit 10 --parallel 2
        The real run over the whole queue.

    python3 reset/run_deepseek_reset.py --commit --phases-limit 10 \\
        --project Cosmos --redo-phases 2,3
        Regenerate only the named phases of one project; everything else is loaded from disk
        at no API cost.

    python3 reset/run_deepseek_reset.py --dry-run
        Exercise the control flow with no API calls at all.
"""
import sys
from pathlib import Path

# reset/ on sys.path so `modules` resolves whether this is run as `python3
# reset/run_deepseek_reset.py` from the repo root or from inside reset/ itself.
sys.path.insert(0, str(Path(__file__).resolve().parent))

from modules.cli import main  # noqa: E402

if __name__ == "__main__":
    main()
