# Sentiment

## Purpose

Companion **sentiment / X-engagement dossiers** — how the community and the project *felt and communicated at
the time*, per phase. One file per project, linked both ways with its fundamental dossier in
`examples/CaseStudies/`.

## Why This Folder Exists

Fundamentals say *what happened & why*; sentiment says *how it was perceived*. Kept in a **separate module**
so the two contexts never mix. The reusable alpha is the **divergence** between them (euphoria vs weak
fundamentals → dump risk; apathy vs strong fundamentals → accumulation) — a signal fundamentals alone cannot
give, and one that is hard to replicate because point-in-time sentiment is ephemeral.

## Source of Truth

Grok/X sampling **triangulated** with archived news, forums, Wayback, and market data. Every claim carries an
evidence level and provenance (see `docs/Protocol/Sentiment-Brief.md`). Verified anchors (with URLs) are kept
separate from sampled aggregate mood; specific quotes are never fabricated.

## Input

8-section sentiment reports (`.docx`) produced per the Sentiment Brief, dropped in
`doc_backup/inbox/sentiment/`.

## Output

Per-project sentiment dossiers (`<Project>.md`, Tier: Sentiment), consumed by the reasoning/prediction layer
alongside the fundamental dossier.

## Consumer

The reasoning engine, the PoC/apps (via `poc/sentiment.json` + the bundled `poc/cif.json`), and analysts.

## Folder Structure

```
Sentiment/
└── <Project>.md   # 8 sections: overview, phase timeline, community voice, project voice,
                   #             divergence, authenticity, patterns, evidence & provenance
```

## Workflow Position

Feeds `Patterns → Reasoning` with the sentiment dimension; links to `docs/Meta/*` (Narratives, Hype,
MarketCycles) and `docs/TokenLifecycle/*`.

## Rules

1. Companion to a fundamental dossier — link both ways.
2. Verified anchors (URL) separated from sampled mood; no fabricated quotes.
3. Evidence level + provenance + capture date on every section.
4. Note the retail/hype bias of X; weight accordingly for Institution/Developer POV.

## Naming Convention

`<Project>.md` matching the fundamental dossier's project name.

## Future Expansion

Quantified sentiment scores, per-phase polarity time-series, and sentiment↔price divergence metrics.
