# CIF Dataset Index

**Pipeline position:** Applications layer — validated knowledge produced by `Research → Extraction` and
structured against the `docs/` ontology.

> Knowledge artifacts (real curated data), not documentation containers. Each conforms to
> `templates/ProjectTemplate.md` and links back to the ontology it instantiates.

This is the master curation record for the dataset stored in `examples/`: what was added per batch,
how the taxonomy is distributed, where the gaps are, and what is queued next.

**Total curated projects: 1 (LayerZero, D13).**

> **⚠ 2026-07-26 dataset reset (maintainer decision).** All prior projects — 12 Deep Dossiers (Ethereum,
> Solana, BNB Chain, Cardano, Avalanche, Polkadot, Cosmos, dYdX, Aave, ether.fi, EigenLayer, Celestia) and
> 13 Summary/Batch profiles (`examples/Pioneer/`) — were built via the old single-mega-prompt Deep Research
> process (22-section / Causal Event Graph v2 formats), which the maintainer judged not rigorous enough:
> inconsistent, incomplete, too much noise, compared to the discipline the new Format v3 phased pipeline
> (11 sequential phases, each independently verified, `docs/Protocol/Phased-Research-Prompts.md`) proved out
> on LayerZero — see the Phase 1–11 log below and `doc_backup/inbox/phased/LayerZero/PROMPTS-LOG.md`. This
> **explicitly supersedes** the "V1 → V2 Upgrade Queue (upgrade before delete)" policy that used to live in
> this section, and the equivalent note in `CLAUDE.md` — both are now stale and have been updated.
>
> **Nothing was permanently deleted.** All files moved (`git mv`, so full history is preserved either way)
> to `_archive_pre_v3/`, mirroring their original paths exactly (e.g.
> `_archive_pre_v3/examples/CaseStudies/Ethereum.md`, `_archive_pre_v3/doc_backup/deep/Ethereum_2026-07_gemini.docx`).
> To restore any project, `git mv` it back from `_archive_pre_v3/` to its original path and re-run
> `tools/build_json.py`. Going forward, **every new project must go through the Format v3 phased pipeline**
> (`docs/Protocol/Phased-Research-Prompts.md`) — the old `deep`/`batch` single-prompt ingest modes in
> `tools/ingest.py` still exist mechanically but are no longer the sanctioned research process.
> `examples/PatternRegistry.md`'s 6 existing patterns all drew their grounding from now-archived projects
> (P1/P2/P4 from `CrossAnalysis-ETH-Lido-EigenLayer.md`, P3 from `Batch-01-EvolutionAnalysis.md`, P5/P6 from
> `Ethereum.md` — none were LayerZero-sourced) — flagged in that file rather than deleted, since the
> abstract pattern reasoning (Shape/Applies When) still has framework value independent of its now-archived
> grounding examples; treat it as historical-reference pending rebuild from new phased-pipeline projects.

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

## V1 → V2 Upgrade Queue — superseded 2026-07-26, see reset note above

This section used to track 11 pre-phased-pipeline Deep Dossiers (plus Solana as the worked v1+v2-merge
example) queued for upgrade rather than deletion. That policy is superseded by the 2026-07-26 dataset reset:
all 12 (including Solana) are now in `_archive_pre_v3/`, same as everything else pre-dating the phased
pipeline. Kept here only so the historical policy and its rationale aren't silently erased from the record.

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
| _(none — LayerZero completed all 11 phases 2026-07-26 and moved to Deep Dossiers as D13; awaiting next candidate)_ | | | | |

**LayerZero Phase 1 — two source files, deliberately.** The first Gemini pass returned a rich but
narrative/table-formatted report in English; a reformat pass produced a clean Indonesian Label:Value version.
A term-by-term diff of the two showed **all numeric facts survived the reformat intact** (funding rounds,
token allocations, dates, prices, percentages — the most fragile category, verified clean), but **8 items were
silently dropped**, so both files are kept:

