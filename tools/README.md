# tools/ — Ingest support tooling

Deterministic helpers for the **Ingest-Deep** runbook (`docs/Protocol/Role-Ingest-Deep.md`).
No LLM, no API, no network. **Quality-preserving:** these scripts never write a dossier — the
knowledge synthesis (source → causal dossier) stays human/LLM reasoning. They only industrialise
the two mechanical steps around it: **extraction** and **audit**.

**Setup:** `pip install -r requirements.txt` (repo root) — everything here is Python stdlib except
`.pdf` phase-file extraction, which needs `pypdf` (+ optional `cffi` backend). `.docx` needs nothing
extra.

This directory is infrastructure, not a layer of the knowledge model — it does not hold project
data (`examples/`, `tracking/`), documentation (`docs/`), or raw sources (`doc_backup/`).

## `extract.py` — source → clean markdown (runbook step 1)

```
python tools/extract.py doc_backup/deep/<Project>_<YYYY-MM>_gemini.docx -o /tmp/<project>.md
python tools/extract.py <report>.pdf -o /tmp/<project>.md      # pypdf; needs `cffi` for some PDFs
```

- `.docx`: walks the body in document order; **reconstructs Word tables row-by-row**
  (`<w:tbl>/<w:tr>/<w:tc>` → `Label: Value` bullets) so no cell is scrambled. A flat text sweep
  loses column↔row association — this is the bug it avoids for legacy (pre-contract) sources.
- `.pdf`: `pypdf.extract_text()`, wrapped lines rejoined.
- Both: strips citation chips, normalises numbered section titles to `## N Title`.

New sources authored under the **Input Formatting Contract** (`docs/Protocol/Deep-Research-Brief.md`)
carry no tables at all, so extraction is trivially lossless — the table logic is for older docs.

## `reconcile.py` — fidelity audit stamp (run after writing the dossier)

```
python tools/reconcile.py doc_backup/deep/<Project>_<YYYY-MM>_gemini.md examples/CaseStudies/<Project>.md
```

Reports which **key figures** (currency, %, unit-suffixed magnitudes, large integers) in the source
are not represented in the finished dossier. **Unit-aware** (`juta`=1e6, `miliar/mrd`=1e9, …) and
matches on normalised numeric value within tolerance, so `$145 juta` ↔ `145,000,000` and a faithful
rounding (`$72,248,571 → $72,25 juta`) both count as covered.

It is a **heuristic for human review**, not a correctness proof: it flags candidates to double-check
and **cannot** verify a value is attached to the correct label — that judgement stays with the curator.
A clean report is the per-ingest fidelity evidence retained for the later dataset audit.

## `ingest.py` — batch auto-file raw docx/pdf → CIF artifacts (no LLM)

Deterministic; the reasoning already lives in the source report, this only transforms+files it.
Four inbox-routed types (`deep`, `batch`, `sentiment`, `phased`) plus the hardened `data_project`
pipeline below. See the file's own docstring and `--help` for the routing rules.

### `data_project/<project>/` — hardened per-project 11-phase assembler

The successor to the `phased` mode's `doc_backup/inbox/phased/<Project>/` convention, built after a
real incident: a phase file named `03-historical.docx` was silently dropped from a dossier assembly
because the old matcher tested phase keys as a loose substring of the filename, and `"history"` is
not a substring of `"historical"` (see `doc_backup/inbox/phased/LayerZero/PROMPTS-LOG.md`). The failure
was silent — the run still reported `✅ ok`, just with one phase missing from the dossier.

`data_project` replaces substring matching with a **strict, hard-failing contract**:

```
data_project/<project>/NN-<phasekey>.docx   e.g. data_project/layerzero/03-history.docx
```

- `NN` — any 1–2 digit ordinal (cosmetic; assembly order is always the fixed dependency order, not
  filename order).
- `<phasekey>` — must be an **exact** match (not substring) to one of the 11 keys: `foundation`,
  `entity`, `history`, `technology`, `financial`, `token`, `ecosystem`, `market`, `behavioral`,
  `knowledge`, `conflict`.
- Any filename that doesn't match the pattern, uses an unknown key, or collides with another file on
  the same key → the whole project **raises and writes nothing** (no partial/misleading dossier).
  A missing phase also raises unless `--allow-partial` is passed explicitly.

**Content-level verification** (`validate_phase_content()`), on top of the filename contract — a
correct filename proves nothing about whether the *content* is real, complete, or belongs to this
project. Runs on every file before anything is written or archived:
- content shorter than 400 chars → broken/empty extraction.
- no `PROJECT: <Name>` header, or the header names a different project than the folder → likely
  misfiled/wrong-project content.
