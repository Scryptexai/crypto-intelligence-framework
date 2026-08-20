# CLAUDE.md — Session Bootstrap (read first, every session)

This file is loaded automatically at the start of every Claude Code session. It is the entry point
that lets any session — in any order, on any day — continue the work without losing context. **The repo
is the memory; the session is a worker that reads the repo, does one job, commits, and forgets.**

## What this repository is

**Crypto Intelligence Framework (CIF)** — a self-documenting *knowledge repository* (not source code)
that turns historical crypto research into a reasoning system: collect history → learn repeating
patterns → predict where new projects are heading, with a calibrated confidence.

Pipeline: `Research → Knowledge → Ontology → Patterns → Reasoning → Framework → Applications`.

**Core philosophy — Causal Intelligence, not a Knowledge Base.** The unit of analysis is not the *Project* —
it is the **Decision Event** (`docs/Ontology/DecisionEvent.md`): Context → Trigger → Decision → Alternatives →
Reason → Execution → Stakeholder Reactions (8 POV) → Short/Long-term Outcome. A project is dozens of these;
the reusable pattern is found *across decisions from unrelated projects*, not by comparing projects wholesale
(Ethereum/smart-contracts, Hyperliquid/on-chain-orderbook, Uniswap/AMM share a decision *shape*, not a sector).
Every Decision Event carries a **Context snapshot** (`docs/Ontology/Context.md` — industry/competitor/tech/
macro/hunter-population state *at that time*), because the same decision produces different outcomes in
different eras — never match a pattern across incompatible eras on mechanic-similarity alone. Record
**Observable** facts (`docs/Ontology/Metrics.md` etc.) separately from **Hidden** factors
(`docs/Ontology/Hidden.md`: motivation, constraint, trade-off) that actually explain them. Research is an
**investigator, not an analyst** — collect evidence and preserve disagreement; `docs/Reasoning/` draws the
causal conclusion, not the source report.

## The three layers (never mix them)

| Layer | Path | Contains | Rule |
|-------|------|----------|------|
| **Raw source** | `doc_backup/` | Original Gemini/research docs (input) | ✅ immutable archive; re-processable, never edited |
| **Containers** | `docs/` | Documentation only — structure, rules, field specs | ❌ never put project data / knowledge here |
| **Knowledge** | `examples/`, `tracking/` | Real curated project data (output) | ✅ all knowledge lives here, links back to `docs/` |

`docs/Taxonomy/` is the one exception that accumulates *vocabulary terms* (not project instances).
Every Ingest session archives its source in `doc_backup/` first, so a future re-architecture never needs re-research.

## Golden rules

1. **Write everything to the repo.** Anything not committed is lost when the session ends.
2. **Don't fabricate.** Every fact needs a source; record provenance (Deep Research / web) per artifact.
3. **Check the index before adding** a project — `examples/DatasetIndex.md` is the dedup guard and map.
4. **`docs/` stays documentation-only.** Knowledge goes to `examples/` (history) or `tracking/` (live).
5. **Commit + push** to the working branch when a unit of work is done. Update the index in the same commit.
6. **Read `docs/Protocol/Lessons.md` before changing pipeline code or a data contract.** Nine failure
   classes this project has already paid for, each with the rule it produced. Most of them happened
   *twice* before being written down. Add an entry whenever a mistake costs more than ten minutes.

## Acquisition readiness — what "done" means here

**This dataset is built to be sold**, to a VC or entity via Acquire.com or a similar B2B marketplace
(maintainer, 2026-08-10). That is not a distant business detail; it changes the acceptance criteria for
every change made in this repo, because the buyer inherits the repo *and* the Supabase project exactly
as they stand.

Four consequences, in the order they bite:

**1. Transferable without its authors.** A new owner must be able to run the pipeline from the README
alone. Any step that only works because someone remembers a detail is a defect. Every constant that was
derived from measurement carries the measurement in a comment — that is why the code reads the way it
does, and it should stay that way.

**2. No dev debris — in the repo or in the database.** Scratch folders, abandoned tables, test rows,
duplicate schemas. Two known examples: `reset/tmp_test/` (stale scaffolds that already corrupted an
audit — see Lessons L2) and the `cif_patterns` / `cif_backtests` / `cif_decision_events` tables, which
belong to the older AirdropOS schema in a *different* Supabase project and are not part of this one.
**Cleanup happens after the dataset is complete, not during** — the exception being anything already
known to be irrelevant, which can go now.

**3. Column and table names are part of the product.** A buyer reads the schema before the data. Every
column must mean exactly what its name says, be typed correctly, and be reachable from a documented
contract in `tools/extract_*.py`. A new table needs its columns agreed before it is created, not
patched afterwards — the frontend team reads these too.

**4. Security is the top constraint, and writes are where it lives.** The database is written by exactly
one path: `tools/sync_supabase.py`, holding a service-role key that exists only in the environment.
Everything else is read-only. Concretely:

- **Never** put a credential in a tracked file, a commit message, a log line, or a chat message. It has
  already happened three times here (`.env` committed twice, an API key pasted into chat once) and each
  one requires rotating the key — the repo's history is part of what gets handed over.
