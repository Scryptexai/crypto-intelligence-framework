# EntityExtraction

## Purpose

Specify how knowledge about **identification of entities (projects, people, orgs, tokens)** must be captured, structured, and validated within CIF's Extraction layer (Research → Knowledge (Stage 2)).

## Description

This file is a documentation container only. It defines *how* knowledge must be captured — it must not contain knowledge, real project data, examples, or history. Actual content is produced downstream by Deep Research and inserted under this specification. It scopes exactly what belongs to identification of entities (projects, people, orgs, tokens) and nothing else, so the knowledge model stays modular and machine-readable.

## Why This File Exists

Within the pipeline (Research → Knowledge → Ontology → Patterns → Reasoning → Framework → Applications), identification of entities (projects, people, orgs, tokens) is a distinct unit that must be captured explicitly so downstream stages can reason over it consistently and traceably.

## Data Source

Verified research artifacts produced by the Research layer.

## Required Content

The following must eventually be filled by research (documentation of fields only, not values):

- Entity types
- Disambiguation rules
- Identifier assignment
- Link to Ontology/Identity

## Data Structure

Methodology documentation for turning documents into structured entities.

## Validation Rules

- Must describe extraction rules, not extracted data.
- Must map outputs to ontology/schema fields.
- Must define normalization consistently.
- Must not store extracted values.

## Used By

The Ontology, Taxonomy, and Schema layers.

## Related Files

`docs/Ontology/*`, `docs/Schema/*`, `docs/Research/*`.

## Future Expansion

Model-based extractors, image/OCR pipelines, and confidence scoring per field.
