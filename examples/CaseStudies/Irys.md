# Irys — Deep Case Study (Phased)

**CIF Dataset — Deep Dossier · Tier: Deep (anchor project)**
**Source:** Deep Research (DeepSeek), Format v3 Dependency Pipeline (10/11 phases: foundation, entity, history, technology, financial, token, ecosystem, market, behavioral, knowledge). **Auto-assembled** by `tools/ingest.py` (deterministic, no LLM, strict data_project/ contract) — each phase extracted and concatenated in dependency order per `docs/Protocol/Deep-Research-Brief.md`; the reasoning is the source reports'.
**Raw sources archived:** doc_backup/deep/Irys_foundation_2026-08.docx, doc_backup/deep/Irys_entity_2026-08.docx, doc_backup/deep/Irys_history_2026-08.docx, doc_backup/deep/Irys_technology_2026-08.docx, doc_backup/deep/Irys_financial_2026-08.docx, doc_backup/deep/Irys_token_2026-08.docx, doc_backup/deep/Irys_ecosystem_2026-08.docx, doc_backup/deep/Irys_market_2026-08.docx, doc_backup/deep/Irys_behavioral_2026-08.docx, doc_backup/deep/Irys_knowledge_2026-08.docx.
**Phases not run:** conflict.

> Faithful concatenation of phase outputs — no fabrication, no distillation beyond what the closing phase (Conflict Resolution / Validation) itself states. Consider a periodic QC pass.

---
## Foundation Intelligence
_ref: `docs/Ontology/Identity.md`, `docs/Ontology/Team.md`_

