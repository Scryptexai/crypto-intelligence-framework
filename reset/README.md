# reset/ — automated Track C (DeepSeek methodology) research pipeline

Automates the 11-phase Track C prompt sequence (`docs/Protocol/Phased-Research-Prompts.md`'s "Fixed vs. the
original DeepSeek run" section — the prompt set actually used to research Arbitrum,
`data_project/Arbitrum/`) against an Anthropic-Messages-API-compatible endpoint, one project at a time, so a
long queue of projects can run unattended instead of being pasted into a chat UI by hand one phase at a time.

## Files

- `phase_01_foundation.txt` … `phase_11_conflict.txt` — the 11 Track C phase prompts, extracted verbatim from
  `docs/Protocol/Phased-Research-Prompts.md` (only Phase 1's prompt has a light addition asking the model to
  look up the project's basic info/description before filling the template — everything else is unchanged).
  These are the *only* prompt set kept in that doc now; Track A (generic, context-window-limited) and Track B
  (condensed) were removed as superseded — see that doc's "How to use these" note, 2026-08-03.
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
- **Never auto-runs `./run.sh` / `./run.sh sync`, in test or commit mode** — a real, cautionary example of
  why: an early version of this script did trigger them automatically, and a single-phase test run ended up
  scanning every other unrelated `data_project/` folder and attempting a database sync before anyone had
  looked at the new output's quality. Ingesting and syncing are always a separate, deliberate, manual step
  now.
