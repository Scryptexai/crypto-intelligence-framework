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
2. Run each phase **in dependency order**. Before pasting a phase's prompt, paste the **previous phase's
   finished output** into the same chat/context as reference material — later phases depend on earlier ones
   (see `Deep-Research-Brief.md` "Format v3" for why this order, not topic order).
3. Export each phase's raw output as its own `.docx`, named so the phase key is a substring
   (e.g. `03-history.docx`) — see `doc_backup/inbox/README.md`. Drop all of a project's phase files into
   `doc_backup/inbox/phased/<ProjectName>/` and run `./run.sh` — `tools/ingest.py` assembles them
   automatically, no LLM needed for that step.
4. Every prompt below shares the same closing/format rules — defined once, not repeated per phase.

## Shared rules (apply to every phase prompt)

Append this block to **every** phase prompt before sending it:

```
FORMAT RULES (apply to your entire answer):
- Output as Label: Value bullets. No tables — a table's row/column association is lost on export; a flat
  bullet list is not.
- One fact per line. Full dates, numbers with units. Never round away or drop a figure.
- Never fabricate. If something is unknown or unverifiable, write "unknown" — do not guess, do not infer
  silently, do not fill a gap with a plausible-sounding but unsourced claim.
- Where a claim is contested by different sources, note it explicitly ("Source A says X, Source B says Y") —
  do not silently pick one.
- Cite a source (name/URL/document) for each non-obvious fact where you can.
- Do not analyze, conclude, or speculate about causality beyond what THIS phase's task asks for — later
  phases handle synthesis; this phase's job is narrower than that.
- Begin your output with: PROJECT: <Name>
- End your output with a heading "Open Threads" followed by a bullet list of anything you found uncertain,
  contradictory, or worth a deeper look — hand it to the next phase instead of guessing it closed.
```

---

## Track A — Large / Anchor Projects (full 11 phases)

Use for projects with substantial history and complexity: Ethereum, Solana, BNB Chain, Avalanche, Polkadot,
Cosmos, and comparable anchor projects. Each phase below is a separate prompt — paste the prior phase's
finished output as context before running the next one.

### Phase 1 — Foundation Intelligence
```
You are a crypto research investigator building a factual foundation dossier on <PROJECT NAME>. This phase
collects FACTS ONLY — no analysis, no interpretation, no "why."

Research and report:
- Official Name, Symbol/Ticker
- Category (e.g. L1, L2, DeFi, DePIN, restaking, modular DA — be specific)
- Founding entity/company (legal name, jurisdiction if known)
- Founder(s) and core team (names, roles; note if anonymous/pseudonymous)
- Country/jurisdiction of operation
- Launch date(s) — testnet, mainnet, TGE (whichever apply)
- Main products/modules
- Official website, repository, documentation, social handles, block explorer
- Token contract address(es) and chain(s)
- Which broader ecosystem(s) it belongs to

Do not editorialize. Do not assess quality. Just the facts, each with a source where possible.
```

### Phase 2 — Entity Intelligence
```
Using the Foundation Intelligence output above as context, build the ENTITY GRAPH for <PROJECT NAME> — every
organization, person, investor, exchange, partner, protocol, developer, product, DAO, government body, media
outlet, or research lab connected to the project.

For each entity, report:
- Entity name and type (Organization / Person / Investor / Foundation / Exchange / Partner / Protocol /
  Developer / Product / DAO / Government / Media / Research Lab)
- Relationship to the project (e.g. "led Series A", "listed token", "core contributor 2021-2023", "advisor")
- Relationship period (start, and end if applicable)
- Evidence/source

This is a GRAPH, not a causal analysis — record who is connected and how, not why or what it caused. Do not
skip entities that seem minor; a small early investor or an exited team member can matter later.
```

