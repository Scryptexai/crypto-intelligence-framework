# Solana — Deep Case Study

**CIF Dataset — Deep Dossier · Tier: Deep (anchor project) · Merged v1+v2**
**Source:** Deep Research (Gemini), two reports merged: (v1) *"Laporan Riset Intelijen Solana: Analisis
Komprehensif Arsitektur Teknikal, Evolusi Ekosistem, Ekonomi Token, dan Dinamika Jaringan"* (22-section
contract), and (v2) *"Exhaustive Historical Investigation: Solana (SOL) Protocol Trajectory, Causal Event
Graph, and Microeconomic Dynamics"* (7-section Causal Event Graph contract — see
`docs/Protocol/Deep-Research-Brief.md` "Format v2"). v2 supplied the **explicit Decision Events**, systematic
**Context Layer**, and **Conflicting Evidence**; v1 supplied the **8-POV Success-Matrix**, funding-round
detail, SIMD policy chronology, and business partnerships that v2 did not cover. Neither report is discarded —
this is a merge-upgrade, not a replacement.
**Pipeline position:** Applications layer — an anchor artifact structured against the full `docs/` ontology,
now including `docs/Ontology/DecisionEvent.md`, `Context.md`, and `Hidden.md`.
**Raw source archived:** `doc_backup/deep/Solana_2026-07_gemini.{docx,md}` (v1, 22-section) and
`doc_backup/deep/Solana_2026-07_gemini_v2.{docx,md}` (v2, Causal Event Graph).

> Knowledge artifact (real curated data), not a documentation container. This is a **deep dossier**: it
> preserves *causality* (why events happened), which is the raw material for prediction. Conforms to
> `templates/CaseStudyTemplate.md`.

---

## 1. Identity
_ref: `docs/Ontology/Identity.md`_

- **Project:** Solana (SOL)
- **Category:** Layer 1 / High-Performance Smart-Contract Platform — monolithic, synchronously composable.
- **Era:** 2017 (konsepsi PoH) – sekarang (pertengahan 2026).
- **Founder:** Anatoly Yakovenko (eks-Qualcomm, Dropbox, Mesosphere; pendiri Alescere VoIP 2003).
- **Innovation archetype:** **First Mover** pada eksekusi transaksi paralel berbasis kronologi kriptografi
  (Proof of History); **Category Creator** untuk narasi "High-Performance monolithic L1".

## 2. Classification
_ref: `docs/Ontology/Classification.md`, `docs/Taxonomy/Sectors.md`, `docs/Taxonomy/Technologies.md`_

Layer 1 · monolitik (bukan modular/rollup-centric) · runtime paralel **Sealevel** · konsensus **Tower BFT**
di atas jam kriptografi **Proof of History** · bahasa program **Rust / sBPF** · optimasi *hardware-limit*
(CPU single-core clock tinggi, GPU sigverify, NVMe SSD).

## 3. Context Snapshot — Era & Environment Layer
_ref: `docs/Ontology/Context.md` — snapshot kondisi dunia saat Solana dikonsep & mulai dibangun (2017–2020)._

**State of Technology (2017–2020):** Pasar L1 didominasi EVM Ethereum single-threaded (~12–15 TPS); L2
(Optimistic/ZK Rollup) masih tahap teoretis/awal. Konsensus generasi ini bergantung jam jaringan tak-tersinkron
(iterative gossip messaging) → latensi tinggi, mencegah CLOB real-time & aplikasi konsumen mulus.

**Market & Macro State:** 2018–2019 = "Crypto Winter" pasca-bubble ICO 2017; likuiditas modal tahap-awal
menyusut, VC beralih dari ICO publik ke SAFT institusional privat. Awal 2020: likuiditas makro membalik arah
(kebijakan moneter ekspansif pasca-COVID) → tailwind bagi platform smart-contract baru.

**Competitor Landscape:** Ethereum dominan atas likuiditas/developer mindshare. "Ethereum Killers" (EOS,
Cardano, Algorand, Polkadot, Cosmos) mayoritas memilih DPoS-validator-kecil atau struktur appchain/shard —
tetapi shard/multi-chain merusak **komposabilitas sinkron**. Solana mengisi celah: eksekusi **monolitik
tak-di-shard** yang skalanya mengikuti kemajuan hardware, mempertahankan *global state* tunggal.

**User & Hunter Behavior:** DeFi awal 2020 mengkristal di sekitar AMM (Uniswap V1/V2) & lending
(Compound/Aave); user memprioritaskan kecepatan & biaya rendah. Distribusi token bergeser dari sale publik ke
airdrop retroaktif; **aktivitas Sybil** (wallet massal untuk farming testnet) mulai intensif — memaksa jaringan
baru merancang batasan komitmen ekonomi & distribusi berbasis hardware.

**Perbandingan arsitektural terhadap baseline ekosistem (2017–2020):**

| Dimensi | Baseline Ekosistem | Strategi Arsitektural Solana |
|---|---|---|
| Mesin eksekusi | EVM single-threaded sekuensial | **Sealevel** — eksekusi paralel |
| Organisasi status | Sharded execution / fragmentasi appchain | Global state monolitik, tetap composable |
| Waktu konsensus | Iterative multi-node messaging (gossip) | **Proof of History** — jam kriptografi pre-ordering |
| Lingkungan modal | Kontraksi modal; beralih ke SAFT institusional selektif | Multi-tahap SAFT institusional + Dutch Auction publik |

*Kenapa Context ini penting:* dibandingkan dengan pilihan **modular/rollup-centric** Ethereum (lihat
`examples/CaseStudies/Ethereum.md` §6), Solana bertaruh pada arah berlawanan — monolitik hardware-limit —
dari kondisi pasar & teknologi yang sama. → `docs/Meta/Narratives.md`, `docs/Innovation/Timing.md`.

## 4. Origin & Team — Momen Eureka PoH dan Rebranding
_ref: `docs/Ontology/Team.md`, `docs/Project/Vision.md`, `docs/Ontology/Governance.md`_

**Anatoly Yakovenko** (spesialis sistem terdistribusi & kompresi) mengalami *momen eureka* akhir 2017:
pengalaman VoIP-nya di **Alescere (2003)** mengajarkan bahwa **jam yang andal** menyederhanakan sinkronisasi
jaringan secara masif. Ia menyadari **SHA-256 Bitcoin** bisa diubah menjadi **jam kriptografi universal** —
hashing berulang di mana output menjadi input berikutnya menciptakan urutan yang *tak dapat diparalelkan* untuk
dibuat tetapi *dapat diverifikasi paralel* dengan cepat. Draf whitepaper pertama: **November 2017**.

**Tim pendiri (Solana Labs, akhir 2017):** Yakovenko (CEO/teknis), **Greg Fitzgerald** & **Stephen Akridge**
(eks-Qualcomm), **Raj Gokal** (strategi bisnis/ekosistem), **Eric Williams**. Insinyur awal berasal dari
Qualcomm, Intel, Google, Microsoft.

### Genealogi nama — Silk → Loom → Solana *(causal event)*
| Fase | Nama | Peristiwa | Karakteristik teknis |
|---|---|---|---|
| Konseptual (2017) | **Silk / Loom** | Prototipe C oleh Yakovenko | Eksekusi sekuensial SHA-256 dasar |
| Migrasi Rust (awal 2018) | **Loom** | Fitzgerald usul Rust (keamanan memori tanpa GC); repo open-source **13 Feb 2018**; demo internal **28 Feb 2018** memproses 10.000 tx terverifikasi dalam 0,5 detik | Akselerasi sigverify via GPU (Akridge) |
| Rebranding (28 Mar 2018) | **Solana** | Konflik nama dengan Ethereum L2 "Loom Network" → ganti nama (terinspirasi Solana Beach) | — |

*Pelajaran kausal:* pilihan **Rust** (memory-safety tanpa garbage-collector) sejak awal 2018 adalah fondasi
performa; migrasi bahasa dini menghindari utang teknis di jalur kritis. → `docs/Ontology/Technology.md`.

## 5. Innovation Analysis — Delapan Inovasi Inti (arsitektur *hardware-limit*)
_ref: `docs/Ontology/Innovation.md`, `docs/Innovation/FirstMover.md`, `docs/Innovation/CompetitiveMoat.md`, `docs/Ontology/Technology.md`_

Stack inti: **Proof of History → Sealevel Runtime → Tower BFT**. Delapan inovasi kausal:

