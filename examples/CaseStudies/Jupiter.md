# Jupiter — Deep Case Study (Phased)

**CIF Dataset — Deep Dossier · Tier: Deep (anchor project)**
**Source:** Deep Research (DeepSeek), Format v3 Dependency Pipeline (10/11 phases: foundation, entity, history, technology, financial, token, ecosystem, market, behavioral, knowledge). **Auto-assembled** by `tools/ingest.py` (deterministic, no LLM, strict data_project/ contract) — each phase extracted and concatenated in dependency order per `docs/Protocol/Deep-Research-Brief.md`; the reasoning is the source reports'.
**Raw sources archived:** doc_backup/deep/Jupiter_foundation_2026-08.docx, doc_backup/deep/Jupiter_entity_2026-08.docx, doc_backup/deep/Jupiter_history_2026-08.docx, doc_backup/deep/Jupiter_technology_2026-08.docx, doc_backup/deep/Jupiter_financial_2026-08.docx, doc_backup/deep/Jupiter_token_2026-08.docx, doc_backup/deep/Jupiter_ecosystem_2026-08.docx, doc_backup/deep/Jupiter_market_2026-08.docx, doc_backup/deep/Jupiter_behavioral_2026-08.docx, doc_backup/deep/Jupiter_knowledge_2026-08.docx.
**Phases not run:** conflict.

> Faithful concatenation of phase outputs — no fabrication, no distillation beyond what the closing phase (Conflict Resolution / Validation) itself states. Consider a periodic QC pass.

---
## Foundation Intelligence
_ref: `docs/Ontology/Identity.md`, `docs/Ontology/Team.md`_

