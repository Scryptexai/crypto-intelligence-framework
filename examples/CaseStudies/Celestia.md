# Celestia — Deep Case Study

**CIF Dataset — Deep Dossier · Tier: Deep (anchor project)**
**Source:** Deep Research (Gemini) — *"Laporan Intelijen Celestia: Dekonstruksi Komprehensif Arsitektur Modular,
Dinamika Tokenomik, dan Evolusi Pasar (2019-2026)"*.
**Pipeline position:** Applications layer — anchor artifact structured against the full `docs/` ontology.
The **category-creating First Mover of sovereign modular Data Availability (alt-DA)** — the chain that forced
Ethereum to ship EIP-4844 blobs. Also the dataset's clearest **"Value-Revenue Gap"** and **vesting-loophole
capital-extraction** case: TVL of narratives, but ~$60–89/day fees; VC (Polychain) drained ~$179–242M in *liquid
staking rewards from locked tokens* → TIA −97%. **Supersedes** the Batch-01 Summary `examples/CaseStudies/Celestia.md`.
**Raw source archived:** `doc_backup/deep/Celestia_2026-07_gemini.docx` (+ `.md` text extraction).
**Input note:** authored in the CIF no-table contract; extracted via `tools/extract.py` (0 tables, 0 chips,
23 sections); fidelity checked with `tools/reconcile.py`.

> Knowledge artifact (real curated data), not a documentation container. This is a **deep dossier**: it
> preserves *causality* (why events happened), which is the raw material for prediction. Conforms to
> `templates/CaseStudyTemplate.md`.

---

## 1. Identity
_ref: `docs/Ontology/Identity.md`_

- **Project:** Celestia (dahulu **LazyLedger**; token: **TIA**).
- **Category:** Modular blockchain — **Data Availability (DA) layer** berdaulat (bukan eksekusi/settlement).
- **Era:** 2019 (LazyLedger paper) – sekarang. **Rebrand:** 15 Jun 2021. **Mainnet Beta:** 31 Okt 2023.
  **Founder/CEO:** **Mustafa Al-Bassam** (PhD blockchain-scaling UCL, ex-Chainspace→Facebook).
- **Innovation archetype:** **First Mover / Category Creator** — alt-DA berdaulat pertama; menetapkan modularitas
  sebagai standar industri → memaksa Ethereum rilis **EIP-4844**.
- **Skala:** **~50% pangsa pasar alt-DA**; **100+ rollup produksi**; 160 GB data diproses; tapi **REV lemah**
  (~$60–89/hari fee) — inti tesis *Value-Revenue Gap* (§15).

## 2. Classification
_ref: `docs/Ontology/Classification.md`, `docs/Taxonomy/Sectors.md`, `docs/Taxonomy/Technologies.md`_

Modular DA layer · **memisahkan konsensus + DA dari eksekusi & settlement** · konsensus **CometBFT/Tendermint PoS
(Cosmos SDK)** · primitif: **Data Availability Sampling (DAS)** via **2D Reed-Solomon erasure coding**, **Namespaced
Merkle Trees (NMT)**, **light node tanpa asumsi mayoritas-jujur** · produk: **Sovereign SDK, Blobstream (ex-QGB),
Lazybridging (ZK), Fibre Blockspace (1 Tb/s ZODA)** · token **TIA** (inflationary, gas + staking + governance).

## 3. Pre-Conditions — DA Bottleneck Rollup (2019–2023)
_Konteks: mengapa Celestia harus ada._
_ref: `docs/Meta/Narratives.md`, `docs/Ontology/Revenue.md`_

Blockchain **monolitik** (Bitcoin/Ethereum) memaksa tiap node menjalankan **4 fungsi** (eksekusi + konsensus + DA +
settlement) → **Trilema**: naikkan throughput → blok membengkak → **state bloat** → hanya operator hardware-tinggi
bertahan → desentralisasi runtuh. **Rollup L2** memindah eksekusi off-chain tapi membentur **DA bottleneck**:
posting calldata ke Ethereum L1 menyerap **>90% biaya operasional rollup** (pra-EIP-4844). Celestia memutus
ketergantungan ini: rantai berdaulat yang **hanya mengurutkan data** (lazy execution) → ruang blok murah-melimpah →
memicu ledakan **RaaS** (Conduit, AltLayer, Caldera). → `examples/CaseStudies/Ethereum.md` §6 (rollup-centric roadmap).