1. **Proof of History (PoH)** — VDF berbasis SHA-256 sekuensial sebagai *cryptographic timestamp*.
   *Dampak:* menghapus koordinasi p2p untuk menyepakati waktu → jaringan memproses transaksi optimistik.
   *Pelajaran:* referensi waktu objektif adalah prasyarat menghilangkan overhead komunikasi.
2. **Tower BFT** — pBFT yang memakai stempel PoH sebagai *vote lock-outs*. *Dampak:* finalitas ~400 ms.
3. **Turbine** — propagasi blok ala BitTorrent; blok dipecah jadi **shreds** + erasure codes lewat pohon
   validator. *Dampak:* memangkas beban bandwidth leader.
4. **Gulf Stream** — forwarding transaksi **tanpa mempool**; karena *leader schedule* diketahui lebih awal,
   transaksi dikirim langsung ke leader berikutnya. *Dampak:* menurunkan latensi & permukaan serangan DDoS
   mempool. *(Sisi lain: kelak jadi vektor spam saat kontrol lalu lintas belum ada — lihat §8.)*
5. **Sealevel** — runtime **eksekusi paralel**; transaksi wajib mendeklarasikan akun yang dibaca/ditulis,
   sehingga transaksi tanpa tumpang tindih dijalankan simultan di banyak core. *Dampak:* memicu tren global
   "Parallel VM". → pola transferable di §20.
6. **Pipelining** — model *assembly line*: sigverify di GPU, eksekusi di CPU, penulisan di NVMe SSD.
7. **Cloudbreak** — database akun tersebar horizontal di banyak NVMe SSD paralel (hindari I/O bottleneck).
8. **Archivers / Replicators** — penyimpanan sejarah didelegasikan ke node non-validator via **Proof of
   Replication (PoRep)**; memisahkan *data availability* dari konsensus (memelopori pemikiran DA terdistribusi).

*Pelajaran kausal menyeluruh:* memperlakukan validator sebagai **komputer multiprosesor modern** (bukan satu
mesin virtual lambat) menghasilkan throughput jauh lebih tinggi daripada menumpuk lapisan abstraksi. Ini
adalah **moat arsitektural** Solana sekaligus sumber biaya (hardware validator mahal — lihat §13, §16).

## 6. Technology Evolution — Rilis, Klien, dan Diversifikasi
_ref: `docs/Ontology/Technology.md`, `docs/TokenLifecycle/Mainnet.md`, `docs/TokenLifecycle/Maturity.md`_

| Tanggal | Milestone | Fokus |
|---|---|---|
| Mar 2020 | **Mainnet Beta** | sBPF smart contracts + Sealevel paralel |
| Feb 2021 | **Full Inflation Activation** | aktivasi emisi + staking rewards di tingkat protokol |
| Q3 2022 | Klien 1.12 (mitigasi spam) | integrasi bertahap **QUIC** menggantikan UDP mentah |
| Sep 2024 / Des 2025 | **Frankendancer** | hibrida: lapisan jaringan Firedancer + runtime Agave |
| Mei 2026 | **Firedancer 1.0** | klien independen (Jump Crypto) → diversifikasi konsensus |
| Jun 2026 | **Mithril (Alpenglow)** | klien Go produksi blok di test cluster; verifikasi status ringan |

**Diversifikasi klien (anti single-point-of-failure):** Agave/Jito (Rust), **Firedancer/Frankendancer** (C,
Jump Crypto — demonstrasi 1.000.000 TPS terkontrol, 100.000 TPS kondisi live), **Mithril** (Go, Overclock
Validator), **Sig** (Zig, Syndica). Ini respons langsung terhadap pelajaran outage 2020–2024 (lihat §8 & §19).
Roadmap **Alpenglow** menargetkan finalitas transaksi turun ke ~150 ms.

## 7. Business & Revenue Model
_ref: `docs/Ontology/Revenue.md`, `docs/Ontology/Tokenomics.md`_

Solana beroperasi sebagai jaringan settlement volume-tinggi biaya-rendah. Base fee dihitung deterministik per
jumlah signature (baseline 0,000005 SOL/signature). **Localized Priority Fee markets** membiarkan user
melampirkan tip eksekusi untuk mengakses akun bertrafik-tinggi tanpa menaikkan biaya aplikasi lain yang tak
macet — kontras dengan pasar biaya global Ethereum. Monetisasi mekanis awalnya membakar 50% seluruh biaya
transaksi (sisanya ke block producer); **SIMD-0096/SIMD-0228** kemudian mengalihkan 100% priority fee langsung
ke validator (detail kausal lengkap di §10). **Real Economic Value (REV)** — gabungan priority fee native +
tip MEV — melampaui **$550 juta pada Januari 2025 saja**, membuktikan generasi pendapatan protokol nyata di
bawah beban jaringan tinggi.

## 8. Reliability Crises — Sejarah Outage & Mitigasi *(causal core)*
_ref: `docs/Ontology/Security.md`, `docs/Ontology/Risks.md`, `docs/Patterns/Failure.md`, `docs/Patterns/Recovery.md`_

**Tabel outage terkonsolidasi** (v2 memuat 8 insiden vs 4 di v1 — digunakan tabel v2 yang lebih lengkap):

| Tanggal | Durasi | Klasifikasi Kegagalan | Akar Masalah & Mekanisme | Resolusi |
|---|---|---|---|---|
| Des 2020 | ~6 jam | Block Propagation Halt | Bug Turbine: cacat logika propagasi blok menyebabkan loop transmisi shred | Patch software perbaikan logika forwarding paket Turbine |
| 14 Sep 2021 | ~17 jam | Memory Exhaustion | Spam bot IDO Grape Protocol (Raydium): trafik UDP tak terbatas ~300–400rb TPS → validator OOM, konsensus hilang | Restart manual validator; batas memori antrean transaksi |
| 21–22 Jan 2022 | Degradasi tinggi (~70% tx drop) | Network Congestion | Banjir transaksi duplikat tak-berharga oleh bot arbitrase | Rollout awal protokol QUIC + desain pasar biaya lokal |
| 30 Apr–1 Mei 2022 | 7–8 jam | Consensus Stall | Bot NFT Candy Machine Metaplex: 4 juta TPS membanjiri memory pool | Klien v1.10; biaya eksekusi wajib untuk transaksi invalid |
| 1 Jun 2022 | 4,5 jam | State Divergence | Bug Durable Nonce: error logika penanganan nonce tahan-lama → hash status bentrok | Fitur Durable Nonce dinonaktifkan hingga dipatch permanen (v1.10.23) |
| 30 Sep 2022 | 8,5 jam | Fork Choice Failure | Bug blok duplikat: error aturan fork-choice → percabangan rantai tak terselesaikan | Koordinasi restart manual berbasis status slot snapshot |
| 25 Feb 2023 | ~19 jam | Shred Forwarding Failure | Overflow shred Turbine berukuran abnormal; logika deduplikasi gagal saat forwarding blok berat | Perbaikan rutin deduplikasi; downgrade ke rilis stabil v1.13 |
| 6 Feb 2024 | ~5 jam | Runtime Cache Halt | Bug cache JIT: infinite recompile loop pada runtime inti Agave | Patch terdistribusi v1.17.20 memaksa restart klaster |

> **INKONSISTENSI (v1 vs v2):** v1 menjelaskan insiden 25 Feb 2023 sebagai *"bug klien memancarkan blok
> raksasa abnormal → fork-selection bingung"*, sedangkan v2 mengklasifikasikannya sebagai *"Shred Forwarding
> Failure"* dengan akar masalah deduplikasi shred Turbine. Kedua deskripsi mungkin menjelaskan sisi berbeda
> dari insiden yang sama (blok abnormal → overflow shred → kebingungan fork), tetapi tidak diselaraskan
> secara eksplisit oleh kedua sumber. **Evidence Level: MEDIUM** — durasi (~19 jam) dan tanggal cocok persis
> di kedua sumber; detail mekanisme akar berbeda penekanan.

**Tiga pilar mitigasi modern:**
1. **QUIC** (ganti UDP) — congestion control + status koneksi → identifikasi/blok IP penyerang instan.
2. **Stake-Weighted QoS** — hak transmisi paket proporsional terhadap SOL yang di-stake → bot tanpa modal
   tak bisa membanjiri antrean.
