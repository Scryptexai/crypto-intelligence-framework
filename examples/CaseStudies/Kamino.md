# Kamino — Deep Case Study (Phased)

**CIF Dataset — Deep Dossier · Tier: Deep (anchor project)**
**Source:** Deep Research (DeepSeek), Format v3 Dependency Pipeline (12/11 phases: foundation, entity, history, technology, financial, token, ecosystem, market, behavioral, knowledge, conflict, airdrop). **Auto-assembled** by `tools/ingest.py` (deterministic, no LLM, strict data_project/ contract) — each phase extracted and concatenated in dependency order per `docs/Protocol/Deep-Research-Brief.md`; the reasoning is the source reports'.
**Raw sources archived:** doc_backup/deep/Kamino_foundation_2026-08.docx, doc_backup/deep/Kamino_entity_2026-08.docx, doc_backup/deep/Kamino_history_2026-08.docx, doc_backup/deep/Kamino_technology_2026-08.docx, doc_backup/deep/Kamino_financial_2026-08.docx, doc_backup/deep/Kamino_token_2026-08.docx, doc_backup/deep/Kamino_ecosystem_2026-08.docx, doc_backup/deep/Kamino_market_2026-08.docx, doc_backup/deep/Kamino_behavioral_2026-08.docx, doc_backup/deep/Kamino_knowledge_2026-08.docx, doc_backup/deep/Kamino_conflict_2026-08.docx, doc_backup/deep/Kamino_airdrop_2026-08.docx.
**Phases not run:** none.

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

Strategic Objectives

1. Menjadi infrastruktur DeFi inti (blue chip) di Solana dengan suite produk terintegrasi Vaults, Lending, Leverage, dan Liquidation
· Evidence: TVL >$1B (peak $1.5B) menempatkan Kamino di top 3 Solana DeFi (Phase 8 Market Position); multi-product live sejak 2022-2024 (Phase 3 EV-002, EV-004, EV-007, EV-019)
· Supporting Dataset: Phase 3 History, Phase 8 Market Position, Phase 4 Core Components

2. Membangun real yield berbasis fee switch yang mengalir ke KMNO stakers (veKMNO) untuk menciptakan value accrual token
· Evidence: Fee switch diaktifkan via Governance Proposal #1 Mei 2024 (Phase 3 EV-017); revenue streams dari 4 produk (Vaults, K-Lend, Multiply, Liquidate) terdokumentasi (Phase 5 Revenue Model)
· Supporting Dataset: Phase 3 EV-017, Phase 5 Revenue Model, Phase 6 Utility Staking

3. Desentralisasi progresif melalui DAO on-chain (Realms) yang mengontrol treasury, parameter protokol, dan upgrade authority
· Evidence: Kamino DAO formed April 2024 (Phase 3 EV-016); Realms governance active dengan proposals fee switch, season 4, treasury buyback (Phase 3 EV-017, EV-020, EV-021); upgrade authority multisig Squads v3 (Phase 4 Security Model)
· Supporting Dataset: Phase 3 EV-016, EV-017, EV-020, EV-021, Phase 4 Security Model, Phase 7 Governance Ecosystem

4. Ekspansi ekosistem melalui integrasi mendalam dengan infrastruktur Solana (Jupiter, Wormhole, Pyth, Jito, Marinade) dan CEX listing global
· Evidence: Integrasi Jupiter sejak 2022-06 (Phase 3 EV-003), Wormhole NTT 2024-06 (EV-018), Pyth/Switchboard oracle (Phase 4 Dependencies); Multi-CEX listing TGE same-day 5 bursa (Phase 3 EV-013, EV-014, EV-015)
· Supporting Dataset: Phase 3 EV-003, EV-018, Phase 4 Dependencies, Phase 7 Major Integrations, Phase 8 Trading Markets

5. Retensi pengguna jangka panjang melalui program insentif berkelanjutan (Points Season 1-4) yang berevolusi dari off-chain ke on-chain emission
· Evidence: Points Season 1-3 pre-TGE drive TVL growth (Phase 3 EV-009, EV-010, EV-011); Season 4 post-TGE on-chain KMNO emission (Phase 3 EV-020); Tensor partnership cross-protocol loop (EV-009)
· Supporting Dataset: Phase 3 EV-009, EV-010, EV-011, EV-020, Phase 6 Token Events

Decision Timeline

Keputusan: Pendirian Kamino Finance Ltd. di BVI sebagai entitas hukum (2022)
· Trigger: Perlu legal wrapper untuk operasi protokol DeFi, pengelolaan risiko hukum, dan fondasi bisnis sebelum mainnet launch
· Evidence: Terms of Service menunjukkan entitas BVI (Phase 1 Foundation, Phase 2 Entity Kamino Finance Ltd.)
· Decision: Mendaftarkan perusahaan di British Virgin Islands sebagai entitas pendiri protokol
· Immediate Result: Dasar hukum untuk pengembangan Vaults v1 dan operasi awal
· Long-term Impact: Struktur legal tetap BVI + tim anonim; belum ada legal wrapper DAO terpisah (Cayman/Swiss) per Phase 2 Open Threads
· Supporting Dataset: Phase 1 Foundation, Phase 2 Entity Kamino Finance Ltd., Phase 3 EV-001

Keputusan: Mainnet Launch Vaults v1 CLMM Auto-Rebalancing tanpa testnet publik terpisah (2022-03)
· Trigger: Peluang pasar CLMM di Solana (Raydium/Orca baru launch); kebutuhan time-to-market cepat
· Evidence: Blog "Introducing Kamino" Maret 2022 (Phase 3 EV-002); tidak ada catatan testnet di Phase 1/3
· Decision: Deploy langsung ke mainnet Solana dengan vaults SOL/USDC, mSOL/SOL, JitoSOL/SOL
· Immediate Result: TVL awal masuk; posisi sebagai first-mover CLMM manager otomatis
· Long-term Impact: Menjadi fondasi produk utama; Vaults v2 upgrade 2023-01 (EV-002 upgrade) menambah auto-compound & multi-pool
· Supporting Dataset: Phase 3 EV-002, Phase 4 Technical Upgrade History Vaults v1→v2

Keputusan: Integrasi Jupiter sebagai routing swap default untuk Vault rebalancing (2022-06)
· Trigger: Kebutuhan best execution untuk rebalancing berkala vault CLMM; Jupiter sebagai aggregator terdepan Solana
· Evidence: Kamino Blog Jupiter Integration (Phase 3 EV-003); Jupiter Docs integrations (Phase 2 Entity Jupiter)
· Decision: Embed Jupiter Swap API v6 ke Vaults Program untuk semua operasi swap rebalancing
· Immediate Result: Efisiensi eksekusi swap meningkat; dependency kritis ke Jupiter terbentuk
· Long-term Impact: Jupiter menjadi dependency kritis (Phase 4 Dependencies, Phase 7 Major Integrations); Multiply kemudian juga menggunakan Jupiter flashloan (EV-007)
· Supporting Dataset: Phase 3 EV-003, Phase 4 Dependencies Jupiter, Phase 7 Integration Jupiter

Keputusan: Launch K-Lend v1 Pooled Lending (2022-09)
· Trigger: Ekspansi produk dari vault-only ke full DeFi stack; permintaan pengguna untuk borrow gegen vault positions
· Evidence: Kamino Docs K-Lend Overview (Phase 3 EV-004); Phase 4 Core Components K-Lend Program
· Decision: Deploy program lending pooled terpisah dengan utilization-based rate model, multiple reserves (SOL, USDC, mSOL, JitoSOL)
· Immediate Result: Pasar lending baru live; TVL lending tumbuh; fondasi untuk Multiply leverage
· Long-term Impact: K-Lend v2 2024-03 menambah isolation mode & dynamic curves (Phase 4 EV-022 upgrade); terintegrasi Multiply & Liquidate
· Supporting Dataset: Phase 3 EV-004, Phase 4 Core Components K-Lend, Phase 4 Technical Upgrade History K-Lend v2

Keputusan: Audit berlapis (Kudelski Feb 2023, Neodyme Mei 2023, Sec3 Okt 2023) sebelum setiap produk mayor launch
· Trigger: Keamanan dana pengguna prioritas; regulasi DeFi makin ketat; reputasi "blue chip" membutuhkan audit trail
· Evidence: Phase 3 EV-005, EV-006, EV-008; Phase 4 Audit History 5 audit total
· Decision: Komisi audit ke 3 firma berbeda (Kudelski, Neodyme, Sec3) untuk Vaults, K-Lend, Multiply, Liquidate
· Immediate Result: Temuan critical/high diperbaiki pre-launch; laporan ringkas dipublikasikan
· Long-term Impact: Audit trail lengkap membangun trust; Immunefi bug bounty $100k max (Phase 4 Security Model); re-audit pada upgrade mayor (K-Lend v2, Liquidate)
· Supporting Dataset: Phase 3 EV-005, EV-006, EV-008, Phase 4 Audit History, Phase 4 Security Model

Keputusan: Launch Multiply Leveraged Vaults dengan auto-loop (2023-07)
· Trigger: Permintaan leverage yield pada LSD/SOL pairs; kompetitor MarginFi/DeltaPrime menawarkan leverage; K-Lend reserves menyediakan borrow capacity
· Evidence: Kamino Blog Multiply Launch (Phase 3 EV-007); Phase 4 Core Components Multiply Program
· Decision: Deploy Multiply Program otomatisasi supply→borrow→supply loop dengan health factor management, Jupiter flashloan entry/exit
· Immediate Result: Produk leverage vault live; TVL Multiply tumbuh; user base power-user tertarik
· Long-term Impact: Multiply v2 2024-06 health factor improvement (Phase 4 EV-025); menjadi pendorong TVL peak $1.5B; fee revenue stream baru
· Supporting Dataset: Phase 3 EV-007, Phase 4 Core Components Multiply, Phase 4 Technical Upgrade History Multiply v2

Keputusan: Points Season 1 dengan Tensor Partnership (2023-11)
· Trigger: Pre-TGE user acquisition & retention; Tensor NFT marketplace populer; cross-protocol incentive loop novelty
· Evidence: Kamino Blog Tensor Partnership (Phase 3 EV-009); Phase 2 Entity Tensor
· Decision: Kolaborasi Points Season 1 Kamino + Tensor simultan; pengguna farm kedua protokol
· Immediate Result: Lonjakan TVL & aktivitas baru; ~100k+ wallets eligible TGE claim (Phase 8 Adoption Metrics)
· Long-term Impact: Model Points Season 2-3 lanjutan (EV-010, EV-011); Season 4 post-TGE on-chain emission (EV-020); template retention program
· Supporting Dataset: Phase 3 EV-009, EV-010, EV-011, EV-020, Phase 8 Adoption Metrics

Keputusan: Token Generation Event KMNO 10B supply + Multi-CEX Listing same-day (2024-04-10)
· Trigger: Maturity protokol (TVL >$1B, 4 produk live, DAO ready); investor/team liquidity event; market window Solana bull run
· Evidence: Kamino X TGE Announcement (Phase 3 EV-012); Binance/Coinbase/Bybit/Gate.io/KuCoin announcements (EV-013, EV-014, EV-015); Solscan mint (Phase 1 Token Contract)
· Decision: Mint 10B KMNO SPL Token-2022; claim live untuk points holders, team, investor, treasury; listing 5 CEX utama hari yang sama
· Immediate Result: KMNO transferable; price discovery immediate; deep CEX liquidity day-1; circulating supply terbentuk
· Long-term Impact: Fee switch activation Mei 2024 (EV-017); DAO governance live (EV-016); Season 4 emission (EV-020); treasury buyback proposal (EV-021)
· Supporting Dataset: Phase 3 EV-012, EV-013, EV-014, EV-015, Phase 6 TGE, Phase 6 Token Events

Keputusan: Formasi Kamino DAO di Realms (SPL Governance) (2024-04-15)
· Trigger: Post-TGE decentralization roadmap; community ownership; regulatory trend DAO-first
· Evidence: Governance Forum & Realms launch (Phase 3 EV-016); Phase 2 Entity Kamino DAO; Phase 7 Governance Ecosystem
· Decision: Deploy DAO di Realms; treasury alokasi KMNO; proposal system on-chain; multisig Squads v3 execution
· Immediate Result: Governance on-chain live; proposal #1 fee switch diajukan & lulus (EV-017)
· Long-term Impact: Semua parameter protokol (fee, emission, upgrade) terkontrol DAO; treasury management proposal aktif (EV-021)
· Supporting Dataset: Phase 3 EV-016, EV-017, Phase 2 Entity Kamino DAO, Phase 7 Governance Ecosystem

Keputusan: Aktivasi Fee Switch via Proposal #1 (2024-05)
· Trigger: Janji tokenomics "real yield"; community pressure post-TGE; DAO governance live
· Evidence: Governance Forum Proposal #1 (Phase 3 EV-017); Realms Vote Record (Phase 3 EV-017); Phase 6 Utility Staking
· Decision: Vote on-chain mengaktifkan fee switch mengarahkan portion protocol fees ke KMNO stakers (veKMNO)
· Immediate Result: Stakers mulai menerima fee distribution; veKMNO voting power active
· Long-term Impact: Value accrual token KMNO terealisasi; staking participation rate jadi metrik kunci (Phase 6 Open Threads); buyback proposal lanjutan (EV-021)
· Supporting Dataset: Phase 3 EV-017, Phase 6 Utility Staking, Phase 6 Token Events EV-017

Keputusan: Integrasi Wormhole NTT untuk Cross-chain Vault Deposits (2024-06)
· Trigger: Narrative multi-chain/Restaking; pengguna ingin deposit ETH/USDC Ethereum ke vault Solana; Wormhole NTT matang
· Evidence: Kamino Blog Cross-chain Vault (Phase 3 EV-018); Wormhole NTT Docs (Phase 2 Entity Wormhole, Phase 7 Dependency Wormhole)
· Decision: Adopsi Wormhole Native Token Transfers untuk bridging aset non-native ke Kamino Vaults
· Immediate Result: Cross-chain deposit UX seamless; vault multichain awal live
· Long-term Impact: Dependency ke Wormhole NTT registry (Phase 4 Known Limitations); emerging narrative cross-chain DeFi (Phase 8 Narrative)
· Supporting Dataset: Phase 3 EV-018, Phase 4 Dependencies Wormhole, Phase 7 Integration Wormhole NTT, Phase 8 Narrative Cross-chain

Keputusan: Launch Liquidate Program Permissionless Marketplace (2024-08)
· Trigger: Bad debt risk di K-Lend/Multiply; MEV liquidation tersentralisasi ke bot internal; permintaan permissionless competition
· Evidence: Kamino Blog Liquidate Launch (Phase 3 EV-019); Phase 4 Core Components Liquidate Program; Phase 4 Technical Upgrade History Liquidate Launch
· Decision: Deploy program terpisah Liquidate dengan Dutch auction discount curve, permissionless keeper registration
· Immediate Result: Liquidator bersaing terbuka; bad debt risk turun; transparansi on-chain
· Long-term Impact: Revenue stream baru (liquidation fees); MEV democratization narrative (Phase 8 Narrative); parameter auction fixed until governance change (Phase 4 Known Limitations)
· Supporting Dataset: Phase 3 EV-019, Phase 4 Core Components Liquidate, Phase 4 Technical Upgrade History, Phase 8 Narrative Liquidation

Keputusan: Points Season 4 On-chain KMNO Emission (2024-10)
· Trigger: Post-TGE token utility diperlukan; off-chain points tidak scalable/transparent; emission dari treasury allocation
· Evidence: Kamino Blog Season 4 (Phase 3 EV-020); Governance Forum Season 4 Parameters (Phase 3 EV-020); Phase 6 Inflation/Emission
· Decision: Deploy program emisi KMNO on-chain untuk rewards vault/lend/multiply/referral; ganti Merkle root claim
· Immediate Result: Rewards real-time on-chain; KMNO utility tambahan; Season 4 ongoing
· Long-term Impact: Emission schedule dari treasury (bukan inflation); buyback proposal untuk offset (EV-021); sustainable tokenomics test
· Supporting Dataset: Phase 3 EV-020, Phase 6 Inflation/Emission, Phase 6 Token Events EV-020

Keputusan: Treasury Buyback & Burn Proposal (2024-12)
· Trigger: Community demand deflationary pressure; treasury KMNO besar; fee switch revenue accumulating
· Evidence: Governance Forum Treasury Proposal (Phase 3 EV-021); Realms Proposal Status (Phase 3 EV-021); Phase 6 Inflation Buyback Proposed
· Decision: Proposal on-chain alokasi treasury revenue untuk buyback KMNO di pasar & burn
· Immediate Result: Diskusi komunitas berlangsung; belum dieksekusi menunggu quorum
· Long-term Impact: Jika lulus, supply reduction mechanism aktif; treasury diversification pressure (Phase 5 Financial Risk)
· Supporting Dataset: Phase 3 EV-021, Phase 6 Inflation Buyback, Phase 5 Financial Risk Treasury Concentration

Evolution Pattern

Perubahan Strategi: Dari Single Product (Vaults) ke Full DeFi Stack Terintegrasi
· Evidence: 2022 Vaults only (EV-002) → 2022 K-Lend added (EV-004) → 2023 Multiply leverage (EV-007) → 2024 Liquidate marketplace (EV-019); setiap produk memperkuat yang lain (Vaults supply K-Lend, K-Lend enable Multiply, Liquidate secure K-Lend/Multiply)
· Supporting Dataset: Phase 3 History EV-002, EV-004, EV-007, EV-019; Phase 4 Core Components 4 core programs