## 4. Origin & Team
_ref: `docs/Ontology/Team.md`, `docs/Project/Philosophy.md`_

Akar: **Mustafa Al-Bassam** merumuskan **Data Availability Sampling (DAS)** saat riset pascasarjana (2018), lalu
publikasi paper **"LazyLedger" (2019)** — rantai konsensus minimalis yang **tak mengeksekusi transaksi**, hanya
menjamin data tersedia untuk diunduh/diverifikasi. Antitesis radikal "komputer global monolitik".
- **Mustafa Al-Bassam** (CEO) — PhD UCL; co-founder **Chainspace** (diakuisisi Facebook 2019).
- **John Adler** (CRO) — ex-ConsenSys; **perancang spesifikasi Optimistic Rollup pertama** di Ethereum.
- **Ismail Khoffi** (CTO) — ex-senior dev **Tendermint / Interchain Foundation**.
- **Nick White** (COO) — co-founder **Harmony Protocol**.
- **Advisor:** **Zaki Manian, Ethan Buchman** (pelopor Cosmos — panduan SDK/IBC).

**Entitas:** UK (**CIN 12391157**, 7 Jan 2020, 28 karyawan/Mar 2024) + **Strange Loop Labs AG** (Vaduz, Liechtenstein —
yayasan/tokenomik). Rebrand **LazyLedger → Celestia** 15 Jun 2021.

## 5. Innovation Analysis — DAS, NMT, Trustless Light Nodes
_ref: `docs/Ontology/Innovation.md`, `docs/Innovation/FirstMover.md`, `docs/Innovation/CategoryCreator.md`, `docs/Ontology/Technology.md`_

1. **Data Availability Sampling (DAS)** — **2D Reed-Solomon erasure coding**: data blok jadi matriks + redundansi →
   produsen yang sembunyikan **1 byte** harus sembunyikan **>50% blok** (terdeteksi). **Light node** unduh sampel acak
   beberapa KB → buktikan **>99,99%** seluruh data terbit — **tanpa unduh blok penuh**. *Mematahkan batas linier skalabilitas.*
2. **Namespaced Merkle Trees (NMT)** — daun Merkle dikelompokkan per **Namespace ID** (satu per rollup) → node rollup
   unduh **hanya data relevan-nya**, abaikan puluhan rollup lain di blok yang sama → hemat bandwidth masif.
3. **Light node tanpa asumsi mayoritas-jujur** — DAS memverifikasi ketersediaan **independen**; jika validator sembunyikan
   data, light node deteksi langsung (vs blockchain tradisional yang percaya 2/3 validator jujur).

*Dampak/moat:* **First Mover murni alt-DA berdaulat** — melembagakan modularitas sebagai standar → **memaksa Ethereum
rilis EIP-4844**. → `docs/Innovation/CategoryCreator.md`.

## 6. Technology Evolution — Mainnet Beta → Matcha → Fibre
_ref: `docs/Ontology/Technology.md`, `docs/TokenLifecycle/*`, `docs/Ontology/Infrastructure.md`_

- **Mamaki testnet (Mei 2022)** — uji publik blob + sampling light node ritel global.
- **Mainnet Beta (31 Okt 2023)** — blok **2–8 MB** (aman, Tendermint).
- **Lemongrass (v2, Sep 2024, CIP-17/10)** — **in-protocol signaling**: upgrade otomatis 1 minggu setelah **5/6 voting
  validator** setuju on-chain (hentikan koordinasi manual).
- **Ginger (v3, Des 2024, CIP-25)** — **"The Doubling"** waktu blok **12→6 detik**; CIP-21 authored blobs; CIP-27 (600
  PayForBlobs/blok); CIP-28 (tx maks 2 MiB).
- **mamo-1 testnet (Apr 2025)** — stress-test **128 MB / 21,33 MB/s** (21 validator Amsterdam/Paris/Warsaw); protokol
  **"Vacuum!"** (Pull-Based Broadcast Tree).
- **Lotus (v4, Jul 2025, blok 6.680.339)** — CIP-29 potong emisi; CIP-30 nonaktifkan auto-claim; **CIP-31 kunci staking
  reward token vesting** *(fix loophole, §15)*.