3. **Localized Fee Markets** — batas Compute Unit per akun ter-lock: kemacetan satu aplikasi (mis. mint NFT)
   hanya menaikkan biaya transaksi yang menyentuh kontrak itu, **bukan** biaya global. →
   `docs/Patterns/Liquidity.md`, `docs/MarketBehaviour/UnlockImpact.md`.

*Pelajaran kausal:* **desain tanpa mempool + optimisme ekstrem** (Gulf Stream) menaikkan performa tetapi
membuka jaringan terhadap spam saat kontrol lalu lintas absen → serangkaian outage (2020–2024, 8 insiden
terdokumentasi). Solusinya bukan mengubah arsitektur, melainkan menambah **lapisan kontrol lalu lintas &
diversifikasi klien**. Sejak **6 Feb 2024**: tanpa outage hingga pertengahan 2026 (lihat §18).

## 9. Chronological Decision Events (Causal Event Graph)
_ref: `docs/Ontology/DecisionEvent.md` — unit kausal atomik; setiap event mengikuti skema Context → Trigger →
Decision → Alternatives → Execution → Stakeholder Reactions → Outcome. Diekstrak dari laporan v2._

### DEV-001 · Pilihan Arsitektural: Eksekusi Paralel Monolitik vs Sharding
- **Context:** Ethereum mengalami degradasi operasional parah akibat eksekusi single-threaded; rival smart-
  contract mengejar arsitektur sharded/multi-chain appchain (lihat §3 Context Snapshot).
- **Timestamp:** Nov 2017 – Mar 2018.
- **Trigger:** Anatoly Yakovenko menulis whitepaper Solana, menerapkan latar belakang timing sistem di
  Qualcomm untuk memecahkan sinkronisasi status terdesentralisasi.
- **Decision:** Komit ke arsitektur status-tunggal monolitik menggunakan Proof of History + eksekusi paralel
  Sealevel, secara eksplisit menolak sharding status atau struktur multi-chain.
- **Alternatives Rejected:** Membangun rollup L2 kompatibel-EVM; memakai framework appchain
  Tendermint/Cosmos SDK; implementasi sharding eksekusi.
- **Execution:** Dibangun native dalam Rust dan C/C++, mengintegrasikan penjadwalan thread hardware
  tingkat-rendah, deklarasi akses akun paralel, dan verifikasi signature hardware.
- **Stakeholder Reactions:** Founder — teguh pada tesis monolitik (§16 POV Founder). Developer — arsitektur
  baru menuntut kurva belajar Rust/sBPF lebih tinggi dari Solidity.
- **Outcome (jangka pendek → panjang):** Menjadi **moat arsitektural** utama Solana (§5); juga akar biaya
  hardware validator ekstrem (§16 POV Validator).
- **Evidence Level:** HIGH.

### DEV-002 · Koreksi Pasokan Darurat & Pembakaran Token
- **Context:** Solana menyelesaikan Dutch auction publik di CoinList Mar 2020, menetapkan perhitungan
  pasokan beredar publik.
- **Timestamp:** Mei 2020.
- **Trigger:** Sleuth on-chain menemukan pool tersembunyi **11,36 juta SOL** dialokasikan ke market maker
  eksternal untuk penyediaan likuiditas, tidak diungkapkan dalam deklarasi pasokan beredar publik.
- **Decision:** Solana Foundation memutuskan menarik kembali dan membakar permanen seluruh pool market maker
  (11,36 juta SOL) untuk memulihkan kepercayaan & keselarasan komunitas.
- **Alternatives Rejected:** Menyerap token kembali ke cadangan treasury terkunci; menempatkan pool pada
  jadwal vesting multi-tahun; membiarkan token beredar di pasar sekunder.
- **Execution:** Transaksi on-chain membakar tepat **11.363.003 SOL**, mengurangi permanen baseline pasokan
  genesis dari 500.000.000 → **488.636.997 SOL**.
- **Related legal event:** Gugatan class action (Apr 2020) menuduh Solana Labs diam-diam meminjamkan token ke
  market maker tanpa pengungkapan — diselesaikan via pembakaran ini. → `docs/Ontology/Risks.md`
  (disclosure/legal risk).
- **Evidence Level:** HIGH (angka burn persis, dikonfirmasi on-chain).

### DEV-003 · Aktivasi Jadwal Inflasi Terprogram
- **Context:** Mainnet-Beta beroperasi 11 bulan tanpa emisi inflasi terprogram, bergantung penuh pada hibah
  bootstrap & biaya transaksi dasar.
- **Timestamp:** 10 Feb 2021 (Epoch 150, Slot 64.800.004).
- **Trigger:** Partisipasi node validator & stabilisasi konsensus cukup untuk transisi ke model keamanan
  ekonomi Proof of Stake permissionless.
- **Decision:** Aktivasi terprogram jadwal inflasi mulai **8,0%/tahun**, disinflasi 15%/tahun, floor jangka
  panjang **1,5%/tahun**.
- **Alternatives Rejected:** Menunda aktivasi inflasi hingga keluar mainnet-beta; mempertahankan nol emisi
  terprogram (danai hanya dari biaya transaksi); menetapkan tingkat cetak token tahunan flat.
- **Execution:** Diberlakukan via aktivasi software on-chain pasca vote governance validator; payout epoch
  awal 213.841 SOL di Epoch 150.
- **Evidence Level:** HIGH.

### DEV-004 · Kapitalisasi Ekspansi Ekosistem (Putaran Investasi $314 Juta)
- **Context:** Aktivitas aplikasi on-chain berkembang pesat, tetapi kedalaman likuiditas order-book
  terdesentralisasi lokal jauh tertinggal dari pasar modal Ethereum.
- **Timestamp:** Jun 2021.
- **Trigger:** Ancaman kompetitif agresif dari ekosistem L1 rival yang meluncurkan program insentif likuiditas
  ratusan-juta-dolar.
- **Decision:** Eksekusi putaran private token sale institusional $314 juta untuk mendanai fund pengembangan
  ekosistem & infrastruktur likuiditas.
- **Alternatives Rejected:** Melikuidasi kepemilikan treasury Foundation di bursa spot publik; menginflasi
  emisi token native untuk reward liquidity mining.
- **Execution:** Private placement SAFT langsung dipimpin **a16z** & **Multicoin Capital**, dengan partisipasi
  Alameda Research, Jump, CoinFund, Polychain, CMS.
- **Evidence Level:** HIGH (dikonfirmasi press release resmi solana.com — lihat §21 Sources).

### DEV-005 · Pengerasan Pipeline Transaksi Inti (QUIC, QoS, Localized Fee Markets)
- **Context:** Antara Sep 2021–Mei 2022, Solana mengalami outage besar berdurasi 7–17 jam akibat spam bot
  otomatis saat mint NFT/peluncuran token bervolume tinggi (lihat §8 tabel outage).
- **Timestamp:** Apr 2022 – Okt 2022.
- **Trigger:** Trafik transaksi bot mencapai 4.000.000 TPS, membanjiri pipeline jaringan UDP node validator &
  menyebabkan memory overflow yang meruntuhkan konsensus.
- **Decision:** Rombak ulang pipeline ingestion inti — ganti UDP mentah dengan protokol QUIC Google, terapkan
  Stake-Weighted QoS, dan deploy Localized Fee Markets.
- **Alternatives Rejected:** Beralih ke sistem lelang gas fee global; mewajibkan verifikasi identitas di
  gateway RPC; membatasi batas blok eksekusi secara artifisial.
- **Execution:** Diluncurkan lintas versi klien validator v1.10–v1.14, memaksa node RPC/validator
  memprioritaskan trafik koneksi berdasarkan bobot stake.
- **Evidence Level:** HIGH.

### DEV-006 · Penugasan Klien Validator Independen (Firedancer)
- **Context:** Setiap node jaringan menjalankan software turunan codebase Rust asli Solana Labs, menciptakan
  profil risiko single-point-of-failure software bug.
- **Timestamp:** Agu 2022.
- **Trigger:** Konsensus-halt berulang akibat bug eksekusi klien menyoroti risiko keandalan jaringan & batas
  adopsi institusional.
- **Decision:** Menugaskan Jump Crypto membangun klien validator independen dari nol dalam C/C++, bernama
  Firedancer.
- **Alternatives Rejected:** Bergantung tanpa batas waktu pada Jito-Solana (fork Rust pengoptimasi MEV);
  mendanai fork Rust sekunder.
