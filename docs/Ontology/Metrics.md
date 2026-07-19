# Metrics

## Purpose

Specify how knowledge about **the quantitative metrics tracked per project** must be captured, structured, and validated within CIF's Ontology layer (Ontology (Stage 3)).

## Description

This file is a documentation container only. It defines *how* knowledge must be captured — it must not contain knowledge, real project data, examples, or history. Actual content is produced downstream by Deep Research and inserted under this specification. It scopes exactly what belongs to the quantitative metrics tracked per project and nothing else, so the knowledge model stays modular and machine-readable.

## Why This File Exists

Within the pipeline (Research → Knowledge → Ontology → Patterns → Reasoning → Framework → Applications), the quantitative metrics tracked per project is a distinct unit that must be captured explicitly so downstream stages can reason over it consistently and traceably.

## Data Source

Normalized entities produced by the Extraction layer.

## Required Content

The following must eventually be filled by research (documentation of fields only, not values):

- Metric definitions
- Units
- Source of each metric
- Update frequency

## Data Structure

Field specification: each attribute defined with type, allowed values, and source.

## Validation Rules

- Each field must have a defined type.
- Allowed values must reference Taxonomy where applicable.
- No real project values may be stored.
- Fields must be traceable to a source.

## Used By

Patterns, Reasoning, and Schema layers.

## Related Files

Other files in `docs/Ontology/`, `docs/Taxonomy/*`, `docs/Schema/OntologySchema.md`.

## Future Expansion

Additional entity dimensions and richer relationship modelling.
