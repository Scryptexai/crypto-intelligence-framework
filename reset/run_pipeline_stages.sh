#!/usr/bin/env bash
# run_pipeline_stages.sh — the whole remaining repair programme as one unattended command.
#
# Runs the maintainer's agreed order, start to finish, without supervision:
#
#   1. repair    every project with broken phases -> targeted --redo-phases regeneration
#   2. publish   git commit + push, rebuild poc/*.json, sync to Supabase
#   3. phase11   Phase 11 (Validation & QA) for projects already clear on phases 1-10
#   4. publish   commit + push + sync again, so the audits reach the database too
#
# Designed for systemd (see reset/systemd/). One invocation attempts the entire programme;
# it is expected to take a day or more on the shared gateway, and it is safe to kill and
# restart at any point.
#
#   ./reset/run_pipeline_stages.sh              # everything, for real
#   ./reset/run_pipeline_stages.sh --dry-run    # print the plan, make no API calls, change nothing
#   ./reset/run_pipeline_stages.sh --stages repair          # just stage 1
#   ./reset/run_pipeline_stages.sh --stages phase11,publish # skip repair
#
# ---------------------------------------------------------------------------------------
# WHY THERE IS NO STATE FILE, AND NO HARDCODED PROJECT LIST
#
# Every stage recomputes what it has to do from `--audit-json`, which reads the actual files
# on disk. That makes the disk the state, which has three consequences worth knowing:
#
#   * Restart is free. A project repaired before the process died is no longer "broken", so
#     the next run simply doesn't see it. Nothing is redone and nothing is skipped.
#   * A frozen list can't go stale. Writing today's "group B" into this file would be wrong
#     by tomorrow -- the manual group-A loop is still repairing projects as this is written,
#     and a run that takes a day will finish against a different set than it started with.
#   * The order is a consequence, not a configuration. Phase 11 only ever considers projects
#     the repair stage has already made clean, because that is what `phase11_todo` means.
#
# The one thing disk state cannot express is "this project has failed repeatedly, stop paying
# for it" -- that is what stage_attempts.log is for.
# ---------------------------------------------------------------------------------------
set -uo pipefail

cd "$(dirname "$0")/.."
ROOT="$PWD"
PY="${PYTHON:-python3}"
RESET="$ROOT/reset"
ATTEMPTS_LOG="$RESET/stage_attempts.log"
LOCK_FILE="$RESET/.pipeline_stages.lock"

# A project that fails its repair this many times across separate runs is left alone and
# reported instead of retried forever. A format the model gets wrong three times is a prompt
# bug in reset/phase_NN_*.txt, not something more attempts will fix -- and on a 24h timer,
# retrying it forever is a standing token bill for a known-broken prompt.
MAX_ATTEMPTS="${PIPELINE_MAX_ATTEMPTS:-3}"

# Stop a stage after this many projects fail BACK TO BACK. One failure is a project problem;
# several in a row is the gateway, and every further project will fail the same way after
# burning its full retry budget first.
#
# Measured 2026-08-09, the day this was added: a one-word completion took 26s, 62s, 15s and
# 56s on four consecutive probes -- the backend was queueing, not generating, and Phase 11
# calls were dying with "Software caused connection abort" after five minutes. Left alone,
# the stage would have spent four hours proving that 25 times.
MAX_CONSECUTIVE_FAILURES="${PIPELINE_MAX_CONSECUTIVE_FAILURES:-3}"

DRY_RUN=0
STAGES="repair,publish,phase11,publish"
GIT_BRANCH="${PIPELINE_GIT_BRANCH:-claude/crypto-intelligence-framework-jegycz}"
# Off by default: an unattended job that pushes on its own is a surprise the first time it
# happens. reset/systemd/cif-pipeline.service turns it on explicitly.
DO_PUSH="${PIPELINE_PUSH:-0}"

while [ $# -gt 0 ]; do
  case "$1" in
    --dry-run) DRY_RUN=1 ;;
    --stages)  STAGES="${2:?--stages needs a value}"; shift ;;
    --branch)  GIT_BRANCH="${2:?--branch needs a value}"; shift ;;
    --push)    DO_PUSH=1 ;;
    --no-push) DO_PUSH=0 ;;
    -h|--help) sed -n '2,40p' "$0"; exit 0 ;;
    *) echo "unknown argument: $1" >&2; exit 2 ;;
  esac
  shift
done