### Phase 3 — Historical Intelligence
```
Using the Foundation and Entity Intelligence outputs above as context, build the CHRONOLOGICAL EVENT TIMELINE
for <PROJECT NAME>. This is the FACTUAL SPINE every later phase will reference — not yet the causal depth
(alternatives considered, hidden motivations come later, in Behavioral Intelligence).

For every major event, in date order, report:
- Date
- Event (what happened)
- Trigger (what precipitated it — the immediate, observable cause, not speculation about motive)
- Decision (what was decided/done)
- Outcome (what resulted, as far as currently known)
- Evidence/source

Cover the full history from founding to present. Do not omit uncomfortable events (outages, controversies,
failed initiatives, governance disputes) — a complete timeline is the point.
```

### Phase 4 — Technology Intelligence
```
Using the prior phases' outputs as context, report the TECHNOLOGY profile of <PROJECT NAME>. Technology ONLY
— do not discuss token, market, or financial topics in this phase.

Report:
- Architecture (high-level design)
- Consensus mechanism
- Virtual machine / execution environment
- Primary languages/frameworks
- Security model and audit history
- Scalability approach and known limits
- Protocol evolution — major upgrades, in order, with what changed and why (technically)
- Current roadmap
- What, if anything, is genuinely novel vs. adapted from prior art

Note explicitly where technical claims are marketing language vs. independently verifiable (audits, published
benchmarks, on-chain data).
```

### Phase 5 — Financial Intelligence
```
Using the prior phases' outputs as context, report the FINANCIAL profile of <PROJECT NAME>. Funding and
revenue economics — not tokenomics (that's the next phase).

Report:
- Funding rounds: round type, date, amount, lead/participating investors, valuation if disclosed
- Treasury size and composition, if disclosed
- Revenue model and actual revenue figures if available
- Cash flow / burn rate, if disclosed or estimable from public data
- Token sale structure (public sale, private sale — amounts and terms, not allocation %, which is Token
  Intelligence)
- Valuation history (funding-round valuation, and market cap at key points, clearly labeled as which)
- Runway estimate if calculable from disclosed treasury + burn

Where a figure is estimated rather than disclosed, say so explicitly and show the basis for the estimate.
```

### Phase 6 — Token Intelligence
```
Using the prior phases' outputs as context, report the TOKEN/TOKENOMICS profile of <PROJECT NAME>.

Report:
- Total supply (fixed or inflationary — specify)
- Distribution breakdown by category (community, team, investors, treasury, ecosystem, etc.) with percentages
- Allocation details per category: cliff, vesting schedule
- Unlock schedule, especially TGE unlock %
- Emission schedule (if inflationary)
- Utility (what the token is actually used for — governance, fees, staking, access)
- Governance mechanism (voting power basis, quorum, timelocks)
- Inflation/deflation mechanics, including any burn mechanism
- Holder concentration (top holders, whale concentration) if measurable
- Notable token-flow patterns (large transfers, exchange flows) if relevant and sourced

If the project is pre-TGE, report planned/announced structure and explicitly flag what's still undecided.
```

### Phase 7 — Ecosystem Intelligence
```
Using the prior phases' outputs as context, report the ECOSYSTEM/EXTERNAL RELATIONSHIPS of <PROJECT NAME>.

Report:
- Integration partners and what the integration does
- Developer ecosystem — number/notable developers or teams building on it, if measurable
- Applications built on/with it
- Wallet support
- Exchange listings (beyond what Entity Intelligence already captured — focus here on breadth/tier)
- Oracle integrations
- Bridge integrations
- Infrastructure/tooling providers supporting it
- Community structure (Discord/Telegram/forum size and activity, if measurable)

Distinguish "integration announced" from "integration live and used" — many crypto partnership announcements
never ship.
```