- `doc_backup/inbox/phased/LayerZero/01-foundation.docx` — the reformatted v2, **the active phase file**
  ingest reads (parseable, Indonesian, conflicts flagged, Open Threads present).
- `doc_backup/deep/LayerZero_2026-07_phase1-narrative-v1.docx` — the original narrative pass, kept out of the
  `phased/` folder so ingest doesn't see two "foundation" files, but retained because it is the **richer**
  source of record for the items below. **Removed 2026-07-26** (Task 1 dataset-reset cleanup, after Phase 11
  confirmed the pipeline complete) — its only unique content (the 4 items below) was already recovered into
  Phase 2 before removal, so nothing was lost; see git history for the file itself if ever needed.

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
  record (same pattern as v1 above). **Removed 2026-07-26** (Task 1 dataset-reset cleanup) — every item it
  carried is accounted for above (superseded by a later phase, or carried forward in `PROMPTS-LOG.md`).
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
`phased/` folder ingest reads. **Removed 2026-07-26** (Task 1 dataset-reset cleanup) — fully superseded by
the citation-complete `03-history.docx` that shipped after the Claude-direct research pass. All 13 known events from the prompt present, in order, plus 4 valuable bonus
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
its citation reformat comes back). **Removed 2026-07-26** (Task 1 dataset-reset cleanup) — fully superseded
by the citation-complete `04-technology.docx`. Every requested recovery item was delivered in real depth: SendUln302/
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

**Phase 3 citation saga resolved — 3 Gemini attempts failed, direct Claude research succeeded
(2026-07-25).** After the citation-only reformat above, two further Gemini attempts were tried and both
failed differently: attempt 2 applied the "cannot re-verify source" fallback to literally every field
instead of searching (and regressed the 2 new events to a single end-of-block Evidence line, the exact
anti-pattern the prompt existed to fix); attempt 3 dropped inline citation entirely (0 `Evidence:` fields,
0 `[sumber N]` tags anywhere) while producing two unmerged, mutually inconsistent bibliography lists —
though it did preserve Open Threads/Kesimpulan Strategis, which attempt 2 had dropped. Attempt 3's raw
output was `doc_backup/inbox/phased/LayerZero/03-historical-attempt3-nocitation.docx` — **removed 2026-07-26**
(Task 1 dataset-reset cleanup); full prompts for all 3 attempts remain in `PROMPTS-LOG.md`, which is the
verbatim record of what was tried and why each attempt failed.