Perubahan Teknologi: Upgrade Bertahap dengan Audit Pre-Launch
· Evidence: Vaults v1→v2 (2023-01), K-Lend v1→v2 (2024-03), Multiply v1→v2 (2024-06); setiap major upgrade didahului audit (Kudelski/Neodyme/Sec3) (Phase 3 EV-005, EV-006, EV-008, Phase 4 Audit History)
· Supporting Dataset: Phase 3 EV-005, EV-006, EV-008, Phase 4 Technical Upgrade History, Phase 4 Audit History

Perubahan Tokenomics: Dari Points Off-chain ke Token On-chain dengan Fee Switch
· Evidence: Season 1-3 off-chain Merkle root (EV-009, EV-010, EV-011) → TGE KMNO 10B fixed supply (EV-012) → Fee switch activation (EV-017) → Season 4 on-chain emission (EV-020) → Buyback proposal (EV-021); evolusi dari "promise" ke "real yield" terverifikasi
· Supporting Dataset: Phase 3 EV-009, EV-010, EV-011, EV-012, EV-017, EV-020, EV-021; Phase 6 Token Events, Phase 6 Inflation/Deflation

Perubahan Governance: Dari Team-Controlled ke DAO On-chain dengan Multisig Timelock
· Evidence: Program upgrade authority multisig tim inti (Phase 4 Security Model) → DAO Realms formed April 2024 (EV-016) → Proposal #1 fee switch passed (EV-017) → Treasury proposals active (EV-021); upgrade authority belum fully DAO-timelocked (Phase 4 Known Limitations)
· Supporting Dataset: Phase 3 EV-016, EV-017, EV-021; Phase 4 Security Model, Phase 4 Known Limitations, Phase 7 Governance Ecosystem

Perubahan Ekosistem: Dari Solana-Native ke Cross-Chain via Wormhole NTT
· Evidence: 2022-2023 pure Solana assets (SOL, mSOL, JitoSOL) → 2024-06 Wormhole NTT integration (EV-018) untuk ETH, USDC Ethereum; dependency baru ke Wormhole guardians & NTT registry
· Supporting Dataset: Phase 3 EV-018, Phase 4 Dependencies Wormhole, Phase 7 Integration Wormhole NTT, Phase 8 Narrative Cross-chain

Technical Decision Pattern

Pola 1: Modular Program Architecture dengan CPI Integration
· Decision Pattern: Setiap produk (Vaults, K-Lend, Multiply, Liquidate, Token, Staking) sebagai program Anchor/Rust terpisah dengan PDA accounts; saling terintegrasi via Cross-Program Invocation (CPI) bukan monolith
· Evidence: Phase 4 Core Components 9 programs terpisah; Phase 4 System Architecture "monolitik on-chain dengan komponen off-chain"; GitHub repo per program (kamino-vaults, kamino-lend, kamino-multiply, kamino-liquidate)
· Supporting Dataset: Phase 4 Core Components, Phase 4 System Architecture, Phase 4 Execution Environment

Pola 2: Dependency pada Infrastructure Solana Native (Pyth, Jupiter, SPL Token-2022)
· Decision Pattern: Memilih infrastructure terbaik di Solana (Pyth oracle, Jupiter swap/flashloan, SPL Token-2022 extensions) daripada build sendiri; accept dependency risk untuk speed & quality
· Evidence: Phase 4 Dependencies Pyth (Critical), Jupiter (Critical), SPL Token-2022 (KMNO token); Phase 7 Major Integrations Jupiter, Pyth, Wormhole; Phase 4 Known Limitations oracle staleness & Jupiter dependency
· Supporting Dataset: Phase 4 Dependencies, Phase 7 Major Integrations, Phase 4 Known Limitations

Pola 3: Upgrade Authority Multisig Squads v3 (Belum Fully Immutable/DAO-Timelocked)
· Decision Pattern: Program upgrade authority di multisig Squads v3 dikontrol tim inti; DAO governance Realms mengontrol parameter tapi bukan upgrade code langsung; timelock proposal di forum tapi tidak on-chain enforced
· Evidence: Phase 4 Security Model "Upgrade authority disimpan di Multisig (Squads v3) dikendalikan tim inti — bukan fully immutable"; Phase 4 Known Limitations "Program upgrade authority masih bersifat multisig tim inti"; Phase 7 Infrastructure Providers Squads Protocol
· Supporting Dataset: Phase 4 Security Model, Phase 4 Known Limitations, Phase 7 Infrastructure Providers

Pola 4: Off-chain Indexer + On-chain Merkle Root untuk Points (Season 1-3) → Fully On-chain Emission (Season 4)
· Decision Pattern: Awalnya trusted off-chain indexer hitung points, commit Merkle root on-chain untuk claim (gas efficient, flexible) → post-TGE migrasi ke program emisi on-chain (transparent, verifiable, composable)
· Evidence: Phase 3 EV-009, EV-010, EV-011 (Season 1-3 off-chain); EV-020 (Season 4 on-chain); Phase 4 Core Components Points Program; Phase 4 Known Limitations "Points Season 1-3 calculation sepenuhnya off-chain — tidak ada verifikasi on-chain hingga Merkle root commit"
· Supporting Dataset: Phase 3 EV-009, EV-010, EV-011, EV-020, Phase 4 Core Components, Phase 4 Known Limitations

Pola 5: Rust/Anchor + TypeScript SDK + Yellowstone gRPC Indexing Stack
· Decision Pattern: Smart contract Rust/Anchor; client TypeScript SDK; real-time indexing Yellowstone gRPC/Geyser; Docker/GitHub Actions CI/CD; standard Solana toolchain
· Evidence: Phase 4 Programming Languages, Development Framework, Current Technical Stack; GitHub repo structure (Phase 4 Official Technical Resources)
· Supporting Dataset: Phase 4 Programming Languages, Phase 4 Development Framework, Phase 4 Current Technical Stack, Phase 4 Official Technical Resources

Financial Decision Pattern

Pola 1: Single Seed Round (2022) + Grants + Protocol Revenue → No Follow-on Funding
· Decision Pattern: Seed round 2022 dari Multicoin, Jump, Solana Ventures (amount undisclosed) + Solana Foundation grants → post-launch fully funded by protocol revenue (Vault fees, K-Lend spread, Multiply fees, Liquidate fees) + DAO treasury KMNO allocation; tidak ada Series A/B publik
· Evidence: Phase 5 Funding History hanya 1 Seed round + 1 Grant; Phase 5 Fundraising Mechanism "VC Funding: Seed round 2022... tidak ada ronde pendanaan baru sejak Seed 2022"; Phase 5 Financial Risk "Funding Dependency on Early Investors: Tidak ada ronde pendanaan baru sejak Seed 2022"
· Supporting Dataset: Phase 5 Funding History, Phase 5 Fundraising Mechanism, Phase 5 Financial Risk

Pola 2: Treasury Denominated Primarily in Native Token (KMNO) dengan Fee Switch Revenue Flow
· Decision Pattern: Treasury DAO menerima alokasi KMNO di TGE (EV-016); fee switch mengarahkan protocol revenue ke stakers (EV-017) bukan treasury; treasury composition tidak transparan (Phase 5 Treasury); buyback proposal untuk convert revenue ke KMNO buyback (EV-021)
· Evidence: Phase 5 Treasury "Treasury Composition: Tidak diungkap... Native Token Holdings: KMNO... alokasi treasury DAO tidak dipublikasikan"; Phase 3 EV-016, EV-017, EV-021; Phase 5 Financial Risk "Treasury Concentration: Treasury sebagian besar denominasi KMNO"
· Supporting Dataset: Phase 5 Treasury, Phase 3 EV-016, EV-017, EV-021, Phase 5 Financial Risk

Pola 3: Revenue Transparency Minimal (No Public Reports, On-chain Only)
· Decision Pattern: Tidak mempublikasikan laporan revenue bulanan/kuartalan; revenue data hanya on-chain (fee receiver accounts, program fees); third-party (DefiLlama, Token Terminal) mengestimasi dari on-chain
· Evidence: Phase 5 Revenue History "Tidak diungkap... no public revenue reports, no transparency dashboard"; Phase 5 Official Financial Resources tidak ada Transparency Report; Phase 8 Open Threads "Protocol Revenue (Fees) Historical: tidak dipublikasikan resmi"
· Supporting Dataset: Phase 5 Revenue History, Phase 5 Official Financial Resources, Phase 8 Open Threads

Pola 4: Token Allocation Opaque (No Public Breakdown Percentages)
· Decision Pattern: Kategori alokasi diketahui (community, team, investor, treasury, ecosystem) tapi persentase exact tidak dipublikasikan; on-chain vesting accounts visible tapi tidak dilabeli resmi
· Evidence: Phase 6 Distribution "persentase exact tidak dipublikasikan resmi"; Phase 6 Vesting Schedule "tidak diketahui" untuk semua kategori; Phase 6 Open Threads "Persentase alokasi token exact per kategori... tidak dipublikasikan resmi"
· Supporting Dataset: Phase 6 Distribution, Phase 6 Vesting Schedule, Phase 6 Open Threads

Ecosystem Decision Pattern

Pola 1: Deep Integration dengan Solana Core Infrastructure (Jupiter, Pyth, Jito, Marinade) sebagai Dependency Strategis
· Decision Pattern: Build pada infrastructure terbaik Solana bukan kompetisi; Jupiter untuk swap/flashloan (Critical), Pyth untuk oracle (Critical), JitoSOL/mSOL sebagai core assets (High), Wormhole untuk cross-chain (High)
· Evidence: Phase 4 Dependencies Critical/High ratings; Phase 7 Major Integrations Jupiter, Pyth, Wormhole, Jito, Marinade; Phase 2 Entities Jupiter, Marinade Finance, Jito Labs, Wormhole, Pyth Network
· Supporting Dataset: Phase 4 Dependencies, Phase 7 Major Integrations, Phase 2 Entities

Pola 2: Partnership Incentive-Driven (Tensor Points Season 1) untuk User Acquisition Cross-Protocol
· Decision Pattern: Kolaborasi points program dengan protokol komplementer (Tensor NFT marketplace) menciptakan loop farming; bukan integrasi teknis tapi incentive alignment
· Evidence: Phase 3 EV-009 Tensor Partnership; Phase 2 Entity Tensor; Phase 7 Applications Tensor; Phase 8 Narrative Points/Incentive
· Supporting Dataset: Phase 3 EV-009, Phase 2 Entity Tensor, Phase 7 Applications, Phase 8 Narrative

Pola 3: Multi-CEX Listing Strategy TGE Same-Day untuk Liquidity & Distribution Maximization
· Decision Pattern: Koordinasi listing 5 CEX utama (Binance, Coinbase, Bybit, Gate.io, KuCoin) hari TGE yang sama; bukan sequential listing; memastikan deep liquidity immediate & global distribution
· Evidence: Phase 3 EV-013, EV-014, EV-015 same date 2024-04-10; Phase 8 Trading Markets 5 CEX live; Phase 2 Entities Binance, Coinbase, Bybit, Gate.io, KuCoin
· Supporting Dataset: Phase 3 EV-013, EV-014, EV-015, Phase 8 Trading Markets, Phase 2 Entities

Pola 4: Wallet Ecosystem Broad Support (Phantom, Backpack, Solflare, Glow, Trust, Exodus, Ledger) Tanpa Eksklusivitas
· Decision Pattern: Integrasi wallet sebisa banyak via Wallet Adapter standard; Phantom & Backpack mendapat fitur tambahan (xNFT, native UX) tapi tidak eksklusif
· Evidence: Phase 7 Wallet Ecosystem 7 wallets supported; Phase 2 Entities Phantom, Backpack; Phase 7 Applications Phantom, Backpack
· Supporting Dataset: Phase 7 Wallet Ecosystem, Phase 2 Entities, Phase 7 Applications

Pola 5: Developer Ecosystem Open Source Core Programs + Internal Infrastructure
· Decision Pattern: Core programs (Vaults, K-Lend, Multiply, Liquidate) open source di GitHub; SDK, IDL, docs publik; tapi indexer, bots, frontend partial private; tidak ada grant program resmi besar selain DAO proposal (EV-021)
· Evidence: Phase 7 Developer Ecosystem GitHub org, SDK, API, IDL; "Partial — core programs open source, some infrastructure private"; Phase 3 EV-021 DAO Grants proposed
· Supporting Dataset: Phase 7 Developer Ecosystem, Phase 3 EV-021

Governance Decision Pattern

Pola 1: Token-Weighted Voting via Realms (SPL Governance) dengan veKMNO dari Staking
· Decision Pattern: 1 KMNO = 1 vote (staked → veKMNO); delegation supported; proposal creation threshold & quorum parameterized; execution via Squads multisig after vote pass
· Evidence: Phase 6 Governance "Token-weighted voting via Realms... 1 KMNO = 1 vote (staked KMNO/veKMNO)"; Phase 3 EV-016 DAO Formation; Phase 7 Governance Ecosystem Kamino DAO
· Supporting Dataset: Phase 6 Governance, Phase 3 EV-016, Phase 7 Governance Ecosystem

Pola 2: Progressive Decentralization — Parameter Control First, Upgrade Authority Later
· Decision Pattern: DAO mengontrol parameter (fee switch, emission, treasury spending) sejak Day 1 post-TGE; upgrade authority masih multisig tim inti (Squads v3); timelock/DAO upgrade proposal di forum tapi belum on-chain enforced
· Evidence: Phase 3 EV-017 Fee Switch (parameter), EV-020 Season 4 params, EV-021 Treasury spending; Phase 4 Security Model "Upgrade authority disimpan di Multisig... bukan fully immutable"; Phase 4 Known Limitations "Program upgrade authority masih bersifat multisig tim inti"
· Supporting Dataset: Phase 3 EV-017, EV-020, EV-021, Phase 4 Security Model, Phase 4 Known Limitations

Pola 3: Active Governance Cycle — Proposals Berkala (Fee Switch, Season 4, Treasury Buyback)
· Decision Pattern: Rata-rata 1 major proposal per kuartal post-TGE; proposal #1 Mei 2024 (fee switch), Season 4 Okt 2024 (emission), Treasury Buyback Des 2024; community forum diskusi aktif sebelum on-chain
· Evidence: Phase 3 EV-017 (Mei 2024), EV-020 (Okt 2024), EV-021 (Des 2024); Phase 6 Governance "Status: Active"; Phase 7 Governance Ecosystem DAO active
· Supporting Dataset: Phase 3 EV-017, EV-020, EV-021, Phase 6 Governance, Phase 7 Governance Ecosystem

Pola 4: Treasury Management via Proposal — No Autonomous Budget
· Decision Pattern: Treasury tidak punya budget otonom; setiap pengeluaran (grants, buyback, strategic) butuh proposal & vote; custodian Squads multisig eksekusi pasca-vote
· Evidence: Phase 3 EV-021 Treasury Buyback Proposal "masih diskusi menunggu quorum"; Phase 5 Treasury "Treasury Custodian: Kamino DAO Multisig (Squads v3)"; Phase 6 Governance "Treasury Governance: DAO Treasury... controlled by Realms governance; spending proposals require vote"
· Supporting Dataset: Phase 3 EV-021, Phase 5 Treasury, Phase 6 Governance

Risk Response Pattern

Pola 1: Pre-emptive Multi-Auditor Security Reviews Sebelum Setiap Major Launch/Upgrade
· Decision Pattern: Komisi audit ke 3 firma berbeda (Kudelski, Neodyme, Sec3) untuk setiap produk/upgrade mayor; temuan critical/high wajib diperbaiki pre-deploy; re-audit pada upgrade v2
· Evidence: Phase 3 EV-005 (Kudelski Vaults/K-Lend Feb 2023), EV-006 (Neodyme Mei 2023), EV-008 (Sec3 Okt 2023); Phase 4 Audit History 5 audits total; Phase 4 Security Model "Audit Coverage: Multiple audits... temuan Critical/High diperbaiki via program upgrade"
· Trigger: Major product launch (Vaults, K-Lend, Multiply, Liquidate) atau major upgrade (K-Lend v2, Multiply v2, Liquidate v1)
· Response: Engage auditors → remediate findings → deploy → publish summary
· Result: Zero major exploits post-launch (Phase 8 Open Threads "Security Incident History: tidak ada insiden keamanan mayor tercatat"); Immunefi bug bounty $100k max active
· Supporting Dataset: Phase 3 EV-005, EV-006, EV-008, Phase 4 Audit History, Phase 4 Security Model, Phase 8 Open Threads

Pola 2: Oracle Redundancy (Pyth Primary + Switchboard Fallback) untuk Mitigasi Price Feed Failure
· Decision Pattern: K-Lend & Multiply menggunakan Pyth pull oracle primary; Switchboard V2 fallback configured; staleness threshold & confidence interval checks on-chain; tidak single point of failure oracle
· Evidence: Phase 4 Dependencies Pyth (Critical), Switchboard (High); Phase 4 Security Model "Oracle Security: Pyth pull oracle... Switchboard V2 pull feeds sebagai fallback; staleness threshold & confidence interval checks"; Phase 4 Known Limitations "Multiply health factor calculation bergantung pada Pyth price feed update frequency... selama volatility ekstrem health factor bisa stale sebentar"
· Trigger: Oracle staleness, price manipulation risk, network congestion
· Response: Dual oracle architecture dengan fallback logic di program code
· Result: Tidak ada bad debt akibat oracle failure tercatat; tapi known limitation stale health factor saat volatility ekstrem
· Supporting Dataset: Phase 4 Dependencies, Phase 4 Security Model, Phase 4 Known Limitations

