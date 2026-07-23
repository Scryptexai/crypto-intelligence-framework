# Deep Research Brief (canonical)

This is the **contract** the framework expects deep reports to follow — the **22-section structure** every
Gemini deep report arrives in, so the `Ingest-Deep` role (and `tools/ingest.py`) map its output losslessly.
Read this before ingesting any deep report.

> The actual paste-ready **research prompt** (the "you are …, produce …" text sent to Gemini) is an external
> working tool kept in the maintainer's local files — intentionally **not** stored in the repo. This file keeps
> only the contract; any prompt must produce output that conforms to it.

**Audience of the output = AI reasoning, not human readers.** Every fact must be *Reusable Knowledge*: it
must answer **APA · MENGAPA · BAGAIMANA · APA DAMPAKNYA · APA PELAJARANNYA · APA HUBUNGANNYA DENGAN INDUSTRI**.
Bare facts without causality are not useful to this system.

**Projects are not random, and not binary "success/fail":**
- They have **types** (innovation archetype: First Mover / Fast Follower / Fork / Improvement; narrative type).
- Success/failure is judged **per point-of-view** — a project can succeed for VC and fail for Retail. The
  eight POVs are: **Founder, VC, Retail, Community, Developer, Institution, Validator, Builder** (§15).

## Core philosophy — Causal Intelligence, not Knowledge Base (read this first)

CIF is not a historical archive and not a similarity engine. The unit of analysis is not the **Project** — it
is the **Decision Event** (`docs/Ontology/DecisionEvent.md`): a single consequential decision, structured as
`Context → Problem/Opportunity → Trigger → Decision → Alternatives → Reason/Evidence → Execution →
Stakeholder Reactions (8 POV) → Short-term Outcome → Long-term Outcome`. A project is dozens of these, and
the pattern that matters is found **across decisions from unrelated projects/sectors**, not by comparing two
projects wholesale. Ethereum (smart contracts), Hyperliquid (on-chain orderbook), and Uniswap (AMM) are
unrelated by sector but may share the same *decision shape* — that shared shape is the reusable pattern, not
their TVL or sector label.

Three consequences for how research must be conducted:

1. **Observable vs Hidden.** Funding/TVL/wallets/volume (`docs/Ontology/Metrics.md` etc.) are *Observable* —
   they describe what happened. They rarely explain *why*. Capture the **Hidden** factors too
   (`docs/Ontology/Hidden.md`: motivation, constraint, pressure, trade-off, strategic goal, risk posture) —
   grounded in the source, never invented. Hidden explains Observable.
2. **Context is not optional.** The same decision produces different outcomes under different conditions — an
   easy incentivized-testnet airdrop worked in 2021 (few hunters, immature Sybil detection); the identical
   mechanic in 2026 does not (saturated hunters, mature Sybil detection). Every Decision Event must carry its
   **Context snapshot** (`docs/Ontology/Context.md`: industry state, competitor state, tech maturity, macro
   conditions, hunter/user population, VC climate, liquidity, narrative). Without this, patterns get
   matched blindly across incompatible eras — treat this as a research requirement, not an afterthought.
3. **Research is an investigator, not an analyst.** Do not conclude "why Uniswap succeeded" — collect every
   measurable and stated factor that plausibly contributed, preserve **conflicting evidence** and **minority
   opinions**, and let the downstream reasoning layer (`docs/Reasoning/*`) draw the causal conclusion with a
   calibrated confidence. A report that pre-concludes has already discarded the evidence CIF needs to find
   patterns *not yet known today*.

## Format v2 — Causal Event Graph (accepted alternative contract)

A second, evolved report contract that operationalises the Core Philosophy above more directly than the
22-section format. It is **auto-detected and auto-ingested** by `tools/ingest.py` (heuristic: ≤8 sections with
a title containing "Causal Event Graph", "Context & Environment", or "Decision Events" — see `is_v2()`), using
a dedicated ontology cross-link map. Either format is valid; v2 is recommended going forward because its
Decision Events section maps 1:1 onto `docs/Ontology/DecisionEvent.md` with no reconstruction needed.

**The 7 sections** (numbered headings `1.` … `7.`, e.g. `1. CONTEXT & ENVIRONMENT LAYER`):

1. **Context & Environment Layer** ("Era" Conditions) — state of technology, market/macro, competitor
   landscape, user/hunter behavior *at the time*, ideally with a Baseline-vs-Strategy comparison table.
   Maps to `docs/Ontology/Context.md` directly.
2. **Project Archetype & Core Value Proposition** — innovation classification, technical architecture,
   business/revenue model. Maps to `docs/Innovation/*`, `docs/Ontology/Technology.md`, `Revenue.md`.
