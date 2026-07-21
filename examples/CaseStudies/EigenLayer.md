# EigenLayer / EigenCloud — Deep Case Study

**CIF Dataset — Deep Dossier · Tier: Deep (anchor project)**
**Source:** Deep Research (Gemini) — *"Laporan Intelijen Analisis Mendalam: Pelopor Restaking EigenLayer dan Transparansi Awan Komputasi Terverifikasi EigenCloud"*.
**Pipeline position:** Applications layer — anchor artifact structured against the full `docs/` ontology.
The **absolute pioneer of the restaking category** and the **security substrate the LRT ecosystem was built on**
(ether.fi D10, Renzo, Kelp, Puffer, Swell all farmed its points) — now the dataset's clearest **infrastructure→
enterprise platform pivot** (restaking → EigenCloud "verifiable AWS for AI"). Also the **slashing-induced capital
realignment** case: TVL $20,09 mrd → $4,3–8,9 mrd after real risk got priced in. **Supersedes** the Batch-01 Summary
`examples/Pioneer/EigenLayer.md`.
**Raw source archived:** `doc_backup/deep/EigenLayer_2026-07_gemini.docx` (+ `.md` text extraction).
**Input note:** authored in the CIF no-table contract; extracted via `tools/extract.py` (0 tables, 0 chips,
23 sections); fidelity checked with `tools/reconcile.py`.

> Knowledge artifact (real curated data), not a documentation container. This is a **deep dossier**: it
> preserves *causality* (why events happened), which is the raw material for prediction. Conforms to
> `templates/CaseStudyTemplate.md`.

---

## 1. Identity
_ref: `docs/Ontology/Identity.md`_

- **Project:** EigenLayer (rebranded **EigenCloud**, 17 Jun 2025; token: **EIGEN** / **bEIGEN** isolated staking variant).
- **Category:** Infrastructure — **Restaking (rehypothecation) pioneer** → **Verifiable Cloud / decentralized-AI infra**.
- **Era:** 2021 (UW research) – sekarang. **Founder/CEO:** **Sreeram Kannan** (ex-Associate Professor AI/blockchain, UW).
  Entitas: **EIGEN Labs, Inc.** (29 Jun 2021) + **Layr Labs, Inc.** (29 Agu 2022). COO **Chris Dury**, CSO **Calvin Liu**.
- **Innovation archetype:** **First Mover** — mendefinisikan kategori restaking (EigenPods/AVS) + **intersubjective
  fork-aware staking** (EIGEN).
- **Skala:** **monopoli struktural 93–94%** pangsa restaking global; EigenDA di **>60 rollup**; TVL puncak **$20,09 mrd**
  (Jun 2024); pendanaan kumulatif **~$220 juta** (a16z lead).

## 2. Classification
_ref: `docs/Ontology/Classification.md`, `docs/Taxonomy/Sectors.md`, `docs/Taxonomy/Technologies.md`_

Infrastructure restaking · evolusi **EigenPods/AVS shared-security → EigenDA (DA) → slashing mainnet → EigenCloud
(EigenCompute/EigenVerify/EigenAI/AgentKit)** · di atas **Ethereum PoS** · primitif: **restaking withdrawal-credentials,
Operator Sets, Unique Stake Allocation, intersubjective forking (EIGEN), TEE compute (AMD SEV-SNP / Intel TDX), KZG-proof
DA** · token **EIGEN** (inflationary, work-token) · value-accrual via **ELIP-12 buyback-and-burn** (EigenDA/EigenCloud fees).

## 3. Pre-Conditions — Fragmented Trust pasca-PoS (2021–22)
_Konteks: mengapa EigenLayer harus ada._
_ref: `docs/Meta/Narratives.md`, `docs/Ontology/Revenue.md`_

Pasca-Merge, jaminan modal Ethereum terkonsentrasi kuat di lapisan konsensus utama, tapi setiap jaringan di luar EVM
(orakel, **bridge**, middleware, **DA**) harus **bootstrap keamanan dari nol** — mahal, hambatan ekonomi besar. Tiga
implikasi: (1) **token inflasioner** untuk insentif validator awal → volatilitas melemahkan keamanan; (2) **bridge/orakel
di-amankan validator kecil** dengan jaminan < nilai yang diamankan → eksploit ratusan juta dolar; (3) **LSD idle** (stETH
Lido mengendap pasif tanpa kegunaan keamanan tambahan). EigenLayer memanfaatkan **staked ETH yang sudah ada** untuk
amankan banyak layanan sekaligus. → `examples/Pioneer/Lido.md` (stETH), `examples/CaseStudies/CrossAnalysis-ETH-Lido-EigenLayer.md`.