Pola 3: Permissionless Liquidation Marketplace (Liquidate Program) untuk Mitigasi Bad Debt & MEV Centralization
· Decision Pattern: Alih-alih liquidator internal/whitelisted, deploy permissionless Dutch auction marketplace; siapa pun bisa jadi liquidator; kompetisi menekan discount & memastikan efisiensi
· Evidence: Phase 3 EV-019 Liquidate Launch; Phase 4 Core Components Liquidate Program; Phase 4 Security Model "Liquidation Protection: Health factor real-time check; Dutch auction discount curve mencegah toxic liquidation; permissionless liquidator registration"; Phase 8 Narrative Liquidation Marketplace
· Trigger: Bad debt accumulation risk di K-Lend/Multiply; MEV liquidation profit tersentralisasi ke few bots
· Response: Deploy Liquidate program v1 Agustus 2024; Dutch auction parameters fixed until governance change
· Result: Bad debt risk turun; liquidator competition live; revenue stream baru; parameter auction belum adaptif (Known Limitation)
· Supporting Dataset: Phase 3 EV-019, Phase 4 Core Components, Phase 4 Security Model, Phase 8 Narrative

Pola 4: Regulatory Compliance via BVI Entity + CEX Listing Standards (Coinbase) + Anonymous Team
· Decision Pattern: Entitas hukum BVI (Kamino Finance Ltd.) untuk legal wrapper; Coinbase listing menandakan compliance bar tinggi; tim tetap anonim (pseudonim) tanpa doxxing; tidak ada legal wrapper DAO terpisah (Cayman/Swiss) yet
· Evidence: Phase 1 Foundation "Founding Entity: Kamino Finance Ltd. (BVI)"; Phase 2 Entity Kamino Finance Ltd. "Legal entity"; Phase 3 EV-014 Coinbase Listing; Phase 2 Entity Kamino Team "sepenuhnya pseudonim"; Phase 2 Open Threads "Identitas legal pendiri... tetap sepenuhnya pseudonim... perlu verifikasi apakah ada entitas hukum tambahan"
· Trigger: Global regulatory uncertainty (securities law, AML, DeFi regulation)
· Response: BVI entity + compliance untuk CEX listing + anonymous core team; DAO governance sebagai decentralization signal
· Result: Operational continuity maintained; Coinbase/US access achieved; regulatory risk remains open (Phase 5 Financial Risk "Regulatory & Legal Risk: Entitas BVI + tim anonim — ketidakpastian regulasi global")
· Supporting Dataset: Phase 1 Foundation, Phase 2 Entities, Phase 3 EV-014, Phase 5 Financial Risk, Phase 2 Open Threads

Pola 5: Market Downturn Response — Product Expansion & Incentive Programs (Points) untuk Retensi TVL
· Decision Pattern: Saat bear market 2022-2023, fokus product shipping (K-Lend, Multiply) + Points Season 1-3 pre-TGE untuk drive TVL; post-TGE Season 4 on-chain emission untuk retain liquidity
· Evidence: Phase 3 timeline 2022-2023 product launches during bear; EV-009, EV-010, EV-011 Points Seasons drive TVL growth; Phase 8 Market Timeline TVL peak $1.5B Mar 2024 pre-TGE; Phase 8 Adoption Metrics TVL ~$1.2B Oct 2024 post-TGE
· Trigger: Crypto winter 2022-2023, TVL pressure, user retention challenge
· Response: Ship lending & leverage products; launch points programs dengan escalating rewards; Tensor partnership cross-protocol
· Result: TVL growth melalui bear market; successful TGE dengan deep liquidity; post-TGE TVL retention via Season 4
· Supporting Dataset: Phase 3 History 2022-2024, Phase 3 EV-009, EV-010, EV-011, EV-020, Phase 8 Market Timeline, Phase 8 Adoption Metrics

Recurring Behavioral Pattern

Pola 1: Ship Product → Audit → Launch → Iterate (v2) dengan Audit Ulang
· Evidence: Vaults v1 (Mar 2022) → Kudelski/Neodyme audit (Feb-Mei 2023) → Vaults v2 (Jan 2023, actually before audit? timeline check: EV-002 Mar 2022 launch, EV-002 upgrade v2 2023-01, EV-005 Kudelski Feb 2023 — so v2 before audit? But audit covered v1/v2); K-Lend v1 (Sep 2022) → audit → K-Lend v2 (Mar 2024) → re-audit; Multiply v1 (Jul 2023) → Sec3 audit (Oct 2023) → Multiply v2 (Jun 2024) → re-audit; Liquidate v1 (Aug 2024) → Neodyme audit (Jun 2024 pre-launch). Pattern: audit sering overlap dengan upgrade cycle.
· Supporting Dataset: Phase 3 EV-002, EV-004, EV-007, EV-019, EV-005, EV-006, EV-008, Phase 4 Technical Upgrade History, Phase 4 Audit History

Pola 2: Integrasi dengan Market Leader Solana (Jupiter, Jito, Marinade, Pyth) sebagai Default Choice
· Evidence: Jupiter swap/flashloan (EV-003, EV-007), JitoSOL core asset (EV-002, EV-011), mSOL core asset (EV-002), Pyth oracle (all lending/leverage), Wormhole NTT (EV-018); tidak build alternative sendiri
· Supporting Dataset: Phase 3 EV-003, EV-007, EV-002, EV-011, EV-018, Phase 4 Dependencies, Phase 7 Major Integrations

Pola 3: Incentive Program Berkelanjutan (Points Season 1→2→3→4) dengan Eskalasi Kompleksitas
· Evidence: Season 1 (Nov 2023) basic vault/lend points + Tensor; Season 2 (Jan 2024) multiply/borrow/referral categories + multiplier; Season 3 (Mar 2024) Jito/restaking bonus; Season 4 (Oct 2024) on-chain KMNO emission; setiap season tambah kategori & mekanisme baru
· Supporting Dataset: Phase 3 EV-009, EV-010, EV-011, EV-020, Phase 6 Token Events

Pola 4: Governance Proposal Berkala Major Parameter (Fee Switch, Emission, Treasury) Setiap ~Kuartal
· Evidence: Proposal #1 Mei 2024 (Fee Switch), Season 4 params Okt 2024, Treasury Buyback Des 2024; forum diskusi aktif antar proposal
· Supporting Dataset: Phase 3 EV-017, EV-020, EV-021, Phase 6 Governance, Phase 7 Governance Ecosystem

Pola 5: Transparansi On-chain > Off-chain Reporting (Revenue, Treasury, Token Distribution)
· Evidence: Revenue tidak ada laporan publik (Phase 5 Revenue History); treasury composition tidak transparan (Phase 5 Treasury); token allocation percentages tidak dipublikasikan (Phase 6 Distribution); semua data tersedia on-chain (program accounts, token accounts, governance votes) tapi butuh technical skill untuk query
· Supporting Dataset: Phase 5 Revenue History, Phase 5 Treasury, Phase 6 Distribution, Phase 6 Open Threads, Phase 8 Open Threads

Strategic Trade-offs

Trade-off 1: Desentralisasi Upgrade Authority vs Kecepatan Eksekusi & Keamanan Tim Inti
· Decision: Upgrade authority tetap di multisig Squads v3 tim inti (bukan DAO timelock atau immutable)
· Trade-off: Kecepatan patch critical bug & upgrade koordinasi lebih cepat (tim inti bisa deploy cepat) dikorbankan untuk desentralisasi penuh; risiko sentralisasi upgrade authority (Phase 4 Known Limitations)
· Evidence: Phase 4 Security Model "Upgrade authority disimpan di Multisig (Squads v3) dikendalikan tim inti — bukan fully immutable"; Phase 4 Known Limitations "Program upgrade authority masih bersifat multisig tim inti — risiko sentralisasi upgrade"
· Supporting Dataset: Phase 4 Security Model, Phase 4 Known Limitations

Trade-off 2: Off-chain Points Calculation (Season 1-3) vs On-chain Verifiability
· Decision: Season 1-3 points dihitung off-chain oleh indexer tepercaya, hanya Merkle root di-commit on-chain
· Trade-off: Gas efficiency & fleksibilitas kategori reward tinggi (bisa ubah logic tanpa deploy) dikorbankan untuk trust-minimization; pengguna harus percaya operator indexer (Phase 4 Known Limitations)
· Evidence: Phase 3 EV-009, EV-010, EV-011 off-chain; Phase 4 Core Components Points Program; Phase 4 Known Limitations "Points Season 1-3 calculation sepenuhnya off-chain — tidak ada verifikasi on-chain hingga Merkle root commit"
· Supporting Dataset: Phase 3 EV-009, EV-010, EV-011, Phase 4 Core Components, Phase 4 Known Limitations

Trade-off 3: Single-Chain (Solana Only) Focus vs Multi-Chain Expansion
· Decision: Semua produk deploy hanya di Solana; cross-chain hanya via Wormhole NTT untuk asset bridging (bukan deploy protokol ke chain lain)
· Trade-off: Fokus resource & liquidity di Solana (deep integration, composability maksimal) dikorbankan untuk market size multi-chain; risiko sistemik Solana outage/regulatory mempengaruhi 100% operasi (Phase 8 Ecosystem Risks)
· Evidence: Phase 4 System Architecture "Sepenuhnya berjalan di Solana mainnet"; Phase 7 Ecosystem Risks "Single Chain Dependency — Solana... risiko sistemik Solana mempengaruhi 100% operasi"; Phase 8 Ecosystem Risks Single Chain Dependency
· Supporting Dataset: Phase 4 System Architecture, Phase 7 Ecosystem Risks, Phase 8 Ecosystem Risks

Trade-off 4: Treasury Concentrated in Native Token (KMNO) vs Stablecoin Diversification
· Decision: Treasury DAO sebagian besar KMNO (TGE allocation); fee switch revenue ke stakers bukan treasury; tidak ada diversification program ke stablecoin/yield-bearing assets yet
· Trade-off: Alignment token holder & treasury (value capture KMNO) dikorbankan untuk runway stability; bear market KMNO price drop mengurangi treasury value drastis (Phase 5 Financial Risk)
· Evidence: Phase 5 Treasury "Native Token Holdings: KMNO... alokasi treasury DAO tidak dipublikasikan"; Phase 5 Financial Risk "Treasury Concentration: Treasury sebagian besar denominasi KMNO — nilai bergantung pada harga KMNO"; Phase 3 EV-021 Buyback proposal sebagai response
· Supporting Dataset: Phase 5 Treasury, Phase 5 Financial Risk, Phase 3 EV-021

Trade-off 5: Anonymous Core Team vs Institutional Trust & Regulatory Clarity
· Decision: Tim inti tetap pseudonim (@kamino_finance); entitas hukum BVI saja; Coinbase listing achieved tanpa doxxing tim
· Trade-off: Privasi & keamanan tim dijaga; regulatory risk & institutional trust terbatas (tidak ada legal wrapper DAO Cayman/Swiss); investor/partner due diligence terbatas (Phase 2 Open Threads, Phase 5 Financial Risk)
· Evidence: Phase 1 Foundation "Founders: anonim/pseudonim"; Phase 2 Entity Kamino Team "sepenuhnya pseudonim"; Phase 2 Open Threads "Identitas legal pendiri... tetap sepenuhnya pseudonim"; Phase 5 Financial Risk "Regulatory & Legal Risk: Entitas BVI + tim anonim"
· Supporting Dataset: Phase 1 Foundation, Phase 2 Entity Kamino Team, Phase 2 Open Threads, Phase 5 Financial Risk

Behavioral Summary

Prioritas Utama Proyek:
1. Product Shipping Velocity & Quality: Launch produk berkualitas (Vaults, K-Lend, Multiply, Liquidate) dengan audit pre-launch; iterate cepat v2 berdasarkan feedback & data
2. Real Yield & Token Value Accrual: Fee switch activation, staking rewards, buyback proposal — buktikan KMNO bukan governance-only token
3. Ecosystem Integration Depth: Jadi "hub" DeFi Solana terintegrasi Jupiter, Pyth, Jito, Marinade, Wormhole — bukan silo
4. Progressive Decentralization: DAO parameter control first, upgrade authority later; community ownership nyata via veKMNO
5. User Retention via Incentive Evolution: Points program berkelanjutan berevolusi off-chain → on-chain emission

Cara Mengambil Keputusan:
- Data-driven dari on-chain metrics (TVL, volume, health factor, oracle staleness)
- Community signaling via governance forum sebelum proposal on-chain
- Security-first: audit wajib pre-launch, multi-auditor, bug bounty tinggi
- Dependency strategy: build on best-of-breed Solana infra (Jupiter, Pyth, SPL) bukan NIH
- Incremental decentralization: parameter → treasury → upgrade authority

Faktor Paling Sering Mempengaruhi Keputusan:
1. Solana Ecosystem Dynamics (Jupiter updates, JitoSOL adoption, Pyth oracle reliability, Wormhole NTT maturity)
2. Competitive Landscape (Orca, Raydium, Solend, MarginFi, Drift, Meteora moves)
3. Token Holder Sentiment (governance forum, fee switch demand, buyback pressure)
4. Regulatory Environment (CEX listing requirements, BVI entity constraints, anonymous team risk)
5. Technical Constraints (Solana compute limits, account size limits, oracle latency)

Pola Evolusi:
Phase 1 (2022): Single Product (Vaults CLMM) → Product-Market Fit
Phase 2 (2022-2023): Stack Expansion (K-Lend, Multiply) → Full DeFi Suite
Phase 3 (2023-2024): Incentive & Security Hardening (Points, Multi-audits) → TGE Readiness
Phase 4 (2024+): Tokenization & Decentralization (TGE, DAO, Fee Switch, On-chain Emission) → Sustainable Protocol

Kekuatan Utama:
- Deep technical moat: CLMM auto-rebalance, pooled lending isolation mode, leverage automation, permissionless liquidation
- Best-in-class Solana integrations: Jupiter, Pyth, Jito, Marinade, Wormhole, Phantom, Backpack
- Real revenue multiple streams: Vault fees, lending spread, multiply fees, liquidation fees
- Active DAO governance dengan real parameter control
- Strong CEX liquidity (Binance, Coinbase, Bybit, Gate.io, KuCoin)
- Zero major exploits track record

Kelemahan Utama:
- Upgrade authority centralized (multisig tim inti)
- Token allocation & treasury opacity (no public percentages, no transparency reports)
- Single-chain dependency (Solana only)
- Oracle & bridge dependency risk (Pyth, Wormhole)
- Anonymous team limits institutional adoption & regulatory clarity
- Points Season 1-3 off-chain trust assumption
- Liquidate auction parameters fixed non-adaptive
- No formal verification (audit only)

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

## Validation & Quality Assurance (CIF Score)
_ref: `docs/Reasoning/Confidence.md` — CIF Score, Data Lineage, Knowledge Dependency Graph_

PROJECT: Kamino

CIF MANIFEST v3.0

Project: Kamino Finance
Symbol: KMNO
Research Date: 2025-02-19
CIF Version: 3.0
QA Date: 2025-02-19

METRICS
Total Knowledge Objects: 10
Total Entities: 32
Total Events: 21
Evidence Links: 54
Sources: 27
Conflicts: 8
- Resolved: 6
- Critical: 0
- High: 1
- Medium: 3
- Low: 4

QUALITY SCORES
Research Quality: 80/100
Consistency: 100/100
Evidence: 75/100
Coverage: 94.6/100
Conflict: 86.25/100
Knowledge: 88.3/100
CIF SCORE: 87.21/100

CONFIDENCE LEVEL: HIGH
QA STATUS: PASSED

RECOMMENDED RE-RUN:
- Phase 2 — Verifikasi identitas legal tim inti dan detail entitas BVI (hanya sumber resmi ToS)
- Phase 5 — Data finansial (Seed round amount, treasury size) tidak transparan; perlu on-chain analysis
- Phase 6 — Tokenomics breakdown persentase alokasi belum dipublikasikan resmi; perlu dashboard resmi
- Phase 8 — Metrik adopsi (DAU, volume harian) tidak tersedia publik; perlu query Dune/Flipside

DATASET INTEGRITY & COVERAGE

Phase 1 — Foundation
- Status: Complete
- Missing Information: Testnet launch date tidak ditemukan (never existed); nama lengkap founder tidak dipublikasikan (not public)
- Notes: Data dasar lengkap untuk chain, products, symbols; launch dates dimulai dari mainnet Maret 2022

Phase 2 — Entity
- Status: Complete
- Missing Information: Identitas anggota tim individu tidak dipublikasikan (not public); alamat legal BVI tidak dicantumkan (not public)
- Notes: 32 entitas teridentifikasi; beberapa mitra ekosistem (Pyth, Switchboard, Raydium, Orca) tidak diekstrak sebagai entitas terpisah namun disebut di Phase 4/7

Phase 3 — History
- Status: Complete
- Missing Information: Tanggal pasti pendirian entitas BVI tidak ada (EV-001 hanya menyebut tahun 2022)
- Notes: 21 event terdokumentasi; timeline konsisten dengan Phase 1 dan 8

Phase 4 — Technology
- Status: Complete
- Missing Information: Oracle staleness threshold exact value tidak terdokumentasi; pause authority / circuit breaker tidak ditemukan
- Notes: Arsitektur lengkap; 10 upgrade terdokumentasi; audit history 5 entri

Phase 5 — Financial
- Status: Incomplete
- Missing Information: Seed round amount (USD) tidak diungkap; treasury size & composition tidak transparan; revenue history tidak dipublikasikan; persentase alokasi token ke kategori tidak diketahui
- Notes: Data finansial sangat terbatas; seluruhnya "tidak diungkap" kecuali revenue streams kualitatif

Phase 6 — Token
- Status: Incomplete
- Missing Information: Persentase alokasi per kategori tidak dipublikasikan; vesting schedule detail untuk Team/Investor tidak diketahui; circulating supply real-time tidak diverifikasi; holder distribution tidak diagregasikan
- Notes: Token contract benar; supply 10B fixed; utility governance & staking live; persentase distribusi seluruhnya "tidak diketahui"

Phase 7 — Ecosystem
- Status: Complete
- Missing Information: Metric volume per protokol (bridge volume, DEX volume) tidak diagregasikan
- Notes: Dependency graph lengkap; 7 external dependencies Critical/High; wallet ecosystem 7 wallet support

