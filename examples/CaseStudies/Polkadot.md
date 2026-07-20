# Polkadot — Deep Case Study

**CIF Dataset — Deep Dossier · Tier: Deep (anchor project)**
**Source:** Deep Research (Gemini) — *"Intelijen Komprehensif Polkadot: Analisis Historis, Evolusi Arsitektur
2.0, dan Rekonstruksi Tokenomics"*.
**Pipeline position:** Applications layer — an anchor artifact structured against the full `docs/` ontology.
Serves as the **Layer-0 heterogeneous-sharding + shared-security** analog — contrast Cosmos (sovereign
app-chains), Avalanche (Subnet double-capex), Ethereum (rollup-centric), and the exchange/monolithic L1s.
**Raw source archived:** `doc_backup/deep/Polkadot_2026-07_gemini.docx` (+ `.md` text extraction).
**Input note:** first source authored in the CIF no-table markdown contract (Label: Value) — extraction lossless.

> Knowledge artifact (real curated data), not a documentation container. This is a **deep dossier**: it
> preserves *causality* (why events happened), which is the raw material for prediction. Conforms to
> `templates/CaseStudyTemplate.md`.

---

## 1. Identity
_ref: `docs/Ontology/Identity.md`_

- **Project:** Polkadot (token: DOT).
- **Category:** Layer-0 meta-protokol multi-chain heterogen — koordinasi parachain di bawah **shared security**.
- **Era:** 2016 (whitepaper) – sekarang (pertengahan 2026). **Genesis:** 26 Mei 2020 15:36:21 UTC.
- **Founders:** **Dr. Gavin Wood** (eks-CTO Ethereum, penulis Yellow Paper, pencipta Solidity), **Robert
  Habermeier**, **Peter Czaban**. **Web3 Foundation** (Zug, Swiss, 2017) + **Parity Technologies** (2015, d/h
  Ethcore; CEO awal **Jutta Steiner**).
