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
  evidence: <citation/quote reference>
```

## Validation Rules

- Entity Intelligence is a **graph, not causal analysis** — record *who is connected and how*, not *why* or
  *what it caused*. Causal interpretation belongs to `docs/Ontology/DecisionEvent.md` (history) and
  `docs/Ontology/Hidden.md` (behavioral), which reference entities by name once this graph exists.
- Never invent an entity or relationship; every entry must be source-grounded.
- An entity discovered in a later research phase (e.g. a partner surfaced during Ecosystem Intelligence)
  should be added back here rather than left only in that phase's own notes — this file is the single
  reference list, not one of several.

## Used By

`docs/Ontology/DecisionEvent.md` (entities referenced by name in Trigger/Decision/Alternatives fields),
`docs/Ontology/Hidden.md` (an entity's incentives can explain a Hidden factor — e.g. VC pressure),
`docs/Ontology/Funding.md` (Investor-type entities overlap with funding records — cross-link, don't duplicate).

## Related Files

`docs/Ontology/Identity.md`, `docs/Ontology/Team.md`, `docs/Ontology/Funding.md`, `docs/Ontology/DecisionEvent.md`.

## Future Expansion

A canonical entity registry shared *across* projects (so "a16z" or "Coinbase" resolve to the same entity
record everywhere they appear) once enough dossiers make cross-project entity overlap common enough to matter.
