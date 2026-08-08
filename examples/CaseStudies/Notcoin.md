# Notcoin — Deep Case Study (Phased)

**CIF Dataset — Deep Dossier · Tier: Deep (anchor project)**
**Source:** Deep Research (DeepSeek), Format v3 Dependency Pipeline (10/11 phases: foundation, entity, history, technology, financial, token, ecosystem, market, behavioral, knowledge). **Auto-assembled** by `tools/ingest.py` (deterministic, no LLM, strict data_project/ contract) — each phase extracted and concatenated in dependency order per `docs/Protocol/Deep-Research-Brief.md`; the reasoning is the source reports'.
**Raw sources archived:** doc_backup/deep/Notcoin_foundation_2026-08.docx, doc_backup/deep/Notcoin_entity_2026-08.docx, doc_backup/deep/Notcoin_history_2026-08.docx, doc_backup/deep/Notcoin_technology_2026-08.docx, doc_backup/deep/Notcoin_financial_2026-08.docx, doc_backup/deep/Notcoin_token_2026-08.docx, doc_backup/deep/Notcoin_ecosystem_2026-08.docx, doc_backup/deep/Notcoin_market_2026-08.docx, doc_backup/deep/Notcoin_behavioral_2026-08.docx, doc_backup/deep/Notcoin_knowledge_2026-08.docx.
**Phases not run:** conflict.

> Faithful concatenation of phase outputs — no fabrication, no distillation beyond what the closing phase (Conflict Resolution / Validation) itself states. Consider a periodic QC pass.

---
## Foundation Intelligence
_ref: `docs/Ontology/Identity.md`, `docs/Ontology/Team.md`_

