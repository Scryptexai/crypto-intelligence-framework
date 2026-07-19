# Schema

## Purpose

Defines the **structural contracts** of CIF: project schema, pattern schema, ontology schema, knowledge graph, entity-relationship model, and database mapping — the shapes every knowledge file must conform to.

## Why This Folder Exists

Structure must be formalised so machines can store and query knowledge. This cross-cutting folder is the bridge between the conceptual model and any storage/serving layer.

## Source of Truth

Derived from the Ontology, Patterns, and Reasoning specifications.

## Input

The conceptual specifications in Ontology, Patterns, and Reasoning.

## Output

Formal, machine-readable structural contracts.

## Consumer

Extraction, databases, and applications.

## Folder Structure

```
Schema/
├── ProjectSchema.md    ├── KnowledgeGraph.md
├── PatternSchema.md    ├── EntityRelationship.md
├── OntologySchema.md   └── DatabaseMapping.md
```

## Workflow Position

Cross-cutting — underpins every stage of `Research → Knowledge → Ontology → Patterns → Reasoning → Framework → Applications`.

## Rules

1. Define contracts only.
2. Stay consistent with Ontology/Patterns.
3. No instance data.

## Naming Convention

`PascalCase.md`.

## Future Expansion

Concrete serialization and DDL artifacts.
