# Cosmos — Deep Case Study

**CIF Dataset — Deep Dossier · Tier: Deep (anchor project)**
**Source:** Deep Research (Gemini) — *"Laporan Riset Komprehensif Ekosistem Cosmos (ATOM): Analisis Sejarah,
Evolusi Teknologi, Tata Kelola, dan Dinamika Ekonomi Interchain"*.
**Pipeline position:** Applications layer — an anchor artifact structured against the full `docs/` ontology.
Serves as the **"Internet of Blockchains" appchain First Mover** and the canonical **value-accrual-failure**
analog (technology adoption without token value capture) — the direct mirror of Polkadot's shared-security bet.
**Raw source archived:** `doc_backup/deep/Cosmos_2026-07_gemini.docx` (+ `.md` text extraction).
**Input note:** authored in the CIF no-table markdown contract; extracted via `tools/extract.py` (0 tables,
0 chips, 23 sections); fidelity checked with `tools/reconcile.py`.

> Knowledge artifact (real curated data), not a documentation container. This is a **deep dossier**: it
> preserves *causality* (why events happened), which is the raw material for prediction. Conforms to
> `templates/CaseStudyTemplate.md`.

---

## 1. Identity
_ref: `docs/Ontology/Identity.md`_

- **Project:** Cosmos (token: ATOM; Hub chain-id: **Gaia**).
- **Category:** Layer-0 / "Internet of Blockchains" — sovereign application-specific chains (appchains)
  interkoneksi via IBC. Tiga pilar: **CometBFT** (dulu Tendermint) · **Cosmos SDK** · **IBC**.
- **Era:** 2014 (Tendermint) – sekarang (pertengahan 2026). **Mainnet Hub:** 13 Maret 2019.
- **Founders:** **Jae Kwon** (All in Bits/AIB, konservatif — menolak ATOM sebagai aset moneter) & **Ethan
  Buchman** (governance/sosio-ekonomi, dewan **Interchain Foundation**). ICF (nirlaba Swiss) + AIB (komersial, Delaware).
- **Innovation archetype:** **First Mover** murni pada tesis **appchain**. → `docs/Innovation/FirstMover.md`,
  `docs/Innovation/CategoryCreator.md`. **Kegagalan inti:** *value accrual* ke ATOM.

## 2. Classification
_ref: `docs/Ontology/Classification.md`, `docs/Taxonomy/Sectors.md`, `docs/Taxonomy/Technologies.md`_

Layer-0 modular · **CometBFT** (BFT PoS, finalitas instan <3 dtk, toleransi 1/3) · **ABCI** (agnostik bahasa) ·
**Cosmos SDK** (framework modular Go) · **IBC** (TCP/IP untuk blockchain, light-client, **0% eksploit**) ·
kedaulatan appchain **tanpa shared-security wajib** (sumber kekuatan adopsi & sekaligus krisis value accrual).

## 3. Pre-Conditions — Blockchain Monolitik Terisolasi (2014–2016)
_Konteks: mengapa Cosmos harus ada._
_ref: `docs/Meta/Narratives.md`, `docs/Ontology/Security.md`_

Empat masalah sistemik era monolitik: **skalabilitas/kepadatan** (satu VM → gas volatil), **developer
friction** (bangun BFT & P2P dari nol), **ketiadaan kedaulatan** (tunduk pada tata kelola rantai induk),
**silo** (chain terisolasi; bridge multisig terpusat = risiko). → lahir visi **"Internet of Blockchains":**
tiap aplikasi punya blockchain berdaulat sendiri, tetap bertukar aset/data secara *trust-minimized*.

## 4. Origin & Team — Tendermint & Faksionalisme
_ref: `docs/Ontology/Team.md`, `docs/Ontology/Governance.md`, `docs/Project/Philosophy.md`_

**Tendermint (2014, Jae Kwon + Ethan Buchman)** — konsensus PoS BFT instan; **ABCI** memisahkan lapisan
aplikasi dari konsensus/jaringan. Whitepaper **"Hub and Zone" (2016)** → Cosmos Hub sebagai perantara.

