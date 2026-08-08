"""
reset.modules — the CIF reset pipeline, split by responsibility.

Load order / dependency direction (each layer only imports from the ones above it):

    config      paths, constants, tunables, locks, credential + queue loading
    logs        console + failures.log / needs_review.log / repairs.log
    api         HTTP client for the research gateway, transport-level retry only
    prompts     loading and assembling prompt text (no network, no validation)
    specs       what "correct output" means per phase + how to ask for it again
    validate    project-level quality gate (verify_10_phases, diagnose_project)
    repair      the self-healing generation loop (spec check -> corrective retry)
    phases      generating one phase, and the four-stage Phase 11
    pipeline    promote -> ingest -> build -> extract -> optional Supabase sync
    runner      per-project orchestration + the sequential/parallel queue
    cli         argparse and entrypoint wiring

Where to make a change:
  new/changed output format .... specs.py (add a Check + its repair hint)
  prompt wording ............... reset/phase_NN_*.txt (not code)
  a new pipeline stage ......... pipeline.py
  a new CLI flag ............... cli.py
  retry/backoff/timeouts ....... config.py
"""
