# Application Blueprint — CIF as a Product (v2)

## Status

**Locked plan, pre-build.** This is the reference document for the `Framework → Applications` stage of the
pipeline. It exists so every future session (and every human) builds toward the same target instead of
re-litigating decisions already made. Update this file when a decision changes — don't silently drift from it.

Written: 2026-07-24. Source: maintainer discussion, no new research.

**Revision 2026-08-08 — §7/§8, prompted by an enterprise-platform proposal.** The maintainer proposed a
Palantir/Bloomberg-style module list (connectors, ontology, collaboration, compliance, intelligence,
operations). Checking it against this file surfaced that §7's telemetry non-goal was **mis-worded, not
merely misread**: taken literally it forbade the live Observable layer that §9.3's own trust mechanism
requires. That bullet now separates positioning (don't sell CIF as on-chain telemetry) from plumbing (a
bounded connector set is required). One genuinely new non-goal was added — never forecast CIF Score, since
it measures our research completeness rather than project health — and §8 now records that the Sentiment
track is dormant rather than rejected. The full module list is triaged and sequenced in
`docs/Project/EnterpriseRoadmap.md`; this file stays the source of truth for positioning and trust rules.

**Revision 2026-07-26 — v1 → v2 (maintainer decision, after LayerZero proved out the 11-phase pipeline).**
v1 was written before any project had gone through the Format v3 phased pipeline — it scoped CIF's whole
product around one use case ("pattern-matching copilot for a due-diligence decision") because that was the
only use case the dataset could support at the time. Having now seen what an actual 11-phase dossier contains
(LayerZero: 76 entities, 15 fully-causal Decision Events with 8-POV stakeholder reactions each, full
financial/token/tech/ecosystem/market intelligence, 29 cross-checked conflict resolutions), the maintainer
judged that framing too narrow — the data supports several genuinely different product surfaces, not just
one. v2 (§2b, §11) broadens the product's use-case scope and proposes an information architecture built
around that breadth, and folds AirdropOS's original content-creator toolkit (rebuilt, not discarded) into
that same structure instead of leaving it as a bolt-on outside CIF's own menu. §§1–10 below are v1 and remain
the trust/positioning/monetization foundation — v2 extends them, it does not replace them. Superseded
specifics are marked inline rather than deleted.

**Revision 2026-07-24 (same-day follow-up discussion):** target market and §4 identification flow revised
(see §4 and new §9) after the maintainer flagged that airdrop hunters are overwhelmingly free-riders and that
on-chain analytics tools (Nansen, Arkham, DeBank) structurally cannot cover pre-TGE projects. Superseded
content is marked inline rather than deleted, so the reasoning behind the change stays visible.

