# Aave — Deep Case Study

**CIF Dataset — Deep Dossier · Tier: Deep (anchor project)**
**Source:** Deep Research (Gemini) — *"Laporan Intelijen Kripto: Analisis Komprehensif Protokol Aave"*.
**Pipeline position:** Applications layer — anchor artifact structured against the full `docs/` ontology.
The **dominant DeFi money-market (lending) protocol**, a **First Mover** (Flash Loans, aTokens), and the third
strong **value-accrual reform** instance in the dataset (mirrors dYdX D8 / Cosmos D7). **Supersedes** the
Batch-01 Summary `examples/Pioneer/Aave.md`.
**Raw source archived:** `doc_backup/deep/Aave_2026-07_gemini.docx` (+ `.md` text extraction).
**Input note:** authored in the CIF no-table contract; extracted via `tools/extract.py` (0 tables, 0 chips,
23 sections); fidelity checked with `tools/reconcile.py`.

> Knowledge artifact (real curated data), not a documentation container. This is a **deep dossier**: it
> preserves *causality* (why events happened), which is the raw material for prediction. Conforms to
> `templates/CaseStudyTemplate.md`.

---

## 1. Identity
_ref: `docs/Ontology/Identity.md`_

- **Project:** Aave (dahulu **ETHLend**; token: **AAVE**, sebelumnya **LEND**).
- **Category:** DeFi — **pasar uang / lending non-kustodian** (pooled liquidity P2C). Penerbit stablecoin **GHO**.
- **Era:** 2017 (London) – sekarang. **Founder:** **Stani Kulechov**. **LEND TGE:** 31 Des 2017; **migrasi AAVE:** Okt 2020.
- **Innovation archetype:** **First Mover** — Flash Loans, aTokens, eMode jadi **standar industri**.
- **Skala:** pangsa pasar lending DeFi **59,79%** (Mar 2026); deposit historis **$3,46 triliun**; pinjaman
  historis **$1 triliun**; net revenue 2025 **$141,8 juta**.

## 2. Classification
_ref: `docs/Ontology/Classification.md`, `docs/Taxonomy/Sectors.md`, `docs/Taxonomy/Technologies.md`_

DeFi lending · evolusi **ETHLend P2P → V1/V2/V3 pooled P2C → V4 Hub-and-Spoke modular** · multi-chain (Ethereum
+ L2/sidechain) · primitif: **Flash Loans, aTokens (1:1 rebasing), Rate Switching, Credit Delegation, eMode,
Isolation Mode** · stablecoin **GHO** · asuransi **Umbrella (ERC-4626)** · RWA **Horizon** · value-accrual via
**buyback $50 juta/th** (Aavenomics 3.0 / "Aave Will Win").

## 3. Pre-Conditions — Kebuntuan Likuiditas P2P (2017)
_Konteks: mengapa Aave harus ada._
_ref: `docs/Meta/Narratives.md`, `docs/Ontology/Revenue.md`_

2017 = era ICO spekulatif; pemegang kripto tak punya opsi likuiditas selain **jual** (konsekuensi pajak +
hilang eksposur). Lending gen-1 (**P2P murni**): pemberi & peminjam sepakati manual jumlah/bunga/tenor/jaminan →
**inefisiensi pencocokan, likuiditas terfragmentasi, gas mahal**. **Compound** memelopori **pooled P2C**. ETHLend
lahir untuk memecahkan kebuntuan likuiditas; saat P2P terbukti tak berskala (bear 2018–19), tim rekayasa ulang
ke **kolam bersama**. → `examples/Pioneer/Uniswap.md` (AMM), competitor Compound.

## 4. Origin & Team
_ref: `docs/Ontology/Team.md`, `docs/Project/Philosophy.md`_

**Stani Kulechov** (mahasiswa hukum U. Helsinki; coding sejak umur 12) — Ethereum Whitepaper mengkristalkan visi
smart contract untuk perjanjian keuangan immutable tanpa pihak ketiga. Didirikan **London, 1 Mei 2017** sebagai
**ETHLend**; whitepaper 15 Jun 2017. Tim: **Jordan Lazaro Gustave** (COO), Nolvia Serrano (CMO), Anastasija
Plotnikova, Martin Wichmann, Jitendra Chittoda, Anthony Akentiev. **Rebrand → Aave** (Finlandia: *"hantu"* —
likuiditas transparan tak terlihat) **akhir 2018** setelah P2P memproses volume kecil.