- **Execution:** Jump Crypto mengerahkan insinyur trading berlatensi-rendah membangun mesin networking,
  eksekusi, dan konsensus berbasis C; meluncurkan rilis hibrida (Frankendancer) sebelum deployment mainnet
  penuh.
- **Evidence Level:** HIGH.

### DEV-007 · Pengelolaan Insolvensi Alameda & Restrukturisasi Lockup OTC
- **Context:** Keruntuhan FTX/Alameda mengungkap entitas memegang **55,86 juta SOL** (~10,8% pasokan
  jaringan), 42,16 juta SOL di antaranya terkunci dalam kontrak vesting multi-tahun; harga spot SOL jatuh
  >90%.
- **Timestamp:** Nov 2022 – Apr 2024.
- **Trigger:** Mandat pengadilan kebangkrutan mewajibkan likuidator merealisasikan pemulihan kas untuk
  kreditur FTX Estate.
- **Decision:** Fasilitasi penjualan OTC terstruktur kepemilikan SOL terkunci ke konsorsium institusional
  (Pantera Capital, Galaxy Digital) dengan diskon (**$64,00/SOL**) terikat jadwal vesting linear multi-tahun
  hingga 2028.
- **Alternatives Rejected:** Melikuidasi token yang sudah unlocked langsung di pasar spot terbuka; hard-fork
  protokol untuk membatalkan alamat token Alameda.
- **Execution:** Penjualan OTC disahkan pengadilan, dieksekusi Galaxy Asset Management, mempertahankan jadwal
  lockup asli sambil memindahkan kustodi token ke dana institusional.
- **Conflicting evidence (lihat §11):** kreditur FTX berargumen penjualan privat diskon merugikan nilai upside
  estate; likuidator & pengembang ekosistem berargumen lockup ketat diperlukan mencegah crash pasar spot
  sekunder.
- **Evidence Level:** HIGH untuk angka kepemilikan/harga; MEDIUM untuk penilaian "benar/salah"-nya keputusan
  (perspektif kreditur vs likuidator berbeda — lihat §11).

### DEV-008 · Pivot Divisi Hardware Mobile (Saga → Seeker)
- **Context:** Solana Mobile meluncurkan ponsel flagship Web3 Saga seharga $1.000 pada Mei 2023, tetapi
  mencatat <2.500 unit terjual hingga Des 2023 — jauh di bawah ambang impas operasional 30.000 unit.
- **Timestamp:** Agu 2023 – Jan 2024.
- **Trigger:** Ancaman kegagalan finansial & write-off vertikal produk hardware.
- **Decision:** Potong harga Saga ke $599, koordinasikan proyek ekosistem melekatkan reward token (klaim
  token BONK 30 juta) ke Genesis Token native perangkat, manfaatkan arbitrase user yang dihasilkan untuk
  mendanai perangkat kedua massal ("Seeker").
- **Alternatives Rejected:** Menutup divisi hardware & menyerap seluruh kerugian produksi terakumulasi.
- **Execution:** Apresiasi cepat alokasi $BONK menyebabkan nilai token yang disertakan melampaui biaya
  hardware $599, memicu sellout inventori viral dalam 48 jam & menghasilkan 150.000+ pre-order ($67,5 juta+
  modal terkumpul) untuk perangkat lanjutan Seeker.
- **Evidence Level:** HIGH.

## 10. Tokenomics & Monetary-Policy Crisis (SIMD-0096 / 0123 / 0228)
_ref: `docs/Ontology/Tokenomics.md`, `docs/Ontology/Incentives.md`, `docs/Ontology/Governance.md`, `docs/MarketBehaviour/UnlockImpact.md`_

**Genesis: 500 juta SOL** (sebelum burn DEV-002; baseline pasca-burn 488.636.997 SOL). Distribusi alokasi (v1):
| Alokasi | % dari Genesis |
|---|---|
| Seed Sale | 15,86% |
| Founding Sale | 12,63% |
| Validator Sale | 5,07% |
| Strategic Sale | 1,84% |
| CoinList Public Auction | 1,60% |
| Team (pendiri) | 12,50% |
| Solana Foundation | 12,50% |
| Community Reserve Fund | 38,00% |

> **INKONSISTENSI (v1 vs v2):** v2 melaporkan tabel alokasi berbeda dengan basis **pasokan pasca-burn**
> (488.636.997 SOL): Seed 25,60% (81,2jt SOL, $0,04), Founding Sale 20,40% (64,6jt SOL, $0,20), Founding Team
> 20,20% (63,9jt SOL), Solana Foundation/Reserve 20,20% (194,5jt SOL), Validator Sale 8,20% (25,9jt SOL,
> ~$0,225), Strategic Sale 3,00% (9,4jt SOL, ~$0,25), CoinList 2,60% (8,0jt SOL, $0,22; total raised ~$26,11jt).
> **Catatan kalkulasi:** persentase v2 untuk baris "Founding Team" dan "Solana Foundation/Reserve" **sama-sama
> tertulis 20,20%** meski volume SOL-nya berbeda jauh (63,9jt vs 194,5jt) — kemungkinan kesalahan transkripsi
> di sumber v2 (194,5jt/488,6jt ≈ 39,8%, lebih dekat ke angka "Community Reserve Fund 38,00%" milik v1).
> **Evidence Level: LOW** untuk persentase v2 baris Reserve/Foundation — gunakan v1 (38,00% Community Reserve)
> sebagai rujukan lebih dapat diandalkan untuk baris ini sampai terverifikasi ulang; volume SOL absolut v2
> (194,5jt) tetap dicatat sebagai data mentah.

**Jadwal inflasi:** initial **8%/th**; disinflasi **−15% per epoch-year** (~180 epoch); **terminal 1,5%/th**
selamanya sebagai insentif keamanan dasar. Staking rate jaringan bertahan ~65% dari ~380 juta SOL ter-stake (v2).

**Struktur biaya:** Base Fee 5.000 lamports/signature → **50% dibakar, 50% ke validator**. Priority Fee →
pasca-SIMD-0096 **100% ke validator**; pasca-SIMD-0123 dibagi otomatis ke staker.

### Krisis kebijakan moneter 2025 *(causal chain)*
1. **Masalah lama (pre-2025):** priority fees ikut dibakar 50%. Karena separuh "hangus", pengirim
   **berkolusi off-chain** dengan validator (mis. Jito Block Engine tip privat) → transparansi biaya jaringan
   runtuh. *(Contoh kebijakan deflasi agresif yang justru memicu bypass protokol.)*
2. **SIMD-0096 (Feb 2025):** hapus pembakaran priority fee → **100% ke validator**; burn 50% hanya di base fee.
   *Dampak makro:* burn harian anjlok **~18.000 → ~1.000 SOL**; inflasi tahunan naik **~3,6% → ~4,7%**.
   *(Sukses menutup kolusi, tetapi memicu lonjakan inflasi — trade-off.)*
3. **Reaksi (Mar 2025):** staker ritel protes validator diuntungkan sepihak. Dua proposal:
   - **SIMD-0228 (DITOLAK, 61,39% menolak):** pangkas emisi dinamis berbasis rasio staking (bisa turun ke
     ~0,9%). Ditolak karena mengancam pendapatan **validator kecil** yang bergantung pada emisi dasar untuk
     menutup biaya hardware. **Suara delegasi Solana Foundation (~10% stake aktif) jadi penentu penolakan.**
   - **SIMD-0123 (DISETUJUI):** mekanisme on-chain agar validator membagikan priority-fee revenue ke
     delegator secara proporsional → menyeimbangkan REV tanpa merusak kelayakan validator kecil.

*Pelajaran kausal:* **pembakaran biaya yang terlalu agresif di L1 performa tinggi memicu bypass off-chain,
memaksa reformasi kembali ke distribusi berbasis staker.** → pola formal di §19. Bandingkan dengan Ethereum
di mana **sukses teknis (Dencun) merusak tokenomics (net-inflasi)** — di Solana, **reformasi anti-kolusi
(SIMD-0096) menaikkan inflasi** sebagai efek samping. → `examples/CaseStudies/Ethereum.md` §10.

## 11. Conflicting Evidence & Unresolved Questions (dari sumber v2 — dipertahankan sebagai bukti, bukan disimpulkan)
_ref: `docs/Ontology/Hidden.md`, `docs/Reasoning/Confidence.md` — prinsip "investigator bukan analyst": simpan
perselisihan, jangan diseragamkan._

