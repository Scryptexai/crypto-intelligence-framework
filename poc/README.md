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

Nothing here is hand-maintained data — re-run `tools/build_json.py` after any ingest and the PoC reflects the
current repo. Patterns are edited in `examples/PatternRegistry.md`; projects come from `examples/DatasetIndex.md`.
