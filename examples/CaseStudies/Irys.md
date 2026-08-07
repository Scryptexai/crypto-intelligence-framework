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

1. Membangun lapisan provenance data permanen native on-chain untuk AI dan DePIN
· Evidence: Website resmi dan blog konstan memposisikan Irys sebagai "permanent data provenance layer"; arsitektur menggabungkan Arweave (permanent storage) dengan provenance layer on-chain native di Irys L1; narasi "provenance for AI" dan DePIN muncul sebagai secondary narrative di komunikasi resmi
· Supporting Dataset: Phase 1 Foundation, Phase 3 EV-005 EV-006, Phase 7 Ecosystem Position, Phase 8 Narrative Position

2. Transisi dari bundler service (Bundlr Network) ke Layer 1 blockchain sovereign dengan consensus sendiri
· Evidence: Rebranding resmi dari Bundlr Network ke Irys pada Maret 2024 (EV-005) mencerminkan evolusi arsitektur; peluncuran Irys L1 mainnet 26 Maret 2024 (EV-006) mengaktifkan validator, consensus, dan provenance layer native; tidak lagi bergantung pada arsitektur bundler semata
· Supporting Dataset: Phase 2 Entities (Bundlr Network Legacy, Irys L1), Phase 3 EV-005 EV-006, Phase 4 Architecture

3. Memanfaatkan keamanan ekonomi Ethereum melalui staking token IRYS untuk validator Irys L1
· Evidence: Tokenomics mendefinisikan Ethereum sebagai settlement dan staking layer untuk token IRYS; keamanan ekonomi validator melalui mekanisme staking/restaking di Ethereum (EV-009); arsitektur cross-chain dependency pada Ethereum untuk sybil resistance
· Supporting Dataset: Phase 3 EV-009, Phase 4 Consensus Mechanism, Phase 6 Token Utility, Phase 7 External Dependencies

4. Menjaga pengendalian pengembangan inti di bawah single entity (Bundlr Labs, Inc.) tanpa foundation terpisah atau DAO aktif pasca-mainnet
· Evidence: Terms of Service mengikat pengguna pada Bundlr Labs, Inc.; tidak ada entitas foundation teridentifikasi di Phase 2; governance model belum dipublikasikan (Phase 6); validator genesis set tidak diungkapkan; tidak ada DAO/community governance forum terdokumentasi
· Supporting Dataset: Phase 2 Entities, Phase 5 Financial Dependencies, Phase 6 Governance, Phase 7 Governance Ecosystem

5. Mengunci adopsi developer melalui SDK TypeScript/JavaScript first-party, CLI, dan dokumentasi lengkap sebelum token live
· Evidence: Irys SDK, dokumentasi, GitHub org, dan saluran komunitas diluncurkan 2023 (EV-003) jauh sebelum mainnet; SDK menjadi primary integration path untuk developer; tidak ada grant program/hackathon terdokumentasi pasca-mainnet
· Supporting Dataset: Phase 3 EV-003, Phase 4 Development Framework, Phase 7 Developer Ecosystem

---

Keputusan: Pendirian Bundlr Labs, Inc. dan peluncuran Bundlr Network pada Arweave (2021)
· Trigger: Kebutuhan lapisan penyederhanaan pembayaran storage Arweave multi-token (bukan hanya AR) untuk developer
· Evidence: Phase 1 Foundation menyatakan Bundlr Network diluncurkan sebagai bundler service untuk Arweave; Phase 3 EV-001 EV-002 mengonfirmasi integrasi Arweave sebagai permanent storage layer sejak 2021
· Decision: Membangun bundler service terpusat di atas Arweave di bawah entitas perusahaan Bundlr Labs, Inc.
· Immediate Result: Entitas perusahaan dan protokol bundler awal beroperasi, menjadi entry point ke penyimpanan permanen Arweave
· Long-term Impact: Menetapkan dependency kritis pada Arweave sebagai storage layer yang berlanjut ke arsitektur Irys L1; mendirikan posisi pasar awal di ekosistem Arweave
· Supporting Dataset: Phase 1 Foundation, Phase 3 EV-001 EV-002, Phase 7 External Dependencies