**Kontroversi likuiditas pasar-maker awal:** pinjaman 11,36 juta SOL ke market maker (DEV-002) tanpa
pengungkapan publik memicu tuduhan pelaporan pasokan menyesatkan. Meski Foundation membakar jumlah setara,
debat historis tentang syarat eksekusi market-maker sebelum ditemukan publik tetap belum tuntas.

**Perselisihan likuidasi FTX/Alameda (DEV-007):** likuidator menjual >40 juta SOL terkunci ke konsorsium
institusional privat seharga $64,00/token — diskon ~60% dari harga spot sekunder ($175,00) saat eksekusi.
**Kreditur FTX** berargumen penjualan privat diskon merampas nilai upside estate. **Likuidator & pengembang
ekosistem** berargumen syarat lockup ketat multi-tahun (hingga 2028) diperlukan mencegah crash pasar spot
sekunder. *(Kedua sisi argumen dipertahankan — bukan disimpulkan siapa benar.)*

**Status regulasi SEC:** Jun 2023 SEC menuduh SOL adalah sekuritas tak-terdaftar dalam gugatan terhadap bursa
tersentralisasi; Solana Foundation menolak formal klasifikasi ini. Persetujuan SEC atas Spot Staking Solana
ETF (akhir 2025) menandakan penerimaan regulasi, namun preseden hukum untuk distribusi SAFT awal tetap
subjek interpretasi yudisial berkelanjutan.

**Pertanyaan terbuka tambahan (dari v2):**
1. Seiring disinflasi -15%/tahun mendekati floor 1,5%/tahun, apakah REV organik (fee dasar + priority fee +
   tip MEV) semata cukup menutup biaya operasional hardware validator selama siklus bear-market volume rendah?
   Model ekonomi jangka-panjang ini belum terkonfirmasi.
2. Pivot hardware Saga→Seeker mengamankan 150.000+ pre-order ($67,5jt+), tetapi data empiris penggunaan
   aplikasi harian aktif jangka-panjang vs pembelian spekulatif murni (mengejar airdrop token masa depan)
   masih belum lengkap.

## 12. Airdrop & Incentive Intelligence
_ref: `docs/Patterns/Points.md`, `docs/Success/Airdrop.md`, `docs/Patterns/Narrative.md`, `docs/Ontology/Community.md`_

| Airdrop | Tujuan | Strategi | Dampak |
|---|---|---|---|
| **BONK** (Des 2022) | Pulihkan moral pasca-FTX (SOL $8) | 50% pasokan retroaktif ke kreator NFT, dev aktif, user DeFi awal | Membalik nilai beli ponsel Saga (DEV-008); publisitas global; menyelamatkan aktivitas on-chain |
| **Jito / JTO** (Des 2023) | Tarik modal ke LST JitoSOL vs Marinade | Poin tertutup; **struktur bergradasi memihak user kecil** | >$165 juta ke komunitas dalam jam; menetapkan standar peluncuran berbasis poin |
| **Jupiter / JUP** (2024→) | Demokratisasi tata kelola ke ~1 juta dompet | Multi-fase; dinilai atas konsistensi volume historis | Klaim tanpa kemacetan; awal 2026 pangkas target airdrop **700 juta → 200 juta JUP** demi kurangi tekanan jual |

**SFDP (Solana Foundation Delegation Program):** yayasan mendelegasikan SOL cadangan ke validator baru
berperforma (uptime & kecepatan shred) untuk menutup biaya server tahun-tahun awal → **~10% stake aktif**,
suara penentu (mis. penolakan SIMD-0228). *(Titik sentralisasi tata kelola yang perlu dicatat.)*
→ `docs/Ontology/Incentives.md`, `docs/Ontology/Governance.md`.

**Anti-Sybil ekosistem (v2):** alih-alih airdrop foundation-level yang memicu farming wallet otomatis, aplikasi
ekosistem (Jito, Pyth, Jupiter, Tensor) mengevaluasi aktivitas historis berdasarkan volume trading kumulatif
order-book, persistensi interaktif multi-bulan, dan verifikasi berbasis-hardware. Insiden arbitrase Saga
(DEV-008) mengonversi 20.000+ user sekunder menjadi partisipan Web3 terverifikasi-hardware; struktur pre-order
Seeker menghilangkan jaringan bot otomatis dengan mewajibkan pembayaran non-refundable $450–500/unit,
mengamankan 150.000+ profil user non-Sybil terverifikasi.

## 13. Community & Narrative Intelligence
_ref: `docs/Ontology/Community.md`, `docs/Meta/Narratives.md`, `docs/Patterns/Narrative.md`, `docs/Meta/MarketCycles.md`_

**Akuisisi developer:** **Global Hackathon** (dinilai langsung oleh VC → jalur cepat pendanaan) & **Hacker
Houses** (co-working gratis + pelatihan insinyur inti). Data Electric Capital: Solana menjadi ekosistem
terdepan penarik developer baru Q3 2023–Q1 2024 (7.625 builder baru, pertumbuhan 83%); dev aktif bulanan
stabil >1.200 kontributor sejak 2025. Adopsi framework **Anchor** (type-safety, serialisasi otomatis,
proteksi CPI exploit) memperkuat retensi developer.

**Pertumbuhan ritel:** Ambassador Program (lokalisasi edukasi Rust), gamifikasi poin (Jito, Kamino), NFT
identitas (Mad Lads, Claynosaurz) sebagai skema loyalitas.

**Peran narasi lintas siklus:**
| Fase | Narasi | Peran Solana |
|---|---|---|
| DeFi Summer (2020–21) | Order book on-chain penuh | **Pencipta** (Serum, bareng FTX) |
| NFT Mania (2021–22) | Mint NFT murah untuk massa | **Fast Follower** (Metaplex, biaya mint −99%) |
| Kejatuhan & Pemulihan (2022–23) | Desentralisasi sejati pasca-korporat | **Pencipta** (OpenBook fork Serum) |
| Spekulasi Meme (2024–25) | Peluncuran token ritel instan | **Pencipta** (Pump.fun, bonding curve) |
| DePIN/RWA/AI (2025–26) | Infra fisik + agen AI mandiri | **Pencipta utama** (Helium & Render migrasi; Google Cloud AI payment agent) |

*Pola:* Solana berulang kali **menciptakan** (bukan sekadar mengikuti) narasi siklus, dengan satu pengecualian
Fast-Follower (NFT). → `docs/Meta/Rotation.md`, `docs/Meta/Hype.md`. Cross-link DePIN: `examples/Pioneer/Helium.md`.

**Sentimen komunitas (v2, kualitatif):** siklus sentimen ekstrem — euforia ritel 2021 (harga $0,22→$258,72),
ketakutan ekstrem pasca-FTX (narasi "proyek terikat SBF"), rebound tajam 2023–2025 didorong volume memecoin,
DePIN, dan opsi liquid staking yang berkembang. Ketidakpuasan awal atas float publik kecil (2,6% CoinList)
membaik seiring biaya sub-sen & finalitas sub-detik terbukti nyata.

## 14. Product Evolution — dari SDK ke Perangkat Keras Konsumen
_ref: `docs/Project/Roadmap.md`, `docs/Ontology/Adoption.md`, `docs/Ontology/Infrastructure.md`_

Pergeseran dari API/SDK murni ke **hardware konsumen** (kronologi kausal lengkap: lihat DEV-008):
- **Solana Mobile Stack (2022):** Seed Vault, dApp Store, penandatanganan berbasis Android.
- **Saga (Apr 2023, $1.000):** flagship premium; **gagal jual** (<2.500 unit vs ambang impas 30.000) — lalu
  **berbalik** akhir 2023 saat **BONK gratis** (klaim genesis) melampaui harga ponsel → borong arbitrase.
- **Seeker (Agustus 2025, $450–500):** pivot ke kelas menengah terjangkau; TEEPIN + Seeker ID + token **SKR**;
  **150.000+ unit** pra-order (vs 20.000 Saga), ~$67,5 juta+ modal terkumpul.

*Pelajaran:* pivot dari "spec war premium" ke "mass-entry terjangkau + utilitas token" memperbaiki
product-market fit. → `docs/Innovation/ProductMarketFit.md`.

## 15. Competitive Landscape (lintas fase)
_ref: `docs/Valuation/Competitors.md`, `docs/Valuation/ComparableProjects.md`, `docs/Meta/MarketCycles.md`_

