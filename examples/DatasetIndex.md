# CIF Dataset Index

**Pipeline position:** Applications layer — validated knowledge produced by `Research → Extraction` and
structured against the `docs/` ontology.

> Knowledge artifacts (real curated data), not documentation containers. Each conforms to
> `templates/ProjectTemplate.md` and links back to the ontology it instantiates.

This is the master curation record for the dataset stored in `examples/`: what was added per batch,
how the taxonomy is distributed, where the gaps are, and what is queued next.

**Batches loaded:** Batch 01 (8 projects, source: Deep Research / Gemini) · Batch 02 (10 projects, source: Web research) · Deep Dossiers (12: Ethereum, Solana, BNB Chain, Cardano, Avalanche, Polkadot, Cosmos, dYdX, Aave, ether.fi, EigenLayer, Celestia — source: Deep Research / Gemini).
**Total curated projects: 26** _(D8 dYdX, D9 Aave, D11 EigenLayer and D12 Celestia supersede their Batch Summaries — same projects, not double-counted; D10 ether.fi is a new project)_.

## Curation Tiers
_How each project is captured (see `docs/Protocol/` for the runbooks)._

| Tier | What | Location | Throughput |
|------|------|----------|------------|
| **Deep** | Full causal dossier for anchor projects | `examples/CaseStudies/<Project>.md` | ~1 / session |
| **Summary** | One profile per project for breadth | `examples/Pioneer/` (or `Successful/`, `Failed/`) | ~10–15 / session |
| **Tracking** | Living record of a project being worked/followed | `tracking/<Project>/` | ongoing |

Target ~1000 projects ≈ ~50 Deep + ~950 Summary ≈ ~150 sessions (state persists in git; per-session cost is flat).

**No-overlap policy:** a project exists in exactly one tier at a time. When a Deep dossier is ingested for a
project that already has a Summary in `examples/Pioneer/`, the Summary is redundant (Deep is strictly richer)
and should be removed in the same session, once the Deep version is confirmed complete — never leave both.
`tools/ingest.py` flags this automatically (`⚠ supersedes Pioneer/<X>.md` in its output) but does not
auto-delete; removing it is a deliberate step, done here in `DatasetIndex.md` alongside the file deletion.

## V1 → V2 Upgrade Queue (policy: upgrade before delete — do not remove)

**Decision (maintainer):** the 11 Deep dossiers below are still in the v1 (22-section) format. They are kept
as-is — **not deleted** — until each is upgraded to a v1+v2 merge (same treatment as `CaseStudies/Solana.md`,
the worked example: keep everything v1 has that v2 doesn't — POV Success-Matrix, funding tables, policy
chronology — add what v2 adds — Context snapshot, explicit Decision Events, Conflicting Evidence — and flag
any cross-source discrepancy as `INKONSISTENSI` rather than silently picking one). Their `doc_backup/deep/`
v1 sources stay archived until the matching project is upgraded.

**Important operational note:** `./run.sh` / `tools/ingest.py` alone will **not** perform this upgrade — its
anti-duplicate guard (`find_existing()`) correctly *skips* a new report for a project that already has a
dossier, rather than blindly overwriting good v1 content. Merging requires the same judgment call as the
Solana rebuild, i.e. a short session per project. This queue is unrelated to net-new projects, which
`run.sh` already ingests fully automatically without a session.

| # | Project | Status | v1 source |
|---|---------|--------|-----------|
| D1 | Ethereum | ⏳ pending v2 merge | `doc_backup/deep/Ethereum_2026-07_gemini.docx` |
| D3 | BNB Chain | ⏳ pending v2 merge | `doc_backup/deep/BNBChain_2026-07_gemini.docx` |
| D4 | Cardano | ⏳ pending v2 merge | `doc_backup/deep/Cardano_2026-07_gemini.docx` |
| D5 | Avalanche | ⏳ pending v2 merge | `doc_backup/deep/Avalanche_2026-07_gemini.docx` |
| D6 | Polkadot | ⏳ pending v2 merge | `doc_backup/deep/Polkadot_2026-07_gemini.docx` |
| D7 | Cosmos | ⏳ pending v2 merge | `doc_backup/deep/Cosmos_2026-07_gemini.docx` |
| D8 | dYdX | ⏳ pending v2 merge | `doc_backup/deep/dYdX_2026-07_gemini.docx` |
| D9 | Aave | ⏳ pending v2 merge | `doc_backup/deep/Aave_2026-07_gemini.docx` |
| D10 | ether.fi | ⏳ pending v2 merge | `doc_backup/deep/EtherFi_2026-07_gemini.docx` |
| D11 | EigenLayer | ⏳ pending v2 merge | `doc_backup/deep/EigenLayer_2026-07_gemini.docx` |
| D12 | Celestia | ⏳ pending v2 merge | `doc_backup/deep/Celestia_2026-07_gemini.docx` |
| D2 | Solana | ✅ upgraded (worked example) | both v1 + v2 archived |

