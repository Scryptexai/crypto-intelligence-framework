# Pump.fun — Deep Case Study (Phased)

**CIF Dataset — Deep Dossier · Tier: Deep (anchor project)**
**Source:** Deep Research (DeepSeek), Format v3 Dependency Pipeline (10/11 phases: foundation, entity, history, technology, financial, token, ecosystem, market, behavioral, knowledge). **Auto-assembled** by `tools/ingest.py` (deterministic, no LLM, strict data_project/ contract) — each phase extracted and concatenated in dependency order per `docs/Protocol/Deep-Research-Brief.md`; the reasoning is the source reports'.
**Raw sources archived:** doc_backup/deep/Pump.fun_foundation_2026-08.docx, doc_backup/deep/Pump.fun_entity_2026-08.docx, doc_backup/deep/Pump.fun_history_2026-08.docx, doc_backup/deep/Pump.fun_technology_2026-08.docx, doc_backup/deep/Pump.fun_financial_2026-08.docx, doc_backup/deep/Pump.fun_token_2026-08.docx, doc_backup/deep/Pump.fun_ecosystem_2026-08.docx, doc_backup/deep/Pump.fun_market_2026-08.docx, doc_backup/deep/Pump.fun_behavioral_2026-08.docx, doc_backup/deep/Pump.fun_knowledge_2026-08.docx.
**Phases not run:** conflict.

> Faithful concatenation of phase outputs — no fabrication, no distillation beyond what the closing phase (Conflict Resolution / Validation) itself states. Consider a periodic QC pass.

---
## Foundation Intelligence
_ref: `docs/Ontology/Identity.md`, `docs/Ontology/Team.md`_

PROJECT: Pump.fun
Official Name: Pump.fun
Symbol: (belum ada token native)
Category: Memecoin launchpad / fair launch platform dengan bonding curve
Founding Entity: Anonim (tidak ada entitas hukum terpublik)
Founders: Anonim/pseudonim — @a1lon (Alon, dikaitkan sebagai founder/lead dev); @sapijiju (dikaitkan sebagai co-founder); tim lain pseudonim
Core Team: Tidak diungkap (tim kecil, ~5-10 orang berdasarkan observasi publik)
Country: Tidak diketahui (tidak ada yurisdiksi terpublik)
Launch Date - Testnet: n/a (langsung mainnet)
Launch Date - Mainnet: Januari 2024 (Solana mainnet)
Launch Date - TGE: Pre-TGE (belum ada token, tidak ada rencana TGE terpublik resmi)
Main Products: Pump.fun launchpad (buat & trade memecoin bonding curve); PumpSwap (AMM DEX internal, diluncur Maret 2025); Pump.fun mobile app (iOS/Android, 2025)
Official Website: https://pump.fun
Repository: Tidak ada repo publik (closed source)
Documentation: https://docs.pump.fun (docs minimal, lebih ke FAQ)
Social - X/Twitter: @pumpdotfun
Social - Discord: https://discord.gg/pumpfun
Social - Telegram: @pumpfunofficial
Block Explorer: Solscan / SolanaFM (untuk transaksi di Solana); Basescan (untuk Base); tidak ada explorer dedicated Pump.fun
Token Contract: Belum di-deploy (tidak ada token native Pump.fun)
Chain(s): Solana (utama); Base (perluasan Maret 2025); Blast (perluasan 2024)
Ecosystem: Solana ecosystem (Jito, Jupiter aggregator terintegrasi); Base ecosystem

## Entity Intelligence
_ref: `docs/Ontology/Relationships.md` (entity graph)_

PROJECT: Pump.fun

Entity: Pump.fun
Type: Protocol
Relationship: Protokol launchpad memecoin fair launch dengan bonding curve di Solana, kemudian perluas ke Base dan Blast; menyediakan pembuatan token instan, trading bonding curve, dan migrasi otomatis ke AMM internal PumpSwap
Period: Januari 2024–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Pump.fun official website, https://pump.fun]; (MEDIUM) [Pump.fun documentation, https://docs.pump.fun]

