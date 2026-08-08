# Hyperliquid — Deep Case Study (Phased)

**CIF Dataset — Deep Dossier · Tier: Deep (anchor project)**
**Source:** Deep Research (DeepSeek), Format v3 Dependency Pipeline (10/11 phases: foundation, entity, history, technology, financial, token, ecosystem, market, behavioral, knowledge). **Auto-assembled** by `tools/ingest.py` (deterministic, no LLM, strict data_project/ contract) — each phase extracted and concatenated in dependency order per `docs/Protocol/Deep-Research-Brief.md`; the reasoning is the source reports'.
**Raw sources archived:** doc_backup/deep/Hyperliquid_foundation_2026-08.docx, doc_backup/deep/Hyperliquid_entity_2026-08.docx, doc_backup/deep/Hyperliquid_history_2026-08.docx, doc_backup/deep/Hyperliquid_technology_2026-08.docx, doc_backup/deep/Hyperliquid_financial_2026-08.docx, doc_backup/deep/Hyperliquid_token_2026-08.docx, doc_backup/deep/Hyperliquid_ecosystem_2026-08.docx, doc_backup/deep/Hyperliquid_market_2026-08.docx, doc_backup/deep/Hyperliquid_behavioral_2026-08.docx, doc_backup/deep/Hyperliquid_knowledge_2026-08.docx.
**Phases not run:** conflict.

> Faithful concatenation of phase outputs — no fabrication, no distillation beyond what the closing phase (Conflict Resolution / Validation) itself states. Consider a periodic QC pass.

---
## Foundation Intelligence
_ref: `docs/Ontology/Identity.md`, `docs/Ontology/Team.md`_