**When a project row above is upgraded:** flip its status to ✅, and only then is that project's specific
`doc_backup/deep/` v1 source (and any framework-level v1-format cleanup) eligible for the maintainer's
separate delete decision — evaluated per-project, not as a blanket action.

## Phased Deep Research Queue (Format v3 — in progress)

**Decision (maintainer, 2026-07-25):** focus on ONE project at a time through the full Format v3 pipeline
(`docs/Protocol/Phased-Research-Prompts.md`) before starting another — a solid foundation project first, so
later projects have a proven reference to follow rather than everyone being worked in parallel and nobody
being done properly. Tracked here so progress survives across sessions (per-phase, since a session may only
complete one phase before running out of budget).

**Candidate criteria** (why a project qualifies for this queue, not just any project): substantial
documented ecosystem collaborators/integrations (to test cross-project entity-graph and contagion mapping —
see the LayerZero↔Optimism discussion), a clear public roadmap, and enough real history to make Behavioral
Intelligence non-trivial.

| Project | Track | Phases done | Next phase | Notes |
|---------|-------|--------------|------------|-------|
| **LayerZero** | A (full 11) | 1 ✅ Foundation, 2 ✅ Entity (76 entities), 3 ⚠ Historical (15/15 events incl. 2 new from Phase 4, citations pending reformat), 4 ⚠ Technology (content excellent, citations pending reformat), 5 prompt sent — awaiting output | **3 + 4 reformats + 5 output → then 6 — Token Intelligence** | Upgrade from existing `Pioneer/LayerZero.md` (Batch 02) to Deep tier. Chosen for its interconnection-heavy ecosystem (160+ chains — strong entity-graph test case) and the ZRO airdrop (Jun 2024) as real Behavioral Intelligence material, already linked as a P4 analog in `PatternRegistry.md`. See the Phase 1/2/3/4 notes below. |

**LayerZero Phase 1 — two source files, deliberately.** The first Gemini pass returned a rich but
narrative/table-formatted report in English; a reformat pass produced a clean Indonesian Label:Value version.
A term-by-term diff of the two showed **all numeric facts survived the reformat intact** (funding rounds,
token allocations, dates, prices, percentages — the most fragile category, verified clean), but **8 items were
silently dropped**, so both files are kept:

- `doc_backup/inbox/phased/LayerZero/01-foundation.docx` — the reformatted v2, **the active phase file**
  ingest reads (parseable, Indonesian, conflicts flagged, Open Threads present).
- `doc_backup/deep/LayerZero_2026-07_phase1-narrative-v1.docx` — the original narrative pass, kept out of the
  `phased/` folder so ingest doesn't see two "foundation" files, but retained because it is the **richer**
  source of record for the items below.

**Dropped in the reformat — recovered in Phase 2** (see below): `Chainlink` (V1 Oracle provider),
`Google Cloud`, `Polyhedra`, `Chainlink CCIP` (V2 DVN options) — all four now present as entities with
`exposure_type: technical-integration`. Still open, lower priority: the "Bridging Trilemma" framing and the
Endpoint library names `SendUln302` / `ReceiveUln302` / `ReadLib1002` — Phase 4 (Technology) material.

**LayerZero Phase 1 — v2 → v3, scope-creep trim (2026-07-25, maintainer-flagged).** The maintainer noticed
the pipeline felt like it "wasn't progressing" past Entity Intelligence. Root cause, verified: v2 (the
active file above) was never actually scoped to the Foundation template — it carried ~50 fields instead of
~20, front-loading shallow one-line previews of funding rounds, ULN/DVN architecture, audit history, the
Kelp DAO incident, the FTX lawsuit, the "Zero" roadmap, and ZRO tokenomics. Phase 3 and Phase 4 then covered
every one of those topics again, in genuinely far more depth — but because Phase 1 had already telegraphed
them shallowly, the real depth added by 3 and 4 read as repetition instead of progress. Two sentences also
broke Phase 1's own "facts only, no analysis" rule (a jurisdiction-strategy interpretation and an
application-owned-security-consequence interpretation).