Keputusan: Peluncuran SDK, dokumentasi, GitHub, dan komunitas (2023)
· Trigger: Persiapan ekosistem developer sebelum transisi ke L1 native
· Evidence: Phase 3 EV-003 mencatat peluncuran SDK, docs.irys.xyz, github.com/irys-xyz, Discord, X, Telegram, Blog pada 2023
· Decision: Menginvestasikan infrastructure developer tooling first-party (SDK TypeScript/JS, CLI, REST API) dan saluran komunitas sebelum testnet/mainnet
· Immediate Result: Infrastructure pengembangan dan komunitas resmi tersedia untuk ekosistem awal
· Long-term Impact: Membangun developer mindshare dan tooling maturity sebelum tokenomics live; SDK menjadi primary integration vector
· Supporting Dataset: Phase 3 EV-003, Phase 4 Development Framework, Phase 7 Developer Ecosystem

Keputusan: Peluncuran Incentivized Testnet Phase 1 (2024-01)
· Trigger: Validasi ekonomi token, performa validator, dan provenance layer sebelum mainnet
· Evidence: Phase 3 EV-004; Phase 6 Major Token Events mencatat testnet berinsentif untuk menguji staking dan reward
· Decision: Menjalankan testnet berinsentif dengan token testnet untuk simulasi staking, validator performance, dan provenance economics
· Immediate Result: Validator dan pengguna mulai menguji jaringan, ekonomi token, dan fitur provenance
· Long-term Impact: Data testnet menginformasikan parameter mainnet; membangun early validator community; token testnet claim/konversi ke mainnet belum diklarifikasi (Open Thread)
· Supporting Dataset: Phase 3 EV-004, Phase 6 Major Token Events, Phase 4 Technical Upgrade History

Keputusan: Rebranding Bundlr Network ke Irys dan arsitektur upgrade ke L1 native (2024-03)
· Trigger: Evolusi dari bundler service ke Layer 1 blockchain dengan provenance layer native
· Evidence: Phase 3 EV-005 pengumuman rebranding; Phase 4 Architecture beschreibt transisi ke custom L1 dengan modular provenance layer
· Decision: Mengganti nama protokol ke Irys, meluncurkan Irys L1 sebagai blockchain Layer 1 native dengan consensus sendiri, provenance layer on-chain, dan gateway retrieval
· Immediate Result: Identitas baru "Irys" diperkenalkan; arsitektur tidak lagi bundler semata melainkan L1 sovereign
· Long-term Impact: Posisioning pasar berubah dari "bundler Arweave" ke "permanent data provenance layer"; menarik narasi AI/DePIN; memerlukan validator set baru dan tokenomics baru
· Supporting Dataset: Phase 3 EV-005, Phase 4 Architecture, Phase 8 Market Position

Keputusan: Peluncuran Mainnet Irys L1 (2024-03-26)
· Trigger: Kesiapan teknis setelah testnet; aktivasi jaringan produksi dengan validator, provenance, gateway, explorer
· Evidence: Phase 3 EV-006 EV-007 EV-008; Phase 4 Technical Upgrade History mainnet launch v1.0/genesis
· Decision: Mengaktifkan Irys L1 mainnet dengan validator consensus, Provenance Layer, Irys Gateway, Irys Explorer secara bersamaan
· Immediate Result: Jaringan produksi live; transaksi data, provenance on-chain, dan operasi validator berfungsi
· Long-term Impact: Mainnet live tanpa token IRYS (pre-TGE); utility storage payment dan staking belum aktif; adopsi bergantung pada developer tooling dan Arweave integration; validator economics belum tervalidasi tanpa token rewards
· Supporting Dataset: Phase 3 EV-006 EV-007 EV-008, Phase 4 Technical Upgrade History, Phase 6 Token Status

