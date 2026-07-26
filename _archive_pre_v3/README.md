# _archive_pre_v3/ — pre-reset dataset (2026-07-26)

Everything here predates the Format v3 phased research pipeline (`docs/Protocol/Phased-Research-Prompts.md`,
proven out on LayerZero — `examples/CaseStudies/LayerZero.md`). The maintainer judged the old
single-mega-prompt Deep Research process these were built with (22-section / Causal Event Graph v2 formats)
insufficiently rigorous — inconsistent, incomplete, too much noise — compared to the discipline the 11-phase
pipeline demonstrated, and reset the active dataset down to LayerZero only.

**Nothing here was deleted** — every file was moved with `git mv`, preserving its original relative path
under this directory (e.g. `_archive_pre_v3/examples/CaseStudies/Ethereum.md` was
`examples/CaseStudies/Ethereum.md`). Full git history is intact either way.

## Contents

- `examples/CaseStudies/` — 12 Deep Dossiers (Ethereum, Solana, BNB Chain, Cardano, Avalanche, Polkadot,
  Cosmos, dYdX, Aave, ether.fi, EigenLayer, Celestia) + 2 cross-project analyses.
- `examples/Pioneer/` — 13 Summary/Batch profiles (Batch 01 + Batch 02).
- `doc_backup/deep/` — their raw Deep Research source files.
- `doc_backup/batch/` — the Batch 01 raw source.

## Restoring a project

`git mv` it back to its original path (mirror the structure under this directory) and re-run
`tools/build_json.py`. If it's a Deep Dossier, also add its row back to the "Deep Dossiers" table in
`examples/DatasetIndex.md`; if Summary, to the appropriate Batch table (or just let `discover_dossiers()` /
filesystem discovery in `build_json.py` pick it up automatically for Deep-tier files).

Full rationale: `examples/DatasetIndex.md`'s reset note at the top of the file, and
`doc_backup/inbox/phased/LayerZero/PROMPTS-LOG.md` for the LayerZero pipeline history that motivated it.