## 4. Origin & Team — dari UW Blockchain Lab ke miliaran dolar
_ref: `docs/Ontology/Team.md`, `docs/Project/Philosophy.md`_

Berakar di **University of Washington (Seattle)**: **Sreeram Kannan**, Associate Professor AI/blockchain yang memimpin
**UW Blockchain Lab**, mengidentifikasi inefisiensi bootstrap konsensus; tim teknik perdana direkrut dari peneliti
mahasiswa. **EIGEN Labs, Inc.** didirikan **29 Jun 2021**; **Layr Labs, Inc.** **29 Agu 2022** (entitas komersial induk).
Kepemimpinan: **Sreeram Kannan** (CEO), **Chris Dury** (COO), **Calvin Liu** (CSO).

**Skandal netralitas (crown governance risk):** **Justin Drake** & **Dankrad Feist** (peneliti inti **Ethereum
Foundation**) jadi **advisor berbayar** dengan kompensasi **EIGEN jutaan dolar** (terungkap 19 Mei 2024) → kemarahan
komunitas atas rusaknya **credible neutrality** lapisan konsensus ETH → keduanya **mengundurkan diri akhir 2024**. → §15, `docs/Reasoning/Confidence.md`.

## 5. Innovation Analysis — Restaking + Intersubjective Forking
_ref: `docs/Ontology/Innovation.md`, `docs/Innovation/FirstMover.md`, `docs/Innovation/CompetitiveMoat.md`, `docs/Ontology/Technology.md`_

1. **Restaking / programmable staking** — validator arahkan **withdrawal credentials** staked-ETH ke kontrak **EigenPods**
   → mengikat diri ke **aturan slashing tambahan AVS eksternal**; kesalahan operasional → modal dipotong di **lapisan dasar
   Ethereum**. Dampak: **menurunkan biaya sewa keamanan terdesentralisasi secara radikal** (AVS pinjam pool jaminan miliaran dolar tanpa bootstrap sendiri).
2. **Intersubjective staking (EIGEN, fork-aware token)** — untuk kesalahan yang **disepakati manusia tapi mustahil
   dibuktikan on-chain** (bukan kesalahan objektif spt double-signing): pemegang jujur dapat **fork token EIGEN**; fork yang
   memotong alokasi pelaku ditetapkan **kanonik via konsensus sosial**. → standar baru koordinasi sengketa non-matematis.

*Dampak/moat:* menyatukan jaminan ekonomi Ethereum untuk keamanan protokol eksternal → **kategori baru** yang dikuasai
93–94% + **melahirkan seluruh sektor LRT** (§9). → `examples/CaseStudies/EtherFi.md`, `docs/Innovation/FirstMover.md`.

## 6. Technology Evolution — Restaking → EigenDA → Slashing → EigenCloud
_ref: `docs/Ontology/Technology.md`, `docs/TokenLifecycle/*`, `docs/Ontology/Infrastructure.md`_

- **PoC & Testnet (Agu 2022 – Apr 2023):** smart contract restaking + audit; **testnet publik 7 Apr 2023** (EigenPods).
- **Mainnet bertahap (Jun 2023 – Apr 2024):** deposit LST (stETH/cbETH/rETH) dibatasi **caps**; **17 Apr 2024** caps dicabut → likuiditas pasar bebas.
- **EigenDA — AVS perdana (10 Apr 2024):** DA berbasis restaking + **KZG proofs** → potong biaya DA rollup **hingga 90%**.
- **Slashing mainnet (17 Apr 2025):** **ELIP 002/003/004** — feature-complete; **Operator Sets** (AVS saring validator) +
  **Unique Stake Allocation** (isolasi alokasi jaminan per-AVS → cegah penularan risiko slashing).
- **EigenCloud rebrand (17 Jun 2025):** **EigenCompute** (Docker off-chain di **TEE** AMD SEV-SNP/Intel TDX) · **EigenVerify**
  (arbitrase intersubjektif via forking) · **EigenAI** (inferensi AI deterministik bit-exact, buktikan akurasi) · **EigenDA** dioptimasi **100 MB/detik**.
- **Era agen otonom (akhir 2025 – 2026):** **Google Cloud Web3 Faucet** (EIGEN testnet Hoodi, 24 Okt 2025) → **AgentKit beta
  (27 Mar 2026):** agen AI otonom + dompet **USDC** on-chain + identitas kriptografis.

