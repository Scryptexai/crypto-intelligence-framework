# CategoryCreator

## Purpose

Specify how knowledge about **the category-creator assessment** must be captured, structured, and validated within CIF's Innovation assessment layer (Patterns (Stage 4) — assessment).

## Description

This file is a documentation container only. It defines *how* knowledge must be captured — it must not contain knowledge, real project data, examples, or history. Actual content is produced downstream by Deep Research and inserted under this specification. It scopes exactly what belongs to the category-creator assessment and nothing else, so the knowledge model stays modular and machine-readable.

## Why This File Exists

Within the pipeline (Research → Knowledge → Ontology → Patterns → Reasoning → Framework → Applications), the category-creator assessment is a distinct unit that must be captured explicitly so downstream stages can reason over it consistently and traceably.

## Data Source

Ontology attributes plus research on competitive landscape.

## Required Content

The following must eventually be filled by research (documentation of fields only, not values):

- Definition
- Qualifying criteria
- Category reference
- Evidence fields

## Data Structure

Field specification for one innovation dimension.

## Validation Rules

- Define assessment criteria, not verdicts on real projects.
- Criteria must be reusable across projects.
- No project instances stored.
- Scoring inputs must be explicit.

## Used By

Reasoning and Valuation layers.

## Related Files

`docs/Ontology/Innovation.md`, other Innovation files, `docs/Reasoning/Scoring.md`.

## Future Expansion

Additional innovation lenses and automated scoring inputs.
