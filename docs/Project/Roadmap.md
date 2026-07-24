# Roadmap

## Purpose

Specify how knowledge about **the planned evolution of the framework structure** must be captured, structured, and validated within CIF's Project meta layer (Meta / Foundational).

## Description

This file is a documentation container only. It defines *how* knowledge must be captured — it must not contain knowledge, real project data, examples, or history. Actual content is produced downstream by Deep Research and inserted under this specification. It scopes exactly what belongs to the planned evolution of the framework structure and nothing else, so the knowledge model stays modular and machine-readable.

## Why This File Exists

Within the pipeline (Research → Knowledge → Ontology → Patterns → Reasoning → Framework → Applications), the planned evolution of the framework structure is a distinct unit that must be captured explicitly so downstream stages can reason over it consistently and traceably.

## Data Source

Authored by the CIF maintainers. Not derived from research.

## Required Content

The following must eventually be filled by research (documentation of fields only, not values):

- Planned phases (structure only)
- Sequencing of layers
- Dependencies between phases
- Definition of done per phase

## Data Structure

Prose documentation with clearly headed sections.

## Validation Rules

- Must describe intent, not knowledge.
- Must stay consistent with the documented pipeline.
- Must not contain project/case data.
- Must be human-readable and unambiguous.

## Used By

All contributors and AI agents that need to understand CIF's intent and boundaries.

## Related Files

Sibling files in `docs/Project/` and the root `README.md`.

## Future Expansion

May grow as governance, licensing, and contribution processes mature.

## Application-layer roadmap (filled — 2026-07-24)

The `Applications` stage of the pipeline has a locked phase plan: see `docs/Project/ApplicationBlueprint.md`
§6 for the full phase table (0=knowledge pipeline, done; 1=trust UI + hybrid identification; 2=Supabase sync;
3=AirdropOS integration; 4=public track-record page). This section stays a pointer, not a duplicate — update
the blueprint file when phases change, not this line.
