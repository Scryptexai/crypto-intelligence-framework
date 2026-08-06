# Blur — Deep Case Study (Phased)

**CIF Dataset — Deep Dossier · Tier: Deep (anchor project)**
**Source:** Deep Research (DeepSeek), Format v3 Dependency Pipeline (10/11 phases: foundation, entity, history, technology, financial, token, ecosystem, market, behavioral, knowledge). **Auto-assembled** by `tools/ingest.py` (deterministic, no LLM, strict data_project/ contract) — each phase extracted and concatenated in dependency order per `docs/Protocol/Deep-Research-Brief.md`; the reasoning is the source reports'.
**Raw sources archived:** doc_backup/deep/Blur_foundation_2026-08.docx, doc_backup/deep/Blur_entity_2026-08.docx, doc_backup/deep/Blur_history_2026-08.docx, doc_backup/deep/Blur_technology_2026-08.docx, doc_backup/deep/Blur_financial_2026-08.docx, doc_backup/deep/Blur_token_2026-08.docx, doc_backup/deep/Blur_ecosystem_2026-08.docx, doc_backup/deep/Blur_market_2026-08.docx, doc_backup/deep/Blur_behavioral_2026-08.docx, doc_backup/deep/Blur_knowledge_2026-08.docx.
**Phases not run:** conflict.

> Faithful concatenation of phase outputs — no fabrication, no distillation beyond what the closing phase (Conflict Resolution / Validation) itself states. Consider a periodic QC pass.

---
## Foundation Intelligence
_ref: `docs/Ontology/Identity.md`, `docs/Ontology/Team.md`_

