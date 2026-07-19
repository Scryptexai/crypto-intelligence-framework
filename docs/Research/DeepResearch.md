# DeepResearch

## Purpose

Specify how knowledge about **how Deep Research (Gemini) is directed and consumed** must be captured, structured, and validated within CIF's Research layer (Research (Stage 1)).

## Description

This file is a documentation container only. It defines *how* knowledge must be captured — it must not contain knowledge, real project data, examples, or history. Actual content is produced downstream by Deep Research and inserted under this specification. It scopes exactly what belongs to how Deep Research (Gemini) is directed and consumed and nothing else, so the knowledge model stays modular and machine-readable.

## Why This File Exists

Within the pipeline (Research → Knowledge → Ontology → Patterns → Reasoning → Framework → Applications), how Deep Research (Gemini) is directed and consumed is a distinct unit that must be captured explicitly so downstream stages can reason over it consistently and traceably.

## Data Source

Deep Research (Gemini) and the primary/secondary sources it consults.

## Required Content

The following must eventually be filled by research (documentation of fields only, not values):

- Prompt/brief structure
- Expected output shape
- Quality expectations
- Integration point with the repo

## Data Structure

Methodology documentation describing process, inputs, and outputs.

## Validation Rules

- Must describe method, not findings.
- Must define source reliability handling.
- Must be reproducible.
- Must not embed real research results.

## Used By

The Extraction layer and quality-control reviewers.

## Related Files

`docs/Extraction/*` and `docs/Schema/*`.

## Future Expansion

Automated collectors, source-scoring, and provenance tracking can be documented here.