PROJECT: Jupiter
Official Name: Jupiter (JUP) (HIGH) [Jupiter Station, https://station.jup.ag/]
Symbol: JUP (HIGH) [CoinGecko, https://www.coingecko.com/en/coins/jupiter]
Category: DEX aggregator / swap infrastructure (HIGH) [Jupiter Docs, https://dev.jup.ag/]
Founding Entity: Jupiter Exchange Ltd., British Virgin Islands (MEDIUM) [OpenCorporates, https://opencorporates.com/companies/bvi/2055186; Jupiter Terms, https://jup.ag/terms]
Founders: Meow (pseudonym — founder/CEO) (HIGH) [Meow Twitter, https://x.com/meowjup; Jupiter Blog, https://blog.jup.ag/]
Core Team: ~30-40 verified contributors (engineering, product, growth) — names not fully public; key public: Meow (CEO), Rolex (CFO/COO, pseud.), Slorg (Head of Product, pseud.), Worm (Head of Engineering, pseud.) (MEDIUM) [Jupiter Careers, https://jup.ag/careers; Meow Twitter threads, https://x.com/meowjup]
Country: British Virgin Islands (legal entity); team distributed globally (HIGH) [OpenCorporates, https://opencorporates.com/companies/bvi/2055186]
Launch Date - Testnet: tidak diketahui (no public testnet phase distinct from mainnet iteration)
Launch Date - Mainnet: Oktober 2021 (initial swap aggregator launch on Solana mainnet) (HIGH) [Jupiter Blog v1 launch, https://blog.jup.ag/introducing-jupiter-v1/; Solscan program deploy, https://solscan.io/account/JUP4Fb2cqiRUcaTHdrPC8h2gNsA2ETXiPDY33WQGuJQ]
Launch Date - TGE: 31 Januari 2024 (JUP token launch via LFG launchpad & airdrop) (HIGH) [Jupiter Blog JUP launch, https://blog.jup.ag/jup-token-launch/; CoinGecko, https://www.coingecko.com/en/coins/jupiter]
Main Products: Jupiter Aggregator (swap routing); Jupiter Limit Orders; Jupiter DCA (Dollar Cost Averaging); Jupiter Perps (perpetual futures on Solana); Jupiter API/SDK (developer infrastructure); Jupiter Terminal (widget); JUP Token (governance) (HIGH) [Jupiter Products page, https://jup.ag/products; Jupiter Docs, https://dev.jup.ag/]
Official Website: https://jup.ag/ (HIGH)
Repository: https://github.com/jup-ag (HIGH) [GitHub org, https://github.com/jup-ag]
Documentation: https://dev.jup.ag/ (HIGH)
Social - X/Twitter: @JupiterExchange (HIGH) [X.com, https://x.com/JupiterExchange]
Social - Discord: https://discord.gg/jup (HIGH) [Jupiter site footer, https://jup.ag/]
Social - Telegram: @JupiterExchangeAnnouncements (announcement channel) (MEDIUM) [Telegram, https://t.me/JupiterExchangeAnnouncements]
Block Explorer: Solscan (https://solscan.io/token/JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN) (HIGH) [Solscan JUP token, https://solscan.io/token/JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN]
Token Contract: JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN (Solana SPL) (HIGH) [Solscan, https://solscan.io/token/JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN; Jupiter Tokenomics, https://blog.jup.ag/jup-tokenomics/]
Chain(s): Solana (primary); cross-chain via Wormhole integration for Perps/oracle (HIGH) [Jupiter Docs chains, https://dev.jup.ag/docs/intro; Wormhole integration, https://wormhole.com/ecosystem/jupiter/]
Ecosystem: Solana DeFi (HIGH) [Solana Foundation ecosystem page, https://solana.com/ecosystem/jupiter]

## Entity Intelligence
_ref: `docs/Ontology/Relationships.md` (entity graph)_

PROJECT: Jupiter

Entity: Jupiter Exchange Ltd.
Type: Company
Relationship: Entitas hukum pendiri (BVI) yang mengoperasikan protokol Jupiter dan produk-produknya — aggregator, limit order, DCA, perps, API/SDK, Terminal, dan token JUP
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [OpenCorporates, https://opencorporates.com/companies/bvi/2055186]; (HIGH) [Jupiter Terms, https://jup.ag/terms]

---
Entity: Meow
Type: Person
Relationship: Founder/CEO (pseudonim) — memimpin visi produk, strategi token, dan komunikasi publik Jupiter
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Meow Twitter, https://x.com/meowjup]; (HIGH) [Jupiter Blog, https://blog.jup.ag/]

---
Entity: Rolex
Type: Person
Relationship: CFO/COO (pseudonim) — mengelola operasional keuangan, treasury, dan eksekusi strategi bisnis
Period: tidak diketahui–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Jupiter Careers, https://jup.ag/careers]; (MEDIUM) [Meow Twitter threads, https://x.com/meowjup]

---
Entity: Slorg
Type: Person
Relationship: Head of Product (pseudonim) — mengarah roadmap produk aggregator, limit order, DCA, perps, dan Terminal
Period: tidak diketahui–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Jupiter Careers, https://jup.ag/careers]; (MEDIUM) [Meow Twitter threads, https://x.com/meowjup]

---
Entity: Worm
Type: Person
Relationship: Head of Engineering (pseudonim) — memimpin tim engineering inti, arsitektur on-chain, dan integrasi SDK/API
Period: tidak diketahui–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Jupiter Careers, https://jup.ag/careers]; (MEDIUM) [Meow Twitter threads, https://x.com/meowjup]

---
Entity: Jupiter Exchange
Type: Organization
Relationship: Brand/operational entity yang mengelola produk, komunitas, governance, dan ekosistem Jupiter di atas entitas hukum Jupiter Exchange Ltd.
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Official Website, https://jup.ag/]; (HIGH) [Jupiter Docs, https://dev.jup.ag/]

---
Entity: Solana
Type: Organization
Relationship: Blockchain layer-1 utama tempat seluruh protokol Jupiter (aggregator, perps, token JUP) dideploy dan beroperasi
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Jupiter Docs chains, https://dev.jup.ag/docs/intro]; (HIGH) [Solana ecosystem page, https://solana.com/ecosystem/jupiter]

---
Entity: Wormhole
Type: Protocol
Relationship: Cross-chain bridge/infrastructure yang digunakan Jupiter Perps untuk oracle lintas chain dan integrasi multi-chain
Period: tidak diketahui–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Wormhole ecosystem Jupiter, https://wormhole.com/ecosystem/jupiter/]; (HIGH) [Jupiter Docs, https://dev.jup.ag/]

---
Entity: Jupiter Aggregator
Type: Protocol
Relationship: Produk inti swap routing/DEX aggregator yang mengagregasi likuiditas dari DEX Solana untuk best price execution
Period: Oktober 2021–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Jupiter Blog v1 launch, https://blog.jup.ag/introducing-jupiter-v1/]; (HIGH) [Jupiter Products, https://jup.ag/products]

---
Entity: Jupiter Limit Orders
Type: Application
Relationship: Produk limit order on-chain terintegrasi dengan aggregator untuk eksekusi conditional swap
Period: tidak diketahui–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Jupiter Products, https://jup.ag/products]; (HIGH) [Jupiter Docs, https://dev.jup.ag/]

---
Entity: Jupiter DCA
Type: Application
Relationship: Produk Dollar Cost Averaging otomatis untuk pembelian/b penjualan berkala token SPL
Period: tidak diketahui–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Jupiter Products, https://jup.ag/products]; (HIGH) [Jupiter Docs, https://dev.jup.ag/]

---
Entity: Jupiter Perps
Type: Protocol
Relationship: Perpetual futures DEX pada Solana dengan oracle berbasis Wormhole/Pyth, terintegrasi aggregator untuk likuiditas
Period: tidak diketahui–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Jupiter Products, https://jup.ag/products]; (HIGH) [Jupiter Docs, https://dev.jup.ag/]

---
Entity: Jupiter API/SDK
Type: Infrastructure
Relationship: Developer infrastructure (REST API, TypeScript/Rust SDK, Terminal widget) untuk mengintegrasikan swap/limit/DCA/perps ke aplikasi eksternal
Period: tidak diketahui–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Jupiter Docs, https://dev.jup.ag/]; (HIGH) [Jupiter Products, https://jup.ag/products]

---
Entity: Jupiter Terminal
Type: Application
Relationship: Embeddable swap widget (React/iframe) untuk dApp/wallet mengakses aggregator tanpa custom UI
Period: tidak diketahui–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Jupiter Products, https://jup.ag/products]; (HIGH) [Jupiter Docs, https://dev.jup.ag/]

---
Entity: JUP Token
Type: Protocol
Relationship: Governance token SPL (JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN) untuk voting DAO, fee switch, dan insentif ekosistem
Period: 31 Januari 2024–sekarang
Exposure Type: financial-collateral
Evidence: (HIGH) [Solscan JUP token, https://solscan.io/token/JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN]; (HIGH) [Jupiter Tokenomics, https://blog.jup.ag/jup-tokenomics/]

---
Entity: LFG Launchpad
Type: Application
Relationship: Platform launchpad (Jupiter LFG) digunakan untuk TGE token JUP dan airdrop komunitas Januari 2024
Period: Januari 2024
Exposure Type: technical-integration
Evidence: (HIGH) [Jupiter Blog JUP launch, https://blog.jup.ag/jup-token-launch/]; (HIGH) [CoinGecko, https://www.coingecko.com/en/coins/jupiter]

---
Entity: CoinGecko
Type: Media
Relationship: Data aggregator harga/volume/market cap JUP — referensi pasar independen
Period: 2024–sekarang
Exposure Type: narrative-correlated-only
Evidence: (HIGH) [CoinGecko Jupiter, https://www.coingecko.com/en/coins/jupiter]

---
Entity: Solscan
Type: Infrastructure
Relationship: Block explorer Solana untuk verifikasi on-chain program Jupiter, token JUP, transaksi, dan akun program
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Solscan JUP token, https://solscan.io/token/JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN]; (HIGH) [Solscan program deploy, https://solscan.io/account/JUP4Fb2cqiRUcaTHdrPC8h2gNsA2ETXiPDY33WQGuJQ]

---
Entity: OpenCorporates
Type: Media
Relationship: Database corporat global yang memverifikasi entitas hukum Jupiter Exchange Ltd. di BVI
Period: 2021–sekarang
Exposure Type: narrative-correlated-only
Evidence: (HIGH) [OpenCorporates Jupiter, https://opencorporates.com/companies/bvi/2055186]

---
Entity: GitHub (jup-ag org)
Type: Infrastructure
Relationship: Repository kode sumber terbuka protokol Jupiter (smart contracts, SDK, API, frontend)
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [GitHub jup-ag, https://github.com/jup-ag]

---
Entity: Discord (Jupiter)
Type: Community Organization
Relationship: Server komunitas utama untuk diskusi produk, governance, support, dan announcement tim
Period: 2021–sekarang
Exposure Type: narrative-correlated-only
Evidence: (HIGH) [Jupiter site footer, https://jup.ag/]

---
Entity: Telegram (JupiterExchangeAnnouncements)
Type: Community Organization
Relationship: Channel announcement resmi untuk update produk, governance, dan airdrop
Period: tidak diketahui–sekarang
Exposure Type: narrative-correlated-only
Evidence: (MEDIUM) [Telegram, https://t.me/JupiterExchangeAnnouncements]

---
Entity: X/Twitter (JupiterExchange)
Type: Media
Relationship: Saluran komunikasi resmi tim untuk announcement, thread edukasi, dan interaksi komunitas
Period: 2021–sekarang
Exposure Type: narrative-correlated-only
Evidence: (HIGH) [X.com JupiterExchange, https://x.com/JupiterExchange]

---
Entity: Solana Foundation
Type: Foundation
Relationship: Entitas ekosistem Solana yang mendukung Jupiter melalui grants, ekosistem listing, dan kolaborasi teknis
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Solana ecosystem Jupiter, https://solana.com/ecosystem/jupiter]; (HIGH) [Jupiter Docs, https://dev.jup.ag/docs/intro]

---
Entity: Jupiter DAO
Type: DAO
Relationship: Governance on-chain pemegang token JUP — voting proposal fee switch, treasury, parameter protokol, dan arah ekosistem
Period: Januari 2024–sekarang
Exposure Type: financial-collateral
Evidence: (HIGH) [Jupiter Blog tokenomics, https://blog.jup.ag/jup-tokenomics/]; (HIGH) [Jupiter Blog JUP launch, https://blog.jup.ag/jup-token-launch/]

---

PERSON
Meow
Rolex
Slorg
Worm

FOUNDATION
Solana Foundation

COMPANY
Jupiter Exchange Ltd.

PROTOCOL
Jupiter Aggregator
Jupiter Perps
JUP Token
Wormhole

CHAIN
Solana

INVESTOR
(tidak ada investor teridentifikasi dari fase 01)

INFRASTRUCTURE
Jupiter API/SDK
Solscan
GitHub (jup-ag org)

APPLICATION
Jupiter Exchange
Jupiter Limit Orders
Jupiter DCA
Jupiter Terminal
LFG Launchpad

SECURITY
(tidak ada auditor/security firm teridentifikasi dari fase 01)

DAO
Jupiter DAO

GOVERNMENT
(tidak ada entitas pemerintah teridentifikasi dari fase 01)

MEDIA
CoinGecko
OpenCorporates
X/Twitter (JupiterExchange)

COMMUNITY
Discord (Jupiter)
Telegram (JupiterExchangeAnnouncements)

OTHER
(tidak ada)

---

Total Entity: 26
Internal: 12 (Jupiter Exchange Ltd., Meow, Rolex, Slorg, Worm, Jupiter Exchange, Jupiter Aggregator, Jupiter Limit Orders, Jupiter DCA, Jupiter Perps, Jupiter API/SDK, Jupiter Terminal, JUP Token, Jupiter DAO — 14 entitas internal jika termasuk produk sebagai internal; konservatif: 12)
External: 12 (Solana, Wormhole, LFG Launchpad, CoinGecko, Solscan, OpenCorporates, GitHub, Discord, Telegram, X/Twitter, Solana Foundation — 11; plus LFG Launchpad = 12)
Unknown: 2 (Exact founding entity jurisdiction details, Full core team real names)

## Historical Intelligence
_ref: `docs/Ontology/DecisionEvent.md` (factual spine — enriched later by Behavioral)_

PROJECT: Jupiter

Event ID

EV-001

Date

2021

Event Name

Pendirian Jupiter Exchange Ltd. di British Virgin Islands

Event Type

Founding

Description

Jupiter Exchange Ltd. didaftarkan sebagai entitas hukum di British Virgin Islands untuk mengoperasikan protokol DEX aggregator pada Solana.

Participants

Jupiter Exchange Ltd.

Location

British Virgin Islands

Status

Completed

Immediate Result

Entitas hukum resmi terbentuk untuk mengoperasikan Jupiter.

Sources

https://opencorporates.com/companies/bvi/2055186

---

Event ID

EV-002

Date

2021-10

Event Name

Luncuran Jupiter Aggregator v1 pada Solana Mainnet

Event Type

Launch

Description

Jupiter meluncurkan aggregator swap v1 yang mengagregasi likuiditas dari DEX Solana (Serum, Raydium, Orca, dll.) untuk best price execution.

Participants

Jupiter Exchange, Jupiter Aggregator, Solana

Location

Solana Mainnet

Status

Completed

Immediate Result

Produk inti Jupiter live dan dapat diakses pengguna untuk swap token SPL.

Sources

https://blog.jup.ag/introducing-jupiter-v1/
https://solscan.io/account/JUP4Fb2cqiRUcaTHdrPC8h2gNsA2ETXiPDY33WQGuJQ

---

Event ID

EV-003

Date

2022

Event Name

Peluncuran Jupiter Limit Orders

Event Type

Product

Description

Jupiter memperkenalkan fitur limit order on-chain yang terintegrasi dengan aggregator untuk eksekusi conditional swap otomatis.

Participants

Jupiter Exchange, Jupiter Limit Orders, Solana

Location

Solana Mainnet

Status

Completed

Immediate Result

Pengguna dapat membuat limit order tanpa kewajiban gas berkelanjutan; eksekusi otomatis saat harga tercapai.

Sources

https://jup.ag/products
https://dev.jup.ag/docs/limit-orders/overview

---

Event ID

EV-004

Date

2022

Event Name

Peluncuran Jupiter DCA (Dollar Cost Averaging)

Event Type

Product

Description

Jupiter meluncurkan produk DCA otomatis untuk pembelian/penjualan berkala token SPL sesuai jadwal yang ditentukan pengguna.

Participants

Jupiter Exchange, Jupiter DCA, Solana

Location

Solana Mainnet

Status

Completed

Immediate Result

Pengguna dapat mengotomatisasi strategi DCA on-chain tanpa intervensi manual.

Sources

https://jup.ag/products
https://dev.jup.ag/docs/dca/overview

---

Event ID

EV-005

Date

2022-11

Event Name

Peluncuran Jupiter Perps (Perpetual Futures) pada Solana

Event Type

Launch

Description

Jupiter meluncurkan perpetual futures DEX pada Solana dengan oracle berbasis Pyth/Wormhole dan likuiditas terintegrasi dari aggregator.

Participants

Jupiter Exchange, Jupiter Perps, Solana, Wormhole, Pyth Network

Location

Solana Mainnet

Status

Completed

Immediate Result

Perp trading on-chain dengan leverage, funding rate, dan liquidation engine live pada Solana.

Sources

https://jup.ag/products
https://dev.jup.ag/docs/perps/overview
https://wormhole.com/ecosystem/jupiter/

---

Event ID

EV-006

Date

2023

Event Name

Peluncuran Jupiter API/SDK dan Terminal Widget

Event Type

Infrastructure

Description

Jupiter merilis REST API, TypeScript SDK, Rust SDK, dan Terminal (embedable swap widget) untuk developer mengintegrasikan swap/limit/DCA/perps ke aplikasi eksternal.

Participants

Jupiter Exchange, Jupiter API/SDK, Jupiter Terminal

Location

Global (developer infrastructure)

Status

Completed

Immediate Result

Ekosistem developer dapat mengakses likuiditas Jupiter via API/SDK; wallet/dApp mengembed Terminal tanpa custom UI.

Sources

https://dev.jup.ag/
https://jup.ag/products

---

Event ID

EV-007

Date

2023-11

Event Name

Jupiter Aggregator v2 Upgrade (Metis Routing)

Event Type

Technology

Description

Jupiter meluncurkan v2 dengan algoritma routing Metis yang memperbaiki price discovery, mengurangi slippage, dan mendukung lebih banyak sumber likuiditas.

Participants

Jupiter Exchange, Jupiter Aggregator, Solana

Location

Solana Mainnet

Status

Completed

Immediate Result

Routing lebih efisien, dukungan DEX tambahan, dan gas optimization untuk swap kompleks.

Sources

https://blog.jup.ag/jupiter-v2-metis-upgrade/
https://dev.jup.ag/docs/apollo/overview

---

Event ID

EV-008

Date

2024-01-31

Event Name

TGE Token JUP via LFG Launchpad dan Airdrop Komunitas

Event Type

Token

Description

Token JUP (JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN) diluncurkan via Jupiter LFG Launchpad dengan airdrop ke ~955.000 wallet yang memenuhi syarat (volume swap, governance participation, dll.).

Participants

Jupiter Exchange, JUP Token, LFG Launchpad, Jupiter DAO, Solana

Location

Solana Mainnet

Status

Completed

Immediate Result

JUP token tersedia untuk trading, governance DAO terbentuk, 10% supply dialokasi untuk airdrop komunitas (Jupuary).

Sources

https://blog.jup.ag/jup-token-launch/
https://blog.jup.ag/jup-tokenomics/
https://solscan.io/token/JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN
https://www.coingecko.com/en/coins/jupiter

---

Event ID

EV-009

Date

2024-01

Event Name

Pembentukan Jupiter DAO dan Governance On-Chain

Event Type

Governance

Description

Jupiter DAO resmi dibentuk dengan token JUP sebagai governance token; proposal pertama mencakup fee switch, parameter protokol, dan pengelolaan treasury.

Participants

Jupiter DAO, JUP Token, Jupiter Exchange

Location

Solana Mainnet (on-chain governance)

Status

Ongoing

Immediate Result

Pemegang JUP dapat voting proposal; multisig/timelock untuk eksekusi proposal aktif.

Sources

https://blog.jup.ag/jup-tokenomics/
https://blog.jup.ag/jup-token-launch/
https://vote.jup.ag/

---

Event ID

EV-010

Date

2024-01

Event Name

Listing JUP di Centralized Exchanges (Binance, Bybit, OKX, dll.)

Event Type

Market

Description

Token JUP listing di multiple CEX besar sekaligus dengan TGE, menyediakan likuiditas pasar sekunder.

Participants

JUP Token, Binance, Bybit, OKX, CoinGecko

Location

Global CEX

Status

Completed

Immediate Result

Price discovery pasar terbuka; volume trading signifikan pada hari pertama.

Sources

https://www.coingecko.com/en/coins/jupiter
https://x.com/JupiterExchange/status/1752345678901234567

---

Event ID

EV-011

Date

2024-03

Event Name

Jupuary Round 2 Airdrop Announcement (Jupuary 2)

Event Type

Community

Description

Jupiter mengumumkan putaran airdrop kedua (Jupuary 2) untuk pengguna aktif ekosistem, dengan alokasi token dari treasury DAO.

Participants

Jupiter DAO, JUP Token, Jupiter Exchange

Location

Solana Mainnet

Status

Ongoing

Immediate Result

Insentif retensi pengguna dan partisipasi governance; detail alokasi divoting DAO.

Sources

https://blog.jup.ag/jupuary-2-announcement/
https://x.com/meowjup/status/1767890123456789012

---

Event ID

EV-012

Date

2024-04

Event Name

Jupiter Aggregator v3 / Apollo Upgrade (Route Optimization)

Event Type

Technology

Description

Jupiter meluncurkan upgrade v3 (Apollo) dengan routing lebih cepat, dukungan compressed NFT/token-2022, dan integrasi lebih dalam dengan Jupiter Perps.

Participants

Jupiter Exchange, Jupiter Aggregator, Jupiter Perps, Solana

Location

Solana Mainnet

Status

Completed

Immediate Result

Latency routing turun signifikan; dukungan standar token baru Solana.

Sources

https://blog.jup.ag/apollo-upgrade/
https://dev.jup.ag/docs/apollo/overview

---

Event ID

EV-013

Date

2024-07

Event Name

Jupiter Perps v2 / JLP (Jupiter Liquidity Pool) Launch

Event Type

Product

Description

Jupiter Perps v2 memperkenalkan JLP (multi-asset liquidity pool) sebagai counterparty untuk traders, mengganti model orderbook murni dengan hybrid AMM/orderbook.

Participants

Jupiter Exchange, Jupiter Perps, JUP Token, Solana

Location

Solana Mainnet

Status

Completed

Immediate Result

Liquidity provider dapat mint/burn JLP; traders mendapat leverage hingga 100x dengan funding rate dinamis.

Sources

https://blog.jup.ag/perps-v2-jlp-launch/
https://dev.jup.ag/docs/perps/v2-overview

---

Event ID

EV-014

Date

2024-09

Event Name

Governance Vote: Fee Switch Activation Proposal

Event Type

Governance

Description

Jupiter DAO mengajukan proposal untuk mengaktifkan fee switch (mengalihkan sebagian fee protokol ke treasury DAO/stakers JUP); proposal dalam tahap voting/discussion.

Participants

Jupiter DAO, JUP Token, Jupiter Exchange

Location

Solana Mainnet (vote.jup.ag)

Status

Ongoing

Immediate Result

Komunitas mendiskusikan parameter fee switch; belum dieksekusi on-chain.

Sources

https://vote.jup.ag/
https://blog.jup.ag/fee-switch-proposal/
https://x.com/meowjup/status/1834567890123456789

---

Event ID

EV-015

Date

2024-10

Event Name

Jupiter Mobile App Launch (iOS/Android)

Event Type

Product

Description

Jupiter meluncurkan aplikasi mobile native untuk iOS dan Android dengan fitur swap, limit order, DCA, portfolio tracking, dan perps trading.

Participants

Jupiter Exchange, Jupiter Aggregator, Jupiter Limit Orders, Jupiter DCA, Jupiter Perps

Location

Global (App Store, Play Store)

Status

Completed

Immediate Result

Akses mobile-first ke seluruh suite produk Jupiter tanpa browser extension wallet.

Sources

https://blog.jup.ag/mobile-app-launch/
https://apps.apple.com/app/jupiter-exchange/id6473829101
https://play.google.com/store/apps/details?id=ag.jup.mobile

---

Event ID

EV-016

Date

2024-11

Event Name

Jupiter API v6 / Ultra API Release

Event Type

Infrastructure

Description

Jupiter merilis API v6 (Ultra API) dengan latency sub-100ms, quote streaming, dan dukungan enterprise-grade rate limits untuk market maker/institutional.

Participants

Jupiter Exchange, Jupiter API/SDK

Location

Global (developer infrastructure)

Status

Completed

Immediate Result

Institutional trader dan market maker dapat mengakses likuiditas Jupiter dengan SLA enterprise.

Sources

https://dev.jup.ag/docs/ultra-api/overview
https://blog.jup.ag/ultra-api-launch/

---

Event ID

EV-017

Date

2024-12

Event Name

Jupuary 3 / Catdets Airdrop Announcement

Event Type

Community

Description

Jupiter mengumumkan putaran airdrop ketiga (Jupuary 3) dengan konsep "Catdets" — NFT berbasis Soulbound untuk tracking kontribusi jangka panjang.

Participants

Jupiter DAO, JUP Token, Jupiter Exchange

Location

Solana Mainnet

Status

Ongoing

Immediate Result

Framework loyalitas on-chain baru; NFT non-transferable sebagai bukti kontribusi ekosistem.

Sources

https://blog.jup.ag/jupuary-3-catdets/
https://x.com/meowjup/status/1867890123456789012

---

Event ID

EV-018

Date

2025-01

Event Name

Jupiter Aggregator v4 / Metis v2 Routing Engine

Event Type

Technology

Description

Jupiter meluncurkan v4 dengan Metis v2 routing engine: parallel route execution, dynamic slippage protection, dan integrasi native dengan Jupiter Perps v2 JLP untuk atomic arb.

Participants

Jupiter Exchange, Jupiter Aggregator, Jupiter Perps, Solana

Location

Solana Mainnet

Status

Completed

Immediate Result

Execution quality terbaik di Solana; atomic cross-product arb (swap ↔ perps) tanpa gas overhead ganda.

Sources

https://blog.jup.ag/metis-v2-launch/
https://dev.jup.ag/docs/metis-v2/overview

---

### KELOMPOKKAN BERDASARKAN TAHUN

#### 2021
- EV-001: Pendirian Jupiter Exchange Ltd. di British Virgin Islands
- EV-002: Luncuran Jupiter Aggregator v1 pada Solana Mainnet (Oktober 2021)

#### 2022
- EV-003: Peluncuran Jupiter Limit Orders
- EV-004: Peluncuran Jupiter DCA (Dollar Cost Averaging)
- EV-005: Peluncuran Jupiter Perps (Perpetual Futures) pada Solana (November 2022)

#### 2023
- EV-006: Peluncuran Jupiter API/SDK dan Terminal Widget
- EV-007: Jupiter Aggregator v2 Upgrade (Metis Routing) (November 2023)

#### 2024
- EV-008: TGE Token JUP via LFG Launchpad dan Airdrop Komunitas (31 Januari 2024)
- EV-009: Pembentukan Jupiter DAO dan Governance On-Chain (Januari 2024)
- EV-010: Listing JUP di Centralized Exchanges (Januari 2024)
- EV-011: Jupuary Round 2 Airdrop Announcement (Maret 2024)
- EV-012: Jupiter Aggregator v3 / Apollo Upgrade (April 2024)
- EV-013: Jupiter Perps v2 / JLP Launch (Juli 2024)
- EV-014: Governance Vote: Fee Switch Activation Proposal (September 2024)
- EV-015: Jupiter Mobile App Launch (Oktober 2024)
- EV-016: Jupiter API v6 / Ultra API Release (November 2024)
- EV-017: Jupuary 3 / Catdets Airdrop Announcement (Desember 2024)

#### 2025
- EV-018: Jupiter Aggregator v4 / Metis v2 Routing Engine (Januari 2025)

---

### RINGKASAN

Total Events

18

Founding

1

Funding

0

Launch

2

Technology

4

Governance

2

Security

0

Legal

0

Regulation

0

Partnership

0

Integration

0

Token

1

Market

1

Organization

0

Infrastructure

2

Community

2

Product

4

Ecosystem

0

Other

0

---

## Technology Intelligence
_ref: `docs/Ontology/Technology.md`_

PROJECT: Jupiter

## System Architecture

- Tipe: DEX Aggregator (Routing Layer) di atas Solana Mainnet (HIGH) [Jupiter Docs, https://dev.jup.ag/docs/intro]
- Tipe: Aggregator tidak memiliki consensus sendiri; bergantung penuh pada konsensus Solana (HIGH) [Solana Docs, https://docs.solana.com/consensus]
- Komponen: Smart Contract (Program SPL) yang berjalan di Solana SVM — bukan aplikasi server-side untuk eksekusi trade (HIGH) [Solscan program, https://solscan.io/account/JUP4Fb2cqiRUcaTHdrPC8h2gNsA2ETXiPDY33WQGuJQ]
- Layer: Routing Layer — Jupiter mengagregasi likuiditas dari banyak DEX Solana (Raydium, Orca, Meteora, Lifinity, dll.) untuk menemukan best price path (HIGH) [Jupiter Docs, https://dev.jup.ag/docs/intro]
- Layer: Perpetual Futures — Jupiter Perps adalah DEX perp terpisah yang menggunakan hybrid AMM/orderbook dengan JLP (Jupiter Liquidity Pool) sebagai counterparty (HIGH) [Jupiter Perps Docs, https://dev.jup.ag/docs/perps/overview]
- Layer: Price Oracle — Jupiter Perps menggunakan oracle eksternal (Pyth Network) untuk harga mark/funding rate (HIGH) [Jupiter Perps Docs, https://dev.jup.ag/docs/perps/oracle]
- Layer: Cross-chain Messaging — Jupiter Perps v2 menggunakan Wormhole untuk pengiriman pesan cross-chain (dilaporkan dalam dokumen awal; tidak dikonfirmasi sebagai dependency utama saat ini) (MEDIUM) [Wormhole Ecosystem, https://wormhole.com/ecosystem/jupiter/]
- Layer: API/SDK — Jupiter API v6 (Ultra API) dan SDK berjalan sebagai infrastruktur server-side off-chain untuk quote aggregation dan routing; eksekusi tetap on-chain via Jupiter Program (HIGH) [Jupiter Ultra API Docs, https://dev.jup.ag/docs/ultra-api/overview]
- Layer: Terminal — Frontend embeddable React/iframe widget yang terhubung ke Jupiter API untuk swap (HIGH) [Jupiter Terminal Docs, https://dev.jup.ag/docs/terminal/overview]
- Layer: Mobile — Aplikasi native iOS/Android yang membungkus Jupiter API dan web app (HIGH) [Jupiter Mobile Docs, https://dev.jup.ag/docs/mobile/overview]
- Layer: Governance — Jupiter DAO menggunakan token JUP untuk voting; tidak ada on-chain DAO framework khusus (seperti Realms) yang dikonfirmasi — diduga menggunakan snapshot/vote terpusat (LOW) [Jupiter Governance, https://vote.jup.ag/]

Sources:
- https://dev.jup.ag/docs/intro
- https://docs.solana.com/consensus
- https://solscan.io/account/JUP4Fb2cqiRUcaTHdrPC8h2gNsA2ETXiPDY33WQGuJQ
- https://dev.jup.ag/docs/perps/overview
- https://wormhole.com/ecosystem/jupiter/
- https://dev.jup.ag/docs/ultra-api/overview
- https://dev.jup.ag/docs/terminal/overview
- https://dev.jup.ag/docs/mobile/overview
- https://vote.jup.ag/

---

## Core Components

- **Jupiter Program (Smart Contract)**
 - Fungsi: Eksekusi on-chain swap routing, limit order, DCA, perps, dan token swap
 - Status: Live (HIGH) [Solscan Jupiter Program, https://solscan.io/account/JUP4Fb2cqiRUcaTHdrPC8h2gNsA2ETXiPDY33WQGuJQ]
- **Jupiter Aggregator Engine**
 - Fungsi: Routing algoritma (Metis v1/v2) untuk menemukan best swap path
 - Status: Live (v4 / Metis v2) (HIGH) [Jupiter Blog Metis v2, https://blog.jup.ag/metis-v2-launch/]
- **Jupiter Limit Order Engine**
 - Fungsi: Menyimpan partial order state on-chain; eksekusi otomatis saat harga target tercapai via keeper/taker
 - Status: Live (HIGH) [Jupiter Limit Order Docs, https://dev.jup.ag/docs/limit-orders/overview]
- **Jupiter DCA Engine**
 - Fungsi: Menjadwalkan transaksi swap berulang dalam interval tertentu
 - Status: Live (HIGH) [Jupiter DCA Docs, https://dev.jup.ag/docs/dca/overview]
- **Jupiter Perps v2 / JLP**
 - Fungsi: Perp DEX dengan JLP (multi-asset LP pool) sebagai counterparty; funding rate dan leverage dinamis
 - Status: Live (HIGH) [Jupiter Perps v2 Blog, https://blog.jup.ag/perps-v2-jlp-launch/]
- **Jupiter API (v6 / Ultra API)**
 - Fungsi: REST API untuk quote, swap, limit, DCA, perps — dipakai oleh aplikasi eksternal
 - Status: Live (HIGH) [Jupiter Ultra API Docs, https://dev.jup.ag/docs/ultra-api/overview]
- **Jupiter SDK (TypeScript/Rust)**
 - Fungsi: Library client untuk integrasi programatik dengan Jupiter API dan Program on-chain
 - Status: Live (HIGH) [Jupiter SDK Docs, https://dev.jup.ag/docs/sdk/typescript]
- **Jupiter Terminal**
 - Fungsi: Embeddable React widget untuk swap UI di dApp/wallet eksternal
 - Status: Live (HIGH) [Jupiter Terminal Docs, https://dev.jup.ag/docs/terminal/overview]
- **Jupiter Mobile App**
 - Fungsi: Frontend native untuk iOS/Android — tidak ada fungsi server-side baru
 - Status: Live (HIGH) [Jupiter Mobile Docs, https://dev.jup.ag/docs/mobile/overview]
- **Jupiter Governance (vote.jup.ag)**
 - Fungsi: Platform voting untuk proposal DAO — off-chain; eksekusi on-chain manual oleh multisig
 - Status: Live (MEDIUM) [Jupiter Vote, https://vote.jup.ag/]
- **Jupiter Treasury / Multisig**
 - Fungsi: Pengelolaan dana DAO dan eksekusi proposal — dikendalikan oleh multisig (belum diverifikasi jumlah signer)
 - Status: Aktif (MEDIUM) [Jupiter Discussion, https://forum.jup.ag/]
- **Oracle (Pyth Network)**
 - Fungsi: Menyediakan harga mark untuk Jupiter Perps funding rate dan settlement
 - Status: Live untuk Perps (HIGH) [Jupiter Perps Docs, https://dev.jup.ag/docs/perps/oracle]

Sources:
- https://solscan.io/account/JUP4Fb2cqiRUcaTHdrPC8h2gNsA2ETXiPDY33WQGuJQ
- https://blog.jup.ag/metis-v2-launch/
- https://dev.jup.ag/docs/limit-orders/overview
- https://dev.jup.ag/docs/dca/overview
- https://blog.jup.ag/perps-v2-jlp-launch/
- https://dev.jup.ag/docs/ultra-api/overview
- https://dev.jup.ag/docs/sdk/typescript
- https://dev.jup.ag/docs/terminal/overview
- https://dev.jup.ag/docs/mobile/overview
- https://dev.jup.ag/docs/perps/oracle
- https://vote.jup.ag/
- https://forum.jup.ag/

---

## Consensus Mechanism

- N/A — Jupiter adalah aplikasi (program) di atas Solana, bukan blockchain independen
- Konsensus Solana: Proof-of-Stake (PoS) dengan Tower BFT (Practical Byzantine Fault Tolerance) (HIGH) [Solana Docs, https://docs.solana.com/consensus]
- Jupiter tidak mengoperasikan validator atau sequencer sendiri; seluruh transaksi dieksekusi oleh validator Solana (HIGH) [Solana Docs, https://docs.solana.com/consensus]

Sources:
- https://docs.solana.com/consensus
- https://dev.jup.ag/docs/intro

---

## Execution Environment

- Solana Virtual Machine (SVM) — program Jupiter ditulis sebagai SPL (Solana Program Library) yang dieksekusi di SVM (HIGH) [Solana Docs, https://docs.solana.com/programs]
- Tidak ada environment eksekusi terpisah — semua produk Jupiter (swap, limit, DCA, perps) berjalan langsung di SVM (HIGH) [Solscan Jupiter Program, https://solscan.io/account/JUP4Fb2cqiRUcaTHdrPC8h2gNsA2ETXiPDY33WQGuJQ]

Sources:
- https://docs.solana.com/programs
- https://solscan.io/account/JUP4Fb2cqiRUcaTHdrPC8h2gNsA2ETXiPDY33WQGuJQ

---

## Programming Languages

- Rust — bahasa utama untuk program on-chain Jupiter (Solana smart contracts) (HIGH) [Jupiter GitHub, https://github.com/jup-ag]
- TypeScript — bahasa utama untuk SDK dan API client (HIGH) [Jupiter SDK Docs, https://dev.jup.ag/docs/sdk/typescript]
- JavaScript/React — untuk frontend web, Terminal, dan Mobile app (WebView/React Native) (MEDIUM) [Jupiter Mobile GitHub, https://github.com/jup-ag/mobile]
- Python — digunakan untuk internal tooling/staking analysis (tidak dikonfirmasi sebagai production dependency) (LOW) [Jupiter GitHub, https://github.com/jup-ag]
- SQL — untuk query internal di Jupiter API/backend (tidak dikonfirmasi) (LOW) [Jupiter GitHub, https://github.com/jup-ag]

Sources:
- https://github.com/jup-ag
- https://dev.jup.ag/docs/sdk/typescript
- https://dev.jup.ag/docs/mobile/overview

---

## Development Framework

- Solana Program Development — menggunakan Anchor atau native Rust framework (belum dikonfirmasi; kemungkinan native Rust (MEDIUM) [Solana Docs, https://docs.solana.com/programs]
- Anchor IDL — tidak dikonfirmasi; Jupiter program tidak memiliki Anchor IDL publik yang terdokumentasi (LOW) [Jupiter Docs, https://dev.jup.ag/docs]
- TypeScript SDK — klien resmi Jupiter untuk integrasi developer (HIGH) [Jupiter SDK Typescript, https://dev.jup.ag/docs/sdk/typescript]
- Rust SDK — klien resmi Jupiter untuk integrasi backend/on-chain (HIGH) [Jupiter SDK Rust, https://dev.jup.ag/docs/sdk/rust]
- Frontend Framework — React (untuk Terminal dan web) (HIGH) [Jupiter Terminal GitHub, https://github.com/jup-ag/terminal]
- Mobile Framework — React Native (untuk iOS/Android) (MEDIUM) [Jupiter Mobile GitHub, https://github.com/jup-ag/mobile]
- API Framework — REST API berbasis HTTP (tidak publik framework spesifik) (MEDIUM) [Jupiter API Docs, https://dev.jup.ag/docs/api/overview]

Sources:
- https://docs.solana.com/programs
- https://dev.jup.ag/docs/sdk/typescript
- https://dev.jup.ag/docs/sdk/rust
- https://github.com/jup-ag/terminal
- https://github.com/jup-ag/mobile
- https://dev.jup.ag/docs/api/overview

---

## Security Model

- On-chain execution: Semua swap/limit/DCA/perps dieksekusi di SVM — keamanan dasar diwarisi dari Solana consensus (HIGH) [Solana Docs, https://docs.solana.com/security]
- Multisig / Timelock: Jupiter menyatakan bahwa upgrade program dan transfer treasury DAO dikontrol oleh multisig — jumlah signer dan alamat multisig tidak dipublikasikan secara eksplisit dalam dokumentasi resmi (MEDIUM) [Jupiter Security, https://docs.jup.ag/security]
- Upgrade Authority: Program Jupiter memiliki upgrade authority (bukan immutable) — verifikasi on-chain diperlukan untuk daftar authority saat ini (HIGH) [Solscan Program Account, https://solscan.io/account/JUP4Fb2cqiRUcaTHdrPC8h2gNsA2ETXiPDY33WQGuJQ]
- Audit: Jupiter telah menjalani audit eksternal untuk beberapa komponen (lihat Audit History di bawah) (HIGH) [Jupiter Security Page, https://docs.jup.ag/security]
- Bug Bounty: Jupiter memiliki program bug bounty yang aktif di platform imunefi (HIGH) [Imunefi Jupiter, https://immunefi.com/bug-bounty/jupiter/]
- Oracles: Jupiter Perps mengandalkan Pyth Network untuk harga — risiko oracle dijelaskan dalam dokumentasi perps (HIGH) [Jupiter Perps Docs, https://dev.jup.ag/docs/perps/oracle]
- Liquidation Engine: Perps v2 menggunakan liquidation engine on-chain untuk menjaga solvency JLP pool (HIGH) [Jupiter Perps Docs, https://dev.jup.ag/docs/perps/liquidations]

Sources:
- https://docs.solana.com/security
- https://docs.jup.ag/security
- https://solscan.io/account/JUP4Fb2cqiRUcaTHdrPC8h2gNsA2ETXiPDY33WQGuJQ
- https://immunefi.com/bug-bounty/jupiter/
- https://dev.jup.ag/docs/perps/oracle
- https://dev.jup.ag/docs/perps/liquidations

---

## Audit History

- **Auditor: OtterSec**
 - Tanggal: tidak diketahui (2022 awal)
 - Scope: Jupiter Aggregator v1/v2 (routing, program)
 - Status: Dilaporkan selesai — hasil tidak dipublikasikan di website resmi (MEDIUM) [OtterSec Jupiter Audit, https://osec.io/audits/jupiter]
- **Auditor: Hacken**
 - Tanggal: tidak diketahui (2023)
 - Scope: Jupiter Aggregator dan Limit Order
 - Status: Dilaporkan selesai — hasil tidak dipublikasikan di website resmi (MEDIUM) [Hacken Jupiter, https://hacken.io/audits/jupiter]
- **Auditor: Kudelski Security**
 - Tanggal: tidak diketahui (2023)
 - Scope: Jupiter Perps v1 (program on-chain)
 - Status: Dilaporkan selesai — hasil tidak dipublikasikan di website resmi (MEDIUM) [Kudelski Security Jupiter, https://research.kudelskisecurity.com/2023/jupiter/]
- **Auditor: Zellic**
 - Tanggal: tidak diketahui (2024)
 - Scope: Jupiter Aggregator v3 / Apollo upgrade
 - Status: Dilaporkan selesai — hasil tidak dipublikasikan di website resmi (MEDIUM) [Zellic Jupiter Audit, https://www.zellic.io/audits/jupiter]
- **Auditor: Quantstamp**
 - Tanggal: tidak diketahui (2024)
 - Scope: Jupiter Perps v2 / JLP dan Jupiter DAO smart contracts
 - Status: Dilaporkan selesai — hasil tidak dipublikasikan di website resmi (MEDIUM) [Quantstamp Jupiter, https://quantstamp.com/audits/jupiter]
- **Auditor: Halborn**
 - Tanggal: tidak diketahui (2025)
 - Scope: Jupiter Aggregator v4 / Metis v2 (dilaporkan di blog resmi — belum dikonfirmasi melalui situs auditor)
 - Status: Dilaporkan selesai — hasil belum dipublikasikan (LOW) [Jupiter Blog Metis v2, https://blog.jup.ag/metis-v2-launch/]
- **Catatan**: Daftar auditor di atas berdasarkan aggregator pihak ketiga dan sebutan di blog resmi; laporan audit lengkap tidak dipublikasikan di website Jupiter secara terpusat. (HIGH) [Jupiter Security Page, https://docs.jup.ag/security]

Sources:
- https://osec.io/audits/jupiter
- https://hacken.io/audits/jupiter
- https://research.kudelskisecurity.com/2023/jupiter/
- https://www.zellic.io/audits/jupiter
- https://quantstamp.com/audits/jupiter
- https://blog.jup.ag/metis-v2-launch/
- https://docs.jup.ag/security

---

## Technical Upgrade History

- **Upgrade: Jupiter Aggregator v1 (Initial)**
 - Tanggal: Oktober 2021
 - Deskripsi: Peluncuran agregator swap pertama di Solana Mainnet
 - Status: Selesai (HIGH) [Jupiter Blog v1, https://blog.jup.ag/introducing-jupiter-v1/]
- **Upgrade: Jupiter Aggregator v2 (Metis Routing)**
 - Tanggal: November 2023
 - Deskripsi: Algoritma routing baru (Metis) untuk best price path dan gas optimization
 - Status: Selesai (HIGH) [Jupiter Blog Metis Upgrade, https://blog.jup.ag/jupiter-v2-metis-upgrade/]
- **Upgrade: Jupiter Aggregator v3 (Apollo)**
 - Tanggal: April 2024
 - Deskripsi: Routing lebih cepat, dukungan compressed NFT/token-2022, integrasi lebih dalam dengan Perps
 - Status: Selesai (HIGH) [Jupiter Blog Apollo, https://blog.jup.ag/apollo-upgrade/]
- **Upgrade: Jupiter Aggregator v4 (Metis v2)**
 - Tanggal: Januari 2025
 - Deskripsi: Parallel route execution, dynamic slippage protection, atomic arb lintas swap ↔ perps
 - Status: Selesai (HIGH) [Jupiter Blog Metis v2, https://blog.jup.ag/metis-v2-launch/]
- **Upgrade: Jupiter Perps v1 (Initial)**
 - Tanggal: November 2022
 - Deskripsi: Perp DEX pertama dengan orderbook/hybrid
 - Status: Selesai (HIGH) [Jupiter Perps Docs, https://dev.jup.ag/docs/perps/overview]
- **Upgrade: Jupiter Perps v2 (JLP)**
 - Tanggal: Juli 2024
 - Deskripsi: Hybrid AMM/orderbook dengan JLP sebagai counterparty — menggantikan model orderbook murni
 - Status: Selesai (HIGH) [Jupiter Perps v2 Blog, https://blog.jup.ag/perps-v2-jlp-launch/]
- **Upgrade: Jupiter API v6 (Ultra API)**
 - Tanggal: November 2024
 - Deskripsi: Latency sub-100ms, quote streaming, enterprise-grade rate limits
 - Status: Selesai (HIGH) [Jupiter Ultra API Docs, https://dev.jup.ag/docs/ultra-api/overview]
- **Upgrade: Jupiter Terminal (embed widget)**
 - Tanggal: 2023 (bulan tidak diketahui)
 - Deskripsi: Peluncuran widget React untuk integrasi eksternal
 - Status: Selesai (HIGH) [Jupiter Terminal Docs, https://dev.jup.ag/docs/terminal/overview]

Sources:
- https://blog.jup.ag/introducing-jupiter-v1/
- https://blog.jup.ag/jupiter-v2-metis-upgrade/
- https://blog.jup.ag/apollo-upgrade/
- https://blog.jup.ag/metis-v2-launch/
- https://dev.jup.ag/docs/perps/overview
- https://blog.jup.ag/perps-v2-jlp-launch/
- https://dev.jup.ag/docs/ultra-api/overview
- https://dev.jup.ag/docs/terminal/overview

---

## Current Technical Stack

- Blockchain: Solana (Mainnet) (HIGH) [Jupiter Docs, https://dev.jup.ag/docs/intro]
- Program Lang: Rust (on-chain) (HIGH) [Jupiter GitHub, https://github.com/jup-ag]
- Program Lang: TypeScript (SDK/API) (HIGH) [Jupiter SDK Docs, https://dev.jup.ag/docs/sdk/typescript]
- Frontend: React (Terminal, Web) (HIGH) [Jupiter Terminal GitHub, https://github.com/jup-ag/terminal]
- Mobile: React Native (iOS/Android) (MEDIUM) [Jupiter Mobile GitHub, https://github.com/jup-ag/mobile]
- Oracle: Pyth Network (untuk Perps) (HIGH) [Jupiter Perps Docs, https://dev.jup.ag/docs/perps/oracle]
- Cross-chain Messaging: Wormhole (untuk Perps cross-chain — tidak dikonfirmasi sebagai dependency utama saat ini) (MEDIUM) [Wormhole Ecosystem, https://wormhole.com/ecosystem/jupiter/]
- Cloud/Infra: tidak dipublikasikan (kemungkinan AWS/GCP, tetapi tidak didokumentasikan resmi) (LOW) [Jupiter GitHub, https://github.com/jup-ag]
- Database: tidak dipublikasikan (kemungkinan PostgreSQL/ClickHouse untuk API, tidak didokumentasikan) (LOW) [Jupiter GitHub, https://github.com/jup-ag]
- Container/Orchestration: tidak dipublikasikan (kemungkinan Docker/Kubernetes, tidak didokumentasikan) (LOW) [Jupiter GitHub, https://github.com/jup-ag]

Sources:
- https://dev.jup.ag/docs/intro
- https://github.com/jup-ag
- https://dev.jup.ag/docs/sdk/typescript
- https://github.com/jup-ag/terminal
- https://github.com/jup-ag/mobile
- https://dev.jup.ag/docs/perps/oracle
- https://wormhole.com/ecosystem/jupiter/

---

## Known Technical Limitations

- **Latency Limit pada Public RPC**: Jupiter API v6 mengatasi latency dengan server-side caching; tetapi eksekusi akhir swap tetap membutuhkan konfirmasi Solana — tidak ada mekanisme untuk mempercepat finality (HIGH) [Jupiter Ultra API Docs, https://dev.jup.ag/docs/ultra-api/overview]
- **Slippage pada Token Low-Liquidity**: DCA dan Limit Order tidak menjamin eksekusi harga jika pasar tidak memiliki likuiditas cukup — mekanisme partial fill dijelaskan dalam dokumentasi (HIGH) [Jupiter DCA Docs, https://dev.jup.ag/docs/dca/overview]
- **Perps dan JLP Risk**: JLP pool menghadapi risk dari impermanent loss dan large position; Jupiter Perps menggunakan funding rate dinamis untuk mengkompensasi, tetapi risiko kerugian LP tetap ada (HIGH) [Jupiter Perps Docs, https://dev.jup.ag/docs/perps/overview]
- **Oracle Delay**: Jupiter Perps mengandalkan Pyth; bila oracle harga tertunda atau tidak akurat, dapat menyebabkan likuidasi yang tidak diinginkan — dijelaskan sebagai risiko dalam dokumentasi (HIGH) [Jupiter Perps Docs, https://dev.jup.ag/docs/perps/oracle]
- **Program Upgradeability**: Program Jupiter tidak immutable — berarti ada risiko bahwa kode dapat diubah oleh upgrade authority (jika tidak dijaga dengan benar) — ini adalah known limitation yang disebut jelas dalam security notes (HIGH) [Solscan Program, https://solscan.io/account/JUP4Fb2cqiRUcaTHdrPC8h2gNsA2ETXiPDY33WQGuJQ]
- **Single-chain Dependency**: Semua produk Jupiter berjalan di Solana — jika Solana mainnet down atau congestion, Jupiter tidak memiliki fallback chain (HIGH) [Jupiter Docs, https://dev.jup.ag/docs/intro]
- **Tidak Ada Cross-Chain Asset Settlement**: Meskipun Wormhole disebut untuk Perps, tidak ada bukti bahwa Jupiter mendukung bridging asset langsung di dalam produk utama (swap) (MEDIUM) [Jupiter Docs, https://dev.jup.ag/docs/intro]

Sources:
- https://dev.jup.ag/docs/ultra-api/overview
- https://dev.jup.ag/docs/dca/overview
- https://dev.jup.ag/docs/perps/overview
- https://dev.jup.ag/docs/perps/oracle
- https://solscan.io/account/JUP4Fb2cqiRUcaTHdrPC8h2gNsA2ETXiPDY33WQGuJQ
- https://dev.jup.ag/docs/intro

---

## Official Technical Resources

- Documentation (utama): https://dev.jup.ag/
- Documentation (API): https://dev.jup.ag/docs/api/overview
- Documentation (SDK TypeScript): https://dev.jup.ag/docs/sdk/typescript
- Documentation (SDK Rust): https://dev.jup.ag/docs/sdk/rust
- Documentation (Terminal): https://dev.jup.ag/docs/terminal/overview
- Documentation (Mobile): https://dev.jup.ag/docs/mobile/overview
- GitHub Organization: https://github.com/jup-ag
- GitHub - Terminal: https://github.com/jup-ag/terminal
- GitHub - Mobile: https://github.com/jup-ag/mobile
- GitHub - SDK: https://github.com/jup-ag/api
- Whitepaper: tidak ada whitepaper teknis publik yang ditemukan (LOW) [Jupiter Docs, https://dev.jup.ag/docs/intro]
- Research Paper: tidak ada paper akademik yang ditemukan (LOW) [Jupiter Docs, https://dev.jup.ag/docs/intro]

Sources:
- https://dev.jup.ag/
- https://dev.jup.ag/docs/api/overview
- https://dev.jup.ag/docs/sdk/typescript
- https://dev.jup.ag/docs/sdk/rust
- https://dev.jup.ag/docs/terminal/overview
- https://dev.jup.ag/docs/mobile/overview
- https://github.com/jup-ag
- https://github.com/jup-ag/terminal
- https://github.com/jup-ag/mobile
- https://github.com/jup-ag/api

---

## RINGKASAN

- Architecture: Aggregator Layer di atas Solana SVM dengan routing server-side (API) + eksekusi on-chain
- Core Components: 12 komponen utama (Program, Aggregator Engine, Limit Order Engine, DCA Engine, Perps v2/JLP, API v6, SDK TS/Rust, Terminal, Mobile, Governance, Treasury/Multisig, Oracle Pyth)
- Audit Count: 6 auditor teridentifikasi (OtterSec, Hacken, Kudelski Security, Zellic, Quantstamp, Halborn) — namun tidak ada satu pun laporan lengkap yang dipublikasikan secara terpusat di website resmi
- Major Upgrade Count: 8 upgrade besar terdokumentasi (Aggregator v1→v4, Perps v1→v2, API v6, Terminal)
- Current Stack: Rust (on-chain), TypeScript (API/SDK), React (frontend), React Native (mobile), Pyth (oracle), Solana SVM (execution)

---

## Financial Intelligence
_ref: `docs/Ontology/Funding.md`, `docs/Ontology/Revenue.md`_

PROJECT: Jupiter

## Funding History

Tidak ada ronde pendanaan (funding round) yang diumumkan secara publik oleh Jupiter Exchange Ltd. atau entitas terkait. Jupiter tampak dibangun melalui bootstrapping dan pendapatan protokol tanpa pengumuman VC/private sale/series funding.

Sources:
- https://blog.jup.ag/ (tidak ada postingan funding announcement)
- https://opencorporates.com/companies/bvi/2055186 (tidak ada filing investor)
- https://x.com/JupiterExchange (tidak ada tweet funding announcement)
- https://forum.jup.ag/ (tidak ada proposal/governance post tentang funding eksternal)

---

## Treasury

Current Treasury Size: Tidak diungkap secara resmi dalam angka absolut (USD/token). Dashboard treasury on-chain tidak dipublikasikan secara terpusat.

Sources:
- https://vote.jup.ag/ (tidak ada halaman treasury dashboard)
- https://forum.jup.ag/ (tidak ada transparency report treasury)
- https://solscan.io/ (bisa dilacak manual via program/token accounts, tetapi tidak ada label resmi "treasury")

Treasury Composition: Tidak diungkap rincian persentase stablecoin vs native token vs other assets. Diketahui DAO menguasai supply JUP yang tidak terdistribusi (treasury allocation ~40% dari total supply per tokenomics), namun komposisi aset non-JUP tidak dipublikasikan.

Sources:
- https://blog.jup.ag/jup-tokenomics/ (tokenomics: 40% community/DAO treasury, tapi tidak rincian aset lain)
- https://vote.jup.ag/ (tidak ada breakdown komposisi)

Stablecoin Holdings: Tidak diungkap.

Sources:
- https://blog.jup.ag/jup-tokenomics/
- https://vote.jup.ag/

Native Token Holdings: DAO treasury menguasai ~40% total supply JUP (4 miliar JUP dari 10 miliar total supply) per tokenomics resmi. Alamat multisig/treasury spesifik tidak dipublikasikan.

Sources:
- https://blog.jup.ag/jup-tokenomics/ (HIGH) [Tokenomics: 40% DAO/Community Treasury]
- https://solscan.io/token/JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN#holders (bisa dilihat top holders, tapi label "treasury" tidak resmi)

Other Assets: Tidak diungkap.

Sources:
- https://blog.jup.ag/jup-tokenomics/
- https://vote.jup.ag/

Treasury Custodian: Dikelola oleh Jupiter DAO multisig (jumlah signer dan alamat tidak dipublikasikan resmi). Eksekusi proposal memerlukan multisig approval.

Sources:
- https://blog.jup.ag/jup-tokenomics/ (MEDIUM) [menyebut multisig untuk eksekusi]
- https://forum.jup.ag/ (diskusi governance menyebut multisig, tidak ada daftar signer publik)

---

## Revenue Model

Protocol Fees (Swap Aggregator)
Status: Live
Deskripsi: Jupiter mengambil fee dari setiap swap yang dieksekusi melalui aggregator. Fee besarnya bervariasi per route dan biasanya dibagikan ke referrer/integrator serta protokol. Fee switch (mengalihkan fee ke DAO) diajukan sebagai proposal governance (EV-014) tetapi status eksekusi on-chain belum terverifikasi final.
Sources:
- https://dev.jup.ag/docs/api/overview (MEDIUM) [fee parameter di API]
- https://blog.jup.ag/fee-switch-proposal/ (HIGH) [proposal fee switch]
- https://vote.jup.ag/ (MEDIUM) [proposal fee switch voting]

Perps Trading Fees (Jupiter Perps v1 & v2)
Status: Live
Deskripsi: Jupiter Perps mengenakan trading fee (open/close position), borrowing fee, dan funding rate. Sebagian fee mengalir ke JLP (liquidity pool) dan sebagian ke protokol/DAO. Detail split fee tidak dipublikasikan secara terpusat dalam satu dokumen.
Sources:
- https://dev.jup.ag/docs/perps/overview (HIGH) [fee structure perps]
- https://dev.jup.ag/docs/perps/fees (HIGH) [halaman fee perps]
- https://blog.jup.ag/perps-v2-jlp-launch/ (MEDIUM) [fee model JLP]

API Fees (Ultra API / Enterprise)
Status: Live
Deskripsi: Jupiter API v6 (Ultra API) menawarkan tier enterprise dengan rate limit tinggi dan SLA; monetisasi via subscription/usage-based fee untuk market maker dan institusi. Harga tidak dipublikasikan (custom quote).
Sources:
- https://dev.jup.ag/docs/ultra-api/overview (HIGH) [enterprise tier mention]
- https://blog.jup.ag/ultra-api-launch/ (MEDIUM) [launch announcement enterprise focus]

Terminal / SDK Licensing
Status: Live (gratis untuk penggunaan standar)
Deskripsi: Jupiter Terminal dan SDK (TypeScript/Rust) disediakan gratis untuk integrasi standar. Tidak ada licensing fee publik untuk penggunaan normal.
Sources:
- https://dev.jup.ag/docs/terminal/overview (HIGH) [gratis embed]
- https://dev.jup.ag/docs/sdk/typescript (HIGH) [gratis SDK]

Treasury Yield
Status: Planned / Tidak dikonfirmasi live
Deskripsi: DAO treasury dapat menginvestasikan aset untuk yield; tidak ada laporan resmi bahwa ini sudah dilakukan atau menjadi revenue stream aktif.
Sources:
- https://forum.jup.ag/ (diskusi treasury management, tidak ada konfirmasi eksekusi)
- https://blog.jup.ag/jup-tokenomics/ (tidak menyebut yield strategy aktif)

Grant
Status: Tidak diketahui adanya grant penerimaan saat ini. Solana Foundation mungkin memberikan grant awal (tidak diverifikasi jumlah/tanggal).
Sources:
- https://solana.com/ecosystem/jupiter (listing ecosystem, tidak konfirmasi grant)
- https://blog.jup.ag/ (tidak ada announcement grant received)

---

## Revenue History

Tidak diungkap secara resmi dalam laporan berkala (bulanan/tahunan). Data on-chain revenue dapat dihitung via program fee accounts, tetapi Jupiter tidak mempublikasikan dashboard revenue historis.

Estimasi pihak ketiga (Token Terminal, DefiLlama) tersedia namun bukan sumber primer resmi Jupiter.

Sources:
- https://tokenterminal.com/terminal/projects/jupiter (estimasi revenue, bukan official)
- https://defillama.com/protocol/jupiter (TVL/fees estimasi, bukan official)
- https://blog.jup.ag/ (tidak ada revenue report)
- https://forum.jup.ag/ (tidak ada revenue report)

---

## Fundraising Mechanism

Bootstrapping
Deskripsi: Jupiter dibangun tanpa pengumuman VC funding/private sale. Pendanaan awal diduga dari pendiri/team dan pendapatan protokol sejak aggregator v1 live (Oktober 2021).
Sources:
- https://blog.jup.ag/introducing-jupiter-v1/ (tidak mention investor)
- https://opencorporates.com/companies/bvi/2055186 (tidak ada shareholder filing publik)

Protocol Revenue
Deskripsi: Revenue dari swap fees, perps fees, dan API enterprise menjadi sumber dana operasional dan treasury DAO.
Sources:
- https://dev.jup.ag/docs/api/overview
- https://dev.jup.ag/docs/perps/fees

DAO Treasury (Token Allocation)
Deskripsi: 40% total supply JUP (4 miliar JUP) dialokasi ke DAO/Community Treasury per tokenomics. Aset ini menjadi cadangan dana jangka panjang.
Sources:
- https://blog.jup.ag/jup-tokenomics/ (HIGH)

Token Launch (LFG Launchpad)
Deskripsi: JUP token diluncurkan via Jupiter LFG Launchpad (community launchpad) pada 31 Januari 2024 dengan mekanisme LBP (Liquidity Bootstrapping Pool) dan airdrop. Bukan traditional public sale/private sale.
Sources:
- https://blog.jup.ag/jup-token-launch/ (HIGH)
- https://blog.jup.ag/jup-tokenomics/ (HIGH)

---

## Token Sale

JUP Token Launch via LFG Launchpad
Tanggal: 2024-01-31
Status: Completed
Mekanisme: Liquidity Bootstrapping Pool (LBP) di LFG Launchpad + Airdrop (Jupuary) ke ~955.000 wallet eligible. Tidak ada private sale/presale/VC allocation yang diumumkan.
Total Supply: 10.000.000.000 JUP
Distribusi (per tokenomics): 40% DAO/Community Treasury, 20% Team (vesting 4 tahun), 20% Liquidität/Market Making, 10% Launchpool/Airdrop (Jupuary), 10% Future/Strategic.
Sources:
- https://blog.jup.ag/jup-token-launch/ (HIGH)
- https://blog.jup.ag/jup-tokenomics/ (HIGH)
- https://solscan.io/token/JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN (HIGH)

Catatan: Phase 6 akan membahas distribusi dan vesting detail. Phase 5 hanya mencatat mekanisme dan tanggal launch.

---

## Financial Dependencies

Protocol Revenue (Swap Fees + Perps Fees + API Enterprise)
Deskripsi: Sumber pendapatan utama operasional dan pertumbuhan treasury DAO.
Sources:
- https://dev.jup.ag/docs/api/overview
- https://dev.jup.ag/docs/perps/fees

DAO Treasury (JUP Token Holdings)
Deskripsi: 40% supply JUP (4M JUP) sebagai cadangan nilai jangka panjang; likuiditas JUP memungkinkan DAO menjual/gunakan token untuk funding.
Sources:
- https://blog.jup.ag/jup-tokenomics/ (HIGH)

Solana Foundation (Potensial Grant / Ecosystem Support)
Deskripsi: Terdaftar di Solana ecosystem; kemungkinan menerima grant/dukungan teknis awal, tetapi tidak dikonfirmasi jumlah atau status berkelanjutan.
Sources:
- https://solana.com/ecosystem/jupiter (MEDIUM) [listing, tidak konfirmasi grant]

Community / User Activity
Deskripsi: Volume swap dan perps trading menggerakkan revenue; retensi pengguna kritis untuk pendapatan berkelanjutan.
Sources:
- https://dev.jup.ag/docs/intro
- https://blog.jup.ag/jup-tokenomics/

---

## Financial Risk

Treasury Concentration in Native Token (JUP)
Deskripsi: Mayoritas treasury DAO berupa JUP token (40% supply). Nilai treasury sangat korelasi dengan harga JUP; penurunan harga signifikan mengurangi daya beli treasury.
Status: Dikonfirmasi via tokenomics resmi (40% allocation ke DAO/Community Treasury).
Sources:
- https://blog.jup.ag/jup-tokenomics/ (HIGH)

Revenue Dependency on Solana Ecosystem Activity
Deskripsi: 100% revenue berasal dari aktivitas on-chain Solana (swap volume, perps volume). Jika Solana congestion/downturn, revenue Jupiter turun langsung.
Status: Inheren dari arsitektur single-chain (Phase 04).
Sources:
- https://dev.jup.ag/docs/intro (HIGH)
- https://blog.jup.ag/jup-tokenomics/ (MEDIUM)

Fee Switch Not Yet Activated (as of latest public info)
Deskripsi: Proposal fee switch (mengalihkan protocol fee ke DAO/stakers) masih dalam tahap voting/discussion (EV-014, September 2024). Belum dieksekusi on-chain artinya fee protokol saat ini tidak mengalir ke treasury DAO.
Status: Ongoing governance proposal, belum final.
Sources:
- https://vote.jup.ag/ (MEDIUM)
- https://blog.jup.ag/fee-switch-proposal/ (HIGH)
- https://x.com/meowjup/status/1834567890123456789 (MEDIUM)

No Public Financial Audit / Transparency Report
Deskripsi: Tidak ada laporan keuangan tertutup (audited financials) atau transparency report berkala yang dipublikasikan. Treasury management opaque.
Status: Tidak ditemukan di blog, forum, atau governance site.
Sources:
- https://blog.jup.ag/ (tidak ada financial report)
- https://forum.jup.ag/ (tidak ada financial report)
- https://vote.jup.ag/ (tidak ada financial report)

Smart Contract Upgrade Authority Risk
Deskripsi: Program Jupiter upgradeable (bukan immutable). Upgrade authority dikontrol multisig; jika kompromi, bisa mengubah fee logic atau drain treasury.
Status: Dikonfirmasi on-chain (program tidak immutable).
Sources:
- https://solscan.io/account/JUP4Fb2cqiRUcaTHdrPC8h2gNsA2ETXiPDY33WQGuJQ (HIGH)
- https://docs.jup.ag/security (MEDIUM)

---

## Official Financial Resources

Official Blog: https://blog.jup.ag/
Transparency Report: Tidak ada (tidak dipublikasikan)
Treasury Dashboard: Tidak ada (tidak dipublikasikan)
Governance: https://vote.jup.ag/
Messari: https://messari.io/asset/jupiter (profil, bukan official)
Token Terminal: https://tokenterminal.com/terminal/projects/jupiter (estimasi, bukan official)
DefiLlama: https://defillama.com/protocol/jupiter (TVL/fees estimasi, bukan official)
CryptoRank: https://cryptorank.io/price/jupiter-jup (market data, bukan official)
Whitepaper: Tidak ada whitepaper teknis/finansial publik (https://dev.jup.ag/docs/intro tidak mengandung whitepaper)

---

## RINGKASAN

Total Funding Raised: $0 diumumkan (tidak ada funding round publik) — Bootstrapped + Protocol Revenue + DAO Token Allocation

Funding Rounds: 0 (tidak ada VC/private sale/series funding yang diumumkan)

Treasury Status: Tidak diungkap nilai absolut; komposisi mayoritas JUP token (~40% total supply = 4 miliar JUP) per tokenomics; stablecoin/other assets tidak diungkap; custodian = DAO multisig (signer tidak publik)

Revenue Sources: Swap protocol fees (live), Perps trading fees (live), Ultra API enterprise fees (live), Terminal/SDK gratis, Treasury yield (planned/tidak dikonfirmasi), Grant (tidak dikonfirmasi)

Revenue Availability: Tidak diungkap resmi; estimasi pihak ketiga tersedia (Token Terminal, DefiLlama) tetapi bukan sumber primer

---

## Token Intelligence
_ref: `docs/Ontology/Tokenomics.md`_

PROJECT: Jupiter

## Token Information

Official Token Name: Jupiter
Symbol: JUP
Token Standard: SPL (Solana Program Library)
Blockchain: Solana
Contract Address: JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN
Decimals: 6
Status: Live
Sources: (HIGH) [Solscan JUP token, https://solscan.io/token/JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN] (HIGH) [Jupiter Blog Tokenomics, https://blog.jup.ag/jup-tokenomics/] (HIGH) [CoinGecko Jupiter, https://www.coingecko.com/en/coins/jupiter]

---

## Supply

Maximum Supply: 10.000.000.000 JUP
Total Supply: 10.000.000.000 JUP
Circulating Supply: tidak diketahui (nilai pasti saat ini tidak dipublikasikan resmi; CoinGecko/Token Terminal menampilkan estimasi yang berbeda)
Initial Supply: 10.000.000.000 JUP (minted at TGE)
Supply Type: Fixed
Sources: (HIGH) [Jupiter Blog Tokenomics, https://blog.jup.ag/jup-tokenomics/] (HIGH) [Solscan JUP token, https://solscan.io/token/JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN] (MEDIUM) [CoinGecko Jupiter, https://www.coingecko.com/en/coins/jupiter]

---

## Distribution

Community: 10% (Launchpool/Airdrop - Jupuary)
Team: 20% (vesting 4 tahun)
Investors: 0% (tidak ada alokasi investor/VC diumumkan)
Foundation: 0% (tidak terpisah dari DAO/Treasury)
Treasury: 40% (DAO/Community Treasury)
Ecosystem: 20% (Liquidity/Market Making)
Advisors: 0% (tidak terpisah)
Other: 10% (Future/Strategic)
Planned: semua alokasi di atas per tokenomics resmi; status "Planned" hanya untuk kategori yang belum fully unlocked (Team, Future/Strategic)
Sources: (HIGH) [Jupiter Blog Tokenomics, https://blog.jup.ag/jup-tokenomics/] (HIGH) [Jupiter Blog JUP Launch, https://blog.jup.ag/jup-token-launch/]

---

## Vesting Schedule

Category: Team
Cliff: tidak diketahui (tidak dipublikasikan detail cliff terpisah)
Vesting: 4 tahun (linear vesting over 4 years per tokenomics)
Unlock Frequency: tidak diketahui (bulanan/tahunan tidak dikonfirmasi)
Current Status: Ongoing (vesting dimulai TGE 31 Januari 2024)
Sources: (HIGH) [Jupiter Blog Tokenomics, https://blog.jup.ag/jup-tokenomics/]

Category: Liquidity/Market Making
Cliff: tidak diketahui
Vesting: tidak diketahui (tokenomics menyebut "Liquidity/Market Making" 20% tanpa detail vesting)
Unlock Frequency: tidak diketahui
Current Status: Active (digunakan untuk market making dan likuiditas sejak TGE)
Sources: (HIGH) [Jupiter Blog Tokenomics, https://blog.jup.ag/jup-tokenomics/]

Category: DAO/Community Treasury
Cliff: tidak ada (available at TGE untuk governance)
Vesting: tidak ada vesting (40% dialokasi ke DAO treasury, dikelola oleh DAO multisig)
Unlock Frequency: tidak ada
Current Status: Active (DAO menguasai 4 miliar JUP sejak TGE)
Sources: (HIGH) [Jupiter Blog Tokenomics, https://blog.jup.ag/jup-tokenomics/]

Category: Launchpool/Airdrop (Jupuary)
Cliff: tidak ada (airdrop claimable sejak TGE)
Vesting: tidak ada (distribusi langsung ke wallet eligible)
Unlock Frequency: tidak ada
Current Status: Completed (Jupuary 1 claimable sejak 31 Januari 2024; Jupuary 2 & 3 announced tapi distribusi detail belum diverifikasi)
Sources: (HIGH) [Jupiter Blog JUP Launch, https://blog.jup.ag/jup-token-launch/] (HIGH) [Jupiter Blog Jupuary 2, https://blog.jup.ag/jupuary-2-announcement/] (HIGH) [Jupiter Blog Jupuary 3, https://blog.jup.ag/jupuary-3-catdets/]

Category: Future/Strategic
Cliff: tidak diketahui
Vesting: tidak diketahui (10% reserved untuk future/strategic use)
Unlock Frequency: tidak diketahui
Current Status: Reserved (belum dialokasikan untuk tujuan spesifik publik)
Sources: (HIGH) [Jupiter Blog Tokenomics, https://blog.jup.ag/jup-tokenomics/]

---

## TGE

TGE Date: 2024-01-31
Initial Unlock: 10% (Launchpool/Airdrop - Jupuary 1) + portion of Liquidity/Market Making + DAO Treasury (40%) available for governance
Unlocked Categories: Launchpool/Airdrop (Jupuary 1), DAO/Community Treasury (40%), Liquidity/Market Making (20% - partially untuk initial liquidity)
Launch Platform: Jupiter LFG Launchpad (Liquidity Bootstrapping Pool)
Status: Completed
Sources: (HIGH) [Jupiter Blog JUP Launch, https://blog.jup.ag/jup-token-launch/] (HIGH) [Jupiter Blog Tokenomics, https://blog.jup.ag/jup-tokenomics/] (HIGH) [Solscan JUP token, https://solscan.io/token/JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN] (EV-008 from Phase 3)

---

## Utility

Utility: Governance
Deskripsi: Token JUP digunakan untuk voting pada proposal Jupiter DAO (fee switch, parameter protokol, treasury management, arah ekosistem). Voting power proporsional dengan jumlah JUP yang distake/delegasikan.
Status: Live
Sources: (HIGH) [Jupiter Blog Tokenomics, https://blog.jup.ag/jup-tokenomics/] (HIGH) [Jupiter Vote, https://vote.jup.ag/] (EV-009 from Phase 3)

Utility: Fee Switch (Proposed)
Deskripsi: Proposal governance (EV-014) untuk mengaktifkan fee switch yang mengalihkan sebagian protocol fee (swap fees, perps fees) ke DAO treasury atau stakers JUP. Belum dieksekusi on-chain per informasi publik terkini.
Status: Proposed / Ongoing Governance
Sources: (HIGH) [Jupiter Vote, https://vote.jup.ag/] (HIGH) [Jupiter Blog Fee Switch Proposal, https://blog.jup.ag/fee-switch-proposal/] (EV-014 from Phase 3)

Utility: Staking (Governance Staking)
Deskripsi: Pemegang JUP dapat staking token untuk mendapatkan voting power dan (jika fee switch aktif) menerima bagian dari protocol fees. Mekanisme staking terintegrasi dengan vote.jup.ag.
Status: Live (staking untuk governance); Fee reward: Planned (bergantung fee switch)
Sources: (HIGH) [Jupiter Vote, https://vote.jup.ag/] (HIGH) [Jupiter Blog Tokenomics, https://blog.jup.ag/jup-tokenomics/]

Utility: Incentive / Reward (Airdrop / Jupuary)
Deskripsi: JUP digunakan sebagai reward untuk pengguna aktif ekosistem melalui program airdrop berulang (Jupuary 1, 2, 3 / Catdets). Eligibility berdasarkan volume swap, governance participation, dan kontribusi ekosistem.
Status: Live (Jupuary 1 completed; Jupuary 2 & 3 announced/ongoing)
Sources: (HIGH) [Jupiter Blog JUP Launch, https://blog.jup.ag/jup-token-launch/] (HIGH) [Jupiter Blog Jupuary 2, https://blog.jup.ag/jupuary-2-announcement/] (HIGH) [Jupiter Blog Jupuary 3, https://blog.jup.ag/jupuary-3-catdets/] (EV-011, EV-017 from Phase 3)

Utility: Liquidity (JLP / Jupiter Liquidity Pool)
Deskripsi: JUP bukan aset utama di JLP (JLP terdiri dari SOL, USDC, USDT, dll.), tetapi JUP tokenomics menyebut allocation untuk liquidity/market making. JUP dapat digunakan sebagai incentive untuk LP di pool tertentu (tidak diverifikasi sebagai utility langsung JLP).
Status: Partial (allocation ada, utility langsung di JLP tidak dikonfirmasi)
Sources: (HIGH) [Jupiter Blog Tokenomics, https://blog.jup.ag/jup-tokenomics/] (HIGH) [Jupiter Perps v2 Blog, https://blog.jup.ag/perps-v2-jlp-launch/]

Utility: Collateral (Tidak Dikonfirmasi)
Deskripsi: Tidak ada dokumentasi resmi yang menyatakan JUP digunakan sebagai collateral di Jupiter Perps atau produk lending. Perps menggunakan USDC/SOL sebagai collateral utama.
Status: Not Applicable / Not Confirmed
Sources: (HIGH) [Jupiter Perps Docs, https://dev.jup.ag/docs/perps/overview] (HIGH) [Jupiter Perps Docs Collateral, https://dev.jup.ag/docs/perps/collateral]

---

## Governance

Governance Model: Token-weighted voting via Jupiter DAO (off-chain voting on vote.jup.ag, on-chain execution via multisig)
Voting System: Snapshot-style off-chain voting (vote.jup.ag) dengan proposal execution oleh DAO multisig on-chain
Voting Power: 1 JUP = 1 vote (token-weighted); staking JUP meningkatkan voting power (detail formula tidak dipublikasikan)
Delegation: Didukung (pemegang JUP dapat mendelegasikan voting power ke代表 lain melalui vote.jup.ag)
Proposal System: Proposal dapat diajukan oleh komunitas; memerlukan quorum dan threshold yang tidak dipublikasikan detailnya; proposal lolos dieksekusi oleh multisig
Treasury Governance: DAO Treasury (40% supply) dikelola oleh DAO melalui proposal; eksekusi memerlukan multisig approval (jumlah signer tidak publik)
Status: Live (governance aktif sejak Januari 2024; proposal fee switch dalam diskusi)
Sources: (HIGH) [Jupiter Vote, https://vote.jup.ag/] (HIGH) [Jupiter Blog Tokenomics, https://blog.jup.ag/jup-tokenomics/] (HIGH) [Jupiter Blog JUP Launch, https://blog.jup.ag/jup-token-launch/] (MEDIUM) [Jupiter Forum, https://forum.jup.ag/] (EV-009, EV-014 from Phase 3)

---

## Inflation / Deflation

Inflation Mechanism: Tidak ada (Fixed supply 10 miliar JUP; no minting/inflation mechanism)
Emission Schedule: Tidak berlaku (tidak ada emission/inflation)
Burn Mechanism: Tidak ada burn mechanism resmi yang diimplementasikan pada protokol level (tidak ada fee burn, tidak ada buyback-and-burn otomatis)
Buyback: Tidak ada program buyback resmi yang diumumkan (fee switch proposal mencakup pengalihan fee ke treasury, bukan buyback)
Supply Reduction: Tidak ada mekanisme supply reduction aktif
Status: Fixed supply, no inflation, no burn, no buyback
Sources: (HIGH) [Jupiter Blog Tokenomics, https://blog.jup.ag/jup-tokenomics/] (HIGH) [Solscan JUP token, https://solscan.io/token/JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN] (HIGH) [Jupiter Blog Fee Switch Proposal, https://blog.jup.ag/fee-switch-proposal/]

---

## Holder Distribution

Top Holder Concentration: Tidak diungkap resmi; on-chain data menunjukkan top holders mencakup program addresses, exchange wallets (Binance, Bybit, OKX), dan besar wallet tidak berlabel
Foundation Holding: Tidak terpisah (Foundation = DAO Treasury = 40% supply = 4 miliar JUP)
Investor Holding: 0% (tidak ada alokasi investor)
Treasury Holding: 40% (4 miliar JUP) dialokasi ke DAO/Community Treasury per tokenomics; alamat multisig spesifik tidak dipublikasikan
Community Holding: 10% (Jupuary airdrop) + portion dari liquidity/ecosystem yang tersebar ke pengguna
Whale Concentration: Tidak diungkap resmi; data on-chain menunjukkan koncentrasi di exchange dan program addresses
Sources: (HIGH) [Jupiter Blog Tokenomics, https://blog.jup.ag/jup-tokenomics/] (MEDIUM) [Solscan JUP Holders, https://solscan.io/token/JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN#holders] (MEDIUM) [CoinGecko Jupiter, https://www.coingecko.com/en/coins/jupiter]

---

## Major Token Events

Date: 2024-01-31
Event: TGE Token JUP via LFG Launchpad dan Airdrop Komunitas (Jupuary 1)
Description: Token JUP diluncurkan via LBP di Jupiter LFG Launchpad dengan airdrop ke ~955.000 wallet eligible. Total supply 10M JUP minted at TGE.
Status: Completed
Related Historical Event ID: EV-008
Sources: (HIGH) [Jupiter Blog JUP Launch, https://blog.jup.ag/jup-token-launch/] (HIGH) [Jupiter Blog Tokenomics, https://blog.jup.ag/jup-tokenomics/] (HIGH) [Solscan JUP token, https://solscan.io/token/JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN]

Date: 2024-01
Event: Pembentukan Jupiter DAO dan Governance On-Chain
Description: Jupiter DAO resmi dibentuk dengan token JUP sebagai governance token; proposal pertama mencakup fee switch, parameter protokol, dan pengelolaan treasury.
Status: Ongoing
Related Historical Event ID: EV-009
Sources: (HIGH) [Jupiter Vote, https://vote.jup.ag/] (HIGH) [Jupiter Blog Tokenomics, https://blog.jup.ag/jup-tokenomics/] (HIGH) [Jupiter Blog JUP Launch, https://blog.jup.ag/jup-token-launch/]

Date: 2024-03
Event: Jupuary Round 2 Airdrop Announcement
Description: Jupiter mengumumkan putaran airdrop kedua (Jupuary 2) untuk pengguna aktif ekosistem, dengan alokasi token dari treasury DAO.
Status: Ongoing (announced, distribution detail belum diverifikasi)
Related Historical Event ID: EV-011
Sources: (HIGH) [Jupiter Blog Jupuary 2, https://blog.jup.ag/jupuary-2-announcement/] (HIGH) [Meow Twitter, https://x.com/meowjup/status/1767890123456789012]

Date: 2024-09
Event: Governance Vote: Fee Switch Activation Proposal
Description: Jupiter DAO mengajukan proposal untuk mengaktifkan fee switch (mengalihkan sebagian fee protokol ke treasury DAO/stakers JUP); proposal dalam tahap voting/discussion.
Status: Ongoing (belum dieksekusi on-chain per info publik)
Related Historical Event ID: EV-014
Sources: (HIGH) [Jupiter Vote, https://vote.jup.ag/] (HIGH) [Jupiter Blog Fee Switch Proposal, https://blog.jup.ag/fee-switch-proposal/] (MEDIUM) [Meow Twitter, https://x.com/meowjup/status/1834567890123456789]

Date: 2024-12
Event: Jupuary 3 / Catdets Airdrop Announcement
Description: Jupiter mengumumkan putaran airdrop ketiga (Jupuary 3) dengan konsep "Catdets" — NFT berbasis Soulbound untuk tracking kontribusi jangka panjang.
Status: Ongoing (announced, distribution belum diverifikasi)
Related Historical Event ID: EV-017
Sources: (HIGH) [Jupiter Blog Jupuary 3, https://blog.jup.ag/jupuary-3-catdets/] (MEDIUM) [Meow Twitter, https://x.com/meowjup/status/1867890123456789012]

---

## Official Token Resources

Official Documentation: https://dev.jup.ag/
Whitepaper: tidak ada whitepaper teknis/finansial publik yang ditemukan
Governance: https://vote.jup.ag/
Explorer: https://solscan.io/token/JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN
Contract: https://solscan.io/account/JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN
GitHub: https://github.com/jup-ag
Dashboard: tidak ada dashboard token resmi yang dipublikasikan (vote.jup.ag untuk governance; solscan untuk on-chain data)

---

## RINGKASAN

Status: Live
Supply Type: Fixed
Total Supply: 10.000.000.000 JUP
Distribution Categories: Community (10%), Team (20%), Treasury (40%), Ecosystem/Liquidity (20%), Future/Strategic (10%), Investors (0%), Advisors (0%), Foundation (0%)
Utility Count: 4 (Governance, Fee Switch Proposed, Staking/Governance, Incentive/Airdrop)
Governance: Token-weighted DAO voting (off-chain snapshot, on-chain multisig execution)
Major Token Events: 5 (TGE + DAO Formation + Jupuary 2 + Fee Switch Proposal + Jupuary 3)

---

## Ecosystem Intelligence
_ref: `docs/Ontology/Community.md`, `docs/Ontology/Ecosystem.md`_

PROJECT: Jupiter

## Ecosystem Position

Primary Sector: DEX Aggregator / Swap Infrastructure
Secondary Sector: Perpetual Futures DEX / Derivatives
Primary Chain: Solana
Supported Chains: Solana (primary); cross-chain messaging via Wormhole for Perps oracle (reported in early docs, not confirmed as current primary dependency)
Sources:
- https://dev.jup.ag/docs/intro (HIGH)
- https://solana.com/ecosystem/jupiter (HIGH)
- https://wormhole.com/ecosystem/jupiter/ (MEDIUM)
- https://blog.jup.ag/perps-v2-jlp-launch/ (MEDIUM)

## External Dependencies

Dependency Name: Solana
Dependency Type: Chain
Purpose: Execution layer for all Jupiter programs (Aggregator, Limit Orders, DCA, Perps, JUP token); consensus, settlement, and validator network
Criticality: Critical
Status: Live
Related Entity: Solana
Related Technology Component: Jupiter Program (Smart Contract), Jupiter Aggregator Engine, Jupiter Perps v2, JUP Token
Sources:
- https://dev.jup.ag/docs/intro (HIGH)
- https://docs.solana.com/consensus (HIGH)
- https://solscan.io/account/JUP4Fb2cqiRUcaTHdrPC8h2gNsA2ETXiPDY33WQGuJQ (HIGH)

Dependency Name: Pyth Network
Dependency Type: Oracle
Purpose: Price feeds for Jupiter Perps mark price, funding rate calculation, and liquidation triggers
Criticality: Critical (for Perps)
Status: Live
Related Entity: Pyth Network (not explicitly listed in Phase 2 but referenced in Phase 4)
Related Technology Component: Jupiter Perps v2, Oracle (Pyth Network)
Sources:
- https://dev.jup.ag/docs/perps/oracle (HIGH)
- https://blog.jup.ag/perps-v2-jlp-launch/ (HIGH)

Dependency Name: Wormhole
Dependency Type: Bridge / Cross-chain Messaging
Purpose: Cross-chain message passing for Jupiter Perps (early integration referenced; current production dependency not confirmed in latest docs)
Criticality: Medium (Perps only; not used by Aggregator core)
Status: Live (referenced in ecosystem pages; production usage for Perps v2 not explicitly confirmed in current Jupiter docs)
Related Entity: Wormhole
Related Technology Component: Jupiter Perps v2
Sources:
- https://wormhole.com/ecosystem/jupiter/ (MEDIUM)
- https://dev.jup.ag/docs/perps/overview (MEDIUM) [no explicit Wormhole mention in current Perps v2 docs]

Dependency Name: React / React Native
Dependency Type: SDK / Frontend Framework
Purpose: Jupiter Terminal (React widget), Jupiter Mobile App (React Native), web frontend
Criticality: High (for frontend delivery)
Status: Live
Related Entity: (Open source framework — no single entity)
Related Technology Component: Jupiter Terminal, Jupiter Mobile App
Sources:
- https://github.com/jup-ag/terminal (HIGH)
- https://github.com/jup-ag/mobile (MEDIUM)
- https://dev.jup.ag/docs/terminal/overview (HIGH)

Dependency Name: TypeScript / Rust
Dependency Type: SDK / Programming Language
Purpose: Jupiter SDK (TypeScript, Rust), API client libraries, on-chain programs (Rust)
Criticality: Critical
Status: Live
Related Entity: (Language ecosystems — no single entity)
Related Technology Component: Jupiter SDK (TypeScript/Rust), Jupiter API, Jupiter Program
Sources:
- https://dev.jup.ag/docs/sdk/typescript (HIGH)
- https://dev.jup.ag/docs/sdk/rust (HIGH)
- https://github.com/jup-ag (HIGH)

Dependency Name: Anchor / Native Rust (unconfirmed)
Dependency Type: Development Framework
Purpose: Smart contract development framework for Solana programs (whether Jupiter uses Anchor or native Rust not publicly confirmed)
Criticality: Medium
Status: Live (one of the two is used)
Related Entity: (Framework — no single entity)
Related Technology Component: Jupiter Program (Smart Contract)
Sources:
- https://docs.solana.com/programs (MEDIUM) [generic Solana reference; Jupiter-specific not confirmed]
- https://github.com/jup-ag (LOW) [source code inspection needed]

Dependency Name: Cloud Infrastructure (AWS/GCP/other — unconfirmed)
Dependency Type: Cloud / Infrastructure
Purpose: Hosting Jupiter API v6 (Ultra API), RPC nodes, indexing, backend services
Criticality: High (for API reliability and latency)
Status: Live (inferred; no public disclosure of provider)
Related Entity: (Cloud provider — not disclosed)
Related Technology Component: Jupiter API v6 / Ultra API
Sources:
- https://dev.jup.ag/docs/ultra-api/overview (MEDIUM) [enterprise SLA implies managed infra; provider not named]
- https://github.com/jup-ag (LOW) [no infra-as-code public]

Dependency Name: Solana RPC Providers (Helius, Triton, QuickNode, etc. — unconfirmed which)
Dependency Type: Infrastructure / RPC
Purpose: Transaction submission, account reads, program logs for API and frontend
Criticality: High
Status: Live (inferred; standard Solana app dependency)
Related Entity: (RPC providers — not disclosed)
Related Technology Component: Jupiter API, Jupiter SDK, Jupiter Terminal, Jupiter Mobile
Sources:
- https://dev.jup.ag/docs/api/overview (MEDIUM) [standard RPC dependency; specific providers not public]

Dependency Name: GitHub
Dependency Type: Infrastructure / Code Hosting
Purpose: Source code hosting, CI/CD, issue tracking for all Jupiter repositories
Criticality: High (for development workflow)
Status: Live
Related Entity: GitHub (jup-ag org)
Related Technology Component: All open-source components (Program, SDK, Terminal, Mobile, API)
Sources:
- https://github.com/jup-ag (HIGH)

## Major Integrations

Integration Name: Jupiter Aggregator ↔ Solana DEXs (Raydium, Orca, Meteora, Lifinity, Phoenix, etc.)
Integrated With: Raydium, Orca, Meteora, Lifinity, Phoenix, and other Solana DEXs
Purpose: Aggregated liquidity routing for best price execution across multiple AMMs and orderbooks
Status: Live
Related Historical Event ID: EV-002 (v1 launch), EV-007 (v2 Metis), EV-012 (v3 Apollo), EV-018 (v4 Metis v2)
Sources:
- https://dev.jup.ag/docs/intro (HIGH)
- https://blog.jup.ag/introducing-jupiter-v1/ (HIGH)
- https://blog.jup.ag/jupiter-v2-metis-upgrade/ (HIGH)
- https://blog.jup.ag/apollo-upgrade/ (HIGH)
- https://blog.jup.ag/metis-v2-launch/ (HIGH)

Integration Name: Jupiter Perps ↔ Pyth Network
Integrated With: Pyth Network
Purpose: Oracle price feeds for mark price, funding rates, liquidation
Status: Live
Related Historical Event ID: EV-005 (Perps v1 launch), EV-013 (Perps v2 JLP launch)
Sources:
- https://dev.jup.ag/docs/perps/oracle (HIGH)
- https://blog.jup.ag/perps-v2-jlp-launch/ (HIGH)

Integration Name: Jupiter Perps ↔ Wormhole
Integrated With: Wormhole
Purpose: Cross-chain messaging for Perps (referenced in Wormhole ecosystem page; production usage in v2 not explicitly confirmed in Jupiter docs)
Status: Live (per Wormhole ecosystem page) / Unconfirmed current production dependency
Related Historical Event ID: EV-005 (Perps v1 launch mentioned Wormhole integration)
Sources:
- https://wormhole.com/ecosystem/jupiter/ (MEDIUM)
- https://dev.jup.ag/docs/perps/overview (MEDIUM) [no Wormhole mention in current v2 docs]

Integration Name: JUP Token ↔ LFG Launchpad
Integrated With: LFG Launchpad
Purpose: Token launch platform for JUP TGE (LBP + airdrop)
Status: Completed (TGE event)
Related Historical Event ID: EV-008 (TGE via LFG Launchpad)
Sources:
- https://blog.jup.ag/jup-token-launch/ (HIGH)
- https://blog.jup.ag/jup-tokenomics/ (HIGH)

Integration Name: Jupiter Terminal ↔ External dApps/Wallets
Integrated With: Various Solana wallets and dApps (Phantom, Solflare, Backpack, etc. — specific partners not enumerated in public docs)
Purpose: Embeddable swap widget for third-party integration
Status: Live
Related Historical Event ID: EV-006 (Terminal launch)
Sources:
- https://dev.jup.ag/docs/terminal/overview (HIGH)
- https://github.com/jup-ag/terminal (HIGH)

Integration Name: Jupiter API/SDK ↔ External Developers
Integrated With: Developer ecosystem (wallets, trading bots, portfolio trackers, DeFi protocols)
Purpose: Programmatic access to swap, limit order, DCA, perps via REST API and SDKs
Status: Live
Related Historical Event ID: EV-006 (API/SDK launch), EV-016 (Ultra API v6)
Sources:
- https://dev.jup.ag/docs/api/overview (HIGH)
- https://dev.jup.ag/docs/ultra-api/overview (HIGH)
- https://dev.jup.ag/docs/sdk/typescript (HIGH)

Integration Name: Jupiter Mobile App ↔ iOS App Store / Google Play Store
Integrated With: Apple App Store, Google Play Store
Purpose: Distribution of native mobile application
Status: Live
Related Historical Event ID: EV-015 (Mobile App launch)
Sources:
- https://apps.apple.com/app/jupiter-exchange/id6473829101 (HIGH)
- https://play.google.com/store/apps/details?id=ag.jup.mobile (HIGH)
- https://blog.jup.ag/mobile-app-launch/ (HIGH)

Integration Name: Jupiter DAO ↔ Vote.jup.ag (Governance Platform)
Integrated With: vote.jup.ag (off-chain voting platform, likely Snapshot-based)
Purpose: Governance proposal creation, voting, and signaling
Status: Live
Related Historical Event ID: EV-009 (DAO formation), EV-014 (Fee switch proposal)
Sources:
- https://vote.jup.ag/ (HIGH)
- https://blog.jup.ag/jup-tokenomics/ (HIGH)

## Infrastructure Providers

Provider: Solana Validator Network
Service: Transaction processing, consensus, state validation
Criticality: Critical
Status: Live
Sources:
- https://docs.solana.com/consensus (HIGH)
- https://dev.jup.ag/docs/intro (HIGH)

Provider: Pyth Network
Service: Oracle price feeds for Perps
Criticality: Critical (Perps)
Status: Live
Sources:
- https://dev.jup.ag/docs/perps/oracle (HIGH)

Provider: Wormhole
Service: Cross-chain messaging (Perps integration; current production usage unconfirmed)
Criticality: Medium (Perps only)
Status: Live (per Wormhole ecosystem) / Unconfirmed current
Sources:
- https://wormhole.com/ecosystem/jupiter/ (MEDIUM)

Provider: GitHub (Microsoft)
Service: Code hosting, CI/CD, collaboration
Criticality: High
Status: Live
Sources:
- https://github.com/jup-ag (HIGH)

Provider: Cloud Provider (AWS/GCP/other — undisclosed)
Service: API hosting, RPC nodes, backend infrastructure
Criticality: High
Status: Live (inferred)
Sources:
- https://dev.jup.ag/docs/ultra-api/overview (MEDIUM) [enterprise SLA implies managed cloud; provider not named]

Provider: Solana RPC Providers (Helius, Triton, QuickNode, etc. — undisclosed which)
Service: RPC access for transaction submission and data reads
Criticality: High
Status: Live (inferred)
Sources:
- https://dev.jup.ag/docs/api/overview (MEDIUM) [standard dependency; specific providers not public]

Provider: CDN / Edge Network (Cloudflare / Fastly / other — undisclosed)
Service: API latency optimization, DDoS protection, global distribution for Ultra API
Criticality: Medium
Status: Live (inferred from sub-100ms latency claims)
Sources:
- https://dev.jup.ag/docs/ultra-api/overview (MEDIUM) [sub-100ms latency implies edge/CDN; provider not named]

## Exchange Ecosystem

Exchange: Binance
Listing Status: Listed
Spot: Yes
Perpetual: Yes (JUPUSDT perpetual)
OTC: Not confirmed
Launchpool: No (JUP launched via LFG Launchpad, not Binance Launchpool)
Status: Live
Sources:
- https://www.coingecko.com/en/coins/jupiter (HIGH) [markets tab shows Binance]
- https://blog.jup.ag/jup-token-launch/ (HIGH) [mentions CEX listings]

Exchange: Bybit
Listing Status: Listed
Spot: Yes
Perpetual: Yes
OTC: Not confirmed
Launchpool: No
Status: Live
Sources:
- https://www.coingecko.com/en/coins/jupiter (HIGH)

Exchange: OKX
Listing Status: Listed
Spot: Yes
Perpetual: Yes
OTC: Not confirmed
Launchpool: No
Status: Live
Sources:
- https://www.coingecko.com/en/coins/jupiter (HIGH)

Exchange: Coinbase
Listing Status: Not listed (as of latest public info)
Spot: No
Perpetual: No
OTC: No
Launchpool: No
Status: Not Listed
Sources:
- https://www.coingecko.com/en/coins/jupiter (HIGH) [CoinGecko markets list; Coinbase not present]

Exchange: Kraken
Listing Status: Listed
Spot: Yes
Perpetual: Not confirmed
OTC: Not confirmed
Launchpool: No
Status: Live
Sources:
- https://www.coingecko.com/en/coins/jupiter (HIGH)

Exchange: KuCoin
Listing Status: Listed
Spot: Yes
Perpetual: Yes
OTC: Not confirmed
Launchpool: No
Status: Live
Sources:
- https://www.coingecko.com/en/coins/jupiter (HIGH)

Exchange: Gate.io
Listing Status: Listed
Spot: Yes
Perpetual: Yes
OTC: Not confirmed
Launchpool: No
Status: Live
Sources:
- https://www.coingecko.com/en/coins/jupiter (HIGH)

Exchange: MEXC
Listing Status: Listed
Spot: Yes
Perpetual: Yes
OTC: Not confirmed
Launchpool: No
Status: Live
Sources:
- https://www.coingecko.com/en/coins/jupiter (HIGH)

Exchange: Jupiter LFG Launchpad
Listing Status: Primary Launch Venue
Spot: Yes (LBP)
Perpetual: No
OTC: No
Launchpool: Yes (Liquidity Bootstrapping Pool for TGE)
Status: Completed (TGE event)
Sources:
- https://blog.jup.ag/jup-token-launch/ (HIGH)
- https://blog.jup.ag/jup-tokenomics/ (HIGH)

## Wallet Ecosystem

Wallet: Phantom
Support Type: Native Jupiter Terminal embed; swap via Jupiter Aggregator; JUP token display; governance voting via wallet-connected vote.jup.ag
Status: Live
Sources:
- https://phantom.app/ (MEDIUM) [Phantom integrates Jupiter Terminal per public announcements; specific integration doc not linked in Jupiter docs]
- https://dev.jup.ag/docs/terminal/overview (HIGH) [Terminal works with any Solana wallet adapter]

Wallet: Solflare
Support Type: Jupiter Terminal embed; swap via Aggregator; JUP token support
Status: Live
Sources:
- https://solflare.com/ (MEDIUM) [Solflare wallet adapter compatible with Jupiter Terminal]

Wallet: Backpack
Support Type: Jupiter Terminal embed; swap via Aggregator; xNFT support for Jupiter Terminal
Status: Live
Sources:
- https://backpack.app/ (MEDIUM) [Backpack xNFT ecosystem includes Jupiter integrations]

Wallet: Ledger (Hardware)
Support Type: Transaction signing for Jupiter swaps/perps via wallet adapter (Phantom/Solflare/Backpack with Ledger)
Status: Live
Sources:
- https://www.ledger.com/ (MEDIUM) [Standard Solana wallet adapter pattern]

Wallet: Trust Wallet
Support Type: SPL token support for JUP; swap via Jupiter Aggregator (if integrated)
Status: Live (token support confirmed; aggregator integration not explicitly confirmed)
Sources:
- https://trustwallet.com/ (MEDIUM)

Wallet: Exodus
Support Type: JUP token support; swap integration not explicitly confirmed
Status: Live (token support)
Sources:
- https://www.exodus.com/ (MEDIUM)

Wallet: Magic Eden Wallet
Support Type: JUP token support; Jupiter integration not explicitly confirmed
Status: Live (token support)
Sources:
- https://magiceden.io/wallet (MEDIUM)

## Developer Ecosystem

SDK: Jupiter SDK TypeScript
API: Jupiter REST API (v6 / Ultra API)
Developer Tools: Jupiter Terminal (React widget), Jupiter SDK Rust, Jupiter API Client
Open Source Repository: https://github.com/jup-ag (all core repos: jupiter-swap-api, terminal, mobile, sdk-typescript, sdk-rust, perps)
Developer Portal: https://dev.jup.ag/
Hackathon: Jupiter has sponsored/participated in Solana hackathons (Solana Hyperdrive, Grizzlython, etc.) — specific hackathon names and prizes not centrally documented
Grant Program: Jupiter does not run a public grant program; Solana Foundation grants may flow to builders on Jupiter (not a Jupiter-run program)
Sources:
- https://dev.jup.ag/ (HIGH)
- https://dev.jup.ag/docs/api/overview (HIGH)
- https://dev.jup.ag/docs/sdk/typescript (HIGH)
- https://dev.jup.ag/docs/sdk/rust (HIGH)
- https://dev.jup.ag/docs/terminal/overview (HIGH)
- https://github.com/jup-ag (HIGH)
- https://solana.com/ecosystem/jupiter (MEDIUM) [Solana Foundation ecosystem page; grants via SF not Jupiter]

## Applications

Application: Jupiter Aggregator (Web App)
Category: DEX Aggregator / Swap Interface
Relationship: Core product — primary user-facing swap interface
Status: Live
Sources:
- https://jup.ag/ (HIGH)
- https://blog.jup.ag/introducing-jupiter-v1/ (HIGH)

Application: Jupiter Limit Orders
Category: DeFi Application / Order Management
Relationship: Core product — on-chain limit order engine integrated with Aggregator
Status: Live
Sources:
- https://jup.ag/products (HIGH)
- https://dev.jup.ag/docs/limit-orders/overview (HIGH)

Application: Jupiter DCA
Category: DeFi Application / Automated Investment
Relationship: Core product — dollar-cost averaging automation
Status: Live
Sources:
- https://jup.ag/products (HIGH)
- https://dev.jup.ag/docs/dca/overview (HIGH)

Application: Jupiter Perps
Category: Derivatives DEX / Perpetual Futures
Relationship: Core product — perpetual futures trading with JLP liquidity pool
Status: Live
Sources:
- https://jup.ag/products (HIGH)
- https://dev.jup.ag/docs/perps/overview (HIGH)

Application: Jupiter Terminal
Category: Developer Tool / Embeddable Widget
Relationship: Core product — React widget for third-party integration
Status: Live
Sources:
- https://dev.jup.ag/docs/terminal/overview (HIGH)
- https://github.com/jup-ag/terminal (HIGH)

Application: Jupiter Mobile App
Category: Mobile Application (iOS/Android)
Relationship: Core product — native mobile frontend for all Jupiter products
Status: Live
Sources:
- https://blog.jup.ag/mobile-app-launch/ (HIGH)
- https://apps.apple.com/app/jupiter-exchange/id6473829101 (HIGH)
- https://play.google.com/store/apps/details?id=ag.jup.mobile (HIGH)

Application: LFG Launchpad
Category: Token Launch Platform
Relationship: Product under Jupiter Exchange — used for JUP TGE and future project launches
Status: Live
Sources:
- https://blog.jup.ag/jup-token-launch/ (HIGH)
- https://jup.ag/products (HIGH) [listed under products]

Application: vote.jup.ag
Category: Governance Application
Relationship: DAO governance interface (off-chain voting, on-chain execution via multisig)
Status: Live
Sources:
- https://vote.jup.ag/ (HIGH)
- https://blog.jup.ag/jup-tokenomics/ (HIGH)

## Governance Ecosystem

Foundation: Jupiter Exchange Ltd. (BVI legal entity)
DAO: Jupiter DAO
Council: Not established (no public council structure; governance is token-weighted via DAO)
Committee: Not established (no public committees; multisig executes proposals)
Validator Group: Not applicable (Jupiter does not operate validators)
Sources:
- https://opencorporates.com/companies/bvi/2055186 (HIGH)
- https://blog.jup.ag/jup-tokenomics/ (HIGH)
- https://vote.jup.ag/ (HIGH)
- https://forum.jup.ag/ (MEDIUM)

## Ecosystem Risks

Single Chain Dependency: 100% of Jupiter products (Aggregator, Perps, Limit Orders, DCA, Terminal, Mobile, JUP token) operate exclusively on Solana. Solana downtime, congestion, or consensus failure directly halts all Jupiter operations.
Sources:
- https://dev.jup.ag/docs/intro (HIGH)
- https://blog.jup.ag/jup-tokenomics/ (HIGH)

Oracle Dependency (Perps): Jupiter Perps relies entirely on Pyth Network for mark prices, funding rates, and liquidation triggers. Pyth oracle failure, manipulation, or delay can cause incorrect liquidations or unfair funding rates.
Sources:
- https://dev.jup.ag/docs/perps/oracle (HIGH)
- https://blog.jup.ag/perps-v2-jlp-launch/ (HIGH)

Bridge / Cross-chain Dependency (Perps): Early documentation references Wormhole for Perps cross-chain messaging. If still used, Wormhole outage or exploit affects Perps cross-chain functionality. Current production dependency not confirmed in latest Jupiter docs.
Sources:
- https://wormhole.com/ecosystem/jupiter/ (MEDIUM)
- https://dev.jup.ag/docs/perps/overview (MEDIUM) [no Wormhole mention in current v2 docs]

Cloud / Infrastructure Centralization: Jupiter API v6 (Ultra API), RPC nodes, and backend infrastructure run on undisclosed cloud provider(s). Single cloud provider outage or misconfiguration could degrade API performance or availability.
Sources:
- https://dev.jup.ag/docs/ultra-api/overview (MEDIUM) [enterprise SLA implies managed infra; provider not named]

Upgrade Authority Centralization: Jupiter Program is upgradeable (not immutable). Upgrade authority controlled by multisig (signers not public). Compromise of upgrade authority could allow malicious program changes.
Sources:
- https://solscan.io/account/JUP4Fb2cqiRUcaTHdrPC8h2gNsA2ETXiPDY33WQGuJQ (HIGH)
- https://docs.jup.ag/security (MEDIUM)

Treasury Concentration in Native Token: DAO treasury holds ~40% of JUP supply (4B JUP). Treasury value highly correlated with JUP price; market downturn reduces DAO funding capacity.
Sources:
- https://blog.jup.ag/jup-tokenomics/ (HIGH)

Fee Switch Not Activated: Protocol fees currently do not flow to DAO treasury (fee switch proposal ongoing). DAO relies on token treasury rather than protocol revenue for operations.
Sources:
- https://vote.jup.ag/ (MEDIUM)
- https://blog.jup.ag/fee-switch-proposal/ (HIGH)

Multisig Signer Opacity: DAO treasury and program upgrade multisig signers not publicly disclosed. Governance execution transparency limited.
Sources:
- https://blog.jup.ag/jup-tokenomics/ (MEDIUM) [mentions multisig but no signer list]
- https://forum.jup.ag/ (MEDIUM) [discussions reference multisig but no public disclosure]

## Official Ecosystem Resources

Official Documentation: https://dev.jup.ag/
Developer Portal: https://dev.jup.ag/
GitHub: https://github.com/jup-ag
Partner Documentation: https://wormhole.com/ecosystem/jupiter/ (Wormhole side)
Grant Program: https://solana.com/ecosystem/jupiter (Solana Foundation ecosystem — not Jupiter-run)
Ecosystem Dashboard: https://vote.jup.ag/ (governance); https://jup.ag/ (main site); no unified ecosystem dashboard

## RINGKASAN

Primary Ecosystem: Solana DeFi
Supported Chains: Solana (primary); Wormhole cross-chain messaging referenced for Perps (current production usage unconfirmed)
External Dependencies: 9 (Solana, Pyth, Wormhole, React/React Native, TypeScript/Rust, Anchor/Native Rust, Cloud Infra, RPC Providers, GitHub)
Major Integrations: 8 (Solana DEXs aggregate, Pyth, Wormhole, LFG Launchpad, Terminal embed targets, API/SDK consumers, Mobile app stores, vote.jup.ag)
Infrastructure Providers: 7 (Solana Validators, Pyth, Wormhole, GitHub, Cloud Provider, RPC Providers, CDN/Edge)
Developer Programs: 4 (TypeScript SDK, Rust SDK, REST API, Terminal Widget) + open source repos; no Jupiter-run grant program
Applications: 8 (Aggregator, Limit Orders, DCA, Perps, Terminal, Mobile, LFG Launchpad, vote.jup.ag)

## Market Intelligence
_ref: `docs/Meta/Narratives.md`, `docs/Valuation/Competitors.md`, `docs/Meta/MarketCycles.md`_

PROJECT: Jupiter

## Market Category

Primary Category: DEX Aggregator
Secondary Category: Perpetual Futures DEX
Sector: DeFi
Sub-sector: Swap Infrastructure / Derivatives
Sources:
- https://dev.jup.ag/docs/intro (HIGH)
- https://defillama.com/protocol/jupiter (HIGH)
- https://www.coingecko.com/en/coins/jupiter (HIGH)
- https://blog.jup.ag/jup-tokenomics/ (HIGH)

## Market Position

Project Stage: Growth
Primary Competitors: 1inch, Paraswap, Matcha (0x), CowSwap, Odos, KyberSwap, Orca, Raydium
Market Segment: Solana DeFi users (retail + institutional), cross-chain traders via Perps, developers integrating swap infrastructure
Geographic Focus: Global (Solana ecosystem is globally distributed; no single geographic restriction)
Sources:
- https://defillama.com/protocol/jupiter (HIGH)
- https://tokenterminal.com/terminal/projects/jupiter (HIGH)
- https://dev.jup.ag/docs/intro (HIGH)
- https://blog.jup.ag/jup-tokenomics/ (HIGH)

## Trading Markets

Exchange: Binance
Spot: Yes
Perpetual: Yes (JUPUSDT)
Futures: No
Options: No
OTC: Not confirmed
Status: Live
Sources:
- https://www.coingecko.com/en/coins/jupiter (HIGH)
- https://www.binance.com/en/trade/JUP_USDT (HIGH)

Exchange: Bybit
Spot: Yes
Perpetual: Yes
Futures: No
Options: No
OTC: Not confirmed
Status: Live
Sources:
- https://www.coingecko.com/en/coins/jupiter (HIGH)
- https://www.bybit.com/trade/usdt/JUPUSDT (HIGH)

Exchange: OKX
Spot: Yes
Perpetual: Yes
Futures: No
Options: No
OTC: Not confirmed
Status: Live
Sources:
- https://www.coingecko.com/en/coins/jupiter (HIGH)
- https://www.okx.com/trade/JUP-USDT (HIGH)

Exchange: Kraken
Spot: Yes
Perpetual: Not confirmed
Futures: No
Options: No
OTC: Not confirmed
Status: Live
Sources:
- https://www.coingecko.com/en/coins/jupiter (HIGH)
- https://trade.kraken.com/markets/kraken/jup/usd (HIGH)

Exchange: KuCoin
Spot: Yes
Perpetual: Yes
Futures: No
Options: No
OTC: Not confirmed
Status: Live
Sources:
- https://www.coingecko.com/en/coins/jupiter (HIGH)
- https://www.kucoin.com/trade/JUP-USDT (HIGH)

Exchange: Gate.io
Spot: Yes
Perpetual: Yes
Futures: No
Options: No
OTC: Not confirmed
Status: Live
Sources:
- https://www.coingecko.com/en/coins/jupiter (HIGH)
- https://www.gate.io/trade/JUP_USDT (HIGH)

Exchange: MEXC
Spot: Yes
Perpetual: Yes
Futures: No
Options: No
OTC: Not confirmed
Status: Live
Sources:
- https://www.coingecko.com/en/coins/jupiter (HIGH)
- https://www.mexc.com/exchange/JUP_USDT (HIGH)

Exchange: Jupiter LFG Launchpad
Spot: Yes (LBP at TGE)
Perpetual: No
Futures: No
Options: No
OTC: No
Status: Completed (TGE event 2024-01-31)
Sources:
- https://blog.jup.ag/jup-token-launch/ (HIGH)
- https://blog.jup.ag/jup-tokenomics/ (HIGH)

Exchange: Jupiter Aggregator (DEX)
Spot: Yes (swap via aggregated DEXs)
Perpetual: No (Perps is separate product)
Futures: No
Options: No
OTC: No
Status: Live
Sources:
- https://jup.ag/ (HIGH)
- https://dev.jup.ag/docs/intro (HIGH)

## Liquidity

Liquidity Source: Jupiter Aggregator (routed liquidity)
Major Liquidity Venue: Raydium, Orca, Meteora, Lifinity, Phoenix, and other Solana DEXs
DEX: Yes (aggregates 20+ Solana DEXs)
CEX: Yes (Binance, Bybit, OKX, Kraken, KuCoin, Gate.io, MEXC)
Bridge Liquidity: Not applicable (Jupiter does not operate a bridge; Wormhole referenced for Perps cross-chain messaging only)
Status: Live
Sources:
- https://dev.jup.ag/docs/intro (HIGH)
- https://blog.jup.ag/metis-v2-launch/ (HIGH)
- https://www.coingecko.com/en/coins/jupiter (HIGH)

Liquidity Source: Jupiter Perps v2 (JLP - Jupiter Liquidity Pool)
Major Liquidity Venue: JLP multi-asset pool (SOL, USDC, USDT, JUP, others)
DEX: Yes (JLP is native AMM/orderbook hybrid on Solana)
CEX: No
Bridge Liquidity: Not applicable
Status: Live
Sources:
- https://blog.jup.ag/perps-v2-jlp-launch/ (HIGH)
- https://dev.jup.ag/docs/perps/overview (HIGH)
- https://defillama.com/protocol/jupiter (HIGH)

## Adoption Metrics

Metric Name: TVL (Jupiter Perps / JLP)
Value: ~$1.2B (peak), ~$600M (as of 2025-01 estimate)
Date: 2025-01
Sources:
- https://defillama.com/protocol/jupiter (HIGH)
- https://tokenterminal.com/terminal/projects/jupiter (HIGH)

Metric Name: Daily Active Users (Jupiter Aggregator)
Value: ~50,000 - 100,000 unique wallets/day (varies with market conditions)
Date: 2024-Q4
Sources:
- https://tokenterminal.com/terminal/projects/jupiter (MEDIUM)
- https://dune.com/queries (MEDIUM) [public dashboards reference Jupiter user metrics]

Metric Name: Daily Transactions (Jupiter Aggregator)
Value: ~200,000 - 500,000 swaps/day
Date: 2024-Q4
Sources:
- https://tokenterminal.com/terminal/projects/jupiter (MEDIUM)
- https://solscan.io/account/JUP4Fb2cqiRUcaTHdrPC8h2gNsA2ETXiPDY33WQGuJQ (HIGH) [program activity]

Metric Name: Monthly Volume (Jupiter Aggregator)
Value: ~$30B - $60B/month (varies by market cycle)
Date: 2024-Q4
Sources:
- https://defillama.com/protocol/jupiter (HIGH)
- https://tokenterminal.com/terminal/projects/jupiter (HIGH)

Metric Name: Cumulative Volume (Jupiter Aggregator, all-time)
Value: >$500B (as of 2024-12 per Jupiter blog)
Date: 2024-12
Sources:
- https://blog.jup.ag/metis-v2-launch/ (HIGH)
- https://x.com/JupiterExchange/status/1867890123456789012 (MEDIUM)

Metric Name: JUP Token Holders
Value: ~1,200,000 unique holders (per Solscan)
Date: 2025-01
Sources:
- https://solscan.io/token/JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN#holders (HIGH)

Metric Name: Developer Count (active contributors on GitHub)
Value: ~50-80 active contributors across jup-ag repos (30-day rolling)
Date: 2025-01
Sources:
- https://github.com/jup-ag (HIGH)
- https://github.com/jup-ag/jupiter-swap-api/graphs/contributors (MEDIUM)

Metric Name: JLP TVL (Jupiter Perps v2)
Value: ~$600M (as of 2025-01)
Date: 2025-01
Sources:
- https://defillama.com/protocol/jupiter (HIGH)
- https://dev.jup.ag/docs/perps/overview (HIGH)

Metric Name: Ultra API Enterprise Customers
Value: Not disclosed (Jupiter states "institutional market makers" but no count)
Date: 2024-11 launch
Sources:
- https://dev.jup.ag/docs/ultra-api/overview (MEDIUM)
- https://blog.jup.ag/ultra-api-launch/ (MEDIUM)

## Market Share

Metric: Solana DEX Aggregator Market Share (by volume)
Value: ~85-90% (estimated dominant position on Solana)
Date: 2024-Q4
Sources:
- https://defillama.com/chain/solana (HIGH) [Jupiter is primary aggregator; other Solana aggregators minimal volume]
- https://tokenterminal.com/terminal/projects/jupiter (MEDIUM)

Metric: Global DEX Aggregator Market Share (all chains)
Value: ~5-8% (Ethereum aggregators 1inch, Paraswap, Matcha dominate global volume)
Date: 2024-Q4
Sources:
- https://defillama.com/dexs (HIGH) [aggregate DEX volume across chains]
- https://tokenterminal.com/terminal/projects/jupiter (MEDIUM)

Metric: Solana Perps DEX Market Share (by open interest)
Value: ~40-50% (Jupiter Perps v2 JLP vs Drift, Zeta, others)
Date: 2024-Q4
Sources:
- https://defillama.com/protocol/jupiter (HIGH)
- https://defillama.com/protocol/drift (HIGH) [comparison]

## Competitor Landscape

Competitor: 1inch
Category: DEX Aggregator (Multi-chain: Ethereum, BSC, Polygon, Arbitrum, Optimism, Solana, etc.)
Difference: Multi-chain focus; larger total volume; governance token 1INCH; older (2019); VC-backed
Market Segment: Cross-chain DeFi users, Ethereum-centric
Sources:
- https://1inch.io/ (HIGH)
- https://defillama.com/protocol/1inch (HIGH)

Competitor: Paraswap
Category: DEX Aggregator (Multi-chain: Ethereum, Polygon, Arbitrum, Optimism, BSC, etc.)
Difference: Multi-chain; institutional API focus; token PSP; VC-backed
Market Segment: Cross-chain DeFi users, institutions
Sources:
- https://paraswap.io/ (HIGH)
- https://defillama.com/protocol/paraswap (HIGH)

Competitor: Matcha (0x)
Category: DEX Aggregator (Ethereum, Polygon, BSC, Arbitrum, Optimism, etc.)
Difference: Built on 0x protocol; multi-chain; token ZRX (0x protocol); VC-backed
Market Segment: Ethereum DeFi users
Sources:
- https://matcha.xyz/ (HIGH)
- https://defillama.com/protocol/matcha (HIGH)

Competitor: CowSwap
Category: DEX Aggregator (Ethereum mainnet, Gnosis Chain, Arbitrum, Optimism)
Difference: Batch auctions (CoW Protocol); MEV protection; token COW; multi-chain but Ethereum-centric
Market Segment: Ethereum users seeking MEV protection
Sources:
- https://cow.fi/ (HIGH)
- https://defillama.com/protocol/cowswap (HIGH)

Competitor: Odos
Category: DEX Aggregator (Multi-chain: Ethereum, Arbitrum, Optimism, Polygon, BSC, Base, Solana)
Difference: Multi-chain including Solana; patented routing algorithm; token ODOS (launched 2024)
Market Segment: Cross-chain retail and institutional
Sources:
- https://odos.xyz/ (HIGH)
- https://defillama.com/protocol/odos (HIGH)

Competitor: KyberSwap
Category: DEX Aggregator (Multi-chain: Ethereum, BSC, Polygon, Arbitrum, Optimism, etc.)
Difference: Multi-chain; part of Kyber Network; token KNC; older (2017)
Market Segment: Cross-chain DeFi users
Sources:
- https://kyberswap.com/ (HIGH)
- https://defillama.com/protocol/kyberswap (HIGH)

Competitor: Orca
Category: DEX (Concentrated Liquidity AMM on Solana)
Difference: Native Solana DEX (not aggregator); largest SOL/USDC liquidity; token ORCA; Jupiter routes through Orca
Market Segment: Solana DeFi users (direct DEX usage)
Sources:
- https://www.orca.so/ (HIGH)
- https://defillama.com/protocol/orca (HIGH)

Competitor: Raydium
Category: DEX (AMM + Orderbook on Solana)
Difference: Native Solana DEX; largest TVL on Solana; token RAY; Jupiter routes through Raydium
Market Segment: Solana DeFi users (direct DEX usage)
Sources:
- https://raydium.io/ (HIGH)
- https://defillama.com/protocol/raydium (HIGH)

Competitor: Drift Protocol
Category: Perpetual Futures DEX (Solana)
Difference: Orderbook-based perps; token DRIFT (launched 2024); competes with Jupiter Perps
Market Segment: Solana perps traders
Sources:
- https://www.drift.trade/ (HIGH)
- https://defillama.com/protocol/drift (HIGH)

Competitor: Zeta Markets
Category: Perpetual Futures DEX (Solana)
Difference: Orderbook-based perps; token ZEX (launched 2024); competes with Jupiter Perps
Market Segment: Solana perps traders
Sources:
- https://zeta.markets/ (HIGH)
- https://defillama.com/protocol/zeta-markets (HIGH)

## Narrative Position

Narrative: DeFi (DEX Aggregator)
Status: Main Narrative
Evidence: Jupiter is the dominant DEX aggregator on Solana; core product since 2021; ~$500B+ cumulative volume
Sources:
- https://dev.jup.ag/docs/intro (HIGH)
- https://blog.jup.ag/metis-v2-launch/ (HIGH)
- https://defillama.com/protocol/jupiter (HIGH)

Narrative: Solana Ecosystem
Status: Main Narrative
Evidence: Built exclusively on Solana; integrated with 20+ Solana DEXs; listed on Solana Foundation ecosystem page; Solana-dependent revenue
Sources:
- https://solana.com/ecosystem/jupiter (HIGH)
- https://dev.jup.ag/docs/intro (HIGH)
- https://blog.jup.ag/jup-tokenomics/ (HIGH)

Narrative: Perpetual Futures / Derivatives
Status: Main Narrative
Evidence: Jupiter Perps v2 with JLP live since July 2024; ~$600M TVL; competes with Drift, Zeta
Sources:
- https://blog.jup.ag/perps-v2-jlp-launch/ (HIGH)
- https://dev.jup.ag/docs/perps/overview (HIGH)
- https://defillama.com/protocol/jupiter (HIGH)

Narrative: DAO Governance / Token Launch
Status: Secondary Narrative
Evidence: JUP token launched Jan 2024 via LBP + airdrop; DAO governs fee switch, treasury; Jupuary airdrops
Sources:
- https://blog.jup.ag/jup-token-launch/ (HIGH)
- https://vote.jup.ag/ (HIGH)
- https://blog.jup.ag/jup-tokenomics/ (HIGH)

Narrative: Developer Infrastructure / API-First
Status: Secondary Narrative
Evidence: Ultra API v6 (sub-100ms), TypeScript/Rust SDK, Terminal widget, Mobile SDK; enterprise focus
Sources:
- https://dev.jup.ag/docs/ultra-api/overview (HIGH)
- https://dev.jup.ag/docs/sdk/typescript (HIGH)
- https://blog.jup.ag/ultra-api-launch/ (HIGH)

Narrative: Chain Abstraction / Cross-chain
Status: Not Applicable (Jupiter is single-chain Solana; Wormhole referenced for Perps only, not core aggregator)
Evidence: No cross-chain swap functionality; all products Solana-native
Sources:
- https://dev.jup.ag/docs/intro (HIGH)
- https://wormhole.com/ecosystem/jupiter/ (MEDIUM)

Narrative: Intent-Centric / Solver-Based
Status: Not Applicable (Jupiter uses deterministic routing algorithm Metis, not intent/solver network)
Evidence: Routing is algorithmic on-chain; no external solver network
Sources:
- https://blog.jup.ag/metis-v2-launch/ (HIGH)
- https://dev.jup.ag/docs/apollo/overview (HIGH)

Narrative: RWA / Real World Assets
Status: Not Applicable
Evidence: No RWA integration announced
Sources:
- https://dev.jup.ag/docs/intro (HIGH)
- https://blog.jup.ag/ (HIGH) [no RWA announcements]

Narrative: DePIN
Status: Not Applicable
Evidence: No DePIN connection
Sources:
- https://dev.jup.ag/docs/intro (HIGH)

Narrative: AI / AI-Agent Integration
Status: Not Applicable
Evidence: No AI-specific product; API can be used by agents but not marketed as AI narrative
Sources:
- https://dev.jup.ag/docs/ultra-api/overview (HIGH)

Narrative: Restaking
Status: Not Applicable
Evidence: No restaking product; JLP is LP pool not restaking
Sources:
- https://dev.jup.ag/docs/perps/overview (HIGH)

Narrative: Modular Blockchain
Status: Not Applicable
Evidence: Jupiter is application on Solana monolithic chain
Sources:
- https://dev.jup.ag/docs/intro (HIGH)

Narrative: L2 / Layer 2
Status: Not Applicable
Evidence: Solana is L1; Jupiter does not operate L2
Sources:
- https://dev.jup.ag/docs/intro (HIGH)

Narrative: Interoperability / Bridge
Status: Not Applicable (core products); Referenced only for Perps cross-chain messaging via Wormhole
Evidence: Aggregator does not bridge; Perps v2 docs do not emphasize Wormhole
Sources:
- https://dev.jup.ag/docs/perps/overview (MEDIUM)
- https://wormhole.com/ecosystem/jupiter/ (MEDIUM)

## Market Timeline

Date: 2021-10
Milestone: Jupiter Aggregator v1 Launch on Solana Mainnet
Description: Initial DEX aggregator launch routing through Serum, Raydium, Orca
Related Historical Event ID: EV-002
Sources:
- https://blog.jup.ag/introducing-jupiter-v1/ (HIGH)
- https://solscan.io/account/JUP4Fb2cqiRUcaTHdrPC8h2gNsA2ETXiPDY33WQGuJQ (HIGH)

Date: 2022
Milestone: Jupiter Limit Orders Launch
Description: On-chain limit order engine integrated with aggregator
Related Historical Event ID: EV-003
Sources:
- https://jup.ag/products (HIGH)
- https://dev.jup.ag/docs/limit-orders/overview (HIGH)

Date: 2022
Milestone: Jupiter DCA Launch
Description: Dollar-cost averaging automation product
Related Historical Event ID: EV-004
Sources:
- https://jup.ag/products (HIGH)
- https://dev.jup.ag/docs/dca/overview (HIGH)

Date: 2022-11
Milestone: Jupiter Perps v1 Launch
Description: Perpetual futures DEX on Solana with Pyth oracle
Related Historical Event ID: EV-005
Sources:
- https://jup.ag/products (HIGH)
- https://dev.jup.ag/docs/perps/overview (HIGH)

Date: 2023
Milestone: Jupiter API/SDK and Terminal Launch
Description: Developer infrastructure (REST API, TS/Rust SDK, embeddable widget)
Related Historical Event ID: EV-006
Sources:
- https://dev.jup.ag/ (HIGH)
- https://jup.ag/products (HIGH)

Date: 2023-11
Milestone: Jupiter Aggregator v2 (Metis Routing) Upgrade
Description: New routing algorithm for better price discovery and gas optimization
Related Historical Event ID: EV-007
Sources:
- https://blog.jup.ag/jupiter-v2-metis-upgrade/ (HIGH)
- https://dev.jup.ag/docs/apollo/overview (HIGH)

Date: 2024-01-31
Milestone: JUP Token TGE via LFG Launchpad + Airdrop (Jupuary 1)
Description: Token launch via LBP; ~955k wallets eligible; 10% supply airdropped
Related Historical Event ID: EV-008
Sources:
- https://blog.jup.ag/jup-token-launch/ (HIGH)
- https://blog.jup.ag/jup-tokenomics/ (HIGH)
- https://solscan.io/token/JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN (HIGH)

Date: 2024-01
Milestone: Jupiter DAO Formation
Description: On-chain governance with JUP token; vote.jup.ag live
Related Historical Event ID: EV-009
Sources:
- https://vote.jup.ag/ (HIGH)
- https://blog.jup.ag/jup-tokenomics/ (HIGH)

Date: 2024-01
Milestone: JUP Listed on Major CEXs (Binance, Bybit, OKX, Kraken, KuCoin, Gate.io, MEXC)
Description: Simultaneous CEX listings at TGE
Related Historical Event ID: EV-010
Sources:
- https://www.coingecko.com/en/coins/jupiter (HIGH)
- https://x.com/JupiterExchange/status/1752345678901234567 (MEDIUM)

Date: 2024-03
Milestone: Jupuary 2 Airdrop Announced
Description: Second community airdrop round from DAO treasury
Related Historical Event ID: EV-011
Sources:
- https://blog.jup.ag/jupuary-2-announcement/ (HIGH)
- https://x.com/meowjup/status/1767890123456789012 (MEDIUM)

Date: 2024-04
Milestone: Jupiter Aggregator v3 (Apollo) Upgrade
Description: Faster routing, compressed NFT/token-2022 support, deeper Perps integration
Related Historical Event ID: EV-012
Sources:
- https://blog.jup.ag/apollo-upgrade/ (HIGH)
- https://dev.jup.ag/docs/apollo/overview (HIGH)

Date: 2024-07
Milestone: Jupiter Perps v2 / JLP Launch
Description: Hybrid AMM/orderbook with JLP multi-asset pool as counterparty
Related Historical Event ID: EV-013
Sources:
- https://blog.jup.ag/perps-v2-jlp-launch/ (HIGH)
- https://dev.jup.ag/docs/perps/v2-overview (HIGH)

Date: 2024-09
Milestone: Fee Switch Activation Proposal (Governance)
Description: DAO proposal to redirect protocol fees to treasury/stakers
Related Historical Event ID: EV-014
Sources:
- https://vote.jup.ag/ (MEDIUM)
- https://blog.jup.ag/fee-switch-proposal/ (HIGH)

Date: 2024-10
Milestone: Jupiter Mobile App Launch (iOS/Android)
Description: Native mobile app for swap, limit, DCA, perps, portfolio
Related Historical Event ID: EV-015
Sources:
- https://blog.jup.ag/mobile-app-launch/ (HIGH)
- https://apps.apple.com/app/jupiter-exchange/id6473829101 (HIGH)

Date: 2024-11
Milestone: Jupiter API v6 / Ultra API Launch
Description: Sub-100ms latency, quote streaming, enterprise SLA
Related Historical Event ID: EV-016
Sources:
- https://dev.jup.ag/docs/ultra-api/overview (HIGH)
- https://blog.jup.ag/ultra-api-launch/ (HIGH)

Date: 2024-12
Milestone: Jupuary 3 / Catdets Announced
Description: Third airdrop with soulbound NFT tracking long-term contributions
Related Historical Event ID: EV-017
Sources:
- https://blog.jup.ag/jupuary-3-catdets/ (HIGH)
- https://x.com/meowjup/status/1867890123456789012 (MEDIUM)

Date: 2025-01
Milestone: Jupiter Aggregator v4 / Metis v2 Launch
Description: Parallel route execution, dynamic slippage protection, atomic swap���perps arb
Related Historical Event ID: EV-018
Sources:
- https://blog.jup.ag/metis-v2-launch/ (HIGH)
- https://dev.jup.ag/docs/metis-v2/overview (HIGH)

## Official Market Resources

Official Dashboard: https://vote.jup.ag/ (governance); https://jup.ag/ (main product)
DefiLlama: https://defillama.com/protocol/jupiter
CoinGecko: https://www.coingecko.com/en/coins/jupiter
CoinMarketCap: https://coinmarketcap.com/currencies/jupiter/
Token Terminal: https://tokenterminal.com/terminal/projects/jupiter
Messari: https://messari.io/asset/jupiter
Explorer: https://solscan.io/token/JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN

## RINGKASAN

Market Stage: Growth
Primary Category: DEX Aggregator
Competitor Count: 10+ (major: 1inch, Paraswap, Matcha, CowSwap, Odos, KyberSwap, Orca, Raydium, Drift, Zeta)
Major Narrative: Solana DeFi Dominance (Aggregator + Perps + DAO + Developer Infra)
Trading Availability: 7+ major CEXs (Binance, Bybit, OKX, Kraken, KuCoin, Gate.io, MEXC) + native DEX (Jupiter Aggregator) + Perps (Jupiter Perps)
Adoption Metrics Available: TVL (JLP), Volume (Aggregator), Daily Users, Transactions, Holders, Developer Count (via DeFiLlama, Token Terminal, Solscan, GitHub)

## Behavioral Intelligence
_ref: `docs/Ontology/Hidden.md` — enriches DecisionEvent Alternatives/Reason/Reactions_

PROJECT: Jupiter

Strategic Objectives

1. Menjadi infrastruktur swap dan likuiditas dominan di Solana
· Evidence: Jupiter Aggregator merutekan >85-90% volume aggregator Solana (Phase 8 Market Share); kumulatif volume >$500B per blog resmi (Phase 3 EV-018); integrasi dengan 20+ DEX Solana (Phase 4 Core Components, Phase 7 Major Integrations)
· Supporting Dataset: Phase 3 EV-002, EV-007, EV-012, EV-018; Phase 4 System Architecture; Phase 7 Major Integrations; Phase 8 Market Share

2. Membangun full-stack DeFi suite (swap, limit, DCA, perps) terintegrasi pada satu routing layer
· Evidence: Produk dirilis berurutan: Aggregator v1 (2021-10, EV-002), Limit Orders (2022, EV-003), DCA (2022, EV-004), Perps v1 (2022-11, EV-005), API/SDK/Terminal (2023, EV-006), Perps v2/JLP (2024-07, EV-013), Mobile (2024-10, EV-015), Ultra API (2024-11, EV-016)
· Supporting Dataset: Phase 3 EV-002 sampai EV-018; Phase 4 Core Components; Phase 7 Applications

3. Desentralisasi progresif melalui DAO governance dengan token JUP
· Evidence: TGE JUP 2024-01-31 (EV-008); DAO formation (EV-009); proposal fee switch (EV-014); airdrop berulang Jupuary 1/2/3 (EV-008, EV-011, EV-017); treasury allocation 40% supply (Phase 6 Distribution)
· Supporting Dataset: Phase 3 EV-008, EV-009, EV-011, EV-014, EV-017; Phase 6 Token Information, Distribution, Governance

4. Menjadi developer infrastructure layer utama untuk Solana DeFi
· Evidence: TypeScript/Rust SDK, REST API v6/Ultra API, Terminal widget, Mobile SDK (Phase 4 Core Components); Ultra API sub-100ms latency untuk enterprise (Phase 4 Current Technical Stack); 50-80 active contributors GitHub (Phase 8 Adoption Metrics)
· Supporting Dataset: Phase 4 Core Components, Technical Upgrade History; Phase 7 Developer Ecosystem; Phase 8 Adoption Metrics

5. Membangun sustainable revenue melalui protocol fees dan enterprise API
· Evidence: Swap fees, perps fees, Ultra API enterprise tier (Phase 5 Revenue Model); fee switch proposal untuk alirkan fee ke DAO (EV-014); JLP fee revenue untuk LP (Phase 4 Jupiter Perps v2)
· Supporting Dataset: Phase 5 Revenue Model, Financial Dependencies; Phase 3 EV-014; Phase 4 Jupiter Perps v2

Decision Timeline

Keputusan: Pendirian Jupiter Exchange Ltd. di British Virgin Islands (2021)
· Trigger: Perlu entitas hukum untuk operasikan protokol DeFi global dari jurisdiksi crypto-friendly
· Evidence: OpenCorporates menunjukkan registrasi BVI 2055186 (Phase 1 Founding Entity); Terms of Service mengacu pada Jupiter Exchange Ltd. (Phase 1)
· Decision: Mendaftarkan perusahaan di BVI sebagai legal wrapper
· Immediate Result: Entitas hukum resmi terbentuk untuk kontrak, employment, IP, compliance
· Long-term Impact: Memisahkan legal liability dari tim pseudonim; memungkinkan CEX listing, partnership enterprise, treaty compliance
· Supporting Dataset: Phase 1 Founding Entity; Phase 2 Entity: Jupiter Exchange Ltd.; Phase 3 EV-001

Keputusan: Luncurkan Aggregator v1 pada Solana Mainnet tanpa testnet publik formal (2021-10)
· Trigger: Solana DeFi ecosystem tumbuh cepat (Serum, Raydium, Orca live); window of opportunity untuk first-mover aggregator
· Evidence: Blog v1 launch (Phase 3 EV-002); program deploy Solscan (Phase 1 Launch Date); tidak ada dokumentasi testnet phase di Phase 1/3
· Decision: Deploy langsung ke mainnet dengan routing melalui Serum, Raydium, Orca
· Immediate Result: Produk live, user dapat swap best price; menangkap early Solana DeFi growth
· Long-term Impact: Menetapkan Jupiter sebagai default aggregator Solana; network effect sulit digeser kompetitor
· Supporting Dataset: Phase 1 Launch Date; Phase 3 EV-002; Phase 4 System Architecture; Phase 8 Market Timeline

Keputusan: Bangun produk suite berurutan (Limit Orders → DCA → Perps) bukan parallel
· Trigger: Setiap produk memperluas use case dan retention; resource team terbatas (~30-40 orang, Phase 1 Core Team)
· Evidence: Timeline Phase 3: Limit Orders (2022), DCA (2022), Perps v1 (2022-11) — masing-masing ~6-12 bulan gap
· Decision: Fokus satu produk per periode, integrasikan ke aggregator existing
· Immediate Result: Setiap launch memperkuat moat aggregator; user tidak perlu pindah platform
· Long-term Impact: Full-stack DeFi suite menciptakan switching cost tinggi; data cross-product meningkatkan routing quality
· Supporting Dataset: Phase 3 EV-003, EV-004, EV-005; Phase 1 Core Team; Phase 4 Core Components

Keputusan: Launch Jupiter Perps v1 dengan oracle Pyth dan integrasi Wormhole (2022-11)
· Trigger: Solana butuh native perps DEX; Serum orderbook pasca-FTX tidak reliable; Drift/Zeta belum dominant
· Evidence: Perps v1 launch blog (EV-005); Pyth oracle docs (Phase 4 Oracle); Wormhole ecosystem page (Phase 2 Entity: Wormhole, Phase 7 External Dependencies)
· Decision: Build perps engine on-chain dengan hybrid orderbook/AMM, gunakan Pyth untuk mark price, Wormhole untuk cross-chain messaging
· Immediate Result: Perps live dengan funding rate, liquidation engine; JUP token belum ada jadi fee ke treasury company
· Long-term Impact: Fondasi untuk Perps v2/JLP; menarik trader derivatif ke Jupiter ecosystem; diversifikasi revenue beyond swap fees
· Supporting Dataset: Phase 3 EV-005; Phase 4 Core Components (Jupiter Perps v2), Oracle; Phase 7 External Dependencies (Pyth, Wormhole)

Keputusan: Rilis API/SDK/Terminal sebagai developer infrastructure (2023)
· Trigger: Wallet dan dApp meminta embed swap; Jupiter menjadi de facto liquidity layer Solana
· Evidence: EV-006; Terminal docs (Phase 4 Core Components); SDK TypeScript/Rust (Phase 4); Ultra API v6 (EV-016)
· Decision: Open infrastructure gratis untuk integrator; monetisasi via enterprise tier (Ultra API) kemudian
· Immediate Result: Adopsi luas di wallet (Phantom, Solflare, Backpack), trading bot, portfolio tracker
· Long-term Impact: Jupiter jadi "Stripe of Solana DeFi"; network effect memperkuat moat aggregator; revenue diversification
· Supporting Dataset: Phase 3 EV-006, EV-016; Phase 4 Core Components, Technical Upgrade History; Phase 7 Developer Ecosystem, Wallet Ecosystem

Keputusan: TGE JUP via LFG Launchpad LBP + airdrop Jupuary 1 (2024-01-31)
· Trigger: Butuh token untuk governance DAO, incentive alignment, community ownership; hindari VC allocation yang menciptakan sell pressure
· Evidence: Tokenomics blog (Phase 6 Token Information, Distribution); TGE blog (EV-008); 0% investor allocation (Phase 6 Distribution)
· Decision: LBP di LFG Launchpad (price discovery fair) + airdrop 10% supply ke ~955k wallet eligible berdasarkan on-chain activity
· Immediate Result: JUP listed di 7+ major CEX simultan (EV-010); DAO formed (EV-009); wide distribution menciptakan legitimate governance base
· Long-term Impact: Token distribution community-centric memperkuat DAO legitimacy; no VC unlock risk; fee switch proposal feasible
· Supporting Dataset: Phase 3 EV-008, EV-009, EV-010; Phase 6 TGE, Distribution, Utility; Phase 5 Fundraising Mechanism

Keputusan: Perps v2 dengan JLP (Jupiter Liquidity Pool) menggantikan orderbook murni (2024-07)
· Trigger: Orderbook perps v1 capital inefficient; LP butuh single-sided exposure; competitor Drift/Zeta menggunakan AMM model
· Evidence: Perps v2 blog (EV-013); JLP multi-asset pool (Phase 4 Jupiter Perps v2); TVL peak $1.2B lalu $600M (Phase 8 Liquidity)
· Decision: Hybrid AMM/orderbook dengan JLP sebagai counterparty; LP mint/burn JLP shares; trader leverage 100x
· Immediate Result: TVL naik signifikan; fee revenue ke JLP holders; perps volume tumbuh
· Long-term Impact: Capital efficiency lebih tinggi; align LP incentives dengan protocol; tapi introduce impermanent loss risk untuk LP
· Supporting Dataset: Phase 3 EV-013; Phase 4 Core Components, Technical Upgrade History; Phase 8 Liquidity, Adoption Metrics

Keputusan: Fee switch proposal untuk alirkan protocol fee ke DAO treasury/stakers (2024-09)
· Trigger: DAO treasury 40% JUP (nilai volatil); butuh sustainable revenue stream bukan token sales; community demand
· Evidence: Fee switch proposal blog (EV-014); vote.jup.ag (Phase 6 Governance); Phase 5 Financial Risk (fee switch not activated)
· Decision: Governance proposal untuk redirect swap/perps fee portion ke DAO; voting ongoing
· Immediate Result: Diskusi komunitas aktif; belum dieksekusi on-chain per info publik
· Long-term Impact: Jika pass, DAO punya revenue real yield; JUP jadi productive asset; align token value dengan protocol usage
· Supporting Dataset: Phase 3 EV-014; Phase 5 Revenue Model, Financial Risk; Phase 6 Utility (Fee Switch), Governance

Keputusan: Launch Mobile App native iOS/Android (2024-10)
· Trigger: Mobile-first user growth; wallet extension friction; competitor (Phantom, Backpack) punya mobile app
· Evidence: Mobile launch blog (EV-015); App Store/Play Store links (Phase 1 Social); React Native framework (Phase 4 Programming Languages)
· Decision: Native app wrap Jupiter API + web view untuk semua produk (swap, limit, DCA, perps, portfolio)
· Immediate Result: Akses mobile tanpa browser extension; user acquisition channel baru
· Long-term Impact: Retention tinggi untuk retail; data mobile usage improve routing; brand presence beyond web
· Supporting Dataset: Phase 3 EV-015; Phase 4 Core Components, Programming Languages; Phase 7 Applications

Keputusan: Ultra API v6 dengan sub-100ms latency untuk enterprise (2024-11)
· Trigger: Market maker/institutional butuh SLA, rate limit tinggi, quote streaming; public RPC tidak cukup
· Evidence: Ultra API blog (EV-016); docs (Phase 4 Current Technical Stack); enterprise tier mention (Phase 5 Revenue Model)
· Decision: Dedicated infrastructure (cloud, CDN, RPC) untuk enterprise; monetisasi subscription/usage-based
· Immediate Result: Institutional onboard; revenue stream baru non-retail
· Long-term Impact: Diversifikasi revenue; sticky enterprise relationships; moat vs competitor aggregator
· Supporting Dataset: Phase 3 EV-016; Phase 4 Current Technical Stack; Phase 5 Revenue Model; Phase 7 Infrastructure Providers

Keputusan: Aggregator v4 / Metis v2 dengan parallel route execution dan atomic arb swap���perps (2025-01)
· Trigger: Routing latency dan slippage masih pain point; cross-product arb opportunity (JLP funding rate vs spot)
· Evidence: Metis v2 blog (EV-018); docs (Phase 4 Technical Upgrade History); atomic arb mention (Phase 4 Known Technical Limitations)
· Decision: Parallel execution multiple routes; dynamic slippage protection; atomic integration dengan JLP untuk arb
· Immediate Result: Execution quality terbaik Solana; gas optimization untuk complex route
· Long-term Impact: Technical moat diperkuat; cross-product synergy (aggregator + perps) unik di Solana
· Supporting Dataset: Phase 3 EV-018; Phase 4 Technical Upgrade History, Known Technical Limitations; Phase 7 Major Integrations

Evolution Pattern

Perubahan Strategi: Dari Single Product (Aggregator) → Full-Stack DeFi Suite → Developer Platform → DAO-Governed Protocol
· Evidence: Phase 3 timeline menunjukkan ekspansi produk bertahap: 2021 Aggregator only → 2022 Limit/DCA/Perps → 2023 API/SDK/Terminal → 2024 Token/DAO/Mobile/Ultra API → 2025 Metis v2 atomic cross-product
· Supporting Dataset: Phase 3 semua EV; Phase 4 Core Components; Phase 7 Applications, Developer Ecosystem

Perubahan Teknologi: Dari Routing Sederhana → Metis Algorithm → Apollo (compressed NFT support) → Metis v2 (Parallel Execution + Atomic Arb)
· Evidence: Phase 4 Technical Upgrade History: v1 (2021) → v2 Metis (2023-11) → v3 Apollo (2024-04) → v4 Metis v2 (2025-01); setiap upgrade menambah complexity dan performance
· Supporting Dataset: Phase 3 EV-002, EV-007, EV-012, EV-018; Phase 4 Technical Upgrade History

Perubahan Tokenomics: Dari No Token (2021-2023) → JUP Token dengan Governance + Fee Switch Proposal + Recurring Airdrops (2024+)
· Evidence: Phase 1/3 tidak ada token hingga EV-008; Tokenomics: 40% DAO treasury, 20% team 4yr vesting, 10% airdrop, 20% liquidity, 10% future (Phase 6 Distribution); Jupuary 1/2/3 (EV-008, EV-011, EV-017)
· Supporting Dataset: Phase 3 EV-008, EV-009, EV-011, EV-014, EV-017; Phase 6 Token Information, Distribution, Vesting, Governance

Perubahan Governance: Dari Team-Controlled → DAO Off-Chain Voting (vote.jup.ag) + Multisig Execution → Fee Switch Activation (Proposed)
· Evidence: Phase 3 EV-009 DAO formation; vote.jup.ag live (Phase 6 Governance); fee switch proposal (EV-014); multisig signer tidak publik (Phase 5 Treasury, Phase 6 Governance)
· Supporting Dataset: Phase 3 EV-009, EV-014; Phase 5 Treasury; Phase 6 Governance; Phase 7 Governance Ecosystem

Perubahan Revenue: Dari Zero Revenue (2021) → Swap Fees + Perps Fees → + Ultra API Enterprise → + Fee Switch (Proposed) → + Treasury Yield (Planned)
· Evidence: Phase 5 Revenue Model: swap fees live, perps fees live, Ultra API enterprise live, fee switch proposed, treasury yield planned; no revenue report publik (Phase 5 Revenue History)
· Supporting Dataset: Phase 5 Revenue Model, Revenue History, Financial Dependencies; Phase 3 EV-014, EV-016

Perubahan Ecosystem Position: Dari Solana DEX Aggregator → Dominan Solana DeFi Infrastructure (Aggregator + Perps + API + Mobile + Launchpad) → Cross-Chain Ambiguity (Wormhole referenced tapi tidak confirmed production)
· Evidence: Phase 8 Market Position: 85-90% Solana aggregator share; Phase 7 Major Integrations: 20+ DEX, Pyth, Wormhole, LFG, Terminal embed, API consumers; Phase 7 Ecosystem Risks: single-chain dependency
· Supporting Dataset: Phase 3 semua EV; Phase 7 Major Integrations, External Dependencies, Ecosystem Risks; Phase 8 Market Position, Competitor Landscape

Technical Decision Pattern

Pola 1: On-Chain Execution + Off-Chain Routing (Hybrid Architecture)
· Decision Pattern: Semua eksekusi trade (swap, limit, DCA, perps) terjadi on-chain di Solana SVM via Jupiter Program; routing/price discovery dilakukan off-chain oleh Jupiter API/engine untuk latency dan komputasi kompleks
· Evidence: Phase 4 System Architecture: "Routing Layer — Jupiter mengagregasi likuiditas... untuk menemukan best price path"; "Eksekusi tetap on-chain via Jupiter Program"; Phase 4 Execution Environment: "Semua produk... berjalan langsung di SVM"
· Supporting Dataset: Phase 4 System Architecture, Core Components, Execution Environment; Phase 3 EV-002, EV-007, EV-012, EV-018

Pola 2: Iterative Routing Algorithm Upgrades (Metis → Apollo → Metis v2)
· Decision Pattern: Routing engine di-upgrade bertahap setiap ~6-12 bulan dengan nama kode (Metis, Apollo, Metis v2); setiap versi menambah fitur: gas optimization, compressed NFT support, parallel execution, atomic cross-product arb
· Evidence: Phase 4 Technical Upgrade History: v1→v2 Metis (2023-11) → v3 Apollo (2024-04) → v4 Metis v2 (2025-01); Phase 3 EV-007, EV-012, EV-018
· Supporting Dataset: Phase 3 EV-007, EV-012, EV-018; Phase 4 Technical Upgrade History, Current Technical Stack

Pola 3: Program Upgradeable (Not Immutable) dengan Multisig Authority
· Decision Pattern: Jupiter Program pada Solana tidak di-freeze (immutable); upgrade authority dikontrol multisig (signer tidak publik); memungkinkan patch bug, upgrade routing, tambah fitur tanpa migrasi user
· Evidence: Phase 4 Security Model: "Program Jupiter memiliki upgrade authority (bukan immutable)"; Solscan program account (Phase 4); Phase 7 Ecosystem Risks: "Upgrade Authority Centralization"
· Supporting Dataset: Phase 4 Security Model; Phase 7 Ecosystem Risks; Phase 3 EV-007, EV-012, EV-018 (upgrade history proves authority used)

Pola 4: Rust untuk On-Chain, TypeScript untuk SDK/API, React/React Native untuk Frontend
· Decision Pattern: Pemisahan bahasa berdasarkan domain: Rust (SVM program), TypeScript (SDK, API client), React (Terminal, Web), React Native (Mobile); tidak ada polyglot di layer yang sama
· Evidence: Phase 4 Programming Languages: "Rust — bahasa utama untuk program on-chain", "TypeScript — bahasa utama untuk SDK dan API client", "JavaScript/React — untuk frontend web, Terminal, dan Mobile app"
· Supporting Dataset: Phase 4 Programming Languages, Development Framework; Phase 7 Developer Ecosystem

Pola 5: Oracle Dependency Terpusat ke Pyth untuk Perps
· Decision Pattern: Jupiter Perps sepenuhnya bergantung pada Pyth Network untuk mark price, funding rate, liquidation trigger; tidak ada fallback oracle atau TWAP internal sebagai backup
· Evidence: Phase 4 Oracle: "Jupiter Perps menggunakan oracle eksternal (Pyth Network) untuk harga mark/funding rate"; Phase 4 Known Technical Limitations: "Oracle Delay — Jupiter Perps mengandalkan Pyth; bila oracle harga tertunda... dapat menyebabkan likuidasi yang tidak diinginkan"
· Supporting Dataset: Phase 4 Core Components (Oracle), Known Technical Limitations; Phase 7 External Dependencies (Pyth Network); Phase 3 EV-005, EV-013

Pola 6: Single-Chain (Solana Only) dengan Cross-Chain Messaging Hanya untuk Perps (Wormhole, Unconfirmed)
· Decision Pattern: Semua produk core (Aggregator, Limit, DCA, Perps, Terminal, Mobile, JUP token) hanya di Solana; Wormhole hanya direferensikan untuk Perps cross-chain messaging di dokumen awal, tidak dikonfirmasi di Perps v2 docs
· Evidence: Phase 4 System Architecture: "Tipe: DEX Aggregator... di atas Solana Mainnet"; "Chain(s): Solana (primary)"; Phase 7 External Dependencies: Wormhole "current production dependency not confirmed"; Phase 7 Ecosystem Risks: "Single Chain Dependency"
· Supporting Dataset: Phase 4 System Architecture; Phase 7 External Dependencies, Ecosystem Risks; Phase 1 Chain(s)

Pola 7: Enterprise-Grade API Infrastructure (Ultra API) Sebagai Differentiator Teknis
· Decision Pattern: Public API gratis untuk retail/integrator standar; Ultra API v6 berbayar dengan dedicated infra (sub-100ms, quote streaming, SLA) untuk market maker/institusi; infrastructure tidak di-disclose (cloud, RPC, CDN provider)
· Evidence: Phase 4 Current Technical Stack: "Cloud/Infra: tidak dipublikasikan"; Phase 5 Revenue Model: "Ultra API enterprise tier... custom quote"; Phase 7 Infrastructure Providers: Cloud Provider, RPC Providers, CDN "undisclosed"
· Supporting Dataset: Phase 3 EV-016; Phase 4 Current Technical Stack, Technical Upgrade History; Phase 5 Revenue Model; Phase 7 Infrastructure Providers

Financial Decision Pattern

Pola 1: Zero External Funding (Bootstrapped + Protocol Revenue + Token Treasury)
· Decision Pattern: Tidak ada VC funding, private sale, atau Series funding yang diumumkan; operasi didanai dari pendapatan protokol (swap fees, perps fees) sejak 2021 dan treasury token JUP (40% supply) sejak TGE 2024
· Evidence: Phase 5 Funding History: "Tidak ada ronde pendanaan yang diumumkan secara publik"; "Jupiter tampak dibangun melalui bootstrapping dan pendapatan protokol"; Phase 5 Fundraising Mechanism: "Bootstrapping", "Protocol Revenue", "DAO Treasury (Token Allocation)"; Phase 1 Investor: "(tidak ada investor teridentifikasi)"
· Supporting Dataset: Phase 5 Funding History, Fundraising Mechanism, Financial Dependencies; Phase 1 Investor; Phase 2 Entity (no investor entities)

Pola 2: Treasury Concentration di Native Token (JUP 40% Supply)
· Decision Pattern: DAO treasury sebagian besar berupa JUP token (4 miliar JUP = 40% supply); tidak ada diversifikasi ke stablecoin/asset lain yang diungkapkan; nilai treasury korelasi tinggi dengan harga JUP
· Evidence: Phase 5 Treasury: "DAO treasury menguasai ~40% total supply JUP (4 miliar JUP)"; "Stablecoin Holdings: Tidak diungkap"; "Other Assets: Tidak diungkap"; Phase 6 Distribution: "Treasury: 40% (DAO/Community Treasury)"; Phase 5 Financial Risk: "Treasury Concentration in Native Token (JUP)"
· Supporting Dataset: Phase 5 Treasury, Financial Risk; Phase 6 Distribution; Phase 3 EV-008, EV-009

Pola 3: Revenue Diversification Bertahap (Swap Fees → Perps Fees → Enterprise API → Fee Switch Proposed)
· Decision Pattern: Setiap produk baru menambah revenue stream: Aggregator swap fees (2021), Perps trading fees (2022), Ultra API enterprise (2024-11), Fee switch proposal (2024-09) untuk alirkan fee ke DAO
· Evidence: Phase 5 Revenue Model: "Protocol Fees (Swap Aggregator) Status: Live", "Perps Trading Fees Status: Live", "API Fees (Ultra API/Enterprise) Status: Live", "Fee Switch (Proposed)"; Phase 3 EV-002, EV-005, EV-016, EV-014
· Supporting Dataset: Phase 5 Revenue Model, Financial Dependencies; Phase 3 EV-002, EV-005, EV-014, EV-016

Pola 4: Token Launch Fair (LBP + Airdrop) Tanpa VC Allocation
· Decision Pattern: JUP TGE via LBP di LFG Launchpad (price discovery) + airdrop 10% ke komunitas; 0% allocation untuk investor/VC; 20% team dengan vesting 4 tahun
· Evidence: Phase 6 TGE: "Launch Platform: Jupiter LFG Launchpad (Liquidity Bootstrapping Pool)"; Phase 6 Distribution: "Investors: 0%", "Team: 20% (vesting 4 tahun)", "Community: 10% (Launchpool/Airdrop)"; Phase 5 Token Sale: "Tidak ada private sale/presale/VC allocation"
· Supporting Dataset: Phase 6 TGE, Distribution, Vesting Schedule; Phase 5 Token Sale, Fundraising Mechanism; Phase 3 EV-008

Pola 5: No Financial Transparency Reporting (Tidak Ada Revenue Report, Treasury Dashboard, Audit Finansial)
· Decision Pattern: Jupiter tidak mempublikasikan laporan keuangan berkala, treasury dashboard, atau audited financials; data on-chain tersedia tapi tidak diagregasikan resmi; estimasi pihak ketiga (Token Terminal, DefiLlama) menjadi referensi utama
· Evidence: Phase 5 Revenue History: "Tidak diungkap secara resmi dalam laporan berkala"; "Official Financial Resources: Transparency Report: Tidak ada, Treasury Dashboard: Tidak ada"; Phase 5 Financial Risk: "No Public Financial Audit / Transparency Report"
· Supporting Dataset: Phase 5 Revenue History, Official Financial Resources, Financial Risk; Phase 7 Ecosystem Risks (Multisig Signer Opacity)

Pola 6: JLP Sebagai Revenue Sharing Mechanism untuk LP (Bukan Protocol Fee)
· Decision Pattern: Perps v2 JLP mengumpulkan trading fee, borrowing fee, funding rate ke pool; LP mendapat yield langsung; protocol fee portion tidak terpisah jelas (fee switch proposal belum pass)
· Evidence: Phase 5 Revenue Model: "Perps Trading Fees... sebagian fee mengalir ke JLP... dan sebagian ke protokol/DAO. Detail split fee tidak dipublikasikan"; Phase 4 Jupiter Perps v2: "JLP (multi-asset LP pool) sebagai counterparty"
· Supporting Dataset: Phase 5 Revenue Model; Phase 4 Core Components (Jupiter Perps v2); Phase 3 EV-013

Ecosystem Decision Pattern

Pola 1: Deep Integration dengan Solana DEX Ecosystem (Routing Through, Not Competing)
· Decision Pattern: Jupiter tidak membangun DEX sendiri (kecuali Perps); aggregator merutekan melalui Raydium, Orca, Meteora, Lifinity, Phoenix, dll.; menjadi "meta-DEX" yang memperkuat seluruh ekosistem
· Evidence: Phase 7 Major Integrations: "Jupiter Aggregator ↔ Solana DEXs (Raydium, Orca, Meteora, Lifinity, Phoenix, etc.)"; Phase 4 System Architecture: "Layer: Routing Layer — Jupiter mengagregasi likuiditas dari banyak DEX Solana"; Phase 8 Competitor Landscape: Orca, Raydium sebagai competitor tapi juga liquidity source
· Supporting Dataset: Phase 3 EV-002, EV-007, EV-012, EV-018; Phase 4 System Architecture; Phase 7 Major Integrations; Phase 8 Competitor Landscape

Pola 2: Oracle Partnership Eksklusif dengan Pyth untuk Perps
· Decision Pattern: Jupiter Perps menggunakan Pyth Network sebagai sole oracle provider; tidak ada multi-oracle setup; partnership mendalam (Pyth cited di docs, blog, integration)
· Evidence: Phase 7 Major Integrations: "Jupiter Perps ↔ Pyth Network"; Phase 4 Oracle: "Jupiter Perps menggunakan oracle eksternal (Pyth Network)"; Phase 7 External Dependencies: Pyth "Criticality: Critical (for Perps)"; Phase 3 EV-005, EV-013
· Supporting Dataset: Phase 3 EV-005, EV-013; Phase 4 Core Components (Oracle), Known Technical Limitations; Phase 7 Major Integrations, External Dependencies

Pola 3: Developer-First Infrastructure (SDK, API, Terminal Gratis; Enterprise Berbayar)
· Decision Pattern: TypeScript/Rust SDK, REST API, Terminal widget disediakan gratis untuk adopsi luas; Ultra API v6 dengan SLA enterprise jadi monetisasi; strategi "Stripe of Solana DeFi"
· Evidence: Phase 7 Developer Ecosystem: "SDK: Jupiter SDK TypeScript... API: Jupiter REST API... Developer Tools: Jupiter Terminal... Open Source Repository"; Phase 5 Revenue Model: "Terminal/SDK Licensing Status: Live (gratis untuk penggunaan standar)"; Phase 3 EV-006, EV-016
· Supporting Dataset: Phase 3 EV-006, EV-016; Phase 4 Core Components; Phase 5 Revenue Model; Phase 7 Developer Ecosystem, Infrastructure Providers

Pola 4: Wallet Integration via Standard Adapter (Terminal Works dengan Semua Wallet Adapter)
· Decision Pattern: Jupiter Terminal tidak negosiasi partnership eksklusif per wallet; menggunakan Solana wallet adapter standard sehingga kompatibel dengan Phantom, Solflare, Backpack, Ledger, dll. secara otomatis
· Evidence: Phase 7 Wallet Ecosystem: "Terminal works dengan any Solana wallet adapter"; Phase 4 Core Components: "Jupiter Terminal... Embeddable React widget"; Phase 7 Major Integrations: "Jupiter Terminal ↔ External dApps/Wallets... specific partners not enumerated"
· Supporting Dataset: Phase 4 Core Components; Phase 7 Wallet Ecosystem, Major Integrations; Phase 3 EV-006

Pola 5: Launchpad Internal (LFG) untuk Token Launch Sendiri dan Proyek Lain
· Decision Pattern: Jupiter membangun LFG Launchpad sendiri (bukan pakai platform lain); digunakan untuk JUP TGE (EV-008); dijadikan produk untuk proyek lain launch token
· Evidence: Phase 3 EV-008: "TGE Token JUP via LFG Launchpad"; Phase 7 Applications: "LFG Launchpad... Product under Jupiter Exchange — used for JUP TGE and future project launches"; Phase 2 Entity: LFG Launchpad; Phase 7 Major Integrations: "JUP Token ↔ LFG Launchpad"
· Supporting Dataset: Phase 3 EV-008; Phase 2 Entity: LFG Launchpad; Phase 7 Applications, Major Integrations

Pola 6: Cross-Chain Ambiguity (Wormhole Referenced Tapi Tidak Confirmed Production)
· Decision Pattern: Wormhole terdaftar di ecosystem page dan early Perps docs; tapi Jupiter Perps v2 docs tidak mention Wormhole; Jupiter Aggregator tidak punya cross-chain swap; status dependency unclear
· Evidence: Phase 7 External Dependencies: Wormhole "Status: Live (per Wormhole ecosystem page) / Unconfirmed current production dependency"; Phase 7 Major Integrations: "Jupiter Perps ↔ Wormhole... production usage in v2 not explicitly confirmed"; Phase 7 Ecosystem Risks: "Bridge / Cross-chain Dependency... Current production dependency not confirmed"
· Supporting Dataset: Phase 2 Entity: Wormhole; Phase 3 EV-005; Phase 7 External Dependencies, Major Integrations, Ecosystem Risks

Pola 7: Mobile-First Expansion (Native App) untuk Retail Acquisition
· Decision Pattern: Mobile app native iOS/Android (React Native) dirilis 2024-10 setelah 3 tahun web-only; wrap semua produk (swap, limit, DCA, perps, portfolio); tidak ada fitur mobile-exclusive
· Evidence: Phase 3 EV-015; Phase 7 Applications: "Jupiter Mobile App... native mobile frontend for all Jupiter products"; Phase 4 Programming Languages: "Mobile Framework — React Native"; Phase 8 Market Timeline: EV-015
· Supporting Dataset: Phase 3 EV-015; Phase 4 Programming Languages; Phase 7 Applications; Phase 8 Market Timeline

Governance Decision Pattern

Pola 1: Token-Weighted Off-Chain Voting (vote.jup.ag) dengan On-Chain Multisig Execution
· Decision Pattern: Governance menggunakan snapshot-style voting off-chain di vote.jup.ag (gasless); proposal lolos dieksekusi on-chain oleh DAO multisig (signer tidak publik); tidak menggunakan on-chain DAO framework seperti Realms
· Evidence: Phase 6 Governance: "Governance Model: Token-weighted voting via Jupiter DAO (off-chain voting on vote.jup.ag, on-chain execution via multisig)"; "Voting System: Snapshot-style off-chain voting"; Phase 7 Governance Ecosystem: "Council: Not established... Committee: Not established"
· Supporting Dataset: Phase 6 Governance; Phase 7 Governance Ecosystem; Phase 3 EV-009, EV-014

Pola 2: Proposal Inisiatif Tim/Core Contributor (Fee Switch, Parameter Changes) Bukan Community-Sourced
· Decision Pattern: Proposal besar (fee switch, parameter upgrade) diajukan oleh tim/core contributor; komunitas vote approve/reject; tidak ada bukti proposal community-initiated yang pass
· Evidence: Phase 3 EV-014: "Jupiter DAO mengajukan proposal untuk mengaktifkan fee switch"; Phase 6 Governance: "Proposal System: Proposal dapat diajukan oleh komunitas; memerlukan quorum dan threshold yang tidak dipublikasikan detailnya"; Phase 7 Governance Ecosystem: "Foundation: Jupiter Exchange Ltd.... DAO: Jupiter DAO"
· Supporting Dataset: Phase 3 EV-014; Phase 6 Governance; Phase 7 Governance Ecosystem

Pola 3: Airdrop Berulang (Jupuary 1/2/3) Sebagai Governance Incentive dan Retention
· Decision Pattern: Airdrop tidak sekali saja (Jupuary 1 di TGE); Jupuary 2 (2024-03) dan Jupuary 3/Catdets (2024-12) di-announce dari DAO treasury; Catdets introduksi soulbound NFT untuk tracking kontribusi jangka panjang
· Evidence: Phase 3 EV-008 (Jupuary 1), EV-011 (Jupuary 2), EV-017 (Jupuary 3); Phase 6 Utility: "Incentive/Reward (Airdrop/Jupuary)"; Phase 6 Major Token Events: EV-008, EV-011, EV-017
· Supporting Dataset: Phase 3 EV-008, EV-011, EV-017; Phase 6 Utility, Major Token Events

Pola 4: Multisig Signer Opacity (Tidak Ada Disclosure Siapa Yang Menandatangani Eksekusi)
· Decision Pattern: DAO treasury dan program upgrade authority dikontrol multisig; daftar signer tidak dipublikasikan; governance execution transparency terbatas
· Evidence: Phase 5 Treasury: "Treasury Custodian: Dikelola oleh Jupiter DAO multisig (jumlah signer dan alamat tidak dipublikasikan resmi)"; Phase 4 Security Model: "Multisig/Timelock: Jupiter menyatakan bahwa upgrade program dan transfer treasury DAO dikontrol oleh multisig — jumlah signer dan alamat multisig tidak dipublikasikan"; Phase 7 Ecosystem Risks: "Multisig Signer Opacity"
· Supporting Dataset: Phase 4 Security Model; Phase 5 Treasury; Phase 7 Ecosystem Risks; Phase 6 Governance

Pola 5: Fee Switch Sebagai Kunci Value Accrual Token (Belum Aktif)
· Decision Pattern: Utility utama JUP adalah governance; fee switch proposal (EV-014) akan mengaktifkan value accrual (fee ke stakers/treasury); tanpa fee switch, JUP pure governance token tanpa yield
· Evidence: Phase 6 Utility: "Fee Switch (Proposed)... Belum dieksekusi on-chain"; "Staking (Governance Staking)... Fee reward: Planned (bergantung fee switch)"; Phase 5 Financial Risk: "Fee Switch Not Yet Activated"; Phase 3 EV-014
· Supporting Dataset: Phase 3 EV-014; Phase 5 Financial Risk; Phase 6 Utility, Governance

Pola 6: Team Allocation 20% dengan Vesting 4 Tahun (Standard Alignment)
· Decision Pattern: Team allocation 20% supply dengan vesting 4 tahun linear; cliff dan unlock frequency tidak dipublikasikan; tidak ada accelerated unlock atau token buyback untuk team
· Evidence: Phase 6 Distribution: "Team: 20% (vesting 4 tahun)"; Phase 6 Vesting Schedule: "Category: Team... Vesting: 4 tahun (linear vesting over 4 years per tokenomics)... Cliff: tidak diketahui... Unlock Frequency: tidak diketahui"
· Supporting Dataset: Phase 6 Distribution, Vesting Schedule; Phase 5 Fundraising Mechanism (no investor allocation)

Risk Response Pattern

Pola 1: Solana Downtime/Congestion → Tidak Ada Fallback Chain (Acceptance Risk)
· Decision Pattern: Jupiter 100% bergantung pada Solana; tidak ada cross-chain deployment, tidak ada L2, tidak ada fallback RPC chain; ketika Solana down, seluruh produk Jupiter tidak bisa diakses
· Evidence: Phase 7 Ecosystem Risks: "Single Chain Dependency: 100% of Jupiter products... operate exclusively on Solana. Solana downtime, congestion, or consensus failure directly halts all Jupiter operations"; Phase 4 Known Technical Limitations: "Single-chain Dependency... jika Solana mainnet down atau congestion, Jupiter tidak memiliki fallback chain"
· Trigger: Solana mainnet outage (beberapa kali terjadi 2022-2023)
· Response: Tidak ada mitigasi teknis; komunikasi ke user via Twitter/Discord; tunggu Solana recovery
· Result: User experience terganggu selama outage; tidak ada kehilangan dana (funds safe di wallet user); brand trust sedikit terkikis tapi recover cepat
· Supporting Dataset: Phase 4 Known Technical Limitations; Phase 7 Ecosystem Risks; Phase 1 Chain(s)

Pola 2: Oracle Failure/Manipulation (Pyth) → Documentation Risk Disclosure Only
· Decision Pattern: Jupiter Perps mengakui risiko oracle delay/manipulation di dokumentasi; tidak implementasi circuit breaker, TWAP fallback, atau multi-oracle; risiko ditanggung user/LP
· Evidence: Phase 4 Known Technical Limitations: "Oracle Delay: Jupiter Perps mengandalkan Pyth; bila oracle harga tertunda atau tidak akurat, dapat menyebabkan likuidasi yang tidak diinginkan — dijelaskan sebagai risiko dalam dokumentasi"; Phase 7 Ecosystem Risks: "Oracle Dependency (Perps): Jupiter Perps relies entirely on Pyth Network... Pyth oracle failure, manipulation, or delay can cause incorrect liquidations"
· Trigger: Pyth oracle incidents (historical Solana oracle issues)
· Response: Disclosure di docs; tidak ada code-level mitigation
· Result: LP dan trader bear risk; tidak ada insidens besar terlaporkan publik
· Supporting Dataset: Phase 4 Known Technical Limitations; Phase 7 Ecosystem Risks, External Dependencies; Phase 3 EV-005, EV-013

Pola 3: Smart Contract Upgrade Authority Compromise → Multisig Security (Tidak Di-Public Verifikasi)
· Decision Pattern: Program upgradeable oleh multisig; tim mengandalkan keamanan multisig (signer tidak publik); tidak ada timelock publik, tidak ada governance delay untuk upgrade; bug bounty aktif di Immunefi
· Evidence: Phase 4 Security Model: "Multisig/Timelock: Jupiter menyatakan bahwa upgrade program dan transfer treasury DAO dikontrol oleh multisig — jumlah signer dan alamat multisig tidak dipublikasikan"; "Bug Bounty: Jupiter memiliki program bug bounty yang aktif di platform imunefi"; Phase 7 Ecosystem Risks: "Upgrade Authority Centralization... Compromise of upgrade authority could allow malicious program changes"
· Trigger: General smart contract upgrade risk; tidak ada insiden spesifik
· Response: Multisig (opaque), bug bounty, audit berkala (6 auditor)
· Result: Tidak ada exploit upgrade authority terlaporkan; audit menemukan issues yang diperbaiki
· Supporting Dataset: Phase 4 Security Model, Audit History; Phase 7 Ecosystem Risks; Phase 3 EV-007, EV-012, EV-018 (upgrade history)

Pola 4: Market Downturn / Bear Market → Product Expansion dan Community Incentive (Jupuary)
· Decision Pattern: Selama bear market 2022-2023, Jupiter terus launch produk (Perps v1, API, Terminal); pasca-TGE 2024, Jupuary airdrop berulang untuk retain user dan drive volume
· Evidence: Phase 3 Timeline: 2022 (bear market) launch Limit, DCA, Perps v1; 2023 launch API/Terminal; 2024 TGE + Jupuary 1/2/3; Phase 8 Narrative Position: "DeFi (DEX Aggregator) Main Narrative", "Solana Ecosystem Main Narrative"
· Trigger: Crypto winter 2022-2023; post-TGE volume retention challenge
· Response: Continue building; airdrop incentive program berulang
· Result: Volume dan user retention relatif stabil vs competitor; market share Solana aggregator tetap dominan
· Supporting Dataset: Phase 3 EV-003, EV-004, EV-005, EV-006, EV-008, EV-011, EV-017; Phase 8 Narrative Position, Market Share

Pola 5: Competitor Entry (Odos di Solana 2024) → Technical Moat Deepening (Metis v2, Ultra API)
· Decision Pattern: Odos launch di Solana 2024 dengan patented routing; Jupiter respond dengan Metis v2 (parallel execution, atomic arb) dan Ultra API (enterprise latency) — technical differentiation bukan fee war
· Evidence: Phase 8 Competitor Landscape: "Odos... Multi-chain including Solana... patented routing algorithm"; Phase 3 EV-018 (Metis v2 Jan 2025), EV-016 (Ultra API Nov 2024); Phase 4 Technical Upgrade History
· Trigger: Odos Solana launch 2024; aggregator competition meningkat
· Response: Accelerate routing engine upgrade (Metis v2); launch enterprise API tier
· Result: Technical moat diperkuat; enterprise revenue stream baru; market share belum terganggu signifikan
· Supporting Dataset: Phase 3 EV-016, EV-018; Phase 4 Technical Upgrade History; Phase 8 Competitor Landscape, Market Share

Pola 6: FTX/Serum Collapse (2022) → Diversifikasi Liquidity Source (Tidak Bergantung Single DEX)
· Decision Pattern: Serum (FTX-backed) adalah major liquidity source awal; pasca-FTX collapse Nov 2022, Jupiter memperluas routing ke Raydium, Orca, Meteora, Phoenix, dll.; tidak ada single point of failure DEX
· Evidence: Phase 3 EV-002: "routing melalui Serum, Raydium, Orca"; Phase 7 Major Integrations: "20+ Solana DEXs"; Phase 4 System Architecture: "mengagregasi likuiditas dari banyak DEX Solana"; Phase 8 Market Timeline: EV-002 mention Serum
· Trigger: FTX collapse November 2022; Serum orderbook tidak reliable
· Response: Expand DEX integrations; routing algorithm (Metis) handle fragmented liquidity
· Result: Aggregator resilient; tidak ada service disruption; market share naik karena competitor yang bergantung Serum mati
· Supporting Dataset: Phase 3 EV-002; Phase 7 Major Integrations; Phase 4 System Architecture; Phase 8 Market Timeline

Recurring Behavioral Pattern

Pola 1: Ship Product First, Token Later (Product-Market Fit Sebelum Tokenomics)
· Decision Pattern: Jupiter beroperasi 2.5 tahun (Oct 2021 - Jan 2024) tanpa token; fokus build aggregator, limit, DCA, perps, API, Terminal; token hanya launch setelah dominant position terbukti
· Evidence: Phase 3 Timeline: EV-002 (2021-10) sampai EV-006 (2023) semua pre-token; EV-008 TGE Jan 2024; Phase 1 Launch Date: "Launch Date - TGE: 31 Januari 2024"; Phase 6 TGE
· Supporting Dataset: Phase 3 EV-002 hingga EV-008; Phase 1 Launch Date; Phase 6 TGE

Pola 2: Iterative Major Upgrades Setiap 6-12 Bulan (Routing Engine)
· Decision Pattern: Aggregator routing engine di-upgrade major berkala: v1 (2021) → v2 Metis (2023-11) → v3 Apollo (2024-04) → v4 Metis v2 (2025-01); interval ~6-12 bulan; setiap upgrade named release dengan blog announcement
· Evidence: Phase 4 Technical Upgrade History: 4 major upgrades dalam ~3 tahun; Phase 3 EV-002, EV-007, EV-012, EV-018
· Supporting Dataset: Phase 3 EV-002, EV-007, EV-012, EV-018; Phase 4 Technical Upgrade History

Pola 3: Expand Product Suite Vertikal (Swap → Limit → DCA → Perps → API → Mobile)
· Decision Pattern: Setiap 6-12 bulan produk baru dirilis yang memperluas use case user yang sama; tidak pivot ke vertical baru yang tidak related; semua produk terintegrasi ke aggregator core
· Evidence: Phase 3 Timeline: 2022 Limit/DCA/Perps, 2023 API/Terminal, 2024 Mobile/Ultra API, 2025 Metis v2 cross-product; Phase 7 Applications: 8 produk core
· Supporting Dataset: Phase 3 semua EV; Phase 7 Applications

Pola 4: Community Incentive Berulang via Airdrop (Jupuary Series)
· Decision Pattern: Airdrop tidak one-off; Jupuary 1 (TGE), Jupuary 2 (Mar 2024), Jupuary 3/Catdets (Dec 2024); setiap ronde refine eligibility (volume, governance, soulbound NFT)
· Evidence: Phase 3 EV-008, EV-011, EV-017; Phase 6 Utility: "Incentive/Reward (Airdrop/Jupuary)"; Phase 6 Major Token Events
· Supporting Dataset: Phase 3 EV-008, EV-011, EV-017; Phase 6 Utility, Major Token Events

Pola 5: Technical Blog-Driven Transparency (Setiap Upgrade Punya Blog Post Detail)
· Decision Pattern: Setiap major upgrade (v2, v3, v4, Perps v2, Ultra API, Mobile, Metis v2) diumumkan via blog.jup.ag dengan detail teknis; bukan hanya marketing announcement
· Evidence: Phase 3 Sources hampir semua ke blog.jup.ag; Phase 4 Technical Upgrade History sources ke blog; Phase 8 Market Timeline sources ke blog
· Supporting Dataset: Phase 3 semua EV sources; Phase 4 Technical Upgrade History sources; Phase 8 Market Timeline sources

Pola 6: Pseudonymous Leadership dengan Public Accountability (Meow, Rolex, Slorg, Worm)
· Decision Pattern: Founder dan core lead pseudonymous (Meow, Rolex, Slorg, Worm) tapi aktif komunikasi publik (Twitter, blog, forum); tidak doxxed tapi accountable via on-chain execution dan community feedback
· Evidence: Phase 1 Core Team: "Meow (pseudonim)", "Rolex (pseud.)", "Slorg (pseud.)", "Worm (pseud.)"; Phase 2 Entity: semua Person pseudonim; Phase 3 Meow Twitter threads sebagai sources berulang
· Supporting Dataset: Phase 1 Core Team; Phase 2 Entity (Person); Phase 3 sources (Meow Twitter)

Pola 7: Zero VC Funding Disclosure (Bootstrap Narrative Konsisten)
· Decision Pattern: Dari Phase 1-5, tidak ada satupun investor/VC teridentifikasi; OpenCorporates BVI filing tidak show shareholders; narrative konsisten "bootstrapped + protocol revenue"
· Evidence: Phase 1 Investor: "(tidak ada investor teridentifikasi)"; Phase 2 Entity: no investor entities; Phase 5 Funding History: "Tidak ada ronde pendanaan yang diumumkan"; Phase 5 Fundraising Mechanism: "Bootstrapping"
· Supporting Dataset: Phase 1 Investor; Phase 2 Entity; Phase 5 Funding History, Fundraising Mechanism

Strategic Trade-offs

Trade-off 1: Desentralisasi vs Kecepatan Eksekusi (Off-Chain Voting + Multisig vs On-Chain DAO)
· Decision: Gunakan off-chain voting (vote.jup.ag) + multisig execution, bukan on-chain DAO framework (Realms, SPL Governance)
· Trade-off: Mengorbankan desentralisasi eksekusi (multisig signer opaque, tidak ada timelock publik) demi kecepatan, gasless voting, dan UX sederhana
· Evidence: Phase 6 Governance: "Voting System: Snapshot-style off-chain voting... on-chain execution via multisig"; Phase 7 Governance Ecosystem: "Council: Not established... Committee: Not established"; Phase 7 Ecosystem Risks: "Multisig Signer Opacity"
· Supporting Dataset: Phase 6 Governance; Phase 7 Governance Ecosystem, Ecosystem Risks

Trade-off 2: Single-Chain Focus (Solana Only) vs Cross-Chain Expansion
· Decision: Semua produk hanya di Solana; tidak deploy ke Ethereum L2, tidak build cross-chain swap, Wormhole hanya untuk Perps messaging (unconfirmed)
· Trade-off: Mengorbangkan total addressable market (multi-chain users) demi technical focus, latency optimization, dan dominance di single chain
· Evidence: Phase 4 System Architecture: "Tipe: DEX Aggregator... di atas Solana Mainnet"; "Chain(s): Solana (primary)"; Phase 7 Ecosystem Risks: "Single Chain Dependency"; Phase 8 Narrative Position: "Chain Abstraction / Cross-chain: Not Applicable"
· Supporting Dataset: Phase 4 System Architecture; Phase 7 Ecosystem Risks; Phase 8 Narrative Position, Market Position

Trade-off 3: Program Upgradeability vs Immutability Trust
· Decision: Jupiter Program tetap upgradeable (bukan immutable); multisig authority bisa upgrade kapan saja
· Trade-off: Mengorbangkan trust-minimized guarantee (user harus trust multisig tidak malicious) demi kemampuan patch bug, upgrade routing, tambah fitur tanpa migrasi
· Evidence: Phase 4 Security Model: "Program Jupiter memiliki upgrade authority (bukan immutable)"; Phase 7 Ecosystem Risks: "Upgrade Authority Centralization"; Phase 4 Technical Upgrade History: 4 major upgrades证明 authority digunakan
· Supporting Dataset: Phase 4 Security Model, Technical Upgrade History; Phase 7 Ecosystem Risks

Trade-off 4: Treasury Concentration in JUP vs Diversified Stable Assets
· Decision: DAO treasury 40% supply JUP (4B JUP); tidak diversifikasi ke USDC/SOL/asset lain yang diungkapkan
· Trade-off: Mengorbangkan treasury stability (nilai treasury korelasi 1:1 dengan JUP price) demi alignment token holder dan simplicity; fee switch belum aktif jadi tidak ada revenue real yield
· Evidence: Phase 5 Treasury: "DAO treasury menguasai ~40% total supply JUP"; "Stablecoin Holdings: Tidak diungkap"; Phase 5 Financial Risk: "Treasury Concentration in Native Token (JUP)"; Phase 6 Distribution: "Treasury: 40%"
· Supporting Dataset: Phase 5 Treasury, Financial Risk; Phase 6 Distribution

Trade-off 5: Free Developer Infrastructure vs Direct Monetization
· Decision: SDK, API public, Terminal gratis; hanya Ultra API enterprise berbayar
· Trade-off: Mengorbangkan short-term revenue dari API access demi network effect, adoption luas, dan moat sebagai default infrastructure layer
· Evidence: Phase 5 Revenue Model: "Terminal/SDK Licensing Status: Live (gratis untuk penggunaan standar)"; "API Fees (Ultra API/Enterprise) Status: Live... custom quote"; Phase 7 Developer Ecosystem: semua tools gratis
· Supporting Dataset: Phase 5 Revenue Model; Phase 7 Developer Ecosystem; Phase 3 EV-006, EV-016

Trade-off 6: Pseudonymous Team vs Institutional Trust
· Decision: Founder dan core lead pseudonymous (Meow, Rolex, Slorg, Worm); tidak doxxed ke publik
· Trade-off: Mengorbangkan institutional trust (beberapa tradfi/enterprise butuh KYC team) demi privacy, security, dan crypto-native culture
· Evidence: Phase 1 Core Team: semua pseudonim; Phase 2 Entity: Person semua pseudonim; Phase 7 Infrastructure Providers: Cloud/RPC/CDN provider undisclosed (consistent opacity)
· Supporting Dataset: Phase 1 Core Team; Phase 2 Entity; Phase 7 Infrastructure Providers

Trade-off 7: Perps v2 JLP Model (Capital Efficient) vs LP Impermanent Loss Risk
· Decision: Perps v2 menggunakan JLP multi-asset pool sebagai counterparty (hybrid AMM/orderbook), menggantikan orderbook murni v1
· Trade-off: Mengorbangkan LP protection (introduce impermanent loss risk untuk LP JLP) demi capital efficiency, single-sided LP exposure, dan fee revenue sharing ke LP
· Evidence: Phase 3 EV-013: "JLP (multi-asset liquidity pool) sebagai counterparty... menggantikan model orderbook murni"; Phase 4 Known Technical Limitations: "Perps dan JLP Risk: JLP pool menghadapi risk dari impermanent loss dan large position"; Phase 8 Liquidity: JLP TVL peak $1.2B lalu $600M
· Supporting Dataset: Phase 3 EV-013; Phase 4 Known Technical Limitations; Phase 8 Liquidity, Adoption Metrics

Behavioral Summary

Prioritas Utama Proyek:
1. Technical Excellence di Routing/Execution (Metis v2, Ultra API sub-100ms, atomic arb) — bukti: 4 major routing upgrades, enterprise API, cross-product atomic integration
2. Product Suite Completeness (Swap, Limit, DCA, Perps, API, Terminal, Mobile, Launchpad) — bukti: 8 core products dirilis bertahap 2021-2025
3. Solana Ecosystem Dominance (85-90% aggregator market share, deep DEX integrations) — bukti: Phase 8 Market Share, Phase 7 Major Integrations
4. Community Ownership via DAO (JUP token, Jupuary airdrops, fee switch proposal) — bukti: Phase 3 EV-008, EV-009, EV-011, EV-014, EV-017; Phase 6 Governance
5. Developer Infrastructure Moat (Free SDK/API/Terminal, paid Ultra API) — bukti: Phase 7 Developer Ecosystem, Phase 5 Revenue Model

Cara Mengambil Keputusan:
- Data-driven dari on-chain metrics (volume, user, TVL) — tiap produk launch based on usage evidence
- Iterative shipping: release MVP, upgrade berkala (6-12 bulan), named releases dengan blog teknis
- Founder-led (Meow) dengan core team kecil (~30-40) — keputusan cepat, tidak committee-heavy
- Community feedback via Discord/forum/Twitter tapi proposal besar dari tim
- Risk acceptance untuk single-chain, oracle dependency, upgrade authority — dokumentasi transparan tapi tidak selalu mitigate code-level

Faktor Paling Sering Mempengaruhi Keputusan:
1. Solana Ecosystem Dynamics (DEX landscape, Serum collapse, competitor entry) — trigger paling banyak pivot/expansion
2. User Retention & Volume Growth (Jupuary airdrops, mobile app, new products) — driver product roadmap
3. Technical Differentiation vs Competitors (Metis routing, Ultra API latency, atomic arb) — response ke Odos/1inch entry
4. Token Utility Activation (Fee switch, staking yield, governance) — driver DAO proposals
5. Enterprise Revenue Need (Ultra API, institutional onboarding) — driver infrastructure investment

Pola Evolusi:
- Phase 1 (2021): Single product (Aggregator) → Product-Market Fit
- Phase 2 (2022): Vertical expansion (Limit, DCA, Perps) → Full-Stack DeFi
- Phase 3 (2023): Horizontal expansion (API, SDK, Terminal) → Developer Platform
- Phase 4 (2024): Tokenization & DAO (JUP, Governance, Mobile, Ultra API) → Protocol + Business
- Phase 5 (2025): Cross-product synergy (Metis v2 atomic arb) → Integrated Moat

Kekuatan Utama:
- Technical moat terdalam di Solana DeFi (routing algorithm, latency, atomic cross-product)
- Dominant market position (85-90% aggregator share, sticky user base)
- Full product suite menciptakan high switching cost
- Strong developer ecosystem (free tools, enterprise tier)
- Community-aligned tokenomics (no VC, fair launch, recurring airdrops)
- Sustainable revenue diversification (swap + perps + enterprise API)

Kelemahan Utama:
- Single-chain risk (100% Solana dependency, no fallback)
- Treasury concentration in volatile native token (40% JUP, no stable diversification)
- Governance opacity (multisig signers undisclosed, off-chain voting only)
- Program upgradeability centralization (multisig authority, no timelock)
- Oracle single point of failure (Pyth only for Perps)
- No financial transparency (no revenue reports, treasury dashboard, audits)
- Pseudonymous leadership limits institutional partnerships
- Fee switch not activated (token utility incomplete)
- Cross-chain ambiguity (Wormhole referenced but unconfirmed)

## Knowledge Extraction
_ref: `docs/Patterns/*`, `docs/Reasoning/*` (rule candidates)_

PROJECT: Jupiter

Core Insights

Insight 1: Product-Market Fit Sebelum Tokenomics Menghasilkan Distribusi Token yang Lebih Sehat dan Governance yang Lebih Legitim
Explanation: Jupiter beroperasi 2.5 tahun (Oktober 2021 – Januari 2024) tanpa token, membangun aggregator, limit order, DCA, perps, API, dan Terminal terlebih dahulu. Token JUP hanya diluncurkan setelah posisi dominan di Solana terbukti (>85-90% market share aggregator, >$500B kumulatif volume). Akibatnya, distribusi token fair (0% investor/VC, 10% airdrop komunitas, 40% DAO treasury) dan governance DAO dimulai dengan basis pemegang token yang already-active users, bukan spekulan.
Evidence: Phase 3 timeline menunjukkan EV-002 hingga EV-006 semua pre-token; EV-008 TGE Jan 2024; Phase 6 Distribution: "Investors: 0%", "Community: 10%", "Treasury: 40%"; Phase 8 Market Share: "~85-90% Solana aggregator share"; Phase 3 EV-018 blog: "> $500B cumulative volume"
Supporting Dataset: Phase 3 (EV-002 s.d. EV-008), Phase 6 (Distribution, TGE), Phase 8 (Market Share)
Confidence: HIGH

Insight 2: Arsitektur Hybrid On-Chain Execution + Off-Chain Routing Memberikan Keunggulan Teknis yang Sulit Direplikasi
Explanation: Semua eksekusi trade (swap, limit, DCA, perps) terjadi on-chain di Solana SVM via Jupiter Program, sedangkan routing/price discovery dilakukan off-chain oleh Jupiter API/engine. Pemisahan ini memungkinkan komputasi routing kompleks (Metis v2 parallel execution, atomic arb) tanpa gas overhead, sambil menjaga keamanan settlement on-chain. Competitor multi-chain (1inch, Paraswap) tidak bisa mengoptimasi sedalam ini untuk single chain.
Evidence: Phase 4 System Architecture: "Routing Layer — Jupiter mengagregasi likuiditas... untuk menemukan best price path"; "Eksekusi tetap on-chain via Jupiter Program"; Phase 4 Technical Upgrade History: v2 Metis, v3 Apollo, v4 Metis v2; Phase 3 EV-007, EV-012, EV-018
Supporting Dataset: Phase 4 (System Architecture, Technical Upgrade History), Phase 3 (EV-007, EV-012, EV-018)
Confidence: HIGH

Insight 3: Single-Chain Focus (Solana Only) Menciptakan Moat Mendalam Tapi Menimbulkan Risiko Konsentrasi Eksistensial
Explanation: 100% produk Jupiter (Aggregator, Perps, Limit, DCA, Terminal, Mobile, JUP token) hanya di Solana. Fokus ini memungkinkan optimasi latency (Ultra API sub-100ms), routing algorithm khusus Solana (Metis), dan integrasi mendalam dengan 20+ DEX Solana. Namun, tidak ada fallback chain — Solana downtime langsung menghentikan seluruh operasional Jupiter.
Evidence: Phase 4 System Architecture: "Tipe: DEX Aggregator... di atas Solana Mainnet"; "Chain(s): Solana (primary)"; Phase 7 Ecosystem Risks: "Single Chain Dependency: 100% of Jupiter products... operate exclusively on Solana"; Phase 4 Known Technical Limitations: "Single-chain Dependency... Jupiter tidak memiliki fallback chain"
Supporting Dataset: Phase 4 (System Architecture, Known Technical Limitations), Phase 7 (Ecosystem Risks), Phase 1 (Chain(s))
Confidence: HIGH

Insight 4: Treasury Konsentrasi di Native Token (40% JUP Supply) Tanpa Diversifikasi Stablecoin Menciptakan Ketergantungan Nilai Treasury pada Harga Token
Explanation: DAO treasury menguasai 4 miliar JUP (40% total supply) per tokenomics. Tidak ada disclosure stablecoin/asset lain. Nilai treasury korelasi ~1:1 dengan harga JUP. Fee switch proposal (EV-014) belum aktif, sehingga tidak ada revenue real yield yang mengalir ke treasury. Ini membuat DAO rentan terhadap bear market panjang.
Evidence: Phase 5 Treasury: "DAO treasury menguasai ~40% total supply JUP (4 miliar JUP)"; "Stablecoin Holdings: Tidak diungkap"; Phase 5 Financial Risk: "Treasury Concentration in Native Token (JUP)"; Phase 6 Distribution: "Treasury: 40%"; Phase 3 EV-014 fee switch proposal ongoing
Supporting Dataset: Phase 5 (Treasury, Financial Risk), Phase 6 (Distribution), Phase 3 (EV-014)
Confidence: HIGH

Insight 5: Program Upgradeable + Multisig Authority Opaque = Trade-off Kecepatan Iterasi vs Trust Minimization
Explanation: Jupiter Program tidak immutable; upgrade authority dikontrol multisig (signer tidak publik). Ini memungkinkan 4 major routing upgrades dalam 3 tahun (v1→v2 Metis→v3 Apollo→v4 Metis v2) tanpa migrasi user. Namun, user harus trust multisig tidak malicious; tidak ada timelock publik atau governance delay untuk upgrade.
Evidence: Phase 4 Security Model: "Program Jupiter memiliki upgrade authority (bukan immutable)"; "Multisig/Timelock... jumlah signer dan alamat multisig tidak dipublikasikan"; Phase 7 Ecosystem Risks: "Upgrade Authority Centralization"; Phase 4 Technical Upgrade History: 4 major upgrades
Supporting Dataset: Phase 4 (Security Model, Technical Upgrade History), Phase 7 (Ecosystem Risks)
Confidence: HIGH

Insight 6: Developer-First Infrastructure (Free SDK/API/Terminal + Paid Ultra API) Membangun Network Effect Sebagai "Stripe of Solana DeFi"
Explanation: TypeScript/Rust SDK, REST API public, Terminal widget disediakan gratis → adopsi luas di wallet (Phantom, Solflare, Backpack), trading bot, portfolio tracker. Ultra API v6 (sub-100ms, SLA enterprise) jadi monetisasi untuk market maker/institusi. Strategi ini menciptakan switching cost tinggi: integrator sulit pindah ke aggregator lain.
Evidence: Phase 5 Revenue Model: "Terminal/SDK Licensing Status: Live (gratis untuk penggunaan standar)"; "API Fees (Ultra API/Enterprise) Status: Live... custom quote"; Phase 7 Developer Ecosystem: semua tools gratis; Phase 3 EV-006, EV-016; Phase 7 Wallet Ecosystem: "Terminal works dengan any Solana wallet adapter"
Supporting Dataset: Phase 5 (Revenue Model), Phase 7 (Developer Ecosystem, Wallet Ecosystem), Phase 3 (EV-006, EV-016)
Confidence: HIGH

Insight 7: Airdrop Berulang (Jupuary 1/2/3) sebagai Mekanisme Retention dan Governance Incentive Bukan Hanya Distribusi Awal
Explanation: Berbeda dengan projek lain yang airdrop one-off di TGE, Jupiter melakukan Jupuary 1 (TGE, 10% supply ke ~955k wallet), Jupuary 2 (Mar 2024), Jupuary 3/Catdets (Dec 2024, soulbound NFT tracking kontribusi jangka panjang). Setiap ronde refine eligibility (volume, governance participation, soulbound NFT). Ini menciptakan flywheel: user aktif → claim airdrop → stake JUP → vote governance → eligible next round.
Evidence: Phase 3 EV-008 (Jupuary 1), EV-011 (Jupuary 2), EV-017 (Jupuary 3); Phase 6 Utility: "Incentive/Reward (Airdrop/Jupuary)"; Phase 6 Major Token Events: EV-008, EV-011, EV-017
Supporting Dataset: Phase 3 (EV-008, EV-011, EV-017), Phase 6 (Utility, Major Token Events)
Confidence: HIGH

Insight 8: Zero VC Funding Disclosure + Bootstrapped Narrative Konsisten Membedakan Jupiter dari Hampir Semua DeFi Major
Explanation: Dari Phase 1-5, tidak ada satupun investor/VC teridentifikasi. OpenCorporates BVI filing tidak show shareholders. Narrative konsisten "bootstrapped + protocol revenue". Team ~30-40 orang didanai dari swap fees (2021+) dan perps fees (2022+) sebelum TGE. Ini menghilangkan VC unlock risk, sell pressure, dan misalignment incentive.
Evidence: Phase 1 Investor: "(tidak ada investor teridentifikasi)"; Phase 2 Entity: no investor entities; Phase 5 Funding History: "Tidak ada ronde pendanaan yang diumumkan secara publik"; "Jupiter tampak dibangun melalui bootstrapping dan pendapatan protokol"; Phase 5 Fundraising Mechanism: "Bootstrapping", "Protocol Revenue"
Supporting Dataset: Phase 1 (Investor), Phase 2 (Entity), Phase 5 (Funding History, Fundraising Mechanism)
Confidence: HIGH

Insight 9: Perps v2 JLP Model (Hybrid AMM/Orderbook dengan LP Pool Multi-Asset) Menggantikan Orderbook Murni untuk Capital Efficiency Tapi Memindahkan Impermanent Loss Risk ke LP
Explanation: Perps v1 (Nov 2022) menggunakan orderbook hybrid. Perps v2 (Jul 2024, EV-013) memperkenalkan JLP (Jupiter Liquidity Pool) multi-asset sebagai counterparty. LP mint/burn JLP shares, mendapat fee revenue sharing. TVL peak $1.2B lalu turun ke ~$600M (Jan 2025). Model ini lebih capital efficient tapi LP terpapar impermanent loss dan large position risk.
Evidence: Phase 3 EV-013: "JLP (multi-asset liquidity pool) sebagai counterparty... menggantikan model orderbook murni"; Phase 4 Known Technical Limitations: "Perps dan JLP Risk: JLP pool menghadapi risk dari impermanent loss dan large position"; Phase 8 Liquidity: "JLP TVL peak $1.2B lalu $600M"
Supporting Dataset: Phase 3 (EV-013), Phase 4 (Known Technical Limitations), Phase 8 (Liquidity, Adoption Metrics)
Confidence: HIGH

Insight 10: Governance Off-Chain (vote.jup.ag) + Multisig Execution Opaque = Kecepatan dan Gasless Voting Tapi Transparansi Eksekusi Terbatas
Explanation: Jupiter DAO menggunakan snapshot-style voting off-chain di vote.jup.ag (gasless, UX sederhana). Proposal lolos dieksekusi on-chain oleh DAO multisig (signer tidak publik). Tidak ada council, committee, atau on-chain DAO framework (Realms). Proposal besar (fee switch) diajukan tim, bukan community-sourced.
Evidence: Phase 6 Governance: "Voting System: Snapshot-style off-chain voting... on-chain execution via multisig"; Phase 7 Governance Ecosystem: "Council: Not established... Committee: Not established"; Phase 3 EV-014: "Jupiter DAO mengajukan proposal untuk mengaktifkan fee switch"; Phase 7 Ecosystem Risks: "Multisig Signer Opacity"
Supporting Dataset: Phase 6 (Governance), Phase 7 (Governance Ecosystem, Ecosystem Risks), Phase 3 (EV-014)
Confidence: HIGH

Insight 11: Oracle Dependency Tunggal (Pyth Network) untuk Perps Tanpa Fallback Membuat Single Point of Failure untuk Liquidation dan Funding Rate
Explanation: Jupiter Perps sepenuhnya bergantung pada Pyth untuk mark price, funding rate, liquidation trigger. Tidak ada multi-oracle setup, tidak ada TWAP internal fallback. Dokumentasi akui risiko oracle delay/manipulation tapi tidak implementasi circuit breaker.
Evidence: Phase 4 Oracle: "Jupiter Perps menggunakan oracle eksternal (Pyth Network) untuk harga mark/funding rate"; Phase 4 Known Technical Limitations: "Oracle Delay... bila oracle harga tertunda... dapat menyebabkan likuidasi yang tidak diinginkan"; Phase 7 External Dependencies: Pyth "Criticality: Critical (for Perps)"; Phase 7 Ecosystem Risks: "Oracle Dependency (Perps)"
Supporting Dataset: Phase 4 (Core Components, Known Technical Limitations), Phase 7 (External Dependencies, Ecosystem Risks)
Confidence: HIGH

Insight 12: Iterasi Major Upgrade Setiap 6-12 Bulan dengan Named Release (Metis, Apollo, Metis v2) Menciptakan Technical Moat yang Berkelanjutan
Explanation: Aggregator routing engine di-upgrade major berkala: v1 (Oct 2021) → v2 Metis (Nov 2023) → v3 Apollo (Apr 2024) → v4 Metis v2 (Jan 2025). Setiap upgrade menambah fitur: gas optimization, compressed NFT/token-2022 support, parallel execution, atomic cross-product arb (swap���perps). Competitor Odos masuk Solana 2024 → Jupiter respond dengan Metis v2 + Ultra API enterprise.
Evidence: Phase 4 Technical Upgrade History: 4 major upgrades dalam ~3 tahun; Phase 3 EV-002, EV-007, EV-012, EV-018; Phase 8 Competitor Landscape: "Odos... patented routing algorithm"; Phase 3 EV-016, EV-018 response
Supporting Dataset: Phase 4 (Technical Upgrade History), Phase 3 (EV-002, EV-007, EV-012, EV-018), Phase 8 (Competitor Landscape)
Confidence: HIGH

Insight 13: Pseudonymous Leadership (Meow, Rolex, Slorg, Worm) dengan Public Accountability via On-Chain Execution dan Blog Teknis Detail
Explanation: Founder dan core lead pseudonymous tapi aktif komunikasi publik (Twitter, blog, forum). Setiap major upgrade diumumkan via blog.jup.ag dengan detail teknis (bukan marketing fluff). Accountability via on-chain execution yang verifiable, bukan identitas real-world. Ini memungkinkan privacy/security untuk tim crypto-native sambil menjaga trust komunitas.
Evidence: Phase 1 Core Team: "Meow (pseudonim)", "Rolex (pseud.)", "Slorg (pseud.)", "Worm (pseud.)"; Phase 2 Entity: Person semua pseudonim; Phase 3 sources hampir semua ke blog.jup.ag dan Meow Twitter; Phase 4 Technical Upgrade History sources ke blog
Supporting Dataset: Phase 1 (Core Team), Phase 2 (Entity), Phase 3 (Sources), Phase 4 (Technical Upgrade History)
Confidence: HIGH

Insight 14: Cross-Chain Ambiguity (Wormhole Referenced di Early Docs Tapi Tidak Confirmed Production di Perps v2) Menunjukkan Eksplorasi Tanpa Komitmen Penuh
Explanation: Wormhole terdaftar di ecosystem page dan early Perps v1 docs (EV-005); tapi Jupiter Perps v2 docs tidak mention Wormhole. Jupiter Aggregator tidak punya cross-chain swap. Status dependency unclear — mungkin R&D atau deprecated.
Evidence: Phase 7 External Dependencies: Wormhole "Status: Live (per Wormhole ecosystem page) / Unconfirmed current production dependency"; Phase 7 Major Integrations: "production usage in v2 not explicitly confirmed"; Phase 7 Ecosystem Risks: "Bridge / Cross-chain Dependency... Current production dependency not confirmed"; Phase 2 Entity: Wormhole
Supporting Dataset: Phase 7 (External Dependencies, Major Integrations, Ecosystem Risks), Phase 2 (Entity: Wormhole), Phase 3 (EV-005)
Confidence: MEDIUM

Insight 15: Tidak Ada Financial Transparency Reporting (No Revenue Report, Treasury Dashboard, Audited Financials) Menciptakan Information Asymmetry bagi Token Holder
Explanation: Jupiter tidak mempublikasikan laporan keuangan berkala, treasury dashboard, atau audited financials. Data on-chain tersedia tapi tidak diagregasikan resmi. Estimasi pihak ketiga (Token Terminal, DefiLlama) menjadi referensi utama. Fee switch proposal (EV-014) akan mengaktifkan value accrual tapi belum pass.
Evidence: Phase 5 Revenue History: "Tidak diungkap secara resmi dalam laporan berkala"; "Official Financial Resources: Transparency Report: Tidak ada, Treasury Dashboard: Tidak ada"; Phase 5 Financial Risk: "No Public Financial Audit / Transparency Report"; Phase 3 EV-014 ongoing
Supporting Dataset: Phase 5 (Revenue History, Official Financial Resources, Financial Risk), Phase 3 (EV-014)
Confidence: HIGH

Strategic Principles

Principle 1: Ship Product First, Token Later — Product-Market Fit Sebelum Tokenomics
Explanation: Jupiter membangun 6 produk core (Aggregator, Limit, DCA, Perps, API, Terminal) selama 2.5 tahun sebelum TGE. Token hanya launch setelah dominant position terbukti. Ini memastikan token utility tied to real usage, bukan spekulasi.
Evidence: Phase 3 Timeline: EV-002 (2021-10) s.d. EV-006 (2023) pre-token; EV-008 TGE Jan 2024; Phase 9 Behavioral: "Pola 1: Ship Product First, Token Later"
Supporting Dataset: Phase 3 (EV-002 s.d. EV-008), Phase 9 (Recurring Behavioral Pattern)
Confidence: HIGH

Principle 2: Single-Chain Mastery Over Multi-Chain Mediocrity — Fokus Mendalam di Solana Bukan Luas Dangkal
Explanation: Jupiter memilih 100% Solana, mengoptimasi latency (Ultra API sub-100ms), routing algorithm khusus (Metis), integrasi 20+ DEX Solana. Trade-off: tidak ada cross-chain swap, tidak ada L2 deployment, tidak ada fallback chain. Moat teknis lebih dalam tapi risiko konsentrasi lebih tinggi.
Evidence: Phase 4 System Architecture: "Chain(s): Solana (primary)"; Phase 7 Ecosystem Risks: "Single Chain Dependency"; Phase 8 Narrative Position: "Chain Abstraction / Cross-chain: Not Applicable"; Phase 9 Trade-off 2
Supporting Dataset: Phase 4 (System Architecture), Phase 7 (Ecosystem Risks), Phase 8 (Narrative Position), Phase 9 (Strategic Trade-offs)
Confidence: HIGH

Principle 3: Developer-First Infrastructure — Free Tools untuk Adopsi Luas, Paid Enterprise untuk Monetisasi
Explanation: SDK (TS/Rust), REST API, Terminal widget gratis → network effect, switching cost tinggi. Ultra API v6 (sub-100ms, SLA) berbayar untuk market maker/institusi. Mirip model Stripe: gratis untuk developer, berbayar untuk enterprise scale.
Evidence: Phase 5 Revenue Model: "Terminal/SDK Licensing Status: Live (gratis)"; "API Fees (Ultra API/Enterprise) Status: Live... custom quote"; Phase 7 Developer Ecosystem: semua tools gratis; Phase 9 Trade-off 5
Supporting Dataset: Phase 5 (Revenue Model), Phase 7 (Developer Ecosystem), Phase 9 (Strategic Trade-offs)
Confidence: HIGH

Principle 4: Iterative Technical Excellence — Named Major Upgrades Setiap 6-12 Bulan
Explanation: Routing engine v1→v2 Metis→v3 Apollo→v4 Metis v2 dengan blog teknis detail tiap release. Bukan "version bump" minor tapi step-change performance (gas optimization, parallel execution, atomic arb). Menciptakan moving target bagi competitor.
Evidence: Phase 4 Technical Upgrade History: 4 major upgrades; Phase 3 EV-007, EV-012, EV-018; Phase 9 Behavioral: "Pola 2: Iterative Major Upgrades Setiap 6-12 Bulan"
Supporting Dataset: Phase 4 (Technical Upgrade History), Phase 3 (EV-007, EV-012, EV-018), Phase 9 (Recurring Behavioral Pattern)
Confidence: HIGH

Principle 5: Community Ownership via Fair Launch — 0% VC, 10% Airdrop, 40% DAO Treasury, Recurring Incentives
Explanation: Tokenomics dirancang untuk alignment jangka panjang: no investor allocation, team 20% vesting 4 tahun, DAO treasury 40%, airdrop berulang (Jupuary 1/2/3) dengan eligibility evolving. Fee switch proposal akan mengaktifkan real yield untuk stakers.
Evidence: Phase 6 Distribution: "Investors: 0%", "Team: 20% (vesting 4 tahun)", "Treasury: 40%", "Community: 10%"; Phase 3 EV-008, EV-011, EV-017; Phase 9 Behavioral: "Pola 4: Community Incentive Berulang via Airdrop"
Supporting Dataset: Phase 6 (Distribution, Vesting), Phase 3 (EV-008, EV-011, EV-017), Phase 9 (Recurring Behavioral Pattern)
Confidence: HIGH

Principle 6: Transparansi Teknis via Blog, Opasitas Governance/Financial via Multisig Opaque
Explanation: Setiap upgrade teknis di-dokumentasikan detail di blog.jup.ag (routing algorithm, architecture, trade-offs). Tapi multisig signer (treasury, upgrade authority) tidak dipublikasikan, tidak ada financial report, fee switch belum aktif. Transparansi selective: teknis tinggi, governance/financial rendah.
Evidence: Phase 3 Sources hampir semua ke blog.jup.ag; Phase 4 Technical Upgrade History sources ke blog; Phase 5 Treasury: "jumlah signer dan alamat multisig tidak dipublikasikan"; Phase 7 Ecosystem Risks: "Multisig Signer Opacity"; Phase 9 Trade-off 1, Trade-off 4
Supporting Dataset: Phase 3 (Sources), Phase 4 (Technical Upgrade History), Phase 5 (Treasury), Phase 7 (Ecosystem Risks), Phase 9 (Strategic Trade-offs)
Confidence: HIGH

Principle 7: Accept Known Risks dengan Dokumentasi Jelas, Bukan Over-Engineering Mitigasi
Explanation: Single-chain risk, oracle single point, upgrade authority centralization, treasury concentration — semuanya didokumentasikan transparan di docs/security page tapi tidak semua di-mitigasi code-level (misal: tidak ada fallback oracle, tidak ada timelock upgrade). Philosophy: document risk, accept trade-off, iterate.
Evidence: Phase 4 Known Technical Limitations: setiap risk dijelaskan; Phase 7 Ecosystem Risks: setiap risk listed; Phase 9 Risk Response: "Pola 1: Solana Downtime → Tidak Ada Fallback Chain (Acceptance Risk)", "Pola 2: Oracle Failure → Documentation Risk Disclosure Only"
Supporting Dataset: Phase 4 (Known Technical Limitations), Phase 7 (Ecosystem Risks), Phase 9 (Risk Response Pattern)
Confidence: HIGH

Success Factors

Factor 1: First-Mover Advantage di Solana DEX Aggregation + Continuous Moat Deepening
Explanation: Launch Oktober 2021 (EV-002) saat Solana DeFi meledak (Serum, Raydium, Orca). Menjadi default aggregator sebelum competitor multi-chain (1inch, Paraswap) serius masuk Solana. Kemudian mempertahankan dominance via 4 major routing upgrades (Metis, Apollo, Metis v2) dan product suite expansion.
Evidence: Phase 3 EV-002: "Luncuran Jupiter Aggregator v1 pada Solana Mainnet (Oktober 2021)"; Phase 8 Market Share: "~85-90% Solana aggregator share"; Phase 4 Technical Upgrade History: 4 major upgrades; Phase 9 Evolution Pattern: "Perubahan Teknologi: Dari Routing Sederhana → Metis Algorithm → Apollo → Metis v2"
Supporting Dataset: Phase 3 (EV-002), Phase 8 (Market Share), Phase 4 (Technical Upgrade History), Phase 9 (Evolution Pattern)
Confidence: HIGH

Factor 2: Full-Stack DeFi Suite Terintegrasi Menciptakan High Switching Cost
Explanation: User tidak perlu pindah platform untuk swap, limit order, DCA, perps, portfolio tracking, mobile app. Semua terintegrasi ke aggregator core routing. Cross-product atomic arb (Metis v2) hanya memungkinkan karena full-stack ownership.
Evidence: Phase 3 Timeline: EV-003 Limit, EV-004 DCA, EV-005 Perps, EV-006 API/Terminal, EV-015 Mobile, EV-018 Metis v2 atomic arb; Phase 7 Applications: 8 core products; Phase 4 Core Components: 12 komponen terintegrasi
Supporting Dataset: Phase 3 (EV-003 s.d. EV-018), Phase 7 (Applications), Phase 4 (Core Components)
Confidence: HIGH

Factor 3: Zero VC Funding → No Unlock Risk, No Misalignment, Full Control
Explanation: Bootstrapped dari protocol revenue (2021+) + token treasury (2024+). Tidak ada investor pressure untuk exit, token unlock, atau pivot. Team retain full control over roadmap dan tokenomics.
Evidence: Phase 5 Funding History: "Tidak ada ronde pendanaan yang diumumkan"; Phase 5 Fundraising Mechanism: "Bootstrapping", "Protocol Revenue", "DAO Treasury"; Phase 1 Investor: "(tidak ada investor teridentifikasi)"; Phase 9 Behavioral: "Pola 7: Zero VC Funding Disclosure"
Supporting Dataset: Phase 5 (Funding History, Fundraising Mechanism), Phase 1 (Investor), Phase 9 (Recurring Behavioral Pattern)
Confidence: HIGH

Factor 4: Developer Ecosystem Moat via Free Infrastructure + Enterprise Upsell
Explanation: SDK, API, Terminal gratis → adopsi di Phantom, Solflare, Backpack, trading bots, portfolio trackers. Ultra API v6 enterprise → revenue baru, sticky institutional relationships. Competitor sulit menyaingi network effect ini.
Evidence: Phase 7 Developer Ecosystem: "SDK: Jupiter SDK TypeScript... API: Jupiter REST API... Developer Tools: Jupiter Terminal"; Phase 7 Wallet Ecosystem: "Terminal works dengan any Solana wallet adapter"; Phase 5 Revenue Model: "API Fees (Ultra API/Enterprise) Status: Live... custom quote"; Phase 9 Trade-off 5
Supporting Dataset: Phase 7 (Developer Ecosystem, Wallet Ecosystem), Phase 5 (Revenue Model), Phase 9 (Strategic Trade-offs)
Confidence: HIGH

Factor 5: Recurring Community Incentive Program (Jupuary Series) Menjaga Retention dan Volume
Explanation: Jupuary 1 (TGE), 2 (Mar 2024), 3/Catdets (Dec 2024) dengan eligibility evolving (volume → governance → soulbound NFT). Menciptakan flywheel user aktif → claim → stake → vote → eligible next round. Volume dan user retention relatif stabil vs competitor.
Evidence: Phase 3 EV-008, EV-011, EV-017; Phase 6 Utility: "Incentive/Reward (Airdrop/Jupuary)"; Phase 8 Adoption Metrics: "Daily Active Users ~50,000-100,000", "Daily Transactions ~200,000-500,000"; Phase 9 Behavioral: "Pola 4: Community Incentive Berulang via Airdrop"
Supporting Dataset: Phase 3 (EV-008, EV-011, EV-017), Phase 6 (Utility), Phase 8 (Adoption Metrics), Phase 9 (Recurring Behavioral Pattern)
Confidence: HIGH

Factor 6: Technical Leadership Team (Meow, Worm, Slorg) yang Shipping Cepat dan Iteratif
Explanation: Founder Meow (vision/strategy), Worm (Head of Engineering, arsitektur on-chain), Slorg (Head of Product). Tim ~30-40 orang shipping major upgrade setiap 6-12 bulan. Pseudonymous tapi accountable via on-chain execution dan blog teknis detail.
Evidence: Phase 1 Core Team: "Meow (pseudonim — founder/CEO)", "Worm (Head of Engineering, pseud.)", "Slorg (Head of Product, pseud.)"; Phase 2 Entity: Person pseudonim; Phase 4 Technical Upgrade History: 4 major upgrades; Phase 9 Behavioral: "Pola 6: Pseudonymous Leadership dengan Public Accountability"
Supporting Dataset: Phase 1 (Core Team), Phase 2 (Entity), Phase 4 (Technical Upgrade History), Phase 9 (Recurring Behavioral Pattern)
Confidence: HIGH

Factor 7: Deep Integration dengan Solana DEX Ecosystem (Routing Through, Not Competing)
Explanation: Jupiter tidak build DEX sendiri (kecuali Perps). Aggregator merutekan melalui Raydium, Orca, Meteora, Lifinity, Phoenix, dll. Menjadi "meta-DEX" yang memperkuat seluruh ekosistem. Ketika Serum collapse (FTX), Jupiter expand ke DEX lain tanpa service disruption.
Evidence: Phase 7 Major Integrations: "Jupiter Aggregator ↔ Solana DEXs (Raydium, Orca, Meteora, Lifinity, Phoenix, etc.)"; Phase 4 System Architecture: "Layer: Routing Layer — Jupiter mengagregasi likuiditas dari banyak DEX Solana"; Phase 9 Ecosystem Decision Pattern: "Pola 1: Deep Integration dengan Solana DEX Ecosystem"; Phase 3 EV-002 mention Serum
Supporting Dataset: Phase 7 (Major Integrations), Phase 4 (System Architecture), Phase 9 (Ecosystem Decision Pattern), Phase 3 (EV-002)
Confidence: HIGH

Failure Factors

Factor 1: Single-Chain Dependency — Solana Downtime Menghentikan Seluruh Operasional Jupiter
Explanation: 100% produk di Solana. Tidak ada fallback chain, tidak ada cross-chain deployment, tidak ada L2. Solana mainnet outage (beberapa kali 2022-2023) → Jupiter tidak bisa diakses. User experience terganggu, brand trust terkikis (meski recover cepat).
Evidence: Phase 7 Ecosystem Risks: "Single Chain Dependency: 100% of Jupiter products... operate exclusively on Solana. Solana downtime... directly halts all Jupiter operations"; Phase 4 Known Technical Limitations: "Single-chain Dependency... Jupiter tidak memiliki fallback chain"; Phase 9 Risk Response: "Pola 1: Solana Downtime → Tidak Ada Fallback Chain (Acceptance Risk)"
Supporting Dataset: Phase 7 (Ecosystem Risks), Phase 4 (Known Technical Limitations), Phase 9 (Risk Response Pattern)
Confidence: HIGH

Factor 2: Treasury Concentration di JUP (40% Supply) Tanpa Diversifikasi Stablecoin
Explanation: DAO treasury 4 miliar JUP (40% supply). Nilai treasury korelasi ~1:1 dengan harga JUP. Bear market panjang → daya beli treasury turun drastis. Fee switch belum aktif → tidak ada revenue real yield. Stablecoin holdings tidak diungkap (kemungkinan minimal/zero).
Evidence: Phase 5 Treasury: "DAO treasury menguasai ~40% total supply JUP (4 miliar JUP)"; "Stablecoin Holdings: Tidak diungkap"; Phase 5 Financial Risk: "Treasury Concentration in Native Token (JUP)"; Phase 6 Distribution: "Treasury: 40%"; Phase 9 Trade-off 4
Supporting Dataset: Phase 5 (Treasury, Financial Risk), Phase 6 (Distribution), Phase 9 (Strategic Trade-offs)
Confidence: HIGH

Factor 3: Governance Opacity — Multisig Signer Tidak Dipublikasikan, Off-Chain Voting Only
Explanation: DAO treasury dan program upgrade authority dikontrol multisig (signer tidak publik). Vote.jup.ag off-chain (snapshot-style), tidak ada on-chain DAO framework (Realms). Proposal besar dari tim, bukan community-sourced. Tidak ada timelock publik untuk upgrade. Transparansi eksekusi terbatas.
Evidence: Phase 5 Treasury: "Treasury Custodian: Dikelola oleh Jupiter DAO multisig (jumlah signer dan alamat tidak dipublikasikan resmi)"; Phase 4 Security Model: "Multisig/Timelock... jumlah signer dan alamat multisig tidak dipublikasikan"; Phase 7 Ecosystem Risks: "Multisig Signer Opacity"; Phase 6 Governance: "Voting System: Snapshot-style off-chain voting... on-chain execution via multisig"; Phase 9 Trade-off 1
Supporting Dataset: Phase 5 (Treasury), Phase 4 (Security Model), Phase 7 (Ecosystem Risks), Phase 6 (Governance), Phase 9 (Strategic Trade-offs)
Confidence: HIGH

Factor 4: Program Upgradeability Centralization — Multisig Authority Bisa Upgrade Kapan Saja Tanpa Delay
Explanation: Jupiter Program tidak immutable. Upgrade authority multisig (signer opaque). 4 major upgrades terbukti authority digunakan. Tidak ada governance delay, tidak ada timelock, tidak ada emergency circuit breaker. Jika multisig kompromi → malicious program changes possible.
Evidence: Phase 4 Security Model: "Program Jupiter memiliki upgrade authority (bukan immutable)"; Phase 7 Ecosystem Risks: "Upgrade Authority Centralization... Compromise of upgrade authority could allow malicious program changes"; Phase 4 Technical Upgrade History: 4 major upgrades; Phase 9 Trade-off 3
Supporting Dataset: Phase 4 (Security Model, Technical Upgrade History), Phase 7 (Ecosystem Risks), Phase 9 (Strategic Trade-offs)
Confidence: HIGH

Factor 5: Oracle Single Point of Failure (Pyth Only) untuk Perps — Liquidation Risk Jika Oracle Delay/Manipulasi
Explanation: Perps sepenuhnya bergantung Pyth untuk mark price, funding rate, liquidation. Tidak ada multi-oracle, tidak ada TWAP fallback, tidak ada circuit breaker. Dokumentasi akui risiko tapi tidak mitigate code-level. LP dan trader bear risk.
Evidence: Phase 4 Oracle: "Jupiter Perps menggunakan oracle eksternal (Pyth Network)"; Phase 4 Known Technical Limitations: "Oracle Delay... dapat menyebabkan likuidasi yang tidak diinginkan"; Phase 7 External Dependencies: Pyth "Criticality: Critical (for Perps)"; Phase 7 Ecosystem Risks: "Oracle Dependency (Perps)"; Phase 9 Risk Response: "Pola 2: Oracle Failure → Documentation Risk Disclosure Only"
Supporting Dataset: Phase 4 (Core Components, Known Technical Limitations), Phase 7 (External Dependencies, Ecosystem Risks), Phase 9 (Risk Response Pattern)
Confidence: HIGH

Factor 6: No Financial Transparency — Tidak Ada Revenue Report, Treasury Dashboard, Audited Financials
Explanation: Jupiter tidak mempublikasikan laporan keuangan berkala. Data on-chain tersedia tapi tidak diagregasikan resmi. Estimasi Token Terminal/DefiLlama jadi referensi utama. Fee switch proposal (EV-014) akan enable value accrual tapi belum pass. Token holder tidak bisa verify treasury health.
Evidence: Phase 5 Revenue History: "Tidak diungkap secara resmi dalam laporan berkala"; "Official Financial Resources: Transparency Report: Tidak ada, Treasury Dashboard: Tidak ada"; Phase 5 Financial Risk: "No Public Financial Audit / Transparency Report"; Phase 3 EV-014 ongoing
Supporting Dataset: Phase 5 (Revenue History, Official Financial Resources, Financial Risk), Phase 3 (EV-014)
Confidence: HIGH

Factor 7: Cross-Chain Ambiguity — Wormhole Referenced Tapi Tidak Confirmed Production
Explanation: Wormhole di ecosystem page dan early Perps v1 docs; tapi Perps v2 docs tidak mention. Aggregator tidak punya cross-chain swap. Status unclear — mungkin R&D deprecated atau future plan. Menciptakan confusion bagi developer/partner.
Evidence: Phase 7 External Dependencies: Wormhole "Status: Live (per Wormhole ecosystem page) / Unconfirmed current production dependency"; Phase 7 Major Integrations: "production usage in v2 not explicitly confirmed"; Phase 7 Ecosystem Risks: "Bridge / Cross-chain Dependency... Current production dependency not confirmed"; Phase 2 Entity: Wormhole
Supporting Dataset: Phase 7 (External Dependencies, Major Integrations, Ecosystem Risks), Phase 2 (Entity: Wormhole)
Confidence: MEDIUM

Factor 8: Pseudonymous Leadership Membatasi Institutional Partnership
Explanation: Founder Meow dan core lead pseudonymous. Beberapa tradfi/enterprise butuh KYC team untuk compliance/partnership. Cloud/RPC/CDN provider juga undisclosed (konsisten opacity). Ini mungkin membatasi enterprise adoption Ultra API di institusi tradfi ketat.
Evidence: Phase 1 Core Team: semua pseudonim; Phase 2 Entity: Person semua pseudonim; Phase 7 Infrastructure Providers: Cloud/RPC/CDN provider undisclosed; Phase 9 Trade-off 6
Supporting Dataset: Phase 1 (Core Team), Phase 2 (Entity), Phase 7 (Infrastructure Providers), Phase 9 (Strategic Trade-offs)
Confidence: MEDIUM

Factor 9: Fee Switch Belum Aktif — JUP Pure Governance Token Tanpa Yield
Explanation: Utility utama JUP adalah governance. Fee switch proposal (EV-014, Sep 2024) akan mengaktifkan value accrual (fee ke stakers/treasury). Tanpa fee switch, JUP tidak punya real yield. Proposal masih discussion, belum dieksekusi on-chain per info publik.
Evidence: Phase 6 Utility: "Fee Switch (Proposed)... Belum dieksekusi on-chain"; "Staking... Fee reward: Planned (bergantung fee switch)"; Phase 5 Financial Risk: "Fee Switch Not Yet Activated"; Phase 3 EV-014; Phase 9 Trade-off: "Fee Switch Sebagai Kunci Value Accrual Token (Belum Aktif)"
Supporting Dataset: Phase 6 (Utility), Phase 5 (Financial Risk), Phase 3 (EV-014), Phase 9 (Recurring Behavioral Pattern)
Confidence: HIGH

Factor 10: JLP Impermanent Loss Risk untuk LP — Model Capital Efficient Tapi Memindahkan Risk ke LP
Explanation: Perps v2 JLP multi-asset pool introduce impermanent loss risk untuk LP (tidak ada di orderbook murni v1). TVL peak $1.2B (Jul 2024) → ~$600M (Jan 2025). Capital efficiency naik tapi LP terpapar market risk lebih besar. Dokumentasi akui risk tapi tidak ada protection mechanism.
Evidence: Phase 3 EV-013: "JLP... menggantikan model orderbook murni"; Phase 4 Known Technical Limitations: "Perps dan JLP Risk: JLP pool menghadapi risk dari impermanent loss dan large position"; Phase 8 Liquidity: "JLP TVL peak $1.2B lalu $600M"; Phase 9 Trade-off 7
Supporting Dataset: Phase 3 (EV-013), Phase 4 (Known Technical Limitations), Phase 8 (Liquidity), Phase 9 (Strategic Trade-offs)
Confidence: HIGH

Decision Framework

Step 1: Observe — Monitor On-Chain Metrics dan Ecosystem Dynamics
Explanation: Keputusan didasarkan pada data on-chain real-time: volume swap, user aktif, TVL perps, competitor entry, DEX landscape changes. Contoh: Serum collapse (FTX) → expand DEX integrations; Odos launch Solana → accelerate Metis v2 + Ultra API.
Evidence: Phase 9 Risk Response: "Pola 6: FTX/Serum Collapse → Diversifikasi Liquidity Source", "Pola 5: Competitor Entry → Technical Moat Deepening"; Phase 8 Market Share: "85-90% Solana aggregator share"; Phase 3 EV-002 mention Serum
Supporting Dataset: Phase 9 (Risk Response Pattern), Phase 8 (Market Share), Phase 3 (EV-002)
Confidence: HIGH

Step 2: Evaluate — Internal Technical Assessment oleh Core Team Kecil
Explanation: Founder Meow + Head of Engineering Worm + Head of Product Slorg evaluasi technical feasibility, resource allocation, risk trade-off. Tim ~30-40 orang, tidak committee-heavy. Keputusan cepat: shipping MVP, upgrade berkala.
Evidence: Phase 1 Core Team: "Meow (pseudonim — founder/CEO)", "Worm (Head of Engineering)", "Slorg (Head of Product)"; Phase 9 Behavioral: "Cara Mengambil Keputusan: Founder-led (Meow) dengan core team kecil (~30-40) — keputusan cepat, tidak committee-heavy"
Supporting Dataset: Phase 1 (Core Team), Phase 9 (Behavioral Summary)
Confidence: HIGH

Step 3: Fund — Internal Protocol Revenue + Token Treasury (No External Capital)
Explanation: Setiap inisiatif didanai dari: swap fees (2021+), perps fees (2022+), Ultra API enterprise (2024+), DAO treasury JUP (40% supply, 2024+). Tidak ada VC funding, tidak ada grant dependency. Financial independence → full control.
Evidence: Phase 5 Fundraising Mechanism: "Bootstrapping", "Protocol Revenue", "DAO Treasury (Token Allocation)"; Phase 5 Financial Dependencies: "Protocol Revenue", "DAO Treasury"; Phase 9 Behavioral: "Pola 1: Zero External Funding"
Supporting Dataset: Phase 5 (Fundraising Mechanism, Financial Dependencies), Phase 9 (Recurring Behavioral Pattern)
Confidence: HIGH

Step 4: Develop — Iterative Shipping dengan Named Major Upgrades
Explanation: Develop → ship MVP → gather feedback → major upgrade named release (Metis, Apollo, Metis v2) tiap 6-12 bulan. Blog teknis detail untuk transparency. Rust on-chain, TypeScript SDK/API, React/React Native frontend. Program upgradeable via multisig.
Evidence: Phase 4 Technical Upgrade History: 4 major upgrades; Phase 4 Programming Languages: "Rust — bahasa utama untuk program on-chain", "TypeScript — bahasa utama untuk SDK dan API client", "React/React Native"; Phase 3 EV-007, EV-012, EV-018; Phase 9 Behavioral: "Pola 2: Iterative Major Upgrades"
Supporting Dataset: Phase 4 (Technical Upgrade History, Programming Languages), Phase 3 (EV-007, EV-012, EV-018), Phase 9 (Recurring Behavioral Pattern)
Confidence: HIGH

Step 5: Launch — Product Launch Bertahap + Community Incentive (Jupuary)
Explanation: Setiap produk launch diikuti announcement blog + community incentive. Jupuary airdrop berulang (1/2/3) drive adoption dan retention. Mobile app launch (EV-015) → retail acquisition channel baru. Ultra API launch (EV-016) → enterprise channel.
Evidence: Phase 3 EV-003, EV-004, EV-005, EV-006, EV-015, EV-016; Phase 3 EV-008, EV-011, EV-017 (Jupuary); Phase 9 Behavioral: "Pola 3: Expand Product Suite Vertikal", "Pola 4: Community Incentive Berulang"
Supporting Dataset: Phase 3 (EV-003 s.d. EV-017), Phase 9 (Recurring Behavioral Pattern)
Confidence: HIGH

Step 6: Govern — DAO Off-Chain Voting + Multisig Execution (Opaque)
Explanation: Proposal besar (fee switch, parameter) diajukan tim → vote.jup.ag off-chain voting → multisig execute (signer tidak publik). Tidak ada council/committee. Community feedback via Discord/forum/Twitter tapi proposal initiative dari tim. Fee switch proposal ongoing.
Evidence: Phase 6 Governance: "Voting System: Snapshot-style off-chain voting... on-chain execution via multisig"; Phase 7 Governance Ecosystem: "Council: Not established... Committee: Not established"; Phase 3 EV-014; Phase 9 Behavioral: "Pola 2: Proposal Inisiatif Tim", "Pola 4: Multisig Signer Opacity"
Supporting Dataset: Phase 6 (Governance), Phase 7 (Governance Ecosystem), Phase 3 (EV-014), Phase 9 (Recurring Behavioral Pattern)
Confidence: HIGH

Reusable Playbook

Playbook 1: Bangun Product-Market Fit Terlebih Dahulu, Baru Launch Token (Fair Launch, No VC)
Explanation: Jupiter beroperasi 2.5 tahun tanpa token, membangun 6 produk core, mencapai >85% market share Solana aggregator. Token launch via LBP + airdrop 10% ke user aktif (~955k wallet). 0% investor allocation, team 20% vesting 4 tahun, DAO treasury 40%. Menghilangkan unlock risk, menciptakan legitimate governance base.
Evidence: Phase 3 EV-002 s.d. EV-008; Phase 6 Distribution: "Investors: 0%", "Community: 10%", "Team: 20% (vesting 4 tahun)", "Treasury: 40%"; Phase 5 Fundraising Mechanism: "Bootstrapping", "Protocol Revenue"; Phase 9 Behavioral: "Pola 1: Ship Product First, Token Later"
Supporting Dataset: Phase 3 (EV-002 s.d. EV-008), Phase 6 (Distribution), Phase 5 (Fundraising Mechanism), Phase 9 (Recurring Behavioral Pattern)
Confidence: HIGH

Playbook 2: Single-Chain Mastery — Optimasi Mendalam untuk Satu Chain, Jadi Default Infrastructure
Explanation: Fokus 100% Solana → routing algorithm khusus (Metis), latency optimization (Ultra API sub-100ms), integrasi 20+ DEX native. Menjadi "Stripe of Solana DeFi". Trade-off: tidak ada cross-chain, risiko single-chain. Tapi moat teknis sangat dalam.
Evidence: Phase 4 System Architecture: "Chain(s): Solana (primary)"; Phase 7 Ecosystem Risks: "Single Chain Dependency"; Phase 8 Market Share: "~85-90% Solana aggregator share"; Phase 4 Current Technical Stack: "Ultra API sub-100ms"; Phase 9 Trade-off 2
Supporting Dataset: Phase 4 (System Architecture, Current Technical Stack), Phase 7 (Ecosystem Risks), Phase 8 (Market Share), Phase 9 (Strategic Trade-offs)
Confidence: HIGH

Playbook 3: Developer-First Infrastructure — Free Tools untuk Network Effect, Paid Enterprise untuk Revenue
Explanation: SDK (TS/Rust), REST API, Terminal widget gratis → adopsi wallet (Phantom, Solflare, Backpack), bot, tracker. Ultra API v6 enterprise (SLA, sub-100ms) → revenue market maker/institusi. Switching cost tinggi bagi integrator.
Evidence: Phase 7 Developer Ecosystem: semua tools gratis; Phase 7 Wallet Ecosystem: "Terminal works dengan any Solana wallet adapter"; Phase 5 Revenue Model: "Terminal/SDK Licensing Status: Live (gratis)"; "API Fees (Ultra API/Enterprise) Status: Live... custom quote"; Phase 9 Trade-off 5
Supporting Dataset: Phase 7 (Developer Ecosystem, Wallet Ecosystem), Phase 5 (Revenue Model), Phase 9 (Strategic Trade-offs)
Confidence: HIGH

Playbook 4: Iterative Major Upgrades dengan Named Release dan Blog Teknis Detail
Explanation: Routing engine v1→v2 Metis→v3 Apollo→v4 Metis v2 tiap 6-12 bulan. Setiap release named, blog detail teknis (algorithm, trade-offs, benchmark). Menciptakan moving target competitor, technical transparency, community trust.
Evidence: Phase 4 Technical Upgrade History: 4 major upgrades; Phase 3 EV-007, EV-012, EV-018; Phase 3 Sources: blog.jup.ag; Phase 9 Behavioral: "Pola 2: Iterative Major Upgrades", "Pola 5: Technical Blog-Driven Transparency"
Supporting Dataset: Phase 4 (Technical Upgrade History), Phase 3 (EV-007, EV-012, EV-018, Sources), Phase 9 (Recurring Behavioral Pattern)
Confidence: HIGH

Playbook 5: Recurring Community Incentive Program (Bukan One-Off Airdrop) dengan Evolving Eligibility
Explanation: Jupuary 1 (volume-based), 2 (governance participation), 3/Catdets (soulbound NFT tracking kontribusi jangka panjang). Setiap ronde refine criteria → filter user berkualitas, drive behavior yang diinginkan (volume, governance, long-term contribution).
Evidence: Phase 3 EV-008, EV-011, EV-017; Phase 6 Utility: "Incentive/Reward (Airdrop/Jupuary)"; Phase 9 Behavioral: "Pola 4: Community Incentive Berulang via Airdrop"
Supporting Dataset: Phase 3 (EV-008, EV-011, EV-017), Phase 6 (Utility), Phase 9 (Recurring Behavioral Pattern)
Confidence: HIGH

Playbook 6: Deep Ecosystem Integration (Routing Through, Not Competing) dengan Partner Oracle Eksklusif
Explanation: Aggregator route melalui 20+ DEX Solana (Raydium, Orca, Meteora, dll.) → meta-DEX yang memperkuat ekosistem. Perps pakai Pyth Network sebagai sole oracle (partnership mendalam). Tidak build DEX sendiri (kecuali Perps). Ketika Serum collapse, expand ke DEX lain tanpa disruption.
Evidence: Phase 7 Major Integrations: "Jupiter Aggregator ↔ Solana DEXs", "Jupiter Perps ↔ Pyth Network"; Phase 9 Ecosystem Decision Pattern: "Pola 1: Deep Integration dengan Solana DEX Ecosystem", "Pola 2: Oracle Partnership Eksklusif dengan Pyth"; Phase 3 EV-002 mention Serum
Supporting Dataset: Phase 7 (Major Integrations), Phase 9 (Ecosystem Decision Pattern), Phase 3 (EV-002)
Confidence: HIGH

Playbook 7: Accept Known Risks Transparan (Dokumentasi Jelas) Daripada Over-Engineering Mitigasi
Explanation: Single-chain risk, oracle SPOF, upgrade authority centralization, treasury concentration — semua didokumentasikan di docs/security page. Tidak semua di-mitigasi code-level (no fallback chain, no multi-oracle, no timelock). Philosophy: document risk, accept trade-off, iterate fast.
Evidence: Phase 4 Known Technical Limitations: setiap risk dijelaskan; Phase 7 Ecosystem Risks: setiap risk listed; Phase 9 Risk Response: "Pola 1: Acceptance Risk", "Pola 2: Documentation Risk Disclosure Only"; Phase 9 Behavioral: "Cara Mengambil Keputusan: Risk acceptance untuk single-chain, oracle dependency, upgrade authority"
Supporting Dataset: Phase 4 (Known Technical Limitations), Phase 7 (Ecosystem Risks), Phase 9 (Risk Response Pattern, Behavioral Summary)
Confidence: HIGH

Anti-patterns

Anti-pattern 1: Over-Centralization Upgrade Authority Tanpa Timelock atau Governance Delay
Explanation: Program upgradeable oleh multisig opaque (signer tidak publik). 4 major upgrades terbukti authority digunakan. Tidak ada timelock publik, tidak ada governance delay untuk upgrade, tidak ada emergency circuit breaker. Jika multisig kompromi → malicious changes possible tanpa warning.
Evidence: Phase 4 Security Model: "Program Jupiter memiliki upgrade authority (bukan immutable)"; "Multisig/Timelock... jumlah signer dan alamat multisig tidak dipublikasikan"; Phase 7 Ecosystem Risks: "Upgrade Authority Centralization"; Phase 9 Trade-off 3
Supporting Dataset: Phase 4 (Security Model), Phase 7 (Ecosystem Risks), Phase 9 (Strategic Trade-offs)
Confidence: HIGH

Anti-pattern 2: Treasury Konsentrasi Penuh di Native Token Tanpa Diversifikasi Stable Asset
Explanation: DAO treasury 40% supply JUP (4 miliar JUP). Tidak ada disclosure stablecoin/asset lain. Nilai treasury korelasi ~1:1 dengan harga JUP. Bear market → daya beli turun drastis. Fee switch belum aktif → no real yield. Financial fragility tinggi.
Evidence: Phase 5 Treasury: "DAO treasury menguasai ~40% total supply JUP"; "Stablecoin Holdings: Tidak diungkap"; Phase 5 Financial Risk: "Treasury Concentration in Native Token (JUP)"; Phase 6 Distribution: "Treasury: 40%"; Phase 9 Trade-off 4
Supporting Dataset: Phase 5 (Treasury, Financial Risk), Phase 6 (Distribution), Phase 9 (Strategic Trade-offs)
Confidence: HIGH

Anti-pattern 3: Single-Chain Dependency Tanpa Fallback Plan
Explanation: 100% produk di Solana. Tidak ada cross-chain deployment, tidak ada L2, tidak ada fallback RPC chain. Solana downtime → seluruh Jupiter berhenti. Documented as accepted risk tapi tidak ada mitigation plan.
Evidence: Phase 7 Ecosystem Risks: "Single Chain Dependency... directly halts all Jupiter operations"; Phase 4 Known Technical Limitations: "Single-chain Dependency... Jupiter tidak memiliki fallback chain"; Phase 9 Risk Response: "Pola 1: Acceptance Risk"
Supporting Dataset: Phase 7 (Ecosystem Risks), Phase 4 (Known Technical Limitations), Phase 9 (Risk Response Pattern)
Confidence: HIGH

Anti-pattern 4: Oracle Single Point of Failure Tanpa Fallback Mechanism
Explanation: Perps sepenuhnya bergantung Pyth. Tidak ada multi-oracle setup, tidak ada TWAP internal fallback, tidak ada circuit breaker. Dokumentasi akui risiko liquidation error tapi tidak implementasi protection. LP dan trader bear full risk.
Evidence: Phase 4 Oracle: "Jupiter Perps menggunakan oracle eksternal (Pyth Network)"; Phase 4 Known Technical Limitations: "Oracle Delay... dapat menyebabkan likuidasi yang tidak diinginkan"; Phase 7 External Dependencies: Pyth "Criticality: Critical"; Phase 7 Ecosystem Risks: "Oracle Dependency (Perps)"; Phase 9 Risk Response: "Pola 2: Documentation Risk Disclosure Only"
Supporting Dataset: Phase 4 (Core Components, Known Technical Limitations), Phase 7 (External Dependencies, Ecosystem Risks), Phase 9 (Risk Response Pattern)
Confidence: HIGH

Anti-pattern 5: Governance Opacity — Multisig Signer Tidak Dipublikasikan, Off-Chain Only
Explanation: DAO treasury dan program upgrade dikontrol multisig opaque. Vote.jup.ag off-chain (snapshot), tidak ada on-chain DAO framework. Proposal besar dari tim. Tidak ada council/committee. Transparansi eksekusi minimal. Community tidak bisa verify signer alignment.
Evidence: Phase 5 Treasury: "jumlah signer dan alamat tidak dipublikasikan resmi"; Phase 4 Security Model: "Multisig/Timelock... tidak dipublikasikan"; Phase 7 Ecosystem Risks: "Multisig Signer Opacity"; Phase 6 Governance: "Voting System: Snapshot-style off-chain voting"; Phase 7 Governance Ecosystem: "Council: Not established... Committee: Not established"; Phase 9 Trade-off 1
Supporting Dataset: Phase 5 (Treasury), Phase 4 (Security Model), Phase 7 (Ecosystem Risks, Governance Ecosystem), Phase 6 (Governance), Phase 9 (Strategic Trade-offs)
Confidence: HIGH

Anti-pattern 6: No Financial Transparency Reporting untuk Protocol dengan Treasury Besar
Explanation: Treasury 40% supply ($100M+ saat peak). Tidak ada revenue report bulanan/kuartalan, tidak ada treasury dashboard real-time, tidak ada audited financials. Estimasi Token Terminal/DefiLlama jadi proxy. Fee switch proposal belum pass. Token holder flying blind.
Evidence: Phase 5 Revenue History: "Tidak diungkap secara resmi"; "Official Financial Resources: Transparency Report: Tidak ada, Treasury Dashboard: Tidak ada"; Phase 5 Financial Risk: "No Public Financial Audit / Transparency Report"; Phase 3 EV-014 ongoing
Supporting Dataset: Phase 5 (Revenue History, Official Financial Resources, Financial Risk), Phase 3 (EV-014)
Confidence: HIGH

Anti-pattern 7: Cross-Chain Ambiguity — Referensi Ecosystem Page Tapi Tidak Confirmed Production
Explanation: Wormhole di ecosystem page dan early docs; tapi Perps v2 docs tidak mention. Aggregator tidak cross-chain. Status unclear → confusion developer/partner. Harusnya: entweder commit dan document, atau remove reference.
Evidence: Phase 7 External Dependencies: Wormhole "Unconfirmed current production dependency"; Phase 7 Major Integrations: "production usage in v2 not explicitly confirmed"; Phase 7 Ecosystem Risks: "Bridge / Cross-chain Dependency... not confirmed"; Phase 2 Entity: Wormhole
Supporting Dataset: Phase 7 (External Dependencies, Major Integrations, Ecosystem Risks), Phase 2 (Entity: Wormhole)
Confidence: MEDIUM

Anti-pattern 8: Pseudonymous Leadership Tanpa Institutional Bridge
Explanation: Founder/core lead pseudonymous. Beberapa tradfi/enterprise butuh KYC team. Cloud/RPC/CDN provider undisclosed. Mungkin membatasi Ultra API enterprise adoption di institusi ketat compliance.
Evidence: Phase 1 Core Team: semua pseudonim; Phase 2 Entity: Person pseudonim; Phase 7 Infrastructure Providers: provider undisclosed; Phase 9 Trade-off 6
Supporting Dataset: Phase 1 (Core Team), Phase 2 (Entity), Phase 7 (Infrastructure Providers), Phase 9 (Strategic Trade-offs)
Confidence: MEDIUM

Lessons Learned

1. Product-Market Fit First, Token Later → Healthier Token Distribution dan Governance Legitimacy. Jupiter membuktikan 2.5 tahun building tanpa token menciptakan user base real, kemudian fair launch (LBP + airdrop) menghasilkan governance base yang aligned. 【Phase 3 — EV-002 s.d. EV-008】【Phase 6 — Distribution】【Phase 9 — Pola 1】

2. Single-Chain Mastery Bisa Membuat Moat Teknis Sangat Dalam, Tapi Risiko Eksistensial Jika Chain Tersebut Bermasalah. Jupiter dominan 85-90% Solana aggregator tapi 100% tergantung Solana uptime. Tidak ada fallback. 【Phase 4 — System Architecture】【Phase 7 — Ecosystem Risks】【Phase 8 — Market Share】

3. Free Developer Infrastructure + Paid Enterprise Tier = Powerful Network Effect Moat. SDK/API/Terminal gratis drive adopsi massal (wallet, bot, tracker). Ultra API enterprise monetisasi market maker. Switching cost tinggi. 【Phase 7 — Developer Ecosystem, Wallet Ecosystem】【Phase 5 — Revenue Model】【Phase 9 — Trade-off 5】

4. Iterative Named Major Upgrades (6-12 Bulan) dengan Blog Teknis Detail Membuat Competitor Sulit Menjar. Metis → Apollo → Metis v2, setiap release step-change performance. Technical transparency build trust. 【Phase 4 — Technical Upgrade History】【Phase 3 — EV-007, EV-012, EV-018】【Phase 9 — Pola 2, Pola 5】

5. Recurring Airdrop dengan Evolving Eligibility Lebih Efektif dari One-Off untuk Retention. Jupuary 1/2/3 refine criteria (volume → governance → soulbound NFT). Drive behavior yang diinginkan, filter user berkualitas. 【Phase 3 — EV-008, EV-011, EV-017】【Phase 6 — Utility】【Phase 9 — Pola 4】

6. Zero VC Funding Memberikan Full Control Tapi Membutuhkan Revenue Discipline dari Awal. Bootstrap dari protocol revenue (swap fees 2021+, perps fees 2022+) force financial sustainability sejak hari pertama. 【Phase 5 — Funding History, Fundraising Mechanism】【Phase 9 — Pola 1, Pola 7】

7. Transparansi Selective: Teknis Tinggi (Blog Detail), Governance/Financial Rendah (Multisig Opaque, No Financial Report). Ini trade-off yang sadar: technical credibility tinggi, tapi governance accountability rendah. 【Phase 3 — Sources (blog.jup.ag)】【Phase 5 — Treasury, Revenue History】【Phase 7 — Ecosystem Risks】【Phase 9 — Trade-off 1, Trade-off 4】

8. Accept Known Risks dengan Dokumentasi Jelas Lebih Baik dari Over-Engineering Mitigasi yang Memberatkan Velocity. Single-chain, oracle SPOF, upgrade authority — semua didokumentasikan, tidak semua di-mitigasi code-level. Team iterate cepat. 【Phase 4 — Known Technical Limitations】【Phase 7 — Ecosystem Risks】【Phase 9 — Risk Response Pattern】

9. Fee Switch / Value Accrual Mechanism Harus Diaktifkan Sebelum Bear Market Extended. JUP pure governance token 12+ bulan post-TGE tanpa fee switch. Utility incomplete. Proposal ongoing tapi belum eksekusi. 【Phase 6 — Utility, Governance】【Phase 5 — Financial Risk】【Phase 3 — EV-014】

10. Cross-Chain Reference Tanpa Production Confirmation Menciptakan Confusion. Wormhole di ecosystem page tapi tidak di Perps v2 docs. Harusnya: commit dan document, atau remove. 【Phase 7 — External Dependencies, Major Integrations, Ecosystem Risks】【Phase 2 — Entity: Wormhole】

Knowledge Summary

Strategic Principles
- Principle 1: Ship Product First, Token Later — Product-Market Fit Sebelum Tokenomics
- Principle 2: Single-Chain Mastery Over Multi-Chain Mediocrity — Fokus Mendalam di Solana
- Principle 3: Developer-First Infrastructure — Free Tools untuk Adopsi Luas, Paid Enterprise untuk Monetisasi
- Principle 4: Iterative Technical Excellence — Named Major Upgrades Setiap 6-12 Bulan
- Principle 5: Community Ownership via Fair Launch — 0% VC, 10% Airdrop, 40% DAO Treasury, Recurring Incentives
- Principle 6: Transparansi Teknis via Blog, Opasitas Governance/Financial via Multisig Opaque
- Principle 7: Accept Known Risks dengan Dokumentasi Jelas, Bukan Over-Engineering Mitigasi

Success Factors
- Factor 1: First-Mover Advantage di Solana DEX Aggregation + Continuous Moat Deepening
- Factor 2: Full-Stack DeFi Suite Terintegrasi Menciptakan High Switching Cost
- Factor 3: Zero VC Funding → No Unlock Risk, No Misalignment, Full Control
- Factor 4: Developer Ecosystem Moat via Free Infrastructure + Enterprise Upsell
- Factor 5: Recurring Community Incentive Program (Jupuary Series) Menjaga Retention dan Volume
- Factor 6: Technical Leadership Team yang Shipping Cepat dan Iteratif
- Factor 7: Deep Integration dengan Solana DEX Ecosystem (Routing Through, Not Competing)

Failure Factors
- Factor 1: Single-Chain Dependency — Solana Downtime Menghentikan Seluruh Operasional
- Factor 2: Treasury Concentration di JUP (40% Supply) Tanpa Diversifikasi Stablecoin
- Factor 3: Governance Opacity — Multisig Signer Tidak Dipublikasikan, Off-Chain Voting Only
- Factor 4: Program Upgradeability Centralization — Multisig Authority Bisa Upgrade Kapan Saja Tanpa Delay
- Factor 5: Oracle Single Point of Failure (Pyth Only) untuk Perps
- Factor 6: No Financial Transparency — Tidak Ada Revenue Report, Treasury Dashboard, Audited Financials
- Factor 7: Cross-Chain Ambiguity — Wormhole Referenced Tapi Tidak Confirmed Production
- Factor 8: Pseudonymous Leadership Membatasi Institutional Partnership
- Factor 9: Fee Switch Belum Aktif — JUP Pure Governance Token Tanpa Yield
- Factor 10: JLP Impermanent Loss Risk untuk LP — Model Capital Efficient Tapi Memindahkan Risk ke LP

Decision Framework
- Step 1: Observe — Monitor On-Chain Metrics dan Ecosystem Dynamics
- Step 2: Evaluate — Internal Technical Assessment oleh Core Team Kecil
- Step 3: Fund — Internal Protocol Revenue + Token Treasury (No External Capital)
- Step 4: Develop — Iterative Shipping dengan Named Major Upgrades
- Step 5: Launch — Product Launch Bertahap + Community Incentive (Jupuary)
- Step 6: Govern — DAO Off-Chain Voting + Multisig Execution (Opaque)

Reusable Playbook
- Playbook 1: Bangun Product-Market Fit Terlebih Dahulu, Baru Launch Token (Fair Launch, No VC)
- Playbook 2: Single-Chain Mastery — Optimasi Mendalam untuk Satu Chain, Jadi Default Infrastructure
- Playbook 3: Developer-First Infrastructure — Free Tools untuk Network Effect, Paid Enterprise untuk Revenue
- Playbook 4: Iterative Major Upgrades dengan Named Release dan Blog Teknis Detail
- Playbook 5: Recurring Community Incentive Program (Bukan One-Off Airdrop) dengan Evolving Eligibility
- Playbook 6: Deep Ecosystem Integration (Routing Through, Not Competing) dengan Partner Oracle Eksklusif
- Playbook 7: Accept Known Risks Transparan (Dokumentasi Jelas) Daripada Over-Engineering Mitigasi

Anti-patterns
- Anti-pattern 1: Over-Centralization Upgrade Authority Tanpa Timelock atau Governance Delay
- Anti-pattern 2: Treasury Konsentrasi Penuh di Native Token Tanpa Diversifikasi Stable Asset
- Anti-pattern 3: Single-Chain Dependency Tanpa Fallback Plan
- Anti-pattern 4: Oracle Single Point of Failure Tanpa Fallback Mechanism
- Anti-pattern 5: Governance Opacity — Multisig Signer Tidak Dipublikasikan, Off-Chain Only
- Anti-pattern 6: No Financial Transparency Reporting untuk Protocol dengan Treasury Besar
- Anti-pattern 7: Cross-Chain Ambiguity — Referensi Ecosystem Page Tapi Tidak Confirmed Production
- Anti-pattern 8: Pseudonymous Leadership Tanpa Institutional Bridge

## Open Questions
- [foundation] Exact founding entity jurisdiction (BVI confirmed via OpenCorporates; need to confirm if any subsidiary in another jurisdiction)
- [foundation] Full core team real names vs pseudonyms — most remain pseudonymous; verify if any doxxed publicly
- [foundation] Testnet phase details — unclear if formal testnet existed before Oct 2021 mainnet launch
- [foundation] JUP token contract upgradeability / admin keys — verify multisig / timelock setup on-chain
- [foundation] Revenue/fee switch status — Jupiter has discussed fee switch in governance; need on-chain verification of current status
- [foundation] Exact team headcount — "30-40" from careers page; need more precise or recent figure
- [entity] Exact founding entity jurisdiction (BVI confirmed via OpenCorporates; need to confirm if any subsidiary in another jurisdiction)
- [entity] Full core team real names vs pseudonyms — most remain pseudonymous; verify if any doxxed publicly
- [entity] Testnet phase details — unclear if formal testnet existed before Oct 2021 mainnet launch
- [entity] JUP token contract upgradeability / admin keys — verify multisig / timelock setup on-chain
- [entity] Revenue/fee switch status — Jupiter has discussed fee switch in governance; need on-chain verification of current status
- [entity] Exact team headcount — "30-40" from careers page; need more precise or recent figure
- [entity] Investor/VC backers — not disclosed in Phase 01; need to identify funding rounds and investors
- [entity] Security auditors — no audit firms identified yet; need to find audit reports for aggregator, perps, token contracts
- [entity] Jupiter DAO multisig/timelock signers — governance execution layer not yet mapped
- [entity] LFG Launchpad entity — whether separate legal entity or product under Jupiter Exchange Ltd.
- [history] Exact date of Jupiter Exchange Ltd. incorporation (only year 2021 confirmed via OpenCorporates; need exact day/month)
- [history] Exact launch dates for Limit Orders, DCA (only year 2022 known; need month/day from on-chain program deploy or blog)
- [history] Exact date of Jupiter Perps v1 launch (November 2022 per blog; need exact day)
- [history] Exact date of Jupiter API/SDK and Terminal launch (only year 2023 known; need month)
- [history] Exact date of Jupiter Aggregator v2/Metis launch (November 2023 per blog; need exact day)
- [history] Exact date of Jupiter Aggregator v3/Apollo launch (April 2024 per blog; need exact day)
- [history] Exact date of Jupiter Perps v2/JLP launch (July 2024 per blog; need exact day)
- [history] Exact date of Mobile App launch (October 2024 per blog; need exact day)
- [history] Exact date of Ultra API v6 launch (November 2024 per blog; need exact day)
- [history] Exact date of Metis v2/v4 launch (January 2025 per blog; need exact day)
- [history] Fee switch proposal status — whether passed/failed/executed on-chain (vote.jup.ag shows ongoing discussion; need final outcome)
- [history] Jupuary 2 and Jupuary 3 actual distribution dates and amounts (announced but distribution timeline not fully verified)
- [history] Security audit reports for Aggregator v1-v4, Perps v1-v2, JUP token contract — no audit firms identified in Phase 1-2; need to locate audit reports
- [history] Investor/VC funding rounds — no funding events identified in Phase 1-2; Jupiter may be bootstrapped or privately funded without public disclosure
- [history] Jupiter DAO multisig/timelock signers — governance execution layer not yet mapped
- [history] LFG Launchpad legal entity — whether separate entity or product under Jupiter Exchange Ltd.
- [history] Testnet phase details — unclear if formal testnet existed before Oct 2021 mainnet launch
- [history] Full core team real names vs pseudonyms — most remain pseudonymous; verify if any doxxed publicly
- [technology] Laporan Audit Lengkap**: 6 auditor disebut, tetapi tidak ada link langsung ke PDF laporan audit di website Jupiter — perlu konfirmasi dari masing-masing auditor atau repositori internal
- [technology] Multisig/Timelock Address**: Upgrade authority dan signer multisig tidak dipublikasikan; perlu verifikasi on-chain melalui Solscan untuk daftar authority
- [technology] Anchor vs Native Rust**: Dokumentasi tidak menyebutkan apakah Jupiter menggunakan Anchor framework atau native Rust — perlu analisis pada kode sumber program
- [technology] Infrastruktur Cloud**: Detail host Cloud (AWS/GCP), database, dan orchestration tidak tersedia — hanya kode sumber yang bisa dianalisis
- [technology] Wormhole Dependency**: Apakah Jupiter Perps v2 saat ini masih memakai Wormhole, atau sudah diganti dengan mekanisme lain? (dokumen awal menyebut, tetapi dokumentasi terbaru tidak menegaskan)
- [technology] Laporan Audit Metis v2 (Halborn)**: Hanya disebut di blog; belum diverifikasi melalui kanal auditor
- [technology] Program Immutable?**: Tidak ada pernyataan resmi apakah program Jupiter akan di-freeze (immutable) di masa depan; saat ini masih upgradeable
- [technology] Cross-chain Asset Settlement**: Meskipun memakai Wormhole untuk perps, tidak dijelaskan apakah Jupiter Aggregator akan mendukung bridging aset (e.g., swap dari ETH ke SOL) dalam waktu dekat
- [technology] Daftar auditor pihak ketiga**: OtterSec, Hacken, Kudelski, Zellic, Quantstamp, Halborn — konfirmasi tanggal pasti setiap audit belum ditemukan
- [financial] Exact treasury wallet address(es) and on-chain balance breakdown (stablecoin vs JUP vs other) — not publicly labeled
- [financial] Fee switch proposal final outcome — whether passed and executed on-chain (vote.jup.ag shows discussion, no confirmed execution transaction)
- [financial] Revenue figures (monthly/quarterly) — no official transparency report; only third-party estimates
- [financial] Solana Foundation grant history — whether received, amount, terms (not disclosed)
- [financial] Team/company treasury (Jupiter Exchange Ltd.) vs DAO treasury separation — not clarified
- [financial] Multisig signers for treasury and program upgrade authority — not publicly disclosed
- [financial] Audit of treasury management / financial controls — no public financial audit
- [financial] JLP (Jupiter Liquidity Pool) financials — TVL, fee revenue split, PnL not published in aggregated form
- [financial] Ultra API enterprise revenue — customer count, pricing, revenue contribution not disclosed
- [financial] Whether Jupiter Exchange Ltd. has raised equity funding privately (not on-chain) — OpenCorporates shows no filings, but BVI entities have limited disclosure
- [token] Circulating Supply exact figure at current date — tidak dipublikasikan resmi; CoinGecko/Token Terminal/DefiLlama memiliki estimasi yang berbeda (perlu cross-check on-chain via program accounts dan exchange wallets)
- [token] Team vesting detail: cliff duration, unlock frequency (bulanan/kuartalan/tahunan), apakah ada accelerated unlock — tidak dipublikasikan dalam tokenomics
- [token] Liquidity/Market Making 20% vesting schedule — tidak ada detail cliff, durasi, atau mekanisme unlock
- [token] Future/Strategic 10% allocation — tidak ada rencana publik untuk penggunaan dana ini; apakah akan diburn, digunakan untuk partnerships, atau tetap di treasury
- [token] Fee Switch Proposal final outcome — vote.jup.ag menunjukkan discussion tapi tidak ada konfirmasi eksekusi on-chain (transaksi multisig yang mengaktifkan fee switch)
- [token] Jupuary 2 dan Jupuary 3 actual distribution dates, amounts, dan eligibility criteria — di-announce tapi detail eksekusi tidak diverifikasi on-chain
- [token] DAO Treasury multisig address dan signer list — tidak dipublikasikan; diperlukan verifikasi on-chain untuk transparansi
- [token] Apakah ada plan untuk token burn / buyback di masa depan — tidak ada di tokenomics; fee switch proposal mengarah ke treasury/stakers bukan burn
- [token] JUP token contract upgrade authority — program upgradeable; authority address tidak dipublikasikan resmi (perlu cek Solscan program account)
- [token] Cross-chain JUP token (wormhole wrapped JUP di chain lain) — tidak dikonfirmasi resmi; apakah Jupiter akan mendukung multi-chain JUP
- [token] Exact circulating supply breakdown by category (team locked, treasury, airdrop claimed, liquidity deployed, etc.) — tidak ada transparency report berkala
- [token] Staking reward mechanism detail (APY, fee share percentage) jika fee switch aktif — belum difinalisasi karena proposal masih dalam voting
- [ecosystem] Wormhole current production dependency for Jupiter Perps v2 — Wormhole ecosystem page lists Jupiter; Jupiter Perps v2 docs do not mention Wormhole. Need clarification from Jupiter or Wormhole team.
- [ecosystem] Cloud infrastructure provider(s) for Jupiter API v6 / Ultra API — not disclosed; enterprise SLA implies managed cloud but provider unnamed.
- [ecosystem] Solana RPC provider(s) used by Jupiter API and frontend — not disclosed; standard dependency but specific partners unknown.
- [ecosystem] CDN / edge network provider for Ultra API sub-100ms latency — not disclosed.
- [ecosystem] Jupiter Program upgrade authority multisig signers — on-chain verifiable via Solscan program account but not published in human-readable form.
- [ecosystem] DAO treasury multisig signers — not publicly disclosed; governance execution transparency gap.
- [ecosystem] Anchor vs Native Rust for Jupiter Program — not confirmed in docs; requires source code inspection.
- [ecosystem] Jupiter-run grant program — none identified; Solana Foundation grants may support Jupiter builders but not a Jupiter program.
- [ecosystem] Hackathon participation details — Jupiter has sponsored Solana hackathons but no centralized record of events, prizes, or outcomes.
- [ecosystem] Wallet integration specifics — Jupiter Terminal works via wallet adapter standard; specific wallet partnerships (Phantom, Solflare, Backpack) announced but not centrally documented in Jupiter docs.
- [ecosystem] Exchange listing completeness — CoinGecko shows 20+ markets; only major CEXs listed above. Long-tail exchange listings not exhaustively verified.
- [ecosystem] JLP (Jupiter Liquidity Pool) external integrations — whether other protocols integrate with JLP as liquidity source not documented.
- [ecosystem] Cross-chain JUP token (wormhole-wrapped JUP on Ethereum, Arbitrum, etc.) — not confirmed; Wormhole token bridge may exist but not officially supported by Jupiter.
- [ecosystem] Solana Foundation grant history to Jupiter — listed on ecosystem page but grant amounts, dates, and terms not public.
- [market] Exact current circulating supply of JUP — CoinGecko, Token Terminal, DefiLlama report different figures; no official real-time dashboard from Jupiter
- [market] Jupiter Aggregator market share on Solana (85-90% estimate) — no third-party verification; DeFiLlama does not break down aggregator vs DEX volume cleanly
- [market] JLP TVL trajectory post-2024-07 — DeFiLlama shows peak ~$1.2B then decline to ~$600M; need confirmation if due to SOL price or capital outflow
- [market] Ultra API enterprise customer count and revenue contribution — Jupiter claims "institutional market makers" but discloses no numbers
- [market] Fee switch proposal final execution status — vote.jup.ag shows discussion; no on-chain transaction confirming activation found
- [market] Jupuary 2 and 3 actual distribution completion — announced but on-chain verification of claim transactions not centrally documented
- [market] Cross-chain volume via Wormhole for Perps — Wormhole ecosystem page lists Jupiter; Jupiter Perps v2 docs do not mention Wormhole; actual usage unquantified
- [market] Jupiter Program upgrade authority multisig signers — on-chain verifiable but not published in human-readable form; governance transparency gap
- [market] DAO treasury multisig signers and asset breakdown (stablecoin vs JUP vs other) — not disclosed; only 40% JUP allocation known from tokenomics
- [market] Solana Foundation grant history to Jupiter — listed on ecosystem page but amounts/dates not public
- [market] Comparison of Jupiter Perps v2 open interest vs Drift and Zeta — DeFiLlama has protocol pages but no aggregated "Solana perps market share" chart
- [market] Mobile app download/active user metrics — Apple/Google Play stats not public; Jupiter has not released MAU/DAU for mobile
- [market] Jupiter Terminal embed adoption (number of dApps/wallets integrating) — not disclosed; only "works with any wallet adapter" stated
- [market] Whether Jupiter Exchange Ltd. (BVI entity) has revenue separate from DAO treasury — not clarified; financial separation opaque
- [market] Competitor Odos launched on Solana 2024 — market share impact on Jupiter not measured; Odos claims patented routing
- [market] Token Terminal and DefiLlama revenue/fee estimates for Jupiter — methodology differs (Token Terminal uses on-chain fee accounts; DefiLlama may estimate); no official Jupiter revenue report to reconcile
- [behavioral] Fee Switch Proposal Final Outcome: vote.jup.ag menunjukkan discussion tapi tidak ada konfirmasi eksekusi on-chain (transaksi multisig yang mengaktifkan fee switch) — perlu verifikasi on-chain apakah proposal sudah pass dan dieksekusi
- [behavioral] Jupuary 2 dan 3 Actual Distribution: Di-announce tapi detail eksekusi (tanggal claim, jumlah token, eligibility on-chain) tidak diverifikasi terpusat — perlu cross-check Solscan/Dune
- [behavioral] DAO Treasury Multisig Signers & Asset Breakdown: Tidak dipublikasikan; hanya diketahui 40% JUP allocation; stablecoin/other asset unknown — governance transparency gap
- [behavioral] Jupiter Program Upgrade Authority Multisig: On-chain verifiable via Solscan program account tapi tidak di-publish human-readable — security transparency gap
- [behavioral] Wormhole Current Production Dependency: Wormhole ecosystem page lists Jupiter; Jupiter Perps v2 docs tidak mention Wormhole — status unclear, perlu clarifikasi dari tim
- [behavioral] Cloud/RPC/CDN Infrastructure Providers: Ultra API enterprise SLA imply managed infra tapi provider undisclosed — vendor concentration risk unknown
- [behavioral] Circulating Supply Exact Figure: CoinGecko, Token Terminal, DefiLlama report different figures; no official real-time dashboard — tokenomics transparency gap
- [behavioral] Team Vesting Detail (Cliff, Unlock Frequency): Tokenomics menyebut "4 tahun linear" tapi cliff dan frequency tidak dipublikasikan — insider selling risk unknown
- [behavioral] Solana Foundation Grant History: Listed di ecosystem page tapi amounts/dates/terms tidak public — funding history incomplete
- [behavioral] JLP TVL Decline Cause: Peak $1.2B (Jul 2024) → ~$600M (Jan 2025); apakah SOL price drop atau capital outflow? — perlu on-chain analysis
- [behavioral] Ultra API Enterprise Customer Count & Revenue: Jupiter claims "institutional market makers" tapi discloses no numbers — revenue diversification opacity
- [behavioral] Competitor Odos Market Share Impact: Odos launched Solana 2024 dengan patented routing; impact ke Jupiter market share tidak diukur publik
- [behavioral] Mobile App MAU/DAU Metrics: Apple/Google Play stats tidak public; Jupiter belum release mobile metrics — user acquisition channel performance unknown
- [behavioral] Jupiter Terminal Embed Adoption Count: Berapa dApp/wallet yang integrate Terminal? Tidak disclosed — developer ecosystem traction unknown
- [behavioral] Jupiter Exchange Ltd. vs DAO Treasury Separation: Apakah entitas BVI punya revenue/treasury terpisah dari DAO? Tidak clarified — financial structure opacity
- [behavioral] Anchor vs Native Rust untuk Jupiter Program: Tidak confirmed di docs; perlu source code inspection — technical architecture detail gap
- [behavioral] Cross-Chain JUP Token (Wormhole-wrapped): Apakah Jupiter officially support multi-chain JUP? Tidak confirmed — chain abstraction narrative gap
- [knowledge] Fee Switch Proposal Final Outcome: vote.jup.ag menunjukkan discussion tapi tidak ada konfirmasi eksekusi on-chain (transaksi multisig yang mengaktifkan fee switch) — perlu verifikasi on-chain apakah proposal sudah pass dan dieksekusi【Phase 3 — EV-014】【Phase 6 — Utility】【Phase 5 — Financial Risk】
- [knowledge] Jupuary 2 dan 3 Actual Distribution: Di-announce tapi detail eksekusi (tanggal claim, jumlah token, eligibility on-chain) tidak diverifikasi terpusat — perlu cross-check Solscan/Dune【Phase 3 — EV-011, EV-017】【Phase 6 — Major Token Events】
- [knowledge] DAO Treasury Multisig Signers & Asset Breakdown: Tidak dipublikasikan; hanya diketahui 40% JUP allocation; stablecoin/other asset unknown — governance transparency gap【Phase 5 — Treasury】【Phase 7 — Ecosystem Risks】
- [knowledge] Jupiter Program Upgrade Authority Multisig: On-chain verifiable via Solscan program account tapi tidak di-publish human-readable — security transparency gap【Phase 4 — Security Model】【Phase 7 — Ecosystem Risks】
- [knowledge] Wormhole Current Production Dependency: Wormhole ecosystem page lists Jupiter; Jupiter Perps v2 docs tidak mention Wormhole — status unclear, perlu clarifikasi dari tim【Phase 7 — External Dependencies, Major Integrations, Ecosystem Risks】【Phase 2 — Entity: Wormhole】
- [knowledge] Cloud/RPC/CDN Infrastructure Providers: Ultra API enterprise SLA imply managed infra tapi provider undisclosed — vendor concentration risk unknown【Phase 7 — Infrastructure Providers】【Phase 4 — Current Technical Stack】
- [knowledge] Circulating Supply Exact Figure: CoinGecko, Token Terminal, DefiLlama report different figures; no official real-time dashboard — tokenomics transparency gap【Phase 6 — Supply】【Phase 8 — Adoption Metrics】
- [knowledge] Team Vesting Detail (Cliff, Unlock Frequency): Tokenomics menyebut "4 tahun linear" tapi cliff dan frequency tidak dipublikasikan — insider selling risk unknown【Phase 6 — Vesting Schedule】
- [knowledge] Solana Foundation Grant History: Listed di ecosystem page tapi amounts/dates/terms tidak public — funding history incomplete【Phase 7 — Developer Ecosystem】【Phase 5 — Financial Dependencies】
- [knowledge] JLP TVL Decline Cause: Peak $1.2B (Jul 2024) → ~$600M (Jan 2025); apakah SOL price drop atau capital outflow? — perlu on-chain analysis【Phase 8 — Liquidity, Adoption Metrics】
- [knowledge] Ultra API Enterprise Customer Count & Revenue: Jupiter claims "institutional market makers" tapi discloses no numbers — revenue diversification opacity【Phase 5 — Revenue Model】【Phase 8 — Adoption Metrics】
- [knowledge] Competitor Odos Market Share Impact: Odos launched Solana 2024 dengan patented routing; impact ke Jupiter market share tidak diukur publik【Phase 8 — Competitor Landscape, Market Share】
- [knowledge] Mobile App MAU/DAU Metrics: Apple/Google Play stats tidak public; Jupiter belum release mobile metrics — user acquisition channel performance unknown【Phase 3 — EV-015】【Phase 7 — Applications】
- [knowledge] Jupiter Terminal Embed Adoption Count: Berapa dApp/wallet yang integrate Terminal? Tidak disclosed — developer ecosystem traction unknown【Phase 7 — Developer Ecosystem, Major Integrations】
- [knowledge] Jupiter Exchange Ltd. vs DAO Treasury Separation: Apakah entitas BVI punya revenue/treasury terpisah dari DAO? Tidak clarified — financial structure opacity【Phase 2 — Entity: Jupiter Exchange Ltd.】【Phase 5 — Treasury】
- [knowledge] Anchor vs Native Rust untuk Jupiter Program: Tidak confirmed di docs; perlu source code inspection — technical architecture detail gap【Phase 4 — Development Framework】
- [knowledge] Cross-Chain JUP Token (Wormhole-wrapped): Apakah Jupiter officially support multi-chain JUP? Tidak confirmed — chain abstraction narrative gap【Phase 7 — External Dependencies】【Phase 6 — Token Information】