Keputusan: Publikasi tokenomics IRYS pre-TGE tanpa detail numerik alokasi, vesting, TGE schedule (2024)
· Trigger: Transparansi awal utility token sebelum TGE
· Evidence: Phase 3 EV-010; Phase 6 Token Information status pre-TGE; Phase 6 Distribution vesting schedule semua "tidak diketahui"
· Decision: Mempublikasikan kategori alokasi (Community, Team, Investors, Foundation, Treasury, Ecosystem) dan utility (storage, staking, governance, fees, incentives) tanpa persentase, cliff, vesting duration, TGE date, atau contract address
· Immediate Result: Kerangka ekonomi token terpublikasi tapi investor/developer tidak bisa memodelkan supply dynamics
· Long-term Impact: Ketidakpastian tokenomics menciptakan information asymmetry; Exchange listing plans tidak diumumkan; governance structure belum terbentuk
· Supporting Dataset: Phase 3 EV-010, Phase 6 Token (Distribution, Vesting, TGE, Governance), Phase 8 Trading Markets

Keputusan: Integrasi Ethereum sebagai settlement dan staking layer untuk token IRYS (2024)
· Trigger: Memanfaatkan keamanan ekonomi Ethereum untuk validator Irys L1 via restaking/mekanisme staking
· Evidence: Phase 3 EV-009; Phase 4 Consensus Mechanism validator selection berbasis staking IRYS di Ethereum; Phase 6 Token Utility staking validator
· Decision: Menempatkan staking contract, validator registration, dan settlement ekonomi di Ethereum mainnet
· Immediate Result: Arsitektur cross-chain Irys L1 ↔ Ethereum ditetapkan; dependency kritis pada Ethereum liveness dan fee market
· Long-term Impact: Sybil resistance bergantung pada Ethereum; validator operational cost terkait ETH gas; regulatory exposure ke Ethereum jurisdiction; bridge/messaging ke chain lain tidak terdokumentasi
· Supporting Dataset: Phase 3 EV-009, Phase 4 Consensus, Phase 6 Utility, Phase 7 External Dependencies

---

Pola 1: Arsitektur modular dengan dependency eksternal kritis (Arweave storage, Ethereum settlement) yerine full-stack sovereign
· Decision Pattern: Irys memilih membangun L1 execution/provenance layer sendiri namun meng-outsource permanent storage ke Arweave dan economic security ke Ethereum, bukan membangun storage/consensus dari nol
· Evidence: Phase 4 Architecture menunjukkan Arweave sebagai permanent storage layer sejak 2021 (EV-002) dan Ethereum sebagai staking/settlement layer (EV-009); Phase 7 External Dependencies menandai keduanya "Critical"; Phase 8 Competitor Landscape membandingkan dengan Celestia/EigenDA/Avail yang juga modular DA layer
· Supporting Dataset: Phase 3 EV-002 EV-009, Phase 4 Architecture, Phase 7 External Dependencies, Phase 8 Competitor Landscape

Pola 2: Upgrade bertahap melalui testnet berinsentif sebelum mainnet launch tanpa token
· Decision Pattern: Menjalankan Incentivized Testnet Phase 1 (Jan 2024) untuk menguji validator economics dan provenance layer, lalu mainnet launch (Mar 2024) tanpa token live (pre-TGE)
· Evidence: Phase 3 EV-004 EV-006; Phase 4 Technical Upgrade History 3 major upgrades; Phase 6 Token Status pre-TGE; Phase 8 Market Stage Pre-TGE/Early
· Supporting Dataset: Phase 3 EV-004 EV-006, Phase 4 Technical Upgrade History, Phase 6 Token, Phase 8 Market

Pola 3: Developer tooling first-party (SDK, CLI, Gateway, Explorer) dibangun dan dioperasikan internal sebelum ecosystem grants
· Decision Pattern: Semua core developer infrastructure (SDK TypeScript/JS, CLI, HTTP Gateway, Block Explorer, Docs) dibangun dan dihosting oleh Bundlr Labs, Inc. tanpa third-party provider atau grant program terdokumentasi
· Evidence: Phase 4 Development Framework; Phase 7 Infrastructure Providers (Irys Gateway, Irys Explorer self-operated); Phase 7 Developer Ecosystem tidak ada grant/hackathon; Phase 2 Entities tidak ada infrastructure partner selain Arweave/Ethereum/GitHub/Discord
· Supporting Dataset: Phase 4 Development Framework, Phase 7 Infrastructure Providers, Phase 7 Developer Ecosystem, Phase 2 Entities

