# dYdX — Deep Case Study

**CIF Dataset — Deep Dossier · Tier: Deep (anchor project)**
**Source:** Deep Research (Gemini) — *"Laporan Rekonstruksi Ekosistem dYdX: Analisis Arsitektur, Tokenomika
Defensif, dan Pivot RWA Arcus"*.
**Pipeline position:** Applications layer — anchor artifact structured against the full `docs/` ontology.
The **pioneer on-chain perp-derivatives DEX** and canonical **app-layer value-accrual-failure → buyback-reform**
analog (mirrors Cosmos D7 at the application layer). **Supersedes** the Batch-02 Summary `examples/Pioneer/dYdX.md`.
**Raw source archived:** `doc_backup/deep/dYdX_2026-07_gemini.docx` (+ `.md` text extraction).
**Input note:** authored in the CIF no-table contract; extracted via `tools/extract.py` (0 tables, 0 chips,
23 sections); fidelity checked with `tools/reconcile.py`.

> Knowledge artifact (real curated data), not a documentation container. This is a **deep dossier**: it
> preserves *causality* (why events happened), which is the raw material for prediction. Conforms to
> `templates/CaseStudyTemplate.md`.

---

## 1. Identity
_ref: `docs/Ontology/Identity.md`_

- **Project:** dYdX (token: DYDX).
- **Category:** DeFi — **DEX derivatif perpetual** berbasis **buku order hibrida** (bukan AMM). Appchain (v4).
- **Era:** 2017 (SF) – sekarang. **Founder:** **Antonio Juliano** (eks-Coinbase/Uber/MongoDB, Princeton CS 2015).
- **Innovation archetype:** **Fast Follower** — mereplikasi order-book CEX ke on-chain via teknologi penskalaan
  termutakhir. → `docs/Innovation/FastFollower.md`. **Volume seumur hidup >$1,55 triliun.**
- **Arc utama:** pionir → didisrupsi **Hyperliquid** (pangsa 75%→7%) → reformasi **buyback 75%** → **pivot RWA (Arcus/Robinhood)**.

## 2. Classification
_ref: `docs/Ontology/Classification.md`, `docs/Taxonomy/Sectors.md`, `docs/Taxonomy/Technologies.md`_

