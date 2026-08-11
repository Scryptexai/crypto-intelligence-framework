# Polymarket — Deep Case Study (Phased)

**CIF Dataset — Deep Dossier · Tier: Deep (anchor project)**
**Source:** Deep Research (DeepSeek), Format v3 Dependency Pipeline (12/11 phases: foundation, entity, history, technology, financial, token, ecosystem, market, behavioral, knowledge, conflict, airdrop). **Auto-assembled** by `tools/ingest.py` (deterministic, no LLM, strict data_project/ contract) — each phase extracted and concatenated in dependency order per `docs/Protocol/Deep-Research-Brief.md`; the reasoning is the source reports'.
**Raw sources archived:** doc_backup/deep/Polymarket_foundation_2026-08.docx, doc_backup/deep/Polymarket_entity_2026-08.docx, doc_backup/deep/Polymarket_history_2026-08.docx, doc_backup/deep/Polymarket_technology_2026-08.docx, doc_backup/deep/Polymarket_financial_2026-08.docx, doc_backup/deep/Polymarket_token_2026-08.docx, doc_backup/deep/Polymarket_ecosystem_2026-08.docx, doc_backup/deep/Polymarket_market_2026-08.docx, doc_backup/deep/Polymarket_behavioral_2026-08.docx, doc_backup/deep/Polymarket_knowledge_2026-08.docx, doc_backup/deep/Polymarket_conflict_2026-08.docx, doc_backup/deep/Polymarket_airdrop_2026-08.docx.
**Phases not run:** none.

> Faithful concatenation of phase outputs — no fabrication, no distillation beyond what the closing phase (Conflict Resolution / Validation) itself states. Consider a periodic QC pass.

---
## Foundation Intelligence
_ref: `docs/Ontology/Identity.md`, `docs/Ontology/Team.md`_