**Dua entitas bertegangan:** **ICF** (nirlaba Swiss — kelola dana ICO 2017, kontrak tim eksternal) vs **AIB /
Tendermint Inc.** (komersial, Jae Kwon). *Konflik kepemimpinan (causal):* **2020 Zaki Manian mundur**,
menuduh Jae Kwon memaksakan "uji loyalitas" & diskriminasi internal → warisan **faksionalisme** yang
membayangi tata kelola hingga 2026 (§10, §15). → `docs/Patterns/Failure.md`.

## 5. Innovation Analysis — CometBFT, SDK, IBC
_ref: `docs/Ontology/Innovation.md`, `docs/Innovation/FirstMover.md`, `docs/Innovation/CompetitiveMoat.md`, `docs/Ontology/Technology.md`_

Arsitektur 3-lapis (aplikasi / konsensus / jaringan):
1. **CometBFT** — BFT PoS, **finalitas instan <3 dtk**, toleransi kegagalan **1/3** voting power; replikasi state deterministik.
2. **ABCI** — antarmuka agnostik bahasa (Go/Rust/Java/Haskell) → logika aplikasi tersambung ke CometBFT tanpa ubah konsensus.
3. **Cosmos SDK** — framework modular open-source terbesar (modul staking/gov/auth/bank/IBC siap pakai).
4. **IBC** — routing nirkustodian ala **TCP/IP**; light-client kriptografis per rantai → transfer trust-minimized;
   **rekam eksploit 0%** sejak rilis.

*Dampak/moat:* jadi **standar industri** — diadopsi **BNB Smart Chain, dYdX Chain, Injective, Osmosis, Celestia**.
*Paradoks (§9, §18):* moat teknologi sangat kuat, tetapi **tanpa pajak keamanan wajib** → adopsi tak menetes
ke nilai ATOM. → cross-link `examples/Pioneer/Celestia.md`, `dYdX.md`, `examples/CaseStudies/BNBChain.md`.

## 6. Technology Evolution — Gaia dari Router Minimalis ke Mesin Aktif
_ref: `docs/Ontology/Technology.md`, `docs/TokenLifecycle/*`, `docs/Ontology/Infrastructure.md`_

- **Testnet (2017–18):** Gaia-6001 (async desentralisasi pertama); Gaia-8001 (stabil >3 bulan, **1 juta blok**).
- **Mainnet (13 Mar 2019):** genesis Hub — staking, ABCI, CometBFT.
- **Theta (2022):** **Interchain Accounts (ICA)** — satu chain mengendalikan akun di chain lain via IBC.
- **Rho (14 Mar 2023):** keamanan modul staking. **Lambda (9 Jul 2023):** efisiensi paket IBC.
- **Sigma (21 Jan 2024):** integrasi **CosmWasm** (kontrak pintar terisolasi).
- **IBC v2 / Eureka (Mar–Apr 2025):** rekonstruksi IBC → konektivitas nirkustodian native ke **Ethereum/EVM**.
- **Cosmos SDK v0.53/v0.54 (2025–26):** **BlockSTM** (eksekusi paralel, target **5.000 TPS**), storage
  **IAVLx**, telemetry OpenTelemetry.

## 7. Funding Intelligence
_ref: `docs/Ontology/Funding.md`, `docs/Ontology/Tokenomics.md`, `docs/TokenLifecycle/TGE.md`_

- **ICO (6 Apr 2017):** **$16,8 juta** *(sumber lain $16–17,3 juta)* dalam **30 menit** *(atau 28)*; masuk
  **4.882,7 BTC + 246.891 ETH**; harga **$0,098/ATOM**; **168 juta ATOM** dialokasikan.
- **Series A (14 Mar 2019):** **$9 juta** *(atau $10 juta)* — lead **Paradigm**, peserta **Bain Capital, 1confirmation**.
- **Realisasi kas ICF (2024):** likuidasi bertahap **21.600 ETH + 295,3 BTC ≈ $78,67 juta** (termasuk 15.100 ETH
  Apr–Okt senilai $37,09 juta + 4.000 ETH Okt senilai $9,5 juta); sisa cadangan Des 2024: 96,4 BTC + 17.188 ETH
  (~$67 juta). Total: modal ICO awal ~$17 juta → **$213,1 juta** nilai kumulatif (likuidasi + cadangan).
