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

1. Mendominasi volume trading NFT Ethereum melalui produk profesional untuk trader berbasis data
· Evidence: Blur Marketplace meluncurkan tanpa platform fee (EV-002), bidding kolektif dan trait bids menarik power trader; market share 60-75% konstan sejak Q1 2023 (Phase 8 Market Share)
· Supporting Dataset: Phase 3 EV-002, Phase 8 Market Share, Phase 4 System Architecture

2. Membangun lapisan finansialisasi NFT (NFTfi) via Blend sebagai diferensiasi struktural dari kompetitor marketplace murni
· Evidence: Blend launch Mei 2023 (EV-010) sebagai protokol lending peer-to-peer perpetual tanpa token sendiri; TVL puncak >$200M; market share lending 40-60% (Phase 8 Market Share)
· Supporting Dataset: Phase 3 EV-010, Phase 4 Core Components (Blend Contract), Phase 8 Competitor Landscape

3. Transisi kendali dari company (Blur Labs) ke DAO melalui token BLUR dengan fee switch sebagai value accrual
· Evidence: TGE Feb 2023 (EV-004) + DAO formation (EV-007) + Fee switch activation Feb 2024 (EV-013) mengarahkan 0.5% protocol fee ke staker; governance via Snapshot off-chain + multisig execution
· Supporting Dataset: Phase 3 EV-004, EV-007, EV-013, Phase 6 Governance, Phase 2 Blur DAO entity

4. Mempertahankan alignment Ethereum-only (no L2, no multi-chain) sebagai moat teknis dan naratif
· Evidence: Tidak ada deployment L2 per 2024-10 (Phase 4 Known Limitations); founder PacmanBlur publik pro-Ethereum L1 (Phase 8 Narrative Position)
· Supporting Dataset: Phase 4 System Architecture, Phase 8 Narrative Position, Phase 3 EV-015

5. Menggunakan insentif token berkelanjutan (Season 1-3) untuk bootstrap liquidity dan user retention tanpa public sale
· Evidence: Season 1 airdrop 360M BLUR (12% supply) ke trader pre-TGE (EV-004); Season 2-3 reward trading/bidding/Blend (EV-011, EV-012); no IDO/public sale (Phase 6 Token Sale)
· Supporting Dataset: Phase 3 EV-004, EV-011, EV-012, Phase 6 Distribution & Vesting

Keputusan: Launch Mainnet Blur Marketplace tanpa testnet publik (2022-10-19)
· Trigger: Kebutuhan time-to-market cepat untuk menangkap momentum NFT bear market 2022 dan mengisi kekosongan fitur pro-trader (bidding pools, aggregator) yang OpenSea tidak layani
· Evidence: Blur Blog "Introducing Blur" menegaskan focus pada "pro traders" dan "aggregator" (Phase 3 EV-002); Phase 4 Architecture menyearkan off-chain orderbook langsung live
· Decision: Deploy kontrak marketplace (Exchange, Bidding) ke Ethereum mainnet langsung 19 Okt 2022 tanpa fase testnet terpisah
· Immediate Result: Marketplace live, volume awal didorong oleh power trader early adopter; zero platform fee menarik volume dari OpenSea
· Long-term Impact: Menetapkan Blur sebagai "pro-first" marketplace; market share naik >60% dalam 6 bulan (EV-015); etablish reputasi speed of execution
· Supporting Dataset: Phase 3 EV-002, Phase 4 System Architecture, Phase 8 Market Timeline

Keputusan: Series A $11M dari Paradigm valuasi $1B (2022-11-01)
· Trigger: Perlu dana ekspansi tim, infrastruktur off-chain orderbook, dan runway 3-4 tahun pasca-launch marketplace
· Evidence: TechCrunch & Paradigm announcement konfirmasi $11M Series A led by Paradigm (Phase 3 EV-003); Variant Fund seed earlier (Phase 2 Investors)
· Decision: Terima Series A $11M dari Paradigm (lead) + Variant + Cozomo de' Medici angel pada valuasi $1B pre-revenue
· Immediate Result: Treasury Blur Labs funded; Paradigm join board/advisory; credibility signal ke market & talent
· Long-term Impact: Paradigm network akses ke ekosistem Ethereum, talent hiring, strategic advice; investor allocation token vesting 4-5 tahun menciptakan overhang supply (Phase 6 Vesting)
· Supporting Dataset: Phase 3 EV-003, Phase 2 Paradigm entity, Phase 6 Vesting Schedule

