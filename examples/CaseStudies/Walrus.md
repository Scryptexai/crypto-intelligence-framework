# Walrus — Deep Case Study (Phased)

**CIF Dataset — Deep Dossier · Tier: Deep (anchor project)**
**Source:** Deep Research (DeepSeek), Format v3 Dependency Pipeline (12/11 phases: foundation, entity, history, technology, financial, token, ecosystem, market, behavioral, knowledge, conflict, airdrop). **Auto-assembled** by `tools/ingest.py` (deterministic, no LLM, strict data_project/ contract) — each phase extracted and concatenated in dependency order per `docs/Protocol/Deep-Research-Brief.md`; the reasoning is the source reports'.
**Raw sources archived:** doc_backup/deep/Walrus_foundation_2026-08.docx, doc_backup/deep/Walrus_entity_2026-08.docx, doc_backup/deep/Walrus_history_2026-08.docx, doc_backup/deep/Walrus_technology_2026-08.docx, doc_backup/deep/Walrus_financial_2026-08.docx, doc_backup/deep/Walrus_token_2026-08.docx, doc_backup/deep/Walrus_ecosystem_2026-08.docx, doc_backup/deep/Walrus_market_2026-08.docx, doc_backup/deep/Walrus_behavioral_2026-08.docx, doc_backup/deep/Walrus_knowledge_2026-08.docx, doc_backup/deep/Walrus_conflict_2026-08.docx, doc_backup/deep/Walrus_airdrop_2026-08.docx.
**Phases not run:** none.

> Faithful concatenation of phase outputs — no fabrication, no distillation beyond what the closing phase (Conflict Resolution / Validation) itself states. Consider a periodic QC pass.

---
## Foundation Intelligence
_ref: `docs/Ontology/Identity.md`, `docs/Ontology/Team.md`_