- **Kepemilikan genesis:** AIB ~9 juta ATOM (2,26%); ICF 6 juta + 14 juta ATOM. **AIB+ICF gabungan 5,6%** hari ini.
- **INKONSISTENSI:** Tracxn mencantumkan Seed (Google Ventures/Accel 2023) & Series A (Shine/Matrix 2026) —
  **data keliru** (entitas komersial lain bernama serupa). **Evidence LOW** untuk Tracxn; **HIGH** untuk ICO 2017 + Series A Paradigm 2019.

## 8. Tokenomics — Anggaran Keamanan, Bukan Token Gas
_ref: `docs/Ontology/Tokenomics.md`, `docs/Ontology/Incentives.md`, `docs/Ontology/Governance.md`, `docs/MarketBehaviour/UnlockImpact.md`_

ATOM didesain sebagai **instrumen anggaran keamanan kriptoekonomi Hub**, bukan token gas monolitik.

**Alokasi genesis (13 Mar 2019, per Sosovalue):** Public Fundraise **44,15%** (160,28 juta) · Block Rewards
**39,50%** (143,41 juta) · Strategic **7,03%** · AIB **6,53%** (23,69 juta) · ICF **6,51%** (23,65 juta) ·
Seed **3,31%** (12 juta). *(INKONSISTENSI vs "Cosmos Plan" 2017 (75/10/10/5) — porsi block-reward belum dicetak
dihitung ke suplai berjalan. Evidence LOW.)*

**Emisi dinamis:** InflationMax **20%**, InflationMin **7%**, GoalBonded **66–67%**, InflationRateChange **100%/th** (block-by-block dari deviasi rasio staking).

**Intervensi governance *(causal chain)*:**
- **Prop 848 (Nov 2023):** InflationMax **20% → 10%** instan (**41,1% YES**, 31,9% NO, 6,6% VETO, 20,4% ABSTAIN;
  partisipasi 72,7%) → APR staking **19% → 13,4%** → memicu **fork AtomOne** oleh Jae Kwon.
- **Prop 868 (Jan 2024):** InflationMin → **0%** (StakeLab).
- **Prop 996 (H1 2025):** **98% emisi langsung ke staker** → APR riil stabil **16,34%**.

## 9. Airdrop & Incentive — "Staking-to-Earn" & Death Spiral
_ref: `docs/Patterns/Points.md`, `docs/Success/Airdrop.md`, `docs/Patterns/Liquidity.md`, `docs/MarketBehaviour/DeathSpiral.md`, `docs/Ontology/Community.md`_

**Mekanisme:** stake ATOM ke validator **non-CEX** → otomatis eligible **airdrop** dari chain SDK baru
(Osmosis, Celestia, Dymension). Ekstraksi via `osmosisd export [height]` → filter eligibility (mis. min **25
ATOM** snapshot 20 Okt 2023; min **23 TIA** snapshot 1 Des 2023). Celestia genesis airdrop menyalurkan
**$728.380.235** TIA. Delegator Hub **+60% H1 2024** (+500.000).

### Airdrop Death Spiral *(causal core — pola transferable)*
Tanpa vesting/lock airdrop → **mercenary capital**: kunci ATOM hanya untuk ekstrak airdrop, lalu jual token
airdrop → **TIA −91,9%, OSMO −79%, JUNO −82%** dari puncak; saat siklus melambat H2 2024, **90.000 delegator
unbond ATOM dalam sebulan (Nov 2024)** → depresi harga ATOM berkelanjutan. → §19 pola *Circular Airdrop Death
Spiral*; `examples/Pioneer/Celestia.md`.

## 10. Community, Narrative & Product Evolution
_ref: `docs/Ontology/Community.md`, `docs/Meta/Narratives.md`, `docs/Patterns/Narrative.md`, `docs/Project/Roadmap.md`_

**Komunitas:** **Game of Stakes** (testnet berinsentif pertama industri, menyaring operator node profesional).

**Peran narasi per fase:**
| Fase | Narasi | Peran |
|---|---|---|
| 2019–21 | Interoperabilitas klasik / "Internet of Blockchains" (IBC Classic) | **Pencipta** (memuncak ke ATH) |
| 2022–23 | Appchain & sovereign DeFi (**dYdX** migrasi dari StarkEx) | **Pemimpin** |
| 2023–24 | Modular & Data Availability (**Celestia**) | **Fondasi** |
| 2024 | Shared Security & Liquid Staking (Replicated Security ICS v1) | **Terlambat** (politik + LSM bermasalah) |
| 2025–26 | MultiVM & Ethereum integration (Circle MultiVM USDC, IBC v2 Eureka) | **Pengikut/pemulihan** |