| Fase | Kompetitor | Keunggulan Solana | Kelemahan | Mengapa menang |
|---|---|---|---|---|
| 1 · Kelahiran (2018–20) | Ethereum, EOS, Tron | ~65.000 TPS tanpa sharding | Ekosistem dev kecil, pustaka belum matang | EOS/Tron sentralisasi tata kelola + gagal tarik dev finansial |
| 2 · Ekspansi DeFi (2021–23) | BSC, Avalanche, Near | Likuiditas institusional (FTX), Sealevel superior | Ketidakstabilan/outage | Komunitas dev organik bertahan; BSC/Avax stagnan pasca-insentif |
| 3 · Multi-Client & MoveVM (2024–26) | Sui, Aptos, Monad, Base/Arbitrum | Likuiditas masif, multi-klien, dominasi volume meme & DePIN | Hardware validator tetap sangat tinggi | Network effect ritel + integrasi Visa/WU + akses Spot ETF menang atas keunggulan teoretis MoveVM |

Kompetisi utama 2026: dominasi Ethereum di satu sisi, ancaman L1 **MoveVM** (Sui/Aptos) di sisi lain.
→ `docs/Valuation/Competitors.md`. Cross-link modular rival: `examples/Pioneer/Optimism.md`, `Celestia.md`.

## 16. Token Lifecycle & Price Causality
_ref: `docs/MarketBehaviour/*`, `docs/Reasoning/Prediction.md`, `docs/TokenLifecycle/*`_

| Metrik | Nilai | Kondisi |
|---|---|---|
| Harga seed terendah | $0,04 | 2018 |
| Harga CoinList | $0,22 | 24 Mar 2020 |
| Pasar sekunder awal | $0,22–$0,95 | 2020 |
| Tembus $15 | Mar 2021 | aktivasi staking + modal FTX/Alameda |
| **ATH** | **$258,72–$259,96** (MC >$74 mrd) | 6 Nov 2021 (spekulasi Metaplex + TVL Serum) |
| **ATL siklus** | **$8,00–$8,42** | Des 2022 (pasca-kebangkrutan FTX) |
| Rebound Q1 2024 | ~$175,00 | pemulihan pasar |
| **Peak Maturity 2025–2026** | **$293,31–$294,00 (ATH baru)** | REV & adopsi institusional |
| Pasokan beredar (2026) | ~582,8–601,5 juta SOL | (v2; v1 mencatat ~440–580 juta — rentang serupa, v2 lebih baru) |
| Market cap (2026, ATH) | $170+ miliar | v2 |
| REV triwulanan | ~$800 juta | v1 — landasan valuasi fundamental |

**Kausalitas harga:** (1) apresiasi 2021 didorong DeFi/NFT + likuiditas FTX; (2) **kejatuhan ke ~$8** akibat
kebangkrutan FTX (risiko konsentrasi DEV-007 terwujud); (3) **rebound 2024–26** ditopang pendapatan riil
(meme, DePIN, payments) + adopsi **Spot ETF** dan institusi. Valuasi 2026 bertumpu pada **arus kas REV**,
bukan spekulasi teoretis. → `docs/MarketBehaviour/DeathSpiral.md` (dihindari), `docs/MarketBehaviour/Recovery.md`.

**Metrik jaringan historis per checkpoint (v2, data granular tambahan):**
| Metrik | TGE (Q1 2020) | Puncak Bull (Nov 2021) | Insolvensi FTX (Des 2022) | Recovery (Q1 2024) | Peak Maturity (2025-26) |
|---|---|---|---|---|---|
| Wallet aktif harian | <5.000 | ~200.000 | ~80.000 | ~1.200.000 | 2,2–2,6 juta |
| Volume DEX harian | Negligible | ~$300 juta | ~$30 juta | ~$1,5 miliar | $39,0 miliar (peak) |
| DeFi TVL | <$1,0 juta | ~$11,2 miliar | ~$210 juta | ~$4,5 miliar | $8,0–$23,0 miliar |
| Throughput puncak terukur | ~1.000 TPS | ~2.500 TPS | ~2.000 TPS | ~4.000 TPS | 100.000+ TPS (Firedancer live) |
| Validator konsensus aktif | ~100 | ~1.000 | ~1.800 | ~1.700 | ~1.295–1.400 |

## 17. Business Intelligence & Kemitraan
_ref: `docs/Ontology/Revenue.md`, `docs/Valuation/Revenue.md`, `docs/Ontology/Metrics.md`, `docs/Ontology/Adoption.md`_

| KPI (2025/26) | Nilai | Implikasi |
|---|---|---|
| DeFi TVL | ~$5,8–23,0 miliar (rentang v1/v2) | likuiditas tebal DEX & lending |
| REV maksimum harian | $56,9 juta (rekor 19 Jan 2025, v1) | kapasitas monetisasi langsung |
| REV bulanan (Jan 2025) | >$550 juta (v2) | validasi independen skala REV |
| Developer aktif | ~17.700 (v1) / 1.200+ inti bulanan, +83% dev baru (v2) | inovasi dApps berkelanjutan |
| Settlement USDC tahunan | ~$3,5 miliar | kepercayaan institusi (Visa) |

**Kemitraan:** **Visa** (Sep 2023, setelmen USDC on-chain), **Western Union** (awal 2026, pilot remittance
stablecoin), **Shopify/Solana Pay** (Agu 2023, checkout USDC tanpa fee kartu). *Dampak:* memvalidasi kelayakan
teknis Solana di mata institusi, mematahkan narasi skeptis "jaringan tidak stabil". → `docs/Success/Revenue.md`,
`docs/Success/Adoption.md`.

## 18. POV Success-Matrix (§15)
_ref: `docs/Success/*`, `docs/Reasoning/Explainability.md`, `docs/Reasoning/Confidence.md`_

Success is **not binary** — verdict per point-of-view, each with an evidence level (see
`docs/Protocol/Deep-Research-Brief.md`, 8 POVs). Solana = keberhasilan **performa, UX ritel & monetisasi riil**,
tetapi hasilnya berbeda tergantung POV:

| POV | Verdict | Alasan | Evidence |
|-----|---------|--------|----------|
| **Founder** (`Success/Founder.md`) | ✅ Sukses | Teguh pada monolitik sinkron (menolak tekanan pindah ke L2 modular, DEV-001) — terbukti optimal untuk UX ritel; tapi meremehkan spam/botting awal → luka reputasi outage | HIGH |
| **VC** (`Success/VC.md`) | ✅ Sukses | Outsized return dari seed $0,04 → ATH ~$259–294; tapi terpapar kebangkrutan FTX/Alameda (~2 tahun kredibilitas ternoda, DEV-007) | HIGH |
| **Retail** (`Success/Community.md`) | ⚠️ Campuran | Eksekusi instan ~seperseribu sen membuka spekulasi tanpa batas; tapi kerugian hack dompet Slope (2022) + MEV botting agresif | MEDIUM |
| **Community** (`Success/Community.md`) | ✅ Sukses | Basis akar rumput loyal; saat FTX bangkrut komunitas merekonstruksi likuiditas (OpenBook) + moral rebound BONK | HIGH |
| **Developer** (`Success/Developer.md`) | ✅ Sukses | ~17.700 dev aktif (1.200+ inti bulanan); inovasi paralel tanpa fragmentasi likuiditas; tapi kompilasi Rust/sBPF jauh lebih sulit dari Solidity EVM | MEDIUM–HIGH |
| **Institution** (`Success/Adoption.md`) | ✅ Sukses | Integrasi Visa/Western Union/Shopify, settlement USDC ~$3,5 mrd/th, akses Spot ETF → memvalidasi kelayakan teknis | HIGH |
| **Validator** (`Success/Protocol.md`) | ⚠️ Campuran | Pendapatan naik drastis pasca-SIMD-0096 (100% priority fee); tapi beban hardware ekstrem (ECC RAM 192–384 GB, ribuan dolar) menekan validator kecil | MEDIUM |
| **Builder (dApp/DePIN)** (`Success/Ecosystem.md`) | ✅ Sukses | Pump.fun mendominasi volume ritel; migrasi DePIN (Helium/Render); tapi lingkungan MEV/botting menyulitkan builder awal | MEDIUM–HIGH |

**Takeaway:** proyek yang sama "menang" di performa/institusi/komunitas namun "seri" di retail/validator —
inilah alasan verdict harus per-POV, bukan satu label. Biaya desentralisasi hardware dan jejak luka
reliabilitas (baru pulih pasca-2024) adalah sisi gelap dari taruhan *hardware-limit*.

