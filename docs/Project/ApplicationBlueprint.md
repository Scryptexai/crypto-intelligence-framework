# Application Blueprint — CIF as a Product

## Status

**Locked plan, pre-build.** This is the reference document for the `Framework → Applications` stage of the
pipeline. It exists so every future session (and every human) builds toward the same target instead of
re-litigating decisions already made. Update this file when a decision changes — don't silently drift from it.

Written: 2026-07-24. Source: maintainer discussion, no new research.

**Revision 2026-07-24 (same-day follow-up discussion):** target market and §4 identification flow revised
(see §4 and new §9) after the maintainer flagged that airdrop hunters are overwhelmingly free-riders and that
on-chain analytics tools (Nansen, Arkham, DeBank) structurally cannot cover pre-TGE projects. Superseded
content is marked inline rather than deleted, so the reasoning behind the change stays visible.

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
- **Structural differentiator (why pay CIF and not Nansen) — lead with this.** Nansen/Arkham/DeBank are
  on-chain analytics: their data model requires a deployed contract/token to exist. A pre-token,
  testnet/points-phase project is *structurally invisible* to them, not just deprioritized. CIF's
  Decision-Event/pattern reasoning doesn't require an on-chain footprint, so it can score a project **before**
  on-chain tools can see it at all. This is the actual product gap, not a marketing angle.
- **Target market (revised from "airdrop hunters"):** hunters are overwhelmingly free-riders — the
  well-documented sybil/multi-wallet-farming pattern optimizes for minimizing cost, not paying for tools.
  They remain the free, top-of-funnel/distribution audience (see §9), not the revenue base. The paying
  persona is **web3 researchers, analysts, and funds/investors doing pre-TGE due diligence** — the same buyer
  segment that already pays for Messari/Delphi/Kaito-style research subscriptions, where a confidence/
  probability read is an input to real capital decisions, not idle curiosity.

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

## 4. Point 5 — project identification on input (REVISED — hybrid demoted to fallback)

Open question from the trust discussion: when a user inputs a new/unfamiliar project, how does CIF know what
it *is* well enough to match it against `cif.json`? Three options were originally weighed:

1. Manual form (user self-tags category/narrative) — cheap, but pushes CIF's taxonomy burden onto the user.
2. Pure LLM auto-extraction from URL/whitepaper — best UX, but risks confident-sounding misclassification on
   thin source material, silently poisoning the match.
3. Hybrid — LLM proposes tags/category from whatever the user supplies; user reviews and corrects before the
   match against `cif.json` runs.

**Superseded as the primary flow.** The maintainer curates and ingests every newly-launched project daily
(the existing `run.sh` pipeline) — coverage is built ahead of demand, not on request. So the end-user
"Analyze" action is a **search over an already-completed catalog**, not a live per-user classification
wizard: `user searches by name → catalog lookup → output with full Section 3 trust chain`. This removes the
identification problem for the common case, because the project is already known to the system before the
user ever asks.

**Hybrid LLM-tagging is demoted to a fallback**, used only for the rare "not yet covered" case (a small
"Request coverage" affordance on the search screen) — not the main path. The original reasoning still holds
for that narrow surface: a human checkpoint between "LLM guessed" and "system matched a pattern from that
guess" prevents an unreviewed miscategorization, which is exactly the kind of unverifiable claim Section 3
exists to prevent.

An **AI assistant** may still sit next to a report (e.g. "Ask AI about this report") — but strictly as an
optional explainer/feedback layer over an already-computed report, never as the thing performing the analysis.

## 5. Data bridge (approved, not yet built)

CIF (this repo) stays the knowledge source of truth. **AirdropOS** (`Scryptexai/AirdropOS`, separate repo —
JS/TS frontend, Python backend, Supabase, Vercel) is the consumer application. Approved integration: repos are
**not** merged; `poc/cif.json` (schema `cif-export/1`) is synced into Supabase tables, and AirdropOS queries
Supabase instead of its current mocked/fabricated intelligence data. Supabase auth for this bridge has already
been granted by the maintainer.