**Product evolution:** **Replicated Security (ICS v1) → Partial Set Security (ICS 2.0, 2024)** opt-in (validator
kecil protes biaya server; **Neutron keluar ke kedaulatan penuh** awal 2025 → akhir era shared-security paksa).
**CosmWasm permissionless (Prop 1007, 2025)** → Hub jadi pusat dApp aktif. **Token Factory (Prop 1010)**.
**Akuisisi Skip Protocol oleh ICF (Des 2024)** → Skip:Go → **Interchain Labs → Cosmos Labs (2025**, Barry
Plunkett & Maghnus Mareneck) — konsolidasi rekayasa terpusat.

## 11. Competitive Landscape — Kedaulatan vs Value Accrual
_ref: `docs/Valuation/Competitors.md`, `docs/Valuation/ComparableProjects.md`, `docs/Meta/MarketCycles.md`_

- **vs Polkadot** — Polkadot: shared security kaku + lelang slot mahal. Cosmos: **kedaulatan gratis tanpa izin**.
  Cosmos **menang adopsi developer mutlak**, tapi tanpa shared-security wajib → **likuiditas terfragmentasi**.
  → `examples/CaseStudies/Polkadot.md` (mirror image: sama-sama "tech elegan, token struggle").
- **vs Avalanche** — Subnet keamanan independen + Warp; keunggulan likuiditas EVM. Cosmos unggul kustomisasi
  non-EVM, kalah penyerapan nilai moneter. → `examples/CaseStudies/Avalanche.md`.
- **vs Ethereum L2** — L2 mewarisi keamanan/likuiditas ETH; Cosmos lebih murah/berdaulat/final instan, tapi tanpa
  jangkar dolar stabil hingga 2026.

**Kelemahan terbesar:** **tiada "pajak keamanan" wajib** — BNB Chain & Celestia pakai software Cosmos **gratis**
tanpa menyetor nilai ke staker ATOM → paradoks: **teknologi sukses, token ATOM terdepresiasi**. → §18.

## 12. Token Lifecycle & Price Causality
_ref: `docs/MarketBehaviour/*`, `docs/Valuation/FairValue.md`, `docs/Valuation/Revenue.md`, `docs/Reasoning/Prediction.md`_

| Titik | Nilai | Kondisi |
|---|---|---|
| Pre-TGE | IOU | 2017–19 |
| Launch | ~$7,50 (listing Binance 22 Apr 2019) | 14 Mar 2019 mainnet |
| **ATL** | **$1,14** *(atau $1,16)* | 13 Mar 2020 (panik COVID) |
| **ATH** | **$44,73** *(atau $43,84)* | 19 Sep 2021 (bull L1 + IBC Classic) |
| Decline | $6,79 (−24%/30d) | akhir 2024 |
| | $2,20–2,40 (MC $1,1 mrd) | awal Jan 2026 |
| | $1,46–1,58 (**−70 s/d −72,5% YoY**); vol harian ~$21,5 juta | pertengahan Jul 2026 |

**Fair value:** **undervalued** dari adopsi teknologi, **overvalued** dari akrual nilai (ATOM bukan gas wajib;
**tanpa burn** signifikan — fee Hub harian ~**$4**, revenue Q3 2023 ~**$145.343**) → inflasi tanpa pengisapan
pasokan. Pemulihan bergantung pada **native DEX Stride** + **buyback dari Injective USDC**. → `docs/Valuation/FairValue.md`.

## 13. Business Intelligence
_ref: `docs/Ontology/Revenue.md`, `docs/Ontology/Metrics.md`, `docs/Valuation/TVL.md`, `docs/Ontology/Adoption.md`_