## 19. Current State (pertengahan 2026)
_ref: `docs/Ontology/Metrics.md`, `docs/Ontology/Security.md`, `docs/TokenLifecycle/Maturity.md`_

Fase **kesehatan fundamental terkuat** sepanjang sejarah:
- **100% uptime** sejak outage terakhir (Feb 2024) — validasi perbaikan QUIC + diversifikasi klien.
- **Diversifikasi klien:** Frankendancer ~20,9% stake aktif; Firedancer 1.0 bertahap mengikis dominasi
  Agave/Jito; demonstrasi 1.000.000 TPS terkontrol, 100.000 TPS live.
- **Alpenglow cluster:** membuktikan kesiapan penghapusan block-level compute-unit cap (**SIMD-0370**),
  membuka jalan **kompresi ZK v2** (penyimpanan akun ~1000× lebih murah); target finalitas ~150 ms.

## 20. Lessons Learned
_ref: `docs/Patterns/Failure.md`, `docs/Patterns/Recovery.md`, `docs/Reasoning/*`_

**Kesalahan terbesar:**
1. **Menunda kontrol lalu lintas** (UDP mentah tanpa kontrol di awal) → 8 outage terdokumentasi (2020–2024) &
   kerusakan reputasi bertahun-tahun.
2. **Ketergantungan klien tunggal** (100% validator pada kode Rust Labs) → satu bug JIT meruntuhkan jaringan
   global.

**Praktik terbaik yang layak ditiru:**
1. **Optimasi perangkat keras asli** > lapisan abstraksi VM lambat.
2. **Pemberdayaan komunitas dev akar rumput** (hackathon tanpa henti) → saat FTX bangkrut, komunitaslah yang
   merekonstruksi infrastruktur likuiditas (OpenBook). → `docs/Success/Community.md`.

## 21. Knowledge Extraction — Patterns & Lessons (§18–19)
_ref: `docs/Patterns/*`, `docs/Reasoning/*`, `docs/Schema/PatternSchema.md` — bahan analog untuk prediksi._

1. **Parallel-VM Access-Declaration Pattern** — L1 paralel stabil **hanya jika** developer wajib mendeklarasikan
   akun baca/tulis di tingkat instruksi (seperti Sealevel). Tanpa itu, klaim paralel runtuh saat beban puncak.
   → `docs/Patterns/Growth.md`, `docs/Reasoning/Prediction.md`.
2. **Priority-Fee Redistribution Dynamic** — *Pembakaran biaya agresif → kolusi off-chain → alokasi 100% ke
   validator → inflasi naik → distribusi otomatis ke staker (SIMD-0123).* Kebijakan deflasi berlebihan di L1
   performa tinggi memaksa reformasi moneter kembali ke staker. → `docs/Patterns/Ponzinomics.md` (anti-pola),
   `docs/Ontology/Incentives.md`.
3. **Morale-Rebounding Meme Cycle** — *Kejatuhan harga ekstrem → airdrop meme komunitas → stimulasi volume
   mikro ritel → pemulihan likuiditas.* Cetak biru pemulihan krisis kepercayaan (BONK pasca-FTX).
   → `docs/Patterns/Narrative.md`, `docs/MarketBehaviour/Recovery.md`.
4. **Reliability-Debt Pattern** — optimisme ekstrem tanpa kontrol lalu lintas menumpuk "utang keandalan" yang
   dibayar lewat outage (8 insiden terdokumentasi); pelunasannya adalah lapisan QoS + diversifikasi klien,
   bukan perombakan arsitektur. → `docs/Patterns/Failure.md`.
5. **Client-Diversity-as-Security** — L1 monolitik aman hanya dengan ≥2 klien independen dalam bahasa berbeda
   (Rust/C/Go/Zig). Klien tunggal = anti-pola risiko kelumpuhan total. → `docs/Ontology/Security.md`.
6. **Token-Value-over-Spec adoption** (Saga/BONK, DEV-008) — utilitas/airdrop token dapat mengalahkan
   spesifikasi sebagai pendorong adopsi hardware. → `docs/Innovation/ProductMarketFit.md`.
7. **Concentration-Overhang Risk** — kepemilikan token besar pihak ketiga (Alameda, DEV-007) = risiko
   sistemik saat entitas itu gagal; mitigasi butuh kustodian & distribusi terkelola. → `docs/Ontology/Risks.md`,
   `docs/MarketBehaviour/Distribution.md`.
8. **Decision-under-Pressure-with-Rejected-Alternatives** — pola berulang di seluruh 8 Decision Event (§9):
   tim selalu punya alternatif lebih murah/cepat yang ditolak demi opsi yang menjaga *trust* atau *arsitektur
   inti* jangka panjang (mis. burn token drpd vesting diam-diam; klien independen drpd fork Rust sekunder).
   → `docs/Ontology/DecisionEvent.md`, `docs/Reasoning/AnalogEngine.md`.

### Entitas & relasi ontologi (kandidat Knowledge Graph)
_ref: `docs/Schema/KnowledgeGraph.md`, `docs/Schema/EntityRelationship.md`_
- `[Anatoly_Yakovenko] —INVENTED→ [Proof_of_History]`
- `[Solana_L1] —USES→ [Proof_of_History]` · `[Solana_L1] —EXECUTED_VIA→ [Sealevel_Parallel_Runtime]`
- `[Firedancer_Client] —WRITTEN_IN→ [C]` · `[Mithril_Client] —WRITTEN_IN→ [Go]` · `[Sig_Client] —WRITTEN_IN→ [Zig]`
- `[SIMD_0096] —ALLOCATES_100%→ [Priority_Fees_To_Validators]`
- `[SIMD_0123] —DISTRIBUTES_ON_CHAIN→ [Priority_Fees_To_Stakers]`
- `[DEV-002] —RESULTED_IN→ [Genesis_Supply_Correction_488636997_SOL]`
- `[DEV-007] —INVOLVED→ [FTX_Estate] , [Pantera_Capital], [Galaxy_Digital]`

## 22. Transferable Intelligence (§20) — heuristik reusable untuk L1 performa tinggi baru
_ref: `docs/Reasoning/AnalogEngine.md`, `docs/Reasoning/Weighting.md`, `docs/Reasoning/Confidence.md`_

- **Account-Declaration Index:** L1 baru yang mengklaim eksekusi paralel **tanpa** memaksa deklarasi akun di
  tingkat instruksi → klaim paralel tak stabil, degradasi parah saat trafik puncak.
- **Client Complexity Ratio:** L1 performa tinggi aman **hanya** dengan ≥2 klien independen (bahasa berbeda).
- **Stake-Weighted QoS Rule:** L1 monolitik throughput tinggi **wajib** membatasi trafik berbasis stake untuk
  menetralkan bot tanpa modal.
- **Solana-specific (tidak transferable):** kebutuhan **clock-speed single-core CPU tertinggi** akibat VDF PoH
  yang sekuensial — tak berlaku pada L1 berbasis DAG yang mengizinkan sinkronisasi asynchronous.
- **scope (era/kondisi berlaku):** heuristik di atas diamati pada era monolitik-vs-modular 2018–2026, saat
  hardware-scaling masih kompetitif melawan rollup-centric scaling. Jika masa depan condong total ke L2/DA
  murah, sebagian premis "hardware-limit menang" bisa melemah — evaluasi `docs/Ontology/Context.md` target
  sebelum menerapkan buta.

## 23. Open Questions (§21)
_ref: `docs/Reasoning/DecisionTree.md`, `docs/Reasoning/Confidence.md`_

1. **Batas kepadatan akun Sealevel:** seberapa jauh runtime paralel bertahan sebelum *state contention* pada
   dApps berskala miliaran pengguna memicu kegagalan transaksi berantai?
2. **Efek inflasi jangka panjang pasca-SIMD-0096:** apakah 100% priority fee ke validator tanpa burn akan
   menekan nilai fundamental SOL secara makro?
3. **Monopoli LST Jito:** jika Jito-Solana menahan ~88% stake aktif via daya tarik tip MEV, apakah tujuan
   diversifikasi klien (Firedancer 1.0) terhambat karena validator enggan melepas imbal hasil lelang MEV Jito?