The maintainer then ran **Claude's own research directly (not Gemini)** to build a sourced citation map
for the same 15 events (archived at `03-historical-citation-map-research.md`) — real, checkable URLs
(CoinDesk, Chainalysis, QuillAudits, PR Newswire, arXiv, official LayerZero/Tether blogs, Delaware court
filings) mapped one-to-one to each event, plus fact-checking against those sources. This succeeded where
the reformat loop hadn't, and surfaced something the phased pipeline had been silently carrying since
the original Phase 3 run: **the Kelp DAO $292M exploit was dated April 2024 everywhere (original Phase 3,
both reformat attempts, and Phase 4's Security Model + Audit History sections) — the real date,
cross-verified by CoinDesk/Chainalysis/QuillAudits, is 18 April 2026.** One incident, not two; it
belongs *after* the Zero blockchain launch (10 Feb 2026) and *immediately before* the May 2026 DVN
security fix that responds to it — the old placement made that response read as disconnected from its
own trigger by two years. Four smaller corrections also surfaced (seed-round lead investors, the exact
FTX-trapped treasury figure, the Stargate acquisition's DAO-approval date, and the ZRO TGE's actual
price-drop path), plus a set of claims that could not be verified and are now flagged explicitly rather
than silently trusted or silently deleted — most notably, **the entire 6-auditor roster already
committed in Phase 4** (Trail of Bits, Zellic, Zokyo, Peckshield, Hacken, ClawSecure) could not be
independently confirmed.

Final synthesis (done directly, no further Gemini round needed, since the citation map plus attempt-3's
sound event content were sufficient): `03-historical.docx` — 15 events each with a real `Evidence:` line,
Kelp DAO repositioned and redated, the 4 other corrections applied inline (marked `[KOREKSI]`), unverified
items marked `[TIDAK TERVERIFIKASI]` rather than resolved either way, Open Threads/Kesimpulan Strategis
preserved and extended, one de-duplicated 58-source bibliography. Verified structurally (15/15
Date/Event/Evidence fields present; OOXML schema validation passed) before committing. `04-technology.docx`
was patched in place for the two "April 2024" Kelp DAO references and given an Open Threads caveat about
the unverified audit roster — full detail in `PROMPTS-LOG.md`.

**LayerZero Phase 5 — Financial Intelligence, resolved via Claude-direct research (2026-07-25).** Same
pattern as Phase 3: rather than sending the Gemini prompt, the maintainer ran Claude's own research
(`05-financial-citation-map-research.md`), which cross-checked cleanly against Phase 3's corrected facts
and sharpened one finding further — the FTX settlement (31 Jan 2025) amount isn't just unverified, a
dedicated docket/press search confirms it was **never publicly disclosed at all** (sole source: the
CEO's own X post, which names no figure). It also surfaced 5 real capital events missing from every
other phase's document — a16z's $55M secondary ZRO purchase, the Stargate acquisition's actual cash
mechanics ($25M effective cost, not the $110-120M headline), two ZRO buybacks, and undisclosed Tether/
Citadel/ARK investments — none of which are priced equity rounds (LayerZero has raised none since April
2023). Synthesized directly into `05-financial.docx`: 4 funding rounds with real per-field citations, a
new "Peristiwa Modal Non-Round" section for the 5 events (no existing template slot fit them), the "$111M"
figure retracted outright, and an Open Threads note flagging the 5 events as Phase 3 timeline candidates
for a future revision. Full detail in `PROMPTS-LOG.md`.

**LayerZero Phase 6 — Token Intelligence, first Gemini draft rejected, Claude-direct research succeeded
(2026-07-26).** The Gemini draft failed worse than any prior LayerZero phase: zero inline citations
(same failure Phase 3 needed 3 attempts to fix) plus a prose-quality collapse — several fields degraded
into page-length run-on sentences — and, most seriously, a claim that TGE released 25% of supply (split
8.5%/5%/11.5%) that contradicted the already-confirmed 8.5%-claimable figure with no traceable source,
alongside a claim that the fee switch was "unconditionally active" since Feb 2026. Not patched (archived
as `06-token-rejected-nocitation-badprose.docx`, **removed 2026-07-26** in the Task 1 dataset-reset cleanup)
— the 25% claim needed independent verification, not a citation retrofit onto content that might be wrong.

A Claude-direct research pass (`06-token-citation-map-research.md`) resolved both issues decisively using
LayerZero Foundation's own primary sources: the 25% TGE figure is fabricated (real figure ~13.5% — 8.5%
retail-claimable + 5% Ecosystem-and-Growth unlock), and the fee switch has **never** been activated — all
4 semi-annual referendums through June 2026 show "Outcome: Off" on the Foundation's governance page;
Referendum #3 got ~97% approval among voters but only 3.71% turnout, failing its 40.59% quorum, which is
likely what the rejected draft misread as "activated." Also confirmed post-TGE buybacks are held in
treasury, not burned (closing a question Phase 5 left open, and matching Phase 5's $112.7M/19.77%-of-
supply buyback figures exactly), and turned "holder concentration: unmeasurable" into a properly caveated
partial picture (ZRO is an OFT concentrated on Arbitrum, not Ethereum; Nansen tracked one entity
accumulating 2.6% of supply via Coinbase-Prime-funded wallets). Surfaced one new open question: no
tracker agrees on circulating supply (252M–514M depending on whether re-locked Foundation holdings
count). Synthesized directly into `06-token.docx`. Full detail in `PROMPTS-LOG.md`.

**LayerZero Phase 7 — Ecosystem Intelligence, first successful non-Gemini attempt (2026-07-26).** After a
Claude usage limit interrupted the direct-research workflow used for Phases 3/5/6, and Gemini's own
Phase 7 attempt came back incomplete, the maintainer tried the same prompt through DeepSeek — the first
time a third model was used in this pipeline. It was the strongest first-attempt result of any LayerZero
phase: correct format, per-fact citations throughout, and the live-vs-announced-only distinction (the
prompt's central ask) applied correctly without any correction needed — Zero blockchain's institutional
partners (Citadel/DTCC/ICE/ARK/Google Cloud) correctly marked announced-only, Tether/USDT0 and Keeta
correctly marked live with real mechanism detail (USDT0 uses lock-and-mint on Ethereum, burn-and-mint
elsewhere — closing the integration-mechanics gap carried since the Phase 1 trim). Cross-checked cleanly
against every prior phase's entity/DVN/exchange lists. Committed with only a mechanical text-to-docx
conversion, no content fixes needed. One minor quality gap versus the Phase 3/5/6 Claude-research
citations: sources are domain+date, not full URLs — noted, not corrected. Full detail in `PROMPTS-LOG.md`.

**LayerZero Phase 8 — Market Intelligence, growth-vs-erosion correctly held together (2026-07-26).**
Executed the phase's central instruction correctly on the first pass: "Current Status" and "Market Share"
both present LayerZero's 85.7% share of 30-day cross-chain GMP volume (Allium Labs Interoperability
Dashboard) *and* the >$7.24B Chainlink CCIP exodus side by side, explaining explicitly why they aren't
contradictory (the exodus is concentrated in institutional/high-value flow and predates Allium's 9 June
2026 dashboard launch, so it doesn't show up in the aggregate metric yet). Surfaced high-value new facts:
ZRO down 87% from its Dec 2024 ATH; Stargate TVL's real trajectory (>$3B peak → $1.37B Q1 2026, already
declining pre-Kelp-DAO → $400-600M by 31 May 2026); and Aave selecting Chainlink CCIP as its default
cross-chain rail — a fact that cross-verifies against a source ("Aave Picks Chainlink CCIP...", Thirdweb)
that had already surfaced unverified in the attempt-2 Phase 3 bibliography months earlier, raising
confidence it's real. Properly reported conflicting numbers (message counts, chain counts, cumulative
value transferred) as ranges with per-source citation rather than picking one. Only mechanical cleanup
needed before committing (stray CJK-style brackets, semicolon artifacts) — no content corrections, unlike
Phase 6's rejected draft. Full detail in `PROMPTS-LOG.md`.