- **Matcha (v6, Nov 2025, blok 8.662.012, CIP-38)** — blok fisik **128 MB**, square maks 512, tx 8 MiB; unbonding **14
  hari 1 jam** (CIP-37); trusting period light node **7 hari** (CIP-36); inflasi **→2,5%**.
- **Fibre Blockspace (Jan 2026)** — protokol DA paralel **1 Tb/s** berbasis **ZODA encoding**; blob 256 KB–128 MB langsung
  ke validator; **881× lebih cepat dari komitmen KZG**.

## 7. Funding Intelligence
_ref: `docs/Ontology/Funding.md`, `docs/Ontology/Tokenomics.md`, `docs/TokenLifecycle/TGE.md`_

| Putaran | Tanggal | Dana | Harga/Valuasi | Investor kunci |
|---|---|---|---|---|
| **Seed** | Mar 2021 | **$1,5 juta** | $0,00943 · val $9,43 juta · 159 juta TIA (15,9%) | **YZi Labs (Binance Labs), Interchain** · Maven 11, KR1 |
| **Series A & B** | 19 Okt 2022 | **$55 juta** | $0,30 · val **$300 juta** · 197 juta TIA (19,7%) | **Bain Capital Crypto, Polychain** · Coinbase/OKX Ventures, Galaxy |
| **Secondary** | Agu 2023 | (tak diungkap) | — | — |
| **OTC Strategis** | 23 Sep 2024 | **$100 juta** | val **$3,5 miliar** | **Bain Capital Crypto** · 1kx, Placeholder |
| **Polychain buyback** | 24 Jul 2025 | **$62,5 juta** | ~$1,44 · 43,45 juta TIA | **Celestia Foundation** (redistribusi rolling ke investor baru) |

*(INKONSISTENSI: total kumulatif Tracxn $204 juta vs Clay/RootData $156,5 juta — selisih ~$47,5 juta = OTC privat.
Chainbroker pisah Series A $15 juta @$0,0955 / Series B $40 juta @$1,00. Evidence LOW.)*

## 8. Tokenomics — Inflasi Tanpa Batas + Reformasi Lotus/Matcha
_ref: `docs/Ontology/Tokenomics.md`, `docs/Ontology/Incentives.md`, `docs/MarketBehaviour/UnlockImpact.md`, `docs/Patterns/Flywheel.md`_

- **Genesis supply:** **1 miliar TIA**; **max supply tak terbatas** (inflationary).
- **Alokasi genesis:** Public **20%** (Genesis Drop 7,41% + Future 12,59%) · **R&D/Ecosystem 26,79%** · **Series A&B
  19,67%** · **Seed 15,9%** · **Core Contributors 17,64%**. Public 100% cair TGE; sisanya cliff 1-th (30 Okt 2024) + linear.
- **Jadwal inflasi:** mula **8%/th**, turun 10%/th → floor **1,5%**. **Lotus (Jul 2025, CIP-29):** potong emisi **−33%**
  (~7,2%→~5%). **Matcha (Nov 2025, CIP-41):** potong radikal ke **~2,5%** — respons kritik dilusi.

### Vesting-loophole fix (Lotus CIP-31) *(causal core — tokenomics)*
Pra-Lotus, token **terkunci (vesting)** tetap bisa di-stake dan **staking reward-nya likuid penuh** → **Polychain
melikuidasi ~$179 juta** reward dari token terkunci (synthetic exit). CIP-31 **mengunci reward proporsional** dengan
% token pokok yang masih terkunci (50% pokok terkunci → 50% reward terkunci). *Aturan baku yang wajib sejak genesis (§16).*

## 9. Airdrop, Community & Competitive Landscape
_ref: `docs/Patterns/Points.md`, `docs/Success/Airdrop.md`, `docs/Ontology/Community.md`, `docs/Valuation/Competitors.md`_

**Cold-start developer-first:** **Modular Fellows** (didik insinyur rollup) + **Modular Summits** (Amsterdam 2022, Paris
2023) → thought-leadership modularitas. **Light node** jalan di latar laptop (DAS) → ribuan operator amatir.