4. **(dari v2) Keberlanjutan REV organik:** apakah fee dasar + priority fee + tip MEV semata cukup menutup
   biaya hardware validator selama siklus bear-market volume rendah, seiring disinflasi mendekati floor 1,5%?
5. **(dari v2) Penggunaan riil Seeker:** proporsi pembeli 150.000+ unit yang benar-benar memakai perangkat
   harian vs membeli murni spekulatif demi airdrop token masa depan — data belum lengkap.

## 24. Evidence Level — kesimpulan kunci (§22)
_ref: `docs/Reasoning/Confidence.md`, `docs/Research/Verification.md`, `docs/Research/QualityControl.md`_

| Kesimpulan | Keyakinan | Alasan |
|---|---|---|
| SIMD-0096 menaikkan inflasi SOL instan (hentikan burn priority fee) | **HIGH** | Agave v2.0 memisahkan proses priority fee; data on-chain (Blockworks): burn ~18.000 → ~1.000 SOL; dikonfirmasi kedua sumber |
| Firedancer 1.0 diluncurkan independen, tingkatkan desentralisasi | **HIGH** | Rilis produksi repo GitHub Firedancer-io; peluncuran mainnet 5 Mei 2026; demonstrasi TPS terkonfirmasi kedua sumber |
| DEV-002 burn 11.363.003 SOL memulihkan kepercayaan pasca kontroversi market-maker | **HIGH** | Angka on-chain persis, dikonfirmasi kedua sumber + gugatan class action terdokumentasi |
| Seeker mengamankan pendapatan ekosistem ≥$67,5 juta | **MEDIUM** | Kalkulasi 150.000 unit × $450–500; realisasi bergantung biaya produksi hardware; penggunaan riil vs spekulatif belum terverifikasi (§23.5) |
| Root-cause tunggal insiden 25 Feb 2023 (fork-selection vs shred-forwarding) | **MEDIUM** | Dua sumber berbeda penekanan mekanisme akar (§8 INKONSISTENSI); tanggal & durasi cocok, detail teknis tidak diselaraskan |
| Persentase alokasi genesis "Founding Team"/"Reserve" v2 (20,20% masing-masing) | **LOW** | Kemungkinan kesalahan transkripsi sumber (§10 INKONSISTENSI); v1 (38,00% Community Reserve) dipakai sebagai rujukan lebih andal |
| Mithril (Go) & Sig (Zig) rebut ≥10% stake masing-masing sebelum 2028 | **LOW** | Kemajuan teknis menjanjikan, tetapi validator enggan pindah dari Jito karena pendapatan tip MEV |

## 25. Related Framework Definitions
- **Ontology:** `docs/Ontology/Identity.md`, `Team.md`, `Funding.md`, `Tokenomics.md`, `Incentives.md`,
  `Governance.md`, `Security.md`, `Risks.md`, `Technology.md`, `Innovation.md`, `Ecosystem.md`, `Adoption.md`,
  `Community.md`, `Infrastructure.md`, `Metrics.md`, `Revenue.md`, **`DecisionEvent.md`, `Context.md`, `Hidden.md`**
- **Innovation:** `docs/Innovation/FirstMover.md`, `CategoryCreator.md`, `CompetitiveMoat.md`, `ProductMarketFit.md`, `Timing.md`
- **Patterns:** `docs/Patterns/Failure.md`, `Recovery.md`, `Narrative.md`, `Points.md`, `Liquidity.md`, `Growth.md`, `Ponzinomics.md`
- **Lifecycle:** `docs/TokenLifecycle/*` (Mainnet→PostTGE→Expansion→Maturity)
- **Market:** `docs/MarketBehaviour/Recovery.md`, `DeathSpiral.md`, `Distribution.md`, `UnlockImpact.md`; `docs/Meta/Narratives.md`, `Rotation.md`, `MarketCycles.md`
- **Valuation:** `docs/Valuation/Competitors.md`, `ComparableProjects.md`, `Revenue.md`, `TVL.md`
- **Reasoning:** `docs/Reasoning/Prediction.md`, `AnalogEngine.md`, `Confidence.md`, `Weighting.md`
- **Success:** `docs/Success/*`
- **Schema:** `docs/Schema/KnowledgeGraph.md`, `EntityRelationship.md`, `PatternSchema.md`
- **Cross-project analogs:** `examples/CaseStudies/Ethereum.md` (modular vs monolitik), `examples/Pioneer/Helium.md`
  (DePIN migrasi ke Solana), `examples/Pioneer/Optimism.md` & `Celestia.md` (rival modular), `examples/Pioneer/Lido.md`
  (analog sentralisasi liquid-staking ↔ Jito/Marinade)

## 26. Sources
_Deep Research provenance (Gemini), dua laporan digabung: v1 mengutip 85 referensi, v2 mengutip 34 referensi;
sumber primer/kunci di bawah._

**v1 (22-section, arsitektur/tokenomics/POV-matrix):**
- Solana: A new architecture for a high-performance blockchain (whitepaper v0.8.13) — solana.com — https://solana.com/solana-whitepaper.pdf
- Solana (blockchain platform) — Wikipedia — https://en.wikipedia.org/wiki/Solana_(blockchain_platform)
- A Complete History of Solana Outages: Causes, Fixes, and Lessons Learnt — Helius — https://www.helius.dev/blog/solana-outages-complete-history
- SIMD-0096: A Deep Dive into Solana's Fee Structure Overhaul — Medium — https://medium.com/@moonsimran/simd-0096-a-deep-dive-into-solanas-fee-structure-overhaul-8e51f3549042
- Solana validators to receive full priority fees as SIMD-0096 gains approval — The Block — https://www.theblock.co/post/296932/solana-validators-to-receive-full-priority-fees-as-simd-0096-proposal-gains-approval
- Solana's SIMD-228: what it is and why it's being debated — Oak Research — https://oakresearch.io/en/analyses/investigations/solana-simd-228-sol-what-it-is-and-why-being-debated-community
- What Is SIMD-123 And How Will It Change Institutional SOL Staking? — Blockdaemon — https://www.blockdaemon.com/blog/what-is-simd-123-and-how-will-it-change-institutional-sol-staking
- Solana Labs Completes a $314.15M Private Token Sale Led by a16z and Polychain — solana.com — https://solana.com/news/solana-labs-completes-a-314-15m-private-token-sale-led-by-andreessen-horowitz-and-polychain-capital
- Why is Jump Trading Group creating Firedancer? — Firedancer Docs — https://docs.firedancer.io/guide/firedancer.html
- Solana Tokenomics: Supply, Inflation, Staking & Fees — findas.org — https://www.findas.org/tokenomics-review/coins/the-tokenomics-of-solana-sol/r/7KPXo3rqeQKcMgVC72GUGu

**v2 (7-section, Causal Event Graph / Context Layer / Conflicting Evidence):**
- Solana Complaint (market-maker/disclosure lawsuit, 2022) — Traverse Legal — https://www.traverselegal.com/wp-content/uploads/2022/07/Mark-young-v-SOLANA-LABS-INC.pdf
- Solana Network Health Report: June 2025 — solana.com — https://solana.com/news/network-health-report-june-2025
- A Financial Institution's Guide to Solana — Sol Research Institute — https://solresearch.institute/posts/a-financial-institutions-guide-to-solana
- Solana Raises $1.76 Million in Sold Out CoinList Auction — solana.com — https://solana.com/news/solana-raises-1-76-million-in-sold-out-coinlist-auction
- Is Solana's inflation too high? — Helius — https://www.helius.dev/blog/solana-issuance-inflation-schedule
- What is Firedancer? A Deep Dive into Solana 2.0 — Helius — https://www.helius.dev/blog/what-is-firedancer
- Securing Solana: A Comprehensive Analysis of Past Security Incidents and Lessons Learnt — Medium — https://medium.com/@khaythefirst/securing-solana-a-comprehensive-analysis-of-past-security-incidents-and-lessons-learnt-26f6d1a79453
- Unveiling the Mammoth FTX Estate's Solana Stash — Binance Square — https://www.binance.com/en/square/post/26818039982874
- Solana Saga Only Lasted for Two Years Before Shutting Down — Moomoo — https://www.moomoo.com/news/post/60202434/solana-saga-only-lasted-for-two-years-before-shutting-down-can-seeker-who-has-now-fully-pivoted-avoid-the-same-fate

_(Bibliografi lengkap v1: 85 sumber; v2: 34 sumber — dipertahankan di file arsip `doc_backup/deep/`.)_