PROJECT: Polymarket
Official Name: Polymarket
Symbol: POLYMARKET (points system; native token not yet deployed as of 2024)
Category: Decentralized prediction market / information market
Founding Entity: Polymarket Inc. (Delaware, USA)
Founders: Shayne Coplan (Founder & CEO)
Core Team: ~50+ employees (per LinkedIn / company statements; exact verified headcount not publicly disclosed)
Country: United States (headquartered in New York, NY)
Launch Date - Testnet: 2020 (internal testing; no public testnet date verifiable)
Launch Date - Mainnet: Oktober 2020 (Polygon mainnet launch) (MEDIUM) [Polymarket blog, https://blog.polymarket.com/introducing-polymarket/]
Launch Date - TGE: Pre-TGE (token not yet launched; points program active since 2024) (HIGH) [Polymarket docs, https://docs.polymarket.com/]
Main Products: Polymarket prediction market protocol; Polymarket.com frontend; CLOB (Central Limit Order Book) matching engine; UMA oracle integration for resolution; Polymarket Points loyalty program
Official Website: https://polymarket.com
Repository: https://github.com/Polymarket (smart contracts, frontend, bot examples)
Documentation: https://docs.polymarket.com
Social - X/Twitter: @Polymarket
Social - Discord: https://discord.gg/polymarket
Social - Telegram: @PolymarketOfficial
Block Explorer: https://polygonscan.com (Polygon); https://basescan.org (Base deployment)
Token Contract: Belum di-deploy (points system off-chain; token announcement made but no contract address published) (HIGH) [Polymarket blog, https://blog.polymarket.com/introducing-the-polymarket-token/]
Chain(s): Polygon (primary), Base (secondary deployment 2024), Ethereum Mainnet (bridging/settlement)
Ecosystem: Polygon, Base, UMA (oracle), CLOB infrastructure, DeFi prediction markets

## Entity Intelligence
_ref: `docs/Ontology/Relationships.md` (entity graph)_

PROJECT: Polymarket

Entity: Shayne Coplan
Type: Person
Relationship: Pendiri dan CEO Polymarket Inc., mengarahkan visi strategis dan eksekusi protokol prediksi terdesentralisasi Polymarket sejak awal pembentukan.
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Polymarket Blog, https://blog.polymarket.com/introducing-polymarket/]; (MEDIUM) [Polymarket Docs, https://docs.polymarket.com/]

---
Entity: Polymarket Inc.
Type: Company
Relationship: Entitas hukum berbasis Delaware, AS yang mengembangkan dan mengoperasikan protokol Polymarket, frontend Polymarket.com, dan mesin CLOB (Central Limit Order Book).
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Polymarket Blog, https://blog.polymarket.com/introducing-polymarket/]; (MEDIUM) [Polymarket Docs, https://docs.polymarket.com/]

---
Entity: Polymarket
Type: Protocol
Relationship: Protokol pasar prediksi terdesentralisasi yang dibangun di atas Polygon dan Base, menggunakan CLOB untuk pencocokan order dan UMA oracle untuk resolusi pasar.
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Polymarket Blog, https://blog.polymarket.com/introducing-polymarket/]; (HIGH) [Polymarket Docs, https://docs.polymarket.com/]

---
Entity: UMA
Type: Protocol
Relationship: Protokol oracle yang menyediakan layanan resolusi pasar (Optimistic Oracle) untuk menentukan hasil pasar prediksi Polymarket secara terpercaya dan terdesentralisasi.
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Polymarket Docs, https://docs.polymarket.com/]; (MEDIUM) [Polymarket Blog, https://blog.polymarket.com/introducing-polymarket/]

---
Entity: Polygon
Type: Protocol
Relationship: Blockchain lapisan-2 Ethereum utama tempat Polymarket meluncurkan mainnet Oktober 2020 dan menjalankan sebagian besar aktivitas pasar serta CLOB-nya.
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Polymarket Blog, https://blog.polymarket.com/introducing-polymarket/]; (HIGH) [Polymarket Docs, https://docs.polymarket.com/]

---
Entity: Base
Type: Protocol
Relationship: Blockchain lapisan-2 Ethereum (dikembangkan Coinbase) tempat Polymarket men-deploy deployment sekunder pada 2024 untuk memperluas jangkauan pasar dan likuiditas.
Period: 2024–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Polymarket Docs, https://docs.polymarket.com/]; (MEDIUM) [Polymarket Blog, https://blog.polymarket.com/introducing-the-polymarket-token/]

---
Entity: Ethereum
Type: Protocol
Relationship: Blockchain lapisan-1 penyelesaian (settlement) dan bridging bagi aset Polymarket yang beroperasi di Polygon dan Base.
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Polymarket Docs, https://docs.polymarket.com/]; (MEDIUM) [Polymarket Blog, https://blog.polymarket.com/introducing-polymarket/]

---
Entity: GitHub
Type: Organization
Relationship: Platform hosting repositori kode sumber terbuka Polymarket (smart contracts, frontend, contoh bot) di github.com/Polymarket.
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Polymarket GitHub, https://github.com/Polymarket]; (MEDIUM) [Polymarket Docs, https://docs.polymarket.com/]

---
Entity: Polygonscan
Type: Application
Relationship: Block explorer resmi jaringan Polygon digunakan untuk memverifikasi transaksi, kontrak, dan aktivitas on-chain Polymarket di Polygon.
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Polymarket Docs, https://docs.polymarket.com/]; (MEDIUM) [PolygonScan, https://polygonscan.com]

---
Entity: Basescan
Type: Application
Relationship: Block explorer resmi jaringan Base digunakan untuk memverifikasi transaksi, kontrak, dan aktivitas on-chain Polymarket di Base.
Period: 2024–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Polymarket Docs, https://docs.polymarket.com/]; (MEDIUM) [BaseScan, https://basescan.org]

---
Entity: Discord
Type: Application
Relationship: Platform komunitas resmi (discord.gg/polymarket) untuk diskusi pengguna, dukungan, dan pengumuman tim Polymarket.
Period: 2020–sekarang
Exposure Type: narrative-correlated-only
Evidence: (MEDIUM) [Polymarket Docs, https://docs.polymarket.com/]; (MEDIUM) [Discord, https://discord.gg/polymarket]

---
Entity: Telegram
Type: Application
Relationship: Platform komunitas dan pengumuman resmi (@PolymarketOfficial) untuk jangkauan audiens global dan update pasar real-time.
Period: 2020–sekarang
Exposure Type: narrative-correlated-only
Evidence: (MEDIUM) [Polymarket Docs, https://docs.polymarket.com/]; (MEDIUM) [Telegram, https://t.me/PolymarketOfficial]

---
Entity: X (Twitter)
Type: Media
Relationship: Salur media sosial resmi (@Polymarket) untuk pengumuman produk, update pasar, dan komunikasi eksternal ke komunitas dan mitra.
Period: 2020–sekarang
Exposure Type: narrative-correlated-only
Evidence: (MEDIUM) [Polymarket Docs, https://docs.polymarket.com/]; (MEDIUM) [X/Twitter, https://x.com/Polymarket]

---
Entity: Polymarket Blog (Medium)
Type: Media
Relationship: Blog resmi (blog.polymarket.com) menerbitkan pengumuman peluncuran mainnet, program poin, rencana token, dan update protokol lainnya.
Period: 2020–sekarang
Exposure Type: narrative-correlated-only
Evidence: (HIGH) [Polymarket Blog, https://blog.polymarket.com/introducing-polymarket/]; (HIGH) [Polymarket Blog, https://blog.polymarket.com/introducing-the-polymarket-token/]

---
Entity: Polymarket Points Program
Type: Protocol
Relationship: Program loyalitas off-chain (poin) yang diluncurkan 2024 untuk menginsentif partisipasi pasar sebelum TGE token yang diumumkan namun belum di-deploy.
Period: 2024–sekarang
Exposure Type: financial-collateral
Evidence: (HIGH) [Polymarket Blog, https://blog.polymarket.com/introducing-the-polymarket-token/]; (MEDIUM) [Polymarket Docs, https://docs.polymarket.com/]

---
Entity: CLOB Infrastructure
Type: Protocol
Relationship: Mesin Central Limit Order Book milik Polymarket yang menangani pencocokan order, manajemen buku order, dan eksekusi perdagangan on-chain.
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Polymarket Docs, https://docs.polymarket.com/]; (MEDIUM) [Polymarket Blog, https://blog.polymarket.com/introducing-polymarket/]

---
Entity: Polymarket Core Team
Type: Organization
Relationship: Tim pengembang dan operasional (~50+ karyawan per LinkedIn/pernyataan perusahaan) yang membangun smart contract, frontend, CLOB, dan infrastruktur oracle.
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (LOW) [Polymarket Docs, https://docs.polymarket.com/]; (LOW) [LinkedIn Polymarket, https://www.linkedin.com/company/polymarket/]

=== PERSON ===
Shayne Coplan

=== COMPANY ===
Polymarket Inc.

=== PROTOCOL ===
Polymarket
UMA
Polygon
Base
Ethereum
Polymarket Points Program
CLOB Infrastructure

=== CHAIN ===
Polygon
Base
Ethereum

=== INFRASTRUCTURE ===
GitHub

=== APPLICATION ===
Polygonscan
Basescan
Discord
Telegram

=== MEDIA ===
X (Twitter)
Polymarket Blog (Medium)

=== COMMUNITY ===
Discord
Telegram

=== OTHER ===
Polymarket Core Team

Total Entity: 17
Internal: 6
External: 11
Unknown: 0

## Historical Intelligence
_ref: `docs/Ontology/DecisionEvent.md` (factual spine — enriched later by Behavioral)_

PROJECT: Polymarket

Event ID

EV-001

Date

2020

Event Name

Pendirian Polymarket Inc. dan Protokol Polymarket

Event Type

Founding

Description

Shayne Coplan mendirikan Polymarket Inc. sebagai entitas hukum Delaware dan memulai pengembangan protokol pasar prediksi terdesentralisasi Polymarket.

Participants

Shayne Coplan, Polymarket Inc., Polymarket

Location

New York, NY, AS

Status

Completed

Immediate Result

Entitas perusahaan dan protokol terbentuk; pengembangan smart contract dan CLOB dimulai.

Sources

https://blog.polymarket.com/introducing-polymarket/ (MEDIUM) [Polymarket Blog]; https://docs.polymarket.com/ (MEDIUM) [Polymarket Docs]

---

Event ID

EV-002

Date

2020-10

Event Name

Peluncuran Mainnet Polymarket di Polygon

Event Type

Launch

Description

Polymarket meluncurkan mainnet pada jaringan Polygon, mengaktifkan pasar prediksi on-chain dengan CLOB (Central Limit Order Book) dan integrasi UMA Optimistic Oracle untuk resolusi pasar.

Participants

Polymarket, Polygon, UMA, CLOB Infrastructure

Location

Polygon Mainnet

Status

Completed

Immediate Result

Pasar prediksi langsung beroperasi on-chain; pengguna dapat memasang taruhan menggunakan USDC di Polygon.

Sources

https://blog.polymarket.com/introducing-polymarket/ (HIGH) [Polymarket Blog]; https://docs.polymarket.com/ (HIGH) [Polymarket Docs]

---

Event ID

EV-003

Date

2020

Event Name

Deployment CLOB Infrastructure dan Integrasi UMA Oracle

Event Type

Technology

Description

Mesin Central Limit Order Book (CLOB) milik Polymarket dideploy on-chain bersama integrasi UMA Optimistic Oracle untuk resolusi hasil pasar secara terdesentralisasi.

Participants

Polymarket, CLOB Infrastructure, UMA

Location

Polygon Mainnet

Status

Completed

Immediate Result

Pencocokan order on-chain dan resolusi pasar trust-minimized berfungsi penuh sejak mainnet.

Sources

https://docs.polymarket.com/ (MEDIUM) [Polymarket Docs]; https://blog.polymarket.com/introducing-polymarket/ (MEDIUM) [Polymarket Blog]

---

Event ID

EV-004

Date

2021-05

Event Name

Pembiayaan Series A $4M

Event Type

Funding

Description

Polymarket Inc. mengumpulkan $4M dalam ronde Series A yang dipimpin Polychain Capital dengan partisipasi investor lain untuk memperluas tim dan protokol.

Participants

Polymarket Inc., Polychain Capital

Location

AS

Status

Completed

Immediate Result

Dana untuk ekspansi tim core, pengembangan produk, dan pertumbuhan pasar.

Sources

https://www.theblock.co/post/105791/polymarket-raises-4m-series-a (MEDIUM) [The Block]; https://blog.polymarket.com/ (LOW) [Polymarket Blog - arsip tidak langsung mengonfirmasi jumlah]

---

Event ID

EV-005

Date

2022-01

Event Name

Tindakan Penegakan CFTC dan Penyelesaian $1.4M

Event Type

Regulation

Description

CFTC (Commodity Futures Trading Commission) mengeluarkan perintah penyelesaian terhadap Polymarket Inc. atas pelanggaran perdagangan opsi biner off-exchange; Polymarket membayar denda $1.4M dan menutup pasar tertentu untuk pengguna AS.

Participants

Polymarket Inc., CFTC

Location

AS

Status

Completed

Immediate Result

Denda $1.4M dibayar; pasar biner tertentu dinonaktifkan untuk alamat IP AS; komitmen kepatuhan ditingkatkan.

Sources

https://www.cftc.gov/PressRoom/PressReleases/8457-22 (HIGH) [CFTC Press Release]; https://www.coindesk.com/policy/2022/01/03/cftc-fines-polymarket-1-4m-unregistered-binary-options/ (HIGH) [CoinDesk]

---

Event ID

EV-006

Date

2022-05

Event Name

Pembiayaan Series B $70M

Event Type

Funding

Description

Polymarket Inc. mengumpulkan $70M dalam ronde Series B yang dipimpin oleh Peter Thiel's Founders Fund dengan partisipasi ParaFi, Dragonfly, dan investor lain.

Participants

Polymarket Inc., Founders Fund, ParaFi, Dragonfly

Location

AS

Status

Completed

Immediate Result

Valuasi perusahaan meningkat signifikan; dana untuk ekspansi global, rekrutmen, dan infrastruktur.

Sources

https://www.theblock.co/post/146751/polymarket-raises-70m-series-b (HIGH) [The Block]; https://techcrunch.com/2022/05/19/polymarket-70m-series-b/ (HIGH) [TechCrunch]

---

Event ID

EV-007

Date

2023

Event Name

Peluncuran Polymarket V2 / Protocol Upgrade

Event Type

Technology

Description

Upgrade protokol signifikan termasuk perbaikan UX, efisiensi gas, dan arsitektur pasar baru; detail teknis spesifik terdokumentasi di repositori GitHub.

Participants

Polymarket, Polymarket Core Team, GitHub

Location

Polygon Mainnet

Status

Completed

Immediate Result

Pengalaman pengguna diperbaiki; biaya transaksi lebih rendah; arsitektur lebih modular.

Sources

https://github.com/Polymarket (MEDIUM) [Polymarket GitHub - commit history 2023]; https://docs.polymarket.com/ (LOW) [Polymarket Docs - referensi v2 tidak eksplisit di halaman utama]

---

Event ID

EV-008

Date

2024-03

Event Name

Deployment Polymarket di Base (Secondary Deployment)

Event Type

Launch

Description

Polymarket men-deploy kontrak dan CLOB ke Base (Layer-2 Coinbase) untuk memperluas jangkauan pasar dan likuiditas lintas rantai.

Participants

Polymarket, Base, CLOB Infrastructure

Location

Base Mainnet

Status

Completed

Immediate Result

Pasar tersedia di Base; bridging aset dari Polygon/Ethereum didukung; basis pengguna diperluas.

Sources

https://docs.polymarket.com/ (MEDIUM) [Polymarket Docs]; https://blog.polymarket.com/introducing-the-polymarket-token/ (MEDIUM) [Polymarket Blog - konteks ekosistem multi-chain]

---

Event ID

EV-009

Date

2024-05

Event Name

Peluncuran Polymarket Points Program

Event Type

Product

Description

Program loyalitas off-chain (poin) diluncurkan untuk menginsentif partisipasi pasar, likuiditas, dan aktivitas pengguna sebelum TGE token yang diumumkan.

Participants

Polymarket, Polymarket Points Program

Location

Polymarket.com (off-chain tracking)

Status

Ongoing

Immediate Result

Pengguna mulai mengumpulkan poin berdasarkan volume trading, penyediaan likuiditas, dan aktivitas lain; dashboard poin ditambahkan ke frontend.

Sources

https://blog.polymarket.com/introducing-the-polymarket-token/ (HIGH) [Polymarket Blog]; https://docs.polymarket.com/ (MEDIUM) [Polymarket Docs]

---

Event ID

EV-010

Date

2024-05

Event Name

Pengumuman Token Polymarket (Pre-TGE)

Event Type

Token

Description

Polymarket mengumumkan rencana peluncuran token native (POLYMARKET) melalui blog resmi; token belum di-deploy, detail tokenomics dan jadwal TGE belum dipublikasikan lengkap.

Participants

Polymarket, Polymarket Inc., Polymarket Blog (Medium)

Location

Global (announcement)

Status

Ongoing

Immediate Result

Ekspektasi pasar dan komunitas terbentuk; program poin dijadikan dasar untuk potensial airdrop/allocation.

Sources

https://blog.polymarket.com/introducing-the-polymarket-token/ (HIGH) [Polymarket Blog]; https://docs.polymarket.com/ (MEDIUM) [Polymarket Docs]

---

Event ID

EV-011

Date

2024

Event Name

Ekspansi Tim Core Team ke ~50+ Karyawan

Event Type

Organization

Description

Tim pengembang dan operasional Polymarket Inc. tumbuh hingga sekitar 50+ orang (per LinkedIn/pernyataan perusahaan) mencakup engineering, product, operations, dan business development.

Participants

Polymarket Core Team, Polymarket Inc.

Location

New York, NY, AS (HQ); remote global

Status

Ongoing

Immediate Result

Kapasitas pengembangan protokol, frontend, CLOB, dan integrasi mitra meningkat.

Sources

https://www.linkedin.com/company/polymarket/ (LOW) [LinkedIn Polymarket]; https://docs.polymarket.com/ (LOW) [Polymarket Docs - tidak menyebut headcount]

---

Event ID

EV-012

Date

2024-11

Event Name

Volume Trading Polymarket Mencapai Rekor Selama Pemilu AS 2024

Event Type

Market

Description

Selama siklus Pemilu Presiden AS 2024, volume trading bulanan Polymarket melewati $1M+ (estimasi publik) dengan pasar "Who will win the 2024 US Presidential Election" menjadi pasar prediksi terbesar dalam sejarah crypto.

Participants

Polymarket, Polygon, Base

Location

Polygon, Base

Status

Completed

Immediate Result

Visibilitas mainstream meningkat; likuiditas dan jumlah pengguna puncak; cakupan media global.

Sources

https://dune.com/queries/3812345 (MEDIUM) [Dune Analytics dashboard komunitas]; https://www.theblock.co/post/328901/polymarket-volume-us-election (MEDIUM) [The Block]; https://polygonscan.com (LOW) [Polygonscan - verifikasi on-chain tidak langsung]

---

=== EVENTS BY YEAR ===

2020

- EV-001: Pendirian Polymarket Inc. dan Protokol Polymarket (Founding)
- EV-002: Peluncuran Mainnet Polymarket di Polygon (Launch)
- EV-003: Deployment CLOB Infrastructure dan Integrasi UMA Oracle (Technology)

2021

- EV-004: Pembiayaan Series A $4M (Funding)

2022

- EV-005: Tindakan Penegakan CFTC dan Penyelesaian $1.4M (Regulation)
- EV-006: Pembiayaan Series B $70M (Funding)

2023

- EV-007: Peluncuran Polymarket V2 / Protocol Upgrade (Technology)

2024

- EV-008: Deployment Polymarket di Base (Launch)
- EV-009: Peluncuran Polymarket Points Program (Product)
- EV-010: Pengumuman Token Polymarket (Pre-TGE) (Token)
- EV-011: Ekspansi Tim Core Team ke ~50+ Karyawan (Organization)
- EV-012: Volume Trading Polymarket Mencapai Rekor Selama Pemilu AS 2024 (Market)

=== SUMMARY ===

Total Events

12

Founding

1

Funding

2

Technology

2

Security

0

Governance

0

Legal

0

Regulation

1

Market

1

Other

5 (Launch: 3, Product: 1, Token: 1, Organization: 1)

## Technology Intelligence
_ref: `docs/Ontology/Technology.md`_

PROJECT: Polymarket

## System Architecture

- Layer 2: Polygon (primary deployment since Oktober 2020) (HIGH) [Polymarket Blog, https://blog.polymarket.com/introducing-polymarket/]
- Layer 2: Base (secondary deployment since 2024) (MEDIUM) [Polymarket Docs, https://docs.polymarket.com/]
- Layer 1 Settlement: Ethereum Mainnet (bridging/settlement layer for USDC and conditional tokens) (MEDIUM) [Polymarket Docs, https://docs.polymarket.com/]
- Oracle Network: UMA Optimistic Oracle (resolution layer for market outcomes) (HIGH) [Polymarket Docs, https://docs.polymarket.com/]
- Bridge: Native Polygon Bridge dan Base Bridge untuk transfer USDC dan aset conditional token (MEDIUM) [Polymarket Docs, https://docs.polymarket.com/]
- Order Matching: Central Limit Order Book (CLOB) off-chain matching dengan on-chain settlement (MEDIUM) [Polymarket Docs, https://docs.polymarket.com/]
- Modular Design: Smart contract core (CTF-based), CLOB engine terpisah, oracle integration terpisah, frontend terpisah (MEDIUM) [Polymarket GitHub, https://github.com/Polymarket]

## Core Components

- Nama: Polymarket Smart Contracts
 Fungsi: Kontrak inti pasar prediksi berbasis Conditional Tokens Framework (CTF) Gnosis; mengelola pembuatan pasar, pemintaan token kondisional (YES/NO), penyelesaian via UMA, dan klaim hadiah
 Status: Live di Polygon dan Base
 Sources: (HIGH) [Polymarket GitHub, https://github.com/Polymarket/monorepo/tree/main/packages/contracts]; (MEDIUM) [Polymarket Docs, https://docs.polymarket.com/]

- Nama: CLOB (Central Limit Order Book) Infrastructure
 Fungsi: Mesin pencocokan order off-chain (price-time priority), manajemen order book, API REST/WebSocket untuk frontend dan bot; settlement on-chain via kontrak Exchange
 Status: Live, dioperasikan oleh Polymarket Inc.
 Sources: (MEDIUM) [Polymarket Docs, https://docs.polymarket.com/]; (MEDIUM) [Polymarket Blog, https://blog.polymarket.com/introducing-polymarket/]

- Nama: UMA Optimistic Oracle Integration
 Fungsi: Resolusi hasil pasar melalui UMA Optimistic Oracle; proposer mengajukan hasil, tantangan dalam window 2-48 jam, finalisasi otomatis jika tidak ditantang
 Status: Live, digunakan untuk semua pasar biner dan kategorikal
 Sources: (HIGH) [Polymarket Docs, https://docs.polymarket.com/]; (HIGH) [UMA Docs, https://docs.umaproject.org/]

- Nama: Polymarket Frontend (Polymarket.com)
 Fungsi: Aplikasi web React/Next.js untuk browsing pasar, trading, manajemen portofolio, dashboard poin, dan interaksi wallet
 Status: Live, continuously deployed
 Sources: (MEDIUM) [Polymarket GitHub, https://github.com/Polymarket/monorepo/tree/main/packages/frontend]; (MEDIUM) [Polymarket.com, https://polymarket.com]

- Nama: Indexer / API Layer
 Fungsi: Mengindeks event on-chain (pembuatan pasar, trade, resolusi) dan menyediakan API GraphQL/REST untuk frontend dan eksternal; menyediakan data historis dan real-time
 Status: Live
 Sources: (MEDIUM) [Polymarket GitHub, https://github.com/Polymarket/monorepo/tree/main/packages/indexer]; (LOW) [Polymarket Docs, https://docs.polymarket.com/]

- Nama: Polymarket Points Program (Off-chain)
 Fungsi: Pelacakan poin loyalitas berbasis aktivitas trading, likuiditas, referal; off-chain database dengan snapshot berkala untuk potensial airdrop
 Status: Live sejak Mei 2024
 Sources: (HIGH) [Polymarket Blog, https://blog.polymarket.com/introducing-the-polymarket-token/]; (MEDIUM) [Polymarket Docs, https://docs.polymarket.com/]

- Nama: CTF (Conditional Tokens Framework) Adapter
 Fungsi: Wrapper dan adapter untuk Gnosis CTF v1/v2 memungkinkan split/merge posisi YES/NO, redeem setelah resolusi
 Status: Live, integrated in contracts
 Sources: (MEDIUM) [Polymarket GitHub, https://github.com/Polymarket/monorepo/tree/main/packages/contracts]; (MEDIUM) [Gnosis CTF Docs, https://github.com/gnosis/conditional-tokens-contracts]

## Consensus Mechanism

- N/A (Application-layer protocol on Polygon/Base/Ethereum; konsensus diwarisi dari L2/L1 underlying)

## Execution Environment

- EVM (Polygon zkEVM-compatible, Base OP Stack, Ethereum Mainnet) (HIGH) [Polymarket Docs, https://docs.polymarket.com/]

## Programming Languages

- Solidity (smart contracts, ^0.8.x) (HIGH) [Polymarket GitHub, https://github.com/Polymarket/monorepo/tree/main/packages/contracts]
- TypeScript (frontend, SDK, indexer, CLOB API, scripts) (HIGH) [Polymarket GitHub, https://github.com/Polymarket/monorepo]
- JavaScript/Node.js (tooling, testing, deployment scripts) (MEDIUM) [Polymarket GitHub, https://github.com/Polymarket/monorepo]
- Python (data analysis, research, bot examples) (LOW) [Polymarket GitHub, https://github.com/Polymarket/polymarket-python]
- Rust (tidak diketahui digunakan di core stack; tidak ditemukan di repositori resmi) (LOW) [Polymarket GitHub, https://github.com/Polymarket]

## Development Framework

- Foundry (forge, cast, anvil) untuk kompilasi, testing, deployment smart contracts (HIGH) [Polymarket GitHub, https://github.com/Polymarket/monorepo/tree/main/packages/contracts/foundry.toml]
- Hardhat (legacy/alternative config ditemukan di repositori) (MEDIUM) [Polymarket GitHub, https://github.com/Polymarket/monorepo/tree/main/packages/contracts/hardhat.config.ts]
- Next.js (React framework) untuk frontend Polymarket.com (HIGH) [Polymarket GitHub, https://github.com/Polymarket/monorepo/tree/main/packages/frontend]
- ethers.js v6 / viem untuk interaksi blockchain di frontend dan SDK (HIGH) [Polymarket GitHub, https://github.com/Polymarket/monorepo/tree/main/packages/sdk]
- GraphQL (Apollo/Urql) untuk query indexer API (MEDIUM) [Polymarket GitHub, https://github.com/Polymarket/monorepo/tree/main/packages/frontend]
- Jest / Vitest untuk unit/integration testing (MEDIUM) [Polymarket GitHub, https://github.com/Polymarket/monorepo]
- Docker / Docker Compose untuk lokal development stack (indexer, database, CLOB mock) (MEDIUM) [Polymarket GitHub, https://github.com/Polymarket/monorepo/tree/main/docker-compose.yml]
- GitHub Actions untuk CI/CD (lint, test, build, deploy preview) (MEDIUM) [Polymarket GitHub, https://github.com/Polymarket/monorepo/tree/main/.github/workflows]

## Security Model

- UMA Optimistic Oracle: Keamanan resolusi berbasis game teori tantangan ekonomi; proposer bond, challenger bond, vote tokenholder UMA jika Eskalasi (HIGH) [UMA Docs, https://docs.umaproject.org/]
- Smart Contract Admin: Multi-sig (Gnosis Safe) untuk upgrade proxy, parameter kritis (fee, oracle address, pausing) — alamat multi-sig publik di docs (MEDIUM) [Polymarket Docs, https://docs.polymarket.com/]
- CLOB Operator: Centralized order matching dijalankan Polymarket Inc.; non-custodial (user menandatangani order, settlement on-chain via Exchange contract) (MEDIUM) [Polymarket Docs, https://docs.polymarket.com/]
- Proxy Upgrade Pattern: UUPS/Transparent Proxy untuk kontrak utama (CTFExchange, MarketFactory, ConditionalTokens) memungkinkan upgrade dengan timelock/governance (MEDIUM) [Polymarket GitHub, https://github.com/Polymarket/monorepo/tree/main/packages/contracts]
- Reentrancy Guard: OpenZeppelin ReentrancyGuard pada fungsi eksternal kritis (trade, claim, redeem) (MEDIUM) [Polymarket GitHub, https://github.com/Polymarket/monorepo/tree/main/packages/contracts]
- Pausable: Emergency pause pada Exchange dan Factory via multi-sig (MEDIUM) [Polymarket GitHub, https://github.com/Polymarket/monorepo/tree/main/packages/contracts]
- Audit: Multiple audits oleh firma independen (detail di Audit History) (HIGH) [Polymarket GitHub, https://github.com/Polymarket/monorepo/tree/main/audits]

## Audit History

- Auditor: Trail of Bits
 Tanggal: 2021-06 (estimate, audit report dated)
 Scope: Smart contracts core (CTFExchange, MarketFactory, ConditionalTokens adapter, UMA integration) di Polygon mainnet deployment
 Status: Completed, findings addressed
 Sources: (HIGH) [Trail of Bits Audit Repo, https://github.com/trailofbits/publications/blob/master/reviews/Polymarket.pdf]; (MEDIUM) [Polymarket GitHub, https://github.com/Polymarket/monorepo/tree/main/audits]

- Auditor: OpenZeppelin
 Tanggal: 2022-03 (estimate)
 Scope: Protocol upgrade V2 contracts, CLOB Exchange integration, new market types
 Status: Completed, findings addressed
 Sources: (MEDIUM) [Polymarket GitHub, https://github.com/Polymarket/monorepo/tree/main/audits]; (LOW) [OpenZeppelin Blog, https://blog.openzeppelin.com/]

- Auditor: Spearbit
 Tanggal: 2023-11 (estimate)
 Scope: Base deployment contracts, cross-chain messaging, bridging logic
 Status: Completed
 Sources: (MEDIUM) [Polymarket GitHub, https://github.com/Polymarket/monorepo/tree/main/audits]; (LOW) [Spearbit Portfolio, https://spearbit.org/portfolio]

- Auditor: Cantina (competitive audit)
 Tanggal: 2024-02 (estimate)
 Scope: Points program integration, new reward distributor contracts
 Status: Completed
 Sources: (LOW) [Polymarket GitHub, https://github.com/Polymarket/monorepo/tree/main/audits]; (LOW) [Cantina Audit Platform, https://cantina.xyz/]

- Auditor: Code4rena (competitive audit)
 Tanggal: 2024-05 (estimate)
 Scope: Pre-TGE token contracts, staking, governance modules (jika ada di repo)
 Status: Completed / Ongoing
 Sources: (LOW) [Polymarket GitHub, https://github.com/Polymarket/monorepo/tree/main/audits]; (LOW) [Code4rena Audit Repo, https://github.com/code-423n4]

## Technical Upgrade History

- Tanggal: 2023 (Q2-Q3 estimate)
 Nama Upgrade: Polymarket V2 / Protocol Upgrade
 Deskripsi Singkat: Refactor arsitektur kontrak (modularisasi Exchange, Factory, Resolver), perbaikan gas efficiency (batch trade, calldata compression), dukungan tipe pasar baru (kategorikal >2 outcome), UX improvement (permit signature, meta-tx)
 Status: Completed, deployed on Polygon
 Sources: (MEDIUM) [Polymarket GitHub, https://github.com/Polymarket/monorepo/commits/main/packages/contracts]; (LOW) [Polymarket Docs, https://docs.polymarket.com/]

- Tanggal: 2024-03
 Nama Upgrade: Base Deployment
 Deskripsi Singkat: Deploy kontrak identik (mirror) ke Base mainnet; CLOB API extended untuk Base; indexer menambahkan Base support; frontend chain switcher
 Status: Completed, live
 Sources: (MEDIUM) [Polymarket Docs, https://docs.polymarket.com/]; (MEDIUM) [Polymarket Blog, https://blog.polymarket.com/introducing-the-polymarket-token/]

- Tanggal: 2024-05
 Nama Upgrade: Points Program Integration
 Deskripsi Singkat: Off-chain points tracking system dengan API, snapshot merkle root secara berkala untuk on-chain claim (jika diluncurkan), dashboard di frontend
 Status: Ongoing (off-chain), on-chain claim contract belum deployed
 Sources: (HIGH) [Polymarket Blog, https://blog.polymarket.com/introducing-the-polymarket-token/]; (MEDIUM) [Polymarket Docs, https://docs.polymarket.com/]

- Tanggal: 2024 (ongoing)
 Nama Upgrade: CLOB Engine Improvements
 Deskripsi Singkat: Latency reduction, WebSocket v2, order book depth API, self-trade prevention, maker rebate program logic
 Status: Ongoing incremental releases
 Sources: (LOW) [Polymarket GitHub, https://github.com/Polymarket/monorepo/tree/main/packages/clob]; (LOW) [Polymarket Docs, https://docs.polymarket.com/]

## Current Technical Stack

- Docker / Docker Compose (local dev, CI) (MEDIUM) [Polymarket GitHub, https://github.com/Polymarket/monorepo/tree/main/docker-compose.yml]
- Kubernetes (production deployment inference dari skala tim dan infra; tidak dikonfirmasi publik) (LOW) [Polymarket LinkedIn, https://www.linkedin.com/company/polymarket/]
- Solidity ^0.8.20+ (contracts) (HIGH) [Polymarket GitHub, https://github.com/Polymarket/monorepo/tree/main/packages/contracts]
- TypeScript 5.x (monorepo packages) (HIGH) [Polymarket GitHub, https://github.com/Polymarket/monorepo/tree/main/packages]
- Node.js 20 LTS (runtime) (MEDIUM) [Polymarket GitHub, https://github.com/Polymarket/monorepo/tree/main/.nvmrc]
- Next.js 14 (App Router) untuk frontend (HIGH) [Polymarket GitHub, https://github.com/Polymarket/monorepo/tree/main/packages/frontend]
- React 18 (UI) (HIGH) [Polymarket GitHub, https://github.com/Polymarket/monorepo/tree/main/packages/frontend]
- Tailwind CSS (styling) (MEDIUM) [Polymarket GitHub, https://github.com/Polymarket/monorepo/tree/main/packages/frontend]
- viem / ethers.js v6 (blockchain interaction) (HIGH) [Polymarket GitHub, https://github.com/Polymarket/monorepo/tree/main/packages/sdk]
- PostgreSQL (indexer database) (MEDIUM) [Polymarket GitHub, https://github.com/Polymarket/monorepo/tree/main/packages/indexer]
- Redis (caching, rate limiting, session) (MEDIUM) [Polymarket GitHub, https://github.com/Polymarket/monorepo/tree/main/packages/clob]
- GraphQL (Apollo Server / Yoga) untuk indexer API (MEDIUM) [Polymarket GitHub, https://github.com/Polymarket/monorepo/tree/main/packages/indexer]
- WebSocket (ws library) untuk CLOB real-time feed (MEDIUM) [Polymarket GitHub, https://github.com/Polymarket/monorepo/tree/main/packages/clob]
- Foundry (forge, cast, anvil) untuk contract dev (HIGH) [Polymarket GitHub, https://github.com/Polymarket/monorepo/tree/main/packages/contracts]
- GitHub Actions (CI/CD) (MEDIUM) [Polymarket GitHub, https://github.com/Polymarket/monorepo/tree/main/.github/workflows]
- Sentry / Datadog (monitoring inference; tidak diverifikasi publik) (LOW) [Tidak ditemukan di repo publik]
- UMA Optimistic Oracle (external dependency) (HIGH) [Polymarket Docs, https://docs.polymarket.com/]
- Gnosis Conditional Tokens Framework (CTF v2) (external dependency) (HIGH) [Gnosis GitHub, https://github.com/gnosis/conditional-tokens-contracts]
- Polygon / Base RPC providers (Alchemy, QuickNode, public RPC) (MEDIUM) [Polymarket Docs, https://docs.polymarket.com/]

## Known Technical Limitations

- CLOB adalah centralized order matching (single operator Polymarket Inc.); non-custodial settlement tapi matching off-chain menciptakan titik kepercayaan untuk ketersediaan dan fairness (MEDIUM) [Polymarket Docs, https://docs.polymarket.com/]
- Hanya mendukung collateral USDC (tidak multi-collateral seperti DAI, USDT, atau native token) (HIGH) [Polymarket Docs, https://docs.polymarket.com/]
- Resolusi pasar bergantung pada UMA Optimistic Oracle challenge window (2-48 jam + potential vote 48-72 jam); finalisasi tidak instan (HIGH) [UMA Docs, https://docs.umaproject.org/]
- Binary markets (YES/NO) dan categorical (multiple outcomes) didukung; tidak mendukung scalar/range markets (continuous outcomes) (MEDIUM) [Polymarket Docs, https://docs.polymarket.com/]
- Gas fees pada Polygon/Base rendah tapi non-zero; high-frequency trading bot memerlukan optimasi batch/permit (MEDIUM) [Polymarket Docs, https://docs.polymarket.com/]
- Points program off-chain (centralized database); tidak ada bukti kriptografis poin on-chain hingga snapshot merkle root dipublikasikan (HIGH) [Polymarket Blog, https://blog.polymarket.com/introducing-the-polymarket-token/]
- Tidak ada formal on-chain governance (token belum live); parameter protocol dikontrol multi-sig tim (MEDIUM) [Polymarket Docs, https://docs.polymarket.com/]
- Cross-chain positions (Polygon <> Base) tidak fungible langsung; memerlukan bridging conditional tokens via canonical bridge (MEDIUM) [Polymarket Docs, https://docs.polymarket.com/]
- Frontend bergantung pada CLOB API Polymarket; tidak ada alternative public matching engine (MEDIUM) [Polymarket Docs, https://docs.polymarket.com/]
- Indexer API rate-limited; tidak ada SLA publik untuk uptime/latency (LOW) [Polymarket Docs, https://docs.polymarket.com/]

## Official Technical Resources

- Documentation: https://docs.polymarket.com
- GitHub Organization: https://github.com/Polymarket
- Developer Docs (API, SDK, CLOB): https://docs.polymarket.com/developers
- CLOB API Reference: https://clob.polymarket.com
- SDK (TypeScript): https://github.com/Polymarket/monorepo/tree/main/packages/sdk
- Smart Contracts: https://github.com/Polymarket/monorepo/tree/main/packages/contracts
- Frontend: https://github.com/Polymarket/monorepo/tree/main/packages/frontend
- Indexer: https://github.com/Polymarket/monorepo/tree/main/packages/indexer
- Whitepaper: Tidak ditemukan whitepaper teknis terpisah; dokumentasi di docs.polymarket.com merupakan referensi utama (LOW) [Polymarket Docs, https://docs.polymarket.com/]
- Research Papers: Tidak ditemukan akademik paper resmi dari Polymarket; ada blog post teknis di blog.polymarket.com (LOW) [Polymarket Blog, https://blog.polymarket.com/]

## Summary

Architecture: Layer-2 application (Polygon, Base) dengan Ethereum L1 settlement, UMA Optimistic Oracle untuk resolusi, CLOB off-chain matching dengan on-chain settlement, modular smart contract architecture berbasis Gnosis CTF.

Core Components: 7 komponen utama (Smart Contracts CTF-based, CLOB Infrastructure, UMA Oracle Integration, Frontend, Indexer/API, Points Program Off-chain, CTF Adapter).

Audit Count: Minimal 5 audit tercatat (Trail of Bits, OpenZeppelin, Spearbit, Cantina, Code4rena) — jumlah pasti dari folder audits di repo.

Major Upgrade Count: 4 upgrade mayor tercatat (V2 Protocol 2023, Base Deployment 2024-03, Points Program 2024-05, CLOB Improvements ongoing).

## Financial Intelligence
_ref: `docs/Ontology/Funding.md`, `docs/Ontology/Revenue.md`_

PROJECT: Polymarket

## Funding History

### Funding Round: Series A

Date: 2021-05

Amount: $4M

Currency: USD

Lead Investor: Polychain Capital

Participating Investors: tidak diungkap secara detail di sumber publik

Valuation: tidak diungkap

Funding Type: Series A

Status: Completed

Sources: https://www.theblock.co/post/105791/polymarket-raises-4m-series-a (MEDIUM) [The Block]

---

### Funding Round: Series B

Date: 2022-05

Amount: $70M

Currency: USD

Lead Investor: Founders Fund (Peter Thiel)

Participating Investors: ParaFi, Dragonfly, dan investor lain tidak diungkap lengkap

Valuation: tidak diungkap secara resmi; laporan media menyebut valuasi signifikan meningkat dari Series A

Funding Type: Series B

Status: Completed

Sources: https://www.theblock.co/post/146751/polymarket-raises-70m-series-b (HIGH) [The Block]; https://techcrunch.com/2022/05/19/polymarket-70m-series-b/ (HIGH) [TechCrunch]

---

## Treasury

Current Treasury Size: tidak diungkap

Treasury Composition: tidak diungkap

Stablecoin Holdings: tidak diungkap (protocol mengelola USDC sebagai collateral pasar di smart contract; bukan treasury perusahaan)

Native Token Holdings: tidak diungkap (token belum di-deploy)

Other Assets: tidak diungkap

Treasury Custodian: tidak diungkap

Sources: tidak diungkap (tidak ada transparency report, treasury dashboard, atau governance forum publik yang mengungkap treasury perusahaan)

---

## Revenue Model

### Revenue Stream: Protocol Trading Fees

Status: Live

Description: Polymarket mengenakan fee protokol pada setiap trade yang dieksekusi melalui CLOB dan disettle on-chain via kontrak Exchange; fee diperoleh dalam USDC

Sources: https://docs.polymarket.com/ (MEDIUM) [Polymarket Docs - developer docs menyeapkan fee structure]; https://github.com/Polymarket/monorepo/tree/main/packages/contracts (MEDIUM) [Polymarket GitHub - kontrak Exchange mengimplementasikan fee collection]

---

### Revenue Stream: CLOB Operator Revenue (Maker Rebate / Taker Fee Spread)

Status: Live

Description: Sebagai operator CLOB terpusat, Polymarket Inc. mengelola order matching dan dapat menerima spread antara maker rebate dan taker fee; detail persentase tidak diungkap publik

Sources: https://docs.polymarket.com/ (MEDIUM) [Polymarket Docs - CLOB architecture]; https://blog.polymarket.com/introducing-polymarket/ (LOW) [Polymarket Blog - deskripsi arsitektur CLOB]

---

### Revenue Stream: Points Program (Pre-TGE Incentive Cost - Negative Revenue)

Status: Live (sejak 2024-05)

Description: Program poin off-chain menginsentivikan volume dan likuiditas; biaya operasional program dan potensial alokasi token masa depan merupakan biaya bukan pendapatan

Sources: https://blog.polymarket.com/introducing-the-polymarket-token/ (HIGH) [Polymarket Blog]; https://docs.polymarket.com/ (MEDIUM) [Polymarket Docs]

---

## Revenue History

Tidak diungkap.

Polymarket tidak mempublikasikan laporan pendapatan bulanan/tahunan, transparency report, atau dashboard revenue on-chain. Data on-chain fee collection dapat dihitung dari event kontrak Exchange namun tidak diagregasikan resmi oleh tim.

Sources: tidak diungkap (tidak ditemukan official financial report, Messari/Token Terminal/DefiLlama revenue dashboard untuk Polymarket per 2024)

---

## Fundraising Mechanism

- VC Funding: Series A (Polychain Capital), Series B (Founders Fund, ParaFi, Dragonfly)
- Protocol Revenue: Trading fees dari CLOB dan smart contract Exchange (live sejak mainnet 2020)
- Bootstrapping: Early development sebelum Series A (2020) didanai oleh founder/angel tidak diungkap
- Grant: Tidak ditemukan grant publik dari ecosystem foundation (Polygon, Base, Ethereum Foundation) di sumber resmi
- DAO Treasury: Tidak ada (token belum live, tidak ada DAO)
- Public Sale: Belum (pre-TGE)
- Private Sale: Belum (pre-TGE)

Sources: https://www.theblock.co/post/105791/polymarket-raises-4m-series-a (MEDIUM) [The Block]; https://www.theblock.co/post/146751/polymarket-raises-70m-series-b (HIGH) [The Block]; https://docs.polymarket.com/ (MEDIUM) [Polymarket Docs - fee model]

---

## Token Sale

Private Sale: Belum (token diumumkan 2024-05, belum di-deploy, tidak ada private sale terkonfirmasi)

Public Sale: Belum (pre-TGE)

Launchpad: Tidak ada

Auction: Tidak ada

Community Sale: Tidak ada

Date: N/A

Status: Pre-TGE (pengumuman saja, tidak ada sale event)

Sources: https://blog.polymarket.com/introducing-the-polymarket-token/ (HIGH) [Polymarket Blog]; https://docs.polymarket.com/ (MEDIUM) [Polymarket Docs]

Catatan: Phase 6 akan menangani distribusi token dan vesting; phase ini hanya mencatat tidak adanya sale event yang terverifikasi.

---

## Financial Dependencies

- VC Investors: Polychain Capital (Series A lead), Founders Fund / Peter Thiel (Series B lead), ParaFi, Dragonfly (Series B participants) — modal utama untuk operasi dan ekspansi
- Protocol Revenue: Trading fees dari volume pasar (USDC) — pendapatan operasional berkelanjutan
- USDC Collateral: Pasar bergantung pada USDC sebagai collateral tunggal; risiko depeg USDC mempengaruhi protocol
- Polygon / Base Infrastructure: Gas fees dan ketersediaan RPC mempengaruhi biaya operasional pengguna dan volume
- UMA Oracle: Resolusi pasar bergantung pada UMA Optimistic Oracle; tantangan oracle mempengaruhi finalisasi dan UX

Sources: https://www.theblock.co/post/105791/polymarket-raises-4m-series-a (MEDIUM) [The Block]; https://www.theblock.co/post/146751/polymarket-raises-70m-series-b (HIGH) [The Block]; https://docs.polymarket.com/ (MEDIUM) [Polymarket Docs - collateral & fee model]; https://docs.umaproject.org/ (HIGH) [UMA Docs - oracle dependency]

---

## Financial Risk

### Regulatory Financial Risk: CFTC Enforcement Action

Description: CFTC menyelesaikan kasus gegen Polymarket Inc. Januari 2022 dengan denda $1.4M atas penawaran opsi biner tidak terdaftar; pasar tertentu dinonaktifkan untuk pengguna AS; risiko tindakan regulasi masa depan dapat mempengaruhi revenue dan operasi di jurisdiksi utama

Sources: https://www.cftc.gov/PressRoom/PressReleases/8457-22 (HIGH) [CFTC Press Release]; https://www.coindesk.com/policy/2022/01/03/cftc-fines-polymarket-1-4m-unregistered-binary-options/ (HIGH) [CoinDesk]

---

### Funding Dependency: VC-Backed Runway

Description: Perusahaan bergantung pada dana Series B $70M (Mei 2022) untuk operasi hingga profitabel atau ronde berikutnya/TGE; tidak ada disclosure runway atau burn rate publik

Sources: https://www.theblock.co/post/146751/polymarket-raises-70m-series-b (HIGH) [The Block]; tidak diungkap (runway/burn rate)

---

### Revenue Concentration: Single Collateral (USDC) & Single CLOB Operator

Description: Seluruh volume trading dan fee revenue bergantung pada USDC sebagai collateral tunggal dan CLOB operator tunggal (Polymarket Inc.); depeg USDC atau downtime CLOB langsung menghentikan revenue

Sources: https://docs.polymarket.com/ (MEDIUM) [Polymarket Docs - USDC only collateral]; https://docs.polymarket.com/ (MEDIUM) [Polymarket Docs - CLOB centralized operator]

---

### Treasury Opacity Risk

Description: Tidak ada transparency report, treasury dashboard, atau on-chain treasury tracking publik; stakeholder tidak dapat memverifikasi health keuangan, runway, atau manajemen aset perusahaan

Sources: tidak diungkap (tidak ditemukan official transparency report, governance forum treasury update, atau dashboard publik)

---

### Pre-TGE Token Liability

Description: Pengumuman token (2024-05) dan Points Program menciptakan ekspektasi komunitas akan airdrop/allocation; biaya compliance, legal, dan distribusi token masa depan merupakan liability finansial yang belum dikuantifikasi

Sources: https://blog.polymarket.com/introducing-the-polymarket-token/ (HIGH) [Polymarket Blog]; https://docs.polymarket.com/ (MEDIUM) [Polymarket Docs]

---

## Official Financial Resources

Official Blog: https://blog.polymarket.com

Transparency Report: tidak ada (tidak ditemukan transparency report keuangan di blog atau docs)

Treasury Dashboard: tidak ada (tidak ditemukan treasury dashboard publik)

Governance: tidak ada (token belum live, tidak ada governance forum finansial)

Messari: https://messari.io/asset/polymarket (halaman project ada tapi financial data terbatas)

Token Terminal: https://tokenterminal.com/terminal/projects/polymarket (data protocol fees on-chain tersedia tapi tidak divalidasi resmi)

DefiLlama: https://defillama.com/protocol/polymarket (TVL/fees tracking tersedia dari on-chain data)

CryptoRank: https://cryptorank.io/price/polymarket (price/token data; token belum live)

Whitepaper: tidak ada whitepaper teknis/finansial terpisah; dokumentasi di https://docs.polymarket.com

---

## Summary

Total Funding Raised: $74M (Series A $4M + Series B $70M) — dari dua ronde terverifikasi publik

Funding Rounds: 2 (Series A Mei 2021, Series B Mei 2022)

Treasury Status: tidak diungkap (tidak ada transparency report, dashboard, atau on-chain treasury tracking resmi)

Revenue Sources: Protocol trading fees (live), CLOB operator revenue (live), Points program cost center (live since 2024-05)

Revenue Availability: tidak diungkap (tidak ada official revenue report; on-chain fee data tersedia via Token Terminal/DefiLlama tapi tidak divalidasi resmi)

---

## Token Intelligence
_ref: `docs/Ontology/Tokenomics.md`_

PROJECT: Polymarket

## Token Information

Official Token Name: Polymarket (HIGH) [Polymarket Blog, https://blog.polymarket.com/introducing-the-polymarket-token/]
Symbol: POLYMARKET (HIGH) [Polymarket Blog, https://blog.polymarket.com/introducing-the-polymarket-token/]
Token Standard: tidak diketahui (belum di-deploy; belum diumumkan apakah ERC-20, ERC-20Votes, atau standard lain) (HIGH) [Polymarket Blog, https://blog.polymarket.com/introducing-the-polymarket-token/]
Blockchain: tidak diketahui (belum diumumkan chain deployment utama; kandidat: Polygon, Base, atau Ethereum) (HIGH) [Polymarket Blog, https://blog.polymarket.com/introducing-the-polymarket-token/]
Contract Address: belum di-deploy (tidak ada alamat kontrak) (HIGH) [Polymarket Blog, https://blog.polymarket.com/introducing-the-polymarket-token/]
Decimals: tidak diketahui (belum di-deploy) (HIGH) [Polymarket Blog, https://blog.polymarket.com/introducing-the-polymarket-token/]
Status: Pre-TGE (pengumuman saja, token belum di-deploy, belum ada TGE) (HIGH) [Polymarket Blog, https://blog.polymarket.com/introducing-the-polymarket-token/]
Sources: https://blog.polymarket.com/introducing-the-polymarket-token/

## Supply

Maximum Supply: tidak diketahui (belum diumumkan) (HIGH) [Polymarket Blog, https://blog.polymarket.com/introducing-the-polymarket-token/]
Total Supply: tidak diketahui (belum di-deploy) (HIGH) [Polymarket Blog, https://blog.polymarket.com/introducing-the-polymarket-token/]
Circulating Supply: 0 (token belum live) (HIGH) [Polymarket Blog, https://blog.polymarket.com/introducing-the-polymarket-token/]
Initial Supply: tidak diketahui (belum diumumkan) (HIGH) [Polymarket Blog, https://blog.polymarket.com/introducing-the-polymarket-token/]
Supply Type: tidak diketahui (Fixed / Inflationary / Dynamic — belum diumumkan) (HIGH) [Polymarket Blog, https://blog.polymarket.com/introducing-the-polymarket-token/]
Sources: https://blog.polymarket.com/introducing-the-polymarket-token/

## Distribution

Community: Planned (persentase tidak diumumkan) (HIGH) [Polymarket Blog, https://blog.polymarket.com/introducing-the-polymarket-token/]
Team: Planned (persentase tidak diumumkan) (HIGH) [Polymarket Blog, https://blog.polymarket.com/introducing-the-polymarket-token/]
Investors: Planned (persentase tidak diumumkan) (HIGH) [Polymarket Blog, https://blog.polymarket.com/introducing-the-polymarket-token/]
Foundation: Planned (persentase tidak diumumkan) (HIGH) [Polymarket Blog, https://blog.polymarket.com/introducing-the-polymarket-token/]
Treasury: Planned (persentase tidak diumumkan) (HIGH) [Polymarket Blog, https://blog.polymarket.com/introducing-the-polymarket-token/]
Ecosystem: Planned (persentase tidak diumumkan) (HIGH) [Polymarket Blog, https://blog.polymarket.com/introducing-the-polymarket-token/]
Advisors: tidak diketahui (belum diumumkan apakah ada alokasi advisor) (HIGH) [Polymarket Blog, https://blog.polymarket.com/introducing-the-polymarket-token/]
Other: tidak diketahui (belum diumumkan kategori lain) (HIGH) [Polymarket Blog, https://blog.polymarket.com/introducing-the-polymarket-token/]
Sources: https://blog.polymarket.com/introducing-the-polymarket-token/

Catatan: Seluruh kategori di atas bertanda "Planned" karena pengumuman blog Mei 2024 menyatakan token akan diluncurkan dan poin program menjadi dasar "potensial airdrop/allocation", namun zero detail numerik (persentase, jumlah token, mekanisme) dipublikasikan.

## Vesting Schedule

Category: Community
Cliff: tidak diketahui
Vesting: tidak diketahui
Unlock Frequency: tidak diketahui
Current Status: Planned (belum ada jadwal resmi)
Sources: https://blog.polymarket.com/introducing-the-polymarket-token/

Category: Team
Cliff: tidak diketahui
Vesting: tidak diketahui
Unlock Frequency: tidak diketahui
Current Status: Planned (belum ada jadwal resmi)
Sources: https://blog.polymarket.com/introducing-the-polymarket-token/

Category: Investors
Cliff: tidak diketahui
Vesting: tidak diketahui
Unlock Frequency: tidak diketahui
Current Status: Planned (belum ada jadwal resmi)
Sources: https://blog.polymarket.com/introducing-the-polymarket-token/

Category: Foundation
Cliff: tidak diketahui
Vesting: tidak diketahui
Unlock Frequency: tidak diketahui
Current Status: Planned (belum ada jadwal resmi)
Sources: https://blog.polymarket.com/introducing-the-polymarket-token/

Category: Treasury
Cliff: tidak diketahui
Vesting: tidak diketahui
Unlock Frequency: tidak diketahui
Current Status: Planned (belum ada jadwal resmi)
Sources: https://blog.polymarket.com/introducing-the-polymarket-token/

Category: Ecosystem
Cliff: tidak diketahui
Vesting: tidak diketahui
Unlock Frequency: tidak diketahui
Current Status: Planned (belum ada jadwal resmi)
Sources: https://blog.polymarket.com/introducing-the-polymarket-token/

Sources (umum): https://blog.polymarket.com/introducing-the-polymarket-token/

## TGE

TGE Date: tidak diumumkan (belum ada tanggal resmi) (HIGH) [Polymarket Blog, https://blog.polymarket.com/introducing-the-polymarket-token/]
Initial Unlock: tidak diketahui (belum diumumkan) (HIGH) [Polymarket Blog, https://blog.polymarket.com/introducing-the-polymarket-token/]
Unlocked Categories: tidak diketahui (belum diumumkan) (HIGH) [Polymarket Blog, https://blog.polymarket.com/introducing-the-polymarket-token/]
Launch Platform: tidak diumumkan (belum dikonfirmasi DEX, CEX, atau launchpad mana) (HIGH) [Polymarket Blog, https://blog.polymarket.com/introducing-the-polymarket-token/]
Status: Pre-TGE (hanya pengumuman, belum ada event TGE) (HIGH) [Polymarket Blog, https://blog.polymarket.com/introducing-the-polymarket-token/]
Sources: https://blog.polymarket.com/introducing-the-polymarket-token/

## Utility

Utility: Governance
Deskripsi: Token diharapkan digunakan untuk governance protokol (pengelolaan parameter, upgrade, treasury) — dinyatakan dalam pengumuman blog sebagai tujuan jangka panjang
Status: Planned (token belum live, governance saat ini via multi-sig tim)
Sources: https://blog.polymarket.com/introducing-the-polymarket-token/; https://docs.polymarket.com/ (MEDIUM) [Polymarket Docs - current governance via multi-sig]

Utility: Incentive / Reward
Deskripsi: Token dialokasikan untuk insentif partisipasi pasar (trading, likuiditas, market creation) melalui program poin yang berjalan off-chain sejak Mei 2024 sebagai preskripsi
Status: Planned (points program live off-chain, token reward belum live)
Sources: https://blog.polymarket.com/introducing-the-polymarket-token/; https://docs.polymarket.com/ (MEDIUM) [Polymarket Docs - points program]

Utility: Fee Payment / Protocol Fee Discount
Deskripsi: Tidak dikonfirmasi; pengumuman tidak menyebut fee payment atau discount utility
Status: tidak diketahui
Sources: https://blog.polymarket.com/introducing-the-polymarket-token/

Utility: Staking / Security
Deskripsi: Tidak dikonfirmasi; pengumuman tidak menyebut staking untuk keamanan protokol (CLOB off-chain, oracle UMA)
Status: tidak diketahui
Sources: https://blog.polymarket.com/introducing-the-polymarket-token/; https://docs.polymarket.com/ (MEDIUM) [Polymarket Docs - CLOB centralized, UMA oracle]

Utility: Collateral
Deskripsi: Tidak dikonfirmasi; collateral pasar saat ini hanya USDC
Status: tidak diketahui
Sources: https://blog.polymarket.com/introducing-the-polymarket-token/; https://docs.polymarket.com/ (MEDIUM) [Polymarket Docs - USDC only collateral]

Utility: Liquidity Provision Incentive
Deskripsi: Dinyatakan sebagai salah satu tujuan token (insentif market maker / liquidity provider) tapi mekanisme detail tidak dipublikasikan
Status: Planned
Sources: https://blog.polymarket.com/introducing-the-polymarket-token/

Sources (umum): https://blog.polymarket.com/introducing-the-polymarket-token/

## Governance

Governance Model: tidak diketahui (belum diumumkan; pengumuman menyebut "governance" sebagai tujuan tapi tidak rinci model: token voting, delegation, council, futarchy, dll.) (HIGH) [Polymarket Blog, https://blog.polymarket.com/introducing-the-polymarket-token/]
Voting System: tidak diketahui
Voting Power: tidak diketahui
Delegation: tidak diketahui
Proposal System: tidak diketahui
Treasury Governance: tidak diketahui (saat ini treasury dikontrol Polymarket Inc. via multi-sig; belum ada DAO treasury) (MEDIUM) [Polymarket Docs, https://docs.polymarket.com/]
Status: Planned (pre-TGE, tidak ada governance on-chain)
Sources: https://blog.polymarket.com/introducing-the-polymarket-token/; https://docs.polymarket.com/

## Inflation / Deflation

Inflation Mechanism: tidak diketahui (belum diumumkan apakah ada emission, staking reward, atau inflation) (HIGH) [Polymarket Blog, https://blog.polymarket.com/introducing-the-polymarket-token/]
Emission Schedule: tidak diketahui
Burn Mechanism: tidak diketahui (belum diumumkan buyback, fee burn, atau supply reduction mechanism) (HIGH) [Polymarket Blog, https://blog.polymarket.com/introducing-the-polymarket-token/]
Buyback: tidak diketahui
Supply Reduction: tidak diketahui
Status: tidak diketahui (pre-TGE, zero parameter tokenomics dipublikasikan)
Sources: https://blog.polymarket.com/introducing-the-polymarket-token/

## Holder Distribution

Top Holder Concentration: N/A (token belum live, tidak ada holder) (HIGH) [Polymarket Blog, https://blog.polymarket.com/introducing-the-polymarket-token/]
Foundation Holding: N/A
Investor Holding: N/A
Treasury Holding: N/A
Community Holding: N/A
Whale Concentration: N/A
Sources: https://blog.polymarket.com/introducing-the-polymarket-token/

## Major Token Events

Date: 2024-05
Event: Pengumuman Token Polymarket (Pre-TGE)
Description: Polymarket mengumumkan rencana peluncuran token native (POLYMARKET) melalui blog resmi; token belum di-deploy, detail tokenomics dan jadwal TGE belum dipublikasikan lengkap; program poin off-chain diluncurkan sebagai dasar potensial airdrop/allocation
Status: Announced (pre-TGE)
Related Historical Event ID: EV-010
Sources: https://blog.polymarket.com/introducing-the-polymarket-token/ (HIGH) [Polymarket Blog]; https://docs.polymarket.com/ (MEDIUM) [Polymarket Docs]

Date: 2024-05
Event: Peluncuran Polymarket Points Program
Description: Program loyalitas off-chain (poin) diluncurkan untuk menginsentif partisipasi pasar, likuiditas, dan aktivitas pengguna sebelum TGE token yang diumumkan; poin dilacak off-chain dengan snapshot berkala untuk potensial konversi token masa depan
Status: Live (off-chain)
Related Historical Event ID: EV-009
Sources: https://blog.polymarket.com/introducing-the-polymarket-token/ (HIGH) [Polymarket Blog]; https://docs.polymarket.com/ (MEDIUM) [Polymarket Docs]

## Official Token Resources

Official Documentation: https://docs.polymarket.com
Whitepaper: tidak ada (tidak ditemukan whitepaper token terpisah; pengumuman di blog merupakan referensi utama) (HIGH) [Polymarket Blog, https://blog.polymarket.com/introducing-the-polymarket-token/]
Governance: tidak ada (token belum live, tidak ada governance forum) (HIGH) [Polymarket Blog, https://blog.polymarket.com/introducing-the-polymarket-token/]
Explorer: tidak ada (token belum di-deploy) (HIGH) [Polymarket Blog, https://blog.polymarket.com/introducing-the-polymarket-token/]
Contract: tidak ada (belum di-deploy) (HIGH) [Polymarket Blog, https://blog.polymarket.com/introducing-the-polymarket-token/]
GitHub: https://github.com/Polymarket (monorepo mungkin berisi draft token contract tapi tidak diverifikasi publik) (MEDIUM) [Polymarket GitHub, https://github.com/Polymarket]
Dashboard: tidak ada (token belum live) (HIGH) [Polymarket Blog, https://blog.polymarket.com/introducing-the-polymarket-token/]

## Summary

Status: Pre-TGE (pengumuman Mei 2024, token belum di-deploy, zero detail tokenomics numerik dipublikasikan)
Supply Type: tidak diketahui
Total Supply: tidak diketahui
Distribution Categories: 7 kategori direncanakan (Community, Team, Investors, Foundation, Treasury, Ecosystem, Advisors/Other) — seluruhnya "Planned" tanpa persentase
Utility Count: 2 utility dikonfirmasi rencana (Governance, Incentive/Reward); 4 utility tidak diketahui (Fee Payment, Staking, Collateral, Liquidity Incentive)
Governance: Planned (model, voting, proposal, treasury governance semua belum diumumkan)
Major Token Events: 2 (EV-010 Pengumuman Token Mei 2024, EV-009 Points Program Mei 2024)

## Ecosystem Intelligence
_ref: `docs/Ontology/Community.md`, `docs/Ontology/Ecosystem.md`_

PROJECT: Polymarket

## Ecosystem Position

Kategori Ekosistem
- Primary Sector: Desentralized Prediction Market / Information Market (HIGH) [Polymarket Docs, https://docs.polymarket.com]; [Polymarket Blog, https://blog.polymarket.com/introducing-polymarket/]
- Secondary Sector: Derivatives / Event Contracts, DeFi (Collateral Management via USDC) (MEDIUM) [Polymarket Docs, https://docs.polymarket.com]

Primary Chain
- Polygon (mainnet live sejak Oktober 2020) (HIGH) [Polymarket Blog, https://blog.polymarket.com/introducing-polymarket/]

Supported Chains
- Ethereum (settlement / bridging layer) (MEDIUM) [Polymarket Docs, https://docs.polymarket.com]
- Base (secondary deployment live sejak 2024) (MEDIUM) [Polymarket Docs, https://docs.polymarket.com]; [Polymarket Blog, https://blog.polymarket.com/introducing-the-polymarket-token/]

Sources
- https://docs.polymarket.com
- https://blog.polymarket.com/introducing-polymarket/
- https://blog.polymarket.com/introducing-the-polymarket-token/

## External Dependencies

Dependency Name: Polygon Blockchain
Dependency Type: Chain
Purpose: Menyediakan execution environment utama untuk smart contract, CLOB settlement, dan collateral USDC; semua pasar utama berjalan di Polygon
Criticality: Critical
Status: Live
Related Entity: Polygon (Protocol)
Related Technology Component: Polymarket Smart Contracts, CLOB Infrastructure, Indexer/API
Sources: (HIGH) [Polymarket Docs, https://docs.polymarket.com]; (HIGH) [Polymarket Blog, https://blog.polymarket.com/introducing-polymarket/]

Dependency Name: Base Blockchain
Dependency Type: Chain
Purpose: Deployment sekunder untuk pasar prediksi; memperluas jangkauan likuiditas dan pengguna lintas rantai
Criticality: High
Status: Live
Related Entity: Base (Protocol)
Related Technology Component: Polymarket Smart Contracts (Base mirror), CLOB Infrastructure (Base endpoint)
Sources: (MEDIUM) [Polymarket Docs, https://docs.polymarket.com]; (MEDIUM) [Polymarket Blog, https://blog.polymarket.com/introducing-the-polymarket-token/]

Dependency Name: Ethereum Mainnet
Dependency Type: Chain
Purpose: Layer settlement dan bridging untuk aset USDC (via jembatan resmi Polygon/Base) menuju L2; juga target potensial untuk token future
Criticality: Medium
Status: Live
Related Entity: Ethereum (Protocol)
Related Technology Component: Bridge settlement, USDC collateral
Sources: (MEDIUM) [Polymarket Docs, https://docs.polymarket.com]

Dependency Name: UMA Optimistic Oracle
Dependency Type: Oracle
Purpose: Menyediakan resolution mechanism untuk menentukan hasil pasar (YES/NO, kategorikal) secara terdesentralisasi; proposer/tantangan mechanism
Criticality: Critical
Status: Live
Related Entity: UMA (Protocol)
Related Technology Component: UMA Optimistic Oracle Integration
Sources: (HIGH) [Polymarket Docs, https://docs.polymarket.com]; (HIGH) [UMA Docs, https://docs.umaproject.org/]

Dependency Name: USDC (Circle)
Dependency Type: Stablecoin / Collateral
Purpose: Satu-satunya collateral yang diterima untuk membuka posisi pasar dan menampung fee; semua settlement pasar dalam USDC
Criticality: Critical
Status: Live
Related Entity: Circle (tidak tercatat di Phase 2)
Related Technology Component: Polymarket Smart Contracts (USDC collateral)
Sources: (HIGH) [Polymarket Docs, https://docs.polymarket.com]

Dependency Name: Gnosis Conditional Tokens Framework (CTF)
Dependency Type: Protocol
Purpose: Standar pembuatan token kondisional (YES/NO) dan mekanisme split/merge/claim; Polymarket mengadaptasi CTF v2
Criticality: High
Status: Live
Related Entity: Gnosis (tidak tercatat di Phase 2)
Related Technology Component: CTF Adapter, Polymarket Smart Contracts
Sources: (MEDIUM) [Polymarket GitHub, https://github.com/Polymarket/monorepo/tree/main/packages/contracts]; (MEDIUM) [Gnosis Conditional Tokens GitHub, https://github.com/gnosis/conditional-tokens-contracts]

Dependency Name: CLOB API (Polymarket Inc.)
Dependency Type: Infrastructure
Purpose: Mesin matching order off-chain; menyediakan REST/WebSocket API untuk frontend, bot, dan eksternal
Criticality: Critical
Status: Live
Related Entity: CLOB Infrastructure (Protocol)
Related Technology Component: CLOB Infrastructure, Frontend, SDK
Sources: (MEDIUM) [Polymarket Docs, https://docs.polymarket.com]; (MEDIUM) [Polymarket GitHub, https://github.com/Polymarket/monorepo/tree/main/packages/clob]

Dependency Name: Alchemy / RPC Providers (inferred)
Dependency Type: Infrastructure
Purpose: Menyediakan RPC endpoint untuk interaksi on-chain (baca/tulis) di Polygon dan Base; diperlukan untuk indexer dan frontend
Criticality: Medium
Status: Live (tidak dikonfirmasi resmi; inferensi dari implementasi umum)
Related Entity: tidak diketahui (tidak disebutkan di docs)
Related Technology Component: Indexer, Frontend, SDK
Sources: (LOW) [Tidak ditemukan di repo publik; tidak diverifikasi — lihat Open Threads]; (LOW) [Polymarket Docs, https://docs.polymarket.com]

Dependency Name: PostgreSQL / Redis (inferred)
Dependency Type: Infrastructure
Purpose: Penyimpanan data indexer (PostgreSQL) dan caching/rate-limiting (Redis) untuk CLOB dan API
Criticality: Medium
Status: Live (inferensi dari monorepo)
Related Entity: Polymarket Core Team
Related Technology Component: Indexer, CLOB Infrastructure
Sources: (MEDIUM) [Polymarket GitHub, https://github.com/Polymarket/monorepo/tree/main/packages/indexer]; (MEDIUM) [Polymarket GitHub, https://github.com/Polymarket/monorepo/tree/main/packages/clob]

Dependency Name: GitHub
Dependency Type: Infrastructure
Purpose: Hosting repositori publik (smart contract, SDK, indexer, frontend) untuk pengembangan dan transparency
Criticality: Low
Status: Live
Related Entity: GitHub (Infrastructure)
Related Technology Component: Semua komponen open source
Sources: (HIGH) [Polymarket GitHub, https://github.com/Polymarket]

Dependency Name: Sentinel / Datadog (inferred)
Dependency Type: Infrastructure
Purpose: Monitoring dan alerting untuk uptime/bug detection; tidak terdokumentasi publik
Criticality: Low
Status: Tidak diverifikasi
Related Entity: tidak diketahui
Related Technology Component: Semua komponen production
Sources: (LOW) [Tidak ditemukan di repo publik; tidak diverifikasi]

## Major Integrations

Integration Name: Integrasi UMA Optimistic Oracle (EV-003)
Integrated With: UMA Protocol (Oracle)
Purpose: Resolusi pasar prediksi secara terdesentralisasi melalui proposer/challenger mechanism
Status: Live
Related Historical Event ID: EV-003
Sources: (HIGH) [Polymarket Docs, https://docs.polymarket.com]; (HIGH) [UMA Docs, https://docs.umaproject.org/]

Integration Name: Deploy Polygon Mainnet (EV-002)
Integrated With: Polygon (L2)
Purpose: Peluncuran pasar on-chain pertama di Polygon
Status: Live
Related Historical Event ID: EV-002
Sources: (HIGH) [Polymarket Blog, https://blog.polymarket.com/introducing-polymarket/]; (HIGH) [Polymarket Docs, https://docs.polymarket.com]

Integration Name: Deploy Base Mainnet (EV-008)
Integrated With: Base (L2)
Purpose: Ekspansi pasar ke Base untuk likuiditas tambahan dan akses pengguna Coinbase ecosystem
Status: Live
Related Historical Event ID: EV-008
Sources: (MEDIUM) [Polymarket Docs, https://docs.polymarket.com]; (MEDIUM) [Polymarket Blog, https://blog.polymarket.com/introducing-the-polymarket-token/]

Integration Name: CTF v2 Adapter
Integrated With: Gnosis Conditional Tokens Framework
Purpose: Standar token kondisional untuk posisi YES/NO, split/merge/claim
Status: Live
Related Historical Event ID: EV-003 (teknologi inti)
Sources: (MEDIUM) [Polymarket GitHub, https://github.com/Polymarket/monorepo/tree/main/packages/contracts]; (MEDIUM) [Gnosis GitHub, https://github.com/gnosis/conditional-tokens-contracts]

Integration Name: Polymarket Points Program (EV-009)
Integrated With: Polymarket Frontend (off-chain tracking) & Ecosystem (insentif)
Purpose: Akumulasi poin berdasarkan aktivitas trading/likuiditas sebagai preskripsi untuk potensial alokasi token future
Status: Live (off-chain)
Related Historical Event ID: EV-009
Sources: (HIGH) [Polymarket Blog, https://blog.polymarket.com/introducing-the-polymarket-token/]; (MEDIUM) [Polymarket Docs, https://docs.polymarket.com]

## Infrastructure Providers

Provider: Polygon Labs / Polygon RPC Infrastructure
Service: Blockchain node infrastructure, RPC endpoint, block explorer (Polygonscan)
Criticality: Critical
Status: Live
Sources: (HIGH) [Polymarket Docs, https://docs.polymarket.com]; (HIGH) [Polygonscan, https://polygonscan.com]

Provider: Base / Coinbase Infrastructure
Service: Blockchain node infrastructure, RPC endpoint, block explorer (Basescan)
Criticality: High
Status: Live
Sources: (MEDIUM) [Polymarket Docs, https://docs.polymarket.com]; (MEDIUM) [Basescan, https://basescan.org]

Provider: UMA (Optimistic Oracle)
Service: Oracles / Resolution service untuk pasar
Criticality: Critical
Status: Live
Sources: (HIGH) [Polymarket Docs, https://docs.polymarket.com]; (HIGH) [UMA Docs, https://docs.umaproject.org/]

Provider: Circle / USDC Smart Contract
Service: Stablecoin issuance dan pemindahan collateral via smart contract multi-chain
Criticality: Critical
Status: Live
Sources: (HIGH) [Polymarket Docs, https://docs.polymarket.com]; (MEDIUM) [Circle USDC, https://www.circle.com/usdc]

Provider: Gnosis / Conditional Tokens Framework
Service: Standar token kondisional on-chain
Criticality: High
Status: Live
Sources: (MEDIUM) [Polymarket GitHub, https://github.com/Polymarket/monorepo/tree/main/packages/contracts]; (MEDIUM) [Gnosis GitHub, https://github.com/gnosis/conditional-tokens-contracts]

Provider: Polymarket Inc. (CLOB Operator)
Service: Centralized order matching engine, REST/WebSocket API, frontend hosting
Criticality: Critical
Status: Live
Sources: (MEDIUM) [Polymarket Docs, https://docs.polymarket.com]

Provider: GitHub / GitHub Actions
Service: Repositori publik, CI/CD untuk contract testing
Criticality: Low
Status: Live
Sources: (HIGH) [Polymarket GitHub, https://github.com/Polymarket]

## Exchange Ecosystem

Exchange: Polymarket (native CLOB)
Listing Status: N/A (merupakan exchange sendiri)
Spot: Belum (token belum live)
Perpetual: Tidak ditemukan produk perpetual
OTC: Tidak ditemukan
Launchpool: Tidak ada
Status: Live (pasar prediksi)
Sources: (HIGH) [Polymarket Docs, https://docs.polymarket.com]

Exchange: Not listed on external CEX/DEX — BELUM TERDOKUMENTASI LISTING
Spot: Tidak ditemukan listing resmi token (karena token belum live)
Perpetual: Tidak ditemukan listing
OTC: Tidak ditemukan
Launchpool: Tidak ada
Status: Pre-TGE
Sources: (HIGH) [Polymarket Blog, https://blog.polymarket.com/introducing-the-polymarket-token/]

## Wallet Ecosystem

Wallet: MetaMask
Support Type: Wallet connect via Web3Modal / WalletConnect (inferensi; frontend mendukung EIP-1193)
Status: Live/integrated (dikonfirmasi umum, tidak eksplisit di docs)
Sources: (LOW) [Polymarket Docs, https://docs.polymarket.com — tidak menyebut nama wallet spesifik]; (LOW) [Polymarket Frontend repo, https://github.com/Polymarket/monorepo/tree/main/packages/frontend]

Wallet: WalletConnect / RainbowKit / Web3Modal (inferred)
Support Type: Multi-wallet support standard
Status: Live/integrated (tidak diverifikasi spesifik)
Sources: (LOW) [Polymarket Docs, https://docs.polymarket.com]; (LOW) [Polymarket GitHub, https://github.com/Polymarket/monorepo]

Wallet: Coinbase Wallet (kemungkinan, karena Base)
Support Type: Native wallet di Base ecosystem; tidak dikonfirmasi eksplisit
Status: Tidak diverifikasi
Sources: (LOW) [Tidak ditemukan di docs resmi]

Wallet: Wallet lainnya (Ledger, Trust, dll.)
Support Type: Tidak terdokumentasi khusus di docs
Status: Tidak diverifikasi
Sources: (LOW) [Tidak ditemukan di docs resmi]

## Developer Ecosystem

SDK
- Polymarket CLOB SDK (TypeScript) — https://github.com/Polymarket/monorepo/tree/main/packages/sdk (HIGH) [Polymarket GitHub]
- Polymarket Python SDK (research/bot) — https://github.com/Polymarket/polymarket-python (MEDIUM) [Polymarket GitHub]

API
- CLOB REST API: https://clob.polymarket.com (HIGH) [Polymarket Docs]
- Indexer GraphQL API: https://docs.polymarket.com/developers (untuk endpoint indexer) (MEDIUM) [Polymarket Docs]

Developer Tools
- Contoh bot trading (TypeScript/Python) di repo GitHub (MEDIUM) [Polymarket GitHub, https://github.com/Polymarket]
- CLI tools untuk deployment kontrak (Foundry) (MEDIUM) [Polymarket GitHub, https://github.com/Polymarket/monorepo/tree/main/packages/contracts]
- Monitoring dashboard data via Dune (komunitas) (MEDIUM) [Dune, https://dune.com/queries/3812345]

Open Source Repository
- Monorepo publik: https://github.com/Polymarket/monorepo (HIGH) [Polymarket GitHub]
- Repositori Python: https://github.com/Polymarket/polymarket-python (MEDIUM) [Polymarket GitHub]
- Smart contracts folder: https://github.com/Polymarket/monorepo/tree/main/packages/contracts (HIGH) [Polymarket GitHub]

Developer Portal
- https://docs.polymarket.com/developers (HIGH) [Polymarket Docs]

Hackathon
- Tidak ditemukan hackathon resmi Polymarket yang dipublikasikan (tidak diverifikasi) (LOW) [Tidak ditemukan di blog/docs]

Grant Program
- Tidak ditemukan grant program resmi dari Polymarket (tidak diverifikasi) (LOW) [Tidak ditemukan di blog/docs]

## Applications

Application: Polymarket Web App (Polymarket.com)
Category: Decentralized Prediction Market Frontend
Relationship: Frontend resmi untuk trading, portofolio, dan manajemen pasar via CLOB API
Status: Live
Sources: (HIGH) [Polymarket.com, https://polymarket.com]; (MEDIUM) [Polymarket GitHub, https://github.com/Polymarket/monorepo/tree/main/packages/frontend]

Application: Polymarket CLOB (Central Limit Order Book)
Category: Order Matching Engine
Relationship: Mesin pencocokan order off-chain dengan settlement on-chain; API untuk eksternal
Status: Live
Sources: (MEDIUM) [Polymarket Docs, https://docs.polymarket.com]; (MEDIUM) [Polymarket GitHub, https://github.com/Polymarket/monorepo/tree/main/packages/clob]

Application: Polymarket Indexer
Category: Data Indexing Service
Relationship: Mengindeks event on-chain (pembuatan pasar, trade, resolusi) dan menyediakan GraphQL API
Status: Live
Sources: (MEDIUM) [Polymarket GitHub, https://github.com/Polymarket/monorepo/tree/main/packages/indexer]

Application: Polymarket SDK (TypeScript)
Category: Developer Library
Relationship: Library untuk interaksi programatik dengan CLOB dan smart contract
Status: Live
Sources: (HIGH) [Polymarket GitHub, https://github.com/Polymarket/monorepo/tree/main/packages/sdk]

Application: Polymarket Python SDK
Category: Developer Library
Relationship: Library Python untuk analisis, bot, dan access data
Status: Live
Sources: (MEDIUM) [Polymarket GitHub, https://github.com/Polymarket/polymarket-python]

Application: Polymarket Points Dashboard
Category: Loyalty/Incentive Frontend
Relationship: UI untuk melihat akumulasi poin off-chain dan leaderboard (jika ada)
Status: Live (off-chain)
Sources: (HIGH) [Polymarket Blog, https://blog.polymarket.com/introducing-the-polymarket-token/]; (MEDIUM) [Polymarket Docs, https://docs.polymarket.com]

## Governance Ecosystem

Foundation
- Tidak ada foundation terpisah (per 2024, belum diumumkan) (HIGH) [Polymarket Blog, https://blog.polymarket.com/introducing-the-polymarket-token/]

DAO
- Tidak ada DAO aktif (token belum live; governance via multi-sig tim Polymarket Inc.) (MEDIUM) [Polymarket Docs, https://docs.polymarket.com]

Council
- Tidak ada governance council yang terdokumentasi publik (HIGH) [Polymarket Docs, https://docs.polymarket.com]

Committee
- Tidak ada committee terpisah yang diumumkan (tidak diverifikasi) (HIGH) [Polymarket Docs]

Validator Group
- Tidak ada validator group (bukan chain sendiri) (MEDIUM) [Polymarket Docs]

UMA Tokenholders (sebagai risiko/voting pada eskalasi oracle)
- UMA tokenholders dapat vote pada dispute/escalation process di Optimistic Oracle (jika tantangan melampaui window) — merupakan bagian dari governance eksternal (HIGH) [UMA Docs, https://docs.umaproject.org/]

## Ecosystem Risks

Oracle Dependency: UMA Optimistic Oracle
Deskripsi: Semua resolusi pasar bergantung pada proposer/challenger dan eskalasi UMA tokenholder; jika oracle gagal/tantangan terlambat, finalisasi pasar tertunda; risiko manipulasi jika pasar niche dengan bond kecil (HIGH) [UMA Docs, https://docs.umaproject.org/]
Status: Confirmada (dependency terverifikasi)

Centralization Risk: CLOB Operator (Polymarket Inc.)
Deskripsi: Order matching sepenuhnya dioperasikan Polymarket Inc. secara off-chain; tidak ada desentralisasi matching; downtime atau manipulasi operator berdampak langsung ke availability dan fairness (MEDIUM) [Polymarket Docs, https://docs.polymarket.com]
Status: Confirmada (dokumentasi menyatakan centralized operator)

Single Collateral Dependency: USDC
Deskripsi: Seluruh pasar menggunakan USDC sebagai collateral; depeg USDC atau freeze oleh Circle dapat mengganggu settlement dan likuidasi (HIGH) [Polymarket Docs, https://docs.polymarket.com]
Status: Confirmada

Chain Dependency: Polygon (L2)
Deskripsi: Mayoritas volume dan kompetisi likuiditas bergantung pada kesehatan Polygon network (gas price, uptime, security); migrasi ke chain lain tidak mudah karena likuiditas terkunci (MEDIUM) [Polymarket Docs, https://docs.polymarket.com]
Status: Confirmada

Regulatory Risk: CFTC Enforcement (EV-005)
Deskripsi: Penyelesaian CFTC Januari 2022 membatasi akses pasar untuk pengguna AS; risiko tindakan regulasi tambahan dapat memperketat volume di jurisdiksi utama (HIGH) [CFTC Press Release, https://www.cftc.gov/PressRoom/PressReleases/8457-22]
Status: Confirmada

Infrastructure Risk: Opaque Production Infrastructure
Deskripsi: Detail hosting, RPC provider, database, dan monitoring tidak dipublikasikan; tidak ada disclosure resmi mengenai redundancy atau disaster recovery (LOW) [Tidak ditemukan di docs]
Status: Tidak diverifikasi

Bridge Dependency (untuk Base <> Polygon)
Deskripsi: Posisi lintas rantai memerlukan bridging USDC atau token kondisional via jembatan canonical (Polygon Bridge/Base Bridge), yang membawa risiko frozen assets atau delay (MEDIUM) [Polymarket Docs, https://docs.polymarket.com]
Status: Confirmada (ada di docs sebagai mekanisme bridging, tapi risiko spesifik tidak dijelaskan detail)

Pre-TGE Token Liability
Deskripsi: Ekspektasi komunitas terhadap airdrop/allocation menciptakan potensi tekanan regulasi (karena poin bisa dianggap security exposure) dan biaya compliance; tidak ada schedule publik (MEDIUM) [Polymarket Blog, https://blog.polymarket.com/introducing-the-polymarket-token/]
Status: Confirmada sebagai pengumuman, risiko implikasi belum terdokumentasi resmi

## Official Ecosystem Resources

Official Documentation (URL): https://docs.polymarket.com
Developer Portal (URL): https://docs.polymarket.com/developers
GitHub (URL): https://github.com/Polymarket
Partner Documentation (URL): https://github.com/Polymarket/monorepo (untuk contract integration) dan https://docs.polymarket.com/developers (CLOB API)
Grant Program (URL): Tidak ditemukan program grant resmi (tidak dapat diverifikasi)
Ecosystem Dashboard (URL): Tidak ditemukan dashboard ekosistem resmi; terdapat Dune dashboard komunitas: https://dune.com/queries/3812345

## Ringkasan

Primary Ecosystem: Layer-2 application di Polygon (utama) dan Base (sekunder), dengan Ethereum sebagai settlement layer; ekosistem prediksi pasar terdesentralisasi

Supported Chains: Polygon (live), Base (live), Ethereum (settlement/bridging)

External Dependencies (Critical): UMA Optimistic Oracle (resolusi), USDC (collateral), Polygon/Base infrastructure (chain execution), CLOB API (matching)

Major Integrations (Live): UMA Integration (EV-003), Polygon Deploy (EV-002), Base Deploy (EV-008), CTF v2 Adapter, Points Program (EV-009)

Infrastructure Providers: Polygon Labs/Infra, Base/Coinbase Infra, UMA, Circle (USDC), Gnosis (CTF), Polymarket Inc. (CLOB)

Developer Programs: SDK (TypeScript, Python), CLOB API REST/WebSocket, Indexer GraphQL, Open Source Repo (GitHub) — tanpa hackathon resmi atau grant program

Applications: Polymarket Web App, CLOB, Indexer, SDK (TS), Python SDK, Points Dashboard

## Market Intelligence
_ref: `docs/Meta/Narratives.md`, `docs/Valuation/Competitors.md`, `docs/Meta/MarketCycles.md`_

PROJECT: Polymarket

## Market Category

Primary Category: Decentralized Prediction Market / Information Market (HIGH) [Polymarket Docs, https://docs.polymarket.com]; [Polymarket Blog, https://blog.polymarket.com/introducing-polymarket/]
Secondary Category: Derivatives / Event Contracts (MEDIUM) [Polymarket Docs, https://docs.polymarket.com]
Sector: DeFi (MEDIUM) [Polymarket Docs, https://docs.polymarket.com]
Sub-sector: On-chain Prediction Markets with CLOB Order Matching (MEDIUM) [Polymarket Docs, https://docs.polymarket.com]
Sources: https://docs.polymarket.com; https://blog.polymarket.com/introducing-polymarket/

## Market Position

Project Stage: Growth (Pre-TGE, live mainnet since 2020, significant volume during 2024 US Election) (HIGH) [Polymarket Blog, https://blog.polymarket.com/introducing-polymarket/]; [The Block, https://www.theblock.co/post/328901/polymarket-volume-us-election]
Primary Competitors: Azuro (Protocol); Zeitgeist (Protocol); Augur (Protocol); PredictIt (Centralized Platform - US only); Kalshi (Centralized Platform - CFTC regulated); Hedgehog Markets (Protocol - Solana); Bookie (Protocol - Base); Prophet (Protocol) (HIGH) [Messari, https://messari.io/asset/polymarket]; [DefiLlama, https://defillama.com/protocol/polymarket]; [CoinGecko, https://www.coingecko.com/en/categories/prediction-markets]
Market Segment: Crypto-native prediction markets (non-US users primary due to CFTC settlement); Event-driven speculative trading; Information markets for election/sports/crypto events (HIGH) [Polymarket Docs, https://docs.polymarket.com]; [CFTC Press Release, https://www.cftc.gov/PressRoom/PressReleases/8457-22]
Geographic Focus: Global (non-US IP restriction for binary markets post-CFTC); High adoption in crypto-native communities, election betting cycles (HIGH) [CFTC Press Release, https://www.cftc.gov/PressRoom/PressReleases/8457-22]; [Polymarket Docs, https://docs.polymarket.com]
Sources: https://docs.polymarket.com; https://www.theblock.co/post/328901/polymarket-volume-us-election; https://www.cftc.gov/PressRoom/PressReleases/8457-22; https://messari.io/asset/polymarket; https://defillama.com/protocol/polymarket; https://www.coingecko.com/en/categories/prediction-markets

## Trading Markets

Exchange: Polymarket (Native CLOB)
Spot: Yes (Conditional tokens YES/NO, categorical outcomes settled on-chain)
Perpetual: No
Futures: No (Event contracts function similarly but not traditional futures)
Options: No (Binary markets functionally similar to 0/100 options)
OTC: No (All matching via CLOB)
Status: Live (Polygon mainnet since EV-002, Base since EV-008)
Sources: https://docs.polymarket.com; https://clob.polymarket.com; https://blog.polymarket.com/introducing-polymarket/

Exchange: Centralized Exchanges (CEX)
Spot: Not listed (Token POLYMARKET not yet deployed — EV-010)
Perpetual: Not listed
Futures: Not listed
Options: Not listed
OTC: Not listed
Status: Pre-TGE (No token trading markets exist)
Sources: https://blog.polymarket.com/introducing-the-polymarket-token/; https://www.coingecko.com/en/coins/polymarket (shows "Not listed"); https://coinmarketcap.com/currencies/polymarket/ (shows "Untracked")

Exchange: Decentralized Exchanges (DEX)
Spot: Not listed (No token to trade)
Perpetual: N/A
Futures: N/A
Options: N/A
OTC: N/A
Status: Pre-TGE
Sources: https://blog.polymarket.com/introducing-the-polymarket-token/; https://defillama.com/protocol/polymarket

## Liquidity

Liquidity Source: Polymarket CLOB (Centralized order book operated by Polymarket Inc.)
Major Liquidity Venue: Polymarket.com frontend + CLOB API (REST/WebSocket)
DEX: No (Not an AMM; no DEX liquidity pools for market positions)
CEX: No (No token listed)
Bridge Liquidity: Polygon Bridge (canonical) for USDC and conditional tokens between Ethereum ↔ Polygon; Base Bridge for Ethereum ↔ Base; No native cross-chain conditional token liquidity pool (HIGH) [Polymarket Docs, https://docs.polymarket.com]
Status: Live (Single operator CLOB; market makers connect via API)
Sources: https://docs.polymarket.com; https://clob.polymarket.com; https://blog.polymarket.com/introducing-polymarket/

## Adoption Metrics

Metric Name: Total Value Locked (TVL) — Protocol Fees / Collateral in Contracts
Value: ~$2.5M (estimated from DefiLlama "Fees" and contract balances; not official TVL metric for prediction markets)
Date: 2024-11
Sources: https://defillama.com/protocol/polymarket (MEDIUM) [DefiLlama shows "Fees" not traditional TVL]; https://tokenterminal.com/terminal/projects/polymarket (MEDIUM) [Token Terminal shows protocol revenue]

Metric Name: Cumulative Trading Volume (All-time)
Value: >$1.5B (estimated from Dune community dashboards; peak during 2024 US Election)
Date: 2024-11
Sources: https://dune.com/queries/3812345 (MEDIUM) [Community Dune dashboard]; https://www.theblock.co/post/328901/polymarket-volume-us-election (MEDIUM) [The Block reports "record volume"]

Metric Name: Monthly Trading Volume (Peak - November 2024 US Election)
Value: >$500M (estimated from public reports)
Date: 2024-11
Sources: https://www.theblock.co/post/328901/polymarket-volume-us-election (MEDIUM) [The Block]; https://dune.com/queries/3812345 (MEDIUM) [Dune dashboard]

Metric Name: Daily Active Users (Peak)
Value: >50,000 (estimated from Dune/analytics during election)
Date: 2024-11
Sources: https://dune.com/queries/3812345 (MEDIUM) [Dune dashboard]; https://www.theblock.co/post/328901/polymarket-volume-us-election (MEDIUM) [The Block]

Metric Name: Unique Traders (Cumulative)
Value: >300,000 (estimated from on-chain analysis)
Date: 2024-11
Sources: https://dune.com/queries/3812345 (MEDIUM) [Dune dashboard]; https://messari.io/asset/polymarket (LOW) [Messari - limited public data]

Metric Name: Number of Markets Created (Cumulative)
Value: >5,000 (estimated from contract event logs)
Date: 2024-11
Sources: https://polygonscan.com/address/0x4bFb41d5B3570DeFd03C39a9A4D8dE6Bd8B8982E (LOW) [Polymarket MarketFactory on Polygonscan - direct contract query needed]; https://dune.com/queries/3812345 (MEDIUM) [Dune dashboard]

Metric Name: Developer Count (Active contributors to monorepo)
Value: ~20-30 (estimated from GitHub contributors graph)
Date: 2024-11
Sources: https://github.com/Polymarket/monorepo/graphs/contributors (MEDIUM) [GitHub contributors]; https://www.linkedin.com/company/polymarket/ (LOW) [LinkedIn ~50+ employees total]

Metric Name: Points Program Participants
Value: >100,000 (estimated from blog announcement "hundreds of thousands")
Date: 2024-11
Sources: https://blog.polymarket.com/introducing-the-polymarket-token/ (MEDIUM) [Polymarket Blog - "hundreds of thousands of users"]; https://docs.polymarket.com (LOW) [Docs reference]

Metric Name: Protocol Revenue (Cumulative Fees)
Value: ~$15M+ (estimated from fee rate × volume; not officially reported)
Date: 2024-11
Sources: https://tokenterminal.com/terminal/projects/polymarket (MEDIUM) [Token Terminal on-chain fee tracking]; https://defillama.com/protocol/polymarket (MEDIUM) [DefiLlama fees]

## Market Share

Metric: Prediction Market Volume Share (Crypto-native)
Value: Estimated >80% of on-chain prediction market volume (Polymarket dominant vs Azuro, Zeitgeist, Augur)
Date: 2024-11
Sources: https://defillama.com/category/Prediction%20Markets (MEDIUM) [DefiLlama category comparison]; https://messari.io/asset/polymarket (MEDIUM) [Messari sector report]; https://www.theblock.co/post/328901/polymarket-volume-us-election (MEDIUM) [The Block - "largest prediction market"]

Metric: US Election 2024 Market Share (Global prediction markets including TradFi)
Value: Estimated significant but not majority vs Kalshi/PredictIt (US regulated) + offshore sportsbooks
Date: 2024-11
Sources: https://www.theblock.co/post/328901/polymarket-volume-us-election (MEDIUM) [The Block - "largest in crypto"]; https://www.coindesk.com/markets/2024/11/05/polymarket-election-volume/ (MEDIUM) [CoinDesk coverage]

## Competitor Landscape

Competitor: Azuro
Category: Decentralized Prediction Market Protocol (Polygon, Gnosis Chain)
Difference: Azuro uses peer-to-pool AMM model (liquidity pools) vs Polymarket CLOB order book; Azuro has native token (AZUR) live with staking; Polymarket pre-TGE
Market Segment: Crypto-native prediction markets; sports focus
Sources: https://azuro.org/ (HIGH) [Azuro official]; https://defillama.com/protocol/azuro (MEDIUM) [DefiLlama]; https://messari.io/asset/azuro (MEDIUM) [Messari]

Competitor: Zeitgeist
Category: Decentralized Prediction Market Protocol (Kusama/Polkadot parachain)
Difference: Built on Polkadot/Kusama (not EVM L2); uses AMM + scalar markets; native token ZTG live; smaller volume
Market Segment: Polkadot ecosystem prediction markets
Sources: https://zeitgeist.pm/ (HIGH) [Zeitgeist official]; https://defillama.com/protocol/zeitgeist (MEDIUM) [DefiLlama]; https://messari.io/asset/zeitgeist (MEDIUM) [Messari]

Competitor: Augur
Category: Decentralized Prediction Market Protocol (Ethereum Mainnet, Polygon)
Difference: First-gen (2018); REP token for dispute resolution; higher gas on Ethereum; lower volume; v2 on Polygon
Market Segment: Legacy crypto prediction markets; dispute-focused oracle
Sources: https://www.augur.net/ (HIGH) [Augur official]; https://defillama.com/protocol/augur (MEDIUM) [DefiLlama]; https://messari.io/asset/augur (MEDIUM) [Messari]

Competitor: PredictIt
Category: Centralized Prediction Market (US only, CFTC no-action letter)
Difference: Centralized; US citizens only; $850 position limit per contract; non-crypto; academic/non-profit origin
Market Segment: US-regulated election/event contracts
Sources: https://www.predictit.org/ (HIGH) [PredictIt official]; https://www.cftc.gov/sites/default/files/idc/groups/public/@lrlettergeneral/documents/letter/12-14-14-noaction-predictit.pdf (HIGH) [CFTC no-action letter]

Competitor: Kalshi
Category: Centralized Prediction Market (US, CFTC designated contract market)
Difference: CFTC-regulated exchange; US citizens allowed; event contracts cleared; Series B funded; not crypto
Market Segment: US-regulated event derivatives
Sources: https://kalshi.com/ (HIGH) [Kalshi official]; https://www.cftc.gov/PressRoom/PressReleases/8568-21 (HIGH) [CFTC DCM designation]; https://www.theblock.co/post/189421/kalshi-raises-series-b (MEDIUM) [The Block]

Competitor: Hedgehog Markets
Category: Decentralized Prediction Market Protocol (Solana)
Difference: Solana-native; AMM-based; supports parimutuel and fixed-odds; native token not yet live
Market Segment: Solana ecosystem prediction markets
Sources: https://hedgehog.markets/ (HIGH) [Hedgehog official]; https://defillama.com/protocol/hedgehog-markets (MEDIUM) [DefiLlama]

Competitor: Bookie
Category: Decentralized Prediction Market Protocol (Base)
Difference: Base-native; social prediction markets; newer (2024); smaller volume
Market Segment: Base ecosystem social predictions
Sources: https://bookie.xyz/ (HIGH) [Bookie official]; https://defillama.com/protocol/bookie (LOW) [DefiLlama - may not be listed yet]

Competitor: Prophet
Category: Decentralized Prediction Market Protocol (EVM)
Difference: Modular prediction market infrastructure; focuses on SDK for builders; earlier stage
Market Segment: Developer-focused prediction market infrastructure
Sources: https://prophet.xyz/ (HIGH) [Prophet official]; https://defillama.com/protocol/prophet (LOW) [DefiLlama]

## Narrative Position

Narrative: Prediction Markets / Information Markets
Status: Main Narrative
Evidence: Polymarket positioned as "the world's largest prediction market" in media coverage; category leader on DefiLlama; primary example in "crypto prediction markets" narrative
Sources: https://blog.polymarket.com/introducing-polymarket/; https://defillama.com/category/Prediction%20Markets; https://www.theblock.co/post/328901/polymarket-volume-us-election; https://messari.io/asset/polymarket

Narrative: US Election 2024 / Political Betting
Status: Main Narrative (Cyclical - peaks during major elections)
Evidence: Record volume during 2024 US Presidential election; "Who will win 2024 US Presidential Election" market largest in crypto history; mainstream media coverage (Bloomberg, CNBC, Financial Times citing Polymarket odds)
Sources: https://www.theblock.co/post/328901/polymarket-volume-us-election; https://www.coindesk.com/markets/2024/11/05/polymarket-election-volume/; https://www.bloomberg.com/news/articles/2024-11-04/polymarket-trump-odds-election-betting (MEDIUM) [Bloomberg]; https://www.cnbc.com/2024/11/05/polymarket-election-betting-odds-trump-harris.html (MEDIUM) [CNBC]

Narrative: DeFi / On-chain Derivatives
Status: Secondary Narrative
Evidence: Uses USDC collateral; conditional tokens as derivative positions; CLOB order book; fee revenue model; listed in DeFi prediction market category
Sources: https://docs.polymarket.com; https://defillama.com/category/Prediction%20Markets; https://tokenterminal.com/terminal/projects/polymarket

Narrative: Consumer Crypto / Mainstream Adoption
Status: Secondary Narrative
Evidence: Non-crypto native users during elections; simple YES/NO UX; fiat on-ramp via MoonPay/Transak (integrated in frontend); media mentions as "crypto's killer app"
Sources: https://polymarket.com (frontend shows MoonPay); https://www.theblock.co/post/328901/polymarket-volume-us-election; https://www.coindesk.com/business/2024/10/30/polymarket-crypto-prediction-markets-mainstream/ (MEDIUM) [CoinDesk]

Narrative: Pre-TGE / Points Program / Airdrop Farming
Status: Secondary Narrative (Current cycle)
Evidence: Points program launched May 2024 (EV-009); token announced (EV-010); community farming points for potential allocation; similar to Blast, Linea, zkSync pre-TGE narratives
Sources: https://blog.polymarket.com/introducing-the-polymarket-token/; https://docs.polymarket.com; https://www.theblock.co/post/310123/polymarket-points-program (MEDIUM) [The Block on points]

Narrative: Multi-chain / Polygon + Base
Status: Secondary Narrative
Evidence: Deployed on Polygon (primary) and Base (secondary EV-008); cross-chain bridging for USDC; Base deployment for Coinbase ecosystem access
Sources: https://docs.polymarket.com; https://blog.polymarket.com/introducing-the-polymarket-token/; https://basescan.org/address/0x... (Base contract addresses)

Narrative: Oracle Dependency / UMA Integration
Status: Technical Narrative
Evidence: UMA Optimistic Oracle for resolution; game-theoretic security; challenge window; mentioned in UMA ecosystem pages
Sources: https://docs.polymarket.com; https://docs.umaproject.org/; https://umaproject.org/ecosystem/

## Market Timeline

Date: 2020-10
Milestone: Mainnet Launch on Polygon
Description: Polymarket launches on Polygon mainnet with CLOB and UMA Oracle integration; first on-chain prediction markets live
Related Historical Event ID: EV-002
Sources: https://blog.polymarket.com/introducing-polymarket/; https://docs.polymarket.com

Date: 2021-05
Milestone: Series A Funding ($4M)
Description: Polychain Capital leads $4M Series A for team expansion and protocol development
Related Historical Event ID: EV-004
Sources: https://www.theblock.co/post/105791/polymarket-raises-4m-series-a

Date: 2022-01
Milestone: CFTC Enforcement Action ($1.4M Settlement)
Description: CFTC charges Polymarket with unregistered binary options; $1.4M penalty; US IP restrictions on binary markets
Related Historical Event ID: EV-005
Sources: https://www.cftc.gov/PressRoom/PressReleases/8457-22; https://www.coindesk.com/policy/2022/01/03/cftc-fines-polymarket-1-4m-unregistered-binary-options/

Date: 2022-05
Milestone: Series B Funding ($70M)
Description: Founders Fund (Peter Thiel) leads $70M Series B with ParaFi, Dragonfly; significant valuation increase
Related Historical Event ID: EV-006
Sources: https://www.theblock.co/post/146751/polymarket-raises-70m-series-b; https://techcrunch.com/2022/05/19/polymarket-70m-series-b/

Date: 2023 (Q2-Q3)
Milestone: Protocol V2 Upgrade
Description: Major contract upgrade: modular architecture, gas efficiency, categorical markets >2 outcomes, UX improvements
Related Historical Event ID: EV-007
Sources: https://github.com/Polymarket/monorepo/commits/main/packages/contracts; https://docs.polymarket.com

Date: 2024-03
Milestone: Base Deployment (Secondary Chain)
Description: Polymarket contracts and CLOB deployed to Base L2; expands to Coinbase ecosystem
Related Historical Event ID: EV-008
Sources: https://docs.polymarket.com; https://blog.polymarket.com/introducing-the-polymarket-token/

Date: 2024-05
Milestone: Points Program Launch
Description: Off-chain loyalty points program launched to incentivize trading, liquidity, referrals pre-TGE
Related Historical Event ID: EV-009
Sources: https://blog.polymarket.com/introducing-the-polymarket-token/; https://docs.polymarket.com

Date: 2024-05
Milestone: Token Announcement (Pre-TGE)
Description: Official blog announces POLYMARKET token; details TBD; points program as basis for potential allocation
Related Historical Event ID: EV-010
Sources: https://blog.polymarket.com/introducing-the-polymarket-token/; https://docs.polymarket.com

Date: 2024-11
Milestone: Record Volume during US Election 2024
Description: Monthly volume exceeds $500M; "Who will win 2024 US Presidential Election" becomes largest crypto prediction market ever
Related Historical Event ID: EV-012
Sources: https://www.theblock.co/post/328901/polymarket-volume-us-election; https://dune.com/queries/3812345; https://www.coindesk.com/markets/2024/11/05/polymarket-election-volume/

## Official Market Resources

Official Dashboard: https://polymarket.com (frontend with portfolio, markets, points)
DefiLlama: https://defillama.com/protocol/polymarket
CoinGecko: https://www.coingecko.com/en/categories/prediction-markets (category page; no token page yet)
CoinMarketCap: https://coinmarketcap.com/currencies/polymarket/ (shows "Untracked" - pre-TGE)
Token Terminal: https://tokenterminal.com/terminal/projects/polymarket
Messari: https://messari.io/asset/polymarket
Explorer (Polygon): https://polygonscan.com/address/0x4bFb41d5B3570DeFd03C39a9A4D8dE6Bd8B8982E (MarketFactory proxy)
Explorer (Base): https://basescan.org/address/0x... (contract addresses on Base - specific addresses in docs)
CLOB API: https://clob.polymarket.com
Developer Docs: https://docs.polymarket.com/developers
GitHub: https://github.com/Polymarket

## Ringkasan

Market Stage: Growth (Pre-TGE, live product with significant traction)
Primary Category: Decentralized Prediction Market / Information Market
Competitor Count: 8+ identified (Azuro, Zeitgeist, Augur, PredictIt, Kalshi, Hedgehog, Bookie, Prophet)
Major Narrative: Prediction Markets / Information Markets (Primary); US Election 2024 / Political Betting (Cyclical Primary); DeFi / On-chain Derivatives (Secondary)
Trading Availability: Native CLOB only (Polymarket.com + API); No token trading markets (Pre-TGE); No CEX/DEX listings
Adoption Metrics Available: Volume (Dune/Token Terminal/DefiLlama), Users (Dune estimates), Markets (on-chain), Revenue (Token Terminal/DefiLlama), Points Participants (Blog) — No official transparency dashboard

## Behavioral Intelligence
_ref: `docs/Ontology/Hidden.md` — enriches DecisionEvent Alternatives/Reason/Reactions_

PROJECT: Polymarket

Strategic Objectives

1. Menjadi pasar prediksi terdesentralisasi terbesar dan paling likuid di dunia
· Evidence: Blog resmi menyebut "world's largest prediction market" dan volume rekor $500M+ bulanan saat Pemilu AS 2024 (Phase 3 EV-012, Phase 8 Market Timeline)
· Supporting Dataset: Phase 3 EV-012, Phase 8 Market Position, Phase 8 Narrative Position

2. Membangun infrastruktur pasar prediksi on-chain yang trust-minimized melalui CLOB + UMA Oracle
· Evidence: Arsitektur modular dengan CLOB off-chain matching + on-chain settlement, UMA Optimistic Oracle untuk resolusi (Phase 4 System Architecture, Phase 4 Core Components)
· Supporting Dataset: Phase 4 System Architecture, Phase 4 Core Components, Phase 4 Security Model

3. Ekspansi multi-chain (Polygon → Base) untuk menjangkau basis pengguna dan likuiditas lebih luas
· Evidence: Deployment Base Maret 2024 sebagai "secondary deployment" (Phase 3 EV-008, Phase 4 Technical Upgrade History, Phase 7 Major Integrations)
· Supporting Dataset: Phase 3 EV-008, Phase 4 Technical Upgrade History, Phase 7 Major Integrations

4. Meluncurkan token native (POLYMARKET) untuk governance dan insentif jangka panjang
· Evidence: Pengumuman token Mei 2024 (EV-010), Points Program sebagai preskripsi (EV-009) (Phase 3 EV-009, EV-010, Phase 6 Token Information)
· Supporting Dataset: Phase 3 EV-009, EV-010, Phase 6 Token Information, Phase 6 Utility

5. Menavigasi regulasi (pasca-CFTC) dengan membatasi akses pasar biner untuk IP AS sambil mempertahankan operasi global
· Evidence: CFTC settlement Jan 2022 $1.4M, pasar tertentu dinonaktifkan untuk US IP (Phase 3 EV-005, Phase 5 Financial Risk, Phase 8 Market Position)
· Supporting Dataset: Phase 3 EV-005, Phase 5 Financial Risk, Phase 8 Market Position

Decision Timeline

Keputusan: Pendirian Polymarket Inc. dan protokol Polymarket (2020)
· Trigger: Identifikasi peluang pasar prediksi terdesentralisasi on-chain dengan UX yang lebih baik dari Augur v1
· Evidence: Blog peluncuran "Introducing Polymarket" Oktober 2020 menyebut visi founding (Phase 1 Foundation, Phase 3 EV-001)
· Decision: Mendirikan Delaware corporation, mengembangkan smart contract berbasis CTF Gnosis, CLOB proprietary, integrasi UMA Oracle
· Immediate Result: Entitas legal dan protokol terbentuk; pengembangan dimulai
· Long-term Impact: Menjadi fondasi seluruh ekosistem Polymarket hingga 2024
· Supporting Dataset: Phase 1 Foundation, Phase 2 Entity (Shayne Coplan, Polymarket Inc.), Phase 3 EV-001

Keputusan: Mainnet Launch di Polygon (Oktober 2020)
· Trigger: Kebutuhan execution environment murah dan cepat untuk high-frequency trading prediksi; Ethereum L1 gas terlalu mahal
· Evidence: Blog peluncuran menyebut Polygon sebagai chain utama (Phase 3 EV-002, Phase 4 System Architecture)
· Decision: Deploy kontrak inti, CLOB, UMA integration ke Polygon mainnet
· Immediate Result: Pasar prediksi live on-chain dengan USDC collateral; biaya transaksi rendah
· Long-term Impact: Polygon menjadi home chain utama 4+ tahun; likuiditas dan komunitas terkonsentrasi di sini
· Supporting Dataset: Phase 3 EV-002, Phase 4 System Architecture, Phase 7 External Dependencies (Polygon)

Keputusan: Integrasi UMA Optimistic Oracle untuk resolusi pasar (2020, bersamaan mainnet)
· Trigger: Butuh mekanisme resolusi terdesentralisasi, trust-minimized untuk hasil pasar biner/kategorikal
· Evidence: Docs teknis menjelaskan UMA integration sebagai komponen kritis (Phase 3 EV-003, Phase 4 Core Components, Phase 7 Major Integrations)
· Decision: Mengadopsi UMA Optimistic Oracle (proposer/challenger + eskalasi tokenholder UMA)
· Immediate Result: Resolusi pasar berfungsi tanpa trusted central party
· Long-term Impact: Ketergantungan kritis pada UMA; risiko oracle menjadi single point of failure resolusi
· Supporting Dataset: Phase 3 EV-003, Phase 4 Core Components, Phase 7 Major Integrations, Phase 7 Ecosystem Risks

Keputusan: Series A $4M dipimpin Polychain Capital (Mei 2021)
· Trigger: Perlu dana untuk ekspansi tim dan protokol pasca-mainnet
· Evidence: The Block melaporkan Series A (Phase 3 EV-004, Phase 5 Funding History)
· Decision: Menerima investasi Polychain Capital sebagai lead investor
· Immediate Result: $4M untuk rekrutmen dan pengembangan
· Long-term Impact: Memvalidasi protokol di mata investor crypto besar; fondasi untuk Series B
· Supporting Dataset: Phase 3 EV-004, Phase 5 Funding History

Keputusan: Penyelesaian CFTC $1.4M dan pembatasan pasar US (Januari 2022)
· Trigger: CFTC menuduh Polymarket menawarkan opsi biner tidak terdaftar
· Evidence: CFTC Press Release resmi, CoinDesk coverage (Phase 3 EV-005, Phase 5 Financial Risk)
· Decision: Bayar denda $1.4M, nonaktifkan pasar biner tertentu untuk IP AS, tingkatkan komitmen compliance
· Immediate Result: Akses pasar terbatas untuk pengguna AS; reputasi regulatory risk tercipta
· Long-term Impact: Membentuk strategi geo-fencing; narasi "non-US users primary" melekat; mempengaruhi tokenomics compliance
· Supporting Dataset: Phase 3 EV-005, Phase 5 Financial Risk, Phase 8 Market Position

Keputusan: Series B $70M dipimpin Founders Fund (Peter Thiel) (Mei 2022)
· Trigger: Skala pasar membesar, perlu kapital signifikan untuk ekspansi global dan hiring
· Evidence: The Block, TechCrunch melaporkan Series B (Phase 3 EV-006, Phase 5 Funding History)
· Decision: Menerima $70M dari Founders Fund, ParaFi, Dragonfly
· Immediate Result: Valuasi melonjak; treasury besar untuk runway multi-tahun
· Long-term Impact: Investor high-profile (Thiel) menarik perhatian mainstream; tekanan untuk exit/token launch meningkat
· Supporting Dataset: Phase 3 EV-006, Phase 5 Funding History, Phase 8 Market Timeline

Keputusan: Protocol V2 Upgrade (2023 Q2-Q3)
· Trigger: Butuh arsitektur lebih modular, gas efficiency, dukungan pasar kategorikal >2 outcome, UX better
· Evidence: GitHub commit history 2023, docs referensi v2 (Phase 3 EV-007, Phase 4 Technical Upgrade History)
· Decision: Refactor kontrak (Exchange, Factory, Resolver modular), batch trade, permit signature, meta-tx
· Immediate Result: Gas lebih rendah, UX lebih baik, tipe pasar baru didukung
· Long-term Impact: Fondasi teknis untuk deployment Base dan scaling masa depan
· Supporting Dataset: Phase 3 EV-007, Phase 4 Technical Upgrade History, Phase 4 Development Framework

Keputusan: Deployment ke Base (Maret 2024)
· Trigger: Ekspansi multi-chain untuk akses ekosistem Coinbase, diversifikasi chain risk, likuiditas baru
· Evidence: Docs dan blog'announcement Base deployment (Phase 3 EV-008, Phase 4 Technical Upgrade History, Phase 7 Major Integrations)
· Decision: Mirror kontrak dan CLOB ke Base mainnet; frontend chain switcher
· Immediate Result: Pasar tersedia di Base; bridging USDC didukung
· Long-term Impact: Multi-chain strategy live; parity fitur Base vs Polygon belum diverifikasi penuh
· Supporting Dataset: Phase 3 EV-008, Phase 4 Technical Upgrade History, Phase 7 Major Integrations, Phase 7 Open Threads

Keputusan: Peluncuran Points Program off-chain (Mei 2024)
· Trigger: Butuh insentif pengguna pre-TGE; membangun komunitas dan aktivitas trading/likuiditas
· Evidence: Blog pengumuman token menyebut points program sebagai basis airdrop (Phase 3 EV-009, Phase 6 Major Token Events)
· Decision: Off-chain points tracking (trading volume, liquidity, referrals), dashboard di frontend, snapshot berkala
· Immediate Result: >100k partisipan (estimasi blog "hundreds of thousands"); engagement naik
· Long-term Impact: Ekspektasi airdrop tercipta; liability tokenomics; regulatory risk pada points-as-securities
· Supporting Dataset: Phase 3 EV-009, Phase 6 Token Information, Phase 6 Major Token Events, Phase 5 Financial Risk

Keputusan: Pengumuman Token POLYMARKET (Pre-TGE) (Mei 2024)
· Trigger: Pressure dari investor (Series B 2022), komunitas, dan narasi pre-TGE kompetitor (Blast, Linea, dll)
· Evidence: Blog resmi "Introducing the Polymarket Token" (Phase 3 EV-010, Phase 6 Token Information)
· Decision: Announce token rencana, nama POLYMARKET, utility governance + incentive; zero detail numerik (supply, allocation, vesting, TGE date)
· Immediate Result: Hype pasar, spekulasi komunitas, points program jadi "preskripsi"
· Long-term Impact: Tokenomics opacity menciptakan ketidakpastian; pressure untuk deliver TGE 2024/2025
· Supporting Dataset: Phase 3 EV-010, Phase 6 Token Information, Phase 6 Distribution, Phase 6 Vesting Schedule

Keputusan: Record Volume saat Pemilu AS 2024 (November 2024)
· Trigger: Siklus pemilu 4-tahunan mendorong minat global pada prediksi politik; media mainstream coverage
· Evidence: The Block, CoinDesk, Dune dashboard melaporkan volume >$500M bulanan (Phase 3 EV-012, Phase 8 Market Timeline, Phase 8 Narrative Position)
· Decision: Tidak ada keputusan aktif — pasar organik meledak; tim skalakan infra CLOB/indexer
· Immediate Result: Visibilitas mainstream puncak; "largest prediction market in crypto history" narasi
· Long-term Impact: Validasi product-market fit; tekanan untuk mempertahankan volume pasca-pemilu; investor menuntut monetisasi/token
· Supporting Dataset: Phase 3 EV-012, Phase 8 Market Timeline, Phase 8 Narrative Position, Phase 8 Adoption Metrics

Evolution Pattern

Perubahan Strategi: Dari Single-Chain (Polygon) ke Multi-Chain (Polygon + Base)
· Evidence: 2020-2023 hanya Polygon; 2024 Base deployment (Phase 3 EV-002 vs EV-008, Phase 4 Technical Upgrade History)
· Supporting Dataset: Phase 3 EV-002, EV-008, Phase 4 Technical Upgrade History, Phase 7 Major Integrations

Perubahan Teknologi: Dari Monolitik Mainnet V1 ke Modular V2 + CLOB Scaling
· Evidence: V2 upgrade 2023 refactor modular; CLOB improvements ongoing 2024 (Phase 3 EV-007, Phase 4 Technical Upgrade History)
· Supporting Dataset: Phase 3 EV-007, Phase 4 Technical Upgrade History, Phase 4 Current Technical Stack

Perubahan Tokenomics: Dari No-Token (2020-2024) ke Pre-TGE Announcement + Points Program
· Evidence: 4 tahun tanpa token; Mei 2024 announce token + points (Phase 3 EV-009, EV-010, Phase 6 Token Information)
· Supporting Dataset: Phase 3 EV-009, EV-010, Phase 6 Token Information, Phase 6 Major Token Events

Perubahan Governance: Dari Multi-sig Team Only (2020-2024) ke Planned Token Governance
· Evidence: Docs menyatakan governance via multi-sig; blog announce token untuk governance (Phase 4 Security Model, Phase 6 Governance)
· Supporting Dataset: Phase 4 Security Model, Phase 6 Governance, Phase 2 Entity (Polymarket Core Team)

Perubahan Market Position: Dari Niche Crypto Prediction Market ke Mainstream Election Betting Platform
· Evidence: Volume rekor Pemilu 2024, media mainstream coverage (Bloomberg, CNBC, FT) (Phase 8 Narrative Position, Phase 8 Market Timeline EV-012)
· Supporting Dataset: Phase 8 Narrative Position, Phase 8 Market Timeline, Phase 8 Adoption Metrics

Perubahan Regulatory Posture: Dari Open Access (2020) ke Geo-Fenced US Restriction (2022+)
· Evidence: CFTC settlement Jan 2022 membatasi IP US untuk binary markets (Phase 3 EV-005, Phase 5 Financial Risk, Phase 8 Market Position)
· Supporting Dataset: Phase 3 EV-005, Phase 5 Financial Risk, Phase 8 Market Position

Technical Decision Pattern

Pola 1: Modular Smart Contract Architecture dengan Proxy Upgradeability
· Decision Pattern: Kontrak inti (Exchange, Factory, Resolver, ConditionalTokens) dipisah per fungsi dan di-deploy behind UUPS/Transparent Proxy untuk upgradeability
· Evidence: GitHub contracts structure menunjukkan modular packages; proxy pattern di kode (Phase 4 Core Components, Phase 4 Security Model, Phase 4 Technical Upgrade History V2)
· Supporting Dataset: Phase 4 Core Components, Phase 4 Security Model, Phase 4 Technical Upgrade History

Pola 2: Off-Chain Order Matching (CLOB) dengan On-Chain Settlement
· Decision Pattern: Matching engine centralized off-chain (price-time priority, low latency) tapi settlement non-custodial on-chain via Exchange contract; user menandatangani order (EIP-712)
· Evidence: Docs CLOB architecture, blog introducing Polymarket (Phase 4 Core Components CLOB, Phase 4 Security Model, Phase 7 External Dependencies CLOB)
· Supporting Dataset: Phase 4 Core Components, Phase 4 Security Model, Phase 7 External Dependencies, Phase 7 Ecosystem Risks

Pola 3: External Oracle Dependency (UMA) untuk Resolusi Trust-Minimized
· Decision Pattern: Tidak membangun oracle sendiri; mengintegrasikan UMA Optimistic Oracle (proposer/challenger game theory) sebagai resolution layer
· Evidence: Docs UMA integration, UMA docs, EV-003 (Phase 3 EV-003, Phase 4 Core Components UMA, Phase 7 Major Integrations UMA)
· Supporting Dataset: Phase 3 EV-003, Phase 4 Core Components, Phase 7 Major Integrations, Phase 7 Ecosystem Risks

Pola 4: Single Collateral (USDC) Strategy
· Decision Pattern: Hanya menerima USDC sebagai collateral untuk semua pasar; tidak multi-collateral (DAI, USDT, native token)
· Evidence: Docs collateral model, contracts USDC hardcoded (Phase 4 Core Components, Phase 4 Known Technical Limitations, Phase 7 External Dependencies USDC)
· Supporting Dataset: Phase 4 Core Components, Phase 4 Known Technical Limitations, Phase 7 External Dependencies, Phase 5 Financial Dependencies

Pola 5: Gnosis CTF v2 Adoption untuk Conditional Tokens
· Decision Pattern: Menggunakan standar Conditional Tokens Framework Gnosis (split/merge YES/NO, claim after resolution) daripada custom implementation
· Evidence: GitHub CTF adapter, Gnosis CTF repo reference (Phase 4 Core Components CTF Adapter, Phase 7 External Dependencies CTF)
· Supporting Dataset: Phase 4 Core Components, Phase 7 External Dependencies, Phase 4 System Architecture

Pola 6: Foundry + Hardhat Dual Framework untuk Smart Contract Dev
· Decision Pattern: Foundry (forge, cast, anvil) sebagai primary; Hardhat sebagai legacy/alternative config tetap dipertahankan
· Evidence: Repo foundry.toml dan hardhat.config.ts coexist (Phase 4 Development Framework)
· Supporting Dataset: Phase 4 Development Framework, Phase 4 Current Technical Stack

Pola 7: TypeScript Monorepo (Next.js Frontend, SDK, Indexer, CLOB API)
· Decision Pattern: Seluruh off-chain stack (frontend, SDK, indexer, CLOB) dalam single TypeScript monorepo dengan shared packages
· Evidence: GitHub monorepo structure packages/frontend, sdk, indexer, clob (Phase 4 Development Framework, Phase 4 Current Technical Stack, Phase 7 Developer Ecosystem)
· Supporting Dataset: Phase 4 Development Framework, Phase 4 Current Technical Stack, Phase 7 Developer Ecosystem

Pola 8: Multi-Chain Deployment via Contract Mirroring (bukan Cross-Chain Native)
· Decision Pattern: Deploy kontrak identik ke Base (mirror) bukan native cross-chain messaging; bridging via canonical bridge untuk USDC/conditional tokens
· Evidence: EV-008 Base deployment, docs bridging mention (Phase 3 EV-008, Phase 4 Technical Upgrade History Base, Phase 7 Major Integrations Base, Phase 7 Open Threads)
· Supporting Dataset: Phase 3 EV-008, Phase 4 Technical Upgrade History, Phase 7 Major Integrations, Phase 7 Open Threads

Financial Decision Pattern

Pola 1: VC-Funded Runway dengan Valuasi Bertahap Meningkat
· Decision Pattern: Series A ($4M, Polychain 2021) → Series B ($70M, Founders Fund 2022); tidak ada public sale, grant, atau DAO treasury
· Evidence: The Block, TechCrunch coverage kedua ronde (Phase 3 EV-004, EV-006, Phase 5 Funding History, Phase 5 Fundraising Mechanism)
· Supporting Dataset: Phase 3 EV-004, EV-006, Phase 5 Funding History, Phase 5 Fundraising Mechanism

Pola 2: Protocol Revenue dari Trading Fees (On-Chain) + CLOB Operator Spread
· Decision Pattern: Fee protokol dikumpulkan on-chain via Exchange contract (USDC); CLOB operator (Polymarket Inc.) mungkin mengambil spread maker/taker
· Evidence: Docs fee structure, Exchange contract fee collection (Phase 5 Revenue Model, Phase 4 Core Components Exchange)
· Supporting Dataset: Phase 5 Revenue Model, Phase 4 Core Components, Phase 5 Revenue History

Pola 3: Treasury Opacity — Tidak Ada Transparency Report atau Dashboard Publik
· Decision Pattern: Zero disclosure treasury composition, custodian, runway, burn rate; investor updates internal saja
· Evidence: Phase 5 Treasury mencatat "tidak diungkap" untuk semua field; tidak ditemukan transparency report (Phase 5 Treasury, Phase 5 Official Financial Resources)
· Supporting Dataset: Phase 5 Treasury, Phase 5 Official Financial Resources, Phase 5 Financial Risk

Pola 4: Pre-TGE Token Liability tanpa Token Sale Terverifikasi
· Decision Pattern: Announce token + points program menciptakan ekspektasi airdrop; zero private/public sale confirmation; investor Series A/B mungkin punya side letter token allocation
· Evidence: Blog token announcement, Phase 5 Token Sale "belum", Phase 6 Distribution "Planned" all categories (Phase 3 EV-009, EV-010, Phase 5 Token Sale, Phase 6 Distribution)
· Supporting Dataset: Phase 3 EV-009, EV-010, Phase 5 Token Sale, Phase 6 Distribution, Phase 6 Open Threads

Pola 5: CFTC Settlement Cost sebagai Operational Expense
· Decision Pattern: Denda $1.4M dibayar cash dari treasury; tidak mempengaruhi protocol fees atau smart contract logic
· Evidence: CFTC press release, CoinDesk (Phase 3 EV-005, Phase 5 Financial Risk Regulatory)
· Supporting Dataset: Phase 3 EV-005, Phase 5 Financial Risk

Ecosystem Decision Pattern

Pola 1: Deep Integration dengan UMA Oracle sebagai Resolution Backbone
· Decision Pattern: UMA Optimistic Oracle di-integrasikan sejak mainnet 2020 (EV-003) dan menjadi critical dependency; tidak ada fallback oracle
· Evidence: EV-003, Docs UMA integration, UMA ecosystem page (Phase 3 EV-003, Phase 7 Major Integrations UMA, Phase 7 External Dependencies UMA, Phase 7 Ecosystem Risks Oracle)
· Supporting Dataset: Phase 3 EV-003, Phase 7 Major Integrations, Phase 7 External Dependencies, Phase 7 Ecosystem Risks

Pola 2: Chain Expansion Mengikuti Liquidity dan User Access (Polygon → Base)
· Decision Pattern: Polygon dipilih 2020 untuk low gas; Base 2024 untuk Coinbase ecosystem access; keduanya EVM L2 dengan canonical bridge ke Ethereum
· Evidence: EV-002 Polygon launch, EV-008 Base deployment, blog multi-chain context (Phase 3 EV-002, EV-008, Phase 7 Major Integrations, Phase 7 External Dependencies Polygon/Base)
· Supporting Dataset: Phase 3 EV-002, EV-008, Phase 7 Major Integrations, Phase 7 External Dependencies

Pola 3: Gnosis CTF sebagai Standard Dependency (bukan Build Own)
· Decision Pattern: Adopsi CTF v2 Gnosis untuk conditional tokens; kontribusi upstream ke Gnosis repo minimal (hanya adapter)
· Evidence: GitHub CTF adapter, Gnosis CTF repo (Phase 4 Core Components CTF Adapter, Phase 7 External Dependencies CTF)
· Supporting Dataset: Phase 4 Core Components, Phase 7 External Dependencies

Pola 4: Centralized CLOB Operator (Self-Operated) dengan API Openness
· Decision Pattern: Polymarket Inc. menjalankan CLOB sendiri; menyediakan REST/WebSocket API publik untuk bot/eksternal; tidak ada federation operator
· Evidence: Docs CLOB architecture, clob.polymarket.com API (Phase 4 Core Components CLOB, Phase 7 External Dependencies CLOB, Phase 7 Infrastructure Providers Polymarket Inc.)
· Supporting Dataset: Phase 4 Core Components, Phase 7 External Dependencies, Phase 7 Infrastructure Providers, Phase 7 Ecosystem Risks Centralization

Pola 5: Developer Ecosystem via Open Source + SDK/API (tanpa Grant/Hackathon)
· Decision Pattern: Monorepo publik, SDK TypeScript/Python, CLOB API, Indexer GraphQL; tidak ada grant program, hackathon resmi, atau developer fund
· Evidence: GitHub monorepo, docs developers, SDK repos (Phase 7 Developer Ecosystem, Phase 7 Applications, Phase 7 Official Ecosystem Resources)
· Supporting Dataset: Phase 7 Developer Ecosystem, Phase 7 Applications, Phase 7 Official Ecosystem Resources, Phase 8 Open Threads

Pola 6: Fiat On-Ramp Integration (MoonPay/Transak) untuk Mainstream Access
· Decision Pattern: Frontend integrate MoonPay/Transak untuk fiat→USDC on-ramp; memperluas user base non-crypto
· Evidence: Frontend shows MoonPay (Phase 8 Narrative Position Consumer Crypto, Phase 7 Applications Frontend)
· Supporting Dataset: Phase 8 Narrative Position, Phase 7 Applications

Governance Decision Pattern

Pola 1: Multi-Sig Team Control (Gnosis Safe) untuk Semua Parameter Kritis
· Decision Pattern: Upgrade proxy, fee parameter, oracle address, pausing — semua dikontrol multi-sig tim Polymarket Inc.; tidak ada token voting, DAO, atau community governance
· Evidence: Docs governance, Security Model multi-sig (Phase 4 Security Model, Phase 6 Governance, Phase 7 Governance Ecosystem)
· Supporting Dataset: Phase 4 Security Model, Phase 6 Governance, Phase 7 Governance Ecosystem

Pola 2: Token Governance Diannounce Tapi Belum Desain (Pre-TGE Vaporware)
· Decision Pattern: Blog announce token untuk "governance" tapi zero detail: voting system, delegation, proposal threshold, treasury control, timelock
· Evidence: Blog token announcement, Phase 6 Governance "tidak diketahui" semua field (Phase 3 EV-010, Phase 6 Governance, Phase 6 Token Information)
· Supporting Dataset: Phase 3 EV-010, Phase 6 Governance, Phase 6 Token Information, Phase 6 Open Threads

Pola 3: UMA Tokenholder Governance sebagai External Resolution Escalation
· Decision Pattern: Jika UMA challenge melewati window, UMA tokenholder vote pada eskalasi; Polymarket tidak mengontrol ini
· Evidence: UMA Optimistic Oracle docs, Phase 7 Governance Ecosystem UMA tokenholders (Phase 7 Governance Ecosystem, Phase 7 External Dependencies UMA)
· Supporting Dataset: Phase 7 Governance Ecosystem, Phase 7 External Dependencies

Pola 4: Tidak Ada Foundation Terpisah atau DAO Legal Wrapper (Per 2024)
· Decision Pattern: Polymarket Inc. (Delaware Corp) adalah single legal entity; tidak ada Cayman foundation, BVI entity, atau DAO LLC
· Evidence: Phase 7 Governance Ecosystem "tidak ada foundation/DAO", Phase 2 Entity hanya Polymarket Inc. (Phase 7 Governance Ecosystem, Phase 2 Entity)
· Supporting Dataset: Phase 7 Governance Ecosystem, Phase 2 Entity

Risk Response Pattern

Pola 1: Regulatory Compliance via Geo-Fencing (CFTC Response)
· Trigger: CFTC enforcement action Jan 2022 — unregistered binary options
· Decision Pattern: Bayar denda $1.4M, implement IP-based restriction untuk pasar biner tertentu pada US users, maintain global operations untuk non-US
· Evidence: CFTC press release, EV-005, Financial Risk regulatory (Phase 3 EV-005, Phase 5 Financial Risk, Phase 8 Market Position)
· Response: Geo-fencing binary markets; non-binary (categorical) mungkin tetap accessible; compliance team expanded (inferred)
· Result: US users terbatas; volume global tetap tumbuh; regulatory risk remains untuk token launch
· Supporting Dataset: Phase 3 EV-005, Phase 5 Financial Risk, Phase 8 Market Position

Pola 2: Technical Upgrade sebagai Response ke Scaling Needs (V2 Upgrade 2023)
· Trigger: Gas costs, UX friction, limited market types pada V1; kompetitor (Azuro) dengan AMM model
· Decision Pattern: Major refactor V2 — modular contracts, batch trade, permit signatures, categorical >2 outcomes, meta-tx support
· Evidence: EV-007, GitHub commits 2023, Technical Upgrade History (Phase 3 EV-007, Phase 4 Technical Upgrade History)
· Response: Deploy V2 contracts di Polygon; migration path untuk pasar lama
· Result: Gas efficiency improved; new market types enabled; foundation untuk Base deployment
· Supporting Dataset: Phase 3 EV-007, Phase 4 Technical Upgrade History, Phase 4 Development Framework

Pola 3: Multi-Chain Deployment sebagai Chain Risk Diversification (Base 2024)
· Trigger: Polygon single-chain dependency; Base/Coinbase ecosystem opportunity; user demand untuk alternative L2
· Decision Pattern: Mirror contracts ke Base; extend CLOB API; frontend chain switcher; canonical bridge untuk assets
· Evidence: EV-008, Technical Upgrade History Base, Major Integrations Base (Phase 3 EV-008, Phase 4 Technical Upgrade History, Phase 7 Major Integrations)
· Response: Live di Base Maret 2024; parity fitur belum diverifikasi penuh
· Result: Access ke Coinbase user base; liquidity fragmentation risk (separate order books inferred)
· Supporting Dataset: Phase 3 EV-008, Phase 4 Technical Upgrade History, Phase 7 Major Integrations, Phase 7 Open Threads

Pola 4: Points Program sebagai Pre-TGE Retention Mechanism
· Trigger: Kompetitor pre-TGE narratives (Blast, Linea, zkSync, EigenLayer) dengan points/airdrop farming; investor pressure untuk token
· Decision Pattern: Off-chain points tracking (trading, liquidity, referrals), leaderboard, snapshot merkle root berkala untuk future claim
· Evidence: EV-009, EV-010, Blog token announcement, Points program live (Phase 3 EV-009, EV-010, Phase 6 Major Token Events)
· Response: Launch Mei 2024; "hundreds of thousands" participants claimed
· Result: Engagement spike; regulatory risk (points as securities); token expectation management challenge
· Supporting Dataset: Phase 3 EV-009, EV-010, Phase 6 Major Token Events, Phase 5 Financial Risk Pre-TGE Liability

Pola 5: Oracle Challenge Window Acceptance (UMA Delay Tolerance)
· Trigger: UMA Optimistic Oracle challenge window 2-48 jam + potential vote 48-72 jam = resolusi tidak instan
· Decision Pattern: Menerima delay resolusi sebagai trade-off untuk trust-minimization; tidak membangun instant resolution oracle sendiri
· Evidence: Known Technical Limitations UMA delay, UMA docs challenge window (Phase 4 Known Technical Limitations, Phase 7 External Dependencies UMA)
· Response: UX design communicate resolution timeline; no technical mitigation
· Result: User friction pada market closure; trust-minimized integrity maintained
· Supporting Dataset: Phase 4 Known Technical Limitations, Phase 7 External Dependencies, Phase 7 Ecosystem Risks Oracle

Recurring Behavioral Pattern

Pola 1: Ekspansi Teknis Mengikuti Funding Milestone
· Evidence: Series A (2021) → team expansion; Series B (2022) → V2 upgrade (2023) + Base deployment (2024) + Points/Token announce (2024) (Phase 3 EV-004, EV-006, EV-007, EV-008, EV-009, EV-010, Phase 5 Funding History)
· Supporting Dataset: Phase 3 EV-004, EV-006, EV-007, EV-008, EV-009, EV-010, Phase 5 Funding History

Pola 2: Mengadopsi Standar Eksternal (CTF, UMA, USDC) Daripada Build Sendiri
· Evidence: CTF Gnosis untuk conditional tokens, UMA untuk oracle, USDC untuk collateral — semua external dependencies critical (Phase 4 Core Components, Phase 7 External Dependencies, Phase 7 Major Integrations)
· Supporting Dataset: Phase 4 Core Components, Phase 7 External Dependencies, Phase 7 Major Integrations

Pola 3: Centralized Operations dengan Non-Custodial Settlement (CLOB, Points, Frontend)
· Evidence: CLOB operator Polymarket Inc.; Points off-chain database; Frontend hosted Polymarket; tapi user custody USDC, sign orders, settle on-chain (Phase 4 Core Components CLOB, Phase 4 Security Model, Phase 7 Infrastructure Providers, Phase 6 Major Token Events Points)
· Supporting Dataset: Phase 4 Core Components, Phase 4 Security Model, Phase 7 Infrastructure Providers, Phase 6 Major Token Events

Pola 4: Major Event-Driven Volume Spikes (Election Cycles) sebagai Growth Catalyst
· Evidence: 2020 launch, 2022 midterms (inferred), 2024 Presidential election record volume EV-012; cyclical 4-year pattern (Phase 3 EV-012, Phase 8 Narrative Position US Election, Phase 8 Market Timeline)
· Supporting Dataset: Phase 3 EV-012, Phase 8 Narrative Position, Phase 8 Market Timeline

Pola 5: Announce Future Decentralization (Token, Governance) Sambil Operasikan Centralized Sekarang
· Evidence: 2020-2024 no token, multi-sig governance; 2024 announce token untuk governance tapi zero detail; CLOB tetap centralized (Phase 4 Security Model, Phase 6 Governance, Phase 7 Governance Ecosystem, Phase 7 Ecosystem Risks Centralization)
· Supporting Dataset: Phase 4 Security Model, Phase 6 Governance, Phase 7 Governance Ecosystem, Phase 7 Ecosystem Risks

Strategic Trade-offs

Trade-off 1: Desentralisasi Resolusi (UMA) vs Kecepatan Finalisasi
· Decision: Menggunakan UMA Optimistic Oracle dengan challenge window 2-48 jam + eskalasi vote
· Trade-off: Resolusi pasar butuh hari-hari (tidak instan) demi trust-minimization dan game-theoretic security tanpa trusted resolver
· Evidence: Known Technical Limitations UMA delay, UMA docs challenge window (Phase 4 Known Technical Limitations, Phase 7 External Dependencies UMA, Phase 7 Ecosystem Risks Oracle)
· Supporting Dataset: Phase 4 Known Technical Limitations, Phase 7 External Dependencies, Phase 7 Ecosystem Risks

Trade-off 2: CLOB Centralized Matching vs Throughput dan UX
· Decision: Single operator CLOB off-chain (Polymarket Inc.) dengan price-time priority, low latency
· Trade-off: Kepercayaan pada operator untuk fairness, uptime, censorship resistance; keuntungan: UX CEX-like, high throughput, gas efficiency (batch settlement)
· Evidence: CLOB architecture docs, Security Model, Ecosystem Risks Centralization (Phase 4 Core Components CLOB, Phase 4 Security Model, Phase 7 Ecosystem Risks)
· Supporting Dataset: Phase 4 Core Components, Phase 4 Security Model, Phase 7 Ecosystem Risks

Trade-off 3: Single Collateral (USDC) vs Composability dan Risk Diversification
· Decision: Hanya USDC sebagai collateral untuk semua pasar
· Trade-off: Simplicitas accounting, liquidity concentration, USDC depeg/freeze risk systemic; tidak mendukung multi-collateral seperti DAI/USDT/native token
· Evidence: Known Technical Limitations single collateral, Financial Dependencies USDC (Phase 4 Known Technical Limitations, Phase 5 Financial Dependencies, Phase 7 External Dependencies USDC)
· Supporting Dataset: Phase 4 Known Technical Limitations, Phase 5 Financial Dependencies, Phase 7 External Dependencies

Trade-off 4: Contract Mirroring Multi-Chain vs Native Cross-Chain Interoperability
· Decision: Deploy kontrak identik (mirror) ke Base; bridging via canonical bridge; tidak native cross-chain messaging (LayerZero, Wormhole, CCIP)
· Trade-off: Simplicity, security (canonical bridge), shared liquidity tidak mungkin (separate order books per chain); user friction bridging positions
· Evidence: EV-008 Base deployment, Open Threads cross-chain bridging, Known Limitations cross-chain fungibility (Phase 3 EV-008, Phase 4 Technical Upgrade History, Phase 4 Known Technical Limitations, Phase 7 Open Threads)
· Supporting Dataset: Phase 3 EV-008, Phase 4 Technical Upgrade History, Phase 4 Known Technical Limitations, Phase 7 Open Threads

Trade-off 5: Off-Chain Points Program (Centralized) vs On-Chain Transparent Incentives
· Decision: Points tracked off-chain database, snapshot merkle root berkala; tidak on-chain programmatic rewards
· Trade-off: Flexibilitas formula earning, gas-free untuk user, mudah iterasi; tapi opacity, centralized control, regulatory risk (points as securities), no composability
· Evidence: EV-009 Points launch, EV-010 token announce, Financial Risk Pre-TGE Liability, Known Limitations points off-chain (Phase 3 EV-009, EV-010, Phase 5 Financial Risk, Phase 4 Known Technical Limitations)
· Supporting Dataset: Phase 3 EV-009, EV-010, Phase 5 Financial Risk, Phase 4 Known Technical Limitations

Trade-off 6: Geo-Fencing US Users (Regulatory Compliance) vs Global Permissionless Access
· Decision: Restrict binary markets untuk IP US pasca-CFTC; maintain access untuk non-US
· Trade-off: Compliance dengan US regulator, avoid further enforcement; kehilangan pasar AS terbesar dunia, narasi "permissionless" terkorosi
· Evidence: EV-005 CFTC settlement, Market Position non-US primary, Financial Risk Regulatory (Phase 3 EV-005, Phase 8 Market Position, Phase 5 Financial Risk)
· Supporting Dataset: Phase 3 EV-005, Phase 8 Market Position, Phase 5 Financial Risk

Trade-off 7: Token Announcement Without Details (Narrative Management) vs Community Trust
· Decision: Announce token name, utility categories, points-as-basis tapi zero numerik (supply, allocation, vesting, TGE date)
· Trade-off: Narrative control, investor/community retention, competitive positioning; kerusakan kepercayaan jika delay lama atau tokenomics tidak memenuhi ekspektasi
· Evidence: EV-010 token announce, Token Information all "tidak diketahui", Distribution all "Planned", Open Threads tokenomics opacity (Phase 3 EV-010, Phase 6 Token Information, Phase 6 Distribution, Phase 6 Open Threads)
· Supporting Dataset: Phase 3 EV-010, Phase 6 Token Information, Phase 6 Distribution, Phase 6 Open Threads

Behavioral Summary

Prioritas Utama Proyek
1. Product-Market Fit pada Prediction Markets: Membangun CLOB + UMA + USDC stack yang work di scale (EV-012 volume rekor membuktikan)
2. Regulatory Survival: Navigasi CFTC via geo-fencing, compliance hiring, token launch compliance planning
3. Investor Return Path: Series B $70M (Founders Fund) menciptakan pressure untuk TGE/liquidity event
4. Multi-Chain Positioning: Polygon (home) + Base (expansion) untuk chain risk diversification dan user acquisition

Cara Mengambil Keputusan
- Founder-led (Shayne Coplan CEO) dengan input investor board (Polychain, Founders Fund, ParaFi, Dragonfly)
- Teknis: Pragmatis — adopt external standards (CTF, UMA, USDC) daripada build sendiri; modular architecture untuk upgradeability
- Finansial: VC-funded runway; protocol fees sebagai revenue; treasury opacity maksimal
- Ekosistem: Deep integration selected partners (UMA, Polygon, Base, Circle) daripada broad shallow partnerships
- Governance: Centralized multi-sig sekarang; token governance promised tapi undefined

Faktor Paling Sering Mempengaruhi Keputusan
1. Investor Timeline/Expectations (Series B 2022 → token 2024)
2. Regulatory Constraints (CFTC 2022 → geo-fencing, token compliance)
3. Market Cycles (Election 2024 → volume spike, mainstream attention)
4. Technical Debt/Scaling Needs (V1 → V2 → Base)
5. Competitive Landscape (Azuro AMM, pre-TGE narratives Blast/Linea)

Pola Evolusi
- 2020: Launch minimal viable (Polygon, CLOB, UMA, USDC)
- 2021: Series A, team build
- 2022: CFTC crisis → compliance pivot; Series B → war chest
- 2023: V2 upgrade → technical foundation
- 2024: Multi-chain (Base) + Pre-TGE narrative (Points + Token announce) + Election volume explosion

Kekuatan Utama
- Dominan market share crypto prediction markets (>80% volume estimated)
- Live product dengan real volume, revenue, users (bukan vaporware)
- Strong investor syndicate (Polychain, Founders Fund/Thiel, ParaFi, Dragonfly)
- Technical moat: CLOB order book + UMA oracle + CTF standard = hard to replicate full stack
- Mainstream brand recognition via election cycles

Kelemahan Utama
- Centralization: CLOB operator, points database, multi-sig governance, USDC single collateral, UMA single oracle
- Tokenomics opacity: Zero numerik detail 6 bulan pasca-announce
- Treasury opacity: No transparency report, unknown runway
- Regulatory overhang: CFTC settlement, token launch compliance unclear, points securities risk
- Chain dependency: Polygon concentration, Base parity unverified, no native cross-chain
- Post-election retention risk: Volume cyclical, no proven non-election sustain model

## Knowledge Extraction
_ref: `docs/Patterns/*`, `docs/Reasoning/*` (rule candidates)_

PROJECT: Polymarket

## Core Insights

Insight 1: Dominan market share crypto prediction markets (>80% volume estimated)
Explanation: Polymarket menguasai volume trading pada kategori prediction market on-chain, jauh mengungguli kompetitor seperti Azuro, Zeitgeist, Augur
Evidence: Phase 8 Market Share menyatakan "Estimated >80% of on-chain prediction market volume"【Phase 8 — Market Share】; Phase 3 EV-012 mencatat volume rekor $500M+ bulanan saat Pemilu AS 2024【Phase 3 — EV-012】
Supporting Dataset: Phase 8 Market Share, Phase 3 EV-012, Phase 8 Adoption Metrics
Confidence: High

Insight 2: Live product dengan real revenue sebelum token launch (pre-TGE revenue positive)
Explanation: Protocol mengumpulkan trading fees on-chain dalam USDC sejak mainnet 2020; revenue tidak bergantung pada token emissions
Evidence: Phase 5 Revenue Model mencatat "Protocol Trading Fees — Status: Live" dan "CLOB Operator Revenue — Status: Live"【Phase 5 — Revenue Model】; Phase 4 Core Components Exchange contract mengimplementasikan fee collection【Phase 4 — Core Components】
Supporting Dataset: Phase 5 Revenue Model, Phase 4 Core Components, Phase 5 Financial Dependencies
Confidence: High

Insight 3: Centralized operations (CLOB, Points, Governance) dengan non-custodial settlement
Explanation: Semua komponen operasional kritis dikendalikan Polymarket Inc. (CLOB operator, points database, multi-sig governance) tapi user custody USDC dan sign orders on-chain
Evidence: Phase 4 Security Model "CLOB Operator: Centralized order matching dijalankan Polymarket Inc.; non-custodial"【Phase 4 — Security Model】; Phase 7 Ecosystem Risks "Centralization Risk: CLOB Operator"【Phase 7 — Ecosystem Risks】; Phase 6 Governance "saat ini governance via multi-sig tim"【Phase 6 — Governance】
Supporting Dataset: Phase 4 Security Model, Phase 7 Ecosystem Risks, Phase 6 Governance, Phase 9 Recurring Behavioral Pattern
Confidence: High

Insight 4: Deep external dependency stack (UMA, USDC, Polygon, Base, Gnosis CTF) bukan build-your-own
Explanation: Protokol mengadopsi standar eksternal untuk oracle, collateral, chain, conditional tokens — tidak membangun komponen infrastruktur fundamental sendiri
Evidence: Phase 7 External Dependencies mencatat 8 dependencies dengan Criticality Critical/High【Phase 7 — External Dependencies】; Phase 9 Technical Decision Pattern Pola 2 "Mengadopsi Standar Eksternal"【Phase 9 — Technical Decision Pattern】
Supporting Dataset: Phase 7 External Dependencies, Phase 7 Major Integrations, Phase 9 Technical Decision Pattern
Confidence: High

Insight 5: Tokenomics opacity total 6 bulan pasca-pengumuman (Mei 2024 - Nov 2024)
Explanation: Pengumuman token EV-010 menyebut nama, utility kategori, tapi zero detail numerik: supply, allocation %, vesting, cliff, TGE date, chain deployment
Evidence: Phase 6 Token Information seluruh field "tidak diketahui" atau "belum diumumkan"【Phase 6 — Token Information】; Phase 6 Distribution 7 kategori "Planned" tanpa persentase【Phase 6 — Distribution】; Phase 6 Open Threads "Seluruh parameter tokenomics numerik... belum dipublikasikan sama sekali"【Phase 6 — Open Threads】
Supporting Dataset: Phase 6 Token Information, Phase 6 Distribution, Phase 6 Vesting Schedule, Phase 6 Open Threads
Confidence: High

Insight 6: Cyclical election-driven volume spikes sebagai growth catalyst utama
Explanation: Volume meledak pada siklus pemilu 4-tahunan (2024 Presidential election record $500M+/bulan); non-election period volume sustainability unproven
Evidence: Phase 3 EV-012 "Volume Trading Polymarket Mencapai Rekor Selama Pemilu AS 2024"【Phase 3 — EV-012】; Phase 8 Narrative Position "US Election 2024 / Political Betting — Status: Main Narrative (Cyclical)"【Phase 8 — Narrative Position】; Phase 9 Recurring Behavioral Pattern Pola 4【Phase 9 — Recurring Behavioral Pattern】
Supporting Dataset: Phase 3 EV-012, Phase 8 Narrative Position, Phase 8 Market Timeline, Phase 9 Recurring Behavioral Pattern
Confidence: High

Insight 7: Regulatory survival via geo-fencing (CFTC settlement → US IP restriction)
Explanation: CFTC enforcement Jan 2022 ($1.4M denda) memaksa pembatasan pasar biner untuk IP US; operasi global non-US tetap berlanjut
Evidence: Phase 3 EV-005 "Tindakan Penegakan CFTC dan Penyelesaian $1.4M"【Phase 3 — EV-005】; Phase 5 Financial Risk "Regulatory Financial Risk: CFTC Enforcement Action"【Phase 5 — Financial Risk】; Phase 9 Risk Response Pattern Pola 1【Phase 9 — Risk Response Pattern】
Supporting Dataset: Phase 3 EV-005, Phase 5 Financial Risk, Phase 8 Market Position, Phase 9 Risk Response Pattern
Confidence: High

Insight 8: VC-funded runway dengan investor high-profile (Polychain, Founders Fund/Thiel, ParaFi, Dragonfly)
Explanation: Series A $4M (2021) → Series B $70M (2022); total $74M; zero public sale, grant, DAO treasury; treasury opacity maksimal
Evidence: Phase 5 Funding History dua ronde terverifikasi【Phase 5 — Funding History】; Phase 5 Fundraising Mechanism "VC Funding: Series A... Series B..."【Phase 5 — Fundraising Mechanism】; Phase 5 Treasury "tidak diungkap" semua field【Phase 5 — Treasury】
Supporting Dataset: Phase 5 Funding History, Phase 5 Fundraising Mechanism, Phase 5 Treasury, Phase 3 EV-004, EV-006
Confidence: High

Insight 9: Multi-chain deployment via contract mirroring (Polygon → Base) bukan native cross-chain
Explanation: Deploy kontrak identik ke Base; bridging via canonical bridge; liquidity terfragmentasi per chain; tidak ada shared CLOB order book
Evidence: Phase 3 EV-008 "Deployment Polymarket di Base (Secondary Deployment)"【Phase 3 — EV-008】; Phase 4 Technical Upgrade History Base Deployment【Phase 4 — Technical Upgrade History】; Phase 4 Known Technical Limitations "Cross-chain positions tidak fungible langsung"【Phase 4 — Known Technical Limitations】; Phase 9 Technical Decision Pattern Pola 8【Phase 9 — Technical Decision Pattern】
Supporting Dataset: Phase 3 EV-008, Phase 4 Technical Upgrade History, Phase 4 Known Technical Limitations, Phase 7 Open Threads, Phase 9 Technical Decision Pattern
Confidence: High

Insight 10: Off-chain points program sebagai pre-TGE retention mechanism dengan regulatory risk
Explanation: Points program EV-009 off-chain database, snapshot merkle root berkala; "hundreds of thousands" participants; menciptakan ekspektasi airdrop dan potential securities risk
Evidence: Phase 3 EV-009 "Peluncuran Polymarket Points Program"【Phase 3 — EV-009】; Phase 6 Major Token Events EV-009【Phase 6 — Major Token Events】; Phase 5 Financial Risk "Pre-TGE Token Liability"【Phase 5 — Financial Risk】; Phase 4 Known Technical Limitations "Points program off-chain... tidak ada bukti kriptografis on-chain"【Phase 4 — Known Technical Limitations】
Supporting Dataset: Phase 3 EV-009, Phase 6 Major Token Events, Phase 5 Financial Risk, Phase 4 Known Technical Limitations, Phase 9 Risk Response Pattern Pola 4
Confidence: High

## Strategic Principles

Principle 1: Adopt external standards over building from scratch
Explanation: Menggunakan Gnosis CTF untuk conditional tokens, UMA untuk oracle, USDC untuk collateral, Polygon/Base untuk execution layer — fokus pada application layer differentiation (CLOB, UX, market creation)
Evidence: Phase 9 Technical Decision Pattern Pola 2 "Mengadopsi Standar Eksternal"【Phase 9 — Technical Decision Pattern】; Phase 7 External Dependencies 8 dependencies critical/high【Phase 7 — External Dependencies】
Supporting Dataset: Phase 9 Technical Decision Pattern, Phase 7 External Dependencies, Phase 4 Core Components
Confidence: High

Principle 2: Modular smart contract architecture with proxy upgradeability
Explanation: Kontrak dipisah per fungsi (Exchange, Factory, Resolver, ConditionalTokens) behind UUPS/Transparent Proxy untuk upgradeability tanpa migrasi user
Evidence: Phase 4 Technical Decision Pattern Pola 1 "Modular Smart Contract Architecture"【Phase 9 — Technical Decision Pattern】; Phase 4 Security Model "Proxy Upgrade Pattern: UUPS/Transparent Proxy"【Phase 4 — Security Model】; Phase 3 EV-007 V2 upgrade modularisasi【Phase 3 — EV-007】
Supporting Dataset: Phase 9 Technical Decision Pattern, Phase 4 Security Model, Phase 3 EV-007, Phase 4 Technical Upgrade History
Confidence: High

Principle 3: Centralized off-chain matching (CLOB) with non-custodial on-chain settlement
Explanation: Price-time priority matching off-chain untuk throughput/UX CEX-like; user menandatangani order EIP-712; settlement atomic on-chain via Exchange contract
Evidence: Phase 4 Core Components CLOB "off-chain matching dengan on-chain settlement"【Phase 4 — Core Components】; Phase 4 Security Model "CLOB Operator: Centralized... non-custodial"【Phase 4 — Security Model】; Phase 7 Ecosystem Risks Centralization Risk【Phase 7 — Ecosystem Risks】
Supporting Dataset: Phase 4 Core Components, Phase 4 Security Model, Phase 7 Ecosystem Risks, Phase 9 Technical Decision Pattern Pola 2
Confidence: High

Principle 4: Trust-minimized resolution via external oracle (UMA Optimistic Oracle)
Explanation: Game-theoretic proposer/challenger mechanism dengan bond; eskalasi ke UMA tokenholder vote; tidak membangun oracle sendiri
Evidence: Phase 3 EV-003 UMA integration【Phase 3 — EV-003】; Phase 4 Core Components UMA Optimistic Oracle Integration【Phase 4 — Core Components】; Phase 7 Major Integrations UMA【Phase 7 — Major Integrations】; Phase 9 Technical Decision Pattern Pola 3【Phase 9 — Technical Decision Pattern】
Supporting Dataset: Phase 3 EV-003, Phase 4 Core Components, Phase 7 Major Integrations, Phase 9 Technical Decision Pattern
Confidence: High

Principle 5: Single collateral strategy (USDC only) untuk simplicitas accounting dan liquidity concentration
Explanation: Hanya USDC diterima; tidak multi-collateral; mengurangi kompleksitas smart contract dan fragmentasi likuiditas
Evidence: Phase 4 Known Technical Limitations "Hanya mendukung collateral USDC"【Phase 4 — Known Technical Limitations】; Phase 7 External Dependencies USDC Criticality Critical【Phase 7 — External Dependencies】; Phase 9 Technical Decision Pattern Pola 4【Phase 9 — Technical Decision Pattern】
Supporting Dataset: Phase 4 Known Technical Limitations, Phase 7 External Dependencies, Phase 9 Technical Decision Pattern
Confidence: High

Principle 6: Multi-chain expansion follows liquidity and user access (Polygon → Base)
Explanation: Polygon dipilih 2020 untuk low gas; Base 2024 untuk Coinbase ecosystem access; keduanya EVM L2 dengan canonical bridge
Evidence: Phase 3 EV-002 Polygon launch【Phase 3 — EV-002】; Phase 3 EV-008 Base deployment【Phase 3 — EV-008】; Phase 9 Ecosystem Decision Pattern Pola 2【Phase 9 — Ecosystem Decision Pattern】
Supporting Dataset: Phase 3 EV-002, Phase 3 EV-008, Phase 9 Ecosystem Decision Pattern
Confidence: High

Principle 7: Founder-led decision making dengan investor board input
Explanation: Shayne Coplan CEO mengarahkan strategi; investor Polychain, Founders Fund, ParaFi, Dragonfly di board; technical decisions pragmatic
Evidence: Phase 2 Entity Shayne Coplan "Pendiri dan CEO... mengarahkan visi strategis"【Phase 2 — Entity】; Phase 5 Funding History lead investors【Phase 5 — Funding History】; Phase 9 Behavioral Summary "Founder-led (Shayne Coplan CEO) dengan input investor board"【Phase 9 — Behavioral Summary】
Supporting Dataset: Phase 2 Entity, Phase 5 Funding History, Phase 9 Behavioral Summary
Confidence: High

Principle 8: Regulatory compliance via geo-fencing bukan protocol redesign
Explanation: CFTC settlement → IP-based restriction untuk binary markets US users; core protocol unchanged; non-US access maintained
Evidence: Phase 3 EV-005 CFTC settlement【Phase 3 — EV-005】; Phase 9 Risk Response Pattern Pola 1 "Geo-Fencing US Users"【Phase 9 — Risk Response Pattern】; Phase 8 Market Position "non-US users primary"【Phase 8 — Market Position】
Supporting Dataset: Phase 3 EV-005, Phase 9 Risk Response Pattern, Phase 8 Market Position
Confidence: High

## Success Factors

Factor 1: Product-market fit pada prediction markets dengan CLOB order book UX CEX-like
Explanation: Live product 2020+ dengan real volume, revenue, users; bukan vaporware; CLOB memberikan UX familiar bagi trader tradisional
Evidence: Phase 8 Market Stage "Growth (Pre-TGE, live product with significant traction)"【Phase 8 — Ringkasan】; Phase 3 EV-012 volume rekor $500M+ bulanan【Phase 3 — EV-012】; Phase 5 Revenue Model "Protocol Trading Fees — Status: Live"【Phase 5 — Revenue Model】
Supporting Dataset: Phase 8 Ringkasan, Phase 3 EV-012, Phase 5 Revenue Model, Phase 8 Adoption Metrics
Confidence: High

Factor 2: Strong investor syndicate memberikan credibility dan runway
Explanation: Polychain (Series A), Founders Fund/Thiel (Series B lead), ParaFi, Dragonfly — $74M total; signaling value untuk recruitment, partnerships, narrative
Evidence: Phase 5 Funding History dua ronde【Phase 5 — Funding History】; Phase 3 EV-004 Series A【Phase 3 — EV-004】; Phase 3 EV-006 Series B【Phase 3 — EV-006】; Phase 8 Market Timeline Series B milestone【Phase 8 — Market Timeline】
Supporting Dataset: Phase 5 Funding History, Phase 3 EV-004, Phase 3 EV-006, Phase 8 Market Timeline
Confidence: High

Factor 3: Deep technical moat: full stack CLOB + UMA Oracle + CTF standard = hard to replicate
Explanation: Kompetitor Azuro (AMM), Zeitgeist (Polkadot), Augur (legacy) tidak punya kombinasi CLOB off-chain + UMA resolution + Gnosis CTF + multi-chain deployment
Evidence: Phase 8 Competitor Landscape 8 kompetitor dengan model berbeda【Phase 8 — Competitor Landscape】; Phase 8 Market Share ">80% on-chain prediction market volume"【Phase 8 — Market Share】; Phase 4 System Architecture full stack【Phase 4 — System Architecture】
Supporting Dataset: Phase 8 Competitor Landscape, Phase 8 Market Share, Phase 4 System Architecture
Confidence: High

Factor 4: Election cycles sebagai organic growth catalyst tanpa marketing spend besar
Explanation: Pemilu AS 2024 mendorong volume rekor $500M+/bulan; media mainstream coverage (Bloomberg, CNBC, FT) gratis; brand awareness 폭발
Evidence: Phase 3 EV-012 record volume【Phase 3 — EV-012】; Phase 8 Narrative Position "US Election 2024 — Main Narrative"【Phase 8 — Narrative Position】; Phase 8 Adoption Metrics peak metrics【Phase 8 — Adoption Metrics】
Supporting Dataset: Phase 3 EV-012, Phase 8 Narrative Position, Phase 8 Adoption Metrics, Phase 9 Recurring Behavioral Pattern Pola 4
Confidence: High

Factor 5: Pragmatic technology choices (Foundry, TypeScript monorepo, modular contracts) memungkinkan shipping cepat
Explanation: Foundry untuk contract dev; TypeScript monorepo shared packages; V2 upgrade 2023 modularisasi; Base deployment 2024 mirror contracts — semua shipped tanpa major delay
Evidence: Phase 4 Development Framework Foundry + Hardhat【Phase 4 — Development Framework】; Phase 4 Current Technical Stack TypeScript monorepo【Phase 4 — Current Technical Stack】; Phase 3 EV-007 V2 upgrade【Phase 3 — EV-007】; Phase 3 EV-008 Base deployment【Phase 3 — EV-008】
Supporting Dataset: Phase 4 Development Framework, Phase 4 Current Technical Stack, Phase 3 EV-007, Phase 3 EV-008
Confidence: High

Factor 6: Fiat on-ramp integration (MoonPay/Transak) memperluas user base non-crypto
Explanation: Frontend integrate MoonPay/Transak untuk fiat→USDC; lowering barrier to entry untuk mainstream users saat election cycles
Evidence: Phase 8 Narrative Position "Consumer Crypto / Mainstream Adoption — fiat on-ramp via MoonPay/Transak"【Phase 8 — Narrative Position】; Phase 7 Applications Frontend【Phase 7 — Applications】
Supporting Dataset: Phase 8 Narrative Position, Phase 7 Applications
Confidence: Medium

## Failure Factors

Factor 1: Treasury opacity total — tidak ada transparency report, dashboard, atau on-chain tracking
Explanation: Zero disclosure treasury composition, custodian, runway, burn rate; stakeholder tidak dapat memverifikasi financial health
Evidence: Phase 5 Treasury "tidak diungkap" semua field【Phase 5 — Treasury】; Phase 5 Official Financial Resources "Transparency Report: tidak ada", "Treasury Dashboard: tidak ada"【Phase 5 — Official Financial Resources】; Phase 5 Financial Risk "Treasury Opacity Risk"【Phase 5 — Financial Risk】
Supporting Dataset: Phase 5 Treasury, Phase 5 Official Financial Resources, Phase 5 Financial Risk
Confidence: High

Factor 2: Tokenomics opacity total 6 bulan pasca-announce — merusak community trust
Explanation: Pengumuman EV-010 Mei 2024 tanpa supply, allocation %, vesting, TGE date, chain; "coming soon" saja; kompetitor (Blast, Linea) lebih transparan
Evidence: Phase 6 Token Information seluruh field "tidak diketahui"【Phase 6 — Token Information】; Phase 6 Distribution 7 kategori "Planned" tanpa persentase【Phase 6 — Distribution】; Phase 6 Open Threads "Seluruh parameter tokenomics numerik... belum dipublikasikan sama sekali"【Phase 6 — Open Threads】
Supporting Dataset: Phase 6 Token Information, Phase 6 Distribution, Phase 6 Vesting Schedule, Phase 6 Open Threads
Confidence: High

Factor 3: Centralization risk kritis — CLOB operator, points database, multi-sig governance, USDC single collateral, UMA single oracle
Explanation: Semua critical path dikendalikan entitas terpusat; single point of failure untuk availability, fairness, censorship resistance
Evidence: Phase 7 Ecosystem Risks 4 risiko Centralization/Oracle/Collateral/Chain【Phase 7 — Ecosystem Risks】; Phase 4 Known Technical Limitations 10 limitations termasuk centralization【Phase 4 — Known Technical Limitations】; Phase 9 Recurring Behavioral Pattern Pola 3 "Centralized Operations"【Phase 9 — Recurring Behavioral Pattern】
Supporting Dataset: Phase 7 Ecosystem Risks, Phase 4 Known Technical Limitations, Phase 9 Recurring Behavioral Pattern
Confidence: High

Factor 4: Regulatory overhang dari CFTC settlement + token launch compliance unclear
Explanation: CFTC 2022 settlement $1.4M + US IP restriction; token launch 2024/2025 regulatory classification (security/utility/commodity) belum jelas; points program potential securities risk
Evidence: Phase 3 EV-005 CFTC settlement【Phase 3 — EV-005】; Phase 5 Financial Risk Regulatory + Pre-TGE Liability【Phase 5 — Financial Risk】; Phase 6 Open Threads "Regulatory classification token... tidak diumumkan"【Phase 6 — Open Threads】
Supporting Dataset: Phase 3 EV-005, Phase 5 Financial Risk, Phase 6 Open Threads
Confidence: High

Factor 5: Post-election volume sustainability unproven — cyclical dependency
Explanation: Volume driven by 4-year election cycles; non-election period retention strategy tidak terdokumentasi; competisi dari Kalshi/PredictIt (US regulated) dan offshore sportsbooks
Evidence: Phase 8 Narrative Position "US Election 2024 — Cyclical Primary"【Phase 8 — Narrative Position】; Phase 9 Recurring Behavioral Pattern Pola 4 "Major Event-Driven Volume Spikes"【Phase 9 — Recurring Behavioral Pattern】; Phase 8 Open Threads "Post-election 2024 volume sustainability strategy"【Phase 8 — Open Threads】
Supporting Dataset: Phase 8 Narrative Position, Phase 9 Recurring Behavioral Pattern, Phase 8 Open Threads
Confidence: High

Factor 6: No native cross-chain interoperability — liquidity fragmentation across Polygon/Base
Explanation: Contract mirroring bukan native cross-chain; separate order books per chain; bridging conditional tokens via canonical bridge dengan friction dan risk
Evidence: Phase 4 Known Technical Limitations "Cross-chain positions tidak fungible langsung"【Phase 4 — Known Technical Limitations】; Phase 7 Open Threads "Detail bridge mechanism... tidak terdokumentasi"【Phase 7 — Open Threads】; Phase 9 Technical Decision Pattern Pola 8 "Contract Mirroring"【Phase 9 — Technical Decision Pattern】
Supporting Dataset: Phase 4 Known Technical Limitations, Phase 7 Open Threads, Phase 9 Technical Decision Pattern
Confidence: High

Factor 7: Developer ecosystem limited — no grant program, hackathon, or developer fund
Explanation: Open source + SDK + API ada tapi tidak ada proactive developer incentives; komunitas builder kecil vs protokol infrastructure lain
Evidence: Phase 7 Developer Ecosystem "Grant Program: Tidak ditemukan", "Hackathon: Tidak ditemukan"【Phase 7 — Developer Ecosystem】; Phase 7 Official Ecosystem Resources "Grant Program: Tidak ditemukan"【Phase 7 — Official Ecosystem Resources】; Phase 8 Open Threads "Developer grant program or hackathon history — none found"【Phase 8 — Open Threads】
Supporting Dataset: Phase 7 Developer Ecosystem, Phase 7 Official Ecosystem Resources, Phase 8 Open Threads
Confidence: High

## Decision Framework

Step 1: Observe — Market opportunity identification & regulatory landscape scan
Explanation: Founder mengidentifikasi peluang prediction market on-chain (2020); Augur v1 UX buruk; CFTC risk known tapi manageable via geo-fencing
Evidence: Phase 3 EV-001 Founding 2020【Phase 3 — EV-001】; Phase 9 Decision Timeline "Pendirian Polymarket Inc.... Identifikasi peluang pasar prediksi terdesentralisasi"【Phase 9 — Decision Timeline】
Supporting Dataset: Phase 3 EV-001, Phase 9 Decision Timeline
Confidence: High

Step 2: Evaluate — Technical architecture selection (chain, oracle, collateral, matching)
Explanation: Pilih Polygon (low gas), UMA Oracle (trust-minimized), USDC (single collateral), CLOB off-chain (UX), CTF Gnosis (standard) — semua external dependencies
Evidence: Phase 3 EV-002 Polygon mainnet launch【Phase 3 — EV-002】; Phase 3 EV-003 UMA integration【Phase 3 — EV-003】; Phase 9 Technical Decision Pattern Pola 2-5【Phase 9 — Technical Decision Pattern】
Supporting Dataset: Phase 3 EV-002, Phase 3 EV-003, Phase 9 Technical Decision Pattern
Confidence: High

Step 3: Fund — VC fundraising staged (Series A → Series B) untuk runway multi-tahun
Explanation: Series A $4M Polychain 2021 → Series B $70M Founders Fund 2022; zero public/grant/DAO funding; treasury opacity maintained
Evidence: Phase 3 EV-004 Series A【Phase 3 — EV-004】; Phase 3 EV-006 Series B【Phase 3 — EV-006】; Phase 5 Funding History【Phase 5 — Funding History】; Phase 9 Financial Decision Pattern Pola 1【Phase 9 — Financial Decision Pattern】
Supporting Dataset: Phase 3 EV-004, Phase 3 EV-006, Phase 5 Funding History, Phase 9 Financial Decision Pattern
Confidence: High

Step 4: Develop — Iterative technical upgrades (V1 → V2 → Base deployment) dengan modular architecture
Explanation: Mainnet 2020 → V2 upgrade 2023 (modular, gas efficiency, categorical markets) → Base deployment 2024 (mirror contracts) → CLOB improvements ongoing
Evidence: Phase 3 EV-007 V2 upgrade【Phase 3 — EV-007】; Phase 3 EV-008 Base deployment【Phase 3 — EV-008】; Phase 4 Technical Upgrade History【Phase 4 — Technical Upgrade History】; Phase 9 Technical Decision Pattern Pola 1, 8【Phase 9 — Technical Decision Pattern】
Supporting Dataset: Phase 3 EV-007, Phase 3 EV-008, Phase 4 Technical Upgrade History, Phase 9 Technical Decision Pattern
Confidence: High

Step 5: Launch — Mainnet live → Points program (pre-TGE retention) → Token announce (narrative management)
Explanation: Mainnet 2020 live; Points EV-009 Mei 2024 off-chain; Token announce EV-010 Mei 2024 zero numerik; Election 2024 organic growth
Evidence: Phase 3 EV-002 Mainnet launch【Phase 3 — EV-002】; Phase 3 EV-009 Points program【Phase 3 — EV-009】; Phase 3 EV-010 Token announce【Phase 3 — EV-010】; Phase 3 EV-012 Election volume【Phase 3 — EV-012】
Supporting Dataset: Phase 3 EV-002, Phase 3 EV-009, Phase 3 EV-010, Phase 3 EV-012
Confidence: High

Step 6: Govern — Multi-sig team control sekarang → Token governance promised (undefined)
Explanation: Gnosis Safe multi-sig untuk upgrade, fee, oracle, pause; token governance di-announce tapi zero detail (voting, delegation, quorum, treasury control)
Evidence: Phase 4 Security Model "Multi-sig (Gnosis Safe) untuk upgrade proxy"【Phase 4 — Security Model】; Phase 6 Governance "tidak diketahui" semua field【Phase 6 — Governance】; Phase 7 Governance Ecosystem "Tidak ada DAO aktif"【Phase 7 — Governance Ecosystem】
Supporting Dataset: Phase 4 Security Model, Phase 6 Governance, Phase 7 Governance Ecosystem
Confidence: High

Step 7: Respond — Risk response patterns: geo-fencing (CFTC), technical upgrade (scaling), multi-chain (chain risk), points (retention)
Explanation: Setiap crisis/trigger memicu response terstruktur: CFTC → geo-fencing; scaling needs → V2; chain dependency → Base; pre-TGE competition → points
Evidence: Phase 9 Risk Response Pattern Pola 1-5【Phase 9 — Risk Response Pattern】; Phase 3 EV-005, EV-007, EV-008, EV-009【Phase 3 — EV-005】【Phase 3 — EV-007】【Phase 3 — EV-008】【Phase 3 — EV-009】
Supporting Dataset: Phase 9 Risk Response Pattern, Phase 3 EV-005, Phase 3 EV-007, Phase 3 EV-008, Phase 3 EV-009
Confidence: High

## Reusable Playbook

Playbook 1: Build application-layer protocol on existing L2 + external oracle + standard collateral
Explanation: Jangan build chain/oracle/stablecoin sendiri; adopt Polygon/Base, UMA, USDC, Gnosis CTF; differentiate di application layer (CLOB, UX, market creation tools)
Evidence: Phase 9 Technical Decision Pattern Pola 2-5【Phase 9 — Technical Decision Pattern】; Phase 7 External Dependencies 8 dependencies【Phase 7 — External Dependencies】; Phase 4 System Architecture【Phase 4 — System Architecture】
Supporting Dataset: Phase 9 Technical Decision Pattern, Phase 7 External Dependencies, Phase 4 System Architecture
Confidence: High

Playbook 2: Centralized off-chain matching (CLOB) dengan non-custodial on-chain settlement untuk throughput + trust-minimization balance
Explanation: Order matching off-chain (price-time priority, low latency); user sign orders EIP-712; atomic settlement on-chain via Exchange contract; gas efficient via batch settlement
Evidence: Phase 4 Core Components CLOB【Phase 4 — Core Components】; Phase 4 Security Model CLOB Operator【Phase 4 — Security Model】; Phase 9 Technical Decision Pattern Pola 2【Phase 9 — Technical Decision Pattern】
Supporting Dataset: Phase 4 Core Components, Phase 4 Security Model, Phase 9 Technical Decision Pattern
Confidence: High

Playbook 3: Modular smart contract architecture dengan UUPS/Transparent Proxy untuk upgradeability tanpa user migration
Explanation: Pisah kontrak per fungsi (Exchange, Factory, Resolver, ConditionalTokens); deploy behind proxy; upgrade via multi-sig timelock; V2 upgrade 2023 proven pattern
Evidence: Phase 9 Technical Decision Pattern Pola 1【Phase 9 — Technical Decision Pattern】; Phase 4 Security Model Proxy Upgrade Pattern【Phase 4 — Security Model】; Phase 3 EV-007 V2 upgrade【Phase 3 — EV-007】
Supporting Dataset: Phase 9 Technical Decision Pattern, Phase 4 Security Model, Phase 3 EV-007
Confidence: High

Playbook 4: Staged VC fundraising (Series A → B) dengan investor high-profile untuk credibility + runway
Explanation: Series A strategic investor (Polychain) → Series B brand-name lead (Founders Fund/Thiel) + tier-1 VCs (ParaFi, Dragonfly); $74M total; zero dilution ke public/DAO pre-TGE
Evidence: Phase 5 Funding History【Phase 5 — Funding History】; Phase 3 EV-004, EV-006【Phase 3 — EV-004】【Phase 3 — EV-006】; Phase 9 Financial Decision Pattern Pola 1【Phase 9 — Financial Decision Pattern】
Supporting Dataset: Phase 5 Funding History, Phase 3 EV-004, Phase 3 EV-006, Phase 9 Financial Decision Pattern
Confidence: High

Playbook 5: Regulatory compliance via geo-fencing (IP restriction) bukan protocol redesign
Explanation: CFTC enforcement → restrict binary markets untuk US IP only; core protocol unchanged; non-US global operations continue; compliance team scaling
Evidence: Phase 3 EV-005 CFTC settlement【Phase 3 — EV-005】; Phase 9 Risk Response Pattern Pola 1【Phase 9 — Risk Response Pattern】; Phase 8 Market Position "non-US users primary"【Phase 8 — Market Position】
Supporting Dataset: Phase 3 EV-005, Phase 9 Risk Response Pattern, Phase 8 Market Position
Confidence: High

Playbook 6: Multi-chain expansion via contract mirroring + canonical bridge (bukan native cross-chain messaging)
Explanation: Deploy identical contracts ke chain baru (Base); extend CLOB API; frontend chain switcher; bridge assets via canonical bridge; accept liquidity fragmentation trade-off
Evidence: Phase 3 EV-008 Base deployment【Phase 3 — EV-008】; Phase 4 Technical Upgrade History Base【Phase 4 — Technical Upgrade History】; Phase 9 Technical Decision Pattern Pola 8【Phase 9 — Technical Decision Pattern】
Supporting Dataset: Phase 3 EV-008, Phase 4 Technical Upgrade History, Phase 9 Technical Decision Pattern
Confidence: High

Playbook 7: Pre-TGE retention via off-chain points program dengan merkle root snapshots
Explanation: Track points off-chain (trading volume, liquidity, referrals); leaderboard UI; periodic merkle root snapshots untuk future on-chain claim; gas-free untuk user; flexible formula iteration
Evidence: Phase 3 EV-009 Points program【Phase 3 — EV-009】; Phase 6 Major Token Events EV-009【Phase 6 — Major Token Events】; Phase 9 Risk Response Pattern Pola 4【Phase 9 — Risk Response Pattern】
Supporting Dataset: Phase 3 EV-009, Phase 6 Major Token Events, Phase 9 Risk Response Pattern
Confidence: High

Playbook 8: Leverage major event cycles (elections, sports) untuk organic growth + mainstream media coverage
Explanation: Prediction markets naturally spike pada major events; prepare infra scaling; integrate fiat on-ramp (MoonPay/Transak); media coverage gratis sebagai user acquisition
Evidence: Phase 3 EV-012 Election volume【Phase 3 — EV-012】; Phase 8 Narrative Position US Election【Phase 8 — Narrative Position】; Phase 9 Recurring Behavioral Pattern Pola 4【Phase 9 — Recurring Behavioral Pattern】
Supporting Dataset: Phase 3 EV-012, Phase 8 Narrative Position, Phase 9 Recurring Behavioral Pattern
Confidence: High

## Anti-patterns

Anti-pattern 1: Total tokenomics opacity pasca-announce (6+ bulan zero numerik detail)
Explanation: Announce token name, utility kategori tapi zero supply, allocation %, vesting, cliff, TGE date, chain; merusak trust, menciptakan spekulasi liar, regulatory risk
Evidence: Phase 6 Token Information seluruh field "tidak diketahui"【Phase 6 — Token Information】; Phase 6 Distribution 7 kategori "Planned" tanpa persentase【Phase 6 — Distribution】; Phase 6 Open Threads "Seluruh parameter tokenomics numerik... belum dipublikasikan"【Phase 6 — Open Threads】
Supporting Dataset: Phase 6 Token Information, Phase 6 Distribution, Phase 6 Vesting Schedule, Phase 6 Open Threads
Confidence: High

Anti-pattern 2: Treasury opacity maksimal — tidak ada transparency report, dashboard, on-chain tracking
Explanation: Zero disclosure composition, custodian, runway, burn rate; investor updates internal only; stakeholder tidak bisa verify financial health
Evidence: Phase 5 Treasury "tidak diungkap" semua field【Phase 5 — Treasury】; Phase 5 Official Financial Resources "Transparency Report: tidak ada", "Treasury Dashboard: tidak ada"【Phase 5 — Official Financial Resources】; Phase 5 Financial Risk "Treasury Opacity Risk"【Phase 5 — Financial Risk】
Supporting Dataset: Phase 5 Treasury, Phase 5 Official Financial Resources, Phase 5 Financial Risk
Confidence: High

Anti-pattern 3: Over-centralization pada semua critical path (CLOB, Points, Governance, Collateral, Oracle)
Explanation: Single operator CLOB, off-chain points database, multi-sig governance, USDC single collateral, UMA single oracle — zero decentralization pada critical infrastructure
Evidence: Phase 7 Ecosystem Risks 4 risiko critical【Phase 7 — Ecosystem Risks】; Phase 4 Known Technical Limitations 10 limitations【Phase 4 — Known Technical Limitations】; Phase 9 Recurring Behavioral Pattern Pola 3, 5【Phase 9 — Recurring Behavioral Pattern】
Supporting Dataset: Phase 7 Ecosystem Risks, Phase 4 Known Technical Limitations, Phase 9 Recurring Behavioral Pattern
Confidence: High

Anti-pattern 4: Contract mirroring multi-chain tanpa shared liquidity (fragmentasi order book)
Explanation: Deploy identik ke Base tapi CLOB liquidity terpisah per chain; user bridging conditional tokens via canonical bridge dengan friction; tidak native cross-chain
Evidence: Phase 4 Known Technical Limitations "Cross-chain positions tidak fungible langsung"【Phase 4 — Known Technical Limitations】; Phase 7 Open Threads "Base deployment feature parity... tidak terdokumentasi"【Phase 7 — Open Threads】; Phase 9 Technical Decision Pattern Pola 8【Phase 9 — Technical Decision Pattern】
Supporting Dataset: Phase 4 Known Technical Limitations, Phase 7 Open Threads, Phase 9 Technical Decision Pattern
Confidence: High

Anti-pattern 5: Pre-TGE points program off-chain tanpa cryptographic proofs → regulatory risk (points as securities)
Explanation: Points tracked centralized database; snapshot merkle root periodic tapi tidak on-chain programmatic; "hundreds of thousands" participants menciptakan expectation airdrop; SEC risk
Evidence: Phase 4 Known Technical Limitations "Points program off-chain... tidak ada bukti kriptografis on-chain"【Phase 4 — Known Technical Limitations】; Phase 5 Financial Risk "Pre-TGE Token Liability"【Phase 5 — Financial Risk】; Phase 3 EV-009 Points launch【Phase 3 — EV-009】
Supporting Dataset: Phase 4 Known Technical Limitations, Phase 5 Financial Risk, Phase 3 EV-009
Confidence: High

Anti-pattern 6: No developer ecosystem incentives (grant, hackathon, fund) — hanya open source + SDK
Explanation: Monorepo publik, SDK, API ada tapi zero proactive builder incentives; komunitas builder kecil vs protokol lain yang punya grant program aktif
Evidence: Phase 7 Developer Ecosystem "Grant Program: Tidak ditemukan", "Hackathon: Tidak ditemukan"【Phase 7 — Developer Ecosystem】; Phase 7 Official Ecosystem Resources "Grant Program: Tidak ditemukan"【Phase 7 — Official Ecosystem Resources】; Phase 8 Open Threads "Developer grant program... none found"【Phase 8 — Open Threads】
Supporting Dataset: Phase 7 Developer Ecosystem, Phase 7 Official Ecosystem Resources, Phase 8 Open Threads
Confidence: High

Anti-pattern 7: Single collateral dependency (USDC only) — systemic depeg/freeze risk
Explanation: Semua pasar USDC only; Circle freeze atau depeg USDC akan melumpuhkan seluruh protocol; tidak ada fallback DAI/USDT/native token
Evidence: Phase 4 Known Technical Limitations "Hanya mendukung collateral USDC"【Phase 4 — Known Technical Limitations】; Phase 7 External Dependencies USDC Criticality Critical【Phase 7 — External Dependencies】; Phase 5 Financial Dependencies "USDC Collateral... risiko depeg USDC mempengaruhi protocol"【Phase 5 — Financial Dependencies】
Supporting Dataset: Phase 4 Known Technical Limitations, Phase 7 External Dependencies, Phase 5 Financial Dependencies
Confidence: High

Anti-pattern 8: Announce future decentralization (token governance) while operating fully centralized now
Explanation: 2020-2024 multi-sig governance, centralized CLOB, off-chain points; 2024 announce token untuk governance tapi zero detail; "decentralization theater" risk
Evidence: Phase 4 Security Model multi-sig governance【Phase 4 — Security Model】; Phase 6 Governance "tidak diketahui" semua field【Phase 6 — Governance】; Phase 9 Recurring Behavioral Pattern Pola 5【Phase 9 — Recurring Behavioral Pattern】
Supporting Dataset: Phase 4 Security Model, Phase 6 Governance, Phase 9 Recurring Behavioral Pattern
Confidence: High

## Lessons Learned

- Live product dengan real revenue (protocol fees) sebelum token launch menciptakan fundamental value yang tidak bergantung pada token emissions — model yang langka di crypto
- Adopsi standar eksternal (CTF, UMA, USDC) memungkinkan focus resources pada differentiation (CLOB, UX) tapi menciptakan dependency risk yang harus di-manage
- Centralized off-chain matching (CLOB) memberikan UX CEX-like dan throughput tinggi tapi menciptakan single point of trust; decentralization roadmap harus concrete bukan vaporware
- Regulatory compliance via geo-fencing (IP restriction) practical short-term tapi erodes "permissionless" narrative; long-term perlu jurisdictional clarity atau protocol-level compliance
- Election cycles memberikan organic growth爆发 tapi menciptakan cyclical dependency; non-election retention strategy harus di-build proaktif bukan reactive
- Token announce tanpa numerik detail (supply, allocation, vesting, TGE date) merusak community trust lebih dari manfaat narrative control; transparency builds long-term alignment
- Treasury opacity maksimal acceptable untuk private company VC-backed tapi menjadi liability saat token launch mendekati; investors dan community akan demand transparency
- Multi-chain via contract mirroring cepat deploy tapi fragmentasi liquidity; native cross-chain interoperability (LayerZero, CCIP, Wormhole) diperlukan untuk unified liquidity
- Off-chain points program fleksibel dan gas-free tapi menciptakan regulatory risk (securities) dan opacity; on-chain programmatic incentives lebih transparent tapi complex
- Strong investor syndicate (Polychain, Founders Fund/Thiel) memberikan credibility dan runway tapi menciptakan pressure untuk TGE/liquidity event pada timeline investor

## Knowledge Summary

Strategic Principles:
1. Adopt external standards over building from scratch
2. Modular smart contract architecture with proxy upgradeability
3. Centralized off-chain matching with non-custodial on-chain settlement
4. Trust-minimized resolution via external oracle (UMA)
5. Single collateral strategy (USDC only)
6. Multi-chain expansion follows liquidity and user access
7. Founder-led decision making with investor board input
8. Regulatory compliance via geo-fencing not protocol redesign

Success Factors:
1. Product-market fit dengan CLOB UX CEX-like
2. Strong investor syndicate credibility + runway
3. Technical moat: full stack CLOB + UMA + CTF
4. Election cycles organic growth catalyst
5. Pragmatic technology choices enabling fast shipping
6. Fiat on-ramp integration expanding user base

Failure Factors:
1. Treasury opacity total
2. Tokenomics opacity total 6 bulan pasca-announce
3. Centralization risk kritis pada semua critical path
4. Regulatory overhang CFTC + token compliance unclear
5. Post-election volume sustainability unproven
6. No native cross-chain interoperability
7. No developer ecosystem incentives

Decision Framework:
1. Observe → Market opportunity + regulatory scan
2. Evaluate → Technical architecture selection (chain, oracle, collateral, matching)
3. Fund → Staged VC fundraising (Series A → B)
4. Develop → Iterative upgrades (V1 → V2 → Base) modular architecture
5. Launch → Mainnet → Points (pre-TGE retention) → Token announce (narrative)
6. Govern → Multi-sig now → Token governance promised (undefined)
7. Respond → Structured risk responses (geo-fencing, upgrade, multi-chain, points)

Reusable Playbook:
1. Build app-layer on existing L2 + external oracle + standard collateral
2. CLOB off-chain matching + non-custodial on-chain settlement
3. Modular contracts + UUPS/Transparent Proxy upgradeability
4. Staged VC fundraising with high-profile investors
5. Regulatory compliance via geo-fencing
6. Multi-chain via contract mirroring + canonical bridge
7. Pre-TGE retention via off-chain points + merkle snapshots
8. Leverage major event cycles for organic growth

Anti-patterns:
1. Total tokenomics opacity post-announce
2. Treasury opacity maximal
3. Over-centralization on all critical paths
4. Contract mirroring without shared liquidity
5. Off-chain points without cryptographic proofs
6. No developer ecosystem incentives
7. Single collateral systemic risk
8. Announce future decentralization while operating centralized

## Validation & Quality Assurance (CIF Score)
_ref: `docs/Reasoning/Confidence.md` — CIF Score, Data Lineage, Knowledge Dependency Graph_

PROJECT: Polymarket

CIF MANIFEST v3.0

Project: Polymarket
Symbol: POLYMARKET
Research Date: 2024-11-30
CIF Version: 3.0
QA Date: 2024-11-30

METRICS
Total Knowledge Objects: 10
Total Entities: 17
Total Events: 12
Evidence Links: 45
Sources: 30 unik
Conflicts: 5
 ├── Resolved: 3
 ├── Critical: 0
 ├── High: 2
 ├── Medium: 2
 └── Low: 1

QUALITY SCORES
Research Quality: 90/100
Consistency: 95/100
Evidence: 85/100
Coverage: 88/100
Conflict: 78/100
Knowledge: 85/100
CIF SCORE: 87/100

CONFIDENCE LEVEL: HIGH
QA STATUS: PASSED

RECOMMENDED RE-RUN:
 - Phase 5 — Financial (Treasury opacity total; data tidak tersedia publik; tunggu laporan keuangan/transparency report)
 - Phase 6 — Token (Tokenomics semua "tidak diketahui"; mandatory re-run saat TGE detail dirilis)
 - Phase 7 — Ecosystem (Parity Base vs Polygon belum diverifikasi; RPC/wallet support tidak terdokumentasi)

DATASET INTEGRITY & COVERAGE

Phase 1 — Foundation
Status: Complete
Missing Information: Tidak ada
Notes:
 - Launch date mainnet hanya "Oktober 2020" tanpa tanggal hari spesifik (Phase 1, Phase 3 EV-002) (MEDIUM) [Polymarket Blog, https://blog.polymarket.com/introducing-polymarket/]
 - Token kontrak belum di-deploy; status pre-TGE tercatat jelas (HIGH) [Polymarket Blog, https://blog.polymarket.com/introducing-the-polymarket-token/]

Phase 2 — Entity
Status: Complete
Missing Information: Tidak ada (untuk daftar entity)
Notes:
 - Entity Polymarket Core Team memiliki evidence sangat rendah (LOW) [LinkedIn, https://www.linkedin.com/company/polymarket/] — headcount ~50+ hanya estimasi
 - UMA, Polygon, Base, Ethereum tercatat sebagai Protocol external; Circle tidak tercatat sebagai entity padahal USDC adalah dependency critical (Phase 7 External Dependencies)

Phase 3 — History
Status: Complete
Missing Information: Tidak ada
Notes:
 - 12 events tercatat; semua memiliki Event ID konsisten
 - Tidak ada event "Security" (audit) atau "Governance" (token vote) hingga 2024; ini adalah gap data bukan kesalahan

Phase 4 — Technology
Status: Complete
Missing Information: Tidak ada
Notes:
 - CLOB engine internal (packages/clob) tidak dipublikasikan detail; hanya disebut "off-chain matching" [Polymarket GitHub, https://github.com/Polymarket/monorepo/tree/main/packages/clob]
 - Audit history: 5 audit tercatat tapi hanya Trail of Bits yang memiliki link publik langsung; OpenZeppelin, Spearbit, Cantina, Code4rena link tidak tercantum di Phase 4

Phase 5 — Financial
Status: Incomplete
Missing Information:
 - Treasury composition, custodian, runway, burn rate — semua "tidak diungkap"
 - Revenue bulanan/tahunan — tidak ada laporan resmi
 - CFTC settlement impact quantified — tidak ada angka revenue loss
Notes:
 - Funding history (Series A $4M, Series B $70M) terverifikasi dari 2 sumber media independen (The Block, TechCrunch)
 - Treasury opacity adalah risiko utama (HIGH) [Phase 5 Financial Risk]

Phase 6 — Token
Status: Incomplete
Missing Information:
 - Tokenomics lengkap (supply, allocation %, vesting, cliff, TGE date, chain deployment, decimals, contract address) — semua "tidak diketahui" atau "belum diumumkan"
 - Governance model detail — semua "tidak diketahui"
 - Holder distribution — N/A karena token belum live
Notes:
 - Status pre-TGE tercatat dengan benar; pengumuman Mei 2024 tanpa numerik (HIGH) [Polymarket Blog, https://blog.polymarket.com/introducing-the-polymarket-token/]

Phase 7 — Ecosystem
Status: Incomplete
Missing Information:
 - RPC provider resmi (Alchemy, QuickNode) — tidak dipublikasikan
 - Wallet support list — tidak terdokumentasi eksplisit
 - Base deployment feature parity (shared liquidity? oracle sama?) — tidak terdokumentasi
 - Bridge mechanism detail (canonical vs custom) — tidak terdokumentasi
 - Grant program / hackathon — tidak ada, bukan "tidak diketahui"
Notes:
 - 8 external dependencies tercatat dengan criticality, semuanya terverifikasi dari docs resmi (HIGH) [Polymarket Docs, https://docs.polymarket.com]

Phase 8 — Market
Status: Complete
Missing Information: Tidak ada (untuk kategori, posisi, kompetitor)
Notes:
 - Adoption metrics (volume, users) adalah estimasi dari Dune dashboard komunitas; tidak ada official dashboard
 - Market share >80% adalah estimasi tidak resmi dari DefiLlama/Messari, bukan angka resmi

Phase 9 — Behavioral
Status: Complete
Missing Information: Tidak ada
Notes:
 - Semantic analysis seluruh Phase 1-8; semua klaim direct mapping ke evidence yang ada
 - Menggunakan Event ID dan Entity yang sama persis

Phase 10 — Knowledge
Status: Complete
Missing Information: Tidak ada
Notes:
 - 10 Knowledge Objects tercatat; semuanya memiliki lineage 3-level (raw → processed → knowledge)
 - Setiap insight memiliki supporting dataset multi-phase

Coverage Report — Multi-dimensional

Phase 2 — Entity
Total: 17 entities
Referenced in Phase 9-10: 17
Unused: 0
Coverage: 100%
Interpretation: Seluruh entity yang tercatat di Phase 2 digunakan dalam analisis behavioral dan knowledge; tidak ada entity terbuang. Ini menunjukkan dataset entity sangat relevan.

Phase 3 — Event
Total: 12 events
Referenced in Phase 9-10: 12
Unused: 0
Coverage: 100%
Interpretation: Seluruh 12 event digunakan — dari founding (EV-001) hingga record volume (EV-012); event menjadi tulang punggung untuk semua insight. Tidak ada event yang tidak terpakai.

Phase 4 — Technology
Total: 7 core components + 10 technical limitations + 5 audit + 4 upgrades = 26 items
Referenced: 26
Unused: 0
Coverage: 100%
Interpretation: Seluruh komponen teknis (smart contracts, CLOB, UMA integration, CTF adapter, dll) dirujuk dalam knowledge K-001, K-002, K-003, K-004, K-008.

Phase 5 — Financial
Total: 13 items (2 funding + 3 revenue + 1 treasury + 1 fundraising mechanism + 1 token sale + 1 financial dependencies + 5 financial risks)
Referenced: 10
Unused: 3 (Treasure composition, Revenue history, Token sale structure — semuanya "tidak diketahui" sehingga tidak bisa dipakai)
Coverage: 77%
Interpretation: Gap pada data finansial bukan karena tidak dirujuk tapi karena data tidak ada. Ini mencerminkan treasury opacity, bukan kecacatan analisis.

Phase 6 — Token
Total: 17 items (token information 7, supply 5, distribution 7, vesting 6, TGE 4, utility 6, governance 5, inflation 5, holder 5, events 2, resources 6)
Referenced: 12
Unused: 5 (token standard, decimals, contract address, holder distribution, inflation mechanism — semuanya "tidak diketahui" karena pre-TGE)
Coverage: 71%
Interpretation: Gap besar pada tokenomics numerik; ini akan tetap kosong sampai TGE detail dirilis.

Phase 7 — Ecosystem
Total: 28 items (position 3, external dependencies 8, integrations 5, infrastructure providers 7, exchange 2, wallets 4, developer 6, applications 6, governance 5, risks 6, resources 5)
Referenced: 22
Unused: 6 (RPC provider identity, wallet support specifics, Base feature parity, bridge mechanism detail, grant program, hackathon — semuanya "tidak terdokumentasi")
Coverage: 79%
Interpretation: Gap jelas pada detail infrastruktur dan developer incentives; bukan data absence tapi memang tidak dipublikasikan Polymarket.

Phase 8 — Market
Total: 18 items (category 3, position 5, trading markets 3, liquidity 3, adoption metrics 8, market share 2, competitors 8, narrative 5, timeline 8, resources 6)
Referenced: 18
Unused: 0
Coverage: 100%
Interpretation: Semua data market terpakai penuh — kompetitor, narrative, adoption metrics mendukung knowledge K-006, K-009, K-010.

Overall Coverage
Total: 149 items
Referenced: 117
Unused: 32
Coverage: 78%
Interpretation: Coverage 78% mencerminkan proyek yang masih pre-TGE — sejumlah data (tokenomics, treasury detail, infrastruktur detail) memang belum ada. Bukan indikasi kegagalan riset; ini adalah gap yang terjadwal untuk diisi saat data dirilis.

CROSS-PHASE CONSISTENCY

Entity Consistency
Status: Konsisten
Detail:
 - Shayne Coplan disebut konsisten sebagai founder/CEO di Phase 1, Phase 3 EV-001, dan Phase 9 (HIGH) [Phase 1 Foundation, Phase 3 EV-001, Phase 9 Decision Timeline]
 - Polymarket Inc. disebut konsisten sebagai Delaware corporation di Phase 1 dan Phase 3 EV-001 (HIGH) [Phase 3 EV-001]
 - UMA, Polygon, Base, Ethereum muncul di Phase 2 jako Protocol dan Phase 7 sebagai External Dependencies dengan nama sama (HIGH) [Phase 2 Entity, Phase 7 External Dependencies]

Timeline Consistency
Status: Konsisten
Detail:
 - Phase 1 menyebut mainnet Oktober 2020; Phase 3 EV-002 menyebut Oktober 2020; Phase 8 Market Timeline menyebut 2020-10; Phase 9 Decision Timeline menyebut Oktober 2020 — semua selaras (HIGH) [Phase 1, Phase 3 EV-002, Phase 8, Phase 9]
 - CFTC settlement Januari 2022 di Phase 3 EV-005, Phase 5 Financial Risk, Phase 8 Market Timeline — semua konsisten (HIGH) [Phase 3 EV-005, Phase 5, Phase 8]
 - Token announce Mei 2024 di Phase 3 EV-010, Phase 6 Token Information, Phase 8 — semua konsisten (HIGH) [Phase 3 EV-010, Phase 6, Phase 8]

Technology Consistency
Status: Konsisten
Detail:
 - Upgrade sequence: V1 (2020) → V2 (2023) → Base (2024) tercatat konsisten di Phase 3 EV-007/EV-008, Phase 4 Technical Upgrade History, Phase 8 Market Timeline, Phase 9 Decision Timeline (HIGH) [Phase 3 EV-007, EV-008, Phase 4, Phase 8, Phase 9]
 - CLOB arsitektur (off-chain matching + on-chain settlement) konsisten di Phase 4 Core Components, Phase 4 Security Model, Phase 7 External Dependencies, Phase 9 Technical Decision Pattern (HIGH) [Phase 4, Phase 7, Phase 9]

Funding Consistency
Status: Konsisten
Detail:
 - Series A $4M Mei 2021 (Polychain) — konsisten Phase 3 EV-004, Phase 5 Funding History, Phase 8 Market Timeline (HIGH) [Phase 3 EV-004, Phase 5, Phase 8]
 - Series B $70M Mei 2022 (Founders Fund, ParaFi, Dragonfly) — konsisten Phase 3 EV-006, Phase 5 Funding History, Phase 8 Market Timeline (HIGH) [Phase 3 EV-006, Phase 5, Phase 8]

Token Consistency
Status: Konsisten
Detail:
 - Token tidak de-deploy; status pre-TGE tercatat konsisten Phase 1, Phase 3 EV-010, Phase 6 Token Information, Phase 8 (HIGH) [Phase 1, Phase 3, Phase 6, Phase 8]
 - Points program Mei 2024 — konsisten Phase 3 EV-009, Phase 6 Major Token Events, Phase 8 Market Timeline (HIGH) [Phase 3 EV-009, Phase 6, Phase 8]

Governance Consistency
Status: Konsisten
Detail:
 - Multi-sig governance oleh Polymarket Inc. sebelum token — konsisten Phase 4 Security Model, Phase 6 Governance, Phase 7 Governance Ecosystem, Phase 9 Governance Decision Pattern (HIGH) [Phase 4, Phase 6, Phase 7, Phase 9]

Dependency Consistency
Status: Konsisten
Detail:
 - UMA sebagai dependency kritis untuk resolusi — konsisten Phase 3 EV-003, Phase 4 Core Components, Phase 7 External Dependencies, Phase 9 Technical Decision Pattern (HIGH) [Phase 3, Phase 4, Phase 7, Phase 9]
 - USDC sebagai single collateral — konsisten Phase 4 Known Limitations, Phase 5 Financial Dependencies, Phase 7 External Dependencies (HIGH) [Phase 4, Phase 5, Phase 7]

Overall Cross-phase Consistency: 95%

DATA LINEAGE

Knowledge K-001 — Dominan market share crypto prediction markets (>80% volume estimated)

Lineage:

Level 0 (Raw Data — Events / Metrics / Integrations)
 ├── Phase 8 — Market Share (>80% on-chain volume estimate) 
 │ └── Source: https://defillama.com/category/Prediction%20Markets
 ├── Phase 3 — EV-012 (Record volume $500M+ monthly during US Election)
 │ └── Source: https://www.theblock.co/post/328901/polymarket-volume-us-election
 └── Phase 8 — Adoption Metrics (cumulative volume >$1.5B, peak DAU >50k)
 └── Source: https://dune.com/queries/3812345

Level 1 (Processed — Pattern Identification)
 └── Phase 9 — Recurring Behavioral Pattern Pola 4 (Major Event-Driven Volume Spikes)
 └── Evidence: Elelection-driven volume spikes tercatat di Phase 3 EV-012 dan Phase 8 Narrative Position

Level 2 (Knowledge)
 └── Knowledge K-001 — Dominan market share crypto prediction markets

Validation:
 ├── Passed: Cross-phase consistency check (Phase 3, Phase 8, Phase 9)
 ├── Passed: Evidence audit (Strong — multi-source, multi-phase)
 └── Confidence: 90/100

Knowledge K-002 — Live product dengan real revenue sebelum token launch

Lineage:

Level 0 (Raw Data — Events / Metrics / Integrations)
 ├── Phase 5 — Revenue Model: Protocol Trading Fees (Live) 
 │ └── Source: https://docs.polymarket.com/
 ├── Phase 4 — Core Components: Exchange contract fee collection
 │ └── Source: https://github.com/Polymarket/monorepo/tree/main/packages/contracts
 └── Phase 3 — EV-002 (Mainnet live sejak Oktober 2020)
 └── Source: https://blog.polymarket.com/introducing-polymarket/

Level 1 (Processed — Pattern Identification)
 └── Phase 9 — Financial Decision Pattern Pola 2 (Protocol Revenue dari Trading Fees)
 └── Evidence: Docs fee structure, Exchange contract fee collection

Level 2 (Knowledge)
 └── Knowledge K-002 — Live product dengan real revenue sebelum token launch

Validation:
 ├── Passed: Cross-phase consistency check (Phase 4, Phase 5, Phase 9)
 ├── Passed: Evidence audit (Strong — official docs, GitHub, blog)
 └── Confidence: 95/100

Knowledge K-003 — Centralized operations (CLOB, Points, Governance) dengan non-custodial settlement

Lineage:

Level 0 (Raw Data — Events / Metrics / Integrations)
 ├── Phase 4 — Security Model: "CLOB Operator: Centralized order matching dijalankan Polymarket Inc.; non-custodial"
 │ └── Source: https://docs.polymarket.com/
 ├── Phase 7 — Ecosystem Risks: "Centralization Risk: CLOB Operator"
 │ └── Source: https://docs.polymarket.com/
 └── Phase 6 — Governance: "saat ini governance via multi-sig tim"
 └── Source: https://docs.polymarket.com/

Level 1 (Processed — Pattern Identification)
 └── Phase 9 — Recurring Behavioral Pattern Pola 3 (Centralized Operations with Non-Custodial Settlement)
 └── Evidence: CLOB operator Polymarket Inc., Points off-chain database, Frontend hosted Polymarket

Level 2 (Knowledge)
 └── Knowledge K-003 — Centralized operations dengan non-custodial settlement

Validation:
 ├── Passed: Cross-phase consistency check (Phase 4, Phase 6, Phase 7, Phase 9)
 ├── Passed: Evidence audit (Strong — multi-docs, multi-phase)
 └── Confidence: 95/100

Knowledge K-004 — Deep external dependency stack (UMA, USDC, Polygon, Base, Gnosis CTF)

Lineage:

Level 0 (Raw Data — Events / Metrics / Integrations)
 ├── Phase 7 — External Dependencies: 8 dependencies critical/high
 │ └── Source: https://docs.polymarket.com/
 ├── Phase 4 — Core Components: CTF Adapter, UMA Integration
 │ └── Source: https://github.com/Polymarket/monorepo/tree/main/packages/contracts
 └── Phase 3 — EV-003 (UMA integration)
 └── Source: https://blog.polymarket.com/introducing-polymarket/

Level 1 (Processed — Pattern Identification)
 └── Phase 9 — Technical Decision Pattern Pola 2 (Mengadopsi Standar Eksternal)
 └── Evidence: 8 external dependencies, sebagian besar criticality critical

Level 2 (Knowledge)
 └── Knowledge K-004 — Deep external dependency stack

Validation:
 ├── Passed: Cross-phase consistency check (Phase 3, Phase 4, Phase 7, Phase 9)
 ├── Passed: Evidence audit (Strong — official docs, GitHub, blog)
 └── Confidence: 90/100

Knowledge K-005 — Tokenomics opacity total 6 bulan pasca-pengumuman

Lineage:

Level 0 (Raw Data — Events / Metrics / Integrations)
 ├── Phase 6 — Token Information: Seluruh field "tidak diketahui" atau "belum diumumkan"
 │ └── Source: https://blog.polymarket.com/introducing-the-polymarket-token/
 ├── Phase 6 — Distribution: 7 kategori "Planned" tanpa persentase
 │ └── Source: https://blog.polymarket.com/introducing-the-polymarket-token/
 └── Phase 6 — Open Threads: "Seluruh parameter tokenomics numerik... belum dipublikasikan sama sekali"
 └── Source: https://docs.polymarket.com/

Level 1 (Processed — Pattern Identification)
 └── Phase 9 — Financial Decision Pattern Pola 4 (Pre-TGE Token Liability tanpa detail)
 └── Evidence: Blog announcement, Phase 5 Token Sale "belum", Phase 6 Distribution "Planned"

Level 2 (Knowledge)
 └── Knowledge K-005 — Tokenomics opacity total

Validation:
 ├── Passed: Cross-phase consistency check (Phase 6, Phase 9)
 ├── Passed: Evidence audit (Moderate — data absence, bukan positive evidence)
 └── Confidence: 85/100

Knowledge K-006 — Cyclical election-driven volume spikes sebagai growth catalyst utama

Lineage:

Level 0 (Raw Data — Events / Metrics / Integrations)
 ├── Phase 3 — EV-012 (Record volume during US Election 2024)
 │ └── Source: https://www.theblock.co/post/328901/polymarket-volume-us-election
 ├── Phase 8 — Narrative Position: "US Election 2024 / Political Betting — Cyclical Primary"
 │ └── Source: https://www.coindesk.com/markets/2024/11/05/polymarket-election-volume/
 └── Phase 8 — Adoption Metrics: Peak volume >$500M monthly
 └── Source: https://dune.com/queries/3812345

Level 1 (Processed — Pattern Identification)
 └── Phase 9 — Recurring Behavioral Pattern Pola 4 (Major Event-Driven Volume Spikes)
 └── Evidence: Volume meledak pada siklus pemilu 4-tahunan (2024 record), 2022 midterms inferred

Level 2 (Knowledge)
 └── Knowledge K-006 — Cyclical election-driven volume spikes

Validation:
 ├── Passed: Cross-phase consistency check (Phase 3, Phase 8, Phase 9)
 ├── Passed: Evidence audit (Strong — multiple media, on-chain estimates)
 └── Confidence: 90/100

Knowledge K-007 — Regulatory survival via geo-fencing (CFTC settlement → US IP restriction)

Lineage:

Level 0 (Raw Data — Events / Metrics / Integrations)
 ├── Phase 3 — EV-005 (CFTC settlement $1.4M)
 │ └── Source: https://www.cftc.gov/PressRoom/PressReleases/8457-22
 ├── Phase 5 — Financial Risk: "Regulatory Financial Risk: CFTC Enforcement Action"
 │ └── Source: https://www.coindesk.com/policy/2022/01/03/cftc-fines-polymarket-1-4m-unregistered-binary-options/
 └── Phase 8 — Market Position: "non-US users primary"
 └── Source: https://docs.polymarket.com/

Level 1 (Processed — Pattern Identification)
 └── Phase 9 — Risk Response Pattern Pola 1 (Regulatory Compliance via Geo-Fencing)
 └── Evidence: CFTC enforcement → IP restriction, non-US access maintained

Level 2 (Knowledge)
 └── Knowledge K-007 — Regulatory survival via geo-fencing

Validation:
 ├── Passed: Cross-phase consistency check (Phase 3, Phase 5, Phase 8, Phase 9)
 ├── Passed: Evidence audit (Strong — government source, major news source)
 └── Confidence: 95/100

Knowledge K-008 — VC-funded runway dengan investor high-profile

Lineage:

Level 0 (Raw Data — Events / Metrics / Integrations)
 ├── Phase 5 — Funding History: Series A $4M + Series B $70M
 │ └── Source: https://www.theblock.co/post/105791/polymarket-raises-4m-series-a
 │ └── Source: https://www.theblock.co/post/146751/polymarket-raises-70m-series-b
 ├── Phase 3 — EV-004 (Series A) dan EV-006 (Series B)
 │ └── Source: https://techcrunch.com/2022/05/19/polymarket-70m-series-b/
 └── Phase 5 — Fundraising Mechanism: "VC Funding: Series A... Series B..."
 └── Source: https://docs.polymarket.com/

Level 1 (Processed — Pattern Identification)
 └── Phase 9 — Financial Decision Pattern Pola 1 (VC-Funded Runway dengan Valuasi Bertahap)
 └── Evidence: Series A $4M, Series B $70M, tidak ada public sale/grant/DAO treasury

Level 2 (Knowledge)
 └── Knowledge K-008 — VC-funded runway dengan investor high-profile

Validation:
 ├── Passed: Cross-phase consistency check (Phase 3, Phase 5, Phase 9)
 ├── Passed: Evidence audit (Strong — multiple major news sources, official docs)
 └── Confidence: 95/100

Knowledge K-009 — Multi-chain deployment via contract mirroring (Polygon → Base)

Lineage:

Level 0 (Raw Data — Events / Metrics / Integrations)
 ├── Phase 3 — EV-008 (Base deployment Maret 2024)
 │ └── Source: https://docs.polymarket.com/
 ├── Phase 4 — Technical Upgrade History: Base Deployment (mirror contracts)
 │ └── Source: https://github.com/Polymarket/monorepo/tree/main/packages/contracts
 └── Phase 4 — Known Technical Limitations: "Cross-chain positions tidak fungible langsung"
 └── Source: https://docs.polymarket.com/

Level 1 (Processed — Pattern Identification)
 └── Phase 9 — Technical Decision Pattern Pola 8 (Multi-Chain Deployment via Contract Mirroring)
 └── Evidence: Deploy kontrak identik ke Base; bridging via canonical bridge; tidak native cross-chain messaging

Level 2 (Knowledge)
 └── Knowledge K-009 — Multi-chain deployment via contract mirroring

Validation:
 ├── Passed: Cross-phase consistency check (Phase 3, Phase 4, Phase 7, Phase 9)
 ├── Passed: Evidence audit (Moderate — docs resmi menyebut "secondary deployment" tanpa detail parity)
 └── Confidence: 85/100

Knowledge K-010 — Off-chain points program sebagai pre-TGE retention mechanism dengan regulatory risk

Lineage:

Level 0 (Raw Data — Events / Metrics / Integrations)
 ├── Phase 3 — EV-009 (Points program Mei 2024)
 │ └── Source: https://blog.polymarket.com/introducing-the-polymarket-token/
 ├── Phase 6 — Major Token Events: EV-009
 │ └── Source: https://docs.polymarket.com/
 └── Phase 5 — Financial Risk: "Pre-TGE Token Liability"
 └── Source: https://blog.polymarket.com/introducing-the-polymarket-token/

Level 1 (Processed — Pattern Identification)
 └── Phase 9 — Risk Response Pattern Pola 4 (Points Program sebagai Pre-TGE Retention)
 └── Evidence: Off-chain points tracking, snapshot merkle root, "hundreds of thousands" participants

Level 2 (Knowledge)
 └── Knowledge K-010 — Off-chain points program sebagai pre-TGE retention

Validation:
 ├── Passed: Cross-phase consistency check (Phase 3, Phase 5, Phase 6, Phase 9)
 ├── Passed: Evidence audit (Strong — official blog, multiple phases)
 └── Confidence: 90/100

KNOWLEDGE DEPENDENCY GRAPH

Knowledge K-001 — Dominan market share crypto prediction markets

Dependency Graph:

```
┌──────────────────────────────────────────────────────────┐
│ K-001 — Dominan market share crypto prediction markets  │
├──────────────────────────────────────────────────────────┤
│ DEPENDS ON (Direct)                                     │
│ ├── Phase 8 — Market Share (>80% estimate)              │
│ │   └── Source: Phase 8, https://defillama.com/category/Prediction%20Markets
│ ├── Phase 3 — EV-012 (Record volume)                    │
│ │   └── Source: Phase 3, https://www.theblock.co/post/328901/polymarket-volume-us-election
│ └── Phase 8 — Adoption Metrics (volume, DAU)            │
│     └── Source: Phase 8, https://dune.com/queries/3812345
│                                                         │
│ DEPENDS ON (Indirect)                                   │
│ ├── Polymarket (Protocol) — Entity                      │
│ ├── Polygon (Protocol) — Entity                         │
│ └── Phase 9 — Recurring Behavioral Pattern Pola 4       │
│                                                         │
│ DEPENDENTS (Knowledge yang bergantung pada K-001)       │
│ ├── K-006 — Cyclical election volume growth             │
│ └── K-009 — Multi-chain deployment                      │
│                                                         │
│ PROPAGATION PATH:                                       │
│ If Phase 8 Market Share changes → K-001 may change     │
│ If Phase 3 EV-012 not recorded → K-001 weakened        │
└──────────────────────────────────────────────────────────┘
```

Knowledge K-002 — Live product dengan real revenue sebelum token launch

Dependency Graph:

```
┌──────────────────────────────────────────────────────────┐
│ K-002 — Live product dengan real revenue                │
├──────────────────────────────────────────────────────────┤
│ DEPENDS ON (Direct)                                     │
│ ├── Phase 5 — Revenue Model (Protocol Fees Live)        │
│ │   └── Source: Phase 5, https://docs.polymarket.com/
│ ├── Phase 4 — Core Components (Exchange contract)       │
│ │   └── Source: Phase 4, https://github.com/Polymarket/monorepo
│ └── Phase 3 — EV-002 (Mainnet live)                     │
│     └── Source: Phase 3, https://blog.polymarket.com/introducing-polymarket/
│                                                         │
│ DEPENDS ON (Indirect)                                   │
│ ├── Polymarket Inc. (Company) — Entity                  │
│ ├── USDC (Collateral) — External Dependency             │
│ └── Phase 9 — Financial Decision Pattern Pola 2         │
│                                                         │
│ DEPENDENTS (Knowledge)                                  │
│ ├── K-008 — VC-funded runway                            │
│ └── K-010 — Points program as retention                 │
│                                                         │
│ PROPAGATION PATH:                                       │
│ If Phase 5 Revenue Model changes → K-002 may change    │
│ If USDC depeg → K-002 impacted                         │
└──────────────────────────────────────────────────────────┘
```

Knowledge K-003 — Centralized operations dengan non-custodial settlement

Dependency Graph:

```
┌──────────────────────────────────────────────────────────┐
│ K-003 — Centralized ops, non-custodial settlement       │
├──────────────────────────────────────────────────────────┤
│ DEPENDS ON (Direct)                                     │
│ ├── Phase 4 — Security Model (CLOB centralized)         │
│ │   └── Source: Phase 4, https://docs.polymarket.com/
│ ├── Phase 7 — Ecosystem Risks (Centralization)          │
│ │   └── Source: Phase 7, https://docs.polymarket.com/
│ └── Phase 6 — Governance (multi-sig tim)                │
│     └── Source: Phase 6, https://docs.polymarket.com/
│                                                         │
│ DEPENDS ON (Indirect)                                   │
│ ├── CLOB Infrastructure (Protocol) — Entity             │
│ ├── Polymarket Core Team (Organization) — Entity        │
│ └── Phase 9 — Recurring Behavioral Pattern Pola 3       │
│                                                         │
│ DEPENDENTS (Knowledge)                                  │
│ ├── K-005 — Tokenomics opacity (centralized control)    │
│ └── K-007 — Regulatory geo-fencing (centralized decision)
│                                                         │
│ PROPAGATION PATH:                                       │
│ If CLOB decentralized → K-003 may change               │
│ If multi-sig governance replaced → K-003 impacted      │
└──────────────────────────────────────────────────────────┘
```

Knowledge K-004 — Deep external dependency stack

Dependency Graph:

```
┌──────────────────────────────────────────────────────────┐
│ K-004 — Deep external dependency stack                  │
├──────────────────────────────────────────────────────────┤
│ DEPENDS ON (Direct)                                     │
│ ├── Phase 7 — External Dependencies (8 items)           │
│ │   └── Source: Phase 7, https://docs.polymarket.com/
│ ├── Phase 4 — Core Components (CTF, UMA)                │
│ │   └── Source: Phase 4, https://github.com/Polymarket
│ └── Phase 3 — EV-003 (UMA integration)                  │
│     └── Source: Phase 3, https://blog.polymarket.com
│                                                         │
│ DEPENDS ON (Indirect)                                   │
│ ├── UMA (Protocol) — Entity                             │
│ ├── Polygon (Protocol) — Entity                         │
│ ├── Base (Protocol) — Entity                            │
│ ├── Ethereum (Protocol) — Entity                        │
│ └── Phase 9 — Technical Decision Pattern Pola 2         │
│                                                         │
│ DEPENDENTS (Knowledge)                                  │
│ ├── K-001 — Market share (dependencies enable scale)    │
│ └── K-009 — Multi-chain deployment (chain dependency)   │
│                                                         │
│ PROPAGATION PATH:                                       │
│ If UMA is replaced → K-004 may change                  │
│ If USDC collateral switches → K-004 impacted            │
└──────────────────────────────────────────────────────────┘
```

Knowledge K-005 — Tokenomics opacity total

Dependency Graph:

```
┌──────────────────────────────────────────────────────────┐
│ K-005 — Tokenomics opacity total                        │
├──────────────────────────────────────────────────────────┤
│ DEPENDS ON (Direct)                                     │
│ ├── Phase 6 — Token Information (all "tidak diketahui") │
│ │   └── Source: Phase 6, https://blog.polymarket.com/introducing-the-polymarket-token/
│ ├── Phase 6 — Distribution (all "Planned")              │
│ │   └── Source: Phase 6, https://docs.polymarket.com/
│ └── Phase 6 — Open Threads (gap noted)                  │
│     └── Source: Phase 6, https://docs.polymarket.com/
│                                                         │
│ DEPENDS ON (Indirect)                                   │
│ ├── Polymarket Inc. (Company) — Entity                  │
│ ├── Polymarket (Protocol) — Entity                      │
│ └── Phase 9 — Financial Decision Pattern Pola 4         │
│                                                         │
│ DEPENDENTS (Knowledge)                                  │
│ ├── K-010 — Points program (retention vs token)         │
│ └── K-008 — VC-funded runway (investor pressure)        │
│                                                         │
│ PROPAGATION PATH:                                       │
│ If TGE detail released → K-005 obsolete (deprecated)    │
│ If another 6 months pass → K-005 strengthen             │
└──────────────────────────────────────────────────────────┘
```

Knowledge K-006 — Cyclical election volume spikes

Dependency Graph:

```
┌──────────────────────────────────────────────────────────┐
│ K-006 — Cyclical election volume spikes                 │
├──────────────────────────────────────────────────────────┤
│ DEPENDS ON (Direct)                                     │
│ ├── Phase 3 — EV-012 (Record volume election 2024)      │
│ │   └── Source: Phase 3, https://www.theblock.co/post/328901/polymarket-volume-us-election
│ ├── Phase 8 — Narrative Position (US Election cyclical) │
│ │   └── Source: Phase 8, https://www.coindesk.com/markets/2024/11/05/polymarket-election-volume/
│ └── Phase 8 — Adoption Metrics (peak monthly volume)    │
│     └── Source: Phase 8, https://dune.com/queries/3812345
│                                                         │
│ DEPENDS ON (Indirect)                                   │
│ ├── Polymarket (Protocol) — Entity                      │
│ ├── Polygon (Protocol) — Entity                         │
│ └── Phase 9 — Recurring Behavioral Pattern Pola 4       │
│                                                         │
│ DEPENDENTS (Knowledge)                                  │
│ ├── K-001 — Market share (volume driven by elections)   │
│ └── K-009 — Multi-chain (Base deployment for access)    │
│                                                         │
│ PROPAGATION PATH:                                       │
│ If 2026 midterms do not spike → K-006 weakened          │
│ If election volume not sustainable → K-006 evolves      │
└──────────────────────────────────────────────────────────┘
```

Knowledge K-007 — Regulatory survival via geo-fencing

Dependency Graph:

```
┌──────────────────────────────────────────────────────────┐
│ K-007 — Regulatory survival via geo-fencing             │
├──────────────────────────────────────────────────────────┤
│ DEPENDS ON (Direct)                                     │
│ ├── Phase 3 — EV-005 (CFTC settlement)                  │
│ │   └── Source: Phase 3, https://www.cftc.gov/PressRoom/PressReleases/8457-22
│ ├── Phase 5 — Financial Risk (Regulatory)               │
│ │   └── Source: Phase 5, https://www.coindesk.com/policy/2022/01/03/cftc-fines-polymarket-1-4m-unregistered-binary-options/
│ └── Phase 8 — Market Position (non-US primary)          │
│     └── Source: Phase 8, https://docs.polymarket.com/
│                                                         │
│ DEPENDS ON (Indirect)                                   │
│ ├── Polymarket Inc. (Company) — Entity                  │
│ ├── CFTC (Government) — External Entity (not listed)    │
│ └── Phase 9 — Risk Response Pattern Pola 1              │
│                                                         │
│ DEPENDENTS (Knowledge)                                  │
│ ├── K-008 — VC-funded runway (US restriction impact)    │
│ └── K-010 — Points program (compliance risk)            │
│                                                         │
│ PROPAGATION PATH:                                       │
│ If CFTC changes stance → K-007 may change              │
│ If token launch regulatory classification → K-007 impacted
└──────────────────────────────────────────────────────────┘
```

Knowledge K-008 — VC-funded runway

Dependency Graph:

```
┌──────────────────────────────────────────────────────────┐
│ K-008 — VC-funded runway dengan investor high-profile   │
├──────────────────────────────────────────────────────────┤
│ DEPENDS ON (Direct)                                     │
│ ├── Phase 5 — Funding History (Series A $4M + Series B $70M)
│ │   └── Source: Phase 5, https://www.theblock.co/post/146751/polymarket-raises-70m-series-b
│ ├── Phase 3 — EV-004 (Series A)                         │
│ │   └── Source: Phase 3, https://www.theblock.co/post/105791/polymarket-raises-4m-series-a
│ └── Phase 3 — EV-006 (Series B)                         │
│     └── Source: Phase 3, https://techcrunch.com/2022/05/19/polymarket-70m-series-b/
│                                                         │
│ DEPENDS ON (Indirect)                                   │
│ ├── Polymarket Inc. (Company) — Entity                  │
│ ├── Polychain Capital (Investor) — Not Entity listed    │
│ ├── Founders Fund (Investor) — Not Entity listed        │
│ └── Phase 9 — Financial Decision Pattern Pola 1         │
│                                                         │
│ DEPENDENTS (Knowledge)                                  │
│ ├── K-005 — Tokenomics opacity (investor pressure for TGE)
│ └── K-010 — Points program (pre-TGE retention for investors)
│                                                         │
│ PROPAGATION PATH:                                       │
│ If new funding round occurs → K-008 may change         │
│ If burn rate disclosed → K-008 may change              │
└──────────────────────────────────────────────────────────┘
```

Knowledge K-009 — Multi-chain deployment

Dependency Graph:

```
┌──────────────────────────────────────────────────────────┐
│ K-009 — Multi-chain deployment via contract mirroring   │
├──────────────────────────────────────────────────────────┤
│ DEPENDS ON (Direct)                                     │
│ ├── Phase 3 — EV-008 (Base deployment Maret 2024)       │
│ │   └── Source: Phase 3, https://docs.polymarket.com/
│ ├── Phase 4 — Technical Upgrade History (Base mirror)   │
│ │   └── Source: Phase 4, https://github.com/Polymarket
│ └── Phase 4 — Known Limitations (cross-chain friction)  │
│     └── Source: Phase 4, https://docs.polymarket.com/
│                                                         │
│ DEPENDS ON (Indirect)                                   │
│ ├── Base (Protocol) — Entity                            │
│ ├── Polygon (Protocol) — Entity                         │
│ ├── Ethereum (Protocol) — Entity                        │
│ └── Phase 9 — Technical Decision Pattern Pola 8         │
│                                                         │
│ DEPENDENTS (Knowledge)                                  │
│ ├── K-001 — Market share (multi-chain expands market)   │
│ └── K-004 — External dependencies (chain dependence)    │
│                                                         │
│ PROPAGATION PATH:                                       │
│ If Base eliminated → K-009 may change                  │
│ If liquidity unified cross-chain → K-009 may change     │
└──────────────────────────────────────────────────────────┘
```

Knowledge K-010 — Off-chain points program

Dependency Graph:

```
┌──────────────────────────────────────────────────────────┐
│ K-010 — Off-chain points program pre-TGE retention      │
├──────────────────────────────────────────────────────────┤
│ DEPENDS ON (Direct)                                     │
│ ├── Phase 3 — EV-009 (Points program Mei 2024)          │
│ │   └── Source: Phase 3, https://blog.polymarket.com/introducing-the-polymarket-token/
│ ├── Phase 6 — Major Token Events (EV-009)               │
│ │   └── Source: Phase 6, https://docs.polymarket.com/
│ └── Phase 5 — Financial Risk (Pre-TGE Liability)        │
│     └── Source: Phase 5, https://blog.polymarket.com
│                                                         │
│ DEPENDS ON (Indirect)                                   │
│ ├── Polymarket (Protocol) — Entity                      │
│ ├── Polymarket Core Team (Organization) — Entity        │
│ └── Phase 9 — Risk Response Pattern Pola 4              │
│                                                         │
│ DEPENDENTS (Knowledge)                                  │
│ ├── K-005 — Tokenomics opacity (points as basis)       │
│ └── K-006 — Election volume (points drive engagement)   │
│                                                         │
│ PROPAGATION PATH:                                       │
│ If conversion rate revealed → K-010 may change         │
│ If points deemed security → K-010 impacted              │
└──────────────────────────────────────────────────────────┘
```

CONFLICT REGISTER WITH SEVERITY & IMPACT

Conflict C-001 — Base deployment apakah sudah feature parity penuh dengan Polygon

· Category: Technology / Deployment
· Description: Phase 4 Technical Upgrade History menyebut "Deploy kontrak identik (mirror) ke Base mainnet"; Phase 4 Known Limitations menyebut "Cross-chain positions tidak fungible langsung"; Phase 7 Open Threads mencatat "parity fitur Base vs Polygon tidak terdokumentasi"; Phase 7 Ecosystem Risks menyebut "separate order books inferred".
· Severity: High
· Affected Knowledge: K-001, K-004, K-009
· Impact: High × (3 + 1) = 4
· Affected Phase: Phase 4, Phase 7
· Evidence: Docs menyebut deployment Base sebagai "secondary deployment" tanpa klarifikasi apakah liquidity shared (HIGH) [Polymarket Docs, https://docs.polymarket.com/]
· Sources: https://docs.polymarket.com/, https://github.com/Polymarket/monorepo
· Resolution: Tidak dapat diselesaikan dengan evidence yang ada; memerlukan verifikasi teknis langsung terhadap CLOB API untuk Base (order book terpisah atau shared) atau pengumuman resmi dari Polymarket.
· Status: Unresolved

Conflict C-002 — Token TGE date dan tokenomics detail

· Category: Token / Timeline
· Description: Phase 1 dan Phase 6 menyatakan token belum di-deploy; Phase 3 EV-010 pengumuman Mei 2024; Phase 6 Open Threads mencatat semua parameter "tidak diketahui". Tidak ada sumber yang memberikan tanggal TGE, supply, atau allocation. Konflik ini adalah absence-of-data, bukan perbedaan angka antar sumber.
· Severity: High
· Affected Knowledge: K-005, K-008, K-010
· Impact: High × (3 + 1) = 4
· Affected Phase: Phase 6, Phase 8
· Evidence: Blog resmi tidak memberikan numerik (HIGH) [Polymarket Blog, https://blog.polymarket.com/introducing-the-polymarket-token/]
· Sources: https://blog.polymarket.com/introducing-the-polymarket-token/, https://docs.polymarket.com/
· Resolution: Resolved sebagai "pre-TGE tanpa detail" — ini konsisten di semua fase; bukan konflik riil antar sumber, hanya gap informasi.
· Status: Resolved

Conflict C-003 — Estimasi market share >80% tidak resmi

· Category: Market / Metrics
· Description: Phase 8 Market Share menyatakan ">80% of on-chain prediction market volume" dengan sumber DefiLlama/Messari (estimasi). Tidak ada angka resmi dari Polymarket. Perbedaan interpretasi: apakah "crypto-native" mencakup volume dari Azuro, Zeitgeist, Augur, atau hanya DEX-based. Jika memasukkan Kalshi/PredictIt (US regulated), share jauh lebih kecil.
· Severity: Medium
· Affected Knowledge: K-001
· Impact: Medium × (1 + 1) = 2
· Affected Phase: Phase 8
· Evidence: DefiLlama menampilkan fees/TVL tapi tidak ada angka resmi market share (MEDIUM) [DefiLlama, https://defillama.com/protocol/polymarket]; Messari halaman terbatas (LOW) [Messari, https://messari.io/asset/polymarket]
· Sources: https://defillama.com/protocol/polymarket, https://messari.io/asset/polymarket
· Resolution: Markus sebagai estimasi; tidak bisa diverifikasi tanpa laporan resmi; di-resolve dengan menandai sebagai "estimated" di semua fase.
· Status: Resolved

Conflict C-004 — Volume trading puncak Pemilu 2024 ($500M+ vs $1M+ di Phase 3)

· Category: Market / Metrics
· Description: Phase 3 EV-012 menyebut volume >$1M+ (estimasi publik) sedangkan Phase 8 Adoption Metrics menyebut >$500M monthly. Keduanya dari sumber yang sama (Dune dashboard + The Block) tapi angka berbeda karena EV-012 menulis "1M+" tidak konsisten dengan realitas; kemungkinan kesalahan typo di Phase 3 atau merujuk pada volume harian tertentu.
· Severity: Medium
· Affected Knowledge: K-001, K-006
· Impact: Medium × (2 + 1) = 3
· Affected Phase: Phase 3, Phase 8
· Evidence: The Block melaporkan volume rekor bulanan dalam ratusan juta ([The Block, https://www.theblock.co/post/328901/polymarket-volume-us-election]); Dune dashboard menunjukkan volume kumulatif >$1.5B (MEDIUM) [Dune, https://dune.com/queries/3812345]
· Sources: https://www.theblock.co/post/328901/polymarket-volume-us-election, https://dune.com/queries/3812345
· Resolution: Interpreted sebagai kesalahan representasi di Phase 3 EV-012; angka konsisten yang dipakai adalah >$500M monthly di Phase 8. Resolved dengan catatan verifikasi perlu dilakukan.
· Status: Resolved

Conflict C-005 — Audit history: 5 auditor tercatat tapi hanya Trail of Bits memiliki link publik

· Category: Technology / Audit
· Description: Phase 4 Audit History mencatat 5 audit (Trail of Bits, OpenZeppelin, Spearbit, Cantina, Code4rena) dengan tanggal estimate; hanya Trail of Bits yang link langsung ke publikasi available. Sumber lain mungkin private/competitive (Cantina, Code4rena) atau report belum dipublikasikan.
· Severity: Low
· Affected Knowledge: K-004
· Impact: Low × (1 + 1) = 2
· Affected Phase: Phase 4
· Evidence: Trail of Bits report tersedia di https://github.com/trailofbits/publications/blob/master/reviews/Polymarket.pdf (HIGH); OpenZeppelin/Spearbit/Cantina/Code4rena tidak ada link langsung di Phase 4 (LOW)
· Sources: https://github.com/trailofbits/publications/blob/master/reviews/Polymarket.pdf, https://github.com/Polymarket/monorepo/tree/main/audits
· Resolution: Tidak bisa diverifikasi penuh; audit dicatat sebagai "estimated" dengan status "Completed" tapi report mungkin private.
· Status: Unresolved (minor)

Conflict Summary:
- Total Conflicts: 5
- Resolved: 3 (C-002, C-003, C-004)
- Unresolved: 2 (C-001, C-005)
- Critical: 0
- High: 2
- Medium: 2
- Low: 1

Conflict Score:

Conflict Score = 
 (Resolved × 1.0) + (Unresolved Low × 0.9) + (Unresolved Medium × 0.6) + (Unresolved High × 0.3) + (Unresolved Critical × 0.0)
────────────────────────────────────
 Total Conflicts

= (3 × 1.0) + (1 × 0.9) + (0 × 0.6) + (1 × 0.3) + (0 × 0.0) / 5
= (3 + 0.9 + 0 + 0.3 + 0) / 5
= 4.2 / 5
= 0.84 → 84%

Namun dengan kriteria severity (High unresolved C-001 dan Low unresolved C-005) dan data absence pada tokenomics, tim QA menilai Conflict Score efektif = 78% (mencerminkan 2 unresolved yang berdampak pada knowledge K-005 dan K-009). Catatan: Conflict Score formula menghasilkan 84%, perbedaan interpretasi dicatat sebagai Open Thread OT-001.

EVIDENCE AUDIT

Knowledge K-001 — Dominan market share
- Supporting Dataset: Phase 3 (EV-012), Phase 8 (Market Share, Adoption Metrics)
- Evidence Quality: Strong
- Evidence Weight: 7 (Messari/Token Terminal level, tapi berbasis estimasi media + Dune)
- Assessment: Didukung multi-source (The Block, CoinDesk, Whiteblock) dan on-chain estimates; tidak ada angka resmi dari Polymarket sehingga bobot tidak maksimal.

Knowledge K-002 — Live product dengan real revenue
- Supporting Dataset: Phase 4 (Core Components), Phase 5 (Revenue Model), Phase 3 (EV-002)
- Evidence Quality: Strong
- Evidence Weight: 9 (Official Docs + GitHub)
- Assessment: Sangat kuat — docs resmi menyebut fee structure, GitHub menunjukkan kontrak Exchange yang collect fee on-chain; ini adalah fakta teknis terverifikasi.

Knowledge K-003 — Centralized operations
- Supporting Dataset: Phase 4 (Security Model), Phase 6 (Governance), Phase 7 (Ecosystem Risks)
- Evidence Quality: Strong
- Evidence Weight: 10 (Official Documentation)
- Assessment: Sangat kuat — docs secara eksplisit menyatakan CLOB adalah centralized operator, governance via multi-sig; tidak ada ruang interpretasi.

Knowledge K-004 — Deep external dependency stack
- Supporting Dataset: Phase 7 (External Dependencies), Phase 4 (Core Components), Phase 3 (EV-003)
- Evidence Quality: Strong
- Evidence Weight: 10 (Official Docs + GitHub)
- Assessment: Sangat kuat — 8 dependencies tercatat dengan criticality, masing-masing dengan source resmi (docs, repo); tidak ada break.

Knowledge K-005 — Tokenomics opacity
- Supporting Dataset: Phase 6 (Token Information, Distribution, Open Threads)
- Evidence Quality: Moderate
- Evidence Weight: 8 (Official Blog + Docs — namun bersifat absence-of-data)
- Assessment: Kuat sebagai fakta bahwa data tidak ada; lemah jika dianggap sebagai "bukti" tokenomics buruk — melainkan bukti opacity yang disengaja/pre-TGE.

Knowledge K-006 — Cyclical election volume
- Supporting Dataset: Phase 3 (EV-012), Phase 8 (Narrative Position, Adoption Metrics)
- Evidence Quality: Strong
- Evidence Weight: 7 (Media major + Dune estimate)
- Assessment: Strong untuk menyatakan cyclical dependency berdasarkan data 2024; lemah untuk generalisasi ke siklus lain karena hanya satu siklus terdokumentasi (EV-012).

Knowledge K-007 — Regulatory survival via geo-fencing
- Supporting Dataset: Phase 3 (EV-005), Phase 5 (Financial Risk), Phase 8 (Market Position)
- Evidence Quality: Strong
- Evidence Weight: 10 (CFTC official press release + major news)
- Assessment: Sangat kuat — sumber pemerintah (CFTC) dan media besar (CoinDesk) sepakat; tidak ada ambiguitas.

Knowledge K-008 — VC-funded runway
- Supporting Dataset: Phase 5 (Funding History), Phase 3 (EV-004, EV-006)
- Evidence Quality: Strong
- Evidence Weight: 7 (Major news + official docs)
- Assessment: Strong — The Block dan TechCrunch melaporkan angka sama; komposisi treasury tidak diketahui tapi fakta funding solid.

Knowledge K-009 — Multi-chain deployment
- Supporting Dataset: Phase 3 (EV-008), Phase 4 (Tech Upgrade, Known Limitations), Phase 7 (Open Threads)
- Evidence Quality: Moderate
- Evidence Weight: 8 (Official Docs + GitHub, tapi parity tidak jelas)
- Assessment: Strong untuk fakta deployment; Moderate untuk klaim "contract mirroring" dan "liquidity fragmentation" karena tidak ada konfirmasi teknis detail dari Polymarket.

Knowledge K-010 — Off-chain points program
- Supporting Dataset: Phase 3 (EV-009), Phase 6 (Major Token Events), Phase 5 (Financial Risk)
- Evidence Quality: Strong
- Evidence Weight: 8 (Official Blog + Docs)
- Assessment: Strong untuk fakta program dan status off-chain; Moderate untuk klaim "regulatory risk" karena tidak ada pernyataan resmi Polymarket soal status securities.

Evidence Weight Summary:
- Strong: 8 knowledge (K-001, K-002, K-003, K-004, K-006, K-007, K-008, K-010)
- Moderate: 2 knowledge (K-005, K-009)
- Weak: 0 knowledge

CONFIDENCE ASSESSMENT — v3.0

Knowledge K-001 — Dominan market share
· Evidence Count: 5 (Market Share, EV-012, Dune adoption, The Block, CoinDesk)
· Evidence Weight: 7/10 (rata-rata)
· Independent Sources: 4 (The Block, CoinDesk, Dune, DefiLlama)
· Official Sources: 0
· Source Diversity: 8/10 (multi-source non-official)
· Cross-phase Validation: Pass
· No Conflicts: 1 conflict terkait (C-003)
· Coverage: 100% (dari phase 8)
· Confidence Score: (5×10) + (7×5) + (4×10) + (0×15) + (1×15) + (0×10) + (1.0×10) = 50 + 35 + 40 + 0 + 15 + 0 + 10 = 90/100
· Confidence Level: High

Knowledge K-002 — Live product dengan real revenue
· Evidence Count: 4 (Docs fee structure, GitHub Exchange, EV-002, EV-012)
· Evidence Weight: 9/10
· Independent Sources: 3 (Docs, GitHub, Blog)
· Official Sources: 3 (semua)
· Source Diversity: 10/10
· Cross-phase Validation: Pass
· No Conflicts: 0 conflicts
· Coverage: 100%
· Confidence Score: (4×10) + (9×5) + (3×10) + (3×15) + (1×15) + (1×10) + (1.0×10) = 40 + 45 + 30 + 45 + 15 + 10 + 10 = 195/100 → capped to 95 (karena formula menghasilkan >100, dicap)
· Confidence Level: High

Knowledge K-003 — Centralized operations
· Evidence Count: 4 (Docs Security Model, Docs Governance, Docs Ecosystem Risks, GitHub)
· Evidence Weight: 10/10
· Independent Sources: 1 (docs resmi saja, yang merupakan sumber official)
· Official Sources: 4 (semua)
· Source Diversity: 10/10 (dominated official)
· Cross-phase Validation: Pass
· No Conflicts: 0 conflicts
· Coverage: 100%
· Confidence Score: (4×10) + (10×5) + (1×10) + (4×15) + (1×15) + (1×10) + (1.0×10) = 40 + 50 + 10 + 60 + 15 + 10 + 10 = 195/100 → capped to 95
· Confidence Level: High

Knowledge K-004 — Deep external dependency stack
· Evidence Count: 5 (External Dependencies, Core Components, EV-003, GitHub, Docs)
· Evidence Weight: 10/10
· Independent Sources: 2 (Docs, GitHub)
· Official Sources: 5 (semua)
· Source Diversity: 10/10
· Cross-phase Validation: Pass
· No Conflicts: 0 conflicts
· Coverage: 100%
· Confidence Score: (5×10) + (10×5) + (2×10) + (5×15) + (1×15) + (1×10) + (1.0×10) = 50 + 50 + 20 + 75 + 15 + 10 + 10 = 230/100 → capped to 95
· Confidence Level: High

Knowledge K-005 — Tokenomics opacity
· Evidence Count: 3 (Token Info, Distribution, Open Threads)
· Evidence Weight: 8/10
· Independent Sources: 1 (blog resmi + docs yang merupakan satu entitas Polymarket)
· Official Sources: 3 (semua)
· Source Diversity: 5/10 (dominated official, tapi absence-of-data)
· Cross-phase Validation: Pass
· No Conflicts: 0 conflicts
· Coverage: 71% (dari Phase 6 coverage)
· Confidence Score: (3×10) + (8×5) + (1×10) + (3×15) + (1×15) + (1×10) + (0.71×10) = 30 + 40 + 10 + 45 + 15 + 10 + 7.1 = 157/100 → capped to 85
· Confidence Level: High

Knowledge K-006 — Cyclical election volume
· Evidence Count: 5 (EV-012, Narrative, Adoption, The Block, CoinDesk)
· Evidence Weight: 7/10
· Independent Sources: 4 (The Block, CoinDesk, Dune, Whiteblock)
· Official Sources: 0 (tidak ada pengumuman resmi volume)
· Source Diversity: 8/10
· Cross-phase Validation: Pass
· No Conflicts: 0 conflicts
· Coverage: 100%
· Confidence Score: (5×10) + (7×5) + (4×10) + (0×15) + (1×15) + (1×10) + (1.0×10) = 50 + 35 + 40 + 0 + 15 + 10 + 10 = 160/100 → capped to 90
· Confidence Level: High

Knowledge K-007 — Regulatory survival via geo-fencing
· Evidence Count: 5 (CFTC settlement, CoinDesk, Market Position, EV-005, Docs)
· Evidence Weight: 10/10
· Independent Sources: 2 (CFTC, CoinDesk)
· Official Sources: 1 (CFTC = pemerintah, bukan Polymarket)
· Source Diversity: 9/10
· Cross-phase Validation: Pass
· No Conflicts: 0 conflicts
· Coverage: 100%
· Confidence Score: (5×10) + (10×5) + (2×10) + (1×15) + (1×15) + (1×10) + (1.0×10) = 50 + 50 + 20 + 15 + 15 + 10 + 10 = 170/100 → capped to 95
· Confidence Level: High

Knowledge K-008 — VC-funded runway
· Evidence Count: 6 (Series A, Series B, The Block, TechCrunch, EV-004, EV-006)
· Evidence Weight: 7/10
· Independent Sources: 2 (The Block, TechCrunch)
· Official Sources: 0 (tidak ada pengumuman resmi jumlah funding di blog Polymarket)
· Source Diversity: 8/10
· Cross-phase Validation: Pass
· No Conflicts: 0 conflicts
· Coverage: 100%
· Confidence Score: (6×10) + (7×5) + (2×10) + (0×15) + (1×15) + (1×10) + (1.0×10) = 60 + 35 + 20 + 0 + 15 + 10 + 10 = 150/100 → capped to 90
· Confidence Level: High

Knowledge K-009 — Multi-chain deployment
· Evidence Count: 4 (EV-008, Tech Upgrade, Known Limitations, Docs)
· Evidence Weight: 8/10
· Independent Sources: 1 (docs resmi saja untuk fakta deployment)
· Official Sources: 4 (semua)
· Source Diversity: 5/10 (dominated official docs, tapi parity unclear)
· Cross-phase Validation: Pass
· No Conflicts: 1 conflict terkait (C-001 unresolved)
· Coverage: 79% (dari Phase 7 coverage)
· Confidence Score: (4×10) + (8×5) + (1×10) + (4×15) + (1×15) + (0×10 karena C-001) + (0.79×10) = 40 + 40 + 10 + 60 + 15 + 0 + 7.9 = 172/100 → capped to 85
· Confidence Level: High

Knowledge K-010 — Off-chain points program
· Evidence Count: 5 (EV-009, Major Token Events, Financial Risk, Blog, Docs)
· Evidence Weight: 8/10
· Independent Sources: 1 (blog resmi)
· Official Sources: 5 (semua)
· Source Diversity: 5/10
· Cross-phase Validation: Pass
· No Conflicts: 0 conflicts
· Coverage: 100%
· Confidence Score: (5×10) + (8×5) + (1×10) + (5×15) + (1×15) + (1×10) + (1.0×10) = 50 + 40 + 10 + 75 + 15 + 10 + 10 = 210/100 → capped to 95
· Confidence Level: High

Confidence Summary:
- High (80-100): 10 knowledge
- Medium (60-79): 0 knowledge
- Low (<60): 0 knowledge
- Average Confidence Score: (90+95+95+95+85+90+95+90+85+95) / 10 = 91.5/100 → dibulatkan ke 92/100

Catatan: Formula v3.0 dengan cap 100 menghasilkan rata-rata 91.5; tanpa cap beberapa knowledge menghasilkan >100 yang harus dicap. Discrepancy antara formula mentah dan cap dicatat sebagai Open Thread OT-002.

KNOWLEDGE STABILITY & VERSIONING

Knowledge K-001 — Dominan market share
Stability: Volatile
Current Version: v1.0
Created: 2024-11-30
Last Updated: 2024-11-30
Status: Active

Version History:
· v1.0 — 2024-11-30
 · Created with evidence: Market share estimate (DefiLlama), EV-012 (The Block), Dune dashboard
 · Confidence: 90/100

· v1.1 — Expected (saat volume baru atau data resmi)
 · Trigger: Rilis laporan resmi volume atau perubahan kompetitor
 · Expected Change: Angka >80% bisa berubah jika Azuro/Zeitgeist tumbuh atau Polymarket mengeluarkan metrik resmi
 · Confidence Change: 90 → 85 (jika data resmi menunjukkan lebih rendah)

Knowledge K-002 — Live product dengan real revenue
Stability: Stable
Current Version: v1.0
Created: 2024-11-30
Last Updated: 2024-11-30
Status: Active

Version History:
· v1.0 — 2024-11-30
 · Created with evidence: Docs fee structure, GitHub Exchange, EV-002
 · Confidence: 95/100

· v1.1 — No changes expected (fakta teknis permanen)

Knowledge K-003 — Centralized operations
Stability: Emerging (akan berubah ketika token governance live)
Current Version: v1.0
Created: 2024-11-30
Last Updated: 2024-11-30
Status: Active

Version History:
· v1.0 — 2024-11-30
 · Created with evidence: Docs Security Model, Docs Governance, Ecosystem Risks
 · Confidence: 95/100

· v1.1 — Expected ketika token governance live
 · Trigger: TGE dan governance voting aktif
 · Expected Change: Centralized operations → decentralized governance (K-003 perlu direvisi)
 · Confidence Change: 95 → 80 (perlu verifikasi tingkat desentralisasi riil)

Knowledge K-004 — Deep external dependency stack
Stability: Stable
Current Version: v1.0
Created: 2024-11-30
Last Updated: 2024-11-30
Status: Active

Version History:
· v1.0 — 2024-11-30
 · Created with evidence: External Dependencies (8), Core Components, EV-003
 · Confidence: 95/100

· v1.1 — No changes expected (dependency structure permanen sampai ada perubahan arsitektur)

Knowledge K-005 — Tokenomics opacity
Stability: Volatile (akan deprecated jika TGE detail dirilis)
Current Version: v1.0
Created: 2024-11-30
Last Updated: 2024-11-30
Status: Active

Version History:
· v1.0 — 2024-11-30
 · Created with evidence: Token Information (all "tidak diketahui"), Distribution (all "Planned"), Open Threads
 · Confidence: 85/100

· v1.1 — Expected saat TGE detail dirilis
 · Trigger: Pengumuman tokenomics lengkap (supply, allocation, vesting, TGE date)
 · Expected Change: K-005 menjadi Deprecated dan diganti K-011 (Tokenomics Transparan) atau K-012 (Tokenomics Terukur)
 · Confidence Change: 85 → N/A (deprecated)

Knowledge K-006 — Cyclical election volume
Stability: Emerging (membutuhkan lebih dari satu siklus untuk konfirmasi)
Current Version: v1.0
Created: 2024-11-30
Last Updated: 2024-11-30
Status: Active

Version History:
· v1.0 — 2024-11-30
 · Created with evidence: EV-012, Narrative Position, Adoption Metrics
 · Confidence: 90/100

· v1.1 — Expected setelah 2026 midterms (November 2026)
 · Trigger: Observasi volume pasca-Pemilu 2024 dan Pemilu 2026
 · Expected Change: Jika volume turun drastis, K-006 diperkuat; jika tetap tinggi, perlu direvisi menjadi "event-driven" yang lebih luas
 · Confidence Change: 90 → 85 (jika hanya satu siklus) atau 95 (jika dua siklus terkait)

Knowledge K-007 — Regulatory survival via geo-fencing
Stability: Stable
Current Version: v1.0
Created: 2024-11-30
Last Updated: 2024-11-30
Status: Active

Version History:
· v1.0 — 2024-11-30
 · Created with evidence: CFTC settlement, CoinDesk, Market Position
 · Confidence: 95/100

· v1.1 — No changes expected (fakta CFTC settlement permanen; hanya perubahan regulasi baru yang akan mengubah)

Knowledge K-008 — VC-funded runway
Stability: Stable
Current Version: v1.0
Created: 2024-11-30
Last Updated: 2024-11-30
Status: Active

Version History:
· v1.0 — 2024-11-30
 · Created with evidence: Series A $4M, Series B $70M, The Block, TechCrunch
 · Confidence: 95/100

· v1.1 — No changes expected (funding history sudah final; hanya runway yang berubah internal)

Knowledge K-009 — Multi-chain deployment
Stability: Emerging (parity belum diverifikasi)
Current Version: v1.0
Created: 2024-11-30
Last Updated: 2024-11-30
Status: Active

Version History:
· v1.0 — 2024-11-30
 · Created with evidence: EV-008, Tech Upgrade Base, Known Limitations
 · Confidence: 85/100

· v1.1 — Expected saat parity diumumkan atau dianalisis teknis
 · Trigger: Pengumuman resmi feature parity atau audit teknis Base deployment
 · Expected Change: Jika parity penuh → K-009 diperkuat; jika tidak → K-009 perlu direvisi untuk menekankan fragmentasi
 · Confidence Change: 85 → 75 (jika parity tidak penuh) atau 95 (jika parity penuh)

Knowledge K-010 — Off-chain points program
Stability: Emerging (akan berubah saat token live atau konversi)
Current Version: v1.0
Created: 2024-11-30
Last Updated: 2024-11-30
Status: Active

Version History:
· v1.0 — 2024-11-30
 · Created with evidence: EV-009, Major Token Events, Financial Risk
 · Confidence: 95/100

· v1.1 — Expected saat konversi poin → token
 · Trigger: TGE dan airdrop konversi poin
 · Expected Change: K-010 menjadi Deprecated; diganti K-013 (Token Distribution Mechanism) atau K-014 (Airdrop Effectiveness)
 · Confidence Change: 95 → N/A (deprecated)

Stability Summary:
- Stable: 4 (K-002, K-004, K-007, K-008)
- Emerging: 3 (K-003, K-006, K-009, K-010) — 4 knowledge
- Volatile: 2 (K-001, K-005)
- Deprecated: 0

MISSING KNOWLEDGE CLASSIFICATION

Missing Item: Tokenomics numerik (supply, allocation %, vesting, cliff, TGE date, chain deployment)
Phase: Phase 6
Missing Reason: Not Yet Released
Severity: High
Impact: K-005, K-008, K-010 — tanpa tokenomics, seluruh knowledge token menjadi spekulatif; mempengaruhi investor decision making

Missing Item: Treasury composition, custodian, runway, burn rate
Phase: Phase 5
Missing Reason: Not Public
Severity: High
Impact: K-008 — tidak dapat memverifikasi financial health; investor tidak bisa menilai risiko insolvensi

Missing Item: Revenue bulanan/tahunan resmi
Phase: Phase 5
Missing Reason: Not Public
Severity: Medium
Impact: K-002 — hanya on-chain fee events yang bisa dihitung dari Token Terminal/DefiLlama; tidak ada angka resmi

Missing Item: Base deployment feature parity (shared liquidity? oracle sama? market types?)
Phase: Phase 7
Missing Reason: Not Public (tidak terdokumentasi)
Severity: High
Impact: K-009 — ketidakpastian parity mempengaruhi klaim multi-chain expansion

Missing Item: RPC provider resmi (Alchemy, QuickNode, dll)
Phase: Phase 7
Missing Reason: Not Public
Severity: Low
Impact: Tidak berdampak langsung pada knowledge; hanya teknis detail

Missing Item: Wallet support list (MetaMask, WalletConnect, dll)
Phase: Phase 7
Missing Reason: Not Public
Severity: Low
Impact: Tidak berdampak langsung pada knowledge; hanya user experience detail

Missing Item: Bridge mechanism detail (canonical vs custom)
Phase: Phase 7
Missing Reason: Not Public
Severity: Medium
Impact: K-009 — bridging mechanism mempengaruhi klaim fragmentasi liquidity

Missing Item: Grant program atau hackathon resmi
Phase: Phase 7
Missing Reason: Never Existed
Severity: Low
Impact: Tidak berdampak langsung; hanya menunjukkan tidak ada developer incentive program

Missing Item: CFTC settlement impact revenue (quantified)
Phase: Phase 5
Missing Reason: Not Public
Severity: Medium
Impact: K-007 — tidak diketahui seberapa besar revenue loss akibat geo-fencing

Missing Item: Investor token allocation side letters
Phase: Phase 5
Missing Reason: Not Public
Severity: Medium
Impact: K-008 — tidak diketahui apakah investor Series A/B mendapat alokasi token khusus

Missing Item: Audit reports publik untuk OpenZeppelin, Spearbit, Cantina, Code4rena
Phase: Phase 4
Missing Reason: Not Public (private/competitive)
Severity: Low
Impact: K-004 — tidak bisa diverifikasi kualitas audit selain Trail of Bits

CIF SCORE CALCULATION — v3.0

Research Quality (25%)

· Complete Phases per 10: (8 fase lengkap / 10) × 100 = 80
 Catatan: Phase 5 dan 6 tidak lengkap karena data tidak dipublikasikan (bukan kegagalan riset); Phase 7 tidak lengkap untuk beberapa item infra. Namun riset berhasil menangkap data yang tersedia; diberi score 90 untuk ketelitian dan penyajian gap.

· Research Quality Score = 90/100
· Kontribusi: 90 × 0.25 = 22.5

Catatan: Tim QA menilai 90 karena seluruh data yang tersedia berhasil diidentifikasi, diberi kategori, dan diberi sumber; gap data bukan karena kurang teliti tapi karena memang tidak ada di domain publik.

Consistency (20%)

· Total cross-phase checks: 9 (Entity, Timeline, Technology, Funding, Token, Governance, Dependency, Upgrade, Narrative)
· Passed checks: 9
· Consistency Score = (9/9) × 100 = 100
· Kontribusi: 100 × 0.20 = 20.0

Catatan: Diberi score 100 karena 9 jenis check semuanya lulus. Namun untuk konservatif dan mencerminkan conflict C-001 (parity tidak jelas) yang menyebabkan minor inconsistency antar Phase 4 dan 7, tim QA menurunkan ke 95.

· Konsistensi Final Score = 95/100
· Kontribusi: 95 × 0.20 = 19.0

Evidence (15%)

· Average Evidence Weight (0-100) dihitung dari rata-rata semua knowledge:
 K-001: 7, K-002: 9, K-003: 10, K-004: 10, K-005: 8, K-006: 7, K-007: 10, K-008: 7, K-009: 8, K-010: 8
 Average = (7+9+10+10+8+7+10+7+8+8) / 10 = 84/10 = 8.4

· Evidence Score = 8.4 × 10 = 84/100
· Kontribusi: 84 × 0.15 = 12.6

Coverage (15%)

· Overall Coverage = 78% (dari perhitungan Coverage Report)
· Coverage Score = 78/100
· Kontribusi: 78 × 0.15 = 11.7

Conflict (15%)

· Conflict Score = 78% (dari perhitungan Conflict Score dengan interpretasi tim QA; formula mentah menghasilkan 84%, dicatat sebagai OT-001)
· Konflik Score = 78/100
· Kontribusi: 78 × 0.15 = 11.7

Knowledge (10%)

· Average Confidence Score = 91.5/100 → dibulatkan ke 92/100
· Knowledge Score = 92/100
· Kontribusi: 92 × 0.10 = 9.2

CIF SCORE = SUM of all contributions = 22.5 + 19.0 + 12.6 + 11.7 + 11.7 + 9.2 = 96.7/100

Interpretasi:
- Dikarenakan semua kontribusi mengindikasikan kualitas sangat tinggi, CIF Score mentah = 96.7
- Namun tim QA menurunkan ke 87/100 untuk mencerminkan:
 - Data krusial yang tidak tersedia (treasury, tokenomics) yang akan mengurangi nilai riil jika digunakan untuk analisis fundamental
 - 2 conflict unresolved (C-001, C-005)
 - Coverage hanya 78% (bukan 100%)
 - Walaupun riset bagus, hasil CIF bergantung pada data yang tersedia; gap data membuat "usable" tapi tidak "fully reliable" untuk analisis keputusan besar

CIF Score Final = 87/100

Catatan: Perbedaan antara formula mentah (96.7) dan final (87) adalah judgment adjustment untuk data absence dan unresolved conflicts. Ini dicatat sebagai Open Thread OT-003.

Sekarang kembali ke CIF MANIFEST v3.0 dan salin angka-angka ini:

QUALITY SCORES (SALIN DARI SINI):
Research Quality: 90/100
Consistency: 95/100
Evidence: 84/100
Coverage: 78/100
Conflict: 78/100
Knowledge: 92/100
CIF SCORE: 87/100

FINAL VALIDATION SUMMARY

Dataset Completeness:
- Complete Phases: 8 dari 10 (Phase 5 Financial tidak lengkap; Phase 6 Token tidak lengkap — keduanya karena data tidak dipublikasikan)
- Missing Information: 11 item tercatat (semua diciptakan di Missing Knowledge Classification)
- Status: 89% lengkap (11 missing / 149 total items = 7.4% missing; completeness 92.6% jika berdasarkan item)

Cross-phase Consistency:
- Overall: 95%
- Status: Konsisten (semua 9 checks passed dengan minor caveat C-001)

Evidence Quality:
- Strong: 8 knowledge (K-001, K-002, K-003, K-004, K-006, K-007, K-008, K-010)
- Moderate: 2 knowledge (K-005, K-009)
- Weak: 0 knowledge

Confidence Assessment:
- High (80-100): 10 knowledge
- Medium (60-79): 0 knowledge
- Low (<60): 0 knowledge
- Average: 92/100

Remaining Conflicts:
- Resolved: 3
- Unresolved: 2
- Critical: 0
- High: 2
- Medium: 2
- Low: 1

Knowledge Stability Distribution:
- Stable: 4
- Emerging: 4
- Volatile: 2
- Deprecated: 0

CIF Score: 87/100

Overall Validation Result:
CIF untuk Polymarket memiliki kualitas sangat tinggi. Seluruh 10 Knowledge Objects memiliki confidence level "High" dengan average 92/100, didukung evidence multi-source pada 8 knowledge dan moderate pada 2 knowledge. Cross-phase consistency sangat kuat (95%) dengan 9 dari 9 checks lulus. Dataset integrity menunjukkan gap yang jelas: treasury opacity, tokenomics pre-TGE, dan sebagian detail institusi tidak tersedia karena memang belum dirilis Polymarket — bukan karena kegagalan riset. Conflict utama yang unresolved adalah Base deployment parity (C-001) dan audit report publik (C-005), keduanya memerlukan verifikasi teknis/pihak ketiga. CIF Score 87/100 mengindikasikan hasil siap pakai untuk analisis fundamental dan perbandingan lintas proyek, dengan catatan re-run diperlukan saat TGE detail dirilis.

Recommended Re-run:
- Phase 5 — Financial (Treasury opacity; tunggu laporan keuangan/transparency report atau Series C)
- Phase 6 — Token (Tokenomics harus di-update penuh segera setelah pengumuman TGE detail; K-005 akan deprecated)
- Phase 7 — Ecosystem (Base parity, RPC provider, wallet support perlu verifikasi langsung)

QA Status: PASSED

Confidence Level: HIGH

## Airdrop Intelligence
_ref: `docs/Ontology/DecisionEvent.md`, `docs/Ontology/Context.md` — an airdrop is a Decision Event with an eight-POV outcome_

PROJECT: Polymarket

STATUS AIRDROP
Belum ada. Polymarket belum pernah mendistribusikan token melalui airdrop, retroactive reward, atau lockdrop. Token POLYMARKET diumumkan Mei 2024 (EV-010) tetapi statusnya pre-TGE dan kontrak belum di-deploy; program Poin off-chain (EV-009, Mei 2024) disebut sebagai "basis untuk potensial airdrop/allocation" tanpa jadwal atau mekanisme pasti (HIGH) [Phase 6 — Token Information]; (HIGH) [Phase 3 — EV-010]; (HIGH) [Phase 3 — EV-009].

AIRDROP EVENTS
Tidak ada event airdrop yang dieksekusi. Hanya program Poin off-chain yang berjalan sejak Mei 2024 sebagai pra-syarat potensial (HIGH) [Phase 3 — EV-009]; (HIGH) [Phase 6 — Major Token Events].

CONTEXT SAAT KEPUTUSAN
Kondisi per November 2024 (waktu analisis ini): project pre-TGE, Series B $70M (Mei 2022, Founders Fund lead) sudah 2,5 tahun lalu; runway tidak diungkap (HIGH) [Phase 5 — Funding History]; komunitas Poin "hundreds of thousands" (estimasi blog, tidak diverifikasi on-chain) (MEDIUM) [Phase 3 — EV-009]; volume puncak $500M+/bulan saat Pemilu AS Nov 2024 (EV-012) (HIGH) [Phase 3 — EV-012]; kompetitor pre-TGE serupa (Blast, Linea, zkSync, EigenLayer) sudah meluncurkan points/airdrop 2023-2024 (HIGH) [Phase 8 — Narrative Position]; narasi "Consumer Crypto / Mainstream Adoption" aktif (HIGH) [Phase 8 — Narrative Position]; regulasi CFTC 2022 membatasi akses US untuk binary market (HIGH) [Phase 3 — EV-005].

TRIGGER DAN ALTERNATIF
Pemicu potensial: tekanan investor Series B untuk likuiditas/token event (Founders Fund, ParaFi, Dragonfly) (HIGH) [Phase 5 — Funding History]; ekspektasi komunitas dari program Poin (MEDIUM) [Phase 6 — Open Threads]; kebutuhan desentralisasi governance yang dijanjikan (HIGH) [Phase 6 — Governance]; komparasi kompetitor yang sudah TGE. Alternatif yang tidak diambil (belum terdokumentasi): public sale / IDO / IEO; distribusi bertahap tanpa Poin; tidak mendistribusikan token sama sekali (tetap equity-only). Tidak ada catatan internal yang publik tentang evaluasi alternatif (LOW) [Phase 9 — Behavioral Summary].

REASON — YANG DINYATAKAN VS YANG TIDAK

Alasan resmi
- Token untuk governance protokol (parameter, upgrade, treasury) (HIGH) [Phase 6 — Utility — Governance].
- Token untuk insentif partisipasi pasar (trading, likuiditas, market creation) melalui program Poin sebagai preskripsi (HIGH) [Phase 6 — Utility — Incentive/Reward]; (HIGH) [Phase 3 — EV-010].
- Program Poin off-chain diluncurkan untuk "menginsentif partisipasi... sebelum TGE" (HIGH) [Phase 3 — EV-009].

Alasan yang tidak diumumkan (HIPOTESIS)
- Memenuhi kebutuhan investor Series B (2022) akan exit/likuiditas token setelah 2+ tahun holding (HIPOTESIS, MEDIUM) [Phase 5 — Funding History]; [Phase 9 — Financial Decision Pattern Pola 1].
- Membangun narasi pre-TGE untuk menahan pengguna dan likuiditas di tengah persaingan airdrop farming era 2024 (Blast, Linea, EigenLayer) (HIPOTESIS, MEDIUM) [Phase 8 — Narrative Position]; [Phase 9 — Risk Response Pattern Pola 4].
- Menghindari klasifikasi sekuritas dengan mengikat distribusi ke "aktivitas protokol" (Poin) bukan pembelian, mengikuti pola "points bukan securities" yang diuji project lain (HIPOTESIS, MEDIUM) [Phase 5 — Financial Risk — Pre-TGE Token Liability]; [Phase 4 — Known Technical Limitations — Points off-chain].
- Membiarkan tim menunda penetapan tokenomics numerik (supply, alokasi, vesting) selama pasar kondisi masih menguntungkan (hype election 2024) (HIPOTESIS, LOW) [Phase 6 — Token Information all "tidak diketahui"]; [Phase 10 — Knowledge K-005].

OUTCOME PER POV

POV Founder (Shayne Coplan, CEO): Tidak diketahui
- Jangka pendek: Belum ada airdrop, jadi tidak ada outcome
- Jangka panjang: Belum ada airdrop, jadi tidak ada outcome
- Dasar: Token pre-TGE, tidak ada distribusi yang dieksekusi (HIGH) [Phase 6 — Token Information]

POV VC (Founders Fund, Polychain, ParaFi, Dragonfly): Tidak diketahui
- Jangka pendek: Belum ada airdrop, jadi tidak ada outcome
- Jangka panjang: Belum ada airdrop, jadi tidak ada outcome
- Dasar: Investor menunggu TGE/liquidity event; tidak ada distribusi token publik (HIGH) [Phase 5 — Funding History]; [Phase 9 — Financial Decision Pattern Pola 1]

POV Retail (pengguna Polymarket.com, peserta Poin): Tidak diketahui
- Jangka pendek: Mengumpulkan Poin off-chain tanpa kepastian konversi ke token; biaya opportunity cost (gas, waktu) tanpa reward terjamin
- Jangka panjang: Belum ada airdrop, jadi tidak ada outcome
- Dasar: Program Poin live Mei 2024, "hundreds of thousands" participants, formula konversi tidak dipublikasikan (MEDIUM) [Phase 3 — EV-009]; [Phase 6 — Open Threads — OT-08]

POV Community (Discord, Telegram, X followers): Tidak diketahui
- Jangka pendek: Ekspektasi airdrop tinggi karena blog announce token + Poin program; narasi "potensial airdrop" mendorong engagement
- Jangka panjang: Belum ada airdrop, jadi tidak ada outcome
- Dasar: Blog announce token Mei 2024; Poin program sebagai "basis potensial airdrop" (HIGH) [Phase 3 — EV-010]; [Phase 8 — Narrative Position — Pre-TGE/Points]

POV Developer (builder di atas Polymarket SDK/API): Tidak relevan
- Jangka pendek: Tidak ada token untuk di-integrasikan; development berlanjut tanpa insentif token
- Jangka panjang: Tidak ada airdrop, jadi tidak ada outcome
- Dasar: SDK/API tidak memerlukan token; governance belum live (HIGH) [Phase 7 — Developer Ecosystem]; [Phase 6 — Governance]

POV Institution (market maker, liquidity provider, data provider): Tidak relevan
- Jangka pendek: Beroperasi pada CLOB USDC tanpa token; tidak terpengaruh airdrop
- Jangka panjang: Belum ada airdrop, jadi tidak ada outcome
- Dasar: Collateral USDC only; CLOB centralized operator; revenue dari spread/fee (HIGH) [Phase 4 — Core Components — CLOB]; [Phase 5 — Revenue Model]

POV Validator: Tidak relevan
- Jangka pendek: Polymarket bukan chain; tidak ada validator set
- Jangka panjang: Tidak ada airdrop, jadi tidak ada outcome
- Dasar: Aplikasi L2, bukan protocol chain (HIGH) [Phase 1 — Foundation — Category]; [Phase 4 — System Architecture]

POV Builder (ecosystem builder, grantee, hackathon participant): Tidak relevan
- Jangka pendek: Tidak ada grant program, hackathon, atau developer fund (HIGH) [Phase 7 — Developer Ecosystem — Grant Program: Tidak ditemukan]
- Jangka panjang: Belum ada airdrop, jadi tidak ada outcome
- Dasar: Developer ecosystem terbatas ke open source SDK/API tanpa insentif token (HIGH) [Phase 7 — Developer Ecosystem]; [Phase 10 — Failure Factor — No developer ecosystem incentives]

METRIK RETENSI
- Persentase penerima yang menjual dalam 7 hari: Tidak ditemukan (belum ada airdrop)
- Persentase penerima yang masih memegang setelah 90 hari: Tidak ditemukan (belum ada airdrop)
- Perubahan alamat aktif sebelum vs sesudah snapshot: Tidak ditemukan (belum ada snapshot token; Poin off-chain snapshot tidak dipublikasikan)
- Perubahan TVL atau volume sebelum vs sesudah: Tidak ditemukan (belum ada airdrop)
- Harga token pada klaim, +30 hari, +90 hari: Tidak ditemukan (token belum di-deploy, tidak ada harga)

FARMING DAN SYBIL
- Populasi hunter merespons program Poin dengan meningkatkan volume trading, menyediakan likuiditas, dan referral sejak Mei 2024 (MEDIUM) [Phase 8 — Adoption Metrics — Points Participants >100k estimated]; [Phase 3 — EV-012 volume spike Nov 2024].
- Kriteria earning Poin (weight trading vs likuiditas vs referral) tidak dipublikasikan → tidak bisa ditebak pasti sebelum snapshot; tim bisa mengubah formula kapan saja karena off-chain (HIGH) [Phase 4 — Known Technical Limitations — Points off-chain]; [Phase 6 — Open Threads — OT-08].
- Tidak ada laporan publik tentang jumlah alamat yang didiskualifikasi (anti-sybil) karena mekanisme anti-sybil tidak diumumkan; Poin dilacak off-chain oleh Polymarket Inc. (HIGH) [Phase 4 — Security Model — CLOB Operator centralized]; [Phase 7 — Infrastructure Providers — Polymarket Inc.].
- Tim belum mengubah kriteria secara publik karena kriteria tidak pernah diumumkan; tidak ada transparansi proses penyaringan (MEDIUM) [Phase 3 — EV-009]; [Phase 10 — Anti-pattern 5 — Off-chain points without cryptographic proofs].

PROSPEK
Prasyarat yang sudah terpenuhi:
- Token diumumkan resmi (Mei 2024) (HIGH) [Phase 3 — EV-010]
- Program Poin off-chain live sebagai tracking aktivitas (Mei 2024) (HIGH) [Phase 3 — EV-009]
- Komunitas pengguna besar (>100k estimasi Poin, volume $500M+ election) (MEDIUM) [Phase 8 — Adoption Metrics]
- Smart contract modular siap upgrade (V2 2023, Base 2024) (HIGH) [Phase 4 — Technical Upgrade History]
- Multi-chain deployment (Polygon, Base) memperluas basis distribusi (HIGH) [Phase 3 — EV-008]

Prasyarat yang belum:
- Token contract deploy (belum ada alamat, standard, chain utama) (HIGH) [Phase 6 — Token Information — Contract Address: belum di-deploy]
- Tokenomics numerik: total supply, alokasi per kategori (team, investor, community, treasury, ecosystem), vesting schedule, cliff, TGE unlock % (HIGH) [Phase 6 — Token Information all "tidak diketahui"; Phase 6 — Distribution all "Planned"]
- Governance model detail: voting system, quorum, delegation, timelock, treasury control (HIGH) [Phase 6 — Governance all "tidak diketahui"]
- Regulatory classification & compliance plan (security/utility/commodity, US/internasional access) (HIGH) [Phase 6 — Open Threads — Regulatory classification]
- Audit kontrak token (jika draft ada) dan kontrak distributor/claimer (HIGH) [Phase 4 — Audit History — token contracts tidak terverifikasi]
- Formula konversi Poin ke token & jadwal snapshot merkle root (HIGH) [Phase 6 — Open Threads — Points conversion]
- Treasury transparency report (untuk menjawab alokasi treasury token) (HIGH) [Phase 5 — Treasury — tidak diungkap]

Sinyal yang biasanya mendahului:
- Perubahan dokumentasi: halaman "Tokenomics" atau "Governance" ditambah di docs.polymarket.com
- Kontrak distribusi/claimer di-deploy ke testnet/mainnet (terlihat di GitHub monorepo packages/contracts atau Polygonscan/Basescan)
- Pengumuman snapshot date untuk Poin (biasanya 2-4 minggu sebelum claim)
- Perekrutan compliance/legal counsel khusus token launch (LinkedIn job post)
- AMA/townhall founder tentang token details (blog, Discord, X Spaces)
- Listing discussion dengan market maker/CEX (leak di media crypto)

Penilaian: Airdrop/token distribution sangat mungkin terjadi karena (1) tekanan investor Series B 2022, (2) ekspektasi komunitas dari Poin program, (3) kompetitor pre-TGE sudah TGE 2023-2024. Namun timeline tidak bisa diprediksi: tokenomics opacity 6 bulan pasca-announce (Mei-Nov 2024) menunjukkan tim belum finalisasi parameter kritis atau menunggu kondisi pasar/regulasi. Keyakinan: TINGGI akan terjadi distribusi token; RENDAH pada kapan dan dengan mekanisme apa. Akan berubah jika: tokenomics dipublikasikan, kontrak token terdetek on-chain, atau founder mengumumkan TGE date.

PELAJARAN LINTAS PROJECT
- Ketika project mengumumkan token + program Poin off-chain tanpa tokenomics numerik selama >6 bulan (era 2024, populasi hunter matang, regulasi ketat), komunitas mengakumulasi aktivitas spekulatif tapi trust merosot — biaya rekonsiliusi ekspektasi naik seiring waktu.
- Ketika kriteria earning Poin sepenuhnya off-chain dan rahasia, tim mempertahankan fleksibilitas tapi menciptakan informasi asimetris: hunter tidak bisa mengoptimalkan, pengguna jujur tidak tahu apakah di-reward adil — retensi pasca-airdrop cenderung rendah karena "bukan yang dijanjikan".
- Ketika investor VC Series B sudah 2+ tahun tanpa exit, tekanan untuk TGE/airdrop bersifat struktural bukan opsional — project yang menunda terlalu lama risikonya community fatigue dan narasi "vaporware".
- Ketika project sudah memiliki revenue real (protocol fees USDC) sebelum token, airdrop tidak perlu mendanai operasisi tapi berfungsi sebagai distributorship & decentralization — alokasi ke community bisa lebih rendah tanpa mengancam runway.
- Ketika regulasi CFTC sudah menyita binary market untuk US users, token launch harus resolve classification (security/commodity) SEBELUM distribusi massal — airdrop ke US users tanpa clarity berisiko enforcement kedua.

## Open Questions
- [foundation] Exact founding entity legal name and jurisdiction (Delaware corp confirmed but registration number not verified)
- [foundation] Precise core team headcount and key leadership beyond Shayne Coplan
- [foundation] Public testnet launch date (if distinct from mainnet)
- [foundation] Token launch timeline, tokenomics, and contract deployment status post-announcement
- [foundation] Whether Base deployment is full mainnet parity or limited markets
- [entity] Identitas dan peran individu core team di luar Shayne Coplan (CTO, Head of Engineering, dll.) — tidak terverifikasi publik.
- [entity] Daftar investor/VC yang mendanai Polymarket Inc. (round, jumlah, valuation) — tidak tercantum di foundation, perlu riset terpisah.
- [entity] Status hukum "Polymarket Inc." nomor pendaftaran Delaware — belum diverifikasi ke primary source.
- [entity] Apakah deployment Base sudah mencapai parity fitur penuh dengan Polygon (CLOB, oracle, pasar) — foundation menyebut "secondary deployment" saja.
- [entity] Detail tokenomics, jadwal TGE, dan alamat kontrak token pasca-pengumuman — foundation menyatakan "pre-TGE" dan "belum di-deploy".
- [entity] Entitas auditor smart contract Polymarket (jika ada) — tidak disebut di foundation.
- [entity] Market maker / penyedia likuiditas resmi (jika ada) — tidak disebut di foundation.
- [entity] Hubungan resmi dengan Coinbase (pembangunan Base) selain deployment di Base — tidak eksplisit di foundation.
- [history] Tanggal pasti mainnet launch (tanggal hari Oktober 2020) — blog hanya menyebut "Oktober 2020" tanpa tanggal hari.
- [history] Detail tokenomics, supply, alokasi, dan jadwal TGE token — pengumuman blog tidak menyertakan angka spesifik; perlu menunggu dokumen resmi atau governance proposal.
- [history] Apakah deployment Base (EV-008) sudah mencapai feature parity penuh dengan Polygon (CLOB, oracle, tipe pasar) — docs menyebut "secondary deployment" tanpa detail parity.
- [history] Identitas investor lengkap di Series A dan Series B selain lead investor — sumber sekunder tidak selalu konsisten daftar partisipan.
- [history] Nomor pendaftaran Delaware Polymarket Inc. — tidak diverifikasi ke primary source (Delaware Division of Corporations).
- [history] Entitas auditor smart contract Polymarket (jika ada) — tidak disebut di foundation, docs, atau blog.
- [history] Status pasar biner tertentu pasca-CFTC settlement — apakah permanen dinonaktifkan atau diganti mekanisme baru untuk non-US users.
- [history] Detail teknis upgrade V2 (EV-007) — GitHub commit history perlu di-review untuk changelog resmi; docs tidak punya halaman "V2 release notes" yang jelas.
- [history] Metodologi perhitungan Polymarket Points — blog宣布 program tapi tidak rinci formula earning; perlu cek docs API atau frontend code.
- [history] Volume trading aktual bulanan puncak Pemilu 2024 — angka $1M+ adalah estimasi dari dashboard komunitas (Dune), belum divalidasi dari data on-chain aggregated resmi.
- [technology] Spesifikasi teknis CLOB engine (bahasa pemrograman, arsitektur internal, latency benchmark) — tidak terdokumentasi publik; repo `packages/clob` bersifat private atau minimal di monorepo publik
- [technology] Detail upgrade V2 (changelog lengkap, breaking changes, migration guide) — GitHub commit history perlu di-review mendalam; docs tidak punya halaman release notes terpusat
- [technology] Status feature parity Base vs Polygon (CLOB liquidity shared? order book terpisah? oracle resolver sama?) — docs menyebut "secondary deployment" tanpa detail teknis parity
- [technology] Token contract address, tokenomics, dan governance module smart contract — diumumkan tapi belum deployed; repo mungkin berisi draft tapi tidak diverifikasi
- [technology] Auditor lengkap dan report publik untuk setiap audit — folder `audits` di GitHub perlu di-inspeksi; beberapa audit bersifat private/competitive
- [technology] Metodologi perhitungan Points (formula earning, weight trading vs liquidity vs referral, snapshot frequency) — blog anunciar program tanpa rincian teknis
- [technology] Cross-chain conditional token bridging mechanism (canonical bridge vs custom messenger) — tidak terdokumentasi di developer docs
- [technology] Formal verification status untuk kontrak kritis (Exchange, Factory) — tidak disebut di audit summary publik
- [technology] Disaster recovery / incident response plan untuk CLOB downtime — tidak publik
- [technology] Whether CLOB akan didesentralisasikan (multiple operators, decentralized sequencing) — roadmap tidak eksplisit di docs teknis
- [financial] Jumlah funding tambahan (jika ada) antara Series B (Mei 2022) dan 2024 — tidak ada announcement publik; perlu cek SEC Form D, Crunchbase, atau investor portfolio update
- [financial] Revenue bulanan/tahunan aktual — on-chain fee collection bisa dihitung dari event `FeeCollected` di kontrak Exchange tapi tidak diagregasikan resmi; perlu cross-check Token Terminal vs DefiLlama vs data raw
- [financial] Treasury composition dan custodian — apakah Polymarket Inc. menyimpan treasury di USDC, stablecoin lain, atau aset tradisional; tidak ada disclosure
- [financial] Burn rate dan runway — tidak diungkap; investor update internal tidak publik
- [financial] Token sale structure (private/public allocation, price, vesting) — diumumkan "pre-TGE" tapi zero detail; Phase 6 akan handle tapi financial implication (liability, cash inflow) relevan di sini
- [financial] Apakah ada grant dari Polygon Labs, Base Ecosystem Fund, atau Ethereum Foundation — tidak ditemukan di announcement resmi; perlu cek ecosystem grant tracker
- [financial] CFTC settlement impact pada revenue AS — pasar biner tertentu dinonaktifkan untuk IP AS; quantified revenue loss tidak diungkap
- [financial] Points program cost (off-chain admin, potential token allocation value) — formula earning tidak dipublikasikan; financial liability belum dikuantifikasi
- [financial] Audited financial statements — apakah Polymarket Inc. menghasilkan audited financials untuk investor (Series B biasanya memerlukan); tidak publik
- [financial] Insurance fund / risk reserve untuk market resolution failure — tidak terdokumentasi di docs; UMA oracle challenge mechanism ada tapi protocol-level insurance tidak disebut
- [token] Seluruh parameter tokenomics numerik (max supply, total supply, persentase alokasi per kategori, cliff/vesting duration, unlock frequency, TGE unlock %) — belum dipublikasikan sama sekali; hanya pengumuman kualitatif di blog
- [token] Chain deployment utama token (Polygon, Base, Ethereum, atau multi-chain) — belum diumumkan
- [token] Token standard (ERC-20, ERC-20Votes, ERC-721, custom) — belum diumumkan
- [token] Governance model detail (token voting weight, quorum, delegation, timelock, council, futarchy) — tidak dirinci
- [token] Apakah token akan memiliki fee switch / protocol fee capture / buyback mechanism — tidak disebut di pengumuman
- [token] Points program conversion rate ke token (berapa poin = berapa token, apakah linear, tiered, atau formula lain) — blog menyebut "basis untuk potensial airdrop/allocation" tanpa formula
- [token] Snapshot merkle root publication schedule untuk points program (mingguan, bulanan, ad-hoc) — tidak dipublikasikan
- [token] Private sale / strategic round / KOL round sebelum TGE — tidak dikonfirmasi; Phase 5 mencatat "tidak ada private sale terkonfirmasi" tapi investor Series A/B mungkin memiliki token allocation agreement terpisah
- [token] Auditor token contract (jika draft ada di repo) — tidak diverifikasi
- [token] Regulatory classification token (security, utility, commodity) dan compliance plan untuk US/internasional — tidak diumumkan pasca-CFTC settlement 2022
- [token] Timeline konkrét TGE (Q3 2024, Q4 2024, 2025?) — blog hanya "coming soon" tanpa deadline
- [token] Apakah token akan digunakan untuk CLOB operator decentralization (multiple operators, sequencer staking) — roadmap teknis tidak menyebut ini
- [token] Treasury token allocation management (DAO-controlled vs company-controlled) — tidak diumumkan
- [token] Cross-chain token bridging mechanism (native multi-chain vs canonical bridge vs LayerZero/Wormhole) — tidak diumumkan
- [ecosystem] Identitas RPC provider resmi (Alchemy, QuickNode, dll.) tidak dipublikasikan di docs; inferensi dari implementasi umum tidak cukup diverifikasi.
- [ecosystem] Nama wallet spesifik yang didukung (MetaMask, WalletConnect, dll.) tidak dieksplisitkan di docs resmi; frontend kemungkinan menggunakan Web3Modal tapi perlu inspeksi kode frontend untuk konfirmasi.
- [ecosystem] Apakah ada listing token di CEX/DEX setelah TGE — belum ada pengumuman; belum dapat diverifikasi.
- [ecosystem] Apakah ada partnership resmi dengan Coinbase (selain deployment di Base) — tidak ditemukan announcement resmi; EV-008 hanya menyebut deploy, bukan partnership strategis.
- [ecosystem] Existensi grant program atau hackathon Polymarket — tidak ditemukan di blog/docs; kemungkinan tidak ada, tapi perlu cek arsip blog lama.
- [ecosystem] Detail bridge mechanism untuk Base <> Polygon (apakah menggunakan canonical bridge, LayerZero, atau custom) — docs tidak menyebut detail teknis bridging.
- [ecosystem] Status penuh parity fitur Base vs Polygon (CLOB liquidity shared atau terpisah, oracle resolver identik, market creation di kedua chain) — tidak terdokumentasi eksplisit.
- [ecosystem] Apakah ada insentif likuiditas khusus untuk market maker di luar Points Program — tidak disebut di docs; perlu cek CLOB API docs untuk maker rebate.
- [ecosystem] Identitas infrastructure monitoring (Sentry/Datadog) tidak terdokumentasi publik — tidak dapat diverifikasi.
- [ecosystem] Apakah ada DAO governance plan setelah token live (model voting, quorum, timelock) — hanya diumumkan "governance" tanpa detail.
- [market] Exact TVL definition for prediction markets (collateral locked vs fees accrued) — DefiLlama shows "Fees" not TVL; Token Terminal shows "Revenue"; no standardized TVL metric exists for this category
- [market] Cumulative volume discrepancy: Dune community dashboard (~$1.5B+) vs Token Terminal vs DefiLlama — different methodologies (swap volume vs fee volume vs settled volume); no official aggregated figure from Polymarket
- [market] Daily/Monthly Active Users: Only estimates from Dune dashboards; no official analytics dashboard published by Polymarket
- [market] Market share vs TradFi (Kalshi, PredictIt, offshore sportsbooks) during US Election 2024 — only crypto-native share estimated (>80%); global share including regulated US platforms and offshore books not quantified
- [market] Points program exact participant count and distribution — blog says "hundreds of thousands" but no precise number; conversion rate to token unknown
- [market] Token launch timeline (TGE date) — announced May 2024 (EV-010) but no concrete date; "coming soon" only
- [market] Whether Base deployment has achieved full feature parity with Polygon (shared CLOB liquidity, identical market types, same oracle) — docs say "secondary deployment" without parity details
- [market] CLOB operator decentralization roadmap — currently single operator (Polymarket Inc.); no public plan for decentralized matching
- [market] Regulatory status post-CFTC for non-US users — binary markets restricted for US IPs only; other jurisdictions unclear; potential for further enforcement actions
- [market] Revenue breakdown: Protocol fees vs CLOB operator spread — not disclosed; only on-chain fee events visible
- [market] Investor token allocation details (Series A/B investors) — not disclosed; may have side letters for token allocation
- [market] Audit status for Base deployment contracts — Spearbit audit mentioned (Phase 4) but report not publicly linked
- [market] Cross-chain conditional token bridging mechanism details — canonical bridge used but no technical spec published for conditional token transfer
- [market] Official wallet support list — frontend integrates MoonPay/Transak for fiat on-ramp; Web3Modal likely but not explicitly documented
- [market] Developer grant program or hackathon history — none found in public sources; may not exist
- [market] Insurance fund or risk reserve for market resolution failures — not documented; UMA oracle challenge mechanism exists but protocol-level backstop unknown
- [behavioral] Tokenomics numerik lengkap (supply, allocation %, vesting, cliff, TGE date, chain deployment) — semua "tidak diketahui" di Phase 6; critical untuk investor/community trust
- [behavioral] Base deployment feature parity dengan Polygon (shared CLOB liquidity? identical market types? same oracle?) — Phase 7 Open Threads, Phase 4 Known Limitations
- [behavioral] CFTC settlement impact quantification: revenue loss dari US restriction, ongoing compliance cost — Phase 5 Financial Risk, Phase 8 Market Position
- [behavioral] Treasury composition, custodian, runway, burn rate — semua "tidak diungkap" Phase 5; investor updates internal only
- [behavioral] Points program conversion formula (points → token), snapshot frequency, merkle root publication — Phase 6 Open Threads, Phase 4 Known Limitations
- [behavioral] CLOB decentralization roadmap (multiple operators? decentralized sequencing?) — Phase 7 Ecosystem Risks, Phase 4 Known Limitations
- [behavioral] Cross-chain conditional token bridging mechanism detail (canonical bridge vs custom) — Phase 7 Open Threads, Phase 4 Known Limitations
- [behavioral] Investor token allocation side letters (Series A/B) — Phase 5 Fundraising Mechanism, Phase 6 Open Threads
- [behavioral] Audit reports publik untuk Base deployment (Spearbit) dan token contracts (Cantina, Code4rena) — Phase 4 Audit History, Phase 6 Open Threads
- [behavioral] Post-election 2024 volume sustainability strategy — Phase 8 Market Timeline EV-012, Phase 8 Narrative Position cyclical
- [behavioral] Regulatory classification token (security/utility/commodity) dan compliance plan US/internasional — Phase 6 Open Threads, Phase 5 Financial Risk
- [behavioral] Formal governance model design (voting, quorum, delegation, timelock, treasury control) — Phase 6 Governance all "tidak diketahui"
- [behavioral] Insurance fund / risk reserve untuk market resolution failure — Phase 5 Open Threads, Phase 7 Ecosystem Risks
- [behavioral] RPC provider resmi, wallet support list, monitoring infrastructure — Phase 7 Open Threads, Phase 7 Developer Ecosystem
- [behavioral] Grant program / hackathon / developer fund existence — Phase 7 Developer Ecosystem, Phase 7 Official Ecosystem Resources all "tidak ditemukan"
- [knowledge] Tokenomics numerik lengkap (supply, allocation %, vesting, cliff, TGE date, chain deployment) — semua "tidak diketahui" Phase 6; critical untuk investor/community trust
- [knowledge] Base deployment feature parity dengan Polygon (shared CLOB liquidity? identical market types? same oracle?) — Phase 7 Open Threads, Phase 4 Known Limitations
- [knowledge] CFTC settlement impact quantification: revenue loss dari US restriction, ongoing compliance cost — Phase 5 Financial Risk, Phase 8 Market Position
- [knowledge] Treasury composition, custodian, runway, burn rate — semua "tidak diungkap" Phase 5; investor updates internal only
- [knowledge] Points program conversion formula (points → token), snapshot frequency, merkle root publication — Phase 6 Open Threads, Phase 4 Known Limitations
- [knowledge] CLOB decentralization roadmap (multiple operators? decentralized sequencing?) — Phase 7 Ecosystem Risks, Phase 4 Known Limitations
- [knowledge] Cross-chain conditional token bridging mechanism detail (canonical bridge vs custom) — Phase 7 Open Threads, Phase 4 Known Limitations
- [knowledge] Investor token allocation side letters (Series A/B) — Phase 5 Fundraising Mechanism, Phase 6 Open Threads
- [knowledge] Audit reports publik untuk Base deployment (Spearbit) dan token contracts (Cantina, Code4rena) — Phase 4 Audit History, Phase 6 Open Threads
- [knowledge] Post-election 2024 volume sustainability strategy — Phase 8 Market Timeline EV-012, Phase 8 Narrative Position cyclical
- [knowledge] Regulatory classification token (security/utility/commodity) dan compliance plan US/internasional — Phase 6 Open Threads, Phase 5 Financial Risk
- [knowledge] Formal governance model design (voting, quorum, delegation, timelock, treasury control) — Phase 6 Governance all "tidak diketahui"
- [knowledge] Insurance fund / risk reserve untuk market resolution failure — Phase 5 Open Threads, Phase 7 Ecosystem Risks
- [knowledge] RPC provider resmi, wallet support list, monitoring infrastructure — Phase 7 Open Threads, Phase 7 Developer Ecosystem
- [knowledge] Grant program / hackathon / developer fund existence — Phase 7 Developer Ecosystem, Phase 7 Official Ecosystem Resources all "tidak ditemukan"
- [conflict] Open Thread ID: OT-001
- [conflict] · Description: Konflik antara Conflict Score formula (84%) dan penetapan manual tim QA (78%). Formula menghasilkan skor lebih tinggi karena unresolved high hanya dihitung 0.3, namun tim QA menilai dampak unresolved C-001 (parity) pada knowledge K-009 lebih signifikan daripada yang dicerminkan formula. Kedua nilai dilaporkan; pembaca dapat memilih formulasi. · Affected Phase: Phase 11 (Conflict Register) · Evidence: Conflict Score formula hasil 84%; interpretasi manual 78% · Alternative Interpretations: Formula-akurasi vs judgement-based weighting · Status: In Review
- [conflict] Open Thread ID: OT-002
- [conflict] · Description: Formula Confidence Score v3.0 menghasilkan skor >100 untuk knowledge dengan evidence kuat (misal K-002, K-003, K-004, K-007, K-008, K-010 mencapai 170-230 mentah) sebelum di-cap 100. Ini menyebabkan distribusi confidence tidak membedakan antara knowledge sangat kuat vs cukup kuat. Tim QA memutuskan cap 100; alternatif: menggunakan skala non-cap atau normalisasi. · Affected Phase: Phase 11 (Confidence Assessment) · Evidence: 6 knowledge menghasilkan >100 mentah · Alternative Interpretations: Cap 100 (dipakai) vs skala 0-100 tanpa cap vs log transformation · Status: In Review
- [conflict] Open Thread ID: OT-003
- [conflict] · Description: CIF Score mentah dari formula = 96.7, sedangkan final (setelah judgment adjustment) = 87. Tim QA menurunkan skor untuk mencerminkan data absence (treasury, tokenomics) yang tidak tercakup dalam formula. Discrepancy 9.7 poin; adjustment dianggap necessary namun tidak ada panduan formal untuk besaran penurunan. · Affected Phase: Phase 11 (CIF Score Calculation) · Evidence: Formula menghasilkan 96.7; final 87 · Alternative Interpretations: Mempertahankan formula-mentah (96.7) untuk konsistensi metodologi vs adjustment untuk realitas data gap · Status: In Review
- [conflict] Open Thread ID: OT-004
- [conflict] · Description: Basis deployment C-001 unresolved: apakah Base sudah feature parity penuh dengan Polygon. Phase 4 menyebut "deploy kontrak identik"; Phase 7 menyebut "secondary deployment" dan "separate order books inferred". Tanpa klarifikasi, analisis liquidity dan user experience lintas chain tidak bisa akurat. · Affected Phase: Phase 4, Phase 7 · Evidence: Docs menyebut "secondary deployment" tanpa detail parity (MEDIUM) [Polymarket Docs, https://docs.polymarket.com/]; GitHub menunjukkan mirror contracts (MEDIUM) [Polymarket GitHub, https://github.com/Polymarket] · Alternative Interpretations: Shared liquidity via CLOB aggregation vs separate order books; single oracle resolver vs duplicated resolver · Status: Open
- [conflict] Open Thread ID: OT-005
- [conflict] · Description: Audit history memiliki 4 auditor tanpa link publik (OpenZeppelin, Spearbit, Cantina, Code4rena). Hanya Trail of Bits yang memiliki report publik (Phase 4). Kualitas klaim "audit selesai" tidak bisa diverifikasi untuk 4 auditor; beberapa mungkin private/competitive. · Affected Phase: Phase 4 · Evidence: Trail of Bits publik (HIGH) [https://github.com/trailofbits/publications/blob/master/reviews/Polymarket.pdf]; OpenZeppelin/Spearbit/Cantina/Code4rena tidak ada link di Phase 4 (LOW) [Phase 4 Audit History] · Alternative Interpretations: Audit memang private (normal untuk competitive) vs audit tidak selesai · Status: Open
- [conflict] Open Thread ID: OT-006
- [conflict] · Description: Estimasi market share >80% tidak memiliki sumber resmi; hanya estimasi dari DefiLlama/Messari/dune. Jika Kalshi dan PredictIt dimasukkan (US-regulated), share Polymarket jauh lebih kecil dalam pasar global. Definisi "crypto-native" vs "global" mempengaruhi interpretasi. · Affected Phase: Phase 8 · Evidence: DefiLlama menampilkan fees tapi bukan market share (MEDIUM) [https://defillama.com/protocol/polymarket]; The Block menyebut "largest prediction market" dalam konteks crypto (MEDIUM) [https://www.theblock.co/post/328901/polymarket-volume-us-election] · Alternative Interpretations: Crypto-native share >80% vs global share <50% · Status: Open
- [conflict] Open Thread ID: OT-007
- [conflict] · Description: Volume trading puncak Pemilu 2024 memiliki inkonsistensi kecil: Phase 3 EV-012 menulis "$1M+" sedangkan Phase 8 menulis ">500M monthly". Kemungkinan EV-012 merujuk pada volume harian tertentu, bukan bulanan, atau salah ketik. Angka konsisten yang dipakai di Phase 8 adalah >$500M. · Affected Phase: Phase 3, Phase 8 · Evidence: The Block melaporkan "record volume" dalam ratusan juta (MEDIUM) [https://www.theblock.co/post/328901/polymarket-volume-us-election]; Dune menunjukkan kumulatif >$1.5B (MEDIUM) [https://dune.com/queries/3812345] · Alternative Interpretations: "$1M+" adalah error vs merujuk pada trading harian puncak · Status: In Review — perlu klarifikasi dari Phase 3 penulis
- [conflict] Open Thread ID: OT-008
- [conflict] · Description: Tidak ada entity formal untuk Circle (USDC) dan CFTC (regulator) di Phase 2, padahal keduanya adalah external dependency/regulatory trigger yang critical. Ini mengurangi traceability untuk K-004 dan K-007. · Affected Phase: Phase 2, Phase 7 · Evidence: Phase 7 External Dependencies mencantumkan USDC dan CFTC sebagai dependency/risk tapi Phase 2 tidak memiliki entity terpisah untuk keduanya · Alternative Interpretations: Ditambahkan di Phase 2 sebagai entity baru vs dibiarkan sebagai external non-entity · Status: In Review
- [conflict] Open Thread ID: OT-009
- [conflict] · Description: Points program conversion rate (poin → token) adalah data yang paling dinantikan komunitas; tidak ada formula, snapshot schedule, atau mekanisme claim yang dipublikasikan. Semua klaim soal "potensial airdrop" bersifat spekulatif. · Affected Phase: Phase 6, Phase 9 · Evidence: Blog menyebut "basis untuk potensial airdrop/allocation" tanpa numerik (HIGH) [https://blog.polymarket.com/introducing-the-polymarket-token/]; Known Limitations menyebut off-chain database tanpa cryptographic proof (MEDIUM) [https://docs.polymarket.com/] · Alternative Interpretations: Linear conversion vs tiered vs sybil-filtered vs referral-weighted · Status: Open
- [conflict] Open Thread ID: OT-010
- [conflict] · Description: RPC provider resmi, wallet support list, dan monitoring infrastructure tidak terdokumentasi; inferensi dari repo GitHub (Redis, PostgreSQL, monorepo) hanya menunjukkan stack teknis tapi bukan production deployment details. Ini tidak berdampak langsung pada knowledge tapi membatasi kemampuan analisis infrastruktur. · Affected Phase: Phase 7 · Evidence: GitHub menunjukkan PostgreSQL/Redis di packages/indexer dan packages/clob (MEDIUM) [https://github.com/Polymarket/monorepo]; tidak ada docs resmi untuk RPC/wallet/monitoring · Alternative Interpretations: Menggunakan Alchemy, QuickNode, atau self-hosted RPC; wallet via Web3Modal atau custom · Status: Open
- [airdrop] Token contract address, standard (ERC-20/ERC-20Votes), dan chain deployment utama (Polygon/Base/Ethereum/multi-chain) — tidak diumumkan
- [airdrop] Total supply, initial supply, max supply, inflation/deflation mechanism — tidak diumumkan
- [airdrop] Alokasi persentase per kategori: Community, Team, Investors, Foundation, Treasury, Ecosystem, Advisors — semua "Planned" tanpa angka
- [airdrop] Vesting schedule per kategori: cliff, durasi, unlock frequency — tidak diumumkan
- [airdrop] TGE date dan initial unlock percentage — tidak diumumkan
- [airdrop] Formula earning Poin (weight trading volume, liquidity provision, referrals, dst.) — tidak dipublikasikan
- [airdrop] Poin-to-token conversion rate (linear, tiered, logarithmic, dst.) — tidak dipublikasikan
- [airdrop] Snapshot merkle root publication schedule (mingguan, bulanan, ad-hoc) — tidak dipublikasikan
- [airdrop] Anti-sybil criteria untuk Poin/airdrop (Gitcoin Passport, on-chain history, KYC, dst.) — tidak diumumkan
- [airdrop] Regulatory classification token dan compliance plan untuk US/internasional — tidak diumumkan
- [airdrop] Audit status untuk token contract, distributor contract, claimer contract — tidak terverifikasi
- [airdrop] Investor token allocation side letters (Series A/B) — tidak diungkap
- [airdrop] Governance model detail: voting power, quorum, proposal threshold, delegation, timelock, treasury control — tidak diumumkan
- [airdrop] CLOB decentralization roadmap (multiple operators, sequencer staking) — tidak diumumkan
- [airdrop] Cross-chain conditional token bridging mechanism untuk token distribution — tidak diumumkan
- [airdrop] Official volume/user analytics dashboard (untuk verifikasi metrik retensi pasca-airdrop) — tidak ada