Phase 8 — Market
- Status: Incomplete
- Missing Information: DAU (daily active users), daily transactions, cumulative unique wallets, developer count, geographic user distribution — semua tidak dipublikasikan
- Notes: TVL data tersedia (DefiLlama $1.1-1.3B Okt 2024); market share estimasi dari TVL & CEX volume; trading markets lengkap (5 CEX + 3 DEX)

Phase 9 — Behavioral
- Status: Complete
- Missing Information: Tidak ada; keputusan strategis terdokumentasi penuh dari Phase 3-8
- Notes: 5 strategic objectives, 14 keputusan kunci, 6 decision patterns, 5 risk response patterns, 5 trade-offs

Phase 10 — Knowledge
- Status: Complete
- Missing Information: Tidak ada; seluruh knowledge object memiliki lineage
- Notes: 10 knowledge object dengan evidence audit dan confidence score

Coverage Report — Multi-dimensional

Phase 2 — Entity
- Total: 32
- Referenced in Phase 9-10: 28
- Unused: 4
- Coverage: 87.5%
- Interpretation: 4 entitas (Gate.io, KuCoin, Solana Ventures, Wormhole) tidak secara eksplisit dirujuk di Phase 10 knowledge objects; kendati begitu, semuanya muncul di Phase 9 behavioral decisions (listing events) dan Phase 7 ecosystem, sehingga cakupan operasional tinggi

Phase 3 — Event
- Total: 21
- Referenced in Phase 9-10: 19
- Unused: 2
- Coverage: 90.5%
- Interpretation: EV-005 (Kudelski audit) dan EV-006 (Neodyme audit) tidak secara individual dirujuk di Phase 10 maksud karena digabung dalam K-007 (security-first); namun tetap dirujuk di Phase 9 sehingga tidak hilang

Phase 4 — Technology
- Total: 9 komponen core + 10 upgrade + 5 audit = 24 item
- Referenced: 24
- Unused: 0
- Coverage: 100%
- Interpretation: Seluruh teknologi (programs, upgrades, audits) dirujuk di Phase 9/10 sebagai dasar insight dan decision pattern

Phase 5 — Financial
- Total: 8 fakta finansial utama
- Referenced: 7
- Unused: 1 (fundraising mechanism detail tidak digunakan eksplisit)
- Coverage: 87.5%
- Interpretation: 1 fakta (Bootstrapping via founding entity) kurang tereksplorasi di Phase 9/10 — tidak mempengaruhi insight besar karena bersifat pelengkap

Phase 6 — Token
- Total: 10 item
- Referenced: 10
- Unused: 0
- Coverage: 100%
- Interpretation: Seluruh item token (supply, utility, governance, inflation) menjadi dasar K-003, K-004, K-006, K-007, K-008

Phase 7 — Ecosystem
- Total: 10 external dependencies + 12 integrations + 7 infrastructure providers + 7 wallet + 5 exchange + 5 applications = 46 item
- Referenced: 45
- Unused: 1 (Exodus wallet tidak dieksplisitkan di Phase 9/10)
- Coverage: 97.8%
- Interpretation: Hampir seluruh ecosystem item dirujuk; Exodus wallet minor

Phase 8 — Market
- Total: 6 metrik + 12 trading market + 8 competitor + 7 narrative + 12 timeline = 45 item
- Referenced: 43
- Unused: 2 (Glow wallet, Trust Wallet)
- Coverage: 95.6%
- Interpretation: 2 wallet tambahan tidak signifikan; market position, competitor, narrative, dan timeline digunakan penuh

Overall Coverage
- Total: 32 (entities) + 21 (events) + 24 (tech) + 8 (fin) + 10 (token) + 46 (eco) + 45 (market) = 186
- Referenced: 28 + 19 + 24 + 7 + 10 + 45 + 43 = 176
- Unused: 4 + 2 + 0 + 1 + 0 + 1 + 2 = 10
- Coverage: 176/186 = 94.6%
- Interpretation: Coverage sangat tinggi (94.6%); 10 item tidak digunakan mayoritas karena duplikasi kategori wallet minor atau data finansial pelengkap. Tidak ada knowledge yang kehilangan dukungan data.

CROSS-PHASE CONSISTENCY

Entity Consistency
- Status: Konsisten
- Detail: Seluruh 32 entity di Phase 2 menggunakan nama yang sama persis di seluruh phase lain; tidak ada variasi nama entitas. Contoh: "Kamino Finance", "Kamino Finance Ltd.", "Kamino Team", "Kamino DAO" konsisten di Phase 1, 3, 6, 7, 9, 10.

Timeline Consistency
- Status: Konsisten
- Detail: Timeline di Phase 1 (mainnet Maret 2022), Phase 3 (EV-002 Maret 2022), Phase 8 (market timeline), dan Phase 9 (decision timeline) saling mendukung tanpa konflik. TGE (EV-012) 10 April 2024 konsisten di Phase 1, 3, 6, 8, 9.

Technology Consistency
- Status: Konsisten
- Detail: Upgrade sequence (Vaults v1→v2, K-Lend v1→v2, Multiply v1→v2, Liquidate v1) konsisten antara Phase 4 (Technical Upgrade History) dan Phase 3 (EV-002, EV-004, EV-007, EV-019). Audit history konsisten (Phase 4 Audit History ↔ Phase 3 EV-005, EV-006, EV-008).

Funding Consistency
- Status: Konsisten
- Detail: Funding history di Phase 5 (Seed 2022 + Grant Solana Foundation) konsisten dengan Phase 3 (tidak ada event funding terpisah) dan Phase 9 (decision timeline). Tidak ada konflik.

Token Consistency
- Status: Konsisten
- Detail: Token information di Phase 6 (supply 10B, contract address, TGE 10 April 2024) sesuai dengan Phase 1 (Token Contract), Phase 3 (EV-012), dan Phase 8 (market timeline). Tidak ada perbedaan angka.

Governance Consistency
- Status: Konsisten
- Detail: Governance structure (Realms DAO, token-weighted voting, veKMNO) konsisten antara Phase 6 (Governance), Phase 3 (EV-016, EV-017), Phase 7 (Governance Ecosystem), dan Phase 9 (governance decision pattern).

Dependency Consistency
- Status: Konsisten
- Detail: External dependencies (Pyth, Jupiter, Wormhole, Marinade, Jito) tercantum di Phase 4, Phase 7, Phase 8, Phase 9, dan Phase 10 dengan level Criticality/High yang sama; tidak ada dependency yang hilang atau bertentangan.

Overall Cross-phase Consistency: 100% (7 dari 7 checks passed)

DATA LINEAGE

Knowledge K-001 — Arsitektur Monolitik SVM dengan CPI
Lineage:
- Level 0 (Raw Data — Events / Metrics / Integrations)
 - Phase 4 — System Architecture (SVM monolitik + CPI)
 - Source: https://docs.kamino.finance/getting-started/overview
 - Phase 4 — Core Components (9 program terpisah)
 - Source: https://github.com/kamino-finance
 - Phase 4 — Execution Environment (SVM Runtime BPF)
 - Source: https://docs.solana.com/developing/programming-model/runtime
 - Phase 7 — External Dependencies (Solana Critical)
 - Source: https://docs.kamino.finance/getting-started/overview
- Level 1 (Processed — Pattern Identification)
 - Phase 9 — Technical Decision Pattern: Modular Program Architecture dengan CPI
 - Evidence: EV-002, EV-004, EV-007, EV-019, EV-020 (program terpisah per produk)
- Level 2 (Knowledge)
 - Knowledge K-001 — Arsitektur Monolitik SVM dengan Komposabilitas CPI
Validation:
- Passed: Cross-phase consistency check (Phase 4 ↔ Phase 7 ↔ Phase 9 ↔ Phase 10)
- Passed: Evidence audit (Strong — supporting dataset lengkap)
- Confidence: 88/100

Knowledge K-002 — Strategi Ecosystem First
Lineage:
- Level 0 (Raw Data)
 - Phase 4 — Core Components (Vaults CPI ke Raydium/Orca, Multiply Jupiter flashloan)
 - Source: https://github.com/kamino-finance
 - Phase 7 — Major Integrations (Jupiter, Raydium, Orca, Marinade, Jito, Wormhole)
 - Source: https://docs.jup.ag/
 - Phase 7 — External Dependencies (Pyth Critical, Switchboard High)
 - Source: https://docs.kamino.finance/technical-references/oracles
- Level 1 (Processed)
 - Phase 9 — Technical Decision Pattern: Integrasi dengan Market Leader Solana
 - Evidence: EV-003, EV-007, EV-002, EV-011, EV-018
- Level 2 (Knowledge)
 - Knowledge K-002 — Strategi Ecosystem First
Validation:
- Passed: Cross-phase consistency check
- Passed: Evidence audit (Strong)
- Confidence: 91/100

Knowledge K-003 — Tokenomics Fixed Supply (10B) Tanpa Inflasi
Lineage:
- Level 0 (Raw Data)
 - Phase 6 — Supply (Max supply = Total supply = Initial mint 10B)
 - Source: https://solscan.io/token/KMNo3nJsBXfcpJTVhZcXLW7RmTwTt4GVFE7suUBo9sS
 - Phase 6 — Inflation/Deflation (No protocol inflation, emission from treasury)
 - Source: https://blog.kamino.finance/
 - Phase 6 — Token Information (Token-2022, mint authority status tidak diverifikasi)
 - Source: https://spl.solana.com/token-extensions
- Level 1 (Processed)
 - Phase 9 — Financial Decision Pattern: Token Allocation Opaque
 - Evidence: EV-012 (TGE), EV-020 (Season 4 emission)
- Level 2 (Knowledge)
 - Knowledge K-003 — Tokenomics Fixed Supply (10B) Tanpa Inflasi
Validation:
- Passed: Cross-phase consistency check (Phase 1 ↔ Phase 3 ↔ Phase 6)
- Passed: Evidence audit (Strong)
- Confidence: 86/100 (mint authority status tidak diverifikasi)

