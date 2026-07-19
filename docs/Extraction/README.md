# Extraction

## Purpose

Documents **Stage 2**: converting verified research into structured, normalized entities, metadata, and patterns that the ontology can hold.

## Why This Folder Exists

Raw research is unstructured. Extraction defines exactly how it becomes typed, normalized data so the knowledge model can consume it reliably.

## Source of Truth

Verified research artifacts produced by the Research layer.

## Input

Verified research documents and media.

## Output

Structured entities, metadata, and normalized fields aligned to the schema.

## Consumer

Ontology and Schema layers.

## Folder Structure

```
Extraction/
├── DocumentExtraction.md
├── EntityExtraction.md
├── MetadataExtraction.md
├── PatternExtraction.md
├── ImageExtraction.md
└── Normalization.md
```

## Workflow Position

The `Research → Knowledge` bridge in `Research → Knowledge → Ontology → Patterns → Reasoning → Framework → Applications`.

## Rules

1. Describe how to extract, never what was extracted.
2. Always map to ontology/schema fields.
3. Normalize consistently.

## Naming Convention

`PascalCase.md`.

## Future Expansion

Automated extraction models and per-field confidence scoring.