### Phase 8 — Market Intelligence
```
Using the prior phases' outputs as context, report the MARKET profile of <PROJECT NAME>. Market only — this
is not the place to explain WHY (that's Behavioral Intelligence, next).

Report:
- Narrative(s) the project is associated with, and whether it originated or followed each narrative
- Direct competitors, by era (who it competed with at launch vs. now, since competitive sets shift)
- Positioning relative to competitors (claimed and actual, if they differ)
- Adoption metrics: users, active addresses, transactions, whatever is measurable and disclosed
- TVL history, if applicable, with key inflection points and dates
- Volume history, key inflection points
- Market share within its category, if calculable
- Which market cycle(s) it has operated through, and how each affected it observably

Report numbers with dates — a metric without a timestamp is not useful for later era-comparison.
```

### Phase 9 — Behavioral Intelligence
```
Using ALL prior phases' outputs as context — especially the Historical, Financial, and Token Intelligence —
this phase is CIF's actual causal layer. For the major decisions identified in Historical Intelligence
(phase 3), answer:

- WHY was this decision made? (motivation)
- What CONSTRAINED the options available at the time? (runway, technical debt, regulatory exposure, team
  size)
- What EXTERNAL PRESSURE acted on the decision? (VC expectations, competitive threat, community demand)
- What TRADE-OFF was accepted — what was given up by choosing this path?
- What ALTERNATIVE(S) were considered or plausibly available, and why were they not chosen?
- What was the team's STATED or evidenced EXPECTATION of the outcome, and how did that compare to what
  actually happened?

Ground every answer in a statement, interview, governance post, or strongly-evidenced inference — and
explicitly label which of those it is. If you cannot ground an answer, write "unknown" rather than
speculating. This phase explains the Historical Intelligence timeline; it does not re-derive it.
```

### Phase 10 — Knowledge Extraction
```
Using ALL prior phases' outputs as context, extract MACHINE-READABLE knowledge candidates from everything
gathered on <PROJECT NAME> so far:

- Entities and relationships not yet captured in Entity Intelligence but implied elsewhere
- Pattern candidates: a repeatable decision-shape observed in this project's history that might generalize to
  other projects (name it, describe the shape, cite the specific decision event(s) it's drawn from)
- Facts that look like they could become a transferable "rule" (a condition → outcome pattern) vs. facts that
  are specific to this project only
- For each pattern candidate, note what would need to be true of ANOTHER project for this pattern to apply
  (the scope/conditions, not just the mechanic)

Do not invent patterns from a single ungrounded guess — every candidate must trace to at least one concrete,
already-reported event or fact.
```

### Phase 11 — Conflict Resolution
```
This is a MERGE-ONLY pass. Do not research anything new. Re-read all prior phase outputs for <PROJECT NAME>
provided as context, and identify every place where:
- Two phases (or two sources within one phase) report different figures for the same fact (funding amount,
  dates, supply numbers, unlock percentages, etc.)
- A claim in one phase is contradicted, complicated, or cast in doubt by something in another phase
- An "Open Thread" from an earlier phase was never actually resolved by a later one

For each conflict found, report it as:
INKONSISTENSI: <what conflicts> — Source A: <value/claim> vs Source B: <value/claim> — Evidence Level: LOW
(unless one source is clearly more authoritative, in which case say why and use MEDIUM)

Do not silently resolve a conflict by picking one side — flag it. If you find no conflicts, say so explicitly
rather than omitting this phase's output.
```

---

## Track B — Small / Young Projects (condensed, 7 phases)

Use for projects with thin history: pre-TGE, under ~1 year old, few entities, limited market data. The
dependency order is unchanged; phases are merged where a young project genuinely doesn't have enough material
to justify a separate pass — merging is about proportionality, not about skipping rigor.

### Phase 1 — Foundation & Entity Intelligence
```
You are a crypto research investigator building a factual foundation dossier on <PROJECT NAME>, a young/small
project. This phase collects FACTS ONLY — no analysis.

Part A — Foundation: Official Name, Symbol, Category, founding entity, founders/core team, country, launch
date(s), main products, website/repo/docs/socials/explorer, token contract + chain, ecosystem.

Part B — Entity graph: every organization, person, investor, exchange, partner, protocol, developer, DAO, or
advisor connected to the project so far. For each: name, type, relationship, period, evidence.

A young project's entity list is naturally short — report exactly what exists, don't pad it, and don't treat
a short list as incomplete research.
```