Keputusan: TGE BLUR token + Season 1 airdrop + Binance/Coinbase listing same day (2023-02-14)
· Trigger: Perlu token untuk governance DAO, incentive alignment, dan liquidity exit untuk investor/team; momentum market share naik butuh retentie user
· Evidence: Blur Blog "BLUR Token" announcement (Phase 3 EV-004); Binance listing announcement same day (EV-005); Coinbase next day (EV-006); 51% supply ke community (Phase 6 Distribution)
· Decision: Deploy token contract 3B supply, mint ke multisig; 12% (360M) claimable immediate Season 1 airdrop; listing Binance (spot+perp) & Coinbase (experimental) hari yang sama
· Immediate Result: Price discovery instan; >$1B volume hari pertama; 150k+ holders; Season 1 claim rate tinggi; market maker Wintermute/GSR provide liquidity
· Long-term Impact: Token menjadi mata uang incentive Season 2-3; fee switch Feb 2024 memberi utility real yield; investor/team cliff 1 tahun mulai unlock Feb 2024 (Phase 6 Major Token Events)
· Supporting Dataset: Phase 3 EV-004, EV-005, EV-006, Phase 6 TGE & Distribution, Phase 8 Market Timeline

Keputusan: Launch Blend Protocol (NFT Lending) setelah dual audit (2023-05-01)
· Trigger: Peluang NFTfi emerging (BendDAO, NFTX); user Blur minta yield pada NFT idle; perlu diferensiasi produk dari OpenSea/Magic Eden
· Evidence: Trail of Bits audit Apr 2023 (EV-008) + OpenZeppelin audit Apr 2023 (EV-009); Blur Blog "Blend" launch (EV-010); Blend contract deploy 1 Mei 2023
· Decision: Deploy Blend sebagai protokol terpisah (contract 0x2946...) dengan model peer-to-peer perpetual loan, oracle Uniswap V3 TWAP, no token
· Immediate Result: $100M+ loan volume minggu pertama; TVL naik >$200M puncak; Blur marketplace volume bertahan via Blend integration
· Long-term Impact: Blend jadi revenue source kedua (protocol fee lending); market share lending 40-60% (Phase 8); no token menghindari regulatory complexity tapi limit governance Blend ke DAO Blur
· Supporting Dataset: Phase 3 EV-008, EV-009, EV-010, Phase 4 Core Components (Blend), Phase 8 Competitor Landscape

Keputusan: Aktifkan Fee Switch 0.5% ke BLUR staker via governance (2024-02 approx)
· Trigger: Token BLUR perlu utility beyond governance; community & investor pressure untuk value accrual; Season 3 ending, perlu retentie staker
· Evidence: Snapshot proposal passed (EV-013); 0.5% protocol fee dari marketplace flow ke delegator; staker >25k addresses (Phase 8 Adoption Metrics)
· Decision: Governance proposal mengaktifkan fee switch pada marketplace contract; fee yang sebelumnya 0% (kecuali royalty) jadi 0.5% protocol fee → staker
· Immediate Result: BLUR staking yield ~10-20% APR (variable); delegasi naik; price support pasca-unlock team/investor cliff Feb 2024
· Long-term Impact: Tokenomics shift dari pure incentive ke real yield; DAO treasury management jadi kritis; fee switch parameter controllable via future proposals
· Supporting Dataset: Phase 3 EV-013, Phase 6 Utility (Staking/Fee Switch), Phase 8 Adoption Metrics

Keputusan: Tidak deploy ke L2 (Arbitrum/Optimism/Base/Blast) hingga 2024-10
· Trigger: Ethereum L1 gas tinggi tapi security & liquidity terpusat; kompetitor (OpenSea, Magic Eden) multi-chain; narasi "Ethereum alignment" diferensiasi
· Evidence: Phase 4 Known Limitations "No L2 deployment resmi"; Phase 8 Narrative "Ethereum Alignment"; Phase 3 EV-015 anniversary blog tidak mention L2
· Decision: Fokus resource pada Ethereum L1 only; optimize gas via contract upgrades; mobile app beta (EV-014) sebagai akses retail alternative
· Immediate Result: Power trader remain di L1 (gas insensitive); retail user terbatas oleh gas cost; volume share dominan tetap di L1
· Long-term Impact: Risk market share erosion ke L2 NFT marketplace (Blur di Base, OpenSea di Base/Arbitrum); potential future pivot jika L2 volume > L1
· Supporting Dataset: Phase 4 Known Limitations, Phase 8 Narrative Position, Phase 3 EV-014, EV-015