say() { printf '[%s] %s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$*"; }

# ---------------------------------------------------------------------------------------
# Single instance. Two copies of this running against the same data_project/ would have them
# overwriting each other's phase files mid-generation. This also guards against the 24h timer
# firing while the previous day's run is still going, which on a 1-2 day programme is the
# normal case rather than the exception.
# ---------------------------------------------------------------------------------------
if command -v flock >/dev/null 2>&1; then
  exec 9>"$LOCK_FILE"
  if ! flock -n 9; then
    say "another run already holds $LOCK_FILE -- exiting without doing anything."
    exit 0
  fi
fi

if [ "$DRY_RUN" = 1 ]; then
  say "DRY RUN -- no API calls, no git writes, no database writes."
fi

# ---------------------------------------------------------------------------------------
# Audit helpers. `audit_field` pulls one list out of --audit-json; `audit_broken` emits
# "<project>\t<phases>" lines. Both re-read disk on every call, deliberately.
# ---------------------------------------------------------------------------------------
audit_json() {
  "$PY" reset/run_deepseek_reset.py --audit-json 2>/dev/null
}

audit_field() {
  audit_json | "$PY" -c '
import json, sys
print("\n".join(json.load(sys.stdin)[sys.argv[1]]))' "$1"
}

audit_broken() {
  audit_json | "$PY" -c '
import json, sys
for b in json.load(sys.stdin)["broken"]:
    print(b["project"], ",".join(str(p) for p in b["phases"]), sep="\t")'
}

attempts_for() {
  [ -f "$ATTEMPTS_LOG" ] || { echo 0; return; }
  # grep -c prints "0" AND exits 1 when nothing matches, so the count has to be captured
  # first and the exit status swallowed separately -- `grep -c ... || echo 0` would print
  # "0" twice and the caller's arithmetic test would then fail outright.
  local n
  n="$(grep -Fc "	$1	" "$ATTEMPTS_LOG" 2>/dev/null)"
  echo "${n:-0}"
}

record_attempt() {
  printf '%s\t%s\t%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$1" "$2" >> "$ATTEMPTS_LOG"
}

consecutive_failures=0

# Runs one project and updates the consecutive-failure counter. Returns 1 when the caller
# should stop the whole stage because the backend is evidently unavailable.
run_one_project() {
  local label="$1"; shift
  if "$PY" reset/run_deepseek_reset.py "$@"; then
    consecutive_failures=0
    return 0
  fi
  consecutive_failures=$((consecutive_failures + 1))
  say "  ✗ $label failed ($consecutive_failures in a row)"
  if [ "$consecutive_failures" -ge "$MAX_CONSECUTIVE_FAILURES" ]; then
    say "  ⚠ $consecutive_failures failures back to back -- treating the gateway as unavailable"
    say "    and stopping this stage. Nothing is lost: every finished project stays on disk and"
    say "    the next run recomputes what is left. Try again when the gateway recovers; a quick"
    say "    check is whether a one-word completion comes back in a couple of seconds."
    return 1
  fi
  return 0
}

# ---------------------------------------------------------------------------------------
# Stage 1 — repair
#
# One targeted regeneration per broken project. --redo-phases sets only the named phases
# aside (as .bak) and regenerates them; every other phase loads from disk as context at no
# API cost, and reset/modules/phases.py keeps whichever of the two versions scores better, so
# a worse regeneration cannot destroy good data.
#
# --phases-limit 10 keeps Phase 11 out of this stage on purpose: repairing phase 9 and then
# immediately auditing the project would spend the audit on data the next repair may replace.
# ---------------------------------------------------------------------------------------
stage_repair() {
  local todo count=0 skipped=0
  todo="$(audit_broken)"
  if [ -z "$todo" ]; then
    say "stage repair: nothing broken -- skipping."
    return 0
  fi

  say "stage repair: $(printf '%s\n' "$todo" | wc -l) project(s) need phases regenerated."
  while IFS=$'\t' read -r project phases; do
    [ -n "$project" ] || continue
    local tries
    tries="$(attempts_for "$project")"
    if [ "$tries" -ge "$MAX_ATTEMPTS" ]; then
      say "  SKIP $project (phases $phases) -- already attempted $tries times. Fix the prompt in reset/phase_NN_*.txt, then clear its lines from $(basename "$ATTEMPTS_LOG")."
      skipped=$((skipped + 1))
      continue
    fi
    say "  repair $project -- phases $phases (attempt $((tries + 1))/$MAX_ATTEMPTS)"
    if [ "$DRY_RUN" = 1 ]; then
      say "    [dry-run] would run: --commit --phases-limit 10 --project '$project' --redo-phases $phases"
      continue
    fi
    record_attempt "$project" "$phases"
    run_one_project "$project" --commit --phases-limit 10 --auto-sync \
      --project "$project" --redo-phases "$phases" || break
    count=$((count + 1))
  done <<< "$todo"

  say "stage repair: done -- $count attempted, $skipped skipped."
}

# ---------------------------------------------------------------------------------------
# Stage 2 — publish
#
# `./run.sh build` rather than `./run.sh all`: the per-project chain inside the reset pipeline
# has already ingested each repaired project (with --force, so the dossier is genuinely
# rebuilt). This re-derives every poc/*.json from the full CaseStudies/ roster, which is what
# catches a project whose own chain failed partway.
# ---------------------------------------------------------------------------------------
stage_publish() {
  say "stage publish: rebuilding poc/*.json from examples/CaseStudies/"
  if [ "$DRY_RUN" = 1 ]; then
    say "  [dry-run] would run: ./run.sh build, git commit/push, ./run.sh sync"
    return 0
  fi

  ./run.sh build || say "  ⚠ ./run.sh build reported a problem -- continuing, see the log above."

  if [ -n "$(git status --porcelain)" ]; then
    git add -A
    git commit -q -m "Pipeline run $(date -u +%Y-%m-%d): repaired phases, rebuilt poc/*.json" \
      && say "  committed."
    if [ "$DO_PUSH" = 1 ]; then
      # HEAD:<branch> rather than a checkout, and no -u: an unattended job must not switch the
      # working branch out from under whoever is logged into the box, and must not rewire the
      # checked-out branch's upstream as a side effect of a nightly push.
      local pushed=0 delay=2
      for _ in 1 2 3 4; do
        if git push origin "HEAD:$GIT_BRANCH"; then pushed=1; break; fi
        say "  push failed -- retrying in ${delay}s"
        sleep "$delay"; delay=$((delay * 2))
      done
      [ "$pushed" = 1 ] && say "  pushed to $GIT_BRANCH." \
        || say "  ⚠ push failed after 4 attempts -- the work is committed locally, push it by hand."
    else
      say "  not pushing (PIPELINE_PUSH=0). Commit is local."
    fi
  else
    say "  nothing to commit."
  fi

  if [ -n "${SUPABASE_URL:-}" ] && [ -n "${SUPABASE_SERVICE_ROLE_KEY:-}" ]; then
    ./run.sh sync || say "  ⚠ sync reported a problem -- data is safe in poc/*.json, see the log."
  else
    say "  SUPABASE_URL / SUPABASE_SERVICE_ROLE_KEY not set -- skipping sync."
  fi
}

# ---------------------------------------------------------------------------------------
# Stage 3 — phase 11
#
# Only for projects `--audit-json` reports as phase11_todo: clear on phases 1-10, no real
# 11-conflict.docx yet. That is the maintainer's rule encoded literally -- a project that has
# never been started, or is still broken, is not audited, because a QA report over phases
# that do not exist is a confident description of nothing.
#
# No --phases-limit, so the run covers all 11: phases 1-10 resume from disk as free context
# and only Phase 11 (four sequential stages) is generated. The run then finalises, which
# rebuilds the dossier so extract_qa.py can actually see the new audit -- without that,
# poc/qa.json would stay at one project no matter how many audits were generated.
# ---------------------------------------------------------------------------------------
stage_phase11() {
  local todo bad work count=0
  todo="$(audit_field phase11_todo)"
  # Projects whose 11-conflict.docx exists but does NOT pass its spec checks. Without this
  # they were finished forever: the resume logic sees a long-enough file and skips it, so a
  # project that saved an unparseable audit could never recover, not even after the bug that
  # caused it was fixed. --redo-phases 11 sets the old file aside (as .bak) and regenerates;
  # phases.run_phase keeps whichever version scores better, so a worse retry cannot lose the
  # report that is already there.
  bad="$(audit_json | "$PY" -c '
import json, sys
for e in json.load(sys.stdin).get("phase11_bad") or []:
    print(e["project"], ",".join(e["checks"]), sep="\t")')"

  if [ -z "$todo" ] && [ -z "$bad" ]; then
    say "stage phase11: every project clear on phases 1-10 has a parseable audit -- skipping."
    return 0
  fi

  [ -n "$todo" ] && say "stage phase11: $(printf '%s\n' "$todo" | wc -l) project(s) need a first audit."
  [ -n "$bad" ] && say "stage phase11: $(printf '%s\n' "$bad" | wc -l) project(s) have an audit that fails its checks -- regenerating."

  while IFS= read -r project; do
    [ -n "$project" ] || continue
    say "  phase 11 for $project"
    if [ "$DRY_RUN" = 1 ]; then
      say "    [dry-run] would run: --commit --phases-limit 11 --auto-sync --project '$project'"
      continue
    fi
    run_one_project "$project" --commit --phases-limit 11 --auto-sync --project "$project" || break
    count=$((count + 1))
  done <<< "$todo"

  while IFS=$'\t' read -r project checks; do
    [ -n "$project" ] || continue
    local tries
    tries="$(attempts_for "$project")"
    if [ "$tries" -ge "$MAX_ATTEMPTS" ]; then
      say "  SKIP $project (phase 11: $checks) -- already attempted $tries times. Fix the prompt or the check, then clear its lines from $(basename "$ATTEMPTS_LOG")."
      continue
    fi
    say "  phase 11 REDO for $project (failing: $checks, attempt $((tries + 1))/$MAX_ATTEMPTS)"
    if [ "$DRY_RUN" = 1 ]; then
      say "    [dry-run] would run: --commit --phases-limit 11 --auto-sync --project '$project' --redo-phases 11"
      continue
    fi
    record_attempt "$project" "phase11:$checks"
    run_one_project "$project" --commit --phases-limit 11 --auto-sync --project "$project" \
        --redo-phases 11 || break
    count=$((count + 1))
  done <<< "$bad"

  say "stage phase11: done -- $count project(s) attempted."
}

# ---------------------------------------------------------------------------------------
# Stage 4 — phase 12 (Airdrop Intelligence)
#
# Separate from phase11 on purpose. Adding phase 12 to config.PHASES quietly turned
# `--stages phase11` into "generate 11 AND 12", because a run with no --phases-limit covers
# every phase -- Blur got an unrequested airdrop report that way on 2026-08-10. The phase11
# stage now passes --phases-limit 11, and asking for phase 12 is a decision you make here.
#
# Candidates are projects whose Phase 11 PARSES, not merely clean ones: the airdrop phase
# reasons over Phases 1-11 in one conversation, so running it against an audit that is about
# to be regenerated wastes both generations.
# ---------------------------------------------------------------------------------------
stage_phase12() {
  local todo bad count=0
  todo="$(audit_field phase12_todo)"
  bad="$(audit_json | "$PY" -c '
import json, sys
for e in json.load(sys.stdin).get("phase12_bad") or []:
    print(e["project"], ",".join(e["checks"]), sep="\t")')"

  if [ -z "$todo" ] && [ -z "$bad" ]; then
    say "stage phase12: every project with a parseable audit already has an airdrop report -- skipping."
    return 0
  fi

  [ -n "$todo" ] && say "stage phase12: $(printf '%s\n' "$todo" | wc -l) project(s) need a first airdrop report."
  [ -n "$bad" ] && say "stage phase12: $(printf '%s\n' "$bad" | wc -l) project(s) have one that fails its checks -- regenerating."

  while IFS= read -r project; do
    [ -n "$project" ] || continue
    say "  phase 12 for $project"
    if [ "$DRY_RUN" = 1 ]; then
      say "    [dry-run] would run: --commit --auto-sync --project '$project'"
      continue
    fi
    run_one_project "$project" --commit --auto-sync --project "$project" || break
    count=$((count + 1))
  done <<< "$todo"

  while IFS=$'\t' read -r project checks; do
    [ -n "$project" ] || continue
    local tries
    tries="$(attempts_for "$project")"
    if [ "$tries" -ge "$MAX_ATTEMPTS" ]; then
      say "  SKIP $project (phase 12: $checks) -- already attempted $tries times."
      continue
    fi
    say "  phase 12 REDO for $project (failing: $checks, attempt $((tries + 1))/$MAX_ATTEMPTS)"
    if [ "$DRY_RUN" = 1 ]; then
      say "    [dry-run] would run: --commit --auto-sync --project '$project' --redo-phases 12"
      continue
    fi
    record_attempt "$project" "phase12:$checks"
    run_one_project "$project" --commit --auto-sync --project "$project" --redo-phases 12 || break
    count=$((count + 1))
  done <<< "$bad"

  say "stage phase12: done -- $count project(s) attempted."
}

# ---------------------------------------------------------------------------------------

summarise() {
  audit_json | "$PY" -c '
import json, sys
d = json.load(sys.stdin)
print("    %s state: %d clean, %d broken, %d not started, %d awaiting phase 11" % (
    sys.argv[1], len(d["clean"]), len(d["broken"]), len(d["not_started"]),
    len(d["phase11_todo"])))
if d["broken"] and sys.argv[1] == "ending":
    print("    still broken: " + ", ".join(
        "%s(%s)" % (b["project"], ",".join(str(p) for p in b["phases"]))
        for b in d["broken"]))' "$1"
}

say "=== pipeline stages: $STAGES ==="
summarise starting

IFS=',' read -r -a stage_list <<< "$STAGES"
for stage in "${stage_list[@]}"; do
  case "$stage" in
    repair)  stage_repair ;;
    publish) stage_publish ;;
    phase11) stage_phase11 ;;
    phase12) stage_phase12 ;;
    *) echo "unknown stage: $stage (want repair|publish|phase11|phase12)" >&2; exit 2 ;;
  esac
done

say "=== all stages finished ==="
summarise ending