### Phase 2 — Historical Intelligence
```
Using the Foundation & Entity output above as context, build the CHRONOLOGICAL EVENT TIMELINE for
<PROJECT NAME> from founding to now. For each event: Date, Event, Trigger, Decision, Outcome, Evidence. A
young project may have few events — report them completely rather than manufacturing filler ones. This is
the factual spine; causal depth comes later (Behavioral Intelligence).
```

### Phase 3 — Technology Intelligence
```
Using the prior phases' outputs as context, report the TECHNOLOGY profile of <PROJECT NAME>: architecture,
consensus (if applicable), execution environment, languages/frameworks, security model and audit status,
scalability approach, roadmap. Technology only — no token/market/financial topics here. For a young project,
be explicit about what's live vs. only planned/announced.
```

### Phase 4 — Financial & Token Intelligence
```
Using the prior phases' outputs as context, report BOTH the financial and token profile of <PROJECT NAME> —
these are merged here because a pre-TGE/young project's funding and token design are tightly coupled and
usually thin enough to cover together.

Financial: funding rounds (type, date, amount, investors, valuation if disclosed), treasury, revenue model
(if any yet), token sale structure.

Token: total supply, planned/actual distribution %, allocation cliffs/vesting, unlock schedule (especially
planned TGE unlock), emission, utility, governance mechanism.

If pre-TGE, report planned/announced structure and flag explicitly what's still undecided — do not present a
plan as if it were finalized.
```

### Phase 5 — Ecosystem & Market Intelligence
```
Using the prior phases' outputs as context, report BOTH the ecosystem and market profile of <PROJECT NAME> —
merged here because a young project's external relationships and market position are usually one story, not
two.

Ecosystem: integration partners (live vs. announced-only), developer ecosystem, wallet support, exchange
listings, community size/activity.

Market: narrative(s) associated with it, direct competitors, positioning, adoption metrics (with dates),
TVL/volume if applicable, which market cycle it's operating in.
```

### Phase 6 — Behavioral Intelligence
```
Using ALL prior phases' outputs as context, this phase is CIF's actual causal layer — do not compress this
one even though the project is young. For the decisions identified in Historical Intelligence, answer: WHY
was each decision made (motivation)? What CONSTRAINED the options? What PRESSURE acted on it? What TRADE-OFF
was accepted? What ALTERNATIVE(S) existed and why weren't they chosen? What did the team EXPECT to happen?

Ground every answer in a statement, interview, or strongly-evidenced inference, labeled as such. Write
"unknown" rather than speculate. A young project's decisions matter just as much causally as an old one's —
this is not the phase to shorten.
```

### Phase 7 — Knowledge & Conflict Synthesis
```
This merges Knowledge Extraction and Conflict Resolution into one closing pass, appropriate for a project
with a smaller total body of research to reconcile.

Part A — Knowledge Extraction: from everything gathered, extract pattern candidates (a repeatable
decision-shape that might generalize), each traced to a specific reported event, with the conditions under
which it would apply to another project.

Part B — Conflict Resolution (merge-only, no new research): re-read all prior phase outputs and flag every
place two sources disagree, or an earlier Open Thread was never resolved. Format each as:
INKONSISTENSI: <what conflicts> — Source A vs Source B — Evidence Level: LOW (or MEDIUM if one source is
clearly more authoritative — say why).

If no conflicts are found, say so explicitly.
```

## Related Files

`docs/Protocol/Deep-Research-Brief.md` (the "Format v3 — Dependency Pipeline" section this operationalizes),
`docs/Ontology/DecisionEvent.md`, `docs/Ontology/Context.md`, `docs/Ontology/Hidden.md`,
`docs/Ontology/Relationships.md`, `tools/ingest.py` (`process_phased_project`), `doc_backup/inbox/README.md`.