Keputusan: Multisig (Blur Labs) memegang admin key kontrak hingga 2024-10 (belum full timelock/DAO)
· Trigger: Perlu kecepatan upgrade parameter (fee, royalty logic, pause) di early stage; DAO governance off-chain Snapshot belum mature untuk emergency response
· Evidence: Etherscan owner address 0x5c8D... labeled "Blur: Owner" (Phase 4 Security Model); Phase 2 Blur Multisig entity; Phase 6 Governance "multisig execution"
· Decision: Retain upgrade authority & parameter control di Gnosis Safe multisig (3-5 signer assumed) بدلاً dari timelock contract controlled by DAO
· Immediate Result: Bisa upgrade cepat (gas optimization, royalty enforcement fix); centralization risk tinggi (single point of failure)
· Long-term Impact: Trust assumption pada Blur Labs/team; regulatory risk (SEC control person); DAO governance advisory only; community pressure untuk timelock meningkat
· Supporting Dataset: Phase 4 Security Model, Phase 2 Blur Multisig, Phase 6 Governance, Phase 5 Financial Risk

Pola 1: Ethereum Alignment First — Semua deployment kontrak (Marketplace, Blend, BLUR Token) hanya di Ethereum Mainnet; tidak ada L2/multi-chain meski gas tinggi dan kompetitor multi-chain
· Decision Pattern: Pilih Ethereum L1 sebagai settlement layer tunggal; tolak multi-chain expansion untuk menjaga security, liquidity concentration, dan narasi "purist"
· Evidence: Phase 4 System Architecture "Cross-chain: Tidak ada"; Phase 8 Narrative "Ethereum Alignment"; Phase 3 EV-002, EV-004, EV-010 all Ethereum Mainnet
· Supporting Dataset: Phase 4, Phase 8, Phase 3

Pola 2: Off-chain Orderbook Terpusat untuk Performa — Matching engine & orderbook di server Blur Labs (Web2 style) bukan on-chain (Seaport style) demi latency rendah, gas efficiency, dan fitur advanced (trait bids, collection bids)
· Decision Pattern: Hybrid architecture — off-chain matching + on-chain settlement; trust assumption pada operator Blur untuk fair ordering
· Evidence: Phase 4 Core Components "Off-chain Orderbook & Matching Engine"; Phase 4 Known Limitations "Orderbook Off-chain Terpusat"; Phase 3 EV-002 launch blog
· Supporting Dataset: Phase 4, Phase 3 EV-002

Pola 3: Dual Audit untuk Produk Baru Berisiko Tinggi (Blend) — Blend mendapatkan audit Trail of Bits + OpenZeppelin sebelum launch; Marketplace core contracts tidak audit publik dari firma top-tier
· Decision Pattern: Produk baru dengan kompleksitas finansial tinggi (lending, liquidation, oracle) wajib dual audit; produk existing (marketplace) rely pada battle-testing live
· Evidence: Phase 3 EV-008, EV-009 (Blend audits); Phase 4 Audit History "Tidak ada audit publik untuk Marketplace core contracts"
· Supporting Dataset: Phase 3, Phase 4

Pola 4: Upgrade via Proxy Pattern (TransparentUpgradeableProxy/UUPS) — Semua kontrak inti (Marketplace, Blend, Token) menggunakan upgradeable proxy dikontrol multisig
· Decision Pattern: Fleksibilitas upgrade parameter & logic tanpa migrasi kontrak; trade-off centralization risk pada admin key
· Evidence: Phase 4 Security Model "Upgradeability: proxy pattern"; Phase 4 Technical Upgrade History multiple upgrades via proxy
· Supporting Dataset: Phase 4

