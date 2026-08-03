#!/usr/bin/env bash
# CIF pipeline runner — one command does everything, deterministically, no LLM.
#
#   ./run.sh          ingest new reports (anti-duplicate) -> build JSON -> extract events -> backtest
#   ./run.sh build    only rebuild JSON + extract events + backtest (no ingest)
#   ./run.sh ingest   only ingest (no build)
#   ./run.sh sync     push poc/{projects,knowledge,evidence,entities,relationships,conflicts,qa,
#                     behavior,decision_events,patterns,benchmarks}.json to Supabase
#                     (tools/sync_supabase.py) -- explicit opt-in only, never runs as part of
#                     `all`/`build`; requires SUPABASE_URL + SUPABASE_SERVICE_ROLE_KEY env vars
#                     (see that file's docstring)
#
# Drop raw reports first:
#   doc_backup/inbox/deep/       <Project>_<YYYY-MM>_gemini.docx   -> examples/CaseStudies/
#   doc_backup/inbox/batch/      <Batch>_<YYYY-MM>_gemini.docx     -> examples/Pioneer/
#   doc_backup/inbox/sentiment/  <Project>_<YYYY-MM>_grok.docx     -> examples/Sentiment/
#   doc_backup/inbox/phased/<Project>/  N phase files (legacy Format v3 location, fuzzy matching)
#   data_project/<project>/      N phase files as NN-<phasekey>.docx (Format v3, hardened)  -> examples/CaseStudies/
# Already-ingested projects are skipped, so re-running only processes newly added files.
#
# Adaptive on bad data: tools/ingest.py verifies each data_project/<project>/ folder (filename
# contract, PROJECT-header match, citation presence, duplicate-content check -- see
# validate_phase_content() in tools/ingest.py) and HARD-FAILS that single project (writes nothing,
# logs exactly what's wrong) rather than silently producing an incomplete/wrong dossier. That
# per-project failure does NOT abort this script -- build/backtest still run against whatever DID
# ingest successfully -- but ./run.sh's own exit code stays non-zero so a wrapper/CI still sees that
# something needs attention. Check the ingest log above for which project and why.
set -uo pipefail
cd "$(dirname "$0")"
PY="${PYTHON:-python3}"
cmd="${1:-all}"
exit_status=0

run_ingest() {
  "$PY" tools/ingest.py --no-build
  exit_status=$?
  if [ "$exit_status" -ne 0 ]; then
    echo "⚠ ingest reported one or more data_project verification failures (see log above) —" \
         "continuing with whatever ingested successfully; ./run.sh will exit non-zero at the end."
  fi
}

_real_dossiers() {
  shopt -s nullglob
  local dossiers=(examples/CaseStudies/*.md)
  shopt -u nullglob
  for f in "${dossiers[@]}"; do
    case "$(basename "$f")" in
      README.md|*Analysis*|*Registry*) continue ;;
    esac
    echo "$f"
  done
}

run_extract_events() {
  # Decision Event is this framework's actual unit of analysis (CLAUDE.md) — pull
  # structured events out of every Deep dossier's Behavioral Intelligence phase.
  # Dossiers without that phase (older/Summary-tier files) simply parse to 0
  # events, so this is safe to run unconditionally over the whole CaseStudies/ dir.
  local real=()
  while IFS= read -r f; do real+=("$f"); done < <(_real_dossiers)
  if [ "${#real[@]}" -gt 0 ]; then
    "$PY" tools/extract_decision_events.py "${real[@]}"
  fi
}

run_extract_entities() {
  # Intelligence Workspace's Entity graph — pull structured entities out of every
  # Deep dossier's Entity Intelligence phase (see tools/extract_entities.py).
  local real=()
  while IFS= read -r f; do real+=("$f"); done < <(_real_dossiers)
  if [ "${#real[@]}" -gt 0 ]; then
    "$PY" tools/extract_entities.py "${real[@]}"
  fi
}

run_extract_conflicts() {
  # Intelligence Workspace's Conflict Center — pull the CONFLICT REGISTER out of every
  # Deep dossier's Validation & QA phase (see tools/extract_conflicts.py). Dossiers with
  # no register parse to 0 conflicts, so this is safe to run over the whole dir.
  local real=()
  while IFS= read -r f; do real+=("$f"); done < <(_real_dossiers)
  if [ "${#real[@]}" -gt 0 ]; then
    "$PY" tools/extract_conflicts.py "${real[@]}"
  fi
}

run_extract_relationships() {
  # Intelligence Workspace's Entity Graph edges — derive source/target/type from literal
  # co-mentions in poc/entities.json (see tools/extract_relationships.py). Must run AFTER
  # run_extract_entities so poc/entities.json exists.
  "$PY" tools/extract_relationships.py || true
}

run_extract_iw_fields() {
  # Intelligence Workspace's Knowledge/QA/Behavior contracts — Track C (DeepSeek
  # methodology) dossiers only; Track A/B dossiers parse to 0 items and are skipped
  # (see each tool's module docstring for why they don't approximate Track A/B).
  local real=()
  while IFS= read -r f; do real+=("$f"); done < <(_real_dossiers)
  if [ "${#real[@]}" -gt 0 ]; then
    "$PY" tools/extract_knowledge.py "${real[@]}"
    "$PY" tools/extract_behavior.py "${real[@]}"
    "$PY" tools/extract_qa.py "${real[@]}"
  fi
}

case "$cmd" in
  ingest)
    run_ingest
    ;;
  build)
    "$PY" tools/build_json.py
    run_extract_events
    run_extract_entities
    run_extract_iw_fields
    run_extract_conflicts
    run_extract_relationships
    "$PY" tools/backtest.py || true
    ;;
  sync)
    "$PY" tools/sync_supabase.py
    exit_status=$?
    ;;
  all)
    run_ingest                           # anti-duplicate ingest of all inbox folders + data_project/
    "$PY" tools/build_json.py            # export projects/patterns/sentiment + bundled cif.json
    run_extract_events                   # export poc/decision_events.json
    run_extract_entities                 # export poc/entities.json
    run_extract_iw_fields                # export poc/{knowledge,behavior,qa}.json (Track C only)
    run_extract_conflicts                # export poc/conflicts.json (Conflict Center)
    run_extract_relationships            # export poc/relationships.json (entity-graph edges)
    "$PY" tools/backtest.py || true      # scorecard (non-zero exit on real failure; run continues)
    ;;
  *)
    echo "usage: ./run.sh [all|ingest|build|sync]"; exit 2
    ;;
esac
echo "✓ done — outputs in poc/ (cif.json, data.js, *.json)"
exit "$exit_status"