**Genesis Drop:** **60 juta TIA (6%)** ke 5 kelompok — Research/Public Goods (6 juta, kontributor GitHub Bitcoin/ETH/Cosmos),
Early Modular Ecosystem (8,35 juta), GitHub Super-Contributors (5,65 juta), **Early Adopters Ethereum Rollups (20 juta**,
50% teratas 10 rollup top L2Beat termasuk dYdX/Arbitrum/OP), **Cosmos/Osmosis Stakers + IBC Relayers (20 juta)**. **Retail
murni hanya ~2%** → kekecewaan (dinilai untungkan insider/dev). → `examples/CaseStudies/dYdX.md`, `Cosmos.md`.

### Airdrop Staking Meta *(causal — reflexivity)*
Rollup baru (**Dymension, Saga, AltLayer**) airdrop eksklusif ke staker TIA → FOMO → **rasio staking 72%** → harga ATH
via kelangkaan pasokan → saat pasar rollup koreksi 2025, **unbonding massal** hancurkan harga (§13).

**Kompetitif (DA layer 2026):**
- **Ethereum Blob (EIP-4844)** — **0,67 MB/s**, ~$3,83/MB, keamanan L1 tertinggi, finality 12–15 mnt, full replication (tanpa DAS).
- **EigenDA (EigenLayer)** — **15 MB/s**, restaked ETH ~$1,6 mrd, **DAC off-chain (tanpa DAS publik)**, risiko sentralisasi komite. → `examples/CaseStudies/EigenLayer.md`.
- **Avail (Polygon spinout)** — DAS + **KZG validity proof** → finality **~40 detik** (vs Celestia ~10 mnt challenge window), NPoS ~$100 juta; ekosistem lebih muda.
- **Celestia menang ~50% pangsa alt-DA** (First Mover + RaaS agresif); **kalah finality** (challenge window ~10 mnt vs Avail KZG ~40 dtk). *(Avail/EigenDA/Dymension/Saga/AltLayer = kandidat gap dataset.)*

## 10. Narrative & Product Evolution
_ref: `docs/Meta/Narratives.md`, `docs/Patterns/Narrative.md`, `docs/Project/Roadmap.md`, `docs/Ontology/Adoption.md`_

**Narasi per fase:** **Modular vs Monolithic** (2021–23, "ruang blok murah-melimpah") → **Airdrop Engine** (TGE–pertengahan
2024, TIA = "indeks modal ekosistem modular") → **Modular Reset / Value-Revenue Gap** (2024–25, kritik REV ~$60/hari vs
valuasi miliaran) → **Vision 2.0 "Every Market Onchain"** (2026, terabit-scale untuk pasar finansial on-chain + pembayaran mikro agen AI).

**Product:** **Sovereign SDK** (rollup berdaulat tanpa settlement Ethereum) → **Blobstream** (ex-QGB, jembatan bukti DA ke
EVM; rollup OP Stack/Arbitrum Orbit simpan data di Celestia) → **Lazybridging** (2025, ZK bridge bawaan, atasi fragmentasi
likuiditas) → **Fibre** (2026, express lane latensi milidetik) → **akuisisi Sovereign Labs (Jul 2026**, tim ZK). → `examples/Pioneer/Optimism.md` (OP Stack).

## 11. Token Lifecycle & Price Causality
_ref: `docs/MarketBehaviour/*`, `docs/Valuation/FairValue.md`, `docs/Reasoning/Prediction.md`_

| Titik | Nilai | Kondisi |
|---|---|---|
| TGE debut | ~$2,00 (float tipis 14,1–15,7%) | 31 Okt 2023 |
| **ATH** | **$20,85** *(alt $20,91)* | 10 Feb 2024 (eforia airdrop staking meta) |
| Unlock cliff #1 | 17,68% pasokan (**$1,1 miliar**) | 30 Okt 2024 (tekanan jual konstan) |
| Kapitulasi | <$1,00 | akhir 2025 (dump Polychain rewards ~$242 juta) |
| **ATL** | **$0,2792** *(alt $0,2796, 5 Apr)* (−97%) | 6 Jun 2026 |

**Fair value (pertengahan 2026):** **undervalued** di $0,35–0,45 — overhang jual investor **selesai** (buyback $62,5 juta +
rolling unlock tuntas 14 Nov 2025), inflasi dipangkas ke 2,5% (Matcha), dominasi ~50% DA (160 GB diproses). MC **~$285–373
juta** / FDV **$370–468 juta** → *potensi pemulihan asimetris* jika adopsi Fibre bervolume tinggi terwujud. → `docs/Valuation/FairValue.md`.
*(INKONSISTENSI ATL: RootData $0,2796/5 Apr vs CoinGecko $0,2792/6 Jun — beda price feed. Evidence LOW.)*