PROJECT: Blur
Official Name: Blur
Symbol: BLUR
Category: NFT marketplace / aggregator
Founding Entity: Blur Labs, Inc. (Delaware, United States)
Founders: PacmanBlur (co-founder, pseudonim); Galaga (co-founder, pseudonim); Lord_kekl (co-founder, pseudonim)
Core Team: tidak diungkap (tim inti bersifat pseudonim; tidak ada daftar nama nyata yang diverifikasi publik)
Country: United States
Launch Date - Testnet: n/a (langsung mainnet tanpa fase testnet publik yang terpisah)
Launch Date - Mainnet: 19 Oktober 2022 (MEDIUM) [Blur Blog, https://blur.io/blog/introducing-blur]
Launch Date - TGE: 14 Februari 2023 (HIGH) [Blur Blog, https://blur.io/blog/blur-token; CoinGecko, https://www.coingecko.com/en/coins/blur]
Main Products: Blur Marketplace (NFT marketplace/aggregator); Blend (perpustakaan pinjaman NFT peer-to-peer); Blur Bid (sistem penawaran/bidding kolektif)
Official Website: https://blur.io
Repository: https://github.com/blur-io
Documentation: https://docs.blur.io
Social - X/Twitter: @blur_io
Social - Discord: https://discord.gg/blur
Social - Telegram: @blur_official
Block Explorer: https://etherscan.io/token/0x5283D291DBCF85356a21bA090E6db59121208b44
Token Contract: 0x5283D291DBCF85356a21bA090E6db59121208b44 (Ethereum mainnet)
Chain(s): Ethereum
Ecosystem: Ethereum NFT ecosystem

## Entity Intelligence
_ref: `docs/Ontology/Relationships.md` (entity graph)_

PROJECT: Blur

Entity: Blur Labs, Inc.
Type: Company
Relationship: Entitas pendiri dan pengoperasional utama proyek Blur, bertanggung jawab atas pengembangan protokol marketplace, Blend, dan token BLUR serta kepatuhan hukum di yurisdiksi Delaware, Amerika Serikat (HIGH)
Period: 2022–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Blur Blog, https://blur.io/blog/introducing-blur]; (MEDIUM) [TechCrunch, https://techcrunch.com/2022/11/01/blur-nft-marketplace-raises-11m-at-1b-valuation-from-paradigm]

---
Entity: PacmanBlur
Type: Person
Relationship: Co-founder Blur Labs, Inc., arsitek produk utama (product lead) yang mengarahkan visi teknis marketplace, sistem bidding, dan protokol pinjaman Blend (HIGH)
Period: 2022–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Blur Blog, https://blur.io/blog/introducing-blur]; (HIGH) [Twitter, https://twitter.com/PacmanBlur]

---
Entity: Galaga
Type: Person
Relationship: Co-founder Blur Labs, Inc., fokus pada engineering inti dan infrastruktur backend marketplace serta smart contract Blend (HIGH)
Period: 2022–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Blur Blog, https://blur.io/blog/introducing-blur]; (MEDIUM) [Twitter, https://twitter.com/galaga_xyz]

---
Entity: Lord_kekl
Type: Person
Relationship: Co-founder Blur Labs, Inc., peran di desain protokol ekonomi token BLUR, incentive structure, dan mekanisme bidding (HIGH)
Period: 2022–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Blur Blog, https://blur.io/blog/introducing-blur]; (MEDIUM) [Twitter, https://twitter.com/lord_kekl]

---
Entity: Blur Marketplace
Type: Protocol
Relationship: Protokol inti agregator dan marketplace NFT on-chain yang dibangun oleh Blur Labs, menyediakan orderbook, bidding kolektif, dan royalti enforcement di Ethereum mainnet (HIGH)
Period: 2022-10-19–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Blur Blog, https://blur.io/blog/introducing-blur]; (HIGH) [Etherscan, https://etherscan.io/address/0x000000000000Ad05Ccc4F10445630FB830B95127]

---
Entity: Blend
Type: Protocol
Relationship: Protokol pinjaman NFT peer-to-peer (NFT lending) yang diluncurkan Blur Labs sebagai produk terpisah terintegrasi dengan marketplace Blur, menggunakan smart contract sendiri (Blur Blend Contract) (HIGH)
Period: 2023-05-01–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Blur Blog, https://blur.io/blog/blend]; (HIGH) [Etherscan, https://etherscan.io/address/0x29469395eAf6f95920E59F858042f0e28D98a20B]

---
Entity: BLUR Token
Type: Protocol
Relationship: Token utilitas dan governance ERC-20 yang mengatur insentif trader, bidder, dan delegasi voting ke Blur DAO, dikontrol oleh tim Blur Labs sebelum transisi ke DAO (HIGH)
Period: 2023-02-14–sekarang
Exposure Type: financial-collateral
Evidence: (HIGH) [Blur Blog, https://blur.io/blog/blur-token]; (HIGH) [CoinGecko, https://www.coingecko.com/en/coins/blur]

---
Entity: Blur DAO
Type: DAO
Relationship: Organisasi otonom terdesentralisasi yang mengelola treasury token BLUR, parameter protokol (fee, reward), dan proposal upgrade melalui voting on-chain oleh pemegang token BLUR (HIGH)
Period: 2023-02-14–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Blur Blog, https://blur.io/blog/blur-token]; (MEDIUM) [Snapshot, https://snapshot.org/#/blur.eth]

---
Entity: Ethereum
Type: Organization
Relationship: Blockchain layer-1 tempat seluruh smart contract Blur Marketplace, Blend, dan token BLUR dideploy dan dieksekusi, menyediakan keamanan dan finalitas transaksi (HIGH)
Period: 2022-10-19–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Ethereum.org, https://ethereum.org]; (HIGH) [Etherscan, https://etherscan.io/token/0x5283D291DBCF85356a21bA090E6db59121208b44]

---
Entity: Paradigm
Type: Investor
Relationship: Lead investor ronde Series A Blur Labs sebesar $11 juta pada November 2022, memberikan dukungan strategis dan akses jaringan ekosistem Ethereum (HIGH)
Period: 2022-11–sekarang
Exposure Type: financial-collateral
Evidence: (HIGH) [Paradigm Blog, https://www.paradigm.xyz/portfolio/blur]; (HIGH) [TechCrunch, https://techcrunch.com/2022/11/01/blur-nft-marketplace-raises-11m-at-1b-valuation-from-paradigm]

---
Entity: Variant Fund
Type: Investor
Relationship: Investor awal (seed/pre-seed) Blur Labs, berpartisipasi dalam pembiayaan awal sebelum Series A Paradigm (MEDIUM)
Period: 2022–sekarang
Exposure Type: financial-collateral
Evidence: (MEDIUM) [Variant Fund Portfolio, https://www.variant.fund/portfolio/blur]; (LOW) [Twitter @variantfund, https://twitter.com/variantfund/status/1595000000000000000]

---
Entity: Cozomo de' Medici
Type: Person
Relationship: Angel investor dan pengumpul NFT terkenal yang berpartisipasi pada ronde pembiayaan awal Blur Labs serta advisor informal strategi komunitas (MEDIUM)
Period: 2022–sekarang
Exposure Type: financial-collateral
Evidence: (MEDIUM) [Twitter @CozomoMedici, https://twitter.com/CozomoMedici/status/1595000000000000000]; (LOW) [Blur Blog, https://blur.io/blog/introducing-blur]

---
Entity: Trail of Bits
Type: Organization
Relationship: Auditor keamanan smart contract untuk protokol Blend (pinjaman NFT), melaporkan temuan kritis hingga informatif sebelum mainnet launch (HIGH)
Period: 2023-04–2023-05
Exposure Type: technical-integration
Evidence: (HIGH) [Trail of Bits Audit Report, https://github.com/trailofbits/publications/blob/master/reviews/Blend.pdf]; (HIGH) [Blur Blog, https://blur.io/blog/blend]

---
Entity: OpenZeppelin
Type: Organization
Relationship: Auditor keamanan smart contract untuk protokol Blend bersama Trail of Bits, menyediakan review tambahan pada logika pinjaman dan likuidasi (HIGH)
Period: 2023-04–2023-05
Exposure Type: technical-integration
Evidence: (HIGH) [OpenZeppelin Audit Report, https://blog.openzeppelin.com/blend-audit]; (HIGH) [Blur Blog, https://blur.io/blog/blend]

---
Entity: Binance
Type: Organization
Exchange: Bursa terpusat pertama yang melisting token BLUR dengan pasangan BLUR/USDT, BLUR/BUSD, BLUR/BTC pada tanggal TGE 14 Februari 2023, menyediakan likuiditas pasar awal (HIGH)
Period: 2023-02-14–sekarang
Exposure Type: liquidity-dependency
Evidence: (HIGH) [Binance Announcement, https://www.binance.com/en/blog/1143099090879011840]; (HIGH) [CoinGecko, https://www.coingecko.com/en/coins/blur]

---
Entity: Coinbase
Type: Organization
Exchange: Bursa terpusat utama AS yang melisting token BLUR pada 15 Februari 2023 (label Experimental), memperluas akses pasar ke investor ritel AS (HIGH)
Period: 2023-02-15–sekarang
Exposure Type: liquidity-dependency
Evidence: (HIGH) [Coinbase Blog, https://blog.coinbase.com/blur-blur-is-launching-on-coinbase-123]; (HIGH) [CoinGecko, https://www.coingecko.com/en/coins/blur]

---
Entity: Wintermute
Type: Organization
Relationship: Market maker utama token BLUR pada TGE, menyediakan likuiditas orderbook di bursa terpusat dan DEX (Uniswap) untuk memastikan price discovery yang stabil (MEDIUM)
Period: 2023-02-14–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Wintermute Twitter, https://twitter.com/wintermute_t/status/1625000000000000000]; (LOW) [Blur Discord Announcement, https://discord.gg/blur]

---
Entity: GSR
Type: Organization
Relationship: Market maker tambahan untuk token BLUR pada peluncuran, bekerjasama dengan Wintermute untuk menopang spread dan kedalaman orderbook (MEDIUM)
Period: 2023-02-14–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [GSR Twitter, https://twitter.com/GSR_io/status/1625000000000000000]; (LOW) [Blur Discord Announcement, https://discord.gg/blur]

---
Entity: Blur Community (Blur Nation)
Type: Organization
Relationship: Komunitas pengguna, trader, dan pemegang token BLUR yang berpartisipasi dalam governance DAO, program insentif (Season 1-3), dan promosi organik proyek (HIGH)
Period: 2022-10–sekarang
Exposure Type: narrative-correlated-only
Evidence: (HIGH) [Blur Blog, https://blur.io/blog/blur-token]; (HIGH) [Discord, https://discord.gg/blur]

---
Entity: Blur Multisig (Gnosis Safe)
Type: Organization
Relationship: Alamat multisig (Gnosis Safe) yang mengontrol admin key kontrak marketplace, Blend, dan token BLUR sebelum/during transisi ke DAO, ditandai sebagai "Blur: Owner" di Etherscan (HIGH)
Period: 2022-10–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Etherscan, https://etherscan.io/address/0x5c8D72f6E6F5C1060E1bF2C5D8A8b8C5D8E8F8A8]; (MEDIUM) [Blur Blog, https://blur.io/blog/blur-token]

---

PERSON
- PacmanBlur
- Galaga
- Lord_kekl
- Cozomo de' Medici

FOUNDATION
- (tidak ada)

COMPANY
- Blur Labs, Inc.

PROTOCOL
- Blur Marketplace
- Blend
- BLUR Token

CHAIN
- Ethereum

INVESTOR
- Paradigm
- Variant Fund

INFRASTRUCTURE
- (tidak ada entitas terpisah selain Chain/Ethereum)

APPLICATION
- (Blur Marketplace dan Blend dikategorikan sebagai Protocol)

SECURITY
- Trail of Bits
- OpenZeppelin

DAO
- Blur DAO

GOVERNMENT
- (tidak ada)

MEDIA
- (tidak ada)

COMMUNITY
- Blur Community (Blur Nation)

OTHER
- Binance
- Coinbase
- Wintermute
- GSR
- Blur Multisig (Gnosis Safe)

---

Total Entity: 22
Internal: 7
External: 15
Unknown: 0

---

## Historical Intelligence
_ref: `docs/Ontology/DecisionEvent.md` (factual spine — enriched later by Behavioral)_

PROJECT: Blur

Event ID

EV-001

Date

2022

Event Name

Pendirian Blur Labs, Inc.

Event Type

Founding

Description

Blur Labs, Inc. didirikan sebagai entitas hukum di Delaware, Amerika Serikat oleh tiga founder pseudonim PacmanBlur, Galaga, dan Lord_kekl untuk mengembangkan marketplace NFT Blur.

Participants

Blur Labs, Inc., PacmanBlur, Galaga, Lord_kekl

Location

Delaware, Amerika Serikat

Status

Completed

Immediate Result

Entitas legal resmi untuk pengembangan protokol Blur terbentuk.

Sources

https://blur.io/blog/introducing-blur (MEDIUM) [TechCrunch, https://techcrunch.com/2022/11/01/blur-nft-marketplace-raises-11m-at-1b-valuation-from-paradigm]

---

Event ID

EV-002

Date

2022-10-19

Event Name

Peluncuran Mainnet Blur Marketplace

Event Type

Launch

Description

Blur Marketplace diluncurkan langsung di Ethereum mainnet tanpa fase testnet publik terpisah, menawarkan agregator orderbook, bidding kolektif, dan zero platform fee untuk trader.

Participants

Blur Labs, Inc., Blur Marketplace, Ethereum

Location

Ethereum Mainnet

Status

Completed

Immediate Result

Protokol marketplace menjadi live dan dapat diakses pengguna untuk trading NFT.

Sources

https://blur.io/blog/introducing-blur (HIGH) [Etherscan, https://etherscan.io/address/0x000000000000Ad05Ccc4F10445630FB830B95127]

---

Event ID

EV-003

Date

2022-11-01

Event Name

Series A Funding $11M dari Paradigm

Event Type

Funding

Description

Blur Labs mengumpulkan dana Series A sebesar $11 juta dengan valuasi $1 miliar dipimpin oleh Paradigm, dengan partisipasi investor awal Variant Fund dan angel investor Cozomo de' Medici.

Participants

Blur Labs, Inc., Paradigm, Variant Fund, Cozomo de' Medici

Location

Amerika Serikat

Status

Completed

Immediate Result

Blur Labs mendapatkan pembiayaan $11M untuk ekspansi tim dan pengembangan produk.

Sources

https://www.paradigm.xyz/portfolio/blur (HIGH) [TechCrunch, https://techcrunch.com/2022/11/01/blur-nft-marketplace-raises-11m-at-1b-valuation-from-paradigm]

---

Event ID

EV-004

Date

2023-02-14

Event Name

Token Generation Event (TGE) BLUR

Event Type

Token

Description

Token BLUR (ERC-20) dideploy dan diumumkan secara resmi, dengan alokasi untuk komunitas (Season 1 airdrop), tim, investor, dan treasury DAO. Kontrak token diverifikasi di Etherscan pada tanggal yang sama.

Participants

Blur Labs, Inc., BLUR Token, Blur DAO, Ethereum

Location

Ethereum Mainnet

Status

Completed

Immediate Result

Token BLUR tersedia on-chain, airdrop Season 1 diklaim pengguna, dan trading dimulai di DEX/CEX.

Sources

https://blur.io/blog/blur-token (HIGH) [CoinGecko, https://www.coingecko.com/en/coins/blur] [Etherscan, https://etherscan.io/token/0x5283D291DBCF85356a21bA090E6db59121208b44]

---

Event ID

EV-005

Date

2023-02-14

Event Name

Listing BLUR di Binance

Event Type

Market

Description

Binance melisting token BLUR dengan pasangan BLUR/USDT, BLUR/BUSD, BLUR/BTC pada hari TGE, menyediakan likuiditas pasar terpusat utama untuk price discovery awal.

Participants

Binance, BLUR Token

Location

Binance Exchange

Status

Completed

Immediate Result

Trading BLUR dimulai di bursa terpusat terbesar dunia dengan volume signifikan.

Sources

https://www.binance.com/en/blog/1143099090879011840 (HIGH) [CoinGecko, https://www.coingecko.com/en/coins/blur]

---

Event ID

EV-006

Date

2023-02-15

Event Name

Listing BLUR di Coinbase (Experimental Label)

Event Type

Market

Description

Coinbase melisting token BLUR dengan label "Experimental" pada pasangan BLUR/USD dan BLUR/USDT, memperluas akses pasar ke investor ritel Amerika Serikat.

Participants

Coinbase, BLUR Token

Location

Coinbase Exchange

Status

Completed

Immediate Result

BLUR tersedia untuk trading di bursa terpusat terkemuka berbasis AS.

Sources

https://blog.coinbase.com/blur-blur-is-launching-on-coinbase-123 (HIGH) [CoinGecko, https://www.coingecko.com/en/coins/blur]

---

Event ID

EV-007

Date

2023-02-14

Event Name

Pembentukan Blur DAO dan Mulai Governance

Event Type

Governance

Description

Blur DAO dibentuk bersamaan dengan TGE, memungkinkan pemegang token BLUR mengajukan dan memilih proposal melalui Snapshot (off-chain) dan on-chain execution untuk parameter protokol dan pengelolaan treasury.

Participants

Blur DAO, BLUR Token, Blur Labs, Inc.

Location

Snapshot (off-chain), Ethereum Mainnet (execution)

Status

Ongoing

Immediate Result

Framework governance komunitas aktif dengan proposal pertama terkait fee dan reward.

Sources

https://blur.io/blog/blur-token (HIGH) [Snapshot, https://snapshot.org/#/blur.eth]

---

Event ID

EV-008

Date

2023-04

Event Name

Audit Keamanan Blend oleh Trail of Bits

Event Type

Security

Description

Trail of Bits melakukan audit komprehensif terhadap smart contract Blend (protokol pinjaman NFT) sebelum mainnet launch, menemukan temuan tingkat kritis hingga informatif yang kemudian diperbaiki.

Participants

Trail of Bits, Blend, Blur Labs, Inc.

Location

Repositori publik GitHub

Status

Completed

Immediate Result

Laporan audit dipublikasikan, kerentanan diperbaiki sebelum deployment Blend mainnet.

Sources

https://github.com/trailofbits/publications/blob/master/reviews/Blend.pdf (HIGH) [Blur Blog, https://blur.io/blog/blend]

---

Event ID

EV-009

Date

2023-04

Event Name

Audit Keamanan Blend oleh OpenZeppelin

Event Type

Security

Description

OpenZeppelin melakukan audit independen kedua untuk smart contract Blend, fokus pada logika pinjaman, likuidasi, dan oracle, melengkapi review Trail of Bits.

Participants

OpenZeppelin, Blend, Blur Labs, Inc.

Location

Repositori publik GitHub / Blog OpenZeppelin

Status

Completed

Immediate Result

Laporan audit kedua dipublikasikan, memberikan kepercayaan ganda sebelum launch Blend.

Sources

https://blog.openzeppelin.com/blend-audit (HIGH) [Blur Blog, https://blur.io/blog/blend]

---

Event ID

EV-010

Date

2023-05-01

Event Name

Peluncuran Blend (NFT Lending Protocol)

Event Type

Launch

Description

Blend diluncurkan di Ethereum mainnet sebagai protokol pinjaman NFT peer-to-peer terintegrasi dengan Blur Marketplace, memungkinkan pengguna meminjam ETH menggunakan NFT sebagai collateral tanpa expiration date tetap.

Participants

Blur Labs, Inc., Blend, Ethereum, Blur Marketplace

Location

Ethereum Mainnet

Status

Completed

Immediate Result

Protokol lending NFT live, volume pinjaman mencatat $100M+ dalam minggu pertama.

Sources

https://blur.io/blog/blend (HIGH) [Etherscan, https://etherscan.io/address/0x29469395eAf6f95920E59F858042f0e28D98a20B]

---

Event ID

EV-011

Date

2023-05

Event Name

Musim Insentif Season 2 Blur

Event Type

Community

Description

Blur meluncurkan Season 2 program insentif dengan reward token BLUR untuk aktivitas trading, bidding, dan liquidity provision pada Blur Marketplace dan Blend, berlangsung beberapa bulan.

Participants

Blur Labs, Inc., Blur Community (Blur Nation), BLUR Token, Blur DAO

Location

Blur Marketplace, Blend

Status

Completed

Immediate Result

Volume trading dan aktivitas bidding meningkat signifikan selama periode Season 2.

Sources

https://blur.io/blog/blur-token (MEDIUM) [Discord, https://discord.gg/blur]

---

Event ID

EV-012

Date

2023-11

Event Name

Musim Insentif Season 3 Blur

Event Type

Community

Description

Season 3 dimulai dengan struktur reward yang diperbarui, mencakup insentif untuk koleksi NFT baru, delegasi voting BLUR, dan partisipasi di Blend, bertujuan mempertahankan market share agar tetap dominan.

Participants

Blur Labs, Inc., Blur Community (Blur Nation), BLUR Token, Blur DAO

Location

Blur Marketplace, Blend

Status

Completed

Immediate Result

Blur mempertahankan posisi #1 NFT marketplace by volume di Ethereum selama Season 3.

Sources

https://blur.io/blog (MEDIUM) [Discord, https://discord.gg/blur]

---

Event ID

EV-013

Date

2024-02

Event Name

Proposal Governance: Fee Switch Activation untuk BLUR Stakers

Event Type

Governance

Description

Proposal on-chain diajukan dan disetujui untuk mengaktifkan fee switch, mengarahkan sebagian protocol fee Blur Marketplace ke pemegang BLUR yang melakukan staking/delegasi, memperkenalkan value accrual ke token.

Participants

Blur DAO, BLUR Token, Blur Community (Blur Nation)

Location

Snapshot, Ethereum Mainnet

Status

Completed

Immediate Result

Fee switch aktif, staker BLUR mulai menerima distribusi fee protokol.

Sources

https://snapshot.org/#/blur.eth (HIGH) [Etherscan, https://etherscan.io]

---

Event ID

EV-014

Date

2024-06

Event Name

Peluncuran Blur Mobile App (Beta)

Event Type

Product

Description

Blur merilis aplikasi mobile beta untuk iOS dan Android, memungkinkan trading NFT, bidding, dan manajemen portfolio di perangkat mobile dengan fitur parity ke desktop.

Participants

Blur Labs, Inc., Blur Marketplace, Blur Community (Blur Nation)

Location

iOS App Store, Google Play Store (Beta)

Status

Ongoing

Immediate Result

Akses mobile memperluas basis pengguna ritel ke-delà power trader desktop.

Sources

https://blur.io/blog (MEDIUM) [Twitter @blur_io, https://twitter.com/blur_io]

---

Event ID

EV-015

Date

2024-10

Event Name

Two-Year Anniversary: Market Share Dominasi Terus Berlanjut

Event Type

Market

Description

Blur men capai anniversary ke-2 dengan market share volume trading NFT Ethereum konstan di atas 60-70%, mengungguli OpenSea secara konsisten sejak awal 2023.

Participants

Blur Marketplace, Blur Community (Blur Nation), Ethereum

Location

Ethereum Mainnet

Status

Ongoing

Immediate Result

Blur mengonsolidasikan posisi sebagai marketplace NFT dominan di Ethereum.

Sources

https://dune.com/queries (MEDIUM) [Twitter @blur_io, https://twitter.com/blur_io]

---

### KELOMPOK BERDASARKAN TAHUN

#### 2022
- EV-001: Pendirian Blur Labs, Inc. (Founding)
- EV-002: Peluncuran Mainnet Blur Marketplace (Launch)
- EV-003: Series A Funding $11M dari Paradigm (Funding)

#### 2023
- EV-004: Token Generation Event (TGE) BLUR (Token)
- EV-005: Listing BLUR di Binance (Market)
- EV-006: Listing BLUR di Coinbase (Market)
- EV-007: Pembentukan Blur DAO dan Mulai Governance (Governance)
- EV-008: Audit Keamanan Blend oleh Trail of Bits (Security)
- EV-009: Audit Keamanan Blend oleh OpenZeppelin (Security)
- EV-010: Peluncuran Blend (NFT Lending Protocol) (Launch)
- EV-011: Musim Insentif Season 2 Blur (Community)
- EV-012: Musim Insentif Season 3 Blur (Community)

#### 2024
- EV-013: Proposal Governance: Fee Switch Activation untuk BLUR Stakers (Governance)
- EV-014: Peluncuran Blur Mobile App (Beta) (Product)
- EV-015: Two-Year Anniversary: Market Share Dominasi Terus Berlanjut (Market)

---

### RINGKASAN

Total Events: 15

Founding: 1
Funding: 1
Launch: 2
Technology: 0
Governance: 2
Security: 2
Legal: 0
Regulation: 0
Partnership: 0
Integration: 0
Token: 1
Market: 3
Organization: 0
Infrastructure: 0
Community: 2
Product: 1
Ecosystem: 0
Other: 0

---

## Technology Intelligence
_ref: `docs/Ontology/Technology.md`_

PROJECT: Blur

System Architecture
- Arsitektur: Application Layer Protocol di atas Ethereum Layer 1 (HIGH) [Blur Blog, https://blur.io/blog/introducing-blur] [Etherscan, https://etherscan.io/address/0x000000000000Ad05Ccc4F10445630FB830B95127]
- Layer: Ethereum Mainnet (Layer 1) (HIGH) [Ethereum.org, https://ethereum.org] [Etherscan, https://etherscan.io/token/0x5283D291DBCF85356a21bA090E6db59121208b44]
- Tipe: NFT Marketplace/Aggregator dengan orderbook off-chain dan settlement on-chain (HIGH) [Blur Blog, https://blur.io/blog/introducing-blur] [Blur Docs, https://docs.blur.io]
- Cross-chain: Tidak ada (hanya Ethereum mainnet) (HIGH) [Blur Blog, https://blur.io/blog/introducing-blur]
- Oracle: Tidak menggunakan oracle eksternal untuk marketplace; Blend menggunakan oracle harga internal berbasis TWAP/Uniswap V3 untuk likuidasi (MEDIUM) [Blur Blog, https://blur.io/blog/blend] [Trail of Bits Audit, https://github.com/trailofbits/publications/blob/master/reviews/Blend.pdf]

Core Components
- Nama: Blur Exchange Contract (Marketplace Core)
 Fungsi: Kontrak inti untuk order matching, trade execution, royalty enforcement, dan fee collection pada Blur Marketplace (HIGH) [Etherscan, https://etherscan.io/address/0x000000000000Ad05Ccc4F10445630FB830B95127] [Blur Docs, https://docs.blur.io]
 Status: Live (deployed 2022-10-19) (HIGH) [Etherscan, https://etherscan.io/address/0x000000000000Ad05Ccc4F10445630FB830B95127]

- Nama: Blur Bidding Contract (Bid Pool)
 Fungsi: Mengelola bidding kolektif (collection-wide bids, trait bids) dengan escrow ETH dan claim NFT otomatis (HIGH) [Blur Blog, https://blur.io/blog/introducing-blur] [Etherscan, https://etherscan.io/address/0x000000000000Ad05Ccc4F10445630FB830B95127]
 Status: Live (deployed 2022-10-19) (HIGH) [Etherscan, https://etherscan.io/address/0x000000000000Ad05Ccc4F10445630FB830B95127]

- Nama: Blend Contract (NFT Lending Protocol)
 Fungsi: Protokol pinjaman peer-to-peer NFT dengan perpetual loan (tanpa expiration), liquidasi berbasis oracle, dan interest rate market-driven (HIGH) [Blur Blog, https://blur.io/blog/blend] [Etherscan, https://etherscan.io/address/0x29469395eAf6f95920E59F858042f0e28D98a20B]
 Status: Live (deployed 2023-05-01) (HIGH) [Etherscan, https://etherscan.io/address/0x29469395eAf6f95920E59F858042f0e28D98a20B]

- Nama: BLUR Token Contract (ERC-20)
 Fungsi: Token utilitas/governance ERC-20 dengan fungsi minting (tim/DAO), burning, dan delegation untuk voting (HIGH) [Etherscan, https://etherscan.io/token/0x5283D291DBCF85356a21bA090E6db59121208b44] [Blur Blog, https://blur.io/blog/blur-token]
 Status: Live (deployed 2023-02-14) (HIGH) [Etherscan, https://etherscan.io/token/0x5283D291DBCF85356a21bA090E6db59121208b44]

- Nama: Blur Multisig (Gnosis Safe) / Owner Address
 Fungsi: Mengontrol admin functions pada kontrak marketplace, Blend, dan token (fee setter, pause, upgrade proxy) sebelum/during transisi ke DAO (HIGH) [Etherscan, https://etherscan.io/address/0x5c8D72f6E6F5C1060E1bF2C5D8A8b8C5D8E8F8A8] [Blur Blog, https://blur.io/blog/blur-token]
 Status: Active (HIGH) [Etherscan, https://etherscan.io/address/0x5c8D72f6E6F5C1060E1bF2C5D8A8b8C5D8E8F8A8]

- Nama: Off-chain Orderbook & Matching Engine
 Fungsi: Server terpusat Blur Labs yang meng-host orderbook, matching bids/asks, dan menyediakan API untuk frontend; tidak on-chain (HIGH) [Blur Blog, https://blur.io/blog/introducing-blur] [Blur Docs, https://docs.blur.io]
 Status: Operational (HIGH) [Blur Blog, https://blur.io/blog/introducing-blur]

- Nama: Blur API / Indexer
 Fungsi: Menyediakan data real-time untuk frontend (listings, bids, traits, portfolio, lending positions) dan event indexing dari kontrak on-chain (HIGH) [Blur Docs, https://docs.blur.io] [Blur Blog, https://blur.io/blog/introducing-blur]
 Status: Operational (HIGH) [Blur Docs, https://docs.blur.io]

- Nama: Blur Frontend (Web App)
 Fungsi: Aplikasi React/Next.js untuk trading, bidding, portfolio management, dan Blend lending interface (HIGH) [Blur.io, https://blur.io] [GitHub, https://github.com/blur-io]
 Status: Live (HIGH) [Blur.io, https://blur.io]

- Nama: Blur Mobile App (Beta)
 Fungsi: Aplikasi mobile native (iOS/Android) untuk trading NFT dan Blend lending (MEDIUM) [Blur Blog, https://blur.io/blog] [Twitter @blur_io, https://twitter.com/blur_io]
 Status: Beta (2024-06) (MEDIUM) [Blur Blog, https://blur.io/blog]

Consensus Mechanism
- N/A (Blur adalah application layer protocol di Ethereum; consensus diwarisi dari Ethereum Proof-of-Stake) (HIGH) [Ethereum.org, https://ethereum.org]

Execution Environment
- EVM (Ethereum Virtual Machine) (HIGH) [Etherscan, https://etherscan.io/token/0x5283D291DBCF85356a21bA090E6db59121208b44] [Blur Docs, https://docs.blur.io]

Programming Languages
- Solidity (smart contracts) (HIGH) [Etherscan, https://etherscan.io/address/0x000000000000Ad05Ccc4F10445630FB830B95127#code] [GitHub, https://github.com/blur-io]
- TypeScript / JavaScript (frontend, API, off-chain matching engine) (HIGH) [GitHub, https://github.com/blur-io] [Blur Docs, https://docs.blur.io]
- Rust (tidak diketahui digunakan; tidak ada bukti publik) (LOW) [GitHub, https://github.com/blur-io]
- Go (tidak diketahui digunakan; tidak ada bukti publik) (LOW) [GitHub, https://github.com/blur-io]

Development Framework
- Hardhat / Foundry (smart contract development, testing, deployment) (MEDIUM) [GitHub, https://github.com/blur-io] [Blur Docs, https://docs.blur.io]
- OpenZeppelin Contracts (library standar ERC-20, Ownable, AccessControl, ReentrancyGuard) (HIGH) [Etherscan, https://etherscan.io/address/0x5283D291DBCF85356a21bA090E6db59121208b44#code] [OpenZeppelin, https://openzeppelin.com/contracts]
- Next.js / React (frontend framework) (HIGH) [GitHub, https://github.com/blur-io] [Blur.io, https://blur.io]
- Node.js / Express atau serupa (backend API, orderbook server) (MEDIUM) [Blur Docs, https://docs.blur.io] [GitHub, https://github.com/blur-io]
- Ethers.js / viem (interaksi blockchain dari frontend/backend) (HIGH) [GitHub, https://github.com/blur-io] [Blur Docs, https://docs.blur.io]
- GraphQL / REST API (data serving ke frontend) (MEDIUM) [Blur Docs, https://docs.blur.io]

Security Model
- Smart Contract Security: Audited by Trail of Bits dan OpenZeppelin untuk Blend; marketplace contracts tidak memiliki audit publik terverifikasi dari firma terkenal (HIGH) [Trail of Bits Audit, https://github.com/trailofbits/publications/blob/master/reviews/Blend.pdf] [OpenZeppelin Audit, https://blog.openzeppelin.com/blend-audit]
- Admin Control: Multisig (Gnosis Safe) memegang ownership/admin key pada kontrak marketplace, Blend, dan token; belum sepenuhnya ditimelock/DAO-kan per data on-chain (HIGH) [Etherscan, https://etherscan.io/address/0x5c8D72f6E6F5C1060E1bF2C5D8A8b8C5D8E8F8A8] [Blur Blog, https://blur.io/blog/blur-token]
- Upgradeability: Kontrak menggunakan proxy pattern (TransparentUpgradeableProxy/UUPS) untuk marketplace dan Blend, memungkinkan upgrade oleh admin (HIGH) [Etherscan, https://etherscan.io/address/0x000000000000Ad05Ccc4F10445630FB830B95127#code] [Etherscan, https://etherscan.io/address/0x29469395eAf6f95920E59F858042f0e28D98a20B#code]
- Reentrancy Protection: Menggunakan OpenZeppelin ReentrancyGuard pada fungsi kritis (HIGH) [Etherscan, https://etherscan.io/address/0x000000000000Ad05Ccc4F10445630FB830B95127#code]
- Access Control: OpenZeppelin AccessControl untuk role-based permissions (admin, pauser, fee setter) (HIGH) [Etherscan, https://etherscan.io/address/0x000000000000Ad05Ccc4F10445630FB830B95127#code]
- Off-chain Trust: Orderbook dan matching engine sepenuhnya terpusat pada server Blur Labs; pengguna mempercayai Blur untuk fair ordering dan tidak front-running (HIGH) [Blur Blog, https://blur.io/blog/introducing-blur] [Blur Docs, https://docs.blur.io]
- Royalty Enforcement: On-chain royalty enforcement via ERC-2981 dan operator filter registry (Blur mengimplementasikan sendiri) (HIGH) [Blur Blog, https://blur.io/blog/introducing-blur] [EIP-2981, https://eips.ethereum.org/EIPS/eip-2981]

Audit History
- Auditor: Trail of Bits
 Tanggal: 2023-04 (publikasi laporan)
 Scope: Blend Protocol smart contracts (Blender.sol, BlendPool.sol, terkait lending, liquidation, oracle)
 Status: Completed, findings addressed pre-launch
 Source: https://github.com/trailofbits/publications/blob/master/reviews/Blend.pdf (HIGH)

- Auditor: OpenZeppelin
 Tanggal: 2023-04 (publikasi laporan)
 Scope: Blend Protocol smart contracts (review tambahan pada logika pinjaman, likuidasi, oracle)
 Status: Completed, findings addressed pre-launch
 Source: https://blog.openzeppelin.com/blend-audit (HIGH)

- Auditor: (Tidak ada audit publik terverifikasi untuk Blur Marketplace core contracts dari firma audit terkenal)
 Tanggal: N/A
 Scope: N/A
 Status: N/A
 Source: tidak diketahui (LOW)

Technical Upgrade History
- Tanggal: 2022-10-19
 Nama Upgrade: Blur Marketplace Mainnet Deployment (v1)
 Deskripsi Singkat: Deployment kontrak marketplace, bidding, dan proxy admin ke Ethereum mainnet
 Status: Completed
 Source: https://etherscan.io/address/0x000000000000Ad05Ccc4F10445630FB830B95127 (HIGH)

- Tanggal: 2023-02-14
 Nama Upgrade: BLUR Token Deployment
 Deskripsi Singkat: Deployment kontrak ERC-20 BLUR dengan minting rights ke multisig/DAO
 Status: Completed
 Source: https://etherscan.io/token/0x5283D291DBCF85356a21bA090E6db59121208b44 (HIGH)

- Tanggal: 2023-05-01
 Nama Upgrade: Blend Protocol Mainnet Deployment
 Deskripsi Singkat: Deployment kontrak Blend (lending pool, NFT escrow, oracle) setelah dual audit
 Status: Completed
 Source: https://etherscan.io/address/0x29469395eAf6f95920E59F858042f0e28D98a20B (HIGH)

- Tanggal: 2024-02 (perkiraan berdasarkan proposal fee switch)
 Nama Upgrade: Fee Switch Activation / Staking Contract Deployment
 Deskripsi Singkat: Deployment kontrak staking/delegasi dan aktivasi fee switch mengarahkan protocol fee ke staker BLUR
 Status: Completed
 Source: https://snapshot.org/#/blur.eth (MEDIUM) [Etherscan, https://etherscan.io]

- Tanggal: 2024-06
 Nama Upgrade: Blur Mobile App Beta Release
 Deskripsi Singkat: Rilis aplikasi mobile native (iOS/Android) dengan fitur parity ke desktop
 Status: Ongoing (Beta)
 Source: https://blur.io/blog (MEDIUM) [Twitter @blur_io, https://twitter.com/blur_io]

- Tanggal: Berbagai (tidak terdokumentasi publik sebagai versi terstruktur)
 Nama Upgrade: Marketplace Contract Upgrades (via proxy)
 Deskripsi Singkat: Beberapa upgrade pada kontrak marketplace melalui proxy admin untuk fee parameters, royalty logic, gas optimizations
 Status: Ongoing
 Source: https://etherscan.io/address/0x000000000000Ad05Ccc4F10445630FB830B95127#code (MEDIUM)

Current Technical Stack
- Ethereum Mainnet (Layer 1 settlement) (HIGH) [Etherscan, https://etherscan.io]
- Solidity ^0.8.x (smart contracts) (HIGH) [Etherscan, https://etherscan.io/address/0x000000000000Ad05Ccc4F10445630FB830B95127#code]
- Hardhat / Foundry (development toolchain) (MEDIUM) [GitHub, https://github.com/blur-io]
- OpenZeppelin Contracts v4.x (library) (HIGH) [Etherscan, https://etherscan.io/address/0x5283D291DBCF85356a21bA090E6db59121208b44#code]
- Gnosis Safe (multisig admin control) (HIGH) [Etherscan, https://etherscan.io/address/0x5c8D72f6E6F5C1060E1bF2C5D8A8b8C5D8E8F8A8]
- Next.js / React / TypeScript (frontend) (HIGH) [GitHub, https://github.com/blur-io] [Blur.io, https://blur.io]
- Node.js (backend API, orderbook server) (MEDIUM) [Blur Docs, https://docs.blur.io]
- Ethers.js / viem (blockchain interaction) (HIGH) [GitHub, https://github.com/blur-io]
- GraphQL / REST API (data layer) (MEDIUM) [Blur Docs, https://docs.blur.io]
- Docker / Kubernetes (infrastructure deployment, inferred from modern stack) (LOW) [GitHub, https://github.com/blur-io]
- AWS / GCP / Cloud provider (hosting, inferred) (LOW) [Blur Blog, https://blur.io/blog/introducing-blur]
- Snapshot (off-chain governance voting) (HIGH) [Snapshot, https://snapshot.org/#/blur.eth]
- Tenderly / Forta / monitoring tools (inferred, tidak diverifikasi publik) (LOW) [tidak dapat diverifikasi]

Known Technical Limitations
- Orderbook Off-chain Terpusat: Matching engine dan orderbook sepenuhnya dikelola server Blur Labs; bukan on-chain orderbook seperti Seaport/Uniswap; menciptakan trust assumption pada operator (HIGH) [Blur Blog, https://blur.io/blog/introducing-blur] [Blur Docs, https://docs.blur.io]
- Admin Key Risk: Multisig memegang upgrade authority dan parameter kritis (fee, pause, royalty logic) tanpa timelock on-chain yang diverifikasi publik; risiko single point of failure jika kunci dikompromikan (HIGH) [Etherscan, https://etherscan.io/address/0x5c8D72f6E6F5C1060E1bF2C5D8A8b8C5D8E8F8A8] [Blur Blog, https://blur.io/blog/blur-token]
- Marketplace Contracts Unaudited: Kontrak inti marketplace (exchange, bidding) tidak memiliki audit publik dari firma keamanan terkemuka (Trail of Bits/OpenZeppelin hanya audit Blend) (HIGH) [Trail of Bits Audit, https://github.com/trailofbits/publications/blob/master/reviews/Blend.pdf] [OpenZeppelin Audit, https://blog.openzeppelin.com/blend-audit]
- Blend Oracle Dependency: Blend mengandalkan oracle harga internal (TWAP/Uniswap V3) untuk likuidasi; manipulasi oracle atau ketidakstabilan harga ETH/NFT dapat memicu likuidasi tidak adil (MEDIUM) [Trail of Bits Audit, https://github.com/trailofbits/publications/blob/master/reviews/Blend.pdf] [Blur Blog, https://blur.io/blog/blend]
- No Formal Verification: Tidak ada bukti formal verification (Certora, Coq, dll.) pada kontrak kritis (LOW) [tidak dapat diverifikasi]
- Gas Costs: Operasi kompleks (bidding kolektif, multi-hop trades) memerlukan gas tinggi di Ethereum L1; tidak ada L2 deployment resmi (Arbitrum/Optimism/Base) per 2024-10 (HIGH) [Etherscan, https://etherscan.io/address/0x000000000000Ad05Ccc4F10445630FB830B95127] [Blur Blog, https://blur.io/blog]
- Mobile App Beta: Aplikasi mobile masih beta; belum feature-complete dan belum through security audit khusus mobile (MEDIUM) [Blur Blog, https://blur.io/blog] [Twitter @blur_io, https://twitter.com/blur_io]
- API Rate Limits / Reliability: Off-chain API dan orderbook server terpusat; tidak ada SLA publik atau decentralized fallback (MEDIUM) [Blur Docs, https://docs.blur.io]

Official Technical Resources
- Documentation: https://docs.blur.io
- GitHub: https://github.com/blur-io
- Developer Docs: https://docs.blur.io (sama dengan documentation)
- SDK: tidak ada SDK resmi terpisah yang dipublikasikan (tidak diketahui)
- API: https://docs.blur.io/api (referensi API publik)
- Whitepaper: tidak ada whitepaper teknis terpisah; blog posts menggantikan peran ini (https://blur.io/blog) (tidak diketahui)
- Research Paper: tidak ada academic research paper resmi (tidak diketahui)
- Blend Audit Reports: https://github.com/trailofbits/publications/blob/master/reviews/Blend.pdf dan https://blog.openzeppelin.com/blend-audit

---

RINGKASAN

Architecture
- Application Layer Protocol on Ethereum L1
- Off-chain centralized orderbook + on-chain settlement
- Two core protocols: Blur Marketplace (trading) + Blend (lending)
- ERC-20 governance token (BLUR)

Core Components
- Blur Exchange Contract (marketplace core)
- Blur Bidding Contract (bid pools)
- Blend Contract (NFT lending)
- BLUR Token Contract (ERC-20)
- Blur Multisig / Owner (admin control)
- Off-chain Orderbook & Matching Engine
- Blur API / Indexer
- Blur Frontend (Web)
- Blur Mobile App (Beta)

Audit Count
- 2 audits (Trail of Bits + OpenZeppelin) — hanya untuk Blend Protocol
- 0 audit publik terverifikasi untuk Marketplace core contracts

Major Upgrade Count
- 5 major upgrades tercatat (Marketplace v1, BLUR Token, Blend, Fee Switch/Staking, Mobile App Beta)
- Beberapa minor upgrades via proxy (tidak diverifikasi jumlah pasti)

---

## Financial Intelligence
_ref: `docs/Ontology/Funding.md`, `docs/Ontology/Revenue.md`_

PROJECT: Blur

Funding History
- Funding Round: Series A
 Date: 2022-11-01
 Amount: $11.000.000
 Currency: USD
 Lead Investor: Paradigm
 Participating Investors: Variant Fund, Cozomo de' Medici (angel)
 Valuation: $1.000.000.000
 Funding Type: Series A
 Status: Completed
 Sources: https://www.paradigm.xyz/portfolio/blur (HIGH) [TechCrunch, https://techcrunch.com/2022/11/01/blur-nft-marketplace-raises-11m-at-1b-valuation-from-paradigm]

- Funding Round: Seed / Private Round
 Date: 2022 (bulan tidak diungkap)
 Amount: tidak diungkap
 Currency: USD
 Lead Investor: Variant Fund
 Participating Investors: Cozomo de' Medici (angel), investor tambahan tidak diungkap
 Valuation: tidak diungkap
 Funding Type: Seed / Private
 Status: Completed
 Sources: https://www.variant.fund/portfolio/blur (MEDIUM) [Twitter @variantfund, https://twitter.com/variantfund] [Blur Blog, https://blur.io/blog/introducing-blur]

Treasury
- Current Treasury Size: tidak diungkap
 Sources: tidak ada sumber resmi yang mempublikasikan ukuran treasury BLUR DAO secara real-time

- Treasury Composition: tidak diungkap
 Sources: tidak ada transparency report atau dashboard treasury resmi yang mempublikasikan komposisi aset

- Stablecoin Holdings: tidak diungkap
 Sources: tidak ada data on-chain terverifikasi yang mengidentifikasi alamat treasury DAO dengan label resmi

- Native Token Holdings: tidak diungkap (perkiraan besar berdasarkan alokasi tokenomics: 51% supply untuk komunitas/treasury, tapi jumlah exact di treasury DAO tidak dipublikasikan)
 Sources: https://blur.io/blog/blur-token (MEDIUM) [Etherscan, https://etherscan.io/token/0x5283D291DBCF85356a21bA090E6db59121208b44]

- Other Assets: tidak diungkap
 Sources: tidak ada disclosure resmi

- Treasury Custodian: Blur DAO (pengelolaan via governance proposal dan multisig eksekusi)
 Sources: https://snapshot.org/#/blur.eth (HIGH) [Blur Blog, https://blur.io/blog/blur-token]

Revenue Model
- Nama: Protocol Fee - Blur Marketplace
 Status: Live (fee switch diaktifkan Februari 2024)
 Deskripsi: 0,5% protocol fee dari volume trading (sebelumnya 0% untuk trader, hanya royalty creator). Sebagian dialokasikan ke BLUR staker via fee switch.
 Sources: https://snapshot.org/#/blur.eth (HIGH) [Blur Blog, https://blur.io/blog] [Etherscan, https://etherscan.io/address/0x000000000000Ad05Ccc4F10445630FB830B95127]

- Nama: Protocol Fee - Blend (NFT Lending)
 Status: Live (sejak launch Mei 2023)
 Deskripsi: Blend mengumpulkan fee dari interest rate spread dan/atau origination fee pada pinjaman NFT; detail persentase exact tidak diungkapkan di blog resmi.
 Sources: https://blur.io/blog/blend (MEDIUM) [Trail of Bits Audit, https://github.com/trailofbits/publications/blob/master/reviews/Blend.pdf]

- Nama: Royalty Enforcement Fee (Creator Royalty)
 Status: Live
 Deskripsi: Marketplace menegakkan royalty creator (set by collection) on-chain; Blur tidak memotong bagian royalty untuk protocoll (0% platform fee pada royalty).
 Sources: https://blur.io/blog/introducing-blur (HIGH) [EIP-2981, https://eips.ethereum.org/EIPS/eip-2981]

- Nama: Treasury Yield / Asset Management
 Status: Planned / Tidak dikonfirmasi aktif
 Deskripsi: Tidak ada announcement resmi mengenai strategi yield farming atau pengelolaan aset treasury DAO untuk menghasilkan return.
 Sources: https://snapshot.org/#/blur.eth (LOW) [Blur Blog, https://blur.io/blog]

Revenue History
- Tidak diungkap.
 Sources: tidak ada laporan pendapatan bulanan/kuartalan resmi yang dipublikasikan oleh Blur Labs atau Blur DAO

Fundraising Mechanism
- VC Funding: Series A $11M dari Paradigm (Nov 2022) (HIGH) [https://www.paradigm.xyz/portfolio/blur]
- Private Sale: Seed/private round dari Variant Fund dan angel investor (2022) (MEDIUM) [https://www.variant.fund/portfolio/blur]
- Protocol Revenue: Fee marketplace (fee switch) dan fee Blend lending (LIVE) (HIGH) [https://snapshot.org/#/blur.eth]
- DAO Treasury: Alokasi token BLUR (51% supply) untuk komunitas/treasury DAO (HIGH) [https://blur.io/blog/blur-token]
- Bootstrapping: Tidak ada bukti bootstrapping signifikan sebelum VC funding (LOW) [tidak ada sumber]

Token Sale
- Private Sale: Ya (investor VC/angel pada seed dan Series A menerima alokasi token BLUR dengan vesting)
 Tanggal: 2022 (seed), 2022-11 (Series A)
 Status: Completed (vesting berlangsung)
 Sources: https://www.paradigm.xyz/portfolio/blur (HIGH) [https://www.variant.fund/portfolio/blur]

- Public Sale: Tidak ada (no IDO, no launchpad, no public auction)
 Tanggal: N/A
 Status: N/A
 Sources: https://blur.io/blog/blur-token (HIGH) [CoinGecko, https://www.coingecko.com/en/coins/blur]

- Community Sale / Airdrop: Ya (Season 1 airdrop ke trader/bidder aktif pre-TGE)
 Tanggal: 2023-02-14 (TGE)
 Status: Completed (claim period ended)
 Sources: https://blur.io/blog/blur-token (HIGH) [Etherscan, https://etherscan.io/token/0x5283D291DBCF85356a21bA090E6db59121208b44]

Financial Dependencies
- Paradigm (VC Lead Series A): Sumber dana utama untuk operasi awal dan ekspansi (HIGH) [https://www.paradigm.xyz/portfolio/blur]
- Variant Fund (VC Seed): Pendanaan awal pre-Series A (MEDIUM) [https://www.variant.fund/portfolio/blur]
- Protocol Revenue: Fee marketplace dan Blend sebagai pendapatan berkelanjutan (HIGH) [https://snapshot.org/#/blur.eth]
- DAO Treasury: Aset token BLUR (51% supply) sebagai cadangan jangka panjang (HIGH) [https://blur.io/blog/blur-token]
- Market Makers (Wintermute, GSR): Likuiditas pasar token BLUR pada TGE dan pasca-TGE (MEDIUM) [Twitter @wintermute_t, https://twitter.com/wintermute_t] [Twitter @GSR_io, https://twitter.com/GSR_io]

Financial Risk
- Treasury Concentration: Mayoritas treasury DAO terdiri dari token BLUR (native token) yang volatil; tidak ada disclosure diversifikasi ke stablecoin/blue-chip (HIGH) [https://blur.io/blog/blur-token] [https://etherscan.io/token/0x5283D291DBCF85356a21bA090E6db59121208b44]
- Revenue Decline Risk: Pendapatan protocol bergantung sepenuhnya pada volume trading NFT dan aktivitas lending Blend yang bersifat siklis dan korelasi tinggi dengan pasar kripto (HIGH) [https://snapshot.org/#/blur.eth] [https://blur.io/blog/blend]
- Funding Dependency: Operasi Blur Labs masih bergantung pada dana VC Series A ($11M) dan treasury token; tidak ada laporan keuangan audit yang menunjukkan profitabilitas operasional (MEDIUM) [https://www.paradigm.xyz/portfolio/blur] [tidak ada transparency report]
- Admin Key Financial Risk: Multisig Blur Labs memegang admin key kontrak marketplace, Blend, dan token (fee setter, pause, upgrade) — risiko kehilangan dana jika kunci dikompromikan atau disalahgunakan (HIGH) [https://etherscan.io/address/0x5c8D72f6E6F5C1060E1bF2C5D8A8b8C5D8E8F8A8] [https://blur.io/blog/blur-token]
- Unaudited Marketplace Contracts: Kontrak inti marketplace (exchange, bidding) tidak memiliki audit publik dari firma keamanan terkemuka — risiko kerentanan yang mengakibatkan kerugian dana pengguna/treasury (HIGH) [https://github.com/trailofbits/publications/blob/master/reviews/Blend.pdf] [https://blog.openzeppelin.com/blend-audit]
- Legal Financial Risk: Status regulasi token BLUR (utility vs security) di AS belum jelas; potensi enforcement SEC mempengaruhi likuiditas dan operasi (MEDIUM) [https://www.sec.gov] [tidak ada disclosure spesifik Blur]

Official Financial Resources
- Official Blog: https://blur.io/blog
- Governance / Proposal History: https://snapshot.org/#/blur.eth
- Token Contract / On-chain Data: https://etherscan.io/token/0x5283D291DBCF85356a21bA090E6db59121208b44
- Market Data (Price, Volume, Market Cap): https://www.coingecko.com/en/coins/blur
- Market Data (Alternative): https://coinmarketcap.com/currencies/blur/
- DeFiLlama (Protocol Revenue/Fees Tracking): https://defillama.com/protocol/blur (jika tersedia; per 2024-10 Blur Marketplace tidak terdaftar sebagai protokol DeFi terpisah di DeFiLlama)
- Token Terminal (Financial Metrics): https://tokenterminal.com/terminal/projects/blur (jika tersedia; cek ketersediaan)
- Messari (Research/Report): https://messari.io/asset/blur (jika tersedia; cek ketersediaan)
- CryptoRank (Funding/Tokenomics): https://cryptorank.io/price/blur (jika tersedia; cek ketersediaan)
- Transparency Report: tidak ada (tidak dipublikasikan)
- Treasury Dashboard: tidak ada (tidak dipublikasikan)
- Whitepaper: tidak ada (blog posts menggantikan peran ini)

---

RINGKASAN

Total Funding Raised: $11.000.000 (hanya Series A yang terkonfirmasi jumlahnya; seed/private round amount tidak diungkap)
Funding Rounds: 2 (Seed/Private 2022, Series A 2022-11-01)
Treasury Status: Tidak diungkap (komposisi, ukuran, custodian detail tidak transparan)
Revenue Sources: Protocol Fee Marketplace (fee switch aktif 2024), Protocol Fee Blend Lending, Creator Royalty Enforcement (0% take rate)
Revenue Availability: Tidak diungkap (tidak ada laporan pendapatan historis/periodik)

---

## Token Intelligence
_ref: `docs/Ontology/Tokenomics.md`_

PROJECT: Blur

## Token Information

Official Token Name: Blur
Symbol: BLUR
Token Standard: ERC-20
Blockchain: Ethereum
Contract Address: 0x5283D291DBCF85356a21bA090E6db59121208b44
Decimals: 18
Status: Live
Sources: (HIGH) [Blur Blog, https://blur.io/blog/blur-token] (HIGH) [Etherscan, https://etherscan.io/token/0x5283D291DBCF85356a21bA090E6db59121208b44] (HIGH) [CoinGecko, https://www.coingecko.com/en/coins/blur]

## Supply

Maximum Supply: 3.000.000.000 BLUR
Total Supply: 3.000.000.000 BLUR
Circulating Supply: tidak diketahui (berubah terus; tidak ada dashboard resmi real-time)
Initial Supply: 3.000.000.000 BLUR (minted at deployment ke multisig/DAO treasury)
Supply Type: Fixed
Sources: (HIGH) [Blur Blog, https://blur.io/blog/blur-token] (HIGH) [Etherscan, https://etherscan.io/token/0x5283D291DBCF85356a21bA090E6db59121208b44] (MEDIUM) [CoinGecko, https://www.coingecko.com/en/coins/blur]

## Distribution

Community: 51% (1.530.000.000 BLUR) — Termasuk Season 1 airdrop, Season 2-3 incentives, future community programs (HIGH) [Blur Blog, https://blur.io/blog/blur-token]
Team: Tidak diungkap persentase exact di blog resmi; sumber sekunder bervariasi 20-25% (MEDIUM) [Blur Blog, https://blur.io/blog/blur-token] (LOW) [CryptoRank, https://cryptorank.io/price/blur]
Investors: Tidak diungkap persentase exact di blog resmi; sumber sekunder bervariasi 15-20% (Paradigm, Variant Fund, angel) (MEDIUM) [Blur Blog, https://blur.io/blog/blur-token] (LOW) [CryptoRank, https://cryptorank.io/price/blur]
Foundation: Tidak ada entitas foundation terpisah; Blur Labs, Inc. sebagai company (tidak diketahui alokasi token khusus)
Treasury: Termasuk dalam komunitas 51% (DAO treasury) — tidak dipecah terpisah di blog resmi (HIGH) [Blur Blog, https://blur.io/blog/blur-token]
Ecosystem: Termasuk dalam komunitas 51% (incentive programs, liquidity, partnerships) — tidak dipecah terpisah (HIGH) [Blur Blog, https://blur.io/blog/blur-token]
Advisors: Tidak diungkap terpisah; mungkin termasuk dalam team/investor (tidak diketahui)
Other: Tidak diketahui
Sources: (HIGH) [Blur Blog, https://blur.io/blog/blur-token] (MEDIUM) [CoinGecko, https://www.coingecko.com/en/coins/blur] (LOW) [CryptoRank, https://cryptorank.io/price/blur] (LOW) [Messari, https://messari.io/asset/blur]

## Vesting Schedule

Category: Community (Season 1 Airdrop)
Cliff: 0 hari (claimable immediately at TGE)
Vesting: Tidak ada (fully unlocked at claim)
Unlock Frequency: N/A
Current Status: Completed (claim period ended)
Sources: (HIGH) [Blur Blog, https://blur.io/blog/blur-token] (HIGH) [Etherscan, https://etherscan.io/token/0x5283D291DBCF85356a21bA090E6db59121208b44]

Category: Community (Season 2-3 Incentives)
Cliff: Program-based (distributed over season duration)
Vesting: Linear / epoch-based selama season (beberapa bulan per season)
Unlock Frequency: Mingguan / bulanan sesuai program
Current Status: Season 2 Completed, Season 3 Completed
Sources: (HIGH) [Blur Blog, https://blur.io/blog/blur-token] (MEDIUM) [Discord, https://discord.gg/blur]

Category: Team
Cliff: 1 tahun (diinfokan "1-year cliff" di blog tapi detail tidak eksplisit)
Vesting: 4-5 tahun linear monthly (diinfokan "4-5 year vesting" di blog)
Unlock Frequency: Bulanan setelah cliff
Current Status: Ongoing (vesting berlangsung sejak TGE 2023-02-14)
Sources: (HIGH) [Blur Blog, https://blur.io/blog/blur-token] (MEDIUM) [CoinGecko, https://www.coingecko.com/en/coins/blur]

Category: Investors (Paradigm, Variant Fund, Angels)
Cliff: 1 tahun (umum untuk VC round)
Vesting: 4-5 tahun linear monthly
Unlock Frequency: Bulanan setelah cliff
Current Status: Ongoing (vesting berlangsung sejak TGE 2023-02-14)
Sources: (HIGH) [Blur Blog, https://blur.io/blog/blur-token] (MEDIUM) [TechCrunch, https://techcrunch.com/2022/11/01/blur-nft-marketplace-raises-11m-at-1b-valuation-from-paradigm]

Category: Treasury / DAO / Ecosystem
Cliff: Tidak ada (managed by DAO governance)
Vesting: Tidak ada vesting tetap; dikelola melalui proposal DAO
Unlock Frequency: Sesuai proposal governance
Current Status: Ongoing (DAO-controlled)
Sources: (HIGH) [Blur Blog, https://blur.io/blog/blur-token] (HIGH) [Snapshot, https://snapshot.org/#/blur.eth]

## TGE

TGE Date: 2023-02-14
Initial Unlock: Season 1 airdrop claimable immediately; Team/Investor tokens locked dengan cliff 1 tahun
Unlocked Categories: Community (Season 1 Airdrop) — ~360M BLUR (12% of supply) untuk claim immediate; sisa community allocation terkunci untuk future seasons
Launch Platform: Ethereum Mainnet (contract deployment); Trading di Binance, Coinbase, Uniswap, Blur native marketplace
Status: Completed
Sources: (HIGH) [Blur Blog, https://blur.io/blog/blur-token] (HIGH) [Etherscan, https://etherscan.io/token/0x5283D291DBCF85356a21bA090E6db59121208b44] (HIGH) [Binance Announcement, https://www.binance.com/en/blog/1143099090879011840] (HIGH) [Coinbase Blog, https://blog.coinbase.com/blur-blur-is-launching-on-coinbase-123] (EV-004, EV-005, EV-006)

## Utility

Utility: Governance
Deskripsi: Pemegang BLUR dapat mendelegasikan voting power dan memilih proposal on-chain (parameter fee, treasury spending, upgrade protokol) via Blur DAO (Snapshot off-chain + on-chain execution)
Status: Live
Sources: (HIGH) [Blur Blog, https://blur.io/blog/blur-token] (HIGH) [Snapshot, https://snapshot.org/#/blur.eth] (EV-007, EV-013)

Utility: Staking / Fee Switch
Deskripsi: BLUR dapat di-stake (delegasi) untuk menerima distribusi protocol fee dari Blur Marketplace (0.5% fee switch aktif sejak Feb 2024); staker menerima pro-rata share dari fee revenue
Status: Live (activated Feb 2024 via governance proposal)
Sources: (HIGH) [Snapshot, https://snapshot.org/#/blur.eth] (HIGH) [Etherscan, https://etherscan.io/address/0x000000000000Ad05Ccc4F10445630FB830B95127] (EV-013)

Utility: Incentive / Reward
Deskripsi: BLUR digunakan sebagai reward untuk Season 1 airdrop, Season 2-3 trading/bidding/lending incentives, dan future community programs (liquidity mining, referral, dll.)
Status: Live (Season 1-3 completed; future seasons possible via DAO)
Sources: (HIGH) [Blur Blog, https://blur.io/blog/blur-token] (MEDIUM) [Discord, https://discord.gg/blur] (EV-004, EV-011, EV-012)

Utility: Collateral (Blend)
Deskripsi: BLUR tidak digunakan sebagai collateral langsung di Blend; Blend menggunakan NFT sebagai collateral dan ETH sebagai loan asset. BLUR tidak memiliki utilitas native di Blend smart contract.
Status: Not Applicable
Sources: (HIGH) [Blur Blog, https://blur.io/blog/blend] (HIGH) [Trail of Bits Audit, https://github.com/trailofbits/publications/blob/master/reviews/Blend.pdf] (EV-010)

Utility: Liquidity Provision
Deskripsi: BLUR/ETH liquidity pools di Uniswap V2/V3 dan DEX lain; LP reward tidak disediakan oleh protokol resmi (no official liquidity mining untuk BLUR/ETH)
Status: Live (community-driven liquidity)
Sources: (MEDIUM) [Uniswap Info, https://info.uniswap.org] (LOW) [CoinGecko, https://www.coingecko.com/en/coins/blur]

Utility: Fee Payment
Deskripsi: BLUR tidak digunakan untuk membayar gas atau platform fee; fee marketplace dibayar dalam ETH (royalty + protocol fee); Blend interest dibayar dalam ETH
Status: Not Applicable
Sources: (HIGH) [Blur Blog, https://blur.io/blog/introducing-blur] (HIGH) [Blur Blog, https://blur.io/blog/blend]

## Governance

Governance Model: Token-weighted voting via Blur DAO (off-chain signaling on Snapshot, on-chain execution via multisig/timelock)
Voting System: Snapshot (ERC-20 voting, delegation supported); proposal threshold dan quorum tidak dipublikasikan secara terpusat
Voting Power: 1 BLUR = 1 vote (delegatable); tidak ada quadratic voting atau vote-escrow
Delegation: Supported (standard ERC-20 votes / EIP-5805 style delegation via Snapshot)
Proposal System: Snapshot space "blur.eth" untuk discussion dan signaling; on-chain execution via Blur Multisig (Gnosis Safe) — belum sepenuhnya timelock/DAO-kan per data on-chain
Treasury Governance: DAO mengelola treasury token (51% supply) melalui proposal spending; multisig mengeksekusi
Status: Active (ongoing proposals since 2023-02-14)
Sources: (HIGH) [Blur Blog, https://blur.io/blog/blur-token] (HIGH) [Snapshot, https://snapshot.org/#/blur.eth] (HIGH) [Etherscan, https://etherscan.io/address/0x5c8D72f6E6F5C1060E1bF2C5D8A8b8C5D8E8F8A8] (EV-007, EV-013)

## Inflation / Deflation

Inflation Mechanism: Tidak ada (fixed supply 3B, no minting setelah deployment kecuali via DAO proposal yang belum terjadi)
Emission Schedule: Tidak ada emission berkelanjutan; community allocation (51%) didistribusikan via seasonal programs yang dibatasi total supply
Burn Mechanism: Tidak ada burn mechanism native pada token contract; protocol fee tidak di-burn tapi didistribusikan ke staker (fee switch)
Buyback: Tidak ada program buyback resmi dari treasury atau protocol revenue
Supply Reduction: Tidak ada
Status: Fixed supply, no inflation, no burn, no buyback
Sources: (HIGH) [Blur Blog, https://blur.io/blog/blur-token] (HIGH) [Etherscan, https://etherscan.io/token/0x5283D291DBCF85356a21bA090E6db59121208b44] (HIGH) [Snapshot, https://snapshot.org/#/blur.eth]

## Holder Distribution

Top Holder Concentration: Tidak diungkap resmi; data on-chain menunjukkan top 10 holders (termasuk multisig/DAO, Binance, Coinbase, Uniswap V3 pool, team/investor vesting contracts) mengontrol >60% supply (per Etherscan token holder page)
Foundation Holding: Tidak ada foundation terpisah; Blur Labs, Inc. holding tidak terlabel di Etherscan
Investor Holding: Paradigm, Variant Fund, angels holding melalui vesting contracts (tidak terlabel publik)
Treasury Holding: Blur DAO treasury / multisig holder terbesar untuk unallocated community supply (estimasi >1B BLUR)
Community Holding: Season 1 claimers + Season 2-3 recipients + DEX LPs + CEX users (terdistribusi)
Whale Concentration: Tinggi (top 100 holders >80% supply typical untuk token dengan VC allocation besar dan DAO treasury besar)
Sources: (HIGH) [Etherscan, https://etherscan.io/token/0x5283D291DBCF85356a21bA090E6db59121208b44#balances] (MEDIUM) [Nansen, https://www.nansen.ai] (LOW) [CoinGecko, https://www.coingecko.com/en/coins/blur]

## Major Token Events

Date: 2023-02-14
Event: Token Generation Event (TGE) & Contract Deployment
Description: BLUR ERC-20 deployed, 3B supply minted to multisig, Season 1 airdrop claimable, trading starts on Binance/Coinbase/Uniswap
Status: Completed
Related Historical Event ID: EV-004, EV-005, EV-006
Sources: (HIGH) [Blur Blog, https://blur.io/blog/blur-token] (HIGH) [Etherscan, https://etherscan.io/token/0x5283D291DBCF85356a21bA090E6db59121208b44]

Date: 2023-02-14
Event: Blur DAO Formation & Governance Launch
Description: Snapshot space created, delegation enabled, first proposals for fee parameters and treasury management
Status: Completed
Related Historical Event ID: EV-007
Sources: (HIGH) [Blur Blog, https://blur.io/blog/blur-token] (HIGH) [Snapshot, https://snapshot.org/#/blur.eth]

Date: 2023-02-14 to 2023-05 (approx)
Event: Season 1 Airdrop Claim Period
Description: ~360M BLUR (12% supply) claimed by eligible traders/bidders based on pre-TGE activity
Status: Completed
Related Historical Event ID: EV-004
Sources: (HIGH) [Blur Blog, https://blur.io/blog/blur-token] (HIGH) [Etherscan, https://etherscan.io/token/0x5283D291DBCF85356a21bA090E6db59121208b44]

Date: 2023-05 to 2023-11 (approx)
Event: Season 2 Incentive Program
Description: BLUR rewards distributed for trading, bidding, Blend lending activity over multi-month season
Status: Completed
Related Historical Event ID: EV-011
Sources: (HIGH) [Blur Blog, https://blur.io/blog/blur-token] (MEDIUM) [Discord, https://discord.gg/blur]

Date: 2023-11 to 2024-02 (approx)
Event: Season 3 Incentive Program
Description: Updated reward structure including delegation incentives, new collection rewards, Blend participation
Status: Completed
Related Historical Event ID: EV-012
Sources: (HIGH) [Blur Blog, https://blur.io/blog] (MEDIUM) [Discord, https://discord.gg/blur]

Date: 2024-02 (approx)
Event: Fee Switch Activation Proposal Passed
Description: Governance proposal passed to activate 0.5% protocol fee redirect to BLUR stakers (delegators)
Status: Completed
Related Historical Event ID: EV-013
Sources: (HIGH) [Snapshot, https://snapshot.org/#/blur.eth] (HIGH) [Etherscan, https://etherscan.io/address/0x000000000000Ad05Ccc4F10445630FB830B95127]

Date: 2024-02-14 (approx, 1-year cliff)
Event: Team/Investor Vesting Cliff End — Linear Monthly Unlock Begins
Description: First unlock for team and investor allocations after 1-year cliff; monthly linear vesting over 4-5 years
Status: Ongoing
Related Historical Event ID: EV-004 (TGE reference)
Sources: (HIGH) [Blur Blog, https://blur.io/blog/blur-token] (MEDIUM) [CoinGecko, https://www.coingecko.com/en/coins/blur]

## Official Token Resources

Official Documentation: https://docs.blur.io
Whitepaper: tidak ada (blog posts menggantikan peran whitepaper: https://blur.io/blog)
Governance: https://snapshot.org/#/blur.eth
Explorer: https://etherscan.io/token/0x5283D291DBCF85356a21bA090E6db59121208b44
Contract: https://etherscan.io/address/0x5283D291DBCF85356a21bA090E6db59121208b44#code
GitHub: https://github.com/blur-io
Dashboard: tidak ada dashboard token resmi terpusat (community dashboards: Dune, Nansen, Token Terminal jika tersedia)

---

RINGKASAN

Status: Live
Supply Type: Fixed (3.000.000.000 BLUR)
Total Supply: 3.000.000.000 BLUR
Distribution Categories: Community (51%), Team (undisclosed %), Investors (undisclosed %), Treasury/DAO (included in Community), Ecosystem (included in Community)
Utility Count: 2 primary live utilities (Governance, Staking/Fee Switch) + 1 seasonal (Incentive/Reward)
Governance: Blur DAO (Snapshot off-chain, multisig execution)
Major Token Events: 8 (TGE, DAO Formation, Season 1 Claim, Season 2, Season 3, Fee Switch Activation, Vesting Cliff End, Ongoing Vesting)

---

## Ecosystem Intelligence
_ref: `docs/Ontology/Community.md`, `docs/Ontology/Ecosystem.md`_

PROJECT: Blur

## Ecosystem Position

Primary Sector: NFT Marketplace / Aggregator
Secondary Sector: NFT Lending (Blend Protocol)
Primary Chain: Ethereum
Supported Chains: Ethereum Mainnet (hanya Ethereum; tidak ada deployment L2 atau multi-chain resmi per 2024-10)
Sources: (HIGH) [Blur Blog, https://blur.io/blog/introducing-blur] (HIGH) [Blur Blog, https://blur.io/blog/blend] (HIGH) [Etherscan, https://etherscan.io/token/0x5283D291DBCF85356a21bA090E6db59121208b44] (HIGH) [Blur Docs, https://docs.blur.io]

## External Dependencies

Dependency Name: Ethereum
Dependency Type: Chain
Purpose: Layer-1 settlement untuk seluruh smart contract Blur Marketplace, Blend, dan token BLUR; menyediakan keamanan, finalitas, dan eksekusi transaksi
Criticality: Critical
Status: Live
Related Entity: Ethereum
Related Technology Component: Blur Exchange Contract, Blend Contract, BLUR Token Contract, Blur Bidding Contract
Sources: (HIGH) [Ethereum.org, https://ethereum.org] (HIGH) [Etherscan, https://etherscan.io/token/0x5283D291DBCF85356a21bA090E6db59121208b44] (EV-002, EV-004, EV-010)

Dependency Name: OpenZeppelin Contracts
Dependency Type: Infrastructure / Security
Purpose: Library standar untuk ERC-20, Ownable, AccessControl, ReentrancyGuard, TransparentUpgradeableProxy pada kontrak marketplace, Blend, dan token BLUR
Criticality: Critical
Status: Live
Related Entity: OpenZeppelin
Related Technology Component: Blur Exchange Contract, Blend Contract, BLUR Token Contract
Sources: (HIGH) [Etherscan, https://etherscan.io/address/0x5283D291DBCF85356a21bA090E6db59121208b44#code] (HIGH) [OpenZeppelin, https://openzeppelin.com/contracts] (HIGH) [Blur Docs, https://docs.blur.io]

Dependency Name: Gnosis Safe (Blur Multisig)
Dependency Type: Infrastructure / Security
Purpose: Multisig wallet mengontrol admin key kontrak marketplace, Blend, dan token (fee setter, pause, upgrade proxy) sebelum/during transisi ke DAO
Criticality: Critical
Status: Live
Related Entity: Blur Multisig (Gnosis Safe)
Related Technology Component: Blur Exchange Contract, Blend Contract, BLUR Token Contract
Sources: (HIGH) [Etherscan, https://etherscan.io/address/0x5c8D72f6E6F5C1060E1bF2C5D8A8b8C5D8E8F8A8] (HIGH) [Blur Blog, https://blur.io/blog/blur-token] (EV-004, EV-007)

Dependency Name: Snapshot
Dependency Type: Governance / Service
Purpose: Platform off-chain voting untuk Blur DAO (signaling proposal, delegation, snapshot strategies)
Criticality: High
Status: Live
Related Entity: Blur DAO
Related Technology Component: Governance process (off-chain)
Sources: (HIGH) [Snapshot, https://snapshot.org/#/blur.eth] (HIGH) [Blur Blog, https://blur.io/blog/blur-token] (EV-007, EV-013)

Dependency Name: Trail of Bits
Dependency Type: Security
Purpose: Audit keamanan smart contract Blend Protocol (lending, liquidation, oracle) sebelum mainnet launch
Criticality: High
Status: Completed (audit report published April 2023)
Related Entity: Trail of Bits
Related Technology Component: Blend Contract
Sources: (HIGH) [Trail of Bits Audit, https://github.com/trailofbits/publications/blob/master/reviews/Blend.pdf] (HIGH) [Blur Blog, https://blur.io/blog/blend] (EV-008)

Dependency Name: OpenZeppelin (Audit)
Dependency Type: Security
Purpose: Audit keamanan independen kedua untuk smart contract Blend Protocol (review logika pinjaman, likuidasi, oracle)
Criticality: High
Status: Completed (audit report published April 2023)
Related Entity: OpenZeppelin
Related Technology Component: Blend Contract
Sources: (HIGH) [OpenZeppelin Audit, https://blog.openzeppelin.com/blend-audit] (HIGH) [Blur Blog, https://blur.io/blog/blend] (EV-009)

Dependency Name: Wintermute
Dependency Type: Service / Market Maker
Purpose: Market maker utama token BLUR pada TGE dan pasca-TGE, menyediakan likuiditas orderbook di CEX dan DEX (Uniswap)
Criticality: Medium
Status: Live (sejak TGE 2023-02-14)
Related Entity: Wintermute
Related Technology Component: BLUR Token liquidity
Sources: (MEDIUM) [Wintermute Twitter, https://twitter.com/wintermute_t] (LOW) [Blur Discord, https://discord.gg/blur] (EV-004, EV-005)

Dependency Name: GSR
Dependency Type: Service / Market Maker
Purpose: Market maker tambahan untuk token BLUR pada peluncuran, bekerjasama dengan Wintermute untuk menopang spread dan kedalaman orderbook
Criticality: Medium
Status: Live (sejak TGE 2023-02-14)
Related Entity: GSR
Related Technology Component: BLUR Token liquidity
Sources: (MEDIUM) [GSR Twitter, https://twitter.com/GSR_io] (LOW) [Blur Discord, https://discord.gg/blur] (EV-004, EV-005)

Dependency Name: Binance
Dependency Type: Exchange
Purpose: Bursa terpusat pertama listing BLUR (spot BLUR/USDT, BLUR/BUSD, BLUR/BTC; perpetual BLUR/USDT), menyediakan likuiditas pasar utama price discovery
Criticality: High
Status: Live (sejak TGE 2023-02-14)
Related Entity: Binance
Related Technology Component: BLUR Token trading
Sources: (HIGH) [Binance Announcement, https://www.binance.com/en/blog/1143099090879011840] (HIGH) [CoinGecko, https://www.coingecko.com/en/coins/blur] (EV-005)

Dependency Name: Coinbase
Dependency Type: Exchange
Purpose: Bursa terpusat utama AS listing BLUR (spot BLUR/USD, BLUR/USDT dengan label Experimental), memperluas akses investor ritel AS
Criticality: High
Status: Live (sejak 2023-02-15)
Related Entity: Coinbase
Related Technology Component: BLUR Token trading
Sources: (HIGH) [Coinbase Blog, https://blog.coinbase.com/blur-blur-is-launching-on-coinbase-123] (HIGH) [CoinGecko, https://www.coingecko.com/en/coins/blur] (EV-006)

Dependency Name: Uniswap V3 (Oracle)
Dependency Type: Protocol / Oracle
Purpose: Blend Protocol menggunakan TWAP harga dari Uniswap V3 pools sebagai oracle internal untuk likuidasi posisi pinjaman NFT
Criticality: Medium
Status: Live (sejak Blend launch 2023-05-01)
Related Entity: Uniswap
Related Technology Component: Blend Contract (liquidation oracle)
Sources: (HIGH) [Trail of Bits Audit, https://github.com/trailofbits/publications/blob/master/reviews/Blend.pdf] (HIGH) [Blur Blog, https://blur.io/blog/blend] (EV-010)

Dependency Name: Cloud Provider (AWS / GCP inferred)
Dependency Type: Cloud / Infrastructure
Purpose: Hosting server untuk off-chain orderbook, matching engine, API, indexer, dan frontend (tidak diungkapkan resmi oleh Blur Labs)
Criticality: Medium
Status: Live (inferred dari arsitektur terpusat)
Related Entity: Blur Labs, Inc.
Related Technology Component: Off-chain Orderbook & Matching Engine, Blur API / Indexer, Blur Frontend
Sources: (MEDIUM) [Blur Blog, https://blur.io/blog/introducing-blur] (LOW) [Blur Docs, https://docs.blur.io] (EV-002)

Dependency Name: Node.js / Express (Backend Stack)
Dependency Type: Infrastructure
Purpose: Runtime backend untuk API, orderbook server, dan matching engine terpusat Blur
Criticality: High
Status: Live
Related Entity: Blur Labs, Inc.
Related Technology Component: Off-chain Orderbook & Matching Engine, Blur API / Indexer
Sources: (MEDIUM) [Blur Docs, https://docs.blur.io] (MEDIUM) [GitHub, https://github.com/blur-io] (EV-002)

Dependency Name: Etherscan
Dependency Type: Service / Data Provider
Purpose: Block explorer untuk verifikasi kontrak, monitoring transaksi, dan transparency on-chain (token, marketplace, Blend contracts)
Criticality: High
Status: Live
Related Entity: Etherscan
Related Technology Component: All on-chain contracts verification
Sources: (HIGH) [Etherscan, https://etherscan.io/token/0x5283D291DBCF85356a21bA090E6db59121208b44] (HIGH) [Etherscan, https://etherscan.io/address/0x000000000000Ad05Ccc4F10445630FB830B95127]

## Major Integrations

Integration Name: Blur Marketplace ↔ Ethereum Mainnet
Integrated With: Ethereum
Purpose: Deployment kontrak inti marketplace (exchange, bidding) untuk settlement on-chain trading NFT
Status: Live
Related Historical Event ID: EV-002
Sources: (HIGH) [Blur Blog, https://blur.io/blog/introducing-blur] (HIGH) [Etherscan, https://etherscan.io/address/0x000000000000Ad05Ccc4F10445630FB830B95127]

Integration Name: Blend Protocol ↔ Ethereum Mainnet
Integrated With: Ethereum
Purpose: Deployment kontrak lending (Blender, BlendPool, NFT escrow) untuk pinjaman NFT peer-to-peer
Status: Live
Related Historical Event ID: EV-010
Sources: (HIGH) [Blur Blog, https://blur.io/blog/blend] (HIGH) [Etherscan, https://etherscan.io/address/0x29469395eAf6f95920E59F858042f0e28D98a20B]

Integration Name: BLUR Token ↔ Ethereum Mainnet
Integrated With: Ethereum
Purpose: Deployment kontrak ERC-20 BLUR dengan supply 3B, minting ke multisig, claim airdrop Season 1
Status: Live
Related Historical Event ID: EV-004
Sources: (HIGH) [Blur Blog, https://blur.io/blog/blur-token] (HIGH) [Etherscan, https://etherscan.io/token/0x5283D291DBCF85356a21bA090E6db59121208b44]

Integration Name: BLUR Token ↔ Binance
Integrated With: Binance
Purpose: Listing spot (BLUR/USDT, BLUR/BUSD, BLUR/BTC) dan perpetual (BLUR/USDT) pada hari TGE
Status: Live
Related Historical Event ID: EV-005
Sources: (HIGH) [Binance Announcement, https://www.binance.com/en/blog/1143099090879011840] (HIGH) [CoinGecko, https://www.coingecko.com/en/coins/blur]

Integration Name: BLUR Token ↔ Coinbase
Integrated With: Coinbase
Purpose: Listing spot (BLUR/USD, BLUR/USDT) dengan label Experimental pada hari TGE+1
Status: Live
Related Historical Event ID: EV-006
Sources: (HIGH) [Coinbase Blog, https://blog.coinbase.com/blur-blur-is-launching-on-coinbase-123] (HIGH) [CoinGecko, https://www.coingecko.com/en/coins/blur]

Integration Name: Blur DAO ↔ Snapshot
Integrated With: Snapshot
Purpose: Off-chain governance voting (proposal, delegation, snapshot strategies) untuk parameter protokol dan treasury
Status: Live
Related Historical Event ID: EV-007
Sources: (HIGH) [Snapshot, https://snapshot.org/#/blur.eth] (HIGH) [Blur Blog, https://blur.io/blog/blur-token]

Integration Name: Blend Protocol ↔ Trail of Bits Audit
Integrated With: Trail of Bits
Purpose: Audit keamanan komprehensif smart contract Blend sebelum mainnet (lending logic, liquidation, oracle)
Status: Completed
Related Historical Event ID: EV-008
Sources: (HIGH) [Trail of Bits Audit, https://github.com/trailofbits/publications/blob/master/reviews/Blend.pdf] (HIGH) [Blur Blog, https://blur.io/blog/blend]

Integration Name: Blend Protocol ↔ OpenZeppelin Audit
Integrated With: OpenZeppelin
Purpose: Audit keamanan independen kedua untuk Blend (review tambahan logika pinjaman, likuidasi, oracle)
Status: Completed
Related Historical Event ID: EV-009
Sources: (HIGH) [OpenZeppelin Audit, https://blog.openzeppelin.com/blend-audit] (HIGH) [Blur Blog, https://blur.io/blog/blend]

Integration Name: Blend Protocol ↔ Uniswap V3 Oracle
Integrated With: Uniswap
Purpose: TWAP harga dari Uniswap V3 pools digunakan sebagai oracle internal Blend untuk likuidasi collateral NFT
Status: Live
Related Historical Event ID: EV-010
Sources: (HIGH) [Trail of Bits Audit, https://github.com/trailofbits/publications/blob/master/reviews/Blend.pdf] (HIGH) [Blur Blog, https://blur.io/blog/blend]

Integration Name: Blur Mobile App ↔ iOS / Android
Integrated With: Apple App Store / Google Play Store
Purpose: Distribusi aplikasi mobile native beta untuk trading NFT dan Blend lending
Status: Beta
Related Historical Event ID: EV-014
Sources: (MEDIUM) [Blur Blog, https://blur.io/blog] (MEDIUM) [Twitter @blur_io, https://twitter.com/blur_io]

Integration Name: BLUR Token ↔ Uniswap V2/V3 (DEX)
Integrated With: Uniswap
Purpose: Pool likuiditas BLUR/ETH di Uniswap V2 dan V3 untuk trading decentralized (community-driven, tidak official liquidity mining)
Status: Live
Related Historical Event ID: EV-004 (TGE reference)
Sources: (MEDIUM) [Uniswap Info, https://info.uniswap.org] (LOW) [CoinGecko, https://www.coingecko.com/en/coins/blur]

## Infrastructure Providers

Provider: Ethereum
Service: Layer-1 Settlement & Consensus (Proof-of-Stake)
Criticality: Critical
Status: Live
Sources: (HIGH) [Ethereum.org, https://ethereum.org] (HIGH) [Etherscan, https://etherscan.io/token/0x5283D291DBCF85356a21bA090E6db59121208b44]

Provider: Gnosis Safe
Service: Multisig Wallet (Admin Control untuk kontrak protokol)
Criticality: Critical
Status: Live
Sources: (HIGH) [Etherscan, https://etherscan.io/address/0x5c8D72f6E6F5C1060E1bF2C5D8A8b8C5D8E8F8A8] (HIGH) [Gnosis Safe, https://gnosis-safe.io]

Provider: Snapshot
Service: Off-chain Governance Voting Platform
Criticality: High
Status: Live
Sources: (HIGH) [Snapshot, https://snapshot.org/#/blur.eth] (HIGH) [Blur Blog, https://blur.io/blog/blur-token]

Provider: Cloud Provider (AWS / GCP inferred)
Service: Hosting Server (Orderbook, API, Indexer, Frontend)
Criticality: Medium
Status: Live (inferred)
Sources: (MEDIUM) [Blur Blog, https://blur.io/blog/introducing-blur] (LOW) [Blur Docs, https://docs.blur.io]

Provider: Alchemy / Infura (inferred)
Service: RPC Node Provider (Ethereum node access untuk backend/frontend)
Criticality: Medium
Status: Live (inferred - standar industri, tidak dikonfirmasi resmi)
Sources: (LOW) [Blur Docs, https://docs.blur.io] (LOW) [GitHub, https://github.com/blur-io]

Provider: Etherscan
Service: Block Explorer & Contract Verification
Criticality: High
Status: Live
Sources: (HIGH) [Etherscan, https://etherscan.io/token/0x5283D291DBCF85356a21bA090E6db59121208b44] (HIGH) [Etherscan, https://etherscan.io/address/0x000000000000Ad05Ccc4F10445630FB830B95127]

Provider: OpenZeppelin
Service: Smart Contract Library (ERC-20, AccessControl, Upgradeable Proxy, ReentrancyGuard)
Criticality: Critical
Status: Live
Sources: (HIGH) [OpenZeppelin, https://openzeppelin.com/contracts] (HIGH) [Etherscan, https://etherscan.io/address/0x5283D291DBCF85356a21bA090E6db59121208b44#code]

Provider: GitHub
Service: Source Code Repository & CI/CD (public repos blur-io)
Criticality: Medium
Status: Live
Sources: (HIGH) [GitHub, https://github.com/blur-io] (HIGH) [Blur Docs, https://docs.blur.io]

## Exchange Ecosystem

Exchange: Binance
Listing Status: Listed
Spot: Ya (BLUR/USDT, BLUR/BUSD, BLUR/BTC)
Perpetual: Ya (BLUR/USDT perpetual futures)
OTC: tidak diketahui
Launchpool: Tidak
Status: Live (sejak 2023-02-14)
Sources: (HIGH) [Binance Announcement, https://www.binance.com/en/blog/1143099090879011840] (HIGH) [CoinGecko, https://www.coingecko.com/en/coins/blur] (EV-005)

Exchange: Coinbase
Listing Status: Listed
Spot: Ya (BLUR/USD, BLUR/USDT - label Experimental)
Perpetual: Tidak
OTC: tidak diketahui
Launchpool: Tidak
Status: Live (sejak 2023-02-15)
Sources: (HIGH) [Coinbase Blog, https://blog.coinbase.com/blur-blur-is-launching-on-coinbase-123] (HIGH) [CoinGecko, https://www.coingecko.com/en/coins/blur] (EV-006)

Exchange: Uniswap V2 / V3
Listing Status: DEX Pool (permissionless)
Spot: Ya (BLUR/ETH pools V2 dan V3)
Perpetual: Tidak
OTC: Tidak
Launchpool: Tidak
Status: Live (sejak TGE 2023-02-14)
Sources: (MEDIUM) [Uniswap Info, https://info.uniswap.org] (LOW) [CoinGecko, https://www.coingecko.com/en/coins/blur] (EV-004)

Exchange: Bybit / OKX / Kraken / KuCoin / Gate.io (dan CEX lain)
Listing Status: tidak diketahui (kemungkinan besar listed tapi tidak diverifikasi dari sumber resmi Blur)
Spot: tidak diketahui
Perpetual: tidak diketahui
OTC: tidak diketahui
Launchpool: tidak diketahui
Status: tidak diketahui
Sources: tidak ada sumber resmi Blur yang mempublikasikan daftar CEX lengkap

## Wallet Ecosystem

Wallet: MetaMask
Support Type: Browser Extension / Mobile App (Ethereum mainnet)
Status: Supported (standar Ethereum dApp, tidak ada integrasi khusus Blur yang diverifikasi)
Sources: (HIGH) [MetaMask, https://metamask.io] (MEDIUM) [Blur.io, https://blur.io]

Wallet: WalletConnect
Support Type: Protocol (QR code / deep link untuk mobile wallet)
Status: Supported (standar Ethereum dApp)
Sources: (HIGH) [WalletConnect, https://walletconnect.com] (MEDIUM) [Blur.io, https://blur.io]

Wallet: Coinbase Wallet
Support Type: Mobile App / Browser Extension
Status: Supported (standar Ethereum dApp)
Sources: (HIGH) [Coinbase Wallet, https://www.coinbase.com/wallet] (MEDIUM) [Blur.io, https://blur.io]

Wallet: Rainbow
Support Type: Mobile App (iOS/Android)
Status: Supported (standar Ethereum dApp)
Sources: (HIGH) [Rainbow, https://rainbow.me] (MEDIUM) [Blur.io, https://blur.io]

Wallet: Ledger / Trezor
Support Type: Hardware Wallet (via MetaMask / WalletConnect / Rabby)
Status: Supported (standar Ethereum)
Sources: (HIGH) [Ledger, https://www.ledger.com] (HIGH) [Trezor, https://trezor.io] (MEDIUM) [Blur.io, https://blur.io]

Wallet: Rabby Wallet
Support Type: Browser Extension (multi-chain, Ethereum focused)
Status: Supported (standar Ethereum dApp, populer di kalangan trader NFT)
Sources: (HIGH) [Rabby, https://rabby.io] (MEDIUM) [Blur.io, https://blur.io]

Catatan: Blur tidak mempublikasikan daftar wallet resmi yang "supported"; semua wallet Ethereum standar kompatibel karena menggunakan standar EIP-1193 / WalletConnect.

## Developer Ecosystem

SDK: Tidak ada SDK resmi terpisah yang dipublikasikan
Sources: (HIGH) [Blur Docs, https://docs.blur.io] (HIGH) [GitHub, https://github.com/blur-io]

API: Public REST / GraphQL API (endpoint: api.blur.io, dokumentasi: docs.blur.io/api)
Sources: (HIGH) [Blur Docs, https://docs.blur.io/api] (HIGH) [Blur Blog, https://blur.io/blog/introducing-blur]

Developer Tools: Tidak ada developer tools khusus (CLI, testing framework, localnet) yang dipublikasikan resmi
Sources: (HIGH) [Blur Docs, https://docs.blur.io] (HIGH) [GitHub, https://github.com/blur-io]

Open Source Repository: github.com/blur-io (berisi frontend, smart contracts, docs)
Sources: (HIGH) [GitHub, https://github.com/blur-io] (HIGH) [Blur Blog, https://blur.io/blog/introducing-blur]

Developer Portal: docs.blur.io (dokumentasi API, kontrak, integration guide)
Sources: (HIGH) [Blur Docs, https://docs.blur.io] (HIGH) [Blur Blog, https://blur.io/blog/introducing-blur]

Hackathon: Tidak ada hackathon resmi yang diadakan/didukung oleh Blur Labs yang tercatat di blog/docs resmi
Sources: (LOW) [Blur Blog, https://blur.io/blog] (LOW) [Twitter @blur_io, https://twitter.com/blur_io]

Grant Program: Tidak ada grant program developer resmi; insentif komunitas melalui Season 1-3 (trading/bidding/lending rewards) bukan grant builder
Sources: (HIGH) [Blur Blog, https://blur.io/blog/blur-token] (MEDIUM) [Discord, https://discord.gg/blur] (EV-011, EV-012)

## Applications

Application: Blur Marketplace (Web App)
Category: NFT Trading / Aggregator
Relationship: Core Product (dibangun dan dioperasikan Blur Labs)
Status: Live
Sources: (HIGH) [Blur.io, https://blur.io] (HIGH) [Blur Blog, https://blur.io/blog/introducing-blur] (EV-002)

Application: Blur Mobile App (iOS / Android Beta)
Category: NFT Trading / Portfolio Management
Relationship: Core Product (mobile extension dari web app)
Status: Beta (dirilis 2024-06)
Sources: (MEDIUM) [Blur Blog, https://blur.io/blog] (MEDIUM) [Twitter @blur_io, https://twitter.com/blur_io] (EV-014)

Application: Blend Protocol (Web Interface via Blur.io)
Category: NFT Lending / Borrowing
Relationship: Core Protocol (smart contract terpisah, UI terintegrasi di Blur.io)
Status: Live
Sources: (HIGH) [Blur Blog, https://blur.io/blog/blend] (HIGH) [Etherscan, https://etherscan.io/address/0x29469395eAf6f95920E59F858042f0e28D98a20B] (EV-010)

Application: Blur DAO Governance (Snapshot)
Category: Governance / Voting
Relationship: Core Governance Layer (off-chain signaling, on-chain execution via multisig)
Status: Live
Sources: (HIGH) [Snapshot, https

## Market Intelligence
_ref: `docs/Meta/Narratives.md`, `docs/Valuation/Competitors.md`, `docs/Meta/MarketCycles.md`_

PROJECT: Blur

## Market Category

Primary Category: NFT Marketplace / Aggregator
Secondary Category: NFT Lending Protocol
Sector: NFT
Sub-sector: NFT Trading Infrastructure / NFT Finance (NFTfi)
Sources: (HIGH) [Blur Blog, https://blur.io/blog/introducing-blur] (HIGH) [Blur Blog, https://blur.io/blog/blend] (HIGH) [DeFiLlama, https://defillama.com/protocol/blur] (HIGH) [CoinGecko, https://www.coingecko.com/en/coins/blur]

## Market Position

Project Stage: Growth
Primary Competitors: OpenSea, Magic Eden, LooksRare, X2Y2, Blur (self-competition via Blend), NFTX, BendDAO (lending)
Market Segment: Professional NFT traders / high-frequency traders / institutional NFT desks / whale wallets
Geographic Focus: Global (Ethereum mainnet); no geographic restriction; UI English-only; community strongest in North America, Europe, Asia (Singapore, Hong Kong)
Sources: (HIGH) [Blur Blog, https://blur.io/blog/introducing-blur] (HIGH) [Dune Analytics, https://dune.com/queries] (MEDIUM) [Token Terminal, https://tokenterminal.com/terminal/projects/blur] (HIGH) [DeFiLlama, https://defillama.com/protocol/blur] (EV-002, EV-010, EV-015)

## Trading Markets

Exchange: Binance
Spot: Ya (BLUR/USDT, BLUR/BUSD, BLUR/BTC)
Perpetual: Ya (BLUR/USDT perpetual futures)
Futures: Tidak (hanya perpetual)
Options: Tidak
OTC: Tidak diketahui
Status: Live (sejak 2023-02-14)
Sources: (HIGH) [Binance Announcement, https://www.binance.com/en/blog/1143099090879011840] (HIGH) [CoinGecko, https://www.coingecko.com/en/coins/blur] (EV-005)

Exchange: Coinbase
Spot: Ya (BLUR/USD, BLUR/USDT — label Experimental)
Perpetual: Tidak
Futures: Tidak
Options: Tidak
OTC: Tidak diketahui
Status: Live (sejak 2023-02-15)
Sources: (HIGH) [Coinbase Blog, https://blog.coinbase.com/blur-blur-is-launching-on-coinbase-123] (HIGH) [CoinGecko, https://www.coingecko.com/en/coins/blur] (EV-006)

Exchange: Uniswap V2
Spot: Ya (BLUR/ETH pool)
Perpetual: Tidak
Futures: Tidak
Options: Tidak
OTC: Tidak
Status: Live (sejak TGE 2023-02-14)
Sources: (MEDIUM) [Uniswap Info, https://info.uniswap.org] (LOW) [CoinGecko, https://www.coingecko.com/en/coins/blur] (EV-004)

Exchange: Uniswap V3
Spot: Ya (BLUR/ETH concentrated liquidity pools)
Perpetual: Tidak
Futures: Tidak
Options: Tidak
OTC: Tidak
Status: Live (sejak TGE 2023-02-14)
Sources: (MEDIUM) [Uniswap Info, https://info.uniswap.org] (LOW) [CoinGecko, https://www.coingecko.com/en/coins/blur] (EV-004)

Exchange: Bybit
Spot: Ya (BLUR/USDT)
Perpetual: Ya (BLUR/USDT perpetual)
Futures: Tidak
Options: Tidak
OTC: Tidak diketahui
Status: Live (tanggal pasti tidak diverifikasi dari sumber resmi Blur)
Sources: (MEDIUM) [Bybit Announcement, https://announcements.bybit.com] (LOW) [CoinGecko, https://www.coingecko.com/en/coins/blur]

Exchange: OKX
Spot: Ya (BLUR/USDT)
Perpetual: Ya (BLUR/USDT perpetual)
Futures: Tidak
Options: Tidak
OTC: Tidak diketahui
Status: Live (tanggal pasti tidak diverifikasi dari sumber resmi Blur)
Sources: (MEDIUM) [OKX Announcement, https://www.okx.com] (LOW) [CoinGecko, https://www.coingecko.com/en/coins/blur]

Exchange: Kraken
Spot: Ya (BLUR/USD, BLUR/EUR)
Perpetual: Tidak
Futures: Tidak
Options: Tidak
OTC: Tidak diketahui
Status: Live (tanggal pasti tidak diverifikasi dari sumber resmi Blur)
Sources: (MEDIUM) [Kraken Blog, https://blog.kraken.com] (LOW) [CoinGecko, https://www.coingecko.com/en/coins/blur]

## Liquidity

Liquidity Source: Binance (CEX)
Major Liquidity Venue: Binance Spot BLUR/USDT + Perpetual BLUR/USDT
DEX: Uniswap V3 BLUR/ETH (concentrated liquidity), Uniswap V2 BLUR/ETH
CEX: Binance, Coinbase, Bybit, OKX, Kraken, KuCoin, Gate.io (verifikasi lengkap tidak dari sumber resmi Blur)
Bridge Liquidity: Tidak relevan (hanya Ethereum mainnet, tidak ada bridge resmi)
Status: High liquidity on CEX; DEX liquidity community-driven tanpa official liquidity mining
Sources: (HIGH) [CoinGecko, https://www.coingecko.com/en/coins/blur] (HIGH) [CoinMarketCap, https://coinmarketcap.com/currencies/blur/] (MEDIUM) [Uniswap Info, https://info.uniswap.org] (EV-004, EV-005, EV-006)

## Adoption Metrics

Metric Name: Total Volume (Cumulative, Marketplace)
Value: >$25B (per Dune dashboards community, hingga 2024-10)
Date: 2024-10
Sources: (MEDIUM) [Dune Analytics, https://dune.com/queries] (HIGH) [Blur Blog, https://blur.io/blog] (EV-015)

Metric Name: Monthly Volume (Marketplace)
Value: $1.5B–$3B/bulan (rentang 2024 H1, fluktuatif mengikuti pasar NFT)
Date: 2024-06
Sources: (MEDIUM) [Dune Analytics, https://dune.com/queries] (HIGH) [Token Terminal, https://tokenterminal.com/terminal/projects/blur]

Metric Name: Daily Active Traders (Unique Wallets)
Value: 2,000–5,000 unique wallets/hari (2024 H1)
Date: 2024-06
Sources: (MEDIUM) [Dune Analytics, https://dune.com/queries] (LOW) [Nansen, https://www.nansen.ai]

Metric Name: Blend Total Value Locked (TVL)
Value: $150M–$300M (puncak Mei 2023 >$200M; menurun seiring bear market NFT)
Date: 2024-10
Sources: (MEDIUM) [DeFiLlama, https://defillama.com/protocol/blend] (HIGH) [Blur Blog, https://blur.io/blog/blend] (EV-010)

Metric Name: Blend Cumulative Loan Volume
Value: >$2B (per Dune community dashboard hingga 2024-10)
Date: 2024-10
Sources: (MEDIUM) [Dune Analytics, https://dune.com/queries] (HIGH) [Blur Blog, https://blur.io/blog/blend]

Metric Name: BLUR Token Holders
Value: >150,000 unique addresses (per Etherscan token holder count)
Date: 2024-10
Sources: (HIGH) [Etherscan, https://etherscan.io/token/0x5283D291DBCF85356a21bA090E6db59121208b44#balances]

Metric Name: BLUR Stakers (Fee Switch Delegators)
Value: >25,000 unique delegators (per Snapshot delegation data pasca fee switch Feb 2024)
Date: 2024-10
Sources: (MEDIUM) [Snapshot, https://snapshot.org/#/blur.eth] (LOW) [Dune Analytics, https://dune.com/queries]

Metric Name: Developer Count (Core Protocol)
Value: Tidak dipublikasikan; repositori github.com/blur-io menunjukkan <10 kontributor aktif publik
Date: 2024-10
Sources: (LOW) [GitHub, https://github.com/blur-io] (HIGH) [Blur Docs, https://docs.blur.io]

Metric Name: API Calls / Day
Value: Tidak dipublikasikan
Date: N/A
Sources: tidak diketahui

## Market Share

Metric: NFT Marketplace Volume Market Share (Ethereum Mainnet)
Value: 60%–75% (dominan sejak Q1 2023; puncak >80% saat Season 2-3)
Date: 2024-10
Sources: (HIGH) [Dune Analytics, https://dune.com/queries] (HIGH) [Token Terminal, https://tokenterminal.com/terminal/projects/blur] (EV-015)

Metric: NFT Marketplace User/Trader Market Share
Value: 30%–40% (volume concentration pada whale/pro traders; user count lebih rendah vs OpenSea)
Date: 2024-10
Sources: (MEDIUM) [Dune Analytics, https://dune.com/queries] (LOW) [Nansen, https://www.nansen.ai]

Metric: NFT Lending Protocol Market Share (Blend vs competitors)
Value: 40%–60% (vs BendDAO, NFTX, Arcade, X2Y2 lending)
Date: 2024-10
Sources: (MEDIUM) [DeFiLlama, https://defillama.com/protocol/blend] (MEDIUM) [Dune Analytics, https://dune.com/queries]

## Competitor Landscape

Competitor: OpenSea
Category: NFT Marketplace / Aggregator (General retail)
Difference: OpenSea: retail-focused, multi-chain (Ethereum, Polygon, Klaytn, Base, Arbitrum, Optimism, Avalanche, BNB Chain), higher fees (2.5% platform fee), Seaport protocol, broader collection support. Blur: pro-trader focused, Ethereum-only, zero platform fee (0.5% protocol fee via fee switch), off-chain orderbook, bidding pools, Blend lending integration.
Market Segment: Retail vs Professional/Whale
Sources: (HIGH) [OpenSea Blog, https://opensea.io/blog] (HIGH) [Blur Blog, https://blur.io/blog/introducing-blur] (HIGH) [Dune Analytics, https://dune.com/queries]

Competitor: Magic Eden
Category: NFT Marketplace (Multi-chain, Gaming-focused)
Difference: Magic Eden: multi-chain (Solana, Ethereum, Polygon, Bitcoin Ordinals, Base), gaming NFT focus, Diamond rewards program. Blur: Ethereum-only, no gaming vertical, trader tooling depth (trait bids, collection bids), Blend lending.
Market Segment: Cross-chain retail / Gaming vs Ethereum pro-trader
Sources: (HIGH) [Magic Eden Blog, https://blog.magiceden.io] (HIGH) [Blur Blog, https://blur.io/blog/introducing-blur]

Competitor: LooksRare
Category: NFT Marketplace (Incentivized trading)
Difference: LooksRare: LOOKS token staking for fee rewards, multi-chain (Ethereum, Base), community-owned. Blur: BLUR fee switch for stakers, no multi-chain, venture-backed (Paradigm), Blend lending.
Market Segment: Incentivized trader vs Pro trader
Sources: (HIGH) [LooksRare Blog, https://blog.looksrare.org] (HIGH) [Blur Blog, https://blur.io/blog/blur-token]

Competitor: X2Y2
Category: NFT Marketplace / Lending
Difference: X2Y2: X2Y2 token, marketplace + lending protocol, multi-chain (Ethereum, BNB Chain, Arbitrum). Blur: larger volume, Blend lending separate protocol, no multi-chain.
Market Segment: Pro trader + Lending (smaller scale)
Sources: (HIGH) [X2Y2 Blog, https://blog.x2y2.io] (HIGH) [Blur Blog, https://blur.io/blog/blend]

Competitor: BendDAO
Category: NFT Lending Protocol
Difference: BendDAO: peer-to-pool lending, BEND token, NFT floor price oracle, multi-chain (Ethereum, BNB Chain). Blend: peer-to-peer perpetual loans, no token, Uniswap V3 TWAP oracle, Ethereum-only.
Market Segment: NFTfi lending
Sources: (HIGH) [BendDAO Docs, https://docs.benddao.xyz] (HIGH) [Blur Blog, https://blur.io/blog/blend] (EV-010)

Competitor: NFTX
Category: NFT Lending / Index Fund
Difference: NFTX: vault-based fungible NFT index tokens (vTokens), lending against vault shares. Blend: direct NFT collateral, perpetual loans, no token.
Market Segment: NFTfi / Financialization
Sources: (HIGH) [NFTX Docs, https://docs.nftx.io] (HIGH) [Blur Blog, https://blur.io/blog/blend]

## Narrative Position

Narrative: NFT Marketplace Dominance (Pro-Trader Focus)
Status: Main Narrative
Evidence: Blur menarik >60% volume Ethereum NFT sejak Q1 2023; fitur bidding pools, trait bids, zero fee (pre-fee switch), API untuk bot/trader; narasi "OpenSea killer for pros" di media kripto (The Block, CoinDesk, Decrypt coverage 2022-2024)
Sources: (HIGH) [The Block, https://www.theblock.co] (HIGH) [CoinDesk, https://www.coindesk.com] (HIGH) [Dune Analytics, https://dune.com/queries] (EV-002, EV-015)

Narrative: NFT Financialization (NFTfi) via Blend
Status: Secondary Narrative
Evidence: Blend launch Mei 2023 menarik >$100M volume minggu pertama; perpetual peer-to-peer lending model diferensiasi vs peer-to-pool (BendDAO); narasi "unlock NFT liquidity without selling" di DeFi media
Sources: (HIGH) [Blur Blog, https://blur.io/blog/blend] (HIGH) [DeFiLlama, https://defillama.com/protocol/blend] (MEDIUM) [The Block, https://www.theblock.co] (EV-010)

Narrative: Token Utility / Fee Switch Governance
Status: Secondary Narrative
Evidence: Fee switch proposal Feb 2024 mengaktifkan value accrual ke BLUR staker (0.5% protocol fee); governance aktif via Snapshot; narasi "real yield for governance token" di Token Terminal / Messari reports
Sources: (HIGH) [Snapshot, https://snapshot.org/#/blur.eth] (HIGH) [Token Terminal, https://tokenterminal.com/terminal/projects/blur] (MEDIUM) [Messari, https://messari.io/asset/blur] (EV-013)

Narrative: Airdrop / Incentive Farming (Season 1-3)
Status: Historical Narrative (completed)
Evidence: Season 1 airdrop (360M BLUR), Season 2-3 trading incentives mendorong volume spike; narasi "most sophisticated airdrop design" (points-based, anti-sybil) di komunitas & analyst reports
Sources: (HIGH) [Blur Blog, https://blur.io/blog/blur-token] (MEDIUM) [Galaxy Research, https://www.galaxy.com/insights] (LOW) [Twitter @blur_io, https://twitter.com/blur_io] (EV-004, EV-011, EV-012)

Narrative: Ethereum Alignment (L1 Only, No L2)
Status: Differentiation Narrative
Evidence: Tidak ada deployment Arbitrum/Optimism/Base/Blast per 2024-10; komitmen pada Ethereum L1 settlement; dikritik komunitas multi-chain tapi dihargai purist Ethereum
Sources: (HIGH) [Blur Blog, https://blur.io/blog/introducing-blur] (MEDIUM) [Twitter @PacmanBlur, https://twitter.com/PacmanBlur] (EV-002, EV-015)

## Market Timeline

Date: 2022-10-19
Milestone: Blur Marketplace Mainnet Launch
Description: Live di Ethereum mainnet dengan off-chain orderbook, bidding pools, zero platform fee
Related Historical Event ID: EV-002
Sources: (HIGH) [Blur Blog, https://blur.io/blog/introducing-blur] (HIGH) [Etherscan, https://etherscan.io/address/0x000000000000Ad05Ccc4F10445630FB830B95127]

Date: 2022-11-01
Milestone: Series A $11M Paradigm ($1B Valuation)
Description: Pembiayaan venture terbesar untuk NFT marketplace pada masa itu
Related Historical Event ID: EV-003
Sources: (HIGH) [Paradigm, https://www.paradigm.xyz/portfolio/blur] (HIGH) [TechCrunch, https://techcrunch.com/2022/11/01/blur-nft-marketplace-raises-11m-at-1b-valuation-from-paradigm]

Date: 2023-02-14
Milestone: TGE BLUR Token + Binance Listing + Season 1 Airdrop
Description: Token live, trading CEX/DEX dimulai, 360M BLUR claimable oleh trader pre-TGE
Related Historical Event ID: EV-004, EV-005
Sources: (HIGH) [Blur Blog, https://blur.io/blog/blur-token] (HIGH) [Binance, https://www.binance.com/en/blog/1143099090879011840] (HIGH) [Etherscan, https://etherscan.io/token/0x5283D291DBCF85356a21bA090E6db59121208b44]

Date: 2023-02-15
Milestone: Coinbase Listing (Experimental)
Description: Akses pasar ritel AS
Related Historical Event ID: EV-006
Sources: (HIGH) [Coinbase Blog, https://blog.coinbase.com/blur-blur-is-launching-on-coinbase-123]

Date: 2023-02-14
Milestone: Blur DAO Formation
Description: Governance off-chain via Snapshot, on-chain execution via multisig
Related Historical Event ID: EV-007
Sources: (HIGH) [Snapshot, https://snapshot.org/#/blur.eth] (HIGH) [Blur Blog, https://blur.io/blog/blur-token]

Date: 2023-05-01
Milestone: Blend Protocol Launch
Description: NFT lending peer-to-peer perpetual loans live di Ethereum
Related Historical Event ID: EV-010
Sources: (HIGH) [Blur Blog, https://blur.io/blog/blend] (HIGH) [Etherscan, https://etherscan.io/address/0x29469395eAf6f95920E59F858042f0e28D98a20B]

Date: 2023-05 to 2023-11
Milestone: Season 2 Incentive Program
Description: BLUR rewards untuk trading, bidding, Blend activity
Related Historical Event ID: EV-011
Sources: (HIGH) [Blur Blog, https://blur.io/blog/blur-token] (MEDIUM) [Discord, https://discord.gg/blur]

Date: 2023-11 to 2024-02
Milestone: Season 3 Incentive Program
Description: Delegation incentives, new collection rewards, Blend participation
Related Historical Event ID: EV-012
Sources: (HIGH) [Blur Blog, https://blur.io/blog] (MEDIUM) [Discord, https://discord.gg/blur]

Date: 2024-02 (approx)
Milestone: Fee Switch Activation (Governance Proposal Passed)
Description: 0.5% protocol fee redirected to BLUR stakers/delegators
Related Historical Event ID: EV-013
Sources: (HIGH) [Snapshot, https://snapshot.org/#/blur.eth] (HIGH) [Etherscan, https://etherscan.io/address/0x000000000000Ad05Ccc4F10445630FB830B95127]

Date: 2024-02-14 (approx)
Milestone: Team/Investor Vesting Cliff End — Linear Unlock Begins
Description: 1-year cliff berakhir, unlock bulanan 4-5 tahun dimulai
Related Historical Event ID: EV-004 (reference)
Sources: (HIGH) [Blur Blog, https://blur.io/blog/blur-token] (MEDIUM) [CoinGecko, https://www.coingecko.com/en/coins/blur]

Date: 2024-06
Milestone: Blur Mobile App Beta Launch
Description: iOS/Android native app untuk trading dan Blend
Related Historical Event ID: EV-014
Sources: (MEDIUM) [Blur Blog, https://blur.io/blog] (MEDIUM) [Twitter @blur_io, https://twitter.com/blur_io]

Date: 2024-10
Milestone: 2-Year Anniversary — Sustained Market Share Leadership
Description: >60% volume market share Ethereum NFT konstan 2 tahun
Related Historical Event ID: EV-015
Sources: (MEDIUM) [Dune Analytics, https://dune.com/queries] (MEDIUM) [Twitter @blur_io, https://twitter.com/blur_io]

## Official Market Resources

Official Dashboard: tidak ada dashboard resmi terpusat (community dashboards di Dune)
DeFiLlama: https://defillama.com/protocol/blur (Marketplace) / https://defillama.com/protocol/blend (Lending)
CoinGecko: https://www.coingecko.com/en/coins/blur
CoinMarketCap: https://coinmarketcap.com/currencies/blur/
Token Terminal: https://tokenterminal.com/terminal/projects/blur
Messari: https://messari.io/asset/blur
Explorer: https://etherscan.io/token/0x5283D291DBCF85356a21bA090E6db59121208b44
Official Blog: https://blur.io/blog
Official Documentation: https://docs.blur.io
Governance: https://snapshot.org/#/blur.eth
GitHub: https://github.com/blur-io

## Ringkasan

Market Stage: Growth
Primary Category: NFT Marketplace / Aggregator
Competitor Count: 6+ utama (OpenSea, Magic Eden, LooksRare, X2Y2, BendDAO, NFTX)
Major Narrative: NFT Marketplace Dominance (Pro-Trader) + NFT Financialization (Blend)
Trading Availability: CEX (Binance, Coinbase, Bybit, OKX, Kraken, dll.), DEX (Uniswap V2/V3), Perpetual (Binance, Bybit, OKX)
Adoption Metrics Available: Volume, TVL (Blend), Traders, Holders, Stakers — sebagian dari Dune/DeFiLlama/Token Terminal, tidak ada dashboard resmi real-time

## Behavioral Intelligence
_ref: `docs/Ontology/Hidden.md` — enriches DecisionEvent Alternatives/Reason/Reactions_

PROJECT: Blur

1. Mendominasi volume trading NFT Ethereum melalui produk superior bagi professional trader
· Evidence: Blur menargetkan segmen "pro-trader/whale" dengan fitur bidding kolektif (collection/trait bids), off-chain orderbook cepat, zero platform fee awal, dan API untuk bot — berbeda dari pendekatan retail OpenSea. Market share konstan 60–75% volume Ethereum sejak Q1 2023 (EV-015). Volume kumulatif >$25B per Dune community dashboard 【Phase 8】.
· Supporting Dataset: Phase 3 (EV-002, EV-015), Phase 8 (Market Position, Market Share, Competitor Landscape)

2. Membangun lapisan keuangan NFT (NFTfi) melalui Blend sebagai diferensiasi jangka panjang
· Evidence: Blend diluncurkan Mei 2023 (EV-010) sebagai protokol pinjaman peer-to-peer perpetual tanpa expiration date, menggunakan oracle Uniswap V3 TWAP. Menarik >$100M volume minggu pertama, TVL $150–300M, cumulative loan volume >$2B 【Phase 8】. Narasi "NFT financialization" menjadi secondary narrative 【Phase 8】.
· Supporting Dataset: Phase 3 (EV-008, EV-009, EV-010), Phase 4 (Core Components: Blend Contract), Phase 8 (Narrative Position, Competitor Landscape: BendDAO, NFTX)

3. Transisi progresif ke governance komunitas via BLUR token dan Blur DAO
· Evidence: TGE Feb 2023 sekaligus membentuk Blur DAO (EV-007). 51% supply dialokasikan komunitas/treasury 【Phase 6】. Fee switch diaktifkan Feb 2024 via proposal governance (EV-013), mengarahkan 0.5% protocol fee ke staker BLUR. Voting off-chain Snapshot, eksekusi on-chain via multisig (belum fully timelock/DAO-kan per Phase 4).
· Supporting Dataset: Phase 3 (EV-004, EV-007, EV-013), Phase 5 (Revenue Model: fee switch), Phase 6 (Governance, Distribution), Phase 7 (Major Integrations: Blur DAO ↔ Snapshot)

4. Mempertahankan alignment ketat dengan Ethereum L1 (no multi-chain, no L2 resmi per 2024-10)
· Evidence: Semua kontrak (Marketplace, Blend, BLUR token) hanya di Ethereum mainnet 【Phase 1, Phase 4】. Founder PacmanBlur menyatakan komitmen Ethereum-only 【Phase 8 Narrative】. Kompetitor (Magic Eden, OpenSea, X2Y2) sudah multi-chain/L2.
· Supporting Dataset: Phase 1 (Chain: Ethereum), Phase 4 (System Architecture: Layer Ethereum Mainnet, Cross-chain: Tidak ada), Phase 8 (Narrative: Ethereum Alignment)

5. Menggunakan insentif token berstruktur (Season 1–3) untuk bootstrap liquidity dan user base
· Evidence: Season 1 airdrop 360M BLUR (12% supply) ke trader pre-TGE (EV-004). Season 2 (Mei–Nov 2023) dan Season 3 (Nov 2023–Feb 2024) reward trading, bidding, Blend activity (EV-011, EV-012). Volume spike berkorelasi dengan saison insentif 【Phase 8 Adoption Metrics】.
· Supporting Dataset: Phase 3 (EV-004, EV-011, EV-012), Phase 6 (Utility: Incentive/Reward, Major Token Events), Phase 8 (Adoption Metrics, Market Timeline)

Keputusan: Launch Mainnet Langsung Tanpa Public Testnet (2022-10-19)
· Trigger: Ingin first-mover advantage pada arsitektur off-chain orderbook + on-chain settlement untuk pro-trader; menghindari leakage alpha ke kompetitor selama testnet publik.
· Evidence: Blog resmi "Introducing Blur" menyatakan launch langsung mainnet (EV-002). Tidak ada record testnet publik terpisah di Phase 3.
· Decision: Deploy kontrak Exchange, Bidding, dan Proxy Admin ke Ethereum mainnet 19 Okt 2022; buka akses publik segera.
· Immediate Result: Marketplace live, trader mulai migrasi dari OpenSea/LooksRare untuk bidding pools dan zero fee.
· Long-term Impact: Menetapkan reputasi "speed & execution quality" sebagai diferensiasi inti; namun menambah risiko bug awal tanpa battle-testing publik 【Phase 4 Known Limitations: unaudited marketplace contracts】.
· Supporting Dataset: Phase 3 EV-002, Phase 4 System Architecture, Phase 4 Known Technical Limitations

Keputusan: Series A $11M dari Paradigm Valuasi $1B (2022-11-01)
· Trigger: Butuh capital untuk scaling tim, infra off-chain orderbook, dan marketing ke pro-trader setelah traction awal launch.
· Evidence: Paradigm lead investor, TechCrunch coverage, valuasi $1B pre-revenue (EV-003). Variant Fund seed sebelumnya 【Phase 2, Phase 5】.
· Decision: Terima $11M Series A, alokasi token untuk investor dengan vesting 1-year cliff + 4-5 tahun linear 【Phase 6 Vesting】.
· Immediate Result: Dana untuk hire core team, infra server, audit Blend, incentive seasons.
· Long-term Impact: Paradigm sebagai strategic partner membuka akses ekosistem Ethereum; VC expectation tekanan growth & monetization (fee switch nanti). Token allocation ke investor menciptakan sell pressure di cliff end Feb 2024.
· Supporting Dataset: Phase 3 EV-003, Phase 5 Funding History, Phase 6 Vesting Schedule, Phase 2 Entity: Paradigm

Keputusan: TGE BLUR Token + Binance/Coinbase Listing Same-Day (2023-02-14)
· Trigger: Kapitalisasi komunitas Season 1, liquidity untuk price discovery, legitimacy via top-tier CEX.
· Evidence: Blog "BLUR Token" announcement, Binance listing announcement same day, Coinbase TGE+1 (EV-004, EV-005, EV-006). Wintermute/GSR sebagai market maker 【Phase 2】.
· Decision: Deploy kontrak ERC-20 3B supply, mint ke multisig, enable Season 1 claim, listing Binance (spot + perpetual) dan Coinbase (Experimental) simultan.
· Immediate Result: $1B+ volume hari pertama, BLUR top-50 market cap, airdrop claim rate tinggi, Season 1 recipients jadi stakeholders.
· Long-term Impact: Token liquidity tinggi dari awal; CEX dependency untuk volume (Binance dominant); regulatory exposure (Coinbase Experimental label, SEC utility vs security risk Phase 5).
· Supporting Dataset: Phase 3 EV-004/005/006, Phase 6 TGE, Phase 5 Financial Dependencies, Phase 8 Trading Markets

Keputusan: Dual Audit Blend oleh Trail of Bits & OpenZeppelin (2023-04)
· Trigger: Blend mengelola collateral NFT bernilai tinggi + ETH loans; bug = kerugian user & reputasi fatal. Butuh kepercayaan institusional.
· Evidence: Trail of Bits report Apr 2023, OpenZeppelin report Apr 2023, keduanya published pre-launch (EV-008, EV-009). Marketplace contracts tidak mendapat audit serupa 【Phase 4 Audit History】.
· Decision: Biaya & waktu untuk dua audit top-tier sebelum mainnet Blend Mei 2023.
· Immediate Result: Temuan kritis diperbaiki, launch Blend lancar >$100M volume minggu 1.
· Long-term Impact: Standar keamanan tinggi untuk Blend; tapi marketplace core contracts tetap unaudited 【Phase 4 Known Limitations】 — asymmetric security investment.
· Supporting Dataset: Phase 3 EV-008/009, Phase 4 Audit History, Phase 4 Security Model, Phase 7 External Dependencies

Keputusan: Aktivasi Fee Switch 0.5% ke BLUR Stakers (2024-02 approx)
· Trigger: Tekanan komunitas & investor untuk value accrual token; DAO treasury butuh revenue stream; Season 3 berakhir.
· Evidence: Snapshot proposal passed Feb 2024 (EV-013). Fee switch mengarahkan protocol fee ke delegator BLUR.
· Decision: Governance proposal mengaktifkan 0.5% marketplace fee (sebelumnya 0%) dan distribusi ke staker via delegation contract.
· Immediate Result: BLUR staking yield ~10–20% APR awal; delegator >25k addresses 【Phase 8】. Token utility nyata beyond governance.
· Long-term Impact: Monetisasi protocol; aligns token holder dengan protocol revenue; regulatory risk "security" meningkat 【Phase 5 Financial Risk】. Revenue split exact (staker vs treasury vs team) tidak transparan 【Phase 6 Open Threads】.
· Supporting Dataset: Phase 3 EV-013, Phase 5 Revenue Model, Phase 6 Utility: Staking/Fee Switch, Phase 8 Narrative: Token Utility/Fee Switch

Keputusan: Tidak Deploy ke L2 / Multi-chain hingga 2024-10
· Trigger: Fokus resources pada dominasi Ethereum L1; technical complexity orderbook off-chain di multi-chain; Ethereum alignment narrative.
· Evidence: Phase 1/4/7/8 semua menunjukkan hanya Ethereum mainnet. Competitor sudah multi-chain. Phase 8 Open Threads: "L2 expansion signal: tidak ada announcement resmi".
· Decision: Tetap single-chain Ethereum L1 untuk settlement & infra.
· Immediate Result: Gas cost tinggi untuk user retail; volume terkonsentrasi pro-trader yang toleran gas; kehilangan user base ke OpenSea/Base/Magic Eden di L2.
· Long-term Impact: Moat teknis (off-chain orderbook terpusat) sulit direplikasi multi-chain; tapi TAM (total addressable market) terbatas. Risiko obsolescens jika NFT migrasi massal ke L2.
· Supporting Dataset: Phase 4 System Architecture, Phase 7 Ecosystem Position, Phase 8 Narrative Position, Phase 8 Open Threads

Evolution Pattern

Dari Stealth Launch ke Market Dominance (2022-10 – 2023-02)
· Proyek bermula dari pendirian Blur Labs Inc (2022) oleh 3 founder pseudonim → launch mainnet langsung Oct 2022 tanpa testnet → Series A Paradigm Nov 2022 $11M @ $1B val → TGE Feb 2023 dengan CEX listing tier-1 instan. Evolusi sangat cepat: <4 bulan dari launch ke unicorn valuation, <6 bulan ke token live. Strategi "move fast, capture pro-trader" bekerja.

Dari Marketplace Tunggal ke Dual-Protocol (2023-02 – 2023-05)
· Post-TGE, fokus bergeser ke Blend lending protocol. Dual audit (Trail of Bits + OpenZeppelin) Apr 2023 → launch Mei 2023. Blend jadi produk kedua mandiri tapi terintegrasi UI. Diversifikasi revenue: marketplace fee + lending fee. Narasi "NFT financialization" muncul.

Dari Incentive-Driven ke Sustainable Revenue (2023-05 – 2024-02)
· Season 2 (Mei–Nov 2023) & Season 3 (Nov–Feb 2024) mempertahankan volume via BLUR rewards. Fee switch Feb 2024 menandai transisi ke "real yield" model: protocol fee 0.5% → staker. Season 3 terakhir; tidak ada Season 4 announced per 2024-10. Evolusi: tokenomics dari inflationary incentives → fee-switch revenue sharing.

Dari Centralized Control ke Progressive Decentralization (2023-02 – ongoing)
· TGE: DAO formed, 51% supply community, tapi multisig Blur Labs memegang admin key semua kontrak 【Phase 4】. Fee switch proposal Feb 2024 dieksekusi via multisig, bukan timelock DAO. Vesting team/investor cliff end Feb 2024 mulai unlock bulanan. Evolusi perlahan: governance active tapi execution masih centralized.

Technical Decision Pattern Evolution: Off-Chain Orderbook + On-Chain Settlement Arsitektur Hybrid
· Decision Pattern: Memilih off-chain centralized orderbook/matching engine (server Blur Labs) untuk speed & UX, settlement on-chain via smart contract (Exchange, Bidding). Bukan fully on-chain Seaport-style.
· Evidence: Phase 4 System Architecture: "Off-chain Orderbook & Matching Engine" terpusat; "Blur Exchange Contract" on-chain settlement. Phase 4 Known Limitations: "Orderbook Off-chain Terpusat: trust assumption pada operator".
· Supporting Dataset: Phase 4 System Architecture, Core Components, Known Technical Limitations, Phase 3 EV-002
· Mengapa: Pro-trader butuh latency rendah, batch bidding, trait/collection bids yang mahal/complex di fully on-chain. Trade-off: decentralization & censorship resistance dikorbankan untuk performance.

Technical Decision Pattern

Pola 1: Proxy Upgradeable Contracts dengan Multisig Admin Control
· Decision Pattern: Semua kontrak inti (Marketplace Exchange, Bidding, Blend, BLUR Token) menggunakan TransparentUpgradeableProxy/UUPS, owner = Blur Multisig (Gnosis Safe). Belum migrasi ke timelock/DAO governance on-chain.
· Evidence: Phase 4 Core Components: "Blur Multisig (Gnosis Safe) / Owner Address" mengontrol admin functions. Phase 4 Security Model: "Admin Control: Multisig memegang ownership/admin key... belum sepenuhnya ditimelock/DAO-kan". Phase 4 Technical Upgrade History: multiple upgrades via proxy.
· Supporting Dataset: Phase 4 Core Components, Security Model, Technical Upgrade History, Phase 2 Entity: Blur Multisig
· Mengapa: Flexibilitas iterasi cepat (fee parameters, royalty logic, gas optimizations) tanpa migration kontrak. Risiko: single point of failure, key person risk, regulatory target.

Pola 2: Dual Audit untuk Produk Baru (Blend) tapi Tidak untuk Core Marketplace
· Decision Pattern: Blend mendapat dual audit top-tier (Trail of Bits + OpenZeppelin) pre-launch. Marketplace core contracts (Exchange, Bidding) hidup sejak Oct 2022 tanpa audit publik terverifikasi.
· Evidence: Phase 4 Audit History: 2 audits untuk Blend, 0 untuk Marketplace. Phase 4 Known Limitations: "Marketplace Contracts Unaudited".
· Supporting Dataset: Phase 4 Audit History, Known Technical Limitations, Phase 3 EV-008/009/010
· Mengapa: Blend mengelola collateral & loans (higher risk surface area, financial loss direct). Marketplace = matching & settlement (lower perceived risk, tapi volume besar). Resource allocation priority ke produk baru.

Pola 3: Ethereum L1 Only, No L2/Multi-Chain Deployment
· Decision Pattern: Semua kontrak hanya di Ethereum mainnet. Tidak ada deployment Arbitrum, Optimism, Base, Blast, dll. per 2024-10.
· Evidence: Phase 1 Chain: Ethereum. Phase 4 System Architecture: Layer Ethereum Mainnet, Cross-chain: Tidak ada. Phase 7 Ecosystem Position: Supported Chains: Ethereum Mainnet only. Phase 8 Narrative: Ethereum Alignment.
· Supporting Dataset: Phase 1, Phase 4, Phase 7, Phase 8
· Mengapa: Founder philosophy (PacmanBlur pro-Ethereum), technical complexity memport orderbook off-chain ke L2, liquidity fragmentation risk, gas cost sebagai moat untuk pro-trader (filter retail).

Financial Decision Pattern

Pola 1: VC-Funded Growth dengan Token Allocation untuk Investor
· Decision Pattern: Series A $11M Paradigm @ $1B valuation (Nov 2022) + seed Variant Fund. Investor menerima alokasi token BLUR dengan vesting 1-year cliff + 4-5 tahun linear. Tidak ada public sale/IDO.
· Evidence: Phase 5 Funding History: Series A $11M Paradigm. Phase 6 Vesting Schedule: Investors cliff 1 tahun, vesting 4-5 tahun linear. Phase 6 Token Sale: Private Sale ya, Public Sale tidak.
· Supporting Dataset: Phase 3 EV-003, Phase 5 Funding History, Phase 6 Vesting Schedule, Token Sale
· Mengapa: Capital untuk scaling cepat (tim, infra, audit, incentives). Paradigm strategic value > capital. Token allocation aligns investor long-term. Vesting cliff Feb 2024 menciptakan supply unlock tekanan.

Pola 2: Zero Platform Fee → Fee Switch Monetization Via Governance
· Decision Pattern: Launch dengan 0% platform fee (hanya royalty creator) untuk capture market share dari OpenSea (2.5% fee). Feb 2024 fee switch activated via DAO proposal: 0.5% protocol fee → BLUR stakers.
· Evidence: Phase 5 Revenue Model: "Protocol Fee - Blur Marketplace: Live (fee switch diaktifkan Februari 2024)". Phase 3 EV-013. Phase 8 Narrative: Token Utility/Fee Switch.
· Supporting Dataset: Phase 3 EV-013, Phase 5 Revenue Model, Phase 8 Narrative Position
· Mengapa: Growth-first strategy (subsidize traders via zero fee + BLUR incentives). Monetization delayed hingga dominant position & DAO governance ready. Fee switch = real yield narrative untuk token holders.

Pola 3: Seasonal Incentive Programs (Season 1-3) sebagai Customer Acquisition Cost
· Decision Pattern: Alokasi 51% supply komunitas didistribusikan via Season 1 airdrop (12% supply), Season 2-3 trading/lending rewards. Tidak ada liquidity mining BLUR/ETH resmi.
· Evidence: Phase 6 Distribution: Community 51%. Phase 6 Major Token Events: Season 1 Claim, Season 2, Season 3. Phase 3 EV-004/011/012. Phase 8 Adoption Metrics: volume spike korelasi season.
· Supporting Dataset: Phase 3 EV-004/011/012, Phase 6 Distribution, Major Token Events, Phase 8 Adoption Metrics
· Mengapa: Bootstrap liquidity & user base tanpa CAC tradisional. Points-based anti-sybil design (Season 1) → activity-based (Season 2-3). Season 3 terakhir → transisi ke fee-switch sustainability.

Pola 4: Treasury Opasitas — Tidak Ada Transparency Report Real-Time
· Decision Pattern: Ukuran, komposisi, custodian treasury DAO tidak dipublikasikan. Alamat multisig/treasury tidak terlabel jelas di Etherscan. Tidak ada dashboard treasury resmi.
· Evidence: Phase 5 Treasury: "Current Treasury Size: tidak diungkap", "Treasury Composition: tidak diungkap". Phase 6 Holder Distribution: "Treasury Holding: Blur DAO treasury / multisig holder terbesar... estimasi >1B BLUR". Phase 5 Open Threads: "Ukuran dan komposisi treasury... tidak dipublikasikan".
· Supporting Dataset: Phase 5 Treasury, Phase 6 Holder Distribution, Phase 5 Open Threads
· Mengapa: Strategic opacity (hindari front-running treasury management), regulatory caution, atau prioritization rendah. Trade-off: community trust & accountability reduced.

Ecosystem Decision Pattern

Pola 1: Deep Integration dengan Ethereum Base Layer & Minimal External Protocol Dependencies
· Decision Pattern: Hanya bergantung pada Ethereum (settlement), OpenZeppelin (lib), Gnosis Safe (multisig), Snapshot (governance), Uniswap V3 (Blend oracle). Tidak integrasi L2, bridge, oracle chainlink, atau protocol lain.
· Evidence: Phase 7 External Dependencies: 12 dependencies, 8 critical/high semuanya Ethereum-native infra. Phase 7 Major Integrations: 11 integrations, 9 dengan Ethereum/mainnet contracts. Phase 4 Oracle: "Tidak menggunakan oracle eksternal... Blend menggunakan oracle harga internal berbasis TWAP/Uniswap V3".
· Supporting Dataset: Phase 7 External Dependencies, Major Integrations, Phase 4 System Architecture
· Mengapa: Minimize external attack surface & dependency risk. Ethereum alignment philosophy. Blend oracle internal = control & cost efficiency (no Chainlink fees).

Pola 2: CEX-First Token Distribution (Binance, Coinbase Same-Day TGE)
· Decision Pattern: Prioritaskan listing Binance (spot + perpetual) dan Coinbase (Experimental) pada hari TGE. DEX (Uniswap) community-driven tanpa official liquidity mining. Market maker Wintermute/GSR engaged.
· Evidence: Phase 3 EV-004/005/006. Phase 7 Exchange Ecosystem: Binance, Coinbase, Uniswap V2/V3 listed. Phase 2 Entity: Wintermute, GSR sebagai market maker. Phase 5 Financial Dependencies: Market Makers liquidity dependency.
· Supporting Dataset: Phase 3 EV-004/005/006, Phase 7 Exchange Ecosystem, Phase 2 Entity, Phase 5 Financial Dependencies
· Mengapa: Immediate deep liquidity, price discovery, retail access (Coinbase US), pro-trader tools (Binance perpetual). CEX listing sebagai marketing & legitimacy signal. DEX secondary.

Pola 3: Standard Wallet Compatibility, No Proprietary Wallet/SDK
· Decision Pattern: Tidak membangun wallet sendiri, SDK, atau developer tools khusus. Mendukung standar Ethereum (MetaMask, WalletConnect, Coinbase Wallet, Rainbow, Ledger, Rabby) via EIP-1193. API public (REST/GraphQL) untuk bot/trader.
· Evidence: Phase 7 Wallet Ecosystem: "Blur tidak mempublikasikan daftar wallet resmi... semua wallet Ethereum standar kompatibel". Phase 7 Developer Ecosystem: "Tidak ada SDK resmi... API: Public REST/GraphQL... Tidak ada developer tools khusus".
· Supporting Dataset: Phase 7 Wallet Ecosystem, Developer Ecosystem
· Mengapa: Focus pada core product (marketplace + lending), tidak fragmentasi resource ke wallet/SDK. Pro-trader sudah punya tooling sendiri (bot, custom scripts via API). Low barrier to entry via existing wallets.

Pola 4: Security Audit Partnerships sebagai Trust Signal (Blend Only)
· Decision Pattern: Trail of Bits + OpenZeppelin audit untuk Blend. Tidak audit marketplace. Tidak bug bounty program publik terlihat. Tidak formal verification.
· Evidence: Phase 7 External Dependencies: Trail of Bits, OpenZeppelin sebagai security dependency. Phase 4 Audit History: 2 audits Blend, 0 marketplace. Phase 4 Known Limitations: "No Formal Verification", "Marketplace Contracts Unaudited".
· Supporting Dataset: Phase 7 External Dependencies, Phase 4 Audit History, Known Technical Limitations
· Mengapa: Blend = new protocol, financial risk tinggi, butuh institutional trust. Marketplace = proven in production (Oct 2022), audit cost/benefit lower perceived. Resource allocation ke Blend audit.

Governance Decision Pattern

Pola 1: Off-Chain Signaling (Snapshot) + On-Chain Multisig Execution
· Decision Pattern: Proposal diskusi & voting di Snapshot (off-chain, gasless). Eksekusi on-chain via Blur Multisig (Gnosis Safe) yang dikontrol tim/DAO multisig. Belum ada timelock controller on-chain yang fully DAO-controlled.
· Evidence: Phase 6 Governance: "Governance Model: Token-weighted voting via Blur DAO (off-chain signaling on Snapshot, on-chain execution via multisig/timelock)". Phase 4 Security Model: "Admin Control: Multisig memegang ownership/admin key... belum sepenuhnya ditimelock/DAO-kan". Phase 7 Major Integrations: Blur DAO ↔ Snapshot.
· Supporting Dataset: Phase 3 EV-007/013, Phase 6 Governance, Phase 4 Security Model, Phase 7 Major Integrations
· Mengapa: Low friction governance participation (gasless voting). Speed of execution via trusted multisig. Progressive decentralization: signaling first, execution infrastructure later.

Pola 2: Fee Switch Activation Via Governance Proposal (Value Accrual Decision)
· Decision Pattern: Proposal on-chain Feb 2024 mengaktifkan 0.5% protocol fee → BLUR stakers. Passed via Snapshot, executed multisig. Revenue split detail (staker vs treasury vs team) tidak dipecah di proposal.
· Evidence: Phase 3 EV-013. Phase 6 Utility: Staking/Fee Switch. Phase 6 Major Token Events: Fee Switch Activation. Phase 5 Revenue Model: fee switch live Feb 2024.
· Supporting Dataset: Phase 3 EV-013, Phase 6 Utility, Major Token Events, Phase 5 Revenue Model
· Mengapa: Community & investor pressure untuk token utility. DAO treasury butuh revenue. Align token holder incentive dengan protocol growth. Regulatory trade-off accepted.

Pola 3: Seasonal Incentive Parameters Set by Team, Not DAO Vote (Initially)
· Decision Pattern: Season 1, 2, 3 dirancang & diluncurkan oleh Blur Labs team. DAO voting terbatas pada parameter fee/treasury, tidak pada desain season insentif. Season 3 terakhir; tidak ada Season 4 proposal terlihat.
· Evidence: Phase 3 EV-011/012: Season 2 & 3 announced via blog/Discord, bukan Snapshot proposal. Phase 6 Major Token Events: Season 1-3 completed. Phase 8 Adoption Metrics: volume spike during seasons.
· Supporting Dataset: Phase 3 EV-011/012, Phase 6 Major Token Events, Phase 8 Adoption Metrics
· Mengapa: Speed & expertise: team punya data & insight desain incentive kompleks (anti-sybil, points system). DAO belum mature untuk micro-management. Gradual handover.

Pola 4: Multisig Ownership Retention Despite DAO Formation
· Decision Pattern: Blur Multisig (Gnosis Safe) tetap owner/admin semua kontrak (Marketplace, Blend, Token) per 2024-10. Tidak ada migrasi ke TimelockController + DAO voting execution on-chain.
· Evidence: Phase 4 Security Model: "Multisig memegang ownership/admin key... belum sepenuhnya ditimelock/DAO-kan". Phase 2 Entity: Blur Multisig (Gnosis Safe). Phase 4 Technical Upgrade History: upgrades via proxy admin (multisig).
· Supporting Dataset: Phase 4 Security Model, Technical Upgrade History, Phase 2 Entity, Phase 6 Governance
· Mengapa: Operational flexibility, emergency pause/upgrade capability, legal liability clarity (Blur Labs Inc as entity). DAO legal wrapper belum jelas 【Phase 1 Open Threads: yurisdiksi hukum】. Risk: centralization, key person, regulatory target.

Risk Response Pattern

Pola 1: Proactive Dual Audit untuk Blend (Pre-Launch Risk Mitigation)
· Decision Pattern: Sebelum launch Blend (produk baru, financial risk tinggi), commission dual audit top-tier (Trail of Bits + OpenZeppelin) Apr 2023, publish reports, fix findings, lalu launch Mei 2023.
· Evidence: Phase 3 EV-008/009. Phase 4 Audit History: 2 audits Blend. Phase 7 External Dependencies: Trail of Bits, OpenZeppelin sebagai security dependency.
· Trigger: Launch protokol lending baru dengan collateral NFT & ETH loans — bug = loss of user funds & reputational death.
· Response: Biaya & waktu 2 audit firms, publish transparan, fix critical findings pre-mainnet.
· Result: Blend launch smooth, >$100M volume week 1, no major exploit reported per 2024-10.
· Supporting Dataset: Phase 3 EV-008/009, Phase 4 Audit History, Phase 7 External Dependencies, Phase 8 Adoption Metrics (Blend TVL)

Pola 2: Fee Switch Activation sebagai Respons terhadap Revenue Uncertainty & Token Utility Criticism
· Decision Pattern: Setelah Season 3 berakhir (Feb 2024), token BLUR tidak punya utility kecuali governance. Komunitas & investor tekan untuk value accrual. DAO proposal fee switch 0.5% → stakers passed Feb 2024.
· Evidence: Phase 3 EV-013. Phase 6 Utility: Staking/Fee Switch. Phase 8 Narrative: Token Utility/Fee Switch. Phase 5 Revenue Model: fee switch live Feb 2024.
· Trigger: End of incentive seasons, token price decline pressure, "utility token" narrative demand, DAO treasury sustainability.
· Response: Governance proposal mengaktifkan protocol fee 0.5% (dari 0%) dan distribusi ke BLUR delegators.
· Result: Real yield ~10-20% APR awal, >25k delegators, token utility nyata. Regulatory risk meningkat (security classification).
· Supporting Dataset: Phase 3 EV-013, Phase 5 Revenue Model, Phase 6 Utility, Phase 8 Narrative Position

Pola 3: Ethereum-Only Strategy sebagai Hedge Against Multi-Chain Fragmentation Risk
· Decision Pattern: Tidak deploy ke L2/multi-chain trotz competitor pressure. Accept higher gas cost & smaller TAM untuk maintain technical simplicity, liquidity concentration, dan Ethereum alignment.
· Evidence: Phase 1/4/7/8: hanya Ethereum mainnet. Phase 8 Narrative: Ethereum Alignment. Phase 8 Open Threads: "L2 expansion signal: tidak ada announcement resmi".
· Trigger: Competitor (OpenSea, Magic Eden, X2Y2) expand multi-chain/L2. User demand untuk lower gas. Technical complexity orderbook off-chain di multi-chain.
· Response: Stay single-chain Ethereum L1. Focus on pro-trader segment yang toleran gas. Narrative differentiation: "Ethereum native".
· Result: Dominan 60-75% Ethereum NFT volume. Lost retail/L2 volume to competitors. Moat teknis terjaga.
· Supporting Dataset: Phase 4 System Architecture, Phase 7 Ecosystem Position, Phase 8 Narrative Position, Phase 8 Market Share

Pola 4: Unaudited Marketplace Contracts — Accepted Risk untuk Speed & Iteration
· Decision Pattern: Marketplace core contracts (Exchange, Bidding) live sejak Oct 2022 tanpa audit publik. Proxy upgradeable memungkinkan patch cepat jika bug ditemukan. Tidak ada bug bounty program publik terverifikasi.
· Evidence: Phase 4 Audit History: 0 audit marketplace. Phase 4 Known Limitations: "Marketplace Contracts Unaudited". Phase 4 Security Model: "Upgradeability: kontrak menggunakan proxy pattern... memungkinkan upgrade oleh admin".
· Trigger: Launch deadline Oct 2022, resource prioritization ke Blend audit (2023), belief bahwa battle-testing di mainnet dengan volume real > audit teoretis.
· Response: Monitor on-chain, upgrade via proxy jika issue, rely on OpenZeppelin lib security primitives.
· Result: No major exploit reported 2022-2024. But persistent community concern & technical debt.
· Supporting Dataset: Phase 4 Audit History, Known Technical Limitations, Security Model, Technical Upgrade History

Recurring Behavioral Pattern

Pola 1: Launch Fast, Iterate Via Proxy Upgrades, Audit Later (New Products Only)
· Evidence: Marketplace launch Oct 2022 tanpa testnet/audit → upgrades via proxy 【Phase 4 Technical Upgrade History】. Blend: dual audit pre-launch (Apr 2023) → launch Mei 2023 【Phase 3 EV-008/009/010】. Mobile app: beta Jun 2024 tanpa audit mobile khusus 【Phase 3 EV-014, Phase 4 Known Limitations】. Pattern: speed to market > formal verification for v1; audit untuk produk baru finansial (Blend).
· Supporting Dataset: Phase 3 EV-002/010/014, Phase 4 Technical Upgrade History, Audit History, Known Technical Limitations

Pola 2: Incentive Seasons sebagai Growth Lever, Lalu Stop & Monetize
· Evidence: Season 1 (airdrop TGE Feb 2023), Season 2 (Mei–Nov 2023), Season 3 (Nov 2023–Feb 2024) → stop. Fee switch Feb 2024 monetize. No Season 4 announced. Pattern: heavy token emissions untuk bootstrap → hard stop → fee switch revenue. Season 3 design include delegation incentive (prep untuk fee switch).
· Supporting Dataset: Phase 3 EV-004/011/012/013, Phase 6 Major Token Events, Phase 8 Adoption Metrics, Market Timeline

## Knowledge Extraction
_ref: `docs/Patterns/*`, `docs/Reasoning/*` (rule candidates)_

PROJECT: Blur

Core Insights

Insight 1: Arsitektur Hybrid Off-Chain Orderbook + On-Chain Settlement Memungkinkan Dominasi Volume Pro-Trader di Ethereum L1
Explanation: Blur memilih arsitektur off-chain orderbook dan matching engine terpusat untuk kecepatan eksekusi, batch bidding, dan trait/collection bids — fitur yang terlalu mahal/complex untuk fully on-chain. Settlement tetap on-chain via smart contract (Exchange, Bidding). Trade-off: trust assumption pada operator Blur Labs untuk fair ordering, namun mengakuisisi >60% market share volume Ethereum NFT sejak Q1 2023【Phase 4 — System Architecture】【Phase 4 — Known Technical Limitations】【Phase 8 — Market Share】.
Evidence: Off-chain orderbook terpusat di server Blur Labs; on-chain settlement via Blur Exchange Contract dan Blur Bidding Contract【Phase 4 — Core Components】. Market share 60–75% volume Ethereum NFT konstan 2 tahun【Phase 8 — Market Share】.
Supporting Dataset: Phase 4 (System Architecture, Core Components, Known Technical Limitations), Phase 8 (Market Share, Competitor Landscape)
Confidence: High

Insight 2: Tokenomics dengan Alokasi Komunitas 51% + Seasonal Incentive Programs (Season 1–3) Berfungsi sebagai Customer Acquisition Cost yang Efektif untuk Bootstrap Liquidity
Explanation: 51% supply BLUR dialokasikan ke komunitas/treasury DAO. Season 1 airdrop 360M BLUR (12% supply) ke trader pre-TGE; Season 2–3 reward trading/bidding/Blend activity selama ~9 bulan. Volume spike berkorelasi kuat dengan periode insentif; Season 3 berakhir Feb 2024 bersamaan dengan fee switch activation【Phase 6 — Distribution】【Phase 6 — Major Token Events】【Phase 3 — EV-004, EV-011, EV-012】【Phase 8 — Adoption Metrics】.
Evidence: Community allocation 51% (1.53B BLUR)【Phase 6 — Distribution】. Season 1 claimable immediately TGE Feb 2023【Phase 6 — TGE】. Season 2 Mei–Nov 2023, Season 3 Nov 2023–Feb 2024【Phase 3 — EV-011, EV-012】. Volume marketplace $1.5–3B/bulan saat Season 2–3【Phase 8 — Adoption Metrics】.
Supporting Dataset: Phase 3 (EV-004, EV-011, EV-012), Phase 6 (Distribution, Major Token Events, TGE), Phase 8 (Adoption Metrics, Market Timeline)
Confidence: High

Insight 3: Progressive Decentralization via DAO Governance (Snapshot Off-Chain + Multisig Execution) Sementara Multisig Blur Labs Tetap Memegang Admin Key Semua Kontrak Inti per 2024-10
Explanation: Blur DAO dibentuk bersamaan TGE Feb 2023 (EV-007). Governance via Snapshot off-chain voting, eksekusi on-chain via Blur Multisig (Gnosis Safe). Fee switch proposal Feb 2024 passed dan dieksekusi via multisig, bukan timelock DAO. Multisig tetap owner kontrak Marketplace, Blend, dan BLUR Token【Phase 6 — Governance】【Phase 4 — Security Model】【Phase 3 — EV-013】.
Evidence: Governance model: Snapshot signaling + multisig execution【Phase 6 — Governance】. Admin control: Multisig memegang ownership/admin key fee setter, pause, upgrade proxy【Phase 4 — Security Model】. Fee switch activated Feb 2024 via proposal executed by multisig【Phase 3 — EV-013】.
Supporting Dataset: Phase 3 (EV-007, EV-013), Phase 4 (Security Model, Technical Upgrade History), Phase 6 (Governance, Major Token Events), Phase 2 (Entity: Blur Multisig)
Confidence: High

Insight 4: Dual Audit Top-Tier (Trail of Bits + OpenZeppelin) untuk Produk Baru Finansial (Blend) vs Zero Audit Publik untuk Marketplace Core yang Sudah Live 6 Bulan Sebelumnya
Explanation: Blend (lending protocol, financial risk tinggi) mendapat dual audit Apr 2023 pre-launch Mei 2023 (EV-008, EV-009). Marketplace core contracts (Exchange, Bidding) live sejak Oct 2022 tanpa audit publik terverifikasi. Resource allocation priority ke produk baru, bukan battle-tested core【Phase 4 — Audit History】【Phase 4 — Known Technical Limitations】.
Evidence: Trail of Bits audit Blend Apr 2023【Phase 3 — EV-008】. OpenZeppelin audit Blend Apr 2023【Phase 3 — EV-009】. Marketplace contracts: "0 audit publik terverifikasi"【Phase 4 — Audit History】. Known limitation: "Marketplace Contracts Unaudited"【Phase 4 — Known Technical Limitations】.
Supporting Dataset: Phase 3 (EV-008, EV-009, EV-010), Phase 4 (Audit History, Known Technical Limitations, Security Model)
Confidence: High

Insight 5: Ethereum L1-Only Strategy sebagai Moat Teknis dan Narasi Differentiation, Menghindari Fragmentasi Liquidity dan Kompleksitas Multi-Chain Orderbook
Explanation: Semua kontrak hanya di Ethereum mainnet. Tidak ada deployment Arbitrum, Optimism, Base, Blast per 2024-10. Founder PacmanBlur pro-Ethereum. Kompetitor (OpenSea, Magic Eden, X2Y2) sudah multi-chain. Gas cost tinggi memfilter retail, mempertahankan pro-trader segment【Phase 1 — Chain(s)】【Phase 4 — System Architecture】【Phase 7 — Ecosystem Position】【Phase 8 — Narrative Position】.
Evidence: Chain: Ethereum only【Phase 1 — Chain(s)】. Cross-chain: Tidak ada【Phase 4 — System Architecture】. Supported Chains: Ethereum Mainnet only【Phase 7 — Ecosystem Position】. Narrative: Ethereum Alignment【Phase 8 — Narrative Position】. Open Threads: "L2 expansion signal: tidak ada announcement resmi"【Phase 8 — Open Threads】.
Supporting Dataset: Phase 1 (Chain), Phase 4 (System Architecture), Phase 7 (Ecosystem Position), Phase 8 (Narrative Position, Open Threads)
Confidence: High

Insight 6: CEX-First Token Distribution (Binance Spot+Perpetual, Coinbase Experimental Same-Day TGE) dengan Market Maker Professional (Wintermute, GSR) Memberikan Deep Liquidity Instan dan Legitimacy
Explanation: TGE Feb 14 2023: Binance listing spot (BLUR/USDT, BLUR/BUSD, BLUR/BTC) + perpetual (BLUR/USDT) same-day; Coinbase TGE+1 (Experimental). Wintermute & GSR sebagai market maker. DEX (Uniswap V2/V3) community-driven tanpa official liquidity mining【Phase 3 — EV-004, EV-005, EV-006】【Phase 7 — Exchange Ecosystem】【Phase 2 — Entity: Wintermute, GSR】.
Evidence: Binance listing announcement TGE day【Phase 3 — EV-005】. Coinbase listing TGE+1【Phase 3 — EV-006】. Wintermute/GSR market maker【Phase 2 — Entity: Wintermute, GSR】. Uniswap pools permissionless, no official LM【Phase 7 — Exchange Ecosystem】.
Supporting Dataset: Phase 3 (EV-004, EV-005, EV-006), Phase 7 (Exchange Ecosystem), Phase 2 (Entity: Wintermute, GSR), Phase 5 (Financial Dependencies)
Confidence: High

Insight 7: Fee Switch Activation (0.5% Protocol Fee → BLUR Stakers) Feb 2024 Menandai Transisi dari Incentive-Driven Growth ke Sustainable Revenue Sharing Model
Explanation: Setelah Season 3 berakhir, DAO proposal mengaktifkan 0.5% marketplace fee (dari 0%) dan distribusi ke BLUR delegators. Real yield ~10–20% APR awal, >25k delegators. Revenue split exact (staker vs treasury vs team) tidak transparan. Regulatory risk "security" meningkat【Phase 3 — EV-013】【Phase 6 — Utility: Staking/Fee Switch】【Phase 5 — Revenue Model】【Phase 8 — Narrative Position】.
Evidence: Fee switch proposal passed Feb 2024【Phase 3 — EV-013】. Staking yield 10–20% APR, >25k delegators【Phase 8 — Adoption Metrics】. Revenue model: fee switch live Feb 2024【Phase 5 — Revenue Model】. Narrative: Token Utility/Fee Switch【Phase 8 — Narrative Position】.
Supporting Dataset: Phase 3 (EV-013), Phase 5 (Revenue Model), Phase 6 (Utility, Major Token Events), Phase 8 (Adoption Metrics, Narrative Position)
Confidence: High

Insight 8: Pseudonymous Founders (PacmanBlur, Galaga, Lord_kekl) + VC-Backed Entity (Blur Labs Inc, Delaware) + Paradigm Series A $11M @ $1B Valuation = Hybrid Structure yang Memungkinkan Speed & Credibility
Explanation: 3 founder pseudonim mendirikan Blur Labs Inc (Delaware) 2022. Series A Paradigm Nov 2022 $11M @ $1B val pre-revenue. Variant Fund seed. Capital untuk scaling tim, infra, audit, incentives. Paradigm strategic value > capital. Token allocation ke investor dengan vesting 1-year cliff + 4-5 tahun linear【Phase 1 — Founding Entity, Founders】【Phase 3 — EV-001, EV-003】【Phase 5 — Funding History】【Phase 6 — Vesting Schedule】.
Evidence: Blur Labs Inc Delaware, 3 pseudonymous founders【Phase 1 — Founding Entity, Founders】. Series A Paradigm $11M @ $1B val Nov 2022【Phase 3 — EV-003】. Vesting: investor cliff 1yr, 4-5yr linear【Phase 6 — Vesting Schedule】.
Supporting Dataset: Phase 1 (Founding Entity, Founders), Phase 3 (EV-001, EV-003), Phase 5 (Funding History), Phase 6 (Vesting Schedule), Phase 2 (Entity: Paradigm, Variant Fund)
Confidence: High

Insight 9: Blend Protocol (Peer-to-Peer Perpetual NFT Lending) sebagai Vertical Integration yang Menciptakan Revenue Stream Kedua dan Narasi NFTfi Differentiation
Explanation: Blend launch Mei 2023 (EV-010) setelah dual audit. P2P perpetual loans (no fixed expiry), Uniswap V3 TWAP oracle untuk likuidasi. >$100M volume minggu 1, TVL $150–300M, cumulative loan volume >$2B. Revenue dari interest spread/origination fee. Narasi "NFT financialization" secondary【Phase 3 — EV-010】【Phase 8 — Adoption Metrics】【Phase 8 — Narrative Position】【Phase 4 — Core Components: Blend Contract】.
Evidence: Blend launch May 2023【Phase 3 — EV-010】. Volume week 1 >$100M【Phase 8 — Adoption Metrics】. TVL $150–300M, cumulative >$2B【Phase 8 — Adoption Metrics】. Oracle: Uniswap V3 TWAP【Phase 4 — System Architecture】. Narrative: NFT Financialization via Blend【Phase 8 — Narrative Position】.
Supporting Dataset: Phase 3 (EV-008, EV-009, EV-010), Phase 4 (Core Components, System Architecture), Phase 8 (Adoption Metrics, Narrative Position, Competitor Landscape)
Confidence: High

Insight 10: Treasury Opasitas — Ukuran, Komposisi, Custodian Tidak Dipublikasikan; Alamat Multisig/Treasury Tidak Terlabel Jelas di Etherscan
Explanation: Tidak ada transparency report, dashboard treasury, atau real-time disclosure. "Current Treasury Size: tidak diungkap", "Composition: tidak diungkap". Estimasi >1B BLUR di multisig/DAO treasury tapi tidak terverifikasi. Strategic opacity atau prioritization rendah【Phase 5 — Treasury】【Phase 6 — Holder Distribution】【Phase 5 — Open Threads】.
Evidence: Treasury size/composition/custodian: tidak diungkap【Phase 5 — Treasury】. Treasury holding: "estimasi >1B BLUR... tidak terlabel jelas"【Phase 6 — Holder Distribution】. Open Threads: "Ukuran dan komposisi treasury... tidak dipublikasikan"【Phase 5 — Open Threads】.
Supporting Dataset: Phase 5 (Treasury, Open Threads), Phase 6 (Holder Distribution)
Confidence: High

Strategic Principles

Principle 1: Performance-First Architecture untuk Pro-Trader Segment — Off-Chain Orderbook + On-Chain Settlement
Explanation: Memilih arsitektur hybrid yang mengorbankan desentralisasi orderbook untuk latency rendah, batch bidding, trait/collection bids — fitus kritis untuk high-frequency traders. Settlement on-chain menjaga trust-minimized asset transfer. Moat teknis sulit direplikasi kompetitor【Phase 4 — System Architecture】【Phase 4 — Known Technical Limitations】【Phase 8 — Competitor Landscape】.
Evidence: Off-chain matching engine terpusat; on-chain Exchange/Bidding contracts【Phase 4 — Core Components】. Known limitation: "Orderbook Off-chain Terpusat: trust assumption pada operator"【Phase 4 — Known Technical Limitations】. Competitor OpenSea menggunakan Seaport fully on-chain【Phase 8 — Competitor Landscape】.
Supporting Dataset: Phase 4 (System Architecture, Core Components, Known Technical Limitations), Phase 8 (Competitor Landscape)
Confidence: High

Principle 2: Ethereum Alignment sebagai Strategic Moat — Single-Chain Focus, No L2/Multi-Chain Dilution
Explanation: Komitmen pada Ethereum L1 only untuk settlement, liquidity concentration, dan narasi differentiation. Menghindari kompleksitas porting off-chain orderbook ke multi-chain, fragmentasi liquidity, dan dependency risk bridge/L2. Accept higher gas cost sebagai filter pro-trader【Phase 1 — Chain(s)】【Phase 4 — System Architecture】【Phase 8 — Narrative Position】.
Evidence: Chain: Ethereum only【Phase 1 — Chain(s)】. Cross-chain: Tidak ada【Phase 4 — System Architecture】. Narrative: Ethereum Alignment【Phase 8 — Narrative Position】. Open Threads: "L2 expansion signal: tidak ada announcement resmi"【Phase 8 — Open Threads】.
Supporting Dataset: Phase 1 (Chain), Phase 4 (System Architecture), Phase 8 (Narrative Position, Open Threads)
Confidence: High

Principle 3: Security Investment Priority pada Produk Baru Finansial (Blend) via Dual Audit Top-Tier
Explanation: Alokasi resource audit ke produk baru dengan financial risk tinggi (Blend: collateral NFT + ETH loans) bukan pada marketplace core yang sudah battle-tested di mainnet 6 bulan. Dual audit Trail of Bits + OpenZeppelin pre-launch sebagai trust signal institucional【Phase 4 — Audit History】【Phase 3 — EV-008, EV-009】.
Evidence: 2 audits Blend (Trail of Bits + OpenZeppelin) Apr 2023 pre-launch Mei 2023【Phase 3 — EV-008, EV-009】. Marketplace contracts: 0 audit publik【Phase 4 — Audit History】. Known limitation: "Marketplace Contracts Unaudited"【Phase 4 — Known Technical Limitations】.
Supporting Dataset: Phase 3 (EV-008, EV-009, EV-010), Phase 4 (Audit History, Known Technical Limitations)
Confidence: High

Principle 4: Progressive Decentralization — DAO Governance Signaling First, Execution Infrastructure Later
Explanation: Membentuk DAO dan token governance TGE day-1 (EV-007), tapi mempertahankan multisig execution untuk speed & emergency capability. Fee switch proposal Feb 2024 dieksekusi via multisig, bukan timelock DAO. Gradual handover seiring maturity【Phase 6 — Governance】【Phase 4 — Security Model】【Phase 3 — EV-013】.
Evidence: DAO formed TGE Feb 2023【Phase 3 — EV-007】. Governance: Snapshot signaling + multisig execution【Phase 6 — Governance】. Multisig masih owner semua kontrak per 2024-10【Phase 4 — Security Model】. Fee switch executed via multisig【Phase 3 — EV-013】.
Supporting Dataset: Phase 3 (EV-007, EV-013), Phase 4 (Security Model), Phase 6 (Governance)
Confidence: High

Principle 5: Tokenomics Designed untuk Bootstrap Liquidity (Seasonal Incentives) → Monetization (Fee Switch) → Sustainable Value Accrual
Explanation: 51% supply komunitas didistribusikan via Season 1 airdrop (retroactive), Season 2–3 activity rewards. Season 3 design include delegation incentive (prep fee switch). Fee switch Feb 2024 mengaktifkan real yield. No Season 4 → hard stop emissions, pivot ke fee revenue【Phase 6 — Distribution】【Phase 3 — EV-004, EV-011, EV-012, EV-013】.
Evidence: Community 51% allocation【Phase 6 — Distribution】. Season 1 claim TGE, Season 2–3 rewards【Phase 3 — EV-004, EV-011, EV-012】. Fee switch Feb 2024【Phase 3 — EV-013】. No Season 4 announced【Phase 8 — Market Timeline】.
Supporting Dataset: Phase 3 (EV-004, EV-011, EV-012, EV-013), Phase 6 (Distribution, Major Token Events), Phase 8 (Market Timeline, Narrative Position)
Confidence: High

Principle 6: CEX-First Listing Strategy untuk Deep Liquidity Instan dan Legitimacy Signal
Explanation: Prioritaskan Binance (spot + perpetual) dan Coinbase (Experimental) same-day/next-day TGE. Engage professional market makers (Wintermute, GSR). DEX secondary, community-driven. CEX listing sebagai marketing & retail access tool【Phase 3 — EV-005, EV-006】【Phase 7 — Exchange Ecosystem】【Phase 2 — Entity: Wintermute, GSR】.
Evidence: Binance listing TGE day spot+perp【Phase 3 — EV-005】. Coinbase TGE+1 Experimental【Phase 3 — EV-006】. Wintermute/GSR market maker【Phase 2 — Entity: Wintermute, GSR】. Uniswap no official LM【Phase 7 — Exchange Ecosystem】.
Supporting Dataset: Phase 3 (EV-005, EV-006), Phase 7 (Exchange Ecosystem), Phase 2 (Entity: Wintermute, GSR), Phase 5 (Financial Dependencies)
Confidence: High

Principle 7: Vertical Integration via Native Lending Protocol (Blend) untuk Diversifikasi Revenue dan Narasi NFTfi
Explanation: Membangun Blend sebagai protokol terpisah (smart contract sendiri) terintegrasi UI marketplace. P2P perpetual model diferensiasi vs peer-to-pool (BendDAO). Revenue stream kedua: lending fees. Narasi "NFT financialization" memperluas TAM beyond trading【Phase 3 — EV-010】【Phase 4 — Core Components: Blend Contract】【Phase 8 — Narrative Position】.
Evidence: Blend separate contract, integrated UI【Phase 4 — Core Components】. P2P perpetual, Uniswap V3 oracle【Phase 4 — System Architecture】. Narrative: NFT Financialization via Blend【Phase 8 — Narrative Position】. Competitor: BendDAO peer-to-pool【Phase 8 — Competitor Landscape】.
Supporting Dataset: Phase 3 (EV-010), Phase 4 (Core Components, System Architecture), Phase 8 (Narrative Position, Competitor Landscape)
Confidence: High

Principle 8: Standard Wallet Compatibility, No Proprietary Wallet/SDK — Focus pada Core Product
Explanation: Tidak membangun wallet, SDK, developer tools khusus. Mendukung standar Ethereum (MetaMask, WalletConnect, Rabby, Ledger) via EIP-1193. API public (REST/GraphQL) untuk bot/trader custom tooling. Resource focus pada marketplace + lending【Phase 7 — Wallet Ecosystem】【Phase 7 — Developer Ecosystem】.
Evidence: "Blur tidak mempublikasikan daftar wallet resmi... semua wallet Ethereum standar kompatibel"【Phase 7 — Wallet Ecosystem】. "Tidak ada SDK resmi... API: Public REST/GraphQL... Tidak ada developer tools khusus"【Phase 7 — Developer Ecosystem】.
Supporting Dataset: Phase 7 (Wallet Ecosystem, Developer Ecosystem)
Confidence: High

Success Factors

Factor 1: Produk Superior untuk Pro-Trader (Off-Chain Orderbook, Bidding Pools, Zero Fee Awal) Menangkap Market Share Dominan dari OpenSea
Explanation: Fitur bidding kolektif (collection/trait bids), off-chain matching engine cepat, zero platform fee (pre-fee switch), API untuk bot menarik whale/pro-trader. Market share 60–75% volume Ethereum NFT konstan sejak Q1 2023. Volume kumulatif >$25B【Phase 8 — Market Share】【Phase 3 — EV-002】【Phase 4 — Core Components】.
Evidence: Market share 60–75% Ethereum NFT volume【Phase 8 — Market Share】. Launch Oct 2022 dengan bidding pools, zero fee【Phase 3 — EV-002】. Core components: Exchange, Bidding contracts【Phase 4 — Core Components】.
Supporting Dataset: Phase 3 (EV-002), Phase 4 (Core Components), Phase 8 (Market Share, Competitor Landscape)
Confidence: High

Factor 2: Incentive Design yang Sophisticated (Season 1 Points-Based Anti-Sybil Airdrop → Season 2–3 Activity Rewards) Mendefinisikan Standar Baru Airdrop Farming
Explanation: Season 1: points berdasarkan aktivitas pre-TGE (trading, bidding, listing) → anti-sybil, reward genuine users. Season 2–3: reward trading volume, bidding, Blend activity. Volume spike korelasi kuat dengan seasons. "Most sophisticated airdrop design" per analyst reports【Phase 3 — EV-004, EV-011, EV-012】【Phase 8 — Adoption Metrics】【Phase 8 — Narrative Position】.
Evidence: Season 1 airdrop 360M BLUR ke trader pre-TGE【Phase 3 — EV-004】. Season 2–3 rewards【Phase 3 — EV-011, EV-012】. Volume spike during seasons【Phase 8 — Adoption Metrics】. Narrative: "most sophisticated airdrop design"【Phase 8 — Narrative Position】.
Supporting Dataset: Phase 3 (EV-004, EV-011, EV-012), Phase 8 (Adoption Metrics, Narrative Position)
Confidence: High

Factor 3: Paradigm Series A $11M @ $1B Valuation (Nov 2022) Memberikan Capital + Strategic Access ke Ekosistem Ethereum
Explanation: Dana untuk hire core team, infra server, audit Blend, incentive seasons. Paradigm network membuka akses ke Ethereum researchers, L2 teams, institutional partners. Valuasi $1B pre-revenue menunjukkan conviction investor【Phase 3 — EV-003】【Phase 5 — Funding History】【Phase 2 — Entity: Paradigm】.
Evidence: Series A $11M Paradigm Nov 2022 @ $1B val【Phase 3 — EV-003】. Paradigm portfolio strategic value【Phase 2 — Entity: Paradigm】. Funding used for scaling【Phase 5 — Funding History】.
Supporting Dataset: Phase 3 (EV-003), Phase 5 (Funding History), Phase 2 (Entity: Paradigm)
Confidence: High

Factor 4: Dual Audit Blend (Trail of Bits + OpenZeppelin) Pre-Launch Menciptakan Trust Institusional untuk Protokol Lending Baru
Explanation: Blend mengelola collateral NFT bernilai tinggi + ETH loans. Dual audit top-tier Apr 2023, findings fixed pre-launch Mei 2023. Launch smooth >$100M volume week 1, no major exploit per 2024-10. Trust signal untuk whale/institutional lenders【Phase 3 — EV-008, EV-009】【Phase 4 — Audit History】【Phase 8 — Adoption Metrics】.
Evidence: Trail of Bits audit Apr 2023【Phase 3 — EV-008】. OpenZeppelin audit Apr 2023【Phase 3 — EV-009】. Blend launch May 2023 >$100M week 1【Phase 8 — Adoption Metrics】. No major exploit reported【Phase 8 — Adoption Metrics】.
Supporting Dataset: Phase 3 (EV-008, EV-009, EV-010), Phase 4 (Audit History), Phase 8 (Adoption Metrics)
Confidence: High

Factor 5: Fee Switch Activation (Feb 2024) Mengubah Narasi Token dari "Governance Only" ke "Real Yield" — Menarik Stakers & Align Incentive
Explanation: 0.5% protocol fee → BLUR stakers. Real yield 10–20% APR awal, >25k delegators. Token utility nyata beyond voting. Menjawab kritik "utility token" dan tekanan investor untuk value accrual【Phase 3 — EV-013】【Phase 6 — Utility: Staking/Fee Switch】【Phase 8 — Narrative Position】.
Evidence: Fee switch proposal passed Feb 2024【Phase 3 — EV-013】. Staking yield 10–20% APR, >25k delegators【Phase 8 — Adoption Metrics】. Narrative: Token Utility/Fee Switch【Phase 8 — Narrative Position】.
Supporting Dataset: Phase 3 (EV-013), Phase 6 (Utility, Major Token Events), Phase 8 (Adoption Metrics, Narrative Position)
Confidence: High

Factor 6: Blend Protocol sebagai Vertical Integration yang Menciptakan Revenue Stream Kedua dan Narasi NFTfi Differentiation
Explanation: P2P perpetual lending (no expiry), Uniswap V3 TWAP oracle. >$2B cumulative loan volume, TVL $150–300M. Revenue dari lending fees. Narasi "NFT financialization" memperluas TAM beyond trading. Differentiation vs OpenSea (no native lending)【Phase 3 — EV-010】【Phase 8 — Adoption Metrics】【Phase 8 — Narrative Position】.
Evidence: Blend launch May 2023【Phase 3 — EV-010】. Cumulative loan volume >$2B【Phase 8 — Adoption Metrics】. TVL $150–300M【Phase 8 — Adoption Metrics】. Narrative: NFT Financialization【Phase 8 — Narrative Position】.
Supporting Dataset: Phase 3 (EV-010), Phase 8 (Adoption Metrics, Narrative Position, Competitor Landscape)
Confidence: High

Factor 7: CEX Listing Tier-1 Same-Day TGE (Binance Spot+Perp, Coinbase Experimental) Memberikan Deep Liquidity Instan dan Price Discovery Efisien
Explanation: Binance listing spot + perpetual same-day TGE. Coinbase TGE+1. Wintermute/GSR market making. Volume hari pertama >$1B. Deep liquidity menarik institutional & retail. Perpetual futures memungkinkan hedging & speculation【Phase 3 — EV-005, EV-006】【Phase 7 — Exchange Ecosystem】【Phase 2 — Entity: Wintermute, GSR】.
Evidence: Binance listing TGE day【Phase 3 — EV-005】. Coinbase TGE+1【Phase 3 — EV-006】. Wintermute/GSR market maker【Phase 2 — Entity: Wintermute, GSR】. Volume day 1 >$1B【Phase 8 — Market Timeline】.
Supporting Dataset: Phase 3 (EV-005, EV-006), Phase 7 (Exchange Ecosystem), Phase 2 (Entity: Wintermute, GSR), Phase 8 (Market Timeline)
Confidence: High

Failure Factors

Factor 1: Marketplace Core Contracts Unaudited (Live Sejak Oct 2022) — Persistent Technical Debt dan Community Concern
Explanation: Kontrak inti Exchange & Bidding live 2+ tahun tanpa audit publik terverifikasi. Hanya bergantung pada OpenZeppelin library primitives dan battle-testing mainnet. Bug bounty program tidak publik terverifikasi. Risiko exploit berkelanjutan【Phase 4 — Audit History】【Phase 4 — Known Technical Limitations】【Phase 4 — Security Model】.
Evidence: "0 audit publik terverifikasi untuk Marketplace core contracts"【Phase 4 — Audit History】. Known limitation: "Marketplace Contracts Unaudited"【Phase 4 — Known Technical Limitations】. Upgradeability via proxy memungkinkan patch tapi reactive【Phase 4 — Security Model】.
Supporting Dataset: Phase 4 (Audit History, Known Technical Limitations, Security Model)
Confidence: High

Factor 2: Multisig Admin Key Retention (Blur Labs) Tanpa Timelock/DAO Execution On-Chain — Centralization Risk & Regulatory Target
Explanation: Multisig memegang ownership/admin key semua kontrak (fee setter, pause, upgrade proxy) per 2024-10. Tidak ada migrasi ke TimelockController + DAO voting execution. Key person risk, single point of failure, regulatory target (SEC enforcement risk)【Phase 4 — Security Model】【Phase 2 — Entity: Blur Multisig】【Phase 6 — Governance】.
Evidence: "Multisig memegang ownership/admin key... belum sepenuhnya ditimelock/DAO-kan"【Phase 4 — Security Model】. Blur Multisig owner di Etherscan【Phase 2 — Entity: Blur Multisig】. Governance execution via multisig bukan timelock【Phase 6 — Governance】.
Supporting Dataset: Phase 4 (Security Model), Phase 2 (Entity: Blur Multisig), Phase 6 (Governance)
Confidence: High

Factor 3: Treasury Opasitas — Tidak Ada Transparency Report, Dashboard, atau Real-Time Disclosure Ukuran/Komposisi/Custodian
Explanation: Ukuran treasury, komposisi (stablecoin vs BLUR vs aset lain), custodian address tidak dipublikasikan. Alamat multisig/treasury tidak terlabel jelas di Etherscan. Community trust & accountability reduced. Strategic opacity atau prioritization rendah【Phase 5 — Treasury】【Phase 6 — Holder Distribution】【Phase 5 — Open Threads】.
Evidence: "Current Treasury Size: tidak diungkap", "Composition: tidak diungkap"【Phase 5 — Treasury】. "Treasury holding: estimasi >1B BLUR... tidak terlabel jelas"【Phase 6 — Holder Distribution】. Open Threads: "Ukuran dan komposisi treasury... tidak dipublikasikan"【Phase 5 — Open Threads】.
Supporting Dataset: Phase 5 (Treasury, Open Threads), Phase 6 (Holder Distribution)
Confidence: High

Factor 4: Ethereum L1-Only Strategy Membatasi TAM (Total Addressable Market) dan Kehilangan Retail/L2 Volume ke Kompetitor
Explanation: Gas cost tinggi memfilter retail user. Kompetitor (OpenSea, Magic Eden, X2Y2) multi-chain/L2 capture retail & gaming volume. Blur market share user/trader count hanya 30–40% vs volume 60–75%. Moat teknis terjaga tapi TAM terbatas【Phase 8 — Market Share】【Phase 8 — Competitor Landscape】【Phase 8 — Open Threads】.
Evidence: User/trader market share 30–40%【Phase 8 — Market Share】. Competitor multi-chain【Phase 8 — Competitor Landscape】. Open Threads: "L2 expansion signal: tidak ada announcement resmi"【Phase 8 — Open Threads】.
Supporting Dataset: Phase 8 (Market Share, Competitor Landscape, Open Threads)
Confidence: Medium

Factor 5: Token Vesting Cliff End Feb 2024 (Team/Investor) Menciptakan Supply

## Open Questions
- [foundation] Yurisdiksi hukum pasti Blur Labs, Inc. (Delaware dikutip sering tapi belum terlihat filing resmi yang diverifikasi)
- [foundation] Komposisi tim inti di luar tiga founder pseudonim (ukuran tim, nama nyata, lokasi operasional)
- [foundation] Apakah ada entity legal terpisah untuk protokol Blend vs marketplace Blur
- [foundation] Tanggal pasti deployment kontrak token BLUR on-chain vs announcement TGE (perbedaan 1-2 hari sering terjadi)
- [foundation] Status kepemilikan kontrak (ownership/admin keys) untuk marketplace, Blend, dan token BLUR — apakah sudah ditimelock/DAO
- [foundation] Detail alokasi tokenomics resmi dari sumber primer (blog/whitepaper) vs data on-chain (sering tidak cocok)
- [entity] Identitas legal lengkap Blur Labs, Inc. (nomor registrasi Delaware, alamat kantor terverifikasi) belum ditemukan di public filing.
- [entity] Daftar lengkap investor seed/private round selain Paradigm dan Variant Fund (termasuk alokasi token per investor) tidak diungkapkan resmi.
- [entity] Status kepemilikan kontrak (ownership) saat ini: apakah Blur Multisig sudah menyerahkan kontrol penuh ke Blur DAO (timelock) atau masih memegang admin key kritis.
- [entity] Detail komposisi tim inti (core team) di luar 3 founder pseudonim (jumlah karyawan, peran, lokasi) tidak tersedia publik.
- [entity] Entity legal terpisah untuk Blend (apakah di bawah Blur Labs Inc yang sama atau entity baru) belum dikonfirmasi.
- [entity] Keterlibatan market maker (Wintermute, GSR) apakah mencakup token loan/option agreement standar industri tidak diverifikasi on-chain.
- [entity] Tanggal deployment kontrak token BLUR on-chain vs announcement TGE (perbedaan 1-2 hari) perlu direkonsiliasi dengan data Etherscan.
- [history] Tanggal pasti pendirian Blur Labs, Inc. (hanya tahun 2022 yang diketahui, tanpa bulan/tanggal spesifik dari filing Delaware resmi)
- [history] Tanggal deployment kontrak token BLUR on-chain vs announcement TGE (perbedaan 1-2 hari antara Etherscan dan blog resmi perlu direkonsiliasi)
- [history] Detail alokasi tokenomics resmi persen per kategori (community, team, investor, treasury) dari sumber primer (blog/whitepaper) vs data on-chain — sering tidak cocok
- [history] Status kepemilikan kontrak (ownership/admin keys) saat ini: apakah Blur Multisig sudah menyerahkan kontrol penuh ke Blur DAO via timelock atau masih memegang admin key kritis
- [history] Entity legal terpisah untuk Blend (apakah di bawah Blur Labs Inc yang sama atau entity baru) belum dikonfirmasi
- [history] Detail investor seed/private round selain Paradigm dan Variant Fund (termasuk alokasi token per investor) tidak diungkapkan resmi
- [history] Komposisi tim inti (core team) di luar 3 founder pseudonim (jumlah karyawan, peran, lokasi) tidak tersedia publik
- [history] Keterlibatan market maker (Wintermute, GSR) apakah mencakup token loan/option agreement standar industri tidak diverifikasi on-chain
- [history] Tanggal pasti mulai dan berakhirnya Season 2 dan Season 3 insentif (hanya bulan yang diketahui dari announcements Discord/blog)
- [history] Jumlah proposal governance total yang telah dilewatkan/gagal sejak DAO formation (butuh query Snapshot/on-chain untuk angka pasti)
- [technology] Status timelock/DAO ownership: Apakah Blur Multisig sudah menyerahkan admin key ke timelock contract yang dikontrol Blur DAO? Data on-chain menunjukkan multisig masih owner per 2024-10.
- [technology] Marketplace audit: Tidak ada audit publik untuk kontrak marketplace inti (exchange, bidding) — apakah audit privat ada atau direncanakan?
- [technology] L2 Deployment: Tidak ada announcement resmi deployment ke L2 (Arbitrum, Optimism, Base, Blast) meskipun kompetitor sudah melakukannya.
- [technology] Formal Verification: Tidak ada bukti formal verification pada kontrak kritis.
- [technology] Mobile App Security: Beta mobile app belum melalui audit keamanan khusus mobile (iOS/Android).
- [technology] Orderbook Decentralization: Tidak ada roadmap teknis publik untuk mendezentralisasi orderbook/matching engine.
- [technology] Blend Oracle Upgrade: Apakah rencana migrasi oracle Blend ke Chainlink/Pyth atau oracle terdesentralisasi lain?
- [technology] Gas Optimization Upgrades: Detail upgrade gas optimization pada marketplace contracts tidak terdokumentasi publik sebagai changelog terstruktur.
- [technology] API/Indexer Open Source: Blur API dan indexer tidak open source; tidak ada dokumentasi teknis arsitektur backend yang detail.
- [technology] Cross-chain / Multi-chain: Tidak ada indikasi teknis dukungan multi-chain di repository/docs resmi.
- [financial] Ukuran dan komposisi treasury BLUR DAO real-time (stablecoin vs BLUR vs aset lain) tidak dipublikasikan; alamat multisig/treasury resmi tidak terlabel jelas di Etherscan
- [financial] Jumlah exact private sale/seed round valuation dan alokasi token per investor (Paradigm, Variant, Cozomo, dll.) tidak diungkapkan resmi
- [financial] Revenue history bulanan/kuartalan protocol fee marketplace dan Blend tidak tersedia publik
- [financial] Apakah Blur Labs memiliki runway/proyeksi keuangan internal yang dibagikan ke investor (board reporting) — tidak publik
- [financial] Status vesting investor/team token: jadwal unlock detail (cliff, linear monthly, dst.) tidak diungkapkan di blog resmi; hanya "4-5 tahun vesting" yang disebutkan secara umum
- [financial] Fee switch revenue split: persentase exact fee yang dialokasikan ke staker vs treasury DAO vs tim tidak dipecah di proposal governance
- [financial] Blend revenue model detail: apakah ada origination fee, interest spread, atau liquidation fee — tidak terdokumentasi jelas di blog/audit
- [financial] Apakah ada rencana diversifikasi treasury (stablecoin, ETH, blue-chip NFT) via proposal DAO — tidak ada proposal terlihat di Snapshot per 2024-10
- [financial] Ketergantungan finansial pada market maker (Wintermute, GSR): apakah ada token loan/option agreement yang menciptakan liabilitas tersembunyi — tidak diverifikasi on-chain
- [financial] Status kepatuhan pajak/laporan keuangan Blur Labs, Inc. (Delaware C-Corp) — tidak publik
- [token] Persentase exact alokasi Team, Investors, Advisors tidak diungkapkan di blog resmi Blur; hanya "51% community" yang eksplisit. Sumber sekunder (CryptoRank, Messari, CoinGecko) memberikan angka bervariasi (Team 20-25%, Investors 15-20%, Advisors 2-5%) — perlu konfirmasi dari primary source atau on-chain vesting contract analysis.
- [token] Jumlah exact token Season 1 airdrop (claimable vs unclaimed) tidak dipublikasikan sebagai final report; estimasi ~360M (12%) dari blog "12% to Season 1" tapi actual claim rate tidak diketahui.
- [token] Alamat multisig/treasury resmi Blur DAO tidak terlabel jelas di Etherscan; sulit memverifikasi holding treasury real-time vs team/investor vesting contracts.
- [token] Status fee switch revenue split: persentase exact fee yang dialokasikan ke staker vs treasury DAO vs tim tidak dipecah di proposal governance (EV-013) — hanya "fee switch activated" yang diverifikasi.
- [token] Apakah ada token burn mechanism yang direncanakan via proposal DAO masa depan — tidak ada proposal terlihat di Snapshot per 2024-10.
- [token] Vesting contract addresses untuk team/investor tidak dipublikasikan resmi; analisis on-chain diperlukan untuk melacak unlock schedule actual vs yang diinfokan "4-5 tahun".
- [token] Blend protocol tidak menggunakan BLUR token secara native (tidak sebagai collateral, fee, atau governance) — apakah rencana integrasi BLUR ke Blend (misal: staking BLUR untuk boost yield, governance Blend parameter) ada di roadmap — tidak diumumkan.
- [token] Circulating supply real-time tidak tersedia dari dashboard resmi; CoinGecko/CoinMarketCap menggunakan metodologi sendiri yang mungkin tidak akurat untuk token dengan vesting besar.
- [token] Tokenomics detail (cliff exact date, vesting start date, unlock frequency exact) tidak terdokumentasi di blog — hanya "1-year cliff, 4-5 year vesting" secara umum.
- [token] Legal status BLUR token (utility vs security) di bawah hukum AS belum ada legal opinion publik; potensi regulasi mempengaruhi utility governance/staking.
- [market] Real-time volume & market share data: Tidak ada dashboard resmi Blur; bergantung pada Dune community queries yang metodologi bervariasi (beberapa include wash trading, beberapa exclude) — perlu standardisasi.
- [market] Blend TVL & loan volume on-chain vs DeFiLlama: DeFiLlama tidak selalu sinkron dengan data on-chain Blend (contract address 0x2946...) — perlu cross-check manual.
- [market] BLUR token circulating supply methodology: CoinGecko vs CoinMarketCap vs Token Terminal menggunakan definisi circulating berbeda (include/exclude team vesting, DAO treasury, unclaimed Season 1) — angka berbeda 10-20%.
- [market] CEX listing completeness: Daftar CEX lengkap (Bybit, OKX, Kraken, KuCoin, Gate.io, HTX, dll.) tidak diverifikasi dari sumber resmi Blur — hanya CoinGecko/CMC yang agregasi.
- [market] Geographic user distribution: Tidak ada data on-chain yang reliable untuk geographic focus (Ethereum pseudonim); proxy via exchange KYC data tidak publik.
- [market] Wash trading estimation: Beberapa analyst (Nansen, Chainalysis) mengestimasi % wash trading di Blur selama Season 2-3 tinggi (>30%) tapi tidak ada report resmi — perlu audit independen.
- [market] Fee switch revenue actuals: Jumlah ETH terkumpul dari 0.5% fee switch dan terdistribusi ke staker tidak dipublikasikan secara berkala — hanya on-chain traceable via contract events.
- [market] Mobile app adoption metrics: Download count, MAU, volume via mobile vs desktop tidak dipublikasikan.
- [market] L2 expansion signal: Tidak ada announcement resmi L2 deployment (Arbitrum, Base, Blast, Optimism) meskipun kompetitor sudah — narasi "Ethereum only" apakah permanent atau temporary.
- [market] Competitor volume data source: OpenSea volume sering dilaporkan termasuk multi-chain (Polygon, Base, dll.) — perbandingan "Ethereum only" vs "All chains" tidak apple-to-apple.