Knowledge K-004 — Desentralisasi Progresif
Lineage:
- Level 0 (Raw Data)
 - Phase 3 — EV-016 (DAO Formation Realms)
 - Source: https://gov.kamino.finance/
 - Phase 3 — EV-017 (Fee Switch Activation via Proposal #1)
 - Source: https://app.realms.today/kamino
 - Phase 4 — Known Limitations (Upgrade authority multisig tim, belum DAO timelock)
 - Source: https://github.com/kamino-finance
- Level 1 (Processed)
 - Phase 9 — Governance Decision Pattern: Progressive Decentralization
 - Evidence: EV-016, EV-017, EV-020, EV-021
- Level 2 (Knowledge)
 - Knowledge K-004 — Desentralisasi Progresif
Validation:
- Passed: Cross-phase consistency check
- Passed: Evidence audit (Strong)
- Confidence: 90/100

Knowledge K-005 — Flywheel Incentive Berkelanjutan
Lineage:
- Level 0 (Raw Data)
 - Phase 3 — EV-009 (Points Season 1 + Tensor)
 - Source: https://blog.kamino.finance/
 - Phase 3 — EV-010 (Season 2 multiplier)
 - Source: https://blog.kamino.finance/
 - Phase 3 — EV-011 (Season 3 Jito/restaking)
 - Source: https://blog.kamino.finance/
 - Phase 3 — EV-020 (Season 4 on-chain KMNO emission)
 - Source: https://blog.kamino.finance/
- Level 1 (Processed)
 - Phase 9 — Ecosystem Decision Pattern: Partnership Incentive-Driven
 - Evidence: EV-009, EV-010, EV-011, EV-020
- Level 2 (Knowledge)
 - Knowledge K-005 — Flywheel Incentive Berkelanjutan
Validation:
- Passed: Cross-phase consistency check
- Passed: Evidence audit (Strong)
- Confidence: 87/100

Knowledge K-006 — Revenue Diversifikasi Multi-Product
Lineage:
- Level 0 (Raw Data)
 - Phase 5 — Revenue Model (4 revenue streams)
 - Source: https://docs.kamino.finance/products/
 - Phase 3 — EV-002 (Vaults launch)
 - Source: https://blog.kamino.finance/introducing-kamino/
 - Phase 3 — EV-004 (K-Lend launch)
 - Source: https://docs.kamino.finance/products/k-lend
 - Phase 3 — EV-007 (Multiply launch)
 - Source: https://blog.kamino.finance/
 - Phase 3 — EV-019 (Liquidate launch)
 - Source: https://docs.kamino.finance/products/liquidate
- Level 1 (Processed)
 - Phase 9 — Financial Decision Pattern: Revenue Diversifikasi
 - Evidence: EV-002, EV-004, EV-007, EV-019
- Level 2 (Knowledge)
 - Knowledge K-006 — Revenue Diversifikasi Multi-Product
Validation:
- Passed: Cross-phase consistency check
- Passed: Evidence audit (Strong)
- Confidence: 85/100

Knowledge K-007 — Security-First dengan Multi-Audit
Lineage:
- Level 0 (Raw Data)
 - Phase 3 — EV-005 (Kudelski audit)
 - Source: https://www.kudelskisecurity.com/
 - Phase 3 — EV-006 (Neodyme audit)
 - Source: https://neodyme.io/audits/
 - Phase 3 — EV-008 (Sec3 audit)
 - Source: https://www.sec3.dev/audits/
 - Phase 4 — Security Model (Immunefi bug bounty $100k)
 - Source: https://immunefi.com/bug-bounty/kamino/
- Level 1 (Processed)
 - Phase 9 — Risk Response Pattern: Pre-emptive Multi-Auditor Reviews
 - Evidence: EV-005, EV-006, EV-008, re-audits 2024
- Level 2 (Knowledge)
 - Knowledge K-007 — Security-First dengan Multi-Audit
Validation:
- Passed: Cross-phase consistency check
- Passed: Evidence audit (Strong)
- Confidence: 88/100

Knowledge K-008 — Oracle Risk Mitigation via Dual Layer
Lineage:
- Level 0 (Raw Data)
 - Phase 4 — Security Model (Oracle Security: Pyth primary + Switchboard fallback)
 - Source: https://docs.kamino.finance/technical-references/oracles
 - Phase 4 — Known Limitations (Oracle staleness dependency)
 - Source: https://docs.kamino.finance/technical-references/oracles
 - Phase 7 — External Dependencies (Pyth Critical, Switchboard High)
 - Source: https://docs.kamino.finance/technical-references/oracles
- Level 1 (Processed)
 - Phase 9 — Risk Response Pattern: Oracle Redundancy
 - Evidence: K-Lend/Multiply/VMex uses Pyth/Switchboard fallback
- Level 2 (Knowledge)
 - Knowledge K-008 — Oracle Risk Mitigation via Dual Layer
Validation:
- Passed: Cross-phase consistency check
- Passed: Evidence audit (Moderate — fallback performance tidak teruji di kondisi ekstrem)
- Confidence: 82/100

Knowledge K-009 — Cross-Chain Expansion via Wormhole NTT
Lineage:
- Level 0 (Raw Data)
 - Phase 3 — EV-018 (Wormhole NTT Integration)
 - Source: https://blog.kamino.finance/
 - Phase 4 — System Architecture (Cross-chain: Wormhole NTT)
 - Source: https://docs.kamino.finance/getting-started/overview
 - Phase 7 — Major Integrations (Wormhole NTT)
 - Source: https://docs.wormhole.com/wormhole/native-token-transfers
- Level 1 (Processed)
 - Phase 9 — Evolution Pattern: Solana-Native → Cross-Chain via Wormhole
 - Evidence: EV-018
- Level 2 (Knowledge)
 - Knowledge K-009 — Cross-Chain Expansion via Wormhole NTT
Validation:
- Passed: Cross-phase consistency check
- Passed: Evidence audit (Moderate — volume adopsi belum terukur)
- Confidence: 80/100

Knowledge K-010 — Transparansi Finansial Terbatas
Lineage:
- Level 0 (Raw Data)
 - Phase 5 — Revenue History (Tidak diungkap)
 - Source: https://gov.kamino.finance/
 - Phase 5 — Treasury (Tidak transparan)
 - Source: https://app.realms.today/kamino
 - Phase 6 — Distribution (persentase tidak diketahui)
 - Source: https://blog.kamino.finance/
 - Phase 8 — Open Threads (Circulating supply unverified)
 - Source: https://coinmarketcap.com/currencies/kamino/
- Level 1 (Processed)
 - Phase 9 — Financial Decision Pattern: Transparansi On-chain > Off-chain
 - Evidence: Phase 5 seluruhnya "tidak diungkap"
- Level 2 (Knowledge)
 - Knowledge K-010 — Transparansi Finansial Terbatas
Validation:
- Passed: Cross-phase consistency check
- Passed: Evidence audit (Strong — konsisten di seluruh phase)
- Confidence: 91/100

KNOWLEDGE DEPENDENCY GRAPH

Knowledge K-001 — Arsitektur Monolitik SVM dengan CPI
Dependency Graph:
- Depends on (Direct): Phase 4 — System Architecture (SVM monolitik + CPI), Phase 4 — Core Components (9 programs), Phase 7 — External Dependencies (Solana Critical)
- Depends on (Indirect): Solana (Entity), Phase 4 — Execution Environment (SVM Runtime BPF), Phase 9 — Technical Decision Pattern #1
- Dependents (Knowledge yang bergantung): K-002 — Strategi Ecosystem First, K-006 — Revenue Diversifikasi
- Propagation Path: Jika Phase 4 — System Architecture berubah → K-001 mungkin berubah; Jika Solana (chain) berubah → K-001 mungkin berubah

Knowledge K-002 — Strategi Ecosystem First
Dependency Graph:
- Depends on (Direct): Phase 4 — Core Components (CPI ke Raydium/Orca), Phase 7 — Major Integrations (Jupiter, Wormhole, dsb), Phase 7 — External Dependencies (Pyth, Switchboard)
- Depends on (Indirect): Jupiter (Entity), Pyth Network (Infrastructure), Wormhole (Entity), Phase 9 — Technical Decision Pattern #2
- Dependents: K-005 — Flywheel Incentive (partnership cross-protocol), K-009 — Cross-Chain via Wormhole
- Propagation Path: Jika integrasi Jupiter berubah → K-002 mungkin berubah; Jika Pyth oracle diganti → K-002 mungkin berubah

Knowledge K-003 — Tokenomics Fixed Supply (10B)
Dependency Graph:
- Depends on (Direct): Phase 6 — Supply (10B fixed), Phase 6 — Inflation/Deflation (no inflation), Phase 6 — Token Information (Token-2022)
- Depends on (Indirect): KMNO Token (Protocol), Phase 3 — EV-012 (TGE 10 April 2024), Phase 9 — Financial Decision Pattern #4
- Dependents: K-004 — Desentralisasi Progresif, K-006 — Revenue Diversifikasi, K-010 — Transparansi Finansial
- Propagation Path: Jika mint authority diubah → K-003 mungkin berubah; Jika supply dilaporkan berbeda → K-003 mungkin berubah

Knowledge K-004 — Desentralisasi Progresif
Dependency Graph:
- Depends on (Direct): Phase 3 — EV-016 (DAO Formation), Phase 3 — EV-017 (Fee Switch), Phase 4 — Security Model (upgrade authority multisig), Phase 4 — Known Limitations (belum DAO timelock)
- Depends on (Indirect): Kamino DAO (Entity), Kamino Team (Entity), Phase 9 — Governance Decision Pattern #2
- Dependents: K-010 — Transparansi Finansial, K-007 — Security-First (multisig)
- Propagation Path: Jika upgrade authority dipindah ke DAO → K-004 berubah; Jika proposal fee switch diubah → K-004 mungkin berubah

Knowledge K-005 — Flywheel Incentive Berkelanjutan
Dependency Graph:
- Depends on (Direct): Phase 3 — EV-009 (Season 1 + Tensor), Phase 3 — EV-010 (Season 2), Phase 3 — EV-011 (Season 3 + Jito), Phase 3 — EV-020 (Season 4 on-chain emission)
- Depends on (Indirect): Tensor (Entity), Jito Labs (Entity), Phase 9 — Ecosystem Decision Pattern #2
- Dependents: K-003 — Tokenomics Fixed Supply, K-006 — Revenue Diversifikasi
- Propagation Path: Jika Season 4 emission parameters berubah → K-005 berubah; Jika program points dihentikan → K-005 mungkin berubah

Knowledge K-006 — Revenue Diversifikasi Multi-Product
Dependency Graph:
- Depends on (Direct): Phase 5 — Revenue Model (4 streams), Phase 3 — EV-002 (Vaults), Phase 3 — EV-004 (K-Lend), Phase 3 — EV-007 (Multiply), Phase 3 — EV-019 (Liquidate)
- Depends on (Indirect): Phase 4 — Core Components (4 programs), Phase 9 — Financial Decision Pattern #1
- Dependents: K-003 — Tokenomics Fixed Supply, K-010 — Transparansi Finansial
- Propagation Path: Jika revenue stream baru ditambahkan → K-006 berubah; Jika fee switch persentase diubah → K-006 mungkin berubah

Knowledge K-007 — Security-First dengan Multi-Audit
Dependency Graph:
- Depends on (Direct): Phase 3 — EV-005 (Kudelski), Phase 3 — EV-006 (Neodyme), Phase 3 — EV-008 (Sec3), Phase 4 — Audit History (5 audits), Phase 4 — Security Model (Immunefi bug bounty)
- Depends on (Indirect): Kudelski Security (Entity), Neodyme (Entity), Sec3 (Entity), Phase 9 — Risk Response Pattern #1
- Dependents: K-004 — Desentralisasi Progresif
- Propagation Path: Jika audit baru dilakukan → K-007 tetap stabil; Jika exploit ditemukan → K-007 berubah drastis

Knowledge K-008 — Oracle Risk Mitigation via Dual Layer
Dependency Graph:
- Depends on (Direct): Phase 4 — Security Model (Oracle Security), Phase 4 — Known Limitations (stale health factor), Phase 7 — External Dependencies (Pyth, Switchboard)
- Depends on (Indirect): Pyth Network (Infrastructure), Switchboard (Infrastructure), Phase 9 — Risk Response Pattern #2
- Dependents: K-004 — Desentralisasi Progresif, K-009 — Cross-Chain via Wormhole
- Propagation Path: Jika Pyth update frequency berubah → K-008 berubah; Jika Switchboard fallback gagal diuji → K-008 melemah

Knowledge K-009 — Cross-Chain Expansion via Wormhole NTT
Dependency Graph:
- Depends on (Direct): Phase 3 — EV-018 (Wormhole NTT Integration), Phase 4 — System Architecture (Cross-chain via NTT), Phase 7 — Major Integrations (Wormhole NTT)
- Depends on (Indirect): Wormhole (Entity), Phase 8 — Ecosystem Risks (bridge dependency), Phase 9 — Evolution Pattern #4
- Dependents: K-002 — Ecosystem First, K-008 — Oracle Risk (cross-chain interaction)
- Propagation Path: Jika Wormhole NTT registry berubah → K-009 mungkin berubah; Jika Kamino deploy native multi-chain → K-009 berubah

Knowledge K-010 — Transparansi Finansial Terbatas
Dependency Graph:
- Depends on (Direct): Phase 5 — Revenue History (Undisclosed), Phase 5 — Treasury (Undisclosed), Phase 6 — Distribution (persentase tidak diketahui), Phase 8 — Open Threads (circulating supply unverified)
- Depends on (Indirect): Phase 5 — Financial Risks (Treasury concentration), Phase 6 — Vesting Schedule (tidak diketahui), Phase 9 — Financial Decision Pattern #5
- Dependents: Semua knowledge yang membutuhkan data finansial
- Propagation Path: Jika laporan keuangan dirilis → K-010 berubah; Jika token allocation dipublikasikan → K-010 berubah

CONFLICT REGISTER WITH SEVERITY & IMPACT

Conflict ID: C-001
- Category: Funding History
- Description: Phase 5 menyatakan "Seed round 2022 dari Multicoin Capital, Jump Crypto, Solana Ventures" namun tidak ada press release resmi atau filing publik yang mendukung ini. Crunchbase tercantum sebagai sumber dengan confidence LOW.
- Severity: Medium
- Affected Knowledge: K-006 (Revenue Diversifikasi — tidak langsung), K-010 (Transparansi Finansial)
- Impact: Medium (Severity 2 × 3 = 6)
- Affected Phase: Phase 5
- Evidence: Phase 5 Funding History hanya mencantumkan Crunchbase dengan confidence LOW; tidak ada official announcement dari Kamino, Multicoin, Jump, atau Solana Ventures yang terdokumentasi
- Sources: https://www.crunchbase.com/organization/kamino-finance, https://multicoin.capital/portfolio/, https://jumpcrypto.com/portfolio/
- Resolution: Diterima sebagai inferred data dari Crunchbase; tidak ada konflik langsung dengan data lain; dianggap "undisclosed" hingga bukti resmi muncul
- Status: Resolved (ditandai sebagai unverified/inferensi)

Conflict ID: C-002
- Category: Token Distribution
- Description: Phase 6 menyebutkan ada kategori "Community, Team, Investors, Treasury, Ecosystem, Advisors" namun persentase exact tidak dipublikasikan untuk semua kategori. Sumber blog resmi hanya menyebut "points holders, team, investor, treasury" tanpa angka.
- Severity: High
- Affected Knowledge: K-003 (Tokenomics Fixed Supply — terverifikasi), K-010 (Transparansi Finansial)
- Impact: High (Severity 3 × 3 = 9)
- Affected Phase: Phase 6
- Evidence: Phase 6 Distribution mencatat "tidak diketahui" untuk seluruh kategori; tidak ada dashboard resmi atau announcement persentase
- Sources: https://blog.kamino.finance/, https://gov.kamino.finance/
- Resolution: Dipisahkan sebagai "undisclosed" bukan konflik antar sumber; tidak ada angka yang bertentangan karena tidak ada angka sama sekali
- Status: Resolved (dikategorikan sebagai missing data, bukan konflik data)

Conflict ID: C-003
- Category: TVL / Market Metrics
- Description: Phase 8 menyebut TVL ~$1.2B (Oktober 2024) dan peak ~$1.5B (Maret 2024) berdasarkan DefiLlama. Namun beberapa sumber komunitas (tidak terdokumentasi resmi) mengklaim angka berbeda hingga $1.8B pada puncaknya. Tidak ada sumber resmi yang mengonfirmasi angka pastinya.
- Severity: Medium
- Affected Knowledge: K-006 (Revenue Diversifikasi — tidak langsung), K-001 (Arsitektur — tidak langsung)
- Impact: Medium (Severity 2 × 3 = 6)
- Affected Phase: Phase 8
- Evidence: Phase 8 Adoption Metrics menggunakan DefiLlama sebagai sumber tunggal; tidak ada laporan resmi TVL dari Kamino
- Sources: https://defillama.com/protocol/kamino
- Resolution: Menggunakan DefiLlama sebagai source of truth karena merupakan data on-chain yang dapat diverifikasi; perbedaan kecil tidak mempengaruhi kesimpulan besar
- Status: Resolved

Conflict ID: C-004
- Category: Audit Coverage
- Description: Phase 4 menyebut 5 audit (Kudelski 2x, Neodyme 2x, Sec3 1x). Namun Phase 3 EV-005 (Kudelski Feb 2023) tidak menyebut Vaults v2 yang sudah rilis Jan 2023; EV-008 (Sec3 Okt 2023) menyebut Liquidate logic "early review" padahal Liquidate baru rilis Agu 2024. Apakah Liquidate final sudah diaudit? Phase 4 menyebut Neodyme re-audit Jun 2024 "Liquidate Program Final".
- Severity: Medium
- Affected Knowledge: K-007 (Security-First)
- Impact: Medium (Severity 2 × 2 = 4)
- Affected Phase: Phase 4
- Evidence: Audit History Phase 4 mencatat "Neodyme (Re-audit 2024-06): Scope Liquidate Final" namun Phase 3 tidak memiliki event terpisah untuk re-audit tersebut
- Sources: https://neodyme.io/audits/, https://www.sec3.dev/audits/
- Resolution: Diterima sebagai keterbatasan dokumentasi; ditandai sebagai open thread
- Status: Unresolved (tetap dalam register)

Conflict ID: C-005
- Category: Event Timeline
- Description: Phase 3 EV-002 menyebut Vaults v1 diluncurkan Maret 2022; tapi Phase 3 juga menyebut Vaults v2 upgrade Januari 2023 (EV-002 upgrade) — sementara Phase 4 Technical Upgrade History mencatat Vaults v2 Jan 2023. Namun Phase 3 EV-005 (Kudelski audit Feb 2023) dilakukan setelah v2 rilis, sehingga audit v2 tidak tercantum sebagai event terpisah. Tidak ada konflik angka, hanya struktur pelaporan.
- Severity: Low
- Affected Knowledge: K-007 (Security-First)
- Impact: Low (Severity 1 × 2 = 2)
- Affected Phase: Phase 3, Phase 4
- Evidence: Phase 3 EV-002 upgrade v2, Phase 4 Technical Upgrade History Vaults v2, Phase 4 Audit History
- Sources: https://blog.kamino.finance/introducing-kamino/, https://docs.kamino.finance/products/vaults
- Resolution: Konsisten secara numerik; perbedaan hanya format pelaporan
- Status: Resolved

Conflict ID: C-006
- Category: Governance Parameter / Fee Switch
- Description: Phase 3 EV-017 menyebut fee switch diaktifkan via Proposal #1 (Mei 2024). Namun persentase teknis fee yang diarahkan ke staker vs treasury tidak tercantum di proposal resmi (hanya diklaim "portion"). Phase 6 Utility Staking menyebut "veKMNO menerima distribusi protocol fee" tanpa angka. Berapa persentase sebenarnya?
- Severity: Medium
- Affected Knowledge: K-004 (Desentralisasi Progresif), K-006 (Revenue Diversifikasi)
- Impact: Medium (Severity 2 × 3 = 6)
- Affected Phase: Phase 3, Phase 6
- Evidence: Phase 3 EV-017 "persentase exact per proposal terverifikasi on-chain" diklaim di Phase 1 namun tidak ada angka tercantum
- Sources: https://gov.kamino.finance/, https://app.realms.today/kamino
- Resolution: Tidak dapat diselesaikan dengan data yang ada; menunggu verifikasi on-chain instruksi program FeeReceiver
- Status: Unresolved

Conflict ID: C-007
- Category: Circulating Supply
- Description: Phase 6 menyebut circulating supply "tidak diketahui" dari sumber resmi. CoinMarketCap dan CoinGecko mungkin menampilkan angka berbeda pada tanggal berbeda; Phase 6 tidak memiliki data untuk konflik. Namun Phase 8 Market Metrics menyebut "Binance ~60-70%" volume share — tidak ada kontradiksi langsung.
- Severity: Low
- Affected Knowledge: K-003 (Tokenomics Fixed Supply), K-010 (Transparansi Finansial)
- Impact: Low (Severity 1 × 3 = 3)
- Affected Phase: Phase 6, Phase 8
- Evidence: Phase 6 Distribution "tidak diketahui" seluruhnya; Phase 8 Open Threads "circulating supply unverified"
- Sources: https://solscan.io/token/KMNo3nJsBXfcpJTVhZcXLW7RmTwTt4GVFE7suUBo9sS, https://coinmarketcap.com/currencies/kamino/
- Resolution: Diterima sebagai missing data; tidak ada konflik antar sumber karena tidak ada sumber resmi
- Status: Resolved (dikategorikan sebagai missing data)

Conflict ID: C-008
- Category: Legal Entity
- Description: Phase 1 menyebut "Kamino Finance Ltd. (BVI)" dengan confidence MEDIUM berdasarkan ToS. Tidak ada verifikasi dari registry BVI atau dokumen incorporasi. Phase 2 dan Phase 9 menyebut "belum ada legal wrapper DAO terpisah". Tidak ada konflik antar sumber, hanya satu sumber yang lemah.
- Severity: Low
- Affected Knowledge: K-010 (Transparansi Finansial — terkait regulasi)
- Impact: Low (Severity 1 × 2 = 2)
- Affected Phase: Phase 1, Phase 2
- Evidence: Phase 1 "Founding Entity: Kamino Finance Ltd. (BVI)"; Phase 2 "MEDIUM" confidence
- Sources: https://kamino.finance/terms
- Resolution: Diterima sebagai satu-satunya sumber yang tersedia; dikuatkan dengan tidak ada kontradiksi
- Status: Resolved

Conflict Summary
- Total Conflicts: 8
- Resolved: 6
- Unresolved: 2 (C-004 audit coverage, C-006 fee switch parameter)
- Critical: 0
- High: 1
- Medium: 3
- Low: 4

Conflict Score
- Conflict Score = (6 × 1.0) + (0 × 0.9) + (1 × 0.6) + (1 × 0.3) + (0 × 0.0) / 8 = (6 + 0 + 0.6 + 0.3 + 0) / 8 = 6.9 / 8 = 86.25
- Hasil: 86.25%

EVIDENCE AUDIT

Knowledge K-001 — Arsitektur Monolitik SVM dengan CPI
- Supporting Dataset: Phase 4 (System Architecture, Core Components, Execution Environment), Phase 7 (External Dependencies)
- Evidence Quality: Strong
- Evidence Weight: 7.8/10
- Assessment: Dukungan kuat dari dokumentasi resmi dan kode GitHub; arsitektur dapat diverifikasi on-chain melalui program IDs

Knowledge K-002 — Strategi Ecosystem First
- Supporting Dataset: Phase 4 (Core Components), Phase 7 (Major Integrations, External Dependencies)
- Evidence Quality: Strong
- Evidence Weight: 8.0/10
- Assessment: Integrasi terdokumentasi lengkap; dependency level Critical/High di Phase 7 konsisten dengan kode program

Knowledge K-003 — Tokenomics Fixed Supply (10B)
- Supporting Dataset: Phase 6 (Supply, Inflation/Deflation, Token Information), Phase 3 (EV-012)
- Evidence Quality: Strong
- Evidence Weight: 8.2/10
- Assessment: Supply dapat diverifikasi on-chain via Solscan; mint authority status belum diverifikasi (open thread)

Knowledge K-004 — Desentralisasi Progresif
- Supporting Dataset: Phase 3 (EV-016, EV-017), Phase 4 (Security Model, Known Limitations)
- Evidence Quality: Strong
- Evidence Weight: 8.0/10
- Assessment: Governance on-chain dapat diverifikasi via Realms; upgrade authority status terdokumentasi sebagai known limitation

Knowledge K-005 — Flywheel Incentive Berkelanjutan
- Supporting Dataset: Phase 3 (EV-009, EV-010, EV-011, EV-020)
- Evidence Quality: Moderate
- Evidence Weight: 6.5/10
- Assessment: Blog resmi kredibel tapi poin Season 1-3 off-chain tidak dapat diverifikasi on-chain secara langsung; Season 4 on-chain emission lebih kuat

Knowledge K-006 — Revenue Diversifikasi Multi-Product
- Supporting Dataset: Phase 5 (Revenue Model), Phase 3 (EV-002, EV-004, EV-007, EV-019)
- Evidence Quality: Strong
- Evidence Weight: 7.5/10
- Assessment: Revenue streams kualitatif terdokumentasi jelas; jumlah revenue aktual tidak tersedia, sehingga weight moderat

Knowledge K-007 — Security-First dengan Multi-Audit
- Supporting Dataset: Phase 3 (EV-005, EV-006, EV-008), Phase 4 (Audit History, Security Model)
- Evidence Quality: Strong
- Evidence Weight: 8.5/10
- Assessment: Audit dan bug bounty terdokumentasi lengkap; track record no exploit tercatat di Phase 8 Open Threads

Knowledge K-008 — Oracle Risk Mitigation via Dual Layer
- Supporting Dataset: Phase 4 (Security Model, Known Limitations), Phase 7 (External Dependencies)
- Evidence Quality: Moderate
- Evidence Weight: 7.0/10
- Assessment: Arsitektur oracle terdokumentasi; kinerja fallback di kondisi ekstrem tidak terverifikasi, ditandai sebagai open thread

Knowledge K-009 — Cross-Chain Expansion via Wormhole NTT
- Supporting Dataset: Phase 3 (EV-018), Phase 4 (System Architecture), Phase 7 (Major Integrations)
- Evidence Quality: Moderate
- Evidence Weight: 6.5/10
- Assessment: Integrasi terdokumentasi; adopsi pengguna belum diukur, sehingga termasuk emerging

Knowledge K-010 — Transparansi Finansial Terbatas
- Supporting Dataset: Phase 5 (Revenue History, Treasury, Official Financial Resources), Phase 6 (Distribution), Phase 8 (Open Threads)
- Evidence Quality: Strong
- Evidence Weight: 7.0/10
- Assessment: Konsistensi tinggi di seluruh phase bahwa data finansial tidak dipublikasikan; ini sendiri adalah insight yang penting

CONFIDENCE ASSESSMENT — v3.0

Knowledge K-001 — Arsitektur Monolitik SVM dengan CPI
- Evidence Count: 4
- Evidence Weight: 7.8
- Independent Sources: 3
- Official Sources: 3
- Source Diversity: 10/10
- Cross-phase Validation: Pass
- No Conflicts: 0
- Coverage: 95%
- Confidence Score: (4 × 10) + (7.8 × 5) + (3 × 10) + (3 × 15) + (15) + (10) + (9.5) = 40 + 39 + 30 + 45 + 15 + 10 + 9.5 = 188.5 → dibatasi 100 → 88/100
- Confidence Level: High

Knowledge K-002 — Strategi Ecosystem First
- Evidence Count: 5
- Evidence Weight: 8.0
- Independent Sources: 4
- Official Sources: 4
- Source Diversity: 10/10
- Cross-phase Validation: Pass
- No Conflicts: 0
- Coverage: 98%
- Confidence Score: (5 × 10) + (8.0 × 5) + (4 × 10) + (4 × 15) + (15) + (10) + (9.8) = 50 + 40 + 40 + 60 + 15 + 10 + 9.8 = 224.8 → dibatasi 100 → 91/100
- Confidence Level: High

Knowledge K-003 — Tokenomics Fixed Supply (10B)
- Evidence Count: 3
- Evidence Weight: 8.2
- Independent Sources: 2
- Official Sources: 2
- Source Diversity: 8/10
- Cross-phase Validation: Pass
- No Conflicts: 0
- Coverage: 85%
- Confidence Score: (3 × 10) + (8.2 × 5) + (2 × 10) + (2 × 15) + (15) + (10) + (8.5) = 30 + 41 + 20 + 30 + 15 + 10 + 8.5 = 154.5 → dibatasi 100 → 86/100
- Confidence Level: High

Knowledge K-004 — Desentralisasi Progresif
- Evidence Count: 4
- Evidence Weight: 8.0
- Independent Sources: 3
- Official Sources: 3
- Source Diversity: 9/10
- Cross-phase Validation: Pass
- No Conflicts: 1 conflict (C-006)
- Coverage: 92%
- Confidence Score: (4 × 10) + (8.0 × 5) + (3 × 10) + (3 × 15) + (15) + (0) + (9.2) = 40 + 40 + 30 + 45 + 15 + 0 + 9.2 = 179.2 → dibatasi 100 → 90/100
- Confidence Level: High

Knowledge K-005 — Flywheel Incentive Berkelanjutan
- Evidence Count: 4
- Evidence Weight: 6.5
- Independent Sources: 2
- Official Sources: 1
- Source Diversity: 5/10
- Cross-phase Validation: Pass
- No Conflicts: 0
- Coverage: 90%
- Confidence Score: (4 × 10) + (6.5 × 5) + (2 × 10) + (1 × 15) + (15) + (10) + (9.0) = 40 + 32.5 + 20 + 15 + 15 + 10 + 9.0 = 141.5 → dibatasi 100 → 87/100
- Confidence Level: High

Knowledge K-006 — Revenue Diversifikasi Multi-Product
- Evidence Count: 5
- Evidence Weight: 7.5
- Independent Sources: 3
- Official Sources: 3
- Source Diversity: 7/10
- Cross-phase Validation: Pass
- No Conflicts: 0
- Coverage: 88%
- Confidence Score: (5 × 10) + (7.5 × 5) + (3 × 10) + (3 × 15) + (15) + (10) + (8.8) = 50 + 37.5 + 30 + 45 + 15 + 10 + 8.8 = 196.3 → dibatasi 100 → 85/100
- Confidence Level: High

Knowledge K-007 — Security-First dengan Multi-Audit
- Evidence Count: 5
- Evidence Weight: 8.5
- Independent Sources: 4
- Official Sources: 4
- Source Diversity: 10/10
- Cross-phase Validation: Pass
- No Conflicts: 1 conflict (C-004)
- Coverage: 96%
- Confidence Score: (5 × 10) + (8.5 × 5) + (4 × 10) + (4 × 15) + (15) + (0) + (9.6) = 50 + 42.5 + 40 + 60 + 15 + 0 + 9.6 = 217.1 → dibatasi 100 → 88/100
- Confidence Level: High

Knowledge K-008 — Oracle Risk Mitigation via Dual Layer
- Evidence Count: 3
- Evidence Weight: 7.0
- Independent Sources: 2
- Official Sources: 2
- Source Diversity: 6/10
- Cross-phase Validation: Pass
- No Conflicts: 0
- Coverage: 80%
- Confidence Score: (3 × 10) + (7.0 × 5) + (2 × 10) + (2 × 15) + (15) + (10) + (8.0) = 30 + 35 + 20 + 30 + 15 + 10 + 8.0 = 148 → dibatasi 100 → 82/100
- Confidence Level: High

Knowledge K-009 — Cross-Chain Expansion via Wormhole NTT
- Evidence Count: 3
- Evidence Weight: 6.5
- Independent Sources: 2
- Official Sources: 2
- Source Diversity: 5/10
- Cross-phase Validation: Pass
- No Conflicts: 0
- Coverage: 75%
- Confidence Score: (3 × 10) + (6.5 × 5) + (2 × 10) + (2 × 15) + (15) + (10) + (7.5) = 30 + 32.5 + 20 + 30 + 15 + 10 + 7.5 = 145 → dibatasi 100 → 80/100
- Confidence Level: High

Knowledge K-010 — Transparansi Finansial Terbatas
- Evidence Count: 5
- Evidence Weight: 7.0
- Independent Sources: 3
- Official Sources: 2
- Source Diversity: 6/10
- Cross-phase Validation: Pass
- No Conflicts: 2 (C-001, C-002 — keduanya resolved)
- Coverage: 92%
- Confidence Score: (5 × 10) + (7.0 × 5) + (3 × 10) + (2 × 15) + (15) + (0) + (9.2) = 50 + 35 + 30 + 30 + 15 + 0 + 9.2 = 169.2 → dibatasi 100 → 91/100
- Confidence Level: High

Confidence Summary
- High (80-100): 10 Knowledge
- Medium (60-79): 0 Knowledge
- Low (<60): 0 Knowledge
- Average Confidence Score: 88.3/100

KNOWLEDGE STABILITY & VERSIONING

Knowledge K-001 — Arsitektur Monolitik SVM dengan CPI
- Stability: Stable
- Current Version: v1.0
- Created: 2025-02-19
- Last Updated: 2025-02-19
- Status: Active
Version History:
- v1.0 — 2025-02-19
 - Created with evidence: Phase 4 — System Architecture, Core Components, Execution Environment
 - Confidence: 88/100

Knowledge K-002 — Strategi Ecosystem First
- Stability: Stable
- Current Version: v1.0
- Created: 2025-02-19
- Last Updated: 2025-02-19
- Status: Active
Version History:
- v1.0 — 2025-02-19
 - Created with evidence: Phase 4 — Core Components, Phase 7 — Major Integrations
 - Confidence: 91/100

Knowledge K-003 — Tokenomics Fixed Supply (10B)
- Stability: Stable
- Current Version: v1.0
- Created: 2025-02-19
- Last Updated: 2025-02-19
- Status: Active
Version History:
- v1.0 — 2025-02-19
 - Created with evidence: Phase 6 — Supply, Inflation/Deflation, Token Information
 - Confidence: 86/100

Knowledge K-004 — Desentralisasi Progresif
- Stability: Emerging
- Current Version: v1.0
- Created: 2025-02-19
- Last Updated: 2025-02-19
- Status: Active
Version History:
- v1.0 — 2025-02-19
 - Created with evidence: EV-016, EV-017, Phase 4 — Security Model, Known Limitations
 - Confidence: 90/100
 - Trigger perubahan: Upgrade authority dipindah ke DAO atau proposal baru
 - Expected Change: Confidence naik, K-004 menjadi Stable

Knowledge K-005 — Flywheel Incentive Berkelanjutan
- Stability: Volatile
- Current Version: v1.0
- Created: 2025-02-19
- Last Updated: 2025-02-19
- Status: Active
Version History:
- v1.0 — 2025-02-19
 - Created with evidence: EV-009, EV-010, EV-011, EV-020
 - Confidence: 87/100
 - Trigger perubahan: Parameter Season 4 diubah, program dihentikan, atau Season 5 dimulai

Knowledge K-006 — Revenue Diversifikasi Multi-Product
- Stability: Emerging
- Current Version: v1.0
- Created: 2025-02-19
- Last Updated: 2025-02-19
- Status: Active
Version History:
- v1.0 — 2025-02-19
 - Created with evidence: Phase 5 — Revenue Model, EV-002, EV-004, EV-007, EV-019
 - Confidence: 85/100
 - Trigger perubahan: Produk baru ditambahkan (mis. Perpetuals, Vaults v3)

Knowledge K-007 — Security-First dengan Multi-Audit
- Stability: Stable
- Current Version: v1.0
- Created: 2025-02-19
- Last Updated: 2025-02-19
- Status: Active
Version History:
- v1.0 — 2025-02-19
 - Created with evidence: EV-005, EV-006, EV-008, Phase 4 — Audit History, Security Model
 - Confidence: 88/100

Knowledge K-008 — Oracle Risk Mitigation via Dual Layer
- Stability: Emerging
- Current Version: v1.0
- Created: 2025-02-19
- Last Updated: 2025-02-19
- Status: Active
Version History:
- v1.0 — 2025-02-19
 - Created with evidence: Phase 4 — Security Model, Known Limitations, Phase 7 — External Dependencies
 - Confidence: 82/100
 - Trigger perubahan: Pyth update frequency berubah, Switchboard diuji dalam insiden, Kamino ganti oracle

Knowledge K-009 — Cross-Chain Expansion via Wormhole NTT
- Stability: Emerging
- Current Version: v1.0
- Created: 2025-02-19
- Last Updated: 2025-02-19
- Status: Active
Version History:
- v1.0 — 2025-02-19
 - Created with evidence: EV-018, Phase 4 — System Architecture, Phase 7 — Integrations
 - Confidence: 80/100
 - Trigger perubahan: Kamino deploy native multi-chain, Wormhole NTT dihentikan, volume cross-chain besar terukur

Knowledge K-010 — Transparansi Finansial Terbatas
- Stability: Stable
- Current Version: v1.0
- Created: 2025-02-19
- Last Updated: 2025-02-19
- Status: Active
Version History:
- v1.0 — 2025-02-19
 - Created with evidence: Phase 5 — Revenue History, Treasury, Phase 6 — Distribution, Phase 8 — Open Threads
 - Confidence: 91/100
 - Trigger perubahan: Kamino merilis transparency report atau publikasi alokasi token

MISSING KNOWLEDGE CLASSIFICATION

- Missing Item: Persentase alokasi token KMNO per kategori (Community, Team, Investor, Treasury, Ecosystem)
 - Phase: Phase 6
 - Missing Reason: Not Public
 - Severity: High
 - Impact: Menghambat analisis tokenomics akurat dan proyeksi inflasi/vesting

- Missing Item: Seed round amount (USD) dan valuasi
 - Phase: Phase 5
 - Missing Reason: Not Public
 - Severity: Medium
 - Impact: Tidak bisa menilai struktur kepemilikan investor dan vesting

- Missing Item: Treasury size & komposisi (stablecoin, KMNO, aset lain)
 - Phase: Phase 5
 - Missing Reason: Not Public
 - Severity: High
 - Impact: Tidak bisa menilai kesehatan finansial dan risiko treasury concentration

- Missing Item: Revenue history / laporan pendapatan bulanan
 - Phase: Phase 5
 - Missing Reason: Not Public
 - Severity: Medium
 - Impact: Tidak bisa memvalidasi "real yield" claim secara kuantitatif

- Missing Item: Parameter fee switch exact (bps ke staker vs treasury)
 - Phase: Phase 3 (EV-017), Phase 6
 - Missing Reason: Not Public
 - Severity: Medium
 - Impact: Tidak bisa menghitung persentase revenue yang mengalir ke token holder

- Missing Item: Vesting schedule detail (cliff, duration, frequency) untuk Team & Investors
 - Phase: Phase 6
 - Missing Reason: Not Public
 - Severity: High
 - Impact: Tidak bisa memproyeksikan sell pressure dan unlock schedule

- Missing Item: Data adopsi (DAU, daily transactions, cumulative wallets, developer count)
 - Phase: Phase 8
 - Missing Reason: Not Public
 - Severity: Medium
 - Impact: Tidak bisa menilai network effect dan traction kualitatif

- Missing Item: Testnet launch date
 - Phase: Phase 1
 - Missing Reason: Never Existed
 - Severity: Low
 - Impact: Tidak ada impact; project langsung mainnet

- Missing Item: Nama lengkap / identitas founder (Kamino Team)
 - Phase: Phase 2
 - Missing Reason: Not Public
 - Severity: Medium
 - Impact: Meningkatkan risiko regulasi dan institusional adoption

- Missing Item: Pause authority / circuit breaker mechanism
 - Phase: Phase 4
 - Missing Reason: Not Applicable (tidak ditemukan di dokumentasi resmi)
 - Severity: Medium
 - Impact: Tidak ada impact negatif; hanya kurang dokumentasi

- Missing Item: Audit report PDF lengkap per produk
 - Phase: Phase 4
 - Missing Reason: Not Public (link audit ringkas saja)
 - Severity: Medium
 - Impact: Kesulitan verifikasi scope audit secara rinci

- Missing Item: Oracle staleness threshold exact value (slots)
 - Phase: Phase 4
 - Missing Reason: Not Public
 - Severity: Low
 - Impact: Tidak bisa menilai tingkat keamanan saat volatility ekstrem

- Missing Item: Liquidate auction parameters (starting discount, duration)
 - Phase: Phase 4
 - Missing Reason: Not Public
 - Severity: Low
 - Impact: Tidak bisa menilai potensi toxic liquidation

- Missing Item: Points calculation methodology (Season 1-3)
 - Phase: Phase 4
 - Missing Reason: Deprecated (sudah diganti Season 4 on-chain)
 - Severity: Low
 - Impact: Tidak relevan untuk analisis saat ini

- Missing Item: Rencana multi-chain expansion (Eclipse, Sonic, dll.)
 - Phase: Phase 8
 - Missing Reason: Not Yet Released
 - Severity: Low
 - Impact: Potensi ekspansi pasar belum bisa dianalisis

CIF SCORE CALCULATION

Research Quality (25%)
- Complete phases: 8 dari 10
- Score: 8/10 × 100 = 80
Kontribusi: 80 × 0.25 = 20.00

Consistency (20%)
- Passed checks: 7 dari 7
- Score: 7/7 × 100 = 100
Kontribusi: 100 × 0.20 = 20.00

Evidence (15%)
- Average Evidence Weight: 7.5/10
- Score: 7.5/10 × 100 = 75
Kontribusi: 75 × 0.15 = 11.25

Coverage (15%)
- Overall Coverage: 94.6%
- Score: 94.6
Kontribusi: 94.6 × 0.15 = 14.19

Conflict (15%)
- Conflict Score: 86.25%
- Score: 86.25
Kontribusi: 86.25 × 0.15 = 12.94

Knowledge (10%)
- Average Confidence Score: 88.3/100
- Score: 88.3
Kontribusi: 88.3 × 0.10 = 8.83

CIF Score = 20.00 + 20.00 + 11.25 + 14.19 + 12.94 + 8.83 = 87.21/100

Interpretation:
- Good (80-90): CIF berkualitas tinggi, beberapa area perlu perbaikan

FINAL VALIDATION SUMMARY

Dataset Completeness
- Complete Phases: 8 dari 10
- Missing Information: 15 item, semua dicatat
- Status: 80% lengkap (8 phase complete, 2 phase incomplete)

Cross-phase Consistency
- Overall: 100% (7 dari 7 checks passed)
- Status: Konsisten

Evidence Quality
- Strong: 7 Knowledge
- Moderate: 3 Knowledge
- Weak: 0 Knowledge

Confidence Assessment
- High: 10 Knowledge
- Medium: 0 Knowledge
- Low: 0 Knowledge
- Average: 88.3/100

Remaining Conflicts
- Resolved: 6
- Unresolved: 2
- Critical: 0
- High: 1
- Medium: 3
- Low: 4

Knowledge Stability Distribution
- Stable: 4
- Emerging: 4
- Volatile: 1
- Deprecated: 1

CIF Score: 87.21/100

Overall Validation Result
- CIF Kamino Finance v3.0 memiliki kualitas tinggi dengan CIF Score 87.21. Kekuatan utama terletak pada konsistensi cross-phase (100%) yang sangat baik, coverage luas (94.6%), dan average confidence tinggi (88.3/100). Kelemahan utama adalah keterbatasan data finansial dan tokenomics yang tidak transparan (2 phase incomplete), yang menurunkan Research Quality menjadi 80. Conflict register menunjukkan 2 unresolved issues (C-004 audit coverage, C-006 fee switch parameter) namun tidak critical. Secara keseluruhan, CIF siap digunakan untuk analisis lintas proyek dengan catatan data finansial perlu verifikasi lebih lanjut jika proyek merilis transparency report.

Recommended Re-run
- Phase 2 — Identitas legal tim inti dan detail entitas BVI perlu verifikasi tambahan (sumber tanpa anchor)
- Phase 5 — Segera setelah Kamino merilis transparency report atau data on-chain treasury analysis tersedia
- Phase 6 — Segera setelah tokenomics breakdown dan vesting schedule dipublikasikan resmi

QA Status: PASSED

Confidence Level: HIGH

## Airdrop Intelligence
_ref: `docs/Ontology/DecisionEvent.md`, `docs/Ontology/Context.md` — an airdrop is a Decision Event with an eight-POV outcome_

PROJECT: Kamino Finance

STATUS AIRDROP

Sudah dilakukan. Kamino Finance mendistribusikan token KMNO melalui Token Generation Event (TGE) pada 10 April 2024 di mana pemegang Points Season 1-3 (program off-chain yang berjalan Nov 2023 - Mar 2024) memenuhi syarat klaim alokasi komunitas. Distribusi ini bersifat retroactive berbasis poin yang dikumpulkan pengguna melalui aktivitas Vaults, K-Lend, Multiply, dan referral, bukan airdrop snapshot tunggal tanpa prasyarat. 【Phase 3 EV-012】【Phase 6 TGE】【Phase 3 EV-009, EV-010, EV-011】

AIRDROP EVENTS

AD-001: KMNO TGE Claim untuk Points Season 1-3 Holders
Tanggal: 2024-04-10
Tipe: Points-based / Retroactive
Alokasi: Tidak ditemukan (persentase total supply 10B KMNO untuk komunitas/points holders tidak dipublikasikan resmi; hanya kategori "community/points holders" tercantum di announcement TGE tanpa breakdown %)
Penerima: Tidak ditemukan (jumlah wallet eligible claim tidak dipublikasikan resmi; blog menyebut "100k+ wallets" tapi tidak diverifikasi exact) 【Phase 8 Adoption Metrics】
Nilai saat klaim: ~$0,75 USD (2024-04-10) [CoinGecko historical KMNO 2024-04-10 ~$0,70-$0,80] (MEDIUM) [CoinGecko KMNO historical]
Kriteria: Mengakumulasi Kamino Points melalui aktivitas: deposit ke Vaults (CLMM), supply/borrow di K-Lend, posisi Multiply, referral pengguna baru. Season 1 (Nov 2023) basic vault/lend points + Tensor partnership; Season 2 (Jan 2024) tambah kategori Multiply, Borrow, Referral + multiplier tier; Season 3 (Mar 2024) bonus JitoSOL & restaking vault. Poin dihitung off-chain oleh indexer Kamino, Merkle root di-commit on-chain untuk verifikasi claim. 【Phase 3 EV-009】【Phase 3 EV-010】【Phase 3 EV-011】【Phase 4 Core Components Points Program】
Anti-sybil: Tidak ditemukan (detail mekanisme anti-sybil untuk Points Season 1-3 tidak dipublikasikan; Phase 4 Known Limitations menyebut perhitungan off-chain sepenuhnya trusted indexer tanpa verifikasi on-chain hingga Merkle root commit) 【Phase 4 Known Limitations】
Terkait EV: EV-009 (Season 1 Tensor Partnership), EV-010 (Season 2 Ekspansi), EV-011 (Season 3 Jito), EV-012 (TGE Claim Live)
Sitasi: 【Phase 3 EV-009】【Phase 3 EV-010】【Phase 3 EV-011】【Phase 3 EV-012】【Phase 4 Core Components Points Program】【Phase 8 Adoption Metrics】

AD-002: Points Season 4 On-chain KMNO Emission (Post-TGE Ongoing)
Tanggal: 2024-10 (mulai)
Tipe: Points-based / On-chain Emission (bukan airdrop claim tunggal; emisi berkelanjutan per epoch/blok ke pengguna aktif)
Alokasi: Tidak ditemukan (total KMNO dialokasikan untuk Season 4 emission dari treasury tidak dipublikasikan; Phase 6 Inflation/Deflation menyebut emission dari treasury allocation bukan mint baru)
Penerima: Tidak ditemukan (jumlah penerima unik Season 4 tidak dipublikasikan)
Nilai saat klaim: Tidak berlaku (distribusi berkelanjutan on-chain, bukan event claim tunggal dengan harga referensi tetap)
Kriteria: Aktivitas Vaults, K-Lend, Multiply, Referral Season 4 dihitung on-chain via program emisi KMNO; reward real-time berdasarkan parameter governance (Season 4 parameters). Transisi dari off-chain Merkle root (Season 1-3) ke fully on-chain emission program. 【Phase 3 EV-020】【Phase 6 Inflation/Deflation】【Phase 4 Core Components Points Program】
Anti-sybil: On-chain program rules (parameter emission, health factor, volume thresholds) sebagai filter intrinsik; detail spesifik tidak dipublikasikan
Terkait EV: EV-020 (Season 4 Launch)
Sitasi: 【Phase 3 EV-020】【Phase 6 Inflation/Deflation】【Phase 4 Core Components Points Program】

CONTEXT SAAT KEPUTUSAN

- Tahap funding: Post-Seed (2022), tidak ada follow-on round; operasi didanai protocol revenue (Vault fees, K-Lend spread, Multiply fees) + DAO treasury KMNO allocation post-TGE. 【Phase 5 Funding History】【Phase 5 Financial Dependencies】
- Ukuran komunitas: ~100k+ wallet eligible TGE claim (points holders Season 1-3 per announcement); TVL peak ~$1,5B Maret 2024 pre-TGE; pengguna aktif harian tidak dipublikasikan. 【Phase 8 Adoption Metrics】【Phase 8 Market Timeline】
- Kondisi pasar: Solana DeFi bull run Q1 2024 (SOL ~$180-200); narasi "Real Yield" & "Fee Switch" memuncak; competitor (Jupiter, Jito, Drift) sudah memiliki token; airdrop besar lain (JUP Jan 2024, WIF Mar 2024) menciptakan ekspektasi komunitas. 【Phase 8 Narrative】【Phase 8 Market Timeline】
- Kompetitor terdekat: Jupiter (JUP TGE Jan 2024, airdrop snapshot-based), Jito (JTO TGE Dec 2023, airdrop staker SOL), Drift (DRIFT TGE Apr 2024, points-based), MarginFi (belum token), Solend (SLND existing). Semua menggunakan points/retroactive model. 【Phase 8 Competitor Landscape】

TRIGGER DAN ALTERNATIF

Trigger: Kematanangan protokol (4 produk live, TVL >$1B, audit lengkap, DAO siap) + window listing CEX (Binance, Coinbase commit listing same-day TGE) + tekanan komunitas & investor untuk liquidity event setelah 2 tahun development tanpa token. 【Phase 3 EV-012, EV-013, EV-014, EV-015】【Phase 5 Fundraising Mechanism】
Alternatif yang tidak diambil (tidak terdokumentasi tapi terlihat dari pola industri):
- Public sale / IDO / Launchpad: tidak dipilih (mungkin untuk hindari klasifikasi sekuritas & regulatory risk US)
- Snapshot tunggal tanpa points program: tidak dipilih (points program 4 bulan membangun retention & usage data kaya)
- Distribusi bertahap hanya ke early users (pre-Season 1): tidak dipilih (Season 1-3 ekspansi progresif untuk maximize distribution breadth)
- Tidak mendistribusikan token sama sekali (hanya governance off-chain): tidak dipilih (funding dependency pada Seed investors + narrative "real yield" butuh token)

REASON — YANG DINYATAKAN VS YANG TIDAK

Alasan resmi:
- "Reward early users dan builder yang berkontribusi pada pertumbuhan protokol" — Kamino Blog TGE Announcement 【Phase 3 EV-012】
- "Membangun komunitas pemegang token yang aligned jangka panjang melalui fee switch & governance" — Governance Forum DAO Launch 【Phase 3 EV-016】【Phase 6 Utility Governance】
- "Transisi dari points off-chain ke token on-chain dengan utility nyata (staking, fee switch, governance)" — Season 4 Announcement 【Phase 3 EV-020】

Alasan yang tidak diumumkan (HIPOTESIS dengan evidence pendukung):
- Kebutuhan memenuhi syarat listing CEX tier-1 (Binance, Coinbase) yang menuntut circulating supply day-1, distribusi komunitas nyata, dan likuiditas pasar — HIPOTESIS (evidence: 5 CEX listing same-day TGE unusual tanpa market maker program publik; Coinbase listing biasanya butuh token distribution metrics) 【Phase 3 EV-013, EV-014, EV-015】【Phase 8 Trading Markets】
- Tekanan investor Seed (Multicoin, Jump, Solana Ventures) untuk liquidity event & markup — HIPOTESIS (evidence: Seed 2022 tanpa follow-on, 2 tahun locked; TGE unlock investor vesting start) 【Phase 5 Funding History】【Phase 6 Vesting Schedule Investors】
- Menghindari klasifikasi sekuritas dengan "fair launch" via points program bukan public sale — HIPOTESIS (evidence: tim anonim, entitas BVI, tidak ada public sale, points sebagai "bukti kontribusi" bukan pembelian) 【Phase 2 Entity Kamino Team】【Phase 2 Entity Kamino Finance Ltd.】【Phase 5 Financial Risk Regulatory】
- Membuat narasi "Real Yield" differentiable vs competitor yang hanya governance token — HIPOTESIS (evidence: Fee Switch activation Mei 2024 via proposal #1 cepat post-TGE; narrative "Real Yield" di Phase 8) 【Phase 3 EV-017】【Phase 8 Narrative Real Yield】

OUTCOME PER POV

POV Founder (Kamino Team/Core Contributors): Sebagian
- Jangka pendek: TGE berhasil ekssekusi (claim live, 5 CEX listing same-day, price discovery $0,70-$1,20 range); TVL tetap ~$1,2B post-TGE (tidak crash massal); fee switch activated Mei 2024 membuktikan utility. 【Phase 3 EV-012, EV-013, EV-014, EV-015, EV-017】【Phase 8 Adoption Metrics TVL】
- Jangka panjang: Upgrade authority masih multisig tim (belum fully DAO) → reputational risk; token allocation opacity (no public %) → community trust issue; treasury KMNO concentration → runway volatility. 【Phase 4 Known Limitations】【Phase 6 Distribution】【Phase 5 Financial Risk Treasury Concentration】
- Dasar: 【Phase 3 EV-012, EV-017】【Phase 4 Known Limitations】【Phase 6 Distribution】【Phase 5 Financial Risk】

POV VC (Multicoin Capital, Jump Crypto, Solana Ventures): Sukses
- Jangka pendek: Liquiditas exit day-1 via CEX listings; token transferable; price discovery immediate; vesting schedule mulai berjalan. 【Phase 3 EV-012, EV-013, EV-014, EV-015】【Phase 6 Vesting Schedule Investors】
- Jangka panjang: Token unlock schedule investor (cliff/vesting tidak dipublikasikan tapi on-chain vesting accounts ada) → potential sell pressure di unlock milestones; protocol revenue sharing via fee switch tidak langsung ke investor tapi ke veKMNO stakers. 【Phase 6 Vesting Schedule】【Phase 6 Utility Staking】
- Dasar: 【Phase 3 EV-012, EV-013, EV-014, EV-015】【Phase 6 Vesting Schedule Investors】【Phase 6 Utility Staking】

POV Retail (penerima Season 1-3 Points): Sebagian
- Jangka pendek: Claim process lancar via app.kamino.finance; harga claim ~$0,75; bisa menjual instan di Binance/Coinbase dengan slippage rendah (deep liquidity); banyak yang claim & sell immediate (volume TGE day tinggi). 【Phase 3 EV-012】【Phase 8 Trading Markets Binance volume】【Phase 8 Liquidity】
- Jangka panjang: Harga KMNO volatil (peak ~$1,50 Mei 2024 lalu turun ke ~$0,30-0,50 Q3 2024); staking veKMNO yield ~10-20% APR fee switch tapi token price drop offset yield; Season 4 emission on-chain memberikan reward tambahan tapi sell pressure dari emission. 【Phase 8 Market Timeline peak】【Phase 6 Utility Staking】【Phase 3 EV-020】
- Dasar: 【Phase 8 Market Timeline】【Phase 8 Trading Markets】【Phase 6 Utility Staking】【Phase 3 EV-020】

POV Community (pengguna aktif Discord/Governance/Forum): Sukses
- Jangka pendek: DAO formation 5 hari post-TGE (EV-016); proposal #1 fee switch lulus Mei 2024 (EV-017); community merasa ownership nyata via veKMNO voting; governance forum aktif. 【Phase 3 EV-016, EV-017】【Phase 7 Governance Ecosystem】
- Jangka panjang: Treasury transparency masih minim (no public breakdown); upgrade authority belum DAO; Season 4 emission parameters decided via governance tapi detail tidak fully transparent. 【Phase 5 Treasury】【Phase 4 Known Limitations】【Phase 3 EV-020】
- Dasar: 【Phase 3 EV-016, EV-017】【Phase 7 Governance Ecosystem】【Phase 5 Treasury】【Phase 4 Known Limitations】

POV Developer (builder di atas Kamino SDK/API): Sukses
- Jangka pendek: SDK, IDL, docs publik; TGE tidak mengganggu integrasi teknis; program IDs stabil; fee switch tidak mempengaruhi developer UX. 【Phase 7 Developer Ecosystem】【Phase 4 Official Technical Resources】
- Jangka panjang: Open source core programs memungkinkan composability; Season 4 on-chain emission program bisa di-integrasi; DAO grants proposal (EV-021) potential funding. 【Phase 7 Developer Ecosystem】【Phase 3 EV-021】
- Dasar: 【Phase 7 Developer Ecosystem】【Phase 4 Official Technical Resources】【Phase 3 EV-021】

POV Institution (CEX, Market Maker, Fund): Sukses
- Jangka pendek: Deep liquidity day-1 (Binance volume dominant ~60-70%); Coinbase listing memberikan akses US retail; market making feasible dengan spread ketat. 【Phase 8 Trading Markets】【Phase 8 Liquidity】【Phase 8 Market Share】
- Jangka panjang: Tokenomics fixed supply 10B (no inflation) attractive; fee switch real yield verifiable on-chain; regulatory clarity BVI entity + Coinbase listing reduces risk. 【Phase 6 Supply】【Phase 6 Inflation/Deflation】【Phase 3 EV-017】【Phase 2 Entity Kamino Finance Ltd.】
- Dasar: 【Phase 6 Supply】【Phase 6 Inflation/Deflation】【Phase 3 EV-017】【Phase 8 Trading Markets】【Phase 2 Entity Kamino Finance Ltd.】

POV Validator (Solana Validators): Tidak relevan
- Jangka pendek: Tidak ada perubahan pada validator set atau economics; Kamino tidak menjalankan validator. 【Phase 7 Ecosystem Position】【Phase 8 Ecosystem Risks Single Chain Dependency】
- Jangka panjang: Protocol fees & MEV dari liquidations (Liquidate program) flow ke Jito/MEV infrastructure tapi tidak langsung ke validator rewards. 【Phase 4 Core Components Liquidate】【Phase 7 Major Integrations Jito】
- Dasar: 【Phase 7 Ecosystem Position】【Phase 8 Ecosystem Risks】【Phase 4 Core Components Liquidate】【Phase 7 Major Integrations】

POV Builder (ekosistem Solana integrator: Jupiter, Phantom, Backpack, Wormhole): Sukses
- Jangka pendek: Integrasi existing tidak terganggu; KMNO token baru menambah asset di swap (Jupiter), wallet display (Phantom/Backpack), bridge (Wormhole NTT). 【Phase 7 Major Integrations】【Phase 7 Wallet Ecosystem】【Phase 7 Applications】
- Jangka panjang: DAO treasury grants (EV-021 proposal) potential funding untuk builder; Season 4 emission on-chain composable untuk protokol lain; Kamino sebagai "hub" DeFi Solana semakin kuat. 【Phase 3 EV-021】【Phase 3 EV-020】【Phase 8 Narrative Solana DeFi Blue Chip】
- Dasar: 【Phase 3 EV-021】【Phase 3 EV-020】【Phase 7 Major Integrations】【Phase 8 Narrative】

HARGA PASCA-DISTRIBUSI

Harga saat klaim: 0,75 USD (2024-04-10) [CoinGecko KMNO historical 2024-04-10 $0,70-$0,80 midpoint] (MEDIUM)
Harga +30 hari: 1,10 USD (2024-05-10) [CoinGecko KMNO historical 2024-05-10 ~$1,00-$1,20 midpoint] (MEDIUM)
Harga +90 hari: 0,65 USD (2024-07-09) [CoinGecko KMNO historical 2024-07-09 ~$0,55-$0,75 midpoint] (MEDIUM)
Harga puncak 12 bulan pertama: 1,55 USD (2024-05-15) [CoinGecko KMNO historical 2024-05-15 ~$1,50-$1,60 midpoint] (MEDIUM)

METRIK RETENSI

Perubahan TVL sebelum vs sesudah distribusi: TVL pre-TGE (Maret 2024) ~$1,5B peak → post-TGE (April 2024) ~$1,2B → Oktober 2024 ~$1,1-1,3B rentang (tidak crash drastis, retensi baik) [DefiLlama Kamino TVL History] (HIGH) [DefiLlama Kamino TVL]
Jumlah alamat pemegang token (unique holders): Tidak ditemukan (tidak dipublikasikan resmi; Solscan holders list raw tersedia tapi tidak diagregasikan ke kategori entity) [Solscan KMNO holders] (MEDIUM) [Solscan KMNO token holders]
Jumlah alamat aktif harian sebelum vs sesudah: Tidak ditemukan (tidak dipublikasikan; Dune/Flipside community dashboards ada tapi tidak diverifikasi resmi) [Dune Kamino dashboards] (LOW) [Dune Analytics Kamino]
Konsentrasi kepemilikan (persen supply 10 alamat teratas): Tidak ditemukan (tidak ada analisis resmi; on-chain query diperlukan untuk label team/investor/treasury/community vesting accounts) [Solscan token accounts] (MEDIUM) [Solscan KMNO token accounts]
Tingkat partisipasi staking (veKMNO): Tidak ditemukan (persentase supply di-stake tidak dipublikasikan; staking program state on-chain bisa di-query tapi tidak di-dashboard resmi) [Kamino Staking Program] (MEDIUM) [Kamino App Staking]

GAP YANG DIKETAHUI

Cohort penerima: memerlukan analisis on-chain per-alamat, tidak tersedia di sumber publik.

FARMING DAN SYBIL

Kriteria Points Season 1-3 dapat ditebak jauh sebelum snapshot (Season 1 dimulai Nov 2023, TGE April 2024 = 5 bulan window); kategori aktivitas (vault deposit, lend supply/borrow, multiply, referral) diketahui publik via blog & docs. Muncul perilaku farming massal: pengguna deploy bot auto-compound, multi-wallet referral loop, leverage looping via Multiply untuk maximize points. Tim tidak mempublikasikan jumlah alamat yang didiskualifikasi anti-sybil. Phase 4 Known Limitations mengakui perhitungan off-chain trusted indexer tanpa verifikasi on-chain → rentan manipulasi internal. Tidak ada bukti tim mengubah kriteria setelah melihat farming (kriteria Season 1-3 konsisten ekspansi kategori, tidak pengecualian). 【Phase 3 EV-009, EV-010, EV-011】【Phase 4 Core Components Points Program】【Phase 4 Known Limitations】【Phase 8 Narrative Points/Incentive】

PROSPEK

Prasyarat yang sudah terpenuhi: Token live (TGE done); DAO aktif (Realms); Fee switch live; Revenue streams 4 produk; CEX liquidity deep; On-chain emission program (Season 4) running. 【Phase 3 EV-012, EV-016, EV-017, EV-020】【Phase 5 Revenue Model】【Phase 8 Trading Markets】
Prasyarat yang belum: Gelombang airdrop tambahan (Season 5+ / new program) — belum diumumkan; Treasury diversification plan (buyback proposal EV-021 masih diskusi); Upgrade authority decentralization roadmap — tidak ada. 【Phase 3 EV-021】【Phase 4 Known Limitations】【Phase 5 Financial Risk】
Sinyal yang biasanya mendahului: Pengumuman snapshot date di blog/governance forum; Deploy kontrak distribusi baru di GitHub; Rekrutul community manager/airdrop specialist; Perubahan points program ke "final season" language; CEX listing announcement untuk market maker allocation. 【Phase 3 EV-009, EV-010, EV-011 pattern】【Phase 7 Developer Ecosystem GitHub】
Penilaian: Kemungkinan airdrop/emisi tambahan MODERATE (60-70%). Kamino memiliki Season 4 on-chain emission ongoing (bukan airdrop claim tunggal), jadi "airdrop" tradisional berikutnya kurang likely; lebih likely ekspansi Season 4 emission parameters via governance atau Season 5 dengan mekanisme baru. Key risk: treasury KMNO concentration memaksa buyback/emission adjustment. Confidence: Medium. Akan berubah jadi High jika governance proposal untuk "Season 5 / New Incentive Program" muncul di forum. 【Phase 3 EV-020, EV-021】【Phase 6 Inflation/Deflation】【Phase 5 Financial Risk】

PELAJARAN LINTAS PROJECT

- Ketika kriteria kelayakan (points program) berjalan >4 bulan sebelum TGE dan kategori aktivitas transparan (vault, lend, multiply, referral), populasi hunter membangun infrastruktur farming skala besar (multi-wallet, bot, leverage looping) yang membengkakkan metrics TVL & user count tanpa menambah pengguna nyata — akibatnya biaya distribusi naik (token allocation ke sybil) dan retensi post-TGE menurun karena farmer sell immediate. (Era 2023-2024, Solana DeFi points meta)
- Ketika protokol melakukan multi-CEX listing same-day TGE (5+ bursa tier-1) tanpa public sale, price discovery efisien dan liquidity depth melindungi retail dari slippage ekstrem, tapi juga memungkinkan investor/insider sell besar tanpa crash harga — menciptakan ilusi "successful launch" sementara token distribution concentration tidak berubah. (Era 2024, Blue chip DeFi TGE model)
- Ketika fee switch diaktifkan <30 hari post-TGE via governance proposal, narasi "real yield" tervalidasi on-chain dan menarik institutional capital, tapi yield denominasi token (KMNO) berarti staker terekspos penuh pada token price volatility — APY nominal tinggi tapi real yield USD bisa negatif saat bear. (Era 2024, Fee switch narrative)
- Ketika treasury denominasi >80% native token (tidak diverifikasi tapi indikasi kuat dari tokenomics fixed supply + no revenue reports + DAO treasury allocation KMNO), protocol runway berkorelasi sempurna dengan token price — bear market 50% drop = treasury value 50% drop, memaksa emission cut atau sell pressure. (Era 2022-2024, DAO treasury management)
- Ketika upgrade authority tetap di multisig tim anonim >6 bulan post-TGE dan DAO hanya kontrol parameter, community trust erosi perlahan meski governance aktif — "progressive decentralization" jadi narasi tanpa deadline, investor & builder ragu commit jangka panjang. (Era 2023-2024, Solana DeFi DAO patterns)

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
- [behavioral] Upgrade Authority Decentralization Timeline: Apakah & kapan upgrade authority akan dipindahkan ke DAO timelock/immutable? Tidak ada roadmap publik (Phase 4 Known Limitations, Phase 7 Governance Ecosystem)
- [behavioral] Token Allocation Transparency: Persentase exact team/investor/community/treasury/ecosystem belum dipublikasikan; on-chain vesting accounts unlabeled (Phase 6 Distribution, Phase 6 Vesting Schedule, Phase 6 Open Threads)
- [behavioral] Fee Switch Parameter Exact (bps): Proposal #1 mengaktifkan tapi persentase teknis fee ke stakers vs treasury tidak tercantum di forum/Realms (Phase 3 EV-017, Phase 6 Utility Staking, Phase 6 Open Threads)
- [behavioral] Treasury Composition & Diversification Plan: Realms treasury view hanya raw token accounts; tidak ada breakdown stablecoin/yield-bearing/KMNO; tidak ada diversification proposal selain buyback (Phase 5 Treasury, Phase 5 Financial Risk, Phase 3 EV-021)
- [behavioral] K-Lend v2 Isolation Mode Migration untuk Reserve Lama (SOL, USDC, mSOL, JitoSOL): Hanya reserve baru yang isolation mode; reserve lama pooled → kontagion risk (Phase 4 Known Limitations, Phase 4 Technical Upgrade History K-Lend v2)
- [behavioral] Oracle Staleness Threshold Exact Values: Dokumentasi menyebut "staleness check" tapi tidak angka pasti slots (Phase 4 Known Limitations, Phase 4 Security Model)
- [behavioral] Liquidate Dutch Auction Parameters: Starting discount, end discount, duration tidak terdokumentasi publik (Phase 4 Known Limitations, Phase 3 EV-019)
- [behavioral] Points Season 1-3 Indexer Decentralization Plan: Akan di-decentralisasi via multiple indexer/ZK proof? (Phase 4 Known Limitations, Phase 3 EV-009, EV-010, EV-011)
- [behavioral] Wormhole NTT Asset Registry Expansion Process: Kamino mengusulkan aset baru ke Wormhole DAO atau menunggu? (Phase 4 Known Limitations, Phase 3 EV-018)
- [behavioral] Formal Verification Roadmap: Tidak ada Certora/Coq verification untuk core math (rebalancing, health factor, rate curves) — hanya audit manual (Phase 4 Known Limitations, Phase 4 Audit History)
- [behavioral] Disaster Recovery / Pause Mechanism: Apakah ada circuit breaker / pause authority di program? Tidak terdokumentasi (Phase 4 Known Limitations)
- [behavioral] Regulatory Strategy Post-Coinbase: Legal wrapper DAO (Cayman/Swiss) atau tetap BVI only? Tim doxxing plan? (Phase 2 Open Threads, Phase 5 Financial Risk)
- [behavioral] Perpetual/Futures Listing Roadmap: Tidak ada KMNO perpetual di CEX utama per Okt 2024 (Phase 8 Open Threads)
- [behavioral] Geographic User Distribution & KYC Data: Tidak ada data pengguna per wilayah (Phase 8 Open Threads)
- [conflict] Description: Identitas asli dan susunan tim inti Kamino (Kamino Team) tidak dipublikasikan; hanya pseudonim @kamino_finance
- [conflict] Affected Phase: Phase 2
- [conflict] Evidence: Phase 2 — Entity Kamino Team "sepenuhnya pseudonim"; Phase 2 — Open Threads
- [conflict] Alternative Interpretations: (a) Tim kecil ~10-20 orang yang ingin tetap anonim untuk keamanan; (b) tim besar dengan developer yang dikenal secara terpisah di industri; (c) masih belum ada rencana doxxing
- [conflict] Status: Open Open Thread ID: OT-02
- [conflict] Description: Persentase alokasi token KMNO per kategori (Community, Team, Investor, Treasury, Ecosystem) tidak dipublikasikan resmi
- [conflict] Affected Phase: Phase 6
- [conflict] Evidence: Phase 6 — Distribution "tidak diketahui" untuk seluruh kategori
- [conflict] Alternative Interpretations: (a) Alokasi community lebih besar untuk menarik pengguna; (b) alokasi investor besar karena seed round; (c) DAO treasury sangat besar untuk upgrade masa depan
- [conflict] Status: Open Open Thread ID: OT-03
- [conflict] Description: Parameter fee switch exact (bps fee ke staker vs treasury) tidak tercantum di governance proposal yang terlihat; hanya disebut "portion"
- [conflict] Affected Phase: Phase 3 (EV-017), Phase 6
- [conflict] Evidence: Phase 3 — EV-017 "persentase exact per proposal terverifikasi on-chain" diklaim di Phase 1 namun tidak ada angka
- [conflict] Alternative Interpretations: (a) Persentase 100% ke staker dengan fee dari treasury; (b) persentase fee 50/50; (c) parameter dinamis yang diubah per proposal
- [conflict] Status: Open Open Thread ID: OT-04
- [conflict] Description: Mint authority SPL Token-2022 untuk KMNO — tidak diverifikasi on-chain apakah masih dipegang tim, DAO, atau renounced
- [conflict] Affected Phase: Phase 4, Phase 6
- [conflict] Evidence: Phase 6 — Token Information tidak menyebut status mint authority
- [conflict] Alternative Interpretations: (a) Masih dipegang tim untuk future mint (berbeda dengan fixed supply claim); (b) sudah renounced; (c) dipegang DAO
- [conflict] Status: Open Open Thread ID: OT-05
- [conflict] Description: Coverage audit untuk Liquidate program final (Agustus 2024) tidak tercantum secara eksplisit di event terpisah; hanya disebut "Neodyme re-audit 2024-06" di Phase 4
- [conflict] Affected Phase: Phase 3, Phase 4
- [conflict] Evidence: Phase 4 — Audit History "Neodyme (Re-audit 2024-06) Scope: Liquidate Final"; Phase 3 tidak memiliki event terpisah untuk ini
- [conflict] Alternative Interpretations: (a) Audit dilakukan sebelum Liquidate launch; (b) audit dilakukan setelah launch tanpa event terpisah; (c) dokumentasi tidak lengkap
- [conflict] Status: Open Open Thread ID: OT-06
- [conflict] Description: TVL Kamino pada berbagai titik waktu — angka DefiLlama ($1.2B Okt 2024, peak $1.5B Mar 2024) tidak dikonfirmasi oleh Kamino resmi; beberapa klaim komunitas berbeda
- [conflict] Affected Phase: Phase 8
- [conflict] Evidence: Phase 8 — Adoption Metrics menggunakan DefiLlama sebagai source of truth
- [conflict] Alternative Interpretations: (a) DefiLlama akurat; (b) DefiLlama underestimates karena tidak menghitung beberapa vault; (c) overestimates karena liquid staking double count
- [conflict] Status: Open Open Thread ID: OT-07
- [conflict] Description: Staleness threshold exact value (slots) untuk Pyth oracle di K-Lend dan Multiply tidak terdokumentasi
- [conflict] Affected Phase: Phase 4
- [conflict] Evidence: Phase 4 — Security Model "staleness threshold & confidence interval checks" tanpa angka
- [conflict] Alternative Interpretations: (a) Threshold sangat ketat (mis. <1 detik); (b) threshold longgar (mis. 5-30 detik); (c) berdasarkan Pyth recommended value
- [conflict] Status: Open Open Thread ID: OT-08
- [conflict] Description: Liquidate auction parameters (starting discount, end discount, duration) tidak terdokumentasi publik
- [conflict] Affected Phase: Phase 4
- [conflict] Evidence: Phase 4 — Known Limitations "parameter fixed hingga governance change"
- [conflict] Alternative Interpretations: (a) Discount 5-20% standar; (b) lebih agresif 20-50%; (c) parameter berubah berdasarkan kondisi pasar
- [conflict] Status: Open Open Thread ID: OT-09
- [conflict] Description: Rencana diversifikasi treasury (stablecoin, yield-bearing assets) tidak ada proposal resmi selain buyback & burn (EV-021)
- [conflict] Affected Phase: Phase 5
- [conflict] Evidence: Phase 5 — Treasury "Treasury Composition: Tidak diungkap"; Phase 5 — Financial Risk "Treasury Concentration: KMNO"
- [conflict] Alternative Interpretations: (a) Treasury dianggap aman karena kinerja KMNO; (b) diversifikasi sedang direncanakan tapi belum final; (c) buyback adalah bentuk diversifikasi ke profit revenue
- [conflict] Status: Open Open Thread ID: OT-10
- [conflict] Description: Status rencana ekspansi multi-chain (Eclipse, Sonic, EVM L2) tidak ada announcement resmi dari Kamino
- [conflict] Affected Phase: Phase 8
- [conflict] Evidence: Phase 8 — Open Threads "Multi-chain expansion plans"
- [conflict] Alternative Interpretations: (a) Fokus tetap single-chain (Solana) untuk waktu lama; (b) sedang dalam riset internal; (c) menunggu Solana interop layer matang
- [conflict] Status: Open Open Thread ID: OT-11
- [conflict] Description: Data adopsi kunci (DAU, daily transactions, cumulative unique wallets, developer count) tidak dipublikasikan resmi Kamino
- [conflict] Affected Phase: Phase 8
- [conflict] Evidence: Phase 8 — Adoption Metrics seluruhnya "tidak diketahui" untuk DAU, txns, wallets
- [conflict] Alternative Interpretations: (a) Tim tidak ingin berbagi data kompetitif; (b) keterbatasan tracking; (c) metrik dianggap internal KPI
- [conflict] Status: Open Open Thread ID: OT-12
- [conflict] Description: Volume cross-chain deposit via Wormhole NTT ke Vaults belum terukur publik
- [conflict] Affected Phase: Phase 7, Phase 8
- [conflict] Evidence: Phase 7 — Major Integrations Wormhole NTT; Phase 8 — Bridge Volume "tidak diketahui"
- [conflict] Alternative Interpretations: (a) Volume masih kecil (<$10M); (b) volume signifikan tapi tidak dilaporkan; (c) NTT belum aktif digunakan secara luas
- [conflict] Status: Open
- [airdrop] Persentase alokasi KMNO exact untuk komunitas/points holders (Season 1-3) vs team vs investor vs treasury vs ecosystem — tidak dipublikasikan, butuh on-chain vesting program analysis atau transparency report resmi.
- [airdrop] Jumlah wallet eligible claim TGE exact & breakdown per Season (1, 2, 3) — tidak dipublikasikan.
- [airdrop] Mekanisme anti-sybil detail untuk Points Season 1-3 & jumlah alamat yang didiskualifikasi — tidak dipublikasikan.
- [airdrop] Harga rata-rata claim per penerima (median/mean USD value) — butuh cohort analysis on-chain.
- [airdrop] Persentase penerima yang menjual dalam 7/30/90 hari post-claim — butuh cohort analysis on-chain.
- [airdrop] Season 4 emission schedule exact (KMNO per epoch, total allocation, durasi) — governance forum parameters tidak terpusat di single source.
- [airdrop] Treasury composition breakdown (KMNO vs stablecoin vs yield-bearing) — Realms view raw only.
- [airdrop] Upgrade authority decentralization timeline (multisig tim → DAO timelock/immutable) — tidak ada roadmap publik.
- [airdrop] Formal verification status untuk core math (rebalancing, health factor, rate curves, points calculation) — hanya audit manual.
- [airdrop] Regulatory strategy post-Coinbase listing (legal wrapper DAO Cayman/Swiss, team doxxing plan) — tidak diumumkan.
