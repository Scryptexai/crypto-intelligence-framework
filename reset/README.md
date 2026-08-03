# CIF Deep-Reset

Automated **DeepSeek research pipeline** that fills `data_project/<Project>/` with the
11-phase CIF dossier for every project, then ingests + syncs it to Supabase — the
programmatic version of the manual "Track C — DeepSeek Methodology" flow described in
`docs/Protocol/Phased-Research-Prompts.md`.

## What it does

For each project in `reset/projects.txt`, sequentially phase 1 → 11:

1. **Phase 1 (Foundation)** — the model researches the project (official site, docs,
   explorers, trusted sources) and fills the foundation template incl. a concise
   `Description`. The project name is injected here (and only here).
2. **Phase 2 … 11** — the phase prompt is sent together with **the output of all prior
   phases as context** (read back from disk, so a resumed run keeps context). Output of
   each phase is written to `data_project/<Project>/NN-<key>.docx`.

Pacing (maintainer spec): **60s between phases, 5 min between projects**, looping until
every project has data. Then it runs `./run.sh build` (ingest → JSON extract) and
`./run.sh sync` (push to Supabase).

Phase → file map (the `tools/ingest.py` `PHASE_KEYS` contract):

| # | key | file |
|---|-----|------|
| 1 | foundation | `01-foundation.docx` |
| 2 | entity | `02-entity.docx` |
| 3 | history | `03-history.docx` |
| 4 | technology | `04-technology.docx` |
| 5 | financial | `05-financial.docx` |
| 6 | token | `06-token.docx` |
| 7 | ecosystem | `07-ecosystem.docx` |
| 8 | market | `08-market.docx` |
| 9 | behavioral | `09-behavioral.docx` |
| 10 | knowledge | `10-knowledge.docx` |
| 11 | conflict (Validation & QA) | `11-conflict.docx` |

> `.docx` files here are plain UTF-8 text with a `.docx` extension — exactly what
> `tools/extract.py:extract_docx()` already reads. No Word/Office needed.

## Layout

```
reset/
├── phases/               # 11 phase prompt .txt files (the DeepSeek prompts)
│   ├── 01-foundation.txt … 11-conflict.txt
├── projects.txt          # one project per line ('#'-comments ignored)
├── config.py             # env-driven config + paths + PHASE_ORDER
├── deep_client.py        # stdlib Anthropic-compatible client (DeepSeek)
├── deep_reset.py         # the orchestrator (loop, context, delays, resume, shard)
├── run_reset.sh          # entrypoint (sources reset/.env, runs orchestrator)
├── deploy/               # cron + systemd timer + parallel launcher
├── .env.example          # credentials & tunables
└── state/                # progress.json + reset.log (gitignored)
```

## Setup

```bash
cp reset/.env.example reset/.env
# edit reset/.env: ANTHROPIC_* creds + SUPABASE_* sync target
```

Only the Python standard library is required (runs on a bare VPS). `./run.sh sync`
uses `SUPABASE_URL` + `SUPABASE_SERVICE_ROLE_KEY`.

## Run

```bash
# Dry run — print the plan, no API calls, no writes
python3 reset/deep_reset.py --dry-run

# Single project (real)
./reset/run_reset.sh --only Aptos

# Everything (empty + half-filled projects), then ingest + sync
./reset/run_reset.sh

# Testing helpers
python3 reset/deep_reset.py --only Aptos --max-phases 2 --no-delay --no-pipeline
```

Useful flags: `--overwrite` (regenerate existing), `--limit N`, `--no-delay`,
`--no-pipeline`, `--shard i/n` (parallel workers).

## Parallel (faster full reset)

```bash
# 4 workers over disjoint shards, then build + sync ONCE
./reset/deploy/parallel.sh 4
```

## Run once every 24h on a VPS

**cron:**
```bash
cp /path/to/repo /opt/crypto-intelligence-framework
crontab reset/deploy/cif-reset.cron   # 02:00 daily
```

**systemd timer:**
```bash
sudo cp reset/deploy/cif-reset.service reset/deploy/cif-reset.timer /etc/systemd/system/
sudo systemctl enable --now cif-reset.timer
```

## Resume & safety

- Completed phases are recorded in `state/progress.json` and skipped on re-run.
- A phase file is only written on a full, long-enough (`RESET_MIN_PHASE_CHARS`) answer —
  no partial/corrupt files.
- If the model omits a header, a `PROJECT: <name>` line is prepended so `tools/ingest.py`
  validation still passes.
- Filled projects are skipped by default (`RESET_SKIP_FILLED=true`); half-filled projects
  resume from their first missing phase.