## 7. Funding Intelligence
_ref: `docs/Ontology/Funding.md`, `docs/Ontology/Tokenomics.md`, `docs/TokenLifecycle/TGE.md`_

| Putaran | Tanggal | Dana | Valuasi post-money | Investor kunci |
|---|---|---|---|---|
| **Series A-1** | 19 Apr 2022 | **$14,48 juta** ($2,44/shr) | $57,92 juta | Ambush, Blockchain Capital, Figment |
| **Seed** | 1 Agu 2022 | **$14,5 juta** | $75 juta (12-bln cliff + 4%/bln) | **Polychain, Ethereal Ventures** · Robot, Figment |
| **Series A** | 28 Mar 2023 | **$50 juta** ($8,31/shr) *(+$64,48 juta ekuitas tambahan per SEC filing)* | $283,65 juta *(alt $500 juta)* | **Blockchain Capital** · Electric, Coinbase Ventures, Hack VC |
| **Series B** | 22 Feb 2024 | **$100 juta** ($28,77/shr) | **$1,02–1,1 mrd** (unicorn) | **a16z** (tunggal) |
| **OTC Token** | 17 Jun 2025 | **$70 juta** | — | **a16z crypto** (beli EIGEN dari Eigen Foundation → danai EigenCloud) |

**Total ~$220 juta.** *(INKONSISTENSI: Tracxn $241 juta / Rootdata $234,5 juta / Forge $164,48 juta / DefiLlama $220 juta —
beda metodologi ekuitas Layr Labs vs OTC token yayasan. Evidence LOW.)* → `docs/Ontology/Funding.md`.

## 8. Tokenomics — EIGEN Universal Work Token (Inflationary)
_ref: `docs/Ontology/Tokenomics.md`, `docs/Ontology/Incentives.md`, `docs/MarketBehaviour/UnlockImpact.md`, `docs/Patterns/Flywheel.md`_

- **Sifat:** **tak terbatas / inflationary**; **bEIGEN** = varian staking terisolasi. **TGE supply:** **1.673.646.668 EIGEN**.
- **Initial float TGE:** **200 juta (11,95%)** — *low-float* (paralel ether.fi 11,52%, §11/§18). **Supply Jul 2026:** ~**1,82 miliar** (beredar ~741 juta).
- **Alokasi:** Komunitas/Ecosystem **45%** (Stakedrops 15% + R&D 15% + Inisiatif masa depan 15%) · **Investor privat 29,5%** · **Kontributor awal (tim/advisor) 25,5%**.
- **Vesting:** cliff 1 th (transferabilitas 30 Sep 2024) → **unlock linear 4%/bln** selama 24 bln sejak **30 Sep 2025** → **tekanan jual ~38,35 juta EIGEN/bln** (crown sell-pressure, §11/§17-R2).
- **Emisi:** inflasi **4%/th** (~1,29 juta EIGEN/minggu) untuk imbalan validator/deposan.

**Value-accrual (deflasi):** **ELIP-12** — **Incentives Committee** alirkan sebagian pendapatan **EigenDA + EigenCloud** untuk
**buyback-and-burn** EIGEN di pasar terbuka. *(Aliran fee-riil masih tipis vs emisi 4% — lebih lemah dari fee-switch Aave/dYdX/Cosmos; lihat §16 & §18 open Q3.)*

## 9. Airdrop, Community & Competitive Landscape
_ref: `docs/Patterns/Points.md`, `docs/Success/Airdrop.md`, `docs/Ontology/Community.md`, `docs/Valuation/Competitors.md`_