**Frontend shipped ahead of the sync (2026-07-24):** AirdropOS's `Intelligence.jsx`/`IntelligenceDetail.jsx`
have already been redesigned to match §3/§4/§9 of this document (search-first over a curated catalog,
citation-backed evidence, base-case/signal-to-watch framing) and deployed to production — but still backed by
`frontend/src/lib/cifMock.js` (static mock data shaped like the future sync), not a real Supabase read. This
was a deliberate sequencing choice: the UI could be validated without waiting on the sync.

**Superseded by this UI, not yet cleaned up:** AirdropOS's old `deep-research`/`research-project` Supabase edge
functions and the `research_reports` table (the previous live-per-user-Gemini-call approach) are now orphaned
— nothing in the frontend calls them anymore, but they still exist. Maintainer decision: **fold their removal
into Phase 2** rather than doing it as a separate cleanup pass — Phase 2 replaces them with the real sync
anyway, so retiring the old path and standing up the new one happen together.

## 6. Build phases

| Phase | Scope | Depends on | Status |
|-------|-------|------------|--------|
| **0** | Knowledge pipeline: ontology, `run.sh` ingest, `poc/cif.json` export, `tools/backtest.py` | — | ✅ done |
| **1** | Application UI: browsable Opportunity Ranking + search-first Analyze (§4) + trust UI (§3: citation panel, evidence badges, base-case/signal-to-watch report format) | Phase 0 | ✅ shipped to AirdropOS production, on mock data (§5) |
| **2** | Supabase sync script: push `cif.json` → Supabase tables on each `run.sh build`; swap AirdropOS's `cifMock.js` for real reads; retire the orphaned `deep-research`/`research-project` edge functions + `research_reports` table (§5) as part of the same cutover | Phase 0 | not started |
| **3** | AirdropOS integration: point its queries at the synced Supabase tables, replacing mocked intelligence data | Phase 2 | not started |
| **4** | Public Prediction Track Record page live (can ship independently once Phase 1's backtest UI exists) | Phase 1 | not started |

Phases 1 and 2 are independent and can run in parallel. Phase 3 cannot start before Phase 2. Definition of
done per phase = the UI/behavior described in the relevant section above is live and demonstrable, not just
coded.

## 7. Non-goals (explicit, to prevent scope creep)

- CIF does not claim real-time on-chain telemetry (that's Nansen's job, not this product's).
- CIF does not output a bare score/verdict with no visible evidence chain — Section 3 is non-negotiable, even
  under UI-simplicity pressure. This includes never gating trust-depth to upsell (§9) — the paywall gates
  scope and continuity, never the citation/evidence chain itself.
- CIF never phrases a live, unresolved read as a binary success/failure prediction (§9) — always a Current
  Read (with Pattern Confidence + Trajectory Probability, separately labeled) plus any Signal being watched.
- CIF never publishes a "signal being watched" without an objective, checkable trigger condition and a
  commitment to grade the resolution publicly either way (§9) — this is what keeps the base-case/signal
  framing from degrading into "hedged both ways, always right."
- The daily-curated-catalog identification flow (§4) does not get silently replaced by live per-user LLM
  classification as the primary path to save engineering effort — hybrid stays a fallback only, unless a
  future maintainer decision explicitly revises this file.

## 8. Open questions (not yet decided)

- Exact UI framework/stack for Phase 1 (artifact prototype vs. real frontend repo — likely lives in
  `poc/` first, graduates later).
- Whether the Supabase sync (Phase 2) is push-on-build (CI-triggered) or pull-on-demand (AirdropOS fetches
  `cif.json` directly and imports).
- Public track-record page hosting (part of AirdropOS, or a standalone page CIF itself publishes).
- Exact Observable-metric set per project archetype (§9) — e.g. blockchain leads with TVL, early-stage
  protocol leads with funding round/stage — not yet formalized as a data-layer rule.
- Pro feature set for the researcher/investor persona (§9) — export-to-PDF, side-by-side comparison,
  portfolio watchlist, API access are named directions only, not designed or scoped.
- Pricing is still illustrative/undecided (see the reviewed prototype's upgrade modal, which says so
  explicitly).

## 9. Monetization & Trust Strategy

### 9.1 Free/paid split rule
Never gate **trust-depth** (the citation chain, evidence badges — CIF's actual differentiator, §3). Gate
**scope** and **continuity** instead. Analogy: Spotify never degrades audio quality on its free tier (its
core trust dimension) — it gates convenience (ads, shuffle-only, no offline). A degraded/stripped-down free
report would undercut the exact thing meant to attract a paying user later.

### 9.2 Dashboard mechanic (design reviewed)
- **Today's Pick** — one project, full report, assigned daily by the system (not user-chosen) — like
  Spotify's shuffle-only: real content, not on-demand control. Always free.
- **Opportunity Ranking** — the full ranked list (name, category, Pattern Confidence, Trajectory Probability,
  signal indicator) is visible to everyone, free, unlimited browsing (catalog browsing is never gated).
  Opening a **full report** for any project other than Today's Pick requires Pro (surface data free, depth
  metered/paid).
- Pro persona-fit features (named only, not designed): export report to PDF/memo, side-by-side project
  comparison, portfolio watchlist, API access — aimed at the researcher/fund persona (§2), not casual hunters.

### 9.3 Proving validity before an outcome resolves
Three mechanisms, required together — none alone is sufficient:
1. **Falsifiable, timestamped public claims** — every live read commits to a specific, checkable condition
   (not vague), published with a timestamp, auditable later even though unverifiable today.
2. **Live Observable-layer transparency** — Observable facts (TVL, funding, unlocks — `docs/Ontology/
   Metrics.md` territory) are verifiable *today*, shown alongside the still-pending read, building trust in
   the machinery while the outcome itself stays open.
3. **Calibration, not per-case verification** — weather-forecast analogy: a single "70% chance" call can't be
   verified in isolation, but a running calibration score (of live calls whose resolution window has passed,
   what fraction resolved the flagged direction) is trusted the way weather probabilities are. The public
   Track Record page (§3.3) needs to grow from the 3 closed historical backtests into also showing this live
   calibration score over time — open item, not yet built.

### 9.4 Base-case / signal-to-watch framing (replaces success/failure language)
Forward-looking output is never phrased as a binary success/failure prediction. Structure:
- **Current Read** — the dominant pattern-alignment given the project's current, disclosed state, with two
  separately-labeled numbers: **Pattern Confidence** (methodology strength — instance count/agreement) and
  **Trajectory Probability** (how much the current state leans toward that read). Never call the second one
  "success probability."
- **Signal being watched** — one or more specific, objectively observable conditions that would shift the
  read, each backed by a named historical analog, with an explicit resolution window and a commitment to log
  the outcome to the public Track Record either way.
- **Guardrail against "hedged both ways, always right":** trigger conditions must be objective/checkable, the
  read must state a real weighting (never a flat 50/50), and resolutions must be graded publicly — including
  inconclusive or wrong ones.

### 9.5 Analyze flow
Search-first over the maintainer-curated catalog (§4) — not a live classification wizard. An AI assistant may
sit next to a report as an optional explainer ("Ask AI about this report"), never as the analysis engine
itself.

## Related Files

`examples/DatasetIndex.md` (V1→V2 Upgrade Queue — separate, data-hygiene track, not blocked by this),
`docs/Reasoning/Prediction.md`, `examples/PatternRegistry.md` (`scope` field, referenced in §3.2),
`tools/backtest.py`, `poc/intake.html`, `poc/cif.json`, `CLAUDE.md`.