3. **Chronological Decision Events** (Causal Event Graph) — a numbered list of `Event ID: DEV-NNN`, each
   with Timestamp, Pre-Conditions & Constraints (=Context), Trigger, The Decision Made, Alternatives Rejected,
   Execution Method. This **is** `docs/Ontology/DecisionEvent.md` — extract each DEV-NNN as one instance.
4. **Stakeholder Impact & Reaction Metrics** — per stakeholder group, empirical metric + response/impact.
   Maps to `docs/Success/*` (POV Success-Matrix) and `docs/Ontology/Community.md`. Note: this section's
   stakeholder groups are often coarser than the mandatory 8 POVs (§15 below) — when ingesting by hand,
   reconcile against the full 8-POV matrix rather than dropping the missing POVs.
5. **Quantifiable Outcomes & Trajectory** — token distribution, historical metric checkpoints across eras,
   incident/outage history. Maps to `docs/Ontology/Metrics.md`, `docs/TokenLifecycle/*`, `docs/MarketBehaviour/*`.
6. **Conflicting Evidence & Unresolved Questions** — discrepancies/controversies with both sides preserved,
   plus open questions. This is the **investigator-not-analyst principle, directly operationalised** — maps
   to `docs/Ontology/Hidden.md` and feeds `docs/Reasoning/Confidence.md` (lower confidence where evidence
   conflicts). Never silently resolve a stated disagreement — flag it as `INKONSISTENSI` if merging with
   another source.
7. **Conclusion & Synthesis** — the *only* section allowed to conclude/synthesize causally.

**Known gap vs v1:** v2's Stakeholder Impact section is not always structured as the full 8-POV grid — when a
project already has a v1 dossier, merge rather than replace (see `examples/CaseStudies/Solana.md` for a
worked example merging v1 + v2 sources, including two flagged `INKONSISTENSI` between them).

## The 22 sections (input contract)

1. **Executive Summary**
2. **Industry Background** — kondisi industri sebelum project lahir; masalah; narrative; kenapa muncul saat itu.
3. **Project Origin** — sejarah/ide awal, inspirasi, masalah utama, founder, core team, advisor.
4. **Innovation Analysis** — inovasi utama; First Mover / Fast Follower / Fork / Improvement; kenapa penting;
   dampak industri; apakah jadi standar.
5. **Technology Evolution** — roadmap, mainnet/testnet, upgrade, evolusi protokol.
6. **Funding Intelligence** — VC, round, valuation, investor strategis, pengaruh VC.
7. **Community Intelligence** — user pertama, growth, referral/ambassador/points/node/mining/quest/NFT/campaign/
   Discord/TG/X/KOL; kenapa berhasil/gagal.
8. **Narrative Intelligence** — narrative per fase (DeFi/NFT/GameFi/AI/DePIN/Restaking/Modular/Intent/L2/RWA/Meme);
   mengikuti / menciptakan / terlambat.
9. **Competitive Landscape** — kompetitor per fase; kenapa menang/kalah.
10. **Product Evolution** — perkembangan produk, pivot, fitur baru.
11. **Tokenomics Intelligence** — supply, unlock, emission, inflation, distribution, treasury, perubahannya.
12. **Airdrop & Incentive Intelligence** (WAJIB) — airdrop/retro/points/mining/quest/testnet/node/validator/
    ambassador/referral/early-adopter; tujuan, strategi, dampak, berhasil?
13. **Token Lifecycle Intelligence** — Pre-TGE, TGE, 30/60/90/180d, 1th, ATH/ATL, pump/dump, unlock, MM,
    likuiditas, volume, fair value, over/undervalued.
14. **Business Intelligence** — revenue, TVL, user, developer, partner, growth, adoption.
15. **Success & Failure Analysis** — dari 8 POV (Founder/VC/Retail/Community/Developer/Institution/Validator/Builder).
16. **Historical Timeline** — urut tanggal.
17. **Current Status** — berkembang / menurun / mati / recovery.
18. **Lessons Learned** — pelajaran & kesalahan terbesar; ditiru / dihindari.
19. **Knowledge Extraction Candidate** *(crown jewel)* — entity baru, relationship, dan pattern (innovation/
    growth/community/funding/token/price/narrative/failure/success/distribution/governance/technology);
    ontology/metadata/knowledge-graph/reasoning candidates.
20. **Transferable Intelligence** *(crown jewel)* — pengetahuan yang reusable untuk mengevaluasi project baru;
    indikator yang layak jadi **rule** vs indikator yang **khusus** project ini.
21. **Open Questions** — yang belum diketahui, hipotesis, research gap.
22. **Evidence Level** — untuk tiap kesimpulan penting: **HIGH / MEDIUM / LOW** + alasan.

## How the 22 sections map into CIF

