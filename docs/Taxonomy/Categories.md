# Categories

## Purpose

Specify how knowledge about **the category vocabulary** must be captured, structured, and validated within CIF's Taxonomy layer (Ontology (Stage 3) — controlled vocabulary).

## Description

This file is a documentation container only. It defines *how* knowledge must be captured — it must not contain knowledge, real project data, examples, or history. Actual content is produced downstream by Deep Research and inserted under this specification. It scopes exactly what belongs to the category vocabulary and nothing else, so the knowledge model stays modular and machine-readable.

## Why This File Exists

Within the pipeline (Research → Knowledge → Ontology → Patterns → Reasoning → Framework → Applications), the category vocabulary is a distinct unit that must be captured explicitly so downstream stages can reason over it consistently and traceably.

## Data Source

Curated by maintainers, informed by research; a controlled vocabulary.

## Required Content

The following must eventually be filled by research (documentation of fields only, not values):

- Category id
- Parent sector
- Definition
- Typical sub-categories

## Data Structure

Controlled-vocabulary lists: each term defined with an id, label, definition, and parent.

## Validation Rules

- Terms must be unique and stable.
- Each term needs a definition.
- Hierarchy must be explicit.
- No project instances stored here.

## Used By

Ontology classification fields, Reasoning, and Schema.

## Related Files

`docs/Ontology/Classification.md`, other Taxonomy files, `docs/Schema/*`.

## Future Expansion

New sectors, categories, chains, and technologies as the market evolves.
