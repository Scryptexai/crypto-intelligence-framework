# Vana — Deep Case Study (Phased)

**CIF Dataset — Deep Dossier · Tier: Deep (anchor project)**
**Source:** Deep Research (DeepSeek), Format v3 Dependency Pipeline (10/11 phases: foundation, entity, history, technology, financial, token, ecosystem, market, behavioral, knowledge). **Auto-assembled** by `tools/ingest.py` (deterministic, no LLM, strict data_project/ contract) — each phase extracted and concatenated in dependency order per `docs/Protocol/Deep-Research-Brief.md`; the reasoning is the source reports'.
**Raw sources archived:** doc_backup/deep/Vana_foundation_2026-08.docx, doc_backup/deep/Vana_entity_2026-08.docx, doc_backup/deep/Vana_history_2026-08.docx, doc_backup/deep/Vana_technology_2026-08.docx, doc_backup/deep/Vana_financial_2026-08.docx, doc_backup/deep/Vana_token_2026-08.docx, doc_backup/deep/Vana_ecosystem_2026-08.docx, doc_backup/deep/Vana_market_2026-08.docx, doc_backup/deep/Vana_behavioral_2026-08.docx, doc_backup/deep/Vana_knowledge_2026-08.docx.
**Phases not run:** conflict.

> Faithful concatenation of phase outputs — no fabrication, no distillation beyond what the closing phase (Conflict Resolution / Validation) itself states. Consider a periodic QC pass.

---
## Foundation Intelligence
_ref: `docs/Ontology/Identity.md`, `docs/Ontology/Team.md`_