- zero `(HIGH)`/`(MEDIUM)`/`(LOW)`/`(TIDAK ADA KONFLIK)` Evidence Level tags anywhere → the exact
  "empty citations" failure mode that took 2–3 rejected drafts each to catch by hand in LayerZero
  Phase 3/4/6 before this check existed.
- the `[sumber tidak dapat diverifikasi ulang]` fallback phrase used as often or more than real
  Evidence Level tags → blanket fallback overuse instead of genuine per-fact citation (Phase 3
  attempt-2's failure mode).
- two files in the same project with identical extracted content (whitespace-normalised hash) →
  likely the same file saved under two phase names by mistake.

Any failure → **raises and writes nothing** for that file's project, listing every file and every
reason found (not just the first). Override with `--allow-unverified` if a human has reviewed the
flagged file and it's a false positive — not recommended as a default habit.

```
python tools/ingest.py --type data_project --input data_project/layerzero
python tools/ingest.py                                   # also scans data_project/ by default
python tools/ingest.py --type data_project --allow-partial --input data_project/arbitrum
python tools/ingest.py --type data_project --allow-unverified --input data_project/arbitrum
```

The process exits non-zero if any `data_project` folder fails validation, so it's safe to gate on in
a script — **`run.sh` already does this correctly**: a failed project is logged and skipped (nothing
written for it), `build_json.py`/`backtest.py` still run against whatever *did* ingest successfully,
and only `run.sh`'s own final exit code carries the failure signal (don't let a shell wrapper's
`set -e` swallow that distinction and abort the whole pipeline on one bad project — see `run.sh`'s
`run_ingest()`). The older `phased` mode (fuzzy matching, soft warnings, no content verification)
still works unchanged for LayerZero's own folder (`doc_backup/inbox/phased/LayerZero/`, which happens
to already satisfy the `data_project` filename contract too — verified by running it through
`process_data_project()` directly). New projects should use `data_project/<project>/`.

## `sync_supabase.py` — push `poc/*.json` to Intelligence Workspace's Postgres tables

```
export SUPABASE_URL="https://<ref>.supabase.co"
export SUPABASE_SERVICE_ROLE_KEY="..."
python tools/sync_supabase.py               # or: ./run.sh sync
python tools/sync_supabase.py --dry-run     # preview rows, no network call, no env vars needed
```

**Rewritten 2026-08-01.** This script originally targeted a `cif_`-prefixed schema designed
independently in this repo. That schema was superseded once the frontend's *actual* repo
(`github.com/scryptexai/intelligence-workspace` — not the earlier `scryptexai/cif` upload,
which turned out to be stale, uncommitted work never pushed) was inspected directly: it ships
a complete Drizzle schema (`src/db/schema.ts`) and a resilient DB-backed data layer
(`src/db/dataService.ts`) already querying plain-named tables. That schema is now the source
of truth — this script upserts into it directly via Supabase's REST API (stdlib only, no
`requests`/`supabase-py` dependency):

`projects`, `entities`, `knowledge_items`, `evidence_items` (separate table, not a jsonb
column — one row per citation), `qa_dimensions`, `qa_phases`, `behavior_profiles` — plus the
unrelated `cif_patterns`/`cif_backtests`/`cif_decision_events` (CIF's own pattern-library
concern, no naming collision, untouched by the schema swap).

Applied to the shared Supabase project (`airdropos-pro`) via the
`align_to_intelligence_workspace_drizzle_schema` migration, which also drops the earlier
`cif_projects`/`cif_entities`/`cif_knowledge`/`cif_relationships`/`cif_events`/`cif_conflicts`/
`cif_notes`/`cif_views` tables it supersedes (all had 0–2 rows, pure scaffolding from the same
day, nothing real lost).

Never run as part of `all`/`build` — explicit opt-in only, since it writes to a shared
production database. `relationships`/`events`/`conflicts`/`notes`/`saved_views`/`users` have
no row builder yet — no extractor produces that data (see `extract_entities.py`'s "known gap"
note on Relationships; Conflicts/Events extractors are not yet built at all).

### Database security posture

One write path, everything else read-only. This script holds the `service_role` key (env only,
never a tracked file); every client-facing table has RLS on and grants `SELECT` to `anon` and
`authenticated` and nothing more. `notes`/`saved_views`/`users` belong to the frontend and are
deliberately RLS-on-with-no-policy, which means closed — the advisor reports those three as INFO
and that is the intended state, not a backlog item.

Run `get_advisors(type="security")` after any schema change. Cleared so far:

- **2026-08-11** — `rls_auto_enable()`, the event-trigger function that turns RLS on for each new
  table in `public`, was `SECURITY DEFINER` and reachable by `anon`/`authenticated` through
  `/rest/v1/rpc/`. `EXECUTE` revoked from `anon`, `authenticated` and `public`. Nothing
  legitimate called it: Postgres does not check `EXECUTE` when firing a trigger, so the privilege
  only ever governed direct REST calls. Verified after the revoke by creating a table inside a
  transaction — RLS was still enabled automatically — and by `has_function_privilege`, which now
  reads false/false/true for anon/authenticated/service_role.

## `extract_decision_events.py` — Behavioral Intelligence phase → structured Decision Events

```
python tools/extract_decision_events.py examples/CaseStudies/LayerZero.md   # or: ./run.sh build
```

Decision Event is this framework's actual unit of analysis (`CLAUDE.md`), but until 2026-07-27 it
only existed as prose — nothing parsed it into structured data. Deterministic regex extraction
(no LLM) of a dossier's Behavioral Intelligence phase (plus any addenda logged later under Open
Questions, prefixed `- [behavioral]` — see LayerZero.md's Open Questions section for why that
addendum exists), recognizing **two** Phase 9 prompt shapes
(`docs/Protocol/Phased-Research-Prompts.md` Track A/B vs. Track C — they capture genuinely
different things, not just a reformatting of the same fields):

- Track A/B: `Decision Event: <date> — <title>` blocks →
  `{date, title, motivation, constraint, pressure, tradeoff, alternatives, expectation_vs_actual,
  reactions: {8 POV}, grounding, open_threads}`
- Track C (DeepSeek methodology): `Keputusan: <title> (<date>)` blocks, bullet-prefixed fields →
  `{date, title, trigger, evidence, decision, immediate_result, long_term_impact,
  supporting_dataset}`. No per-stakeholder reactions exist in this prompt shape — `reactions`
  stays `{}` rather than being guessed at.

Every output event carries the full union of both shapes' keys (unpopulated ones are `null`/`{}`),
so `poc/decision_events.json` has one stable schema regardless of which track produced a given
event. Wired into `run.sh build`/`all` — runs over every file in `examples/CaseStudies/`
automatically (dossiers without a Behavioral Intelligence phase just parse to 0 events). Output:
`poc/decision_events.json`, keyed by project name.

## `extract_entities.py` — Entity Intelligence phase → structured Entities

```
python tools/extract_entities.py examples/CaseStudies/LayerZero.md   # or: ./run.sh build
```

Built 2026-08-01 to feed the Intelligence Workspace product's `Entity` contract
(`scryptexai/intelligence-workspace`'s `src/lib/types/entity.ts`, table `entities`). Deterministic
regex extraction of a dossier's Entity Intelligence phase, recognizing both Format v3 tracks:

- Track A/B: one packed paragraph — `Entity: <Name> (<HIGH|MEDIUM|LOW>) Type: <Type>
  Relationship: <prose> Period: <period> Exposure Type: <exposure> Evidence: <sources>`
- Track C (DeepSeek methodology): one field per line, blocks separated by a `---` rule, no
  confidence tag after the name.

`type` is normalised from the dossier's free-text vocabulary (`Organization`, `Protocol (DeFi)`,
`Research Lab`, `Media / Research Lab`, ...) to Intelligence Workspace's fixed `EntityType` enum;
anything with no confident mapping stays `null` rather than being force-fit into the nearest wrong
bucket. `status` (Active/Dormant/Contested/Unknown) and `founded` are always `null` — the dossier
phase never captures a lifecycle status or founding date, so guessing one would be fabrication.
`period`/`exposureType`/`evidence`/`evidenceLevel` (no dedicated column in the `Entity` contract)
are kept in the `metadata` catch-all rather than dropped.

**Known gap, by design, not yet solved:** this tool only emits `Entity` rows, never `Relationship`
rows (entity-to-entity graph edges). The Entity Intelligence phase describes each entity's relation
*to the project*, not entity-to-entity triples — synthesizing a `source`/`target`/`type` edge from
that prose would mean asserting a relationship the text doesn't actually state.

Wired into `run.sh build`/`all`, same pattern as `extract_decision_events.py`. Output:
`poc/entities.json`, keyed by project name.

## `extract_knowledge.py` / `extract_behavior.py` / `extract_qa.py` — Track C only

