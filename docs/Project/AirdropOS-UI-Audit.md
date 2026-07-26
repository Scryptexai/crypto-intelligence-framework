# AirdropOS UI/UX Audit vs. ApplicationBlueprint.md (2026-07-26)

## Status

**Audit only — no implementation.** This document diagnoses how `Scryptexai/AirdropOS` (the consumer app
that will be built up, upgraded, and rebranded to CIF) currently measures up against the locked spec in
`docs/Project/ApplicationBlueprint.md`. It does not prescribe pixel-level designs or component code — that
is explicitly out of scope here (maintainer's own instruction: this pass determines *what's wrong/missing*,
not *the new design*, which is a separate design pass). Findings are ranked by what actually blocks or
undermines the trust-architecture goal, not cosmetic preference.

Read alongside `ApplicationBlueprint.md` (the target) and AirdropOS's own `docs/UX_FRAMEWORK.md`,
`design_guidelines.json`, `memory/PRD.md` (three *different*, mutually-inconsistent prior visions — see
Finding 1).

## Executive summary

The core Intelligence surface (`Intelligence.jsx` / `IntelligenceDetail.jsx`, commit "Replace live per-user
Gemini research with CIF-style curated Intelligence", 2026-07-24) is **substantially better-aligned to the
locked trust architecture than expected** — Observable-data tiles, Current Read with two separately-labeled
numbers, Signal-being-watched with a resolution window, expandable per-pattern citation cards, and the
Today's Pick/Opportunity Ranking free-vs-Pro split are all genuinely implemented, not just planned. The real
problems are everywhere *around* that surface: three non-aligned legacy product visions still living in the
repo's docs, one still-missing trust-critical page (Track Record), an auth wall that contradicts the "free,
public browsing" promise, dead code from the pre-CIF architecture not yet removed, and branding that still
says "airdrop hunter os" while the actual target user has been repositioned to institutional researchers.

## Finding 1 — Three non-aligned product visions coexist in AirdropOS's own docs (HIGH priority)

The repo currently contains **three separate documents describing three different products**, none of which
agree with each other or with the actual current code:

| Document | Product it describes | Era |
|---|---|---|
| `memory/PRD.md` | Personal airdrop tracker, WhatsApp reminders via Fonnte, multi-"Paket" localStorage auth, per-project Discord role-farming | Oldest (v1/v2, Feb 2026) |
| `design_guidelines.json` | "Swiss & High-Contrast", light theme (`#F9FAFB` bg, black primary), wallet-slot management UI | Also old — doesn't match current dark theme at all |
| `docs/UX_FRAMEWORK.md` | "Crypto Intelligence Operating System" — 5-tab cockpit, Intelligence as 3 sub-tabs (Overview/Research/Knowledge) tied to the `research_reports` table + `research-project` edge function (live per-user Gemini research) | Middle — post-tracker, pre-CIF-pivot |
| **Actual current code** | CIF-curated catalog (`cifMock.js`), search-first, single flat Intelligence page, dark theme matching `UX_FRAMEWORK.md`'s palette but a flatter IA than it describes | **Current, 2026-07-24** |

None of the three documents was updated when the code pivoted to the CIF model. A rebrand/upgrade pass that
reads any one of them as "the current spec" without cross-checking against actual code will build on stale
assumptions. **Recommendation: retire or explicitly mark all three as historical before Claude Design starts
— the only living source of truth for the target state is `ApplicationBlueprint.md` (in this repo) plus
whatever the actual current `.jsx` files do.**

## Finding 2 — Public Prediction Track Record page does not exist (HIGH priority)

`ApplicationBlueprint.md` §3.3 calls this **"the single most Nansen-equivalent trust signal CIF has"** and
§6 lists it as Phase 4 (can ship independently once Phase 1's UI exists — it does). `App.js`'s route table
has no route for it, no page file exists for it, and `tools/backtest.py`'s scorecard (`poc/benchmarks.json`)
has no consumer in the frontend at all. This is not a partial implementation — it is fully unbuilt. Given how
central this page is to the "not opinion, but what actually happened" trust claim the maintainer described,
this is the single highest-leverage missing surface.

## Finding 3 — Every route requires login, including ones meant to be public (HIGH priority)

`App.js` wraps every route except `/login` and `/register` in `ProtectedRoute`. `ApplicationBlueprint.md`'s
own §9.2 says Opportunity Ranking browsing is "free, unlimited browsing... never gated," and §10.4 lists
"public (anon) read access for the Track Record page vs. requiring login" as an explicit open question. As
currently wired, there is no way for an unauthenticated visitor to see *anything* — not the ranking, not a
future Track Record page. This directly contradicts the stated free/paid split (§9.1: gate scope and
continuity, never the trust-depth or the ability to browse) and would make the Track Record page from
Finding 2 non-public even once built, undermining its entire purpose as an external trust signal. This is an
architectural decision (which routes are genuinely public vs. behind auth), not a styling one — flagging it
as something Claude Design needs to resolve explicitly, not inherit by default from the old tracker's
all-gated model.

## Finding 4 — Dead code from the pre-CIF architecture, confirmed still present (MEDIUM priority)

`lib/db.js` still defines `researchProject()`, `deepResearch()`, `getResearchReports()`,
`getResearchReport()` calling the `research-project`/`deep-research` Supabase edge functions and reading the
`research_reports` table. Grepped for callers across `pages/` and `components/` — **zero references found**;
this is confirmed dead code, not a hidden live path. The edge functions themselves
(`supabase/functions/deep-research/`, `supabase/functions/research-project/`) still physically exist too.
`ApplicationBlueprint.md` §5 already flagged this and scoped its removal into Phase 2 (the Supabase sync
build) rather than as a separate cleanup — that sequencing call still holds; flagging here so it isn't
missed or independently "rediscovered" as a surprise during the rebuild.

## Finding 5 — Branding still says "airdrop hunter os," contradicting the locked target market (MEDIUM priority)

`AppShell.jsx`'s header renders "AirdropOS" with the tagline "airdrop hunter os" directly under it. But
`ApplicationBlueprint.md` §2 explicitly revised the target market *away* from airdrop hunters ("overwhelmingly
free-riders... not the revenue base") *toward* web3 researchers/analysts/funds doing due diligence — the
persona the redesigned Intelligence page (Pattern Confidence, Trajectory Probability, cited evidence) is
actually built for. The header text is telling a hunter this app is for them, while the actual product below
it is built for an institutional-adjacent researcher. This is the most visible, single-line instance of the
rebrand the maintainer asked for, and the browser tab title is even less branded than that: `index.html`'s
`<title>` is still the literal scaffold default, `"Emergent | Fullstack App"` — never set to anything at all.

## Finding 6 — Terminology collision: "confidence" and "research" mean different things in different parts of the app (LOW priority, but genuinely confusing)

`Guide.jsx` exports a `RESEARCH_PROMPT_TEMPLATE` — but this is a prompt for the user's *own* manual research
to draft daily social-media content ideas ("bahan konten sosmed harian"), completely unrelated to CIF's
Decision-Event research pipeline. A reader skimming the Guide page could easily mistake this for "how CIF
research works," when it's actually a leftover content-creation aid from the old tracker product. Similarly,
`memory/PRD.md` describes a per-project "Confidence (0-100 slider)" field on the old airdrop tracker — a
manual, subjective, user-set number — which is an entirely different concept from CIF's `patternConfidence`
(methodology strength, backtest-derived) shown on the same app's Intelligence page. (Note: this specific
slider field was not found in the current `Projects.jsx`/`Dashboard.jsx` code during this audit, so it may
already be gone — but the vocabulary collision risk applies to any surviving fields named "confidence"
outside the Intelligence surface, and to the Guide page's prompt template regardless.) Recommendation:
rename or clearly re-scope anything outside the Intelligence surface that reuses "confidence" or "research"
language, so a user (or a future engineer) can't conflate CIF's evidence-backed numbers with an unrelated
manual/subjective field of the same name.

## What's already right (don't rebuild these — extend them)

- `cifMock.js`'s shape (`patternConfidence`/`trajectoryProbability`/`observable`/`currentRead`/`signal`/
  `evidence`/`comparables`) maps directly onto `ApplicationBlueprint.md` §10.1's proposed `cif_projects`
  columns — the Phase 2 Supabase sync should be a straightforward swap, not a redesign.
- The expand-to-citation pattern in `EvidenceCard` (`IntelligenceDetail.jsx`) already implements §3.1's
  "no claim without a one-click path to its raw citation" rule correctly, including source path + verbatim
  quote + analog list + era-mismatch warning (`eraNote`) — the era/scope-mismatch visual warning in
  particular is a real, non-trivial requirement (§3.2) that's already handled.
- Today's Pick vs. Opportunity Ranking vs. Pro-gated full report (`Intelligence.jsx`) already implements
  §9.2's free/paid split correctly — free unlimited browsing of the ranking, one free full report/day, Pro
  for the rest.
- The disclaimer footer on `IntelligenceDetail.jsx` ("bukan ramalan pasti... copilot due-diligence historis,
  bukan oracle") already matches §2's required positioning language.

## Priority order for the rebuild

1. Resolve Finding 1 (retire/mark the stale docs) *before* anyone designs against them — otherwise the
   rebuild inherits contradictory requirements silently.
2. Finding 3 (which routes are actually public) — this is a prerequisite decision for Finding 2, since a
   Track Record page built inside the current all-gated route structure won't achieve its purpose.
3. Finding 2 (build the Track Record page) — highest-leverage missing trust surface.
4. Finding 5 (rebrand pass) — the maintainer's explicit ask; also the fastest to fix (header, tagline, page
   title, any remaining "AirdropOS"/"airdrop hunter" copy).
5. Finding 4 (dead-code removal) — bundle into the Phase 2 Supabase sync as `ApplicationBlueprint.md` §5
   already decided, don't do it standalone.
6. Finding 6 (terminology cleanup) — lowest urgency, but cheap to fix alongside the rebrand pass.

## Related Files

`docs/Project/ApplicationBlueprint.md` (the spec this audits against), `poc/cif.json` (the real data this
UI needs to render once Phase 2's sync exists), `Scryptexai/AirdropOS` — specifically
`frontend/src/pages/Intelligence.jsx`, `IntelligenceDetail.jsx`, `lib/cifMock.js`, `lib/db.js`,
`components/AppShell.jsx`, `App.js`, `docs/UX_FRAMEWORK.md`, `design_guidelines.json`, `memory/PRD.md`.