PROJECT: Notcoin
Official Name: Notcoin
Symbol: NOT
Category: Telegram Mini App / Tap-to-Earn Game / Consumer Crypto Onboarding
Founding Entity: Open Builders (yurisdiksi tidak diumumkan secara publik)
Founders: Sasha Plotnikov (Co-founder, CEO); Mad Tail (Co-founder, CTO — pseudonim)
Core Team: Open Builders (tim inti ~10-15 orang identitas terverifikasi parsial; kontributor eksternal & advisor tidak diungkapkan totalnya)
Country: Tidak diumumkan (tim terdistribusi global; entitas hukum Open Builders tidak mempublikasikan yurisdiksi inkorporasi)
Launch Date - Testnet: n/a (produk diluncurkan langsung di Telegram mainnet environment)
Launch Date - Mainnet: 1 Januari 2024 (HIGH) [Notcoin Blog, https://notcoin.com/blog/notcoin-launch]
Launch Date - TGE: 16 Mei 2024 (HIGH) [Binance Announcement, https://www.binance.com/en/support/announcement/notcoin-not-listing]
Main Products: Notcoin Game (Tap-to-Earn Mini App di Telegram); Notcoin Explore (discovery platform untuk Mini App lain); Notcoin Earn (kampanye reward on-chain); Notcoin Wallet (smart wallet berbasis Telegram/ERC-4337)
Official Website: https://notcoin.com
Repository: https://github.com/notcoin (organisasi GitHub publik; repositori utama game tidak open-source penuh)
Documentation: https://docs.notcoin.com
Social - X/Twitter: @notcoin
Social - Discord: https://discord.gg/notcoin
Social - Telegram: @notcoin (channel resmi); @notcoin_bot (bot game)
Block Explorer: https://tonscan.org (TON mainnet explorer untuk token NOT)
Token Contract: EQB... (TON Jetton master address: EQAvlWfdqGdO... — lengkap: EQAvlWfdqGdO-...; verifikasi di tonscan.org) (HIGH) [Tonviewer, https://tonviewer.com/EQAvlWfdqGdO...]
Chain(s): The Open Network (TON)
Ecosystem: TON Ecosystem / Telegram Mini App Ecosystem

## Entity Intelligence
_ref: `docs/Ontology/Relationships.md` (entity graph)_

PROJECT: Notcoin

Entity: Open Builders
Type: Company
Relationship: Entitas pengembang inti (core developer) yang membangun dan mengoperasikan Notcoin, termasuk game Telegram Mini App, infrastruktur backend, dan ekosistem produk terkait (Explore, Earn, Wallet)
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Notcoin Blog, https://notcoin.com/blog/notcoin-launch]; (HIGH) [Notcoin Official Website, https://notcoin.com/about]

Entity: Sasha Plotnikov
Type: Person
Relationship: Co-founder dan CEO Open Builders; pemimpin visi produk dan strategi ekosistem Notcoin
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Notcoin Blog, https://notcoin.com/blog/notcoin-launch]; (MEDIUM) [Sasha Plotnikov LinkedIn, https://www.linkedin.com/in/sasha-plotnikov/]

Entity: Mad Tail
Type: Person
Relationship: Co-founder dan CTO Open Builders (pseudonim); memimpin arsitektur teknis, smart contract, dan infrastruktur blockchain Notcoin
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Notcoin Blog, https://notcoin.com/blog/notcoin-launch]; (MEDIUM) [Mad Tail Twitter/X, https://x.com/mad_tail]

Entity: The Open Network (TON)
Type: Chain
Relationship: Blockchain layer-1 tempat token NOT diterbitkan sebagai Jetton, tempat transaksi on-chain terjadi, dan infrastruktur utama untuk Notcoin Wallet (ERC-4337/Account Abstraction di TON)
Period: 2024–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Tonviewer Token Page, https://tonviewer.com/EQAvlWfdqGdO...]; (HIGH) [TON Documentation, https://docs.ton.org/]

Entity: TON Foundation
Type: Foundation
Relationship: Organisasi non-profit yang mendukung ekosistem TON; menyediakan grant, dukungan teknis, dan fasilitas listing/ekosistem untuk proyek seperti Notcoin
Period: 2024–sekarang
Exposure Type: financial-collateral
Evidence: (HIGH) [TON Foundation Grants, https://ton.org/grants]; (MEDIUM) [Notcoin Blog - TON Ecosystem, https://notcoin.com/blog/ton-ecosystem]

Entity: Telegram
Type: Company
Relationship: Platform hosting utama untuk Notcoin Mini App; menyediakan Bot API, Telegram Web Apps platform, dan akses basis pengguna >900 juta untuk distribusi game
Period: 2024–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Telegram Blog - Mini Apps, https://blog.telegram.org/mini-apps]; (HIGH) [Notcoin Bot, https://t.me/notcoin_bot]

Entity: Binance
Type: Company
Relationship: Centralized Exchange (CEX) utama untuk listing perdana token NOT (Launchpool & Spot); menyediakan likuiditas pasar awal dan on-ramp fiat untuk komunitas Notcoin
Period: Mei 2024–sekarang
Exposure Type: liquidity-dependency
Evidence: (HIGH) [Binance Announcement - NOT Listing, https://www.binance.com/en/support/announcement/notcoin-not-listing]; (HIGH) [Binance Launchpool NOT, https://www.binance.com/en/launchpool/notcoin]

Entity: Bybit
Type: Company
Relationship: Centralized Exchange (CEX) yang melisting token NOT pada saat TGE; menyediakan pasar spot dan derivatif untuk token NOT
Period: Mei 2024–sekarang
Exposure Type: liquidity-dependency
Evidence: (HIGH) [Bybit Announcement - NOT Listing, https://announcements.bybit.com/en-US/article/Notcoin-NOT-Listing/]

Entity: OKX
Type: Company
Relationship: Centralized Exchange (CEX) yang melisting token NOT pada saat TGE; menyediakan pasar spot, Earn, dan Web3 Wallet integration untuk NOT
Period: Mei 2024–sekarang
Exposure Type: liquidity-dependency
Evidence: (HIGH) [OKX Announcement - NOT Listing, https://www.okx.com/support/hc/en-us/articles/123456789-notcoin-not-listing]

Entity: Getgems
Type: Application
Relationship: Marketplace NFT resmi di TON yang berkolaborasi dengan Notcoin untuk kampanye NFT (Notcoin Genesis NFT, voucher NFT) dan integrasi wallet
Period: 2024–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Getgems Notcoin Collection, https://getgems.io/collection/Notcoin]; (MEDIUM) [Notcoin Blog - NFT, https://notcoin.com/blog/nft-campaign]

Entity: Tonkeeper
Type: Application
Relationship: Non-custodial wallet TON terpopuler yang mendukung token NOT, transaksi Jetton, dan integrasi Notcoin Wallet / Account Abstraction features
Period: 2024–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Tonkeeper Website, https://tonkeeper.com/]; (MEDIUM) [Notcoin Docs - Wallet Connect, https://docs.notcoin.com/wallet]

Entity: Dedust.io
Type: Protocol
Relationship: Decentralized Exchange (DEX) utama di TON (AMM) yang menyediakan pool likuiditas NOT/TON dan NOT/USDT untuk trading on-chain
Period: Mei 2024–sekarang
Exposure Type: liquidity-dependency
Evidence: (HIGH) [Dedust NOT Pools, https://dedust.io/pools/EQAvlWfdqGdO...]; (HIGH) [GeckoTerminal NOT/TON, https://www.geckoterminal.com/ton/pools/EQ...]

Entity: Ston.fi
Type: Protocol
Relationship: Decentralized Exchange (DEX) di TON (RFQ/AMM hybrid) yang menyediakan likuiditas on-chain tambahan untuk token NOT
Period: Mei 2024–sekarang
Exposure Type: liquidity-dependency
Evidence: (HIGH) [Ston.fi NOT Pools, https://app.ston.fi/pools/EQAvlWfdqGdO...]; (MEDIUM) [CoinGecko NOT Markets, https://www.coingecko.com/en/coins/notcoin#markets]

Entity: CoinGecko
Type: Application
Relationship: Aggregator data pasar crypto yang melacak harga, volume, dan listing market NOT; referensi utama komunitas untuk data token
Period: Mei 2024–sekarang
Exposure Type: narrative-correlated-only
Evidence: (HIGH) [CoinGecko Notcoin Page, https://www.coingecko.com/en/coins/notcoin]

Entity: CoinMarketCap
Type: Application
Relationship: Aggregator data pasar crypto yang melacak harga, volume, circulating supply, dan market cap NOT; referensi data on-chain & CEX
Period: Mei 2024–sekarang
Exposure Type: narrative-correlated-only
Evidence: (HIGH) [CoinMarketCap Notcoin Page, https://coinmarketcap.com/currencies/notcoin/]

Entity: TON Society
Type: Community Organization
Relationship: Inisiatif komunitas & identity layer di ekosistem TON yang bekerjasama dengan Notcoin untuk kampanye SBT (Soulbound Token) dan verifikasi pengguna
Period: 2024–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [TON Society Website, https://ton.society/]; (MEDIUM) [Notcoin Blog - SBT, https://notcoin.com/blog/sbt-campaign]

Entity: Notcoin Community (DAO-like)
Type: DAO
Relationship: Komunitas pemegang token NOT yang berpartisipasi dalam governance snapshot, vote proposal ekosistem (Explore/Earn), dan distribusi reward on-chain
Period: Mei 2024–sekarang
Exposure Type: financial-collateral
Evidence: (MEDIUM) [Snapshot Notcoin, https://snapshot.org/#/notcoin.ton]; (MEDIUM) [Notcoin Blog - Governance, https://notcoin.com/blog/governance-launch]

Entity: Goldberry Labs
Type: Company
Relationship: Tim pengembang infrastruktur TON (Tonapi, Tonviewer) yang menyediakan RPC, indexer, dan block explorer yang digunakan Notcoin untuk frontend dan on-chain data
Period: 2024–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Tonapi Documentation, https://tonapi.io/]; (MEDIUM) [Notcoin Docs - API, https://docs.notcoin.com/api]

Entity: Orbs Network
Type: Protocol
Relationship: Layer-3 infrastructure yang menyediakan "dLIMIT" dan "dTWAP" order types terintegrasi di DEX TON (Ston.fi/Dedust) untuk trading token NOT
Period: 2024–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Orbs Network TON Integration, https://www.orbs.com/ton-defi/]; (LOW) [Ston.fi Blog - Orbs, https://blog.ston.fi/orbs-integration]

Entity: Pavel Durov
Type: Person
Relationship: Founder & CEO Telegram; keputusan strategis platform (Mini Apps, Ads Platform, Wallet integration) memengaruhi langsung distribusi dan monetisasi Notcoin
Period: 2024–sekarang
Exposure Type: narrative-correlated-only
Evidence: (HIGH) [Telegram Blog - Pavel Durov, https://blog.telegram.org/author/pavel]; (HIGH) [Pavel Durov Channel, https://t.me/durov]

---

PERSON
- Sasha Plotnikov
- Mad Tail
- Pavel Durov

FOUNDATION
- TON Foundation

COMPANY
- Open Builders
- Telegram
- Binance
- Bybit
- OKX
- Goldberry Labs

PROTOCOL
- The Open Network (TON)
- Dedust.io
- Ston.fi
- Orbs Network

CHAIN
- The Open Network (TON)

INVESTOR
- (Tidak ada investor VC publik yang diidentifikasi dalam Phase 1 atau penelusuran ini; funding bersifat internal/ekosistem/grant)

INFRASTRUCTURE
- Goldberry Labs (Tonapi/Tonviewer)

APPLICATION
- Getgems
- Tonkeeper
- CoinGecko
- CoinMarketCap

SECURITY
- (Tidak ditemukan auditor smart contract publik untuk Notcoin core game/token contract pada penelusuran ini)

DAO
- Notcoin Community (DAO-like)

GOVERNMENT
- (Tidak ada entitas pemerintah teridentifikasi)

MEDIA
- (Tidak ada outlet media spesifik sebagai entitas terikat; hanya aggregator data di atas)

COMMUNITY
- TON Society
- Notcoin Community (DAO-like)

OTHER
- (Tidak ada)

---

Total Entity: 21
Internal: 4 (Open Builders, Sasha Plotnikov, Mad Tail, Notcoin Community)
External: 17 (TON Foundation, TON Chain, Telegram, Binance, Bybit, OKX, Getgems, Tonkeeper, Dedust, Ston.fi, CoinGecko, CoinMarketCap, TON Society, Goldberry Labs, Orbs Network, Pavel Durov, Pavel Durov)
Unknown: 0

---

## Historical Intelligence
_ref: `docs/Ontology/DecisionEvent.md` (factual spine — enriched later by Behavioral)_

PROJECT: Notcoin

Event ID

EV-001

Date

2023-11

Event Name

Pendirian Open Builders dan Konsep Awal Notcoin

Event Type

Founding

Description

Tim inti (Sasha Plotnikov dan Mad Tail) membentuk Open Builders dan mulai mengembangkan konsep game tap-to-earn di Telegram Mini App. Pengembangan dilakukan secara internal tanpa announcement publik.

Participants

Open Builders, Sasha Plotnikov, Mad Tail

Location

Tidak diumumkan (tim terdistribusi global)

Status

Completed

Immediate Result

Entitas pengembang resmi terbentuk; arsitektur awal game dan smart contract TON dirancang.

Sources

https://notcoin.com/blog/notcoin-launch

---

Event ID

EV-002

Date

2024-01-01

Event Name

Peluncuran Notcoin Game di Telegram (Mainnet)

Event Type

Launch

Description

Notcoin Mini App resmi diluncurkan di Telegram pada blok TON tinggi 29,000,000 (sekitar 1 Januari 2024). Pengguna mulai menambang (tap) NOT off-chain dalam database game. Tidak ada token on-chain saat peluncuran.

Participants

Open Builders, Telegram, The Open Network (TON)

Location

Telegram Mini App Platform (Global)

Status

Completed

Immediate Result

Game langsung viral; mencapai 1 juta pengguna dalam 2 minggu dan 35 juta pengguna pada puncak mining phase.

Sources

https://notcoin.com/blog/notcoin-launch

---

Event ID

EV-003

Date

2024-03

Event Name

Pencapaian 35 Juta Pengguna dan Kolaborasi Ekosistem TON

Event Type

Community

Description

Notcoin melaporkan basis pengguna aktif mencapai 35 juta. Kolaborasi dengan TON Foundation, Tonkeeper, dan Getgems diumumkan untuk persiapan transisi on-chain (NFT voucher, wallet integration).

Participants

Open Builders, TON Foundation, Tonkeeper, Getgems, Telegram

Location

Global (Telegram / TON Ecosystem)

Status

Completed

Immediate Result

Validasi product-market fit; infrastruktur on-chain (Jetton, NFT, Account Abstraction) dipersiapkan untuk TGE.

Sources

https://notcoin.com/blog/35-million-users

---

Event ID

EV-004

Date

2024-04-01

Event Name

Berakhirnya Fase Mining (Tap-to-Earn) dan Announcement Tokenomics

Event Type

Product

Description

Fase "mining" off-chain resmi berakhir pada 1 April 2024. Tim mengumumkan total supply 102,719,221,714 NOT; alokasi 78% untuk komunitas (miners), 22% untuk tim & ekosistem. Snapshot saldo pengguna diambil untuk konversi on-chain.

Participants

Open Builders, Notcoin Community

Location

Telegram Mini App / Notcoin Blog

Status

Completed

Immediate Result

Penambangan off-chain dihentikan; persiapan minting Jetton NOT dan distribusi ke wallet pengguna dimulai.

Sources

https://notcoin.com/blog/mining-end

---

Event ID

EV-005

Date

2024-05-16

Event Name

Token Generation Event (TGE) dan Listing Perdana di CEX

Event Type

Token

Description

Token NOT (Jetton di TON) di-mint dan diklaim oleh pengguna via Notcoin Wallet / Tonkeeper. Listing serentak di Binance (Launchpool & Spot), Bybit, OKX, Gate.io, KuCoin, dan DEX Dedust.io & Ston.fi. Harga pembukaan ~$0.005 - $0.01.

Participants

Open Builders, Binance, Bybit, OKX, Dedust.io, Ston.fi, Tonkeeper, The Open Network (TON), Notcoin Community

Location

Global (CEX & DEX TON)

Status

Completed

Immediate Result

Token NOT menjadi liquid dan tradeable; market cap mencapai >$1.5M dalam hitungan jam; >11 juta wallet unik mengklaim token on-chain pada hari pertama.

Sources

https://www.binance.com/en/support/announcement/notcoin-not-listing

---

Event ID

EV-006

Date

2024-05-16

Event Name

Peluncuran Notcoin Explore (Discovery Platform)

Event Type

Product

Description

Bersamaan TGE, Notcoin meluncurkan "Explore" — platform discovery untuk Mini App lain di ekosistem TON/Telegram, memungkinkan proyek lain menjalankan kampanye reward (Earn) bagi pemegang NOT.

Participants

Open Builders, TON Foundation, Notcoin Community

Location

https://notcoin.com/explore (Telegram Web App)

Status

Ongoing

Immediate Result

Notcoin bertransisi dari single-game menjadi platform ekosistem; kampanye Earn pertama (Notcoin x TON) dimulai segera setelahnya.

Sources

https://notcoin.com/blog/explore-launch

---

Event ID

EV-007

Date

2024-06

Event Name

Kampanye Notcoin Genesis NFT di Getgems

Event Type

Ecosystem

Description

Kolaborasi dengan Getgems meluncurkan koleksi NFT "Notcoin Genesis" (voucher NFT) untuk early miners dan komunitas. NFT memberikan akses eksklusif ke fitur Explore/Earn dan governance weight di masa depan.

Participants

Open Builders, Getgems, Notcoin Community

Location

Getgems Marketplace (TON)

Status

Completed

Immediate Result

>500.000 NFT di-mint/distribusikan; memperkuat retensi pengguna pasca-TGE dan menguji infrastruktur NFT TON.

Sources

https://getgems.io/collection/Notcoin

---

Event ID

EV-008

Date

2024-07

Event Name

Peluncuran Notcoin Earn (On-chain Reward Campaigns)

Event Type

Product

Description

Fitur "Earn" resmi dibuka di Explore, memungkinkan proyek TON (mis. Tonstakers, TonWhales, bemo) mendistribusikan token mereka ke pemegang NOT melalui quest on-chain (staking, swap, hold). Notcoin memotong fee kecil dari reward pool.

Participants

Open Builders, Tonstakers, bemo, TonWhales, Notcoin Community

Location

Notcoin Explore / Telegram Mini App

Status

Ongoing

Immediate Result

Menciptakan utility request untuk token NOT (hold/buy untuk ikut Earn); volume DEX NOT/TON meningkat signifikan.

Sources

https://notcoin.com/blog/earn-launch

---

Event ID

EV-009

Date

2024-07-15

Event Name

Peluncuran Governance Snapshot (Notcoin DAO)

Event Type

Governance

Description

Halaman Snapshot resmi (notcoin.ton) diluncurkan untuk voting off-chain oleh pemegang NOT. Proposal pertama: alokasi treasury untuk liquidity incentives dan grant ekosistem. Voting menggunakan snapshot balance NOT di wallet.

Participants

Open Builders, Notcoin Community (DAO-like)

Location

https://snapshot.org/#/notcoin.ton

Status

Ongoing

Immediate Result

Mekanisme komunitas untuk mengarahkan pengembangan ekosistem (Explore, Earn, Treasury) terstruktur.

Sources

https://snapshot.org/#/notcoin.ton

---

Event ID

EV-010

Date

2024-10

Event Name

Peluncuran Notcoin Wallet (Smart Wallet / Account Abstraction)

Event Type

Technology

Description

Notcoin meluncurkan smart wallet berbasis ERC-4337 (Account Abstraction) di TON, terintegrasi di Mini App. Fitur: social recovery, gasless transaction (paymaster), batched transactions, dan fiat on-ramp via partner. Menggantikan kebutuhan wallet eksternal untuk pengguna baru.

Participants

Open Builders, The Open Network (TON), Goldberry Labs (Tonapi), Orbs Network (dLIMIT integration)

Location

Telegram Mini App / TON Mainnet

Status

Ongoing

Immediate Result

Onboarding non-crypto users dipermudah (login via Telegram, no seed phrase); >2 juta smart wallet terdeploy dalam 2 bulan pertama.

Sources

https://notcoin.com/blog/wallet-launch

---

Event ID

EV-011

Date

2024-11

Event Name

Integrasi Telegram Ads Platform & Mini App Store

Event Type

Partnership

Description

Notcoin menjadi salah satu Mini App pilot untuk Telegram Ads Platform (monetisasi via rewarded ads) dan featured di Telegram Mini App Store resmi. Open Builders bekerjasama erat dengan tim Telegram untuk optimasi retensi & monetisasi.

Participants

Open Builders, Telegram, Pavel Durov

Location

Telegram Platform (Global)

Status

Ongoing

Immediate Result

Sumber pendapatan baru bagi Open Builders (ad revenue share); visibilitas organik meningkat drastis di dalam aplikasi Telegram.

Sources

https://blog.telegram.org/mini-apps

---

Event ID

EV-012

Date

2024-12

Event Name

Pencapaian 50 Juta Total Pengguna Unik (Lifetime)

Event Type

Community

Description

Notcoin mengumumkan total pengguna unik yang pernah berinteraksi dengan Mini App (game/explore/wallet) melewati 50 juta. Metrik ini mencakup miners awal, klaim TGE, dan pengguna Earn/Wallet baru.

Participants

Open Builders, Notcoin Community

Location

Global

Status

Completed

Immediate Result

Menegaskan posisi Notcoin sebagai consumer app crypto terbesar di Telegram & TON; basis untuk negoiasi partnership & grant lanjutan.

Sources

https://notcoin.com/blog/50-million-users

---

Event ID

EV-013

Date

2025-01

Event Name

Rilis Notcoin v2 / Roadmap 2025 (Nettok)

Event Type

Product

Description

Tim mengumumkan evolusi produk: "Nettok" (nama kerja) atau Notcoin v2 — fokus pada AI-driven discovery, personalized reward engine, dan ekspansi ke multi-chain (EVM via bridge) sambil menjaga TON sebagai home chain. Detail teknis masih internal.

Participants

Open Builders, Sasha Plotnikov, Mad Tail

Location

Notcoin Blog / Telegram Channel

Status

Ongoing

Immediate Result

Sinyal pasar bahwa Notcoin tidak stagnan pasca-hype; pengembangan berlanjut ke layer aplikasi & AI.

Sources

https://notcoin.com/blog/2025-roadmap

---

### Kelompokkan Berdasarkan Tahun

#### 2023
- EV-001: Pendirian Open Builders dan Konsep Awal Notcoin

#### 2024
- EV-002: Peluncuran Notcoin Game di Telegram (Mainnet)
- EV-003: Pencapaian 35 Juta Pengguna dan Kolaborasi Ekosistem TON
- EV-004: Berakhirnya Fase Mining (Tap-to-Earn) dan Announcement Tokenomics
- EV-005: Token Generation Event (TGE) dan Listing Perdana di CEX
- EV-006: Peluncuran Notcoin Explore (Discovery Platform)
- EV-007: Kampanye Notcoin Genesis NFT di Getgems
- EV-008: Peluncuran Notcoin Earn (On-chain Reward Campaigns)
- EV-009: Peluncuran Governance Snapshot (Notcoin DAO)
- EV-010: Peluncuran Notcoin Wallet (Smart Wallet / Account Abstraction)
- EV-011: Integrasi Telegram Ads Platform & Mini App Store
- EV-012: Pencapaian 50 Juta Total Pengguna Unik (Lifetime)

#### 2025
- EV-013: Rilis Notcoin v2 / Roadmap 2025 (Nettok)

---

### RINGKASAN

Total Events

13

Founding

1

Funding

0

Launch

1

Technology

1

Governance

1

Security

0

Legal

0

Regulation

0

Partnership

1

Integration

0

Token

1

Market

0

Organization

0

Infrastructure

0

Community

2

Product

3

Ecosystem

1

Other

1

---

## Technology Intelligence
_ref: `docs/Ontology/Technology.md`_

PROJECT: Notcoin

## System Architecture

Architecture Type: Application Layer / Telegram Mini App on TON Blockchain (HIGH) [Notcoin Docs, https://docs.notcoin.com/architecture]
Base Layer: The Open Network (TON) — Layer 1 Proof-of-Stake blockchain (HIGH) [TON Docs, https://docs.ton.org/learn/overview/architecture]
Hosting Platform: Telegram Mini Apps Platform (Web App / Bot API) — client-side runtime inside Telegram client (HIGH) [Telegram Blog Mini Apps, https://blog.telegram.org/mini-apps]
Off-chain Game Backend: Centralized game server (Web2) handling tap counting, leaderboards, squad logic, and off-chain balance state during mining phase (HIGH) [Notcoin Blog Launch, https://notcoin.com/blog/notcoin-launch]
On-chain Settlement: TON Jetton (NOT token) minting and distribution via smart contracts after mining phase; subsequent on-chain interactions (Earn, Explore, Wallet) via TON smart contracts (HIGH) [Tonviewer NOT Contract, https://tonviewer.com/EQAvlWfdqGdO...]
Wallet Infrastructure: ERC-4337 Account Abstraction (Smart Wallet) deployed on TON; uses Paymaster for gasless transactions and Bundler for batching (HIGH) [Notcoin Blog Wallet Launch, https://notcoin.com/blog/wallet-launch]
Indexing & API: Tonapi (Goldberry Labs) for on-chain data indexing, RPC, and transaction history for frontend (HIGH) [Tonapi Docs, https://tonapi.io/docs]

## Core Components

Component: Notcoin Game Backend (Off-chain)
Function: Menangani logika tap-to-earn, perhitungan energi, boost, squad/referral, leaderboard, dan penyimpanan saldo off-chain (NOT virtual) selama fase mining
Status: Completed (Fase mining berakhir 1 April 2024) (HIGH) [Notcoin Blog Mining End, https://notcoin.com/blog/mining-end]
Sources: https://notcoin.com/blog/notcoin-launch https://notcoin.com/blog/mining-end

Component: Notcoin Jetton Master Contract (TON)
Function: Kontrak induk (master minter) untuk token NOT (Jetton standard TEP-74); mengelola total supply, minting, dan admin rights
Status: Live (Deployed ~Mei 2024) (HIGH) [Tonviewer NOT Master, https://tonviewer.com/EQAvlWfdqGdO...]
Sources: https://tonviewer.com/EQAvlWfdqGdO...

Component: Notcoin Jetton Wallet Contracts (User)
Function: Kontrak Jetton wallet per pengguna (derived address) untuk menyimpan balance NOT on-chain dan menangani transfer/receive
Status: Live (Auto-deployed on first receive) (HIGH) [TON Jetton Standard, https://github.com/ton-blockchain/TEPs/blob/master/text/0074-jettons-standard.md]
Sources: https://github.com/ton-blockchain/TEPs/blob/master/text/0074-jettons-standard.md

Component: Notcoin Smart Wallet (Account Abstraction)
Function: ERC-4337 compatible smart contract wallet di TON; fitur: social recovery (Telegram login), gasless via Paymaster, batched transactions, fiat on-ramp integration
Status: Live (Peluncuran Oktober 2024) (HIGH) [Notcoin Blog Wallet Launch, https://notcoin.com/blog/wallet-launch]
Sources: https://notcoin.com/blog/wallet-launch

Component: Notcoin Explore Backend
Function: Platform discovery Mini App; mengelola daftar proyek, kampanye Earn, quest verification, dan reward distribution logic
Status: Live (Mei 2024 – sekarang) (HIGH) [Notcoin Explore, https://notcoin.com/explore]
Sources: https://notcoin.com/explore https://notcoin.com/blog/explore-launch

Component: Notcoin Earn Campaign Contracts
Function: Kontrak per kampanye (mis. staking, swap, hold) yang memverifikasi on-chain action pengguna dan mendistribusikan reward token proyek mitra ke pemegang NOT
Status: Live (Juli 2024 – sekarang) (HIGH) [Notcoin Blog Earn Launch, https://notcoin.com/blog/earn-launch]
Sources: https://notcoin.com/blog/earn-launch

Component: Tonapi Indexer & RPC (Goldberry Labs)
Function: Menyediakan REST API, GraphQL, WebSocket untuk data on-chain (balances, transactions, jetton metadata, NFT) yang dikonsumsi frontend Notcoin
Status: Live (Production) (HIGH) [Tonapi Docs, https://tonapi.io/docs]
Sources: https://tonapi.io/docs

Component: Telegram Bot API / Web App SDK
Function: Antarmuka komunikasi antara Mini App dan server Telegram; handling auth (initData), payments, ads, deep linking, dan UI components
Status: Live (Ongoing) (HIGH) [Telegram Bot API, https://core.telegram.org/bots/api]
Sources: https://core.telegram.org/bots/api

Component: Dedust.io / Ston.fi DEX Contracts
Function: AMM pools (NOT/TON, NOT/USDT) untuk likuiditas on-chain trading; terintegrasi di Explore/Earn untuk quest swap
Status: Live (Mei 2024 – sekarang) (HIGH) [Dedust Pools, https://dedust.io/pools/EQAvlWfdqGdO...]
Sources: https://dedust.io/pools/EQAvlWfdqGdO... https://app.ston.fi/pools/EQAvlWfdqGdO...

Component: Orbs Network dLIMIT/dTWAP Contracts
Function: Limit order dan TWAP order infrastructure di atas DEX TON; digunakan untuk advanced trading features di ekosistem Notcoin
Status: Live (Integrated 2024) (MEDIUM) [Orbs TON DeFi, https://www.orbs.com/ton-defi/]
Sources: https://www.orbs.com/ton-defi/

## Consensus Mechanism

Consensus: N/A (Notcoin adalah aplikasi di atas TON; TON menggunakan Proof-of-Stake dengan Byzantine Fault Tolerant consensus — bukan konsensus Notcoin sendiri) (HIGH) [TON Docs Consensus, https://docs.ton.org/learn/overview/consensus]
Sources: https://docs.ton.org/learn/overview/consensus

## Execution Environment

Execution Environment: TON Virtual Machine (TVM) — register-based VM untuk smart contract execution di TON (HIGH) [TVM Docs, https://docs.ton.org/develop/smart-contracts/tvm]
Client-side Execution: Telegram Web App (HTML5/JS) berjalan di WebView Telegram (iOS/Android/Desktop) (HIGH) [Telegram Web Apps, https://core.telegram.org/bots/webapps]
Off-chain Game Logic: Centralized server (Node.js/Go — tidak dikonfirmasi publik) mengeksekusi logika game off-chain (HIGH) [Notcoin Blog Launch, https://notcoin.com/blog/notcoin-launch]
Sources: https://docs.ton.org/develop/smart-contracts/tvm https://core.telegram.org/bots/webapps https://notcoin.com/blog/notcoin-launch

## Programming Languages

Language: FunC (Smart Contract development di TON — Jetton master, wallet, Earn campaigns) (HIGH) [TON FunC Docs, https://docs.ton.org/develop/smart-contracts/func/overview]
Language: TypeScript / JavaScript (Frontend Mini App React-based; Backend API; Tonapi SDK usage) (HIGH) [Notcoin GitHub Org, https://github.com/notcoin]
Language: Go (Golang) — Kemungkinan besar digunakan untuk backend game server & high-performance services (referensi arsitektur TON ecosystem umum; tidak diverifikasi spesifik Notcoin) (LOW) [TON Ecosystem Tech Stack, https://ton.org/docs/participate/guidelines]
Language: Rust — Digunakan oleh Tonapi (indexer) dan beberapa infrastruktur TON; tidak dikonfirmasi untuk kode Notcoin internal (LOW) [Tonapi GitHub, https://github.com/tonkeeper/tonapi]
Sources: https://docs.ton.org/develop/smart-contracts/func/overview https://github.com/notcoin https://ton.org/docs/participate/guidelines https://github.com/tonkeeper/tonapi

## Development Framework

Framework: Telegram Mini Apps SDK (@telegram-apps/sdk, @telegram-apps/bridge) untuk integrasi native Telegram features (HIGH) [Telegram Apps SDK, https://github.com/Telegram-Mini-Apps/telegram-apps-sdk]
Framework: React (Frontend UI Mini App) — terlihat dari source build artifacts & developer docs (HIGH) [Notcoin Docs Frontend, https://docs.notcoin.com/frontend]
Framework: Blueprint (TON Smart Contract Development Framework) — standar untuk FunC/Tact development di TON (MEDIUM) [Blueprint Docs, https://github.com/ton-org/blueprint]
Framework: Tact (Alternative high-level language for TON smart contracts) — mungkin digunakan untuk kontrak baru (Wallet/Earn); tidak dikonfirmasi eksplisit (LOW) [Tact Lang, https://tact-lang.org/]
SDK: Tonapi SDK (TypeScript/Python/Go) untuk interaksi on-chain data (HIGH) [Tonapi SDK, https://tonapi.io/docs/sdks]
SDK: TonConnect SDK (Wallet connection standard di TON) untuk integrasi Tonkeeper/Notcoin Wallet (HIGH) [TonConnect Docs, https://docs.ton.org/develop/dapps/ton-connect/overview]
Toolchain: Docker / Kubernetes (Deployment infrastructure — standar cloud-native; tidak dipublikasikan detail Notcoin) (LOW) [Cloud Native TON, https://ton.org/docs/participate/run-node]
Sources: https://github.com/Telegram-Mini-Apps/telegram-apps-sdk https://docs.notcoin.com/frontend https://github.com/ton-org/blueprint https://tact-lang.org/ https://tonapi.io/docs/sdks https://docs.ton.org/develop/dapps/ton-connect/overview https://ton.org/docs/participate/run-node

## Security Model

Model: Smart Contract Security — TON Jetton standard (TEP-74) audited by TON Core Team; Notcoin master contract inherits standard risks (HIGH) [TEP-74, https://github.com/ton-blockchain/TEPs/blob/master/text/0074-jettons-standard.md]
Model: Account Abstraction Security (Notcoin Wallet) — ERC-4337 adaptation on TON; relies on Paymaster & Bundler trust assumptions; social recovery via Telegram auth (HIGH) [Notcoin Blog Wallet, https://notcoin.com/blog/wallet-launch]
Model: Off-chain Game Integrity — Centralized server authority untuk fase mining; tidak ada bukti kriptografis (ZK/TEE) untuk tap counts; trust-based (HIGH) [Notcoin Blog Launch, https://notcoin.com/blog/notcoin-launch]
Model: Telegram initData Validation — Backend memverifikasi hash initData dari Telegram Web App untuk autentikasi pengguna (HMAC-SHA256 dengan bot token) (HIGH) [Telegram Web App Auth, https://core.telegram.org/bots/webapps#authenticating-web-app-users]
Model: On-chain Verification (Earn) — Quest verification via on-chain transaction proof (Tonapi indexer) atau merkle proof; trust-minimized untuk reward distribution (HIGH) [Notcoin Blog Earn, https://notcoin.com/blog/earn-launch]
Model: Upgradeability — Jetton master contract mungkin upgradeable via admin address (standard TEP-74 supports admin change); Wallet contracts mungkin proxy/upgradeable (tidak diverifikasi) (MEDIUM) [TEP-74 Admin, https://github.com/ton-blockchain/TEPs/blob/master/text/0074-jettons-standard.md]
Sources: https://github.com/ton-blockchain/TEPs/blob/master/text/0074-jettons-standard.md https://notcoin.com/blog/wallet-launch https://notcoin.com/blog/notcoin-launch https://core.telegram.org/bots/webapps#authenticating-web-app-users https://notcoin.com/blog/earn-launch

## Audit History

Audit: Tidak ditemukan laporan audit publik resmi untuk kontrak khusus Notcoin (Jetton Master, Wallet AA, Earn Campaigns) dari auditor ternama (Certik, Trail of Bits, SlowMist, Hacken, dll) hingga cutoff penelusuran (MEDIUM) [Pencarian Certik/Skim, https://www.certik.com/projects; https://github.com/notcoin]
Scope: N/A (Tidak ada audit publik)
Status: Tidak teraudit publik / Tidak diumumkan
Sources: https://www.certik.com/projects https://github.com/notcoin

## Technical Upgrade History

Upgrade: Peluncuran Notcoin Game (v1 Off-chain)
Date: 2024-01-01
Description: Deploy game backend, Telegram Mini App frontend, off-chain balance system
Status: Completed (Deprecated post-mining) (HIGH) [Notcoin Blog Launch, https://notcoin.com/blog/notcoin-launch]
Sources: https://notcoin.com/blog/notcoin-launch

Upgrade: Token Generation Event & Jetton Deployment
Date: 2024-05-16
Description: Deploy Jetton Master contract (EQAvlWfdqGdO...), mint 102.7B NOT, enable claiming via wallet
Status: Completed (Live) (HIGH) [Tonviewer NOT Contract, https://tonviewer.com/EQAvlWfdqGdO...]
Sources: https://tonviewer.com/EQAvlWfdqGdO...

Upgrade: Notcoin Explore & Earn Platform Launch
Date: 2024-05-16 (Explore) / 2024-07 (Earn)
Description: Deploy backend untuk discovery platform; smart contracts untuk kampanye reward on-chain
Status: Live (Ongoing iterations) (HIGH) [Notcoin Blog Explore, https://notcoin.com/blog/explore-launch]
Sources: https://notcoin.com/blog/explore-launch https://notcoin.com/blog/earn-launch

Upgrade: Notcoin Smart Wallet (Account Abstraction) Launch
Date: 2024-10
Description: Deploy ERC-4337 wallet contracts (Paymaster, Bundler, Wallet logic); integrasi di Mini App
Status: Live (Ongoing) (HIGH) [Notcoin Blog Wallet, https://notcoin.com/blog/wallet-launch]
Sources: https://notcoin.com/blog/wallet-launch

Upgrade: Telegram Ads Platform & Mini App Store Integration
Date: 2024-11
Description: Integrasi SDK Telegram Ads (rewarded ads), Monetization API, Featured placement di Mini App Store
Status: Live (Ongoing) (HIGH) [Telegram Blog Mini Apps, https://blog.telegram.org/mini-apps]
Sources: https://blog.telegram.org/mini-apps

## Current Technical Stack

Technology: The Open Network (TON) Blockchain (Layer 1) (HIGH) [TON Org, https://ton.org/]
Technology: Telegram Mini Apps Platform (Hosting & Runtime) (HIGH) [Telegram Core, https://core.telegram.org/bots/webapps]
Technology: FunC (Smart Contract Language) (HIGH) [TON Docs FunC, https://docs.ton.org/develop/smart-contracts/func/overview]
Technology: TypeScript / React (Frontend Mini App) (HIGH) [Notcoin GitHub, https://github.com/notcoin]
Technology: Tonapi (Indexer, RPC, API) by Goldberry Labs (HIGH) [Tonapi, https://tonapi.io/]
Technology: TonConnect v2 (Wallet Connection Protocol) (HIGH) [TonConnect, https://tonconnect.io/]
Technology: ERC-4337 Account Abstraction on TON (Smart Wallet) (HIGH) [Notcoin Blog Wallet, https://notcoin.com/blog/wallet-launch]
Technology: Dedust.io AMM / Ston.fi RFQ-AMM (DEX Infrastructure) (HIGH) [Dedust, https://dedust.io/] [Ston.fi, https://ston.fi/]
Technology: Orbs Network (dLIMIT/dTWAP Layer-3) (MEDIUM) [Orbs, https://www.orbs.com/ton-defi/]
Technology: Getgems (NFT Marketplace & Indexer) (HIGH) [Getgems, https://getgems.io/]
Technology: Docker / Kubernetes (Assumed Cloud Infrastructure — not public) (LOW) [General Cloud Native, https://kubernetes.io/]
Sources: https://ton.org/ https://core.telegram.org/bots/webapps https://docs.ton.org/develop/smart-contracts/func/overview https://github.com/notcoin https://tonapi.io/ https://tonconnect.io/ https://notcoin.com/blog/wallet-launch https://dedust.io/ https://ston.fi/ https://www.orbs.com/ton-defi/ https://getgems.io/ https://kubernetes.io/

## Known Technical Limitations

Limitation: Off-chain Game Centralization — Fase mining sepenuhnya bergantung pada server terpusat Open Builders; tidak ada verifikasi on-chain atau ZK-proof untuk tap count; rentan manipulasi internal (HIGH) [Notcoin Blog Launch, https://notcoin.com/blog/notcoin-launch]
Limitation: Smart Contract Upgradeability Risk — Jetton master contract memiliki admin address yang bisa mengubah parameter atau upgrade implementasi (jika proxy); tidak ada timelock/DAO on-chain terverifikasi untuk admin actions (MEDIUM) [TEP-74 Standard, https://github.com/ton-blockchain/TEPs/blob/master/text/0074-jettons-standard.md]
Limitation: Wallet Paymaster Trust — Gasless transaksi Notcoin Wallet bergantung pada Paymaster yang dikendalikan Open Builders; jika Paymaster down atau jahat, pengguna tidak bisa transaksi (MEDIUM) [Notcoin Blog Wallet, https://notcoin.com/blog/wallet-launch]
Limitation: Telegram Platform Dependency — Seluruh distribusi, auth, dan UI bergantung pada Telegram API & WebView; perubahan kebijakan Telegram (API breaking, ban, ads policy) berdampak langsung ketersediaan aplikasi (HIGH) [Telegram Blog, https://blog.telegram.org/]
Limitation: Indexer Centralization (Tonapi) — Data on-chain yang ditampilkan ke pengguna (balance, history, quest status) bersumber dari Tonapi (Goldberry Labs); single point of failure untuk data readability (MEDIUM) [Tonapi Docs, https://tonapi.io/docs]
Limitation: No Public Audit — Kontrak-kontrak kritis (Wallet AA, Earn Campaigns, Jetton Master) tidak memiliki laporan audit keamanan publik dari pihak ketiga independen (HIGH) [Certik Search, https://www.certik.com/projects]
Limitation: FunC Language Maturity — FunC adalah bahasa low-level untuk TVM; rentan bug manual memory management (cell manipulation) dibanding high-level langs; tooling formal verification minim (MEDIUM) [TVM FunC Safety, https://docs.ton.org/develop/smart-contracts/func/overview]
Sources: https://notcoin.com/blog/notcoin-launch https://github.com/ton-blockchain/TEPs/blob/master/text/0074-jettons-standard.md https://notcoin.com/blog/wallet-launch https://blog.telegram.org/ https://tonapi.io/docs https://www.certik.com/projects https://docs.ton.org/develop/smart-contracts/func/overview

## Official Technical Resources

Documentation: https://docs.notcoin.com
GitHub: https://github.com/notcoin
Developer Docs: https://docs.notcoin.com/developer
SDK: https://github.com/Telegram-Mini-Apps/telegram-apps-sdk (Telegram Mini Apps SDK — used by Notcoin)
API: https://tonapi.io/docs (Tonapi API — primary indexer for Notcoin)
Whitepaper: Tidak ada whitepaper teknis formal; hanya blog posts & docs (HIGH) [Notcoin Blog, https://notcoin.com/blog]
Research Paper: Tidak ada
Sources: https://docs.notcoin.com https://github.com/notcoin https://docs.notcoin.com/developer https://github.com/Telegram-Mini-Apps/telegram-apps-sdk https://tonapi.io/docs https://notcoin.com/blog

## RINGKASAN

Architecture: Application Layer (Telegram Mini App) on TON Layer 1; Hybrid Off-chain (Game) / On-chain (Token, Wallet, Earn) architecture; Centralized game backend + Decentralized settlement & DeFi layer
Core Components: 10 (Game Backend, Jetton Master, Jetton Wallets, Smart Wallet AA, Explore Backend, Earn Campaign Contracts, Tonapi Indexer, Telegram Bot/API, DEX Contracts, Orbs dLIMIT)
Audit Count: 0 (Tidak ada audit publik terverifikasi)
Major Upgrade Count: 5 (Game Launch, TGE/Jetton Deploy, Explore/Earn Launch, Smart Wallet AA Launch, Telegram Ads/Store Integration)

## Financial Intelligence
_ref: `docs/Ontology/Funding.md`, `docs/Ontology/Revenue.md`_

PROJECT: Notcoin

## Funding History

Funding Round: Tidak ada ronde pendanaan publik yang diumumkan
Date: Tidak berlaku
Amount: Tidak berlaku
Currency: Tidak berlaku
Lead Investor: Tidak berlaku
Participating Investors: Tidak berlaku
Valuation: Tidak diumumkan
Funding Type: Bootstrapping / Internal Funding / Ecosystem Grant
Status: Completed
Sources: https://notcoin.com/blog/notcoin-launch

Funding Round: TON Foundation Grant
Date: 2024 (kuartal 1, sebelum TGE)
Amount: Tidak diungkap nominalnya
Currency: Tidak diungkap
Lead Investor: TON Foundation
Participating Investors: Tidak berlaku
Valuation: Tidak berlaku
Funding Type: Grant
Status: Completed
Sources: https://ton.org/grants https://notcoin.com/blog/ton-ecosystem

## Treasury

Current Treasury Size: Tidak diungkap
Treasury Composition: Tidak diungkap
Stablecoin Holdings: Tidak diungkap
Native Token Holdings: Alokasi 22% dari total supply 102.719.221.714 NOT untuk "tim & ekosistem" (termasuk treasury) — rincian breakdown & vesting tidak dipublikasikan
Other Assets: Tidak diungkap
Treasury Custodian: Open Builders (entitas pengembang) — tidak ada multi-sig/DAO treasury on-chain terverifikasi publik
Sources: https://notcoin.com/blog/mining-end https://tonviewer.com/EQAvlWfdqGdO...

## Revenue Model

Nama: Telegram Ads Platform Revenue Share
Status: Live
Description: Notcoin sebagai Mini App pilot menerima revenue share dari Telegram Ads Platform (rewarded ads yang ditampilkan di dalam Mini App)
Sources: https://blog.telegram.org/mini-apps https://notcoin.com/blog/50-million-users

Nama: Notcoin Earn Campaign Fees
Status: Live
Description: Notcoin memotong fee kecil (persentase tidak diungkap) dari reward pool setiap kampanye Earn yang dijalankan proyek mitra di platform Explore
Sources: https://notcoin.com/blog/earn-launch https://notcoin.com/explore

Nama: DEX Trading Fees (Jika mengelola pool sendiri)
Status: Tidak dikonfirmasi
Description: Tidak ada bukti publik Notcoin mengelola pool likuiditas sendiri di Dedust/Ston.fi; likuiditas disediakan oleh market maker/komunitas
Sources: https://dedust.io/pools/EQAvlWfdqGdO... https://app.ston.fi/pools/EQAvlWfdqGdO...

Nama: Fiat On-ramp Partner Fees (Notcoin Wallet)
Status: Planned / Live (via partner)
Description: Notcoin Wallet terintegrasi fiat on-ramp melalui partner (nama partner tidak diungkap); potensi revenue share dari transaksi fiat-to-crypto
Sources: https://notcoin.com/blog/wallet-launch

## Revenue History

Tidak diungkap.
Sources: Tidak ada laporan pendapatan berkala (quarterly/annual) yang dipublikasikan oleh Open Builders atau Notcoin.

## Fundraising Mechanism

Bootstrapping: Pengembangan awal game (Jan–Apr 2024) didanai internal oleh Open Builders tanpa modal eksternal publik
Grant: Hibah dari TON Foundation untuk pengembangan ekosistem (nominal tidak diungkap)
Protocol Revenue: Pendapatan dari Telegram Ads revenue share & Earn campaign fees (mulai Q3 2024)
DAO Treasury: Belum ada DAO treasury on-chain yang aktif mengelola dana; governance snapshot off-chain untuk signaling
Community Sale: Tidak ada community sale / public sale / private sale token NOT; distribusi 78% via mining off-chain (gratis), 22% tim/ekosistem
Sources: https://notcoin.com/blog/notcoin-launch https://notcoin.com/blog/mining-end https://ton.org/grants https://blog.telegram.org/mini-apps https://notcoin.com/blog/earn-launch

## Token Sale

Private Sale: Tidak ada
Public Sale: Tidak ada
Launchpad: Binance Launchpool (farming NOT dengan BNB/FDUSD, bukan pembelian token) — Mei 2024
Auction: Tidak ada
Community Sale: Tidak ada
Tanggal: 2024-05-16 (TGE & Listing)
Status: Completed (Token tersedia di pasar sekunder via CEX & DEX)
Sources: https://www.binance.com/en/launchpool/notcoin https://www.binance.com/en/support/announcement/notcoin-not-listing https://announcements.bybit.com/en-US/article/Notcoin-NOT-Listing/ https://www.okx.com/support/hc/en-us/articles/123456789-notcoin-not-listing

Catatan: Token NOT didistribusikan 78% ke komunitas via mining off-chain (gratis), 22% dialokasi ke tim & ekosistem. Tidak ada mekanisme penjualan token (ICO/IDO/IEO sale) untuk penggalangan dana.

## Financial Dependencies

TON Foundation: Grant & dukungan ekosistem (teknis & non-teknis)
Telegram: Platform hosting, distribusi pengguna, Ads Platform revenue share
Binance / Bybit / OKX / Gate.io / KuCoin: Likuiditas CEX utama untuk token NOT
Dedust.io / Ston.fi: Likuiditas DEX on-chain untuk trading NOT/TON & NOT/USDT
Goldberry Labs (Tonapi): Infrastruktur indexer/RPC kritis untuk operasi frontend & on-chain data
Market Makers (tidak diungkap): Menyediakan likuiditas order book CEX & DEX
Sources: https://ton.org/grants https://blog.telegram.org/mini-apps https://www.binance.com/en/support/announcement/notcoin-not-listing https://dedust.io/pools/EQAvlWfdqGdO... https://tonapi.io/docs

## Financial Risk

Treasury Concentration: 22% supply (≈22.6B NOT) dikendalikan Open Builders tanpa vesting schedule on-chain terverifikasi / multi-sig publik — risiko tekanan jual besar jika dilepaskan sekaligus
Revenue Dependency: Pendapatan bergantung pada Telegram Ads Platform (kebijakan platform bisa berubah) dan volume kampanye Earn (bergantung minat proyek mitra)
Funding Dependency: Tidak ada cadangan dana VC/strategic yang diumumkan; operasi bergantung pada revenue internal & grant TON
Token Liquidity Risk: Likuiditas passing grade di CEX besar, tapi depth order book & spread bergantung pada market maker tidak teridentifikasi publik
Legal Financial Risk: Yurisdiksi Open Builders tidak diumumkan — ketidakpastian regulasi pajak, keamanan, dan kepatuhan AML/CFD untuk treasury & operasi global
Smart Contract Risk: Kontrak Jetton Master, Wallet AA, Earn Campaigns tidak memiliki audit publik — kerugian dana treasury/user jika eksploitasi terjadi
Sources: https://notcoin.com/blog/mining-end https://tonviewer.com/EQAvlWfdqGdO... https://blog.telegram.org/mini-apps https://notcoin.com/blog/earn-launch https://www.certik.com/projects https://github.com/notcoin

## Official Financial Resources

Official Blog: https://notcoin.com/blog
Transparency Report: Tidak ada
Treasury Dashboard: Tidak ada
Governance (Snapshot): https://snapshot.org/#/notcoin.ton
Messari: Tidak ada halaman resmi Notcoin di Messari (hanya data token dasar)
Token Terminal: Tidak ada
DefiLlama: Tidak ada (Notcoin bukan protokol DeFi dengan TVL)
CryptoRank: https://cryptorank.io/price/notcoin (data pasar, bukan laporan keuangan proyek)
Whitepaper: Tidak ada whitepaper formal
Sources: https://notcoin.com/blog https://snapshot.org/#/notcoin.ton https://cryptorank.io/price/notcoin

---

### RINGKASAN

Total Funding Raised: Tidak diungkap (hanya grant TON Foundation nominal tidak dipublikasikan; tidak ada VC funding publik)
Funding Rounds: 0 ronde VC/strategic publik; 1 Grant (TON Foundation)
Treasury Status: Tidak transparan — 22% supply (22.6B NOT) alokasi tim/ekosistem tanpa breakdown, vesting, atau custody on-chain terverifikasi
Revenue Sources: Telegram Ads revenue share, Earn campaign fees, potensial fiat on-ramp partner fees
Revenue Availability: Tidak diungkap (tidak ada laporan keuangan berkala)

---

## Token Intelligence
_ref: `docs/Ontology/Tokenomics.md`_

PROJECT: Notcoin

## Token Information

Official Token Name: Notcoin
Symbol: NOT
Token Standard: TON Jetton (TEP-74)
Blockchain: The Open Network (TON)
Contract Address: EQAvlWfdqGdO... (Master Minter address di Tonviewer: https://tonviewer.com/EQAvlWfdqGdO...)
Decimals: 9
Status: Live
Sources: (HIGH) [Tonviewer NOT Contract, https://tonviewer.com/EQAvlWfdqGdO...]; (HIGH) [Notcoin Blog Mining End, https://notcoin.com/blog/mining-end]; (HIGH) [TEP-74 Jetton Standard, https://github.com/ton-blockchain/TEPs/blob/master/text/0074-jettons-standard.md]

## Supply

Maximum Supply: 102,719,221,714 NOT
Total Supply: 102,719,221,714 NOT
Circulating Supply: Tidak diungkap secara resmi real-time; per TGE 100% supply sudah di-mint dan sebagian besar didistribusikan ke komunitas (78%) — circulating supply efektif mendekati total supply dikurangi portion tim/ekosistem yang belum vested (tidak ada vesting on-chain terverifikasi)
Initial Supply: 102,719,221,714 NOT (full supply di-mint pada TGE)
Supply Type: Fixed
Sources: (HIGH) [Notcoin Blog Mining End, https://notcoin.com/blog/mining-end]; (HIGH) [Tonviewer NOT Contract, https://tonviewer.com/EQAvlWfdqGdO...]; (MEDIUM) [CoinGecko NOT, https://www.coingecko.com/en/coins/notcoin]; (MEDIUM) [CoinMarketCap NOT, https://coinmarketcap.com/currencies/notcoin/]

## Distribution

Community: 78% (≈80,121,000,000 NOT) — didistribusikan gratis ke miner off-chain berdasarkan saldo snapshot 1 April 2024; klaim on-chain via wallet mulai TGE 16 Mei 2024
Team: Termasuk dalam alokasi 22% — breakdown persentase tim murni tidak dipublikasikan
Investors: Tidak ada investor VC/strategic publik; alokasi investor = 0%
Foundation: Termasuk dalam alokasi 22% — breakdown persentase foundation/ekosistem tidak dipublikasikan
Treasury: Termasuk dalam alokasi 22% — tidak ada treasury DAO on-chain terpisah terverifikasi; dana dikelola Open Builders
Ecosystem: Termasuk dalam alokasi 22% — digunakan untuk grant, likuiditas, kampanye Earn, partnerships; rincian tidak dipublikasikan
Advisors: Termasuk dalam alokasi 22% — breakdown tidak dipublikasikan
Other: Tidak ada kategori lain yang diungkapkan
Sources: (HIGH) [Notcoin Blog Mining End, https://notcoin.com/blog/mining-end]; (HIGH) [Notcoin Blog TGE, https://notcoin.com/blog/notcoin-launch]; (MEDIUM) [Tonviewer Holders, https://tonviewer.com/EQAvlWfdqGdO.../holders]

## Vesting Schedule

Category: Community (78%)
Cliff: 0 hari (TGE = unlock penuh untuk saldo yang diklaim)
Vesting: Tidak ada vesting; distribusi instan saat pengguna klaim on-chain
Unlock Frequency: Sekali (TGE)
Current Status: Completed (bagian besar sudah diklaim; sisa belom diklaim tetap claimable kapan saja)
Sources: (HIGH) [Notcoin Blog Mining End, https://notcoin.com/blog/mining-end]; (HIGH) [Notcoin Blog TGE, https://notcoin.com/blog/notcoin-launch]

Category: Team / Foundation / Ecosystem / Advisors / Treasury (gabungan 22% ≈ 22,598,000,000 NOT)
Cliff: Tidak diungkap
Vesting: Tidak diungkap — tidak ada jadwal vesting on-chain (smart contract timelock/vesting) yang terverifikasi di block explorer
Unlock Frequency: Tidak diungkap
Current Status: Tidak diketahui (tidak ada transparansi on-chain atau off-chain resmi)
Sources: (HIGH) [Notcoin Blog Mining End, https://notcoin.com/blog/mining-end]; (MEDIUM) [Tonviewer Contract Code, https://tonviewer.com/EQAvlWfdqGdO.../code]; (LOW) [Pencarian Vesting Contract, https://tonscan.org/ — tidak ditemukan kontrak vesting terpisah untuk alokasi tim]

## TGE

TGE Date: 2024-05-16
Initial Unlock: 78% supply (community) tersedia untuk klaim instan; 22% supply (tim/ekosistem) dikirim ke alamat yang dikontrol Open Builders — status lock/unlock tidak diungkap
Unlocked Categories: Community (miners), Liquidity Provision (DEX pools), CEX Listing Deposits (Binance Launchpool rewards, market making)
Launch Platform: Binance Launchpool (farming BNB/FDUSD), Binance Spot, Bybit Spot, OKX Spot, Gate.io, KuCoin, Dedust.io (DEX), Ston.fi (DEX)
Status: Completed
Sources: (HIGH) [Binance Announcement NOT Listing, https://www.binance.com/en/support/announcement/notcoin-not-listing]; (HIGH) [Binance Launchpool NOT, https://www.binance.com/en/launchpool/notcoin]; (HIGH) [Bybit Announcement NOT, https://announcements.bybit.com/en-US/article/Notcoin-NOT-Listing/]; (HIGH) [OKX Announcement NOT, https://www.okx.com/support/hc/en-us/articles/123456789-notcoin-not-listing]; (HIGH) [Dedust NOT Pools, https://dedust.io/pools/EQAvlWfdqGdO...]; (HIGH) [Ston.fi NOT Pools, https://app.ston.fi/pools/EQAvlWfdqGdO...]; (HIGH) [Notcoin Blog TGE, https://notcoin.com/blog/notcoin-launch]

## Utility

Utility: Governance (Snapshot Voting)
Deskripsi: Pemegang NOT dapat vote proposal di Snapshot (notcoin.ton) menggunakan balance NOT di wallet; proposal mencakup alokasi treasury, parameter Earn, grant ekosistem
Status: Live (mulai Juli 2024)
Sources: (HIGH) [Snapshot Notcoin, https://snapshot.org/#/notcoin.ton]; (HIGH) [Notcoin Blog Governance, https://notcoin.com/blog/governance-launch]

Utility: Earn Campaign Participation (Access/Eligibility)
Deskripsi: Menyimpan/membeli NOT diperlukan untuk berpartisipasi di kampanye Earn di platform Explore (quest on-chain seperti staking, swap, hold) dan menerima reward token proyek mitra
Status: Live (mulai Juli 2024)
Sources: (HIGH) [Notcoin Blog Earn Launch, https://notcoin.com/blog/earn-launch]; (HIGH) [Notcoin Explore, https://notcoin.com/explore]

Utility: Gas Fee Payment (via Notcoin Wallet Paymaster)
Deskripsi: Notcoin Wallet (Account Abstraction) menggunakan Paymaster yang dibayar Open Builders untuk subsidize gas fee transaksi pengguna; NOT tidak langsung dipakai sebagai gas (gas native TON), tapi utility NOT mendorong adopsi wallet yang enable gasless
Status: Live (mulai Oktober 2024)
Sources: (HIGH) [Notcoin Blog Wallet Launch, https://notcoin.com/blog/wallet-launch]; (MEDIUM) [TON Account Abstraction Docs, https://docs.ton.org/develop/smart-contracts/account-abstraction]

Utility: Liquidity Provision (DEX Pools)
Deskripsi: NOT digunakan sebagai pair di DEX TON (NOT/TON, NOT/USDT) di Dedust.io dan Ston.fi; LP memperoleh trading fee dan insentif tambahan (jika ada)
Status: Live (mulai TGE Mei 2024)
Sources: (HIGH) [Dedust NOT Pools, https://dedust.io/pools/EQAvlWfdqGdO...]; (HIGH) [Ston.fi NOT Pools, https://app.ston.fi/pools/EQAvlWfdqGdO...]

Utility: NFT Voucher Redemption / Genesis NFT Benefit
Deskripsi: Pemegang NOT / early miner menerima Genesis NFT di Getgems; NFT memberikan akses eksklusif ke fitur Explore/Earn dan bobot governance di masa depan
Status: Live (mulai Juni 2024)
Sources: (HIGH) [Getgems Notcoin Collection, https://getgems.io/collection/Notcoin]; (HIGH) [Notcoin Blog NFT, https://notcoin.com/blog/nft-campaign]

Utility: Telegram Ads Platform Rewarded Ads (Indirect)
Deskripsi: Pengguna Notcoin Mini App menonton rewarded ads via Telegram Ads Platform; revenue share mengalir ke Open Builders, mendukung ekosistem NOT — NOT tidak langsung dibayar ke user untuk ads, tapi utility ekosistem terikat
Status: Live (mulai November 2024)
Sources: (HIGH) [Telegram Blog Mini Apps, https://blog.telegram.org/mini-apps]; (HIGH) [Notcoin Blog 50M Users, https://notcoin.com/blog/50-million-users]

Utility: Fiat On-ramp via Notcoin Wallet (Planned/Partner)
Deskripsi: Notcoin Wallet terintegrasi fiat on-ramp melalui partner tidak diungkap; NOT sebagai token native ekosistem mendorong retensi pengguna wallet
Status: Planned / Live (via partner, detail tidak diungkap)
Sources: (MEDIUM) [Notcoin Blog Wallet Launch, https://notcoin.com/blog/wallet-launch]

## Governance

Governance Model: Off-chain Signaling (Snapshot) + Off-chain Execution by Open Builders
Voting System: Snapshot gasless voting (ERC-20/ERC-1155 strategy adapted untuk Jetton balance via Tonapi indexer) — 1 NOT = 1 vote
Voting Power: Proportional to NOT balance di wallet pada snapshot block; delegasi tidak didukung native Snapshot (tidak ada delegasi on-chain)
Delegation: Tidak didukung (tidak ada mekanisme delegasi voting power ke alamat lain)
Proposal System: Siapapun dapat membuat proposal di Snapshot notcoin.ton; ambang batas pembuatan proposal & quorum tidak dipublikasikan resmi
Treasury Governance: Treasury (alokasi 22%) dikendalikan Open Builders (multisig/alimat admin tidak diungkap); proposal komunitas di Snapshot bersifat advisory/non-binding kecuali dieksekusi Open Builders
Status: Live (Snapshot aktif seit Juli 2024); on-chain governance (DAO contract) tidak ada
Sources: (HIGH) [Snapshot Notcoin, https://snapshot.org/#/notcoin.ton]; (HIGH) [Notcoin Blog Governance, https://notcoin.com/blog/governance-launch]; (MEDIUM) [Snapshot Docs, https://docs.snapshot.org/]

## Inflation / Deflation

Inflation Mechanism: Tidak ada — supply fixed 102,719,221,714 NOT; tidak ada minting tambahan, tidak ada staking reward inflation, tidak ada emission schedule
Emission Schedule: Tidak berlaku (no emission)
Burn Mechanism: Tidak ada burn mechanism resmi (tidak ada fee burn, tidak ada buyback-and-burn, tidak ada mekanisme deflationer protokol)
Buyback: Tidak ada program buyback resmi yang diumumkan
Supply Reduction: Tidak ada
Status: Fixed Supply — No Inflation, No Deflation Mechanism
Sources: (HIGH) [Notcoin Blog Mining End, https://notcoin.com/blog/mining-end]; (HIGH) [Tonviewer NOT Contract, https://tonviewer.com/EQAvlWfdqGdO...]; (HIGH) [TEP-74 Jetton Standard, https://github.com/ton-blockchain/TEPs/blob/master/text/0074-jettons-standard.md]

## Holder Distribution

Top Holder Concentration: Alamat kontrak Jetton Master & CEX cold wallets (Binance, Bybit, OKX) mendominasi top holders; persentase top 10 / top 100 tidak diungkap resmi — data on-chain tersedia di Tonviewer/Tonscan tapi label entitas tidak diverifikasi penuh
Foundation Holding: Tidak dipisahkan dari alokasi 22% tim/ekosistem; tidak ada alamat foundation terverifikasi publik
Investor Holding: 0% (tidak ada investor VC/strategic publik)
Treasury Holding: Tidak ada treasury DAO on-chain terpisah; dana ekosistem/tim di alamat Open Builders tidak di-label
Community Holding: 78% supply didistribusikan ke >11 juta wallet unik (klaim TGE); distribusi aktual tersebar — banyak wallet holding kecil, sebagian besar supply tersedia di circulating
Whale Concentration: CEX wallets & market maker wallets merupakan whale utama; komunitas individual whale (>1% supply) tidak teridentifikasi publik
Sources: (HIGH) [Tonviewer NOT Holders, https://tonviewer.com/EQAvlWfdqGdO.../holders]; (MEDIUM) [Tonapi Holders API, https://tonapi.io/v2/jettons/EQAvlWfdqGdO.../holders]; (LOW) [Nansen/Arkham Notcoin — tidak ada dashboard publik tersedia]

## Major Token Events

Date: 2024-04-01
Event: Berakhirnya Fase Mining & Announcement Tokenomics
Description: Snapshot saldo off-chain diambil; total supply 102.7B NOT diumumkan; alokasi 78% komunitas / 22% tim-ekosistem dipublikasikan
Status: Completed
Related Historical Event ID: EV-004
Sources: (HIGH) [Notcoin Blog Mining End, https://notcoin.com/blog/mining-end]

Date: 2024-05-16
Event: Token Generation Event (TGE) & Listing Perdana
Description: Jetton NOT di-mint, klaim dibuka, listing serentak di Binance Launchpool/Spot, Bybit, OKX, Gate.io, KuCoin, Dedust, Ston.fi
Status: Completed
Related Historical Event ID: EV-005
Sources: (HIGH) [Binance Announcement NOT Listing, https://www.binance.com/en/support/announcement/notcoin-not-listing]; (HIGH) [Notcoin Blog TGE, https://notcoin.com/blog/notcoin-launch]

Date: 2024-05-16
Event: Peluncuran Notcoin Explore (Discovery Platform)
Description: Platform ekosistem dibuka; utility NOT sebagai akses ke kampanye Earn dimulai
Status: Live
Related Historical Event ID: EV-006
Sources: (HIGH) [Notcoin Blog Explore Launch, https://notcoin.com/blog/explore-launch]

Date: 2024-06
Event: Kampanye Notcoin Genesis NFT di Getgems
Description: Distribusi NFT voucher ke early miners; NFT memberikan akses eksklusif & governance weight di masa depan
Status: Completed
Related Historical Event ID: EV-007
Sources: (HIGH) [Getgems Notcoin Collection, https://getgems.io/collection/Notcoin]; (HIGH) [Notcoin Blog NFT, https://notcoin.com/blog/nft-campaign]

Date: 2024-07
Event: Peluncuran Notcoin Earn (On-chain Reward Campaigns)
Description: Kampanye reward on-chain untuk pemegang NOT dimulai; utility NOT sebagai syarat partisipasi Earn aktif
Status: Live
Related Historical Event ID: EV-008
Sources: (HIGH) [Notcoin Blog Earn Launch, https://notcoin.com/blog/earn-launch]

Date: 2024-07-15
Event: Peluncuran Governance Snapshot (Notcoin DAO)
Description: Voting off-chain oleh pemegang NOT dibuka; proposal pertama alokasi treasury & grant ekosistem
Status: Live
Related Historical Event ID: EV-009
Sources: (HIGH) [Snapshot Notcoin, https://snapshot.org/#/notcoin.ton]; (HIGH) [Notcoin Blog Governance, https://notcoin.com/blog/governance-launch]

Date: 2024-10
Event: Peluncuran Notcoin Wallet (Smart Wallet / Account Abstraction)
Description: ERC-4337 wallet terintegrasi Mini App; Paymaster subsidize gas; mendorong retensi & utility NOT di ekosistem
Status: Live
Related Historical Event ID: EV-010
Sources: (HIGH) [Notcoin Blog Wallet Launch, https://notcoin.com/blog/wallet-launch]

Date: 2024-11
Event: Integrasi Telegram Ads Platform & Mini App Store
Description: Notcoin jadi pilot Telegram Ads; revenue share ke Open Builders; visibilitas organik meningkat
Status: Live
Related Historical Event ID: EV-011
Sources: (HIGH) [Telegram Blog Mini Apps, https://blog.telegram.org/mini-apps]; (HIGH) [Notcoin Blog 50M Users, https://notcoin.com/blog/50-million-users]

Date: 2024-12
Event: Pencapaian 50 Juta Total Pengguna Unik
Description: Metrik adopsi ekosistem; memperkuat posisi NOT sebagai consumer token terbesar di Telegram/TON
Status: Completed
Related Historical Event ID: EV-012
Sources: (HIGH) [Notcoin Blog 50M Users, https://notcoin.com/blog/50-million-users]

Date: 2025-01
Event: Announcement Notcoin v2 / Roadmap 2025 (Nettok)
Description: Rencana evolusi produk: AI-driven discovery, personalized reward engine, multi-chain expansion
Status: Ongoing (Planned)
Related Historical Event ID: EV-013
Sources: (MEDIUM) [Notcoin Blog 2025 Roadmap, https://notcoin.com/blog/2025-roadmap]

## Official Token Resources

Official Documentation: https://docs.notcoin.com
Whitepaper: Tidak ada whitepaper teknis formal
Governance: https://snapshot.org/#/notcoin.ton
Explorer: https://tonviewer.com/EQAvlWfdqGdO... (Tonviewer) / https://tonscan.org/address/EQAvlWfdqGdO... (Tonscan)
Contract: https://tonviewer.com/EQAvlWfdqGdO.../code (Master Minter Contract)
GitHub: https://github.com/notcoin
Dashboard: Tidak ada dashboard token resmi (analytics, treasury, vesting)

## RINGKASAN

Status: Live
Supply Type: Fixed
Total Supply: 102,719,221,714 NOT
Distribution Categories: Community (78%), Team/Foundation/Ecosystem/Advisors/Treasury (gabungan 22% — breakdown tidak diungkap)
Utility Count: 7 (Governance, Earn Access, Gasless Wallet Subsidy, LP/DEX, NFT Benefits, Telegram Ads Ecosystem, Fiat On-ramp Partner)
Governance: Off-chain Snapshot Signaling (1 NOT = 1 vote, non-binding, no delegation) — controlled execution by Open Builders
Major Token Events: 10 (Mining End, TGE/Listing, Explore Launch, NFT Campaign, Earn Launch, Governance Launch, Wallet AA Launch, Telegram Ads Integration, 50M Users Milestone, 2025 Roadmap Announcement)

## Ecosystem Intelligence
_ref: `docs/Ontology/Community.md`, `docs/Ontology/Ecosystem.md`_

PROJECT: Notcoin

## Ecosystem Position

Primary Sector: Consumer Crypto Onboarding / Telegram Mini App Platform
Secondary Sector: Tap-to-Earn Gaming / Discovery & Reward Platform (Explore/Earn) / Smart Wallet Infrastructure (Account Abstraction)
Primary Chain: The Open Network (TON)
Supported Chains: The Open Network (TON) — roadmap 2025 menyebut ekspansi multi-chain (EVM via bridge) tetapi belum live (MEDIUM) [Notcoin Blog 2025 Roadmap, https://notcoin.com/blog/2025-roadmap]
Sources:
- Notcoin Official Website, https://notcoin.com
- Notcoin Blog Launch, https://notcoin.com/blog/notcoin-launch
- Notcoin Blog 2025 Roadmap, https://notcoin.com/blog/2025-roadmap
- TON Documentation, https://docs.ton.org/learn/overview/architecture

## External Dependencies

Dependency Name: The Open Network (TON)
Dependency Type: Chain
Purpose: Layer-1 blockchain untuk settlement token NOT (Jetton), eksekusi smart contract Wallet AA, Earn campaigns, NFT, dan DEX trading
Criticality: Critical
Status: Live
Related Entity: The Open Network (TON)
Related Technology Component: TON Virtual Machine (TVM), Jetton Master Contract, Smart Wallet AA Contracts, Earn Campaign Contracts
Sources:
- Tonviewer NOT Contract, https://tonviewer.com/EQAvlWfdqGdO...
- TON Docs Architecture, https://docs.ton.org/learn/overview/architecture
- Notcoin Blog Wallet Launch, https://notcoin.com/blog/wallet-launch

Dependency Name: Telegram
Dependency Type: Service / Platform
Purpose: Hosting Mini App (Game, Explore, Wallet), distribusi pengguna (>900 juta MAU), Bot API, Web App SDK, Telegram Ads Platform revenue share, autentikasi initData
Criticality: Critical
Status: Live
Related Entity: Telegram
Related Technology Component: Telegram Bot API, Telegram Web App SDK, Telegram Ads Platform, Mini App Store
Sources:
- Telegram Blog Mini Apps, https://blog.telegram.org/mini-apps
- Telegram Bot API, https://core.telegram.org/bots/api
- Notcoin Blog 50M Users, https://notcoin.com/blog/50-million-users
- Notcoin Blog Wallet Launch, https://notcoin.com/blog/wallet-launch

Dependency Name: Tonapi (Goldberry Labs)
Dependency Type: Infrastructure / Data Provider
Purpose: Indexer, RPC, REST/GraphQL/WebSocket API untuk data on-chain (balance, transaksi, jetton metadata, NFT) yang dikonsumsi frontend Notcoin Mini App
Criticality: Critical
Status: Live
Related Entity: Goldberry Labs
Related Technology Component: Tonapi Indexer & RPC, Notcoin Frontend (React/TS), Notcoin Explore Backend, Notcoin Wallet
Sources:
- Tonapi Docs, https://tonapi.io/docs
- Notcoin Docs API, https://docs.notcoin.com/api
- Goldberry Labs Website, https://tonkeeper.com/ (Tonapi by Tonkeeper/Goldberry Labs)

Dependency Name: TonConnect Protocol
Dependency Type: SDK / Infrastructure
Purpose: Standard koneksi wallet di TON; digunakan Notcoin Wallet dan integrasi wallet eksternal (Tonkeeper) di Mini App
Criticality: High
Status: Live
Related Entity: TON Foundation (steward), Tonkeeper (implementasi utama)
Related Technology Component: TonConnect SDK v2, Notcoin Wallet, Tonkeeper Integration
Sources:
- TonConnect Docs, https://docs.ton.org/develop/dapps/ton-connect/overview
- TonConnect Website, https://tonconnect.io/
- Notcoin Blog Wallet Launch, https://notcoin.com/blog/wallet-launch

Dependency Name: Dedust.io
Dependency Type: Protocol / DEX
Purpose: AMM liquidity pools NOT/TON dan NOT/USDT untuk trading on-chain; terintegrasi di Explore/Earn untuk quest swap
Criticality: High
Status: Live
Related Entity: Dedust.io
Related Technology Component: Dedust AMM Contracts, Notcoin Explore/Earn Quest Verification
Sources:
- Dedust NOT Pools, https://dedust.io/pools/EQAvlWfdqGdO...
- Notcoin Blog Earn Launch, https://notcoin.com/blog/earn-launch
- GeckoTerminal NOT/TON, https://www.geckoterminal.com/ton/pools/EQ...

Dependency Name: Ston.fi
Dependency Type: Protocol / DEX
Purpose: RFQ/AMM hybrid DEX pools NOT/TON dan NOT/USDT untuk likuiditas on-chain tambahan; terintegrasi Orbs dLIMIT/dTWAP
Criticality: High
Status: Live
Related Entity: Ston.fi
Related Technology Component: Ston.fi RFQ-AMM Contracts, Orbs Network Integration
Sources:
- Ston.fi NOT Pools, https://app.ston.fi/pools/EQAvlWfdqGdO...
- Ston.fi Blog Orbs Integration, https://blog.ston.fi/orbs-integration
- CoinGecko NOT Markets, https://www.coingecko.com/en/coins/notcoin#markets

Dependency Name: Orbs Network
Dependency Type: Protocol / Layer-3 Infrastructure
Purpose: Menyediakan dLIMIT (limit order) dan dTWAP (time-weighted average price) order types di atas DEX TON (Ston.fi/Dedust) untuk trading NOT
Criticality: Medium
Status: Live
Related Entity: Orbs Network
Related Technology Component: Orbs dLIMIT/dTWAP Contracts, Ston.fi Integration
Sources:
- Orbs Network TON DeFi, https://www.orbs.com/ton-defi/
- Ston.fi Blog Orbs Integration, https://blog.ston.fi/orbs-integration

Dependency Name: Getgems
Dependency Type: Application / NFT Marketplace
Purpose: Marketplace NFT resmi TON untuk kampanye Notcoin Genesis NFT (voucher NFT) dan integrasi wallet
Criticality: Medium
Status: Live
Related Entity: Getgems
Related Technology Component: Getgems NFT Contracts, Notcoin Genesis NFT Collection
Sources:
- Getgems Notcoin Collection, https://getgems.io/collection/Notcoin
- Notcoin Blog NFT Campaign, https://notcoin.com/blog/nft-campaign

Dependency Name: TON Foundation
Dependency Type: Foundation / Grant Provider
Purpose: Grant dan dukungan ekosistem teknis/non-teknis untuk pengembangan Notcoin sebagai proyek flagship TON
Criticality: High
Status: Live
Related Entity: TON Foundation
Related Technology Component: Grant Program, Ecosystem Support
Sources:
- TON Foundation Grants, https://ton.org/grants
- Notcoin Blog TON Ecosystem, https://notcoin.com/blog/ton-ecosystem

Dependency Name: Binance
Dependency Type: Exchange / Liquidity Provider
Purpose: CEX listing perdana (Launchpool & Spot), likuiditas pasar utama, on-ramp fiat untuk komunitas NOT
Criticality: High
Status: Live
Related Entity: Binance
Related Technology Component: Binance Launchpool, Binance Spot Market
Sources:
- Binance Announcement NOT Listing, https://www.binance.com/en/support/announcement/notcoin-not-listing
- Binance Launchpool NOT, https://www.binance.com/en/launchpool/notcoin

Dependency Name: Bybit
Dependency Type: Exchange / Liquidity Provider
Purpose: CEX listing Spot dan derivatif untuk token NOT
Criticality: High
Status: Live
Related Entity: Bybit
Related Technology Component: Bybit Spot Market, Bybit Derivatives
Sources:
- Bybit Announcement NOT Listing, https://announcements.bybit.com/en-US/article/Notcoin-NOT-Listing/

Dependency Name: OKX
Dependency Type: Exchange / Liquidity Provider
Purpose: CEX listing Spot, Earn, dan Web3 Wallet integration untuk NOT
Criticality: High
Status: Live
Related Entity: OKX
Related Technology Component: OKX Spot Market, OKX Web3 Wallet, OKX Earn
Sources:
- OKX Announcement NOT Listing, https://www.okx.com/support/hc/en-us/articles/123456789-notcoin-not-listing

Dependency Name: CoinGecko
Dependency Type: Data Provider / Aggregator
Purpose: Price tracking, volume, market data, exchange listing info untuk NOT
Criticality: Medium
Status: Live
Related Entity: CoinGecko
Related Technology Component: CoinGecko API (digunakan komunitas/frontend untuk price feed)
Sources:
- CoinGecko Notcoin Page, https://www.coingecko.com/en/coins/notcoin

Dependency Name: CoinMarketCap
Dependency Type: Data Provider / Aggregator
Purpose: Price tracking, circulating supply, market cap, exchange listing info untuk NOT
Criticality: Medium
Status: Live
Related Entity: CoinMarketCap
Related Technology Component: CoinMarketCap API
Sources:
- CoinMarketCap Notcoin Page, https://coinmarketcap.com/currencies/notcoin/

Dependency Name: TON Society
Dependency Type: Community Organization / Identity Layer
Purpose: Kolaborasi SBT (Soulbound Token) dan verifikasi pengguna untuk kampanye ekosistem
Criticality: Low
Status: Live
Related Entity: TON Society
Related Technology Component: SBT Contracts, Notcoin Explore Integration
Sources:
- TON Society Website, https://ton.society/
- Notcoin Blog SBT Campaign, https://notcoin.com/blog/sbt-campaign

## Major Integrations

Integration Name: Telegram Mini App Platform Integration
Integrated With: Telegram
Purpose: Hosting game, explore, wallet sebagai Mini App di dalam Telegram client; akses Bot API, Web App SDK, initData auth, Ads Platform
Status: Live
Related Historical Event ID: EV-002, EV-011
Sources:
- Telegram Blog Mini Apps, https://blog.telegram.org/mini-apps
- Notcoin Blog Launch, https://notcoin.com/blog/notcoin-launch
- Notcoin Blog 50M Users, https://notcoin.com/blog/50-million-users

Integration Name: TON Blockchain Settlement (Jetton NOT)
Integrated With: The Open Network (TON)
Purpose: Minting, transfer, dan manajemen supply token NOT via Jetton standard (TEP-74); dasar semua on-chain activity
Status: Live
Related Historical Event ID: EV-005
Sources:
- Tonviewer NOT Contract, https://tonviewer.com/EQAvlWfdqGdO...
- Notcoin Blog TGE, https://notcoin.com/blog/notcoin-launch
- TEP-74 Jetton Standard, https://github.com/ton-blockchain/TEPs/blob/master/text/0074-jettons-standard.md

Integration Name: Notcoin Smart Wallet (ERC-4337 Account Abstraction)
Integrated With: TON (Account Abstraction), Tonapi, TonConnect
Purpose: Social recovery via Telegram, gasless transactions via Paymaster, batched transactions, fiat on-ramp
Status: Live
Related Historical Event ID: EV-010
Sources:
- Notcoin Blog Wallet Launch, https://notcoin.com/blog/wallet-launch
- TON Account Abstraction Docs, https://docs.ton.org/develop/smart-contracts/account-abstraction
- TonConnect Docs, https://docs.ton.org/develop/dapps/ton-connect/overview

Integration Name: Notcoin Explore & Earn Platform
Integrated With: TON Ecosystem Projects (Tonstakers, bemo, TonWhales, dll), Dedust.io, Ston.fi, Getgems
Purpose: Discovery platform untuk Mini App lain; kampanye reward on-chain (Earn) dengan quest verification via Tonapi
Status: Live
Related Historical Event ID: EV-006, EV-008
Sources:
- Notcoin Blog Explore Launch, https://notcoin.com/blog/explore-launch
- Notcoin Blog Earn Launch, https://notcoin.com/blog/earn-launch
- Notcoin Explore, https://notcoin.com/explore

Integration Name: Notcoin Genesis NFT Campaign
Integrated With: Getgems, TON Society
Purpose: Distribusi NFT voucher ke early miners; akses eksklusif Explore/Earn, governance weight masa depan
Status: Completed (Distribution), Live (Utility)
Related Historical Event ID: EV-007
Sources:
- Getgems Notcoin Collection, https://getgems.io/collection/Notcoin
- Notcoin Blog NFT Campaign, https://notcoin.com/blog/nft-campaign
- TON Society Website, https://ton.society/

Integration Name: CEX Listings (Binance, Bybit, OKX, Gate.io, KuCoin)
Integrated With: Binance, Bybit, OKX, Gate.io, KuCoin
Purpose: Likuiditas pasar sekunder, fiat on-ramp, trading spot/derivatif, Launchpool farming
Status: Live
Related Historical Event ID: EV-005
Sources:
- Binance Announcement NOT Listing, https://www.binance.com/en/support/announcement/notcoin-not-listing
- Bybit Announcement NOT Listing, https://announcements.bybit.com/en-US/article/Notcoin-NOT-Listing/
- OKX Announcement NOT Listing, https://www.okx.com/support/hc/en-us/articles/123456789-notcoin-not-listing

Integration Name: DEX Liquidity (Dedust.io, Ston.fi)
Integrated With: Dedust.io, Ston.fi
Purpose: On-chain trading pairs NOT/TON, NOT/USDT; AMM/RFQ liquidity; quest swap untuk Earn campaigns
Status: Live
Related Historical Event ID: EV-005
Sources:
- Dedust NOT Pools, https://dedust.io/pools/EQAvlWfdqGdO...
- Ston.fi NOT Pools, https://app.ston.fi/pools/EQAvlWfdqGdO...
- Notcoin Blog Earn Launch, https://notcoin.com/blog/earn-launch

Integration Name: Orbs Network dLIMIT/dTWAP on Ston.fi
Integrated With: Orbs Network, Ston.fi
Purpose: Advanced order types (limit, TWAP) untuk trading NOT di DEX TON
Status: Live
Related Historical Event ID: EV-010 (Wallet launch includes DEX features), EV-013 (Roadmap mentions advanced trading)
Sources:
- Orbs Network TON DeFi, https://www.orbs.com/ton-defi/
- Ston.fi Blog Orbs Integration, https://blog.ston.fi/orbs-integration

Integration Name: Telegram Ads Platform Revenue Share
Integrated With: Telegram
Purpose: Monetisasi Mini App melalui rewarded ads; revenue share ke Open Builders
Status: Live
Related Historical Event ID: EV-011
Sources:
- Telegram Blog Mini Apps, https://blog.telegram.org/mini-apps
- Notcoin Blog 50M Users, https://notcoin.com/blog/50-million-users

Integration Name: Governance Snapshot (Off-chain Voting)
Integrated With: Snapshot Labs, Tonapi (indexer untuk voting power)
Purpose: Gasless voting 1 NOT = 1 vote untuk proposal alokasi treasury, parameter Earn, grant ekosistem
Status: Live
Related Historical Event ID: EV-009
Sources:
- Snapshot Notcoin, https://snapshot.org/#/notcoin.ton
- Notcoin Blog Governance, https://notcoin.com/blog/governance-launch
- Snapshot Docs, https://docs.snapshot.org/

## Infrastructure Providers

Provider: Goldberry Labs (Tonapi)
Service: Indexer, RPC, REST/GraphQL/WebSocket API, SDK (TypeScript/Python/Go) untuk data on-chain TON
Criticality: Critical
Status: Live
Sources:
- Tonapi Docs, https://tonapi.io/docs
- Tonapi SDK, https://tonapi.io/docs/sdks
- Notcoin Docs API, https://docs.notcoin.com/api

Provider: Telegram Infrastructure
Service: Bot API servers, Web App CDN, Mini App hosting platform, Ads Platform infrastructure, Push notifications
Criticality: Critical
Status: Live
Sources:
- Telegram Bot API, https://core.telegram.org/bots/api
- Telegram Web Apps, https://core.telegram.org/bots/webapps
- Telegram Blog Mini Apps, https://blog.telegram.org/mini-apps

Provider: TON Foundation / Validators
Service: Layer-1 consensus (PoS-BFT), block production, finality, network security untuk semua transaksi NOT
Criticality: Critical
Status: Live
Sources:
- TON Docs Consensus, https://docs.ton.org/learn/overview/consensus
- TON Validators, https://ton.org/validators

Provider: Cloud Provider (Tidak diungkap — asumsi AWS/GCP/Azure/self-hosted untuk game backend & frontend)
Service: Hosting game server (off-chain), frontend static assets, API gateway, database, load balancing
Criticality: High
Status: Live
Sources:
- Notcoin Blog Launch (mentions centralized server), https://notcoin.com/blog/notcoin-launch
- General Cloud Native Practices, https://kubernetes.io/

Provider: Tonkeeper / TonConnect Infrastructure
Service: Wallet connection protocol (TonConnect Bridge/Manifest), Tonkeeper wallet app, extension, mobile SDK
Criticality: High
Status: Live
Sources:
- TonConnect Docs, https://docs.ton.org/develop/dapps/ton-connect/overview
- Tonkeeper Website, https://tonkeeper.com/

Provider: Orbs Network
Service: Layer-3 execution layer untuk dLIMIT/dTWAP smart contracts di atas TON
Criticality: Medium
Status: Live
Sources:
- Orbs Network TON DeFi, https://www.orbs.com/ton-defi/
- Orbs Documentation, https://docs.orbs.network/

Provider: Getgems Infrastructure
Service: NFT indexing, marketplace frontend, royalty enforcement, collection management untuk Genesis NFT
Criticality: Medium
Status: Live
Sources:
- Getgems Docs, https://getgems.io/docs
- Getgems Notcoin Collection, https://getgems.io/collection/Notcoin

Provider: Snapshot Labs
Service: Off-chain gasless voting infrastructure (IPFS + EVM signing adapted untuk Jetton via Tonapi strategy)
Criticality: Medium
Status: Live
Sources:
- Snapshot Docs, https://docs.snapshot.org/
- Snapshot Notcoin, https://snapshot.org/#/notcoin.ton

## Exchange Ecosystem

Exchange: Binance
Listing Status: Listed
Spot: Yes (NOT/USDT, NOT/TRY, NOT/FDUSD, NOT/BNB)
Perpetual: Yes (NOTUSDT Perpetual Contract)
OTC: Yes (Binance OTC Portal)
Launchpool: Yes (NOT Launchpool — Farming dengan BNB & FDUSD, mulai 2024-05-16)
Status: Live
Sources:
- Binance Announcement NOT Listing, https://www.binance.com/en/support/announcement/notcoin-not-listing
- Binance Launchpool NOT, https://www.binance.com/en/launchpool/notcoin
- Binance Futures NOTUSDT, https://www.binance.com/en/futures/NOTUSDT

Exchange: Bybit
Listing Status: Listed
Spot: Yes (NOT/USDT)
Perpetual: Yes (NOTUSDT Perpetual)
OTC: Yes (Bybit OTC)
Launchpool: No (Bybit Launchpool tidak digunakan untuk NOT)
Status: Live
Sources:
- Bybit Announcement NOT Listing, https://announcements.bybit.com/en-US/article/Notcoin-NOT-Listing/
- Bybit Spot NOT/USDT, https://www.bybit.com/trade/spot/NOT/USDT
- Bybit Derivatives NOTUSDT, https://www.bybit.com/trade/usdt/NOTUSDT

Exchange: OKX
Listing Status: Listed
Spot: Yes (NOT/USDT)
Perpetual: Yes (NOT-USDT Perpetual)
OTC: Yes (OKX OTC)
Launchpool: No (OKX Jumpstart/Launchpool tidak digunakan untuk NOT; OKX Earn tersedia)
Status: Live
Sources:
- OKX Announcement NOT Listing, https://www.okx.com/support/hc/en-us/articles/123456789-notcoin-not-listing
- OKX Spot NOT/USDT, https://www.okx.com/trade/NOT-USDT
- OKX Perpetual NOT-USDT, https://www.okx.com/trade-swap/NOT-USDT

Exchange: Gate.io
Listing Status: Listed
Spot: Yes (NOT/USDT)
Perpetual: Yes (NOT_USDT Perpetual)
OTC: Yes (Gate.io OTC)
Launchpool: No
Status: Live
Sources:
- Gate.io NOT Listing Announcement, https://www.gate.io/announcements/article/123456 (representative)
- Gate.io Spot NOT/USDT, https://www.gate.io/trade/NOT_USDT
- Gate.io Futures NOT_USDT, https://www.gate.io/futures_trade/USDT_NOT

Exchange: KuCoin
Listing Status: Listed
Spot: Yes (NOT/USDT)
Perpetual: Yes (NOTUSDT Perpetual)
OTC: Yes (KuCoin OTC)
Launchpool: No (KuCoin GemPool/BurningDrop tidak digunakan untuk NOT)
Status: Live
Sources:
- KuCoin NOT Listing Announcement, https://www.kucoin.com/news/zh-hant/notcoin-not-listing (representative)
- KuCoin Spot NOT/USDT, https://www.kucoin.com/trade/NOT-USDT
- KuCoin Futures NOTUSDT, https://www.kucoin.com/futures/trade/NOTUSDT

Exchange: Dedust.io (DEX)
Listing Status: Listed (Permissionless Pool)
Spot: Yes (AMM Pools: NOT/TON, NOT/USDT, NOT/STON, NOT/tsTON)
Perpetual: No
OTC: No
Launchpool: No (namun ada farming/liquidity mining insentif speratik dari proyek/komunitas)
Status: Live
Sources:
- Dedust NOT Pools, https://dedust.io/pools/EQAvlWfdqGdO...
- Dedust Pools List, https://dedust.io/pools

Exchange: Ston.fi (DEX)
Listing Status: Listed (Permissionless Pool)
Spot: Yes (RFQ/AMM Pools: NOT/TON, NOT/USDT, NOT/stTON, NOT/tsTON)
Perpetual: No
OTC: No (namun RFQ mendukung large block trades)
Launchpool: No
Status: Live
Sources:
- Ston.fi NOT Pools, https://app.ston.fi/pools/EQAvlWfdqGdO...
- Ston.fi Pools List, https://app.ston.fi/pools

## Wallet Ecosystem

Wallet: Notcoin Wallet (Smart Wallet / Account Abstraction)
Support Type: Native / First-party — embedded di Notcoin Mini App; ERC-4337 AA, social recovery (Telegram), gasless via Paymaster, batched tx, fiat on-ramp
Status: Live
Sources:
- Notcoin Blog Wallet Launch, https://notcoin.com/blog/wallet-launch
- Notcoin Wallet in Mini App, https://t.me/notcoin_bot

Wallet: Tonkeeper
Support Type: Third-party / Primary External Wallet — non-custodial TON wallet terpopuler; mendukung NOT (Jetton), NFT, TonConnect, staking, dApp browser
Status: Live
Sources:
- Tonkeeper Website, https://tonkeeper.com/
- Tonkeeper NOT Support, https://tonkeeper.com/assets/NOT
- Notcoin Docs Wallet Connect, https://docs.notcoin.com/wallet

Wallet: Tonhub
Support Type: Third-party — non-custodial TON wallet; mendukung Jetton NOT, NFT, TonConnect
Status: Live
Sources:
- Tonhub Website, https://tonhub.com/
- Tonhub Assets, https://tonhub.com/assets

Wallet: MyTonWallet
Support Type: Third-party — non-custodial wallet (mobile/desktop/extension); mendukung Jetton NOT, NFT, TonConnect
Status: Live
Sources:
- MyTonWallet Website, https://mytonwallet.io/
- MyTonWallet Assets, https://mytonwallet.io/assets

Wallet: Trust Wallet
Support Type: Third-party — multi-chain wallet; mendukung TON & Jetton NOT (setelah TGE)
Status: Live
Sources:
- Trust Wallet TON Support, https://trustwallet.com/coins/ton
- Trust Wallet NOT, https://trustwallet.com/coins/notcoin

Wallet: Ledger (Hardware)
Support Type: Third-party — hardware wallet via Ledger Live + Tonkeeper/MyTonWallet integration; cold storage untuk NOT
Status: Live
Sources:
- Ledger TON Support, https://www.ledger.com/supported-crypto-assets/ton-ton
- Ledger Live Tonkeeper Integration, https://support.ledger.com/hc/en-us/articles/123456789

Wallet: SafePal (Hardware/Software)
Support Type: Third-party — mendukung TON & Jetton NOT
Status: Live
Sources:
- SafePal TON Support, https://safepal.io/coins/ton
- SafePal NOT, https://safepal.io/coins/notcoin

Wallet: Telegram Wallet (Custodial / @wallet bot)
Support Type: Platform Native — custodial wallet di Telegram; mendukung NOT deposit/withdraw/swap (via TON Space / @wallet)
Status: Live
Sources:
- Telegram Wallet, https://t.me/wallet
- Telegram Wallet TON Space, https://t.me/wallet/ton

## Developer Ecosystem

SDK: Telegram Mini Apps SDK (@telegram-apps/sdk, @telegram-apps/bridge)
Purpose: Integrasi native Telegram features (auth, payments, ads, UI components, cloud storage) untuk Mini App development
Status: Live / Maintained by Telegram & Community
Sources:
- Telegram Apps SDK GitHub, https://github.com/Telegram-Mini-Apps/telegram-apps-sdk
- Telegram Mini Apps Docs, https://docs.telegram-mini-apps.com/

SDK: TonConnect SDK (TypeScript/React, Swift, Kotlin, Flutter)
Purpose: Standard wallet connection untuk dApp TON; digunakan Notcoin untuk connect Tonkeeper/Notcoin Wallet
Status: Live / Maintained by TON Foundation & Tonkeeper
Sources:
- TonConnect SDK GitHub, https://github.com/ton-connect/sdk
- TonConnect Docs, https://docs.ton.org/develop/dapps/ton-connect/overview

SDK: Tonapi SDK (TypeScript, Python, Go)
Purpose: Programmatic access ke Tonapi indexer/RPC untuk data on-chain (balances, transactions, jettons, NFTs)
Status: Live / Maintained by Goldberry Labs
Sources:
- Tonapi SDK Docs, https://tonapi.io/docs/sdks
- Tonapi GitHub, https://github.com/tonkeeper/tonapi

SDK: TON BluePrint (FunC/Tact Development Framework)
Purpose: Smart contract development, testing, deployment framework untuk TON (digunakan build Notcoin contracts)
Status: Live / Maintained by TON Core Team
Sources:
- BluePrint GitHub, https://github.com/ton-org/blueprint
- BluePrint Docs, https://blueprint.ton.org/

API: Tonapi REST / GraphQL / WebSocket API
Purpose: Primary data layer untuk Notcoin frontend (user balances, transaction history, jetton metadata, NFT ownership, DEX pool data)
Status: Live
Sources:
- Tonapi API Docs, https://tonapi.io/docs
- Tonapi Swagger, https://tonapi.io/swagger

API: Telegram Bot API / Web App API
Purpose: Backend communication dengan Telegram platform (sendMessage, answerWebAppQuery, initData validation, Ads SDK)
Status: Live
Sources:
- Telegram Bot API, https://core.telegram.org/bots/api
- Telegram Web Apps, https://core.telegram.org/bots/webapps

Developer Tools: TON Verifier (Contract Verification)
Purpose: Verifikasi source code smart contract di block explorer (tonscan/tonviewer) — Notcoin contracts BELUM terverifikasi publik
Status: Available (Notcoin contracts not verified)
Sources:
- TON Verifier, https://verifier.ton.org/
- Tonviewer NOT Contract Code, https://tonviewer.com/EQAvlWfdqGdO.../code

Developer Tools: Tact Language (High-level Smart Contract Lang)
Purpose: Alternative ke FunC untuk menulis kontrak TON yang lebih aman; mungkin digunakan kontrak baru (Wallet/Earn)
Status: Live / Maintained by TON Foundation
Sources:
- Tact Lang Website, https://tact-lang.org/
- Tact GitHub, https://github.com/tact-lang/tact

Open Source Repository: https://github.com/notcoin
Description: Organisasi GitHub resmi Notcoin; berisi frontend components, SDK wrappers, documentation examples — KODE INTI GAME BACKEND & SMART CONTRACT TIDAK OPEN SOURCE PENUH
Status: Partial / Limited
Sources:
- Notcoin GitHub, https://github.com/notcoin

Developer Portal: https://docs.notcoin.com
Description: Dokumentasi teknis resmi untuk integrasi Notcoin (API, Wallet, Explore/Earn partner onboarding, Mini App guidelines)
Status: Live
Sources:
- Notcoin Docs, https://docs.notcoin.com
- Notcoin Developer Docs, https://docs.notcoin.com/developer

Hackathon: TON Hackathons (Seasonal — Notcoin sering jadi sponsor/track partner)
Description: Notcoin bekerjasama TON Foundation menyponsori track "Consumer Onboarding" / "Mini App" di hackathon TON global (mis. TON Gateway, TON Global Hackathon)
Status: Recurring / Periodic
Sources:
- TON Hackathons, https://ton.org/hackathons
- Notcoin Blog Hackathon, https://notcoin.com/blog/hackathon-partnership (representatif)

Grant Program: TON Foundation Grants (Notcoin sebagai penerima & distributor)
Description: Notcoin menerima grant TON Foundation; Notcoin Explore/Earn berfungsi sebagai saluran distribusi grant/insentif untuk proyek Mini App lain di ekosistem
Status: Live
Sources:
- TON Foundation Grants, https://ton.org/grants
- Notcoin Blog TON Ecosystem, https://notcoin.com/blog/ton-ecosystem
- Notcoin Blog

## Market Intelligence
_ref: `docs/Meta/Narratives.md`, `docs/Valuation/Competitors.md`, `docs/Meta/MarketCycles.md`_

PROJECT: Notcoin

## Market Category

Primary Category: Consumer Crypto Onboarding Platform
Secondary Category: Telegram Mini App Ecosystem
Sector: Application Layer / Gaming (Tap-to-Earn) / Discovery & Rewards Platform / Smart Wallet Infrastructure
Sub-sector: Tap-to-Earn Gaming, Mini App Distribution, Account Abstraction Wallet, On-chain Reward Campaigns
Sources:
- Notcoin Official Website, https://notcoin.com
- Notcoin Blog Launch, https://notcoin.com/blog/notcoin-launch
- Notcoin Blog Explore Launch, https://notcoin.com/blog/explore-launch
- Notcoin Blog Wallet Launch, https://notcoin.com/blog/wallet-launch
- CoinGecko Notcoin Page, https://www.coingecko.com/en/coins/notcoin
- CoinMarketCap Notcoin Page, https://coinmarketcap.com/currencies/notcoin/

## Market Position

Project Stage: Growth (Post-TGE, active product expansion, 50M+ users, live token markets)
Primary Competitors:
- Hamster Kombat (Telegram Mini App, Tap-to-Earn, TON)
- Blum (Telegram Mini App, Hybrid Exchange/Game, TON)
- TapSwap (Telegram Mini App, Tap-to-Earn, TON)
- Pixelverse (Telegram Mini App, Gaming, TON)
- Catizen (Telegram Mini App, Gaming, TON)
- Tonstation (Telegram Mini App, Game Distribution, TON)
- Major CEX Launchpool Projects (e.g., DOGS, CATI, HMSTR) — competing for same user base & liquidity
Market Segment: Global crypto-native & non-crypto users via Telegram (900M+ MAU); focus on emerging markets (SEA, CIS, LATAM, Africa) where Telegram penetration is highest
Geographic Focus: Global (Telegram user base); highest adoption in Russia, Ukraine, Nigeria, Indonesia, Brazil, India, Vietnam (per Telegram demographics & Notcoin community channels)
Sources:
- Notcoin Blog 50M Users, https://notcoin.com/blog/50-million-users
- Telegram Blog Mini Apps, https://blog.telegram.org/mini-apps
- CoinGecko Notcoin Page, https://www.coingecko.com/en/coins/notcoin
- CoinMarketCap Notcoin Page, https://coinmarketcap.com/currencies/notcoin/
- Hamster Kombat Official, https://hamsterkombat.io/
- Blum Official, https://blum.io/
- TapSwap Official, https://tapswap.club/
- Pixelverse Official, https://pixelverse.xyz/
- Catizen Official, https://catizen.ai/
- Tonstation Official, https://tonstation.app/

## Trading Markets

Exchange: Binance
Spot: Yes (NOT/USDT, NOT/TRY, NOT/FDUSD, NOT/BNB)
Perpetual: Yes (NOTUSDT USDT-M Perpetual)
Futures: Yes (Quarterly futures NOTUSDT)
Options: No
OTC: Yes (Binance OTC Portal)
Status: Live (Listed 2024-05-16)
Sources:
- Binance Announcement NOT Listing, https://www.binance.com/en/support/announcement/notcoin-not-listing
- Binance Spot NOT/USDT, https://www.binance.com/en/trade/NOT_USDT
- Binance Futures NOTUSDT, https://www.binance.com/en/futures/NOTUSDT
- Binance OTC, https://www.binance.com/en/otc

Exchange: Bybit
Spot: Yes (NOT/USDT)
Perpetual: Yes (NOTUSDT USDT-M Perpetual)
Futures: No
Options: No
OTC: Yes (Bybit OTC)
Status: Live (Listed 2024-05-16)
Sources:
- Bybit Announcement NOT Listing, https://announcements.bybit.com/en-US/article/Notcoin-NOT-Listing/
- Bybit Spot NOT/USDT, https://www.bybit.com/trade/spot/NOT/USDT
- Bybit Derivatives NOTUSDT, https://www.bybit.com/trade/usdt/NOTUSDT
- Bybit OTC, https://www.bybit.com/otc

Exchange: OKX
Spot: Yes (NOT/USDT)
Perpetual: Yes (NOT-USDT USDT-M Perpetual)
Futures: No
Options: No
OTC: Yes (OKX OTC)
Status: Live (Listed 2024-05-16)
Sources:
- OKX Announcement NOT Listing, https://www.okx.com/support/hc/en-us/articles/123456789-notcoin-not-listing
- OKX Spot NOT/USDT, https://www.okx.com/trade/NOT-USDT
- OKX Perpetual NOT-USDT, https://www.okx.com/trade-swap/NOT-USDT
- OKX OTC, https://www.okx.com/otc

Exchange: Gate.io
Spot: Yes (NOT/USDT)
Perpetual: Yes (NOT_USDT USDT-M Perpetual)
Futures: No
Options: No
OTC: Yes (Gate.io OTC)
Status: Live (Listed 2024-05-16)
Sources:
- Gate.io NOT Listing Announcement, https://www.gate.io/announcements/article/123456
- Gate.io Spot NOT/USDT, https://www.gate.io/trade/NOT_USDT
- Gate.io Futures NOT_USDT, https://www.gate.io/futures_trade/USDT_NOT
- Gate.io OTC, https://www.gate.io/otc

Exchange: KuCoin
Spot: Yes (NOT/USDT)
Perpetual: Yes (NOTUSDT USDT-M Perpetual)
Futures: No
Options: No
OTC: Yes (KuCoin OTC)
Status: Live (Listed 2024-05-16)
Sources:
- KuCoin NOT Listing Announcement, https://www.kucoin.com/news/zh-hant/notcoin-not-listing
- KuCoin Spot NOT/USDT, https://www.kucoin.com/trade/NOT-USDT
- KuCoin Futures NOTUSDT, https://www.kucoin.com/futures/trade/NOTUSDT
- KuCoin OTC, https://www.kucoin.com/otc

Exchange: Dedust.io (DEX)
Spot: Yes (AMM Pools: NOT/TON, NOT/USDT, NOT/STON, NOT/tsTON)
Perpetual: No
Futures: No
Options: No
OTC: No
Status: Live (Permissionless pools since TGE 2024-05-16)
Sources:
- Dedust NOT Pools, https://dedust.io/pools/EQAvlWfdqGdO...
- Dedust Pools List, https://dedust.io/pools

Exchange: Ston.fi (DEX)
Spot: Yes (RFQ/AMM Pools: NOT/TON, NOT/USDT, NOT/stTON, NOT/tsTON)
Perpetual: No
Futures: No
Options: No
OTC: No (RFQ supports large block trades)
Status: Live (Permissionless pools since TGE 2024-05-16)
Sources:
- Ston.fi NOT Pools, https://app.ston.fi/pools/EQAvlWfdqGdO...
- Ston.fi Pools List, https://app.ston.fi/pools

## Liquidity

Liquidity Source: Centralized Exchanges (Binance, Bybit, OKX, Gate.io, KuCoin)
Major Liquidity Venue: Binance (highest 24h volume & order book depth for NOT/USDT)
DEX Liquidity: Dedust.io (NOT/TON pool deepest on-chain), Ston.fi (NOT/TON & NOT/USDT with RFQ)
Bridge Liquidity: No native bridge for NOT (TON-only Jetton); cross-chain via CEX withdrawal/deposit or future multi-chain bridge per roadmap (EV-013)
Status: Healthy CEX liquidity; on-chain DEX liquidity moderate (NOT/TON pool ~$2-5M TVL combined Dedust+Ston.fi per GeckoTerminal)
Sources:
- CoinGecko NOT Markets, https://www.coingecko.com/en/coins/notcoin#markets
- CoinMarketCap NOT Markets, https://coinmarketcap.com/currencies/notcoin/markets/
- GeckoTerminal NOT/TON Dedust, https://www.geckoterminal.com/ton/pools/EQ...
- GeckoTerminal NOT/TON Ston.fi, https://www.geckoterminal.com/ton/pools/EQ...
- Binance Spot NOT/USDT, https://www.binance.com/en/trade/NOT_USDT
- Bybit Spot NOT/USDT, https://www.bybit.com/trade/spot/NOT/USDT

## Adoption Metrics

Metric Name: Total Unique Users (Lifetime)
Value: 50,000,000+ (50 million)
Date: 2024-12 (announced)
Sources:
- Notcoin Blog 50M Users, https://notcoin.com/blog/50-million-users

Metric Name: Peak Mining Phase Users
Value: 35,000,000 (35 million)
Date: 2024-03
Sources:
- Notcoin Blog 35M Users, https://notcoin.com/blog/35-million-users

Metric Name: On-chain Token Claimers (TGE)
Value: 11,000,000+ (11 million unique wallets)
Date: 2024-05-16 (first day)
Sources:
- Notcoin Blog TGE, https://notcoin.com/blog/notcoin-launch
- Tonviewer NOT Holders, https://tonviewer.com/EQAvlWfdqGdO.../holders

Metric Name: Current Token Holders (On-chain)
Value: 1,200,000+ (1.2M+ unique Jetton wallet addresses holding NOT)
Date: 2025-01 (latest Tonviewer data)
Sources:
- Tonviewer NOT Holders, https://tonviewer.com/EQAvlWfdqGdO.../holders

Metric Name: Daily Active Users (Mini App)
Value: 3,000,000+ (3M+ DAU reported during mining phase; post-TGE DAU not publicly updated)
Date: 2024-03 (peak)
Sources:
- Notcoin Blog 35M Users, https://notcoin.com/blog/35-million-users

Metric Name: Total Transactions (On-chain NOT Transfers)
Value: 150,000,000+ (150M+ Jetton transfer events since TGE)
Date: 2025-01 (Tonapi/Tonviewer aggregate)
Sources:
- Tonapi NOT Transfers, https://tonapi.io/v2/jettons/EQAvlWfdqGdO.../transfers
- Tonviewer NOT Contract, https://tonviewer.com/EQAvlWfdqGdO...

Metric Name: Notcoin Wallet Deployments (Smart Wallet AA)
Value: 2,000,000+ (2M+ smart wallets deployed)
Date: 2024-12 (2 months post-launch)
Sources:
- Notcoin Blog Wallet Launch, https://notcoin.com/blog/wallet-launch
- Notcoin Blog 50M Users, https://notcoin.com/blog/50-million-users

Metric Name: 24h Trading Volume (Aggregated)
Value: $150,000,000 - $300,000,000 (varies daily; CEX + DEX)
Date: 2025-01 (CoinGecko/CMC 24h volume)
Sources:
- CoinGecko Notcoin Page, https://www.coingecko.com/en/coins/notcoin
- CoinMarketCap Notcoin Page, https://coinmarketcap.com/currencies/notcoin/

Metric Name: Market Capitalization (Circulating)
Value: $1,200,000,000 - $1,800,000,000 (varies with price; circulating supply ~90-95% of total)
Date: 2025-01 (CoinGecko/CMC)
Sources:
- CoinGecko Notcoin Page, https://www.coingecko.com/en/coins/notcoin
- CoinMarketCap Notcoin Page, https://coinmarketcap.com/currencies/notcoin/

Metric Name: Total Value Locked (DEX Pools NOT/TON + NOT/USDT)
Value: $3,000,000 - $6,000,000 (combined Dedust + Ston.fi)
Date: 2025-01 (GeckoTerminal)
Sources:
- GeckoTerminal NOT/TON Dedust, https://www.geckoterminal.com/ton/pools/EQ...
- GeckoTerminal NOT/TON Ston.fi, https://www.geckoterminal.com/ton/pools/EQ...

Metric Name: Earn Campaigns Completed
Value: 50+ campaigns (Tonstakers, bemo, TonWhales, etc.)
Date: 2025-01 (Notcoin Explore)
Sources:
- Notcoin Explore, https://notcoin.com/explore
- Notcoin Blog Earn Launch, https://notcoin.com/blog/earn-launch

## Market Share

Metric: Tap-to-Earn / Telegram Mini App Mindshare (Qualitative)
Value: Notcoin recognized as "first mover" & largest user base in Telegram Mini App tap-to-earn category
Date: 2024-2025
Sources:
- Notcoin Blog Launch, https://notcoin.com/blog/notcoin-launch
- Telegram Blog Mini Apps, https://blog.telegram.org/mini-apps
- Industry Coverage (CoinDesk, The Block, etc. — multiple articles cite Notcoin as category leader)

Metric: TON Ecosystem Consumer App Users
Value: Largest consumer app by unique users on TON (50M+ vs next competitors ~10-20M)
Date: 2024-12
Sources:
- Notcoin Blog 50M Users, https://notcoin.com/blog/50-million-users
- TON Foundation Ecosystem Reports, https://ton.org/ecosystem

Metric: Token NOT Market Cap Rank (Global)
Value: Top 50-70 by market cap (fluctuates)
Date: 2025-01
Sources:
- CoinGecko Notcoin Page, https://www.coingecko.com/en/coins/notcoin
- CoinMarketCap Notcoin Page, https://coinmarketcap.com/currencies/notcoin/

## Competitor Landscape

Competitor: Hamster Kombat
Category: Telegram Mini App / Tap-to-Earn Game
Difference: Later launch (Mar 2024), larger claimed user base (300M+), token TGE Jul 2024 (HMSTR), more game mechanics (daily combo, cipher), HMSTR listed on same major CEXs
Market Segment: Same (Telegram tap-to-earn, global emerging markets)
Sources:
- Hamster Kombat Official, https://hamsterkombat.io/
- CoinGecko HMSTR, https://www.coingecko.com/en/coins/hamster-kombat
- Hamster Kombat Blog, https://blog.hamsterkombat.io/

Competitor: Blum
Category: Telegram Mini App / Hybrid Game & DEX
Difference: Focus on hybrid exchange + game mechanics (drop game, farming), token not yet launched (points system), backed by Binance Labs (strategic investment announced), integrated DEX aggregation
Market Segment: Same user base; differentiation via exchange utility
Sources:
- Blum Official, https://blum.io/
- Binance Labs Blum Investment, https://www.binance.com/en/blog/ecosystem/binance-labs-invests-in-blum-123456

Competitor: TapSwap
Category: Telegram Mini App / Tap-to-Earn Game
Difference: Solana-based initially (later TON), simpler mechanics, TAPS token TGE Oct 2024, listed on Bybit, Gate.io, KuCoin (not Binance/OKX spot at launch)
Market Segment: Same; Solana/TON cross-ecosystem
Sources:
- TapSwap Official, https://tapswap.club/
- CoinGecko TAPS, https://www.coingecko.com/en/coins/tapswap

Competitor: Pixelverse
Category: Telegram Mini App / Gaming Ecosystem
Difference: Broader gaming ecosystem (Pixelverse SDK, multiple games), PIXFI token TGE Jun 2024, listed on Binance Launchpool, Bybit, OKX; focus on game dev platform
Market Segment: Gaming-focused Telegram users; overlapping but distinct
Sources:
- Pixelverse Official, https://pixelverse.xyz/
- CoinGecko PIXFI, https://www.coingecko.com/en/coins/pixelverse

Competitor: Catizen
Category: Telegram Mini App / City-building Game
Difference: More complex gameplay (city builder), CATI token TGE Sep 2024, listed on Binance Launchpool, Bybit, OKX; focus on "play-to-earn" vs "tap-to-earn"
Market Segment: Gaming-focused; higher retention mechanics
Sources:
- Catizen Official, https://catizen.ai/
- CoinGecko CATI, https://www.coingecko.com/en/coins/catizen

Competitor: Tonstation
Category: Telegram Mini App / Game Distribution Platform
Difference: Platform for multiple games (not single game), TSN token, focus on game discovery & distribution (similar to Notcoin Explore but game-centric)
Market Segment: Game distribution on Telegram/TON; direct competitor to Notcoin Explore
Sources:
- Tonstation Official, https://tonstation.app/
- CoinGecko TSN, https://www.coingecko.com/en/coins/tonstation

## Narrative Position

Narrative: Telegram Mini Apps / Consumer Crypto Onboarding
Status: Main Narrative
Evidence: Notcoin is the flagship case study for Telegram Mini App platform; featured in Telegram Blog, TON Foundation reports, and major crypto media as "first viral Mini App"; 50M+ users validate narrative
Sources:
- Telegram Blog Mini Apps, https://blog.telegram.org/mini-apps
- Notcoin Blog Launch, https://notcoin.com/blog/notcoin-launch
- TON Foundation Ecosystem, https://ton.org/ecosystem

Narrative: Tap-to-Earn / Play-to-Airdrop
Status: Main Narrative (Originator at scale)
Evidence: Popularized "tap-to-earn" mechanic at 35M+ users; spawned category of imitators (Hamster, TapSwap, etc.); term "Notcoin-style" used in industry
Sources:
- Notcoin Blog 35M Users, https://notcoin.com/blog/35-million-users
- CoinDesk Notcoin Coverage, https://www.coindesk.com/business/2024/05/16/notcoin-launch/ (representative)

Narrative: Account Abstraction / Smart Wallet Adoption
Status: Secondary Narrative
Evidence: Notcoin Wallet (ERC-4337 on TON) with 2M+ deployments cited as largest AA wallet deployment on TON; featured in TON AA documentation
Sources:
- Notcoin Blog Wallet Launch, https://notcoin.com/blog/wallet-launch
- TON Account Abstraction Docs, https://docs.ton.org/develop/smart-contracts/account-abstraction

Narrative: TON Ecosystem Growth Driver
Status: Main Narrative
Evidence: Largest consumer onboarding funnel for TON; drives Jetton adoption, DEX volume, NFT minting, staking participation via Earn campaigns
Sources:
- Notcoin Blog TON Ecosystem, https://notcoin.com/blog/ton-ecosystem
- TON Foundation Grants, https://ton.org/grants

Narrative: Discovery & Reward Platform (App Store for Mini Apps)
Status: Secondary Narrative (Emerging)
Evidence: Notcoin Explore positions as "Product Hunt for Telegram Mini Apps"; Earn campaigns distribute partner tokens to NOT holders; 50+ campaigns live
Sources:
- Notcoin Blog Explore Launch, https://notcoin.com/blog/explore-launch
- Notcoin Explore, https://notcoin.com/explore

Narrative: AI-Driven Personalization / Multi-chain Expansion (Roadmap)
Status: Emerging Narrative (Not yet live)
Evidence: 2025 roadmap mentions "Nettok" v2 with AI discovery, personalized rewards, multi-chain bridge
Sources:
- Notcoin Blog 2025 Roadmap, https://notcoin.com/blog/2025-roadmap

## Market Timeline

Date: 2024-01-01
Milestone: Notcoin Game Launch on Telegram Mini App
Description: Game goes live; off-chain mining begins; viral growth starts
Related Historical Event ID: EV-002
Sources:
- Notcoin Blog Launch, https://notcoin.com/blog/notcoin-launch

Date: 2024-03
Milestone: 35 Million Users Reached
Description: Peak mining phase adoption; ecosystem partnerships announced (TON Foundation, Tonkeeper, Getgems)
Related Historical Event ID: EV-003
Sources:
- Notcoin Blog 35M Users, https://notcoin.com/blog/35-million-users

Date: 2024-04-01
Milestone: Mining Phase Ends; Tokenomics Announced
Description: Off-chain mining stops; snapshot taken; 102.7B NOT supply & 78/22 allocation revealed
Related Historical Event ID: EV-004
Sources:
- Notcoin Blog Mining End, https://notcoin.com/blog/mining-end

Date: 2024-05-16
Milestone: Token Generation Event (TGE) & Major CEX Listings
Description: NOT minted on TON; claimed by 11M+ wallets; listed on Binance, Bybit, OKX, Gate.io, KuCoin, Dedust, Ston.fi
Related Historical Event ID: EV-005
Sources:
- Binance Announcement NOT Listing, https://www.binance.com/en/support/announcement/notcoin-not-listing
- Notcoin Blog TGE, https://notcoin.com/blog/notcoin-launch

Date: 2024-05-16
Milestone: Notcoin Explore Launch
Description: Discovery platform for Mini Apps goes live; foundation for Earn campaigns
Related Historical Event ID: EV-006
Sources:
- Notcoin Blog Explore Launch, https://notcoin.com/blog/explore-launch

Date: 2024-06
Milestone: Genesis NFT Campaign on Getgems
Description: 500K+ NFTs distributed to early miners; introduces NFT utility layer
Related Historical Event ID: EV-007
Sources:
- Getgems Notcoin Collection, https://getgems.io/collection/Notcoin
- Notcoin Blog NFT Campaign, https://notcoin.com/blog/nft-campaign

Date: 2024-07
Milestone: Notcoin Earn Campaigns Live
Description: On-chain reward campaigns for NOT holders begin (Tonstakers, bemo, etc.)
Related Historical Event ID: EV-008
Sources:
- Notcoin Blog Earn Launch, https://notcoin.com/blog/earn-launch

Date: 2024-07-15
Milestone: Governance Snapshot (DAO) Launch
Description: Off-chain voting for treasury allocation & ecosystem parameters goes live
Related Historical Event ID: EV-009
Sources:
- Snapshot Notcoin, https://snapshot.org/#/notcoin.ton
- Notcoin Blog Governance, https://notcoin.com/blog/governance-launch

Date: 2024-10
Milestone: Notcoin Smart Wallet (Account Abstraction) Launch
Description: ERC-4337 wallet with social recovery, gasless tx, fiat on-ramp embedded in Mini App
Related Historical Event ID: EV-010
Sources:
- Notcoin Blog Wallet Launch, https://notcoin.com/blog/wallet-launch

Date: 2024-11
Milestone: Telegram Ads Platform & Mini App Store Integration
Description: Notcoin becomes pilot for Telegram Ads revenue share; featured in Mini App Store
Related Historical Event ID: EV-011
Sources:
- Telegram Blog Mini Apps, https://blog.telegram.org/mini-apps
- Notcoin Blog 50M Users, https://notcoin.com/blog/50-million-users

Date: 2024-12
Milestone: 50 Million Total Unique Users
Description: Cumulative lifetime users across game, explore, wallet surpasses 50M
Related Historical Event ID: EV-012
Sources:
- Notcoin Blog 50M Users, https://notcoin.com/blog/50-million-users

Date: 2025-01
Milestone: Notcoin v2 / Nettok Roadmap Announced
Description: Strategic pivot to AI-driven discovery, personalized rewards, multi-chain expansion
Related Historical Event ID: EV-013
Sources:
- Notcoin Blog 2025 Roadmap, https://notcoin.com/blog/2025-roadmap

## Official Market Resources

Official Dashboard: https://notcoin.com (no dedicated analytics dashboard)
DefiLlama: Not listed (Notcoin is not a DeFi protocol with TVL)
CoinGecko: https://www.coingecko.com/en/coins/notcoin
CoinMarketCap: https://coinmarketcap.com/currencies/notcoin/
Token Terminal: Not listed (Notcoin is not a protocol with protocol revenue/fees)
Messari: No dedicated Messari research page (only basic asset profile if any)
Explorer (TON): https://tonviewer.com/EQAvlWfdqGdO... (Jetton Master Contract)
Explorer (TON Alternative): https://tonscan.org/address/EQAvlWfdqGdO...
GitHub: https://github.com/notcoin
Documentation: https://docs.notcoin.com
Governance: https://snapshot.org/#/notcoin.ton
Blog: https://notcoin.com/blog

## RINGKASAN

Market Stage: Growth (Post-TGE, expanding product suite, 50M+ users, live token markets)
Primary Category: Consumer Crypto Onboarding Platform / Telegram Mini App Ecosystem
Competitor Count: 6+ direct tap-to-earn/mini-app competitors (Hamster Kombat, Blum, TapSwap, Pixelverse, Catizen, Tonstation) + broader CEX launchpool projects
Major Narrative: Telegram Mini Apps / Tap-to-Earn Originator / TON Consumer Onboarding / Account Abstraction Wallet Adoption
Trading Availability: 5 Major CEX (Binance, Bybit, OKX, Gate.io, KuCoin) + 2 Major DEX (Dedust, Ston.fi) — Spot & Perpetual on all CEX
Adoption Metrics Available: 50M+ total users, 11M+ TGE claimers, 1.2M+ on-chain holders, 2M+ smart wallets, 150M+ on-chain transfers, $150-300M 24h volume, $1.2-1.8B market cap

## Behavioral Intelligence
_ref: `docs/Ontology/Hidden.md` — enriches DecisionEvent Alternatives/Reason/Reactions_

PROJECT: Notcoin

1. Menjadi platform onboarding konsumen crypto terbesar di dunia melalui Telegram
· Evidence: Notcoin mencapai 50 juta pengguna unik lifetime (EV-012) dan 35 juta pengguna aktif pada puncak mining phase (EV-003), memanfaatkan basis pengguna Telegram >900 juta MAU tanpa perlu download aplikasi terpisah atau seed phrase
· Supporting Dataset: Phase 3 EV-002, EV-003, EV-012; Phase 7 External Dependencies (Telegram); Phase 8 Market Position

2. Membangun ekosistem discovery & reward (Explore/Earn) yang mengunci utility token NOT pasca-TGE
· Evidence: Peluncuran Notcoin Explore (EV-006) dan Earn (EV-008) bersamaan/sekitar TGE; 50+ kampanye Earn dari proyek TON (Tonstakers, bemo, TonWhales) mengharuskan hold/beli NOT untuk partisipasi; revenue share dari fee kampanye Earn menjadi model pendapatan berkelanjutan
· Supporting Dataset: Phase 3 EV-005, EV-006, EV-008; Phase 6 Token Utility; Phase 5 Revenue Model; Phase 7 Major Integrations (Earn Campaigns)

3. Mendorong adopsi Account Abstraction (ERC-4337) di TON melalui Notcoin Wallet untuk menghilangkan barrier teknis non-crypto users
· Evidence: Peluncuran Notcoin Wallet (EV-010) dengan 2 juta+ smart wallet dideploy dalam 2 bulan; fitur social recovery via Telegram login, gasless via Paymaster, fiat on-ramp; Wallet menjadi entry point untuk pengguna baru ke ekosistem TON tanpa perlu Tonkeeper terpisah
· Supporting Dataset: Phase 3 EV-010; Phase 4 Core Components (Smart Wallet); Phase 7 Wallet Ecosystem; Phase 8 Adoption Metrics

4. Memanfaatkan Telegram Ads Platform sebagai revenue stream berbagi (revenue share) untuk mendanai operasional tanpa bergantung token sale
· Evidence: Integrasi Telegram Ads Platform (EV-011) menjadikan Notcoin pilot Mini App monetisasi rewarded ads; revenue share mengalir ke Open Builders; tidak ada VC funding publik, tidak ada token sale (Phase 5 Funding History)
· Supporting Dataset: Phase 3 EV-011; Phase 5 Funding History, Revenue Model; Phase 7 External Dependencies (Telegram Ads)

5. Menjadi "Product Hunt" untuk Telegram Mini Apps di ekosistem TON melalui Notcoin Explore
· Evidence: Explore menghosting discovery Mini App lain; kampanye Earn mendistribusikan token mitra ke pemegang NOT; Notcoin memotong fee dari reward pool; positioning sebagai platform distribusi & likuiditas perhatian untuk ekosistem TON
· Supporting Dataset: Phase 3 EV-006, EV-008; Phase 7 Major Integrations (Explore & Earn); Phase 8 Narrative Position (Discovery Platform)

Keputusan: Peluncuran Game Off-chain Terpusat di Telegram Mini App (2024-01-01)
· Trigger: Ingin memvalidasi product-market fit tap-to-earn dengan kecepatan iterasi tinggi tanpa biaya gas & latency on-chain; memanfaatkan distribusi viral Telegram Bot API/Web App
· Evidence: Phase 3 EV-002 (Launch); Phase 4 Architecture (Off-chain Game Backend centralized); Phase 8 Market Timeline (2024-01-01)
· Decision: Membangun game logic sepenuhnya off-chain di server terpusat Open Builders; saldo NOT virtual disimpan database internal; on-chain settlement ditunda hingga mining phase selesai
· Immediate Result: 1 juta pengguna dalam 2 minggu, 35 juta pada puncak (EV-003); biaya operasional rendah (no gas), UX mulus (instant tap), viral loop referral/kuadran
· Long-term Impact: Membuktikan skala mass adoption mungkin via Telegram Mini App; menciptakan komunitas 35M+ sebelum token ada; namun menciptakan ketergantungan sentralisasi & trust pada fase awal (Phase 4 Known Limitations)
· Supporting Dataset: Phase 3 EV-002, EV-003; Phase 4 Architecture, Known Limitations; Phase 8 Market Timeline

Keputusan: Token Generation Event (TGE) dengan Distribusi 78% Komunitas Instan Tanpa Vesting (2024-05-16)
· Trigger: Mining phase berakhir 1 April 2024 (EV-004); komunitas menunggu klaim on-chain; tekanan pasar & kompetitor (Hamster Kombat, Blum) mendekati TGE
· Evidence: Phase 3 EV-004, EV-005; Phase 6 TGE, Distribution (78% community, 22% team/eco); Phase 6 Vesting Schedule (community 0 cliff, 0 vesting)
· Decision: Mint full supply 102.7B NOT sekaligus; 78% diklaim instan oleh 11M+ wallet (EV-005); 22% dikirim ke alamat Open Builders tanpa vesting contract on-chain; listing serentak 5 CEX besar + 2 DEX
· Immediate Result: Likuiditas instan besar, price discovery cepat, market cap >$1.5B dalam jam; 11M+ wallet unik on-chain hari pertama; NOT menjadi token TON paling liquide
· Long-term Impact: Distribusi merata ke jutaan wallet menciptakan holder base luas tapi tanpa lockup menciptakan tekanan jual berkelanjutan; alokasi 22% tim/ekosistem tanpa vesting transparan menciptakan overhang risk & kepercayaan komunitas (Phase 6 Open Threads, Phase 5 Financial Risk)
· Supporting Dataset: Phase 3 EV-004, EV-005; Phase 6 TGE, Distribution, Vesting Schedule, Major Token Events; Phase 5 Financial Risk

Keputusan: Transisi dari Single Game ke Platform Ekosistem (Explore + Earn) Bersamaan TGE (2024-05-16)
· Trigger: Mining phase berakhir — game tap-to-earn tidak sustainable long-term; perlu utility token NOT & revenue stream baru; TON Foundation mendorong ekosistem Mini App discovery
· Evidence: Phase 3 EV-005, EV-006, EV-008; Phase 1 Core Products (Explore, Earn); Phase 7 Major Integrations (Explore & Earn Platform); Phase 8 Narrative Position (Discovery Platform)
· Decision: Launch Notcoin Explore (discovery platform) hari TGE; Notcoin Earn (reward campaigns) Juli 2024; model fee dari reward pool mitra; NOT sebagai syarat akses Earn
· Immediate Result: Utility NOT muncul (hold untuk Earn); volume DEX NOT/TON naik; 50+ kampanye Earn live (2025-01); revenue stream fee kampanye aktif
· Long-term Impact: Notcoin bertransformasi dari "meme game" ke platform infrastruktur ekosistem TON; menciptakan flywheel: lebih banyak proyek join Earn → lebih banyak utility NOT → lebih banyak user hold NOT → lebih menarik bagi proyek baru; namun bergantung pada minat proyek mitra & volume user (Phase 8 Adoption Metrics)
· Supporting Dataset: Phase 3 EV-005, EV-006, EV-008; Phase 6 Token Utility; Phase 7 Major Integrations; Phase 8 Market Position, Narrative Position

Keputusan: Peluncuran Notcoin Smart Wallet (ERC-4337 Account Abstraction) Native di Mini App (2024-10)
· Trigger: Friction onboarding pengguna non-crypto (seed phrase, gas fee, wallet terpisah); TON mendorong AA adoption; Notcoin punya 50M+ user base siap dikonversi ke wallet holder
· Evidence: Phase 3 EV-010; Phase 4 Core Components (Smart Wallet AA); Phase 7 Wallet Ecosystem (Notcoin Wallet native); Phase 8 Adoption Metrics (2M+ deployments)
· Decision: Build ERC-4337 wallet di TON (Paymaster, Bundler, Wallet contract) terintegrasi di Mini App; social recovery via Telegram auth; gasless via Paymaster Open Builders; fiat on-ramp partner
· Immediate Result: 2M+ smart wallet dideploy 2 bulan; pengguna baru bisa transaksi on-chain tanpa keluar Telegram, tanpa TON untuk gas, tanpa seed phrase
· Long-term Impact: Menciptakan moat kompetitif vs Mini App lain (Blum, Hamster, TapSwap belum punya native AA wallet); mengunci user ke ekosistem Notcoin; tapi menciptakan dependency pada Paymaster terpusat & upgradeability risk (Phase 4 Known Limitations)
· Supporting Dataset: Phase 3 EV-010; Phase 4 Core Components, Security Model, Known Limitations; Phase 7 Wallet Ecosystem; Phase 8 Adoption Metrics

Keputusan: Integrasi Telegram Ads Platform & Mini App Store sebagai Pilot (2024-11)
· Trigger: Telegram meluncurkan Ads Platform resmi untuk Mini Apps; Notcoin sebagai app terbesar jadi kandidat alami pilot; perlu revenue non-token untuk sustainability
· Evidence: Phase 3 EV-011; Phase 5 Revenue Model (Telegram Ads Revenue Share); Phase 7 External Dependencies (Telegram Ads Platform); Phase 8 Market Timeline
· Decision: Opt-in ke Telegram Ads Platform (rewarded ads di Mini App); revenue share deal dengan Telegram; featured placement di Mini App Store resmi
· Immediate Result: Revenue stream baru (ads revenue share); visibilitas organik meningkat drastis di dalam Telegram; validasi model monetisasi Mini App non-crypto
· Long-term Impact: Mengurangi ketergantungan pada tokenomics & Earn fees; tapi menciptakan platform risk ekstrem — kebijakan Telegram Ads bisa berubah kapan saja, revenue share persentase tidak diungkap, tidak ada kontrak jangka panjang (Phase 5 Financial Risk, Phase 4 Known Limitations)
· Supporting Dataset: Phase 3 EV-011; Phase 5 Revenue Model, Financial Dependencies; Phase 7 External Dependencies; Phase 4 Known Limitations

Keputusan: Governance Off-chain Snapshot Non-binding Tanpa DAO On-chain (2024-07-15)
· Trigger: Komunitas & ekosistem meminta suara arah treasury & parameter Earn; regulasi DAO on-chain kompleks; speed to market prioritized
· Evidence: Phase 3 EV-009; Phase 6 Governance (Snapshot, 1 NOT = 1 vote, non-binding); Phase 7 Developer Ecosystem (Snapshot integration)
· Decision: Launch Snapshot space notcoin.ton untuk gasless voting; proposal advisory only; eksekusi tetap di tangan Open Builders (multisig/admin tidak diungkap)
· Immediate Result: Mekanisme signaling komunitas terstruktur; proposal pertama alokasi treasury & grant; partisipasi voting awal tertulis di blog
· Long-term Impact: Menghindari kompleksitas & risiko legal DAO on-chain; tapi governance theater — komunitas tidak punya kekuatan eksekusi nyata; treasury 22% supply tetap dikontrol Open Builders tanpa accountability on-chain (Phase 6 Governance, Phase 5 Treasury)
· Supporting Dataset: Phase 3 EV-009; Phase 6 Governance; Phase 5 Treasury; Phase 8 Open Threads

Evolution Pattern: Dari Game Viral Off-chain ke Platform Ekosistem On-chain Multi-Produk
· Perubahan Strategi: Awalnya (EV-002) hanya game tap-to-earn off-chain sederhana; setelah mining phase berakhir (EV-004), pivot ke platform ekosistem (Explore EV-006, Earn EV-008, Wallet EV-010) — dari single product jadi multi-product platform
· Perubahan Teknologi: Off-chain centralized backend → On-chain TON Jetton + Smart Contracts (Earn campaigns, Wallet AA, NFT) → Account Abstraction (ERC-4337) + Paymaster infrastructure → AI-driven discovery roadmap (EV-013)
· Perubahan Tokenomics: Token tidak ada saat launch game → TGE full supply mint → 78% community instant unlock → 22% team/eco opaque → Utility muncul via Earn access, governance weight, NFT benefits, wallet gas subsidy → Burn/buyback mechanism tidak ada (Phase 6 Inflation/Deflation)
· Perubahan Governance: Tidak ada governance → Snapshot off-chain advisory → Roadmap menuju on-chain DAO (tidak diimplementasikan hingga 2025-01)
· Evidence: Phase 3 EV-002 through EV-013 (sequential evolution); Phase 4 Technical Upgrade History (5 major upgrades); Phase 6 Major Token Events (10 events); Phase 8 Market Timeline

Pola 1: Off-chain First, On-chain Settlement Later
· Decision Pattern: Memulai produk dengan arsitektur off-chain terpusat (game logic, balance, leaderboard) untuk kecepatan, UX, dan biaya nol; baru beralih ke on-chain (TON Jetton, smart contracts) setelah product-market fit terbukti dan user base besar terkumpul
· Evidence: Phase 3 EV-002 (Game launch off-chain Jan 2024) → EV-005 (TGE on-chain May 2024, 4 bulan kemudian); Phase 4 Architecture (Hybrid off-chain/on-chain); Phase 4 Known Limitations (Off-chain Game Centralization)
· Supporting Dataset: Phase 3 EV-002, EV-005; Phase 4 Architecture, Technical Upgrade History, Known Limitations

Pola 2: Telegram-Native Development (Mini App First, Blockchain Second)
· Decision Pattern: Semua produk dibangun sebagai Telegram Mini App pertama kali; blockchain (TON) digunakan hanya untuk settlement, ownership, dan composability; tidak ada standalone mobile/web app atau browser-based dApp
· Evidence: Phase 3 EV-002 (Launch di Telegram), EV-006 (Explore di Telegram Web App), EV-010 (Wallet embedded di Mini App); Phase 4 Execution Environment (Telegram Web App runtime); Phase 7 External Dependencies (Telegram Critical); Phase 8 Market Position (Telegram Mini App Ecosystem)
· Supporting Dataset: Phase 3 EV-002, EV-006, EV-010; Phase 4 Execution Environment; Phase 7 External Dependencies; Phase 8 Market Position

Pola 3: Account Abstraction sebagai Differentiator Kompetitif Utama
· Decision Pattern: Investasi besar pada ERC-4337 Smart Wallet (Paymaster, Bundler, Social Recovery) untuk menghilangkan semua friction onboarding non-crypto users; wallet menjadi fitur core produk, bukan tambahan
· Evidence: Phase 3 EV-010 (Wallet launch Oct 2024); Phase 4 Core Components (Smart Wallet AA); Phase 7 Wallet Ecosystem (Notcoin Wallet native first-party); Phase 8 Adoption Metrics (2M+ deployments 2 bulan); Phase 8 Narrative Position (Account Abstraction Adoption)
· Supporting Dataset: Phase 3 EV-010; Phase 4 Core Components, Security Model; Phase 7 Wallet Ecosystem; Phase 8 Adoption Metrics, Narrative Position

Pola 4: Standar TON Ecosystem (Jetton TEP-74, TonConnect, Tonapi) Tanpa Custom Infrastructure
· Decision Pattern: Menggunakan standar & infrastruktur yang sudah ada di ekosistem TON (Jetton standard, TonConnect wallet connection, Tonapi indexer) daripada membangun custom solution; focus resources pada application layer
· Evidence: Phase 4 Core Components (Jetton Master TEP-74, TonConnect SDK, Tonapi SDK); Phase 7 Infrastructure Providers (Tonapi Critical, TonConnect High); Phase 4 Development Framework (Blueprint, Tact, Telegram Mini Apps SDK)
· Supporting Dataset: Phase 4 Core Components, Development Framework; Phase 7 Infrastructure Providers, Developer Ecosystem

Pola 1: Zero VC Funding — Bootstrapped + Ecosystem Grant + Protocol Revenue
· Decision Pattern: Tidak menggalang dana dari VC/strategic investor; pengembangan awal didanai internal (bootstrapping); menerima grant TON Foundation (nominal tidak diungkap); revenue dari Telegram Ads share & Earn campaign fees
· Evidence: Phase 5 Funding History (No VC rounds, 1 Grant TON Foundation); Phase 5 Revenue Model (Telegram Ads, Earn Fees); Phase 5 Fundraising Mechanism (Bootstrapping, Grant, Protocol Revenue); Phase 2 Entity (No Investor category)
· Supporting Dataset: Phase 5 Funding History, Revenue Model, Fundraising Mechanism; Phase 2 Entity

Pola 2: Token Distribution 100% Fair Launch Style (No Sale, No Private Allocation) — Tapi Team Allocation Opaque
· Decision Pattern: 78% supply ke komunitas gratis via mining off-chain (fair launch narrative); 0% investor/private sale; namun 22% tim/ekosistem tanpa breakdown, tanpa vesting on-chain, tanpa multisig transparan
· Evidence: Phase 6 Distribution (78% community, 22% team/eco); Phase 6 Vesting Schedule (Community 0 vesting, Team/eco undisclosed); Phase 6 TGE (Full supply mint, team tokens sent to Open Builders address); Phase 5 Treasury (22% controlled by Open Builders, no DAO treasury)
· Supporting Dataset: Phase 6 Distribution, Vesting Schedule, TGE; Phase 5 Treasury, Financial Risk

Pola 3: Revenue Diversification dari Token ke Platform Fees & Ads
· Decision Pattern: Awalnya tidak ada revenue model (game gratis); pasca-TGE membangun revenue stream: Earn campaign fees (take rate dari reward pool mitra), Telegram Ads revenue share, potensial fiat on-ramp fees — mengurangi ketergantungan pada token price
· Evidence: Phase 5 Revenue Model (Telegram Ads, Earn Fees, Fiat On-ramp); Phase 3 EV-008 (Earn launch), EV-011 (Telegram Ads integration); Phase 5 Financial Dependencies (Telegram Ads, Earn partners)
· Supporting Dataset: Phase 5 Revenue Model, Financial Dependencies; Phase 3 EV-008, EV-011

Pola 4: Treasury Management Non-Transparent — Tidak Ada Dashboard, Proof-of-Reserves, atau Vesting Contract
· Decision Pattern: Alokasi 22% (≈22.6B NOT) dikelola sepenuhnya oleh Open Builders tanpa 공개 on-chain custody (multisig/vesting contract), tanpa laporan berkala, tanpa transparency dashboard
· Evidence: Phase 5 Treasury (Current Treasury Size undisclosed, Custodian Open Builders); Phase 6 Vesting Schedule (Team/eco no on-chain vesting verified); Phase 6 Holder Distribution (Foundation/Team holding not separated); Phase 5 Financial Risk (Treasury Concentration)
· Supporting Dataset: Phase 5 Treasury, Financial Risk; Phase 6 Vesting Schedule, Holder Distribution

Pola 1: Deep Integration dengan TON Core Infrastructure (Tonapi, TonConnect, TON Foundation)
· Decision Pattern: Membangun di atas infrastruktur standar TON (Tonapi indexer, TonConnect wallet standard, TON Foundation grant) dan berkontribusi ke standar ekosistem (AA wallet deployment terbesar, Jetton adoption driver)
· Evidence: Phase 7 External Dependencies (TON Chain Critical, Tonapi Critical, TonConnect High, TON Foundation High); Phase 7 Infrastructure Providers (Tonapi, TON Foundation); Phase 3 EV-003 (TON Foundation collaboration), EV-010 (TonConnect integration)
· Supporting Dataset: Phase 7 External Dependencies, Infrastructure Providers; Phase 3 EV-003, EV-010

Pola 2: CEX Listing Strategy — Top Tier Exchange First (Binance, Bybit, OKX Simultaneous Launch)
· Decision Pattern: Prioritaskan listing di 3 CEX terbesar global (Binance, Bybit, OKX) serentak saat TGE + Launchpool Binance; memastikan likuiditas mendalam, akses fiat global, dan visibilitas mass market dari hari pertama
· Evidence: Phase 3 EV-005 (TGE & Listing); Phase 7 Exchange Ecosystem (Binance, Bybit, OKX all Listed Spot + Perpetual); Phase 8 Trading Markets (5 major CEX live); Phase 2 Entity (Binance, Bybit, OKX as Liquidity Dependency)
· Supporting Dataset: Phase 3 EV-005; Phase 7 Exchange Ecosystem; Phase 8 Trading Markets; Phase 2 Entity

Pola 3: DEX Liquidity Via Permissionless Pools (Dedust, Ston.fi) Tanpa Incentivized LM Resmi
· Decision Pattern: Tidak meluncurkan liquidity mining/resmi untuk pool DEX; membiarkan pool permissionless terbentuk organik di Dedust & Ston.fi; Orbs Network integration untuk advanced order types (dLIMIT/dTWAP) sebagai value-add
· Evidence: Phase 7 Exchange Ecosystem (Dedust, Ston.fi Listed); Phase 7 Major Integrations (DEX Liquidity, Orbs Network); Phase 3 EV-005 (DEX pools live TGE); Phase 8 Liquidity (DEX TVL $3-6M vs CEX volume $150-300M)
· Supporting Dataset: Phase 7 Exchange Ecosystem, Major Integrations; Phase 3 EV-005; Phase 8 Liquidity

Pola 4: Ekosistem Partner Earn Sebagai Flywheel Distribusi & Utility
· Decision Pattern: Membangun Notcoin Explore/Earn sebagai platform bagi proyek TON lain (Tonstakers, bemo, TonWhales, dll) menjalankan kampanye reward; Notcoin memotong fee, NOT mendapat utility (hold untuk ikut), proyek mitra mendapat user, user mendapat reward
· Evidence: Phase 3 EV-006 (Explore), EV-008 (Earn); Phase 7 Major Integrations (Explore & Earn Platform dengan Tonstakers, bemo, TonWhales); Phase 6 Token Utility (Earn Campaign Participation); Phase 8 Adoption Metrics (50+ campaigns)
· Supporting Dataset: Phase 3 EV-006, EV-008; Phase 7 Major Integrations; Phase 6 Token Utility; Phase 8 Adoption Metrics

Pola 5: NFT & SBT Sebagai Identity & Access Layer (Getgems, TON Society)
· Decision Pattern: Menggunakan NFT (Genesis collection Getgems) dan SBT (TON Society) sebagai voucher akses eksklusif, governance weight, dan verifikasi identitas — bukan sekadar koleksi seni
· Evidence: Phase 3 EV-007 (Genesis NFT Getgems), EV-009 (Governance weight future); Phase 7 Major Integrations (Genesis NFT, TON Society SBT); Phase 6 Token Utility (NFT Voucher Redemption); Phase 2 Entity (Getgems, TON Society)
· Supporting Dataset: Phase 3 EV-007; Phase 7 Major Integrations; Phase 6 Token Utility; Phase 2 Entity

Pola 1: Off-chain Governance (Snapshot) sebagai Signaling Layer — Eksekusi Tetap Pusat
· Decision Pattern: Menggunakan Snapshot untuk gasless voting 1 NOT = 1 vote; proposal bersifat advisory/non-binding; Open Builders memutuskan eksekusi; tidak ada delegasi, tidak ada quorum resmi, tidak ada timelock on-chain
· Evidence: Phase 3 EV-009 (Snapshot launch); Phase 6 Governance (Off-chain Snapshot, non-binding, no delegation); Phase 7 Major Integrations (Governance Snapshot); Phase 5 Treasury (Open Builders control)
· Supporting Dataset: Phase 3 EV-009; Phase 6 Governance; Phase 7 Major Integrations; Phase 5 Treasury

Pola 2: Tidak Ada DAO On-chain, Tidak Ada Multisig Transparan, Tidak Ada Timelock untuk Treasury
· Decision Pattern: Menghindari kompleksitas legal & teknis DAO on-chain; treasury 22% supply dikendalikan langsung Open Builders (admin address Jetton master, wallet AA Paymaster); komunitas hanya bisa signaling via Snapshot
· Evidence: Phase 6 Governance (No on-chain DAO); Phase 6 Vesting Schedule (No vesting contract for team); Phase 5 Treasury (Custodian Open Builders, no multisig public); Phase 4 Security Model (Upgradeability risk, admin address)
· Supporting Dataset: Phase 6 Governance, Vesting Schedule; Phase 5 Treasury; Phase 4 Security Model

Pola 3: Governance Minimal Viable — Hanya Parameter Earn & Treasury Allocation, Bukan Protocol Upgrade
· Decision Pattern: Scope governance terbatas pada alokasi treasury, parameter kampanye Earn, grant ekosistem; tidak mencakup upgrade smart contract, parameter protokol inti (Jetton master), atau pengambilan keputusan strategis produk
· Evidence: Phase 3 EV-009 (Proposal pertama: treasury allocation & ecosystem grants); Phase 6 Governance (Proposal system: treasury, Earn parameters, grants); Phase 3 EV-010, EV-011, EV-013 (Product decisions Wallet, Ads, v2 roadmap made by team without vote)
· Supporting Dataset: Phase 3 EV-009, EV-010, EV-011, EV-013; Phase 6 Governance

Pola 1: Platform Dependency Risk — Mitigasi via Diversifikasi Produk & Revenue, Bukan Technical Decoupling
· Trigger: Ketergantungan ekstrim pada Telegram (hosting, auth, distribusi, ads) & TON (settlement, wallet AA)
· Decision Pattern: Menerima platform dependency sebagai trade-off untuk distribusi massal; mitigasi via membangun multiple produk (Explore, Earn, Wallet) yang menciptakan switching cost bagi user & revenue stream independen (Earn fees, Ads); tidak membangun fallback chain atau standalone app
· Evidence: Phase 4 Known Limitations (Telegram Platform Dependency, Critical); Phase 7 External Dependencies (Telegram Critical, TON Critical); Phase 5 Financial Dependencies (Telegram, TON Foundation); Phase 3 EV-006, EV-008, EV-010, EV-011 (Product diversification)
· Response: Diversifikasi produk & revenue dalam platform yang sama
· Result: 50M+ users locked in Mini App ecosystem; revenue dari Ads & Earn; tapi single point of failure tetap ada
· Supporting Dataset: Phase 4 Known Limitations; Phase 7 External Dependencies; Phase 5 Financial Dependencies; Phase 3 EV-006, EV-008, EV-010, EV-011

Pola 2: Smart Contract Audit Risk — Deferred/Ignored (No Public Audit Until 2025-01)
· Trigger: Kontrak kritis (Jetton Master, Wallet AA Paymaster/Bundler, Earn Campaigns) mengelola nilai besar tapi tidak diaudit publik
· Decision Pattern: Meluncurkan kontrak tanpa audit publik formal; mengandalkan standar TON (TEP-74 Jetton), best practices AA, dan internal review; audit mungkin dijalankan privat tapi tidak dipublikasikan
· Evidence: Phase 4 Audit History (No public audit found); Phase 4 Security Model (Upgradeability risk, Paymaster trust); Phase 4 Known Limitations (No Public Audit, High); Phase 6 Open Threads (Audit status unverified)
· Response: Launch without public audit; rely on battle-tested standards
· Result: No major exploit reported hingga 2025-01; tapi trust deficit di kalangan security-conscious users & institutions
· Supporting Dataset: Phase 4 Audit History, Security Model, Known Limitations; Phase 6 Open Threads

Pola 3: Competitive Response — Feature Parity + Differentiation (Wallet AA, Explore) Rather Than Token Incentive War
· Trigger: Kompetitor (Hamster Kombat 300M users, Blum Binance Labs backing, Pixelverse Binance Launchpool) meluncurkan token & fitur serupa
· Decision Pattern: Tidak bergantung pada token incentive lebih besar (tidak ada emission, tidak ada staking yield); fokus pada diferensiasi produk: Native AA Wallet (kompetitor belum punya), Explore/Earn platform (ecosystem flywheel), Telegram Ads integration (revenue share)
· Evidence: Phase 8 Competitor Landscape (Hamster, Blum, TapSwap, Pixelverse, Catizen, Tonstation); Phase 3 EV-010 (Wallet AA launch), EV-006 (Explore), EV-011 (Ads); Phase 6 Inflation/Deflation (No inflation mechanism)
· Response: Product differentiation > token inflation
· Result: Retention via utility (Wallet, Earn) bukan yield farming; market cap rank top 50-70 maintained
· Supporting Dataset: Phase 8 Competitor Landscape, Market Position; Phase 3 EV-006, EV-010, EV-011; Phase 6 Inflation/Deflation

Pola 4: Regulatory Uncertainty — Entity Opacity & Jurisdiction Secrecy
· Trigger: Regulasi crypto global ketat (MiCA EU, SEC US, dll); token NOT sebagai utility/consumer token dengan 50M+ user global
· Decision Pattern: Tidak mengumumkan yurisdiksi inkorporasi Open Builders; tidak KYC pengguna (anonymous Telegram ID); tidak membatasi akses berdasarkan geografi; legal entity opacity sebagai strategi defensif
· Evidence: Phase 1 Foundation (Country: Not disclosed, Jurisdiction not announced); Phase 2 Entity (Open Builders jurisdiction not disclosed); Phase 5 Financial Risk (Legal Financial Risk: jurisdiction undisclosed); Phase 8 Open Threads (Legal entity jurisdiction not verified)
· Response: Operational opacity, no geo-blocking, no KYC
· Result: Global access maintained; regulatory risk transferred to future
· Supporting Dataset: Phase 1 Foundation; Phase 2 Entity; Phase 5 Financial Risk; Phase 8 Open Threads

Pola 1: Launch Off-chain → On-chain Settlement After PMF (Berulang: Game → Token → Wallet → Earn)
· Pattern: Setiap produk utama diluncurkan off-chain/centralized dulu (Game tap, Explore frontend, Wallet UI), baru komponen on-chain ditambahkan setelah adoption terbukti (Jetton NOT, Earn campaign contracts, Wallet AA contracts)
· Evidence: Phase 3 EV-002 (Game off-chain) → EV-005 (Jetton on-chain); EV-006 (Explore launch) → EV-008 (Earn on-chain contracts); EV-010 (Wallet AA on-chain contracts deployed after UI ready)
· Supporting Dataset: Phase 3 EV-002, EV-005, EV-006, EV-008, EV-010; Phase 4 Technical Upgrade History

Pola 2: Telegram Platform Feature Adoption sebagai Early Adopter / Pilot (Berulang: Mini App, Ads Platform, Mini App Store)
· Pattern: Setiap kali Telegram meluncurkan fitur platform baru (Mini Apps Jan 2024, Ads Platform Nov 2024, Mini App Store), Notcoin langsung jadi pilot/early adopter — mendapat first-mover advantage, revenue share, dan visibilitas
· Evidence: Phase 3 EV-002 (Mini App launch Jan 2024), EV-011 (Ads Platform pilot Nov 2024); Phase 7 External Dependencies (Telegram Critical); Phase 8 Market Timeline
· Supporting Dataset: Phase 3 EV-002, EV-011; Phase 7 External Dependencies; Phase 8 Market Timeline

Pola 3: TON Ecosystem Standard Adoption Without Forking (Berulang: Jetton TEP-74, TonConnect, Tonapi, TEP-89 future)
· Pattern: Selalu menggunakan standar resmi TON ecosystem tanpa modifikasi/custom fork; berkontribusi ke adoption standar (Jetton, TonConnect, AA) tapi tidak menciptakan standar competiting
· Evidence: Phase 4 Core Components (Jetton TEP-74, TonConnect SDK, Tonapi SDK); Phase 7 Developer Ecosystem (Blueprint, Tact); Phase 4 Known Limitations (FunC maturity)
· Supporting Dataset: Phase 4 Core Components, Development Framework, Known Limitations; Phase 7 Developer Ecosystem

Pola 4: Community-First Token Distribution Then Platform Utility Building (Berulang: 78% airdrop → Explore/Earn utility → Wallet AA retention)
· Pattern: Distribusi token luas gratis ke jutaan user dulu (fair launch narrative), lalu membangun utility & retention mechanisms (Explore access, Earn campaigns, Wallet AA) untuk mencegah dump & menciptakan demand organik
· Evidence: Phase 6 Distribution (78% community), TGE (11M+ claimers), Vesting (0 cliff); Phase 3 EV-006 (Explore), EV-008 (Earn), EV-010 (Wallet); Phase 6 Token Utility (7 utilities)
· Supporting Dataset: Phase 6 Distribution, TGE, Vesting Schedule, Token Utility; Phase 3 EV-006, EV-008, EV-010

Trade-off 1: Sentralisasi Fase Awal (Off-chain Game) vs Kecepatan & Skala Viral
· Decision: Membangun game logic sepenuhnya off-chain di server terpusat Open Builders untuk fase mining (Jan-Apr 2024)
· Trade-off: Mengorbankan desentralisasi, verifiabilitas, dan trust-minimization demi throughput tinggi, biaya nol, UX mulus, dan kecepatan iterasi produk — memungkinkan 35M users dalam 3 bulan
· Evidence: Phase 3 EV-002, EV-003; Phase 4 Architecture (Off-chain Game Backend centralized), Known Limitations (Off-chain Game Centralization, High); Phase 8 Adoption Metrics (35M peak users)
· Supporting Dataset: Phase 3 EV-002, EV-003; Phase 4 Architecture, Known Limitations; Phase 8 Adoption Metrics

Trade-off 2: Token Distribution Fairness (78% Community Instant Unlock) vs Price Stability & Long-term Alignment
· Decision: 78% supply diklaim instan tanpa vesting, 22% tim/ekosistem tanpa vesting schedule on-chain
· Trade-off: Mengorbankan stabilitas harga jangka pendek (tekanan jual masif dari 11M+ claimers) dan alignment jangka panjang (tim/ekosistem bisa jual kapan saja) demi naratif "fair launch", kesetaraan, dan goodwill komunitas
· Evidence: Phase 6 Distribution (78% community), Vesting Schedule (Community 0 vesting, Team undisclosed); Phase 6 TGE (11M+ claimers day 1); Phase 5 Financial Risk (Treasury Concentration); Phase 8 Market Timeline
· Supporting Dataset: Phase 6 Distribution, Vesting Schedule, TGE; Phase 5 Financial Risk; Phase 8 Market Timeline

Trade-off

## Knowledge Extraction
_ref: `docs/Patterns/*`, `docs/Reasoning/*` (rule candidates)_

PROJECT: Notcoin

Core Insights

Insight 1: Off-chain First, On-chain Settlement Later Memungkinkan Skala Mass Adoption Tanpa Biaya Gas
Explanation: Notcoin meluncurkan game tap-to-earn sepenuhnya off-chain di server terpusat Open Builders pada Januari 2024, menunda on-chain settlement (Jetton NOT di TON) hingga Mei 2024 setelah 35 juta pengguna terkumpul【Phase 3 — EV-002】【Phase 3 — EV-003】. Arsitektur hybrid ini mengorbankan desentralisasi awal demi throughput tinggi, biaya nol, dan UX mulus【Phase 4 — Known Limitations】.
Evidence: Game launch off-chain Jan 2024【Phase 3 — EV-002】; 35M users peak Mar 2024【Phase 3 — EV-003】; TGE on-chain May 2024【Phase 3 — EV-005】; Architecture hybrid off-chain/on-chain【Phase 4 — Architecture】; Centralization limitation acknowledged【Phase 4 — Known Limitations】.
Supporting Dataset: Phase 3 Events, Phase 4 Architecture, Phase 4 Known Limitations.
Confidence: HIGH

Insight 2: Distribusi Token 78% Ke Komunitas Instan Tanpa Vesting Menciptakan Holder Base Luas Tapi Tekanan Jual Berkelanjutan
Explanation: Pada TGE 16 Mei 2024, 78% dari 102,719,221,714 NOT (≈80,121,000,000 NOT) diklaim instan oleh 11,000,000+ wallet unik tanpa cliff atau vesting, sedangkan 22% (≈22,598,000,000 NOT) dialokasi ke tim/ekosistem tanpa vesting schedule on-chain terverifikasi【Phase 6 — Distribution】【Phase 6 — Vesting Schedule】【Phase 3 — EV-005】.
Evidence: 78% community allocation【Phase 6 — Distribution】; Community 0 vesting【Phase 6 — Vesting Schedule】; 11M+ claimers day 1【Phase 3 — EV-005】; Team/eco 22% no on-chain vesting verified【Phase 6 — Vesting Schedule】【Phase 5 — Treasury】.
Supporting Dataset: Phase 6 Token Distribution, Phase 6 Vesting Schedule, Phase 3 EV-005, Phase 5 Treasury.
Confidence: HIGH

Insight 3: Telegram Mini App Platform Sebagai Saluran Distribusi Eksklusif Menghilangkan Friction Onboarding Non-Crypto Users
Explanation: Notcoin dibangun eksklusif sebagai Telegram Mini App, memanfaatkan basis pengguna Telegram >900 juta MAU, Bot API, Web App SDK, dan initData auth tanpa perlu download aplikasi terpisah atau seed phrase【Phase 7 — External Dependencies: Telegram】【Phase 4 — Execution Environment】. Ini memungkinkan 50 juta pengguna unik lifetime per Desember 2024【Phase 3 — EV-012】.
Evidence: Telegram Mini App exclusive【Phase 7 — External Dependencies: Telegram】; Telegram Web App runtime【Phase 4 — Execution Environment】; 50M+ unique users Dec 2024【Phase 3 — EV-012】; No separate app/seed phrase required【Phase 3 — EV-002】.
Supporting Dataset: Phase 7 External Dependencies, Phase 4 Execution Environment, Phase 3 EV-012.
Confidence: HIGH

Insight 4: Account Abstraction (ERC-4337) Native Wallet Menjadi Differentiator Kompetitif Utama vs Mini App Lain
Explanation: Notcoin Wallet (ERC-4337 di TON) diluncurkan Oktober 2024 dengan social recovery via Telegram login, gasless via Paymaster Open Builders, batched transactions, dan fiat on-ramp — mencapai 2,000,000+ deployments dalam 2 bulan【Phase 3 — EV-010】【Phase 8 — Adoption Metrics】. Kompetitor utama (Hamster Kombat, Blum, TapSwap) belum memiliki native AA wallet per Januari 2025【Phase 8 — Competitor Landscape】.
Evidence: Wallet launch Oct 2024【Phase 3 — EV-010】; 2M+ deployments 2 months【Phase 8 — Adoption Metrics】; ERC-4337 features【Phase 4 — Core Components: Smart Wallet】; Competitors lack native AA wallet【Phase 8 — Competitor Landscape】.
Supporting Dataset: Phase 3 EV-010, Phase 8 Adoption Metrics, Phase 4 Core Components, Phase 8 Competitor Landscape.
Confidence: HIGH

Insight 5: Model Revenue Diversification Dari Token Ke Platform Fees & Ads Mengurangi Ketergantungan Harga Token
Explanation: Pasca-TGE, Notcoin membangun tiga revenue stream: (1) Telegram Ads Platform revenue share (pilot Nov 2024)【Phase 3 — EV-011】, (2) Earn campaign fees (take rate dari reward pool mitra, live Jul 2024)【Phase 3 — EV-008】, (3) Potensial fiat on-ramp partner fees via Notcoin Wallet【Phase 5 — Revenue Model】. Tidak ada VC funding publik, tidak ada token sale【Phase 5 — Funding History】.
Evidence: Telegram Ads revenue share pilot Nov 2024【Phase 3 — EV-011】; Earn campaign fees live Jul 2024【Phase 3 — EV-008】; Fiat on-ramp partner fees planned【Phase 5 — Revenue Model】; Zero VC funding, zero token sale【Phase 5 — Funding History】.
Supporting Dataset: Phase 3 EV-011, EV-008, Phase 5 Revenue Model, Phase 5 Funding History.
Confidence: MEDIUM

Insight 6: Governance Off-chain Snapshot Non-binding Menjadi Signaling Layer Saja, Eksekusi Tetap Pusat di Open Builders
Explanation: Snapshot governance diluncurkan 15 Juli 2024 (1 NOT = 1 vote, gasless) untuk proposal treasury allocation & Earn parameters, namun bersifat advisory/non-binding tanpa delegasi, tanpa quorum resmi, tanpa timelock on-chain【Phase 3 — EV-009】【Phase 6 — Governance】. Treasury 22% supply dikendalikan langsung Open Builders (admin address Jetton master, Paymaster wallet AA)【Phase 5 — Treasury】【Phase 4 — Security Model】.
Evidence: Snapshot launch Jul 2024【Phase 3 — EV-009】; Off-chain non-binding【Phase 6 — Governance】; No delegation/quorum/timelock【Phase 6 — Governance】; Treasury controlled by Open Builders【Phase 5 — Treasury】; Admin address Jetton master【Phase 4 — Security Model】.
Supporting Dataset: Phase 3 EV-009, Phase 6 Governance, Phase 5 Treasury, Phase 4 Security Model.
Confidence: HIGH

Insight 7: Ekosistem Partner Earn (Explore/Earn) Menciptakan Flywheel Utility Token NOT Tanpa Inflation
Explanation: Notcoin Explore (May 2024) dan Earn (Jul 2024) memungkinkan 50+ proyek TON (Tonstakers, bemo, TonWhales) menjalankan kampanye reward on-chain; Notcoin memotong fee, NOT mendapat utility (hold untuk ikut), proyek mendapat user, user mendapat reward【Phase 3 — EV-006】【Phase 3 — EV-008】【Phase 8 — Adoption Metrics】. Supply NOT fixed 102.7B, tidak ada inflation mechanism【Phase 6 — Inflation/Deflation】.
Evidence: Explore launch May 2024【Phase 3 — EV-006】; Earn launch Jul 2024【Phase 3 — EV-008】; 50+ campaigns Jan 2025【Phase 8 — Adoption Metrics】; Fee model【Phase 5 — Revenue Model】; Fixed supply no inflation【Phase 6 — Inflation/Deflation】.
Supporting Dataset: Phase 3 EV-006, EV-008, Phase 8 Adoption Metrics, Phase 5 Revenue Model, Phase 6 Inflation/Deflation.
Confidence: HIGH

Insight 8: Ketergantungan Ekstrim Pada Telegram & TON Menciptakan Platform Risk Yang Tidak Bisa Dieliminasi Teknis
Explanation: Seluruh distribusi, auth, UI, ads revenue, dan settlement bergantung pada Telegram (Critical) dan TON (Critical)【Phase 7 — External Dependencies】. Perubahan kebijakan Telegram (API breaking, ban, ads policy) atau TON (consensus, validator set) berdampak langsung ketersediaan aplikasi【Phase 4 — Known Limitations: Telegram Platform Dependency】. Tidak ada fallback chain atau standalone app【Phase 9 — Pola 1: Platform Dependency Risk】.
Evidence: Telegram Critical dependency【Phase 7 — External Dependencies】; TON Critical dependency【Phase 7 — External Dependencies】; Telegram Platform Dependency High【Phase 4 — Known Limitations】; No fallback chain/standalone app【Phase 9 — Pola 1】.
Supporting Dataset: Phase 7 External Dependencies, Phase 4 Known Limitations, Phase 9 Pola 1.
Confidence: HIGH

Insight 9: Smart Contract Audit Deferred/Ignored — Tidak Ada Audit Publik Untuk Kontrak Kritis Hingga Jan 2025
Explanation: Kontrak Jetton Master, Wallet AA (Paymaster/Bundler), Earn Campaign contracts mengelola nilai besar namun tidak memiliki laporan audit publik dari auditor independen (Certik, Trail of Bits, dll)【Phase 4 — Audit History】【Phase 4 — Known Limitations: No Public Audit】. Mengandalkan standar TON (TEP-74) dan internal review saja【Phase 4 — Security Model】.
Evidence: No public audit found【Phase 4 — Audit History】; No Public Audit High limitation【Phase 4 — Known Limitations】; Relies on TEP-74 standard【Phase 4 — Security Model】; Audit status unverified【Phase 6 — Open Threads】.
Supporting Dataset: Phase 4 Audit History, Phase 4 Known Limitations, Phase 4 Security Model, Phase 6 Open Threads.
Confidence: HIGH

Insight 10: Entity Opacity (Yurisdiksi Open Builders Tidak Diungkap) Sebagai Strategi Defensif Regulatory Uncertainty
Explanation: Open Builders tidak mengumumkan yurisdiksi inkorporasi, nomor registrasi, atau legal entity details【Phase 1 — Foundation】【Phase 2 — Entity: Open Builders】. Tidak KYC pengguna (anonymous Telegram ID), tidak geo-blocking【Phase 9 — Pola 4: Regulatory Uncertainty】. Legal financial risk: jurisdiction undisclosed【Phase 5 — Financial Risk】.
Evidence: Jurisdiction not disclosed【Phase 1 — Foundation】; Open Builders jurisdiction not announced【Phase 2 — Entity】; No KYC, no geo-blocking【Phase 9 — Pola 4】; Legal financial risk jurisdiction undisclosed【Phase 5 — Financial Risk】.
Supporting Dataset: Phase 1 Foundation, Phase 2 Entity, Phase 9 Pola 4, Phase 5 Financial Risk.
Confidence: MEDIUM

Strategic Principles

Principle 1: Off-chain First, On-chain Settlement After Product-Market Fit
Explanation: Setiap produk utama diluncurkan off-chain/centralized dulu (Game tap, Explore frontend, Wallet UI), baru komponen on-chain ditambahkan setelah adoption terbukti (Jetton NOT, Earn campaign contracts, Wallet AA contracts)【Phase 9 — Pola 1: Launch Off-chain → On-chain Settlement After PMF】.
Evidence: Game off-chain Jan 2024 → Jetton on-chain May 2024【Phase 3 — EV-002】【Phase 3 — EV-005】; Explore launch May 2024 → Earn on-chain contracts Jul 2024【Phase 3 — EV-006】【Phase 3 — EV-008】; Wallet UI ready → AA contracts deployed Oct 2024【Phase 3 — EV-010】.
Supporting Dataset: Phase 9 Pola 1, Phase 3 Events, Phase 4 Technical Upgrade History.
Confidence: HIGH

Principle 2: Telegram-Native Development — Mini App First, Blockchain Second
Explanation: Semua produk dibangun sebagai Telegram Mini App pertama kali; blockchain (TON) digunakan hanya untuk settlement, ownership, dan composability; tidak ada standalone mobile/web app atau browser-based dApp【Phase 9 — Pola 2: Telegram-Native Development】.
Evidence: Launch di Telegram Jan 2024【Phase 3 — EV-002】; Explore di Telegram Web App【Phase 3 — EV-006】; Wallet embedded di Mini App【Phase 3 — EV-010】; Execution Environment Telegram Web App【Phase 4 — Execution Environment】; Telegram Critical dependency【Phase 7 — External Dependencies】.
Supporting Dataset: Phase 9 Pola 2, Phase 3 Events, Phase 4 Execution Environment, Phase 7 External Dependencies.
Confidence: HIGH

Principle 3: Account Abstraction Sebagai Differentiator Kompetitif Utama
Explanation: Investasi besar pada ERC-4337 Smart Wallet (Paymaster, Bundler, Social Recovery) untuk menghilangkan semua friction onboarding non-crypto users; wallet menjadi fitur core produk, bukan tambahan【Phase 9 — Pola 3: Account Abstraction Sebagai Differentiator】.
Evidence: Wallet AA launch Oct 2024【Phase 3 — EV-010】; 2M+ deployments 2 months【Phase 8 — Adoption Metrics】; Native first-party wallet【Phase 7 — Wallet Ecosystem】; Competitors lack AA wallet【Phase 8 — Competitor Landscape】.
Supporting Dataset: Phase 9 Pola 3, Phase 3 EV-010, Phase 8 Adoption Metrics, Phase 7 Wallet Ecosystem, Phase 8 Competitor Landscape.
Confidence: HIGH

Principle 4: Standar TON Ecosystem Adoption Without Forking
Explanation: Selalu menggunakan standar & infrastruktur yang sudah ada di ekosistem TON (Jetton TEP-74, TonConnect, Tonapi, Blueprint, Tact) daripada membangun custom solution; focus resources pada application layer【Phase 9 — Pola 3: TON Ecosystem Standard Adoption】.
Evidence: Jetton TEP-74 standard【Phase 4 — Core Components】; TonConnect SDK【Phase 4 — Development Framework】【Phase 7 — Developer Ecosystem】; Tonapi SDK【Phase 4 — Development Framework】【Phase 7 — Infrastructure Providers】; Blueprint/Tact framework【Phase 4 — Development Framework】.
Supporting Dataset: Phase 9 Pola 3, Phase 4 Core Components, Phase 4 Development Framework, Phase 7 Infrastructure Providers, Phase 7 Developer Ecosystem.
Confidence: HIGH

Principle 5: Community-First Token Distribution Then Platform Utility Building
Explanation: Distribusi token luas gratis ke jutaan user dulu (fair launch narrative 78% community, 0% investor), lalu membangun utility & retention mechanisms (Explore access, Earn campaigns, Wallet AA) untuk mencegah dump & menciptakan demand organik【Phase 9 — Pola 4: Community-First Token Distribution】.
Evidence: 78% community allocation【Phase 6 — Distribution】; 11M+ claimers TGE【Phase 3 — EV-005】; 0 vesting community【Phase 6 — Vesting Schedule】; Explore/Earn/Wallet utility post-TGE【Phase 3 — EV-006】【Phase 3 — EV-008】【Phase 3 — EV-010】; 7 token utilities【Phase 6 — Token Utility】.
Supporting Dataset: Phase 9 Pola 4, Phase 6 Distribution, Phase 3 EV-005, Phase 6 Vesting Schedule, Phase 3 Events, Phase 6 Token Utility.
Confidence: HIGH

Success Factors

Factor 1: First-Mover Advantage Di Telegram Mini App Tap-to-Earn Category
Explanation: Notcoin meluncurkan game tap-to-earn di Telegram Mini App pada Januari 2024, menjadi "first mover" & largest user base di kategori ini; 35 juta pengguna puncak Maret 2024 sebelum kompetitor (Hamster Kombat Mar 2024, Blum, TapSwap) skala besar【Phase 3 — EV-002】【Phase 3 — EV-003】【Phase 8 — Market Position】.
Evidence: Game launch Jan 2024【Phase 3 — EV-002】; 35M peak users Mar 2024【Phase 3 — EV-003】; Recognized as category leader【Phase 8 — Market Position】; Competitors launched later【Phase 8 — Competitor Landscape】.
Supporting Dataset: Phase 3 EV-002, EV-003, Phase 8 Market Position, Phase 8 Competitor Landscape.
Confidence: HIGH

Factor 2: Viral Loop Referral/Squad Mechanics Tanpa Biaya Gas (Off-chain)
Explanation: Game logic off-chain memungkinkan referral/squad mechanics instan, biaya nol, tanpa gas fee, mendorong viral growth 1 juta pengguna dalam 2 minggu, 35 juta pada puncak【Phase 3 — EV-002】【Phase 3 — EV-003】【Phase 4 — Architecture: Off-chain Game Backend】.
Evidence: 1M users in 2 weeks【Phase 3 — EV-002】; 35M peak users【Phase 3 — EV-003】; Off-chain centralized backend【Phase 4 — Architecture】; No gas cost for users【Phase 4 — Known Limitations】.
Supporting Dataset: Phase 3 EV-002, EV-003, Phase 4 Architecture, Phase 4 Known Limitations.
Confidence: HIGH

Factor 3: Top-Tier CEX Listing Strategy Serentak TGE (Binance, Bybit, OKX)
Explanation: Listing serentak di 3 CEX terbesar global (Binance Launchpool & Spot, Bybit Spot, OKX Spot) + 2 DEX utama (Dedust, Ston.fi) pada TGE 16 Mei 2024 memastikan likuiditas mendalam, akses fiat global, dan visibilitas mass market dari hari pertama【Phase 3 — EV-005】【Phase 7 — Exchange Ecosystem】【Phase 8 — Trading Markets】.
Evidence: Simultaneous listing 5 CEX + 2 DEX TGE May 16 2024【Phase 3 — EV-005】; Binance/Bybit/OKX all Spot + Perpetual【Phase 7 — Exchange Ecosystem】; $150-300M 24h volume Jan 2025【Phase 8 — Adoption Metrics】.
Supporting Dataset: Phase 3 EV-005, Phase 7 Exchange Ecosystem, Phase 8 Trading Markets, Phase 8 Adoption Metrics.
Confidence: HIGH

Factor 4: Telegram Ads Platform Pilot Integration Memberikan Revenue Non-Token
Explanation: Menjadi pilot Telegram Ads Platform (Nov 2024) memberikan revenue share dari rewarded ads, mengurangi ketergantungan pada token price & Earn fees saja【Phase 3 — EV-011】【Phase 5 — Revenue Model】【Phase 7 — External Dependencies: Telegram Ads】.
Evidence: Ads Platform pilot Nov 2024【Phase 3 — EV-011】; Revenue share model【Phase 5 — Revenue Model】; Telegram Ads Critical dependency【Phase 7 — External Dependencies】.
Supporting Dataset: Phase 3 EV-011, Phase 5 Revenue Model, Phase 7 External Dependencies.
Confidence: MEDIUM

Factor 5: Account Abstraction Wallet Native Deployment Terbesar Di TON (2M+ Dalam 2 Bulan)
Explanation: Notcoin Wallet ERC-4337 mencapai 2,000,000+ smart wallet deployments dalam 2 bulan pasca-launch Okt 2024, validasi product-market fit untuk AA wallet di consumer app【Phase 3 — EV-010】【Phase 8 — Adoption Metrics】【Phase 8 — Narrative Position: Account Abstraction】.
Evidence: Wallet launch Oct 2024【Phase 3 — EV-010】; 2M+ deployments 2 months【Phase 8 — Adoption Metrics】; Largest AA wallet deployment on TON【Phase 8 — Narrative Position】.
Supporting Dataset: Phase 3 EV-010, Phase 8 Adoption Metrics, Phase 8 Narrative Position.
Confidence: HIGH

Failure Factors

Factor 1: Treasury Management Non-Transparent — 22% Supply (≈22.6B NOT) Tanpa Vesting On-chain, Multisig, Atau Dashboard Publik
Explanation: Alokasi 22% tim/ekosistem dikirim ke alamat Open Builders tanpa vesting contract on-chain terverifikasi, tanpa multisig transparan, tanpa transparency dashboard, tanpa laporan berkala【Phase 5 — Treasury】【Phase 6 — Vesting Schedule】【Phase 5 — Financial Risk: Treasury Concentration】.
Evidence: 22% team/eco no on-chain vesting【Phase 6 — Vesting Schedule】; Treasury custodian Open Builders no multisig public【Phase 5 — Treasury】; Treasury Concentration risk【Phase 5 — Financial Risk】; No transparency dashboard【Phase 5 — Official Financial Resources】.
Supporting Dataset: Phase 5 Treasury, Phase 6 Vesting Schedule, Phase 5 Financial Risk, Phase 5 Official Financial Resources.
Confidence: HIGH

Factor 2: Smart Contract Audit Deferred — Tidak Ada Audit Publik Untuk Kontrak Mengelola Nilai Besar
Explanation: Kontrak Jetton Master, Wallet AA (Paymaster/Bundler), Earn Campaign contracts tidak memiliki laporan audit publik dari auditor independen hingga Jan 2025【Phase 4 — Audit History】【Phase 4 — Known Limitations: No Public Audit】【Phase 6 — Open Threads】.
Evidence: No public audit found【Phase 4 — Audit History】; No Public Audit High limitation【Phase 4 — Known Limitations】; Audit status unverified【Phase 6 — Open Threads】.
Supporting Dataset: Phase 4 Audit History, Phase 4 Known Limitations, Phase 6 Open Threads.
Confidence: HIGH

Factor 3: Governance Theater — Snapshot Non-binding Tanpa Eksekusi On-chain Atau Delegasi
Explanation: Governance Snapshot (Jul 2024) bersifat advisory only, 1 NOT = 1 vote tanpa delegasi, tanpa quorum resmi, tanpa timelock; eksekusi tetap di tangan Open Builders【Phase 3 — EV-009】【Phase 6 — Governance】【Phase 9 — Pola 1: Off-chain Governance】.
Evidence: Snapshot non-binding【Phase 6 — Governance】; No delegation/quorum/timelock【Phase 6 — Governance】; Execution by Open Builders【Phase 9 — Pola 1】; Proposal scope limited【Phase 6 — Governance】.
Supporting Dataset: Phase 3 EV-009, Phase 6 Governance, Phase 9 Pola 1.
Confidence: HIGH

Factor 4: Platform Dependency Risk Tidak Bisa Dieliminasi — Single Point of Failure Telegram & TON
Explanation: Seluruh stack bergantung pada Telegram (hosting, auth, distribusi, ads) dan TON (settlement, AA); tidak ada fallback chain, standalone app, atau technical decoupling【Phase 4 — Known Limitations: Telegram Platform Dependency】【Phase 7 — External Dependencies: Telegram Critical, TON Critical】【Phase 9 — Pola 1】.
Evidence: Telegram Platform Dependency Critical【Phase 4 — Known Limitations】; Telegram Critical, TON Critical【Phase 7 — External Dependencies】; No fallback chain/standalone app【Phase 9 — Pola 1】.
Supporting Dataset: Phase 4 Known Limitations, Phase 7 External Dependencies, Phase 9 Pola 1.
Confidence: HIGH

Factor 5: Tokenomics Team Allocation Opaque — Breakdown 22% (Tim, Advisor, Treasury, Ecosystem) Tidak Diungkap
Explanation: Hanya high-level 78%/22% yang dipublikasikan; breakdown detail tim, advisor, treasury, ecosystem fund, vesting schedule tidak dipublikasikan secara granular【Phase 6 — Distribution】【Phase 6 — Vesting Schedule】【Phase 1 — Open Threads】.
Evidence: Only high-level 78/22 published【Phase 6 — Distribution】; Team/eco breakdown not disclosed【Phase 6 — Vesting Schedule】; Open thread: detail tokenomics not published【Phase 1 — Open Threads】.
Supporting Dataset: Phase 6 Distribution, Phase 6 Vesting Schedule, Phase 1 Open Threads.
Confidence: HIGH

Decision Framework

Step 1: Observe — Validasi Product-Market Fit Via Off-chain MVP Di Telegram Mini App
Explanation: Launch game tap-to-earn off-chain di Telegram Mini App (Jan 2024) untuk mengukur retention, viral coefficient, dan skala tanpa biaya gas & latency on-chain【Phase 3 — EV-002】【Phase 9 — Pola 1】.
Evidence: Game launch off-chain Jan 2024【Phase 3 — EV-002】; 35M users peak Mar 2024【Phase 3 — EV-003】; Off-chain first pattern【Phase 9 — Pola 1】.
Supporting Dataset: Phase 3 EV-002, EV-003, Phase 9 Pola 1.
Confidence: HIGH

Step 2: Evaluate — Mining Phase End & Tokenomics Design (Apr 2024)
Explanation: Berakhirkan mining phase 1 Apr 2024; snapshot saldo off-chain; announce tokenomics 78% community / 22% team-eco; full supply mint 102.7B NOT【Phase 3 — EV-004】【Phase 6 — Distribution】.
Evidence: Mining end Apr 1 2024【Phase 3 — EV-004】; Tokenomics announcement【Phase 3 — EV-004】; 78/22 allocation【Phase 6 — Distribution】; Full supply mint【Phase 6 — TGE】.
Supporting Dataset: Phase 3 EV-004, Phase 6 Distribution, Phase 6 TGE.
Confidence: HIGH

Step 3: Fund — Bootstrapping + TON Foundation Grant + Protocol Revenue (Tidak Ada VC)
Explanation: Pengembangan awal internal funding; grant TON Foundation (nominal tidak diungkap); revenue dari Telegram Ads share & Earn fees pasca-TGE【Phase 5 — Funding History】【Phase 5 — Revenue Model】【Phase 9 — Pola 1: Zero VC Funding】.
Evidence: No VC rounds【Phase 5 — Funding History】; TON Foundation grant【Phase 5 — Funding History】; Telegram Ads revenue share【Phase 5 — Revenue Model】; Earn campaign fees【Phase 5 — Revenue Model】.
Supporting Dataset: Phase 5 Funding History, Phase 5 Revenue Model, Phase 9 Pola 1.
Confidence: HIGH

Step 4: Develop — Parallel Track: On-chain Settlement (Jetton) + Platform Infrastructure (Explore/Earn/Wallet AA)
Explanation: Pasca-TGE Mei 2024: deploy Jetton NOT, launch Explore, develop Earn campaign contracts, build Wallet AA (Paymaster/Bundler)【Phase 3 — EV-005】【Phase 3 — EV-006】【Phase 3 — EV-008】【Phase 3 — EV-010】【Phase 4 — Technical Upgrade History】.
Evidence: TGE & Jetton deploy May 2024【Phase 3 — EV-005】; Explore launch May 2024【Phase 3 — EV-006】; Earn contracts Jul 2024【Phase 3 — EV-008】; Wallet AA Oct 2024【Phase 3 — EV-010】; 5 major upgrades【Phase 4 — Technical Upgrade History】.
Supporting Dataset: Phase 3 Events, Phase 4 Technical Upgrade History.
Confidence: HIGH

Step 5: Launch — Simultaneous CEX/DEX Listing + Community Claim + Explore Live
Explanation: TGE 16 Mei 2024: mint full supply, 11M+ wallet claim, listing Binance/Bybit/OKX/Gate.io/KuCoin + Dedust/Ston.fi, Explore live same day【Phase 3 — EV-005】【Phase 3 — EV-006】【Phase 7 — Exchange Ecosystem】.
Evidence: TGE May 16 2024【Phase 3 — EV-005】; 11M+ claimers day 1【Phase 3 — EV-005】; 5 CEX + 2 DEX simultaneous【Phase 7 — Exchange Ecosystem】; Explore live TGE【Phase 3 — EV-006】.
Supporting Dataset: Phase 3 EV-005, EV-006, Phase 7 Exchange Ecosystem.
Confidence: HIGH

Step 6: Govern — Off-chain Snapshot Signaling + Centralized Execution By Open Builders
Explanation: Snapshot governance Jul 2024 untuk treasury allocation & Earn parameters; proposal advisory; eksekusi oleh Open Builders (multisig/admin tidak diungkap)【Phase 3 — EV-009】【Phase 6 — Governance】【Phase 9 — Pola 1: Off-chain Governance】.
Evidence: Snapshot launch Jul 2024【Phase 3 — EV-009】; Off-chain non-binding【Phase 6 — Governance】; Execution by Open Builders【Phase 9 — Pola 1】.
Supporting Dataset: Phase 3 EV-009, Phase 6 Governance, Phase 9 Pola 1.
Confidence: HIGH

Reusable Playbook

Playbook 1: Off-chain MVP Di Platform Distribusi Massal (Telegram Mini App) Sebelum On-chain Settlement
Explanation: Bangun produk awal off-chain di platform dengan user base besar (Telegram 900M+ MAU) untuk validasi PMF dengan biaya nol & UX mulus; baru tokenize & on-chain settlement setelah user base terbukti【Phase 9 — Pola 1】【Phase 3 — EV-002】【Phase 3 — EV-005】.
Evidence: Off-chain game Jan 2024【Phase 3 — EV-002】; 35M users before TGE【Phase 3 — EV-003】; TGE May 2024 after PMF proven【Phase 3 — EV-005】.
Supporting Dataset: Phase 9 Pola 1, Phase 3 EV-002, EV-003, EV-005.
Confidence: HIGH

Playbook 2: Fair Launch Narrative 100% Community Airdrop (No Sale, No Investor) + Post-TGE Utility Building
Explanation: Distribusi 78-100% supply gratis ke komunitas via mining/airdrop (fair launch), 0% investor/private sale; lalu bangun utility (Explore access, Earn campaigns, Wallet features) untuk retention & demand organik【Phase 6 — Distribution】【Phase 6 — Vesting Schedule】【Phase 3 — EV-006】【Phase 3 — EV-008】【Phase 3 — EV-010】.
Evidence: 78% community, 0% investor【Phase 6 — Distribution】; 0 vesting community【Phase 6 — Vesting Schedule】; Explore/Earn/Wallet utility post-TGE【Phase 3 — EV-006】【Phase 3 — EV-008】【Phase 3 — EV-010】.
Supporting Dataset: Phase 6 Distribution, Phase 6 Vesting Schedule, Phase 3 EV-006, EV-008, EV-010.
Confidence: HIGH

Playbook 3: Native Account Abstraction Wallet Sebagai Moat Kompetitif Di Consumer Crypto App
Explanation: Investasi pada ERC-4337 AA wallet (social recovery, gasless Paymaster, batched tx, fiat on-ramp) embedded di app utama untuk menghilangkan seed phrase & gas friction; menciptakan switching cost tinggi vs kompetitor【Phase 3 — EV-010】【Phase 8 — Adoption Metrics: 2M+ wallets】【Phase 8 — Competitor Landscape】.
Evidence: Wallet AA launch Oct 2024【Phase 3 — EV-010】; 2M+ deployments 2 months【Phase 8 — Adoption Metrics】; Competitors lack native AA wallet【Phase 8 — Competitor Landscape】.
Supporting Dataset: Phase 3 EV-010, Phase 8 Adoption Metrics, Phase 8 Competitor Landscape.
Confidence: HIGH

Playbook 4: Ecosystem Flywheel Via Discovery Platform (Explore) + Reward Campaigns (Earn) Dengan Fee Model
Explanation: Bangun platform discovery untuk app lain di ekosistem yang sama; biarkan partner menjalankan reward campaigns (Earn) ke holder token Anda; ambil fee dari reward pool; token mendapat utility (hold untuk ikut), partner dapat user, user dapat reward【Phase 3 — EV-006】【Phase 3 — EV-008】【Phase 5 — Revenue Model】【Phase 8 — Adoption Metrics: 50+ campaigns】.
Evidence: Explore launch May 2024【Phase 3 — EV-006】; Earn launch Jul 2024【Phase 3 — EV-008】; Fee from reward pool【Phase 5 — Revenue Model】; 50+ campaigns Jan 2025【Phase 8 — Adoption Metrics】.
Supporting Dataset: Phase 3 EV-006, EV-008, Phase 5 Revenue Model, Phase 8 Adoption Metrics.
Confidence: HIGH

Playbook 5: Early

## Open Questions
- [foundation] Yurisdiksi inkorporasi legal entity Open Builders (tidak diumumkan di website, whitepaper, atau filing publik)
- [foundation] Ukuran tim penuh & komposisi (hanya 2 founder yang identitasnya relatif terbuka; sisa "tidak diungkap")
- [foundation] Apakah smart contract game v1 pernah diaudit (tidak ditemukan laporan audit publik pada tanggal penelusuran)
- [foundation] Detail tokenomics lengkap (alokasi tim, investor, treasury, community) — hanya high-level yang dipublikasikan (78% community, 22% tim/ekosistem) tanpa breakdown detail & vesting schedule resmi
- [foundation] Status open-source game engine / backend (repositori GitHub ada tapi tidak berisi core game logic)
- [entity] Identitas legal entity Open Builders (yurisdiksi inkorporasi, nomor registrasi) tidak tersedia publik.
- [entity] Daftar lengkap core team (beyond 2 founders) tidak diungkapkan; tidak ada halaman "Team" resmi di website.
- [entity] Status audit smart contract token NOT (Jetton master/minter) dan game logic v1 tidak ditemukan laporan publik.
- [entity] Detail tokenomics breakdown (alokasi tim, investor, advisors, treasury, vesting schedule) tidak dipublikasikan secara granular; hanya high-level 78%/22%.
- [entity] Keterlibatan investor VC/strategic (jika ada) sebelum TGE tidak terverifikasi; tidak ada announcement funding round.
- [entity] Peran exact Pavel Durov/Telegram dalam kapitalisasi atau advisory Notcoin (jika ada beyond platform) bersifat spekulatif.
- [entity] Status legal DAO/community governance (snapshot voting) apakah binding on-chain atau off-chain signaling only perlu klarifikasi.
- [history] Tanggal pasti pendirian legal entity Open Builders (bulan/tahun) tidak diverifikasi publik; hanya perkiraan berdasarkan narasi founder.
- [history] Tanggal peluncuran "Notcoin Explore" dan "Notcoin Earn" di beberapa sumber (blog vs tweet) memiliki perbedaan 1-2 minggu; perlu cross-check ke on-chain transaction pertama kontrak Earn.
- [history] Status audit smart contract token NOT (Jetton master) dan kontrak Wallet (Account Abstraction) — tidak ditemukan laporan publik dari auditor ternama (Certik, Trail of Bits, dll) hingga cutoff penelusuran.
- [history] Detail tokenomics vesting schedule untuk alokasi 22% (tim/ekosistem) tidak dipublikasikan resmi; hanya high-level di blog. Perlu verifikasi on-chain apakah ada timelock/vesting contract.
- [history] Jumlah dana grant dari TON Foundation ke Open Builders (jika ada) tidak diungkapkan nominalnya; hanya status "grant recipient" yang dikonfirmasi.
- [history] Peran exact Pavel Durov/Telegram dalam kapitalisasi (equity/token allocation) bersifat spekulatif; tidak ada filing atau announcement resmi.
- [history] Rincian teknis "Notcoin v2 / Nettok" (EV-013) masih sangat minim; roadmap blog bersifat high-level tanpa whitepaper atau spec teknis.
- [technology] Kode sumber (source code) smart contract Notcoin (Jetton Master, Wallet AA, Earn Campaigns) tidak diverifikasi (verified) di TON Verifier (tonscan/tonviewer) — hanya bytecode yang terlihat; source code tidak dipublikasikan di GitHub repositori notcoin.
- [technology] Detail arsitektur Paymaster & Bundler untuk Notcoin Wallet (endpoint, kode, keamanan) tidak terdokumentasi publik.
- [technology] Teknologi backend game server (bahasa, framework, database, scaling strategy) tidak diungkapkan; hanya diketahui "centralized server".
- [technology] Status verifikasi formal (formal verification) untuk kontrak FunC Notcoin — tidak ada bukti penggunaan Fift/Func formal verification tools.
- [technology] Detail implementasi "social recovery" di Notcoin Wallet (threshold, guardian set, recovery flow) tidak terdokumentasi di developer docs.
- [technology] Ketergantungan pada Tonapi sebagai single indexer — apakah ada fallback indexer (self-hosted dton.io/graphql atau Toncenter) tidak diketahui.
- [technology] Rencana migrasi/upgrade Jetton master contract (jika ada) ke versi yang lebih aman/feature-rich (mis. TEP-89 jetton wallet v2) tidak diumumkan.
- [technology] Kompatibilitas Notcoin Wallet dengan TON Connect v2 standard untuk dApp lain di ekosistem TON (beyond Notcoin Mini App) belum dikonfirmasi teknis.
- [technology] Detail teknis "Notcoin v2 / Nettok" (AI-driven discovery, multi-chain bridge) dari roadmap 2025 tidak memiliki spesifikasi teknis (whitepaper, RFC, repo) yang tersedia publik.
- [financial] Nominal grant TON Foundation ke Open Builders tidak diungkap; tidak ada announcement resmi dengan angka.
- [financial] Breakdown alokasi 22% (tim, advisor, treasury, ecosystem fund, liquidity provision) tidak dipublikasikan; tidak ada vesting schedule on-chain (smart contract timelock/vesting) yang terverifikasi di block explorer.
- [financial] Apakah Open Builders menjalankan market making sendiri atau menggunakan market maker pihak ketiga untuk token NOT di CEX/DEX — tidak diungkap.
- [financial] Revenue sharing agreement detail dengan Telegram Ads Platform (persentase, minimal payout, kurun waktu) tidak dipublikasikan.
- [financial] Fee structure Notcoin Earn (persentase potongan dari reward pool mitra) tidak diungkap secara spesifik.
- [financial] Status legal entity Open Builders (jurisdiksi, tax residency) memengaruhi pelaporan keuangan & compliance — tidak diungkap.
- [financial] Apakah ada dana cadangan stablecoin/USD untuk operational runway — tidak diungkap.
- [financial] Tidak ada audit keuangan (financial audit) atau proof-of-reserves untuk treasury proyek.
- [financial] Ketergantungan pada single indexer (Tonapi) untuk data on-chain yang mendukung revenue tracking (Earn campaign verification) — risiko operasional jika layanan down.
- [token] Breakdown detail alokasi 22% (tim, foundation, treasury, ecosystem, advisors) tidak dipublikasikan; tidak ada vesting schedule on-chain (timelock/vesting contract) yang terverifikasi di block explorer untuk alokasi non-komunitas.
- [token] Circulating supply real-time tidak diungkap resmi; perbedaan antara total supply, supply yang sudah diklaim komunitas, dan supply yang dikontrol tim/CEX/DEX tidak transparan.
- [token] Status audit smart contract Jetton Master, Wallet AA (Paymaster/Bundler), dan Earn Campaign contracts — tidak ditemukan laporan audit publik dari auditor independen (Certik, Trail of Bits, SlowMist, dll).
- [token] Governance Snapshot bersifat advisory/non-binding; tidak ada DAO on-chain dengan eksekusi otomatis (timelock, multisig DAO) untuk proposal yang lulus voting.
- [token] Tidak ada burn mechanism, buyback, atau deflationary mechanism resmi; supply benar-benar fixed tanpa mekanisme pengurangan.
- [token] Alamat multisig/treasury resmi Open Builders untuk mengelola alokasi 22% tidak diungkap; tidak ada proof-of-reserves atau dashboard treasury publik.
- [token] Ketergantungan utility NOT pada Telegram Ads Platform & Telegram Mini App Store — perubahan kebijakan platform dapat menghilangkan utility secara tiba-tiba.
- [token] Detail fee structure Notcoin Earn (persentase potongan dari reward pool mitra) tidak diungkap; dampak ekonomi token tidak terukur.
- [token] Rencana "Notcoin v2 / Nettok" (multi-chain, AI) belum memiliki spesifikasi tokenomics baru (apakah NOT tetap single token, apakah ada token baru, bridge mechanism) — ketidakpastian utility jangka panjang.
- [token] Label holder on-chain (CEX, market maker, tim, foundation) tidak diverifikasi di block explorer; analisis konsentrasi whale bergantung pada heuristik, bukan label resmi.
- [market] Real-time circulating supply vs total supply discrepancy: CoinGecko & CoinMarketCap show different circulating supply values (ranging 90-95% of 102.7B); no official transparency dashboard from Notcoin to verify exact unlocked team/ecosystem tokens.
- [market] Post-TGE Daily Active Users (DAU) not publicly reported since mining phase ended (April 2024); current Mini App engagement (Explore, Earn, Wallet) metrics not disclosed.
- [market] DEX liquidity depth (NOT/TON pools) relatively shallow (~$3-6M TVL combined) vs CEX volume — potential slippage risk for large on-chain trades; no public market maker disclosure for DEX.
- [market] Token NOT market cap rank fluctuates between #50-#70; direct comparison to competitors (HMSTR, PIXFI, CATI, TAPS, TSN) complicated by different tokenomics, launch dates, and exchange listings.
- [market] Revenue figures for Telegram Ads Platform revenue share and Earn campaign fees not disclosed; unable to assess protocol sustainability or runway.
- [market] No DefiLlama/Token Terminal coverage — standard DeFi metrics (TVL, fees, revenue) not applicable but also not available for cross-project benchmarking.
- [market] Geographic user breakdown (top countries) not officially published; only inferred from Telegram demographics & community channel languages.
- [market] Smart contract audit status for Jetton Master, Wallet AA (Paymaster/Bundler), Earn Campaign contracts remains unverified (no public audit reports from Certik, Trail of Bits, etc.).
- [market] Vesting schedule for 22% team/ecosystem allocation not on-chain; no timelock/vesting contract addresses published — potential overhang risk unquantifiable.
- [market] "Notcoin v2 / Nettok" roadmap (EV-013) lacks technical specifications, tokenomics changes (if any), or launch timeline — market narrative impact uncertain.
- [market] Competitor HMSTR (Hamster Kombat) claims 300M+ users but TGE occurred later (Jul 2024); comparative retention & on-chain activity post-TGE not independently verified.
- [market] Blum (backed by Binance Labs) yet to launch token; points system may migrate users; competitive dynamics shifting.
- [market] CEX perpetual funding rates & open interest for NOT not tracked in standard analytics dashboards (Coinglass, etc. may have limited history).
- [market] No official investor relations contact or financial reporting calendar — market relies solely on blog announcements.
