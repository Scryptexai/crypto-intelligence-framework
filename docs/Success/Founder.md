# Founder

## Purpose

Specify how knowledge about **the founder-quality factor** must be captured, structured, and validated within CIF's Success-factor layer (Patterns (Stage 4) — success factors).

## Description

This file is a documentation container only. It defines *how* knowledge must be captured — it must not contain knowledge, real project data, examples, or history. Actual content is produced downstream by Deep Research and inserted under this specification. It scopes exactly what belongs to the founder-quality factor and nothing else, so the knowledge model stays modular and machine-readable.

## Why This File Exists

Within the pipeline (Research → Knowledge → Ontology → Patterns → Reasoning → Framework → Applications), the founder-quality factor is a distinct unit that must be captured explicitly so downstream stages can reason over it consistently and traceably.

## Data Source

Ontology attributes plus outcome research.

## Required Content

The following must eventually be filled by research (documentation of fields only, not values):

- Founder signals
- Track-record fields
- Network fields
- Evidence

## Data Structure

Field specification for one success factor.

## Validation Rules

- Define the factor and its signals, not outcomes of real projects.
- Signals must be observable.
- No project instances.
- Link outcomes to evidence fields.

## Used By

Reasoning, Valuation, and ExitStrategy layers.

## Related Files

Other Success files, `docs/Ontology/Success.md`, `docs/Reasoning/Scoring.md`.

## Future Expansion

Additional success factors and quantified signal inputs.
