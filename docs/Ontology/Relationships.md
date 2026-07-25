# Relationships

## Purpose

Specify how knowledge about **the entities connected to a project, and the project's relationship to each**
must be captured — organizations, people, investors, exchanges, partners, protocols, developers, products,
DAOs, government bodies, media, and research labs — as a relational graph, not free text buried inside prose
sections.

## Description

This file is a documentation container only. It defines *how* entities and their relationships must be
captured — it must not contain real project data. Actual content is produced downstream by the
**Entity Intelligence** research phase (`docs/Protocol/Deep-Research-Brief.md`) and inserted under this
specification.

## Why This File Exists

A project is never isolated — its behavior is shaped by who it's connected to: which VCs funded it, which
exchanges listed it, which protocols it integrates, which people left or joined. Before this file was filled,
that information lived scattered across `Funding.md`-adjacent prose and dossier narrative, with no queryable
relationship structure. Extracting entities as a distinct graph — **before** the causal/historical layers are
built (`docs/Ontology/DecisionEvent.md`) — means later research phases can reference a stable cast of named
entities instead of re-describing "a VC" or "an exchange" inline every time.

## Data Source

Deep dossiers — the `Entity Intelligence` research phase output, run *after* Foundation Intelligence (the
entity graph needs the project's own identity fixed first) and *before* Historical Intelligence (decision
events reference entities by name, e.g. "Investor X led the Series A that triggered Decision Y").

## Required Content

The following must eventually be filled by research (documentation of fields only, not values):

- **Entity name** and **entity type** — one of: Organization, Person, Investor, Foundation, Exchange, Partner,
  Protocol, Developer, Product, DAO, Government, Media, Research Lab.
- **Relationship to the project** — e.g. "led Series A", "listed token", "co-developed module", "advisor".
- **Relationship period** — when the relationship started (and ended, if applicable) — required so later
  phases can place an entity correctly against the project's timeline.
- **Evidence** — the source grounding the relationship (never invented).

## Data Structure

```
Entity:
  name: text
  type: Organization | Person | Investor | Foundation | Exchange | Partner | Protocol | Developer | Product
        | DAO | Government | Media | Research Lab
  relationship: text (free-form, e.g. "led Series A", "core contributor 2021-2023")
  period: text | unknown
  exposure_type: financial-collateral | shared-investor-only | technical-integration | liquidity-dependency
                 | narrative-correlated-only | unknown
  evidence: <citation/quote reference>
```

**`exposure_type`** (added 2026-07-25) exists for **cross-project contagion mapping** — the question "if this
entity fails, which other projects in the dataset are actually at risk, not just loosely associated?" A
project sharing an investor with a failed project is weak/irrelevant coupling; a project holding a failed
project's token as treasury collateral, or depending on it for critical liquidity/infrastructure, is real
transmission risk. Without this field every entity graph collapses into "everyone is connected to everyone,"
which is noise, not signal (Terra/Luna → FTX → BTC contagion is real and mappable *because* the transmission
channels were specific and identifiable, not because everything in crypto is vaguely related).

- **financial-collateral** — holds/held the entity's token/asset as treasury, collateral, or reserve backing.
- **technical-integration** — depends on the entity's infrastructure to function (a bridge, an oracle, a DA
  layer, an execution environment).
- **liquidity-dependency** — the entity is/was a primary liquidity venue or market-maker relationship.
- **shared-investor-only** — same investor(s) appear in both cap tables; no operational dependency exists.
- **narrative-correlated-only** — grouped by market narrative/sector only (e.g. "both are restaking"), not by
  any actual operational or financial link.
- **unknown** — relationship exists but exposure type isn't yet determined; do not guess.

## Validation Rules

- Entity Intelligence is a **graph, not causal analysis** — record *who is connected and how*, not *why* or
  *what it caused*. Causal interpretation belongs to `docs/Ontology/DecisionEvent.md` (history) and
  `docs/Ontology/Hidden.md` (behavioral), which reference entities by name once this graph exists.
- Never invent an entity or relationship; every entry must be source-grounded.
- An entity discovered in a later research phase (e.g. a partner surfaced during Ecosystem Intelligence)
  should be added back here rather than left only in that phase's own notes — this file is the single
  reference list, not one of several.
- `exposure_type` must be the **strongest applicable** category, not the most convenient one — a relationship
  that is both "shared-investor" and "technical-integration" is recorded as `technical-integration` (the
  stronger, actually-consequential link), not left at the weaker label.

## Used By

`docs/Ontology/DecisionEvent.md` (entities referenced by name in Trigger/Decision/Alternatives fields),
`docs/Ontology/Hidden.md` (an entity's incentives can explain a Hidden factor — e.g. VC pressure),
`docs/Ontology/Funding.md` (Investor-type entities overlap with funding records — cross-link, don't duplicate).

## Related Files

`docs/Ontology/Identity.md`, `docs/Ontology/Team.md`, `docs/Ontology/Funding.md`, `docs/Ontology/DecisionEvent.md`.

## Future Expansion

A canonical entity registry shared *across* projects (so "a16z" or "Coinbase" resolve to the same entity
record everywhere they appear) once enough dossiers make cross-project entity overlap common enough to matter.