Trimmed directly (no new Gemini prompt needed — this was dedup/reallocation of already-existing content,
not new research):
- `doc_backup/deep/LayerZero_2026-07_phase1-outofscope-v2.docx` — the old bloated v2, archived as source of
  record (same pattern as v1 above).
- `doc_backup/inbox/phased/LayerZero/01-foundation.docx` — **now v3, the active phase file**, trimmed to the
  ~20-field template only. 17.7KB raw text → 2.5KB. Existing Evidence Level tags were preserved as-is —
  Phase 1 was, ironically, the best-cited phase of the four so far; the citation failure only started at
  Phase 3.
- Content removed because a later phase already fully supersedes it: funding rounds (→ Phase 5), ULN/DVN
  architecture + audit list + "Zero" roadmap (→ Phase 4), Kelp DAO + FTX lawsuit narrative + TGE reaction
  (→ Phase 3), OFT mechanism (→ already in Phase 4's Novelty Assessment). Content removed for being pure
  interpretation rather than fact: both analysis sentences noted above.
- Content **not yet owned by any phase** — carried forward in `PROMPTS-LOG.md` to be injected when each
  phase is drafted, not lost: ZRO Genesis Allocation %/distribution/Sybil Defense/Proof-of-Donation
  mechanism/Protocol Guild proceeds/TGE price reaction → **Phase 6**; historical message count ($80M+) and
  value transferred ($95B+) and Stargate TVL peak (~$3B) → **Phase 8**; Tether/USDT0's use of the OFT
  standard → **Phase 7**.
- This also shrinks Phase 1's footprint as the one phase that's always pasted in full into every later
  phase's Context Pack (see `Phased-Research-Prompts.md`'s point 3) — the trim directly serves that fix too,
  not just readability.

**LayerZero Phase 2 — Entity Intelligence, clean pass.** `doc_backup/inbox/phased/LayerZero/02-entity.docx`.
76 entities mapped; all 13 entities mandated by the prompt present (4 recovered from Phase 1's drop, plus
Alameda Ventures/FTX Group, Protocol Guild, Stargate, Tether, and the 5 named auditors); all 10 investors from
Phase 1's funding rounds cross-referenced. `exposure_type` distribution: 33 technical-integration, 17
shared-investor-only, 15 liquidity-dependency, 6 narrative-correlated-only, 5 financial-collateral — notably
**FTX/Alameda and FTX Recovery Trust are both tagged `financial-collateral`**, the strongest category, not
downgraded to the more convenient `shared-investor-only` — this is the entity-graph data the cross-project
contagion-mapping discussion needs.

Both open threads from Phase 1 were substantively investigated rather than left as "unknown": the
Optimistic Labs Limited / LayerZero Labs Ltd. relationship is explained in detail (still unresolved — a
genuine conflict, correctly flagged rather than guessed) and the core team headcount was found — ~58
employees (27 core engineering, 16 go-to-market), from employment-intelligence sources not used in Phase 1.

Minor format deviation (not a data-loss issue): each entity's fields are joined into one paragraph rather
than one field per line as the template specifies. Noted for the Phase 3 prompt; not worth a re-run.

**Ingest status — explicit, so this never becomes ambiguous later:**
- `poc/cif.json` **right now** still reflects only the OLD `examples/Pioneer/LayerZero.md` (Summary tier,
  Batch 02) — none of Phase 1–2's research has entered CIF's live dataset yet. This is deliberate, not an
  oversight: running `tools/ingest.py` before the Track is substantially complete would create a partial
  Deep entry in `examples/CaseStudies/` that overlaps tiers with the still-live Pioneer entry.
- **Trigger to finally ingest:** once all 11 Track A phases are done (or the maintainer explicitly decides
  fewer is "good enough" for this project). Not before.
- **Every prompt actually sent** (with LayerZero-specific injected context, not just the generic template)
  is logged verbatim in `doc_backup/inbox/phased/LayerZero/PROMPTS-LOG.md` — so the exact ask behind any
  raw output is always reconstructable, not just the output itself.
- `tools/ingest.py`'s `process_phased_project()` now detects the same cross-tier overlap `process_deep()`
  already handled for single-shot dossiers (2026-07-25 fix) — when this project is finally ingested, the
  assembled dossier will automatically get a `**Supersedes:** examples/Pioneer/LayerZero.md` note and the
  console output will flag it, exactly like the V1→V2 queue's projects do. It will **not** auto-delete the
  Pioneer file — that removal is a maintainer decision made once the Deep dossier is confirmed complete,
  same policy as the rest of this document.