Pola 4: Tidak ada public security audit terdokumentasi sebelum atau sesudah mainnet launch
· Decision Pattern: Mainnet diluncurkan 26 Maret 2024 tanpa laporan audit konsensus, kriptografi, atau smart contract yang dipublikasikan di website/blog/docs
· Evidence: Phase 4 Audit History "tidak ditemukan"; Phase 4 Security Model slashing conditions "tidak terdokumentasi"; Phase 7 Ecosystem Risks "No Public Security Audits"; Phase 8 Market Risks "tidak ada audit keamanan publik"
· Supporting Dataset: Phase 4 Audit History, Phase 4 Security Model, Phase 7 Ecosystem Risks, Phase 8 Market

Pola 5: Custom L1 consensus tanpa adopsi framework standar (Cosmos SDK, Substrate, OP Stack) terdokumentasi
· Decision Pattern: Irys L1 dibangun sebagai custom blockchain framework bukan berbasis modular framework populer; detail consensus library, P2P networking, cryptography library tidak dipublikasikan
· Evidence: Phase 4 Current Technical Stack "Custom L1 (tidak berbasis Cosmos SDK, Substrate, atau OP Stack secara eksplisit)"; Consensus Library, P2P Networking, Cryptography semua "tidak diketahui"
· Supporting Dataset: Phase 4 Current Technical Stack, Phase 4 Consensus Mechanism, Phase 4 Core Components

---

Pola 1: Tidak ada fundraising history, investor list, valuation, atau treasury disclosure publik
· Decision Pattern: Seluruh informasi finansial (funding rounds, treasury size, composition, custodian, revenue history) tidak diungkapkan di sumber primer resmi (website, blog, docs, ToS)
· Evidence: Phase 5 Funding History semua "Tidak diungkap (LOW)"; Phase 5 Treasury semua "Tidak diungkap"; Phase 5 Revenue History "Tidak diungkap"; Phase 5 Financial Dependencies "Primary Funding Source: Tidak diungkap"; Phase 8 Market tidak ada financial backing data
· Supporting Dataset: Phase 5 Financial (Funding History, Treasury, Revenue Model, Revenue History, Fundraising Mechanism, Financial Dependencies, Financial Risk), Phase 8 Market

Pola 2: Revenue model sepenuhnya planned/pre-TGE tanpa realisasi pendapatan mainnet
· Decision Pattern: Protocol fees (storage payments), staking fees, governance fees semuanya berstatus "Planned (Pre-TGE)"; mainnet live sejak Maret 2024 tapi token utility payment/staking belum aktif
· Evidence: Phase 5 Revenue Model ketiga kategori status "Planned (Pre-TGE)"; Phase 6 Token Utility storage payment dan staking validator status "Planned (Pre-TGE)"; Phase 3 EV-006 mainnet live tanpa token
· Supporting Dataset: Phase 5 Revenue Model, Phase 6 Token Utility, Phase 3 EV-006

Pola 3: Token sale mechanism dan TGE details sepenuhnya undisclosed
· Decision Pattern: Private sale, public sale, launchpad, auction, community sale semua "Tidak diungkap"; TGE date "belum dijadwalkan resmi"; launch platform "tidak diketahui"
· Evidence: Phase 5 Token Sale semua kategori "Tidak diungkap"; Phase 6 TGE TGE Date "belum dijadwalkan resmi"; Phase 8 Trading Markets "Tidak tersedia (Pre-TGE)"
· Supporting Dataset: Phase 5 Token Sale, Phase 6 TGE, Phase 8 Trading Markets