Pola 5: OpenZeppelin Library sebagai Standard — ERC-20, AccessControl, ReentrancyGuard, Upgradeable Proxy semua dari OpenZeppelin Contracts v4.x
· Decision Pattern: Minimalkan custom cryptography/security code; gunakan library battle-tested; audit fokus pada business logic bukan primitive
· Evidence: Phase 4 Development Framework "OpenZeppelin Contracts"; Etherscan contract code verification shows OpenZeppelin imports
· Supporting Dataset: Phase 4

Pola 1: VC Funding Tunggal Series A Large ($11M at $1B) — Tidak ada public sale, tidak ada strategic round berulang; single large Series A dari Paradigm cukup untuk runway panjang
· Decision Pattern: Amati capital efficiency; raise once at high valuation dari top-tier VC (Paradigm) yang bawa network value > capital; avoid dilution berantai
· Evidence: Phase 3 EV-003 Series A only; Phase 5 Funding History hanya 2 rounds (Seed undisclosed + Series A $11M); Phase 2 Investors hanya Paradigm & Variant
· Supporting Dataset: Phase 3, Phase 5, Phase 2

Pola 2: Token Allocation Community-Heavy (51%) — Mayoritas supply ke community/treasury/ecosystem; team & investor allocation tidak diungkap exact tapi vesting 4-5 tahun cliff 1 tahun
· Decision Pattern: Align incentive jangka panjang ke community growth; VC/team locked lama mencegah dump early; DAO treasury besar untuk self-funding future
· Evidence: Phase 6 Distribution "Community 51%"; Phase 6 Vesting "Team/Investor 4-5 year linear"; Phase 5 Treasury "DAO Treasury 51% supply"
· Supporting Dataset: Phase 5, Phase 6

Pola 3: Revenue dari Protocol Fee (Fee Switch) + Blend Fees — Zero platform fee awal → Fee switch 0.5% Feb 2024 ke staker; Blend lending fee sejak launch Mei 2023
· Decision Pattern: Bootstrap volume dengan zero fee → monetize via governance-activated fee switch; lending sebagai revenue stream kedua independen
· Evidence: Phase 3 EV-002 "zero platform fee"; EV-013 "fee switch activated"; EV-010 "Blend fee live"; Phase 5 Revenue Model
· Supporting Dataset: Phase 3, Phase 5

Pola 4: Treasury Concentrated di Native Token (BLUR) — Tidak ada disclosure diversifikasi treasury ke stablecoin/ETH/blue-chip; mayoritas aset DAO = BLUR token
· Decision Pattern: Bet pada appreciation token sendiri; high beta exposure; risk jika bear market NFT + token price crash simultan
· Evidence: Phase 5 Treasury "Composition tidak diungkap"; Phase 5 Financial Risk "Treasury Concentration HIGH"; Phase 6 Distribution "51% community includes treasury"
· Supporting Dataset: Phase 5, Phase 6

Pola 5: Market Maker Professional (Wintermute, GSR) pada TGE — Engage top-tier market maker untuk liquidity CEX/DEX hari launch; tidak rely pada community liquidity saja
· Decision Pattern: Ensure tight spreads & depth dari hari pertama; professional MM reduce volatility & support price discovery; cost = token loan/option (undisclosed)
· Evidence: Phase 3 EV-004, EV-005 Wintermute/GSR mention; Phase 2 Wintermute/GSR entities; Phase 5 Financial Dependencies
· Supporting Dataset: Phase 3, Phase 2, Phase 5

Pola 1: Integrasi Vertikal (Marketplace + Lending) — Blend dibangun in-house, terintegrasi UI di Blur.io, share user base & NFT collateral; bukan partnership eksternal
· Decision Pattern: Build core financial primitive (lending) sendiri daripada integrate BendDAO/NFTX; control UX, fee, risk parameters; faster iteration
· Evidence: Phase 3 EV-010 Blend launch; Phase 4 Core Components Blend Contract; Phase 7 Applications "Blend Protocol (Web Interface via Blur.io)"
· Supporting Dataset: Phase 3, Phase 4, Phase 7

