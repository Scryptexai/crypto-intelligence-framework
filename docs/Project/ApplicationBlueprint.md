# Application Blueprint — CIF as a Product

## Status

**Locked plan, pre-build.** This is the reference document for the `Framework → Applications` stage of the
pipeline. It exists so every future session (and every human) builds toward the same target instead of
re-litigating decisions already made. Update this file when a decision changes — don't silently drift from it.

Written: 2026-07-24. Supersedes nothing (first version). Source: maintainer discussion, no new research.

## 1. Why this file exists

Every other file in `docs/` specifies the **knowledge model** (how facts about crypto projects are captured).
Nothing until now specified the **application layer** — the actual product a user opens, what it shows them,
and why they'd trust it. That gap caused rework risk: without a locked reference, each session would
re-derive product decisions from scratch. This file is that lock.

`docs/` stays documentation-only per `CLAUDE.md` — this file documents *intent and design decisions for the
application*, not crypto project knowledge. It does not belong in `examples/` or `tracking/`.

## 2. Product positioning (locked)

- **What CIF is**: a *copilot for historical due-diligence* — it turns "what happened to comparable projects
  before" into a structured, sourced, confidence-rated input to a user's own airdrop/investment decision.
- **What CIF is NOT**: an oracle that predicts outcomes. Never phrase output as "this project will succeed."
  Always phrase as "N comparable decision events looked like this; here's what happened; here's the
  confidence and why."
- **Value vs. doing your own deep research**: manual research gets you the same facts. It does not get you
  **pattern recognition across dozens of unrelated projects held in working memory simultaneously**, and it
  does not get you a **calibrated, falsifiable confidence score** (backtest-verified, not vibes).
- **Relationship to Nansen-style tools**: complementary, not competing. Nansen answers "where is the money
  moving right now" (on-chain telemetry). CIF answers "what does this pattern of decisions usually lead to"
  (historical causal analogy). A user plausibly wants both.

## 3. Trust architecture (locked) — three layers, each needs dedicated UI

Nansen's trust trigger is verifiable on-chain data. CIF has no equivalent single source of truth, so trust is
built from three UI-visible layers instead. **No layer is optional; all three ship together, not staged.**

### 3.1 Source / citation panel
Every claim the system surfaces (analog cited, pattern fired, prediction generated) must expand — one click,
inline, not a separate page — to the original dossier passage it came from. Rule: **no claim without a
one-click path to its raw citation.**

```
[Pattern fired: "Efficiency → Concentration → Mitigation"]
  ↳ Observed in: EigenLayer, Lido, Ethereum (3 instances)      [expand ▾]
     EigenLayer.md → Decision Events → DEV-004
     "...restaked collateral concentrated into a few AVS/operators..."
     Evidence: HIGH · Provenance: Gemini Deep Research
     [Open full dossier →]
```

### 3.2 Evidence Level + provenance badges
Two distinct meanings that must never be visually conflated into one number:
- **Fact-level badge** (HIGH/MED/LOW): how many independent sources agree on this specific fact.
- **Pattern-level badge**: instance count + whether the pattern's `scope` (era range, per
  `examples/PatternRegistry.md`) actually covers the project being evaluated. A pattern with 3 instances but
  wrong era-scope must visibly warn, not silently apply.

### 3.3 Public Prediction Track Record page
`tools/backtest.py`'s scorecard becomes a public page, not just internal QA — this is the single most
Nansen-equivalent trust signal CIF has: proof the system was right on a case it didn't use to build the
pattern. Each row must show **as-of date vs. event date** explicitly, so it's structurally impossible to read
as post-hoc cherry-picking.

```
✅ Renzo ezETH depeg (Apr 2024)
   Pattern: P3 "Rehypothecation compounds correlated failure"
   As-of data cutoff: [date before depeg]  →  Event: Apr 2024  →  Outcome: PASS
   [Backtest detail →] [Pattern source →]
```

## 4. Point 5 — project identification on input (locked: Hybrid)