Pola 4: Zero financial transparency infrastructure (no dashboard, no transparency report, no third-party analytics)
· Decision Pattern: Tidak ada treasury dashboard, transparency report, governance forum, atau listing di Messari/Token Terminal/DefiLlama/CryptoRank
· Evidence: Phase 5 Official Financial Resources semua "Tidak tersedia (LOW)"; Phase 8 Official Market Resources DefiLlama, CoinGecko, CMC, Token Terminal, Messari semua "Tidak tersedia (LOW)"
· Supporting Dataset: Phase 5 Official Financial Resources, Phase 8 Official Market Resources

---

Pola 1: Dependency kritis pada Arweave (storage) dan Ethereum (settlement/staking) tanpa alternative/fallback layer
· Decision Pattern: Semua data blob permanen dikirim ke Arweave; semua validator economics di-stake di Ethereum; tidak ada multi-storage atau multi-settlement layer redundancy terdokumentasi
· Evidence: Phase 7 External Dependencies Arweave dan Ethereum keduanya "Criticality: Critical"; Phase 7 Ecosystem Risks "Single Storage Layer Dependency" dan "Single Settlement Layer Dependency" keduanya HIGH; Phase 4 Architecture Arweave Integration dan Ethereum Staking Contracts sebagai core components
· Supporting Dataset: Phase 7 External Dependencies, Phase 7 Ecosystem Risks, Phase 4 Architecture

Pola 2: First-party infrastructure operations (Gateway, Explorer, Indexer) tanpa third-party provider diversity
· Decision Pattern: Irys Gateway, Irys Explorer, dan indexer dioperasikan self-hosted oleh Bundlr Labs; tidak ada community-run gateway/explorer atau third-party infrastructure provider terdokumentasi
· Evidence: Phase 7 Infrastructure Providers Irys Gateway dan Irys Explorer "self-operated"; Phase 7 Major Integrations Gateway Integration status Live; Phase 2 Entities tidak ada infrastructure partner selain Arweave/Ethereum/GitHub/Discord
· Supporting Dataset: Phase 7 Infrastructure Providers, Phase 7 Major Integrations, Phase 2 Entities

Pola 3: Developer ecosystem sepenuhnya first-party tooling tanpa grant program, hackathon, atau accelerator
· Decision Pattern: SDK, CLI, API, Docs, GitHub semua first-party; tidak ada grant program, hackathon, atau incentive program pasca-mainnet terdokumentasi
· Evidence: Phase 7 Developer Ecosystem Grant Program dan Hackathon "tidak diketahui (LOW)"; Phase 7 Applications 6 first-party apps; Phase 8 Adoption Metrics Developer Count "Tidak tersedia"
· Supporting Dataset: Phase 7 Developer Ecosystem, Phase 7 Applications, Phase 8 Adoption Metrics

Pola 4: Narasi AI/Data Provenance dan DePIN sebagai secondary narrative tanpa bukti adopsi teknis terverifikasi
· Decision Pattern: Website dan blog mengklaim AI data provenance dan DePIN sebagai target market; tidak ada nama proyek AI/DePIN spesifik, volume data, atau partnership teknis yang diverifikasi publik
· Evidence: Phase 8 Narrative Position AI data provenance dan DePIN "Secondary Narrative" dengan evidence hanya blog category dan website mentions; Phase 7 Ecosystem Position Secondary Sector AI/Data Provenance; DePIN; Phase 7 Open Threads "Status partnership dengan proyek AI/DePIN spesifik... hanya dikategorikan naratif... tanpa detail teknis"
· Supporting Dataset: Phase 8 Narrative Position, Phase 7 Ecosystem Position, Phase 7 Open Threads

Pola 5: Tidak ada wallet ecosystem integration terdokumentasi untuk mainnet
· Decision Pattern: Wallet support tidak diketahui; SDK kemungkinan mendukung wallet Ethereum standar (MetaMask/WalletConnect) untuk signing tapi tidak diverifikasi eksplisit di docs
· Evidence: Phase 7 Wallet Ecosystem "tidak diketahui... tidak ada integrasi wallet spesifik terdokumentasi"; Phase 4 Development Framework tidak menyebut wallet integration
· Supporting Dataset: Phase 7 Wallet Ecosystem, Phase 4 Development Framework