DeFi derivatif · evolusi **L1 Ethereum (v1/v2) → L2 StarkEx zk-rollup (v3) → Sovereign Appchain Cosmos SDK/
CometBFT (v4) → pivot Robinhood Chain/Arbitrum L2 (Arcus)** · order book off-chain + settlement on-chain ·
value-accrual via **buyback 75% net revenue** (pasca-Prop #313). → `docs/Taxonomy/Chains.md`.

## 3. Pre-Conditions — Order Book Gap di DeFi (2017)
_Konteks: mengapa dYdX harus ada._
_ref: `docs/Meta/Narratives.md`, `docs/Ontology/Security.md`_

CEX kustodian dominan (risiko sistemik — **Mt. Gox 850.000 BTC** hilang 2014). DEX gen-1 (EtherDelta) di
Ethereum L1 lumpuh (blok 12–15 dtk, gas mahal per order/cancel). **AMM (Uniswap, x·y=k)** memecahkan likuiditas
spot ekor-panjang tetapi **tak efisien untuk derivatif/margin** (price impact, slippage). Pedagang profesional
butuh **order book** (limit order presisi, kedalaman, spread ketat) → tetap di CEX. Celah: **DEX non-kustodian
sekecepatan CEX**. dYdX lahir di momentum eksplorasi L2. → `examples/Pioneer/Uniswap.md` (kontras AMM vs order book).

## 4. Origin & Team
_ref: `docs/Ontology/Team.md`, `docs/Project/Philosophy.md`_

**Antonio Juliano** (SF, 2017; sebelumnya bangun Weipoint — dihentikan 5 bulan). Tim inti: **Brendan Chou**
(lead eng, eks-Google SRE/Bloomberg), **Bryce Neal** (eks-Square/Amazon), **David Gogel** (growth, Wharton MBA);
**Eddie Zhang** (President dYdX Labs, Agu 2025, via akuisisi **Pocket Protector**). Advisor: **Fred Ehrsam**
(co-founder Coinbase & Paradigm), Steve Jang, Barry Kwok. *"Coinbase Mafia"* membuka akses VC papan atas sejak awal.

## 5. Innovation Analysis — Order Book Hibrida → Appchain
_ref: `docs/Ontology/Innovation.md`, `docs/Innovation/FastFollower.md`, `docs/Innovation/CompetitiveMoat.md`, `docs/Ontology/Technology.md`_

1. **Hybrid L2 Order Book (v3, StarkEx):** matching engine + order book **off-chain terpusat** (dYdX Labs, sub-detik);
   settlement via **StarkEx zk-rollup** (bukti STARK ke Ethereum L1) → **tanpa gas untuk order/cancel** (masalah utama DEX L1).
2. **Sovereign L1 Appchain (v4):** dYdX Chain (**Cosmos SDK + CometBFT**) — tiap validator jalankan order book di
   **mempool** terdistribusi, matching per blok on-chain; **~20.000 ops/detik**. *(Membuktikan dApp besar bisa
   jadi blockchain mandiri — validasi tesis appchain Cosmos, `examples/CaseStudies/Cosmos.md` §8.)*
3. **MegaVault + Instant Listings (dYdX Unlimited, Nov 2024):** master liquidity pool (deposit USDC → yield);
   **permissionless listing** pasar perp baru (jaminan **10.000 USDC**, tanpa governance).

*Dampak:* menginspirasi **Hyperliquid, Vertex, Aevo** (appchain khusus perp) — yang lalu **mengalahkan dYdX** (§9).

## 6. Technology Evolution
_ref: `docs/Ontology/Technology.md`, `docs/TokenLifecycle/*`, `docs/Ontology/Infrastructure.md`_

- **v1 Solo (Okt 2018):** margin/spot L1 Ethereum. **v2 (2020):** isolated margin — lumpuh saat DeFi Summer gas.
- **v3 (Feb 2021):** StarkEx zk-rollup L2; perp cross-margin, leverage 20×; **sunset 28 Okt 2024** (konsolidasi ke v4).
- **v4 (Okt 2023):** dYdX Chain (Cosmos SDK/CometBFT); order book terdesentralisasi penuh.
- **2025–26 latency/ritel:** **Designated Proposer Model** (Sep 2025), **OEGS** (one-hop trader↔proposer);
  **Arcus (Jul 2026):** di **Robinhood Chain** (Arbitrum EVM L2) — spot saham AS terdigitalisasi tanpa fee +
  perp RWA leverage **50×**.

## 7. Funding Intelligence
_ref: `docs/Ontology/Funding.md`, `docs/Ontology/Tokenomics.md`, `docs/TokenLifecycle/TGE.md`_

| Putaran | Tanggal | Dana | Valuasi | Investor kunci |
|---|---|---|---|---|
| **Seed** | 19 Des 2017 | $2 juta *(PitchBook $1,96 juta — LOW)* | ~$20 juta | **Polychain, a16z**, Brian Armstrong, Fred Ehrsam |
| **Series A** | 19 Okt 2018 | $10 juta | ~$100 juta | **a16z**, Bain, Polychain, Naval, Dragonfly |
| **Series B** | 26 Jan 2021 | $10 juta | ~$100 juta | **3AC, DeFiance**, a16z, Paradigm, Wintermute |
| **Series C** | 15 Jun 2021 | **$65 juta** | ~$650 juta | **Paradigm**, a16z, Polychain, 3AC, StarkWare, Electric, Delphi |
| **Foundation Strategic Grant** | 11 Agu 2025 | $8 juta | — | dYdX Foundation (self-fund) |

*(INKONSISTENSI total: Wellfound $87 juta vs RootData $85 juta — LOW.)* **Risiko struktural:** VC menguasai
**27,73%** suplai genesis → hambatan narasi desentralisasi murni yang **dieksploitasi Hyperliquid** (tanpa VC). → §9.

## 8. Tokenomics — Governance-Only → 75% Buyback
_ref: `docs/Ontology/Tokenomics.md`, `docs/Ontology/Incentives.md`, `docs/MarketBehaviour/UnlockImpact.md`, `docs/Patterns/Flywheel.md`_

**Mint:** **1 miliar DYDX** (3 Agu 2021), rilis 5 tahun (s/d Jun 2026). **Alokasi:** Community **50%** (**500
juta** — Trading Rewards 25%/**250 juta**, Retroactive Mining 7,5%/75 juta, LP Rewards 7,5%/75 juta, Treasury
5%/50 juta, USDC Staking Pool 2,5%/25 juta, Safety Staking Pool 2,5%/25 juta) · **Investors 27,73%** (277,3
juta) · **Founders/Employees/Advisors 15,27%** (152,7 juta) · Future Employees **7%** (70 juta). **Insider vesting:** 30% (Des 2023), 40% (Jan–Jun 2024), 20% (Jul 2024–Jun 2025),
10% (Jul 2025–Jun 2026). **Emisi −50%** (Jun 2025); inflasi perpetual maks **2%/th** dari 3 Agu 2026.

**wethDYDX bridge sunset *(causal event)*:** proposal 9 Jun 2025, deprecated **13 Jun 2025**; migrasi 1:1 **>94%**;
**~14% (41,66 juta DYDX) terdampar** di Ethereum, **~13.800 dompet** rugi tanpa opsi migrasi → gejolak politik.

### Reformasi buyback *(causal core — value accrual)*
Distribusi fee v4: Staking **15%**, MegaVault **5%**, Treasury subDAO **5%**, **Buyback 75%**. Eskalasi:
launch **23 Apr 2025** (Prop #225 **12,5%**) → Prop #231 **25%** → **Prop #313 75%** (**13 Nov 2025**). Buyback
terkumpul **8,46 juta DYDX ($1,72 juta)** per 1 Jan 2026 → mengubah DYDX dari **token tata kelola kosong** jadi
**aset penangkap nilai**. → §19 pola; mirror Cosmos value-accrual fix.

## 9. Airdrop, Community & Competitive Landscape
_ref: `docs/Patterns/Points.md`, `docs/Success/Airdrop.md`, `docs/Ontology/Community.md`, `docs/Valuation/Competitors.md`, `docs/MarketBehaviour/DeathSpiral.md`_

**Retroactive airdrop (Sep 2021):** **7,5% (75 juta DYDX)**; snapshot 26 Jul 2021; **Epoch 0 milestone** (wajib
trading untuk klaim penuh, sisa hangus→Treasury); **AS diblokir**. *Cerdas* (memaksa adopsi L2, order book tebal)
tetapi memicu **wash trading** + **dump** (tanpa vesting ritel). **Epoch (28 hari) trading rewards** → yield farmer
melikuidasi → tekanan harga. Program lanjut: **dYdX Surge $20 juta**, Trading Leagues ($1 juta), Fee Holidays
(BTC/SOL, +2–3× volume), Affiliate Booster (15–50% USDC).

### Disrupsi Hyperliquid *(causal core)*
Awal (2021–23): unggul GMX/Synthetix (order book pro; **TVL puncak $1,1 mrd Okt 2021**). Lalu **Hyperliquid**
mengeksploitasi **tiga kelemahan**:
1. **Value accrual** — v3 100% fee ke **dYdX Trading Inc**; v4 fee ke validator/staker (USDC) **tanpa tekanan
   beli DYDX**. Hyperliquid **Assistance Fund** = **97–99% fee harian buyback HYPE**.
2. **Friksi UX** — Cosmos bridging lambat + latensi ~1 dtk vs Hyperliquid **sub-detik + deposit USDC instan**.
3. **VC pressure** — investor 27,73% + tim 15,27% vs Hyperliquid **31% airdrop, tanpa VC**.

**Dampak:** pangsa volume **75% (awal 2023) → ~7% (akhir 2024)**; volume bulanan dYdX **$20 mrd** vs Hyperliquid
**$200 mrd**. *(Hyperliquid = kandidat gap dataset.)* **Arcus** (Robinhood Chain) hindari perang perp-kripto →
lawan Lighter/Meridian/SynFutures; keunggulan = **distribusi 25 juta user Robinhood**.

## 10. Narrative Intelligence
_ref: `docs/Meta/Narratives.md`, `docs/Patterns/Narrative.md`, `docs/Meta/MarketCycles.md`_

| Fase | Narasi | Peran |
|---|---|---|
| 2020–21 | DeFi Summer / L2 "CEX-Killer" (StarkEx, tanpa gas) | **Pencipta** |
| 2023–24 | Kedaulatan Appchain (dYdX Chain/Cosmos) | **Pencipta** |
| 2025 | Telegram mini-app & social trading (Pocket Protector) | **Pengikut cepat** |
| 2026 | RWA & saham tokenisasi (Arcus/Robinhood) | **Pencipta/pivot** |

## 11. Token Lifecycle & Price Causality
_ref: `docs/MarketBehaviour/*`, `docs/Valuation/FairValue.md`, `docs/Reasoning/Prediction.md`_

- **ATH:** **$2,7291** (6 Des 2024) *atau* **$4,52** (7 Mar 2024) — *(INKONSISTENSI: pemisahan tracking ethDYDX
  ERC-20 vs native DYDX Cosmos; LOW)*.
- **ATL:** **$0,07881** (8 Mar 2026). Apr 2026 ~$0,10–0,12 (di bawah SMA-200 $0,276) — **−95%+ dari ATH** (kalah
  Hyperliquid + kemarahan bridge). MM: **Pulsar** (loan 250k DYDX, 12 bln, exp 14 Mei 2026).
- **Fair value:** **undervalued** — **buyback 75%** memberi lantai penyerapan pasokan konstan. → `docs/Valuation/FairValue.md`.

## 12. Business Intelligence & Arcus/RWA
_ref: `docs/Ontology/Revenue.md`, `docs/Valuation/Revenue.md`, `docs/Ontology/Metrics.md`, `docs/Valuation/TVL.md`, `docs/Ontology/Adoption.md`_

**dYdX (Jan 2026):** volume seumur hidup **>$1,55 triliun**; cumulative fees **$64,7 juta**; staking rewards
dibagikan **$48 juta** USDC; holders **98.200**; staked **>240 juta DYDX**; buyback 8,46 juta DYDX ($1,72 juta);
MegaVault TVL **>$79 juta**. **Net earnings:** Q2 2024 **$20,1 juta → Q2 2025 $3,2 juta (−84,07% YoY)**. **TVL:**
puncak **$1,1 mrd** (Okt 2021) → **$312 juta** (mid-2025).

**Arcus/Robinhood Chain (Jul 2026):** Arcus TVL **$14,3 juta** (peringkat #3 di rantai); Robinhood Chain TVL
**$193 juta** (Morpho $116 juta, Uniswap $61 juta); DEX volume >$750 juta; app fees ~$40 juta (Uniswap 66,4%);
**95 saham tokenisasi** (mcap $17,7 juta; aktif di DeFi hanya **$721 ribu**), **35 pasar perp RWA**. *(Adopsi
saham tokenisasi masih embrio; jalur pemulihan di luar kripto murni.)* → `examples/CaseStudies/Avalanche.md` (RWA), `examples/Pioneer/Uniswap.md`.

## 13. POV Success-Matrix (§15)
_ref: `docs/Success/*`, `docs/Reasoning/Explainability.md`, `docs/Reasoning/Confidence.md`_

| POV | Verdict | Alasan | Evidence |
|-----|---------|--------|----------|
| **Founder** (`Success/Founder.md`) | ⚠️ Campuran | Bina perp DEX triliunan; tapi **Juliano mundur (Mei 2024) → kembali (Okt 2024)** + PHK **35%**; Arcus = kecerdikan taktis | HIGH |
| **VC** (`Success/VC.md`) | ✅ Sukses | Token murah ($20–100 juta val) + cair sebelum devaluasi pasca-2024 | HIGH |
| **Retail** (`Success/Community.md`) | ❌ Gagal | Harga −95%+; token terkunci akibat sunset bridge wethDYDX | HIGH |
| **Community** (`Success/Community.md`) | ⚠️ Campuran | Hibah stabil; tapi perpecahan politik dominasi validator (bridge) | HIGH |
| **Developer** (`Success/Developer.md`) | ✅ Sukses | Buktikan appchain L1 Cosmos performa tinggi; Designated Proposer, OEGS | HIGH |
| **Institution** (`Success/Adoption.md`) | ⚠️ Campuran | Permissioned Keys & fee sederhana disambut; tapi likuiditas turun hambat MM | MEDIUM |
| **Validator** (`Success/Protocol.md`) | ✅ Sukses | Amankan dYdX Chain + komisi USDC dari staker | HIGH |
| **Builder** (`Success/Ecosystem.md`) | ✅ Sukses | Integrasi mulus IBC, Osmosis, oracle | HIGH |

**Takeaway:** menang di VC/developer/validator/builder; **gagal** retail; **campuran** founder/community/institution.
Kegagalan inti = **tokenomika tata kelola kosong** (value accrual), diperbaiki telat via buyback 75%.

## 14. Historical Timeline
_ref: `docs/TokenLifecycle/*`_

- **19 Des 2017** — Seed $2 juta. **3 Okt 2018** — v1 mainnet (Ethereum). **19 Okt 2018** — Series A $10 juta.
- **26 Jan 2021** — Series B $10 juta (3AC). **Feb 2021** — v3 L2 (StarkEx). **15 Jun 2021** — Series C $65 juta (Paradigm). **3 Agu 2021** — mint 1 mrd DYDX. **Sep 2021** — retroactive airdrop.
- **Nov 2022** — kolaps FTX → user dYdX **+39%**. **26/31 Okt 2023** — genesis/mainnet **dYdX Chain v4**.
- **13 Mei 2024** — **Juliano mundur** (→ Ivo Crnkovic-Rubsamen). **Agu 2024** — **Hyperliquid lampaui volume dYdX**. **10 Okt 2024** — **Juliano kembali CEO**. **28 Okt 2024** — sunset v3. **30 Okt 2024** — PHK 35%. **19 Nov 2024** — dYdX Unlimited (MegaVault).
- **23 Apr 2025** — buyback pertama (12,5%). **13 Jun 2025** — sunset bridge wethDYDX (14% terdampar). **18 Jul 2025** — akuisisi Pocket Protector. **Sep 2025** — Telegram trading. **13 Nov 2025** — **Prop #313 (buyback 75%)**. **11 Des 2025** — spot Solana.
- **1 Jul 2026** — **Arcus di Robinhood Chain**.

## 15. Current Status & Lessons Learned
_ref: `docs/TokenLifecycle/Maturity.md`, `docs/Patterns/Failure.md`, `docs/Patterns/Recovery.md`_

**Status (pertengahan 2026):** **bifurkasi** — dYdX Chain v4 stagnan ($3,2 juta Q2 2025) tapi stabil (>240 juta
DYDX staked, lantai buyback 75%); pertumbuhan bertumpu pada **Arcus** ($14,3 juta TVL, RWA/Robinhood).

**Pelajaran:**
1. **Value Accrual Over Governance** — mengisolasi fee ke kas perusahaan + token tata kelola kosong = kalah dari
   pesaing yang bagi hasil ke pemegang token.
2. **User Friction = pembunuh tersembunyi** — pindah L2→Cosmos L1 (bridging manual) bertepatan dengan pesaing sub-detik.
3. **Sunset bridge tanpa kompensasi** merusak integritas (13.800 dompet).
4. **Founder Pivot Agility** — restrukturisasi + Telegram + Arcus/Robinhood = adaptasi menjauh dari perp-kripto jenuh.

## 16. Knowledge Extraction — Patterns & Lessons (§18–19)
_ref: `docs/Patterns/*`, `docs/Reasoning/*`, `docs/Schema/PatternSchema.md`_

1. **Governance-Token Vulnerability** *(crown, app-layer mirror of Cosmos)* — *fee ke kas terpusat → token hanya
   tata kelola + emisi tinggi → tekanan jual ritel tanpa penyerapan → harga merosot → kalah saat pesaing buyback.*
   → `docs/Valuation/FairValue.md`, `examples/CaseStudies/Cosmos.md` §19.
2. **Buyback Accrual Redesign** *(the fix)* — *volume turun → redesain token → alokasikan >70% pendapatan
   operasional ke buyback harian → penyerapan pasokan konstan.* → `docs/Patterns/Flywheel.md`, `docs/Ontology/Tokenomics.md`.
3. **Traditional-Broker Integration Pivot** — *pasar perp-kripto jenuh → rantai patuh hukum → bursa saham
   tokenisasi/RWA → integrasi langsung ke broker berlisensi (jutaan nasabah) → likuiditas non-kripto.*
   → `docs/Innovation/CompetitiveMoat.md`, `docs/Meta/Narratives.md`.
4. **User-Friction Volume Drain** — migrasi L2→sovereign L1 dengan bridging manual > 2 langkah → penyusutan
   volume signifikan. → `docs/Patterns/Failure.md`.
5. **Uncompensated Bridge Sunset** — penutupan bridge via voting validator merugikan pemegang pasif. →
   `docs/Ontology/Governance.md`, `docs/Ontology/Risks.md`.
6. **Milestone-Gated Airdrop → Wash Trading** — syarat volume klaim memaksa adopsi tapi memicu wash trading + dump.
   → `docs/Success/Airdrop.md`, `docs/MarketBehaviour/DeathSpiral.md`.

### Entitas & relasi ontologi (kandidat Knowledge Graph)
_ref: `docs/Schema/KnowledgeGraph.md`, `docs/Schema/EntityRelationship.md`_
- `[Antonio_Juliano] —founded→ [dYdX_Labs]` · `[dYdX_Labs] —developed→ [dYdX_Chain]` · `—acquired→ [Pocket_Protector]`
- `[dYdX_Chain] —builtOn→ [Cosmos_SDK/CometBFT]` · `[dYdX_v3] —settledVia→ [StarkEx]`
- `[dYdX_Labs] —developed→ [Arcus]` · `[Arcus] —operatesOn→ [Robinhood_Chain]` · `—partneredWith→ [Robinhood]`
- `[Prop_313] —allocates75%RevenueTo→ [DYDX_Buyback]` · `[Hyperliquid] —disrupted→ [dYdX_MarketShare]`

## 17. Transferable Intelligence (§20) — rule candidates untuk DEX derivatif baru
_ref: `docs/Reasoning/AnalogEngine.md`, `docs/Reasoning/Weighting.md`, `docs/Reasoning/Confidence.md`_

- **R1 — Value Capture Distribution Rule:** DEX yang menyalurkan fee riil hanya ke tim / insentif emisi inflasi
  = **risiko tinggi**; skor superior **hanya** jika **>50% pendapatan riil harian (USDC)** dipakai **buyback
  on-chain** di pasar sekunder. *(dYdX gagal → Hyperliquid menang; dYdX perbaiki via 75%.)*
- **R2 — Max User Friction Threshold:** pindah dari L2 terintegrasi ke L1 berdaulat yang menuntut **bridge manual
  >2 langkah** → depresiasi potensi volume **≥40%**; tanpa deposit satu-klik dari L1 besar, turunkan skor.
- **Khusus-dYdX/Arcus:** nilai bursa RWA berbasis broker (Arcus) via **rasio konversi nasabah Robinhood → pelaku
  perp on-chain**, bukan metrik DEX biasa (bergantung lisensi & distribusi tertutup).

## 18. Open Questions (§21)
_Research gap — belum tervalidasi._
1. Bisakah **Arcus** mengonversi ritel Robinhood jadi pelaku **perp RWA 50×** berkelanjutan (butuh literasi risiko
   tinggi)? (evidence: LOW)
2. Adakah kompensasi struktural untuk **14% / 41,66 juta DYDX / 13.800 dompet** yang terdampar pasca-sunset bridge? (MEDIUM)
3. Status hukum kepatuhan dYdX Labs menawarkan spot/perp di **yurisdiksi AS**? (MEDIUM)

## 19. Evidence Level — kesimpulan kunci (§22)
_ref: `docs/Reasoning/Confidence.md`, `docs/Research/Verification.md`_

| Kesimpulan | Evidence | Alasan |
|---|---|---|
| Struktur pendanaan Seed→Series C | **HIGH** | Dokumen resmi dYdX, cap table PitchBook, blog Paradigm |
| Kekalahan pangsa pasar ke Hyperliquid | **HIGH** | Data volume bulanan on-chain + struktur biaya komparatif |
| Dampak sunset bridge wethDYDX (~13.800 dompet) | **MEDIUM** | Forum tata kelola; nilai nominal belum diaudit eksternal |
| Prospek Arcus RWA di Robinhood | **LOW** | Baru Jul 2026; tren retensi masih spekulatif |

## 20. Related Framework Definitions
- **Ontology:** `docs/Ontology/Identity.md`, `Team.md`, `Funding.md`, `Tokenomics.md`, `Incentives.md`,
  `Governance.md`, `Technology.md`, `Infrastructure.md`, `Security.md`, `Risks.md`, `Ecosystem.md`, `Community.md`, `Revenue.md`, `Metrics.md`, `Adoption.md`, `Innovation.md`
- **Innovation:** `docs/Innovation/FastFollower.md`, `CompetitiveMoat.md`, `Execution.md`, `ProductMarketFit.md`
- **Patterns:** `docs/Patterns/Flywheel.md`, `Failure.md`, `Recovery.md`, `Narrative.md`; `docs/MarketBehaviour/DeathSpiral.md`, `UnlockImpact.md`
- **Valuation/Market:** `docs/Valuation/FairValue.md`, `Revenue.md`, `Competitors.md`, `TVL.md`; `docs/Meta/Narratives.md`, `MarketCycles.md`
- **Reasoning:** `docs/Reasoning/Prediction.md`, `AnalogEngine.md`, `Confidence.md`, `Weighting.md`
- **Success:** `docs/Success/*` · **Schema:** `docs/Schema/KnowledgeGraph.md`, `EntityRelationship.md`, `PatternSchema.md`
- **Cross-project analogs:** `examples/CaseStudies/Cosmos.md` (dYdX Chain = flagship appchain + **same value-accrual
  pattern** at app layer), `Avalanche.md` (RWA + 3AC exposure), `examples/Pioneer/Uniswap.md` (AMM vs order book),
  `examples/Pioneer/Optimism.md`/`LayerZero.md` (L2/interop). **Supersedes:** `examples/Pioneer/dYdX.md` (Summary).
- **Gap candidate:** **Hyperliquid** (the disruptor — appchain perp DEX, aggressive buyback, no-VC airdrop).

## 21. Sources
_Deep Research provenance (Gemini). Laporan sumber mengutip **59 referensi**; sumber primer/kunci di bawah._

- Introducing DYDX (token & allocation) — dYdX Foundation — https://www.dydx.foundation/blog/introducing-dydx-token
- dYdX Closes $65M Series C — dYdX — https://www.dydx.xyz/blog/series-c
- dYdX Token Transparency Filing — Blockworks — https://blockworks.com/token-transparency/filing/dydx--2
- dYdX Foundation Allocates 75% of Protocol Revenue for Token Buyback — Binance Square — https://www.binance.com/en/square/post/11-13-2025-dydx-foundation-allocates-75-of-protocol-revenue-for-token-buyback-32336305438890
- dYdX Passes Landmark Buyback (75% of Revenue) — 99bitcoins — https://99bitcoins.com/news/altcoins/dydx-pass-landmark-buyback-allocating-75-of-revenue-to-dydx-token-repurchases/
- [DRC] Cease support for the wethDYDX bridge — dYdX Forum — https://dydx.forum/t/drc-cease-support-for-the-wethdydx-smart-contract-i-e-the-bridge-on-the-dydx-chain-side/3619
- Antonio Juliano returns as CEO after six months — The Block — https://www.theblock.co/post/320502/dydx-trading-founder-antonio-juliano-returns-as-ceo-after-stepping-away-for-six-months
- dYdX Launches Permissionless Listings (Unlimited) — The Defiant — https://thedefiant.io/news/defi/dydx-launches-permissionless-listings-with-unlimited-upgrade
- dYdX collaborates with Robinhood to launch Arcus — Bitget — https://www.bitget.com/asia/amp/news/detail/12560605489681
- Who Is the Biggest Winner of the Robinhood Chain Launch? — Oak Research — https://oakresearch.io/en/analyses/investigations/who-is-biggest-winner-robinhood-chain-launch-uniswap-but-not-really
- Exploring Hyperliquid: Redefining Derivatives Trading — VanEck — https://www.vaneck.com/nl/en/blog/digital-assets/exploring-hyperliquid-redefining-derivatives-trading/
- The Tokenomics of dYdX — Findas — https://www.findas.org/tokenomics-review/coins/the-tokenomics-of-dydx/r/Vm8xr9SHi31vNF6qQCiRv3
- Annual Report 2025 — dYdX — https://www.dydx.xyz/annual-report/annual-report-2025
- dYdX acquires Pocket Protector — LA Times — https://www.latimes.com/b2b/banking-finance/story/2025-07-28/dydx-acquires-pocket-protector

_(Full 59-source bibliography retained in the original Deep Research report + archived at
`doc_backup/deep/dYdX_2026-07_gemini.md`.)_