## 12. Business Intelligence — Value-Revenue Gap
_ref: `docs/Ontology/Revenue.md`, `docs/Valuation/Revenue.md`, `docs/Ontology/Metrics.md`, `docs/Valuation/TVL.md`, `docs/Success/Adoption.md`_

**Krisis akrual nilai (crown weakness):** biaya DA **termurah industri (~$0,07/MB)** — tapi justru **gagal menangkap nilai**:
- **Daily fees (Jul 2026):** **$89,26** · **daily revenue $1,79** · REV Q2 2025 **$79.503**. Blob fees: ~$225/hari (akhir
  2024) → ~$60/hari (H1 2025, efisiensi kompresi) → naik **10×** menuju pertengahan 2026 (adopsi rollup).
- **Adopsi:** **100+ rollup produksi** (35+ komersial); **160 GB** diproses total; **2,5 GB/hari** rata-rata.
- **Staking:** rasio **64–65%**; APY puncak **14,67%** (Mei 2026); validator maks **100**, komisi cap 25% (Lotus) → efektif 20% (Matcha).

*Tesis inti:* ruang blok terlalu murah + inflasi → **komoditas murah tanpa value capture** kecuali volume masif atau burn agresif (§16 rule). → `docs/Valuation/Revenue.md`.

## 13. POV Success-Matrix (§15)
_ref: `docs/Success/*`, `docs/Reasoning/Explainability.md`, `docs/Reasoning/Confidence.md`_

| POV | Verdict | Alasan | Evidence |
|-----|---------|--------|----------|
| **Founder** (`Success/Founder.md`) | ✅ Sukses | Buktikan hipotesis modular global; standar pasar baru; mainnet stabil proses gigabyte | HIGH |
| **VC** (`Success/VC.md`) | ✅ Sukses | Polychain realisasi **~$242 juta** dari ekstraksi staking-reward likuid atas modal awal ~$20 juta | HIGH |
| **Retail** (`Success/Community.md`) | ⚠️ Campuran | Penerima airdrop untung 4-digit bebas risiko; pembeli sekunder rugi **−97%** di puncak gelembung | HIGH |
| **Community** (`Success/Community.md`) | ⚠️ Campuran | Staker nikmati airdrop beruntun; tapi struktur insentif hancur saat pokok terdepresiasi | HIGH |
| **Developer** (`Success/Developer.md`) | ✅ Sukses | Sovereign SDK bebas aturan settlement; DA termurah industri (~$0,07/MB) | HIGH |
| **Institution** (`Success/Adoption.md`) | ⚠️ Campuran | Masuk OTC Sep 2024 terdiskon; tapi akumulasi terhambat **fee capture lemah** | MEDIUM |
| **Validator** (`Success/Protocol.md`) | ✅ Sukses | Stabil karena delegasi >60%; margin longgar (komisi 20% Matcha) | HIGH |
| **Builder** (`Success/Ecosystem.md`) | ✅ Sukses | Terintegrasi di OP Stack/Arbitrum Orbit/Polygon CDK → fondasi **sangat lengket** | HIGH |

**Takeaway:** menang di Founder/Developer/Validator/Builder/VC; **campuran** Retail/Community/Institution — semuanya berakar
pada **satu cacat: Value-Revenue Gap** (teknologi menang, moneter lemah). Kontras dengan ether.fi (menang luas via fee riil).

## 14. Historical Timeline
_ref: `docs/TokenLifecycle/*`_

