# Lessons — failure classes this project has already paid for

## What this file is

The repo is the memory; a session is a worker that reads it and forgets. That works for *data*
but not for *judgement* — every session re-derives how to think about this codebase, and so
re-makes the same mistakes. This file is the judgement layer: each entry is a failure that
actually happened here, what it cost, and the rule it produced.

**Read this before changing pipeline code or a data contract.** Not as background — as a
checklist. Most entries below happened *twice* before being written down.

**Add to it when a mistake costs more than ten minutes.** One entry, in the same shape: what
broke, the cost, the rule. An entry with no rule is a war story and does not belong here. An
entry whose rule is "be careful" does not belong here either — the rule has to be something a
future session can check itself against mechanically.

---

## L1 — A skip must be as loud as a failure

**Happened four separate times**, each costing hours:

| symptom | what was really happening |
|---|---|
| `ingest: ⏭️ dossier exists` | phases regenerated, dossier never rebuilt, extractors reading stale text |
| `poc/behavior.json` missing a project | the chain ran, reported success, wrote nothing |
| Phase 11 "done", `qa.json` unchanged | `run_project` only finalised at `--phases-limit 10` |
| Phase 11 complete but unparseable | response cut off by `max_tokens`, `finish_reason` never read |

Every one reported success. That is what made them expensive: a loud error gets fixed in
minutes, a silent no-op gets diagnosed after someone notices missing data days later.

**Rule.** Any code path that decides *not* to do the work must say so in the log, with the
reason. If a function can return "nothing happened" and "everything worked" through the same
value, that is the bug — change the signature.

---

## L2 — Never iterate a `set` where output order matters

**Happened twice**, both times producing output that changed between runs of the same command
on the same input:

- `cli._classify` picked a project's source directory from `{data_project, tmp_test}`. Aptos
  existed in both, so consecutive audits reported "phases 2,3,9,10 broken" and "phase 9
  broken" — the verdict depended on `PYTHONHASHSEED`.
- `extract_behavior.DECISION_PATTERN_SECTIONS` was a set, iterated to concatenate five
  sections. Every `./run.sh build` produced a different `poc/behavior.json` with identical
  content in shuffled order — a spurious 80-line diff and a Supabase column rewritten for
  nothing, on every single run.

**Rule.** A `set` is for membership tests. The moment its contents are iterated into output —
a filename, a list, a report — use a tuple or list in the order you actually mean. Both bugs
were a one-character fix and neither was found by reading the code; they were found by running
the same command twice and diffing.

---

## L3 — Something added today cannot invalidate work finished yesterday

Phase 12 was added when 29 dossiers already existed without it. Twice in one hour it broke
everything:

- `tools/ingest.py`: adding `airdrop` to `PHASE_KEYS` would have made every existing project
  "incomplete: missing phase(s) airdrop" and hard-failed `./run.sh ingest`. Caught before
  landing, by asking what the change does to files already on disk.
- `validate.diagnose_project`: the same phase was made optional in ingest but not here, so all
  27 completed projects turned `broken(12)`, which emptied `phase11_todo`, which made the
  driver report "nothing to do" and skip the whole queue. **Not** caught before landing.

**Rule.** When adding a required element to a contract, first answer: what happens to the
records that already exist? If the answer is "they become invalid", the element is optional
(`OPTIONAL_PHASE_KEYS`) — and then grep for *every* place that enumerates the contract, because
there is always more than one.

---

## L4 — The prompt and the parser are one contract; verify them against each other

`reset/phase_11_conflict.txt` told the model to write `Research Quality:` while
`extract_qa.DIM_BLOCK_RE` required `Research Quality (25%)`. Arbitrum's run happened to deviate
from the template and produce the parseable form, and the regex had been written against that
output. So the only Phase 11 anyone had ever parsed was the one that *ignored* the
instructions, and Aave — which followed them exactly — produced an unreadable score.

Worse, the self-repair loop then spent two full regenerations per project (~16 minutes) trying
to correct output toward a format the prompt never asked for. **A repair loop aimed at the
wrong target cannot converge no matter how many attempts it is given.**

**Rule.** When a prompt and an extractor describe the same structure, one of them is the source
of truth and the other must be verified against it — by running the parser over the prompt's
own template, not over one project's output. A parser written from a single sample encodes that
sample's accidents.

---

## L5 — Measure before diagnosing; a plausible cause is not a cause

Three wrong diagnoses in this project, each costing a cycle:

- Phase 9's 504s blamed on a ~58k-token prefill, inferred from Arbitrum's phase sizes —
  Arbitrum never went through that gateway. Real cause: non-streaming requests.
- Phase 11's failures blamed on `max_tokens`, then dismissed as *not* `max_tokens` because
  30,707 chars looked small — using an assumed 3.3 chars/token. Measured later at 2.95, from a
  cap hit at exactly 70,499 chars. It *was* `max_tokens`.
- Connection aborts blamed on raising `max_tokens` to 24000. A 10-second probe showed 8000,
  16000, 24000 and 32000 all accepted — and that a one-word completion was taking 62 seconds.
  The cause was congestion, visible only because the probe measured something.

**Rule.** Before changing anything, produce a number that distinguishes the hypotheses. A
10-second probe beats an 8-minute regeneration every time, and this project's slow backend makes
the ratio far worse than that. If a diagnosis rests on a constant you assumed rather than
measured, measure it first.

---

## L6 — A retry must change something

