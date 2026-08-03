#!/usr/bin/env bash
# CIF Deep-Reset entrypoint — research every project via DeepSeek, then ingest + sync.
#
#   ./reset/run_reset.sh                 # full run (all empty/half projects), then run.sh build+sync
#   ./reset/run_reset.sh --only Aptos    # single project
#   ./reset/run_reset.sh --shard 0/4     # this worker handles 1/4 of the list (parallel)
#
# Credentials + tunables come from the environment (see reset/.env.example). If a
# reset/.env file exists it is sourced automatically so cron/systemd need no inline vars.
set -uo pipefail
cd "$(dirname "$0")/.."                     # repo root

if [ -f reset/.env ]; then
  set -a; . reset/.env; set +a
fi

: "${ANTHROPIC_BASE_URL:?set ANTHROPIC_BASE_URL (see reset/.env.example)}"
: "${ANTHROPIC_AUTH_TOKEN:?set ANTHROPIC_AUTH_TOKEN}"
: "${ANTHROPIC_MODEL:?set ANTHROPIC_MODEL}"

PY="${PYTHON:-python3}"
exec "$PY" reset/deep_reset.py "$@"