**LayerZero Phase 9 — Behavioral Intelligence, genuine interpretive work confirmed (2026-07-26).** All 15
Decision Events completed with the full 8-field template (including the 8-POV Stakeholder Reactions
block), and — the actual test of this phase — the model engaged substantively with all 7 targeted
cross-phase hints rather than restating Historical Intelligence's facts. Notably: read Stargate's
pre-acquisition TVL decline as a defensive pressure behind the Aug 2025 acquisition, not just an offensive
move, and reasoned about Wormhole's rejected higher cash counter-bid as evidence LayerZero traded price
for control; tied the Fee Switch's 4 consecutive quorum failures (Phase 6) to the Zero blockchain launch
as a plausible alternative-utility play, correctly hedged as a MEDIUM-confidence inference rather than
stated as fact; and captured that the post-Kelp-DAO institutional exodus *grew* even after the public
apology and DVN hardening, naming Aave's specific switch to Chainlink CCIP rather than describing it
generically. Correctly preserved the corrected 18 April 2026 Kelp DAO date throughout. One quality note
(not a defect): many Stakeholder Reactions sub-fields for earlier, thinner-sourced events are generic,
low-specificity inferences rather than genuinely grounded reactions — honestly labeled `(Inferensi)`
throughout, so nothing is misrepresented as fact, just lower signal density in some cells. Committed with
only a mechanical text-to-docx conversion. Full detail in `PROMPTS-LOG.md`.