Pola 2: Dependency Minimal pada External Protocol — Hanya dependency kritis: Ethereum (L1), OpenZeppelin (lib), Uniswap V3 (oracle Blend), Gnosis Safe (multisig); tidak bergantung pada oracle chainlink, cross-chain bridge, atau middleware lain
· Decision Pattern: Minimalkan external smart contract risk; gunakan primitives yang sudah battle-tested (Uniswap TWAP untuk oracle); build sendiri kalau perlu
· Evidence: Phase 7 External Dependencies list; Phase 4 Core Components; Phase 3 EV-010 Blend oracle Uniswap V3
· Supporting Dataset: Phase 7, Phase 4, Phase 3

Pola 3: CEX Listing Strategy — Top-tier CEX only (Binance, Coinbase) pada TGE; tidak listing mass-market ke banyak CEX kecil; perp futures di Binance/Bybit/OKX untuk hedging
· Decision Pattern: Quality over quantity; Binance untuk global liquidity, Coinbase untuk US retail access; perp untuk institutional hedging & price discovery
· Evidence: Phase 3 EV-005 Binance, EV-006 Coinbase; Phase 8 Exchange Ecosystem major CEX listed; Phase 7 Exchange Ecosystem
· Supporting Dataset: Phase 3, Phase 8, Phase 7

Pola 4: Wallet Agnostic (No Official Wallet Partnership) — Tidak ada wallet "official partner"; support standar EIP-1193/WalletConnect; MetaMask, Rabby, Coinbase Wallet, Rainbow, Ledger semua work out-of-box
· Decision Pattern: Neutral infrastructure; tidak lock-in ke wallet tertentu; user experience consistent across wallets
· Evidence: Phase 7 Wallet Ecosystem "Catatan: Blur tidak mempublikasikan daftar wallet resmi"; all standard Ethereum wallets supported
· Supporting Dataset: Phase 7

Pola 5: Developer Ecosystem Minimal (No SDK, No Grants, No Hackathon) — Fokus pada API publik (REST/GraphQL) untuk power trader/bot; tidak invest pada builder ecosystem (SDK, grants, hackathon)
· Decision Pattern: Target user = trader bukan builder; API cukup untuk bot/terminal; resource allocation ke core product (matching engine, mobile) bukan developer tooling
· Evidence: Phase 7 Developer Ecosystem "Tidak ada SDK resmi", "Tidak ada grant program", "Tidak ada hackathon"; Phase 4 API/Indexer operational
· Supporting Dataset: Phase 7, Phase 4

Pola 1: Governance Off-chain Signaling (Snapshot) + Multisig Execution — Proposal di Snapshot (blur.eth), voting token-weighted, execution via Blur Multisig; belum full on-chain timelock
· Decision Pattern: Speed & flexibility early stage; off-chain gasless voting; multisig execution cepat; gradual decentralization path
· Evidence: Phase 3 EV-007 DAO formation; Phase 6 Governance "Snapshot off-chain, multisig execution"; Phase 2 Blur DAO entity
· Supporting Dataset: Phase 3, Phase 6, Phase 2

Pola 2: Token-Weighted Voting (1 BLUR = 1 Vote) — Delegation supported; no quadratic voting, no vote-escrow (veToken), no reputation weighting
· Decision Pattern: Simple, plutocratic governance; whale/investor dominance accepted; delegation allows community representation
· Evidence: Phase 6 Governance "1 BLUR = 1 vote"; Phase 6 Holder Distribution "Whale concentration tinggi"; Phase 3 EV-013 fee switch proposal passed
· Supporting Dataset: Phase 6, Phase 3

Pola 3: DAO Treasury Management via Proposal — Spending dari treasury (51% supply) melalui proposal Snapshot → multisig execution; no automated budget, no stream payments
· Decision Pattern: Ad-hoc treasury management; high friction untuk recurring ops; community entscheiden each spend
· Evidence: Phase 6 Governance "Treasury Governance: DAO mengelola treasury melalui proposal spending"; Phase 5 Treasury "Custodian: Blur DAO via governance proposal"
· Supporting Dataset: Phase 5, Phase 6

Pola 4: Parameter Control Gradual Handover — Fee switch (0.5%) activated via proposal; future parameter (royalty enforcement, Blend params) bisa di-propose; admin key masih di multisig
· Decision Pattern: Incremental decentralization; critical params (pause, upgrade) remain multisig; revenue params (fee) moved to DAO first
· Evidence: Phase 3 EV-013 fee switch; Phase 4 Security Model "Admin Control: Multisig memegang ownership"; Phase 6 Governance status "Active"
· Supporting Dataset: Phase 3, Phase 4, Phase 6