**Jaringan:** **87,16 juta tx** sejak inception; **180 validator**; staked **232,16 juta ATOM** (akhir 2024) →
**274,04 juta** (H1 2025, **60%** suplai); **1,28 juta** alamat delegator; IBC transfer bulanan **>$1 mrd**; IBC
MAU **2,1 juta**; volume stablecoin Noble pra-migrasi **$22 mrd**; **fee tx Hub $0,0125**.
**TVL:** Hub akhir 2025 **$240.445** (sangat kecil); Osmosis mid-2026 TVL $13,12 juta, volume kumulatif **$41,5
mrd**, bulanan $67,65 juta, DAU 18.200.
**ICF budget 2024 $26,4 juta** (IBC $7,5 juta; SDK $3,5 juta; Gaia $3,5 juta; CometBFT $3 juta; CosmWasm $2,5
juta; strategic reserve $7,2 juta; dll). Belanja tahunan ICF: 2022 **$54,1 juta**, 2023 **$40 juta**.

## 14. Security — Infiltrasi DPRK dalam LSM
_ref: `docs/Ontology/Security.md`, `docs/Patterns/Failure.md`, `docs/Ontology/Risks.md`_

**Rantai peristiwa (causal):** Ago 2021 Zaki Manian (via Iqlusion) merekrut dev eksternal (termasuk **Jun Kai,
Sarawut Sanit**) untuk **Liquid Staking Module (LSM)** → **Jul 2022** audit Oak Security temukan celah *slashing
evasion* (ditugaskan diperbaiki oleh tim yang sama) → **4 Des 2022** commit terakhir kontributor **terafiliasi
Korea Utara** → **Mar 2023** **FBI** peringatkan Zaki (dirahasiakan dari komunitas) → **Sep 2023** LSM deploy di
Gaia → **2 Okt 2024** Zaki mengakui publik → **15 Okt 2024** Jae Kwon terbitkan exposé GitHub.

*Pelajaran:* **kerentanan rantai pasok software terdesentralisasi** — audit tak boleh dipasrahkan ke kontributor
kode yang sama; wajib audit multi-tahap. Integritas LSM tersisa masih **open question** (§20). Evidence **HIGH**.

## 15. POV Success-Matrix (§15)
_ref: `docs/Success/*`, `docs/Reasoning/Explainability.md`, `docs/Reasoning/Confidence.md`_

| POV | Verdict | Alasan | Evidence |
|-----|---------|--------|----------|
| **Founder** (`Success/Founder.md`) | ⚠️ Campuran | CometBFT/SDK sukses teknis mutlak; tapi gagal kepemimpinan → polarisasi, resign massal, fork AtomOne | HIGH |
| **VC** (`Success/VC.md`) | ✅ Sukses | Paradigm/Bain/1confirmation untung besar dari ICO $0,098 → likuidasi puncak 2021 | HIGH |
| **Retail** (`Success/Community.md`) | ❌ Gagal | ATOM −95%+ dari ATH; yield/airdrop tak mengompensasi kerugian modal | HIGH |
| **Community** (`Success/Community.md`) | ❌ Gagal | Konflik politik toksik (Prop 82, Prop 848) menghambat konsensus & inovasi | HIGH |
| **Developer** (`Success/Developer.md`) | ✅ Sukses | Akses gratis ke framework modular terbaik; blockchain berdaulat tanpa hambatan | HIGH |
| **Institution** (`Success/Adoption.md`) | ❌ Gagal | Instabilitas kepemimpinan + sengketa hukum + insiden **DPRK/LSM** menurunkan investability | MEDIUM |
| **Validator** (`Success/Protocol.md`) | ✅ Sukses | Bisnis operasional profitabel (komisi jutaan delegator + block rewards); kendali politik | HIGH |
| **Builder (appchain)** (`Success/Ecosystem.md`) | ✅ Sukses | BNB/dYdX/Injective/Celestia luncur cepat pakai kode gratis, **tanpa bayar pajak ke Hub** | HIGH |

**Takeaway:** developer/validator/appchain-builder/VC **menang**; retail/community/institution **gagal**; founder
**campuran**. Pola definitif: **adopsi teknologi sukses ≠ nilai token** — value-accrual adalah titik gagal utama.

## 16. Historical Timeline
_ref: `docs/TokenLifecycle/*`_