**Lesson recorded for future reformat passes:** asking an LLM to reformat its own output does preserve
numbers reliably but drops incidental named entities mentioned in prose. Either diff every reformat against
the original (as done here), or instruct the reformat pass to preserve every proper noun explicitly.

**LayerZero Phase 3 — Historical Intelligence, content excellent / citations empty.**
Raw (pre-reformat) file archived at `doc_backup/deep/LayerZero_2026-07_phase3-nocitations-v1.docx` — same
pattern as Phase 1's v1/v2 split. It will **not** become the active `phased/LayerZero/03-history.docx` until
the citation reformat pass below comes back; only content-complete + citation-complete files enter the
`phased/` folder ingest reads. All 13 known events from the prompt present, in order, plus 4 valuable bonus
findings not explicitly requested: LayerZero bought back FTX's equity stake, the FTX Recovery Trust
lawsuit's Sep 2023–Mar 2024 timeline including a Motion to Dismiss, a second-order Radiant Capital exploit
(late 2024) distinct from the Kelp DAO incident, and the DVN diversification response (Nethermind/Google/
Animoca nodes) after Kelp DAO. Context Snapshot, Execution, Short-term Outcome, and Long-term Outcome are
all present for 13/13 events (verified by count, not spot-check). Entity cross-referencing from Phase 2
mostly holds: Chainlink, Kelp DAO, Alameda, FTX Recovery Trust, and Protocol Guild are all referenced by
the exact Phase 2 names — but **Trail of Bits (a Phase 2 auditor entity) is never mentioned in the
timeline**, flagged as a minor gap, not blocking.

**Citation problem:** all 13 `Evidence:` fields are empty (`Evidence:.` — literally nothing between the
colon and the period), verified via `grep -o "Evidence:\.\?" | sort | uniq -c` → `13 Evidence:.`. A 21-source
numbered bibliography exists at the end of the document but is not linked to individual events — this is the
exact same failure mode as the original (pre-reformat) Phase 1 output, despite the per-fact citation rule
having already been stated and then tightened twice. A citation-only reformat pass (same shape as the Phase
1 reformat) was sent — logged in `PROMPTS-LOG.md`; result pending as of this commit. Minor format deviation
(not blocking, same as Phase 2): fields are joined into one flowing paragraph per event instead of one field
per line as the template specifies.

**Parser bug found and fixed during Phase 3 verification (2026-07-25, commit `39d38ed`):** LayerZero's Open
Threads heading was written as "Analisis Lapisan Resolusi & Konteks Tidak Terekam (Open Threads)" — the
marker phrase at the *end* of a longer heading — which `tools/ingest.py`'s old `OPEN_THREADS_RE` (required
"open threads" at the start of the line) never matched. The section's content was also written as narrative
paragraphs with zero bullet points, which the old bullet-only parser would have produced zero threads from
even if the regex had matched. Together this meant the real content there (a Radiant Capital finding, FTX
clawback litigation docket status) was about to be **silently and completely discarded** from the final
dossier with no trace. Fixed by broadening the regex and adding a paragraph-splitting fallback plus a
bibliography stop-point (`BIBLIOGRAPHY_RE`) so the citation list isn't absorbed as fake "threads." Verified
directly against LayerZero Phase 3's real extracted text (0 → 7 threads) and regression-tested against
Phase 1 and Phase 2's real files (unchanged: 5 and 2 threads respectively) before committing. This means
**Phase 1 and Phase 2 were parsed correctly all along** — only Phase 3's narrative-style heading exposed the
bug.

**LayerZero Phase 4 — Technology Intelligence, technically excellent / citations empty (3rd occurrence).**
Raw file archived at `doc_backup/deep/LayerZero_2026-07_phase4-nocitations-v1.docx` (same v1/v2-split
pattern as Phase 1 and Phase 3 — will not become the active `phased/LayerZero/04-technology.docx` until
its citation reformat comes back). Every requested recovery item was delivered in real depth: SendUln302/
ReceiveUln302/ReadLib1002 explained mechanically (down to `_payWorkers`, `payloadHash`, `_clearPayload`),
the Kelp DAO 1-of-1 DVN vulnerability explained down to the RPC-node-poisoning attack mechanism, all 5
Phase 2 auditors given scope + dates, the "Bridging Trilemma" framing explained and contrasted against the
Nakamoto/Blockchain trilemma, and the "Zero" blockchain roadmap — which turned out to already be **live**
(launched 10 Feb 2026: Pure Delegated Proof of Stake, 10K TPS target, "System Zone" module), not merely
planned as assumed when the prompt was written.

