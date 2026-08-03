#!/usr/bin/env bash
# Run N Deep-Reset workers in parallel over disjoint shards of the project list.
# Each worker: --no-pipeline (skip build/sync); the wrapper runs build+sync ONCE at the end.
#   ./reset/deploy/parallel.sh 4
set -uo pipefail
cd "$(dirname "$0")/../.."
N="${1:-4}"
pids=()
for i in $(seq 0 $((N-1))); do
  ./reset/run_reset.sh --shard "$i/$N" --no-pipeline & pids+=($!)
done
for pid in "${pids[@]}"; do wait "$pid"; done
echo "all $N workers done — running ingest + sync once"
bash run.sh build
bash run.sh sync
