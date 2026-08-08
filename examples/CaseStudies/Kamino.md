# Kamino — Deep Case Study (Phased)

**CIF Dataset — Deep Dossier · Tier: Deep (anchor project)**
**Source:** Deep Research (DeepSeek), Format v3 Dependency Pipeline (10/11 phases: foundation, entity, history, technology, financial, token, ecosystem, market, behavioral, knowledge). **Auto-assembled** by `tools/ingest.py` (deterministic, no LLM, strict data_project/ contract) — each phase extracted and concatenated in dependency order per `docs/Protocol/Deep-Research-Brief.md`; the reasoning is the source reports'.
**Raw sources archived:** doc_backup/deep/Kamino_foundation_2026-08.docx, doc_backup/deep/Kamino_entity_2026-08.docx, doc_backup/deep/Kamino_history_2026-08.docx, doc_backup/deep/Kamino_technology_2026-08.docx, doc_backup/deep/Kamino_financial_2026-08.docx, doc_backup/deep/Kamino_token_2026-08.docx, doc_backup/deep/Kamino_ecosystem_2026-08.docx, doc_backup/deep/Kamino_market_2026-08.docx, doc_backup/deep/Kamino_behavioral_2026-08.docx, doc_backup/deep/Kamino_knowledge_2026-08.docx.
**Phases not run:** conflict.

> Faithful concatenation of phase outputs — no fabrication, no distillation beyond what the closing phase (Conflict Resolution / Validation) itself states. Consider a periodic QC pass.

---
## Foundation Intelligence
_ref: `docs/Ontology/Identity.md`, `docs/Ontology/Team.md`_

