# Taxonomy

## Purpose

Holds the **controlled vocabularies** used to classify projects: sectors, categories, sub-categories, chains, ecosystems, and technologies.

## Why This Folder Exists

Consistent classification requires a fixed, shared vocabulary. This folder is that vocabulary, referenced by the Ontology instead of free text.

## Source of Truth

Curated by maintainers, informed by research; a controlled vocabulary.

## Input

Curated term lists.

## Output

Stable classification vocabularies with defined hierarchy.

## Consumer

Ontology and Reasoning layers.

## Folder Structure

```
Taxonomy/
├── Sectors.md
├── Categories.md
├── SubCategories.md
├── Chains.md
├── Ecosystems.md
└── Technologies.md
```

## Workflow Position

Vocabulary backbone of the `Ontology` stage in `Research → Knowledge → Ontology → Patterns → Reasoning → Framework → Applications`.

## Rules

1. Terms only, never project instances.
2. Every term is defined and uniquely identified.
3. Hierarchy is explicit.

## Naming Convention

`PascalCase.md`, one vocabulary per file.

## Future Expansion

Expandable term lists and multi-language labels.
