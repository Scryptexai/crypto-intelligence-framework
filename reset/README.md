# reset/ — automated Track C (DeepSeek methodology) research pipeline

Automates the 11-phase Track C prompt sequence (`docs/Protocol/Phased-Research-Prompts.md`'s "Fixed vs. the
original DeepSeek run" section — the prompt set actually used to research Arbitrum,
`data_project/Arbitrum/`) against an OpenAI-compatible `/v1/chat/completions` endpoint, one project at a
time, so a long queue of projects can run unattended instead of being pasted into a chat UI by hand one
phase at a time.

## Layout (modular since 2026-08-08)

`run_deepseek_reset.py` is now a thin entrypoint; all logic lives in `modules/`, one file per
responsibility, each importing only from the ones above it:

| module | owns |
|---|---|
| `config.py` | paths, constants, tunables, locks, credential + queue loading |
| `logs.py` | console + `failures.log` / `needs_review.log` / `repairs.log` |
| `api.py` | HTTP client for the gateway; transport-level retry only |
| `prompts.py` | loading/assembling prompt text (no network, no validation) |
| `specs.py` | **what "correct output" means per phase, and how to ask for it again** |
| `validate.py` | project-level quality gate (`verify_10_phases`, `diagnose_project`) |
| `repair.py` | **the self-healing loop: spec check → corrective retry** |
| `phases.py` | generating one phase (all 11 as a single prompt; staged fallbacks for 9 and 11) |
| `pipeline.py` | promote → ingest → build → extract → optional Supabase sync |
| `runner.py` | per-project orchestration + sequential/parallel queue |
| `cli.py` | argparse and entrypoint wiring |

Where to change what: a new/changed output format → `specs.py` (add a `Check` + its repair
hint); prompt wording → `phase_NN_*.txt`, not code; a new pipeline stage → `pipeline.py`; a
new flag → `cli.py`; retry/backoff/timeouts → `config.py`.

## Self-repair (the loop that fixes its own output)

Every phase is checked the moment it arrives against the **real downstream parsers** —
`tools/extract_*.py` and `tools/ingest.py`'s own `validate_phase_content`, not an
approximation. If a check fails, the output is sent back with a precise corrective
instruction (exact literal labels + a worked example) and regenerated, up to
`RESET_MAX_REPAIR_ATTEMPTS` times (default 2).

Details that matter:

- **The repair exchange is not left in the conversation.** Later phases see only the final
  corrected output. Keeping the rejected draft and the correction in context would teach the
  model that malformed-then-fixed is acceptable, and would grow every later request by the
  size of a whole failed phase.
- **A repair that doesn't improve things stops the loop.** A model that ignored an explicit
  format correction once won't comply on attempt three — that's a prompt bug to fix in
  `phase_NN_*.txt`, and `repairs.log` is what makes it visible. A check that repairs on nearly
  every project is being paid for with a wasted generation each time.
- **A phase that still fails is saved anyway**, with its failures recorded. Real research
  isn't thrown away over a format problem; the project-level gate is what stops it reaching
  the database.

Checks currently enforced: `no_junk` (leaked `<tool_call>` syntax, "I'll search for…"
narration with no findings, meta-commentary, decorative banners — the failure mode that
produced Berachain/EigenLayer/Cosmos), `min_length`, `ingest_contract` (PROJECT header +
citation density), plus per-phase `entities_parse` / `events_parse` / `decisions_parse` /
`behavior_sections` / `knowledge_parse`, and for Phase 11 `qa_parse` (extract_qa finds a CIF Score
with dimensions) + `no_md_headers` (a `## ` line inside the report silently truncates it).

Set `RESET_DISABLE_REPAIR=1` to turn the loop off.

## Diagnosing and fixing existing data

```bash
# what's on disk and what's wrong with it — no API calls, no credentials, writes nothing
python3 reset/run_deepseek_reset.py --audit

# regenerate ONLY the named phases of one project; every other phase loads from disk free
python3 reset/run_deepseek_reset.py --commit --phases-limit 10 --project Cosmos --redo-phases 2,3
```

`--audit` separates three cases deliberately: projects that fully pass, projects with real
content but specific broken phases (each printed with the exact `--redo-phases` command to
fix it), and projects never started (all phases empty — the normal queue picks these up, no
decision needed).

`--audit-json` prints the same classification as JSON for a script to consume, plus the split
`--audit` doesn't show: `phase11_todo` (clear on phases 1-10, no audit yet) vs `phase11_done`.

## Running the whole repair programme unattended

`run_pipeline_stages.sh` chains the stages the maintainer agreed, in order, in one command:

```bash
./reset/run_pipeline_stages.sh --dry-run     # print the exact plan; no API calls, no writes
./reset/run_pipeline_stages.sh               # the real thing (expect a day or more)
./reset/run_pipeline_stages.sh --stages phase11,publish
```

| stage | what it does |
|---|---|
| `repair` | every project `--audit-json` calls broken → targeted `--redo-phases` regeneration |
| `publish` | `./run.sh build`, `git commit`, `git push` (opt-in), `./run.sh sync` |
| `phase11` | Phase 11 for projects already clear on phases 1-10 (`phase11_todo`) |
| `publish` | again, so the audits reach `poc/qa.json` and the database |

**No state file and no hardcoded project list.** Every stage recomputes its work from disk, so
a run killed halfway doesn't redo what it already fixed, and a list can't go stale over a run
that spans days. The one thing disk state can't express — "this project has failed repeatedly,
stop paying for it" — is `reset/stage_attempts.log` plus `PIPELINE_MAX_ATTEMPTS` (default 3).

`reset/systemd/` has the unit + timer to run this on a VPS, and a README covering the four
things that will bite you (chief among them: `TimeoutStartSec=infinity`, without which systemd
kills the run after 90 seconds).

## Files

- `phase_01_foundation.txt` … `phase_10_knowledge.txt` — 10 of the 11 Track C phase prompts, extracted verbatim
  from `docs/Protocol/Phased-Research-Prompts.md` (only Phase 1's prompt has a light addition asking the model
  to look up the project's basic info/description before filling the template — everything else is unchanged).
  These are the *only* prompt set kept in that doc now; Track A (generic, context-window-limited) and Track B
  (condensed) were removed as superseded — see that doc's "How to use these" note, 2026-08-03.
- `phase_11_conflict.txt` — Phase 11 (Validation & QA), the **default** and only sanctioned path: one prompt,
  sent like every other phase. Extracted verbatim from `docs/Protocol/Phased-Research-Prompts.md` (the
  section's 683 lines) — and it is the prompt that actually produced `data_project/Arbitrum/11-conflict.docx`,
  the only Phase 11 `tools/extract_qa.py` has ever parsed (total=81.6, 6 dimensions, 7 phases). Verified on
  restoration that every section marker across the four stage files below also appears here.
- `phase_11a_audit.txt` / `phase_11b_audit.txt` / `phase_11c_audit.txt` / `phase_11d_scoring.txt` — the same
  Phase 11 split into four sequential calls. **Fallback only since 2026-08-09**, reached when streaming is off
  *and* no heavy-capable provider is configured (same gate as Phase 9's split). It was built for gateway 504s
  that turned out to be an artifact of non-streaming requests, and it carries a cost timing never accounted
  for: stage 11d is instructed to merge every earlier stage's findings, and a model restating prior findings
  rewords them — in a validation report a reworded finding is indistinguishable from a second real one, which
  is the one place an invented or double-counted item does the most damage, because the output reads
  authoritative. The four files also fixed a real, separate bug found while first building them: the original
  single `phase_11_conflict.txt` captured only ~15% of the real prompt (its extraction stopped partway,
  silently dropping Coverage Report, Cross-phase Consistency, Data Lineage, Dependency Graph, Conflict
  Register, Evidence Audit, Confidence Assessment, and CIF Score Calculation). The restored single file above
  is complete — that truncation is what made it look, for a while, as though splitting were the only option.
- `shared_format_rules.txt` — the doc's mandatory "ATURAN FORMAT" block (citations on every fact, Evidence
  Level tags, no fabrication, template-exactness, etc.) — the doc's own instructions say this gets appended
  to **every** phase prompt before sending, not just used once. `load_phase_prompt()` does this
  automatically for all 11 phases; don't send a `phase_NN_*.txt` file's content alone. (A version of this
  script that skipped this produced citation-free output that `tools/ingest.py` would hard-reject — verified
  live, 2026-08-03, see git history.)
- `projects.txt` — the project queue, one name per line, processed top to bottom. Append more any time.
- `run_deepseek_reset.py` — the pipeline. Read its module docstring for the full contract (env vars, retry/
  resume behavior, timing).
- `failures.log` — appended to (not overwritten) whenever a phase permanently fails after all retries; each
  line is `<timestamp>\t<project>\t<phase>\t<error>`.

## Credentials

**Never hardcode these anywhere, never commit them, never let them appear in a script's output.** Export them
in your shell before running:

```bash
export ANTHROPIC_BASE_URL="https://api.hcnsec.cn/"
export ANTHROPIC_AUTH_TOKEN="sk-..."
export ANTHROPIC_MODEL="DeepSeek-V4-Pro"
```

This is a development/testing credential — rotate it once end-to-end testing is done.

## Safe by default — test output never leaves reset/, and nothing auto-syncs

Every run writes to **`reset/tmp_test/<Project>/NN-<phasekey>.docx`** — never `data_project/` — unless you
pass **`--commit`**. And in *either* mode, this script **never runs `./run.sh` or `./run.sh sync` itself** —
assembling the dossier and pushing it to the live database are decisions you make after reading the output,
not an automatic side effect of an API call finishing. When you're ready, run those two commands yourself
from the repo root.

```bash
# Smoke test first -- no API key needed, just exercises the file/loop logic (writes to reset/tmp_test/):
python3 reset/run_deepseek_reset.py --dry-run --projects-limit 1 --phases-limit 2

# Real API call, one project, one phase -- confirms the endpoint works, output stays in reset/tmp_test/Aptos/:
python3 reset/run_deepseek_reset.py --project Aptos --phases-limit 1

# Read reset/tmp_test/Aptos/01-foundation.docx. Compare its structure against data_project/Arbitrum/
# 01-foundation.docx. Only once you trust the output quality:
python3 reset/run_deepseek_reset.py --project Aptos --commit

# The real run -- every project in projects.txt, all 11 phases each, unattended, writing to data_project/:
python3 reset/run_deepseek_reset.py --commit

# Same, but 4 projects processed concurrently instead of one at a time:
python3 reset/run_deepseek_reset.py --commit --parallel 4
```

Run the real (`--commit`) run in the background (`nohup ... &`, `tmux`, or similar) — sequentially it's
designed to take hours (60s between phases, 300s between projects, times 11 phases times however many
projects are queued); `--parallel N` divides that by roughly N since each project is an independent
conversation running in its own thread — raise it gradually and watch `reset/failures.log` for rate-limit
errors rather than jumping straight to a large number. Either way it survives being interrupted: it's
resumable. If it's stopped and restarted, it checks each phase's output file in the active output root
(`data_project/<Project>/NN-<phasekey>.docx` with `--commit`, `reset/tmp_test/<Project>/NN-<phasekey>.docx`
without it) before calling the API again — anything already there (and long enough to be real content, not
a stub) is loaded back into the running conversation as context instead of being regenerated, so restarting
never wastes API calls redoing finished work.

After a `--commit` run (or once you've committed the projects you've reviewed), from the repo root:

```bash
./run.sh          # assembles data_project/<Project>/ into examples/CaseStudies/<Project>.md, extracts fields
./run.sh sync     # pushes to Supabase -- needs its own SUPABASE_URL / SUPABASE_SERVICE_ROLE_KEY env vars
                   # (see tools/sync_supabase.py's docstring), separate from the ANTHROPIC_* ones above
```

## Design notes (why it works this way)

- **One continuous conversation per project**, not one-shot stateless calls — matches Track C's actual
  design ("run phases in one sitting, in the same chat, back to back", since DeepSeek's 1M-token window
  removes the reason Track A/B needed trimmed Context Packs). Every phase's prompt and response both go into
  a running `messages` list that's resent in full on each subsequent call.
- **`.docx` extension, plain text content** — matches how the real `data_project/Arbitrum/*.docx` files are
  actually saved (confirmed by reading them: they're UTF-8 text, not real OOXML containers).
  `tools/extract.py`'s `extract_docx()` already has a fallback for exactly this (`except zipfile.BadZipFile`),
  so no `.docx`-generation library is needed here.
- **A phase that fails all its retries stops that project, not the whole run** — later phases need the
  failed one's output as context, so fabricating a skip would poison everything after it. The script logs
  the failure and moves to the next project; re-running the script later resumes the stalled project exactly
  where it left off (see resumability above).
- **`run_deepseek_reset.py` never auto-runs `./run.sh` / `./run.sh sync`, in test or commit mode** — a real,
  cautionary example of why: an early version of this script did trigger them automatically, and a
  single-phase test run ended up scanning every other unrelated `data_project/` folder and attempting a
  database sync before anyone had looked at the new output's quality. Ingesting and syncing stay a separate,
  deliberate step.

  Two later additions opt back into that deliberately, and neither weakens the rule — both are gated behind a
  flag you have to type, and both only reach the database *after* a project has passed `verify_10_phases`
  and `ingest.py`'s own validator:

  - `--auto-sync` (with `--phases-limit 10`) syncs one project at a time, as it passes.
  - `run_pipeline_stages.sh` runs `./run.sh build` and `./run.sh sync` as its `publish` stage. That script's
    entire purpose is to be unattended, so "a human decides when to sync" is replaced by "the quality gate
    decides" — the same gate, just without the wait.