- **2018** — Al-Bassam formulasi DAS. **2019** — paper **LazyLedger**. **7 Jan 2020** — entitas UK (CIN 12391157). **4 Mar 2021** — Seed $1,5 juta (Interchain/Binance Labs). **15 Jun 2021** — rebrand **Celestia**.
- **25 Mei 2022** — Mamaki testnet. **20 Okt 2022** — Series A&B $55 juta (Bain/Polychain). **Agu 2023** — secondary round. **26 Sep 2023** — Genesis Drop diumumkan. **31 Okt 2023** — **Mainnet Beta + TGE** (Binance/Coinbase listing).
- **10 Feb 2024** — **ATH $20,85**. **18 Sep 2024** — Lemongrass v2 mainnet. **23 Sep 2024** — OTC $100 juta (val $3,5 mrd). **30 Okt 2024** — **unlock cliff #1** ($1,1 miliar). **12 Des 2024** — Ginger v3 (blok 6 detik).
- **Apr 2025** — mamo-1 (128 MB). **23 Jun 2025** — co-founder respons FUD (kas >$100 juta). **26 Jun 2025** — data on-chain: Polychain profit $80 juta staking. **24 Jul 2025** — **buyback Polychain $62,5 juta**. **28 Jul 2025** — **Lotus v4** (inflasi ~5%, CIP-31 lock rewards). **24 Nov 2025** — **Matcha v6** (128 MB, inflasi ~2,5%).
- **13 Jan 2026** — **Fibre Blockspace** (1 Tb/s ZODA). **22 Jan 2026** — Celestia Private Blockspace. **6 Jun 2026** — **ATL $0,2792**. **15 Jul 2026** — akuisisi **Sovereign Labs** (tim ZK).

## 15. Value-Revenue Gap, Vesting Extraction, Current Status, Lessons
_ref: `docs/Ontology/Revenue.md`, `docs/Patterns/Failure.md`, `docs/Patterns/Recovery.md`, `docs/TokenLifecycle/Maturity.md`_

### Value-Revenue Gap *(causal core — value accrual)*
Sukses teknis (**DA 99% lebih murah dari L1**) **justru** melahirkan krisis moneter: ruang blok murah-melimpah → REV
~$60–89/hari → **jurang lebar** antara valuasi spekulatif miliaran vs pendapatan riil. *Analog kausal dengan Ethereum
pasca-Dencun (sukses skalabilitas menggerus value-accrual) — tapi lebih ekstrem karena Celestia lahir "terlalu murah".*

### Vesting Loophole Capital Extraction *(causal core — tokenomics)*
Token VC terkunci tetap di-stake → **reward likuid penuh** → **Polychain ekstraksi ~$179–242 juta** synthetic exit →
tekanan jual insider konstan → ritel rugi + kemarahan → **buyback darurat $62,5 juta** + **Lotus CIP-31** kunci-paksa reward.

**Status (pertengahan 2026):** *quiet structural recovery* — harga $0,31–0,45 stabil, spekulan pergi, jaringan dihargai
utilitas murni; teknologi puncak (Matcha 128 MB stabil, Fibre, Lazybridging); moneter jauh lebih sehat (inflasi 2,5%,
overhang jual tuntas). Transisi ke L1 pasar-on-chain performa-tinggi (Vision 2.0).

**Pelajaran:** (1) **Modularitas menang teknis, menantang finansial** — ruang blok terlalu murah = gagal akrual nilai
tanpa burn agresif/volume masif; (2) **tutup celah vesting-reward sejak genesis** (CIP-31 = aturan baku); (3) **bootstrap
developer-first > airdrop ritel** (retensi tinggi); (4) **keamanan DAS bergantung light node** (wajib SDK ringan di wallet).

## 16. Knowledge Extraction — Patterns & Lessons (§18–19)
_ref: `docs/Patterns/*`, `docs/Reasoning/*`, `docs/Schema/PatternSchema.md`_

1. **Cost-Revenue Divergence Trap** *(crown value-accrual pattern)* — *infrastruktur pangkas biaya 99% → asumsi harga token
   naik SALAH → jika ruang blok terlalu murah, butuh volume ratusan juta tx/hari agar burn imbangi inflasi → tanpa value
   capture kuat = komoditas murah, kinerja token buruk.* → `docs/Valuation/FairValue.md`, `docs/Reasoning/Prediction.md`; analog `examples/CaseStudies/Ethereum.md` §10 (Dencun).
2. **Vesting Loophole Capital Extraction** *(crown tokenomics pattern)* — *token VC cliff → boleh di-stake → reward likuid
   harian → VC jual sistematis synthetic-exit → tekanan jual insider → ritel rugi → yayasan buyback + upgrade lock-paksa.* → `docs/Patterns/Failure.md`, `docs/Patterns/Recovery.md`.
3. **Airdrop Reflexivity Meta Loop** — *mainnet float-rendah → rollup baru airdrop ke staker → FOMO stake → rasio staking
   >70% → harga ATH via kelangkaan → hype dingin → unbonding massal → harga hancur.* → `docs/Patterns/Points.md`, `docs/Patterns/Narrative.md`.