| Gemini § | CIF target |
|----------|-----------|
| 2 | `docs/Ontology/Context.md` snapshot (industry state, competitors, macro — as of the events discussed) |
| 3 | `docs/Ontology/Identity.md`, `Team.md` |
| 4 | `docs/Innovation/*` |
| 5, 10 | `docs/Ontology/Technology.md`, `docs/TokenLifecycle/*` |
| 6 | `docs/Ontology/Funding.md` (Observable) + `docs/Ontology/Hidden.md` if a strategic rationale is stated |
| 7 | `docs/Ontology/Community.md`, `docs/Success/Community.md` |
| 8 | `docs/Meta/Narratives.md` → also part of `docs/Ontology/Context.md` (narrative context) |
| 9 | `docs/Valuation/Competitors.md`, `docs/Meta/MarketCycles.md` → also `docs/Ontology/Context.md` |
| 11, 12 | `docs/Ontology/Tokenomics.md`, `Incentives.md`; `docs/Patterns/Points,Mining,Referral` |
| 13 | `docs/TokenLifecycle/*`, `docs/MarketBehaviour/*`, `docs/Valuation/*` |
| 14 | `docs/Ontology/Revenue.md`, `Adoption.md`, `Metrics.md` |
| 15 | **POV Success-Matrix** (see below) + `docs/Success/*` — also the Stakeholder Reactions field of any `DecisionEvent` |
| 16, 17 | Dossier timeline — **extract each major turning point as a `docs/Ontology/DecisionEvent.md` instance** + current snapshot |
| 18, 19 | `docs/Patterns/*`, `docs/Ontology/*`, `docs/Schema/*`, **`docs/Ontology/DecisionEvent.md`** (the crown-jewel sections are largely a set of Decision Events) |
| 20 | `docs/Reasoning/*` (rule candidates) — state the **Context range** each candidate rule holds under |
| 21 | Dossier "Open Questions" field |
| 22 | **Evidence Level** field → `docs/Reasoning/Confidence.md` |

## Standard fields introduced by this brief

- **POV Success-Matrix** — every deep dossier records success/failure across all 8 POVs, each with an evidence
  level. Example row: `VC: ✅ · Retail: ❌ · Developer: ✅` with per-POV reasons. Binary `examples/Successful/`
  and `Failed/` folders are reserved for clear-cut, single-verdict cases only.
- **Evidence Level (HIGH/MEDIUM/LOW)** — attached to important conclusions; feeds `docs/Reasoning/Confidence.md`.
- **Decision Events** — a dossier's Timeline (§16) and Knowledge Extraction (§19) should identify the
  project's major turning points as explicit Decision Events (`docs/Ontology/DecisionEvent.md`): each with its
  Context snapshot, Trigger, Alternatives, per-POV Stakeholder Reactions, and Short/Long-term Outcome. This is
  the unit patterns are actually discovered from — not the project as a whole.
- **Context snapshot** — required per Decision Event (`docs/Ontology/Context.md`): the industry/competitor/tech/
  macro/hunter-population/VC-climate state *at that time*. This is what prevents a pattern observed in one era
  from being blindly applied to an incompatible one.
- **Observable vs Hidden** — record both (`docs/Ontology/Metrics.md` etc. vs `docs/Ontology/Hidden.md`). Hidden
  factors (motivation, constraint, trade-off, strategic goal) must be grounded in the source or left `unknown` —
  never invented.
- **Open Questions** — explicit research gaps, so later sessions know what is still unvalidated.

## Writing rules (from the brief)
Not an article, summary, or promotion. Always explain cause→effect, industry context, impact, and lesson.
Long and complete is better than losing a small but important detail. Cross-verify; never rely on one source.

## Input Formatting Contract (source authoring — WAJIB)

The report is written **for machine reasoning, not human readers**, and is parsed by `tools/extract.py`. To
keep extraction **lossless and unambiguous**, the source document (`.docx`, exported from the research prompt)
MUST follow this contract. Reports that ignore it still work but risk value↔label mis-association.

1. **`.docx`, markdown-only, single column.** No images, no ASCII/box-drawing diagrams, no multi-column layout,
   no inline citation chips (`[span_1]`, `[1]`, footnote markers) — paste as plain text (Ctrl+Shift+V) to strip
   grounding chips before export.
2. **No tables.** All tabular data as nested **`Label: Value`** bullets — this is the single most important rule.
   A Word table flattens to cell-by-cell text on extraction and its column↔row association is lost. Example:
   ```
   - Funding Round: Seed
     - Date: April 2018
     - Amount: $3,170,000
     - Lead Investor: Multicoin Capital
   ```
3. **Numbered headings, one line each:** `# 1 Executive Summary` … `# 23 Karya yang dikutip`. Never split a
   heading across lines or renumber. (Word heading styles are fine; the number+title is what matters.)