Built 2026-08-01 alongside `extract_entities.py`, for Intelligence Workspace's `KnowledgeItem`,
`BehaviorProfile`, and `QAReport` contracts. **Track C (DeepSeek methodology) dossiers only** —
Track A/B's Knowledge Extraction/Behavioral Intelligence/Conflict Resolution phases (LayerZero)
never produce these as discrete labeled fields, and the maintainer explicitly rejected deriving
them from unlabeled prose as too error-prone ("lebih baik bangun dari nol data field-nya karena
kalau diderivasi rentan error salah baca", 2026-08-01). Track C's Phase 9/10/11 prompts do produce
genuinely itemized, labeled sections (verified against `examples/CaseStudies/Arbitrum.md`), so
these three tools parse those literally — no synthesis, no inferred confidence/status where the
dossier doesn't state one. A Track A/B dossier parses to 0 items/an empty profile/no report and is
silently skipped, not force-fit.

- `extract_knowledge.py` — Core Insights / Strategic Principles / Success Factors / Failure
  Factors / Decision Framework / Reusable Playbook / Anti-patterns → `KnowledgeItem[]`.
  `confidence` only populated where an explicit `Confidence: High|Medium|Low` tag exists (mapped
  90/60/30). The raw Evidence-field text is kept separately as `evidenceText` (not merged into
  `description`) — `tools/sync_supabase.py`'s `evidence_rows()` turns it into one row in the real
  schema's dedicated `evidence_items` table, `weight` left at that column's own default (1) rather
  than inventing a per-citation grade. `dependencies` is a literal `EV-\d+` grep of the item's
  citations. Output: `poc/knowledge.json`.
- `extract_behavior.py` — Strategic Objectives / {Technical,Financial,Ecosystem,Governance,
  Recurring} Decision Pattern / Risk Response Pattern / Strategic Trade-offs sections → the four
  `BehaviorProfile` arrays, extracting the dossier's own item titles verbatim. Output: `poc/behavior.json`.
- `extract_qa.py` — the "CIF SCORE CALCULATION — v3.0" section's six weighted dimensions (Research/
  Consistency/Evidence/Coverage/Conflict/Knowledge) → `QAReport.dimensions`, plus the "COVERAGE
  REPORT" per-phase table → `QAReport.phases` (`status`/`owner` are fixed system defaults, not
  per-phase source data — see the tool's docstring). Uses the *detailed calculation's* CIF Score,
  not the earlier Manifest summary — the two can genuinely disagree (Arbitrum: 88.2 vs 81.6), and
  the detailed one is the documented-authoritative one (see Phased-Research-Prompts.md's "Known
  gaps" section). Output: `poc/qa.json`.

All three wired into `run.sh build`/`all` via `run_extract_iw_fields`. `tools/sync_supabase.py`
upserts `qa.json` into the real schema's `qa_dimensions`/`qa_phases` tables (one row per
dimension/phase per project, plus `projects.cif_score`), `behavior.json` into `behavior_profiles`
(one row per project, PK = `project_slug`), and `knowledge.json` into `knowledge_items` (+
`evidence_items` for the raw Evidence text — see `extract_knowledge.py`'s note above).

### Phase 12 — Airdrop Intelligence

`extract_airdrop.py` parses the Phase 12 section (`reset/phase_12_airdrop.txt`) into
`poc/airdrop.json`, which `sync_supabase.py` fans out across five tables. Nothing here is
computed: there is no success score and no cross-project comparison, because an airdrop
succeeds for the founder and fails for retail in the same month and collapsing that into one
number is the mistake the phase exists to prevent.

| Table | Grain | Notes |
|---|---|---|
| `airdrop_profiles` | one row per project, PK `project_slug` | status + the four PROSPEK fields |
| `airdrop_events` | one row per distribution wave | `id` is `<slug>-AD-001`; AD ids restart per project |
| `airdrop_pov_outcomes` | eight rows per project | `verdict` is one of five canonical values, `verdict_raw` keeps the model's own words |
| `airdrop_retention` | one row per metric line | TVL/volume, holders, active addresses, concentration, staking retention |
| `airdrop_price_points` | up to four rows per project | the post-distribution trajectory |

`airdrop_price_points` (created 2026-08-11) is the only typed table of the five: `usd numeric`,
`observed_on date`, `evidence` constrained to HIGH/MEDIUM/LOW, `point` constrained to
`at_claim`/`day_30`/`day_90`/`peak_12m` with a `seq` so a chart sorts without a CASE. The
siblings stay text because their reports genuinely contain ranges and qualifications
("2023-05 hingga 2023-11"); this one does not, because the prompt demands one figure and one
ISO date per line and the parser only fills the typed columns when it matched exactly that.
`usd` null with `raw` present means the report said `Tidak berlaku` — no listing, or a
continuous distribution with no single claim date.

The price block replaced the recipient-cohort questions Phase 12 used to ask ("what share sold
within 7 days"). Those returned nothing on 13 of 13 projects: it needs per-address on-chain
tracking that no public source publishes. Price at claim vs +30/+90 days answers the same
question from CoinGecko's daily history — see `docs/Protocol/Lessons.md` L12.