4. **Category-Creator First Mover** — *definisikan kategori (alt-DA modular) → paksa incumbent adaptasi (Ethereum EIP-4844)
   → menang pangsa via RaaS meski ada pesaing teknis lebih baik (Avail KZG finality).* → `docs/Innovation/CategoryCreator.md`, `docs/Innovation/FirstMover.md`.
5. **Developer-First Cold Start** — *Modular Fellows + Summits + light-node murah → retensi dev tinggi > airdrop ritel.* → `docs/Success/Airdrop.md`, `docs/Ontology/Community.md`.

### Entitas & relasi ontologi (kandidat Knowledge Graph)
_ref: `docs/Schema/KnowledgeGraph.md`, `docs/Schema/EntityRelationship.md`_
- `[Mustafa_Al-Bassam] —co-founded→ [Celestia_Labs]` · `[Celestia] —pioneered→ [Data_Availability_Sampling]` · `[Celestia] —forced→ [Ethereum_EIP-4844]`
- `[Celestia_Foundation] —repurchased→ [Polychain_TIA_Stake]` · `[Lotus_Upgrade] —implemented→ [CIP-31_Vesting_Lock]` · `[Matcha_Upgrade] —cut→ [Inflation_2.5%]`
- `[Fibre_Blockspace] —utilizes→ [ZODA_Encoding]` · `[Celestia] —competes_with→ [EigenDA]/[Avail]/[Ethereum_Blob]` · `[Celestia_Labs] —acquired→ [Sovereign_Labs]`

## 17. Transferable Intelligence (§20) — rule candidates untuk infrastruktur baru
_ref: `docs/Reasoning/AnalogEngine.md`, `docs/Reasoning/Weighting.md`, `docs/Reasoning/Confidence.md`_

- **R1 — Staking Reward Lockstep Rule:** jika kontrak izinkan **token terkunci menghasilkan reward likuid** → beri
  **risiko tekanan-jual insider TINGGI** sejak peluncuran. Aturan baku: reward token terkunci wajib ikut jadwal vesting pokoknya. *(Pelajaran Polychain.)*
- **R2 — Cost-Revenue Divergence Trap:** jangan simpulkan pangkas biaya 99% → harga token naik. Hitung **elastisitas
  permintaan ruang blok**: terlalu murah → butuh volume masif agar burn > inflasi. Utilitas tinggi tanpa value-capture = komoditas murah. *(Celestia = kasus utama.)*
- **R3 — Client-side Light Node Feasibility (khusus DAS):** keamanan DAS valid hanya jika light node jalan di **perangkat
  pengguna akhir** (SDK ringan di wallet/browser); jika verifikasi bergantung server cloud pihak ketiga → **penalti keyakinan** atas klaim desentralisasi.

## 18. Open Questions (§21)
_Research gap — belum tervalidasi._
1. Apakah **Vision 2.0 / Fibre 1 Tb/s** benar menarik industri non-kripto (iklan real-time, pembayaran mikro agen AI), atau berakhir jadi ruang blok kosong tak terutilisasi komersial? (evidence: MEDIUM)
2. Dinamika jangka panjang **Celestia vs EigenDA** pasca EigenDA aktifkan slashing L1 — apakah restaking ETH lebih stabil dari DPoS independen Celestia? (MEDIUM)
3. Cukupkah pemangkasan inflasi Lotus/Matcha (terminal 1,5%) mengimbangi emisi, atau Celestia butuh **burn paksa** di tingkat blob agar deflasioner? (MEDIUM)

## 19. Evidence Level — kesimpulan kunci (§22)
_ref: `docs/Reasoning/Confidence.md`, `docs/Research/Verification.md`_

| Kesimpulan | Evidence | Alasan |
|---|---|---|
| Celah ekstraksi staking-reward Polychain = pemicu utama jatuhnya TIA 2024–25 | **HIGH** | On-chain: penjualan reward ~$179–242 juta + Lotus CIP-31 khusus tutup celah + buyback $62,5 juta |
| Matcha naikkan kapasitas blok 128 MB tanpa korban stabilitas/desentralisasi | **HIGH** | CIP-38 + binary v6 + mamo-1 128 MB + rilis stabil Mainnet Beta sejak Nov 2025 |
| Fibre pertahankan 1 Tb/s stabil di kondisi dunia nyata | **MEDIUM** | 1 Tb/s tercapai di GCP terkontrol (498 server, 34–45 Gbps); validator riil bervariasi latensi antar-negara |
| Total pendanaan / alokasi tokenomics | **LOW** | Inkonsistensi Tracxn $204 juta vs $156,5 juta; Chainbroker pisah Series A/B beda harga |