PROJECT: Walrus
Official Name: Walrus
Symbol: WAL
Category: Decentralized programmable data storage protocol (blob storage) di atas Sui
Founding Entity: Mysten Labs (pengembang awal; tim di balik Sui); Walrus Foundation (non-profit, pengarah protokol pasca token sale) (HIGH) [CoinDesk Walrus raises $140M, https://www.coindesk.com/business/2025/03/20/data-storage-protocol-walrus-raises-usd140m-in-token-sale-ahead-of-mainnet-launch]
Founders: Evan Cheng (CEO Mysten Labs); Sam Blackshear (co-founder, pencipta bahasa Move); Adeniyi Abiodun (co-founder); George Danezis (co-founder); Kostas Chalkias (co-founder) — pendiri Mysten Labs, organisasi induk Walrus (HIGH) [Backpack Exchange Walrus overview, https://learn.backpack.exchange/articles/what-is-walrus-a-programmable-decentralized-storage-network]; [Altcoin Buzz Walrus TGE, https://www.altcoinbuzz.io/reviews/walrus-protocol-mainnet-and-tge-are-coming/]
Core Team: Tim engineering Mysten Labs yang mengembangkan Walrus sejak inkubasi; Walrus Foundation managing executive: Rebecca Simmonds; ukuran tim Walrus spesifik tidak dipublikasikan terpisah (MEDIUM) [CoinDesk, https://www.coindesk.com/business/2025/03/20/data-storage-protocol-walrus-raises-usd140m-in-token-sale-ahead-of-mainnet-launch]
Country: Mysten Labs berbasis di Amerika Serikat (Palo Alto); Walrus Foundation yurisdiksi non-profit (tidak dirinci publik) (MEDIUM) [Altcoin Buzz, https://www.altcoinbuzz.io/reviews/walrus-protocol-mainnet-and-tge-are-coming/]
Launch Date - Testnet: Desember 2024 (fase testnet publik sebelum mainnet; tanggal persis tidak dirinci di sumber yang diakses) (MEDIUM) [Imperator Walrus overview, https://www.imperator.co/resources/blog/walrus-protocol]
Launch Date - Mainnet: 2025-03-27 (HIGH) [CoinDesk, https://www.coindesk.com/business/2025/03/20/data-storage-protocol-walrus-raises-usd140m-in-token-sale-ahead-of-mainnet-launch]; [Backpack Exchange, https://learn.backpack.exchange/articles/what-is-walrus-a-programmable-decentralized-storage-network]
Launch Date - TGE: 2025-03-27 (WAL token live bersamaan mainnet; airdrop komunitas didistribusikan bertahap pasca-TGE) (HIGH) [Altcoin Buzz, https://www.altcoinbuzz.io/product-release/crypto-gem-sui-is-launching-a-new-altcoin-today-walrus-wal/]
Main Products: Walrus blob storage network (penyimpanan file/AI model/dataset besar terdesentralisasi); WAL token (pembayaran storage, staking, governance); integrasi Sui Move smart contracts untuk metadata & kepemilikan blob; Walrus Sites (hosting konten) (HIGH) [Backpack Exchange, https://learn.backpack.exchange/articles/what-is-walrus-a-programmable-decentralized-storage-network]
Official Website: https://walrus.xyz (HIGH)
Repository: https://github.com/MystenLabs/walrus (HIGH) [GitHub MystenLabs, https://github.com/MystenLabs]
Documentation: https://docs.walrus.xyz (HIGH)
Social - X/Twitter: @WalrusProtocol (HIGH) [Altcoin Buzz, https://www.altcoinbuzz.io/reviews/walrus-protocol-mainnet-and-tge-are-coming/]
Social - Discord: https://discord.gg/walrus (MEDIUM)
Social - Telegram: tidak ada kanal Telegram resmi utama (MEDIUM)
Block Explorer: https://suiscan.xyz dan https://suivision.org (explorer ekosistem Sui untuk kontrak Walrus) (MEDIUM)
Token Contract: WAL adalah token native dengan kontrak di Sui (alamat kontrak per dokumentasi resmi; tidak dirinci di sumber yang diakses) (LOW)
Chain(s): Sui (Layer 1); Walrus berjalan sebagai protokol storage terpisah yang berkoordinasi via smart contract Sui (HIGH) [Backpack Exchange, https://learn.backpack.exchange/articles/what-is-walrus-a-programmable-decentralized-storage-network]
Ecosystem: Sui ecosystem; AI/decentralized data (penyimpanan model AI, dataset); partner termasuk Lombard (likuiditas BTC di Sui) dan proyek kredit/storage lain (MEDIUM) [Altcoin Buzz, https://www.altcoinbuzz.io/product-release/crypto-gem-sui-is-launching-a-new-altcoin-today-walrus-wal/]

## Entity Intelligence
_ref: `docs/Ontology/Relationships.md` (entity graph)_

PROJECT: Walrus

Entity: Mysten Labs
Type: Organization
Relationship: Pengembang awal Walrus dan pencipta Sui; core contributors Walrus berasal dari tim Mysten Labs; menerima alokasi 30% supply WAL (kategori Core Contributors bersama early contributors)
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Backpack Exchange, https://learn.backpack.exchange/articles/what-is-walrus-a-programmable-decentralized-storage-network]; (MEDIUM) [Altcoin Buzz, https://www.altcoinbuzz.io/reviews/walrus-protocol-mainnet-and-tge-are-coming/]

---
Entity: Walrus Foundation
Type: Foundation
Relationship: Entitas non-profit pengarah protokol Walrus pasca token sale; pelaksana $140M token sale dan pengelola arah pengembangan jaringan
Period: 2025–sekarang
Exposure Type: financial-collateral
Evidence: (HIGH) [CoinDesk, https://www.coindesk.com/business/2025/03/20/data-storage-protocol-walrus-raises-usd140m-in-token-sale-ahead-of-mainnet-launch]

---
Entity: Evan Cheng
Type: Person
Relationship: CEO Mysten Labs, organisasi induk yang mengembangkan Walrus
Period: 2021–sekarang
Exposure Type: governance
Evidence: (MEDIUM) [Backpack Exchange, https://learn.backpack.exchange/articles/what-is-walrus-a-programmable-decentralized-storage-network]

---
Entity: Sam Blackshear
Type: Person
Relationship: Co-founder Mysten Labs dan pencipta bahasa Move (bahasa smart contract Sui yang juga dipakai kontrak Walrus)
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Backpack Exchange, https://learn.backpack.exchange/articles/what-is-walrus-a-programmable-decentralized-storage-network]

---
Entity: Adeniyi Abiodun
Type: Person
Relationship: Co-founder Mysten Labs; menyatakan publik bahwa airdrop WAL akan menjadi salah satu yang terbesar dan paling terdistribusi dalam sejarah crypto (Maret 2025)
Period: 2021–sekarang
Exposure Type: governance
Evidence: (MEDIUM) [Altcoin Buzz, https://www.altcoinbuzz.io/reviews/walrus-protocol-mainnet-and-tge-are-coming/]

---
Entity: Rebecca Simmonds
Type: Person
Relationship: Managing executive Walrus Foundation; juru bicara resmi token sale $140M dan peluncuran mainnet
Period: 2025–sekarang
Exposure Type: governance
Evidence: (HIGH) [CoinDesk, https://www.coindesk.com/business/2025/03/20/data-storage-protocol-walrus-raises-usd140m-in-token-sale-ahead-of-mainnet-launch]

---
Entity: Sui Network
Type: Protocol
Relationship: Layer-1 tempat Walrus dibangun — smart contract Sui mengelola metadata, kepemilikan, dan siklus hidup blob; staking dan koordinasi jaringan memanfaatkan infrastruktur Sui
Period: 2024–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [CoinDesk, https://www.coindesk.com/business/2025/03/20/data-storage-protocol-walrus-raises-usd140m-in-token-sale-ahead-of-mainnet-launch]; (HIGH) [Backpack Exchange, https://learn.backpack.exchange/articles/what-is-walrus-a-programmable-decentralized-storage-network]

---
Entity: Standard Crypto
Type: Investor
Relationship: Lead investor token sale WAL $140 juta (pengumuman 20 Maret 2025)
Period: 2025–sekarang
Exposure Type: financial-collateral
Evidence: (HIGH) [CoinDesk, https://www.coindesk.com/business/2025/03/20/data-storage-protocol-walrus-raises-usd140m-in-token-sale-ahead-of-mainnet-launch]

---
Entity: a16z crypto
Type: Investor
Relationship: Partisipan token sale WAL $140 juta; juga investor historis Mysten Labs/Sui
Period: 2025–sekarang
Exposure Type: financial-collateral
Evidence: (HIGH) [CoinDesk, https://www.coindesk.com/business/2025/03/20/data-storage-protocol-walrus-raises-usd140m-in-token-sale-ahead-of-mainnet-launch]

---
Entity: Electric Capital
Type: Investor
Relationship: Partisipan token sale WAL $140 juta
Period: 2025–sekarang
Exposure Type: financial-collateral
Evidence: (HIGH) [CoinDesk, https://www.coindesk.com/business/2025/03/20/data-storage-protocol-walrus-raises-usd140m-in-token-sale-ahead-of-mainnet-launch]

---
Entity: Franklin Templeton Digital Assets
Type: Investor
Relationship: Partisipan token sale WAL $140 juta
Period: 2025–sekarang
Exposure Type: financial-collateral
Evidence: (HIGH) [CoinDesk, https://www.coindesk.com/business/2025/03/20/data-storage-protocol-walrus-raises-usd140m-in-token-sale-ahead-of-mainnet-launch]

---
Entity: RW3 Ventures
Type: Investor
Relationship: Partisipan token sale WAL $140 juta
Period: 2025–sekarang
Exposure Type: financial-collateral
Evidence: (HIGH) [CoinDesk, https://www.coindesk.com/business/2025/03/20/data-storage-protocol-walrus-raises-usd140m-in-token-sale-ahead-of-mainnet-launch]

---
Entity: Lombard
Type: Protocol
Relationship: Partner ekosistem Sui/Walrus — penyedia LBTC (Bitcoin berlikuiditas) di Sui; kolaborasi lintas-ekosistem diumumkan sekitar peluncuran WAL
Period: 2025–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Altcoin Buzz, https://www.altcoinbuzz.io/product-release/crypto-gem-sui-is-launching-a-new-altcoin-today-walrus-wal/]

---
Entity: MEXC
Type: Exchange
Relationship: Exchange terpusat pertama yang mengumumkan listing WAL pada TGE (27 Maret 2025), diikuti exchange lain
Period: 2025–sekarang
Exposure Type: financial-collateral
Evidence: (MEDIUM) [Altcoin Buzz, https://www.altcoinbuzz.io/product-release/crypto-gem-sui-is-launching-a-new-altcoin-today-walrus-wal/]

---
Entity: Backpack Exchange
Type: Exchange
Relationship: Exchange yang me-listing WAL dan menerbitkan riset tokenomics WAL
Period: 2025–sekarang
Exposure Type: financial-collateral
Evidence: (MEDIUM) [Backpack Exchange, https://learn.backpack.exchange/articles/what-is-walrus-a-programmable-decentralized-storage-network]

## Historical Intelligence
_ref: `docs/Ontology/DecisionEvent.md` (factual spine — enriched later by Behavioral)_

PROJECT: Walrus

Event ID

EV-001

Date

2021

Event Name

Pendirian Mysten Labs oleh tim arsitek Sui

Event Type

Founding

Description

Evan Cheng, Sam Blackshear, Adeniyi Abiodun, George Danezis, dan Kostas Chalkias mendirikan Mysten Labs dan mengembangkan blockchain Sui beserta bahasa Move — fondasi organisasi dan teknologi tempat Walrus kemudian dibangun.

Participants

Evan Cheng; Sam Blackshear; Adeniyi Abiodun; George Danezis; Kostas Chalkias

Location

Palo Alto, Amerika Serikat (tim global)

Status

Completed

Immediate Result

Sui dikembangkan dan kemudian mainnet (Mei 2023); Mysten Labs menjadi organisasi induk Walrus.

Sources

https://learn.backpack.exchange/articles/what-is-walrus-a-programmable-decentralized-storage-network (MEDIUM)

---

Event ID

EV-002

Date

2024 (semester kedua)

Event Name

Pengembangan dan pengumuman Walrus sebagai protokol storage di Sui

Event Type

Product Announcement

Description

Mysten Labs mengembangkan Walrus, protokol penyimpanan blob terdesentralisasi (file besar, dataset AI, media) yang berkoordinasi melalui smart contract Sui, dengan teknologi erasure coding untuk redundansi data.

Participants

Mysten Labs; Walrus dev team

Location

Global

Status

Completed

Immediate Result

Arsitektur blob storage + erasure coding disiapkan menuju testnet.

Sources

https://www.imperator.co/resources/blog/walrus-protocol (MEDIUM)

---

Event ID

EV-003

Date

2024-12

Event Name

Peluncuran testnet Walrus

Event Type

Testnet Launch

Description

Walrus membuka testnet publik; pengguna dapat menyimpan blob, menjalankan storage node, dan berpartisipasi dalam campaign (termasuk Walrus Academy) yang kemudian dikaitkan dengan eligibility airdrop WAL.

Participants

Walrus dev team; komunitas testnet; storage node operators awal

Location

Global (testnet)

Status

Completed

Immediate Result

Partisipasi testnet besar (didorong komunitas Sui); kesiapan mainnet diverifikasi bertahap.

Sources

https://learn.backpack.exchange/articles/what-is-walrus-a-programmable-decentralized-storage-network (MEDIUM)

---

Event ID

EV-004

Date

2025-03-20

Event Name

Token sale WAL $140 juta dipimpin Standard Crypto

Event Type

Funding

Description

Walrus Foundation mengumumkan private token sale WAL senilai $140 juta — fundraising pertama khusus untuk Walrus (terpisah dari fundraising Sui/Mysten) — dipimpin Standard Crypto dengan partisipasi a16z crypto, Electric Capital, Franklin Templeton Digital Assets, dan RW3 Ventures; dana untuk memperluas jaringan storage dan tooling.

Participants

Walrus Foundation; Standard Crypto; a16z crypto; Electric Capital; Franklin Templeton Digital Assets; RW3 Ventures; Rebecca Simmonds (managing executive)

Location

Global

Status

Completed

Immediate Result

$140.000.000 terkumpul seminggu sebelum mainnet; jadwal mainnet 27 Maret 2025 dikonfirmasi publik.

Sources

https://www.coindesk.com/business/2025/03/20/data-storage-protocol-walrus-raises-usd140m-in-token-sale-ahead-of-mainnet-launch (HIGH)

---

Event ID

EV-005

Date

2025-03-27

Event Name

Mainnet Walrus dan TGE WAL

Event Type

TGE

Description

Mainnet Walrus live dengan WAL sebagai token native pembayaran storage, staking, dan governance; TGE dilaksanakan bersamaan; MEXC mengumumkan listing hari pertama diikuti exchange lain dan DEX ekosistem Sui.

Participants

Walrus Foundation; Mysten Labs; storage node operators; komunitas Sui; MEXC; Backpack Exchange

Location

Global

Status

Completed

Immediate Result

Jaringan storage produksi berjalan dengan token ekonomis aktif; distribusi airdrop komunitas dimulai bertahap.

Sources

https://www.altcoinbuzz.io/product-release/crypto-gem-sui-is-launching-a-new-altcoin-today-walrus-wal/ (MEDIUM); https://learn.backpack.exchange/articles/what-is-walrus-a-programmable-decentralized-storage-network (MEDIUM)

---

Event ID

EV-006

Date

2025-03 hingga 2025 (berlanjut)

Event Name

Distribusi airdrop komunitas WAL (4% pre-mainnet + 6% post-mainnet)

Event Type

Airdrop

Description

10% total supply WAL dialokasikan ke komunitas: 4% didistribusikan segera pasca-mainnet (klaim via portal resmi untuk wallet eligible dari aktivitas testnet/kampanye) dan 6% didistribusikan bertahap seiring kematangan ekosistem; co-founder Mysten menyebutnya salah satu airdrop terbesar dan paling terdistribusi.

Participants

Walrus Foundation; komunitas testnet/mainnet; pemegang/pengguna ekosistem Sui

Location

Global

Status

Ongoing (fase bertahap)

Immediate Result

Klaim pre-mainnet 4% berjalan pasca-TGE; gelombang lanjutan post-mainnet berjalan sepanjang 2025.

Sources

https://learn.backpack.exchange/articles/what-is-walrus-a-programmable-decentralized-storage-network (MEDIUM); https://www.altcoinbuzz.io/reviews/walrus-protocol-mainnet-and-tge-are-coming/ (MEDIUM)

## Technology Intelligence
_ref: `docs/Ontology/Technology.md`_

PROJECT: Walrus

## System Architecture

**Decentralized blob storage layer di atas Sui**
Walrus adalah protokol penyimpanan data besar (blob: file, gambar, video, dataset AI, model AI, aset game) yang berjalan berdampingan dengan blockchain Sui. Metadata, kepemilikan, dan siklus hidup blob dikelola smart contract Sui (Move), sementara isi data disimpan jaringan storage node terpisah — pemisahan yang membuat penyimpanan skala besar tidak membebani throughput chain. (HIGH) [Backpack Exchange, https://learn.backpack.exchange/articles/what-is-walrus-a-programmable-decentralized-storage-network]; [CoinDesk, https://www.coindesk.com/business/2025/03/20/data-storage-protocol-walrus-raises-usd140m-in-token-sale-ahead-of-mainnet-launch]

**Programmable & verifiable storage**
Data yang disimpan bersifat dinamis, terverifikasi, dan dapat diprogram — blob dapat dirujuk, dipindahkan, dan dikelola via kontrak (sesuai positioning "storage isn't just storage anymore: dynamic, verifiable, programmable"). (HIGH) [Altcoin Buzz, https://www.altcoinbuzz.io/reviews/walrus-protocol-mainnet-and-tge-are-coming/]

**Modular Components**
- Client/Publisher SDK: library untuk encode, publish, dan baca blob (Rust; SDK developer)
- Storage Nodes: operator independen yang menyimpan shard blob dan melayani pembacaan
- Erasure Coding Layer: redundansi matematis ("Red Stuff") agar blob tetap dapat direkonstruksi walau sebagian node hilang/gagal
- Sui Smart Contracts (Move): registrasi blob, kepemilikan, pembayaran storage, dan staking WAL
- Aggregator/indexer: layanan bantu untuk ketersediaan dan akses blob (ekosistem)
(MEDIUM) [Imperator Walrus overview, https://www.imperator.co/resources/blog/walrus-protocol]; [Backpack Exchange, https://learn.backpack.exchange/articles/what-is-walrus-a-programmable-decentralized-storage-network]

**Cross-chain/chain relationship**
Walrus bukan L1/L2 sendiri — ia protokol storage yang memakai Sui sebagai lapisan koordinasi dan ekonomi; tidak ada consensus terpisah Walrus; keamanan dan finality metadata mengikuti Sui. (HIGH) [Backpack Exchange, https://learn.backpack.exchange/articles/what-is-walrus-a-programmable-decentralized-storage-network]

## Core Components

- Blob: unit data immutable (atau mutable via kepemilikan kontrak) yang dipecah menjadi shard ter-erasure-code
- Storage epoch: periode operasional tempat staker memvalidasi storage proofs dan parameter jaringan diperbarui; reward dibagikan per epoch
- WAL staking pada storage nodes: partisipasi staker dalam validasi dan keamanan jaringan storage (HIGH) [Backpack Exchange, https://learn.backpack.exchange/articles/what-is-walrus-a-programmable-decentralized-storage-network]

## Consensus Mechanism

Consensus: Walrus mewarisi mekanisme konsensus Sui untuk seluruh state on-chain (metadata, kepemilikan, staking); jaringan storage sendiri memakai proof/validasi per epoch alih-alih consensus Nakamoto terpisah (MEDIUM) [Backpack Exchange, https://learn.backpack.exchange/articles/what-is-walrus-a-programmable-decentralized-storage-network]

## Execution Environment

Execution Environment: Move VM di Sui untuk seluruh logika kontrak Walrus (registrasi blob, pembayaran, staking); aplikasi klien berjalan off-chain dengan SDK (MEDIUM) [Backpack Exchange, https://learn.backpack.exchange/articles/what-is-walrus-a-programmable-decentralized-storage-network]

## Security Model

Security Model: Redundansi erasure coding menjamin ketersediaan data walau sebagian storage node gagal/hilang; staking + validasi per epoch memberi insentif ekonomi bagi node jujur; mekanisme burn/penalti pada stake shifts direncanakan sebagai tekanan deflasioner dan disinsentif perilaku buruk (MEDIUM) [Backpack Exchange, https://learn.backpack.exchange/articles/what-is-walrus-a-programmable-decentralized-storage-network]

## Audit History

Audit History: tidak ditemukan laporan audit publik spesifik Walrus di sumber yang diakses riset ini — perlu verifikasi langsung ke Walrus Foundation/dokumentasi resmi (LOW)

## Technical Upgrade History

Technical Upgrade History: Testnet (Desember 2024) → Mainnet (27 Maret 2025) dengan token ekonomis aktif; upgrade mayor pasca-mainnet tidak dirinci di sumber yang diakses (MEDIUM) [Imperator, https://www.imperator.co/resources/blog/walrus-protocol]

## Current Technical Stack

Current Technical Stack: Rust (node & SDK), Move smart contracts di Sui, erasure coding layer, portal klaim/UX web; explorer via Suiscan/SuiVision untuk kontrak terkait (MEDIUM) [GitHub MystenLabs, https://github.com/MystenLabs]

## Known Technical Limitations

Known Technical Limitations: Sentralisasi pengembangan awal di Mysten Labs (kode dikembangkan satu organisasi sebelum transisi foundation); ketergantungan pada ketersediaan/keamanan Sui untuk lapisan koordinasi; detail desentralisasi storage node set (jumlah, distribusi geografis) tidak dipublikasikan penuh (MEDIUM) [Backpack Exchange, https://learn.backpack.exchange/articles/what-is-walrus-a-programmable-decentralized-storage-network]

## Official Technical Resources

Official Technical Resources: https://github.com/MystenLabs/walrus (HIGH); https://docs.walrus.xyz (HIGH)

## Financial Intelligence
_ref: `docs/Ontology/Funding.md`, `docs/Ontology/Revenue.md`_

PROJECT: Walrus

## Funding History

### Funding Round: Mysten Labs Seed Round
Date: 2021
Amount: $36M
Currency: USD
Lead Investor: a16z crypto
Participating Investors: Consortium of strategic angels
Valuation: Tidak diungkap
Funding Type: Seed
Status: Completed
Sources: https://www.mystenlabs.com/blog/mysten-labs-raises-36m-series-a

### Funding Round: Mysten Labs Series A
Date: December 2021
Amount: $92M
Currency: USD
Lead Investor: a16z crypto
Participating Investors: Coinbase Ventures, Circle, Slow Ventures, Samsung Next, others
Valuation: Tidak diungkap
Funding Type: Series A
Status: Completed
Sources: https://www.mystenlabs.com/blog/mysten-labs-raises-92m-series-a

### Funding Round: Mysten Labs Series B
Date: September 2022
Amount: $300M
Currency: USD
Lead Investor: FTX Ventures
Participating Investors: a16z crypto, Coinbase Ventures, Circle, Slow Ventures, others
Valuation: $2B+
Funding Type: Series B
Status: Completed
Sources: https://www.mystenlabs.com/blog/mysten-labs-raises-300m-series-b

### Funding Round: Walrus-Specific Funding
Date: Tidak diungkap
Amount: Tidak diungkap
Currency: USD
Lead Investor: Tidak diungkap
Participating Investors: Tidak diungkap
Valuation: Tidak diungkap
Funding Type: N/A
Status: Tidak diungkap
Sources: https://walrus.xyz/, https://www.mystenlabs.com/
Evidence: Walrus adalah produk protocol dari Mysten Labs, tidak memiliki ronde pendanaan terpisah yang diumumkan secara publik

## Treasury

Current Treasury Size: Tidak diungkap
Treasury Composition: Tidak diungkap
Stablecoin Holdings: Tidak diungkap
Native Token Holdings: Tidak diungkap
Other Assets: Tidak diungkap
Treasury Custodian: Tidak diungkap
Sources: https://walrus.xyz/, https://www.mystenlabs.com/, https://github.com/MystenLabs/walrus
Note: Tidak ada transparency report atau treasury dashboard resmi yang diterbitkan untuk Walrus protocol secara terpisah dari Mysten Labs/Sui Foundation

## Revenue Model

### Revenue Stream: Protocol Storage Fees
Nama: Blob Storage Fees
Status: Planned
Description: Biaya penyimpanan blob data pada jaringan Walrus, dibayar dalam SUI atau WAL token
Sources: https://walrus.xyz/docs/, https://github.com/MystenLabs/walrus/blob/main/docs/tokenomics.md

### Revenue Stream: Read/Retrieval Fees
Nama: Data Retrieval Fees
Status: Planned
Description: Biaya untuk mengambil/membaca data yang tersimpan
Sources: https://walrus.xyz/docs/

### Revenue Stream: Validator/Storage Node Rewards
Nama: Storage Node Rewards Distribution
Status: Planned
Description: Bagian dari fee yang didistribusikan ke storage node operators
Sources: https://walrus.xyz/docs/

## Revenue History

Tidak diungkap.
Sources: https://walrus.xyz/, https://www.mystenlabs.com/
Note: Walrus baru meluncurkan testnet (2024) dan mainnet belum live secara penuh, belum ada revenue history yang dipublikasikan

## Fundraising Mechanism

VC Funding: Ya (via Mysten Labs - a16z crypto, FTX Ventures, Coinbase Ventures, dll)
Private Sale: Tidak diungkap (khusus WAL token)
Public Sale: Tidak diungkap
Grant: Ya (Sui Foundation ecosystem grants untuk builders di atas Walrus)
Foundation: Ya (Mysten Labs, Sui Foundation)
DAO Treasury: Belum terbentuk (Walrus Foundation direncanakan)
Protocol Revenue: Belum live
Bootstrapping: Tidak (didukung oleh treasury Mysten Labs)
Sources: https://www.mystenlabs.com/blog/, https://sui.io/foundation/grants, https://walrus.xyz/

## Token Sale

### Private Sale: WAL Token
Tanggal: Tidak diungkap
Status: Tidak diungkap / Belum diumumkan
Sources: https://walrus.xyz/, https://github.com/MystenLabs/walrus
Note: Tidak ada informasi resmi mengenai private sale WAL token

### Public Sale: WAL Token
Tanggal: Tidak diungkap
Status: Tidak diungkap / Belum diumumkan
Sources: https://walrus.xyz/
Note: Tidak ada informasi resmi mengenai public sale WAL token

### Launchpad: WAL Token
Tanggal: Tidak diungkap
Status: Tidak diungkap
Sources: https://walrus.xyz/

### Auction: WAL Token
Tanggal: Tidak diungkap
Status: Tidak diungkap
Sources: https://walrus.xyz/

### Community Sale: WAL Token
Tanggal: Tidak diungkap
Status: Tidak diungkap
Sources: https://walrus.xyz/

## Financial Dependencies

### Dependency: Mysten Labs
Type: VC-Backed Parent Company
Description: Entitas induk yang mengembangkan dan mendanai pengembangan Walrus
Sources: https://www.mystenlabs.com/, https://www.mystenlabs.com/blog/mysten-labs-raises-300m-series-b

### Dependency: Sui Foundation
Type: Foundation / Grant Program
Description: Menyediakan ekosystem grants untuk proyek yang membangun di atas Walrus/Sui
Sources: https://sui.io/foundation/grants

### Dependency: a16z crypto
Type: VC / Lead Investor Series A & Seed
Description: Investor utama Mysten Labs sejak tahap awal
Sources: https://www.mystenlabs.com/blog/mysten-labs-raises-92m-series-a

### Dependency: FTX Ventures (Historical)
Type: VC / Lead Investor Series B
Description: Lead investor Series B ($300M) - status kompleks pasca-kollapse FTX
Sources: https://www.mystenlabs.com/blog/mysten-labs-raises-300m-series-b

### Dependency: Future Walrus DAO/Foundation
Type: DAO Treasury (Planned)
Description: Direncanakan untuk governance dan pengelolaan treasury protocol
Sources: https://walrus.xyz/docs/, https://github.com/MystenLabs/walrus

## Financial Risk

### Risk: Treasury Concentration in Parent Company
Description: Walrus bergantung sepenuhnya pada treasury Mysten Labs; tidak ada treasury terpisah yang transparan
Sources: https://www.mystenlabs.com/, https://walrus.xyz/
Evidence Level: MEDIUM (inferensi dari struktur organisasi)

### Risk: FTX Ventures Exposure
Description: Series B dipimpin oleh FTX Ventures ($300M); kollapse FTX menciptakan ketidakpastian pada status equity dan potensi clawback
Sources: https://www.mystenlabs.com/blog/mysten-labs-raises-300m-series-b, https://www.coindesk.com/business/2022/11/11/mysten-labs-ftx-venture-investment/
Evidence Level: HIGH (banyak dilaporkan media kredibel)

### Risk: No Live Protocol Revenue
Description: Protocol belum menghasilkan revenue; seluruh operasi didanai dari treasury VC
Sources: https://walrus.xyz/, https://www.mystenlabs.com/
Evidence Level: HIGH (fakta operasional)

### Risk: Token Launch Uncertainty
Description: WAL token belum diluncurkan; tokenomics dan distribusi belum difinalisasi secara publik
Sources: https://walrus.xyz/, https://github.com/MystenLabs/walrus
Evidence Level: MEDIUM (berdasarkan roadmap publik)

## Official Financial Resources

Official Blog: https://www.mystenlabs.com/blog/
Walrus Blog: https://walrus.xyz/blog/
Transparency Report: Tidak tersedia
Treasury Dashboard: Tidak tersedia
Governance: https://gov.sui.io/ (Sui governance, belum ada Walrus-specific)
Messari: https://messari.io/project/sui (covers Sui ecosystem termasuk Walrus)
Token Terminal: https://tokenterminal.com/terminal/projects/sui
DefiLlama: https://defillama.com/chain/Sui
CryptoRank: https://cryptorank.io/ico/mysten-labs
Whitepaper: https://walrus.xyz/whitepaper.pdf, https://github.com/MystenLabs/walrus/blob/main/docs/whitepaper.md

## RINGKASAN

Total Funding Raised: ~$428M (via Mysten Labs: $36M Seed + $92M Series A + $300M Series B)
Funding Rounds: 3 ronde (Seed, Series A, Series B) semua di level Mysten Labs, tidak ada ronde terpisah untuk Walrus
Treasury Status: Tidak diungkap (tidak ada transparency report terpisah untuk Walrus)
Revenue Sources: Planned - blob storage fees, retrieval fees, validator rewards (belum live)
Revenue Availability: Tidak tersedia (belum ada revenue history)

## Token Intelligence
_ref: `docs/Ontology/Tokenomics.md`_

PROJECT: Walrus

## Token Information

Official Token Name: Walrus
Symbol: WAL
Token Standard: Native token dengan kontrak di Sui (SPL-style Sui coin)
Blockchain: Sui
Contract Address: tidak dirinci di sumber yang diakses (lihat Open Threads) (LOW)
Decimals: tidak dirinci di sumber yang diakses (LOW)
Status: Live (TGE 27 Maret 2025) (HIGH) [Altcoin Buzz, https://www.altcoinbuzz.io/product-release/crypto-gem-sui-is-launching-a-new-altcoin-today-walrus-wal/]
Sources: https://www.altcoinbuzz.io/product-release/crypto-gem-sui-is-launching-a-new-altcoin-today-walrus-wal/ (MEDIUM)
Sources: https://learn.backpack.exchange/articles/what-is-walrus-a-programmable-decentralized-storage-network (MEDIUM)

## Supply

Maximum Supply: 5.000.000.000 WAL (5 miliar) (MEDIUM) [Backpack Exchange, https://learn.backpack.exchange/articles/what-is-walrus-a-programmable-decentralized-storage-network]
Total Supply: 5.000.000.000 WAL (MEDIUM) [Backpack Exchange, https://learn.backpack.exchange/articles/what-is-walrus-a-programmable-decentralized-storage-network]
Circulating Supply: ~690.000.000 WAL tersedia di launch (bagian Community Reserve yang cair awal); angka beredar real-time tidak dipublikasikan resmi di sumber yang diakses (MEDIUM) [Altcoin Buzz, https://www.altcoinbuzz.io/reviews/walrus-protocol-mainnet-and-tge-are-coming/]
Initial Supply: tidak dirinci terpisah dari total supply (LOW)
Supply Type: Fixed total supply dengan jadwal unlock/burn; mekanisme burn (penalti stake shifts) menambah tekanan deflasioner bertahap (MEDIUM) [Backpack Exchange, https://learn.backpack.exchange/articles/what-is-walrus-a-programmable-decentralized-storage-network]
Sources: https://learn.backpack.exchange/articles/what-is-walrus-a-programmable-decentralized-storage-network (MEDIUM)
Sources: https://www.altcoinbuzz.io/reviews/walrus-protocol-mainnet-and-tge-are-coming/ (MEDIUM)

## Distribution

Community Reserve: 43% (2,15 miliar WAL) — 690 juta tersedia di launch, sisanya linear unlock hingga Maret 2033 (MEDIUM) [Altcoin Buzz, https://www.altcoinbuzz.io/reviews/walrus-protocol-mainnet-and-tge-are-coming/]
Community Airdrop (bagian dari komunitas): 10% total supply — 4% pre-mainnet + 6% post-mainnet bertahap (MEDIUM) [Backpack Exchange, https://learn.backpack.exchange/articles/what-is-walrus-a-programmable-decentralized-storage-network]
Investors: 7% (350 juta WAL) — unlock dimulai 12 bulan setelah launch (MEDIUM) [Altcoin Buzz, https://www.altcoinbuzz.io/reviews/walrus-protocol-mainnet-and-tge-are-coming/]
Core Contributors (early contributors + Mysten Labs): 30% (1,5 miliar WAL) — berbagai mekanisme unlock (MEDIUM) [Altcoin Buzz, https://www.altcoinbuzz.io/reviews/walrus-protocol-mainnet-and-tge-are-coming/]; [Backpack Exchange, https://learn.backpack.exchange/articles/what-is-walrus-a-programmable-decentralized-storage-network]
Subsidies/Ecosystem/Foundation (sisa ~20%): untuk subsidi storage dan pertumbuhan ekosistem — rincian per sub-kategori tidak dipublikasikan penuh di sumber sekunder (LOW) [Backpack Exchange, https://learn.backpack.exchange/articles/what-is-walrus-a-programmable-decentralized-storage-network]
INKONSISTENSI: Altcoin Buzz menyebut "Community Reserve 43% = 690 juta token available at launch" sementara Backpack memecah "10% community airdrop (4% pre + 6% post)" dari supply 5 miliar — kedua angka dapat konsisten (690 juta = porsi cair awal dari reserve 43%, airdrop 10% adalah sub-alokasi) namun dokumen tokenomics resmi harus dirujuk untuk kepastian; Evidence Level MEDIUM untuk kedua sumber sekunder.
Advisors: tidak diketahui (tidak tercantum terpisah) (LOW)
Sources: https://www.altcoinbuzz.io/reviews/walrus-protocol-mainnet-and-tge-are-coming/ (MEDIUM)
Sources: https://learn.backpack.exchange/articles/what-is-walrus-a-programmable-decentralized-storage-network (MEDIUM)

## Vesting Schedule

Category: Community Reserve
Cliff: 0 (690 juta cair di launch)
Vesting: Linear unlock hingga Maret 2033 untuk sisanya (MEDIUM) [Altcoin Buzz, https://www.altcoinbuzz.io/reviews/walrus-protocol-mainnet-and-tge-are-coming/]
Unlock Frequency: Linear/bertahap (MEDIUM)
Current Status: Berjalan sejak 27 Maret 2025

Category: Investors
Cliff: 12 bulan (unlock pertama ~Maret 2026)
Vesting: jadwal pasca-cliff tidak dirinci publik (LOW)
Unlock Frequency: tidak dirinci (LOW)
Current Status: Cliff berjalan

Category: Core Contributors
Cliff: tidak dirinci publik
Vesting: berbagai mekanisme unlock (per tokenomics blog) — detail tidak dikutip penuh di sumber sekunder (LOW)
Unlock Frequency: tidak dirinci (LOW)
Current Status: Berjalan sejak TGE

## Utility

Utility 1: Pembayaran storage — seluruh biaya publish/extend blob dibayar dalam WAL (HIGH) [Backpack Exchange, https://learn.backpack.exchange/articles/what-is-walrus-a-programmable-decentralized-storage-network]
Utility 2: Staking — WAL di-stake ke storage nodes; staker memvalidasi storage proofs dan parameter jaringan per epoch, menerima reward epoch (HIGH) [Backpack Exchange, https://learn.backpack.exchange/articles/what-is-walrus-a-programmable-decentralized-storage-network]
Utility 3: Governance — WAL sebagai token governance protokol (MEDIUM) [Backpack Exchange, https://learn.backpack.exchange/articles/what-is-walrus-a-programmable-decentralized-storage-network]
Utility 4: Burn mechanism — penalti pada stake shifts dibakar, tekanan deflasioner jangka panjang (MEDIUM) [Backpack Exchange, https://learn.backpack.exchange/articles/what-is-walrus-a-programmable-decentralized-storage-network]

## Inflation / Deflation

Inflation/Deflation: Emisi reward epoch untuk staker (inflasioner bertahap per jadwal) diimbangi mekanisme burn penalti — net trajectory bergantung parameter yang tidak dirinci publik di sumber sekunder (LOW) [Backpack Exchange, https://learn.backpack.exchange/articles/what-is-walrus-a-programmable-decentralized-storage-network]

## Holder Distribution

Holder Distribution: tidak ditemukan data on-chain holder concentration yang dipublikasikan di sumber sekunder (LOW)

## Ecosystem Intelligence
_ref: `docs/Ontology/Community.md`, `docs/Ontology/Ecosystem.md`_

PROJECT: Walrus

## Ecosystem Position

Primary Sector: Decentralized Storage
Primary Sector Evidence Level: HIGH
Primary Sector Sources: https://walrus.xyz/, https://github.com/MystenLabs/walrus

Secondary Sector: Data Availability Layer
Secondary Sector Evidence Level: HIGH
Secondary Sector Sources: https://walrus.xyz/docs/, https://github.com/MystenLabs/walrus/blob/main/docs/whitepaper.md

Primary Chain: Sui
Primary Chain Evidence Level: HIGH
Primary Chain Sources: https://walrus.xyz/, https://sui.io/

Supported Chains: Sui (native), Planned cross-chain via Wormhole and other bridges
Supported Chains Evidence Level: MEDIUM
Supported Chains Sources: https://walrus.xyz/docs/, https://github.com/MystenLabs/walrus

## External Dependencies

Dependency Name: Sui Blockchain
Dependency Type: Chain
Purpose: Consensus layer, settlement, validator coordination, staking, governance
Criticality: Critical
Status: Live
Related Entity: Sui Foundation
Related Technology Component: Sui consensus (Narwhal/Bullshark), Move VM, Sui SDK
Sources: https://walrus.xyz/docs/, https://github.com/MystenLabs/walrus/blob/main/docs/whitepaper.md
Evidence Level: HIGH

Dependency Name: Mysten Labs
Dependency Type: Protocol (Developer/Infrastructure Provider)
Purpose: Core protocol development, testnet operation, initial validator set, SDK maintenance
Criticality: Critical
Status: Live
Related Entity: Mysten Labs
Related Technology Component: Walrus core protocol, Walrus CLI, Walrus SDK (TypeScript/Rust)
Sources: https://www.mystenlabs.com/, https://github.com/MystenLabs/walrus
Evidence Level: HIGH

Dependency Name: Wormhole
Dependency Type: Bridge
Purpose: Cross-chain messaging, enabling Walrus blob storage access from non-Sui chains
Criticality: High
Status: Planned / Beta
Related Entity: Wormhole Foundation
Related Technology Component: Wormhole NTT, Wormhole Gateway
Sources: https://walrus.xyz/blog/, https://wormhole.com/
Evidence Level: MEDIUM

Dependency Name: Sui Foundation
Dependency Type: Foundation / Grant Provider
Purpose: Ecosystem grants for builders, validator delegation program, community support
Criticality: High
Status: Live
Related Entity: Sui Foundation
Related Technology Component: Sui Foundation Delegation Program, Grant Program
Sources: https://sui.io/foundation/grants, https://sui.io/foundation/delegation
Evidence Level: HIGH

Dependency Name: a16z crypto
Dependency Type: VC / Financial Dependency
Purpose: Lead investor in Mysten Labs (Seed, Series A), strategic guidance
Criticality: Medium
Status: Live
Related Entity: a16z crypto
Related Technology Component: N/A (financial)
Sources: https://www.mystenlabs.com/blog/mysten-labs-raises-92m-series-a
Evidence Level: HIGH

Dependency Name: FTX Ventures (Historical)
Dependency Type: VC / Financial Dependency
Purpose: Lead investor Mysten Labs Series B ($300M) — status uncertain post-bankruptcy
Criticality: Medium
Status: Uncertain
Related Entity: FTX Ventures
Related Technology Component: N/A (financial)
Sources: https://www.mystenlabs.com/blog/mysten-labs-raises-300m-series-b, https://www.coindesk.com/business/2022/11/11/mysten-labs-ftx-venture-investment/
Evidence Level: HIGH

Dependency Name: Cloud Providers (AWS/GCP/Azure)
Dependency Type: Cloud / Infrastructure
Purpose: Testnet node hosting, RPC endpoints, CI/CD infrastructure
Criticality: Medium
Status: Live
Related Entity: Amazon Web Services, Google Cloud Platform, Microsoft Azure
Related Technology Component: Walrus testnet nodes, indexer infrastructure
Sources: https://github.com/MystenLabs/walrus/blob/main/docs/running-a-node.md
Evidence Level: MEDIUM

Dependency Name: Sui Name Service (SNS)
Dependency Type: Protocol / Service
Purpose: Human-readable names for Walrus blob addresses and sites
Criticality: Low
Status: Planned / Beta
Related Entity: Sui Name Service
Related Technology Component: SNS resolution integration
Sources: https://walrus.xyz/docs/, https://sns.xyz/
Evidence Level: LOW

## Major Integrations

Integration Name: Walrus + Sui Native Integration
Integrated With: Sui Blockchain
Purpose: Native blob storage for Sui smart contracts, Move VM execution environment, on-chain metadata
Status: Live (Testnet)
Related Historical Event ID: Testnet Launch 2024
Sources: https://walrus.xyz/docs/, https://github.com/MystenLabs/walrus
Evidence Level: HIGH

Integration Name: Walrus + Wormhole Cross-Chain
Integrated With: Wormhole
Purpose: Cross-chain blob storage access, multi-chain data availability
Status: Planned
Related Historical Event ID: N/A (Announced partnership)
Sources: https://walrus.xyz/blog/, https://wormhole.com/blog/
Evidence Level: MEDIUM

Integration Name: Walrus + Sui Name Service
Integrated With: Sui Name Service (SNS)
Purpose: Human-readable names for Walrus Sites and blob references
Status: Beta
Related Historical Event ID: N/A
Sources: https://walrus.xyz/docs/sites/, https://sns.xyz/
Evidence Level: MEDIUM

Integration Name: Walrus + Akord
Integrated With: Akord
Purpose: Secure data vault application using Walrus for decentralized storage backend
Status: Live (Testnet)
Related Historical Event ID: N/A
Sources: https://akord.com/, https://walrus.xyz/blog/
Evidence Level: MEDIUM

Integration Name: Walrus + Decrypt Media
Integrated With: Decrypt Media
Purpose: Decentralized content publishing and archiving using Walrus Sites
Status: Beta / Pilot
Related Historical Event ID: N/A
Sources: https://walrus.xyz/blog/, https://decrypt.co/
Evidence Level: LOW

Integration Name: Walrus + SuiPlay0x1
Integrated With: SuiPlay0x1 (Playtron/Mysten Labs gaming handheld)
Purpose: Game asset storage and distribution via Walrus
Status: Planned
Related Historical Event ID: N/A
Sources: https://walrus.xyz/blog/, https://www.mystenlabs.com/blog/
Evidence Level: LOW

## Infrastructure Providers

Provider: Mysten Labs (Testnet Operators)
Service: Testnet validator nodes, RPC endpoints, indexer nodes, faucet
Criticality: Critical
Status: Live
Sources: https://github.com/MystenLabs/walrus/blob/main/docs/running-a-node.md, https://walrus.xyz/docs/
Evidence Level: HIGH

Provider: Community Validators (Testnet)
Service: Storage nodes, validator nodes, RPC endpoints
Criticality: High
Status: Live (Testnet)
Sources: https://github.com/MystenLabs/walrus/blob/main/docs/running-a-node.md, https://discord.gg/sui
Evidence Level: MEDIUM

Provider: Shinami
Service: Node infrastructure (RPC, indexer, gas station) for Sui/Walrus developers
Criticality: Medium
Status: Live
Sources: https://shinami.com/, https://walrus.xyz/docs/
Evidence Level: MEDIUM

Provider: Ankr
Service: RPC endpoints, node hosting for Sui network (used by Walrus)
Criticality: Medium
Status: Live
Sources: https://www.ankr.com/rpc/sui/, https://walrus.xyz/docs/
Evidence Level: MEDIUM

Provider: Google Cloud Platform
Service: Cloud infrastructure for Mysten Labs testnet operations
Criticality: Medium
Status: Live
Sources: https://github.com/MystenLabs/walrus/blob/main/.github/workflows/
Evidence Level: LOW

## Exchange Ecosystem

Exchange: N/A (WAL token not yet launched)
Listing Status: Not Listed
Spot: N/A
Perpetual: N/A
OTC: N/A
Launchpool: N/A
Status: Not Applicable
Sources: https://walrus.xyz/, https://coinmarketcap.com/, https://coingecko.com/
Evidence Level: HIGH

## Wallet Ecosystem

Wallet: Sui Wallet (Official)
Support Type: Native Sui wallet, will support Walrus Sites and blob interactions
Status: Live (Sui Mainnet) / Planned (Walrus features)
Sources: https://wallet.sui.io/, https://walrus.xyz/docs/
Evidence Level: HIGH

Wallet: Suiet Wallet
Support Type: Sui ecosystem wallet, planned Walrus integration
Status: Live (Sui) / Planned (Walrus)
Sources: https://suiet.app/, https://walrus.xyz/docs/
Evidence Level: MEDIUM

Wallet: Ethos Wallet
Support Type: Sui ecosystem wallet, planned Walrus integration
Status: Live (Sui) / Planned (Walrus)
Sources: https://ethoswallet.xyz/, https://walrus.xyz/docs/
Evidence Level: MEDIUM

Wallet: Martian Wallet
Support Type: Sui ecosystem wallet
Status: Live (Sui) / Planned (Walrus)
Sources: https://martianwallet.xyz/, https://walrus.xyz/docs/
Evidence Level: MEDIUM

Wallet: Glass Wallet
Support Type: Sui ecosystem wallet
Status: Live (Sui) / Planned (Walrus)
Sources: https://glasswallet.xyz/, https://walrus.xyz/docs/
Evidence Level: LOW

Wallet: Ledger (Hardware)
Support Type: Hardware wallet support for Sui (via Ledger Live / blind signing)
Status: Live (Sui) / Planned (Walrus)
Sources: https://www.ledger.com/, https://walrus.xyz/docs/
Evidence Level: HIGH

## Developer Ecosystem

SDK: Walrus TypeScript SDK
API: Walrus HTTP API (blob store, read, delete, sites)
Developer Tools: Walrus CLI (walrus binary), Walrus Sites CLI
Open Source Repository: https://github.com/MystenLabs/walrus
Developer Portal: https://walrus.xyz/docs/
Hackathon: Sui Overflow (Sui Foundation hackathons include Walrus tracks), Sui Global Hackathons
Grant Program: Sui Foundation Grants (ecosystem builders on Walrus), Mysten Labs Builder Grants
Sources: https://github.com/MystenLabs/walrus, https://walrus.xyz/docs/, https://sui.io/foundation/grants, https://www.mystenlabs.com/grants
Evidence Level: HIGH

## Applications

Application: Walrus Sites
Category: Decentralized Web Hosting
Relationship: Core protocol application (static site hosting on Walrus blobs)
Status: Live (Testnet)
Sources: https://walrus.xyz/docs/sites/, https://github.com/MystenLabs/walrus/tree/main/sites
Evidence Level: HIGH

Application: Akord
Category: Secure Data Vault / Collaboration
Relationship: Built on Walrus (storage backend)
Status: Live (Testnet)
Sources: https://akord.com/, https://walrus.xyz/blog/
Evidence Level: MEDIUM

Application: Decrypt Media Archive
Category: Content Publishing / Archiving
Relationship: Pilot integration using Walrus Sites
Status: Beta
Sources: https://walrus.xyz/blog/, https://decrypt.co/
Evidence Level: LOW

Application: SuiPlay0x1 Game Asset Storage
Category: Gaming / Asset Distribution
Relationship: Planned integration for game asset storage
Status: Planned
Sources: https://walrus.xyz/blog/, https://www.mystenlabs.com/blog/
Evidence Level: LOW

Application: Walrus Encrypted Blobs (Seal Integration)
Category: Encrypted Storage / Access Control
Relationship: Protocol feature using Seal (threshold encryption on Sui)
Status: Live (Testnet)
Sources: https://walrus.xyz/docs/encryption/, https://github.com/MystenLabs/seal
Evidence Level: HIGH

## Governance Ecosystem

Foundation: Mysten Labs
Role: Core developer, testnet operator, initial governance steward
Sources: https://www.mystenlabs.com/, https://github.com/MystenLabs/walrus
Evidence Level: HIGH

Foundation: Sui Foundation
Role: Ecosystem grants, validator delegation, community governance for Sui (affects Walrus)
Sources: https://sui.io/foundation/, https://gov.sui.io/
Evidence Level: HIGH

DAO: Walrus Foundation (Planned)
Role: Future protocol governance, treasury management, parameter upgrades
Status: Not Yet Formed
Sources: https://walrus.xyz/docs/, https://github.com/MystenLabs/walrus/blob/main/docs/tokenomics.md
Evidence Level: MEDIUM

Council: Sui Validators (indirectly govern Walrus via Sui governance)
Role: Sui protocol upgrades affect Walrus; validator set operates storage nodes
Sources: https://gov.sui.io/, https://walrus.xyz/docs/
Evidence Level: HIGH

Committee: Walrus Testnet Committee (Mysten Labs + selected community validators)
Role: Testnet operations, parameter tuning, upgrade coordination
Sources: https://github.com/MystenLabs/walrus/blob/main/docs/testnet.md
Evidence Level: MEDIUM

Validator Group: Walrus Storage Node Operators
Role: Store and serve blobs, participate in proof-of-availability consensus
Status: Testnet (permissioned), Mainnet (planned permissionless)
Sources: https://github.com/MystenLabs/walrus/blob/main/docs/running-a-node.md
Evidence Level: HIGH

## Ecosystem Risks

Risk: Single Chain Dependency (Sui)
Description: Walrus is natively built on Sui; any critical Sui consensus failure, validator centralization, or governance issue directly impacts Walrus availability and security
Sources: https://walrus.xyz/docs/, https://github.com/MystenLabs/walrus/blob/main/docs/whitepaper.md
Evidence Level: HIGH

Risk: Centralized Testnet Operation
Description: Testnet validators and infrastructure primarily operated by Mysten Labs; limited decentralization currently
Sources: https://github.com/MystenLabs/walrus/blob/main/docs/running-a-node.md
Evidence Level: HIGH

Risk: Cloud Infrastructure Concentration
Description: Significant testnet infrastructure hosted on centralized cloud providers (GCP, AWS); potential censorship or outage risk
Sources: https://github.com/MystenLabs/walrus/blob/main/.github/workflows/
Evidence Level: MEDIUM

Risk: Bridge Dependency (Wormhole)
Description: Cross-chain functionality depends on Wormhole bridge security; bridge exploits could affect cross-chain Walrus operations
Sources: https://wormhole.com/, https://walrus.xyz/blog/
Evidence Level: MEDIUM

Risk: Financial Dependency on Mysten Labs Treasury
Description: No independent Walrus treasury; all development funded by Mysten Labs (VC-backed); Series B investor FTX Ventures in bankruptcy
Sources: https://www.mystenlabs.com/blog/mysten-labs-raises-300m-series-b, https://www.coindesk.com/business/2022/11/11/mysten-labs-ftx-venture-investment/
Evidence Level: HIGH

Risk: No Live Token / Governance Mechanism
Description: WAL token not launched; no on-chain governance for parameter changes or treasury management; protocol upgrades controlled by Mysten Labs
Sources: https://walrus.xyz/, https://github.com/MystenLabs/walrus
Evidence Level: HIGH

Risk: Limited Validator Set (Testnet)
Description: Testnet storage nodes are permissioned and limited in number; not representative of mainnet decentralization
Sources: https://github.com/MystenLabs/walrus/blob/main/docs/running-a-node.md
Evidence Level: HIGH

## Official Ecosystem Resources

Official Documentation: https://walrus.xyz/docs/
Developer Portal: https://walrus.xyz/docs/
GitHub: https://github.com/MystenLabs/walrus
Partner Documentation: https://wormhole.com/docs/, https://sns.xyz/docs/, https://shinami.com/docs/
Grant Program: https://sui.io/foundation/grants, https://www.mystenlabs.com/grants
Ecosystem Dashboard: https://suivision.xyz/ (Sui explorer, includes Walrus testnet), https://walruscan.com/ (planned)

## BUAT RINGKASAN

Primary Ecosystem: Sui (native), with planned cross-chain via Wormhole
Supported Chains: Sui (primary), Ethereum/Solana/others via Wormhole (planned)
External Dependencies: Sui Blockchain (Critical), Mysten Labs (Critical), Wormhole (High), Sui Foundation (High), a16z crypto (Medium), FTX Ventures (Medium, uncertain), Cloud Providers (Medium), SNS (Low)
Major Integrations: Sui Native (Live Testnet), Wormhole Cross-Chain (Planned), Sui Name Service (Beta), Akord (Live Testnet), Decrypt Media (Beta), SuiPlay0x1 (Planned), Seal Encryption (Live Testnet)
Infrastructure Providers: Mysten Labs (Critical), Community Validators (High), Shinami (Medium), Ankr (Medium), GCP (Medium)
Developer Programs: Walrus TS SDK, HTTP API, CLI, Sites CLI, Sui Foundation Grants, Mysten Labs Builder Grants, Sui Overflow Hackathons
Applications: Walrus Sites (Core, Live Testnet), Akord (Built on, Live Testnet), Decrypt Media Archive (Pilot, Beta), SuiPlay0x1 (Planned), Encrypted Blobs via Seal (Live Testnet)

## Market Intelligence
_ref: `docs/Meta/Narratives.md`, `docs/Valuation/Competitors.md`, `docs/Meta/MarketCycles.md`_

PROJECT: Walrus

## Market Category

Primary Category: Decentralized Storage (HIGH) [https://walrus.xyz/, https://github.com/MystenLabs/walrus]
Secondary Category: Data Availability Layer (HIGH) [https://walrus.xyz/docs/, https://github.com/MystenLabs/walrus/blob/main/docs/whitepaper.md]
Sector: DePIN (Decentralized Physical Infrastructure Networks) (HIGH) [https://walrus.xyz/, https://messari.io/project/sui]
Sub-sector: Blob Storage / Programmable Storage (HIGH) [https://walrus.xyz/docs/, https://github.com/MystenLabs/walrus/blob/main/docs/whitepaper.md]
Sources: https://walrus.xyz/, https://github.com/MystenLabs/walrus, https://walrus.xyz/docs/, https://github.com/MystenLabs/walrus/blob/main/docs/whitepaper.md, https://messari.io/project/sui

## Market Position

Project Stage: Pre-TGE / Testnet (HIGH) [https://walrus.xyz/, https://github.com/MystenLabs/walrus/blob/main/docs/testnet.md]
Primary Competitors: Filecoin, Arweave, Storj, Sia, 0G, Celestia (data availability), EigenDA (HIGH) [https://walrus.xyz/docs/, https://filecoin.io/, https://arweave.org/, https://storj.io/, https://0g.ai/, https://celestia.org/, https://eigenlayer.xyz/eigenda]
Market Segment: Developer-focused programmable storage for Sui ecosystem, expanding to cross-chain via Wormhole (HIGH) [https://walrus.xyz/docs/, https://walrus.xyz/blog/, https://wormhole.com/]
Geographic Focus: Global (no geographic restriction) (HIGH) [https://walrus.xyz/, https://github.com/MystenLabs/walrus]
Sources: https://walrus.xyz/, https://github.com/MystenLabs/walrus, https://walrus.xyz/docs/, https://github.com/MystenLabs/walrus/blob/main/docs/testnet.md, https://filecoin.io/, https://arweave.org/, https://storj.io/, https://0g.ai/, https://celestia.org/, https://eigenlayer.xyz/eigenda, https://walrus.xyz/blog/, https://wormhole.com/

## Trading Markets

Exchange: N/A (WAL token not yet launched)
Spot: Not Listed
Perpetual: Not Listed
Futures: Not Listed
Options: Not Listed
OTC: Not Listed
Status: Not Applicable — Token does not exist yet
Sources: https://walrus.xyz/, https://coinmarketcap.com/, https://coingecko.com/, https://github.com/MystenLabs/walrus

## Liquidity

Liquidity Source: None (Token not launched)
Major Liquidity Venue: N/A
DEX: N/A
CEX: N/A
Bridge Liquidity: N/A
Status: Not Applicable
Sources: https://walrus.xyz/, https://coinmarketcap.com/, https://coingecko.com/, https://defillama.com/chain/Sui

## Adoption Metrics

Metric Name: Testnet Storage Nodes
Value: ~50-100 permissioned nodes (estimated from testnet docs)
Date: 2024 (Testnet period)
Sources: https://github.com/MystenLabs/walrus/blob/main/docs/running-a-node.md, https://discord.gg/sui
Evidence Level: MEDIUM (inferred from testnet documentation, no public dashboard)

Metric Name: Testnet Blobs Stored
Value: Tidak diketahui (no public metrics dashboard)
Date: 2024
Sources: https://walrus.xyz/docs/, https://github.com/MystenLabs/walrus
Evidence Level: LOW (no public data)

Metric Name: Daily Active Users (Testnet)
Value: Tidak diketahui
Date: 2024
Sources: https://walrus.xyz/docs/, https://github.com/MystenLabs/walrus
Evidence Level: LOW (no public data)

Metric Name: Transactions (Testnet)
Value: Tidak diketahui
Date: 2024
Sources: https://walrus.xyz/docs/, https://github.com/MystenLabs/walrus
Evidence Level: LOW (no public data)

Metric Name: Wallets Interacting with Walrus
Value: Tidak diketahui
Date: 2024
Sources: https://walrus.xyz/docs/, https://github.com/MystenLabs/walrus
Evidence Level: LOW (no public data)

Metric Name: Developer Count (Walrus SDK downloads / GitHub stars)
Value: ~500+ GitHub stars on walrus repo (as of 2024)
Date: 2024
Sources: https://github.com/MystenLabs/walrus
Evidence Level: MEDIUM (public GitHub metric)

Metric Name: Volume (Storage Fees)
Value: $0 (Testnet uses test tokens, no real fees)
Date: 2024
Sources: https://walrus.xyz/docs/, https://github.com/MystenLabs/walrus/blob/main/docs/testnet.md
Evidence Level: HIGH (testnet uses test SUI)

Metric Name: Bridge Volume (Wormhole)
Value: N/A (Integration not live)
Date: 2024
Sources: https://walrus.xyz/blog/, https://wormhole.com/
Evidence Level: HIGH (announced but not deployed)

Metric Name: Messages (Cross-chain)
Value: N/A
Date: 2024
Sources: https://walrus.xyz/blog/, https://wormhole.com/
Evidence Level: HIGH

Metric Name: Validator Count (Storage Nodes)
Value: ~50-100 (Testnet, permissioned)
Date: 2024
Sources: https://github.com/MystenLabs/walrus/blob/main/docs/running-a-node.md
Evidence Level: MEDIUM

Sources: https://walrus.xyz/, https://github.com/MystenLabs/walrus, https://walrus.xyz/docs/, https://github.com/MystenLabs/walrus/blob/main/docs/testnet.md, https://github.com/MystenLabs/walrus/blob/main/docs/running-a-node.md, https://discord.gg/sui, https://walrus.xyz/blog/, https://wormhole.com/

## Market Share

Tidak tersedia. (Protocol in testnet, no live mainnet, no token, no revenue, no standardized market share metrics for decentralized storage protocols)
Sources: https://walrus.xyz/, https://github.com/MystenLabs/walrus, https://defillama.com/, https://tokenterminal.com/

## Competitor Landscape

Competitor: Filecoin
Category: Decentralized Storage (Layer 1 / Storage Network)
Difference: Filecoin uses Proof-of-Replication/Spacetime, FVM for compute; Walrus uses erasure coding + proof-of-availability on Sui, programmable via Move
Market Segment: General-purpose decentralized storage, enterprise, NFT.Storage, Web3.storage
Sources: https://filecoin.io/, https://walrus.xyz/docs/, https://github.com/MystenLabs/walrus/blob/main/docs/whitepaper.md
Evidence Level: HIGH

Competitor: Arweave
Category: Decentralized Permanent Storage (Layer 1)
Difference: Arweave focuses on permanent storage with endowment model; Walrus focuses on programmable, deletable blob storage with fee-based model
Market Segment: Permanent data, permaweb, NFT metadata
Sources: https://arweave.org/, https://walrus.xyz/docs/, https://github.com/MystenLabs/walrus/blob/main/docs/whitepaper.md
Evidence Level: HIGH

Competitor: Storj
Category: Decentralized Cloud Storage (S3-compatible)
Difference: Storj is S3-compatible, centralized satellite coordination; Walrus is native to Sui, smart-contract programmable, no S3 API
Market Segment: Developers needing S3-compatible, backup, video streaming
Sources: https://storj.io/, https://walrus.xyz/docs/, https://github.com/MystenLabs/walrus/blob/main/docs/whitepaper.md
Evidence Level: HIGH

Competitor: Sia / Skynet
Category: Decentralized Storage (Layer 1)
Difference: Sia uses host-renter contracts, Skynet provides portal layer; Walrus integrates directly with Move VM on Sui
Market Segment: General storage, CDN via Skynet
Sources: https://sia.tech/, https://walrus.xyz/docs/, https://github.com/MystenLabs/walrus/blob/main/docs/whitepaper.md
Evidence Level: HIGH

Competitor: 0G (ZeroGravity)
Category: Data Availability / AI-focused Storage (Layer 1)
Difference: 0G targets AI workloads with high throughput DA; Walrus targets general programmable storage on Sui
Market Segment: AI data, high-throughput DA, modular blockchain
Sources: https://0g.ai/, https://walrus.xyz/docs/, https://github.com/MystenLabs/walrus/blob/main/docs/whitepaper.md
Evidence Level: HIGH

Competitor: Celestia
Category: Data Availability Layer (Modular Blockchain)
Difference: Celestia provides DA for rollups via blobstream; Walrus provides programmable blob storage with on-chain logic via Move
Market Segment: Rollup DA, sovereign chains
Sources: https://celestia.org/, https://walrus.xyz/docs/, https://github.com/MystenLabs/walrus/blob/main/docs/whitepaper.md
Evidence Level: HIGH

Competitor: EigenDA
Category: Data Availability Layer (EigenLayer AVS)
Difference: EigenDA secured by ETH restaking, serves Ethereum rollups; Walrus secured by Sui validators, serves Sui + cross-chain
Market Segment: Ethereum rollup DA
Sources: https://eigenlayer.xyz/eigenda, https://walrus.xyz/docs/, https://github.com/MystenLabs/walrus/blob/main/docs/whitepaper.md
Evidence Level: HIGH

Sources: https://filecoin.io/, https://arweave.org/, https://storj.io/, https://sia.tech/, https://0g.ai/, https://celestia.org/, https://eigenlayer.xyz/eigenda, https://walrus.xyz/docs/, https://github.com/MystenLabs/walrus/blob/main/docs/whitepaper.md

## Narrative Position

Narrative: DePIN (Decentralized Physical Infrastructure Networks)
Status: Main Narrative
Evidence: Walrus positioned as programmable storage layer for Sui ecosystem, marketed as DePIN infrastructure
Sources: https://walrus.xyz/, https://messari.io/project/sui, https://github.com/MystenLabs/walrus
Evidence Level: HIGH

Narrative: Modular Blockchain / Data Availability
Status: Secondary Narrative
Evidence: Walrus provides DA-like blob storage for Sui and cross-chain via Wormhole; compared to Celestia/EigenDA in technical discussions
Sources: https://walrus.xyz/docs/, https://github.com/MystenLabs/walrus/blob/main/docs/whitepaper.md, https://wormhole.com/
Evidence Level: MEDIUM

Narrative: Programmable Storage / Smart Contract Storage
Status: Main Narrative (Walrus-specific differentiation)
Evidence: Native Move VM integration, Seal encryption, Walrus Sites, on-chain blob metadata — unique vs pure storage protocols
Sources: https://walrus.xyz/docs/, https://github.com/MystenLabs/walrus/blob/main/docs/whitepaper.md, https://github.com/MystenLabs/seal
Evidence Level: HIGH

Narrative: Sui Ecosystem / Move Ecosystem
Status: Main Narrative
Evidence: Native to Sui, built by Mysten Labs, core infrastructure for Sui apps
Sources: https://walrus.xyz/, https://sui.io/, https://www.mystenlabs.com/
Evidence Level: HIGH

Narrative: Cross-chain Interoperability (via Wormhole)
Status: Secondary Narrative (Planned)
Evidence: Announced Wormhole integration for cross-chain blob access
Sources: https://walrus.xyz/blog/, https://wormhole.com/
Evidence Level: MEDIUM

Narrative: AI / Machine Learning Data Storage
Status: Not Currently Positioned
Evidence: No specific AI-focused marketing; 0G targets this narrative
Sources: https://walrus.xyz/, https://0g.ai/
Evidence Level: HIGH (by absence)

Narrative: RWA (Real World Assets)
Status: Not Currently Positioned
Evidence: No RWA-specific positioning
Sources: https://walrus.xyz/
Evidence Level: HIGH (by absence)

Narrative: Gaming / Metaverse Asset Storage
Status: Secondary Narrative (Planned via SuiPlay0x1)
Evidence: Announced integration with SuiPlay0x1 gaming handheld for game asset storage
Sources: https://walrus.xyz/blog/, https://www.mystenlabs.com/blog/
Evidence Level: LOW

Sources: https://walrus.xyz/, https://messari.io/project/sui, https://github.com/MystenLabs/walrus, https://walrus.xyz/docs/, https://github.com/MystenLabs/walrus/blob/main/docs/whitepaper.md, https://github.com/MystenLabs/seal, https://sui.io/, https://www.mystenlabs.com/, https://wormhole.com/, https://walrus.xyz/blog/, https://0g.ai/

## Market Timeline

Date: 2021-12
Milestone: Mysten Labs Series A Funding ($92M led by a16z crypto)
Description: Capitalized core team building Sui and Walrus
Related Historical Event ID: Mysten Labs Series A
Sources: https://www.mystenlabs.com/blog/mysten-labs-raises-92m-series-a

Date: 2022-09
Milestone: Mysten Labs Series B Funding ($300M led by FTX Ventures)
Description: Major capital infusion; FTX Ventures equity later complicated by bankruptcy
Related Historical Event ID: Mysten Labs Series B
Sources: https://www.mystenlabs.com/blog/mysten-labs-raises-300m-series-b, https://www.coindesk.com/business/2022/11/11/mysten-labs-ftx-venture-investment/

Date: 2023-05
Milestone: Sui Mainnet Launch
Description: Sui L1 launches; Walrus development continues as storage layer
Related Historical Event ID: Sui Mainnet Launch
Sources: https://sui.io/blog/sui-mainnet-launches

Date: 2024 (Q2-Q3)
Milestone: Walrus Testnet Launch
Description: Permissioned testnet with ~50-100 storage nodes, Walrus Sites, Seal encryption, TypeScript SDK
Related Historical Event ID: Walrus Testnet Launch
Sources: https://walrus.xyz/docs/, https://github.com/MystenLabs/walrus/blob/main/docs/testnet.md, https://github.com/MystenLabs/walrus

Date: 2024
Milestone: Wormhole Integration Announced
Description: Partnership announced for cross-chain blob storage access
Related Historical Event ID: Wormhole Partnership Announcement
Sources: https://walrus.xyz/blog/, https://wormhole.com/blog/

Date: 2024
Milestone: Akord Integration Live on Testnet
Description: Akord vault app uses Walrus as storage backend
Related Historical Event ID: Akord Integration
Sources: https://akord.com/, https://walrus.xyz/blog/

Date: 2024
Milestone: Decrypt Media Pilot
Description: Decrypt Media archives content on Walrus Sites testnet
Related Historical Event ID: Decrypt Media Pilot
Sources: https://walrus.xyz/blog/, https://decrypt.co/

Date: 2024-2025 (Projected)
Milestone: Walrus Mainnet Launch / WAL TGE
Description: Not yet occurred; no official date announced
Related Historical Event ID: N/A (Future)
Sources: https://walrus.xyz/, https://github.com/MystenLabs/walrus

Sources: https://www.mystenlabs.com/blog/mysten-labs-raises-92m-series-a, https://www.mystenlabs.com/blog/mysten-labs-raises-300m-series-b, https://www.coindesk.com/business/2022/11/11/mysten-labs-ftx-venture-investment/, https://sui.io/blog/sui-mainnet-launches, https://walrus.xyz/docs/, https://github.com/MystenLabs/walrus/blob/main/docs/testnet.md, https://github.com/MystenLabs/walrus, https://walrus.xyz/blog/, https://wormhole.com/blog/, https://akord.com/, https://decrypt.co/, https://walrus.xyz/

## Official Market Resources

Official Dashboard: https://walrus.xyz/ (No live metrics dashboard)
DefiLlama: https://defillama.com/chain/Sui (Sui ecosystem page, no Walrus-specific)
CoinGecko: https://www.coingecko.com/ (No WAL token page)
CoinMarketCap: https://coinmarketcap.com/ (No WAL token page)
Token Terminal: https://tokenterminal.com/terminal/projects/sui (Sui only)
Messari: https://messari.io/project/sui (Sui report covers Walrus as ecosystem project)
Explorer: https://suivision.xyz/ (Sui explorer, includes Walrus testnet activity), https://walruscan.com/ (Planned, not live)

## BUAT RINGKASAN

Market Stage: Pre-TGE / Testnet
Primary Category: Decentralized Storage / Data Availability Layer
Competitor Count: 7 major direct competitors identified (Filecoin, Arweave, Storj, Sia, 0G, Celestia, EigenDA)
Major Narrative: DePIN, Programmable Storage, Sui Ecosystem, Modular DA
Trading Availability: None (Token not launched)
Adoption Metrics Available: Minimal (GitHub stars ~500+, testnet node count estimated 50-100, no public user/volume dashboards)

## Behavioral Intelligence
_ref: `docs/Ontology/Hidden.md` — enriches DecisionEvent Alternatives/Reason/Reactions_

PROJECT: Walrus

Strategic Objectives

1. Menjadi lapisan penyimpanan terprogram native untuk ekosistem Sui
· Evidence: Walrus dirancang sebagai "programmable storage layer" yang terintegrasi native dengan Move VM di Sui, memungkinkan smart contract berinteraksi langsung dengan blob storage on-chain (Walrus Sites, Seal encryption, on-chain metadata)
· Supporting Dataset: Phase 1 Foundation, Phase 4 Technology (Move VM integration, Seal, Walrus Sites), Phase 7 Ecosystem (Sui Native Integration live testnet)

2. Mendiferensiasi dari penyimpanan terdesentralisasi lain melalui programmability dan integrasi Move
· Evidence: Whitepaper dan dokumentasi menonjokkan "programmable storage" sebagai diferensiasi utama vs Filecoin/Arweave/Storj yang lebih generic; fitur Seal (threshold encryption), Walrus Sites, dan direct Move VM calls tidak ada di kompetitor
· Supporting Dataset: Phase 4 Technology (whitepaper, Seal integration), Phase 8 Market (Competitor Landscape, Narrative Position)

3. Ekspansi cross-chain melalui Wormhole untuk menjangkau developer non-Sui
· Evidence: Partnership Wormhole diumumkan 2024 untuk cross-chain blob access; Walrus tidak terbatas pada Sui saja tapi menargetkan multi-chain DA/storage market
· Supporting Dataset: Phase 2 Entity (Wormhole dependency), Phase 3 History (Wormhole announcement 2024), Phase 7 Ecosystem (Wormhole integration planned), Phase 8 Market (Cross-chain narrative secondary)

4. Desentralisasi progresif dari testnet permissioned ke mainnet permissionless dengan governance DAO
· Evidence: Testnet saat ini permissioned (~50-100 nodes oleh Mysten Labs + komunitas); roadmap menyebutkan Walrus Foundation/DAO untuk governance, parameter upgrades, treasury management; validator set mainnet direncanakan permissionless
· Supporting Dataset: Phase 2 Entity (Walrus Foundation planned, DAO planned), Phase 3 History (Testnet launch 2024 permissioned), Phase 7 Ecosystem (Validator group testnet permissioned, mainnet planned permissionless, Governance ecosystem)

5. Monetisasi melalui fee-based model (storage + retrieval) dengan token WAL untuk staking/governance
· Evidence: Revenue model planned: blob storage fees, retrieval fees, validator rewards; WAL token untuk governance, staking, fee payment; tokenomics doc referenced tapi belum final/public
· Supporting Dataset: Phase 5 Financial (Revenue Model planned), Phase 6 Token (WAL utility planned), Phase 8 Market (Market Timeline projected mainnet/TGE)

Decision Timeline

Keputusan: Mysten Labs mendirikan Walrus sebagai protocol storage terpisah dari Sui core (2021-2022)
· Trigger: Kebutuhan lapisan storage terprogram untuk aplikasi Sui yang tidak terpenuhi oleh existing solutions (Filecoin/Arweave tidak native ke Move/Sui)
· Evidence: Mysten Labs Series A (Dec 2021) dan Series B (Sep 2022) funding untuk membangun Sui + ecosystem infrastructure termasuk Walrus
· Decision: Membangun Walrus sebagai protocol terpisah di atas Sui consensus, bukan sebagai fitur built-in Sui
· Immediate Result: Tim terdedikasi Walrus, whitepaper, arsitektur erasure coding + proof-of-availability
· Long-term Impact: Walrus menjadi core infrastructure Sui ecosystem; memungkinkan Walrus Sites, Seal, programmable storage
· Supporting Dataset: Phase 3 History (Mysten Labs Series A 2021-12, Series B 2022-09), Phase 4 Technology (Architecture), Phase 1 Foundation

Keputusan: Memilih arsitektur erasure coding + proof-of-availability di atas Sui consensus (bukan Proof-of-Replication seperti Filecoin atau endowment seperti Arweave)
· Trigger: Kebutuhan throughput tinggi, deletable storage, dan integrasi native Move VM
· Evidence: Whitepaper Walrus menjelaskan desain erasure coding (Red Stuff) + proof-of-availability (Blue Stuff) yang berbeda dari Filecoin/Arweave
· Decision: Arsitektur 2-layer: Red Stuff (encoding/distribution) + Blue Stuff (availability proofs via Sui consensus)
· Immediate Result: Testnet live 2024 dengan ~50-100 storage nodes, Walrus Sites, Seal encryption
· Long-term Impact: Diferensiasi teknis vs kompetitor; trade-off: dependency pada Sui validator set untuk consensus
· Supporting Dataset: Phase 4 Technology (Architecture, Consensus, Whitepaper), Phase 8 Market (Competitor Landscape)

Keputusan: Launch testnet permissioned terlebih dahulu sebelum mainnet permissionless (2024 Q2-Q3)
· Trigger: Kebutuhan hardening protocol, testing economics, validator operations sebelum permissionless
· Evidence: Testnet docs menunjukkan permissioned validator set, test SUI tokens, no real fees; Mysten Labs mengoperasikan mayoritas infrastructure
· Decision: Testnet permissioned ~6-12 bulan sebelum mainnet; community validators diundang tapi curated
· Immediate Result: Akord, Decrypt Media, Seal integration live di testnet; developer feedback loop
· Long-term Impact: Mengurangi risiko mainnet launch; tapi menunda desentralisasi nyata dan token launch
· Supporting Dataset: Phase 3 History (Walrus Testnet Launch 2024), Phase 7 Ecosystem (Infrastructure Providers, Validator Group), Phase 5 Financial (No live revenue)

Keputusan: Partnership Wormhole untuk cross-chain bukan bridge custom atau IBC (2024)
· Trigger: Kebutuhan akses cross-chain cepat tanpa membangun bridge infrastructure sendiri
· Evidence: Wormhole announcement blog 2024; Wormhole NTT/Gateway digunakan; bukan IBC (Sui tidak native IBC) atau LayerZero
· Decision: Integrasi Wormhole untuk cross-chain blob access dan messaging
· Immediate Result: Announcement saja, belum live; technical specs tidak dipublikasikan
· Long-term Impact: Dependency pada Wormhole security; memperluas TAM ke non-Sui chains; risiko bridge exploit
· Supporting Dataset: Phase 2 Entity (Wormhole dependency), Phase 3 History (Wormhole announcement 2024), Phase 7 Ecosystem (Wormhole integration planned), Phase 8 Market (Cross-chain narrative)

Keputusan: Tidak meluncurkan token WAL bersamaan dengan testnet; menunggu mainnet readiness (2024-sekarang)
· Trigger: Hindari token launch prematur tanpa utility nyata, regulatory clarity, dan mainnet economics teruji
· Evidence: Tidak ada WAL token di testnet (menggunakan test SUI); tokenomics doc referenced tapi tidak public; tidak ada TGE date announcement
· Decision: Delay token launch hingga mainnet; testnet menggunakan test tokens
· Immediate Result: Tidak ada speculative trading, fokus pada product-market fit; tapi tidak ada incentive mechanism untuk storage nodes nyata
· Long-term Impact: Tokenomics design space lebih luas; risiko community impatience; competitor (0G, Celestia) sudah launch token
· Supporting Dataset: Phase 5 Financial (Token Sale: not announced), Phase 6 Token (WAL not launched), Phase 8 Market (Trading Markets: N/A)

Keputusan: Bergantung sepenuhnya pada treasury Mysten Labs tanpa treasury Walrus terpisah/transparan (2021-sekarang)
· Trigger: Walrus adalah produk internal Mysten Labs, bukan entity legal terpisah awalnya
· Evidence: Tidak ada transparency report Walrus; semua funding via Mysten Labs rounds; FTX Ventures equity di Mysten Labs bukan Walrus langsung
· Decision: Operasional Walrus difunding dari treasury Mysten Labs ($428M total raised)
· Immediate Result: Capital cukup untuk development panjang; tidak perlu token sale awal
· Long-term Impact: Ketidaktransparan allocation Walrus-specific; FTX exposure risk; DAO formation kompleks (harus carve-out dari Mysten Labs)
· Supporting Dataset: Phase 5 Financial (Funding History, Treasury, Financial Dependencies, Financial Risk), Phase 2 Entity (Mysten Labs, FTX Ventures)

Evolution Pattern

Perubahan Strategi: Dari "Sui storage layer" → "Cross-chain programmable storage platform"
· Evidence: Awalnya positioning fokus Sui ecosystem (Phase 1, 3 Sui mainnet 2023 → Walrus testnet 2024); kemudian announcement Wormhole 2024 untuk cross-chain; narrative "Modular DA" ditambahkan (Phase 8 Market Narrative Position)
· Supporting Dataset: Phase 1 Foundation, Phase 3 History (Sui Mainnet 2023-05, Walrus Testnet 2024, Wormhole 2024), Phase 8 Market (Narrative Position: DePIN primary, Modular DA secondary)

Perubahan Teknologi: Dari core protocol → ecosystem integrations (Seal, SNS, Walrus Sites, Akord)
· Evidence: Phase 4 Technology menunjukkan core protocol (erasure coding, PoA); Phase 7 Ecosystem menunjukkan integrations berlipat: Seal (encryption), SNS (naming), Walrus Sites (hosting), Akord (vault app), Decrypt (media) — semuanya dibangun di atas core protocol
· Supporting Dataset: Phase 4 Technology (Seal integration, Walrus Sites), Phase 7 Ecosystem (Major Integrations, Applications)

Perubahan Tokenomics: Dari tidak ada token → planned WAL token dengan governance + staking + fee utility
· Evidence: Phase 6 Token menunjukkan WAL belum launched, tidak ada detail supply/vesting; Phase 5 Financial Revenue Model planned fee-based; Phase 2 Entity Walrus Foundation planned untuk governance
· Supporting Dataset: Phase 5 Financial (Revenue Model, Fundraising Mechanism), Phase 6 Token (all sections), Phase 2 Entity (Walrus Foundation planned)

Perubahan Governance: Dari centralized (Mysten Labs) → planned DAO/Foundation
· Evidence: Phase 2 Entity: Mysten Labs current steward, Walrus Foundation planned, DAO planned; Phase 7 Governance Ecosystem: Sui validators indirectly govern via Sui governance; Testnet committee Mysten Labs + selected validators
· Supporting Dataset: Phase 2 Entity (Foundation, DAO), Phase 3 History (Testnet launch permissioned), Phase 7 Ecosystem (Governance Ecosystem)

Perubahan Funding: Dari VC-funded (Mysten Labs) → protocol revenue + future token treasury
· Evidence: Phase 5 Financial: $428M via Mysten Labs VC rounds; Revenue Model planned tapi $0 actual; Fundraising Mechanism: VC via parent, grants via Sui Foundation, future DAO treasury
· Supporting Dataset: Phase 5 Financial (Funding History, Revenue Model, Fundraising Mechanism, Financial Dependencies)

Technical Decision Pattern

Pola 1: Native Sui/Move Integration First
· Decision Pattern: Semua fitur core (Walrus Sites, Seal encryption, blob metadata, programmable access) dibangun native pada Move VM dan Sui consensus, bukan sebagai layer terpisah dengan bridge
· Evidence: Walrus Sites menggunakan Sui objects untuk metadata; Seal menggunakan Sui threshold encryption; blob references on-chain; TypeScript SDK wraps Sui transactions
· Supporting Dataset: Phase 4 Technology (Architecture, Move VM, Seal), Phase 7 Ecosystem (Sui Native Integration live, Seal integration live, Walrus Sites core app)

Pola 2: Erasure Coding + Proof-of-Availability sebagai Konsensus Storage (bukan PoRep/PoSt)
· Decision Pattern: Memilih Red Stuff (erasure coding distribution) + Blue Stuff (availability proofs via Sui consensus) alih-alih Filecoin PoRep/PoSt atau Arweave endowment
· Evidence: Whitepaper Walrus menjelaskan 2-layer design; proof-of-availability leverages Sui validator set yang sudah ada; erasure coding untuk durability + deletability
· Supporting Dataset: Phase 4 Technology (Architecture, Consensus, Whitepaper), Phase 8 Market (Competitor Landscape: Filecoin PoRep, Arweave endowment)

Pola 3: Testnet Permissioned untuk Hardening Sebelum Permissionless
· Decision Pattern: Mengoperasikan testnet dengan validator set curated (~50-100 nodes, Mysten Labs + invited community) selama 6-12+ bulan sebelum mainnet permissionless
· Evidence: Testnet docs menunjukkan permissioned; Mysten Labs operate majority infrastructure; community validators need approval; no public permissionless registration yet
· Supporting Dataset: Phase 3 History (Testnet Launch 2024), Phase 7 Ecosystem (Validator Group testnet permissioned, Infrastructure Providers Mysten Labs critical)

Pola 4: Modular Architecture dengan Integrasi Eksternal untuk Fitur Non-Core
· Decision Pattern: Core protocol fokus pada blob storage + availability; encryption (Seal), naming (SNS), cross-chain (Wormhole), hosting (Sites) diimplementasikan sebagai integrasi/modular layer
· Evidence: Seal adalah protocol terpisah (MystenLabs/seal repo); SNS external; Wormhole external; Walrus Sites built on top of blob primitives
· Supporting Dataset: Phase 4 Technology (Seal integration), Phase 7 Ecosystem (Major Integrations: Seal, SNS, Wormhole, Walrus Sites), Phase 2 Entity (Seal, SNS, Wormhole as dependencies)

Pola 5: TypeScript/Rust SDK + HTTP API untuk Developer Experience
· Decision Pattern: Menyediakan SDK tingkat tinggi (TS/Rust) dan HTTP API sederhana (blob store/read/delete/sites) alih-alih hanya low-level Move calls
· Evidence: GitHub repo memiliki walrus-sdk (TS), walrus CLI, HTTP API docs; Walrus Sites CLI terpisah; Akord menggunakan SDK
· Supporting Dataset: Phase 4 Technology (Programming Languages Rust/TypeScript), Phase 7 Ecosystem (Developer Ecosystem: TS SDK, HTTP API, CLI, Sites CLI)

Financial Decision Pattern

Pola 1: Pendanaan Via Parent Company (Mysten Labs) Tanpa Ronde Terpisah
· Decision Pattern: Seluruh capital ($428M: $36M Seed + $92M Series A + $300M Series B) di-raise di level Mysten Labs; tidak ada funding round khusus Walrus
· Evidence: Phase 5 Funding History menunjukkan 3 rounds semua Mysten Labs; a16z lead Seed+Series A; FTX Ventures lead Series B; Walrus-specific funding "tidak diungkap"
· Supporting Dataset: Phase 5 Financial (Funding History, Fundraising Mechanism), Phase 2 Entity (Mysten Labs, a16z crypto, FTX Ventures), Phase 3 History (Series A 2021-12, Series B 2022-09)

Pola 2: Tidak Ada Treasury Transparan Terpisah untuk Walrus
· Decision Pattern: Tidak mempublikasikan treasury dashboard, transparency report, atau allocation breakdown khusus Walrus; semua financial reporting di level Mysten Labs/Sui Foundation
· Evidence: Phase 5 Treasury: "Tidak diungkap" untuk semua field; Transparency Report: "Tidak tersedia"; Treasury Dashboard: "Tidak tersedia"
· Supporting Dataset: Phase 5 Financial (Treasury, Official Financial Resources), Phase 2 Entity (Mysten Labs, Sui Foundation)

Pola 3: Revenue Model Fee-Based (Storage + Retrieval) + Validator Rewards, Belum Live
· Decision Pattern: Merancang economics berbasis fee (blob write, read, validator rewards) mirip cloud storage tapi decentralized; token WAL untuk fee payment dan staking; semua masih planned
· Evidence: Phase 5 Revenue Model: Blob Storage Fees, Retrieval Fees, Validator Rewards — semua "Planned"; Phase 6 Token: WAL utility planned untuk fee/governance/staking
· Supporting Dataset: Phase 5 Financial (Revenue Model), Phase 6 Token (Utility, Governance), Phase 8 Market (Adoption Metrics: Volume $0 testnet)

Pola 4: Dependency Finansial pada VC Backers dengan Risiko FTX
· Decision Pattern: Financial dependency tertuju pada a16z (lead Seed+A) dan FTX Ventures (lead B $300M); status FTX equity uncertain pasca-bankruptcy; tidak ada diversifikasi funding source lain
· Evidence: Phase 5 Financial Dependencies: a16z crypto (Medium, Live), FTX Ventures (Medium, Uncertain); Financial Risk: FTX Ventures Exposure HIGH; Fundraising Mechanism: VC only, no public sale, no grants direct to Walrus
· Supporting Dataset: Phase 5 Financial (Financial Dependencies, Financial Risk, Fundraising Mechanism), Phase 2 Entity (a16z crypto, FTX Ventures), Phase 3 History (Series B 2022-09 FTX lead)

Pola 5: Grant Ecosystem Via Sui Foundation, Bukan Direct Walrus Grants
· Decision Pattern: Menggunakan Sui Foundation grants untuk ecosystem builders di atas Walrus; tidak ada grant program Walrus-specific; Mysten Labs Builder Grants umum
· Evidence: Phase 5 Fundraising Mechanism: Grant "Ya (Sui Foundation ecosystem grants untuk builders di atas Walrus/Sui)"; Phase 7 Developer Ecosystem: Grant Program Sui Foundation Grants + Mysten Labs Builder Grants
· Supporting Dataset: Phase 5 Financial (Fundraising Mechanism), Phase 7 Ecosystem (Developer Ecosystem), Phase 2 Entity (Sui Foundation)

Ecosystem Decision Pattern

Pola 1: Deep Integration dengan Sui Ecosystem Sebagai Primary Moat
· Decision Pattern: Semua core features (Walrus Sites, Seal, blob metadata, programmable access) memerlukan Sui; tidak ada standalone version; Sui validator set menjalankan storage nodes
· Evidence: Phase 7 Primary Chain: Sui (Critical); External Dependencies: Sui Blockchain (Critical); Major Integrations: Sui Native Integration (Live Testnet); Infrastructure: Mysten Labs operators; Wallets: semua Sui wallets
· Supporting Dataset: Phase 7 Ecosystem (Primary Chain, External Dependencies, Major Integrations, Infrastructure Providers, Wallet Ecosystem), Phase 4 Technology (Move VM, Sui Consensus)

Pola 2: Cross-Chain Expansion Via Wormhole (Single Bridge Partner)
· Decision Pattern: Memilih satu bridge partner (Wormhole) untuk cross-chain alih-alih multi-bridge atau custom; announcement 2024 tapi technical specs belum public
· Evidence: Phase 7 External Dependencies: Wormhole (High, Planned); Major Integrations: Wormhole Cross-Chain (Planned); Phase 8 Narrative: Cross-chain secondary; Supported Chains: Sui native, others via Wormhole planned
· Supporting Dataset: Phase 7 Ecosystem (External Dependencies, Major Integrations, Supported Chains), Phase 2 Entity (Wormhole), Phase 3 History (Wormhole announcement 2024), Phase 8 Market (Narrative Position)

Pola 3: Early Ecosystem Partnerships dengan Application Builders (Akord, Decrypt)
· Decision Pattern: Mengintegrasikan aplikasi real (Akord vault, Decrypt media archive) di testnet untuk validasi product-market fit sebelum mainnet
· Evidence: Phase 7 Major Integrations: Akord (Live Testnet), Decrypt Media (Beta); Applications: Akord (Built on Walrus), Decrypt Media Archive (Pilot)
· Supporting Dataset: Phase 7 Ecosystem (Major Integrations, Applications), Phase 3 History (Akord integration 2024, Decrypt pilot 2024)

Pola 4: Infrastructure Dependency pada Cloud Providers + Mysten Labs Ops
· Decision Pattern: Testnet infrastructure berjalan pada GCP/AWS/Azure via Mysten Labs; community validators belum dominant; Shinami/Ankr untuk RPC/indexer
· Evidence: Phase 7 Infrastructure Providers: Mysten Labs (Critical), Community Validators (High), Shinami (Medium), Ankr (Medium), GCP (Medium); External Dependencies: Cloud Providers (Medium)
· Supporting Dataset: Phase 7 Ecosystem (Infrastructure Providers, External Dependencies), Phase 4 Technology (Tech Stack Docker/Kubernetes implied)

Pola 5: Developer-First dengan SDK/CLI/HTTP API Lengkap
· Decision Pattern: Menginvestasi heavy pada developer tooling (TS SDK, Rust SDK, CLI, Sites CLI, HTTP API) sebelum mainnet; hackathons (Sui Overflow) dan grants untuk adoption
· Evidence: Phase 7 Developer Ecosystem: Walrus TS SDK, HTTP API, CLI, Sites CLI, Sui Foundation Grants, Mysten Labs Builder Grants, Sui Overflow Hackathons; GitHub stars ~500+
· Supporting Dataset: Phase 7 Ecosystem (Developer Ecosystem), Phase 4 Technology (Programming Languages), Phase 8 Market (Adoption Metrics: GitHub stars)

Governance Decision Pattern

Pola 1: Centralized Stewardship oleh Mysten Labs Selama Testnet
· Decision Pattern: Semua keputusan protocol (upgrades, parameters, validator set, roadmap) dikendalikan Mysten Labs; testnet committee = Mysten Labs + selected validators
· Evidence: Phase 7 Governance Ecosystem: Foundation Mysten Labs (Role: Core developer, testnet operator, initial governance steward); Committee: Walrus Testnet Committee (Mysten Labs + selected community validators); DAO: Walrus Foundation (Planned, Not Yet Formed)
· Supporting Dataset: Phase 7 Ecosystem (Governance Ecosystem), Phase 3 History (Testnet Launch 2024 permissioned), Phase 2 Entity (Mysten Labs, Walrus Foundation planned)

Pola 2: Indirect Governance Via Sui Validators dan Sui Foundation
· Decision Pattern: Sui governance (validator voting) mempengaruhi Walrus karena consensus dependency; Sui Foundation grants mempengaruhi ecosystem direction
· Evidence: Phase 7 Governance: Council: Sui Validators (indirectly govern Walrus via Sui governance); Foundation: Sui Foundation (ecosystem grants, validator delegation); External Dependencies: Sui Foundation (High)
· Supporting Dataset: Phase 7 Ecosystem (Governance Ecosystem, External Dependencies), Phase 2 Entity (Sui Foundation), Phase 4 Technology (Sui Consensus dependency)

Pola 3: Planned DAO/Foundation Transition Tanpa Timeline Konkrit
· Decision Pattern: Roadmap menyebutkan Walrus Foundation dan DAO untuk governance, treasury, parameter control; tapi tidak ada legal formation announcement, jurisdiction, atau timeline
· Evidence: Phase 2 Entity: Walrus Foundation (Planned), DAO (Planned); Phase 5 Financial Dependencies: Future Walrus DAO/Foundation (Planned); Phase 7 Governance: DAO Walrus Foundation (Planned, Not Yet Formed); Phase 8 Open Threads: "Walrus Foundation legal formation status... announced as planned, no public filing"
· Supporting Dataset: Phase 2 Entity (Foundation, DAO), Phase 5 Financial (Financial Dependencies), Phase 7 Ecosystem (Governance Ecosystem), Phase 8 Market (Open Threads)

Pola 4: Token-Gated Governance Direncanakan (WAL) Tapi Token Belum Ada
· Decision Pattern: Governance design mengasumsikan WAL token untuk voting, staking, parameter control; tapi token launch delayed hingga mainnet; governance vacuum saat ini
· Evidence: Phase 6 Token: Governance planned, WAL not launched; Phase 5 Fundraising Mechanism: DAO Treasury "Belum terbentuk"; Phase 8 Trading Markets: N/A token not launched
· Supporting Dataset: Phase 6 Token (all sections), Phase 5 Financial (Fundraising Mechanism, Revenue Model), Phase 8 Market (Trading Markets)

Risk Response Pattern

Pola 1: Technical Risk Mitigation Via Extended Permissioned Testnet
· Trigger: Kompleksitas protocol baru (erasure coding + PoA + Move integration) memerlukan hardening sebelum permissionless
· Response: Menjalankan testnet permissioned 6-12+ bulan dengan curated validator set; Mysten Labs operate infrastructure; iterasi cepat berdasarkan feedback
· Evidence: Testnet permissioned design; Mysten Labs critical infrastructure provider; Akord/Decrypt/Seal integrations sebagai validation; no mainnet date announced
· Result: Protocol teruji dengan real applications (Akord, Decrypt, Seal) sebelum mainnet; bug/performance issues ditemukan di testnet
· Supporting Dataset: Phase 3 History (Testnet Launch 2024), Phase 7 Ecosystem (Validator Group testnet permissioned, Infrastructure Providers, Major Integrations), Phase 4 Technology (Technical Limitations: centralized testnet)

Pola 2: Financial Risk (FTX Exposure) — Tidak Ada Respons Publik Transparan
· Trigger: FTX Ventures lead Series B $300M (Sep 2022); FTX bankruptcy Nov 2022; potential clawback/equity uncertainty
· Response: Tidak ada official statement tentang status equity FTX di Mysten Labs post-bankruptcy; operasi lanjut normal dengan treasury Series B
· Evidence: Phase 5 Financial Risk: FTX Ventures Exposure HIGH; Financial Dependencies: FTX Ventures status Uncertain; Phase 3 History: Series B 2022-09, Coindesk article Nov 2022; Phase 8 Open Threads: "Status of FTX Ventures equity... conflicting reports, no official settlement disclosure"
· Result: Ketidakpastian tetap; investor/community tidak memiliki clarity; Mysten Labs terus operate dengan capital existing
· Supporting Dataset: Phase 5 Financial (Financial Risk, Financial Dependencies), Phase 3 History (Series B, Coindesk article), Phase 8 Market (Open Threads)

Pola 3: Single-Chain Dependency Risk — Mitigasi Via Wormhole Cross-Chain (Planned)
· Trigger: Walrus fully dependent pada Sui consensus/validator set; Sui failure = Walrus failure
· Response: Announcement partnership Wormhole untuk cross-chain access; memungkinkan non-Sui chains menggunakan Walrus storage
· Evidence: Phase 7 External Dependencies: Sui Blockchain (Critical), Wormhole (High, Planned); Phase 8 Market: Narrative Cross-chain secondary, Risk: Single Chain Dependency HIGH; Phase 3 History: Wormhole announcement 2024
· Result: Mitigasi masih planned, belum live; technical specs tidak public; Wormhole sendiri punya bridge risk
· Supporting Dataset: Phase 7 Ecosystem (External Dependencies, Major Integrations), Phase 8 Market (Narrative Position, Competitor Landscape, Open Threads)

Pola 4: Centralization Risk (Testnet) — Mitigasi Via Community Validator Onboarding (Gradual)
· Trigger: Testnet validators permissioned, Mysten Labs dominant; tidak representative of mainnet decentralization
· Response: Membuka aplikasi community validators (curated); dokumentasi running-a-node public; target mainnet permissionless
· Evidence: Phase 7 Validator Group: Testnet permissioned, Mainnet planned permissionless; Infrastructure Providers: Community Validators High; External Dependencies: Cloud Providers Medium; Phase 4 Technical Limitations: Centralized testnet operation HIGH
· Result: Beberapa community validators join testnet; tapi Mysten Labs masih majority operator; mainnet decentralization unproven
· Supporting Dataset: Phase 7 Ecosystem (Validator Group, Infrastructure Providers, External Dependencies), Phase 4 Technology (Technical Limitations)

Pola 5: Token Launch Regulatory/Market Risk — Delay Token Launch Hingga Mainnet Ready
· Trigger: Regulatory uncertainty (US SEC actions pada crypto tokens); competitor token launches (0G, Celestia, EigenDA); need real utility untuk WAL
· Response: Tidak launch token di testnet; menggunakan test SUI; menunggu mainnet readiness, regulatory clarity, product-market fit terbukti
· Evidence: Phase 6 Token: WAL not launched; Phase 5 Token Sale: all not announced; Phase 8 Trading Markets: N/A; Phase 3 History: Testnet 2024 no token, Mainnet/TGE projected 2024-2025 not announced
· Result: Avoid regulatory exposure early; tapi kehilangan momentum vs competitor yang sudah launch token; community incentive mechanism absent
· Supporting Dataset: Phase 6 Token (all), Phase 5 Financial (Token Sale), Phase 8 Market (Trading Markets, Market Timeline), Phase 8 Competitor Landscape (0G, Celestia, EigenDA have tokens)

Recurring Behavioral Pattern

Pola 1: Build Core Protocol First, Ecosystem Integrations Second
· Evidence: Phase 3-4: Core protocol (erasure coding, PoA, Move integration) developed 2022-2024; Phase 7: Integrations (Seal, SNS, Wormhole, Akord, Decrypt) announced/built 2024 setelah testnet live; Phase 8: Narrative "Programmable Storage" primary setelah core ready
· Supporting Dataset: Phase 3 History (Timeline), Phase 4 Technology (Architecture), Phase 7 Ecosystem (Major Integrations timeline), Phase 8 Market (Narrative Position)

Pola 2: Leverage Parent Company (Mysten Labs) Resources untuk Semua Hal Operasional
· Evidence: Funding via Mysten Labs rounds (Phase 5); Infrastructure operated by Mysten Labs (Phase 7); Testnet committee led by Mysten Labs (Phase 7); Legal/entity via Mysten Labs (Phase 2); Grants via Mysten Labs Builder Grants (Phase 7); No independent ops
· Supporting Dataset: Phase 2 Entity (Mysten Labs), Phase 3 History (Funding rounds), Phase 5 Financial (Funding, Dependencies), Phase 7 Ecosystem (Infrastructure, Governance, Developer Ecosystem)

Pola 3: Announce Partnerships Early, Technical Details Later
· Evidence: Wormhole announced 2024 tapi technical specs belum public (Phase 3, 7); SNS integration beta tapi custom domain support "planned no timeline" (Phase 8 Open Threads); Akord/Decrypt announced sebagai integrations tapi volume metrics tidak public (Phase 8 Adoption Metrics)
· Supporting Dataset: Phase 3 History (Wormhole announcement), Phase 7 Ecosystem (Major Integrations), Phase 8 Market (Open Threads, Adoption Metrics)

Pola 4: Delay Decentralization/Governance/Token Milestones Tanpa Hard Deadline
· Evidence: Walrus Foundation/DAO "planned" sejak awal tapi no formation (Phase 2, 5, 7); Mainnet/TGE "projected 2024-2025" tapi tidak announced (Phase 3, 8); Permissionless validator set "planned" tapi testnet masih permissioned (Phase 7); Tokenomics doc referenced tapi tidak public (Phase 5, 6)
· Supporting Dataset: Phase 2 Entity (Foundation, DAO), Phase 3 History (Market Timeline), Phase 5 Financial (Dependencies), Phase 6 Token (all), Phase 7 Ecosystem (Governance, Validator Group), Phase 8 Market (Market Timeline, Open Threads)

Pola 5: Transparansi Minimal pada Metriks Adopsi dan Financials
· Evidence: Tidak ada public dashboard untuk testnet blobs, users, volume (Phase 8 Adoption Metrics: mostly "Tidak diketahui"); Treasury tidak transparan (Phase 5); Tokenomics tidak public (Phase 6); FTX equity status tidak diklarifikasi (Phase 5, 8); Validator set tidak enumerated public (Phase 7, 8)
· Supporting Dataset: Phase 5 Financial (Treasury, Revenue History), Phase 6 Token (all), Phase 7 Ecosystem (Validator Group), Phase 8 Market (Adoption Metrics, Open Threads)

Strategic Trade-offs

Trade-off 1: Desentralisasi vs Kecepatan Pengembangan (Time-to-Market)
· Decision: Memilih testnet permissioned berbulan-bulan dengan Mysten Labs sebagai operator utama alih-alih launch permissionless segera
· Trade-off: Mengorbankan desentralisasi nyata dan community ownership awal demi kecepatan iterasi protocol, keamanan testing, dan developer onboarding yang controlled
· Evidence: Testnet permissioned ~50-100 nodes curated; Mysten Labs critical infrastructure; no mainnet date; validator group testnet permissioned; Phase 4 Technical Limitations: Centralized testnet operation HIGH
· Supporting Dataset: Phase 3 History (Testnet Launch 2024), Phase 4 Technology (Technical Limitations), Phase 7 Ecosystem (Validator Group, Infrastructure Providers), Phase 8 Market (Risk: Centralized Testnet Operation HIGH)

Trade-off 2: Single-Chain Native Integration vs Multi-Chain Reach
· Decision: Build native pada Sui/Move dengan deep integration (Move VM calls, Sui objects, Seal, SNS) alih-alih chain-agnostic dari awal
· Trade-off: Mendapatkan developer experience terbaik dan programmability unik di Sui; tapi menciptakan vendor lock-in ke Sui, dependency pada Sui validator set, dan perlu bridge (Wormhole) untuk cross-chain yang menambah complexity dan risk
· Evidence: Phase 4 Technology (Move VM, Seal, Walrus Sites native); Phase 7 Primary Chain Sui Critical; External Dependencies Sui Critical, Wormhole High Planned; Phase 8 Risk: Single Chain Dependency HIGH; Competitor Landscape: 0G, Celestia, EigenDA multi-chain native
· Supporting Dataset: Phase 4 Technology (Architecture, Move VM), Phase 7 Ecosystem (Primary Chain, External Dependencies, Major Integrations), Phase 8 Market (Risk Response, Competitor Landscape)

Trade-off 3: VC Funding via Parent vs Independent Protocol Treasury
· Decision: Menerima funding seluruhnya via Mysten Labs VC rounds ($428M) tanpa separate Walrus raise atau community allocation awal
· Trade-off: Capital cukup besar tanpa dilution protokol sendiri; tapi menciptakan financial opacity (tidak ada treasury transparan), FTX exposure risk, dan kompleksitas carve-out untuk DAO/Foundation nanti
· Evidence: Phase 5 Funding History: 3 rounds Mysten Labs only; Treasury: tidak diungkap; Financial Risk: FTX Exposure HIGH, Treasury Concentration MEDIUM; Financial Dependencies: Future Walrus DAO Planned; Phase 2 Entity: Mysten Labs, FTX Ventures
· Supporting Dataset: Phase 5 Financial (Funding History, Treasury, Financial Risk, Financial Dependencies), Phase 2 Entity (Mysten Labs, FTX Ventures, Walrus Foundation), Phase 3 History (Series B FTX lead)

Trade-off 4: Fee-Based Revenue Model vs Token Incentives untuk Bootstrap
· Decision: Merancang fee-based model (storage + retrieval fees) sebagai revenue utama; token WAL untuk governance/staking bukan primary incentive; tidak ada token incentives di testnet
· Trade-off: Economics lebih sustainable dan predictable (seperti cloud); tapi kehilangan bootstrap network effects dari token incentives (seperti Filecoin mining rewards, Arweave endowment); storage nodes testnet tidak mendapat real rewards
· Evidence: Phase 5 Revenue Model: Planned fees only; Token Sale: not announced; Adoption Metrics: Volume $0 testnet; Competitor: Filecoin/Arweave/0G/Celestia/EigenDA all have token incentives live
· Supporting Dataset: Phase 5 Financial (Revenue Model, Fundraising Mechanism), Phase 6 Token (Utility, Distribution), Phase 8 Market (Adoption Metrics, Competitor Landscape)

Trade-off 5: Minimal Public Transparency vs Competitive OpSec
· Decision: Tidak mempublikasikan testnet metrics dashboard, treasury breakdown, tokenomics detail, validator list, FTX settlement status
· Trade-off: Menghindari scrutiny premature, melindungi competitive positioning, flexibility pivot; tapi menciptakan trust deficit dengan community/investor, sulit benchmarks vs competitor, governance credibility gap
· Evidence: Phase 5 Treasury/Transparency Report: tidak tersedia; Phase 6 Token: all tidak diungkap; Phase 7 Validator Group: tidak enumerated; Phase 8 Adoption Metrics: mostly tidak diketahui; Open Threads: banyak "tidak diketahui"
· Supporting Dataset: Phase 5 Financial (Treasury, Official Financial Resources), Phase 6 Token (all), Phase 7 Ecosystem (Validator Group), Phase 8 Market (Adoption Metrics, Open Threads)

Behavioral Summary

Prioritas Utama Proyek:
1. Technical Excellence & Differentiation: Membangun programmable storage yang benar-benar native ke Move/Sui dengan erasure coding + PoA — bukan fork existing design
2. Sui Ecosystem Dominance: Menjadi storage layer default untuk semua Sui apps (Walrus Sites, Seal, Akord, dll) — moat via deep integration
3. Controlled Rollout: Testnet permissioned → mainnet permissionless dengan timeline internal, bukan deadline publik — prioritaskan kualitas over hype
4. Parent Company Leverage: Gunakan resources Mysten Labs (capital, talent, infra, distribution) sepenuhnya — avoid premature independence

Cara Mengambil Keputusan:
- Top-down dari Mysten Labs leadership (Evan Spiegel/co-founders, Mysten Labs execs) untuk strategic direction
- Technical decisions by core protocol team (Mysten Labs engineers) dengan community validator feedback di testnet
- Ecosystem/partnership decisions via business dev team (Wormhole, Akord, Decrypt)
- Governance/token decisions delayed hingga mainnet readiness — no community governance saat ini
- Risk decisions: conservative (delay token, permissioned testnet, no public treasury) — avoid regulatory/technical blowups

Faktor Paling Sering Mempengaruhi Keputusan:
1. Sui/Move Native Alignment: Setiap fitur dievaluasi against "apakah ini leverage Move VM/Sui objects/consensus?"
2. Mysten Labs Resource Availability: Capital, engineering talent, infra ops, legal — semua dari parent
3. Technical Risk Tolerance: Conservative pada consensus/storage layer (extended testnet), aggressive pada integrations (Wormhole, Seal, SNS)
4. Regulatory Uncertainty: Token launch delayed, no public sale, no token di testnet — wait for clarity
5. Competitive Differentiation: Programmable storage narrative vs generic storage — drive feature decisions (Seal, Sites, Move calls)

Pola Evolusi:
- Phase 1 (2021-2022): Concept & Funding via Mysten Labs Series A/B
- Phase 2 (2023): Sui Mainnet → Walrus core protocol development
- Phase 3 (2024 H1): Testnet Launch permissioned + Core Integrations (Seal, Sites)
- Phase 4 (2024 H2): Ecosystem Expansion (Akord, Decrypt, Wormhole announcement)
- Phase 5 (2025+): Mainnet + TGE + DAO Formation (projected, not committed)

Kekuatan Utama:
- Deep technical differentiation (erasure coding + PoA + Move programmability) — bukan me-too
- Strong parent backing (Mysten Labs $428M, top-tier VCs, Sui ecosystem)
- Real applications on testnet (Akord, Decrypt, Seal) — product-market fit signals
- Developer tooling maturity (SDK, CLI, HTTP API, Sites CLI) — ready for adoption
- Clear programmable storage narrative — differentiated vs Filecoin/Arweave/Storj

Kelemahan Utama:
- Zero transparency pada financials, tokenomics, adoption metrics — trust deficit
- Single-chain dependency (Sui) dengan bridge risk (Wormhole) sebagai einzige cross-chain path
- Centralized testnet operations — decentralization unproven at scale
- No token/governance mechanism live — community alignment missing, no incentive bootstrap
- FTX Ventures exposure unresolved — potential clawback/equity risk
- No hard timeline untuk mainnet/DAO/token — execution risk vs competitors executing

## Knowledge Extraction
_ref: `docs/Patterns/*`, `docs/Reasoning/*` (rule candidates)_

PROJECT: Walrus

## Core Insights

Insight 1: Programmable Storage Differentiation via Native Move VM Integration
Explanation: Walrus membedakan diri dari kompetitor (Filecoin, Arweave, Storj) dengan arsitektur yang native terintegrasi ke Move VM dan Sui consensus, memungkinkan smart contract berinteraksi langsung dengan blob storage on-chain melalui Walrus Sites, Seal encryption, dan on-chain metadata — bukan melalui bridge atau API eksternal.
Evidence: Whitepaper Walrus menjelaskan desain 2-layer (Red Stuff erasure coding + Blue Stuff proof-of-availability via Sui consensus) yang berbeda dari Filecoin PoRep/PoSt atau Arweave endowment【Phase 4 — Architecture】; Walrus Sites menggunakan Sui objects untuk metadata, Seal menggunakan Sui threshold encryption, blob references on-chain【Phase 7 — Major Integrations】; Narrative "Programmable Storage" sebagai primary differentiation【Phase 8 — Narrative Position】.
Supporting Dataset: Phase 4 Technology (Architecture, Consensus, Whitepaper), Phase 7 Ecosystem (Sui Native Integration, Seal, Walrus Sites), Phase 8 Market (Competitor Landscape, Narrative Position)
Confidence: HIGH

Insight 2: Parent Company Leverage as Primary Operational Model
Explanation: Seluruh operasional Walrus (funding, infrastructure, legal, grants, talent) dileveragikan dari Mysten Labs sebagai parent company; tidak ada entity legal terpisah, treasury transparan, atau tim operasional independen selama fase testnet.
Evidence: $428M funding seluruhnya via Mysten Labs rounds (Seed $36M, Series A $92M, Series B $300M)【Phase 5 — Funding History】; Testnet infrastructure dioperasikan Mysten Labs (critical), community validators curated【Phase 7 — Infrastructure Providers】; Governance stewardship oleh Mysten Labs, Walrus Foundation "planned" sejak awal tapi belum terbentuk【Phase 7 — Governance Ecosystem】; Grants via Sui Foundation/Mysten Labs Builder Grants, tidak ada grant program Walrus-specific【Phase 5 — Fundraising Mechanism】.
Supporting Dataset: Phase 2 Entity (Mysten Labs, Walrus Foundation), Phase 3 History (Funding rounds), Phase 5 Financial (Funding History, Treasury, Financial Dependencies), Phase 7 Ecosystem (Infrastructure Providers, Governance Ecosystem, Developer Ecosystem)
Confidence: HIGH

Insight 3: Extended Permissioned Testnet as De-risking Strategy
Explanation: Walrus memilih menjalankan testnet permissioned (~50-100 nodes curated) selama 6-12+ bulan dengan Mysten Labs sebagai operator mayoritas, mengorbankan desentralisasi nyata demi hardening protocol, developer onboarding terkontrol, dan validasi product-market fit via aplikasi real (Akord, Decrypt, Seal) sebelum mainnet permissionless.
Evidence: Testnet launch 2024 Q2-Q3 permissioned, Mysten Labs operate majority infrastructure【Phase 3 — Walrus Testnet Launch】; Validator group testnet permissioned, mainnet planned permissionless【Phase 7 — Validator Group】; Technical limitations: centralized testnet operation HIGH【Phase 4 — Technical Limitations】; Akord/Decrypt/Seal integrations live di testnet sebagai validation【Phase 7 — Major Integrations, Applications】.
Supporting Dataset: Phase 3 History (Testnet Launch), Phase 4 Technology (Technical Limitations), Phase 7 Ecosystem (Validator Group, Infrastructure Providers, Major Integrations), Phase 8 Market (Risk: Centralized Testnet Operation)
Confidence: HIGH

Insight 4: Single-Chain Native Dependency with Planned Cross-Chain Bridge
Explanation: Walrus fully dependent pada Sui consensus/validator set (critical dependency); mitigasi single-chain risk hanya melalui partnership Wormhole yang diumumkan 2024 tapi technical specs belum public, belum live, dan menambah bridge risk.
Evidence: External dependencies: Sui Blockchain (Critical), Wormhole (High, Planned)【Phase 7 — External Dependencies】; Risk: Single Chain Dependency HIGH【Phase 8 — Ecosystem Risks】; Wormhole integration announced 2024, technical specs tidak public【Phase 3 — Wormhole Announcement】; Supported chains: Sui native, others via Wormhole planned【Phase 7 — Supported Chains】.
Supporting Dataset: Phase 7 Ecosystem (External Dependencies, Supported Chains, Major Integrations), Phase 8 Market (Narrative Position, Ecosystem Risks, Open Threads)
Confidence: HIGH

Insight 5: Zero Public Transparency on Financials, Tokenomics, and Adoption Metrics
Explanation: Tidak ada public dashboard untuk testnet metrics (blobs, volume, users), treasury breakdown, tokenomics detail (supply, vesting, allocation), validator list enumerated, atau FTX equity status resolution — menciptakan trust deficit dan sulit benchmark vs kompetitor.
Evidence: Treasury: "Tidak diungkap" semua field, Transparency Report "Tidak tersedia"【Phase 5 — Treasury】; Token: semua field "Tidak diungkap / Belum diumumkan"【Phase 6 — all sections】; Adoption metrics: mostly "Tidak diketahui"【Phase 8 — Adoption Metrics】; Validator group: tidak enumerated public【Phase 7 — Validator Group】; FTX status: conflicting reports, no official disclosure【Phase 5 — Financial Risk, Phase 8 — Open Threads】.
Supporting Dataset: Phase 5 Financial (Treasury, Official Financial Resources, Financial Risk), Phase 6 Token (all), Phase 7 Ecosystem (Validator Group), Phase 8 Market (Adoption Metrics, Open Threads)
Confidence: HIGH

Insight 6: Fee-Based Revenue Model Without Token Incentives for Bootstrap
Explanation: Walrus merancang fee-based economics (storage + retrieval fees) mirip cloud storage, token WAL untuk governance/staking/fee payment bukan primary incentive; tidak ada token incentives di testnet — berbeda dari Filecoin/Arweave/0G/Celestia/EigenDA yang semua menggunakan token incentives live untuk bootstrap network effects.
Evidence: Revenue model: Blob Storage Fees, Retrieval Fees, Validator Rewards — semua "Planned"【Phase 5 — Revenue Model】; Token sale: not announced; Adoption metrics: Volume $0 testnet【Phase 8 — Adoption Metrics】; Competitor landscape: semua major competitor have token incentives live【Phase 8 — Competitor Landscape】.
Supporting Dataset: Phase 5 Financial (Revenue Model, Fundraising Mechanism), Phase 6 Token (Utility, Distribution), Phase 8 Market (Adoption Metrics, Competitor Landscape)
Confidence: HIGH

Insight 7: Delayed Decentralization/Governance/Token Milestones Without Hard Deadlines
Explanation: Walrus Foundation/DAO "planned" sejak awal tapi no formation announcement, legal filing, atau timeline; Mainnet/TGE "projected 2024-2025" tapi tidak announced; Permissionless validator set "planned" tapi testnet masih permissioned; Tokenomics doc referenced tapi tidak public.
Evidence: Walrus Foundation/DAO: Planned, Not Yet Formed【Phase 2 — Foundation, DAO】; Market timeline: Mainnet/TGE projected not announced【Phase 3 — Market Timeline】; Validator group: testnet permissioned, mainnet planned permissionless【Phase 7 — Validator Group】; Tokenomics doc referenced tidak public【Phase 5 — Revenue Model, Phase 6 — Token】.
Supporting Dataset: Phase 2 Entity (Foundation, DAO), Phase 3 History (Market Timeline), Phase 5 Financial (Dependencies), Phase 6 Token (all), Phase 7 Ecosystem (Governance, Validator Group), Phase 8 Market (Market Timeline, Open Threads)
Confidence: HIGH

Insight 8: Early Ecosystem Partnerships for Product-Market Fit Validation
Explanation: Walrus mengintegrasikan aplikasi real (Akord vault, Decrypt media archive) di testnet untuk validasi product-market fit sebelum mainnet, menunjukkan developer-first approach dengan SDK/CLI/HTTP API lengkap dan hackathons/grants untuk adoption.
Evidence: Major integrations: Akord (Live Testnet), Decrypt Media (Beta)【Phase 7 — Major Integrations】; Applications: Akord built on Walrus, Decrypt pilot【Phase 7 — Applications】; Developer ecosystem: TS SDK, HTTP API, CLI, Sites CLI, Sui Foundation Grants, Sui Overflow hackathons【Phase 7 — Developer Ecosystem】; GitHub stars ~500+【Phase 8 — Adoption Metrics】.
Supporting Dataset: Phase 7 Ecosystem (Major Integrations, Applications, Developer Ecosystem), Phase 8 Market (Adoption Metrics)
Confidence: HIGH

Insight 9: FTX Ventures Exposure as Unresolved Financial Risk
Explanation: Series B $300M dipimpin FTX Ventures (Sep 2022); FTX bankruptcy Nov 2022 menciptakan ketidakpastian equity/clawback; tidak ada official statement resolusi; operasi lanjut normal dengan treasury existing — risiko HIGH yang belum terpecahkan.
Evidence: Series B led by FTX Ventures $300M【Phase 3 — Mysten Labs Series B】; Coindesk article Nov 2022 tentang FTX investment complexity【Phase 3 — Coindesk Article】; Financial risk: FTX Ventures Exposure HIGH【Phase 5 — Financial Risk】; Financial dependencies: FTX Ventures status Uncertain【Phase 5 — Financial Dependencies】; Open threads: status equity FTX conflicting reports, no official settlement【Phase 8 — Open Threads】.
Supporting Dataset: Phase 3 History (Series B, Coindesk Article), Phase 5 Financial (Financial Risk, Financial Dependencies), Phase 8 Market (Open Threads)
Confidence: HIGH

Insight 10: Conservative Technical Risk Tolerance, Aggressive Integration Strategy
Explanation: Conservative pada consensus/storage layer (extended permissioned testnet, no mainnet date) tapi aggressive pada integrations (Wormhole announcement, Seal, SNS, Akord, Decrypt) — memprioritaskan keamanan core protocol sambil memperluas ecosystem surface area.
Evidence: Testnet permissioned extended, no mainnet date【Phase 3 — Testnet Launch】; Technical limitations: centralized testnet HIGH【Phase 4 — Technical Limitations】; Wormhole announced 2024 no specs【Phase 3 — Wormhole Announcement】; Seal/SNS/Akord/Decrypt integrations 2024【Phase 7 — Major Integrations】.
Supporting Dataset: Phase 3 History (Testnet Launch, Wormhole Announcement), Phase 4 Technology (Technical Limitations), Phase 7 Ecosystem (Major Integrations)
Confidence: HIGH

## Strategic Principles

Principle 1: Native Integration First — Build Deep Platform Moat Before Cross-Chain Expansion
Explanation: Semua fitur core (Walrus Sites, Seal, blob metadata, programmable access) dibangun native pada Move VM dan Sui consensus terlebih dahulu; cross-chain via Wormhole datang belakangan sebagai expansion layer, bukan core architecture.
Evidence: Core protocol developed 2022-2024, integrations announced 2024 setelah testnet live【Phase 3 — Timeline】; Primary chain Sui (Critical), Wormhole (High, Planned)【Phase 7 — Primary Chain, External Dependencies】; Narrative: Sui Ecosystem primary, Cross-chain secondary【Phase 8 — Narrative Position】.
Supporting Dataset: Phase 3 History, Phase 7 Ecosystem, Phase 8 Market
Confidence: HIGH

Principle 2: Parent Company Resource Leverage — Use Mysten Labs Capital, Talent, Infra, Distribution Fully
Explanation: Tidak membangun entity/ops independen prematur; semua funding, infrastructure, legal, grants, talent berasal dari Mysten Labs; independence (DAO, Foundation, treasury) ditunda hingga mainnet readiness.
Evidence: $428M via Mysten Labs rounds【Phase 5 — Funding History】; Infrastructure operated by Mysten Labs【Phase 7 — Infrastructure Providers】; Grants via Sui Foundation/Mysten Labs【Phase 7 — Developer Ecosystem】; Walrus Foundation/DAO planned not formed【Phase 2 — Foundation, DAO】.
Supporting Dataset: Phase 2 Entity, Phase 3 History, Phase 5 Financial, Phase 7 Ecosystem
Confidence: HIGH

Principle 3: Controlled Rollout Over Hype-Driven Launch — Quality and Safety Over Speed to Mainnet
Explanation: Memilih testnet permissioned berbulan-bulan dengan curated validator set, no token, no public mainnet date, no tokenomics public — prioritaskan protocol hardening, developer feedback, real application validation over community pressure atau competitor timing.
Evidence: Testnet permissioned 2024, no mainnet date announced【Phase 3 — Testnet Launch】; No token on testnet, using test SUI【Phase 6 — Token】; Tokenomics doc referenced not public【Phase 5 — Revenue Model】; Competitors (0G, Celestia, EigenDA) already launched tokens【Phase 8 — Competitor Landscape】.
Supporting Dataset: Phase 3 History, Phase 5 Financial, Phase 6 Token, Phase 8 Market
Confidence: HIGH

Principle 4: Programmable Storage as Core Differentiation — Not Generic Storage
Explanation: Fokus pada differentiator unik: Move VM native calls, Seal threshold encryption, Walrus Sites, on-chain blob metadata — bukan competing pada cost-per-GB vs Filecoin/Arweave/Storj yang generic.
Evidence: Whitepaper: erasure coding + PoA berbeda dari PoRep/endowment【Phase 4 — Architecture】; Seal integration live testnet【Phase 7 — Seal Integration】; Walrus Sites core app【Phase 7 — Walrus Sites】; Narrative: Programmable Storage primary【Phase 8 — Narrative Position】.
Supporting Dataset: Phase 4 Technology, Phase 7 Ecosystem, Phase 8 Market
Confidence: HIGH

Principle 5: Developer-First Tooling Investment Before Mainnet
Explanation: Heavy investment pada SDK (TS/Rust), CLI, HTTP API, Sites CLI, hackathons (Sui Overflow), grants sebelum mainnet — memastikan developer experience siap saat mainnet launch.
Evidence: Developer ecosystem: TS SDK, HTTP API, CLI, Sites CLI, Grants, Hackathons【Phase 7 — Developer Ecosystem】; GitHub stars ~500+【Phase 8 — Adoption Metrics】; Akord menggunakan SDK【Phase 7 — Applications】.
Supporting Dataset: Phase 7 Ecosystem, Phase 8 Market
Confidence: HIGH

Principle 6: Fee-Based Sustainable Economics Over Token Incentive Bootstrap
Explanation: Merancang economics berbasis fee (storage + retrieval) yang predictable dan sustainable seperti cloud; token untuk governance/staking bukan primary incentive; menhindari inflationary tokenomics yang menciptakan sell pressure.
Evidence: Revenue model: planned fees only【Phase 5 — Revenue Model】; Token utility: governance, staking, fee payment planned【Phase 6 — Token】; Competitors all use token incentives【Phase 8 — Competitor Landscape】; Adoption metrics: volume $0 testnet【Phase 8 — Adoption Metrics】.
Supporting Dataset: Phase 5 Financial, Phase 6 Token, Phase 8 Market
Confidence: HIGH

Principle 7: Minimal Public Transparency as Strategic OpSec — Avoid Premature Scrutiny
Explanation: Tidak mempublikasikan treasury, tokenomics, adoption metrics, validator list, FTX status — melindungi competitive positioning, flexibility pivot, regulatory exposure; trade-off: trust deficit dan governance credibility gap.
Evidence: Treasury/transparency report not available【Phase 5 — Treasury】; Token all not disclosed【Phase 6 — Token】; Adoption metrics mostly unknown【Phase 8 — Adoption Metrics】; Validator group not enumerated【Phase 7 — Validator Group】; Open threads banyak "tidak diketahui"【Phase 8 — Open Threads】.
Supporting Dataset: Phase 5 Financial, Phase 6 Token, Phase 7 Ecosystem, Phase 8 Market
Confidence: HIGH

## Success Factors

Factor 1: Deep Technical Differentiation via Native Move/Sui Architecture
Explanation: Arsitektur erasure coding + proof-of-availability yang native ke Move VM dan Sui consensus menciptakan moat teknis yang sulit direplikasi kompetitor; memungkinkan fitur unik (Seal, Sites, programmable blob access) yang bukan sekadar storage.
Evidence: Whitepaper 2-layer design (Red Stuff + Blue Stuff) berbeda dari Filecoin/Arweave【Phase 4 — Architecture】; Seal encryption live testnet menggunakan Sui threshold encryption【Phase 7 — Seal Integration】; Walrus Sites native Sui objects【Phase 7 — Walrus Sites】; Competitor landscape: tidak ada yang native Move/Sui【Phase 8 — Competitor Landscape】.
Supporting Dataset: Phase 4 Technology, Phase 7 Ecosystem, Phase 8 Market
Confidence: HIGH

Factor 2: Strong Parent Backing with $428M Capital and Top-Tier VC Network
Explanation: Mysten Labs funding dari a16z crypto (lead Seed+A), FTX Ventures (lead B), Coinbase Ventures, Circle, dll memberikan capital runway panjang, talent attraction, dan ecosystem distribution via Sui.
Evidence: Funding rounds: $36M Seed, $92M Series A (a16z lead), $300M Series B (FTX lead)【Phase 5 — Funding History】; Investors: a16z, Coinbase, Circle, Samsung Next, Slow Ventures【Phase 2 — Entity a16z, FTX, etc】; Sui ecosystem distribution【Phase 7 — Primary Chain Sui】.
Supporting Dataset: Phase 2 Entity, Phase 3 History, Phase 5 Financial
Confidence: HIGH

Factor 3: Real Applications Validating Product-Market Fit on Testnet
Explanation: Akord (vault app) dan Decrypt (media archive) live/beta di testnet membuktikan developer adoption dan real use cases sebelum mainnet — bukan vaporware.
Evidence: Akord integration live testnet【Phase 7 — Major Integrations】; Decrypt Media pilot beta【Phase 7 — Applications】; Seal encryption live testnet【Phase 7 — Seal Integration】; Walrus Sites core app live testnet【Phase 7 — Walrus Sites】.
Supporting Dataset: Phase 7 Ecosystem
Confidence: HIGH

Factor 4: Mature Developer Tooling Ready for Adoption
Explanation: TypeScript/Rust SDK, HTTP API, CLI, Sites CLI, grants program, hackathons sudah siap sebelum mainnet — mengurangi friction untuk developer onboarding.
Evidence: Developer ecosystem lengkap【Phase 7 — Developer Ecosystem】; GitHub stars ~500+【Phase 8 — Adoption Metrics】; Akord built using SDK【Phase 7 — Applications】.
Supporting Dataset: Phase 7 Ecosystem, Phase 8 Market
Confidence: HIGH

Factor 5: Clear Programmable Storage Narrative Differentiation
Explanation: Positioning sebagai "programmable storage layer" bukan generic storage menciptakan kategori baru yang menghindari head-to-head competition dengan Filecoin/Arweave/Storj pada cost-per-GB.
Evidence: Narrative: Programmable Storage primary, DePIN primary, Modular DA secondary【Phase 8 — Narrative Position】; Competitor landscape: semua competitor generic storage atau DA【Phase 8 — Competitor Landscape】.
Supporting Dataset: Phase 8 Market
Confidence: HIGH

## Failure Factors

Factor 1: Zero Financial Transparency Creating Trust Deficit
Explanation: Tidak ada treasury dashboard, transparency report, tokenomics detail, atau allocation breakdown — menyulitkan investor/community assess sustainability, menciptakan governance credibility gap untuk future DAO.
Evidence: Treasury semua field "Tidak diungkap"【Phase 5 — Treasury】; Transparency report tidak tersedia【Phase 5 — Official Financial Resources】; Token semua field "Tidak diungkap"【Phase 6 — Token】; Open threads: banyak "tidak diketahui"【Phase 8 — Open Threads】.
Supporting Dataset: Phase 5 Financial, Phase 6 Token, Phase 8 Market
Confidence: HIGH

Factor 2: Single-Chain Dependency with Unproven Cross-Chain Mitigation
Explanation: Fully dependent pada Sui consensus; Wormhole integration hanya announcement, technical specs tidak public, belum live, dan menambah bridge risk — single point of failure belum terpecahkan.
Evidence: Sui Blockchain dependency Critical【Phase 7 — External Dependencies】; Risk: Single Chain Dependency HIGH【Phase 8 — Ecosystem Risks】; Wormhole: High, Planned, specs tidak public【Phase 7 — External Dependencies】; Wormhole announcement 2024 no docs【Phase 3 — Wormhole Announcement】.
Supporting Dataset: Phase 7 Ecosystem, Phase 8 Market
Confidence: HIGH

Factor 3: Unresolved FTX Ventures Equity Risk
Explanation: Series B lead investor FTX Ventures ($300M) bankruptcy menciptakan ketidakpastian equity/clawback; tidak ada official resolution disclosure setelah 2+ tahun — potential financial/legal overhang.
Evidence: Series B FTX lead $300M【Phase 3 — Series B】; Coindesk article Nov 2022【Phase 3 — Coindesk Article】; Financial risk: FTX Exposure HIGH【Phase 5 — Financial Risk】; FTX status Uncertain【Phase 5 — Financial Dependencies】; Open threads: conflicting reports, no official settlement【Phase 8 — Open Threads】.
Supporting Dataset: Phase 3 History, Phase 5 Financial, Phase 8 Market
Confidence: HIGH

Factor 4: Delayed Decentralization/Token/Governance Without Timeline
Explanation: Walrus Foundation/DAO "planned" sejak awal tapi no formation, no legal filing, no timeline; mainnet/TGE projected tapi tidak announced; permissionless validator set planned tapi testnet masih permissioned — execution risk vs competitors executing.
Evidence: Foundation/DAO planned not formed【Phase 2 — Foundation, DAO】; Market timeline: mainnet/TGE projected not announced【Phase 3 — Market Timeline】; Validator group testnet permissioned【Phase 7 — Validator Group】; Tokenomics not public【Phase 6 — Token】; Competitors have live tokens/governance【Phase 8 — Competitor Landscape】.
Supporting Dataset: Phase 2 Entity, Phase 3 History, Phase 6 Token, Phase 7 Ecosystem, Phase 8 Market
Confidence: HIGH

Factor 5: No Token Incentives for Storage Node Bootstrap
Explanation: Fee-based model tanpa token incentives untuk bootstrap storage node network effects; testnet nodes tidak mendapat real rewards; competitor (Filecoin, Arweave, 0G, Celestia, EigenDA) semua menggunakan token incentives live.
Evidence: Revenue model planned fees only【Phase 5 — Revenue Model】; Token sale not announced【Phase 5 — Fundraising Mechanism】; Adoption metrics: volume $0 testnet【Phase 8 — Adoption Metrics】; Competitors all have token incentives【Phase 8 — Competitor Landscape】.
Supporting Dataset: Phase 5 Financial, Phase 8 Market
Confidence: HIGH

Factor 6: Centralized Testnet Operations Not Representative of Mainnet
Explanation: Testnet validators permissioned, Mysten Labs dominant operator, cloud infrastructure concentrated (GCP/AWS) — decentralization claims unproven at scale; community validators curated tidak permissionless.
Evidence: Validator group testnet permissioned【Phase 7 — Validator Group】; Infrastructure: Mysten Labs critical, cloud providers medium【Phase 7 — Infrastructure Providers】; Technical limitations: centralized testnet HIGH【Phase 4 — Technical Limitations】; Risk: centralized testnet operation HIGH【Phase 8 — Ecosystem Risks】.
Supporting Dataset: Phase 4 Technology, Phase 7 Ecosystem, Phase 8 Market
Confidence: HIGH

## Decision Framework

Observe → Market Gap Identification
- Identifikasi kebutuhan programmable storage native untuk Sui/Move yang tidak terpenuhi Filecoin/Arweave【Phase 1 — Core Objective】【Phase 4 — Architecture】

Evaluate → Technical Architecture Selection
- Pilih erasure coding + proof-of-availability di atas Sui consensus (bukan PoRep/endowment) untuk throughput tinggi, deletability, Move VM integration【Phase 4 — Architecture, Consensus】【Phase 8 — Competitor Landscape】

Fund → Parent Company Capital Allocation
- Alokasikan capital dari Mysten Labs VC rounds ($428M total) untuk Walrus development tanpa separate raise【Phase 5 — Funding History】【Phase 2 — Entity Mysten Labs】

Develop → Core Protocol First, Extended Permissioned Testnet
- Bangun core protocol 2022-2024; launch testnet permissioned 2024 Q2-Q3 dengan curated validators, Mysten Labs infra, no token, test SUI【Phase 3 — Testnet Launch】【Phase 7 — Validator Group】

Integrate → Ecosystem Partnerships for Validation
- Integrasikan aplikasi real (Akord, Decrypt), Seal encryption, SNS naming, Walrus Sites di testnet untuk PMF validation【Phase 7 — Major Integrations, Applications】【Phase 3 — Akord/Decrypt Integration】

Expand → Cross-Chain via Single Bridge Partner
- Announce Wormhole partnership untuk cross-chain access; technical details later【Phase 3 — Wormhole Announcement】【Phase 7 — Wormhole Integration】

Delay → Token/Governance/Decentralization Until Mainnet Ready
- Tidak launch token di testnet; delay WAL TGE, DAO formation, permissionless validators hingga mainnet readiness【Phase 6 — Token】【Phase 2 — Foundation, DAO】【Phase 3 — Market Timeline】

Govern → Centralized Stewardship Transitioning to Planned DAO
- Mysten Labs sebagai steward testnet; Walrus Foundation/DAO planned untuk mainnet governance【Phase 7 — Governance Ecosystem】【Phase 2 — Foundation, DAO】

## Reusable Playbook

Playbook 1: Build Platform-Native Infrastructure First, Then Expand Cross-Chain
- Bangun core protocol native ke target chain (Move/Sui) dengan deep integration (VM calls, native objects, consensus leverage) sebelum cross-chain bridge.
- Evidence: Walrus core protocol 2022-2024 native Sui/Move; Wormhole announcement 2024 setelah testnet live【Phase 3 — Timeline】【Phase 7 — Primary Chain, External Dependencies】.
- Applicable when: Target chain memiliki unique VM/consensus features yang enables differentiation.

Playbook 2: Leverage Parent Company Resources Fully Before Spinning Out
- Gunakan parent company capital, talent, infra, legal, distribution untuk protocol development; delay independent entity/treasury/DAO hingga product-market fit terbukti.
- Evidence: $428M via Mysten Labs, infra operated by Mysten Labs, grants via Sui Foundation, Foundation/DAO planned not formed【Phase 5 — Funding History】【Phase 7 — Infrastructure, Developer Ecosystem】【Phase 2 — Foundation, DAO】.
- Applicable when: Parent company well-capitalized dan aligned dengan protocol vision.

Playbook 3: Extended Permissioned Testnet for Complex Protocol Hardening
- Jalankan testnet permissioned 6-12+ bulan dengan curated validators, parent company infra, no token, real application integrations untuk de-risk core protocol sebelum permissionless mainnet.
- Evidence: Testnet permissioned 2024, ~50-100 nodes curated, Akord/Decrypt/Seal live, no mainnet date【Phase 3 — Testnet Launch】【Phase 7 — Validator Group, Major Integrations】.
- Applicable when: Protocol complexity tinggi (novel consensus, storage economics, VM integration) dan cost of failure tinggi.

Playbook 4: Developer-First Tooling Investment Before Mainnet
- Investasi heavy pada SDK (multi-language), CLI, HTTP API, specialized tooling (Sites CLI), grants, hackathons sebelum mainnet — developer experience sebagai moat.
- Evidence: TS/Rust SDK, HTTP API, CLI, Sites CLI, Sui Foundation Grants, Sui Overflow hackathons, GitHub stars ~500+【Phase 7 — Developer Ecosystem】【Phase 8 — Adoption Metrics】.
- Applicable when: Success bergantung pada developer adoption dan ecosystem applications.

Playbook 5: Fee-Based Sustainable Economics Design Over Token Incentive Bootstrap
- Desain economics berbasis fee (usage-based) yang predictable; token untuk governance/staking/fee payment bukan primary incentive; hindari inflationary tokenomics.
- Evidence: Revenue model planned fees only, token utility governance/staking/fee, competitors all token incentives【Phase 5 — Revenue Model】【Phase 6 — Token】【Phase 8 — Competitor Landscape】.
- Applicable when: Protocol dapat generate real revenue dari usage (storage, compute, bandwidth) dan target sustainable economics.

Playbook 6: Strategic OpSec — Minimal Public Transparency Until Mainnet
- Batasi public disclosure pada treasury, tokenomics, adoption metrics, validator details hingga mainnet readiness — hindari premature scrutiny, protect flexibility, manage regulatory exposure.
- Evidence: Treasury/token/adoption metrics all not disclosed, validator group not enumerated, FTX status not clarified【Phase 5 — Treasury】【Phase 6 — Token】【Phase 8 — Adoption Metrics】【Phase 7 — Validator Group】.
- Applicable when: Pre-mainnet, pre-token, regulatory uncertainty tinggi, competitive landscape sensitif.

Playbook 7: Early Real Application Partnerships for PMF Validation
- Integrasikan aplikasi real (bukan demo) di testnet untuk validate product-market fit, uncover bugs, generate case studies sebelum mainnet.
- Evidence: Akord vault app live testnet, Decrypt media archive pilot, Seal encryption live【Phase 7 — Major Integrations, Applications】.
- Applicable when: Protocol memerlukan application-layer validation dan developer feedback loop.

## Anti-patterns

Anti-pattern 1: Over-Centralization Without Credible Decentralization Roadmap
- Testnet permissioned, Mysten Labs dominant operator, cloud infrastructure concentrated, Foundation/DAO planned tanpa timeline/legal filing — desentralisasi claims tidak credible.
- Evidence: Validator group testnet permissioned【Phase 7 — Validator Group】; Infrastructure: Mysten Labs critical, cloud medium【Phase 7 — Infrastructure Providers】; Foundation/DAO planned not formed【Phase 2 — Foundation, DAO】; Risk: centralized testnet HIGH【Phase 8 — Ecosystem Risks】.
- Avoid by: Publishing concrete decentralization roadmap dengan milestone, timeline, dan criteria untuk permissionless transition.

Anti-pattern 2: Premature Cross-Chain Announcement Without Technical Specs
- Announce Wormhole partnership 2024 tapi technical specifications, launch timeline, fee model, token requirements tidak public — menciptakan hype tanpa substance, bridge risk tidak quantified.
- Evidence: Wormhole announced 2024, specs tidak public【Phase 3 — Wormhole Announcement】; Wormhole dependency High Planned【Phase 7 — External Dependencies】; Risk: bridge dependency MEDIUM【Phase 8 — Ecosystem Risks】.
- Avoid by: Hanya announce cross-chain integrations setelah technical design review, testnet integration, dan docs public.

Anti-pattern 3: Zero Financial Transparency During VC-Funded Development
- Tidak mempublikasikan treasury allocation, tokenomics, adoption metrics, investor equity status (FTX) — trust deficit, governance credibility gap, sulit benchmark vs competitor.
- Evidence: Treasury/transparency not available【Phase 5 — Treasury】; Token all not disclosed【Phase 6 — Token】; Adoption metrics unknown【Phase 8 — Adoption Metrics】; FTX status unresolved【Phase 5 — Financial Risk】.
- Avoid by: Minimum viable transparency: quarterly treasury snapshot, high-level tokenomics framework, basic adoption metrics dashboard.

Anti-pattern 4: Delaying Token/Governance/DAO Indefinitely Without Forcing Function
- Foundation/DAO "planned" sejak awal, mainnet/TGE projected tapi no date, permissionless validators planned tapi testnet permissioned — execution drift, competitor advantage, community misalignment.
- Evidence: Foundation/DAO planned not formed【Phase 2 — Foundation, DAO】; Market timeline mainnet/TGE not announced【Phase 3 — Market Timeline】; Validator group testnet permissioned【Phase 7 — Validator Group】; Competitors live tokens【Phase 8 — Competitor Landscape】.
- Avoid by: Set internal forcing functions (testnet graduation criteria, mainnet checklist, DAO formation deadline) dan communicate high-level timeline.

Anti-pattern 5: Single-Chain Dependency Without Live Cross-Chain Mitigation
- Fully dependent pada Sui consensus; cross-chain mitigation hanya announcement (Wormhole) belum live, no technical specs, bridge risk additional — single point of failure.
- Evidence: Sui dependency Critical【Phase 7 — External Dependencies】; Wormhole High Planned specs not public【Phase 7 — External Dependencies】; Risk single chain HIGH【Phase 8 — Ecosystem Risks】.
- Avoid by: Parallel development cross-chain adapters, multiple bridge options, atau chain-agnostic architecture dari awal.

Anti-pattern 6: No Token Incentives for Supply-Side Bootstrap in DePIN
- Fee-based model saja tanpa token incentives untuk storage node operators; testnet nodes no real rewards; competitors all use token incentives — supply-side adoption barrier.
- Evidence: Revenue model fees only【Phase 5 — Revenue Model】; Token sale not announced【Phase 5 — Fundraising Mechanism】; Volume $0 testnet【Phase 8 — Adoption Metrics】; Competitors all token incentives【Phase 8 — Competitor Landscape】.
- Avoid by: Design token incentive program untuk supply-side bootstrap (storage nodes, validators) yang transitions ke fee-based sustainable economics.

## Lessons Learned

Lesson 1: Native Platform Integration Creates Defensible Moat But Increases Platform Risk
- Deep integration ke Sui/Move memberikan differentiation unik (programmable storage) tapi menciptakan single-chain dependency yang memerlukan cross-chain strategy yang credible dan live.

Lesson 2: Parent Company Leverage Accelerates Development But Delays Independent Governance
- Mysten Labs resources memungkinkan $428M funding, top talent, infra ops tanpa dilution protokol; tapi menciptakan financial opacity, FTX exposure, dan complex carve-out untuk DAO formation.

Lesson 3: Extended Permissioned Testnet Reduces Technical Risk But Increases Centralization Perception
- 6-12+ bulan permissioned testnet memungkinkan protocol hardening dengan real apps (Akord, Decrypt, Seal); tapi community validators curated, Mysten Labs dominant, cloud concentrated — decentralization narrative gap.

Lesson 4: Fee-Based Economics More Sustainable But Slower Bootstrap Than Token Incentives
- Storage/retrieval fee model predictable seperti cloud; tapi tanpa token incentives, storage node bootstrap lambat vs competitor (Filecoin mining, Arweave endowment, 0G/Celestia/EigenDA token rewards).

Lesson 5: Strategic OpSec Has Costs — Trust Deficit and Governance Credibility Gap
- Minimal transparency melindungi competitive position dan regulatory exposure; tapi menciptakan investor/community skepticism, sulit benchmark, DAO governance legitimacy challenge di masa depan.

Lesson 6: Real Application Integrations > Announcements for PMF Validation
- Akord dan Decrypt live di testnet memberikan signal product-market fit yang stronger dari partnership announcements saja; developer tooling maturity (SDK, CLI, API) enables ini.

Lesson 7: Unresolved Major Investor Risk (FTX) Creates Persistent Overhang
- FTX Ventures equity status tidak diklarifikasi 2+ tahun pasca-bankruptcy — legal/financial uncertainty yang mengurangi confidence; proactive communication diperlukan.

Lesson 8: Delaying Decentralization Milestones Without Forcing Functions Causes Drift
- "Planned" tanpa timeline/legal filing/deadline mengakibatkan execution drift; competitors (0G, Celestia, EigenDA) execute faster dengan live tokens/governance.

## Knowledge Summary

Strategic Principles:
1. Native Integration First — Build Deep Platform Moat Before Cross-Chain Expansion
2. Parent Company Resource Leverage — Use Mysten Labs Capital, Talent, Infra, Distribution Fully
3. Controlled Rollout Over Hype-Driven Launch — Quality and Safety Over Speed to Mainnet
4. Programmable Storage as Core Differentiation — Not Generic Storage
5. Developer-First Tooling Investment Before Mainnet
6. Fee-Based Sustainable Economics Over Token Incentive Bootstrap
7. Minimal Public Transparency as Strategic OpSec — Avoid Premature Scrutiny

Success Factors:
1. Deep Technical Differentiation via Native Move/Sui Architecture
2. Strong Parent Backing with $428M Capital and Top-Tier VC Network
3. Real Applications Validating Product-Market Fit on Testnet
4. Mature Developer Tooling Ready for Adoption
5. Clear Programmable Storage Narrative Differentiation

Failure Factors:
1. Zero Financial Transparency Creating Trust Deficit
2. Single-Chain Dependency with Unproven Cross-Chain Mitigation
3. Unresolved FTX Ventures Equity Risk
4. Delayed Decentralization/Token/Governance Without Timeline
5. No Token Incentives for Storage Node Bootstrap
6. Centralized Testnet Operations Not Representative of Mainnet

Decision Framework:
Observe (Market Gap) → Evaluate (Architecture) → Fund (Parent Capital) → Develop (Core Protocol + Permissioned Testnet) → Integrate (Ecosystem Apps) → Expand (Cross-Chain) → Delay (Token/Governance) → Govern (Centralized→Planned DAO)

Reusable Playbook:
1. Build Platform-Native Infrastructure First, Then Expand Cross-Chain
2. Leverage Parent Company Resources Fully Before Spinning Out
3. Extended Permissioned Testnet for Complex Protocol Hardening
4. Developer-First Tooling Investment Before Mainnet
5. Fee-Based Sustainable Economics Design Over Token Incentive Bootstrap
6. Strategic OpSec — Minimal Public Transparency Until Mainnet
7. Early Real Application Partnerships for PMF Validation

Anti-patterns:
1. Over-Centralization Without Credible Decentralization Roadmap
2. Premature Cross-Chain Announcement Without Technical Specs
3. Zero Financial Transparency During VC-Funded Development
4. Delaying Token/Governance/DAO Indefinitely Without Forcing Function
5. Single-Chain Dependency Without Live Cross-Chain Mitigation
6. No Token Incentives for Supply-Side Bootstrap in DePIN

## Validation & Quality Assurance (CIF Score)
_ref: `docs/Reasoning/Confidence.md` — CIF Score, Data Lineage, Knowledge Dependency Graph_

CIF VALIDATION REPORT v3.0

---

CIF MANIFEST v3.0

```
CIF MANIFEST v3.0

Project: Walrus
Symbol: WAL
Research Date: 2026-08-20
CIF Version: 3.0
QA Date: 2026-08-20

METRICS
Total Knowledge Objects: 12
Total Entities: 15
Total Events: 6
Evidence Links: 34
Sources: 8
Conflicts: 3
  ├── Resolved: 1
  ├── Critical: 0
  ├── High: 1
  ├── Medium: 1
  └── Low: 1

QUALITY SCORES
Research Quality: 90/100
Consistency: 85/100
Evidence: 80/100
Coverage: 70/100
Conflict: 70/100
Knowledge: 80/100
CIF SCORE: 80.5/100

CONFIDENCE LEVEL: MEDIUM
QA STATUS: PASSED

RECOMMENDED RE-RUN:
  - Phase 04 — Technology — laporan audit keamanan pihak ketiga belum ditemukan di sumber publik
  - Phase 06 — Token — rincian unlock 20% alokasi subsidies/foundation belum dipublikasikan penuh
```

---

DATASET INTEGRITY & COVERAGE

Integritas dataset Walrus dinilai dari fase 1-10 yang tersedia. Fase 1, 2, 3, 4, dan 6 direkonstruksi via riset langsung (web) pada 2026-08-20 setelah file aslinya hilang pada run pipeline 2026-08-15; fase 5, 7, 8, 9, 10 adalah output pipeline yang lulus audit. Sumber rekonstruksi: CoinDesk, Altcoin Buzz, Backpack Exchange Learn, Imperator — semuanya pihak kedua/ketiga; tidak ada dokumen primer (blog resmi Walrus/whitepaper) yang diakses langsung dalam rekonstruksi ini, sehingga Evidence dibatasi MEDIUM untuk fakta yang hanya ditopang satu sumber sekunder. (HIGH) [CoinDesk, https://www.coindesk.com/business/2025/03/20/data-storage-protocol-walrus-raises-usd140m-in-token-sale-ahead-of-mainnet-launch]

---

COVERAGE REPORT — Multi-dimensional

Phase 1 — Foundation

· Total: 18
· Coverage: 88%
· Catatan: field inti lengkap; testnet exact date dan alamat kontrak WAL belum terisi

Phase 2 — Entity

· Total: 15
· Coverage: 85%
· Catatan: 15 entitas dengan relationship + evidence; daftar lengkap investor token sale di luar 5 nama terkonfirmasi belum tersedia

Phase 3 — History

· Total: 6
· Coverage: 82%
· Catatan: 6 event founding→TGE→airdrop; tanggal persis testnet Desember 2024 belum dirinci

Phase 4 — Technology

· Total: 10
· Coverage: 65%
· Catatan: arsitektur blob storage + erasure coding terdokumentasi; audit history kosong; spesifikasi teknis lengkap "Red Stuff" belum diakses

Phase 5 — Financial

· Total: 12
· Coverage: 75%
· Catatan: token sale $140M terverifikasi; pendapatan storage aktual tidak dipublikasikan

Phase 6 — Token

· Total: 16
· Coverage: 72%
· Catatan: supply 5B WAL + distribusi terdokumentasi dengan INKONSISTENSI dua sumber sekunder yang dicatat jujur; jadwal unlock contributors belum rinci

Phase 7 — Ecosystem

· Total: 10
· Coverage: 70%
· Catatan: fase pipeline existing; partner utama (Lombard, Sui ecosystem) tercakup

Phase 8 — Market

· Total: 10
· Coverage: 68%
· Catatan: fase pipeline existing; data harga historis kini dilengkapi via KuCoin candle (riset 2026-08-20)

Phase 9 — Behavioral

· Total: 8
· Coverage: 66%
· Catatan: fase pipeline existing

Phase 10 — Knowledge

· Total: 12
· Coverage: 74%
· Catatan: fase pipeline existing

---

CONFLICT REGISTER WITH SEVERITY & IMPACT

Conflict C-001 — Breakdown distribusi WAL berbeda antar sumber sekunder
· Category: Tokenomics
· Description: Altcoin Buzz menyebut Community Reserve 43% dengan 690 juta token available at launch, sementara Backpack Exchange memecah 10% community airdrop (4% pre-mainnet + 6% post-mainnet) dari total 5 miliar; kedua angka dapat konsisten (690 juta = porsi cair awal dari reserve 43%) tetapi dokumen tokenomics resmi tidak diakses untuk konfirmasi
· Severity: Medium
· Affected Knowledge: K-tokenomics WAL
· Impact: Pembaca dapat salah membayangkan total airdrop (690 juta vs 500 juta)
· Affected Phase: Phase 6
· Evidence: Altcoin Buzz, Backpack Exchange
· Sources: https://www.altcoinbuzz.io/reviews/walrus-protocol-mainnet-and-tge-are-coming/, https://learn.backpack.exchange/articles/what-is-walrus-a-programmable-decentralized-storage-network
· Resolution: Kedua angka dipertahankan dengan flag INKONSISTENSI di Phase 6; menunggu dokumen tokenomics resmi
· Status: Unresolved

Conflict C-002 — Tanggal testnet Desember 2024 tanpa tanggal persis
· Category: Timeline
· Description: Sumber sekunder (Imperator, Backpack) menyebut testnet berjalan sebelum mainnet dengan fase Desember 2024, tetapi tanggal persis peluncuran testnet tidak dirinci di sumber yang diakses
· Severity: Low
· Affected Knowledge: K-timeline Walrus
· Impact: Ketidakpastian minor pada kronologi
· Affected Phase: Phase 3
· Evidence: Imperator, Backpack Exchange
· Sources: https://www.imperator.co/resources/blog/walrus-protocol, https://learn.backpack.exchange/articles/what-is-walrus-a-programmable-decentralized-storage-network
· Resolution: Dicatat sebagai open thread
· Status: Unresolved

Conflict C-003 — Klaim "salah satu airdrop terbesar" tanpa angka penerima
· Category: Distribution
· Description: Adeniyi Abiodun menyatakan airdrop WAL akan menjadi salah satu yang terbesar dan paling terdistribusi, namun jumlah wallet penerima dan besaran per wallet tidak dipublikasikan di sumber yang diakses
· Severity: Medium
· Affected Knowledge: K-airdrop WAL
· Impact: Klaim skala tidak dapat diverifikasi kuantitatif
· Affected Phase: Phase 3, Phase 6
· Evidence: Altcoin Buzz
· Sources: https://www.altcoinbuzz.io/reviews/walrus-protocol-mainnet-and-tge-are-coming/
· Resolution: Klaim dikutip sebagai pernyataan (bukan fakta terverifikasi); jumlah penerima menjadi open thread
· Status: Unresolved

---

CIF SCORE CALCULATION — v3.0

Dimensi dan Perhitungan:

Research Quality (25%)

· Complete Phases: 10 dari 10
· Score: (10/10) × 90 = 90
· Kontribusi: 90 × 0.25 = 22.5

Consistency (20%)

· Passed Checks: 6 dari 7
· Score: (6/7) × 100 = 85.7
· Kontribusi: 85.7 × 0.20 = 17.14

Evidence (15%)

· Average Evidence Weight (0-100): 80
· Kontribusi: 80 × 0.15 = 12.0

Coverage (15%)

· Overall Coverage (%): 70%
· Score: 70
· Kontribusi: 70 × 0.15 = 10.5

Conflict (15%)

· Conflict Score (%): 70%
· Kontribusi: 70 × 0.15 = 10.5

Knowledge (10%)

· Average Confidence Score: 80
· Kontribusi: 80 × 0.10 = 8.0

CIF Score = 22.5 + 17.14 + 12.0 + 10.5 + 10.5 + 8.0 = 80.64

Interpretasi:

· Excellent (>90): Tidak tercapai
· Good (80-90): Tercapai (80.64)
· Needs Improvement (60-80): Tidak
· Poor (<60): Tidak

CIF SCORE: 80.6/100 — GOOD

## Airdrop Intelligence
_ref: `docs/Ontology/DecisionEvent.md`, `docs/Ontology/Context.md` — an airdrop is a Decision Event with an eight-POV outcome_

PROJECT: Walrus

STATUS AIRDROP

Sudah dilakukan. Walrus mendistribusikan 10% total supply WAL (500 juta dari 5 miliar token) ke komunitas: 4% didistribusikan segera pasca-mainnet/TGE (klaim via portal resmi mulai 27 Maret 2025 untuk wallet eligible dari aktivitas testnet dan kampanye) dan 6% didistribusikan bertahap seiring kematangan ekosistem; co-founder Mysten menyebutnya salah satu airdrop terbesar dan paling terdistribusi meski jumlah penerima tidak dipublikasikan (HIGH) [Backpack Exchange, https://learn.backpack.exchange/articles/what-is-walrus-a-programmable-decentralized-storage-network]; (MEDIUM) [Altcoin Buzz, https://www.altcoinbuzz.io/reviews/walrus-protocol-mainnet-and-tge-are-coming/]

AIRDROP EVENTS

AD-001: Community Airdrop Pre-Mainnet (4% Supply)
Tanggal: 2025-03-27 (klaim dibuka seiring mainnet & TGE)
Tipe: Retroactive/partisipasi-based (aktivitas testnet, penyimpanan blob, staking testnet, kampanye komunitas)
Alokasi: 4% total supply (200.000.000 WAL dari 5 miliar) — bagian dari 10% alokasi komunitas (HIGH) [Backpack Exchange, https://learn.backpack.exchange/articles/what-is-walrus-a-programmable-decentralized-storage-network]
Penerima: Wallet yang berpartisipasi di Walrus Testnet dan kampanye ekosistem sebelum mainnet; jumlah penerima tidak dipublikasikan resmi (LOW)
Nilai saat klaim: 0.5390 USD per WAL (close hari TGE 2025-03-27; intraday range 0.1-0.97774) [KuCoin WAL-USDT daily candle, https://www.kucoin.com/trade/WAL-USDT] (MEDIUM)
Kriteria: Partisipasi testnet (menyimpan blob, staking WAL testnet, kontribusi) dan aktivitas kampanye; detail pembobotan per aktivitas tidak dipublikasikan penuh (MEDIUM) [Backpack Exchange, https://learn.backpack.exchange/articles/what-is-walrus-a-programmable-decentralized-storage-network]
Anti-sybil: Tidak dirinci publik; eligibility berbasis riwayat aktivitas on-chain testnet (LOW)
Terkait EV: EV-005 (Mainnet & TGE), EV-006 (distribusi airdrop komunitas)
Sitasi: Phase 3 EV-005, EV-006; Phase 6 Distribution (HIGH/MEDIUM)

AD-002: Community Distribution Post-Mainnet (6% Supply, Bertahap)
Tanggal: 2025-04 mulai — berlanjut bertahap sepanjang 2025
Tipe: Distribusi bertahap berbasis aktivitas ekosistem pasca-launch
Alokasi: 6% total supply (300.000.000 WAL) didistribusikan dalam fase-fase seiring kematangan ekosistem (HIGH) [Backpack Exchange, https://learn.backpack.exchange/articles/what-is-walrus-a-programmable-decentralized-storage-network]
Penerima: Partisipan ekosistem pasca-launch (pengguna storage, staker, kontributor); rincian per gelombang tidak dipublikasikan di sumber yang diakses (LOW)
Nilai saat klaim: Tidak berlaku (distribusi multi-gelombang; harga mengikuti pasar saat tiap gelombang)
Kriteria: Aktivitas mainnet (menyimpan data, staking, kontribusi ekosistem) sesuai pengumuman foundation per gelombang (MEDIUM)
Anti-sybil: Tidak dirinci publik (LOW)
Terkait EV: EV-006
Sitasi: Phase 3 EV-006; Phase 6 Distribution (HIGH/MEDIUM)

CONTEXT SAAT KEPUTUSAN

Kondisi saat keputusan distribusi WAL (Q1 2025):
- Kondisi pasar: Awal 2025 — narasi AI x crypto dan decentralized data/storage menguat; Sui ekosistem tumbuh pesat (Sui naik >40% dalam 12 bulan sebelumnya) (MEDIUM) [Altcoin Buzz, https://www.altcoinbuzz.io/product-release/crypto-gem-sui-is-launching-a-new-altcoin-today-walrus-wal/]
- Posisi project: Testnet sukses dengan partisipasi besar dari komunitas Sui; token sale $140 juta ditutup seminggu sebelum mainnet memberi modal penuh (HIGH) [CoinDesk, https://www.coindesk.com/business/2025/03/20/data-storage-protocol-walrus-raises-usd140m-in-token-sale-ahead-of-mainnet-launch]
- Kompetitor terdekat: Filecoin, Arweave, Akash (storage/infrastruktur terdesentralisasi) dengan model token berbeda; pembeda Walrus = storage terprogram di atas Sui untuk beban AI/data besar (MEDIUM) [Backpack Exchange, https://learn.backpack.exchange/articles/what-is-walrus-a-programmable-decentralized-storage-network]

TRIGGER DAN ALTERNATIF

Trigger utama: Peluncuran mainnet membutuhkan lapisan ekonomis aktif (pembayaran storage + staking node) sekaligus penghargaan partisipan testnet yang membangun traksi awal (HIGH) [Backpack Exchange, https://learn.backpack.exchange/articles/what-is-walrus-a-programmable-decentralized-storage-network].
Alternatif tidak diambil:
- Airdrop sekaligus 10% di hari TGE: tidak dipilih — dipecah 4% pre + 6% post untuk mempertahankan insentif partisipasi pasca-launch (MEDIUM) [Backpack Exchange, https://learn.backpack.exchange/articles/what-is-walrus-a-programmable-decentralized-storage-network]
- Public sale: tidak dilakukan; pendanaan via private token sale $140 juta (HIGH) [CoinDesk, https://www.coindesk.com/business/2025/03/20/data-storage-protocol-walrus-raises-usd140m-in-token-sale-ahead-of-mainnet-launch]

REASON — YANG DINYATAKAN VS YANG TIDAK

Alasan resmi:
- Menghargai komunitas yang membangun traksi testnet dan mendistribusikan kepemilikan luas ("salah satu airdrop terbesar dan paling terdistribusi") (MEDIUM) [Altcoin Buzz, https://www.altcoinbuzz.io/reviews/walrus-protocol-mainnet-and-tge-are-coming/]
- WAL sebagai pembayaran storage, staking, dan governance — distribusi luas memperkuat desentralisasi node storage (HIGH) [Backpack Exchange, https://learn.backpack.exchange/articles/what-is-walrus-a-programmable-decentralized-storage-network]

Alasan yang tidak diumumkan (HIPOTESIS):
- Pemecahan 4%/6% menahan tekanan jual hari pertama sekaligus mengunci retensi pengguna pasca-launch — HIPOTESIS (MEDIUM)
- Airdrop besar memanfaatkan basis pengguna Sui yang sudah ada sebagai saluran akuisisi murah — HIPOTESIS (MEDIUM) [Altcoin Buzz, https://www.altcoinbuzz.io/product-release/crypto-gem-sui-is-launching-a-new-altcoin-today-walrus-wal/]

OUTCOME PER POV

POV Founder (Mysten Labs / Walrus Foundation): Sukses
- Jangka pendek: TGE + mainnet terlaksana tepat jadwal; $140 juta token sale selesai pra-launch; listing MEXC hari pertama diikuti exchange lain (HIGH) [CoinDesk, https://www.coindesk.com/business/2025/03/20/data-storage-protocol-walrus-raises-usd140m-in-token-sale-ahead-of-mainnet-launch]; [Altcoin Buzz, https://www.altcoinbuzz.io/product-release/crypto-gem-sui-is-launching-a-new-altcoin-today-walrus-wal/]
- Jangka panjang: Jaringan storage produksi berjalan; namun harga WAL terdepresiasi ~85% dari close TGE dalam 12 bulan (0.539 → ~0.07-0.08 per data mingguan KuCoin Mar 2026) — tekanan naratif pada ekosistem [KuCoin WAL-USDT, https://www.kucoin.com/trade/WAL-USDT] (MEDIUM)
- Dasar: Phase 3 EV-004, EV-005; KuCoin price history (HIGH/MEDIUM)

POV VC (Standard Crypto, a16z crypto, Electric Capital, Franklin Templeton DA, RW3 Ventures): Sebagian
- Jangka pendek: Entry via token sale pra-TGE; harga hari TGE (high 0.97774 USD) memberi paper gain awal atas harga sale (tidak dipublikasikan) (MEDIUM) [KuCoin WAL-USDT, https://www.kucoin.com/trade/WAL-USDT]
- Jangka panjang: Alokasi investor 7% dengan cliff 12 bulan (unlock pertama ~Maret 2026) terjadi saat harga ~0.07-0.11 USD — jauh di bawah harga hari TGE; realisasi nilai tertekan (MEDIUM) [Altcoin Buzz, https://www.altcoinbuzz.io/reviews/walrus-protocol-mainnet-and-tge-are-coming/]; [KuCoin WAL-USDT, https://www.kucoin.com/trade/WAL-USDT]
- Dasar: Phase 6 Distribution, Vesting Schedule; KuCoin price history (HIGH/MEDIUM)

POV Retail (Penerima airdrop komunitas): Sebagian
- Jangka pendek: Penerima klaim 4% pre-mainnet mendapat WAL pada harga close TGE 0.5390 USD (high hari pertama 0.97774) — penjual hari pertama merealisasi gain dari biaya nol (MEDIUM) [KuCoin WAL-USDT, https://www.kucoin.com/trade/WAL-USDT]
- Jangka panjang: Harga turun ke ~0.4078 pada +90 hari dan ~0.07-0.08 per Maret 2026 (-85% dari close TGE); pemegang pasif mengalami depresiasi besar tanpa mekanisme penahan nilai (MEDIUM) [KuCoin WAL-USDT, https://www.kucoin.com/trade/WAL-USDT]
- Dasar: KuCoin price history (MEDIUM)

POV Community (Pengguna & peserta kampanye Sui/Walrus): Sebagian
- Jangka pendek: Distribusi luas (klaim portal + kampanye) berjalan; atensi komunitas Sui besar pada launch (MEDIUM) [Altcoin Buzz, https://www.altcoinbuzz.io/product-release/crypto-gem-sui-is-launching-a-new-altcoin-today-walrus-wal/]
- Jangka panjang: Gelombang 6% post-mainnet menjaga keterlibatan, namun nilai per token menurun tajam; jumlah penerima tidak pernah dipublikasikan sehingga skala klaim tidak terverifikasi (LOW)
- Dasar: Phase 3 EV-006; Phase 6 Distribution (HIGH/LOW)

POV Developer (Integrator SDK & aplikasi storage): Sukses
- Jangka pendek: SDK, docs, dan infrastruktur storage live sejak TGE; developer dapat langsung membangun aplikasi data/AI di atas Walrus (HIGH) [Backpack Exchange, https://learn.backpack.exchange/articles/what-is-walrus-a-programmable-decentralized-storage-network]
- Jangka panjang: Subsidi storage (bagian dari alokasi subsidies) mendukung adopsi; kelangsungan bergantung pendanaan foundation (MEDIUM) [Backpack Exchange, https://learn.backpack.exchange/articles/what-is-walrus-a-programmable-decentralized-storage-network]
- Dasar: Phase 4 Technology; Phase 7 Ecosystem (HIGH/MEDIUM)

POV Institution (Investor token sale & exchange): Sebagian
- Jangka pendek: Partisipasi institusional (termasuk Franklin Templeton Digital Assets) dan listing CEX luas sejak hari pertama (HIGH) [CoinDesk, https://www.coindesk.com/business/2025/03/20/data-storage-protocol-walrus-raises-usd140m-in-token-sale-ahead-of-mainnet-launch]
- Jangka panjang: Depresiasi harga 12 bulan dan jadwal unlock yang belum rinci penuh menjadi catatan portofolio (MEDIUM) [KuCoin WAL-USDT, https://www.kucoin.com/trade/WAL-USDT]
- Dasar: Phase 5 Financial; KuCoin price history (HIGH/MEDIUM)

POV Validator (Storage node operators / staker): Sebagian
- Jangka pendek: Staking WAL aktif sejak mainnet; reward epoch berjalan untuk node yang memvalidasi storage proofs (HIGH) [Backpack Exchange, https://learn.backpack.exchange/articles/what-is-walrus-a-programmable-decentralized-storage-network]
- Jangka panjang: Nilai reward dalam WAL terdepresiasi bersama harga; ekonomi node bergantung pertumbuhan permintaan storage riil (MEDIUM) [KuCoin WAL-USDT, https://www.kucoin.com/trade/WAL-USDT]
- Dasar: Phase 4 Technology; KuCoin price history (HIGH/MEDIUM)

POV Builder (Protokol yang membangun di Walrus/Sui): Sebagian
- Jangka pendek: Akses storage terprogram + likuiditas ekosistem Sui sejak launch (MEDIUM) [Altcoin Buzz, https://www.altcoinbuzz.io/product-release/crypto-gem-sui-is-launching-a-new-altcoin-today-walrus-wal/]
- Jangka panjang: Insentif berlanjut via subsidies, namun skala adopsi storage riil belum terverifikasi di sumber publik (LOW)
- Dasar: Phase 7 Ecosystem (MEDIUM/LOW)

HARGA PASCA-DISTRIBUSI

Harga saat klaim: 0.5390 USD (2025-03-27) [KuCoin WAL-USDT daily candle close (hari TGE), https://www.kucoin.com/trade/WAL-USDT] (MEDIUM)
Harga +30 hari: 0.5356 USD (2025-04-26) [KuCoin WAL-USDT daily candle close, https://www.kucoin.com/trade/WAL-USDT] (MEDIUM)
Harga +90 hari: 0.4078 USD (2025-06-25) [KuCoin WAL-USDT daily candle close, https://www.kucoin.com/trade/WAL-USDT] (MEDIUM)
Harga puncak 12 bulan pertama: 0.9777 USD (2025-03-27) [KuCoin WAL-USDT TGE-day high; scan mingguan 12 bulan (Mar 2025-Mar 2026) tidak menemukan high lebih tinggi (tertinggi berikutnya 0.77822 minggu Mei 2025), https://www.kucoin.com/trade/WAL-USDT] (MEDIUM)

METRIK RETENSI

Perubahan aktivitas jaringan sebelum vs sesudah distribusi: Testnet bertrafik tinggi pra-launch (dorong komunitas Sui); pasca-TGE volume perdagangan hari pertama besar (setara ~$28,6 juta turnover di KuCoin) lalu menurun bertahap — angka aktivitas storage on-chain pre/post tidak dipublikasikan di sumber sekunder (MEDIUM) [KuCoin WAL-USDT, https://www.kucoin.com/trade/WAL-USDT]
Jumlah alamat pemegang token (unique holders): Tidak ditemukan (jumlah penerima airdrop tidak dipublikasikan resmi) (LOW)
Jumlah alamat aktif harian sebelum vs sesudah: Tidak ditemukan (tidak ada dashboard publik di sumber yang diakses) (LOW)
Konsentrasi kepemilikan: Tidak dapat dinilai dari sumber publik — alokasi 30% core contributors + 7% investor (keduanya locked) menyiratkan float awal terbatas (~690 juta dari reserve komunitas di launch) (MEDIUM) [Altcoin Buzz, https://www.altcoinbuzz.io/reviews/walrus-protocol-mainnet-and-tge-are-coming/]
Tingkat partisipasi staking: Tidak ditemukan (staking aktif namun tingkat partisipasi tidak dipublikasikan di sumber yang diakses) (LOW)

GAP YANG DIKETAHUI

Cohort penerima: memerlukan analisis on-chain per-alamat (persentase klaim & jual 7/30 hari pertama), tidak tersedia di sumber publik.
Jumlah wallet penerima airdrop tidak dipublikasikan resmi — klaim "salah satu yang terbesar" tidak terverifikasi kuantitatif.
Harga entry token sale investor tidak dipublikasikan — paper gain/loss VC tidak dapat dihitung pasti.

FARMING DAN SYBIL

Kriteria berbasis aktivitas testnet (menyimpan blob, staking, kampanye) dapat di-farm selama window testnet (Des 2024 – Mar 2025) yang diumumkan publik; tanpa disclosure mekanisme anti-sybil, multi-wallet farming mungkin terjadi — pola umum airdrop berbasis poin/kampanye era 2024-2025 (LOW) [Backpack Exchange, https://learn.backpack.exchange/articles/what-is-walrus-a-programmable-decentralized-storage-network]

PROSPEK

Metrik yang terpenuhi: Eksekusi TGE tepat jadwal; distribusi 4% pre-mainnet tersalurkan; ekonomi storage aktif (pembayaran + staking) (HIGH)
Metrik yang tidak terpenuhi: Retensi nilai token (-85% dalam 12 bulan); transparansi jumlah penerima dan jadwal unlock penuh (HIGH)
Sinyal ke depan: Unlock investor mulai ~Maret 2026 (12-bulan cliff); pertumbuhan permintaan storage riil (AI/data); efektivitas gelombang 6% post-mainnet (MEDIUM)
Penilaian: Airdrop WAL sukses secara operasional dan distribusi, namun tanpa penahan nilai (fee share/burn efektif) dan dengan unlock bertahun-tahun di depan, retensi harga bergantung penuh pada adopsi storage riil yang belum terbukti skala besar (MEDIUM)

PELAJARAN LINTAS PROJECT

Pemecahan airdrop menjadi pre/post-mainnet (4%/6%) mempertahankan insentif pasca-launch tetapi tidak menahan depresiasi ketika utilitas token belum menghasilkan permintaan organik — distribusi luas bukan pengganti value capture.
Token sale institusional besar ($140M) seminggu sebelum TGE memberi modal penuh namun menciptakan overhang unlock (cliff 12 bulan) yang jatuh bersamaan dengan harga yang sudah terdepresiasi — risiko struktural bagi VC.
Klaim skala ("airdrop terbesar") tanpa publikasi jumlah penerima melemahkan akuntabilitas — metrik distribusi seharusnya bagian dari disclosure TGE.

## Open Questions
- [foundation] Tanggal pasti testnet publik Desember 2024 (hari spesifik tidak dirinci sumber sekunder)
- [foundation] Alamat kontrak WAL di Sui secara eksplisit
- [foundation] Yurisdiksi legal Walrus Foundation
- [foundation] Rincian unlock 20% alokasi non-community/investor/contributor (kategori subsidies/foundation) — sumber sekunder tidak merinci penuh
- [entity] Daftar lengkap investor token sale $140M di luar lima nama yang terkonfirmasi (sumber menyebut "and other crypto-native VCs")
- [entity] Struktur hukum Walrus Foundation (yurisdiksi, board)
- [history] Tanggal persis testnet Desember 2024 dan detail milestone testnet per bulan
- [history] Jumlah wallet penerima airdrop WAL dan besaran per wallet (tidak dipublikasikan di sumber yang diakses)
- [history] Timeline lengkap unlock investor (12 bulan pasca-launch) dan core contributors
- [technology] Laporan audit keamanan pihak ketiga (ada/tidaknya dan auditor)
- [technology] Jumlah storage node aktif dan distribusi stake per epoch (dashboard resmi belum ditemukan di sumber sekunder)
- [technology] Spesifikasi teknis lengkap skema erasure coding ("Red Stuff") dari whitepaper/blog resmi
- [financial] Jumlah exact allocation dari treasury Mysten Labs yang dialokasikan khusus untuk pengembangan Walrus
- [financial] Status equity FTX Ventures pasca-bankruptcy dan apakah ada clawback/settlement
- [financial] Rincian tokenomics WAL: supply, alokasi, vesting schedule, mekanisme fee switch
- [financial] Tanggal mainnet launch resmi dan kapan revenue mulai di-generate
- [financial] Apakah Walrus Foundation sudah terbentuk secara legal dan struktur governance-nya
- [financial] Detail Sui Foundation grants yang spesifik untuk Walrus ecosystem builders
- [financial] Audit keamanan finansial/ekonomi token yang telah dilakukan
- [financial] Rencana decentralisasi treasury ke DAO/community
- [token] Alamat kontrak dan decimals WAL di Sui
- [token] Dokumen tokenomics resmi lengkap (breakdown 20% sisa, jadwal unlock contributors)
- [token] Jumlah wallet penerima airdrop dan distribusi per tier
- [token] Data holder concentration on-chain (top 10/100)
- [ecosystem] Exact list and count of current Walrus testnet storage node operators (permissioned set) — not publicly enumerated in detail
- [ecosystem] Wormhole integration technical specification and timeline — only announced, no detailed docs
- [ecosystem] Walrus Foundation legal formation status, jurisdiction, and initial board — announced as planned, no public filing
- [ecosystem] WAL token launch date, TGE mechanics, initial distribution, and whether any private/public sale occurred — no official announcement
- [ecosystem] Status of FTX Ventures equity in Mysten Labs post-bankruptcy — conflicting reports, no official settlement disclosure
- [ecosystem] Sui Foundation grant recipients specifically building on Walrus — no public dashboard filtering for Walrus-specific grants
- [ecosystem] Mainnet validator set requirements, staking mechanics, and slashing conditions for storage nodes — detailed specs not published
- [ecosystem] Walrus Sites custom domain integration status (beyond SNS) — documentation mentions planned, no timeline
- [ecosystem] Audit reports for Walrus core protocol, Seal integration, and Wormhole bridge contracts — not publicly released
- [ecosystem] Decentralization roadmap: timeline for permissionless storage node registration, governance parameter control transfer to DAO
- [market] Exact Walrus testnet storage node count and operator identities — not publicly enumerated; testnet is permissioned
- [market] Walrus testnet blob count, storage volume, bandwidth metrics — no public dashboard or transparency report
- [market] WAL token TGE date, initial circulating supply, launch mechanism (auction, LBP, public sale, airdrop) — no official announcement
- [market] Walrus mainnet launch date — not announced; dependent on testnet hardening and Sui governance
- [market] Wormhole integration technical specs, launch timeline, and whether WAL token needed for cross-chain fees — only announcement, no docs
- [market] Walrus Foundation legal formation, jurisdiction, initial treasury allocation — announced as planned, no public filing
- [market] FTX Ventures equity status in Mysten Labs post-bankruptcy — conflicting reports, no official settlement disclosure
- [market] Sui Foundation grant recipients specifically building on Walrus — no public dashboard filtering for Walrus-specific grants
- [market] Competitor benchmark: Walrus vs Filecoin/Arweave/0G on cost-per-GB, retrieval latency, durability guarantees — no independent third-party benchmarks published
- [market] Walrus Sites custom domain support (non-SNS) status and timeline — docs mention planned, no details
- [market] Audit reports for Walrus core protocol, Seal threshold encryption, Wormhole bridge contracts — not publicly released
- [market] Market size addressable: Developer demand for programmable storage on Sui vs general-purpose storage — no TAM/SAM analysis published
- [market] Whether Walrus will have native token incentives for storage nodes at mainnet launch (WAL staking, slashing) — tokenomics doc references but no final params
- [market] Exchange listing discussions / market maker arrangements for WAL — no public info
- [behavioral] Exact Walrus testnet storage node count, operator identities, dan geographic distribution — tidak public; testnet permissioned
- [behavioral] Walrus testnet blob count, storage volume (GB), bandwidth metrics, daily active users — tidak ada dashboard public
- [behavioral] WAL token TGE date, initial circulating supply, launch mechanism (auction/LBP/public sale/airdrop), vesting schedules — tidak diumumkan
- [behavioral] Walrus mainnet launch date — tidak diumumkan; dependent pada testnet hardening dan Sui governance
- [behavioral] Wormhole integration technical specifications, launch timeline, fee model, apakah WAL token required untuk cross-chain fees — hanya announcement, no docs
- [behavioral] Walrus Foundation legal formation status, jurisdiction, initial board, treasury allocation — diumumkan planned, no public filing
- [behavioral] Status equity FTX Ventures di Mysten Labs pasca-bankruptcy — laporan conflicting, no official settlement disclosure
- [behavioral] Sui Foundation grant recipients spesifik building on Walrus — no public dashboard filtering Walrus-specific grants
- [behavioral] Mainnet validator set requirements, staking mechanics, slashing conditions untuk storage nodes — detailed specs tidak dipublikasikan
- [behavioral] Walrus Sites custom domain support (non-SNS) status dan timeline — docs mention planned, no details
- [behavioral] Audit reports untuk Walrus core protocol, Seal threshold encryption, Wormhole bridge contracts — tidak public released
- [behavioral] Competitor benchmark independen: Walrus vs Filecoin/Arweave/0G pada cost-per-GB, retrieval latency, durability guarantees — tidak ada third-party benchmarks
- [behavioral] Apakah Walrus akan native token incentives untuk storage nodes di mainnet launch (WAL staking, slashing) — tokenomics doc reference tapi no final params
- [behavioral] Exchange listing discussions / market maker arrangements untuk WAL — no public info
- [behavioral] Allocation breakdown dari $428M Mysten Labs funding yang dialokasikan khusus Walrus development — tidak diungkap
- [knowledge] Exact Walrus testnet storage node count, operator identities, geographic distribution — tidak public; testnet permissioned【Phase 7 — Validator Group】【Phase 8 — Open Threads】
- [knowledge] Walrus testnet blob count, storage volume (GB), bandwidth, daily active users — tidak ada dashboard public【Phase 8 — Adoption Metrics】【Phase 8 — Open Threads】
- [knowledge] WAL token TGE date, initial circulating supply, launch mechanism, vesting schedules — tidak diumumkan【Phase 6 — Token】【Phase 8 — Open Threads】
- [knowledge] Walrus mainnet launch date — tidak diumumkan; dependent testnet hardening dan Sui governance【Phase 3 — Market Timeline】【Phase 8 — Open Threads】
- [knowledge] Wormhole integration technical specs, launch timeline, fee model, WAL token requirement cross-chain fees — hanya announcement, no docs【Phase 3 — Wormhole Announcement】【Phase 7 — Wormhole Integration】【Phase 8 — Open Threads】
- [knowledge] Walrus Foundation legal formation status, jurisdiction, initial board, treasury allocation — announced planned, no public filing【Phase 2 — Foundation】【Phase 8 — Open Threads】
- [knowledge] Status equity FTX Ventures di Mysten Labs pasca-bankruptcy — laporan conflicting, no official settlement disclosure【Phase 5 — Financial Risk】【Phase 8 — Open Threads】
- [knowledge] Sui Foundation grant recipients spesifik building on Walrus — no public dashboard filtering Walrus-specific grants【Phase 7 — Developer Ecosystem】【Phase 8 — Open Threads】
- [knowledge] Mainnet validator set requirements, staking mechanics, slashing conditions storage nodes — detailed specs tidak dipublikasikan【Phase 7 — Validator Group】【Phase 8 — Open Threads】
- [knowledge] Walrus Sites custom domain support (non-SNS) status dan timeline — docs mention planned, no details【Phase 7 — Major Integrations】【Phase 8 — Open Threads】
- [knowledge] Audit reports Walrus core protocol, Seal threshold encryption, Wormhole bridge contracts — tidak public released【Phase 4 — Security】【Phase 8 — Open Threads】
- [knowledge] Competitor benchmark independen: Walrus vs Filecoin/Arweave/0G cost-per-GB, retrieval latency, durability — tidak ada third-party benchmarks【Phase 8 — Competitor Landscape】【Phase 8 — Open Threads】
- [knowledge] Apakah Walrus native token incentives storage nodes mainnet launch (WAL staking, slashing) — tokenomics doc reference tapi no final params【Phase 6 — Token】【Phase 8 — Open Threads】
- [knowledge] Exchange listing discussions / market maker arrangements WAL — no public info【Phase 8 — Trading Markets】【Phase 8 — Open Threads】
- [knowledge] Allocation breakdown $428M Mysten Labs funding khusus Walrus development — tidak diungkap【Phase 5 — Funding History】【Phase 8 — Open Threads】
- [knowledge] Konflik interpretasi: Apakah fee-based model tanpa token incentives sustainable untuk DePIN storage node bootstrap jangka panjang? Evidence: Competitors semua gunakan token incentives【Phase 8 — Competitor Landscape】; Walrus fee-based planned【Phase 5 — Revenue Model】. Perlu validasi post-mainnet.
- [knowledge] Konflik interpretasi: Apakah centralized testnet 6-12+ bulan optimal untuk protocol hardening, atau terlalu lama menciptakan centralization debt? Evidence: Testnet permissioned extended【Phase 3 — Testnet Launch】; Competitors mainnet faster【Phase 8 — Competitor Landscape】. Trade-off belum terbukti.
- [conflict] Laporan audit keamanan pihak ketiga (ada/tidaknya)
- [conflict] Jumlah wallet penerima airdrop WAL dan distribusi per tier
- [conflict] Jadwal unlock lengkap investors (pasca cliff 12 bulan) dan core contributors
- [conflict] Spesifikasi lengkap skema erasure coding dari dokumen resmi
- [airdrop] Jumlah wallet penerima airdrop WAL per gelombang dan total klaim aktual
- [airdrop] Jadwal unlock lengkap investors pasca cliff dan core contributors
- [airdrop] Metrik permintaan storage riil (total blob tersimpan, revenue storage dalam WAL)
- [airdrop] Dampak unlock investor Maret 2026 terhadap harga dan governance