Open question from the trust discussion: when a user inputs a new/unfamiliar project, how does CIF know what
it *is* well enough to match it against `cif.json`? Three options were weighed:

1. Manual form (user self-tags category/narrative) — cheap, but pushes CIF's taxonomy burden onto the user.
2. Pure LLM auto-extraction from URL/whitepaper — best UX, but risks confident-sounding misclassification on
   thin source material, silently poisoning the match.
3. **Hybrid (chosen)** — LLM proposes tags/category from whatever the user supplies (URL, name, socials,
   whitepaper excerpt); user reviews and corrects before the match against `cif.json` runs.

**Why hybrid wins**: it keeps a human checkpoint between "LLM guessed" and "system matched a pattern from
that guess" — an unreviewed miscategorization is exactly the kind of unverifiable claim Section 3 exists to
prevent. The proposed tags themselves must show *why* the LLM proposed them (which input text triggered which
tag) — same one-click-to-evidence rule as everything else in this document.

Flow: `user input → LLM extraction (draft tags) → user confirm/edit → match against cif.json → output with
full Section 3 trust chain`.

## 5. Data bridge (approved, not yet built)

CIF (this repo) stays the knowledge source of truth. **AirdropOS** (`Scryptexai/AirdropOS`, separate repo —
JS/TS frontend, Python backend, Supabase, Vercel) is the consumer application. Approved integration: repos are
**not** merged; `poc/cif.json` (schema `cif-export/1`) is synced into Supabase tables, and AirdropOS queries
Supabase instead of its current mocked/fabricated intelligence data. Supabase auth for this bridge has already
been granted by the maintainer. No sync script exists yet — this is queued, not started.

## 6. Build phases

| Phase | Scope | Depends on | Status |
|-------|-------|------------|--------|
| **0** | Knowledge pipeline: ontology, `run.sh` ingest, `poc/cif.json` export, `tools/backtest.py` | — | ✅ done |
| **1** | Application UI: Section 3 (citation panel, evidence badges, public track-record page) + Section 4 hybrid identification, built into/around `poc/intake.html` | Phase 0 | not started |
| **2** | Supabase sync script: push `cif.json` → Supabase tables on each `run.sh build` | Phase 0 | not started |
| **3** | AirdropOS integration: point its queries at the synced Supabase tables, replacing mocked intelligence data | Phase 2 | not started |
| **4** | Public Prediction Track Record page live (can ship independently once Phase 1's backtest UI exists) | Phase 1 | not started |

Phases 1 and 2 are independent and can run in parallel. Phase 3 cannot start before Phase 2. Definition of
done per phase = the UI/behavior described in the relevant section above is live and demonstrable, not just
coded.

## 7. Non-goals (explicit, to prevent scope creep)

- CIF does not claim real-time on-chain telemetry (that's Nansen's job, not this product's).
- CIF does not output a bare score/verdict with no visible evidence chain — Section 3 is non-negotiable, even
  under UI-simplicity pressure.
- The Hybrid identification flow (Section 4) does not get silently downgraded to pure auto-extraction to save
  a click — the human-confirm step stays unless a future maintainer decision explicitly revises this file.

## 8. Open questions (not yet decided)

- Exact UI framework/stack for Phase 1 (artifact prototype vs. real frontend repo — likely lives in
  `poc/` first, graduates later).
- Whether the Supabase sync (Phase 2) is push-on-build (CI-triggered) or pull-on-demand (AirdropOS fetches
  `cif.json` directly and imports).
- Public track-record page hosting (part of AirdropOS, or a standalone page CIF itself publishes).

## Related Files

`examples/DatasetIndex.md` (V1→V2 Upgrade Queue — separate, data-hygiene track, not blocked by this),
`docs/Reasoning/Prediction.md`, `examples/PatternRegistry.md` (`scope` field, referenced in §3.2),
`tools/backtest.py`, `poc/intake.html`, `poc/cif.json`, `CLAUDE.md`.