PROJECT: Hyperliquid
Official Name: Hyperliquid (HIGH) [Official Website, https://hyperliquid.xyz]
Symbol: HYPE (HIGH) [CoinGecko, https://www.coingecko.com/en/coins/hyperliquid]
Category: Layer 1 Blockchain / Decentralized Exchange (Perpetual Futures & Spot) / On-chain Order Book (CLOB) (HIGH) [Documentation, https://hyperliquid.gitbook.io/hyperliquid-docs]
Founding Entity: Hyperliquid Labs (British Virgin Islands) (MEDIUM) [Messari Report, https://messari.io/report/hyperliquid-deep-dive; The Block Article, https://www.theblock.co/post/298123/hyperliquid-labs-raises-funding]
Founders: Jeff Yan (Co-founder, CEO); iliensinc (Co-founder, CTO — pseudonim) (HIGH) [Official Blog "Introducing Hyperliquid", https://hyperliquid.xyz/blog/introducing-hyperliquid; The Block Interview, https://www.theblock.co/post/298123/hyperliquid-labs-raises-funding]
Core Team: ~20-30 insinyur & peneliti (tidak diungkap penuh nama publik) (MEDIUM) [Messari Report, https://messari.io/report/hyperliquid-deep-dive; LinkedIn "Hyperliquid Labs" employee count]
Country: British Virgin Islands (entitas hukum); Tim terdistribusi global (HIGH) [Messari Report, https://messari.io/report/hyperliquid-deep-dive]
Launch Date - Testnet: Q4 2022 (testnet internal/closed); Maret 2023 (testnet publik berincentiv "Hyperliquid Testnet") (MEDIUM) [Official Blog "Testnet Launch", https://hyperliquid.xyz/blog/testnet-launch; DefiLlama "Hyperliquid" chain page, https://defillama.com/chain/Hyperliquid]
Launch Date - Mainnet: 14 Mei 2023 (Mainnet Perpetual DEX); Oktober 2023 (Spot DEX); November 2024 (HyperEVM testnet) (HIGH) [Official Blog "Mainnet Launch", https://hyperliquid.xyz/blog/mainnet-launch; Official Blog "Spot Launch", https://hyperliquid.xyz/blog/spot-launch; Official Blog "HyperEVM", https://hyperliquid.xyz/blog/hyperevm]
Launch Date - TGE: 29 November 2024 (Token Generation Event HYPE) (HIGH) [Official Blog "HYPE Genesis", https://hyperliquid.xyz/blog/hype-genesis; CoinGecko HYPE listing date]
Main Products: Hyperliquid Perpetual DEX (CLOB on-chain); Hyperliquid Spot DEX; Hyperliquid L1 (Layer 1 custom, HyperBFT consensus); HyperEVM (EVM execution environment di atas Hyperliquid L1); Hyperliquid Bridge (native bridge ke Arbitrum/Ethereum) (HIGH) [Documentation "Products", https://hyperliquid.gitbook.io/hyperliquid-docs/products/overview]
Official Website: https://hyperliquid.xyz (HIGH) [Verifikasi langsung]
Repository: https://github.com/hyperliquid-dex (HIGH) [GitHub Org]
Documentation: https://hyperliquid.gitbook.io/hyperliquid-docs (HIGH) [GitBook]
Social - X/Twitter: @HyperliquidX (HIGH) [X Profile]
Social - Discord: https://discord.gg/hyperliquid (HIGH) [Website Footer]
Social - Telegram: @hyperliquidofficial (MEDIUM) [Website Footer / X Bio]
Block Explorer: https://hypurrscan.io (utama); https://explorer.hyperliquid.xyz (resmi) (HIGH) [Documentation "Explorers", https://hyperliquid.gitbook.io/hyperliquid-docs/ecosystem/explorers]
Token Contract: Native HYPE di Hyperliquid L1 (bukan ERC-20); Wrapped HYPE (WHYPE) di Arbitrum: 0xC5b... (tidak diverifikasi kontrak resmi Ethereum mainnet saat TGE) (MEDIUM) [Hypurrscan Native Token Page; Official Bridge UI]
Chain(s): Hyperliquid L1 (Layer 1 sovereign, HyperBFT consensus); HyperEVM (EVM-compatible execution layer di atas L1) (HIGH) [Documentation "Architecture", https://hyperliquid.gitbook.io/hyperliquid-docs/architecture/overview]
Ecosystem: Hyperliquid Ecosystem (Perp DEX, Spot DEX, HyperEVM dApps, Builder Grants, HYPE Staking/Governance) (HIGH) [Official Blog "Ecosystem Fund", https://hyperliquid.xyz/blog/ecosystem-fund; Documentation "Ecosystem"]

## Entity Intelligence
_ref: `docs/Ontology/Relationships.md` (entity graph)_

PROJECT: Hyperliquid

Entity: Hyperliquid Labs
Type: Company
Relationship: Entitas pendiri dan pengembang inti yang membangun Hyperliquid L1, Hyperliquid DEX (Perpetual & Spot), HyperEVM, serta mengelola ekosistem Hyperliquid (HIGH)
Period: 2022–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Messari Report, https://messari.io/report/hyperliquid-deep-dive]; (HIGH) [The Block Article, https://www.theblock.co/post/298123/hyperliquid-labs-raises-funding]; (HIGH) [Official Blog Introducing Hyperliquid, https://hyperliquid.xyz/blog/introducing-hyperliquid]
---
Entity: Jeff Yan
Type: Person
Relationship: Co-founder dan CEO Hyperliquid Labs, mengarahkan visi strategis dan pengembangan produk Hyperliquid (HIGH)
Period: 2022–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Official Blog Introducing Hyperliquid, https://hyperliquid.xyz/blog/introducing-hyperliquid]; (HIGH) [The Block Interview, https://www.theblock.co/post/298123/hyperliquid-labs-raises-funding]
---
Entity: iliensinc
Type: Person
Relationship: Co-founder dan CTO Hyperliquid Labs (pseudonim), memimpin arsitektur teknis dan konsensus HyperBFT (HIGH)
Period: 2022–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Official Blog Introducing Hyperliquid, https://hyperliquid.xyz/blog/introducing-hyperliquid]; (HIGH) [The Block Interview, https://www.theblock.co/post/298123/hyperliquid-labs-raises-funding]
---
Entity: Hyperliquid L1
Type: Organization
Relationship: Layer 1 blockchain sovereign dengan konsensus HyperBFT, lapisan settlement dan execution untuk seluruh ekosistem Hyperliquid (HIGH)
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Documentation Architecture, https://hyperliquid.gitbook.io/hyperliquid-docs/architecture/overview]; (HIGH) [Official Blog Mainnet Launch, https://hyperliquid.xyz/blog/mainnet-launch]; (HIGH) [DefiLlama Chain Page, https://defillama.com/chain/Hyperliquid]
---
Entity: Hyperliquid Perpetual DEX
Type: Protocol
Relationship: Decentralized perpetual futures exchange on-chain dengan CLOB (Central Limit Order Book) native di Hyperliquid L1, produk utama perdagangan perp (HIGH)
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Documentation Products, https://hyperliquid.gitbook.io/hyperliquid-docs/products/overview]; (HIGH) [Official Blog Mainnet Launch, https://hyperliquid.xyz/blog/mainnet-launch]
---
Entity: Hyperliquid Spot DEX
Type: Protocol
Relationship: Decentralized spot exchange on-chain dengan CLOB native di Hyperliquid L1, meluncur Oktober 2023 (HIGH)
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Documentation Products, https://hyperliquid.gitbook.io/hyperliquid-docs/products/overview]; (HIGH) [Official Blog Spot Launch, https://hyperliquid.xyz/blog/spot-launch]
---
Entity: HyperEVM
Type: Protocol
Relationship: Lingkungan eksekusi EVM-compatible di atas Hyperliquid L1, memungkinkan deployment smart contract Ethereum (HIGH)
Period: 2024–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Official Blog HyperEVM, https://hyperliquid.xyz/blog/hyperevm]; (HIGH) [Documentation Architecture, https://hyperliquid.gitbook.io/hyperliquid-docs/architecture/overview]
---
Entity: Hyperliquid Foundation
Type: Foundation
Relationship: Entitas governance dan pengelola ekosistem Hyperliquid (jika ada), terpisah dari Hyperliquid Labs (MEDIUM)
Period: 2024–sekarang
Exposure Type: unknown
Evidence: (LOW) [Open Thread Phase 1 Foundation, https://hyperliquid.xyz/blog/hype-genesis]; (MEDIUM) [Official Blog HYPE Genesis, https://hyperliquid.xyz/blog/hype-genesis]
---
Entity: Variant Fund
Type: Investor
Relationship: Investor venture capital yang berpartisipasi dalam ronde pendanaan Hyperliquid Labs (MEDIUM)
Period: 2023–sekarang
Exposure Type: financial-collateral
Evidence: (MEDIUM) [The Block Article Funding Round, https://www.theblock.co/post/298123/hyperliquid-labs-raises-funding]
---
Entity: Delphi Digital
Type: Investor
Relationship: Investor venture capital dan penasihat riset yang berpartisipasi dalam ronde pendanaan Hyperliquid Labs (MEDIUM)
Period: 2023–sekarang
Exposure Type: financial-collateral
Evidence: (MEDIUM) [The Block Article Funding Round, https://www.theblock.co/post/298123/hyperliquid-labs-raises-funding]
---
Entity: Hack VC
Type: Investor
Relationship: Investor venture capital yang berpartisipasi dalam ronde pendanaan Hyperliquid Labs (MEDIUM)
Period: 2023–sekarang
Exposure Type: financial-collateral
Evidence: (MEDIUM) [The Block Article Funding Round, https://www.theblock.co/post/298123/hyperliquid-labs-raises-funding]
---
Entity: Susquehanna International Group (SIG)
Type: Organization
Relationship: Market maker dan penyedia likuiditas institusional yang beroperasi di Hyperliquid Perpetual DEX (MEDIUM)
Period: 2023–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [The Block Article Funding Round, https://www.theblock.co/post/298123/hyperliquid-labs-raises-funding]
---
Entity: GSR Markets
Type: Organization
Relationship: Market maker dan penyedia likuiditas institusional yang beroperasi di Hyperliquid Perpetual DEX (MEDIUM)
Period: 2023–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [The Block Article Funding Round, https://www.theblock.co/post/298123/hyperliquid-labs-raises-funding]
---
Entity: Winter

## Historical Intelligence
_ref: `docs/Ontology/DecisionEvent.md` (factual spine — enriched later by Behavioral)_

PROJECT: Hyperliquid

Event ID

EV-001

Date

2022

Event Name

Pendirian Hyperliquid Labs

Event Type

Founding

Description

Hyperliquid Labs didirikan oleh Jeff Yan dan iliensinc untuk membangun Layer 1 blockchain custom dengan konsensus HyperBFT dan DEX perpetual on-chain dengan CLOB native.

Participants

Hyperliquid Labs, Jeff Yan, iliensinc

Location

British Virgin Islands

Status

Completed

Immediate Result

Entitas hukum pendiri terbentuk; pengembangan arsitektur Hyperliquid L1 dan HyperBFT dimulai.

Sources

https://hyperliquid.xyz/blog/introducing-hyperliquid (HIGH) [Official Blog Introducing Hyperliquid]; https://www.theblock.co/post/298123/hyperliquid-labs-raises-funding (MEDIUM) [The Block Article]; https://messari.io/report/hyperliquid-deep-dive (HIGH) [Messari Report]

---

Event ID

EV-002

Date

2022-Q4

Event Name

Testnet Internal/Tertutup Hyperliquid

Event Type

Launch

Description

Hyperliquid meluncurkan testnet internal/tertutup untuk validasi arsitektur HyperBFT dan CLOB on-chain sebelum testnet publik.

Participants

Hyperliquid Labs

Location

Testnet internal

Status

Completed

Immediate Result

Validasi teknis konsensus HyperBFT dan matching engine CLOB on-chain.

Sources

https://hyperliquid.xyz/blog/testnet-launch (MEDIUM) [Official Blog Testnet Launch]; https://defillama.com/chain/Hyperliquid (MEDIUM) [DefiLlama Chain Page]; https://messari.io/report/hyperliquid-deep-dive (HIGH) [Messari Report]

---

Event ID

EV-003

Date

2023-03

Event Name

Testnet Publik Berincentiv Hyperliquid

Event Type

Launch

Description

Hyperliquid meluncurkan testnet publik berincentiv ("Hyperliquid Testnet") mengundang pengguna untuk menguji perpetual DEX dan CLOB on-chain dengan reward poin/airdrop di masa depan.

Participants

Hyperliquid Labs

Location

Testnet publik

Status

Completed

Immediate Result

Onboarding komunitas awal; pengujian beban matching engine dan konsensus HyperBFT dalam kondisi nyata.

Sources

https://hyperliquid.xyz/blog/testnet-launch (HIGH) [Official Blog Testnet Launch]; https://defillama.com/chain/Hyperliquid (MEDIUM) [DefiLlama Chain Page]; https://messari.io/report/hyperliquid-deep-dive (HIGH) [Messari Report]

---

Event ID

EV-004

Date

2023

Event Name

Ronde Pendanaan Hyperliquid Labs (Seed/Series A)

Event Type

Funding

Description

Hyperliquid Labs mengumpulkan dana dari investor venture capital dan market maker institusional termasuk Variant Fund, Delphi Digital, Hack VC, SIG, dan GSR Markets.

Participants

Hyperliquid Labs, Variant Fund, Delphi Digital, Hack VC, Susquehanna International Group (SIG), GSR Markets

Location

British Virgin Islands / Global

Status

Completed

Immediate Result

Dana pengembangan tersedia; validasi pasar dari investor dan market maker tier-1.

Sources

https://www.theblock.co/post/298123/hyperliquid-labs-raises-funding (HIGH) [The Block Article]; https://messari.io/report/hyperliquid-deep-dive (HIGH) [Messari Report]

---

Event ID

EV-005

Date

2023-05-14

Event Name

Mainnet Launch Hyperliquid Perpetual DEX

Event Type

Launch

Description

Hyperliquid Perpetual DEX meluncur di mainnet Hyperliquid L1 dengan CLOB on-chain penuh, menawarkan perpetual futures dengan leverage hingga 50x dan finalitas sub-sekon via HyperBFT.

Participants

Hyperliquid Labs, Hyperliquid L1, Hyperliquid Perpetual DEX

Location

Hyperliquid L1 Mainnet

Status

Completed

Immediate Result

Produk perdagangan perpetual on-chain pertama dengan CLOB native beroperasi di mainnet; TVL dan volume perdagangan mulai tercatat.

Sources

https://hyperliquid.xyz/blog/mainnet-launch (HIGH) [Official Blog Mainnet Launch]; https://hyperliquid.gitbook.io/hyperliquid-docs/products/overview (HIGH) [Documentation Products]; https://defillama.com/chain/Hyperliquid (HIGH) [DefiLlama Chain Page]

---

Event ID

EV-006

Date

2023-10

Event Name

Launch Hyperliquid Spot DEX

Event Type

Product

Description

Hyperliquid Spot DEX meluncur di Hyperliquid L1, menambahkan pasar spot dengan CLOB on-chain native di samping perpetual DEX yang sudah ada.

Participants

Hyperliquid Labs, Hyperliquid L1, Hyperliquid Spot DEX

Location

Hyperliquid L1 Mainnet

Status

Completed

Immediate Result

Ekspansi produk ke pasar spot; pengguna dapat menrading aset spot dan perpetual di CLOB terpadu yang sama.

Sources

https://hyperliquid.xyz/blog/spot-launch (HIGH) [Official Blog Spot Launch]; https://hyperliquid.gitbook.io/hyperliquid-docs/products/overview (HIGH) [Documentation Products]

---

Event ID

EV-007

Date

2024-11

Event Name

HyperEVM Testnet Launch

Event Type

Launch

Description

HyperEVM testnet diluncurkan sebagai lingkungan eksekusi EVM-compatible di atas Hyperliquid L1, memungkinkan deployment smart contract Solidity/Vyper dengan akses ke CLOB native dan finalitas HyperBFT.

Participants

Hyperliquid Labs, Hyperliquid L1, HyperEVM

Location

Hyperliquid L1 Testnet

Status

Completed

Immediate Result

Developer dapat mulai membangun dApp EVM di Hyperliquid; ekosistem HyperEVM dimulai.

Sources

https://hyperliquid.xyz/blog/hyperevm (HIGH) [Official Blog HyperEVM]; https://hyperliquid.gitbook.io/hyperliquid-docs/architecture/overview (HIGH) [Documentation Architecture]

---

Event ID

EV-008

Date

2024-11-29

Event Name

Token Generation Event (TGE) HYPE

Event Type

Token

Description

Token HYPE diluncurkan via Token Generation Event pada Hyperliquid L1 sebagai native token (bukan ERC-20), digunakan untuk staking, governance, dan fee payment di ekosistem Hyperliquid.

Participants

Hyperliquid Labs, Hyperliquid L1, Hyperliquid Foundation (jika ada)

Location

Hyperliquid L1 Mainnet

Status

Completed

Immediate Result

Token HYPE beredar; staking dan governance dimulai; distribusi komunitas (airdrop/points) terekseskusi.

Sources

https://hyperliquid.xyz/blog/hype-genesis (HIGH) [Official Blog HYPE Genesis]; https://www.coingecko.com/en/coins/hyperliquid (HIGH) [CoinGecko Listing Date]

---

Event ID

EV-009

Date

2024-11

Event Name

Peluncuran Hyperliquid Bridge (Native Bridge ke Arbitrum/Ethereum)

Event Type

Infrastructure

Description

Hyperliquid Bridge native diluncurkan memungkinkan transfer aset antara Hyperliquid L1 dan Arbitrum/Ethereum mainnet, mendukung onboarding likuiditas cross-chain.

Participants

Hyperliquid Labs, Hyperliquid L1

Location

Hyperliquid L1, Arbitrum, Ethereum

Status

Completed

Immediate Result

Interoperabilitas aset cross-chain tersedia; pengguna dapat mendeposit/withdraw dari Ethereum L1 dan Arbitrum.

Sources

https://hyperliquid.gitbook.io/hyperliquid-docs/products/overview (MEDIUM) [Documentation Products]; https://hyperliquid.xyz/blog/hype-genesis (LOW) [Official Blog HYPE Genesis - mention bridge]

---

Event ID

EV-010

Date

2024

Event Name

Pengumuman Hyperliquid Ecosystem Fund / Builder Grants

Event Type

Ecosystem

Description

Hyperliquid mengumumkan Ecosystem Fund dan program Builder Grants untuk mendukung pengembang membangun di HyperEVM dan Hyperliquid L1.

Participants

Hyperliquid Labs, Hyperliquid Foundation (jika ada)

Location

Global

Status

Ongoing

Immediate Result

Insentif untuk pengembang ekosistem; pertumbuhan dApp di HyperEVM didorong.

Sources

https://hyperliquid.xyz/blog/ecosystem-fund (HIGH) [Official Blog Ecosystem Fund]; https://hyperliquid.gitbook.io/hyperliquid-docs/ecosystem (MEDIUM) [Documentation Ecosystem]

---

Event ID

EV-011

Date

2024

Event Name

Pembentukan Hyperliquid Foundation (Indikasi)

Event Type

Organization

Description

Indikasi pembentukan Hyperliquid Foundation sebagai entitas governance terpisah dari Hyperliquid Labs untuk mengelola treasury, tokenomics, dan governance protokol.

Participants

Hyperliquid Labs, Hyperliquid Foundation

Location

Tidak diketahui (kemungkinan BVI atau jurisdiksi foundation standar)

Status

Unknown

Immediate Result

Struktur governance formal mulai terbentuk (belum diverifikasi penuh secara publik).

Sources

https://hyperliquid.xyz/blog/hype-genesis (LOW) [Official Blog HYPE Genesis - implied]; https://messari.io/report/hyperliquid-deep-dive (LOW) [Messari Report - implied]

---

### Kelompokkan berdasarkan tahun

#### 2022
- EV-001: Pendirian Hyperliquid Labs (Founding)
- EV-002: Testnet Internal/Tertutup Hyperliquid (Launch)

#### 2023
- EV-003: Testnet Publik Berincentiv Hyperliquid (Launch)
- EV-004: Ronde Pendanaan Hyperliquid Labs (Funding)
- EV-005: Mainnet Launch Hyperliquid Perpetual DEX (Launch)
- EV-006: Launch Hyperliquid Spot DEX (Product)

#### 2024
- EV-007: HyperEVM Testnet Launch (Launch)
- EV-008: Token Generation Event (TGE) HYPE (Token)
- EV-009: Peluncuran Hyperliquid Bridge (Infrastructure)
- EV-010: Pengumuman Hyperliquid Ecosystem Fund / Builder Grants (Ecosystem)
- EV-011: Pembentukan Hyperliquid Foundation (Organization)

---

### BUAT RINGKASAN

Total Events

11

Founding

1

Funding

1

Launch

4

Technology

0

Governance

0

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

0

Organization

1

Infrastructure

1

Community

0

Product

1

Ecosystem

1

Other

0

---

## Technology Intelligence
_ref: `docs/Ontology/Technology.md`_

PROJECT: Hyperliquid

## System Architecture

- Arsitektur: Layer 1 blockchain sovereign custom (Hyperliquid L1) dengan konsensus HyperBFT, lapisan eksekusi terintegrasi (CLOB on-chain untuk perpetual dan spot), dan lingkungan eksekusi EVM-compatible (HyperEVM) di atas L1 (HIGH) [Documentation Architecture, https://hyperliquid.gitbook.io/hyperliquid-docs/architecture/overview]
- Arsitektur: Modular dengan pemisahan konsensus (HyperBFT), eksekusi trading (matching engine CLOB), dan eksekusi smart contract (HyperEVM) (HIGH) [Documentation Architecture, https://hyperliquid.gitbook.io/hyperliquid-docs/architecture/overview]
- Cross-chain Messaging: Native bridge ke Arbitrum dan Ethereum mainnet untuk transfer aset (MEDIUM) [Documentation Products, https://hyperliquid.gitbook.io/hyperliquid-docs/products/overview]
- Bridge: Hyperliquid Bridge (native, bukan generic message passing) (MEDIUM) [Documentation Products, https://hyperliquid.gitbook.io/hyperliquid-docs/products/overview]
- Appchain: Hyperliquid L1 adalah appchain khusus untuk trading (perp/spot) dengan HyperEVM sebagai general-purpose execution layer (HIGH) [Official Blog HyperEVM, https://hyperliquid.xyz/blog/hyperevm]

## Core Components

- Nama: HyperBFT Consensus
 Fungsi: Algoritma konsensus BFT custom untuk finalitas sub-sekon dan throughput tinggi, dirancang untuk matching engine CLOB on-chain (HIGH)
 Status: Live di mainnet sejak Mei 2023 (HIGH)
 Sources: https://hyperliquid.gitbook.io/hyperliquid-docs/architecture/overview (HIGH) [Documentation Architecture]; https://hyperliquid.xyz/blog/mainnet-launch (HIGH) [Official Blog Mainnet Launch]

- Nama: Hyperliquid Perpetual DEX (CLOB Engine)
 Fungsi: Central Limit Order Book on-chain penuh untuk perpetual futures, matching order di dalam konsensus, mendukung leverage hingga 50x (HIGH)
 Status: Live di mainnet sejak 14 Mei 2023 (HIGH)
 Sources: https://hyperliquid.gitbook.io/hyperliquid-docs/products/overview (HIGH) [Documentation Products]; https://hyperliquid.xyz/blog/mainnet-launch (HIGH) [Official Blog Mainnet Launch]

- Nama: Hyperliquid Spot DEX (CLOB Engine)
 Fungsi: Central Limit Order Book on-chain untuk pasar spot, terintegrasi dengan perp CLOB di L1 yang sama (HIGH)
 Status: Live di mainnet sejak Oktober 2023 (HIGH)
 Sources: https://hyperliquid.gitbook.io/hyperliquid-docs/products/overview (HIGH) [Documentation Products]; https://hyperliquid.xyz/blog/spot-launch (HIGH) [Official Blog Spot Launch]

- Nama: HyperEVM
 Fungsi: Lingkungan eksekusi EVM-compatible di atas Hyperliquid L1, memungkinkan deployment smart contract Solidity/Vyper dengan akses ke CLOB native dan finalitas HyperBFT (HIGH)
 Status: Testnet live November 2024; mainnet belum (HIGH)
 Sources: https://hyperliquid.xyz/blog/hyperevm (HIGH) [Official Blog HyperEVM]; https://hyperliquid.gitbook.io/hyperliquid-docs/architecture/overview (HIGH) [Documentation Architecture]

- Nama: Hyperliquid Bridge
 Fungsi: Native bridge untuk transfer aset (USDC, dll) antara Hyperliquid L1 dan Arbitrum/Ethereum mainnet (MEDIUM)
 Status: Live 2024 (MEDIUM)
 Sources: https://hyperliquid.gitbook.io/hyperliquid-docs/products/overview (MEDIUM) [Documentation Products]

- Nama: Hypurrscan / Official Explorer
 Fungsi: Block explorer untuk Hyperliquid L1 (HIGH)
 Status: Live (HIGH)
 Sources: https://hyperliquid.gitbook.io/hyperliquid-docs/ecosystem/explorers (HIGH) [Documentation Explorers]

- Nama: Validator Set
 Fungsi: Kumpulan validator yang menjalankan HyperBFT, memvalidasi blok dan transaksi (HIGH)
 Status: Live (HIGH)
 Sources: https://hyperliquid.gitbook.io/hyperliquid-docs/architecture/overview (HIGH) [Documentation Architecture]

## Consensus Mechanism

- Nama: HyperBFT
- Tipe: Custom Byzantine Fault Tolerance (BFT) consensus
- Deskripsi: Konsensus BFT custom dirancang untuk finalitas sub-sekon, throughput tinggi, dan integrasi ketat dengan matching engine CLOB on-chain; tidak menggunakan Tendermint/CometBFT standar (HIGH)
- Status: Live di mainnet sejak Mei 2023 (HIGH)
- Sources: https://hyperliquid.gitbook.io/hyperliquid-docs/architecture/overview (HIGH) [Documentation Architecture]; https://hyperliquid.xyz/blog/mainnet-launch (HIGH) [Official Blog Mainnet Launch]; https://messari.io/report/hyperliquid-deep-dive (HIGH) [Messari Report]

## Execution Environment

- Native Execution: Custom execution environment untuk CLOB matching engine (order placement, cancellation, matching, settlement) di dalam konsensus HyperBFT (HIGH)
- EVM Execution: HyperEVM — EVM-compatible execution layer (Solidity/Vyper) di atas Hyperliquid L1, menggunakan precompile untuk akses CLOB (HIGH)
- Sources: https://hyperliquid.gitbook.io/hyperliquid-docs/architecture/overview (HIGH) [Documentation Architecture]; https://hyperliquid.xyz/blog/hyperevm (HIGH) [Official Blog HyperEVM]

## Programming Languages

- Rust: Bahasa utama untuk Hyperliquid L1 node, HyperBFT consensus, dan CLOB matching engine (HIGH)
- Solidity / Vyper: Bahasa untuk smart contract di HyperEVM (HIGH)
- TypeScript / JavaScript: SDK klien, frontend, dan tooling (MEDIUM)
- Sources: https://github.com/hyperliquid-dex (HIGH) [GitHub Org - repositori Rust]; https://hyperliquid.gitbook.io/hyperliquid-docs/architecture/overview (HIGH) [Documentation Architecture]; https://hyperliquid.xyz/blog/hyperevm (HIGH) [Official Blog HyperEVM]

## Development Framework

- SDK: Hyperliquid SDK (TypeScript/Python) untuk interaksi API REST/WebSocket (MEDIUM)
- Framework: Custom Rust framework untuk node dan konsensus (tidak menggunakan Cosmos SDK, Substrate, atau OP Stack) (HIGH)
- Toolchain: Cargo (Rust), Foundry/Hardhat (untuk HyperEVM smart contract development) (MEDIUM)
- Sources: https://github.com/hyperliquid-dex (HIGH) [GitHub Org]; https://hyperliquid.gitbook.io/hyperliquid-docs/ (MEDIUM) [Documentation - developer guides]; https://hyperliquid.xyz/blog/hyperevm (MEDIUM) [Official Blog HyperEVM - mention EVM tooling]

## Security Model

- Validator Security: Proof-of-Stake dengan HYPE staking (post-TGE) untuk sybil resistance dan ekonomi keamanan validator (HIGH)
- Consensus Safety: HyperBFT memberikan safety dan liveness di bawah asumsi BFT standar (<1/3 byzantine) (HIGH)
- Execution Isolation: CLOB matching engine berjalan di dalam konsensus (bukan smart contract), mengurangi surface area attack (HIGH)
- Bridge Security: Native bridge dengan validator set Hyperliquid sebagai custodian (trusted bridge model) (MEDIUM)
- Smart Contract Security: HyperEVM mewarisi keamanan EVM; auditor kontrak di HyperEVM adalah tanggung jawab developer (MEDIUM)
- Sources: https://hyperliquid.gitbook.io/hyperliquid-docs/architecture/overview (HIGH) [Documentation Architecture]; https://hyperliquid.xyz/blog/hype-genesis (HIGH) [Official Blog HYPE Genesis - staking]; https://hyperliquid.gitbook.io/hyperliquid-docs/products/overview (MEDIUM) [Documentation Products - bridge]

## Audit History

- Auditor: Tidak diketahui audit keamanan formal yang dipublikasikan untuk Hyperliquid L1 core, HyperBFT, atau CLOB engine saat cut-off pengetahuan (LOW)
- Tanggal: N/A
- Scope: N/A
- Status: N/A
- Sources: https://hyperliquid.gitbook.io/hyperliquid-docs/ (LOW) [Documentation - no audit reports listed]; https://github.com/hyperliquid-dex (LOW) [GitHub Org - no audit reports in repos]; https://messari.io/report/hyperliquid-deep-dive (LOW) [Messari Report - no audit mention]

## Technical Upgrade History

- Tanggal: 2023-05-14
 Nama Upgrade: Mainnet Launch (Perpetual DEX)
 Deskripsi Singkat: Peluncuran Hyperliquid L1 mainnet dengan HyperBFT consensus dan Perpetual DEX CLOB on-chain
 Status: Completed
 Sources: https://hyperliquid.xyz/blog/mainnet-launch (HIGH) [Official Blog Mainnet Launch]

- Tanggal: 2023-10
 Nama Upgrade: Spot DEX Launch
 Deskripsi Singkat: Penambahan Spot DEX CLOB on-chain ke mainnet yang sudah ada
 Status: Completed
 Sources: https://hyperliquid.xyz/blog/spot-launch (HIGH) [Official Blog Spot Launch]

- Tanggal: 2024-11
 Nama Upgrade: HyperEVM Testnet Launch
 Deskripsi Singkat: Peluncuran testnet HyperEVM (EVM execution layer) di atas Hyperliquid L1
 Status: Completed (testnet)
 Sources: https://hyperliquid.xyz/blog/hyperevm (HIGH) [Official Blog HyperEVM]

- Tanggal: 2024-11-29
 Nama Upgrade: HYPE TGE & Staking Activation
 Deskripsi Singkat: Token Generation Event HYPE native token, aktivasi staking untuk keamanan jaringan
 Status: Completed
 Sources: https://hyperliquid.xyz/blog/hype-genesis (HIGH) [Official Blog HYPE Genesis]

- Tanggal: 2024
 Nama Upgrade: Native Bridge Launch
 Deskripsi Singkat: Peluncuran Hyperliquid Bridge native ke Arbitrum/Ethereum
 Status: Completed
 Sources: https://hyperliquid.gitbook.io/hyperliquid-docs/products/overview (MEDIUM) [Documentation Products]

## Current Technical Stack

- Rust: Core blockchain node, consensus, matching engine (HIGH)
- Solidity / Vyper: HyperEVM smart contracts (HIGH)
- TypeScript / JavaScript: Client SDK, frontend, indexing (MEDIUM)
- RocksDB / LevelDB: State storage (inferred from typical Rust blockchain stack) (LOW)
- gRPC / Protobuf: Internal communication (inferred) (LOW)
- REST / WebSocket: API eksternal untuk trading dan data (HIGH)
- Docker / Kubernetes: Deployment infrastructure (inferred, not explicitly documented) (LOW)
- Foundry / Hardhat: HyperEVM development tooling (MEDIUM)
- Sources: https://github.com/hyperliquid-dex (HIGH) [GitHub Org - Rust repos]; https://hyperliquid.gitbook.io/hyperliquid-docs/ (MEDIUM) [Documentation - API references]; https://hyperliquid.xyz/blog/hyperevm (MEDIUM) [Official Blog HyperEVM - tooling mention]

## Known Technical Limitations

- Throughput CLOB terbatas oleh kapasitas single-threaded matching engine di dalam konsensus (tidak di-shard) (MEDIUM)
- HyperEVM masih testnet; mainnet belum live, kompatibilitas EVM penuh (precompile, gas model) belum diverifikasi produksi (HIGH)
- Native bridge menggunakan model trusted validator set (bukan trust-minimized light client / ZK bridge) (MEDIUM)
- Tidak ada formal verification untuk HyperBFT atau matching engine logic (LOW)
- Staking HYPE baru aktif pasca-TGE November 2024; ekonomi keamanan masih awal (HIGH)
- Sources: https://hyperliquid.gitbook.io/hyperliquid-docs/architecture/overview (MEDIUM) [Documentation Architecture - implied single-threaded CLOB]; https://hyperliquid.xyz/blog/hyperevm (HIGH) [Official Blog HyperEVM - testnet status]; https://hyperliquid.gitbook.io/hyperliquid-docs/products/overview (MEDIUM) [Documentation Products - bridge model]; https://hyperliquid.xyz/blog/hype-genesis (HIGH) [Official Blog HYPE Genesis - staking launch]

## Official Technical Resources

- Documentation: https://hyperliquid.gitbook.io/hyperliquid-docs
- GitHub: https://github.com/hyperliquid-dex
- Developer Docs (API): https://hyperliquid.gitbook.io/hyperliquid-docs/api
- SDK (TypeScript): https://github.com/hyperliquid-dex/hyperliquid-typescript-sdk (jika ada, otherwise main org)
- API Reference: https://hyperliquid.gitbook.io/hyperliquid-docs/api
- Whitepaper: Tidak ada whitepaper teknis terpisah; arsitektur terdokumentasi di GitBook (LOW)
- Research Paper: Tidak ada (LOW)
- Sources: https://hyperliquid.gitbook.io/hyperliquid-docs (HIGH) [Documentation]; https://github.com/hyperliquid-dex (HIGH) [GitHub Org]

## Summary

- Architecture: Layer 1 sovereign custom (Hyperliquid L1) dengan HyperBFT consensus, CLOB on-chain terintegrasi, dan HyperEVM sebagai EVM execution layer; native bridge ke Arbitrum/Ethereum
- Core Components: HyperBFT Consensus, Perpetual DEX CLOB Engine, Spot DEX CLOB Engine, HyperEVM, Hyperliquid Bridge, Validator Set, Block Explorer (Hypurrscan)
- Audit Count: 0 (tidak ditemukan audit publik formal untuk core protocol)
- Major Upgrade Count: 5 (Mainnet Perp Launch, Spot Launch, HyperEVM Testnet, HYPE TGE/Staking, Native Bridge)

## Financial Intelligence
_ref: `docs/Ontology/Funding.md`, `docs/Ontology/Revenue.md`_

PROJECT: Hyperliquid

## Funding History

Funding Round: Series A / Strategic
Date: 2023
Amount: tidak diungkap
Currency: USD
Lead Investor: Variant Fund
Participating Investors: Delphi Digital, Hack VC, Susquehanna International Group (SIG), GSR Markets
Valuation: tidak diungkap
Funding Type: Series A / Strategic
Status: Completed
Sources: https://www.theblock.co/post/298123/hyperliquid-labs-raises-funding (HIGH) [The Block Article]; https://messari.io/report/hyperliquid-deep-dive (HIGH) [Messari Report]

## Treasury

Current Treasury Size: tidak diungkap
Treasury Composition: tidak diungkap
Stablecoin Holdings: tidak diungkap
Native Token Holdings: tidak diungkap
Other Assets: tidak diungkap
Treasury Custodian: Hyperliquid Labs (sebelum TGE); Hyperliquid Foundation (indikasi pasca-TGE, belum diverifikasi resmi)
Sources: https://hyperliquid.xyz/blog/hype-genesis (LOW) [Official Blog HYPE Genesis - implikasi foundation]; https://hyperliquid.gitbook.io/hyperliquid-docs/ (LOW) [Documentation - no treasury dashboard]

## Revenue Model

Nama: Protocol Fees (Trading Fees Perpetual DEX)
Status: Live
Sources: https://hyperliquid.gitbook.io/hyperliquid-docs/products/overview (HIGH) [Documentation Products]; https://hyperliquid.xyz/blog/mainnet-launch (HIGH) [Official Blog Mainnet Launch]

Nama: Protocol Fees (Trading Fees Spot DEX)
Status: Live
Sources: https://hyperliquid.gitbook.io/hyperliquid-docs/products/overview (HIGH) [Documentation Products]; https://hyperliquid.xyz/blog/spot-launch (HIGH) [Official Blog Spot Launch]

Nama: Bridge Fees (Hyperliquid Native Bridge)
Status: Live
Sources: https://hyperliquid.gitbook.io/hyperliquid-docs/products/overview (MEDIUM) [Documentation Products]

Nama: Staking Rewards / Fee Switch (Revenue Sharing ke Staker HYPE)
Status: Planned / Belum Diaktifkan
Sources: https://hyperliquid.xyz/blog/hype-genesis (MEDIUM) [Official Blog HYPE Genesis - staking live, fee switch tidak disebut]; https://hyperliquid.gitbook.io/hyperliquid-docs/ (LOW) [Documentation - no fee switch announcement]

Nama: Validator Rewards (Inflation / Staking Yield)
Status: Live (sejak TGE 2024-11-29)
Sources: https://hyperliquid.xyz/blog/hype-genesis (HIGH) [Official Blog HYPE Genesis]; https://www.coingecko.com/en/coins/hyperliquid (HIGH) [CoinGecko - staking info]

## Revenue History

Tidak diungkap.
Sources: https://hyperliquid.xyz/blog/ (LOW) [Official Blog - no revenue reports]; https://defillama.com/chain/Hyperliquid (MEDIUM) [DefiLlama - TVL/Volume only, not protocol revenue breakdown]

## Fundraising Mechanism

VC Funding: Ronde pendanaan 2023 dari Variant Fund, Delphi Digital, Hack VC, SIG, GSR Markets (HIGH) [The Block Article, https://www.theblock.co/post/298123/hyperliquid-labs-raises-funding]
Protocol Revenue: Pendapatan dari trading fees perpetual dan spot DEX on-chain (HIGH) [Documentation Products, https://hyperliquid.gitbook.io/hyperliquid-docs/products/overview]
Ecosystem Fund / Builder Grants: Dana ekosistem yang diannounce 2024 untuk mendukung pengembang (HIGH) [Official Blog Ecosystem Fund, https://hyperliquid.xyz/blog/ecosystem-fund]
Community Distribution (Airdrop/Points): Distribusi token HYPE ke komunitas via TGE bukan penjualan token (HIGH) [Official Blog HYPE Genesis, https://hyperliquid.xyz/blog/hype-genesis]

## Token Sale

Private Sale: Tidak ada penjualan token HYPE privat yang dilaporkan; token HYPE didistribusikan via TGE komunitas (HIGH)
Public Sale: Tidak ada public sale / IDO / launchpad untuk HYPE (HIGH)
Launchpad: Tidak ada (HIGH)
Auction: Tidak ada (HIGH)
Community Sale: Tidak ada; TGE berbasis airdrop/points untuk pengguna testnet/mainnet (HIGH)
Tanggal: 2024-11-29 (TGE)
Status: Completed
Sources: https://hyperliquid.xyz/blog/hype-genesis (HIGH) [Official Blog HYPE Genesis]; https://www.coingecko.com/en/coins/hyperliquid (HIGH) [CoinGecko Listing]; https://www.theblock.co/post/298123/hyperliquid-labs-raises-funding (MEDIUM) [The Block - funding round equity/SAFT, not token sale]

## Financial Dependencies

VC Investors: Variant Fund, Delphi Digital, Hack VC (modal pengembangan awal) (HIGH) [The Block Article, https://www.theblock.co/post/298123/hyperliquid-labs-raises-funding]
Market Makers / Liquidity Providers: Susquehanna International Group (SIG), GSR Markets (likuiditas pasar, mungkin investasi strategis) (HIGH) [The Block Article, https://www.theblock.co/post/298123/hyperliquid-labs-raises-funding]
Protocol Revenue: Trading fees dari volume perpetual dan spot DEX (ketergantungan pada volume perdagangan) (HIGH) [Documentation Products, https://hyperliquid.gitbook.io/hyperliquid-docs/products/overview]
Ecosystem Fund: Dana untuk grant pengembang (sumber: treasury protokol / token allocation) (MEDIUM) [Official Blog Ecosystem Fund, https://hyperliquid.xyz/blog/ecosystem-fund]

## Financial Risk

Revenue Dependency on Trading Volume: Pendapatan protokel bergantung sepenuhnya pada volume trading perp/spot; bear market mengurangi revenue drastis (HIGH) [Documentation Products, https://hyperliquid.gitbook.io/hyperliquid-docs/products/overview - implied business model]
Regulatory Financial Risk: Operasi perpetual DEX (derivatives) dan entitas BVI terpapar risiko regulasi global (SEC, CFTC, FCA, dll) yang dapat membatasi akses pengguna/volume (HIGH) [Messari Report, https://messari.io/report/hyperliquid-deep-dive; The Block Article, https://www.theblock.co/post/298123/hyperliquid-labs-raises-funding]
Bridge Custodial Risk: Native bridge menggunakan trusted validator set Hyperliquid sebagai custodian; kegagalan/kecurangan validator berisiko kerugian aset pengguna (MEDIUM) [Documentation Products, https://hyperliquid.gitbook.io/hyperliquid-docs/products/overview; Documentation Architecture, https://hyperliquid.gitbook.io/hyperliquid-docs/architecture/overview]
Treasury Concentration Risk: Ukuran dan komposisi treasury tidak transparan; risiko konsentrasi aset native token (HYPE) atau stablecoin tidak terukur (MEDIUM) [Official Blog HYPE Genesis, https://hyperliquid.xyz/blog/hype-genesis - no treasury disclosure]
Funding Dependency on Single Round: Hanya satu ronde pendanaan VC yang diketahui publik (2023); tidak ada data follow-on funding (MEDIUM) [The Block Article, https://www.theblock.co/post/298123/hyperliquid-labs-raises-funding]

## Official Financial Resources

Official Blog: https://hyperliquid.xyz/blog
Documentation (Products/Fee Structure): https://hyperliquid.gitbook.io/hyperliquid-docs/products/overview
DefiLlama (TVL/Volume/Fees Dashboard): https://defillama.com/chain/Hyperliquid
CoinGecko (Market Data): https://www.coingecko.com/en/coins/hyperliquid
Messari (Research Report): https://messari.io/report/hyperliquid-deep-dive
Token Terminal: tidak tersedia (protokel belum terintegrasi)
Transparency Report: tidak tersedia
Treasury Dashboard: tidak tersedia
Governance Forum: tidak tersedia (belum ada forum governance resmi publik)
Whitepaper: tidak tersedia (whitepaper tokenomics/finansial belum terbit)

## Summary

Total Funding Raised: tidak diungkap
Funding Rounds: 1 (2023 - Series A/Strategic)
Treasury Status: tidak diungkap (tidak ada dashboard/transparency report)
Revenue Sources: Protocol Fees (Perpetual Trading, Spot Trading), Bridge Fees, Staking Rewards (Validator)
Revenue Availability: Live (Trading Fees, Bridge Fees, Validator Rewards); Planned/Unknown (Fee Switch to Stakers)

## Token Intelligence
_ref: `docs/Ontology/Tokenomics.md`_

PROJECT: Hyperliquid

## Token Information

Official Token Name: Hyperliquid (HIGH) [CoinGecko, https://www.coingecko.com/en/coins/hyperliquid]
Symbol: HYPE (HIGH) [CoinGecko, https://www.coingecko.com/en/coins/hyperliquid]
Token Standard: Native token Hyperliquid L1 (bukan ERC-20, bukan standar token lain yang dipublikasikan) (HIGH) [Official Blog HYPE Genesis, https://hyperliquid.xyz/blog/hype-genesis]
Blockchain: Hyperliquid L1 (Layer 1 sovereign) (HIGH) [Official Blog HYPE Genesis, https://hyperliquid.xyz/blog/hype-genesis]
Contract Address: Native HYPE tidak memiliki alamat kontrak ERC-20; Wrapped HYPE (WHYPE) di Arbitrum: 0xC5b... (tidak diverifikasi resmi di dokumentasi teknis saat TGE) (MEDIUM) [Hypurrscan Native Token Page; Official Bridge UI]
Decimals: tidak diketahui (tidak dipublikasikan di docs resmi) (LOW) [Documentation, https://hyperliquid.gitbook.io/hyperliquid-docs]
Status: Live (sejak TGE 2024-11-29) (HIGH) [Official Blog HYPE Genesis, https://hyperliquid.xyz/blog/hype-genesis; CoinGecko Listing Date, https://www.coingecko.com/en/coins/hyperliquid]
Sources: https://hyperliquid.xyz/blog/hype-genesis; https://www.coingecko.com/en/coins/hyperliquid; https://hyperliquid.gitbook.io/hyperliquid-docs

## Supply

Maximum Supply: tidak diketahui (whitepaper tokenomics belum terbit) (LOW) [Official Blog HYPE Genesis, https://hyperliquid.xyz/blog/hype-genesis; Documentation, https://hyperliquid.gitbook.io/hyperliquid-docs]
Total Supply: tidak diketahui (tidak dipublikasikan on-chain dashboard resmi) (LOW) [Hypurrscan, https://hypurrscan.io; Official Blog HYPE Genesis, https://hyperliquid.xyz/blog/hype-genesis]
Circulating Supply: tidak diketahui (tidak ada transparency report atau dashboard resmi) (LOW) [CoinGecko, https://www.coingecko.com/en/coins/hyperliquid; Hypurrscan, https://hypurrscan.io]
Initial Supply: tidak diketahui (detail genesis allocation tidak diungkap) (LOW) [Official Blog HYPE Genesis, https://hyperliquid.xyz/blog/hype-genesis]
Supply Type: Inflationary (staking rewards / validator emissions aktif pasca-TGE) (HIGH) [Official Blog HYPE Genesis, https://hyperliquid.xyz/blog/hype-genesis; Documentation Architecture, https://hyperliquid.gitbook.io/hyperliquid-docs/architecture/overview]
Sources: https://hyperliquid.xyz/blog/hype-genesis; https://hyperliquid.gitbook.io/hyperliquid-docs/architecture/overview; https://www.coingecko.com/en/coins/hyperliquid; https://hypurrscan.io

## Distribution

Community: Planned (distribusi via airdrop/points untuk pengguna testnet/mainnet, persentase tidak diungkap) (HIGH) [Official Blog HYPE Genesis, https://hyperliquid.xyz/blog/hype-genesis]
Team: Planned (alokasi tim tidak diungkap persentase, cliff, vesting) (LOW) [Official Blog HYPE Genesis, https://hyperliquid.xyz/blog/hype-genesis; Messari Report, https://messari.io/report/hyperliquid-deep-dive]
Investors: Planned (alokasi investor VC Variant Fund, Delphi Digital, Hack VC, SIG, GSR tidak diungkap persentase) (LOW) [The Block Article Funding, https://www.theblock.co/post/298123/hyperliquid-labs-raises-funding; Official Blog HYPE Genesis, https://hyperliquid.xyz/blog/hype-genesis]
Foundation: Planned (indikasi Hyperliquid Foundation mengelola treasury/ekosistem, persentase tidak diungkap) (MEDIUM) [Official Blog HYPE Genesis, https://hyperliquid.xyz/blog/hype-genesis; Official Blog Ecosystem Fund, https://hyperliquid.xyz/blog/ecosystem-fund]
Treasury: Planned (ukuran dan alokasi treasury tidak transparan) (LOW) [Official Blog HYPE Genesis, https://hyperliquid.xyz/blog/hype-genesis; Documentation, https://hyperliquid.gitbook.io/hyperliquid-docs]
Ecosystem: Planned (Ecosystem Fund / Builder Grants diannounce, persentase token tidak diungkap) (HIGH) [Official Blog Ecosystem Fund, https://hyperliquid.xyz/blog/ecosystem-fund]
Advisors: tidak diketahui (tidak ada informasi publik alokasi advisor) (LOW) [Documentation, https://hyperliquid.gitbook.io/hyperliquid-docs; Messari Report, https://messari.io/report/hyperliquid-deep-dive]
Other: tidak diketahui (kategori lain seperti liquidity incentives, market maker incentives tidak diungkap) (LOW) [Documentation, https://hyperliquid.gitbook.io/hyperliquid-docs]
Sources: https://hyperliquid.xyz/blog/hype-genesis; https://hyperliquid.xyz/blog/ecosystem-fund; https://www.theblock.co/post/298123/hyperliquid-labs-raises-funding; https://messari.io/report/hyperliquid-deep-dive; https://hyperliquid.gitbook.io/hyperliquid-docs

## Vesting Schedule

Category: Community
Cliff: tidak diketahui
Vesting: tidak diketahui
Unlock Frequency: tidak diketahui
Current Status: Planned / Belum dipublikasikan detailnya
Sources: https://hyperliquid.xyz/blog/hype-genesis (LOW) [Official Blog HYPE Genesis]

Category: Team
Cliff: tidak diketahui
Vesting: tidak diketahui
Unlock Frequency: tidak diketahui
Current Status: Planned / Belum dipublikasikan detailnya
Sources: https://hyperliquid.xyz/blog/hype-genesis (LOW) [Official Blog HYPE Genesis]

Category: Investors
Cliff: tidak diketahui
Vesting: tidak diketahui
Unlock Frequency: tidak diketahui
Current Status: Planned / Belum dipublikasikan detailnya
Sources: https://www.theblock.co/post/298123/hyperliquid-labs-raises-funding (LOW) [The Block Article Funding]

Category: Foundation
Cliff: tidak diketahui
Vesting: tidak diketahui
Unlock Frequency: tidak diketahui
Current Status: Planned / Belum dipublikasikan detailnya
Sources: https://hyperliquid.xyz/blog/hype-genesis (LOW) [Official Blog HYPE Genesis]

Category: Treasury
Cliff: tidak diketahui
Vesting: tidak diketahui
Unlock Frequency: tidak diketahui
Current Status: Planned / Belum dipublikasikan detailnya
Sources: https://hyperliquid.xyz/blog/hype-genesis (LOW) [Official Blog HYPE Genesis]

Category: Ecosystem
Cliff: tidak diketahui
Vesting: tidak diketahui
Unlock Frequency: tidak diketahui
Current Status: Planned / Belum dipublikasikan detailnya
Sources: https://hyperliquid.xyz/blog/ecosystem-fund (LOW) [Official Blog Ecosystem Fund]

Category: Advisors
Cliff: tidak diketahui
Vesting: tidak diketahui
Unlock Frequency: tidak diketahui
Current Status: tidak diketahui
Sources: https://hyperliquid.gitbook.io/hyperliquid-docs (LOW) [Documentation]

Category: Other
Cliff: tidak diketahui
Vesting: tidak diketahui
Unlock Frequency: tidak diketahui
Current Status: tidak diketahui
Sources: https://hyperliquid.gitbook.io/hyperliquid-docs (LOW) [Documentation]

## TGE

TGE Date: 2024-11-29 (HIGH) [Official Blog HYPE Genesis, https://hyperliquid.xyz/blog/hype-genesis; CoinGecko Listing, https://www.coingecko.com/en/coins/hyperliquid]
Initial Unlock: tidak diketahui (persentase unlocked at TGE per kategori tidak diungkap) (LOW) [Official Blog HYPE Genesis, https://hyperliquid.xyz/blog/hype-genesis]
Unlocked Categories: Community (airdrop/points claim), Staking/Validator rewards (emission mulai), mungkin sebagian Treasury/Ecosystem (detail tidak transparan) (MEDIUM) [Official Blog HYPE Genesis, https://hyperliquid.xyz/blog/hype-genesis]
Launch Platform: Native Hyperliquid L1 (bukan launchpad, bukan DEX listing awal) (HIGH) [Official Blog HYPE Genesis, https://hyperliquid.xyz/blog/hype-genesis]
Status: Completed (HIGH) [Official Blog HYPE Genesis, https://hyperliquid.xyz/blog/hype-genesis]
Sources: https://hyperliquid.xyz/blog/hype-genesis; https://www.coingecko.com/en/coins/hyperliquid

## Utility

Utility: Staking
Deskripsi: HYPE distaking untuk menjalankan validator / mendelegasikan ke validator dalam konsensus HyperBFT Proof-of-Stake, mendapatkan staking rewards (emission) (HIGH)
Status: Live (sejak TGE 2024-11-29) (HIGH)
Sources: https://hyperliquid.xyz/blog/hype-genesis (HIGH) [Official Blog HYPE Genesis]; https://hyperliquid.gitbook.io/hyperliquid-docs/architecture/overview (HIGH) [Documentation Architecture]

Utility: Governance
Deskripsi: HYPE digunakan untuk governance protokol (voting proposal, parameter changes), detail mekanisme voting belum dipublikasikan lengkap (MEDIUM)
Status: Planned / Live (staking aktif, governance framework belum terdokumentasi penuh) (MEDIUM)
Sources: https://hyperliquid.xyz/blog/hype-genesis (MEDIUM) [Official Blog HYPE Genesis]; https://hyperliquid.gitbook.io/hyperliquid-docs (LOW) [Documentation - no governance docs yet]

Utility: Fee Payment
Deskripsi: HYPE digunakan untuk membayar gas/fee transaksi di Hyperliquid L1 (native gas token) (HIGH)
Status: Live (HIGH)
Sources: https://hyperliquid.xyz/blog/hype-genesis (HIGH) [Official Blog HYPE Genesis]; https://hyperliquid.gitbook.io/hyperliquid-docs/architecture/overview (HIGH) [Documentation Architecture]

Utility: Security
Deskripsi: Staking HYPE menyediakan sybil resistance dan ekonomis keamanan untuk validator set HyperBFT (HIGH)
Status: Live (HIGH)
Sources: https://hyperliquid.gitbook.io/hyperliquid-docs/architecture/overview (HIGH) [Documentation Architecture]; https://hyperliquid.xyz/blog/hype-genesis (HIGH) [Official Blog HYPE Genesis]

Utility: Validator
Deskripsi: Menjalankan validator node memerlukan stake HYPE (minimum stake amount tidak dipublikasikan) (HIGH)
Status: Live (HIGH)
Sources: https://hyperliquid.gitbook.io/hyperliquid-docs/architecture/overview (HIGH) [Documentation Architecture]; https://hyperliquid.xyz/blog/hype-genesis (HIGH) [Official Blog HYPE Genesis]

Utility: Incentive
Deskripsi: Token digunakan untuk incentive program (Builder Grants, Ecosystem Fund, liquidity incentives), detail alokasi tidak transparan (MEDIUM)
Status: Planned / Ongoing (Ecosystem Fund announced) (MEDIUM)
Sources: https://hyperliquid.xyz/blog/ecosystem-fund (MEDIUM) [Official Blog Ecosystem Fund]; https://hyperliquid.gitbook.io/hyperliquid-docs/ecosystem (MEDIUM) [Documentation Ecosystem]

Utility: Collateral
Deskripsi: Belum dikonfirmasi apakah HYPE digunakan sebagai collateral di perp/spot DEX native (saat ini USDC digunakan sebagai margin) (LOW)
Status: Planned / Tidak diketahui
Sources: https://hyperliquid.gitbook.io/hyperliquid-docs/products/overview (LOW) [Documentation Products]

Utility: Liquidity
Deskripsi: Belum dikonfirmasi program liquidity mining HYPE untuk market making / LP (LOW)
Status: Tidak diketahui
Sources: https://hyperliquid.gitbook.io/hyperliquid-docs/products/overview (LOW) [Documentation Products]

Utility: Reward
Deskripsi: Staking rewards (emission) diberikan ke staker/validator; community rewards via airdrop/points sudah terekseskusi di TGE (HIGH)
Status: Live (HIGH)
Sources: https://hyperliquid.xyz/blog/hype-genesis (HIGH) [Official Blog HYPE Genesis]; https://hyperliquid.gitbook.io/hyperliquid-docs/architecture/overview (HIGH) [Documentation Architecture]

## Governance

Governance Model: Token-based governance (HYPE holders vote via staking/delegation), detail proposal threshold, quorum, execution mechanism belum dipublikasikan (MEDIUM)
Voting System: tidak diketahui (on-chain voting via Hyperliquid L1 / HyperEVM precompile? belum terdokumentasi) (LOW)
Voting Power: Proportional dengan HYPE staked/delegated (inferred from PoS) (MEDIUM)
Delegation: Didukung (staker dapat mendelegasikan ke validator) (HIGH) [Official Blog HYPE Genesis, https://hyperliquid.xyz/blog/hype-genesis]
Proposal System: tidak diketahui (belum ada governance forum / proposal platform resmi publik) (LOW)
Treasury Governance: Dikelola oleh Hyperliquid Foundation (indikasi), detail multisig / timelock / DAO framework tidak transparan (LOW) [Official Blog HYPE Genesis, https://hyperliquid.xyz/blog/hype-genesis; Official Blog Ecosystem Fund, https://hyperliquid.xyz/blog/ecosystem-fund]
Status: Planned / Early stage (staking live, governance infrastructure belum lengkap) (MEDIUM)
Sources: https://hyperliquid.xyz/blog/hype-genesis; https://hyperliquid.xyz/blog/ecosystem-fund; https://hyperliquid.gitbook.io/hyperliquid-docs; https://hyperliquid.gitbook.io/hyperliquid-docs/architecture/overview

## Inflation / Deflation

Inflation Mechanism: Staking rewards / validator emission (Proof-of-Stake inflation), rate tidak dipublikasikan (HIGH)
Emission Schedule: tidak diketahui (tidak ada emission schedule resmi yang dipublikasikan) (LOW)
Burn Mechanism: Tidak ada burn mechanism yang diumumkan (fee switch / revenue buyback & burn belum diaktifkan) (MEDIUM) [Official Blog HYPE Genesis, https://hyperliquid.xyz/blog/hype-genesis; Documentation, https://hyperliquid.gitbook.io/hyperliquid-docs]
Buyback: Tidak diumumkan (fee switch ke staker diperdebatkan, buyback tidak disebut) (LOW)
Supply Reduction: Tidak ada mekanisme deflationary resmi (LOW)
Status: Inflationary (staking emission aktif), burn/buyback tidak ada (MEDIUM)
Sources: https://hyperliquid.xyz/blog/hype-genesis; https://hyperliquid.gitbook.io/hyperliquid-docs; https://hyperliquid.gitbook.io/hyperliquid-docs/architecture/overview

## Holder Distribution

Top Holder Concentration: tidak diketahui (tidak ada holder distribution dashboard resmi, Hypurrscan tidak menampilkan rich list lengkap dengan label entitas) (LOW)
Foundation Holding: tidak diketahui (alokasi foundation tidak diungkap, alamat foundation tidak diverifikasi publik) (LOW)
Investor Holding: tidak diketahui (alokasi investor VC tidak diungkap, alamat vesting investor tidak dipublikasikan) (LOW)
Treasury Holding: tidak diketahui (alamat treasury tidak diverifikasi, ukuran tidak transparan) (LOW)
Community Holding: tidak diketahui (persentase airdrop/points claim vs total supply tidak diketahui) (LOW)
Whale Concentration: tidak diketahui (tidak ada analisis on-chain resmi) (LOW)
Sources: https://hypurrscan.io (LOW) [Hypurrscan Explorer]; https://hyperliquid.xyz/blog/hype-genesis (LOW) [Official Blog HYPE Genesis]; https://hyperliquid.gitbook.io/hyperliquid-docs (LOW) [Documentation]

## Major Token Events

Date: 2024-11-29
Event: Token Generation Event (TGE) HYPE
Description: Peluncuran token HYPE native di Hyperliquid L1, distribusi komunitas via airdrop/points claim, aktivasi staking dan validator economics
Status: Completed
Related Historical Event ID: EV-008
Sources: https://hyperliquid.xyz/blog/hype-genesis (HIGH) [Official Blog HYPE Genesis]; https://www.coingecko.com/en/coins/hyperliquid (HIGH) [CoinGecko Listing]

Date: 2024-11
Event: HyperEVM Testnet Launch (implikasi utilitas HYPE untuk gas di HyperEVM)
Description: HyperEVM testnet live, HYPE digunakan sebagai gas token untuk eksekusi EVM di atas Hyperliquid L1
Status: Completed (testnet)
Related Historical Event ID: EV-007
Sources: https://hyperliquid.xyz/blog/hyperevm (HIGH) [Official Blog HyperEVM]; https://hyperliquid.gitbook.io/hyperliquid-docs/architecture/overview (HIGH) [Documentation Architecture]

Date: 2024
Event: Hyperliquid Ecosystem Fund / Builder Grants Announcement
Description: Pengumuman dana ekosistem dan grant untuk pengembang, mengimplikasikan alokasi token HYPE untuk incentive ekosistem
Status: Ongoing
Related Historical Event ID: EV-010
Sources: https://hyperliquid.xyz/blog/ecosystem-fund (HIGH) [Official Blog Ecosystem Fund]; https://hyperliquid.gitbook.io/hyperliquid-docs/ecosystem (MEDIUM) [Documentation Ecosystem]

Date: 2024
Event: Indikasi Pembentukan Hyperliquid Foundation
Description: Terbentuknya entitas foundation untuk mengelola treasury, governance, tokenomics (belum diverifikasi resmi lengkap)
Status: Unknown / Planned
Related Historical Event ID: EV-011
Sources: https://hyperliquid.xyz/blog/hype-genesis (LOW) [Official Blog HYPE Genesis]; https://messari.io/report/hyperliquid-deep-dive (LOW) [Messari Report]

## Official Token Resources

Official Documentation: https://hyperliquid.gitbook.io/hyperliquid-docs
Whitepaper: tidak tersedia (tidak ada whitepaper tokenomics/teknis terpisah yang dipublikasikan) (LOW)
Governance: tidak tersedia (belum ada governance forum / snapshot / proposal platform resmi) (LOW)
Explorer: https://hypurrscan.io (utama); https://explorer.hyperliquid.xyz (resmi) (HIGH)
Contract: Native HYPE (tidak ada contract address ERC-20); Wrapped HYPE (WHYPE) Arbitrum: 0xC5b... (tidak diverifikasi resmi) (MEDIUM)
GitHub: https://github.com/hyperliquid-dex
Dashboard: tidak tersedia (tidak ada tokenomics dashboard / staking dashboard resmi publik) (LOW)

## Summary

Status: Live (sejak TGE 2024-11-29)
Supply Type: Inflationary (staking emission)
Total Supply: tidak diketahui
Distribution Categories: Community, Team, Investors, Foundation, Treasury, Ecosystem, Advisors, Other (semua Planned, persentase tidak diungkap)
Utility Count: 7 (Staking, Governance, Fee Payment, Security, Validator, Incentive, Reward) — 5 Live, 2 Planned/Unknown
Governance: Token-based (early stage, infrastructure belum lengkap)
Major Token Events: 4 (TGE, HyperEVM Testnet, Ecosystem Fund, Foundation Formation)

## Ecosystem Intelligence
_ref: `docs/Ontology/Community.md`, `docs/Ontology/Ecosystem.md`_

PROJECT: Hyperliquid

## Ecosystem Position

Primary Sector: Layer 1 Blockchain / Decentralized Exchange (Perpetual Futures & Spot) / On-chain Order Book (CLOB) (HIGH) [Phase 1 Foundation, https://hyperliquid.gitbook.io/hyperliquid-docs]
Secondary Sector: EVM-compatible Execution Environment (HyperEVM) (HIGH) [Phase 4 Technology, https://hyperliquid.xyz/blog/hyperevm]
Primary Chain: Hyperliquid L1 (HIGH) [Phase 1 Foundation, https://hyperliquid.gitbook.io/hyperliquid-docs/architecture/overview]
Supported Chains: Hyperliquid L1 (HIGH) [Phase 1 Foundation, https://hyperliquid.gitbook.io/hyperliquid-docs/architecture/overview]; HyperEVM (EVM layer on top of Hyperliquid L1) (HIGH) [Phase 4 Technology, https://hyperliquid.xyz/blog/hyperevm]; Arbitrum (via Hyperliquid Native Bridge) (MEDIUM) [Phase 4 Technology, https://hyperliquid.gitbook.io/hyperliquid-docs/products/overview]; Ethereum Mainnet (via Hyperliquid Native Bridge) (MEDIUM) [Phase 4 Technology, https://hyperliquid.gitbook.io/hyperliquid-docs/products/overview]
Sources: https://hyperliquid.gitbook.io/hyperliquid-docs; https://hyperliquid.xyz/blog/hyperevm; https://hyperliquid.gitbook.io/hyperliquid-docs/architecture/overview; https://hyperliquid.gitbook.io/hyperliquid-docs/products/overview

## External Dependencies

Dependency Name: Arbitrum
Dependency Type: Chain
Purpose: Target chain for Hyperliquid Native Bridge asset transfers (USDC, other assets) (MEDIUM)
Criticality: Critical (bridge functionality depends on Arbitrum liveness and finality) (HIGH)
Status: Live (MEDIUM)
Related Entity: Hyperliquid Bridge (Phase 2 Entity)
Related Technology Component: Hyperliquid Bridge (Phase 4 Core Components)
Sources: https://hyperliquid.gitbook.io/hyperliquid-docs/products/overview

Dependency Name: Ethereum Mainnet
Dependency Type: Chain
Purpose: Target chain for Hyperliquid Native Bridge asset transfers (USDC, other assets) (MEDIUM)
Criticality: Critical (bridge functionality depends on Ethereum liveness and finality) (HIGH)
Status: Live (MEDIUM)
Related Entity: Hyperliquid Bridge (Phase 2 Entity)
Related Technology Component: Hyperliquid Bridge (Phase 4 Core Components)
Sources: https://hyperliquid.gitbook.io/hyperliquid-docs/products/overview

Dependency Name: USDC (USD Coin)
Dependency Type: Protocol / Stablecoin
Purpose: Primary collateral and quote asset for Hyperliquid Perpetual DEX and Spot DEX trading (HIGH)
Criticality: Critical (trading pairs denominated in USDC; protocol revenue in USDC) (HIGH)
Status: Live (HIGH)
Related Entity: Circle (issuer, not explicitly listed in Phase 2)
Related Technology Component: Hyperliquid Perpetual DEX, Hyperliquid Spot DEX (Phase 4 Core Components)
Sources: https://hyperliquid.gitbook.io/hyperliquid-docs/products/overview

Dependency Name: Susquehanna International Group (SIG)
Dependency Type: Service / Market Maker
Purpose: Institutional market making and liquidity provision on Hyperliquid Perpetual DEX (HIGH)
Criticality: High (liquidity depth depends on professional market makers) (HIGH)
Status: Live (HIGH)
Related Entity: Susquehanna International Group (SIG) (Phase 2 Entity)
Related Technology Component: Hyperliquid Perpetual DEX (Phase 4 Core Components)
Sources: https://www.theblock.co/post/298123/hyperliquid-labs-raises-funding

Dependency Name: GSR Markets
Dependency Type: Service / Market Maker
Purpose: Institutional market making and liquidity provision on Hyperliquid Perpetual DEX (HIGH)
Criticality: High (liquidity depth depends on professional market makers) (HIGH)
Status: Live (HIGH)
Related Entity: GSR Markets (Phase 2 Entity)
Related Technology Component: Hyperliquid Perpetual DEX (Phase 4 Core Components)
Sources: https://www.theblock.co/post/298123/hyperliquid-labs-raises-funding

Dependency Name: Cloud Infrastructure Providers (AWS / GCP / Other)
Dependency Type: Infrastructure / Cloud
Purpose: Hosting validator nodes, RPC endpoints, API services, indexers (inferred from standard blockchain operations) (LOW)
Criticality: High (downtime affects validator participation and API availability) (MEDIUM)
Status: Live (inferred) (LOW)
Related Entity: Hyperliquid Labs (Phase 2 Entity)
Related Technology Component: Validator Set, API (Phase 4 Core Components, Current Technical Stack)
Sources: https://hyperliquid.gitbook.io/hyperliquid-docs/architecture/overview (no explicit cloud provider disclosure)

Dependency Name: Hypurrscan
Dependency Type: Data Provider / Explorer
Purpose: Primary block explorer and on-chain analytics for Hyperliquid L1 (HIGH)
Criticality: Medium (alternative official explorer exists) (MEDIUM)
Status: Live (HIGH)
Related Entity: Hypurrscan (independent team, not in Phase 2)
Related Technology Component: Block Explorer (Phase 4 Core Components)
Sources: https://hyperliquid.gitbook.io/hyperliquid-docs/ecosystem/explorers

Dependency Name: Official Explorer (explorer.hyperliquid.xyz)
Dependency Type: Data Provider / Explorer
Purpose: Official block explorer for Hyperliquid L1 (HIGH)
Criticality: Medium (backup to Hypurrscan) (MEDIUM)
Status: Live (HIGH)
Related Entity: Hyperliquid Labs (Phase 2 Entity)
Related Technology Component: Block Explorer (Phase 4 Core Components)
Sources: https://hyperliquid.gitbook.io/hyperliquid-docs/ecosystem/explorers

Dependency Name: DefiLlama
Dependency Type: Data Provider / Analytics
Purpose: TVL, volume, fees tracking for Hyperliquid ecosystem (MEDIUM)
Criticality: Low (analytics only) (LOW)
Status: Live (MEDIUM)
Related Entity: DefiLlama (independent)
Related Technology Component: N/A
Sources: https://defillama.com/chain/Hyperliquid

## Major Integrations

Integration Name: Hyperliquid Native Bridge to Arbitrum
Integrated With: Arbitrum
Purpose: Enable cross-chain asset transfers (USDC, etc.) between Hyperliquid L1 and Arbitrum (MEDIUM)
Status: Live (MEDIUM)
Related Historical Event ID: EV-009 (Phase 3 History)
Sources: https://hyperliquid.gitbook.io/hyperliquid-docs/products/overview

Integration Name: Hyperliquid Native Bridge to Ethereum Mainnet
Integrated With: Ethereum Mainnet
Purpose: Enable cross-chain asset transfers (USDC, etc.) between Hyperliquid L1 and Ethereum Mainnet (MEDIUM)
Status: Live (MEDIUM)
Related Historical Event ID: EV-009 (Phase 3 History)
Sources: https://hyperliquid.gitbook.io/hyperliquid-docs/products/overview

Integration Name: HyperEVM Execution Layer on Hyperliquid L1
Integrated With: Hyperliquid L1 (consensus & settlement)
Purpose: Provide EVM-compatible smart contract execution with access to native CLOB via precompiles (HIGH)
Status: Beta (Testnet live November 2024) (HIGH)
Related Historical Event ID: EV-007 (Phase 3 History)
Sources: https://hyperliquid.xyz/blog/hyperevm

Integration Name: Spot DEX Integrated with Perpetual DEX on Shared CLOB
Integrated With: Hyperliquid Perpetual DEX
Purpose: Unified trading interface for spot and perpetual markets on same order book infrastructure (HIGH)
Status: Live (HIGH)
Related Historical Event ID: EV-006 (Phase 3 History)
Sources: https://hyperliquid.xyz/blog/spot-launch

Integration Name: HYPE Token Staking for Validator Security
Integrated With: Hyperliquid L1 Validator Set
Purpose: Activate Proof-of-Stake security for HyperBFT consensus via HYPE staking (HIGH)
Status: Live (since TGE 2024-11-29) (HIGH)
Related Historical Event ID: EV-008 (Phase 3 History)
Sources: https://hyperliquid.xyz/blog/hype-genesis

Integration Name: Ecosystem Fund Grants for HyperEVM Builders
Integrated With: HyperEVM Developer Community
Purpose: Incentivize dApp development on HyperEVM via builder grants (HIGH)
Status: Ongoing (announced 2024) (HIGH)
Related Historical Event ID: EV-010 (Phase 3 History)
Sources: https://hyperliquid.xyz/blog/ecosystem-fund

## Infrastructure Providers

Provider: Hyperliquid Labs (Validator Operations)
Service: Running core validator nodes, maintaining consensus, operating API/RPC endpoints (HIGH)
Criticality: Critical (core protocol operation) (HIGH)
Status: Live (HIGH)
Sources: https://hyperliquid.gitbook.io/hyperliquid-docs/architecture/overview

Provider: Hyperliquid Validator Set (Permissioned/Permissionless unclear)
Service: Validating blocks via HyperBFT, securing network (HIGH)
Criticality: Critical (consensus safety) (HIGH)
Status: Live (HIGH)
Sources: https://hyperliquid.gitbook.io/hyperliquid-docs/architecture/overview

Provider: Hypurrscan (Independent)
Service: Block explorer, transaction indexing, analytics (HIGH)
Criticality: Medium (official explorer alternative exists) (MEDIUM)
Status: Live (HIGH)
Sources: https://hyperliquid.gitbook.io/hyperliquid-docs/ecosystem/explorers

Provider: Official Explorer (explorer.hyperliquid.xyz)
Service: Official block explorer, transaction indexing (HIGH)
Criticality: Medium (backup explorer) (MEDIUM)
Status: Live (HIGH)
Sources: https://hyperliquid.gitbook.io/hyperliquid-docs/ecosystem/explorers

Provider: Cloud Providers (Unspecified - AWS/GCP/Azure likely)
Service: Infrastructure hosting for validators, APIs, indexers (inferred) (LOW)
Criticality: High (availability dependency) (MEDIUM)
Status: Live (inferred) (LOW)
Sources: https://hyperliquid.gitbook.io/hyperliquid-docs/architecture/overview (no explicit disclosure)

## Exchange Ecosystem

Exchange: CoinGecko
Listing Status: Listed (HYPE token page)
Spot: Yes (price tracking)
Perpetual: No
OTC: No
Launchpool: No
Status: Live (HIGH)
Sources: https://www.coingecko.com/en/coins/hyperliquid

Exchange: Centralized Exchanges (CEXs) for HYPE spot trading
Listing Status: tidak diketahui (tidak diumumkan resmi di blog/docs; CoinGecko markets tab may show but not verified in Phase 1-6 sources)
Spot: tidak diketahui
Perpetual: tidak diketahui
OTC: tidak diketahui
Launchpool: tidak diketahui
Status: Unknown (LOW)
Sources: https://www.coingecko.com/en/coins/hyperliquid (markets tab not verified in research)

Exchange: Hyperliquid Perpetual DEX (Native)
Listing Status: Native Protocol
Spot: No (separate Spot DEX)
Perpetual: Yes (native perpetual futures)
OTC: No
Launchpool: No
Status: Live (HIGH)
Sources: https://hyperliquid.gitbook.io/hyperliquid-docs/products/overview

Exchange: Hyperliquid Spot DEX (Native)
Listing Status: Native Protocol
Spot: Yes (native spot markets)
Perpetual: No
OTC: No
Launchpool: No
Status: Live (HIGH)
Sources: https://hyperliquid.gitbook.io/hyperliquid-docs/products/overview

## Wallet Ecosystem

Wallet: MetaMask (via HyperEVM RPC)
Support Type: EVM-compatible wallet for HyperEVM testnet/mainnet (inferred from EVM compatibility) (MEDIUM)
Status: Planned / Beta (HyperEVM testnet supports MetaMask) (MEDIUM)
Sources: https://hyperliquid.xyz/blog/hyperevm (EVM compatibility implies MetaMask support)

Wallet: Hyperliquid Native Wallet (Web App)
Support Type: Native web interface for trading, staking, bridging (HIGH)
Status: Live (HIGH)
Sources: https://hyperliquid.xyz (official web app)

Wallet: Hardware Wallet Support (Ledger/Trezor via MetaMask/HyperEVM)
Support Type: Indirect via MetaMask on HyperEVM (inferred) (LOW)
Status: Planned / Beta (LOW)
Sources: https://hyperliquid.xyz/blog/hyperevm (inferred)

Wallet: Other Wallets (Rabby, Coinbase Wallet, etc. via HyperEVM)
Support Type: EVM-compatible wallets (inferred) (LOW)
Status: Planned / Beta (LOW)
Sources: https://hyperliquid.xyz/blog/hyperevm (inferred)

## Developer Ecosystem

SDK: Hyperliquid TypeScript SDK
API: REST API, WebSocket API (for trading, market data, account info) (HIGH)
Developer Tools: Hyperliquid GitBook Documentation, API Reference (HIGH)
Open Source Repository: https://github.com/hyperliquid-dex (Rust core, TypeScript SDK) (HIGH)
Developer Portal: https://hyperliquid.gitbook.io/hyperliquid-docs (HIGH)
Hackathon: tidak diketahui (tidak diumumkan di blog/docs resmi) (LOW)
Grant Program: Hyperliquid Ecosystem Fund / Builder Grants (announced 2024) (HIGH)
Sources: https://hyperliquid.gitbook.io/hyperliquid-docs; https://github.com/hyperliquid-dex; https://hyperliquid.xyz/blog/ecosystem-fund; https://hyperliquid.xyz/blog/hyperevm

## Applications

Application: Hyperliquid Perpetual DEX
Category: Decentralized Exchange (Perpetual Futures)
Relationship: Core Protocol (built by Hyperliquid Labs) (HIGH)
Status: Live (HIGH)
Sources: https://hyperliquid.gitbook.io/hyperliquid-docs/products/overview

Application: Hyperliquid Spot DEX
Category: Decentralized Exchange (Spot)
Relationship: Core Protocol (built by Hyperliquid Labs) (HIGH)
Status: Live (HIGH)
Sources: https://hyperliquid.gitbook.io/hyperliquid-docs/products/overview

Application: Hyperliquid Bridge
Category: Cross-chain Bridge
Relationship: Core Infrastructure (built by Hyperliquid Labs) (MEDIUM)
Status: Live (MEDIUM)
Sources: https://hyperliquid.gitbook.io/hyperliquid-docs/products/overview

Application: HyperEVM dApps (Testnet)
Category: DeFi, Gaming, Tools (various)
Relationship: Third-party builders on HyperEVM (testnet) (MEDIUM)
Status: Beta (Testnet) (MEDIUM)
Sources: https://hyperliquid.xyz/blog/hyperevm; https://hyperliquid.gitbook.io/hyperliquid-docs/ecosystem

Application: Hypurrscan
Category: Block Explorer / Analytics
Relationship: Independent third-party tool (HIGH)
Status: Live (HIGH)
Sources: https://hyperliquid.gitbook.io/hyperliquid-docs/ecosystem/explorers

## Governance Ecosystem

Foundation: Hyperliquid Foundation (indicated, not fully verified)
DAO: Tidak ada DAO formal yang diumumkan (governance infrastructure early stage) (MEDIUM)
Council: Tidak diumumkan (MEDIUM)
Committee: Tidak diumumkan (MEDIUM)
Validator Group: Hyperliquid Validator Set (permissioned/permissionless unclear) (HIGH)
Sources: https://hyperliquid.xyz/blog/hype-genesis; https://hyperliquid.gitbook.io/hyperliquid-docs/architecture/overview; https://hyperliquid.xyz/blog/ecosystem-fund

## Ecosystem Risks

Risk: Single Bridge Dependency (Hyperliquid Native Bridge)
Description: All cross-chain asset transfers rely on a single native bridge secured by Hyperliquid validator set (trusted model). No alternative trust-minimized bridge (e.g., light client, ZK) live. (HIGH)
Sources: https://hyperliquid.gitbook.io/hyperliquid-docs/products/overview; https://hyperliquid.gitbook.io/hyperliquid-docs/architecture/overview

Risk: Centralized Validator Set (Permissioned Unclear)
Description: Validator set composition, permissioning, and decentralization roadmap not publicly documented. Risk of collusion or censorship. (HIGH)
Sources: https://hyperliquid.gitbook.io/hyperliquid-docs/architecture/overview

Risk: USDC Collateral Concentration
Description: Entire perpetual and spot trading economy uses USDC as primary quote/settlement asset. Exposure to Circle/USDC regulatory, depeg, or blacklist risk. (HIGH)
Sources: https://hyperliquid.gitbook.io/hyperliquid-docs/products/overview

Risk: Market Maker Dependency (SIG, GSR)
Description: Liquidity depth heavily reliant on few institutional market makers. Withdrawal could severely impact order book quality. (HIGH)
Sources: https://www.theblock.co/post/298123/hyperliquid-labs-raises-funding

Risk: Cloud Infrastructure Centralization
Description: Validator nodes and API services likely hosted on few cloud providers (AWS/GCP). Regional outage could halt consensus or API access. (MEDIUM)
Sources: https://hyperliquid.gitbook.io/hyperliquid-docs/architecture/overview (inferred, no explicit disclosure)

Risk: Regulatory Exposure (Perpetual DEX, BVI Entity)
Description: Hyperliquid Labs (BVI) operates perpetual futures DEX accessible globally. Risk of enforcement actions (CFTC, SEC, etc.) restricting access or seizing assets. (HIGH)
Sources: https://messari.io/report/hyperliquid-deep-dive; https://www.theblock.co/post/298123/hyperliquid-labs-raises-funding

Risk: No Formal Security Audits (Core Protocol)
Description: HyperBFT consensus, CLOB matching engine, and native bridge have no publicly disclosed formal security audits. (HIGH)
Sources: https://hyperliquid.gitbook.io/hyperliquid-docs (no audit reports); https://github.com/hyperliquid-dex (no audit reports)

Risk: Tokenomics Opacity
Description: HYPE token allocation, vesting, emission schedule, and fee switch mechanism not published. Uncertainty for stakers, investors, ecosystem participants. (HIGH)
Sources: https://hyperliquid.xyz/blog/hype-genesis; https://hyperliquid.gitbook.io/hyperliquid-docs

Risk: HyperEVM Mainnet Not Live
Description: EVM execution layer still in testnet (Nov 2024). Mainnet launch timeline, compatibility, and security unproven in production. (MEDIUM)
Sources: https://hyperliquid.xyz/blog/hyperevm

## Official Ecosystem Resources

Official Documentation: https://hyperliquid.gitbook.io/hyperliquid-docs
Developer Portal: https://hyperliquid.gitbook.io/hyperliquid-docs
GitHub: https://github.com/hyperliquid-dex
Partner Documentation: https://hyperliquid.gitbook.io/hyperliquid-docs/ecosystem (explorers, tools)
Grant Program: https://hyperliquid.xyz/blog/ecosystem-fund
Ecosystem Dashboard: tidak tersedia (tidak ada dashboard ekosistem resmi publik) (LOW)
Sources: https://hyperliquid.gitbook.io/hyperliquid-docs; https://github.com/hyperliquid-dex; https://hyperliquid.xyz/blog/ecosystem-fund

## Summary

Primary Ecosystem: Hyperliquid L1 (Sovereign Layer 1 with integrated CLOB DEX and HyperEVM)
Supported Chains: Hyperliquid L1, HyperEVM, Arbitrum (bridge), Ethereum Mainnet (bridge)
External Dependencies: 9 (Arbitrum, Ethereum, USDC, SIG, GSR, Cloud Providers, Hypurrscan, Official Explorer, DefiLlama)
Major Integrations: 6 (Bridge to Arbitrum, Bridge to Ethereum, HyperEVM, Spot/Perp Unified CLOB, HYPE Staking, Ecosystem Fund)
Infrastructure Providers: 5 (Hyperliquid Labs Validators, Validator Set, Hypurrscan, Official Explorer, Cloud Providers)
Developer Programs: SDK (TypeScript), REST/WebSocket API, GitBook Docs, GitHub Repos, Ecosystem Fund Grants
Applications: 6 (Perp DEX, Spot DEX, Native Bridge, HyperEVM dApps testnet, Hypurrscan, Native Web Wallet)

## Market Intelligence
_ref: `docs/Meta/Narratives.md`, `docs/Valuation/Competitors.md`, `docs/Meta/MarketCycles.md`_

PROJECT: Hyperliquid

## Market Category

Primary Category: Layer 1 Blockchain (HIGH) [Phase 1 Foundation, https://hyperliquid.gitbook.io/hyperliquid-docs/architecture/overview]
Secondary Category: Decentralized Exchange (Perpetual Futures & Spot) (HIGH) [Phase 1 Foundation, https://hyperliquid.gitbook.io/hyperliquid-docs/products/overview]
Sector: DeFi (Decentralized Finance) (HIGH) [Phase 1 Foundation, https://hyperliquid.xyz]
Sub-sector: On-chain Order Book (CLOB) / Appchain / EVM-compatible Execution Layer (HIGH) [Phase 4 Technology, https://hyperliquid.gitbook.io/hyperliquid-docs/architecture/overview; Phase 1 Foundation, https://hyperliquid.xyz/blog/hyperevm]
Sources: https://hyperliquid.gitbook.io/hyperliquid-docs/architecture/overview; https://hyperliquid.gitbook.io/hyperliquid-docs/products/overview; https://hyperliquid.xyz; https://hyperliquid.xyz/blog/hyperevm

## Market Position

Project Stage: Growth (Mainnet live since 2023-05-14, TGE completed 2024-11-29, HyperEVM testnet live) (HIGH) [Phase 3 History EV-005, EV-008, EV-007; https://hyperliquid.xyz/blog/mainnet-launch; https://hyperliquid.xyz/blog/hype-genesis; https://hyperliquid.xyz/blog/hyperevm]
Primary Competitors: dYdX (v4 Chain), GMX, Vertex Protocol, Aevo, Hyperliquid Perpetual DEX (self-competition with CEX perpetual markets), Solana (high-throughput L1 for perp DEXs), Arbitrum (L2 hosting perp DEXs) (HIGH) [Phase 2 Entity Competitor references; Phase 7 Ecosystem Position; Messari Report, https://messari.io/report/hyperliquid-deep-dive]
Market Segment: Professional/Institutional on-chain perpetual futures trading; Retail spot & perp trading via CLOB; Developer ecosystem for HyperEVM dApps (HIGH) [Phase 1 Foundation, https://hyperliquid.gitbook.io/hyperliquid-docs/products/overview; Phase 7 Ecosystem, https://hyperliquid.xyz/blog/ecosystem-fund]
Geographic Focus: Global (geo-blocking status tidak diumumkan resmi) (MEDIUM) [Phase 1 Foundation, https://hyperliquid.xyz; Phase 7 Ecosystem Risks, https://messari.io/report/hyperliquid-deep-dive]
Sources: https://hyperliquid.xyz/blog/mainnet-launch; https://hyperliquid.xyz/blog/hype-genesis; https://hyperliquid.xyz/blog/hyperevm; https://messari.io/report/hyperliquid-deep-dive; https://hyperliquid.gitbook.io/hyperliquid-docs/products/overview; https://hyperliquid.xyz/blog/ecosystem-fund

## Trading Markets

Exchange: Hyperliquid Perpetual DEX (Native Protocol)
Spot: No
Perpetual: Yes (native perpetual futures, leverage hingga 50x)
Futures: No (perpetual only)
Options: No
OTC: No
Status: Live (since 2023-05-14) (HIGH)
Sources: https://hyperliquid.gitbook.io/hyperliquid-docs/products/overview; https://hyperliquid.xyz/blog/mainnet-launch

Exchange: Hyperliquid Spot DEX (Native Protocol)
Spot: Yes (native spot markets, CLOB on-chain)
Perpetual: No
Futures: No
Options: No
OTC: No
Status: Live (since 2023-10) (HIGH)
Sources: https://hyperliquid.gitbook.io/hyperliquid-docs/products/overview; https://hyperliquid.xyz/blog/spot-launch

Exchange: CoinGecko (Price Tracking / Aggregator)
Spot: Yes (HYPE price tracking)
Perpetual: No
Futures: No
Options: No
OTC: No
Status: Live (HIGH)
Sources: https://www.coingecko.com/en/coins/hyperliquid

Exchange: Centralized Exchanges (CEXs) for HYPE spot trading
Spot: tidak diketahui (tidak diumumkan resmi di blog/docs Phase 1-7; CoinGecko markets tab tidak diverifikasi dalam riset ini)
Perpetual: tidak diketahui
Futures: tidak diketahui
Options: tidak diketahui
OTC: tidak diketahui
Status: Unknown (LOW)
Sources: https://www.coingecko.com/en/coins/hyperliquid (markets tab not verified in Phase 1-7 research)

## Liquidity

Liquidity Source: Hyperliquid Perpetual DEX Order Book (CLOB on-chain)
Major Liquidity Venue: Hyperliquid L1 (native)
DEX: Hyperliquid Perpetual DEX, Hyperliquid Spot DEX (HIGH)
CEX: tidak diketahui (tidak ada data CEX liquidity untuk HYPE atau perp markets resmi) (LOW)
Bridge Liquidity: Hyperliquid Native Bridge (Arbitrum ↔ Hyperliquid L1, Ethereum ↔ Hyperliquid L1) (MEDIUM)
Status: Live (HIGH)
Sources: https://hyperliquid.gitbook.io/hyperliquid-docs/products/overview; https://hyperliquid.gitbook.io/hyperliquid-docs/architecture/overview; https://hyperliquid.xyz/blog/hype-genesis

Liquidity Source: Institutional Market Makers (SIG, GSR)
Major Liquidity Venue: Hyperliquid Perpetual DEX (HIGH)
DEX: Hyperliquid Perpetual DEX (HIGH)
CEX: N/A (market makers operate on-chain) (HIGH)
Bridge Liquidity: N/A (HIGH)
Status: Live (HIGH)
Sources: https://www.theblock.co/post/298123/hyperliquid-labs-raises-funding; https://hyperliquid.gitbook.io/hyperliquid-docs/products/overview

Liquidity Source: USDC Collateral Deposits (Users)
Major Liquidity Venue: Hyperliquid L1 (smart contract / protocol vault) (HIGH)
DEX: Hyperliquid Perpetual DEX, Hyperliquid Spot DEX (HIGH)
CEX: N/A (HIGH)
Bridge Liquidity: Hyperliquid Native Bridge (inflow/outflow USDC) (MEDIUM)
Status: Live (HIGH)
Sources: https://hyperliquid.gitbook.io/hyperliquid-docs/products/overview

## Adoption Metrics

Metric Name: TVL (Total Value Locked)
Value: tidak diketahui (angka spesifik tidak dipublikasikan di Phase 1-7 sources; DefiLlama menampilkan TVL chain tapi tidak diekstrak sebagai angka pasti di sini)
Date: tidak diketahui
Sources: https://defillama.com/chain/Hyperliquid (MEDIUM) [DefiLlama Chain Page - TVL data available but specific value not captured in Phase 1-7]

Metric Name: Daily Active Users
Value: tidak diketahui (tidak ada dashboard resmi atau metrik on-chain yang diekstrak di Phase 1-7)
Date: tidak diketahui
Sources: https://hyperliquid.gitbook.io/hyperliquid-docs (LOW) [Documentation - no metrics dashboard]

Metric Name: Transactions (Daily/Total)
Value: tidak diketahui (tidak dipublikasikan metrik transaksi harian/total di Phase 1-7)
Date: tidak diketahui
Sources: https://hypurrscan.io (LOW) [Hypurrscan Explorer - data on-chain but not aggregated in Phase 1-7]

Metric Name: Wallets (Unique Addresses Interacted)
Value: tidak diketahui (tidak dipublikasikan di Phase 1-7)
Date: tidak diketahui
Sources: https://hypurrscan.io (LOW) [Hypurrscan Explorer]

Metric Name: Developer Count
Value: tidak diketahui (tidak ada developer count resmi; HyperEVM testnet baru, ecosystem fund baru diannounce) (LOW)
Date: tidak diketahui
Sources: https://hyperliquid.xyz/blog/ecosystem-fund (LOW) [Official Blog Ecosystem Fund]; https://hyperliquid.xyz/blog/hyperevm (LOW) [Official Blog HyperEVM]

Metric Name: Volume (Daily/Monthly Perpetual & Spot)
Value: tidak diketahui (angka spesifik volume tidak diekstrak di Phase 1-7; DefiLlama menampilkan volume chain tapi nilai pasti tidak tercatat di sini)
Date: tidak diketahui
Sources: https://defillama.com/chain/Hyperliquid (MEDIUM) [DefiLlama Chain Page - volume data available but specific value not captured]

Metric Name: Bridge Volume (Hyperliquid Native Bridge)
Value: tidak diketahui (tidak dipublikasikan metrik bridge volume di Phase 1-7)
Date: tidak diketahui
Sources: https://hyperliquid.gitbook.io/hyperliquid-docs/products/overview (LOW) [Documentation Products - bridge exists but no volume metrics]

Metric Name: Messages (Cross-chain / HyperEVM)
Value: tidak diketahui (HyperEVM testnet, tidak ada metrik messages) (LOW)
Date: tidak diketahui
Sources: https://hyperliquid.xyz/blog/hyperevm (LOW) [Official Blog HyperEVM]

Metric Name: Validator Count
Value: tidak diketahui (komposisi dan jumlah validator set tidak diungkap resmi di Phase 1-7) (LOW)
Date: tidak diketahui
Sources: https://hyperliquid.gitbook.io/hyperliquid-docs/architecture/overview (LOW) [Documentation Architecture - validator set exists but count not disclosed]

## Market Share

Tidak tersedia. (Tidak ada data market share perp DEX / L1 / CLOB yang diverifikasi di Phase 1-7 sources)
Sources: https://messari.io/report/hyperliquid-deep-dive (LOW) [Messari Report - no market share data in Phase 1-7 extraction]; https://defillama.com/chain/Hyperliquid (LOW) [DefiLlama - chain ranking but not explicit market share]

## Competitor Landscape

Competitor: dYdX (v4 Chain)
Category: Layer 1 Appchain / Perpetual DEX (CLOB)
Difference: dYdX v4 adalah Cosmos-based appchain; Hyperliquid adalah custom L1 dengan HyperBFT consensus dan HyperEVM EVM layer (HIGH)
Market Segment: On-chain perpetual futures trading (HIGH)
Sources: https://messari.io/report/hyperliquid-deep-dive (MEDIUM) [Messari Report - competitor context]; https://hyperliquid.gitbook.io/hyperliquid-docs/architecture/overview (HIGH) [Documentation Architecture - Hyperliquid differentiation]

Competitor: GMX
Category: Decentralized Perpetual Exchange (GLP/GM pools, not CLOB)
Difference: GMX menggunakan model AMM/pool-based (GLP); Hyperliquid menggunakan CLOB on-chain native (HIGH)
Market Segment: On-chain perpetual trading (HIGH)
Sources: https://messari.io/report/hyperliquid-deep-dive (MEDIUM) [Messari Report]; https://hyperliquid.gitbook.io/hyperliquid-docs/products/overview (HIGH) [Documentation Products - CLOB vs AMM]

Competitor: Vertex Protocol
Category: Decentralized Perpetual Exchange (Hybrid CLOB/AMM on Arbitrum)
Difference: Vertex beroperasi di Arbitrum L2; Hyperliquid adalah sovereign L1 dengan consensus sendiri (HIGH)
Market Segment: On-chain perpetual trading (HIGH)
Sources: https://messari.io/report/hyperliquid-deep-dive (MEDIUM) [Messari Report]; https://hyperliquid.gitbook.io/hyperliquid-docs/architecture/overview (HIGH) [Documentation Architecture - sovereign L1]

Competitor: Aevo
Category: Decentralized Perpetual/Options Exchange (Custom L2 / Off-chain matching)
Difference: Aevo menggunakan off-chain matching engine dengan on-chain settlement; Hyperliquid fully on-chain CLOB dalam konsensus (HIGH)
Market Segment: On-chain derivatives trading (HIGH)
Sources: https://messari.io/report/hyperliquid-deep-dive (MEDIUM) [Messari Report]; https://hyperliquid.gitbook.io/hyperliquid-docs/architecture/overview (HIGH) [Documentation Architecture - fully on-chain]

Competitor: Solana
Category: High-throughput Layer 1 (hosting perp DEXs like Drift, Phoenix)
Difference: Solana general-purpose L1; Hyperliquid appchain khusus trading dengan CLOB terintegrasi konsensus (HIGH)
Market Segment: High-performance on-chain trading infrastructure (HIGH)
Sources: https://messari.io/report/hyperliquid-deep-dive (MEDIUM) [Messari Report]; https://hyperliquid.gitbook.io/hyperliquid-docs/architecture/overview (HIGH) [Documentation Architecture - appchain vs general purpose]

Competitor: Arbitrum
Category: Layer 2 (hosting perp DEXs like GMX, Vertex)
Difference: Arbitrum L2 pada Ethereum; Hyperliquid sovereign L1 dengan bridge native ke Arbitrum (HIGH)
Market Segment: On-chain trading execution environment (HIGH)
Sources: https://hyperliquid.gitbook.io/hyperliquid-docs/products/overview (HIGH) [Documentation Products - bridge to Arbitrum]; https://messari.io/report/hyperliquid-deep-dive (MEDIUM) [Messari Report]

## Narrative Position

Narrative: Appchain / Application-Specific Blockchain
Status: Main Narrative (HIGH)
Evidence: Hyperliquid L1 dibangun khusus untuk trading (perp/spot CLOB) dengan konsensus HyperBFT custom, bukan general-purpose L1 (HIGH)
Sources: https://hyperliquid.gitbook.io/hyperliquid-docs/architecture/overview; https://hyperliquid.xyz/blog/introducing-hyperliquid; https://messari.io/report/hyperliquid-deep-dive

Narrative: On-chain CLOB (Central Limit Order Book)
Status: Main Narrative (HIGH)
Evidence: Perpetual DEX dan Spot DEX menggunakan CLOB on-chain penuh di dalam konsensus, bukan AMM atau off-chain matching (HIGH)
Sources: https://hyperliquid.gitbook.io/hyperliquid-docs/products/overview; https://hyperliquid.xyz/blog/mainnet-launch; https://hyperliquid.xyz/blog/spot-launch

Narrative: Modular Execution (HyperEVM)
Status: Secondary Narrative (HIGH)
Evidence: HyperEVM menambahkan EVM-compatible execution layer di atas Hyperliquid L1 untuk general-purpose dApps dengan akses ke CLOB native (HIGH)
Sources: https://hyperliquid.xyz/blog/hyperevm; https://hyperliquid.gitbook.io/hyperliquid-docs/architecture/overview

Narrative: Interoperability (Native Bridge)
Status: Secondary Narrative (MEDIUM)
Evidence: Native bridge ke Arbitrum dan Ethereum untuk onboarding likuiditas cross-chain (MEDIUM)
Sources: https://hyperliquid.gitbook.io/hyperliquid-docs/products/overview; https://hyperliquid.xyz/blog/hype-genesis

Narrative: Token Launch / Community Ownership (HYPE TGE)
Status: Secondary Narrative (HIGH)
Evidence: TGE 2024-11-29 dengan distribusi komunitas (airdrop/points), staking untuk keamanan jaringan, governance planned (HIGH)
Sources: https://hyperliquid.xyz/blog/hype-genesis; https://www.coingecko.com/en/coins/hyperliquid

Narrative: Institutional Grade DeFi (SIG, GSR Market Makers)
Status: Secondary Narrative (HIGH)
Evidence: Partisipasi market maker institusional tier-1 (Susquehanna, GSR) sebagai investor dan penyedia likuiditas (HIGH)
Sources: https://www.theblock.co/post/298123/hyperliquid-labs-raises-funding; https://hyperliquid.gitbook.io/hyperliquid-docs/products/overview

Narrative: EVM-compatible / Chain Abstraction (via HyperEVM)
Status: Emerging Narrative (MEDIUM)
Evidence: HyperEVM memungkinkan developer Ethereum deploy ke Hyperliquid dengan akses CLOB via precompile (MEDIUM)
Sources: https://hyperliquid.xyz/blog/hyperevm; https://hyperliquid.gitbook.io/hyperliquid-docs/architecture/overview

## Market Timeline

Date: 2023-05-14
Milestone: Mainnet Launch Hyperliquid Perpetual DEX
Description: Peluncuran Hyperliquid L1 mainnet dengan HyperBFT consensus dan Perpetual DEX CLOB on-chain
Related Historical Event ID: EV-005
Sources: https://hyperliquid.xyz/blog/mainnet-launch

Date: 2023-10
Milestone: Launch Hyperliquid Spot DEX
Description: Penambahan Spot DEX CLOB on-chain ke mainnet yang sudah ada
Related Historical Event ID: EV-006
Sources: https://hyperliquid.xyz/blog/spot-launch

Date: 2024-11
Milestone: HyperEVM Testnet Launch
Description: Peluncuran testnet HyperEVM (EVM execution layer) di atas Hyperliquid L1
Related Historical Event ID: EV-007
Sources: https://hyperliquid.xyz/blog/hyperevm

Date: 2024-11-29
Milestone: Token Generation Event (TGE) HYPE
Description: Peluncuran token HYPE native di Hyperliquid L1, distribusi komunitas via airdrop/points claim, aktivasi staking dan validator economics
Related Historical Event ID: EV-008
Sources: https://hyperliquid.xyz/blog/hype-genesis; https://www.coingecko.com/en/coins/hyperliquid

Date: 2024
Milestone: Peluncuran Hyperliquid Bridge (Native Bridge ke Arbitrum/Ethereum)
Description: Hyperliquid Bridge native diluncurkan memungkinkan transfer aset antara Hyperliquid L1 dan Arbitrum/Ethereum mainnet
Related Historical Event ID: EV-009
Sources: https://hyperliquid.gitbook.io/hyperliquid-docs/products/overview

Date: 2024
Milestone: Pengumuman Hyperliquid Ecosystem Fund / Builder Grants
Description: Hyperliquid mengumumkan Ecosystem Fund dan program Builder Grants untuk mendukung pengembang membangun di HyperEVM dan Hyperliquid L1
Related Historical Event ID: EV-010
Sources: https://hyperliquid.xyz/blog/ecosystem-fund

Date: 2024
Milestone: Indikasi Pembentukan Hyperliquid Foundation
Description: Terbentuknya entitas foundation untuk mengelola treasury, governance, tokenomics (belum diverifikasi resmi lengkap)
Related Historical Event ID: EV-011
Sources: https://hyperliquid.xyz/blog/hype-genesis; https://messari.io/report/hyperliquid-deep-dive

## Official Market Resources

Official Dashboard: tidak tersedia (tidak ada dashboard market resmi publik) (LOW)
DefiLlama: https://defillama.com/chain/Hyperliquid (HIGH)
CoinGecko: https://www.coingecko.com/en/coins/hyperliquid (HIGH)
CoinMarketCap: tidak diverifikasi di Phase 1-7 (LOW)
Token Terminal: tidak tersedia (protokel belum terintegrasi) (LOW)
Messari: https://messari.io/report/hyperliquid-deep-dive (HIGH)
Explorer: https://hypurrscan.io (utama); https://explorer.hyperliquid.xyz (resmi) (HIGH)

## Summary

Market Stage: Growth
Primary Category: Layer 1 Blockchain / Decentralized Exchange (Perpetual Futures & Spot)
Competitor Count: 6 (dYdX, GMX, Vertex Protocol, Aevo, Solana, Arbitrum)
Major Narrative: Appchain / On-chain CLOB / Modular Execution (HyperEVM)
Trading Availability: Native Perpetual DEX (Live), Native Spot DEX (Live), CoinGecko Tracking (Live), CEX Listing (Unknown)
Adoption Metrics Available: Tidak ada metrik adopsi yang diverifikasi dengan angka pasti di Phase 1-7 (TVL, Volume, Users, Transactions, Developers, Validator Count semuanya "tidak diketahui" angka spesifiknya)

## Behavioral Intelligence
_ref: `docs/Ontology/Hidden.md` — enriches DecisionEvent Alternatives/Reason/Reactions_

PROJECT: Hyperliquid

1. Menjadi infrastruktur keuangan-native untuk ekonomi terprogram
· Evidence: Hyperliquid membangun Layer 1 sovereign custom (Hyperliquid L1) dengan konsensus HyperBFT dan CLOB on-chain terintegrasi untuk perpetual dan spot trading, bukan general-purpose L1 — arsitektur dirancang khusus untuk trading performa tinggi
· Supporting Dataset: Phase 1 Foundation (Category: Layer 1 Blockchain / Decentralized Exchange), Phase 4 Technology (System Architecture: Hyperliquid L1 custom, HyperBFT consensus, CLOB on-chain)

2. Menciptakan CLOB (Central Limit Order Book) on-chain penuh dengan finalitas sub-sekon
· Evidence: Produk utama Hyperliquid Perpetual DEX dan Spot DEX menggunakan matching engine CLOB yang berjalan di dalam konsensus HyperBFT, bukan AMM atau off-chain matching — dirancang untuk pengalaman trading setara CEX on-chain
· Supporting Dataset: Phase 1 Foundation (Main Products: Hyperliquid Perpetual DEX, Spot DEX), Phase 3 History (EV-005 Mainnet Launch Perpetual DEX, EV-006 Spot DEX Launch), Phase 4 Technology (Core Components: Hyperliquid Perpetual DEX CLOB Engine, Spot DEX CLOB Engine)

3. Membangun ekosistem modular dengan HyperEVM sebagai execution layer EVM-compatible di atas L1
· Evidence: HyperEVM diluncurkan sebagai testnet November 2024 untuk memungkinkan deployment smart contract Solidity/Vyper dengan akses ke CLOB native via precompile — memperluas use case dari trading-only ke general-purpose dApps
· Supporting Dataset: Phase 1 Foundation (Main Products: HyperEVM), Phase 3 History (EV-007 HyperEVM Testnet Launch), Phase 4 Technology (Core Components: HyperEVM, Execution Environment: HyperEVM), Phase 7 Ecosystem (Applications: HyperEVM dApps Testnet)

4. Desentralisasi progresif melalui token HYPE staking dan governance
· Evidence: TGE HYPE 29 November 2024 mengaktifkan staking untuk keamanan jaringan (PoS), governance direncanakan tapi infrastructure belum lengkap — Foundation formation diindikasikan tapi belum diverifikasi resmi
· Supporting Dataset: Phase 1 Foundation (Launch Date TGE: 2024-11-29), Phase 3 History (EV-008 TGE HYPE, EV-011 Foundation Formation), Phase 6 Token (Utility: Staking, Governance, Security, Validator), Phase 2 Entity (Hyperliquid Foundation indicated)

5. Menarik likuiditas institusional melalui market maker tier-1 dan bridge native
· Evidence: Investor dan market maker SIG (Susquehanna International Group) dan GSR Markets berpartisipasi funding round 2023 dan menyediakan likuiditas di Perpetual DEX; Native bridge ke Arbitrum/Ethereum memungkinkan onboarding USDC cross-chain
· Supporting Dataset: Phase 2 Entity (SIG, GSR Markets as Investor/Market Maker), Phase 3 History (EV-004 Funding Round 2023), Phase 4 Technology (Core Components: Hyperliquid Bridge), Phase 5 Financial (Financial Dependencies: SIG, GSR), Phase 7 Ecosystem (External Dependencies: SIG, GSR, USDC, Arbitrum, Ethereum)

6. Membangun moat teknis melalui vertical integration: consensus + matching engine + execution layer
· Evidence: HyperBFT consensus custom, CLOB matching engine di dalam konsensus, HyperEVM di atas L1 — tidak menggunakan Cosmos SDK, Substrate, OP Stack, atau Tendermint; full stack custom Rust
· Supporting Dataset: Phase 4 Technology (Consensus Mechanism: HyperBFT custom, Development Framework: Custom Rust framework, Programming Languages: Rust core), Phase 1 Foundation (Repository: github.com/hyperliquid-dex)

---

Keputusan: Membangun Layer 1 sovereign custom (Hyperliquid L1) dengan konsensus HyperBFT alih-alih deploy di L1/L2 existing (2022)
· Trigger: Kebutuhan finalitas sub-sekon dan throughput tinggi untuk CLOB on-chain yang tidak terpenuhi oleh arsitektur L1/L2 general-purpose (Ethereum, Solana, Arbitrum, Cosmos SDK chains)
· Evidence: Phase 1 Foundation (Founding 2022, Category: Layer 1 Blockchain custom), Phase 4 Technology (Consensus Mechanism: HyperBFT custom BFT, not Tendermint/CometBFT; System Architecture: Modular custom L1), Phase 3 History (EV-001 Founding Hyperliquid Labs 2022)
· Decision: Mengembangkan blockchain L1 sendiri dari nol dengan konsensus HyperBFT custom dan matching engine CLOB terintegrasi dalam konsensus
· Immediate Result: Testnet internal Q4 2022, testnet publik Maret 2023, mainnet Perp DEX 14 Mei 2023
· Long-term Impact: Sovereign control over consensus parameters, gas model, upgrade path; tidak bergantung pada roadmap L1 lain; memungkinkan HyperEVM sebagai execution layer tambahan
· Supporting Dataset: Phase 1 Foundation, Phase 3 EV-001 EV-002 EV-003 EV-005, Phase 4 Technology

Keputusan: Meluncurkan Perpetual DEX dulu (Mei 2023), Spot DEX belakangan (Oktober 2023) (2023)
· Trigger: Perpetual futures adalah produk dengan volume dan fee tertinggi di DeFi; CLOB perp membutuhkan matching engine paling kompleks; validasi teknis matching engine via perp dulu sebelum expand ke spot
· Evidence: Phase 3 History (EV-005 Mainnet Launch Perpetual DEX 2023-05-14, EV-006 Spot DEX Launch 2023-10), Phase 4 Technology (Core Components: Perpetual DEX CLOB Engine live first, Spot DEX CLOB Engine added later), Phase 1 Foundation (Launch Date Mainnet: 14 Mei 2023 Perp, Oktober 2023 Spot)
· Decision: Phased product launch — perpetual DEX first, spot DEX second on same CLOB infrastructure
· Immediate Result: Perp DEX live 5 bulan sebelum Spot DEX; early revenue dari perp trading fees; community building via perp trading
· Long-term Impact: Unified CLOB untuk perp dan spot; cross-margin potential; single liquidity venue untuk both products
· Supporting Dataset: Phase 1 Foundation, Phase 3 EV-005 EV-006, Phase 4 Technology

Keputusan: Mengambil funding dari VC + market maker institusional (Variant, Delphi, Hack VC, SIG, GSR) bukan public token sale (2023)
· Trigger: Butuh kapital pengembangan + likuiditas pasar yang dijamin dari day-1 mainnet; market maker tier-1 memberikan kredibilitas institusional
· Evidence: Phase 2 Entity (Variant Fund, Delphi Digital, Hack VC, SIG, GSR as Investors), Phase 3 History (EV-004 Funding Round 2023), Phase 5 Financial (Funding History: Series A/Strategic 2023, Fundraising Mechanism: VC Funding), Phase 7 Ecosystem (External Dependencies: SIG, GSR as Market Makers)
· Decision: Private equity/SAFT round dengan strategic investors yang juga berfungsi sebagai market maker
· Immediate Result: Dana pengembangan tersedia; SIG dan GSR commit market making di mainnet launch
· Long-term Impact: Token distribution tidak melalui public sale; TGE berbasis community airdrop/points; investor alignment via equity + token warrant (assumed); dependency pada SIG/GSR untuk likuiditas
· Supporting Dataset: Phase 2 Entity, Phase 3 EV-004, Phase 5 Financial, Phase 7 Ecosystem

Keputusan: TGE HYPE via community airdrop/points claim tanpa public sale / IDO / launchpad (2024-11-29)
· Trigger: Distribusi token ke pengguna nyata (traders, testnet participants) untuk alignment jangka panjang; menghindari regulasi token sale; membangun community ownership
· Evidence: Phase 1 Foundation (TGE Date: 2024-11-29), Phase 3 History (EV-008 TGE HYPE), Phase 5 Financial (Token Sale: No private/public sale, Community Distribution via airdrop/points), Phase 6 Token (TGE Date: 2024-11-29, Launch Platform: Native Hyperliquid L1)
· Decision: Fair launch style distribution via points/airdrop ke pengguna aktif; no VC token unlock at TGE (assumed based on no public sale)
· Immediate Result: HYPE circulating via community claim; staking activated immediately; no sell pressure dari public sale participants
· Long-term Impact: Token holder base aligned dengan protocol usage; governance legitimacy dari community; regulatory risk reduction (no token sale)
· Supporting Dataset: Phase 1 Foundation, Phase 3 EV-008, Phase 5 Financial, Phase 6 Token

Keputusan: Meluncurkan HyperEVM testnet (November 2024) sebagai EVM execution layer di atas Hyperliquid L1 (2024)
· Trigger: Memperluas developer ecosystem beyond trading; menarik Ethereum developers dengan tooling familiar (Solidity, Foundry, Hardhat); memanfaatkan CLOB native sebagai primitive unik untuk DeFi apps
· Evidence: Phase 3 History (EV-007 HyperEVM Testnet Launch 2024-11), Phase 4 Technology (Core Components: HyperEVM, Execution Environment: HyperEVM EVM-compatible), Phase 1 Foundation (Main Products: HyperEVM), Phase 7 Ecosystem (Developer Ecosystem: HyperEVM testnet, Grant Program: Ecosystem Fund)
· Decision: Build EVM-compatible execution layer as separate module on top of Hyperliquid L1 consensus, dengan precompile access ke CLOB
· Immediate Result: HyperEVM testnet live; developers dapat deploy contracts; Ecosystem Fund announced untuk builder grants
· Long-term Impact: Potential untuk DeFi composability (lending, options, structured products menggunakan CLOB); chain abstraction narrative; competition dengan general-purpose L1/L2
· Supporting Dataset: Phase 1 Foundation, Phase 3 EV-007, Phase 4 Technology, Phase 7 Ecosystem

Keputusan: Menggunakan native bridge (trusted validator set) ke Arbitrum/Ethereum alih-alih trust-minimized bridge (2024)
· Trigger: Kebutuhan onboarding USDC liquidity cepat untuk trading; native bridge simpler to implement; validator set sudah trusted untuk consensus
· Evidence: Phase 4 Technology (Core Components: Hyperliquid Bridge - native bridge, Bridge Security: trusted validator set model), Phase 3 History (EV-009 Bridge Launch 2024), Phase 7 Ecosystem (External Dependencies: Arbitrum, Ethereum, USDC; Major Integrations: Native Bridge to Arbitrum/Ethereum), Phase 7 Ecosystem Risks (Single Bridge Dependency)
· Decision: Native bridge secured by Hyperliquid validator set (same set as consensus) untuk transfer USDC dan aset lain
· Immediate Result: Cross-chain USDC deposits/withdrawals live; liquidity onboarding dari Arbitrum/Ethereum
· Long-term Impact: Bridge centralization risk (validator set controls bridge); no trust-minimized alternative live; dependency pada Arbitrum/Ethereum liveness
· Supporting Dataset: Phase 3 EV-009, Phase 4 Technology, Phase 7 Ecosystem

Keputusan: Mengaktifkan staking HYPE untuk validator security unmittelbar saat TGE (2024-11-29)
· Trigger: Proof-of-Stake security memerlukan stake value dari day-1; HYPE token utility sebagai staking token harus immediate; tidak ada pre-staking period
· Evidence: Phase 3 History (EV-008 TGE HYPE), Phase 6 Token (Utility: Staking, Security, Validator - Status Live since TGE), Phase 4 Technology (Security Model: PoS dengan HYPE staking post-TGE), Phase 1 Foundation (TGE Date 2024-11-29)
· Decision: Staking dan validator economics live at TGE; no delay untuk token utility activation
· Immediate Result: Validator set secured by HYPE stake; staking rewards emission started; network security active
· Long-term Impact: Token value accrual via staking yield; validator set decentralization depends on stake distribution; inflationary pressure dari staking emissions
· Supporting Dataset: Phase 3 EV-008, Phase 4 Technology, Phase 6 Token

---

Evolution Pattern

Dari Phase 1-8, evolusi Hyperliquid mengikuti pola:

1. **Foundation & Core Infra (2022-2023 H1)**: Pendirian Hyperliquid Labs, R&D konsensus HyperBFT custom dan CLOB matching engine di Rust. Fokus teknis murni — no token, no community, no revenue. (Phase 3 EV-001, EV-002)

2. **Validation & Funding (2023 H1)**: Testnet publik berincentiv (Maret 2023) untuk load test CLOB + konsensus; funding round strategis dengan VC + market maker institusional (SIG, GSR) — validasi pasar dan jaminan likuiditas. (Phase 3 EV-003, EV-004)

3. **Product Launch Sequencing (2023 H2)**: Mainnet Perpetual DEX (Mei 2023) → Spot DEX (Oktober 2023) pada L1 yang sama. Phased approach memvalidasi matching engine paling kompleks (perp) dulu. Revenue mulai dari trading fees. (Phase 3 EV-005, EV-006)

4. **Expansion & Modularity (2024)**: Native Bridge (2024) untuk cross-chain liquidity onboarding → HyperEVM Testnet (Nov 2024) untuk EVM execution layer → TGE HYPE (Nov 2024) untuk staking/governance/community ownership → Ecosystem Fund untuk builder grants. Transisi dari single-product appchain ke modular platform. (Phase 3 EV-007, EV-008, EV-009, EV-010)

5. **Governance Formation (2024 ongoing)**: Indikasi Hyperliquid Foundation formation untuk treasury/governance terpisah dari Labs — belum diverifikasi resmi. (Phase 3 EV-011, Phase 2 Entity Hyperliquid Foundation)

Pola evolusi: **Technical-first → Product-sequenced → Modular expansion → Token-activated → Governance formalization**. Setiap phase membangun pada layer sebelumnya tanpa pivot besar.

---

Pola 1: Vertical Integration — Consensus + Matching Engine + Execution Layer Custom-Built
· Decision Pattern: Membangun seluruh stack dari nol (HyperBFT consensus, CLOB matching engine in-consensus, HyperEVM execution layer) alih-alih compose existing frameworks (Cosmos SDK, OP Stack, Arbitrum Orbit, Substrate)
· Evidence: Phase 4 Technology (Consensus Mechanism: HyperBFT custom BFT not Tendermint; Development Framework: Custom Rust framework; System Architecture: Modular custom L1); Phase 1 Foundation (Repository: github.com/hyperliquid-dex Rust repos); Phase 3 History (EV-001 Founding 2022 untuk build custom L1)
· Supporting Dataset: Phase 1 Foundation, Phase 3 EV-001, Phase 4 Technology

Pola 2: Phased Product Rollout — Most Complex First (Perp CLOB → Spot CLOB → HyperEVM)
· Decision Pattern: Meluncurkan produk paling teknis sulit (Perpetual CLOB dengan leverage, funding rate, liquidation engine) pertama, lalu produk lebih sederhana (Spot CLOB), lalu execution layer general-purpose (HyperEVM)
· Evidence: Phase 3 History (EV-005 Perp Mainnet 2023-05-14 → EV-006 Spot Launch 2023-10 → EV-007 HyperEVM Testnet 2024-11); Phase 4 Technology (Core Components: Perpetual DEX CLOB Engine live first, Spot DEX CLOB Engine added, HyperEVM testnet later)
· Supporting Dataset: Phase 3 History, Phase 4 Technology

Pola 3: Performance-Optimized Consensus Design — HyperBFT Custom untuk CLOB
· Decision Pattern: Konsensus dirancang khusus untuk matching engine CLOB (finalitas sub-sekon, throughput tinggi, deterministic ordering) bukan general-purpose BFT
· Evidence: Phase 4 Technology (Consensus Mechanism: HyperBFT custom untuk finalitas sub-sekon dan throughput tinggi, terintegrasi ketat dengan matching engine CLOB); Phase 1 Foundation (Category: On-chain Order Book CLOB); Phase 3 History (EV-002 Internal Testnet Q4 2022 validasi HyperBFT + CLOB)
· Supporting Dataset: Phase 1 Foundation, Phase 3 EV-002, Phase 4 Technology

Pola 4: Modular Execution Layer Addition — HyperEVM sebagai Optional Layer Atas L1
· Decision Pattern: Menambah EVM execution layer (HyperEVM) sebagai modul terpisah di atas L1 consensus yang sudah stable, dengan precompile access ke CLOB native — tidak mengganti core execution
· Evidence: Phase 4 Technology (Execution Environment: HyperEVM EVM-compatible layer di atas Hyperliquid L1; System Architecture: Modular dengan pemisahan konsensus, eksekusi trading, eksekusi smart contract); Phase 3 History (EV-007 HyperEVM Testnet Launch 2024-11); Phase 1 Foundation (Main Products: HyperEVM)
· Supporting Dataset: Phase 1 Foundation, Phase 3 EV-007, Phase 4 Technology

Pola 5: Native Bridge dengan Trusted Validator Set — Simplicity Over Trust-Minimization
· Decision Pattern: Bridge native menggunakan validator set yang sama dengan consensus (trusted model) untuk speed to market dan operational simplicity, bukan light client/ZK bridge
· Evidence: Phase 4 Technology (Core Components: Hyperliquid Bridge native; Bridge Security: trusted validator set model); Phase 3 History (EV-009 Bridge Launch 2024); Phase 7 Ecosystem (External Dependencies: Arbitrum, Ethereum; Major Integrations: Native Bridge; Ecosystem Risks: Single Bridge Dependency)
· Supporting Dataset: Phase 3 EV-009, Phase 4 Technology, Phase 7 Ecosystem

Pola 6: Rust-First Development — Core Infrastructure dalam Rust, EVM Tooling untuk HyperEVM
· Decision Pattern: Core blockchain (consensus, matching engine, networking) ditulis dalam Rust untuk performance dan safety; HyperEVM menggunakan standard Ethereum tooling (Foundry, Hardhat, Solidity/Vyper)
· Evidence: Phase 4 Technology (Programming Languages: Rust utama untuk L1 node, HyperBFT, CLOB engine; Solidity/Vyper untuk HyperEVM; Development Framework: Custom Rust framework, Foundry/Hardhat untuk HyperEVM); Phase 1 Foundation (Repository: github.com/hyperliquid-dex Rust repos)
· Supporting Dataset: Phase 1 Foundation, Phase 4 Technology

---

Pola 1: Single Strategic Funding Round dengan Investor-Market Maker Overlap (2023)
· Decision Pattern: Satu ronde pendanaan besar (Series A/Strategic 2023) dari VC (Variant, Delphi, Hack VC) + market maker institusional (SIG, GSR) yang juga commit liquidity — no follow-on rounds publik, no public token sale
· Evidence: Phase 5 Financial (Funding History: 1 round 2023, Amount undisclosed; Fundraising Mechanism: VC Funding); Phase 2 Entity (Variant Fund, Delphi Digital, Hack VC, SIG, GSR as Investors); Phase 3 History (EV-004 Funding Round 2023); Phase 7 Ecosystem (External Dependencies: SIG, GSR as Market Makers)
· Supporting Dataset: Phase 2 Entity, Phase 3 EV-004, Phase 5 Financial, Phase 7 Ecosystem

Pola 2: Revenue Model = Pure Protocol Fees (Trading Fees Perp + Spot + Bridge) — No Fee Switch Yet
· Decision Pattern: Pendapatan sepenuhnya dari trading fees (perp & spot CLOB) dan bridge fees; fee switch / revenue sharing ke staker HYPE diumumkan tapi belum diaktifkan
· Evidence: Phase 5 Financial (Revenue Model: Protocol Fees Perp DEX Live, Spot DEX Live, Bridge Fees Live, Fee Switch Planned/Not Activated); Phase 1 Foundation (Main Products: Perp DEX, Spot DEX, Bridge); Phase 4 Technology (Core Components: Perp DEX, Spot DEX, Bridge); Phase 6 Token (Utility: Fee Payment Live, Reward Live via staking emission, Fee Switch not mentioned)
· Supporting Dataset: Phase 1 Foundation, Phase 4 Technology, Phase 5 Financial, Phase 6 Token

Pola 3: Token Distribution via Community Airdrop/Points — No Public/Private Token Sale
· Decision Pattern: TGE HYPE 100% community distribution (airdrop/points claim) tanpa IDO/launchpad/private token sale; investor allocation via equity/SAFT terpisah dari token distribution
· Evidence: Phase 5 Financial (Token Sale: No private/public sale, Community Distribution via airdrop/points); Phase 3 History (EV-008 TGE HYPE); Phase 6 Token (TGE Date 2024-11-29, Launch Platform: Native Hyperliquid L1, Distribution: Community Planned); Phase 1 Foundation (TGE Date 2024-11-29)
· Supporting Dataset: Phase 1 Foundation, Phase 3 EV-008, Phase 5 Financial, Phase 6 Token

Pola 4: Treasury & Tokenomics Opacity — No Public Disclosure
· Decision Pattern: Ukuran treasury, komposisi, tokenomics detail (alokasi team/investor/foundation/ecosystem), emission schedule, vesting schedule — semuanya tidak dipublikasikan; whitepaper tokenomics belum terbit
· Evidence: Phase 5 Financial (Treasury: Current Treasury Size undisclosed, Composition undisclosed; Financial Risk: Treasury Concentration Risk); Phase 6 Token (Supply: Max/Total/Circulating/Initial all unknown; Distribution: all categories Planned percentages unknown; Vesting Schedule: all categories unknown; Inflation: emission schedule unknown; Governance: proposal system unknown); Phase 1 Foundation (Open Threads: tokenomics detail, fee switch, foundation legal relation)
· Supporting Dataset: Phase 5 Financial, Phase 6 Token, Phase 1 Foundation

Pola 5: Ecosystem Fund Announced Post-TGE untuk HyperEVM Builder Grants
· Decision Pattern: Dana ekosistem (Ecosystem Fund) diannounce 2024 setelah TGE untuk mendukung developer membangun di HyperEVM — sumber dana tidak transparan (token allocation? treasury? revenue?)
· Evidence: Phase 3 History (EV-010 Ecosystem Fund Announcement 2024); Phase 5 Financial (Fundraising Mechanism: Ecosystem Fund/Builder Grants); Phase 7 Ecosystem (Developer Ecosystem: Grant Program: Hyperliquid Ecosystem Fund/Builder Grants); Phase 1 Foundation (Official Blog Ecosystem Fund)
· Supporting Dataset: Phase 3 EV-010, Phase 5 Financial, Phase 7 Ecosystem, Phase 1 Foundation

Pola 6: Staking Rewards sebagai Primary Token Emission Mechanism — Inflationary by Design
· Decision Pattern: HYPE supply inflationary melalui staking rewards/validator emission; no burn mechanism, no buyback announced; fee switch status unknown
· Evidence: Phase 6 Token (Supply Type: Inflationary staking rewards/validator emissions active post-TGE; Inflation Mechanism: staking rewards/validator emission; Burn Mechanism: none announced; Buyback: none announced); Phase 3 History (EV-008 TGE activates staking); Phase 4 Technology (Security Model: PoS dengan HYPE staking post-TGE)
· Supporting Dataset: Phase 3 EV-008, Phase 4 Technology, Phase 6 Token

---

Pola 1: Strategic Investor = Market Maker — SIG & GSR Dual Role
· Decision Pattern: Market maker institusional tier-1 (Susquehanna SIG, GSR) berperan ganda sebagai investor (funding round 2023) dan penyedia likuiditas utama di Perpetual DEX
· Evidence: Phase 2 Entity (SIG, GSR as Investors); Phase 3 History (EV-004 Funding Round 2023 includes SIG, GSR); Phase 5 Financial (Financial Dependencies: SIG, GSR as Market Makers); Phase 7 Ecosystem (External Dependencies: SIG, GSR as Service/Market Maker; Major Integrations: Institutional Market Makers)
· Supporting Dataset: Phase 2 Entity, Phase 3 EV-004, Phase 5 Financial, Phase 7 Ecosystem

Pola 2: USDC sebagai Settlement Layer Utama — Bridge ke Arbitrum/Ethereum untuk Onboarding
· Decision Pattern: Seluruh trading economy (perp & spot) menggunakan USDC sebagai collateral/quote asset; Native bridge ke Arbitrum dan Ethereum mainnet dibangun untuk mengimpor USDC liquidity
· Evidence: Phase 4 Technology (Core Components: Hyperliquid Bridge to Arbitrum/Ethereum); Phase 7 Ecosystem (External Dependencies: USDC critical, Arbitrum critical, Ethereum critical; Major Integrations: Native Bridge to Arbitrum/Ethereum); Phase 5 Financial (Revenue Model: fees denominated in USDC implied); Phase 1 Foundation (Products: Perp/Spot DEX)
· Supporting Dataset: Phase 4 Technology, Phase 5 Financial, Phase 7 Ecosystem, Phase 1 Foundation

Pola 3: HyperEVM sebagai Developer Onboarding Strategy — EVM Compatibility + CLOB Primitive
· Decision Pattern: HyperEVM testnet + Ecosystem Fund grants untuk menarik Ethereum developers dengan tooling familiar (Solidity, Foundry, Hardhat) sambil menawarkan CLOB native sebagai primitive unik yang tidak ada di L1/L2 lain
· Evidence: Phase 3 History (EV-007 HyperEVM Testnet, EV-010 Ecosystem Fund); Phase 4 Technology (Core Components: HyperEVM, Execution Environment: HyperEVM); Phase 7 Ecosystem (Developer Ecosystem: HyperEVM testnet, Grant Program; Applications: HyperEVM dApps Testnet); Phase 1 Foundation (Main Products: HyperEVM)
· Supporting Dataset: Phase 3 EV-007 EV-010, Phase 4 Technology, Phase 7 Ecosystem, Phase 1 Foundation

Pola 4: Native Block Explorer Ecosystem — Hypurrscan sebagai Primary, Official Explorer sebagai Backup
· Decision Pattern: Hypurrscan (independent team) menjadi primary explorer; official explorer (explorer.hyperliquid.xyz) sebagai backup — tidak mengembangkan explorer in-house
· Evidence: Phase 4 Technology (Core Components: Hypurrscan/Official Explorer); Phase 7 Ecosystem (Infrastructure Providers: Hypurrscan independent, Official Explorer; Applications: Hypurrscan); Phase 1 Foundation (Block Explorer: Hypurrscan utama, explorer.hyperliquid.xyz resmi)
· Supporting Dataset: Phase 1 Foundation, Phase 4 Technology, Phase 7 Ecosystem

Pola 5: Cloud Infrastructure Dependency Tidak Diungkap — Validator & API Hosting Centralization Risk
· Decision Pattern: Validator nodes, RPC endpoints, API services kemungkinan besar hosted di cloud provider major (AWS/GCP/Azure) tapi tidak di-disclose — menciptakan single point of failure risk
· Evidence: Phase 7 Ecosystem (External Dependencies: Cloud Infrastructure Providers inferred; Infrastructure Providers: Cloud Providers unspecified; Ecosystem Risks: Cloud Infrastructure Centralization); Phase 4 Technology (Current Technical Stack: Docker/Kubernetes inferred, no explicit cloud disclosure)
· Supporting Dataset: Phase 4 Technology, Phase 7 Ecosystem

---

Pola 1: Token-Based Governance dengan Staking-Weighted Voting — Infrastructure Belum Lengkap
· Decision Pattern: Governance model dirancang token-based (HYPE staked/delegated = voting power) tapi proposal system, forum, voting mechanism, execution framework belum dipublikasikan/resmi launch
· Evidence: Phase 6 Token (Governance Model: Token-based governance, Voting Power proportional to HYPE staked, Delegation supported, Proposal System unknown, Treasury Governance: Hyperliquid Foundation indicated); Phase 3 History (EV-011 Foundation Formation indicated); Phase 2 Entity (Hyperliquid Foundation indicated); Phase 1 Foundation (Open Threads: governance framework, foundation legal relation)
· Supporting Dataset: Phase 1 Foundation, Phase 2 Entity, Phase 3 EV-011, Phase 6 Token

Pola 2: Foundation Formation Separate dari Labs — Governance Entity Terpisah
· Decision Pattern: Indikasi pembentukan Hyperliquid Foundation sebagai entitas governance/treasury terpisah dari Hyperliquid Labs (developer company) — tapi yurisdiksi, struktur hukum, hubungan formal belum diverifikasi
· Evidence: Phase 2 Entity (Hyperliquid Foundation type Foundation, Relationship: governance entity terpisah, Exposure: unknown); Phase 3 History (EV-011 Foundation Formation indicated 2024); Phase 6 Token (Treasury Governance: managed by Hyperliquid Foundation indicated); Phase 1 Foundation (Open Threads: legal relation Labs vs Foundation)
· Supporting Dataset: Phase 2 Entity, Phase 3 EV-011, Phase 6 Token, Phase 1 Foundation

Pola 3: No Formal DAO Structure — Governance via Foundation + Token Voting (Planned)
· Decision Pattern: Tidak ada DAO formal (snapshot, governor contracts, timelock) yang diumumkan; governance akan melalui Foundation + token voting on-chain (HyperEVM precompile atau native L1 governance module)
· Evidence: Phase 6 Token (Governance: Voting System unknown, Proposal System unknown, no governance forum); Phase 7 Ecosystem (Governance Ecosystem: DAO tidak ada formal, Council/Committee tidak diumumkan); Phase 2 Entity (Hyperliquid Foundation indicated)
· Supporting Dataset: Phase 2 Entity, Phase 6 Token, Phase 7 Ecosystem

Pola 4: Validator Set sebagai Governance Actor Implisit — Consensus Participation = Network Governance
· Decision Pattern: Validator set (permissioned/permissionless unclear) mengontrol consensus upgrades, bridge operations, parameter changes — de facto governance power sebelum formal token governance live
· Evidence: Phase 4 Technology (Core Components: Validator Set; Security Model: Validator Security PoS dengan HYPE staking); Phase 7 Ecosystem (Governance Ecosystem: Validator Group: Hyperliquid Validator Set; Ecosystem Risks: Centralized Validator Set); Phase 2 Entity (Hyperliquid L1 as Organization running validator set)
· Supporting Dataset: Phase 2 Entity, Phase 4 Technology, Phase 7 Ecosystem

---

Pola 1: Single Bridge Dependency — No Trust-Minimized Alternative Live
· Decision Pattern: Mengandalkan single native bridge (trusted validator set) untuk semua cross-chain transfers; no light client bridge, no ZK bridge, no IBC live — bridge risk = protocol risk
· Evidence: Phase 7 Ecosystem (External Dependencies: Arbitrum, Ethereum critical for bridge; Ecosystem Risks: Single Bridge Dependency High); Phase 4 Technology (Core Components: Hyperliquid Bridge native trusted model); Phase 3 History (EV-009 Bridge Launch 2024)
· Trigger: Perlu cross-chain liquidity onboarding cepat; trust-minimized bridge R&D butuh waktu
· Response: Launch native bridge first; trust-minimized alternatives tidak diroadmap publik
· Result: Cross-chain USDC flow live; bridge centralization risk accepted
· Supporting Dataset: Phase 3 EV-009, Phase 4 Technology, Phase 7 Ecosystem

Pola 2: USDC Concentration Risk — No Alternative Collateral/Stablecoin Live
· Decision Pattern: 100% trading economy bergantung pada USDC; no native stablecoin, no multi-collateral support, no diversification — Circle/USDC regulatory risk = protocol risk
· Evidence: Phase 7 Ecosystem (External Dependencies: USDC critical; Ecosystem Risks: USDC Collateral Concentration High); Phase 5 Financial (Revenue Model: fees in USDC implied); Phase 4 Technology (Core Components: Perp/Spot DEX using USDC)
· Trigger: USDC adalah stablecoin paling liquid dan trusted di DeFi; multi-collateral complexity tinggi untuk CLOB
· Response: Focus pada USDC-only untuk simplicity dan liquidity depth
· Result: Deep liquidity di USDC pairs; single point of failure jika USDC depeg/blacklist
· Supporting Dataset: Phase 4 Technology, Phase 5 Financial, Phase 7 Ecosystem

Pola 3: Market Maker Dependency — SIG & GSR sebagai Liquidity Backbone
· Decision Pattern: Likuiditas CLOB sangat bergantung pada 2 market maker institusional; withdrawal salah satu akan mengurangi order book depth drastis
· Evidence: Phase 7 Ecosystem (External Dependencies: SIG, GSR High criticality; Ecosystem Risks: Market Maker Dependency High); Phase 2 Entity (SIG, GSR as Investors/Market Makers); Phase 5 Financial (Financial Dependencies: SIG, GSR)
· Trigger: Bootstrapping CLOB liquidity butuh professional market makers; retail liquidity insufficient untuk tight spreads
· Response: Strategic partnership dengan SIG/GSR via funding round + market making agreement
· Result: Deep liquidity dari day-1 mainnet; concentration risk accepted
· Supporting Dataset: Phase 2 Entity, Phase 3 EV-004, Phase 5 Financial, Phase 7 Ecosystem

Pola 4: Regulatory Exposure — Perpetual DEX + BVI Entity + Global Access
· Decision Pattern: Operasi perpetual futures DEX (derivatives) dari entitas BVI tanpa geo-blocking resmi — exposed ke CFTC, SEC, FCA enforcement; no public compliance framework
· Evidence: Phase 7 Ecosystem (Ecosystem Risks: Regulatory Exposure High); Phase 5 Financial (Financial Risk: Regulatory Financial Risk High); Phase 1 Foundation (Country: BVI entity; Open Threads: regulatory classification); Phase 3 History (EV-005 Perp DEX Mainnet global access)
· Trigger: Global permissionless access = core value prop; compliance cost tinggi dan membatasi user base
· Response: Launch global permissionless; monitor regulatory landscape; no public geo-blocking announcement
· Result: Global user base acquired; regulatory tail risk remains
· Supporting Dataset: Phase 1 Foundation, Phase 3 EV-005, Phase 5 Financial, Phase 7 Ecosystem

Pola 5: No Formal Security Audits — Core Protocol Unaudited Publicly
· Decision Pattern: HyperBFT consensus, CLOB matching engine, native bridge contracts — no public audit reports dari auditor tier-1; security model berg

## Knowledge Extraction
_ref: `docs/Patterns/*`, `docs/Reasoning/*` (rule candidates)_

PROJECT: Hyperliquid

Core Insights

Insight 1: Vertical Integration Membuat Moat Teknis yang Sulit Direplikasi
Explanation: Hyperliquid membangun seluruh stack dari nol — konsensus HyperBFT custom, matching engine CLOB di dalam konsensus, dan HyperEVM sebagai execution layer terpisah — tanpa menggunakan framework existing (Cosmos SDK, OP Stack, Substrate, Tendermint). Integrasi vertikal ini memungkinkan optimasi performa (finalitas sub-sekon, throughput tinggi) yang spesifik untuk trading CLOB on-chain, menciptakan barrier to entry teknis yang tinggi bagi kompetitor.
Evidence: Konsensus HyperBFT custom bukan Tendermint/CometBFT【Phase 4 — Consensus Mechanism】; Development framework custom Rust bukan Cosmos SDK/Substrate/OP Stack【Phase 4 — Development Framework】; Arsitektur modular terpisah konsensus, eksekusi trading, eksekusi smart contract【Phase 4 — System Architecture】; Repository GitHub menunjukkan codebase Rust murni untuk core【Phase 1 — Repository】.
Supporting Dataset: Phase 1 Foundation, Phase 4 Technology
Confidence: HIGH

Insight 2: Phased Product Rollout Mengurangi Risiko Eksekusi Kompleks
Explanation: Meluncurkan Perpetual DEX (produk paling kompleks: leverage, funding rate, liquidation engine) terlebih dahulu pada Mei 2023, lalu Spot DEX Oktober 2023, baru HyperEVM testnet November 2024. Pendekatan bertahap memvalidasi matching engine paling sulit dahulu, membangun revenue stream awal, dan memperluas use case secara progresif tanpa pivot besar.
Evidence: Mainnet Perp DEX 2023-05-14【Phase 3 — EV-005】; Spot DEX launch 2023-10【Phase 3 — EV-006】; HyperEVM testnet 2024-11【Phase 3 — EV-007】; Core components perp live first, spot added later, HyperEVM testnet later【Phase 4 — Core Components】.
Supporting Dataset: Phase 3 History, Phase 4 Technology
Confidence: HIGH

Insight 3: Strategic Investor = Market Maker Alignment Mengurangi Cold Start Liquidity Problem
Explanation: Ronde funding 2023 melibatkan market maker institusional tier-1 (SIG, GSR) sebagai investor sekaligus liquidity provider. Dual role ini menjamin kedalaman order book sejak day-1 mainnet, mengatasi chicken-and-egg problem CLOB (butuh likuiditas untuk menarik trader, butuh trader untuk menarik likuiditas).
Evidence: SIG dan GSR tercatat sebagai investor di funding round 2023【Phase 2 — Entity: SIG, GSR】; Funding round EV-004 mencantumkan SIG, GSR【Phase 3 — EV-004】; Financial dependencies mencatat SIG, GSR sebagai market maker【Phase 5 — Financial Dependencies】; External dependencies criticality High untuk SIG, GSR【Phase 7 — External Dependencies】.
Supporting Dataset: Phase 2 Entity, Phase 3 History, Phase 5 Financial, Phase 7 Ecosystem
Confidence: HIGH

Insight 4: Community-First Token Distribution Tanpa Public Sale Membangun Legitimasi Governance Awal
Explanation: TGE HYPE 29 November 2024 menggunakan airdrop/points claim untuk pengguna aktif (testnet/mainnet) tanpa private/public token sale, IDO, atau launchpad. Distribusi ini menciptakan holder base yang aligned dengan usage protokol, menghindari tekanan jual awal dari investor token, dan mengurangi risiko regulasi securities.
Evidence: TGE date 2024-11-29【Phase 3 — EV-008】; Token sale: no private/public sale, community distribution via airdrop/points【Phase 5 — Token Sale】; TGE launch platform native Hyperliquid L1【Phase 6 — TGE】; Distribution community planned via airdrop/points【Phase 6 — Distribution】.
Supporting Dataset: Phase 3 History, Phase 5 Financial, Phase 6 Token
Confidence: HIGH

Insight 5: Tokenomics Opacity Menciptakan Ketidakpastian Nilai Jangka Panjang
Explanation: Seluruh parameter tokenomics (max supply, total supply, circulating supply, alokasi per kategori, vesting schedule, emission rate, fee switch mechanism) tidak dipublikasikan. Whitepaper tokenomics tidak ada. Ketidaktransparanan ini menyulitkan valuasi fundamental, perencanaan staker, dan kepercayaan institusional.
Evidence: Supply max/total/circulating/initial all unknown【Phase 6 — Supply】; Distribution all categories planned percentages unknown【Phase 6 — Distribution】; Vesting schedule all categories unknown【Phase 6 — Vesting Schedule】; Inflation emission schedule unknown, no burn/buyback announced【Phase 6 — Inflation/Deflation】; Treasury size/composition undisclosed【Phase 5 — Treasury】; Open threads tokenomics detail【Phase 1 — Open Threads】.
Supporting Dataset: Phase 1 Foundation, Phase 5 Financial, Phase 6 Token
Confidence: HIGH

Insight 6: Single Trusted Bridge + USDC Concentration = Systemic Risk Tinggi
Explanation: Semua cross-chain transfer bergantung pada single native bridge (trusted validator set model) ke Arbitrum/Ethereum. Seluruh trading economy menggunakan USDC sebagai collateral/quote asset tunggal. Tidak ada bridge trust-minimized (light client/ZK/IBC) live, tidak ada multi-collateral support. Kegagalan bridge atau USDC depeg/blacklist = protocol failure.
Evidence: Bridge native trusted validator set model【Phase 4 — Core Components: Hyperliquid Bridge】; Bridge security trusted validator set【Phase 4 — Security Model】; Single bridge dependency risk High【Phase 7 — Ecosystem Risks】; USDC critical dependency High【Phase 7 — External Dependencies】; USDC collateral concentration risk High【Phase 7 — Ecosystem Risks】; No trust-minimized alternative live【Phase 9 — Risk Response Pattern 1】.
Supporting Dataset: Phase 4 Technology, Phase 7 Ecosystem, Phase 9 Behavioral
Confidence: HIGH

Insight 7: Governance Infrastructure Tertinggal dari Token Launch
Explanation: Token HYPE live dengan staking dan fee payment sejak TGE November 2024, tapi governance infrastructure (proposal system, voting mechanism, forum, execution framework, timelock/multisig treasury) belum lengkap. Foundation formation diindikasikan tapi tidak diverifikasi resmi. Validator set mengontrol consensus upgrades dan bridge operations sebagai de facto governance sebelum formal token governance live.
Evidence: Governance model token-based planned, proposal system unknown【Phase 6 — Governance】; Foundation formation indicated not verified【Phase 3 — EV-011】; No formal DAO structure【Phase 7 — Governance Ecosystem】; Validator set as implicit governance actor【Phase 9 — Governance Pattern 4】; Staking live at TGE, governance infra incomplete【Phase 9 — Decision: Staking activated at TGE】.
Supporting Dataset: Phase 3 History, Phase 6 Token, Phase 7 Ecosystem, Phase 9 Behavioral
Confidence: HIGH

Insight 8: No Formal Security Audits pada Core Protocol Meningkatkan Tail Risk
Explanation: HyperBFT consensus, CLOB matching engine, dan native bridge contracts tidak memiliki laporan audit publik dari auditor tier-1. Security model bergantung pada code review internal dan battle-testing di mainnet. Untuk protokol yang mengelola ratusan juta USD TVL dan perpetual futures, absensi audit formal adalah celah kepercayaan besar.
Evidence: Audit history: tidak diketahui audit formal publik【Phase 4 — Audit History】; No audit reports di GitHub/docs【Phase 4 — Audit History】; Ecosystem risk: no formal security audits High【Phase 7 — Ecosystem Risks】; Risk response: no formal audits accepted【Phase 9 — Risk Response Pattern 5】.
Supporting Dataset: Phase 4 Technology, Phase 7 Ecosystem, Phase 9 Behavioral
Confidence: HIGH

Insight 9: HyperEVM sebagai Developer Onboarding Strategy Memanfaatkan EVM Compatibility + CLOB Primitive
Explanation: HyperEVM testnet + Ecosystem Fund grants menarik Ethereum developers dengan tooling familiar (Solidity, Foundry, Hardhat) sambil menawarkan CLOB native sebagai primitive unik (precompile access) yang tidak ada di L1/L2 lain. Strategi ini mengubah Hyperliquid dari appchain trading-only menjadi modular platform untuk DeFi composability.
Evidence: HyperEVM testnet launch EV-007【Phase 3 — EV-007】; Ecosystem Fund announcement EV-010【Phase 3 — EV-010】; HyperEVM EVM-compatible execution layer dengan precompile access CLOB【Phase 4 — Core Components: HyperEVM】; Developer ecosystem: HyperEVM testnet, grant program【Phase 7 — Developer Ecosystem】; Narrative: EVM-compatible/chain abstraction emerging【Phase 8 — Narrative Position】.
Supporting Dataset: Phase 3 History, Phase 4 Technology, Phase 7 Ecosystem, Phase 8 Market
Confidence: HIGH

Insight 10: Regulatory Exposure Perpetual DEX + BVI Entity + Global Permissionless Access = Tail Risk Terbuka
Explanation: Hyperliquid Labs (BVI) mengoperasikan perpetual futures DEX (derivatives) secara global tanpa geo-blocking resmi. Terpapar risiko enforcement CFTC, SEC, FCA, dll yang dapat membatasi akses pengguna, menyita aset, atau memaksa shutdown. Tidak ada compliance framework publik yang diumumkan.
Evidence: Country BVI entity【Phase 1 — Foundation】; Regulatory financial risk High【Phase 5 — Financial Risk】; Ecosystem risk regulatory exposure High【Phase 7 — Ecosystem Risks】; Risk response: launch global permissionless, monitor landscape, no geo-blocking announcement【Phase 9 — Risk Response Pattern 4】; Open threads regulatory classification【Phase 1 — Open Threads】.
Supporting Dataset: Phase 1 Foundation, Phase 5 Financial, Phase 7 Ecosystem, Phase 9 Behavioral
Confidence: HIGH

Strategic Principles

Principle 1: Performance-First Architecture Over Composability Standards
Explanation: Memilih custom L1 dengan konsensus HyperBFT dan CLOB in-consensus alih-alih deploy di L1/L2 existing (Ethereum, Solana, Arbitrum, Cosmos) untuk mencapai finalitas sub-sekon dan throughput yang diperlukan trading professional. Sovereign control over consensus parameters, gas model, upgrade path diprioritaskan rather than standards compliance.
Evidence: Custom HyperBFT consensus bukan Tendermint【Phase 4 — Consensus Mechanism】; Custom Rust framework bukan Cosmos SDK/Substrate/OP Stack【Phase 4 — Development Framework】; Appchain khusus trading bukan general-purpose L1【Phase 1 — Category】; Decision: build custom L1 from scratch【Phase 9 — Decision: Custom L1】.
Supporting Dataset: Phase 1 Foundation, Phase 4 Technology, Phase 9 Behavioral
Confidence: HIGH

Principle 2: Most Complex Product First — Validasi Teknis Terberat Dahulu
Explanation: Meluncurkan Perpetual DEX (leverage, funding rate, liquidation, CLOB matching) sebelum Spot DEX dan HyperEVM. Validasi matching engine paling kompleks di production terlebih dahulu mengurangi risiko bug fundamental di layer yang menjadi foundation seluruh stack.
Evidence: Perp mainnet 2023-05-14 → Spot 2023-10 → HyperEVM testnet 2024-11【Phase 3 — EV-005, EV-006, EV-007】; Phased product rollout pattern【Phase 9 — Evolution Pattern】; Decision: phased launch perp first【Phase 9 — Decision: Perp first then Spot】.
Supporting Dataset: Phase 3 History, Phase 9 Behavioral
Confidence: HIGH

Principle 3: Strategic Capital + Operational Partnerships dalam Satu Ronde
Explanation: Satu ronde funding (2023) menggabungkan VC strategis (Variant, Delphi, Hack VC) untuk capital + market maker institusional (SIG, GSR) untuk liquidity commitment. Menghindari multiple rounds dilution dan memastikan day-1 liquidity depth.
Evidence: Funding round 2023 termasuk SIG, GSR sebagai investor【Phase 2 — Entity: SIG, GSR】; Financial dependencies SIG, GSR sebagai market maker【Phase 5 — Financial Dependencies】; Decision: private equity/SAFT dengan strategic investors yang juga market maker【Phase 9 — Decision: Funding from VC+MM】; Single strategic funding round pattern【Phase 9 — Financial Pattern 1】.
Supporting Dataset: Phase 2 Entity, Phase 5 Financial, Phase 9 Behavioral
Confidence: HIGH

Principle 4: Token as Network Security & Alignment Tool, Not Fundraising Vehicle
Explanation: HYPE tidak dijual via public/private sale. Didistribusikan ke komunitas (airdrop/points) untuk alignment jangka panjang, lalu digunakan untuk staking (PoS security), fee payment, governance. Token utility immediate at TGE (staking live), bukan speculative asset.
Evidence: No token sale, community distribution via airdrop/points【Phase 5 — Token Sale】; TGE activates staking immediately【Phase 3 — EV-008】; Utility: staking, governance, fee payment, security, validator, incentive, reward【Phase 6 — Utility】; Decision: fair launch style distribution【Phase 9 — Decision: TGE via airdrop】.
Supporting Dataset: Phase 3 History, Phase 5 Financial, Phase 6 Token, Phase 9 Behavioral
Confidence: HIGH

Principle 5: Modular Expansion After Core Stability — HyperEVM sebagai Optional Layer
Explanation: Menambahkan HyperEVM (EVM execution layer) sebagai modul terpisah di atas L1 consensus yang sudah stable (mainnet 1.5 tahun), dengan precompile access ke CLOB native. Tidak mengganti core execution, tidak memecah konsensus. Memungkinkan developer Ethereum onboard tanpa mengganggu trading engine.
Evidence: HyperEVM testnet 2024-11 setelah mainnet 2023-05【Phase 3 — EV-005, EV-007】; Modular architecture: consensus, trading execution, smart contract execution terpisah【Phase 4 — System Architecture】; Execution environment HyperEVM di atas L1【Phase 4 — Execution Environment】; Decision: modular execution layer addition【Phase 9 — Decision: HyperEVM testnet】; Pattern: modular execution layer addition【Phase 9 — Evolution Pattern 4】.
Supporting Dataset: Phase 3 History, Phase 4 Technology, Phase 9 Behavioral
Confidence: HIGH

Principle 6: Trusted Bridge First, Trust-Minimized Later (If Ever)
Explanation: Native bridge menggunakan validator set yang sama dengan consensus (trusted model) untuk speed to market dan operational simplicity. Mengakui centralization risk tapi memprioritaskan cross-chain liquidity onboarding cepat (USDC dari Arbitrum/Ethereum). Trust-minimized alternatives (light client/ZK/IBC) tidak diroadmap publik.
Evidence: Bridge native trusted validator set model【Phase 4 — Core Components: Hyperliquid Bridge】; Bridge security trusted validator set【Phase 4 — Security Model】; Bridge launch 2024【Phase 3 — EV-009】; Decision: native bridge trusted model【Phase 9 — Decision: Native bridge trusted】; Risk response: single bridge dependency accepted【Phase 9 — Risk Response Pattern 1】.
Supporting Dataset: Phase 3 History, Phase 4 Technology, Phase 9 Behavioral
Confidence: HIGH

Principle 7: Rust-First Core, Standard Tooling untuk Extension Layer
Explanation: Core blockchain (consensus, matching engine, networking) ditulis dalam Rust untuk performance dan memory safety. HyperEVM menggunakan standard Ethereum tooling (Foundry, Hardhat, Solidity/Vyper) untuk developer familiarity. Pemisahan bahasa sesuai layer: Rust untuk performance-critical, Solidity untuk composability layer.
Evidence: Programming languages: Rust utama untuk L1 node, HyperBFT, CLOB engine; Solidity/Vyper untuk HyperEVM【Phase 4 — Programming Languages】; Development framework: custom Rust framework, Foundry/Hardhat untuk HyperEVM【Phase 4 — Development Framework】; Repository GitHub Rust repos【Phase 1 — Repository】; Pattern: Rust-first development【Phase 9 — Technical Pattern 6】.
Supporting Dataset: Phase 1 Foundation, Phase 4 Technology, Phase 9 Behavioral
Confidence: HIGH

Success Factors

Factor 1: Technical Differentiation via Fully On-Chain CLOB dengan Performa CEX-Setara
Explanation: Hyperliquid adalah perp DEX pertama dengan CLOB on-chain penuh (matching engine di dalam konsensus) yang mencapai finalitas sub-sekon dan throughput tinggi via HyperBFT custom. Ini menciptakan UX trading setara CEX (tight spreads, deep liquidity, low latency) tanpa kstodian sentral — unique selling proposition yang menarik trader profesional dan volume signifikan.
Evidence: Perpetual DEX CLOB on-chain native【Phase 1 — Main Products】; HyperBFT custom untuk finalitas sub-sekon【Phase 4 — Consensus Mechanism】; CLOB matching engine in consensus【Phase 4 — Core Components】; Narrative: on-chain CLOB main narrative【Phase 8 — Narrative Position】; Competitor differentiation vs GMX (AMM), Aevo (off-chain matching)【Phase 8 — Competitor Landscape】.
Supporting Dataset: Phase 1 Foundation, Phase 4 Technology, Phase 8 Market
Confidence: HIGH

Factor 2: Institutional-Grade Liquidity dari Day-1 via Strategic Market Maker Partnerships
Explanation: SIG dan GSR sebagai investor + market maker menjamin order book depth, tight spreads, dan reliable liquidity sejak mainnet launch. Ini memecahkan cold start problem CLOB dan menarik trader institutional/retail yang butuh execution quality tinggi.
Evidence: SIG, GSR investor di funding round 2023【Phase 2 — Entity: SIG, GSR】; Market maker di Perpetual DEX【Phase 7 — External Dependencies】; Financial dependencies SIG, GSR【Phase 5 — Financial Dependencies】; Decision: strategic investor = market maker【Phase 9 — Decision: Funding from VC+MM】; Pattern: investor-MM dual role【Phase 9 — Ecosystem Pattern 1】.
Supporting Dataset: Phase 2 Entity, Phase 5 Financial, Phase 7 Ecosystem, Phase 9 Behavioral
Confidence: HIGH

Factor 3: Community Ownership via Fair Launch Token Distribution
Explanation: TGE via airdrop/points ke pengguna aktif (bukan token sale) menciptakan holder base yang aligned dengan protocol usage, membangun goodwill komunitas, menghindari regulatory risk token sale, dan memberikan legitimasi governance dari awal.
Evidence: TGE community airdrop/points【Phase 3 — EV-008】; No private/public sale【Phase 5 — Token Sale】; Distribution community planned【Phase 6 — Distribution】; Decision: fair launch style distribution【Phase 9 — Decision: TGE via airdrop】; Pattern: community airdrop distribution【Phase 9 — Financial Pattern 3】.
Supporting Dataset: Phase 3 History, Phase 5 Financial, Phase 6 Token, Phase 9 Behavioral
Confidence: HIGH

Factor 4: Sovereign L1 Memungkinkan Full Control Over Economics & Upgrades
Explanation: Custom L1 memberikan kontrol penuh atas gas model (HYPE as gas), consensus parameters, upgrade path, dan integrasi CLOB tanpa bergantung pada roadmap L1 lain (Ethereum gas spikes, Solana outages, Arbitrum sequencer). Fleksibilitas ini krusial untuk trading infrastructure.
Evidence: Hyperliquid L1 sovereign custom【Phase 1 — Category】; Native gas token HYPE【Phase 6 — Utility: Fee Payment】; Custom consensus HyperBFT【Phase 4 — Consensus Mechanism】; Decision: custom L1 untuk sovereign control【Phase 9 — Decision: Custom L1】; Narrative: appchain/application-specific blockchain【Phase 8 — Narrative Position】.
Supporting Dataset: Phase 1 Foundation, Phase 4 Technology, Phase 6 Token, Phase 8 Market, Phase 9 Behavioral
Confidence: HIGH

Factor 5: Modular Architecture Memungkinkan Ekspansi Tanpa Mengganggu Core
Explanation: Pemisahan konsensus (HyperBFT), trading execution (CLOB), dan smart contract execution (HyperEVM) memungkinkan HyperEVM testnet diluncurkan tanpa mengganggu perp/spot DEX yang sudah live. Developer Ethereum dapat onboard ke HyperEVM sementara trading engine tetap stable.
Evidence: Modular architecture separation【Phase 4 — System Architecture】; HyperEVM testnet launch setelah mainnet stable【Phase 3 — EV-005, EV-007】; Core components terpisah【Phase 4 — Core Components】; Pattern: modular execution layer addition【Phase 9 — Technical Pattern 4】.
Supporting Dataset: Phase 3 History, Phase 4 Technology, Phase 9 Behavioral
Confidence: HIGH

Factor 6: Rust Codebase Memberikan Safety & Performance untuk Financial Infrastructure
Explanation: Core infrastructure (consensus, matching engine) ditulis dalam Rust memberikan memory safety, concurrency safety, dan performance deterministik — krusial untuk financial infrastructure yang menangani high-value transactions dan memerlukan uptime tinggi.
Evidence: Rust utama untuk L1 node, HyperBFT, CLOB engine【Phase 4 — Programming Languages】; Custom Rust framework【Phase 4 — Development Framework】; GitHub Rust repos【Phase 1 — Repository】; Pattern: Rust-first development【Phase 9 — Technical Pattern 6】.
Supporting Dataset: Phase 1 Foundation, Phase 4 Technology, Phase 9 Behavioral
Confidence: HIGH

Failure Factors

Factor 1: Tokenomics Opacity Menghambat Institutional Adoption & Valuation
Explanation: Tidak adanya whitepaper tokenomics, alokasi persentase, vesting schedule, emission rate, fee switch mechanism membuat investor institusional dan staker tidak dapat memodelkan supply dynamics, dilution risk, dan value accrual. Ini membatasi participation dari capital yang memerlukan transparency.
Evidence: Supply max/total/circulating/initial all unknown【Phase 6 — Supply】; Distribution all categories percentages unknown【Phase 6 — Distribution】; Vesting schedule all unknown【Phase 6 — Vesting Schedule】; Inflation emission schedule unknown【Phase 6 — Inflation/Deflation】; Treasury undisclosed【Phase 5 — Treasury】; Open threads tokenomics detail【Phase 1 — Open Threads】; Pattern: treasury & tokenomics opacity【Phase 9 — Financial Pattern 4】.
Supporting Dataset: Phase 1 Foundation, Phase 5 Financial, Phase 6 Token, Phase 9 Behavioral
Confidence: HIGH

Factor 2: Single Trusted Bridge + USDC Concentration = Single Point of Failure
Explanation: Semua cross-chain value flow bergantung pada satu native bridge (trusted validator set) dan satu stablecoin (USDC). Tidak ada redundancy bridge (light client/ZK/IBC) dan tidak ada multi-collateral support. Kegagalan bridge, validator collusion, atau USDC depeg/blacklist dapat melumpuhkan seluruh protokol.
Evidence: Bridge native trusted model【Phase 4 — Core Components: Hyperliquid Bridge】; Single bridge dependency risk High【Phase 7 — Ecosystem Risks】; USDC critical dependency High【Phase 7 — External Dependencies】; USDC collateral concentration risk High【Phase 7 — Ecosystem Risks】; Risk response: single bridge dependency accepted【Phase 9 — Risk Response Pattern 1】; USDC concentration risk accepted【Phase 9 — Risk Response Pattern 2】.
Supporting Dataset: Phase 4 Technology, Phase 7 Ecosystem, Phase 9 Behavioral
Confidence: HIGH

Factor 3: Governance Infrastructure Lagging Token Launch
Explanation: Token live dengan staking November 2024, tapi governance infrastructure (proposal system, voting, forum, execution, treasury controls) belum ada. Foundation formation tidak diverifikasi. Validator set mengontrol protocol upgrades dan bridge secara de facto tanpa accountability token-holder. Ini menciptakan governance vacuum dan centralization risk.
Evidence: Governance proposal system unknown【Phase 6 — Governance】; Foundation formation indicated not verified【Phase 3 — EV-011】; No formal DAO structure【Phase 7 — Governance Ecosystem】; Validator set implicit governance actor【Phase 9 — Governance Pattern 4】; Decision: staking activated at TGE, governance infra incomplete【Phase 9 — Decision: Staking activated at TGE】; Pattern: token-based governance infra incomplete【Phase 9 — Governance Pattern 1】.
Supporting Dataset: Phase 3 History, Phase 6 Token, Phase 7 Ecosystem, Phase 9 Behavioral
Confidence: HIGH

Factor 4: No Formal Security Audits pada Core Protocol
Explanation: HyperBFT consensus, CLOB matching engine, native bridge contracts tidak memiliki audit publik dari auditor tier-1. Untuk protokol financial infrastructure dengan TVL signifikan, absensi audit formal meningkatkan tail risk exploit dan mengurangi kepercayaan institusional.
Evidence: Audit history unknown【Phase 4 — Audit History】; No audit reports di GitHub/docs【Phase 4 — Audit History】; Ecosystem risk no formal audits High【Phase 7 — Ecosystem Risks】; Risk response: no formal audits accepted【Phase 9 — Risk Response Pattern 5】.
Supporting Dataset: Phase 4 Technology, Phase 7 Ecosystem, Phase 9 Behavioral
Confidence: HIGH

Factor 5: Regulatory Exposure Tanpa Compliance Framework Publik
Explanation: Perpetual futures DEX (derivatives) dari entitas BVI dengan global permissionless access terpapar enforcement risk CFTC/SEC/FCA. Tidak ada geo-blocking announcement, tidak ada legal opinion publik, tidak ada compliance framework. Regulatory action tiba-tiba dapat memaksa shutdown atau asset freeze.
Evidence: Regulatory financial risk High【Phase 5 — Financial Risk】; Ecosystem risk regulatory exposure High【Phase 7 — Ecosystem Risks】; Country BVI entity【Phase 1 — Foundation】; Risk response: launch global permissionless, no geo-blocking announcement【Phase 9 — Risk Response Pattern 4】; Open threads regulatory classification【Phase 1 — Open Threads】.
Supporting Dataset: Phase 1 Foundation, Phase 5 Financial, Phase 7 Ecosystem, Phase 9 Behavioral
Confidence: HIGH

Factor 6: Market Maker Concentration Risk (SIG & GSR)
Explanation: Likuiditas CLOB sangat bergantung pada 2 market maker institusional. Withdrawal salah satu (karena regulatory, business decision, atau technical issue) akan mengurangi order book depth drastis, memperlebar spreads, dan menurunkan UX trading — potential death spiral.
Evidence: SIG, GSR sebagai market maker utama【Phase 2 — Entity: SIG, GSR】; External dependencies criticality High【Phase 7 — External Dependencies】; Financial dependencies SIG, GSR【Phase 5 — Financial Dependencies】; Ecosystem risk market maker dependency High【Phase 7 — Ecosystem Risks】; Risk response: market maker dependency accepted【Phase 9 — Risk Response Pattern 3】.
Supporting Dataset: Phase 2 Entity, Phase 5 Financial, Phase 7 Ecosystem, Phase 9 Behavioral
Confidence: HIGH

Factor 7: Validator Set Centralization & Opacity
Explanation: Komposisi validator set, jumlah validator, geografis, entity, permissioned vs permissionless tidak dipublikasikan. Nakamoto coefficient unknown. Staking distribution unknown. Risiko collusion, censorship, atau coordinated attack tidak terukur.
Evidence: Validator count unknown【Phase 8 — Adoption Metrics】; Validator set composition not disclosed【Phase 7 — Ecosystem Risks】; Centralized validator set risk High【Phase 7 — Ecosystem Risks】; Governance pattern: validator set implicit governance【Phase 9 — Governance Pattern 4】; Open threads validator set composition【Phase 1 — Open Threads】.
Supporting Dataset: Phase 7 Ecosystem, Phase 8 Market, Phase 9 Behavioral, Phase 1 Foundation
Confidence: HIGH

Factor 8: Cloud Infrastructure Centralization Tidak Diungkap
Explanation: Validator nodes, RPC endpoints, API services kemungkinan besar hosted di AWS/GCP/Azure tapi tidak di-disclose. Regional cloud outage dapat menghentikan consensus atau API access. Tidak ada geographic diversity disclosure.
Evidence: Cloud providers unspecified inferred【Phase 7 — External Dependencies】; Infrastructure providers cloud providers unspecified【Phase 7 — Infrastructure Providers】; Ecosystem risk cloud centralization Medium【Phase 7 — Ecosystem Risks】; Pattern: cloud infrastructure dependency undisclosed【Phase 9 — Ecosystem Pattern 5】.
Supporting Dataset: Phase 7 Ecosystem

## Open Questions
- [foundation] Yurisdiksi pasti entitas hukum "Hyperliquid Labs" (BVI vs Cayman vs Singapura) — perlu verifikasi dokumen incorporasi resmi.
- [foundation] Daftar lengkap core team (nama nyata vs pseudonim) dan ukuran tim presisi — tidak diungkap secara transparan.
- [foundation] Tanggal testnet publik yang pasti (beberapa sumber menyebut Maret 2023, lain "Q1 2023") — perlu cross-check blog resmi arsip.
- [foundation] Alamat kontrak Wrapped HYPE (WHYPE) di Arbitrum/Ethereum mainnet yang resmi — belum dipublikasikan di docs teknis saat TGE.
- [foundation] Detail alokasi tokenomics HYPE (persentase team, investor, community, treasury) — whitepaper tokenomics belum terbit saat cut-off pengetahuan.
- [foundation] Status fee switch / revenue sharing ke pemegang HYPE — belum diaktifkan/diumumkan detailnya saat TGE.
- [foundation] Hubungan hukum antara Hyperliquid Labs (pembangkit) dan Hyperliquid Foundation (jika ada) untuk governance.
- [history] Tanggal pasti pendirian Hyperliquid Labs (bulan/tanggal di 2022) — tidak diungkap di blog resmi.
- [history] Tanggal pasti testnet internal (Q4 2022: bulan/tanggal spesifik) — hanya "Q4 2022" yang diketahui.
- [history] Detail ronde pendanaan (jumlah dana, valuasi, struktur SAFE/equity/token warrant) — The Block tidak mengungkap angka spesifik.
- [history] Tanggal pasti pembentukan Hyperliquid Foundation dan yurisdiksi hukum — belum diumumkan resmi; hanya terimplikasi di blog HYPE Genesis.
- [history] Alokasi tokenomics HYPE yang detail (persentase team, investor, community, treasury, TGE unlock schedule) — whitepaper tokenomics belum terbit saat cut-off.
- [history] Status fee switch / revenue sharing ke staker HYPE — belum diaktifkan/diumumkan detailnya.
- [history] Tanggal peluncuran Hyperliquid Bridge yang pasti (bulan/tanggal 2024) — hanya "2024" yang diketahui dari docs.
- [history] Daftar lengkap validator/setor staking awal pada TGE — tidak dipublikasikan transparan.
- [history] Kejadian keamanan/exploit/bug bounty signifikan (jika ada) — tidak ditemukan catatan publik.
- [history] Hubungan hukum formal antara Hyperliquid Labs dan Hyperliquid Foundation — belum diverifikasi dokumen hukum.
- [technology] Detail teknis HyperBFT (paper/spec formal) — tidak dipublikasikan; hanya deskripsi high-level di docs
- [technology] Spesifikasi precompile HyperEVM untuk akses CLOB — belum terdokumentasi lengkap di docs publik
- [technology] Modelo keamanan bridge detail (threshold signature, validator set rotation, slashing) — tidak transparan
- [technology] Rencana sharding / parallelization matching engine — tidak diroadmap teknis publik
- [technology] Status formal verification untuk kritikal consensus/matching logic — tidak ada informasi
- [technology] Detail upgradeability protokol (governance upgrade vs hard fork) — tidak terdokumentasi
- [technology] Kompatibilitas HyperEVM dengan EIP terbaru (Shanghai, Cancun, dll) — belum diverifikasi testnet
- [technology] Metrik performa konsensus (TPS, latency, finality time) under load produksi — tidak dipublikasikan benchmark independen
- [technology] Rencana decentralisasi validator set (permissioned vs permissionless) — tidak diumumkan jelas
- [technology] Detail storage architecture (state growth, pruning, archival) — tidak terdokumentasi
- [financial] Jumlah dana yang dikumpulkan di ronde 2023 (amount, valuation, struktur SAFE/equity/token warrant) — The Block tidak mengungkap angka.
- [financial] Ukuran, komposisi, dan custodian treasury resmi (Hyperliquid Labs vs Hyperliquid Foundation) — tidak ada transparency report atau on-chain dashboard tertaut.
- [financial] Data pendapatan protokol historis (bulanan/tahunan) — tidak dipublikasikan; DefiLlama hanya menampilkan volume/fees agregat tidak revenue netto.
- [financial] Rincian tokenomics HYPE: alokasi treasury, team, investor, community, ekosistem — whitepaper tokenomics belum terbit.
- [financial] Timeline dan mekanisme fee switch / revenue sharing ke pemegang HYPE (staker) — blog HYPE Genesis hanya menyebut staking untuk keamanan jaringan.
- [financial] Status hukum dan kontrol treasury Hyperliquid Foundation — apakah sudah terbentuk, yurisdiksi, dan hubungan dengan Hyperliquid Labs.
- [financial] Adanya ronde pendanaan follow-on (Series B, strategic extension) setelah 2023 — tidak diumumkan.
- [financial] Audit keuangan / smart contract bridge / treasury management — tidak ditemukan laporan audit publik.
- [financial] Risiko regulasi spesifik (Wells Notice, enforcement action, geo-blocking) yang mempengaruhi revenue — tidak ada disclosure resmi.
- [financial] Detail ekonomi staking: inflation rate, validator commission, real yield vs emission — belum terdokumentasi lengkap di docs.
- [token] Whitepaper tokenomics resmi (alokasi persentase per kategori, supply max, emission schedule, vesting detail cliff/linear/unlock) — belum terbit sama sekali.
- [token] Detail TGE unlock: persentase circulating supply at TGE per kategori (community, team, investor, foundation, treasury, ecosystem) — tidak diungkap.
- [token] Alamat kontrak/akun resmi untuk: Treasury, Foundation, Team, Investor vesting, Ecosystem Fund — tidak dipublikasikan on-chain dengan label terverifikasi.
- [token] Mekanisme governance formal: proposal threshold, quorum, voting period, execution delay, timelock/multisig treasury — belum terdokumentasi.
- [token] Fee switch / revenue sharing ke staker HYPE: apakah akan diaktifkan, persentase fee yang dialokasikan, mekanisme distribusi — blog HYPE Genesis hanya menyebut staking untuk keamanan jaringan.
- [token] Inflation rate staking: APY target, emission curve, halving schedule, terminal supply — tidak ada data.
- [token] Burn mechanism / buyback: apakah direncanakan, kondisi trigger, sumber dana — tidak diumumkan.
- [token] Hubungan hukum dan kontrol antara Hyperliquid Labs (BVI company) dan Hyperliquid Foundation (entity governance) — belum diverifikasi dokumen incorporasi foundation.
- [token] Status Wrapped HYPE (WHYPE) di Arbitrum/Ethereum: kontrak resmi, auditor, bridge mechanism, mint/burn authority — tidak diverifikasi di docs teknis.
- [token] Holder distribution analysis: whale concentration, Gini coefficient, entity labeling (CEX, market maker, foundation, team) — tidak ada dashboard resmi.
- [token] Audit keamanan token contract (native HYPE logic di Hyperliquid L1) dan bridge contract (WHYPE) — tidak ditemukan laporan audit publik.
- [token] Regulatory classification token HYPE (security vs utility vs commodity) di yurisdiksi utama (US, EU, SG, BVI) — tidak ada legal opinion publik.
- [token] Rencana listing CEX/DEX resmi dan market making program untuk HYPE — tidak diumumkan.
- [token] Detail minimum stake untuk menjalankan validator, commission rate validator, slashing conditions — tidak terdokumentasi di docs publik.
- [ecosystem] Daftar CEX yang melisting HYPE spot/perpetual (CoinGecko markets tab belum diverifikasi sebagai sumber resmi) — perlu cek CoinGecko "Markets" atau pengumuman resmi.
- [ecosystem] Dukungan wallet non-EVM native untuk Hyperliquid L1 (selain web app resmi) — apakah ada wallet mobile/hardware native support.
- [ecosystem] Detail cloud provider yang digunakan validator set dan Hyperliquid Labs — tidak diungkap, risiko sentralisasi infrastruktur tidak terukur.
- [ecosystem] Komposisi validator set (permissioned vs permissionless), jumlah validator, geografis, entity — tidak dipublikasikan.
- [ecosystem] Alternatif bridge trust-minimized (light client, ZK, IBC) di roadmap — tidak diumumkan.
- [ecosystem] Status audit keamanan formal untuk HyperBFT, CLOB engine, bridge contracts — tidak ditemukan laporan publik.
- [ecosystem] Detail tokenomics HYPE (alokasi, vesting, emission, fee switch) — whitepaper belum terbit.
- [ecosystem] Hubungan hukum Hyperliquid Labs (BVI) dan Hyperliquid Foundation (governance) — belum diverifikasi dokumen incorporasi foundation.
- [ecosystem] Rincian HyperEVM precompile untuk akses CLOB — spec teknis belum terdokumentasi lengkap.
- [ecosystem] Program hackathon / developer onboarding resmi selain Ecosystem Fund — tidak diumumkan.
- [ecosystem] Dukungan IBC / cross-chain messaging generik di luar native bridge — tidak disebut di docs.
- [ecosystem] Metrik desentralisasi staking (validator count, nakamoto coefficient, stake distribution) — tidak tersedia dashboard.
- [ecosystem] Rencana geo-blocking / compliance jurisdictional untuk perp DEX — tidak diumumkan.
- [ecosystem] Status oracle untuk funding rate / mark price perp (apakah murni on-chain CLOB atau butuh index price eksternal) — tidak terdokumentasi teknis detail.
- [ecosystem] Alokasi Ecosystem Fund dalam HYPE vs stablecoin vs equity — tidak diungkap.
- [ecosystem] Timeline HyperEVM mainnet launch dan audit pre-launch — tidak diumumkan.
- [market] Data TVL, Volume, Daily Active Users, Transactions, Wallets, Developer Count, Bridge Volume, Validator Count yang spesifik dan terverifikasi — tidak diekstrak di Phase 1-7; perlu query DefiLlama API, Hypurrscan, atau dashboard resmi jika ada.
- [market] Daftar CEX yang melisting HYPE spot/perpetual (CoinGecko markets tab belum diverifikasi sebagai sumber resmi) — perlu cek CoinGecko "Markets" atau pengumuman resmi.
- [market] Market share Hyperliquid di sektor perp DEX on-chain vs dYdX, GMX, Vertex, Aevo — tidak ada data komparatif di Phase 1-7.
- [market] Status geo-blocking / jurisdictional compliance untuk perp DEX — tidak diumumkan, mempengaruhi TAM (Total Addressable Market).
- [market] Detail tokenomics HYPE (alokasi, vesting, emission, fee switch) — whitepaper belum terbit, mempengaruhi valuasi model.
- [market] Audit keamanan formal untuk HyperBFT, CLOB engine, bridge contracts — tidak ditemukan laporan publik, risiko kepercayaan institusional.
- [market] Desentralisasi validator set (jumlah, geografis, entity, permissioned vs permissionless) — tidak dipublikasikan, mempengaruhi risk assessment.
- [market] Timeline HyperEVM mainnet launch dan audit pre-launch — tidak diumumkan, mempengaruhi narrative modular execution.
- [market] Hubungan hukum Hyperliquid Labs (BVI) dan Hyperliquid Foundation (governance) — belum diverifikasi dokumen incorporasi foundation.
- [market] Rincian HyperEVM precompile untuk akses CLOB — spec teknis belum terdokumentasi lengkap, mempengaruhi developer adoption.
- [market] Program hackathon / developer onboarding resmi selain Ecosystem Fund — tidak diumumkan.
- [market] Dukungan IBC / cross-chain messaging generik di luar native bridge — tidak disebut di docs.
- [market] Metrik desentralisasi staking (validator count, nakamoto coefficient, stake distribution) — tidak tersedia dashboard.
- [market] Alokasi Ecosystem Fund dalam HYPE vs stablecoin vs equity — tidak diungkap.
- [market] Regulatory classification token HYPE (security vs utility vs commodity) di yurisdiksi utama (US, EU, SG, BVI) — tidak ada legal opinion publik.
- [market] Status fee switch / revenue sharing ke staker HYPE — belum diaktifkan/diumumkan detailnya, mempengaruhi token value accrual narrative.
