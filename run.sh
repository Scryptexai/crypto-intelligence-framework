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
# Already-ingested projects are skipped, so re-running only processes newly added files.
set -euo pipefail
cd "$(dirname "$0")"
PY="${PYTHON:-python3}"
cmd="${1:-all}"

case "$cmd" in
  ingest)
    "$PY" tools/ingest.py --no-build
    ;;
  build)
    "$PY" tools/build_json.py
    "$PY" tools/backtest.py || true
    ;;
  all)
    "$PY" tools/ingest.py --no-build     # anti-duplicate ingest of all three inbox folders
    "$PY" tools/build_json.py            # export projects/patterns/sentiment + bundled cif.json
    "$PY" tools/backtest.py || true      # scorecard (non-zero exit on real failure; run continues)
    ;;
  *)
    echo "usage: ./run.sh [all|ingest|build]"; exit 2
    ;;
esac
echo "✓ done — outputs in poc/ (cif.json, data.js, *.json)"