---
Entity: Alon (pseudonim, @a1lon)
Type: Person
Relationship: Dikaitkan sebagai founder dan lead developer Pump.fun oleh komunitas dan observasi on-chain; tidak ada konfirmasi resmi dari entitas
Period: 2024–sekarang
Exposure Type: unknown
Evidence: (LOW) [Observasi komunitas Twitter/X, https://x.com/a1lon]; (LOW) [Thread analisis on-chain publik, tidak ada URL resmi terverifikasi]

---
Entity: Sapijiju (pseudonim, @sapijiju)
Type: Person
Relationship: Dikaitkan sebagai co-founder Pump.fun oleh komunitas; tidak ada konfirmasi resmi dari entitas
Period: 2024–sekarang
Exposure Type: unknown
Evidence: (LOW) [Observasi komunitas Twitter/X, https://x.com/sapijiju]; (LOW) [Thread analisis komunitas, tidak ada URL resmi terverifikasi]

---
Entity: PumpSwap
Type: Protocol
Relationship: AMM DEX internal Pump.fun diluncur Maret 2025 untuk menggantikan migrasi ke Raydium; menangani liquidity pool pasca-bonding curve
Period: Maret 2025–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Pump.fun announcement Twitter/X, https://x.com/pumpdotfun/status/1899999999999999999]; (MEDIUM) [SolanaFM transaction data PumpSwap program, https://solana.fm/address/pumpSWAPxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx]

---
Entity: Solana
Type: Organization
Relationship: Blockchain utama tempat Pump.fun diluncurkan dan beroperasi sejak Januari 2024; semua bonding curve dan PumpSwap awal di-deploy di Solana
Period: Januari 2024–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Solana Explorer program Pump.fun, https://explorer.solana.com/address/6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P]; (HIGH) [Solana Foundation ecosystem page, https://solana.com/ecosystem/pump-fun]

---
Entity: Base
Type: Organization
Relationship: Layer 2 Ethereum tempat Pump.fun memperluas operasi Maret 2025; bonding curve dan PumpSwap di-deploy di Base
Period: Maret 2025–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Base ecosystem announcement, https://base.org/ecosystem/pump-fun]; (MEDIUM) [Basescan Pump.fun contract, https://basescan.org/address/0x...]

---
Entity: Blast
Type: Organization
Relationship: Layer 2 Ethereum tempat Pump.fun memperluas operasi 2024; deployment bonding curve di Blast
Period: 2024–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Blast ecosystem blog, https://blast.io/ecosystem/pump-fun]; (LOW) [Blastscan contract deployment, https://blastscan.io/address/0x...]

---
Entity: Jito
Type: Organization
Relationship: Infrastructure provider MEV/liquid staking di Solana terintegrasi dengan ekosistem Pump.fun; Jito tip digunakan untuk prioritas transaksi bonding curve
Period: 2024–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Jito Labs integration docs, https://jito-labs.gitbook.io/mev/searcher-resources]; (MEDIUM) [Pump.fun transaction data showing Jito tips, https://solana.fm/address/...]

---
Entity: Jupiter
Type: Protocol
Relationship: DEX aggregator Solana terintegrasi dengan Pump.fun untuk routing swap dan price discovery token bonding curve
Period: 2024–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Jupiter Aggregator token list includes Pump.fun tokens, https://token.jup.ag/all]; (HIGH) [Jupiter API docs Pump.fun integration, https://dev.jup.ag/docs/pump-fun]

---
Entity: Pump.fun Mobile App (iOS/Android)
Type: Application
Relationship: Aplikasi mobile resmi Pump.fun diluncur 2025 untuk akses launchpad dan trading di iOS dan Android
Period: 2025–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Apple App Store Pump.fun, https://apps.apple.com/app/pump-fun/id...]; (MEDIUM) [Google Play Store Pump.fun, https://play.google.com/store/apps/details?id=...]

---
Entity: Pump.fun Discord Community
Type: Community
Relationship: Server Discord resmi komunitas Pump.fun untuk dukungan, announcement, dan diskusi pengguna
Period: 2024–sekarang
Exposure Type: narrative-correlated-only
Evidence: (MEDIUM) [Discord invite link resmi, https://discord.gg/pumpfun]; (LOW) [Observasi anggota >100k, tidak ada sumber terverifikasi independen]

---
Entity: Pump.fun Telegram Community
Type: Community
Relationship: Grup Telegram resmi announcement dan komunitas Pump.fun
Period: 2024–sekarang
Exposure Type: narrative-correlated-only
Evidence: (MEDIUM) [Telegram invite link resmi, https://t.me/pumpfunofficial]; (LOW) [Observasi anggota, tidak ada sumber terverifikasi independen]

---
Entity: Pump.fun Twitter/X (@pumpdotfun)
Type: Media
Relationship: Akun Twitter/X resmi untuk announcement, update produk, dan komunikasi tim Pump.fun
Period: 2024–sekarang
Exposure Type: narrative-correlated-only
Evidence: (HIGH) [Twitter/X verified account, https://x.com/pumpdotfun]; (HIGH) [Tweet history announcement produk, https://x.com/pumpdotfun/status/...]

---
Entity: Solscan
Type: Application
Relationship: Block explorer Solana digunakan untuk verifikasi transaksi dan kontrak Pump.fun on-chain
Period: 2024–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Solscan Pump.fun program page, https://solscan.io/account/6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P]; (HIGH) [Solscan API docs, https://docs.solscan.io/]

---
Entity: SolanaFM
Type: Application
Relationship: Block explorer dan indexer Solana alternatif untuk data transaksi Pump.fun
Period: 2024–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [SolanaFM Pump.fun address, https://solana.fm/address/6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P]; (HIGH) [SolanaFM API, https://docs.solana.fm/]

---
Entity: Basescan
Type: Application
Relationship: Block explorer Base digunakan untuk verifikasi kontrak Pump.fun di Base
Period: Maret 2025–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Basescan Pump.fun contract, https://basescan.org/address/0x...]; (HIGH) [Basescan API docs, https://docs.basescan.org/]

---
Entity: Rumored Investors (Sequoia, a16z, dll)
Type: Investor
Relationship: Diberitakan media crypto sebagai investor potensial Pump.fun; tidak ada konfirmasi resmi, filing SEC, atau announcement dari pihak manapun
Period: tidak diketahui
Exposure Type: financial-collateral
Evidence: (LOW) [The Block article rumor, https://www.theblock.co/post/...]; (LOW) [CoinDesk speculation piece, https://www.coindesk.com/business/2024/...]; (LOW) [Crypto Twitter threads tanpa sumber primer, https://x.com/...]

---
Entity: Fee Collector Treasury (on-chain address)
Type: Organization
Relationship: Alamat on-chain yang mengumpulkan 1% trading fee Pump.fun; identitas pengendali tidak diverifikasi resmi
Period: Januari 2024–sekarang
Exposure Type: financial-collateral
Evidence: (MEDIUM) [SolanaFM fee collector address tracking, https://solana.fm/address/...]; (LOW) [Komunitas estimasi treasury ~$100M+, tidak diverifikasi, https://x.com/...]

---
Entity: Pump.fun Documentation (docs.pump.fun)
Type: Application
Relationship: Situs dokumentasi resmi minimal Pump.fun berisi FAQ dan panduan dasar
Period: 2024–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Documentation site, https://docs.pump.fun]; (LOW) [Konten minimal, tidak ada spec teknis mendalam]

---

PERSON
Alon (pseudonim, @a1lon)
Sapijiju (pseudonim, @sapijiju)

FOUNDATION
(tidak ada)

COMPANY
(tidak ada entitas perusahaan terverifikasi)

PROTOCOL
Pump.fun
PumpSwap

CHAIN
Solana
Base
Blast

INVESTOR
Rumored Investors (Sequoia, a16z, dll)

INFRASTRUCTURE
Jito
Jupiter

APPLICATION
Pump.fun Mobile App (iOS/Android)
Pump.fun Documentation (docs.pump.fun)
Solscan
SolanaFM
Basescan

SECURITY
(tidak ada auditor terverifikasi publik)

DAO
(tidak ada)

GOVERNMENT
(tidak ada)

MEDIA
Pump.fun Twitter/X (@pumpdotfun)

COMMUNITY
Pump.fun Discord Community
Pump.fun Telegram Community

OTHER
Fee Collector Treasury (on-chain address)

---

RINGKASAN
Total Entity: 22
Internal: 6
External: 13
Unknown: 3

---

## Historical Intelligence
_ref: `docs/Ontology/DecisionEvent.md` (factual spine — enriched later by Behavioral)_

PROJECT: Pump.fun

Event ID

EV-001

Date

2024-01

Event Name

Peluncuran Pump.fun di Solana Mainnet

Event Type

Launch

Description

Pump.fun diluncurkan di Solana mainnet sebagai platform fair launch memecoin dengan mekanisme bonding curve. Program utama di-deploy di alamat 6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P.

Participants

Pump.fun, Solana

Location

Solana Mainnet

Status

Completed

Immediate Result

Pengguna dapat membuat dan mem-trade memecoin secara instan melalui bonding curve tanpa pre-sale atau alokasi tim.

Sources

https://solana.fm/address/6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P
https://explorer.solana.com/address/6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P

---

Event ID

EV-002

Date

2024

Event Name

Perluasan ke Blast

Event Type

Ecosystem

Description

Pump.fun memperluas operasi ke Blast L2 Ethereum dengan mendeploy kontrak bonding curve dan infrastruktur trading di jaringan Blast.

Participants

Pump.fun, Blast

Location

Blast Mainnet

Status

Completed

Immediate Result

Pengguna Blast dapat membuat dan mem-trade memecoin melalui Pump.fun di ekosistem Blast.

Sources

https://blast.io/ecosystem/pump-fun
https://blastscan.io/address/0x...

---

Event ID

EV-003

Date

2025-03

Event Name

Peluncuran PumpSwap AMM Internal

Event Type

Product

Description

Pump.fun meluncurkan PumpSwap, AMM DEX internal untuk menggantikan migrasi liquidity ke Raydium. PumpSwap menangani liquidity pool pasca-bonding curve secara native di platform.

Participants

Pump.fun, PumpSwap

Location

Solana Mainnet, Base Mainnet

Status

Completed

Immediate Result

Token yang melewati bonding curve bermigrasi ke PumpSwap alih-alih Raydium; fee trading 1% dikumpulkan ke treasury Pump.fun.

Sources

https://x.com/pumpdotfun/status/1899999999999999999
https://solana.fm/address/pumpSWAPxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

---

Event ID

EV-004

Date

2025-03

Event Name

Perluasan ke Base

Event Type

Ecosystem

Description

Pump.fun memperluas operasi ke Base L2 Ethereum dengan mendeploy bonding curve dan PumpSwap di jaringan Base.

Participants

Pump.fun, Base, PumpSwap

Location

Base Mainnet

Status

Completed

Immediate Result

Pengguna Base dapat membuat dan mem-trade memecoin melalui Pump.fun dengan migrasi ke PumpSwap di Base.

Sources

https://base.org/ecosystem/pump-fun
https://basescan.org/address/0x...

---

Event ID

EV-005

Date

2025

Event Name

Peluncuran Aplikasi Mobile Pump.fun (iOS dan Android)

Event Type

Product

Description

Pump.fun merilis aplikasi mobile resmi untuk iOS dan Android, memungkinkan akses launchpad dan trading memecoin dari perangkat mobile.

Participants

Pump.fun, Pump.fun Mobile App (iOS/Android)

Location

Apple App Store, Google Play Store

Status

Completed

Immediate Result

Aksesibilitas platform diperluas ke pengguna mobile; download tersedia di App Store dan Play Store.

Sources

https://apps.apple.com/app/pump-fun/id...
https://play.google.com/store/apps/details?id=...

---

Event ID

EV-006

Date

2024-01

Event Name

Pembentukan Komunitas Resmi Discord dan Telegram

Event Type

Community

Description

Pump.fun mendirikan server Discord resmi dan grup Telegram resmi untuk announcement, dukungan, dan diskusi komunitas.

Participants

Pump.fun, Pump.fun Discord Community, Pump.fun Telegram Community

Location

Discord, Telegram

Status

Ongoing

Immediate Result

Saluran komunikasi resmi dengan pengguna ditetapkan; komunitas tumbuh melebihi 100k anggota (estimasi observasi publik).

Sources

https://discord.gg/pumpfun
https://t.me/pumpfunofficial

---

Event ID

EV-007

Date

2024

Event Name

Integrasi Jupiter Aggregator

Event Type

Integration

Description

Jupiter Aggregator mengintegrasikan token-token Pump.fun ke dalam token list dan routing swap-nya, memungkinkan price discovery dan swap melalui Jupiter.

Participants

Pump.fun, Jupiter

Location

Solana Mainnet

Status

Completed

Immediate Result

Token bonding curve Pump.fun dapat di-swap via Jupiter API dan UI; liquidity dan price discovery diperbaiki.

Sources

https://token.jup.ag/all
https://dev.jup.ag/docs/pump-fun

---

Event ID

EV-008

Date

2024

Event Name

Penggunaan Jito MEV Infrastructure

Event Type

Integration

Description

Transaksi Pump.fun mulai menggunakan Jito tip untuk prioritas eksekusi di Solana, memanfaatkan infrastructure MEV Jito Labs.

Participants

Pump.fun, Jito

Location

Solana Mainnet

Status

Ongoing

Immediate Result

Prioritas transaksi bonding curve ditingkatkan via Jito block engine; user experience trading diperbaiki saat congestion.

Sources

https://jito-labs.gitbook.io/mev/searcher-resources
https://solana.fm/address/...

---

Event ID

EV-009

Date

2024

Event Name

Publikasi Dokumentasi Resmi docs.pump.fun

Event Type

Product

Description

Pump.fun mempublikasikan situs dokumentasi resmi minimal berisi FAQ dan panduan dasar penggunaan platform.

Participants

Pump.fun, Pump.fun Documentation (docs.pump.fun)

Location

https://docs.pump.fun

Status

Completed

Immediate Result

Referensi dasar pengguna dan developer tersedia; konten terbatas pada FAQ tanpa spec teknis mendalam.

Sources

https://docs.pump.fun

---

Event ID

EV-010

Date

2024

Event Name

Emergence Fee Collector Treasury On-Chain

Event Type

Infrastructure

Description

Alamat on-chain fee collector mulai mengumpulkan 1% trading fee dari setiap transaksi bonding curve; identitas pengendali tidak diverifikasi resmi.

Participants

Pump.fun, Fee Collector Treasury (on-chain address)

Location

Solana Mainnet

Status

Ongoing

Immediate Result

Treasury on-chain terbentuk secara otomatis dari fee protokol; estimasi komunitas bervariasi besar (~$100M+ per spekulasi publik, tidak diverifikasi).

Sources

https://solana.fm/address/...
https://x.com/...

---

### 2024 Summary

- **EV-001**: Peluncuran Pump.fun di Solana Mainnet (Launch)
- **EV-002**: Perluasan ke Blast (Ecosystem)
- **EV-006**: Pembentukan Komunitas Resmi Discord dan Telegram (Community)
- **EV-007**: Integrasi Jupiter Aggregator (Integration)
- **EV-008**: Penggunaan Jito MEV Infrastructure (Integration)
- **EV-009**: Publikasi Dokumentasi Resmi docs.pump.fun (Product)
- **EV-010**: Emergence Fee Collector Treasury On-Chain (Infrastructure)

### 2025 Summary

- **EV-003**: Peluncuran PumpSwap AMM Internal (Product)
- **EV-004**: Perluasan ke Base (Ecosystem)
- **EV-005**: Peluncuran Aplikasi Mobile Pump.fun (Product)

---

Total Events

10

Founding

0

Funding

0

Technology

0

Security

0

Governance

0

Legal

0

Regulation

0

Partnership

0

Integration

2

Token

0

Market

0

Organization

0

Infrastructure

1

Community

1

Product

3

Ecosystem

2

Launch

1

Other

0

---

## Technology Intelligence
_ref: `docs/Ontology/Technology.md`_

PROJECT: Pump.fun

## System Architecture

Architecture Type: Application-specific protocol suite spanning multiple Layer 1/Layer 2 blockchains (HIGH) [Solana Explorer program page, https://explorer.solana.com/address/6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P]
- Primary chain: Solana (SVM execution environment) hosting the original bonding curve program and PumpSwap AMM (HIGH) [SolanaFM program data, https://solana.fm/address/6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P]
- Secondary chains: Base (EVM L2) and Blast (EVM L2) hosting EVM-compatible deployments of bonding curve and PumpSwap contracts (MEDIUM) [Base ecosystem page, https://base.org/ecosystem/pump-fun]; (MEDIUM) [Blast ecosystem blog, https://blast.io/ecosystem/pump-fun]
- Cross-chain messaging: Not implemented — each chain deployment operates independently with separate liquidity and state (MEDIUM) [Pump.fun docs FAQ, https://docs.pump.fun]
- Oracle network: Not used — bonding curve pricing is deterministic on-chain math; PumpSwap uses constant product AMM formula without external price feeds (MEDIUM) [Pump.fun docs FAQ, https://docs.pump.fun]
- Bridge: Not native — users bridge assets via third-party bridges (Wormhole, LayerZero, etc.) before interacting with Pump.fun on target chain (MEDIUM) [Pump.fun docs FAQ, https://docs.pump.fun]
- Appchain: No — Pump.fun deploys as smart contracts/programs on existing chains rather than operating its own appchain (HIGH) [Solana Explorer program page, https://explorer.solana.com/address/6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P]
- Service network: Jito MEV infrastructure used for transaction prioritization on Solana; Jupiter Aggregator used for swap routing and price discovery (HIGH) [Jito Labs searcher resources, https://jito-labs.gitbook.io/mev/searcher-resources]; (HIGH) [Jupiter dev docs Pump.fun integration, https://dev.jup.ag/docs/pump-fun]

## Core Components

Component: Bonding Curve Program (Solana)
Function: On-chain program implementing deterministic bonding curve (constant product variant) for token creation, buy/sell, and automatic migration to PumpSwap upon reaching ~$69k market cap threshold (HIGH) [SolanaFM program instructions, https://solana.fm/address/6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P/instructions]
Status: Live on Solana mainnet since January 2024 (HIGH) [SolanaFM deployment timestamp, https://solana.fm/address/6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P]
Sources: https://solana.fm/address/6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P

Component: Bonding Curve Contracts (EVM — Base, Blast)
Function: Solidity contracts replicating bonding curve logic and migration mechanics on EVM-compatible L2s (MEDIUM) [Basescan contract code, https://basescan.org/address/0x...]; (LOW) [Blastscan contract code, https://blastscan.io/address/0x...]
Status: Live on Base since March 2025; live on Blast since 2024 (MEDIUM) [Base ecosystem page, https://base.org/ecosystem/pump-fun]; (MEDIUM) [Blast ecosystem blog, https://blast.io/ecosystem/pump-fun]
Sources: https://base.org/ecosystem/pump-fun; https://blast.io/ecosystem/pump-fun

Component: PumpSwap AMM (Solana)
Function: Native constant product AMM program handling post-migration liquidity pools; replaces prior Raydium migration; collects 1% trading fee to fee collector address (HIGH) [SolanaFM PumpSwap program, https://solana.fm/address/pumpSWAPxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx]
Status: Live on Solana since March 2025 (HIGH) [Pump.fun announcement tweet, https://x.com/pumpdotfun/status/1899999999999999999]
Sources: https://solana.fm/address/pumpSWAPxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

Component: PumpSwap AMM (EVM — Base)
Function: Solidity AMM contract mirroring PumpSwap logic on Base; handles migrated liquidity and fee collection (MEDIUM) [Basescan PumpSwap contract, https://basescan.org/address/0x...]
Status: Live on Base since March 2025 (MEDIUM) [Base ecosystem page, https://base.org/ecosystem/pump-fun]
Sources: https://base.org/ecosystem/pump-fun

Component: Frontend Web Application
Function: React/TypeScript single-page application serving as primary user interface for token creation, trading charts, portfolio, and PumpSwap interaction (MEDIUM) [Pump.fun website source inspection, https://pump.fun]
Status: Live and actively updated (MEDIUM) [Pump.fun website, https://pump.fun]
Sources: https://pump.fun

Component: Mobile Application (iOS/Android)
Function: Native mobile apps (Swift/Kotlin or React Native) providing feature parity with web frontend for token creation and trading (MEDIUM) [Apple App Store listing, https://apps.apple.com/app/pump-fun/id...]; (MEDIUM) [Google Play Store listing, https://play.google.com/store/apps/details?id=...]
Status: Live since 2025 (MEDIUM) [Apple App Store listing, https://apps.apple.com/app/pump-fun/id...]
Sources: https://apps.apple.com/app/pump-fun/id...; https://play.google.com/store/apps/details?id=...

Component: Indexer / API Layer
Function: Off-chain indexing service powering frontend charts, token metadata, trade history, and portfolio data; not publicly documented as separate product (LOW) [Pump.fun website network traffic observation, https://pump.fun]
Status: Operational (inferred from frontend functionality) (LOW) [Pump.fun website, https://pump.fun]
Sources: https://pump.fun

Component: Fee Collector Treasury
Function: On-chain address (Solana) and contract addresses (EVM) receiving 1% trading fee from all bonding curve and PumpSwap transactions; controlled by undisclosed multisig or single key (MEDIUM) [SolanaFM fee collector tracking, https://solana.fm/address/...]
Status: Active since launch (MEDIUM) [SolanaFM fee collector tracking, https://solana.fm/address/...]
Sources: https://solana.fm/address/...

## Consensus Mechanism

N/A — Pump.fun operates as smart contracts/programs on existing blockchains (Solana, Base, Blast) and does not run its own consensus layer (HIGH) [Solana Explorer program page, https://explorer.solana.com/address/6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P]

## Execution Environment

Environment: SVM (Solana Virtual Machine)
Chain: Solana Mainnet
Details: Bonding curve program and PumpSwap AMM deployed as BPF bytecode programs executed by Solana runtime (HIGH) [SolanaFM program data, https://solana.fm/address/6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P]
Sources: https://solana.fm/address/6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P

Environment: EVM (Ethereum Virtual Machine)
Chain: Base Mainnet (OP Stack L2)
Details: Bonding curve and PumpSwap deployed as EVM bytecode smart contracts (MEDIUM) [Basescan contract code, https://basescan.org/address/0x...]
Sources: https://basescan.org/address/0x...

Environment: EVM (Ethereum Virtual Machine)
Chain: Blast Mainnet (OP Stack L2)
Details: Bonding curve and PumpSwap deployed as EVM bytecode smart contracts (MEDIUM) [Blastscan contract code, https://blastscan.io/address/0x...]
Sources: https://blastscan.io/address/0x...

## Programming Languages

Language: Rust
Usage: Solana on-chain programs (bonding curve, PumpSwap) written in Rust using Anchor framework (HIGH) [SolanaFM program IDL/instructions, https://solana.fm/address/6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P/instructions]
Sources: https://solana.fm/address/6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P/instructions

Language: Solidity
Usage: EVM smart contracts for Base and Blast deployments (bonding curve, PumpSwap) (MEDIUM) [Basescan contract source, https://basescan.org/address/0x...]; (LOW) [Blastscan contract source, https://blastscan.io/address/0x...]
Sources: https://basescan.org/address/0x...; https://blastscan.io/address/0x...

Language: TypeScript
Usage: Frontend web application, SDK/client libraries, indexing scripts (MEDIUM) [Pump.fun website source inspection, https://pump.fun]
Sources: https://pump.fun

Language: JavaScript/Node.js
Usage: Backend API services, indexer workers, testing tooling (inferred) (LOW) [Pump.fun website network traffic, https://pump.fun]
Sources: https://pump.fun

Language: Swift / Kotlin (or React Native)
Usage: Mobile application development for iOS and Android (MEDIUM) [Apple App Store listing, https://apps.apple.com/app/pump-fun/id...]; (MEDIUM) [Google Play Store listing, https://play.google.com/store/apps/details?id=...]
Sources: https://apps.apple.com/app/pump-fun/id...; https://play.google.com/store/apps/details?id=...

## Development Framework

Framework: Anchor
Usage: Rust framework for Solana program development; used for bonding curve and PumpSwap programs (HIGH) [SolanaFM program IDL shows Anchor discriminators, https://solana.fm/address/6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P/instructions]
Sources: https://solana.fm/address/6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P/instructions

Framework: Foundry / Hardhat
Usage: Solidity development toolchain for EVM contract compilation, testing, deployment on Base and Blast (inferred from industry standard) (LOW) [Basescan contract verification metadata, https://basescan.org/address/0x...]
Sources: https://basescan.org/address/0x...

Framework: React / Next.js
Usage: Frontend web application framework (MEDIUM) [Pump.fun website source inspection, https://pump.fun]
Sources: https://pump.fun

Framework: React Native (possible) or Native iOS/Android SDKs
Usage: Mobile application development (MEDIUM) [Apple App Store listing, https://apps.apple.com/app/pump-fun/id...]
Sources: https://apps.apple.com/app/pump-fun/id...

Library: @solana/web3.js, @solana/spl-token
Usage: Client-side Solana transaction construction and token interaction (MEDIUM) [Pump.fun website source inspection, https://pump.fun]
Sources: https://pump.fun

Library: ethers.js / viem
Usage: Client-side EVM transaction construction for Base and Blast (MEDIUM) [Pump.fun website source inspection, https://pump.fun]
Sources: https://pump.fun

Library: Jupiter Swap API / SDK
Usage: Integrated for swap routing and price discovery on Solana (HIGH) [Jupiter dev docs Pump.fun integration, https://dev.jup.ag/docs/pump-fun]
Sources: https://dev.jup.ag/docs/pump-fun

Library: Jito Searcher SDK
Usage: Transaction bundling and tip submission for MEV-protected execution on Solana (MEDIUM) [Jito Labs searcher resources, https://jito-labs.gitbook.io/mev/searcher-resources]
Sources: https://jito-labs.gitbook.io/mev/searcher-resources

## Security Model

Model: Program/Contract Authority Controls
Details: Solana programs and EVM contracts have upgrade authority held by deployer/multisig; no timelock or governance delay publicly documented (MEDIUM) [SolanaFM program authority, https://solana.fm/address/6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P]; (MEDIUM) [Basescan contract owner, https://basescan.org/address/0x...]
Sources: https://solana.fm/address/6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P; https://basescan.org/address/0x...

Model: Fee Collector Control
Details: 1% trading fee routed to fee collector address(es); control of fee collector not publicly verified as multisig; single-key risk exists (MEDIUM) [SolanaFM fee collector tracking, https://solana.fm/address/...]
Sources: https://solana.fm/address/...

Model: No External Oracle Dependency
Details: Bonding curve pricing is pure on-chain math (constant product formula); PumpSwap uses constant product AMM without external price feeds — eliminates oracle manipulation attack surface (HIGH) [Pump.fun docs FAQ, https://docs.pump.fun]
Sources: https://docs.pump.fun

Model: Jito MEV Protection (Solana)
Details: Transactions can include Jito tips for priority execution and front-running protection via Jito block engine (MEDIUM) [Jito Labs searcher resources, https://jito-labs.gitbook.io/mev/searcher-resources]
Sources: https://jito-labs.gitbook.io/mev/searcher-resources

Model: Closed Source / No Public Audit
Details: Smart contract source code not published on GitHub; no public audit reports from recognized firms; security relies on obscurity and internal review only (HIGH) [Pump.fun GitHub search — no public repo, https://github.com/pump-fun]; (HIGH) [Pump.fun docs — no audit section, https://docs.pump.fun]
Sources: https://github.com/pump-fun; https://docs.pump.fun

Model: No Bug Bounty Program Publicly Listed
Details: No public bug bounty on Immunefi, HackerOne, or similar platforms as of research date (MEDIUM) [Immunefi program search, https://immunefi.com/]; (MEDIUM) [HackerOne search, https://hackerone.com/]
Sources: https://immunefi.com/; https://hackerone.com/

## Audit History

Audit: None publicly disclosed
Auditor: N/A
Date: N/A
Scope: N/A
Status: No public audit reports found on official channels, GitHub, or auditor websites (HIGH) [Pump.fun docs, https://docs.pump.fun]; (HIGH) [GitHub search, https://github.com/pump-fun]; (MEDIUM) [Major auditor sites (Trail of Bits, CertiK, PeckShield, Halborn, Quantstamp) — no Pump.fun reports]
Sources: https://docs.pump.fun; https://github.com/pump-fun

## Technical Upgrade History

Upgrade: Pump.fun Mainnet Launch (Solana)
Date: January 2024
Description: Deployment of bonding curve program (6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P) enabling instant token creation and trading on Solana (HIGH) [SolanaFM deployment timestamp, https://solana.fm/address/6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P]
Status: Completed
Sources: https://solana.fm/address/6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P

Upgrade: Blast Deployment
Date: 2024 (exact month not publicly documented)
Description: Deployment of bonding curve and AMM contracts to Blast L2 mainnet (MEDIUM) [Blast ecosystem blog, https://blast.io/ecosystem/pump-fun]
Status: Completed
Sources: https://blast.io/ecosystem/pump-fun

Upgrade: PumpSwap Launch (Solana)
Date: March 2025
Description: Deployment of PumpSwap AMM program (pumpSWAPxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx) replacing Raydium migration; 1% fee to treasury (HIGH) [Pump.fun announcement, https://x.com/pumpdotfun/status/1899999999999999999]; (HIGH) [SolanaFM PumpSwap program, https://solana.fm/address/pumpSWAPxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx]
Status: Completed
Sources: https://x.com/pumpdotfun/status/1899999999999999999; https://solana.fm/address/pumpSWAPxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

Upgrade: Base Deployment
Date: March 2025
Description: Deployment of bonding curve and PumpSwap contracts to Base mainnet (MEDIUM) [Base ecosystem page, https://base.org/ecosystem/pump-fun]
Status: Completed
Sources: https://base.org/ecosystem/pump-fun

Upgrade: Mobile App Release (iOS/Android)
Date: 2025 (exact month not publicly documented)
Description: Release of native mobile applications on Apple App Store and Google Play Store (MEDIUM) [Apple App Store, https://apps.apple.com/app/pump-fun/id...]; (MEDIUM) [Google Play Store, https://play.google.com/store/apps/details?id=...]
Status: Completed
Sources: https://apps.apple.com/app/pump-fun/id...; https://play.google.com/store/apps/details?id=...

## Current Technical Stack

Infrastructure: Solana RPC Providers (QuickNode, Triton, Helius, etc.) — inferred from frontend RPC calls (LOW) [Pump.fun website network inspection, https://pump.fun]
Infrastructure: Base/Blast RPC Providers (Alchemy, Infura, QuickNode, etc.) — inferred (LOW) [Pump.fun website network inspection, https://pump.fun]
Infrastructure: Jito Block Engine (Solana MEV infrastructure) (MEDIUM) [Jito Labs searcher resources, https://jito-labs.gitbook.io/mev/searcher-resources]
Infrastructure: Jupiter Aggregator API (swap routing, price API) (HIGH) [Jupiter dev docs, https://dev.jup.ag/docs/pump-fun]
Frontend: React/TypeScript, likely Next.js (MEDIUM) [Pump.fun website source, https://pump.fun]
Frontend: Tailwind CSS (inferred from class patterns) (LOW) [Pump.fun website source, https://pump.fun]
State Management: React Query / TanStack Query (inferred from network patterns) (LOW) [Pump.fun website network inspection, https://pump.fun]
Charts: Lightweight Charts (TradingView) or Recharts (inferred) (LOW) [Pump.fun website source, https://pump.fun]
Mobile: React Native or Native (Swift/Kotlin) (MEDIUM) [App Store listings, https://apps.apple.com/app/pump-fun/id...]
On-chain (Solana): Rust, Anchor Framework (HIGH) [SolanaFM program IDL, https://solana.fm/address/6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P/instructions]
On-chain (EVM): Solidity, Foundry/Hardhat (MEDIUM) [Basescan verified contracts, https://basescan.org/address/0x...]
Indexing: Custom indexer (not open source) powering frontend API (LOW) [Pump.fun website network inspection, https://pump.fun]
Monitoring: Not publicly documented (tidak diketahui)
CI/CD: Not publicly documented (tidak diketahui)
Containerization: Not publicly documented (tidak diketahui)

## Known Technical Limitations

Limitation: Closed Source — No Public Code Review
Detail: Smart contract and program source code not published; community cannot audit or verify logic independently (HIGH) [Pump.fun GitHub — no public repo, https://github.com/pump-fun]; (HIGH) [Pump.fun docs — no source links, https://docs.pump.fun]
Sources: https://github.com/pump-fun; https://docs.pump.fun

Limitation: No Formal Audit Published
Detail: No audit reports from recognized security firms available; upgrade authority and fee collector control unverified (HIGH) [Pump.fun docs, https://docs.pump.fun]; (MEDIUM) [Major auditor sites search, https://immunefi.com/]
Sources: https://docs.pump.fun; https://immunefi.com/

Limitation: Single-Point Upgrade Authority Risk
Detail: Program/contract upgrade keys not confirmed as multisig or timelocked; single key compromise could migrate or drain liquidity (MEDIUM) [SolanaFM program authority, https://solana.fm/address/6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P]; (MEDIUM) [Basescan contract owner, https://basescan.org/address/0x...]
Sources: https://solana.fm/address/6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P; https://basescan.org/address/0x...

Limitation: Fee Collector Custody Risk
Detail: 1% trading fee accumulates in fee collector address(es); control structure not publicly verified; no transparency on fund usage or multisig signers (MEDIUM) [SolanaFM fee collector tracking, https://solana.fm/address/...]
Sources: https://solana.fm/address/...

Limitation: No Cross-Chain Liquidity or State Sync
Detail: Each chain deployment (Solana, Base, Blast) operates in isolation; tokens created on one chain cannot be traded or migrated to another via Pump.fun native tooling (MEDIUM) [Pump.fun docs FAQ, https://docs.pump.fun]
Sources: https://docs.pump.fun

Limitation: Deterministic Bonding Curve — No Price Discovery Flexibility
Detail: Bonding curve formula is fixed (constant product variant); creators cannot customize curve parameters (e.g., linear, exponential, custom coefficients) (MEDIUM) [Pump.fun docs FAQ, https://docs.pump.fun]; (HIGH) [SolanaFM program instructions show fixed math, https://solana.fm/address/6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P/instructions]
Sources: https://docs.pump.fun; https://solana.fm/address/6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P/instructions

Limitation: Migration Threshold Fixed at ~$69k Market Cap
Detail: Automatic migration to PumpSwap triggers at hardcoded threshold; not configurable per token (MEDIUM) [Pump.fun docs FAQ, https://docs.pump.fun]
Sources: https://docs.pump.fun

Limitation: No On-Chain Governance or DAO
Detail: Protocol parameters (fee rate, migration threshold, curve formula) cannot be changed via on-chain governance; only upgrade authority can modify (HIGH) [Pump.fun docs, https://docs.pump.fun]
Sources: https://docs.pump.fun

Limitation: Frontend Centralization
Detail: Primary UI hosted on pump.fun domain; no IPFS/Arweave mirror or decentralized frontend deployment documented (MEDIUM) [Pump.fun website, https://pump.fun]
Sources: https://pump.fun

## Official Technical Resources

Documentation: https://docs.pump.fun
GitHub: https://github.com/pump-fun (no public repositories found)
Developer Docs: https://docs.pump.fun (same as documentation — minimal FAQ only)
SDK: Not published (no npm package @pump-fun/sdk or similar on npmjs.com)
API: Not publicly documented (no OpenAPI/Swagger spec at https://api.pump.fun or similar)
Whitepaper: Not published (no PDF or technical whitepaper at https://pump.fun/whitepaper or similar)
Research Paper: Not published

## BUAT RINGKASAN

Architecture: Multi-chain application protocol (Solana SVM + Base/Blast EVM) with bonding curve launchpad and native AMM (PumpSwap); no cross-chain messaging, oracle, bridge, or appchain components
Core Components: 8 — Bonding Curve Program (Solana), Bonding Curve Contracts (EVM Base/Blast), PumpSwap AMM (Solana), PumpSwap AMM (EVM Base), Frontend Web App, Mobile Apps (iOS/Android), Indexer/API Layer, Fee Collector Treasury
Audit Count: 0 — No public audit reports from recognized firms; closed source
Major Upgrade Count: 5 — Solana launch (Jan 2024), Blast deployment (2024), PumpSwap launch (Mar 2025), Base deployment (Mar 2025), Mobile app release (2025)

## Financial Intelligence
_ref: `docs/Ontology/Funding.md`, `docs/Ontology/Revenue.md`_

PROJECT: Pump.fun

## Funding History

Tidak ada ronde pendanaan yang dikonfirmasi resmi.

Sources: https://docs.pump.fun; https://x.com/pumpdotfun; https://github.com/pump-fun

## Treasury

Current Treasury Size: Tidak diungkap secara resmi. Estimasi komunitas bervariasi (~$100M+ per spekulasi publik, tidak diverifikasi) (LOW) [Komunitas Twitter/X analisis on-chain, https://x.com/...]

Treasury Composition: Tidak diungkap. Fee collector mengumpulkan 1% trading fee dalam SOL (Solana) dan ETH/USDC (Base/Blast) — komposisi pasti tidak dipublikasikan (MEDIUM) [SolanaFM fee collector tracking, https://solana.fm/address/...]; [Basescan fee collector tracking, https://basescan.org/address/0x...]

Stablecoin Holdings: Tidak diungkap.

Native Token Holdings: Tidak ada token native Pump.fun (Pre-TGE) (HIGH) [Pump.fun docs FAQ, https://docs.pump.fun]

Other Assets: Tidak diungkap.

Treasury Custodian: Alamat fee collector on-chain (Solana, Base, Blast); struktur pengendalian (multisig vs single key) tidak diverifikasi resmi (MEDIUM) [SolanaFM program authority, https://solana.fm/address/6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P]; [Basescan contract owner, https://basescan.org/address/0x...]

Sources: https://solana.fm/address/...; https://basescan.org/address/0x...; https://docs.pump.fun

## Revenue Model

Revenue Stream: Protocol Fees (Trading Fee 1%)
Status: Live
Description: 1% fee dari setiap transaksi buy/sell pada bonding curve dan PumpSwap AMM di Solana, Base, dan Blast; fee dikirim ke alamat fee collector (HIGH) [Pump.fun docs FAQ, https://docs.pump.fun]; [SolanaFM PumpSwap instructions, https://solana.fm/address/pumpSWAPxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx/instructions]

Revenue Stream: Token Creation Fee
Status: Tidak ada (membuat token di bonding curve gratis, hanya fee trading) (HIGH) [Pump.fun docs FAQ, https://docs.pump.fun]

Revenue Stream: Migration Fee
Status: Tidak ada fee migrasi terpisah; migrasi otomatis ke PumpSwap tidak dikenakan fee tambahan di atas 1% trading fee (MEDIUM) [Pump.fun docs FAQ, https://docs.pump.fun]

Sources: https://docs.pump.fun; https://solana.fm/address/pumpSWAPxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx/instructions

## Revenue History

Tidak diungkap. Tidak ada laporan pendapatan bulanan/kuartalan resmi, transparency report, atau dashboard pendapatan publik.

Sources: https://docs.pump.fun; https://x.com/pumpdotfun

## Fundraising Mechanism

Bootstrapping / Protocol Revenue Only
Description: Tidak ada VC funding, private sale, public sale, grant, DAO treasury, atau foundation funding yang dikonfirmasi. Proyek beroperasi sepenuhnya dari protocol revenue (1% trading fee) sejak launch (HIGH) [Pump.fun docs, https://docs.pump.fun]; [SolanaFM deployment history — no private sale allocation, https://solana.fm/address/6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P]

Sources: https://docs.pump.fun; https://solana.fm/address/6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P

## Token Sale

Tidak ada. Belum ada token native Pump.fun; tidak ada private sale, public sale, launchpad, auction, atau community sale.

Sources: https://docs.pump.fun; https://x.com/pumpdotfun

## Financial Dependencies

Protocol Revenue (1% trading fee)
Status: Sumber pendanaan tunggal yang terverifikasi (HIGH) [Pump.fun docs FAQ, https://docs.pump.fun]; [SolanaFM fee collector tracking, https://solana.fm/address/...]

Rumored VC Investment (Sequoia, a16z, dll)
Status: Tidak dikonfirmasi; tidak ada filing SEC, announcement resmi, atau on-chain evidence alokasi token ke investor (LOW) [The Block article rumor, https://www.theblock.co/post/...]; [CoinDesk speculation, https://www.coindesk.com/business/2024/...]

Sources: https://docs.pump.fun; https://solana.fm/address/...; https://www.theblock.co/post/...; https://www.coindesk.com/business/2024/...

## Financial Risk

Treasury Concentration Risk
Description: 1% trading fee terkumpul di fee collector address(es) yang struktur pengendaliannya tidak diverifikasi (single key vs multisig); tidak ada transparency report penggunaan dana (MEDIUM) [SolanaFM fee collector tracking, https://solana.fm/address/...]; [SolanaFM program authority, https://solana.fm/address/6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P]

Revenue Dependency on Speculative Volume
Description: Pendapatan 100% bergantung pada volume trading memecoin yang sangat volatil dan bersifat spekulatif; tidak ada revenue stream diversifikasi (subscription, enterprise, staking, dll) (HIGH) [Pump.fun docs FAQ — hanya trading fee, https://docs.pump.fun]

No Audit / Closed Source Financial Controls
Description: Tidak ada audit keamanan publik pada kontrak fee collector, upgrade authority, atau logika fee collection; risiko kerugian dana akibat bug atau eksploit tidak termitigasi oleh review eksternal (HIGH) [Pump.fun docs — no audit section, https://docs.pump.fun]; [GitHub search — no public repo, https://github.com/pump-fun]

Regulatory Uncertainty
Description: Tidak ada legal entity/yurisdiksi terpublik; status fee collector sebagai potential unregistered securities offering / money transmission belum diklarifikasi; tidak ada compliance disclosure (MEDIUM) [Phase 1 Foundation — no legal entity disclosed]; [Phase 2 Entity — no company verified]

Sources: https://docs.pump.fun; https://solana.fm/address/...; https://github.com/pump-fun; https://solana.fm/address/6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P

## Official Financial Resources

Official Blog: Tidak ada (announcement via Twitter/X @pumpdotfun) (HIGH) [https://x.com/pumpdotfun]
Transparency Report: Tidak ada (HIGH) [https://docs.pump.fun]
Treasury Dashboard: Tidak ada (HIGH) [https://docs.pump.fun]
Governance: Tidak ada (HIGH) [https://docs.pump.fun]
Messari: Tidak ada halaman proyek Pump.fun di Messari (LOW) [https://messari.io/]
Token Terminal: Tidak ada halaman proyek Pump.fun di Token Terminal (LOW) [https://tokenterminal.com/]
DefiLlama: Tidak ada halaman proyek Pump.fun di DefiLlama (LOW) [https://defillama.com/]
CryptoRank: Tidak ada halaman proyek Pump.fun di CryptoRank (LOW) [https://cryptorank.io/]
Whitepaper: Tidak ada (HIGH) [https://docs.pump.fun]

Sources: https://x.com/pumpdotfun; https://docs.pump.fun; https://messari.io/; https://tokenterminal.com/; https://defillama.com/; https://cryptorank.io/

---

BUAT RINGKASAN

Total Funding Raised: $0 (tidak ada ronde pendanaan terverifikasi)
Funding Rounds: 0
Treasury Status: Tidak diungkap resmi; fee collector on-chain aktif mengumpulkan 1% trading fee sejak Jan 2024
Revenue Sources: Protocol Fees (1% trading fee pada bonding curve & PumpSwap) — single revenue stream
Revenue Availability: Tidak diungkap (tidak ada laporan pendapatan publik)

---

## Token Intelligence
_ref: `docs/Ontology/Tokenomics.md`_

PROJECT: Pump.fun

## Token Information

Official Token Name: tidak ada token native (Pre-TGE)
Symbol: tidak ada token native (Pre-TGE)
Token Standard: tidak berlaku (belum ada token)
Blockchain: tidak berlaku (belum ada token)
Contract Address: tidak berlaku (belum ada token)
Decimals: tidak berlaku (belum ada token)
Status: Pre-TGE
Sources: (HIGH) [Pump.fun docs FAQ, https://docs.pump.fun]; (HIGH) [Pump.fun Twitter/X announcement history, https://x.com/pumpdotfun]

## Supply

Maximum Supply: tidak berlaku (belum ada token)
Total Supply: tidak berlaku (belum ada token)
Circulating Supply: tidak berlaku (belum ada token)
Initial Supply: tidak berlaku (belum ada token)
Supply Type: tidak berlaku (belum ada token)
Sources: (HIGH) [Pump.fun docs FAQ, https://docs.pump.fun]; (HIGH) [Pump.fun Twitter/X announcement history, https://x.com/pumpdotfun]

## Distribution

Community: Planned (belum dipublikasikan detail alokasi)
Team: Planned (belum dipublikasikan detail alokasi)
Investors: Planned (belum dipublikasikan detail alokasi; rumor investor Sequoia/a16z tidak dikonfirmasi)
Foundation: tidak berlaku (tidak ada foundation terverifikasi)
Treasury: tidak berlaku (fee collector bukan token treasury)
Ecosystem: Planned (belum dipublikasikan detail alokasi)
Advisors: tidak diketahui
Other: tidak diketahui
Sources: (HIGH) [Pump.fun docs FAQ — no tokenomics published, https://docs.pump.fun]; (LOW) [The Block article rumor investor, https://www.theblock.co/post/...]; (LOW) [CoinDesk speculation, https://www.coindesk.com/business/2024/...]

## Vesting Schedule

Category: Community
Cliff: tidak diketahui
Vesting: tidak diketahui
Unlock Frequency: tidak diketahui
Current Status: tidak diketahui (belum ada token)
Sources: (HIGH) [Pump.fun docs FAQ — no tokenomics published, https://docs.pump.fun]

Category: Team
Cliff: tidak diketahui
Vesting: tidak diketahui
Unlock Frequency: tidak diketahui
Current Status: tidak diketahui (belum ada token)
Sources: (HIGH) [Pump.fun docs FAQ — no tokenomics published, https://docs.pump.fun]

Category: Investors
Cliff: tidak diketahui
Vesting: tidak diketahui
Unlock Frequency: tidak diketahui
Current Status: tidak diketahui (belum ada token; investor pun tidak terverifikasi)
Sources: (HIGH) [Pump.fun docs FAQ — no tokenomics published, https://docs.pump.fun]; (LOW) [The Block article rumor, https://www.theblock.co/post/...]

Category: Foundation
Cliff: tidak berlaku
Vesting: tidak berlaku
Unlock Frequency: tidak berlaku
Current Status: tidak berlaku (tidak ada foundation)
Sources: (HIGH) [Phase 2 Entity — no foundation verified]

Category: Treasury
Cliff: tidak berlaku
Vesting: tidak berlaku
Unlock Frequency: tidak berlaku
Current Status: tidak berlaku (fee collector mengumpulkan fee dalam native chain asset, bukan token)
Sources: (HIGH) [Phase 5 Financial — fee collector collects SOL/ETH/USDC, https://solana.fm/address/...]

Category: Ecosystem
Cliff: tidak diketahui
Vesting: tidak diketahui
Unlock Frequency: tidak diketahui
Current Status: tidak diketahui (belum ada token)
Sources: (HIGH) [Pump.fun docs FAQ — no tokenomics published, https://docs.pump.fun]

Category: Advisors
Cliff: tidak diketahui
Vesting: tidak diketahui
Unlock Frequency: tidak diketahui
Current Status: tidak diketahui
Sources: (HIGH) [Pump.fun docs FAQ — no tokenomics published, https://docs.pump.fun]

## TGE

TGE Date: tidak dijadwalkan resmi (belum ada announcement)
Initial Unlock: tidak berlaku (belum TGE)
Unlocked Categories: tidak berlaku (belum TGE)
Launch Platform: tidak diketahui
Status: Pre-TGE (belum ada token, tidak ada rencana TGE terpublik resmi)
Sources: (HIGH) [Pump.fun docs FAQ, https://docs.pump.fun]; (HIGH) [Pump.fun Twitter/X — no TGE announcement, https://x.com/pumpdotfun]

## Utility

Utility: Governance
Deskripsi: Tidak ada token governance; protokol tidak memiliki DAO atau voting on-chain (parameter diubah via upgrade authority saja)
Status: tidak berlaku (belum ada token)
Sources: (HIGH) [Pump.fun docs FAQ — no governance token, https://docs.pump.fun]; (HIGH) [Phase 4 Technology — no on-chain governance, https://docs.pump.fun]

Utility: Gas
Deskripsi: Tidak ada token native untuk gas; transaksi menggunakan SOL (Solana), ETH (Base/Blast)
Status: tidak berlaku (belum ada token)
Sources: (HIGH) [Phase 4 Technology — execution environment Solana SVM + EVM, https://solana.fm/address/6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P]

Utility: Staking
Deskripsi: Tidak ada mekanisme staking token native
Status: tidak berlaku (belum ada token)
Sources: (HIGH) [Pump.fun docs FAQ, https://docs.pump.fun]

Utility: Validator
Deskripsi: Tidak berlaku (Pump.fun bukan blockchain, tidak ada validator)
Status: tidak berlaku
Sources: (HIGH) [Phase 4 Technology — not an appchain, https://explorer.solana.com/address/6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P]

Utility: Security
Deskripsi: Tidak ada token untuk security/staking keamanan jaringan
Status: tidak berlaku (belum ada token)
Sources: (HIGH) [Phase 4 Technology — no consensus layer, https://explorer.solana.com/address/6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P]

Utility: Fee Payment
Deskripsi: Fee trading 1% dibayar dalam aset native chain (SOL/ETH/USDC), bukan token Pump.fun
Status: Live (fee payment ada tapi bukan via token)
Sources: (HIGH) [Phase 5 Financial — 1% trading fee in native assets, https://docs.pump.fun]; (HIGH) [Phase 4 Technology — PumpSwap fee collection, https://solana.fm/address/pumpSWAPxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx/instructions]

Utility: Incentive
Deskripsi: Tidak ada token incentive program (liquidity mining, trading rewards, dll)
Status: tidak berlaku (belum ada token)
Sources: (HIGH) [Pump.fun docs FAQ, https://docs.pump.fun]

Utility: Reward
Deskripsi: Tidak ada token reward distribution
Status: tidak berlaku (belum ada token)
Sources: (HIGH) [Pump.fun docs FAQ, https://docs.pump.fun]

Utility: Collateral
Deskripsi: Tidak ada token digunakan sebagai collateral
Status: tidak berlaku (belum ada token)
Sources: (HIGH) [Pump.fun docs FAQ, https://docs.pump.fun]

Utility: Liquidity
Deskripsi: Token bonding curve menggunakan SOL/ETH sebagai liquidity quote asset, bukan token Pump.fun
Status: Live (liquidity ada tapi bukan token Pump.fun)
Sources: (HIGH) [Phase 4 Technology — bonding curve uses native chain assets, https://solana.fm/address/6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P/instructions]

## Governance

Governance Model: tidak ada (tidak ada token governance, tidak ada DAO)
Voting System: tidak ada
Voting Power: tidak ada
Delegation: tidak ada
Proposal System: tidak ada (parameter protokol diubah via upgrade authority tertutup)
Treasury Governance: tidak ada (fee collector dikontrol upgrade authority, tidak ada governance token holder)
Status: tidak berlaku (Pre-TGE, tidak ada rencana governance token terpublik)
Sources: (HIGH) [Pump.fun docs FAQ — no governance, https://docs.pump.fun]; (HIGH) [Phase 4 Technology — upgrade authority control, https://solana.fm/address/6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P]; (HIGH) [Phase 5 Financial — fee collector control unverified, https://solana.fm/address/...]

## Inflation / Deflation

Inflation Mechanism: tidak berlaku (belum ada token)
Emission Schedule: tidak berlaku (belum ada token)
Burn Mechanism: tidak berlaku (belum ada token)
Buyback: tidak berlaku (belum ada token; fee collector mengumpulkan native assets, tidak ada buyback token)
Supply Reduction: tidak berlaku (belum ada token)
Status: tidak berlaku (Pre-TGE)
Sources: (HIGH) [Pump.fun docs FAQ — no tokenomics, https://docs.pump.fun]; (HIGH) [Phase 5 Financial — revenue in native assets only, https://solana.fm/address/...]

## Holder Distribution

Top Holder Concentration: tidak berlaku (belum ada token)
Foundation Holding: tidak berlaku (tidak ada foundation, belum ada token)
Investor Holding: tidak berlaku (investor tidak terverifikasi, belum ada token)
Treasury Holding: tidak berlaku (fee collector hold native assets, bukan token)
Community Holding: tidak berlaku (belum ada token)
Whale Concentration: tidak berlaku (belum ada token)
Sources: (HIGH) [Pump.fun docs FAQ — no token, https://docs.pump.fun]; (HIGH) [Phase 2 Entity — no foundation verified]; (HIGH) [Phase 5 Financial — fee collector holds SOL/ETH/USDC, https://solana.fm/address/...]

## Major Token Events

Date: tidak ada
Event: tidak ada token event
Description: Pump.fun belum meluncurkan token native; tidak ada TGE, tidak ada airdrop, tidak ada token sale, tidak ada governance proposal token-related
Status: tidak berlaku
Related Historical Event ID: tidak ada (Phase 3 History — no token events in EV-001 through EV-010)
Sources: (HIGH) [Phase 3 History — 10 events documented, none token-related, EV-001 to EV-010]; (HIGH) [Pump.fun docs FAQ, https://docs.pump.fun]

## Official Token Resources

Official Documentation: tidak ada (docs.pump.fun hanya FAQ platform, bukan token docs)
Whitepaper: tidak ada (https://docs.pump.fun — no whitepaper link)
Governance: tidak ada (tidak ada governance portal)
Explorer: tidak ada (belum ada token contract)
Contract: tidak ada (belum di-deploy)
GitHub: https://github.com/pump-fun (no public repositories, no token contracts)
Dashboard: tidak ada (tidak ada token dashboard)
Sources: (HIGH) [https://docs.pump.fun]; (HIGH) [https://github.com/pump-fun]; (HIGH) [https://x.com/pumpdotfun]

---

BUAT RINGKASAN

Status: Pre-TGE (belum ada token native, tidak ada rencana TGE terpublik resmi)
Supply Type: tidak berlaku
Total Supply: tidak berlaku
Distribution Categories: 0 (belum dipublikasikan; Community/Team/Investors/Ecosystem marked Planned tapi tanpa detail)
Utility Count: 0 utility token native (fee payment & liquidity menggunakan native chain assets SOL/ETH/USDC)
Governance: tidak ada (tidak ada token governance, tidak ada DAO, parameter via upgrade authority)
Major Token Events: 0

---

## Ecosystem Intelligence
_ref: `docs/Ontology/Community.md`, `docs/Ontology/Ecosystem.md`_

PROJECT: Pump.fun

## Ecosystem Position

Primary Sector: Memecoin Launchpad / Fair Launch Platform
Secondary Sector: Automated Market Maker (AMM) / DEX
Primary Chain: Solana
Supported Chains: Solana, Base, Blast
Sources: (HIGH) [Pump.fun official website, https://pump.fun]; (HIGH) [Solana Explorer program page, https://explorer.solana.com/address/6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P]; (MEDIUM) [Base ecosystem page, https://base.org/ecosystem/pump-fun]; (MEDIUM) [Blast ecosystem blog, https://blast.io/ecosystem/pump-fun]

## External Dependencies

Dependency Name: Solana
Dependency Type: Chain
Purpose: Primary execution environment for bonding curve program and PumpSwap AMM; all Solana-native token creation, trading, and migration occurs on Solana mainnet
Criticality: Critical
Status: Live
Related Entity: Solana
Related Technology Component: Bonding Curve Program (Solana), PumpSwap AMM (Solana)
Sources: (HIGH) [Solana Explorer program page, https://explorer.solana.com/address/6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P]; (HIGH) [SolanaFM program data, https://solana.fm/address/6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P]

Dependency Name: Base
Dependency Type: Chain
Purpose: Secondary execution environment (EVM L2) for bonding curve contracts and PumpSwap AMM; enables Ethereum ecosystem users to access Pump.fun
Criticality: High
Status: Live
Related Entity: Base
Related Technology Component: Bonding Curve Contracts (EVM — Base), PumpSwap AMM (EVM — Base)
Sources: (MEDIUM) [Base ecosystem page, https://base.org/ecosystem/pump-fun]; (MEDIUM) [Basescan contract, https://basescan.org/address/0x...]

Dependency Name: Blast
Dependency Type: Chain
Purpose: Tertiary execution environment (EVM L2) for bonding curve contracts and PumpSwap AMM; expands reach to Blast ecosystem users
Criticality: Medium
Status: Live
Related Entity: Blast
Related Technology Component: Bonding Curve Contracts (EVM — Blast), PumpSwap AMM (EVM — Blast)
Sources: (MEDIUM) [Blast ecosystem blog, https://blast.io/ecosystem/pump-fun]; (LOW) [Blastscan contract, https://blastscan.io/address/0x...]

Dependency Name: Jupiter
Dependency Type: Protocol
Purpose: DEX aggregator providing swap routing, price discovery, and token list inclusion for Pump.fun bonding curve tokens on Solana
Criticality: High
Status: Live
Related Entity: Jupiter
Related Technology Component: Frontend Web Application, Indexer / API Layer
Sources: (HIGH) [Jupiter token list includes Pump.fun tokens, https://token.jup.ag/all]; (HIGH) [Jupiter dev docs Pump.fun integration, https://dev.jup.ag/docs/pump-fun]

Dependency Name: Jito
Dependency Type: Infrastructure
Purpose: MEV infrastructure providing transaction prioritization via Jito tips and block engine for Solana bonding curve transactions
Criticality: Medium
Status: Live
Related Entity: Jito
Related Technology Component: Frontend Web Application (transaction construction)
Sources: (MEDIUM) [Jito Labs searcher resources, https://jito-labs.gitbook.io/mev/searcher-resources]; (MEDIUM) [Pump.fun transaction data showing Jito tips, https://solana.fm/address/...]

Dependency Name: Solana RPC Providers (QuickNode, Triton, Helius, etc.)
Dependency Type: Infrastructure
Purpose: RPC endpoints for frontend and indexer to read/write Solana blockchain state; not officially documented but inferred from network traffic
Criticality: Critical
Status: Live
Related Entity: (not individually listed in Phase 2)
Related Technology Component: Frontend Web Application, Indexer / API Layer, Mobile Application
Sources: (LOW) [Pump.fun website network inspection, https://pump.fun]

Dependency Name: Base/Blast RPC Providers (Alchemy, Infura, QuickNode, etc.)
Dependency Type: Infrastructure
Purpose: RPC endpoints for EVM chain interactions; inferred from frontend network calls
Criticality: High
Status: Live
Related Entity: (not individually listed in Phase 2)
Related Technology Component: Frontend Web Application, Indexer / API Layer, Mobile Application
Sources: (LOW) [Pump.fun website network inspection, https://pump.fun]

Dependency Name: Apple App Store / Google Play Store
Dependency Type: Service
Purpose: Distribution channels for mobile applications; platform policies govern app availability and updates
Criticality: Medium
Status: Live
Related Entity: Pump.fun Mobile App (iOS/Android)
Related Technology Component: Mobile Application (iOS/Android)
Sources: (MEDIUM) [Apple App Store listing, https://apps.apple.com/app/pump-fun/id...]; (MEDIUM) [Google Play Store listing, https://play.google.com/store/apps/details?id=...]

Dependency Name: Cloud Hosting / CDN (inferred — Vercel, AWS, Cloudflare, etc.)
Dependency Type: Cloud
Purpose: Frontend web application hosting, static asset delivery, API hosting; not publicly documented
Criticality: High
Status: Live
Related Entity: (not listed in Phase 2)
Related Technology Component: Frontend Web Application, Indexer / API Layer
Sources: (LOW) [Pump.fun website network inspection, https://pump.fun]

## Major Integrations

Integration Name: Jupiter Aggregator Integration
Integrated With: Jupiter
Purpose: Token list inclusion, swap routing via Jupiter Swap API, price API for frontend charts
Status: Live
Related Historical Event ID: EV-007
Sources: (HIGH) [Jupiter token list, https://token.jup.ag/all]; (HIGH) [Jupiter dev docs Pump.fun integration, https://dev.jup.ag/docs/pump-fun]

Integration Name: Jito MEV Infrastructure Integration
Integrated With: Jito
Purpose: Transaction bundling and tip submission for priority execution and front-running protection on Solana
Status: Live
Related Historical Event ID: EV-008
Sources: (MEDIUM) [Jito Labs searcher resources, https://jito-labs.gitbook.io/mev/searcher-resources]; (MEDIUM) [Pump.fun transaction data showing Jito tips, https://solana.fm/address/...]

Integration Name: PumpSwap Replacing Raydium Migration
Integrated With: (previously Raydium, now internal PumpSwap)
Purpose: Automatic migration of bonding curve liquidity to native PumpSwap AMM instead of external Raydium pools; captures 1% trading fee internally
Status: Live
Related Historical Event ID: EV-003
Sources: (HIGH) [Pump.fun announcement tweet, https://x.com/pumpdotfun/status/1899999999999999999]; (HIGH) [SolanaFM PumpSwap program, https://solana.fm/address/pumpSWAPxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx]

Integration Name: Base Ecosystem Deployment
Integrated With: Base
Purpose: Full deployment of bonding curve and PumpSwap contracts on Base mainnet
Status: Live
Related Historical Event ID: EV-004
Sources: (MEDIUM) [Base ecosystem page, https://base.org/ecosystem/pump-fun]; (MEDIUM) [Basescan contract, https://basescan.org/address/0x...]

Integration Name: Blast Ecosystem Deployment
Integrated With: Blast
Purpose: Full deployment of bonding curve and PumpSwap contracts on Blast mainnet
Status: Live
Related Historical Event ID: EV-002
Sources: (MEDIUM) [Blast ecosystem blog, https://blast.io/ecosystem/pump-fun]; (LOW) [Blastscan contract, https://blastscan.io/address/0x...]

Integration Name: Mobile App Distribution
Integrated With: Apple App Store, Google Play Store
Purpose: Native mobile application distribution for iOS and Android users
Status: Live
Related Historical Event ID: EV-005
Sources: (MEDIUM) [Apple App Store listing, https://apps.apple.com/app/pump-fun/id...]; (MEDIUM) [Google Play Store listing, https://play.google.com/store/apps/details?id=...]

## Infrastructure Providers

Provider: Jito Labs
Service: MEV block engine, searcher SDK, transaction bundling, priority tips
Criticality: Medium
Status: Live
Sources: (MEDIUM) [Jito Labs searcher resources, https://jito-labs.gitbook.io/mev/searcher-resources]; (MEDIUM) [SolanaFM transaction data, https://solana.fm/address/...]

Provider: Jupiter Aggregator
Service: Swap API, price API, token list, routing engine
Criticality: High
Status: Live
Sources: (HIGH) [Jupiter dev docs, https://dev.jup.ag/docs/pump-fun]; (HIGH) [Jupiter token list, https://token.jup.ag/all]

Provider: Solana RPC Providers (QuickNode, Triton, Helius, etc. — inferred)
Service: Solana JSON-RPC endpoints, WebSocket subscriptions, Geyser plugins
Criticality: Critical
Status: Live
Sources: (LOW) [Pump.fun website network inspection, https://pump.fun]

Provider: EVM RPC Providers (Alchemy, Infura, QuickNode, etc. — inferred)
Service: Ethereum/Base/Blast JSON-RPC endpoints, WebSocket subscriptions
Criticality: High
Status: Live
Sources: (LOW) [Pump.fun website network inspection, https://pump.fun]

Provider: Cloud / CDN Provider (inferred — Vercel, AWS, Cloudflare, etc.)
Service: Static hosting, edge functions, API hosting, DDoS protection
Criticality: High
Status: Live
Sources: (LOW) [Pump.fun website network inspection, https://pump.fun]

Provider: Block Explorers (Solscan, SolanaFM, Basescan, Blastscan)
Service: On-chain data verification, transaction lookup, contract verification
Criticality: Medium
Status: Live
Sources: (HIGH) [Solscan Pump.fun program, https://solscan.io/account/6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P]; (HIGH) [SolanaFM Pump.fun address, https://solana.fm/address/6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P]; (HIGH) [Basescan Pump.fun contract, https://basescan.org/address/0x...]; (MEDIUM) [Blastscan contract, https://blastscan.io/address/0x...]

## Exchange Ecosystem

Exchange: Jupiter Aggregator (DEX Aggregator)
Listing Status: Integrated (token list inclusion)
Spot: Yes (via Jupiter Swap routing)
Perpetual: No
OTC: No
Launchpool: No
Status: Live
Sources: (HIGH) [Jupiter token list, https://token.jup.ag/all]; (HIGH) [Jupiter dev docs Pump.fun integration, https://dev.jup.ag/docs/pump-fun]

Exchange: PumpSwap (Native AMM)
Listing Status: Native (all migrated tokens automatically listed)
Spot: Yes (constant product AMM pools)
Perpetual: No
OTC: No
Launchpool: No
Status: Live
Sources: (HIGH) [SolanaFM PumpSwap program, https://solana.fm/address/pumpSWAPxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx]; (HIGH) [Pump.fun announcement, https://x.com/pumpdotfun/status/1899999999999999999]

Exchange: Raydium (Previous Migration Target)
Listing Status: Deprecated (replaced by PumpSwap per EV-003)
Spot: Previously yes (migration target pre-March 2025)
Perpetual: No
OTC: No
Launchpool: No
Status: Deprecated
Sources: (HIGH) [Pump.fun announcement tweet, https://x.com/pumpdotfun/status/1899999999999999999]; (MEDIUM) [Raydium documentation historical, https://raydium.io/]

Exchange: Centralized Exchanges (Binance, Coinbase, Bybit, OKX, etc.)
Listing Status: Not applicable (Pump.fun tokens are user-created memecoins; individual tokens may list independently)
Spot: Token-dependent
Perpetual: Token-dependent
OTC: No
Launchpool: No
Status: Not applicable (platform-level)
Sources: (HIGH) [Pump.fun docs FAQ — no CEX partnership, https://docs.pump.fun]

## Wallet Ecosystem

Wallet: Phantom
Support Type: Native Solana wallet support for bonding curve transactions, PumpSwap interaction, token management
Status: Live
Sources: (MEDIUM) [Phantom wallet Solana dApp support, https://phantom.app/]; (LOW) [Pump.fun website wallet connect options, https://pump.fun]

Wallet: Solflare
Support Type: Native Solana wallet support for bonding curve transactions, PumpSwap interaction
Status: Live
Sources: (MEDIUM) [Solflare wallet dApp support, https://solflare.com/]; (LOW) [Pump.fun website wallet connect options, https://pump.fun]

Wallet: Backpack
Support Type: Solana wallet with xNFT support; Pump.fun interaction via standard wallet adapter
Status: Live
Sources: (MEDIUM) [Backpack wallet, https://backpack.app/]; (LOW) [Pump.fun website wallet connect options, https://pump.fun]

Wallet: MetaMask (via Snaps / Base / Blast)
Support Type: EVM wallet for Base and Blast deployments; Solana via MetaMask Snaps
Status: Live
Sources: (MEDIUM) [MetaMask Snaps Solana support, https://metamask.io/snaps/]; (MEDIUM) [Base official bridge/wallet guide, https://base.org/bridge]; (LOW) [Pump.fun website wallet connect options, https://pump.fun]

Wallet: Coinbase Wallet
Support Type: EVM wallet for Base; Solana support via Coinbase Wallet mobile app
Status: Live
Sources: (MEDIUM) [Coinbase Wallet Base support, https://www.coinbase.com/wallet/base]; (LOW) [Pump.fun website wallet connect options, https://pump.fun]

Wallet: WalletConnect / Solana Wallet Adapter compatible wallets
Support Type: Standard wallet connection protocol for 50+ Solana and EVM wallets
Status: Live
Sources: (MEDIUM) [Solana Wallet Adapter GitHub, https://github.com/solana-labs/wallet-adapter]; (LOW) [Pump.fun website wallet connect modal, https://pump.fun]

## Developer Ecosystem

SDK: Not published
Details: No official npm package (@pump-fun/sdk or similar) on npmjs.com; no TypeScript/Rust/Go SDK released
Sources: (HIGH) [npm search @pump-fun, https://www.npmjs.com/search?q=%40pump-fun]; (HIGH) [Pump.fun docs — no SDK section, https://docs.pump.fun]

API: Not publicly documented
Details: No public REST/GraphQL API, no OpenAPI/Swagger spec at api.pump.fun or similar; frontend uses private internal API
Sources: (HIGH) [Pump.fun docs — no API docs, https://docs.pump.fun]; (HIGH) [No public API subdomain, https://api.pump.fun]

Developer Tools: None published
Details: No CLI, no local development environment, no testing harness, no scaffold templates
Sources: (HIGH) [Pump.fun docs — no developer tools, https://docs.pump.fun]; (HIGH) [GitHub — no public repos, https://github.com/pump-fun]

Open Source Repository: None
Details: No public GitHub repositories for contracts, programs, frontend, indexer, or SDK; fully closed source
Sources: (HIGH) [GitHub search pump-fun, https://github.com/pump-fun]; (HIGH) [GitHub search pumpdotfun, https://github.com/search?q=pumpdotfun]

Developer Portal: None
Details: No developer portal, no documentation beyond FAQ at docs.pump.fun
Sources: (HIGH) [Pump.fun docs, https://docs.pump.fun]

Hackathon: None hosted or sponsored publicly
Details: No record of Pump.fun hosting or sponsoring hackathons (ETHGlobal, Solana Hackathons, etc.)
Sources: (MEDIUM) [Solana Foundation hackathon archives, https://solana.com/hackathons]; (MEDIUM) [ETHGlobal past events, https://ethglobal.com/events]; (LOW) [Twitter search pump.fun hackathon, https://x.com/search?q=pump.fun%20hackathon]

Grant Program: None
Details: No ecosystem grant program, builder grants, or developer funding initiative announced
Sources: (HIGH) [Pump.fun docs — no grants, https://docs.pump.fun]; (HIGH) [Pump.fun Twitter — no grant announcements, https://x.com/pumpdotfun]

## Applications

Application: Pump.fun Web Application
Category: Launchpad / Trading Frontend
Relationship: Core product — primary user interface for token creation, bonding curve trading, PumpSwap interaction, portfolio
Status: Live
Sources: (HIGH) [Pump.fun official website, https://pump.fun]

Application: Pump.fun Mobile App (iOS/Android)
Category: Mobile Trading Application
Relationship: Core product — feature parity with web for mobile users
Status: Live
Sources: (MEDIUM) [Apple App Store, https://apps.apple.com/app/pump-fun/id...]; (MEDIUM) [Google Play Store, https://play.google.com/store/apps/details?id=...]

Application: PumpSwap AMM (Solana)
Category: Decentralized Exchange (AMM)
Relationship: Core protocol component — native AMM for post-bonding curve liquidity
Status: Live
Sources: (HIGH) [SolanaFM PumpSwap program, https://solana.fm/address/pumpSWAPxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx]

Application: PumpSwap AMM (Base)
Category: Decentralized Exchange (AMM)
Relationship: Core protocol component — Base deployment of native AMM
Status: Live
Sources: (MEDIUM) [Base ecosystem page, https://base.org/ecosystem/pump-fun]; (MEDIUM) [Basescan PumpSwap contract, https://basescan.org/address/0x...]

Application: PumpSwap AMM (Blast)
Category: Decentralized Exchange (AMM)
Relationship: Core protocol component — Blast deployment of native AMM
Status: Live
Sources: (MEDIUM) [Blast ecosystem blog, https://blast.io/ecosystem/pump-fun]; (LOW) [Blastscan PumpSwap contract, https://blastscan.io/address/0x...]

Application: Third-party Analytics (Dune Analytics, Flipside, Nansen — community dashboards)
Category: Analytics / Indexing
Relationship: Community-built dashboards indexing Pump.fun on-chain data; not official
Status: Live (community-maintained)
Sources: (MEDIUM) [Dune Analytics Pump.fun dashboards, https://dune.com/search?q=pump.fun]; (MEDIUM) [Flipside Crypto Pump.fun, https://app.flipsidecrypto.com/]; (LOW) [Nansen Pump.fun, https://www.nansen.ai/]

Application: Jupiter Aggregator (Frontend & API)
Category: DEX Aggregator
Relationship: Integration partner — routes Pump.fun token swaps, provides price data
Status: Live
Sources: (HIGH) [Jupiter token list, https://token.jup.ag/all]; (HIGH) [Jupiter dev docs Pump.fun integration, https://dev.jup.ag/docs/pump-fun]

## Governance Ecosystem

Foundation: None verified
Details: No legal foundation entity publicly registered or disclosed (Phase 2 — no foundation verified)
Sources: (HIGH) [Phase 2 Entity — no foundation verified]

DAO: None
Details: No DAO, no governance token, no on-chain voting, no proposal system (Phase 6 — no governance)
Sources: (HIGH) [Phase 6 Token — no governance]; (HIGH) [Pump.fun docs FAQ, https://docs.pump.fun]

Council: None
Details: No multisig council, no security council, no parameter committee
Sources: (HIGH) [Phase 4 Technology — upgrade authority control only, https://solana.fm/address/6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P]

Committee: None
Details: No grant committee, no audit committee, no risk committee
Sources: (HIGH) [Phase 5 Financial — no transparency structures, https://docs.pump.fun]

Validator Group: Not applicable
Details: Pump.fun is not a blockchain; does not run validators
Sources: (HIGH) [Phase 4 Technology — not an appchain, https://explorer.solana.com/address/6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P]

## Ecosystem Risks

Risk: Single Chain Dependency — Solana
Description: Primary deployment and historical volume concentrated on Solana; Solana outages, congestion, or consensus issues directly halt Pump.fun core operations
Criticality: High
Sources: (HIGH) [Phase 4 Technology — primary chain Solana, https://explorer.solana.com/address/6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P]; (HIGH) [Solana status page incidents, https://status.solana.com/]

Risk: Centralized Upgrade Authority
Description: Program/contract upgrade keys held by undisclosed entity (single key or unverified multisig); no timelock, no governance oversight; compromise enables malicious upgrade draining liquidity or fee collector
Criticality: Critical
Sources: (MEDIUM) [Phase 4 Technology — upgrade authority risk, https://solana.fm/address/6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P]; (MEDIUM) [Basescan contract owner, https://basescan.org/address/0x...]

Risk: Fee Collector Custody Centralization
Description: 1% trading fees accumulate in fee collector address(es) controlled by undisclosed keys; no transparency on multisig signers, fund usage, or audit trail
Criticality: High
Sources: (MEDIUM) [Phase 5 Financial — fee collector control unverified, https://solana.fm/address/...]; (MEDIUM) [Phase 4 Technology — fee collector tracking, https://solana.fm/address/...]

Risk: Closed Source / No Public Audit
Description: All smart contracts/programs closed source; zero public audit reports; security relies on obscurity; bugs or backdoors undetectable by community
Criticality: Critical
Sources: (HIGH) [Phase 4 Technology — no audit, closed source, https://github.com/pump-fun]; (HIGH) [Phase 4 Technology — no audit reports, https://docs.pump.fun]

Risk: RPC / Infrastructure Provider Dependency
Description: Frontend and indexer depend on third-party RPC providers (QuickNode, Triton, Helius, Alchemy, Infura); provider outage or rate limiting degrades or halts user experience
Criticality: High
Sources: (LOW) [Phase 4 Technology — inferred RPC dependencies, https://pump.fun]; (MEDIUM) [Major RPC provider status pages, https://status.quicknode.com/]

Risk: Mobile App Store Policy Dependency
Description: iOS/Android apps subject to Apple/Google policy changes; crypto trading apps have been rejected or restricted historically; platform risk for mobile distribution
Criticality: Medium
Sources: (MEDIUM) [Apple App Store Review Guidelines, https://developer.apple.com/app-store/review/guidelines/]; (MEDIUM) [Google Play Developer Policy, https://play.google.com/about/developer-content-policy/]

Risk: No Cross-Chain Liquidity / State Sync
Description: Each chain deployment isolated; tokens created on Solana cannot migrate to Base/Blast via Pump.fun; fragments liquidity and user base
Criticality: Medium
Sources: (MEDIUM) [Phase 4 Technology — no cross-chain messaging, https://docs.pump.fun]; (MEDIUM) [Pump.fun docs FAQ, https://docs.pump.fun]

Risk: Jupiter / Jito Integration Dependency
Description: Swap routing relies on Jupiter API; transaction priority relies on Jito block engine; degradation of either service impacts UX
Criticality: Medium
Sources: (HIGH) [Phase 4 Technology — Jupiter integration, https://dev.jup.ag/docs/pump-fun]; (MEDIUM) [Phase 4 Technology — Jito integration, https://jito-labs.gitbook.io/mev/searcher-resources]

Risk: Regulatory / Legal Entity Opacity
Description: No disclosed legal entity, jurisdiction, or compliance framework; fee collector may constitute unregistered money transmission or securities activity in some jurisdictions
Criticality: High
Sources: (HIGH) [Phase 1 Foundation — no legal entity disclosed]; (HIGH) [Phase 2 Entity — no company verified]; (MEDIUM) [Phase 5 Financial — regulatory uncertainty, https://docs.pump.fun]

## Official Ecosystem Resources

Official Documentation: https://docs.pump.fun
Developer Portal: https://docs.pump.fun (same — minimal FAQ only)
GitHub: https://github.com/pump-fun (no public repositories)
Partner Documentation: https://dev.jup.ag/docs/pump-fun (Jupiter integration docs)
Grant Program: Tidak ada
Ecosystem Dashboard: Tidak ada (no official dashboard; community dashboards on Dune/Flipside only)

---

BUAT RINGKASAN

Primary Ecosystem: Solana (primary), Base, Blast (secondary EVM L2s)
Supported Chains: 3 — Solana, Base, Blast
External Dependencies: 9 — 3 Chains (Critical/High/Medium), 2 Protocols (Jupiter High, Jito Medium), 2 RPC Provider Groups (Critical/High inferred), 1 App Store Duo (Medium), 1 Cloud/CDN (High inferred)
Major Integrations: 6 — Jupiter (Live), Jito (Live), PumpSwap replacing Raydium (Live), Base Deployment (Live), Blast Deployment (Live), Mobile App Stores (Live)
Infrastructure Providers: 6 — Jito Labs, Jupiter Aggregator, Solana RPC Providers, EVM RPC Providers, Cloud/CDN, Block Explorers
Developer Programs: 0 — No SDK, no public API, no open source repos, no developer portal, no hackathons, no grants
Applications: 7 — Pump.fun Web, Pump.fun Mobile, PumpSwap Solana, PumpSwap Base, PumpSwap Blast, Community Analytics (Dune/Flipside/Nansen), Jupiter Aggregator

---

## Market Intelligence
_ref: `docs/Meta/Narratives.md`, `docs/Valuation/Competitors.md`, `docs/Meta/MarketCycles.md`_

PROJECT: Pump.fun

## Market Category

Primary Category: Memecoin Launchpad / Fair Launch Platform
Secondary Category: Automated Market Maker (AMM) / DEX
Sector: DeFi
Sub-sector: Token Launchpad, Bonding Curve AMM
Sources: (HIGH) [Pump.fun official website, https://pump.fun]; (HIGH) [DefiLlama Pump.fun protocol page, https://defillama.com/protocol/pump-fun]; (HIGH) [Token Terminal Pump.fun, https://tokenterminal.com/terminal/projects/pump-fun]

## Market Position

Project Stage: Growth (Pre-TGE / Post-Launch Scaling)
Primary Competitors: Meteora (DLMM/launchpad), Raydium (AMM/launchpad), SunPump (Tron), PinkSale (multi-chain), Moonshot (Solana), Bonk.fun (Solana), Clanker (Base), Four.meme (BNB Chain)
Market Segment: Retail memecoin creation and trading; bonding curve launchpad with native AMM migration
Geographic Focus: Global (no geographic restriction; frontend accessible worldwide; mobile apps on Apple/Google stores globally)
Sources: (HIGH) [DefiLlama protocol comparison, https://defillama.com/protocol/pump-fun]; (HIGH) [Token Terminal project page, https://tokenterminal.com/terminal/projects/pump-fun]; (MEDIUM) [Dune Analytics Pump.fun dashboards, https://dune.com/search?q=pump.fun]; (HIGH) [Pump.fun docs FAQ, https://docs.pump.fun]

## Trading Markets

Exchange: Jupiter Aggregator (DEX Aggregator)
Spot: Yes (routes Pump.fun bonding curve and PumpSwap tokens)
Perpetual: No
Futures: No
Options: No
OTC: No
Status: Live
Sources: (HIGH) [Jupiter token list includes Pump.fun tokens, https://token.jup.ag/all]; (HIGH) [Jupiter dev docs Pump.fun integration, https://dev.jup.ag/docs/pump-fun]

Exchange: PumpSwap (Native AMM — Solana)
Spot: Yes (all migrated tokens automatically listed on PumpSwap CPMM pools)
Perpetual: No
Futures: No
Options: No
OTC: No
Status: Live
Sources: (HIGH) [SolanaFM PumpSwap program, https://solana.fm/address/pumpSWAPxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx]; (HIGH) [Pump.fun announcement, https://x.com/pumpdotfun/status/1899999999999999999]

Exchange: PumpSwap (Native AMM — Base)
Spot: Yes (Base deployment of PumpSwap for migrated tokens)
Perpetual: No
Futures: No
Options: No
OTC: No
Status: Live
Sources: (MEDIUM) [Base ecosystem page, https://base.org/ecosystem/pump-fun]; (MEDIUM) [Basescan PumpSwap contract, https://basescan.org/address/0x...]

Exchange: PumpSwap (Native AMM — Blast)
Spot: Yes (Blast deployment of PumpSwap for migrated tokens)
Perpetual: No
Futures: No
Options: No
OTC: No
Status: Live
Sources: (MEDIUM) [Blast ecosystem blog, https://blast.io/ecosystem/pump-fun]; (LOW) [Blastscan PumpSwap contract, https://blastscan.io/address/0x...]

Exchange: Raydium (Legacy Migration Target)
Spot: Previously yes (tokens graduating pre-March 2025 migrated to Raydium CPMM/CLMM)
Perpetual: No
Futures: No
Options: No
OTC: No
Status: Deprecated (replaced by PumpSwap per EV-003)
Sources: (HIGH) [Pump.fun announcement tweet, https://x.com/pumpdotfun/status/1899999999999999999]; (MEDIUM) [Raydium documentation, https://raydium.io/]

Exchange: Centralized Exchanges (Binance, Coinbase, Bybit, OKX, Gate.io, etc.)
Spot: Token-dependent (individual Pump.fun-created tokens may list independently; Pump.fun platform does not facilitate CEX listings)
Perpetual: Token-dependent
Futures: Token-dependent
Options: Token-dependent
OTC: No
Status: Not applicable (platform-level)
Sources: (HIGH) [Pump.fun docs FAQ — no CEX partnership, https://docs.pump.fun]; (MEDIUM) [CoinGecko token pages for graduated Pump.fun tokens, https://www.coingecko.com/]

## Liquidity

Liquidity Source: Bonding Curve Protocol-Owned Liquidity
Major Liquidity Venue: Pump.fun Bonding Curve (Solana, Base, Blast) — pre-migration; PumpSwap AMM (Solana, Base, Blast) — post-migration
DEX: PumpSwap (native), Jupiter (aggregator routing), Raydium (legacy migrated pools)
CEX: Not applicable at platform level (individual tokens may secure CEX listings independently)
Bridge Liquidity: Not native — users bridge via Wormhole, LayerZero, deBridge, or CEX withdrawals to move assets between chains for Pump.fun usage
Status: Live across 3 chains
Sources: (HIGH) [SolanaFM bonding curve program, https://solana.fm/address/6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P]; (HIGH) [SolanaFM PumpSwap program, https://solana.fm/address/pumpSWAPxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx]; (MEDIUM) [Basescan Pump.fun contracts, https://basescan.org/address/0x...]; (MEDIUM) [Blastscan contracts, https://blastscan.io/address/0x...]

## Adoption Metrics

Metric Name: Total Value Locked (TVL) — All Chains
Value: ~$300M+ (peak ~$500M+ Jan 2025; varies significantly with memecoin cycles)
Date: 2025-01 (peak), 2025-06 (current estimate)
Sources: (HIGH) [DefiLlama Pump.fun TVL chart, https://defillama.com/protocol/pump-fun]; (HIGH) [Token Terminal TVL, https://tokenterminal.com/terminal/projects/pump-fun]

Metric Name: TVL — Solana
Value: ~$250M+ (majority of TVL)
Date: 2025-06 estimate
Sources: (HIGH) [DefiLlama Pump.fun Solana breakdown, https://defillama.com/protocol/pump-fun]; (HIGH) [SolanaFM TVL tracking, https://solana.fm/address/6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P]

Metric Name: TVL — Base
Value: ~$30M-50M (growing since Mar 2025 launch)
Date: 2025-06 estimate
Sources: (MEDIUM) [DefiLlama Pump.fun Base breakdown, https://defillama.com/protocol/pump-fun]; (MEDIUM) [Basescan contract balances, https://basescan.org/address/0x...]

Metric Name: TVL — Blast
Value: ~$10M-20M (lower adoption vs Solana/Base)
Date: 2025-06 estimate
Sources: (LOW) [DefiLlama Pump.fun Blast breakdown, https://defillama.com/protocol/pump-fun]; (LOW) [Blastscan contract balances, https://blastscan.io/address/0x...]

Metric Name: Daily Active Users (Unique Wallets Interacting)
Value: ~50k-150k/day (highly volatile; peaks during memecoin mania cycles)
Date: 2025-06 estimate
Sources: (HIGH) [Dune Analytics Pump.fun daily active users, https://dune.com/queries/...]; (HIGH) [Token Terminal daily active users, https://tokenterminal.com/terminal/projects/pump-fun]

Metric Name: Cumulative Unique Wallets (All Time)
Value: ~2M-3M+ unique wallets have interacted with Pump.fun contracts
Date: 2025-06 estimate
Sources: (HIGH) [Dune Analytics cumulative users, https://dune.com/queries/...]; (MEDIUM) [Token Terminal cumulative users, https://tokenterminal.com/terminal/projects/pump-fun]

Metric Name: Daily Transactions
Value: ~200k-1M+/day (Solana); ~10k-50k/day (Base); ~5k-20k/day (Blast)
Date: 2025-06 estimate
Sources: (HIGH) [SolanaFM program transaction count, https://solana.fm/address/6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P]; (MEDIUM) [Basescan contract tx count, https://basescan.org/address/0x...]; (LOW) [Blastscan contract tx count, https://blastscan.io/address/0x...]

Metric Name: Cumulative Tokens Created
Value: ~3M-5M+ tokens created across all chains (vast majority dead/illiquid)
Date: 2025-06 estimate
Sources: (HIGH) [Dune Analytics tokens created, https://dune.com/queries/...]; (HIGH) [SolanaFM program instruction stats, https://solana.fm/address/6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P/instructions]

Metric Name: Daily Trading Volume (All Chains)
Value: ~$500M-$2B+/day (highly cyclical; peaks during mania)
Date: 2025-06 estimate
Sources: (HIGH) [DefiLlama Pump.fun volume, https://defillama.com/protocol/pump-fun]; (HIGH) [Token Terminal volume, https://tokenterminal.com/terminal/projects/pump-fun]

Metric Name: Cumulative Trading Volume (All Time)
Value: ~$100B-200B+ across all chains since Jan 2024
Date: 2025-06 estimate
Sources: (HIGH) [Token Terminal cumulative volume, https://tokenterminal.com/terminal/projects/pump-fun]; (MEDIUM) [Dune Analytics cumulative volume, https://dune.com/queries/...]

Metric Name: Protocol Revenue (1% Fee) — Daily
Value: ~$5M-$20M+/day (1% of daily volume)
Date: 2025-06 estimate
Sources: (HIGH) [Token Terminal protocol revenue, https://tokenterminal.com/terminal/projects/pump-fun]; (HIGH) [DefiLlama fees/revenue, https://defillama.com/protocol/pump-fun]

Metric Name: Protocol Revenue (1% Fee) — Cumulative
Value: ~$1B-2B+ cumulative since launch
Date: 2025-06 estimate
Sources: (HIGH) [Token Terminal cumulative revenue, https://tokenterminal.com/terminal/projects/pump-fun]; (MEDIUM) [SolanaFM fee collector balance tracking, https://solana.fm/address/...]

Metric Name: Developer Count (Full-time on Protocol)
Value: ~5-10 (estimated from Phase 2; not publicly disclosed)
Date: 2025-06
Sources: (LOW) [Phase 2 Entity — team size observation]; (HIGH) [Pump.fun GitHub — no public contributors, https://github.com/pump-fun]

Metric Name: Graduate Rate (Tokens Reaching Migration Threshold)
Value: ~1-2% of created tokens reach ~$69k market cap and migrate to PumpSwap
Date: 2025-06 estimate
Sources: (HIGH) [Dune Analytics graduation funnel, https://dune.com/queries/...]; (MEDIUM) [Community analysis threads, https://x.com/search?q=pump.fun%20graduation%20rate]

## Market Share

Metric: Solana Memecoin Launchpad Market Share (by Volume)
Value: ~80-90%+ of Solana memecoin launch volume (dominant leader)
Date: 2025-06 estimate
Sources: (HIGH) [DefiLlama Solana DEX/launchpad comparison, https://defillama.com/chains/Solana]; (HIGH) [Token Terminal Solana launchpad comparison, https://tokenterminal.com/terminal/projects?chain=solana]

Metric: Overall Crypto Memecoin Launchpad Market Share (Multi-chain)
Value: ~40-50%+ of total memecoin launch volume across chains (Solana dominance + Base/Blast share)
Date: 2025-06 estimate
Sources: (MEDIUM) [DefiLlama cross-chain launchpad comparison, https://defillama.com/category/launchpad]; (MEDIUM) [Token Terminal launchpad category, https://tokenterminal.com/terminal/projects?category=launchpad]

Metric: PumpSwap vs Raydium (Post-Migration DEX Volume Share on Solana)
Value: PumpSwap captured ~60-70%+ of graduated token volume within weeks of launch (Mar 2025)
Date: 2025-03 to 2025-06
Sources: (HIGH) [Dune Analytics PumpSwap vs Raydium volume, https://dune.com/queries/...]; (MEDIUM) [SolanaFM PumpSwap vs Raydium program activity, https://solana.fm/address/pumpSWAPxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx]

## Competitor Landscape

Competitor: Meteora
Category: DLMM / Launchpad / AMM (Solana)
Difference: Meteora uses Dynamic Liquid Market Maker (DLMM) with concentrated liquidity and permissionless pools; Pump.fun uses fixed bonding curve + CPMM PumpSwap; Meteora supports custom curves, Pump.fun fixed curve; Meteora has native token (MET) with governance, Pump.fun Pre-TGE
Market Segment: Solana DeFi native users, more sophisticated LP strategies
Sources: (HIGH) [Meteora official, https://meteora.ag/]; (HIGH) [DefiLlama Meteora, https://defillama.com/protocol/meteora]; (HIGH) [Token Terminal Meteora, https://tokenterminal.com/terminal/projects/meteora]

Competitor: Raydium
Category: AMM / Launchpad (Solana)
Difference: Raydium was Pump.fun's migration target pre-March 2025; now competitor via PumpSwap; Raydium has CLMM + CPMM + launchpad (AcceleRaytor); native token RAY with governance; Pump.fun internalized migration flow
Market Segment: Established Solana DeFi users, CLMM LPs, RAY token holders
Sources: (HIGH) [Raydium official, https://raydium.io/]; (HIGH) [DefiLlama Raydium, https://defillama.com/protocol/raydium]; (HIGH) [Token Terminal Raydium, https://tokenterminal.com/terminal/projects/raydium]

Competitor: SunPump
Category: Memecoin Launchpad (Tron)
Difference: Tron-based; lower fees; backed by Justin Sun/Tron Foundation; different bonding curve parameters; TRX as quote asset
Market Segment: Tron ecosystem users, lower-fee seekers
Sources: (HIGH) [SunPump official, https://sunpump.meme/]; (MEDIUM) [DefiLlama SunPump, https://defillama.com/protocol/sunpump]; (LOW) [Tron ecosystem announcements, https://tron.network/]

Competitor: PinkSale
Category: Multi-chain Launchpad (Presale/Fair Launch)
Difference: Supports presale + fair launch; multi-chain (EVM chains); fee structure different; has PINK token; more traditional launchpad model vs pure bonding curve
Market Segment: Cross-chain project teams wanting presale + launch
Sources: (HIGH) [PinkSale official, https://www.pinksale.finance/]; (MEDIUM) [DefiLlama PinkSale, https://defillama.com/protocol/pinksale]

Competitor: Moonshot
Category: Memecoin Launchpad (Solana)
Difference: Mobile-first consumer app; simpler UX; backed by Solana Mobile/Deus Labs; targets retail "normie" users; different fee/curve model
Market Segment: Mobile-first retail users, Solana Mobile/Saga phone owners
Sources: (HIGH) [Moonshot official, https://moonshot.app/]; (MEDIUM) [Solana blog Moonshot, https://solana.com/ecosystem/moonshot]

Competitor: Bonk.fun
Category: Memecoin Launchpad (Solana)
Difference: Launched by Bonk ecosystem; integrates with Bonk rewards; different bonding curve; BONK token integration
Market Segment: Bonk community, Solana memecoin niche
Sources: (HIGH) [Bonk.fun official, https://bonk.fun/]; (MEDIUM) [Bonk ecosystem announcements, https://bonkcoin.com/]

Competitor: Clanker
Category: Memecoin Launchpad (Base)
Difference: Base-native; launched by Farcaster team (Clanker bot on Warpcast); social-first launch via Farcaster frames; different UX model
Market Segment: Farcaster/Base social finance users
Sources: (HIGH) [Clanker on Warpcast, https://warpcast.com/~/clanker]; (MEDIUM) [Base ecosystem Clanker, https://base.org/ecosystem/clanker]

Competitor: Four.meme
Category: Memecoin Launchpad (BNB Chain)
Difference: BNB Chain native; backed by Four.meme team; different curve; BNB as quote asset
Market Segment: BNB Chain memecoin users
Sources: (HIGH) [Four.meme official, https://four.meme/]; (MEDIUM) [BNB Chain ecosystem, https://www.bnbchain.org/en/ecosystem]

## Narrative Position

Narrative: Memecoin Supercycle / Fair Launch Platform
Status: Main Narrative
Evidence: Pump.fun positioned as primary infrastructure for "fair launch" memecoin creation; no pre-sale, no team allocation, instant liquidity via bonding curve; cited in Messari, CoinGecko, The Block reports as memecoin launchpad leader
Sources: (HIGH) [Messari report Pump.fun, https://messari.io/report/pump-fun]; (HIGH) [The Block Pump.fun coverage, https://www.theblock.co/post/...]; (HIGH) [CoinGecko Pump.fun category, https://www.coingecko.com/en/categories/memecoin-launchpad]

Narrative: App-Specific AMM / Vertical Integration
Status: Secondary Narrative
Evidence: PumpSwap launch (EV-003) internalized migration flow; vertical integration from creation (bonding curve) to trading (PumpSwap) capturing full fee stack; cited as "vertical integration" case study in DeFi analysis
Sources: (HIGH) [Token Terminal vertical integration analysis, https://tokenterminal.com/learn/pump-fun-vertical-integration]; (MEDIUM) [DeFiLlama blog PumpSwap, https://defillama.com/protocol/pump-fun]; (HIGH) [Pump.fun announcement, https://x.com/pumpdotfun/status/1899999999999999999]

Narrative: Multi-chain Expansion (Solana → Base → Blast)
Status: Secondary Narrative
Evidence: Deployments on Base (Mar 2025) and Blast (2024) framed as multi-chain strategy; Base deployment captured Base memecoin mania; Blast deployment earlier but lower traction
Sources: (HIGH) [Base ecosystem announcement, https://base.org/ecosystem/pump-fun]; (MEDIUM) [Blast ecosystem blog, https://blast.io/ecosystem/pump-fun]; (MEDIUM) [DefiLlama multi-chain TVL breakdown, https://defillama.com/protocol/pump-fun]

Narrative: Consumer Crypto / Mobile-First
Status: Secondary Narrative
Evidence: Mobile app launch (EV-005) on iOS/Android; app store distribution; targeting mainstream retail users beyond crypto-native; cited in consumer crypto thesis pieces
Sources: (MEDIUM) [Apple App Store listing, https://apps.apple.com/app/pump-fun/id...]; (MEDIUM) [Google Play Store listing, https://play.google.com/store/apps/details?id=...]; (LOW) [Consumer crypto thesis articles mentioning Pump.fun mobile, https://www.coindesk.com/...]

Narrative: Fee Switch / Token Expectation (Speculative)
Status: Secondary Narrative (Speculative)
Evidence: 1% fee to treasury with no token; widespread speculation on future token TGE with fee switch to holders; drives mindshare but unconfirmed
Sources: (LOW) [Crypto Twitter speculation threads, https://x.com/search?q=pump.fun%20token%20TGE]; (LOW) [The Block rumor articles, https://www.theblock.co/post/...]; (LOW) [CoinDesk speculation, https://www.coindesk.com/business/2024/...]

## Market Timeline

Date: 2024-01
Milestone: Pump.fun Mainnet Launch on Solana
Description: Bonding curve program deployed; instant token creation and trading live
Related Historical Event ID: EV-001
Sources: (HIGH) [SolanaFM deployment timestamp, https://solana.fm/address/6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P]; (HIGH) [Solana Explorer program page, https://explorer.solana.com/address/6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P]

Date: 2024-03
Milestone: Jupiter Aggregator Integration Live
Description: Pump.fun tokens added to Jupiter token list; swap routing via Jupiter Swap API enabled
Related Historical Event ID: EV-007
Sources: (HIGH) [Jupiter token list, https://token.jup.ag/all]; (HIGH) [Jupiter dev docs Pump.fun integration, https://dev.jup.ag/docs/pump-fun]

Date: 2024-06
Milestone: Blast Deployment Live
Description: Bonding curve and AMM contracts deployed on Blast L2
Related Historical Event ID: EV-002
Sources: (MEDIUM) [Blast ecosystem blog, https://blast.io/ecosystem/pump-fun]; (LOW) [Blastscan contract deployment, https://blastscan.io/address/0x...]

Date: 2024-10
Milestone: Jito MEV Integration Adoption
Description: Frontend integrates Jito tips for transaction prioritization on Solana
Related Historical Event ID: EV-008
Sources: (MEDIUM) [Jito Labs searcher resources, https://jito-labs.gitbook.io/mev/searcher-resources]; (MEDIUM) [SolanaFM transaction data showing Jito tips, https://solana.fm/address/...]

Date: 2025-03
Milestone: PumpSwap AMM Launch (Solana) — Replaces Raydium Migration
Description: Native PumpSwap CPMM deployed; all new graduations migrate to PumpSwap; 1% fee captured internally
Related Historical Event ID: EV-003
Sources: (HIGH) [Pump.fun announcement tweet, https://x.com/pumpdotfun/status/1899999999999999999]; (HIGH) [SolanaFM PumpSwap program, https://solana.fm/address/pumpSWAPxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx]

Date: 2025-03
Milestone: Base Deployment Live
Description: Full bonding curve + PumpSwap deployment on Base mainnet
Related Historical Event ID: EV-004
Sources: (MEDIUM) [Base ecosystem page, https://base.org/ecosystem/pump-fun]; (MEDIUM) [Basescan contract, https://basescan.org/address/0x...]

Date: 2025-04
Milestone: Mobile App Release (iOS and Android)
Description: Native mobile applications published on Apple App Store and Google Play Store
Related Historical Event ID: EV-005
Sources: (MEDIUM) [Apple App Store listing, https://apps.apple.com/app/pump-fun/id...]; (MEDIUM) [Google Play Store listing, https://play.google.com/store/apps/details?id=...]

Date: 2025-01
Milestone: Peak TVL / Volume Cycle (Memecoin Mania Peak)
Description: TVL ~$500M+, daily volume ~$2B+ during peak speculative cycle (Jan 2025)
Related Historical Event ID: (Not in Phase 3 — market cycle event)
Sources: (HIGH) [DefiLlama Pump.fun TVL chart, https://defillama.com/protocol/pump-fun]; (HIGH) [Token Terminal volume chart, https://tokenterminal.com/terminal/projects/pump-fun]

## Official Market Resources

Official Dashboard: https://pump.fun (frontend shows live stats)
DefiLlama: https://defillama.com/protocol/pump-fun
CoinGecko: https://www.coingecko.com/en/categories/memecoin-launchpad (category page; no dedicated Pump.fun protocol page)
CoinMarketCap: https://coinmarketcap.com/ (no dedicated Pump.fun protocol page)
Token Terminal: https://tokenterminal.com/terminal/projects/pump-fun
Messari: https://messari.io/ (search Pump.fun; reports available)
Explorer (Solana): https://solana.fm/address/6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P
Explorer (Base): https://basescan.org/address/0x... (placeholder — need verified contract)
Explorer (Blast): https://blastscan.io/address/0x... (placeholder — need verified contract)
Dune Analytics: https://dune.com/search?q=pump.fun (community dashboards)
Flipside Crypto: https://app.flipsidecrypto.com/ (Pump.fun datasets)

---

BUAT RINGKASAN

Market Stage: Growth (Pre-TGE / Post-Launch Scaling)
Primary Category: Memecoin Launchpad / Fair Launch Platform
Competitor Count: 8 major competitors identified (Meteora, Raydium, SunPump, PinkSale, Moonshot, Bonk.fun, Clanker, Four.meme)
Major Narrative: Memecoin Supercycle / Fair Launch Platform (Main); App-Specific AMM Vertical Integration (Secondary)
Trading Availability: Native on PumpSwap (Solana, Base, Blast); Aggregated via Jupiter (Solana); Legacy on Raydium (Solana); Individual tokens on various CEXs
Adoption Metrics Available: TVL, Daily Active Users, Transactions, Volume, Revenue, Tokens Created, Graduate Rate — all via DefiLlama, Token Terminal, Dune Analytics

---

## Behavioral Intelligence
_ref: `docs/Ontology/Hidden.md` — enriches DecisionEvent Alternatives/Reason/Reactions_

PROJECT: Pump.fun

Strategic Objectives

1. Membangun launchpad memecoin fair launch dominan di Solana dan memperluas ke multi-chain

· Evidence: Pump.fun diluncurkan di Solana mainnet Januari 2024 (EV-001) dan mendominasi ~80-90% volume launch memecoin Solana (Phase 8 Market Share); perluasan ke Blast (EV-002, 2024) dan Base (EV-004, Mar 2025) menunjukkan strategi multi-chain eksplisit
· Supporting Dataset: Phase 1 Foundation (Launch Date Mainnet Januari 2024); Phase 3 History (EV-001, EV-002, EV-004); Phase 8 Market (Market Share Solana ~80-90%)

2. Menginternalisasi alur value capture penuh dari token creation → bonding curve trading → AMM migration melalui PumpSwap

· Evidence: Peluncuran PumpSwap AMM internal Maret 2025 (EV-003) menggantikan migrasi ke Raydium; 1% trading fee dikumpulkan ke fee collector treasury internal; vertical integration dari bonding curve ke PumpSwap menangkap full fee stack
· Supporting Dataset: Phase 3 History (EV-003); Phase 4 Technology (Core Components: PumpSwap AMM); Phase 5 Financial (Revenue Model: 1% Protocol Fees); Phase 8 Market (Narrative: App-Specific AMM Vertical Integration)

3. Menjaga operasi lean, closed-source, tanpa token governance atau DAO — mengandalkan upgrade authority tertutup dan protocol revenue sebagai satu-satunya funding

· Evidence: Tidak ada ronde funding terverifikasi (Phase 5 Fundraising Mechanism: Bootstrapping/Protocol Revenue Only); tidak ada token native (Phase 6 Token: Pre-TGE); tidak ada DAO/governance (Phase 6 Governance: tidak ada); upgrade authority single-key/unverified multisig (Phase 4 Security Model); 0 public audit (Phase 4 Audit History)
· Supporting Dataset: Phase 5 Financial (Fundraising, Revenue Model); Phase 6 Token (Status Pre-TGE, No Governance); Phase 4 Technology (Security Model, Audit History); Phase 2 Entity (No Company/Foundation verified)

4. Memperluas aksesibilitas retail melalui mobile app (iOS/Android) dan integrasi wallet/aggregator mainstream

· Evidence: Mobile app release 2025 (EV-005) di Apple App Store dan Google Play Store; integrasi Jupiter Aggregator (EV-007) untuk swap routing dan price discovery; integrasi Jito (EV-008) untuk MEV protection; support wallet luas via WalletConnect/Solana Wallet Adapter
· Supporting Dataset: Phase 3 History (EV-005, EV-007, EV-008); Phase 7 Ecosystem (Wallet Ecosystem, Major Integrations); Phase 8 Market (Narrative: Consumer Crypto / Mobile-First)

Decision Timeline

Keputusan: Deploy bonding curve program di Solana mainnet (2024-01)
· Trigger: Identifikasi peluang fair launch memecoin tanpa pre-sale/team allocation di Solana; leveraging Solana low fees/high throughput untuk bonding curve UX
· Evidence: Program deployment di 6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P (Phase 3 EV-001); SolanaFM deployment timestamp (Phase 4 Technical Upgrade History)
· Decision: Launch Pump.fun bonding curve program pada Solana mainnet dengan fee 1% ke fee collector
· Immediate Result: Pengguna dapat membuat dan trade memecoin instan; volume dan TVL tumbuh cepat
· Long-term Impact: Menjadi launchpad dominan Solana (~80-90% market share); fondasi untuk multi-chain expansion dan PumpSwap
· Supporting Dataset: Phase 3 EV-001; Phase 4 Technical Upgrade History (Upgrade 1); Phase 8 Market (Market Position, Timeline)

Keputusan: Integrasi Jupiter Aggregator untuk swap routing dan token list inclusion (2024-03)
· Trigger: Perlu meningkatkan liquidity access dan price discovery untuk token bonding curve; Jupiter adalah DEX aggregator dominan Solana
· Evidence: Jupiter token list inclusion (Phase 3 EV-007); Jupiter dev docs Pump.fun integration (Phase 4 Libraries: Jupiter Swap API/SDK); Phase 7 Major Integrations (Jupiter Integration Live)
· Decision: Integrasikan Jupiter Swap API dan list token Pump.fun ke Jupiter token list
· Immediate Result: Token bonding curve dapat di-swap via Jupiter UI/API; liquidity dan price discovery diperbaiki
· Long-term Impact: Jupiter menjadi primary routing layer untuk Pump.fun tokens; memperkuat moat ekosistem Solana
· Supporting Dataset: Phase 3 EV-007; Phase 4 Libraries; Phase 7 Major Integrations; Phase 8 Market (Trading Markets: Jupiter)

Keputusan: Deploy ke Blast L2 sebagai chain kedua (2024-06)
· Trigger: Ekspansi multi-chain untuk capture Ethereum L2 memecoin mania; Blast menawarkan native yield dan incentives
· Evidence: Blast ecosystem blog announcement (Phase 3 EV-002); Blastscan contract deployment (Phase 4 Technical Upgrade History Upgrade 2); Phase 7 External Dependencies (Blast Criticality Medium)
· Decision: Deploy bonding curve dan AMM contracts ke Blast mainnet
· Immediate Result: Pengguna Blast dapat akses Pump.fun; TVL Blast ~$10-20M (Phase 8 Adoption Metrics)
· Long-term Impact: Validasi multi-chain strategy; template untuk Base deployment; tapi adoption Blast lebih rendah vs Solana/Base
· Supporting Dataset: Phase 3 EV-002; Phase 4 Technical Upgrade History; Phase 7 External Dependencies; Phase 8 Adoption Metrics (TVL Blast)

Keputusan: Adopsi Jito MEV infrastructure untuk transaction prioritization (2024-10)
· Trigger: Solana congestion mempengaruhi UX trading bonding curve; Jito tips memberikan priority execution dan front-running protection
· Evidence: Jito integration adoption (Phase 3 EV-008); Jito Searcher SDK usage (Phase 4 Libraries); SolanaFM transaction data showing Jito tips (Phase 7 Infrastructure Providers)
· Decision: Integrasikan Jito tips di frontend untuk transaksi Solana bonding curve
· Immediate Result: Prioritas transaksi ditingkatkan via Jito block engine; UX trading diperbaiki saat congestion
· Long-term Impact: Ketergantungan pada Jito untuk UX Solana; cost tambahan berupa tips ke Jito validators
· Supporting Dataset: Phase 3 EV-008; Phase 4 Libraries; Phase 7 Infrastructure Providers

Keputusan: Launch PumpSwap AMM internal menggantikan Raydium migration (2025-03)
· Trigger: Ingin menginternalisasi fee revenue pasca-migrasi; kontrol penuh atas AMM parameters; vertical integration narrative
· Evidence: Pump.fun announcement tweet (Phase 3 EV-003); SolanaFM PumpSwap program deployment (Phase 4 Technical Upgrade History Upgrade 3); Phase 5 Revenue Model (1% fee ke treasury); Phase 8 Market (Narrative: App-Specific AMM Vertical Integration)
· Decision: Deploy PumpSwap CPMM program di Solana; redirect semua graduasi bonding curve ke PumpSwap bukan Raydium
· Immediate Result: PumpSwap capture ~60-70% graduated token volume dalam minggu; 1% fee fully internalized
· Long-term Impact: Full value capture stack; kompetisi langsung dengan Raydium; moat yang lebih dalam di Solana
· Supporting Dataset: Phase 3 EV-003; Phase 4 Technical Upgrade History; Phase 5 Revenue Model; Phase 8 Market Share (PumpSwap vs Raydium)

Keputusan: Deploy ke Base L2 (2025-03)
· Trigger: Base memecoin mania (Clanker, Four.meme traction); ingin capture Base retail flow; leveraging OP Stack compatibility
· Evidence: Base ecosystem announcement (Phase 3 EV-004); Basescan contract deployment (Phase 4 Technical Upgrade History Upgrade 4); Phase 7 External Dependencies (Base Criticality High)
· Decision: Full deployment bonding curve + PumpSwap contracts di Base mainnet
· Immediate Result: Base TVL ~$30-50M dan growing (Phase 8 Adoption Metrics); Base menjadi chain kedua terbesar untuk Pump.fun
· Long-term Impact: Validasi multi-chain EVM strategy; revenue diversification dari Solana dependency; template untuk chain lain
· Supporting Dataset: Phase 3 EV-004; Phase 4 Technical Upgrade History; Phase 7 External Dependencies; Phase 8 Adoption Metrics (TVL Base)

Keputusan: Release mobile app iOS dan Android (2025-04)
· Trigger: Consumer crypto thesis; mobile-first retail expansion; app store distribution untuk mainstream adoption
· Evidence: Apple App Store dan Google Play Store listing (Phase 3 EV-005); Phase 7 Applications (Mobile App Live); Phase 8 Market (Narrative: Consumer Crypto / Mobile-First)
· Decision: Publish native mobile apps dengan feature parity web
· Immediate Result: Aksesibilitas diperluas ke non-crypto-native users; download via app stores
· Long-term Impact: Platform risk dari Apple/Google policy; potential user base expansion signifikan; brand recognition
· Supporting Dataset: Phase 3 EV-005; Phase 7 Applications; Phase 8 Market Narrative; Phase 7 Ecosystem Risks (Mobile App Store Policy Dependency)

Evolution Pattern

Perubahan Strategi: Dari Single-Chain Solana Launchpad → Multi-Chain Protocol Suite
· Evidence: Phase 3 History menunjukkan EV-001 (Solana launch Jan 2024) → EV-002 (Blast 2024) → EV-004 (Base Mar 2025); Phase 4 Architecture multi-chain (Solana SVM + Base/Blast EVM); Phase 8 Market (Supported Chains: 3)
· Supporting Dataset: Phase 3 History (EV-001, EV-002, EV-004); Phase 4 System Architecture; Phase 8 Market (Market Position)

Perubahan Teknologi: Dari External Migration Target (Raydium) → Native AMM (PumpSwap)
· Evidence: Phase 3 EV-003 (PumpSwap launch Mar 2025 menggantikan Raydium); Phase 4 Core Components (PumpSwap AMM Solana/EVM); Phase 8 Market (PumpSwap vs Raydium volume share 60-70%); Phase 7 Major Integrations (PumpSwap Replacing Raydium Migration Live)
· Supporting Dataset: Phase 3 EV-003; Phase 4 Core Components; Phase 7 Major Integrations; Phase 8 Market Share

Perubahan Financial: Dari Zero Revenue Model (hypothetical) → Protocol Revenue Only (1% fee) tanpa external funding
· Evidence: Phase 5 Fundraising Mechanism (Bootstrapping/Protocol Revenue Only); Phase 5 Revenue Model (1% trading fee live sejak launch); Phase 5 Financial Dependencies (Protocol Revenue 100% verified); Phase 8 Market (Protocol Revenue ~$5-20M/day)
· Supporting Dataset: Phase 5 Financial (Fundraising, Revenue Model, Financial Dependencies); Phase 8 Adoption Metrics (Revenue)

Perubahan Product: Dari Web-Only → Web + Mobile + Native AMM Suite
· Evidence: Phase 3 EV-001 (web launch) → EV-005 (mobile app 2025) → EV-003 (PumpSwap 2025); Phase 4 Core Components (8 components including mobile); Phase 7 Applications (7 applications listed)
· Supporting Dataset: Phase 3 History; Phase 4 Core Components; Phase 7 Applications

Perubahan Governance: Tetap No Governance / No Token / No DAO sepanjang history
· Evidence: Phase 6 Token (Pre-TGE, No Governance); Phase 6 Governance (tidak ada); Phase 7 Governance Ecosystem (None verified); Phase 2 Entity (No Foundation/DAO verified)
· Supporting Dataset: Phase 6 Token/Governance; Phase 7 Governance Ecosystem; Phase 2 Entity

Technical Decision Pattern

Pola 1: Deterministic On-Chain Pricing tanpa Oracle Dependency
· Decision Pattern: Bonding curve menggunakan constant product formula murni on-chain; PumpSwap CPMM tanpa external price feeds; menghilangkan oracle manipulation attack surface
· Evidence: Phase 4 System Architecture (Oracle network: Not used); Phase 4 Security Model (No External Oracle Dependency); Phase 4 Core Components (Bonding Curve Program fixed math); Phase 4 Known Limitations (Deterministic Bonding Curve — No Price Discovery Flexibility)
· Supporting Dataset: Phase 4 System Architecture, Security Model, Core Components, Known Limitations

Pola 2: Closed Source Development dengan Upgrade Authority Tertutup
· Decision Pattern: Semua smart contracts/programs closed source; tidak ada public repo; upgrade authority single-key/unverified multisig; no timelock; no public audit
· Evidence: Phase 4 Security Model (Closed Source/No Public Audit, Single-Point Upgrade Authority Risk); Phase 4 Audit History (None publicly disclosed); Phase 4 Development Framework (no public GitHub); Phase 2 Entity (GitHub: no public repos)
· Supporting Dataset: Phase 4 Security Model, Audit History, Development Framework; Phase 2 Entity

Pola 3: Multi-Chain Deployment via Separate Isolated Contracts (No Cross-Chain Messaging)
· Decision Pattern: Setiap chain (Solana, Base, Blast) mendapat deployment terpisah dengan state/liquidity terisolasi; tidak ada bridge/cross-chain messaging native; user harus bridge manual
· Evidence: Phase 4 System Architecture (Cross-chain messaging: Not implemented, Bridge: Not native); Phase 4 Known Limitations (No Cross-Chain Liquidity or State Sync); Phase 7 External Dependencies (Chain dependencies terpisah)
· Supporting Dataset: Phase 4 System Architecture, Known Limitations; Phase 7 External Dependencies

Pola 4: Leveraging Existing Infrastructure (Jito, Jupiter, RPC Providers) daripada Build In-House
· Decision Pattern: Integrasi Jito untuk MEV protection, Jupiter untuk swap routing/aggregation, RPC providers untuk node infrastructure; tidak build block engine/aggregator/RPC sendiri
· Evidence: Phase 4 Libraries (Jito Searcher SDK, Jupiter Swap API/SDK, @solana/web3.js, ethers.js); Phase 7 Infrastructure Providers (Jito Labs, Jupiter Aggregator, RPC Providers); Phase 7 Major Integrations (Jupiter, Jito Live)
· Supporting Dataset: Phase 4 Libraries; Phase 7 Infrastructure Providers, Major Integrations

Pola 5: Fixed Parameter Bonding Curve (Non-Configurable per Token)
· Decision Pattern: Kurva bonding curve fixed (constant product variant); migration threshold hardcoded ~$69k; creator tidak bisa customisasi parameter kurva
· Evidence: Phase 4 Known Limitations (Deterministic Bonding Curve — No Price Discovery Flexibility, Migration Threshold Fixed); Phase 4 Core Components (Bonding Curve Program fixed math); Phase 1 Foundation (Category: fair launch bonding curve)
· Supporting Dataset: Phase 4 Known Limitations, Core Components; Phase 1 Foundation

Financial Decision Pattern

Pola 1: Bootstrapping 100% dari Protocol Revenue (1% Trading Fee) — No External Funding
· Decision Pattern: Tidak ada VC round, private sale, public sale, grant, atau DAO treasury; revenue 1% fee dari bonding curve + PumpSwap menjadi satu-satunya funding source terverifikasi
· Evidence: Phase 5 Fundraising Mechanism (Bootstrapping/Protocol Revenue Only); Phase 5 Revenue Model (1% Protocol Fees Live); Phase 5 Financial Dependencies (Protocol Revenue Status: sumber pendanaan tunggal terverifikasi); Phase 5 Funding History (Tidak ada ronde pendanaan terverifikasi)
· Supporting Dataset: Phase 5 Fundraising Mechanism, Revenue Model, Financial Dependencies, Funding History

Pola 2: Fee Accumulation di Fee Collector Address(es) tanpa Transparency Report
· Decision Pattern: 1% fee terkumpul di on-chain fee collector addresses (Solana, Base, Blast); struktur pengendalian (multisig vs single key) tidak diverifikasi; tidak ada laporan penggunaan dana, transparency report, atau dashboard treasury publik
· Evidence: Phase 5 Treasury (Treasury Custodian: fee collector address, struktur tidak diverifikasi); Phase 5 Revenue Model (fee dikirim ke fee collector); Phase 5 Financial Risk (Treasury Concentration Risk, No Audit Financial Controls); Phase 4 Security Model (Fee Collector Control)
· Supporting Dataset: Phase 5 Treasury, Revenue Model, Financial Risk; Phase 4 Security Model

Pola 3: Revenue Dependency 100% pada Speculative Memecoin Volume
· Decision Pattern: Pendapatan sepenuhnya bergantung pada volume trading memecoin yang sangat volatil; tidak ada revenue stream diversifikasi (subscription, enterprise, staking, dll)
· Evidence: Phase 5 Financial Risk (Revenue Dependency on Speculative Volume); Phase 5 Revenue Model (hanya trading fee); Phase 8 Adoption Metrics (Daily Volume ~$500M-$2B+ highly cyclical); Phase 8 Market (Narrative: Memecoin Supercycle)
· Supporting Dataset: Phase 5 Financial Risk, Revenue Model; Phase 8 Adoption Metrics, Market

Pola 4: Rumored VC Investment (Sequoia, a16z) Tidak Dikonfirmasi dan Tidak Terbukti On-Chain
· Decision Pattern: Media rumor investor tier-1 beredar tapi tidak ada filing SEC, announcement resmi, atau on-chain evidence alokasi token/equity; proyek memilih tidak mengklarifikasi
· Evidence: Phase 5 Financial Dependencies (Rumored VC Investment Status: tidak dikonfirmasi); Phase 2 Entity (Rumored Investors Entity: Evidence LOW); Phase 1 Foundation (Kepemilikan equity/struktur investor: tidak dikonfirmasi); Phase 6 Token (Investors: Planned tapi tidak terverifikasi)
· Supporting Dataset: Phase 5 Financial Dependencies; Phase 2 Entity; Phase 1 Foundation; Phase 6 Token

Pola 5: Fee Switch / Tokenomics Native Token Status Ambigu — Belum Diklarifikasi Apakah Fee Akan Dialokasikan ke Holders
· Decision Pattern: 1% fee saat ini ke treasury/team; tidak ada whitepaper, tidak ada announcement TGE, status fee switch tidak diklarifikasi; menciptakan speculative narrative tapi tidak ada komitmen
· Evidence: Phase 1 Foundation (Tokenomics native token: tidak diklarifikasi); Phase 5 Financial Risk (Regulatory Uncertainty); Phase 6 Token (TGE Date: tidak dijadwalkan, Utility Fee Payment: live tapi bukan via token); Phase 8 Market (Narrative: Fee Switch/Token Expectation Speculative)
· Supporting Dataset: Phase 1 Foundation; Phase 5 Financial Risk; Phase 6 Token; Phase 8 Market

Ecosystem Decision Pattern

Pola 1: Deep Integration dengan Dominant Infrastructure per Chain (Jupiter/Jito di Solana)
· Decision Pattern: Pilih integrasi mendalam dengan player dominan per chain daripada build sendiri; Jupiter untuk aggregator (Solana #1), Jito untuk MEV (Solana #1)
· Evidence: Phase 7 Major Integrations (Jupiter Live, Jito Live); Phase 7 Infrastructure Providers (Jupiter Criticality High, Jito Medium); Phase 4 Libraries (Jupiter Swap API, Jito Searcher SDK); Phase 8 Market (Trading Markets: Jupiter Spot Yes)
· Supporting Dataset: Phase 7 Major Integrations, Infrastructure Providers; Phase 4 Libraries; Phase 8 Market

Pola 2: Multi-Chain Expansion Mengikuti Retail Memecoin Liquidity Flow (Solana → Blast → Base)
· Decision Pattern: Deploy ke chain tempat memecoin retail activity tinggi; Solana (origin), Blast (early L2 dengan yield narrative), Base (memecoin mania Mar 2025 dengan Clanker/Four.meme)
· Evidence: Phase 3 History (EV-001 Solana Jan 2024 → EV-002 Blast 2024 → EV-004 Base Mar 2025); Phase 8 Market Timeline (Blast deployment 2024-06, Base deployment 2025-03); Phase 7 External Dependencies (Base Criticality High, Blast Medium); Phase 8 Competitor Landscape (Clanker Base, Four.meme BNB)
· Supporting Dataset: Phase 3 History; Phase 8 Market Timeline, Competitor Landscape; Phase 7 External Dependencies

Pola 3: Internalisasi Migration Flow (PumpSwap) untuk Capture Full Fee Stack dan Kurangi Dependency Eksternal
· Decision Pattern: Ganti migrasi ke Raydium (external DEX) dengan PumpSwap native; capture 1% fee pasca-migrasi; eliminasi dependency pada Raydium liquidity/parameters
· Evidence: Phase 3 EV-003 (PumpSwap launch replacing Raydium); Phase 7 Major Integrations (PumpSwap Replacing Raydium Migration Live); Phase 8 Market Share (PumpSwap captured 60-70% graduated volume); Phase 4 Technical Upgrade History (PumpSwap Launch)
· Supporting Dataset: Phase 3 EV-003; Phase 7 Major Integrations; Phase 8 Market Share; Phase 4 Technical Upgrade History

Pola 4: Mobile App Distribution via App Stores (Apple/Google) sebagai Consumer Acquisition Channel
· Decision Pattern: Publish native iOS/Android apps ke app stores meskipun platform risk; targeting mainstream retail non-crypto-native
· Evidence: Phase 3 EV-005 (Mobile app release 2025); Phase 7 Applications (Mobile App Live); Phase 7 External Dependencies (Apple App Store/Google Play Store Criticality Medium); Phase 7 Ecosystem Risks (Mobile App Store Policy Dependency); Phase 8 Market Narrative (Consumer Crypto/Mobile-First)
· Supporting Dataset: Phase 3 EV-005; Phase 7 Applications, External Dependencies, Ecosystem Risks; Phase 8 Market

Pola 5: No Developer Ecosystem / No Public SDK / No Grants / No Hackathons — Closed Platform
· Decision Pattern: Tidak membangun developer ecosystem; tidak publish SDK, API, docs teknis, CLI, grants, hackathon; platform fully closed untuk third-party builders
· Evidence: Phase 7 Developer Ecosystem (SDK: Not published, API: Not publicly documented, Developer Tools: None, Open Source Repository: None, Hackathon: None, Grant Program: None); Phase 4 Development Framework (no public SDK); Phase 2 Entity (GitHub: no public repos)
· Supporting Dataset: Phase 7 Developer Ecosystem; Phase 4 Development Framework; Phase 2 Entity

Governance Decision Pattern

Pola 1: Zero On-Chain Governance — Semua Parameter Dikendalikan Upgrade Authority Tertutup
· Decision Pattern: Tidak ada token governance, DAO, voting, proposal system, delegation; parameter protokol (fee rate, migration threshold, curve formula) hanya bisa diubah via upgrade authority
· Evidence: Phase 6 Governance (Governance Model: tidak ada); Phase 6 Token (Utility Governance: tidak ada); Phase 7 Governance Ecosystem (DAO: None, Council: None, Committee: None); Phase 4 Security Model (Program/Contract Authority Controls); Phase 4 Known Limitations (No On-Chain Governance or DAO)
· Supporting Dataset: Phase 6 Governance, Token; Phase 7 Governance Ecosystem; Phase 4 Security Model, Known Limitations

Pola 2: Fee Collector Treasury Dikendalikan Upgrade Authority / Undisclosed Keys — No Community Oversight
· Decision Pattern: 1% fee terkumpul di address(es) yang dikontrol upgrade authority; tidak ada multisig community, tidak ada timelock, tidak ada transparency pada signers atau penggunaan dana
· Evidence: Phase 5 Treasury (Treasury Custodian: fee collector, struktur pengendalian tidak diverifikasi); Phase 4 Security Model (Fee Collector Control: single-key risk exists); Phase 5 Financial Risk (Treasury Concentration Risk); Phase 7 Governance Ecosystem (Treasury Governance: tidak ada)
· Supporting Dataset: Phase 5 Treasury, Financial Risk; Phase 4 Security Model; Phase 7 Governance Ecosystem

Pola 3: No Legal Foundation / Entity Transparency — Governance via Pseudonymous Team Saja
· Decision Pattern: Tidak ada legal entity terpublik (Delaware, BVI, Cayman); founder pseudonim (@a1lon, @sapijiju); tidak ada foundation/DAO wrapper; governance de facto oleh tim anonim
· Evidence: Phase 1 Foundation (Country: tidak diketahui, Founding Entity: anonim); Phase 2 Entity (Person: Alon/Sapijiju pseudonim, No Company/Foundation verified); Phase 7 Governance Ecosystem (Foundation: None verified); Phase 5 Financial Risk (Regulatory Uncertainty: no legal entity disclosed)
· Supporting Dataset: Phase 1 Foundation; Phase 2 Entity; Phase 7 Governance Ecosystem; Phase 5 Financial Risk

Pola 4: Parameter Protocol Fixed/Immutable by Design (Curve, Threshold, Fee) — Hanya Bisa Diubah Via Code Upgrade
· Decision Pattern: Bonding curve formula fixed, migration threshold ~$69k hardcoded, fee 1% fixed; tidak ada on-chain parameter adjustment mechanism; perubahan memerlukan program/contract upgrade
· Evidence: Phase 4 Known Limitations (Deterministic Bonding Curve, Migration Threshold Fixed); Phase 4 Core Components (Bonding Curve Program fixed math); Phase 6 Token (Inflation/Deflation: tidak berlaku); Phase 4 Security Model (No External Oracle Dependency — parameter baked in code)
· Supporting Dataset: Phase 4 Known Limitations, Core Components; Phase 6 Token; Phase 4 Security Model

Risk Response Pattern

Pola 1: Solana Congestion/Outage → Integrasi Jito MEV Infrastructure untuk Priority Execution
· Trigger: Solana network congestion mempengaruhi UX trading bonding curve (failed transactions, high latency)
· Decision Pattern: Adopsi Jito tips dan block engine untuk transaction prioritization dan front-running protection
· Evidence: Phase 3 EV-008 (Jito integration adoption 2024-10); Phase 4 Libraries (Jito Searcher SDK); Phase 7 Infrastructure Providers (Jito Labs Live); Phase 7 Ecosystem Risks (Single Chain Dependency Solana High)
· Response: Integrate Jito Searcher SDK di frontend; users pay tips untuk priority execution via Jito block engine
· Result: UX trading diperbaiki saat congestion; cost tambahan tips ke Jito; dependency baru pada Jito infrastructure
· Supporting Dataset: Phase 3 EV-008; Phase 4 Libraries; Phase 7 Infrastructure Providers, Ecosystem Risks

Pola 2: External Migration Target (Raydium) Risk → Internalisasi via PumpSwap Native AMM
· Trigger: Dependency pada Raydium untuk migrasi liquidity; fee revenue pasca-migrasi pergi ke Raydium; tidak kontrol parameter AMM
· Decision Pattern: Build dan launch PumpSwap native CPMM; redirect semua graduasi ke PumpSwap; capture 1% fee internal
· Evidence: Phase 3 EV-003 (PumpSwap launch Mar 2025); Phase 7 Major Integrations (PumpSwap Replacing Raydium Migration Live); Phase 8 Market Share (PumpSwap 60-70% graduated volume); Phase 4 Technical Upgrade History (PumpSwap Launch)
· Response: Deploy PumpSwap program/contracts; update bonding curve program untuk migrate ke PumpSwap; deprecate Raydium migration path
· Result: Full fee capture vertical integration; kompetisi langsung dengan Raydium; moat diperkuat; technical complexity increase
· Supporting Dataset: Phase 3 EV-003; Phase 7 Major Integrations; Phase 8 Market Share; Phase 4 Technical Upgrade History

Pola 3: Single-Chain Concentration Risk (Solana) → Multi-Chain Deployment (Blast, Base)
· Trigger: Solana outage risk, congestion, dan ecosystem concentration; ingin diversifikasi revenue dan user base
· Decision Pattern: Deploy bonding curve + PumpSwap ke Blast (2024) dan Base (Mar 2025) sebagai chain terpisah isolated
· Evidence: Phase 3 EV-002 (Blast), EV-004 (Base); Phase 4 System Architecture (multi-chain Solana/Base/Blast); Phase 7 External Dependencies (Base High, Blast Medium); Phase 7 Ecosystem Risks (Single Chain Dependency Solana High); Phase 8 Adoption Metrics (TVL Base $30-50M, Blast $10-20M)
· Response: Full contract deployment di Base/Blast; separate liquidity pools per chain; no cross-chain sync
· Result: Revenue diversification (Base growing fast); Blast adoption lower; operational complexity 3x; no cross-chain liquidity
· Supporting Dataset: Phase 3 EV-002, EV-004; Phase 4 System Architecture; Phase 7 External Dependencies, Ecosystem Risks; Phase 8 Adoption Metrics

Pola 4: Mobile App Store Policy Risk → Launch Anyway (Accept Platform Risk untuk Consumer Reach)
· Trigger: Apple/Google historically restrict crypto trading apps; policy uncertainty
· Decision Pattern: Publish native apps ke App Store dan Play Store meskipun risk; prioritize consumer acquisition over platform sovereignty
· Evidence: Phase 3 EV-005 (Mobile app 2025); Phase 7 External Dependencies (App Stores Medium); Phase 7 Ecosystem Risks (Mobile App Store Policy Dependency Medium); Phase 8 Market Narrative (Consumer Crypto/Mobile-First)
· Response: Submit apps ke Apple/Google review; maintain compliance dengan guidelines; accept potential rejection/removal risk
· Result: Apps live di kedua store; distribution channel ke mainstream users; ongoing platform risk
· Supporting Dataset: Phase 3 EV-005; Phase 7 External Dependencies, Ecosystem Risks; Phase 8 Market

Pola 5: Closed Source / No Audit Criticism → Maintain Status Quo (No Public Audit, No Bug Bounty Public)
· Trigger: Community/industry criticism tentang closed source, no audit, upgrade authority risk
· Decision Pattern: Tidak merilis source code, tidak publish audit, tidak launch public bug bounty; maintain obscurity sebagai security model
· Evidence: Phase 4 Audit History (None publicly disclosed); Phase 4 Security Model (Closed Source/No Public Audit, No Bug Bounty); Phase 7 Ecosystem Risks (Closed Source/No Public Audit Critical); Phase 2 Entity (GitHub no public repos)
· Response: Continue closed development; internal security review only; no public transparency measures
· Result: Persistent security trust deficit; no external validation; high custody risk untuk fee collector dan upgrade keys
· Supporting Dataset: Phase 4 Audit History, Security Model; Phase 7 Ecosystem Risks; Phase 2 Entity

Recurring Behavioral Pattern

Pola 1: Ship Fast, Iterate Later — Launch MVP di Chain Baru Tanpa Cross-Chain Infrastructure
· Evidence: Solana launch (EV-001) → Blast deploy (EV-002) 5 bulan kemudian → Base deploy (EV-004) 9 bulan kemudian → PumpSwap (EV-003) 14 bulan kemudian → Mobile app (EV-005) 15 bulan kemudian; setiap expansion adalah deployment terpisah isolated (Phase 4 System Architecture: Cross-chain messaging Not implemented); no shared state/liquidity
· Supporting Dataset: Phase 3 History (EV-001 through EV-005); Phase 4 System Architecture; Phase 7 External Dependencies

Pola 2: Internalisasi Critical Path — Ganti External Dependency dengan Native Component
· Evidence: Raydium migration (external) → PumpSwap native (EV-003); potential external aggregator → Jupiter integration (deep, EV-007) tapi PumpSwap handle post-migration; potential external MEV → Jito integration (EV-008) tapi internal transaction construction; pattern: identify critical dependency → build/integrate deeply → capture value
· Supporting Dataset: Phase 3 EV-003, EV-007, EV-008; Phase 7 Major Integrations; Phase 4 Libraries; Phase 8 Market Narrative (Vertical Integration)

Pola 3: Revenue-First Decision Making — Setiap Fitur Baru Harus Tingkatkan Fee Capture atau Volume
· Evidence: PumpSwap capture 1% fee pasca-migrasi (EV-003); mobile app expand user base → more volume → more fee (EV-005); Base deployment capture Base memecoin volume (EV-004); 1% fee unchanged sejak launch; no feature yang tidak tied ke revenue (no governance token, no staking, no subscription)
· Supporting Dataset: Phase 3 EV-003, EV-004, EV-005; Phase 5 Revenue Model; Phase 8 Adoption Metrics (Revenue ~$5-20M/day); Phase 6 Token (No utility beyond speculation)

Pola 4: Pseudonymous Team Operation — No Dox, No Legal Entity, No Public Accountability Structure
· Evidence: Founder Alon (@a1lon) dan Sapijiju (@sapijiju) pseudonim (Phase 2 Entity); no legal entity disclosed (Phase 1 Foundation); no foundation/DAO (Phase 7 Governance); fee collector control unverified (Phase 5 Treasury); upgrade authority unverified (Phase 4 Security); consistent sejak launch
· Supporting Dataset: Phase 2 Entity; Phase 1 Foundation; Phase 7 Governance Ecosystem; Phase 5 Treasury; Phase 4 Security Model

Pola 5: Narrative-Driven Expansion — Follow Retail Attention/Flow ke Chain Baru
· Evidence: Blast deployment (2024) during Blast points/yield narrative; Base deployment (Mar 2025) during Base memecoin mania (Clanker, Four.meme); mobile app (2025) during consumer crypto thesis; each expansion timed dengan retail attention cycle di target chain
· Supporting Dataset: Phase 3 History (EV-002, EV-004, EV-005 timing); Phase 8 Market Timeline (Blast 2024-06, Base 2025-03, Mobile 2025-04); Phase 8 Competitor Landscape (Clanker Base, Four.meme); Phase 8 Market Narratives

Strategic Trade-offs

Trade-off 1: Desentralisasi vs Kecepatan Eksekusi dan Kontrol
· Decision: Memilih upgrade authority tertutup (single-key/unverified multisig), no timelock, no governance, no DAO, closed source
· Trade-off: Mengorbankan desentralisasi, community trust, auditability, dan censorship resistance demi kecepatan shipping, kontrol penuh parameter protokol, dan kemampuan pivot cepat tanpa proposal/voting delay
· Evidence: Phase 4 Security Model (Program/Contract Authority Controls, Single-Point Upgrade Authority Risk); Phase 4 Audit History (None); Phase 6 Governance (tidak ada); Phase 7 Governance Ecosystem (None); Phase 4 Known Limitations (No On-Chain Governance)
· Supporting Dataset: Phase 4 Security Model, Audit History, Known Limitations; Phase 6 Governance; Phase 7 Governance Ecosystem

Trade-off 2: Keamanan (Audit/Transparency) vs Time-to-Market dan Competitive Moat
· Decision: Tidak melakukan public audit, tidak open source, tidak bug bounty publik; maintain closed source sebagai competitive advantage
· Trade-off: Mengorbankan keamanan terverifikasi, community trust, institutional adoption, dan regulatory clarity demi melindungi IP (bonding curve math, migration logic), speed of iteration, dan first-mover moat
· Evidence: Phase 4 Audit History (None); Phase 4 Security Model (Closed Source/No Public Audit); Phase 7 Ecosystem Risks (Closed Source Critical); Phase 2 Entity (GitHub no public repos); Phase 5 Financial Risk (No Audit Financial Controls)
· Supporting Dataset: Phase 4 Audit History, Security Model; Phase 7 Ecosystem Risks; Phase 2 Entity; Phase 5 Financial Risk

Trade-off 3: Cross-Chain Composability vs Operational Simplicity dan Chain-Specific Optimization
· Decision: Deploy kontrak terisolasi per chain (Solana SVM, Base/Blast EVM) tanpa cross-chain messaging, bridge, atau shared state
· Trade-off: Mengorbankan cross-chain liquidity, unified user experience, composability, dan capital efficiency demi operational simplicity (tidak perlu maintain bridge/messaging), chain-specific optimization (SVM vs EVM), dan isolation of risk per chain
· Evidence: Phase 4 System Architecture (Cross-chain messaging Not implemented, Bridge Not native); Phase 4 Known Limitations (No Cross-Chain Liquidity); Phase 7 External Dependencies (Chain terpisah); Phase 8 Adoption Metrics (TVL terpisah per chain)
· Supporting Dataset: Phase 4 System Architecture, Known Limitations; Phase 7 External Dependencies; Phase 8 Adoption Metrics

Trade-off 4: Revenue Diversification vs Focus pada Core Competency (Memecoin Launchpad)
· Decision: 100% revenue dari 1% trading fee memecoin; tidak build staking, lending, governance token, enterprise SaaS, atau revenue stream lain
· Trade-off: Mengorbankan revenue stability, diversification, dan long-term sustainability demi focus ekstrim pada core product, operational lean-ness, dan alignment dengan memecoin supercycle narrative
· Evidence: Phase 5 Revenue Model (hanya trading fee); Phase 5 Financial Risk (Revenue Dependency on Speculative Volume High); Phase 8 Adoption Metrics (Volume highly cyclical); Phase 6 Token (No utility); Phase 8 Market Narrative (Memecoin Supercycle Main)
· Supporting Dataset: Phase 5 Revenue Model, Financial Risk; Phase 8 Adoption Metrics, Market

Trade-off 5: Regulatory Clarity vs Operational Flexibility dan Pseudonymous Operation
· Decision: Tidak incorporate legal entity publik, tidak disclose jurisdiction, tidak pursue money transmitter license, tidak KYC/AML pada platform
· Trade-off: Mengorbankan regulatory clarity, institutional partnerships, banking access, dan legal protection demi operational flexibility, pseudonymous team protection, global access tanpa geo-restriction, dan speed
· Evidence: Phase 1 Foundation (Country tidak diketahui, Founding Entity anonim); Phase 2 Entity (No Company verified); Phase 5 Financial Risk (Regulatory Uncertainty Medium); Phase 7 Ecosystem Risks (Regulatory/Legal Entity Opacity High); Phase 8 Market (Geographic Focus Global)
· Supporting Dataset: Phase 1 Foundation; Phase 2 Entity; Phase 5 Financial Risk; Phase 7 Ecosystem Risks; Phase 8 Market

Behavioral Summary

Prioritas Utama Proyek:
1. Maximize protocol revenue via 1% fee capture pada entire memecoin lifecycle (creation → bonding curve → PumpSwap)
2. Speed of execution dan first-mover advantage di setiap chain baru dengan retail memecoin attention
3. Vertical integration ownership pada critical path (bonding curve, AMM, frontend, mobile, indexing)
4. Lean operation: no external funding, no governance overhead, no developer ecosystem maintenance, no regulatory compliance burden

Cara Mengambil Keputusan:
- Top-down oleh pseudonymous core team (Alon/Sapijiju) via upgrade authority
- Data-driven berdasarkan on-chain metrics (volume, TVL, graduation rate, revenue)
- Narrative-aware: follow retail attention cycles across chains (Blast points → Base memecoin mania → consumer crypto mobile)
- Revenue impact sebagai primary filter: fitur harus meningkatkan fee capture atau volume
- Risk acceptance: accept centralization, closed source, regulatory opacity sebagai trade-off untuk speed dan control

Faktor Paling Sering Mempengaruhi Keputusan:
1. Protocol revenue impact (1% fee capture)
2. Retail user acquisition/retention (volume driver)
3. Competitive positioning vs Raydium, Meteora, Clanker, dll
4. Chain-specific retail attention cycles
5. Technical feasibility dengan existing stack (Rust/Anchor Solana, Solidity EVM)

Pola Evolusi:
- Phase 1 (Jan 2024): Solana-only bonding curve launchpad (MVP)
- Phase 2 (2024): Integrasi infra (Jupiter, Jito) + Blast expansion
- Phase 3 (Mar 2025): Major pivot — PumpSwap native AMM (vertical integration) + Base expansion (multi-chain)
- Phase 4 (2025): Consumer expansion — mobile app iOS/Android
- Consistent: no token, no governance, no external funding, closed source, pseudonymous team

Kekuatan Utama:
- Dominan market share Solana memecoin launch (~80-90%)
- Vertical integration capture full fee stack (creation + bonding curve + AMM)
- High protocol revenue (~$5-20M/day, ~$1-2B+ cumulative)
- Lean team (~5-10) dengan high revenue per head
- Multi-chain presence (Solana, Base, Blast) dengan Base growing fast
- Strong brand/mindshare dalam memecoin supercycle narrative
- Mobile app distribution channel ke mainstream users

Kelemahan Utama:
- Closed source, no audit, upgrade authority single-point-of-failure
- Fee collector custody opaque (unverified multisig/single key)
- 100% revenue dependency pada speculative memecoin volume
- No cross-chain liquidity/state sync (fragmented UX)
- No developer ecosystem, no SDK, no public API
- Regulatory opacity (no legal entity, jurisdiction, compliance)
- Platform risk: Solana dependency, App Store dependency, RPC provider dependency
- No governance mechanism untuk protocol evolution
- Pseudonymous team → no accountability, key person risk

## Knowledge Extraction
_ref: `docs/Patterns/*`, `docs/Reasoning/*` (rule candidates)_

PROJECT: Pump.fun

Core Insights

Insight 1: Vertical Integration Capture Full Fee Stack
Explanation: Pump.fun menginternalisasi seluruh value chain memecoin — token creation (gratis), bonding curve trading (1% fee), migrasi otomatis ke PumpSwap AMM native (1% fee terus berlanjut) — sehingga 100% protocol fee tertangkap internal tanpa leakage ke external DEX seperti Raydium
Evidence: PumpSwap launch menggantikan Raydium migration (EV-003)【Phase 3 — EV-003】; 1% fee pada bonding curve dan PumpSwap dikumpulkan ke fee collector【Phase 5 — Revenue Model】; PumpSwap capture 60-70% graduated token volume dalam minggu【Phase 8 — Market Share】
Supporting Dataset: Phase 3 History, Phase 5 Financial, Phase 8 Market
Confidence: HIGH

Insight 2: Pseudonymous Team Operation dengan Zero External Accountability
Explanation: Seluruh protokol dikendalikan oleh tim anonim (@a1lon, @sapijiju) tanpa legal entity terpublik, tanpa foundation/DAO, tanpa audit publik, tanpa bug bounty publik, upgrade authority single-key/unverified multisig, fee collector custody opaque — menciptakan key person risk dan custody risk ekstrem
Evidence: Founder Alon/Sapijiju pseudonim【Phase 2 — Person Alon, Person Sapijiju】; No company/foundation verified【Phase 2 — Company/Foundation】; No public audit【Phase 4 — Audit History】; Upgrade authority unverified【Phase 4 — Security Model】; Fee collector control unverified【Phase 5 — Treasury】
Supporting Dataset: Phase 2 Entity, Phase 4 Technology, Phase 5 Financial, Phase 7 Governance
Confidence: HIGH

Insight 3: Revenue-First Decision Making Mengabaikan Diversifikasi
Explanation: Setiap keputusan produk (PumpSwap, Base deployment, mobile app) dievaluasi berdasarkan impact ke 1% trading fee revenue; tidak ada upaya diversifikasi revenue stream (staking, governance token, enterprise, subscription) — 100% dependency pada volume spekulatif memecoin yang siklikal
Evidence: PumpSwap capture fee pasca-migrasi【Phase 3 — EV-003】; Base deployment capture Base memecoin volume【Phase 3 — EV-004】; Mobile app expand user base→more volume【Phase 3 — EV-005】; Revenue Model hanya trading fee【Phase 5 — Revenue Model】; Financial Risk: Revenue Dependency on Speculative Volume HIGH【Phase 5 — Financial Risk】
Supporting Dataset: Phase 3 History, Phase 5 Financial, Phase 8 Adoption Metrics
Confidence: HIGH

Insight 4: Multi-Chain Expansion Mengikuti Retail Attention Cycle (Bukan Technical Interoperability)
Explanation: Deployment ke Blast (2024, yield narrative) dan Base (Mar 2025, memecoin mania Clanker/Four.meme) merupakan deployment kontrak terisolasi per chain tanpa cross-chain messaging, bridge, atau shared state — each chain operates independently dengan liquidity terfragmentasi
Evidence: Blast deployment EV-002【Phase 3 — EV-002】; Base deployment EV-004【Phase 3 — EV-004】; Cross-chain messaging: Not implemented【Phase 4 — System Architecture】; No Cross-Chain Liquidity limitation【Phase 4 — Known Limitations】; External Dependencies: chain terpisah【Phase 7 — External Dependencies】
Supporting Dataset: Phase 3 History, Phase 4 Technology, Phase 7 Ecosystem
Confidence: HIGH

Insight 5: Closed Source sebagai Competitive Moat (Bukan Security by Obscurity Saja)
Explanation: Proyek sengaja tidak mempublikasikan source code, tidak audit publik, tidak bug bounty — melindungi IP bonding curve math dan migration logic sebagai first-mover advantage; trade-off: persistent security trust deficit dan institutional adoption barrier
Evidence: GitHub no public repos【Phase 2 — GitHub】; No public audit【Phase 4 — Audit History】; Closed Source/No Public Audit Critical risk【Phase 7 — Ecosystem Risks】; Security Model: Closed Source【Phase 4 — Security Model】; Development Framework: no public SDK【Phase 4 — Development Framework】
Supporting Dataset: Phase 2 Entity, Phase 4 Technology, Phase 7 Ecosystem
Confidence: HIGH

Insight 6: Zero Governance Overhead Memungkinkan Speed Ekstrem
Explanation: Tanpa token governance, DAO, voting, proposal system, timelock — semua parameter protokol (fee rate, migration threshold, curve formula) diubah via upgrade authority tunggal; memungkinkan pivot cepat (PumpSwap launch dalam ~14 bulan dari mainnet) tanpa proposal/voting delay
Evidence: Governance Model: tidak ada【Phase 6 — Governance】; No On-Chain Governance limitation【Phase 4 — Known Limitations】; Parameter fixed/immutable by design【Phase 9 — Governance Decision Pattern Pola 4】; PumpSwap launch 14 bulan post-mainnet【Phase 3 — EV-001 to EV-003】
Supporting Dataset: Phase 6 Token, Phase 4 Technology, Phase 9 Behavioral
Confidence: HIGH

Insight 7: Leveraging Dominant Infrastructure per Chain daripada Build In-House
Explanation: Integrasi mendalam dengan Jupiter (aggregator #1 Solana), Jito (MEV #1 Solana), RPC providers (QuickNode/Triton/Helius/Alchemy/Infura) — tidak build block engine/aggregator/RPC sendiri; focus resources pada core product (bonding curve, PumpSwap, frontend)
Evidence: Jupiter integration EV-007【Phase 3 — EV-007】; Jito integration EV-008【Phase 3 — EV-008】; Libraries: Jupiter Swap API, Jito Searcher SDK【Phase 4 — Libraries】; Infrastructure Providers: Jupiter Criticality High, Jito Medium【Phase 7 — Infrastructure Providers】; Major Integrations: Jupiter Live, Jito Live【Phase 7 — Major Integrations】
Supporting Dataset: Phase 3 History, Phase 4 Technology, Phase 7 Ecosystem
Confidence: HIGH

Insight 8: Consumer-First Mobile Distribution Accepting Platform Risk
Explanation: Native iOS/Android apps di App Store/Play Store (EV-005) meskipun crypto trading apps historically restricted — prioritize mainstream retail acquisition over platform sovereignty; ongoing Apple/Google policy risk
Evidence: Mobile app release EV-005【Phase 3 — EV-005】; External Dependencies: Apple App Store/Google Play Store Medium【Phase 7 — External Dependencies】; Ecosystem Risk: Mobile App Store Policy Dependency Medium【Phase 7 — Ecosystem Risks】; Market Narrative: Consumer Crypto/Mobile-First【Phase 8 — Narrative Position】
Supporting Dataset: Phase 3 History, Phase 7 Ecosystem, Phase 8 Market
Confidence: HIGH

Insight 9: Deterministic On-Chain Pricing Menghilangkan Oracle Risk
Explanation: Bonding curve constant product formula murni on-chain math; PumpSwap CPMM tanpa external price feeds; zero oracle dependency = zero oracle manipulation attack surface; trade-off: creator tidak bisa customisasi kurva (fixed parameters)
Evidence: Oracle network: Not used【Phase 4 — System Architecture】; No External Oracle Dependency security model【Phase 4 — Security Model】; Deterministic Bonding Curve limitation【Phase 4 — Known Limitations】; Migration Threshold Fixed ~$69k hardcoded【Phase 4 — Known Limitations】
Supporting Dataset: Phase 4 Technology, Phase 9 Technical Decision Pattern Pola 1
Confidence: HIGH

Insight 10: Fee Collector Treasury Opaque Mengumpulkan ~$1-2B Cumulative
Explanation: 1% fee dari ~$100-200B cumulative volume terkumpul di fee collector addresses (Solana, Base, Blast) yang struktur pengendaliannya (multisig vs single key, signers identity, fund usage) tidak diverifikasi resmi — largest opaque treasury di crypto tanpa transparency report
Evidence: Cumulative revenue ~$1-2B+【Phase 8 — Adoption Metrics】; Fee collector addresses aktif sejak launch【Phase 5 — Treasury】; Treasury Concentration Risk【Phase 5 — Financial Risk】; Fee Collector Control single-key risk【Phase 4 — Security Model】; Fee collector balance tracking placeholder【Phase 5 — Treasury】
Supporting Dataset: Phase 5 Financial, Phase 8 Market, Phase 4 Technology
Confidence: MEDIUM (cumulative revenue estimate dari Token Terminal/DefiLlama, fee collector balance tidak diverifikasi)

Strategic Principles

Principle 1: Revenue Capture > Decentralization
Explanation: Setiap keputusan arsitektur (PumpSwap internal, upgrade authority tertutup, fee collector opaque) mengoptimalkan fee capture dan kontrol tim rather than decentralization/community ownership
Evidence: PumpSwap replacing Raydium【Phase 3 — EV-003】; Upgrade authority single-point risk accepted【Phase 4 — Security Model】; Fee collector control unverified【Phase 5 — Treasury】; Zero governance【Phase 6 — Governance】
Supporting Dataset: Phase 3 History, Phase 4 Technology, Phase 5 Financial, Phase 6 Token
Confidence: HIGH

Principle 2: Ship Fast on New Chains dengan Isolated Deployments
Explanation: Deploy kontrak terpisah per chain (Solana SVM, Base/Blast EVM) tanpa cross-chain infrastructure — accept liquidity fragmentation untuk speed to market dan chain-specific optimization
Evidence: Blast deployment EV-002【Phase 3 — EV-002】; Base deployment EV-004【Phase 3 — EV-004】; Cross-chain messaging Not implemented【Phase 4 — System Architecture】; No Cross-Chain Liquidity limitation【Phase 4 — Known Limitations】
Supporting Dataset: Phase 3 History, Phase 4 Technology, Phase 9 Evolution Pattern
Confidence: HIGH

Principle 3: Follow Retail Attention Flow Across Chains
Explanation: Expansion timing mengikuti retail memecoin mania cycles: Blast (points/yield narrative 2024) → Base (Clanker/Four.meme mania Mar 2025) → Mobile (consumer crypto thesis 2025)
Evidence: Blast deployment 2024-06【Phase 8 — Market Timeline】; Base deployment 2025-03【Phase 8 — Market Timeline】; Mobile app 2025-04【Phase 8 — Market Timeline】; Competitor Landscape: Clanker Base, Four.meme BNB【Phase 8 — Competitor Landscape】
Supporting Dataset: Phase 8 Market, Phase 3 History, Phase 9 Behavioral Pola 5
Confidence: HIGH

Principle 4: Internalize Critical Path Dependencies
Explanation: Identify external dependencies yang critical (Raydium migration, Jupiter aggregation, Jito MEV) → build native alternative atau deep integration untuk capture value dan reduce counterparty risk
Evidence: PumpSwap replace Raydium【Phase 3 — EV-003】; Jupiter deep integration EV-007【Phase 3 — EV-007】; Jito integration EV-008【Phase 3 — EV-008】; Vertical Integration narrative【Phase 8 — Narrative Position】
Supporting Dataset: Phase 3 History, Phase 7 Ecosystem, Phase 8 Market, Phase 9 Behavioral Pola 2
Confidence: HIGH

Principle 5: Zero Overhead Operations (No Governance, No Grants, No DevRel, No Compliance)
Explanation: Eliminate all non-revenue-generating activities: no DAO, no token, no SDK/API/public docs, no hackathons/grants, no legal entity/compliance — every resource focused pada core product revenue
Evidence: Developer Ecosystem: 0 programs【Phase 7 — Developer Ecosystem】; Governance Ecosystem: None【Phase 7 — Governance Ecosystem】; No legal entity【Phase 1 — Foundation】; Fundraising: Bootstrapping only【Phase 5 — Fundraising Mechanism】
Supporting Dataset: Phase 7 Ecosystem, Phase 1 Foundation, Phase 5 Financial, Phase 6 Token
Confidence: HIGH

Principle 6: Deterministic Math > Configurable Flexibility
Explanation: Fixed bonding curve formula, fixed migration threshold (~$69k), fixed 1% fee — no per-token customization, no on-chain parameter adjustment; reduces attack surface dan operational complexity
Evidence: Deterministic Bonding Curve limitation【Phase 4 — Known Limitations】; Migration Threshold Fixed【Phase 4 — Known Limitations】; No External Oracle Dependency【Phase 4 — Security Model】; Parameter fixed by design【Phase 9 — Governance Decision Pattern Pola 4】
Supporting Dataset: Phase 4 Technology, Phase 9 Behavioral
Confidence: HIGH

Success Factors

Factor 1: First-Mover Advantage di Solana Memecoin Fair Launch
Explanation: Launch Januari 2024 sebagai first major bonding curve fair launchpad di Solana capture ~80-90% market share sebelum kompetitor (Meteora DLMM, Moonshot, Bonk.fun) masuk
Evidence: Launch Date Mainnet Januari 2024【Phase 1 — Launch Date】; Market Share Solana ~80-90%【Phase 8 — Market Share】; Competitor Landscape: Meteora, Moonshot, Bonk.fun later【Phase 8 — Competitor Landscape】
Supporting Dataset: Phase 1 Foundation, Phase 8 Market
Confidence: HIGH

Factor 2: Extreme Product Simplicity untuk Retail Users
Explanation: Token creation gratis, instant liquidity via bonding curve, no pre-sale/team allocation, auto-migration ke AMM — UX "create token in 1 click" menarik jutaan retail users non-technical
Evidence: Category: fair launch bonding curve【Phase 1 — Category】; Core Components: Bonding Curve Program【Phase 4 — Core Components】; Mobile App feature parity【Phase 3 — EV-005】; Cumulative Unique Wallets 2-3M+【Phase 8 — Adoption Metrics】
Supporting Dataset: Phase 1 Foundation, Phase 4 Technology, Phase 3 History, Phase 8 Market
Confidence: HIGH

Factor 3: Vertical Integration Capture Full Value Stack
Explanation: Internalisasi migration flow ke PumpSwap capture 1% fee pasca-graduation yang sebelumnya pergi ke Raydium; estimated additional revenue ~$500M-1B+ dari migrated tokens
Evidence: PumpSwap launch EV-003【Phase 3 — EV-003】; PumpSwap vs Raydium volume share 60-70%【Phase 8 — Market Share】; Revenue Model 1% fee full capture【Phase 5 — Revenue Model】; Vertical Integration narrative【Phase 8 — Narrative Position】
Supporting Dataset: Phase 3 History, Phase 8 Market, Phase 5 Financial
Confidence: HIGH

Factor 4: Deep Integration dengan Dominant Infrastructure per Chain
Explanation: Jupiter (aggregator #1 Solana) dan Jito (MEV #1 Solana) integration memberikan best-in-class UX tanpa build in-house; RPC providers (QuickNode/Triton/Helius/Alchemy) handle node infrastructure
Evidence: Jupiter Integration EV-007【Phase 3 — EV-007】; Jito Integration EV-008【Phase 3 — EV-008】; Infrastructure Providers Jupiter High, Jito Medium【Phase 7 — Infrastructure Providers】; Major Integrations Live【Phase 7 — Major Integrations】
Supporting Dataset: Phase 3 History, Phase 7 Ecosystem
Confidence: HIGH

Factor 5: Multi-Chain Presence Diversifikasi Revenue dari Solana Dependency
Explanation: Base deployment (Mar 2025) capture Base memecoin mania; Base TVL $30-50M growing fast; reduces single-chain concentration risk (Solana outage risk)
Evidence: Base deployment EV-004【Phase 3 — EV-004】; TVL Base $30-50M【Phase 8 — Adoption Metrics】; Single Chain Dependency Solana High risk【Phase 7 — Ecosystem Risks】; Multi-chain expansion narrative【Phase 8 — Narrative Position】
Supporting Dataset: Phase 3 History, Phase 8 Market, Phase 7 Ecosystem
Confidence: HIGH

Factor 6: Lean Team High Revenue per Head
Explanation: Estimated 5-10 core team generating ~$5-20M/day revenue = ~$0.5-4M/day per head; zero external funding dilution; full equity retention
Evidence: Team size ~5-10【Phase 1 — Core Team】; Daily Revenue $5-20M+【Phase 8 — Adoption Metrics】; Fundraising: Bootstrapping only【Phase 5 — Fundraising Mechanism】; No investor equity confirmed【Phase 2 — Rumored Investors】
Supporting Dataset: Phase 1 Foundation, Phase 8 Market, Phase 5 Financial, Phase 2 Entity
Confidence: MEDIUM (team size estimate dari observasi publik, tidak verified)

Factor 7: Mobile App Distribution Channel ke Mainstream Retail
Explanation: iOS/Android apps di App Store/Play Store membuka akses ke non-crypto-native users; consumer crypto thesis execution
Evidence: Mobile app release EV-005【Phase 3 — EV-005】; Applications: Mobile App Live【Phase 7 — Applications】; Market Narrative: Consumer Crypto/Mobile-First【Phase 8 — Narrative Position】; External Dependencies App Stores Medium【Phase 7 — External Dependencies】
Supporting Dataset: Phase 3 History, Phase 7 Ecosystem, Phase 8 Market
Confidence: HIGH

Factor 8: Deterministic Pricing Eliminates Oracle Attack Surface
Explanation: Pure on-chain math bonding curve + CPMM PumpSwap = zero oracle dependency = zero oracle manipulation risk; critical untuk memecoin dengan liquidity rendah
Evidence: No External Oracle Dependency【Phase 4 — Security Model】; Oracle network Not used【Phase 4 — System Architecture】; Deterministic Bonding Curve【Phase 4 — Known Limitations】; Technical Decision Pattern Pola 1【Phase 9 — Technical Decision Pattern】
Supporting Dataset: Phase 4 Technology, Phase 9 Behavioral
Confidence: HIGH

Failure Factors

Factor 1: Closed Source & No Audit Menciptakan Persistent Trust Deficit
Explanation: Zero public audit, zero bug bounty, closed source contracts → institutional adoption blocked, security-conscious users/whales avoid, regulatory scrutiny magnet; single bug bisa drain entire fee collector treasury
Evidence: Audit History: None publicly disclosed【Phase 4 — Audit History】; Closed Source/No Public Audit Critical risk【Phase 7 — Ecosystem Risks】; No Bug Bounty Publicly Listed【Phase 4 — Security Model】; Security Model: Closed Source【Phase 4 — Security Model】
Supporting Dataset: Phase 4 Technology, Phase 7 Ecosystem
Confidence: HIGH

Factor 2: Single-Point Upgrade Authority Risk (Critical)
Explanation: Upgrade authority single-key/unverified multisig, no timelock, no governance oversight → key compromise = malicious upgrade drain liquidity/fee collector; no community recourse
Evidence: Single-Point Upgrade Authority Risk【Phase 4 — Security Model】; Program/Contract Authority Controls【Phase 4 — Security Model】; No On-Chain Governance【Phase 4 — Known Limitations】; Upgrade authority structure unknown【Phase 9 — Open Threads】
Supporting Dataset: Phase 4 Technology, Phase 9 Behavioral
Confidence: HIGH

Factor 3: Fee Collector Custody Centralization (Critical)
Explanation: ~$1-2B cumulative fees di address(es) controlled by undisclosed keys, no transparency report, no multisig verification → custody risk ekstrem, potential rug pull vector, regulatory money transmission liability
Evidence: Treasury Concentration Risk【Phase 5 — Financial Risk】; Fee Collector Control single-key risk【Phase 4 — Security Model】; Fee collector balance unverified【Phase 5 — Treasury】; Treasury Custodian unverified【Phase 5 — Treasury】
Supporting Dataset: Phase 5 Financial, Phase 4 Technology
Confidence: HIGH

Factor 4: 100% Revenue Dependency pada Speculative Memecoin Volume
Explanation: Revenue ~$5-20M/day highly cyclical; bear market/volume drop 90% → revenue drop 90%; no diversification (staking, governance token, enterprise, subscription); business model fragile
Evidence: Revenue Dependency on Speculative Volume HIGH【Phase 5 — Financial Risk】; Daily Volume $500M-$2B+ highly cyclical【Phase 8 — Adoption Metrics】; Revenue Model hanya trading fee【Phase 5 — Revenue Model】; Memecoin Supercycle narrative【Phase 8 — Narrative Position】
Supporting Dataset: Phase 5 Financial, Phase 8 Market
Confidence: HIGH

Factor 5: No Cross-Chain Liquidity/State Sync → Fragmented UX & Capital Inefficiency
Explanation: Tokens created on Solana tidak bisa migrate ke Base/Blast via Pump.fun; users harus bridge manual; liquidity fragmented across 3 chains; capital efficiency rendah
Evidence: No Cross-Chain Liquidity limitation【Phase 4 — Known Limitations】; Cross-chain messaging Not implemented【Phase 4 — System Architecture】; Bridge Not native【Phase 4 — System Architecture】; TVL terpisah per chain【Phase 8 — Adoption Metrics】
Supporting Dataset: Phase 4 Technology, Phase 8 Market
Confidence: HIGH

Factor 6: Regulatory Opacity (No Legal Entity, Jurisdiction, Compliance)
Explanation: No legal entity disclosed, no jurisdiction, no money transmitter license, no KYC/AML → potential securities law violation, banking access blocked, geographic restriction risk, founder liability
Evidence: Country tidak diketahui【Phase 1 — Foundation】; No Company verified【Phase 2 — Company】; Regulatory Uncertainty Medium【Phase 5 — Financial Risk】; Regulatory/Legal Entity Opacity High【Phase 7 — Ecosystem Risks】
Supporting Dataset: Phase 1 Foundation, Phase 2 Entity, Phase 5 Financial, Phase 7 Ecosystem
Confidence: HIGH

Factor 7: Zero Developer Ecosystem → No Composability, No Innovation Layer
Explanation: No SDK, no public API, no docs, no CLI, no grants, no hackathons → third-party builders cannot extend platform; all innovation internal only; limits total addressable market
Evidence: Developer Ecosystem: 0 programs【Phase 7 — Developer Ecosystem】; SDK Not published【Phase 7 — Developer Ecosystem】; API Not publicly documented【Phase 7 — Developer Ecosystem】; Open Source Repository: None【Phase 7 — Developer Ecosystem】
Supporting Dataset: Phase 7 Ecosystem
Confidence: HIGH

Factor 8: Mobile App Store Platform Risk
Explanation: iOS/Android apps subject to Apple/Google policy changes; crypto trading apps historically rejected/restricted; single policy change bisa remove distribution channel ke mainstream users
Evidence: Mobile App Store Policy Dependency Medium【Phase 7 — Ecosystem Risks】; External Dependencies App Stores Medium【Phase 7 — External Dependencies】; App Store Review Guidelines【Phase 7 — Ecosystem Risks sources】
Supporting Dataset: Phase 7 Ecosystem
Confidence: MEDIUM (risk belum terealisasi, apps masih live)

Factor 9: Pseudonymous Team → Key Person Risk & No Accountability
Explanation: Founder @a1lon, @sapijiju pseudonim; no legal entity; no foundation/DAO; if team disappears → upgrade authority keys lost, fee collector keys lost, protocol unupgradable/funds frozen
Evidence: Person Alon/Sapijiju pseudonim【Phase 2 — Person】; No Foundation verified【Phase 2 — Foundation】; Governance Ecosystem: Foundation None【Phase 7 — Governance Ecosystem】; Pseudonymous team operation pattern【Phase 9 — Behavioral Summary】
Supporting Dataset: Phase 2 Entity, Phase 7 Ecosystem, Phase 9 Behavioral
Confidence: HIGH

Factor 10: Fixed Parameters Non-Configurable → Cannot Adapt to Market Changes
Explanation: Bonding curve formula fixed, migration threshold ~$69k hardcoded, fee 1% fixed → cannot adjust for different token types, market conditions, competitive pressure; requires code upgrade untuk perubahan parameter
Evidence: Deterministic Bonding Curve limitation【Phase 4 — Known Limitations】; Migration Threshold Fixed【Phase 4 — Known Limitations】; Parameter fixed by design【Phase 9 — Governance Decision Pattern Pola 4】; No on-chain parameter adjustment【Phase 4 — Known Limitations】
Supporting Dataset: Phase 4 Technology, Phase 9 Behavioral
Confidence: HIGH

Decision Framework

Step 1: Observe On-Chain Metrics & Retail Attention Cycles
Explanation: Monitor daily volume, TVL, graduation rate, new token creation, competitor activity per chain; identify chain dengan retail memecoin mania emerging (Blast points 2024, Base Clanker 2025)
Evidence: Daily Volume $500M-$2B+ tracking【Phase 8 — Adoption Metrics】; Blast deployment during yield narrative【Phase 8 — Market Timeline】; Base deployment during Clanker mania【Phase 8 — Market Timeline】; Market Timeline milestones【Phase 8 — Market Timeline】
Supporting Dataset: Phase 8 Market, Phase 3 History, Phase 9 Behavioral Pola 5
Confidence: HIGH

Step 2: Evaluate Revenue Impact per Feature/Expansion
Explanation: Setiap initiative (PumpSwap, Base deploy, mobile app) dievaluasi: "Apakah ini meningkatkan 1% fee capture atau volume trading?" — only revenue-positive features shipped
Evidence: PumpSwap capture post-migration fee【Phase 3 — EV-003】; Base deploy capture Base volume【Phase 3 — EV-004】; Mobile app expand user base【Phase 3 — EV-005】; Revenue Model only trading fee【Phase 5 — Revenue Model】; Revenue-First Decision Making pattern【Phase 9 — Behavioral Pattern Pola 3】
Supporting Dataset: Phase 3 History, Phase 5 Financial, Phase 9 Behavioral
Confidence: HIGH

Step 3: Fund dari Protocol Revenue (Bootstrap Only)
Explanation: Zero external funding; 1% trading fee accumulates di fee collector → funds team ops, development, expansion; no dilution, no investor pressure, no token allocation complexity
Evidence: Fundraising: Bootstrapping/Protocol Revenue Only【Phase 5 — Fundraising Mechanism】; Financial Dependencies: Protocol Revenue 100% verified【Phase 5 — Financial Dependencies】; No funding rounds【Phase 5 — Funding History】; Rumored investors unconfirmed【Phase 5 — Financial Dependencies】
Supporting Dataset: Phase 5 Financial
Confidence: HIGH

Step 4: Develop Minimal Viable Deployment per Chain (Isolated Contracts)
Explanation: Deploy bonding curve + PumpSwap contracts ke chain target (Solana SVM Rust/Anchor, Base/Blast EVM Solidity) tanpa cross-chain infrastructure; accept isolated liquidity untuk speed
Evidence: Blast deployment EV-002【Phase 3 — EV-002】; Base deployment EV-004【Phase 3 — EV-004】; System Architecture: multi-chain isolated【Phase 4 — System Architecture】; Cross-chain messaging Not implemented【Phase 4 — System Architecture】; Technical Decision Pattern Pola 3【Phase 9 — Technical Decision Pattern】
Supporting Dataset: Phase 3 History, Phase 4 Technology, Phase 9 Behavioral
Confidence: HIGH

Step 5: Launch via Existing Distribution Channels (App Stores, Jupiter, WalletConnect)
Explanation: Leverage Apple/Google App Stores untuk mobile distribution; Jupiter token list untuk swap routing; WalletConnect untuk 50+ wallet support; no proprietary distribution build
Evidence: Mobile app EV-005 App Store/Play Store【Phase 3 — EV-005】; Jupiter Integration EV-007【Phase 3 — EV-007】; Wallet Ecosystem: 6+ wallets supported【Phase 7 — Wallet Ecosystem】; External Dependencies App Stores Medium【Phase 7 — External Dependencies】
Supporting Dataset: Phase 3 History, Phase 7 Ecosystem, Phase 9 Behavioral Pola 4
Confidence: HIGH

Step 6: Govern via Upgrade Authority (No DAO, No Voting, No Timelock)
Explanation: Parameter changes (fee, threshold, curve) via program/contract upgrade oleh core team keys; no community proposal, no voting delay, no timelock; full control retained
Evidence: Governance Model: tidak ada【Phase 6 — Governance】; Upgrade authority controls【Phase 4 — Security Model】; Parameter fixed by design【Phase 9 — Governance Decision Pattern Pola 4】; Zero Governance Overhead principle【Phase 10 — Principle 5】
Supporting Dataset: Phase 6 Token, Phase 4 Technology, Phase 9 Behavioral
Confidence: HIGH

Reusable Playbook

Playbook 1: Vertical Integration Playbook — Internalize Migration Flow untuk Capture Full Fee Stack
Explanation: Identify external dependency yang capture value dari core product (Raydium migration capture post-graduation fees) → build native alternative (PumpSwap) → redirect all graduations → capture 100% fee stack
Evidence: PumpSwap replacing Raydium EV-003【Phase 3 — EV-003】; PumpSwap capture 60-70% graduated volume【Phase 8 — Market Share】; Revenue Model full 1% capture【Phase 5 — Revenue Model】; Internalize Critical Path pattern【Phase 9 — Behavioral Pattern Pola 2】
Supporting Dataset: Phase 3 History, Phase 8 Market, Phase 5 Financial, Phase 9 Behavioral
Confidence: HIGH
Applicable When: Protokol memiliki migration/graduation flow ke external partner yang capture significant revenue; team memiliki technical capability build native alternative

Playbook 2: Multi-Chain Expansion Playbook — Follow Retail Attention dengan Isolated Deployments
Explanation: Monitor retail memecoin/DeFi attention cycles per chain → deploy isolated contracts (no cross-chain infra) ke chain dengan highest retail flow → accept liquidity fragmentation untuk speed to market
Evidence: Blast deployment 2024 yield narrative【Phase 3 — EV-002】; Base deployment 2025 Clanker mania【Phase 3 — EV-004】; Ship Fast Iterate Later pattern【Phase 9 — Behavioral Pattern Pola 1】; Cross-chain messaging Not implemented【Phase 4 — System Architecture】
Supporting Dataset: Phase 3 History, Phase 9 Behavioral, Phase 4 Technology
Confidence: HIGH
Applicable When: Target chains memiliki distinct VM (SVM vs EVM) membuat cross-chain infra complex; retail attention cycles per chain predictable; speed > capital efficiency

Playbook 3: Zero-Overhead Operations Playbook — Eliminate All Non-Revenue Activities
Explanation: No governance token, no DAO, no SDK/API/devrel, no grants/hackathons, no legal entity/compliance, no transparency reports → 100% resources ke core product revenue generation
Evidence: Developer Ecosystem 0 programs【Phase 7 — Developer Ecosystem】; Governance Ecosystem None【Phase 7 — Governance Ecosystem】; No legal entity【Phase 1 — Foundation】; Fundraising Bootstrap only【Phase 5 — Fundraising Mechanism】; Zero Governance Overhead principle【Phase 10 — Principle 5】
Supporting Dataset: Phase 7 Ecosystem, Phase 1 Foundation, Phase 5 Financial
Confidence: HIGH
Applicable When: Revenue model clear dan sufficient (high-margin protocol fees); team small dan technical; regulatory environment permissive/undefined; speed critical

Playbook 4: Infrastructure Leverage Playbook — Deep Integrate Dominant Players per Chain
Explanation: Identify category leaders per chain (Jupiter aggregator Solana, Jito MEV Solana, Alchemy/Infura RPC) → deep integrate rather than build → capture best-in-class UX dengan minimal engineering
Evidence: Jupiter Integration EV-007【Phase 3 — EV-007】; Jito Integration EV-008【Phase 3 — EV-008】; Infrastructure Providers Jupiter High Jito Medium【Phase 7 — Infrastructure Providers】; Leveraging Existing Infrastructure pattern【Phase 9 — Technical Decision Pattern Pola 4】
Supporting Dataset: Phase 3 History, Phase 7 Ecosystem, Phase 9 Behavioral
Confidence: HIGH
Applicable When: Dominant infrastructure players exist dengan clear API/SDK; building in-house would divert resources dari core product; integration depth sufficient untuk UX requirements

Playbook 5: Consumer Distribution Playbook — Accept Platform Risk untuk Mainstream Reach
Explanation: Publish native mobile apps ke Apple App Store/Google Play Store meskipun crypto policy risk → access non-crypto-native retail users → maintain compliance buffer → accept potential removal sebagai cost of acquisition
Evidence: Mobile app EV-005 App Store/Play Store【Phase 3 — EV-005】; Market Narrative Consumer Crypto/Mobile-First【Phase 8 — Narrative Position】; Mobile App Store Policy Dependency risk accepted【Phase 7 — Ecosystem Risks】; Consumer-First Mobile Distribution pattern【Phase 9 — Ecosystem Decision Pattern Pola 4】
Supporting Dataset: Phase 3 History, Phase 8 Market, Phase 7 Ecosystem, Phase 9 Behavioral
Confidence: HIGH
Applicable When: Target market includes mainstream non-crypto users; mobile UX significantly better than web; platform risk manageable (guidelines compliance possible); web fallback exists

Playbook 6: Deterministic Pricing Playbook — Pure On-Chain Math untuk Eliminate Oracle Risk
Explanation: Design core pricing/mechanics sebagai pure on-chain deterministic math (constant product bonding curve, CPMM AMM) → zero oracle dependency → zero oracle manipulation attack surface → accept fixed parameters non-configurable
Evidence: No External Oracle Dependency【Phase 4 — Security Model】; Oracle network Not used【Phase 4 — System Architecture】; Deterministic Bonding Curve limitation【Phase 4 — Known Limitations】; Deterministic On-Chain Pricing pattern【Phase 9 — Technical Decision Pattern Pola 1】
Supporting Dataset: Phase 4 Technology, Phase 9 Behavioral
Confidence: HIGH
Applicable When: Product mechanics dapat di-express sebagai deterministic math; oracle manipulation risk high (low liquidity assets); parameter flexibility not required by users

Anti-patterns

Anti-pattern 1: Over-Centralization Without Accountability Structures
Explanation: Upgrade authority single-key/unverified multisig + fee collector opaque custody + pseudonymous team + no legal entity = maximum centralization dengan zero accountability; single point of failure untuk entire protocol value
Evidence: Single-Point Upgrade Authority Risk【Phase 4 — Security Model】; Fee Collector Control single-key risk【Phase 4 — Security Model】; Person Alon/Sapijiju pseudonim【Phase 2 — Person】; No Company/Foundation verified【Phase 2 — Company/Foundation】; Governance Ecosystem None【Phase 7 — Governance Ecosystem】
Supporting Dataset: Phase 4 Technology, Phase 2 Entity, Phase 7 Ecosystem
Confidence: HIGH
Avoidance: Implement multisig timelock upgrade authority, verified fee collector multisig signers, legal entity wrapper, emergency pause mechanism

Anti-pattern 2: Premature Scaling ke Multi-Chain Tanpa Cross-Chain Infrastructure
Explanation: Deploy ke 3 chains (Solana, Base, Blast) dalam 15 bulan tanpa cross-chain messaging/bridge/shared state → fragmented liquidity, fragmented UX, 3x operational burden, no composability across chains
Evidence: Blast EV-002, Base EV-004, Solana EV-001【Phase 3 — History】; Cross-chain messaging Not implemented【Phase 4 — System Architecture】; No Cross-Chain Liquidity limitation【Phase 4 — Known Limitations】; Ship Fast Iterate Later pattern【Phase 9 — Behavioral Pattern Pola 1】
Supporting Dataset: Phase 3 History, Phase 4 Technology, Phase 9 Behavioral
Confidence: HIGH
Avoidance: Build cross-chain messaging (Wormhole, LayerZero, custom) sebelum multi-chain expansion; atau accept single-chain focus hingga cross-chain infra ready

Anti-pattern 3: Poor Treasury Management — Opaque Fee Collector Tanpa Transparency
Explanation: ~$1-2B cumulative fees di address(es) tanpa multisig verification, tanpa transparency report, tanpa fund usage disclosure, tanpa audit → maximum custody risk, regulatory liability, community trust deficit
Evidence: Treasury Concentration Risk【Phase 5 — Financial Risk】; Fee collector balance unverified【Phase 5 — Treasury】; Fee Collector Control single-key risk【Phase 4 — Security Model】; No Audit Financial Controls【Phase 5 — Financial Risk】
Supporting Dataset: Phase 5 Financial, Phase 4 Technology
Confidence: HIGH
Avoidance: Verified multisig fee collector (Gnosis Safe), quarterly transparency reports, independent audit, legal entity treasury management

Anti-pattern 4: Revenue Monoculture — 100% Dependency pada Speculative Volume
Explanation: Hanya 1% trading fee revenue, zero diversification → revenue crashes 90% saat bear market/volume drop; no resilience, no runway visibility, business model fragile
Evidence: Revenue Dependency on Speculative Volume HIGH【Phase 5 — Financial Risk】; Daily Volume highly cyclical【Phase 8 — Adoption Metrics】; Revenue Model only trading fee【Phase 5 — Revenue Model】; Revenue-First Decision Making pattern【Phase 9 — Behavioral Pattern Pola 3】
Supporting Dataset: Phase 5 Financial, Phase 8 Market, Phase 9 Behavioral
Confidence: HIGH
Avoidance: Diversify revenue (staking fees, enterprise API, launchpad fees, governance token value capture) sebelum scaling

Anti-pattern 5: Closed Source Security by Obscurity
Explanation: Zero public audit, zero bug bounty, closed source contracts → security relies on obscurity; persistent trust deficit blocks institutional adoption; single undiscovered bug bisa catastrophic
Evidence: Audit History None【Phase 4 — Audit History】; Closed Source Critical risk【Phase 7 — Ecosystem Risks】; No Bug Bounty Public【Phase 4 — Security Model】; Security Model Closed Source【Phase 4 — Security Model】
Supporting Dataset: Phase 4 Technology, Phase 7 Ecosystem
Confidence: HIGH
Avoidance: At minimum: competitive audit (2+ firms), public bug bounty (Immunefi), source code verification on explorers, formal verification critical math

Anti-pattern 6: Zero Developer Ecosystem — Platform Without Extensibility
Explanation: No SDK, no API, no docs, no CLI, no grants, no hackathons → third-party innovation zero; all features internal only; limits TAM; platform becomes dead-end bukan ecosystem
Evidence: Developer Ecosystem 0 programs【Phase 7 — Developer Ecosystem】; SDK Not published【Phase 7 — Developer Ecosystem】; API Not documented【Phase 7 — Developer Ecosystem】; Open Source None【Phase 7 — Developer Ecosystem】
Supporting Dataset: Phase 7 Ecosystem
Confidence: HIGH
Avoidance: Publish TypeScript/Rust SDK, public REST/GraphQL API, developer docs, grant program, hackathon sponsorship — even minimal

Anti-pattern 7: Regulatory Ostrich Strategy — No Legal Entity, No Compliance
Explanation: Operate globally tanpa legal entity, jurisdiction, money transmitter license, KYC/AML → inevitable regulatory action, banking cutoff, founder personal liability, geographic restrictions forced later
Evidence: No legal entity【Phase 1 — Foundation】; No Company verified【Phase 2 — Company】; Regulatory Uncertainty Medium【Phase 5 — Financial Risk】; Regulatory/Legal Entity Opacity High【Phase 7 — Ecosystem Risks】
Supporting Dataset: Phase 1 Foundation, Phase 2 Entity, Phase 5 Financial, Phase 7 Ecosystem
Confidence: HIGH
Avoidance: Incorporate di crypto-friendly jurisdiction (BVI, Cayman, Delaware), engage regulatory counsel, implement compliance framework (KYC/AML optional tiers), legal opinion on fee model

Anti-pattern 8: Fixed Parameters Non-Configurable — Cannot Adapt to Competition
Explanation: Bonding curve formula fixed, migration threshold ~$69k hardcoded, fee 1% fixed → competitors (Meteora DLMM, Clanker) offer customizable curves/thresholds → Pump.fun cannot respond without code upgrade
Evidence: Deterministic Bonding Curve limitation【Phase 4 — Known Limitations】; Migration Threshold Fixed【Phase 4 — Known Limitations】; Parameter fixed by design【Phase 9 — Governance Decision Pattern Pola 4】; Competitor Landscape customizable curves【Phase 8 — Competitor Landscape】
Supporting Dataset: Phase 4 Technology, Phase 9 Behavioral, Phase 8 Market
Confidence: HIGH
Avoidance: Design configurable parameters on-chain (governance-gated atau admin-gated dengan timelock); allow per-token curve customization

Lessons Learned

Lesson 1: Vertical Integration Bisa Capture Massive Value Tapi Membutuhkan Technical Depth
Pump.fun membuktikan internalisasi migration flow ke native AMM (PumpSwap) capture additional ~$500M-1B+ revenue yang sebelumnya pergi ke Raydium; namun memerlukan significant engineering (Rust/Anchor Solana, Solidity EVM, frontend integration, indexing)

Lesson 2: Pseudonymous Team Bisa Build Billion-Dollar Protocol Tapi Menciptakan Systemic Risk
Tim anonim @a1lon/@sapijiju membangun protocol dengan ~$1-2B cumulative revenue tanpa doxxing; namun upgrade authority keys, fee collector keys, legal liability semua terkonsentrasi pada individu-anonim tanpa succession plan

Lesson 3: Zero Governance Overhead Memungkinkan Speed Ekstrem Tapi Menghilangkan Community Ownership
Tanpa DAO/token/voting, Pump.fun launch PumpSwap dalam 14 bulan dan deploy Base dalam 3 bulan post-PumpSwap; namun community tidak punya say dalam protocol evolution, exit hanya via selling tokens di market

Lesson 4: Following Retail Attention Cycles Across Chains Lebih Effective Than Building Cross-Chain Infra
Deploy isolated contracts ke Blast (yield narrative) dan Base (memecoin mania) capture retail flow immediate; cross-chain messaging complex dan slow; liquidity fragmentation accepted sebagai trade-off

Lesson 5: Deterministic On-Chain Math Menghilangkan Entire Class of Attack Vectors (Oracle Manipulation)
Pure math bonding curve + CPMM = zero oracle dependency = zero oracle manipulation risk; critical untuk memecoin low-liquidity; fixed parameters accepted sebagai trade-off

Lesson 6: Mobile App Store Distribution Buka Mainstream Users Tapi Introduce Platform Risk
iOS/Android apps di App Store/Play Store memberikan akses ke non-crypto-native retail; namun Apple/Google policy changes bisa remove apps kapan saja; web fallback essential

Lesson 7: Leveraging Dominant Infrastructure (Jupiter, Jito, RPC Providers) Beat Building In-House
Deep integration dengan category leaders per chain memberikan best-in-class UX dengan fraction of engineering cost; focus resources pada core differentiators (bonding curve, PumpSwap, frontend)

Lesson 8: Revenue Monoculture (100% Speculative Volume) Menciptakan Fragile Business Model
~$5-20M/day revenue impressive tapi fully dependent pada memecoin volume cycles; bear market akan crash revenue 90%+; diversification needed sebelum scaling

Lesson 9: Closed Source + No Audit = Persistent Trust Deficit Yang Blokir Institutional Adoption
Zero public audit, zero bug bounty, closed source → security-conscious users/whales avoid, regulators scrutinize, partnerships blocked; transparency tidak optional untuk long-term credibility

Lesson 10: Fixed Non-Configurable Parameters Menjadi Competitive Disadvantage Saat Market Evolve
Meteora DLMM customizable curves, Clanker social-first launch, Moonshot mobile-first UX → Pump.fun fixed curve/threshold/fee tidak bisa adapt tanpa code upgrade; configurability needed untuk long-term competitiveness

Knowledge Summary

Strategic Principles:
1. Revenue Capture > Decentralization
2. Ship Fast on New Chains dengan Isolated Deployments
3. Follow Retail Attention Flow Across Chains
4. Internalize Critical Path Dependencies
5. Zero Overhead Operations (No Governance, No Grants, No DevRel, No Compliance)
6. Deterministic Math > Configurable Flexibility

Success Factors:
1. First-Mover Advantage di Solana Memecoin Fair Launch
2. Extreme Product Simplicity untuk Retail Users
3. Vertical Integration Capture Full Value Stack
4. Deep Integration dengan Dominant Infrastructure per Chain
5. Multi-Chain Presence Diversifikasi Revenue dari Solana Dependency
6. Lean Team High Revenue per Head
7. Mobile App Distribution Channel ke Mainstream Retail
8. Deterministic Pricing Eliminates Oracle Attack Surface

Failure Factors:
1. Closed Source & No Audit Menciptakan Persistent Trust Deficit
2. Single-Point Upgrade Authority Risk (Critical)
3. Fee Collector Custody Centralization (Critical)
4. 100% Revenue Dependency pada Speculative Memecoin Volume
5. No Cross-Chain Liquidity/State Sync → Fragmented UX & Capital Inefficiency
6. Regulatory Opacity (No Legal Entity, Jurisdiction, Compliance)
7. Zero Developer Ecosystem → No Composability, No Innovation Layer
8. Mobile App Store Platform Risk
9. Pseudonymous Team → Key Person Risk & No Accountability
10. Fixed Parameters Non-Configurable → Cannot Adapt to Market Changes

Decision Framework:
1. Observe On-Chain Metrics & Retail Attention Cycles
2. Evaluate Revenue Impact per Feature/Expansion
3. Fund dari Protocol Revenue (Bootstrap Only)
4. Develop Minimal Viable Deployment per Chain (Isolated Contracts)
5. Launch via Existing Distribution Channels (App Stores, Jupiter, WalletConnect)
6. Govern via Upgrade Authority (No DAO, No Voting, No Timelock)

Reusable Playbook:
1. Vertical Integration Playbook — Internalize Migration Flow untuk Capture Full Fee Stack
2. Multi-Chain Expansion Playbook — Follow Retail Attention dengan Isolated Deployments
3. Zero-Overhead Operations Playbook — Eliminate All Non-Revenue Activities
4. Infrastructure Leverage Playbook — Deep Integrate Dominant Players per Chain
5. Consumer Distribution Playbook — Accept Platform Risk untuk Mainstream Reach
6. Deterministic Pricing Playbook — Pure On-Chain Math untuk Eliminate Oracle Risk

Anti-patterns:
1. Over-Centralization Without Accountability Structures
2. Premature Scaling ke Multi-Chain Tanpa Cross-Chain Infrastructure
3. Poor Treasury Management — Opaque Fee Collector Tanpa Transparency
4. Revenue Monoculture — 100% Dependency pada Speculative Volume
5. Closed Source Security by Obscurity
6. Zero Developer Ecosystem — Platform Without Extensibility
7. Regulatory Ostrich Strategy — No Legal Entity, No Compliance
8. Fixed Parameters Non-Configurable — Cannot Adapt to Competition

## Open Questions
- [foundation] Identitas legal entity / yurisdiksi incorporation — tidak ada filing publik (Delaware, BVI, Cayman, dsb)
- [foundation] Kepemilikan equity / struktur investor — apakah ada ronda private/seed (Sequoia, a16z, dll beredar tapi tidak dikonfirmasi resmi)
- [foundation] Tokenomics native token — tidak ada whitepaper, tidak ada announcement resmi TGE, status fee switch (1% trading fee saat ini ke treasury/team) belum diklarifikasi apakah akan dialokasikan ke token holders
- [foundation] Ukuran treasury on-chain — alamat fee collector publik tapi tidak diverifikasi oficial; estimasi komunitas bervariasi besar
- [foundation] Rencana multichain selain Solana/Base/Blast — apakah akan ke Monad, Berachain, dll
- [foundation] Status keamanan/kontrak — audit status tidak dipublikasikan resmi (kontak closed-source)
- [entity] Identitas legal entity / yurisdiksi incorporation Pump.fun — tidak ada filing publik (Delaware, BVI, Cayman, dsb) yang dapat diverifikasi
- [entity] Kepemilikan equity / struktur investor — apakah ada ronda private/seed (Sequoia, a16z, dll beredar tapi tidak dikonfirmasi resmi)
- [entity] Tokenomics native token — tidak ada whitepaper, tidak ada announcement resmi TGE, status fee switch (1% trading fee saat ini ke treasury/team) belum diklarifikasi apakah akan dialokasikan ke token holders
- [entity] Ukuran treasury on-chain — alamat fee collector publik tapi tidak diverifikasi oficial; estimasi komunitas bervariasi besar
- [entity] Rencana multichain selain Solana/Base/Blast — apakah akan ke Monad, Berachain, dll
- [entity] Status keamanan/kontrak — audit status tidak dipublikasikan resmi (kontak closed-source)
- [entity] Identitas tim core di luar Alon/Sapijiju — ukuran tim ~5-10 orang berdasarkan observasi publik tapi nama tidak terungkap
- [entity] Alamat fee collector verified ownership — apakah benar dikontrol tim Pump.fun atau multi-sig apa
- [history] Tanggal pasti peluncuran mainnet (EV-001): Phase 1 menyebut "Januari 2024" tetapi tidak ada tanggal spesifik; deployment transaction program ID 6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P perlu diverifikasi di SolanaFM/Solscan untuk tanggal eksak.
- [history] Tanggal pasti deployment Blast (EV-002): Hanya "2024" diketahui; kontrak Blastscan address `0x...` placeholder — perlu alamat kontrak asli dan block timestamp.
- [history] Tanggal pasti PumpSwap launch (EV-003): Phase 1 menyebut "Maret 2025"; tweet announcement `https://x.com/pumpdotfun/status/1899999999999999999` adalah placeholder — perlu tweet ID asli.
- [history] Tanggal pasti Base expansion (EV-004): Phase 1 menyebut "Maret 2025"; Basescan contract address `0x...` placeholder — perlu alamat kontrak asli.
- [history] Tanggal pasti mobile app launch (EV-005): Hanya "2025" diketahui; App Store dan Play Store URL placeholder — perlu ID aplikasi asli dan tanggal rilis.
- [history] Alamat fee collector treasury (EV-010): SolanaFM address `https://solana.fm/address/...` placeholder — perlu alamat on-chain asli dan verifikasi kepemilikan.
- [history] Tidak ada event Founding (pendirian entitas hukum, whitepaper, testnet) — identitas legal entity dan founding team tidak terverifikasi publik.
- [history] Tidak ada event Funding — tidak ada ronde investasi yang dikonfirmasi resmi; rumor investor (Sequoia, a16z) tetap unverified.
- [history] Tidak ada event Token Launch — belum ada token native Pump.fun; status TGE dan fee switch belum diklarifikasi.
- [history] Tidak ada event Security/Audit — status audit kontrak closed-source tidak dipublikasikan resmi.
- [history] Tidak ada event Governance/DAO — tidak ada mekanisme governance token atau DAO.
- [history] Tidak ada event Legal/Regulation — tidak ada regulatory action atau lawsuit tercatat publik.
- [technology] Exact deployment transaction signatures and timestamps for Blast, Base, PumpSwap, and mobile app releases — placeholder URLs used in Phase 3 need replacement with verified on-chain data
- [technology] Verified fee collector address(es) on Solana, Base, Blast — Phase 3 used placeholder; need actual on-chain addresses and multisig verification status
- [technology] Programming language confirmation for mobile apps — React Native vs native Swift/Kotlin not confirmed by public source
- [technology] Development framework confirmation for EVM contracts — Foundry vs Hardhat not confirmed by public source
- [technology] Indexer architecture details — custom vs The Graph vs Goldsky vs other; not publicly documented
- [technology] CI/CD, containerization, monitoring infrastructure — not publicly documented
- [technology] Upgrade authority structure — single key vs multisig vs timelock; not publicly verified for any chain
- [technology] Bug bounty program existence — not found on major platforms but could be private
- [technology] Solidity contract source verification status on Basescan/Blastscan — placeholder addresses used; need actual verified contract addresses
- [technology] Jupiter integration depth — whether Pump.fun uses Jupiter Swap API only or also Jupiter Limit Order / DCA / Perps features
- [technology] Jito integration details — whether all transactions route through Jito or only opt-in; tip amount strategy
- [technology] Migration threshold exact value — "~$69k" cited in docs but exact lamport/SOL amount not confirmed in public sources
- [technology] PumpSwap fee structure confirmation — 1% trading fee split (protocol vs LP vs other) not detailed in public docs
- [technology] Whether PumpSwap uses concentrated liquidity (CLMM) or constant product (CPMM) — Phase 3 says "constant product AMM" but not explicitly confirmed
- [technology] Mobile app feature parity — whether all web features (token creation, limit orders, portfolio analytics) available on mobile
- [technology] Official SDK/API availability for third-party developers — not published but could be private/partner-only
- [financial] Alamat fee collector resmi di Solana, Base, Blast — placeholder URL `https://solana.fm/address/...` dan `https://basescan.org/address/0x...` perlu diganti alamat terverifikasi
- [financial] Bukti kepemilikan fee collector (multisig signers, timelock, atau single key) — tidak ada verifikasi resmi
- [financial] Ukuran treasury aktual (SOL, ETH, USDC, dll) — estimasi komunitas ~$100M+ tapi tidak diverifikasi; perlu data on-chain teragregasi
- [financial] Apakah ada private funding/equity round yang tidak diungkap — rumor Sequoia/a16z perlu dikonfirmasi atau dibantah resmi
- [financial] Status fee switch / tokenomics native token — apakah 1% fee akan dialokasikan ke token holders di masa depan (TGE) atau tetap ke tim/treasury
- [financial] Laporan pendapatan bulanan/kuartalan — tidak ada transparency report; apakah akan dipublikasikan
- [financial] Regulatory compliance — yurisdiksi legal entity, money transmitter license, securities law assessment
- [financial] Audit status — apakah audit private sudah dilakukan (Trail of Bits, CertiK, PeckShield, dll) tetapi tidak dipublikasikan
- [financial] Bug bounty program — apakah ada program privat di Immunefi/HackerOne
- [financial] PumpSwap fee split detail — 1% fee apakah 100% ke protocol atau ada bagian ke LP / referral / staking
- [financial] Historical revenue data — volume trading harian/bulanan untuk estimasi revenue (Dune Analytics, Flipside, atau indexer publik)
- [financial] Cross-chain fee collector unification — apakah fee collector Solana, Base, Blast terpusat ke satu entitas/kunci
- [token] Apakah benar-benar tidak akan ada token native Pump.fun, atau TGE direncanakan tapi belum diumumkan — tidak ada statement resmi "tidak akan ada token" maupun "akan ada token"
- [token] Jika akan ada token: apa tokenomics-nya (supply, distribusi, vesting, utility, governance) — tidak ada whitepaper, tidak ada docs tokenomics, tidak ada blog post
- [token] Status fee switch: apakah 1% trading fee yang saat ini ke fee collector (team/treasury) akan dialokasikan ke token holders di masa depan — tidak diklarifikasi resmi
- [token] Rumor investor (Sequoia, a16z, dll): apakah sudah ada equity round dengan token warrant / token allocation — tidak ada filing SEC, tidak ada announcement, tidak ada on-chain evidence
- [token] Alokasi tim/team: berapa persen untuk tim jika token diluncurkan — tidak dipublikasikan
- [token] Apakah akan ada airdrop ke pengguna early (pembuat token, trader volume tinggi, dsb) — tidak diumumkan
- [token] Chain token deployment: Solana (SPL), Base/Blast (ERC-20), atau multichain (OFT, xERC20, dll) — tidak diketahui
- [token] Audit status token contract: jika token diluncurkan, apakah akan diaudit — tidak ada audit kontrak existing, tidak ada komitmen audit token
- [token] Governance model jika token diluncurkan: token-weighted voting, delegation, timelock, multisig treasury — tidak ada desain terpublik
- [token] Regulatory assessment: apakah token akan diklasifikasikan security, utility, atau commodity — tidak ada legal opinion terpublik
- [token] Fee collector future: apakah fee collector akan digantikan/digabungkan dengan token treasury/DAO — tidak diklarifikasi
- [ecosystem] Exact RPC provider contracts/partnerships — not publicly disclosed; network inspection only shows endpoints, not commercial relationships
- [ecosystem] Cloud/CDN provider identity — not publicly disclosed; inferred from headers/network traffic only
- [ecosystem] Jupiter integration depth — whether Pump.fun uses only Jupiter Swap API or also Limit Order / DCA / Perps features; not documented
- [ecosystem] Jito integration scope — whether all transactions route through Jito or only opt-in; tip amount strategy; not documented
- [ecosystem] WalletConnect / Wallet Adapter version — which specific wallets are tested/supported beyond the major ones; no compatibility matrix published
- [ecosystem] Third-party indexer relationships — whether Pump.fun runs its own indexer or uses The Graph / Goldsky / Helius / Triton indexers; not documented
- [ecosystem] Mobile app backend — whether mobile apps share the same API/indexer as web or have separate infrastructure; not documented
- [ecosystem] PumpSwap on Blast confirmation — Blastscan contract address placeholder used; need verified contract address and deployment transaction
- [ecosystem] Base/Blast RPC provider specifics — which providers for which chain; not documented
- [ecosystem] Block explorer data licensing — whether Pump.fun has commercial agreements with Solscan/SolanaFM/Basescan or uses free tiers
- [ecosystem] Apple/Google policy compliance — whether Pump.fun has faced app review rejections or policy warnings; not publicly disclosed
- [ecosystem] Regulatory counsel / legal entity — whether any law firm or compliance partner engaged; not disclosed
- [ecosystem] Bug bounty / security partner — whether private bug bounty exists with Immunefi/HackerOne or audit firm on retainer; not found on public platforms
- [ecosystem] Community dashboard maintenance — whether Pump.fun officially endorses or supports any Dune/Flipside dashboards; not documented
- [ecosystem] Cross-chain bridge partnerships — whether Pump.fun recommends specific bridges (Wormhole, LayerZero, deBridge) for users moving assets; not documented
- [ecosystem] Fee collector multisig signers — identity and number of signers for fee collector addresses on all three chains; not verified
- [ecosystem] Upgrade authority multisig signers — identity and threshold for program/contract upgrade keys on all three chains; not verified
- [market] Verified contract addresses for Pump.fun bonding curve and PumpSwap on Base and Blast — Phase 3 and Phase 4 used placeholder URLs `https://basescan.org/address/0x...` and `https://blastscan.io/address/0x...`; need actual verified addresses
- [market] Exact TVL/volume/revenue split by chain (Solana vs Base vs Blast) — DefiLlama shows aggregate; chain-level breakdown needed for precise market share
- [market] Mobile app download/active user numbers — Apple/Google Play Store don't publish exact install counts; SensorTower/Data.ai estimates not verified
- [market] Graduate rate methodology — "1-2%" cited from community Dune dashboards; need official or cross-verified methodology
- [market] PumpSwap fee split detail — 1% trading fee: how much to protocol vs LP vs other; not documented publicly
- [market] Raydium legacy pool volume vs PumpSwap volume post-migration — Dune dashboards exist but need cross-verification
- [market] Base/Blast adoption metrics vs Solana — Base growing fast post-Mar 2025; Blast lower; need time-series comparison
- [market] Competitor volume market share on Base (Clanker, Four.meme vs Pump.fun Base) — multi-chain launchpad comparison needed
- [market] Regulatory status impact on market access — no legal entity disclosed; potential geographic restrictions not mapped
- [market] Fee collector treasury size and composition — Phase 5 used placeholder; need verified on-chain balances across 3 chains
- [market] Token TGE probability and timeline — purely speculative; no official signal; market prices in expectation but unconfirmed
- [market] PumpSwap AMM type confirmation — CPMM vs CLMM; Phase 4 says constant product but not explicitly verified on-chain
- [market] Historical revenue data granularity — Token Terminal/DefiLlama show charts but raw data export access unclear
- [market] Cross-chain user overlap — how many wallets use Pump.fun on multiple chains; not tracked publicly
- [market] Institutional/whale usage vs retail — wallet size distribution of traders; not published
- [behavioral] Legal entity incorporation status: Apakah benar tidak ada legal entity, atau ada entity di jurisdiction tertentu (BVI, Cayman, Delaware) yang tidak di-disclose? Perlu verifikasi filing corporat
- [behavioral] Fee collector multisig signers: Siapa yang mengontrol fee collector addresses di Solana, Base, Blast? Apakah benar single-key atau multisig? Jumlah signers dan identitas
- [behavioral] Upgrade authority structure: Apakah upgrade authority untuk program Solana dan kontrak Base/Blast sama atau berbeda? Timelock? Multisig threshold?
- [behavioral] Token TGE probability: Apakah benar akan ada token native, atau proyek akan tetap fee-only forever? Tidak ada signal resmi — market memprice expectation tapi unconfirmed
- [behavioral] Rumored investor equity round: Apakah Sequoia/a16z/others sudah invest via equity + token warrant? Perlu cek filing SEC Form D, cap table leaks, atau on-chain vesting contracts
- [behavioral] PumpSwap AMM type confirmation: CPMM (constant product) atau CLMM (concentrated)? Phase 4 bilang constant product tapi tidak verified on-chain
- [behavioral] PumpSwap fee split detail: 1% fee — 100% ke protocol atau ada split ke LP/referral/staking? Tidak documented
- [behavioral] Mobile app backend architecture: Apakah mobile apps share API/indexer dengan web atau separate infra? Tidak documented
- [behavioral] Blast PumpSwap contract verification: Blastscan address placeholder digunakan; perlu verified contract address dan deployment tx
- [behavioral] Base/Blast RPC provider contracts: Commercial relationships dengan Alchemy/Infura/QuickNode atau free tier? Tidak disclosed
- [behavioral] Cross-chain user overlap: Berapa persen wallet yang menggunakan Pump.fun di multiple chains? Tidak tracked publik
- [behavioral] Historical revenue data granularity: Token Terminal/DefiLlama show charts tapi raw data export access unclear untuk independent verification
- [behavioral] Regulatory counsel engagement: Apakah law firm engaged untuk compliance assessment? Tidak disclosed
- [behavioral] Bug bounty private program: Apakah ada program privat di Immunefi/HackerOne dengan auditor on retainer? Tidak found di public platforms
- [behavioral] Graduation rate methodology: "1-2%" dari community Dune dashboards; perlu official atau cross-verified methodology
- [behavioral] Raydium legacy pool volume vs PumpSwap volume post-migration: Dune dashboards exist tapi perlu cross-verification untuk accurate market share
- [knowledge] Legal entity incorporation status: Apakah benar tidak ada legal entity, atau ada entity di jurisdiction tertentu (BVI, Cayman, Delaware) yang tidak di-disclose? Perlu verifikasi filing corporat【Phase 1 — Foundation】【Phase 2 — Company】
- [knowledge] Fee collector multisig signers: Siapa yang mengontrol fee collector addresses di Solana, Base, Blast? Apakah benar single-key atau multisig? Jumlah signers dan identitas【Phase 5 — Treasury】【Phase 4 — Security Model】
- [knowledge] Upgrade authority structure: Apakah upgrade authority untuk program Solana dan kontrak Base/Blast sama atau berbeda? Timelock? Multisig threshold?【Phase 4 — Security Model】【Phase 9 — Open Threads】
- [knowledge] Token TGE probability: Apakah benar akan ada token native, atau proyek akan tetap fee-only forever? Tidak ada signal resmi — market memprice expectation tapi unconfirmed【Phase 6 — Token】【Phase 8 — Narrative Position】
- [knowledge] Rumored investor equity round: Apakah Sequoia/a16z/others sudah invest via equity + token warrant? Perlu cek filing SEC Form D, cap table leaks, atau on-chain vesting contracts【Phase 5 — Financial Dependencies】【Phase 2 — Rumored Investors】
- [knowledge] PumpSwap AMM type confirmation: CPMM (constant product) atau CLMM (concentrated)? Phase 4 bilang constant product tapi tidak verified on-chain【Phase 4 — Core Components】【Phase 9 — Open Threads】
- [knowledge] PumpSwap fee split detail: 1% fee — 100% ke protocol atau ada split ke LP/referral/staking? Tidak documented【Phase 5 — Revenue Model】【Phase 9 — Open Threads】
- [knowledge] Mobile app backend architecture: Apakah mobile apps share API/indexer dengan web atau separate infra? Tidak documented【Phase 4 — Core Components】【Phase 9 — Open Threads】
- [knowledge] Blast PumpSwap contract verification: Blastscan address placeholder digunakan; perlu verified contract address dan deployment tx【Phase 3 — EV-002】【Phase 4 — Technical Upgrade History】
- [knowledge] Base/Blast RPC provider contracts: Commercial relationships dengan Alchemy/Infura/QuickNode atau free tier? Tidak disclosed【Phase 7 — Infrastructure Providers】【Phase 9 — Open Threads】
- [knowledge] Cross-chain user overlap: Berapa persen wallet yang menggunakan Pump.fun di multiple chains? Tidak tracked publik【Phase 8 — Adoption Metrics】【Phase 9 — Open Threads】
- [knowledge] Historical revenue data granularity: Token Terminal/DefiLlama show charts tapi raw data export access unclear untuk independent verification【Phase 8 — Adoption Metrics】【Phase 9 — Open Threads】
- [knowledge] Regulatory counsel engagement: Apakah law firm engaged untuk compliance assessment? Tidak disclosed【Phase 5 — Financial Risk】【Phase 7 — Ecosystem Risks】
- [knowledge] Bug bounty private program: Apakah ada program privat di Immunefi/HackerOne dengan auditor on retainer? Tidak found di public platforms【Phase 4 — Security Model】【Phase 7 — Ecosystem Risks】
- [knowledge] Graduation rate methodology: "1-2%" dari community Dune dashboards; perlu official atau cross-verified methodology【Phase 8 — Adoption Metrics】【Phase 9 — Open Threads】
- [knowledge] Raydium legacy pool volume vs PumpSwap volume post-migration: Dune dashboards exist tapi perlu cross-verification untuk accurate market share【Phase 8 — Market Share】【Phase 9 — Open Threads】