Two cross-phase findings surfaced by this pass:
- **New entity not in Phase 2:** a 6th auditor, **ClawSecure** (Feb 2026, co-audited a LayerZero client
  with Trail of Bits) — not present in Phase 2's 76-entity graph. Flagged as a Phase 2 gap to recover
  later, same pattern as Chainlink/Google Cloud/Polyhedra being dropped from Phase 1 and recovered in
  Phase 2.
- **Two real historical events missing from Phase 3's timeline:** the Zero blockchain launch (10 Feb 2026)
  and a systemic DVN security fix (May 2026, hardcoded 5-of-5 minimum for LayerZero Labs' own DVN,
  responding to Kelp DAO) both postdate Phase 3's last recorded event (Aug 2024/2025 Stargate governance
  merger). Rather than a third separate pass, these were folded directly into the (still-pending) Phase 3
  citation reformat prompt, which now asks for both citations AND these 2 new event blocks in one pass —
  see the revised prompt in `PROMPTS-LOG.md`.

**Citation problem — third occurrence of the identical failure mode:** zero inline Evidence Level or
sourcing anywhere in the document (verified: 0 matches for "(HIGH)"/"(MEDIUM)"/"(LOW)", 0 inline URLs/
source brackets) despite an 11-field response with a 21-source bibliography at the end, unlinked to any
individual claim. This is the same failure as the original Phase 1 attempt and Phase 3 — the per-fact
citation rule has now failed three separate times despite being stated from Phase 1 onward and tightened
twice. A citation-only reformat pass was sent (logged in `PROMPTS-LOG.md`), this time also explicitly
asking the model to break each long paragraph field into individual per-claim bullet lines so citations
can attach per-fact rather than per-paragraph. **Worth reconsidering before Phase 5:** if this 3-for-3
pattern continues, the per-fact citation instruction may need to move from "stated in the prompt" to
"structurally enforced" (e.g. requiring bullets from the start rather than allowing paragraph fields) —
not yet acted on, flagged for the next reformat's outcome to confirm.

**When a phase completes:** update its row's "Phases done"/"Next phase" columns in the same commit as dropping
the phase's raw `.docx` into `doc_backup/inbox/phased/LayerZero/`. Once all phases planned for the Track are
done, run `./run.sh` to assemble the dossier, then move the finished project out of this table (it becomes a
normal `Deep Dossiers` row above) and add the next candidate.

## Deep Dossiers
_Tier: Deep · anchor projects with full causal history._

| # | Project | Category | Era | Source | File | Raw source |
|---|---------|----------|-----|--------|------|-----------|
| D1 | Ethereum | Layer 1 / Smart-Contract Platform | 2013– | Deep Research (Gemini) | `CaseStudies/Ethereum.md` | `doc_backup/deep/Ethereum_2026-07_gemini.docx` (rebuilt; prior PDF retained) |
| D2 | Solana | Layer 1 / High-Performance Monolithic Platform | 2017– | Deep Research (Gemini) — **merged v1+v2** | `CaseStudies/Solana.md` | `doc_backup/deep/Solana_2026-07_gemini.docx` (v1, 22-section) + `Solana_2026-07_gemini_v2.docx` (v2, Causal Event Graph) |
| D3 | BNB Chain | Layer 1 EVM (Exchange-backed) + modular suite (opBNB/Greenfield) | 2017– | Deep Research (Gemini) | `CaseStudies/BNBChain.md` | `doc_backup/deep/BNBChain_2026-07_gemini.docx` |
| D4 | Cardano | Layer 1 / Peer-reviewed EUTXO platform (Ouroboros PoS) | 2015– | Deep Research (Gemini) | `CaseStudies/Cardano.md` | `doc_backup/deep/Cardano_2026-07_gemini.docx` (rebuilt; prior PDF retained) |
| D5 | Avalanche | Layer 1 / Metastable-consensus multi-chain (Subnet/L1) + RWA-TradFi | 2018– | Deep Research (Gemini) | `CaseStudies/Avalanche.md` | `doc_backup/deep/Avalanche_2026-07_gemini.docx` (rebuilt; prior PDF retained) |
| D6 | Polkadot | Layer 0 / Heterogeneous-sharding + shared-security (Relay/parachains) | 2016– | Deep Research (Gemini) | `CaseStudies/Polkadot.md` | `doc_backup/deep/Polkadot_2026-07_gemini.docx` |
| D7 | Cosmos | Layer 0 / Appchain "Internet of Blockchains" (CometBFT/SDK/IBC) | 2014– | Deep Research (Gemini) | `CaseStudies/Cosmos.md` | `doc_backup/deep/Cosmos_2026-07_gemini.docx` |
| D8 | dYdX | DeFi / Perp-derivatives DEX (order-book appchain → RWA pivot) | 2017– | Deep Research (Gemini) | `CaseStudies/dYdX.md` | `doc_backup/deep/dYdX_2026-07_gemini.docx` |
| D9 | Aave | DeFi / Money-market lending (Flash Loans, GHO, V4 Hub-and-Spoke) | 2017– | Deep Research (Gemini) | `CaseStudies/Aave.md` | `doc_backup/deep/Aave_2026-07_gemini.docx` |
| D10 | ether.fi | DeFi / Liquid Restaking (LRT) + DeFi Neobank (Stake/Liquid/Cash) | 2022– | Deep Research (Gemini) | `CaseStudies/EtherFi.md` | `doc_backup/deep/EtherFi_2026-07_gemini.docx` |
| D11 | EigenLayer | Infrastructure / Restaking pioneer → EigenCloud (verifiable AI/compute) | 2021– | Deep Research (Gemini) | `CaseStudies/EigenLayer.md` | `doc_backup/deep/EigenLayer_2026-07_gemini.docx` |
| D12 | Celestia | Modular / Data Availability (sovereign alt-DA; DAS/NMT; Fibre 1 Tb/s) | 2019– | Deep Research (Gemini) | `CaseStudies/Celestia.md` | `doc_backup/deep/Celestia_2026-07_gemini.docx` |

