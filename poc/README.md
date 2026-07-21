# poc — Proof of Concept

A minimal, offline demonstration that the CIF knowledge base is **functional**: input a new project →
match it against the curated dataset (analogs + patterns) → output a prediction and a ready-to-save
`tracking/<project>/prediction.md`.

This is the **Hybrid read-path** from the architecture: deterministic code turns the repo's markdown into
structured data; the app reads that data. (Reasoning stays rule-based here — an LLM layer is the next step.)

## Files

```
poc/
├── intake.html    # the PoC UI (open in a browser)
├── data.js        # AUTO-GENERATED: window.CIF = {projects, patterns, meta}
├── projects.json  # AUTO-GENERATED project roster + tags
└── patterns.json  # AUTO-GENERATED pattern catalogue
```

## How to run

1. Build the data from the repo (deterministic, no LLM/API):
   ```
   python3 tools/build_json.py
   ```
   This reads `examples/DatasetIndex.md` (roster + content-derived tags) and `examples/PatternRegistry.md`
   (patterns) and writes `poc/data.js` + the two JSON files.
2. Open `poc/intake.html` in a browser (works from `file://` — `data.js` is a plain script include, no server).
3. Fill the form and click **Analyze → Tracking**.

## Try this

Category **Restaking / LRT** · stage **Points campaign** · tick **airdrop + points + looping + liquid-restaking**
→ pulls analogs **EigenLayer / ether.fi**, fires **P2 (rehypothecation → cascading failure, validated by Renzo)**
and **P4 (airdrop → dump)**, confidence **HIGH**, and generates the tracking prediction.

## Data source of truth

Nothing here is hand-maintained data — re-run `./run.sh` (or `tools/build_json.py`) after any ingest and the
PoC reflects the current repo. Patterns are edited in `examples/PatternRegistry.md`; projects come from
`examples/DatasetIndex.md` + auto-discovered `examples/CaseStudies/`; sentiment from `examples/Sentiment/`.

## Consuming the data (for LLMs / apps that need tracking · signal · prediction)

`poc/cif.json` is a single self-describing bundle (`data.js` is the same, wrapped as `window.CIF`). Schema
`cif-export/1`:

```jsonc
{
  "meta":     { "schema", "generated", "projects", "deep", "summary", "sentiment", "patterns", "source" },
  "projects": [ { "n": name, "tier": "Deep|Summary", "file", "cat", "era",
                  "tags": [ … ],           // content-derived mechanics tags (analog matching)
                  "sentiment": "examples/Sentiment/<P>.md"   // present only if a companion exists
                } ],
  "patterns": [ { "id", "nm", "triggers": [ … ], "instances", "confidence": "HIGH|MEDIUM|LOW",
                  "analogs": [ … ], "src", "val", "pred", "watch": [ … ] } ],
  "sentiment":[ { "project", "file" } ]
}
```

Typical use: given a new project's `{category, tags}`, an app/LLM (1) retrieves analog `projects` by tag
overlap, (2) fires `patterns` whose `triggers` intersect the tags → `pred` + `confidence` + `watch`, (3) reads
the linked `file`s for deep causal + sentiment context. This is exactly what `intake.html` does and what
`tools/backtest.py` scores. Also emitted: `projects.json`, `patterns.json`, `sentiment.json` (the same data,
split) for pipelines that want one concern at a time.