**EigenLayer Points (pertengahan 2023):** linear = staked-ETH/LST × durasi kunci → **point-farming frenzy**; LRT pihak-ketiga
(**ether.fi, Renzo, Kelp, Puffer**) tumpuk **dual-points** → leverage sirkular. **Krisis keadilan:** distribusi linear
memihak **whales** yang masuk sesaat sebelum snapshot → kemarahan ritel (Discord/X) → **e-beggars**.
- **Stakedrop S1:** ~**113 juta EIGEN (6,75%)**, snapshot 15 Mar 2024 (blok #19437000), klaim 10 Mei–7 Sep 2024; **floor 110 EIGEN** (bonus flat 100) meredam kemarahan whale-bias; **blokir IP** AS/Kanada/RRT/dll.
- **Stakedrop S2:** ~**87 juta EIGEN (5,2%)**, snapshot 15 Agu 2024; linear murni tanpa floor (anti-sybil). *(INKONSISTENSI: Dune p2p_org catat ~5,0%. Evidence LOW.)*

**Kompetitif (perang restaking segitiga):**
- **Symbiotic** (2024, Series A **$34,8 juta** pimpin **Pantera**) — **collateral-agnostic + permissionless**, slashing/insentif di **vault level** (bukan komite tata kelola).
- **Karak** — multi-aset hibrida lintas rantai (Ethereum/Blast/BNB/Mantle + L2 sendiri K2); antrean tarik **9 hari** vs EigenLayer **7 hari** awal.
- **EigenLayer tetap monopoli 93–94%** — kedalaman likuiditas + slashing teruji sejak Apr 2025 + EigenDA di >60 rollup. *(Symbiotic/Karak/Renzo/Kelp/Swell = kandidat gap dataset.)*

## 10. Narrative & Product Evolution — Restaking → Verifiable Cloud/AI
_ref: `docs/Meta/Narratives.md`, `docs/Patterns/Narrative.md`, `docs/Project/Roadmap.md`, `docs/Ontology/Adoption.md`_

**Narasi per fase:** **Rehipotekasi DeFi & yield** (2022–23, restaking modal LST pasif) → **Shared Security & DA** (2024,
lawan **Celestia** — "DA harus dilindungi jaminan ETH", EigenDA) → **Verifiable Cloud & AI infra** (2025–26, reposisi radikal
"**AWS bagi Web3**" — verifiable AI inference + agen otonom, mempertahankan minat institusi saat DeFi lesu).

**Product:** protokol kriptografi mentah (EigenPods, operator registration, 2022–23) → **EigenDA** (Apr 2024, KZG, −90% biaya
DA) → **platform keamanan dua-arah** (slashing Apr 2025: Operator Sets + Unique Stake Allocation) → **EigenCloud primitives**
(Jun 2025: EigenCompute TEE / EigenVerify / EigenAI) → **AgentKit** (Mar 2026: agen AI + dompet USDC + inferensi otomatis). → `examples/CaseStudies/EtherFi.md` (LRT konsumen di atas restaking), `docs/Ontology/Adoption.md`.

## 11. Token Lifecycle & Price Causality
_ref: `docs/MarketBehaviour/*`, `docs/Valuation/FairValue.md`, `docs/Reasoning/Prediction.md`_

| Titik | Nilai | Kondisi |
|---|---|---|
| Pra-TGE OTC | $2,00–3,50 (rumor FDV $2 mrd) | Agu–Sep 2024 |
| Transferabilitas | $3,50–4,50 (FDV **$6,7 mrd**, vol $400 juta) | 30 Sep–1 Okt 2024 |
| **ATH** | **$5,65** | 17 Des 2024 (puncak spekulasi restaking) |
| Koreksi pasca-slashing | **<$1,00** | Apr–Sep 2025 (risiko operasional nyata) |
| Pemulihan rebranding | $1,16–1,17 (+10%) | Jun–Jul 2025 (EigenCloud + OTC $70 juta a16z) |
| **ATL** | **$0,1483** *(alt $0,1484)* | 5 Apr 2026 (tekanan unlock 38,35 juta/bln) |

**Fair value:** **MC/TVL ~0,03** (awal 2025) → **undervalued ekstrem**: MC riil ~$171–320 juta vs TVL diamankan
**$4,3–11,2 mrd**. Diskon merefleksikan **"tail-end risk"** — kecemasan sengketa slashing massal off-chain yang belum teruji ekstrem. → `docs/Valuation/FairValue.md`.

## 12. Business Intelligence — TVL, Revenue, Aethir GPU
_ref: `docs/Ontology/Revenue.md`, `docs/Valuation/Revenue.md`, `docs/Ontology/Metrics.md`, `docs/Valuation/TVL.md`, `docs/Success/Adoption.md`_

**TVL:** $250 juta (Des 2023) → $7 mrd (Feb 2024) → **puncak $20,09 mrd** (Jun 2024, *alt $19,7 mrd*) → ~$17,51 mrd (akhir 2025) →
**$4,3–8,9 mrd** (pertengahan 2026, pasca-slashing realignment). *(INKONSISTENSI: Sacra $12 mrd — lag input. Evidence LOW.)*

**Revenue kotor per kuartal:** Q3 2024 **$801** → Q4 2024 **$63,27 juta** (puncak) → Q1 2025 $31,93 juta → Q2 $16,68 juta →
Q3 $21,71 juta → Q4 $16,21 juta → Q1 2026 $8,74 juta → Q2 2026 **$2,49 juta** (tren turun tajam). **Q1 2026:** annualized fees
$44,04 juta; cumulative fees $161,32 juta; cumulative incentives $161,74 juta → **Token Holder Net Income = $0** (emisi ≈ fee).

**Aliansi GPU Aethir (2025):** pendapatan kumulatif **$127,8 juta**; **ARR $166 juta** (Q3 2025); **1,5 miliar+ jam GPU**;
**440.000+ kontainer** di 94 negara. → sinyal traksi DePIN/AI-compute nyata di luar DeFi sirkular. → `docs/Valuation/Revenue.md`.

## 13. POV Success-Matrix (§15)
_ref: `docs/Success/*`, `docs/Reasoning/Explainability.md`, `docs/Reasoning/Confidence.md`_

| POV | Verdict | Alasan | Evidence |
|-----|---------|--------|----------|
| **Founder** (`Success/Founder.md`) | ✅ Sukses | Tesis akademik → industri miliaran dolar; monopoli 93% + pendanaan tak tertandingi $220 juta | HIGH |
| **VC** (`Success/VC.md`) | ⚠️ Campuran | Kuasai simpul kritis keamanan ETH; tapi **paper loss** Series B ($100 juta) + OTC ($70 juta), EIGEN −90% dari ATH | HIGH |
| **Retail** (`Success/Community.md`) | ❌ Gagal | Airdrop linear rugikan deposan kecil vs whale; de-peg LRT (ezETH −18–20%, Apr 2024) → likuidasi paksa | HIGH |
| **Community** (`Success/Community.md`) | ⚠️ Campuran | Berhasil paksa floor airdrop adil; tapi **skandal advisor EF rahasia** cederai netralitas kredibel | MEDIUM |
| **Developer** (`Success/Developer.md`) | ✅ Sukses | Akses instan pool keamanan miliaran dolar tanpa bootstrap; EigenDA potong biaya DA 90% | HIGH |
| **Institution** (`Success/Adoption.md`) | ✅ Sukses | Saluran yield-berlipat dari ETH terkelola via delegasi terenkripsi, tanpa lepas kustodi | HIGH |
| **Validator** (`Success/Protocol.md`) | ⚠️ Campuran | Pendapatan komisi operator 5% AVS; tapi slashing Apr 2025 = beban risiko pemotongan teknis ekstrem | MEDIUM |
| **Builder** (`Success/Ecosystem.md`) | ✅ Sukses | LRT (ether.fi/Swell/Kelp/Renzo) tunggangi demam poin → TVL miliaran → TGE premium (ETHFI/REZ) | HIGH |

**Takeaway:** menang di Founder/Developer/Institution/Builder; **Retail GAGAL** (whale-bias + de-peg LRT); campuran
VC/Community/Validator (paper loss, skandal netralitas, beban slashing). Kontras dgn ether.fi (D10) yang menang lebih luas.

## 14. Historical Timeline
_ref: `docs/TokenLifecycle/*`_

- **29 Jun 2021** — EIGEN Labs, Inc. (Seattle). **19 Apr 2022** — Series A-1 $14,48 juta. **1 Agu 2022** — Seed $14,5 juta (Polychain). **29 Agu 2022** — Layr Labs, Inc.
- **28 Mar 2023** — Series A $50 juta (Blockchain Capital). **7 Apr 2023** — testnet publik. **Jun 2023** — mainnet terbatas (caps LST).
- **5 Feb 2024** — caps LST dicabut (→ **$1 mrd masuk 24 jam**). **22 Feb 2024** — Series B $100 juta (a16z). **15 Mar 2024** — snapshot S1 (blok #19437000). **10 Apr 2024** — **EigenDA mainnet**. **10 Mei 2024** — klaim S1. **19 Mei 2024** — **kontroversi advisor Justin Drake**. **15 Agu 2024** — snapshot S2.
- **30 Sep 2024** — **transferabilitas EIGEN** (perdagangan bebas). **5 Okt 2024** — **hack $5,7 juta** (insiden eksternal terisolasi). **17 Des 2024** — **ATH $5,65**. **Akhir 2024** — advisor EF mundur (pulihkan netralitas).
- **17 Apr 2025** — **slashing mainnet** (ELIP 002–004) → TVL $15 mrd → $7 mrd. **17 Jun 2025** — **rebrand EigenCloud** + OTC $70 juta a16z. **8 Jul 2025** — **PHK 29 karyawan (25%)**. **24 Okt 2025** — Google Cloud Faucet (Hoodi).
- **27 Mar 2026** — **AgentKit beta**. **5 Apr 2026** — **ATL $0,1483** (kejenuhan unlock bulanan).

## 15. Slashing Realignment, Neutrality Scandal, Pivot, Current Status, Lessons
_ref: `docs/Ontology/Security.md`, `docs/Patterns/Failure.md`, `docs/Patterns/Recovery.md`, `docs/TokenLifecycle/Maturity.md`_

### Slashing-induced capital realignment *(causal core — risk repricing)*
Aktivasi slashing (**17 Apr 2025**, ELIP 002–004) mengubah restaking dari **"asumsi bebas risiko"** jadi **risiko
operasional nyata** → validator hindari pemotongan modal tak disengaja → **penarikan modal spekulatif masif** → TVL $20,09 mrd
→ $4,3–8,9 mrd (**leverage wash-out**), menyisakan staker institusional jangka panjang. Sinyal: *points-farming menciptakan
permintaan palsu yang runtuh saat risiko nyata muncul.*

### Neutrality scandal *(causal core — governance)*
Advisor berbayar **Justin Drake / Dankrad Feist** (peneliti EF, EIGEN jutaan dolar) → krisis kepercayaan **credible
neutrality**; mundur akhir 2024. Pelajaran: *netralitas sosial > kedekatan politik; menyerap otoritas dengan token justru merusak kredibilitas.*

### Infrastructure→enterprise pivot *(causal core — survival)*
Deteksi kejenuhan restaking murni + harga token jatuh → **PHK 25% (29 org, 8 Jul 2025)** + rebrand **EigenCloud** + primitif
**TEE compute** → amankan modal a16z ($70 juta) untuk vertikal **decentralized AI/DePIN**. *Transformasi dari jaminan ekonomi ke wadah komputasi TEE menyelamatkan proyek dari kepunahan narasi.*

**Status (pertengahan 2026):** **utility-driven recovery** — monopoli 93–94% bertahan; EigenCompute/AgentKit mulai berbuah
(puluhan proyek DePIN/agen-AI bayar sewa keamanan riil pakai EIGEN); tak lagi bergantung DeFi sirkular. Harga tertekan ATL karena unlock bulanan.

**Pelajaran:** (1) **points = noise** (bootstrap TVL tapi permintaan palsu, seimbangkan dengan risiko sejak hari-1); (2)
**skandal netralitas hancurkan konsensus sosial**; (3) **rebranding wajib didukung fleksibilitas teknologi** (TEE pivot).

## 16. Knowledge Extraction — Patterns & Lessons (§18–19)
_ref: `docs/Patterns/*`, `docs/Reasoning/*`, `docs/Schema/PatternSchema.md`_

1. **Slashing-Induced Capital Realignment** *(crown risk-repricing pattern)* — *aktivasi slashing mainnet → kekhawatiran
   pemotongan modal → penarikan spekulatif masif → TVL turun ke dasar institusional jangka panjang.* → `docs/Patterns/Failure.md`, `docs/Ontology/Security.md`.
2. **Point-farming Circular Leverage Loop** — *poin loyalitas linear → protokol LRT sekunder → leverage sirkular (LST ganda
   → cetak LRT) → inflasi TVL artifisial → de-peg jaminan sekunder (ezETH −18–20%) saat likuiditas terkunci di antrean.* → `docs/Patterns/Points.md`; `examples/CaseStudies/EtherFi.md`.
3. **Infrastructure-to-Enterprise Platform Pivot** — *yield DeFi turun → harga token depresiasi → PHK non-teknis + rebrand →
   primitif komputasi TEE → modal baru untuk vertikal Decentralized AI/DePIN.* → `docs/Patterns/Narrative.md`, `docs/Meta/Narratives.md`.
4. **Intersubjective Fork-Aware Governance** — *kesalahan tak-terbukti-on-chain → fork token → fork pemotong-pelaku jadi
   kanonik via konsensus sosial* → resolusi sengketa di luar logika EVM. → `docs/Reasoning/Confidence.md`, `docs/Ontology/Governance.md`.
5. **Shared-Security Bootstrapping** — *pool jaminan ETH tunggal → disewakan ke banyak AVS → hilangkan biaya bootstrap
   validator baru* → moat kategori + efek jaringan LRT. → `docs/Innovation/CompetitiveMoat.md`, `docs/Patterns/NetworkEffect.md`.

### Entitas & relasi ontologi (kandidat Knowledge Graph)
_ref: `docs/Schema/KnowledgeGraph.md`, `docs/Schema/EntityRelationship.md`_
- `[Sreeram_Kannan] —founded→ [EIGEN_Labs]` · `[EIGEN_Labs] —launched→ [EigenLayer]` · `[EigenLayer] —rebranded_to→ [EigenCloud]`
- `[EigenCloud] —deploys_data_via→ [EigenDA]` · `—runs_secure_compute_via→ [EigenCompute]` · `[AgentKit] —executes_on→ [EigenCloud]`
- `[a16z_crypto] —purchased_tokens_from→ [Eigen_Foundation]` · `[Justin_Drake] —accepted_fees_from→ [Eigen_Foundation]` (skandal netralitas)
- `[EtherFi]/[Renzo]/[Kelp]/[Puffer] —restake_on→ [EigenLayer]` · `[EigenLayer] —secures→ [AVS]` · `[Symbiotic]/[Karak] —compete_with→ [EigenLayer]`

## 17. Transferable Intelligence (§20) — rule candidates untuk protokol infrastruktur jaminan
_ref: `docs/Reasoning/AnalogEngine.md`, `docs/Reasoning/Weighting.md`, `docs/Reasoning/Confidence.md`_

- **R1 — MC/TVL Infra Rule:** untuk infrastruktur jaminan (restaking/PoS), **MC-beredar/TVL** tahun-pertama tidak boleh
  **>0,15**; di atas itu = **overvalued** rentan depresiasi. *(EIGEN ~0,03 = ekstrem undervalued spot, tapi lihat tail-risk.)*
- **R2 — Passive Sell-Pressure Rule:** jaringan dengan **unlock bulanan investor >4% float/bln** wajib punya **volume harian
  ≥15× nilai dolar unlock**; jika tidak → devaluasi konstan ke ATL baru. *(EIGEN 38,35 juta/bln = penekan harga ke ATL.)*
- **R3 — Forkability Premium:** protokol dengan **token forking** (EIGEN) punya ketahanan koordinasi sosial > token utilitas
  murni → beri **premium valuasi** untuk resolusi sengketa kesalahan subjektif.
- **R4 — Points→Risk Reality Filter:** TVL yang di-bootstrap points wajib di-diskon; nilai riil = TVL yang **bertahan pasca
  event risiko nyata** (slashing/de-peg), bukan puncak farming. *(EigenLayer $20,09 mrd → dasar institusional.)*

## 18. Open Questions (§21)
_Research gap — belum tervalidasi._
1. Bagaimana forking EIGEN bertahan jika penyerang pegang **>40% pasokan** — apakah konsensus sosial tetap saring pemegang jujur tanpa hancurkan likuiditas? (evidence: LOW)
2. Apakah pengembang Web2 bersedia tanggung **overhead TEE (EigenCompute)** dibanding cloud tersentralisasi yang lebih efisien? (MEDIUM)
3. Bagaimana insentif staker dipelihara saat **emisi 4%/th melambat** sedangkan **fee AVS riil belum cukup** tutup biaya operator? (MEDIUM)

## 19. Evidence Level — kesimpulan kunci (§22)
_ref: `docs/Reasoning/Confidence.md`, `docs/Research/Verification.md`_

| Kesimpulan | Evidence | Alasan |
|---|---|---|
| Rebrand EigenCloud = taktik pivot ke AI terdesentralisasi pasca-koreksi DeFi | **HIGH** | AgentKit + TEE AMD/Intel + PHK 25% + OTC $70 juta a16z khusus EigenCloud |
| Slashing 17 Apr 2025 = penyebab langsung penyusutan TVL | **HIGH** | Kronologi DefiLlama + LlamaRisk: penarikan persis pasca ELIP 002–004 |
| Pendanaan kumulatif tepat $241 juta | **LOW** | Basis data bertolak belakang (Tracxn $241/Rootdata $234,5/Forge $164,48/DefiLlama $220 juta) |
| Tokenomics supply awal / alokasi | **LOW** | Pembulatan bursa (Whitepaper 1,67 mrd vs Rootdata 1,673646668 mrd; Dune S2 5,0% vs 5,2%) |

## 20. Related Framework Definitions
- **Ontology:** `docs/Ontology/Identity.md`, `Team.md`, `Funding.md`, `Tokenomics.md`, `Incentives.md`,
  `Governance.md`, `Security.md`, `Risks.md`, `Technology.md`, `Infrastructure.md`, `Ecosystem.md`, `Community.md`, `Revenue.md`, `Metrics.md`, `Adoption.md`, `Innovation.md`
- **Innovation:** `docs/Innovation/FirstMover.md`, `CompetitiveMoat.md`, `ProductMarketFit.md`, `Execution.md`
- **Patterns:** `docs/Patterns/Points.md`, `NetworkEffect.md`, `Failure.md`, `Recovery.md`, `Narrative.md`, `Flywheel.md`
- **Valuation/Market:** `docs/Valuation/FairValue.md`, `Revenue.md`, `Competitors.md`, `TVL.md`; `docs/MarketBehaviour/UnlockImpact.md`; `docs/Meta/Narratives.md`, `MarketCycles.md`
- **Reasoning:** `docs/Reasoning/Prediction.md`, `AnalogEngine.md`, `Confidence.md`, `Weighting.md`
- **Success:** `docs/Success/*` · **Schema:** `docs/Schema/KnowledgeGraph.md`, `EntityRelationship.md`, `PatternSchema.md`
- **Cross-project analogs:** `examples/CaseStudies/EtherFi.md` (**LRT terbesar yang dibangun DI ATAS** restaking EigenLayer +
  low-float toxicity paralel), `examples/CaseStudies/CrossAnalysis-ETH-Lido-EigenLayer.md` (staking→restaking stack),
  `examples/Pioneer/Lido.md` (stETH direstake), `examples/CaseStudies/Aave.md`/`dYdX.md`/`Cosmos.md` (bandingkan value-accrual
  ELIP-12 buyback vs fee-switch 100%). **Supersedes:** `examples/Pioneer/EigenLayer.md` (Summary). **Gap candidates:** Symbiotic, Karak, Renzo, Kelp DAO, Swell, Puffer, Celestia (DA competitor), Aethir (DePIN GPU).

## 21. Sources
_Deep Research provenance (Gemini). Laporan sumber mengutip **80 referensi**; sumber primer/kunci di bawah._

- EIGEN: The Universal Intersubjective Work Token (Whitepaper) — EigenCloud — https://docs.eigencloud.xyz/assets/files/EIGEN_Token_Whitepaper-0df8e17b7efa052fd2a22e1ade9c6f69.pdf
- EigenLayer and EIGEN Token Explained — Nethermind — https://www.nethermind.io/blog/eigenlayer-and-eigen-token-explained
- EigenLayer Activates Mainnet Slashing on April 17 (ELIPs 002–004) — The Defiant — https://thedefiant.io/news/blockchains/eigenlayer-activates-mainnet-slashing-on-april-17-implementing-elips-002-004-ecb683e0
- EigenLayer: The $15B-to-$7B Crash Nobody Saw Coming — Medium (Cynthia Cheng) — https://medium.com/@pycheng9/eigenlayer-the-15b-to-7b-crash-nobody-saw-coming-d8e73f7b3169
- a16z crypto invests $70M in direct EigenLayer token deal (EigenCloud) — The Block — https://www.theblock.co/post/358511/a16z-crypto-eigen-token-eigencloud
- Eigen Labs Reduces Workforce by 25% to Focus on EigenCloud — ForkLog — https://forklog.com/en/eigen-labs-reduces-workforce-by-25-to-focus-on-eigencloud/
- Community Erupts as EF Players Become Advisors to EigenLayer — The Defiant — https://thedefiant.io/news/blockchains/community-erupts-as-key-players-from-ethereum-foundation-become-advisors-to-eigenlayer
- Introducing the Eigen Foundation, EIGEN token and Season 1 stakedrop — Eigen Foundation — https://blog.eigenfoundation.org/announcement/
- EIGEN Tokenomics: Intersubjective Staking and Forking — Figment — https://www.figment.io/insights/eigen-tokenomics-eigenlayers-token-for-intersubjective-staking-and-forking/
- Current State of Symbiotic — LlamaRisk — https://www.llamarisk.com/research/current-state-of-symbiotic
- AVS Risk Assessment: EigenDA — LlamaRisk — https://llamarisk.com/research/avs-risk-assessment-eigenda
- EigenCloud analysis — Sacra — https://sacra.com/c/eigencloud/
- EigenLayer Crosses $18B in Restaked ETH (Vertical AVS Specialization) — BlockEden — https://blockeden.xyz/blog/2026/03/20/eigenlayer-18b-tvl-vertical-avs-specialization-restaking-evolution/
- EigenCloud TVL, Fees & Revenue — DefiLlama — https://defillama.com/protocol/eigencloud
- EIGEN goes live on Google Cloud's Web3 faucet — CryptoRank — https://cryptorank.io/news/feed/fdd00-eigen-goes-live-on-google-clouds-web3-faucet-to-boost-developer-testing

_(Full 80-source bibliography retained in the original Deep Research report + archived at
`doc_backup/deep/EigenLayer_2026-07_gemini.md`.)_