---

## Curated Projects — Batch 01
_Container: `examples/Pioneer/` · Source: Deep Research (Gemini) — "Rekomendasi Kurasi Proyek Historis"._
_Raw source archived: `doc_backup/batch/Batch-01_Kurasi-Dataset_2026-07_gemini.pdf` (+ `.md`)._

| # | Project | Category | Era | Priority | File |
|---|---------|----------|-----|----------|------|
| 1 | Celestia | Modular / Data Availability | 2019– | P0 | **removed** — superseded by Deep D12, `CaseStudies/Celestia.md` |
| 2 | Synthetix | DeFi (DeFi Pioneer) | 2017– | P0 | `Pioneer/Synthetix.md` |
| 3 | Helium | DePIN (IoT & Wireless) | 2013– | P0 | `Pioneer/Helium.md` |
| 4 | EigenLayer | Infrastructure / Restaking | 2021– | P0 | **removed** — superseded by Deep D11, `CaseStudies/EigenLayer.md` |
| 5 | Aave | DeFi (DeFi Pioneer) | 2017– | P1 | **removed** — superseded by Deep D9, `CaseStudies/Aave.md` |
| 6 | Arweave / AO | Data Availability / Modular Compute | 2017– | P1 | `Pioneer/Arweave-AO.md` |
| 7 | Farcaster | Social (Decentralized Social) | 2020– | P1 | `Pioneer/Farcaster.md` |
| 8 | MakerDAO / Sky | DeFi (Decentralized Central Bank) | 2015– | P0 | `Pioneer/MakerDAO-Sky.md` |

Cross-project analysis: `examples/CaseStudies/Batch-01-EvolutionAnalysis.md`.

## Cross-Project Analyses
_Syntheses that turn multiple project histories into transferable patterns (tier: Synthesis)._

| Analysis | Projects linked | File |
|----------|-----------------|------|
| Batch 01 Evolution | Celestia, Arweave/AO, Helium, Synthetix, EigenLayer | `CaseStudies/Batch-01-EvolutionAnalysis.md` |
| Staking → Restaking Stack | Ethereum, Lido, EigenLayer | `CaseStudies/CrossAnalysis-ETH-Lido-EigenLayer.md` |

## Curated Projects — Batch 02
_Container: `examples/Pioneer/` · Source: Web research (public sources, July 2026 — cited per file)._
_Promoted from the Batch 01 candidate queue. Provenance is web research, **not** Deep Research (Gemini)._