**LayerZero Phase 10 — Knowledge Extraction, 10 well-grounded pattern candidates (2026-07-26).** Used
`examples/CaseStudies/LayerZero.md` (the assembled 9-phase dossier) as the single context document rather
than re-pasting every phase, per the Phase 10/11 convention. The model went beyond the 5 seeded pattern
candidates and found 5 more independently, all properly grounded with `Shape`/`Drawn From`/`Applies When`/
Evidence Level and structural (not LayerZero-specific) transfer conditions — notably a dual-verification
security model pattern (Oracle+Relayer in V1, DVN+Executor in V2 both resting on a non-collusion
assumption that becomes a single point of failure once one party is compromised) and a DAO-picks-lower-
nominal-bid-over-higher-cash-rival-offer governance pattern (Stargate's DAO choosing LayerZero over
Wormhole's larger cash bid for strategic reasons). The 8-POV Success-Matrix avoided forcing clean labels
where the record is genuinely mixed — e.g. Institution: failure, citing the exodus, while still noting
the countervailing Feb 2026 institutional investment as unproven. Full detail in `PROMPTS-LOG.md`.

**LayerZero Phase 11 — Conflict Resolution, all 12 seeded conflicts checked + 17 more found independently
(2026-07-26).** Merge-only pass over the assembled 10-phase dossier (no new research). All 12 seeded
known-conflicts were re-verified against the actual dossier text rather than copied: correctly confirmed
resolved (not forced into a contradiction block) where a later phase's correction had genuinely propagated
— e.g. the Kelp DAO date fix (18 Apr 2026) has zero residual "April 2024" references across Historical/
Technology/Behavioral, and the fabricated "$111M FTX settlement" figure appears nowhere as fact — while
correctly kept open where the record genuinely disagrees, e.g. chain-count (50+/130+/165+/168/170+, no
consistent definition or date across phases) and the LayerZero Labs Ltd./Optimistic Labs Limited entity
relationship (still unclarified). 29 INKONSISTENSI blocks total (12 seeded + 17 self-found, e.g. distinguishing
LayerZero's 85.7% GMP *volume* share from the $7.24B Chainlink CCIP TVL exodus as different metrics, not a
contradiction). Verification found the raw output's own "Open Threads" section mixed genuinely-unresolved
items with resolved-no-conflict recaps under one misleading header (an artifact of how the prompt itself was
worded, not a model error) — patched mechanically into two accurately-labeled subsections during docx
conversion, no wording changes. Assembling the final 11/11 dossier also surfaces a live instance of the
Phase 3 filename-detection bug: `06-token-rejected-nocitation-badprose.docx` (the rejected first Phase 6
draft, kept in the folder for audit trail) fuzzy-matched the "token" phase key and was silently pulled into
the archive step — the *correct* file's content still won by alphabetical sort luck, verified against the
assembled dossier's Token Intelligence section, but this is exactly the fragility Task 2's `data_project`
mode (see `tools/README.md`) was built to hard-fail on instead of silently tolerating. Moved both stray
`.docx` drafts out of the phase-detection path non-destructively and rebuilt — clean 11/11 assembly, no
unmatched-file warnings, no duplicate archive citations; both were then permanently removed in the same-day
Task 1 dataset-reset cleanup below, once Phase 11 confirmed the pipeline complete.
**LayerZero is now a complete Deep Dossier (D13)** —
moved out of this queue; `examples/Pioneer/LayerZero.md` removed per the established Deep-supersedes-Summary
precedent (same treatment already applied to D9 Aave, D11 EigenLayer, D12 Celestia). `poc/cif.json`/`data.js`
rebuilt (`build_json.py`) — 13 deep projects now; `backtest.py` still passes 3/3.

**LayerZero Task 1 — dataset-reset cleanup (2026-07-26, after Phase 11 confirmed complete).** Removed the
6 superseded/rejected draft `.docx` files from this project's trial-and-error history, now that the 11-phase
pipeline is 100% the system of record: `LayerZero_2026-07_phase1-narrative-v1.docx`,
`LayerZero_2026-07_phase1-outofscope-v2.docx`, `LayerZero_2026-07_phase3-nocitations-v1.docx`,
`LayerZero_2026-07_phase4-nocitations-v1.docx` (all `doc_backup/deep/`), plus
`03-historical-attempt3-nocitation.docx` and `06-token-rejected-nocitation-badprose.docx` (the two rejected
drafts moved into `_rejected/` during Phase 11 finalization, now removed). Every one of these was already
confirmed fully superseded by its corresponding final phase file before removal — see the individual Phase
1/3/4/6 notes above, each now annotated with a removal marker rather than left as a dangling file reference.
**Kept, deliberately not treated as duplicates:** the 7 intermediate research/support files still in
`doc_backup/inbox/phased/LayerZero/` (`03-historical-citation-map-research.md`,
`05-financial-citation-map-research.md`, `06-token-citation-map-research.md`, `07-ecosystem-deepseek-raw.txt`,
`08-market-raw.txt`, `09-behavioral-raw.txt`, `10-knowledge-raw.txt`) — these are the citation/source-mapping
work product behind the final phase files, not draft duplicates of them, and `PROMPTS-LOG.md` (the verbatim
prompt-by-prompt record, which is the point of the whole logging discipline — it is not a "backup doc,"
it is the audit trail). Nothing about the 11 canonical phase files, the assembled dossier, or the archived
`doc_backup/deep/LayerZero_<phase>_2026-07.docx` set changed.

**When a phase completes:** update its row's "Phases done"/"Next phase" columns in the same commit as dropping
the phase's raw `.docx` into `doc_backup/inbox/phased/LayerZero/`. Once all phases planned for the Track are
done, run `./run.sh` to assemble the dossier, then move the finished project out of this table (it becomes a
normal `Deep Dossiers` row above) and add the next candidate.

## Deep Dossiers
_Tier: Deep · anchor projects with full causal history._

| # | Project | Category | Era | Source | File | Raw source |
|---|---------|----------|-----|--------|------|-----------|
| D13 | LayerZero | Interoperability / Omnichain Messaging (Bridge, GMP, DVN security) | 2021– | Deep Research (Gemini + Claude-direct + DeepSeek), Format v3 Dependency Pipeline (11/11 phases) | `CaseStudies/LayerZero.md` | `doc_backup/inbox/phased/LayerZero/01..11-*.docx` (per-phase, archived individually to `doc_backup/deep/LayerZero_<phase>_2026-07.docx`); full prompt history in `doc_backup/inbox/phased/LayerZero/PROMPTS-LOG.md` |

_D1–D12 (Ethereum, Solana, BNB Chain, Cardano, Avalanche, Polkadot, Cosmos, dYdX, Aave, ether.fi, EigenLayer,
Celestia) moved to `_archive_pre_v3/` in the 2026-07-26 dataset reset — see the note at the top of this file._

---

## Archived Content (pre-2026-07-26 dataset reset)

The sections that used to live here — **Curated Projects Batch 01** (8 projects), **Cross-Project Analyses**
(2 syntheses), **Curated Projects Batch 02** (10 projects), **Dataset Distribution**, **Dataset Gap —
Status**, **Candidate Queue — Status**, and the **Batch 01/02 bibliographies** — described the 13 Summary
profiles now moved to `_archive_pre_v3/examples/Pioneer/` (see the reset note at the top of this file). Their
full detail (tables, per-project bibliography, gap analysis) is preserved in git history as of commit
`4281cf7` and earlier, and in the archived files themselves — not reproduced here to avoid this index
describing files that are no longer active. Restore any of it the same way as a Deep Dossier: `git mv` back
from `_archive_pre_v3/` and re-run `tools/build_json.py`.

The **Dataset Gap** analysis in particular is still conceptually useful (ZK Privacy, RWA-as-a-category,
Gaming/NFT Infrastructure, AI x Crypto were flagged as open gaps) — worth re-checking once new phased-pipeline
projects are added, since the gap itself doesn't depend on the now-archived projects being present.