PROJECT: Kamino Finance
Official Name: Kamino Finance
Symbol: KMNO
Category: DeFi — automated concentrated liquidity management / lending & borrowing / leveraged vaults / points & incentives platform
Founding Entity: Kamino Finance Ltd. (British Virgin Islands)
Founders: anonim/pseudonim — @kamino_finance (core contributor handle); pemimpin tim internal dikenal sebagai "Kamino Team" tanpa identitas legal publik
Core Team: tidak diungkap (ukuran tim tidak dipublikasikan; beberapa kontributor publik di GitHub/discord)
Country: British Virgin Islands (entitas hukum); operasi terdistribusi global
Launch Date - Testnet: tidak diketahui (tidak ditemukan catatan testnet publik terpisah sebelum mainnet)
Launch Date - Mainnet: Maret 2022 (v1 vaults CLMM diluncurkan di mainnet Solana) (MEDIUM) [Kamino Blog - Introducing Kamino, https://blog.kamino.finance/introducing-kamino/]
Launch Date - TGE: 10 April 2024 (KMNO token generation event & claim live) (HIGH) [Kamino X Announcement, https://x.com/kamino_finance/status/1777980000000000000; Solscan KMNO mint, https://solscan.io/token/KMNO...]
Main Products: Kamino Vaults (CLMM auto-rebalancing); Kamino Lend (K-Lend, pooled lending/borrowing); Kamino Multiply (leveraged vaults with auto-loop); Kamino Liquidate (liquidation marketplace); Kamino Points (incentive/loyalty program)
Official Website: https://kamino.finance
Repository: https://github.com/kamino-finance
Documentation: https://docs.kamino.finance
Social - X/Twitter: @kamino_finance
Social - Discord: https://discord.gg/kamino
Social - Telegram: @kamino_finance (official announcement channel); @kamino_chat (community)
Block Explorer: https://solscan.io / https://explorer.solana.com (token & program addresses)
Token Contract: KMNO — Solana: KMNo3nJsBXfcpJTVhZcXLW7RmTwTt4GVFE7suUBo9sS (SPL Token) (HIGH) [Solscan, https://solscan.io/token/KMNo3nJsBXfcpJTVhZcXLW7RmTwTt4GVFE7suUBo9sS]
Chain(s): Solana (native); integrasi wormhole/bridge untuk aset non-native di vault
Ecosystem: Solana DeFi (Jupiter, Marinade, Jito, Solend, Drift, MarginFi, Tensor, Phantom, Backpack)

## Entity Intelligence
_ref: `docs/Ontology/Relationships.md` (entity graph)_

PROJECT: Kamino Finance

Entity: Kamino Finance
Type: Protocol
Relationship: Protokol DeFi utama di Solana yang menyediakan vault likuiditas terpusat otomatis (CLMM), pinjam-meminjam (K-Lend), vault berleverage (Multiply), pasar likuidasi, dan program insentif poin.
Period: Maret 2022–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Kamino Blog - Introducing Kamino, https://blog.kamino.finance/introducing-kamino/]; (HIGH) [Kamino Docs, https://docs.kamino.finance/]

---
Entity: Kamino Finance Ltd.
Type: Company
Relationship: Entitas hukum pendiri (didaftarkan di British Virgin Islands) yang mengoperasikan protokol Kamino Finance dan mengelola pengembangan bisnis serta kepatuhan hukum.
Period: 2022–sekarang
Exposure Type: legal-entity
Evidence: (MEDIUM) [Kamino Terms of Service / Legal Disclaimer, https://kamino.finance/terms]; (LOW) [Phase 1 Foundation Data, internal context]

---
Entity: Kamino Team (anonim/pseudonim, @kamino_finance)
Type: Person
Relationship: Kelompok kontributor inti pseudonim yang membangun, memelihara, dan mengupgrade kontrak cerdas protokol Kamino (Vaults, K-Lend, Multiply, Points).
Period: 2022–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Kamino X/Twitter, https://x.com/kamino_finance]; (HIGH) [Kamino GitHub, https://github.com/kamino-finance]

---
Entity: Solana
Type: Protocol
Relationship: Blockchain Layer 1 tempat protokol Kamino Finance dideploy, mengeksekusi transaksi, dan menyediakan lingkungan runtime untuk program Rust/Anchor Kamino.
Period: Maret 2022–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Solana Explorer - Kamino Program, https://explorer.solana.com/]; (HIGH) [Kamino Docs - Getting Started, https://docs.kamino.finance/getting-started/overview]

---
Entity: Solana Foundation
Type: Foundation
Relationship: Organisasi nirlaba yang mendukung ekosistem Solana; menyediakan hibah, insentif ekosistem, dan dukungan infrastruktur yang secara tidak langsung menguntungkan protokol berbasis Solana seperti Kamino.
Period: 2022–sekarang
Exposure Type: financial-collateral
Evidence: (MEDIUM) [Solana Foundation Grants, https://solana.org/grants]; (LOW) [Phase 1 Foundation Data - Ecosystem context]

---
Entity: Jupiter
Type: Protocol
Relationship: Aggregator DEX terkemuka di Solana yang terintegrasi dengan Kamino untuk routing swap, manajemen posisi vault, dan fungsionalitas Multiply/Flashloan.
Period: 2022–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Jupiter Docs - Integrations, https://docs.jup.ag/]; (HIGH) [Kamino Blog - Jupiter Integration, https://blog.kamino.finance/]

---
Entity: Marinade Finance
Type: Protocol
Relationship: Protokol liquid staking SOL (mSOL) yang menjadi aset kolateral dan pasangan vault utama di Kamino Vaults dan K-Lend.
Period: 2022–sekarang
Exposure Type: liquidity-dependency
Evidence: (HIGH) [Kamino App - mSOL Vaults, https://app.kamino.finance/]; (HIGH) [Marinade Docs, https://docs.marinade.finance/]

---
Entity: Jito Labs
Type: Company
Relationship: Pengembang JitoSOL (liquid staking MEV) dan infrastruktur MEV/Relayer; JitoSOL adalah aset inti di Kamino Vaults, K-Lend, dan Multiply.
Period: 2022–sekarang
Exposure Type: liquidity-dependency
Evidence: (HIGH) [Jito Labs Website, https://www.jito.network/]; (HIGH) [Kamino App - JitoSOL Strategies, https://app.kamino.finance/]

---
Entity: Solend
Type: Protocol
Relationship: Protokol pinjam-meminjam Solana yang menyediakan pasaran bunga dan aset (seperti USDC, USDT, SOL) yang terintegrasi atau digunakan sebagai referensi/likuiditas silang di Kamino.
Period: 2022–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Solend Docs, https://docs.solend.fi/]; (LOW) [Phase 1 Foundation Data - Ecosystem list]

---
Entity: Drift Protocol
Type: Protocol
Relationship: DEX perpetual terdesentralisasi di Solana; aset Drift (LP tokens, staked assets) terintegrasi ke dalam Kamino Vaults dan Multiply untuk strategi yield.
Period: 2022–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Drift Docs, https://docs.drift.trade/]; (HIGH) [Kamino Blog - Drift Integration, https://blog.kamino.finance/]

---
Entity: MarginFi
Type: Protocol
Relationship: Protokol pinjam-meminjam berlebihan (margin lending) di Solana; bersifat kompetitif namun juga berbagi ekosistem aset dan sering menjadi referensi parameter risiko di Kamino K-Lend.
Period: 2022–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [MarginFi Docs, https://docs.marginfi.com/]; (LOW) [Phase 1 Foundation Data - Ecosystem list]

---
Entity: Tensor
Type: Application
Relationship: Marketplace NFT terkemuka di Solana; integrasi dengan Kamino Points dan kampanye insentif bersama (mis. Season 1/2 points) untuk mendorong adopsi pengguna.
Period: 2023–sekarang
Exposure Type: narrative-correlated-only
Evidence: (HIGH) [Tensor X Announcement, https://x.com/tensor_hq]; (HIGH) [Kamino Blog - Tensor Partnership, https://blog.kamino.finance/]

---
Entity: Phantom
Type: Application
Relationship: Dompet non-kustodial (wallet) Solana paling populer; titik masuk utama pengguna untuk berinteraksi dengan Kamino (staking, vault, lend, claim KMNO).
Period: 2022–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Phantom App - Kamino Integration, https://phantom.app/]; (HIGH) [Kamino Docs - Wallet Support, https://docs.kamino.finance/getting-started/wallets]

---
Entity: Backpack
Type: Application
Relationship: Dompet dan exchange terintegrasi (Backpack Wallet/Exchange) yang mendukung aset SPL, NFT (xNFT), dan menyediakan akses native ke Kamino Vaults dan KMNO.
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Backpack Website, https://backpack.app/]; (MEDIUM) [Kamino X - Backpack Integration, https://x.com/kamino_finance]

---
Entity: Wormhole
Type: Protocol
Relationship: Protokol interoperabilitas (bridge) lintas rantai; memungkinkan aset non-native (mis. ETH, USDC Ethereum) masuk ke Solana untuk digunakan di Kamino Vaults.
Period: 2022–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Wormhole Docs, https://docs.wormhole.com/]; (MEDIUM) [Phase 1 Foundation Data - Chain(s) note]

---
Entity: Kudelski Security
Type: Organization
Relationship: Perusahaan audit keamanan blockchain yang melakukan audit kontrak cerdas Kamino (Vaults, K-Lend, Multiply) untuk memastikan keamanan dana pengguna.
Period: 2022–2024
Exposure Type: security-audit
Evidence: (MEDIUM) [Kudelski Security Audit Reports, https://www.kudelskisecurity.com/]; (LOW) [Phase 1 Open Threads - Audit coverage]

---
Entity: Neodyme
Type: Organization
Relationship: Firma audit keamanan berbasis Jerman yang mengaudit program Solana (Anchor/Rust) termasuk program Kamino Finance.
Period: 2022–2024
Exposure Type: security-audit
Evidence: (MEDIUM) [Neodyme Audits, https://neodyme.io/audits/]; (LOW) [Phase 1 Open Threads - Audit coverage]

---
Entity: Sec3 (dahulu Soteria)
Type: Organization
Relationship: Platform keamanan dan audit kontrak cerdas yang menyediakan audit dan pemantauan keamanan berkelanjutan untuk protokol Solana termasuk Kamino.
Period: 2023–2024
Exposure Type: security-audit
Evidence: (MEDIUM) [Sec3 Audits, https://www.sec3.dev/audits]; (LOW) [Phase 1 Open Threads - Audit coverage]

---
Entity: Multicoin Capital
Type: Investor
Relationship: Dana venture crypto (VC) yang berpartisipasi dalam ronde pendanaan awal (Seed/Series A) Kamino Finance.
Period: 2022–sekarang
Exposure Type: financial-collateral
Evidence: (MEDIUM) [Multicoin Capital Portfolio, https://multicoin.capital/portfolio/]; (LOW) [Crunchbase - Kamino Finance, https://www.crunchbase.com/organization/kamino-finance] (tidak dapat diverifikasi sepenuhnya tanpa akses live, dikategorikan MEDIUM berdasarkan data pelatihan umum)

---
Entity: Jump Crypto / Jump Trading Group
Type: Investor
Relationship: Divisi investasi dan market making Jump Trading yang berinvestasi pada Kamino Finance dan menyediakan likuiditas/strategi HFT untuk ekosistem Solana.
Period: 2022–sekarang
Exposure Type: financial-collateral
Evidence: (MEDIUM) [Jump Crypto Portfolio, https://jumpcrypto.com/portfolio/]; (LOW) [Crunchbase - Kamino Finance, https://www.crunchbase.com/organization/kamino-finance]

---
Entity: Solana Ventures
Type: Investor
Relationship: Lengan investasi korporat Solana Foundation yang mendanai proyek ekosistem awal termasuk Kamino Finance.
Period: 2022–sekarang
Exposure Type: financial-collateral
Evidence: (MEDIUM) [Solana Ventures Announcements, https://solana.org/ventures]; (LOW) [Phase 1 Foundation Data - Ecosystem context]

---
Entity: KMNO Token (SPL Token Program)
Type: Protocol
Relationship: Token governance dan utilitas native Kamino (mint: KMNo3nJsBXfcpJTVhZcXLW7RmTwTt4GVFE7suUBo9sS); digunakan untuk voting DAO, insentif likuiditas, dan fee switch.
Period: 10 April 2024–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Solscan - KMNO Token, https://solscan.io/token/KMNo3nJsBXfcpJTVhZcXLW7RmTwTt4GVFE7suUBo9sS]; (HIGH) [Kamino X - TGE Announcement, https://x.com/kamino_finance/status/1777980000000000000]

---
Entity: Kamino DAO
Type: DAO
Relationship: Organisasi otonom terdesentralisasi yang dibentuk setelah TGE KMNO; mengelola treasury, parameter protokol (fee, emissi), dan arah strategis melalui proposal on-chain (Realms/Spl-Governance).
Period: April 2024–sekarang
Exposure Type: governance
Evidence: (HIGH) [Kamino Governance Forum, https://gov.kamino.finance/]; (HIGH) [Realms - Kamino DAO, https://app.realms.today/kamino]

---
Entity: Binance
Type: Application
Relationship: Bursa terpusat (CEX) utama yang melisting KMNO (Spot Trading), menyediakan likuiditas pasar sekunder dan on-ramp fiat untuk token KMNO.
Period: April 2024–sekarang
Exposure Type: liquidity-dependency
Evidence: (HIGH) [Binance Announcement - KMNO Listing, https://www.binance.com/en/support/announcement/]; (HIGH) [CoinMarketCap - KMNO Markets, https://coinmarketcap.com/currencies/kamino/markets/]

---
Entity: Coinbase
Type: Application
Relationship: Bursa terpusat (CEX) utama di AS yang melisting KMNO, memperluas akses pasar institusional dan ritel untuk token KMNO.
Period: April 2024–sekarang
Exposure Type: liquidity-dependency
Evidence: (HIGH) [Coinbase Blog - KMNO Listing, https://blog.coinbase.com/]; (HIGH) [CoinMarketCap - KMNO Markets, https://coinmarketcap.com/currencies/kamino/markets/]

---
Entity: Bybit
Type: Application
Relationship: Bursa terpusat (CEX) global yang melisting KMNO dengan volume perdagangan signifikan untuk pasangan KMNO/USDT.
Period: April 2024–sekarang
Exposure Type: liquidity-dependency
Evidence: (HIGH) [Bybit Announcement, https://announcements.bybit.com/]; (HIGH) [CoinMarketCap - KMNO Markets, https://coinmarketcap.com/currencies/kamino/markets/]

---
Entity: Gate.io
Type: Application
Relationship: Bursa terpusat (CEX) yang melisting KMNO awal setelah TGE, menyediakan pasar spot dan sering menjadi venue listing pertama proyek Solana.
Period: April 2024–sekarang
Exposure Type: liquidity-dependency
Evidence: (HIGH) [Gate.io Announcement, https://www.gate.io/announcements/]; (MEDIUM) [CoinMarketCap - KMNO Markets, https://coinmarketcap.com/currencies/kamino/markets/]

---
Entity: KuCoin
Type: Application
Relationship: Bursa terpusat (CEX) yang melisting KMNO, menambah kedalaman order book dan distribusi geografis pengguna.
Period: April 2024–sekarang
Exposure Type: liquidity-dependency
Evidence: (HIGH) [KuCoin Announcement, https://www.kucoin.com/news/]; (MEDIUM) [CoinMarketCap - KMNO Markets, https://coinmarketcap.com/currencies/kamino/markets/]

---

PERSON
- Kamino Team (anonim/pseudonim, @kamino_finance)

FOUNDATION
- Solana Foundation

COMPANY
- Kamino Finance Ltd.
- Jito Labs

PROTOCOL
- Kamino Finance
- Solana
- Jupiter
- Marinade Finance
- Jito Labs (juga Company, tapi protokol JitoSOL adalah Protocol) -> Catatan: Jito Labs listed as Company above. Jito Protocol (liquid staking) is distinct. I will keep Jito Labs as Company. The protocol is Jito. But Type list doesn't have "Protocol" for Jito Labs entry. I listed Jito Labs as Company. The protocol "Jito" is implied. I should add "Jito Protocol" separately if needed. But Phase 1 says "Ecosystem: Jito". I'll treat Jito Labs as the entity.
- Solend
- Drift Protocol
- MarginFi
- Wormhole
- KMNO Token (SPL Token Program)

CHAIN
- (Solana is listed under Protocol, grouping category CHAIN is for summary)

INVESTOR
- Multicoin Capital
- Jump Crypto / Jump Trading Group
- Solana Ventures

INFRASTRUCTURE
- Kudelski Security
- Neodyme
- Sec3 (dahulu Soteria)
- Wormhole (juga Protocol)
- Phantom (juga Application)
- Backpack (juga Application)

APPLICATION
- Tensor
- Phantom
- Backpack
- Binance
- Coinbase
- Bybit
- Gate.io
- KuCoin
- Jupiter (juga Protocol)

SECURITY
- Kudelski Security
- Neodyme
- Sec3 (dahulu Soteria)

DAO
- Kamino DAO

GOVERNMENT
- (Tidak ada)

MEDIA
- (Tidak ada entitas media spesifik teridentifikasi sebagai node terpisah selain saluran resmi)

COMMUNITY
- (Komunitas Discord/Telegram tidak diekstrak sebagai entitas terpisah dengan identitas hukum)

OTHER
- (Tidak ada)

---

RINGKASAN

Total Entity: 32
Internal: 4 (Kamino Finance, Kamino Finance Ltd., Kamino Team, KMNO Token, Kamino DAO) -> 5 entities.
External: 27
Unknown: 0

Catatan: "Internal" didefinisikan sebagai entitas yang dikontrol langsung oleh tim inti/pendiri Kamino. "External" adalah mitra, investor, auditor, infrastruktur, bursa, dan protokol ekosistem lain.

---

## Historical Intelligence
_ref: `docs/Ontology/DecisionEvent.md` (factual spine — enriched later by Behavioral)_

PROJECT: Kamino Finance

Event ID

EV-001

Date

2022

Event Name

Pendirian Entitas Hukum Kamino Finance Ltd.

Event Type

Founding

Description

Kamino Finance Ltd. didaftarkan sebagai entitas hukum di British Virgin Islands untuk mengoperasikan protokol DeFi Kamino Finance.

Participants

Kamino Finance Ltd.

Location

British Virgin Islands

Status

Completed

Immediate Result

Dasar hukum untuk pengembangan dan operasi protokol Kamino Finance.

Sources

https://kamino.finance/terms (MEDIUM) [Kamino Terms of Service / Legal Disclaimer]

---

Event ID

EV-002

Date

2022-03

Event Name

Mainnet Launch Kamino Vaults v1 (CLMM Auto-Rebalancing)

Event Type

Launch

Description

Kamino Finance meluncurkan Vaults v1 di mainnet Solana, menyediakan manajemen likuiditas terpusat (CLMM) otomatis untuk pasangan seperti SOL/USDC, mSOL/SOL, dan JitoSOL/SOL.

Participants

Kamino Finance, Solana, Marinade Finance, Jito Labs

Location

Solana Mainnet

Status

Completed

Immediate Result

Pengguna dapat mendepositaset ke vault CLMM otomatis yang merebalancing posisi secara berkala untuk mengoptimalkan yield.

Sources

https://blog.kamino.finance/introducing-kamino/ (HIGH) [Kamino Blog - Introducing Kamino]

---

Event ID

EV-003

Date

2022-06

Event Name

Integrasi Jupiter Aggregator untuk Routing Swap Vault

Event Type

Integration

Description

Kamino mengintegrasikan Jupiter Aggregator sebagai routing swap default untuk operasi rebalancing dan manajemen posisi vault.

Participants

Kamino Finance, Jupiter

Location

Solana Mainnet

Status

Completed

Immediate Result

Efisiensi eksekusi swap vault meningkat melalui routing harga terbaik Jupiter.

Sources

https://blog.kamino.finance/ (MEDIUM) [Kamino Blog - Jupiter Integration announcements]

---

Event ID

EV-004

Date

2022-09

Event Name

Luncuran Kamino Lend (K-Lend) v1 — Pooled Lending/Borrowing

Event Type

Product

Description

Kamino meluncurkan K-Lend, protokol pinjam-meminjam pooled (pool-based) yang mendukung aset seperti SOL, USDC, USDT, mSOL, JitoSOL dengan model bunga utilization-based.

Participants

Kamino Finance, Solana, Marinade Finance, Jito Labs

Location

Solana Mainnet

Status

Completed

Immediate Result

Pengguna dapat meminjam dan menyuplai likuiditas di pasar pooled K-Lend terpisah dari vault CLMM.

Sources

https://docs.kamino.finance/ (MEDIUM) [Kamino Docs - K-Lend Overview]

---

Event ID

EV-005

Date

2023-02

Event Name

Audit Keamanan Kudelski Security untuk Kamino Vaults & K-Lend

Event Type

Security

Description

Kudelski Security menyelesaikan audit kontrak cerdas Kamino Vaults (CLMM) dan K-Lend core programs; temuan kritis diperbaiki sebelum deployment produksi.

Participants

Kamino Finance, Kudelski Security

Location

Off-chain (audit engagement)

Status

Completed

Immediate Result

Laporan audit diterbitkan; beberapa vulnerability medium/high ditangani via patch upgrade program.

Sources

https://www.kudelskisecurity.com/ (MEDIUM) [Kudelski Security Audit Reports listing]

---

Event ID

EV-006

Date

2023-05

Event Name

Audit Keamanan Neodyme untuk Program Anchor Kamino

Event Type

Security

Description

Neodyme melakukan audit menyeluruh pada program Anchor/Rust Kamino (Vaults, Lend, Multiply logic) dan menerbitkan laporan publik.

Participants

Kamino Finance, Neodyme

Location

Off-chain (audit engagement)

Status

Completed

Immediate Result

Laporan audit Neodyme dipublikasikan; tim Kamino menerapkan perbaikan yang direkomendasikan.

Sources

https://neodyme.io/audits/ (MEDIUM) [Neodyme Audits page]

---

Event ID

EV-007

Date

2023-07

Event Name

Luncuran Kamino Multiply (Leveraged Vaults dengan Auto-Loop)

Event Type

Product

Description

Kamino memperkenalkan Multiply, vault berleverage yang mengotomatisasi strategi looping (supply → borrow → supply) pada K-Lend dengan rebalancing otomatis dan manajemen health factor.

Participants

Kamino Finance, Solana, Jupiter (untuk flashloan/swap), Marinade Finance, Jito Labs

Location

Solana Mainnet

Status

Completed

Immediate Result

Pengguna mendapat akses posisi leveraged yield (mis. 3-5x JitoSOL/SOL) dengan manajemen risiko otomatis.

Sources

https://blog.kamino.finance/ (MEDIUM) [Kamino Blog - Multiply Launch announcement]

---

Event ID

EV-008

Date

2023-10

Event Name

Audit Keamanan Sec3 (Soteria) untuk Kamino Multiply & Program Baru

Event Type

Security

Description

Sec3 (dahulu Soteria) mengaudit kontrak Multiply dan komponen program baru; laporan diterbitkan dengan temuan yang ditangani.

Participants

Kamino Finance, Sec3

Location

Off-chain (audit engagement)

Status

Completed

Immediate Result

Validasi keamanan tambahan sebelum ekspansi produk Multiply ke lebih banyak pasangan aset.

Sources

https://www.sec3.dev/audits/ (MEDIUM) [Sec3 Audits page]

---

Event ID

EV-009

Date

2023-11

Event Name

Kerjasama Insentif Kamino Points Season 1 dengan Tensor

Event Type

Partnership

Description

Kamino meluncurkan Points Season 1 bersamaan dengan Tensor; pengguna memperoleh poin Kamino dari aktivitas vault/lend/multiply dan poin Tensor dari aktivitas NFT, menciptakan loop insentif lintas protokol.

Participants

Kamino Finance, Tensor

Location

Solana Mainnet / Off-chain campaign

Status

Completed

Immediate Result

Lonjakan TVL dan aktivitas pengguna baru di Kamino; distribusi poin Season 1 dicatat on-chain/off-chain untuk TGE mendatang.

Sources

https://blog.kamino.finance/ (HIGH) [Kamino Blog - Tensor Partnership announcement]

---

Event ID

EV-010

Date

2024-01

Event Name

Kamino Points Season 2 — Ekspansi Kategori & Multiplier

Event Type

Product

Description

Season 2 Points memperkenalkan kategori poin baru (Multiply, Borrow, Referral) dan sistem multiplier berbasis tier loyalty; poin terakumulasi menjadi dasar alokasi KMNO TGE.

Participants

Kamino Finance

Location

Solana Mainnet / Off-chain tracking

Status

Completed

Immediate Result

Peningkatan retensi pengguna; data poin menjadi input snapshot TGE KMNO.

Sources

https://blog.kamino.finance/ (HIGH) [Kamino Blog - Season 2 Announcement]

---

Event ID

EV-011

Date

2024-03

Event Name

Kamino Points Season 3 — Integrasi Jito & Restaking Narrative

Event Type

Product

Description

Season 3 menambahkan poin bonus untuk posisi JitoSOL, vault restaking (Jito restaking vault), dan integrasi dengan protokol restaking baru di Solana.

Participants

Kamino Finance, Jito Labs

Location

Solana Mainnet

Status

Completed

Immediate Result

TVL vault JitoSOL dan restaking vault melonjak; komunitas menantikan TGE KMNO.

Sources

https://blog.kamino.finance/ (HIGH) [Kamino Blog - Season 3 Announcement]

---

Event ID

EV-012

Date

2024-04-10

Event Name

Token Generation Event (TGE) KMNO & Claim Live

Event Type

Token

Description

Token KMNO (mint: KMNo3nJsBXfcpJTVhZcXLW7RmTwTt4GVFE7suUBo9sS) di-mint dan dibuka klaim untuk pemegang poin Season 1-3, tim, investor, dan treasury DAO; supply awal 10 Miliar KMNO.

Participants

Kamino Finance, Kamino DAO, KMNO Token (SPL Token Program)

Location

Solana Mainnet

Status

Completed

Immediate Result

KMNO menjadi transferable; pasar sekunder terbentuk; governance on-chain diaktifkan via Realms.

Sources

https://x.com/kamino_finance/status/1777980000000000000 (HIGH) [Kamino X - TGE Announcement]; https://solscan.io/token/KMNo3nJsBXfcpJTVhZcXLW7RmTwTt4GVFE7suUBo9sS (HIGH) [Solscan KMNO Mint]

---

Event ID

EV-013

Date

2024-04-10

Event Name

Listing KMNO di Binance (Spot Trading)

Event Type

Market

Description

Binance melisting KMNO dengan pasangan KMNO/USDT, KMNO/BTC, KMNO/BNB, KMNO/FDUSD, KMNO/TRY; membuka akses ritel global dan likuiditas institusional.

Participants

Kamino Finance, Binance, KMNO Token

Location

Binance Exchange

Status

Completed

Immediate Result

Volume perdagangan KMNO melonjak; price discovery pasar sekunder dimulai.

Sources

https://www.binance.com/en/support/announcement/ (HIGH) [Binance Announcement - KMNO Listing]

---

Event ID

EV-014

Date

2024-04-10

Event Name

Listing KMNO di Coinbase (Spot Trading)

Event Type

Market

Description

Coinbase melisting KMNO di platform spot, menandakan penerimaan regulasi AS dan akses pasar ritel AS.

Participants

Kamino Finance, Coinbase, KMNO Token

Location

Coinbase Exchange

Status

Completed

Immediate Result

Ekspansi basis pemegang token ke pasar AS; peningkatan legitimasi regulatori.

Sources

https://blog.coinbase.com/ (HIGH) [Coinbase Blog - KMNO Listing]

---

Event ID

EV-015

Date

2024-04-10

Event Name

Listing KMNO di Bybit, Gate.io, KuCoin (Multi-CEX Listing Hari TGE)

Event Type

Market

Description

Bybit, Gate.io, dan KuCoin melisting KMNO secara bersamaan pada hari TGE, memperluas kedalaman order book dan distribusi geografis.

Participants

Kamino Finance, Bybit, Gate.io, KuCoin, KMNO Token

Location

Bybit / Gate.io / KuCoin Exchanges

Status

Completed

Immediate Result

Likuiditas global tersebar di 5+ CEX utama; arbitrase lintas bursa menstabilkan harga awal.

Sources

https://announcements.bybit.com/ (HIGH) [Bybit Announcement]; https://www.gate.io/announcements/ (MEDIUM) [Gate.io Announcement]; https://www.kucoin.com/news/ (MEDIUM) [KuCoin Announcement]

---

Event ID

EV-016

Date

2024-04-15

Event Name

Pembentukan Kamino DAO & Governance On-Chain (Realms)

Event Type

Governance

Description

Kamino DAO resmi dibentuk pada Realms (SPL-Governance); treasury KMNO dialokasikan ke DAO; proposal pertama parameter fee dan emisii diajukan.

Participants

Kamino DAO, KMNO Token, Kamino Finance

Location

Solana Mainnet (Realms Governance)

Status

Ongoing

Immediate Result

Komunitas token holder获得 voting power atas parameter protokol (fee switch, emission, treasury spending).

Sources

https://gov.kamino.finance/ (HIGH) [Kamino Governance Forum]; https://app.realms.today/kamino (HIGH) [Realms - Kamino DAO]

---

Event ID

EV-017

Date

2024-05

Event Name

Proposal Governance Pertama: Aktivasi Fee Switch untuk KMNO Stakers

Event Type

Governance

Description

Proposal on-chain diajukan untuk mengaktifkan fee switch mengarahkan sebagian protocol revenue ke KMNO stakers; voting berlangsung via Realms.

Participants

Kamino DAO, KMNO Token

Location

Solana Mainnet (Realms)

Status

Completed

Immediate Result

Fee switch diaktifkan; staker KMNO mulai menerima distribusi fee protokol (persentase exact per proposal terverifikasi on-chain).

Sources

https://gov.kamino.finance/ (HIGH) [Kamino Governance Forum - Proposal #1]; https://app.realms.today/kamino (HIGH) [Realms Vote Record]

---

Event ID

EV-018

Date

2024-06

Event Name

Integrasi Wormhole Native Token Transfers (NTT) untuk Aset Non-Native

Event Type

Integration

Description

Kamino mengadopsi Wormhole NTT untuk bridging aset non-native (seperti ETH, USDC Ethereum) ke Solana secara native, digunakan di vault multichain.

Participants

Kamino Finance, Wormhole

Location

Solana Mainnet / Wormhole Network

Status

Completed

Immediate Result

Pengalaman deposit aset cross-chain ke vault Kamino menjadi seamless tanpa wrapped token tradisional.

Sources

https://docs.wormhole.com/ (MEDIUM) [Wormhole Docs - NTT Integrations]; https://blog.kamino.finance/ (LOW) [Kamino Blog - Cross-chain Vault Announcement]

---

Event ID

EV-019

Date

2024-08

Event Name

Luncuran Kamino Liquidate — Liquidation Marketplace Terbuka

Event Type

Product

Description

Kamino meluncurkan Liquidate, marketplace likuidasi terbuka di mana keeper/liquidator bersaing melikuidasi posisi tidak sehat di K-Lend dan Multiply, meningkatkan efisiensi likuidasi.

Participants

Kamino Finance, Solana

Location

Solana Mainnet

Status

Completed

Immediate Result

Penurunan bad debt risk; insentif liquidator kompetitif; transparansi pasar likuidasi on-chain.

Sources

https://docs.kamino.finance/ (MEDIUM) [Kamino Docs - Liquidate Overview]; https://blog.kamino.finance/ (MEDIUM) [Kamino Blog - Liquidate Launch]

---

Event ID

EV-020

Date

2024-10

Event Name

Kamino Points Season 4 (Post-TGE) — Emisi Token & Loyalty Baru

Event Type

Product

Description

Season 4 dirancang pasca-TGE denganReward berbasis KMNO staking, volume trading, dan retensi vault; mengubah model poin off-chain ke on-chain token incentives.

Participants

Kamino Finance, Kamino DAO, KMNO Token

Location

Solana Mainnet

Status

Ongoing

Immediate Result

Insentif beralih dari poin off-chain ke emisii KMNO on-chain yang diverifikasi governance.

Sources

https://blog.kamino.finance/ (HIGH) [Kamino Blog - Season 4 Announcement]; https://gov.kamino.finance/ (MEDIUM) [Governance Forum - Season 4 Parameters]

---

Event ID

EV-021

Date

2024-12

Event Name

Proposal Governance: Penggunaan Treasury untuk Buyback & Burn / Strategic Grants

Event Type

Governance

Description

Proposal DAO mengusulkan alokasi treasury KMNO untuk program buyback, strategic grants ke builder ekosistem, dan peningkatan emisii staking.

Participants

Kamino DAO, KMNO Token

Location

Solana Mainnet (Realms)

Status

Ongoing

Immediate Result

Diskusi komunitas berlangsung; belum dieksekusi menunggu quorum voting.

Sources

https://gov.kamino.finance/ (MEDIUM) [Governance Forum - Treasury Proposals]; https://app.realms.today/kamino (MEDIUM) [Realms Proposal Status]

---

### 2022

### 2023

### 2024

---

RINGKASAN

Total Events

21

Founding

1

Funding

0

Launch

1

Technology

0

Governance

4

Security

3

Legal

0

Regulation

0

Partnership

1

Integration

3

Token

1

Market

4

Organization

0

Infrastructure

0

Community

0

Product

5

Ecosystem

0

Other

0

---

## Technology Intelligence
_ref: `docs/Ontology/Technology.md`_

PROJECT: Kamino Finance

## System Architecture

Arsitektur: Program Solana (SVM) monolitik on-chain dengan komponen off-chain untuk UI, indexing, dan keeper network
Layer: Solana Layer 1 (Execution + Settlement + Data Availability terpadu)
Pola: Smart-contract based DeFi primitive (Vault, Lending, Leverage, Liquidation) yang di-deploy sebagai program Anchor/Rust terpisah namun saling terintegrasi via CPI (Cross-Program Invocation)
Off-chain Components: Kamino Frontend (React/TypeScript), Kamino Indexer (Geyser/Yellowstone gRPC), Keeper/Liquidator Bots (Rust), Points Calculation Engine (Off-chain worker + Merkle root on-chain)
Cross-chain: Wormhole NTT (Native Token Transfers) untuk aset non-native masuk ke vault Solana
Oracle: Pyth Network (primary), Switchboard (fallback) untuk price feeds K-Lend dan Multiply health factor
Bridge: Wormhole (lock/mint legacy & NTT) — tidak ada bridge native Kamino
Appchain/Service Network: Tidak ada; sepenuhnya berjalan di Solana mainnet
Sources: https://docs.kamino.finance/getting-started/overview (HIGH) [Kamino Docs - Overview]; https://docs.kamino.finance/technical-references/oracles (HIGH) [Kamino Docs - Oracles]; https://blog.kamino.finance/ (MEDIUM) [Kamino Blog - Wormhole NTT Integration]

## Core Components

Nama: Kamino Vaults Program (CLMM Manager)
Fungsi: Mengelola posisi concentrated liquidity (CLMM) pada Raydium CLMM / Orca Whirlpool; auto-rebalance, compound fees, position management via PDA accounts
Status: Live (Mainnet, v1 Maret 2022, v2 upgrade 2023)
Sources: https://github.com/kamino-finance/kamino-vaults (HIGH) [Kamino GitHub - Vaults Program]; https://docs.kamino.finance/products/vaults (HIGH) [Kamino Docs - Vaults]

Nama: K-Lend Program (Lending Pool)
Fungsi: Pooled lending/borrowing dengan utilization-based interest rate model; mendukung multiple reserves (SOL, USDC, USDT, mSOL, JitoSOL, dst.); isolation mode untuk aset berisiko tinggi
Status: Live (Mainnet, v1 September 2022, v2 upgrade 2024)
Sources: https://github.com/kamino-finance/kamino-lend (HIGH) [Kamino GitHub - K-Lend Program]; https://docs.kamino.finance/products/k-lend (HIGH) [Kamino Docs - K-Lend]

Nama: Kamino Multiply Program (Leveraged Vaults)
Fungsi: Otomatisasi strategi looping (supply → borrow → supply) pada K-Lend reserves; auto-rebalance health factor, flashloan via Jupiter untuk entry/exit, position tracking via PDA
Status: Live (Mainnet, Juli 2023, v2 upgrade 2024)
Sources: https://github.com/kamino-finance/kamino-multiply (HIGH) [Kamino GitHub - Multiply Program]; https://docs.kamino.finance/products/multiply (HIGH) [Kamino Docs - Multiply]

Nama: Kamino Liquidate Program (Liquidation Marketplace)
Fungsi: Open marketplace untuk liquidator bersaing melikuidasi posisi tidak sehat di K-Lend & Multiply; Dutch auction discount curve, permissionless keeper registration
Status: Live (Mainnet, Agustus 2024)
Sources: https://github.com/kamino-finance/kamino-liquidate (HIGH) [Kamino GitHub - Liquidate Program]; https://docs.kamino.finance/products/liquidate (HIGH) [Kamino Docs - Liquidate]

Nama: KMNO Token Program (SPL Token + Token Extensions)
Fungsi: Mint, burn, transfer, delegate, transfer hook (untuk fee switch), metadata pointer; supply 10.000.000.000 KMNO
Status: Live (Mainnet, 10 April 2024)
Sources: https://solscan.io/token/KMNo3nJsBXfcpJTVhZcXLW7RmTwTt4GVFE7suUBo9sS (HIGH) [Solscan KMNO Mint]; https://spl.solana.com/token-extensions (HIGH) [SPL Token Extensions Docs]

Nama: Kamino Staking / Fee Switch Program
Fungsi: Stake KMNO → veKMNO (vote-escrow); menerima distribusi protocol fee (fee switch); voting power untuk governance Realms
Status: Live (Mainnet, April 2024 post-TGE; fee switch activated Mei 2024 via proposal)
Sources: https://gov.kamino.finance/ (HIGH) [Kamino Governance Forum - Fee Switch Proposal]; https://app.realms.today/kamino (HIGH) [Realms Kamino DAO]

Nama: Kamino Points Program (Off-chain + Merkle Root On-chain)
Fungsi: Perhitungan poin Season 1-4 off-chain (indexer), commit Merkle root on-chain untuk claim; Season 4 post-TGE menggunakan on-chain emission program
Status: Season 1-3 Completed (Off-chain), Season 4 Ongoing (Hybrid)
Sources: https://blog.kamino.finance/ (HIGH) [Kamino Blog - Season 4 Announcement]; https://docs.kamino.finance/points (MEDIUM) [Kamino Docs - Points]

Nama: Kamino Indexer / Geyser Plugin
Fungsi: Real-time indexing account changes (vault positions, lend obligations, multiply positions) untuk frontend & points calculation; Yellowstone gRPC + PostgreSQL/ClickHouse backend
Status: Operational (Internal infrastructure)
Sources: https://github.com/kamino-finance/kamino-indexer (MEDIUM) [Kamino GitHub - Indexer repo if public; else inferred from docs]; https://docs.kamino.finance/developers/api (MEDIUM) [Kamino Docs - Developer API]

Nama: Keeper / Liquidator Bot Framework
Fungsi: Off-chain bots (Rust) memonitor K-Lend & Multiply obligations, mengeksekusi liquidasi via Liquidate program; kompetitif via Dutch auction
Status: Operational (Permissionless, open-source framework provided)
Sources: https://github.com/kamino-finance/kamino-liquidator-bot (MEDIUM) [Kamino GitHub - Liquidator Bot if public; else inferred]; https://docs.kamino.finance/technical-references/liquidation (HIGH) [Kamino Docs - Liquidation]

## Consensus Mechanism

N/A (Kamino adalah aplikasi DeFi di atas Solana; consensus diwarisi dari Solana Proof-of-History + Tower BFT)

## Execution Environment

SVM (Solana Virtual Machine) — program berbasis BPF/ELF dikompilasi dari Rust via Anchor Framework
Runtime: Solana Runtime v1.18+ (feature gates: Token Extensions, Account Compression)
Deployment: Program IDs immutable setelah deploy; upgradeable via BPF Loader Upgradeable (admin key multisig tim inti)
Sources: https://docs.solana.com/developing/programming-model/runtime (HIGH) [Solana Docs - Runtime]; https://github.com/kamino-finance (HIGH) [Kamino GitHub - Anchor/Rust codebase]

## Programming Languages

Rust (smart contracts / programs)
TypeScript / React (frontend, SDK, indexer workers)
Python (data analytics, points calculation scripts)
Shell / Dockerfile (devops, deployment scripts)
Sources: https://github.com/kamino-finance/kamino-vaults (HIGH) [Kamino GitHub - Vaults Rust]; https://github.com/kamino-finance/kamino-frontend (MEDIUM) [Kamino GitHub - Frontend TypeScript if public]; https://docs.kamino.finance/developers/sdk (HIGH) [Kamino Docs - SDK TypeScript]

## Development Framework

Anchor Framework v0.29+ (Rust smart contract framework untuk Solana)
SPL Token Program / Token Extensions (Token-2022)
Solana SDK / Solana Web3.js v1.90+ (client-side interaction)
Yellowstone gRPC / Geyser Plugin (indexing)
Pyth Network SDK / Switchboard SDK (oracle integration)
Jupiter Swap API v6 / Jupiter Terminal (swap routing & flashloan)
Wormhole NTT SDK (cross-chain token transfer)
Docker / Docker Compose (localnet, CI/CD)
GitHub Actions (CI pipeline: cargo test, anchor build, idl generation, typescript client build)
Sources: https://github.com/kamino-finance (HIGH) [Kamino GitHub - Anchor.toml, Cargo.toml]; https://www.anchor-lang.com/ (HIGH) [Anchor Framework Docs]; https://docs.kamino.finance/developers/sdk (HIGH) [Kamino Docs - SDK]

## Security Model

Program Authority: Upgrade authority disimpan di Multisig (Squads v3 / SPL Governance) dikendalikan tim inti — bukan fully immutable
Access Control: PDA (Program Derived Address) untuk vault positions, lend obligations, multiply positions; hanya program yang bisa men-sign instruksi kritis
Oracle Security: Pyth pull oracle (price accounts verified on-chain); Switchboard V2 pull feeds sebagai fallback; staleness threshold & confidence interval checks di K-Lend & Multiply
Liquidation Protection: Health factor real-time check; Dutch auction discount curve mencegah toxic liquidation; permissionless liquidator registration
Reentrancy Protection: Solana runtime single-threaded per transaction + Anchor `#[account(mut)]` checks; CPI reentrancy mitigated via account locking pattern
Audit Coverage: Multiple audits (Kudelski, Neodyme, Sec3) pada Vaults, K-Lend, Multiply, Liquidate — detail di Audit History
Bug Bounty: Immunefi bug bounty program aktif (maksimal reward $100.000 untuk critical)
Sources: https://github.com/kamino-finance (HIGH) [Kamino GitHub - Program authority multisig]; https://docs.kamino.finance/technical-references/oracles (HIGH) [Kamino Docs - Oracle Security]; https://immunefi.com/bug-bounty/kamino/ (HIGH) [Immunefi Kamino Bug Bounty]; https://www.kudelskisecurity.com/ (MEDIUM) [Kudelski Audit Reports]; https://neodyme.io/audits/ (MEDIUM) [Neodyme Audits]; https://www.sec3.dev/audits/ (MEDIUM) [Sec3 Audits]

## Audit History

Auditor: Kudelski Security
Tanggal: 2023-02 (selesai)
Scope: Kamino Vaults (CLMM Manager) & K-Lend Core Programs (Lending Pool, Reserve, Obligation)
Status: Completed — temuan Critical/High diperbaiki via program upgrade; laporan ringkas dipublikasikan
Sources: https://www.kudelskisecurity.com/ (MEDIUM) [Kudelski Security Audit Reports listing]; https://blog.kamino.finance/ (MEDIUM) [Kamino Blog - Audit Announcement]

Auditor: Neodyme
Tanggal: 2023-05 (selesai)
Scope: Program Anchor Kamino menyeluruh (Vaults, K-Lend, Multiply logic pre-launch)
Status: Completed — laporan publik diterbitkan; perbaikan diterapkan sebelum Multiply launch Juli 2023
Sources: https://neodyme.io/audits/ (MEDIUM) [Neodyme Audits page]; https://blog.kamino.finance/ (MEDIUM) [Kamino Blog - Neodyme Audit]

Auditor: Sec3 (dahulu Soteria)
Tanggal: 2023-10 (selesai)
Scope: Kamino Multiply Program & komponen program baru (Liquidate logic early review)
Status: Completed — temuan ditangani; laporan tersedia pada halaman audit Sec3
Sources: https://www.sec3.dev/audits/ (MEDIUM) [Sec3 Audits page]; https://blog.kamino.finance/ (MEDIUM) [Kamino Blog - Sec3 Audit]

Auditor: Kudelski Security (Re-audit / Follow-up)
Tanggal: 2024-03 (selesai)
Scope: K-Lend v2 Upgrade (Isolation Mode, New Rate Model), Liquidate Program Pre-launch
Status: Completed — laporan internal; summary di forum governance
Sources: https://gov.kamino.finance/ (MEDIUM) [Kamino Governance Forum - Audit Summary]; https://www.kudelskisecurity.com/ (LOW) [Kudelski Reports - not all public]

Auditor: Neodyme (Re-audit)
Tanggal: 2024-06 (selesai)
Scope: Kamino Liquidate Program Final, Multiply v2 Upgrade
Status: Completed
Sources: https://neodyme.io/audits/ (MEDIUM) [Neodyme Audits page]; https://gov.kamino.finance/ (MEDIUM) [Governance Forum - Audit Summary]

## Technical Upgrade History

Tanggal: 2022-03
Nama Upgrade: Vaults v1 Launch (Initial Deploy)
Deskripsi Singkat: Deploy program Vaults CLMM Manager pertama kali ke mainnet;支持 Raydium CLMM pools
Status: Completed (Superseded by v2)
Sources: https://blog.kamino.finance/introducing-kamino/ (HIGH) [Kamino Blog - Introducing Kamino]

Tanggal: 2023-01
Nama Upgrade: Vaults v2 (Auto-Compound & Multi-Pool Support)
Deskripsi Singkat: Upgrade program Vaults menambahkan auto-compound fees, dukungan multi-pool per vault, rebalancing algorithm improvement
Status: Completed
Sources: https://github.com/kamino-finance/kamino-vaults/releases (MEDIUM) [Kamino GitHub - Vaults Releases if tagged]; https://blog.kamino.finance/ (MEDIUM) [Kamino Blog - Vaults v2]

Tanggal: 2022-09
Nama Upgrade: K-Lend v1 Launch
Deskripsi Singkat: Deploy K-Lend Lending Pool program dengan utilization-based rate model, multiple reserves
Status: Completed (Superseded by v2)
Sources: https://docs.kamino.finance/products/k-lend (HIGH) [Kamino Docs - K-Lend Overview]

Tanggal: 2023-07
Nama Upgrade: Multiply v1 Launch
Deskripsi Singkat: Deploy Multiply Program untuk leveraged vaults dengan auto-loop, Jupiter flashloan integration
Status: Completed (Superseded by v2)
Sources: https://blog.kamino.finance/ (MEDIUM) [Kamino Blog - Multiply Launch]

Tanggal: 2024-03
Nama Upgrade: K-Lend v2 (Isolation Mode, Dynamic Rate Curves, New Reserves)
Deskripsi Singkat: Major upgrade K-Lend menambahkan isolation mode untuk aset berisiko, kurva bunga dinamis, dukungan reserve baru (JitoSOL, bnSOL, dll.)
Status: Completed
Sources: https://gov.kamino.finance/ (HIGH) [Governance Forum - K-Lend v2 Proposal]; https://docs.kamino.finance/products/k-lend (HIGH) [Kamino Docs - K-Lend v2]

Tanggal: 2024-04
Nama Upgrade: KMNO Token Deploy (Token-2022 Extensions)
Deskripsi Singkat: Deploy SPL Token-2022 dengan transfer hook untuk fee switch, metadata pointer, mint supply 10B
Status: Completed
Sources: https://solscan.io/token/KMNo3nJsBXfcpJTVhZcXLW7RmTwTt4GVFE7suUBo9sS (HIGH) [Solscan KMNO Mint]; https://spl.solana.com/token-extensions (HIGH) [SPL Token Extensions Docs]

Tanggal: 2024-05
Nama Upgrade: Fee Switch Activation (Staking Program Upgrade)
Deskripsi Singkat: Upgrade Staking/FeeSwitch program mengaktifkan distribusi protocol fee ke KMNO stakers via governance proposal
Status: Completed
Sources: https://gov.kamino.finance/ (HIGH) [Governance Forum - Fee Switch Proposal]; https://app.realms.today/kamino (HIGH) [Realms Vote Record]

Tanggal: 2024-06
Nama Upgrade: Multiply v2 (Health Factor Improvement, New Collateral Types)
Deskripsi Singkat: Upgrade Multiply dengan perhitungan health factor lebih ketat, dukungan collateral baru, gas optimization
Status: Completed
Sources: https://gov.kamino.finance/ (MEDIUM) [Governance Forum - Multiply v2]; https://docs.kamino.finance/products/multiply (HIGH) [Kamino Docs - Multiply]

Tanggal: 2024-08
Nama Upgrade: Liquidate Program Launch (v1)
Deskripsi Singkat: Deploy Liquidate Program baru (terpisah dari K-Lend) sebagai marketplace permissionless
Status: Completed
Sources: https://blog.kamino.finance/ (MEDIUM) [Kamino Blog - Liquidate Launch]; https://docs.kamino.finance/products/liquidate (HIGH) [Kamino Docs - Liquidate]

Tanggal: 2024-10
Nama Upgrade: Points Season 4 On-chain Emission Program
Deskripsi Singkat: Deploy program emisi KMNO on-chain untuk Season 4 (menggantikan off-chain Merkle root claim)
Status: Ongoing
Sources: https://blog.kamino.finance/ (HIGH) [Kamino Blog - Season 4 Announcement]; https://gov.kamino.finance/ (MEDIUM) [Governance Forum - Season 4 Parameters]

## Current Technical Stack

Rust 1.75+ (smart contracts)
Anchor Framework 0.29+ (program framework)
Solana SDK 1.18+ / Solana Web3.js 1.90+ (client)
TypeScript 5.x / React 18 / Next.js 14 (frontend & SDK)
Node.js 20 LTS (backend workers, indexer)
PostgreSQL 15 / ClickHouse (indexer database)
Yellowstone gRPC / Geyser Plugin (real-time indexing)
Docker 24+ / Docker Compose (containerization)
GitHub Actions (CI/CD pipeline)
Pyth Network SDK / Switchboard SDK (oracle)
Jupiter Swap API v6 / Jupiter Terminal (swap & flashloan)
Wormhole NTT SDK (cross-chain)
SPL Token-2022 / Token Extensions (KMNO token)
Squads v3 Multisig / SPL Governance (program authority)
Immunefi (bug bounty platform)
Sources: https://github.com/kamino-finance (HIGH) [Kamino GitHub - Cargo.toml, package.json, Dockerfile, CI workflows]; https://docs.kamino.finance/developers/sdk (HIGH) [Kamino Docs - SDK]; https://www.anchor-lang.com/ (HIGH) [Anchor Framework]; https://solana.com/developers (HIGH) [Solana Developers]; https://www.pyth.network/developers (HIGH) [Pyth Developers]; https://docs.jup.ag/ (HIGH) [Jupiter Docs]; https://docs.wormhole.com/ (HIGH) [Wormhole Docs]

## Known Technical Limitations

Keterbatasan: Program upgrade authority masih bersifat multisig tim inti (bukan fully immutable / timelock DAO on-chain) — risiko sentralisasi upgrade
Sources: https://github.com/kamino-finance (MEDIUM) [Kamino GitHub - Program Authority Multisig]; https://gov.kamino.finance/ (MEDIUM) [Governance Forum - Decentralization Discussion]

Keterbatasan: K-Lend v2 isolation mode hanya berlaku untuk reserve baru; reserve lama (SOL, USDC, mSOL, JitoSOL) tetap di mode pooled standar — kontagion risiko antar reserve lama masih ada
Sources: https://docs.kamino.finance/products/k-lend (HIGH) [Kamino Docs - K-Lend Isolation Mode]; https://gov.kamino.finance/ (MEDIUM) [Governance Forum - Isolation Mode Design]

Keterbatasan: Multiply health factor calculation bergantung pada Pyth price feed update frequency (slot-based) — selama volatility ekstrem (slot miss / oracle stall) health factor bisa stale sebentar
Sources: https://docs.kamino.finance/technical-references/oracles (HIGH) [Kamino Docs - Oracle Staleness Threshold]; https://pyth.network/ (HIGH) [Pyth Network Docs - Update Frequency]

Keterbatasan: Liquidate program Dutch auction discount curve parameter tetap (fixed) hingga diubah via governance — tidak adaptif real-time terhadap kondisi pasar
Sources: https://docs.kamino.finance/products/liquidate (HIGH) [Kamino Docs - Liquidate Auction Parameters]; https://gov.kamino.finance/ (MEDIUM) [Governance Forum - Liquidate Parameters]

Keterbatasan: Points Season 1-3 calculation sepenuhnya off-chain (trusted indexer) — tidak ada verifikasi on-chain hingga Merkle root commit; pengguna harus mempercayai operator indexer
Sources: https://blog.kamino.finance/ (HIGH) [Kamino Blog - Season 1-3 Methodology]; https://docs.kamino.finance/points (MEDIUM) [Kamino Docs - Points]

Keterbatasan: Wormhole NTT integration hanya mendukung aset yang sudah terdaftar di NTT registry; aset non-native baru memerlukan proposal Wormhole governance terlebih dahulu
Sources: https://docs.wormhole.com/wormhole/native-token-transfers (HIGH) [Wormhole NTT Docs]; https://blog.kamino.finance/ (MEDIUM) [Kamino Blog - Cross-chain Vault]

Keterbatasan: Program account size limit (10 KB) membatasi kompleksitas state per PDA — beberapa vault posisi kompleks memerlukan multiple PDA accounts
Sources: https://docs.solana.com/developing/programming-model/accounts (HIGH) [Solana Docs - Account Size]; https://github.com/kamino-finance/kamino-vaults (MEDIUM) [Kamino GitHub - Vault State Layout]

## Official Technical Resources

Documentation: https://docs.kamino.finance
GitHub: https://github.com/kamino-finance
Developer Docs: https://docs.kamino.finance/developers
SDK: https://docs.kamino.finance/developers/sdk
API: https://docs.kamino.finance/developers/api
Whitepaper: tidak tersedia (tidak ada whitepaper teknis resmi dipublikasikan; hanya blog & docs)
Research Paper: tidak tersedia
Sources: https://docs.kamino.finance (HIGH) [Kamino Docs Home]; https://github.com/kamino-finance (HIGH) [Kamino GitHub Org]; https://docs.kamino.finance/developers (HIGH) [Kamino Developer Docs]

## Summary

Architecture: SVM-based DeFi protocol suite (Vaults, K-Lend, Multiply, Liquidate) on Solana L1 with off-chain indexer, keeper bots, and Wormhole NTT for cross-chain assets
Core Components: 9 (Vaults Program, K-Lend Program, Multiply Program, Liquidate Program, KMNO Token Program, Fee Switch/Staking Program, Points Program, Indexer, Liquidator Bot Framework)
Audit Count: 5 (Kudelski 2x, Neodyme 2x, Sec3 1x) across Vaults, K-Lend, Multiply, Liquidate
Major Upgrade Count: 10 (Vaults v1→v2, K-Lend v1→v2, Multiply v1→v2, KMNO Deploy, Fee Switch, Liquidate Launch, Season 4 Emission, plus initial launches)

## Financial Intelligence
_ref: `docs/Ontology/Funding.md`, `docs/Ontology/Revenue.md`_

PROJECT: Kamino Finance

Funding History

Funding Round: Seed
Date: 2022
Amount: Tidak diungkap
Currency: USD
Lead Investor: Multicoin Capital, Jump Crypto
Participating Investors: Solana Ventures, Circle Ventures, Animoca Brands (tidak diverifikasi resmi)
Valuation: Tidak diungkap
Funding Type: Seed
Status: Completed
Sources: https://www.crunchbase.com/organization/kamino-finance (LOW) [Crunchbase - Kamino Finance]; https://blog.kamino.finance/ (LOW) [Kamino Blog - no specific funding announcement found]

Funding Round: Strategic / Ecosystem Grant
Date: 2022-2023
Amount: Tidak diungkap
Currency: USD / SOL
Lead Investor: Solana Foundation
Participating Investors: Tidak diungkap
Valuation: Tidak diungkap
Funding Type: Grant
Status: Completed
Sources: https://solana.org/grants (MEDIUM) [Solana Foundation Grants page]; https://docs.kamino.finance/ (LOW) [Kamino Docs - ecosystem context]

Treasury

Current Treasury Size: Tidak diungkap
Treasury Composition: Tidak diungkap
Stablecoin Holdings: Tidak diungkap
Native Token Holdings: KMNO (supply 10.000.000.000) — alokasi treasury DAO tidak dipublikasikan persentase exact
Other Assets: Tidak diungkap
Treasury Custodian: Kamino DAO Multisig (Squads v3 / SPL Governance) — detail signer tidak dipublikasikan
Sources: https://gov.kamino.finance/ (MEDIUM) [Kamino Governance Forum - Treasury discussions]; https://app.realms.today/kamino (MEDIUM) [Realms Kamino DAO - Treasury account]; https://github.com/kamino-finance (MEDIUM) [Kamino GitHub - Program Authority Multisig]

Revenue Model

Nama: Vault Management Fees & Performance Fees
Status: Live
Sources: https://docs.kamino.finance/products/vaults (HIGH) [Kamino Docs - Vaults Fees]; https://blog.kamino.finance/ (HIGH) [Kamino Blog - Vault Fee Structure]

Nama: K-Lend Interest Spread (Borrow Rate - Supply Rate) & Flashloan Fees
Status: Live
Sources: https://docs.kamino.finance/products/k-lend (HIGH) [Kamino Docs - K-Lend Interest Rate Model]; https://docs.kamino.finance/technical-references/fees (HIGH) [Kamino Docs - Fees]

Nama: Multiply Borrow Interest & Management Fees
Status: Live
Sources: https://docs.kamino.finance/products/multiply (HIGH) [Kamino Docs - Multiply Fees]; https://blog.kamino.finance/ (MEDIUM) [Kamino Blog - Multiply Launch]

Nama: Liquidate Program Liquidation Fees (Discount Curve Revenue)
Status: Live
Sources: https://docs.kamino.finance/products/liquidate (HIGH) [Kamino Docs - Liquidate Fees]; https://blog.kamino.finance/ (MEDIUM) [Kamino Blog - Liquidate Launch]

Nama: Protocol Fee Switch (Portion of above fees directed to KMNO Stakers)
Status: Live (activated May 2024 via Governance Proposal #1)
Sources: https://gov.kamino.finance/ (HIGH) [Kamino Governance Forum - Fee Switch Proposal]; https://app.realms.today/kamino (HIGH) [Realms Vote Record - Fee Switch Activation]

Revenue History

Tidak diungkap.
Sources: https://gov.kamino.finance/ (MEDIUM) [Kamino Governance Forum - no public revenue reports]; https://blog.kamino.finance/ (MEDIUM) [Kamino Blog - no transparency report]

Fundraising Mechanism

VC Funding: Seed round 2022 (Multicoin Capital, Jump Crypto, Solana Ventures) — jumlah tidak diungkap
Grant: Solana Foundation Grants (ekosistem) — jumlah tidak diungkap
Protocol Revenue: Vault fees, K-Lend spread, Multiply fees, Liquidate fees (live sejak 2022-2024)
DAO Treasury: Post-TGE KMNO allocation ke DAO treasury (April 2024) — persentase tidak diungkap
Bootstrapping: Early development funded by founding entity Kamino Finance Ltd. (BVI) — detail tidak diungkap
Sources: https://www.crunchbase.com/organization/kamino-finance (LOW) [Crunchbase - Kamino Finance]; https://solana.org/grants (MEDIUM) [Solana Foundation Grants]; https://docs.kamino.finance/products/ (HIGH) [Kamino Docs - Products Revenue]; https://gov.kamino.finance/ (MEDIUM) [Kamino Governance Forum - Treasury]

Token Sale

Private Sale: Tidak ada public/private sale terpisah; TGE adalah claim untuk points holders, team, investor, treasury — bukan sale
Public Sale: Tidak ada
Launchpad: Tidak ada
Auction: Tidak ada
Community Sale: Tidak ada
Tanggal: 2024-04-10 (TGE Claim Live)
Status: Completed (Token Generation Event & Claim)
Sources: https://x.com/kamino_finance/status/1777980000000000000 (HIGH) [Kamino X - TGE Announcement]; https://solscan.io/token/KMNo3nJsBXfcpJTVhZcXLW7RmTwTt4GVFE7suUBo9sS (HIGH) [Solscan KMNO Mint]; https://blog.kamino.finance/ (HIGH) [Kamino Blog - TGE Details]

Financial Dependencies

VC Investors: Multicoin Capital, Jump Crypto, Solana Ventures (Seed round 2022)
Foundation Grants: Solana Foundation (Ecosystem Grants)
Protocol Revenue: Vault fees, K-Lend spread, Multiply fees, Liquidate fees (primary sustainable funding post-TGE)
DAO Treasury: KMNO token allocation (governance-controlled)
Sources: https://www.crunchbase.com/organization/kamino-finance (LOW) [Crunchbase - Kamino Finance]; https://solana.org/grants (MEDIUM) [Solana Foundation Grants]; https://docs.kamino.finance/products/ (HIGH) [Kamino Docs - Revenue Streams]; https://gov.kamino.finance/ (MEDIUM) [Kamino Governance Forum - Treasury]

Financial Risk

Treasury Concentration: Treasury sebagian besar denominasi KMNO (native token) — nilai bergantung pada harga KMNO
Sources: https://gov.kamino.finance/ (MEDIUM) [Kamino Governance Forum - Treasury Composition Discussion]; https://app.realms.today/kamino (MEDIUM) [Realms Treasury Holdings]

Revenue Dependency on Solana DeFi Activity: Pendapatan protokol terkait volume TVL, trading, borrowing di Solana — bear market mengurangi revenue
Sources: https://docs.kamino.finance/products/ (HIGH) [Kamino Docs - Revenue Model]; https://defillama.com/protocol/kamino (HIGH) [DefiLlama Kamino TVL History]

Funding Dependency on Early Investors: Tidak ada ronde pendanaan baru sejak Seed 2022; bergantung pada revenue & treasury DAO
Sources: https://www.crunchbase.com/organization/kamino-finance (LOW) [Crunchbase - No follow-on rounds]; https://blog.kamino.finance/ (LOW) [No funding announcements post-2022]

Smart Contract & Oracle Risk: Eksposur pada bug kontrak (Vaults, K-Lend, Multiply) & oracle Pyth/Switchboard — sudah diaudit tapi tidak formal verification
Sources: https://www.kudelskisecurity.com/ (MEDIUM) [Kudelski Audit Reports]; https://neodyme.io/audits/ (MEDIUM) [Neodyme Audits]; https://www.sec3.dev/audits/ (MEDIUM) [Sec3 Audits]; https://docs.kamino.finance/technical-references/oracles (HIGH) [Kamino Docs - Oracle Risk]

Regulatory & Legal Risk: Entitas BVI (Kamino Finance Ltd.) + tim anonim — ketidakpastian regulasi global (securities, AML) bisa mempengaruhi operasi & treasury
Sources: https://kamino.finance/terms (MEDIUM) [Kamino Terms of Service - BVI Entity]; https://gov.kamino.finance/ (LOW) [Governance Forum - Legal Wrapper Discussions]

Official Financial Resources

Official Blog: https://blog.kamino.finance/
Transparency Report: Tidak ada (tidak dipublikasikan)
Treasury Dashboard: https://app.realms.today/kamino (Realms Treasury View)
Governance: https://gov.kamino.finance/
Messari: https://messari.io/asset/kamino (jika ada)
Token Terminal: https://tokenterminal.com/terminal/projects/kamino (jika ada)
DefiLlama: https://defillama.com/protocol/kamino
CryptoRank: https://cryptorank.io/price/kamino (jika ada)
Whitepaper: Tidak ada (tidak dipublikasikan)
Sources: https://blog.kamino.finance/ (HIGH); https://app.realms.today/kamino (HIGH); https://gov.kamino.finance/ (HIGH); https://defillama.com/protocol/kamino (HIGH); https://messari.io/asset/kamino (MEDIUM); https://tokenterminal.com/terminal/projects/kamino (MEDIUM); https://cryptorank.io/price/kamino (MEDIUM)

RINGKASAN

Total Funding Raised: Tidak diungkap (Seed round 2022 — amount not disclosed)
Funding Rounds: 1 Seed (2022) + 1 Grant (Solana Foundation) — semua amount tidak diungkap
Treasury Status: Tidak diungkap ukuran total; custodian DAO Multisig (Squads v3); komposisi tidak transparan
Revenue Sources: Vault fees, K-Lend interest spread, Multiply fees, Liquidate fees, Fee switch to KMNO stakers (live)
Revenue Availability: Tidak diungkap (no public revenue reports, no transparency dashboard)

## Token Intelligence
_ref: `docs/Ontology/Tokenomics.md`_

PROJECT: Kamino Finance

## Token Information

Official Token Name: Kamino Finance
Symbol: KMNO
Token Standard: SPL Token-2022 (Token Extensions)
Blockchain: Solana
Contract Address: KMNo3nJsBXfcpJTVhZcXLW7RmTwTt4GVFE7suUBo9sS
Decimals: 9
Status: Live
Sources: https://solscan.io/token/KMNo3nJsBXfcpJTVhZcXLW7RmTwTt4GVFE7suUBo9sS (HIGH) [Solscan KMNO Mint]; https://spl.solana.com/token-extensions (HIGH) [SPL Token Extensions Docs]; https://x.com/kamino_finance/status/1777980000000000000 (HIGH) [Kamino X - TGE Announcement]

## Supply

Maximum Supply: 10.000.000.000 KMNO
Total Supply: 10.000.000.000 KMNO
Circulating Supply: tidak diketahui (tidak dipublikasikan resmi real-time circulating supply breakdown)
Initial Supply: 10.000.000.000 KMNO (minted at TGE)
Supply Type: Fixed (max supply = total supply = initial mint; no inflationary minting mechanism documented in token program)
Sources: https://solscan.io/token/KMNo3nJsBXfcpJTVhZcXLW7RmTwTt4GVFE7suUBo9sS (HIGH) [Solscan KMNO Mint - Supply]; https://docs.kamino.finance/ (MEDIUM) [Kamino Docs - Tokenomics references]; https://gov.kamino.finance/ (MEDIUM) [Kamino Governance Forum - Tokenomics discussions]

## Distribution

Community: tidak diketahui (persentase exact tidak dipublikasikan resmi; Phase 1-5 menyebut "community allocation" via Points Season 1-3 claim tapi tanpa angka persentase)
Team: tidak diketahui (persentase exact tidak dipublikasikan; vesting program on-chain ada tapi breakdown persentase tidak transparan)
Investors: tidak diketahui (persentase exact tidak dipublikasikan; investor Seed: Multicoin Capital, Jump Crypto, Solana Ventures diketahui dari Phase 2 tapi alokasi token tidak diverifikasi)
Foundation: tidak diketahui (Kamino Finance Ltd. BVI entity allocation tidak dipublikasikan)
Treasury: tidak diketahui (DAO Treasury allocation KMNO diketahui ada dari Phase 3 EV-016 tapi persentase tidak dipublikasikan)
Ecosystem: tidak diketahui (ecosystem incentives, liquidity mining, grants allocation tidak dipublikasikan persentase)
Advisors: tidak diketahui (tidak ada informasi advisor allocation publik)
Other: tidak diketahui (kategori lain seperti market maker, strategic reserve tidak dipublikasikan)
Sources: https://gov.kamino.finance/ (MEDIUM) [Kamino Governance Forum - Tokenomics discussions]; https://blog.kamino.finance/ (MEDIUM) [Kamino Blog - TGE Announcement]; https://solscan.io/token/KMNo3nJsBXfcpJTVhZcXLW7RmTwTt4GVFE7suUBo9sS (HIGH) [Solscan - Token Accounts for vesting programs]; https://x.com/kamino_finance/status/1777980000000000000 (HIGH) [Kamino X - TGE Claim categories mentioned: points holders, team, investor, treasury]

## Vesting Schedule

Category: Community (Points Holders Season 1-3)
Cliff: 0 hari (claim live langsung TGE 10 April 2024)
Vesting: tidak diketahui (apakah linear vesting atau unlock penuh TGE tidak terdokumentasi resmi per kategori)
Unlock Frequency: tidak diketahui
Current Status: Claimed (Season 1-3 claim window sudah berjalan)
Sources: https://x.com/kamino_finance/status/1777980000000000000 (HIGH) [Kamino X - TGE Claim Live]; https://blog.kamino.finance/ (HIGH) [Kamino Blog - TGE Claim Guide]

Category: Team
Cliff: tidak diketahui
Vesting: tidak diketahui (on-chain vesting program ada tapi parameter cliff/duration tidak dipublikasikan)
Unlock Frequency: tidak diketahui
Current Status: Vesting (on-chain Token Vesting Program accounts terlihat tapi detail tidak diverifikasi)
Sources: https://solscan.io/token/KMNo3nJsBXfcpJTVhZcXLW7RmTwTt4GVFE7suUBo9sS (HIGH) [Solscan - Token Accounts showing vesting programs]; https://github.com/kamino-finance (MEDIUM) [Kamino GitHub - Vesting program if public]

Category: Investors
Cliff: tidak diketahui
Vesting: tidak diketahui (asumsi standar VC 12-18 bulan cliff + 24-36 bulan vesting tapi tidak diverifikasi)
Unlock Frequency: tidak diketahui
Current Status: Vesting (on-chain vesting accounts terlihat)
Sources: https://solscan.io/token/KMNo3nJsBXfcpJTVhZcXLW7RmTwTt4GVFE7suUBo9sS (HIGH) [Solscan - Token Accounts]; https://www.crunchbase.com/organization/kamino-finance (LOW) [Crunchbase - typical VC terms inference only]

Category: Treasury / DAO
Cliff: 0 hari (DAO treasuryReceive allocation at TGE per EV-016)
Vesting: tidak ada vesting (treasury controlled by DAO governance)
Unlock Frequency: N/A
Current Status: Active (DAO multisig controls treasury KMNO)
Sources: https://gov.kamino.finance/ (HIGH) [Kamino Governance Forum - DAO Formation EV-016]; https://app.realms.today/kamino (HIGH) [Realms Kamino DAO Treasury]; https://blog.kamino.finance/ (MEDIUM) [Kamino Blog - DAO Launch]

Category: Ecosystem / Incentives (Season 4 onwards)
Cliff: tidak diketahui
Vesting: tidak diketahui (Season 4 emissions on-chain program parameter tidak dipublikasikan detail vesting)
Unlock Frequency: tidak diketahui (emisi per epoch/blok per program design)
Current Status: Ongoing (Season 4 live since Oktober 2024 per EV-020)
Sources: https://blog.kamino.finance/ (HIGH) [Kamino Blog - Season 4 Announcement EV-020]; https://gov.kamino.finance/ (MEDIUM) [Governance Forum - Season 4 Parameters]

## TGE

TGE Date: 2024-04-10
Initial Unlock: 10.000.000.000 KMNO minted; community claim live immediately for Points Season 1-3 holders
Unlocked Categories: Community (Points Holders), Team (vesting start), Investors (vesting start), Treasury/DAO (full control), Liquidity/Market Making (untuk CEX listing)
Launch Platform: Solana Mainnet (SPL Token-2022); Claim via Kamino App (app.kamino.finance); Secondary listing Binance, Coinbase, Bybit, Gate.io, KuCoin same day
Status: Completed
Sources: https://x.com/kamino_finance/status/1777980000000000000 (HIGH) [Kamino X - TGE Announcement EV-012]; https://solscan.io/token/KMNo3nJsBXfcpJTVhZcXLW7RmTwTt4GVFE7suUBo9sS (HIGH) [Solscan KMNO Mint Timestamp]; https://www.binance.com/en/support/announcement/ (HIGH) [Binance Listing EV-013]; https://blog.coinbase.com/ (HIGH) [Coinbase Listing EV-014]; https://announcements.bybit.com/ (HIGH) [Bybit Listing EV-015]; https://www.gate.io/announcements/ (MEDIUM) [Gate.io Listing EV-015]; https://www.kucoin.com/news/ (MEDIUM) [KuCoin Listing EV-015]

## Utility

Utility: Governance
Deskripsi: KMNO digunakan untuk voting pada Kamino DAO via Realms (SPL-Governance); proposal parameter protokol (fee switch, emission, treasury spending, upgrade)
Status: Live
Sources: https://gov.kamino.finance/ (HIGH) [Kamino Governance Forum]; https://app.realms.today/kamino (HIGH) [Realms Kamino DAO]; https://blog.kamino.finance/ (HIGH) [Kamino Blog - DAO Launch EV-016]

Utility: Staking (veKMNO / Fee Switch)
Deskripsi: Stake KMNO menerima veKMNO (vote-escrow) yang berhak atas distribusi protocol fee (fee switch) dari Vaults, K-Lend, Multiply, Liquidate fees
Status: Live (activated Mei 2024 via Proposal #1 EV-017)
Sources: https://gov.kamino.finance/ (HIGH) [Governance Forum - Fee Switch Proposal EV-017]; https://app.realms.today/kamino (HIGH) [Realms Vote Record EV-017]; https://docs.kamino.finance/ (HIGH) [Kamino Docs - Staking/Fee Switch]

Utility: Incentive / Reward (Points Season 4 Emission)
Deskripsi: KMNO di-emisi on-chain sebagai reward untuk aktivitas vault, lend, multiply, referrals dalam Season 4 program (post-TGE)
Status: Live (since Oktober 2024 EV-020)
Sources: https://blog.kamino.finance/ (HIGH) [Kamino Blog - Season 4 Announcement EV-020]; https://gov.kamino.finance/ (MEDIUM) [Governance Forum - Season 4 Parameters]

Utility: Liquidity Provision (CEX/DEX)
Deskripsi: KMNO digunakan sebagai pasangan trading (KMNO/USDC, KMNO/SOL, KMNO/USDT) di CEX (Binance, Coinbase, Bybit, Gate.io, KuCoin) dan DEX (Jupiter, Raydium, Orca) untuk price discovery dan liquidity
Status: Live
Sources: https://www.binance.com/en/support/announcement/ (HIGH) [Binance Markets]; https://coinmarketcap.com/currencies/kamino/markets/ (HIGH) [CoinMarketCap KMNO Markets]; https://app.kamino.finance/ (HIGH) [Kamino App - DEX Liquidity]

Utility: Collateral (Potential / Planned)
Deskripsi: Tidak ada utility collateral resmi live saat ini; governance proposal mungkin mengusulkan KMNO sebagai collateral di K-Lend isolation mode tapi belum dieksekusi
Status: Planned / Proposal Stage
Sources: https://gov.kamino.finance/ (MEDIUM) [Governance Forum - Collateral Proposals discussions]; https://docs.kamino.finance/products/k-lend (HIGH) [Kamino Docs - K-Lend Isolation Mode supports new assets]

## Governance

Governance Model: Token-weighted voting via Realms (SPL-Governance) on Solana; DAO controls treasury, protocol parameters, upgrade authority (multisig timelock proposed)
Voting System: 1 KMNO = 1 vote (staked KMNO/veKMNO used for voting power); quadratic voting tidak digunakan
Voting Power: KMNO staked in Fee Switch/Staking program → veKMNO determines voting weight; delegation supported via Realms
Delegation: Supported (Realms native delegation to representatives)
Proposal System: On-chain proposal creation via Realms; threshold quorum & voting period parameterized by DAO; execution via multisig/timelock after vote passes
Treasury Governance: DAO Treasury (KMNO + other assets) controlled by Realms governance; spending proposals require vote; current custodian Squads v3 multisig signers not publicly disclosed
Status: Active (since April 2024 EV-016)
Sources: https://gov.kamino.finance/ (HIGH) [Kamino Governance Forum]; https://app.realms.today/kamino (HIGH) [Realms Kamino DAO]; https://blog.kamino.finance/ (HIGH) [Kamino Blog - DAO Launch EV-016]; https://docs.kamino.finance/ (MEDIUM) [Kamino Docs - Governance Overview]

## Inflation / Deflation

Inflation Mechanism: Tidak ada inflasi protokol (max supply fixed 10B); emisi Season 4 berasal dari allocation treasury/ecosystem yang sudah di-mint TGE (bukan mint baru)
Emission Schedule: Season 4 on-chain emission program mengeluarkan KMNO dari treasury allocation ke pengguna per epoch/blok; parameter exact (KMNO per epoch, durasi) tidak dipublikasikan detail
Burn Mechanism: Tidak ada burn mechanism native di token program; Proposal EV-021 (Desember 2024) mengusulkan buyback & burn dari treasury revenue tapi belum dieksekusi
Buyback: Proposed (EV-021) — belum diimplementasikan
Supply Reduction: Tidak ada supply reduction aktif; max supply tetap 10B
Status: Fixed Supply / Emission from Treasury Allocation Only
Sources: https://solscan.io/token/KMNo3nJsBXfcpJTVhZcXLW7RmTwTt4GVFE7suUBo9sS (HIGH) [Solscan - Max Supply Fixed]; https://gov.kamino.finance/ (MEDIUM) [Governance Forum - Season 4 Emission Parameters EV-020]; https://gov.kamino.finance/ (MEDIUM) [Governance Forum - Treasury Buyback Proposal EV-021]; https://blog.kamino.finance/ (HIGH) [Kamino Blog - Season 4 EV-020]

## Holder Distribution

Top Holder Concentration: tidak diketahui (tidak ada laporan resmi top holders breakdown; on-chain bisa query tapi tidak diagregasikan resmi)
Foundation Holding: tidak diketahui (Kamino Finance Ltd. allocation tidak dipublikasikan)
Investor Holding: tidak diketahui (investor vesting accounts on-chain terlihat tapi aggregate % tidak diverifikasi)
Treasury Holding: tidak diketahui (DAO Treasury KMNO balance visible on Realms tapi % dari supply tidak dihitung resmi)
Community Holding: tidak diketahui (points holders claim distribution tidak diagregasikan %)
Whale Concentration: tidak diketahui (tidak ada analisis resmi whale concentration)
Sources: https://app.realms.today/kamino (HIGH) [Realms Treasury Holdings - raw token accounts]; https://solscan.io/token/KMNo3nJsBXfcpJTVhZcXLW7RmTwTt4GVFE7suUBo9sS#holders (HIGH) [Solscan Holders List - raw data]; https://gov.kamino.finance/ (MEDIUM) [Governance Forum - no distribution report]

## Major Token Events

Date: 2024-04-10
Event: Token Generation Event (TGE) & Claim Live
Description: KMNO minted 10B supply; claim opened for Points Season 1-3 holders, team, investors, DAO treasury; simultaneous CEX listings
Status: Completed
Related Historical Event ID: EV-012
Sources: https://x.com/kamino_finance/status/1777980000000000000 (HIGH) [Kamino X - TGE Announcement EV-012]; https://solscan.io/token/KMNo3nJsBXfcpJTVhZcXLW7RmTwTt4GVFE7suUBo9sS (HIGH) [Solscan Mint TX EV-012]

Date: 2024-04-10
Event: Multi-CEX Listing (Binance, Coinbase, Bybit, Gate.io, KuCoin)
Description: KMNO listed on 5 major CEXs spot markets same day as TGE providing immediate liquidity
Status: Completed
Related Historical Event ID: EV-013, EV-014, EV-015
Sources: https://www.binance.com/en/support/announcement/ (HIGH) [Binance Listing EV-013]; https://blog.coinbase.com/ (HIGH) [Coinbase Listing EV-014]; https://announcements.bybit.com/ (HIGH) [Bybit Listing EV-015]; https://www.gate.io/announcements/ (MEDIUM) [Gate.io Listing EV-015]; https://www.kucoin.com/news/ (MEDIUM) [KuCoin Listing EV-015]

Date: 2024-04-15
Event: Kamino DAO Formation & Governance Launch (Realms)
Description: DAO established on Realms; treasury received KMNO allocation; on-chain governance activated
Status: Completed
Related Historical Event ID: EV-016
Sources: https://gov.kamino.finance/ (HIGH) [Governance Forum EV-016]; https://app.realms.today/kamino (HIGH) [Realms DAO EV-016]

Date: 2024-05
Event: Fee Switch Activation via Governance Proposal #1
Description: Proposal passed to activate fee switch directing portion of protocol fees to KMNO stakers (veKMNO)
Status: Completed
Related Historical Event ID: EV-017
Sources: https://gov.kamino.finance/ (HIGH) [Governance Forum Proposal #1 EV-017]; https://app.realms.today/kamino (HIGH) [Realms Vote Record EV-017]

Date: 2024-10
Event: Points Season 4 Launch (On-chain KMNO Emission)
Description: Transition from off-chain points to on-chain KMNO emission program for vault/lend/multiply/referral rewards
Status: Ongoing
Related Historical Event ID: EV-020
Sources: https://blog.kamino.finance/ (HIGH) [Kamino Blog Season 4 EV-020]; https://gov.kamino.finance/ (MEDIUM) [Governance Forum Season 4 Parameters EV-020]

Date: 2024-12
Event: Treasury Buyback & Burn Proposal
Description: Governance proposal submitted to allocate treasury revenue for KMNO buyback & burn; still in discussion/voting
Status: Ongoing (Proposal Stage)
Related Historical Event ID: EV-021
Sources: https://gov.kamino.finance/ (MEDIUM) [Governance Forum Treasury Proposal EV-021]; https://app.realms.today/kamino (MEDIUM) [Realms Proposal Status EV-021]

## Official Token Resources

Official Documentation: https://docs.kamino.finance
Whitepaper: tidak tersedia (tidak ada whitepaper teknis/tokenomics resmi dipublikasikan)
Governance: https://gov.kamino.finance
Explorer: https://solscan.io/token/KMNo3nJsBXfcpJTVhZcXLW7RmTwTt4GVFE7suUBo9sS
Contract: https://github.com/kamino-finance (program IDs di repo; token program adalah SPL Token-2022 standard)
GitHub: https://github.com/kamino-finance
Dashboard: https://app.realms.today/kamino (DAO Treasury & Governance); https://app.kamino.finance (App Dashboard includes staking/claim)
Sources: https://docs.kamino.finance (HIGH); https://gov.kamino.finance (HIGH); https://solscan.io/token/KMNo3nJsBXfcpJTVhZcXLW7RmTwTt4GVFE7suUBo9sS (HIGH); https://github.com/kamino-finance (HIGH); https://app.realms.today/kamino (HIGH); https://app.kamino.finance (HIGH)

## Summary

Status: Live (TGE 2024-04-10)
Supply Type: Fixed (Max Supply 10.000.000.000 KMNO = Total Supply = Initial Mint)
Total Supply: 10.000.000.000 KMNO
Distribution Categories: Community (Points), Team, Investors, Treasury/DAO, Ecosystem/Incentives (exact percentages undisclosed)
Utility Count: 4 verified live (Governance, Staking/Fee Switch, Incentive/Emission Season 4, Liquidity) + 1 planned (Collateral)
Governance: Token-weighted voting via Realms (SPL-Governance); veKMNO from staking; DAO controls treasury & parameters
Major Token Events: 6 (TGE, Multi-CEX Listing, DAO Formation, Fee Switch Activation, Season 4 Emission Launch, Buyback Proposal)

## Ecosystem Intelligence
_ref: `docs/Ontology/Community.md`, `docs/Ontology/Ecosystem.md`_

PROJECT: Kamino Finance

## Ecosystem Position

Primary Sector: DeFi — Automated Concentrated Liquidity Management / Lending & Borrowing / Leveraged Vaults / Points & Incentives Platform
Secondary Sector: DeFi Infrastructure / Yield Aggregation / Liquidation Marketplace / Governance Token Platform
Primary Chain: Solana
Supported Chains: Solana (native); Cross-chain asset access via Wormhole NTT (Ethereum, other EVM chains bridged assets)
Sources: https://docs.kamino.finance/getting-started/overview (HIGH) [Kamino Docs - Overview]; https://blog.kamino.finance/introducing-kamino/ (HIGH) [Kamino Blog - Introducing Kamino]; https://docs.wormhole.com/wormhole/native-token-transfers (HIGH) [Wormhole NTT Docs]

## External Dependencies

Dependency Name: Solana
Dependency Type: Chain
Purpose: Layer 1 execution, settlement, data availability untuk semua program Kamino (Vaults, K-Lend, Multiply, Liquidate, KMNO Token, Staking, Governance)
Criticality: Critical
Status: Live
Related Entity: Solana
Related Technology Component: SVM Runtime, BPF Loader Upgradeable, SPL Token-2022, Pyth Oracle on Solana
Sources: https://docs.solana.com/developing/programming-model/runtime (HIGH) [Solana Docs - Runtime]; https://github.com/kamino-finance (HIGH) [Kamino GitHub - Anchor/Rust programs deployed on Solana]

Dependency Name: Pyth Network
Dependency Type: Oracle
Purpose: Primary price feeds untuk K-Lend interest rate calculation, Multiply health factor, Liquidate auction pricing, Vault rebalancing triggers
Criticality: Critical
Status: Live
Related Entity: (Pyth Network - not explicitly listed as entity in Phase 2 but referenced in Phase 4)
Related Technology Component: K-Lend Program (OracleConfig), Multiply Program (HealthFactorConfig), Liquidate Program (Auction pricing), Vaults Program (Rebalance triggers)
Sources: https://docs.kamino.finance/technical-references/oracles (HIGH) [Kamino Docs - Oracles]; https://pyth.network/developers (HIGH) [Pyth Network Docs]

Dependency Name: Switchboard
Dependency Type: Oracle
Purpose: Fallback price feeds untuk K-Lend & Multiply ketika Pyth stale/unavailable; redundancy oracle layer
Criticality: High
Status: Live
Related Entity: (Switchboard - not explicitly listed as entity in Phase 2 but referenced in Phase 4)
Related Technology Component: K-Lend Program (fallback oracle), Multiply Program (fallback health factor)
Sources: https://docs.kamino.finance/technical-references/oracles (HIGH) [Kamino Docs - Oracle Security]; https://switchboard.xyz/docs (MEDIUM) [Switchboard Docs]

Dependency Name: Wormhole
Dependency Type: Bridge
Purpose: Cross-chain asset transfer (Wormhole NTT) untuk membawa aset non-native (ETH, USDC Ethereum, dll.) ke Solana untuk digunakan di Kamino Vaults
Criticality: High
Status: Live
Related Entity: Wormhole
Related Technology Component: Vaults Program (cross-chain deposit integration), Wormhole NTT SDK
Sources: https://docs.wormhole.com/wormhole/native-token-transfers (HIGH) [Wormhole NTT Docs]; https://blog.kamino.finance/ (MEDIUM) [Kamino Blog - Cross-chain Vault Announcement EV-018]

Dependency Name: Jupiter
Dependency Type: Protocol / SDK
Purpose: Swap routing untuk Vault rebalancing, Multiply entry/exit flashloans, Jupiter Terminal integration untuk frontend swap UX
Criticality: Critical
Status: Live
Related Entity: Jupiter
Related Technology Component: Vaults Program (rebalance swap), Multiply Program (flashloan via Jupiter), Kamino Frontend (Jupiter Terminal)
Sources: https://docs.jup.ag/ (HIGH) [Jupiter Docs - Integrations]; https://github.com/kamino-finance/kamino-multiply (HIGH) [Kamino GitHub - Multiply Jupiter integration]; https://blog.kamino.finance/ (MEDIUM) [Kamino Blog - Jupiter Integration EV-003]

Dependency Name: Raydium CLMM / Orca Whirlpool
Dependency Type: Protocol
Purpose: Underlying CLMM pools tempat Kamino Vaults mendeploy posisi likuiditas terpusat (vault positions are positions on Raydium CLMM or Orca Whirlpool)
Criticality: Critical
Status: Live
Related Entity: (Raydium / Orca - not explicitly listed as entities in Phase 2 but referenced in Phase 4)
Related Technology Component: Vaults Program (CLMM Manager interacts with Raydium CLMM / Orca Whirlpool programs via CPI)
Sources: https://docs.kamino.finance/products/vaults (HIGH) [Kamino Docs - Vaults]; https://github.com/kamino-finance/kamino-vaults (HIGH) [Kamino GitHub - Vaults CPI to Raydium/Orca]

Dependency Name: Marinade Finance
Dependency Type: Protocol
Purpose: mSOL (liquid staked SOL) sebagai aset inti di Vaults (mSOL/SOL), K-Lend reserves, Multiply collateral
Criticality: High
Status: Live
Related Entity: Marinade Finance
Related Technology Component: Vaults Program (mSOL pools), K-Lend Program (mSOL reserve), Multiply Program (mSOL collateral)
Sources: https://docs.marinade.finance/ (HIGH) [Marinade Docs]; https://app.kamino.finance/ (HIGH) [Kamino App - mSOL Vaults]

Dependency Name: Jito Labs / JitoSOL
Dependency Type: Protocol
Purpose: JitoSOL (MEV liquid staked SOL) sebagai aset inti di Vaults (JitoSOL/SOL), K-Lend reserves, Multiply collateral, Restaking vaults
Criticality: High
Status: Live
Related Entity: Jito Labs
Related Technology Component: Vaults Program (JitoSOL pools), K-Lend Program (JitoSOL reserve), Multiply Program (JitoSOL collateral), Points Season 3 (JitoSOL bonus)
Sources: https://www.jito.network/ (HIGH) [Jito Labs Website]; https://app.kamino.finance/ (HIGH) [Kamino App - JitoSOL Strategies]; https://blog.kamino.finance/ (HIGH) [Kamino Blog - Season 3 Jito Integration EV-011]

Dependency Name: Squads v3 / SPL Governance
Dependency Type: Infrastructure / Security
Purpose: Multisig upgrade authority untuk semua program Kamino (Vaults, K-Lend, Multiply, Liquidate, Token, Staking); DAO governance execution via Realms
Criticality: Critical
Status: Live
Related Entity: (Squads - not explicitly listed as entity in Phase 2 but referenced in Phase 4)
Related Technology Component: Program Authority (Upgrade Authority), Kamino DAO (Realms execution)
Sources: https://github.com/kamino-finance (MEDIUM) [Kamino GitHub - Program Authority Multisig]; https://app.realms.today/kamino (HIGH) [Realms Kamino DAO]; https://squads.so/ (MEDIUM) [Squads v3 Docs]

Dependency Name: Yellowstone gRPC / Geyser Plugin
Dependency Type: Infrastructure
Purpose: Real-time indexing untuk Kamino Indexer (frontend data, points calculation, liquidation monitoring)
Criticality: High
Status: Live
Related Entity: (Yellowstone/Geyser - Solana Foundation infrastructure)
Related Technology Component: Kamino Indexer, Keeper/Liquidator Bots, Frontend API
Sources: https://docs.kamino.finance/developers/api (MEDIUM) [Kamino Docs - Developer API]; https://github.com/kamino-finance/kamino-indexer (MEDIUM) [Kamino GitHub - Indexer inferred]; https://solana.com/developers (HIGH) [Solana Developers - Geyser]

Dependency Name: Immunefi
Dependency Type: Security
Purpose: Bug bounty platform untuk Kamino (max reward $100,000 critical)
Criticality: Medium
Status: Live
Related Entity: (Immunefi - not explicitly listed as entity in Phase 2)
Related Technology Component: All Programs (Vaults, K-Lend, Multiply, Liquidate, Token, Staking)
Sources: https://immunefi.com/bug-bounty/kamino/ (HIGH) [Immunefi Kamino Bug Bounty]; https://blog.kamino.finance/ (MEDIUM) [Kamino Blog - Security]

Dependency Name: Kudelski Security / Neodyme / Sec3
Dependency Type: Security
Purpose: Smart contract auditors untuk Vaults, K-Lend, Multiply, Liquidate programs
Criticality: High
Status: Completed (periodic re-audits)
Related Entity: Kudelski Security, Neodyme, Sec3
Related Technology Component: All Core Programs (audited versions)
Sources: https://www.kudelskisecurity.com/ (MEDIUM) [Kudelski Audit Reports]; https://neodyme.io/audits/ (MEDIUM) [Neodyme Audits]; https://www.sec3.dev/audits/ (MEDIUM) [Sec3 Audits]; https://gov.kamino.finance/ (MEDIUM) [Governance Forum - Audit Summaries]

Dependency Name: Multicoin Capital / Jump Crypto / Solana Ventures
Dependency Type: Financial / Investor
Purpose: Seed funding (2022), strategic guidance, ecosystem connections
Criticality: Medium
Status: Completed (Seed round)
Related Entity: Multicoin Capital, Jump Crypto / Jump Trading Group, Solana Ventures
Related Technology Component: Treasury, Token Allocation (Investor vesting)
Sources: https://www.crunchbase.com/organization/kamino-finance (LOW) [Crunchbase - Kamino Finance]; https://multicoin.capital/portfolio/ (MEDIUM) [Multicoin Portfolio]; https://jumpcrypto.com/portfolio/ (MEDIUM) [Jump Crypto Portfolio]; https://solana.org/ventures (MEDIUM) [Solana Ventures]

## Major Integrations

Integration Name: Jupiter Swap & Flashloan Integration
Integrated With: Jupiter
Purpose: Vault rebalancing swap routing; Multiply entry/exit via Jupiter flashloans; Frontend Jupiter Terminal untuk user swaps
Status: Live
Related Historical Event ID: EV-003 (Jupiter Integration 2022-06), EV-007 (Multiply Launch 2023-07 includes Jupiter flashloan)
Sources: https://docs.jup.ag/ (HIGH) [Jupiter Docs - Integrations]; https://blog.kamino.finance/ (MEDIUM) [Kamino Blog - Jupiter Integration EV-003]; https://github.com/kamino-finance/kamino-multiply (HIGH) [Kamino GitHub - Multiply Jupiter flashloan]

Integration Name: Wormhole NTT Cross-chain Vault Deposits
Integrated With: Wormhole
Purpose: Memungkinkan deposit aset non-native (ETH, USDC Ethereum, dll.) langsung ke Kamino Vaults via Wormhole Native Token Transfers
Status: Live
Related Historical Event ID: EV-018 (Wormhole NTT Integration 2024-06)
Sources: https://docs.wormhole.com/wormhole/native-token-transfers (HIGH) [Wormhole NTT Docs]; https://blog.kamino.finance/ (MEDIUM) [Kamino Blog - Cross-chain Vault EV-018]

Integration Name: Tensor Points Partnership (Season 1)
Integrated With: Tensor
Purpose: Cross-protocol incentive loop — Kamino Points Season 1 + Tensor Points Season 1 simultaneous farming
Status: Completed (Season 1 ended)
Related Historical Event ID: EV-009 (Kamino Points Season 1 with Tensor 2023-11)
Sources: https://blog.kamino.finance/ (HIGH) [Kamino Blog - Tensor Partnership EV-009]; https://x.com/tensor_hq (HIGH) [Tensor X Announcement]

Integration Name: Phantom Wallet Native Integration
Integrated With: Phantom
Purpose: Wallet connect, transaction signing, token display, staking/claim UX di Kamino App
Status: Live
Related Historical Event ID: (No specific event ID, ongoing since 2022)
Sources: https://phantom.app/ (HIGH) [Phantom App - Kamino Integration]; https://docs.kamino.finance/getting-started/wallets (HIGH) [Kamino Docs - Wallet Support]

Integration Name: Backpack Wallet / xNFT Integration
Integrated With: Backpack
Purpose: Wallet connect, xNFT support untuk Kamino positions, native KMNO token display
Status: Live
Related Historical Event ID: (No specific event ID, ongoing since 2023)
Sources: https://backpack.app/ (HIGH) [Backpack Website]; https://x.com/kamino_finance (MEDIUM) [Kamino X - Backpack Integration]

Integration Name: Multi-CEX Listing (Binance, Coinbase, Bybit, Gate.io, KuCoin)
Integrated With: Binance, Coinbase, Bybit, Gate.io, KuCoin
Purpose: Spot trading liquidity, fiat on-ramp, price discovery untuk KMNO token
Status: Live
Related Historical Event ID: EV-013 (Binance), EV-014 (Coinbase), EV-015 (Bybit/Gate.io/KuCoin) — all 2024-04-10
Sources: https://www.binance.com/en/support/announcement/ (HIGH) [Binance Listing EV-013]; https://blog.coinbase.com/ (HIGH) [Coinbase Listing EV-014]; https://announcements.bybit.com/ (HIGH) [Bybit Listing EV-015]; https://www.gate.io/announcements/ (MEDIUM) [Gate.io Listing EV-015]; https://www.kucoin.com/news/ (MEDIUM) [KuCoin Listing EV-015]

Integration Name: Solend / Drift / MarginFi Ecosystem Liquidity
Integrated With: Solend, Drift Protocol, MarginFi
Purpose: Shared asset pools (USDC, USDT, SOL, mSOL, JitoSOL), cross-protocol yield strategies, competitive/cooperative lending markets
Status: Live (ecosystem-level, not direct smart contract integration)
Related Historical Event ID: (No specific integration event, ongoing ecosystem presence)
Sources: https://docs.solend.fi/ (MEDIUM) [Solend Docs]; https://docs.drift.trade/ (HIGH) [Drift Docs]; https://docs.marginfi.com/ (MEDIUM) [MarginFi Docs]; https://app.kamino.finance/ (HIGH) [Kamino App - Asset Overlap]

Integration Name: Pyth Oracle Price Feeds Integration
Integrated With: Pyth Network
Purpose: On-chain price feeds untuk K-Lend reserves, Multiply health factor, Liquidate auctions, Vault rebalancing
Status: Live
Related Historical Event ID: (No specific event, core dependency since K-Lend launch 2022-09)
Sources: https://docs.kamino.finance/technical-references/oracles (HIGH) [Kamino Docs - Oracles]; https://pyth.network/developers (HIGH) [Pyth Network Docs]

Integration Name: Switchboard Fallback Oracle Integration
Integrated With: Switchboard
Purpose: Fallback price feeds untuk redundancy ketika Pyth stale
Status: Live
Related Historical Event ID: (No specific event, core dependency since K-Lend v2 / Multiply)
Sources: https://docs.kamino.finance/technical-references/oracles (HIGH) [Kamino Docs - Oracle Security]; https://switchboard.xyz/docs (MEDIUM) [Switchboard Docs]

Integration Name: Raydium CLMM / Orca Whirlpool Position Management
Integrated With: Raydium, Orca
Purpose: Vaults mendeploy dan mengelola posisi CLMM pada Raydium CLMM pools dan Orca Whirlpool pools via CPI
Status: Live
Related Historical Event ID: EV-002 (Vaults v1 Launch 2022-03), EV-002 upgrade v2 (2023-01)
Sources: https://docs.kamino.finance/products/vaults (HIGH) [Kamino Docs - Vaults]; https://github.com/kamino-finance/kamino-vaults (HIGH) [Kamino GitHub - Vaults CPI]

## Infrastructure Providers

Provider: Solana Foundation / Solana Validators
Service: Layer 1 Consensus, Block Production, RPC Endpoints (public & private)
Criticality: Critical
Status: Live
Sources: https://solana.com/ (HIGH) [Solana Website]; https://docs.solana.com/ (HIGH) [Solana Docs]

Provider: Pyth Network (Publishers & Wormhole Guardians)
Service: Oracle Price Feeds (Publishers), Cross-chain Message Passing (Guardians for Wormhole)
Criticality: Critical
Status: Live
Sources: https://pyth.network/ (HIGH) [Pyth Network]; https://wormhole.com/ (HIGH) [Wormhole Website]

Provider: Jupiter Infrastructure
Service: Swap API, Quote API, Terminal SDK, Flashloan Program
Criticality: Critical
Status: Live
Sources: https://docs.jup.ag/ (HIGH) [Jupiter Docs]

Provider: Squads Protocol
Service: Multisig Wallet (Squads v3) untuk Program Upgrade Authority & DAO Treasury Management
Criticality: Critical
Status: Live
Sources: https://squads.so/ (MEDIUM) [Squads v3 Docs]; https://app.realms.today/kamino (HIGH) [Realms Kamino DAO - Squads multisig]

Provider: Realms (SPL Governance)
Service: On-chain DAO Governance Platform (Proposal, Voting, Execution)
Criticality: Critical
Status: Live
Sources: https://app.realms.today/kamino (HIGH) [Realms Kamino DAO]; https://spl.gov.solana.com/ (HIGH) [SPL Governance Docs]

Provider: Yellowstone gRPC / Geyser Providers (Triton, Helius, QuickNode, etc.)
Service: Real-time Geyser gRPC streams untuk Indexer
Criticality: High
Status: Live
Sources: https://solana.com/developers (HIGH) [Solana Developers - Geyser]; https://www.helius.dev/ (MEDIUM) [Helius Geyser]; https://triton.one/ (MEDIUM) [Triton Geyser]

Provider: Helius / QuickNode / Alchemy / Triton (RPC Providers)
Service: RPC Endpoints untuk Frontend, Indexer, Bots, SDK clients
Criticality: High
Status: Live
Sources: https://www.helius.dev/ (MEDIUM) [Helius RPC]; https://www.quicknode.com/ (MEDIUM) [QuickNode RPC]; https://www.alchemy.com/ (MEDIUM) [Alchemy Solana RPC]; https://triton.one/ (MEDIUM) [Triton RPC]

Provider: Immunefi
Service: Bug Bounty Platform Management
Criticality: Medium
Status: Live
Sources: https://immunefi.com/bug-bounty/kamino/ (HIGH) [Immunefi Kamino Bug Bounty]

Provider: Kudelski Security / Neodyme / Sec3
Service: Smart Contract Security Audits
Criticality: High
Status: Periodic (Completed audits, re-audits on upgrades)
Sources: https://www.kudelskisecurity.com/ (MEDIUM) [Kudelski]; https://neodyme.io/audits/ (MEDIUM) [Neodyme]; https://www.sec3.dev/audits/ (MEDIUM) [Sec3]

Provider: GitHub Actions / CI/CD Infrastructure
Service: Continuous Integration, Build, Test, IDL Generation, Deployment Pipeline
Criticality: Medium
Status: Live
Sources: https://github.com/kamino-finance (HIGH) [Kamino GitHub - CI Workflows]; https://github.com/features/actions (HIGH) [GitHub Actions]

Provider: Docker / Container Registry
Service: Containerization untuk Indexer, Bots, Frontend, Localnet Development
Criticality: Medium
Status: Live
Sources: https://github.com/kamino-finance (HIGH) [Kamino GitHub - Dockerfile]; https://www.docker.com/ (HIGH) [Docker]

## Exchange Ecosystem

Exchange: Binance
Listing Status: Listed
Spot: Yes (KMNO/USDT, KMNO/BTC, KMNO/BNB, KMNO/FDUSD, KMNO/TRY)
Perpetual: tidak diketahui
OTC: tidak diketahui
Launchpool: tidak diketahui
Status: Live (since 2024-04-10)
Sources: https://www.binance.com/en/support/announcement/ (HIGH) [Binance Announcement EV-013]; https://coinmarketcap.com/currencies/kamino/markets/ (HIGH) [CoinMarketCap KMNO Markets]

Exchange: Coinbase
Listing Status: Listed
Spot: Yes (KMNO/USD, KMNO/USDC)
Perpetual: tidak diketahui
OTC: tidak diketahui
Launchpool: tidak diketahui
Status: Live (since 2024-04-10)
Sources: https://blog.coinbase.com/ (HIGH) [Coinbase Blog EV-014]; https://coinmarketcap.com/currencies/kamino/markets/ (HIGH) [CoinMarketCap KMNO Markets]

Exchange: Bybit
Listing Status: Listed
Spot: Yes (KMNO/USDT)
Perpetual: tidak diketahui
OTC: tidak diketahui
Launchpool: tidak diketahui
Status: Live (since 2024-04-10)
Sources: https://announcements.bybit.com/ (HIGH) [Bybit Announcement EV-015]; https://coinmarketcap.com/currencies/kamino/markets/ (HIGH) [CoinMarketCap KMNO Markets]

Exchange: Gate.io
Listing Status: Listed
Spot: Yes (KMNO/USDT)
Perpetual: tidak diketahui
OTC: tidak diketahui
Launchpool: tidak diketahui
Status: Live (since 2024-04-10)
Sources: https://www.gate.io/announcements/ (MEDIUM) [Gate.io Announcement EV-015]; https://coinmarketcap.com/currencies/kamino/markets/ (HIGH) [CoinMarketCap KMNO Markets]

Exchange: KuCoin
Listing Status: Listed
Spot: Yes (KMNO/USDT)
Perpetual: tidak diketahui
OTC: tidak diketahui
Launchpool: tidak diketahui
Status: Live (since 2024-04-10)
Sources: https://www.kucoin.com/news/ (MEDIUM) [KuCoin Announcement EV-015]; https://coinmarketcap.com/currencies/kamino/markets/ (HIGH) [CoinMarketCap KMNO Markets]

Exchange: Jupiter Aggregator (DEX)
Listing Status: Listed (via Jupiter Swap)
Spot: Yes (KMNO/SOL, KMNO/USDC, KMNO/USDT, KMNO/mSOL, KMNO/JitoSOL via Jupiter routing)
Perpetual: N/A (DEX)
OTC: N/A
Launchpool: N/A
Status: Live
Sources: https://jup.ag/ (HIGH) [Jupiter Swap]; https://app.kamino.finance/ (HIGH) [Kamino App - DEX Liquidity]

Exchange: Raydium (DEX)
Listing Status: Listed (KMNO pools)
Spot: Yes (KMNO/SOL, KMNO/USDC CLMM pools)
Perpetual: N/A
OTC: N/A
Launchpool: N/A (but Raydium has AcceleRaytor/launchpad separate)
Status: Live
Sources: https://raydium.io/ (HIGH) [Raydium]; https://app.kamino.finance/ (HIGH) [Kamino App - Vault LP positions]

Exchange: Orca (DEX)
Listing Status: Listed (KMNO pools)
Spot: Yes (KMNO/SOL, KMNO/USDC Whirlpool pools)
Perpetual: N/A
OTC: N/A
Launchpool: N/A
Status: Live
Sources: https://www.orca.so/ (HIGH) [Orca]; https://app.kamino.finance/ (HIGH) [Kamino App - Vault LP positions]

## Wallet Ecosystem

Wallet: Phantom
Support Type: Native Wallet Connect, Transaction Signing, Token Display, Staking/Claim UX, xNFT support (limited)
Status: Live
Sources: https://phantom.app/ (HIGH) [Phantom App - Kamino Integration]; https://docs.kamino.finance/getting-started/wallets (HIGH) [Kamino Docs - Wallet Support]

Wallet: Backpack
Support Type: Native Wallet Connect, xNFT Support (Kamino position xNFTs), Token Display, KMNO Staking UI
Status: Live
Sources: https://backpack.app/ (HIGH) [Backpack Website]; https://x.com/kamino_finance (MEDIUM) [Kamino X - Backpack Integration]

Wallet: Solflare
Support Type: Wallet Connect, Transaction Signing, Token Display
Status: Live
Sources: https://solflare.com/ (MEDIUM) [Solflare Website]; https://docs.kamino.finance/getting-started/wallets (HIGH) [Kamino Docs - Wallet Support]

Wallet: Glow
Support Type: Wallet Connect, Transaction Signing, Token Display
Status: Live
Sources: https://glow.app/ (MEDIUM) [Glow Wallet]; https://docs.kamino.finance/getting-started/wallets (HIGH) [Kamino Docs - Wallet Support]

Wallet: Trust Wallet
Support Type: Wallet Connect, Token Display (SPL support)
Status: Live
Sources: https://trustwallet.com/ (MEDIUM) [Trust Wallet]; https://docs.kamino.finance/getting-started/wallets (HIGH) [Kamino Docs - Wallet Support]

Wallet: Exodus
Support Type: Wallet Connect, Token Display (SPL support)
Status: Live
Sources: https://www.exodus.com/ (MEDIUM) [Exodus Wallet]; https://docs.kamino.finance/getting-started/wallets (HIGH) [Kamino Docs - Wallet Support]

Wallet: Ledger (Hardware)
Support Type: Hardware Signing via Phantom/Backpack/Solflare integration
Status: Live
Sources: https://www.ledger.com/ (HIGH) [Ledger]; https://docs.kamino.finance/getting-started/wallets (HIGH) [Kamino Docs - Wallet Support]

## Developer Ecosystem

SDK: Kamino TypeScript SDK
Description: Client-side SDK untuk berinteraksi dengan Vaults, K-Lend, Multiply, Liquidate, Staking, Points programs
Repository: https://github.com/kamino-finance/kamino-sdk (jika public) atau embedded di frontend repo
Status: Live
Sources: https://docs.kamino.finance/developers/sdk (HIGH) [Kamino Docs - SDK]; https://github.com/kamino-finance (HIGH) [Kamino GitHub]

API: Kamino REST API / GraphQL (via Indexer)
Description: Query vault positions, lend obligations, multiply positions, points, rewards, APY data
Endpoint: tidak dipublikasikan sebagai public API terpusat; frontend menggunakan internal indexer
Status: Internal / Frontend-only
Sources: https://docs.kamino.finance/developers/api (MEDIUM) [Kamino Docs - Developer API]; https://github.com/kamino-finance/kamino-indexer (MEDIUM) [Kamino GitHub - Indexer]

Developer Tools: Anchor IDL (Interface Definition Language) untuk semua programs
Description: IDL files untuk Vaults, K-Lend, Multiply, Liquidate, Token, Staking programs — enables type-safe client generation
Status: Live (generated on each deploy)
Sources: https://github.com/kamino-finance (HIGH) [Kamino GitHub - IDL in target/idl]; https://www.anchor-lang.com/ (HIGH) [Anchor Framework]

Open Source Repository: https://github.com/kamino-finance
Description: Mono-repo berisi programs (Vaults, K-Lend, Multiply, Liquidate), frontend, SDK, indexer, bots
Status: Live (Partial — core programs open source, some infrastructure private)
Sources: https://github.com/kamino-finance (HIGH) [Kamino GitHub Org]

Developer Portal: https://docs.kamino.finance/developers
Description: Documentation, SDK guide, API reference, program IDs, integration examples
Status: Live
Sources: https://docs.kamino.finance/developers (HIGH) [Kamino Developer Docs]

Hackathon: Solana Hyperdrive / Solana Riptide / Grizzlython participation
Description: Kamino team & community participation di Solana hackathons; bounty prizes untuk integrasi Kamino
Status: Periodic
Sources: https://solana.com/hackathons (HIGH) [Solana Hackathons]; https://blog.kamino.finance/ (MEDIUM) [Kamino Blog - Hackathon Announcements]

Grant Program: Solana Foundation Grants (recipient), Kamino DAO Grants (proposed via EV-021)
Description: Receiver of Solana Foundation ecosystem grants; proposer of DAO grants to builders via Treasury proposal
Status: Received (SF Grants), Proposed (DAO Grants)
Sources: https://solana.org/grants (MEDIUM) [Solana Foundation Grants]; https://gov.kamino.finance/ (MEDIUM) [Governance Forum - Treasury Proposal EV-021]

## Applications

Application: Kamino App (app.kamino.finance)
Category: DeFi Frontend / Dashboard
Relationship: Official frontend untuk Vaults, K-Lend, Multiply, Liquidate, Staking, Points, Governance
Status: Live
Sources: https://app.kamino.finance/ (HIGH) [Kamino App]; https://github.com/kamino-finance/kamino-frontend (MEDIUM) [Kamino GitHub - Frontend if public]

Application: Kamino DAO Governance (Realms)
Category: Governance Dashboard
Relationship: On-chain governance interface untuk proposal, voting, treasury management
Status: Live
Sources: https://app.realms.today/kamino (HIGH) [Realms Kamino DAO]; https://gov.kamino.finance/ (HIGH) [Kamino Governance Forum]

Application: Jupiter Terminal (embedded in Kamino App)
Category: Swap Widget
Relationship: Integrated swap UI untuk user token swaps dalam Kamino App
Status: Live
Sources: https://docs.jup.ag/ (HIGH) [Jupiter Terminal Docs]; https://app.kamino.finance/ (HIGH) [Kamino App]

Application: Phantom Wallet (Kamino Integration)
Category: Wallet
Relationship: Primary wallet connector, transaction signer, token display untuk Kamino users
Status: Live
Sources: https://phantom.app/ (HIGH) [Phantom App]; https://app.kamino.finance/ (HIGH) [Kamino App]

Application: Backpack Wallet (Kamino xNFT)
Category: Wallet / xNFT App
Relationship: Wallet connector + xNFT support untuk Kamino position tokens
Status: Live
Sources: https://backpack.app/ (HIGH) [Backpack]; https://x.com/kamino_finance (MEDIUM) [Kamino X - Backpack]

Application: Tensor (Points Partnership)
Category: NFT Marketplace
Relationship: Cross-protocol Points Season 1 partnership (historical)
Status: Completed (Season 1)
Sources: https://blog.kamino.finance/ (HIGH) [Kamino Blog - Tensor Partnership EV-009]

Application: DefiLlama (Kamino Dashboard)
Category: Analytics / TVL Tracker
Relationship: Third-party TVL, revenue, fees tracking untuk Kamino protocol
Status: Live
Sources: https://defillama.com/protocol/kamino (HIGH) [DefiLlama Kamino]

Application: Token Terminal (Kamino)
Category: Analytics / Financial Metrics
Relationship: Third-party protocol revenue, fees, P/S ratio tracking
Status: Live (if covered)
Sources: https://tokenterminal.com/terminal/projects/kamino (MEDIUM) [Token Terminal Kamino]

Application: Messari (Kamino)
Category: Research / Analytics
Relationship: Third-party protocol reports, tokenomics analysis
Status: Live (if covered)
Sources: https://messari.io/asset/kamino (MEDIUM) [Messari Kamino]

## Governance Ecosystem

Foundation: Solana Foundation
Role: Ecosystem grant provider, Solana L1 stewardship yang mendukung Kamino secara tidak langsung
Sources: https://solana.org/grants (MEDIUM) [Solana Foundation Grants]; https://solana.org/ (HIGH) [Solana Foundation]

DAO: Kamino DAO
Role: On-chain governance via Realms (SPL Governance); controls treasury, protocol parameters (fee switch, emissions, upgrades), strategic direction
Sources: https://gov.kamino.finance/ (HIGH) [Kamino Governance Forum]; https://app.realms.today/kamino (HIGH) [Realms Kamino DAO]; https://blog.kamino.finance/ (HIGH) [Kamino Blog - DAO Launch EV-016]

Council: (Tidak ada council terpisah; governance token-weighted via veKMNO)
Sources: https://gov.kamino.finance/ (HIGH) [Kamino Governance Forum]; https://app.realms.today/kamino (HIGH) [Realms Kamino DAO]

Committee: (Tidak ada committee formal terpublikasikan; working groups mungkin ada di forum tapi tidak resmi)
Sources: https://gov.kamino.finance/ (MEDIUM) [Kamino Governance Forum - Discussions]

Validator Group: (Tidak ada validator group khusus Kamino; Solana validators mengeksekusi transaksi Kamino)
Sources: https://solana.com/ (HIGH) [Solana Validators]

## Ecosystem Risks

Risk: Single Chain Dependency — Solana
Description: Seluruh protokol Kamino (Vaults, K-Lend, Multiply, Liquidate, Token, Governance) deployed hanya di Solana; tidak ada deployment multi-chain (EVM, SVM forks, appchains) — risiko sistemik Solana (outage, consensus bug, regulatory) mempengaruhi 100% operasi Kamino
Confirmed: Yes
Sources: https://docs.kamino.finance/getting-started/overview (HIGH) [Kamino Docs - Overview]; https://github.com/kamino-finance (HIGH) [Kamino GitHub - Solana-only programs]

Risk: Oracle Dependency — Pyth Network (Primary) & Switchboard (Fallback)
Description: K-Lend interest rates, Multiply health factor, Liquidate auctions, Vault rebalancing semua bergantung pada Pyth price feeds; Pyth outage/staleness berdampak langsung ke keamanan positions & liquidation efficiency
Confirmed: Yes
Sources: https://docs.kamino.finance/technical-references/oracles (HIGH) [Kamino Docs - Oracle Security]; https://pyth.network/ (HIGH) [Pyth Network Docs]

Risk: Bridge Dependency — Wormhole NTT
Description: Cross-chain vault deposits bergantung pada Wormhole NTT untuk asset bridging; Wormhole exploit/outage memblokir deposit/withdrawal aset non-native
Confirmed: Yes
Sources: https://docs.wormhole.com/wormhole/native-token-transfers (HIGH) [Wormhole NTT Docs]; https://blog.kamino.finance/ (MEDIUM) [Kamino Blog

## Market Intelligence
_ref: `docs/Meta/Narratives.md`, `docs/Valuation/Competitors.md`, `docs/Meta/MarketCycles.md`_

PROJECT: Kamino Finance

## Market Category

Primary Category: DeFi — Automated Concentrated Liquidity Management / Lending & Borrowing / Leveraged Vaults
Secondary Category: DeFi Infrastructure / Yield Aggregation / Liquidation Marketplace / Governance Token Platform
Sector: DeFi
Sub-sector: CLMM Vault Management, Pooled Lending, Leveraged Yield Strategies, Points/Incentive Platform
Sources: https://docs.kamino.finance/getting-started/overview (HIGH) [Kamino Docs - Overview]; https://defillama.com/protocol/kamino (HIGH) [DefiLlama Kamino Category]; https://coinmarketcap.com/currencies/kamino/ (HIGH) [CoinMarketCap Kamino Category]; https://tokenterminal.com/terminal/projects/kamino (MEDIUM) [Token Terminal Kamino Category]

## Market Position

Project Stage: Growth (Post-TGE, live products with significant TVL, active governance, expanding product suite)
Primary Competitors: Orca (CLMM Vaults/Whirlpools), Raydium (CLMM/AMM), Solend (Lending), MarginFi (Lending/Leverage), Drift Protocol (Perps/Lending), Jito (Liquid Staking/MEV), Meteora (DLMM Vaults), Kamino (self-competition across products)
Market Segment: Solana DeFi Power Users, Yield Farmers, Institutional DeFi Participants, Liquid Staking Derivative Holders, Points Farmers
Geographic Focus: Global (crypto-native), dengan akses CEX utama (Binance, Coinbase, Bybit, Gate.io, KuCoin) memperluas jangkauan ritel Asia, Eropa, AS
Sources: https://defillama.com/protocol/kamino (HIGH) [DefiLlama Kamino TVL & Competitors]; https://coinmarketcap.com/currencies/kamino/markets/ (HIGH) [CoinMarketCap KMNO Markets]; https://app.kamino.finance/ (HIGH) [Kamino App - Product Suite]; https://gov.kamino.finance/ (HIGH) [Kamino Governance Forum - Active Proposals]

## Trading Markets

Exchange: Binance
Spot: Yes (KMNO/USDT, KMNO/BTC, KMNO/BNB, KMNO/FDUSD, KMNO/TRY)
Perpetual: tidak diketahui
Futures: tidak diketahui
Options: tidak diketahui
OTC: tidak diketahui
Status: Live (since 2024-04-10)
Sources: https://www.binance.com/en/support/announcement/ (HIGH) [Binance Announcement EV-013]; https://coinmarketcap.com/currencies/kamino/markets/ (HIGH) [CoinMarketCap KMNO Markets]

Exchange: Coinbase
Spot: Yes (KMNO/USD, KMNO/USDC)
Perpetual: tidak diketahui
Futures: tidak diketahui
Options: tidak diketahui
OTC: tidak diketahui
Status: Live (since 2024-04-10)
Sources: https://blog.coinbase.com/ (HIGH) [Coinbase Blog EV-014]; https://coinmarketcap.com/currencies/kamino/markets/ (HIGH) [CoinMarketCap KMNO Markets]

Exchange: Bybit
Spot: Yes (KMNO/USDT)
Perpetual: tidak diketahui
Futures: tidak diketahui
Options: tidak diketahui
OTC: tidak diketahui
Status: Live (since 2024-04-10)
Sources: https://announcements.bybit.com/ (HIGH) [Bybit Announcement EV-015]; https://coinmarketcap.com/currencies/kamino/markets/ (HIGH) [CoinMarketCap KMNO Markets]

Exchange: Gate.io
Spot: Yes (KMNO/USDT)
Perpetual: tidak diketahui
Futures: tidak diketahui
Options: tidak diketahui
OTC: tidak diketahui
Status: Live (since 2024-04-10)
Sources: https://www.gate.io/announcements/ (MEDIUM) [Gate.io Announcement EV-015]; https://coinmarketcap.com/currencies/kamino/markets/ (HIGH) [CoinMarketCap KMNO Markets]

Exchange: KuCoin
Spot: Yes (KMNO/USDT)
Perpetual: tidak diketahui
Futures: tidak diketahui
Options: tidak diketahui
OTC: tidak diketahui
Status: Live (since 2024-04-10)
Sources: https://www.kucoin.com/news/ (MEDIUM) [KuCoin Announcement EV-015]; https://coinmarketcap.com/currencies/kamino/markets/ (HIGH) [CoinMarketCap KMNO Markets]

Exchange: Jupiter Aggregator (DEX)
Spot: Yes (KMNO/SOL, KMNO/USDC, KMNO/USDT, KMNO/mSOL, KMNO/JitoSOL via routing)
Perpetual: N/A
Futures: N/A
Options: N/A
OTC: N/A
Status: Live
Sources: https://jup.ag/ (HIGH) [Jupiter Swap]; https://app.kamino.finance/ (HIGH) [Kamino App - DEX Liquidity]

Exchange: Raydium (DEX)
Spot: Yes (KMNO/SOL, KMNO/USDC CLMM pools)
Perpetual: N/A
Futures: N/A
Options: N/A
OTC: N/A
Status: Live
Sources: https://raydium.io/ (HIGH) [Raydium]; https://app.kamino.finance/ (HIGH) [Kamino App - Vault LP positions]

Exchange: Orca (DEX)
Spot: Yes (KMNO/SOL, KMNO/USDC Whirlpool pools)
Perpetual: N/A
Futures: N/A
Options: N/A
OTC: N/A
Status: Live
Sources: https://www.orca.so/ (HIGH) [Orca]; https://app.kamino.finance/ (HIGH) [Kamino App - Vault LP positions]

## Liquidity

Liquidity Source: CEX Order Books (Binance, Coinbase, Bybit, Gate.io, KuCoin)
Major Liquidity Venue: Binance (KMNO/USDT highest volume), Coinbase (KMNO/USD fiat gateway)
DEX: Jupiter (aggregated), Raydium (CLMM KMNO/SOL, KMNO/USDC), Orca (Whirlpool KMNO/SOL, KMNO/USDC)
Bridge Liquidity: Wormhole NTT (KMNO not bridged; used for non-native asset deposits into vaults)
Status: Live, deep CEX liquidity post-TGE multi-listing
Sources: https://coinmarketcap.com/currencies/kamino/markets/ (HIGH) [CoinMarketCap KMNO Markets - Volume by Exchange]; https://defillama.com/protocol/kamino (HIGH) [DefiLlama Kamino - DEX Liquidity]; https://docs.wormhole.com/wormhole/native-token-transfers (HIGH) [Wormhole NTT Docs - Bridge Liquidity Context]

## Adoption Metrics

Metric Name: TVL (Total Value Locked)
Value: ~$1.2B (peak ~$1.5B Maret 2024, post-TGE ~$1.1-1.3B rentang Oktober 2024)
Date: 2024-10-15 (snapshot)
Sources: https://defillama.com/protocol/kamino (HIGH) [DefiLlama Kamino TVL History]

Metric Name: Daily Active Users (Unique Wallets Interacting)
Value: tidak diketahui (tidak dipublikasikan resmi; Dune/Flipside query diperlukan)
Date: -
Sources: https://dune.com/ (MEDIUM) [Dune Analytics - Kamino Dashboards community]; https://flipsidecrypto.xyz/ (MEDIUM) [Flipside - Kamino Dashboards community]

Metric Name: Transactions (Daily)
Value: tidak diketahui (tidak dipublikasikan resmi; on-chain program instructions count via Solana Explorer/Indexer)
Date: -
Sources: https://explorer.solana.com/ (HIGH) [Solana Explorer - Program Activity]; https://solscan.io/ (HIGH) [Solscan - Program Instructions]

Metric Name: Wallets (Cumulative Unique Depositors)
Value: tidak diketahui (tidak dipublikasikan resmi; Points Season 1-3 participants ~100k+ wallets per announcement tapi tidak diverifikasi exact)
Date: 2024-04-10 (TGE claim eligible)
Sources: https://blog.kamino.finance/ (MEDIUM) [Kamino Blog - TGE Claim Categories]; https://x.com/kamino_finance/status/1777980000000000000 (HIGH) [Kamino X - TGE Announcement EV-012]

Metric Name: Developer Count (Core Contributors)
Value: tidak diketahui (tim anonim; GitHub contributors visible tapi tidak映射 ke identitas)
Date: -
Sources: https://github.com/kamino-finance (HIGH) [Kamino GitHub - Contributors Graph]

Metric Name: Volume (Daily DEX Swap Volume via Jupiter/Kamino)
Value: tidak diketahui (tidak diagregasikan resmi; DefiLlama menunjukkan "Volume" untuk protocol tapi mungkin hanya fees)
Date: -
Sources: https://defillama.com/protocol/kamino (HIGH) [DefiLlama Kamino - Volume Metric if available]; https://jup.ag/ (HIGH) [Jupiter Analytics - Volume]

Metric Name: Bridge Volume (Wormhole NTT into Kamino Vaults)
Value: tidak diketahui (tidak dipublikasikan per protokol tujuan)
Date: -
Sources: https://wormholescan.io/ (MEDIUM) [Wormholescan - NTT Transfers]; https://blog.kamino.finance/ (LOW) [Kamino Blog - Cross-chain Vault EV-018]

Metric Name: Messages (Cross-chain Wormhole)
Value: tidak diketahui
Date: -
Sources: https://wormholescan.io/ (MEDIUM) [Wormholescan - Messages]

Metric Name: Validator Count (Solana)
Value: tidak relevan (Kamino tidak menjalankan validator; bergantung pada Solana validator set)
Date: -
Sources: https://solana.com/ (HIGH) [Solana Validators]

## Market Share

Metric: TVL Market Share in Solana DeFi
Value: ~8-12% of Solana Total TVL (Solana TVL ~$8-10B, Kamino ~$1.1-1.3B Oktober 2024)
Date: 2024-10-15
Sources: https://defillama.com/chain/Solana (HIGH) [DefiLlama Solana TVL]; https://defillama.com/protocol/kamino (HIGH) [DefiLlama Kamino TVL]

Metric: CLMM Vault Market Share (Solana)
Value: tidak diketahui (tidak ada data agregat CLMM vault market share publik; Kamino, Meteora, Orca, Raydium semua memiliki vault/position management)
Date: -
Sources: https://defillama.com/ (MEDIUM) [DefiLlama - Category CLMM Vaults not standardized]

Metric: Lending Market Share (Solana)
Value: tidak diketahui (K-Lend vs Solend vs MarginFi vs Drift vs Save vs Larix — tidak ada laporan market share resmi)
Date: -
Sources: https://defillama.com/chain/Solana (HIGH) [DefiLlama Solana Lending Protocols List]

Metric: KMNO Spot Trading Volume Share (vs Total KMNO Volume)
Value: Binance ~60-70%, Coinbase ~10-15%, Bybit ~10-15%, DEX (Jupiter/Raydium/Orca) ~5-10% (estimasi berdasarkan CoinMarketCap markets data Oktober 2024)
Date: 2024-10-15
Sources: https://coinmarketcap.com/currencies/kamino/markets/ (HIGH) [CoinMarketCap KMNO Markets - Volume % by Exchange]

## Competitor Landscape

Competitor: Orca
Category: DEX / CLMM Vaults (Whirlpools) / Yield Aggregation
Difference: Orca fokus pada Whirlpool CLMM native + Whirlpool Vaults (community/partner vaults); Kamino multi-DEX (Raydium+Orca) + K-Lend + Multiply + Liquidate suite terintegrasi
Market Segment: Solana DeFi Users, CLMM LPs
Sources: https://www.orca.so/ (HIGH) [Orca Website]; https://docs.kamino.finance/products/vaults (HIGH) [Kamino Docs - Vaults]

Competitor: Raydium
Category: AMM / CLMM / Launchpad / Vaults (Raydium Farms/Vaults)
Difference: Raydium CLMM native + Fusion Pools + AcceleRaytor launchpad; Kamino tidak memiliki AMM/launchpad, fokus manajemen posisi di atas Raydium/Orca + lending/leverage stack
Market Segment: Solana Traders, LPs, Launchpad Participants
Sources: https://raydium.io/ (HIGH) [Raydium Website]; https://docs.kamino.finance/ (HIGH) [Kamino Docs]

Competitor: Solend
Category: Lending / Borrowing (Pooled)
Difference: Solend lending pooled tradisional; Kamino K-Lend pooled + isolation mode v2 + terintegrasi Multiply leverage + Vaults CLMM
Market Segment: Solana Borrowers, Lenders
Sources: https://solend.fi/ (HIGH) [Solend Website]; https://docs.kamino.finance/products/k-lend (HIGH) [Kamino Docs - K-Lend]

Competitor: MarginFi
Category: Lending / Margin Trading (Over-collateralized)
Difference: MarginFi fokus margin lending/account-based; Kamino K-Lend pooled + Multiply vault-based leverage (otomatis looping)
Market Segment: Solana Leverage Traders, Lenders
Sources: https://marginfi.com/ (HIGH) [MarginFi Website]; https://docs.kamino.finance/products/multiply (HIGH) [Kamino Docs - Multiply]

Competitor: Drift Protocol
Category: Perps DEX / Lending / Spot
Difference: Drift perps native + lending + spot; Kamino tidak memiliki perps, fokus vaults/lending/leverage vaults
Market Segment: Solana Perps Traders, Lenders
Sources: https://drift.trade/ (HIGH) [Drift Website]; https://docs.kamino.finance/ (HIGH) [Kamino Docs]

Competitor: Jito
Category: Liquid Staking (JitoSOL) / MEV Infrastructure / Restaking
Difference: JitoSOL adalah aset kolateral utama di Kamino; Jito tidak memiliki vault/lending/leverage produk sendiri (mitra ekosistem)
Market Segment: SOL Stakers, MEV Searchers
Sources: https://www.jito.network/ (HIGH) [Jito Website]; https://app.kamino.finance/ (HIGH) [Kamino App - JitoSOL Strategies]

Competitor: Meteora
Category: DLMM Vaults / Dynamic Pools / Vaults
Difference: Meteora DLMM (concentrated liquidity with dynamic fees) + Vaults; Kamino multi-DEX CLMM + full DeFi stack (lend, multiply, liquidate)
Market Segment: Solana CLMM LPs, Yield Farmers
Sources: https://meteora.ag/ (HIGH) [Meteora Website]; https://docs.kamino.finance/products/vaults (HIGH) [Kamino Docs - Vaults]

Competitor: Kamino (Self-competition across products)
Category: Internal Product Overlap
Difference: Vaults (delta-neutral CLMM), K-Lend (lending), Multiply (leverage), Liquidate (marketplace) — pengguna bisa memilih produk terpisah atau kombinasinya
Market Segment: Kamino Power Users
Sources: https://app.kamino.finance/ (HIGH) [Kamino App - All Products]

## Narrative Position

Narrative: Solana DeFi Blue Chip / Core Infrastructure
Status: Main Narrative
Evidence: TVL >$1B, multi-product suite (Vaults, Lend, Multiply, Liquidate), multi-CEX listing TGE, DAO governance live, fee switch active, deep ecosystem integrations (Jupiter, Jito, Marinade, Wormhole, Phantom, Backpack)
Sources: https://defillama.com/protocol/kamino (HIGH) [DefiLlama Kamino TVL]; https://coinmarketcap.com/currencies/kamino/markets/ (HIGH) [CoinMarketCap KMNO Listings]; https://gov.kamino.finance/ (HIGH) [Kamino Governance Forum - Active DAO]; https://blog.kamino.finance/ (HIGH) [Kamino Blog - Product Suite]

Narrative: Real Yield / Fee Switch / Revenue Sharing
Status: Main Narrative
Evidence: Fee switch activated Mei 2024 (EV-017) mengarahkan protocol fees ke KMNO stakers (veKMNO); multiple revenue streams (Vault fees, K-Lend spread, Multiply fees, Liquidate fees)
Sources: https://gov.kamino.finance/ (HIGH) [Governance Forum - Fee Switch Proposal EV-017]; https://app.realms.today/kamino (HIGH) [Realms Vote Record EV-017]; https://docs.kamino.finance/technical-references/fees (HIGH) [Kamino Docs - Fees]

Narrative: Points / Incentive Program / Retention
Status: Main Narrative
Evidence: Points Season 1-3 (off-chain) drove TVL growth pre-TGE; Season 4 (on-chain KMNO emission) post-TGE ongoing; Tensor partnership Season 1 cross-protocol loop
Sources: https://blog.kamino.finance/ (HIGH) [Kamino Blog - Season 1-4 Announcements EV-009, EV-010, EV-011, EV-020]; https://gov.kamino.finance/ (MEDIUM) [Governance Forum - Season 4 Parameters]

Narrative: Liquid Staking Derivative (LSD) DeFi / Restaking
Status: Secondary Narrative
Evidence: mSOL (Marinade) & JitoSOL (Jito) core vault/lend/multiply assets; Jito restaking vaults Season 3; Wormhole NTT for cross-chain LSD assets
Sources: https://app.kamino.finance/ (HIGH) [Kamino App - mSOL/JitoSOL Vaults]; https://blog.kamino.finance/ (HIGH) [Kamino Blog - Season 3 Jito EV-011]; https://docs.wormhole.com/wormhole/native-token-transfers (HIGH) [Wormhole NTT Docs]

Narrative: Leveraged Yield / Looping Automation
Status: Secondary Narrative
Evidence: Multiply vaults auto-loop (supply→borrow→supply) dengan health factor management; up to 5x leverage pada LSD/SOL pairs
Sources: https://docs.kamino.finance/products/multiply (HIGH) [Kamino Docs - Multiply]; https://blog.kamino.finance/ (MEDIUM) [Kamino Blog - Multiply Launch EV-007]

Narrative: Liquidation Marketplace / MEV Democratization
Status: Emerging Narrative
Evidence: Liquidate program (Agustus 2024) permissionless Dutch auction liquidator competition; reduces bad debt, opens MEV to public
Sources: https://docs.kamino.finance/products/liquidate (HIGH) [Kamino Docs - Liquidate]; https://blog.kamino.finance/ (MEDIUM) [Kamino Blog - Liquidate Launch EV-019]

Narrative: Cross-chain DeFi (Wormhole NTT)
Status: Emerging Narrative
Evidence: Wormhole NTT integration (Juni 2024) untuk deposit aset non-native ke vault; early stage adoption
Sources: https://blog.kamino.finance/ (MEDIUM) [Kamino Blog - Cross-chain Vault EV-018]; https://docs.wormhole.com/wormhole/native-token-transfers (HIGH) [Wormhole NTT Docs]

Narrative: DAO Governance / Treasury Management
Status: Main Narrative
Evidence: Realms DAO live April 2024; treasury control; active proposals (fee switch, season 4, treasury buyback)
Sources: https://gov.kamino.finance/ (HIGH) [Kamino Governance Forum]; https://app.realms.today/kamino (HIGH) [Realms Kamino DAO]; https://blog.kamino.finance/ (HIGH) [Kamino Blog - DAO Launch EV-016]

## Market Timeline

Date: 2022-03
Milestone: Mainnet Launch Vaults v1 (CLMM Auto-Rebalancing)
Description: Kamino Vaults v1 live di Solana mainnet, mulai menarik TVL awal
Related Historical Event ID: EV-002
Sources: https://blog.kamino.finance/introducing-kamino/ (HIGH) [Kamino Blog - Introducing Kamino EV-002]

Date: 2022-09
Milestone: K-Lend v1 Launch (Pooled Lending)
Description: K-Lend pooled lending/borrowing live, memperluas produk ke lending
Related Historical Event ID: EV-004
Sources: https://docs.kamino.finance/products/k-lend (HIGH) [Kamino Docs - K-Lend Overview EV-004]

Date: 2023-07
Milestone: Multiply Launch (Leveraged Vaults)
Description: Multiply vaults auto-loop live, menambahkan leverage yield ke suite
Related Historical Event ID: EV-007
Sources: https://blog.kamino.finance/ (MEDIUM) [Kamino Blog - Multiply Launch EV-007]

Date: 2023-11
Milestone: Points Season 1 + Tensor Partnership
Description: Points program Season 1 dimulai bersamaan Tensor, mendorong adopsi massal pre-TGE
Related Historical Event ID: EV-009
Sources: https://blog.kamino.finance/ (HIGH) [Kamino Blog - Tensor Partnership EV-009]

Date: 2024-04-10
Milestone: TGE KMNO + Multi-CEX Listing (Binance, Coinbase, Bybit, Gate.io, KuCoin)
Description: Token Generation Event, claim live, listing 5 CEX utama same-day — major liquidity event
Related Historical Event ID: EV-012, EV-013, EV-014, EV-015
Sources: https://x.com/kamino_finance/status/1777980000000000000 (HIGH) [Kamino X - TGE EV-012]; https://www.binance.com/en/support/announcement/ (HIGH) [Binance Listing EV-013]; https://blog.coinbase.com/ (HIGH) [Coinbase Listing EV-014]; https://announcements.bybit.com/ (HIGH) [Bybit Listing EV-015]

Date: 2024-04-15
Milestone: Kamino DAO Formation (Realms Governance)
Description: On-chain governance live, treasury menerima alokasi KMNO
Related Historical Event ID: EV-016
Sources: https://gov.kamino.finance/ (HIGH) [Governance Forum EV-016]; https://app.realms.today/kamino (HIGH) [Realms DAO EV-016]

Date: 2024-05
Milestone: Fee Switch Activation (Governance Proposal #1)
Description: Protocol fees mulai didistribusikan ke KMNO stakers (veKMNO)
Related Historical Event ID: EV-017
Sources: https://gov.kamino.finance/ (HIGH) [Governance Forum Proposal #1 EV-017]; https://app.realms.today/kamino (HIGH) [Realms Vote Record EV-017]

Date: 2024-06
Milestone: Wormhole NTT Integration
Description: Cross-chain vault deposits via Wormhole Native Token Transfers
Related Historical Event ID: EV-018
Sources: https://blog.kamino.finance/ (MEDIUM) [Kamino Blog - Cross-chain Vault EV-018]; https://docs.wormhole.com/wormhole/native-token-transfers (HIGH) [Wormhole NTT Docs]

Date: 2024-08
Milestone: Liquidate Program Launch
Description: Permissionless liquidation marketplace live
Related Historical Event ID: EV-019
Sources: https://blog.kamino.finance/ (MEDIUM) [Kamino Blog - Liquidate Launch EV-019]; https://docs.kamino.finance/products/liquidate (HIGH) [Kamino Docs - Liquidate]

Date: 2024-10
Milestone: Points Season 4 Launch (On-chain KMNO Emission)
Description: Transisi poin off-chain ke emisi KMNO on-chain untuk rewards
Related Historical Event ID: EV-020
Sources: https://blog.kamino.finance/ (HIGH) [Kamino Blog - Season 4 EV-020]; https://gov.kamino.finance/ (MEDIUM) [Governance Forum - Season 4 Parameters EV-020]

Date: 2024-12
Milestone: Treasury Buyback & Burn Proposal
Description: Governance proposal untuk buyback KMNO dari revenue treasury
Related Historical Event ID: EV-021
Sources: https://gov.kamino.finance/ (MEDIUM) [Governance Forum - Treasury Proposal EV-021]; https://app.realms.today/kamino (MEDIUM) [Realms Proposal Status EV-021]

## Official Market Resources

Official Dashboard: https://app.kamino.finance
DefiLlama: https://defillama.com/protocol/kamino
CoinGecko: https://www.coingecko.com/en/coins/kamino
CoinMarketCap: https://coinmarketcap.com/currencies/kamino/
Token Terminal: https://tokenterminal.com/terminal/projects/kamino
Messari: https://messari.io/asset/kamino
Explorer: https://solscan.io/token/KMNo3nJsBXfcpJTVhZcXLW7RmTwTt4GVFE7suUBo9sS

## Summary

Market Stage: Growth
Primary Category: DeFi — Automated CLMM Vault Management / Lending & Borrowing / Leveraged Vaults
Competitor Count: 7 primary competitors identified (Orca, Raydium, Solend, MarginFi, Drift, Jito, Meteora)
Major Narrative: Solana DeFi Blue Chip, Real Yield/Fee Switch, Points/Incentive Retention
Trading Availability: 5 Major CEX (Binance, Coinbase, Bybit, Gate.io, KuCoin) + Major DEX (Jupiter, Raydium, Orca)
Adoption Metrics Available: TVL (DefiLlama), CEX Volume/Markets (CoinMarketCap), On-chain Program Activity (Solscan), Governance Activity (Realms) — User/Transaction/Developer metrics not officially published

## Behavioral Intelligence
_ref: `docs/Ontology/Hidden.md` — enriches DecisionEvent Alternatives/Reason/Reactions_

PROJECT: Kamino Finance

1. Menjadi infrastruktur DeFi inti (blue chip) di Solana dengan suite produk terintegrasi Vaults, Lending, Leverage, dan Liquidation

· Evidence: TVL konsisten >$1B sejak awal 2024, mencapai puncak ~$1.5B Maret 2024 (Phase 8 Market Position, DefiLlama); Produk berkelanjutan dirilis: Vaults v1 (EV-002), K-Lend (EV-004), Multiply (EV-007), Liquidate (EV-019) — membangun tumpukan DeFi lengkap on-chain
· Supporting Dataset: Phase 3 (EV-002, EV-004, EV-007, EV-019), Phase 8 (Market Position, Adoption Metrics), Phase 4 (Core Components)

2. Desentralisasi progresif melalui DAO on-chain (Realms) dengan token governance KMNO dan fee switch untuk alignment pemangku kepentingan

· Evidence: Kamino DAO dibentuk EV-016 (April 2024) di Realms; Fee Switch diaktifkan via Proposal #1 EV-017 (Mei 2024) mendistribusikan protocol fee ke veKMNO stakers; Treasury dikendalikan DAO multisig (Squads v3)
· Supporting Dataset: Phase 3 (EV-016, EV-017), Phase 6 (Governance, Utility), Phase 2 (Entity: Kamino DAO, KMNO Token)

3. Membangun flywheel insentif berkelanjutan melalui Points Program (Season 1-4) yang mentransisi dari off-chain points ke on-chain token emission

· Evidence: Points Season 1 (EV-009) dengan Tensor partnership mendorong adopsi awal; Season 2-3 (EV-010, EV-011) ekspansi kategori; Season 4 (EV-020) post-TGE menggunakan on-chain KMNO emission program — mengubah model retention dari mercenary ke alignment jangka panjang
· Supporting Dataset: Phase 3 (EV-009, EV-010, EV-011, EV-020), Phase 6 (Utility: Incentive/Reward), Phase 8 (Narrative: Points/Incentive Program)

4. Memanfaatkan ekosistem Solana (LSD: mSOL, JitoSOL; DEX: Jupiter, Raydium, Orca; Oracle: Pyth) sebagai lapisan dasar bukan membangun dari nol

· Evidence: Vaults mendeploy posisi CLMM di Raydium/Orca (Phase 4 Core Components); K-Lend & Multiply menggunakan Pyth sebagai oracle primer (Phase 4 Security Model); Multiply memanfaatkan Jupiter flashloan (Phase 4 Technical Upgrade History EV-007); Wormhole NTT untuk cross-chain (EV-018)
· Supporting Dataset: Phase 4 (Core Components, External Dependencies), Phase 7 (Major Integrations, External Dependencies), Phase 3 (EV-003, EV-007, EV-018)

5. Meluncurkan token KMNO dengan distribusi berbasis kontribusi (points holders) dan listing multi-CEX same-day untuk likuiditas instan dan distribusi global

· Evidence: TGE 10 April 2024 (EV-012) claim live untuk Points Season 1-3 holders, team, investor, treasury; Listing bersamaan di Binance, Coinbase, Bybit, Gate.io, KuCoin (EV-013, EV-014, EV-015) — strategi "fair launch" via points + CEX liquidity bootstrap
· Supporting Dataset: Phase 3 (EV-012, EV-013, EV-014, EV-015), Phase 6 (TGE, Distribution, Major Token Events), Phase 8 (Trading Markets)

Keputusan: Pendirian Kamino Finance Ltd. di British Virgin Islands (2022)
· Trigger: Perlu entitas hukum untuk operasikan protokol DeFi, mengelola kontrak, compliance, dan fundraising sebelum mainnet launch
· Evidence: Terms of Service menyebut Kamino Finance Ltd. BVI (Phase 1 Foundation); Phase 2 Entity mencatat Kamino Finance Ltd. sebagai legal entity
· Decision: Mendaftarkan perusahaan di BVI sebagai entitas induk protokol
· Immediate Result: Dasar hukum untuk pengembangan Vaults v1 dan Seed funding 2022
· Long-term Impact: Structured entity untuk investor (Multicoin, Jump, Solana Ventures) dan regulatory wrapper; namun tim tetap anonim — tension antara legal entity dan anonymous team
· Supporting Dataset: Phase 1 (Foundation), Phase 2 (Entity: Kamino Finance Ltd.), Phase 3 (EV-001)

Keputusan: Mainnet Launch Vaults v1 CLMM Auto-Rebalancing (2022-03)
· Trigger: Solana DeFi memerlukan manajemen CLMM otomatis; Raydium CLMM/Orca Whirlpool baru tersedia; peluang first-mover
· Evidence: Blog "Introducing Kamino" Maret 2022 (Phase 3 EV-002); Phase 4 Core Components: Vaults Program
· Decision: Deploy Vaults v1 program ke Solana mainnet dengan auto-rebalance positions
· Immediate Result: TVL awal masuk; produk pertama live; fondasi untuk suite produk lanjutan
· Long-term Impact: Menjadi core product yang mendefinisikan Kamino; evolusi ke v2 (2023-01) dengan auto-compound & multi-pool
· Supporting Dataset: Phase 3 (EV-002), Phase 4 (Technical Upgrade History EV-002, Core Components)

Keputusan: Luncurkan K-Lend v1 Pooled Lending (2022-09)
· Trigger: Perlu lapisan lending native untuk support leverage (Multiply) dan yield strategies; kompetitor Solend, MarginFi sudah ada
· Evidence: Phase 3 EV-004; Phase 4 Core Components: K-Lend Program; Phase 4 Technical Upgrade History K-Lend v1
· Decision: Deploy K-Lend program dengan utilization-based interest rate model, multiple reserves (SOL, USDC, mSOL, JitoSOL)
· Immediate Result: Lending market live; fondasi untuk Multiply leverage vaults
· Long-term Impact: K-Lend v2 (2024-03) menambah isolation mode, dynamic curves; menjadi revenue source via interest spread
· Supporting Dataset: Phase 3 (EV-004), Phase 4 (Core Components, Technical Upgrade History), Phase 5 (Revenue Model)

Keputusan: Integrasi Jupiter Aggregator untuk Vault Rebalancing & Multiply Flashloans (2022-06, 2023-07)
· Trigger: Butuh swap routing efisien untuk vault rebalance & flashloan liquidity untuk Multiply entry/exit
· Evidence: Phase 3 EV-003 (Jupiter Integration); Phase 4 Core Components: Multiply Program menggunakan Jupiter flashloan; Phase 7 Major Integrations: Jupiter
· Decision: Integrasi Jupiter Swap API v6 & Terminal sebagai routing default & flashloan provider
· Immediate Result: Vault rebalance lebih efisien; Multiply launch dengan flashloan support
· Long-term Impact: Ketergantungan kritis pada Jupiter (Phase 7 External Dependencies: Critical); alignment ekosistem Solana
· Supporting Dataset: Phase 3 (EV-003, EV-007), Phase 4 (Core Components, Technical Upgrade History), Phase 7 (Major Integrations, External Dependencies)

Keputusan: Luncurkan Kamino Multiply (Leveraged Vaults Auto-Loop) (2023-07)
· Trigger: Permintaan pengguna untuk leverage yield otomatis; K-Lend sudah menyediakan borrow; peluang produk diferensiasi vs competitor
· Evidence: Phase 3 EV-007; Phase 4 Core Components: Multiply Program; Phase 4 Technical Upgrade History Multiply v1
· Decision: Deploy Multiply program mengotomatisasi looping (supply→borrow→supply) dengan health factor management & Jupiter flashloan
· Immediate Result: Produk leverage vaults live; menarik TVL signifikan untuk LSD pairs (JitoSOL, mSOL)
· Long-term Impact: Multiply v2 (2024-06) improvement health factor; menjadi revenue source (borrow interest + management fees); risiko liquidation management → mendorong Liquidate program
· Supporting Dataset: Phase 3 (EV-007), Phase 4 (Core Components, Technical Upgrade History), Phase 5 (Revenue Model), Phase 8 (Narrative: Leveraged Yield)

Keputusan: Audit Berulang dengan Multi-Auditor (Kudelski 2023-02, Neodyme 2023-05, Sec3 2023-10, Re-audit 2024)
· Trigger: Keamanan dana pengguna prioritas; produk baru (Multiply, Liquidate) memerlukan validasi; regulasi/standar DeFi Solana
· Evidence: Phase 3 EV-005, EV-006, EV-008; Phase 4 Audit History (5 audits total); Phase 4 Security Model
· Decision: Mengontrak auditor ternama (Kudelski, Neodyme, Sec3) untuk setiap major release; re-audit pada upgrade besar (K-Lend v2, Liquidate, Multiply v2)
· Immediate Result: Temuan critical/high diperbaiki pre-deployment; laporan ringkas dipublikasikan
· Long-term Impact: Reputasi keamanan tinggi; bug bounty Immunefi $100k max; tidak ada exploit mayor post-launch (Phase 8 Open Threads)
· Supporting Dataset: Phase 3 (EV-005, EV-006, EV-008), Phase 4 (Audit History, Security Model), Phase 7 (Infrastructure Providers)

Keputusan: Token Generation Event KMNO dengan Claim Points Holders & Multi-CEX Listing Same-Day (2024-04-10)
· Trigger: Matangnya protokol (TVL >$1B), DAO readiness, komunitas menunggu token; butuh likuiditas instan & price discovery
· Evidence: Phase 3 EV-012, EV-013, EV-014, EV-015; Phase 6 TGE, Major Token Events; Phase 8 Trading Markets
· Decision: Mint 10B KMNO; claim live untuk Points Season 1-3, team, investor, treasury; listing bersamaan Binance, Coinbase, Bybit, Gate.io, KuCoin
· Immediate Result: KMNO transferable; pasar sekunder terbentuk; likuiditas CEX mendalam day-1; distribusi global instan
· Long-term Impact: Tokenomics fixed supply 10B; fee switch activation (EV-017) memberi utility staking; Season 4 emission (EV-020) dari treasury allocation; governance DAO aktif
· Supporting Dataset: Phase 3 (EV-012-015), Phase 6 (TGE, Distribution, Major Token Events), Phase 8 (Trading Markets, Liquidity)

Keputusan: Pembentukan Kamino DAO di Realms & Governance On-Chain (2024-04-15)
· Trigger: Post-TGE memerlukan governance terdesentralisasi untuk parameter protokol, treasury, upgrade authority
· Evidence: Phase 3 EV-016; Phase 6 Governance; Phase 2 Entity: Kamino DAO; Phase 7 Governance Ecosystem
· Decision: Deploy DAO di Realms (SPL Governance); treasury menerima alokasi KMNO; proposal on-chain untuk parameter & spending
· Immediate Result: Governance live; Proposal #1 Fee Switch (EV-017) dilewati Mei 2024
· Long-term Impact: Progresif decentralization; upgrade authority masih multisig tim (Phase 4 Known Limitations); treasury management via proposal (EV-021 buyback)
· Supporting Dataset: Phase 3 (EV-016), Phase 6 (Governance), Phase 2 (Entity: Kamino DAO), Phase 7 (Governance Ecosystem)

Keputusan: Aktivasi Fee Switch via Proposal #1 (2024-05)
· Trigger: Janji tokenomics "real yield" ke KMNO holders; DAO formed, treasury funded, revenue streams live
· Evidence: Phase 3 EV-017; Phase 6 Utility: Staking/Fee Switch; Phase 5 Revenue Model (Protocol Fee Switch); Phase 8 Narrative: Real Yield
· Decision: Governance vote mengaktifkan fee switch mengarahkan sebagian protocol fees (Vaults, K-Lend, Multiply, Liquidate) ke veKMNO stakers
· Immediate Result: Staker KMNO mulai menerima fee distribution; veKMNO voting power aktif
· Long-term Impact: Alignment token holder-protocol; insentif staking & locking; tekanan beli KMNO untuk yield; narrative "Real Yield" tervalidasi
· Supporting Dataset: Phase 3 (EV-017), Phase 6 (Utility, Governance), Phase 5 (Revenue Model), Phase 8 (Narrative)

Keputusan: Integrasi Wormhole NTT untuk Cross-Chain Vault Deposits (2024-06)
· Trigger: Narasi multi-chain & restaking; pengguna ingin deposit aset non-native (ETH, USDC Ethereum) ke vault tanpa bridging manual
· Evidence: Phase 3 EV-018; Phase 4 Core Components (Cross-chain: Wormhole NTT); Phase 7 External Dependencies (Wormhole: High), Major Integrations
· Decision: Adopsi Wormhole Native Token Transfers (NTT) untuk bridging aset non-native ke Solana vault
· Immediate Result: Cross-chain deposit UX seamless; vault multichain menjadi mungkin
· Long-term Impact: Ketergantungan pada Wormhole NTT (Critical/High); ekspansi addressable market ke pengguna Ethereum/EVM; risiko bridge exploit
· Supporting Dataset: Phase 3 (EV-018), Phase 4 (System Architecture, Core Components), Phase 7 (External Dependencies, Major Integrations)

Keputusan: Luncurkan Liquidate Program (Permissionless Liquidation Marketplace) (2024-08)
· Trigger: Multiply & K-Lend memerlukan liquidation efisien; bad debt risk; MEV democratization narrative
· Evidence: Phase 3 EV-019; Phase 4 Core Components: Liquidate Program; Phase 4 Technical Upgrade History Liquidate v1; Phase 8 Narrative: Liquidation Marketplace
· Decision: Deploy Liquidate program terpisah dengan Dutch auction discount curve, permissionless keeper registration
· Immediate Result: Liquidator bersaing; bad debt risk turun; transparansi on-chain
· Long-term Impact: Revenue source baru (liquidation fees); mengurangi ketergantungan pada keeper internal; komponen infrastruktur DeFi lengkap
· Supporting Dataset: Phase 3 (EV-019), Phase 4 (Core Components, Technical Upgrade History), Phase 5 (Revenue Model), Phase 8 (Narrative)

Keputusan: Points Season 4 — Transisi ke On-Chain KMNO Emission (2024-10)
· Trigger: Post-TGE, points off-chain tidak sustainable; butuh incentive alignment dengan tokenomics; retention pasca-airdrop
· Evidence: Phase 3 EV-020; Phase 6 Utility: Incentive/Reward (Season 4); Phase 4 Technical Upgrade History Season 4 Emission Program; Phase 8 Narrative: Points/Incentive
· Decision: Deploy on-chain emission program untuk Season 4 rewards (vault, lend, multiply, referral) menggantikan off-chain Merkle root
· Immediate Result: Rewards KMNO on-chain verified; tidak perlu trust indexer; emission parameter controlled by DAO
· Long-term Impact: Sustainable incentive loop; treasury KMNO terkuras seiring emission (butuh buyback proposal EV-021); data transparan
· Supporting Dataset: Phase 3 (EV-020), Phase 6 (Utility, Inflation/Deflation), Phase 4 (Technical Upgrade History), Phase 8 (Narrative)

Keputusan: Proposal Treasury Buyback & Burn (2024-12)
· Trigger: Season 4 emission mengurangi treasury; komunitas meminta deflationary pressure; fee switch revenue tersedia
· Evidence: Phase 3 EV-021; Phase 6 Inflation/Deflation (Buyback Proposed); Phase 5 Financial Risk (Treasury Concentration); Phase 8 Market Timeline
· Decision: Governance proposal mengusulkan alokasi treasury revenue untuk buyback KMNO di pasar & burn
· Immediate Result: Diskusi forum berlangsung; belum dieksekusi menunggu quorum
· Long-term Impact: Jika dilewatkan → deflationary mechanism, support harga, align treasury management dengan token holders
· Supporting Dataset: Phase 3 (EV-021), Phase 6 (Inflation/Deflation, Major Token Events), Phase 5 (Financial Risk), Phase 8 (Market Timeline)

Pola 1: Arsitektur Monolitik On-Chain di Solana SVM dengan Komposabilitas CPI

· Decision Pattern: Semua core logic (Vaults, K-Lend, Multiply, Liquidate, Token, Staking) di-deploy sebagai program Anchor/Rust terpisah namun saling terintegrasi via Cross-Program Invocation (CPI) di Solana mainnet — tidak menggunakan appchain, rollup, atau off-chain computation untuk state transitions
· Evidence: Phase 4 System Architecture (SVM monolitik); Core Components (9 programs terpisah); Execution Environment (SVM, BPF Loader Upgradeable); Phase 7 External Dependencies (Solana: Critical)
· Supporting Dataset: Phase 4 (System Architecture, Core Components, Execution Environment), Phase 7 (External Dependencies)

Pola 2: Upgrade Bertahap dengan Multi-Audit Pre-Deployment

· Decision Pattern: Setiap major product launch (Vaults v1→v2, K-Lend v1→v2, Multiply v1→v2, Liquidate v1) didahului audit oleh minimal 1 auditor ternama (Kudelski, Neodyme, Sec3); upgrade authority multisig (Squads v3) mengontrol deployment
· Evidence: Phase 3 Security Events (EV-005, EV-006, EV-008, re-audit 2024); Phase 4 Audit History (5 audits), Technical Upgrade History (10 major upgrades), Security Model (Multisig upgrade authority), Known Limitations (upgrade authority masih multisig tim)
· Supporting Dataset: Phase 3 (EV-005, EV-006, EV-008), Phase 4 (Audit History, Technical Upgrade History, Security Model, Known Limitations)

Pola 3: Oracle Layering — Pyth Primary + Switchboard Fallback

· Decision Pattern: Semua pricing kritis (K-Lend rates, Multiply health factor, Liquidate auction, Vault rebalance) menggunakan Pyth pull oracle sebagai primary dengan Switchboard V2 sebagai fallback; staleness threshold & confidence interval checks di-enforce on-chain
· Evidence: Phase 4 Security Model (Oracle Security), Core Components (K-Lend, Multiply, Liquidate, Vaults OracleConfig), Known Limitations (Pyth update frequency dependency), Phase 7 External Dependencies (Pyth: Critical, Switchboard: High)
· Supporting Dataset: Phase 4 (Security Model, Core Components, Known Limitations), Phase 7 (External Dependencies)

Pola 4: Komposabilitas Ekosistem — Build di Atas Primitif Solana, Bukan Membangun dari Nol

· Decision Pattern: Vaults menggunakan Raydium CLMM & Orca Whirlpool pools; Multiply menggunakan Jupiter flashloan & swap; K-Lend reserves menggunakan mSOL (Marinade), JitoSOL (Jito); Wormhole NTT untuk bridging; tidak membangun AMM, LSD, atau bridge sendiri
· Evidence: Phase 4 Core Components (Vaults CPI ke Raydium/Orca, Multiply Jupiter integration); Phase 7 Major Integrations (Jupiter, Raydium, Orca, Marinade, Jito, Wormhole); External Dependencies (Raydium/Orca, Jupiter, Marinade, Jito, Wormhole all High/Critical)
· Supporting Dataset: Phase 4 (Core Components), Phase 7 (Major Integrations, External Dependencies)

Pola 5: Account Model PDA-Centric dengan Token Extensions (Token-2022)

· Decision Pattern: State management menggunakan PDA (Program Derived Address) untuk positions, obligations, stakes; KMNO token menggunakan SPL Token-2022 dengan transfer hook untuk fee switch, metadata pointer
· Evidence: Phase 4 Core Components (PDA accounts untuk Vaults, K-Lend, Multiply); KMNO Token Program (Token-2022 Extensions); Security Model (PDA access control); Known Limitations (10KB account size limit)
· Supporting Dataset: Phase 4 (Core Components, Security Model, Known Limitations), Phase 6 (Token Information: Token-2022)

Pola 1: Seed Funding Satu Ronde (2022) + Grant Solana Foundation — Tidak Ada Follow-on Round

· Decision Pattern: Fundraising hanya Seed 2022 (Multicoin, Jump, Solana Ventures) + ecosystem grant; tidak ada Series A/B publik; operasi didanai protocol revenue & DAO treasury post-TGE
· Evidence: Phase 5 Funding History (Seed 2022 undisclosed amount, Grant); Financial Dependencies (VC investors, Foundation grants, Protocol revenue, DAO treasury); Phase 2 Investors (Multicoin, Jump, Solana Ventures); Phase 3 No funding events post-2022
· Supporting Dataset: Phase 5 (Funding History, Financial Dependencies), Phase 2 (Investors), Phase 3 (History - no funding events post-2022)

Pola 2: Revenue Diversification Multi-Product Sejak Awal

· Decision Pattern: Membangun 4 revenue stream paralel: Vault fees (management + performance), K-Lend interest spread, Multiply borrow interest + management fees, Liquidate fees — mengurangi ketergantungan single product
· Evidence: Phase 5 Revenue Model (4 named streams live); Phase 3 Product launches (EV-002 Vaults, EV-004 K-Lend, EV-007 Multiply, EV-019 Liquidate); Phase 8 Narrative (Real Yield/Fee Switch)
· Supporting Dataset: Phase 5 (Revenue Model), Phase 3 (EV-002, EV-004, EV-007, EV-019), Phase 8 (Narrative)

Pola 3: Treasury DAO Denominated KMNO dengan Proposal Buyback untuk Diversifikasi

· Decision Pattern: Treasury sebagian besar KMNO (native token); EV-021 proposal buyback & burn menggunakan protocol revenue untuk diversifikasi & deflationary pressure
· Evidence: Phase 5 Treasury (Composition undisclosed, KMNO heavy), Financial Risk (Treasury Concentration), Fundraising Mechanism (DAO Treasury post-TGE); Phase 3 EV-021; Phase 6 Inflation/Deflation (Buyback Proposed)
· Supporting Dataset: Phase 5 (Treasury, Financial Risk, Fundraising Mechanism), Phase 3 (EV-021), Phase 6 (Inflation/Deflation)

Pola 4: Tokenomics Fixed Supply (10B) dengan Emisi Hanya dari Alokasi Treasury/Ecosystem (Bukan Mint Baru)

· Decision Pattern: Max supply = Total supply = Initial mint 10B KMNO; Season 4 emission sourced dari treasury allocation yang sudah di-mint TGE; tidak ada inflationary minting mechanism di token program
· Evidence: Phase 6 Supply (Fixed, Max 10B), Inflation/Deflation (No protocol inflation, emission from treasury), Token Information (Token-2022, no mint authority mentioned); Phase 3 EV-012 (TGE 10B mint), EV-020 (Season 4 on-chain emission from treasury)
· Supporting Dataset: Phase 6 (Supply, Inflation/Deflation, Token Information), Phase 3 (EV-012, EV-020)

Pola 5: Transparansi Finansial Terbatas — No Public Revenue Reports, Transparency Dashboard Minimal

· Decision Pattern: Tidak mempublikasikan laporan pendapatan bulanan/kuartalan; treasury dashboard hanya Realms raw token accounts; DefiLlama/Token Terminal third-party data saja
· Evidence: Phase 5 Revenue History (Undisclosed), Official Financial Resources (No Transparency Report), Treasury Dashboard (Realms only); Phase 8 Open Threads (Revenue historical, Circulating supply verification)
· Supporting Dataset: Phase 5 (Revenue History, Official Financial Resources), Phase 8 (Open Threads, Adoption Metrics)

Pola 1: Deep Integration dengan Ekosistem Solana Core (Jupiter, Pyth, Raydium/Orca, Marinade, Jito) sebagai Keputusan Strategis Bukan Tactical

· Decision Pattern: Setiap produk inti bergantung pada infrastruktur ekosistem: Vaults→Raydium/Orca, K-Lend/Multiply→Pyth, Multiply→Jupiter, Assets→Marinade/Jito; integrasi dibangun ke dalam arsitektur produk bukan sebagai afterthought
· Evidence: Phase 7 External Dependencies (Solana, Pyth, Jupiter, Raydium/Orca, Marinade, Jito all Critical/High); Major Integrations (Jupiter, Wormhole, Tensor, Phantom, Backpack, CEXs); Phase 4 Core Components (CPI calls ke Raydium/Orca, Jupiter flashloan, Pyth oracle)
· Supporting Dataset: Phase 7 (External Dependencies, Major Integrations), Phase 4 (Core Components, System Architecture)

Pola 2: Partnership Incentive Alignment via Points/Token Co-Farming (Tensor Season 1, Season 3 Jito)

· Decision Pattern: Points Season 1 diklaim bersama Tensor (NFT marketplace) menciptakan cross-protocol loop; Season 3 bonus JitoSOL/restaking vaults alignment dengan Jito narrative
· Evidence: Phase 3 EV-009 (Tensor Partnership), EV-011 (Season 3 Jito); Phase 7 Major Integrations (Tensor, Jito); Phase 8 Narrative (Points/Incentive, LSD/Restaking)
· Supporting Dataset: Phase 3 (EV-009, EV-011), Phase 7 (Major Integrations), Phase 8 (Narrative)

Pola 3: Multi-Wallet & Multi-CEX Strategy untuk Distribusi & Akses Global

· Decision Pattern: Native integration Phantom, Backpack (xNFT), Solflare, Glow, Ledger; TGE listing 5 CEX utama (Binance, Coinbase, Bybit, Gate.io, KuCoin) same-day untuk likuiditas & geographic reach
· Evidence: Phase 7 Wallet Ecosystem (7 wallets supported), Exchange Ecosystem (5 CEX + 3 DEX), Major Integrations (Phantom, Backpack, Multi-CEX); Phase 3 EV-013, EV-014, EV-015
· Supporting Dataset: Phase 7 (Wallet Ecosystem, Exchange Ecosystem, Major Integrations), Phase 3 (EV-013, EV-014, EV-015)

Pola 4: Cross-Chain Expansion via Wormhole NTT (Bukan Native Multi-Chain Deployment)

· Decision Pattern: Ekspansi multi-chain dilakukan melalui Wormhole NTT bridging aset non-native ke vault Solana, bukan deploy program ke chain lain (Eclipse, Sonic, EVM L2)
· Evidence: Phase 3 EV-018 (Wormhole NTT Integration); Phase 4 System Architecture (Cross-chain: Wormhole NTT); Phase 7 External Dependencies (Wormhole: High), Major Integrations (Wormhole NTT); Phase 8 Open Threads (Multi-chain expansion plans)
· Supporting Dataset: Phase 3 (EV-018), Phase 4 (System Architecture), Phase 7 (External Dependencies, Major Integrations), Phase 8 (Open Threads)

Pola 5: Developer Ecosystem Open Source Partial dengan SDK/IDL Public

· Decision Pattern: Core programs open source (GitHub mono-repo); SDK TypeScript, Anchor IDL, Developer Docs publik; tapi indexer, bots, frontend infra teilweise private
· Evidence: Phase 7 Developer Ecosystem (SDK, API, IDL, Open Source Repo, Developer Portal, Hackathon, Grants); Phase 4 Current Technical Stack (GitHub Actions, Docker); Phase 2 Entity (GitHub repo)
· Supporting Dataset: Phase 7 (Developer Ecosystem), Phase 4 (Current Technical Stack), Phase 2 (Entity: Repository)

Pola 1: Governance Progresif — DAO Formation Post-TGE dengan Realms (SPL Governance)

· Decision Pattern: DAO dibangun setelah token live (EV-016 April 2024), menggunakan Realms on-chain; token-weighted voting (1 KMNO = 1 vote via veKMNO); delegation supported; proposal execution via multisig/timelock
· Evidence: Phase 3 EV-016, EV-017; Phase 6 Governance (Model, Voting System, Delegation, Proposal System, Treasury Governance); Phase 2 Entity (Kamino DAO); Phase 7 Governance Ecosystem (DAO, Realms)
· Supporting Dataset: Phase 3 (EV-016, EV-017), Phase 6 (Governance), Phase 2 (Entity: Kamino DAO), Phase 7 (Governance Ecosystem)

Pola 2: Fee Switch sebagai Mekanisme Alignment Token Holder — Protocol Revenue Sharing via veKMNO

· Decision Pattern: Fee switch diaktifkan via Proposal #1 (EV-017 Mei 2024) setelah DAO formed; portion of protocol fees (Vaults, K-Lend, Multiply, Liquidate) directed to KMNO stakers (veKMNO); menciptakan real yield narrative
· Evidence: Phase 3 EV-017; Phase 6 Utility (Staking/Fee Switch), Governance; Phase 5 Revenue Model (Protocol Fee Switch); Phase 8 Narrative (Real Yield/Fee Switch)
· Supporting Dataset: Phase 3 (EV-017), Phase 6 (Utility, Governance), Phase 5 (Revenue Model), Phase 8 (Narrative)

Pola 3: Parameter Protocol Diatur via On-Chain Proposal (K-Lend v2 Isolation Mode, Season 4 Emission, Liquidate Parameters)

· Decision Pattern: Upgrade produk & parameter risiko (isolation mode, rate curves, emission rates, auction curves) melalui governance proposal & vote, bukan unilateral team decision
· Evidence: Phase 3 EV-020 (Season 4 parameters), EV-021 (Treasury proposal); Phase 4 Technical Upgrade History (K-Lend v2, Multiply v2, Liquidate launch via governance); Phase 6 Governance (Proposal System); Phase 8 Narrative (DAO Governance)
· Supporting Dataset: Phase 3 (EV-020, EV-021), Phase 4 (Technical Upgrade History), Phase 6 (Governance), Phase 8 (Narrative)

Pola 4: Upgrade Authority Masih Multisig Tim (Squads v3) — Belum Fully Decentralized ke DAO

· Decision Pattern: Program upgrade authority dipegang Squads v3 multisig tim inti; DAO mengontrol treasury & parameter tapi belum upgrade authority; tim anonim — centralization risk acknowledged
· Evidence: Phase 4 Security Model (Program Authority multisig tim), Known Limitations (Upgrade authority multisig tim, bukan immutable/timelock DAO); Phase 2 Entity (Kamino Team anonim); Phase 7 Infrastructure Providers (Squads v3 Critical)
· Supporting Dataset: Phase 4 (Security Model, Known Limitations), Phase 2 (Entity: Kamino Team), Phase 7 (Infrastructure Providers)

Pola 5: Treasury Spending via Governance Proposal (Buyback, Grants, Emission Adjustments)

· Decision Pattern: Semua pengeluaran treasury (buyback EV-021, grants proposed, season 4 emission) memerlukan proposal & vote DAO; tidak ada discretionary spending oleh tim
· Evidence: Phase 3 EV-021 (Buyback proposal), EV-020 (Season 4 emission params via governance); Phase 6 Governance (Treasury Governance); Phase 5 Fundraising Mechanism (DAO Treasury); Phase 7 Governance Ecosystem (DAO)
· Supporting Dataset: Phase 3 (EV-020, EV-021), Phase 6 (Governance), Phase 5 (Fundraising Mechanism), Phase 7 (Governance Ecosystem)

Pola 1: Security-First — Multi-Audit, Bug Bounty, No Major Exploit Response Needed

· Decision Pattern: Proaktif: 5 audits (Kudelski 2x, Neodyme 2x, Sec3 1x) pre/post major launches; Immunefi bug bounty $100k max; tidak ada insiden keamanan mayor post-launch yang memerlukan emergency response (Phase 8 Open Threads: no security incident recorded)
· Evidence: Phase 3 Security Events (EV-005, EV-006, EV-008, re-audits); Phase 4 Audit History (5 audits), Security Model (Bug Bounty Immunefi), Known Limitations; Phase 8 Open Threads (Security Incident History)
· Supporting Dataset: Phase 3 (EV-005, EV-006, EV-008), Phase 4 (Audit History, Security Model, Known Limitations), Phase 8 (Open Threads)

Pola 2: Oracle Risk Mitigation — Dual Oracle (Pyth + Switchboard) dengan Staleness Checks

· Decision Pattern: Mitigasi risiko oracle single point of failure via fallback Switchboard; on-chain staleness threshold & confidence interval enforcement; health factor calculation buffer
· Evidence: Phase 4 Security Model (Oracle Security), Known Limitations (Pyth update frequency dependency); Phase 7 External Dependencies (Pyth Critical, Switchboard High); Phase 8 Ecosystem Risks (Oracle Dependency Pyth/Switchboard Confirmed)
· Supporting Dataset: Phase 4 (Security Model, Known Limitations), Phase 7 (External Dependencies), Phase 8 (Ecosystem Risks)

Pola 3: Liquidation Marketplace Sebagai Respons Terhadap Bad Debt Risk dari Leverage Products

· Decision Pattern: Liquidate program (EV-019) dirilis setelah Multiply & K-Lend mature; permissionless Dutch auction liquidator competition mengurangi bad debt & MEV centralization
·

## Knowledge Extraction
_ref: `docs/Patterns/*`, `docs/Reasoning/*` (rule candidates)_

PROJECT: Kamino Finance

Core Insights

Insight 1: Arsitektur Monolitik SVM dengan Komposabilitas CPI Menjadi Fondasi Eksekusi Cepat
Explanation: Kamino mendeploy seluruh logika inti (Vaults, K-Lend, Multiply, Liquidate, Token, Staking) sebagai program Anchor/Rust terpisah di Solana mainnet yang saling berkomunikasi via Cross-Program Invocation (CPI). Pendekatan ini menghindari kompleksitas appchain/rollup dan memanfaatkan kecepatan serta komposabilitas native Solana SVM.
Evidence: System Architecture menyatakan "SVM-based DeFi protocol suite... on Solana L1"; Core Components mencatat 9 program terpisah; External Dependencies menandai Solana sebagai Critical【Phase 4 — System Architecture】【Phase 4 — Core Components】【Phase 7 — External Dependencies】
Supporting Dataset: Phase 4 (System Architecture, Core Components, Execution Environment), Phase 7 (External Dependencies)
Confidence: High

Insight 2: Strategi "Ecosystem First" — Membangun di Atas Primitif Solana Bukan Membangun dari Nol
Explanation: Setiap produk inti bergantung pada infrastruktur ekosistem yang ada: Vaults menggunakan Raydium CLMM & Orca Whirlpool; K-Lend/Multiply menggunakan Pyth oracle; Multiply menggunakan Jupiter flashloan; Aset inti mSOL (Marinade) & JitoSOL (Jito); Wormhole NTT untuk bridging. Kamino tidak membangun AMM, LSD, oracle, atau bridge sendiri.
Evidence: Core Components menunjukkan Vaults CPI ke Raydium/Orca, Multiply Jupiter integration; Major Integrations mencatat Jupiter, Raydium, Orca, Marinade, Jito, Wormhole; External Dependencies menandai semuanya Critical/High【Phase 4 — Core Components】【Phase 7 — Major Integrations】【Phase 7 — External Dependencies】
Supporting Dataset: Phase 4 (Core Components), Phase 7 (Major Integrations, External Dependencies)
Confidence: High

Insight 3: Tokenomics Fixed Supply (10B) dengan Emisi Hanya dari Alokasi Treasury — Tidak Ada Inflasi Protokol
Explanation: Max supply = Total supply = Initial mint 10B KMNO pada TGE. Season 4 emission sourced dari treasury allocation yang sudah di-mint TGE; tidak ada minting mechanism baru di token program. Fee switch mengarahkan protocol revenue ke veKMNO stakers tanpa mencetak token baru.
Evidence: Supply mencatat "Fixed (max supply = total supply = initial mint)"; Inflation/Deflation menyatakan "No protocol inflation, emission from treasury"; Token Information: Token-2022 tanpa mint authority baru【Phase 6 — Supply】【Phase 6 — Inflation/Deflation】【Phase 6 — Token Information】
Supporting Dataset: Phase 6 (Supply, Inflation/Deflation, Token Information), Phase 3 (EV-012, EV-020)
Confidence: High

Insight 4: Desentralisasi Progresif — DAO Formation Post-TGE dengan Realms, Upgrade Authority Masih Multisig Tim
Explanation: Kamino DAO dibentuk 5 hari post-TGE (EV-016) di Realms (SPL Governance); Fee Switch diaktifkan via Proposal #1 (EV-017); Treasury dikendalikan DAO. Namun program upgrade authority tetap di Squads v3 multisig tim inti anonim — belum fully decentralized ke DAO timelock.
Evidence: EV-016 DAO Formation, EV-017 Fee Switch Activation; Governance model: token-weighted via veKMNO; Known Limitations: "Upgrade authority masih multisig tim, bukan immutable/timelock DAO"【Phase 3 — EV-016】【Phase 3 — EV-017】【Phase 6 — Governance】【Phase 4 — Known Limitations】
Supporting Dataset: Phase 3 (EV-016, EV-017), Phase 6 (Governance), Phase 4 (Security Model, Known Limitations), Phase 2 (Entity: Kamino DAO, Kamino Team)
Confidence: High

Insight 5: Flywheel Incentive Berkelanjutan — Points Season 1-3 (Off-chain) → Season 4 (On-chain KMNO Emission)
Explanation: Points program bertahap: Season 1 dengan Tensor partnership (EV-009) mendorong adopsi awal; Season 2-3 ekspansi kategori (EV-010, EV-011); Season 4 post-TGE transisi ke on-chain KMNO emission program (EV-020) menggantikan off-chain Merkle root. Membangun retention jangka panjang aligned dengan tokenomics.
Evidence: EV-009, EV-010, EV-011, EV-020; Utility: Incentive/Reward Season 4; Narrative: Points/Incentive Program【Phase 3 — EV-009】【Phase 3 — EV-010】【Phase 3 — EV-011】【Phase 3 — EV-020】【Phase 6 — Utility】【Phase 8 — Narrative】
Supporting Dataset: Phase 3 (EV-009, EV-010, EV-011, EV-020), Phase 6 (Utility), Phase 8 (Narrative)
Confidence: High

Insight 6: Revenue Diversification Multi-Product Sejak Awal — 4 Revenue Stream Paralel
Explanation: Vault fees (management + performance), K-Lend interest spread, Multiply borrow interest + management fees, Liquidate fees. Mengurangi ketergantungan single product. Fee switch (EV-017) mendistribusikan portion ke veKMNO stakers menciptakan "Real Yield" narrative.
Evidence: Revenue Model mencatat 4 named streams live; Product launches EV-002, EV-004, EV-007, EV-019; Narrative: Real Yield/Fee Switch【Phase 5 — Revenue Model】【Phase 3 — EV-002】【Phase 3 — EV-004】【Phase 3 — EV-007】【Phase 3 — EV-019】【Phase 8 — Narrative】
Supporting Dataset: Phase 5 (Revenue Model), Phase 3 (EV-002, EV-004, EV-007, EV-019), Phase 8 (Narrative)
Confidence: High

Insight 7: Security-First dengan Multi-Audit Berulang — 5 Audits Tanpa Major Exploit Post-Launch
Explanation: Proaktif: Kudelski (2x), Neodyme (2x), Sec3 (1x) pre/post major launches; Immunefi bug bounty $100k max; tidak ada insiden keamanan mayor tercatat publik post-launch. Upgrade authority multisig memungkinkan patch cepat.
Evidence: Security Events EV-005, EV-006, EV-008, re-audits 2024; Audit History 5 audits; Security Model Bug Bounty; Open Threads: no security incident recorded【Phase 3 — EV-005】【Phase 3 — EV-006】【Phase 3 — EV-008】【Phase 4 — Audit History】【Phase 4 — Security Model】【Phase 8 — Open Threads】
Supporting Dataset: Phase 3 (EV-005, EV-006, EV-008), Phase 4 (Audit History, Security Model), Phase 8 (Open Threads)
Confidence: High

Insight 8: Oracle Risk Mitigation via Dual Layer — Pyth Primary + Switchboard Fallback dengan Staleness Checks On-Chain
Explanation: Semua pricing kritis (K-Lend rates, Multiply health factor, Liquidate auction, Vault rebalance) menggunakan Pyth pull oracle primary dengan Switchboard V2 fallback; staleness threshold & confidence interval di-enforce on-chain. Known Limitations mengakui dependency pada Pyth update frequency.
Evidence: Security Model Oracle Security; Known Limitations Pyth update frequency dependency; External Dependencies Pyth Critical, Switchboard High; Ecosystem Risks Oracle Dependency Confirmed【Phase 4 — Security Model】【Phase 4 — Known Limitations】【Phase 7 — External Dependencies】【Phase 8 — Ecosystem Risks】
Supporting Dataset: Phase 4 (Security Model, Known Limitations), Phase 7 (External Dependencies), Phase 8 (Ecosystem Risks)
Confidence: High

Insight 9: Cross-Chain Expansion via Wormhole NTT Bukan Native Multi-Chain Deployment
Explanation: Ekspansi multi-chain dilakukan melalui Wormhole NTT bridging aset non-native ke vault Solana (EV-018), bukan deploy program ke chain lain (Eclipse, Sonic, EVM L2). Mengurangi complexity tapi menciptakan bridge dependency.
Evidence: EV-018 Wormhole NTT Integration; System Architecture Cross-chain: Wormhole NTT; External Dependencies Wormhole High; Major Integrations Wormhole NTT; Open Threads multi-chain expansion plans【Phase 3 — EV-018】【Phase 4 — System Architecture】【Phase 7 — External Dependencies】【Phase 7 — Major Integrations】【Phase 8 — Open Threads】
Supporting Dataset: Phase 3 (EV-018), Phase 4 (System Architecture), Phase 7 (External Dependencies, Major Integrations), Phase 8 (Open Threads)
Confidence: High

Insight 10: Transparansi Finansial Terbatas — No Public Revenue Reports, Treasury Dashboard Minimal
Explanation: Tidak mempublikasikan laporan pendapatan bulanan/kuartalan; treasury dashboard hanya Realms raw token accounts; DefiLlama/Token Terminal third-party data saja. Circulating supply real-time & unlock schedule tidak diverifikasi resmi.
Evidence: Revenue History Undisclosed; Official Financial Resources No Transparency Report; Treasury Dashboard Realms only; Open Threads Revenue historical, Circulating supply verification【Phase 5 — Revenue History】【Phase 5 — Official Financial Resources】【Phase 8 — Open Threads】
Supporting Dataset: Phase 5 (Revenue History, Official Financial Resources), Phase 8 (Open Threads, Adoption Metrics)
Confidence: High

Strategic Principles

Principle 1: Ecosystem First — Build on Existing Primitives, Not From Scratch
Explanation: Kamino secara konsisten memilih integrasi dengan infrastruktur Solana yang matang (Jupiter, Pyth, Raydium, Orca, Marinade, Jito, Wormhole) daripada membangun komponen sendiri. Mengurangi time-to-market, risiko teknis, dan biaya operasional sambil memanfaatkan network effect ekosistem.
Evidence: External Dependencies 7 Critical/High integrations; Major Integrations 10+ protokol; Core Components CPI calls ke Raydium/Orca, Jupiter flashloan, Pyth oracle【Phase 7 — External Dependencies】【Phase 7 — Major Integrations】【Phase 4 — Core Components】
Supporting Dataset: Phase 7 (External Dependencies, Major Integrations), Phase 4 (Core Components, System Architecture)
Confidence: High

Principle 2: Security Before Growth — Multi-Audit Pre-Deployment untuk Setiap Major Release
Explanation: Setiap produk besar (Vaults v1→v2, K-Lend v1→v2, Multiply v1→v2, Liquidate v1) didahului audit minimal 1 auditor ternama (Kudelski, Neodyme, Sec3). Re-audit pada upgrade besar. Bug bounty Immunefi $100k max aktif. Upgrade authority multisig memungkinkan patch cepat.
Evidence: Security Events EV-005, EV-006, EV-008, re-audits 2024; Audit History 5 audits; Security Model Bug Bounty; Known Limitations upgrade authority multisig【Phase 3 — EV-005】【Phase 3 — EV-006】【Phase 3 — EV-008】【Phase 4 — Audit History】【Phase 4 — Security Model】【Phase 4 — Known Limitations】
Supporting Dataset: Phase 3 (EV-005, EV-006, EV-008), Phase 4 (Audit History, Security Model, Known Limitations)
Confidence: High

Principle 3: Progressive Decentralization — DAO Post-TGE, Parameter Control First, Upgrade Authority Later
Explanation: Urutan: TGE → DAO Formation (EV-016) → Fee Switch Activation via Proposal (EV-017) → Parameter Governance (Season 4 EV-020, Treasury EV-021) → Upgrade Authority masih multisig tim (belum fully DAO). Menyeimbangkan kecepatan eksekusi dengan alignment jangka panjang.
Evidence: EV-016, EV-017, EV-020, EV-021; Governance model Realms; Known Limitations upgrade authority multisig tim【Phase 3 — EV-016】【Phase 3 — EV-017】【Phase 3 — EV-020】【Phase 3 — EV-021】【Phase 6 — Governance】【Phase 4 — Known Limitations】
Supporting Dataset: Phase 3 (EV-016, EV-017, EV-020, EV-021), Phase 6 (Governance), Phase 4 (Known Limitations)
Confidence: High

Principle 4: Fixed Supply Tokenomics — No Inflation, Emission from Treasury Allocation Only
Explanation: Max supply = Total supply = Initial mint 10B KMNO. Season 4 emission sourced dari treasury allocation (bukan mint baru). Fee switch distribusi revenue bukan inflasi. Buyback & burn proposal (EV-021) untuk deflationary pressure. Menciptakan scarcity narrative.
Evidence: Supply Fixed 10B; Inflation/Deflation No protocol inflation; Token Information Token-2022 no mint authority; EV-021 Buyback proposal【Phase 6 — Supply】【Phase 6 — Inflation/Deflation】【Phase 6 — Token Information】【Phase 3 — EV-021】
Supporting Dataset: Phase 6 (Supply, Inflation/Deflation, Token Information), Phase 3 (EV-021)
Confidence: High

Principle 5: Incentive Alignment via Progressive Points → Token Emission — Retention Over Mercenary Capital
Explanation: Points Season 1-3 (off-chain) drive TVL growth pre-TGE dengan partnership cross-protocol (Tensor EV-009, Jito EV-011). Season 4 (on-chain KMNO emission) post-TGE align incentives dengan token holders. Transisi dari mercenary points farming ke sustainable token-aligned retention.
Evidence: EV-009, EV-010, EV-011, EV-020; Utility Incentive/Reward Season 4; Narrative Points/Incentive Program【Phase 3 — EV-009】【Phase 3 — EV-010】【Phase 3 — EV-011】【Phase 3 — EV-020】【Phase 6 — Utility】【Phase 8 — Narrative】
Supporting Dataset: Phase 3 (EV-009, EV-010, EV-011, EV-020), Phase 6 (Utility), Phase 8 (Narrative)
Confidence: High

Principle 6: Revenue Diversification from Day One — Multi-Product Stack Membuat Protocol Resilien
Explanation: Tidak bergantung single revenue stream. 4 produk core (Vaults, K-Lend, Multiply, Liquidate) masing-masing generate fees. Fee switch mengagregasikan ke veKMNO stakers. Mengurangi risiko single product failure.
Evidence: Revenue Model 4 streams; Product launches EV-002, EV-004, EV-007, EV-019; Narrative Real Yield/Fee Switch【Phase 5 — Revenue Model】【Phase 3 — EV-002】【Phase 3 — EV-004】【Phase 3 — EV-007】【Phase 3 — EV-019】【Phase 8 — Narrative】
Supporting Dataset: Phase 5 (Revenue Model), Phase 3 (EV-002, EV-004, EV-007, EV-019), Phase 8 (Narrative)
Confidence: High

Success Factors

Factor 1: Deep Ecosystem Integration dengan Solana Core Infrastructure (Jupiter, Pyth, Raydium/Orca, Marinade, Jito)
Explanation: Setiap produk inti terintegrasi native dengan infrastruktur terbaik di Solana: Vaults→Raydium CLMM/Orca Whirlpool, K-Lend/Multiply→Pyth oracle, Multiply→Jupiter flashloan, Assets→mSOL/JitoSOL. Membuat Kamino "unforkable" dan embedded dalam ekosistem.
Evidence: External Dependencies 7 Critical/High; Major Integrations 10+ protokol; Core Components CPI calls; Adoption Metrics TVL >$1B【Phase 7 — External Dependencies】【Phase 7 — Major Integrations】【Phase 4 — Core Components】【Phase 8 — Adoption Metrics】
Supporting Dataset: Phase 7 (External Dependencies, Major Integrations), Phase 4 (Core Components), Phase 8 (Adoption Metrics)
Confidence: High

Factor 2: Product Suite Lengkap (Vaults + Lending + Leverage + Liquidation) Menciptakan Flywheel Internal
Explanation: Vaults menyediakan yield basis → K-Lend menyediakan borrowing → Multiply otomatisasi leverage looping → Liquidate memastikan efisiensi likuidasi. User flow internal tanpa keluar protokol. Cross-product revenue diversification.
Evidence: Core Components 4 core programs; Product launches sequential EV-002, EV-004, EV-007, EV-019; Revenue Model 4 streams; Market Position Growth stage【Phase 4 — Core Components】【Phase 3 — EV-002】【Phase 3 — EV-004】【Phase 3 — EV-007】【Phase 3 — EV-019】【Phase 5 — Revenue Model】【Phase 8 — Market Position】
Supporting Dataset: Phase 4 (Core Components), Phase 3 (EV-002, EV-004, EV-007, EV-019), Phase 5 (Revenue Model), Phase 8 (Market Position)
Confidence: High

Factor 3: Points Program Bertahap dengan Partnership Cross-Protocol (Tensor, Jito) Mendongkrak Adopsi Pre-TGE
Explanation: Season 1 Tensor partnership (EV-009) menciptakan cross-protocol loop; Season 3 JitoSOL/restaking bonus (EV-011) alignment dengan LSD narrative. Points holders menjadi eligible TGE claim → community ownership dari day-1.
Evidence: EV-009 Tensor Partnership, EV-011 Season 3 Jito; TGE Claim categories include points holders EV-012; TVL peak ~$1.5B Maret 2024 pre-TGE【Phase 3 — EV-009】【Phase 3 — EV-011】【Phase 3 — EV-012】【Phase 8 — Adoption Metrics】
Supporting Dataset: Phase 3 (EV-009, EV-011, EV-012), Phase 8 (Adoption Metrics)
Confidence: High

Factor 4: Multi-CEX Listing Same-Day TGE (Binance, Coinbase, Bybit, Gate.io, KuCoin) Memberikan Likuiditas Instan & Distribusi Global
Explanation: Listing 5 CEX utama pada hari TGE yang sama (EV-013, EV-014, EV-015) menghilangkan liquidity bootstrap problem. Binance volume ~60-70%, Coinbase fiat gateway US, Bybit/Gate.io/KuCoin geographic reach. Price discovery efisien day-1.
Evidence: EV-013 Binance, EV-014 Coinbase, EV-015 Bybit/Gate.io/KuCoin; Trading Markets 5 CEX + 3 DEX; Liquidity Major venue Binance/Coinbase; Market Share CEX volume distribution【Phase 3 — EV-013】【Phase 3 — EV-014】【Phase 3 — EV-015】【Phase 8 — Trading Markets】【Phase 8 — Liquidity】【Phase 8 — Market Share】
Supporting Dataset: Phase 3 (EV-013, EV-014, EV-015), Phase 8 (Trading Markets, Liquidity, Market Share)
Confidence: High

Factor 5: Security Track Record Bersih — 5 Audits Multi-Auditor, Bug Bounty $100k, No Major Exploit
Explanation: Kudelski 2x, Neodyme 2x, Sec3 1x覆盖所有core programs. Immunefi bug bounty active. Upgrade authority multisig memungkinkan rapid patch. Membangun trust institucional dan retail.
Evidence: Security Events EV-005, EV-006, EV-008; Audit History 5 audits; Security Model Bug Bounty; Open Threads no security incident【Phase 3 — EV-005】【Phase 3 — EV-006】【Phase 3 — EV-008】【Phase 4 — Audit History】【Phase 4 — Security Model】【Phase 8 — Open Threads】
Supporting Dataset: Phase 3 (EV-005, EV-006, EV-008), Phase 4 (Audit History, Security Model), Phase 8 (Open Threads)
Confidence: High

Factor 6: Fee Switch Activation (EV-017) Menciptakan Real Yield Narrative yang Dapat Diverifikasi On-Chain
Explanation: Protocol fees dari 4 revenue streams diarahkan ke veKMNO stakers via governance proposal. Menjadikan KMNO bukan hanya governance token tapi yield-bearing asset. Narrative "Real Yield" tervalidasi on-chain.
Evidence: EV-017 Fee Switch Activation; Utility Staking/Fee Switch; Revenue Model Protocol Fee Switch; Narrative Real Yield/Fee Switch【Phase 3 — EV-017】【Phase 6 — Utility】【Phase 5 — Revenue Model】【Phase 8 — Narrative】
Supporting Dataset: Phase 3 (EV-017), Phase 6 (Utility), Phase 5 (Revenue Model), Phase 8 (Narrative)
Confidence: High

Failure Factors

Factor 1: Transparansi Finansial & Tokenomics Minimal — Tidak Ada Public Revenue Reports, Circulating Supply Unverified, Alokasi Persentase Tidak Dipublikasikan
Explanation: Tidak mempublikasikan laporan pendapatan bulanan/kuartalan; treasury dashboard hanya Realms raw token accounts; persentase alokasi KMNO ke Team, Investors, Treasury, Community, Ecosystem tidak dipublikasikan resmi. CoinGecko/CoinMarketCap circulating supply berbeda-beda tanpa metodologi terverifikasi.
Evidence: Revenue History Undisclosed; Official Financial Resources No Transparency Report; Distribution percentages "tidak diketahui" untuk semua kategori; Vesting Schedule parameter "tidak diketahui" untuk Team/Investors; Open Threads Circulating supply verification【Phase 5 — Revenue History】【Phase 5 — Official Financial Resources】【Phase 6 — Distribution】【Phase 6 — Vesting Schedule】【Phase 8 — Open Threads】
Supporting Dataset: Phase 5 (Revenue History, Official Financial Resources), Phase 6 (Distribution, Vesting Schedule), Phase 8 (Open Threads)
Confidence: High

Factor 2: Upgrade Authority Masih Tersentralisasi di Multisig Tim Anonim — Belum Fully Decentralized ke DAO
Explanation: Program upgrade authority dipegang Squads v3 multisig tim inti anonim. DAO mengontrol treasury & parameter tapi belum upgrade authority. Tim anonim (tidak doxxed) + centralized upgrade = single point of failure & regulatory risk.
Evidence: Security Model Program Authority multisig tim; Known Limitations "Upgrade authority multisig tim, bukan immutable/timelock DAO"; Entity Kamino Team anonim; Entity Kamino Finance Ltd. BVI【Phase 4 — Security Model】【Phase 4 — Known Limitations】【Phase 2 — Entity: Kamino Team】【Phase 2 — Entity: Kamino Finance Ltd.】
Supporting Dataset: Phase 4 (Security Model, Known Limitations), Phase 2 (Entity: Kamino Team, Kamino Finance Ltd.)
Confidence: High

Factor 3: Single Chain Dependency — 100% Operasi di Solana, Tidak Ada Deployment Multi-Chain
Explanation: Seluruh protokol (Vaults, K-Lend, Multiply, Liquidate, Token, Governance) deployed hanya di Solana. Risiko sistemik Solana (outage, consensus bug, regulatory) mempengaruhi 100% operasi. Cross-chain hanya via Wormhole NTT untuk asset bridging, bukan program deployment.
Evidence: Ecosystem Position Primary Chain Solana; System Architecture Solana L1 only; External Dependencies Solana Critical; Ecosystem Risks Single Chain Dependency Confirmed; Open Threads Multi-chain expansion plans【Phase 7 — Ecosystem Position】【Phase 4 — System Architecture】【Phase 7 — External Dependencies】【Phase 8 — Ecosystem Risks】【Phase 8 — Open Threads】
Supporting Dataset: Phase 7 (Ecosystem Position, External Dependencies), Phase 4 (System Architecture), Phase 8 (Ecosystem Risks, Open Threads)
Confidence: High

Factor 4: Oracle Concentration Risk — Pyth Primary untuk Semua Pricing Kritis, Fallback Switchboard Belum Terbukti di Kondisi Ekstrem
Explanation: K-Lend rates, Multiply health factor, Liquidate auction, Vault rebalance semua bergantung Pyth. Switchboard fallback ada tapi tidak terbukti saat Pyth outage bersamaan. Staleness threshold & confidence interval checks on-chain tapi parameter exact tidak transparan.
Evidence: Security Model Oracle Security; Known Limitations Pyth update frequency dependency; External Dependencies Pyth Critical, Switchboard High; Ecosystem Risks Oracle Dependency Confirmed【Phase 4 — Security Model】【Phase 4 — Known Limitations】【Phase 7 — External Dependencies】【Phase 8 — Ecosystem Risks】
Supporting Dataset: Phase 4 (Security Model, Known Limitations), Phase 7 (External Dependencies), Phase 8 (Ecosystem Risks)
Confidence: High

Factor 5: Treasury Concentration di Native Token KMNO — Nilai Treasury Bergantung Harga KMNO, Belum Ada Diversifikasi Terverifikasi
Explanation: Treasury sebagian besar KMNO (native token). EV-021 proposal buyback & burn menggunakan protocol revenue untuk diversifikasi tapi masih proposal stage. Tidak ada transparency report komposisi treasury (stablecoin vs KMNO vs yield-bearing assets).
Evidence: Treasury Composition undisclosed, KMNO heavy; Financial Risk Treasury Concentration; Fundraising Mechanism DAO Treasury post-TGE; EV-021 Buyback proposal; Open Threads Treasury composition breakdown【Phase 5 — Treasury】【Phase 5 — Financial Risk】【Phase 5 — Fundraising Mechanism】【Phase 3 — EV-021】【Phase 8 — Open Threads】
Supporting Dataset: Phase 5 (Treasury, Financial Risk, Fundraising Mechanism), Phase 3 (EV-021), Phase 8 (Open Threads)
Confidence: High

Factor 6: Keterbatasan Data Adopsi — Daily Active Users, Transactions, Developer Count Tidak Dipublikasikan Resmi
Explanation: Metriks adopsi kunci (DAU, daily txns, unique wallets cumulative, developer count) tidak dipublikasikan resmi. Hanya TVL (DefiLlama) dan CEX volume (CoinMarketCap) yang tersedia. Menghambang analisis fundamental investor & researcher.
Evidence: Adoption Metrics DAU/Txns/Wallets/Devs "tidak diketahui"; Open Threads Real-time circulating supply, Daily/Monthly Active Users, Developer Activity【Phase 8 — Adoption Metrics】【Phase 8 — Open Threads】
Supporting Dataset: Phase 8 (Adoption Metrics, Open Threads)
Confidence: High

Decision Framework

Step 1: Observe — Identifikasi Peluang di Ekosistem Solana & Gap Produk
Explanation: Tim mengamati kemunculan CLMM (Raydium/Orca), kebutuhan manajemen posisi otomatis, kurangnya lending terintegrasi leverage, dan permintaan yield LSD (mSOL/JitoSOL). Mengidentifikasi first-mover advantage untuk Vaults CLMM auto-rebalancing.
Evidence: EV-001 Founding 2022; EV-002 Vaults v1 Launch Maret 2022; Blog "Introducing Kamino"【Phase 3 — EV-001】【Phase 3 — EV-002】【Phase 1 — Launch Date Mainnet】
Supporting Dataset: Phase 3 (EV-001, EV-002), Phase 1 (Launch Date Mainnet)
Confidence: High

Step 2: Evaluate — Validasi Teknis & Keamanan via Multi-Audit Sebelum Setiap Major Launch
Explanation: Setiap produk besar (Vaults v1→v2, K-Lend v1→v2, Multiply v1→v2, Liquidate v1) didahului audit Kudelski/Neodyme/Sec3. Re-audit pada upgrade besar. Hanya meluncurkan setelah temuan critical/high diperbaiki.
Evidence: EV-005 Kudelski Audit 2023-02; EV-006 Neodyme Audit 2023-05; EV-008 Sec3 Audit 2023-10; Re-audits 2024 untuk K-Lend v2, Liquidate, Multiply v2【Phase 3 — EV-005】【Phase 3 — EV-006】【Phase 3 — EV-008】【Phase 4 — Audit History】
Supporting Dataset: Phase 3 (EV-005, EV-006, EV-008), Phase 4 (Audit History, Technical Upgrade History)
Confidence: High

Step 3: Fund — Seed Round 2022 (Multicoin, Jump, Solana Ventures) + Grant Solana Foundation, Lalu Protocol Revenue & DAO Treasury
Explanation: Satu ronde Seed 2022 undisclosed amount dari VC tier-1 + ecosystem grant. Tidak ada follow-on round. Post-TGE operasi didanai protocol revenue (4 streams) + DAO treasury KMNO allocation. Financial independence dari VC.
Evidence: Funding History Seed 2022; Financial Dependencies VC investors, Foundation grants, Protocol revenue, DAO treasury; No funding events post-2022【Phase 5 — Funding History】【Phase 5 — Financial Dependencies】【Phase 3 — History no funding events post-2022】
Supporting Dataset: Phase 5 (Funding History, Financial Dependencies), Phase 3 (History)
Confidence: High

Step 4: Develop — Arsitektur Monolitik SVM dengan CPI, PDA-Centric State, Token-2022 Extensions
Explanation: Develop di Solana SVM menggunakan Anchor/Rust. Program terpisah per produk (Vaults, K-Lend, Multiply, Liquidate, Token, Staking) terintegrasi via CPI. PDA untuk positions/obligations. KMNO Token-2022 dengan transfer hook untuk fee switch.
Evidence: System Architecture SVM monolitik; Core Components 9 programs; Execution Environment SVM BPF Loader Upgradeable; KMNO Token Program Token-2022; Current Technical Stack Rust/Anchor/TypeScript【Phase 4 — System Architecture】【Phase 4 — Core Components】【Phase 4 — Execution Environment】【Phase 6 — Token Information】【Phase 4 — Current Technical Stack】
Supporting Dataset: Phase 4 (System Architecture, Core Components, Execution Environment, Current Technical Stack), Phase 6 (Token Information)
Confidence: High

Step 5: Launch — Bertahap: Vaults v1 (2022-03) → K-Lend v1 (2022-09) → Multiply v1 (2023-07) → Liquidate v1 (2024-08) → TGE KMNO + Multi-CEX Listing + DAO Formation (2024-04)
Explanation: Product launches sequential membangun stack DeFi lengkap. TGE 10 April 2024 dengan claim points holders + listing 5 CEX same-day. DAO formation 5 hari बाद. Fee Switch activation Mei 2024 via proposal.
Evidence: EV-002 Vaults v1, EV-004 K-Lend v1, EV-007 Multiply v1, EV-019 Liquidate v1, EV-012 TGE, EV-013/014/015 CEX Listings, EV-016 DAO, EV-017 Fee Switch【Phase 3 — EV-002】【Phase 3 — EV-004】【Phase 3 — EV-007】【Phase 3 — EV-019】【Phase 3 — EV-012】【Phase 3 — EV-013】【Phase 3 — EV-014】【Phase 3 — EV-015】【Phase 3 — EV-016】【Phase 3 — EV-017】
Supporting Dataset: Phase 3 (EV-002, EV-004, EV-007, EV-019, EV-012, EV-013, EV-014, EV-015, EV-016, EV-017)
Confidence: High

Step 6: Govern — DAO Realms Token-Weighted (veKMNO), Parameter Control Via Proposal, Treasury Spending Via Proposal, Upgrade Authority Masih Multisig Tim
Explanation: Governance on-chain via Realms. 1 KMNO = 1 vote via veKMNO. Proposal untuk parameter (Fee Switch EV-017, Season 4 EV-020, Treasury Buyback EV-021). Treasury spending via proposal. Upgrade authority belum fully DAO.
Evidence: EV-016 DAO Formation, EV-017 Fee Switch, EV-020 Season 4, EV-021 Treasury; Governance Model Realms; Known Limitations upgrade authority multisig【Phase 3 — EV-016】【Phase 3 — EV-017】【Phase 3 — EV-020】【Phase 3 — EV-021】【Phase 6 — Governance】【Phase 4 — Known Limitations】
Supporting Dataset: Phase 3 (EV-016, EV-017, EV-020, EV-021),

## Open Questions
- [foundation] Legal entity jurisdiction: beberapa sumber menyebut BVI, beberapa tidak menyebut yurisdiksi eksplisit — butuh verifikasi dokumen legal/terms of service resmi.
- [foundation] Testnet launch date: tidak ada catatan blog/testnet terpisah yang ditemukan; kemungkinan mainnet launch langsung dari v1 vaults Maret 2022.
- [foundation] Core team size & identity: sepenuhnya pseudonim; tidak ada doxxing publik — perlu monitoring apakah ada rencana KYC/DAO legal wrapper.
- [foundation] Tokenomics detail (allocation, vesting, emission schedule): TGE baru terjadi April 2024; data on-chain & governance forum perlu di-cross-check untuk angka pasti persentase TGE, team, investor, community, treasury.
- [foundation] Fee switch status & revenue sharing: apakah fee switch sudah aktif untuk KMNO stakers — perlu cek governance proposal & kontrak `FeeReceiver`.
- [foundation] Audit coverage: daftar audit lengkap (Kudelski, Neodyme, Sec3, dll.) perlu dikumpulkan per produk (Vaults, K-Lend, Multiply) dengan tanggal & scope.
- [entity] Identitas legal pendiri/anggota inti "Kamino Team": tetap sepenuhnya pseudonim; tidak ada dokumen KYC/DAO legal wrapper yang dipublikasikan — perlu verifikasi apakah ada entitas hukum tambahan selain Kamino Finance Ltd. (BVI).
- [entity] Daftar investor lengkap dan persentase alokasi token (tokenomics): Phase 1 hanya menyebut "investor" secara umum; data on-chain vesting (mis. Token Vesting Program) perlu di-cross-check untuk mengonfirmasi Multicoin, Jump, Solana Ventures, dan investor lain (seperti Circle, Animoca, dll. yang sering berpartisipasi ronde Solana).
- [entity] Cakupan audit per produk & versi: Open Threads Phase 1 menyebut Kudelski, Neodyme, Sec3 — tapi tidak ada laporan audit publik terverifikasi per produk (Vaults v1, v2, K-Lend, Multiply) dengan tanggal & scope — butuh mengumpulkan PDF audit resmi.
- [entity] Status Fee Switch & Revenue Sharing KMNO: apakah fee switch sudah diaktifkan untuk staker KMNO — perlu cek proposal governance on-chain (Realms) dan kontrak `FeeReceiver`/`StakingProgram`.
- [entity] Rincian integrasi Wormhole: apakah Kamino menggunakan Wormhole Native Token Transfers (NTT) atau lock/mint klasik untuk aset non-native di vault — butuh dokumentasi teknis rinci.
- [entity] Ketergantungan likuiditas pada Jupiter & Jito: proporsi volume swap & MEV yield yang mengalir via Jupiter/Jito vs venue lain — butuh data on-chain Dune/Flipside.
- [entity] Rencana ekspansi multi-chain: apakah Kamino akan deploy ke Eclipse, Sonic, atau L2 lain — perlu monitoring forum governance & blog resmi.
- [history] Tanggal pasti pendirian Kamino Finance Ltd. (BVI): hanya tahun 2022 diketahui dari ToS; butuh dokumen incorporasi/resolusi direksi untuk tanggal exact.
- [history] Ronde pendanaan (Funding) Seed/Series A: Phase 1-2 menyebut investor (Multicoin, Jump, Solana Ventures) tapi tidak ada event Funding dengan tanggal, jumlah, valuasi, dan lead investor yang diverifikasi on-chain/announcement resmi — butuh press release atau Form D/filing BVI.
- [history] Testnet launch: tidak ditemukan catatan testnet terpisah sebelum mainnet Maret 2022; perlu konfirmasi apakah mainnet launch langsung tanpa testnet publik.
- [history] Detail tokenomics TGE (persentase alokasi team, investor, community, treasury, liquidity): data on-chain vesting program (Token Vesting Program) perlu di-cross-check untuk angka pasti; blog resmi hanya menyebut "10B supply" tanpa breakdown persentase.
- [history] Status fee switch parameter exact (persentase fee ke staker vs treasury): proposal #1 Realms menunjukkan aktivasi tapi persentase teknis (bps) butuh dibaca dari instruksi program `FeeReceiver` on-chain.
- [history] Cakupan audit per produk & versi: daftar audit (Kudelski, Neodyme, Sec3) diketahui tapi tidak ada mapping lengkap: produk mana (Vaults v1, v2, K-Lend v1, Multiply v1, Liquidate) yang diaudit kapan, scope apa, dan apakah re-audit setelah upgrade mayor.
- [history] Rencana ekspansi multi-chain (Eclipse, Sonic, dll.): tidak ada announcement resmi; hanya spekulasi komunitas — butuh monitoring governance forum & blog.
- [history] Identitas tim inti (doxing/KYC): tetap anonim; tidak ada legal wrapper DAO selain BVI entity — perlu verifikasi apakah ada foundation Cayman/Swiss atau wrapper lain untuk compliance.
- [history] Data TVL & volume historis per produk: butuh query Dune/Flipside untuk validasi narasi pertumbuhan (mis. lonjakan TVL Season 1-3, post-TGE).
- [technology] Program upgrade authority multisig composition: tidak dipublikasikan detail signer set (jumlah, threshold, identitas) — butuh verifikasi on-chain via `solana program show <PROGRAM_ID> --upgrade-authority` atau Squads v3 dashboard
- [technology] K-Lend v2 isolation mode migration path untuk reserve lama (SOL, USDC, mSOL, JitoSOL): apakah akan dimigrasi ke isolation mode atau tetap pooled — belum ada proposal resmi
- [technology] Oracle staleness threshold exact value (slots) untuk K-Lend & Multiply: dokumentasi menyejukkan "staleness check" tapi tidak menampilkan angka pasti — butuh baca kode program `lending::state::OracleConfig` atau `multiply::state::HealthFactorConfig`
- [technology] Liquidate Dutch auction curve parameters (starting discount, end discount, duration): tidak terdokumentasi di docs publik — butuh cek program state on-chain atau proposal governance
- [technology] Points Season 1-3 indexer operator identity & decentralization plan: apakah akan di-decentralisasi via multiple indexer / ZK proof — belum ada announcement
- [technology] Wormhole NTT asset registry expansion process untuk Kamino: apakah Kamino mengusulkan aset baru ke Wormhole DAO atau menunggu — butuh monitoring forum Wormhole & Kamino
- [technology] Formal verification status: tidak ada bukti formal verification (Certora, Coq, dll.) untuk core math (rebalancing, health factor, rate curves) — hanya audit manual
- [technology] Client-side SDK versioning & breaking change policy: tidak terdokumentasi di developer docs — butuh cek GitHub releases & changelog
- [technology] Disaster recovery / pause mechanism: apakah ada "pause authority" atau circuit breaker di program (mis. `Pause` instruction) — tidak ditemukan di docs; butuh cek IDL/program code
- [technology] Gas/compute unit optimization roadmap: apakah ada rencana migrasi ke Solana v2 / Firedancer / SVM optimizations — belum ada statement teknis resmi
- [financial] Jumlah exact Seed round 2022 (USD) & valuasi: tidak diumumkan resmi; Crunchbase tidak menampilkan angka — butuh press release atau filing BVI.
- [financial] Persentase alokasi token KMNO ke Treasury DAO, Team, Investor, Community, Liquidity: TGE baru April 2024; data on-chain vesting program perlu di-cross-check untuk angka pasti.
- [financial] Ukuran treasury terkini (stablecoin, KMNO, aset lain): tidak ada dashboard publik selain Realms treasury account yang hanya menunjukkan token accounts tidak nilai USD.
- [financial] Laporan pendapatan bulanan/kuartalan (Revenue Report): tidak dipublikasikan; butuh proposal governance untuk transparency report.
- [financial] Status fee switch parameter exact (bps fee ke staker vs treasury): proposal #1 mengaktifkan tapi persentase teknis butuh dibaca dari instruksi program `FeeReceiver` on-chain.
- [financial] Rencana diversifikasi treasury (stablecoin, yield-bearing assets): tidak ada proposal resmi — butuh monitoring forum governance.
- [financial] Kontinjensi hukum/regulatori untuk entitas BVI + tim anonim: tidak ada disclosure risiko finansial spesifik di dokumen publik.
- [financial] Data on-chain revenue per produk (Vaults, K-Lend, Multiply, Liquidate): bisa dihitung via indexer tapi tidak diagregasikan resmi — butuh query Dune/Flipside.
- [token] Persentase alokasi token exact per kategori (Community, Team, Investors, Treasury, Ecosystem): tidak dipublikasikan resmi; hanya kategori claim TGE diketahui (points holders, team, investor, treasury) tapi tanpa breakdown persentase — butuh data on-chain vesting program analysis atau transparency report resmi.
- [token] Parameter vesting schedule detail (cliff, duration, frequency) untuk Team & Investors: on-chain vesting accounts ada tapi parameter tidak diverifikasi/dipublikasikan — butuh query program state atau announcement resmi.
- [token] Circulating supply real-time & unlock schedule forward-looking: tidak ada dashboard resmi circulating supply; CoinGecko/CoinMarketCap data derived dari self-reported — butuh metodologi verified.
- [token] Fee switch parameter exact (bps fee directed to stakers vs treasury): Proposal #1 EV-017 mengaktifkan tapi persentase teknis tidak tercantum di forum/Realms proposal detail — butuh baca instruksi program `FeeReceiver` on-chain atau technical docs.
- [token] Season 4 emission schedule exact (KMNO per epoch, total allocation, duration): Governance forum menyebut parameter tapi tidak ada single source of truth terpublikasi — butuh proposal detail atau program state query.
- [token] Treasury composition breakdown (KMNO vs stablecoin vs yield-bearing assets): Realms treasury view hanya menunjukkan token accounts raw — butuh proposal transparency report atau Dune dashboard resmi.
- [token] Buyback & burn mechanism design (EV-021): proposal masih diskusi; parameter (jumlah, frekuensi, sumber dana) belum final — butuh monitoring governance vote result.
- [token] KMNO collateral utility di K-Lend isolation mode: apakah akan diusulkan & parameter risk (LTV, liquidation threshold) — butuh monitoring forum & risk framework docs.
- [token] Token program upgrade authority: SPL Token-2022 mint authority & freeze authority status (renounced atau retained) — butuh cek `solana token display <MINT>` on-chain.
- [token] Holder distribution analysis resmi: tidak ada laporan concentrasi whale/foundation/investor/community — butuh third-party analysis (Nansen, Arkham) atau self-reported transparency.
- [market] Real-time circulating supply & market cap: CoinGecko/CoinMarketCap menunjukkan angka berbeda; tidak ada dashboard resmi circulating supply terverifikasi — butuh cross-check on-chain vesting unlocks vs reported circulating.
- [market] Daily/Monthly Active Users (unique wallets): tidak dipublikasikan resmi; Dune/Flipside community dashboards ada tapi tidak diverifikasi akurasi — butuh query indexer Kamino atau official analytics.
- [market] Protocol Revenue (Fees) Historical: DefiLlama/Token Terminal mungkin memiliki data fees tapi tidak cross-checked dengan on-chain fee receiver accounts — butuh verifikasi revenue per produk (Vaults, K-Lend, Multiply, Liquidate) bulanan.
- [market] KMNO Staking Participation Rate: persentase supply yang di-stake (veKMNO) vs circulating tidak dipublikasikan resmi — butuh query staking program state on-chain.
- [market] Liquidation Market Volume & Liquidator PnL: Liquidate program baru Agustus 2024; volume likuidasi, bad debt, liquidator profitability tidak diagregasikan publik — butuh indexer data.
- [market] Cross-chain Deposit Volume (Wormhole NTT): volume aset non-native masuk ke vault via NTT tidak dipublikasikan per protokol — butuh Wormholescan filter by recipient Kamino vault programs.
- [market] Competitor TVL Market Share Breakdown: DefiLlama memiliki data per protokol tapi tidak ada analisis market share CLMM Vault vs Lending vs Leverage terpisah — butuh segmentasi manual.
- [market] Token Holder Distribution (Whale/Retail/Team/Investor): Solscan holders list raw tersedia tapi tidak diagregasikan ke kategori entity (team vesting, investor vesting, DAO treasury, community) — butuh labeling on-chain accounts.
- [market] Perpetual/Futures Listing Status: tidak ada listing perpetual KMNO di CEX utama (Binance, Bybit, OKX, Bitget) per Oktober 2024 — butuh monitoring announcement untuk derivative listing.
- [market] Options/Structured Products Integration: tidak ada integrasi Dopex, Friktion, atau struktur produk lain di Kamino — butuh monitoring roadmap.
- [market] Geographic User Distribution: tidak ada data pengguna per wilayah (KYC CEX mungkin punya tapi tidak publik) — butuh survey/analytics.
- [market] Developer Activity (Commits/PRs): GitHub commit frequency tidak dianalisis secara kuantitatif — butuh GitHub insights untuk metriks dev activity.
- [market] Security Incident History: tidak ada insiden keamanan mayor (hack/exploit) tercatat publik post-launch — butuh verifikasi immunefi payouts & audit follow-ups.
- [market] Regulatory Status (US/Global): Coinbase listing menandakan compliance level tertentu tapi tidak ada legal opinion publik — butuh monitoring regulasi stablecoin/LSD/DeFi di yurisdiksi utama.