- **RLS on, policies explicit.** Client-facing tables grant `SELECT` to `anon` and nothing more. A table
  with RLS enabled and no policy is closed, which is the correct default for anything the frontend owns
  (`users`, `saved_views`, `notes`).
- **No `SECURITY DEFINER` function reachable by `anon` or `authenticated`** unless it is deliberately
  public — it bypasses RLS by design.
- Run `get_advisors(type="security")` after any schema change; it catches exactly these.
- The write path stays deterministic and reviewable. Never put an LLM between the extractors and the
  database.

## How the knowledge is meant to be used

The audience is **AI reasoning**, not human readers. Every fact must be *Reusable Knowledge* — carry its
**why / impact / lesson / industry link**, not just the bare fact. Deep reports follow the **22-section
research brief** in `docs/Protocol/Deep-Research-Brief.md`; ingest against it losslessly. Projects have
**types** (innovation archetype, narrative), and **success/failure is per-POV** (Founder, VC, Retail,
Community, Developer, Institution, Validator, Builder) — never a single binary verdict. Tag important
conclusions with an **evidence level** (HIGH/MED/LOW).

## Curation tiers (quality × scale)

- **Deep dossier** (like `examples/CaseStudies/LayerZero.md`) — full causal history for *anchor* projects,
  produced via the Format v3 phased pipeline (`docs/Protocol/Phased-Research-Prompts.md`, 11 sequential
  phases). ~1 per session. Highest quality; the analog library that prediction reasons from.
- **Batch summary** (like `examples/Pioneer/*`) — one profile per project for breadth. ~10–15 per session.
- **Tracking** (`tracking/<project>/`) — living dossier for projects being actively worked/followed.

**Data hygiene:** never leave a project in two tiers at once (Deep supersedes Summary — remove the redundant
Summary in the same session). Never delete a curated dossier or a `doc_backup/` raw source without an
explicit maintainer decision on scope.

**2026-07-26 dataset reset:** the maintainer judged the old single-mega-prompt Deep Research process (used
for the dataset's first 12 Deep dossiers + 13 Summaries) insufficiently rigorous compared to the Format v3
phased pipeline proven out on LayerZero, and moved all pre-reset projects to `_archive_pre_v3/` (not
deleted — `git mv`, fully restorable). LayerZero is currently the only active project. This **supersedes**
the old "V1 → V2 Upgrade Queue (upgrade before delete)" policy that used to be referenced here — see
`examples/DatasetIndex.md`'s reset note for the full rationale and restore instructions. Going forward,
every new project must go through the Format v3 phased pipeline, not the older single-prompt `deep`/`batch`
ingest modes (which still exist mechanically in `tools/ingest.py` but are no longer the sanctioned process).

Target scale (~1000 projects) ≈ ~50 deep + ~950 summary ≈ **~150 sessions**. State persists in git, so
per-session cost stays flat regardless of dataset size.

## Repo boundary — this repo is DATA INTEGRATION only

**The frontend and backend live in a separate Next.js repo, owned by a different team.** This repo does not
build UI. Its output is data: the research pipeline, the extraction contracts, `poc/*.json`, and the Supabase
tables the other repo reads. Work stops at the database.

| Lane | Owner | Scope |
|------|-------|-------|
| **Data integration** | **this repo** | `reset/` pipeline, `tools/` extractors + sync, `data_project/`, `examples/`, `poc/*.json`, Supabase schema and contents |
| Frontend + backend | separate Next.js repo | every user-facing surface, API serving layer, auth/RBAC/SSO, rendering |

Consequences worth internalising, because they change what "done" means here:

- A surface being unbuilt is **not this repo's problem**. A surface being *unbuildable because the data isn't
  there* **is** — e.g. the `relationships` table is empty, so an entity-graph screen would render nothing.
- The frontend reads real data as of 2026-08-08, so **thin data is immediately visible as a thin product**.
  A dossier that exists but was never extracted into `poc/*.json` is invisible to users (this actually
  happened to Friend.tech).
- Don't clone, read, or plan work in the frontend repo. If something there needs to change, say so and hand
  it over.

**Product decisions still live here as documentation:** `docs/Project/ApplicationBlueprint.md` is the locked
plan for positioning, the three-layer trust architecture, the identification flow, and build-phase
sequencing — read it before changing anything that affects what the product can claim, and update it if a
decision changes. `docs/Project/EnterpriseRoadmap.md` sequences longer-term modules and tags each one
`[data]` or `[frontend]`.

## Roles — pick one per session, then read its runbook

Tell me the role at the start of the session (or I infer it from your request). Each has a runbook:

| Role | When | Runbook |
|------|------|---------|
| **Ingest-Deep** | You give a deep research report (one project) | `docs/Protocol/Role-Ingest-Deep.md` |
| **Ingest-Batch** | You give a summary batch (many projects) | `docs/Protocol/Role-Ingest-Batch.md` |
| **Tracking** | Follow a project you are working on | `docs/Protocol/Role-Tracking.md` |
| **Analysis** | Predict the direction of a new project | `docs/Protocol/Role-Analysis.md` |

Session flow is defined in `docs/Protocol/SessionProtocol.md`. Start there if unsure.

## Working branch

Develop on `claude/crypto-intelligence-framework-jegycz`; the maintainer also mirrors to `main`.