Blur's Phase 11 was truncated by the output limit, then retried twice at the identical limit,
truncating identically. Twenty-six minutes to re-prove what the first attempt established, and
the project was then abandoned.

**Rule.** Classify failures by what a retry can fix. Transient (network, congestion) → retry
unchanged with backoff. Capacity (request too big) → rotate provider, do not retry. Truncation
(answer too big) → retry with a larger budget, and skip the backoff, because nothing is
overloaded. A retry that changes no input is only correct for the first class.

---

## L7 — Verify behaviour on the target machine, not the commit hash

A fix was pushed and reported as delivered **four times** while the VPS was still running the
old code: `git pull` aborted on a dirty `poc/cif.json`, then again, then diverged and needed a
rebase. Each round produced a full failing run — hours — against code that had already been
fixed.

Reading `git log` did not catch it, because the log was read in the wrong place or the pull had
silently failed above it in the scrollback.

**Rule.** Confirm a fix arrived by checking the *behaviour that changed*, not the commit:

```bash
python3 -c "import sys;sys.path.insert(0,'reset');from modules import config;print(config.PHASE11_MAX_TOKENS)"
```

And: generated files (`poc/*.json`) are rebuildable, so they must never be the reason a pull
fails — `git checkout -- poc/` then pull.

---

## L8 — A stage does what its name says, and nothing more

Adding phase 12 to `config.PHASES` silently turned `--stages phase11` into "generate 11 and 12",
because a run with no `--phases-limit` covers every phase. Fourteen projects got an airdrop
report nobody had asked for. The output was good and none of it was wasted — but API budget was
spent on a decision no one made.

**Rule.** A named stage states its bounds explicitly rather than inheriting them from a global
list that someone else will extend later. `--phases-limit 11` in the phase11 stage is not
redundant; it is the stage's contract.

---

## L9 — Quality gates decide what is finished; file existence does not

"Phase 11 done" meant a file over 400 chars existed. A report saved with unresolved spec checks
counted as complete, the resume logic skipped it on every later run, and the project could never
recover — not even after the bug that caused the failure was fixed. Three projects sat in that
state until the definition was changed.

**Rule.** "Done" is "passes the same checks the database sync will run". Anything weaker creates
records that are permanently stuck: too finished to retry, too broken to use.

---

## L10 — Never run the pipeline while git is mid-operation

`git pull --rebase` stopped on a conflict in `poc/cif.json`. The rest of the pasted command
ran anyway, and the phase11 stage began regenerating Celestia against a working tree that was
neither the old commit nor the new one — half the files from each. `--redo-phases` had already
moved `11-conflict.docx` aside to `.bak`, so interrupting it left that project with **no Phase
11 at all**, recoverable only by knowing the `.bak` was there.

The pipeline cannot detect this on its own: it reads whatever files are on disk, and a
conflicted tree looks like a normal tree to `open()`.

**Rule.** Any script that reads the repo as its input state checks for `rebase-merge`,
`rebase-apply`, `MERGE_HEAD` and `CHERRY_PICK_HEAD` in `$(git rev-parse --git-dir)` and
refuses to start. Related: a command that pulls and then acts on the result must not be
pasted as one block, because the shell runs line 2 whether or not line 1 succeeded.


---

## L11 — A list that filters is not the same as a list that orders

`sync_supabase.ORDER` was written as "insertion sequence, for foreign keys". It is also the
inclusion filter: the sync loops over `[t for t in ORDER if t in targets]`, so a table present
in `TABLES` and `BUILDERS` but absent from `ORDER` gets built, counted in `--dry-run`, printed
as a row count — and never posted. The four `airdrop_*` tables were one edit away from exactly
that, and `--dry-run` would have shown 339 rows either way.

**Rule.** When one list serves two purposes, the second purpose needs its own assertion. Here
that is four lines: `set(targets) - set(ORDER)` must be empty or the run dies. An omission from
a list like this is always a mistake and never a deliberate choice, so it can be fatal rather
than a warning.

---

## L12 — Ask sources for what they contain, not for what you wish they contained

Phase 12's `METRIK RETENSI` asked every project for the share of recipients who sold within
7 days and the share still holding at 90 days. Across 13 completed airdrops that produced **44
of 66 rows reading "Tidak ditemukan"** and exactly 3 rows containing a percentage. The data is
not missing by accident: it requires per-address on-chain tracking of a specific recipient set,
which no article, blog or public dashboard publishes.

The fix was not a better prompt for the same question. It was a **different question with the
same meaning**: price at claim vs +30 / +90 days, which CoinGecko has daily history for on
nearly every listed token. A recipient who held either gained or lost, and four numbers say
which — without a cohort analysis existing anywhere.

Worth noting what made this expensive: each unanswerable field still costs a full research pass
and looks like a research-quality problem, so the natural response is to sharpen the prompt and
run it again.

**Rule.** Before adding a field to a research prompt, name the source that would contain it and
check one project by hand. If a field comes back empty on the first three projects, the next
change is to the *question*, not to the wording — and record the dead end in the prompt itself
(Phase 12's `GAP YANG DIKETAHUI` tells the model not to spend effort there) so the next session
does not re-discover it.

## Related

- `CLAUDE.md` — the session bootstrap; its "Acquisition readiness" section is what these rules
  ultimately serve
- `reset/README.md` — the self-repair loop these lessons mostly came out of
- `docs/Protocol/SessionProtocol.md` — session flow