- **2014** — Tendermint BFT (Jae Kwon). **6 Apr 2017** — ICO $16,8 juta (30 mnt). **13 Mar 2019** — genesis Gaia (~236 juta ATOM). **14 Mar 2019** — Series A $9 juta (Paradigm).
- **13 Mar 2020** — ATL $1,14 (COVID). **Ago 2021** — LSM dev mulai (Iqlusion). **19 Sep 2021** — ATH $44,73.
- **Jul 2022** — audit Oak (celah LSM). **Nov 2022** — veto **Prop 82 (ATOM 2.0)** (kekhawatiran treasury ala-FTX). **4 Des 2022** — commit terakhir dev DPRK.
- **Mar 2023** — FBI peringatkan Zaki. **Sep 2023** — LSM deploy. **25 Nov 2023** — **Prop 848** (inflasi max 10%) → fork AtomOne.
- **21 Jan 2024** — Sigma (CosmWasm). **27 Feb 2024** — GovGen (AtomOne). **2 Okt 2024** — Zaki akui DPRK. **15 Okt 2024** — exposé Jae Kwon. **10 Des 2024** — akuisisi Skip.
- **Q1 2025** — Prop 1007 (CosmWasm permissionless). **18 Mar 2026** — **Noble migrasi ke EVM L1** (krisis stablecoin). **7 Mei 2026** — Circle MultiVM USDC di Injective. **11 Mei 2026** — Injective USDC = standar kanonikal Hub (≥4 tahun).

## 17. Current Status & 18. Lessons Learned
_ref: `docs/TokenLifecycle/Maturity.md`, `docs/Patterns/Failure.md`, `docs/Patterns/Recovery.md`_

**Status (pertengahan 2026):** *Recovery & Centralized Consolidation* di bawah **Cosmos Labs** — akhir era
airdrop spekulatif, membangun pendapatan riil. Peringkat pasar **#70**. Fondasi teknis menguat: BlockSTM (v0.54,
5.000 TPS), IBC v2 Eureka (murah ke Ethereum), krisis stablecoin diatasi via **Injective USDC** (pasca-matinya Noble).

**Tiga pelajaran fundamental:**
1. **Kedaulatan tanpa penyerapan nilai = kegagalan ekonomi** — SDK dipakai seluruh industri, tapi ATOM tak wajib
   → adopsi tak berkorelasi harga. *Model modular masa depan wajib desain value-accrual sejak awal.*
2. **Bahaya tata kelola omnibus** — Prop 82 (ATOM 2.0) menumpuk terlalu banyak perubahan radikal dalam satu
   proposal → gagal konsensus sosial. *Pecah reformasi jadi proposal kecil terverifikasi.*
3. **Kerentanan rantai pasok software terdesentralisasi** — kasus DPRK/LSM; audit multi-tahap wajib, tak boleh
   ke kontributor kode yang sama.

## 19. Knowledge Extraction — Patterns & Lessons (§18–19)
_ref: `docs/Patterns/*`, `docs/Reasoning/*`, `docs/Schema/PatternSchema.md`_

1. **Adoption-without-Value-Accrual** *(crown pattern)* — *framework dasar diadopsi luas → token induk tak jadi
   gas/jaminan wajib → pertumbuhan adopsi tak menetes ke harga → token terdepresiasi meski teknologi menang.*
   → `docs/Valuation/FairValue.md`, `docs/Reasoning/Prediction.md`. **Rule kandidat R1 (§20).**
2. **Circular Airdrop Death Spiral** — *staking berhadiah airdrop → mercenary capital → distribusi genesis →
   jual airdrop → runtuh harga token ekosistem → unbonding massal token L1 → depresi L1 berkelanjutan.*
   → `docs/MarketBehaviour/DeathSpiral.md`, `docs/Patterns/Liquidity.md`.
3. **Monetary Governance Split** — *governance loloskan potong inflasi via margin tipis → murka pendiri model
   keamanan murni → hard fork → komunitas & likuiditas terpecah → kerugian nilai kolektif.* (Prop 848 → AtomOne)
   → `docs/Patterns/Failure.md`, `docs/Ontology/Governance.md`.
4. **Software Supply-Chain Infiltration** — kontributor open-source anonim (DPRK) pada modul kritis; audit oleh
   tim yang sama = titik buta. → `docs/Ontology/Security.md`, `docs/Ontology/Risks.md`.
5. **Omnibus Governance Failure** — proposal tunggal terlalu besar → kecurigaan niat tersembunyi → veto (Prop 82).
   → `docs/Ontology/Governance.md`.