---

Pola 1: Governance sepenuhnya terpusat di Bundlr Labs, Inc. tanpa foundation terpisah, DAO, atau council
· Decision Pattern: Semua keputusan protokol (upgrade, parameter, treasury, tokenomics) dikendalikan oleh single entity Bundlr Labs, Inc.; Terms of Service mengikat pengguna pada entitas ini; tidak ada governance forum, snapshot, proposal system terdokumentasi
· Evidence: Phase 2 Entities tidak ada Foundation/DAO entity; Phase 6 Governance "tidak diketahui... belum terbentuk (Pre-TGE)"; Phase 7 Governance Ecosystem Foundation/DAO/Council/Committee semua "tidak diketahui"; Phase 5 Financial Dependencies "Primary Funding Source: Tidak diungkap"
· Supporting Dataset: Phase 2 Entities, Phase 6 Governance, Phase 7 Governance Ecosystem, Phase 5 Financial Dependencies

Pola 2: Token governance utility didefinisikan tapi mechanism tidak dipublikasikan
· Decision Pattern: Tokenomics mencantumkan "Governance" sebagai utility IRYS; tapi voting system, delegation, proposal threshold, treasury governance semua "tidak diketahui"
· Evidence: Phase 6 Governance semua field "tidak diketahui (LOW)"; Phase 6 Token Utility Governance status "Planned (Pre-TGE)"; Phase 3 EV-010 tokenomics publication hanya garis besar
· Supporting Dataset: Phase 6 Governance, Phase 6 Token Utility, Phase 3 EV-010

Pola 3: Validator set genesis tidak transparan — tidak ada validator group, council, atau committee terdokumentasi
· Decision Pattern: Mainnet launch dengan validator set tapi tidak diungkapkan entity, jumlah, distribusi stake, geographic distribution; block explorer tidak menampilkan validator set publik detail
· Evidence: Phase 7 Governance Ecosystem Validator Group "tidak diketahui... genesis validator set tidak diungkapkan"; Phase 8 Adoption Metrics Validator Count "Tidak tersedia"; Phase 7 Ecosystem Risks "Undisclosed Validator Set" MEDIUM
· Supporting Dataset: Phase 7 Governance Ecosystem, Phase 8 Adoption Metrics, Phase 7 Ecosystem Risks

Pola 4: Tidak ada emergency governance atau security council mechanism terdokumentasi
· Decision Pattern: Tidak ada security council, emergency multisig, atau incident response framework dipublikasikan; slashing conditions tidak terdokumentasi
· Evidence: Phase 4 Security Model Slashing/Conditions "tidak terdokumentasi"; Phase 7 Ecosystem Risks "No Public Security Audits"; Phase 9 Risk Response Pattern (section ini) akan mencatat absence
· Supporting Dataset: Phase 4 Security Model, Phase 7 Ecosystem Risks

---

Pola 1: Tidak ada incident response pattern terdokumentasi (no exploits, market crashes, security incidents, governance conflicts di mainnet)
· Decision Pattern: Proyek baru mainnet Maret 2024, pre-TGE, belum mengalami exploit/incident publik yang memerlukan emergency response
· Evidence: Phase 3 History tidak mencatat security incident; Phase 4 Audit History tidak ada audit; Phase 7 Ecosystem Risks mencatat risiko tapi tidak ada actualized incident; Phase 8 Market tidak ada market crash data (pre-TGE)
· Supporting Dataset: Phase 3 History, Phase 4 Audit History, Phase 7 Ecosystem Risks, Phase 8 Market

Pola 2: Risk mitigation melalui architectural dependency acceptance (menerima single point of failure pada Arweave/Ethereum) tanpa fallback plan publik
· Decision Pattern: Mengakui dependency kritis pada Arweave dan Ethereum sebagai arsitektur by-design; tidak mempublikasikan contingency plan untuk Arweave outage, Ethereum congestion, atau fork
· Evidence: Phase 7 Ecosystem Risks "Single Storage Layer Dependency" dan "Single Settlement Layer Dependency" HIGH; Phase 7 External Dependencies keduanya "Criticality: Critical"; Phase 4 Architecture tidak menunjukkan alternative storage/settlement
· Supporting Dataset: Phase 7 Ecosystem Risks, Phase 7 External Dependencies, Phase 4 Architecture

