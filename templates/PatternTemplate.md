# PatternTemplate

## Purpose

Specify how knowledge about **the template for capturing a pattern** must be captured, structured, and validated within CIF's Templates layer (Tooling for Research → Knowledge capture).

## Description

This file is a documentation container only. It defines *how* knowledge must be captured — it must not contain knowledge, real project data, examples, or history. Actual content is produced downstream by Deep Research and inserted under this specification. It scopes exactly what belongs to the template for capturing a pattern and nothing else, so the knowledge model stays modular and machine-readable.

## Why This File Exists

Within the pipeline (Research → Knowledge → Ontology → Patterns → Reasoning → Framework → Applications), the template for capturing a pattern is a distinct unit that must be captured explicitly so downstream stages can reason over it consistently and traceably.

## Data Source

Authored by maintainers to standardise capture; not derived from research.

## Required Content

The following must eventually be filled by research (documentation of fields only, not values):

- Pattern name
- Definition fields
- Trigger/signal placeholders
- Outcome fields

## Data Structure

A section-by-section template with headed placeholders and field labels only.

## Validation Rules

- Provide structure/placeholders only.
- Must align with Schema and Ontology.
- No real data in the template.
- Every field must map to a documented dimension.

## Used By

Researchers and extraction agents who capture knowledge.

## Related Files

`docs/Schema/*`, `docs/Ontology/*`, other templates.

## Future Expansion

New templates as additional knowledge types are introduced.