4. **One fact per line/bullet.** Numbers with units + full dates. Never round away or drop a figure.
5. **Flag conflicts, don't smooth them:** write `INKONSISTENSI: …` + `Evidence Level: LOW`. Never fabricate.
6. **§15 = 8 POVs, separated:** Founder, VC, Retail, Community, Developer, Institution, Validator, Builder —
   each with Verdict + Alasan + Tingkat Keyakinan.
7. **§23 Karya yang dikutip:** numbered source list `Title — URL`, no inline chips.

The maintainer's external research prompt embeds this contract in its `FORMATTING CONTRACT` block (the prompt
itself is kept local, not in the repo).

## Ingest tooling (deterministic, no LLM/API)

Support tooling for the `Ingest-Deep` runbook lives in `tools/` and is quality-preserving (it never writes the
dossier — synthesis stays human/LLM reasoning):

- **`tools/extract.py`** — `.docx`/`.pdf` → clean reflowed markdown. Detects `N Title` and `N. TITLE` headings
  (v1 and v2 numbering styles), strips citation chips, and reconstructs any legacy Word tables **table-aware**
  (`<w:tbl>/<w:tr>/<w:tc>` → proper rows) so no cell is scrambled. This is step 1 of the runbook (also archive
  the original under `doc_backup/`).
- **`tools/reconcile.py`** — audit stamp. Diffs the extracted source against the finished dossier and reports
  which **key figures** (currency, %, unit-suffixed magnitudes) are not represented in the dossier. Unit-aware
  (`juta`=1e6, `miliar/mrd`=1e9) to avoid format-only false positives. Run after writing each dossier; a clean
  report is the per-ingest fidelity proof for later audit. Heuristic (flags for human review), not a correctness
  proof — a rounded value (e.g. `$72,248,571 → $72,25 juta`) is a faithful match, not a miss.

### Automated batch ingest — `tools/ingest.py` (no LLM at all)

For scale (usage-limit constrained), the whole ingest can run **without an LLM**, because the reasoning is
already in the Gemini 22-section report — the program only transforms and files it:

```
# 1. drop raw reports in the inbox
cp *.docx doc_backup/inbox/
# 2. one command: extract -> 22-section split -> CIF dossier + cross-links -> archive -> rebuild JSON + backtest
python3 tools/ingest.py
```

Each `<Project>_<YYYY-MM>_gemini.docx` becomes `examples/CaseStudies/<Project>.md`: a **faithful restructure**
of the source into CIF format with the section→ontology `_ref:` links applied from the fixed mapping above.
`ingest.py` auto-detects v1 (22-section) vs v2 (Causal Event Graph) and applies the matching ref-map
(`DEEP_REF` vs `DEEP_V2_REF`) — see "Format v2" above. It never fabricates or distils. `build_json.py` then
**auto-discovers** the new dossiers from the filesystem (dedup by path), so **no DatasetIndex edit is needed**
for the pipeline to see them. **Merges** (a v2 report arriving for a project that already has a v1 dossier)
are *not* automated — hand-merge per the worked example in `examples/CaseStudies/Solana.md`, since deciding
what to keep/flag-as-inconsistent is a judgment call.

**Honest scope:** this yields ~90–95% of a hand-authored dossier — everything the source contains, structured
and cross-linked, but **not** distilled/condensed and without novel synthesis or subtle-inconsistency catching.
Run a periodic LLM/human QC pass on a sample (`tools/reconcile.py` helps), and refine category/era in
`DatasetIndex.md` when convenient. Use this when Claude budget is the bottleneck; use the hand-authored
`Ingest-Deep` role when a project deserves the extra distillation (top anchors).

### One-command pipeline & the three inbox types

`./run.sh` (repo root) chains ingest → build_json → backtest. Drop raw reports by type; ingest is
**anti-duplicate** (existing outputs are skipped, so re-running only processes newly added files):

| Inbox | Type | Contract | Output |
|-------|------|----------|--------|
| `doc_backup/inbox/deep/` | deep (1 project) | 22-section brief | `examples/CaseStudies/<P>.md` |
| `doc_backup/inbox/batch/` | batch (N projects) | each project starts with a line `PROJECT: <Name>` | `examples/Pioneer/<P>.md` |
| `doc_backup/inbox/sentiment/` | sentiment (1 project) | `docs/Protocol/Sentiment-Brief.md` (8 sections) | `examples/Sentiment/<P>.md` |

Fundamental (`CaseStudies/`) and Sentiment (`Sentiment/`) are **separate modules** linked both ways — contexts
never mix. `build_json.py` auto-discovers all three and emits `poc/cif.json` (schema `cif-export/1`) plus split
JSONs for any LLM/app that needs tracking · signal · prediction data (see `poc/README.md`).