## 20. Related Framework Definitions
- **Ontology:** `docs/Ontology/Identity.md`, `Team.md`, `Funding.md`, `Tokenomics.md`, `Incentives.md`,
  `Governance.md`, `Security.md`, `Risks.md`, `Technology.md`, `Infrastructure.md`, `Ecosystem.md`, `Community.md`, `Revenue.md`, `Metrics.md`, `Adoption.md`, `Innovation.md`
- **Innovation:** `docs/Innovation/FirstMover.md`, `CategoryCreator.md`, `CompetitiveMoat.md`, `ProductMarketFit.md`
- **Patterns:** `docs/Patterns/Failure.md`, `Recovery.md`, `Points.md`, `Narrative.md`, `Distribution.md`, `Flywheel.md`
- **Valuation/Market:** `docs/Valuation/FairValue.md`, `Revenue.md`, `Competitors.md`, `TVL.md`; `docs/MarketBehaviour/UnlockImpact.md`; `docs/Meta/Narratives.md`, `MarketCycles.md`
- **Reasoning:** `docs/Reasoning/Prediction.md`, `AnalogEngine.md`, `Confidence.md`, `Weighting.md`
- **Success:** `docs/Success/*` · **Schema:** `docs/Schema/KnowledgeGraph.md`, `EntityRelationship.md`, `PatternSchema.md`
- **Cross-project analogs:** `examples/CaseStudies/EigenLayer.md` (**EigenDA — DA competitor + restaking-security contrast**),
  `examples/CaseStudies/Ethereum.md` (**EIP-4844 blob competitor + Dencun value-accrual analog + rollup roadmap**),
  `examples/CaseStudies/Cosmos.md` (**CometBFT/SDK/IBC lineage; advisors Zaki Manian/Ethan Buchman**), `examples/CaseStudies/dYdX.md`
  (dalam snapshot Genesis Drop), `examples/Pioneer/Optimism.md` (OP Stack rollup). **Supersedes:** `examples/CaseStudies/Celestia.md`
  (Summary). **Gap candidates:** Avail, EigenDA (standalone), Dymension, Saga, AltLayer, Sovereign Labs, Conduit, Caldera.

## 21. Sources
_Deep Research provenance (Gemini). Sumber primer/kunci di bawah; bibliografi penuh di arsip mentah._

- Celestia: The First Modular Blockchain Network — celestia.org — https://celestia.org/
- LazyLedger: A Distributed Data Availability Ledger (Al-Bassam, 2019) — https://arxiv.org/abs/1905.09274
- Data Availability Sampling & Celestia — Celestia Docs — https://docs.celestia.org/learn/how-celestia-works/data-availability-layer
- Celestia (TIA) Tokenomics & Allocation — DropsTab — https://dropstab.com/coins/celestia
- Celestia Raises $100M at $3B Valuation (Bain Capital Crypto) — CoinDesk — https://www.coindesk.com/business/2024/09/23/celestia-raises-100m
- CIP-31: Lock Staking Rewards for Vesting Accounts (Lotus) — Celestia Improvement Proposals — https://github.com/celestiaorg/CIPs
- Matcha (v6) & CIP-38 128MB Blocks — Celestia Blog — https://blog.celestia.org/
- Fibre: 1 Tb/s Blockspace with ZODA — Celestia Blog — https://blog.celestia.org/fibre
- Polychain's TIA Staking Rewards Extraction — on-chain analysis (RootData) — https://www.rootdata.com/Projects/detail/Celestia
- EigenDA vs Celestia vs Avail — Data Availability Comparison — https://l2beat.com/data-availability
- Celestia (TIA) Price, Market Cap & FDV — CoinGecko — https://www.coingecko.com/en/coins/celestia

_(Full bibliography retained in the original Deep Research report + archived at
`doc_backup/deep/Celestia_2026-07_gemini.md`.)_