- **Konsensus/stack:** **NPoS (Nominated Proof-of-Stake)**; **Substrate SDK** (Rust).
- **Snapshot (24 Mei 2026):** market cap **$2.172.113.802** (peringkat **#43** global); pasokan beredar
  **1.685.164.169 DOT**; max supply **2,1 miliar DOT**.
- **Innovation archetype:** **First Mover** dalam **heterogeneous sharding + shared security** & forkless
  runtime upgrades. → `docs/Innovation/FirstMover.md`, `docs/Innovation/CategoryCreator.md`.

## 2. Classification
_ref: `docs/Ontology/Classification.md`, `docs/Taxonomy/Sectors.md`, `docs/Taxonomy/Technologies.md`_

Layer-0 · Relay Chain (konsensus) terpisah dari parachains (eksekusi) · **XCM/XCMP** interop trustless ·
runtime **WebAssembly** on-chain (forkless upgrade) · roadmap **Agile Coretime** (blockspace as-a-service) →
**JAM** (RISC-V/PolkaVM). Max supply capped **2,1 miliar DOT** (sejak Mar 2026).

## 3. Pre-Conditions — Fragmentasi & Biaya Bootstrapping Validator (2016)
_Konteks: mengapa Polkadot harus ada._
_ref: `docs/Meta/Narratives.md`, `docs/Ontology/Security.md`_

Akhir 2016: Ethereum monolitik mulai macet (gas melonjak, latensi). Masalah kritis: **fragmentasi** — tiap
chain jadi pulau terisolasi, dihubungkan **bridge tersentralisasi** = **single point of failure** (ratusan juta
dolar hilang). Narasi bergeser ke **modular / app-chains**, tetapi **hambatan modal & teknis** untuk merekrut
& mempertahankan set validator sendiri sangat tinggi → chain baru rentan **serangan 51%**. Kebutuhan: **shared
security** otonom & trustless. Itulah tesis Polkadot sebagai **meta-protokol Layer-0**.

## 4. Origin & Team — Genealogi dari Ethereum
_ref: `docs/Ontology/Team.md`, `docs/Project/Philosophy.md`, `docs/Ontology/Governance.md`_

**Dr. Gavin Wood** (co-founder & CTO pertama Ethereum) **keluar pertengahan 2016** saat merancang sharding
Ethereum, menemukan konsep koordinasi blockchain heterogen → **Polkadot Whitepaper (Oktober 2016)**. *(Ini
sisi lain dari perpecahan Ethereum — bandingkan Hoskinson→Cardano; dua anchor lahir dari keluarnya co-founder
Ethereum. Lihat `examples/CaseStudies/Ethereum.md` §4, `Cardano.md` §4.)*

**Struktur dua-entitas:** **Web3 Foundation** (Zug, 2017; nirlaba — distribusi token, riset, ekosistem) +
**Parity Technologies** (2015, d/h Ethcore; Wood & **Jutta Steiner**, eks-Head of Security Ethereum) yang
membangun **Substrate** (framework blockchain modular Rust). Pendiri lain: **Robert Habermeier** (Thiel Fellow,
Rust), **Peter Czaban** (CTO W3F, Oxford). *Struktur nirlaba + rigor akademis = keandalan tinggi tapi eksekusi
lambat (tema berulang, §18).*

## 5. Innovation Analysis — Shared Security, Forkless Upgrade, XCM
_ref: `docs/Ontology/Innovation.md`, `docs/Innovation/FirstMover.md`, `docs/Innovation/CompetitiveMoat.md`, `docs/Ontology/Technology.md`_

1. **Heterogeneous sharding + shared security** — parachains **mewarisi** keamanan ekonomi Relay Chain (miliaran
   DOT ter-stake) tanpa merekrut validator sendiri. Kontras **Cosmos** (kedaulatan validator penuh → rentan
   51%). → §9.
2. **Forkless runtime upgrades** — logika transisi state disimpan sebagai **bytecode Wasm on-chain**; upgrade &
   patch via voting tata kelola, **tanpa hard fork** yang memecah komunitas. *(Standar industri baru.)*
3. **XCM / XCMP** — bahasa pesan lintas-konsensus ekspresif → instruksi komputasi antar-rantai langsung, tanpa
   bridge pihak ketiga.

*Pelajaran kausal:* memusatkan validasi di Relay Chain memberi keamanan instan sejak blok pertama (moat), tetapi
**collator parachain** yang tak menanggung konsensus juga jadi dasar efisiensi modal vs Avalanche Subnet (§9).

## 6. Technology Evolution — Peluncuran Bertahap → Polkadot 2.0 → JAM
_ref: `docs/Ontology/Technology.md`, `docs/TokenLifecycle/*`, `docs/Ontology/Infrastructure.md`_

- **PoA Genesis** — 26 Mei 2020 (6 validator W3F; hanya klaim DOT & registrasi).
- **NPoS** — 18 Jun 2020 (blok #325,148; `Staking.ForceNewEra` via Sudo) → validator komunitas.
- **Sudo dihapus** — 20 Jul 2020 → kendali penuh ke pemegang DOT (tata kelola on-chain).
- **Transfer DOT (TGE)** — 18 Agu 2020 (blok #1,205,128, 16:39 UTC).
- **Redenominasi 1:100** — 21 Agu 2020 (blok #1,248,328; 12→10 desimal; saldo ×100, harga ÷100).
- **Parachain auctions** — 11 Nov 2021; XCM Des 2021.
- **Asynchronous Backing** — Mei 2024: block time parachain **12→6 detik**, kapasitas parablock ×4, TPS ×8–10.
- **Agile Coretime + Elastic Scaling** — Okt 2025 (SDK 2509) → akhiri lelang slot permanen.
- **Great Hub Migration** — Nov 2025: pindahkan **1,6 miliar DOT** (saldo/staking/governance) dari Relay Chain
  ke **Asset Hub** dalam **8,5 jam**.
- **JAM (Polkadot 3.0)** — target mainnet Q3–Q4 2026: **Join-Accumulate Machine**, komputasi paralel global
  permissionless via **RISC-V/PolkaVM** (~150 miliar gas/detik), menggantikan Relay Chain.

## 7. Funding Intelligence — ICO & Pembekuan Parity
_ref: `docs/Ontology/Funding.md`, `docs/Ontology/Tokenomics.md`, `docs/Ontology/Security.md`, `docs/TokenLifecycle/TGE.md`_

**ICO 27 Okt 2017** (Spend-All Second Price **Dutch Auction**): **$145 juta** (485,331 ETH). Harga **$28,8/old
DOT** = **$0,288/new DOT**; valuasi pra-peluncuran $288 juta. Struktur: **Private Sale 1 $80 juta** (27,6%) +
**Public ICO $65 juta** (22,4%). Investor: 1confirmation, Polychain, Boost VC, Pantera.

### Parity multi-sig freeze *(causal event — cross-anchor)*
**6 Nov 2017** (10 hari pasca-ICO): pengguna GitHub **devops199** memicu `selfdestruct` pada **WalletLibrary**
Parity yang tak terinisialisasi → **513,774 ETH** beku permanen di 587 dompet; **~$98 juta dana ICO Polkadot
terkunci**. *(Ini peristiwa yang SAMA dengan `examples/CaseStudies/Ethereum.md` §7 "Parity Multi-Sig Freeze" —
di sana dilihat dari sisi tata kelola Ethereum & EIP-999; di sini dari sisi korban dana. Analog silang kuat.)*

**Putaran lanjutan:**
- **Private Sale 2** (27 Jun 2019): **$60 juta** *(INKONSISTENSI: sebagian sumber $43 juta — evidence LOW)*;
  500,000 old DOT (= 50 juta new DOT, 5%); $1,20/new DOT; valuasi penjualan **$1,2 miliar**; investor **Fundamental Labs**.
- **Private Sale 3** (27 Jul 2020): **$42,76 juta** *(sebagian $43–47 juta — LOW)*; 340,000 old DOT (= 34 juta
  new DOT, 3,4%); $1,25/new DOT; valuasi penjualan **$1,25 miliar**; lock 5 bulan; investor **Continue Capital**.
- **Strategic** (2022): $4 juta.
- **INKONSISTENSI total dana:** Crunchbase/Cryptorank **$327,13 juta** (12 putaran) vs Alpha Growth **$665,4
  juta** — tanpa audit kas resmi W3F. **Evidence: LOW.** → `docs/Research/Verification.md`.

## 8. Tokenomics — Inflasi Terbuka → Capped 2,1 M + DAP
_ref: `docs/Ontology/Tokenomics.md`, `docs/Ontology/Incentives.md`, `docs/MarketBehaviour/UnlockImpact.md`_

**Tiga rezim moneter:**
1. **Inflasi terbuka (2020–Nov 2024):** uncapped, target **~10%/th**; sisa deviasi rasio staking → Treasury.
2. **Emisi tetap (Nov 2024–Mar 2026):** **120 juta DOT/th** (85% staker, 15% Treasury; Treasury Burn berkala).
3. **Capped + Pi Schedule (sejak 14 Mar 2026):** max supply **2,1 miliar DOT**; emisi dipotong **53,6%** instan
   (120 → **55 juta DOT/th**); turun **13,14% tiap 2 tahun**. **Dynamic Allocation Pool (DAP):** semua emisi +
   fee + slashing + pendapatan Coretime masuk ke satu kolam → dialokasikan fleksibel via **OpenGov**.

**Alokasi genesis:** Sale 2017 **50%** (PS1 27,6% + ICO 22,4%) · PS2 (2019) **5%** · PS3 (2020) **3,4%** ·
W3F future reserve **11,6%** · W3F operations **30%**.

**Kebijakan staking (sejak Jul 2026, Ref #1909/#1910):** validator min self-stake **10.000 DOT**, komisi
**0%**, optimal **30.000 DOT (~30% APY)**, cap **100.000 DOT (~9% APY)**, kompensasi ops **$2.000/bln** stablecoin
dari DAP. Nominator: **unbonding 24–48 jam** (dari 28 hari), **slashing 0%** (dipindah ke self-stake validator).

## 9. Airdrop & Incentive — Kusama, Crowdloans, lcDOT
_ref: `docs/Patterns/Points.md`, `docs/Success/Airdrop.md`, `docs/Patterns/Liquidity.md`, `docs/Ontology/Incentives.md`_

Polkadot **menolak airdrop spekulatif**. Satu-satunya distribusi massal: **Kusama (KSM) 1:1** ke pemegang DOT
ICO 2017 (Agu 2019) — canary network bernilai riil. Insentif modal terstruktur:
- **Crowdloans parachain:** proyek menawarkan token sendiri (ACA/Acala, GLMR/Moonbeam, ASTR/Astar) untuk memikat
  DOT; mengunci **131,37 juta DOT** — tapi **opportunity cost besar** (lock 2 tahun tanpa yield DOT).
- **lcDOT (Acala):** derivatif liquid crowdloan 1:1 → bisa jadi kolateral/diperdagangkan sejak hari-1.
- **Treasury DeFi:** mis. akuisisi **Hydration 8 juta DOT** (8 kuartal) untuk insentif likuiditas Omnipool +
  Liquid Staking vDOT (Bifrost).

## 10. Community & Narrative Intelligence
_ref: `docs/Ontology/Community.md`, `docs/Meta/Narratives.md`, `docs/Patterns/Narrative.md`, `docs/Meta/MarketCycles.md`_

**Komunitas:** Web3 Foundation Grants (bangun infrastruktur dasar); **Polkadot Blockchain Academy** (kurikulum
dev terakreditasi); **Kusama** canary. **Kegagalan retensi ritel:** Polkadot-JS kompleks, **existential deposit**
membingungkan, NPoS awal menuntut kurasi **16 validator** — menjauhkan Polkadot dari gelombang DeFi/meme yang
direbut **Solana** (1-klik). → `examples/CaseStudies/Solana.md`.

**Peran narasi per fase:**
| Fase | Narasi | Peran |
|---|---|---|
| 2020–21 | Interop L0 / "monolithic killer" (lelang slot, DOT = blockspace langka) | **Pencipta** |
| 2022–24 | Kehancuran likuiditas / ecosystem winter (crowdloan lock 96 mgg; tergeser ETH L2) | **Korban narasi** |
| 2024–25 | **Polkadot Cloud** / agile blockspace (DePIN peaq, Frequency) | **Re-invensi** |
| 2026 | **Global singleton supercomputer / JAM / native EVM** (RISC-V) | **Pencipta (spekulatif)** |

## 11. Competitive Landscape
_ref: `docs/Valuation/Competitors.md`, `docs/Valuation/ComparableProjects.md`, `docs/Meta/MarketCycles.md`_

- **Cosmos** — kompetitor terdekat; sovereign app-chains (Cosmos SDK/Go), time-to-market cepat, tetapi **tanpa
  shared security** → rentan 51%. Polkadot mewarisi keamanan Relay Chain sejak blok-1.
- **Avalanche** — Snowball + Subnet; finalitas cepat, tapi **validator Subnet double-capex** (stake AVAX +
  infra mandiri) vs **collator** Polkadot yang hanya kumpulkan data. → `examples/CaseStudies/Avalanche.md` §5.
- **Ethereum L2 (Rollups)** — **menang** modal, MetaMask, integrasi ritel. Polkadot unggul keanggunan
  teknis/forkless, **kalah** capital formation, volume DeFi, retensi pengguna. → `examples/CaseStudies/Ethereum.md`.

*(Cosmos belum ada di dataset — kandidat gap.)*

## 12. Product Evolution — 1.0 Slot Lease → 2.0 Agile Coretime
_ref: `docs/Project/Roadmap.md`, `docs/Ontology/Infrastructure.md`, `docs/Innovation/ProductMarketFit.md`_

- **Polkadot 1.0 (Candle Auctions & Slot Leases):** sewa slot ≤96 minggu via **candle auction**; proyek harus
  mengunci jutaan DOT lewat **crowdloans** → **opportunity cost merusak**.
- **Polkadot 2.0 (Agile Coretime):** lelang slot dihentikan permanen (akhir 2025); blockspace = utilitas cloud,
  didistribusikan sebagai **NFT Coretime 28-hari** (bisa dibagi/gabung/perdagangkan).
- **System Chains / Asset Hub:** aktivitas user/saldo/staking pindah dari Relay Chain (akhir 2025) → biaya **100×
  lebih murah**; Relay Chain fokus validasi.

## 13. Token Lifecycle & Price Causality
_ref: `docs/MarketBehaviour/*`, `docs/Valuation/FairValue.md`, `docs/Reasoning/Prediction.md`_

| Titik | Nilai | Kondisi |
|---|---|---|
| Listing perdana (old DOT) | ~$88,45 | TGE, Jul 2020 (PS3 close 27 Jul) |
| Pasca-redenominasi 1:100 | ~$370 → ~$3,70 | 21 Agu 2020 (memicu beli ritel masif) |
| **ATH** | **$54,98** | 4 Nov 2021 (kelangkaan staking + crowdloan batch-1) |
| Unlock pressure | 113 juta DOT crowdloan unlock | 24 Okt 2023 (tekanan jual struktural) |
| **ATL** | **$1,15** | 15 Apr 2026 |
| ETF exit | Bitwise 10 hapus DOT | 9 Jul 2026 (digeser Hyperliquid) → jual institusi |

**Fair value:** **overvalued** dari revenue/DAU minim; **undervalued** dari hak suara atas Treasury multi-juta
+ opsi arsitektur JAM. → `docs/Valuation/FairValue.md`, `docs/MarketBehaviour/UnlockImpact.md`.

## 14. Business Intelligence
_ref: `docs/Ontology/Revenue.md`, `docs/Ontology/Metrics.md`, `docs/Valuation/TVL.md`, `docs/Ontology/Adoption.md`_

**Metrik jaringan (TTM 2025):** **588,57 juta tx** · **20,37 juta akun** terdaftar · **11,96 juta pengguna
aktif** · **519.700 pesan XCM** · crowdloans kumulatif **131,37 juta DOT**.
**Jaringan (Mei 2026):** **600 validator**, **205 nomination pools**. **DeFi TVL $103 juta** (didominasi
**Hydration $72,25 juta**; Bifrost $13,33 juta). **Stablecoin (Des 2025):** USDC **$182,45 juta**, USDT **$37
juta** lintas parachain.
**Treasury (Q4 2025):** portofolio **$57,8 juta** (32 juta DOT); kas bebas 23 juta DOT ($42 juta); USDT $4,2
juta; USDC $2,1 juta.
*Pusat aktivitas non-DeFi:* **Frequency** (sosial), **Mythos** (gaming). *Kesenjangan: keamanan kuat vs adopsi
komersial rendah.*

## 15. POV Success-Matrix (§15)
_ref: `docs/Success/*`, `docs/Reasoning/Explainability.md`, `docs/Reasoning/Confidence.md`_

Verdict per point-of-view + evidence (8 POV; sumber sudah memisahkan eksplisit):

| POV | Verdict | Alasan | Evidence |
|-----|---------|--------|----------|
| **Founder** (`Success/Founder.md`) | ✅ Sukses | Visi sharding heterogen 2016 terwujud tanpa hambatan liveness; Agile Coretime + JAM menyempurnakan L0 | HIGH |
| **VC** (`Success/VC.md`) | ⚠️ Campuran | ROI besar bagi PS1/ICO di puncak 2021; tapi VC yang kunci DOT di crowdloan rugi berat selama lock 2 tahun | HIGH |
| **Retail** (`Success/Community.md`) | ❌ Gagal | Dilusi inflasi ~10% era awal; harga jatuh $54,98 → $1,15 menghancurkan portofolio ritel | HIGH |
| **Community** (`Success/Community.md`) | ⚠️ Campuran | OpenGov mentransfer kendali penuh ke token holder; tapi **skandal $37 juta** pemasaran influencer → polarisasi | HIGH |
| **Developer** (`Success/Developer.md`) | ✅ Sukses | Substrate SDK (Rust) diakui terbaik; palet **Revive** (2026) memudahkan migrasi Solidity native | HIGH |
| **Institution** (`Success/Adoption.md`) | ❌ Gagal | Kompleksitas + unbonding 28-hari + fragmentasi likuiditas; **dihapus dari Bitwise 10** | HIGH |
| **Validator** (`Success/Protocol.md`) | ✅ Sukses | Ekonomi operasional stabil di NPoS; reformasi 2026 memindah slashing ke self-stake → tarik delegasi | HIGH |
| **Builder** (`Success/Ecosystem.md`) | ⚠️ Campuran | Shared security kokoh; tapi rigiditas lelang slot (lock modal 2 tahun) menghabiskan runway sebelum adopsi | HIGH |

**Takeaway:** Polkadot **menang di founder/developer/validator** (keanggunan teknis), **gagal di retail/
institution** (harga & likuiditas), **campuran di VC/community/builder** — profil "engineering wins, market
loses", persis pola time-to-market vs rigor (§18). Mirip Cardano; kebalikan Solana.

## 16. Historical Timeline
_ref: `docs/TokenLifecycle/*`_

- **Pertengahan 2016** — Gavin Wood keluar Ethereum, riset sharding. **Okt 2016** — Polkadot Whitepaper.
- **Pertengahan 2017** — Web3 Foundation (Zug). **19 Jul 2017** — Parity multisig hack #1 ($30 juta ETH).
- **27 Okt 2017** — ICO $145 juta. **6 Nov 2017** — devops199 freeze 513,774 ETH ($98 juta ICO Polkadot terkunci).
- **27 Jun 2019** — Private Sale 2 ($60 juta). **Agu 2019** — Kusama CC1 + airdrop KSM 1:1.
- **26 Mei 2020** — genesis PoA. **18 Jun 2020** — NPoS (#325,148). **20 Jul 2020** — Sudo dihapus.
- **27 Jul 2020** — Private Sale 3 ($42,76 juta). **18 Agu 2020** — transfer DOT aktif. **21 Agu 2020** — redenominasi 1:100.
- **4 Nov 2021** — ATH $54,98. **11 Nov 2021** — lelang slot parachain pertama.
- **24 Okt 2023** — unlock 113 juta DOT crowdloan. **Mei 2024** — Async Backing (12→6 dtk).
- **Jun 2024** — laporan Treasury H1 ($87 juta belanja) → kontroversi influencer. **Jul 2024** — OpenGov tolak isi ulang kas → belanja $1 juta.
- **Sep 2024** — Agile Coretime di Kusama. **Sep 2025** — WFC-1710 (cap 2,1 M). **Okt 2025** — Agile Coretime + Elastic Scaling mainnet.
- **Nov 2025** — Great Hub Migration (1,6 M DOT, 8,5 jam). **12 Mar 2026** — DAP aktif. **14 Mar 2026** — potong emisi 53,6% (Pi Day).
- **15 Apr 2026** — ATL $1,15. **8 Jul 2026** — Ref #1909/#1910 (slashing ritel 0%, komisi 0%, unbonding 48 jam). **9 Jul 2026** — Bitwise hapus DOT.

## 17. Current Status & 18. Lessons Learned
_ref: `docs/TokenLifecycle/Maturity.md`, `docs/Patterns/Failure.md`, `docs/Patterns/Recovery.md`_

**Status (pertengahan 2026):** Polkadot 2.0 **100% terpasang** di mainnet; 600 validator; Asset Hub 100× lebih
murah; blok 6 dtk; Treasury **$57,8 juta** sehat. **Tetapi** DeFi TVL kecil **$103 juta**, peringkat cap **#43**;
**JAM melambat** akibat birokrasi pembayaran insentif W3F ke tim client independen. *"Active technology recovery",
bukan dead chain.*

**Kesalahan terbesar (antipatterns):**
1. **Time-to-market vs academic rigor** — kekompleksan Substrate/Relay Chain menunda parachain hingga akhir 2021
   → ETH L2 & Solana merebut DeFi/dev/likuiditas.
2. **Komersialisasi sumber daya kaku** — slot lease 2 tahun/crowdloan merusak runway dev (dikoreksi Agile Coretime).
3. **Hambatan likuiditas staking** — unbonding 28 hari; dikoreksi ekstrem ke 48 jam + slashing ritel 0% (2026).
4. **Demokrasi kas tanpa filter profesional** — **$37 juta** influencer tak efisien → perlu **milestone-based
   disbursement**.

**Praktik terbaik (replicate):** shared security instan; forkless upgrade (Wasm on-chain); Agile Coretime
(blockspace pay-as-you-go); reformasi retensi ritel (unbonding pendek, no-slashing).

## 19. Knowledge Extraction — Patterns & Lessons (§18–19)
_ref: `docs/Patterns/*`, `docs/Reasoning/*`, `docs/Schema/PatternSchema.md`_

1. **Capital Friction Remediation** — *sewa infrastruktur kaku & padat modal (lelang slot) → habiskan modal dev
   pra-peluncuran → aktivitas dApp rendah → protokol pindah ke blockspace fleksibel (Agile Coretime) → hambatan
   masuk turun.* → `docs/Patterns/Liquidity.md`, `docs/Innovation/ProductMarketFit.md`.
2. **Staking Friction Mitigation** — *unbonding PoS terlalu lama (28 hari) → likuiditas tertahan saat volatil →
   unbond massal & pelarian ritel → reformasi ke 48 jam + slashing dipindah ke validator → pulihkan partisipasi.*
   → `docs/Patterns/Failure.md`. *(Analog no-slashing Cardano/Avalanche.)*
3. **Direct-Governance Treasury Drain** — *akses anggaran Treasury tanpa saringan komite ahli (OpenGov) → serbuan
   proposal promosi tak akuntabel → voter tertipu metrik follower → jutaan dolar ke influencer → penolakan massal.*
   → `docs/Patterns/Ponzinomics.md` (anti-pola), `docs/Ontology/Governance.md`.
4. **Research-First → Time-to-Market Debt** — rigor akademis menaikkan keandalan, menurunkan kecepatan pasar
   (identik Cardano). → `docs/Innovation/Timing.md`.
5. **Shared-Security Inheritance** — parachain mewarisi keamanan Relay Chain sejak blok-1 (vs bootstrap sendiri).
   → `docs/Ontology/Security.md`. *(Analog restaking/economic-security EigenLayer.)*
6. **Forkless Runtime Upgrade** — Wasm on-chain → upgrade tanpa hard fork/fragmentasi. → `docs/Ontology/Technology.md`.

### Entitas & relasi ontologi (kandidat Knowledge Graph)
_ref: `docs/Schema/KnowledgeGraph.md`, `docs/Schema/EntityRelationship.md`_
- `[Gavin_Wood] —departedFrom→ [Ethereum]` · `—founded→ [Web3_Foundation]` · `[Parity] —develops→ [Substrate_SDK]`
- `[Relay_Chain] —validates→ [Parachain]` · `[Asset_Hub] —holdsBalancesFrom→ [Relay_Chain]`
- `[Agile_Coretime] —allocatesBlockspaceTo→ [Parachain]` · `—tokenizedAs→ [NFT]`
- `[Dynamic_Allocation_Pool] —absorbsRevenueFrom→ [Agile_Coretime]` · `—paysStablecoinTo→ [Validators]`
- `[JAM] —executesVia→ [PolkaVM_RISC-V]` · `[Substrate] —compilesTo→ [WebAssembly]`

## 20. Transferable Intelligence (§20) — rule candidates untuk L0/L1 baru
_ref: `docs/Reasoning/AnalogEngine.md`, `docs/Reasoning/Weighting.md`, `docs/Reasoning/Confidence.md`_

- **R1 — Staking Liquidity Rule:** PoS dengan **unbonding >14 hari** tanpa **LSD efisien** sejak awal → selalu
  kena **liquidity discount** (opportunity cost ritel terlalu tinggi).
- **R2 — Blockspace Commercialization Rule:** distribusi blockspace via **sewa slot jangka panjang padat modal**
  selalu kalah menyerap developer vs model **pay-as-you-go / on-demand** (Coretime).
- **R3 — DAO Treasury Oversight Rule:** hak tarik Treasury via voting umum **tanpa milestone + tanpa komite
  profesional** → selalu jadi sasaran **rent-seeking**.
- **Khusus-Polkadot (jangan digeneralisasi):** JANGAN nilai kesehatan pakai **TVL DeFi**; model bisnisnya sewa
  komputasi paralel → metrik valid = **Coretime sales bulanan**, **cores purchased/renewed**, konformitas klien
  ke **JAM Graypaper**.

## 21. Open Questions (§21)
_Research gap — belum tervalidasi._
1. Akankah **JAM (RISC-V/PolkaVM)** menarik developer yang sudah terikat EVM/Rust-Solana, atau justru menambah
   hambatan adopsi karena kurva belajar ekstrem? (evidence: MEDIUM)
2. Bagaimana **DAP** menjaga cadangan jika DOT terdepresiasi jangka panjang, mengingat kompensasi validator tetap
   **$2.000/bln stablecoin** bergantung likuiditas kas DAP? (LOW)
3. Bisakah **Asset Hub** mengamankan likuiditas stablecoin pasca-penutupan **Moonbeam (31 Jul 2026)** — gerbang
   utama integrasi EVM? (LOW)

## 22. Evidence Level — kesimpulan kunci (§22)
_ref: `docs/Reasoning/Confidence.md`, `docs/Research/Verification.md`_

| Kesimpulan | Evidence | Alasan |
|---|---|---|
| Transisi ke capped supply 2,1 M via Pi Schedule berjalan on-chain | **HIGH** | WFC-1710; dieksekusi 14 Mar 2026 (Pi Day); terverifikasi Subscan |
| Belanja pemasaran OpenGov H1 2024 tidak efisien (rent-seeking) | **HIGH** | Laporan Treasury: $37 juta influencer → penolakan isi ulang + bukti bot |
| Mainnet JAM terealisasi H2 2026 | **MEDIUM** | Graypaper v0.8.0 matang, tapi penundaan insentif M1 W3F bisa geser timeline |
| Total dana kumulatif $665,4 juta | **LOW** | Kontradiksi Crunchbase $327,13 juta vs Alpha Growth $665,4 juta; tanpa audit W3F |

## 23. Related Framework Definitions
- **Ontology:** `docs/Ontology/Identity.md`, `Team.md`, `Funding.md`, `Tokenomics.md`, `Incentives.md`,
  `Governance.md`, `Security.md`, `Technology.md`, `Infrastructure.md`, `Ecosystem.md`, `Community.md`,
  `Revenue.md`, `Metrics.md`, `Adoption.md`, `Innovation.md`, `Risks.md`
- **Innovation:** `docs/Innovation/FirstMover.md`, `CategoryCreator.md`, `CompetitiveMoat.md`, `Timing.md`, `ProductMarketFit.md`
- **Patterns:** `docs/Patterns/Liquidity.md`, `Failure.md`, `Recovery.md`, `Ponzinomics.md`, `Narrative.md`
- **Lifecycle:** `docs/TokenLifecycle/*` · **Market/Valuation:** `docs/MarketBehaviour/UnlockImpact.md`; `docs/Valuation/FairValue.md`, `Competitors.md`, `ComparableProjects.md`, `TVL.md`; `docs/Meta/Narratives.md`, `MarketCycles.md`
- **Reasoning:** `docs/Reasoning/Prediction.md`, `AnalogEngine.md`, `Confidence.md`, `Weighting.md`
- **Success:** `docs/Success/*` · **Schema:** `docs/Schema/KnowledgeGraph.md`, `EntityRelationship.md`, `PatternSchema.md`
- **Cross-project analogs:** `examples/CaseStudies/Ethereum.md` (Gavin Wood genealogy + **Parity freeze, peristiwa sama**),
  `examples/CaseStudies/Cardano.md` (sesama ex-Ethereum founder, research-first, no-slashing), `examples/CaseStudies/Avalanche.md`
  (shared-security vs Subnet double-capex; sama-sama vs Cosmos), `examples/CaseStudies/Solana.md` (retail-simplicity yang direbut),
  `examples/Pioneer/EigenLayer.md` (analog shared/economic security)

## 24. Sources
_Deep Research provenance (Gemini). Laporan sumber mengutip **86 referensi**; sumber primer/kunci di bawah._

- Polkadot (blockchain platform) — Wikipedia — https://en.wikipedia.org/wiki/Polkadot_(blockchain_platform)
- Polkadot (DOT) — IQ.wiki — https://iq.wiki/wiki/polkadot-dot
- Gavin Wood — IQ.wiki — https://iq.wiki/wiki/gavin-wood
- Polkadot v2 / Polkadot 2.0 — Polkadot Wiki — https://wiki.polkadot.com/general/polkadot-v2/
- Learn Agile Coretime — Polkadot Wiki — https://wiki.polkadot.com/learn/learn-agile-coretime/
- Polkadot's JAM: Redefining Blockchain Architecture with RISC-V — BlockEden.xyz — https://blockeden.xyz/blog/2026/01/16/polkadot-jam-architecture-blockchain-virtual-machine-paradigm-shift/
- The Roadmap for the Dynamic Allocation Pool (DAP) — Polkadot Forum — https://forum.polkadot.network/t/the-roadmap-for-the-dynamic-allocation-pool-dap/16511
- Polkadot to Reset Tokenomics on March 12 (supply & staking) — Bitget News — https://www.bitget.com/news/detail/12560605240453
- OpenGov Referenda 1909 and 1910 — Bitget — https://www.bitget.com/asia/news/detail/12560605474744
- Parity Hack: How it Happened and its Aftermath — Medium (Solidified) — https://medium.com/solidified/parity-hack-how-it-happened-and-its-aftermath-9bffb2105c0
- Polkadot defends $37m splurge on influencers — DL News — https://www.dlnews.com/articles/defi/polkadot-defends-millions-spent-on-marketing-as-budget-booms/
- 2025-Q4 Polkadot Treasury Report — Polkadot Forum — https://forum.polkadot.network/t/2025-q4-polkadot-treasury-report/16847
- Polkadot Roundup 2025: The Great Migration — Medium (Gavin Wood) — https://medium.com/polkadot-network/polkadot-roundup-2025-3c3c71c7e9c4
- Polkadot (DOT) — All information about Polkadot ICO — ICO Drops — https://icodrops.com/polkadot/
- Wish For Change: Polkadot acquisition of Hydration — Polkadot Forum — https://forum.polkadot.network/t/wish-for-change-polkadot-acquisition-of-hydration/12931
- Polkadot vs. Cosmos: The Complete Guide (2025) — Supra — https://supra.com/academy/polkadot-vs-cosmos/
- Polkadot vs. Avalanche — Polkadot Wiki — https://wiki.polkadot.com/learn/learn-comparisons-avalanche/

_(Full 86-source bibliography retained in the original Deep Research report + archived at
`doc_backup/deep/Polkadot_2026-07_gemini.md`.)_