Pola 5: No Formal Dispute Resolution / Legal Wrapper — DAO unincorporated; no legal entity for DAO (Blur Labs Inc is company); multisig signers unknown legal liability
· Decision Pattern: Pure code-based governance; legal ambiguity accepted; rely on Delaware corp (Blur Labs) untuk legal compliance
· Evidence: Phase 2 Entities "Blur Labs Inc" only company; "Blur DAO" as DAO type; Phase 5 Legal Financial Risk "Status regulasi token BLUR belum jelas"
· Supporting Dataset: Phase 2, Phase 5

Pola 1: Security Incident Response — Audit Pre-Launch (Blend Dual Audit) — Tidak ada exploit major historis; responsif via audit sebelum launch produk berisiko tinggi (Blend)
· Decision Pattern: Preventive security > reactive; invest dual audit top-tier untuk lending protocol; marketplace rely pada battle-testing live volume
· Evidence: Phase 3 EV-008, EV-009 Blend audits; Phase 4 Audit History "Marketplace contracts tidak audit publik"; Phase 4 Known Limitations "Marketplace Contracts Unaudited HIGH"
· Supporting Dataset: Phase 3, Phase 4

Pola 2: Market Crash Response — Incentive Season Extension (Season 2→3) — Saat NFT bear market 2023, Blur lanjutkan Season 2 & 3 reward untuk retain volume & market share
· Decision Pattern: Counter-cyclical incentive spending; gunakan treasury token (51% supply) untuk subsidize volume; defend market share posisi #1
· Evidence: Phase 3 EV-011 Season 2 (May-Nov 2023), EV-012 Season 3 (Nov 2023-Feb 2024); Phase 8 Adoption Metrics volume sustained; Phase 5 Financial Risk "Revenue Decline Risk HIGH"
· Supporting Dataset: Phase 3, Phase 8, Phase 5

Pola 3: Regulatory Ambiguity Response — No Geo-blocking, No KYC, Token Utility Real (Fee Switch) — Tidak implement KYC/geo-block; fee switch Feb 2024 memberi "real yield" utility argument; legal opinion tidak publik
· Decision Pattern: Operate sebagai protocol global permissionless; utility token argument via fee switch; accept US regulatory risk (Paradigm backed, Coinbase listed)
· Evidence: Phase 8 Geographic Focus "Global, no restriction"; Phase 3 EV-013 fee switch; Phase 5 Legal Financial Risk MEDIUM; Phase 2 Coinbase investor/listing
· Supporting Dataset: Phase 8, Phase 3, Phase 5, Phase 2

Pola 4: Centralization Risk Mitigation — Multisig (Gnosis Safe) bukan single EOA; 3-5 signer assumed; timelock tidak ada tapi multisig raise attack threshold
· Decision Pattern: Pragmatic decentralization; multisig cukup untuk now; timelock/DAO kan di future roadmap (tidak veröffentlichte)
· Evidence: Phase 4 Security Model "Admin Control: Multisig"; Phase 2 Blur Multisig entity; Phase 6 Governance "multisig execution"
· Supporting Dataset: Phase 4, Phase 2, Phase 6

Pola 5: Competitive Pressure Response — Feature Parity + Innovation (Mobile App, Trait Bids, Blend) — Saat OpenSea launch Seaport/Pro, Blur launch Mobile App Beta (EV-014) & Blend (EV-010); feature differentiation terus
· Decision Pattern: Product velocity sebagai moat; ship fast, iterate; mobile untuk retail expansion; Blend untuk NFTfi moat
· Evidence: Phase 3 EV-010 Blend, EV-014 Mobile App; Phase 8 Competitor Landscape vs OpenSea/Magic Eden; Phase 4 Technical Upgrade History
· Supporting Dataset: Phase 3, Phase 8, Phase 4

Pola 1: Speed-to-Market > Perfect Decentralization — Launch marketplace mainnet tanpa testnet (EV-002); launch token dengan multisig control (EV-004); Blend launch setelah audit tapi admin key multisig (EV-010)
· Evidence: Phase 3 timeline compressed (Oct 2022 launch → Feb 2023 TGE → May 2023 Blend); Phase 4 admin key multisig retained; Phase 8 Growth stage
· Supporting Dataset: Phase 3, Phase 4, Phase 8