## 5. Innovation Analysis — Flash Loans, aTokens, Hub-and-Spoke
_ref: `docs/Ontology/Innovation.md`, `docs/Innovation/FirstMover.md`, `docs/Innovation/CompetitiveMoat.md`, `docs/Ontology/Technology.md`_

1. **Flash Loans (Jan 2020)** — pinjaman **tanpa jaminan** pertama, memanfaatkan **atomisitas** transaksi
   (batal jika tak dilunasi dalam satu blok) → demokratisasi modal arbitrase.
2. **aTokens (Jan 2020)** — dipatok **1:1** ke aset dasar, saldo **bertambah real-time** di dompet (vs cToken
   Compound berbasis exchange-rate) → integrasi dApp mudah.
3. **Rate Switching (Des 2020)** — peminjam pindah suku bunga variabel↔stabil (proteksi risiko bunga).
4. **Credit Delegation (V2)** — delegasi batas kredit ke pihak ketiga (jembatan pinjaman tanpa jaminan korporat).

*Dampak/moat:* eksekusi agresif menjadikan Aave **pemimpin pasar sejati** (meski Compound populerkan pooled dulu)
— mengubah DeFi dari spekulasi ritel ke pasar uang kegunaan riil.

## 6. Technology Evolution — V1 → V4 Hub-and-Spoke
_ref: `docs/Ontology/Technology.md`, `docs/TokenLifecycle/*`, `docs/Ontology/Infrastructure.md`_

- **ETHLend (2017):** P2P escrow kaku (jaminan dikunci ke pemberi tunggal).
- **V1 (Jan 2020):** shared liquidity pool (Ethereum); aTokens + Flash Loans dasar.
- **V2 (Des 2020):** gas **−15–20%**; flash liquidation; collateral swap; credit delegation.
- **V3 (Mar 2022 / Jan 2023):** multi-chain; **eMode** (LTV hingga **98%** untuk aset berkorelasi spt stETH/ETH);
  **Isolation Mode**; **Portals** (aToken lintas rantai).
- **V4 (Mar 2026):** **Hub-and-Spoke modular** — **Core Liquidity Hub** (likuiditas terpadu, cegah fragmentasi,
  akuntansi global) + **Spokes** (antarmuka modular: ritel/institusi/eMode). Kontrak: Hub.sol (stateless engine),
  Spoke.sol, GiverPositionManager, TakerPositionManager, SignatureGateway (**meta-tx/signed intents EIP-712**),
  NativeTokenGateway. *(Menyatukan likuiditas Morpho-style + isolasi risiko — jawaban kompetitif, §9.)*

## 7. Funding Intelligence
_ref: `docs/Ontology/Funding.md`, `docs/Ontology/Tokenomics.md`, `docs/TokenLifecycle/TGE.md`_

| Putaran | Tanggal | Dana | Investor kunci |
|---|---|---|---|
| **ICO (LEND)** | 25–30 Nov 2017 | **$17,86 juta** *(alt $16,2–17 juta)* · $0,0173/LEND | publik (30 menit, bonus presale 20%) |
| **Series A (OTC)** | 9 Jul 2020 | $4,5 juta + $3 juta = **$7,5 juta** | **ParaFi, Framework**, 3AC |
| **Series B** | 12 Okt 2020 | **$25 juta** *(VC tracker $29,5 juta)* | **Standard Crypto, Blockchain Capital**, 3AC |
| **Later Stage VC** | 18 Des 2024 | **$31 juta** | **Apollo Crypto** + manajer investasi swasta |

**Total: $75,5 juta.** *(INKONSISTENSI: aavenomics — LEND holders 13 juta AAVE/81,25%, Ecosystem Reserve 3
juta/18,75% — vs CryptoRank Private 72,3%/Reserve 23,1%/Public 4,6%. Evidence LOW.)*

## 8. Tokenomics — Governance → Cash-Flow Token (Aave Will Win)
_ref: `docs/Ontology/Tokenomics.md`, `docs/Ontology/Incentives.md`, `docs/MarketBehaviour/UnlockImpact.md`, `docs/Patterns/Flywheel.md`_

**Migrasi LEND→AAVE (Okt 2020):** rasio **100:1**, hard cap **16 juta AAVE** (dari 1,3 miliar LEND). Alokasi:
LEND holders **13 juta (81,25%)**, Ecosystem Reserve **3 juta (18,75%)**.

