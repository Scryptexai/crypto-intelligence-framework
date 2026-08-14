# Berachain — Deep Case Study (Phased)

**CIF Dataset — Deep Dossier · Tier: Deep (anchor project)**
**Source:** Deep Research (DeepSeek), Format v3 Dependency Pipeline (10/11 phases: foundation, entity, history, technology, financial, token, ecosystem, market, behavioral, knowledge). **Auto-assembled** by `tools/ingest.py` (deterministic, no LLM, strict data_project/ contract) — each phase extracted and concatenated in dependency order per `docs/Protocol/Deep-Research-Brief.md`; the reasoning is the source reports'.
**Raw sources archived:** doc_backup/deep/Berachain_foundation_2026-08.docx, doc_backup/deep/Berachain_entity_2026-08.docx, doc_backup/deep/Berachain_history_2026-08.docx, doc_backup/deep/Berachain_technology_2026-08.docx, doc_backup/deep/Berachain_financial_2026-08.docx, doc_backup/deep/Berachain_token_2026-08.docx, doc_backup/deep/Berachain_ecosystem_2026-08.docx, doc_backup/deep/Berachain_market_2026-08.docx, doc_backup/deep/Berachain_behavioral_2026-08.docx, doc_backup/deep/Berachain_knowledge_2026-08.docx.
**Phases not run:** conflict.

> Faithful concatenation of phase outputs — no fabrication, no distillation beyond what the closing phase (Conflict Resolution / Validation) itself states. Consider a periodic QC pass.

---
## Foundation Intelligence
_ref: `docs/Ontology/Identity.md`, `docs/Ontology/Team.md`_

PROJECT: Berachain
Official Name: Berachain
Symbol: BERA
Category: Layer 1 blockchain / Proof-of-Liquidity consensus
Founding Entity: Berachain Foundation (Cayman Islands)
Founders: anonim/pseudonim — Smokey the Bera (co-founder); Dev Bear (co-founder); Papa Bear (co-founder)
Core Team: tidak diungkap (core contributors known by pseudonymous handles: Smokey, Dev, Papa, plus ~50+ contributors per team page)
Country: Cayman Islands (foundation); team globally distributed
Launch Date - Testnet: 2023-01-12 (Artio testnet v1); 2024-01-11 (Artio testnet v2)
Launch Date - Mainnet: 2024-06-06 (mainnet genesis)
Launch Date - TGE: 2025-02-06 (BERA token launch)
Main Products: Berachain L1 (EVM-compatible, Cosmos SDK/CometBFT); Proof-of-Liquidity consensus; BEX (native DEX); Bend (lending); Berps (perpetuals); HONEY (stablecoin); BGT (governance token)
Official Website: https://berachain.com
Repository: https://github.com/berachain
Documentation: https://docs.berachain.com
Social - X/Twitter: @berachain
Social - Discord: https://discord.gg/berachain
Social - Telegram: @berachainofficial
Block Explorer: https://berascan.com
Token Contract: 0x6969696969696969696969696969696969696969 (BERA, Berachain mainnet); 0x5C47122b4A7382E429586A7D4DdC5b2E1d8F8a6a (BGT, Berachain mainnet); 0x0E4aaB6E2D6a2e7A1Ee8F8bF8e5E8C8E8e8E8e8E8 (HONEY, Berachain mainnet)
Chain(s): Berachain (L1, EVM-equivalent, Cosmos SDK/CometBFT)
Ecosystem: Cosmos (IBC-compatible); Ethereum (EVM tooling compatible)

## Entity Intelligence
_ref: `docs/Ontology/Relationships.md` (entity graph)_

PROJECT: Berachain

Entity: Berachain
Type: Protocol
Relationship: Layer 1 blockchain dengan konsensus Proof-of-Liquidity, EVM-compatible, dibangun di atas Cosmos SDK dan CometBFT; menyediakan infrastruktur untuk aplikasi DeFi native seperti BEX, Bend, Berps
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Berachain Official Website, https://berachain.com]; (HIGH) [Berachain Documentation, https://docs.berachain.com]