**2026-07-26 — AirdropOS UI audit.** Before the maintainer hands AirdropOS to Claude Design for the actual
build/upgrade/rebrand-to-CIF pass, this repo's session audited the current AirdropOS codebase against this
document. See `docs/Project/AirdropOS-UI-Audit.md` for the full findings (diagnosis only, no implementation)
— summary: the Intelligence surface is more faithfully built to this spec than expected, but the Track Record
page (§3.3) is fully unbuilt, every route requires login (contradicting §9.2's free-browsing promise and
blocking §3.3's public-ness), three stale/contradictory legacy product docs still live in that repo, and
branding still reads "airdrop hunter os" against the revised §2 target market.

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

## 2b. Beyond pattern-matching (v2 — what an 11-phase dossier actually supports)

v1 scoped the whole product around one surface: a user asks about one project, CIF returns a pattern-match
read. A completed Format v3 dossier (11 phases, proven on LayerZero) is much richer than that single use case
needs — treating it as *only* pattern-matching input leaves most of what was actually collected unused. Each
row below names a **distinct product surface**, which phase(s) of the dossier it draws from, and who it's
for. None of these require new research — they're different *views* over data CIF already collects.

| Surface | Draws from (phase) | For whom | What it does that pattern-matching alone doesn't |
|---|---|---|---|
| **Due-diligence memo / one-click export** | All 11, synthesized | Fund analyst, VC | Compiles funding history, team, tokenomics, audit history, and flagged risks into one exportable document — the deliverable an analyst actually needs to hand upward, not just a screen to read. |
| **Entity graph / relationship explorer** | 2 Entity | Analyst mapping exposure across a portfolio | Query *across* projects: which of my portfolio companies share an investor, auditor, or exchange listing with a project that just had an incident? This is the "contagion mapping" `docs/Ontology/Relationships.md` was already built for, but v1 never gave it a screen. |
| **Founder/team track record lookup** | 2 Entity + 3 Historical, cross-project | Anyone diligencing a new founder/team | Search a person or org by name, see every project and Decision Event they're linked to across the whole dataset — surfaces repeat-founder and repeat-VC patterns a single-project view can't. |
| **Red-flag / risk scanner** | 3 Historical, 4 Technology, 6 Token, 11 Conflict Resolution | Fast pre-screen before deep reading | A scannable checklist pulled from what's already extracted — unresolved `INKONSISTENSI`, audit gaps, concentrated holder positions, era-mismatched claims — instead of requiring someone to read the full prose to notice them. |
| **Historical-analog comparison** | 3 Historical + 9 Behavioral, cross-project | Same as pattern-matching, but side-by-side | The *current* single-pattern-fired UI (§9.4) stays, but this adds an explicit N-way comparison table against the most similar historical Decision Events — closer to how an analyst actually works (compare 3–4 precedents at once), not a single generated verdict. |
| **Content Studio (rebuilt from AirdropOS's original purpose — see §11.3)** | All 11, repurposed | Content creators, CIF's own marketing | The same cited, structured intelligence that grounds a due-diligence memo also grounds a content template (thread, explainer, timeline graphic script) — an AI agent drafts from real dossier facts instead of the old flow's "paste your own unverified research." Reuses the trust chain, doesn't bypass it. |
| **Portfolio with graded outcomes (rebuilt from AirdropOS's "Porto")** | 3 Historical + whatever the user tracked | Individual user (any tier) | Not just "what I hold," but *"CIF said X about this project — here's what happened since."* Ties a user's own positions back to CIF's own Current Read/Signal history, so the user's portfolio becomes a personal instance of the same public Track Record (§3.3) mechanism. |
| **Structured query / API access** | All 11, machine-readable | Power users, funds (Pro) | v1 named "API access" as an unscoped Pro feature (§9.2); v2 makes concrete *why* it's valuable now — the data model is rich enough to answer questions like "every project where a Series A closed within 5 months of a security incident," not just "fetch project X's report." |

None of this changes §3's trust architecture (every one of these surfaces still needs the same citation
chain, the same Evidence Level discipline) — it changes what's built *on top of* that trust chain. §11
proposes how these fold into one coherent information architecture instead of shipping as disconnected
bolt-ons.

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
| **2** | Supabase sync script (`tools/sync_supabase.py`, opt-in `./run.sh sync`, not automatic on every build — see §10.2); swap AirdropOS's `cifMock.js` for real reads; retire the orphaned `deep-research`/`research-project` edge functions + `research_reports` table (§5) as part of the same cutover | Phase 0 | sync script + `cif_projects`/`cif_patterns`/`cif_backtests` tables done; frontend swap (10.3) not started |
| **3** | AirdropOS integration: point its queries at the synced Supabase tables, replacing mocked intelligence data | Phase 2 | not started |
| **4** | Public Prediction Track Record page live (can ship independently once Phase 1's backtest UI exists) | Phase 1 | not started |

Phases 1 and 2 are independent and can run in parallel. Phase 3 cannot start before Phase 2. Definition of
done per phase = the UI/behavior described in the relevant section above is live and demonstrable, not just
coded.

## 7. Non-goals (explicit, to prevent scope creep)

- CIF does not **position or sell itself** as a real-time on-chain telemetry product — that is Nansen's job,
  and competing there abandons the structural differentiator in §2 (pre-token projects are invisible to
  on-chain tools, not merely deprioritized). *This bullet is about positioning, not plumbing.* CIF **does**
  pull a bounded set of Observable metrics (TVL, funding rounds, unlock schedules), because §9.3's second
  trust mechanism requires exactly that — verifiable-today facts shown next to a still-pending read. The
  bound is explicit: connectors exist to serve the Observable layer and the daily catalog refresh, at daily
  freshness, not to become a general data platform. Wording revised 2026-08-08 (see Status) because the
  original phrasing read as a ban on §9.3.2 itself.
- CIF does not output a bare score/verdict with no visible evidence chain — Section 3 is non-negotiable, even
  under UI-simplicity pressure. This includes never gating trust-depth to upsell (§9) — the paywall gates
  scope and continuity, never the citation/evidence chain itself.
- CIF never phrases a live, unresolved read as a binary success/failure prediction (§9) — always a Current
  Read (with Pattern Confidence + Trajectory Probability, separately labeled) plus any Signal being watched.
- CIF never publishes a "signal being watched" without an objective, checkable trigger condition and a
  commitment to grade the resolution publicly either way (§9) — this is what keeps the base-case/signal
  framing from degrading into "hedged both ways, always right."
- **CIF never forecasts its own CIF Score as a user-facing output** (added 2026-08-08). CIF Score measures
  *research completeness* — the six dimensions in `tools/extract_qa.py` are Research Quality, Consistency,
  Evidence, Coverage, Conflict, Knowledge, all properties of **our dossier**, not of the project. "This
  project's CIF Score will reach 92 in three months" therefore forecasts our own future diligence, which is
  worthless to a user and, worse, invites reading a research-completeness number as a project-health
  number. Forward-looking statements about a *project* use §9.4's Current Read (Pattern Confidence +
  Trajectory Probability) and nothing else. Ranking dossiers by weakest coverage to decide what to research
  next is legitimate and encouraged — as a maintainer-ops view, never a product surface.
- The daily-curated-catalog identification flow (§4) does not get silently replaced by live per-user LLM
  classification as the primary path to save engineering effort — hybrid stays a fallback only, unless a
  future maintainer decision explicitly revises this file.
- (v2) Content Studio (§11.3) never generates content from an unverified/pasted document as its primary
  path — it drafts from CIF's own cited dossier data, same as every other surface. A "paste your own
  research" fallback may still exist for a not-yet-covered project (mirroring §4's fallback), but it is not
  the default flow, the same way hybrid LLM-tagging isn't the default identification flow.
- (v2) Content Studio's generated output never drops the citation trail (§11.3) — a template is still bound
  by §3's "no claim without a one-click path to its raw citation" rule; it is a new *surface*, not an
  exemption from the trust architecture.

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
- (v2) Desktop-first vs. mobile-first for the Intelligence core (§11.1) — presented as a strong
  recommendation, not yet a locked decision; needs explicit maintainer sign-off before Claude Design commits
  to a layout direction.
- (v2) Content Studio's exact output formats/templates (§11.3) — not scoped here; should be derived from
  what AirdropOS's original content workflow already validated works, not invented fresh.
- (v2) Which of §2b's new surfaces (due-diligence export, entity graph explorer, founder/team lookup,
  red-flag scanner, analog comparison) ship in the first build-out vs. later — §2b describes what the data
  supports, not a sequencing commitment; needs a build-phase pass similar to §6's, once 11.1 is settled.
- **Sentiment: dormant, not rejected** (recorded 2026-08-08). `tools/ingest.py` still supports a `sentiment`
  type and `examples/Sentiment/` exists, but holds only a README — the track was never carried into the
  Format v3 era and this document has never taken a position on it either way. Reviving it needs a specific
  job, not a general "add sentiment analysis": the two candidates worth considering are (a) an Observable-
  layer input under §9.3.2, or (b) a *divergence* signal — where crowd sentiment disagrees with the Current
  Read, which is more interesting than sentiment on its own. Undecided; whoever revives it should say which.

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

## 10. Phase 2 scope — Supabase sync (scoped 2026-07-24; tables + sync script built 2026-07-26)

Scoped against the live `airdropos-pro` Supabase project (`szumyjuvfjkobvcqswwd`). Key finding: **every
existing AirdropOS table is per-user, RLS-scoped to `auth.uid()`** (`research_reports`, `projects`, `accounts`,
etc. — each user only ever sees their own rows). CIF's data is structurally different: it is **one shared
catalog every user reads**, not something any user owns. This is the central design decision Phase 2 must get
right — CIF's tables need **read-for-everyone, write-only-via-sync** RLS, not the per-user pattern the rest of
the schema uses.

**2026-07-26 update:** the three tables below turned out to **already exist** on the live project (created by
an earlier pass this document didn't have a record of) with an initial sync already in them. §10.1's field
list below has been corrected to match the actual live schema (confirmed via direct inspection, not
re-guessed) — a few names differ from this section's original draft (`prediction`/`validation` spelled out in
full, not abbreviated `pred`/`val`; `cif_backtests` carries `given`/`expect`/`fired`/`missed` arrays mirroring
`tools/backtest.py`'s own result shape, not the originally-guessed `as_of_note`/`event_date`). `airdrop_portfolio`
also already has a `cif_project_id` foreign key into `cif_projects.id`, wiring up §2b's Portfolio-linked-to-CIF
concept at the schema level already. `tools/sync_supabase.py` now exists (§10.2) and its output was verified
field-for-field against the live LayerZero row before being considered correct — including one real mismatch
caught and fixed: `category` is a `text[]` split into meaningful parts
(`"Interoperability / Omnichain Messaging (Bridge, GMP, DVN security)"` → 5 array elements), not one blob string.

### 10.1 Tables (CIF-owned, additive — nothing existing altered; already live)

- **`cif_projects`** — one row per project. `id` (text, the CIF slug e.g. `layerzero`), `name`, `category`
  (text[] — split on `/` and the trailing parenthetical, not one string), `tier` (deep/summary), `era`,
  `tags` (text[]), `is_todays_pick` (bool), `pattern_confidence` (int, nullable), `trajectory_probability`
  (int, nullable), `observable` (jsonb, the verified-now metric tiles), `current_read` (text, nullable),
  `signal` (jsonb, nullable), `evidence` (jsonb, the cited pattern cards), `comparables` (jsonb),
  `source_file` (text — the CIF dossier path, for traceability), `synced_at`. **Only the deterministic
  roster fields are populated by the sync script today** (id/name/category/tier/era/tags/source_file) —
  `pattern_confidence` through `comparables` need the not-yet-built per-project synthesis step (§8) and are
  left null/empty rather than guessed; do not backfill them with placeholder values.
- **`cif_patterns`** — standalone, mirrors `examples/PatternRegistry.md` 1:1 (`id` "P1".."P6", `name`,
  `confidence`, `instances`, `scope`, `analogs` text[], `triggers` text[], `source`, `prediction`,
  `validation`, `watch` text[], `synced_at`). Kept separate from `cif_projects.evidence` (rather than only
  embedded there) so a standalone Patterns Library page can query it directly.
- **`cif_backtests`** — mirrors `poc/benchmarks.json` (`tools/backtest.py`'s own scorecard shape) 1:1, feeds
  the Phase 4 public Track Record page: `id` (derived `backtest-01` etc.), `title`, `type`
  (validation/consistency/control), `category`, `given`/`expect`/`fired`/`missed` (text[]), `outcome`,
  `source`, `verdict`, `recall` (numeric), `file`, `synced_at`.

RLS on all three: enabled, with a `SELECT` policy (confirmed live). **No `INSERT`/`UPDATE`/`DELETE` policy for
any client role** — writes happen only via the sync script using the Supabase **service_role** key, which
bypasses RLS. Whether the `SELECT` policy also covers `anon` (needed for a truly public Track Record page,
not just `authenticated`) is still open — see §10.4.

### 10.2 Sync mechanism (built)
`tools/sync_supabase.py`, in **this** repo (not AirdropOS) — reads `poc/{projects,patterns,benchmarks}.json`,
upserts into the three tables above via Supabase's REST API directly (stdlib only, no
`requests`/`supabase-py` dependency, matching this repo's minimal-dependency convention —
`requirements.txt`). `SUPABASE_URL`/`SUPABASE_SERVICE_ROLE_KEY` stay as local env vars, never committed, same
treatment as the research prompts (see `Deep-Research-Brief.md`). Wired into `run.sh` as an explicit opt-in
step (`./run.sh sync`), not automatic on every build/`all` — pushing to a live production database shouldn't
be a silent side-effect of a routine local build. `--dry-run` prints the rows without any network call or
env vars, for previewing. See `tools/README.md` for usage.

### 10.3 Frontend swap (AirdropOS)
Replace `frontend/src/lib/cifMock.js` reads in `Intelligence.jsx`/`IntelligenceDetail.jsx` with real
`supabase.from('cif_projects')...` calls via a new thin `lib/cifData.js`, mirroring the existing `lib/db.js`
pattern — same component code/props shape, so this is a data-layer swap, not a UI rewrite. Retire the orphaned
`deep-research`/`research-project` edge functions and `research_reports` table in the same change (§5).

### 10.4 Open questions
- Public (`anon`) read access for the Track Record page vs. requiring login — affects whether §3.3's "public"
  page is actually public.
- "Today's Pick" selection rule — not yet decided; simplest default is top of the Opportunity Ranking, rotated
  daily by the sync script.
- Sync cadence — manual `./run.sh sync` only, or also scheduled (e.g. a cron trigger) so AirdropOS updates
  without the maintainer remembering to run it by hand.

## 11. Information architecture v2 (maintainer decision 2026-07-26 — diagnosis/direction, not final UI)

This section states *what the menu structure should contain and why*, at the same level of abstraction as
the rest of this document (product decisions, not pixels/components) — the actual visual design is Claude
Design's job, per `docs/Project/AirdropOS-UI-Audit.md`'s own scoping. It exists because the maintainer flagged
two compounding problems with the current AirdropOS menu: (a) it doesn't read as a professional research
SaaS at all, and (b) even setting that aside, its labels/structure predate both the CIF pivot and the 11-phase
data (§2b) — it was built for a WhatsApp-reminder airdrop tracker, then partially relabeled, never redesigned
from the product this now actually is.

### 11.1 Root-cause finding: the mobile-bottom-nav form factor itself is likely wrong, not just the labels

`docs/UX_FRAMEWORK.md` (superseded, see `AirdropOS-UI-Audit.md` Finding 1) inherited a "5 slot + Lainnya"
mobile bottom-nav constraint from the original tracker app, because a solo hunter checking daily tasks on
their phone is a genuinely mobile-first use case. **CIF's actual paying persona (§2: researchers, analysts,
funds doing due diligence) is not that user** — Messari, Delphi, Nansen, and Bloomberg-terminal-style tools
that this persona already pays for are desktop-first, dense, multi-panel products, because diligence work
(reading a memo, comparing analogs side-by-side, cross-referencing an entity graph) genuinely benefits from
screen real estate a phone doesn't have. Relabeling icons inside a mobile-hunter-shaped nav will not produce
"feels like a professional SaaS," because the constraint that shape was designed around no longer describes
the primary user. **Recommendation: the Intelligence/research core should be desktop-first (a proper
multi-panel dashboard layout), with a lighter mobile companion view for on-the-go lookups — not the reverse.**
This is the single highest-leverage form-factor decision for Claude Design to resolve before laying out
screens, and it is presented here as a strong recommendation, not yet a locked decision — flag if this
should be revisited.

### 11.2 Proposed top-level structure

Not a nav-bar spec (slot count/order is Claude Design's call once 11.1 is resolved) — this is the set of
first-class sections and what each owns, so nothing from §2b ships as a disconnected bolt-on:

- **Intelligence** (existing core, keep and extend) — search/browse the curated catalog (§4), Opportunity
  Ranking, Today's Pick, full reports with the §3 trust chain. §2b's due-diligence memo export, entity graph
  explorer, founder/team lookup, red-flag scanner, and historical-analog comparison all live *inside* this
  section as views/tools over the same underlying report — not separate top-level items — because they're
  all facets of "diligencing one project or comparing several," the same job Intelligence already does.
- **Track Record** (planned, unbuilt — `AirdropOS-UI-Audit.md` Finding 2) — public, not behind login (Finding
  3) — CIF's own calibration history, independent of any single project.
- **Content Studio** (rebuilt from AirdropOS's "Sesi" — see §11.3) — first-class section, not hidden inside
  Intelligence or left outside the app's menu as a separate tool. Content creation is a genuinely different
  job-to-be-done from diligence, even though it draws on the same data.
- **Portfolio** (rebuilt from AirdropOS's "Porto" — see §2b) — personal tracking re-grounded in CIF's own
  Current Read/Signal history instead of a bare manual list.
- **Account/Settings** — unchanged in kind from today, rebranded.

### 11.3 Content Studio — how the rebuilt "Sesi" actually works

AirdropOS's original purpose (per the maintainer, and consistent with `memory/PRD.md`'s "content for daily
social media" framing predating the CIF pivot) was a content-creator tool: paste/add a doc, an AI turns it
into ready-to-use templates. That job doesn't go away — it gets **re-grounded in CIF's own cited data instead
of an unverified user-pasted doc**, which is strictly an upgrade on the same trust principle §3 already
established for diligence use:

- **Input:** any project already in CIF's catalog (no separate research step — the whole point of the
  curated-catalog model in §4 is that this data already exists), or, for a project not yet covered, the same
  "Request coverage" fallback §4 already defines.
  1. Draws structured facts from the dossier (a launch date, a funding round, a Decision Event, an
     Evidence-Level-tagged claim) — the same underlying JSON that grounds a due-diligence report — and
     drafts a template (thread outline, explainer script, timeline graphic copy) in whatever format the
     content type needs.
  2. **Every generated template keeps its source attachment**, the same one-click-to-citation rule as §3.1 —
     a generated thread about "why this project's TVL dropped" must still trace each claim back to the
     dossier passage it came from. This is what stops Content Studio from degrading into ungrounded AI
     content generation once it's inside CIF's own menu — the same non-negotiable rule as §7's, extended to
     a new surface rather than exempted from it.
  3. Output formats are a build detail (not scoped here) but should map to what AirdropOS's original content
     workflow already validated works for its users, rather than inventing new formats unprompted.
- **Why this belongs inside CIF's menu, not bolted on outside:** the maintainer's own framing — a
  content-creator tool connected to an AI agent with CIF's rich, cited dataset behind it is a *more powerful*
  version of the same tool, not an unrelated feature riding alongside CIF. Keeping it external would mean
  duplicating the trust-chain plumbing (§3) a second time instead of reusing it.

## Related Files

`examples/DatasetIndex.md` (V1→V2 Upgrade Queue — separate, data-hygiene track, not blocked by this),
`docs/Reasoning/Prediction.md`, `examples/PatternRegistry.md` (`scope` field, referenced in §3.2),
`tools/backtest.py`, `poc/intake.html`, `poc/cif.json`, `CLAUDE.md`,
`docs/Project/AirdropOS-UI-Audit.md` (2026-07-26 audit of the current AirdropOS build against this spec),
`docs/Project/AirdropOS-Rebuild-Prompt.md` (paste-ready prompt derived from this file + the audit, for the
session that will actually do the rebuild/rebrand).