6. **Free-Rider Framework** — teknologi open-source sukses tanpa mekanisme upeti → builder pihak ketiga bebas
   memakai tanpa menyetor nilai. → `docs/Innovation/CompetitiveMoat.md`.

### Entitas & relasi ontologi (kandidat Knowledge Graph)
_ref: `docs/Schema/KnowledgeGraph.md`, `docs/Schema/EntityRelationship.md`_
- `[Cosmos_Hub/Gaia] —secures→ [Consumer_Chains]` · `[Interchain_Foundation] —funds→ [Cosmos_Labs]`
- `[All_in_Bits] —opposes→ [Proposal_848]` · `[Jae_Kwon] —founded→ [AtomOne]`
- `[Noble] —migratedTo→ [EVM_Standalone_L1]` · `[Injective_USDC] —replaces→ [Noble_USDC]`
- `[Cosmos_Labs] —maintains→ [Cosmos_SDK]` · `[Cosmos_SDK] —usedFreelyBy→ [BNB_Chain, dYdX, Injective, Celestia]`

## 20. Transferable Intelligence (§20) — rule candidates untuk L0/L1 baru
_ref: `docs/Reasoning/AnalogEngine.md`, `docs/Reasoning/Weighting.md`, `docs/Reasoning/Confidence.md`_

- **R1 — L1 Gas Integration Rule:** apakah token gas asli **wajib** dipakai seluruh appchain? Jika appchain bisa
  jalan **tanpa** membayar upeti/gas dalam token induk → klasifikasikan **"Berisiko Tinggi Lemah Value Accrual"**.
- **R2 — Validator Subsidy Alignment:** apakah biaya server validator rantai samping **disubsidi penuh** oleh
  emisi/pendapatan rantai itu? Jika tidak, validator berhenti → keamanan bersama runtuh (kasus RS→PSS).
- **R3 — Founder Supply Lock:** alokasi tim harus **vesting linier ≥24 bulan** pasca-TGE; ketiadaan lock = red flag dumping.
- **Khusus-Cosmos:** (a) abaikan target bond 66% jika governance bisa memotong InflationMax secara politis
  (parameter minting fleksibel); (b) **kehadiran Jae Kwon** di dev aktif/oposisi = indikator **social volatility
  risk** (memicu berita negatif & split berkala).

## 21. Open Questions (§21)
_Research gap — belum tervalidasi._
1. Hasil akhir **AtomOne (ATONE)** (inflasi 20% + blokir voting LST) — menarik kembali loyalis keamanan murni,
   atau memperparah fragmentasi modal? (evidence: MEDIUM)
2. Apakah **Injective USDC** mengamankan retensi likuiditas berkelanjutan, atau ketergantungan rantai luar
   mengikis kedaulatan ekonomi Hub? (LOW)
3. Integritas kode **LSM** tersisa — adakah backdoor/kerentanan tersembunyi dev DPRK? (LOW)

## 22. Evidence Level — kesimpulan kunci (§22)
_ref: `docs/Reasoning/Confidence.md`, `docs/Research/Verification.md`_

| Kesimpulan | Evidence | Alasan |
|---|---|---|
| Kejatuhan nilai ATOM = fragmentasi likuiditas + gagal value accrual | **HIGH** | Blog resmi, Prop 82/848, TVL Hub $240.445, migrasi Noble |
| Infiltrasi DPRK dalam LSM (bawah Iqlusion) | **HIGH** | Pengakuan Zaki Manian, forensik AIB, peringatan FBI terdokumentasi |
| Prop 848 (inflasi 10%) memperlemah pertahanan 51% Hub | **LOW (INKONSISTENSI)** | Perdebatan matematis terbuka: kubu 20%-wajib vs kubu 58%-cukup-aman |

## 23. Related Framework Definitions
- **Ontology:** `docs/Ontology/Identity.md`, `Team.md`, `Funding.md`, `Tokenomics.md`, `Incentives.md`,
  `Governance.md`, `Security.md`, `Risks.md`, `Technology.md`, `Infrastructure.md`, `Ecosystem.md`, `Community.md`,
  `Revenue.md`, `Metrics.md`, `Adoption.md`, `Innovation.md`
