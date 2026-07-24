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

## How the knowledge is meant to be used

The audience is **AI reasoning**, not human readers. Every fact must be *Reusable Knowledge* — carry its
**why / impact / lesson / industry link**, not just the bare fact. Deep reports follow the **22-section
research brief** in `docs/Protocol/Deep-Research-Brief.md`; ingest against it losslessly. Projects have
**types** (innovation archetype, narrative), and **success/failure is per-POV** (Founder, VC, Retail,
Community, Developer, Institution, Validator, Builder) — never a single binary verdict. Tag important
conclusions with an **evidence level** (HIGH/MED/LOW).

## Curation tiers (quality × scale)

- **Deep dossier** (like `examples/CaseStudies/Ethereum.md`) — full causal history for *anchor* projects.
  ~1 per session. Highest quality; the analog library that prediction reasons from.
- **Batch summary** (like `examples/Pioneer/*`) — one profile per project for breadth. ~10–15 per session.
- **Tracking** (`tracking/<project>/`) — living dossier for projects being actively worked/followed.

**Data hygiene:** never leave a project in two tiers at once (Deep supersedes Summary — remove the redundant
Summary in the same session). Never delete a curated dossier or a `doc_backup/` raw source without an
explicit maintainer decision on scope — see `examples/DatasetIndex.md` § "V1 → V2 Upgrade Queue" for the
current policy: 11 Deep dossiers are still v1-format and are kept as-is until upgraded (Solana-style merge)
before any removal.

Target scale (~1000 projects) ≈ ~50 deep + ~950 summary ≈ **~150 sessions**. State persists in git, so
per-session cost stays flat regardless of dataset size.

## Application layer (product/UI, not knowledge)

Before building or changing anything user-facing (UI, trust/citation display, project-identification flow,
Supabase/AirdropOS bridge), read `docs/Project/ApplicationBlueprint.md` first — it is the locked plan for
positioning, the three-layer trust architecture, the hybrid project-identification flow, and the build-phase
sequencing. Don't re-derive these decisions from scratch; update that file if a decision changes.

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