Pola 2: Incentive-Driven Growth Loops — Season 1 airdrop → volume spike → Season 2-3 reward → volume sustain → fee switch → staking yield → retention
· Evidence: Phase 3 EV-004, EV-011, EV-012, EV-013 sequential; Phase 8 Adoption Metrics volume & stakers; Phase 6 Utility incentive + staking
· Supporting Dataset: Phase 3, Phase 8, Phase 6

Pola 3: Vertical Integration over Partnerships — Build Blend in-house bukan partner BendDAO; build mobile app in-house bukan partner wallet; build orderbook in-house bukan use Seaport
· Evidence: Phase 7 Major Integrations mostly internal; Phase 4 Core Components all proprietary contracts; Phase 7 Developer Ecosystem minimal
· Supporting Dataset: Phase 7, Phase 4

Pola 4: Ethereum Maximalism as Strategy — No L2, no multi-chain, no bridging; bet on Ethereum L1 settlement dominance untuk high-value NFT
· Evidence: Phase 4 Cross-chain "Tidak ada"; Phase 8 Narrative "Ethereum Alignment"; Phase 3 all events Ethereum Mainnet only
· Supporting Dataset: Phase 4, Phase 8, Phase 3

Pola 5: VC-Backed but Community-Owned Narrative — Paradigm $11M Series A (VC control) tapi 51% token ke community; DAO governance advisory; fee switch ke staker
· Evidence: Phase 2 Paradigm investor; Phase 6 Distribution 51% community; Phase 3 EV-013 fee switch; Phase 6 Governance multisig execution
· Supporting Dataset: Phase 2, Phase 6, Phase 3

Trade-off 1: Desentralisasi vs Kecepatan Eksekusi (Speed)
· Decision: Retain admin key & upgrade authority di Blur Multisig (company-controlled) daripada timelock/DAO dari hari pertama
· Trade-off: Kecepatan upgrade parameter (fee, royalty, pause, gas opt) dan emergency response ditukar dengan centralization risk (single point of failure, regulatory exposure, trust assumption)
· Evidence: Phase 4 Security Model "Admin Control: Multisig memegang ownership"; Phase 4 Technical Upgrade History multiple upgrades via proxy; Phase 5 Financial Risk "Admin Key Financial Risk HIGH"
· Supporting Dataset: Phase 4, Phase 5

Trade-off 2: On-chain Orderbook (Trustless) vs Off-chain Orderbook (Performa)
· Decision: Off-chain centralized matching engine (Web2 style) untuk latency rendah, gas efficiency, fitur advanced (trait bids, collection bids)
· Trade-off: Performa & UX pro-trader ditukar dengan trust assumption pada operator Blur (fair ordering, no front-running, censorship resistance); tidak verifiable on-chain
· Evidence: Phase 4 System Architecture "Off-chain Orderbook & Matching Engine"; Phase 4 Known Limitations "Orderbook Off-chain Terpusat HIGH"; Phase 8 Competitor vs OpenSea Seaport on-chain
· Supporting Dataset: Phase 4, Phase 8

Trade-off 3: Multi-chain Expansion (User Growth) vs Ethereum L1 Focus (Liquidity Concentration)
· Decision: Tidak deploy ke L2 (Arbitrum, Base, Optimism, Blast) hingga 2024-10; fokus resource pada Ethereum L1
· Trade-off: Retail user & volume di L2 dikorbankan untuk menjaga liquidity concentration di L1, security alignment, dan narasi diferensiasi; risk market share erosion ke competitor multi-chain
· Evidence: Phase 4 Known Limitations "No L2 deployment"; Phase 8 Narrative "Ethereum Alignment"; Phase 8 Competitor Magic Eden/OpenSea multi-chain
· Supporting Dataset: Phase 4, Phase 8

Trade-off 4: Zero Platform Fee (Growth) vs Protocol Fee Sustainability (Revenue)
· Decision: Zero platform fee launch Oct 2022 → Fee switch 0.5% Feb 2024 via governance (16 bulan zero revenue)
· Trade-off: User acquisition & market share dominance awal ditukar dengan delayed monetization; fee switch activation bergantung pada DAO vote (uncertainty)
· Evidence: Phase 3 EV-002 "zero platform fee"; EV-013 "fee switch activated"; Phase 5 Revenue Model "Protocol Fee Live (fee switch activated Feb 2024)"
· Supporting Dataset: Phase 3, Phase 5