- **Innovation:** `docs/Innovation/FirstMover.md`, `CategoryCreator.md`, `CompetitiveMoat.md`
- **Patterns:** `docs/Patterns/Failure.md`, `Liquidity.md`, `Narrative.md`, `Distribution.md`; `docs/MarketBehaviour/DeathSpiral.md`, `UnlockImpact.md`
- **Valuation:** `docs/Valuation/FairValue.md`, `Revenue.md`, `Competitors.md`, `ComparableProjects.md`, `TVL.md` · **Market/Meta:** `docs/Meta/Narratives.md`, `MarketCycles.md`
- **Reasoning:** `docs/Reasoning/Prediction.md`, `AnalogEngine.md`, `Confidence.md`, `Weighting.md`
- **Success:** `docs/Success/*` · **Schema:** `docs/Schema/KnowledgeGraph.md`, `EntityRelationship.md`, `PatternSchema.md`
- **Cross-project analogs:** `examples/CaseStudies/Polkadot.md` (sovereignty vs shared-security mirror), `Avalanche.md`
  (appchain/Subnet + vs-Cosmos), `BNBChain.md` (Binance Chain/Greenfield di atas Tendermint/Cosmos SDK);
  `examples/Pioneer/Celestia.md` (SDK-built DA; TIA airdrop + death spiral), `examples/Pioneer/dYdX.md` (migrasi StarkEx→Cosmos appchain)

## 24. Sources
_Deep Research provenance (Gemini). Laporan sumber mengutip **87 referensi**; sumber primer/kunci di bawah._

- Cosmos SDK — GitHub (cosmos/cosmos-sdk) — https://github.com/cosmos/cosmos-sdk
- cosmos/PLAN.md (Cosmos Plan) — GitHub — https://github.com/cosmos/cosmos/blob/master/PLAN.md
- Exploring the Cosmos: Inside the Cosmos Ecosystem — Galaxy — https://www.galaxy.com/insights/research/exploring-the-cosmos
- The Tokenomics of Cosmos Hub ATOM — Findas — https://www.findas.org/tokenomics-review/coins/the-tokenomics-of-cosmos-hub-atom/r/N7AoxCpWnWCTNupE8EoXcG
- Sosovalue: Cosmos Hub Token Distribution — https://m.sosovalue.com/coins/cosmos-hub
- Cosmos co-founder splits ATOM after years of infighting — Blockworks — https://blockworks.com/news/cosmos-fork-jae-kwon
- Infiltrating Cosmos (LSM security) — Rekt News — https://rekt.news/infiltrating-cosmos
- Cosmos cofounder blames Iqlusion for North Korea-linked security risks — The Block — https://www.theblock.co/post/321351/cosmos-liquid-staking-north-korea
- AllInBits announcement 2024_10_15 (LSM/NK) — GitHub — https://github.com/allinbits/announcements/blob/main/2024_10_15_lsmnk.md
- Why All in Bits Recommends Strong No-with-Veto on Prop 82 — Cosmos Hub Forum — https://forum.cosmos.network/t/why-all-in-bits-recommends-a-strong-no-with-veto-on-prop-82/8198
- Cosmos Proposal 848 → new AtomOne Network — Binance Square — https://www.binance.com/en/square/post/612958289138
- Who killed the cross-chain king Cosmos? (Airdrop Death Spiral) — ChainCatcher — https://www.chaincatcher.com/en/article/2195964
- Injective USDC as Canonical Stablecoin for Cosmos & dYdX — Injective — https://injective.com/blog/inj-usdc-coming-soon-cosmos-dydx
- Interchain Labs becomes Cosmos Labs — cosmos.network — https://cosmos.network/blog/interchain-labs-becomes-cosmos-labs
- The Interchain Foundation puts aside $26.4M — Blockworks — https://blockworks.com/news/cosmos-ecosystem-receives-funding
- Tendermint Inc Announces Series A Round (Paradigm) — Medium — https://medium.com/tendermint/tendermint-inc-announces-series-a-round-9c062d1bd7de
- The Cosmos Stack Roadmap for 2026 — cosmos.network — https://cosmos.network/blog/the-cosmos-stack-roadmap-2026

_(Full 87-source bibliography retained in the original Deep Research report + archived at
`doc_backup/deep/Cosmos_2026-07_gemini.md`.)_