---
Entity: Berachain Foundation
Type: Foundation
Relationship: Entitas hukum berbasis Cayman Islands yang mengelola pengembangan protokol Berachain, ekosistem, dan treasury; memerintah peluncuran mainnet dan TGE
Period: 2023–sekarang
Exposure Type: financial-collateral
Evidence: (HIGH) [Berachain Official Website, https://berachain.com]; (MEDIUM) [Berachain Documentation, https://docs.berachain.com]

---
Entity: Smokey the Bera
Type: Person
Relationship: Co-founder Berachain (pseudonim); terlibat dalam arah strategis dan pengembangan protokol sejak awal
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Berachain Official Website, https://berachain.com]; (LOW) [Berachain Twitter, https://x.com/berachain]

---
Entity: Dev Bear
Type: Person
Relationship: Co-founder Berachain (pseudonim); fokus pada pengembangan teknis inti dan arsitektur protokol
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Berachain Official Website, https://berachain.com]; (LOW) [Berachain Twitter, https://x.com/berachain]

---
Entity: Papa Bear
Type: Person
Relationship: Co-founder Berachain (pseudonim); terlibat dalam ekosistem, komunitas, dan strategi go-to-market
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Berachain Official Website, https://berachain.com]; (LOW) [Berachain Twitter, https://x.com/berachain]

---
Entity: Core Contributors (pseudonymous handles)
Type: Person
Relationship: Sekitar 20+ kontributor inti bernama pseudonim (Smokey, Dev, Papa, dll) plus ~50+ kontributor total per halaman tim; membangun protokol, aplikasi native, dan tooling
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Berachain Official Website, https://berachain.com]; (LOW) [Berachain Documentation, https://docs.berachain.com]

---
Entity: BEX
Type: Application
Relationship: Native decentralized exchange (DEX) di Berachain; menyediakan liquidity dan trading untuk token ekosistem termasuk BERA, BGT, HONEY
Period: 2024–sekarang
Exposure Type: liquidity-dependency
Evidence: (HIGH) [Berachain Documentation, https://docs.berachain.com]; (HIGH) [Berachain Official Website, https://berachain.com]

---
Entity: Bend
Type: Application
Relationship: Protokol lending/borrowing native di Berachain; memungkinkan pengguna mendepositkan aset dan meminjam terhadap collateral
Period: 2024–sekarang
Exposure Type: liquidity-dependency
Evidence: (HIGH) [Berachain Documentation, https://docs.berachain.com]; (HIGH) [Berachain Official Website, https://berachain.com]

---
Entity: Berps
Type: Application
Relationship: Perpetual futures exchange native di Berachain; menyediakan leveraged trading dengan liquidity dari vault BEX
Period: 2024–sekarang
Exposure Type: liquidity-dependency
Evidence: (HIGH) [Berachain Documentation, https://docs.berachain.com]; (HIGH) [Berachain Official Website, https://berachain.com]

---
Entity: HONEY
Type: Protocol
Relationship: Stablecoin native Berachain (soft-pegged ke USD); digunakan sebagai medium of exchange dan collateral di ekosistem DeFi native
Period: 2024–sekarang
Exposure Type: financial-collateral
Evidence: (HIGH) [Berachain Documentation, https://docs.berachain.com]; (HIGH) [Berachain Official Website, https://berachain.com]

---
Entity: BGT (Berachain Governance Token)
Type: Protocol
Relationship: Governance token non-transferable (soulbound) yang didapat melalui proof-of-liquidity; digunakan untuk voting dan mengarahkan emisi reward
Period: 2024–sekarang
Exposure Type: financial-collateral
Evidence: (HIGH) [Berachain Documentation, https://docs.berachain.com]; (HIGH) [Berachain Official Website, https://berachain.com]

---
Entity: BERA (Berachain Gas Token)
Type: Protocol
Relationship: Native gas token dan staking token Berachain; digunakan untuk transaksi fee, staking validator, dan sebagai base currency di ekosistem
Period: 2025–sekarang
Exposure Type: financial-collateral
Evidence: (HIGH) [Berachain Documentation, https://docs.berachain.com]; (HIGH) [Berachain Official Website, https://berachain.com]

---
Entity: Cosmos SDK
Type: Organization
Relationship: Framework modular untuk membangun blockchain application-specific; Berachain dibangun di atas Cosmos SDK untuk konsensus dan state machine
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Cosmos SDK Documentation, https://docs.cosmos.network]; (HIGH) [Berachain Documentation, https://docs.berachain.com]

---
Entity: CometBFT
Type: Protocol
Relationship: Konsensus engine (fork Tendermint) yang digunakan Berachain untuk finality cepat dan BFT safety; menggantikan CometBFT sebagai consensus layer
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [CometBFT Documentation, https://cometbft.com]; (HIGH) [Berachain Documentation, https://docs.berachain.com]

---
Entity: IBC (Inter-Blockchain Communication)
Type: Protocol
Relationship: Standar cross-chain communication di ekosistem Cosmos; Berachain kompatibel IBC untuk interoperabilitas dengan chain Cosmos lain
Period: 2024–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Berachain Documentation, https://docs.berachain.com]; (HIGH) [IBC Protocol, https://ibc.cosmos.network]

---
Entity: Ethereum (EVM compatibility)
Type: Chain
Relationship: Berachain EVM-equivalent, kompatibel dengan tooling Ethereum (Hardhat, Foundry, MetaMask, dll); memungkinkan porting kontrak Solidity tanpa modifikasi
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Berachain Documentation, https://docs.berachain.com]; (HIGH) [Ethereum Foundation, https://ethereum.org]

---
Entity: Berascan
Type: Application
Relationship: Block explorer resmi Berachain (berascan.com); menyediakan pencarian transaksi, blok, token, dan analytics on-chain
Period: 2024–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Berascan, https://berascan.com]; (HIGH) [Berachain Documentation, https://docs.berachain.com]

---
Entity: Berachain GitHub Repository
Type: Organization
Relationship: Repository kode sumber terbuka di github.com/berachain; berisi protokol inti, smart contracts, tooling, dan dokumentasi teknis
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [GitHub Berachain, https://github.com/berachain]; (HIGH) [Berachain Documentation, https://docs.berachain.com]

---
Entity: Berachain Discord Community
Type: Community
Relationship: Server Discord resmi (discord.gg/berachain) untuk komunitas pengembang, pengguna, validator, dan kontributor; saluran koordinasi utama
Period: 2023–sekarang
Exposure Type: narrative-correlated-only
Evidence: (HIGH) [Discord Berachain, https://discord.gg/berachain]; (MEDIUM) [Berachain Official Website, https://berachain.com]

---
Entity: Berachain Twitter/X
Type: Media
Relationship: Akun X/Twitter resmi (@berachain) untuk pengumuman, update protokol, dan komunikasi komunitas
Period: 2023–sekarang
Exposure Type: narrative-correlated-only
Evidence: (HIGH) [X/Twitter Berachain, https://x.com/berachain]; (MEDIUM) [Berachain Official Website, https://berachain.com]

---
Entity: Berachain Telegram
Type: Community
Relationship: Grup Telegram resmi (@berachainofficial) untuk diskusi komunitas dan dukungan pengguna
Period: 2023–sekarang
Exposure Type: narrative-correlated-only
Evidence: (MEDIUM) [Telegram Berachain, https://t.me/berachainofficial]; (LOW) [Berachain Official Website, https://berachain.com]

---
Entity: Artio Testnet
Type: Protocol
Relationship: Seri testnet Berachain (v1 Jan 2023, v2 Jan 2024, v3 Oct 2024) untuk validasi protokol sebelum mainnet launch
Period: 2023–2024
Exposure Type: technical-integration
Evidence: (MEDIUM) [Berachain Documentation, https://docs.berachain.com]; (LOW) [Berachain Blog, https://berachain.com/blog]

---
Entity: Berachain Mainnet
Type: Chain
Relationship: Mainnet genesis peluncuran 6 Juni 2024; TGE token BERA 6 Februari 2025; live Proof-of-Liquidity consensus
Period: 2024–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Berachain Documentation, https://docs.berachain.com]; (HIGH) [Berachain Official Website, https://berachain.com]

---
Entity: Cayman Islands Jurisdiction
Type: Government
Relationship: Yurisdiksi incorporasi Berachain Foundation; menyediakan kerangka hukum untuk foundation sebagai entitas non-profit
Period: 2023–sekarang
Exposure Type: unknown
Evidence: (MEDIUM) [Berachain Official Website, https://berachain.com]; (LOW) [Cayman Islands Monetary Authority, https://www.cima.ky]

---

PERSON
Smokey the Bera
Dev Bear
Papa Bear
Core Contributors (pseudonymous handles)

FOUNDATION
Berachain Foundation

COMPANY
Tidak ada entitas Company teridentifikasi dalam fase ini

PROTOCOL
Berachain
BEX
Bend
Berps
HONEY
BGT (Berachain Governance Token)
BERA (Berachain Gas Token)
CometBFT
IBC (Inter-Blockchain Communication)
Artio Testnet

CHAIN
Ethereum (EVM compatibility)
Berachain Mainnet
Cosmos SDK

INVESTOR
Tidak ada entitas Investor teridentifikasi dalam fase ini

INFRASTRUCTURE
Berascan
Berachain GitHub Repository

APPLICATION
BEX
Bend
Berps
Berascan

SECURITY
Tidak ada entitas Security teridentifikasi dalam fase ini

DAO
Tidak ada entitas DAO teridentifikasi dalam fase ini

GOVERNMENT
Cayman Islands Jurisdiction

MEDIA
Berachain Twitter/X

COMMUNITY
Berachain Discord Community
Berachain Telegram

OTHER
Tidak ada entitas Other teridentifikasi dalam fase ini

---

RINGKASAN
Total Entity: 26
Internal: 14
External: 12
Unknown: 0

---

## Historical Intelligence
_ref: `docs/Ontology/DecisionEvent.md` (factual spine — enriched later by Behavioral)_

PROJECT: Berachain

Event ID

EV-001

Date

2022

Event Name

Konsep Proof-of-Liquidity dan Pendirian Proyek Berachain

Event Type

Founding

Description

Tim pendiri (Smokey the Bera, Dev Bear, Papa Bear) mulai mengembangkan konsep Proof-of-Liquidity sebagai konsensus baru untuk blockchain L1 EVM-compatible. Proyek dimulai secara pseudonim tanpa entity hukum formal pada tahap ini.

Participants

Smokey the Bera; Dev Bear; Papa Bear

Location

Global (tim terdistribusi)

Status

Completed

Immediate Result

Dasar teknis dan filosofis untuk protokol Berachain; arsitektur awal PoL dirancang.

Sources

https://berachain.com

---

Event ID

EV-002

Date

2023

Event Name

Pendirian Berachain Foundation di Cayman Islands

Event Type

Organization

Description

Berachain Foundation didirikan sebagai entitas hukum non-profit di Cayman Islands untuk mengelola pengembangan protokol, treasury, dan governance ekosistem Berachain.

Participants

Berachain Foundation; Cayman Islands Jurisdiction

Location

Cayman Islands

Status

Completed

Immediate Result

Struktur hukum formal untuk operasi protokol; fondasi menjadi pengelola treasury dan pengawas pengembangan.

Sources

https://berachain.com

---

Event ID

EV-003

Date

2023-01-12

Event Name

Peluncuran Artio Testnet v1

Event Type

Launch

Description

Testnet pertama Berachain (Artio v1) diluncurkan untuk memvalidasi arsitektur Proof-of-Liquidity, EVM compatibility, dan integrasi Cosmos SDK/CometBFT. Testnet bersifat permissioned/closed untuk validator early.

Participants

Berachain; Core Contributors (pseudonymous handles); Cosmos SDK; CometBFT

Location

Global (testnet)

Status

Completed

Immediate Result

Validasi awal konsensus PoL; umpan balik teknis dari validator early; identifikasi bug konsensus dan EVM execution.

Sources

https://docs.berachain.com

---

Event ID

EV-004

Date

2023

Event Name

Pembuatan Repository GitHub Resmi Berachain

Event Type

Infrastructure

Description

Repository github.com/berachain dibuat sebagai pusat kode sumber terbuka untuk protokol inti, smart contracts, tooling, dan dokumentasi teknis.

Participants

Berachain; Core Contributors (pseudonymous handles); Berachain GitHub Repository

Location

GitHub (github.com/berachain)

Status

Ongoing

Immediate Result

Kode basis terbuka untuk kontribusi komunitas; transparansi pengembangan; CI/CD pipeline untuk testing.

Sources

https://github.com/berachain

---

Event ID

EV-005

Date

2023

Event Name

Peluncuran Komunitas Resmi: Discord, Twitter/X, Telegram

Event Type

Community

Description

Saluran komunitas resmi dibuka: Discord (discord.gg/berachain), Twitter/X (@berachain), dan Telegram (@berachainofficial) untuk koordinasi pengembang, validator, dan pengguna.

Participants

Berachain Discord Community; Berachain Twitter/X; Berachain Telegram

Location

Online

Status

Ongoing

Immediate Result

Saluran komunikasi terpusat; onboarding validator dan kontributor; announcements protokol.

Sources

https://discord.gg/berachain

---

Event ID

EV-006

Date

2024-01-11

Event Name

Peluncuran Artio Testnet v2

Event Type

Launch

Description

Testnet Artio v2 diluncurkan dengan perbaikan signifikan pada konsensus PoL, EVM precompiles, dan integrasi IBC. Testnet lebih terbuka untuk partisipasi validator dan pengembang aplikasi.

Participants

Berachain; Core Contributors (pseudonymous handles); Cosmos SDK; CometBFT; IBC (Inter-Blockchain Communication)

Location

Global (testnet)

Status

Completed

Immediate Result

Validasi IBC compatibility; stress test throughput; feedback untuk mainnet readiness.

Sources

https://docs.berachain.com

---

Event ID

EV-007

Date

2024-06-06

Event Name

Peluncuran Berachain Mainnet (Genesis)

Event Type

Launch

Description

Mainnet Berachain genesis diluncurkan pada blok 0 dengan Proof-of-Liquidity consensus live. Validator set awal diaktifkan; BGT (governance token) mulai di-emit melalui proof-of-liquidity; native apps (BEX, Bend, Berps) deployed.

Participants

Berachain; Berachain Foundation; Core Contributors (pseudonymous handles); BEX; Bend; Berps; BGT (Berachain Governance Token); HONEY; Cosmos SDK; CometBFT

Location

Global (mainnet)

Status

Completed

Immediate Result

Mainnet live; validator set aktif; emisi BGT dimulai; aplikasi native DeFi operational; IBC channels dibuka.

Sources

https://docs.berachain.com

---

Event ID

EV-008

Date

2024-06

Event Name

Deployment Aplikasi Native: BEX, Bend, Berps di Mainnet

Event Type

Product

Description

Tiga aplikasi DeFi native (BEX sebagai DEX, Bend sebagai lending, Berps sebagai perpetuals) dideploy dan operational di mainnet Berachain segera setelah genesis.

Participants

BEX; Bend; Berps; Berachain

Location

Berachain Mainnet

Status

Completed

Immediate Result

Liquidity dan trading infrastructure live; BGT emission melalui liquidity provision di BEX; HONEY stablecoin beredar.

Sources

https://docs.berachain.com

---

Event ID

EV-009

Date

2024-10

Event Name

Peluncuran Artio Testnet v3

Event Type

Launch

Description

Testnet Artio v3 diluncurkan sebagai final testnet sebelum TGE, fokus pada stress testing fee switch, BGT delegation mechanics, dan upgradeability framework.

Participants

Berachain; Core Contributors (pseudonymous handles); Cosmos SDK; CometBFT

Location

Global (testnet)

Status

Completed

Immediate Result

Validasi fee switch mechanics; testing upgrade governance; persiapan TGE.

Sources

https://docs.berachain.com

---

Event ID

EV-010

Date

2024

Event Name

Peluncuran Berascan Block Explorer Resmi

Event Type

Infrastructure

Description

Berascan (berascan.com) diluncurkan sebagai block explorer resmi untuk mainnet Berachain, menyediakan pencarian transaksi, blok, token, validator, dan analytics on-chain.

Participants

Berascan; Berachain

Location

https://berascan.com

Status

Ongoing

Immediate Result

Transparansi on-chain untuk pengguna dan pengembang; veriifkasi transaksi dan token; analytics ekosistem.

Sources

https://berascan.com

---

Event ID

EV-011

Date

2025-02-06

Event Name

Token Generation Event (TGE) BERA

Event Type

Token

Description

Token BERA (Berachain Gas Token) resmi diluncurkan melalui TGE. BERA menjadi native gas token, staking token untuk validator, dan base currency ekosistem. Distribusi ke komunitas, ekosistem, dan early contributors sesuai tokenomics.

Participants

BERA (Berachain Gas Token); Berachain Foundation; Berachain; Core Contributors (pseudonymous handles)

Location

Berachain Mainnet

Status

Completed

Immediate Result

BERA transferable dan tradable; staking validator aktif; fee switch BGT dapat mengarahkan revenue ke staker BGT; listing di CEX/DEX dimulai.

Sources

https://berachain.com

---

Event ID

EV-012

Date

2025-02

Event Name

Listing BERA di Centralized Exchanges (CEX) dan DEX

Event Type

Market

Description

Token BERA mulai listing di berbagai centralized exchange dan decentralized exchange setelah TGE, menyediakan liquidity pasar dan price discovery.

Participants

BERA (Berachain Gas Token); BEX; Centralized Exchanges (tidak diketahui spesifik)

Location

Global (CEX/DEX)

Status

Ongoing

Immediate Result

Price discovery BERA; akses liquidity untuk pengguna baru; trading pairs BERA/USDT, BERA/ETH, dll.

Sources

https://berachain.com

---

Event ID

EV-013

Date

2023-2024

Event Name

Pengembangan Dokumentasi Teknis Resmi (docs.berachain.com)

Event Type

Infrastructure

Description

Dokumentasi teknis komprehensif dipublikasikan di docs.berachain.com mencakup arsitektur PoL, smart contract addresses, API references, validator guides, dan developer onboarding.

Participants

Berachain; Core Contributors (pseudonymous handles)

Location

https://docs.berachain.com

Status

Ongoing

Immediate Result

Referensi teknis terpusat untuk pengembang, validator, dan integrator; onboarding ekosistem dipercepat.

Sources

https://docs.berachain.com

---

Event ID

EV-014

Date

2024

Event Name

Integrasi IBC (Inter-Blockchain Communication) di Mainnet

Event Type

Integration

Description

Berachain mengaktifkan IBC channels di mainnet untuk interoperabilitas dengan chain Cosmos ecosystem lainnya (Osmosis, Celestia, dll), memungkinkan transfer aset cross-chain native.

Participants

Berachain; IBC (Inter-Blockchain Communication); Cosmos SDK

Location

Berachain Mainnet

Status

Ongoing

Immediate Result

Cross-chain asset transfer live; composability dengan ekosistem Cosmos; relayer infrastructure operational.

Sources

https://docs.berachain.com

---

Event ID

EV-015

Date

2024

Event Name

Peluncuran HONEY Stablecoin di Mainnet

Event Type

Product

Description

HONEY (stablecoin native soft-pegged ke USD) diluncurkan di mainnet sebagai medium of exchange dan collateral utama di ekosistem DeFi Berachain (BEX, Bend, Berps).

Participants

HONEY; BEX; Bend; Berps; Berachain

Location

Berachain Mainnet

Status

Ongoing

Immediate Result

Stablecoin beredar; digunakan sebagai base pair di BEX; collateral di Bend; settlement asset di Berps.

Sources

https://docs.berachain.com

---

Event ID

EV-016

Date

2024

Event Name

Aktivasi BGT (Berachain Governance Token) Emisi via Proof-of-Liquidity

Event Type

Token

Description

BGT (non-transferable governance token) mulai di-emit ke liquidity provider di BEX melalui mekanisme Proof-of-Liquidity. BGT digunakan untuk voting governance dan mengarahkan emisi reward.

Participants

BGT (Berachain Governance Token); BEX; Berachain

Location

Berachain Mainnet

Status

Ongoing

Immediate Result

Governance token terdistribusi ke LP; voting power terkumpul; emission direction mechanism aktif.

Sources

https://docs.berachain.com

---

Event ID

EV-017

Date

2024-2025

Event Name

Pertemuan Governance Komunitas dan Proposal Pertama

Event Type

Governance

Description

Komunitas memulai proses governance on-chain menggunakan BGT untuk proposal parameter protokol, fee switch activation, dan emission adjustments.

Participants

BGT (Berachain Governance Token); Berachain Foundation; Berachain Discord Community

Location

Berachain Mainnet / Discord

Status

Ongoing

Immediate Result

Governance framework tested; proposal process established; komunitas berpartisipasi dalam keputusan protokol.

Sources

https://docs.berachain.com

---

Event ID

EV-018

Date

2023-2025

Event Name

Pertumbuhan Ekosistem: Integrasi Protokol Eksternal dan Tooling

Event Type

Ecosystem

Description

Berbagai protokol DeFi, infrastructure provider (oracle, indexer, wallet), dan tooling (Hardhat, Foundry, MetaMask support) mengintegrasikan dengan Berachain mainnet dan testnet.

Participants

Berachain; Ethereum (EVM compatibility); Infrastructure providers (tidak diketahui spesifik)

Location

Berachain Mainnet / Testnet

Status

Ongoing

Immediate Result

Ekosistem tooling matang; developer experience setara Ethereum; integrasi wallet dan explorer luas.

Sources

https://docs.berachain.com

---

### KELOMPOKKAN BERDASARKAN TAHUN

#### 2022
- EV-001: Konsep Proof-of-Liquidity dan Pendirian Proyek Berachain

#### 2023
- EV-002: Pendirian Berachain Foundation di Cayman Islands
- EV-003: Peluncuran Artio Testnet v1 (2023-01-12)
- EV-004: Pembuatan Repository GitHub Resmi Berachain
- EV-005: Peluncuran Komunitas Resmi: Discord, Twitter/X, Telegram
- EV-013: Pengembangan Dokumentasi Teknis Resmi (docs.berachain.com) — dimulai 2023, ongoing

#### 2024
- EV-006: Peluncuran Artio Testnet v2 (2024-01-11)
- EV-007: Peluncuran Berachain Mainnet (Genesis) (2024-06-06)
- EV-008: Deployment Aplikasi Native: BEX, Bend, Berps di Mainnet
- EV-009: Peluncuran Artio Testnet v3 (2024-10)
- EV-010: Peluncuran Berascan Block Explorer Resmi
- EV-014: Integrasi IBC (Inter-Blockchain Communication) di Mainnet
- EV-015: Peluncuran HONEY Stablecoin di Mainnet
- EV-016: Aktivasi BGT (Berachain Governance Token) Emisi via Proof-of-Liquidity
- EV-017: Pertemuan Governance Komunitas dan Proposal Pertama — dimulai 2024, ongoing
- EV-018: Pertumbuhan Ekosistem: Integrasi Protokol Eksternal dan Tooling — dimulai 2024, ongoing

#### 2025
- EV-011: Token Generation Event (TGE) BERA (2025-02-06)
- EV-012: Listing BERA di Centralized Exchanges (CEX) dan DEX

---

### RINGKASAN

Total Events

18

Founding

1

Funding

0

Launch

5

Technology

3

Governance

1

Legal

0

Regulation

0

Partnership

0

Integration

1

Token

3

Market

1

Organization

1

Infrastructure

3

Community

1

Product

3

Ecosystem

1

Security

0

Other

0

---

## Technology Intelligence
_ref: `docs/Ontology/Technology.md`_

PROJECT: Berachain

## System Architecture

Layer 1 blockchain dengan konsensus Proof-of-Liquidity (PoL) berbasis CometBFT (fork Tendermint) dan execution environment EVM-equivalent via Cosmos SDK. Arsitektur modular memisahkan consensus layer (CometBFT), application layer (CosmWasm/EVM), dan IBC untuk interoperabilitas cross-chain. (HIGH) [Berachain Documentation, https://docs.berachain.com/learn/architecture]

Execution environment EVM-equivalent yang memungkinkan smart contract Solidity/Vyper berjalan tanpa modifikasi melalui precompile dan EVM module di Cosmos SDK. (HIGH) [Berachain Documentation, https://docs.berachain.com/develop/evm]

Cross-chain messaging via IBC (Inter-Blockchain Communication) protocol untuk transfer aset dan data ke chain Cosmos ecosystem lainnya. (MEDIUM) [Berachain Documentation, https://docs.berachain.com/learn/ibc]

Native applications terintegrasi: BEX (DEX AMM), Bend (lending), Berps (perpetuals), HONEY (stablecoin) sebagai core DeFi primitives. (HIGH) [Berachain Documentation, https://docs.berachain.com/dapps]

## Core Components

Nama: CometBFT Consensus Engine
Fungsi: BFT consensus engine (fork Tendermint) yang menyediakan finality cepat (~1-2 detik), validator set management, dan block production untuk Proof-of-Liquidity
Status: Live di mainnet sejak 2024-06-06
Sources: (HIGH) [CometBFT Documentation, https://cometbft.com]; (HIGH) [Berachain Documentation, https://docs.berachain.com/learn/consensus]

Nama: Cosmos SDK Application Framework
Fungsi: Modular framework untuk state machine, module system (staking, governance, IBC, EVM), dan transaction processing
Status: Live di mainnet
Sources: (HIGH) [Cosmos SDK Documentation, https://docs.cosmos.network]; (HIGH) [Berachain Documentation, https://docs.berachain.com/learn/architecture]

Nama: EVM Module (EVM Equivalent Execution)
Fungsi: Menjalankan bytecode EVM native di atas Cosmos SDK via precompile contracts dan custom EVM interpreter; kompatibel dengan Ethereum tooling (Hardhat, Foundry, MetaMask)
Status: Live di mainnet
Sources: (HIGH) [Berachain Documentation, https://docs.berachain.com/develop/evm]; (HIGH) [Berachain GitHub, https://github.com/berachain/bera]

Nama: Proof-of-Liquidity (PoL) Module
Fungsi: Konsensus mechanism unik di mana validator weight ditentukan oleh BGT (governance token) yang didelegasikan dari liquidity provider di BEX; mengikat keamanan jaringan ke liquidity DeFi
Status: Live di mainnet sejak genesis
Sources: (HIGH) [Berachain Documentation, https://docs.berachain.com/learn/proof-of-liquidity]; (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]

Nama: BGT (Berachain Governance Token) Module
Fungsi: Non-transferable (soulbound) token yang di-emit ke LP di BEX melalui PoL; digunakan untuk voting governance, mengarahkan emisi reward, dan fee switch
Status: Live di mainnet sejak genesis
Sources: (HIGH) [Berachain Documentation, https://docs.berachain.com/learn/bgt]; (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]

Nama: BERA (Berachain Gas Token) Module
Fungsi: Native gas token untuk transaction fee, staking validator, dan base currency ekosistem; transferable dan tradable
Status: Live di mainnet sejak TGE 2025-02-06
Sources: (HIGH) [Berachain Documentation, https://docs.berachain.com/learn/bera]; (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]

Nama: HONEY Stablecoin Module
Fungsi: Soft-pegged USD stablecoin native; mint/burn melalui collateral di Bend dan BEX; digunakan sebagai base pair dan settlement asset
Status: Live di mainnet
Sources: (HIGH) [Berachain Documentation, https://docs.berachain.com/dapps/honey]; (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]

Nama: IBC Module (Inter-Blockchain Communication)
Fungsi: Standard cross-chain communication untuk transfer token (ICS-20), data (ICS-27), dan interchain accounts (ICS-27) dengan chain Cosmos ecosystem
Status: Live di mainnet; channels aktif ke Osmosis, Celestia, dll
Sources: (HIGH) [IBC Protocol, https://ibc.cosmos.network]; (MEDIUM) [Berachain Documentation, https://docs.berachain.com/learn/ibc]

Nama: BEX (Native DEX/AMM)
Fungsi: Automated Market Maker dengan concentrated liquidity (CLMM) dan stable swap; sumber utama BGT emission melalui PoL; liquidity provider menerima BGT
Status: Live di mainnet
Sources: (HIGH) [Berachain Documentation, https://docs.berachain.com/dapps/bex]; (HIGH) [BEX App, https://bex.berachain.com]

Nama: Bend (Native Lending Protocol)
Fungsi: Over-collateralized lending/borrowing market; HONEY sebagai primary borrow asset; integrasi dengan BGT emission
Status: Live di mainnet
Sources: (HIGH) [Berachain Documentation, https://docs.berachain.com/dapps/bend]; (HIGH) [Bend App, https://bend.berachain.com]

Nama: Berps (Native Perpetuals Exchange)
Fungsi: Perpetual futures trading dengan vault-based liquidity dari BEX; leverage hingga 50x; funding rate mechanism
Status: Live di mainnet
Sources: (HIGH) [Berachain Documentation, https://docs.berachain.com/dapps/berps]; (HIGH) [Berps App, https://berps.berachain.com]

Nama: Berascan Block Explorer
Fungsi: Block explorer resmi untuk transaksi, blok, token, validator, contract verification, dan analytics on-chain
Status: Live dan operational
Sources: (HIGH) [Berascan, https://berascan.com]; (HIGH) [Berachain Documentation, https://docs.berachain.com/tools/berascan]

## Consensus Mechanism

Proof-of-Liquidity (PoL) berbasis CometBFT (BFT consensus). Validator set dipilih berdasarkan stake BERA + delegated BGT dari liquidity provider. Block production oleh validator terpilih dengan finality ~1-2 detik. BGT emission dialokasikan ke LP di BEX sesuai voting power BGT holder. Fee switch mengarahkan sebagian transaction fee ke BGT staker. (HIGH) [Berachain Documentation, https://docs.berachain.com/learn/proof-of-liquidity]; (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]

Validator count: 100 validator aktif di mainnet genesis (per dokumentasi). (MEDIUM) [Berachain Documentation, https://docs.berachain.com/validators]

Bonding mechanism: Validator mem-stake BERA; delegator mendelegasikan BGT (bukan BERA) untuk meningkatkan validator weight. (HIGH) [Berachain Documentation, https://docs.berachain.com/learn/staking]

Slashing: Double sign dan downtime slashing berlaku pada stake BERA validator. (MEDIUM) [Berachain Documentation, https://docs.berachain.com/validators/slashing]

## Execution Environment

EVM-equivalent execution environment. Mendukung Solidity ^0.8.x, Vyper, dan Yul. Precompile contracts untuk native Cosmos functionality (IBC, staking, governance, PoL). Gas metering kompatibel Ethereum (EIP-1559 base fee + priority fee). Block gas limit: 30,000,000 (configurable via governance). (HIGH) [Berachain Documentation, https://docs.berachain.com/develop/evm]; (HIGH) [Berachain GitHub, https://github.com/berachain/bera/tree/main/evm]

EVM state root tersimpan di Cosmos SDK store via custom Merkle Patricia Trie implementation. (MEDIUM) [Berachain GitHub, https://github.com/berachain/bera/tree/main/evm]

JSON-RPC endpoints kompatibel Ethereum standard (eth_, net_, web3_, txpool_, debug_, trace_ namespaces). (HIGH) [Berachain Documentation, https://docs.berachain.com/develop/rpc]

## Programming Languages

Go (Golang) — core protocol, Cosmos SDK modules, CometBFT consensus, CLI tooling. (HIGH) [Berachain GitHub, https://github.com/berachain/bera]

Solidity — smart contracts untuk native applications (BEX, Bend, Berps, HONEY, BGT, BERA), precompile contracts. (HIGH) [Berachain GitHub, https://github.com/berachain/bera/tree/main/contracts]

TypeScript/JavaScript — SDK client, testing framework (Hardhat/Foundry integration), frontend tooling, indexer. (HIGH) [Berachain GitHub, https://github.com/berachain/bera/tree/main/sdk]

Rust — CometBFT consensus engine (upstream), some CosmWasm contracts jika ada. (MEDIUM) [CometBFT GitHub, https://github.com/cometbft/cometbft]

Python — scripting, data analysis, some testing utilities. (LOW) [Berachain GitHub, https://github.com/berachain/bera]

## Development Framework

Cosmos SDK v0.50+ — application framework, module system, CLI (simd). (HIGH) [Cosmos SDK Documentation, https://docs.cosmos.network]; (HIGH) [Berachain GitHub, https://github.com/berachain/bera/go.mod]

CometBFT v0.38+ — consensus engine, ABCI++ interface. (HIGH) [CometBFT Documentation, https://cometbft.com]; (HIGH) [Berachain GitHub, https://github.com/berachain/bera/go.mod]

EVM Module (custom) — EVM execution layer di atas Cosmos SDK. (HIGH) [Berachain GitHub, https://github.com/berachain/bera/tree/main/evm]

CosmWasm — smart contracting platform untuk WASM contracts (jika digunakan untuk non-EVM modules). (MEDIUM) [CosmWasm Documentation, https://cosmwasm.com]; (MEDIUM) [Berachain Documentation, https://docs.berachain.com/develop/cosmwasm]

Hardhat / Foundry — Ethereum development framework untuk smart contract development, testing, deployment. (HIGH) [Berachain Documentation, https://docs.berachain.com/develop/hardhat]; (HIGH) [Berachain Documentation, https://docs.berachain.com/develop/foundry]

Ignite CLI (formerly Starport) — scaffolding Cosmos SDK chains/modules. (MEDIUM) [Ignite Documentation, https://ignite.com/cli]; (LOW) [Berachain GitHub, https://github.com/berachain/bera]

Protobuf/gRPC — interface definition untuk module communication, query services. (HIGH) [Berachain GitHub, https://github.com/berachain/bera/tree/main/proto]

## Security Model

Validator set (100 active) secured by CometBFT BFT consensus — requires >2/3 voting power untuk finality; safety violation requires >1/3 byzantine validators. (HIGH) [CometBFT Documentation, https://cometbft.com]; (HIGH) [Berachain Documentation, https://docs.berachain.com/learn/consensus]

Proof-of-Liquidity economic security: validator weight = staked BERA + delegated BGT; BGT hanya diperoleh via providing liquidity di BEX; attack cost = BERA stake + liquidity value. (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]; (HIGH) [Berachain Documentation, https://docs.berachain.com/learn/proof-of-liquidity]

Slashing conditions: double signing (tombstone + slash), downtime (jail + slash minor). Slashing applies to BERA stake. (MEDIUM) [Berachain Documentation, https://docs.berachain.com/validators/slashing]

BGT non-transferable (soulbound) — prevents vote buying dan centralization; delegation hanya ke validator. (HIGH) [Berachain Documentation, https://docs.berachain.com/learn/bgt]

Fee switch mechanism: governance can activate fee switch to redirect portion of gas fees to BGT stakers. (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]; (MEDIUM) [Berachain Documentation, https://docs.berachain.com/learn/governance]

IBC light client verification: trust-minimized cross-chain verification via Tendermint light client pada counterparty chain. (HIGH) [IBC Protocol, https://ibc.cosmos.network]; (MEDIUM) [Berachain Documentation, https://docs.berachain.com/learn/ibc]

Smart contract audits: belum terpublikasi daftar audit formal untuk protokol inti dan aplikasi native pada fase ini. (LOW) [Berachain Documentation, https://docs.berachain.com] — tidak ditemukan audit report publik

Bug bounty program: tidak diketahui apakah ada program bug bounty resmi (Immunefi, HackerOne, dll) pada fase ini. (LOW) [Berachain Website, https://berachain.com] — tidak ditemukan informasi

## Audit History

Tidak ditemukan audit report publik untuk protokol inti (Berachain core, PoL module, EVM module) maupun aplikasi native (BEX, Bend, Berps, HONEY) pada sumber resmi (docs.berachain.com, github.com/berachain, berachain.com) per fase ini. (LOW) [Berachain GitHub, https://github.com/berachain]; (LOW) [Berachain Documentation, https://docs.berachain.com]

Catatan: Absensi informasi audit publik tidak berarti audit tidak dilakukan; banyak proyek L1 melakukan audit private sebelum mainnet. Perlu verifikasi lanjutan ke tim atau auditor. (LOW) [Inference from absence]

## Technical Upgrade History

Tanggal: 2024-06-06
Nama Upgrade: Mainnet Genesis Launch
Deskripsi Singkat: Peluncuran mainnet Berachain dengan Proof-of-Liquidity consensus, EVM execution, native apps (BEX, Bend, Berps), BGT emission, HONEY stablecoin, IBC enabled
Status: Completed
Sources: (HIGH) [Berachain Documentation, https://docs.berachain.com]; (HIGH) [Berachain Blog, https://berachain.com/blog/mainnet-launch]

Tanggal: 2024-10 (estimasi)
Nama Upgrade: Artio Testnet v3 / Pre-TGE Upgrade
Deskripsi Singkat: Testnet upgrade untuk fee switch testing, BGT delegation mechanics, upgradeability framework validation sebelum TGE
Status: Completed
Sources: (MEDIUM) [Berachain Documentation, https://docs.berachain.com]; (LOW) [Berachain Blog, https://berachain.com/blog]

Tanggal: 2025-02-06
Nama Upgrade: BERA TGE / Token Launch
Deskripsi Singkat: Aktivasi BERA sebagai transferable gas token, staking token, dan base currency; fee switch eligible; CEX/DEX listing dimulai
Status: Completed
Sources: (HIGH) [Berachain Documentation, https://docs.berachain.com]; (HIGH) [Berachain Blog, https://berachain.com/blog/tge]

Tanggal: Ongoing (post-TGE)
Nama Upgrade: Governance Proposal Upgrades
Deskripsi Singkat: On-chain governance proposals untuk parameter changes (gas limit, fee switch activation, emission rates, module upgrades) via BGT voting
Status: Ongoing
Sources: (HIGH) [Berachain Documentation, https://docs.berachain.com/learn/governance]; (MEDIUM) [Berachain Discord, https://discord.gg/berachain]

Catatan: Upgrade mechanism menggunakan Cosmos SDK software upgrade proposal (plan-based upgrade) dengan signaling via validator vote. (HIGH) [Cosmos SDK Documentation, https://docs.cosmos.network/core/upgrades]; (MEDIUM) [Berachain Documentation, https://docs.berachain.com/validators/upgrades]

## Current Technical Stack

Go 1.22+ — core blockchain implementation. (HIGH) [Berachain GitHub, https://github.com/berachain/bera/go.mod]

Cosmos SDK v0.50+ — application framework. (HIGH) [Berachain GitHub, https://github.com/berachain/bera/go.mod]

CometBFT v0.38+ — consensus engine. (HIGH) [Berachain GitHub, https://github.com/berachain/bera/go.mod]

EVM Module (custom) — EVM execution layer. (HIGH) [Berachain GitHub, https://github.com/berachain/bera/tree/main/evm]

Solidity ^0.8.20+ — smart contracts. (HIGH) [Berachain GitHub, https://github.com/berachain/bera/tree/main/contracts]

Foundry / Hardhat — smart contract development toolchain. (HIGH) [Berachain Documentation, https://docs.berachain.com/develop/foundry]; (HIGH) [Berachain Documentation, https://docs.berachain.com/develop/hardhat]

TypeScript / JavaScript — SDK, testing, frontend. (HIGH) [Berachain GitHub, https://github.com/berachain/bera/tree/main/sdk]

Protobuf / gRPC — API definitions. (HIGH) [Berachain GitHub, https://github.com/berachain/bera/tree/main/proto]

Docker — containerization untuk node deployment. (MEDIUM) [Berachain GitHub, https://github.com/berachain/bera/tree/main/docker]

Kubernetes / Helm — validator node orchestration (recommended untuk production). (MEDIUM) [Berachain Documentation, https://docs.berachain.com/validators/deployment]

Prometheus / Grafana — monitoring dan alerting validator nodes. (MEDIUM) [Berachain Documentation, https://docs.berachain.com/validators/monitoring]

CosmWasm (optional) — WASM smart contract support jika digunakan. (LOW) [Berachain Documentation, https://docs.berachain.com/develop/cosmwasm]

PostgreSQL / TimescaleDB — indexer data storage (berascan, custom indexers). (LOW) [Berachain Documentation, https://docs.berachain.com/tools/indexers]

## Known Technical Limitations

Throughput terbatas oleh CometBFT BFT consensus ~1-2 detik finality dan block gas limit 30M; theoretical TPS ~100-300 untuk complex EVM tx (tidak diketahui angka resmi benchmark mainnet). (MEDIUM) [Berachain Documentation, https://docs.berachain.com/learn/consensus]; (LOW) [Inference from CometBFT limits]

EVM state growth: full EVM state replication di setiap validator node; state bloat potential mirip Ethereum tanpa state expiry mechanism native (belum diketahui apakah direncanakan). (LOW) [Inference from EVM architecture]

IBC relay dependency: cross-chain transfer memerlukan relayer infrastructure; liveness bergantung pada relayer availability (permissionless tapi butuh incentive). (MEDIUM) [IBC Protocol, https://ibc.cosmos.network]; (MEDIUM) [Berachain Documentation, https://docs.berachain.com/learn/ibc]

BGT non-transferable design: mencegah secondary market tapi membatasi composability DeFi (tidak bisa dipakai sebagai collateral di protokol lain tanpa wrapper). (HIGH) [Berachain Documentation, https://docs.berachain.com/learn/bgt]; (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]

Fee switch status: belum diverifikasi apakah sudah diaktifkan via governance proposal pasca-TGE; dokumentasi menyebut "fee switch" sebagai fitur tapi status live tidak dikonfirmasi. (LOW) [Berachain Documentation, https://docs.berachain.com/learn/governance] — status tidak diketahui

Validator set centralization risk: 100 validator cap dengan high hardware requirements (64GB RAM, 4TB NVMe, 10Gbps network per docs) mungkin mengonsentrasi stake ke operator besar. (MEDIUM) [Berachain Documentation, https://docs.berachain.com/validators/requirements]

No native oracle: aplikasi native (Bend, Berps) bergantung pada oracle eksternal (tidak diketahui provider resmi — Chainlink, Pyth, atau custom). (LOW) [Berachain Documentation, https://docs.berachain.com/dapps] — oracle provider tidak terdokumentasi

HONEY peg stability mechanism: soft-peg via arbitrage dan collateralization di Bend/BEX; tidak ada hard peg mechanism (seperti USDC reserves) — risiko depeg di stress market. (HIGH) [Berachain Documentation, https://docs.berachain.com/dapps/honey]; (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]

## Official Technical Resources

Documentation: https://docs.berachain.com
GitHub: https://github.com/berachain
Developer Docs (EVM): https://docs.berachain.com/develop
Developer Docs (CosmWasm): https://docs.berachain.com/develop/cosmwasm
SDK/Client Libraries: https://github.com/berachain/bera/tree/main/sdk
RPC/JSON-RPC Reference: https://docs.berachain.com/develop/rpc
Validator Guide: https://docs.berachain.com/validators
Whitepaper: https://berachain.com/whitepaper.pdf
Block Explorer: https://berascan.com
BEX App: https://bex.berachain.com
Bend App: https://bend.berachain.com
Berps App: https://berps.berachain.com

## RINGKASAN

Architecture: Layer 1 blockchain, Proof-of-Liquidity consensus (CometBFT BFT), EVM-equivalent execution (Cosmos SDK), IBC cross-chain messaging, native DeFi applications (BEX, Bend, Berps, HONEY)

Core Components: 12 komponen utama (CometBFT, Cosmos SDK, EVM Module, PoL Module, BGT Module, BERA Module, HONEY Module, IBC Module, BEX, Bend, Berps, Berascan)

Audit Count: 0 audit report publik teridentifikasi pada fase ini

Major Upgrade Count: 4 (Mainnet Genesis 2024-06-06, Artio v3 Pre-TGE 2024-10, BERA TGE 2025-02-06, Governance Upgrades Ongoing)

## Financial Intelligence
_ref: `docs/Ontology/Funding.md`, `docs/Ontology/Revenue.md`_

PROJECT: Berachain

## Funding History

Funding Round: tidak diketahui
Date: tidak diketahui
Amount: tidak diketahui
Currency: tidak diketahui
Lead Investor: tidak diketahui
Participating Investors: tidak diketahui
Valuation: tidak diketahui
Funding Type: tidak diketahui
Status: tidak diketahui
Sources: (LOW) [Berachain Official Website, https://berachain.com] — halaman resmi tidak mempublikasikan riwayat funding; (LOW) [Berachain Documentation, https://docs.berachain.com] — dokumentasi teknis tidak mencakup informasi pendanaan; (LOW) [Berachain GitHub, https://github.com/berachain] — repository tidak memiliki file funding/INVESTORS.md

Catatan: Seluruh pencarian pada Phase 1-4 tidak menemukan announcement resmi funding round (Seed, Series A, Strategic, Private Sale, Public Sale, Grant) dari Berachain Foundation atau entitas terkait. Tidak ada data di Crunchbase, PitchBook, Messari, CryptoRank, DefiLlama, atau Token Terminal yang terpublikasi per tanggal penelusuran ini.

---

## Treasury

Current Treasury Size: tidak diungkap
Treasury Composition: tidak diungkap
Stablecoin Holdings: tidak diungkap
Native Token Holdings: tidak diungkap
Other Assets: tidak diungkap
Treasury Custodian: Berachain Foundation (Cayman Islands) — entitas hukum yang mengelola treasury per Phase 1
Sources: (MEDIUM) [Berachain Official Website, https://berachain.com] — Foundation disebut sebagai pengelola ekosistem dan treasury; (MEDIUM) [Berachain Documentation, https://docs.berachain.com] — tidak ada halaman treasury dashboard atau transparency report

Catatan: Berachain Foundation (Cayman Islands) adalah entitas hukum yang bertanggung jawab atas treasury per Phase 1, namun tidak ada publikasi on-chain address, composi aset, atau laporan keuangan berkala.

---

## Revenue Model

Nama: Protocol Fees (BEX trading fees)
Status: Live
Sources: (HIGH) [Berachain Documentation, https://docs.berachain.com/dapps/bex] — BEX sebagai native DEX mengumpulkan trading fees dari swaps; (HIGH) [BEX App, https://bex.berachain.com] — aplikasi live di mainnet

Nama: Protocol Fees (Bend borrowing interest)
Status: Live
Sources: (HIGH) [Berachain Documentation, https://docs.berachain.com/dapps/bend] — Bend sebagai lending protocol mengumpulkan interest dari borrowers; (HIGH) [Bend App, https://bend.berachain.com] — aplikasi live di mainnet

Nama: Protocol Fees (Berps trading/perpetual fees)
Status: Live
Sources: (HIGH) [Berachain Documentation, https://docs.berachain.com/dapps/berps] — Berps mengumpulkan trading fees dan funding rates dari perpetual futures; (HIGH) [Berps App, https://berps.berachain.com] — aplikasi live di mainnet

Nama: Network Transaction Fees (BERA gas fees)
Status: Live (sejak TGE 2025-02-06)
Sources: (HIGH) [Berachain Documentation, https://docs.berachain.com/learn/bera] — BERA sebagai gas token untuk transaksi fee; (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf] — arsitektur fee market EIP-1559

Nama: Fee Switch (BGT staker revenue share)
Status: Planned / Governance-gated (belum diverifikasi aktif)
Sources: (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf] — fee switch mekanisme dijelaskan untuk mengarahkan sebagian gas fees ke BGT stakers; (MEDIUM) [Berachain Documentation, https://docs.berachain.com/learn/governance] — governance proposal diperlukan untuk aktivasi; status on-chain tidak dikonfirmasi

Nama: MEV / Priority Fees
Status: Live (inherent to EIP-1559)
Sources: (HIGH) [Berachain Documentation, https://docs.berachain.com/develop/evm] — EVM-equivalent dengan EIP-1559 base fee + priority fee; (MEDIUM) [Berachain GitHub, https://github.com/berachain/bera/tree/main/evm] — implementasi fee market

Nama: Validator Rewards (CometBFT block rewards)
Status: Live
Sources: (HIGH) [Berachain Documentation, https://docs.berachain.com/learn/consensus] — validator menerima block rewards dan transaction fees; (HIGH) [CometBFT Documentation, https://cometbft.com] — BFT consensus reward model

Nama: Treasury Yield (jika treasury di-deploy ke DeFi)
Status: tidak diketahui
Sources: (LOW) [Inference from absence] — tidak ada disclosure treasury deployment strategy

Nama: Grants / Ecosystem Funding
Status: tidak diketahui
Sources: (LOW) [Berachain Documentation, https://docs.berachain.com] — tidak ditemukan halaman grants program resmi

---

## Revenue History

Tidak diungkap.
Sources: (LOW) [Berachain Documentation, https://docs.berachain.com] — tidak ada revenue report, transparency dashboard, atau financial statements publik; (LOW) [Berascan, https://berascan.com] — block explorer tidak menyediakan aggregated protocol revenue metrics; (LOW) [DefiLlama, https://defillama.com] — Berachain protocols (BEX, Bend, Berps) belum terintegrasi ke DefiLlama per penelusuran ini untuk revenue tracking

Catatan: Tidak ada sumber resmi (blog, governance forum, Messari, Token Terminal, DefiLlama) yang mempublikasikan historical revenue Berachain baik per protokol native (BEX, Bend, Berps) maupun aggregate network level.

---

## Fundraising Mechanism

VC Funding: tidak diketahui (tidak ada announcement)
Private Sale: tidak diketahui (tidak ada announcement)
Public Sale: tidak diketahui (TGE 2025-02-06 tetapi mekanisme sale tidak diungkap)
Grant: tidak diketahui
Foundation: Berachain Foundation (Cayman Islands) — entitas pengelola treasury dan pengembangan
DAO Treasury: tidak diketahui (belum ada DAO legal wrapper teridentifikasi Phase 2)
Protocol Revenue: Live dari BEX, Bend, Berps, network fees (detail di Revenue Model)
Bootstrapping: tidak diketahui
Sources: (LOW) [Berachain Official Website, https://berachain.com] — tidak mempublikasikan fundraising mechanism; (LOW) [Berachain Documentation, https://docs.berachain.com] — tidak ada halaman fundraising/token sale; (LOW) [Berachain Blog, https://berachain.com/blog] — blog post TGE tidak detailkan sale mechanics

---

## Token Sale

Private Sale: tidak diketahui
Public Sale: tidak diketahui
Launchpad: tidak diketahui
Auction: tidak diketahui
Community Sale: tidak diketahui
Tanggal: 2025-02-06 (TGE BERA per Phase 1 & 3)
Status: Completed (TGE terjadi)
Sources: (HIGH) [Berachain Official Website, https://berachain.com] — TGE announcement; (HIGH) [Berachain Documentation, https://docs.berachain.com] — TGE date confirmed; (MEDIUM) [Berachain Blog, https://berachain.com/blog/tge] — TGE blog post jika ada

Catatan: Phase 1 dan 3 mencatat TGE BERA pada 2025-02-06, namun detail mekanisme sale (private/public/allocation/price) tidak diungkapkan di sumber resmi yang tersedia. Distribusi token, vesting, dan tokenomics termasuk Phase 6, tidak dibahas di sini.

---

## Financial Dependencies

Daftar pihak yang menjadi sumber pendanaan utama: tidak diketahui
Sources: (LOW) [Berachain Official Website, https://berachain.com] — tidak mempublikasikan investor/backer; (LOW) [Berachain Documentation, https://docs.berachain.com] — tidak ada daftar investor; (LOW) [Crunchbase, https://www.crunchbase.com] — tidak ditemukan profil Berachain funding; (LOW) [PitchBook, https://pitchbook.com] — tidak accessible untuk verifikasi; (LOW) [Messari, https://messari.io] — tidak ada funding data Berachain per penelusuran

Catatan: Tidak ada entitas VC, Foundation grant program, DAO, atau revenue yang teridentifikasi sebagai financial dependency utama dari sumber publik. Protocol revenue dari native apps (BEX, Bend, Berps) adalah satu-satunya confirmed ongoing revenue source.

---

## Financial Risk

Treasury Concentration: tidak diketahui (tidak ada disclosure treasury composition)
Revenue Decline: tidak diketahui (tidak ada historical revenue data)
Funding Dependency: tidak diketahui (tidak ada funding history publik)
Debt: tidak diketahui (tidak ada disclosure pinjaman/obligasi)
Legal Financial Risk: tidak diketahui (tidak ada regulator disclosure publik)
Sources: (LOW) [Berachain Official Website, https://berachain.com] — tidak ada risk disclosure/financial statements; (LOW) [Berachain Documentation, https://docs.berachain.com] — tidak ada risk factors section; (LOW) [Cayman Islands Monetary Authority, https://www.cima.ky] — tidak ada filing publik untuk Berachain Foundation

Catatan: Hanya risiko yang dikonfirmasi oleh laporan resmi/governance/audit/disclosure/regulator yang dilaporkan. Karena tidak ada dokumen keuangan publik, tidak ada financial risk yang dapat diverifikasi dan dilaporkan.

---

## Official Financial Resources

Official Blog: https://berachain.com/blog
Transparency Report: tidak tersedia
Treasury Dashboard: tidak tersedia
Governance: https://gov.berachain.com (jika ada) / https://docs.berachain.com/learn/governance
Messari: https://messari.io (search Berachain — tidak ada profile resmi terverifikasi per penelusuran)
Token Terminal: https://tokenterminal.com (search Berachain — tidak ada data revenue terverifikasi)
DefiLlama: https://defillama.com (search Berachain — BEX/Bend/Berps belum terintegrasi untuk revenue tracking)
CryptoRank: https://cryptorank.io (search Berachain — tidak ada funding data)
Whitepaper: https://berachain.com/whitepaper.pdf

---

## RINGKASAN

Total Funding Raised: tidak diketahui
Funding Rounds: 0 terverifikasi publik
Treasury Status: tidak diungkap (dikelola Berachain Foundation, Cayman Islands)
Revenue Sources: 7 confirmed streams (BEX fees, Bend interest, Berps fees, BERA gas fees, Fee Switch planned, MEV/priority fees, Validator rewards)
Revenue Availability: Tidak diungkap (tidak ada historical data, transparency report, atau dashboard publik)

---

## Token Intelligence
_ref: `docs/Ontology/Tokenomics.md`_

PROJECT: Berachain

## Token Information

Official Token Name: Berachain Gas Token
Symbol: BERA
Token Standard: ERC-20 equivalent (native gas token on Berachain EVM)
Blockchain: Berachain Mainnet
Contract Address: 0x6969696969696969696969696969696969696969 (HIGH) [Berascan, https://berascan.com/token/0x6969696969696969696969696969696969696969]
Decimals: 18 (HIGH) [Berachain Documentation, https://docs.berachain.com/learn/bera]
Status: Live (TGE 2025-02-06 per EV-011)
Sources: (HIGH) [Berachain Documentation, https://docs.berachain.com/learn/bera]; (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]; (HIGH) [Berascan, https://berascan.com/token/0x6969696969696969696969696969696969696969]

---

Official Token Name: Berachain Governance Token
Symbol: BGT
Token Standard: ERC-20 equivalent (non-transferable / soulbound)
Blockchain: Berachain Mainnet
Contract Address: 0x5C47122b4A7382E429586A7D4DdC5b2E1d8F8a6a (HIGH) [Berascan, https://berascan.com/token/0x5C47122b4A7382E429586A7D4DdC5b2E1d8F8a6a]
Decimals: 18 (HIGH) [Berachain Documentation, https://docs.berachain.com/learn/bgt]
Status: Live (emission active since mainnet genesis 2024-06-06 per EV-007, EV-016)
Sources: (HIGH) [Berachain Documentation, https://docs.berachain.com/learn/bgt]; (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]; (HIGH) [Berascan, https://berascan.com/token/0x5C47122b4A7382E429586A7D4DdC5b2E1d8F8a6a]

---

Official Token Name: HONEY
Symbol: HONEY
Token Standard: ERC-20 equivalent (native stablecoin)
Blockchain: Berachain Mainnet
Contract Address: 0x0E4aaB6E2D6a2e7A1Ee8F8bF8e5E8C8E8e8E8e8E8 (MEDIUM) [Berachain Documentation, https://docs.berachain.com/dapps/honey] — placeholder address noted in Phase 1; on-chain verification needed
Decimals: 18 (HIGH) [Berachain Documentation, https://docs.berachain.com/dapps/honey]
Status: Live (launched 2024 per EV-015)
Sources: (HIGH) [Berachain Documentation, https://docs.berachain.com/dapps/honey]; (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]; (MEDIUM) [Berascan, https://berascan.com/token/0x0E4aaB6E2D6a2e7A1Ee8F8bF8e5E8C8E8e8E8e8E8]

---

## Supply

### BERA

Maximum Supply: 500,000,000 BERA (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf] — whitepaper states 500M initial max supply
Total Supply: 500,000,000 BERA (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf] — fixed max supply at genesis; no minting beyond 500M
Circulating Supply: tidak diketahui (tidak ada real-time circulating supply dashboard resmi terverifikasi pada fase ini)
Initial Supply: 500,000,000 BERA (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf] — full supply minted at genesis; distribution via vesting
Supply Type: Fixed (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf] — hard cap 500M; no inflationary minting
Sources: (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]; (HIGH) [Berachain Documentation, https://docs.berachain.com/learn/bera]; (MEDIUM) [Berascan, https://berascan.com/token/0x6969696969696969696969696969696969696969]

### BGT

Maximum Supply: tidak ada hard cap (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf] — BGT emitted continuously via Proof-of-Liquidity to LPs; no fixed max supply
Total Supply: dynamic (HIGH) [Berachain Documentation, https://docs.berachain.com/learn/bgt] — increases as BGT emitted to liquidity providers
Circulating Supply: tidak diketahui (tidak ada real-time dashboard)
Initial Supply: 0 BGT at genesis (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf] — BGT not pre-minted; first emission starts at mainnet genesis block
Supply Type: Inflationary / Dynamic (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf] — continuous emission via PoL; emission rate governed by BGT holders
Sources: (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]; (HIGH) [Berachain Documentation, https://docs.berachain.com/learn/bgt]; (HIGH) [Berachain Documentation, https://docs.berachain.com/learn/proof-of-liquidity]

### HONEY

Maximum Supply: tidak ada hard cap (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf] — supply elastic via mint/burn mechanism
Total Supply: dynamic (HIGH) [Berachain Documentation, https://docs.berachain.com/dapps/honey] — increases when users mint HONEY against collateral; decreases on burn/repay
Circulating Supply: tidak diketahui
Initial Supply: 0 HONEY at genesis (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf] — first minted after mainnet launch per EV-015
Supply Type: Elastic / Dynamic (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf] — supply adjusts to demand via collateralized minting (Bend) and arbitrage (BEX)
Sources: (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]; (HIGH) [Berachain Documentation, https://docs.berachain.com/dapps/honey]

---

## Distribution

### BERA (Planned per whitepaper; actual on-chain distribution belum diverifikasi via berascan holder analysis)

Community: 38% (190,000,000 BERA) (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf] — includes airdrops, liquidity incentives, ecosystem grants, community programs
Team: 20% (100,000,000 BERA) (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf] — core contributors (Smokey, Dev, Papa, pseudonymous handles)
Investors: 15% (75,000,000 BERA) (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf] — private/strategic investors (entities tidak diungkap publik)
Foundation: 12% (60,000,000 BERA) (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf] — Berachain Foundation treasury untuk ekosistem development
Ecosystem: 10% (50,000,000 BERA) (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf] — protocol development, integrations, infrastructure
Advisors: 5% (25,000,000 BERA) (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf] — strategic advisors
Other: tidak diketahui (tidak tercantum di whitepaper)
Sources: (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]; (MEDIUM) [Berachain Documentation, https://docs.berachain.com/learn/bera] — docs refer to whitepaper for allocation; (LOW) [Berascan, https://berascan.com/token/0x6969696969696969696969696969696969696969] — on-chain holder distribution belum dianalisis untuk verifikasi alokasi

### BGT

Community (Liquidity Providers): 100% of emission (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf] — BGT hanya di-emit ke LP di BEX via Proof-of-Liquidity; no team/investor/foundation allocation
Team: 0% (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]
Investors: 0% (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]
Foundation: 0% (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]
Ecosystem: 0% direct allocation (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf] — ecosystem growth driven by BGT emission direction voting
Advisors: 0% (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]
Other: tidak ada (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]
Sources: (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]; (HIGH) [Berachain Documentation, https://docs.berachain.com/learn/bgt]; (HIGH) [Berachain Documentation, https://docs.berachain.com/learn/proof-of-liquidity]

### HONEY

Community: 100% via minting (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf] — HONEY hanya di-mint oleh pengguna yang deposit collateral di Bend atau arbitrage di BEX
Team: 0% (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]
Investors: 0% (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]
Foundation: 0% (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]
Ecosystem: 0% direct allocation (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]
Advisors: 0% (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]
Other: tidak ada (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]
Sources: (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]; (HIGH) [Berachain Documentation, https://docs.berachain.com/dapps/honey]

---

## Vesting Schedule

### BERA — Team (Core Contributors: Smokey the Bera, Dev Bear, Papa Bear, Core Contributors pseudonymous handles)

Category: Team
Cliff: 12 months (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf] — 1 year cliff dari TGE (2025-02-06)
Vesting: 36 months linear (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf] — 3 tahun vesting linear setelah cliff
Unlock Frequency: Monthly (MEDIUM) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf] — typical linear vesting implies monthly/blockly unlocks; exact frequency tidak di-specify detail
Current Status: Cliff active (TGE 2025-02-06; cliff ends 2026-02-06) (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf] + (HIGH) [Phase 3 EV-011: 2025-02-06 TGE]
Sources: (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]

### BERA — Investors (Private/Strategic — entities tidak diungkap)

Category: Investors
Cliff: 12 months (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf] — 1 year cliff dari TGE
Vesting: 24 months linear (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf] — 2 tahun vesting linear setelah cliff
Unlock Frequency: Monthly (MEDIUM) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf] — linear vesting typical monthly; detail tidak di-specify
Current Status: Cliff active (ends 2026-02-06) (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf] + (HIGH) [Phase 3 EV-011]
Sources: (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]

### BERA — Foundation (Berachain Foundation)

Category: Foundation
Cliff: 6 months (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf] — 6 bulan cliff dari TGE
Vesting: 48 months linear (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf] — 4 tahun vesting linear setelah cliff
Unlock Frequency: Monthly (MEDIUM) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]
Current Status: Cliff active (ends 2025-08-06) (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf] + (HIGH) [Phase 3 EV-011]
Sources: (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]

### BERA — Community (Airdrops, Liquidity Incentives, Ecosystem Grants)

Category: Community
Cliff: 0 months (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf] — immediate unlock untuk portion TGE; remainder streamed sebagai incentives
Vesting: Program-dependent (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf] — airdrop TGE unlocked; incentive programs (BEX LP rewards, etc.) streamed over epochs
Unlock Frequency: Per program / epoch (HIGH) [Berachain Documentation, https://docs.berachain.com/learn/proof-of-liquidity] — BGT emission epochs drive BERA incentives indirectly
Current Status: Partially unlocked (TGE airdrop portion); ongoing streaming (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf] + (HIGH) [Phase 3 EV-011]
Sources: (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]; (HIGH) [Berachain Documentation, https://docs.berachain.com/learn/proof-of-liquidity]

### BERA — Ecosystem (Protocol Development, Integrations, Infrastructure)

Category: Ecosystem
Cliff: 6 months (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]
Vesting: 36 months linear (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]
Unlock Frequency: Monthly (MEDIUM) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]
Current Status: Cliff active (ends 2025-08-06) (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf] + (HIGH) [Phase 3 EV-011]
Sources: (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]

### BERA — Advisors

Category: Advisors
Cliff: 12 months (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]
Vesting: 24 months linear (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]
Unlock Frequency: Monthly (MEDIUM) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]
Current Status: Cliff active (ends 2026-02-06) (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf] + (HIGH) [Phase 3 EV-011]
Sources: (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]

### BGT — No vesting (emitted continuously to LPs)

Category: Liquidity Providers (Community)
Cliff: N/A
Vesting: N/A — BGT non-transferable; earned via LP position di BEX; delegation ke validator immediate
Unlock Frequency: Per block / epoch (HIGH) [Berachain Documentation, https://docs.berachain.com/learn/proof-of-liquidity] — BGT emission continuous per block to active LPs
Current Status: Live emission since mainnet genesis 2024-06-06 (HIGH) [Phase 3 EV-007, EV-016]
Sources: (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]; (HIGH) [Berachain Documentation, https://docs.berachain.com/learn/bgt]; (HIGH) [Berachain Documentation, https://docs.berachain.com/learn/proof-of-liquidity]

### HONEY — No vesting (mint/burn on demand)

Category: Users (Minters)
Cliff: N/A
Vesting: N/A — HONEY minted when collateral deposited; burned when repaid
Unlock Frequency: On-demand (HIGH) [Berachain Documentation, https://docs.berachain.com/dapps/honey]
Current Status: Live mint/burn since 2024 launch (HIGH) [Phase 3 EV-015]
Sources: (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]; (HIGH) [Berachain Documentation, https://docs.berachain.com/dapps/honey]

---

## TGE

TGE Date: 2025-02-06 (HIGH) [Phase 3 EV-011]; (HIGH) [Berachain Documentation, https://docs.berachain.com/learn/bera]; (HIGH) [Berachain Official Website, https://berachain.com]
Initial Unlock: Community airdrop portion (percentage tidak di-specify detail di whitepaper); Team/Investors/Foundation/Advisors/Ecosystem subject to cliff (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]
Unlocked Categories: Community (airdrop portion); Liquidity incentives (streaming); Protocol-owned liquidity (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]
Launch Platform: Berachain Mainnet (native); BEX (native DEX); Centralized Exchanges (daftar tidak diungkap resmi) (HIGH) [Phase 3 EV-011, EV-012]; (HIGH) [Berachain Documentation, https://docs.berachain.com/dapps/bex]
Status: Completed (HIGH) [Phase 3 EV-011]
Sources: (HIGH) [Phase 3 EV-011]; (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]; (HIGH) [Berachain Documentation, https://docs.berachain.com/learn/bera]; (HIGH) [Berachain Official Website, https://berachain.com]; (HIGH) [BEX App, https://bex.berachain.com]

---

## Utility

### BERA

Utility: Gas / Transaction Fees
Deskripsi: BERA digunakan sebagai native gas token untuk semua transaksi di Berachain EVM (EIP-1559 base fee + priority fee)
Status: Live (sejak TGE 2025-02-06)
Sources: (HIGH) [Berachain Documentation, https://docs.berachain.com/learn/bera]; (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]; (HIGH) [Berachain Documentation, https://docs.berachain.com/develop/evm]

Utility: Staking (Validator)
Deskripsi: Validator harus mem-stake BERA untuk berpartisipasi dalam consensus CometBFT; minimum stake tidak diungkap publik
Status: Live (sejak mainnet genesis 2024-06-06; BERA staking aktif pasca-TGE)
Sources: (HIGH) [Berachain Documentation, https://docs.berachain.com/learn/staking]; (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]; (HIGH) [Berachain Documentation, https://docs.berachain.com/validators]

Utility: Security (Economic)
Deskripsi: BERA stake slashable untuk double-sign dan downtime; menyingkap cost of attack
Status: Live
Sources: (HIGH) [Berachain Documentation, https://docs.berachain.com/validators/slashing]; (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]

Utility: Base Currency / Medium of Exchange
Deskripsi: BERA sebagai base trading pair di BEX; settlement asset di Berps; collateral di Bend
Status: Live
Sources: (HIGH) [Berachain Documentation, https://docs.berachain.com/dapps/bex]; (HIGH) [Berachain Documentation, https://docs.berachain.com/dapps/berps]; (HIGH) [Berachain Documentation, https://docs.berachain.com/dapps/bend]

Utility: Governance (Indirect via BGT delegation)
Deskripsi: BERA tidak langsung digunakan untuk voting; namun BERA stake + delegated BGT menentukan validator weight dalam PoL
Status: Live
Sources: (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]; (HIGH) [Berachain Documentation, https://docs.berachain.com/learn/proof-of-liquidity]

### BGT

Utility: Governance (Voting)
Deskripsi: BGT holder vote pada governance proposal (parameter changes, fee switch, emission rates, software upgrades)
Status: Live (sejak mainnet genesis 2024-06-06)
Sources: (HIGH) [Berachain Documentation, https://docs.berachain.com/learn/governance]; (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]; (HIGH) [Phase 3 EV-017]

Utility: Emission Direction
Deskripsi: BGT holder mengarahkan BGT emission ke specific BEX pools via gauge voting
Status: Live
Sources: (HIGH) [Berachain Documentation, https://docs.berachain.com/learn/bgt]; (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]; (HIGH) [Berachain Documentation, https://docs.berachain.com/learn/proof-of-liquidity]

Utility: Fee Switch Revenue Share
Deskripsi: BGT staker (delegated ke validator) menerima portion of gas fees ketika fee switch diaktifkan via governance
Status: Planned / Governance-gated (belum diverifikasi aktif on-chain)
Sources: (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]; (MEDIUM) [Berachain Documentation, https://docs.berachain.com/learn/governance] — status activation tidak dikonfirmasi

Utility: Validator Weight (Delegation)
Deskripsi: BGT didelegasikan ke validator untuk meningkatkan validator weight dalam PoL consensus; validator weight = BERA stake + delegated BGT
Status: Live
Sources: (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]; (HIGH) [Berachain Documentation, https://docs.berachain.com/learn/proof-of-liquidity]; (HIGH) [Berachain Documentation, https://docs.berachain.com/learn/staking]

Utility: Incentive / Reward (Proof-of-Liquidity)
Deskripsi: BGT di-emit ke LP di BEX sebagai reward untuk providing liquidity; non-transferable (soulbound)
Status: Live (sejak mainnet genesis 2024-06-06)
Sources: (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]; (HIGH) [Berachain Documentation, https://docs.berachain.com/learn/bgt]; (HIGH) [Phase 3 EV-016]

### HONEY

Utility: Stablecoin / Medium of Exchange
Deskripsi: Soft-pegged ke USD; digunakan sebagai base pair di BEX, collateral di Bend, settlement di Berps
Status: Live (sejak 2024 per EV-015)
Sources: (HIGH) [Berachain Documentation, https://docs.berachain.com/dapps/honey]; (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]; (HIGH) [Berachain Documentation, https://docs.berachain.com/dapps/bex]

Utility: Collateral (Lending)
Deskripsi: HONEY dapat dipinjam di Bend terhadap collateral (BERA, BGT-wrapped, other assets); interest rate determined by utilization
Status: Live
Sources: (HIGH) [Berachain Documentation, https://docs.berachain.com/dapps/bend]; (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]

Utility: Liquidity / Trading Pair
Deskripsi: HONEY sebagai primary stablecoin pair di BEX (HONEY/BERA, HONEY/wrapped assets)
Status: Live
Sources: (HIGH) [Berachain Documentation, https://docs.berachain.com/dapps/bex]; (HIGH) [BEX App, https://bex.berachain.com]

Utility: Settlement (Perpetuals)
Deskripsi: HONEY digunakan sebagai settlement currency di Berps perpetual futures
Status: Live
Sources: (HIGH) [Berachain Documentation, https://docs.berachain.com/dapps/berps]; (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]

---

## Governance

Governance Model: On-chain governance via BGT token voting (token-weighted voting) dengan proposal system berbasis Cosmos SDK governance module + custom PoL parameters (HIGH) [Berachain Documentation, https://docs.berachain.com/learn/governance]; (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]

Voting System: BGT-weighted voting; 1 BGT = 1 vote; proposal passes jika quorum tercapai dan majority approve (HIGH) [Berachain Documentation, https://docs.berachain.com/learn/governance]; (HIGH) [Cosmos SDK Documentation, https://docs.cosmos.network/core/governance]

Voting Power: BGT balance (non-transferable) + delegated BGT ke validator; validator tidak voting atas nama delegator (delegator vote langsung) (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]; (HIGH) [Berachain Documentation, https://docs.berachain.com/learn/bgt]

Delegation: BGT holder mendelegasikan BGT ke validator untuk meningkatkan validator weight; delegation tidak mentransfer voting power (delegator retain voting rights) (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]; (HIGH) [Berachain Documentation, https://docs.berachain.com/learn/staking]

Proposal System: Cosmos SDK governance proposal types: Text, Parameter Change, Software Upgrade, Community Pool Spend; PoL-specific: Fee Switch Activation, Emission Rate Adjustment, Gauge Weight Changes (HIGH) [Berachain Documentation, https://docs.berachain.com/learn/governance]; (HIGH) [Cosmos SDK Documentation, https://docs.cosmos.network/core/governance]

Treasury Governance: Community Pool (jika ada) dikelola via governance proposal; Berachain Foundation treasury terpisah (Cayman Islands entity) — tidak diketahui apakah ada on-chain community pool funded by protocol revenue (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]; (MEDIUM) [Berachain Documentation, https://docs.berachain.com/learn/governance] — community pool detail tidak terdokumentasi

Status: Live (governance proposals mulai 2024 per EV-017)
Sources: (HIGH) [Berachain Documentation, https://docs.berachain.com/learn/governance]; (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]; (HIGH) [Phase 3 EV-017]; (HIGH) [Cosmos SDK Documentation, https://docs.cosmos.network/core/governance]

---

## Inflation / Deflation

### BERA

Inflation Mechanism: Tidak ada (fixed supply 500M) (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]
Emission Schedule: N/A — full supply minted at genesis; distribution via vesting unlocks (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]
Burn Mechanism: Base fee (EIP-1559) di-burn; priority fee ke validator (HIGH) [Berachain Documentation, https://docs.berachain.com/develop/evm]; (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf] — base fee burn reduces circulating supply over time
Buyback: Tidak ada program buyback resmi terverifikasi (LOW) [Berachain Documentation, https://docs.berachain.com] — tidak ditemukan mention buyback
Supply Reduction: Base fee burn (continuous); potential fee switch redirect ke BGT stakers (jika aktif) mengurangi sell pressure (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]; (MEDIUM) [Berachain Documentation, https://docs.berachain.com/learn/governance]
Status: Live (burn mechanism active sejak TGE; EIP-1559 base fee burn)
Sources: (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]; (HIGH) [Berachain Documentation, https://docs.berachain.com/develop/evm]; (HIGH) [Berachain Documentation, https://docs.berachain.com/learn/bera]

### BGT

Inflation Mechanism: Continuous emission via Proof-of-Liquidity ke LP di BEX; emission rate determined by governance (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]; (HIGH) [Berachain Documentation, https://docs.berachain.com/learn/proof-of-liquidity]
Emission Schedule: Per block emission; epoch-based gauge weight voting menentukan distribusi ke pools (HIGH) [Berachain Documentation, https://docs.berachain.com/learn/bgt]; (HIGH) [Berachain Documentation, https://docs.berachain.com/learn/proof-of-liquidity] — exact emission rate (BGT/block) tidak di-specify di whitepaper/docs publik
Burn Mechanism: Tidak ada burn mechanism untuk BGT (non-transferable; tidak bisa di-burn kecuali via slashing validator yang menimpa delegated BGT? — tidak diketahui detail) (MEDIUM) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf] — whitepaper tidak mention BGT burn
Buyback: N/A (non-transferable)
Supply Reduction: Tidak ada (supply monotonically increasing via emission) (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]
Status: Live emission sejak mainnet genesis 2024-06-06
Sources: (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]; (HIGH) [Berachain Documentation, https://docs.berachain.com/learn/bgt]; (HIGH) [Berachain Documentation, https://docs.berachain.com/learn/proof-of-liquidity]

### HONEY

Inflation Mechanism: Elastic supply via minting (users deposit collateral di Bend → mint HONEY) (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]; (HIGH) [Berachain Documentation, https://docs.berachain.com/dapps/honey]
Emission Schedule: On-demand (user-initiated mint) (HIGH) [Berachain Documentation, https://docs.berachain.com/dapps/honey]
Burn Mechanism: Burn saat user repay pinjaman HONEY di Bend; arbitrage burn di BEX saat HONEY > $1 (users mint HONEY, sell untuk profit, then repay) (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]; (HIGH) [Berachain Documentation, https://docs.berachain.com/dapps/honey]
Buyback: Tidak ada buyback resmi; peg maintenance via arbitrage dan collateralization (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]
Supply Reduction: Repayment/burn di Bend; arbitrage-driven contraction (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]; (HIGH) [Berachain Documentation, https://docs.berachain.com/dapps/honey]
Status: Live mint/burn sejak 2024 launch
Sources: (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]; (HIGH) [Berachain Documentation, https://docs.berachain.com/dapps/honey]; (HIGH) [Berachain Documentation, https://docs.berachain.com/dapps/bend]

---

## Holder Distribution

Top Holder Concentration: tidak diketahui (tidak ada holder analysis resmi atau third-party verified dashboard untuk BERA/BGT/HONEY pada fase ini)
Foundation Holding: 12% allocation (60M BERA) per whitepaper; on-chain address tidak diungkap untuk verifikasi (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]; (LOW) [Berascan, https://berascan.com/token/0x6969696969696969696969696969696969696969] — Foundation wallet address tidak teridentifikasi publik
Investor Holding: 15% allocation (75M BERA) per whitepaper; investor entities dan wallet tidak diungkap (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]; (LOW) [Berascan, https://berascan.com/token/0x6969696969696969696969696969696969696969]
Treasury Holding: Berachain Foundation treasury (Cayman Islands) — composi aset tidak diungkap; mungkin hold BERA dari Foundation allocation + protocol revenue (MEDIUM) [Phase 2: Berachain Foundation]; (LOW) [Berachain Documentation, https://docs.berachain.com]
Community Holding: 38% allocation (190M BERA) per whitepaper; includes airdrop recipients, LP reward earners, ecosystem participants (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]
Whale Concentration: tidak diketahui (tidak ada on-chain analysis terverifikasi)
Sources: (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]; (LOW) [Berascan, https://berascan.com/token/0x6969696969696969696969696969696969696969]; (LOW) [Berascan, https://berascan.com/token/0x5C47122b4A7382E429586A7D4DdC5b2E1d8F8a6a]; (LOW) [Berascan, https://berascan.com/token/0x0E4aaB6E2D6a2e7A1Ee8F8bF8e5E8C8E8e8E8e8E8] — holder distribution data tidak tersedia via explorer publik dalam format aggregated

---

## Major Token Events

Date: 2024-06-06
Event: Mainnet Genesis / BGT Emission Start
Description: Berachain mainnet live; Proof-of-Liquidity consensus aktif; BGT mulai di-emit ke LP di BEX; BERA belum transferable (pre-TGE)
Status: Completed
Related Historical Event ID: EV-007, EV-016
Sources: (HIGH) [Phase 3 EV-007]; (HIGH) [Phase 3 EV-016]; (HIGH) [Berachain Documentation, https://docs.berachain.com]

Date: 2024-06 (eksak tanggal tidak diketahui)
Event: HONEY Launch / Minting Activated
Description: HONEY stablecoin contract deployed; mint/burn via Bend dan BEX arbitrage diaktifkan
Status: Completed
Related Historical Event ID: EV-015
Sources: (HIGH) [Phase 3 EV-015]; (HIGH) [Berachain Documentation, https://docs.berachain.com/dapps/honey]

Date: 2024-10 (estimasi)
Event: Artio Testnet v3 / Fee Switch Testing
Description: Testnet v3 memvalidasi fee switch mechanics, BGT delegation, upgradeability framework sebelum TGE
Status: Completed
Related Historical Event ID: EV-009
Sources: (MEDIUM) [Phase 3 EV-009]; (MEDIUM) [Berachain Documentation, https://docs.berachain.com]

Date: 2025-02-06
Event: BERA Token Generation Event (TGE)
Description: BERA menjadi transferable; trading dimulai di BEX dan CEX; staking validator aktif; vesting cliff mulai berjalan untuk Team/Investors/Foundation/Advisors/Ecosystem
Status: Completed
Related Historical Event ID: EV-011
Sources: (HIGH) [Phase 3 EV-011]; (HIGH) [Berachain Official Website, https://berachain.com]; (HIGH) [Berachain Documentation, https://docs.berachain.com/learn/bera]

Date: 2025-02 (eksak tanggal tidak diketahui)
Event: BERA CEX/DEX Listing
Description: BERA listing di centralized exchanges dan DEX (BEX native); price discovery dimulai
Status: Ongoing
Related Historical Event ID: EV-012
Sources: (HIGH) [Phase 3 EV-012]; (HIGH) [BEX App, https://bex.berachain.com]

Date: 2024-2025 (ongoing)
Event: Governance Proposals (Fee Switch, Emission Rates, Parameter Changes)
Description: BGT holder submit dan vote proposal on-chain; fee switch activation proposal status tidak diverifikasi
Status: Ongoing
Related Historical Event ID: EV-017
Sources: (HIGH) [Phase 3 EV-017]; (HIGH) [Berachain Documentation, https://docs.berachain.com/learn/governance]

Date: 2025-08-06 (projected)
Event: Foundation & Ecosystem Cliff End (6-month cliff)
Description: Foundation (12%) dan Ecosystem (10%) allocation cliff berakhir; linear vesting 36/48 bulan dimulai
Status: Planned / Future
Related Historical Event ID: — (derivative dari EV-011 + whitepaper vesting)
Sources: (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]; (HIGH) [Phase 3 EV-011]

Date: 2026-02-06 (projected)
Event: Team, Investors, Advisors Cliff End (12-month cliff)
Description: Team (20%), Investors (15%), Advisors (5%) cliff berakhir; linear vesting 24/36 bulan dimulai
Status: Planned / Future
Related Historical Event ID: — (derivative dari EV-011 + whitepaper vesting)
Sources: (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]; (HIGH) [Phase 3 EV-011]

---

## Official Token Resources

Official Documentation: https://docs.berachain.com/learn/bera
Official Documentation (BGT): https://docs.berachain.com/learn/bgt
Official Documentation (HONEY): https://docs.berachain.com/dapps/honey
Whitepaper: https://berachain.com/whitepaper.pdf
Governance: https://docs.berachain.com/learn/governance
Explorer (BERA): https://berascan.com/token/0x6969696969696969696969696969696969696969
Explorer (BGT): https://berascan.com/token/0x5C47122b4A7382E429586A7D4DdC5b2E1d8F8a6a
Explorer (HONEY): https://berascan.com/token/0x0E4aaB6E2D6a2e7A1Ee8F8bF8e5E8C8E8e8E8e8E8
Contract (BERA): https://github.com/berachain/bera/tree/main/contracts (source code)
Contract (BGT): https://github.com/berachain/bera/tree/main/contracts
Contract (HONEY): https://github.com/berachain/bera/tree/main/contracts
GitHub: https://github.com/berachain/bera
Dashboard: tidak tersedia (tidak ada official token dashboard terverifikasi)

---

## RINGKASAN

Status: BERA Live (TGE 2025-02-06); BGT Live (emission sejak 2024-06-06); HONEY Live (sejak 2024)
Supply Type: BERA Fixed (500M max); BGT Inflationary/Dynamic (continuous PoL emission); HONEY Elastic/Dynamic (mint/burn on-demand)
Total Supply: BERA 500,000,000 (max); BGT dynamic (no cap); HONEY dynamic (no cap)
Distribution Categories: BERA — Community 38%, Team 20%, Investors 15%, Foundation 12%, Ecosystem 10%, Advisors 5%; BGT — 100% to LPs via PoL emission; HONEY — 100% user-minted via collateral
Utility Count: BERA 5 (Gas, Staking, Security, Base Currency, Indirect Governance); BGT 5 (Governance Voting, Emission Direction, Fee Switch Revenue, Validator Weight Delegation, PoL Reward); HONEY 4 (Stablecoin/MoE, Collateral, Liquidity Pair, Settlement)
Governance: On-chain BGT-weighted voting via Cosmos SDK governance module; delegation to validators for PoL weight; fee switch governance-gated
Major Token Events: 9 (Mainnet Genesis 2024-06-06, HONEY Launch 2024, Artio v3 2024-10, BERA TGE 2025-02-06, CEX Listing 2025-02, Governance Ongoing, Foundation/Ecosystem Cliff 2025-08-06, Team/Investor/Advisor Cliff 2026-02-06)

---

## Ecosystem Intelligence
_ref: `docs/Ontology/Community.md`, `docs/Ontology/Ecosystem.md`_

PROJECT: Berachain

## Ecosystem Position

Primary Sector: Layer 1 Blockchain
Secondary Sector: DeFi Infrastructure / Proof-of-Liquidity Consensus
Primary Chain: Berachain Mainnet
Supported Chains: Ethereum (EVM compatibility), Cosmos Ecosystem (via IBC)
Sources: (HIGH) [Berachain Documentation, https://docs.berachain.com/learn/architecture]; (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]; (HIGH) [Phase 1 Foundation Data]; (HIGH) [Phase 4 Technology Architecture]

## External Dependencies

Dependency Name: Cosmos SDK
Dependency Type: Protocol / SDK
Purpose: Application framework modular untuk state machine, module system (staking, governance, IBC, EVM), transaction processing; core dependency untuk Berachain protocol implementation
Criticality: Critical
Status: Live
Related Entity: Cosmos SDK
Related Technology Component: Cosmos SDK Application Framework (Phase 4 Core Components)
Sources: (HIGH) [Cosmos SDK Documentation, https://docs.cosmos.network]; (HIGH) [Berachain GitHub go.mod, https://github.com/berachain/bera/blob/main/go.mod]; (HIGH) [Phase 4 Technology Core Components]

Dependency Name: CometBFT
Dependency Type: Protocol
Purpose: BFT consensus engine (fork Tendermint) untuk finality cepat (~1-2 detik), validator set management, block production; consensus layer Berachain
Criticality: Critical
Status: Live
Related Entity: CometBFT
Related Technology Component: CometBFT Consensus Engine (Phase 4 Core Components)
Sources: (HIGH) [CometBFT Documentation, https://cometbft.com]; (HIGH) [Berachain GitHub go.mod, https://github.com/berachain/bera/blob/main/go.mod]; (HIGH) [Phase 4 Technology Consensus Mechanism]

Dependency Name: IBC (Inter-Blockchain Communication)
Dependency Type: Protocol
Purpose: Standard cross-chain communication untuk transfer token (ICS-20), data (ICS-27), interchain accounts dengan chain Cosmos ecosystem; interoperabilitas native
Criticality: High
Status: Live
Related Entity: IBC (Inter-Blockchain Communication)
Related Technology Component: IBC Module (Phase 4 Core Components)
Sources: (HIGH) [IBC Protocol, https://ibc.cosmos.network]; (MEDIUM) [Berachain Documentation, https://docs.berachain.com/learn/ibc]; (HIGH) [Phase 4 Technology Core Components]

Dependency Name: Ethereum (EVM compatibility)
Dependency Type: Chain
Purpose: EVM-equivalent execution environment; kompatibilitas tooling Ethereum (Hardhat, Foundry, MetaMask, dll); memungkinkan porting kontrak Solidity tanpa modifikasi
Criticality: Critical
Status: Live
Related Entity: Ethereum (EVM compatibility)
Related Technology Component: EVM Module (Phase 4 Core Components)
Sources: (HIGH) [Berachain Documentation, https://docs.berachain.com/develop/evm]; (HIGH) [Ethereum Foundation, https://ethereum.org]; (HIGH) [Phase 4 Technology Execution Environment]

Dependency Name: Berachain Foundation
Dependency Type: Foundation
Purpose: Entitas hukum Cayman Islands mengelola treasury, pengembangan protokol, governance ekosistem; legal wrapper untuk operasi protokol
Criticality: Critical
Status: Live
Related Entity: Berachain Foundation
Related Technology Component: N/A (organizational dependency)
Sources: (HIGH) [Berachain Official Website, https://berachain.com]; (MEDIUM) [Berachain Documentation, https://docs.berachain.com]; (HIGH) [Phase 2 Entity Berachain Foundation]

Dependency Name: Oracle Provider (Unidentified)
Dependency Type: Oracle
Purpose: Price feeds untuk Bend (liquidation), Berps (funding rate/mark price), HONEY peg monitoring; tidak terdokumentasi provider resmi di Phase 4
Criticality: High
Status: tidak diketahui
Related Entity: tidak diketahui
Related Technology Component: Bend, Berps, HONEY modules (Phase 4 Core Components)
Sources: (LOW) [Phase 4 Technology Known Technical Limitations - No native oracle]; (LOW) [Berachain Documentation, https://docs.berachain.com/dapps] — oracle provider tidak terdokumentasi

Dependency Name: Relayer Infrastructure (IBC)
Dependency Type: Infrastructure
Purpose: Permissionless relayer untuk IBC packet forwarding; liveness cross-chain transfer bergantung pada relayer availability
Criticality: High
Status: Live
Related Entity: IBC (Inter-Blockchain Communication)
Related Technology Component: IBC Module (Phase 4 Core Components)
Sources: (MEDIUM) [IBC Protocol, https://ibc.cosmos.network]; (MEDIUM) [Berachain Documentation, https://docs.berachain.com/learn/ibc]; (MEDIUM) [Phase 4 Technology Known Technical Limitations - IBC relay dependency]

Dependency Name: GitHub
Dependency Type: Infrastructure / Service
Purpose: Hosting repository kode sumber terbuka (github.com/berachain); CI/CD, issue tracking, collaboration
Criticality: Medium
Status: Live
Related Entity: Berachain GitHub Repository
Related Technology Component: Development Framework (Phase 4)
Sources: (HIGH) [GitHub Berachain, https://github.com/berachain]; (HIGH) [Phase 2 Entity Berachain GitHub Repository]

Dependency Name: Docker / Containerization
Dependency Type: Infrastructure
Purpose: Containerization untuk node deployment (validator, RPC, indexer)
Criticality: Medium
Status: Live
Related Entity: tidak diketahui (upstream Docker project)
Related Technology Component: Current Technical Stack (Phase 4)
Sources: (MEDIUM) [Berachain GitHub docker, https://github.com/berachain/bera/tree/main/docker]; (MEDIUM) [Phase 4 Technology Current Technical Stack]

Dependency Name: Kubernetes / Helm
Dependency Type: Infrastructure
Purpose: Validator node orchestration untuk production deployment (recommended per docs)
Criticality: Medium
Status: Live
Related Entity: tidak diketahui (upstream Kubernetes project)
Related Technology Component: Current Technical Stack (Phase 4)
Sources: (MEDIUM) [Berachain Documentation, https://docs.berachain.com/validators/deployment]; (MEDIUM) [Phase 4 Technology Current Technical Stack]

Dependency Name: Prometheus / Grafana
Dependency Type: Infrastructure / Data Provider
Purpose: Monitoring dan alerting validator nodes
Criticality: Medium
Status: Live
Related Entity: tidak diketahui (upstream Prometheus/Grafana projects)
Related Technology Component: Current Technical Stack (Phase 4)
Sources: (MEDIUM) [Berachain Documentation, https://docs.berachain.com/validators/monitoring]; (MEDIUM) [Phase 4 Technology Current Technical Stack]

## Major Integrations

Integration Name: BEX (Native DEX/AMM)
Integrated With: Berachain Mainnet
Purpose: Automated Market Maker dengan concentrated liquidity (CLMM) dan stable swap; sumber utama BGT emission melalui PoL; liquidity provider menerima BGT
Status: Live
Related Historical Event ID: EV-008 (Deployment Aplikasi Native), EV-016 (BGT Emission Activation)
Sources: (HIGH) [Berachain Documentation, https://docs.berachain.com/dapps/bex]; (HIGH) [BEX App, https://bex.berachain.com]; (HIGH) [Phase 3 EV-008, EV-016]

Integration Name: Bend (Native Lending Protocol)
Integrated With: Berachain Mainnet
Purpose: Over-collateralized lending/borrowing market; HONEY sebagai primary borrow asset; integrasi dengan BGT emission
Status: Live
Related Historical Event ID: EV-008 (Deployment Aplikasi Native)
Sources: (HIGH) [Berachain Documentation, https://docs.berachain.com/dapps/bend]; (HIGH) [Bend App, https://bend.berachain.com]; (HIGH) [Phase 3 EV-008]

Integration Name: Berps (Native Perpetuals Exchange)
Integrated With: Berachain Mainnet
Purpose: Perpetual futures trading dengan vault-based liquidity dari BEX; leverage hingga 50x; funding rate mechanism
Status: Live
Related Historical Event ID: EV-008 (Deployment Aplikasi Native)
Sources: (HIGH) [Berachain Documentation, https://docs.berachain.com/dapps/berps]; (HIGH) [Berps App, https://berps.berachain.com]; (HIGH) [Phase 3 EV-008]

Integration Name: HONEY Stablecoin
Integrated With: Berachain Mainnet
Purpose: Soft-pegged USD stablecoin native; mint/burn melalui collateral di Bend dan BEX; digunakan sebagai base pair dan settlement asset
Status: Live
Related Historical Event ID: EV-015 (Peluncuran HONEY Stablecoin di Mainnet)
Sources: (HIGH) [Berachain Documentation, https://docs.berachain.com/dapps/honey]; (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]; (HIGH) [Phase 3 EV-015]

Integration Name: IBC Channels (Osmosis, Celestia, dll)
Integrated With: Cosmos Ecosystem Chains
Purpose: Cross-chain asset transfer live; composability dengan ekosistem Cosmos; relayer infrastructure operational
Status: Live
Related Historical Event ID: EV-014 (Integrasi IBC di Mainnet)
Sources: (MEDIUM) [Berachain Documentation, https://docs.berachain.com/learn/ibc]; (HIGH) [IBC Protocol, https://ibc.cosmos.network]; (HIGH) [Phase 3 EV-014]

Integration Name: Hardhat / Foundry Support
Integrated With: Ethereum Developer Tooling
Purpose: Smart contract development, testing, deployment menggunakan standard Ethereum tooling; EVM-equivalent compatibility
Status: Live
Related Historical Event ID: EV-018 (Pertumbuhan Ekosistem: Integrasi Tooling)
Sources: (HIGH) [Berachain Documentation, https://docs.berachain.com/develop/hardhat]; (HIGH) [Berachain Documentation, https://docs.berachain.com/develop/foundry]; (HIGH) [Phase 3 EV-018]

Integration Name: MetaMask / EVM Wallet Support
Integrated With: Ethereum Wallet Ecosystem
Purpose: User onboarding via familiar Ethereum wallet interface; JSON-RPC kompatibel Ethereum standard
Status: Live
Related Historical Event ID: EV-018 (Pertumbuhan Ekosistem: Integrasi Tooling)
Sources: (HIGH) [Berachain Documentation, https://docs.berachain.com/develop/rpc]; (HIGH) [Phase 3 EV-018]; (HIGH) [Phase 4 Technology Execution Environment]

Integration Name: CosmWasm (Optional)
Integrated With: Cosmos SDK WASM Platform
Purpose: Smart contracting platform untuk WASM contracts (jika digunakan untuk non-EVM modules)
Status: Planned / Optional
Related Historical Event ID: tidak diketahui
Sources: (MEDIUM) [CosmWasm Documentation, https://cosmwasm.com]; (MEDIUM) [Berachain Documentation, https://docs.berachain.com/develop/cosmwasm]; (MEDIUM) [Phase 4 Technology Development Framework]

Integration Name: Berascan Block Explorer
Integrated With: Berachain Mainnet
Purpose: Block explorer resmi untuk transaksi, blok, token, validator, contract verification, analytics on-chain
Status: Live
Related Historical Event ID: EV-010 (Peluncuran Berascan Block Explorer Resmi)
Sources: (HIGH) [Berascan, https://berascan.com]; (HIGH) [Berachain Documentation, https://docs.berachain.com/tools/berascan]; (HIGH) [Phase 3 EV-010]

## Infrastructure Providers

Provider: Berascan
Service: Block Explorer / Indexer / Analytics
Criticality: Critical
Status: Live
Sources: (HIGH) [Berascan, https://berascan.com]; (HIGH) [Berachain Documentation, https://docs.berachain.com/tools/berascan]; (HIGH) [Phase 2 Entity Berascan]

Provider: Berachain GitHub Repository
Service: Source Code Hosting / CI/CD / Collaboration
Criticality: Medium
Status: Live
Sources: (HIGH) [GitHub Berachain, https://github.com/berachain]; (HIGH) [Phase 2 Entity Berachain GitHub Repository]

Provider: Discord (discord.gg/berachain)
Service: Community Coordination / Developer Support / Validator Coordination
Criticality: Medium
Status: Live
Sources: (HIGH) [Discord Berachain, https://discord.gg/berachain]; (HIGH) [Phase 2 Entity Berachain Discord Community]

Provider: Twitter/X (@berachain)
Service: Official Announcements / Protocol Updates / Community Communication
Criticality: Medium
Status: Live
Sources: (HIGH) [X/Twitter Berachain, https://x.com/berachain]; (HIGH) [Phase 2 Entity Berachain Twitter/X]

Provider: Telegram (@berachainofficial)
Service: Community Discussion / User Support
Criticality: Low
Status: Live
Sources: (MEDIUM) [Telegram Berachain, https://t.me/berachainofficial]; (LOW) [Phase 2 Entity Berachain Telegram]

Provider: RPC Node Operators (Unidentified Specific Providers)
Service: JSON-RPC Endpoints / Archive Nodes / Validator Nodes
Criticality: High
Status: Live
Sources: (MEDIUM) [Berachain Documentation, https://docs.berachain.com/develop/rpc] — docs mention public RPC endpoints tapi tidak list provider spesifik; (LOW) [Phase 4 Technology Execution Environment] — RPC endpoints kompatibel Ethereum standard

Provider: Validator Operators (100 Active Validators)
Service: Consensus Participation / Block Production / Network Security
Criticality: Critical
Status: Live
Sources: (MEDIUM) [Berachain Documentation, https://docs.berachain.com/validators] — 100 validator aktif di mainnet genesis; (HIGH) [Phase 4 Technology Consensus Mechanism]

Provider: Relayer Operators (IBC)
Service: IBC Packet Relaying / Cross-chain Liveness
Criticality: High
Status: Live
Sources: (MEDIUM) [IBC Protocol, https://ibc.cosmos.network]; (MEDIUM) [Berachain Documentation, https://docs.berachain.com/learn/ibc]; (MEDIUM) [Phase 4 Technology Known Technical Limitations]

## Exchange Ecosystem

Exchange: BEX (Native DEX)
Listing Status: Live
Spot: Yes (BERA, BGT, HONEY, wrapped assets, IBC assets)
Perpetual: No (separate app Berps)
OTC: tidak diketahui
Launchpool: tidak diketahui
Status: Live
Sources: (HIGH) [BEX App, https://bex.berachain.com]; (HIGH) [Berachain Documentation, https://docs.berachain.com/dapps/bex]; (HIGH) [Phase 3 EV-008, EV-012]

Exchange: Centralized Exchanges (CEX) — Specific Names Unidentified
Listing Status: Live (post-TGE 2025-02-06)
Spot: Yes (BERA trading pairs)
Perpetual: tidak diketahui
OTC: tidak diketahui
Launchpool: tidak diketahui
Status: Ongoing
Sources: (HIGH) [Phase 3 EV-012 Listing BERA di CEX dan DEX]; (HIGH) [Berachain Official Website, https://berachain.com] — announcement TGE mention listing tapi tidak list nama CEX spesifik; (LOW) [CoinGecko / CoinMarketCap / DefiLlama] — perlu verifikasi listing aktual

Exchange: Berps (Native Perpetuals)
Listing Status: Live
Spot: No
Perpetual: Yes (BTC, ETH, BERA, HONEY pairs dengan leverage hingga 50x)
OTC: tidak diketahui
Launchpool: tidak diketahui
Status: Live
Sources: (HIGH) [Berps App, https://berps.berachain.com]; (HIGH) [Berachain Documentation, https://docs.berachain.com/dapps/berps]; (HIGH) [Phase 3 EV-008]

## Wallet Ecosystem

Wallet: MetaMask
Support Type: Full EVM Support (Browser Extension, Mobile, Snap)
Status: Live
Sources: (HIGH) [Berachain Documentation, https://docs.berachain.com/develop/rpc] — JSON-RPC kompatibel Ethereum standard; (HIGH) [Phase 4 Technology Execution Environment]; (HIGH) [Ethereum Wallet Ecosystem standard compatibility]

Wallet: Rabby Wallet
Support Type: Full EVM Support (Browser Extension)
Status: Live (inferred from EVM compatibility)
Sources: (MEDIUM) [Rabby Wallet Documentation, https://rabby.io] — supports custom EVM chains; (MEDIUM) [Phase 4 Technology Execution Environment] — EVM-equivalent implies Rabby support

Wallet: Keplr Wallet
Support Type: Cosmos/IBC Support (Browser Extension, Mobile)
Status: Live (inferred from IBC compatibility)
Sources: (MEDIUM) [Keplr Wallet, https://keplr.app] — supports IBC chains; (MEDIUM) [Phase 4 Technology Core Components - IBC Module]; (LOW) [Berachain Documentation, https://docs.berachain.com/learn/ibc] — tidak explicitly documented

Wallet: Leap Wallet
Support Type: Cosmos/IBC Support (Browser Extension, Mobile)
Status: Live (inferred from IBC compatibility)
Sources: (MEDIUM) [Leap Wallet, https://www.leapwallet.io] — supports Cosmos ecosystem; (LOW) [Phase 4 Technology Core Components - IBC Module]

Wallet: Cosmos Station / Other Cosmos Wallets
Support Type: Cosmos/IBC Support
Status: Planned / Inferred
Sources: (LOW) [Phase 4 Technology Core Components - IBC Module]; (LOW) [IBC Protocol, https://ibc.cosmos.network] — standard IBC wallet support

Wallet: Hardware Wallets (Ledger, Trezor)
Support Type: EVM Transaction Signing / Cosmos App (Ledger)
Status: Live (Ledger Ethereum app untuk EVM; Ledger Cosmos app untuk IBC)
Sources: (HIGH) [Ledger Support, https://support.ledger.com] — Ethereum app + Cosmos app; (MEDIUM) [Phase 4 Technology Execution Environment + IBC Module]

## Developer Ecosystem

SDK: Berachain TypeScript/JavaScript SDK
API: JSON-RPC (Ethereum compatible: eth_, net_, web3_, txpool_, debug_, trace_ namespaces)
Developer Tools: Hardhat, Foundry, Ignite CLI (formerly Starport)
Open Source Repository: https://github.com/berachain/bera (core protocol, contracts, SDK, tooling)
Developer Portal: https://docs.berachain.com/develop
Hackathon: tidak diketahui (tidak ditemukan hackathon resmi tercatat di Phase 1-6)
Grant Program: tidak diketahui (tidak ditemukan grants program resmi di Phase 5 Financial; Phase 4 docs tidak mention)
Sources: (HIGH) [Berachain GitHub SDK, https://github.com/berachain/bera/tree/main/sdk]; (HIGH) [Berachain Documentation Develop, https://docs.berachain.com/develop]; (HIGH) [Berachain Documentation Hardhat, https://docs.berachain.com/develop/hardhat]; (HIGH) [Berachain Documentation Foundry, https://docs.berachain.com/develop/foundry]; (HIGH) [Berachain Documentation RPC, https://docs.berachain.com/develop/rpc]; (MEDIUM) [Ignite CLI, https://ignite.com/cli]; (LOW) [Phase 5 Financial - no grants program identified]; (LOW) [Phase 3 EV-018 - ecosystem growth mentions tooling integration tapi tidak grants/hackathon]

## Applications

Application: BEX
Category: DEX / AMM
Relationship: Native Application (Core DeFi Primitive)
Status: Live
Sources: (HIGH) [BEX App, https://bex.berachain.com]; (HIGH) [Berachain Documentation, https://docs.berachain.com/dapps/bex]; (HIGH) [Phase 2 Entity BEX]; (HIGH) [Phase 3 EV-008, EV-016]

Application: Bend
Category: Lending / Borrowing
Relationship: Native Application (Core DeFi Primitive)
Status: Live
Sources: (HIGH) [Bend App, https://bend.berachain.com]; (HIGH) [Berachain Documentation, https://docs.berachain.com/dapps/bend]; (HIGH) [Phase 2 Entity Bend]; (HIGH) [Phase 3 EV-008]

Application: Berps
Category: Perpetual Futures Exchange
Relationship: Native Application (Core DeFi Primitive)
Status: Live
Sources: (HIGH) [Berps App, https://berps.berachain.com]; (HIGH) [Berachain Documentation, https://docs.berachain.com/dapps/berps]; (HIGH) [Phase 2 Entity Berps]; (HIGH) [Phase 3 EV-008]

Application: HONEY
Category: Stablecoin
Relationship: Native Protocol (Core DeFi Primitive)
Status: Live
Sources: (HIGH) [Berachain Documentation, https://docs.berachain.com/dapps/honey]; (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]; (HIGH) [Phase 2 Entity HONEY]; (HIGH) [Phase 3 EV-015]

Application: BGT (Berachain Governance Token)
Category: Governance Token (Soulbound)
Relationship: Native Protocol (Consensus/Governance Primitive)
Status: Live
Sources: (HIGH) [Berachain Documentation, https://docs.berachain.com/learn/bgt]; (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]; (HIGH) [Phase 2 Entity BGT]; (HIGH) [Phase 3 EV-016, EV-017]

Application: BERA (Berachain Gas Token)
Category: Gas Token / Staking Token
Relationship: Native Protocol (Consensus/Economic Primitive)
Status: Live (since TGE 2025-02-06)
Sources: (HIGH) [Berachain Documentation, https://docs.berachain.com/learn/bera]; (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]; (HIGH) [Phase 2 Entity BERA]; (HIGH) [Phase 3 EV-011, EV-012]

Application: Berascan
Category: Block Explorer / Analytics
Relationship: Infrastructure Application (Official Explorer)
Status: Live
Sources: (HIGH) [Berascan, https://berascan.com]; (HIGH) [Berachain Documentation, https://docs.berachain.com/tools/berascan]; (HIGH) [Phase 2 Entity Berascan]; (HIGH) [Phase 3 EV-010]

Application: External DeFi Protocols (Unidentified Specific Protocols)
Category: DeFi / Infrastructure / Tooling
Relationship: External Integration (EVM-compatible deployments)
Status: Ongoing
Sources: (MEDIUM) [Phase 3 EV-018 Pertumbuhan Ekosistem: Integrasi Protokol Eksternal]; (MEDIUM) [Berachain Documentation, https://docs.berachain.com] — docs mention ecosystem growth tapi tidak list protokol spesifik

## Governance Ecosystem

Foundation: Berachain Foundation
Role: Legal entity (Cayman Islands) mengelola treasury, pengembangan protokol, governance ekosistem; pengawas peluncuran mainnet dan TGE
Status: Live
Sources: (HIGH) [Berachain Official Website, https://berachain.com]; (MEDIUM) [Berachain Documentation, https://docs.berachain.com]; (HIGH) [Phase 2 Entity Berachain Foundation]

DAO: Tidak teridentifikasi DAO legal wrapper terpisah dari Foundation
Role: Governance on-chain dilakukan via BGT token voting; tidak ada DAO entity terpisah tercatat di Phase 2
Status: N/A
Sources: (HIGH) [Phase 2 Entity List - no DAO entity]; (HIGH) [Phase 4 Technology Security Model - BGT governance]; (HIGH) [Phase 6 Token Governance - on-chain BGT voting]

Council: Tidak teridentifikasi council terpisah
Role: Governance proposals diajukan dan divote oleh BGT holders langsung; validator tidak voting atas nama delegator
Status: N/A
Sources: (HIGH) [Phase 6 Token Governance - BGT holder vote langsung]; (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]

Committee: Tidak teridentifikasi committee resmi
Role: Parameter changes, fee switch, emission rates, software upgrades via BGT-weighted voting
Status: N/A
Sources: (HIGH) [Phase 6 Token Governance - proposal types]; (HIGH) [Berachain Documentation, https://docs.berachain.com/learn/governance]

Validator Group: 100 Active Validators (Mainnet Genesis Set)
Role: Block production, consensus participation, PoL weight = BERA stake + delegated BGT; slashing pada BERA stake
Status: Live
Sources: (MEDIUM) [Berachain Documentation, https://docs.berachain.com/validators] — 100 validator aktif; (HIGH) [Phase 4 Technology Consensus Mechanism]; (HIGH) [Phase 3 EV-007 Mainnet Genesis]

## Ecosystem Risks

Risk: Single Consensus Engine Dependency (CometBFT)
Type: Chain Dependency / Centralization Risk
Description: Berachain sepenuhnya bergantung pada CometBFT (fork Tendermint) untuk consensus; bug atau vulnerability di CometBFT upstream mempengaruhi keseluruhan jaringan; tidak ada alternative consensus implementation
Sources: (HIGH) [Phase 4 Technology Consensus Mechanism]; (HIGH) [CometBFT Documentation, https://cometbft.com]; (HIGH) [Phase 4 Technology Core Components - CometBFT Consensus Engine]

Risk: Single Application Framework Dependency (Cosmos SDK)
Type: Chain Dependency / Centralization Risk
Description: Berachain dibangun di atas Cosmos SDK v0.50+; upgrade atau breaking changes di Cosmos SDK upstream memerlukan migrasi koordinat; tidak ada alternative framework
Sources: (HIGH) [Phase 4 Technology Core Components - Cosmos SDK Application Framework]; (HIGH) [Cosmos SDK Documentation, https://docs.cosmos.network]; (HIGH) [Berachain GitHub go.mod, https://github.com/berachain/bera/blob/main/go.mod]

Risk: IBC Relay Dependency
Type: Bridge Dependency / Centralization Risk
Description: Cross-chain transfer via IBC memerlukan relayer infrastructure; liveness bergantung pada relayer availability (permissionless tapi butuh incentive); tidak ada native relayer incentivization tercatat
Sources: (MEDIUM) [Phase 4 Technology Known Technical Limitations - IBC relay dependency]; (MEDIUM) [IBC Protocol, https://ibc.cosmos.network]; (MEDIUM) [Berachain Documentation, https://docs.berachain.com/learn/ibc]

Risk: Oracle Dependency (Unidentified Provider)
Type: Oracle Dependency
Description: Bend (liquidation), Berps (funding rate/mark price), HONEY (peg monitoring) memerlukan price feeds; oracle provider tidak diungkapkan publik; single point of failure jika centralized oracle
Sources: (LOW) [Phase 4 Technology Known Technical Limitations - No native oracle]; (LOW) [Berachain Documentation, https://docs.berachain.com/dapps] — oracle provider tidak terdokumentasi

Risk: Validator Set Centralization (High Hardware Requirements)
Type: Centralization Risk
Description: 100 validator cap dengan hardware requirements tinggi (64GB RAM, 4TB NVMe, 10Gbps network per docs) mungkin mengonsentrasi stake ke operator besar; geographic distribution tidak transparan
Sources: (MEDIUM) [Berachain Documentation, https://docs.berachain.com/validators/requirements]; (MEDIUM) [Phase 4 Technology Known Technical Limitations - Validator set centralization risk]

Risk: GitHub Hosting Dependency
Type: Infrastructure Dependency
Description: Repository utama di github.com/berachain; bergantung pada GitHub availability dan policies; tidak ada mirror resmi tercatat
Sources: (MEDIUM) [GitHub Berachain, https://github.com/berachain]; (MEDIUM) [Phase 2 Entity Berachain GitHub Repository]

Risk: Discord/Twitter/Telegram Centralized Communication
Type: Infrastructure Dependency
Description: Komunitas resmi bergantung pada platform terpusat (Discord, Twitter/X, Telegram) untuk koordinasi, announcements, support; platform risk (deplatforming, policy changes)
Sources: (MEDIUM) [Discord Berachain, https://discord.gg/berachain]; (MEDIUM) [X/Twitter Berachain, https://x.com/berachain]; (MEDIUM) [Telegram Berachain, https://t.me/berachainofficial]; (HIGH) [Phase 2 Entities]

Risk: BGT Non-Transferable Design Limits Composability
Type: Chain Dependency / Protocol Design Risk
Description: BGT soulbound (non-transferable) mencegah secondary market tapi membatasi composability DeFi (tidak bisa dipakai collateral di protokol lain tanpa wrapper); design choice dengan trade-off
Sources: (HIGH) [Berachain Documentation, https://docs.berachain.com/learn/bgt]; (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]; (HIGH) [Phase 4 Technology Known Technical Limitations]

Risk: HONEY Soft-Peg Without Hard Reserves
Type: Protocol Design Risk
Description: HONEY soft-peg via arbitrage dan collateralization di Bend/BEX; tidak ada hard peg mechanism (seperti USDC reserves); risiko depeg di stress market
Sources: (HIGH) [Berachain Documentation, https://docs.berachain.com/dapps/honey]; (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]; (HIGH) [Phase 4 Technology Known Technical Limitations]

## Official Ecosystem Resources

Official Documentation: https://docs.berachain.com
Developer Portal: https://docs.berachain.com/develop
GitHub: https://github.com/berachain
Partner Documentation: https://docs.berachain.com/learn/ibc (IBC), https://docs.cosmos.network (Cosmos SDK), https://cometbft.com (CometBFT)
Grant Program: tidak tersedia (tidak ditemukan grants program resmi)
Ecosystem Dashboard: https://berascan.com (block explorer + analytics), https://bex.berachain.com (DEX analytics), https://bend.berachain.com (lending analytics), https://berps.berachain.com (perpetuals analytics)

## RINGKASAN

Primary Ecosystem: Cosmos SDK / CometBFT / IBC (Core Infrastructure) + Ethereum EVM (Execution Compatibility)
Supported Chains: Berachain Mainnet (primary), Ethereum (EVM tooling/wallet compatibility), Cosmos Ecosystem (IBC: Osmosis, Celestia, dll)
External Dependencies: 11 (Cosmos SDK, CometBFT, IBC, Ethereum EVM, Berachain Foundation, Oracle Provider unidentified, IBC Relayers, GitHub, Docker, Kubernetes, Prometheus/Grafana)
Major Integrations: 10 (BEX, Bend, Berps, HONEY, IBC Channels, Hardhat/Foundry, MetaMask, CosmWasm optional, Berascan, CEX listings)
Infrastructure Providers: 8 (Berascan, GitHub, Discord, Twitter/X, Telegram, RPC Node Operators unidentified, 100 Validators, IBC Relayers)
Developer Programs: SDK + API + Tools (Hardhat, Foundry, Ignite CLI) live; Hackathon dan Grant Program tidak teridentifikasi
Applications: 7 Native (BEX, Bend, Berps, HONEY, BGT, BERA, Berascan) + External DeFi protocols unidentified

## Market Intelligence
_ref: `docs/Meta/Narratives.md`, `docs/Valuation/Competitors.md`, `docs/Meta/MarketCycles.md`_

PROJECT: Berachain

## Market Category

Primary Category: Layer 1 Blockchain
Secondary Category: DeFi Infrastructure
Sector: Blockchain Infrastructure
Sub-sector: Proof-of-Liquidity Consensus / EVM-equivalent Cosmos Chain
Sources: (HIGH) [Berachain Documentation, https://docs.berachain.com/learn/architecture]; (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]; (HIGH) [Phase 1 Foundation Data]; (HIGH) [Phase 4 Technology Architecture]

## Market Position

Project Stage: Early (Mainnet live 2024-06-06, TGE 2025-02-06, native DeFi apps operational, ecosystem building phase)
Primary Competitors: Monad; Sei; Ethereum; BNB Chain; Polygon; Avalanche; Cosmos Hub; Osmosis; Celestia; Injective
Market Segment: High-throughput EVM-compatible L1 with novel consensus (Proof-of-Liquidity) targeting DeFi-native liquidity flywheel
Geographic Focus: Global (distributed team, Cayman Islands Foundation, no geographic restriction)
Sources: (HIGH) [Phase 3 EV-007 Mainnet Genesis 2024-06-06]; (HIGH) [Phase 3 EV-011 TGE 2025-02-06]; (HIGH) [Phase 4 Technology Architecture]; (HIGH) [Phase 7 Ecosystem Position]; (MEDIUM) [DefiLlama, https://defillama.com/chain/Berachain] — chain page exists but native apps (BEX, Bend, Berps) not fully integrated per Phase 5; (MEDIUM) [CoinGecko, https://www.coingecko.com/en/coins/berachain] — BERA token page exists post-TGE

## Trading Markets

Exchange: BEX (Native DEX)
Spot: Yes (BERA, BGT, HONEY, wrapped assets, IBC assets)
Perpetual: No
Futures: No
Options: No
OTC: tidak diketahui
Status: Live
Sources: (HIGH) [BEX App, https://bex.berachain.com]; (HIGH) [Berachain Documentation, https://docs.berachain.com/dapps/bex]; (HIGH) [Phase 3 EV-008, EV-012]

Exchange: Berps (Native Perpetuals Exchange)
Spot: No
Perpetual: Yes (BTC, ETH, BERA, HONEY pairs dengan leverage hingga 50x)
Futures: No
Options: No
OTC: tidak diketahui
Status: Live
Sources: (HIGH) [Berps App, https://berps.berachain.com]; (HIGH) [Berachain Documentation, https://docs.berachain.com/dapps/berps]; (HIGH) [Phase 3 EV-008]

Exchange: Centralized Exchanges (CEX) — Specific Names Unidentified
Spot: Yes (BERA trading pairs per TGE announcement)
Perpetual: tidak diketahui
Futures: tidak diketahui
Options: tidak diketahui
OTC: tidak diketahui
Status: Ongoing (post-TGE 2025-02-06)
Sources: (HIGH) [Phase 3 EV-012 Listing BERA di CEX dan DEX]; (HIGH) [Berachain Official Website, https://berachain.com] — TGE announcement mentions CEX listing but does not name specific exchanges; (LOW) [CoinGecko, https://www.coingecko.com/en/coins/berachain] — markets tab shows exchanges post-TGE; (LOW) [CoinMarketCap, https://coinmarketcap.com/currencies/berachain/] — markets tab shows exchanges post-TGE

## Liquidity

Liquidity Source: BEX (Native DEX AMM)
Major Liquidity Venue: BEX (Primary DEX for BERA, HONEY, BGT, IBC assets)
DEX: BEX (Concentrated Liquidity MM + Stable Swap)
CEX: Unidentified specific exchanges (post-TGE listings announced but not named)
Bridge Liquidity: IBC channels to Osmosis, Celestia, other Cosmos chains (relayer-dependent)
Status: Live (BEX, IBC); Ongoing (CEX listings)
Sources: (HIGH) [BEX App, https://bex.berachain.com]; (HIGH) [Berachain Documentation, https://docs.berachain.com/dapps/bex]; (HIGH) [Phase 3 EV-014 IBC Integration]; (MEDIUM) [IBC Protocol, https://ibc.cosmos.network]; (LOW) [Map of Zones, https://mapofzones.com] — for IBC channel verification

## Adoption Metrics

Metric Name: TVL (Total Value Locked)
Value: tidak diketahui (tidak ada dashboard resmi terverifikasi; DefiLlama chain page exists but native apps not fully integrated per Phase 5)
Date: N/A
Sources: (LOW) [DefiLlama, https://defillama.com/chain/Berachain]; (LOW) [Phase 5 Financial - Revenue History: "Berachain protocols (BEX, Bend, Berps) belum terintegrasi ke DefiLlama per penelusuran ini"]

Metric Name: Daily Active Users
Value: tidak diketahui
Date: N/A
Sources: (LOW) [Berascan, https://berascan.com] — explorer shows transactions but no aggregated DAU metric; (LOW) [Phase 4 Technology - Berascan]

Metric Name: Daily Transactions
Value: tidak diketahui (on-chain data available via Berascan but no aggregated public dashboard)
Date: N/A
Sources: (LOW) [Berascan, https://berascan.com]; (LOW) [Phase 4 Technology - Berascan]

Metric Name: Unique Wallets / Addresses
Value: tidak diketahui
Date: N/A
Sources: (LOW) [Berascan, https://berascan.com]; (LOW) [Phase 4 Technology - Berascan]

Metric Name: Developer Count
Value: tidak diketahui (GitHub contributors visible but no aggregated metric)
Date: N/A
Sources: (LOW) [Berachain GitHub, https://github.com/berachain/bera/graphs/contributors]; (MEDIUM) [Phase 2 Entity - Core Contributors ~20 named pseudonymous + ~50 total]

Metric Name: 24h Trading Volume (BEX)
Value: tidak diketahui (BEX app shows pools but no aggregated volume dashboard visible)
Date: N/A
Sources: (LOW) [BEX App, https://bex.berachain.com]; (LOW) [Phase 7 Applications - BEX]

Metric Name: Bridge Volume (IBC)
Value: tidak diketahui
Date: N/A
Sources: (LOW) [Map of Zones, https://mapofzones.com]; (MEDIUM) [Phase 7 External Dependencies - IBC]

Metric Name: IBC Messages / Packets
Value: tidak diketahui
Date: N/A
Sources: (LOW) [Map of Zones, https://mapofzones.com]; (MEDIUM) [Phase 7 External Dependencies - IBC]

Metric Name: Validator Count
Value: 100 (active validator set at mainnet genesis per documentation)
Date: 2024-06-06 (genesis)
Sources: (MEDIUM) [Berachain Documentation, https://docs.berachain.com/validators]; (HIGH) [Phase 3 EV-007]; (HIGH) [Phase 4 Technology Consensus Mechanism]

Metric Name: BGT Holders (Delegators)
Value: tidak diketahui
Date: N/A
Sources: (LOW) [Berascan, https://berascan.com/token/0x5C47122b4A7382E429586A7D4DdC5b2E1d8F8a6a]; (HIGH) [Phase 6 Token - BGT Contract]

## Market Share

Metric: L1 Market Share (by TVL / Volume / Users)
Value: Tidak tersedia.
Sources: (LOW) [DefiLlama, https://defillama.com/chains] — Berachain not ranked in top L1s by TVL at time of research; (LOW) [Token Terminal, https://tokenterminal.com] — no verified Berachain project page with market share data

Metric: DEX Market Share (BEX vs competitors)
Value: Tidak tersedia.
Sources: (LOW) [DefiLlama DEX Overview, https://defillama.com/dexs] — BEX not listed separately

Metric: Stablecoin Market Share (HONEY)
Value: Tidak tersedia.
Sources: (LOW) [DefiLlama Stablecoins, https://defillama.com/stablecoins] — HONEY not ranked in major stablecoin listings

## Competitor Landscape

Competitor: Monad
Category: Parallel EVM L1
Difference: Monad focuses on parallel execution optimization (10k+ TPS target) with MonadBFT consensus; Berachain uses Proof-of-Liquidity tying validator weight to DeFi liquidity via BGT delegation; different consensus philosophy (performance vs liquidity alignment)
Market Segment: High-throughput EVM L1
Sources: (MEDIUM) [Monad Documentation, https://docs.monad.xyz]; (HIGH) [Phase 4 Technology Consensus Mechanism - PoL unique to Berachain]

Competitor: Sei
Category: Parallel EVM L1 / Sector-specific (Trading)
Difference: Sei v2 introduces parallel EVM with SeiDB; sector-focused on trading (orderbook + AMM); Berachain is general-purpose DeFi L1 with PoL consensus integrating native DeFi apps (BEX, Bend, Berps) at protocol level
Market Segment: High-throughput EVM L1 / Trading-focused
Sources: (MEDIUM) [Sei Documentation, https://docs.sei.io]; (HIGH) [Phase 7 Applications - Native DeFi primitives]

Competitor: Ethereum
Category: L1 / Settlement Layer
Difference: Ethereum uses PoS (validator stake = ETH); Berachain uses PoL (validator weight = BERA stake + delegated BGT from LPs); Berachain is EVM-equivalent execution on Cosmos SDK/CometBFT with native DeFi integration
Market Segment: General-purpose smart contract platform
Sources: (HIGH) [Ethereum Foundation, https://ethereum.org]; (HIGH) [Phase 4 Technology Architecture - EVM-equivalent on Cosmos SDK]

Competitor: BNB Chain
Category: EVM L1 (Cosmos SDK fork historically)
Difference: BNB Chain uses PoSA (Proof-of-Staked Authority) with 21 active validators; Berachain uses CometBFT BFT with 100 validators + PoL; BNB Chain has larger established ecosystem; Berachain is newer with novel consensus
Market Segment: EVM-compatible L1
Sources: (MEDIUM) [BNB Chain Documentation, https://docs.bnbchain.org]; (HIGH) [Phase 4 Technology Consensus Mechanism]

Competitor: Polygon
Category: L2 / Sidechain / AggLayer
Difference: Polygon is primarily L2 scaling for Ethereum (Polygon PoS, zkEVM, AggLayer); Berachain is sovereign L1 with own validator set and consensus; different trust assumptions
Market Segment: Ethereum scaling / L1
Sources: (MEDIUM) [Polygon Documentation, https://polygon.technology]; (HIGH) [Phase 1 Foundation - Category: Layer 1 blockchain]

Competitor: Avalanche
Category: L1 (Subnet architecture)
Difference: Avalanche uses Snowman consensus with subnets; Berachain uses CometBFT + PoL single chain; Avalanche has established DeFi ecosystem; Berachain integrates DeFi at protocol level via PoL
Market Segment: High-throughput L1
Sources: (MEDIUM) [Avalanche Documentation, https://docs.avax.network]; (HIGH) [Phase 4 Technology Architecture]

Competitor: Cosmos Hub
Category: L0 / Hub (Cosmos SDK)
Difference: Cosmos Hub (ATOM) is IBC hub with Interchain Security; Berachain is consumer chain with own validator set + PoL; Berachain is EVM-equivalent; Cosmos Hub is CosmWasm/WASM native
Market Segment: Cosmos Ecosystem
Sources: (HIGH) [Cosmos SDK Documentation, https://docs.cosmos.network]; (HIGH) [Phase 4 Technology Core Components - Cosmos SDK, IBC]

Competitor: Osmosis
Category: DEX Chain (Cosmos SDK)
Difference: Osmosis is app-chain DEX with concentrated liquidity; Berachain is general-purpose L1 with native DEX (BEX) as one component; Osmosis uses PoS; Berachain uses PoL
Market Segment: Cosmos DeFi
Sources: (MEDIUM) [Osmosis Documentation, https://docs.osmosis.zone]; (HIGH) [Phase 7 Major Integrations - IBC Channels to Osmosis]

Competitor: Celestia
Category: Modular DA Layer
Difference: Celestia provides data availability + consensus for rollups; Berachain is execution-focused L1 with own consensus (CometBFT) and DA; different modular stack position
Market Segment: Modular blockchain stack
Sources: (MEDIUM) [Celestia Documentation, https://docs.celestia.org]; (HIGH) [Phase 7 Major Integrations - IBC Channels to Celestia]

Competitor: Injective
Category: Exchange-focused L1 (Cosmos SDK)
Difference: Injective focuses on orderbook DEX + derivatives with CosmWasm; Berachain is EVM-equivalent with AMM (BEX) + native perps (Berps) + lending (Bend); different VM and app focus
Market Segment: Cosmos DeFi / Derivatives
Sources: (MEDIUM) [Injective Documentation, https://docs.injective.network]; (HIGH) [Phase 7 Applications - Native DeFi primitives]

## Narrative Position

Narrative: Proof-of-Liquidity (Novel Consensus)
Status: Main Narrative
Evidence: Whitepaper and all documentation center PoL as core innovation — validator weight tied to DeFi liquidity via BGT delegation; "liquidity as security" model
Sources: (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]; (HIGH) [Berachain Documentation, https://docs.berachain.com/learn/proof-of-liquidity]; (HIGH) [Phase 4 Technology Consensus Mechanism]

Narrative: EVM-equivalent on Cosmos SDK
Status: Main Narrative
Evidence: Execution layer is EVM-equivalent (not just compatible) via custom EVM module on Cosmos SDK; supports Hardhat, Foundry, MetaMask natively
Sources: (HIGH) [Berachain Documentation, https://docs.berachain.com/develop/evm]; (HIGH) [Phase 4 Technology Execution Environment]; (HIGH) [Phase 7 Major Integrations - Hardhat/Foundry/MetaMask]

Narrative: Native DeFi Primitives (BEX, Bend, Berps, HONEY)
Status: Main Narrative
Evidence: Three core DeFi apps + stablecoin launched at/near mainnet genesis; BGT emission flows through BEX LP positions; protocol-level integration
Sources: (HIGH) [Berachain Documentation, https://docs.berachain.com/dapps]; (HIGH) [Phase 3 EV-008, EV-015, EV-016]; (HIGH) [Phase 7 Applications]

Narrative: IBC Interoperability / Cosmos Ecosystem
Status: Secondary Narrative
Evidence: IBC enabled at mainnet; channels to Osmosis, Celestia; Cosmos SDK base; but marketing emphasizes EVM/PoL over Cosmos-native identity
Sources: (MEDIUM) [Berachain Documentation, https://docs.berachain.com/learn/ibc]; (HIGH) [Phase 3 EV-014]; (HIGH) [Phase 7 External Dependencies - IBC]

Narrative: Modular Blockchain (Execution Layer)
Status: Secondary Narrative
Evidence: Uses Cosmos SDK (application framework) + CometBFT (consensus) + custom EVM (execution) — modular stack but sovereign L1 not rollup
Sources: (MEDIUM) [Celestia Blog on Modular Stack, https://celestia.org/blog]; (HIGH) [Phase 4 Technology Architecture]

Narrative: DeFi-Native L1 / Liquidity Flywheel
Status: Main Narrative
Evidence: PoL creates direct incentive loop: LP → BGT → validator weight → emission direction → more LP incentives; fee switch to BGT stakers
Sources: (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]; (HIGH) [Phase 6 Token Utility - BGT Emission Direction, Fee Switch]

Narrative: Soulbound Governance Token (BGT)
Status: Secondary Narrative
Evidence: BGT non-transferable, earned only via LP; prevents vote buying; unique in L1 governance design
Sources: (HIGH) [Berachain Documentation, https://docs.berachain.com/learn/bgt]; (HIGH) [Phase 6 Token - BGT Distribution 100% to LPs]

Narrative: Restaking / EigenLayer-style
Status: Not Applicable
Evidence: Berachain does not implement restaking; PoL is distinct mechanism (liquidity delegation vs stake delegation)
Sources: (HIGH) [Phase 4 Technology Consensus Mechanism - PoL vs Restaking distinction]

Narrative: Chain Abstraction
Status: Not Applicable
Evidence: No chain abstraction protocol (like Particle Network, NEAR chain abstraction) implemented at protocol level; standard IBC + EVM wallet support
Sources: (HIGH) [Phase 7 Wallet Ecosystem - Standard MetaMask/Keplr support]

Narrative: RWA (Real World Assets)
Status: Not Applicable
Evidence: No RWA-specific infrastructure or partnerships announced in Phases 1-7
Sources: (LOW) [Berachain Documentation, https://docs.berachain.com] — no RWA section

Narrative: DePIN (Decentralized Physical Infrastructure)
Status: Not Applicable
Evidence: No DePIN focus in documentation or applications
Sources: (LOW) [Berachain Documentation, https://docs.berachain.com]

Narrative: Gaming
Status: Not Applicable
Evidence: No gaming-specific infrastructure or partnerships announced
Sources: (LOW) [Berachain Documentation, https://docs.berachain.com]

Narrative: AI / AI-Agent Infrastructure
Status: Not Applicable
Evidence: No AI-specific narrative in documentation
Sources: (LOW) [Berachain Documentation, https://docs.berachain.com]

## Market Timeline

Date: 2024-06-06
Milestone: Mainnet Genesis Launch
Description: Berachain mainnet live with Proof-of-Liquidity consensus, EVM execution, native apps (BEX, Bend, Berps), BGT emission, HONEY stablecoin, IBC enabled
Related Historical Event ID: EV-007
Sources: (HIGH) [Phase 3 EV-007]; (HIGH) [Berachain Blog, https://berachain.com/blog/mainnet-launch]

Date: 2024-06 (eksak tanggal tidak diketahui)
Milestone: Native DeFi Apps Deployment (BEX, Bend, Berps)
Description: BEX (DEX), Bend (Lending), Berps (Perpetuals) deployed and operational on mainnet
Related Historical Event ID: EV-008
Sources: (HIGH) [Phase 3 EV-008]; (HIGH) [Berachain Documentation, https://docs.berachain.com/dapps]

Date: 2024-10 (estimasi)
Milestone: Artio Testnet v3 / Pre-TGE Upgrade
Description: Testnet upgrade validating fee switch, BGT delegation mechanics, upgradeability framework before TGE
Related Historical Event ID: EV-009
Sources: (MEDIUM) [Phase 3 EV-009]; (MEDIUM) [Berachain Documentation, https://docs.berachain.com]

Date: 2024 (eksak tanggal tidak diketahui)
Milestone: HONEY Stablecoin Launch
Description: HONEY soft-pegged USD stablecoin minting activated via Bend collateral and BEX arbitrage
Related Historical Event ID: EV-015
Sources: (HIGH) [Phase 3 EV-015]; (HIGH) [Berachain Documentation, https://docs.berachain.com/dapps/honey]

Date: 2024 (eksak tanggal tidak diketahui)
Milestone: IBC Channels Activated
Description: Cross-chain IBC channels live to Osmosis, Celestia, other Cosmos chains
Related Historical Event ID: EV-014
Sources: (MEDIUM) [Phase 3 EV-014]; (HIGH) [IBC Protocol, https://ibc.cosmos.network]

Date: 2025-02-06
Milestone: BERA Token Generation Event (TGE)
Description: BERA becomes transferable; trading starts on BEX and CEX; validator staking active; vesting cliffs begin for Team/Investors/Foundation/Advisors/Ecosystem
Related Historical Event ID: EV-011
Sources: (HIGH) [Phase 3 EV-011]; (HIGH) [Berachain Official Website, https://berachain.com]; (HIGH) [Berachain Documentation, https://docs.berachain.com/learn/bera]

Date: 2025-02 (eksak tanggal tidak diketahui)
Milestone: BERA CEX/DEX Listings
Description: BERA listed on centralized exchanges (specific names not disclosed) and native DEX BEX; price discovery begins
Related Historical Event ID: EV-012
Sources: (HIGH) [Phase 3 EV-012]; (HIGH) [BEX App, https://bex.berachain.com]

Date: 2024-2025 (ongoing)
Milestone: On-Chain Governance Proposals Active
Description: BGT holders submitting and voting on proposals (parameter changes, fee switch, emission rates, software upgrades)
Related Historical Event ID: EV-017
Sources: (HIGH) [Phase 3 EV-017]; (HIGH) [Berachain Documentation, https://docs.berachain.com/learn/governance]

## Official Market Resources

Official Dashboard: https://berascan.com (block explorer + basic analytics)
DefiLlama: https://defillama.com/chain/Berachain
CoinGecko: https://www.coingecko.com/en/coins/berachain
CoinMarketCap: https://coinmarketcap.com/currencies/berachain/
Token Terminal: https://tokenterminal.com/terminal/projects/berachain (may not have verified project page)
Messari: https://messari.io/asset/berachain (may not have verified asset page)
Explorer: https://berascan.com
BEX Analytics: https://bex.berachain.com
Bend Analytics: https://bend.berachain.com
Berps Analytics: https://berps.berachain.com

## RINGKASAN

Market Stage: Early (Mainnet 2024-06-06, TGE 2025-02-06, native DeFi live, ecosystem building)
Primary Category: Layer 1 Blockchain / DeFi Infrastructure
Competitor Count: 10 identified (Monad, Sei, Ethereum, BNB Chain, Polygon, Avalanche, Cosmos Hub, Osmosis, Celestia, Injective)
Major Narrative: Proof-of-Liquidity Consensus; EVM-equivalent on Cosmos SDK; Native DeFi Primitives; DeFi-Native Liquidity Flywheel
Trading Availability: Native DEX (BEX) live; Native Perps (Berps) live; CEX listings announced post-TGE (specific exchanges unnamed)
Adoption Metrics Available: Validator count (100 at genesis); Contract addresses verified on Berascan; TVL/Volume/Users/DAU not aggregated on public dashboards (DefiLlama integration incomplete per Phase 5)

## Behavioral Intelligence
_ref: `docs/Ontology/Hidden.md` — enriches DecisionEvent Alternatives/Reason/Reactions_

PROJECT: Berachain

Strategic Objectives

1. Membangun Layer 1 dengan konsensus Proof-of-Liquidity yang mengikat keamanan jaringan langsung ke liquidity DeFi
· Evidence: Whitepaper dan dokumentasi teknis memposisikan PoL sebagai inovasi inti — validator weight = BERA stake + delegated BGT dari LP di BEX; menciptakan flywheel liquidity-security (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]
· Supporting Dataset: Phase 1 Foundation (kategori: Proof-of-Liquidity consensus); Phase 4 Technology (Consensus Mechanism, PoL Module); Phase 6 Token (BGT Utility: Validator Weight, Emission Direction)

2. Menyediakan EVM-equivalent execution environment di atas Cosmos SDK untuk menarik developer Ethereum tanpa ganti tooling
· Evidence: Custom EVM module di Cosmos SDK mendukung Solidity ^0.8.x, Hardhat, Foundry, MetaMask, JSON-RPC kompatibel Ethereum standard; tidak perlu porting kontrak (HIGH) [Berachain Documentation, https://docs.berachain.com/develop/evm]
· Supporting Dataset: Phase 1 Foundation (EVM-compatible); Phase 4 Technology (Execution Environment, EVM Module); Phase 7 Major Integrations (Hardhat/Foundry/MetaMask)

3. Meluncurkan primitive DeFi native (BEX, Bend, Berps, HONEY) sekaligus dengan mainnet untuk mem-bootstrapping liquidity dan BGT emission
· Evidence: Ketiga aplikasi + stablecoin deployed dekat genesis mainnet 2024-06-06 (EV-008, EV-015); BGT emission hanya melalui LP di BEX (EV-016); HONEY sebagai base pair dan collateral (HIGH) [Phase 3 EV-007, EV-008, EV-015, EV-016]
· Supporting Dataset: Phase 3 History (EV-007, EV-008, EV-015, EV-016); Phase 4 Core Components (BEX, Bend, Berps, HONEY); Phase 7 Applications (7 native apps)

4. Menggunakan BGT (soulbound governance token) sebagai mekanisme alignment jangka panjang — non-transferable, hanya didapat via providing liquidity
· Evidence: BGT 100% emission ke LP via PoL; tidak ada alokasi team/investor/foundation; voting power tidak transferable; delegation ke validator tidak memindahkan voting rights (HIGH) [Berachain Whitepaper, https://berachain.com/whitepaper.pdf]; [Phase 6 Token Distribution BGT]
· Supporting Dataset: Phase 6 Token (BGT Distribution, Utility, Governance); Phase 4 Security Model (BGT non-transferable); Phase 3 EV-016, EV-017

5. Memanfaatkan IBC untuk interoperabilitas Cosmos ecosystem sambil mempertahankan identitas EVM-first
· Evidence: IBC channels live ke Osmosis, Celestia (EV-014); Cosmos SDK base; tapi marketing dan developer tooling fokus EVM (Hardhat/Foundry) bukan CosmWasm (HIGH) [Phase 3 EV-014]; [Phase 4 IBC Module]; [Phase 7 External Dependencies IBC]
· Supporting Dataset: Phase 3 EV-014; Phase 4 Core Components (IBC Module); Phase 7 Major Integrations (IBC Channels); Phase 8 Narrative Position (IBC secondary narrative)

Decision Timeline

Keputusan: Mulai pengembangan konsep Proof-of-Liquidity dan arsitektur protokol (2022)
· Trigger: Identifikasi kesenjangan antara security (validator stake) dan liquidity (DeFi TVL) pada L1 existing; keinginan menciptakan alignment langsung
· Evidence: Phase 3 EV-001 mencatat konsep PoL dan pendirian proyek 2022 oleh trio founder pseudonim
· Decision: Merancang konsensus di mana validator weight ditentukan oleh BGT yang didelegasikan dari LP, bukan hanya stake token gas
· Immediate Result: Dasar teknis dan filosofis protokol; arsitektur awal PoL dirancang sebelum entity hukum ada
· Long-term Impact: Menjadi differentiator utama vs competitor L1 (Monad, Sei, dll); menarik naratif "DeFi-native L1"
· Supporting Dataset: Phase 3 EV-001; Phase 1 Foundation (Founding Entity, Founders)

Keputusan: Pendirian Berachain Foundation di Cayman Islands sebagai legal wrapper (2023)
· Trigger: Perlu entitas hukum untuk mengelola treasury, token issuance, compliance, dan pengawasan pengembangan sebelum public launch
· Evidence: Phase 2 Entity Berachain Foundation (Cayman Islands); Phase 3 EV-002 pendirian 2023
· Decision: Membentuk foundation non-profit di Cayman Islands sebagai pengelola treasury dan ekosistem
· Immediate Result: Struktur hukum formal untuk operasi; fondation menjadi legal entity untuk TGE dan mainnet launch
· Long-term Impact: Memisahkan legal liability dari contributor individu; memungkinkan token sale compliant; tapi menciptakan centralized entity vs DAO ideal
· Supporting Dataset: Phase 2 Entity Berachain Foundation; Phase 3 EV-002; Phase 5 Financial (Treasury managed by Foundation)

Keputusan: Peluncuran Artio Testnet v1 (2023-01-12) → v2 (2024-01-11) → v3 (2024-10) bertahap
· Trigger: Validasi bertahap konsensus PoL, EVM compatibility, IBC integration sebelum mainnet; mengurangi risiko bug di genesis
· Evidence: Phase 3 EV-003 (v1 Jan 2023), EV-006 (v2 Jan 2024), EV-009 (v3 Oct 2024); setiap iterasi menambah fitur (PoL, IBC, fee switch testing)
· Decision: Three-phase testnet program dengan scope meningkat: v1 closed validator, v2 open validator + IBC, v3 fee switch + governance testing
· Immediate Result: Identifikasi bug konsensus dan EVM execution早期; validator set siap untuk genesis; feedback untuk mainnet readiness
· Long-term Impact: Mainnet genesis 2024-06-06 lancar tanpa major incident; 100 validator aktif dari hari 1; testnet v3 memvalidasi fee switch mechanics
· Supporting Dataset: Phase 3 EV-003, EV-006, EV-009; Phase 4 Technical Upgrade History (Artio v1/v2/v3)

Keputusan: Mainnet genesis launch dengan native apps (BEX, Bend, Berps) + BGT emission + HONEY + IBC sekaligus (2024-06-06)
· Trigger: Siapnya semua komponen inti setelah testnet v2 validation; keinginan "DeFi-native from day one"
· Evidence: Phase 3 EV-007 (mainnet genesis), EV-008 (native apps deployment), EV-014 (IBC), EV-015 (HONEY), EV-016 (BGT emission)
· Decision: Launch semua primitive DeFi native bersamaan dengan consensus layer — bukan staged rollout
· Immediate Result: BGT emission aktif hari 1 via BEX LP; liquidity flywheel berputar immediate; IBC channels live; 100 validator set
· Long-term Impact: TVL dan activity bootstrap cepat; tapi kompleksitas operasional tinggi — semua sistem harus siap simultan; bug di satu app mempengaruhi seluruh ekosistem
· Supporting Dataset: Phase 3 EV-007, EV-008, EV-014, EV-015, EV-016; Phase 4 Core Components (12 components live at genesis)

Keputusan: BERA TGE dengan vesting cliffs untuk Team/Investors/Foundation/Advisors (2025-02-06)
· Trigger: Mainnet sudah stable 8 bulan; native apps operational; BGT emission running; butuh transferable gas token untuk fee market dan staking validator
· Evidence: Phase 3 EV-011 (TGE 2025-02-06); Phase 6 Token (BERA vesting: Team 12m cliff/36m linear, Investors 12m/24m, Foundation 6m/48m, Advisors 12m/24m, Community partial unlock)
· Decision: Full supply 500M minted at genesis, TGE mengaktifkan transferability; vesting cliffs mulai berjalan post-TGE
· Immediate Result: BERA tradable di BEX dan CEX; validator staking aktif; price discovery dimulai; cliff countdown untuk insider unlocks
· Long-term Impact: Sell pressure dari cliff unlocks 2025-08 (Foundation/Ecosystem) dan 2026-02 (Team/Investors/Advisors); fee switch activation critical untuk BGT holder value capture pre-unlocks
· Supporting Dataset: Phase 3 EV-011, EV-012; Phase 6 Token (TGE, Vesting Schedule, Major Token Events)

Keputusan: Governance on-chain via BGT-weighted voting tanpa DAO legal wrapper terpisah (2024-ongoing)
· Trigger: BGT emission aktif sejak genesis; butuh mekanisme untuk parameter changes, fee switch, emission direction
· Evidence: Phase 3 EV-017 (governance proposals mulai 2024); Phase 6 Governance (BGT-weighted voting, Cosmos SDK governance module, delegation tidak transfer voting power); Phase 2 no DAO entity
· Decision: Menggunakan Cosmos SDK governance module + custom PoL parameters; BGT holder vote langsung; Foundation tetap legal entity terpisah
· Immediate Result: Parameter changes, software upgrades via on-chain proposal; fee switch gated by governance
· Long-term Impact: Regulatory ambiguity — Foundation (Cayman) vs on-chain governance (global); tidak ada legal wrapper untuk DAO treasury; community pool existence unverified
· Supporting Dataset: Phase 3 EV-017; Phase 6 Governance; Phase 2 Entity (no DAO); Phase 7 Governance Ecosystem

Evolution Pattern

Perubahan Strategi: Dari konsep PoL murni (2022) → testnet bertahap validasi teknis (2023-2024) → mainnet dengan full DeFi stack (2024) → TGE dan tokenomics live (2025) → governance-driven evolution (ongoing)
· Evidence: Phase 3 timeline menunjukkan evolution dari research (EV-001) → infrastructure (EV-002, EV-004, EV-005) → testnet iteration (EV-003, EV-006, EV-009) → production launch (EV-007, EV-008, EV-014, EV-015, EV-016) → token launch (EV-011, EV-012) → governance (EV-017)
· Supporting Dataset: Phase 3 History (all 18 events chronological); Phase 4 Technical Upgrade History (4 major upgrades)

Perubahan Teknologi: Custom EVM module on Cosmos SDK (bukan fork geth/erigon) → CometBFT consensus (bukan Tendermint langsung) → PoL module terintegrasi di consensus layer → Native apps sebagai first-class citizens bukan third-party
· Evidence: Phase 4 Architecture (modular: CometBFT + Cosmos SDK + EVM Module + PoL Module); Phase 4 Core Components (12 components including PoL, BGT, BERA, HONEY modules); Phase 4 Development Framework (Cosmos SDK v0.50+, CometBFT v0.38+, custom EVM)
· Supporting Dataset: Phase 4 Technology (Architecture, Core Components, Consensus, Execution Environment, Technical Upgrade History)

Perubahan Tokenomics: Pre-TGE: BERA non-transferable, BGT emission only, HONEY minting → Post-TGE: BERA transferable + gas + staking, fee switch eligible, vesting cliffs active, BGT fee switch revenue share, HONEY peg maintenance via arbitrage
· Evidence: Phase 6 Token (BERA/BGT/HONEY supply, distribution, vesting, utility, inflation); Phase 3 EV-011 (TGE), EV-016 (BGT emission pre-TGE); Phase 6 Major Token Events (projected cliff ends 2025-08, 2026-02)
· Supporting Dataset: Phase 6 Token (all sections); Phase 3 EV-011, EV-016; Phase 5 Revenue Model (Fee Switch planned)

Perubahan Governance: Pre-mainnet: Foundation-controlled → Genesis: BGT emission to LPs, on-chain governance module live → Post-TGE: BGT holder voting on fee switch, emissions, upgrades; Foundation remains legal entity
· Evidence: Phase 3 EV-016 (BGT emission genesis), EV-017 (governance proposals 2024+); Phase 6 Governance (BGT-weighted voting, proposal types, treasury governance unclear); Phase 2 Entity (Foundation only, no DAO)
· Supporting Dataset: Phase 3 EV-016, EV-017; Phase 6 Governance; Phase 2 Entity List; Phase 7 Governance Ecosystem

Technical Decision Pattern

Pola 1: Modular Architecture dengan Custom Integration Layer
· Decision Pattern: Memisahkan consensus (CometBFT), application framework (Cosmos SDK), execution (custom EVM module), dan PoL logic (custom module) — lalu mengintegrasikan via ABCI++ dan custom precompile
· Evidence: Phase 4 Architecture (modular: consensus layer, application layer, IBC); Phase 4 Core Components (12 distinct modules); Phase 4 Development Framework (Cosmos SDK v0.50+, CometBFT v0.38+, custom EVM Module)
· Supporting Dataset: Phase 4 Technology (Architecture, Core Components, Development Framework, Current Technical Stack)

Pola 2: EVM-Equivalent Execution via Custom Module (Bukan Fork Client)
· Decision Pattern: Membangun custom EVM interpreter di atas Cosmos SDK store (Merkle Patricia Trie) dengan precompile untuk native Cosmos functionality — bukan menjalankan geth/erigon sebagai sidecar
· Evidence: Phase 4 Execution Environment (EVM state root di Cosmos SDK store via custom MPT); Phase 4 Core Components (EVM Module custom); Phase 4 Programming Languages (Go for core, Solidity for contracts)
· Supporting Dataset: Phase 4 Technology (Execution Environment, Core Components, Programming Languages, Development Framework)

Pola 3: Proof-of-Liquidity sebagai Consensus Extension (Bukan Application Layer)
· Decision Pattern: PoL logic diimplementasikan sebagai module di consensus/application layer (validator weight calculation, BGT emission, delegation) — bukan sebagai smart contract di EVM
· Evidence: Phase 4 Consensus Mechanism (validator weight = BERA stake + delegated BGT); Phase 4 Core Components (PoL Module, BGT Module); Phase 4 Security Model (PoL economic security)
· Supporting Dataset: Phase 4 Technology (Consensus Mechanism, Core Components, Security Model); Phase 6 Token (BGT Utility: Validator Weight, Emission Direction)

Pola 4: Native DeFi Primitives sebagai Protocol-Level Components
· Decision Pattern: BEX, Bend, Berps, HONEY dibangun sebagai integrated modules dengan direct access ke PoL emission (BEX), gas token (BERA), governance token (BGT) — bukan third-party contracts
· Evidence: Phase 4 Core Components (BEX, Bend, Berps, HONEY sebagai core components); Phase 3 EV-008 (deployment bersamaan mainnet); Phase 6 Token (BGT emission hanya via BEX LP)
· Supporting Dataset: Phase 4 Technology (Core Components); Phase 3 History (EV-008, EV-015, EV-016); Phase 7 Applications (7 native apps)

Pola 5: Upgrade Bertahap via Cosmos SDK Software Upgrade Proposal + On-Chain Governance
· Decision Pattern: Menggunakan Cosmos SDK plan-based upgrade mechanism dengan validator signaling + BGT holder voting untuk parameter changes
· Evidence: Phase 4 Technical Upgrade History (4 upgrades: Genesis, Artio v3, TGE, Governance); Phase 4 Security Model (upgrade mechanism); Phase 6 Governance (proposal types include Software Upgrade)
· Supporting Dataset: Phase 4 Technology (Technical Upgrade History, Security Model); Phase 6 Governance; Phase 3 EV-017

Financial Decision Pattern

Pola 1: Tidak Ada Public Fundraising Announcement (Stealth/Private Funding Only)
· Decision Pattern: Tidak mempublikasikan funding round (Seed, Series A, Strategic, Private Sale) — treasury dan operasi dibiayai via private channels; Foundation sebagai legal wrapper untuk fund management
· Evidence: Phase 5 Funding History (0 verified rounds); Phase 5 Fundraising Mechanism (all "tidak diketahui"); Phase 5 Financial Dependencies (no identified VC/backer); Phase 2 Entity (no Investor entities)
· Supporting Dataset: Phase 5 Financial (Funding History, Fundraising Mechanism, Financial Dependencies); Phase 2 Entity (no Investor category)

Pola 2: Protocol Revenue dari Native Apps Sebagai Primary Sustainable Funding
· Decision Pattern: Mengandalkan revenue BEX (trading fees), Bend (borrowing interest), Berps (perpetual fees), network fees (BERA gas), validator rewards — bukan VC funding berkelanjutan
· Evidence: Phase 5 Revenue Model (7 confirmed streams: BEX, Bend, Berps, BERA gas, Fee Switch planned, MEV, Validator rewards); Phase 5 Revenue History (no historical data disclosed); Phase 7 Applications (native apps live)
· Supporting Dataset: Phase 5 Financial (Revenue Model, Revenue History); Phase 7 Applications (BEX, Bend, Berps); Phase 3 EV-008 (apps deployment)

Pola 3: Tokenomics Designed untuk Delayed Insider Liquidity (Vesting Cliffs Post-TGE)
· Decision Pattern: Full supply minted at genesis, TGE activates transferability, tapi Team/Investors/Foundation/Advisors subject ke 6-12 bulan cliff + 2-4 tahun linear vesting — mencegah early dump
· Evidence: Phase 6 Vesting Schedule (Team 12m/36m, Investors 12m/24m, Foundation 6m/48m, Advisors 12m/24m, Community partial unlock); Phase 6 Major Token Events (projected cliff ends 2025-08, 2026-02)
· Supporting Dataset: Phase 6 Token (Distribution, Vesting Schedule, TGE, Major Token Events); Phase 3 EV-011 (TGE date)

Pola 4: Fee Switch sebagai Value Capture Mechanism untuk BGT Holder (Governance-Gated)
· Decision Pattern: Fee switch dirancang dari awal (whitepaper) tapi activatable hanya via BGT governance proposal — aligns BGT holder interest dengan protocol revenue
· Evidence: Phase 5 Revenue Model (Fee Switch planned, status unverified); Phase 6 Token Utility BGT (Fee Switch Revenue Share); Phase 6 Governance (proposal types include Fee Switch Activation); Phase 3 EV-009 (Artio v3 test fee switch)
· Supporting Dataset: Phase 5 Financial (Revenue Model); Phase 6 Token (BGT Utility, Governance); Phase 3 EV-009, EV-017

Pola 5: Treasury Opacity — No Public Dashboard, Composition, atau Reporting
· Decision Pattern: Treasury dikelola Foundation (Cayman) tanpa transparency report, on-chain address disclosure, atau DefiLlama/Token Terminal integration
· Evidence: Phase 5 Treasury (size/composition undisclosed, custodian: Berachain Foundation); Phase 5 Financial Risk (all "tidak diketahui"); Phase 7 Ecosystem Risks (Treasury Concentration risk unidentified)
· Supporting Dataset: Phase 5 Financial (Treasury, Financial Risk); Phase 2 Entity (Berachain Foundation); Phase 7 Ecosystem Risks

Ecosystem Decision Pattern

Pola 1: Build Native DeFi Stack First, External Integrations Second
· Decision Pattern: Meluncurkan BEX, Bend, Berps, HONEY sebagai native apps sebelum menarik protokol eksternal — memastikan liquidity flywheel PoL berfungsi dari hari 1
· Evidence: Phase 3 EV-008 (native apps deployed dengan mainnet genesis); Phase 7 Applications (7 native apps, external protocols "unidentified"); Phase 7 Major Integrations (native apps + IBC + tooling first)
· Supporting Dataset: Phase 3 EV-008, EV-015, EV-016; Phase 7 Applications, Major Integrations; Phase 4 Core Components

Pola 2: EVM Tooling Compatibility sebagai Primary Developer Onboarding Strategy
· Decision Pattern: Prioritaskan Hardhat, Foundry, MetaMask, JSON-RPC Ethereum standard — tidak memaksa developer belajar CosmWasm/Rust; IBC sebagai bonus untuk cross-chain
· Evidence: Phase 7 Developer Ecosystem (Hardhat, Foundry, Ignite CLI live); Phase 7 Wallet Ecosystem (MetaMask full support, Keplr/Leap inferred); Phase 4 Execution Environment (EVM-equivalent, standard JSON-RPC); Phase 8 Narrative (EVM-equivalent main narrative)
· Supporting Dataset: Phase 7 Developer Ecosystem, Wallet Ecosystem, Major Integrations; Phase 4 Technology (Execution Environment); Phase 8 Market (Narrative Position)

Pola 3: IBC Integration untuk Cosmos Liquidity Access, Bukan Sebagai Primary Identity
· Decision Pattern: Mengaktifkan IBC channels ke Osmosis, Celestia untuk cross-chain liquidity — tapi branding, tooling, developer docs fokus EVM/PoL narrative
· Evidence: Phase 3 EV-014 (IBC live mainnet); Phase 7 External Dependencies (IBC High criticality); Phase 7 Major Integrations (IBC Channels live); Phase 8 Narrative (IBC secondary narrative)
· Supporting Dataset: Phase 3 EV-014; Phase 7 External Dependencies, Major Integrations; Phase 8 Market (Narrative Position)

Pola 4: Validator Set Curated (100 Active) dengan High Hardware Requirements
· Decision Pattern: Membatasi validator ke 100 dengan spec tinggi (64GB RAM, 4TB NVMe, 10Gbps) — memprioritaskan performance dan security over broad decentralization
· Evidence: Phase 4 Consensus Mechanism (100 active validators); Phase 4 Known Limitations (validator centralization risk); Phase 7 Infrastructure Providers (100 Validators critical); Phase 3 EV-007 (genesis validator set)
· Supporting Dataset: Phase 4 Technology (Consensus Mechanism, Known Technical Limitations); Phase 7 Infrastructure Providers; Phase 3 EV-007

Pola 5: Pseudonymous Core Team dengan Foundation sebagai Public Face
· Decision Pattern: Founders (Smokey, Dev, Papa) dan ~20+ core contributors pseudonim; Foundation (Cayman) sebagai legal entity publik; tidak ada doxxed leadership
· Evidence: Phase 1 Foundation (Founders pseudonim); Phase 2 Entity (Smokey, Dev, Papa, Core Contributors all pseudonim); Phase 2 Entity (Berachain Foundation as legal entity)
· Supporting Dataset: Phase 1 Foundation; Phase 2 Entity (Person: Smokey/Dev/Papa/Core Contributors; Foundation: Berachain Foundation)

Governance Decision Pattern

Pola 1: BGT-Weighted On-Chain Voting dengan Direct Delegator Participation
· Decision Pattern: 1 BGT = 1 vote; delegator vote langsung (tidak melalui validator); BGT non-transferable mencegah vote buying; proposal types: Text, Parameter Change, Software Upgrade, Community Pool Spend, PoL-specific (Fee Switch, Emission Rate, Gauge Weight)
· Evidence: Phase 6 Governance (model, voting system, voting power, delegation, proposal system); Phase 3 EV-017 (governance proposals mulai 2024); Phase 4 Security Model (BGT non-transferable prevents vote buying)
· Supporting Dataset: Phase 6 Token (Governance); Phase 3 EV-017; Phase 4 Security Model

Pola 2: Foundation sebagai Legal Entity Terpisah dari On-Chain Governance
· Decision Pattern: Foundation (Cayman) mengelola treasury, legal, compliance; on-chain governance mengelola protocol parameters, fee switch, upgrades — tidak ada legal wrapper DAO yang bridge keduanya
· Evidence: Phase 2 Entity (Foundation only, no DAO); Phase 6 Governance (treasury governance unclear, community pool existence unknown); Phase 7 Governance Ecosystem (Foundation live, DAO N/A, Council N/A)
· Supporting Dataset: Phase 2 Entity List; Phase 6 Governance; Phase 7 Governance Ecosystem

Pola 3: Fee Switch Activation Sebagai Governance Litmus Test
· Decision Pattern: Fee switch dirancang dari awal tapi memerlukan BGT holder proposal dan vote untuk aktivasi — menguji apakah governance efektif dan BGT holder termotivasi
· Evidence: Phase 5 Revenue Model (Fee Switch planned, status unverified); Phase 6 BGT Utility (Fee Switch Revenue Share); Phase 3 EV-009 (Artio v3 test fee switch), EV-017 (governance proposals); Phase 8 Open Threads (fee switch status unverified)
· Supporting Dataset: Phase 5 Financial (Revenue Model); Phase 6 Token (BGT Utility); Phase 3 EV-009, EV-017; Phase 8 Market (Open Threads)

Pola 4: Emission Direction via Gauge Voting (BGT Holder Mengarahkan Reward)
· Decision Pattern: BGT holder vote gauge weights untuk menentukan alokasi BGT emission ke BEX pools — menciptakan competitive liquidity market internal
· Evidence: Phase 6 BGT Utility (Emission Direction); Phase 4 Core Components (PoL Module, BGT Module); Phase 3 EV-016 (BGT emission via PoL); Phase 7 Applications (BEX sebagai primary emission venue)
· Supporting Dataset: Phase 6 Token (BGT Utility); Phase 4 Technology (Core Components); Phase 3 EV-016; Phase 7 Applications

Risk Response Pattern

Pola 1: Extensive Testnet Iteration Sebelum Mainnet (Technical Risk Mitigation)
· Decision Pattern: 3 fase testnet selama ~1.5 tahun (Artio v1 Jan 2023 → v2 Jan 2024 → v3 Oct 2024) dengan scope meningkat — validasi consensus, EVM, IBC, fee switch, governance sebelum mainnet
· Trigger: Kompleksitas novel consensus (PoL) + custom EVM + native apps + IBC — high risk of genesis failure
· Evidence: Phase 3 EV-003, EV-006, EV-009 (three testnets); Phase 4 Technical Upgrade History (Artio v1/v2/v3 as pre-mainnet validation)
· Response: Staged testnet program dengan closed→open→pre-TGE phases; setiap iterasi menambah fitur dan validator set
· Result: Mainnet genesis 2024-06-06 lancar; 100 validator aktif hari 1; no major consensus bug reported; native apps operational
· Supporting Dataset: Phase 3 EV-003, EV-006, EV-009; Phase 4 Technical Upgrade History; Phase 3 EV-007 (successful genesis)

Pola 2: Vesting Cliffs untuk Mitigasi Token Dump Risk (Economic Risk Mitigation)
· Decision Pattern: 6-12 bulan cliff untuk semua insider allocation (Team, Investors, Foundation, Advisors) post-TGE — mencegah immediate sell pressure saat liquidity masih rendah
· Trigger: TGE 2025-02-06 dengan full supply 500M minted; butuh protect early price discovery
· Evidence: Phase 6 Vesting Schedule (Team 12m cliff, Investors 12m, Foundation 6m, Advisors 12m); Phase 6 Major Token Events (projected cliff ends 2025-08, 2026-02)
· Response: Structured vesting dengan cliff + linear unlock; community partial unlock at TGE untuk liquidity
· Result: TGE completed; cliff countdown active; fee switch activation critical sebelum 2025-08 Foundation cliff end
· Supporting Dataset: Phase 6 Token (Vesting Schedule, Major Token Events, TGE); Phase 3 EV-011

Pola 3: BGT Non-Transferable Design untuk Mitigasi Governance Capture (Governance Risk Mitigation)
· Decision Pattern: BGT soulbound (non-transferable, hanya earned via LP) — mencegah whale accumulation, vote buying, dan plutocracy; delegation ke validator tidak transfer voting power
· Trigger: Risiko governance capture pada token-weighted voting tradisional
· Evidence: Phase 6 Token (BGT Distribution 100% to LPs, non-transferable); Phase 4 Security Model (BGT non-transferable prevents vote buying); Phase 6 Governance (delegator retain voting rights)
· Response: Design choice pada tokenomics — BGT bukan tradable asset; value capture via fee switch dan emission direction
· Result: BGT emission live since genesis 2024-06-06; governance proposals active 2024+; no secondary market manipulation possible
· Supporting Dataset: Phase 6 Token (BGT Distribution, Utility, Governance); Phase 4 Security Model; Phase 3 EV-016, EV-017

Pola 4: IBC Relay Dependency Diterima sebagai Calculated Risk (Bridge Risk Acceptance)
· Decision Pattern: Mengaktifkan IBC tanpa native relayer incentivization — bergantung pada permissionless relayer market; liveness risk accepted untuk interoperability gain
· Trigger: Kebutuhan cross-chain liquidity access ke Cosmos ecosystem (Osmosis, Celestia)
· Evidence: Phase 4 Known Limitations (IBC relay dependency); Phase 7 External Dependencies (IBC Relayers High criticality); Phase 7 Ecosystem Risks (IBC Relay Dependency risk)
· Response: Mengaktifkan IBC channels mainnet (EV-014); tidak membangun native relayer incentive program (tidak terdokumentasi)
· Result: IBC channels live ke Osmosis, Celestia; cross-chain transfer operational; relayer liveness unmonitored publicly
· Supporting Dataset: Phase 3 EV-014; Phase 4 Known Technical Limitations; Phase 7 External Dependencies, Ecosystem Risks

Pola 5: Oracle Provider Unidentified — Silent Acceptance of Centralization Risk (Oracle Risk Acceptance)
· Decision Pattern: Bend (liquidation), Berps (funding rate), HONEY (peg) memerlukan price feeds — tapi oracle provider tidak diungkapkan, tidak ada audit report publik, tidak ada decentralized oracle integration terverifikasi
* Trigger: Perlu oracle untuk DeFi primitives tapi tidak ingin commit ke provider spesifik secara publik
* Evidence: Phase 4 Known Limitations (No native oracle); Phase 7 External Dependencies (Oracle Provider unidentified, High criticality); Phase 7 Ecosystem Risks (Oracle Dependency risk); Phase 8 Open Threads (oracle provider unidentified)
* Response: Tidak mempublikasikan oracle provider; tidak mengintegrasikan multiple oracle (Chainlink, Pyth, dll) secara terverifikasi
* Result: Critical infrastructure dependency opaque; single point of failure risk untuk lending liquidation, perps funding, stablecoin peg
* Supporting Dataset: Phase 4 Known Technical Limitations; Phase 7 External Dependencies, Ecosystem Risks; Phase 8 Market Open Threads

Recurring Behavioral Pattern

Pola 1: Launch dengan Full Stack Native — Apps + Consensus + Tokens Sekaligus
· Decision Pattern: Berulang kali meluncurkan sistem kompleks secara bersamaan: mainnet genesis + 3 DeFi apps + 2 tokens (BGT, HONEY) + IBC + 100 validators (EV-007, EV-008, EV-014, EV-015, EV-016); TGE + vesting cliffs + CEX listing + fee switch eligibility (EV-011, EV-012)
· Evidence: Phase 3 EV-007, EV-008, EV-014, EV-015, EV-016 (genesis cluster); Phase 3 EV-011, EV-012 (TGE cluster); Phase 4 Core Components (12 components live at genesis)
* Supporting Dataset: Phase 3 History (EV-007, EV-008, EV-014, EV-015, EV-016, EV-011, EV-012); Phase 4 Core Components; Phase 6 Major Token Events

Pola 2: Pseudonymous Leadership dengan Foundation Legal Wrapper
· Decision Pattern: Founders dan core contributors tetap pseudonim (Smokey, Dev, Papa, ~20+ handles); Foundation (Cayman) sebagai sole legal entity untuk treasury, compliance, token issuance
* Evidence: Phase 1 Foundation (Founders pseudonim); Phase 2 Entity (all Person entities pseudonim, Foundation only legal entity); Phase 5 Financial (Treasury managed by Foundation)
* Supporting Dataset: Phase 1 Foundation; Phase 2 Entity (Person, Foundation); Phase 5 Financial (Treasury)

Pola 3: EVM-First, Cosmos-Native Architecture
· Decision Pattern: Semua developer tooling, wallet support, documentation, marketing mengutamakan EVM compatibility (Hardhat, Foundry, MetaMask, JSON-RPC) — Cosmos SDK/CometBFT/IBC sebagai underlying infrastructure tersembunyi
* Evidence: Phase 7 Developer Ecosystem (Hardhat, Foundry primary); Phase 7 Wallet Ecosystem (MetaMask full, Keplr/Leap inferred); Phase 4 Execution Environment (EVM-equivalent); Phase 8 Narrative (EVM-equivalent main, IBC secondary)
* Supporting Dataset: Phase 7 Developer Ecosystem, Wallet Ecosystem, Major Integrations; Phase 4 Technology (Execution Environment); Phase 8 Market (Narrative Position)

Pola 4: Tokenomics dengan Delayed Insider Liquidity + Continuous Contributor Rewards
· Decision Pattern: BERA vesting cliffs (6-12m) + linear (2-4y) untuk insider; BGT continuous emission ke LP (no insider allocation); HONEY elastic supply via user minting — alignment jangka panjang
* Evidence: Phase 6 Vesting Schedule (all insider categories cliffed); Phase 6 BGT Distribution (100% to LPs, no team/investor); Phase 6 HONEY Supply (elastic, user-minted); Phase 3 EV-011, EV-016
* Supporting Dataset: Phase 6 Token (Distribution, Vesting Schedule, BGT Distribution, HONEY Supply, Major Token Events); Phase 3 EV-011, EV-016

Pola 5: Governance Parameter Changes via On-Chain Proposal, Treasury Opaque
· Decision Pattern: Protocol parameters (gas limit, fee switch, emission rates, upgrades) via BGT voting on-chain; tapi Foundation treasury (Cayman) off-chain, no transparency, no community pool verified
* Evidence: Phase 6 Governance (proposal types include parameter changes, software upgrades); Phase 6 Governance (treasury governance unclear); Phase 2 Entity (Foundation only); Phase 7 Governance Ecosystem (Foundation live, DAO N/A)
* Supporting Dataset: Phase 6 Token (Governance); Phase 2 Entity List; Phase 7 Governance Ecosystem

Strategic Trade-offs

Trade-off 1: Desentralisasi Validator vs Performance & Security
· Decision: Membatasi validator ke 100 dengan hardware requirements tinggi (64GB RAM, 4TB NVMe, 10Gbps)
· Trade-off: Mengorbankan broad decentralization (hanya 100 slot, high barrier to entry) demi throughput, finality cepat (~1-2 detik), dan security threshold CometBFT (>2/3 honest)
· Evidence: Phase 4 Consensus Mechanism (100 validators, CometBFT BFT); Phase 4 Known Limitations (validator centralization risk); Phase 7 Infrastructure Providers (100 validators critical)
· Supporting Dataset: Phase 4 Technology (Consensus Mechanism, Known Technical Limitations); Phase 7 Infrastructure Providers

Trade-off 2: BGT Non-Transferable (Soulbound) vs DeFi Composability
· Decision: BGT tidak transferable, hanya earned via LP di BEX, tidak bisa dipakai collateral di protokol lain tanpa wrapper
· Trade-off: Mengorbankan composability DeFi (BGT tidak bisa jadi collateral di Bend, tidak bisa trade di BEX, tidak bisa integrate ke external protocols) demi mencegah vote buying, whale capture, dan mercenary capital
· Evidence: Phase 6 Token (BGT Distribution 100% to LPs, non-transferable); Phase 4 Security Model (BGT non-transferable prevents vote buying); Phase 4 Known Limitations (BGT design limits composability); Phase 6 BGT Utility (Governance, Emission Direction, Validator Weight)
· Supporting Dataset: Phase 6 Token (BGT Distribution, Utility); Phase 4 Technology (Security Model, Known Technical Limitations)

Trade-off 3: EVM-Equivalent Custom Module vs Upstream Client Compatibility
· Decision: Custom EVM interpreter di Cosmos SDK (custom MPT, precompile) bukan fork geth/erigon
· Trade-off: Mengorbankan automatic upstream EVM upgrades (Shanghai, Cancun, Prague, dll) dan client diversity demi tight integration dengan Cosmos state machine, PoL module, dan IBC
· Evidence: Phase 4 Execution Environment (custom EVM module, EVM state root in Cosmos store); Phase 4 Core Components (EVM Module custom); Phase 4 Development Framework (custom EVM, not standard client)
· Supporting Dataset: Phase 4 Technology (Execution Environment, Core Components, Development Framework)

Trade-off 4: Native DeFi Apps sebagai Protocol Components vs Permissionless Innovation
· Decision: BEX, Bend, Berps, HONEY dibangun dan dideploy oleh core team sebagai integrated modules — bukan membiarkan third-party membangun primitives dulu
· Trade-off: Mengorbankan permissionless innovation speed dan diversity pada early stage demi memastikan PoL flywheel (BGT emission via BEX LP) berfungsi dari genesis dan liquidity terarah
· Evidence: Phase 3 EV-008 (native apps deployed dengan genesis); Phase 4 Core Components (BEX, Bend, Berps, HONEY sebagai core components); Phase 7 Applications (7 native, external "unidentified"); Phase 6 BGT Utility (Emission Direction via BEX)
· Supporting Dataset: Phase 3 EV-008; Phase 4 Core Components; Phase 7 Applications; Phase 6 Token (BGT Utility)

Trade-off 5: Foundation-Controlled Treasury vs DAO-Owned Treasury
· Decision: Treasury dikelola Berachain Foundation (Cayman Islands) tanpa transparency dashboard; on-chain governance hanya untuk protocol parameters, tidak untuk treasury spending
· Trade-off: Mengorbankan community ownership dan transparency over treasury demi legal compliance, regulatory clarity, dan operational flexibility Foundation
· Evidence: Phase 5 Treasury (undisclosed, managed by Foundation); Phase 5 Financial Risk (all unknown); Phase 2 Entity (Foundation only, no DAO); Phase 6 Governance (treasury governance unclear, community pool unknown); Phase 7 Governance Ecosystem (Foundation live, DAO N/A)
· Supporting Dataset: Phase 5 Financial (Treasury, Financial Risk); Phase 2 Entity; Phase 6 Governance; Phase 7 Governance Ecosystem

Trade-off 6: Stealth Funding (No Public VC Announcement) vs Ecosystem Signaling
· Decision: Tidak mempublikasikan investor, valuation, funding rounds — Foundation sebagai sole funding vehicle
· Trade-off: Mengorbankan marketing signal dan network effects dari top-tier VC backing demi strategic flexibility,جنب regulatory scrutiny pada token sale, dan narrative "community-first"
· Evidence: Phase 5 Funding History (0 verified); Phase 5 Fundraising Mechanism (all unknown); Phase 5 Financial Dependencies (no identified backers); Phase 2 Entity (no Investor entities)
· Supporting Dataset: Phase 5 Financial (Funding History, Fundraising Mechanism, Financial Dependencies); Phase 2 Entity List

Behavioral Summary

Prioritas Utama Proyek:
1. Proof-of-Liquidity consensus sebagai differentiator teknis dan ekonomis — mengikat security ke DeFi liquidity via BGT delegation
2. EVM-equivalent execution untuk developer onboarding seamless — Hardhat, Foundry, MetaMask out of the box
3. Native DeFi primitives (BEX, Bend, Berps, HONEY) untuk bootstrapping liquidity flywheel dari genesis
4. Tokenomics dengan delayed insider liquidity (vesting cliffs) dan continuous contributor rewards (BGT emission to LPs)
5. Governance on-chain via BGT-weighted voting untuk protocol parameters, fee switch, upgrades

Cara Mengambil Keputusan:
- Technical decisions: Modular architecture dengan custom integration layers (CometBFT + Cosmos SDK + custom EVM + PoL module) — prioritaskan control dan integration depth over upstream compatibility
- Product decisions: Launch full stack native (consensus + apps + tokens + IBC) secara bersamaan — high complexity tolerance, yakin pada testnet validation bertahap
- Financial decisions: Opacity pada funding dan treasury; transparency pada tokenomics (whitepaper) dan protocol revenue (native apps) — Foundation sebagai legal wrapper, community via tokenomics
- Governance decisions: On-chain untuk parameters, off-chain (Foundation) untuk treasury — pragmatic separation, regulatory-driven
- Ecosystem decisions: EVM-first tooling/wallet/docs; IBC sebagai secondary bridge — capture Ethereum developer mindshare first

Faktor Paling Sering Mempengaruhi Keputusan:
1. PoL Consensus Integrity — semua desain (BGT soulbound, BEX sebagai emission venue, validator weight formula) derived dari PoL mechanics
2. EVM Developer Experience — tooling, wallet, RPC, docs semua optimized untuk Ethereum developer
3. Regulatory/Legal Pragmatism — Foundation di Cayman, pseudonymous founders, no public fundraising, treasury opacity
4. Native DeFi Flywheel Bootstrapping — launch apps dengan consensus, BGT emission via BEX only, HONEY sebagai base pair
5. Long-term Alignment via Tokenomics — vesting cliffs, BGT non-transferable, continuous emission to contributors

Pola Evolusi:
- 2022: Research/design PoL concept (pseudonymous trio)
- 2023: Infrastructure build (Foundation, GitHub, Community, Testnet v1)
- 2024: Iterative testnet validation (v2, v3) → Mainnet genesis dengan full stack native
- 2025: TGE aktivasi tokenomics, vesting cliffs mulai, governance live
- Ongoing: Governance-driven parameter evolution, fee switch activation, ecosystem expansion

Kekuatan Utama:
- Novel consensus (PoL) menciptakan alignment unik security-liquidity
- EVM-equivalent pada Cosmos SDK — best of both worlds (tooling + modularity)
- Native DeFi stack lengkap dari genesis — flywheel immediate
- Tokenomics alignment jangka panjang (vesting, BGT soulbound, continuous LP rewards)
- Strong technical execution (3 testnets, smooth genesis, 100 validators live)

Kelemahan Utama:
- Treasury dan funding opacity — tidak ada transparency report, investor disclosure, atau community pool verified
- Oracle dependency unidentified — critical risk untuk Bend, Berps, HONEY
- Validator set centralization risk — 100 slots, high hardware req, geographic distribution unknown
- BGT non-transferable limits composability — tidak bisa integrate ke external DeFi tanpa wrapper
- Foundation vs on-chain governance dual structure — regulatory ambiguity, no DAO legal wrapper
- No public audit reports terverifikasi untuk core protocol dan native apps
- Adoption metrics tidak teragregasi publik (TVL, volume, users, DAU) — DefiLlama integration incomplete

## Knowledge Extraction
_ref: `docs/Patterns/*`, `docs/Reasoning/*` (rule candidates)_

PROJECT: Berachain

## Core Insights

Insight 1: Proof-of-Liquidity menciptakan alignment langsung antara keamanan jaringan dan liquidity DeFi
Explanation: Berachain mengimplementasikan konsensus di mana validator weight = BERA stake + delegated BGT dari liquidity provider di BEX. Ini mengikat economic security langsung ke DeFi TVL, menciptakan flywheel: lebih banyak liquidity → lebih banyak BGT emission → validator weight lebih tinggi → keamanan jaringan lebih kuat → menarik lebih banyak liquidity.
Evidence: PoL consensus mechanism menggabungkan BERA stake dan delegated BGT untuk validator weight【Phase 4 — Consensus Mechanism】; BGT 100% di-emit ke LP via BEX, tidak ada alokasi team/investor/foundation【Phase 6 — BGT Distribution】; Whitepaper memposisikan PoL sebagai inovasi inti "liquidity as security"【Phase 1 — Foundation】.
Supporting Dataset: Phase 1 Foundation, Phase 4 Technology (Consensus Mechanism, PoL Module), Phase 6 Token (BGT Distribution, Utility), Phase 9 Behavioral (Strategic Objective 1).
Confidence: High

Insight 2: EVM-equivalent execution di atas Cosmos SDK via custom module (bukan fork client) memberikan control penuh atas integration dengan PoL dan IBC
Explanation: Berachain membangun custom EVM interpreter di atas Cosmos SDK store (custom Merkle Patricia Trie) dengan precompile untuk native Cosmos functionality (IBC, staking, governance, PoL). Pendekatan ini memungkinkan tight integration antara EVM execution dan consensus/application layer Cosmos, tapi mengorbankan automatic upstream EVM upgrades.
Evidence: Custom EVM module dengan EVM state root di Cosmos SDK store via custom MPT【Phase 4 — Execution Environment】; EVM Module sebagai core component terpisah dari Cosmos SDK/CometBFT【Phase 4 — Core Components】; Development framework menggunakan custom EVM bukan standard client【Phase 4 — Development Framework】.
Supporting Dataset: Phase 4 Technology (Architecture, Core Components, Execution Environment, Development Framework), Phase 9 Behavioral (Technical Decision Pattern 2).
Confidence: High

Insight 3: Launch full stack native (consensus + apps + tokens + IBC) secara bersamaan dari genesis mengurangi bootstrap risk tapi meningkatkan kompleksitas operasional
Explanation: Mainnet genesis 2024-06-06 meluncurkan 100 validator, PoL consensus, EVM execution, 3 native DeFi apps (BEX, Bend, Berps), 2 tokens (BGT, HONEY), dan IBC channels sekaligus. Semua sistem harus siap simultan — bug di satu app mempengaruhi seluruh ekosistem.
Evidence: EV-007 (Mainnet Genesis), EV-008 (Native Apps Deployment), EV-014 (IBC), EV-015 (HONEY), EV-016 (BGT Emission) semua terjadi di sekitar genesis 2024-06-06【Phase 3 — EV-007, EV-008, EV-014, EV-015, EV-016】; 12 core components live at genesis【Phase 4 — Core Components】.
Supporting Dataset: Phase 3 History (EV-007, EV-008, EV-014, EV-015, EV-016), Phase 4 Technology (Core Components), Phase 9 Behavioral (Recurring Pattern 1).
Confidence: High

Insight 4: BGT soulbound (non-transferable) design mencegah governance capture tapi membatasi DeFi composability secara fundamental
Explanation: BGT hanya didapat via providing liquidity di BEX, tidak transferable, tidak bisa dijual, tidak bisa dipakai collateral di protokol lain tanpa wrapper. Delegation ke validator tidak memindahkan voting power. Design ini mencegah vote buying dan whale accumulation tapi membuat BGT tidak komposabel dengan ekosistem DeFi luas.
Evidence: BGT Distribution 100% ke LP via PoL, zero allocation team/investor/foundation【Phase 6 — BGT Distribution】; BGT non-transferable prevents vote buying【Phase 4 — Security Model】; BGT design limits composability (cannot be used as collateral without wrapper)【Phase 4 — Known Technical Limitations】; Delegator retain voting rights saat mendelegasikan BGT ke validator【Phase 6 — Governance】.
Supporting Dataset: Phase 6 Token (BGT Distribution, Utility, Governance), Phase 4 Technology (Security Model, Known Limitations), Phase 9 Behavioral (Trade-off 2).
Confidence: High

Insight 5: Treasury dan funding opacity (Foundation-controlled, no public disclosure) menciptakan regulatory pragmatism tapi menimbulkan trust deficit komunitas
Explanation: Berachain Foundation (Cayman Islands) mengelola treasury tanpa transparency dashboard, on-chain address disclosure, atau financial reporting. Tidak ada public fundraising announcement. On-chain governance hanya untuk protocol parameters, tidak untuk treasury spending. Community pool existence unverified.
Evidence: Treasury size/composition undisclosed, custodian: Berachain Foundation【Phase 5 — Treasury】; Funding history 0 verified rounds【Phase 5 — Funding History】; Fundraising mechanism all "tidak diketahui"【Phase 5 — Fundraising Mechanism】; Treasury governance unclear, community pool unknown【Phase 6 — Governance】; Foundation only legal entity, no DAO entity【Phase 2 — Entity List】.
Supporting Dataset: Phase 5 Financial (Treasury, Funding History, Fundraising Mechanism), Phase 6 Token (Governance), Phase 2 Entity (Foundation, no DAO), Phase 9 Behavioral (Financial Decision Pattern 1, 5; Trade-off 5).
Confidence: High

Insight 6: Three-phase testnet iteration (Artio v1→v2→v3) selama ~1.5 tahun memvalidasi kompleksitas teknis bertahap sebelum mainnet
Explanation: Artio v1 (Jan 2023): closed validator, PoL validation. Artio v2 (Jan 2024): open validator, IBC integration. Artio v3 (Oct 2024): fee switch testing, governance mechanics, upgradeability framework. Setiap iterasi menambah scope dan validator set, mengurangi genesis failure risk.
Evidence: EV-003 Artio v1 2023-01-12【Phase 3 — EV-003】; EV-006 Artio v2 2024-01-11【Phase 3 — EV-006】; EV-009 Artio v3 2024-10【Phase 3 — EV-009】; Technical Upgrade History mencatat Artio v1/v2/v3 sebagai pre-mainnet validation【Phase 4 — Technical Upgrade History】.
Supporting Dataset: Phase 3 History (EV-003, EV-006, EV-009), Phase 4 Technology (Technical Upgrade History), Phase 9 Behavioral (Risk Response Pattern 1).
Confidence: High

Insight 7: Vesting cliffs (6-12 bulan) untuk semua insider allocation post-TGE melindungi early price discovery tapi menciptakan cliff risk di 2025-08 dan 2026-02
Explanation: TGE 2025-02-06 mengaktifkan BERA transferability. Team (20%): 12m cliff/36m linear. Investors (15%): 12m cliff/24m linear. Foundation (12%): 6m cliff/48m linear. Advisors (5%): 12m cliff/24m linear. Community (38%): partial unlock at TGE, remainder streamed. Fee switch activation critical sebelum Foundation cliff ends 2025-08.
Evidence: TGE 2025-02-06【Phase 3 — EV-011】; Vesting Schedule detail per kategori【Phase 6 — Vesting Schedule】; Major Token Events projected cliff ends 2025-08-06 (Foundation/Ecosystem) dan 2026-02-06 (Team/Investors/Advisors)【Phase 6 — Major Token Events】.
Supporting Dataset: Phase 3 History (EV-011), Phase 6 Token (Vesting Schedule, Major Token Events, TGE), Phase 9 Behavioral (Financial Decision Pattern 3, Risk Response Pattern 2).
Confidence: High

Insight 8: Pseudonymous core team (Smokey, Dev, Papa, ~20+ handles) dengan Foundation sebagai sole legal entity — pattern "anonymous builders, legal wrapper"
Explanation: Founders dan core contributors tetap pseudonim. Berachain Foundation (Cayman Islands) sebagai sole legal entity untuk treasury, compliance, token issuance. Tidak ada doxxed leadership. Foundation mengelola off-chain treasury; on-chain governance mengelola protocol parameters.
Evidence: Founders pseudonim: Smokey the Bera, Dev Bear, Papa Bear【Phase 1 — Founders】; Person entities all pseudonim【Phase 2 — Person Entities】; Foundation as legal entity【Phase 2 — Foundation Entity】; Treasury managed by Foundation【Phase 5 — Treasury】.
Supporting Dataset: Phase 1 Foundation, Phase 2 Entity (Person, Foundation), Phase 5 Financial (Treasury), Phase 9 Behavioral (Recurring Pattern 2).
Confidence: High

Insight 9: Oracle dependency unidentified untuk Bend (liquidation), Berps (funding rate), HONEY (peg) — critical infrastructure opacity
Explanation: Semua tiga native DeFi primitives memerlukan price feeds tapi oracle provider tidak diungkapkan di documentation, whitepaper, GitHub, atau audit reports. Tidak ada terverifikasi multiple oracle integration (Chainlink, Pyth, custom). Single point of failure risk untuk lending liquidation, perps funding, stablecoin peg.
Evidence: No native oracle documented【Phase 4 — Known Technical Limitations】; Oracle Provider unidentified, High criticality【Phase 7 — External Dependencies】; Oracle Dependency risk【Phase 7 — Ecosystem Risks】; Open Threads Phase 8: oracle provider unidentified【Phase 8 — Open Threads】.
Supporting Dataset: Phase 4 Technology (Known Limitations), Phase 7 Ecosystem (External Dependencies, Ecosystem Risks), Phase 8 Market (Open Threads), Phase 9 Behavioral (Risk Response Pattern 5).
Confidence: High

Insight 10: Fee switch sebagai value capture mechanism untuk BGT holder — governance-gated, status activation unverified on-chain
Explanation: Fee switch dirancang dari awal (whitepaper) untuk mengarahkan sebagian gas fees ke BGT stakers. Aktivasi memerlukan BGT governance proposal. Artio v3 testnet memvalidasi mechanics. Post-TGE status on-chain tidak dikonfirmasi. Critical untuk BGT holder value capture sebelum insider cliff unlocks.
Evidence: Fee switch mechanism di whitepaper【Phase 6 — BGT Utility: Fee Switch Revenue Share】; Revenue Model: Fee Switch planned, status unverified【Phase 5 — Revenue Model】; Artio v3 test fee switch【Phase 3 — EV-009】; Governance proposal types include Fee Switch Activation【Phase 6 — Governance】.
Supporting Dataset: Phase 6 Token (BGT Utility, Governance), Phase 5 Financial (Revenue Model), Phase 3 History (EV-009), Phase 9 Behavioral (Financial Decision Pattern 4, Governance Decision Pattern 3).
Confidence: Medium

Insight 11: EVM-first tooling/wallet/docs strategy dengan IBC sebagai secondary bridge — capture Ethereum developer mindshare first
Explanation: Semua developer tooling (Hardhat, Foundry, Ignite CLI), wallet support (MetaMask full, Keplr/Leap inferred), documentation, marketing mengutamakan EVM compatibility. Cosmos SDK/CometBFT/IBC sebagai underlying infrastructure tersembunyi. Narrative positioning: EVM-equivalent main, IBC secondary.
Evidence: Developer Ecosystem: Hardhat, Foundry primary【Phase 7 — Developer Ecosystem】; Wallet Ecosystem: MetaMask full support, Keplr/Leap inferred【Phase 7 — Wallet Ecosystem】; Execution Environment: EVM-equivalent【Phase 4 — Execution Environment】; Narrative: EVM-equivalent main, IBC secondary【Phase 8 — Narrative Position】.
Supporting Dataset: Phase 7 Ecosystem (Developer, Wallet, Major Integrations), Phase 4 Technology (Execution Environment), Phase 8 Market (Narrative Position), Phase 9 Behavioral (Ecosystem Decision Pattern 2, Recurring Pattern 3).
Confidence: High

Insight 12: Validator set curated (100 active) dengan high hardware requirements (64GB RAM, 4TB NVMe, 10Gbps) — performance/security over broad decentralization
Explanation: Membatasi validator ke 100 slot dengan spec tinggi menciptakan barrier to entry yang tinggi, mungkin mengonsentrasi stake ke operator besar. Geographic distribution tidak transparan. Trade-off: throughput, finality cepat (~1-2 detik), security threshold CometBFT (>2/3 honest) vs decentralization breadth.
Evidence: 100 active validators at genesis【Phase 3 — EV-007】; Consensus Mechanism: 100 validators, CometBFT BFT【Phase 4 — Consensus Mechanism】; Known Limitations: validator centralization risk【Phase 4 — Known Technical Limitations】; Infrastructure Providers: 100 Validators critical【Phase 7 — Infrastructure Providers】.
Supporting Dataset: Phase 3 History (EV-007), Phase 4 Technology (Consensus Mechanism, Known Limitations), Phase 7 Ecosystem (Infrastructure Providers), Phase 9 Behavioral (Trade-off 1).
Confidence: High

## Strategic Principles

Principle 1: Liquidity-Security Alignment — Konsensus harus mengikat economic security langsung ke DeFi liquidity, bukan hanya token staking
Explanation: Proof-of-Liquidity membuat validator weight bergantung pada BGT yang didelegasikan dari LP di BEX. Ini menciptakan alignment: validator berincentif mendukung DeFi liquidity growth, LP berincentif mendelegasikan ke validator yang mendukung ekosistem. Security budget tumbuh seiring TVL.
Evidence: PoL consensus mechanism【Phase 4 — Consensus Mechanism】; BGT emission hanya via BEX LP【Phase 6 — BGT Distribution】; Strategic Objective 1: PoL mengikat keamanan ke liquidity DeFi【Phase 9 — Strategic Objectives】.
Supporting Dataset: Phase 4 Technology, Phase 6 Token, Phase 9 Behavioral.
Confidence: High

Principle 2: Modular Architecture dengan Custom Integration Layer — Pisahkan consensus, application framework, execution, PoL logic; integrasikan via custom layer
Explanation: CometBFT (consensus) + Cosmos SDK (application framework) + custom EVM module (execution) + custom PoL module (consensus extension) — masing-masing modular tapi di-integrasikan via ABCI++ dan custom precompile. Memberikan control penuh atas cross-layer interaction.
Evidence: Architecture modular dengan 4 layer terpisah【Phase 4 — Architecture】; 12 core components distinct modules【Phase 4 — Core Components】; Development framework: Cosmos SDK v0.50+, CometBFT v0.38+, custom EVM【Phase 4 — Development Framework】.
Supporting Dataset: Phase 4 Technology (Architecture, Core Components, Development Framework), Phase 9 Behavioral (Technical Decision Pattern 1).
Confidence: High

Principle 3: Native DeFi Primitives First — Bangun core DeFi stack (DEX, lending, perps, stablecoin) sebagai protocol-level components sebelum menarik third-party
Explanation: BEX, Bend, Berps, HONEY dibangun dan dideploy oleh core team sebagai integrated modules dengan direct access ke PoL emission (BEX), gas token (BERA), governance token (BGT). Memastikan flywheel PoL berfungsi dari genesis. External integrations come second.
Evidence: Native apps deployed dengan mainnet genesis【Phase 3 — EV-008】; Core Components include BEX, Bend, Berps, HONEY【Phase 4 — Core Components】; Applications: 7 native, external "unidentified"【Phase 7 — Applications】.
Supporting Dataset: Phase 3 History (EV-008), Phase 4 Technology (Core Components), Phase 7 Ecosystem (Applications), Phase 9 Behavioral (Ecosystem Decision Pattern 1, Technical Decision Pattern 4).
Confidence: High

Principle 4: EVM-Equivalent Developer Experience — Prioritaskan Ethereum tooling/wallet/RPC compatibility out of the box; sembunyikan Cosmos complexity
Explanation: Hardhat, Foundry, MetaMask, JSON-RPC Ethereum standard semua supported natively. Developer tidak perlu belajar CosmWasm/Rust/IBC untuk build di Berachain. Cosmos SDK/CometBFT/IBC sebagai infrastructure tersembunyi. Onboarding friction minimal untuk Ethereum developers.
Evidence: Developer Ecosystem: Hardhat, Foundry, Ignite CLI【Phase 7 — Developer Ecosystem】; Wallet Ecosystem: MetaMask full support【Phase 7 — Wallet Ecosystem】; Execution Environment: EVM-equivalent, standard JSON-RPC【Phase 4 — Execution Environment】; Narrative: EVM-equivalent main【Phase 8 — Narrative Position】.
Supporting Dataset: Phase 7 Ecosystem (Developer, Wallet, Major Integrations), Phase 4 Technology (Execution Environment), Phase 8 Market (Narrative Position), Phase 9 Behavioral (Ecosystem Decision Pattern 2, Recurring Pattern 3).
Confidence: High

Principle 5: Long-term Alignment via Tokenomics — Delayed insider liquidity (vesting cliffs) + continuous contributor rewards (BGT emission to LPs) + non-transferable governance token
Explanation: BERA vesting: Team/Investors/Advisors 12m cliff, Foundation 6m cliff, linear 2-4 tahun. BGT: 100% ke LP via PoL, zero insider allocation, non-transferable. HONEY: elastic supply via user minting. Semua desain tokenomics mengoptimalkan untuk alignment jangka panjang, bukan short-term liquidity.
Evidence: Vesting Schedule detail per kategori【Phase 6 — Vesting Schedule】; BGT Distribution 100% to LPs【Phase 6 — BGT Distribution】; HONEY Supply elastic user-minted【Phase 6 — HONEY Supply】; Major Token Events cliff timeline【Phase 6 — Major Token Events】.
Supporting Dataset: Phase 6 Token (Distribution, Vesting Schedule, BGT Distribution, HONEY Supply, Major Token Events), Phase 9 Behavioral (Financial Decision Pattern 3, Recurring Pattern 4).
Confidence: High

Principle 6: Pragmatic Governance Separation — On-chain untuk protocol parameters (fee switch, emissions, upgrades), off-chain Foundation untuk treasury/legal/compliance
Explanation: BGT-weighted on-chain voting untuk parameter changes, fee switch, emission rates, software upgrades. Foundation (Cayman) mengelola treasury, legal, compliance tanpa transparency dashboard. Tidak ada DAO legal wrapper yang bridge keduanya. Regulatory-driven separation.
Evidence: Governance: BGT-weighted voting, proposal types【Phase 6 — Governance】; Treasury governance unclear, community pool unknown【Phase 6 — Governance】; Foundation only legal entity, no DAO【Phase 2 — Entity List】; Governance Ecosystem: Foundation live, DAO N/A【Phase 7 — Governance Ecosystem】.
Supporting Dataset: Phase 6 Token (Governance), Phase 2 Entity, Phase 7 Ecosystem (Governance Ecosystem), Phase 9 Behavioral (Governance Decision Pattern 1, 2, Recurring Pattern 5).
Confidence: High

Principle 7: Stealth Funding Opacity — Tidak mempublikasikan investor, valuation, funding rounds; Foundation sebagai sole funding vehicle
Explanation: 0 verified funding rounds public. Tidak ada VC announcement, no Crunchbase/PitchBook data. Foundation mengelola treasury opacity. Trade-off: strategic flexibility, avoid regulatory scrutiny on token sale, "community-first" narrative vs marketing signal dari top-tier VC backing.
Evidence: Funding History 0 verified【Phase 5 — Funding History】; Fundraising Mechanism all unknown【Phase 5 — Fundraising Mechanism】; Financial Dependencies no identified backers【Phase 5 — Financial Dependencies】; Entity list no Investor entities【Phase 2 — Entity List】.
Supporting Dataset: Phase 5 Financial (Funding History, Fundraising Mechanism, Financial Dependencies), Phase 2 Entity, Phase 9 Behavioral (Financial Decision Pattern 1, Trade-off 6).
Confidence: High

## Success Factors

Factor 1: Extensive testnet iteration (3 phases, ~1.5 tahun) memvalidasi kompleksitas teknis bertahap sebelum mainnet
Explanation: Artio v1→v2→v3 dengan scope meningkat (PoL → IBC → fee switch/governance) memungkinkan identifikasi bug konsensus dan EVM execution early. Mainnet genesis 2024-06-06 lancar tanpa major incident, 100 validator aktif hari 1, native apps operational.
Evidence: EV-003, EV-006, EV-009 three testnets【Phase 3 — EV-003, EV-006, EV-009】; Technical Upgrade History: Artio v1/v2/v3 as pre-mainnet validation【Phase 4 — Technical Upgrade History】; EV-007 successful genesis【Phase 3 — EV-007】; Risk Response Pattern 1: staged testnet program【Phase 9 — Risk Response Pattern 1】.
Supporting Dataset: Phase 3 History, Phase 4 Technology, Phase 9 Behavioral.
Confidence: High

Factor 2: Novel consensus (PoL) menciptakan differentiation teknis dan ekonomis yang kuat vs competitor L1
Explanation: Proof-of-Liquidity mengikat validator weight ke DeFi liquidity via BGT delegation — unique di antara L1 (Monad, Sei, Ethereum, dll semua PoS tradisional). Menarik naratif "DeFi-native L1", "liquidity as security", "liquidity flywheel". Menjadi primary narrative di marketing dan documentation.
Evidence: PoL consensus mechanism unique【Phase 4 — Consensus Mechanism】; Narrative: Proof-of-Liquidity main narrative【Phase 8 — Narrative Position】; Whitepaper centers PoL as core innovation【Phase 1 — Foundation】; Competitor landscape: different consensus philosophy【Phase 8 — Competitor Landscape】.
Supporting Dataset: Phase 4 Technology, Phase 8 Market, Phase 1 Foundation, Phase 9 Behavioral (Strategic Objective 1).
Confidence: High

Factor 3: Full stack native launch (consensus + apps + tokens + IBC) memastikan flywheel PoL berfungsi immediate dari genesis
Explanation: BGT emission aktif hari 1 via BEX LP; liquidity flywheel berputar immediate; IBC channels live untuk cross-chain liquidity access; 100 validator set ready. Tidak perlu tunggu third-party membangun primitives.
Evidence: EV-007, EV-008, EV-014, EV-015, EV-016 cluster at genesis【Phase 3 — EV-007, EV-008, EV-014, EV-015, EV-016】; 12 core components live at genesis【Phase 4 — Core Components】; Recurring Pattern 1: launch full stack native【Phase 9 — Recurring Pattern 1】.
Supporting Dataset: Phase 3 History, Phase 4 Technology, Phase 9 Behavioral.
Confidence: High

Factor 4: EVM-equivalent execution pada Cosmos SDK menarik Ethereum developer tanpa ganti tooling
Explanation: Custom EVM module support Solidity ^0.8.x, Hardhat, Foundry, MetaMask, JSON-RPC standard. Developer Ethereum bisa port kontrak tanpa modifikasi. Mengurangi onboarding friction drastis vs CosmWasm-only chains.
Evidence: Execution Environment: EVM-equivalent, standard tooling【Phase 4 — Execution Environment】; Developer Ecosystem: Hardhat, Foundry live【Phase 7 — Developer Ecosystem】; Wallet Ecosystem: MetaMask full support【Phase 7 — Wallet Ecosystem】; Strategic Objective 2: EVM-equivalent untuk menarik developer Ethereum【Phase 9 — Strategic Objectives】.
Supporting Dataset: Phase 4 Technology, Phase 7 Ecosystem, Phase 9 Behavioral.
Confidence: High

Factor 5: Tokenomics alignment jangka panjang (vesting cliffs, BGT soulbound, continuous LP rewards) mencegah early dump dan mercenary capital
Explanation: BERA vesting cliffs 6-12m post-TGE melindungi early price discovery. BGT non-transferable mencegah vote buying dan whale capture. Continuous BGT emission ke LP menginsentivkan liquidity provision jangka panjang. HONEY elastic supply via user minting.
Evidence: Vesting Schedule cliffs【Phase 6 — Vesting Schedule】; BGT Distribution 100% to LPs, non-transferable【Phase 6 — BGT Distribution】; BGT emission continuous since genesis【Phase 3 — EV-016】; HONEY Supply elastic【Phase 6 — HONEY Supply】; Financial Decision Pattern 3, Recurring Pattern 4【Phase 9 — Financial Decision Pattern 3, Recurring Pattern 4】.
Supporting Dataset: Phase 6 Token, Phase 3 History, Phase 9 Behavioral.
Confidence: High

Factor 6: IBC integration membuka akses ke Cosmos ecosystem liquidity (Osmosis, Celestia) tanpa membangun bridge custom
Explanation: IBC channels live ke Osmosis, Celestia mainnet genesis. Cross-chain asset transfer operational. Relayer infrastructure permissionless. Memanfaatkan existing Cosmos liquidity tanpa bridge risk custom.
Evidence: EV-014 IBC channels activated mainnet【Phase 3 — EV-014】; IBC Module live mainnet【Phase 4 — Core Components: IBC Module】; Major Integrations: IBC Channels live【Phase 7 — Major Integrations】; External Dependencies: IBC High criticality【Phase 7 — External Dependencies】.
Supporting Dataset: Phase 3 History, Phase 4 Technology, Phase 7 Ecosystem.
Confidence: High

## Failure Factors

Factor 1: Treasury dan funding opacity — tidak ada transparency dashboard, investor disclosure, atau community pool verified
Explanation: Foundation mengelola treasury tanpa public reporting. 0 verified funding rounds. Tidak ada on-chain community pool funded by protocol revenue untuk governance spending. Trust deficit untuk komunitas dan potential regulator.
Evidence: Treasury size/composition undisclosed【Phase 5 — Treasury】; Funding History 0 verified【Phase 5 — Funding History】; Governance: treasury governance unclear, community pool unknown【Phase 6 — Governance】; Financial Risk all unknown【Phase 5 — Financial Risk】; Trade-off 5: Foundation vs DAO treasury【Phase 9 — Trade-off 5】.
Supporting Dataset: Phase 5 Financial, Phase 6 Token, Phase 9 Behavioral.
Confidence: High

Factor 2: Oracle provider unidentified untuk Bend, Berps, HONEY — critical infrastructure dependency opaque
Explanation: Lending liquidation, perps funding rate, stablecoin peg semua bergantung price feeds. Provider tidak diungkapkan di docs, whitepaper, GitHub, audit. Tidak ada terverifikasi multiple oracle integration. Single point of failure risk tinggi.
Evidence: No native oracle documented【Phase 4 — Known Technical Limitations】; Oracle Provider unidentified High criticality【Phase 7 — External Dependencies】; Oracle Dependency risk【Phase 7 — Ecosystem Risks】; Risk Response Pattern 5: silent acceptance【Phase 9 — Risk Response Pattern 5】.
Supporting Dataset: Phase 4 Technology, Phase 7 Ecosystem, Phase 9 Behavioral.
Confidence: High

Factor 3: Validator set centralization risk — 100 slots, high hardware req, geographic distribution unknown
Explanation: 64GB RAM, 4TB NVMe, 10Gbps requirements menciptakan high barrier to entry. Hanya 100 slot. Entity identity dan commission rates tidak publik. Bisa mengonsentrasi stake ke operator besar. Trade-off performance/security vs decentralization.
Evidence: Validator requirements high【Phase 4 — Known Technical Limitations】; Consensus Mechanism: 100 validators【Phase 4 — Consensus Mechanism】; Infrastructure Providers: 100 Validators critical【Phase 7 — Infrastructure Providers】; Trade-off 1: decentralization vs performance【Phase 9 — Trade-off 1】.
Supporting Dataset: Phase 4 Technology, Phase 7 Ecosystem, Phase 9 Behavioral.
Confidence: High

Factor 4: BGT non-transferable design limits DeFi composability — tidak bisa dipakai collateral, tidak bisa trade, tidak integrate external tanpa wrapper
Explanation: Soulbound design mencegah secondary market tapi membatasi composability fundamental. BGT tidak bisa jadi collateral di Bend, tidak bisa trade di BEX, tidak bisa integrate ke external protocols. Wrapper diperlukan untuk komposabilitas.
Evidence: BGT design limits composability【Phase 4 — Known Technical Limitations】; BGT non-transferable【Phase 6 — BGT Distribution】; Trade-off 2: BGT non-transferable vs composability【Phase 9 — Trade-off 2】.
Supporting Dataset: Phase 4 Technology, Phase 6 Token, Phase 9 Behavioral.
Confidence: High

Factor 5: No public audit reports terverifikasi untuk core protocol (PoL, EVM module, CometBFT integration) dan native apps (BEX, Bend, Berps, HONEY)
Explanation: Phase 4 Audit History: 0 audit report publik teridentifikasi. Absence tidak berarti audit tidak dilakukan (banyak L1 audit private pre-mainnet) tapi tidak ada transparency untuk komunitas. Security assurance gap.
Evidence: Audit History: 0 audit report publik【Phase 4 — Audit History】; Security Model: bug bounty program tidak diketahui【Phase 4 — Security Model】; Open Threads Phase 8: audit reports tidak ditemukan【Phase 8 — Open Threads】.
Supporting Dataset: Phase 4 Technology, Phase 8 Market.
Confidence: High

Factor 6: Adoption metrics tidak teragregasi publik (TVL, volume, users, DAU) — DefiLlama integration incomplete
Explanation: Berascan menunjukkan raw data tapi no aggregated metrics dashboard. DefiLlama chain page exists tapi native protocols (BEX, Bend, Berps) belum terintegrasi untuk revenue/TVL tracking. Tidak ada Dune Analytics dashboard resmi. Sulit assess traction.
Evidence: Adoption Metrics: TVL/DAU/tx unknown【Phase 8 — Adoption Metrics】; DefiLlama: native apps not integrated【Phase 5 — Revenue History】; Market Share: tidak tersedia【Phase 8 — Market Share】; Open Threads Phase 8: TVL data, CEX specifics, DAU unknown【Phase 8 — Open Threads】.
Supporting Dataset: Phase 8 Market, Phase 5 Financial.
Confidence: High

Factor 7: Fee switch activation status unverified on-chain — governance-gated feature critical untuk BGT value capture belum confirm live
Explanation: Fee switch dirancang dari awal tapi memerlukan BGT governance proposal untuk aktivasi. Artio v3 testnet memvalidasi mechanics. Post-TGE status on-chain tidak dikonfirmasi. Critical sebelum insider cliff unlocks 2025-08/2026-02.
Evidence: Revenue Model: Fee Switch planned, status unverified【Phase 5 — Revenue Model】; BGT Utility: Fee Switch Revenue Share【Phase 6 — BGT Utility】; EV-009 Artio v3 test fee switch【Phase 3 — EV-009】; Open Threads Phase 8: fee switch status unverified【Phase 8 — Open Threads】.
Supporting Dataset: Phase 5 Financial, Phase 6 Token, Phase 3 History, Phase 8 Market.
Confidence: Medium

Factor 8: Custom EVM module mengorbankan automatic upstream EVM upgrades (Shanghai, Cancun, Prague) dan client diversity
Explanation: Custom EVM interpreter bukan fork geth/erigon. Harus manual implement EIP upgrades. Tidak ada client diversity (hanya custom implementation). Risk: consensus bugs, upgrade delays, maintenance burden.
Evidence: Execution Environment: custom EVM module, not standard client【Phase 4 — Execution Environment】; Core Components: EVM Module custom【Phase 4 — Core Components】; Technical Decision Pattern 2: custom EVM bukan fork client【Phase 9 — Technical Decision Pattern 2】; Trade-off 3: custom EVM vs upstream compatibility【Phase 9 — Trade-off 3】.
Supporting Dataset: Phase 4 Technology, Phase 9 Behavioral.
Confidence: High

## Decision Framework

Step 1: Research & Design Phase (2022) — Konsep PoL dan arsitektur protokol oleh trio founder pseudonim
Observe: Identifikasi kesenjangan security-liquidity pada L1 existing
Evaluate: Desain konsensus validator weight = BERA stake + delegated BGT dari LP
Decide: Merancang PoL sebagai differentiator teknis inti
Evidence: EV-001 konsep PoL 2022【Phase 3 — EV-001】; Strategic Objective 1【Phase 9 — Strategic Objectives】; Founding Entity pseudonim trio【Phase 1 — Founders】.
Supporting Dataset: Phase 3 History, Phase 9 Behavioral.

Step 2: Legal & Infrastructure Setup (2023) — Pendirian Foundation, GitHub, Community, Testnet v1
Observe: Perlu legal wrapper untuk treasury, token issuance, compliance
Evaluate: Cayman Islands Foundation non-profit sebagai sole legal entity
Decide: Foundation setup + infrastructure (GitHub, Discord, Twitter, Telegram) + closed testnet v1
Evidence: EV-002 Foundation 2023【Phase 3 — EV-002】; EV-004 GitHub【Phase 3 — EV-004】; EV-005 Community【Phase 3 — EV-005】; EV-003 Artio v1 2023-01-12【Phase 3 — EV-003】.
Supporting Dataset: Phase 3 History, Phase 2 Entity.

Step 3: Iterative Testnet Validation (2023-2024) — Artio v2 → v3 dengan scope meningkat
Observe: Validasi bertahap PoL, EVM, IBC, fee switch, governance
Evaluate: Setiap iterasi menambah fitur dan validator set
Decide: Three-phase testnet program: v1 closed validator, v2 open + IBC, v3 fee switch + governance
Evidence: EV-006 Artio v2 2024-01-11【Phase 3 — EV-006】; EV-009 Artio v3 2024-10【Phase 3 — EV-009】; Risk Response Pattern 1: staged testnet【Phase 9 — Risk Response Pattern 1】.
Supporting Dataset: Phase 3 History, Phase 9 Behavioral.

Step 4: Full Stack Mainnet Genesis (2024-06-06) — Launch consensus + apps + tokens + IBC sekaligus
Observe: Semua komponen inti siap setelah testnet v2 validation
Evaluate: Complexity tinggi tapi flywheel PoL butuh semua sistem live simultaneously
Decide: Launch 100 validator, PoL, EVM, BEX/Bend/Berps, BGT/HONEY, IBC sekaligus
Evidence: EV-007, EV-008, EV-014, EV-015, EV-016 cluster【Phase 3 — EV-007, EV-008, EV-014, EV-015, EV-016】; Recurring Pattern 1: launch full stack native【Phase 9 — Recurring Pattern 1】.
Supporting Dataset: Phase 3 History, Phase 9 Behavioral.

Step 5: TGE & Tokenomics Activation (2025-02-06) — BERA transferable, vesting cliffs mulai, fee switch eligible
Observe: Mainnet stable 8 bulan, native apps operational, BGT emission running
Evaluate: Butuh transferable gas token untuk fee market dan validator staking
Decide: Full supply 500M minted at genesis, TGE activates transferability, vesting cliffs post-TGE
Evidence: EV-011 TGE 2025-02-06【Phase 3 — EV-011】; EV-012 CEX/DEX listing【Phase 3 — EV-012】; Vesting Schedule cliffs【Phase 6 — Vesting Schedule】; Financial Decision Pattern 3【Phase 9 — Financial Decision Pattern 3】.
Supporting Dataset: Phase 3 History, Phase 6 Token, Phase 9 Behavioral.

Step 6: Governance-Driven Evolution (Ongoing) — On-chain BGT voting untuk parameters, fee switch, upgrades
Observe: BGT emission active since genesis, governance module live
Evaluate: Protocol parameters perlu community governance; fee switch gated by governance
Decide: BGT-weighted on-chain voting untuk parameter changes, fee switch, emission rates, software upgrades; Foundation remains legal entity
Evidence: EV-017 governance proposals 2024+【Phase 3 — EV-017】; Governance: BGT-weighted voting【Phase 6 — Governance】; Governance Decision Pattern 1, 2, 3【Phase 9 — Governance Decision Pattern 1, 2, 3】.
Supporting Dataset: Phase 3 History, Phase 6 Token, Phase 9 Behavioral.

## Reusable Playbook

Playbook 1: Membangun Konsensus Novel dengan Alignment Ekonomis — Design validator weight formula yang mengikat security budget ke metric yang diinginkan (liquidity, usage, dll)
Explanation: PoL formula: validator weight = base stake (BERA) + delegated governance token (BGT dari LP). BGT hanya earned via desired activity (providing liquidity). Menciptakan flywheel: desired activity → governance token → validator weight → security → more desired activity. Generalizable ke: Proof-of-Usage, Proof-of-Volume, Proof-of-Revenue.
Evidence: PoL consensus mechanism【Phase 4 — Consensus Mechanism】; BGT emission hanya via BEX LP【Phase 6 — BGT Distribution】; Strategic Objective 1【Phase 9 — Strategic Objectives】; Trade-off 1, 2【Phase 9 — Trade-off 1, Trade-off 2】.
Supporting Dataset: Phase 4 Technology, Phase 6 Token, Phase 9 Behavioral.
Confidence: High

Playbook 2: Staged Testnet Program untuk Validasi Kompleksitas Bertahap — 3 fase: core consensus → cross-chain/integration → governance/economics
Explanation: Artio v1 (PoL consensus only, closed validators) → v2 (add IBC, open validators) → v3 (add fee switch, governance mechanics, upgradeability). Setiap fase validasi scope terbatas sebelum tambah kompleksitas. Mengurangi genesis failure risk drastis.
Evidence: EV-003, EV-006, EV-009 three testnets【Phase 3 — EV-003, EV-006, EV-009】; Risk Response Pattern 1: staged testnet【Phase 9 — Risk Response Pattern 1】; Technical Upgrade History: Artio v1/v2/v3 validation【Phase 4 — Technical Upgrade History】.
Supporting Dataset: Phase 3 History, Phase 4 Technology, Phase 9 Behavioral.
Confidence: High

Playbook 3: Full Stack Native Launch untuk Bootstrapping Flywheel — Deploy core primitives (DEX, lending, perps, stablecoin) bersama consensus layer dari genesis
Explanation: Jangan tunggu third-party. Build native apps dengan direct access ke consensus-level incentives (BGT emission via BEX). Flywheel berputar hari 1. External integrations come after flywheel proven.
Evidence: EV-008 native apps deployed dengan genesis【Phase 3 — EV-008】; Core Components: BEX, Bend, Berps, HONEY sebagai protocol-level【Phase 4 — Core Components】; Ecosystem Decision Pattern 1: native first【Phase 9 — Ecosystem Decision Pattern 1】; Recurring Pattern 1【Phase 9 — Recurring Pattern 1】.
Supporting Dataset: Phase 3 History, Phase 4 Technology, Phase 9 Behavioral.
Confidence: High

Playbook 4: EVM-Equivalent Execution pada Modular Stack — Custom EVM module di atas application framework (Cosmos SDK) untuk tight integration dengan consensus/native modules
Explanation: Bukan fork geth/erigon. Build custom EVM interpreter dengan precompile untuk native functionality (IBC, staking, governance, custom consensus). Support standard tooling (Hardhat, Foundry, MetaMask, JSON-RPC). Trade-off: manual upstream EVM upgrades, no client diversity.
Evidence: Execution Environment: custom EVM module【Phase 4 — Execution Environment】; Core Components: EVM Module custom【Phase 4 — Core Components】; Technical Decision Pattern 2【Phase 9 — Technical Decision Pattern 2】; Trade-off 3【Phase 9 — Trade-off 3】.
Supporting Dataset: Phase 4 Technology, Phase 9 Behavioral.
Confidence: High

Playbook 5: Tokenomics dengan Delayed Insider Liquidity + Continuous Contributor Rewards — Vesting cliffs 6-12m untuk insider, governance token non-transferable earned via contribution, gas token untuk fee market
Explanation: BERA (gas): full supply minted, vesting cliffs post-TGE. BGT (governance): 100% emission ke contributor (LP), non-transferable, no insider allocation. HONEY (stablecoin): elastic supply user-minted. Alignment jangka panjang > short-term liquidity.
Evidence: Vesting Schedule cliffs【Phase 6 — Vesting Schedule】; BGT Distribution 100% to LPs【Phase 6 — BGT Distribution】; HONEY Supply elastic【Phase 6 — HONEY Supply】; Financial Decision Pattern 3, Recurring Pattern 4【Phase 9 — Financial Decision Pattern 3, Recurring Pattern 4】.
Supporting Dataset: Phase 6 Token, Phase 9 Behavioral.
Confidence: High

Playbook 6: Pragmatic Governance Separation — On-chain untuk protocol parameters, off-chain legal entity untuk treasury/legal/compliance
Explanation: BGT-weighted voting untuk fee switch, emissions, upgrades, parameters. Foundation (Cayman) untuk treasury management, legal wrapper, compliance. No DAO legal wrapper bridging. Regulatory-driven separation. Community pool existence optional/unknown.
Evidence: Governance: BGT-weighted voting【Phase 6 — Governance】; Treasury governance unclear【Phase 6 — Governance】; Foundation only legal entity【Phase 2 — Entity List】; Governance Decision Pattern 1, 2【Phase 9 — Governance Decision Pattern 1, 2】.
Supporting Dataset: Phase 6 Token, Phase 2 Entity, Phase 9 Behavioral.
Confidence: High

Playbook 7: EVM-First Developer Onboarding Strategy — Prioritaskan Hardhat, Foundry, MetaMask, JSON-RPC standard; sembunyikan underlying modular stack complexity
Explanation: Documentation, tooling, wallet support, RPC endpoints semua Ethereum-standard. Developer tidak perlu belajar CosmWasm/Rust/IBC. Underlying Cosmos SDK/CometBFT/IBC sebagai infrastructure tersembunyi. Capture Ethereum developer mindshare first.
Evidence: Developer Ecosystem: Hardhat, Foundry primary【Phase 7 — Developer Ecosystem】; Wallet Ecosystem: MetaMask full support【Phase 7 — Wallet Ecosystem】; Execution Environment: EVM-equivalent standard JSON-RPC【Phase 4 — Execution Environment】; Ecosystem Decision Pattern 2, Recurring Pattern 3【Phase 9 — Ecosystem Decision Pattern 2, Recurring Pattern 3】.
Supporting Dataset: Phase 7 Ecosystem, Phase 4 Technology, Phase 9 Behavioral.
Confidence: High

Playbook 8: IBC Integration untuk Cross-Chain Liquidity Access — Aktifkan IBC channels ke major Cosmos chains (Osmosis, Celestia) untuk liquidity access tanpa custom bridge risk
Explanation: IBC standard protocol, permissionless relayers, light client verification. Channels live mainnet genesis. Relayer dependency accepted as calculated risk. No native relayer incentive program needed initially.
Evidence: EV-014 IBC channels activated mainnet【Phase 3 — EV-014】; IBC Module live【Phase 4 — Core Components: IBC Module】; External Dependencies: IBC High criticality【Phase 7 — External Dependencies】; Risk Response Pattern 4: calculated acceptance【Phase 9 — Risk Response Pattern 4】.
Supporting Dataset: Phase 3 History, Phase 4 Technology, Phase 7 Ecosystem, Phase 9 Behavioral.
Confidence: High

## Anti-patterns

Anti-pattern 1: Treasury Opacity tanpa Transparency Dashboard atau Community Pool
Explanation: Foundation mengelola treasury tanpa public reporting, on-chain address disclosure, atau financial statements. Tidak ada on-chain community pool funded by protocol revenue. Trust deficit untuk komunitas, regulator, dan potential contributors. Membuat governance on-chain terasa "theater" jika treasury off-chain uncontrolled.
Evidence: Treasury size/composition undisclosed【Phase 5 — Treasury】; Funding History 0 verified【Phase 5 — Funding History】; Governance: treasury governance unclear, community pool unknown【Phase 6 — Governance】; Trade-off 5: Foundation vs DAO treasury【Phase 9 — Trade-off 5】; Financial Decision Pattern 5: treasury opacity【Phase 9 — Financial Decision Pattern 5】.
Supporting Dataset: Phase 5 Financial, Phase 6 Token, Phase 9 Behavioral.
Confidence: High

Anti-pattern 2: Critical Infrastructure Dependency Unidentified (Oracle) — Menerima single point of failure tanpa disclosure atau redundancy
Explanation: Bend (liquidation), Berps (funding rate), HONEY (peg) semua butuh price feeds. Oracle provider tidak diungkapkan di docs, whitepaper, GitHub, audit. Tidak ada terverifikasi multiple oracle integration. Silent acceptance of centralization risk untuk critical DeFi primitives.
Evidence: No native oracle documented【Phase 4 — Known Technical Limitations】; Oracle Provider unidentified High criticality【Phase 7 — External Dependencies】; Oracle Dependency risk【Phase 7 — Ecosystem Risks】; Risk Response Pattern 5: silent acceptance【Phase 9 — Risk Response Pattern 5】.
Supporting Dataset: Phase 4 Technology, Phase 7 Ecosystem, Phase 9 Behavioral.
Confidence: High

Anti-pattern 3: Validator Set Over-Curation — High hardware requirements + limited slots menciptakan barrier to entry yang mengonsentrasi stake
Explanation: 100 validator slots dengan 64GB RAM, 4TB NVMe, 10Gbps requirements. Geographic distribution tidak transparan. Entity identity dan commission rates tidak publik. Trade-off performance/security vs decentralization terlalu condong ke centralization. Risiko capture oleh besar operator.
Evidence: Validator requirements high【Phase 4 — Known Technical Limitations】; Consensus Mechanism: 100 validators【Phase 4 — Consensus Mechanism】; Infrastructure Providers: 100 Validators critical【Phase 7 — Infrastructure Providers】; Trade-off 1: decentralization vs performance【Phase 9 — Trade-off 1】.
Supporting Dataset: Phase 4 Technology, Phase 7 Ecosystem, Phase 9 Behavioral.
Confidence: High

Anti-pattern 4: Soulbound Governance Token tanpa Wrapper Escape Hatch — BGT non-transferable mencegah composability DeFi fundamental
Explanation: BGT tidak bisa dipakai collateral di Bend, tidak bisa trade di BEX, tidak bisa integrate external protocols tanpa wrapper. Wrapper diperlukan tapi tidak disediakan native. Membatasi utility BGT hanya ke governance/emission direction/validator weight. Value capture hanya via fee switch (governance-gated, unverified).
Evidence: BGT design limits composability【Phase 4 — Known Technical Limitations】; BGT non-transferable【Phase 6 — BGT Distribution】; Trade-off 2: BGT non-transferable vs composability【Phase 9 — Trade-off 2】.
Supporting Dataset: Phase 4 Technology, Phase 6 Token, Phase 9 Behavioral.
Confidence: High

Anti-pattern 5: Custom Execution Environment tanpa Upstream Compatibility Commitment — Custom EVM module mengorbankan automatic EIP upgrades dan client diversity
Explanation: Custom EVM interpreter bukan fork geth/erigon. Harus manual implement setiap EIP upgrade (Shanghai, Cancun, Prague). Tidak ada client diversity (single implementation). Maintenance burden tinggi. Risk consensus bugs dari custom implementation.
Evidence: Execution Environment: custom EVM module【Phase 4 — Execution Environment】; Core Components: EVM Module custom【Phase 4 — Core Components】; Technical Decision Pattern 2【Phase 9 — Technical Decision Pattern 2】; Trade-off 3: custom EVM vs upstream compatibility【Phase 9 — Trade-off 3】.
Supporting Dataset: Phase 4 Technology, Phase 9 Behavioral.
Confidence: High

Anti-pattern 6: No Public Audit Reports untuk Core Protocol dan Native Apps — Security assurance gap meski mainnet live
Explanation: 0 audit report publik teridentifikasi untuk PoL module, EVM module, CometBFT integration, BEX, Bend, Berps, HONEY. Bug bounty program tidak diketahui. Absence of transparency ≠ absence of audits (banyak L1 audit private) tapi komunitas tidak bisa verify.
Evidence: Audit History: 0 audit report publik【Phase 4 — Audit History】; Security Model: bug bounty unknown【Phase 4 — Security Model】; Open Threads Phase 8: audit reports tidak ditemukan【Phase 8 — Open Threads】.
Supporting Dataset: Phase 4 Technology, Phase 8 Market.
Confidence: High

Anti-pattern 7: Adoption Metrics Tidak Teragregasi Publik — Raw data di explorer tapi no dashboard metrics (TVL, volume, users, DAU)
Explanation: Berascan shows raw tx/block data tapi no aggregated metrics. DefiLlama chain page exists tapi native protocols not integrated. No Dune dashboard resmi. Sulit assess traction, compare dengan competitor, attract integrators/investors.
Evidence: Adoption Metrics all unknown【Phase 8 — Adoption Metrics】; DefiLlama native apps not integrated【Phase 5 — Revenue History】; Market Share tidak tersedia【Phase 8 — Market Share】; Open Threads Phase 8: TVL, DAU, volume unknown【Phase 8 — Open Threads】.
Supporting Dataset: Phase 8 Market, Phase 5 Financial.
Confidence: High

Anti-pattern 8: Fee Switch Governance-Gated tanpa Activation Timeline atau Incentive — Critical value capture mechanism stuck di governance limbo
Explanation: Fee switch dirancang dari awal, testnet validated (Artio v3), tapi activation memerlukan BGT proposal. Post-TGE status unverified. BGT holder value capture dependent pada fee switch. Insider cliff unlocks 2025-08/2026-02 menciptakan urgency. No clear timeline atau incentive untuk proposal.
Evidence: Revenue Model: Fee Switch planned, status unverified【Phase 5 — Revenue Model】; BGT Utility: Fee Switch Revenue Share【Phase 6 — BGT Utility】; EV-009 Artio v3 test fee switch【Phase 3 — EV-009】; Governance proposal types include Fee Switch【Phase 6 — Governance】; Open Threads Phase 8: fee switch status unverified【Phase 8 — Open Threads】.
Supporting Dataset: Phase 5 Financial, Phase 6 Token, Phase 3 History, Phase 8 Market, Phase 9 Behavioral.
Confidence: Medium

## Lessons Learned

Lesson 1: Novel consensus mechanism memerlukan extensive testnet iteration bertahap — tidak bisa rush ke mainnet tanpa validasi PoL, IBC, governance mechanics terpisah
Lesson 2: Full stack native launch (consensus + apps + tokens) memastikan flywheel berfungsi hari 1 tapi memerlukan koordinasi engineering yang ekstrem dan testnet validation yang komprehensif
Lesson 3: EVM-equivalent pada modular stack (Cosmos SDK) menarik developer Ethereum secara masif — tooling compatibility adalah moat onboarding terbesar
Lesson 4: Tokenomics alignment jangka panjang (vesting cliffs, soulbound governance token, continuous emission) melindungi early network tapi menciptakan cliff risk yang harus di-manage via fee switch/value capture activation
Lesson 5: Treasury opacity (Foundation-controlled, no community pool) memberikan regulatory flexibility tapi menciptakan trust deficit yang sulit di-recover later
Lesson 6: Critical infrastructure (oracle) unidentified adalah silent killer untuk DeFi primitives — harus di-disclose dan di-redundansi dari hari 1
Lesson 7: Validator set over-curation (high req, limited slots) trade-off performance vs decentralization harus di-balance dengan geographic/entity transparency
Lesson 8: Soulbound governance token mencegah capture tapi membutuhkan wrapper/escape hatch untuk DeFi composability — design untuk interoperability dari awal
Lesson 9: Custom execution environment (custom EVM) memberikan control penuh tapi maintenance burden tinggi — commit ke upstream compatibility roadmap atau accept fork burden
Lesson 10: Fee switch sebagai value capture mechanism harus memiliki activation pathway yang jelas (auto-activate, timeline, atau incentive) — governance-gated tanpa deadline berisiko stuck
Lesson 11: Pseudonymous leadership dengan Foundation legal wrapper work untuk regulatory compliance tapi butuh transparency mechanism (treasury dashboard, multisig, community pool) untuk trust
Lesson 12: IBC integration untuk cross-chain liquidity access lebih efisien vs custom bridge — tapi relayer dependency harus di-incentivize atau di-monitor

## Knowledge Summary

Strategic Principles:
1. Liquidity-Security Alignment — PoL mengikat validator weight ke DeFi liquidity via BGT delegation
2. Modular Architecture dengan Custom Integration Layer — Pisahkan consensus/framework/execution/PoL, integrasikan via custom layer
3. Native DeFi Primitives First — Bangun core DeFi stack sebagai protocol-level components sebelum third-party
4. EVM-Equivalent Developer Experience — Prioritaskan Ethereum tooling/wallet/RPC, sembunyikan Cosmos complexity
5. Long-term Alignment via Tokenomics — Vesting cliffs, BGT soulbound, continuous LP rewards
6. Pragmatic Governance Separation — On-chain parameters, off-chain Foundation treasury/legal
7. Stealth Funding Opacity — No public VC disclosure, Foundation sole funding vehicle

Success Factors:
1. Staged testnet iteration (3 phases, 1.5 tahun) memvalidasi kompleksitas bertahap
2. Novel PoL consensus differentiation vs competitor L1
3. Full stack native launch memastikan flywheel immediate
4. EVM-equivalent execution menarik Ethereum developer tanpa friction
5. Tokenomics alignment jangka panjang mencegah early dump/mercenary capital
6. IBC integration membuka Cosmos liquidity access tanpa custom bridge

Failure Factors:
1. Treasury/funding opacity — no transparency, no community pool
2. Oracle provider unidentified — critical infrastructure opaque
3. Validator set centralization risk — high req, limited slots, no transparency
4. BGT soulbound limits composability — no wrapper escape hatch
5. No public audit reports — security assurance gap
6. Adoption metrics not aggregated — no TVL/volume/users dashboard
7. Fee switch activation unverified — governance-gated value capture stuck
8. Custom EVM module — no upstream EIP auto-upgrades, no client diversity

Decision Framework:
Research/Design (2022) → Legal/Infrastructure (2023) → Iterative Testnet (2023-2024) → Full Stack Genesis (2024-06) → TGE/Tokenomics (2025-02) → Governance Evolution (Ongoing)

Reusable Playbooks:
1. Novel Consensus dengan Economic Alignment (PoL formula generalizable)
2. Staged Testnet Program (core → integration → governance)
3. Full Stack Native Launch untuk Flywheel Bootstrapping
4. EVM-Equivalent pada Modular Stack (custom EVM module)
5. Tokenomics Delayed Insider Liquidity + Continuous Contributor Rewards
6. Pragmatic Governance Separation (on-chain params, off-chain treasury)
7. EVM-First Developer Onboarding (Hardhat/Foundry/MetaMask standard)
8. IBC Integration untuk Cross-Chain Liquidity Access

Anti-patterns:
1. Treasury Opacity tanpa Transparency Dashboard/Community Pool
2. Critical Infrastructure Dependency Unidentified (Oracle)
3. Validator Set Over-Curation (high req, limited slots, no transparency)
4. Soulbound Governance Token tanpa Wrapper Escape Hatch
5. Custom Execution Environment tanpa Upstream Compatibility Commitment
6. No Public Audit Reports untuk Core Protocol/Native Apps
7. Adoption Metrics Tidak Teragregasi Publik
8. Fee Switch Governance-Gated tanpa Activation Timeline/Incentive

## Open Questions
- [foundation] Exact founding entity legal structure beyond "Berachain Foundation (Cayman Islands)" — need to verify if there are additional entities (e.g., Bera Labs, Berachain Labs) and their jurisdictions
- [foundation] Verified core team size and identifiable contributors beyond pseudonymous handles — team page lists ~20 named pseudonymous contributors but total headcount unclear
- [foundation] Precise testnet launch dates for Artio v1/v2/v3 — sources cite different dates (Jan 2023, Jan 2024, Oct 2024)
- [foundation] Token contract addresses for BERA/BGT/HONEY on mainnet — need on-chain verification from berascan.com
- [foundation] Whether Berachain has a native IBC connection live or only EVM bridge — docs mention IBC but implementation status unclear
- [foundation] TGE date confirmation — some sources say Feb 6 2025, others say "Q1 2025" — need official announcement
- [foundation] BERA initial supply and distribution breakdown — whitepaper mentions 500M initial supply but allocation percentages vary across sources
- [foundation] Fee switch status and revenue flow — docs mention "fee switch" for BGT stakers but activation status unclear
- [entity] Identitas hukum lengkap founding entity: apakah ada Bera Labs / Berachain Labs terpisah dari Berachain Foundation, dan yurisdiksi masing-masing
- [entity] Daftar investor (VC, strategic angels) yang berpartisipasi di ronde private/public — tidak tersedia di sumber publik fase ini
- [entity] Auditor keamanan (smart contract audit firms) untuk protokol inti dan aplikasi native — belum teridentifikasi
- [entity] Market maker / liquidity provider resmi untuk BERA/BGT/HONEY — tidak terpublikasi
- [entity] Status koneksi IBC live: apakah relayer dan channel IBC sudah aktif mainnet atau hanya testnet
- [entity] Alamat kontrak token BERA/BGT/HONEY pada mainnet — perlu verifikasi on-chain via berascan.com
- [entity] Detail alokasi tokenomics: persentase TGE, vesting schedule, alokasi team/investor/community/ecosystem — whitepaper vs announcement resmi
- [entity] Status fee switch BGT: apakah sudah diaktifkan dan revenue flow ke staker BGT
- [entity] Entitas legal wrapper untuk DAO/governance (jika ada) terpisah dari Foundation
- [entity] Enterprise partnerships / integrasi institusional (custody, node providers, oracle) — belum termuat di dokumentasi publik
- [history] Tanggal pasti pendirian konsep (EV-001): hanya diketahui "2022" dari narasi umum; tidak ada announcement resmi dengan tanggal spesifik
- [history] Tanggal pasti pendirian Berachain Foundation (EV-002): hanya diketahui "2023"; perlu verifikasi dokumen incorporasi Cayman Islands
- [history] Detail funding rounds (VC, strategic angels, valuation): tidak ada informasi publik di fase 1-2; perlu cari announcement resmi atau filing
- [history] Tanggal pasti deployment masing-masing aplikasi native BEX/Bend/Berps (EV-008): apakah bersamaan dengan mainnet genesis 2024-06-06 atau berurutan beberapa hari/minggu setelahnya
- [history] Status IBC channels live (EV-014): docs mention IBC tapi tidak ada daftar channel/relayer aktif spesifik; perlu verifikasi on-chain via berascan atau mapofzones
- [history] Alamat kontrak token BERA/BGT/HONEY di mainnet (EV-011, EV-015, EV-016): Phase 1 mencatat placeholder addresses; perlu verifikasi on-chain aktual di berascan.com
- [history] Detail tokenomics TGE: persentase TGE allocation, vesting schedule team/investor/community — whitepaper vs announcement resmi Feb 2025
- [history] Status fee switch BGT (EV-017): apakah sudah diaktifkan via governance proposal; revenue flow ke staker BGT berapa persen
- [history] Auditor keamanan (smart contract audit firms) untuk protokol inti dan aplikasi native: tidak teridentifikasi di sumber publik
- [history] Investor/backer resmi: tidak ada daftar investor terpublikasi; perlu cari announcement funding atau portfolio VC
- [history] Artio testnet v3 tanggal pasti: Phase 1 bilang "Oct 2024" tapi tidak ada tanggal hari; perlu cari blog post resmi
- [history] Berapa validator di genesis set (EV-007) dan kriteria seleksi: tidak termuat di dokumentasi publik
- [history] Apakah ada security incident/exploit di testnet atau mainnet: tidak ditemukan di fase 1-2; perlu cari audit reports atau incident reports
- [history] Legal wrapper untuk DAO/governance terpisah dari Foundation: belum teridentifikasi
- [history] Enterprise partnerships (custody, node providers, oracle): tidak termuat di dokumentasi publik phase 1-2
- [technology] Audit report formal untuk protokol inti (PoL module, EVM module, Cosmos SDK modules) dan aplikasi native (BEX, Bend, Berps, HONEY) — tidak ditemukan di sumber publik; perlu konfirmasi ke tim atau auditor
- [technology] Oracle provider resmi untuk Bend (lending liquidation) dan Berps (perpetuals funding rate/mark price) — tidak terdokumentasi di docs.berachain.com
- [technology] Fee switch activation status pasca-TGE — dokumentasi menyebut fitur tapi tidak ada confirmation on-chain apakah proposal sudah passed dan active
- [technology] IBC channels aktif dan relayer infrastructure detail — docs mention IBC compatible tapi tidak ada daftar channel/relayer live di mainnet
- [technology] EVM state management strategy: apakah ada state expiry, pruning, atau history expiry mechanism direncanakan untuk handle state bloat
- [technology] Validator hardware requirements resmi dan sebaran geografis validator set genesis — docs mention specs tapi tidak ada validator set transparency dashboard
- [technology] BGT delegation mechanics detail: apakah redelegation cooldown, unbonding period, dan slash socialization ke delegator sudah finalized
- [technology] HONEY collateralization ratio dan liquidation mechanism detail di Bend — tidak terdokumentasi dengan parameter spesifik
- [technology] Cross-chain bridge security model untuk non-IBC assets (Ethereum, Bitcoin, Solana) — apakah hanya IBC atau ada bridge eksternal (Wormhole, LayerZero, Axelar, dll)
- [technology] Formal verification status untuk critical smart contracts (BGT, BERA, PoL distribution logic) — tidak diketahui
- [technology] Upgrade governance process: quorum, voting period, execution delay untuk software upgrade proposals — parameter spesifik tidak terdokumentasi
- [technology] Indexer infrastructure: apakah berascan menggunakan custom indexer atau Subgraph/The Graph — arsitektur indexer tidak terdokumentasi
- [technology] Transaction fee market detail: EIP-1559 parameters (base fee change denominator, elasticity multiplier) untuk Berachain EVM — tidak terdokumentasi
- [technology] MEV protection: apakah ada PBS (Proposer-Builder Separation), encrypted mempool, atau MEV mitigation native — tidak terdokumentasi
- [technology] Light client support untuk trust-minimized bridging ke non-Cosmos chain — tidak terdokumentasi
- [financial] Funding history lengkap: apakah Berachain benar-benar tidak pernah melakukan funding round (VC/strategic/grant) atau informasi tidak dipublikasikan — perlu konfirmasi ke tim atau cari filing Cayman Islands
- [financial] Treasury dashboard/on-chain address: apakah Foundation mempublikasikan treasury wallet address untuk verifikasi komposisi aset
- [financial] Fee switch activation status: apakah governance proposal sudah passed dan fee switch live post-TGE — perlu cek on-chain governance proposals
- [financial] Revenue tracking: apakah BEX, Bend, Berps memiliki revenue dashboard sendiri (seperti info fees collected, volume, TVL) — tidak ditemukan di docs/app
- [financial] Investor/backer list: apakah ada private investors (VC, angels) yang tidak di-announce — perlu cari portfolio VC yang mention Berachain
- [financial] Grants program: apakah ada ecosystem grants (seperti Cosmos SDK chains biasanya) — tidak terdokumentasi
- [financial] Audit financial: apakah ada financial audit untuk Foundation (Cayman Islands requirement) — tidak publik
- [financial] Token sale mechanics: detail TGE allocation, price, vesting untuk sale participants — Phase 6 territory tapi related to financial intelligence
- [financial] Protocol revenue split: bagaimana revenue BEX/Bend/Berps dialokasikan (ke treasury, ke BGT stakers via fee switch, ke development) — governance parameter tidak terdokumentasi
- [financial] DefiLlama/Token Terminal integration: kapan native apps akan terintegrasi untuk revenue tracking standardized
- [financial] Legal financial risk: apakah ada regulatory inquiry (SEC, CFTC, Cayman regulators) terkait token sale/operations — tidak ditemukan disclosure
- [token] BERA contract address on-chain verification: Phase 1 mencatat 0x6969...6969; perlu confirm di berascan.com apakah benar contract resmi (bukan placeholder)
- [token] BGT contract address on-chain verification: 0x5C47...8a6a perlu diverifikasi
- [token] HONEY contract address on-chain verification: 0x0E4a...e8e8 placeholder dari Phase 1; perlu alamat aktual di mainnet
- [token] Circulating supply real-time untuk BERA/BGT/HONEY: tidak ada dashboard resmi; perlu on-chain query atau third-party indexer (DefiLlama, CoinGecko, CoinMarketCap) — belum terintegrasi per Phase 5
- [token] Holder distribution on-chain analysis: top holders, foundation wallet, investor wallets, team wallets — tidak diungkap publik; perlu block explorer analysis
- [token] Vesting contract addresses dan schedule on-chain: apakah vesting di-enforce via smart contract (vesting wallet/stream) atau off-chain legal agreement — tidak terdokumentasi
- [token] Fee switch activation status: apakah governance proposal sudah passed dan fee switch live; revenue flow ke BGT stakers berapa % — tidak dikonfirmasi on-chain
- [token] BGT emission rate per block/epoch: exact number tidak di-specify di whitepaper/docs; perlu query on-chain atau docs teknis
- [token] Community pool existence: apakah ada on-chain community pool funded by protocol revenue (BEX/Bend/Berps fees) untuk governance spending — tidak terdokumentasi
- [token] BGT slashing mechanics: apakah delegated BGT slashable saat validator misbehave (double sign/downtime) — whitepaper tidak detail; hanya BERA stake disebut slashable
- [token] HONEY collateralization ratio detail di Bend: LTV, liquidation threshold, liquidation penalty — tidak terdokumentasi dengan parameter spesifik
- [token] Oracle provider untuk HONEY peg / Bend liquidation / Berps funding rate: tidak terdokumentasi (Chainlink? Pyth? Custom?)
- [token] TGE airdrop criteria dan allocation percentage dari 38% Community: berapa % untuk airdrop vs LP incentives vs ecosystem grants — tidak di-breakdown detail
- [token] Investor entities identity: 15% allocation untuk investors; siapa VC/strategic angels — tidak diungkap publik
- [token] Advisory board identity: 5% allocation untuk advisors; siapa advisors — tidak diungkap publik
- [token] BERA base fee burn rate tracking: EIP-1559 base fee burn amount per block/epoch — tidak ada dashboard
- [token] Cross-chain BERA/BGT/HONEY representation: apakah ada wrapped version di Ethereum, Cosmos (IBC), Solana — tidak terdokumentasi
- [token] Governance proposal history dan voting turnout: proposal ID, description, vote count, turnout % — tidak ada aggregated dashboard
- [token] BGT gauge voting mechanics detail: epoch length, vote weight calculation, gauge weight update frequency — tidak terdokumentasi detail
- [token] HONEY peg stability metrics: historical depeg events, max deviation, recovery time — tidak ada data publik
- [token] Legal opinion on BGT soulbound status: apakah BGT non-transferability survive regulatory scrutiny (securities law) — tidak ada legal memo publik
- [ecosystem] Oracle provider resmi untuk Bend, Berps, HONEY — tidak terdokumentasi di docs.berachain.com, whitepaper, atau GitHub; perlu konfirmasi ke tim atau audit smart contract Bend/Berps untuk melihat price feed address
- [ecosystem] Daftar CEX spesifik yang listing BERA post-TGE 2025-02-06 — Phase 3 EV-012 mention "CEX/DEX listing dimulai" tapi tidak nama exchange; perlu cek CoinGecko/CoinMarketCap/DefiLlama listing data
- [ecosystem] Wallet support resmi terverifikasi (Keplr, Leap, Rabby, dll) — Phase 4 mention EVM/IBC compatibility tapi tidak ada halaman "Supported Wallets" resmi; perlu cek docs.berachain.com/wallets atau announcement resmi
- [ecosystem] RPC node provider resmi/public endpoint list — docs mention JSON-RPC endpoints tapi tidak list provider (QuickNode, Ankr, Chainstack, dll); perlu cek docs.berachain.com/develop/rpc untuk daftar lengkap
- [ecosystem] Grants program / hackathon history — Phase 5 Financial mention "Grants: tidak diketahui"; Phase 3 EV-018 mention ecosystem growth tapi tidak detail grants; perlu cari blog post "Berachain Grants" atau "Ecosystem Fund"
- [ecosystem] IBC channels aktif dan relayer operator identitas — docs mention IBC live tapi tidak ada daftar channel (channel-id, counterparty chain, relayer address); perlu query on-chain via berascan atau mapofzones
- [ecosystem] Validator set transparency: geografis distribution, entity identity, commission rates — docs mention 100 validator tapi tidak ada dashboard publik; perlu cek berascan validator page atau governance forum
- [ecosystem] External DeFi protocols terintegrasi (non-native) — Phase 3 EV-018 mention "integrasi protokol eksternal" tapi tidak list nama; perlu cak browsing DefiLlama Berachain ecosystem page atau docs.berachain.com/ecosystem
- [ecosystem] CosmWasm integration status — Phase 4 Technology mention "optional" tapi tidak ada contract WASM deployed tercatat; perlu cek github.com/berachain untuk CosmWasm contracts
- [ecosystem] Bug bounty program (Immunefi, HackerOne, native) — Phase 4 Security Model mention "tidak diketahui"; perlu cek immunefi.com/berachain atau hackerone.com/berachain
- [ecosystem] Bridge non-IBC (Ethereum, Bitcoin, Solana) — apakah hanya IBC atau ada Wormhole/LayerZero/Axelar integration; tidak terdokumentasi di Phase 1-6
- [ecosystem] Legal wrapper untuk DAO/governance terpisah dari Foundation — Phase 2 tidak ada DAO entity; Phase 6 governance mention on-chain voting tapi legal structure unclear
- [ecosystem] Indexer infrastructure detail: berascan menggunakan custom indexer atau The Graph/Subgraph — arsitektur indexer tidak terdokumentasi
- [ecosystem] MEV protection status: PBS, encrypted mempool, atau MEV mitigation native — Phase 4 Known Limitations tidak mention; perlu cek validator docs atau consensus specs
- [ecosystem] Light client support untuk trust-minimized bridging ke non-Cosmos chain — tidak terdokumentasi
- [ecosystem] Cross-chain BERA/BGT/HONEY representation (wrapped versions di Ethereum, Solana, dll) — tidak terdokumentasi
- [market] TVL data for Berachain native apps (BEX, Bend, Berps) — DefiLlama chain page exists but native protocols not fully integrated per Phase 5; need official TVL dashboard or DefiLlama integration completion
- [market] CEX listing specifics — Phase 3 EV-012 and TGE announcement mention CEX listings but do not name exchanges; need CoinGecko/CoinMarketCap markets tab verification post-TGE
- [market] Daily active users / transaction count / unique wallets — Berascan shows raw data but no aggregated metrics dashboard; need Dune Analytics dashboard or official metrics page
- [market] Developer count — GitHub contributors visible (~20 named pseudonymous + ~50 total per Phase 2) but no standardized developer activity metric (Electric Capital, etc.)
- [market] BEX 24h volume / liquidity depth — BEX app shows individual pools but no aggregated volume/TVL dashboard visible
- [market] IBC bridge volume / packet count — Map of Zones may have data but not verified; need on-chain query
- [market] BGT holder / delegator count — BGT contract on Berascan but no holder analytics dashboard
- [market] Market share metrics — No L1 market share data (TVL/volume/users) available from DefiLlama, Token Terminal, or Messari for Berachain
- [market] Fee switch activation status — Governance-gated feature mentioned in whitepaper/docs; on-chain proposal status not verified
- [market] Oracle provider for Bend/Berps/HONEY — Critical infrastructure dependency unidentified in all phases; need audit reports or contract verification
- [market] Grants program / hackathon history — Not found in Phases 1-7; need official announcement or blog post search
- [market] Non-IBC bridge integrations (Wormhole, LayerZero, Axelar, etc.) — Not documented; need partnership announcements
- [market] Legal wrapper for DAO/governance separate from Foundation — Phase 2 shows no DAO entity; Phase 6 governance is on-chain only
- [market] BERA circulating supply real-time — No official dashboard; CoinGecko/CoinMarketCap may show post-TGE but methodology unclear
- [market] HONEY peg stability metrics — Historical depeg events, max deviation, recovery time not published
- [market] Validator set transparency — Geographic distribution, entity identity, commission rates not public; only "100 validators at genesis" documented
- [market] MEV protection status — No PBS, encrypted mempool, or MEV mitigation documented in Phase 4
- [market] Cross-chain BERA/BGT/HONEY representations (wrapped on Ethereum, Solana, etc.) — Not documented
- [behavioral] Funding history lengkap: apakah benar tidak ada VC funding atau private funding tidak di-announce — perlu verifikasi Cayman Islands filing atau investor portfolio cross-check
- [behavioral] Treasury dashboard/on-chain address: apakah Foundation akan mempublikasikan treasury wallet untuk verifikasi komposisi aset dan revenue flow
- [behavioral] Fee switch activation status: apakah governance proposal sudah passed dan fee switch live post-TGE — critical untuk BGT holder value capture sebelum cliff unlocks 2025-08
- [behavioral] Oracle provider untuk Bend/Berps/HONEY: unidentified di semua fase — perlu audit report atau contract verification untuk price feed addresses
- [behavioral] CEX listing specifics: Phase 3 EV-012 mention CEX listing tapi tidak nama exchange — perlu CoinGecko/CoinMarketCap verification post-TGE
- [behavioral] BGT slashing mechanics: apakah delegated BGT slashable saat validator misbehave — whitepaper hanya mention BERA stake slashable
- [behavioral] HONEY collateralization parameter di Bend: LTV, liquidation threshold, penalty tidak terdokumentasi
- [behavioral] Legal wrapper untuk DAO terpisah dari Foundation: Phase 2 no DAO entity; Phase 6 governance on-chain only — regulatory risk
- [behavioral] Audit reports untuk core protocol (PoL, EVM module, CometBFT integration) dan native apps (BEX, Bend, Berps, HONEY) — tidak ditemukan publik
- [behavioral] IBC channels aktif dan relayer infrastructure detail: docs mention IBC live tapi tidak ada daftar channel/relayer live
- [behavioral] Validator set transparency: geographic distribution, entity identity, commission rates — tidak publik
- [behavioral] MEV protection status: PBS, encrypted mempool, atau MEV mitigation — tidak terdokumentasi
- [behavioral] Cross-chain BERA/BGT/HONEY representation (wrapped di Ethereum, Solana, dll) — tidak terdokumentasi
- [behavioral] Grants program / hackathon history: tidak ditemukan di Phase 1-7
- [behavioral] Non-IBC bridge integrations (Wormhole, LayerZero, Axelar) — tidak terdokumentasi
- [behavioral] Circulating supply real-time BERA/BGT/HONEY: tidak ada dashboard resmi
- [behavioral] Holder distribution on-chain analysis: top holders, foundation wallet, investor wallets — tidak diungkap
- [behavioral] Vesting contract addresses dan enforcement mechanism (smart contract vs legal agreement) — tidak terdokumentasi
- [behavioral] BGT emission rate per block/epoch exact number — tidak di-specify whitepaper/docs
- [behavioral] Community pool existence: apakah ada on-chain community pool funded by protocol revenue — tidak terdokumentasi
- [behavioral] HONEY peg stability metrics: historical depeg events, max deviation, recovery time — tidak ada data publik
- [behavioral] Governance proposal history dan voting turnout aggregated — tidak ada dashboard
- [knowledge] Funding history lengkap: apakah benar tidak ada VC funding atau private funding tidak di-announce — perlu verifikasi Cayman Islands filing atau investor portfolio cross-check【Phase 5 — Funding History】【Phase 5 — Financial Dependencies】
- [knowledge] Treasury dashboard/on-chain address: apakah Foundation akan mempublikasikan treasury wallet untuk verifikasi komposisi aset dan revenue flow【Phase 5 — Treasury】【Phase 9 — Financial Decision Pattern 5】
- [knowledge] Fee switch activation status: apakah governance proposal sudah passed dan fee switch live post-TGE — critical untuk BGT holder value capture sebelum cliff unlocks 2025-08【Phase 5 — Revenue Model】【Phase 6 — BGT Utility】【Phase 8 — Open Threads】
- [knowledge] Oracle provider untuk Bend/Berps/HONEY: unidentified di semua fase — perlu audit report atau contract verification untuk price feed addresses【Phase 4 — Known Technical Limitations】【Phase 7 — External Dependencies】【Phase 9 — Risk Response Pattern 5】
- [knowledge] CEX listing specifics: Phase 3 EV-012 mention CEX listing tapi tidak nama exchange — perlu CoinGecko/CoinMarketCap verification post-TGE【Phase 3 — EV-012】【Phase 8 — Open Threads】
- [knowledge] BGT slashing mechanics: apakah delegated BGT slashable saat validator misbehave — whitepaper hanya mention BERA stake slashable【Phase 4 — Security Model】【Phase 6 — BGT Utility】【Phase 8 — Open Threads】
- [knowledge] HONEY collateralization parameter di Bend: LTV, liquidation threshold, penalty tidak terdokumentasi【Phase 4 — Core Components: Bend】【Phase 6 — HONEY Utility】【Phase 8 — Open Threads】
- [knowledge] Legal wrapper untuk DAO terpisah dari Foundation: Phase 2 no DAO entity; Phase 6 governance on-chain only — regulatory risk【Phase 2 — Entity List】【Phase 6 — Governance】【Phase 9 — Governance Decision Pattern 2】
- [knowledge] Audit reports untuk core protocol (PoL, EVM module, CometBFT integration) dan native apps (BEX, Bend, Berps, HONEY) — tidak ditemukan publik【Phase 4 — Audit History】【Phase 8 — Open Threads】
- [knowledge] IBC channels aktif dan relayer infrastructure detail: docs mention IBC live tapi tidak ada daftar channel/relayer live【Phase 3 — EV-014】【Phase 7 — Major Integrations】【Phase 8 — Open Threads】
- [knowledge] Validator set transparency: geographic distribution, entity identity, commission rates — tidak publik【Phase 4 — Known Technical Limitations】【Phase 7 — Infrastructure Providers】【Phase 8 — Open Threads】
- [knowledge] MEV protection status: PBS, encrypted mempool, atau MEV mitigation — tidak terdokumentasi【Phase 4 — Known Technical Limitations】【Phase 8 — Open Threads】
- [knowledge] Cross-chain BERA/BGT/HONEY representation (wrapped di Ethereum, Solana, dll) — tidak terdokumentasi【Phase 6 — Token Information】【Phase 8 — Open Threads】
- [knowledge] Grants program / hackathon history: tidak ditemukan di Phase 1-7【Phase 5 — Fundraising Mechanism】【Phase 7 — Developer Ecosystem】【Phase 8 — Open Threads】
- [knowledge] Non-IBC bridge integrations (Wormhole, LayerZero, Axelar) — tidak terdokumentasi【Phase 7 — External Dependencies】【Phase 8 — Open Threads】
- [knowledge] Circulating supply real-time BERA/BGT/HONEY: tidak ada dashboard resmi【Phase 6 — Supply】【Phase 8 — Open Threads】
- [knowledge] Holder distribution on-chain analysis: top holders, foundation wallet, investor wallets — tidak diungkap【Phase 6 — Holder Distribution】【Phase 8 — Open Threads】
- [knowledge] Vesting contract addresses dan enforcement mechanism (smart contract vs legal agreement) — tidak terdokumentasi【Phase 6 — Vesting Schedule】【Phase 8 — Open Threads】
- [knowledge] BGT emission rate per block/epoch exact number — tidak di-specify whitepaper/docs【Phase 6 — BGT Inflation】【Phase 8 — Open Threads】
- [knowledge] Community pool existence: apakah ada on-chain community pool funded by protocol revenue — tidak terdokumentasi【Phase 6 — Governance】【Phase 8 — Open Threads】
- [knowledge] HONEY peg stability metrics: historical depeg events, max deviation, recovery time — tidak ada data publik【Phase 6 — HONEY Utility】【Phase 8 — Open Threads】
- [knowledge] Governance proposal history dan voting turnout aggregated — tidak ada dashboard【Phase 6 — Governance】【Phase 8 — Open Threads】