PROJECT: Vana
Official Name: Vana (HIGH) [Vana.org, https://vana.org]
Symbol: VANA (HIGH) [CoinGecko, https://www.coingecko.com/en/coins/vana]
Category: data liquidity / data DAO infrastructure (HIGH) [Vana Whitepaper, https://vana.org/whitepaper.pdf; Messari, https://messari.io/report/vana]
Founding Entity: Vana Foundation, Cayman Islands (HIGH) [Vana Foundation GitHub, https://github.com/vana-com; Cayman Islands registry via OpenCorporates]
Founders: Anna Kazlauskas (CEO/Co-founder); Art Abal (COO/Co-founder) (HIGH) [Vana.org Team, https://vana.org/team; Forbes 30 Under 30 2024, https://www.forbes.com/profile/anna-kazlauskas]
Core Team: ~30+ full-time (engineering, research, BD, operations) — key public members: Jesse Walden (Advisor), Polymorphic Capital (investor/partner) (MEDIUM) [Vana.org Team page; LinkedIn searches; Messari report]
Country: Cayman Islands (Foundation); team distributed globally (US, Europe, Asia) (HIGH) [Vana Foundation legal structure; team page bios]
Launch Date - Testnet: 2023-07 (Moksha testnet) (HIGH) [Vana Blog "Introducing Moksha Testnet", https://blog.vana.org/introducing-moksha-testnet/]
Launch Date - Mainnet: 2024-10-16 (mainnet genesis) (HIGH) [Vana Blog "Vana Mainnet is Live", https://blog.vana.org/vana-mainnet-is-live/]
Launch Date - TGE: 2024-12-16 (TGE & VANA token launch) (HIGH) [Vana Blog "VANA Token Launch", https://blog.vana.org/vana-token-launch/; CoinGecko launch date]
Main Products: Vana Network (L1 for data liquidity); Data DAOs (user-owned data collectives — e.g., r/datadao, Volara, Flirtual); Vana Portal (user dashboard for data contribution); Universal Connectors (data portability SDKs); Proof-of-Contribution (consensus for data valuation) (HIGH) [Vana Whitepaper; Vana Docs, https://docs.vana.org]
Official Website: https://vana.org
Repository: https://github.com/vana-com
Documentation: https://docs.vana.org
Social - X/Twitter: @vana
Social - Discord: https://discord.gg/vana
Social - Telegram: @vana_official
Block Explorer: https://explorer.vana.org (HIGH) [Vana Explorer]
Token Contract: 0x5Af... (Ethereum mainnet) — VANA ERC-20; native VANA on Vana L1 (HIGH) [CoinGecko contract page; Vana Explorer]
Chain(s): Vana (native L1, EVM-compatible, Cosmos SDK-based); Ethereum (ERC-20 bridge) (HIGH) [Vana Whitepaper; Vana Docs "Architecture"]
Ecosystem: Data DAOs: r/datadao (Reddit data), Volara (Twitter/X data), Flirtual (dating data), DataPig (DeFi data), Kappa (gaming data); Partners: Polymorphic Capital, Paradigm, Coinbase Ventures, Polychain, Dragonfly (investors) (HIGH) [Vana Blog "Data DAO Ecosystem", https://blog.vana.org/category/data-daos/; Messari]

## Entity Intelligence
_ref: `docs/Ontology/Relationships.md` (entity graph)_

PROJECT: Vana

Entity: Vana Foundation
Type: Foundation
Relationship: Entitas hukum resmi yang mendirikan dan mengelola proyek Vana, terdaftar di Cayman Islands sebagai yayasan nirlaba yang mengawasi pengembangan protokol, ekosistem Data DAO, dan governance token VANA (HIGH)
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Vana Foundation GitHub, https://github.com/vana-com]; [Vana.org Team, https://vana.org/team]

Entity: Anna Kazlauskas
Type: Person
Relationship: Co-founder dan CEO Vana, memimpin visi strategis, pengembangan produk, dan ekosistem Data DAO; Forbes 30 Under 30 2024 (HIGH)
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Vana.org Team, https://vana.org/team]; [Forbes 30 Under 30 2024, https://www.forbes.com/profile/anna-kazlauskas]

Entity: Art Abal
Type: Person
Relationship: Co-founder dan COO Vana, mengelola operasional, business development, dan ekspansi ekosistem Data DAO (HIGH)
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Vana.org Team, https://vana.org/team]; [Vana Blog, https://blog.vana.org]

Entity: Jesse Walden
Type: Person
Relationship: Advisor Vana, memberikan arahan strategis pada protokol data liquidity dan tokenomics; pendiri Variant Fund (MEDIUM)
Period: 2023–sekarang
Exposure Type: shared-investor-only
Evidence: (MEDIUM) [Vana.org Team, https://vana.org/team]; [Messari Vana Report, https://messari.io/report/vana]

Entity: Polymorphic Capital
Type: Investor
Relationship: Investor awal dan mitra strategis Vana, berpartisipasi dalam ronde pendanaan dan mendukung ekosistem Data DAO (HIGH)
Period: 2023–sekarang
Exposure Type: financial-collateral
Evidence: (HIGH) [Vana Blog Data DAO Ecosystem, https://blog.vana.org/category/data-daos/]; [Messari Vana Report, https://messari.io/report/vana]

Entity: Paradigm
Type: Investor
Relationship: Investor Vana, menyediakan dana dan dukungan strategis untuk pengembangan L1 data liquidity (HIGH)
Period: 2023–sekarang
Exposure Type: financial-collateral
Evidence: (HIGH) [Messari Vana Report, https://messari.io/report/vana]; [Vana Blog, https://blog.vana.org]

Entity: Coinbase Ventures
Type: Investor
Relationship: Investor Vana melalui divisi venture Coinbase, mendukung pembangunan infrastruktur data portability (HIGH)
Period: 2023–sekarang
Exposure Type: financial-collateral
Evidence: (HIGH) [Messari Vana Report, https://messari.io/report/vana]; [Vana Blog, https://blog.vana.org]

Entity: Polychain Capital
Type: Investor
Relationship: Investor Vana, berpartisipasi dalam pembiayaan protokol data liquidity layer (HIGH)
Period: 2023–sekarang
Exposure Type: financial-collateral
Evidence: (HIGH) [Messari Vana Report, https://messari.io/report/vana]; [Vana Blog, https://blog.vana.org]

Entity: Dragonfly Capital
Type: Investor
Relationship: Investor Vana, mendanai pengembangan Vana Network dan ekosistem Data DAO (HIGH)
Period: 2023–sekarang
Exposure Type: financial-collateral
Evidence: (HIGH) [Messari Vana Report, https://messari.io/report/vana]; [Vana Blog, https://blog.vana.org]

Entity: Vana Network
Type: Protocol
Relationship: Layer 1 blockchain EVM-kompatibel berbasis Cosmos SDK yang dirancang untuk data liquidity, memungkinkan Proof-of-Contribution dan Data DAO (HIGH)
Period: 2024-10-16–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Vana Whitepaper, https://vana.org/whitepaper.pdf]; [Vana Docs Architecture, https://docs.vana.org]

Entity: Vana Mainnet
Type: Chain
Relationship: Mainnet produksi Vana Network yang diluncurkan pada 16 Oktober 2024, menhosting token VANA native dan aktivitas Data DAO (HIGH)
Period: 2024-10-16–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Vana Blog Mainnet Live, https://blog.vana.org/vana-mainnet-is-live/]; [Vana Explorer, https://explorer.vana.org]

Entity: Moksha Testnet
Type: Chain
Relationship: Testnet Vana (Moksha) yang diluncurkan Juli 2023 untuk pengujian protokol, validator, dan Data DAO sebelum mainnet (HIGH)
Period: 2023-07–2024-10
Exposure Type: technical-integration
Evidence: (HIGH) [Vana Blog Introducing Moksha, https://blog.vana.org/introducing-moksha-testnet/]; [Vana Docs, https://docs.vana.org]

Entity: VANA Token
Type: Protocol
Relationship: Token utilitas dan governance native Vana (ERC-20 di Ethereum, native di Vana L1), digunakan untuk staking, governance, dan insentif Data DAO; TGE 16 Desember 2024 (HIGH)
Period: 2024-12-16–sekarang
Exposure Type: financial-collateral
Evidence: (HIGH) [Vana Blog Token Launch, https://blog.vana.org/vana-token-launch/]; [CoinGecko VANA, https://www.coingecko.com/en/coins/vana]

Entity: r/datadao
Type: DAO
Relationship: Data DAO pertama dan terbesar di ekosistem Vana, mengumpulkan dan mengelola data Reddit pengguna untuk dilikuidasikan (HIGH)
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Vana Blog Data DAO Ecosystem, https://blog.vana.org/category/data-daos/]; [Messari Vana Report, https://messari.io/report/vana]

Entity: Volara
Type: DAO
Relationship: Data DAO Vana fokus pada data Twitter/X, memungkinkan pengguna mengekspor dan memonetisasi data media sosial mereka (HIGH)
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Vana Blog Data DAO Ecosystem, https://blog.vana.org/category/data-daos/]; [Messari Vana Report, https://messari.io/report/vana]

Entity: Flirtual
Type: DAO
Relationship: Data DAO Vana untuk data aplikasi kencan, memfasilitasi portabilitas dan likuiditas data preferensi pengguna (HIGH)
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Vana Blog Data DAO Ecosystem, https://blog.vana.org/category/data-daos/]; [Messari Vana Report, https://messari.io/report/vana]

Entity: DataPig
Type: DAO
Relationship: Data DAO Vana yang berfokus pada data DeFi, mengumpulkan riwayat transaksi dan posisi on-chain untuk analisis (HIGH)
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Vana Blog Data DAO Ecosystem, https://blog.vana.org/category/data-daos/]; [Messari Vana Report, https://messari.io/report/vana]

Entity: Kappa
Type: DAO
Relationship: Data DAO Vana untuk data gaming, memungkinkan pemain mengontrol dan memonetisasi data gameplay mereka (HIGH)
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Vana Blog Data DAO Ecosystem, https://blog.vana.org/category/data-daos/]; [Messari Vana Report, https://messari.io/report/vana]

Entity: Vana Portal
Type: Application
Relationship: Dashboard pengguna resmi Vana untuk kontribusi data, manajemen Data DAO, staking VANA, dan melacak reward (HIGH)
Period: 2024–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Vana Docs, https://docs.vana.org]; [Vana.org, https://vana.org]

Entity: Universal Connectors
Type: Application
Relationship: SDK portabilitas data Vana yang memungkinkan developer membangun konektor untuk mengekspor data dari platform Web2 ke Data DAO (HIGH)
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Vana Whitepaper, https://vana.org/whitepaper.pdf]; [Vana Docs, https://docs.vana.org]

Entity: Proof-of-Contribution
Type: Protocol
Relationship: Mekanisme konsensus Vana untuk valuasi dan verifikasi kualitas data yang dikontribusikan ke Data DAO, menentukan reward distribution (HIGH)
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Vana Whitepaper, https://vana.org/whitepaper.pdf]; [Vana Docs, https://docs.vana.org]

Entity: Vana Explorer
Type: Infrastructure
Relationship: Block explorer resmi Vana Mainnet untuk melihat transaksi, blok, validator, dan aktivitas token VANA (HIGH)
Period: 2024-10-16–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Vana Explorer, https://explorer.vana.org]; [Vana Blog Mainnet Live, https://blog.vana.org/vana-mainnet-is-live/]

Entity: Vana Docs
Type: Media
Relationship: Dokumentasi teknis resmi Vana mencakup arsitektur, API, smart contract, dan panduan developer (HIGH)
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Vana Docs, https://docs.vana.org]; [Vana GitHub, https://github.com/vana-com]

Entity: Vana Blog
Type: Media
Relationship: Blog resmi Vana untuk pengumuman produk, update mainnet, token launch, dan artikel ekosistem Data DAO (HIGH)
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Vana Blog, https://blog.vana.org]; [Vana.org, https://vana.org]

Entity: Vana GitHub
Type: Infrastructure
Relationship: Repositori kode sumber terbuka Vana berisi protokol, smart contract, SDK, dan tooling (HIGH)
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Vana GitHub, https://github.com/vana-com]; [Vana Docs, https://docs.vana.org]

Entity: Vana Discord
Type: Community
Relationship: Server komunitas resmi Vana untuk diskusi developer, kontributor data, dan governance (HIGH)
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Vana.org, https://vana.org]; [Discord Invite, https://discord.gg/vana]

Entity: Vana Telegram
Type: Community
Relationship: Grup Telegram resmi Vana untuk update announcements dan diskusi komunitas global (HIGH)
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Vana.org, https://vana.org]; [Telegram, https://t.me/vana_official]

Entity: Vana X (Twitter)
Type: Media
Relationship: Akun X/Twitter resmi @vana untuk pengumuman real-time, thread edukasi, dan engagement komunitas (HIGH)
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [X.com/vana, https://x.com/vana]; [Vana.org, https://vana.org]

Entity: CoinGecko
Type: Infrastructure
Relationship: Penyedia data pasar kripto yang melacak harga, volume, dan metadata token VANA sejak TGE (HIGH)
Period: 2024-12-16–sekarang
Exposure Type: narrative-correlated-only
Evidence: (HIGH) [CoinGecko VANA, https://www.coingecko.com/en/coins/vana]; [Vana Blog Token Launch, https://blog.vana.org/vana-token-launch/]

Entity: Messari
Type: Research Lab
Relationship: Platform riset kripto yang menerbitkan laporan mendalam Vana Report mencakup tokenomics, arsitektur, dan ekosistem (HIGH)
Period: 2024–sekarang
Exposure Type: narrative-correlated-only
Evidence: (HIGH) [Messari Vana Report, https://messari.io/report/vana]; [Vana Blog, https://blog.vana.org]

Entity: Forbes
Type: Media
Relationship: Media bisnis global yang menampilkan Anna Kazlauskas di Forbes 30 Under 30 2024 untuk kategori Technology (HIGH)
Period: 2024
Exposure Type: narrative-correlated-only
Evidence: (HIGH) [Forbes Profile Anna Kazlauskas, https://www.forbes.com/profile/anna-kazlauskas]; [Vana.org Team, https://vana.org/team]

Entity: OpenCorporates
Type: Infrastructure
Relationship: Database registrasi perusahaan global yang mereferensikan Vana Foundation sebagai entitas terdaftar di Cayman Islands (MEDIUM)
Period: 2023–sekarang
Exposure Type: narrative-correlated-only
Evidence: (MEDIUM) [OpenCorporates, https://opencorporates.com]; [Vana Foundation GitHub, https://github.com/vana-com]

Entity: Cayman Islands Registry
Type: Government
Relationship: Badan pemerintah Cayman Islands yang mengatur pendaftaran yayasan (foundation) termasuk Vana Foundation (MEDIUM)
Period: 2023–sekarang
Exposure Type: unknown
Evidence: (MEDIUM) [Vana Foundation legal structure, https://vana.org/team]; [Cayman Islands General Registry, https://www.gov.ky/portal/page/portal/home]

---

PERSON
Anna Kazlauskas
Art Abal
Jesse Walden

FOUNDATION
Vana Foundation

COMPANY
Polymorphic Capital
Paradigm
Coinbase Ventures
Polychain Capital
Dragonfly Capital

PROTOCOL
Vana Network
VANA Token
Proof-of-Contribution

CHAIN
Vana Mainnet
Moksha Testnet

INVESTOR
Polymorphic Capital
Paradigm
Coinbase Ventures
Polychain Capital
Dragonfly Capital

INFRASTRUCTURE
Vana Explorer
Vana GitHub
CoinGecko
OpenCorporates

APPLICATION
Vana Portal
Universal Connectors

SECURITY
(tidak ada entity security teridentifikasi)

DAO
r/datadao
Volara
Flirtual
DataPig
Kappa

GOVERNMENT
Cayman Islands Registry

MEDIA
Vana Blog
Vana Docs
Vana X (Twitter)
Messari
Forbes

COMMUNITY
Vana Discord
Vana Telegram

OTHER
(tidak ada)

---

Total Entity: 36
Internal: 14
External: 22
Unknown: 0

## Historical Intelligence
_ref: `docs/Ontology/DecisionEvent.md` (factual spine — enriched later by Behavioral)_

PROJECT: Vana

Event ID

EV-001

Date

2021

Event Name

Pendirian Vana oleh Anna Kazlauskas dan Art Abal

Event Type

Founding

Description

Anna Kazlauskas dan Art Abal mendirikan Vana dengan visi membangun lapisan likuiditas data (data liquidity layer) yang memungkinkan pengguna memiliki dan memonetisasi data mereka melalui Data DAO.

Participants

Anna Kazlauskas; Art Abal

Location

San Francisco, AS

Status

Completed

Immediate Result

Terwujudnya tim inti dan konsep awal protokol Vana.

Sources

https://vana.org/team
https://www.forbes.com/profile/anna-kazlauskas

---

Event ID

EV-002

Date

2023

Event Name

Pendirian Vana Foundation di Cayman Islands

Event Type

Organization

Description

Vana Foundation didirikan sebagai yayasan nirlaba di Cayman Islands untuk mengawasi pengembangan protokol, ekosistem Data DAO, dan governance token VANA.

Participants

Vana Foundation

Location

Cayman Islands

Status

Completed

Immediate Result

Entitas hukum resmi untuk pengelolaan protokol Vana dan ekosistemnya.

Sources

https://github.com/vana-com
https://vana.org/team

---

Event ID

EV-003

Date

2023

Event Name

Publikasi Vana Whitepaper

Event Type

Technology

Description

Vana mempublikasikan whitepaper yang mendetail arsitektur L1 berbasis Cosmos SDK, mekanisme Proof-of-Contribution, dan desain Data DAO untuk likuiditas data.

Participants

Vana Foundation

Location

Online

Status

Completed

Immediate Result

Dokumen spesifikasi teknis resmi tersedia untuk developer dan komunitas.

Sources

https://vana.org/whitepaper.pdf
https://docs.vana.org

---

Event ID

EV-004

Date

2023-07

Event Name

Peluncuran Moksha Testnet

Event Type

Launch

Description

Vana meluncurkan Moksha testnet untuk pengujian protokol, validator, Data DAO, dan mekanisme Proof-of-Contribution sebelum mainnet.

Participants

Vana Foundation; Vana Network

Location

Online

Status

Completed

Immediate Result

Testnet publik aktif untuk pengujian validator, Data DAO, dan infrastruktur protokol.

Sources

https://blog.vana.org/introducing-moksha-testnet/
https://docs.vana.org

---

Event ID

EV-005

Date

2023

Event Name

Ronde Pendanaan Awal dari Paradigm, Polymorphic Capital, Coinbase Ventures, Polychain Capital, Dragonfly Capital

Event Type

Funding

Description

Vana mengamankan pendanaan dari investor terkemuka termasuk Paradigm, Polymorphic Capital, Coinbase Ventures, Polychain Capital, dan Dragonfly Capital untuk pengembangan L1 data liquidity.

Participants

Vana Foundation; Paradigm; Polymorphic Capital; Coinbase Ventures; Polychain Capital; Dragonfly Capital

Location

San Francisco, AS / Global

Status

Completed

Immediate Result

Dana pengembangan protokol Vana Network dan ekosistem Data DAO tersedia.

Sources

https://messari.io/report/vana
https://blog.vana.org

---

Event ID

EV-006

Date

2023

Event Name

Peluncuran r/datadao (Data DAO Reddit)

Event Type

Ecosystem

Description

r/datadao diluncurkan sebagai Data DAO pertama dan terbesar di ekosistem Vana, memungkinkan pengguna Reddit mengekspor dan mengumpulkan data mereka untuk dilikuidasikan.

Participants

Vana Foundation; r/datadao

Location

Online

Status

Completed

Immediate Result

Data DAO pertama beroperasi di testnet Moksha, mengumpulkan data Reddit pengguna.

Sources

https://blog.vana.org/category/data-daos/
https://messari.io/report/vana

---

Event ID

EV-007

Date

2023

Event Name

Peluncuran Volara (Data DAO Twitter/X)

Event Type

Ecosystem

Description

Volara diluncurkan sebagai Data DAO untuk data Twitter/X, memungkinkan pengguna mengekspor dan memonetisasi data media sosial mereka.

Participants

Vana Foundation; Volara

Location

Online

Status

Completed

Immediate Result

Data DAO kedua beroperasi, memperluas cakupan portabilitas data ke platform media sosial.

Sources

https://blog.vana.org/category/data-daos/
https://messari.io/report/vana

---

Event ID

EV-008

Date

2023

Event Name

Peluncuran Flirtual (Data DAO Dating)

Event Type

Ecosystem

Description

Flirtual diluncurkan sebagai Data DAO untuk data aplikasi kencan, memfasilitasi portabilitas dan likuiditas data preferensi pengguna.

Participants

Vana Foundation; Flirtual

Location

Online

Status

Completed

Immediate Result

Data DAO ketiga beroperasi, menambah vertikal data dating ke ekosistem.

Sources

https://blog.vana.org/category/data-daos/
https://messari.io/report/vana

---

Event ID

EV-009

Date

2023

Event Name

Peluncuran DataPig (Data DAO DeFi)

Event Type

Ecosystem

Description

DataPig diluncurkan sebagai Data DAO fokus data DeFi, mengumpulkan riwayat transaksi dan posisi on-chain untuk analisis.

Participants

Vana Foundation; DataPig

Location

Online

Status

Completed

Immediate Result

Data DAO keempat beroperasi, menambah vertikal data keuangan terdesentralisasi.

Sources

https://blog.vana.org/category/data-daos/
https://messari.io/report/vana

---

Event ID

EV-010

Date

2023

Event Name

Peluncuran Kappa (Data DAO Gaming)

Event Type

Ecosystem

Description

Kappa diluncurkan sebagai Data DAO untuk data gaming, memungkinkan pemain mengontrol dan memonetisasi data gameplay mereka.

Participants

Vana Foundation; Kappa

Location

Online

Status

Completed

Immediate Result

Data DAO kelima beroperasi, menambah vertikal data gaming ke ekosistem.

Sources

https://blog.vana.org/category/data-daos/
https://messari.io/report/vana

---

Event ID

EV-011

Date

2023

Event Name

Pengembangan Universal Connectors SDK

Event Type

Technology

Description

Vana mengembangkan Universal Connectors SDK untuk portabilitas data, memungkinkan developer membangun konektor mengekspor data dari platform Web2 ke Data DAO.

Participants

Vana Foundation

Location

Online

Status

Ongoing

Immediate Result

SDK tersedia untuk developer membangun konektor data portabilitas.

Sources

https://vana.org/whitepaper.pdf
https://docs.vana.org

---

Event ID

EV-012

Date

2023

Event Name

Implementasi Mekanisme Proof-of-Contribution

Event Type

Technology

Description

Vana mengimplementasikan Proof-of-Contribution sebagai mekanisme konsensus untuk valuasi dan verifikasi kualitas data yang dikontribusikan ke Data DAO.

Participants

Vana Foundation; Vana Network

Location

Online

Status

Completed

Immediate Result

Mekanisme konsensus untuk reward distribution berdasarkan kualitas data tersedia di testnet.

Sources

https://vana.org/whitepaper.pdf
https://docs.vana.org

---

Event ID

EV-013

Date

2024-10-16

Event Name

Peluncuran Vana Mainnet

Event Type

Launch

Description

Vana Mainnet resmi diluncurkan pada blok genesis, menhosting token VANA native dan aktivitas Data DAO pada L1 EVM-kompatibel berbasis Cosmos SDK.

Participants

Vana Foundation; Vana Network; Vana Mainnet

Location

Online

Status

Completed

Immediate Result

Mainnet produksi aktif, validator set beroperasi, Data DAO bermigrasi dari testnet.

Sources

https://blog.vana.org/vana-mainnet-is-live/
https://explorer.vana.org

---

Event ID

EV-014

Date

2024-10-16

Event Name

Vana Block Explorer Resmi Online

Event Type

Infrastructure

Description

Block explorer resmi Vana Mainnet diluncurkan untuk melihat transaksi, blok, validator, dan aktivitas token VANA.

Participants

Vana Foundation; Vana Explorer

Location

Online

Status

Completed

Immediate Result

Transparansi on-chain tersedia untuk komunitas dan developer.

Sources

https://explorer.vana.org
https://blog.vana.org/vana-mainnet-is-live/

---

Event ID

EV-015

Date

2024

Event Name

Peluncuran Vana Portal

Event Type

Product

Description

Dashboard pengguna resmi Vana (Vana Portal) diluncurkan untuk kontribusi data, manajemen Data DAO, staking VANA, dan pelacakan reward.

Participants

Vana Foundation; Vana Portal

Location

Online

Status

Completed

Immediate Result

Antarmuka pengguna terpusat untuk berinteraksi dengan ekosistem Vana tersedia.

Sources

https://docs.vana.org
https://vana.org

---

Event ID

EV-016

Date

2024-12-16

Event Name

VANA Token Generation Event (TGE) dan Peluncuran Token

Event Type

Token

Description

Token VANA resmi diluncurkan melalui TGE; VANA berfungsi sebagai token utilitas dan governance (ERC-20 di Ethereum, native di Vana L1) untuk staking, governance, dan insentif Data DAO.

Participants

Vana Foundation; VANA Token

Location

Online

Status

Completed

Immediate Result

Token VANA tersebar ke komunitas, investor, dan tim; trading dimulai di exchange.

Sources

https://blog.vana.org/vana-token-launch/
https://www.coingecko.com/en/coins/vana

---

Event ID

EV-017

Date

2024-12

Event Name

Listing VANA Token di Exchange Terpusat (CEX)

Event Type

Market

Description

Token VANA mulai terdaftar di berbagai exchange terpusat (CEX) setelah TGE, menyediakan likuiditas pasar.

Participants

VANA Token; CoinGecko

Location

Global

Status

Completed

Immediate Result

Price discovery dan akses pasar luas untuk token VANA.

Sources

https://www.coingecko.com/en/coins/vana
https://blog.vana.org/vana-token-launch/

---

Event ID

EV-018

Date

2024

Event Name

Publikasi Laporan Messari Vana Report

Event Type

Other

Description

Messari menerbitkan laporan riset mendalam "Vana Report" mencakup tokenomics, arsitektur, dan ekosistem Data DAO.

Participants

Messari; Vana Foundation

Location

Online

Status

Completed

Immediate Result

Analisis independen komprehensif tersedia untuk investor dan peneliti.

Sources

https://messari.io/report/vana
https://blog.vana.org

---

Event ID

EV-019

Date

2024

Event Name

Anna Kazlauskas Masuk Forbes 30 Under 30 2024

Event Type

Other

Description

Anna Kazlauskas (CEO/Co-founder Vana) dicatat dalam Forbes 30 Under 30 2024 kategori Technology.

Participants

Anna Kazlauskas; Forbes

Location

AS

Status

Completed

Immediate Result

Pengakuan industri dan visibilitas media untuk proyek Vana.

Sources

https://www.forbes.com/profile/anna-kazlauskas
https://vana.org/team

---

## Summary by Year

### 2021
- EV-001: Pendirian Vana (Founding)

### 2023
- EV-002: Pendirian Vana Foundation (Organization)
- EV-003: Publikasi Whitepaper (Technology)
- EV-004: Peluncuran Moksha Testnet (Launch)
- EV-005: Ronde Pendanaan Awal (Funding)
- EV-006: Peluncuran r/datadao (Ecosystem)
- EV-007: Peluncuran Volara (Ecosystem)
- EV-008: Peluncuran Flirtual (Ecosystem)
- EV-009: Peluncuran DataPig (Ecosystem)
- EV-010: Peluncuran Kappa (Ecosystem)
- EV-011: Pengembangan Universal Connectors (Technology)
- EV-012: Implementasi Proof-of-Contribution (Technology)

### 2024
- EV-013: Peluncuran Vana Mainnet (Launch)
- EV-014: Vana Block Explorer Online (Infrastructure)
- EV-015: Peluncuran Vana Portal (Product)
- EV-016: VANA Token TGE (Token)
- EV-017: Listing VANA di CEX (Market)
- EV-018: Laporan Messari (Other)
- EV-019: Forbes 30 Under 30 (Other)

## Total Events by Type

Total Events: 19

Founding: 1
Funding: 1
Launch: 2
Technology: 3
Governance: 0
Security: 0
Legal: 0
Regulation: 0
Partnership: 0
Integration: 0
Token: 1
Market: 1
Organization: 1
Infrastructure: 1
Community: 0
Product: 1
Ecosystem: 5
Other: 2

## Technology Intelligence
_ref: `docs/Ontology/Technology.md`_

PROJECT: Vana

## System Architecture

Architecture Type: Layer 1 blockchain berbasis Cosmos SDK dengan kompatibilitas EVM (HIGH) [Vana Whitepaper, https://vana.org/whitepaper.pdf; Vana Docs Architecture, https://docs.vana.org]
Architecture Description: Vana Network adalah Layer 1 sovereign chain yang menggunakan Cosmos SDK sebagai framework inti dan mengimplementasikan EVM melalui Ethermint untuk kompatibilitas Ethereum; lapisan konsensus menggunakan CometBFT (Tendermint) BFT consensus; lapisan aplikasi meng-hosting Data DAO smart contracts dan Proof-of-Contribution modules (HIGH) [Vana Whitepaper, https://vana.org/whitepaper.pdf; Vana Docs, https://docs.vana.org]
Modular Design: Pemisahan lapisan konsensus (CometBFT), eksekusi (EVM via Ethermint), dan aplikasi (Data DAO modules, PoC modules) mengikuti arsitektur modular Cosmos SDK (HIGH) [Vana Whitepaper, https://vana.org/whitepaper.pdf; Cosmos SDK Docs, https://docs.cosmos.network]
Cross-chain Messaging: IBC (Inter-Blockchain Communication) native dari Cosmos SDK untuk interoperabilitas antar chain Cosmos; bridge Ethereum-Vana untuk transfer token VANA ERC-20 ↔ native VANA (HIGH) [Vana Whitepaper, https://vana.org/whitepaper.pdf; Vana Docs Bridge, https://docs.vana.org]
Bridge: Vana-Ethereum Bridge (official bridge) untuk two-way peg VANA token antara Ethereum mainnet (ERC-20) dan Vana L1 (native); menggunakan validator set Vana untuk attestation (HIGH) [Vana Blog Mainnet Live, https://blog.vana.org/vana-mainnet-is-live/; Vana Docs Bridge, https://docs.vana.org]
Settlement Layer: Vana L1 sendiri sebagai settlement layer untuk Data DAO transactions dan Proof-of-Contribution verification (HIGH) [Vana Whitepaper, https://vana.org/whitepaper.pdf]
Execution Layer: EVM execution environment via Ethermint module pada Cosmos SDK (HIGH) [Vana Whitepaper, https://vana.org/whitepaper.pdf; Ethermint GitHub, https://github.com/evmos/ethermint]
Storage: On-chain state storage via Cosmos SDK KVStore (IAVL tree) untuk application state; off-chain data storage untuk Data DAO raw data (IPFS, Arweave, atau centralized cloud per Data DAO design) (HIGH) [Vana Whitepaper, https://vana.org/whitepaper.pdf; Universal Connectors Docs, https://docs.vana.org]

Sources:
- Vana Whitepaper: https://vana.org/whitepaper.pdf
- Vana Docs Architecture: https://docs.vana.org
- Vana Blog Mainnet Live: https://blog.vana.org/vana-mainnet-is-live/
- Cosmos SDK Docs: https://docs.cosmos.network
- Ethermint GitHub: https://github.com/evmos/ethermint

## Core Components

Component: CometBFT Consensus Engine
Function: BFT consensus engine (Tendermint) yang memproduksi block dan memvalidasi transaksi; validator set mengeksekusi Proof-of-Stake untuk network security (HIGH)
Status: Live on mainnet since 2024-10-16 (HIGH)
Sources: [Vana Whitepaper, https://vana.org/whitepaper.pdf; CometBFT Docs, https://docs.cometbft.com]

Component: Ethermint EVM Module
Function: Modul Cosmos SDK yang menyediakan EVM execution environment; memungkinkan deployment Solidity smart contracts dan kompatibilitas Ethereum RPC (HIGH)
Status: Live on mainnet since 2024-10-16 (HIGH)
Sources: [Vana Whitepaper, https://vana.org/whitepaper.pdf; Ethermint GitHub, https://github.com/evmos/ethermint]

Component: Proof-of-Contribution (PoC) Module
Function: Custom Cosmos SDK module untuk valuasi dan verifikasi kualitas data yang dikontribusikan ke Data DAO; menentukan reward distribution berdasarkan data quality scores (HIGH)
Status: Live on mainnet since 2024-10-16; active di Data DAOs (HIGH)
Sources: [Vana Whitepaper, https://vana.org/whitepaper.pdf; Vana Docs PoC, https://docs.vana.org]

Component: Data DAO Smart Contracts
Function: Solidity smart contracts yang di-deploy di EVM Vana untuk mengelola Data DAO operations: data contribution, token rewards, governance, treasury management (HIGH)
Status: Live — r/datadao, Volara, Flirtual, DataPig, Kappa contracts deployed (HIGH)
Sources: [Vana Blog Data DAO Ecosystem, https://blog.vana.org/category/data-daos/; Vana Explorer Contracts, https://explorer.vana.org]

Component: Universal Connectors SDK
Function: TypeScript/Python SDK untuk developer membangun data connectors yang mengekspor data dari platform Web2 (Reddit, Twitter, dll.) ke Data DAO via encrypted upload (HIGH)
Status: Active development; used by existing Data DAOs (HIGH)
Sources: [Vana Whitepaper, https://vana.org/whitepaper.pdf; Vana Docs Connectors, https://docs.vana.org; Vana GitHub, https://github.com/vana-com]

Component: Vana Portal (Frontend)
Function: React-based web application untuk user dashboard: data contribution flow, Data DAO discovery, VANA staking, reward tracking, portfolio management (HIGH)
Status: Live at portal.vana.org (HIGH)
Sources: [Vana Portal, https://portal.vana.org; Vana Docs, https://docs.vana.org]

Component: Vana-Ethereum Bridge
Function: Bidirectional bridge contract set (Ethereum side: ERC-20 VANA + bridge contract; Vana side: native VANA + bridge module) dengan validator attestation untuk mint/burn (HIGH)
Status: Live since mainnet launch 2024-10-16 (HIGH)
Sources: [Vana Blog Mainnet Live, https://blog.vana.org/vana-mainnet-is-live/; Vana Docs Bridge, https://docs.vana.org]

Component: Vana Explorer (Block Explorer)
Function: Block explorer berbasis Blockscout/ustom untuk Vana Mainnet: block, transaction, validator, contract, token tracking (HIGH)
Status: Live at explorer.vana.org (HIGH)
Sources: [Vana Explorer, https://explorer.vana.org; Vana Blog Mainnet Live, https://blog.vana.org/vana-mainnet-is-live/]

Component: IBC Module
Function: Cosmos SDK IBC module untuk cross-chain communication dengan chain lain di ecosystem Cosmos (Osmosis, Celestia, dll.) (HIGH)
Status: Enabled on mainnet; channels may be in progress (MEDIUM)
Sources: [Vana Whitepaper, https://vana.org/whitepaper.pdf; Cosmos IBC Docs, https://ibc.cosmos.network]

Component: Validator Node Software
Function: CometBFT full node + Ethermint EVM + Vana custom modules (PoC, Bridge, IBC); dijalankan oleh validator untuk consensus dan block production (HIGH)
Status: Live; validator set active (HIGH)
Sources: [Vana GitHub Node Repo, https://github.com/vana-com; Vana Docs Validator, https://docs.vana.org]

Sources:
- Vana Whitepaper: https://vana.org/whitepaper.pdf
- Vana Docs: https://docs.vana.org
- Vana Blog Data DAO Ecosystem: https://blog.vana.org/category/data-daos/
- Vana Explorer: https://explorer.vana.org
- Vana Portal: https://portal.vana.org
- Vana GitHub: https://github.com/vana-com
- CometBFT Docs: https://docs.cometbft.com
- Ethermint GitHub: https://github.com/evmos/ethermint
- Cosmos IBC Docs: https://ibc.cosmos.network

## Consensus Mechanism

Consensus Name: CometBFT (Tendermint) BFT Proof-of-Stake (HIGH)
Description: Validator set melakukan round-based BFT consensus dengan 2/3+ voting power untuk finality; block time ~1-2 detik; instant finality (no probabilistic reorg) (HIGH)
Validator Selection: Proof-of-Stake berdasarkan VANA token stake (native staking di Vana L1); delegation didukung; top N validators by stake menjadi active set (parameter governance-controlled) (HIGH)
Proof-of-Contribution Role: PoC BUKAN consensus mechanism untuk block production; PoC adalah application-layer mechanism untuk data quality valuation dan reward distribution di Data DAO (HIGH)
Slashing: Double-sign slashing dan downtime slashing per CometBFT standard; parameter governed on-chain (HIGH)
Sources:
- Vana Whitepaper: https://vana.org/whitepaper.pdf
- CometBFT Docs: https://docs.cometbft.com
- Vana Docs Consensus: https://docs.vana.org
- Vana Blog Mainnet Live: https://blog.vana.org/vana-mainnet-is-live/

## Execution Environment

Primary: EVM (Ethereum Virtual Machine) via Ethermint module pada Cosmos SDK (HIGH)
Version: Ethereum London/EIP-1559 compatible; Solidity ^0.8.x support (HIGH)
RPC Compatibility: Standard Ethereum JSON-RPC methods (eth_call, eth_sendRawTransaction, eth_getLogs, dll.) tersedia via Ethermint JSON-RPC server (HIGH)
Precompiles: Native Cosmos SDK module access via precompile contracts (staking, governance, IBC, PoC, Bridge) (HIGH)
Gas Metering: EVM gas + Cosmos SDK gas unified; fee market EIP-1559 style (HIGH)
Smart Contract Language: Solidity (primary); Vyper teoretis supported (HIGH)
WASM/CosmWasm: Tidak digunakan untuk execution layer utama; Cosmos SDK modules ditulis dalam Go (HIGH)
Sources:
- Vana Whitepaper: https://vana.org/whitepaper.pdf
- Ethermint GitHub: https://github.com/evmos/ethermint
- Vana Docs Developers: https://docs.vana.org
- Vana Blog Mainnet Live: https://blog.vana.org/vana-mainnet-is-live/

## Programming Languages

Go: Core blockchain node (Cosmos SDK modules, CometBFT, Ethermint integration, custom modules: PoC, Bridge, IBC) (HIGH)
Solidity: Smart contracts untuk Data DAO, VANA token (ERC-20 di Ethereum), bridge contracts, governance contracts (HIGH)
TypeScript/JavaScript: Universal Connectors SDK, Vana Portal frontend, developer tooling, testing frameworks (HIGH)
Python: Data connector scripts, data processing pipelines, research/analytics tooling (MEDIUM)
Rust: Tidak digunakan di core protocol; mungkin di tooling tambahan (LOW)
Sources:
- Vana GitHub: https://github.com/vana-com
- Vana Docs: https://docs.vana.org
- Universal Connectors Repo: https://github.com/vana-com (monorepo structure)

## Development Framework

Cosmos SDK: v0.47+ / v0.50+ (framework utama untuk blockchain application layer) (HIGH)
CometBFT: v0.37+ / v0.38+ (consensus engine) (HIGH)
Ethermint: v0.4+ (EVM module) (HIGH)
Ignite CLI: Scaffold dan development tooling untuk Cosmos chains (MEDIUM)
Hardhat / Foundry: Smart contract development, testing, deployment untuk Solidity contracts (HIGH)
TypeScript SDK: Universal Connectors SDK development (HIGH)
React / Next.js: Vana Portal frontend framework (HIGH)
Docker: Containerization untuk node deployment, CI/CD (HIGH)
GitHub Actions: CI/CD pipeline (HIGH)
Protobuf / gRPC: Inter-module communication, ABCI interface, client APIs (HIGH)
Sources:
- Vana GitHub: https://github.com/vana-com
- Cosmos SDK Docs: https://docs.cosmos.network
- Ethermint GitHub: https://github.com/evmos/ethermint
- Ignite CLI: https://ignite.com/cli

## Security Model

Validator Security: CometBFT BFT consensus dengan 2/3+ honest validator assumption; slashing untuk double-sign (5% stake) dan downtime (0.01% per block window) (HIGH)
Economic Security: VANA token staking di Vana L1; delegation mechanism; total staked VANA menentukan attack cost (HIGH)
Bridge Security: Validator-set attestation model untuk Vana-Ethereum bridge; multi-sig / threshold signature untuk bridge contract upgrades (HIGH)
Smart Contract Security: Standard Ethereum security model (reentrancy guards, access control, audited patterns); Data DAO contracts upgradeable via proxy (HIGH)
Data Privacy: Data kontributor di-enkripsi client-side sebelum upload; Data DAO hanya menerima encrypted data + proof; raw data tidak visible on-chain (HIGH)
Proof-of-Contribution Security: Cryptographic verification of data authenticity (zkTLS, TEEs, atau API signatures tergantung connector); challenge period untuk fraudulent submissions (HIGH)
IBC Security: Light client verification pada counter-party chain; standard IBC security model (HIGH)
Governance Security: On-chain governance untuk parameter changes, upgrades; timelock untuk critical changes (HIGH)
Sources:
- Vana Whitepaper: https://vana.org/whitepaper.pdf
- Vana Docs Security: https://docs.vana.org
- CometBFT Security: https://docs.cometbft.com
- Cosmos SDK Security: https://docs.cosmos.network

## Audit History

Auditor: tidak diketahui (no public audit reports found as of research cutoff)
Date: N/A
Scope: N/A
Status: N/A
Source: [Vana GitHub, https://github.com/vana-com; Vana Blog, https://blog.vana.org; Vana Docs, https://docs.vana.org — no audit announcements found]
Note: Tidak ada audit publik yang diumumkan oleh Vana Foundation untuk smart contracts, bridge, atau core modules per pencarian di GitHub, blog, dan dokumentasi resmi hingga cutoff penelitian. (HIGH)

Sources:
- Vana GitHub: https://github.com/vana-com
- Vana Blog: https://blog.vana.org
- Vana Docs: https://docs.vana.org

## Technical Upgrade History

Upgrade: Mainnet Genesis Launch
Date: 2024-10-16
Description: Genesis block production dimulai; validator set aktif; VANA native token minted; Data DAO contracts deployed; bridge contracts deployed; IBC enabled; Vana Portal live; Explorer live
Status: Completed
Source: [Vana Blog Mainnet Live, https://blog.vana.org/vana-mainnet-is-live/; Vana Explorer, https://explorer.vana.org]

Upgrade: VANA Token TGE & ERC-20 Deployment
Date: 2024-12-16
Description: VANA ERC-20 token deployed di Ethereum mainnet; TGE distribution executed; bridge activated untuk two-way transfer; CEX listings initiated
Status: Completed
Source: [Vana Blog Token Launch, https://blog.vana.org/vana-token-launch/; CoinGecko VANA, https://www.coingecko.com/en/coins/vana]

Upgrade: Moksha Testnet Launch
Date: 2023-07
Description: Public testnet (Moksha) launch untuk validator testing, Data DAO onboarding, PoC mechanism testing, bridge testing
Status: Completed (deprecated after mainnet)
Source: [Vana Blog Introducing Moksha, https://blog.vana.org/introducing-moksha-testnet/; Vana Docs, https://docs.vana.org]

Upgrade: Data DAO Mainnet Deployments (Sequential)
Date: 2024-10-16 hingga 2024-12
Description: r/datadao, Volara, Flirtual, DataPig, Kappa smart contracts deployed dan activated di Vana Mainnet secara bertahap
Status: Completed
Source: [Vana Blog Data DAO Ecosystem, https://blog.vana.org/category/data-daos/; Vana Explorer Contracts, https://explorer.vana.org]

Sources:
- Vana Blog Mainnet Live: https://blog.vana.org/vana-mainnet-is-live/
- Vana Blog Token Launch: https://blog.vana.org/vana-token-launch/
- Vana Blog Introducing Moksha: https://blog.vana.org/introducing-moksha-testnet/
- Vana Blog Data DAO Ecosystem: https://blog.vana.org/category/data-daos/
- Vana Explorer: https://explorer.vana.org
- CoinGecko VANA: https://www.coingecko.com/en/coins/vana

## Current Technical Stack

Cosmos SDK: Core application framework (Go) (HIGH)
CometBFT: Consensus engine (Go) (HIGH)
Ethermint: EVM execution module (Go) (HIGH)
Go: Primary language untuk node software, custom modules (HIGH)
Solidity: Smart contract language (HIGH)
TypeScript: Universal Connectors SDK, frontend tooling (HIGH)
React / Next.js: Vana Portal frontend (HIGH)
Docker: Container orchestration untuk node deployment (HIGH)
Kubernetes: Production validator node orchestration (assumed, not explicitly confirmed) (MEDIUM)
PostgreSQL: Indexer / explorer backend database (Blockscout-based explorer) (MEDIUM)
Redis: Caching layer untuk RPC / indexer (assumed) (LOW)
IPFS / Arweave: Off-chain data storage untuk Data DAO raw data (per Data DAO choice) (HIGH)
Prometheus / Grafana: Monitoring dan alerting untuk validator nodes (standard Cosmos stack) (MEDIUM)
GitHub Actions: CI/CD (HIGH)
Protobuf: Serialization, gRPC interfaces (HIGH)
gRPC / REST: Client APIs (Cosmos SDK standard) (HIGH)
Sources:
- Vana GitHub: https://github.com/vana-com
- Vana Docs: https://docs.vana.org
- Cosmos SDK Docs: https://docs.cosmos.network
- Ethermint GitHub: https://github.com/evmos/ethermint
- Vana Blog Mainnet Live: https://blog.vana.org/vana-mainnet-is-live/

## Known Technical Limitations

Limitation: Bridge trust model bergantung pada validator set Vana (honest majority assumption); bukan trust-minimized seperti light-client bridge (HIGH)
Source: [Vana Whitepaper, https://vana.org/whitepaper.pdf; Vana Docs Bridge, https://docs.vana.org]

Limitation: Proof-of-Contribution verification quality bergantung pada connector implementation per Data DAO; tidak ada universal verification standard enforced at protocol level (HIGH)
Source: [Vana Whitepaper, https://vana.org/whitepaper.pdf; Vana Docs PoC, https://docs.vana.org]

Limitation: Data DAO raw data storage off-chain (IPFS/Arweave/cloud) — protocol tidak menjamin persistence atau availability; tanggung jawab per Data DAO (HIGH)
Source: [Vana Whitepaper, https://vana.org/whitepaper.pdf; Universal Connectors Docs, https://docs.vana.org]

Limitation: EVM execution throughput terbatas oleh single-threaded Ethermint EVM; tidak ada parallel execution (seperti Sei v2 atau Monad) (HIGH)
Source: [Ethermint GitHub, https://github.com/evmos/ethermint; Vana Whitepaper, https://vana.org/whitepaper.pdf]

Limitation: IBC channels ke chain lain belum sepenuhnya terdocumetasi secara publik yang aktif; relayer infrastructure community-run (MEDIUM)
Source: [Vana Docs IBC, https://docs.vana.org; Cosmos IBC Docs, https://ibc.cosmos.network]

Limitation: Tidak ada audit keamanan publik yang diumumkan untuk core modules, bridge, atau Data DAO contracts (HIGH)
Source: [Vana GitHub, https://github.com/vana-com; Vana Blog, https://blog.vana.org; Vana Docs, https://docs.vana.org]

Limitation: Validator set size dan decentralization metrics tidak terpublikasi dalam dashboard terpusat; explorer menunjukkan active set tapi tidak historical decentralization score (MEDIUM)
Source: [Vana Explorer, https://explorer.vana.org; Vana Docs Validator, https://docs.vana.org]

Limitation: Upgrade mechanism memerlukan on-chain governance proposal + validator coordination; tidak ada emergency patch mechanism terdocumentasi (MEDIUM)
Source: [Vana Whitepaper, https://vana.org/whitepaper.pdf; Cosmos SDK Governance, https://docs.cosmos.network]

Sources:
- Vana Whitepaper: https://vana.org/whitepaper.pdf
- Vana Docs: https://docs.vana.org
- Vana GitHub: https://github.com/vana-com
- Vana Blog: https://blog.vana.org
- Vana Explorer: https://explorer.vana.org
- Ethermint GitHub: https://github.com/evmos/ethermint
- Cosmos IBC Docs: https://ibc.cosmos.network
- Cosmos SDK Governance: https://docs.cosmos.network

## Official Technical Resources

Documentation: https://docs.vana.org
GitHub: https://github.com/vana-com
Developer Docs: https://docs.vana.org/developers
Universal Connectors SDK: https://docs.vana.org/connectors (SDK reference di docs; source di GitHub)
API Reference: https://docs.vana.org/api (JSON-RPC, REST, gRPC endpoints)
Whitepaper: https://vana.org/whitepaper.pdf
Block Explorer: https://explorer.vana.org
Portal (User Dashboard): https://portal.vana.org
Blog (Technical Announcements): https://blog.vana.org
Discord (Developer Community): https://discord.gg/vana

Sources:
- Vana Docs: https://docs.vana.org
- Vana GitHub: https://github.com/vana-com
- Vana Whitepaper: https://vana.org/whitepaper.pdf
- Vana Explorer: https://explorer.vana.org
- Vana Portal: https://portal.vana.org
- Vana Blog: https://blog.vana.org

## Summary

Architecture: Layer 1 (Cosmos SDK + Ethermint EVM + CometBFT BFT PoS); Modular (Consensus / Execution / Application layers); IBC-enabled; Ethereum bridge (HIGH)
Core Components: 10 komponen utama (CometBFT, Ethermint, PoC Module, Data DAO Contracts, Universal Connectors SDK, Vana Portal, Vana-Ethereum Bridge, Vana Explorer, IBC Module, Validator Node Software) — semua live di mainnet (HIGH)
Audit Count: 0 publik audit diumumkan (HIGH)
Major Upgrade Count: 4 major upgrades (Moksha Testnet 2023-07, Mainnet Genesis 2024-10-16, Data DAO Deployments 2024-10 to 2024-12, VANA TGE 2024-12-16) (HIGH)

Sources:
- Vana Whitepaper: https://vana.org/whitepaper.pdf
- Vana Blog Mainnet Live: https://blog.vana.org/vana-mainnet-is-live/
- Vana Blog Token Launch: https://blog.vana.org/vana-token-launch/
- Vana Blog Introducing Moksha: https://blog.vana.org/introducing-moksha-testnet/
- Vana Blog Data DAO Ecosystem: https://blog.vana.org/category/data-daos/
- Vana GitHub: https://github.com/vana-com
- Vana Explorer: https://explorer.vana.org

## Financial Intelligence
_ref: `docs/Ontology/Funding.md`, `docs/Ontology/Revenue.md`_

PROJECT: Vana

## Funding History

Funding Round: Early Funding Round (2023)
Date: 2023
Amount: tidak diungkap
Currency: USD
Lead Investor: Paradigm
Participating Investors: Polymorphic Capital; Coinbase Ventures; Polychain Capital; Dragonfly Capital
Valuation: tidak diungkap
Funding Type: Strategic / Private
Status: Completed
Sources: [Messari Vana Report, https://messari.io/report/vana] (MEDIUM) [Vana Blog, https://blog.vana.org] (MEDIUM)

Funding Round: VANA Token Generation Event (TGE)
Date: 2024-12-16
Amount: tidak diungkap (total raise via token sale tidak dipublikasikan terpisah dari TGE distribution)
Currency: VANA / USD
Lead Investor: N/A (public token launch)
Participating Investors: Community; early contributors; Data DAO participants
Valuation: tidak diungkap (FDV at launch tidak diumumkan resmi)
Funding Type: Public Sale / Token Launch
Status: Completed
Sources: [Vana Blog Token Launch, https://blog.vana.org/vana-token-launch/] (HIGH) [CoinGecko VANA, https://www.coingecko.com/en/coins/vana] (HIGH)

## Treasury

Current Treasury Size: tidak diungkap
Treasury Composition: tidak diungkap
Stablecoin Holdings: tidak diungkap
Native Token Holdings: tidak diungkap
Other Assets: tidak diungkap
Treasury Custodian: Vana Foundation (Cayman Islands foundation) — per struktur hukum; detail multi-sig / custodian arrangement tidak dipublikasikan
Sources: [Vana Foundation GitHub, https://github.com/vana-com] (MEDIUM) [Vana.org Team, https://vana.org/team] (MEDIUM) [Vana Whitepaper, https://vana.org/whitepaper.pdf] (MEDIUM)

## Revenue Model

Revenue Stream: Protocol Fees (Data DAO transaction fees / PoC verification fees)
Status: Planned / Not Live (whitepaper mentions fee mechanisms but no public confirmation of active fee collection on mainnet)
Sources: [Vana Whitepaper, https://vana.org/whitepaper.pdf] (MEDIUM)

Revenue Stream: Bridge Fees (Vana-Ethereum bridge transfer fees)
Status: Planned / Not Confirmed Live (bridge contracts exist; fee parameters governance-controlled; no public fee revenue dashboard)
Sources: [Vana Whitepaper, https://vana.org/whitepaper.pdf] (MEDIUM) [Vana Docs Bridge, https://docs.vana.org] (MEDIUM)

Revenue Stream: Validator Rewards / Staking Fees (commission on delegated stake)
Status: Live (CometBFT PoS staking active since mainnet 2024-10-16; validators earn block rewards + commission)
Sources: [Vana Blog Mainnet Live, https://blog.vana.org/vana-mainnet-is-live/] (HIGH) [Vana Explorer, https://explorer.vana.org] (HIGH) [CometBFT Docs, https://docs.cometbft.com] (HIGH)

Revenue Stream: Treasury Yield (staking rewards on Foundation-held VANA; potential DeFi yield on stablecoins)
Status: Planned / Not Confirmed (no public treasury management disclosure)
Sources: [Vana Whitepaper, https://vana.org/whitepaper.pdf] (MEDIUM)

Revenue Stream: Enterprise Services / Data Licensing (Data DAO data sales to buyers)
Status: Live at Data DAO level (r/datadao, Volara, etc. facilitate data sales; protocol takes no direct cut confirmed)
Sources: [Vana Blog Data DAO Ecosystem, https://blog.vana.org/category/data-daos/] (HIGH) [Messari Vana Report, https://messari.io/report/vana] (MEDIUM)

Revenue Stream: Grants (ecosystem grants from Foundation treasury)
Status: Planned / Ongoing (whitepaper references grant program; no public recipient list or amounts)
Sources: [Vana Whitepaper, https://vana.org/whitepaper.pdf] (MEDIUM)

## Revenue History

Tidak diungkap.
Sources: [Vana Blog, https://blog.vana.org] (HIGH) [Vana Docs, https://docs.vana.org] (HIGH) [Messari Vana Report, https://messari.io/report/vana] (MEDIUM)

## Fundraising Mechanism

VC Funding: Early 2023 round from Paradigm, Polymorphic Capital, Coinbase Ventures, Polychain Capital, Dragonfly Capital (completed)
Private Sale: Likely part of early funding round / token allocation to investors (not separately disclosed as distinct "private sale" event)
Public Sale: VANA TGE 2024-12-16 (public token launch with community allocation)
Launchpad: Tidak diungkap (no specific launchpad announced; TGE distribution via claim/portal)
Auction: Tidak diungkap
Community Sale: TGE included community allocation via Vana Portal / Data DAO participation
Grant: Ecosystem grants referenced in whitepaper; no public grant round announcements
Foundation: Vana Foundation holds treasony; funds development via Foundation resources
DAO Treasury: Individual Data DAOs (r/datadao, Volara, etc.) manage own treasuries from data sales
Protocol Revenue: Not yet active at protocol level (fees not confirmed live)
Bootstrapping: Initial development funded by founders pre-2023 funding round
Sources: [Messari Vana Report, https://messari.io/report/vana] (MEDIUM) [Vana Blog Token Launch, https://blog.vana.org/vana-token-launch/] (HIGH) [Vana Whitepaper, https://vana.org/whitepaper.pdf] (MEDIUM) [Vana Blog Data DAO Ecosystem, https://blog.vana.org/category/data-daos/] (HIGH)

## Token Sale

Private Sale: Included in early 2023 funding round (investor token allocation); exact terms, price, allocation percentage tidak diungkap
Public Sale: VANA TGE 2024-12-16 (public launch); distribution via claim portal; no fixed-price public sale announced
Launchpad: Tidak diungkap (no launchpad partnership announced)
Auction: Tidak diungkap
Community Sale: TGE community allocation (exact % tidak diungkap); distributed to Data DAO participants, testnet users, ecosystem contributors
Tanggal: 2024-12-16 (TGE)
Status: Completed
Sources: [Vana Blog Token Launch, https://blog.vana.org/vana-token-launch/] (HIGH) [CoinGecko VANA, https://www.coingecko.com/en/coins/vana] (HIGH) [Messari Vana Report, https://messari.io/report/vana] (MEDIUM) [Vana Whitepaper, https://vana.org/whitepaper.pdf] (MEDIUM)

Catatan: Distribusi token, vesting schedule, dan alokasi detail adalah Phase 6 — tidak dibahas di sini.

## Financial Dependencies

VC: Paradigm; Polymorphic Capital; Coinbase Ventures; Polychain Capital; Dragonfly Capital (early funding round 2023)
Foundation: Vana Foundation (Cayman Islands) — holds treasury, funds protocol development
Grant Program: Vana Foundation ecosystem grants (referenced in whitepaper; no public deployment data)
Revenue: Data DAO-level revenue (data sales) — not protocol revenue; validator staking rewards (protocol-level, live)
DAO: r/datadao; Volara; Flirtual; DataPig; Kappa — independent treasuries from data monetization
Sources: [Messari Vana Report, https://messari.io/report/vana] (MEDIUM) [Vana Blog Data DAO Ecosystem, https://blog.vana.org/category/data-daos/] (HIGH) [Vana Whitepaper, https://vana.org/whitepaper.pdf] (MEDIUM) [Vana Blog Token Launch, https://blog.vana.org/vana-token-launch/] (HIGH)

## Financial Risk

Treasury Concentration: Tidak dapat diverifikasi (treasury size/composition tidak diungkap; tidak bisa menilai konsentrasi)
Revenue Decline: Tidak ada revenue history protokol untuk dievaluasi; Data DAO revenue bergantung pada permintaan pembeli data
Funding Dependency: Protokol bergantung pada Vana Foundation treasury (sumber: early VC round + TGE allocation) untuk pengembangan berkelanjutan; tidak ada protocol fee revenue live
Debt: Tidak diungkap (tidak ada disclosure pinjaman / hutang)
Legal Financial Risk: Status regulasi Data DAO di berbagai yurisdiksi tidak pasti (whitepaper mengakui ketidakpastian regulasi); Cayman Islands foundation structure may face regulatory scrutiny
Audit Risk: Tidak ada audit keamanan publik yang diumumkan untuk smart contracts, bridge, atau core modules (financial risk jika ditemukan vulnerability)
Sources: [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH) [Vana GitHub, https://github.com/vana-com] (HIGH) [Vana Blog, https://blog.vana.org] (HIGH) [Messari Vana Report, https://messari.io/report/vana] (MEDIUM)

## Official Financial Resources

Official Blog: https://blog.vana.org
Transparency Report: Tidak tersedia (no dedicated transparency report page)
Treasury Dashboard: Tidak tersedia (no public treasury dashboard)
Governance: https://docs.vana.org/governance (governance docs; no financial dashboard)
Messari: https://messari.io/report/vana
Token Terminal: Tidak terdaftar (as of research cutoff)
DefiLlama: Tidak terdaftar (as of research cutoff; Vana L1 not indexed)
CryptoRank: https://cryptorank.io/ico/vana (may have TGE data; verify independently)
Whitepaper: https://vana.org/whitepaper.pdf
CoinGecko: https://www.coingecko.com/en/coins/vana
Vana Explorer: https://explorer.vana.org (on-chain data only)
Vana Portal: https://portal.vana.org (user dashboard; not financial reporting)

## Summary

Total Funding Raised: tidak diungkap (early 2023 VC round amount not disclosed; TGE raise not separately disclosed)
Funding Rounds: 2 teridentifikasi (Early VC Round 2023; VANA TGE 2024-12-16)
Treasury Status: tidak diungkap (size, composition, custodian details not public)
Revenue Sources: Validator staking rewards (live); Data DAO data sales (live at DAO level); Protocol fees / bridge fees / treasury yield (planned per whitepaper, not confirmed live)
Revenue Availability: Tidak diungkap (no revenue history published)

## Token Intelligence
_ref: `docs/Ontology/Tokenomics.md`_

PROJECT: Vana

## Token Information

Official Token Name: VANA
Symbol: VANA
Token Standard: ERC-20 (Ethereum); Native token (Vana L1, Cosmos SDK-based chain)
Blockchain: Vana Mainnet (native L1, EVM-compatible, Cosmos SDK-based); Ethereum Mainnet (ERC-20 representation)
Contract Address: 0x5Af... (Ethereum mainnet ERC-20) — alamat lengkap tidak dipublikasikan dalam sumber resmi yang terverifikasi; native VANA pada Vana L1 tidak memiliki alamat kontrak ERC-20 (native coin)
Decimals: 18 (standar ERC-20 / Cosmos SDK coin) — tidak diketahui secara eksplisit dari dokumentasi resmi
Status: Live (TGE 2024-12-16)
Sources:
- [Vana Blog Token Launch, https://blog.vana.org/vana-token-launch/] (HIGH)
- [CoinGecko VANA, https://www.coingecko.com/en/coins/vana] (HIGH)
- [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH)
- [Vana Explorer, https://explorer.vana.org] (HIGH)

## Supply

Maximum Supply: tidak diketahui (tidak diungkap dalam whitepaper, blog resmi, atau CoinGecko)
Total Supply: tidak diketahui (tidak diungkap; TGE distribution tidak mencakup total supply number)
Circulating Supply: tidak diketahui (tidak diungkap; CoinGecko menampilkan "Circulating Supply" tetapi tanpa angka terverifikasi pada cutoff penelitian)
Initial Supply: tidak diketahui (jumlah token yang dimintakan pada genesis/TGE tidak dipublikasikan)
Supply Type: Inflationary (PoS staking rewards menghasilkan emisian token baru; whitepaper menyebutkan staking rewards dan inflation mechanism) — detail parameter inflation tidak diungkap
Sources:
- [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH)
- [Vana Blog Token Launch, https://blog.vana.org/vana-token-launch/] (HIGH)
- [CoinGecko VANA, https://www.coingecko.com/en/coins/vana] (MEDIUM)
- [Vana Explorer, https://explorer.vana.org] (MEDIUM)
- [CometBFT Docs, https://docs.cometbft.com] (HIGH) — PoS chains secara inheren inflationary melalui block rewards

## Distribution

Community: Planned — persentase tidak diungkap; whitepaper menyebutkan community allocation tetapi tanpa angka spesifik
Team: Planned — persentase tidak diungkap; whitepaper menyebutkan team allocation dengan vesting tetapi tanpa angka spesifik
Investors: Planned — persentase tidak diungkap; early 2023 funding round (Paradigm, Polymorphic Capital, Coinbase Ventures, Polychain Capital, Dragonfly Capital) termasuk token allocation; detail tidak diungkap
Foundation: Planned — persentase tidak diungkap; Vana Foundation (Cayman Islands) memegang treasury token untuk pengembangan ekosistem
Treasury: Planned — persentase tidak diungkap; Foundation treasury dan/atau protocol treasury terpisah tidak dibedakan dalam publikasi
Ecosystem: Planned — persentase tidak diungkap; whitepaper menyebutkan ecosystem fund, grants, Data DAO incentives
Advisors: Planned — persentase tidak diungkap; Jesse Walden (Advisor) kemungkinan memiliki allocation; tidak dikonfirmasi
Other: tidak diketahui — tidak ada kategori lain yang diidentifikasi dari sumber resmi
Sources:
- [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH) — menyebutkan kategori alokasi tanpa persentase
- [Vana Blog Token Launch, https://blog.vana.org/vana-token-launch/] (HIGH) — tidak mencantumkan breakdown distribusi
- [Messari Vana Report, https://messari.io/report/vana] (MEDIUM) — merujuk tokenomics tapi tidak mempublikasikan tabel alokasi lengkap
- [CoinGecko VANA, https://www.coingecko.com/en/coins/vana] (MEDIUM) — tidak menampilkan distribusi alokasi

## Vesting Schedule

Category: Team
Cliff: tidak diketahui
Vesting: tidak diketahui
Unlock Frequency: tidak diketahui
Current Status: Planned (belum diverifikasi on-chain)
Sources: [Vana Whitepaper, https://vana.org/whitepaper.pdf] (MEDIUM) — menyebutkan vesting untuk team tusi tanpa detail

Category: Investors
Cliff: tidak diketahui
Vesting: tidak diketahui
Unlock Frequency: tidak diketahui
Current Status: Planned (belum diverifikasi on-chain)
Sources: [Vana Whitepaper, https://vana.org/whitepaper.pdf] (MEDIUM) — menyebutkan vesting untuk investor tanpa detail

Category: Advisors
Cliff: tidak diketahui
Vesting: tidak diketahui
Unlock Frequency: tidak diketahui
Current Status: Planned (belum diverifikasi on-chain)
Sources: [Vana Whitepaper, https://vana.org/whitepaper.pdf] (LOW) — inferensi dari praktik standar; tidak eksplisit

Category: Foundation / Treasury
Cliff: tidak diketahui
Vesting: tidak diketahui
Unlock Frequency: tidak diketahui
Current Status: Planned (belum diverifikasi on-chain)
Sources: [Vana Whitepaper, https://vana.org/whitepaper.pdf] (MEDIUM) — menyebutkan foundation allocation tanpa schedule

Category: Ecosystem / Community
Cliff: tidak diketahui
Vesting: tidak diketahui
Unlock Frequency: tidak diketahui
Current Status: Planned (belum diverifikasi on-chain)
Sources: [Vana Whitepaper, https://vana.org/whitepaper.pdf] (MEDIUM) — menyebutkan ecosystem fund tanpa schedule

Catatan: Tidak ada vesting schedule detail (cliff, durasi, frekuensi unlock) yang dipublikasikan oleh Vana Foundation, whitepaper, atau block explorer. Semua kategori bertanda "Planned" dan "tidak diketahui" untuk parameter numerik.

## TGE

TGE Date: 2024-12-16
Initial Unlock: tidak diketahui (persentase atau jumlah token yang unlocked pada TGE tidak diungkap)
Unlocked Categories: tidak diketahui (kategori mana yang unlocked pada TGE vs locked tidak diungkap)
Launch Platform: Vana Portal (claim portal) — https://portal.vana.org; CEX listings dimulai segera setelah TGE (exchange spesifik tidak diumumkan resmi)
Status: Completed
Sources:
- [Vana Blog Token Launch, https://blog.vana.org/vana-token-launch/] (HIGH) — EV-016
- [CoinGecko VANA, https://www.coingecko.com/en/coins/vana] (HIGH) — listing date 2024-12-16
- [Vana Portal, https://portal.vana.org] (HIGH) — claim interface
- [Vana Blog Data DAO Ecosystem, https://blog.vana.org/category/data-daos/] (MEDIUM) — community allocation via Data DAO participation

## Utility

Utility: Governance
Deskripsi: Token VANA digunakan untuk voting pada on-chain governance proposals (parameter changes, upgrades, treasury spending) di Vana L1
Status: Live (governance module aktif sejak mainnet 2024-10-16; TGE 2024-12-16 memperluas token holder base)
Sources: [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH); [Vana Docs Governance, https://docs.vana.org/governance] (HIGH)

Utility: Staking
Deskripsi: VANA di-stake ke validator untuk network security (CometBFT PoS); delegator menerima staking rewards; validator memerlukan stake untuk consensus participation
Status: Live (sejak mainnet 2024-10-16)
Sources: [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH); [Vana Blog Mainnet Live, https://blog.vana.org/vana-mainnet-is-live/] (HIGH); [CometBFT Docs, https://docs.cometbft.com] (HIGH)

Utility: Validator
Deskripsi: Menjadi validator memerlukan VANA stake (self-stake + delegation); top N by stake menjadi active set; validator memproduksi block dan menerima rewards
Status: Live (sejak mainnet 2024-10-16)
Sources: [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH); [Vana Explorer, https://explorer.vana.org] (HIGH)

Utility: Fee Payment
Deskripsi: VANA digunakan sebagai gas token untuk transaksi di Vana L1 (EVM execution via Ethermint); bridge fees mungkin denominated in VANA
Status: Live (gas token sejak mainnet); Bridge fees: Planned / Not Confirmed Live
Sources: [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH); [Vana Docs Bridge, https://docs.vana.org] (MEDIUM)

Utility: Incentive
Deskripsi: VANA dialokasikan sebagai insentif bagi kontributor data di Data DAO (Proof-of-Contribution rewards); r/datadao, Volara, Flirtual, DataPig, Kappa mendistribusikan reward dalam VANA atau Data DAO token sendiri
Status: Live (Data DAO aktif di mainnet mendistribusikan reward)
Sources: [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH); [Vana Blog Data DAO Ecosystem, https://blog.vana.org/category/data-daos/] (HIGH); [Vana Docs PoC, https://docs.vana.org] (HIGH)

Utility: Reward
Deskripsi: Staking rewards (inflationary emissions) dibayarkan dalam VANA ke validator dan delegator; Data DAO reward pool mungkin menggunakan VANA dari ecosystem allocation
Status: Live (staking rewards); Data DAO reward: Live per DAO
Sources: [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH); [CometBFT Docs, https://docs.cometbft.com] (HIGH)

Utility: Collateral
Deskripsi: Tidak diketahui apakah VANA digunakan sebagai collateral di DeFi protocols di Vana L1; tidak diungkap dalam whitepaper
Status: tidak diketahui
Sources: [Vana Whitepaper, https://vana.org/whitepaper.pdf] (MEDIUM) — tidak menyebut collateral use case

Utility: Liquidity
Deskripsi: VANA menyediakan likuiditas di DEX/CEX untuk trading; bridge memerlukan likuiditas VANA di kedua sisi (Ethereum dan Vana L1)
Status: Live (CEX listing sejak 2024-12; DEX likuiditas kemungkinan ada)
Sources: [Vana Blog Token Launch, https://blog.vana.org/vana-token-launch/] (HIGH); [CoinGecko VANA, https://www.coingecko.com/en/coins/vana] (HIGH)

Utility: Security
Deskripsi: VANA staking mengamankan network melalui PoS (slashing risk untuk validator yang double-sign atau downtime); economic security proporsional dengan total VANA staked
Status: Live (sejak mainnet 2024-10-16)
Sources: [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH); [CometBFT Docs, https://docs.cometbft.com] (HIGH)

## Governance

Governance Model: On-chain governance via Cosmos SDK governance module; token-weighted voting (1 VANA = 1 vote) melalui staked/delegated token
Voting System: Proposal submission → Deposit period → Voting period (parameter governance-controlled) → Execution jika passed; standard Cosmos SDK governance flow
Voting Power: Berdasarkan VANA yang di-stake (bonded token); delegator voting power mengikuti validator choice kecuali delegator override (standard Cosmos SDK)
Delegation: Didukung; token holder bisa delegate ke validator; validator voting power = total stake (self + delegated); redelegation / unbonding period berlaku (parameter governance-controlled)
Proposal System: On-chain proposal submission memerlukan deposit minimum (parameter); jenis proposal: ParameterChange, SoftwareUpgrade, TextProposal, CommunityPoolSpend, dll. (Cosmos SDK standard)
Treasury Governance: Community pool (jika diaktifkan) dikontrol via governance proposals; Vana Foundation treasury terpisah dari protocol treasury — detail tidak diungkap
Status: Live (governance module aktif sejak mainnet 2024-10-16; TGE memperluas participation)
Sources:
- [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH)
- [Vana Docs Governance, https://docs.vana.org/governance] (HIGH)
- [Cosmos SDK Governance, https://docs.cosmos.network/main/build/modules/gov] (HIGH)
- [Vana Blog Mainnet Live, https://blog.vana.org/vana-mainnet-is-live/] (HIGH)

## Inflation / Deflation

Inflation Mechanism: PoS block rewards (staking rewards) memintakan VANA baru per block; inflation rate ditentukan oleh parameter governance (target bonded ratio, blocks per year, reward distribution) — parameter spesifik tidak diungkap
Emission Schedule: Tidak diungkap; tidak ada emission schedule publik (tahun per tahun, persentase per tahun)
Burn Mechanism: Tidak diungkap; whitepaper tidak menyebutkan token burn mechanism; EIP-1559 style fee burn mungkin ada di EVM layer (base fee burned) tetapi tidak dikonfirmasi untuk VANA native
Buyback: Tidak diungkap; tidak ada buyback program yang diumumkan
Supply Reduction: Tidak diungkap; tidak ada mekanisme supply reduction (burn, buyback, dll.) yang dikonfirmasi
Status: Inflationary (staking rewards live); Burn/Buyback: tidak diketahui / tidak diungkap
Sources:
- [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH) — menyebutkan staking rewards, tidak menyebut burn/buyback
- [Vana Blog Token Launch, https://blog.vana.org/vana-token-launch/] (HIGH) — tidak membahas inflation parameters
- [Ethermint GitHub, https://github.com/evmos/ethermint] (MEDIUM) — EVM fee market EIP-1559; base fee burn behavior tergantung konfigurasi chain
- [CometBFT Docs, https://docs.cometbft.com] (HIGH) — PoS inflation mechanism standard

## Holder Distribution

Top Holder Concentration: tidak diketahui (tidak ada holder distribution report resmi; block explorer menampilkan top accounts tetapi tidak teragregasi sebagai kategori)
Foundation Holding: tidak diketahui (jumlah VANA yang dipegang Vana Foundation tidak diungkap)
Investor Holding: tidak diketahui (alokasi investor dari early 2023 round tidak diungkap; vesting status tidak diverifikasi on-chain)
Treasury Holding: tidak diketahui (protocol treasury vs foundation treasury tidak dibedakan publik)
Community Holding: tidak diketahui (community allocation TGE tidak diungkap; circulating supply tidak diketahui)
Whale Concentration: tidak diketahui (tidak ada analisis holder concentration yang dipublikasikan)
Sources:
- [Vana Explorer, https://explorer.vana.org] (MEDIUM) — menampilkan top accounts raw tapi tidak kategorisasi
- [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH) — tidak mencantumkan holder distribution
- [Vana Blog Token Launch, https://blog.vana.org/vana-token-launch/] (HIGH) — tidak mencantumkan holder distribution
- [Messari Vana Report, https://messari.io/report/vana] (MEDIUM) — tidak mencantumkan holder distribution detail

## Major Token Events

Date: 2024-10-16
Event: Vana Mainnet Genesis — Native VANA token minted pada genesis; validator set mulai menerima staking rewards
Description: Mainnet diluncurkan dengan VANA sebagai native gas dan staking token; TGE belum terjadi (VANA belum transferable/tradable di Ethereum)
Status: Completed
Related Historical Event ID: EV-013
Sources: [Vana Blog Mainnet Live, https://blog.vana.org/vana-mainnet-is-live/] (HIGH); [Vana Explorer, https://explorer.vana.org] (HIGH)

Date: 2024-12-16
Event: VANA Token Generation Event (TGE) & Public Launch
Description: VANA ERC-20 deployed di Ethereum; TGE distribution via Vana Portal claim; bridge activated untuk two-way transfer; CEX listings dimulai; token menjadi transferable dan tradable
Status: Completed
Related Historical Event ID: EV-016
Sources: [Vana Blog Token Launch, https://blog.vana.org/vana-token-launch/] (HIGH); [CoinGecko VANA, https://www.coingecko.com/en/coins/vana] (HIGH); [Vana Portal, https://portal.vana.org] (HIGH)

Date: 2024-12 (bulan yang sama)
Event: VANA Listing di Centralized Exchanges (CEX)
Description: Token VANA mulai terdaftar di berbagai CEX menyediakan likuiditas pasar; exchange spesifik tidak diumumkan resmi
Status: Completed
Related Historical Event ID: EV-017
Sources: [Vana Blog Token Launch, https://blog.vana.org/vana-token-launch/] (HIGH); [CoinGecko VANA, https://www.coingecko.com/en/coins/vana] (HIGH)

Date: 2023-07
Event: Moksha Testnet Launch — Test VANA token digunakan untuk testing staking, governance, Data DAO rewards
Description: Testnet token (bukan mainnet VANA) digunakan untuk testing mekanisme; tidak memiliki nilai ekonomis
Status: Completed (deprecated after mainnet)
Related Historical Event ID: EV-004
Sources: [Vana Blog Introducing Moksha, https://blog.vana.org/introducing-moksha-testnet/] (HIGH); [Vana Docs, https://docs.vana.org] (HIGH)

Date: 2023 (selama testnet/mainnet development)
Event: Data DAO Smart Contract Deployments (r/datadao, Volara, Flirtual, DataPig, Kappa) — masing-masing mungkin memiliki reward token sendiri atau menggunakan VANA
Description: Data DAO contracts deployed secara bertahap; reward distribution mekanisme menggunakan VANA dan/atau Data DAO native token
Status: Completed (mainnet deployments 2024-10 hingga 2024-12)
Related Historical Event ID: EV-006, EV-007, EV-008, EV-009, EV-010
Sources: [Vana Blog Data DAO Ecosystem, https://blog.vana.org/category/data-daos/] (HIGH); [Vana Explorer Contracts, https://explorer.vana.org] (HIGH)

## Official Token Resources

Official Documentation: https://docs.vana.org
Whitepaper: https://vana.org/whitepaper.pdf
Governance: https://docs.vana.org/governance
Explorer: https://explorer.vana.org
Contract: https://explorer.vana.org (native VANA); Ethereum ERC-20 contract address lengkap tidak dipublikasikan di sumber resmi terverifikasi
GitHub: https://github.com/vana-com
Dashboard: https://portal.vana.org (user dashboard, bukan token analytics dashboard)

## Summary

Status: Live (TGE 2024-12-16; mainnet native token sejak 2024-10-16)
Supply Type: Inflationary (PoS staking rewards)
Total Supply: tidak diketahui (tidak diungkap)
Distribution Categories: Community, Team, Investors, Foundation, Treasury, Ecosystem, Advisors — semua persentase tidak diungkap
Utility Count: 8 utilitas teridentifikasi (Governance, Staking, Validator, Fee Payment, Incentive, Reward, Liquidity, Security) — Collateral tidak diketahui
Governance: On-chain (Cosmos SDK governance module), token-weighted voting, delegation supported, live since mainnet
Major Token Events: 5 (Moksha Testnet 2023-07, Mainnet Genesis 2024-10-16, TGE 2024-12-16, CEX Listings 2024-12, Data DAO Deployments 2024-10 to 2024-12)

## Ecosystem Intelligence
_ref: `docs/Ontology/Community.md`, `docs/Ontology/Ecosystem.md`_

PROJECT: Vana

## Ecosystem Position

Primary Sector: Data Liquidity / Data DAO Infrastructure
Secondary Sector: Layer 1 Blockchain (EVM-compatible, Cosmos SDK-based)
Primary Chain: Vana Mainnet
Supported Chains: Ethereum (via Vana-Ethereum Bridge, ERC-20 VANA); Cosmos ecosystem chains (via IBC, planned/active channels not publicly documented)
Sources:
- [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH)
- [Vana Docs Architecture, https://docs.vana.org] (HIGH)
- [Vana Blog Mainnet Live, https://blog.vana.org/vana-mainnet-is-live/] (HIGH)
- [Vana Blog Data DAO Ecosystem, https://blog.vana.org/category/data-daos/] (HIGH)

## External Dependencies

Dependency Name: Cosmos SDK
Dependency Type: SDK
Purpose: Core application framework untuk blockchain layer (consensus, staking, governance, IBC, custom modules PoC/Bridge)
Criticality: Critical
Status: Live
Related Entity: Cosmos SDK (technology, not separate entity in Phase 2)
Related Technology Component: Cosmos SDK application layer; Validator Node Software; Proof-of-Contribution Module; IBC Module
Sources:
- [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH)
- [Vana GitHub, https://github.com/vana-com] (HIGH)
- [Cosmos SDK Docs, https://docs.cosmos.network] (HIGH)

Dependency Name: CometBFT (Tendermint)
Dependency Type: Protocol
Purpose: BFT consensus engine untuk block production dan finality; validator set management
Criticality: Critical
Status: Live
Related Entity: CometBFT (technology)
Related Technology Component: CometBFT Consensus Engine; Validator Node Software
Sources:
- [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH)
- [CometBFT Docs, https://docs.cometbft.com] (HIGH)
- [Vana Blog Mainnet Live, https://blog.vana.org/vana-mainnet-is-live/] (HIGH)

Dependency Name: Ethermint
Dependency Type: Protocol
Purpose: EVM execution module pada Cosmos SDK; menyediakan Ethereum JSON-RPC compatibility dan Solidity smart contract support
Criticality: Critical
Status: Live
Related Entity: Ethermint (technology, Evmos team)
Related Technology Component: Ethermint EVM Module; EVM execution environment; Data DAO Smart Contracts
Sources:
- [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH)
- [Ethermint GitHub, https://github.com/evmos/ethermint] (HIGH)
- [Vana Docs Developers, https://docs.vana.org] (HIGH)

Dependency Name: Vana-Ethereum Bridge
Dependency Type: Bridge
Purpose: Two-way peg VANA token antara Ethereum mainnet (ERC-20) dan Vana L1 (native); validator set attestation untuk mint/burn
Criticality: Critical
Status: Live
Related Entity: Vana-Ethereum Bridge (protocol component, not separate entity)
Related Technology Component: Vana-Ethereum Bridge; Bridge contracts (Ethereum side + Vana side)
Sources:
- [Vana Blog Mainnet Live, https://blog.vana.org/vana-mainnet-is-live/] (HIGH)
- [Vana Docs Bridge, https://docs.vana.org] (HIGH)
- [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH)

Dependency Name: IBC (Inter-Blockchain Communication)
Dependency Type: Protocol
Purpose: Cross-chain communication dengan chain lain di ecosystem Cosmos (Osmosis, Celestia, dll.)
Criticality: High
Status: Live (enabled on mainnet; active channels not publicly documented)
Related Entity: IBC Protocol (technology)
Related Technology Component: IBC Module; Validator Node Software
Sources:
- [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH)
- [Cosmos IBC Docs, https://ibc.cosmos.network] (HIGH)
- [Vana Docs, https://docs.vana.org] (MEDIUM)

Dependency Name: IPFS / Arweave / Cloud Storage
Dependency Type: Infrastructure
Purpose: Off-chain data storage untuk Data DAO raw data (encrypted); protocol tidak menjamin persistence — tanggung jawab per Data DAO
Criticality: High
Status: Live (per Data DAO choice)
Related Entity: IPFS; Arweave; various cloud providers (not individual entities in Phase 2)
Related Technology Component: Universal Connectors SDK; Data DAO Smart Contracts; Data storage architecture
Sources:
- [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH)
- [Universal Connectors Docs, https://docs.vana.org] (HIGH)
- [Vana Blog Data DAO Ecosystem, https://blog.vana.org/category/data-daos/] (MEDIUM)

Dependency Name: Vana Foundation
Dependency Type: Foundation
Purpose: Entitas hukum yang mengelola treasury, pengembangan protokol, ekosistem Data DAO, governance; Cayman Islands foundation
Criticality: Critical
Status: Live
Related Entity: Vana Foundation
Related Technology Component: Treasury management; Grant program (referenced); Protocol upgrades via governance
Sources:
- [Vana Foundation GitHub, https://github.com/vana-com] (HIGH)
- [Vana.org Team, https://vana.org/team] (HIGH)
- [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH)

Dependency Name: Paradigm
Dependency Type: Investor
Purpose: Early funding round 2023; strategic support untuk pengembangan L1 data liquidity
Criticality: High
Status: Live (investor relationship)
Related Entity: Paradigm
Related Technology Component: Protocol development funding
Sources:
- [Messari Vana Report, https://messari.io/report/vana] (MEDIUM)
- [Vana Blog, https://blog.vana.org] (MEDIUM)

Dependency Name: Polymorphic Capital
Dependency Type: Investor
Purpose: Early funding round 2023; mitra strategis ekosistem Data DAO
Criticality: High
Status: Live
Related Entity: Polymorphic Capital
Related Technology Component: Protocol development funding; Data DAO ecosystem support
Sources:
- [Vana Blog Data DAO Ecosystem, https://blog.vana.org/category/data-daos/] (HIGH)
- [Messari Vana Report, https://messari.io/report/vana] (MEDIUM)

Dependency Name: Coinbase Ventures
Dependency Type: Investor
Purpose: Early funding round 2023; dukungan infrastruktur data portability
Criticality: High
Status: Live
Related Entity: Coinbase Ventures
Related Technology Component: Protocol development funding
Sources:
- [Messari Vana Report, https://messari.io/report/vana] (MEDIUM)
- [Vana Blog, https://blog.vana.org] (MEDIUM)

Dependency Name: Polychain Capital
Dependency Type: Investor
Purpose: Early funding round 2023; pembiayaan protokol data liquidity layer
Criticality: High
Status: Live
Related Entity: Polychain Capital
Related Technology Component: Protocol development funding
Sources:
- [Messari Vana Report, https://messari.io/report/vana] (MEDIUM)
- [Vana Blog, https://blog.vana.org] (MEDIUM)

Dependency Name: Dragonfly Capital
Dependency Type: Investor
Purpose: Early funding round 2023; mendanai Vana Network dan ekosistem Data DAO
Criticality: High
Status: Live
Related Entity: Dragonfly Capital
Related Technology Component: Protocol development funding
Sources:
- [Messari Vana Report, https://messari.io/report/vana] (MEDIUM)
- [Vana Blog, https://blog.vana.org] (MEDIUM)

Dependency Name: Jesse Walden
Dependency Type: Person (Advisor)
Purpose: Advisor strategis protokol data liquidity dan tokenomics; pendiri Variant Fund
Criticality: Medium
Status: Live
Related Entity: Jesse Walden
Related Technology Component: Strategic advisory; tokenomics guidance
Sources:
- [Vana.org Team, https://vana.org/team] (MEDIUM)
- [Messari Vana Report, https://messari.io/report/vana] (MEDIUM)

Dependency Name: CoinGecko
Dependency Type: Infrastructure
Purpose: Penyedia data pasar kripto melacak harga, volume, metadata token VANA sejak TGE
Criticality: Low
Status: Live
Related Entity: CoinGecko
Related Technology Component: Market data visibility
Sources:
- [CoinGecko VANA, https://www.coingecko.com/en/coins/vana] (HIGH)
- [Vana Blog Token Launch, https://blog.vana.org/vana-token-launch/] (HIGH)

Dependency Name: Messari
Dependency Type: Research Lab
Purpose: Platform riset kripto menerbitkan Vana Report mencakup tokenomics, arsitektur, ekosistem
Criticality: Low
Status: Live
Related Entity: Messari
Related Technology Component: Independent research coverage
Sources:
- [Messari Vana Report, https://messari.io/report/vana] (HIGH)
- [Vana Blog, https://blog.vana.org] (MEDIUM)

Dependency Name: GitHub
Dependency Type: Infrastructure
Purpose: Hosting repositori kode sumber terbuka Vana (protokol, smart contract, SDK, tooling)
Criticality: High
Status: Live
Related Entity: Vana GitHub
Related Technology Component: All open source components; CI/CD via GitHub Actions
Sources:
- [Vana GitHub, https://github.com/vana-com] (HIGH)
- [Vana Docs, https://docs.vana.org] (HIGH)

Dependency Name: Docker
Dependency Type: Infrastructure
Purpose: Containerization untuk node deployment, CI/CD pipeline
Criticality: Medium
Status: Live
Related Entity: Docker (technology)
Related Technology Component: Validator Node Software deployment; CI/CD
Sources:
- [Vana GitHub, https://github.com/vana-com] (HIGH)
- [Cosmos SDK Docs, https://docs.cosmos.network] (MEDIUM)

Dependency Name: Kubernetes
Dependency Type: Infrastructure
Purpose: Production validator node orchestration (assumed standard Cosmos stack; not explicitly confirmed)
Criticality: Medium
Status: Planned / Assumed
Related Entity: Kubernetes (technology)
Related Technology Component: Validator Node Software deployment
Sources:
- [Cosmos SDK Docs, https://docs.cosmos.network] (MEDIUM)
- [Vana Docs Validator, https://docs.vana.org] (MEDIUM)

Dependency Name: Prometheus / Grafana
Dependency Type: Infrastructure
Purpose: Monitoring dan alerting untuk validator nodes (standard Cosmos stack)
Criticality: Medium
Status: Live (assumed standard)
Related Entity: Prometheus; Grafana (technologies)
Related Technology Component: Validator Node Software observability
Sources:
- [Cosmos SDK Docs, https://docs.cosmos.network] (MEDIUM)
- [CometBFT Docs, https://docs.cometbft.com] (MEDIUM)

Dependency Name: PostgreSQL
Dependency Type: Infrastructure
Purpose: Indexer / explorer backend database (Blockscout-based explorer)
Criticality: Medium
Status: Live
Related Entity: PostgreSQL (technology)
Related Technology Component: Vana Explorer backend
Sources:
- [Vana Explorer, https://explorer.vana.org] (MEDIUM)
- [Blockscout GitHub, https://github.com/blockscout/blockscout] (MEDIUM)

Dependency Name: Redis
Dependency Type: Infrastructure
Purpose: Caching layer untuk RPC / indexer (assumed standard)
Criticality: Low
Status: Assumed
Related Entity: Redis (technology)
Related Technology Component: RPC performance; indexer caching
Sources:
- [Cosmos SDK Docs, https://docs.cosmos.network] (LOW)
- [Ethermint GitHub, https://github.com/evmos/ethermint] (LOW)

Dependency Name: React / Next.js
Dependency Type: SDK
Purpose: Vana Portal frontend framework
Criticality: High
Status: Live
Related Entity: React; Next.js (technologies)
Related Technology Component: Vana Portal (Frontend)
Sources:
- [Vana Portal, https://portal.vana.org] (HIGH)
- [Vana Docs, https://docs.vana.org] (HIGH)

Dependency Name: TypeScript / JavaScript
Dependency Type: SDK
Purpose: Universal Connectors SDK, developer tooling, testing frameworks
Criticality: High
Status: Live
Related Entity: TypeScript (technology)
Related Technology Component: Universal Connectors SDK; Vana Portal
Sources:
- [Vana GitHub, https://github.com/vana-com] (HIGH)
- [Vana Docs Connectors, https://docs.vana.org] (HIGH)

Dependency Name: Python
Dependency Type: SDK
Purpose: Data connector scripts, data processing pipelines, research/analytics tooling
Criticality: Medium
Status: Live
Related Entity: Python (technology)
Related Technology Component: Universal Connectors SDK; data processing
Sources:
- [Vana GitHub, https://github.com/vana-com] (MEDIUM)
- [Vana Docs Connectors, https://docs.vana.org] (MEDIUM)

Dependency Name: Protobuf / gRPC
Dependency Type: Protocol
Purpose: Serialization, gRPC interfaces, ABCI interface, client APIs (Cosmos SDK standard)
Criticality: High
Status: Live
Related Entity: Protobuf; gRPC (technologies)
Related Technology Component: All Cosmos SDK modules; Validator Node Software APIs
Sources:
- [Cosmos SDK Docs, https://docs.cosmos.network] (HIGH)
- [Vana GitHub, https://github.com/vana-com] (HIGH)

Dependency Name: Hardhat / Foundry
Dependency Type: SDK
Purpose: Smart contract development, testing, deployment untuk Solidity contracts
Criticality: High
Status: Live
Related Entity: Hardhat; Foundry (technologies)
Related Technology Component: Data DAO Smart Contracts; Bridge contracts; VANA token contracts
Sources:
- [Vana GitHub, https://github.com/vana-com] (HIGH)
- [Vana Docs Developers, https://docs.vana.org] (HIGH)

Dependency Name: Ignite CLI
Dependency Type: SDK
Purpose: Scaffold dan development tooling untuk Cosmos chains
Criticality: Medium
Status: Live (assumed used for scaffolding)
Related Entity: Ignite CLI (technology)
Related Technology Component: Cosmos SDK module development
Sources:
- [Ignite CLI, https://ignite.com/cli] (MEDIUM)
- [Cosmos SDK Docs, https://docs.cosmos.network] (MEDIUM)

## Major Integrations

Integration Name: Vana-Ethereum Bridge
Integrated With: Ethereum Mainnet
Purpose: Two-way transfer VANA token (ERC-20 ↔ native); validator set attestation untuk mint/burn
Status: Live
Related Historical Event ID: EV-013 (Mainnet launch included bridge); EV-016 (TGE activated bridge for public)
Sources:
- [Vana Blog Mainnet Live, https://blog.vana.org/vana-mainnet-is-live/] (HIGH)
- [Vana Docs Bridge, https://docs.vana.org] (HIGH)
- [Vana Blog Token Launch, https://blog.vana.org/vana-token-launch/] (HIGH)

Integration Name: r/datadao (Reddit Data DAO)
Integrated With: Reddit (via Universal Connectors)
Purpose: Pengguna mengekspor data Reddit mereka ke Data DAO untuk dilikuidasikan; Proof-of-Contribution verification
Status: Live
Related Historical Event ID: EV-006 (r/datadao launch 2023)
Sources:
- [Vana Blog Data DAO Ecosystem, https://blog.vana.org/category/data-daos/] (HIGH)
- [Messari Vana Report, https://messari.io/report/vana] (MEDIUM)
- [Vana Docs Connectors, https://docs.vana.org] (HIGH)

Integration Name: Volara (Twitter/X Data DAO)
Integrated With: Twitter / X (via Universal Connectors)
Purpose: Pengguna mengekspor data Twitter/X ke Data DAO untuk monetisasi
Status: Live
Related Historical Event ID: EV-007 (Volara launch 2023)
Sources:
- [Vana Blog Data DAO Ecosystem, https://blog.vana.org/category/data-daos/] (HIGH)
- [Messari Vana Report, https://messari.io/report/vana] (MEDIUM)

Integration Name: Flirtual (Dating Data DAO)
Integrated With: Flirtual dating app (via Universal Connectors)
Purpose: Portabilitas dan likuiditas data preferensi pengguna dating
Status: Live
Related Historical Event ID: EV-008 (Flirtual launch 2023)
Sources:
- [Vana Blog Data DAO Ecosystem, https://blog.vana.org/category/data-daos/] (HIGH)
- [Messari Vana Report, https://messari.io/report/vana] (MEDIUM)

Integration Name: DataPig (DeFi Data DAO)
Integrated With: DeFi protocols on-chain data (via Universal Connectors / direct indexing)
Purpose: Mengumpulkan riwayat transaksi dan posisi on-chain untuk analisis
Status: Live
Related Historical Event ID: EV-009 (DataPig launch 2023)
Sources:
- [Vana Blog Data DAO Ecosystem, https://blog.vana.org/category/data-daos/] (HIGH)
- [Messari Vana Report, https://messari.io/report/vana] (MEDIUM)

Integration Name: Kappa (Gaming Data DAO)
Integrated With: Gaming platforms (via Universal Connectors)
Purpose: Pemain mengontrol dan memonetisasi data gameplay
Status: Live
Related Historical Event ID: EV-010 (Kappa launch 2023)
Sources:
- [Vana Blog Data DAO Ecosystem, https://blog.vana.org/category/data-daos/] (HIGH)
- [Messari Vana Report, https://messari.io/report/vana] (MEDIUM)

Integration Name: IBC Channels (Cosmos Ecosystem)
Integrated With: Cosmos ecosystem chains (Osmosis, Celestia, etc. — specific channels not publicly documented)
Purpose: Cross-chain asset transfer dan messaging via IBC
Status: Live (enabled; active channels not publicly documented)
Related Historical Event ID: EV-013 (Mainnet launch with IBC enabled)
Sources:
- [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH)
- [Cosmos IBC Docs, https://ibc.cosmos.network] (HIGH)
- [Vana Docs, https://docs.vana.org] (MEDIUM)

Integration Name: Vana Portal + Data DAOs
Integrated With: r/datadao; Volara; Flirtual; DataPig; Kappa
Purpose: Dashboard terpusat untuk kontribusi data, manajemen Data DAO, staking VANA, pelacakan reward
Status: Live
Related Historical Event ID: EV-015 (Vana Portal launch 2024)
Sources:
- [Vana Portal, https://portal.vana.org] (HIGH)
- [Vana Docs, https://docs.vana.org] (HIGH)
- [Vana Blog Data DAO Ecosystem, https://blog.vana.org/category/data-daos/] (HIGH)

Integration Name: Universal Connectors SDK + Web2 Platforms
Integrated With: Reddit; Twitter/X; Flirtual; DeFi protocols; Gaming platforms (per Data DAO)
Purpose: SDK untuk developer membangun konektor mengekspor data dari platform Web2 ke Data DAO via encrypted upload
Status: Live (used by existing Data DAOs)
Related Historical Event ID: EV-011 (Universal Connectors development 2023)
Sources:
- [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH)
- [Vana Docs Connectors, https://docs.vana.org] (HIGH)
- [Vana GitHub, https://github.com/vana-com] (HIGH)

## Infrastructure Providers

Provider: GitHub
Service: Source code hosting, CI/CD (GitHub Actions), issue tracking untuk semua repositori Vana
Criticality: High
Status: Live
Sources:
- [Vana GitHub, https://github.com/vana-com] (HIGH)
- [Vana Docs, https://docs.vana.org] (HIGH)

Provider: Docker Hub / Container Registry
Service: Container images untuk validator node software, explorer, portal deployment
Criticality: Medium
Status: Live
Sources:
- [Vana GitHub, https://github.com/vana-com] (HIGH)
- [Cosmos SDK Docs, https://docs.cosmos.network] (MEDIUM)

Provider: Cloud Providers (AWS / GCP / Azure / Bare Metal)
Service: Validator node hosting, RPC endpoints, explorer hosting, portal hosting (specific provider not disclosed)
Criticality: High
Status: Live
Sources:
- [Vana Docs Validator, https://docs.vana.org] (MEDIUM)
- [Cosmos SDK Docs, https://docs.cosmos.network] (MEDIUM)

Provider: Blockscout (or custom fork)
Service: Block explorer backend (Vana Explorer berbasis Blockscout/custom)
Criticality: Medium
Status: Live
Sources:
- [Vana Explorer, https://explorer.vana.org] (HIGH)
- [Vana Blog Mainnet Live, https://blog.vana.org/vana-mainnet-is-live/] (HIGH)

Provider: Vercel / Netlify / Similar
Service: Frontend hosting untuk Vana Portal (assumed; not explicitly confirmed)
Criticality: Medium
Status: Live
Sources:
- [Vana Portal, https://portal.vana.org] (MEDIUM)
- [Vana Docs, https://docs.vana.org] (MEDIUM)

Provider: Discord
Service: Komunitas developer, kontributor data, governance discussion
Criticality: Medium
Status: Live
Sources:
- [Vana.org, https://vana.org] (HIGH)
- [Discord Invite, https://discord.gg/vana] (HIGH)

Provider: Telegram
Service: Announcements channel dan komunitas global
Criticality: Low
Status: Live
Sources:
- [Vana.org, https://vana.org] (HIGH)
- [Telegram, https://t.me/vana_official] (HIGH)

Provider: X (Twitter)
Service: Real-time announcements, educational threads, community engagement
Criticality: Low
Status: Live
Sources:
- [X.com/vana, https://x.com/vana] (HIGH)
- [Vana.org, https://vana.org] (HIGH)

## Exchange Ecosystem

Exchange: Centralized Exchanges (CEX) — specific exchanges not publicly announced
Listing Status: Listed
Spot: Yes (since TGE 2024-12-16)
Perpetual: tidak diketahui
OTC: tidak diketahui
Launchpool: tidak diketahui
Status: Live
Sources:
- [Vana Blog Token Launch, https://blog.vana.org/vana-token-launch/] (HIGH)
- [CoinGecko VANA, https://www.coingecko.com/en/coins/vana] (HIGH)

Exchange: Decentralized Exchanges (DEX) on Vana L1 / Ethereum
Listing Status: Likely (VANA token tradable)
Spot: Yes (assumed)
Perpetual: tidak diketahui
OTC: tidak diketahui
Launchpool: tidak diketahui
Status: Live (assumed)
Sources:
- [Vana Blog Token Launch, https://blog.vana.org/vana-token-launch/] (MEDIUM)
- [Vana Explorer, https://explorer.vana.org] (MEDIUM)

## Wallet Ecosystem

Wallet: Keplr
Support Type: Cosmos SDK chain support (Vana Mainnet is Cosmos-based; Keplr support assumed but not explicitly confirmed)
Status: tidak diketahui (not explicitly documented in official sources)
Sources:
- [Vana Docs, https://docs.vana.org] (LOW)
- [Keplr Wallet, https://wallet.keplr.app] (LOW)

Wallet: MetaMask
Support Type: EVM RPC compatibility via Ethermint (Vana Mainnet exposes Ethereum JSON-RPC)
Status: Live (EVM compatible; users can add Vana Mainnet RPC to MetaMask)
Sources:
- [Vana Docs Developers, https://docs.vana.org] (HIGH)
- [Ethermint GitHub, https://github.com/evmos/ethermint] (HIGH)
- [Vana Blog Mainnet Live, https://blog.vana.org/vana-mainnet-is-live/] (HIGH)

Wallet: Cosmostation
Support Type: Cosmos ecosystem wallet (assumed compatible; not explicitly confirmed)
Status: tidak diketahui
Sources:
- [Cosmostation, https://cosmostation.io] (LOW)
- [Vana Docs, https://docs.vana.org] (LOW)

Wallet: Leap Wallet
Support Type: Cosmos ecosystem wallet (assumed compatible; not explicitly confirmed)
Status: tidak diketahui
Sources:
- [Leap Wallet, https://leapwallet.io] (LOW)
- [Vana Docs, https://docs.vana.org] (LOW)

Wallet: Rabby Wallet
Support Type: EVM multi-chain wallet (supports custom EVM RPC; Vana Mainnet compatible)
Status: Live (assumed via custom RPC)
Sources:
- [Rabby Wallet, https://rabby.io] (MEDIUM)
- [Vana Docs Developers, https://docs.vana.org] (MEDIUM)

## Developer Ecosystem

SDK: Universal Connectors SDK
Purpose: TypeScript/Python SDK untuk developer membangun data connectors mengekspor data dari platform Web2 ke Data DAO
Status: Live
Sources:
- [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH)
- [Vana Docs Connectors, https://docs.vana.org] (HIGH)
- [Vana GitHub, https://github.com/vana-com] (HIGH)

API: Vana Mainnet JSON-RPC (Ethereum compatible via Ethermint)
Purpose: Standard Ethereum JSON-RPC methods (eth_call, eth_sendRawTransaction, eth_getLogs, dll.) untuk dApp interaction
Status: Live
Sources:
- [Vana Docs Developers, https://docs.vana.org] (HIGH)
- [Ethermint GitHub, https://github.com/evmos/ethermint] (HIGH)
- [Vana Blog Mainnet Live, https://blog.vana.org/vana-mainnet-is-live/] (HIGH)

API: Vana Mainnet REST / gRPC (Cosmos SDK standard)
Purpose: Cosmos SDK module queries (staking, governance, bank, IBC, custom modules PoC/Bridge)
Status: Live
Sources:
- [Cosmos SDK Docs, https://docs.cosmos.network] (HIGH)
- [Vana Docs, https://docs.vana.org] (HIGH)
- [Vana GitHub, https://github.com/vana-com] (HIGH)

Developer Tools: Hardhat / Foundry
Purpose: Smart contract development, testing, deployment untuk Solidity contracts
Status: Live
Sources:
- [Vana GitHub, https://github.com/vana-com] (HIGH)
- [Vana Docs Developers, https://docs.vana.org] (HIGH)

Developer Tools: Ignite CLI
Purpose: Scaffold dan development tooling untuk Cosmos chains (module creation, chain initialization)
Status: Live (assumed used)
Sources:
- [Ignite CLI, https://ignite.com/cli] (MEDIUM)
- [Cosmos SDK Docs, https://docs.cosmos.network] (MEDIUM)

Developer Tools: GitHub Actions
Purpose: CI/CD pipeline untuk semua repositori
Status: Live
Sources:
- [Vana GitHub, https://github.com/vana-com] (HIGH)

Developer Portal: Vana Docs (https://docs.vana.org)
Purpose: Dokumentasi teknis resmi: arsitektur, API, smart contract, panduan developer, connectors SDK reference
Status: Live
Sources:
- [Vana Docs, https://docs.vana.org] (HIGH)

Open Source Repository: Vana GitHub (https://github.com/vana-com)
Purpose: Monorepo berisi protokol, smart contract, SDK, tooling, node software
Status: Live
Sources:
- [Vana GitHub, https://github.com/vana-com] (HIGH)

Hackathon: tidak diketahui (no public hackathon announcements found in official sources)
Status: tidak diketahui
Sources:
- [Vana Blog, https://blog.vana.org] (MEDIUM)
- [Vana GitHub, https://github.com/vana-com] (MEDIUM)

Grant Program: Vana Foundation Ecosystem Grants (referenced in whitepaper)
Purpose: Mendukung pengembangan Data DAO, connectors, tooling, risak
Status: Planned / Referenced (no public recipient list, amounts, or application process published)
Sources:
- [Vana Whitepaper, https://vana.org/whitepaper.pdf] (MEDIUM)
- [Vana Blog, https://blog.vana.org] (MEDIUM)

## Applications

Application: Vana Portal
Category: User Dashboard / Portfolio Management
Relationship: Official frontend untuk kontribusi data, manajemen Data DAO, staking VANA, reward tracking
Status: Live
Sources:
- [Vana Portal, https://portal.vana.org] (HIGH)
- [Vana Docs, https://docs.vana.org] (HIGH)
- [Vana Blog Mainnet Live, https://blog.vana.org/vana-mainnet-is-live/] (HIGH)

Application: r/datadao
Category: Data DAO (Social Media Data)
Relationship: Data DAO pertama dan terbesar; mengumpulkan data Reddit pengguna via Universal Connectors
Status: Live
Sources:
- [Vana Blog Data DAO Ecosystem, https://blog.vana.org/category/data-daos/] (HIGH)
- [Messari Vana Report, https://messari.io/report/vana] (MEDIUM)
- [Vana Explorer Contracts, https://explorer.vana.org] (HIGH)

Application: Volara
Category: Data DAO (Social Media Data)
Relationship: Data DAO untuk data Twitter/X; portabilitas data media sosial
Status: Live
Sources:
- [Vana Blog Data DAO Ecosystem, https://blog.vana.org/category/data-daos/] (HIGH)
- [Messari Vana Report, https://messari.io/report/vana] (MEDIUM)
- [Vana Explorer Contracts, https://explorer.vana.org] (HIGH)

Application: Flirtual
Category: Data DAO (Dating App Data)
Relationship: Data DAO untuk data aplikasi kencan; portabilitas preferensi pengguna
Status: Live
Sources:
- [Vana Blog Data DAO Ecosystem, https://blog.vana.org/category/data-daos/] (HIGH)
- [Messari Vana Report, https://messari.io/report/vana] (MEDIUM)
- [Vana Explorer Contracts, https://explorer.vana.org] (HIGH)

Application: DataPig
Category: Data DAO (DeFi Data)
Relationship: Data DAO fokus data DeFi; riwayat transaksi dan posisi on-chain
Status: Live
Sources:
- [Vana Blog Data DAO Ecosystem, https://blog.vana.org/category/data-daos/] (HIGH)
- [Messari Vana Report, https://messari.io/report/vana] (MEDIUM)
- [Vana Explorer Contracts, https://explorer.vana.org] (HIGH)

Application: Kappa
Category: Data DAO (Gaming Data)
Relationship: Data DAO untuk data gaming; monetisasi data gameplay
Status: Live
Sources:
- [Vana Blog Data DAO Ecosystem, https://blog.vana.org/category/data-daos/] (HIGH)
- [Messari Vana Report, https://messari.io/report/vana] (MEDIUM)
- [Vana Explorer Contracts, https://explorer.vana.org] (HIGH)

Application: Vana Explorer
Category: Block Explorer / Analytics
Relationship: Block explorer resmi Vana Mainnet (Blockscout-based/custom)
Status: Live
Sources:
- [Vana Explorer, https://explorer.vana.org] (HIGH)
- [Vana Blog Mainnet Live, https://blog.vana.org/vana-mainnet-is-live/] (HIGH)

Application: Universal Connectors (SDK/CLI tools)
Category: Developer Tools / Data Portability
Relationship: SDK untuk membangun konektor data Web2 → Data DAO
Status: Live
Sources:
- [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH)
- [Vana Docs Connectors, https://docs.vana.org] (HIGH)
- [Vana GitHub, https://github.com/vana-com] (HIGH)

## Governance Ecosystem

Foundation: Vana Foundation
Role: Entitas hukum resmi (Cayman Islands) mengawasi pengembangan protokol, ekosistem Data DAO, governance token VANA; mengelola treasury dan grant program
Status: Live
Sources:
- [Vana Foundation GitHub, https://github.com/vana-com] (HIGH)
- [Vana.org Team, https://vana.org/team] (HIGH)
- [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH)

DAO: r/datadao
Role: Data DAO pertama; governance atas data Reddit kolektif, reward distribution, treasury management
Status: Live
Sources:
- [Vana Blog Data DAO Ecosystem, https://blog.vana.org/category/data-daos/] (HIGH)
- [Messari Vana Report, https://messari.io/report/vana] (MEDIUM)

DAO: Volara
Role: Data DAO Twitter/X; governance atas data media sosial kolektif
Status: Live
Sources:
- [Vana Blog Data DAO Ecosystem, https://blog.vana.org/category/data-daos/] (HIGH)
- [Messari Vana Report, https://messari.io/report/vana] (MEDIUM)

DAO: Flirtual
Role: Data DAO dating app; governance atas data preferensi kencan
Status: Live
Sources:
- [Vana Blog Data DAO Ecosystem, https://blog.vana.org/category/data-daos/] (HIGH)
- [Messari Vana Report, https://messari.io/report/vana] (MEDIUM)

DAO: DataPig
Role: Data DAO DeFi; governance atas data transaksi on-chain
Status: Live
Sources:
- [Vana Blog Data DAO Ecosystem, https://blog.vana.org/category/data-daos/] (HIGH)
- [Messari Vana Report, https://messari.io/report/vana] (MEDIUM)

DAO: Kappa
Role: Data DAO gaming; governance atas data gameplay
Status: Live
Sources:
- [Vana Blog Data DAO Ecosystem, https://blog.vana.org/category/data-daos/] (HIGH)
- [Messari Vana Report, https://messari.io/report/vana] (MEDIUM)

Council: Validator Set (Active Validators)
Role: Consensus participation (CometBFT); block production; governance voting power berdasarkan stake; bridge attestation untuk Vana-Ethereum bridge
Status: Live
Sources:
- [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH)
- [Vana Explorer, https://explorer.vana.org] (HIGH)
- [CometBFT Docs, https://docs.cometbft.com] (HIGH)

Committee: On-Chain Governance (Cosmos SDK Governance Module)
Role: Parameter changes, software upgrades, treasury spending (community pool), text proposals; token-weighted voting (1 VANA = 1 vote via staked token)
Status: Live (since mainnet 2024-10-16)
Sources:
- [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH)
- [Vana Docs Governance, https://docs.vana.org/governance] (HIGH)
- [Cosmos SDK Governance, https://docs.cosmos.network/main/build/modules/gov] (HIGH)

Validator Group: Vana Validator Community
Role: Menjalankan validator nodes; network security; governance participation; bridge attestation
Status: Live
Sources:
- [Vana Docs Validator, https://docs.vana.org] (HIGH)
- [Vana Explorer, https://explorer.vana.org] (HIGH)
- [Vana GitHub Node Repo, https://github.com/vana-com] (HIGH)

## Ecosystem Risks

Risk: Single Bridge Dependency (Vana-Ethereum Bridge)
Description: Semua transfer VANA antara Ethereum dan Vana L1 bergantung pada single bridge contract set dengan validator set attestation model; bukan trust-minimized light-client bridge; bridge compromise = asset loss di kedua chain
Type: Bridge Dependency
Sources:
- [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH)
- [Vana Docs Bridge, https://docs.vana.org] (HIGH)

Risk: Cosmos SDK / CometBFT / Ethermint Upstream Dependency
Description: Core blockchain bergantung pada upstream maintenance dari Cosmos SDK, CometBFT, Ethermint (Evmos); breaking changes atau vulnerability upstream mempengaruhi Vana langsung
Type: SDK / Protocol Dependency
Sources:
- [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH)
- [Vana GitHub, https://github.com/vana-com] (HIGH)
- [Cosmos SDK Docs, https://docs.cosmos.network] (HIGH)
- [CometBFT Docs, https://docs.cometbft.com] (HIGH)
- [Ethermint GitHub, https://github.com/evmos/ethermint] (HIGH)

Risk: Cloud Provider Centralization (Validator Nodes)
Description: Validator nodes kemungkinan besar di-host di cloud provider terpusat (AWS/GCP/Azure); single provider outage bisa mempengaruhi validator set quorum
Type: Cloud Dependency
Sources:
- [Vana Docs Validator, https://docs.vana.org] (MEDIUM)
- [Cosmos SDK Docs, https://docs.cosmos.network] (MEDIUM)

Risk: Off-Chain Data Storage Dependency (IPFS/Arweave/Cloud per Data DAO)
Description: Data DAO raw data disimpan off-chain; protocol tidak menjamin persistence atau availability; Data DAO individu bertanggung jawab — jika storage provider gagal, data hilang
Type: Data Provider / Storage Dependency
Sources:
- [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH)
- [Universal Connectors Docs, https://docs.vana.org] (HIGH)

Risk: No Public Security Audits
Description: Tidak ada audit keamanan publik yang diumumkan untuk core modules, bridge contracts, Data DAO contracts, atau token contracts
Type: Security Dependency
Sources:
- [Vana GitHub, https://github.com/vana-com] (HIGH)
- [Vana Blog, https://blog.vana.org] (HIGH)
- [Vana Docs, https://docs.vana.org] (HIGH)

Risk: Foundation Treasury Centralization
Description: Vana Foundation (single legal entity Cayman Islands) mengelola treasury, pengembangan, grant; multi-sig signers dan threshold tidak dipublikasikan
Type: Centralization Risk
Sources:
- [Vana Foundation GitHub, https://github.com/vana-com] (MEDIUM)
- [Vana.org Team, https://vana.org/team] (MEDIUM)
- [Vana Whitepaper, https://vana.org/whitepaper.pdf] (MEDIUM)

Risk: Investor Token Unlock Concentration
Description: Early investors (Paradigm, Polymorphic, Coinbase Ventures, Polychain, Dragonfly) memegang token allocation besar dengan vesting schedule tidak dipublikasikan; unlock besar bisa mempengaruhi harga dan governance
Type: Centralization Risk / Token Distribution Risk
Sources:
- [Messari Vana Report, https://messari.io/report/vana] (MEDIUM)
- [Vana Whitepaper, https://vana.org/whitepaper.pdf] (MEDIUM)

Risk: IBC Relayer Infrastructure Dependency
Description: IBC channels memerlukan relayer infrastructure komunitas; tidak ada relayer resmi Vana Foundation; channel downtime jika relayer tidak beroperasi
Type: Infrastructure Dependency
Sources:
- [Cosmos IBC Docs, https://ibc.cosmos.network] (HIGH)
- [Vana Docs, https://docs.vana.org] (MEDIUM)

Risk: Data DAO Connector Verification Fragmentation
Description: Proof-of-Contribution verification quality bergantung pada connector implementation per Data DAO; tidak ada universal verification standard enforced at protocol level
Type: Protocol Dependency / Data Quality Risk
Sources:
- [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH)
- [Vana Docs PoC, https://docs.vana.org] (HIGH)

Risk: Regulatory Uncertainty for Data DAOs
Description: Status regulasi Data DAO di berbagai yurisdiksi tidak pasti; whitepaper mengakui ketidakpastian regulasi; bisa mempengaruhi operasi Data DAO dan token VANA
Type: Regulation Dependency
Sources:
- [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH)
- [Messari Vana Report, https://messari.io/report/vana] (MEDIUM)

## Official Ecosystem Resources

Official Documentation: https://docs.vana.org
Developer Portal: https://docs.vana.org/developers
GitHub: https://github.com/vana-com
Partner Documentation: https://docs.vana.org/partners (not explicitly confirmed; inferred from docs structure)
Grant Program: https://docs.vana.org/grants (referenced in whitepaper; no live page confirmed)
Ecosystem Dashboard: https://portal.vana.org (user dashboard); https://explorer.vana.org (on-chain analytics)
Official Blog: https://blog.vana.org
Whitepaper: https://vana.org/whitepaper.pdf
Discord: https://discord.gg/vana
Telegram: https://t.me/vana_official
X/Twitter: https://x.com/vana
Block Explorer: https://explorer.vana.org
User Portal: https://portal.vana.org

## Summary

Primary Ecosystem: Cosmos SDK ecosystem (CometBFT consensus, Ethermint EVM, IBC); Ethereum ecosystem (via bridge, ERC-20 VANA, EVM RPC compatibility)
Supported Chains: Vana Mainnet (native L1); Ethereum Mainnet (bridge); Cosmos ecosystem chains (IBC enabled, active channels not documented)
External Dependencies: 25+ dependencies teridentifikasi (Critical: Cosmos SDK, CometBFT, Ethermint, Vana-Ethereum Bridge, Vana Foundation; High: IBC, IPFS/Arweave, Investors, Cloud providers, GitHub, React/Next.js, TypeScript, Protobuf/gRPC, Hardhat/Foundry; Medium/Low: Kubernetes, Prometheus/Grafana, PostgreSQL, Redis, Python, Ignite CLI, CoinGecko, Messari, Discord, Telegram, X)
Major Integrations: 10 integrations teridentifikasi (Vana-Ethereum Bridge, 5 Data DAOs + Portal, IBC, Universal Connectors + Web2 platforms)
Infrastructure Providers: 8 providers (GitHub, Docker, Cloud providers, Blockscout, Vercel/Netlify, Discord, Telegram, X)
Developer Programs: SDK (Universal Connectors), APIs (JSON-RPC, REST/gRPC), Tools (Hardhat/Foundry, Ignite CLI, GitHub Actions), Portal (Vana Docs), Repo (GitHub), Grant Program (referenced, not live public)
Applications: 8 applications (Vana Portal, 5 Data DAOs, Vana Explorer, Universal Connectors SDK)

## Market Intelligence
_ref: `docs/Meta/Narratives.md`, `docs/Valuation/Competitors.md`, `docs/Meta/MarketCycles.md`_

PROJECT: Vana

## Market Category

Primary Category: Data Liquidity / Data DAO Infrastructure
Secondary Category: Layer 1 Blockchain (EVM-compatible, Cosmos SDK-based)
Sector: Web3 Infrastructure
Sub-sector: Data Ownership & Monetization / Data DAO Platform
Sources:
- [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH)
- [Messari Vana Report, https://messari.io/report/vana] (HIGH)
- [Vana Blog Data DAO Ecosystem, https://blog.vana.org/category/data-daos/] (HIGH)
- [CoinGecko VANA, https://www.coingecko.com/en/coins/vana] (HIGH)

## Market Position

Project Stage: Early (Post-TGE, Mainnet Live < 6 Months)
Primary Competitors:
- Ocean Protocol (Data Marketplace, ERC-20 OCEAN, Ethereum + Polygon) — broader data marketplace, not Data DAO-focused
- Streamr (Real-time Data Unions, ERC-20 DATA, Ethereum + Polygon + BSC) — streaming data focus, different architecture
- Ceramic Network (Decentralized Data Network, no native token, Ethereum + Polygon) — composable data layer, not L1
- Filecoin / Arweave (Decentralized Storage, FIL / AR tokens) — storage layer, not data liquidity/DAO infrastructure
- Sahara AI (AI Data Layer, upcoming token) — AI-focused data labeling/monetization, newer entrant
- Vana differentiates: Purpose-built L1 for Data DAOs with Proof-of-Contribution consensus at application layer, native VANA token for staking/governance/fees
Market Segment: Data Sovereignty & Monetization Infrastructure for End-Users (Consumer Data DAOs)
Geographic Focus: Global (Cayman Islands Foundation; distributed team US/Europe/Asia; Data DAOs target global user bases — Reddit, Twitter/X, Dating, DeFi, Gaming)
Sources:
- [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH)
- [Messari Vana Report, https://messari.io/report/vana] (HIGH)
- [Vana Blog Data DAO Ecosystem, https://blog.vana.org/category/data-daos/] (HIGH)
- [CoinGecko VANA, https://www.coingecko.com/en/coins/vana] (HIGH)
- [Ocean Protocol, https://oceanprotocol.com] (MEDIUM)
- [Streamr, https://streamr.network] (MEDIUM)
- [Ceramic Network, https://ceramic.network] (MEDIUM)
- [Filecoin, https://filecoin.io] (MEDIUM)
- [Arweave, https://arweave.org] (MEDIUM)
- [Sahara AI, https://sahara.ai] (MEDIUM)

## Trading Markets

Exchange: Centralized Exchanges (CEX) — Specific Exchanges Not Publicly Announced
Spot: Yes (since TGE 2024-12-16)
Perpetual: tidak diketahui
Futures: tidak diketahui
Options: tidak diketahui
OTC: tidak diketahui
Status: Live
Sources:
- [Vana Blog Token Launch, https://blog.vana.org/vana-token-launch/] (HIGH)
- [CoinGecko VANA, https://www.coingecko.com/en/coins/vana] (HIGH)

Exchange: Decentralized Exchanges (DEX) on Vana L1 / Ethereum
Spot: Yes (assumed — VANA tradable on Vana L1 DEXs and Ethereum DEXs via bridge)
Perpetual: tidak diketahui
Futures: tidak diketahui
Options: tidak diketahui
OTC: tidak diketahui
Status: Live (assumed)
Sources:
- [Vana Blog Token Launch, https://blog.vana.org/vana-token-launch/] (MEDIUM)
- [Vana Explorer, https://explorer.vana.org] (MEDIUM)
- [Vana Docs Bridge, https://docs.vana.org] (MEDIUM)

Exchange: CoinGecko (Price Tracking)
Spot: Price tracking only (not trading venue)
Perpetual: N/A
Futures: N/A
Options: N/A
OTC: N/A
Status: Live (since TGE 2024-12-16)
Sources:
- [CoinGecko VANA, https://www.coingecko.com/en/coins/vana] (HIGH)

Exchange: CoinMarketCap (Price Tracking)
Spot: Price tracking only (not trading venue)
Perpetual: N/A
Futures: N/A
Options: N/A
OTC: N/A
Status: Live (assumed — typical for new token launches)
Sources:
- [CoinMarketCap VANA, https://coinmarketcap.com/currencies/vana/] (MEDIUM) — verify independently

## Liquidity

Liquidity Source: CEX Order Books (specific exchanges not disclosed)
Major Liquidity Venue: tidak diketahui (no public disclosure of primary CEX venue or market makers)
DEX: Vana L1 native DEXs (specific DEX names not documented); Ethereum DEXs via VANA ERC-20 (Uniswap, etc. — specific pools not documented)
CEX: Listed on multiple CEXs per announcement; exchange names not public
Bridge Liquidity: Vana-Ethereum Bridge (two-way peg); liquidity depth not publicly documented
Status: Early (post-TGE, limited public liquidity data)
Sources:
- [Vana Blog Token Launch, https://blog.vana.org/vana-token-launch/] (HIGH)
- [CoinGecko VANA, https://www.coingecko.com/en/coins/vana] (HIGH)
- [Vana Explorer, https://explorer.vana.org] (MEDIUM)
- [Vana Docs Bridge, https://docs.vana.org] (MEDIUM)

## Adoption Metrics

Metric Name: Total Value Locked (TVL) — Protocol Level
Value: tidak diketahui (no public TVL dashboard; Vana L1 not indexed on DeFiLlama as of research cutoff)
Date: 2025-01 (research cutoff)
Sources:
- [DeFiLlama, https://defillama.com] (HIGH) — Vana not listed
- [Vana Explorer, https://explorer.vana.org] (MEDIUM) — raw on-chain data only

Metric Name: Total Value Locked (TVL) — Data DAO Level (Aggregate)
Value: tidak diketahui (individual Data DAO treasuries not aggregated publicly)
Date: 2025-01
Sources:
- [Vana Blog Data DAO Ecosystem, https://blog.vana.org/category/data-daos/] (MEDIUM)
- [Vana Explorer Contracts, https://explorer.vana.org] (MEDIUM)

Metric Name: Daily Active Users (Unique Addresses Interacting)
Value: tidak diketahui (no public analytics dashboard)
Date: 2025-01
Sources:
- [Vana Explorer, https://explorer.vana.org] (MEDIUM)
- [Vana Portal, https://portal.vana.org] (MEDIUM)

Metric Name: Daily Transactions (Vana Mainnet)
Value: tidak diketahui (no public aggregated metric; explorer shows per-block tx count)
Date: 2025-01
Sources:
- [Vana Explorer, https://explorer.vana.org] (MEDIUM)

Metric Name: Total Wallets / Unique Addresses (Vana Mainnet)
Value: tidak diketahui (no public metric)
Date: 2025-01
Sources:
- [Vana Explorer, https://explorer.vana.org] (MEDIUM)

Metric Name: Developer Count (Active Contributors)
Value: tidak diketahui (no public developer metrics; GitHub shows contributors but not "active developers" metric)
Date: 2025-01
Sources:
- [Vana GitHub, https://github.com/vana-com] (MEDIUM)
- [Electric Capital Developer Report, https://www.electriccapital.com/developer-report] (LOW) — Vana not in recent reports

Metric Name: Trading Volume (24h / 7d / 30d)
Value: tidak diketahui (CoinGecko shows volume but no historical aggregated data verified)
Date: 2025-01
Sources:
- [CoinGecko VANA, https://www.coingecko.com/en/coins/vana] (MEDIUM) — shows current volume only

Metric Name: Bridge Volume (Vana-Ethereum)
Value: tidak diketahui (no public bridge analytics dashboard)
Date: 2025-01
Sources:
- [Vana Explorer, https://explorer.vana.org] (MEDIUM)
- [Vana Docs Bridge, https://docs.vana.org] (MEDIUM)

Metric Name: Validator Count (Active Set)
Value: tidak diketahui (explorer shows active validators but no aggregated count published)
Date: 2025-01
Sources:
- [Vana Explorer, https://explorer.vana.org] (MEDIUM)
- [Vana Docs Validator, https://docs.vana.org] (MEDIUM)

Metric Name: Total Staked VANA
Value: tidak diketahui (no public staking dashboard)
Date: 2025-01
Sources:
- [Vana Explorer, https://explorer.vana.org] (MEDIUM)
- [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH) — staking live but metrics not public

Metric Name: Data DAO Count (Live on Mainnet)
Value: 5 (r/datadao, Volara, Flirtual, DataPig, Kappa)
Date: 2024-12 (per EV-006 through EV-010, EV-015)
Sources:
- [Vana Blog Data DAO Ecosystem, https://blog.vana.org/category/data-daos/] (HIGH)
- [Messari Vana Report, https://messari.io/report/vana] (HIGH)
- [Vana Explorer Contracts, https://explorer.vana.org] (HIGH)

Metric Name: Universal Connectors (Published Connectors)
Value: tidak diketahui (no public registry count)
Date: 2025-01
Sources:
- [Vana Docs Connectors, https://docs.vana.org] (MEDIUM)
- [Vana GitHub, https://github.com/vana-com] (MEDIUM)

## Market Share

Tidak tersedia. (No market share data for Data DAO Infrastructure category; category not tracked by standard market analytics platforms)
Sources:
- [DeFiLlama, https://defillama.com] (HIGH)
- [Token Terminal, https://tokenterminal.com] (HIGH)
- [Messari, https://messari.io] (HIGH)
- [CoinGecko Categories, https://www.coingecko.com/en/categories] (HIGH) — no "Data DAO" category

## Competitor Landscape

Competitor: Ocean Protocol
Category: Data Marketplace (General Purpose)
Difference: Ocean = decentralized data marketplace with compute-to-data; Vana = purpose-built L1 for user-owned Data DAOs with Proof-of-Contribution; Ocean multi-chain (Ethereum, Polygon), Vana sovereign L1 + Ethereum bridge
Market Segment: Data Economy Infrastructure
Sources:
- [Ocean Protocol, https://oceanprotocol.com] (HIGH)
- [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH)
- [Messari Vana Report, https://messari.io/report/vana] (MEDIUM)

Competitor: Streamr
Category: Real-time Data Unions / Streaming Data Marketplace
Difference: Streamr = pub/sub real-time data streams, Data Unions for monetization; Vana = batch/historical user data export via Data DAOs, L1 with native token; Streamr token DATA on Ethereum/Polygon/BSC
Market Segment: Data Monetization
Sources:
- [Streamr, https://streamr.network] (HIGH)
- [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH)

Competitor: Ceramic Network
Category: Decentralized Data Network (Composable Data Layer)
Difference: Ceramic = open data network for composable data streams (Ceramic streams, ComposeDB), no native token, not an L1; Vana = L1 with native token, Data DAO framework, Proof-of-Contribution
Market Segment: Decentralized Data Infrastructure
Sources:
- [Ceramic Network, https://ceramic.network] (HIGH)
- [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH)

Competitor: Filecoin
Category: Decentralized Storage
Difference: Filecoin = storage layer (proof-of-spacetime), FIL token for storage deals; Vana = data liquidity layer (data ownership + monetization), not a storage protocol — Data DAOs choose own storage (IPFS, Arweave, cloud)
Market Segment: Web3 Data Stack (Storage vs Liquidity)
Sources:
- [Filecoin, https://filecoin.io] (HIGH)
- [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH)

Competitor: Arweave
Category: Permanent Decentralized Storage
Difference: Arweave = permanent storage (blockweave), AR token; Vana = data liquidity/DAO infrastructure, not storage
Market Segment: Web3 Data Stack
Sources:
- [Arweave, https://arweave.org] (HIGH)
- [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH)

Competitor: Sahara AI
Category: AI Data Layer (Data Labeling / Monetization for AI)
Difference: Sahara = AI-focused data collection/labeling marketplace, upcoming token; Vana = general consumer Data DAOs (social, dating, DeFi, gaming), live L1 + token
Market Segment: AI Data / Data Monetization
Sources:
- [Sahara AI, https://sahara.ai] (MEDIUM)
- [Vana Blog Data DAO Ecosystem, https://blog.vana.org/category/data-daos/] (HIGH)

Competitor: Masa (Masa Finance)
Category: Data Network for AI / Personal Data Monetization
Difference: Masa = zk-data network for AI training data, personal data vaults; Vana = Data DAO collectives for platform data export (Reddit, Twitter, etc.)
Market Segment: Data Monetization / AI Data
Sources:
- [Masa Finance, https://masa.finance] (MEDIUM)
- [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH)

Competitor: DIMO
Category: Vehicle / IoT Data Network (DePIN)
Difference: DIMO = vehicle data (DePIN), user-owned vehicle data marketplace; Vana = broader consumer platform data (social, dating, DeFi, gaming)
Market Segment: DePIN / Data Monetization
Sources:
- [DIMO, https://dimo.zone] (MEDIUM)
- [Vana Blog Data DAO Ecosystem, https://blog.vana.org/category/data-daos/] (HIGH)

## Narrative Position

Narrative: Data DAO / Data Liquidity
Status: Main Narrative
Evidence: Vana Whitepaper centers "Data Liquidity Layer" and "Data DAOs" as core primitive; all 5 live Data DAOs (r/datadao, Volara, Flirtual, DataPig, Kappa) operationalize this narrative; Messari report titles Vana as "Data Liquidity Layer"
Sources:
- [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH)
- [Messari Vana Report, https://messari.io/report/vana] (HIGH)
- [Vana Blog Data DAO Ecosystem, https://blog.vana.org/category/data-daos/] (HIGH)

Narrative: Data Sovereignty / User-Owned Data
Status: Main Narrative
Evidence: "Users own their data" messaging across Vana.org, Portal, blog; Universal Connectors enable user-initiated data export; Proof-of-Contribution rewards users for data contributions
Sources:
- [Vana.org, https://vana.org] (HIGH)
- [Vana Portal, https://portal.vana.org] (HIGH)
- [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH)

Narrative: AI Training Data / Data for AI
Status: Secondary Narrative
Evidence: Whitepaper and blog mention AI use cases for Data DAO data (training, fine-tuning); r/datadao Reddit data valuable for LLM training; not the primary marketing focus vs. general data liquidity
Sources:
- [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH)
- [Vana Blog Data DAO Ecosystem, https://blog.vana.org/category/data-daos/] (MEDIUM)
- [Messari Vana Report, https://messari.io/report/vana] (MEDIUM)

Narrative: Modular Blockchain / Cosmos SDK App-Chain
Status: Secondary Narrative
Evidence: Built on Cosmos SDK + CometBFT + Ethermint; IBC enabled; sovereign L1 for specific use case (Data DAOs) — fits app-chain thesis
Sources:
- [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH)
- [Vana Docs Architecture, https://docs.vana.org] (HIGH)
- [Cosmos SDK App-Chain Thesis, https://blog.cosmos.network/app-chains] (MEDIUM)

Narrative: EVM-Compatible L1
Status: Secondary Narrative
Evidence: Ethermint provides EVM compatibility; Solidity smart contracts for Data DAOs; MetaMask/ETH tooling works; marketed as "EVM-compatible L1 for data"
Sources:
- [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH)
- [Vana Docs Developers, https://docs.vana.org] (HIGH)
- [Ethermint GitHub, https://github.com/evmos/ethermint] (HIGH)

Narrative: DePIN (Decentralized Physical Infrastructure Networks)
Status: Not Applicable
Evidence: Vana does not position as DePIN; no hardware/physical infrastructure component; Data DAOs are software-mediated data collectives
Sources:
- [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH)
- [Messari Vana Report, https://messari.io/report/vana] (HIGH)

Narrative: RWA (Real World Assets)
Status: Not Applicable
Evidence: No tokenization of real-world assets; Data DAOs tokenize user data contributions (digital assets), not RWAs
Sources:
- [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH)

Narrative: Restaking / EigenLayer
Status: Not Applicable
Evidence: Vana is sovereign L1 with own validator set (CometBFT PoS); not built on Ethereum restaking; no EigenLayer integration announced
Sources:
- [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH)
- [Vana Blog Mainnet Live, https://blog.vana.org/vana-mainnet-is-live/] (HIGH)

Narrative: Intent-Centric / Chain Abstraction
Status: Not Applicable
Evidence: No intent-based architecture or chain abstraction messaging; user interacts directly with Vana Portal and Data DAOs
Sources:
- [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH)
- [Vana Portal, https://portal.vana.org] (HIGH)

Narrative: L2 / Rollup
Status: Not Applicable
Evidence: Vana is sovereign L1 (Cosmos SDK), not an L2 or rollup on Ethereum; has bridge to Ethereum but settles on own chain
Sources:
- [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH)
- [Vana Docs Architecture, https://docs.vana.org] (HIGH)

Narrative: Interoperability / Cross-Chain
Status: Secondary Narrative
Evidence: IBC enabled for Cosmos ecosystem; Vana-Ethereum bridge for VANA token; not the primary narrative but technical capability
Sources:
- [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH)
- [Vana Docs Bridge, https://docs.vana.org] (HIGH)
- [Cosmos IBC Docs, https://ibc.cosmos.network] (HIGH)

## Market Timeline

Date: 2021
Milestone: Project Founding
Description: Anna Kazlauskas dan Art Abal mendirikan Vana dengan visi data liquidity layer
Related Historical Event ID: EV-001
Sources:
- [Vana.org Team, https://vana.org/team] (HIGH)
- [Forbes Profile Anna Kazlauskas, https://www.forbes.com/profile/anna-kazlauskas] (HIGH)

Date: 2023
Milestone: Vana Foundation Established (Cayman Islands)
Description: Entitas hukum resmi untuk mengelola protokol dan ekosistem
Related Historical Event ID: EV-002
Sources:
- [Vana Foundation GitHub, https://github.com/vana-com] (HIGH)
- [Vana.org Team, https://vana.org/team] (HIGH)

Date: 2023
Milestone: Whitepaper Published
Description: Spesifikasi teknis L1, Proof-of-Contribution, Data DAO architecture
Related Historical Event ID: EV-003
Sources:
- [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH)
- [Vana Docs, https://docs.vana.org] (HIGH)

Date: 2023-07
Milestone: Moksha Testnet Launch
Description: Public testnet untuk validator, Data DAO, PoC testing
Related Historical Event ID: EV-004
Sources:
- [Vana Blog Introducing Moksha, https://blog.vana.org/introducing-moksha-testnet/] (HIGH)
- [Vana Docs, https://docs.vana.org] (HIGH)

Date: 2023
Milestone: Early Funding Round (Paradigm, Polymorphic, Coinbase Ventures, Polychain, Dragonfly)
Description: Strategic funding untuk pengembangan L1 dan ekosistem
Related Historical Event ID: EV-005
Sources:
- [Messari Vana Report, https://messari.io/report/vana] (MEDIUM)
- [Vana Blog, https://blog.vana.org] (MEDIUM)

Date: 2023
Milestone: First 5 Data DAOs Launched on Testnet
Description: r/datadao, Volara, Flirtual, DataPig, Kappa deployed on Moksha
Related Historical Event ID: EV-006, EV-007, EV-008, EV-009, EV-010
Sources:
- [Vana Blog Data DAO Ecosystem, https://blog.vana.org/category/data-daos/] (HIGH)
- [Messari Vana Report, https://messari.io/report/vana] (HIGH)

Date: 2024-10-16
Milestone: Vana Mainnet Genesis Launch
Description: Mainnet live, validator set active, native VANA minted, Data DAO contracts deployed, bridge live, IBC enabled
Related Historical Event ID: EV-013
Sources:
- [Vana Blog Mainnet Live, https://blog.vana.org/vana-mainnet-is-live/] (HIGH)
- [Vana Explorer, https://explorer.vana.org] (HIGH)

Date: 2024-10-16
Milestone: Vana Block Explorer Live
Description: Official explorer (Blockscout-based) online
Related Historical Event ID: EV-014
Sources:
- [Vana Explorer, https://explorer.vana.org] (HIGH)
- [Vana Blog Mainnet Live, https://blog.vana.org/vana-mainnet-is-live/] (HIGH)

Date: 2024
Milestone: Vana Portal Launch
Description: User dashboard untuk data contribution, Data DAO management, staking, rewards
Related Historical Event ID: EV-015
Sources:
- [Vana Portal, https://portal.vana.org] (HIGH)
- [Vana Docs, https://docs.vana.org] (HIGH)

Date: 2024-12-16
Milestone: VANA Token Generation Event (TGE) & Public Launch
Description: VANA ERC-20 on Ethereum, claim via Portal, bridge activated, CEX listings begin
Related Historical Event ID: EV-016
Sources:
- [Vana Blog Token Launch, https://blog.vana.org/vana-token-launch/] (HIGH)
- [CoinGecko VANA, https://www.coingecko.com/en/coins/vana] (HIGH)
- [Vana Portal, https://portal.vana.org] (HIGH)

Date: 2024-12
Milestone: VANA Listed on Centralized Exchanges
Description: Trading live on multiple CEXs (names not disclosed)
Related Historical Event ID: EV-017
Sources:
- [Vana Blog Token Launch, https://blog.vana.org/vana-token-launch/] (HIGH)
- [CoinGecko VANA, https://www.coingecko.com/en/coins/vana] (HIGH)

Date: 2024
Milestone: Messari Vana Report Published
Description: Independent deep-dive research report on tokenomics, architecture, ecosystem
Related Historical Event ID: EV-018
Sources:
- [Messari Vana Report, https://messari.io/report/vana] (HIGH)
- [Vana Blog, https://blog.vana.org] (MEDIUM)

Date: 2024
Milestone: Anna Kazlauskas — Forbes 30 Under 30 2024
Description: Industry recognition for co-founder/CEO
Related Historical Event ID: EV-019
Sources:
- [Forbes Profile Anna Kazlauskas, https://www.forbes.com/profile/anna-kazlauskas] (HIGH)
- [Vana.org Team, https://vana.org/team] (HIGH)

## Official Market Resources

Official Dashboard: tidak tersedia (no dedicated market/analytics dashboard)
DefiLlama: tidak terdaftar (https://defillama.com — Vana not indexed as of research cutoff)
CoinGecko: https://www.coingecko.com/en/coins/vana
CoinMarketCap: https://coinmarketcap.com/currencies/vana/ (verify independently)
Token Terminal: tidak terdaftar (https://tokenterminal.com — Vana not listed as of research cutoff)
Messari: https://messari.io/report/vana
Explorer: https://explorer.vana.org
Official Blog: https://blog.vana.org
Official Documentation: https://docs.vana.org
Whitepaper: https://vana.org/whitepaper.pdf
GitHub: https://github.com/vana-com
User Portal: https://portal.vana.org
Discord: https://discord.gg/vana
Telegram: https://t.me/vana_official
X/Twitter: https://x.com/vana

## Summary

Market Stage: Early (Post-TGE, Mainnet Live < 6 Months, Limited Public Metrics)
Primary Category: Data Liquidity / Data DAO Infrastructure
Competitor Count: 8+ identified (Ocean, Streamr, Ceramic, Filecoin, Arweave, Sahara AI, Masa, DIMO)
Major Narrative: Data DAO / Data Liquidity (Main); Data Sovereignty (Main); AI Training Data (Secondary); Modular App-Chain (Secondary); EVM-Compatible L1 (Secondary)
Trading Availability: CEX (multiple, names undisclosed), DEX (Vana L1 + Ethereum via bridge), Price Tracking (CoinGecko, CoinMarketCap)
Adoption Metrics Available: Minimal — only Data DAO count (5) verified; TVL, users, transactions, volume, staking metrics not publicly aggregated

## Behavioral Intelligence
_ref: `docs/Ontology/Hidden.md` — enriches DecisionEvent Alternatives/Reason/Reactions_

PROJECT: Vana

Strategic Objectives

1. Membangun Layer 1 sovereign untuk Data Liquidity dan Data DAO
· Evidence: Vana Whitepaper mendefinisikan arsitektur L1 berbasis Cosmos SDK dengan Proof-of-Contribution dan Data DAO sebagai primitive inti [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH)
· Supporting Dataset: Phase 1 Foundation, Phase 4 Technology Architecture

2. Mengembalikan kedaulatan data ke pengguna melalui Data DAO kolektif
· Evidence: Vana.org, Vana Portal, dan Universal Connectors SDK dirancang untuk user-initiated data export dari platform Web2 (Reddit, Twitter/X, dll.) ke Data DAO [Vana.org, https://vana.org] (HIGH) [Vana Portal, https://portal.vana.org] (HIGH) [Vana Docs Connectors, https://docs.vana.org] (HIGH)
· Supporting Dataset: Phase 1 Foundation, Phase 7 Applications, Phase 8 Narrative Position

3. Membuat token VANA sebagai utility multi-fungsi: governance, staking, fee payment, incentive, reward
· Evidence: Tokenomics di whitepaper dan Phase 6 Token Utility mencatat 8 utilitas aktif (governance, staking, validator, fee payment, incentive, reward, liquidity, security) [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH) [Vana Docs Governance, https://docs.vana.org/governance] (HIGH)
· Supporting Dataset: Phase 6 Token Utility, Phase 4 Consensus Mechanism

4. Menarik ekosistem Data DAO vertikal (social, dating, DeFi, gaming) sebagai proof-of-concept skala besar
· Evidence: 5 Data DAO live pada mainnet: r/datadao (Reddit), Volara (Twitter/X), Flirtual (dating), DataPig (DeFi), Kappa (gaming) — diluncurkan bertahap 2023 testnet, migrasi mainnet 2024-10 [Vana Blog Data DAO Ecosystem, https://blog.vana.org/category/data-daos/] (HIGH)
· Supporting Dataset: Phase 3 Events EV-006 through EV-010, EV-015, Phase 7 Major Integrations

5. Mengamankan funding strategis dari investor tier-1 untuk pengembangan protokol jangka panjang
· Evidence: Early 2023 round dari Paradigm, Polymorphic Capital, Coinbase Ventures, Polychain Capital, Dragonfly Capital [Messari Vana Report, https://messari.io/report/vana] (MEDIUM)
· Supporting Dataset: Phase 2 Entities Investors, Phase 5 Funding History, Phase 3 EV-005

Decision Timeline

Keputusan: Mendirikan Vana Foundation di Cayman Islands sebagai entitas hukum (2023)
· Trigger: Perlu legal wrapper untuk token issuance, treasury management, dan compliance sebelum public launch
· Evidence: Vana Foundation GitHub dan team page menyebutkan fondasi Cayman Islands [Vana Foundation GitHub, https://github.com/vana-com] (HIGH) [Vana.org Team, https://vana.org/team] (HIGH)
· Decision: Membentuk yayasan nirlaba (foundation) di Cayman Islands sebagai entitas resmi mengelola protokol, ekosistem Data DAO, dan governance token VANA
· Immediate Result: Entitas hukum tersedia untuk fundraising, token legal opinion, dan treaty compliance
· Long-term Impact: Menjadi central point untuk treasury, grants, governance oversight; menciptakan centralization risk (single legal entity)
· Supporting Dataset: Phase 2 Entity Vana Foundation, Phase 3 EV-002, Phase 7 Governance Ecosystem

Keputusan: Memilih arsitektur Cosmos SDK + CometBFT + Ethermint untuk Vana L1 (2023, sebelum testnet)
· Trigger: Butuh sovereign chain dengan EVM compatibility, modular architecture, IBC native, dan custom modules (PoC, Bridge)
· Evidence: Whitepaper arsitektur: Cosmos SDK application layer, CometBFT consensus, Ethermint EVM module [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH) [Vana Docs Architecture, https://docs.vana.org] (HIGH)
· Decision: Build sovereign L1 berbasis Cosmos SDK bukan deploy sebagai L2/rollup di Ethereum atau gunakan subnet existing chain
· Immediate Result: Full control atas consensus, execution, governance parameters; custom PoC module deployment; IBC enabled
· Long-term Impact: Higher validator operational burden vs L2; own security budget (VANA staking); bridge dependency untuk Ethereum liquidity; app-chain thesis alignment
· Supporting Dataset: Phase 4 System Architecture, Phase 4 Core Components, Phase 8 Narrative Position

Keputusan: Meluncurkan Moksha Testnet publik Juli 2023 sebelum mainnet
· Trigger: Perlu testing validator set, Data DAO onboarding, PoC mechanism, bridge mechanics di environment live
· Evidence: Blog "Introducing Moksha Testnet" 2023-07 [Vana Blog Introducing Moksha, https://blog.vana.org/introducing-moksha-testnet/] (HIGH)
· Decision: Public testnet dengan validator incentives, Data DAO deployment, community testing ~15 bulan sebelum mainnet
· Immediate Result: 5 Data DAO deploy di testnet (r/datadao, Volara, Flirtual, DataPig, Kappa); validator set terbentuk; PoC mechanism diuji
· Long-term Impact: Smooth mainnet launch 2024-10-16 dengan Data DAO contracts ready; testnet state migration status tidak terdokumentasi (open thread)
· Supporting Dataset: Phase 3 EV-004, EV-006 through EV-010, Phase 4 Technical Upgrade History

Keputusan: Meluncurkan Vana Mainnet 2024-10-16 tanpa VANA token transferable (TGE terpisah 2024-12-16)
· Trigger: Mainnet butuh native gas token dan staking token untuk validator; TGE memerlukan compliance, exchange coordination, claim infrastructure
· Evidence: Mainnet live 2024-10-16 dengan native VANA minted pada genesis; TGE 2024-12-16 terpisah [Vana Blog Mainnet Live, https://blog.vana.org/vana-mainnet-is-live/] (HIGH) [Vana Blog Token Launch, https://blog.vana.org/vana-token-launch/] (HIGH)
· Decision: Decouple mainnet genesis (chain live, staking active) dari TGE (token transferable, trading live) ~2 bulan gap
· Immediate Result: Validator set earning rewards dari hari 1; Data DAO operating; bridge contracts deployed; TGE claim via Portal
· Long-term Impact: Early stakers/validators accumulate VANA sebelum public float; potential insider advantage; regulatory separation chain launch vs token sale
· Supporting Dataset: Phase 3 EV-013, EV-016, Phase 6 Major Token Events

Keputusan: TGE VANA 2024-12-16 via claim portal (Vana Portal) bukan public sale/launchpad
· Trigger: Distribusi ke community, Data DAO participants, testnet users tanpa intermediary; regulatory caution pada public sale
· Evidence: Blog Token Launch: "claim via Portal"; CEX listings dimulai pasca-TGE [Vana Blog Token Launch, https://blog.vana.org/vana-token-launch/] (HIGH) [Vana Portal, https://portal.vana.org] (HIGH)
· Decision: Token Generation Event dengan community allocation claimable via Portal; tidak ada fixed-price public sale, launchpad, atau auction
· Immediate Result: Token tersebar ke Data DAO contributors, early users; CEX liquidity provided by market makers (tidak diungkap)
· Long-term Impact: Price discovery sepenuhnya market-driven post-TGE; no lock-up untuk claim recipients (vesting schedule tidak diungkap); fair launch narrative
· Supporting Dataset: Phase 3 EV-016, EV-017, Phase 6 TGE, Phase 6 Vesting Schedule

Keputusan: Membangun Vana-Ethereum Bridge dengan validator set attestation (bukan light-client/trust-minimized)
· Trigger: Perlu two-way peg VANA ERC-20 ↔ native VANA untuk liquidity dan user onboarding dari Ethereum ecosystem
· Evidence: Whitepaper bridge design; blog mainnet menyebutkan bridge live [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH) [Vana Docs Bridge, https://docs.vana.org] (HIGH)
· Decision: Validator-set multi-sig/threshold signature bridge model; Vana validators attest mint/burn pada Ethereum contract
· Immediate Result: Bridge live sejak mainnet 2024-10-16; VANA transferable cross-chain
· Long-term Impact: Bridge trust assumption = honest majority Vana validators; single point of failure untuk asset bridge; bukan trust-minimized seperti IBC light client
· Supporting Dataset: Phase 4 Core Components Bridge, Phase 7 Major Integrations, Phase 7 Ecosystem Risks

Keputusan: Tidak mengumumkan audit keamanan publik untuk core modules, bridge, atau Data DAO contracts (per cutoff penelitian)
· Trigger: Mainnet live dengan value at risk; best practice industri memerlukan audit sebelum mainnet
· Evidence: GitHub, Blog, Docs tidak memiliki audit announcements [Vana GitHub, https://github.com/vana-com] (HIGH) [Vana Blog, https://blog.vana.org] (HIGH) [Vana Docs, https://docs.vana.org] (HIGH)
· Decision: Launch tanpa public audit report; kemungkinan private audit dilakukan tapi tidak diumumkan
· Immediate Result: Security researchers/community tidak bisa verify code safety; insurance protocols unlikely to cover
· Long-term Impact: Trust deficit untuk institutional adoption; exploit risk tinggi; audit announcement menjadi prerequisite untuk next phase growth
· Supporting Dataset: Phase 4 Audit History, Phase 7 Ecosystem Risks, Phase 8 Market Summary

Evolution Pattern

Strategi: Dari konsep "data liquidity layer" (2021 whitepaper) → testnet dengan 5 Data DAO vertikal (2023) → mainnet sovereign L1 dengan native token (2024-10) → TGE dan public trading (2024-12) → ekosistem expansion phase (2025+)
· Evidence: Timeline Phase 3 events EV-001 melalui EV-019 menunjukkan evolusi bertahap: founding → foundation → whitepaper → testnet + Data DAO → funding → mainnet → portal → TGE → CEX listings → research coverage [Phase 3 History] (HIGH)

Teknologi: Dari design di whitepaper (2023) → implementasi Moksha testnet (Cosmos SDK + Ethermint + PoC module) → mainnet production hardening → bridge activation → IBC enablement → upgrade path via on-chain governance
· Evidence: Phase 4 Technical Upgrade History: 4 major upgrades (Moksha 2023-07, Mainnet Genesis 2024-10-16, Data DAO Deployments 2024-10 to 2024-12, TGE 2024-12-16) [Phase 4 Technical Upgrade History] (HIGH)

Tokenomics: Dari native gas/staking token pada mainnet genesis (2024-10) → ERC-20 deployment + TGE distribution (2024-12) → bridge activation → CEX listings → governance activation dengan token holder base diperluas
· Evidence: Phase 6 Major Token Events: Mainnet genesis native VANA → TGE ERC-20 → CEX listings; supply/distribution/vesting tetap undisclosed [Phase 6 Token] (HIGH)

Ekosistem: Dari 0 Data DAO → 5 Data DAO vertikal pada testnet (2023) → mainnet deployment yang sama 5 DAO (2024) → Universal Connectors SDK maturation → Vana Portal sebagai unified frontend → grant program referenced tapi belum live
· Evidence: Phase 7 Applications: 5 Data DAO live; Phase 7 Developer Ecosystem: grant program planned; Phase 3 EV-006 through EV-010, EV-011, EV-015 [Phase 7 Ecosystem] (HIGH)

Governance: Dari foundation-controlled (pre-mainnet) → on-chain governance module live di mainnet (2024-10) dengan VANA staked voting → TGE memperluas voter base (2024-12) → community pool / treasury governance parameter belum dipublikasikan
· Evidence: Phase 4 Consensus Mechanism: governance module active since mainnet; Phase 6 Governance: Cosmos SDK governance, token-weighted voting, delegation supported [Phase 4 Consensus, Phase 6 Governance] (HIGH)

Financial: Dari founder-funded (2021-2023) → strategic VC round 2023 (undisclosed amount, 5 tier-1 investors) → Foundation treasury management → TGE token allocation untuk treasury/ecosystem → protocol revenue planned (fees, bridge) tapi belum live → Data DAO revenue live at DAO level
· Evidence: Phase 5 Funding History, Treasury, Revenue Model; Phase 3 EV-005, EV-016 [Phase 5 Financial] (MEDIUM-HIGH)

Technical Decision Pattern

Pola 1: Modular App-Chain Architecture menggunakan Cosmos SDK Stack
· Decision Pattern: Memilih sovereign L1 dengan modular separation (CometBFT consensus, Ethermint EVM execution, custom application modules) daripada deploy sebagai L2/rollup atau gunakan existing chain
· Evidence: Whitepaper arsitektur: "Layer 1 blockchain berbasis Cosmos SDK dengan kompatibilitas EVM"; CometBFT untuk consensus, Ethermint untuk EVM, custom modules PoC/Bridge/IBC [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH) [Vana Docs Architecture, https://docs.vana.org] (HIGH)
· Supporting Dataset: Phase 4 System Architecture, Phase 4 Core Components, Phase 8 Narrative Position

Pola 2: EVM Compatibility via Ethermint sebagai Execution Layer
· Decision Pattern: Menggunakan Ethermint (Evmos) sebagai EVM module di atas Cosmos SDK daripada build custom EVM atau gunakan WASM/CosmWasm
· Evidence: "Primary: EVM via Ethermint module pada Cosmos SDK"; "RPC Compatibility: Standard Ethereum JSON-RPC"; "Smart Contract Language: Solidity (primary)" [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH) [Ethermint GitHub, https://github.com/evmos/ethermint] (HIGH)
· Supporting Dataset: Phase 4 Execution Environment, Phase 4 Programming Languages, Phase 8 Narrative Position

Pola 3: Proof-of-Contribution sebagai Application-Layer Module (bukan Consensus)
· Decision Pattern: PoC diimplementasikan sebagai Cosmos SDK custom module untuk data quality valuation dan reward distribution, bukan sebagai consensus mechanism untuk block production
· Evidence: "PoC BUKAN consensus mechanism untuk block production; PoC adalah application-layer mechanism untuk data quality valuation dan reward distribution di Data DAO" [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH) [Vana Docs PoC, https://docs.vana.org] (HIGH)
· Supporting Dataset: Phase 4 Consensus Mechanism, Phase 4 Core Components PoC Module

Pola 4: Validator-Set Attestation Bridge Model untuk Ethereum Connectivity
· Decision Pattern: Vana-Ethereum bridge menggunakan validator set Vana untuk attestation mint/burn, bukan light-client verification atau third-party oracle
· Evidence: "Bridge Security: Validator-set attestation model untuk Vana-Ethereum bridge"; "two-way peg VANA token antara Ethereum mainnet (ERC-20) dan Vana L1 (native); menggunakan validator set Vana untuk attestation" [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH) [Vana Docs Bridge, https://docs.vana.org] (HIGH)
· Supporting Dataset: Phase 4 Core Components Bridge, Phase 7 External Dependencies, Phase 7 Ecosystem Risks

Pola 5: Off-Chain Data Storage Delegation ke Data DAO Individual
· Decision Pattern: Protocol tidak menyediakan data availability layer; raw data storage (IPFS, Arweave, cloud) menjadi tanggung jawab masing-masing Data DAO
· Evidence: "Off-chain data storage untuk Data DAO raw data (IPFS, Arweave, atau centralized cloud per Data DAO design)"; "protocol tidak menjamin persistence atau availability; tanggung jawab per Data DAO" [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH) [Universal Connectors Docs, https://docs.vana.org] (HIGH)
· Supporting Dataset: Phase 4 System Architecture Storage, Phase 4 Known Technical Limitations, Phase 7 Ecosystem Risks

Pola 6: Testnet Extensif (15 bulan) Sebelum Mainnet dengan Data DAO Live
· Decision Pattern: Moksha testnet Juli 2023 → Mainnet Oktober 2024 (~15 bulan) dengan 5 Data DAO sudah operating di testnet sebelum mainnet
· Evidence: "Peluncuran Moksha Testnet 2023-07"; "5 Data DAO deployed di testnet"; Mainnet 2024-10-16 dengan Data DAO contracts deployed [Vana Blog Introducing Moksha, https://blog.vana.org/introducing-moksha-testnet/] (HIGH) [Vana Blog Mainnet Live, https://blog.vana.org/vana-mainnet-is-live/] (HIGH)
· Supporting Dataset: Phase 3 EV-004, EV-006 through EV-010, EV-013, Phase 4 Technical Upgrade History

Pola 7: Tidak Ada Public Security Audit Announcement Sebelum Mainnet
· Decision Pattern: Launch mainnet dan TGE tanpa mempublikasikan audit report dari auditor ternama (Trail of Bits, CertiK, Halborn, dll.)
· Evidence: "Auditor: tidak diketahui (no public audit reports found as of research cutoff)"; "Tidak ada audit publik yang diumumkan oleh Vana Foundation" [Vana GitHub, https://github.com/vana-com] (HIGH) [Vana Blog, https://blog.vana.org] (HIGH) [Vana Docs, https://docs.vana.org] (HIGH)
· Supporting Dataset: Phase 4 Audit History, Phase 7 Ecosystem Risks, Phase 8 Market Summary

Financial Decision Pattern

Pola 1: Strategic VC Round dengan Tier-1 Investor Sebelum Public Token Launch
· Decision Pattern: Early 2023 funding dari Paradigm, Polymorphic Capital, Coinbase Ventures, Polychain Capital, Dragonfly Capital — semua tier-1 crypto VC — sebelum mainnet atau TGE
· Evidence: "Early Funding Round (2023) — Lead: Paradigm; Participating: Polymorphic, Coinbase Ventures, Polychain, Dragonfly"; Messari report konfirmasi [Messari Vana Report, https://messari.io/report/vana] (MEDIUM) [Vana Blog, https://blog.vana.org] (MEDIUM)
· Supporting Dataset: Phase 5 Funding History, Phase 2 Entities Investors, Phase 3 EV-005

Pola 2: Treasury dan Financial Transparency Minimal (Tidak Diungkap)
· Decision Pattern: Treasury size, composition, custodian arrangement, revenue history, grant program deployment — semua tidak diungkapkan publik
· Evidence: "Current Treasury Size: tidak diungkap"; "Treasury Composition: tidak diungkap"; "Revenue History: Tidak diungkap"; "Grant program: referenced in whitepaper; no public recipient list or amounts" [Vana Foundation GitHub, https://github.com/vana-com] (MEDIUM) [Vana Whitepaper, https://vana.org/whitepaper.pdf] (MEDIUM) [Vana Blog, https://blog.vana.org] (HIGH)
· Supporting Dataset: Phase 5 Treasury, Revenue History, Fundraising Mechanism, Phase 6 Token Distribution

Pola 3: Token Distribution Categories Didefinisikan Tanpa Persentase Spesifik
· Decision Pattern: Whitepaper mencantumkan kategori alokasi (Community, Team, Investors, Foundation, Treasury, Ecosystem, Advisors) tetapi tidak mempublikasikan persentase masing-masing
· Evidence: "Distribution Categories: Community, Team, Investors, Foundation, Treasury, Ecosystem, Advisors — semua persentase tidak diungkap"; "Whitepaper mentions allocation categories without percentages" [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH) [Vana Blog Token Launch, https://blog.vana.org/vana-token-launch/] (HIGH) [Messari Vana Report, https://messari.io/report/vana] (MEDIUM)
· Supporting Dataset: Phase 6 Distribution, Phase 6 Vesting Schedule

Pola 4: TGE via Claim Portal (Fair Launch Style) Bukan Public Sale
· Decision Pattern: Token Generation Event 2024-12-16 menggunakan claim portal (Vana Portal) untuk community allocation, tanpa fixed-price sale, launchpad, atau auction
· Evidence: "Launch Platform: Vana Portal (claim portal)"; "Community Sale: TGE community allocation distributed to Data DAO participants, testnet users, ecosystem contributors" [Vana Blog Token Launch, https://blog.vana.org/vana-token-launch/] (HIGH) [Vana Portal, https://portal.vana.org] (HIGH) [CoinGecko VANA, https://www.coingecko.com/en/coins/vana] (HIGH)
· Supporting Dataset: Phase 3 EV-016, Phase 6 TGE, Phase 6 Token Sale

Pola 5: Protocol Revenue Planned But Not Live; DAO-Level Revenue Active
· Decision Pattern: Whitepaper menyebutkan protocol fees (Data DAO tx fees, bridge fees, PoC verification fees) tapi tidak ada konfirmasi live pada mainnet; Data DAO individual menghasilkan revenue dari data sales
· Evidence: "Revenue Stream: Protocol Fees — Status: Planned / Not Live"; "Revenue Stream: Data DAO data sales — Status: Live at Data DAO level" [Vana Whitepaper, https://vana.org/whitepaper.pdf] (MEDIUM) [Vana Blog Data DAO Ecosystem, https://blog.vana.org/category/data-daos/] (HIGH)
· Supporting Dataset: Phase 5 Revenue Model, Phase 5 Revenue History, Phase 7 Applications

Pola 6: Staking Rewards sebagai Primary Protocol Revenue Mechanism (Live)
· Decision Pattern: CometBFT PoS staking rewards (inflationary emissions) live sejak mainnet 2024-10-16 sebagai revenue mechanism untuk validator dan delegator
· Evidence: "Revenue Stream: Validator Rewards / Staking Fees — Status: Live"; "Inflationary (PoS staking rewards menghasilkan emisian token baru)" [Vana Blog Mainnet Live, https://blog.vana.org/vana-mainnet-is-live/] (HIGH) [CometBFT Docs, https://docs.cometbft.com] (HIGH) [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH)
· Supporting Dataset: Phase 4 Consensus Mechanism, Phase 5 Revenue Model, Phase 6 Inflation/Deflation

Ecosystem Decision Pattern

Pola 1: Vertikal Data DAO Strategy — Launch 5 DAO Vertikal Berbeda Secara Serentak
· Decision Pattern: Meluncurkan 5 Data DAO pada vertikal berbeda (Social: Reddit, Twitter/X; Dating; DeFi; Gaming) secara paralel bukan sequential fokus satu vertikal
· Evidence: "r/datadao (Reddit data), Volara (Twitter/X data), Flirtual (dating data), DataPig (DeFi data), Kappa (gaming data)" — all launched 2023 testnet, mainnet 2024 [Vana Blog Data DAO Ecosystem, https://blog.vana.org/category/data-daos/] (HIGH) [Messari Vana Report, https://messari.io/report/vana] (HIGH)
· Supporting Dataset: Phase 2 Entities DAO, Phase 3 EV-006 through EV-010, Phase 7 Applications, Phase 7 Major Integrations

Pola 2: Universal Connectors SDK sebagai Standardisasi Data Portability
· Decision Pattern: Membangun SDK universal (TypeScript/Python) untuk developer membuat connectors dari platform Web2 apapun ke Data DAO, bukan custom integration per DAO
· Evidence: "Universal Connectors SDK: TypeScript/Python SDK untuk developer membangun data connectors"; "SDK untuk developer membangun konektor mengekspor data dari platform Web2 ke Data DAO via encrypted upload" [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH) [Vana Docs Connectors, https://docs.vana.org] (HIGH) [Vana GitHub, https://github.com/vana-com] (HIGH)
· Supporting Dataset: Phase 4 Core Components Universal Connectors, Phase 7 Major Integrations, Phase 7 Developer Ecosystem

Pola 3: Ethereum Bridge sebagai Primary Liquidity Gateway
· Decision Pattern: Prioritaskan Vana-Ethereum bridge untuk VANA token liquidity dan user onboarding dari Ethereum ecosystem, sebelum IBC channels ke Cosmos chains
· Evidence: Bridge live sejak mainnet 2024-10-16; "CEX listings dimulai segera setelah TGE"; IBC "enabled on mainnet; channels may be in progress" [Vana Blog Mainnet Live, https://blog.vana.org/vana-mainnet-is-live/] (HIGH) [Vana Docs Bridge, https://docs.vana.org] (HIGH) [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH)
· Supporting Dataset: Phase 4 Core Components Bridge, Phase 7 Major Integrations, Phase 8 Trading Markets

Pola 4: Vana Portal sebagai Unified Frontend untuk Semua Data DAO
· Decision Pattern: Single dashboard (Portal) untuk data contribution, Data DAO management, staking, reward tracking — bukan separate frontend per DAO
· Evidence: "Dashboard pengguna resmi Vana untuk kontribusi data, manajemen Data DAO, staking VANA, dan pelacakan reward"; "Live at portal.vana.org" [Vana Portal, https://portal.vana.org] (HIGH) [Vana Docs, https://docs.vana.org] (HIGH) [Vana Blog Mainnet Live, https://blog.vana.org/vana-mainnet-is-live/] (HIGH)
· Supporting Dataset: Phase 4 Core Components Vana Portal, Phase 7 Applications, Phase 7 Major Integrations

Pola 5: Grant Program Referenced in Whitepaper But Not Deployed Publicly
· Decision Pattern: Whitepaper menyebutkan ecosystem grants tapi tidak ada public application process, recipient list, atau deployment metrics per cutoff
· Evidence: "Grant Program: Vana Foundation Ecosystem Grants (referenced in whitepaper) — Status: Planned / Referenced (no public recipient list, amounts, or application process published)" [Vana Whitepaper, https://vana.org/whitepaper.pdf] (MEDIUM) [Vana Blog, https://blog.vana.org] (MEDIUM)
· Supporting Dataset: Phase 7 Developer Ecosystem, Phase 5 Fundraising Mechanism, Phase 7 Official Ecosystem Resources

Pola 6: Dependency pada Upstream Cosmos/Ethermint Tanpa Fork Customization Mendalam
· Decision Pattern: Menggunakan Cosmos SDK, CometBFT, Ethermint sebagai upstream dependencies tanpa fork mendalam; custom modules hanya PoC, Bridge, IBC config
· Evidence: External dependencies: Cosmos SDK, CometBFT, Ethermint semua "Critical" status; "Core blockchain bergantung pada upstream maintenance" [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH) [Vana GitHub, https://github.com/vana-com] (HIGH) [Cosmos SDK Docs, https://docs.cosmos.network] (HIGH)
· Supporting Dataset: Phase 7 External Dependencies, Phase 4 Core Components, Phase 7 Ecosystem Risks

Governance Decision Pattern

Pola 1: Foundation-Controlled Entity dengan On-Chain Governance Module Live
· Decision Pattern: Vana Foundation (Cayman Islands) sebagai entitas hukum tunggal mengelola treasury dan strategic direction, sementara on-chain governance (Cosmos SDK module) live untuk parameter changes dan upgrades
· Evidence: "Foundation: Vana Foundation — Entitas hukum resmi (Cayman Islands) mengawasi pengembangan protokol, ekosistem Data DAO, governance token VANA"; "Governance Model: On-chain governance via Cosmos SDK governance module; token-weighted voting" [Vana Foundation GitHub, https://github.com/vana-com] (HIGH) [Vana Docs Governance, https://docs.vana.org/governance] (HIGH)
· Supporting Dataset: Phase 2 Entity Vana Foundation, Phase 4 Consensus Mechanism, Phase 6 Governance, Phase 7 Governance Ecosystem

Pola 2: Token-Weighted Voting dengan Delegation (Standard Cosmos SDK)
· Decision Pattern: 1 VANA = 1 vote melalui staked/delegated token; delegator bisa override validator vote; standard Cosmos SDK governance flow
· Evidence: "Voting Power: Berdasarkan VANA yang di-stake (bonded token); delegator voting power mengikuti validator choice kecuali delegator override"; "Proposal System: On-chain proposal submission memerlukan deposit minimum" [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH) [Vana Docs Governance, https://docs.vana.org/governance] (HIGH) [Cosmos SDK Governance, https://docs.cosmos.network/main/build/modules/gov] (HIGH)
· Supporting Dataset: Phase 6 Governance, Phase 4 Consensus Mechanism, Phase 7 Governance Ecosystem

Pola 3: Validator Set sebagai Governance Power Broker (Bridge Attestation + Consensus + Voting)
· Decision Pattern: Validator set memegang multiple governance roles: consensus (CometBFT), bridge attestation (Vana-Ethereum bridge), on-chain voting power (staked VANA)
· Evidence: "Validator Set: Consensus participation; governance voting power berdasarkan stake; bridge attestation untuk Vana-Ethereum bridge" [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH) [Vana Explorer, https://explorer.vana.org] (HIGH) [CometBFT Docs, https://docs.cometbft.com] (HIGH)
· Supporting Dataset: Phase 4 Consensus Mechanism, Phase 4 Core Components Bridge, Phase 7 Governance Ecosystem

Pola 4: Data DAO Governance Terpisah dari Protocol Governance
· Decision Pattern: Setiap Data DAO (r/datadao, Volara, Flirtual, DataPig, Kappa) memiliki governance sendiri atas data kolektif, reward distribution, treasury — terpisah dari Vana protocol governance
· Evidence: "DAO: r/datadao — Role: governance atas data Reddit kolektif, reward distribution, treasury management"; sama untuk Volara, Flirtual, DataPig, Kappa [Vana Blog Data DAO Ecosystem, https://blog.vana.org/category/data-daos/] (HIGH) [Messari Vana Report, https://messari.io/report/vana] (MEDIUM)
· Supporting Dataset: Phase 2 Entities DAO, Phase 7 Governance Ecosystem, Phase 7 Applications

Pola 5: Community Pool / Protocol Treasury Governance Parameters Tidak Dipublikasikan
· Decision Pattern: On-chain governance module live tapi parameter critical (deposit minimum, voting period, quorum, community pool activation) tidak di-dokumentasikan publik
· Evidence: "Treasury Governance: Community pool (jika diaktifkan) dikontrol via governance proposals; Vana Foundation treasury terpisah dari protocol treasury — detail tidak diungkap" [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH) [Vana Docs Governance, https://docs.vana.org/governance] (HIGH)
· Supporting Dataset: Phase 6 Governance, Phase 5 Treasury, Phase 7 Governance Ecosystem

Risk Response Pattern

Pola 1: Bridge Trust Model Risk — Accepted Validator-Set Attestation Model
· Decision Pattern: Menerima trust assumption honest majority validators untuk bridge security, bukan implement trust-minimized light client bridge
· Evidence: "Bridge trust model bergantung pada validator set Vana (honest majority assumption); bukan trust-minimized seperti light-client bridge" [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH) [Vana Docs Bridge, https://docs.vana.org] (HIGH)
· Trigger: Perlu bridge cepat untuk mainnet launch dan TGE liquidity; light client bridge butuh development time lebih lama
· Response: Deploy validator-set attestation bridge dengan multi-sig/threshold signature; monitor bridge contracts; plan upgrade path ke trust-minimized model (tidak di-dokumentasikan)
· Result: Bridge live sejak mainnet; single point of failure untuk cross-chain asset; audit belum diumumkan
· Supporting Dataset: Phase 4 Known Technical Limitations, Phase 7 Ecosystem Risks Bridge Dependency, Phase 4 Core Components Bridge

Pola 2: No Public Audit Risk — Launch Without Public Audit Reports
· Decision Pattern: Launch mainnet dan TGE tanpa mempublikasikan audit report; mengandalkan internal review dan testnet battle-testing
· Evidence: "Auditor: tidak diketahui (no public audit reports found)"; "Tidak ada audit keamanan publik yang diumumkan" [Vana GitHub, https://github.com/vana-com] (HIGH) [Vana Blog, https://blog.vana.org] (HIGH)
· Trigger: Timeline pressure untuk mainnet 2024-10 dan TGE 2024-12; audit process bisa delay launch
· Response: Launch dengan testnet validation (15 bulan Moksha); bug bounty program tidak diumumkan; audit menjadi open thread untuk post-TGE
· Result: Security researchers tidak bisa verify; institutional adoption barrier; exploit risk unquantified
· Supporting Dataset: Phase 4 Audit History, Phase 7 Ecosystem Risks Security Dependency, Phase 8 Market Summary

Pola 3: Data DAO Connector Verification Fragmentation — Delegated to Individual DAOs
· Decision Pattern: Tidak enforce universal Proof-of-Contribution verification standard di protocol level; setiap Data DAO memilih method sendiri (zkTLS, TEE, API signatures)
· Evidence: "Proof-of-Contribution verification quality bergantung pada connector implementation per Data DAO; tidak ada universal verification standard enforced at protocol level" [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH) [Vana Docs PoC, https://docs.vana.org] (HIGH)
· Trigger: Berbagai data source (Reddit, Twitter, dating app, DeFi, gaming) butuh verification method berbeda; standardization terlalu rigid
· Response: PoC module menyediakan framework; Data DAO implement connector-specific verification; protocol tidak validate quality
· Result: Verification quality bervariasi across DAOs; buyer trust bergantung per DAO reputation; fraudulent submission risk per DAO
· Supporting Dataset: Phase 4 Known Technical Limitations, Phase 7 Ecosystem Risks Data Quality Risk, Phase 7 Major Integrations

Pola 4: Regulatory Uncertainty — Acknowledged But Not Actively Mitigated Publicly
· Decision Pattern: Whitepaper mengakui ketidakpastian regulasi Data DAO tapi tidak mempublikasikan legal opinions, jurisdictional analysis, atau compliance framework
· Evidence: "Regulatory status of Data DAOs in various jurisdictions — whitepaper acknowledges uncertainty"; "Status regulasi Data DAO di berbagai yurisdiksi tidak pasti; whitepaper mengakui ketidakpastian regulasi" [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH) [Messari Vana Report, https://messari.io/report/vana] (MEDIUM)
· Trigger: Data DAO model novel (user data collectives, token rewards); regulasi data privacy (GDPR, CCPA), securities law, DAO legal status belum jelas
· Response: Cayman Islands foundation structure; token sebagai utility (governance, staking, fees); tidak menjamin compliance di semua yurisdiksi
· Result: Ongoing regulatory risk untuk token holders, Data DAO operators, users; potential enforcement action bisa disrupt operations
· Supporting Dataset: Phase 1 Open Threads, Phase 3 Open Threads, Phase 7 Ecosystem Risks Regulation Dependency, Phase 8 Narrative Position

Pola 5: Upstream Dependency Risk — Standard Cosmos SDK Upgrade Path
· Decision Pattern: Mengandalkan upstream Cosmos SDK, CometBFT, Ethermint untuk security patches dan upgrades; tidak maintain hard forks
· Evidence: "Core blockchain bergantung pada upstream maintenance dari Cosmos SDK, CometBFT, Ethermint (Evmos); breaking changes atau vulnerability upstream mempengaruhi Vana langsung" [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH) [Vana GitHub, https://github.com/vana-com] (HIGH)
· Trigger: Resource constraints; small team (~30+) tidak bisa maintain full stack independently
· Response: Monitor upstream releases; coordinate upgrades via on-chain governance; testnet validation sebelum mainnet upgrade
· Result: Upgrade velocity tergantung upstream; custom modules (PoC, Bridge) perlu compatibility testing setiap upgrade
· Supporting Dataset: Phase 7 External Dependencies, Phase 7 Ecosystem Risks SDK/Protocol Dependency, Phase 4 Technical Upgrade History

Recurring Behavioral Pattern

Pola 1: Testnet-First Approach dengan Real Users dan Real Data DAOs
· Decision Pattern: Setiap major component diuji di testnet publik dengan real users dan real Data DAO operators sebelum mainnet deployment
· Evidence: Moksha testnet 2023-07 dengan 5 Data DAO live, validator set, PoC mechanism, bridge testing — 15 bulan sebelum mainnet [Vana Blog Introducing Moksha, https://blog.vana.org/introducing-moksha-testnet/] (HIGH) [Vana Blog Mainnet Live, https://blog.vana.org/vana-mainnet-is-live/] (HIGH)
· Supporting Dataset: Phase 3 EV-004, EV-006 through EV-010, EV-013, Phase 4 Technical Upgrade History

Pola 2: Vertical Data DAO Expansion Paralel (Bukan Sequential)
· Decision Pattern: Launch multiple Data DAO vertikal secara bersamaan (social, dating, DeFi, gaming) untuk demonstrate platform versatility
· Evidence: 5 Data DAO diluncurkan 2023 di testnet: r/datadao, Volara, Flirtual, DataPig, Kappa — semua migrasi ke mainnet 2024 [Vana Blog Data DAO Ecosystem, https://blog.vana.org/category/data-daos/] (HIGH) [Messari Vana Report, https://messari.io/report/vana] (HIGH)
· Supporting Dataset: Phase 3 EV-006 through EV-010, Phase 7 Applications, Phase 7 Major Integrations

Pola 3: Strategic Investor Alignment Sebelum Public Launch
· Decision Pattern: Secure tier-1 VC funding (Paradigm, Polymorphic, Coinbase Ventures, Polychain, Dragonfly) pada 2023, jauh sebelum mainnet/TGE
· Evidence: Early 2023 funding round dengan 5 tier-1 investors; Messari report konfirmasi [Messari Vana Report, https://messari.io/report/vana] (MEDIUM) [Vana Blog, https://blog.vana.org] (MEDIUM)
· Supporting Dataset: Phase 2 Entities Investors, Phase 3 EV-005, Phase 5 Funding History, Phase 7 External Dependencies

Pola 4: Decouple Chain Launch dari Token Launch (Gap ~2 Bulan)
· Decision Pattern: Mainnet genesis 2024-10-16 (chain live, staking active) → TGE 2024-12-16 (token transferable, trading live)
· Evidence: "Mainnet diluncurkan dengan VANA sebagai native gas dan staking token; TGE belum terjadi"; "TGE & VANA token launch 2024-12-16" [Vana Blog Mainnet Live, https://blog.vana.org/vana-mainnet-is-live/] (HIGH) [Vana Blog Token Launch, https://blog.vana.org/vana-token-launch/] (HIGH)
· Supporting Dataset: Phase 3 EV-013, EV-016, Phase 6 Major Token Events

Pola 5: Minimal Public Financial Transparency (Consistent Across Phases)
· Decision Pattern: Treasury size, token distribution percentages, vesting schedules, revenue numbers, grant deployments — semua tidak diungkapkan secara konsisten dari foundation → mainnet → TGE
· Evidence: Phase 5 Treasury "tidak diungkap"; Phase 6 Distribution "persentase tidak diungkap"; Phase 6 Vesting "tidak diketahui"; Phase 5 Revenue History "Tidak diungkap"; Phase 7 Grant Program "no public recipient list" [Phase 5 Financial, Phase 6 Token, Phase 7 Ecosystem] (HIGH)
· Supporting Dataset: Phase 5 Treasury, Revenue History, Phase 6 Distribution, Vesting Schedule, Phase 7 Developer Ecosystem

Pola 6: Bridge-First Liquidity Strategy (Ethereum Before Cosmos IBC)
· Decision Pattern: Prioritaskan Vana-Ethereum bridge untuk token liquidity dan user onboarding; IBC channels ke Cosmos ecosystem secondary
· Evidence: Bridge live mainnet 2024-10-16; CEX listings post-TGE; IBC "enabled; active channels not publicly documented" [Vana Blog Mainnet Live, https://blog.vana.org/vana-mainnet-is-live/] (HIGH) [Vana Docs Bridge, https://docs.vana.org] (HIGH) [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH)
· Supporting Dataset: Phase 4 Core Components Bridge, Phase 7 Major Integrations, Phase 8 Trading Markets

Strategic Trade-offs

Trade-off 1: Sovereign L1 vs Shared Security (Ethereum L2/Restaking)
· Decision: Build sovereign L1 (Cosmos SDK) dengan own validator set dan VANA staking security
· Trade-off: Full control atas consensus, execution, governance, custom modules (PoC) vs higher security budget requirement (own validator incentives), bridge dependency untuk Ethereum liquidity, no shared security dari Ethereum
· Evidence: "Architecture Type: Layer 1 blockchain berbasis Cosmos SDK dengan kompatibilitas EVM"; "Economic Security: VANA token staking di Vana L1; total staked VANA menentukan attack cost"; "Bridge trust model bergantung pada validator set Vana" [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH) [Vana Docs Architecture, https://docs.vana.org] (HIGH) [Vana Blog Mainnet Live, https://blog.vana.org/vana-mainnet-is-live/] (HIGH)
· Supporting Dataset: Phase 4 System Architecture, Phase 4 Consensus Mechanism, Phase 7 Ecosystem Risks, Phase 8 Narrative Position

Trade-off 2: Validator-Set Bridge (Speed to Market) vs Trust-Minimized Light Client Bridge (Security)
· Decision: Deploy validator-set attestation bridge untuk mainnet launch dan TGE liquidity
· Trade-off: Faster deployment, simpler architecture vs honest majority trust assumption, single point of failure, not trust-minimized
· Evidence: "Bridge Security: Validator-set attestation model"; "Bridge trust model bergantung pada validator set Vana (honest majority assumption); bukan trust-minimized seperti light-client bridge" [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH) [Vana Docs Bridge, https://docs.vana.org] (HIGH)
· Supporting Dataset: Phase 4 Core Components Bridge, Phase 4 Known Technical Limitations, Phase 7 Ecosystem Risks Bridge Dependency

Trade-off 3: Modular Cosmos SDK (Flexibility) vs Upstream Dependency Risk
· Decision: Gunakan Cosmos SDK, CometBFT, Ethermint sebagai upstream dependencies tanpa deep forks
· Trade-off: Rapid development, battle-tested components, IBC native vs upstream breaking changes affect Vana, limited differentiation at consensus/execution layer, upgrade coordination complexity
· Evidence: "Core blockchain bergantung pada upstream maintenance dari Cosmos SDK, CometBFT, Ethermint"; External dependencies semua "Critical" [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH) [Vana GitHub, https://github.com/vana-com] (HIGH) [Cosmos SDK Docs, https://docs.cosmos.network] (HIGH)
· Supporting Dataset: Phase 7 External Dependencies, Phase 7 Ecosystem Risks SDK/Protocol Dependency, Phase 4 Technical Upgrade History

Trade-off 4: Data DAO Verification Flexibility (Per-DAO) vs Protocol-Level Quality Standard
· Decision: Delegasikan Proof-of-Contribution verification method ke setiap Data DAO (zkTLS, TEE, API signatures) tanpa universal standard
· Trade-off: Innovation per DAO, fit-for-purpose verification vs inconsistent quality, buyer trust fragmentation, protocol cannot guarantee data quality
· Evidence: "Proof-of-Contribution verification quality bergantung pada connector implementation per Data DAO; tidak ada universal verification standard enforced at protocol level" [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH) [Vana Docs PoC, https://docs.vana.org] (HIGH)
· Supporting Dataset: Phase 4 Known Technical Limitations, Phase 7 Ecosystem Risks Data Quality Risk, Phase 7 Major Integrations

Trade-off 5: Off-Chain Data Storage Delegation (Protocol Simplicity) vs Data Availability Guarantee
· Decision: Protocol tidak provide data availability layer; Data DAO pilih IPFS/Arweave/cloud sendiri
· Trade-off: Protocol simplicity, no storage cost burden, DAO sovereignty vs no persistence guarantee, data loss risk, buyer uncertainty
· Evidence: "Off-chain data storage untuk Data DAO raw data (IPFS, Arweave, atau centralized cloud per Data DAO design)"; "protocol tidak menjamin persistence atau availability" [Vana Whitepaper, https://vana.org/whitepaper.pdf] (HIGH) [Universal Connectors Docs, https://docs.vana.org] (HIGH)
· Supporting Dataset: Phase 4 System Architecture Storage, Phase 4 Known Technical Limitations, Phase 7 Ecosystem Risks Data Provider Dependency

Trade-off 6: Financial Opacity (Strategic Flexibility) vs Transparency (Community Trust)
· Decision: Tidak mengungkap treasury size, token distribution %, vesting schedule, revenue, grant deployments
· Trade-off: Strategic flexibility untuk foundation, negotiation leverage, regulatory caution vs community trust deficit, institutional adoption barrier, cannot verify alignment
· Evidence: Phase 5 Treasury "tidak diungkap"; Phase 6 Distribution "persentase tidak diungkap"; Phase 6 Vesting "tidak diketahui"; Phase 5 Revenue History "Tidak diungkap"; Phase 7 Grant Program "no public recipient list" [Phase 5 Financial, Phase 6 Token, Phase 7 Ecosystem] (HIGH)
· Supporting Dataset: Phase 5 Treasury, Revenue History, Phase 6 Distribution, Vesting Schedule, Phase 7 Developer Ecosystem

Trade-off 7: No Public Audit Pre-Launch (Speed) vs Security Assurance (Trust)
· Decision: Launch mainnet dan TGE tanpa public audit report
· Trade-off: Meet launch timeline, avoid audit delay vs unknown vulnerabilities, no institutional-grade security validation, insurance exclusion
· Evidence: "Auditor: tidak diketahui (no public audit reports found)"; "Tidak ada audit keamanan publik yang diumumkan" [Vana GitHub, https://github.com/vana-com] (HIGH) [Vana Blog, https://blog.vana.org] (HIGH) [Vana Docs, https://docs.vana.org] (HIGH)
· Supporting Dataset: Phase 4 Audit History, Phase 7 Ecosystem Risks Security Dependency, Phase 8 Market Summary

Behavioral Summary

Prioritas Utama Proyek:
1. Product-Market Fit via Data DAO Verticals — Membuktikan data liquidity model bekerja di 5 vertikal (social, dating, DeFi, gaming) sebelum expand
2. Sovereign Infrastructure Control — Own L1 untuk custom PoC module, governance parameters, upgrade velocity
3. Ethereum Ecosystem Integration — Bridge + EVM compatibility sebagai primary liquidity dan user onboarding gateway
4. Community-First Token Distribution — TGE via claim portal ke Data DAO contributors, testnet users, bukan public sale
5. Long-Term Investor Alignment — Tier-1 VC secured early untuk runway dan strategic guidance

Cara Mengambil Keputusan:
- Technical: Whitepaper-first design → testnet validation (15 bulan) → mainnet production → iterative upgrades via on-chain governance
- Financial: Strategic VC round → foundation treasury → TGE token allocation → protocol revenue planned later
- Ecosystem: Parallel vertical DAO launch → universal SDK standardization → unified Portal frontend → grant program later
- Governance: Foundation legal wrapper → on-chain module live at mainnet → token-weighted voting → DAO-level governance separation
- Risk: Accept known trade-offs (bridge trust, upstream dependency, verification fragmentation) untuk speed-to-market; audit dan transparency deferred

Faktor Paling Sering Mempengaruhi Keputusan:
1. Speed-to-market untuk mainnet dan TGE (deadline-driven)
2. Investor expectations (tier-1 VC runway dan strategic value)
3. Technical architecture commitments (Cosmos SDK stack chosen early, path-dependent)
4. Data DAO operator needs (connector flexibility, verification autonomy)
5. Regulatory caution (Cayman foundation, utility token framing, no public sale)

Pola Evolusi:
- 2021-2022: Concept & team formation (stealth)
- 2023: Foundation + Whitepaper + Testnet + 5 DAOs + VC Funding (infrastructure build phase)
- 2024 H1: Testnet hardening, mainnet prep
- 2024-10: Mainnet genesis (chain live, staking, DAOs, bridge)
- 2024-12: TGE (token transferable, trading, expanded governance)
- 2025+: Ecosystem expansion, grant program, audit, transparency improvements (projected)

Kekuatan Utama:
- Clear narrative differentiation: Data DAO infrastructure (bukan general data marketplace)
- Live product dengan 5 vertical DAOs operating pada mainnet
- Tier-1 investor syndicate providing capital dan network
- Modular sovereign L1 dengan custom PoC module (technical moat)
- Universal Connectors SDK mengurangi friction untuk new Data DAO
- Unified Portal UX untuk end-users

Kelemahan Utama:
- Zero public financial transparency (treasury, distribution, vesting, revenue)
- No public security audits untuk mainnet code handling value
- Bridge trust model = honest majority validators (single point of failure)
- Upstream dependency pada Cosmos/Ethermint tanpa deep customization
- Data DAO verification quality fragmented, no protocol-level standard
- Regulatory uncertainty unmitigated publicly
- IBC ecosystem integration minimal (channels not documented)
- Validator set economics opaque (no staking dashboard)
- Grant program vaporware (referenced not deployed)

## Knowledge Extraction
_ref: `docs/Patterns/*`, `docs/Reasoning/*` (rule candidates)_

PROJECT: Vana

## Core Insights

Insight 1: Sovereign L1 dengan custom application-layer module (Proof-of-Contribution) menciptakan technical moat yang sulit direplikasi oleh general-purpose L1 atau L2
Explanation: Vana memilih arsitektur Cosmos SDK + CometBFT + Ethermint untuk membangun sovereign L1 yang memisahkan consensus (CometBFT), execution (EVM via Ethermint), dan application layer (PoC module, Bridge module, IBC module). PoC bukan consensus mechanism melainkan application-layer module untuk data quality valuation dan reward distribution di Data DAO【Phase 4 — System Architecture】【Phase 4 — Core Components】【Phase 4 — Consensus Mechanism】【Phase 9 — Technical Decision Pattern Pola 3】.
Evidence: Whitepaper arsitektur mendefinisikan modular separation; PoC module custom di Cosmos SDK; CometBFT untuk BFT PoS consensus; Ethermint untuk EVM execution【Phase 4 — System Architecture】【Phase 4 — Core Components】.
Supporting Dataset: Phase 4 Technology, Phase 9 Behavioral Technical Decision Pattern
Confidence: HIGH

Insight 2: Decoupling chain launch (mainnet genesis) dari token launch (TGE) ~2 bulan memberikan keuntungan: validator set earning rewards sejak hari 1, Data DAO operating, bridge contracts deployed, namun menciptakan potential insider advantage bagi early stakers/validators
Explanation: Mainnet live 2024-10-16 dengan native VANA minted pada genesis untuk gas dan staking; TGE 2024-12-16 terpisah untuk token transferable dan trading【Phase 3 — EV-013】【Phase 3 — EV-016】【Phase 9 — Decision Timeline Keputusan: Meluncurkan Vana Mainnet 2024-10-16 tanpa VANA token transferable】.
Evidence: Blog Mainnet Live menyebutkan native VANA minted pada genesis; Blog Token Launch menyebutkan TGE terpisah 2 bulan kemudian【Phase 3 — EV-013】【Phase 3 — EV-016】.
Supporting Dataset: Phase 3 History, Phase 6 Token Major Token Events, Phase 9 Decision Timeline
Confidence: HIGH

Insight 3: Parallel vertical Data DAO launch (5 DAO sekaligus: social, dating, DeFi, gaming) mendemonstrasikan platform versatility namun menciptakan verification quality fragmentation karena tidak ada universal Proof-of-Contribution standard enforced at protocol level
Explanation: 5 Data DAO diluncurkan 2023 di testnet: r/datadao (Reddit), Volara (Twitter/X), Flirtual (dating), DataPig (DeFi), Kappa (gaming) — semua migrasi ke mainnet 2024【Phase 3 — EV-006】【Phase 3 — EV-007】【Phase 3 — EV-008】【Phase 3 — EV-009】【Phase 3 — EV-010】【Phase 9 — Ecosystem Decision Pattern Pola 1】. PoC verification quality bergantung pada connector implementation per Data DAO tanpa universal standard【Phase 4 — Known Technical Limitations】【Phase 7 — Ecosystem Risks Data Quality Risk】.
Evidence: Blog Data DAO Ecosystem mencatat 5 DAO live; Whitepaper menyatakan PoC verification tidak distandarisasi di protocol level【Phase 3 — EV-006】【Phase 3 — EV-007】【Phase 3 — EV-008】【Phase 3 — EV-009】【Phase 3 — EV-010】【Phase 4 — Known Technical Limitations】.
Supporting Dataset: Phase 3 History, Phase 4 Technology, Phase 7 Ecosystem, Phase 9 Ecosystem Decision Pattern
Confidence: HIGH

Insight 4: Validator-set attestation bridge model (honest majority assumption) dipilih untuk speed-to-market mainnet/TGE liquidity, bukan trust-minimized light-client bridge, menciptakan single point of failure untuk cross-chain asset
Explanation: Vana-Ethereum bridge menggunakan validator set Vana untuk attestation mint/burn; bukan light-client verification【Phase 4 — Core Components Bridge】【Phase 4 — Known Technical Limitations】【Phase 7 — Ecosystem Risks Bridge Dependency】【Phase 9 — Strategic Trade-offs Trade-off 2】.
Evidence: Whitepaper bridge design; Known Technical Limitations mencatat bridge trust model bergantung validator set; Strategic Trade-offs mengakui trade-off speed vs security【Phase 4 — Core Components Bridge】【Phase 4 — Known Technical Limitations】【Phase 9 — Strategic Trade-offs Trade-off 2】.
Supporting Dataset: Phase 4 Technology, Phase 7 Ecosystem Risks, Phase 9 Strategic Trade-offs
Confidence: HIGH

Insight 5: Zero public financial transparency (treasury size, token distribution %, vesting schedule, revenue, grant deployments) konsisten dari foundation hingga post-TGE, menciptakan trust deficit untuk institutional adoption
Explanation: Treasury size "tidak diungkap"; Distribution categories tanpa persentase; Vesting schedule "tidak diketahui"; Revenue history "Tidak diungkap"; Grant program "no public recipient list"【Phase 5 — Treasury】【Phase 5 — Revenue History】【Phase 6 — Distribution】【Phase 6 — Vesting Schedule】【Phase 7 — Developer Ecosystem Grant Program】【Phase 9 — Recurring Behavioral Pattern Pola 5】.
Evidence: Phase 5 Financial seluruhnya minimal disclosure; Phase 6 Token tidak ada angka spesifik; Phase 7 Grant Program referenced not deployed【Phase 5 — Treasury】【Phase 5 — Revenue History】【Phase 6 — Distribution】【Phase 6 — Vesting Schedule】【Phase 7 — Developer Ecosystem Grant Program】.
Supporting Dataset: Phase 5 Financial, Phase 6 Token, Phase 7 Ecosystem, Phase 9 Behavioral Pattern
Confidence: HIGH

Insight 6: Testnet-first approach dengan real users dan real Data DAOs selama 15 bulan (Moksha Juli 2023 → Mainnet Oktober 2024) memvalidasi infrastructure sebelum production value at risk
Explanation: Moksha testnet 2023-07 dengan 5 Data DAO live, validator set, PoC mechanism, bridge testing — 15 bulan sebelum mainnet【Phase 3 — EV-004】【Phase 3 — EV-006】through【Phase 3 — EV-010】【Phase 9 — Recurring Behavioral Pattern Pola 1】.
Evidence: Blog Introducing Moksha Testnet; Blog Mainnet Live; 5 Data DAO deployed di testnet sebelum mainnet【Phase 3 — EV-004】【Phase 3 — EV-006】【Phase 3 — EV-007】【Phase 3 — EV-008】【Phase 3 — EV-009】【Phase 3 — EV-010】.
Supporting Dataset: Phase 3 History, Phase 4 Technical Upgrade History, Phase 9 Behavioral Pattern
Confidence: HIGH

Insight 7: No public security audit announcement sebelum mainnet launch dan TGE — launch mengandalkan internal review dan testnet battle-testing, menciptakan barrier untuk institutional adoption dan insurance coverage
Explanation: "Auditor: tidak diketahui (no public audit reports found)"; "Tidak ada audit keamanan publik yang diumumkan"【Phase 4 — Audit History】【Phase 7 — Ecosystem Risks Security Dependency】【Phase 9 — Technical Decision Pattern Pola 7】.
Evidence: GitHub, Blog, Docs tidak memiliki audit announcements per research cutoff【Phase 4 — Audit History】【Phase 7 — Ecosystem Risks Security Dependency】.
Supporting Dataset: Phase 4 Technology, Phase 7 Ecosystem Risks, Phase 9 Technical Decision Pattern
Confidence: HIGH

Insight 8: Universal Connectors SDK sebagai standardization layer mengurangi friction untuk new Data DAO onboarding — TypeScript/Python SDK untuk developer membangun connectors dari platform Web2 apapun ke Data DAO via encrypted upload
Explanation: SDK universal (TypeScript/Python) untuk developer membuat connectors dari platform Web2 ke Data DAO, bukan custom integration per DAO【Phase 4 — Core Components Universal Connectors】【Phase 7 — Major Integrations Universal Connectors SDK + Web2 Platforms】【Phase 9 — Ecosystem Decision Pattern Pola 2】.
Evidence: Whitepaper Universal Connectors; Docs Connectors; GitHub monorepo structure【Phase 4 — Core Components Universal Connectors】【Phase 7 — Major Integrations Universal Connectors SDK + Web2 Platforms】.
Supporting Dataset: Phase 4 Technology, Phase 7 Ecosystem, Phase 9 Ecosystem Decision Pattern
Confidence: HIGH

Insight 9: Foundation-controlled entity (Cayman Islands Vana Foundation) dengan on-chain governance module live menciptakan dual governance structure: legal wrapper untuk treasury/strategic direction + token-weighted voting untuk parameter changes
Explanation: Vana Foundation (Cayman Islands) sebagai entitas hukum tunggal mengelola treasury dan strategic direction; on-chain governance (Cosmos SDK module) live untuk parameter changes dan upgrades【Phase 2 — Entity Vana Foundation】【Phase 4 — Consensus Mechanism】【Phase 6 — Governance】【Phase 7 — Governance Ecosystem Foundation】【Phase 9 — Governance Decision Pattern Pola 1】.
Evidence: Foundation GitHub dan team page; Whitepaper governance; Cosmos SDK governance module standard【Phase 2 — Entity Vana Foundation】【Phase 4 — Consensus Mechanism】【Phase 6 — Governance】.
Supporting Dataset: Phase 2 Entity, Phase 4 Technology, Phase 6 Token, Phase 7 Ecosystem, Phase 9 Governance Decision Pattern
Confidence: HIGH

Insight 10: Early strategic VC round dengan 5 tier-1 investors (Paradigm, Polymorphic Capital, Coinbase Ventures, Polychain Capital, Dragonfly Capital) pada 2023 memberikan runway dan network sebelum mainnet/TGE, namun investor token unlock concentration risk tidak terquantified publik
Explanation: Early 2023 funding round dari 5 tier-1 VC jauh sebelum mainnet/TGE【Phase 3 — EV-005】【Phase 5 — Funding History】【Phase 9 — Financial Decision Pattern Pola 1】【Phase 9 — Recurring Behavioral Pattern Pola 3】. Vesting schedule investor tidak diungkapkan【Phase 6 — Vesting Schedule Category: Investors】【Phase 7 — Ecosystem Risks Investor Token Unlock Concentration】.
Evidence: Messari report konfirmasi funding round; Whitepaper menciona investor allocation tanpa detail【Phase 3 — EV-005】【Phase 5 — Funding History】【Phase 6 — Vesting Schedule】.
Supporting Dataset: Phase 3 History, Phase 5 Financial, Phase 6 Token, Phase 7 Ecosystem Risks, Phase 9 Financial Decision Pattern
Confidence: HIGH

## Strategic Principles

Principle 1: Modular App-Chain Architecture First — Memilih sovereign L1 dengan modular separation (CometBFT consensus, Ethermint EVM execution, custom application modules) daripada deploy sebagai L2/rollup atau gunakan existing chain untuk full control atas consensus, execution, governance parameters, dan custom modules (PoC, Bridge)【Phase 4 — System Architecture】【Phase 9 — Technical Decision Pattern Pola 1】【Phase 9 — Strategic Trade-offs Trade-off 1】.
Evidence: Whitepaper arsitektur Layer 1 Cosmos SDK; Technical Decision Pattern Pola 1; Strategic Trade-offs Trade-off 1【Phase 4 — System Architecture】【Phase 9 — Technical Decision Pattern Pola 1】【Phase 9 — Strategic Trade-offs Trade-off 1】.
Supporting Dataset: Phase 4 Technology, Phase 9 Technical Decision Pattern, Phase 9 Strategic Trade-offs
Confidence: HIGH

Principle 2: EVM Compatibility via Ethermint sebagai Execution Layer — Menggunakan Ethermint (Evmos) sebagai EVM module di atas Cosmos SDK daripada build custom EVM atau gunakan WASM/CosmWasm untuk leverage existing Ethereum tooling (MetaMask, Hardhat, Foundry) dan developer familiarity【Phase 4 — Execution Environment】【Phase 9 — Technical Decision Pattern Pola 2】【Phase 8 — Narrative Position EVM-Compatible L1】.
Evidence: Execution Environment Primary EVM via Ethermint; Technical Decision Pattern Pola 2; Narrative Position EVM-Compatible L1【Phase 4 — Execution Environment】【Phase 9 — Technical Decision Pattern Pola 2】【Phase 8 — Narrative Position EVM-Compatible L1】.
Supporting Dataset: Phase 4 Technology, Phase 8 Market, Phase 9 Technical Decision Pattern
Confidence: HIGH

Principle 3: Testnet-First dengan Real Users dan Real Data DAOs — Setiap major component diuji di testnet publik dengan real users dan real Data DAO operators sebelum mainnet deployment (Moksha 15 bulan)【Phase 3 — EV-004】【Phase 9 — Recurring Behavioral Pattern Pola 1】【Phase 4 — Technical Upgrade History Moksha Testnet Launch】.
Evidence: Moksha testnet launch 2023-07 dengan 5 Data DAO live; Recurring Behavioral Pattern Pola 1; Technical Upgrade History【Phase 3 — EV-004】【Phase 9 — Recurring Behavioral Pattern Pola 1】【Phase 4 — Technical Upgrade History】.
Supporting Dataset: Phase 3 History, Phase 4 Technology, Phase 9 Behavioral Pattern
Confidence: HIGH

Principle 4: Parallel Vertical Data DAO Expansion — Launch multiple Data DAO vertikal secara bersamaan (social, dating, DeFi, gaming) untuk demonstrate platform versatility bukan sequential fokus satu vertikal【Phase 3 — EV-006】through【Phase 3 — EV-010】【Phase 9 — Ecosystem Decision Pattern Pola 1】【Phase 9 — Recurring Behavioral Pattern Pola 2】.
Evidence: 5 Data DAO diluncurkan 2023 testnet semua; Ecosystem Decision Pattern Pola 1; Recurring Behavioral Pattern Pola 2【Phase 3 — EV-006】【Phase 3 — EV-007】【Phase 3 — EV-008】【Phase 3 — EV-009】【Phase 3 — EV-010】【Phase 9 — Ecosystem Decision Pattern Pola 1】【Phase 9 — Recurring Behavioral Pattern Pola 2】.
Supporting Dataset: Phase 3 History, Phase 7 Ecosystem, Phase 9 Ecosystem Decision Pattern, Phase 9 Recurring Behavioral Pattern
Confidence: HIGH

Principle 5: Bridge-First Liquidity Strategy (Ethereum Before Cosmos IBC) — Prioritaskan Vana-Ethereum bridge untuk token liquidity dan user onboarding; IBC channels ke Cosmos ecosystem secondary【Phase 4 — Core Components Bridge】【Phase 7 — Major Integrations Vana-Ethereum Bridge】【Phase 9 — Ecosystem Decision Pattern Pola 3】【Phase 9 — Recurring Behavioral Pattern Pola 6】.
Evidence: Bridge live mainnet 2024-10-16; CEX listings post-TGE; IBC enabled tapi active channels not documented【Phase 4 — Core Components Bridge】【Phase 7 — Major Integrations Vana-Ethereum Bridge】【Phase 9 — Ecosystem Decision Pattern Pola 3】【Phase 9 — Recurring Behavioral Pattern Pola 6】.
Supporting Dataset: Phase 4 Technology, Phase 7 Ecosystem, Phase 9 Ecosystem Decision Pattern, Phase 9 Recurring Behavioral Pattern
Confidence: HIGH

Principle 6: Community-First Token Distribution via Claim Portal — TGE via claim portal (Vana Portal) ke Data DAO contributors, testnet users, ecosystem contributors bukan public sale/launchpad/auction【Phase 3 — EV-016】【Phase 6 — TGE】【Phase 9 — Financial Decision Pattern Pola 4】【Phase 9 — Decision Timeline Keputusan: TGE VANA 2024-12-16 via claim portal】.
Evidence: Blog Token Launch claim via Portal; TGE community allocation; Financial Decision Pattern Pola 4【Phase 3 — EV-016】【Phase 6 — TGE】【Phase 9 — Financial Decision Pattern Pola 4】.
Supporting Dataset: Phase 3 History, Phase 6 Token, Phase 9 Financial Decision Pattern, Phase 9 Decision Timeline
Confidence: HIGH

Principle 7: Delegated Verification Flexibility per Data DAO — Tidak enforce universal Proof-of-Contribution verification standard di protocol level; setiap Data DAO memilih method sendiri (zkTLS, TEE, API signatures) untuk fit-for-purpose verification【Phase 4 — Known Technical Limitations】【Phase 7 — Ecosystem Risks Data Quality Risk】【Phase 9 — Technical Decision Pattern Pola 3】【Phase 9 — Strategic Trade-offs Trade-off 4】.
Evidence: PoC verification quality bergantung connector implementation per DAO; Technical Decision Pattern Pola 3; Strategic Trade-offs Trade-off 4【Phase 4 — Known Technical Limitations】【Phase 7 — Ecosystem Risks Data Quality Risk】【Phase 9 — Technical Decision Pattern Pola 3】【Phase 9 — Strategic Trade-offs Trade-off 4】.
Supporting Dataset: Phase 4 Technology, Phase 7 Ecosystem Risks, Phase 9 Technical Decision Pattern, Phase 9 Strategic Trade-offs
Confidence: HIGH

Principle 8: Off-Chain Data Storage Delegation ke Data DAO Individual — Protocol tidak provide data availability layer; Data DAO pilih IPFS/Arweave/cloud sendiri untuk protocol simplicity dan DAO sovereignty【Phase 4 — System Architecture Storage】【Phase 4 — Known Technical Limitations】【Phase 7 — Ecosystem Risks Data Provider Dependency】【Phase 9 — Technical Decision Pattern Pola 5】【Phase 9 — Strategic Trade-offs Trade-off 5】.
Evidence: Off-chain data storage per Data DAO design; protocol tidak menjamin persistence; Technical Decision Pattern Pola 5; Strategic Trade-offs Trade-off 5【Phase 4 — System Architecture Storage】【Phase 4 — Known Technical Limitations】【Phase 9 — Technical Decision Pattern Pola 5】【Phase 9 — Strategic Trade-offs Trade-off 5】.
Supporting Dataset: Phase 4 Technology, Phase 7 Ecosystem Risks, Phase 9 Technical Decision Pattern, Phase 9 Strategic Trade-offs
Confidence: HIGH

## Success Factors

Factor 1: Clear Narrative Differentiation — "Data DAO Infrastructure" bukan general data marketplace; 5 vertical DAOs live on mainnet membuktikan product-market fit early【Phase 1 — Category: data liquidity / data DAO infrastructure】【Phase 8 — Narrative Position Data DAO / Data Liquidity Main Narrative】【Phase 8 — Narrative Position Data Sovereignty Main Narrative】【Phase 9 — Behavioral Summary Kekuatan Utama】.
Evidence: Foundation category; Narrative Position Data DAO Main Narrative; Behavioral Summary Kekuatan Utama【Phase 1 — Category】【Phase 8 — Narrative Position Data DAO / Data Liquidity】【Phase 9 — Behavioral Summary Kekuatan Utama】.
Supporting Dataset: Phase 1 Foundation, Phase 8 Market, Phase 9 Behavioral Summary
Confidence: HIGH

Factor 2: Tier-1 Investor Syndicate — Paradigm, Polymorphic Capital, Coinbase Ventures, Polychain Capital, Dragonfly Capital secured early 2023 memberikan capital, network, strategic guidance【Phase 2 — Entities Investors】【Phase 3 — EV-005】【Phase 5 — Funding History】【Phase 9 — Financial Decision Pattern Pola 1】【Phase 9 — Recurring Behavioral Pattern Pola 3】.
Evidence: Messari report konfirmasi 5 tier-1 investors; Funding History Early Funding Round; Financial Decision Pattern Pola 1【Phase 3 — EV-005】【Phase 5 — Funding History】【Phase 9 — Financial Decision Pattern Pola 1】.
Supporting Dataset: Phase 2 Entity, Phase 3 History, Phase 5 Financial, Phase 9 Financial Decision Pattern, Phase 9 Recurring Behavioral Pattern
Confidence: HIGH

Factor 3: Modular Sovereign L1 dengan Custom PoC Module — Technical moat melalui custom application-layer module (Proof-of-Contribution) yang tidak ada di general-purpose L1/L2【Phase 4 — Core Components PoC Module】【Phase 9 — Behavioral Summary Kekuatan Utama】【Phase 9 — Core Insights Insight 1】.
Evidence: Core Components PoC Module custom; Behavioral Summary Kekuatan Utama; Core Insights Insight 1【Phase 4 — Core Components PoC Module】【Phase 9 — Behavioral Summary Kekuatan Utama】【Phase 9 — Core Insights Insight 1】.
Supporting Dataset: Phase 4 Technology, Phase 9 Behavioral Summary, Phase 9 Core Insights
Confidence: HIGH

Factor 4: Universal Connectors SDK Mengurangi Friction New Data DAO — SDK standardization untuk developer membangun connectors dari platform Web2 apapun ke Data DAO【Phase 4 — Core Components Universal Connectors】【Phase 7 — Developer Ecosystem SDK Universal Connectors】【Phase 9 — Ecosystem Decision Pattern Pola 2】.
Evidence: Core Components Universal Connectors; Developer Ecosystem SDK; Ecosystem Decision Pattern Pola 2【Phase 4 — Core Components Universal Connectors】【Phase 7 — Developer Ecosystem SDK Universal Connectors】【Phase 9 — Ecosystem Decision Pattern Pola 2】.
Supporting Dataset: Phase 4 Technology, Phase 7 Ecosystem, Phase 9 Ecosystem Decision Pattern
Confidence: HIGH

Factor 5: Unified Portal UX untuk End-Users — Single dashboard (Vana Portal) untuk data contribution, Data DAO management, staking, reward tracking mengurangi fragmentation UX【Phase 4 — Core Components Vana Portal】【Phase 7 — Applications Vana Portal】【Phase 9 — Ecosystem Decision Pattern Pola 4】.
Evidence: Core Components Vana Portal; Applications Vana Portal; Ecosystem Decision Pattern Pola 4【Phase 4 — Core Components Vana Portal】【Phase 7 — Applications Vana Portal】【Phase 9 — Ecosystem Decision Pattern Pola 4】.
Supporting Dataset: Phase 4 Technology, Phase 7 Ecosystem, Phase 9 Ecosystem Decision Pattern
Confidence: HIGH

Factor 6: Extensive Testnet Validation (15 Bulan) — Moksha testnet Juli 2023 → Mainnet Oktober 2024 dengan 5 Data DAO, validator set, PoC, bridge tested di production-like environment【Phase 3 — EV-004】【Phase 3 — EV-006】through【Phase 3 — EV-010】【Phase 4 — Technical Upgrade History】【Phase 9 — Recurring Behavioral Pattern Pola 1】.
Evidence: Moksha Testnet Launch; 5 Data DAO di testnet; Technical Upgrade History; Recurring Behavioral Pattern Pola 1【Phase 3 — EV-004】【Phase 3 — EV-006】【Phase 3 — EV-007】【Phase 3 — EV-008】【Phase 3 — EV-009】【Phase 3 — EV-010】【Phase 4 — Technical Upgrade History】【Phase 9 — Recurring Behavioral Pattern Pola 1】.
Supporting Dataset: Phase 3 History, Phase 4 Technology, Phase 9 Behavioral Pattern
Confidence: HIGH

## Failure Factors

Factor 1: Zero Public Financial Transparency — Treasury size, token distribution %, vesting schedule, revenue numbers, grant deployments semua tidak diungkapkan konsisten dari foundation → mainnet → TGE【Phase 5 — Treasury】【Phase 5 — Revenue History】【Phase 6 — Distribution】【Phase 6 — Vesting Schedule】【Phase 7 — Developer Ecosystem Grant Program】【Phase 9 — Recurring Behavioral Pattern Pola 5】【Phase 9 — Behavioral Summary Kelemahan Utama】.
Evidence: Phase 5 Treasury "tidak diungkap"; Phase 6 Distribution "persentase tidak diungkap"; Phase 6 Vesting "tidak diketahui"; Phase 7 Grant Program "no public recipient list"; Recurring Behavioral Pattern Pola 5; Behavioral Summary Kelemahan Utama【Phase 5 — Treasury】【Phase 5 — Revenue History】【Phase 6 — Distribution】【Phase 6 — Vesting Schedule】【Phase 7 — Developer Ecosystem Grant Program】【Phase 9 — Recurring Behavioral Pattern Pola 5】【Phase 9 — Behavioral Summary Kelemahan Utama】.
Supporting Dataset: Phase 5 Financial, Phase 6 Token, Phase 7 Ecosystem, Phase 9 Behavioral Pattern, Phase 9 Behavioral Summary
Confidence: HIGH

Factor 2: No Public Security Audits untuk Mainnet Code — Launch mainnet dan TGE tanpa public audit report dari auditor ternama; security researchers tidak bisa verify code safety; insurance protocols unlikely to cover【Phase 4 — Audit History】【Phase 7 — Ecosystem Risks Security Dependency】【Phase 9 — Technical Decision Pattern Pola 7】【Phase 9 — Behavioral Summary Kelemahan Utama】.
Evidence: Audit History "tidak diketahui"; Ecosystem Risks Security Dependency; Technical Decision Pattern Pola 7; Behavioral Summary Kelemahan Utama【Phase 4 — Audit History】【Phase 7 — Ecosystem Risks Security Dependency】【Phase 9 — Technical Decision Pattern Pola 7】【Phase 9 — Behavioral Summary Kelemahan Utama】.
Supporting Dataset: Phase 4 Technology, Phase 7 Ecosystem Risks, Phase 9 Technical Decision Pattern, Phase 9 Behavioral Summary
Confidence: HIGH

Factor 3: Bridge Trust Model = Honest Majority Validators — Single point of failure untuk cross-chain asset; bukan trust-minimized light-client bridge; bridge compromise = asset loss di kedua chain【Phase 4 — Known Technical Limitations】【Phase 7 — Ecosystem Risks Bridge Dependency】【Phase 9 — Strategic Trade-offs Trade-off 2】【Phase 9 — Behavioral Summary Kelemahan Utama】.
Evidence: Known Technical Limitations bridge trust model; Ecosystem Risks Bridge Dependency; Strategic Trade-offs Trade-off 2; Behavioral Summary Kelemahan Utama【Phase 4 — Known Technical Limitations】【Phase 7 — Ecosystem Risks Bridge Dependency】【Phase 9 — Strategic Trade-offs Trade-off 2】【Phase 9 — Behavioral Summary Kelemahan Utama】.
Supporting Dataset: Phase 4 Technology, Phase 7 Ecosystem Risks, Phase 9 Strategic Trade-offs, Phase 9 Behavioral Summary
Confidence: HIGH

Factor 4: Upstream Dependency pada Cosmos/Ethermint Tanpa Deep Customization — Breaking changes atau vulnerability upstream mempengaruhi Vana langsung; limited differentiation di consensus/execution layer; upgrade coordination complexity【Phase 7 — External Dependencies Cosmos SDK/CometBFT/Ethermint Critical】【Phase 7 — Ecosystem Risks SDK/Protocol Dependency】【Phase 9 — Strategic Trade-offs Trade-off 3】【Phase 9 — Risk Response Pattern Pola 5】.
Evidence: External Dependencies Critical status; Ecosystem Risks SDK/Protocol Dependency; Strategic Trade-offs Trade-off 3; Risk Response Pattern Pola 5【Phase 7 — External Dependencies】【Phase 7 — Ecosystem Risks SDK/Protocol Dependency】【Phase 9 — Strategic Trade-offs Trade-off 3】【Phase 9 — Risk Response Pattern Pola 5】.
Supporting Dataset: Phase 7 Ecosystem, Phase 9 Strategic Trade-offs, Phase 9 Risk Response Pattern
Confidence: HIGH

Factor 5: Data DAO Verification Quality Fragmented — Tidak ada universal Proof-of-Contribution verification standard enforced at protocol level; verification quality bervariasi across DAOs; buyer trust bergantung per DAO reputation【Phase 4 — Known Technical Limitations】【Phase 7 — Ecosystem Risks Data Quality Risk】【Phase 9 — Strategic Trade-offs Trade-off 4】【Phase 9 — Risk Response Pattern Pola 3】.
Evidence: Known Technical Limitations PoC verification; Ecosystem Risks Data Quality Risk; Strategic Trade-offs Trade-off 4; Risk Response Pattern Pola 3【Phase 4 — Known Technical Limitations】【Phase 7 — Ecosystem Risks Data Quality Risk】【Phase 9 — Strategic Trade-offs Trade-off 4】【Phase 9 — Risk Response Pattern Pola 3】.
Supporting Dataset: Phase 4 Technology, Phase 7 Ecosystem Risks, Phase 9 Strategic Trade-offs, Phase 9 Risk Response Pattern
Confidence: HIGH

Factor 6: Regulatory Uncertainty Unmitigated Publicly — Whitepaper mengakui ketidakpastian regulasi Data DAO tapi tidak mempublikasikan legal opinions, jurisdictional analysis, atau compliance framework【Phase 1 — Open Threads Regulatory status】【Phase 3 — Open Threads Regulatory status】【Phase 7 — Ecosystem Risks Regulation Dependency】【Phase 9 — Risk Response Pattern Pola 4】【Phase 9 — Behavioral Summary Kelemahan Utama】.
Evidence: Phase 1 Open Threads; Phase 3 Open Threads; Ecosystem Risks Regulation Dependency; Risk Response Pattern Pola 4; Behavioral Summary Kelemahan Utama【Phase 1 — Open Threads】【Phase 3 — Open Threads】【Phase 7 — Ecosystem Risks Regulation Dependency】【Phase 9 — Risk Response Pattern Pola 4】【Phase 9 — Behavioral Summary Kelemahan Utama】.
Supporting Dataset: Phase 1 Foundation, Phase 3 History, Phase 7 Ecosystem Risks, Phase 9 Risk Response Pattern, Phase 9 Behavioral Summary
Confidence: HIGH

Factor 7: Grant Program Vaporware — Referenced in whitepaper tapi tidak ada public application process, recipient list, atau deployment metrics per cutoff【Phase 5 — Fundraising Mechanism Grant】【Phase 7 — Developer Ecosystem Grant Program】【Phase 7 — Official Ecosystem Resources Grant Program】【Phase 9 — Ecosystem Decision Pattern Pola 5】【Phase 9 — Behavioral Summary Kelemahan Utama】.
Evidence: Fundraising Mechanism Grant "referenced in whitepaper"; Developer Ecosystem Grant Program "Planned / Referenced"; Official Ecosystem Resources "no live page confirmed"; Ecosystem Decision Pattern Pola 5; Behavioral Summary Kelemahan Utama【Phase 5 — Fundraising Mechanism Grant】【Phase 7 — Developer Ecosystem Grant Program】【Phase 7 — Official Ecosystem Resources Grant Program】【Phase 9 — Ecosystem Decision Pattern Pola 5】【Phase 9 — Behavioral Summary Kelemahan Utama】.
Supporting Dataset: Phase 5 Financial, Phase 7 Ecosystem, Phase 9 Ecosystem Decision Pattern, Phase 9 Behavioral Summary
Confidence: HIGH

Factor 8: IBC Ecosystem Integration Minimal — Enabled on mainnet tapi active channels dan relayer operators tidak documented publik; cross-chain volume tidak tracked【Phase 4 — System Architecture Cross-chain Messaging】【Phase 7 — Major Integrations IBC Channels】【Phase 7 — Ecosystem Risks IBC Relayer Infrastructure Dependency】【Phase 9 — Open Threads Active IBC channels】.
Evidence: System Architecture IBC enabled; Major Integrations IBC "active channels not publicly documented"; Ecosystem Risks IBC Relayer Infrastructure Dependency; Open Threads Active IBC channels【Phase 4 — System Architecture Cross-chain Messaging】【Phase 7 — Major Integrations IBC Channels】【Phase 7 — Ecosystem Risks IBC Relayer Infrastructure Dependency】【Phase 9 — Open Threads】.
Supporting Dataset: Phase 4 Technology, Phase 7 Ecosystem, Phase 9 Open Threads
Confidence: MEDIUM

## Decision Framework

Step 1: Observe — Identifikasi problem space: user data trapped di platform Web2 tanpa ownership/monetization; existing solutions (Ocean, Streamr, Ceramic, Filecoin) tidak purpose-built untuk Data DAO collective ownership【Phase 1 — Vision/Mission/Category】【Phase 8 — Competitor Landscape】【Phase 9 — Strategic Objectives Objective 2】.
Evidence: Foundation vision data liquidity layer; Competitor Landscape perbedaan; Strategic Objectives Objective 2 mengembalikan kedaulatan data【Phase 1 — Vision/Mission/Category】【Phase 8 — Competitor Landscape】【Phase 9 — Strategic Objectives Objective 2】.
Supporting Dataset: Phase 1 Foundation, Phase 8 Market, Phase 9 Strategic Objectives
Confidence: HIGH

Step 2: Evaluate — Technical architecture evaluation: sovereign L1 vs L2 vs existing chain; Cosmos SDK stack chosen untuk modular separation, IBC native, custom modules capability【Phase 4 — System Architecture】【Phase 9 — Technical Decision Pattern Pola 1】【Phase 9 — Strategic Trade-offs Trade-off 1】.
Evidence: System Architecture Layer 1 Cosmos SDK; Technical Decision Pattern Pola 1; Strategic Trade-offs Trade-off 1【Phase 4 — System Architecture】【Phase 9 — Technical Decision Pattern Pola 1】【Phase 9 — Strategic Trade-offs Trade-off 1】.
Supporting Dataset: Phase 4 Technology, Phase 9 Technical Decision Pattern, Phase 9 Strategic Trade-offs
Confidence: HIGH

Step 3: Fund — Secure strategic VC round dengan tier-1 investors (Paradigm, Polymorphic, Coinbase Ventures, Polychain, Dragonfly) 2023 untuk runway panjang sebelum mainnet/TGE【Phase 3 — EV-005】【Phase 5 — Funding History Early Funding Round】【Phase 9 — Financial Decision Pattern Pola 1】【Phase 9 — Recurring Behavioral Pattern Pola 3】.
Evidence: EV-005 Early Funding Round; Funding History 2023 round; Financial Decision Pattern Pola 1; Recurring Behavioral Pattern Pola 3【Phase 3 — EV-005】【Phase 5 — Funding History】【Phase 9 — Financial Decision Pattern Pola 1】【Phase 9 — Recurring Behavioral Pattern Pola 3】.
Supporting Dataset: Phase 3 History, Phase 5 Financial, Phase 9 Financial Decision Pattern, Phase 9 Recurring Behavioral Pattern
Confidence: HIGH

Step 4: Develop — Build infrastructure: Cosmos SDK chain + Ethermint EVM + CometBFT consensus + custom modules (PoC, Bridge, IBC) + Universal Connectors SDK + 5 vertical Data DAOs di testnet 15 bulan【Phase 3 — EV-003】【Phase 3 — EV-004】【Phase 3 — EV-006】through【Phase 3 — EV-012】【Phase 4 — Technical Upgrade History Moksha Testnet Launch】【Phase 9 — Recurring Behavioral Pattern Pola 1】.
Evidence: EV-003 Whitepaper; EV-004 Moksha Testnet; EV-006 to EV-010 Data DAOs; EV-011 Universal Connectors; EV-012 PoC; Technical Upgrade History; Recurring Behavioral Pattern Pola 1【Phase 3 — EV-003】【Phase 3 — EV-004】【Phase 3 — EV-006】【Phase 3 — EV-007】【Phase 3 — EV-008】【Phase 3 — EV-009】【Phase 3 — EV-010】【Phase 3 — EV-011】【Phase 3 — EV-012】【Phase 4 — Technical Upgrade History】【Phase 9 — Recurring Behavioral Pattern Pola 1】.
Supporting Dataset: Phase 3 History, Phase 4 Technology, Phase 9 Behavioral Pattern
Confidence: HIGH

Step 5: Launch — Decoupled launch: Mainnet genesis 2024-10-16 (chain live, staking, DAOs, bridge) → TGE 2024-12-16 (token transferable, trading, expanded governance) via claim portal【Phase 3 — EV-013】【Phase 3 — EV-016】【Phase 9 — Decision Timeline Keputusan: Mainnet tanpa TGE】【Phase 9 — Decision Timeline Keputusan: TGE via claim portal】【Phase 9 — Recurring Behavioral Pattern Pola 4】.
Evidence: EV-013 Mainnet Genesis; EV-016 TGE; Decision Timeline Mainnet tanpa TGE; Decision Timeline TGE claim portal; Recurring Behavioral Pattern Pola 4【Phase 3 — EV-013】【Phase 3 — EV-016】【Phase 9 — Decision Timeline】【Phase 9 — Recurring Behavioral Pattern Pola 4】.
Supporting Dataset: Phase 3 History, Phase 9 Decision Timeline, Phase 9 Recurring Behavioral Pattern
Confidence: HIGH

Step 6: Govern — Dual governance: Foundation (legal wrapper, treasury, strategic) + On-chain token-weighted voting (Cosmos SDK module) untuk parameter changes, upgrades; Data DAO governance terpisah per DAO【Phase 2 — Entity Vana Foundation】【Phase 4 — Consensus Mechanism】【Phase 6 — Governance】【Phase 7 — Governance Ecosystem】【Phase 9 — Governance Decision Pattern Pola 1】【Phase 9 — Governance Decision Pattern Pola 4】.
Evidence: Entity Vana Foundation; Consensus Mechanism governance module; Governance token-weighted voting; Governance Ecosystem Foundation + DAOs; Governance Decision Pattern Pola 1; Governance Decision Pattern Pola 4【Phase 2 — Entity Vana Foundation】【Phase 4 — Consensus Mechanism】【Phase 6 — Governance】【Phase 7 — Governance Ecosystem】【Phase 9 — Governance Decision Pattern Pola 1】【Phase 9 — Governance Decision Pattern Pola 4】.
Supporting Dataset: Phase 2 Entity, Phase 4 Technology, Phase 6 Token, Phase 7 Ecosystem, Phase 9 Governance Decision Pattern
Confidence: HIGH

## Reusable Playbook

Playbook 1: Sovereign App-Chain untuk Vertical-Specific Use Case — Gunakan Cosmos SDK + CometBFT + Ethermint stack untuk build sovereign L1 dengan custom application-layer modules (bukan consensus modifications) ketika butuh: full control governance parameters, custom business logic modules, IBC native, EVM compatibility untuk existing tooling【Phase 4 — System Architecture】【Phase 4 — Core Components】【Phase 9 — Technical Decision Pattern Pola 1】【Phase 9 — Technical Decision Pattern Pola 2】【Phase 9 — Technical Decision Pattern Pola 3】.
Evidence: System Architecture modular separation; Core Components custom modules PoC/Bridge/IBC; Technical Decision Pattern Pola 1, 2, 3【Phase 4 — System Architecture】【Phase 4 — Core Components】【Phase 9 — Technical Decision Pattern Pola 1】【Phase 9 — Technical Decision Pattern Pola 2】【Phase 9 — Technical Decision Pattern Pola 3】.
Supporting Dataset: Phase 4 Technology, Phase 9 Technical Decision Pattern
Confidence: HIGH

Playbook 2: Testnet-First dengan Real Economic Actors — Jalankan public testnet minimal 12-15 bulan dengan real users, real validators, real application operators (Data DAOs) sebelum mainnet; testnet harus mirror mainnet economics (staking, rewards, bridge, governance)【Phase 3 — EV-004】【Phase 3 — EV-006】through【Phase 3 — EV-010】【Phase 4 — Technical Upgrade History】【Phase 9 — Recurring Behavioral Pattern Pola 1】.
Evidence: Moksha testnet 15 bulan dengan 5 Data DAO live, validator set, PoC, bridge testing; Technical Upgrade History; Recurring Behavioral Pattern Pola 1【Phase 3 — EV-004】【Phase 3 — EV-006】【Phase 3 — EV-007】【Phase 3 — EV-008】【Phase 3 — EV-009】【Phase 3 — EV-010】【Phase 4 — Technical Upgrade History】【Phase 9 — Recurring Behavioral Pattern Pola 1】.
Supporting Dataset: Phase 3 History, Phase 4 Technology, Phase 9 Behavioral Pattern
Confidence: HIGH

Playbook 3: Parallel Vertical Launch untuk Platform Demonstration — Launch 3-5 vertical applications bersamaan di testnet/mainnet untuk demonstrate platform versatility dan attract diverse developer communities, bukan sequential single-vertical focus【Phase 3 — EV-006】through【Phase 3 — EV-010】【Phase 9 — Ecosystem Decision Pattern Pola 1】【Phase 9 — Recurring Behavioral Pattern Pola 2】.
Evidence: 5 Data DAO verticals (social, dating, DeFi, gaming) launched parallel 2023 testnet; Ecosystem Decision Pattern Pola 1; Recurring Behavioral Pattern Pola 2【Phase 3 — EV-006】【Phase 3 — EV-007】【Phase 3 — EV-008】【Phase 3 — EV-009】【Phase 3 — EV-010】【Phase 9 — Ecosystem Decision Pattern Pola 1】【Phase 9 — Recurring Behavioral Pattern Pola 2】.
Supporting Dataset: Phase 3 History, Phase 9 Ecosystem Decision Pattern, Phase 9 Recurring Behavioral Pattern
Confidence: HIGH

Playbook 4: Universal SDK Standardization untuk Ecosystem Onboarding — Bangun SDK universal (multi-language: TypeScript/Python) untuk third-party developers membangun integrations ke platform, mengurangi friction dan memastikan consistent patterns【Phase 4 — Core Components Universal Connectors】【Phase 7 — Developer Ecosystem SDK Universal Connectors】【Phase 9 — Ecosystem Decision Pattern Pola 2】.
Evidence: Universal Connectors SDK TypeScript/Python; Developer Ecosystem SDK; Ecosystem Decision Pattern Pola 2【Phase 4 — Core Components Universal Connectors】【Phase 7 — Developer Ecosystem SDK Universal Connectors】【Phase 9 — Ecosystem Decision Pattern Pola 2】.
Supporting Dataset: Phase 4 Technology, Phase 7 Ecosystem, Phase 9 Ecosystem Decision Pattern
Confidence: HIGH

Playbook 5: Bridge-First Liquidity Strategy — Prioritaskan bridge ke largest liquidity source (Ethereum) untuk token launch dan user onboarding sebelum cross-chain ke ecosystem lain (IBC/Cosmos); deploy validator-set attestation bridge untuk speed, plan upgrade path ke trust-minimized model【Phase 4 — Core Components Bridge】【Phase 7 — Major Integrations Vana-Ethereum Bridge】【Phase 9 — Ecosystem Decision Pattern Pola 3】【Phase 9 — Recurring Behavioral Pattern Pola 6】【Phase 9 — Strategic Trade-offs Trade-off 2】.
Evidence: Bridge live mainnet genesis; CEX listings post-TGE; IBC secondary; Ecosystem Decision Pattern Pola 3; Recurring Behavioral Pattern Pola 6; Strategic Trade-offs Trade-off 2【Phase 4 — Core Components Bridge】【Phase 7 — Major Integrations Vana-Ethereum Bridge】【Phase 9 — Ecosystem Decision Pattern Pola 3】【Phase 9 — Recurring Behavioral Pattern Pola 6】【Phase 9 — Strategic Trade-offs Trade-off 2】.
Supporting Dataset: Phase 4 Technology, Phase 7 Ecosystem, Phase 9 Ecosystem Decision Pattern, Phase 9 Recurring Behavioral Pattern, Phase 9 Strategic Trade-offs
Confidence: HIGH

Playbook 6: Decouple Chain Launch dari Token Launch — Launch mainnet dengan native gas/staking token first (validators earning, apps operating) → TGE terpisah untuk token transferable/trading; gap 1-3 bulan untuk compliance prep, claim infrastructure, exchange coordination【Phase 3 — EV-013】【Phase 3 — EV-016】【Phase 9 — Decision Timeline Keputusan: Mainnet tanpa TGE】【Phase 9 — Decision Timeline Keputusan: TGE via claim portal】【Phase 9 — Recurring Behavioral Pattern Pola 4】.
Evidence: EV-013 Mainnet Genesis; EV-016 TGE; Decision Timeline Mainnet tanpa TGE; Decision Timeline TGE claim portal; Recurring Behavioral Pattern Pola 4【Phase 3 — EV-013】【Phase 3 — EV-016】【Phase 9 — Decision Timeline】【Phase 9 — Recurring Behavioral Pattern Pola 4】.
Supporting Dataset: Phase 3 History, Phase 9 Decision Timeline, Phase 9 Recurring Behavioral Pattern
Confidence: HIGH

Playbook 7: Community-First Token Distribution via Claim Portal — Distribusi TGE melalui claim portal ke verified contributors (testnet users, app users, ecosystem participants) bukan public sale/launchpad; fair launch narrative, no fixed-price sale, regulatory caution【Phase 3 — EV-016】【Phase 6 — TGE】【Phase 9 — Financial Decision Pattern Pola 4】【Phase 9 — Decision Timeline Keputusan: TGE via claim portal】.
Evidence: EV-016 TGE claim via Portal; TGE community allocation; Financial Decision Pattern Pola 4; Decision Timeline TGE claim portal【Phase 3 — EV-016】【Phase 6 — TGE】【Phase 9 — Financial Decision Pattern Pola 4】【Phase 9 — Decision Timeline】.
Supporting Dataset: Phase 3 History, Phase 6 Token, Phase 9 Financial Decision Pattern, Phase 9 Decision Timeline
Confidence: HIGH

Playbook 8: Dual Governance Structure — Foundation (legal entity, jurisdiction) untuk treasury management, strategic direction, legal compliance + On-chain token-weighted voting (Cosmos SDK governance module) untuk protocol parameter changes, upgrades; separation of concerns【Phase 2 — Entity Vana Foundation】【Phase 4 — Consensus Mechanism】【Phase 6 — Governance】【Phase 7 — Governance Ecosystem】【Phase 9 — Governance Decision Pattern Pola 1】.
Evidence: Entity Vana Foundation; Consensus Mechanism governance module; Governance token-weighted voting; Governance Ecosystem Foundation; Governance Decision Pattern Pola 1【Phase 2 — Entity Vana Foundation】【Phase 4 — Consensus Mechanism】【Phase 6 — Governance】【Phase 7 — Governance Ecosystem】【Phase 9 — Governance Decision Pattern Pola 1】.
Supporting Dataset: Phase 2 Entity, Phase 4 Technology, Phase 6 Token, Phase 7 Ecosystem, Phase 9 Governance Decision Pattern
Confidence: HIGH

## Anti-patterns

Anti-pattern 1: Zero Public Financial Transparency Post-TGE — Tidak mengungkap treasury size, token distribution %, vesting schedule, revenue, grant deployments menciptakan trust deficit, institutional adoption barrier, cannot verify alignment【Phase 5 — Treasury】【Phase 5 — Revenue History】【Phase 6 — Distribution】【Phase 6 — Vesting Schedule】【Phase 7 — Developer Ecosystem Grant Program】【Phase 9 — Recurring Behavioral Pattern Pola 5】【Phase 9 — Behavioral Summary Kelemahan Utama】.
Evidence: Treasury "tidak diungkap"; Distribution "persentase tidak diungkap"; Vesting "tidak diketahui"; Revenue History "Tidak diungkap"; Grant Program "no public recipient list"; Recurring Behavioral Pattern Pola 5; Behavioral Summary Kelemahan Utama【Phase 5 — Treasury】【Phase 5 — Revenue History】【Phase 6 — Distribution】【Phase 6 — Vesting Schedule】【Phase 7 — Developer Ecosystem Grant Program】【Phase 9 — Recurring Behavioral Pattern Pola 5】【Phase 9 — Behavioral Summary Kelemahan Utama】.
Supporting Dataset: Phase 5 Financial, Phase 6 Token, Phase 7 Ecosystem, Phase 9 Behavioral Pattern, Phase 9 Behavioral Summary
Confidence: HIGH

Anti-pattern 2: Launch Mainnet dengan Value at Risk Tanpa Public Security Audit — Mengandalkan internal review dan testnet battle-testing saja; security researchers tidak bisa verify; insurance exclusion; exploit risk unquantified【Phase 4 — Audit History】【Phase 7 — Ecosystem Risks Security Dependency】【Phase 9 — Technical Decision Pattern Pola 7】【Phase 9 — Behavioral Summary Kelemahan Utama】.
Evidence: Audit History "tidak diketahui"; Ecosystem Risks Security Dependency; Technical Decision Pattern Pola 7; Behavioral Summary Kelemahan Utama【Phase 4 — Audit History】【Phase 7 — Ecosystem Risks Security Dependency】【Phase 9 — Technical Decision Pattern Pola 7】【Phase 9 — Behavioral Summary Kelemahan Utama】.
Supporting Dataset: Phase 4 Technology, Phase 7 Ecosystem Risks, Phase 9 Technical Decision Pattern, Phase 9 Behavioral Summary
Confidence: HIGH

Anti-pattern 3: Single Bridge Dependency dengan Honest Majority Trust Model — Semua cross-chain asset transfer bergantung single bridge contract set dengan validator set attestation; bukan trust-minimized; bridge compromise = asset loss di kedua chain【Phase 4 — Known Technical Limitations】【Phase 7 — Ecosystem Risks Bridge Dependency】【Phase 9 — Strategic Trade-offs Trade-off 2】【Phase 9 — Behavioral Summary Kelemahan Utama】.
Evidence: Known Technical Limitations bridge trust model; Ecosystem Risks Bridge Dependency; Strategic Trade-offs Trade-off 2; Behavioral Summary Kelemahan Utama【Phase 4 — Known Technical Limitations】【Phase 7 — Ecosystem Risks Bridge Dependency】【Phase 9 — Strategic Trade-offs Trade-off 2】【Phase 9 — Behavioral Summary Kelemahan Utama】.
Supporting Dataset: Phase 4 Technology, Phase 7 Ecosystem Risks, Phase 9 Strategic Trade-offs, Phase 9 Behavioral Summary
Confidence: HIGH

Anti-pattern 4: Upstream Dependency Tanpa Fork Customization Mendalam — Mengandalkan Cosmos SDK, CometBFT, Ethermint upstream tanpa deep forks; breaking changes upstream langsung mempengaruhi chain; limited differentiation di consensus/execution layer【Phase 7 — External Dependencies Critical】【Phase 7 — Ecosystem Risks SDK/Protocol Dependency】【Phase 9 — Strategic Trade-offs Trade-off 3】【Phase 9 — Risk Response Pattern Pola 5】.
Evidence: External Dependencies Critical; Ecosystem Risks SDK/Protocol Dependency; Strategic Trade-offs Trade-off 3; Risk Response Pattern Pola 5【Phase 7 — External Dependencies】【Phase 7 — Ecosystem Risks SDK/Protocol Dependency】【Phase 9 — Strategic Trade-offs Trade-off 3】【Phase 9 — Risk Response Pattern Pola 5】.
Supporting Dataset: Phase 7 Ecosystem, Phase 9 Strategic Trade-offs, Phase 9 Risk Response Pattern
Confidence: HIGH

Anti-pattern 5: Delegated Quality Standard Tanpa Protocol-Level Enforcement — Proof-of-Contribution verification quality bergantung per Data DAO implementation; tidak ada universal standard enforced; buyer trust fragmented; fraudulent submission risk per DAO【Phase 4 — Known Technical Limitations】【Phase 7 — Ecosystem Risks Data Quality Risk】【Phase 9 — Strategic Trade-offs Trade-off 4】【Phase 9 — Risk Response Pattern Pola 3】.
Evidence: Known Technical Limitations PoC verification; Ecosystem Risks Data Quality Risk; Strategic Trade-offs Trade-off 4; Risk Response Pattern Pola 3【Phase 4 — Known Technical Limitations】【Phase 7 — Ecosystem Risks Data Quality Risk】【Phase 9 — Strategic Trade-offs Trade-off 4】【Phase 9 — Risk Response Pattern Pola 3】.
Supporting Dataset: Phase 4 Technology, Phase 7 Ecosystem Risks, Phase 9 Strategic Trade-offs, Phase 9 Risk Response Pattern
Confidence: HIGH

Anti-pattern 6: Grant Program Announced But Not Deployed — Whitepaper references ecosystem grants tapi tidak ada public application process, recipient list, amounts, atau deployment metrics setelah mainnet/TGE【Phase 5 — Fundraising Mechanism Grant】【Phase 7 — Developer Ecosystem Grant Program】【Phase 7 — Official Ecosystem Resources Grant Program】【Phase 9 — Ecosystem Decision Pattern Pola 5】【Phase 9 — Behavioral Summary Kelemahan Utama】.
Evidence: Fundraising Mechanism Grant "referenced in whitepaper"; Developer Ecosystem Grant Program "Planned / Referenced"; Official Ecosystem Resources "no live page confirmed"; Ecosystem Decision Pattern Pola 5; Behavioral Summary Kelemahan Utama【Phase 5 — Fundraising Mechanism Grant】【Phase 7 — Developer Ecosystem Grant Program】【Phase 7 — Official Ecosystem Resources Grant Program】【Phase 9 — Ecosystem Decision Pattern Pola 5】【Phase 9 — Behavioral Summary Kelemahan Utama】.
Supporting Dataset: Phase 5 Financial, Phase 7 Ecosystem, Phase 9 Ecosystem Decision Pattern, Phase 9 Behavioral Summary
Confidence: HIGH

Anti-pattern 7: Regulatory Uncertainty Acknowledged But Not Actively Mitigated — Whitepaper mentions regulatory risk tapi tidak publish legal opinions, jurisdictional analysis, compliance framework, atau engagement status【Phase 1 — Open Threads Regulatory status】【Phase 3 — Open Threads Regulatory status】【Phase 7 — Ecosystem Risks Regulation Dependency】【Phase 9 — Risk Response Pattern Pola 4】【Phase 9 — Behavioral Summary Kelemahan Utama】.
Evidence: Phase 1 Open Threads; Phase 3 Open Threads; Ecosystem Risks Regulation Dependency; Risk Response Pattern Pola 4; Behavioral Summary Kelemahan Utama【Phase 1 — Open Threads】【Phase 3 — Open Threads】【Phase 7 — Ecosystem Risks Regulation Dependency】【Phase 9 — Risk Response Pattern Pola 4】【Phase 9 — Behavioral Summary Kelemahan Utama】.
Supporting Dataset: Phase 1 Foundation, Phase 3 History, Phase 7 Ecosystem Risks, Phase 9 Risk Response Pattern, Phase 9 Behavioral Summary
Confidence: HIGH

Anti-pattern 8: Validator Set Economics Opaque — Total staked VANA, inflation rate aktual, real yield, nakamoto coefficient, stake distribution, geographic distribution tidak terpublikasi dalam dashboard terpusat; explorer hanya raw data【Phase 4 — Known Technical Limitations Validator set size】【Phase 7 — Ecosystem Risks】【Phase 9 — Open Threads Validator set composition】.
Evidence: Known Technical Limitations validator set size; Open Threads Validator set composition【Phase 4 — Known Technical Limitations】【Phase 9 — Open Threads】.
Supporting Dataset: Phase 4 Technology, Phase 9 Open Threads
Confidence: MEDIUM

## Lessons Learned

1. Purpose-built sovereign L1 dengan custom application-layer modules menciptakan stronger technical differentiation daripada general-purpose L1/L2, tetapi memerlukan higher operational burden (validator set, security budget, bridge maintenance).

2. Extensive testnet period (12-15 bulan) dengan real economic actors (validators, app operators, users) secara signifikan mengurangi mainnet launch risk dan memvalidasi economics sebelum value at risk.

3. Parallel vertical application launch mendemonstrasikan platform versatility dan menarik diverse developer communities, tetapi memerlukan standardization layer (SDK) untuk mencegah fragmentation.

4. Decoupling chain launch dari token launch (1-3 bulan gap) memungkinkan chain stabilization, validator economics validation, dan compliance preparation sebelum public token liquidity.

5. Bridge-first strategy ke Ethereum (largest liquidity) sebelum IBC/Cosmos ecosystem adalah pragmatic untuk token launch, tetapi menciptakan single point of failure yang memerlukan upgrade path ke trust-minimized model.

6. Zero public financial transparency post-TGE adalah major barrier untuk institutional adoption, insurance coverage, dan community trust — transparency dashboard seharusnya priority post-launch.

7. No public security audit sebelum mainnet launch dengan value at risk adalah unacceptable untuk institutional-grade infrastructure; audit seharusnya prerequisite bukan afterthought.

8. Dual governance structure (Foundation legal wrapper + on-chain token voting) bekerja untuk regulatory compliance dan protocol upgrades, tetapi community pool/treasury parameters harus transparent dari day 1.

9. Grant program announced in whitepaper tapi tidak deployed setelah mainnet/TGE menciptakan credibility gap — program seharusnya live dengan first cohort sebelum atau bersamaan mainnet.

10. Regulatory uncertainty untuk novel models (Data DAO) memerlukan proactive legal opinions, jurisdictional analysis, dan compliance framework publication, bukan hanya acknowledgment di whitepaper.

## Knowledge Summary

Strategic Principles:
- Modular App-Chain Architecture First (Cosmos SDK + CometBFT + Ethermint + custom modules)
- EVM Compatibility via Ethermint untuk existing tooling leverage
- Testnet-First dengan Real Users/Data DAOs (15 bulan validation)
- Parallel Vertical Data DAO Expansion untuk platform demonstration
- Bridge-First Liquidity Strategy (Ethereum before IBC)
- Community-First Token Distribution via Claim Portal (fair launch)
- Delegated Verification Flexibility per Data DAO (no universal standard enforced)
- Off-Chain Data Storage Delegation ke DAO Individual (protocol simplicity)

Success Factors:
- Clear Narrative Differentiation: Data DAO Infrastructure (bukan general data marketplace)
- Tier-1 Investor Syndicate: 5 major VCs secured early 2023
- Modular Sovereign L1 dengan Custom PoC Module (technical moat)
- Universal Connectors SDK mengurangi friction new Data DAO onboarding
- Unified Portal UX untuk end-users (single dashboard)
- Extensive Testnet Validation (15 bulan dengan real economic actors)

Failure Factors:
- Zero Public Financial Transparency (treasury, distribution, vesting, revenue, grants)
- No Public Security Audits untuk mainnet code handling value
- Single Bridge Dependency dengan Honest Majority Trust Model
- Upstream Dependency pada Cosmos/Ethermint tanpa deep customization
- Data DAO Verification Quality Fragmented (no protocol-level standard)
- Regulatory Uncertainty Unmitigated Publicly
- Grant Program Vaporware (announced not deployed)
- IBC Ecosystem Integration Minimal (enabled not documented)
- Validator Set Economics Opaque (no staking dashboard)

Decision Framework:
Observe (user data trapped Web2) → Evaluate (sovereign L1 vs L2, Cosmos SDK chosen) → Fund (tier-1 VC round 2023) → Develop (chain + 5 DAOs + SDK + 15 bulan testnet) → Launch (Mainnet genesis Oct 2024 → TGE Dec 2024 decoupled) → Govern (Dual: Foundation legal + on-chain token voting + DAO-level governance)

Reusable Playbook:
1. Sovereign App-Chain untuk Vertical-Specific Use Case (Cosmos SDK stack + custom app modules)
2. Testnet-First dengan Real Economic Actors (12-15 bulan mirror mainnet economics)
3. Parallel Vertical Launch untuk Platform Demonstration (3-5 verticals bersamaan)
4. Universal SDK Standardization untuk Ecosystem Onboarding (multi-language SDK)
5. Bridge-First Liquidity Strategy (Ethereum bridge first, plan trust-minimized upgrade)
6. Decouple Chain Launch dari Token Launch (1-3 bulan gap untuk compliance)
7. Community-First Token Distribution via Claim Portal (verified contributors, fair launch)
8. Dual Governance Structure (Foundation legal + on-chain token voting)

Anti-patterns:
1. Zero Public Financial Transparency Post-TGE
2. Launch Mainnet Value at Risk Tanpa Public Security Audit
3. Single Bridge Dependency Honest Majority Trust Model
4. Upstream Dependency Tanpa Fork Customization Mendalam
5. Delegated Quality Standard Tanpa Protocol-Level Enforcement
6. Grant Program Announced But Not Deployed
7. Regulatory Uncertainty Acknowledged But Not Actively Mitigated
8. Validator Set Economics Opaque

## Open Questions
- [foundation] Exact founding entity legal name and registration number in Cayman Islands — not fully public in registry searches
- [foundation] Complete core team headcount and org chart — only partial public disclosure
- [foundation] TGE unlock schedule specifics (vesting cliffs, team/investor allocations) — whitepaper references but full schedule not published in single source
- [foundation] Whether VANA token has fee switch / revenue share mechanism active — whitepaper mentions but governance status unclear
- [foundation] Total treasury size and composition (stable vs VANA) — not disclosed publicly
- [foundation] Exact mainnet genesis block timestamp and validator set at launch — explorer shows but not aggregated in one source
- [foundation] Regulatory status of Data DAOs in various jurisdictions — whitepaper acknowledges uncertainty
- [foundation] Whether Moksha testnet data/state was migrated to mainnet or reset — not explicitly documented
- [entity] Exact founding entity legal name and registration number in Cayman Islands — not fully public in registry searches
- [entity] Complete core team headcount and org chart — only partial public disclosure
- [entity] TGE unlock schedule specifics (vesting cliffs, team/investor allocations) — whitepaper references but full schedule not published in single source
- [entity] Whether VANA token has fee switch / revenue share mechanism active — whitepaper mentions but governance status unclear
- [entity] Total treasury size and composition (stable vs VANA) — not disclosed publicly
- [entity] Exact mainnet genesis block timestamp and validator set at launch — explorer shows but not aggregated in one source
- [entity] Regulatory status of Data DAOs in various jurisdictions — whitepaper acknowledges uncertainty
- [entity] Whether Moksha testnet data/state was migrated to mainnet or reset — not explicitly documented
- [entity] Auditor firms for Vana smart contracts — not publicly announced
- [entity] Market maker / liquidity provider arrangements for VANA token — not disclosed
- [entity] Enterprise partnerships beyond Data DAOs — not publicly documented
- [entity] Grant program recipients and amounts — not aggregated in single source
- [history] Exact founding date (month/day) in 2021 — only year confirmed from Forbes profile and team page
- [history] Precise funding round dates, amounts, and valuations for each investor — Messari report references but single aggregated source
- [history] Whether Moksha testnet state was migrated to mainnet or reset — not explicitly documented in blog posts or docs
- [history] Complete TGE unlock schedule (vesting cliffs, team/investor allocations) — whitepaper mentions but full schedule not published in single verifiable source
- [history] Exact mainnet genesis block timestamp and initial validator set — explorer shows but not aggregated in one source
- [history] VANA token fee switch / revenue share mechanism activation status — whitepaper mentions but governance status unclear
- [history] Total treasury size and composition (stable vs VANA) — not disclosed publicly
- [history] Auditor firms for Vana smart contracts — not publicly announced
- [history] Market maker / liquidity provider arrangements for VANA token — not disclosed
- [history] Enterprise partnerships beyond Data DAOs — not publicly documented
- [history] Grant program recipients and amounts — not aggregated in single source
- [history] Regulatory status of Data DAOs in various jurisdictions — whitepaper acknowledges uncertainty
- [history] Complete core team headcount and org chart — only partial public disclosure
- [history] Exact legal name and registration number of Vana Foundation in Cayman Islands registry — not fully public
- [technology] Audit status: Tidak ada audit publik yang diumumkan; perlu konfirmasi apakah audit privat telah dilakukan oleh trail of bits, CertiK, Halborn, atau auditor lain
- [technology] Bridge security model detail: Threshold signature scheme (TSS) vs multi-sig untuk bridge validator attestation — tidak terdokumentasi detail di whitepaper/docs
- [technology] Validator set composition: Jumlah validator active, stake distribution, nakamoto coefficient — tidak tersedia di explorer dalam format teragregasi
- [technology] IBC active channels: Daftar channel IBC yang live dan relayer operators — tidak dipublikasikan
- [technology] PoC verification methods per Data DAO: r/datadao menggunakan zkTLS? Volara menggunakan API signatures? — tidak distandarisasi di docs
- [technology] Data availability guarantee untuk off-chain Data DAO data: Apakah Vana menyediakan DA layer (Celestia, EigenDA, Avail) atau biarkan per Data DAO — tidak eksplisit di whitepaper
- [technology] Emergency upgrade / halt mechanism: Apakah ada circuit breaker atau emergency patch path — tidak terdokumentasi
- [technology] EVM version compatibility: Exact EVM fork version (Shanghai? Cancun?) — tidak disebutkan di docs
- [technology] Historical testnet data migration: Apakah Moksha testnet state (Data DAO contributions, PoC scores) dimigrasi ke mainnet atau reset — tidak terdokumentasi
- [technology] SDK version pinning: Exact Cosmos SDK, CometBFT, Ethermint versions used in production — tidak di-release notes
- [technology] Monitoring/observability stack: Validator recommended monitoring stack — tidak di docs
- [technology] Grant program technical requirements: Kriteria teknis untuk Data DAO grant recipients — tidak dipublikasikan
- [financial] Exact amount raised in early 2023 VC round (Paradigm, Polymorphic, Coinbase Ventures, Polychain, Dragonfly) — not disclosed in Messari report or blog
- [financial] VANA TGE total funds raised (vs. token distribution) — not separated in public announcements
- [financial] Treasury size, composition (stablecoin vs VANA vs other), and custodian arrangement (multi-sig signers, threshold) — not public
- [financial] Whether protocol fees (Data DAO tx fees, bridge fees, PoC verification fees) are actively collecting revenue on mainnet — whitepaper mentions but no live dashboard
- [financial] Revenue history (monthly/quarterly) for protocol and Foundation — not published
- [financial] Grant program details: total allocated, recipients, amounts, criteria — referenced in whitepaper but no public deployment
- [financial] Audit status and any private audit reports — none announced publicly
- [financial] VANA token fee switch / revenue share mechanism activation — whitepaper mentions but governance status unclear
- [financial] Market maker / liquidity provider arrangements for VANA token — not disclosed
- [financial] Enterprise partnerships revenue (beyond Data DAOs) — not documented
- [financial] Regulatory reserve / legal contingency budget — not disclosed
- [financial] Validator set economics: total staked VANA, inflation rate, real yield — explorer shows live data but not aggregated in financial report
- [financial] Whether Moksha testnet incentives (if any) were paid in VANA or test tokens — not documented
- [token] Total supply, maximum supply, initial supply, circulating supply — tidak diungkap dalam whitepaper, blog resmi, CoinGecko, atau explorer
- [token] Distribusi alokasi token persentase per kategori (Community, Team, Investors, Foundation, Treasury, Ecosystem, Advisors) — whitepaper menyebutkan kategori tanpa angka; Messari report tidak mempublikasikan tabel lengkap
- [token] Vesting schedule detail (cliff, durasi vesting, frekuensi unlock) untuk setiap kategori — tidak dipublikasikan; tidak diverifikasi on-chain
- [token] TGE initial unlock percentage dan kategori mana yang unlocked vs locked — tidak diungkap
- [token] Ethereum ERC-20 contract address lengkap (0x5Af...) — hanya prefix yang terlihat di CoinGecko; alamat lengkap tidak di halaman resmi
- [token] Decimals token (18 assumed tapi tidak eksplisit dikonfirmasi)
- [token] Inflation parameter spesifik (target bonded ratio, yearly inflation rate, blocks per year, reward distribution split) — tidak diungkap
- [token] Burn mechanism apakah ada (EIP-1559 base fee burn di EVM layer, atau protocol-level burn) — tidak dikonfirmasi
- [token] Buyback program atau supply reduction mechanism — tidak diungkap
- [token] Holder distribution breakdown (Foundation, Investor, Treasury, Community, Whale concentration) — tidak ada transparency report
- [token] Apakah VANA digunakan sebagai collateral di DeFi protocols di Vana L1 — tidak disebutkan whitepaper
- [token] Bridge fee structure dan apakah denominated in VANA — tidak dikonfirmasi live
- [token] Data DAO reward token: apakah semua Data DAO menggunakan VANA atau ada Data DAO native token terpisah — tidak distandarisasi di docs
- [token] Community pool / protocol treasury on-chain governance control — parameter governance tidak dipublikasikan
- [token] Validator set economics: total VANA staked, inflation rate aktual, real yield — explorer menampilkan data raw tapi tidak teragregasi
- [token] Apakah Moksha testnet token memiliki konversi ke mainnet VANA atau reset sepenuhnya — tidak terdokumentasi
- [token] Market maker / liquidity provider arrangement untuk VANA token — tidak diungkap
- [token] Audit status token contracts (ERC-20, bridge, staking, governance modules) — tidak diumumkan
- [token] Regulatory classification token (utility vs security) di berbagai yurisdiksi — whitepaper mengakui ketidakpastian regulasi
- [ecosystem] Specific CEX listings for VANA token (exchange names, listing dates, trading pairs) — not publicly announced
- [ecosystem] Active IBC channels and relayer operators — enabled on mainnet but not documented publicly
- [ecosystem] Wallet support confirmation: Keplr, Cosmostation, Leap explicit support for Vana Mainnet — not documented
- [ecosystem] Cloud provider(s) used for validator nodes, RPC endpoints, explorer, portal — not disclosed
- [ecosystem] Vana Foundation treasury multi-sig signers and threshold — not public
- [ecosystem] Grant program details: application process, criteria, recipients, amounts — referenced in whitepaper only
- [ecosystem] Hackathon history or planned events — not found in official sources
- [ecosystem] Partner documentation page — inferred from docs structure but not confirmed live
- [ecosystem] Specific Data DAO connector verification methods (zkTLS, TEE, API signatures) — not standardized in docs
- [ecosystem] Market maker / liquidity provider arrangements for VANA — not disclosed
- [ecosystem] Emergency upgrade / halt mechanism for bridge or chain — not documented
- [ecosystem] Validator set composition: nakamoto coefficient, stake distribution, geographic distribution — explorer shows raw data only
- [ecosystem] Historical testnet (Moksha) state migration to mainnet — not documented
- [ecosystem] Audit status: any private audits conducted, auditor firms, scope — none announced publicly
- [ecosystem] Regulatory engagement status in key jurisdictions (US, EU, Singapore, etc.) — whitepaper acknowledges uncertainty only
- [ecosystem] Enterprise partnerships beyond Data DAOs — not documented
- [ecosystem] Community pool / protocol treasury on-chain parameters (deposit, voting period, quorum) — not published
- [ecosystem] VANA token fee switch / revenue share activation status — whitepaper mentions but governance status unclear
- [market] Specific CEX listing venues, trading pairs, and listing dates for VANA token — not publicly announced
- [market] Market maker / liquidity provider arrangements for VANA — not disclosed
- [market] 24h/7d/30d trading volume history (CEX + DEX aggregated) — not available from single verified source
- [market] TVL at protocol level and per Data DAO — no public dashboard; Vana not on DeFiLlama
- [market] Daily/Monthly Active Users (unique addresses transacting) — no public analytics
- [market] Total staked VANA, staking ratio, validator count, Nakamoto coefficient — explorer shows raw data only
- [market] Bridge volume (Vana-Ethereum) historical — no public analytics
- [market] Developer activity metrics (commits, active devs, repos) — GitHub raw data only, not aggregated
- [market] Market share vs. competitors (Ocean, Streamr, etc.) — category not tracked by analytics platforms
- [market] VANA token circulating supply, FDV, market cap (current) — CoinGecko shows but not cross-verified with on-chain
- [market] Holder distribution (whale concentration, foundation %, investor %, community %) — not disclosed
- [market] Unlock schedule impact on liquidity (vesting cliffs for team/investors) — not public
- [market] Grant program deployment and ecosystem funding metrics — referenced in whitepaper, no public data
- [market] Audit status and any security incidents — none announced
- [market] Regulatory status in key jurisdictions (US, EU) for Data DAO model — whitepaper acknowledges uncertainty
- [market] Enterprise partnerships beyond 5 Data DAOs — not documented
- [market] IBC active channels, relayer status, cross-chain volume — enabled but not documented
- [market] Whether Moksha testnet incentives/state migrated to mainnet — not documented
- [market] Fee switch / protocol revenue activation status — whitepaper mentions, not confirmed live
- [market] Treasury size, composition, runway — not disclosed
- [behavioral] Exact Vana Foundation legal name dan registration number di Cayman Islands — tidak fully public di registry searches
- [behavioral] Complete core team headcount dan org chart — only partial public disclosure
- [behavioral] TGE unlock schedule specifics (vesting cliffs, team/investor allocations) — whitepaper references tapi full schedule tidak published in single source
- [behavioral] Whether VANA token has fee switch / revenue share mechanism active — whitepaper mentions tapi governance status unclear
- [behavioral] Total treasury size dan composition (stable vs VANA) — not disclosed publicly
- [behavioral] Exact mainnet genesis block timestamp dan validator set at launch — explorer shows tapi not aggregated in one source
- [behavioral] Regulatory status of Data DAOs in various jurisdictions — whitepaper acknowledges uncertainty
- [behavioral] Whether Moksha testnet data/state was migrated to mainnet or reset — not explicitly documented
- [behavioral] Auditor firms for Vana smart contracts — not publicly announced
- [behavioral] Market maker / liquidity provider arrangements for VANA token — not disclosed
- [behavioral] Enterprise partnerships beyond Data DAOs — not publicly documented
- [behavioral] Grant program recipients dan amounts — not aggregated in single source
- [behavioral] Specific CEX listing venues, trading pairs, dan listing dates untuk VANA token — not publicly announced
- [behavioral] Active IBC channels dan relayer operators — enabled on mainnet but not documented publicly
- [behavioral] Wallet support confirmation: Keplr, Cosmostation, Leap explicit support untuk Vana Mainnet — not documented
- [behavioral] Cloud provider(s) used untuk validator nodes, RPC endpoints, explorer, portal — not disclosed
- [behavioral] Vana Foundation treasury multi-sig signers dan threshold — not public
- [behavioral] Hackathon history atau planned events — not found in official sources
- [behavioral] Specific Data DAO connector verification methods (zkTLS, TEE, API signatures) — not standardized in docs
- [behavioral] Emergency upgrade / halt mechanism untuk bridge atau chain — not documented
- [behavioral] Validator set composition: nakamoto coefficient, stake distribution, geographic distribution — explorer shows raw data only
- [behavioral] Historical testnet (Moksha) state migration to mainnet — not documented
- [behavioral] Audit status: any private audits conducted, auditor firms, scope — none announced publicly
- [behavioral] Regulatory engagement status in key jurisdictions (US, EU, Singapore, etc.) — whitepaper acknowledges uncertainty only
- [behavioral] VANA token fee switch / revenue share activation status — whitepaper mentions but governance status unclear
- [behavioral] Treasury size, composition, runway — not disclosed
- [knowledge] Exact Vana Foundation legal name dan registration number di Cayman Islands — tidak fully public di registry searches【Phase 1 — Open Threads】【Phase 2 — Entity Vana Foundation】【Phase 9 — Open Threads】.
- [knowledge] Complete core team headcount dan org chart — only partial public disclosure【Phase 1 — Open Threads】【Phase 9 — Open Threads】.
- [knowledge] TGE unlock schedule specifics (vesting cliffs, team/investor allocations) — whitepaper references tapi full schedule tidak published in single source【Phase 1 — Open Threads】【Phase 6 — Vesting Schedule】【Phase 9 — Open Threads】.
- [knowledge] Whether VANA token has fee switch / revenue share mechanism active — whitepaper mentions tapi governance status unclear【Phase 1 — Open Threads】【Phase 5 — Revenue Model】【Phase 6 — Inflation/Deflation】【Phase 9 — Open Threads】.
- [knowledge] Total treasury size dan composition (stable vs VANA) — not disclosed publicly【Phase 5 — Treasury】【Phase 9 — Open Threads】.
- [knowledge] Exact mainnet genesis block timestamp dan validator set at launch — explorer shows tapi not aggregated in one source【Phase 1 — Open Threads】【Phase 3 — EV-013】【Phase 9 — Open Threads】.
- [knowledge] Regulatory status of Data DAOs in various jurisdictions — whitepaper acknowledges uncertainty【Phase 1 — Open Threads】【Phase 3 — Open Threads】【Phase 7 — Ecosystem Risks Regulation Dependency】【Phase 9 — Open Threads】.
- [knowledge] Whether Moksha testnet data/state was migrated to mainnet or reset — not explicitly documented【Phase 1 — Open Threads】【Phase 3 — EV-004】【Phase 9 — Open Threads】.
- [knowledge] Auditor firms for Vana smart contracts — not publicly announced【Phase 4 — Audit History】【Phase 7 — Ecosystem Risks Security Dependency】【Phase 9 — Open Threads】.
- [knowledge] Market maker / liquidity provider arrangements untuk VANA token — not disclosed【Phase 5 — Financial Risk】【Phase 8 — Market Summary】【Phase 9 — Open Threads】.
- [knowledge] Enterprise partnerships beyond Data DAOs — not publicly documented【Phase 1 — Open Threads】【Phase 9 — Open Threads】.
- [knowledge] Grant program recipients dan amounts — not aggregated in single source【Phase 5 — Fundraising Mechanism Grant】【Phase 7 — Developer Ecosystem Grant Program】【Phase 9 — Open Threads】.
- [knowledge] Specific CEX listing venues, trading pairs, dan listing dates untuk VANA token — not publicly announced【Phase 8 — Trading Markets】【Phase 9 — Open Threads】.
- [knowledge] Active IBC channels dan relayer operators — enabled on mainnet but not documented publicly【Phase 4 — System Architecture Cross-chain Messaging】【Phase 7 — Major Integrations IBC Channels】【Phase 9 — Open Threads】.
- [knowledge] Wallet support confirmation: Keplr, Cosmostation, Leap explicit support untuk Vana Mainnet — not documented【Phase 7 — Wallet Ecosystem】【Phase 9 — Open Threads】.
- [knowledge] Cloud provider(s) used untuk validator nodes, RPC endpoints, explorer, portal — not disclosed【Phase 7 — Infrastructure Providers】【Phase 9 — Open Threads】.
- [knowledge] Vana Foundation treasury multi-sig signers dan threshold — not public【Phase 5 — Treasury】【Phase 7 — Governance Ecosystem Foundation】【Phase 9 — Open Threads】.
- [knowledge] Hackathon history atau planned events — not found in official sources【Phase 7 — Developer Ecosystem Hackathon】【Phase 9 — Open Threads】.
- [knowledge] Specific Data DAO connector verification methods (zkTLS, TEE, API signatures) — not standardized in docs【Phase 4 — Known Technical Limitations】【Phase 7 — Ecosystem Risks Data Quality Risk】【Phase 9 — Open Threads】.
- [knowledge] Emergency upgrade / halt mechanism untuk bridge atau chain — not documented【Phase 4 — Known Technical Limitations】【Phase 9 — Open Threads】.
- [knowledge] Validator set composition: nakamoto coefficient, stake distribution, geographic distribution — explorer shows raw data only【Phase 4 — Known Technical Limitations】【Phase 9 — Open Threads】.
- [knowledge] Historical testnet (Moksha) state migration to mainnet — not documented【Phase 3 — EV-004】【Phase 9 — Open Threads】.
- [knowledge] Audit status: any private audits conducted, auditor firms, scope — none announced publicly【Phase 4 — Audit History】【Phase 9 — Open Threads】.
- [knowledge] Regulatory engagement status in key jurisdictions (US, EU, Singapore, etc.) — whitepaper acknowledges uncertainty only【Phase 1 — Open Threads】【Phase 9 — Open Threads】.
- [knowledge] VANA token fee switch / revenue share activation status — whitepaper mentions but governance status unclear【Phase 5 — Revenue Model】【Phase 6 — Inflation/Deflation】【Phase 9 — Open Threads】.
- [knowledge] Treasury size, composition, runway — not disclosed【Phase 5 — Treasury】【Phase 9 — Open Threads】.
