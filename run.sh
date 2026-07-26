#!/usr/bin/env bash
# CIF pipeline runner — one command does everything, deterministically, no LLM.
#
#   ./run.sh          ingest new reports (anti-duplicate) -> build JSON -> backtest
#   ./run.sh build    only rebuild JSON + backtest (no ingest)
#   ./run.sh ingest   only ingest (no build)
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
ingest_status=0

run_ingest() {
  "$PY" tools/ingest.py --no-build
  ingest_status=$?
  if [ "$ingest_status" -ne 0 ]; then
    echo "⚠ ingest reported one or more data_project verification failures (see log above) —" \
         "continuing with whatever ingested successfully; ./run.sh will exit non-zero at the end."
  fi
}

case "$cmd" in
  ingest)
    run_ingest
    ;;
  build)
    "$PY" tools/build_json.py
    "$PY" tools/backtest.py || true
    ;;
  all)
    run_ingest                           # anti-duplicate ingest of all inbox folders + data_project/
    "$PY" tools/build_json.py            # export projects/patterns/sentiment + bundled cif.json
    "$PY" tools/backtest.py || true      # scorecard (non-zero exit on real failure; run continues)
    ;;
  *)
    echo "usage: ./run.sh [all|ingest|build]"; exit 2
    ;;
esac
echo "✓ done — outputs in poc/ (cif.json, data.js, *.json)"
exit "$ingest_status"