Trade-off 5: Token Incentive Cost (Inflationary Pressure) vs Volume Retention
· Decision: Season 1-3 allocate ~39% supply (51% community includes future) untuk incentive trading/bidding/lending selama ~1 tahun
· Trade-off: Sell pressure dari claimer & farmer ditukar dengan volume dominance & market share; fee switch Feb 2024 offset sebagian via buy pressure staking
· Evidence: Phase 6 Distribution "Community 51% includes Season 1-3"; Phase 3 EV-004, EV-011, EV-012; Phase 8 Adoption Metrics volume sustained
· Supporting Dataset: Phase 6, Phase 3, Phase 8

Trade-off 6: Blend No Token (Regulatory Simplicity) vs Blend Governance Integration
· Decision: Blend protocol tidak punya token sendiri; governance Blend parameter via Blur DAO (BLUR token); no direct BLUR utility di Blend smart contract
· Trade-off: Regulatory simplicity & focus liquidity ke BLUR token ditukar dengan limited governance granularity untuk Blend-specific params (LTV, oracle, liquidation)
· Evidence: Phase 4 Core Components Blend Contract no token; Phase 6 Utility "BLUR tidak digunakan di Blend"; Phase 3 EV-010 Blend launch
· Supporting Dataset: Phase 4, Phase 6, Phase 3

Behavioral Summary

Prioritas Utama Proyek:
1. Market share dominance di NFT trading Ethereum (pro-trader segment) — terukur via volume share 60-75% konstan
2. Product velocity & feature differentiation — ship fast: marketplace, Blend, mobile app, fee switch dalam 2 tahun
3. Token incentive alignment — 51% supply ke community, seasonal rewards, fee switch real yield
4. Ethereum alignment sebagai moat naratif & teknis — no L2, no multi-chain

Cara Mengambil Keputusan:
- Founder-led (PacmanBlur, Galaga, Lord_kekl) dengan input Paradigm strategic; decision speed tinggi
- Data-driven dari on-chain metrics (volume, bid activity, loan volume) untuk design incentive
- Governance advisory via Snapshot; execution control di multisig (company) untuk kecepatan
- Risk tolerance tinggi pada centralization (admin key, off-chain orderbook) demi speed & UX

Faktor Paling Sering Mempengaruhi Keputusan:
1. Competitive positioning vs OpenSea/Magic Eden (feature parity + differentiation)
2. Trader feedback & on-chain behavior (bidding patterns, loan demand)
3. Token price & liquidity management (MM engagement, fee switch timing, vesting cliff)
4. Paradigm network & strategic advice (Series A lead investor)
5. Regulatory environment US (token utility argument, Coinbase listing, no KYC)

Pola Evolusi:
Phase 1 (Oct 2022-Feb 2023): Marketplace launch → VC funding → Token TGE + Airdrop + CEX listing (bootstrap)
Phase 2 (Mar-Nov 2023): Blend launch (NFTfi vertical) → Season 2-3 incentives (retention) → Volume dominance established
Phase 3 (Feb 2024-sekarang): Fee switch activation (monetization) → Mobile app beta (retail expansion) → Sustained leadership

Kekuatan Utama:
- Product execution speed & quality (off-chain orderbook performance, Blend innovation)
- Trader-centric UX moat (bidding pools, trait bids, API for bots)
- Capital efficiency (single Series A, community-heavy tokenomics)
- Paradigm backing (talent, network, credibility)
- Vertical integration (Marketplace + Lending + Token flywheel)

Kelemahan Utama:
- Centralization risk tinggi (multisig admin key, off-chain orderbook, no timelock)
- Treasury concentration di BLUR token (no diversification disclosed)
- No L2/multi-chain strategy (retail exclusion, competitor encroachment)
- Marketplace contracts unaudited (security debt)
- Governance not fully decentralized (multisig execution, plutocratic voting)
- Developer ecosystem minimal (no SDK, grants, hackathon)
- Regulatory ambiguity (token utility

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