| # | Project | Category | Era | Priority | File |
|---|---------|----------|-----|----------|------|
| 9 | Safe | Wallet / Account Abstraction | 2017– | P0 | `Pioneer/Safe.md` |
| 10 | Chainlink | Oracle | 2017– | P0 | `Pioneer/Chainlink.md` |
| 11 | LayerZero | Bridge / Interoperability | 2021– | P1 | `Pioneer/LayerZero.md` |
| 12 | Lido | Liquid Staking | 2020– | P1 | `Pioneer/Lido.md` |
| 13 | Uniswap | DeFi / AMM | 2018– | P1 | `Pioneer/Uniswap.md` |
| 14 | World Network (Worldcoin) | Identity | 2019– | P1 | `Pioneer/WorldNetwork-Worldcoin.md` |
| 15 | dYdX | DeFi / Appchain | 2017– | P1 | **removed** — superseded by Deep D8, `CaseStudies/dYdX.md` |
| 16 | Ethena | DeFi / Stablecoin | 2023– | P2 | `Pioneer/Ethena.md` |
| 17 | Berachain | Layer 1 (Proof-of-Liquidity) | 2021– | P2 | `Pioneer/Berachain.md` |
| 18 | Optimism | Layer 2 (OP Stack / Superchain) | 2019– | P2 | `Pioneer/Optimism.md` |

## Dataset Distribution (Cumulative)
_After Batch 01 + Batch 02._

| Category | Batch 01 | Batch 02 | Cumulative |
|----------|----------|----------|------------|
| DeFi (Pioneer, AMM, Appchain, Stablecoin, Central Bank) | 3 | 3 | 6 |
| Modular / Data Availability | 1 | 0 | 1 |
| Data Availability / Modular Compute | 1 | 0 | 1 |
| Infrastructure / Restaking | 1 | 0 | 1 |
| DePIN | 1 | 0 | 1 |
| Social | 1 | 0 | 1 |
| Wallet / Account Abstraction | 0 | 1 | 1 |
| Oracle | 0 | 1 | 1 |
| Bridge / Interoperability | 0 | 1 | 1 |
| Liquid Staking | 0 | 1 | 1 |
| Identity | 0 | 1 | 1 |
| Layer 1 | 0 | 1 | 1 |
| Layer 2 | 0 | 1 | 1 |
| **Total** | **8** | **10** | **18** |

## Dataset Gap — Status
_Progress against the gaps identified in Batch 01._

- **Wallet & Account Abstraction** — ✅ terisi oleh **Safe** (Batch 02).
- **Oracle & Real-Time Data Infrastructure** — ✅ terisi oleh **Chainlink** (Batch 02).
- **Cross-Chain Communication & Bridges** — ✅ terisi oleh **LayerZero** (Batch 02).
- **Privacy & Identity Security** — ⚠️ *sebagian*: identitas/proof-of-personhood terisi oleh **Worldcoin**,
  namun **privasi transaksi berbasis Zero-Knowledge Proofs** (mis. Aztec, Railgun, Zcash) masih terbuka.

### Remaining / New Gaps (untuk batch berikutnya)
- **ZK Privacy** — protokol privasi transaksi berbasis ZKP.
- **RWA (Real-World Assets)** — ⚠️ *sebagian*: adopsi RWA/TradFi institusional terisi oleh **Avalanche** (Deep D5:
  Evergreen/AvaCloud, Progmat $2,8 mrd, JPMorgan Onyx); RWA sebagai **kategori Summary tersendiri** masih terbuka.
- **Gaming / NFT Infrastructure** — belum terwakili.
- **AI x Crypto** — kategori baru yang berkembang pesat.

## Candidate Queue — Status
_The Batch 01 candidate queue has been **fully processed into Batch 02** (see table above)._
The queue is now empty; the next queue will be defined from the Remaining/New Gaps section once
new research is available.

> Note: a candidate queue is a curation backlog of instances. It lives here in `examples/` (knowledge),
> not in `docs/Research/` (which documents *how* research is done, not *what* to research).

---

## Karya yang Dikutip — Batch 01 (Bibliography)
_Sumber Deep Research untuk Batch 01._