Pola 3: Centralized development risk mitigation melalui first-party tooling completeness (SDK, Gateway, Explorer) sebelum decentralization
· Decision Pattern: Membangun complete first-party developer stack dan infrastructure sebelum membuka validator set atau governance ke komunitas
· Evidence: Phase 3 EV-003 SDK/docs/komunitas 2023; Phase 3 EV-006 mainnet 2024; Phase 7 Developer Ecosystem first-party tools; Phase 7 Governance Ecosystem belum ada DAO/foundation
· Supporting Dataset: Phase 3 EV-003 EV-006, Phase 7 Developer Ecosystem, Phase 7 Governance Ecosystem

Pola 4: Pre-TGE token economic risk mitigation melalui testnet incentivized (EV-004) untuk validasi economics sebelum mainnet token launch
· Decision Pattern: Menjalankan testnet berinsentif dengan token testnet untuk mensimulasikan staking, rewards, dan provenance economics sebelum token mainnet live
· Evidence: Phase 3 EV-004 Incentivized Testnet Phase 1; Phase 6 Major Token Events testnet simulasi staking/reward; Phase 6 Token Status pre-TGE mainnet launch
· Supporting Dataset: Phase 3 EV-004, Phase 6 Major Token Events, Phase 6 Token Status

---

Pola 1: Evolusi dari bundler service (2021) ke L1 provenance layer (2024) — strategic pivot mengubah value proposition fundamental
· Decision Pattern: Mulai sebagai layanan bundling pembayaran multi-token untuk Arweave (Bundlr Network), lalu rebrand dan rebuild sebagai Layer 1 blockchain native dengan provenance layer sendiri (Irys)
· Evidence: Phase 3 EV-001 EV-002 Bundlr Network 2021; Phase 3 EV-005 Rebranding Mar 2024; Phase 3 EV-006 Mainnet Irys L1; Phase 4 Architecture custom L1 dengan provenance layer; Phase 8 Market Timeline pivot 2021→2024
· Supporting Dataset: Phase 3 History (EV-001, EV-002, EV-005, EV-006), Phase 4 Architecture, Phase 8 Market Timeline

Pola 2: Developer-first go-to-market: SDK, docs, GitHub, community channels (2023) → Testnet (Jan 2024) → Mainnet (Mar 2024) → Token (TBD)
· Decision Pattern: Urutan prioritas: tooling → community → testnet → mainnet → token; tidak token-first launch
· Evidence: Phase 3 EV-003 2023 tooling/community; EV-004 Jan 2024 testnet; EV-006 Mar 2024 mainnet; Phase 6 Token pre-TGE; Phase 8 Market Stage Pre-TGE/Early
· Supporting Dataset: Phase 3 History, Phase 6 Token, Phase 8 Market

Pola 3: Narasi expansion bertahap: Arweave bundler → Permanent data provenance layer → AI data provenance + DePIN + Modular blockchain + Restaking
· Decision Pattern: Setiap phase menambah narrative layer tanpa mengganti core positioning; "permanent data provenance layer" konsisten sebagai primary narrative sejak rebranding
· Evidence: Phase 8 Narrative Position Primary "Permanent data provenance layer" HIGH; Secondary narratives AI/DePIN/Modular/Restaking MEDIUM; Phase 3 EV-005 rebranding announcement; Phase 7 Ecosystem Position Secondary Sector AI/DePIN
· Supporting Dataset: Phase 8 Narrative Position, Phase 3 EV-005, Phase 7 Ecosystem Position

