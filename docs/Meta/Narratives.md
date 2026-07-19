# Narratives

## Purpose

Specify how knowledge about **market narratives and how they are modelled** must be captured, structured, and validated within CIF's Meta / market-narrative layer (Ontology (Stage 3) — meta layer).

## Description

This file is a documentation container only. It defines *how* knowledge must be captured — it must not contain knowledge, real project data, examples, or history. Actual content is produced downstream by Deep Research and inserted under this specification. It scopes exactly what belongs to market narratives and how they are modelled and nothing else, so the knowledge model stays modular and machine-readable.

## Why This File Exists

Within the pipeline (Research → Knowledge → Ontology → Patterns → Reasoning → Framework → Applications), market narratives and how they are modelled is a distinct unit that must be captured explicitly so downstream stages can reason over it consistently and traceably.

## Data Source

Research on market narratives, cycles, and attention.

## Required Content

The following must eventually be filled by research (documentation of fields only, not values):

- Narrative id/label
- Definition
- Associated sectors
- Lifecycle stage reference

## Data Structure

Field specification for narrative/market meta-attributes.

## Validation Rules

- Define concepts and fields, not live market calls.
- Reference Taxonomy where relevant.
- No dated market data stored.
- Fields must be measurable or classifiable.

## Used By

Reasoning, Patterns, and Valuation layers.

## Related Files

`docs/Patterns/Narrative.md`, `docs/Reasoning/*`, other Meta files.

## Future Expansion

Sentiment feeds, attention metrics, and cycle indicators.