1. Modularity and App-Specific Chains — Blockchain@NUS, Medium — https://medium.com/@nusfintech.bc/modularity-and-app-specific-chains-524547bc33a8
2. celestiaorg/celestia-core (fork of CometBFT) — GitHub — https://github.com/celestiaorg/celestia-core
3. nmt/docs/spec/nmt.md — celestiaorg/nmt, GitHub — https://github.com/celestiaorg/nmt/blob/master/docs/spec/nmt.md
4. AMA: AO and Artificial Intelligence — Perma DAO, Medium — https://medium.com/@perma_dao/ama-ao-and-artificial-intelligence-93dc5649dc39
5. Let's solve these crucial protocol weaknesses — DFINITY Forum — https://forum.dfinity.org/t/lets-solve-these-crucial-protocol-weaknesses/28329?page=2
6. AVS Risk Assessment: EigenDA — LlamaRisk Research — https://llamarisk.com/research/avs-risk-assessment-eigenda
7. API Providers — APIs.io — https://apis.io/providers/
8. Synthetix Price: SNX/USD — CoinGecko — https://www.coingecko.com/en/coins/synthetix-network-token
9. The Tokenomics of Helium (HNT) — findas.org — https://www.findas.org/tokenomics-review/coins/the-tokenomics-of-helium-hnt/r/DUr5bvmBPVYzPkKJUiXz7Z
10. Helium Mining 2026: The Complete Operator Guide — MillionMiner — https://millionminer.com/news/helium-mining-2026-complete-operator-guide
11. simpleaswater/defi-resources — GitHub — https://github.com/simpleaswater/defi-resources
12. Catching Up to Crypto — DOKUMEN.PUB — https://dokumen.pub/catching-up-to-crypto-your-guide-to-bitcoin-and-the-new-digital-economy-9781394158744-9781394158751-9781394158768-1394158742-c-6678457.html
13. Helium — Cryptoassets, IQ.wiki — https://iq.wiki/wiki/helium
14. Helium Network — Wikipedia — https://en.wikipedia.org/wiki/Helium_Network
15. EIGEN: The Universal Intersubjective Work Token — EigenCloud — https://docs.eigencloud.xyz/assets/files/EIGEN_Token_Whitepaper-0df8e17b7efa052fd2a22e1ade9c6f69.pdf
16. EigenCloud: Rebuilding Web3's Trust Foundation — blockeden.xyz — https://blockeden.xyz/blog/2025/12/03/eigencloud-rebuilding-web3-s-trust-foundation-through-verifiable-cloud-infrastructure/
17. The Delphi Podcast — Buzzsprout — https://feeds.buzzsprout.com/2609274.rss
18. EIGEN Token Whitepaper (HTML) — EigenCloud — https://docs.eigencloud.xyz/html/EIGEN_Token_Whitepaper-converted-xodo.html

## Bibliography — Batch 02
_Sumber riset web (diakses Juli 2026). Rincian per-proyek ada di bagian "Sources" tiap file._

- **Safe** — IQ.wiki (https://iq.wiki/wiki/safe); Gnosis Forum GIP-29 (https://forum.gnosis.io/t/gip-29-spin-off-safedao-and-launch-safe-token/3476); Safe Foundation Tokenomics (https://safefoundation.org/blog/safe-tokenomics)
- **Chainlink** — Wikipedia (https://en.wikipedia.org/wiki/Chainlink_(blockchain_oracle)); Messari (https://messari.io/project/chainlink/profile)
- **LayerZero** — LayerZero Docs (https://docs.layerzero.network/v2/concepts/layerzero-protocol-architecture); Messari (https://messari.io/report/understanding-layerzero)
- **Lido** — lido.fi (https://lido.fi/); Messari (https://messari.io/report/liquid-staking-with-lido); Datawallet (https://www.datawallet.com/crypto/lido-explained)
- **Uniswap** — Wikipedia (https://en.wikipedia.org/wiki/Uniswap); Uniswap Blog (https://blog.uniswap.org/uniswap-history)
- **World Network (Worldcoin)** — TechCrunch (https://techcrunch.com/2024/10/17/sam-altmans-worldcoin-becomes-world-and-shows-new-iris-scanning-orb-to-prove-your-humanity/); Quartz (https://qz.com/sam-altman-worldcoin-crypto-ai-biometrics-identity-1850669360)
- **dYdX** — Antonio Juliano, Medium (https://antonio-dydx.medium.com/the-history-of-dydx-so-far-68bf46789f86); dYdX v4 Evolution, Medium (https://medium.com/@gwrx2005/dydx-v4-architectural-and-protocol-evolution-from-v3-6c312f51f7b7)
- **Ethena** — Ethena Docs (https://docs.ethena.fi/); Nansen (https://nansen.ai/post/what-is-ethena)
- **Berachain** — Fireblocks (https://www.fireblocks.com/blog/what-is-berachain-and-proof-of-liquidity); DAIC Capital (https://daic.capital/blog/berachain-tokens-explained); Decrypt (https://decrypt.co/resources/what-is-berachain-proof-of-liquidity-blockchain)
- **Optimism** — Coin Bureau (https://coinbureau.com/review/optimism-review); Eco (https://eco.com/support/en/articles/10273675-what-is-optimism-the-ethereum-l2-and-op-mainnet-explained); The Block (https://www.theblock.co/linked/149464/optimisms-governance-token-officially-goes-live)
