# Phased Research Prompts (Format v3)

## Policy note — why these live in the repo

`docs/Protocol/Deep-Research-Brief.md` states the paste-ready research prompt is kept external, in the
maintainer's local files, not in the repo. **The v3 phased prompts below are an explicit, scoped exception
(maintainer decision, 2026-07-25) — but the exception is about storage, not usage.** Actual usage is
unchanged: these are still pasted manually into Gemini (or another external research tool) exactly as before,
outside the repo, one phase at a time. What changes is only that a copy also lives here, so it (a) can't be
lost or accidentally deleted from a local machine, and (b) stays in the same place as, and in sync with, the
contract it implements (`Deep-Research-Brief.md`'s Format v3 section), the ontology it maps to, and the code
that ingests its output (`tools/ingest.py`) — one connected context instead of a prompt file sitting
disconnected from the pipeline it feeds. It is not a process change, and it does not make this file a
mandatory script to follow word-for-word forever — it's a backup with context, not new governance. The v1/v2
single-shot prompt is unaffected and stays external as before.

## How to use these

1. Pick a track: **Track A (Large/Anchor)** for projects with substantial history (Ethereum, Solana, BNB
   Chain, and similarly aged/complex projects) or **Track B (Small/Young)** for projects with thin history —
   pre-TGE, <1 year old, few entities. Track choice is a judgment call, not a hard rule; a "small" project that
   turns out to have surprising depth can graduate mid-research by picking up Track A's remaining phases.
2. **Focus on one project at a time through the whole pipeline before starting another** — see
   `examples/DatasetIndex.md` § "Phased Deep Research Queue" for the currently in-progress project and which
   phase is next. A finished foundation project is worth more than several half-finished ones.
3. Run each phase **in dependency order**. Before pasting a phase's prompt, paste the **previous phase's
   finished output** into the same chat/context as reference material — later phases depend on earlier ones
   (see `Deep-Research-Brief.md` "Format v3" for why this order, not topic order).
4. If the project already has a `examples/Sentiment/<Project>.md` companion (Grok/X), paste it as additional
   context for **Phase 8 (Market/Ecosystem) and the Conflict Resolution phase** — Gemini's research is
   secondary/aggregated evidence (what's been written about the project); Grok's is primary/live evidence
   (what the community is saying right now, with real post citations). A gap between the two — Gemini's
   sources say the community is positive, Grok's live scan says sentiment soured last week — is exactly the
   kind of `INKONSISTENSI` this pipeline exists to surface, not smooth over.
5. Export each phase's raw output as its own `.docx`, named so the phase key is a substring
   (e.g. `03-history.docx`) — see `doc_backup/inbox/README.md`. Drop all of a project's phase files into
   `doc_backup/inbox/phased/<ProjectName>/` and run `./run.sh` — `tools/ingest.py` assembles them
   automatically, no LLM needed for that step.
6. Every prompt below shares the same closing/format rules — defined once, not repeated per phase. Every
   phase output must follow the literal template given (field names, order) — a template exists specifically
   so output is comparable across projects instead of free-form and inconsistent.

## Shared rules (apply to every phase prompt)

Append this block to **every** phase prompt before sending it:

```
FORMAT RULES (apply to your entire answer):
- Write in BAHASA INDONESIA. Keep these in their original language, untranslated: product/technology
  names (Ultra Light Node, DVN, OFT, Proof-of-Donation), people's names, company names, chain names,
  and URLs. Translating a technical term makes it unmatchable against other dossiers.
- Follow the literal output template given for this phase — same field labels, same order. Do not
  reformat as prose, do not rename fields, do not reorder them. A consistent shape across every project
  is the point; free-form answers can't be compared later.
- Output as Label: Value bullets. NO TABLES AT ALL — not even for "structured" data. A Word table
  survives extraction but flattens into an awkward two-line-per-fact shape; a flat bullet list does not.
- One fact per line. Full dates, numbers with units. Never round away or drop a figure.
- Never fabricate. If something is unknown or unverifiable, write "unknown" — do not guess, do not infer
  silently, do not fill a gap with a plausible-sounding but unsourced claim.
- Where a claim is contested by different sources, note it explicitly ("Source A says X, Source B says Y") —
  do not silently pick one.
- Attach the source to EACH FACT, on the same line — not as a bibliography at the end. A numbered source
  list at the bottom with no per-fact link is NOT acceptable: it makes every individual claim unverifiable,
  which is the one thing this framework cannot tolerate.
- Tag an Evidence Level — HIGH (multiple independent sources agree) / MEDIUM (one credible source) / LOW
  (inference, single weak source, or contested) — on every significant claim, not just in the Conflict
  Resolution phase.
- Combined, every fact line looks like: "Amount: $6.5M (HIGH) [Messari, https://...]".
- Do not analyze, conclude, or speculate about causality beyond what THIS phase's task asks for — later
  phases handle synthesis; this phase's job is narrower than that.
- Begin your output with: PROJECT: <Name>
- End your output with a heading "Open Threads" followed by a bullet list of anything you found uncertain,
  contradictory, or worth a deeper look — hand it to the next phase instead of guessing it closed.
```

---

## Track A — Large / Anchor Projects (full 11 phases)

Use for projects with substantial history and complexity: Ethereum, Solana, BNB Chain, Avalanche, Polkadot,
Cosmos, LayerZero, and comparable anchor projects. Each phase below is a separate prompt — paste the prior
phase's finished output as context before running the next one.

### Phase 1 — Foundation Intelligence
```
You are a crypto research investigator building a factual foundation dossier on <PROJECT NAME>. This phase
collects FACTS ONLY — no analysis, no interpretation, no "why."

Fill this exact template (write "unknown" for anything unverifiable — do not guess):

PROJECT: <Name>
Official Name: <value>
Symbol: <value>
Category: <value — be specific, e.g. "cross-chain messaging / interoperability", not just "infra">
Founding Entity: <legal name, jurisdiction>
Founders: <name1 (role); name2 (role); ... — or "anonymous/pseudonymous — <handle>">
Core Team: <size/notable names, or "undisclosed">
Country: <value>
Launch Date - Testnet: <date or "n/a">
Launch Date - Mainnet: <date or "n/a">
Launch Date - TGE: <date or "pre-TGE">
Main Products: <semicolon-separated list>
Official Website: <url>
Repository: <url>
Documentation: <url>
Social - X/Twitter: <handle>
Social - Discord: <invite/handle>
Social - Telegram: <handle>
Block Explorer: <url>
Token Contract: <address, chain — or "not yet deployed">
Chain(s): <value>
Ecosystem: <value>

Open Threads
- <anything uncertain>
```

### Phase 2 — Entity Intelligence
```
Using the Foundation Intelligence output above as context, build the ENTITY GRAPH for <PROJECT NAME> — every
organization, person, investor, exchange, partner, protocol, developer, product, DAO, government body, media
outlet, or research lab connected to the project. This is a GRAPH, not causal analysis — record who is
connected and how, not why or what it caused. Do not skip entities that seem minor.

For EACH entity, repeat this block:

Entity: <name>
Type: <Organization|Person|Investor|Foundation|Exchange|Partner|Protocol|Developer|Product|DAO|Government|Media|Research Lab>
Relationship: <free text, e.g. "led Series A", "core contributor 2021-2023">
Period: <start-end, or "start-present", or "unknown">
Exposure Type: <financial-collateral|technical-integration|liquidity-dependency|shared-investor-only|narrative-correlated-only|unknown>
  (financial-collateral = holds/held this project's asset as treasury/collateral; technical-integration =
  depends on this project's infrastructure to function; liquidity-dependency = primary liquidity venue;
  shared-investor-only = same investor(s), no operational link; narrative-correlated-only = same sector
  label only. Use the STRONGEST applicable category, not the most convenient one.)
Evidence: <source>
---

Open Threads
- <anything uncertain>
```

### Phase 3 — Historical Intelligence
```
Using the Foundation and Entity Intelligence outputs above as context, build the CHRONOLOGICAL EVENT TIMELINE
for <PROJECT NAME> — the FACTUAL SPINE every later phase references. Cover full history from founding to
present; do not omit uncomfortable events (outages, controversies, failed initiatives, governance disputes).

For EACH major event, in date order, repeat this block:

Date: <YYYY-MM-DD or best available precision>
Event: <short label>
Trigger: <the immediate, observable cause — not speculation about motive>
Context Snapshot (as of this date): Industry state: <...> | Competitor state: <...> | Tech maturity: <...>
  | Macro conditions: <...> | Hunter/user population (if airdrop-relevant): <...> | VC climate: <...>
  | Narrative: <...>
  (Skip any sub-field that genuinely doesn't apply, but don't skip the whole Context line — this is what
  lets later phases avoid matching this event's pattern to an incompatible era.)
Decision: <what was decided/done>
Execution: <how it was actually carried out, operationally — distinct from the decision itself>
Short-term Outcome: <effect within roughly weeks-months>
Long-term Outcome: <effect over the longer horizon, or "too early to assess">
Evidence: <source>
---

Open Threads
- <anything uncertain>
```

### Phase 4 — Technology Intelligence
```
Using the prior phases' outputs as context, report the TECHNOLOGY profile of <PROJECT NAME>. Technology ONLY
— no token/market/financial topics.

Architecture: <value>
Consensus Mechanism: <value or "n/a">
VM / Execution Environment: <value>
Languages/Frameworks: <value>
Security Model: <value>
Audit History: <auditor — date — scope; repeat per audit, or "none disclosed">
Scalability Approach: <value>
Known Limits: <value>
Protocol Evolution: <upgrade name — date — what changed technically; repeat per upgrade>
Current Roadmap: <value>
Novelty Assessment: <what's genuinely new vs. adapted from prior art, with basis>

Open Threads
- <anything uncertain>
```

### Phase 5 — Financial Intelligence
```
Using the prior phases' outputs as context, report the FINANCIAL profile of <PROJECT NAME>. Funding/revenue
economics — not tokenomics (that's Phase 6).

For EACH funding round, repeat this block:
Funding Round: <type, e.g. Seed/Series A>
  Date: <value>  Amount: <value + currency>  Lead Investor: <value>
  Participating Investors: <value>  Valuation: <value or "undisclosed">
---

Then, once:
Treasury Size: <value or "undisclosed">
Treasury Composition: <value>
Revenue Model: <value>
Revenue Figures: <value + date, or "undisclosed">
Burn Rate: <value, or "estimated as X — basis: ...", or "undisclosed">
Token Sale Structure: <public/private terms and amounts — NOT allocation %, that's Phase 6>
Runway Estimate: <value + calculation basis, or "not calculable">

Open Threads
- <anything uncertain>
```

### Phase 6 — Token Intelligence
```
Using the prior phases' outputs as context, report the TOKEN/TOKENOMICS profile of <PROJECT NAME>. If
pre-TGE, mark every field below explicitly as "planned" and flag what's still undecided.

Total Supply: <value>
Supply Type: <fixed|inflationary>
Distribution: Community <%>, Team <%>, Investors <%>, Treasury <%>, Ecosystem <%>, Other <label:%>
Allocation - Team: <cliff, vesting>
Allocation - Investors: <cliff, vesting>
Allocation - <any other category>: <cliff, vesting>
TGE Unlock: <% of total supply + which categories>
Emission Schedule: <value or "n/a — fixed supply">
Utility: <bullet-style list>
Governance Mechanism: <value>
Inflation/Deflation: <value>
Burn Mechanism: <value or "none">
Holder Concentration: <value or "not yet measurable">
Notable Token Flow: <value or "n/a">
Status: <live|planned/pre-TGE>

Open Threads
- <anything uncertain>
```

### Phase 7 — Ecosystem Intelligence
```
Using the prior phases' outputs as context, report the ECOSYSTEM/EXTERNAL RELATIONSHIPS of <PROJECT NAME>.
Distinguish "integration announced" from "integration live and used."

For EACH integration partner, repeat this block:
Integration Partner: <name>
  What it does: <value>   Status: <live|announced-only>
---

Then, once:
Developer Ecosystem: <value>
Applications Built On It: <list>
Wallet Support: <list>
Exchange Listings: <breadth/tier summary — beyond what Entity Intelligence already captured>
Oracle Integrations: <list>
Bridge Integrations: <list>
Infra/Tooling Providers: <list>
Community Size/Activity: <Discord/TG/forum numbers + date>

Open Threads
- <anything uncertain>
```

### Phase 8 — Market Intelligence
```
Using the prior phases' outputs as context, report the MARKET profile of <PROJECT NAME>. Market only — not
WHY (that's Behavioral Intelligence, next). If a `examples/Sentiment/<Project>.md` (Grok/X) companion was
provided as context, cross-check your narrative/community claims against it explicitly.

Narrative(s): <value — note originated vs. followed each>

For EACH competitor/era, repeat this block:
Competitor: <name>   Era: <when they competed>   Positioning vs. them: <value>
---

Then, once:
Adoption Metrics: <metric: value (date); repeat per metric>
TVL History: <value: date; repeat key inflection points, or "n/a">
Volume History: <value: date; repeat key inflection points>
Market Share: <value or "not calculable">
Market Cycles Operated Through: <list, with dates and observed effect on this project specifically>
Current Status: <growing|declining|stagnant|dormant|recovering> — basis: <what observation supports this>

Open Threads
- <anything uncertain, including any gap vs. the Sentiment companion if one was provided>
```

### Phase 9 — Behavioral Intelligence
```
Using ALL prior phases' outputs as context — especially Historical, Financial, and Token Intelligence — this
phase is CIF's actual causal layer. Ground every answer in a statement, interview, governance post, or
strongly-evidenced inference, labeled as such; write "unknown" rather than speculate.

For EACH major decision event from Historical Intelligence, repeat this block:

Decision Event: <name/date, matching Historical Intelligence exactly>
  Motivation: <why this decision was made, or "unknown">
  Constraint: <what limited the options — runway, tech debt, regulatory exposure, team size — or "unknown">
  Pressure: <external force acting on it — VC expectations, competitive threat, community demand — or "unknown">
  Trade-off: <what was given up by choosing this path, or "unknown">
  Alternative(s) Considered: <what else was plausibly available and why not chosen, or "unknown">
  Expectation vs. Actual: <what the team expected to happen vs. what did, or "unknown">
  Stakeholder Reactions:
    Founder: <reaction/impact or "no notable reaction">
    VC: <...>
    Retail: <...>
    Community: <...>
    Developer: <...>
    Institution: <...>
    Validator: <...>
    Builder: <...>
  Grounding: <statement | interview | governance post | strongly-evidenced inference — label which>
---

Open Threads
- <anything uncertain>
```

### Phase 10 — Knowledge Extraction
```
Using ALL prior phases' outputs as context, extract MACHINE-READABLE knowledge from everything gathered on
<PROJECT NAME>. Do not invent a pattern from a single ungrounded guess — every candidate must trace to a
concrete, already-reported event or fact.

POV Success-Matrix (project-level verdict, not per-event):
  Founder: <success|failure|mixed — reason — Evidence Level>
  VC: <...>
  Retail: <...>
  Community: <...>
  Developer: <...>
  Institution: <...>
  Validator: <...>
  Builder: <...>

Lessons Learned:
  Biggest mistake: <what — to avoid — cite the specific event>
  Biggest win: <what — to imitate — cite the specific event>

Entity/Relationship Addendum: <anything missed in Entity Intelligence, or "none">

For EACH pattern candidate, repeat this block:
Pattern Candidate: <name>
  Shape: <description of the repeatable decision-shape>
  Drawn From: <specific event(s)/fact(s) cited, by name/date>
  Applies When: <conditions under which this would transfer to another project — not just the mechanic>
---

Open Threads
- <anything uncertain>
```

### Phase 11 — Conflict Resolution
```
This is a MERGE-ONLY pass. Do not research anything new. Re-read all prior phase outputs for <PROJECT NAME>
provided as context — including a `examples/Sentiment/<Project>.md` companion if one was provided — and
identify every place where:
- Two phases (or two sources within one phase) report different figures for the same fact
- A claim in one phase is contradicted, complicated, or cast in doubt by something in another phase
- Gemini's research narrative disagrees with the Grok/Sentiment companion's live read (if provided) —
  e.g. Gemini's sources describe positive community sentiment based on older material, but the Sentiment
  companion's live X scan shows it has since soured, or vice versa
- An "Open Thread" from an earlier phase was never actually resolved by a later one

For EACH conflict found, repeat this block:
INKONSISTENSI: <what conflicts>
  Source A: <value/claim>   Source B: <value/claim>
  Evidence Level: <LOW, or MEDIUM if one source is clearly more authoritative — say why>
---

If no conflicts are found, write "No conflicts found." explicitly rather than omitting this phase's output.

Open Threads
- <only if something remains genuinely unresolved even after this pass>
```

---

## Track B — Small / Young Projects (condensed, 7 phases)

Use for projects with thin history: pre-TGE, under ~1 year old, few entities, limited market data. The
dependency order and the enrichments above (Context Snapshot, Execution, Stakeholder Reactions, POV Matrix,
Evidence Level, Current Status) all still apply — condensing means merging phases, not dropping fields.

### Phase 1 — Foundation & Entity Intelligence
```
You are a crypto research investigator building a factual foundation dossier on <PROJECT NAME>, a young/small
project. FACTS ONLY.

Part A — Foundation (fill this template):
PROJECT: <Name>
Official Name / Symbol / Category / Founding Entity / Founders / Core Team / Country: <each>
Launch Date - Testnet / Mainnet / TGE: <each, or "n/a"/"pre-TGE">
Main Products / Website / Repository / Documentation / Socials / Explorer: <each>
Token Contract / Chain(s) / Ecosystem: <each>

Part B — Entity graph (repeat per entity):
Entity: <name>   Type: <...>   Relationship: <...>   Period: <...>
Exposure Type: <financial-collateral|technical-integration|liquidity-dependency|shared-investor-only|narrative-correlated-only|unknown>
Evidence: <source>
---

A young project's entity list is naturally short — report exactly what exists, don't pad it.

Open Threads
- <anything uncertain>
```

### Phase 2 — Historical Intelligence
```
Using the Foundation & Entity output above as context, build the CHRONOLOGICAL EVENT TIMELINE for
<PROJECT NAME>. A young project may have few events — report them completely, don't manufacture filler ones.

For EACH event, repeat:
Date: <...>   Event: <...>   Trigger: <...>
Context Snapshot (as of this date): Industry/Competitor/Tech maturity/Macro/Hunter-population/VC climate/
  Narrative — <fill what applies>
Decision: <...>   Execution: <...>
Short-term Outcome: <...>   Long-term Outcome: <... or "too early to assess">
Evidence: <source>
---

Open Threads
- <anything uncertain>
```

### Phase 3 — Technology Intelligence
```
Using the prior phases' outputs as context, report the TECHNOLOGY profile of <PROJECT NAME>: Architecture,
Consensus (if applicable), VM/Execution Environment, Languages/Frameworks, Security Model, Audit Status,
Scalability Approach, Roadmap. Technology only. Be explicit about what's live vs. only planned/announced.

Open Threads
- <anything uncertain>
```

### Phase 4 — Financial & Token Intelligence
```
Using the prior phases' outputs as context, report BOTH financial and token profile of <PROJECT NAME> —
merged since a young project's funding and token design are usually thin enough to cover together.

Financial: Funding Round(s) (type/date/amount/investors/valuation, repeat per round), Treasury, Revenue Model,
Token Sale Structure.

Token: Total Supply, Distribution %, Allocation cliffs/vesting per category, TGE Unlock %, Emission, Utility,
Governance Mechanism, Status (live|planned).

If pre-TGE, mark every field "planned" explicitly and flag what's undecided.

Open Threads
- <anything uncertain>
```

### Phase 5 — Ecosystem & Market Intelligence
```
Using the prior phases' outputs as context, report BOTH ecosystem and market profile of <PROJECT NAME>.

Ecosystem: Integration Partner (name, what it does, live|announced-only — repeat per partner), Developer
Ecosystem, Wallet Support, Exchange Listings, Community Size/Activity.

Market: Narrative(s) (originated vs. followed), Competitors (repeat per competitor/era), Adoption Metrics
(with dates), TVL/Volume if applicable, Current Status (growing|declining|stagnant|dormant|recovering + basis).

If a `examples/Sentiment/<Project>.md` companion exists, cross-check community claims against it.

Open Threads
- <anything uncertain, including any gap vs. the Sentiment companion>
```

### Phase 6 — Behavioral Intelligence
```
Using ALL prior phases' outputs as context — do not compress this phase even though the project is young.

For EACH decision event from Historical Intelligence, repeat:
Decision Event: <name/date>
  Motivation / Constraint / Pressure / Trade-off / Alternative(s) Considered / Expectation vs. Actual: <each,
  or "unknown">
  Stakeholder Reactions: Founder/VC/Retail/Community/Developer/Institution/Validator/Builder — <each, or
  "no notable reaction">
  Grounding: <statement|interview|governance post|strongly-evidenced inference — label which>
---

Open Threads
- <anything uncertain>
```

### Phase 7 — Knowledge & Conflict Synthesis
```
Merges Knowledge Extraction and Conflict Resolution into one closing pass.

Part A — Knowledge Extraction:
POV Success-Matrix: Founder/VC/Retail/Community/Developer/Institution/Validator/Builder — <verdict + reason +
  Evidence Level, each>
Lessons Learned: Biggest mistake (to avoid) / Biggest win (to imitate) — cite the specific event(s).
Pattern Candidate (repeat per candidate): Name / Shape / Drawn From / Applies When.

Part B — Conflict Resolution (merge-only, no new research; include the Sentiment companion if one was
provided): repeat per conflict —
INKONSISTENSI: <what conflicts>   Source A: <...>   Source B: <...>   Evidence Level: <LOW|MEDIUM + why>
---
If no conflicts found, write "No conflicts found." explicitly.

Open Threads
- <only if something remains genuinely unresolved>
```

## Related Files

`docs/Protocol/Deep-Research-Brief.md` (the "Format v3 — Dependency Pipeline" section this operationalizes),
`docs/Ontology/DecisionEvent.md`, `docs/Ontology/Context.md`, `docs/Ontology/Hidden.md`,
`docs/Ontology/Relationships.md` (entity graph + `exposure_type`, for cross-project contagion mapping),
`examples/DatasetIndex.md` § "Phased Deep Research Queue" (progress tracking), `examples/PatternRegistry.md`,
`tools/ingest.py` (`process_phased_project`), `doc_backup/inbox/README.md`.
