# Deep Research Brief (canonical)

This is the **maintainer's canonical research prompt** used to generate deep reports (via Gemini) for
anchor projects. Every deep report arrives in this **22-section structure**, so the `Ingest-Deep` role maps
its output losslessly. Read this before ingesting any deep report.

**Audience of the output = AI reasoning, not human readers.** Every fact must be *Reusable Knowledge*: it
must answer **APA · MENGAPA · BAGAIMANA · APA DAMPAKNYA · APA PELAJARANNYA · APA HUBUNGANNYA DENGAN INDUSTRI**.
Bare facts without causality are not useful to this system.

**Projects are not random, and not binary "success/fail":**
- They have **types** (innovation archetype: First Mover / Fast Follower / Fork / Improvement; narrative type).
- Success/failure is judged **per point-of-view** — a project can succeed for VC and fail for Retail. The
  eight POVs are: **Founder, VC, Retail, Community, Developer, Institution, Validator, Builder** (§15).

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
| 2 | Dossier "Pre-conditions" (context) |
| 3 | `docs/Ontology/Identity.md`, `Team.md` |
| 4 | `docs/Innovation/*` |
| 5, 10 | `docs/Ontology/Technology.md`, `docs/TokenLifecycle/*` |
| 6 | `docs/Ontology/Funding.md` |
| 7 | `docs/Ontology/Community.md`, `docs/Success/Community.md` |
| 8 | `docs/Meta/Narratives.md` |
| 9 | `docs/Valuation/Competitors.md`, `docs/Meta/MarketCycles.md` |
| 11, 12 | `docs/Ontology/Tokenomics.md`, `Incentives.md`; `docs/Patterns/Points,Mining,Referral` |
| 13 | `docs/TokenLifecycle/*`, `docs/MarketBehaviour/*`, `docs/Valuation/*` |
| 14 | `docs/Ontology/Revenue.md`, `Adoption.md`, `Metrics.md` |
| 15 | **POV Success-Matrix** (see below) + `docs/Success/*` |
| 16, 17 | Dossier timeline + current snapshot |
| 18, 19 | `docs/Patterns/*`, `docs/Ontology/*`, `docs/Schema/*` |
| 20 | `docs/Reasoning/*` (rule candidates) |
| 21 | Dossier "Open Questions" field |
| 22 | **Evidence Level** field → `docs/Reasoning/Confidence.md` |

## Standard fields introduced by this brief

- **POV Success-Matrix** — every deep dossier records success/failure across all 8 POVs, each with an evidence
  level. Example row: `VC: ✅ · Retail: ❌ · Developer: ✅` with per-POV reasons. Binary `examples/Successful/`
  and `Failed/` folders are reserved for clear-cut, single-verdict cases only.
- **Evidence Level (HIGH/MEDIUM/LOW)** — attached to important conclusions; feeds `docs/Reasoning/Confidence.md`.
- **Open Questions** — explicit research gaps, so later sessions know what is still unvalidated.

## Writing rules (from the brief)
Not an article, summary, or promotion. Always explain cause→effect, industry context, impact, and lesson.
Long and complete is better than losing a small but important detail. Cross-verify; never rely on one source.