**Safety Module emisi (turun):** stkAAVE **315→260 AAVE/hari** (~3,25% APY); stkABPT **216→130/hari** (~6,10%);
stkGHO legacy **0** (pasca-Umbrella). **Slashing cap:** stkAAVE/stkABPT **20%→10%**.

### Aave Will Win (AWW) *(causal core — value accrual)*
**Buyback $50 juta/th** (Aavenomics 3.0), permanen **9 Apr 2025**; fase uji **94.000+ AAVE** ditarik (~$22 juta).
Kerangka **AWW** (temp check 2 Mar 2026 **52,58%**; lolos **13 Apr 2026 ~75%**): **100% pendapatan produk → kas
DAO** untuk buyback → mengubah AAVE dari **token tata kelola** jadi **aset arus-kas** (memungkinkan valuasi DCF).
*(Pola & fix yang sama dengan dYdX Prop #313 dan Cosmos value-accrual — lihat §16.)* → `examples/CaseStudies/dYdX.md`, `Cosmos.md`.

## 9. Airdrop, Community & Competitive Landscape
_ref: `docs/Patterns/Points.md`, `docs/Success/Airdrop.md`, `docs/Ontology/Community.md`, `docs/Valuation/Competitors.md`_

**Tidak ada retroactive airdrop** — Aave pakai **liquidity mining** terarah (didanai chain mitra):
- **Polygon PoS (Mei 2021):** **$200 juta MATIC** → TVL **>$1 miliar** dalam 3 bulan.
- **Avalanche Rush (Okt 2021):** **$20 juta AVAX** → TVL Avalanche **>$3,3 miliar** dalam seminggu.
- **V4 Avalanche (Jul 2026):** insentif **$15 juta**. → `examples/CaseStudies/Avalanche.md` (Rush + V4 + Progmat).

**ACI (Aave Chan Initiative, 30 Nov 2022, Marc Zeller):** koordinasi tata kelola & parameter risiko harian.

**Kompetitif:** vs **Compound** (Aave menang via listing aset cepat + Flash Loans + multi-chain agresif; pinjaman
aktif Compound **$547,9 juta** vs Aave **$16,55 miliar** awal 2026); vs **Morpho/Fluid** (efisiensi P2P atas kolam
Aave → dijawab V4 modular); vs **Dolomite** (model 3-token). *(Compound/Morpho = kandidat gap dataset.)*

## 10. Narrative & Product Evolution
_ref: `docs/Meta/Narratives.md`, `docs/Patterns/Narrative.md`, `docs/Project/Roadmap.md`, `docs/Ontology/Adoption.md`_

**Narasi per fase:** FinTech/disintermediasi (2017–18) → **DeFi blue-chip & yield farming** (2020–21, aTokens/
Flash Loans, TVL = tolok ukur) → multi-chain/L2 (2021–22, Polygon/Avalanche) → **RWA & institusi** (2025–26,
Horizon) → **token produktif arus-kas riil** (2026, AWW).

**Product:** core lending → **GHO** (stablecoin, Jul 2023; dicetak vs jaminan; **100% bunga → kas DAO**) →
**Umbrella Safety Module** (5 Jun 2025; ERC-4626 terisolasi, staking aToken sebagai **first-loss**, auto-slashing
saat bad debt) → **Horizon** (27 Agu 2025; RWA berizin, jaminan **US Treasuries tokenisasi** sUSG/USTB/JAAA) →
**sGHO Savings Vault** (3 Apr 2026; ASR **4,25% APR**, 50 bps di atas Sky SSR) → **Aave App** (mobile). →
`examples/Pioneer/MakerDAO-Sky.md` (GHO vs Sky SSR).

## 11. Token Lifecycle & Price Causality
_ref: `docs/MarketBehaviour/*`, `docs/Valuation/FairValue.md`, `docs/Reasoning/Prediction.md`_

| Titik | Nilai | Kondisi |
|---|---|---|
| LEND diperdagangkan | — | 31 Des 2017 |
| **ATL** | **$26,02** | 5 Nov 2020 (awal AAVE) |
| **ATH** | **$661,69** *(alt $666,86)* | 18 Mei 2021 (leverage looping DeFi Summer) |
| Bear | <$70 | 2022–23 (Terra-UST, Celsius, deleveraging) |
| Konsolidasi | **$89–100** | pertengahan 2026 |

**Konsentrasi:** 100 dompet teratas ~**80%** pasokan (termasuk stkAAVE + Ecosystem Reserve). **MC/TVL 0,059**
(MC $1,45 mrd / TVL $24,46 mrd, Apr 2026) → **undervalued**; AWW memungkinkan **DCF** → Standard Chartered target
**$3.500 (2030)**. → `docs/Valuation/FairValue.md`.

## 12. Business Intelligence & RWA (Horizon)
_ref: `docs/Ontology/Revenue.md`, `docs/Valuation/Revenue.md`, `docs/Ontology/Metrics.md`, `docs/Valuation/TVL.md`, `docs/Success/Adoption.md`_

**TVL:** puncak **$70,1 mrd** (Sep 2025) / **$75 mrd** (2025 keseluruhan) → $55 mrd (Des 2025) → $57,33 mrd (Jan
2026) → $44,94 mrd (Feb) → $42,34 mrd (Mar) → **~$14 mrd (Mei, pasca-hack)** → $22 mrd (Jun avg). **Active loans:**
$23,25 mrd (Jan) → $16,55 mrd (Mar) → $9,4 mrd (Jun avg). Kumulatif: deposit **$3,46 triliun**, pinjaman **$1 triliun**.

**DAO revenue:** 2022 **$5,22 juta** → 2023 **$22,54 juta** (+331,54%) → 2024 **$90,19 juta** (+300,15%) → 2025
**$141,8 juta** (+57,25%) → **YTD 2026 $333 juta**. **GHO supply:** $467,53 juta (Feb) → $584 juta (Mei) → $547,9
juta (Jun); GHO net revenue >$22 juta.

**Horizon (RWA institusional):** net deposits $250 juta (Okt 2025) → $600 juta (Jan) → **$1 miliar (Feb 2026)**;
active loans $500 juta (Jun). **V4 Ethereum deposits:** $4,5 juta (Mar) → $170,5 juta (Jun avg) → **>$200 juta**
(akhir Jun). → `examples/CaseStudies/Avalanche.md` (V4 Avalanche + **Progmat ¥452 mrd**, RWA thread bersama).

## 13. POV Success-Matrix (§15)
_ref: `docs/Success/*`, `docs/Reasoning/Explainability.md`, `docs/Reasoning/Confidence.md`_

| POV | Verdict | Alasan | Evidence |
|-----|---------|--------|----------|
| **Founder** (`Success/Founder.md`) | ✅ Sukses | ETHLend gagal → pilar likuiditas DeFi global; kekayaan Kulechov ~$300–500 juta | HIGH |
| **VC** (`Success/VC.md`) | ✅ Sukses | Kontrol tata kelola besar (~25–35%, 2023) + apresiasi token masif | HIGH |
| **Retail** (`Success/Community.md`) | ⚠️ Campuran | Akses pinjaman transparan; tapi likuidasi instan (penalti 5–10%) akibat salah paham LTV | MEDIUM |
| **Community** (`Success/Community.md`) | ⚠️ Campuran | DAO paling aktif; tapi **governance drift** (AWW Feb–Mar 2026, whale/founder) → **ACI mundur** | HIGH |
| **Developer** (`Success/Developer.md`) | ✅ Sukses | Pustaka open-source matang; tapi kepergian **BGD Labs** (Apr 2026) merugikan jangka pendek | HIGH |
| **Institution** (`Success/Adoption.md`) | ✅ Sukses | Horizon → pembiayaan stablecoin berjaminan US Treasuries tokenisasi | HIGH |
| **Validator** (`Success/Protocol.md`) | ✅ Sukses | Volume on-chain Aave menaikkan gas fee validator EVM | HIGH |
| **Builder** (`Success/Ecosystem.md`) | ⚠️ Campuran | Integrasi yield mudah; tapi **rsETH hack** buktikan risiko sistemik bridge pihak ketiga | HIGH |

**Takeaway:** menang di founder/VC/institution/validator/developer; **campuran** retail/community/builder
(likuidasi, governance drift, risiko komposabilitas). Kegagalan-nyaris-fatal (rsETH) dipulihkan penuh (§15).

## 14. Historical Timeline
_ref: `docs/TokenLifecycle/*`_

- **1 Mei 2017** — ETHLend (London). **25 Nov 2017** — ICO LEND $17,86 juta. **Sep 2018** — rebrand Aave.
- **8 Jan 2020** — **V1 mainnet** (pool, aTokens, Flash Loans). **9 Jul 2020** — Series A (ParaFi). **Okt 2020** — migrasi LEND→AAVE (100:1). **12 Okt 2020** — Series B. **16 Des 2020** — V2.
- **14 Apr 2021** — V2 Polygon ($200 juta MATIC). **18 Mei 2021** — **ATH $661,69**. **4 Okt 2021** — V2 Avalanche (Rush $20 juta). **Mar 2022** — V3 (6 L2). **30 Nov 2022** — ACI (Marc Zeller).
- **27 Jan 2023** — V3 Ethereum. **15 Jul 2023** — **GHO**. **5 Jun 2025** — **Umbrella**. **27 Agu 2025** — **Horizon (RWA)**. **Des 2025** — **SEC tutup investigasi (tanpa denda)**.
- **16 Feb 2026** — Grayscale ajukan konversi ETF. **2 Mar 2026** — AWW temp check 52,58%. **30 Mar 2026** — **V4 Ethereum (Hub-and-Spoke)**. **3 Apr 2026** — sGHO. **13 Apr 2026** — **AWW lolos ~75%**.
- **18 Apr 2026** — **rsETH hack $292 juta** (LayerZero 1-of-1 DVN → mint rsETH → pinjam $190 juta WETH). **6 Mei 2026** — likuidasi paksa (106.993 rsETH pulih). **15 Jul 2026** — **V4 Avalanche** ($15 juta + Progmat ¥452 mrd).

## 15. rsETH Hack & Recovery, Current Status, Lessons Learned
_ref: `docs/Ontology/Security.md`, `docs/Patterns/Failure.md`, `docs/Patterns/Recovery.md`, `docs/TokenLifecycle/Maturity.md`_

### rsETH Kelp DAO exploit *(causal core — security)*
**18 Apr 2026:** verifikasi **1-of-1 DVN** pada jembatan **LayerZero** (Kelp DAO, Unichain↔Ethereum) →
**pencetakan rsETH tanpa jaminan** → didepositkan ke Aave → **pinjam $190 juta WETH** → pembekuan pasar darurat.
**Recovery:** **DeFi United** (koalisi Lido, Ethena, Mantle) himpun **>$318 juta**; likuidasi paksa penyerang
(**106.993 rsETH pulih**, 6 Mei); **30.765 ETH** sitaan dari Arbitrum DAO ditransfer ke Aave; LTV WETH normal.
**Tanpa kerugian depositor jangka panjang.** → `examples/Pioneer/LayerZero.md`, `EigenLayer.md`/`Lido.md` (LRT thread).

**Status (pertengahan 2026):** pemulihan kuat + ekspansi V4; YTD revenue **$333 juta**; buyback $50 juta/th; neraca
DAO paling likuid sepanjang sejarah.

**Pelajaran:** (1) **Composability thresholds** — jaminan token-jembatan wajib LTV 0% default sebelum verifikasi
berlapis; (2) **Automated loss protection** (Umbrella) > Safety Module lama berbasis harga token asli; (3)
**Enforceable value capture** (buyback AWW) = penangkal devaluasi + reputasi DCF.

## 16. Knowledge Extraction — Patterns & Lessons (§18–19)
_ref: `docs/Patterns/*`, `docs/Reasoning/*`, `docs/Schema/PatternSchema.md`_

1. **Governance-to-Cashflow Transition** *(crown value-accrual — 3rd dataset instance)* — *ketidakpuasan token
   tata kelola murni → utilitas turun (emisi) → fee-switch 100% ke DAO → buyback otomatis → pasokan menyusut →
   valuasi DCF fundamental.* → `docs/Valuation/FairValue.md`; mirror `examples/CaseStudies/dYdX.md` §16, `Cosmos.md` §19.
2. **LST/LRT Composability Vulnerability** — *terima jaminan restaking rantai sekunder → ketergantungan bridge →
   eksploit verifikator tunggal → mint sintetis tanpa jaminan → pinjam aset riil → pembekuan darurat Guardian.*
   → `docs/Ontology/Security.md`, `docs/Patterns/Failure.md`.
3. **DeFi Coalition Solvency Rescue** — *bad debt besar → risiko sistemik → koalisi protokol (DeFi United) →
   dana talangan dari penerbit jaminan (Lido/Ethena) → likuidasi paksa via payload → solvabilitas pulih tanpa
   kerugian ritel.* → `docs/Patterns/Recovery.md`.
4. **Automated On-Chain Insurance (Umbrella)** — brankas ERC-4626 aToken + auto-slashing > Safety Module berbasis
   token asli volatil. → `docs/Ontology/Security.md`, `docs/Ontology/Incentives.md`.
5. **Chain-Subsidized Liquidity Mining** — insentif didanai chain mitra (Polygon $200 juta, Avalanche $20 juta) →
   lonjakan TVL cepat. → `docs/Patterns/Liquidity.md`, `docs/Success/Airdrop.md`.

### Entitas & relasi ontologi (kandidat Knowledge Graph)
_ref: `docs/Schema/KnowledgeGraph.md`, `docs/Schema/EntityRelationship.md`_
- `[Stani_Kulechov] —founded→ [ETHLend]` · `[ETHLend] —rebrandedTo→ [Aave]` · `[Aave] —developed→ [Aave_V4]`
- `[Aave_V4] —implements→ [Hub-and-Spoke]` · `[Core_Liquidity_Hub] —aggregates→ [Global_Liquidity]` · `[Spokes] —isolate→ [Collateral_Risk]`
- `[Umbrella] —utilizes→ [aToken_Staking]` · `[Aave_Will_Win] —redirects→ [100%_Product_Revenue]`
- `[Kelp_rsETH_Bridge] —used→ [1-of-1_DVN]` · `—enabled→ [rsETH_Exploit]` · `—generated→ [Aave_Bad_Debt]` · `[DeFi_United] —collateralized→ [Recovery]`

## 17. Transferable Intelligence (§20) — rule candidates untuk protokol pasar uang baru
_ref: `docs/Reasoning/AnalogEngine.md`, `docs/Reasoning/Weighting.md`, `docs/Reasoning/Confidence.md`_

- **R1 — MC/TVL DeFi Rule:** pasar uang matang dengan pangsa **>40%** + **MC/TVL <0,10** + komitmen aliran dana
  riil ke kas DAO → klasifikasikan **undervalued**. *(Aave 0,059.)*
- **R2 — Bridge Verification Filter:** deteksi jaminan lintas-rantai; jika verifikasi **<3-of-5 multisig** atau
  **1-of-1 DVN** → wajib **LTV 0%** (cegah bad debt instan). *(Pelajaran rsETH.)*
- **R3 — Insurance Decentralization:** asuransi keselamatan **dilarang** bergantung pada harga token asli;
  gunakan brankas **ERC-4626 aToken** + slashing otomatis.
- **Khusus-Aave:** **suku bunga GHO diskresioner** (diatur komite untuk bersaing dengan Sky SSR), bukan algoritma
  murni → pantau penyesuaian tata kelola.

## 18. Open Questions (§21)
_Research gap — belum tervalidasi._
1. Bagaimana **Horizon** memitigasi benturan **MiCA (EU) vs SEC (AS)** saat jaminan RWA lintas yurisdiksi? (evidence: MEDIUM)
2. Apakah pengalihan **100% pendapatan** produk (AWW) **enforceable** secara hukum atas Avara jika sengketa? (MEDIUM)
3. Bisakah Spoke modular bertahan di rantai **non-EVM** (Solana) tanpa race condition sinkronisasi Hub? (LOW)

## 19. Evidence Level — kesimpulan kunci (§22)
_ref: `docs/Reasoning/Confidence.md`, `docs/Research/Verification.md`_

| Kesimpulan | Evidence | Alasan |
|---|---|---|
| Kinerja finansial (revenue 2022→2025 $5,22→141,8 juta; YTD $333 juta) | **HIGH** | Ledger on-chain Token Terminal + laporan tata kelola resmi |
| rsETH hack $292 juta + pemulihan | **HIGH** | Post-mortem Metrika/Blockonomi + draf denda forum tata kelola |
| Penutupan investigasi SEC (Des 2025) | **MEDIUM** | Dilaporkan Bloomberg; dokumen formal bisa dibuka ulang rezim baru |
| Target harga $3.500 (2030, Standard Chartered) | **LOW** | Asumsi pertumbuhan DeFi 37× tanpa risiko black-swan makro |

## 20. Related Framework Definitions
- **Ontology:** `docs/Ontology/Identity.md`, `Team.md`, `Funding.md`, `Tokenomics.md`, `Incentives.md`,
  `Governance.md`, `Security.md`, `Risks.md`, `Technology.md`, `Infrastructure.md`, `Ecosystem.md`, `Community.md`, `Revenue.md`, `Metrics.md`, `Adoption.md`, `Innovation.md`
- **Innovation:** `docs/Innovation/FirstMover.md`, `CompetitiveMoat.md`, `ProductMarketFit.md`, `Execution.md`
- **Patterns:** `docs/Patterns/Flywheel.md`, `Failure.md`, `Recovery.md`, `Liquidity.md`, `Narrative.md`
- **Valuation/Market:** `docs/Valuation/FairValue.md`, `Revenue.md`, `Competitors.md`, `TVL.md`; `docs/MarketBehaviour/UnlockImpact.md`; `docs/Meta/Narratives.md`, `MarketCycles.md`
- **Reasoning:** `docs/Reasoning/Prediction.md`, `AnalogEngine.md`, `Confidence.md`, `Weighting.md`
- **Success:** `docs/Success/*` · **Schema:** `docs/Schema/KnowledgeGraph.md`, `EntityRelationship.md`, `PatternSchema.md`
- **Cross-project analogs:** `examples/CaseStudies/dYdX.md` & `Cosmos.md` (**same value-accrual pattern + fix**),
  `Avalanche.md` (Rush + V4 + Progmat RWA), `examples/Pioneer/MakerDAO-Sky.md` (GHO vs Sky SSR), `examples/Pioneer/LayerZero.md`
  (rsETH bridge), `examples/Pioneer/EigenLayer.md` & `Lido.md` (LRT/restaking + DeFi United), `examples/Pioneer/Uniswap.md` (AMM).
  **Supersedes:** `examples/Pioneer/Aave.md` (Summary). **Gap candidates:** Compound, Morpho.

## 21. Sources
_Deep Research provenance (Gemini). Laporan sumber mengutip **89 referensi**; sumber primer/kunci di bawah._

- Aavenomics — GitHub — https://github.com/aave/aavenomics
- From ETHLend to Aave V4: Evolution of the Leading DeFi Lending Protocol — Gate Learn — https://www.gate.com/learn/articles/from-ethlend-to-aave-v4-the-building-plan-of-the-leading-lending-ecosystem/3115
- Aave V4: How the Hub-and-Spoke Architecture Reshapes DeFi Lending — Gate — https://www.gate.com/blog/aave-v4-how-the-hub-spoke-architecture-reshapes-defi-lending-infrastructure
- Anatomy of the Aave v4 contracts — Jean Cvllr (Medium) — https://jeancvllr.medium.com/anatomy-of-the-aave-v4-contracts-364fa3189d04
- The Kelp-Aave Incident post-mortem — Metrika — https://www.metrika.co/blog/post-mortem-kelp-aave
- The KelpDAO rsETH Exploit: $292M from a 1-of-1 Bridge — DeFi Prime — https://defiprime.com/kelpdao-rseth-exploit
- Aave Reports $907M Revenue in 2025, $333M YTD 2026 (Standard Chartered) — KuCoin — https://www.kucoin.com/news/flash/aave-reports-907m-revenue-in-2025-333m-ytd-2026-as-standard-chartered-initiates-coverage
- [ARFC] Aave Will Win Framework — Aave Governance — https://governance.aave.com/t/arfc-aave-will-win-framework/24352
- Update on Aave's governance crisis (enforceability) — 21Shares — https://www.21shares.com/en-eu/insights/update-on-aaves-governance-crisis-alignment-is-on-the-table-enforceability-is-not-yet
- What is Umbrella, Aave's new security module — Oak Research — https://oakresearch.io/en/analyses/innovations/what-is-umbrella-new-product-from-aave
- How Aave Horizon is Built to Support Institutions — Aave — https://aave.com/blog/horizon-built-for-institutions
- Aave Surpasses $1T in DeFi Lending Milestone — CryptoRank — https://cryptorank.io/news/feed/dd3af-aave-surpasses-1t-in-defi-lending-milestone
- Standard Chartered Predicts 50x Upside for AAVE ($3,500 by 2030) — CryptoRank — https://cryptorank.io/news/feed/f3dfe-standard-chartered-aave-price-prediction-2030
- ETHLend LEND Token Raises Over $10M in 30 Min — Finance Magnates — https://www.financemagnates.com/thought-leadership/ethlends-lend-token-raises-10-million-30-minutes/

_(Full 89-source bibliography retained in the original Deep Research report + archived at
`doc_backup/deep/Aave_2026-07_gemini.md`.)_