PROJECT: Irys
Official Name: Irys (dahulu Bundlr Network) (MEDIUM) [Blog Resmi Irys, https://blog.irys.xyz/introducing-irys]
Symbol: IRYS (MEDIUM) [Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics]
Category: Permanent data provenance layer / Layer 1 blockchain (MEDIUM) [Website Resmi, https://irys.xyz]
Founding Entity: Bundlr Labs, Inc. (MEDIUM) [Terms of Service Irys, https://irys.xyz/terms]
Founders: Josh Benaron (Co-founder & CEO) (MEDIUM) [Profil LinkedIn Josh Benaron, https://www.linkedin.com/in/joshbenaron]; Anggota pendiri lain: tidak diketahui
Core Team: tidak diungkap (MEDIUM) [Halaman Tim Irys, https://irys.xyz/team]
Country: Amerika Serikat (Global/Remote) (MEDIUM) [Terms of Service Irys, https://irys.xyz/terms]
Launch Date - Testnet: Januari 2024 (Incentivized Testnet Phase 1) (MEDIUM) [Blog Resmi Irys, https://blog.irys.xyz/irys-incentivized-testnet]
Launch Date - Mainnet: 26 Maret 2024 (Mainnet Launch) (HIGH) [Blog Resmi Irys, https://blog.irys.xyz/irys-mainnet-launch]
Launch Date - TGE: pre-TGE (MEDIUM) [Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics]
Main Products: Irys L1 (Layer 1 blockchain); Irys SDK; Provenance Layer; Irys Gateway (MEDIUM) [Dokumentasi Produk Irys, https://docs.irys.xyz]
Official Website: https://irys.xyz (HIGH) [Verifikasi DNS]
Repository: https://github.com/irys-xyz (HIGH) [Organisasi GitHub Resmi]
Documentation: https://docs.irys.xyz (HIGH) [Situs Dokumentasi Resmi]
Social - X/Twitter: @irys_xyz (HIGH) [Profil X Resmi, https://x.com/irys_xyz]
Social - Discord: https://discord.gg/irys (HIGH) [Tautan Undangan Resmi di Website]
Social - Telegram: @irys_xyz (MEDIUM) [Tautan Telegram di Footer Website]
Block Explorer: https://explorer.irys.xyz (HIGH) [Block Explorer Resmi]
Token Contract: belum di-deploy (pre-TGE) (MEDIUM) [Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics]
Chain(s): Irys (Native L1); Ethereum (Staking & Settlement); Arweave (Permanent Storage Layer) (MEDIUM) [Arsitektur Teknis Irys, https://docs.irys.xyz/architecture]
Ecosystem: Arweave; Ethereum; AI/Data Provenance; DePIN (MEDIUM) [Blog Ekosistem Irys, https://blog.irys.xyz/category/ecosystem]

## Entity Intelligence
_ref: `docs/Ontology/Relationships.md` (entity graph)_

PROJECT: Irys

Entity: Bundlr Labs, Inc.
Type: Company
Relationship: Entitas pendiri dan pengembang inti (core developer) protokol Irys, sebelumnya dikenal sebagai Bundlr Network, bertanggung jawab atas pengembangan Layer 1 blockchain Irys, SDK, dan lapisan provenance (HIGH)
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Terms of Service Irys, https://irys.xyz/terms]; (MEDIUM) [Blog Resmi Irys, https://blog.irys.xyz/introducing-irys]

---
Entity: Josh Benaron
Type: Person
Relationship: Co-founder dan CEO Bundlr Labs, Inc., memimpin visi dan eksekusi strategis proyek Irys sejak masa Bundlr Network (HIGH)
Period: 2021–sekarang
Exposure Type: leadership
Evidence: (HIGH) [Profil LinkedIn Josh Benaron, https://www.linkedin.com/in/joshbenaron]; (MEDIUM) [Blog Resmi Irys, https://blog.irys.xyz/introducing-irys]

---
Entity: Irys
Type: Protocol
Relationship: Protokol Layer 1 blockchain permanent data provenance layer yang dibangun oleh Bundlr Labs, menyediakan penyimpanan data permanen dengan bukti provenance terverifikasi on-chain (HIGH)
Period: 2024–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Website Resmi Irys, https://irys.xyz]; (HIGH) [Dokumentasi Arsitektur Irys, https://docs.irys.xyz/architecture]

---
Entity: Irys L1
Type: Protocol
Relationship: Blockchain Layer 1 native Irys yang berfungsi sebagai lapisan konsensus dan eksekusi untuk transaksi data dan provenance, menggantikan arsitektur bundler sebelumnya (HIGH)
Period: Maret 2024–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Blog Resmi Irys Mainnet Launch, https://blog.irys.xyz/irys-mainnet-launch]; (MEDIUM) [Dokumentasi Produk Irys, https://docs.irys.xyz]

---
Entity: Irys SDK
Type: Application
Relationship: Software Development Kit resmi untuk mengintegrasikan aplikasi ke jaringan Irys, memungkinkan developer mengunggah dan menandatangani data dengan provenance (HIGH)
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Dokumentasi SDK Irys, https://docs.irys.xyz/sdk]; (MEDIUM) [Repositori GitHub Irys, https://github.com/irys-xyz]

---
Entity: Irys Gateway
Type: Infrastructure
Relationship: Gateway/http gateway resmi untuk mengakses dan mengambil data dari jaringan Irys, menyediakan antarmuka retrieval data permanen (HIGH)
Period: 2024–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Dokumentasi Produk Irys, https://docs.irys.xyz]; (HIGH) [Website Resmi Irys, https://irys.xyz]

---
Entity: Arweave
Type: Protocol
Relationship: Lapisan penyimpanan permanen (permanent storage layer) yang digunakan Irys untuk menyimpan data blob secara permanen, fondasi data availability Irys (HIGH)
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Arsitektur Teknis Irys, https://docs.irys.xyz/architecture]; (HIGH) [Blog Ekosistem Irys, https://blog.irys.xyz/category/ecosystem]

---
Entity: Ethereum
Type: Chain
Relationship: Chain settlement dan staking untuk token IRYS, serta lapisan keamanan ekonomi untuk validator Irys melalui restaking/mekanisme staking (HIGH)
Period: 2024–sekarang
Exposure Type: financial-collateral
Evidence: (MEDIUM) [Arsitektur Teknis Irys, https://docs.irys.xyz/architecture]; (MEDIUM) [Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics]

---
Entity: IRYS (Token)
Type: Protocol
Relationship: Token utilitas dan governance native jaringan Irys, digunakan untuk pembayaran storage, staking validator, dan governance protokol (pre-TGE per dokumentasi) (HIGH)
Period: 2024–sekarang
Exposure Type: financial-collateral
Evidence: (MEDIUM) [Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics]; (HIGH) [Blog Resmi Irys, https://blog.irys.xyz/introducing-irys]

---
Entity: Irys Incentivized Testnet
Type: Protocol
Relationship: Program testnet berinsentif (Phase 1 Januari 2024) untuk menguji ekonomi token, performa validator, dan provenance layer sebelum mainnet (HIGH)
Period: Januari 2024–Maret 2024
Exposure Type: technical-integration
Evidence: (HIGH) [Blog Resmi Irys Testnet, https://blog.irys.xyz/irys-incentivized-testnet]; (MEDIUM) [Dokumentasi Irys, https://docs.irys.xyz]

---
Entity: Irys Explorer
Type: Application
Relationship: Block explorer resmi jaringan Irys untuk memverifikasi transaksi, blok, akun, dan bukti provenance on-chain (HIGH)
Period: Maret 2024–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Block Explorer Resmi, https://explorer.irys.xyz]; (MEDIUM) [Website Resmi Irys, https://irys.xyz]

---
Entity: Irys Documentation (docs.irys.xyz)
Type: Application
Relationship: Portal dokumentasi teknis resmi untuk developer, validator, dan pengguna protokol Irys (HIGH)
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Dokumentasi Resmi, https://docs.irys.xyz]; (HIGH) [Website Resmi Irys, https://irys.xyz]

---
Entity: Irys GitHub Organization (irys-xyz)
Type: Organization
Relationship: Repositori kode sumber terbuka (open-source) untuk protokol Irys, SDK, CLI, dan tooling terkait (HIGH)
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Organisasi GitHub Resmi, https://github.com/irys-xyz]; (MEDIUM) [Website Resmi Irys, https://irys.xyz]

---
Entity: Irys Discord Community
Type: Community
Relationship: Komunitas resmi diskusi, dukungan, dan koordinasi validator/developer/user protokol Irys (HIGH)
Period: 2023–sekarang
Exposure Type: narrative-correlated-only
Evidence: (HIGH) [Tautan Undangan Resmi di Website, https://irys.xyz]; (MEDIUM) [Discord Irys, https://discord.gg/irys]

---
Entity: Irys X/Twitter (@irys_xyz)
Type: Media
Relationship: Saluran komunikasi resmi (official announcement channel) untuk pengumuman produk, upgrade, dan ekosistem Irys (HIGH)
Period: 2023–sekarang
Exposure Type: narrative-correlated-only
Evidence: (HIGH) [Profil X Resmi, https://x.com/irys_xyz]; (HIGH) [Website Resmi Irys, https://irys.xyz]

---
Entity: Irys Telegram (@irys_xyz)
Type: Media
Relationship: Saluran komunitas tambahan untuk pengumuman dan diskusi cepat terkait protokol Irys (MEDIUM)
Period: 2023–sekarang
Exposure Type: narrative-correlated-only
Evidence: (MEDIUM) [Tautan Telegram di Footer Website, https://irys.xyz]; (LOW) [Telegram Irys, https://t.me/irys_xyz]

---
Entity: Irys Blog (blog.irys.xyz)
Type: Media
Relationship: Platform publikasi resmi artikel teknis, pengumuman rilis (testnet, mainnet), tokenomics, dan update ekosistem (HIGH)
Period: 2023–sekarang
Exposure Type: narrative-correlated-only
Evidence: (HIGH) [Blog Resmi Irys, https://blog.irys.xyz]; (HIGH) [Website Resmi Irys, https://irys.xyz]

---
Entity: Provenance Layer
Type: Protocol
Relationship: Lapisan protokol inti Irys yang menyediakan bukti kriptografis asal-usul dan integritas data (provenance) terverifikasi on-chain (HIGH)
Period: 2024–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Website Resmi Irys, https://irys.xyz]; (MEDIUM) [Dokumentasi Arsitektur Irys, https://docs.irys.xyz/architecture]

---
Entity: Bundlr Network (Legacy)
Type: Protocol
Relationship: Nama dan arsitektur protokol sebelumnya (bundler service untuk Arweave) yang direbrand dan diupgrade menjadi Irys L1 (HIGH)
Period: 2021–2024
Exposure Type: technical-integration
Evidence: (HIGH) [Blog Resmi Rebranding, https://blog.irys.xyz/introducing-irys]; (MEDIUM) [Terms of Service Irys, https://irys.xyz/terms]

---
Entity: Irys Terms of Service / Legal Entity
Type: Organization
Relationship: Kerangka hukum operasional (Terms of Service) yang mengikat pengguna dan validator pada entitas Bundlr Labs, Inc. (HIGH)
Period: 2024–sekarang
Exposure Type: unknown
Evidence: (HIGH) [Terms of Service Irys, https://irys.xyz/terms]; (MEDIUM) [Website Resmi Irys, https://irys.xyz]

---
Entity: AI / Data Provenance Ecosystem
Type: Other
Relationship: Kategori naratif dan pasar sasaran utama Irys (AI training data provenance, DePIN, permanent data) yang menarik mitra dan adopsi (MEDIUM)
Period: 2024–sekarang
Exposure Type: narrative-correlated-only
Evidence: (MEDIUM) [Blog Ekosistem Irys, https://blog.irys.xyz/category/ecosystem]; (HIGH) [Website Resmi Irys, https://irys.xyz]

---
Entity: DePIN Ecosystem Partners
Type: Other
Relationship: Kategori mitra ekosistem Decentralized Physical Infrastructure Networks yang terintegrasi atau membangun di atas Irys untuk provenance data sensor/fisik (MEDIUM)
Period: 2024–sekarang
Exposure Type: narrative-correlated-only
Evidence: (MEDIUM) [Blog Ekosistem Irys, https://blog.irys.xyz/category/ecosystem]; (LOW) [Website Resmi Irys, https://irys.xyz]

---

PERSON
Josh Benaron

FOUNDATION
(tidak ada entitas foundation teridentifikasi)

COMPANY
Bundlr Labs, Inc.

PROTOCOL
Irys
Irys L1
IRYS (Token)
Irys Incentivized Testnet
Provenance Layer
Bundlr Network (Legacy)
Arweave

CHAIN
Ethereum
Irys (Native L1)

INVESTOR
(tidak ada entitas investor teridentifikasi publik dari sumber primer)

INFRASTRUCTURE
Irys Gateway
Arweave

APPLICATION
Irys SDK
Irys Explorer
Irys Documentation (docs.irys.xyz)
Irys GitHub Organization (irys-xyz)

SECURITY
(tidak ada entitas auditor/security firm teridentifikasi publik dari sumber primer)

DAO
(tidak ada entitas DAO teridentifikasi publik dari sumber primer)

GOVERNMENT
(tidak ada entitas pemerintah/regulator teridentifikasi)

MEDIA
Irys X/Twitter (@irys_xyz)
Irys Telegram (@irys_xyz)
Irys Blog (blog.irys.xyz)

COMMUNITY
Irys Discord Community

OTHER
AI / Data Provenance Ecosystem
DePIN Ecosystem Partners
Irys Terms of Service / Legal Entity

---

Total Entity: 23
Internal: 10
External: 11
Unknown: 2

---

## Historical Intelligence
_ref: `docs/Ontology/DecisionEvent.md` (factual spine — enriched later by Behavioral)_

PROJECT: Irys

Event ID

EV-001

Date

2021

Event Name

Pendirian Bundlr Labs, Inc. dan Peluncuran Bundlr Network

Event Type

Founding

Description

Bundlr Labs, Inc. didirikan dan meluncurkan Bundlr Network sebagai layanan bundler untuk Arweave, memungkinkan pembayaran storage menggunakan berbagai token bukan hanya AR.

Participants

Bundlr Labs, Inc.; Josh Benaron; Arweave

Location

Amerika Serikat (Global/Remote)

Status

Completed

Immediate Result

Entitas perusahaan dan protokol bundler awal beroperasi, menjadi lapisan penyederhanaan akses ke penyimpanan permanen Arweave.

Sources

https://irys.xyz/terms
https://blog.irys.xyz/introducing-irys
https://docs.irys.xyz/architecture

---

Event ID

EV-002

Date

2021

Event Name

Integrasi Bundlr Network dengan Arweave sebagai Permanent Storage Layer

Event Type

Integration

Description

Bundlr Network mulai menggunakan Arweave sebagai lapisan penyimpanan permanen (permanent storage layer) untuk data blob yang dibundel.

Participants

Bundlr Network (Legacy); Arweave

Location

On-chain (Arweave)

Status

Completed

Immediate Result

Arweave menjadi fondasi data availability untuk protokol Bundlr, memungkinkan penyimpanan permanen terdesentralisasi.

Sources

https://docs.irys.xyz/architecture
https://blog.irys.xyz/category/ecosystem

---

Event ID

EV-003

Date

2023

Event Name

Peluncuran Irys SDK, Dokumentasi, GitHub Organization, dan Saluran Komunitas

Event Type

Product

Description

Dirilisnya Irys SDK untuk developer, portal dokumentasi teknis (docs.irys.xyz), organisasi GitHub resmi (irys-xyz), serta saluran komunitas Discord, X/Twitter, Telegram, dan Blog resmi.

Participants

Irys SDK; Irys Documentation (docs.irys.xyz); Irys GitHub Organization (irys-xyz); Irys Discord Community; Irys X/Twitter (@irys_xyz); Irys Telegram (@irys_xyz); Irys Blog (blog.irys.xyz)

Location

Online (GitHub, docs.irys.xyz, Discord, X, Telegram, blog.irys.xyz)

Status

Completed

Immediate Result

Infrastruktur pengembangan, dokumentasi, dan komunitas resmi tersedia untuk ekosistem awal sebelum mainnet.

Sources

https://docs.irys.xyz/sdk
https://docs.irys.xyz
https://github.com/irys-xyz
https://discord.gg/irys
https://x.com/irys_xyz
https://t.me/irys_xyz
https://blog.irys.xyz

---

Event ID

EV-004

Date

2024-01

Event Name

Peluncuran Irys Incentivized Testnet Phase 1

Event Type

Launch

Description

Program testnet berinsentif Phase 1 dimulai untuk menguji ekonomi token, performa validator, dan lapisan provenance sebelum mainnet.

Participants

Irys Incentivized Testnet; Irys L1; IRYS (Token)

Location

Testnet Irys

Status

Completed

Immediate Result

Validator dan pengguna mulai menguji jaringan, ekonomi token, dan fitur provenance pada lingkungan testnet berinsentif.

Sources

https://blog.irys.xyz/irys-incentivized-testnet
https://docs.irys.xyz

---

Event ID

EV-005

Date

2024-03

Event Name

Pengumuman Rebranding dari Bundlr Network ke Irys

Event Type

Other

Description

Proyek secara resmi mengumumkan rebranding dari Bundlr Network menjadi Irys, mencerminkan evolusi dari bundler service ke Layer 1 blockchain provenance layer.

Participants

Bundlr Labs, Inc.; Bundlr Network (Legacy); Irys; Irys Blog (blog.irys.xyz)

Location

Online (blog.irys.xyz)

Status

Completed

Immediate Result

Identitas baru "Irys" diperkenalkan secara publik, menandai transisi arsitektur dan posisining pasar.

Sources

https://blog.irys.xyz/introducing-irys
https://irys.xyz/terms

---

Event ID

EV-006

Date

2024-03-26

Event Name

Peluncuran Irys Mainnet dan Irys L1

Event Type

Launch

Description

Mainnet Irys secara resmi diluncurkan pada 26 Maret 2024, mengaktifkan Irys L1 sebagai blockchain Layer 1 native untuk konsensus dan eksekusi transaksi data serta provenance.

Participants

Irys; Irys L1; Bundlr Labs, Inc.; Josh Benaron

Location

Mainnet Irys (Native L1)

Status

Completed

Immediate Result

Jaringan produksi Irys L1 live, memungkinkan transaksi data, provenance on-chain, dan operasi validator pada mainnet.

Sources

https://blog.irys.xyz/irys-mainnet-launch
https://irys.xyz
https://explorer.irys.xyz

---

Event ID

EV-007

Date

2024-03

Event Name

Peluncuran Irys Explorer (Block Explorer Resmi)

Event Type

Infrastructure

Description

Block explorer resmi (explorer.irys.xyz) diluncurkan seiring mainnet untuk verifikasi transaksi, blok, akun, dan bukti provenance on-chain.

Participants

Irys Explorer; Irys L1

Location

https://explorer.irys.xyz

Status

Completed

Immediate Result

Pengguna dan validator dapat memverifikasi state jaringan, transaksi, dan provenance melalui antarmuka explorer resmi.

Sources

https://explorer.irys.xyz
https://irys.xyz

---

Event ID

EV-008

Date

2024-03

Event Name

Aktivasi Irys Gateway dan Provenance Layer pada Mainnet

Event Type

Infrastructure

Description

Irys Gateway (HTTP gateway untuk retrieval data) dan Provenance Layer (lapisan bukti kriptografis asal-usul data) diaktifkan pada mainnet.

Participants

Irys Gateway; Provenance Layer; Irys L1

Location

Mainnet Irys

Status

Completed

Immediate Result

Layanan retrieval data permanen dan verifikasi provenance tersedia untuk developer dan aplikasi di mainnet.

Sources

https://docs.irys.xyz
https://irys.xyz
https://docs.irys.xyz/architecture

---

Event ID

EV-009

Date

2024

Event Name

Integrasi Ethereum sebagai Settlement dan Staking Layer untuk Token IRYS

Event Type

Integration

Description

Ethereum ditetapkan sebagai chain settlement dan staking untuk token IRYS, serta lapisan keamanan ekonomi validator melalui mekanisme staking/restaking.

Participants

Ethereum; IRYS (Token); Irys L1

Location

Ethereum Mainnet; Irys L1

Status

Ongoing

Immediate Result

Arsitektur cross-chain antara Irys L1 dan Ethereum untuk keamanan ekonomi dan utility token IRYS ditetapkan.

Sources

https://docs.irys.xyz/architecture
https://docs.irys.xyz/tokenomics

---

Event ID

EV-010

Date

2024

Event Name

Publikasi Tokenomics IRYS (Pre-TGE)

Event Type

Token

Description

Dokumentasi tokenomics IRYS dipublikasikan di docs.irys.xyz/tokenomics, menggariskan alokasi, utilitas (storage payment, staking, governance), dan status pre-TGE.

Participants

IRYS (Token); Irys Documentation (docs.irys.xyz)

Location

https://docs.irys.xyz/tokenomics

Status

Ongoing

Immediate Result

Kerangka ekonomi token IRYS terpublikasi, memberikan transparansi awal terkait utilitas dan alokasi sebelum TGE.

Sources

https://docs.irys.xyz/tokenomics
https://blog.irys.xyz/introducing-irys

---

## KELOMPOKKAN BERDASARKAN TAHUN

### 2021
- EV-001: Pendirian Bundlr Labs, Inc. dan Peluncuran Bundlr Network (Founding)
- EV-002: Integrasi Bundlr Network dengan Arweave sebagai Permanent Storage Layer (Integration)

### 2023
- EV-003: Peluncuran Irys SDK, Dokumentasi, GitHub Organization, dan Saluran Komunitas (Product)

### 2024
- EV-004: Peluncuran Irys Incentivized Testnet Phase 1 (Launch)
- EV-005: Pengumuman Rebranding dari Bundlr Network ke Irys (Other)
- EV-006: Peluncuran Irys Mainnet dan Irys L1 (Launch)
- EV-007: Peluncuran Irys Explorer (Block Explorer Resmi) (Infrastructure)
- EV-008: Aktivasi Irys Gateway dan Provenance Layer pada Mainnet (Infrastructure)
- EV-009: Integrasi Ethereum sebagai Settlement dan Staking Layer untuk Token IRYS (Integration)
- EV-010: Publikasi Tokenomics IRYS (Pre-TGE) (Token)

## RINGKASAN

Total Events: 10

Founding: 1
Funding: 0
Technology: 0
Security: 0
Governance: 0
Legal: 0
Market: 0
Other: 9
 - Launch: 3
 - Integration: 2
 - Product: 1
 - Infrastructure: 2
 - Token: 1
 - Other: 1

## Technology Intelligence
_ref: `docs/Ontology/Technology.md`_

PROJECT: Irys

## System Architecture
Architecture Type: Layer 1 blockchain (native L1) dengan modular provenance layer dan integrasi cross-chain ke Ethereum serta Arweave (HIGH) [Dokumentasi Arsitektur Irys, https://docs.irys.xyz/architecture]
Storage Layer: Arweave (permanent storage layer untuk data blob) (HIGH) [Dokumentasi Arsitektur Irys, https://docs.irys.xyz/architecture]
Settlement Layer: Ethereum (staking, settlement, keamanan ekonomi validator) (HIGH) [Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics]
Provenance Layer: Lapisan native on-chain untuk bukti kriptografis asal-usul dan integritas data (HIGH) [Website Resmi Irys, https://irys.xyz]
Gateway Layer: HTTP gateway (Irys Gateway) untuk retrieval data permanen (HIGH) [Dokumentasi Produk Irys, https://docs.irys.xyz]
Cross-chain Messaging: Tidak terdokumentasi secara eksplisit sebagai messaging layer terpisah; integrasi Ethereum untuk staking/settlement (MEDIUM) [Dokumentasi Arsitektur Irys, https://docs.irys.xyz/architecture]

## Core Components
- Nama: Irys L1 (Validator/Consensus Layer)
 Fungsi: Blockchain Layer 1 native untuk konsensus, eksekusi transaksi data, dan provenance on-chain (HIGH) [Blog Mainnet Launch, https://blog.irys.xyz/irys-mainnet-launch]
 Status: Live (Mainnet sejak 26 Maret 2024) (HIGH) [Block Explorer Resmi, https://explorer.irys.xyz]

- Nama: Provenance Layer
 Fungsi: Menyediakan bukti kriptografis (provenance) asal-usul, timestamp, dan integritas data yang terverifikasi on-chain (HIGH) [Website Resmi Irys, https://irys.xyz]
 Status: Live pada Mainnet (HIGH) [Dokumentasi Arsitektur Irys, https://docs.irys.xyz/architecture]

- Nama: Irys Gateway
 Fungsi: HTTP gateway resmi untuk retrieval dan akses data permanen dari jaringan Irys (HIGH) [Dokumentasi Produk Irys, https://docs.irys.xyz]
 Status: Live pada Mainnet (HIGH) [Website Resmi Irys, https://irys.xyz]

- Nama: Irys SDK
 Fungsi: Software Development Kit untuk developer mengintegrasikan aplikasi, mengunggah data, menandatangani transaksi provenance (HIGH) [Dokumentasi SDK Irys, https://docs.irys.xyz/sdk]
 Status: Tersedia (pre-mainnet dan mainnet) (HIGH) [Repositori GitHub Irys, https://github.com/irys-xyz]

- Nama: Irys Explorer
 Fungsi: Block explorer resmi untuk verifikasi transaksi, blok, akun, dan bukti provenance (HIGH) [Block Explorer Resmi, https://explorer.irys.xyz]
 Status: Live (Mainnet) (HIGH) [Website Resmi Irys, https://irys.xyz]

- Nama: Arweave Integration (Storage Layer)
 Fungsi: Permanent storage layer untuk data blob yang dibundel oleh Irys (HIGH) [Dokumentasi Arsitektur Irys, https://docs.irys.xyz/architecture]
 Status: Operational (sejak era Bundlr Network 2021) (HIGH) [Blog Ekosistem Irys, https://blog.irys.xyz/category/ecosystem]

- Nama: Ethereum Staking/Settlement Contracts
 Fungsi: Smart contracts di Ethereum untuk staking token IRYS, validator registration, dan settlement ekonomi (MEDIUM) [Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics]
 Status: Pre-TGE / Tidak diketahui detail deploy (MEDIUM) [Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics]

## Consensus Mechanism
Consensus Type: Tidak terdokumentasi secara detail di sumber primer (whitepaper/research paper belum dipublikasikan) (MEDIUM) [Dokumentasi Arsitektur Irys, https://docs.irys.xyz/architecture]
Validator Selection: Berbasis staking token IRYS di Ethereum (economic security via Ethereum) (MEDIUM) [Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics]
Finality: Tidak diketahui (tidak terdokumentasi) (LOW) [Tidak ada sumber primer]
Block Time: Tidak diketahui (tidak terdokumentasi) (LOW) [Tidak ada sumber primer]
Sybil Resistance: Token-weighted staking (IRYS) pada Ethereum (MEDIUM) [Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics]

## Execution Environment
Execution Environment: Tidak diketahui secara eksplisit (EVM-compatible, WASM, SVM, atau custom VM tidak terdokumentasi di docs primer) (LOW) [Dokumentasi Arsitektur Irys, https://docs.irys.xyz/architecture]
Smart Contract Support: Tidak diketahui apakah mendukung smart contract umum atau hanya transaksi data/provenance (LOW) [Tidak ada sumber primer]
Transaction Types: Data transactions, provenance signing, storage payments (HIGH) [Dokumentasi SDK Irys, https://docs.irys.xyz/sdk]

## Programming Languages
Core Protocol (Node/Validator): Tidak diketahui (repositori GitHub irys-xyz berisi multiple repos, bahasa dominan tidak diverifikasi dari README utama) (LOW) [Organisasi GitHub Irys, https://github.com/irys-xyz]
SDK/Client: TypeScript/JavaScript (Irys SDK utama) (HIGH) [Dokumentasi SDK Irys, https://docs.irys.xyz/sdk]
CLI/Tooling: TypeScript/JavaScript (berbasis Node.js) (HIGH) [Repositori GitHub Irys, https://github.com/irys-xyz]
Smart Contracts (Ethereum side): Solidity (untuk staking/settlement contracts di Ethereum) (MEDIUM) [Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics]

## Development Framework
SDK: Irys SDK (TypeScript/JavaScript) untuk browser dan Node.js (HIGH) [Dokumentasi SDK Irys, https://docs.irys.xyz/sdk]
CLI: Irys CLI (bundled dalam SDK/repo terpisah) untuk deployment dan interaction (HIGH) [Repositori GitHub Irys, https://github.com/irys-xyz]
API: HTTP REST API via Irys Gateway untuk data retrieval (HIGH) [Dokumentasi Produk Irys, https://docs.irys.xyz]
Testing Framework: Tidak terdokumentasi resmi (LOW) [Tidak ada sumber primer]
Deployment Tooling: Tidak terdokumentasi resmi (LOW) [Tidak ada sumber primer]

## Security Model
Validator Security: Proof-of-Stake berbasis token IRYS di-stake di Ethereum (economic security dari Ethereum) (MEDIUM) [Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics]
Data Integrity: Provenance Layer menyediakan bukti kriptografis (merkle proofs, timestamps) on-chain (HIGH) [Website Resmi Irys, https://irys.xyz]
Storage Permanence: Data blob disimpan permanen di Arweave (replicated, immutable) (HIGH) [Dokumentasi Arsitektur Irys, https://docs.irys.xyz/architecture]
Gateway Security: HTTPS/TLS untuk retrieval; verifikasi provenance via explorer (HIGH) [Block Explorer Resmi, https://explorer.irys.xyz]
Slashing/Conditions: Tidak terdokumentasi detail slashing conditions untuk validator Irys L1 (LOW) [Tidak ada sumber primer]
Audit Status: Tidak ditemukan laporan audit resmi dipublikasikan di website/docs (LOW) [Website Resmi Irys, https://irys.xyz; Dokumentasi Irys, https://docs.irys.xyz]

## Audit History
Tidak ditemukan riwayat audit keamanan (smart contract, consensus, cryptography) yang dipublikasikan secara resmi di website, blog, atau dokumentasi Irys per tanggal cut-off pengetahuan (LOW) [Website Resmi Irys, https://irys.xyz; Blog Resmi Irys, https://blog.irys.xyz; Dokumentasi Irys, https://docs.irys.xyz]

## Technical Upgrade History
- Tanggal: 2024-03-26
 Nama Upgrade: Irys Mainnet Launch (v1.0 / Genesis)
 Deskripsi Singkat: Peluncuran Irys L1 mainnet, aktivasi validator, provenance layer, gateway, dan explorer
 Status: Completed (HIGH) [Blog Mainnet Launch, https://blog.irys.xyz/irys-mainnet-launch]

- Tanggal: 2024-01
 Nama Upgrade: Irys Incentivized Testnet Phase 1
 Deskripsi Singkat: Testnet berinsentif untuk menguji ekonomi token, performa validator, provenance layer
 Status: Completed (HIGH) [Blog Testnet, https://blog.irys.xyz/irys-incentivized-testnet]

- Tanggal: 2024-03 (sebelum mainnet)
 Nama Upgrade: Rebranding Bundlr Network → Irys (Arsitektur Upgrade)
 Deskripsi Singkat: Transisi dari bundler service (Bundlr) ke Layer 1 blockchain native (Irys L1) dengan provenance layer
 Status: Completed (HIGH) [Blog Rebranding, https://blog.irys.xyz/introducing-irys]

## Current Technical Stack
Blockchain Framework: Custom L1 (tidak berbasis Cosmos SDK, Substrate, atau OP Stack secara eksplisit terdokumentasi) (LOW) [Dokumentasi Arsitektur Irys, https://docs.irys.xyz/architecture]
Consensus Library: Tidak diketahui (LOW) [Tidak ada sumber primer]
P2P Networking: Tidak diketahui (libp2p, custom, dll.) (LOW) [Tidak ada sumber primer]
Cryptography: Tidak diketahui detail library (BLS, ECDSA, Merkle trees untuk provenance) (LOW) [Tidak ada sumber primer]
Storage Integration: Arweave (via bundler/transaction submission ke Arweave) (HIGH) [Dokumentasi Arsitektur Irys, https://docs.irys.xyz/architecture]
Ethereum Integration: Solidity smart contracts untuk staking/settlement; EVM RPC untuk interaction (MEDIUM) [Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics]
SDK Language: TypeScript/JavaScript (Node.js, Browser) (HIGH) [Dokumentasi SDK Irys, https://docs.irys.xyz/sdk]
Gateway/Indexer: Custom HTTP Gateway (Irys Gateway) + Indexer untuk explorer (HIGH) [Dokumentasi Produk Irys, https://docs.irys.xyz]
Infrastructure: Docker/Kubernetes (asumsi standar deployment, tidak terdokumentasi eksplisit) (LOW) [Tidak ada sumber primer]
Monitoring/Observability: Tidak terdokumentasi (LOW) [Tidak ada sumber primer]

## Known Technical Limitations
Throughput/Latency: Tidak dipublikasikan angka TPS, block time, atau latency resmi (LOW) [Tidak ada sumber primer]
Smart Contract Generality: Tidak diketahui apakah Irys L1 mendukung general-purpose smart contracts atau hanya transaksi data/provenance spesifik (LOW) [Tidak ada sumber primer]
Validator Hardware Requirements: Tidak dipublikasikan spesifikasi minimum hardware untuk menjalankan validator node (LOW) [Tidak ada sumber primer]
Cross-chain Interoperability: Hanya terdokumentasi integrasi Ethereum (staking/settlement) dan Arweave (storage); bridge/messaging ke chain lain tidak terdokumentasi (MEDIUM) [Dokumentasi Arsitektur Irys, https://docs.irys.xyz/architecture]
Token Contract Deploy: Token IRYS contract di Ethereum belum di-deploy/verified secara publik (pre-TGE) (MEDIUM) [Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics]
Audit Coverage: Tidak ada laporan audit keamanan publik untuk consensus, cryptography, atau smart contracts (LOW) [Website Resmi Irys, https://irys.xyz]

## Official Technical Resources
Documentation: https://docs.irys.xyz
GitHub Organization: https://github.com/irys-xyz
Developer Docs (SDK): https://docs.irys.xyz/sdk
API Reference (Gateway): https://docs.irys.xyz (bagian Gateway/API)
Whitepaper: Tidak tersedia (tidak ditemukan di website/docs resmi) (LOW) [Website Resmi Irys, https://irys.xyz]
Research Papers: Tidak tersedia (tidak ditemukan di website/docs resmi) (LOW) [Blog Resmi Irys, https://blog.irys.xyz]
Block Explorer: https://explorer.irys.xyz
Gateway Endpoint: Tidak dipublikasikan URL endpoint spesifik di docs utama (menggunakan domain gateway.irys.xyz atau serupa) (MEDIUM) [Dokumentasi Produk Irys, https://docs.irys.xyz]

## RINGKASAN
Architecture: Layer 1 blockchain (native) dengan modular Provenance Layer, menggunakan Arweave sebagai permanent storage layer dan Ethereum sebagai settlement/staking layer
Core Components: 7 komponen utama (Irys L1 Validator, Provenance Layer, Irys Gateway, Irys SDK, Irys Explorer, Arweave Integration, Ethereum Staking Contracts)
Audit Count: 0 (tidak ditemukan audit publik)
Major Upgrade Count: 3 (Mainnet Launch Mar 2024, Incentivized Testnet Jan 2024, Rebranding/Arsitektur Upgrade Mar 2024)

## Financial Intelligence
_ref: `docs/Ontology/Funding.md`, `docs/Ontology/Revenue.md`_

PROJECT: Irys

## Funding History
- Funding Round: Tidak diungkap (LOW) [Website Resmi Irys, https://irys.xyz]
- Date: Tidak diungkap (LOW) [Blog Resmi Irys, https://blog.irys.xyz]
- Amount: Tidak diungkap (LOW) [Dokumentasi Irys, https://docs.irys.xyz]
- Currency: Tidak diungkap (LOW) [Terms of Service Irys, https://irys.xyz/terms]
- Lead Investor: Tidak diungkap (LOW) [Blog Resmi Irys, https://blog.irys.xyz]
- Participating Investors: Tidak diungkap (LOW) [Dokumentasi Irys, https://docs.irys.xyz]
- Valuation: Tidak diungkap (LOW) [Website Resmi Irys, https://irys.xyz]
- Funding Type: Tidak diungkap (LOW) [Blog Resmi Irys, https://blog.irys.xyz]
- Status: Tidak diungkap (LOW) [Dokumentasi Irys, https://docs.irys.xyz]
- Sources: https://irys.xyz; https://blog.irys.xyz; https://docs.irys.xyz; https://irys.xyz/terms

## Treasury
- Current Treasury Size: Tidak diungkap (LOW) [Website Resmi Irys, https://irys.xyz]
- Treasury Composition: Tidak diungkap (LOW) [Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics]
- Stablecoin Holdings: Tidak diungkap (LOW) [Blog Resmi Irys, https://blog.irys.xyz]
- Native Token Holdings: Tidak diungkap (LOW) [Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics]
- Other Assets: Tidak diungkap (LOW) [Website Resmi Irys, https://irys.xyz]
- Treasury Custodian: Tidak diungkap (LOW) [Terms of Service Irys, https://irys.xyz/terms]
- Sources: https://irys.xyz; https://docs.irys.xyz/tokenomics; https://blog.irys.xyz; https://irys.xyz/terms

## Revenue Model
- Nama: Protocol Fees (Storage Payments) (MEDIUM) [Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics]
 Status: Planned (Pre-TGE) (MEDIUM) [Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics]
 Sources: https://docs.irys.xyz/tokenomics
- Nama: Staking Fees / Validator Rewards (MEDIUM) [Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics]
 Status: Planned (Pre-TGE) (MEDIUM) [Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics]
 Sources: https://docs.irys.xyz/tokenomics
- Nama: Governance Fees (MEDIUM) [Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics]
 Status: Planned (Pre-TGE) (MEDIUM) [Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics]
 Sources: https://docs.irys.xyz/tokenomics

## Revenue History
- Tidak diungkap (LOW) [Website Resmi Irys, https://irys.xyz]
- Sources: https://irys.xyz; https://blog.irys.xyz; https://docs.irys.xyz

## Fundraising Mechanism
- Mechanism: Tidak diungkap (LOW) [Website Resmi Irys, https://irys.xyz]
- Sources: https://irys.xyz; https://blog.irys.xyz; https://docs.irys.xyz

## Token Sale
- Private Sale: Tidak diungkap (LOW) [Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics]
- Public Sale: Tidak diungkap (LOW) [Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics]
- Launchpad: Tidak diungkap (LOW) [Blog Resmi Irys, https://blog.irys.xyz]
- Auction: Tidak diungkap (LOW) [Website Resmi Irys, https://irys.xyz]
- Community Sale: Tidak diungkap (LOW) [Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics]
- Tanggal: Pre-TGE (belum terjadwal resmi) (MEDIUM) [Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics]
- Status: Pre-TGE (MEDIUM) [Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics]
- Sources: https://docs.irys.xyz/tokenomics; https://blog.irys.xyz; https://irys.xyz

## Financial Dependencies
- Primary Funding Source: Tidak diungkap (LOW) [Website Resmi Irys, https://irys.xyz]
- Sources: https://irys.xyz; https://blog.irys.xyz; https://docs.irys.xyz

## Financial Risk
- Treasury Concentration: Tidak diungkap (LOW) [Website Resmi Irys, https://irys.xyz]
- Revenue Decline: Tidak diungkap (LOW) [Blog Resmi Irys, https://blog.irys.xyz]
- Funding Dependency: Tidak diungkap (LOW) [Dokumentasi Irys, https://docs.irys.xyz]
- Debt: Tidak diungkap (LOW) [Terms of Service Irys, https://irys.xyz/terms]
- Legal Financial Risk: Tidak diungkap (LOW) [Terms of Service Irys, https://irys.xyz/terms]
- Sources: https://irys.xyz; https://blog.irys.xyz; https://docs.irys.xyz; https://irys.xyz/terms

## Official Financial Resources
- Official Blog: https://blog.irys.xyz
- Transparency Report: Tidak tersedia (LOW) [Website Resmi Irys, https://irys.xyz]
- Treasury Dashboard: Tidak tersedia (LOW) [Website Resmi Irys, https://irys.xyz]
- Governance: Tidak tersedia (LOW) [Website Resmi Irys, https://irys.xyz]
- Messari: Tidak tersedia (LOW) [Messari, https://messari.io]
- Token Terminal: Tidak tersedia (LOW) [Token Terminal, https://tokenterminal.com]
- DefiLlama: Tidak tersedia (LOW) [DefiLlama, https://defillama.com]
- CryptoRank: Tidak tersedia (LOW) [CryptoRank, https://cryptorank.io]
- Whitepaper: Tidak tersedia (LOW) [Website Resmi Irys, https://irys.xyz]
- Sources: https://irys.xyz; https://blog.irys.xyz; https://docs.irys.xyz

## RINGKASAN
- Total Funding Raised: Tidak diungkap
- Funding Rounds: 0 (tidak diungkap)
- Treasury Status: Tidak diungkap
- Revenue Sources: Protocol Fees (Storage Payments), Staking Fees, Governance Fees (semua Planned/Pre-TGE)
- Revenue Availability: Tidak diungkap

## Token Intelligence
_ref: `docs/Ontology/Tokenomics.md`_

PROJECT: Irys

## Token Information
Official Token Name: IRYS (MEDIUM) [Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics]
Symbol: IRYS (MEDIUM) [Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics]
Token Standard: ERC-20 (direncanakan di Ethereum) (MEDIUM) [Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics; Dokumentasi Arsitektur Irys, https://docs.irys.xyz/architecture]
Blockchain: Ethereum (untuk token IRYS); Irys Native L1 (untuk utility/provenance) (MEDIUM) [Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics; Dokumentasi Arsitektur Irys, https://docs.irys.xyz/architecture]
Contract Address: belum di-deploy (pre-TGE) (MEDIUM) [Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics]
Decimals: tidak diketahui (LOW) [Tidak ada sumber primer]
Status: Pre-TGE (MEDIUM) [Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics]
Sources: https://docs.irys.xyz/tokenomics; https://docs.irys.xyz/architecture; https://blog.irys.xyz/introducing-irys

## Supply
Maximum Supply: tidak diketahui (LOW) [Tidak ada sumber primer]
Total Supply: tidak diketahui (LOW) [Tidak ada sumber primer]
Circulating Supply: 0 (Pre-TGE) (HIGH) [Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics]
Initial Supply: tidak diketahui (LOW) [Tidak ada sumber primer]
Supply Type: tidak diketahui (Fixed / Inflationary / Dynamic tidak dipublikasikan) (LOW) [Tidak ada sumber primer]
Sources: https://docs.irys.xyz/tokenomics

## Distribution
Community: Planned (persentase tidak diungkap) (MEDIUM) [Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics]
Team: Planned (persentase tidak diungkap) (MEDIUM) [Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics]
Investors: Planned (persentase tidak diungkap) (MEDIUM) [Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics]
Foundation: Planned (persentase tidak diungkap) (MEDIUM) [Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics]
Treasury: Planned (persentase tidak diungkap) (MEDIUM) [Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics]
Ecosystem: Planned (persentase tidak diungkap) (MEDIUM) [Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics]
Advisors: tidak diketahui apakah ada alokasi terpisah (LOW) [Tidak ada sumber primer]
Other: tidak diketahui (LOW) [Tidak ada sumber primer]
Sources: https://docs.irys.xyz/tokenomics

## Vesting Schedule
Category: Community
Cliff: tidak diketahui
Vesting: tidak diketahui
Unlock Frequency: tidak diketahui
Current Status: Planned (Pre-TGE)
Sources: https://docs.irys.xyz/tokenomics

Category: Team
Cliff: tidak diketahui
Vesting: tidak diketahui
Unlock Frequency: tidak diketahui
Current Status: Planned (Pre-TGE)
Sources: https://docs.irys.xyz/tokenomics

Category: Investors
Cliff: tidak diketahui
Vesting: tidak diketahui
Unlock Frequency: tidak diketahui
Current Status: Planned (Pre-TGE)
Sources: https://docs.irys.xyz/tokenomics

Category: Foundation
Cliff: tidak diketahui
Vesting: tidak diketahui
Unlock Frequency: tidak diketahui
Current Status: Planned (Pre-TGE)
Sources: https://docs.irys.xyz/tokenomics

Category: Treasury
Cliff: tidak diketahui
Vesting: tidak diketahui
Unlock Frequency: tidak diketahui
Current Status: Planned (Pre-TGE)
Sources: https://docs.irys.xyz/tokenomics

Category: Ecosystem
Cliff: tidak diketahui
Vesting: tidak diketahui
Unlock Frequency: tidak diketahui
Current Status: Planned (Pre-TGE)
Sources: https://docs.irys.xyz/tokenomics

## TGE
TGE Date: belum dijadwalkan resmi (Pre-TGE) (MEDIUM) [Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics]
Initial Unlock: tidak diketahui (LOW) [Tidak ada sumber primer]
Unlocked Categories: tidak diketahui (LOW) [Tidak ada sumber primer]
Launch Platform: tidak diketahui (CEX/DEX/Launchpad tidak diumumkan) (LOW) [Tidak ada sumber primer]
Status: Pre-TGE (MEDIUM) [Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics]
Sources: https://docs.irys.xyz/tokenomics; https://blog.irys.xyz/introducing-irys

## Utility
Utility: Storage Payment
Deskripsi: Token IRYS digunakan untuk membayar biaya penyimpanan data permanen di jaringan Irys
Status: Planned (Pre-TGE)
Sources: https://docs.irys.xyz/tokenomics; https://docs.irys.xyz/architecture; https://irys.xyz

Utility: Staking Validator
Deskripsi: Token IRYS di-stake di Ethereum untuk keamanan ekonomi validator Irys L1 (mekanisme staking/restaking)
Status: Planned (Pre-TGE)
Sources: https://docs.irys.xyz/tokenomics; https://docs.irys.xyz/architecture

Utility: Governance
Deskripsi: Token IRYS digunakan untuk governance protokol (voting, proposal)
Status: Planned (Pre-TGE)
Sources: https://docs.irys.xyz/tokenomics; https://irys.xyz

Utility: Fee Payment
Deskripsi: Token IRYS digunakan untuk pembayaran protocol fees (storage, provenance, gateway)
Status: Planned (Pre-TGE)
Sources: https://docs.irys.xyz/tokenomics; https://docs.irys.xyz/architecture

Utility: Incentive/Reward
Deskripsi: Token IRYS sebagai insentif untuk validator, data contributor, dan ekosistem (testnet berinsentif sudah dijalankan EV-004)
Status: Live di Testnet / Planned untuk Mainnet
Sources: https://blog.irys.xyz/irys-incentivized-testnet; https://docs.irys.xyz/tokenomics

## Governance
Governance Model: tidak diketahui (tidak dipublikasikan detail model governance on-chain/off-chain) (LOW) [Tidak ada sumber primer]
Voting System: tidak diketahui (LOW) [Tidak ada sumber primer]
Voting Power: tidak diketahui (LOW) [Tidak ada sumber primer]
Delegation: tidak diketahui (LOW) [Tidak ada sumber primer]
Proposal System: tidak diketahui (LOW) [Tidak ada sumber primer]
Treasury Governance: tidak diketahui (LOW) [Tidak ada sumber primer]
Status: Belum terbentuk (Pre-TGE)
Sources: https://docs.irys.xyz/tokenomics; https://irys.xyz; https://blog.irys.xyz

## Inflation / Deflation
Inflation Mechanism: tidak diketahui (LOW) [Tidak ada sumber primer]
Emission Schedule: tidak diketahui (LOW) [Tidak ada sumber primer]
Burn Mechanism: tidak diketahui (LOW) [Tidak ada sumber primer]
Buyback: tidak diketahui (LOW) [Tidak ada sumber primer]
Supply Reduction: tidak diketahui (LOW) [Tidak ada sumber primer]
Status: Belum dipublikasikan detailnya
Sources: https://docs.irys.xyz/tokenomics

## Holder Distribution
Top Holder Concentration: N/A (Pre-TGE, token belum ada) (HIGH) [Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics]
Foundation Holding: N/A (Pre-TGE) (HIGH) [Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics]
Investor Holding: N/A (Pre-TGE) (HIGH) [Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics]
Treasury Holding: N/A (Pre-TGE) (HIGH) [Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics]
Community Holding: N/A (Pre-TGE) (HIGH) [Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics]
Whale Concentration: N/A (Pre-TGE) (HIGH) [Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics]
Sources: https://docs.irys.xyz/tokenomics

## Major Token Events
Date: 2024-01
Event: Irys Incentivized Testnet Phase 1 (EV-004)
Description: Program testnet berinsentif Phase 1 dimulai untuk menguji ekonomi token, performa validator, dan lapisan provenance sebelum mainnet. Token testnet digunakan untuk simulasi staking dan reward.
Status: Completed
Related Historical Event ID: EV-004
Sources: https://blog.irys.xyz/irys-incentivized-testnet; https://docs.irys.xyz

Date: 2024-03
Event: Publikasi Tokenomics IRYS (EV-010)
Description: Dokumentasi tokenomics IRYS dipublikasikan di docs.irys.xyz/tokenomics, menggariskan alokasi, utilitas (storage payment, staking, governance), dan status pre-TGE.
Status: Ongoing (dokumen live)
Related Historical Event ID: EV-010
Sources: https://docs.irys.xyz/tokenomics; https://blog.irys.xyz/introducing-irys

Date: 2024-03-26
Event: Mainnet Launch Irys L1 (EV-006)
Description: Mainnet Irys diluncurkan, mengaktifkan Irys L1, Provenance Layer, Gateway, dan Explorer. Token IRYS belum live (pre-TGE), utility storage payment dan staking direncanakan pasca-TGE.
Status: Completed (Mainnet live, token belum)
Related Historical Event ID: EV-006
Sources: https://blog.irys.xyz/irys-mainnet-launch; https://irys.xyz; https://explorer.irys.xyz

## Official Token Resources
Official Documentation: https://docs.irys.xyz/tokenomics
Whitepaper: tidak tersedia (tidak ditemukan di website/docs resmi) (LOW) [Website Resmi Irys, https://irys.xyz]
Governance: tidak tersedia (belum terbentuk) (LOW) [Website Resmi Irys, https://irys.xyz]
Explorer: https://explorer.irys.xyz (untuk Irys L1, bukan token IRYS di Ethereum)
Contract: belum di-deploy (pre-TGE) (MEDIUM) [Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics]
GitHub: https://github.com/irys-xyz
Dashboard: tidak tersedia (LOW) [Website Resmi Irys, https://irys.xyz]
Sources: https://docs.irys.xyz/tokenomics; https://irys.xyz; https://github.com/irys-xyz; https://explorer.irys.xyz

## RINGKASAN
Status: Pre-TGE
Supply Type: tidak diketahui
Total Supply: tidak diketahui
Distribution Categories: Community, Team, Investors, Foundation, Treasury, Ecosystem (semua Planned, persentase tidak diungkap)
Utility Count: 5 (Storage Payment, Staking Validator, Governance, Fee Payment, Incentive/Reward)
Governance: Belum terbentuk
Major Token Events: 3 (Incentivized Testnet Phase 1 EV-004, Tokenomics Publication EV-010, Mainnet Launch EV-006)

## Ecosystem Intelligence
_ref: `docs/Ontology/Community.md`, `docs/Ontology/Ecosystem.md`_

PROJECT: Irys

## Ecosystem Position
Primary Sector: Permanent data provenance layer / Layer 1 blockchain (HIGH) [Website Resmi Irys, https://irys.xyz; Dokumentasi Arsitektur Irys, https://docs.irys.xyz/architecture]
Secondary Sector: AI/Data Provenance; DePIN (MEDIUM) [Blog Ekosistem Irys, https://blog.irys.xyz/category/ecosystem; Website Resmi Irys, https://irys.xyz]
Primary Chain: Irys (Native L1) (HIGH) [Blog Mainnet Launch, https://blog.irys.xyz/irys-mainnet-launch; Block Explorer Resmi, https://explorer.irys.xyz]
Supported Chains: Ethereum (Staking & Settlement); Arweave (Permanent Storage Layer) (HIGH) [Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics; Dokumentasi Arsitektur Irys, https://docs.irys.xyz/architecture]
Sources: https://irys.xyz; https://docs.irys.xyz/architecture; https://docs.irys.xyz/tokenomics; https://blog.irys.xyz/category/ecosystem; https://blog.irys.xyz/irys-mainnet-launch; https://explorer.irys.xyz

## External Dependencies
Dependency Name: Arweave
Dependency Type: Protocol
Purpose: Permanent storage layer untuk data blob yang dibundel oleh Irys; fondasi data availability (HIGH) [Dokumentasi Arsitektur Irys, https://docs.irys.xyz/architecture; Blog Ekosistem Irys, https://blog.irys.xyz/category/ecosystem]
Criticality: Critical
Status: Live
Related Entity: Arweave
Related Technology Component: Arweave Integration (Storage Layer)
Sources: https://docs.irys.xyz/architecture; https://blog.irys.xyz/category/ecosystem

Dependency Name: Ethereum
Dependency Type: Chain
Purpose: Settlement layer dan staking untuk token IRYS; lapisan keamanan ekonomi validator melalui mekanisme staking/restaking (HIGH) [Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics; Dokumentasi Arsitektur Irys, https://docs.irys.xyz/architecture]
Criticality: Critical
Status: Live (kontrak staking/settlement direncanakan pre-TGE)
Related Entity: Ethereum
Related Technology Component: Ethereum Staking/Settlement Contracts
Sources: https://docs.irys.xyz/tokenomics; https://docs.irys.xyz/architecture

Dependency Name: Bundlr Labs, Inc.
Dependency Type: Company
Purpose: Entitas pengembang inti (core developer) dan operator protokol Irys; bertanggung jawab atas pengembangan L1, SDK, Gateway, Provenance Layer (HIGH) [Terms of Service Irys, https://irys.xyz/terms; Blog Resmi Irys, https://blog.irys.xyz/introducing-irys]
Criticality: Critical
Status: Live
Related Entity: Bundlr Labs, Inc.
Related Technology Component: Irys L1 (Validator/Consensus Layer); Provenance Layer; Irys Gateway; Irys SDK
Sources: https://irys.xyz/terms; https://blog.irys.xyz/introducing-irys

## Major Integrations
Integration Name: Arweave Storage Integration
Integrated With: Arweave
Purpose: Penyimpanan permanen data blob via Arweave; data availability layer (HIGH) [Dokumentasi Arsitektur Irys, https://docs.irys.xyz/architecture; Blog Ekosistem Irys, https://blog.irys.xyz/category/ecosystem]
Status: Live
Related Historical Event ID: EV-002
Sources: https://docs.irys.xyz/architecture; https://blog.irys.xyz/category/ecosystem

Integration Name: Ethereum Staking/Settlement Integration
Integrated With: Ethereum
Purpose: Staking token IRYS, registrasi validator, settlement ekonomi, keamanan ekonomi validator (HIGH) [Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics; Dokumentasi Arsitektur Irys, https://docs.irys.xyz/architecture]
Status: Live (kontrak di Ethereum direncanakan pre-TGE)
Related Historical Event ID: EV-009
Sources: https://docs.irys.xyz/tokenomics; https://docs.irys.xyz/architecture

Integration Name: Irys SDK Integration
Integrated With: Developer applications / dApps
Purpose: Mengunggah data, menandatangani transaksi provenance, pembayaran storage via SDK (HIGH) [Dokumentasi SDK Irys, https://docs.irys.xyz/sdk; Repositori GitHub Irys, https://github.com/irys-xyz]
Status: Live
Related Historical Event ID: EV-003
Sources: https://docs.irys.xyz/sdk; https://github.com/irys-xyz

Integration Name: Irys Gateway Integration
Integrated With: Data consumers / aplikasi retrieval
Purpose: HTTP gateway untuk retrieval dan akses data permanen dari jaringan Irys (HIGH) [Dokumentasi Produk Irys, https://docs.irys.xyz; Website Resmi Irys, https://irys.xyz]
Status: Live
Related Historical Event ID: EV-008
Sources: https://docs.irys.xyz; https://irys.xyz

## Infrastructure Providers
Provider: Arweave
Service: Permanent storage layer untuk data blob (HIGH) [Dokumentasi Arsitektur Irys, https://docs.irys.xyz/architecture]
Criticality: Critical
Status: Live
Sources: https://docs.irys.xyz/architecture

Provider: Ethereum
Service: Settlement & staking layer untuk token IRYS dan keamanan ekonomi validator (HIGH) [Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics]
Criticality: Critical
Status: Live
Sources: https://docs.irys.xyz/tokenomics

Provider: Irys Gateway (self-operated)
Service: HTTP data retrieval gateway resmi (HIGH) [Dokumentasi Produk Irys, https://docs.irys.xyz; Website Resmi Irys, https://irys.xyz]
Criticality: High
Status: Live
Sources: https://docs.irys.xyz; https://irys.xyz

Provider: Irys Explorer (self-operated)
Service: Block explorer & verifikasi transaksi, blok, akun, provenance (HIGH) [Block Explorer Resmi, https://explorer.irys.xyz; Website Resmi Irys, https://irys.xyz]
Criticality: High
Status: Live
Sources: https://explorer.irys.xyz; https://irys.xyz

Provider: GitHub (github.com)
Service: Source code hosting untuk organisasi irys-xyz (HIGH) [Organisasi GitHub Resmi, https://github.com/irys-xyz]
Criticality: Medium
Status: Live
Sources: https://github.com/irys-xyz

Provider: Discord (discord.gg)
Service: Komunitas koordinasi validator/developer/user (HIGH) [Tautan Undangan Resmi, https://discord.gg/irys]
Criticality: Medium
Status: Live
Sources: https://discord.gg/irys

## Exchange Ecosystem
Exchange: tidak diketahui (Pre-TGE, token IRYS belum di-deploy) (HIGH) [Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics]
Listing Status: N/A
Spot: N/A
Perpetual: N/A
OTC: N/A
Launchpool: N/A
Status: Pre-TGE
Sources: https://docs.irys.xyz/tokenomics

## Wallet Ecosystem
Wallet: tidak diketahui (tidak ada integrasi wallet spesifik terdokumentasi di sumber primer; Irys SDK kemungkinan mendukung wallet Ethereum standar seperti MetaMask/WalletConnect untuk signing namun tidak diverifikasi eksplisit) (LOW) [Dokumentasi SDK Irys, https://docs.irys.xyz/sdk; Dokumentasi Arsitektur Irys, https://docs.irys.xyz/architecture]
Support Type: tidak diketahui
Status: tidak diketahui
Sources: https://docs.irys.xyz/sdk; https://docs.irys.xyz/architecture

## Developer Ecosystem
SDK: Irys SDK (TypeScript/JavaScript untuk browser dan Node.js) (HIGH) [Dokumentasi SDK Irys, https://docs.irys.xyz/sdk; Repositori GitHub Irys, https://github.com/irys-xyz]
API: HTTP REST API via Irys Gateway untuk data retrieval (HIGH) [Dokumentasi Produk Irys, https://docs.irys.xyz]
Developer Tools: Irys CLI (bundled dalam SDK/repo terpisah) untuk deployment dan interaction (HIGH) [Repositori GitHub Irys, https://github.com/irys-xyz]
Open Source Repository: Irys GitHub Organization (irys-xyz) (HIGH) [Organisasi GitHub Resmi, https://github.com/irys-xyz]
Developer Portal: https://docs.irys.xyz (HIGH) [Dokumentasi Resmi, https://docs.irys.xyz]
Hackathon: tidak diketahui (tidak terdokumentasi di blog, website, docs, atau GitHub resmi) (LOW) [Blog Resmi Irys, https://blog.irys.xyz; Website Resmi Irys, https://irys.xyz; Repositori GitHub Irys, https://github.com/irys-xyz]
Grant Program: tidak diketahui (tidak terdokumentasi di sumber primer resmi) (LOW) [Blog Resmi Irys, https://blog.irys.xyz; Website Resmi Irys, https://irys.xyz; Dokumentasi Irys, https://docs.irys.xyz]
Sources: https://docs.irys.xyz/sdk; https://github.com/irys-xyz; https://docs.irys.xyz; https://blog.irys.xyz; https://irys.xyz

## Applications
Application: Irys Explorer
Category: Block Explorer
Relationship: Official first-party application untuk verifikasi transaksi, blok, akun, provenance (HIGH) [Block Explorer Resmi, https://explorer.irys.xyz; Website Resmi Irys, https://irys.xyz]
Status: Live
Sources: https://explorer.irys.xyz; https://irys.xyz

Application: Irys Gateway
Category: Data Retrieval Gateway
Relationship: Official first-party infrastructure untuk HTTP retrieval data permanen (HIGH) [Dokumentasi Produk Irys, https://docs.irys.xyz; Website Resmi Irys, https://irys.xyz]
Status: Live
Sources: https://docs.irys.xyz; https://irys.xyz

Application: Irys SDK
Category: Developer Library
Relationship: Official first-party SDK untuk integrasi developer (HIGH) [Dokumentasi SDK Irys, https://docs.irys.xyz/sdk; Repositori GitHub Irys, https://github.com/irys-xyz]
Status: Live
Sources: https://docs.irys.xyz/sdk; https://github.com/irys-xyz

Application: Irys Documentation (docs.irys.xyz)
Category: Developer Portal
Relationship: Official documentation portal (HIGH) [Dokumentasi Resmi, https://docs.irys.xyz]
Status: Live
Sources: https://docs.irys.xyz

Application: Irys Incentivized Testnet
Category: Testnet Program
Relationship: Official testnet berinsentif Phase 1 (HIGH) [Blog Resmi Irys Testnet, https://blog.irys.xyz/irys-incentivized-testnet; Dokumentasi Irys, https://docs.irys.xyz]
Status: Completed (Phase 1)
Sources: https://blog.irys.xyz/irys-incentivized-testnet; https://docs.irys.xyz

Application: Bundlr Network (Legacy)
Category: Bundler Service
Relationship: Predecessor protocol (rebranded ke Irys) (HIGH) [Blog Resmi Rebranding, https://blog.irys.xyz/introducing-irys; Terms of Service Irys, https://irys.xyz/terms]
Status: Deprecated/Rebranded
Sources: https://blog.irys.xyz/introducing-irys; https://irys.xyz/terms

## Governance Ecosystem
Foundation: tidak diketahui (tidak ada entitas foundation terpisah teridentifikasi dari Bundlr Labs, Inc. di sumber primer) (MEDIUM) [Terms of Service Irys, https://irys.xyz/terms; Website Resmi Irys, https://irys.xyz; Blog Resmi Irys, https://blog.irys.xyz]
DAO: tidak diketahui (belum terbentuk, pre-TGE) (HIGH) [Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics; Website Resmi Irys, https://irys.xyz]
Council: tidak diketahui (tidak dipublikasikan) (LOW) [Website Resmi Irys, https://irys.xyz; Dokumentasi Irys, https://docs.irys.xyz]
Committee: tidak diketahui (tidak dipublikasikan) (LOW) [Website Resmi Irys, https://irys.xyz; Dokumentasi Irys, https://docs.irys.xyz]
Validator Group: tidak diketahui (genesis validator set tidak diungkapkan secara publik) (MEDIUM) [Blog Mainnet Launch, https://blog.irys.xyz/irys-mainnet-launch; Block Explorer Resmi, https://explorer.irys.xyz]
Sources: https://irys.xyz/terms; https://irys.xyz; https://blog.irys.xyz; https://docs.irys.xyz/tokenomics; https://blog.irys.xyz/irys-mainnet-launch; https://explorer.irys.xyz

## Ecosystem Risks
Risk: Single Storage Layer Dependency (Arweave)
Description: Irys bergantung sepenuhnya pada Arweave sebagai permanent storage layer; outage atau perubahan signifikan pada Arweave berdampak langsung pada ketersediaan data Irys (HIGH) [Dokumentasi Arsitektur Irys, https://docs.irys.xyz/architecture]
Sources: https://docs.irys.xyz/architecture

Risk: Single Settlement Layer Dependency (Ethereum)
Description: Keamanan ekonomi validator dan staking token IRYS bergantung pada Ethereum; congestion, fork, atau kegagalan Ethereum mempengaruhi operasi validator Irys (HIGH) [Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics; Dokumentasi Arsitektur Irys, https://docs.irys.xyz/architecture]
Sources: https://docs.irys.xyz/tokenomics; https://docs.irys.xyz/architecture

Risk: Centralized Development Dependency (Bundlr Labs, Inc.)
Description: Pengembangan protokol inti (L1, SDK, Gateway, Provenance) dikendalikan oleh single entity (Bundlr Labs, Inc.) tanpa foundation terpisah atau DAO governance yang aktif (MEDIUM) [Terms of Service Irys, https://irys.xyz/terms; Blog Resmi Irys, https://blog.irys.xyz/introducing-irys]
Sources: https://irys.xyz/terms; https://blog.irys.xyz/introducing-irys

Risk: Pre-TGE Token Economic Risk
Description: Token IRYS belum live (pre-TGE), utility staking, governance, payment storage, dan reward validator belum diuji di mainnet; model ekonomi belum tervalidasi (MEDIUM) [Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics]
Sources: https://docs.irys.xyz/tokenomics

Risk: No Public Security Audits
Description: Tidak ada laporan audit keamanan publik (consensus, cryptography, smart contracts) yang dipublikasikan di website, blog, atau docs resmi (LOW) [Website Resmi Irys, https://irys.xyz; Dokumentasi Irys, https://docs.irys.xyz; Blog Resmi Irys, https://blog.irys.xyz]
Sources: https://irys.xyz; https://docs.irys.xyz; https://blog.irys.xyz

Risk: Undisclosed Validator Set
Description: Genesis validator set dan infrastructure provider di baliknya tidak diungkapkan secara transparan; tingkat desentralisasi validator tidak dapat diverifikasi (MEDIUM) [Blog Mainnet Launch, https://blog.irys.xyz/irys-mainnet-launch; Block Explorer Resmi, https://explorer.irys.xyz]
Sources: https://blog.irys.xyz/irys-mainnet-launch; https://explorer.irys.xyz

## Official Ecosystem Resources
Official Documentation: https://docs.irys.xyz
Developer Portal: https://docs.irys.xyz
GitHub: https://github.com/irys-xyz
Partner Documentation: tidak tersedia (tidak ada partner documentation terlink di sumber primer) (LOW) [Website Resmi Irys, https://irys.xyz; Dokumentasi Irys, https://docs.irys.xyz]
Grant Program: tidak tersedia (tidak terdokumentasi) (LOW) [Blog Resmi Irys, https://blog.irys.xyz; Website Resmi Irys, https://irys.xyz; Dokumentasi Irys, https://docs.irys.xyz]
Ecosystem Dashboard: tidak tersedia (LOW) [Website Resmi Irys, https://irys.xyz; Dokumentasi Irys, https://docs.irys.xyz]
Sources: https://docs.irys.xyz; https://github.com/irys-xyz; https://irys.xyz; https://blog.irys.xyz

## RINGKASAN
Primary Ecosystem: Arweave (storage), Ethereum (settlement/staking), AI/Data Provenance, DePIN
Supported Chains: Irys Native L1, Ethereum, Arweave
External Dependencies: 3 critical (Arweave, Ethereum, Bundlr Labs, Inc.)
Major Integrations: 4 live (Arweave storage, Ethereum staking, SDK, Gateway)
Infrastructure Providers: 6 (Arweave, Ethereum, Irys Gateway, Irys Explorer, GitHub, Discord)
Developer Programs: SDK, API, CLI, GitHub, Docs (hackathon/grant tidak terdokumentasi)
Applications: 6 first-party (Explorer, Gateway, SDK, Docs, Testnet, Legacy Bundlr)

## Market Intelligence
_ref: `docs/Meta/Narratives.md`, `docs/Valuation/Competitors.md`, `docs/Meta/MarketCycles.md`_

PROJECT: Irys

## Market Category
Primary Category: Layer 1 blockchain (MEDIUM) [Website Resmi Irys, https://irys.xyz; Dokumentasi Arsitektur Irys, https://docs.irys.xyz/architecture]
Secondary Category: Permanent data provenance layer (MEDIUM) [Website Resmi Irys, https://irys.xyz; Blog Resmi Irys, https://blog.irys.xyz/introducing-irys]
Sector: Data Availability / Storage (MEDIUM) [Dokumentasi Arsitektur Irys, https://docs.irys.xyz/architecture; Blog Ekosistem Irys, https://blog.irys.xyz/category/ecosystem]
Sub-sector: AI/Data Provenance; DePIN (MEDIUM) [Blog Ekosistem Irys, https://blog.irys.xyz/category/ecosystem; Website Resmi Irys, https://irys.xyz]
Sources: https://irys.xyz; https://docs.irys.xyz/architecture; https://blog.irys.xyz/introducing-irys; https://blog.irys.xyz/category/ecosystem

## Market Position
Project Stage: Pre-TGE / Early (HIGH) [Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics; Blog Mainnet Launch, https://blog.irys.xyz/irys-mainnet-launch]
Primary Competitors: Arweave; Filecoin; Celestia; EigenDA; Avail; 0G; Walrus (MEDIUM) [Dokumentasi Arsitektur Irys, https://docs.irys.xyz/architecture; Blog Ekosistem Irys, https://blog.irys.xyz/category/ecosystem]
Market Segment: Permanent data storage with on-chain provenance for AI and DePIN (MEDIUM) [Website Resmi Irys, https://irys.xyz; Blog Resmi Irys, https://blog.irys.xyz/introducing-irys]
Geographic Focus: Global / Remote (MEDIUM) [Terms of Service Irys, https://irys.xyz/terms]
Sources: https://irys.xyz; https://docs.irys.xyz/tokenomics; https://blog.irys.xyz/irys-mainnet-launch; https://docs.irys.xyz/architecture; https://blog.irys.xyz/category/ecosystem; https://blog.irys.xyz/introducing-irys; https://irys.xyz/terms

## Trading Markets
Exchange: Tidak tersedia (Pre-TGE, token IRYS belum di-deploy) (HIGH) [Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics]
Spot: N/A
Perpetual: N/A
Futures: N/A
Options: N/A
OTC: N/A
Status: Pre-TGE
Sources: https://docs.irys.xyz/tokenomics

## Liquidity
Liquidity Source: Tidak tersedia (Pre-TGE) (HIGH) [Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics]
Major Liquidity Venue: N/A
DEX: N/A
CEX: N/A
Bridge Liquidity: N/A
Status: Pre-TGE
Sources: https://docs.irys.xyz/tokenomics

## Adoption Metrics
Metric Name: TVL
Value: Tidak tersedia (Irys bukan protokol DeFi dengan TVL tradisional; tidak ada data di DefiLlama/Token Terminal) (LOW) [DefiLlama, https://defillama.com; Token Terminal, https://tokenterminal.com]
Date: 2024
Sources: https://defillama.com; https://tokenterminal.com

Metric Name: Daily Active Users
Value: Tidak tersedia (tidak dipublikasikan di dashboard resmi atau pihak ketiga) (LOW) [Website Resmi Irys, https://irys.xyz; Blog Resmi Irys, https://blog.irys.xyz; Dune Analytics, https://dune.com]
Date: 2024
Sources: https://irys.xyz; https://blog.irys.xyz; https://dune.com

Metric Name: Transactions (Daily/Total)
Value: Tidak tersedia secara agregat publik; explorer menampilkan transaksi per blok tapi tidak ada metrik ringkasan harian resmi (LOW) [Block Explorer Resmi, https://explorer.irys.xyz]
Date: 2024
Sources: https://explorer.irys.xyz

Metric Name: Wallets (Unique Addresses)
Value: Tidak tersedia secara publik (explorer tidak menampilkan total unique addresses) (LOW) [Block Explorer Resmi, https://explorer.irys.xyz]
Date: 2024
Sources: https://explorer.irys.xyz

Metric Name: Developer Count
Value: Tidak tersedia (tidak dipublikasikan di Electric Capital / GitHub insights resmi) (LOW) [Organisasi GitHub Irys, https://github.com/irys-xyz; Electric Capital, https://www.electriccapital.com]
Date: 2024
Sources: https://github.com/irys-xyz; https://www.electriccapital.com

Metric Name: Volume (Storage/Transaction)
Value: Tidak tersedia (tidak ada dashboard volume resmi atau pihak ketiga) (LOW) [Website Resmi Irys, https://irys.xyz; Block Explorer Resmi, https://explorer.irys.xyz]
Date: 2024
Sources: https://irys.xyz; https://explorer.irys.xyz

Metric Name: Validator Count
Value: Tidak tersedia (genesis validator set tidak diungkapkan publik; explorer tidak menampilkan halaman validator set) (MEDIUM) [Blog Mainnet Launch, https://blog.irys.xyz/irys-mainnet-launch; Block Explorer Resmi, https://explorer.irys.xyz]
Date: 2024-03-26
Sources: https://blog.irys.xyz/irys-mainnet-launch; https://explorer.irys.xyz

## Market Share
Tidak tersedia. (Irys baru meluncurkan mainnet Maret 2024, token pre-TGE, tidak ada data market share penyimpanan/provenance yang dipublikasikan oleh pihak independen seperti Messari/Token Terminal/DefiLlama)

## Competitor Landscape
Competitor: Arweave
Category: Permanent storage layer (Layer 1)
Difference: Arweave adalah lapisan penyimpanan permanen yang digunakan Irys sebagai storage layer; Irys menambahkan provenance layer on-chain dan L1 konsensus sendiri di atas Arweave (MEDIUM) [Dokumentasi Arsitektur Irys, https://docs.irys.xyz/architecture; Blog Ekosistem Irys, https://blog.irys.xyz/category/ecosystem]
Market Segment: Permanent data storage
Sources: https://docs.irys.xyz/architecture; https://blog.irys.xyz/category/ecosystem

Competitor: Filecoin
Category: Decentralized storage network
Difference: Filecoin menggunakan proof-of-replication/storage untuk penyimpanan terdesentralisasi; Irys menggunakan Arweave untuk permanen dan menambahkan provenance layer native (MEDIUM) [Dokumentasi Arsitektur Irys, https://docs.irys.xyz/architecture; Blog Ekosistem Irys, https://blog.irys.xyz/category/ecosystem]
Market Segment: Decentralized storage
Sources: https://docs.irys.xyz/architecture; https://blog.irys.xyz/category/ecosystem

Competitor: Celestia
Category: Modular data availability layer
Difference: Celestia menyediakan data availability untuk rollup/L2; Irys adalah L1 penuh dengan provenance dan permanent storage via Arweave (MEDIUM) [Dokumentasi Arsitektur Irys, https://docs.irys.xyz/architecture; Blog Ekosistem Irys, https://blog.irys.xyz/category/ecosystem]
Market Segment: Data availability
Sources: https://docs.irys.xyz/architecture; https://blog.irys.xyz/category/ecosystem

Competitor: EigenDA
Category: Data availability service (AVS on EigenLayer)
Difference: EigenDA adalah DA layer terpercaya pada Ethereum via restaking; Irys adalah L1 sovereign dengan permanent storage dan provenance (MEDIUM) [Dokumentasi Arsitektur Irys, https://docs.irys.xyz/architecture; Blog Ekosistem Irys, https://blog.irys.xyz/category/ecosystem]
Market Segment: Data availability
Sources: https://docs.irys.xyz/architecture; https://blog.irys.xyz/category/ecosystem

Competitor: Avail
Category: Modular data availability layer
Difference: Avail fokus DA untuk rollup dengan validium/light clients; Irys menyediakan permanent storage + provenance + L1 execution (MEDIUM) [Dokumentasi Arsitektur Irys, https://docs.irys.xyz/architecture; Blog Ekosistem Irys, https://blog.irys.xyz/category/ecosystem]
Market Segment: Data availability
Sources: https://docs.irys.xyz/architecture; https://blog.irys.xyz/category/ecosystem

Competitor: 0G (ZeroGravity)
Category: Modular AI chain / Data availability
Difference: 0G menargetkan AI dengan DA terukur dan storage; Irys menargetkan provenance data permanen untuk AI/DePIN via Arweave (MEDIUM) [Blog Ekosistem Irys, https://blog.irys.xyz/category/ecosystem; Website Resmi Irys, https://irys.xyz]
Market Segment: AI data infrastructure
Sources: https://blog.irys.xyz/category/ecosystem; https://irys.xyz

Competitor: Walrus (Mysten Labs)
Category: Decentralized storage / blob availability
Difference: Walrus adalah protokol storage terdesentralisasi baru dari Mysten Labs (Sui); Irys sudah mainnet dengan Arweave backend dan provenance layer (MEDIUM) [Blog Ekosistem Irys, https://blog.irys.xyz/category/ecosystem; Website Resmi Irys, https://irys.xyz]
Market Segment: Decentralized storage
Sources: https://blog.irys.xyz/category/ecosystem; https://irys.xyz

## Narrative Position
Narrative: Permanent data provenance layer
Status: Main Narrative
Evidence: Website resmi dan blog konstan menggunakan "permanent data provenance layer" sebagai posisining utama; arsitektur menggabungkan Arweave (permanent storage) dengan provenance layer on-chain native (HIGH) [Website Resmi Irys, https://irys.xyz; Blog Resmi Irys, https://blog.irys.xyz/introducing-irys; Dokumentasi Arsitektur Irys, https://docs.irys.xyz/architecture]
Sources: https://irys.xyz; https://blog.irys.xyz/introducing-irys; https://docs.irys.xyz/architecture

Narrative: AI data provenance
Status: Secondary Narrative
Evidence: Blog kategori ekosystem dan website menyebut AI training data provenance sebagai pasar sasaran; narasi "provenance for AI" muncul di komunikasi resmi (MEDIUM) [Blog Ekosistem Irys, https://blog.irys.xyz/category/ecosystem; Website Resmi Irys, https://irys.xyz]
Sources: https://blog.irys.xyz/category/ecosystem; https://irys.xyz

Narrative: DePIN
Status: Secondary Narrative
Evidence: Website dan blog mencantumkan DePIN sebagai kategori ekosistem; provenance data sensor/fisik untuk DePIN disebutkan sebagai use case (MEDIUM) [Blog Ekosistem Irys, https://blog.irys.xyz/category/ecosystem; Website Resmi Irys, https://irys.xyz]
Sources: https://blog.irys.xyz/category/ecosystem; https://irys.xyz

Narrative: Modular blockchain
Status: Secondary Narrative
Evidence: Arsitektur memisahkan storage (Arweave), settlement/staking (Ethereum), execution/provenance (Irys L1) - karakteristik modular; namun Irys dipasarkan sebagai L1 sovereign bukan modular DA layer (MEDIUM) [Dokumentasi Arsitektur Irys, https://docs.irys.xyz/architecture; Blog Resmi Irys, https://blog.irys.xyz/introducing-irys]
Sources: https://docs.irys.xyz/architecture; https://blog.irys.xyz/introducing-irys

Narrative: Restaking
Status: Secondary Narrative
Evidence: Tokenomics menyebut staking IRYS di Ethereum untuk keamanan ekonomi validator; mengimplikasikan restaking/mekanisme serupa EigenLayer (MEDIUM) [Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics; Dokumentasi Arsitektur Irys, https://docs.irys.xyz/architecture]
Sources: https://docs.irys.xyz/tokenomics; https://docs.irys.xyz/architecture

Narrative: Interoperability
Status: Tidak diterapkan sebagai narasi utama
Evidence: Tidak ada messaging layer/bridge resmi ke chain lain selain Ethereum-Arweave; tidak dipasarkan sebagai interoperability solution (LOW) [Dokumentasi Arsitektur Irys, https://docs.irys.xyz/architecture]
Sources: https://docs.irys.xyz/architecture

## Market Timeline
Date: 2021
Milestone: Pendirian Bundlr Labs dan peluncuran Bundlr Network pada Arweave
Description: Entitas perusahaan dan protokol bundler awal beroperasi, menjadi lapisan penyederhanaan akses ke penyimpanan permanen Arweave
Related Historical Event ID: EV-001
Sources: https://irys.xyz/terms; https://blog.irys.xyz/introducing-irys; https://docs.irys.xyz/architecture

Date: 2023
Milestone: Peluncuran SDK, dokumentasi, GitHub, dan saluran komunitas
Description: Infrastruktur pengembangan, dokumentasi, dan komunitas resmi tersedia untuk ekosistem awal sebelum mainnet
Related Historical Event ID: EV-003
Sources: https://docs.irys.xyz/sdk; https://docs.irys.xyz; https://github.com/irys-xyz; https://discord.gg/irys; https://x.com/irys_xyz; https://t.me/irys_xyz; https://blog.irys.xyz

Date: 2024-01
Milestone: Peluncuran Incentivized Testnet Phase 1
Description: Program testnet berinsentif untuk menguji ekonomi token, performa validator, dan lapisan provenance sebelum mainnet
Related Historical Event ID: EV-004
Sources: https://blog.irys.xyz/irys-incentivized-testnet; https://docs.irys.xyz

Date: 2024-03
Milestone: Pengumuman rebranding Bundlr Network ke Irys
Description: Proyek mengumumkan rebranding dari Bundlr Network menjadi Irys, mencerminkan evolusi dari bundler service ke Layer 1 blockchain provenance layer
Related Historical Event ID: EV-005
Sources: https://blog.irys.xyz/introducing-irys; https://irys.xyz/terms

Date: 2024-03-26
Milestone: Peluncuran Mainnet Irys L1
Description: Mainnet Irys secara resmi diluncurkan, mengaktifkan Irys L1 sebagai blockchain Layer 1 native untuk konsensus dan eksekusi transaksi data serta provenance
Related Historical Event ID: EV-006
Sources: https://blog.irys.xyz/irys-mainnet-launch; https://irys.xyz; https://explorer.irys.xyz

Date: 2024-03
Milestone: Peluncuran Irys Explorer dan aktivasi Gateway/Provenance Layer
Description: Block explorer resmi dan HTTP gateway untuk retrieval data serta provenance layer diaktifkan pada mainnet
Related Historical Event ID: EV-007; EV-008
Sources: https://explorer.irys.xyz; https://irys.xyz; https://docs.irys.xyz; https://docs.irys.xyz/architecture

Date: 2024
Milestone: Publikasi tokenomics IRYS (pre-TGE)
Description: Dokumentasi tokenomics dipublikasikan menggariskan alokasi, utilitas, dan status pre-TGE
Related Historical Event ID: EV-010
Sources: https://docs.irys.xyz/tokenomics; https://blog.irys.xyz/introducing-irys

Date: 2024
Milestone: Integrasi Ethereum sebagai settlement dan staking layer
Description: Ethereum ditetapkan sebagai chain settlement dan staking untuk token IRYS serta keamanan ekonomi validator
Related Historical Event ID: EV-009
Sources: https://docs.irys.xyz/tokenomics; https://docs.irys.xyz/architecture

## Official Market Resources
Official Dashboard: tidak tersedia (LOW) [Website Resmi Irys, https://irys.xyz]
DefiLlama: tidak tersedia (LOW) [DefiLlama, https://defillama.com]
CoinGecko: tidak tersedia (LOW) [CoinGecko, https://www.coingecko.com]
CoinMarketCap: tidak tersedia (LOW) [CoinMarketCap, https://coinmarketcap.com]
Token Terminal: tidak tersedia (LOW) [Token Terminal, https://tokenterminal.com]
Messari: tidak tersedia (LOW) [Messari, https://messari.io]
Explorer: https://explorer.irys.xyz (HIGH) [Block Explorer Resmi, https://explorer.irys.xyz]
Sources: https://irys.xyz; https://defillama.com; https://www.coingecko.com; https://coinmarketcap.com; https://tokenterminal.com; https://messari.io; https://explorer.irys.xyz

## RINGKASAN
Market Stage: Pre-TGE / Early
Primary Category: Layer 1 blockchain / Permanent data provenance layer
Competitor Count: 7 (Arweave, Filecoin, Celestia, EigenDA, Avail, 0G, Walrus)
Major Narrative: Permanent data provenance layer
Trading Availability: None (Pre-TGE)
Adoption Metrics Available: None (no public dashboard, no third-party analytics)

## Behavioral Intelligence
_ref: `docs/Ontology/Hidden.md` — enriches DecisionEvent Alternatives/Reason/Reactions_

PROJECT: Irys

Strategic Objectives

1. Membangun Layer 1 blockchain native untuk permanent data provenance
· Evidence: Website resmi Irys memposisikan proyek sebagai "permanent data provenance layer" dengan arsitektur L1 sendiri (Irys L1) yang terpisah dari Arweave [Website Resmi Irys, https://irys.xyz; Blog Resmi Irys, https://blog.irys.xyz/introducing-irys]
· Supporting Dataset: Phase 1 Foundation, Phase 4 Technology (System Architecture), Phase 8 Market (Market Category)

2. Menggunakan Arweave sebagai permanent storage layer dan Ethereum sebagai settlement/staking layer
· Evidence: Arsitektur teknis Irys secara eksplisit menggunakan Arweave untuk data blob permanen dan Ethereum untuk staking token IRYS serta keamanan ekonomi validator [Dokumentasi Arsitektur Irys, https://docs.irys.xyz/architecture; Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics]
· Supporting Dataset: Phase 4 Technology (System Architecture, Core Components), Phase 7 Ecosystem (External Dependencies), Phase 8 Market (Market Position)

3. Menyediakan provenance layer on-chain untuk verifikasi kriptografis asal-usul dan integritas data
· Evidence: Provenance Layer adalah komponen inti Irys yang menyediakan bukti kriptografis (merkle proofs, timestamps) terverifikasi on-chain [Website Resmi Irys, https://irys.xyz; Dokumentasi Arsitektur Irys, https://docs.irys.xyz/architecture]
· Supporting Dataset: Phase 1 Foundation, Phase 4 Technology (Core Components), Phase 7 Ecosystem (Major Integrations)

4. Menargetkan pasar AI/Data Provenance dan DePIN sebagai use case utama
· Evidence: Blog ekosistem dan website konstan menyebut AI training data provenance dan DePIN sebagai kategori ekosistem dan pasar sasaran [Blog Ekosistem Irys, https://blog.irys.xyz/category/ecosystem; Website Resmi Irys, https://irys.xyz]
· Supporting Dataset: Phase 1 Foundation, Phase 7 Ecosystem (Ecosystem Position), Phase 8 Market (Narrative Position)

5. Meluncurkan token IRYS dengan utility: storage payment, staking validator, governance, fee payment, incentive/reward
· Evidence: Dokumentasi tokenomics menggariskan 5 utility token IRYS: Storage Payment, Staking Validator, Governance, Fee Payment, Incentive/Reward [Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics]
· Supporting Dataset: Phase 6 Token (Utility), Phase 5 Financial (Revenue Model)

Decision Timeline

Keputusan: Pendirian Bundlr Labs, Inc. dan peluncuran Bundlr Network sebagai bundler service untuk Arweave (2021)
· Trigger: Kebutuhan menyederhanakan akses ke penyimpanan permanen Arweave dengan pembayaran multi-token
· Evidence: Terms of Service Irys mengidentifikasi Bundlr Labs, Inc. sebagai entitas pendiri; blog rebranding menjelaskan asal-usul sebagai Bundlr Network [Terms of Service Irys, https://irys.xyz/terms; Blog Resmi Irys, https://blog.irys.xyz/introducing-irys]
· Decision: Membangun bundler service di atas Arweave sebagai entry point awal ke ekosistem permanent storage
· Immediate Result: Entitas perusahaan dan protokol bundler awal beroperasi, menjadi lapisan penyederhanaan akses ke Arweave
· Long-term Impact: Menjadi fondasi teknis dan organisasi untuk transisi ke Irys L1 tahun 2024
· Supporting Dataset: Phase 2 Entity (Bundlr Labs, Inc., Bundlr Network Legacy), Phase 3 History (EV-001, EV-002)

Keputusan: Integrasi Arweave sebagai permanent storage layer (2021)
· Trigger: Arweave menyediakan penyimpanan permanen terdesentralisasi yang matang
· Evidence: Arsitektur teknis Irys mendokumentasikan Arweave sebagai storage layer sejak era Bundlr [Dokumentasi Arsitektur Irys, https://docs.irys.xyz/architecture; Blog Ekosistem Irys, https://blog.irys.xyz/category/ecosystem]
· Decision: Menggunakan Arweave sebagai backend storage bukan membangun storage layer sendiri
· Immediate Result: Data availability dan permanens data dijamin oleh jaringan Arweave yang sudah ada
· Long-term Impact: Ketergantungan kritis pada Arweave (single storage layer dependency) — risiko ecosystem teridentifikasi di Phase 7
· Supporting Dataset: Phase 4 Technology (Storage Layer), Phase 7 Ecosystem (External Dependencies, Ecosystem Risks), Phase 3 History (EV-002)

Keputusan: Peluncuran Irys SDK, dokumentasi, GitHub, dan saluran komunitas (2023)
· Trigger: Persiapan ekosistem developer sebelum mainnet dan testnet
· Evidence: Multi-channel launch terdokumentasi di Phase 3 EV-003 mencakup SDK, docs, GitHub, Discord, X, Telegram, Blog [Dokumentasi SDK Irys, https://docs.irys.xyz/sdk; Dokumentasi Irys, https://docs.irys.xyz; GitHub Irys, https://github.com/irys-xyz; Discord Irys, https://discord.gg/irys; X Irys, https://x.com/irys_xyz; Telegram Irys, https://t.me/irys_xyz; Blog Irys, https://blog.irys.xyz]
· Decision: Membangun infrastruktur developer dan komunitas secara paralel sebelum mainnet
· Immediate Result: Developer tools, dokumentasi, dan saluran komunitas live sebelum testnet
· Long-term Impact: Fondasi adopsi developer dan feedback loop untuk testnet/mainnet
· Supporting Dataset: Phase 3 History (EV-003), Phase 4 Technology (Development Framework), Phase 7 Ecosystem (Developer Ecosystem)

Keputusan: Peluncuran Incentivized Testnet Phase 1 (2024-01)
· Trigger: Perlu menguji ekonomi token, performa validator, dan provenance layer sebelum mainnet
· Evidence: Blog testnet resmi menjelaskan tujuan menguji token economics, validator performance, provenance layer [Blog Resmi Irys Testnet, https://blog.irys.xyz/irys-incentivized-testnet; Dokumentasi Irys, https://docs.irys.xyz]
· Decision: Menjalankan testnet berinsentif dengan token testnet untuk simulasi staking dan reward
· Immediate Result: Validator dan pengguna menguji jaringan, ekonomi token, dan fitur provenance
· Long-term Impact: Validasi arsitektur sebelum mainnet; data untuk parameter mainnet launch
· Supporting Dataset: Phase 3 History (EV-004), Phase 6 Token (Major Token Events), Phase 8 Market (Market Timeline)

Keputusan: Rebranding dari Bundlr Network ke Irys (2024-03)
· Trigger: Evolusi dari bundler service ke Layer 1 blockchain provenance layer memerlukan identitas baru
· Evidence: Blog rebranding resmi mengumumkan transisi arsitektur dan positioning [Blog Resmi Irys, https://blog.irys.xyz/introducing-irys; Terms of Service Irys, https://irys.xyz/terms]
· Decision: Ganti nama protokol dari Bundlr Network ke Irys, menandai transisi arsitektur
· Immediate Result: Identitas baru "Irys" diperkenalkan publik sebagai L1 blockchain provenance layer
· Long-term Impact: Positioning pasar berubah dari bundler service ke L1 sovereign dengan provenance
· Supporting Dataset: Phase 3 History (EV-005), Phase 1 Foundation, Phase 8 Market (Market Timeline)

Keputusan: Peluncuran Mainnet Irys L1 (2024-03-26)
· Trigger: Testnet selesai, siap untuk produksi
· Evidence: Blog mainnet launch resmi mengkonfirmasi tanggal 26 Maret 2024 [Blog Resmi Irys Mainnet Launch, https://blog.irys.xyz/irys-mainnet-launch; Website Resmi Irys, https://irys.xyz; Block Explorer Resmi, https://explorer.irys.xyz]
· Decision: Mengaktifkan Irys L1 sebagai blockchain Layer 1 native untuk konsensus dan eksekusi transaksi data serta provenance
· Immediate Result: Jaringan produksi Irys L1 live dengan validator, provenance layer, gateway, explorer
· Long-term Impact: Protokol operasional; token IRYS tetap pre-TGE — utility storage payment, staking, governance belum live di mainnet
· Supporting Dataset: Phase 3 History (EV-006), Phase 4 Technology (Technical Upgrade History), Phase 6 Token (Major Token Events), Phase 8 Market (Market Timeline)

Keputusan: Peluncuran Irys Explorer dan aktivasi Gateway/Provenance Layer pada mainnet (2024-03)
· Trigger: Kebutuhan verifikasi on-chain dan data retrieval untuk mainnet
· Evidence: Explorer dan Gateway diluncurkan seiring mainnet [Block Explorer Resmi, https://explorer.irys.xyz; Website Resmi Irys, https://irys.xyz; Dokumentasi Produk Irys, https://docs.irys.xyz; Dokumentasi Arsitektur Irys, https://docs.irys.xyz/architecture]
· Decision: Mengaktifkan block explorer resmi dan HTTP gateway untuk retrieval data permanen
· Immediate Result: Verifikasi transaksi/blok/akun/provenance dan retrieval data tersedia untuk pengguna
· Long-term Impact: Infrastructure observability dan data access layer operational
· Supporting Dataset: Phase 3 History (EV-007, EV-008), Phase 4 Technology (Core Components), Phase 7 Ecosystem (Applications, Infrastructure Providers)

Keputusan: Integrasi Ethereum sebagai settlement dan staking layer untuk token IRYS (2024)
· Trigger: Kebutuhan keamanan ekonomi validator via Ethereum staking/restaking
· Evidence: Tokenomics dan arsitektur mendokumentasikan Ethereum untuk staking IRYS dan validator economic security [Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics; Dokumentasi Arsitektur Irys, https://docs.irys.xyz/architecture]
· Decision: Menggunakan Ethereum sebagai settlement layer dan staking layer untuk token IRYS
· Immediate Result: Arsitektur cross-chain Irys-Ethereum untuk keamanan ekonomi ditetapkan
· Long-term Impact: Ketergantungan kritis pada Ethereum (single settlement layer dependency); token contract belum deploy pre-TGE
· Supporting Dataset: Phase 3 History (EV-009), Phase 4 Technology (Settlement Layer, Core Components), Phase 6 Token (Utility), Phase 7 Ecosystem (External Dependencies, Ecosystem Risks)

Keputusan: Publikasi tokenomics IRYS (pre-TGE) (2024)
· Trigger: Transparansi ekonomi token sebelum TGE
· Evidence: Dokumentasi tokenomics dipublikasikan di docs.irys.xyz/tokenomics [Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics; Blog Resmi Irys, https://blog.irys.xyz/introducing-irys]
· Decision: Mempublikasikan garis besar alokasi, utilitas, dan status pre-TGE tanpa detail numerik (persentase, vesting, cliff, TGE schedule)
· Immediate Result: Kerangka ekonomi token terpublikasi; detail numerik tetap tidak diungkapkan
· Long-term Impact: Investor/analis tidak bisa memodelkan supply dynamics; transparency gap teridentifikasi di Phase 6 dan Phase 8
· Supporting Dataset: Phase 3 History (EV-010), Phase 6 Token (Token Information, Supply, Distribution, Vesting, TGE, Governance), Phase 5 Financial (Token Sale), Phase 8 Market (Adoption Metrics)

Evolution Pattern

Perubahan Strategi: Dari Bundler Service (Bundlr Network) ke Layer 1 Blockchain Sovereign (Irys L1)
· Evidence: Phase 3 EV-001 (2021) mendirikan Bundlr Network sebagai bundler untuk Arweave; Phase 3 EV-005 (2024-03) mengumumkan rebranding ke Irys sebagai L1 blockchain; Phase 3 EV-006 (2024-03-26) meluncurkan mainnet Irys L1 dengan konsensus sendiri [Blog Resmi Irys, https://blog.irys.xyz/introducing-irys; Blog Resmi Irys Mainnet Launch, https://blog.irys.xyz/irys-mainnet-launch]
· Supporting Dataset: Phase 1 Foundation, Phase 2 Entity (Bundlr Network Legacy vs Irys L1), Phase 3 History (EV-001, EV-005, EV-006), Phase 8 Market (Market Timeline)

Perubahan Teknologi: Arsitektur modular dengan tiga layer terpisah (Execution/Provenance di Irys L1, Storage di Arweave, Settlement/Staking di Ethereum)
· Evidence: Phase 4 Technology mendokumentasikan arsitektur dengan Irys L1 sebagai validator/consensus layer, Provenance Layer native, Arweave Integration sebagai storage layer, Ethereum Staking Contracts sebagai settlement layer [Dokumentasi Arsitektur Irys, https://docs.irys.xyz/architecture]
· Supporting Dataset: Phase 4 Technology (System Architecture, Core Components), Phase 7 Ecosystem (External Dependencies, Major Integrations)

Perubahan Tokenomics: Dari tidak ada token (era Bundlr) ke token IRYS dengan 5 utility (storage payment, staking, governance, fee payment, incentive) — tetapi pre-TGE tanpa detail numerik
· Evidence: Phase 6 Token mendokumentasikan status pre-TGE, 5 utility, 6 kategori alokasi (Community, Team, Investors, Foundation, Treasury, Ecosystem) semua "Planned" tanpa persentase, vesting, cliff, TGE date [Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics]
· Supporting Dataset: Phase 3 History (EV-010), Phase 5 Financial (Token Sale), Phase 6 Token (Token Information, Supply, Distribution, Vesting, TGE, Utility, Governance), Phase 8 Market (Trading Markets, Liquidity)

Perubahan Governance: Dari centralized development (Bundlr Labs, Inc.) menuju arah DAO/governance on-chain (belum terbentuk)
· Evidence: Phase 2 Entity hanya mengidentifikasi Bundlr Labs, Inc. sebagai core developer; Phase 6 Token Governance status "Belum terbentuk (Pre-TGE)"; Phase 7 Ecosystem Governance Ecosystem: Foundation, DAO, Council, Committee, Validator Group semua "tidak diketahui/belum terbentuk" [Terms of Service Irys, https://irys.xyz/terms; Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics]
· Supporting Dataset: Phase 2 Entity (Bundlr Labs, Inc.), Phase 6 Token (Governance), Phase 7 Ecosystem (Governance Ecosystem), Phase 8 Market (Market Position)

Perubahan Market Position: Dari bundler service niche ke L1 blockchain kompetitor langsung dengan Arweave, Filecoin, Celestia, EigenDA, Avail, 0G, Walrus
· Evidence: Phase 8 Market Competitor Landscape mencantumkan 7 kompetitor utama; Phase 1 Foundation positioning sebagai "Permanent data provenance layer / Layer 1 blockchain" [Dokumentasi Arsitektur Irys, https://docs.irys.xyz/architecture; Blog Ekosistem Irys, https://blog.irys.xyz/category/ecosystem]
· Supporting Dataset: Phase 1 Foundation, Phase 8 Market (Market Category, Market Position, Competitor Landscape, Narrative Position)

Technical Decision Pattern

Pola 1: Modular Architecture dengan External Dependencies Kritis
· Decision Pattern: Memisahkan fungsi inti ke layer eksternal yang sudah mature (Arweave untuk storage, Ethereum untuk settlement/staking) sambil membangun L1 sendiri untuk execution/provenance
· Evidence: System Architecture Phase 4 mendokumentasikan Storage Layer: Arweave, Settlement Layer: Ethereum, Provenance Layer: Native on-chain Irys L1 [Dokumentasi Arsitektur Irys, https://docs.irys.xyz/architecture]; Phase 7 Ecosystem mengidentifikasi Arweave dan Ethereum sebagai "Critical" external dependencies [Dokumentasi Arsitektur Irys, https://docs.irys.xyz/architecture; Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics]
· Supporting Dataset: Phase 4 Technology (System Architecture, Core Components), Phase 7 Ecosystem (External Dependencies, Ecosystem Risks)

Pola 2: Provenance Layer sebagai Differentiator Teknis Utama
· Decision Pattern: Membangun lapisan provenance native on-chain (merkle proofs, timestamps, cryptographic proofs) sebagai value proposition unik di atas storage permanen
· Evidence: Website resmi dan arsitektur teknis menempatkan Provenance Layer sebagai komponen inti terpisah dari storage layer [Website Resmi Irys, https://irys.xyz; Dokumentasi Arsitektur Irys, https://docs.irys.xyz/architecture]; Phase 4 Core Components lists Provenance Layer sebagai komponen utama [Dokumentasi Arsitektur Irys, https://docs.irys.xyz/architecture]
· Supporting Dataset: Phase 1 Foundation, Phase 4 Technology (Core Components, System Architecture), Phase 8 Market (Narrative Position)

Pola 3: TypeScript/JavaScript First untuk SDK dan Developer Tooling
· Decision Pattern: Menggunakan TypeScript/JavaScript (Node.js, Browser) untuk Irys SDK, CLI, dan tooling — memprioritaskan developer experience web2/web3 hybrid
· Evidence: Phase 4 Technology mendokumentasikan SDK Language: TypeScript/JavaScript, CLI: TypeScript/JavaScript berbasis Node.js [Dokumentasi SDK Irys, https://docs.irys.xyz/sdk; Repositori GitHub Irys, https://github.com/irys-xyz]; Phase 7 Developer Ecosystem mengonfirmasi SDK, API, CLI, GitHub, Docs [Dokumentasi SDK Irys, https://docs.irys.xyz/sdk; Repositori GitHub Irys, https://github.com/irys-xyz; Dokumentasi Produk Irys, https://docs.irys.xyz]
· Supporting Dataset: Phase 4 Technology (Programming Languages, Development Framework), Phase 7 Ecosystem (Developer Ecosystem)

Pola 4: Custom L1 Consensus (Non-Standard Framework)
· Decision Pattern: Membangun konsensus custom bukan menggunakan framework standar (Cosmos SDK, Substrate, OP Stack) — detail konsensus tidak dipublikasikan
· Evidence: Phase 4 Technology Current Technical Stack: "Blockchain Framework: Custom L1 (tidak berbasis Cosmos SDK, Substrate, atau OP Stack secara eksplisit terdokumentasi)" [Dokumentasi Arsitektur Irys, https://docs.irys.xyz/architecture]; Consensus Mechanism: "Tidak terdokumentasi secara detail di sumber primer" [Dokumentasi Arsitektur Irys, https://docs.irys.xyz/architecture]
· Supporting Dataset: Phase 4 Technology (Consensus Mechanism, Current Technical Stack, Known Technical Limitations)

Pola 5: Staged Launch dengan Testnet Berinsentif Sebelum Mainnet
· Decision Pattern: Menjalankan Incentivized Testnet Phase 1 (Jan 2024) untuk menguji ekonomi token, validator performance, provenance layer sebelum mainnet launch (Mar 2024)
· Evidence: Phase 3 History EV-004 (Testnet Jan 2024) → EV-006 (Mainnet Mar 2024) [Blog Resmi Irys Testnet, https://blog.irys.xyz/irys-incentivized-testnet; Blog Resmi Irys Mainnet Launch, https://blog.irys.xyz/irys-mainnet-launch]; Phase 4 Technical Upgrade History mencatat kedua event [Dokumentasi Arsitektur Irys, https://docs.irys.xyz/architecture]
· Supporting Dataset: Phase 3 History (EV-004, EV-006), Phase 4 Technology (Technical Upgrade History), Phase 8 Market (Market Timeline)

Pola 6: Tidak Ada Public Security Audit Sebelum Mainnet Launch
· Decision Pattern: Meluncurkan mainnet tanpa mempublikasikan laporan audit keamanan (consensus, cryptography, smart contracts) di website/docs resmi
· Evidence: Phase 4 Technology Audit History: "Tidak ditemukan riwayat audit keamanan... yang dipublikasikan secara resmi" [Website Resmi Irys, https://irys.xyz; Blog Resmi Irys, https://blog.irys.xyz; Dokumentasi Irys, https://docs.irys.xyz]; Phase 7 Ecosystem Risks: "No Public Security Audits" [Website Resmi Irys, https://irys.xyz; Dokumentasi Irys, https://docs.irys.xyz; Blog Resmi Irys, https://blog.irys.xyz]
· Supporting Dataset: Phase 4 Technology (Audit History, Security Model), Phase 7 Ecosystem (Ecosystem Risks), Phase 8 Market (Adoption Metrics)

Financial Decision Pattern

Pola 1: Tidak Mengungkapkan Funding History, Treasury, dan Investor sama sekali
· Decision Pattern: Zero transparency pada funding rounds, investor list, valuation, treasury size, composition, custodian — semua "Tidak diungkap" di Phase 5
· Evidence: Phase 5 Financial Funding History, Treasury, Revenue History, Fundraising Mechanism, Financial Dependencies, Financial Risk semua "Tidak diungkap (LOW)" [Website Resmi Irys, https://irys.xyz; Blog Resmi Irys, https://blog.irys.xyz; Dokumentasi Irys, https://docs.irys.xyz; Terms of Service Irys, https://irys.xyz/terms]
· Supporting Dataset: Phase 5 Financial (Funding History, Treasury, Revenue History, Fundraising Mechanism, Financial Dependencies, Financial Risk, Official Financial Resources)

Pola 2: Revenue Model Berbasis Protocol Fees Yang Belum Live (Pre-TGE)
· Decision Pattern: Merencanakan tiga revenue stream (Protocol Fees/Storage Payments, Staking Fees/Validator Rewards, Governance Fees) semuanya status "Planned (Pre-TGE)" — tidak ada revenue actual
· Evidence: Phase 5 Financial Revenue Model mencatat ketiga stream dengan status "Planned (Pre-TGE)" [Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics]; Phase 6 Token Utility mengonfirmasi Storage Payment, Staking Validator, Fee Payment sebagai utility yang "Planned (Pre-TGE)" [Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics]
· Supporting Dataset: Phase 5 Financial (Revenue Model), Phase 6 Token (Utility), Phase 8 Market (Trading Markets, Liquidity)

Pola 3: Token Sale dan Fundraising Mechanism Tidak Diungkapkan
· Decision Pattern: Tidak ada informasi apapun tentang private sale, public sale, launchpad, auction, community sale, mecanismo fundraising — semua "Tidak diungkap (LOW)" atau "Pre-TGE"
· Evidence: Phase 5 Financial Token Sale: semua field "Tidak diungkap (LOW)"; Fundraising Mechanism: "Tidak diungkap (LOW)" [Website Resmi Irys, https://irys.xyz; Blog Resmi Irys, https://blog.irys.xyz; Dokumentasi Irys, https://docs.irys.xyz]; Phase 6 Token TGE: "belum dijadwalkan resmi (Pre-TGE)" [Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics]
· Supporting Dataset: Phase 5 Financial (Token Sale, Fundraising Mechanism), Phase 6 Token (TGE, Distribution, Vesting Schedule), Phase 8 Market (Trading Markets, Liquidity)

Pola 4: Tidak Ada Financial Transparency Infrastructure (Dashboard, Reports, Third-party Analytics)
· Decision Pattern: Tidak menyediakan transparency report, treasury dashboard, governance forum, atau listing di Messari/Token Terminal/DefiLlama/CryptoRank
· Evidence: Phase 5 Official Financial Resources: semua "Tidak tersedia (LOW)" [Website Resmi Irys, https://irys.xyz; Blog Resmi Irys, https://blog.irys.xyz; Dokumentasi Irys, https://docs.irys.xyz]; Phase 8 Official Market Resources: DefiLlama, CoinGecko, CoinMarketCap, Token Terminal, Messari semua "Tidak tersedia (LOW)" [DefiLlama, https://defillama.com; CoinGecko, https://www.coingecko.com; CoinMarketCap, https://coinmarketcap.com; Token Terminal, https://tokenterminal.com; Messari, https://messari.io]
· Supporting Dataset: Phase 5 Financial (Official Financial Resources), Phase 8 Market (Official Market Resources, Adoption Metrics)

Ecosystem Decision Pattern

Pola 1: Deep Integration dengan Arweave sebagai Single Storage Layer (Critical Dependency)
· Decision Pattern: Menggunakan Arweave sebagai exclusive permanent storage layer sejak era Bundlr (2021) hingga sekarang — tidak ada multi-storage strategy
· Evidence: Phase 3 EV-002 (2021) integrasi Arweave; Phase 4 Storage Layer: Arweave; Phase 7 External Dependencies: Arweave "Critical"; Major Integrations: Arweave Storage Integration "Live"; Infrastructure Providers: Arweave "Critical" [Dokumentasi Arsitektur Irys, https://docs.irys.xyz/architecture; Blog Ekosistem Irys, https://blog.irys.xyz/category/ecosystem]
· Supporting Dataset: Phase 3 History (EV-002), Phase 4 Technology (System Architecture, Core Components), Phase 7 Ecosystem (External Dependencies, Major Integrations, Infrastructure Providers, Ecosystem Risks)

Pola 2: Ethereum sebagai Settlement/Staking Layer Exclusive (Critical Dependency)
· Decision Pattern: Memilih Ethereum sebagai single settlement dan staking layer untuk token IRYS dan validator economic security — tidak ada alternative chain
· Evidence: Phase 4 Settlement Layer: Ethereum; Phase 7 External Dependencies: Ethereum "Critical"; Major Integrations: Ethereum Staking/Settlement Integration "Live"; Infrastructure Providers: Ethereum "Critical" [Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics; Dokumentasi Arsitektur Irys, https://docs.irys.xyz/architecture]
· Supporting Dataset: Phase 3 History (EV-009), Phase 4 Technology (System Architecture, Core Components), Phase 6 Token (Utility), Phase 7 Ecosystem (External Dependencies, Major Integrations, Infrastructure Providers, Ecosystem Risks)

Pola 3: First-Party Infrastructure Development (Gateway, Explorer, SDK, Docs, CLI)
· Decision Pattern: Membangun dan mengoperasikan seluruh infrastructure stack sendiri: Gateway, Explorer, SDK, Documentation, CLI, GitHub org — minimal third-party infra providers
· Evidence: Phase 7 Applications: 6 first-party apps (Explorer, Gateway, SDK, Docs, Testnet, Legacy Bundlr); Infrastructure Providers: Irys Gateway "High", Irys Explorer "High", GitHub "Medium", Discord "Medium" — semua self-operated kecuali GitHub/Discord [Block Explorer Resmi, https://explorer.irys.xyz; Dokumentasi Produk Irys, https://docs.irys.xyz; Website Resmi Irys, https://irys.xyz; Dokumentasi SDK Irys, https://docs.irys.xyz/sdk; Repositori GitHub Irys, https://github.com/irys-xyz; Discord Irys, https://discord.gg/irys]
· Supporting Dataset: Phase 4 Technology (Core Components), Phase 7 Ecosystem (Applications, Infrastructure Providers, Developer Ecosystem)

Pola 4: Developer-First Ecosystem tanpa Grant Program/Hackathon Publik
· Decision Pattern: Menyediakan SDK, API, CLI, Docs, GitHub sebagai developer tooling tetapi tidak meluncurkan grant program, hackathon, atau accelerator program yang terdokumentasi publik
· Evidence: Phase 7 Developer Ecosystem: SDK, API, CLI, GitHub, Docs "Live"; Hackathon: "tidak diketahui (LOW)"; Grant Program: "tidak diketahui (LOW)" [Dokumentasi SDK Irys, https://docs.irys.xyz/sdk; Repositori GitHub Irys, https://github.com/irys-xyz; Dokumentasi Produk Irys, https://docs.irys.xyz; Blog Resmi Irys, https://blog.irys.xyz; Website Resmi Irys, https://irys.xyz]
· Supporting Dataset: Phase 4 Technology (Development Framework), Phase 7 Ecosystem (Developer Ecosystem, Official Ecosystem Resources), Phase 8 Market (Adoption Metrics)

Pola 5: Narasi AI/DePIN Tanpa Bukti Adopsi Teknis Terverifikasi
· Decision Pattern: Mengklaim AI/Data Provenance dan DePIN sebagai secondary narrative dan market segment tetapi tidak mempublikasikan nama proyek terintegrasi, volume data, atau partnership teknis spesifik
· Evidence: Phase 1 Foundation Category: "AI/Data Provenance; DePIN"; Phase 7 Ecosystem Position: "AI/Data Provenance; DePIN (MEDIUM)"; Phase 8 Narrative Position: "AI data provenance (Secondary)", "DePIN (Secondary)" — semua berbasis blog category/website claims tanpa bukti adopsi [Blog Ekosistem Irys, https://blog.irys.xyz/category/ecosystem; Website Resmi Irys, https://irys.xyz; Dokumentasi Arsitektur Irys, https://docs.irys.xyz/architecture]
· Supporting Dataset: Phase 1 Foundation, Phase 7 Ecosystem (Ecosystem Position, Major Integrations), Phase 8 Market (Market Position, Narrative Position, Competitor Landscape)

Governance Decision Pattern

Pola 1: Centralized Development di Bawah Bundlr Labs, Inc. Tanpa Foundation Terpisah
· Decision Pattern: Seluruh pengembangan protokol (L1, SDK, Gateway, Provenance) dikendalikan oleh single entity Bundlr Labs, Inc. — tidak ada Irys Foundation terpisah yang teridentifikasi
· Evidence: Phase 2 Entity: Bundlr Labs, Inc. "Entitas pendiri dan pengembang inti"; Terms of Service mengikat pengguna pada Bundlr Labs, Inc.; Phase 7 Governance Ecosystem: Foundation "tidak diketahui (tidak ada entitas foundation terpisah teridentifikasi)" [Terms of Service Irys, https://irys.xyz/terms; Blog Resmi Irys, https://blog.irys.xyz/introducing-irys; Website Resmi Irys, https://irys.xyz]
· Supporting Dataset: Phase 2 Entity (Bundlr Labs, Inc., Irys Terms of Service), Phase 7 Ecosystem (Governance Ecosystem), Phase 8 Market (Market Position)

Pola 2: Token Governance Direncanakan Tapi Belum Terbentuk (Pre-TGE Blocker)
· Decision Pattern: Tokenomics menggariskan "Governance" sebagai utility token IRYS tetapi governance model, voting system, proposal system, delegation, treasury governance semua "tidak diketahui" dan status "Belum terbentuk (Pre-TGE)"
· Evidence: Phase 6 Token Governance: semua field "tidak diketahui (LOW)", Status: "Belum terbentuk (Pre-TGE)" [Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics; Website Resmi Irys, https://irys.xyz; Blog Resmi Irys, https://blog.irys.xyz]; Phase 7 Governance Ecosystem: DAO "tidak diketahui (belum terbentuk, pre-TGE)" [Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics; Website Resmi Irys, https://irys.xyz]
· Supporting Dataset: Phase 6 Token (Governance, Utility), Phase 7 Ecosystem (Governance Ecosystem), Phase 3 History (EV-010)

Pola 3: Validator Set Tidak Transparan (Genesis Validator Unidentified)
· Decision Pattern: Genesis validator set dan infrastructure provider di baliknya tidak diungkapkan secara publik — block explorer tidak menampilkan halaman validator set detail
· Evidence: Phase 7 Governance Ecosystem: Validator Group "tidak diketahui (genesis validator set tidak diungkapkan secara publik)"; Phase 8 Adoption Metrics: Validator Count "Tidak tersedia (genesis validator set tidak diungkapkan publik; explorer tidak menampilkan halaman validator set)" [Blog Mainnet Launch, https://blog.irys.xyz/irys-mainnet-launch; Block Explorer Resmi, https://explorer.irys.xyz]
· Supporting Dataset: Phase 3 History (EV-006), Phase 4 Technology (Security Model, Known Technical Limitations), Phase 7 Ecosystem (Governance Ecosystem, Ecosystem Risks), Phase 8 Market (Adoption Metrics)

Pola 4: Tidak Ada On-Chain Governance Mechanism Live
· Decision Pattern: Tidak ada snapshot, forum governance, DAO voting, atau proposal system yang operational — semua governance off-chain dan centralized ke Bundlr Labs, Inc.
· Evidence: Phase 6 Token Governance: Proposal System "tidak diketahui"; Phase 7 Governance Ecosystem: DAO, Council, Committee semua "tidak diketahui"; Phase 2 Entity hanya Bundlr Labs, Inc. sebagai company [Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics; Website Resmi Irys, https://irys.xyz; Blog Resmi Irys, https://blog.irys.xyz; Terms of Service Irys, https://irys.xyz/terms]
· Supporting Dataset: Phase 2 Entity, Phase 6 Token (Governance), Phase 7 Ecosystem (Governance Ecosystem)

Risk Response Pattern

Pola 1: Single Point of Failure Mitigation Via Architecture Design (Tapi Tidak Eliminasi Dependency)
· Decision Pattern: Arsitektur modular memisahkan storage (Arweave), settlement (Ethereum), execution (Irys L1) — namun masing-masing layer memiliki single critical dependency tanpa fallback
· Evidence: Phase 7 Ecosystem Risks: "Single Storage Layer Dependency (Arweave)" — outage Arweave berdampak langsung ketersediaan data Irys; "Single Settlement Layer Dependency (Ethereum)" — congestion/fork Ethereum mempengaruhi operasi validator Irys [Dokumentasi Arsitektur Irys, https://docs.irys.xyz/architecture; Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics]
· Trigger: Desain arsitektur modular yang bergantung pada layer eksternal yang sudah mature
· Response: Memisahkan concerns ke layer specialist (Arweave untuk storage, Ethereum untuk economic security) — acceptance of dependency risk
· Result: Critical dependencies teridentifikasi tapi tidak ada mitigation plan yang dipublikasikan (multi-storage, multi-settlement, atau fallback mechanism)
· Supporting Dataset: Phase 4 Technology (System Architecture), Phase 7 Ecosystem (External Dependencies, Ecosystem Risks), Phase 8 Market (Market Position)

Pola 2: Centralized Development Risk Mitigation Via Open Source dan Community Channels
· Decision Pattern: Mengembangkan core protocol closed/centralized di Bundlr Labs tapi membuka SDK, docs, GitHub, Discord, X, Telegram untuk community feedback dan transparency
· Evidence: Phase 7 Ecosystem Risks: "Centralized Development Dependency (Bundlr Labs, Inc.)" — single entity tanpa foundation/DAO; Developer Ecosystem: SDK, API, CLI, GitHub, Docs live; Community: Discord, X, Telegram active [Terms of Service Irys, https://irys.xyz/terms; Blog Resmi Irys, https://blog.irys.xyz/introducing-irys; Dokumentasi SDK Irys, https://docs.irys.xyz/sdk; Repositori GitHub Irys, https://github.com/irys-xyz; Discord Irys, https://discord.gg/irys; X Irys, https://x.com/irys_xyz]
· Trigger: Kebutuhan kecepatan eksekusi dan koordinasi teknis di early stage
· Response: Open source tooling dan komunitas channels untuk external input — tetapi governance tetap centralized
· Result: Developer tooling transparent; protocol governance tidak — risk tetap ada hingga DAO/Foundation terbentuk
· Supporting Dataset: Phase 2 Entity (Bundlr Labs, Inc.), Phase 4 Technology (Development Framework), Phase 7 Ecosystem (Developer Ecosystem, Governance Ecosystem, Ecosystem Risks)

Pola 3: Pre-TGE Economic Risk Mitigation Via Incentivized Testnet
· Decision Pattern: Menjalankan Incentivized Testnet Phase 1 (Jan 2024) untuk menguji token economics, validator performance, provenance layer sebelum mainnet dan TGE
· Evidence: Phase 3 History EV-004: Testnet berinsentif untuk "menguji ekonomi token, performa validator, dan lapisan provenance"; Phase 6 Major Token Events: Testnet "Token testnet digunakan untuk simulasi staking dan reward" [Blog Resmi Irys Testnet, https://blog.irys.xyz/irys-incentivized-testnet; Dokumentasi Irys, https://docs.irys.xyz]
· Trigger: Tokenomics belum tervalidasi di mainnet; perlu data empiris untuk parameter mainnet
· Response: Testnet berinsentif dengan token testnet (bukan mainnet token) untuk simulasi ekonomi
· Result: Validasi arsitektur sebelum mainnet; tapi token testnet → mainnet conversion/claim tidak diklarifikasi (Phase 6 Open Threads)
· Supporting Dataset: Phase 3 History (EV-004), Phase 6 Token (Major Token Events, Utility), Phase 8 Market (Market Timeline)

Pola 4: Security Audit Risk — Tidak Ada Respons Publik (Silent Acceptance)
· Decision Pattern: Meluncurkan mainnet tanpa mempublikasikan audit — tidak ada emergency response, bug bounty program, atau audit announcement
· Evidence: Phase 4 Audit History: "Tidak ditemukan riwayat audit keamanan... yang dipublikasikan secara resmi"; Phase 7 Ecosystem Risks: "No Public Security Audits" [Website Resmi Irys, https://irys.xyz; Blog Resmi Irys, https://blog.irys.xyz; Dokumentasi Irys, https://docs.irys.xyz]
· Trigger: Mainnet launch deadline (Mar 2024) mungkin memprioritaskan launch over audit publication
· Response: Tidak ada respons publik yang terdokumentasi — silent launch tanpa audit transparency
· Result: Security validation gap; community/validator tidak bisa memverifikasi security posture
· Supporting Dataset: Phase 4 Technology (Audit History, Security Model), Phase 7 Ecosystem (Ecosystem Risks), Phase 8 Market (Adoption Metrics)

Recurring Behavioral Pattern

Pola 1: Build First, Decentralize Later (Progressive Decentralization)
· Decision Pattern: Mulai dari centralized entity (Bundlr Labs, Inc.) → buat protokol → mainnet launch → rencanakan token/DAO/governance pasca-TGE
· Evidence: Phase 2: Bundlr Labs sebagai single core developer; Phase 3: EV-001 founding → EV-006 mainnet launch → EV-010 tokenomics publication (pre-TGE); Phase 6: Governance "Belum terbentuk (Pre-TGE)"; Phase 7: Foundation/DAO "tidak diketahui/belum terbentuk" [Terms of Service Irys, https://irys.xyz/terms; Blog Resmi Irys, https://blog.irys.xyz/introducing-irys; Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics; Website Resmi Irys, https://irys.xyz]
· Supporting Dataset: Phase 2 Entity, Phase 3 History (EV-001, EV-006, EV-010), Phase 6 Token (Governance, TGE), Phase 7 Ecosystem (Governance Ecosystem), Phase 8 Market (Market Timeline)

Pola 2: Leverage Existing L1s untuk Security/Storage, Build Custom untuk Differentiation
· Decision Pattern: Gunakan Arweave (storage) + Ethereum (settlement/staking) yang sudah battle-tested, bangun custom L1 hanya untuk provenance layer dan execution
· Evidence: Phase 4 System Architecture: Storage Layer Arweave, Settlement Layer Ethereum, Provenance Layer Native Irys L1; Phase 7 External Dependencies: Arweave "Critical", Ethereum "Critical" [Dokumentasi Arsitektur Irys, https://docs.irys.xyz/architecture; Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics]
· Supporting Dataset: Phase 4 Technology (System Architecture, Core Components), Phase 7 Ecosystem (External Dependencies, Major Integrations), Phase 8 Market (Market Position)

Pola 3: Announce Narrative/Positioning Before Technical Details Are Public
· Decision Pattern: Website/blog mengklaim "AI data provenance", "DePIN", "permanent data provenance layer" sebagai positioning — tapi technical specs (consensus, VM, TPS, validator requirements) tidak dipublikasikan
· Evidence: Phase 1 Foundation Category; Phase 8 Narrative Position: 5 narratives diklaim; Phase 4 Known Technical Limitations: Throughput/Latency "Tidak dipublikasikan", Smart Contract Generality "Tidak diketahui", Validator Hardware Requirements "Tidak dipublikasikan" [Website Resmi Irys, https://irys.xyz; Blog Resmi Irys, https://blog.irys.xyz/introducing-irys; Dokumentasi Arsitektur Irys, https://docs.irys.xyz/architecture]
· Supporting Dataset: Phase 1 Foundation, Phase 4 Technology (Known Technical Limitations, Consensus Mechanism, Execution Environment), Phase 8 Market (Narrative Position, Market Category)

Pola 4: Minimal Quantitative Transparency (Financial, Token, Adoption)
· Decision Pattern: Secara konsisten tidak mempublikasikan angka kuantitatif: funding amount, investor names, treasury size, token allocation %, vesting schedule, TGE date, TVL, DAU, transaction volume, validator count
· Evidence: Phase 5 Financial: semua "Tidak diungkap"; Phase 6 Token: Supply "tidak diketahui", Distribution "persentase tidak diungkap", Vesting "tidak diketahui", TGE "belum dijadwalkan"; Phase 8 Adoption Metrics: TVL, DAU, Transactions, Wallets, Developer Count, Volume, Validator Count semua "Tidak tersedia" [Website Resmi Irys, https://irys.xyz; Blog Resmi Irys, https://blog.irys.xyz; Dokumentasi Irys, https://docs.irys.xyz; Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics; Block Explorer Resmi, https://explorer.irys.xyz; DefiLlama, https://defillama.com; Token Terminal, https://tokenterminal.com]
· Supporting Dataset: Phase 5 Financial (Funding History, Treasury, Revenue History, Token Sale), Phase 6 Token (Supply, Distribution, Vesting Schedule, TGE, Holder Distribution), Phase 8 Market (Adoption Metrics, Trading Markets, Liquidity)

Pola 5: First-Party Infrastructure Ownership
· Decision Pattern: Membangun dan mengoperasikan sendiri: Gateway, Explorer, SDK, Docs, CLI, GitHub org, Blog, Discord, X, Telegram — minimal reliance on third-party infrastructure providers
· Evidence: Phase 7 Applications: 6 first-party apps; Infrastructure Providers: Irys Gateway "High", Irys Explorer "High" (self-operated); hanya GitHub dan Discord sebagai third-party [Block Explorer Resmi, https://explorer.irys.xyz; Dokumentasi Produk Irys, https://docs.irys.xyz; Website Resmi Irys, https://irys.xyz; Dokumentasi SDK Irys, https://docs.irys.xyz/sdk; Repositori GitHub Irys, https://github.com/irys-xyz; Discord Irys, https://discord.gg/irys]
· Supporting Dataset: Phase 4 Technology (Core Components), Phase 7 Ecosystem (Applications, Infrastructure Providers, Developer Ecosystem)

Strategic Trade-offs

Trade-off 1: Desentralisasi vs Kecepatan Eksekusi (Time-to-Market)
· Decision: Meluncurkan mainnet dengan centralized development (Bundlr Labs, Inc.) dan tanpa DAO/Foundation, token pre-TGE, validator set tidak transparan
· Trade-off: Mengorbankan desentralisasi dan governance transparency demi kecepatan mainnet launch (Mar 2024) setelah testnet Jan 2024
· Evidence: Phase 3: EV-004 testnet Jan → EV-006 mainnet Mar (2 bulan); Phase 7: Governance Ecosystem semua "tidak diketahui/belum terbentuk"; Phase 4: Audit History "Tidak ditemukan" [Blog Resmi Irys Testnet, https://blog.irys.xyz/irys-incentivized-testnet; Blog Resmi Irys Mainnet Launch, https://blog.irys.xyz/irys-mainnet-launch; Terms of Service Irys, https://irys.xyz/terms; Website Resmi Irys, https://irys.xyz]
· Supporting Dataset: Phase 3 History (EV-004, EV-006), Phase 4 Technology (Audit History), Phase 7 Ecosystem (Governance Ecosystem, Ecosystem Risks)

Trade-off 2: Single Storage Layer Dependency (Arweave) vs Storage Permanence Guarantee
· Decision: Menggunakan Arweave sebagai exclusive permanent storage layer tanpa multi-storage fallback
· Trade-off: Mengorbankan redundancy dan sovereignty over storage layer demi jaminan permanens data yang sudah battle-tested di Arweave
· Evidence: Phase 4: Storage Layer Arweave; Phase 7: External Dependencies Arweave "Critical", Ecosystem Risks "Single Storage Layer Dependency" [Dokumentasi Arsitektur Irys, https://docs.irys.xyz/architecture; Blog Ekosistem Irys, https://blog.irys.xyz/category/ecosystem]
· Supporting Dataset: Phase 4 Technology (System Architecture, Core Components), Phase 7 Ecosystem (External Dependencies, Ecosystem Risks)

Trade-off 3: Single Settlement Layer Dependency (Ethereum) vs Economic Security
· Decision: Menggunakan Ethereum sebagai exclusive settlement/staking layer untuk token IRYS dan validator economic security
· Trade-off: Mengorbankan chain sovereignty dan exposure ke Ethereum congestion/fork risk demi keamanan ekonomi dari validator set yang di-secure oleh Ethereum staking
· Evidence: Phase 4: Settlement Layer Ethereum; Phase 7: External Dependencies Ethereum "Critical", Ecosystem Risks "Single Settlement Layer Dependency" [Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics; Dokumentasi Arsitektur Irys, https://docs.irys.xyz/architecture]
· Supporting Dataset: Phase 3 History (EV-009), Phase 4 Technology (System Architecture, Core Components), Phase 6 Token (Utility), Phase 7 Ecosystem (External Dependencies, Ecosystem Risks)

Trade-off 4: Custom L1 Consensus (Non-Standard) vs Differentiation/Flexibility
· Decision: Membangun custom consensus bukan menggunakan Cosmos SDK/Substrate/OP Stack — detail tidak dipublikasikan
· Trade-off: Mengorbankan interoperability, developer familiarity, dan battle-tested codebase demi flexibility dan differentiation pada provenance layer
· Evidence: Phase 4: Current Technical Stack "Custom L1 (tidak berbasis Cosmos SDK, Substrate, atau OP Stack)"; Consensus Mechanism "Tidak terdokumentasi secara detail"; Known Technical Limitations: Cross-chain Interoperability "Hanya terdokumentasi integrasi Ethereum-Arweave" [Dokumentasi Arsitektur Irys, https://docs.irys.xyz/architecture]
· Supporting Dataset: Phase 4 Technology (Consensus Mechanism, Current Technical Stack, Known Technical Limitations), Phase 7 Ecosystem (Major Integrations, Ecosystem Risks)

Trade-off 5: Narrative-First Positioning (AI/DePIN) vs Technical Substance Transparency
· Decision: Mengklaim AI data provenance dan DePIN sebagai market segment tanpa mempublikasikan partnership teknis, volume data, atau nama proyek terintegrasi
· Trade-off: Mengorbankan credibility dan verifiability bagi narrative strength dan market positioning
· Evidence: Phase 1: Category "AI/Data Provenance; DePIN"; Phase 8: Narrative Position "AI data provenance (Secondary)", "DePIN (Secondary)" — semua berbasis claims; Phase 7: Major Integrations hanya Arweave, Ethereum, SDK, Gateway — tidak ada AI/DePIN project spesifik [Website Resmi Irys, https://irys.xyz; Blog Ekosistem Irys, https://blog.irys.xyz/category/ecosystem; Dokumentasi Arsitektur Irys, https://docs.irys.xyz/architecture]
· Supporting Dataset: Phase 1 Foundation, Phase 7 Ecosystem (Ecosystem Position, Major Integrations), Phase 8 Market (Narrative Position, Market Position)

Trade-off 6: Zero Financial/Token Transparency vs Strategic Opacity
· Decision: Tidak mengungkapkan funding, treasury, token allocation %, vesting, TGE schedule, investor list
· Trade-off: Mengorbankan investor/analyst confidence dan community trust demi strategic flexibility dalam token launch dan negotiation leverage
· Evidence: Phase 5: semua "Tidak diungkap"; Phase 6: Supply/Distribution/Vesting/TGE semua "tidak diketahui/belum dijadwalkan"; Phase 8: Trading Markets "N/A (Pre-TGE)" [Website Resmi Irys, https://irys.xyz; Blog Resmi Irys, https://blog.irys.xyz; Dokumentasi Irys, https://docs.irys.xyz; Dokumentasi Tokenomics Irys, https://docs.irys.xyz/tokenomics]
· Supporting Dataset: Phase 5 Financial (Funding History, Treasury, Token Sale), Phase 6 Token (Supply, Distribution, Vesting Schedule, TGE), Phase 8 Market (Trading Markets, Liquidity, Adoption Metrics)

Behavioral Summary

Prioritas Utama Proyek
1. Mainnet Launch Timeliness: Launch Irys L1 mainnet Mar 2024 setelah testnet Jan 2024 — 2 bulan window, prioritaskan launch over audit/governance/transparency
2. Provenance Layer Differentiation: Bangun provenance layer native sebagai unique value proposition di atas Arweave storage
3. Developer Experience: SDK TypeScript/JS first, docs, CLI, Gateway, Explorer — first-party infrastructure ownership
4. Narrative Positioning: "Permanent data provenance layer" + AI/DePIN narratives untuk market differentiation
5. Ethereum Economic Security: Leverage Ethereum staking untuk validator security tanpa membangun validator set dari nol

Cara Mengambil Keputusan
- Centralized di Bundlr Labs, Inc. (CEO Josh Benaron) — single entity kontrol pengembangan protokol inti
- Architecture decisions: Leverage existing L1s (Arweave, Ethereum) untuk non-differentiating functions
- Launch decisions: Staged (testnet → mainnet) dengan incentivized testnet untuk validasi ekonomi
- Transparency decisions: Minimal quantitative disclosure — strategic opacity pada financial/token/adoption metrics
- Governance decisions: Deferred ke post-TGE — progressive decentralization roadmap

Faktor Paling Sering Mempengaruhi Keputusan
1. Time-to-Market: Mainnet launch deadline mendorong trade-off pada audit, governance, transparency
2. Technical Differentiation: Provenance layer sebagai moat → custom L1, native provenance, modular architecture
3. Risk Acceptance: Single critical dependencies (Arweave, Ethereum) diterima sebagai trade-off untuk battle-tested infrastructure
4. Narrative Control: Positioning sebagai "provenance layer" bukan "storage layer" atau "DA layer" — dikontrol via website/blog
5. Developer Adoption: First-party tooling investment (SDK, Gateway, Explorer, Docs) untuk menarik builder early

Pola Evolusi
- 2021: Bundlr Labs founding → Bundlr Network (bundler service on Arweave)
- 2023: Developer infrastructure build-out (SDK, Docs, GitHub, Community channels)
- 2024-01: Incentivized Testnet Phase 1 (economic/validator/provenance testing)
- 2024-03: Rebranding Bundlr → Irys (identity shift: bundler → L1 provenance layer)
- 2024-03-26: Mainnet Launch (Irys L1 live, provenance layer, gateway, explorer)
- 2024: Tokenomics publication (pre-TGE, qualitative only), Ethereum integration defined
- Next: TGE, DAO/Foundation formation, governance activation, quantitative transparency (?)

Kekuatan Utama
1. Technical Architecture: Modular design leveraging battle-tested Arweave + Ethereum, custom provenance layer differentiation
2. Developer Tooling: Comprehensive first-party SDK, Gateway, Explorer, Docs, CLI — TypeScript/JS native
3. Clear Positioning: "Permanent data provenance layer" narrative yang differentiated dari storage/DA competitors
4. Staged Validation: Incentivized testnet sebelum mainnet untuk de-risk economics dan validator performance
5. Team Continuity: Bundlr Labs (2021) → Irys (2024) — same entity, same CEO, domain expertise di permanent storage

Kelemahan Utama
1. Zero Quantitative Transparency: Funding, treasury, tokenomics numerik, adoption metrics — semua undisclosed
2. Centralized Governance: Single entity (Bundlr Labs) control, no Foundation/DAO, validator set opaque
3. Critical Single Dependencies: Arweave (storage), Ethereum (settlement) — no fallback, no multi-layer strategy
4. No Public Security Audit: Mainnet launched tanpa audit transparency — trust assumption tinggi
5. Pre-TGE Token Uncertainty: Token contract undeployed, TGE unscheduled, vesting/allocation unknown — economic model unvalidated
6. Narrative-Adoption Gap: AI/DePIN claims tanpa bukti teknis/adopsi terverifikasi
7. Custom Consensus Risk: Non-standard framework, undocumented consensus mechanism, unknown validator requirements

## Knowledge Extraction
_ref: `docs/Patterns/*`, `docs/Reasoning/*` (rule candidates)_

PROJECT: Irys

Core Insights

Insight 1: Arsitektur modular dengan dependency eksternal kritis menggantikan full-stack sovereign
Explanation: Irys memilih membangun Layer 1 execution/provenance layer sendiri namun meng-outsource permanent storage ke Arweave (sejak 2021) dan economic security ke Ethereum (staking/settlement), bukan membangun storage/consensus dari nol. Dependency keduanya ditandai "Critical" di Phase 7.
Evidence: Phase 4 Architecture menunjukkan Arweave sebagai permanent storage layer sejak 2021【Phase 3 — EV-002】 dan Ethereum sebagai staking/settlement layer【Phase 3 — EV-009】; Phase 7 External Dependencies menandai keduanya "Criticality: Critical"【Phase 7 — External Dependencies】; Phase 8 Competitor Landscape membandingkan dengan Celestia/EigenDA/Avail yang juga modular DA layer【Phase 8 — Competitor Landscape】
Supporting Dataset: Phase 3 EV-002 EV-009, Phase 4 Architecture, Phase 7 External Dependencies, Phase 8 Competitor Landscape
Confidence: High

Insight 2: Mainnet launch tanpa token live (pre-TGE) dan tanpa public security audit
Explanation: Irys meluncurkan mainnet 26 Maret 2024 dengan validator aktif, provenance layer, gateway, dan explorer, namun token IRYS belum di-deploy (pre-TGE) dan tidak ada laporan audit konsensus/kriptografi/smart contract yang dipublikasikan.
Evidence: Phase 3 EV-006 Mainnet launch【Phase 3 — EV-006】; Phase 6 Token Status pre-TGE【Phase 6 — Token Information】; Phase 4 Audit History "tidak ditemukan"【Phase 4 — Audit History】; Phase 7 Ecosystem Risks "No Public Security Audits"【Phase 7 — Ecosystem Risks】
Supporting Dataset: Phase 3 EV-006, Phase 6 Token, Phase 4 Audit History, Phase 7 Ecosystem Risks
Confidence: High

Insight 3: Zero financial transparency di semua phase — funding, treasury, revenue, token sale semua undisclosed
Explanation: Dari founding 2021 hingga mainnet 2024, tidak ada funding announcement, investor disclosure, treasury report, revenue transparency, atau token sale detail di sumber primer resmi.
Evidence: Phase 5 Funding History/Treasury/Revenue/Token Sale semua "Tidak diungkap (LOW)"【Phase 5 — Funding History】【Phase 5 — Treasury】【Phase 5 — Revenue Model】【Phase 5 — Token Sale】; Phase 8 Market tidak ada financial backing data【Phase 8 — Market】; Phase 2 Entities tidak ada Investor entity【Phase 2 — Entities】
Supporting Dataset: Phase 5 Financial, Phase 8 Market, Phase 2 Entities
Confidence: High

Insight 4: Developer-first go-to-market sequence: tooling (2023) → testnet (Jan 2024) → mainnet (Mar 2024) → token (TBD)
Explanation: Urutan prioritas konsisten: SDK, docs, GitHub, community channels diluncurkan 2023 (EV-003), lalu Incentivized Testnet Phase 1 Jan 2024 (EV-004), lalu Mainnet Mar 2024 (EV-006), token masih pre-TGE. Bukan token-first launch.
Evidence: Phase 3 EV-003 2023 tooling/community【Phase 3 — EV-003】; EV-004 Jan 2024 testnet【Phase 3 — EV-004】; EV-006 Mar 2024 mainnet【Phase 3 — EV-006】; Phase 6 Token pre-TGE【Phase 6 — Token Information】; Phase 8 Market Stage Pre-TGE/Early【Phase 8 — Market Position】
Supporting Dataset: Phase 3 History, Phase 6 Token, Phase 8 Market
Confidence: High

Insight 5: Governance sepenuhnya terpusat di Bundlr Labs, Inc. tanpa foundation terpisah, DAO, atau council
Explanation: Semua keputusan protokol dikendalikan single entity Bundlr Labs, Inc.; Terms of Service mengikat pengguna pada entitas ini; tidak ada governance forum, snapshot, proposal system, validator transparency, atau emergency council terdokumentasi.
Evidence: Phase 2 Entities tidak ada Foundation/DAO entity【Phase 2 — Entities】; Phase 6 Governance "tidak diketahui... belum terbentuk (Pre-TGE)"【Phase 6 — Governance】; Phase 7 Governance Ecosystem Foundation/DAO/Council/Committee/Validator Group semua "tidak diketahui"【Phase 7 — Governance Ecosystem】; Phase 4 Security Model Slashing/Conditions "tidak terdokumentasi"【Phase 4 — Security Model】
Supporting Dataset: Phase 2 Entities, Phase 6 Governance, Phase 7 Governance Ecosystem, Phase 4 Security Model
Confidence: High

Insight 6: Narasi expansion bertahap tanpa mengganti core positioning: Arweave bundler → Permanent data provenance layer → AI/DePIN/Modular/Restaking
Explanation: "Permanent data provenance layer" konsisten sebagai primary narrative sejak rebranding (EV-005); secondary narratives AI data provenance, DePIN, Modular blockchain, Restaking ditambah bertahap tanpa mengganti core.
Evidence: Phase 8 Narrative Position Primary "Permanent data provenance layer" HIGH【Phase 8 — Narrative Position】; Secondary narratives AI/DePIN/Modular/Restaking MEDIUM【Phase 8 — Narrative Position】; Phase 3 EV-005 rebranding announcement【Phase 3 — EV-005】; Phase 7 Ecosystem Position Secondary Sector AI/DePIN【Phase 7 — Ecosystem Position】
Supporting Dataset: Phase 8 Narrative Position, Phase 3 EV-005, Phase 7 Ecosystem Position
Confidence: High

Insight 7: Technical opacity konsisten — consensus detail, execution environment, validator requirements, audit reports semua tidak dipublikasikan
Explanation: Whitepaper/research paper tidak tersedia; consensus mechanism, VM type, slashing, hardware requirements, audit reports semua "tidak diketahui" atau "tidak terdokumentasi"; custom L1 tanpa framework standar (Cosmos SDK, Substrate, OP Stack).
Evidence: Phase 4 Consensus Mechanism "tidak terdokumentasi"【Phase 4 — Consensus Mechanism】; Execution Environment "tidak diketahui"【Phase 4 — Execution Environment】; Current Technical Stack consensus library/P2P/cryptography "tidak diketahui"【Phase 4 — Current Technical Stack】; Audit History "tidak ditemukan"【Phase 4 — Audit History】; Known Technical Limitations throughput/validator hardware "tidak dipublikasikan"【Phase 4 — Known Technical Limitations】
Supporting Dataset: Phase 4 Technology (Consensus, Execution, Current Stack, Audit History, Known Limitations)
Confidence: High

Insight 8: First-party infrastructure operations (Gateway, Explorer, Indexer) tanpa third-party provider diversity
Explanation: Irys Gateway, Irys Explorer, dan indexer dioperasikan self-hosted oleh Bundlr Labs; tidak ada community-run gateway/explorer atau third-party infrastructure provider terdokumentasi.
Evidence: Phase 7 Infrastructure Providers Irys Gateway dan Irys Explorer "self-operated"【Phase 7 — Infrastructure Providers】; Phase 7 Major Integrations Gateway Integration status Live【Phase 7 — Major Integrations】; Phase 2 Entities tidak ada infrastructure partner selain Arweave/Ethereum/GitHub/Discord【Phase 2 — Entities】
Supporting Dataset: Phase 7 Infrastructure Providers, Phase 7 Major Integrations, Phase 2 Entities
Confidence: High

Strategic Principles

Principle 1: Modular first — outsourcing critical dependencies (storage ke Arweave, economic security ke Ethereum) daripada full-stack sovereign
Explanation: Irys membangun hanya execution/provenance layer proprietary, mengandalkan Arweave untuk permanent storage (sejak 2021) dan Ethereum untuk validator economics. Ini mengurangi development complexity dan time-to-market.
Evidence: Phase 4 Architecture Arweave Integration dan Ethereum Staking Contracts sebagai core components【Phase 4 — Core Components】; Phase 7 External Dependencies keduanya "Criticality: Critical"【Phase 7 — External Dependencies】; Phase 8 Competitor Landscape positioning vs Celestia/EigenDA/Avail【Phase 8 — Competitor Landscape】
Supporting Dataset: Phase 4 Architecture, Phase 7 External Dependencies, Phase 8 Competitor Landscape
Confidence: High

Principle 2: Developer tooling completeness before token launch — SDK, CLI, Gateway, Explorer, Docs semua first-party ready sebelum mainnet dan jauh sebelum TGE
Explanation: Semua core developer infrastructure dibangun dan dihosting internal oleh Bundlr Labs sejak 2023 (EV-003), memberikan integration path yang matang sebelum token economics live.
Evidence: Phase 3 EV-003 2023 tooling/community launch【Phase 3 — EV-003】; Phase 4 Development Framework SDK/CLI/API first-party【Phase 4 — Development Framework】; Phase 7 Developer Ecosystem tidak ada grant/hackathon tercer-party【Phase 7 — Developer Ecosystem】
Supporting Dataset: Phase 3 EV-003, Phase 4 Development Framework, Phase 7 Developer Ecosystem
Confidence: High

Principle 3: Narrative consistency dengan layering — core positioning "permanent data provenance layer" tidak berubah, secondary narratives ditambah bertahap
Explanation: Sejak rebranding EV-005, primary narrative konsisten; AI/DePIN/Modular/Restaking ditambah sebagai secondary tanpa mengubah core value proposition.
Evidence: Phase 8 Narrative Position Primary HIGH, Secondary MEDIUM【Phase 8 — Narrative Position】; Phase 3 EV-005 rebranding announcement【Phase 3 — EV-005】; Phase 7 Ecosystem Position Secondary Sector AI/DePIN【Phase 7 — Ecosystem Position】
Supporting Dataset: Phase 8 Narrative Position, Phase 3 EV-005, Phase 7 Ecosystem Position
Confidence: High

Principle 4: Staged validation via incentivized testnet before mainnet — testnet berinsentif Phase 1 (Jan 2024) untuk validasi validator economics dan provenance layer sebelum mainnet launch (Mar 2024)
Explanation: Menggunakan token testnet untuk simulasi staking, rewards, dan provenance economics, mengumpulkan data performa validator sebelum commit ke mainnet production.
Evidence: Phase 3 EV-004 Incentivized Testnet Phase 1【Phase 3 — EV-004】; Phase 6 Major Token Events testnet simulasi staking/reward【Phase 6 — Major Token Events】; Phase 4 Technical Upgrade History 3 major upgrades【Phase 4 — Technical Upgrade History】
Supporting Dataset: Phase 3 EV-004, Phase 6 Major Token Events, Phase 4 Technical Upgrade History
Confidence: High

Principle 5: Centralized development control until protocol maturity — single entity (Bundlr Labs) mengendalikan semua core decisions, infrastructure, tooling tanpa foundation/DAO hingga post-TGE
Explanation: Terms of Service mengikat pada Bundlr Labs; tidak ada governance forum, validator transparency, atau emergency council. Kontrol terpusat memungkinkan kecepatan eksekusi tapi menciptakan single point of failure governance.
Evidence: Phase 2 Entities Bundlr Labs sebagai core developer【Phase 2 — Entities】; Phase 6 Governance "belum terbentuk"【Phase 6 — Governance】; Phase 7 Governance Ecosystem semua "tidak diketahui"【Phase 7 — Governance Ecosystem】; Phase 5 Financial Dependencies "Primary Funding Source: Tidak diungkap"【Phase 5 — Financial Dependencies】
Supporting Dataset: Phase 2 Entities, Phase 6 Governance, Phase 7 Governance Ecosystem, Phase 5 Financial Dependencies
Confidence: High

Success Factors

Factor 1: Early Arweave ecosystem integration (2021) memberikan storage layer maturity dan data availability foundation sebelum L1 launch
Explanation: Bundlr Network beroperasi sebagai Arweave bundler sejak 2021 (EV-001, EV-002), membangun expertise, tooling, dan user base di ekosistem Arweave 3 tahun sebelum Irys L1 mainnet.
Evidence: Phase 3 EV-001 Founding 2021【Phase 3 — EV-001】; EV-002 Arweave integration 2021【Phase 3 — EV-002】; Phase 7 External Dependencies Arweave "Critical" live sejak 2021【Phase 7 — External Dependencies】
Supporting Dataset: Phase 3 EV-001 EV-002, Phase 7 External Dependencies
Confidence: High

Factor 2: Developer-first tooling maturity (SDK TypeScript/JS, CLI, REST API, Docs, GitHub) tersedia 1+ tahun sebelum mainnet
Explanation: EV-003 (2023) meluncurkan complete developer stack; SDK menjadi primary integration vector; docs.irys.xyz dan GitHub org memberikan reference implementation dan community support sebelum testnet/mainnet.
Evidence: Phase 3 EV-003 2023 tooling launch【Phase 3 — EV-003】; Phase 4 Development Framework SDK/CLI/API first-party【Phase 4 — Development Framework】; Phase 7 Developer Ecosystem SDK/API/CLI/GitHub/Docs all Live【Phase 7 — Developer Ecosystem】
Supporting Dataset: Phase 3 EV-003, Phase 4 Development Framework, Phase 7 Developer Ecosystem
Confidence: High

Factor 3: Incentivized testnet Phase 1 (Jan 2024) memvalidasi validator economics dan provenance layer sebelum mainnet
Explanation: Testnet berinsentif menguji staking simulation, validator performance, provenance economics dengan token testnet, mengurangi risiko mainnet launch tanpa token economics validation.
Evidence: Phase 3 EV-004 Incentivized Testnet Phase 1【Phase 3 — EV-004】; Phase 6 Major Token Events testnet simulasi staking/reward【Phase 6 — Major Token Events】; Phase 4 Technical Upgrade History testnet sebagai upgrade phase【Phase 4 — Technical Upgrade History】
Supporting Dataset: Phase 3 EV-004, Phase 6 Major Token Events, Phase 4 Technical Upgrade History
Confidence: Medium

Factor 4: Clear primary narrative "permanent data provenance layer" yang differentiated dari pure storage (Arweave/Filecoin) dan pure DA (Celestia/EigenDA)
Explanation: Positioning unik: bukan hanya storage, bukan hanya DA, tapi provenance layer on-chain native di atas permanent storage. Menarik AI/DePIN use cases yang butuh verifiable data lineage.
Evidence: Phase 8 Narrative Position Primary HIGH【Phase 8 — Narrative Position】; Phase 8 Competitor Landscape differentiation vs Arweave/Filecoin/Celestia/EigenDA【Phase 8 — Competitor Landscape】; Phase 7 Ecosystem Position AI/DePIN secondary【Phase 7 — Ecosystem Position】
Supporting Dataset: Phase 8 Narrative Position, Phase 8 Competitor Landscape, Phase 7 Ecosystem Position
Confidence: High

Factor 5: Ethereum settlement/staking integration memberikan economic security bootstrap tanpa membangun validator set dari nol
Explanation: Memanfaatkan Ethereum validator economics via staking IRYS di Ethereum; sybil resistance dari Ethereum; tidak perlu bootstrap standalone validator economics pre-TGE.
Evidence: Phase 3 EV-009 Ethereum integration【Phase 3 — EV-009】; Phase 4 Consensus Mechanism validator selection berbasis staking IRYS di Ethereum【Phase 4 — Consensus Mechanism】; Phase 6 Token Utility staking validator【Phase 6 — Utility】; Phase 7 External Dependencies Ethereum "Critical"【Phase 7 — External Dependencies】
Supporting Dataset: Phase 3 EV-009, Phase 4 Consensus, Phase 6 Utility, Phase 7 External Dependencies
Confidence: High

Failure Factors

Factor 1: Zero financial transparency menciptakan information asymmetry untuk investor, validator, dan ecosystem partners
Explanation: Tidak ada funding history, investor list, valuation, treasury size, composition, custodian, revenue history, token sale details. Stakeholder tidak bisa assess financial health, runway, atau tokenomics fairness.
Evidence: Phase 5 Funding History/Treasury/Revenue/Token Sale semua "Tidak diungkap"【Phase 5 — Funding History】【Phase 5 — Treasury】【Phase 5 — Revenue Model】【Phase 5 — Token Sale】; Phase 8 Market tidak ada financial backing data【Phase 8 — Market】; Phase 2 Entities tidak ada Investor entity【Phase 2 — Entities】
Supporting Dataset: Phase 5 Financial, Phase 8 Market, Phase 2 Entities
Confidence: High

Factor 2: Mainnet launch tanpa public security audit dan tanpa slashing conditions documentation
Explanation: Mainnet live 26 Mar 2024 tanpa audit konsensus/kriptografi/smart contract publik; slashing conditions tidak terdokumentasi; validator set genesis undisclosed. Security assurance gap untuk early adopters dan validators.
Evidence: Phase 4 Audit History "tidak ditemukan"【Phase 4 — Audit History】; Phase 4 Security Model Slashing/Conditions "tidak terdokumentasi"【Phase 4 — Security Model】; Phase 7 Ecosystem Risks "No Public Security Audits" LOW & "Undisclosed Validator Set" MEDIUM【Phase 7 — Ecosystem Risks】; Phase 8 Market Risks "tidak ada audit keamanan publik"【Phase 8 — Market】
Supporting Dataset: Phase 4 Audit History, Phase 4 Security Model, Phase 7 Ecosystem Risks, Phase 8 Market
Confidence: High

Factor 3: Tokenomics numerik detail undisclosed (alokasi %, vesting, cliff, TGE schedule, initial/max supply) — investor/developer tidak bisa model supply dynamics
Explanation: Tokenomics hanya garis besar kategori alokasi (Community, Team, Investors, Foundation, Treasury, Ecosystem) tanpa persentase; vesting schedule semua "tidak diketahui"; TGE date "belum dijadwalkan resmi"; contract address "belum di-deploy".
Evidence: Phase 6 Distribution semua "Planned, persentase tidak diungkap"【Phase 6 — Distribution】; Phase 6 Vesting Schedule semua kategori "tidak diketahui"【Phase 6 — Vesting Schedule】; Phase 6 TGE TGE Date "belum dijadwalkan resmi"【Phase 6 — TGE】; Phase 6 Token Information Contract Address "belum di-deploy"【Phase 6 — Token Information】
Supporting Dataset: Phase 6 Token (Distribution, Vesting, TGE, Token Information)
Confidence: High

Factor 4: Governance centralization tanpa transparency — single entity control, no foundation/DAO, no validator transparency, no emergency council
Explanation: Bundlr Labs mengendalikan semua decisions; Terms of Service bind ke corporate entity; tidak ada governance forum, proposal system, delegation, treasury governance; validator genesis set undisclosed.
Evidence: Phase 2 Entities tidak ada Foundation/DAO【Phase 2 — Entities】; Phase 6 Governance semua "tidak diketahui"【Phase 6 — Governance】; Phase 7 Governance Ecosystem Foundation/DAO/Council/Committee/Validator Group semua "tidak diketahui"【Phase 7 — Governance Ecosystem】; Phase 4 Security Model slashing undocumented【Phase 4 — Security Model】
Supporting Dataset: Phase 2 Entities, Phase 6 Governance, Phase 7 Governance Ecosystem, Phase 4 Security Model
Confidence: High

Factor 5: Technical opacity — consensus mechanism, execution environment/VM, validator hardware requirements, cryptography libraries, P2P networking semua undocumented
Explanation: Tidak ada whitepaper/research paper; custom L1 tanpa framework standar; developer dan validator tidak bisa assess technical risk, hardware costs, atau contribute to protocol improvements.
Evidence: Phase 4 Consensus Mechanism "tidak terdokumentasi"【Phase 4 — Consensus Mechanism】; Execution Environment "tidak diketahui"【Phase 4 — Execution Environment】; Current Technical Stack consensus library/P2P/cryptography "tidak diketahui"【Phase 4 — Current Technical Stack】; Known Technical Limitations throughput/validator hardware "tidak dipublikasikan"【Phase 4 — Known Technical Limitations】
Supporting Dataset: Phase 4 Technology (Consensus, Execution, Current Stack, Known Limitations)
Confidence: High

Factor 6: Single points of failure pada critical dependencies (Arweave storage, Ethereum settlement) tanpa fallback/alternative layer
Explanation: Semua data blob → Arweave; semua validator economics → Ethereum; tidak ada multi-storage atau multi-settlement redundancy. Arweave outage atau Ethereum congestion/fork langsung berdampak Irys liveness.
Evidence: Phase 7 External Dependencies Arweave & Ethereum "Criticality: Critical"【Phase 7 — External Dependencies】; Phase 7 Ecosystem Risks "Single Storage Layer Dependency" & "Single Settlement Layer Dependency" HIGH【Phase 7 — Ecosystem Risks】; Phase 4 Architecture tidak menunjukkan alternative【Phase 4 — Architecture】
Supporting Dataset: Phase 7 External Dependencies, Phase 7 Ecosystem Risks, Phase 4 Architecture
Confidence: High

Decision Framework

Step 1: Observe — Identifikasi kebutuhan pasar dan dependency eksternal yang matang (Arweave storage 2021, Ethereum economic security)
Evidence: Phase 3 EV-001 Founding Bundlr Labs 2021【Phase 3 — EV-001】; EV-002 Arweave integration 2021【Phase 3 — EV-002】; Phase 7 External Dependencies Arweave/Ethereum Critical【Phase 7 — External Dependencies】
Supporting Dataset: Phase 3 EV-001 EV-002, Phase 7 External Dependencies
Confidence: High

Step 2: Evaluate — Bangun developer tooling first-party (SDK, CLI, Docs, Gateway, Explorer) sebelum protocol launch
Evidence: Phase 3 EV-003 2023 tooling/community launch【Phase 3 — EV-003】; Phase 4 Development Framework first-party stack【Phase 4 — Development Framework】; Phase 7 Developer Ecosystem all first-party Live【Phase 7 — Developer Ecosystem】
Supporting Dataset: Phase 3 EV-003, Phase 4 Development Framework, Phase 7 Developer Ecosystem
Confidence: High

Step 3: Fund — (Undisclosed) Private funding melalui Bundlr Labs corporate entity; tidak ada public fundraising, grant, atau community funding terdokumentasi
Evidence: Phase 5 Funding History "Tidak diungkap"【Phase 5 — Funding History】; Phase 5 Fundraising Mechanism "Tidak diungkap"【Phase 5 — Fundraising Mechanism】; Phase 2 Entities hanya Bundlr Labs, Inc.【Phase 2 — Entities】
Supporting Dataset: Phase 5 Financial, Phase 2 Entities
Confidence: Low (karena undisclosed)

Step 4: Develop — Custom L1 consensus + Provenance Layer proprietary; modular architecture dengan Arweave storage + Ethereum staking
Evidence: Phase 4 Architecture custom L1 modular【Phase 4 — Architecture】; Phase 4 Core Components Irys L1 + Provenance Layer + Arweave Integration + Ethereum Staking Contracts【Phase 4 — Core Components】; Phase 3 EV-005 Rebranding ke Irys L1【Phase 3 — EV-005】
Supporting Dataset: Phase 4 Architecture, Phase 4 Core Components, Phase 3 EV-005
Confidence: High

Step 5: Launch — Staged: Incentivized Testnet Phase 1 (Jan 2024) → Mainnet (Mar 2024) tanpa token → Token TGE (TBD)
Evidence: Phase 3 EV-004 Testnet Jan 2024【Phase 3 — EV-004】; EV-006 Mainnet Mar 2024【Phase 3 — EV-006】; Phase 6 Token Status pre-TGE【Phase 6 — Token Information】; Phase 4 Technical Upgrade History 3 major upgrades【Phase 4 — Technical Upgrade History】
Supporting Dataset: Phase 3 EV-004 EV-006, Phase 6 Token, Phase 4 Technical Upgrade History
Confidence: High

Step 6: Govern — Centralized di Bundlr Labs hingga post-TGE; roadmap ke DAO/Foundation tidak dipublikasikan
Evidence: Phase 2 Entities Bundlr Labs sebagai core developer【Phase 2 — Entities】; Phase 6 Governance "belum terbentuk (Pre-TGE)"【Phase 6 — Governance】; Phase 7 Governance Ecosystem semua "tidak diketahui"【Phase 7 — Governance Ecosystem】
Supporting Dataset: Phase 2 Entities, Phase 6 Governance, Phase 7 Governance Ecosystem
Confidence: High

Reusable Playbook

Playbook 1: Leverage mature external layers untuk critical dependencies (storage, settlement) instead of building from scratch
Explanation: Irys menggunakan Arweave (permanent storage, live sejak 2018) dan Ethereum (economic security, validator set terbesar) sebagai foundation, membangun hanya differentiation layer (provenance + L1 execution). Mengurangi 3+ tahun development time untuk storage/consensus.
Evidence: Phase 3 EV-002 Arweave integration 2021【Phase 3 — EV-002】; Phase 3 EV-009 Ethereum integration 2024【Phase 3 — EV-009】; Phase 7 External Dependencies Critical live dependencies【Phase 7 — External Dependencies】; Phase 8 Competitor Landscape vs full-stack competitors【Phase 8 — Competitor Landscape】
Supporting Dataset: Phase 3 EV-002 EV-009, Phase 7 External Dependencies, Phase 8 Competitor Landscape
Confidence: High

Playbook 2: Developer tooling completeness (SDK, CLI, Gateway, Explorer, Docs) 12-18 bulan sebelum mainnet launch
Explanation: EV-003 (2023) meluncurkan full stack developer tools; ketika mainnet live (EV-006 Mar 2024), developers sudah memiliki mature integration path, reducing friction untuk early adoption.
Evidence: Phase 3 EV-003 2023 tooling launch【Phase 3 — EV-003】; Phase 4 Development Framework SDK/CLI/API/Docs all Live【Phase 4 — Development Framework】; Phase 7 Developer Ecosystem all first-party Live【Phase 7 — Developer Ecosystem】; Phase 3 EV-006 Mainnet 2024【Phase 3 — EV-006】
Supporting Dataset: Phase 3 EV-003 EV-006, Phase 4 Development Framework, Phase 7 Developer Ecosystem
Confidence: High

Playbook 3: Incentivized testnet dengan token simulation untuk validasi economics sebelum mainnet token launch
Explanation: Testnet Phase 1 (Jan 2024) menggunakan token testnet untuk simulasi staking, rewards, provenance economics; mengumpulkan validator performance data dan economics parameter sebelum mainnet real value.
Evidence: Phase 3 EV-004 Incentivized Testnet Phase 1【Phase 3 — EV-004】; Phase 6 Major Token Events testnet simulasi staking/reward【Phase 6 — Major Token Events】; Phase 4 Technical Upgrade History testnet sebagai validation phase【Phase 4 — Technical Upgrade History】
Supporting Dataset: Phase 3 EV-004, Phase 6 Major Token Events, Phase 4 Technical Upgrade History
Confidence: High

Playbook 4: Narrative layering — lock primary narrative early, add secondary narratives incrementally without diluting core
Explanation: "Permanent data provenance layer" locked sebagai primary sejak rebranding EV-005; AI/DePIN/Modular/Restaking ditambah sebagai secondary layers, masing-masing targeting specific developer segments tanpa confusing core positioning.
Evidence: Phase 8 Narrative Position Primary HIGH Secondary MEDIUM【Phase 8 — Narrative Position】; Phase 3 EV-005 Rebranding announcement【Phase 3 — EV-005】; Phase 7 Ecosystem Position Secondary Sector AI/DePIN【Phase 7 — Ecosystem Position】
Supporting Dataset: Phase 8 Narrative Position, Phase 3 EV-005, Phase 7 Ecosystem Position
Confidence: High

Playbook 5: First-party infrastructure ownership (Gateway, Explorer, Indexer) untuk control quality dan availability pada early network
Explanation: Bundlr Labs self-operates Gateway, Explorer, indexer; memastikan SLA, data consistency, dan upgrade coordination tanpa dependency pada third-party providers yang mungkin tidak aligned incentives early stage.
Evidence: Phase 7 Infrastructure Providers Gateway/Explorer "self-operated"【Phase 7 — Infrastructure Providers】; Phase 7 Major Integrations Gateway Live【Phase 7 — Major Integrations】; Phase 2 Entities tidak ada infrastructure partner ketiga【Phase 2 — Entities】
Supporting Dataset: Phase 7 Infrastructure Providers, Phase 7 Major Integrations, Phase 2 Entities
Confidence: High

Anti-patterns

Anti-pattern 1: Zero financial transparency sepanjang lifecycle (founding → mainnet) menciptakan trust deficit dan information asymmetry
Explanation: Tidak ada funding announcement, investor disclosure, treasury report, revenue transparency, token sale details. Stakeholder (validator, developer, investor, user) tidak bisa assess financial health, runway, tokenomics fairness, atau alignment.
Evidence: Phase 5 Funding History/Treasury/Revenue/Token Sale semua "Tidak diungkap"【Phase 5 — Funding History】【Phase 5 — Treasury】【Phase 5 — Revenue Model】【Phase 5 — Token Sale】; Phase 8 Market tidak ada financial backing data【Phase 8 — Market】; Phase 2 Entities tidak ada Investor entity【Phase 2 — Entities】
Supporting Dataset: Phase 5 Financial, Phase 8 Market, Phase 2 Entities
Confidence: High

Anti-pattern 2: Mainnet launch tanpa public security audit dan tanpa slashing conditions documentation
Explanation: Production network live dengan validator economics dan user funds at risk, tanpa independent audit konsensus/kriptografi/smart contract; slashing conditions undocumented; validator set genesis undisclosed. Security assurance gap fundamental.
Evidence: Phase 4 Audit History "tidak ditemukan"【Phase 4 — Audit History】; Phase 4 Security Model Slashing/Conditions "tidak terdokumentasi"【Phase 4 — Security Model】; Phase 7 Ecosystem Risks "No Public Security Audits" & "Undisclosed Validator Set"【Phase 7 — Ecosystem Risks】; Phase 8 Market Risks "tidak ada audit keamanan publik"【Phase 8 — Market】
Supporting Dataset: Phase 4 Audit History, Phase 4 Security Model, Phase 7 Ecosystem Risks, Phase 8 Market
Confidence: High

Anti-pattern 3: Tokenomics numerik detail undisclosed (alokasi %, vesting, cliff, TGE schedule, supply params) — community tidak bisa participate informed
Explanation: Hanya kategori alokasi high-level tanpa persentase; vesting schedule "tidak diketahui" untuk semua kategori; TGE date "belum dijadwalkan"; contract address "belum di-deploy". Membuat impossible untuk model supply dynamics, assess fairness, atau plan participation.
Evidence: Phase 6 Distribution semua "Planned, persentase tidak diungkap"【Phase 6 — Distribution】; Phase 6 Vesting Schedule semua "tidak diketahui"【Phase 6 — Vesting Schedule】; Phase 6 TGE TGE Date "belum dijadwalkan resmi"【Phase 6 — TGE】; Phase 6 Token Information Contract Address "belum di-deploy"【Phase 6 — Token Information】
Supporting Dataset: Phase 6 Token (Distribution, Vesting, TGE, Token Information)
Confidence: High

Anti-pattern 4: Governance centralization tanpa transparency roadmap ke decentralization
Explanation: Single entity (Bundlr Labs) control semua decisions; Terms of Service bind ke corporate; tidak ada foundation/DAO/council/committee/validator group transparency; tidak ada emergency governance mechanism. Creates single point of failure dan misalignment risk.
Evidence: Phase 2 Entities tidak ada Foundation/DAO【Phase 2 — Entities】; Phase 6 Governance semua "tidak diketahui... belum terbentuk"【Phase 6 — Governance】; Phase 7 Governance Ecosystem semua "tidak diketahui"【Phase 7 — Governance Ecosystem】; Phase 4 Security Model slashing undocumented【Phase 4 — Security Model】
Supporting Dataset: Phase 2 Entities, Phase 6 Governance, Phase 7 Governance Ecosystem, Phase 4 Security Model
Confidence: High

Anti-pattern 5: Technical opacity pada core protocol parameters (consensus, VM, validator requirements, cryptography) menghindari community review dan contribution
Explanation: Tidak ada whitepaper/research paper; consensus mechanism, execution environment/VM, validator hardware specs, cryptography libraries, P2P networking semua undocumented. Developers/validators tidak bisa assess technical risk, optimize, atau contribute improvements.
Evidence: Phase 4 Consensus Mechanism "tidak terdokumentasi"【Phase 4 — Consensus Mechanism】; Execution Environment "tidak diketahui"【Phase 4 — Execution Environment】; Current Technical Stack consensus library/P2P/cryptography "tidak diketahui"【Phase 4 — Current Technical Stack】; Known Technical Limitations throughput/validator hardware "tidak dipublikasikan"【Phase 4 — Known Technical Limitations】
Supporting Dataset: Phase 4 Technology (Consensus, Execution, Current Stack, Known Limitations)
Confidence: High

Anti-pattern 6: Single critical dependencies tanpa fallback (Arweave storage, Ethereum settlement) — systemic risk concentration
Explanation: 100% data blob → Arweave; 100% validator economics → Ethereum; tidak ada multi-storage, multi-settlement, atau contingency plan dokumentasi. Arweave outage atau Ethereum congestion/fork = Irys liveness failure.
Evidence: Phase 7 External Dependencies Arweave & Ethereum "Criticality: Critical"【Phase 7 — External Dependencies】; Phase 7 Ecosystem Risks "Single Storage Layer Dependency" & "Single Settlement Layer Dependency" HIGH【Phase 7 — Ecosystem Risks】; Phase 4 Architecture tidak menunjukkan alternative【Phase 4 — Architecture】
Supporting Dataset: Phase 7 External Dependencies, Phase 7 Ecosystem Risks, Phase 4 Architecture
Confidence: High

Anti-pattern 7: AI/DePIN narrative claims tanpa bukti adopsi teknis terverifikasi (nama proyek, volume data, partnership teknis)
Explanation: Website/blog mengklaim AI data provenance dan DeP

## Open Questions
- [foundation] Yurisdiksi hukum pasti Bundlr Labs, Inc. (Delaware vs negara bagian lain) belum terverifikasi dari dokumen primer (Articles of Incorporation).
- [foundation] Daftar lengkap co-founders selain Josh Benaron tidak dipublikasikan secara resmi di website atau blog.
- [foundation] Ukuran core team (jumlah karyawan/engineer) tidak diungkapkan secara transparan.
- [foundation] Tanggal pasti mulai Testnet Phase 1 (hari/bulan/tahun lengkap) perlu dikonfirmasi dari announcement awal testnet.
- [foundation] Detail tokenomics lengkap (alokasi, vesting, TGE schedule) belum dipublikasikan sepenuhnya di docs.tokenomics (hanya garis besar).
- [foundation] Status smart contract token di Ethereum (pre-deploy address / proxy) belum ada informasi resmi.
- [foundation] Hubungan hukum/operasional antara "Bundlr Labs, Inc." dan fondasi protokol Irys (jika ada entitas terpisah) belum jelas.
- [entity] Identitas lengkap co-founders selain Josh Benaron (apakah ada CTO, COO, atau founder lain yang tidak dipublikasikan).
- [entity] Keberadaan entitas Foundation (misal Irys Foundation) terpisah dari Bundlr Labs, Inc. untuk governance protokol dan pengelolaan treasury token.
- [entity] Daftar investor (VC, Strategic) yang mendanai Bundlr Labs / Irys (seed, Series A, dll) — tidak ditemukan di sumber primer resmi.
- [entity] Detail tim inti (core team) — jumlah engineer, researcher, cryptographer — tidak diungkap di website/team page.
- [entity] Entitas auditor keamanan (smart contract audit, consensus audit) untuk Irys L1 sebelum mainnet launch.
- [entity] Status yurisdiksi hukum pasti Bundlr Labs, Inc. (Delaware C-Corp? LLC? Negara bagian lain?).
- [entity] Alamat kontrak token IRYS di Ethereum (pre-deploy / proxy address) dan jadwal TGE detail.
- [entity] Daftar validator genesis / early validator set dan entitas di baliknya (infrastructure providers).
- [entity] Mitra ekosistem spesifik (nama proyek/perusahaan) di vertical AI dan DePIN yang sudah terintegrasi.
- [entity] Apakah ada DAO atau komunitas governance on-chain yang sudah terbentuk (snapshot, forum governance).
- [history] Tanggal pasti pendirian Bundlr Labs, Inc. (hari/bulan/tahun lengkap) tidak ditemukan di dokumen primer (Articles of Incorporation).
- [history] Tanggal pasti peluncuran Bundlr Network awal (2021) perlu dikonfirmasi dari announcement pertama.
- [history] Tanggal pasti rebranding announcement (EV-005) - hanya diketahui bulan Maret 2024, hari exact tidak diverifikasi dari blog post.
- [history] Detail funding rounds (Seed, Series A, investor names, amounts) tidak ditemukan di sumber primer resmi.
- [history] Tanggal pasti deploy smart contract token IRYS di Ethereum (pre-deploy address / proxy) belum ada informasi resmi.
- [history] Jadwal TGE detail (tanggal, mekanisme, persentase unlock) belum dipublikasikan sepenuhnya.
- [history] Detail validator genesis set dan entitas infrastructure provider di baliknya tidak dipublikasikan.
- [history] Keberadaan dan tanggal pendirian Irys Foundation (jika terpisah dari Bundlr Labs, Inc.) tidak diverifikasi.
- [history] Riwayat audit keamanan (smart contract, consensus) sebelum mainnet launch tidak ditemukan di sumber primer.
- [history] Apakah ada governance vote atau DAO formation event setelah mainnet launch.
- [technology] Konsensus mechanism detail (algoritma, block time, finality, validator set size) tidak terdokumentasi di whitepaper/research paper resmi.
- [technology] Execution environment (VM type, smart contract support) tidak diklarifikasi di dokumentasi teknis.
- [technology] Bahasa pemrograman core protocol (Rust/Go/C++) tidak diverifikasi dari repositori utama.
- [technology] Detail keamanan validator (slashing conditions, rotation, decentralization metrics) tidak dipublikasikan.
- [technology] Status audit keamanan (apakah audit private sudah dilakukan, auditor siapa, scope apa) tidak transparan.
- [technology] Spesifikasi teknis token IRYS contract di Ethereum (proxy address, implementation, upgradeability) tidak tersedia pre-TGE.
- [technology] Arsitektur cross-chain messaging/bridge di luar Ethereum-Arweave tidak terdokumentasi.
- [technology] Hardware requirements dan operasional validator node tidak dipublikasikan untuk calon operator.
- [technology] Throughput, latency, dan kapasitas jaringan (TPS, block size) tidak memiliki benchmark resmi.
- [technology] Keberadaan whitepaper/research paper formal yang mendeskripsikan arsitektur kriptografi provenance layer.
- [financial] Jumlah total dana yang dikumpulkan (funding rounds: seed, Series A, strategic) tidak dipublikasikan di blog, website, docs, maupun Terms of Service.
- [financial] Investor utama (lead investor) dan daftar investor partisipan tidak diungkapkan secara resmi.
- [financial] Valuasi perusahaan/protokol pada ronde funding apa pun tidak tersedia.
- [financial] Ukuran treasury saat ini, komposisi aset (stablecoin, native token, other), dan custodian tidak diungkapkan.
- [financial] Model pendapatan detail (persentase fee storage, fee staking, fee governance) belum dipublikasikan secara numerik di tokenomics.
- [financial] Riwayat pendapatan bulanan/tahunan tidak tersedia.
- [financial] Mekanisme fundraising (VC, grant, public sale, community sale) tidak dijelaskan di sumber primer.
- [financial] Detail token sale (private sale allocation, public sale mechanism, launchpad, auction, community sale, tanggal, status) tidak diumumkan selain status "pre-TGE".
- [financial] Ketergantungan finansial pada VC, foundation, grant program, revenue, atau DAO tidak diketahui.
- [financial] Risiko finansial (konsentrasi treasury, penurunan revenue, ketergantungan funding, hutang, risiko hukum finansial) tidak diungkapkan dalam laporan resmi, governance, audit, atau disclosure regulator.
- [financial] Tidak ada transparency report, treasury dashboard, governance forum, atau listing di Messari/Token Terminal/DefiLlama/CryptoRank yang resmi dikaitkan.
- [token] Total supply, max supply, initial supply, dan supply type (fixed/inflationary/dynamic) tidak dipublikasikan di dokumentasi tokenomics resmi.
- [token] Persentase alokasi distribusi untuk setiap kategori (Community, Team, Investors, Foundation, Treasury, Ecosystem, Advisors) tidak diungkapkan secara numerik.
- [token] Detail vesting schedule (cliff, durasi vesting, unlock frequency) untuk setiap kategori alokasi tidak tersedia.
- [token] Tanggal TGE pasti, initial unlock percentage, kategori yang unlock di TGE, dan launch platform (CEX/DEX/launchpad) tidak diumumkan.
- [token] Alamat kontrak token IRYS di Ethereum (pre-deploy address, proxy, implementation) tidak tersedia.
- [token] Detail governance model (on-chain/off-chain, voting system, delegation, proposal threshold, treasury governance) tidak dipublikasikan.
- [token] Mekanisme inflasi/deflasi (emission schedule, burn mechanism, buyback) tidak terdokumentasi.
- [token] Status auditor keamanan untuk smart contract token IRYS (audit belum/pada saat apa) tidak diketahui.
- [token] Apakah token testnet (incentivized testnet Phase 1) memiliki konversi/claim ke token mainnet tidak diklarifikasi.
- [token] Detail tokenomics lengkap (seperti yang dirujuk di blog "introducing-irys" namun tidak ada di docs/tokenomics) mungkin ada di versi internal/private yang tidak dipublikasikan.
- [ecosystem] Status integrasi wallet spesifik (MetaMask, WalletConnect, Rainbow, dll.) tidak diverifikasi dari dokumentasi SDK atau website resmi.
- [ecosystem] Keberadaan hackathon, grant program, atau accelerator program untuk developer tidak ditemukan di blog, website, docs, atau GitHub resmi; kemungkinan belum diluncurkan atau tidak dipublikasikan.
- [ecosystem] Detail validator genesis set (entity, jumlah, distribusi stake, geographic distribution) tidak diungkapkan; block explorer tidak menampilkan halaman validator set publik yang detail.
- [ecosystem] Status pembentukan DAO, Foundation terpisah, atau governance council tidak diklarifikasi di tokenomics atau blog resmi.
- [ecosystem] Apakah ada oracle dependency (price feed untuk storage payment, staking rewards) tidak terdokumentasi di arsitektur teknis.
- [ecosystem] Bridge/messaging dependency ke chain lain selain Ethereum-Arweave tidak terdokumentasi (misalnya IBC, LayerZero, Wormhole, Hyperlane).
- [ecosystem] Cloud infrastructure provider (AWS, GCP, Azure, bare metal) untuk validator nodes, gateway, explorer, indexer tidak diungkapkan.
- [ecosystem] Status partnership dengan proyek AI/DePIN spesifik (nama proyek, integrasi teknis) hanya dikategorikan naratif di blog category "ecosystem" tanpa detail teknis.
- [ecosystem] Exchange listing plans (CEX/DEX) untuk token IRYS post-TGE tidak diumumkan.
- [ecosystem] Apakah ada auditor keamanan yang sudah melakukan audit private (consensus, crypto, smart contract) sebelum mainnet launch tidak dikonfirmasi publik.
- [ecosystem] Tokenomics numerik detail (alokasi %, vesting, cliff, TGE schedule) belum dipublikasikan; hanya garis besar kategori alokasi.
- [ecosystem] Hubungan hukum/operasional antara Bundlr Labs, Inc. dan potensial Irys Foundation (jika dibentuk) untuk pengelolaan treasury dan governance tidak jelas.
- [market] Token IRYS belum di-deploy (pre-TGE), sehingga tidak ada trading market, liquidity, atau price discovery.
- [market] Tidak ada data adopsi kuantitatif publik (TVL, DAU, transaksi harian, unique wallets, developer count, volume, validator count) dari dashboard resmi maupun pihak ketiga (DefiLlama, Token Terminal, Dune, Messari, CoinGecko, CMC).
- [market] Market share untuk kategori "permanent data provenance layer" tidak ada data industri yang dapat diverifikasi.
- [market] Funding history, investor list, valuation, dan treasury size tidak diungkapkan — tidak bisa menilai financial backing atau runway.
- [market] Competitor landscape berdasarkan positioning naratif Irys; tidak ada analisis pasar independen yang memetakan Irys vs kompetitor.
- [market] Narasi "AI data provenance" dan "DePIN" diklaim di website/blog tapi tidak ada bukti adopsi nyata (nama proyek AI/DePIN terintegrasi, volume data, partnership teknis) yang diverifikasi publik.
- [market] Validator count dan distribusi stake tidak transparan; tidak bisa menilai desentralisasi atau keamanan ekonomi.
- [market] Tidak ada audit keamanan publik — risiko teknis belum tervalidasi pasar.
- [market] Tidak ada grant program, hackathon, atau incentive program pasca-mainnet yang diumumkan — adoption flywheel belum terlihat.
- [market] Exchange listing plans (CEX/DEX) untuk post-TGE tidak diumumkan.
- [market] Wallet ecosystem support tidak terdokumentasi (MetaMask, WalletConnect, dll.) — developer experience tidak terverifikasi.
- [market] Tokenomics numerik detail (alokasi %, vesting, cliff, TGE schedule, initial supply, max supply) tidak dipublikasikan — investor/analis tidak bisa memodelkan supply dynamics.
- [market] Governance structure (DAO, foundation, council) belum terbentuk — decentralization roadmap tidak jelas.
- [market] Hubungan hukum Bundlr Labs, Inc. vs potensial Irys Foundation untuk treasury/token governance tidak diklarifikasi.
- [behavioral] Interpretasi Multi: Apakah "pre-TGE" status tokenomics berarti TGE dekat (bulan) atau jauh (tahun)? Dokumentasi hanya menyatakan "pre-TGE" tanpa timeline — bisa jadi strategic ambiguity atau belum siap.
- [behavioral] Konflik Data: Phase 4 Technology menyatakan "Consensus Mechanism: Tidak terdokumentasi secara detail" tapi Phase 1 Foundation positioning sebagai "Layer 1 blockchain" — L1 tanpa consensus documentation publik adalah anomali.
- [behavioral] Bukti Tidak Cukup: AI/DePIN adoption claims (Phase 1, 7, 8) tidak didukung oleh Major Integrations data (Phase 7) yang hanya menunjukkan Arweave, Ethereum, SDK, Gateway — perlukan verifikasi partnership teknis.
- [behavioral] Perlu Verifikasi: Bundlr Labs, Inc. jurisdiction (Delaware vs lain), co-founders lain selain Josh Benaron, investor list, funding rounds — semua fundamental untuk risk assessment tapi undisclosed.
- [behavioral] Konflik Potensial: Token IRYS utility "Staking Validator" di Ethereum (Phase 6) tapi validator set Irys L1 tidak transparan (Phase 7, 8) — bagaimana staking mechanism bekerja tanpa validator registry publik?
- [behavioral] Interpretasi Multi: "Custom L1 (tidak berbasis Cosmos SDK, Substrate, atau OP Stack)" — apakah custom consensus = novel research (high risk) atau fork existing (lower risk)? Tidak ada whitepaper/research paper untuk verifikasi.
- [behavioral] Bukti Tidak Cukup: Incentivized Testnet Phase 1 token testnet → mainnet token conversion/claim mechanism tidak diklarifikasi (Phase 6 Open Threads) — mempengaruhi early participant incentive alignment.
- [behavioral] Perlu Verifikasi: Apakah ada private security audit yang dilakukan tapi tidak dipublikasikan? Atau benar-benar tidak ada audit sama sekali sebelum mainnet?
- [behavioral] Konflik Data: Phase 4 menyatakan "Execution Environment: Tidak diketahui... VM type tidak terdokumentasi" tapi Phase 6 Token Utility "Smart Contract Support" tidak diklarifikasi — apakah Irys L1 support general smart contracts atau hanya data/provenance transactions?
- [behavioral] Interpretasi Multi: Phase 8 Competitor Landscape mencantumkan 7 kompetitor (Arweave, Filecoin, Celestia, EigenDA, Avail, 0G, Walrus) tapi Irys menggunakan Arweave sebagai storage layer — apakah Arweave competitor atau dependency? Positioning ambigu.
