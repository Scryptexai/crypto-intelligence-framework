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

This is a development/testing credential — rotate it once end-to-end testing is done. The sync step
(`./run.sh sync`, triggered automatically after each project) needs its own separate `SUPABASE_URL` /
`SUPABASE_SERVICE_ROLE_KEY` pair (see `tools/sync_supabase.py`'s docstring) — if those aren't set, the sync
step fails loudly but non-fatally; data stays ingested locally under `data_project/` and `examples/
CaseStudies/` until you export those too and re-run `./run.sh sync` by hand.

## Running it

```bash
# Smoke test first -- no API key needed, just exercises the file/loop logic:
python3 reset/run_deepseek_reset.py --dry-run --projects-limit 1 --phases-limit 2

# Smoke test against the real API -- one project, one phase, to confirm the endpoint actually works:
python3 reset/run_deepseek_reset.py --project Aptos --phases-limit 1

# The real run -- every project in projects.txt, all 11 phases each, unattended:
python3 reset/run_deepseek_reset.py
```

Run it in the background (`nohup ... &`, `tmux`, or similar) for the real run — it's designed to take hours
(60s between phases, 300s between projects, times 11 phases times however many projects are queued) and
survive being interrupted: it's resumable. If it's stopped and restarted, it checks
`data_project/<Project>/NN-<phasekey>.docx` for each phase before calling the API again — anything already
there (and long enough to be real content, not a stub) is loaded back into the running conversation as
context instead of being regenerated, so restarting never wastes API calls redoing finished work.

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
- **`./run.sh` + `./run.sh sync` run after every project**, not after every phase — `tools/ingest.py`'s
  `data_project` mode only assembles a project once all 11 of its phase files are present (it hard-fails a
  single incomplete project without aborting the rest of the run), so triggering it mid-project would just be
  wasted work.