Pola 4: Zero public financial disclosure di semua phase — konsisten opaque financial posture
· Decision Pattern: Dari founding 2021 hingga mainnet 2024, tidak ada funding announcement, investor disclosure, treasury report, atau revenue transparency
· Evidence: Phase 5 Funding History/Treasury/Revenue/Token Sale semua "Tidak diungkap"; Phase 8 Market tidak ada financial backing data; Phase 2 Entities tidak ada Investor entity
· Supporting Dataset: Phase 5 Financial, Phase 8 Market, Phase 2 Entities

Pola 5: Technical opacity konsisten — consensus detail, execution environment, validator requirements, audit reports semua tidak dipublikasikan
· Decision Pattern: Whitepaper/research paper tidak tersedia; consensus mechanism, VM type, slashing, hardware requirements, audit reports semua "tidak diketahui" atau "tidak terdokumentasi"
· Evidence: Phase 4 Consensus Mechanism "tidak terdokumentasi"; Execution Environment "tidak diketahui"; Current Technical Stack consensus library/P2P/cryptography "tidak diketahui"; Audit History "tidak ditemukan"; Known Technical Limitations throughput/validator hardware "tidak dipublikasikan"
· Supporting Dataset: Phase 4 Technology (Consensus, Execution, Current Stack, Audit History, Known Limitations)

---

Trade-off 1: Desentralisasi validator vs Kecepatan go-to-market (Mainnet launch tanpa token dan tanpa validator transparency)
· Decision: Meluncurkan mainnet 26 Maret 2024 dengan validator set aktif tapi tidak mengungkapkan genesis validator entity, stake distribution, atau geographic diversity; token IRYS pre-TGE sehingga validator economics belum live
· Trade-off: Mempercepat time-to-market dan menonjolkan technical delivery (L1 live, provenance live, gateway live) mengorbankan decentralization transparency dan validator economic alignment
· Evidence: Phase 3 EV-006 Mainnet launch; Phase 6 Token Status pre-TGE; Phase 7 Governance Ecosystem Validator Group undisclosed; Phase 8 Adoption Metrics Validator Count unavailable; Phase 7 Ecosystem Risks Undisclosed Validator Set MEDIUM
· Supporting Dataset: Phase 3 EV-006, Phase 6 Token, Phase 7 Governance Ecosystem, Phase 8 Adoption Metrics, Phase 7 Ecosystem Risks

Trade-off 2: Security assurance (audit) vs Launch timeline — mainnet tanpa public audit
· Decision: Meluncurkan mainnet tanpa mempublikasikan laporan audit konsensus, kriptografi, atau smart contract
· Trade-off: Menghindari delay launch untuk audit publik mengorbankan security assurance dan market trust; mengandalkan private review atau internal testing saja
· Evidence: Phase 4 Audit History "tidak ditemukan"; Phase 4 Security Model slashing conditions undocumented; Phase 7 Ecosystem Risks No Public Security Audits LOW; Phase 8 Market Risks "tidak ada audit keamanan publik"
· Supporting Dataset: Phase 4 Audit History, Phase 4 Security Model, Phase 7 Ecosystem Risks, Phase 8 Market

Trade-off 3: Single storage layer dependency (Arweave) vs Development complexity — memilih dependency kritis rather than multi-storage atau native storage
· Decision: Menggunakan Arweave sebagai sole permanent storage layer sejak 2021 (Bundlr) dan melanjutkan ke Irys L1; tidak membangun native storage atau multi-storage redundancy
· Trade-off: Mengurangi development complexity dan time-to-market dengan leverage Arweave maturity mengorbankan sovereignty over storage layer dan menciptakan single point of failure
· Evidence: Phase 3 EV-002 Arweave integration 2021; Phase 4 Architecture Arweave Integration core component; Phase 7 External Dependencies Arweave Criticality Critical; Phase 7 Ecosystem Risks Single Storage Layer Dependency HIGH
· Supporting Dataset: Phase 3 EV-002, Phase 4 Architecture, Phase 7 External Dependencies, Phase 7 Ecosystem Risks

Trade-off 4: Single settlement layer dependency (Ethereum) vs Economic security bootstrap — leverage Ethereum validator set vs sovereign staking
· Decision: Menempatkan staking IRYS dan validator registration di Ethereum; tidak membangun sovereign st

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
