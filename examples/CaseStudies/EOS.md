# EOS — Deep Case Study (Phased)

**CIF Dataset — Deep Dossier · Tier: Deep (anchor project)**
**Source:** Deep Research (DeepSeek), Format v3 Dependency Pipeline (10/11 phases: foundation, entity, history, technology, financial, token, ecosystem, market, behavioral, knowledge). **Auto-assembled** by `tools/ingest.py` (deterministic, no LLM, strict data_project/ contract) — each phase extracted and concatenated in dependency order per `docs/Protocol/Deep-Research-Brief.md`; the reasoning is the source reports'.
**Raw sources archived:** doc_backup/deep/EOS_foundation_2026-08.docx, doc_backup/deep/EOS_entity_2026-08.docx, doc_backup/deep/EOS_history_2026-08.docx, doc_backup/deep/EOS_technology_2026-08.docx, doc_backup/deep/EOS_financial_2026-08.docx, doc_backup/deep/EOS_token_2026-08.docx, doc_backup/deep/EOS_ecosystem_2026-08.docx, doc_backup/deep/EOS_market_2026-08.docx, doc_backup/deep/EOS_behavioral_2026-08.docx, doc_backup/deep/EOS_knowledge_2026-08.docx.
**Phases not run:** conflict.

> Faithful concatenation of phase outputs — no fabrication, no distillation beyond what the closing phase (Conflict Resolution / Validation) itself states. Consider a periodic QC pass.

---
## Foundation Intelligence
_ref: `docs/Ontology/Identity.md`, `docs/Ontology/Team.md`_

PROJECT: EOS
Official Name: EOS Network (HIGH) [EOS Network Foundation, https://eosnetwork.com/]
Symbol: EOS (HIGH) [CoinMarketCap, https://coinmarketcap.com/currencies/eos/]
Category: Layer 1 Blockchain / Smart Contract Platform (HIGH) [EOS Network Foundation, https://eosnetwork.com/]
Founding Entity: Block.one (Cayman Islands) — entitas peluncur awal; EOS Network Foundation (ENF, Cayman Islands) — entitas pengelola jaringan saat ini (HIGH) [Block.one Website, https://block.one/; EOS Network Foundation, https://eosnetwork.com/foundation/]
Founders: Brendan Blumer (CEO Block.one); Dan Larimer (CTO Block.one, keluar 2021); Brock Pierce (Co-founder Block.one, keluar awal) (HIGH) [Bloomberg, https://www.bloomberg.com/profile/person/18563544; CoinDesk, https://www.coindesk.com/business/2021/01/11/dan-larimer-leaves-block-one/]
Core Team: EOS Network Foundation (ENF) dipimpin Yves La Rose (CEO ENF) + tim engineering, growth, operations (~30+ orang terverifikasi di halaman tim ENF) (MEDIUM) [EOS Network Foundation Team Page, https://eosnetwork.com/foundation/team/]
Country: Cayman Islands (Block.one & ENF) (HIGH) [Block.one Terms of Use, https://block.one/terms-of-use/; EOS Network Foundation, https://eosnetwork.com/foundation/]
Launch Date - Testnet: 31 Januari 2018 (Dawn 1.0) (HIGH) [Block.one Blog, https://block.one/blog/block-one-releases-dawn-1-0/]
Launch Date - Mainnet: 14 Juni 2018 (HIGH) [CoinDesk, https://www.coindesk.com/markets/2018/06/14/eos-mainnet-launches-after-block-producers-vote/]
Launch Date - TGE: 26 Juni 2017 – 1 Juni 2018 (distribusi token berlangsung 1 tahun via ICO) (HIGH) [EOS Token Distribution Contract, https://github.com/EOSIO/eos/blob/master/contracts/eosio.token/eosio.token.cpp; SEC Complaint vs Block.one, https://www.sec.gov/litigation/complaints/2019/pr2019-197.pdf]
Main Products: EOS Mainnet (Layer 1); EOS EVM (Ethereum-compatible execution environment); Spring SDK (dikenal sebelumnya EOS SDK/CDT); Hyperion History API; EOSIO/Antelope Leap Node Software (HIGH) [EOS Network Foundation Products, https://eosnetwork.com/ecosystem/; GitHub EOS Network Foundation, https://github.com/eosnetworkfoundation]
Official Website: https://eosnetwork.com/ (HIGH)
Repository: https://github.com/eosnetworkfoundation (HIGH)
Documentation: https://developers.eosnetwork.com/ (HIGH)
Social - X/Twitter: @EOSNetwork (HIGH) [X.com, https://x.com/EOSNetwork]
Social - Discord: https://discord.gg/eosnetwork (HIGH) [EOS Network Foundation, https://eosnetwork.com/discord/]
Social - Telegram: @EOSProject (HIGH) [Telegram, https://t.me/EOSProject]
Block Explorer: https://eosq.app/ (resmi ENF); https://bloks.io/ (populer komunitas) (HIGH) [EOS Network Foundation, https://eosnetwork.com/block-explorers/]
Token Contract: eosio.token @ EOS Mainnet (native); 0x86Fa049857E0209aa7D9e616F7eb3b3B78ECfdb0 @ Ethereum (ERC-20 bridge token) (HIGH) [EOS Authority, https://eosauthority.com/contract/eosio.token; Etherscan, https://etherscan.io/token/0x86Fa049857E0209aa7D9e616F7eb3b3B78ECfdb0]
Chain(s): EOS Mainnet (Antelope Protocol); EOS EVM (Layer 2/EVM layer di atas EOS) (HIGH) [EOS Network Foundation, https://eosnetwork.com/ecosystem/eos-evm/]
Ecosystem: DeFi (Defibox, OrganicSwap), GameFi (Ultra, WAX bridge), Social (Voice - ditutup), Infrastructure (Hyperion, Firehose), Tooling (Anchor Wallet, Wombat) (MEDIUM) [EOS Network Foundation Ecosystem Page, https://eosnetwork.com/ecosystem/; DappRadar EOS, https://dappradar.com/rankings/protocol/eos]

## Entity Intelligence
_ref: `docs/Ontology/Relationships.md` (entity graph)_

PROJECT: EOS

Entity: EOS Network Foundation (ENF)
Type: Foundation
Relationship: Entitas pengelola jaringan EOS saat ini yang bertanggung jawab atas pengembangan protokol, pertumbuhan ekosistem, operasi, dan pengelolaan treasury jaringan (HIGH)
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [EOS Network Foundation, https://eosnetwork.com/foundation/]; (HIGH) [CoinDesk, https://www.coindesk.com/business/2021/09/22/eos-community-launches-foundation-to-take-over-from-block-one/]

---
Entity: Block.one
Type: Company
Relationship: Entitas peluncur awal (original launcher) yang mengadakan ICO tahunan 2017–2018, mengembangkan perangkat lunak EOSIO awal, dan menyelesaikan tuntutan SEC 2019 sebesar $24 juta (HIGH)
Period: 2017–2021 (peran aktif), 2021–sekarang (pemegang IP/lisensi)
Exposure Type: technical-integration
Evidence: (HIGH) [SEC Complaint vs Block.one, https://www.sec.gov/litigation/complaints/2019/pr2019-197.pdf]; (HIGH) [Block.one Blog, https://block.one/blog/block-one-releases-dawn-1-0/]; (HIGH) [CoinDesk, https://www.coindesk.com/business/2021/01/11/dan-larimer-leaves-block-one/]

---
Entity: Brendan Blumer
Type: Person
Relationship: CEO Block.one sejak pendirian; tokoh kunci di balik ICO EOS $4+ miliar dan visi awal protokol (HIGH)
Period: 2017–sekarang
Exposure Type: financial-collateral
Evidence: (HIGH) [Bloomberg, https://www.bloomberg.com/profile/person/18563544]; (HIGH) [SEC Complaint vs Block.one, https://www.sec.gov/litigation/complaints/2019/pr2019-197.pdf]

---
Entity: Dan Larimer
Type: Person
Relationship: CTO Block.one dan arsitek utama arsitektur DPoS/EOSIO; keluar dari Block.one Januari 2021 (HIGH)
Period: 2017–2021
Exposure Type: technical-integration
Evidence: (HIGH) [CoinDesk, https://www.coindesk.com/business/2021/01/11/dan-larimer-leaves-block-one/]; (HIGH) [Block.one Blog, https://block.one/blog/block-one-releases-dawn-1-0/]

---
Entity: Brock Pierce
Type: Person
Relationship: Co-founder Block.one; keluar pada tahap awal sebelum peluncuran mainnet (HIGH)
Period: 2017–2018
Exposure Type: financial-collateral
Evidence: (HIGH) [CoinDesk, https://www.coindesk.com/business/2021/01/11/dan-larimer-leaves-block-one/]; (MEDIUM) [Forbes, https://www.forbes.com/sites/rogerhuang/2021/01/11/dan-larimer-leaves-block-one-what-does-it-mean-for-eos/]

---
Entity: Yves La Rose
Type: Person
Relationship: CEO EOS Network Foundation (ENF) memimpin tim engineering, growth, dan operations sejak pembentukan ENF 2021 (HIGH)
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [EOS Network Foundation Team Page, https://eosnetwork.com/foundation/team/]; (HIGH) [CoinDesk, https://www.coindesk.com/business/2021/09/22/eos-community-launches-foundation-to-take-over-from-block-one/]

---
Entity: EOS Network Foundation Core Team
Type: Organization
Relationship: Tim engineering, growth, operations (~30+ orang terverifikasi) yang membangun dan memelihara EOS Mainnet, EOS EVM, Spring SDK, Hyperion, dan infrastruktur terkait (MEDIUM)
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [EOS Network Foundation Team Page, https://eosnetwork.com/foundation/team/]; (MEDIUM) [GitHub EOS Network Foundation, https://github.com/eosnetworkfoundation]

---
Entity: U.S. Securities and Exchange Commission (SEC)
Type: Government
Relationship: Regulator yang menuntut Block.one atas penjualan token EOS tidak terdaftar; menyelesaikan kasus September 2019 dengan denda $24 juta tanpa mengakui atau menolak tuduhan (HIGH)
Period: 2019 (penyelesaian)
Exposure Type: unknown
Evidence: (HIGH) [SEC Press Release, https://www.sec.gov/news/press-release/2019-197]; (HIGH) [SEC Complaint vs Block.one, https://www.sec.gov/litigation/complaints/2019/pr2019-197.pdf]

---
Entity: Antelope Protocol (Leap Node Software)
Type: Protocol
Relationship: Protokol konsensus dan perangkat lunak node (Leap) yang menjadi dasar EOS Mainnet; dikembangkan kolaboratif oleh ENF dan kontributor komunitas (HIGH)
Period: 2021–sekarang (sebagai Antelope), 2018–2021 (sebagai EOSIO)
Exposure Type: technical-integration
Evidence: (HIGH) [GitHub AntelopeIO/leap, https://github.com/AntelopeIO/leap]; (HIGH) [EOS Network Foundation, https://eosnetwork.com/ecosystem/]

---
Entity: EOS Mainnet
Type: Chain
Relationship: Layer 1 blockchain utama yang menggunakan protokol Antelope/DPoS; diluncurkan 14 Juni 2018 oleh Block Producers terpilih (HIGH)
Period: 2018–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [CoinDesk, https://www.coindesk.com/markets/2018/06/14/eos-mainnet-launches-after-block-producers-vote/]; (HIGH) [EOS Network Foundation, https://eosnetwork.com/]

---
Entity: EOS EVM
Type: Protocol
Relationship: Lingkungan eksekusi kompatibel Ethereum (EVM) yang berjalan di atas EOS Mainnet; memungkinkan deployment kontrak Solidity/Vyper asli (HIGH)
Period: 2022–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [EOS Network Foundation EOS EVM, https://eosnetwork.com/ecosystem/eos-evm/]; (HIGH) [GitHub eosnetworkfoundation/eos-evm, https://github.com/eosnetworkfoundation/eos-evm]

---
Entity: Spring SDK (f.k.a. EOS SDK/CDT)
Type: Application
Relationship: Toolkit pengembang (SDK) untuk membangun smart contract dan dApp di ekosistem EOS/Antelope; dikelola ENF (HIGH)
Period: 2018–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [EOS Network Foundation Products, https://eosnetwork.com/ecosystem/]; (HIGH) [GitHub eosnetworkfoundation/spring, https://github.com/eosnetworkfoundation/spring]

---
Entity: Hyperion History API
Type: Infrastructure Provider
Relationship: Layanan API sejarah/indeks data on-chain EOS yang dipakai eksplorator, wallet, dan dApp untuk query data historis (HIGH)
Period: 2019–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [EOS Network Foundation Ecosystem, https://eosnetwork.com/ecosystem/]; (HIGH) [GitHub eosrio/hyperion, https://github.com/eosrio/hyperion]

---
Entity: Firehose (StreamingFast)
Type: Infrastructure Provider
Relationship: Layanan streaming data blok real-time dan indeks terstruktur untuk EOS/Antelope; digunakan pengembang untuk sinkronisasi cepat (MEDIUM)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [StreamingFast Firehose, https://streamingfast.io/firehose]; (MEDIUM) [EOS Network Foundation Ecosystem, https://eosnetwork.com/ecosystem/]

---
Entity: Defibox
Type: Application
Relationship: Protokol DeFi terbesar di EOS (DEX AMM, lending, stablecoin USN); TVL historis paling tinggi ekosistem (MEDIUM)
Period: 2020–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [DappRadar EOS, https://dappradar.com/rankings/protocol/eos]; (MEDIUM) [Defibox Official, https://defibox.com/]

---
Entity: OrganicSwap
Type: Application
Relationship: DEX AMM berbasis EOS dengan fokus pairing stablecoin dan token ekosistem; kontributor likuiditas DeFi (MEDIUM)
Period: 2021–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [DappRadar EOS, https://dappradar.com/rankings/protocol/eos]; (MEDIUM) [OrganicSwap, https://organicswap.io/]

---
Entity: Ultra
Type: Application
Relationship: Platform GameFi/penerbitan game berbasis blockchain; menggunakan teknologi EOS/Antelope dan menjembatani ke WAX (MEDIUM)
Period: 2019–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Ultra.io, https://ultra.io/]; (MEDIUM) [EOS Network Foundation Ecosystem, https://eosnetwork.com/ecosystem/]

---
Entity: WAX (Worldwide Asset eXchange)
Type: Chain
Relationship: Blockchain berjenis Antelope yang berfokus NFT/GameFi; memiliki bridge dan interoperabilitas dengan EOS Mainnet (MEDIUM)
Period: 2019–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [WAX Official, https://wax.io/]; (MEDIUM) [EOS Network Foundation Ecosystem, https://eosnetwork.com/ecosystem/]

---
Entity: Voice
Type: Application
Relationship: Platform media sosial berbasis blockchain yang dibangun Block.one di atas EOS; ditutup 2021 (HIGH)
Period: 2020–2021
Exposure Type: technical-integration
Evidence: (HIGH) [CoinDesk, https://www.coindesk.com/business/2021/02/10/block-one-shuts-down-voice-social-media-platform/]; (HIGH) [Block.one Blog, https://block.one/blog/voice-launches-beta/]

---
Entity: Anchor Wallet
Type: Application
Relationship: Wallet non-custodial populer untuk ekosistem Antelope (EOS, WAX, Telos, dll); mendukung signing, resource management, dan dApp browser (HIGH)
Period: 2019–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Anchor Wallet, https://greymass.com/anchor]; (HIGH) [EOS Network Foundation Ecosystem, https://eosnetwork.com/ecosystem/]

---
Entity: Wombat Wallet
Type: Application
Relationship: Wallet mobile/web non-custodial untuk EOS dan chain Antelope lain; terintegrasi dApp store dan NFT gallery (MEDIUM)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Wombat Wallet, https://wombat.app/]; (MEDIUM) [EOS Network Foundation Ecosystem, https://eosnetwork.com/ecosystem/]

---
Entity: EOS Authority
Type: Infrastructure Provider
Relationship: Penyedia block explorer resmi ENF (eosq.app), tooling voting BP, dan analisis on-chain; entitas komunitas independen (HIGH)
Period: 2018–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [EOS Authority, https://eosauthority.com/]; (HIGH) [EOS Network Foundation Block Explorers, https://eosnetwork.com/block-explorers/]

---
Entity: Bloks.io
Type: Infrastructure Provider
Relationship: Block explorer populer komunitas untuk EOS dan chain Antelope lain; dikembangkan oleh HiveBP/EOS Cafe Block (MEDIUM)
Period: 2018–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Bloks.io, https://bloks.io/]; (MEDIUM) [EOS Network Foundation Block Explorers, https://eosnetwork.com/block-explorers/]

---
Entity: Etherscan
Type: Infrastructure Provider
Relationship: Block explorer Ethereum yang menampilkan kontrak token EOS ERC-20 bridge (0x86Fa049857E0209aa7D9e616F7eb3b3B78ECfdb0) (HIGH)
Period: 2017–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Etherscan EOS Token, https://etherscan.io/token/0x86Fa049857E0209aa7D9e616F7eb3b3B78ECfdb0]

---
Entity: DappRadar
Type: Media
Relationship: Platform analitik dApp yang melacak ranking protokol, TVL, dan aktivitas pengguna di ekosistem EOS (MEDIUM)
Period: 2019–sekarang
Exposure Type: narrative-correlated-only
Evidence: (MEDIUM) [DappRadar EOS Rankings, https://dappradar.com/rankings/protocol/eos]

---
Entity: CoinMarketCap
Type: Media
Relationship: Penyedia data harga, market cap, dan volume trading token EOS; referensi pasar standar industri (HIGH)
Period: 2017–sekarang
Exposure Type: narrative-correlated-only
Evidence: (HIGH) [CoinMarketCap EOS, https://coinmarketcap.com/currencies/eos/]

---
Entity: CoinDesk
Type: Media
Relationship: Media berita industri crypto yang meliput peluncuran mainnet, pembentukan ENF, keluarnya Dan Larimer, dan penutupan Voice (HIGH)
Period: 2018–sekarang
Exposure Type: narrative-correlated-only
Evidence: (HIGH) [CoinDesk EOS Tag, https://www.coindesk.com/tag/eos/]

---
Entity: Bloomberg
Type: Media
Relationship: Media bisnis global yang memprofil Brendan Blumer dan meliput perkembangan Block.one/EOS (MEDIUM)
Period: 2018–sekarang
Exposure Type: narrative-correlated-only
Evidence: (MEDIUM) [Bloomberg Brendan Blumer Profile, https://www.bloomberg.com/profile/person/18563544]

---
Entity: GitHub (Microsoft)
Type: Company
Relationship: Platform hosting repositori resmi kode EOS/Antelope (github.com/eosnetworkfoundation, github.com/AntelopeIO) (HIGH)
Period: 2017–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [GitHub EOS Network Foundation, https://github.com/eosnetworkfoundation]; (HIGH) [GitHub AntelopeIO, https://github.com/AntelopeIO]

---
Entity: Cayman Islands Jurisdiction
Type: Government
Relationship: Yurisdiksi inkorporasi Block.one dan EOS Network Foundation; kerangka hukum operasi entitas (HIGH)
Period: 2017–sekarang
Exposure Type: unknown
Evidence: (HIGH) [Block.one Terms of Use, https://block.one/terms-of-use/]; (HIGH) [EOS Network Foundation, https://eosnetwork.com/foundation/]

---
Entity: Block Producers (BP) Collective
Type: Organization
Relationship: 21 Block Producer aktif + cadangan yang divoting pemegang token; memproduksi blok, memvalidasi transaksi, dan menerima inflasi 1% tahunan (HIGH)
Period: 2018–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [EOS Authority Block Producers, https://eosauthority.com/block-producers]; (HIGH) [EOS Network Foundation, https://eosnetwork.com/]

---
Entity: eosio.token Contract
Type: Protocol
Relationship: Kontrak sistem native yang mengelola supply token EOS, transfer, dan aksi terkait token di mainnet (HIGH)
Period: 2018–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [EOS Authority Contract, https://eosauthority.com/contract/eosio.token]; (HIGH) [GitHub EOSIO eosio.token, https://github.com/EOSIO/eos/blob/master/contracts/eosio.token/eosio.token.cpp]

---
Entity: eosio.system Contract
Type: Protocol
Relationship: Kontrak sistem yang mengelola staking, voting BP, alokasi inflasi (1% BP, 1% ENF, dst), RAM market, dan resource management (HIGH)
Period: 2018–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [EOS Authority Contract, https://eosauthority.com/contract/eosio.system]; (HIGH) [GitHub EOSIO eosio.system, https://github.com/EOSIO/eos/blob/master/contracts/eosio.system/eosio.system.cpp]

---
Entity: EOS Network Foundation Discord Community
Type: Community Organization
Relationship: Server Discord resmi komunitas EOS untuk diskusi pengembang, pemegang token, dan kontributor (~50k+ member) (MEDIUM)
Period: 2021–sekarang
Exposure Type: narrative-correlated-only
Evidence: (MEDIUM) [EOS Network Foundation Discord, https://discord.gg/eosnetwork]

---
Entity: EOS Project Telegram
Type: Community Organization
Relationship: Grup Telegram resmi komunitas EOS untuk announcements dan diskusi umum (MEDIUM)
Period: 2017–sekarang
Exposure Type: narrative-correlated-only
Evidence: (MEDIUM) [Telegram EOSProject, https://t.me/EOSProject]

---
Entity: EOS X/Twitter Account (@EOSNetwork)
Type: Media
Relationship: Akun media sosial resmi ENF untuk pengumuman rilis, upgrade jaringan, dan kampanye ekosistem (HIGH)
Period: 2021–sekarang
Exposure Type: narrative-correlated-only
Evidence: (HIGH) [X.com EOSNetwork, https://x.com/EOSNetwork]

### PERSON
- Brendan Blumer
- Dan Larimer
- Brock Pierce
- Yves La Rose

### FOUNDATION
- EOS Network Foundation (ENF)

### COMPANY
- Block.one
- GitHub (Microsoft)
- StreamingFast (Firehose provider)

### PROTOCOL
- Antelope Protocol (Leap Node Software)
- EOS EVM
- eosio.token Contract
- eosio.system Contract

### CHAIN
- EOS Mainnet
- WAX (Worldwide Asset eXchange)

### INVESTOR
- (Tidak teridentifikasi investor/VC spesifik dari Phase 1; ICO bersifat publik permissionless)

### INFRASTRUCTURE
- Hyperion History API
- Firehose (StreamingFast)
- EOS Authority
- Bloks.io
- Etherscan
- Anchor Wallet
- Wombat Wallet

### APPLICATION
- Spring SDK (f.k.a. EOS SDK/CDT)
- Defibox
- OrganicSwap
- Ultra
- Voice

### SECURITY
- (Tidak teridentifikasi auditor/firma keamanan spesifik dari Phase 1)

### DAO
- Block Producers (BP) Collective

### GOVERNMENT
- U.S. Securities and Exchange Commission (SEC)
- Cayman Islands Jurisdiction

### MEDIA
- CoinMarketCap
- CoinDesk
- Bloomberg
- DappRadar
- EOS X/Twitter Account (@EOSNetwork)

### COMMUNITY
- EOS Network Foundation Discord Community
- EOS Project Telegram

### OTHER
- EOS Network Foundation Core Team

---

**SUMMARY**

Total Entity: 38
Internal: 12 (ENF, Block.one, Core Team, Founders, BP Collective, EOS Mainnet, EOS EVM, Spring SDK, eosio.token, eosio.system, Antelope Protocol, Voice)
External: 26 (SEC, Cayman Islands, GitHub, Media x5, Community x2, Infrastructure x7, DeFi/App x4, WAX, Ultra, Investors none identified)
Unknown: 0

---

## Historical Intelligence
_ref: `docs/Ontology/DecisionEvent.md` (factual spine — enriched later by Behavioral)_

PROJECT: EOS

Event ID

EV-001

Date

2017-05-01

Event Name

Pendirian Block.one

Event Type

Founding

Description

Block.one didirikan sebagai perusahaan teknologi blockchain di Cayman Islands oleh Brendan Blumer, Dan Larimer, dan Brock Pierce untuk mengembangkan protokol EOSIO dan mengadakan distribusi token EOS.

Participants

Block.one; Brendan Blumer; Dan Larimer; Brock Pierce

Location

Cayman Islands

Status

Completed

Immediate Result

Entitas legal Block.one terbentuk untuk memulai pengembangan EOSIO dan persiapan ICO token EOS.

Sources

https://block.one/terms-of-use/

https://www.bloomberg.com/profile/person/18563544

---

Event ID

EV-002

Date

2017-06-26

Event Name

Mulai Distribusi Token EOS (ICO Tahap 1)

Event Type

Token

Description

Block.one memulai distribusi token EOS melalui smart contract di Ethereum mainnet; periode distribusi berlangsung 341 hari hingga 1 Juni 2018 dengan total 1 miliar token dialokasikan.

Participants

Block.one; eosio.token Contract (Ethereum)

Location

Ethereum Mainnet

Status

Completed

Immediate Result

Token EOS ERC-20 mulai didistribusikan ke peserta ICO; kontrak distribusi terkunci di blockchain Ethereum.

Sources

https://github.com/EOSIO/eos/blob/master/contracts/eosio.token/eosio.token.cpp

https://www.sec.gov/litigation/complaints/2019/pr2019-197.pdf

---

Event ID

EV-003

Date

2017-10-01

Event Name

Rilis Whitepaper EOSIO Technical

Event Type

Technology

Description

Block.one mempublikasikan whitepaper teknis EOSIO yang mendeskripsikan arsitektur Delegated Proof of Stake (DPoS), paralelisme eksekusi, dan model resource (CPU, NET, RAM).

Participants

Block.one; Dan Larimer

Location

https://github.com/EOSIO/Documentation/blob/master/TechnicalWhitePaper.md

Status

Completed

Immediate Result

Spesifikasi teknis protokol EOSIO tersedia publik untuk review komunitas dan pengembang.

Sources

https://github.com/EOSIO/Documentation/blob/master/TechnicalWhitePaper.md

---

Event ID

EV-004

Date

2018-01-31

Event Name

Rilis Dawn 1.0 (Testnet Pertama)

Event Type

Launch

Description

Block.one merilis Dawn 1.0 sebagai implementasi testnet pertama perangkat lunak EOSIO; memvalidasi arsitektur DPoS dan konsensus BFT-DPoS di lingkungan live.

Participants

Block.one

Location

https://block.one/blog/block-one-releases-dawn-1-0/

Status

Completed

Immediate Result

Testnet pertama EOSIO beroperasi; pengembang mulai mencoba smart contract dan arsitektur resource.

Sources

https://block.one/blog/block-one-releases-dawn-1-0/

---

Event ID

EV-005

Date

2018-03-01

Event Name

Rilis Dawn 2.0

Event Type

Technology

Description

Block.one merilis Dawn 2.0 dengan perbaikan performa, API RPC, dan dukungan multi-threading untuk eksekusi transaksi paralel.

Participants

Block.one

Location

https://block.one/blog/block-one-releases-dawn-2-0/

Status

Completed

Immediate Result

Testnet versi kedua dengan stabilitas dan fitur pengembang yang ditingkatkan.

Sources

https://block.one/blog/block-one-releases-dawn-2-0/

---

Event ID

EV-006

Date

2018-04-01

Event Name

Rilis Dawn 3.0

Event Type

Technology

Description

Dawn 3.0 memperkenalkan sistem akun berbasis nama manusia (readable account names), perbaikan voting BP, dan manajemen resource RAM.

Participants

Block.one

Location

https://block.one/blog/block-one-releases-dawn-3-0/

Status

Completed

Immediate Result

Model akun dan resource yang akan digunakan mainnet mulai matang.

Sources

https://block.one/blog/block-one-releases-dawn-3-0/

---

Event ID

EV-007

Date

2018-05-01

Event Name

Rilis Dawn 4.0 (Release Candidate)

Event Type

Technology

Description

Dawn 4.0 sebagai release candidate untuk mainnet; mencakup finalisasi konsensus, sistem voting 21 BP, dan parameter inflasi token.

Participants

Block.one

Location

https://block.one/blog/block-one-releases-dawn-4-0/

Status

Completed

Immediate Result

Kode siap produksi untuk peluncuran mainnet oleh Block Producers terpilih.

Sources

https://block.one/blog/block-one-releases-dawn-4-0/

---

Event ID

EV-008

Date

2018-06-01

Event Name

Berakhirnya Periode Distribusi Token EOS (ICO)

Event Type

Token

Description

Periode distribusi token EOS berlangsung 341 hari secara resmi berakhir; total 1 miliar token EOS telah didistribusikan ke peserta ICO melalui kontrak Ethereum.

Participants

Block.one; eosio.token Contract (Ethereum)

Location

Ethereum Mainnet

Status

Completed

Immediate Result

Supply awal token EOS ERC-20 finalisasi; persiapan snapshot untuk genesis mainnet.

Sources

https://www.sec.gov/litigation/complaints/2019/pr2019-197.pdf

https://github.com/EOSIO/eos/blob/master/contracts/eosio.token/eosio.token.cpp

---

Event ID

EV-009

Date

2018-06-14

Event Name

Peluncuran EOS Mainnet

Event Type

Launch

Description

Jaringan EOS Mainnet secara resmi diluncurkan setelah 21 Block Producer terpilih menghasilkan blok genesis; Block.one menyerahkan kode sumber ke komunitas.

Participants

Block.one; Block Producers (BP) Collective; EOS Mainnet

Location

https://www.coindesk.com/markets/2018/06/14/eos-mainnet-launches-after-block-producers-vote/

Status

Completed

Immediate Result

EOS Mainnet live dengan 21 BP aktif; token EOS native migrasi dari ERC-20 ke mainnet via snapshot.

Sources

https://www.coindesk.com/markets/2018/06/14/eos-mainnet-launches-after-block-producers-vote/

https://eosnetwork.com/

---

Event ID

EV-010

Date

2018-06-15

Event Name

Aktivasi Sistem Voting BP dan Inflasi

Event Type

Governance

Description

Kontrak eosio.system diaktifkan; pemegang token mulai voting Block Producer, staking CPU/NET, dan membeli RAM; inflasi 5% tahunan mulai dialokasikan (1% BP, 4% savings/disburn nanti).

Participants

Block Producers (BP) Collective; eosio.system Contract; EOS Mainnet

Location

EOS Mainnet

Status

Completed

Immediate Result

Mekanisme governance on-chain berfungsi; BP mulai menerima reward inflasi 1%.

Sources

https://github.com/EOSIO/eos/blob/master/contracts/eosio.system/eosio.system.cpp

https://eosauthority.com/contract/eosio.system

---

Event ID

EV-011

Date

2018-11-01

Event Name

Rilis EOSIO 1.0 (Versi Produksi Pertama)

Event Type

Technology

Description

Block.one merilis EOSIO 1.0 sebagai versi stabil pertama untuk deployment produksi; termasuk hardening keamanan dan optimisasi WASM runtime.

Participants

Block.one

Location

https://github.com/EOSIO/eos/releases/tag/v1.0.0

Status

Completed

Immediate Result

Standar perangkat lunak node untuk BP dan pengembang ekosistem.

Sources

https://github.com/EOSIO/eos/releases/tag/v1.0.0

---

Event ID

EV-012

Date

2019-02-01

Event Name

Peluncuran Voice (Beta) oleh Block.one

Event Type

Product

Description

Block.one meluncurkan platform media sosial Voice di atas EOS Mainnet dengan model tokenisasi perhatian dan verifikasi identitas KYC.

Participants

Block.one; Voice; EOS Mainnet

Location

https://block.one/blog/voice-launches-beta/

Status

Cancelled

Immediate Result

Voice beta live; namun adopsi rendah dan biaya operasional tinggi.

Sources

https://block.one/blog/voice-launches-beta/

---

Event ID

EV-013

Date

2019-09-30

Event Name

Penyelesaian Kasus SEC vs Block.one

Event Type

Legal

Description

SEC menyelesaikan tuntutan terhadap Block.one atas penjualan token EOS tidak terdaftar; Block.one membayar denda $24 juta tanpa mengakui atau menolak tuduhan.

Participants

U.S. Securities and Exchange Commission (SEC); Block.one

Location

https://www.sec.gov/news/press-release/2019-197

Status

Completed

Immediate Result

Kecamasan hukum federal AS atas ICO EOS terselesaikan; Block.one melanjutkan operasional.

Sources

https://www.sec.gov/news/press-release/2019-197

https://www.sec.gov/litigation/complaints/2019/pr2019-197.pdf

---

Event ID

EV-014

Date

2020-02-10

Event Name

Penutupan Platform Voice

Event Type

Product

Description

Block.one resmi menutup platform Voice setelah kurang dari satu tahun operasi; aset dan tim dialihkan ke proyek lain.

Participants

Block.one; Voice

Location

https://www.coindesk.com/business/2021/02/10/block-one-shuts-down-voice-social-media-platform/

Status

Completed

Immediate Result

Voice dihentikan; komunitas EOS kehilangan aplikasi flagship Block.one.

Sources

https://www.coindesk.com/business/2021/02/10/block-one-shuts-down-voice-social-media-platform/

---

Event ID

EV-015

Date

2021-01-11

Event Name

Dan Larimer Keluar dari Block.one

Event Type

Organization

Description

Dan Larimer (CTO dan arsitek EOSIO) mengumumkan keluar dari Block.one untuk mengejar proyek pribadi; mengakhiri peran teknis langsungnya di protokol.

Participants

Dan Larimer; Block.one

Location

https://www.coindesk.com/business/2021/01/11/dan-larimer-leaves-block-one/

Status

Completed

Immediate Result

Kepemimpinan teknis Block.one beralih; komunitas mulai mendorong mandiri pengembangan protokol.

Sources

https://www.coindesk.com/business/2021/01/11/dan-larimer-leaves-block-one/

---

Event ID

EV-016

Date

2021-03-01

Event Name

Rebranding EOSIO Menjadi Antelope Protocol

Event Type

Technology

Description

Komunitas dan kontributor utama memutuskan rebranding perangkat lunak node dari "EOSIO" ke "Antelope" untuk memisahkan identitas protokol dari Block.one; repositori dipindah ke AntelopeIO.

Participants

EOS Network Foundation Core Team; Block Producers (BP) Collective; Antelope Protocol (Leap Node Software)

Location

https://github.com/AntelopeIO/leap

Status

Completed

Immediate Result

Protokol bersifat netral vendor; fondasi untuk governance komunitas mandiri.

Sources

https://github.com/AntelopeIO/leap

---

Event ID

EV-017

Date

2021-09-22

Event Name

Pembentukan EOS Network Foundation (ENF)

Event Type

Foundation

Description

Komunitas EOS meluncurkan EOS Network Foundation (ENF) sebagai entitas non-profit di Cayman Islands untuk mengelola pengembangan protokol, pertumbuhan ekosistem, dan treasury jaringan.

Participants

EOS Network Foundation (ENF); Yves La Rose; Block Producers (BP) Collective

Location

https://www.coindesk.com/business/2021/09/22/eos-community-launches-foundation-to-take-over-from-block-one/

Status

Completed

Immediate Result

ENF menjadi entitas pengelola resmi jaringan EOS; menerima alokasi inflasi 1% tahunan dari eosio.system.

Sources

https://www.coindesk.com/business/2021/09/22/eos-community-launches-foundation-to-take-over-from-block-one/

https://eosnetwork.com/foundation/

---

Event ID

EV-018

Date

2021-10-01

Event Name

Rilis Antelope Leap 3.1 (Versi Mayor Pertama Pasca-ENF)

Event Type

Technology

Description

ENF merilis Antelope Leap 3.1 dengan perbaikan performa, keamanan, dan kompatibilitas tooling; versi ini menjadi baseline node software untuk BP.

Participants

EOS Network Foundation Core Team; Antelope Protocol (Leap Node Software)

Location

https://github.com/AntelopeIO/leap/releases/tag/v3.1.0

Status

Completed

Immediate Result

Node software standar baru diadopsi BP; pengembangan dilanjutkan oleh ENF dan kontributor komunitas.

Sources

https://github.com/AntelopeIO/leap/releases/tag/v3.1.0

---

Event ID

EV-019

Date

2022-04-01

Event Name

Peluncuran EOS EVM Mainnet

Event Type

Launch

Description

ENF meluncurkan EOS EVM — lingkungan eksekusi kompatibel Ethereum (EVM) yang berjalan di atas EOS Mainnet — memungkinkan deployment kontrak Solidity/Vyper asli.

Participants

EOS Network Foundation Core Team; EOS EVM; EOS Mainnet

Location

https://eosnetwork.com/ecosystem/eos-evm/

Status

Completed

Immediate Result

Pengembang Ethereum dapat memigrasikan dApp ke EOS dengan perubahan minimal; interoperabilitas ERC-20 native.

Sources

https://eosnetwork.com/ecosystem/eos-evm/

https://github.com/eosnetworkfoundation/eos-evm

---

Event ID

EV-020

Date

2022-06-14

Event Name

Upgrade Hard Fork "Spring" / EOSIO 3.0 / Leap 4.0

Event Type

Technology

Description

Hard fork terkoordinasi oleh BP dan ENF mengaktifkan fitur Spring SDK, perbaikan RAM market, dan peningkatan throughput; versi node naik ke Leap 4.0.

Participants

Block Producers (BP) Collective; EOS Network Foundation Core Team; Antelope Protocol (Leap Node Software)

Location

https://github.com/AntelopeIO/leap/releases/tag/v4.0.0

Status

Completed

Immediate Result

Protokol diperbarui dengan SDK modern (Spring) dan ekonomi RAM yang direvisi.

Sources

https://github.com/AntelopeIO/leap/releases/tag/v4.0.0

https://eosnetwork.com/ecosystem/

---

Event ID

EV-021

Date

2022-09-01

Event Name

Rilis Spring SDK (f.k.a. EOS SDK/CDT)

Event Type

Product

Description

ENF merilis Spring SDK sebagai toolkit pengembang baru untuk smart contract C++ di Antelope; menggantikan CDT lama dengan ergonomi modern dan tooling terintegrasi.

Participants

EOS Network Foundation Core Team; Spring SDK (f.k.a. EOS SDK/CDT)

Location

https://github.com/eosnetworkfoundation/spring

Status

Completed

Immediate Result

Pengalaman pengembang (DX) ditingkatkan; dukungan C++20, CMake, dan testing framework bawaan.

Sources

https://github.com/eosnetworkfoundation/spring

https://eosnetwork.com/ecosystem/

---

Event ID

EV-022

Date

2023-03-01

Event Name

Integrasi Hyperion History API ke Infrastruktur Resmi ENF

Event Type

Infrastructure

Description

ENF mengadopsi Hyperion History API (dikembangkan EOS Rio) sebagai layanan indeks data sejarah standar untuk eksplorator, wallet, dan dApp ekosistem.

Participants

EOS Network Foundation Core Team; Hyperion History API

Location

https://github.com/eosrio/hyperion

Status

Completed

Immediate Result

Ketersediaan data on-chain historis andal untuk seluruh ekosistem.

Sources

https://github.com/eosrio/hyperion

https://eosnetwork.com/ecosystem/

---

Event ID

EV-023

Date

2023-06-14

Event Name

Perayaan Tahun Ke-5 Mainnet & Kampanye "EOS Hot Sauce"

Event Type

Community

Description

ENF dan komunitas merayakan ulang tahun ke-5 mainnet dengan kampanye pertumbuhan ekosistem, hackathon, dan insentif likuiditas DeFi.

Participants

EOS Network Foundation (ENF); EOS Network Foundation Discord Community; EOS Project Telegram

Location

https://eosnetwork.com/

Status

Completed

Immediate Result

Aktivitas on-chain dan partisipasi komunitas meningkat signifikan selama periode kampanye.

Sources

https://eosnetwork.com/

https://discord.gg/eosnetwork

---

Event ID

EV-024

Date

2023-09-01

Event Name

Peluncuran Program "EOS Network Ventures" / Ecosystem Fund

Event Type

Funding

Description

ENF meluncurkan dana ekosistem untuk investasi strategis ke proyek DeFi, GameFi, dan infrastruktur di atas EOS/EOS EVM; ukuran dana tidak dipublikasikan detailnya.

Participants

EOS Network Foundation (ENF)

Location

https://eosnetwork.com/foundation/

Status

Ongoing

Immediate Result

Pendanaan awal untuk startup ekosistem; portofolio investasi mulai terbentuk.

Sources

https://eosnetwork.com/foundation/

---

Event ID

EV-025

Date

2024-01-01

Event Name

Rilis Antelope Leap 5.0 (Performa & Keamanan)

Event Type

Technology

Description

Leap 5.0 membawa peningkatan throughput signifikan, perbaikan konsensus BFT-DPoS, dan mitigasi vektor serangan resource exhaustion.

Participants

EOS Network Foundation Core Team; Antelope Protocol (Leap Node Software); Block Producers (BP) Collective

Location

https://github.com/AntelopeIO/leap/releases/tag/v5.0.0

Status

Completed

Immediate Result

BP mengupgrade node; jaringan lebih stabil di bawah beban tinggi.

Sources

https://github.com/AntelopeIO/leap/releases/tag/v5.0.0

---

Event ID

EV-026

Date

2024-03-01

Event Name

Integrasi Firehose (StreamingFast) sebagai Standar Indexing Real-time

Event Type

Infrastructure

Description

ENF merekomendasikan Firehose oleh StreamingFast sebagai solusi streaming data blok real-time standar untuk pengembang dApp dan analytics.

Participants

EOS Network Foundation Core Team; Firehose (StreamingFast)

Location

https://streamingfast.io/firehose

Status

Completed

Immediate Result

Pengembang mengakses data blok terstruktur dengan latensi sub-sekon.

Sources

https://streamingfast.io/firehose

https://eosnetwork.com/ecosystem/

---

Event ID

EV-027

Date

2024-06-14

Event Name

Perayaan Tahun Ke-6 Mainnet & Rilis Roadmap 2024-2025

Event Type

Community

Description

ENF mempublikasikan roadmap teknis 2024-2025 mencakup: scaling horizontal (sidechain), zero-knowledge integration, dan perbaikan UX onboarding.

Participants

EOS Network Foundation (ENF); Yves La Rose

Location

https://eosnetwork.com/

Status

Completed

Immediate Result

Visibelnya arah teknis jangka menengah kepada komunitas dan investor.

Sources

https://eosnetwork.com/

---

Event ID

EV-028

Date

2024-09-01

Event Name

Migrasi Token Bridge EOS ERC-20 ke Smart Contract Baru (Jika Terjadi)

Event Type

Technology

Description

Pembaruan kontrak bridge token EOS di Ethereum (0x86Fa049857E0209aa7D9e616F7eb3b3B78ECfdb0) untuk keamanan dan efisiensi gas; detail migrasi belum diverifikasi publik penuh.

Participants

EOS Network Foundation Core Team; eosio.token Contract; Etherscan

Location

https://etherscan.io/token/0x86Fa049857E0209aa7D9e616F7eb3b3B78ECfdb0

Status

Unknown

Immediate Result

Tidak diketahui (belum ada announcement resmi terverifikasi)

Sources

https://etherscan.io/token/0x86Fa049857E0209aa7D9e616F7eb3b3B78ECfdb0

---

Event ID

EV-029

Date

2024-12-01

Event Name

Rilis Antelope Leap 6.0 (Rencana)

Event Type

Technology

Description

Rencana rilis Leap 6.0 dengan dukungan eksperimental untuk ZK-SNARK verification on-chain dan peningkatan parallel execution engine.

Participants

EOS Network Foundation Core Team; Antelope Protocol (Leap Node Software)

Location

https://github.com/AntelopeIO/leap

Status

Ongoing

Immediate Result

Pengembangan di cabang main repositori; belum dirilis stabil.

Sources

https://github.com/AntelopeIO/leap

---

### KELOMPOKKAN BERDASARKAN TAHUN

#### 2017
- EV-001: Pendirian Block.one (Founding)
- EV-002: Mulai Distribusi Token EOS (ICO Tahap 1) (Token)
- EV-003: Rilis Whitepaper EOSIO Technical (Technology)

#### 2018
- EV-004: Rilis Dawn 1.0 (Testnet Pertama) (Launch)
- EV-005: Rilis Dawn 2.0 (Technology)
- EV-006: Rilis Dawn 3.0 (Technology)
- EV-007: Rilis Dawn 4.0 (Release Candidate) (Technology)
- EV-008: Berakhirnya Periode Distribusi Token EOS (ICO) (Token)
- EV-009: Peluncuran EOS Mainnet (Launch)
- EV-010: Aktivasi Sistem Voting BP dan Inflasi (Governance)
- EV-011: Rilis EOSIO 1.0 (Versi Produksi Pertama) (Technology)

#### 2019
- EV-012: Peluncuran Voice (Beta) oleh Block.one (Product)
- EV-013: Penyelesaian Kasus SEC vs Block.one (Legal)

#### 2020
- EV-014: Penutupan Platform Voice (Product)

#### 2021
- EV-015: Dan Larimer Keluar dari Block.one (Organization)
- EV-016: Rebranding EOSIO Menjadi Antelope Protocol (Technology)
- EV-017: Pembentukan EOS Network Foundation (ENF) (Foundation)
- EV-018: Rilis Antelope Leap 3.1 (Versi Mayor Pertama Pasca-ENF) (Technology)

#### 2022
- EV-019: Peluncuran EOS EVM Mainnet (Launch)
- EV-020: Upgrade Hard Fork "Spring" / EOSIO 3.0 / Leap 4.0 (Technology)
- EV-021: Rilis Spring SDK (f.k.a. EOS SDK/CDT) (Product)

#### 2023
- EV-022: Integrasi Hyperion History API ke Infrastruktur Resmi ENF (Infrastructure)
- EV-023: Perayaan Tahun Ke-5 Mainnet & Kampanye "EOS Hot Sauce" (Community)
- EV-024: Peluncuran Program "EOS Network Ventures" / Ecosystem Fund (Funding)

#### 2024
- EV-025: Rilis Antelope Leap 5.0 (Performa & Keamanan) (Technology)
- EV-026: Integrasi Firehose (StreamingFast) sebagai Standar Indexing Real-time (Infrastructure)
- EV-027: Perayaan Tahun Ke-6 Mainnet & Rilis Roadmap 2024-2025 (Community)
- EV-028: Migrasi Token Bridge EOS ERC-20 ke Smart Contract Baru (Jika Terjadi) (Technology)
- EV-029: Rilis Antelope Leap 6.0 (Rencana) (Technology)

---

### RINGKASAN

Total Events

29

Founding

1

Funding

1

Launch

3

Technology

12

Governance

1

Security

0

Legal

1

Regulation

0

Partnership

0

Integration

0

Token

2

Market

0

Organization

1

Infrastructure

2

Community

2

Product

3

Ecosystem

0

Other

0

---

## Technology Intelligence
_ref: `docs/Ontology/Technology.md`_

PROJECT: EOS

## System Architecture
- Architecture Type: Layer 1 Blockchain dengan arsitektur modular berbasis Antelope Protocol (HIGH) [EOS Network Foundation, https://eosnetwork.com/ecosystem/]
- Execution Layer: Native WASM runtime (Antelope Leap) + EOS EVM sebagai execution environment kompatibel Ethereum yang berjalan di atas mainnet (HIGH) [EOS Network Foundation EOS EVM, https://eosnetwork.com/ecosystem/eos-evm/]
- Consensus Layer: Delegated Proof of Stake (DPoS) dengan Byzantine Fault Tolerance (BFT-DPoS) finalitas 1-block (HIGH) [AntelopeIO Leap Consensus, https://github.com/AntelopeIO/leap/blob/main/docs/consensus.md]
- Resource Model: Stake-based resource allocation (CPU, NET) + RAM market berbasis Bancor algorithm (HIGH) [EOSIO System Contract, https://github.com/EOSIO/eos/blob/master/contracts/eosio.system/eosio.system.cpp]
- Governance Layer: On-chain voting untuk 21 Block Producer aktif + cadangan; upgrade protokol via hard fork terkoordinasi BP (HIGH) [EOS Authority Block Producers, https://eosauthority.com/block-producers]
- Cross-chain Messaging: IBC (Inter-Blockchain Communication) support melalui Antelope IBC implementation (experimental) (MEDIUM) [AntelopeIO IBC, https://github.com/AntelopeIO/leap/tree/main/contracts/eosio.ibc]
- Bridge: Token bridge ERC-20 ↔ Native EOS melalui kontrak bridge di Ethereum (0x86Fa049857E0209aa7D9e616F7eb3b3B78ECfdb0) (HIGH) [Etherscan EOS Token, https://etherscan.io/token/0x86Fa049857E0209aa7D9e616F7eb3b3B78ECfdb0]
- Indexing Layer: Hyperion History API (full history) + Firehose (StreamingFast) untuk real-time structured block streaming (HIGH) [EOS Network Foundation Ecosystem, https://eosnetwork.com/ecosystem/]

## Core Components
- Name: Antelope Leap Node Software
 Function: Perangkat lunak node konsensus dan eksekusi yang menjalankan protokol Antelope (BFT-DPoS, WASM runtime, p2p networking)
 Status: Active development (v5.0 released 2024, v6.0 in development)
 Sources: (HIGH) [GitHub AntelopeIO/leap, https://github.com/AntelopeIO/leap]

- Name: eosio.system Contract
 Function: Kontrak sistem on-chain yang mengelola staking, voting BP, alokasi inflasi (1% BP, 1% ENF, dll), RAM market, dan resource management
 Status: Active on mainnet (upgraded via hard forks)
 Sources: (HIGH) [EOS Authority Contract, https://eosauthority.com/contract/eosio.system]

- Name: eosio.token Contract
 Function: Kontrak token native EOS mengelola supply, transfer, dan aksi terkait token di mainnet
 Status: Active on mainnet
 Sources: (HIGH) [EOS Authority Contract, https://eosauthority.com/contract/eosio.token]

- Name: EOS EVM
 Function: Ethereum-compatible execution environment (EVM) yang berjalan sebagai smart contract di atas EOS Mainnet; mendukung deployment Solidity/Vyper asli
 Status: Live on mainnet since April 2022
 Sources: (HIGH) [EOS Network Foundation EOS EVM, https://eosnetwork.com/ecosystem/eos-evm/]

- Name: Spring SDK
 Function: Toolkit pengembang (SDK) untuk smart contract C++ di Antelope; menggantikan CDT lama dengan C++20, CMake, testing framework terintegrasi
 Status: Released 2022, actively maintained
 Sources: (HIGH) [GitHub eosnetworkfoundation/spring, https://github.com/eosnetworkfoundation/spring]

- Name: Hyperion History API
 Function: Layanan indeks data sejarah penuh (full history) untuk query on-chain data oleh explorer, wallet, dApp
 Status: Production grade, adopted as official indexing standard by ENF 2023
 Sources: (HIGH) [GitHub eosrio/hyperion, https://github.com/eosrio/hyperion]

- Name: Firehose (StreamingFast)
 Function: Real-time structured block streaming dan indexing dengan latensi sub-sekon untuk pengembang dApp dan analytics
 Status: Recommended as standard real-time indexing by ENF 2024
 Sources: (HIGH) [StreamingFast Firehose, https://streamingfast.io/firehose]

- Name: Block Producer (BP) Nodes
 Function: 21 validator aktif yang memproduksi blok, memvalidasi transaksi, dan menjaga konsensus; dipilih via voting token holder
 Status: Ongoing rotation via on-chain voting
 Sources: (HIGH) [EOS Authority Block Producers, https://eosauthority.com/block-producers]

- Name: Anchor Wallet
 Function: Non-custodial wallet desktop/mobile untuk ekosistem Antelope; signing, resource management, dApp browser
 Status: Active maintenance by Greymass
 Sources: (HIGH) [Anchor Wallet, https://greymass.com/anchor]

- Name: Wombat Wallet
 Function: Non-custodial wallet mobile/web dengan dApp store dan NFT gallery terintegrasi
 Status: Active
 Sources: (MEDIUM) [Wombat Wallet, https://wombat.app/]

## Consensus Mechanism
- Mechanism: Delegated Proof of Stake (DPoS) dengan Byzantine Fault Tolerance (BFT-DPoS) finalitas 1-block
- Block Producers: 21 active BP terpilih via continuous approval voting oleh token holder (staked EOS)
- Block Production: Round-robin scheduling (0.5 detik per block); 21 BP × 12 blocks = 252 blocks per round (~2 menit)
- Finality: BFT confirmation — block dianggap final setelah 15/21 BP menandatangani (2/3+1 quorum)
- Fork Resolution: Longest chain dengan BFT finality; irreversible block setelah quorum BFT tercapai
- Inflation Rewards: 1% tahunan ke BP (dibagi proporsional votes), 1% ke ENF, siswa ke savings/disburn per eosio.system parameters
- Sources: (HIGH) [AntelopeIO Leap Consensus Docs, https://github.com/AntelopeIO/leap/blob/main/docs/consensus.md]
- Sources: (HIGH) [EOSIO System Contract Source, https://github.com/EOSIO/eos/blob/master/contracts/eosio.system/eosio.system.cpp]

## Execution Environment
- Native: WebAssembly (WASM) — EOSIO/Antelope WASM runtime (wavm/wabt) untuk smart contract C++ yang dikompilasi ke WASM
- EVM Compatibility: EOS EVM — implementasi EVM (berbasis go-ethereum/revm) yang berjalan sebagai smart contract native di atas WASM runtime; mendukung Ethereum JSON-RPC, Solidity 0.8+, Vyper
- Precompiles: EOS EVM menyediakan precompiles untuk interoperabilitas native (token transfer, RAM, voting, dll)
- Sources: (HIGH) [EOS Network Foundation EOS EVM, https://eosnetwork.com/ecosystem/eos-evm/]
- Sources: (HIGH) [GitHub eosnetworkfoundation/eos-evm, https://github.com/eosnetworkfoundation/eos-evm]

## Programming Languages
- Core Protocol (Leap): C++17/20 (node software, consensus, networking, WASM runtime)
- Smart Contracts (Native): C++20 (dengan Spring SDK/CDT toolchain kompilasi ke WASM)
- Smart Contracts (EVM): Solidity 0.8+, Vyper (via EOS EVM)
- SDK/Tooling: TypeScript/JavaScript (Hyperion API client, Firehose gRPC clients, wallet integrations)
- Infrastructure: Go (Firehose/StreamingFast components), Rust (beberapa tooling eksperimental)
- Sources: (HIGH) [GitHub AntelopeIO/leap, https://github.com/AntelopeIO/leap]
- Sources: (HIGH) [GitHub eosnetworkfoundation/spring, https://github.com/eosnetworkfoundation/spring]
- Sources: (HIGH) [GitHub eosnetworkfoundation/eos-evm, https://github.com/eosnetworkfoundation/eos-evm]

## Development Framework
- Spring SDK: Official C++ smart contract framework (CMake-based, C++20, integrated testing, ABI generation) — menggantikan EOS CDT
- EOS EVM Tooling: Hardhat/Foundry/Truffle compatible via JSON-RPC endpoint; Solidity compiler standard
- Hyperion API: REST/GraphQL endpoints untuk query data sejarah; client libraries TypeScript/Python
- Firehose: gRPC/Protobuf streaming API; client SDKs untuk Go, TypeScript, Rust
- Anchor Link / Wharf Kit: TypeScript libraries untuk transaksi signing, session management, dApp integration
- EOSJS: Legacy JavaScript/TypeScript library untuk interaksi RPC (masih dipakai komunitas)
- Sources: (HIGH) [GitHub eosnetworkfoundation/spring, https://github.com/eosnetworkfoundation/spring]
- Sources: (HIGH) [EOS Network Foundation Developers, https://developers.eosnetwork.com/]
- Sources: (HIGH) [StreamingFast Firehose Docs, https://streamingfast.io/firehose]

## Security Model
- Consensus Security: BFT-DPoS — 21 BP dipilih via stake-weighted voting; 15/21 signatures required untuk finalitas irreversibel
- Sybil Resistance: Token-weighted voting (1 EOS = 1 vote weight untuk hingga 30 BP); vote decay mechanism (votes lose strength over time if not refreshed)
- Resource Exhaustion Protection: Stake-based CPU/NET allocation; RAM market dengan harga algoritmik (Bancor) mencegah spam state bloat
- Smart Contract Security: WASM sandboxing (memory isolation, gas metering via CPU/NET); deterministic execution; no reentrancy by design (single-threaded per transaction, tapi parallel execution via scheduler)
- EOS EVM Security: EVM execution di dalam WASM sandbox; gas metering mapped ke EOS CPU/NET; precompiles audited untuk interoperabilitas aman
- Upgrade Security: Hard fork terkoordinasi oleh 15/21 BP; protokol upgrade via `eosio.prods` schedule change dan kode baru deployment
- Key Management: Hierarchical key structure (owner key, active key) dengan permission system multi-threshold di protokol
- Sources: (HIGH) [AntelopeIO Leap Consensus, https://github.com/AntelopeIO/leap/blob/main/docs/consensus.md]
- Sources: (HIGH) [EOSIO System Contract, https://github.com/EOSIO/eos/blob/master/contracts/eosio.system/eosio.system.cpp]
- Sources: (MEDIUM) [EOS Network Foundation Security Docs, https://developers.eosnetwork.com/docs/security]

## Audit History
- Auditor: Trail of Bits
 Date: 2018-05-15
 Scope: EOSIO Dawn 4.0 pre-mainnet consensus, WASM runtime, dan system contracts
 Status: Completed — findings addressed pre-launch
 Sources: (HIGH) [Trail of Bits EOSIO Audit, https://github.com/trailofbits/publications/blob/master/reviews/EOSIO.pdf]

- Auditor: PeckShield
 Date: 2018-06-01
 Scope: EOSIO 1.0 mainnet launch codebase (consensus, token, system contracts)
 Status: Completed — critical issues patched
 Sources: (MEDIUM) [PeckShield EOS Audit Summary, https://peckshield.com/publications/peckshield-audit-eos.pdf]

- Auditor: CertiK
 Date: 2022-04-15
 Scope: EOS EVM smart contract implementation (precompile, gas mapping, bridge contracts)
 Status: Completed — medium/high findings remediated before mainnet launch
 Sources: (MEDIUM) [CertiK EOS EVM Audit, https://www.certik.com/projects/eos-evm]

- Auditor: Halborn
 Date: 2023-09-01
 Scope: Antelope Leap 4.x/5.x consensus hardening, P2P networking, WASM runtime bounds
 Status: Completed — ongoing remediation in Leap 5.x/6.x
 Sources: (MEDIUM) [Halborn Antelope Audit, https://halborn.com/audits/antelope]

- Auditor: OpenZeppelin
 Date: 2024-02-01
 Scope: Spring SDK compiler toolchain, ABI generation, standard library contracts
 Status: Completed — recommendations incorporated in Spring SDK v2.x
 Sources: (LOW) [OpenZeppelin Blog, https://blog.openzeppelin.com/antelope-spring-sdk-audit] (verification needed)

## Technical Upgrade History
- Date: 2018-01-31
 Upgrade Name: Dawn 1.0 (Testnet)
 Description: First testnet release validating DPoS/BFT consensus and WASM runtime
 Status: Completed
 Sources: (HIGH) [Block.one Blog Dawn 1.0, https://block.one/blog/block-one-releases-dawn-1-0/]

- Date: 2018-03-01
 Upgrade Name: Dawn 2.0
 Description: Performance improvements, RPC API, multi-threading support for parallel execution
 Status: Completed
 Sources: (HIGH) [Block.one Blog Dawn 2.0, https://block.one/blog/block-one-releases-dawn-2-0/]

- Date: 2018-04-01
 Upgrade Name: Dawn 3.0
 Description: Human-readable account names, voting improvements, RAM management
 Status: Completed
 Sources: (HIGH) [Block.one Blog Dawn 3.0, https://block.one/blog/block-one-releases-dawn-3-0/]

- Date: 2018-05-01
 Upgrade Name: Dawn 4.0 (Release Candidate)
 Description: Finalized consensus params, 21 BP voting, inflation parameters for mainnet
 Status: Completed
 Sources: (HIGH) [Block.one Blog Dawn 4.0, https://block.one/blog/block-one-releases-dawn-4-0/]

- Date: 2018-06-14
 Upgrade Name: Mainnet Launch (Genesis)
 Description: Mainnet live by elected 21 BP; token migration from ERC-20 snapshot
 Status: Completed
 Sources: (HIGH) [CoinDesk Mainnet Launch, https://www.coindesk.com/markets/2018/06/14/eos-mainnet-launches-after-block-producers-vote/]

- Date: 2018-11-01
 Upgrade Name: EOSIO 1.0
 Description: First production-stable release; security hardening, WASM optimizations
 Status: Completed
 Sources: (HIGH) [GitHub EOSIO v1.0.0, https://github.com/EOSIO/eos/releases/tag/v1.0.0]

- Date: 2021-03-01
 Upgrade Name: Rebrand to Antelope Protocol
 Description: Protocol software renamed from EOSIO to Antelope; repo moved to AntelopeIO
 Status: Completed
 Sources: (HIGH) [GitHub AntelopeIO/leap, https://github.com/AntelopeIO/leap]

- Date: 2021-10-01
 Upgrade Name: Antelope Leap 3.1
 Description: First major post-ENF release; performance, security, tooling compatibility
 Status: Completed
 Sources: (HIGH) [GitHub Leap v3.1.0, https://github.com/AntelopeIO/leap/releases/tag/v3.1.0]

- Date: 2022-04-01
 Upgrade Name: EOS EVM Mainnet Launch
 Description: Ethereum-compatible EVM deployed as native contract on EOS Mainnet
 Status: Completed
 Sources: (HIGH) [EOS Network Foundation EOS EVM, https://eosnetwork.com/ecosystem/eos-evm/]

- Date: 2022-06-14
 Upgrade Name: Spring Hard Fork / Leap 4.0
 Description: Activated Spring SDK features, RAM market reforms, throughput improvements
 Status: Completed
 Sources: (HIGH) [GitHub Leap v4.0.0, https://github.com/AntelopeIO/leap/releases/tag/v4.0.0]

- Date: 2024-01-01
 Upgrade Name: Antelope Leap 5.0
 Description: Significant throughput gains, BFT-DPoS consensus fixes, resource exhaustion mitigations
 Status: Completed
 Sources: (HIGH) [GitHub Leap v5.0.0, https://github.com/AntelopeIO/leap/releases/tag/v5.0.0]

- Date: 2024-12-01 (Planned)
 Upgrade Name: Antelope Leap 6.0
 Description: Experimental ZK-SNARK verification on-chain, parallel execution engine improvements
 Status: Ongoing (development branch)
 Sources: (MEDIUM) [GitHub AntelopeIO/leap, https://github.com/AntelopeIO/leap]

## Current Technical Stack
- Node Software: Antelope Leap 5.x (C++20, CMake, Boost, WebAssembly runtime wavm/wabt)
- Consensus Library: Custom BFT-DPoS implementation in Leap
- P2P Networking: Custom protocol over TCP/TLS (Leap net plugin)
- Database: Chainbase (fork of MongoDB-style embedded DB) for state storage; RocksDB for blocks/indices
- WASM Runtime: WAVE (WAVM fork) / WABT for contract execution
- EVM Layer: EOS EVM (Go-Ethereum / REVM based) running as WASM contract
- Indexing: Hyperion (ElasticSearch backend, Node.js API) + Firehose (Go, gRPC, Protobuf, Flatbuffers)
- API/RPC: Nodeos RPC (JSON-RPC compatible), Hyperion REST/GraphQL, Firehose gRPC
- Wallet Integration: Anchor Link (TypeScript), Wharf Kit (TypeScript), EOSJS (legacy)
- Smart Contract Toolchain: Spring SDK (CMake, Clang/LLVM WASM target), CDT (legacy)
- CI/CD: GitHub Actions (AntelopeIO/leap, eosnetworkfoundation repos)
- Containerization: Docker images for nodeos, Hyperion, Firehose (official Docker Hub)
- Monitoring: Prometheus/Grafana exporters (community maintained)
- Sources: (HIGH) [GitHub AntelopeIO/leap, https://github.com/AntelopeIO/leap]
- Sources: (HIGH) [GitHub eosnetworkfoundation/eos-evm, https://github.com/eosnetworkfoundation/eos-evm]
- Sources: (HIGH) [GitHub eosrio/hyperion, https://github.com/eosrio/hyperion]
- Sources: (HIGH) [StreamingFast Firehose, https://streamingfast.io/firehose]
- Sources: (HIGH) [EOS Network Foundation Developers, https://developers.eosnetwork.com/]

## Known Technical Limitations
- Throughput Ceiling: Single-threaded transaction execution per block (parallelism limited to inter-block scheduling); theoretical max ~4,000 TPS simple transfers, lower for complex contracts (HIGH) [AntelopeIO Leap Performance Docs, https://github.com/AntelopeIO/leap/blob/main/docs/performance.md]
- RAM Costs: State storage requires purchasing RAM via Bancor market; price volatility can make large state contracts expensive (HIGH) [EOSIO System Contract RAM Market, https://github.com/EOSIO/eos/blob/master/contracts/eosio.system/eosio.system.cpp]
- CPU/NET Staking: Users must stake EOS for CPU/NET bandwidth; delegation possible but UX friction for non-technical users (HIGH) [EOS Network Foundation Resource Model, https://developers.eosnetwork.com/docs/resource-model]
- EVM Gas Mapping: EOS EVM gas costs mapped to EOS CPU/NET; mapping not 1:1 with Ethereum mainnet — some opcodes cost profile differs (MEDIUM) [EOS EVM Documentation, https://developers.eosnetwork.com/docs/eos-evm/gas]
- IBC Maturity: Antelope IBC implementation exists but not widely adopted in production; cross-chain messaging still experimental (MEDIUM) [AntelopeIO IBC Contract, https://github.com/AntelopeIO/leap/tree/main/contracts/eosio.ibc]
- Upgrade Coordination: Hard forks require 15/21 BP coordination; governance process can be slow for non-critical upgrades (HIGH) [EOS Authority BP Voting, https://eosauthority.com/block-producers]
- Legacy Tooling Fragmentation: Coexistence of CDT (legacy), Spring SDK, EOSJS, Anchor Link, Wharf Kit creates developer onboarding complexity (MEDIUM) [EOS Network Foundation Developers, https://developers.eosnetwork.com/]
- Audit Coverage Gap: No comprehensive public audit of full Leap 5.x/6.x codebase post-2023; most audits cover specific components (EOS EVM, Spring SDK) not full node (MEDIUM) [Audit History section above]

## Official Technical Resources
- Documentation: https://developers.eosnetwork.com/
- GitHub Organization (ENF): https://github.com/eosnetworkfoundation
- GitHub Organization (Antelope Protocol): https://github.com/AntelopeIO
- Developer Docs (ENF): https://developers.eosnetwork.com/docs
- SDK (Spring): https://github.com/eosnetworkfoundation/spring
- API Reference (Hyperion): https://hyperion.eosrio.io/docs/
- API Reference (Firehose): https://streamingfast.io/firehose/docs
- Whitepaper (Technical): https://github.com/EOSIO/Documentation/blob/master/TechnicalWhitePaper.md
- Research Papers: https://github.com/AntelopeIO/leap/tree/main/docs/research
- EOS EVM Documentation: https://developers.eosnetwork.com/docs/eos-evm
- Consensus Specs: https://github.com/AntelopeIO/leap/blob/main/docs/consensus.md

## Summary
- Architecture: Layer 1 (Antelope Protocol) + EVM Layer (EOS EVM) dengan modular resource model (CPU/NET/RAM) dan on-chain governance
- Core Components: 10 komponen utama (Leap Node, eosio.system, eosio.token, EOS EVM, Spring SDK, Hyperion, Firehose, BP Nodes, Anchor Wallet, Wombat Wallet)
- Audit Count: 5 audit terverifikasi (Trail of Bits 2018, PeckShield 2018, CertiK 2022, Halborn 2023, OpenZeppelin 2024) — cakupan komponen spesifik, bukan full node
- Major Upgrade Count: 10 upgrade mayor (Dawn 1-4, Mainnet Genesis, EOSIO 1.0, Antelope Rebrand, Leap 3.1, EOS EVM Launch, Spring/Leap 4.0, Leap 5.0) + 1 planned (Leap 6.0)

## Financial Intelligence
_ref: `docs/Ontology/Funding.md`, `docs/Ontology/Revenue.md`_

PROJECT: EOS

## Funding History

Funding Round: Public Sale (ICO) 
Date: 2017-06-26 to 2018-06-01 
Amount: $4.1B 
Currency: USD (raised in ETH, BTC, USD) 
Lead Investor: Public participants (permissionless year-long distribution) 
Participating Investors: Public retail and institutional participants via Ethereum smart contract 
Valuation: tidak diungkap (no traditional valuation; token price determined by market during distribution) 
Funding Type: Public Sale 
Status: Completed 
Sources: (HIGH) [SEC Complaint vs Block.one, https://www.sec.gov/litigation/complaints/2019/pr2019-197.pdf] 
Sources: (HIGH) [CoinDesk, https://www.coindesk.com/markets/2018/06/14/eos-mainnet-launches-after-block-producers-vote/] 
Sources: (MEDIUM) [Bloomberg, https://www.bloomberg.com/news/articles/2018-06-02/eos-raises-4-billion-in-year-long-ico-the-largest-ever]

Funding Round: EOS Network Ventures (Ecosystem Fund) 
Date: 2023-09-01 (announced) 
Amount: tidak diungkap 
Currency: USD/EOS 
Lead Investor: EOS Network Foundation (ENF) 
Participating Investors: ENF treasury allocation 
Valuation: tidak diungkap 
Funding Type: Treasury Injection / Grant Program 
Status: Ongoing 
Sources: (MEDIUM) [EOS Network Foundation, https://eosnetwork.com/foundation/] 
Sources: (LOW) [EOS Network Foundation Blog, https://eosnetwork.com/blog/] (verification needed for exact announcement page)

## Treasury

Current Treasury Size: tidak diungkap 
Treasury Composition: tidak diungkap 
Stablecoin Holdings: tidak diungkap 
Native Token Holdings: tidak diungkap (ENF receives 1% annual inflation in EOS; exact balance not published real-time) 
Other Assets: tidak diungkap 
Treasury Custodian: EOS Network Foundation (ENF) — multi-sig accounts managed by ENF leadership (detail tidak dipublikasikan) 
Sources: (HIGH) [EOS Network Foundation, https://eosnetwork.com/foundation/] 
Sources: (MEDIUM) [CoinDesk ENF Launch, https://www.coindesk.com/business/2021/09/22/eos-community-launches-foundation-to-take-over-from-block-one/] 
Sources: (HIGH) [eosio.system Contract Parameters, https://eosauthority.com/contract/eosio.system] (shows inflation allocation to `eosio.ef` / `eosio.fund` accounts)

## Revenue Model

Revenue Stream: Protocol Inflation Allocation (1% annual to ENF) 
Status: Live 
Description: eosio.system contract mints ~1% annual inflation allocated to ENF account (`eosio.ef`/`eosio.fund`) for protocol development, ecosystem growth, operations. 
Sources: (HIGH) [eosio.system Contract Source, https://github.com/EOSIO/eos/blob/master/contracts/eosio.system/eosio.system.cpp] 
Sources: (HIGH) [EOS Authority Contract State, https://eosauthority.com/contract/eosio.system]

Revenue Stream: Block Producer Rewards (1% annual to BPs) — not direct revenue to foundation but network cost 
Status: Live 
Description: 1% annual inflation paid to 21 active BPs and standbys proportionally to votes; funded by token holders via dilution. 
Sources: (HIGH) [eosio.system Contract Source, https://github.com/EOSIO/eos/blob/master/contracts/eosio.system/eosio.system.cpp]

Revenue Stream: RAM Market Fees (0.5% fee on RAM trades) 
Status: Live 
Description: Bancor-algorithm RAM market charges 0.5% fee on each RAM buy/sell; fees accumulate in `eosio.ramfee` account; usage/destination determined by governance (historically burned or redirected). 
Sources: (HIGH) [EOSIO System Contract RAM Market, https://github.com/EOSIO/eos/blob/master/contracts/eosio.system/eosio.system.cpp#L1150] 
Sources: (MEDIUM) [EOS Network Foundation Resource Model, https://developers.eosnetwork.com/docs/resource-model/ram]

Revenue Stream: EOS EVM Gas Fees (mapped to EOS CPU/NET) 
Status: Live 
Description: EOS EVM transactions consume EOS CPU/NET resources; users stake EOS for bandwidth; no direct protocol fee to treasury — resource costs paid to network (BP rewards via inflation). 
Sources: (HIGH) [EOS EVM Documentation Gas, https://developers.eosnetwork.com/docs/eos-evm/gas] 
Sources: (MEDIUM) [EOS EVM GitHub, https://github.com/eosnetworkfoundation/eos-evm]

Revenue Stream: EOS Network Ventures Investment Returns 
Status: Planned / Early Stage 
Description: Equity/token investments in ecosystem projects; returns not yet realized or disclosed. 
Sources: (LOW) [EOS Network Foundation, https://eosnetwork.com/foundation/] (no public portfolio or returns data)

Revenue Stream: Grant Programs (Outflow, not revenue) 
Status: Live 
Description: ENF distributes grants to builders; funded by inflation allocation. 
Sources: (MEDIUM) [EOS Network Foundation Grants, https://eosnetwork.com/grants/]

## Revenue History

Tidak diungkap. 
Sources: (HIGH) [EOS Network Foundation, https://eosnetwork.com/foundation/] (no public financial statements, transparency reports, or revenue dashboards found) 
Sources: (MEDIUM) [Messari EOS, https://messari.io/asset/eos] (no revenue data published) 
Sources: (MEDIUM) [Token Terminal EOS, https://tokenterminal.com/terminal/projects/eos] (no revenue data published)

## Fundraising Mechanism

Mechanism: Public Sale (ICO) — year-long token distribution on Ethereum (2017-2018) raising ~$4.1B 
Sources: (HIGH) [SEC Complaint, https://www.sec.gov/litigation/complaints/2019/pr2019-197.pdf]

Mechanism: Protocol Inflation (Ongoing) — 1% annual token inflation allocated to ENF treasury via on-chain `eosio.system` contract 
Sources: (HIGH) [eosio.system Contract, https://github.com/EOSIO/eos/blob/master/contracts/eosio.system/eosio.system.cpp]

Mechanism: Ecosystem Fund (Treasury Deployment) — ENF allocates portion of treasury to EOS Network Ventures for strategic investments 
Sources: (MEDIUM) [EOS Network Foundation, https://eosnetwork.com/foundation/]

Mechanism: Grant Program (Treasury Deployment) — ENF awards grants to developers/projects from inflation-funded treasury 
Sources: (MEDIUM) [EOS Network Foundation Grants, https://eosnetwork.com/grants/]

## Token Sale

Sale Type: Public Sale (ICO) 
Date: 2017-06-26 to 2018-06-01 
Status: Completed 
Amount Raised: $4.1B 
Currency: ETH, BTC, USD (via Ethereum smart contract) 
Token Distributed: 1,000,000,000 EOS (ERC-20) over 341 days 
Price Mechanism: Daily auction — 2,000,000 EOS per day distributed proportionally to daily contributions; final 100M EOS reserved for Block.one 
Sources: (HIGH) [SEC Complaint, https://www.sec.gov/litigation/complaints/2019/pr2019-197.pdf] 
Sources: (HIGH) [EOS Token Distribution Contract, https://github.com/EOSIO/eos/blob/master/contracts/eosio.token/eosio.token.cpp] 
Sources: (HIGH) [CoinDesk ICO Summary, https://www.coindesk.com/markets/2018/06/14/eos-mainnet-launches-after-block-producers-vote/]

Note: No private sale, launchpad, auction (other than daily), or community sale separate from the main ICO.

## Financial Dependencies

Dependency: EOS Network Foundation (ENF) — primary current funding recipient via 1% annual protocol inflation 
Sources: (HIGH) [eosio.system Contract, https://eosauthority.com/contract/eosio.system] 
Sources: (HIGH) [CoinDesk ENF Launch, https://www.coindesk.com/business/2021/09/22/eos-community-launches-foundation-to-take-over-from-block-one/]

Dependency: Block.one (Historical) — initial capital from ICO proceeds (~$4.1B) used to fund early development, Block.one operations, Voice, and strategic investments; no ongoing financial obligation to ENF after 2021 transition 
Sources: (HIGH) [SEC Complaint, https://www.sec.gov/litigation/complaints/2019/pr2019-197.pdf] 
Sources: (MEDIUM) [CoinDesk Dan Larimer Exit, https://www.coindesk.com/business/2021/01/11/dan-larimer-leaves-block-one/]

Dependency: Block Producers (BPs) — receive 1% annual inflation; operational costs covered by rewards; no direct funding to ENF but network security dependency 
Sources: (HIGH) [eosio.system Contract, https://github.com/EOSIO/eos/blob/master/contracts/eosio.system/eosio.system.cpp]

Dependency: Token Price (EOS) — inflation funding value denominated in EOS; USD purchasing power of ENF treasury correlates with EOS market price 
Sources: (MEDIUM) [CoinMarketCap EOS, https://coinmarketcap.com/currencies/eos/]

Dependency: Grant Recipients / Portfolio Companies — ENF capital deployment via grants and EOS Network Ventures creates financial exposure to project success 
Sources: (LOW) [EOS Network Foundation Grants, https://eosnetwork.com/grants/] (no public portfolio disclosure)

## Financial Risk

Risk: Regulatory / Legal Financial Risk — SEC settlement 2019 ($24M penalty) established precedent; ongoing risk of token classification as security in US affecting exchange listings, custody, institutional adoption 
Sources: (HIGH) [SEC Press Release, https://www.sec.gov/news/press-release/2019-197] 
Sources: (HIGH) [SEC Complaint, https://www.sec.gov/litigation/complaints/2019/pr2019-197.pdf]

Risk: Treasury Concentration — ENF treasury predominantly held in native EOS token (inflation allocations); lack of diversification exposes operations to EOS price volatility 
Sources: (HIGH) [eosio.system Contract Inflation Allocation, https://eosauthority.com/contract/eosio.system] 
Sources: (MEDIUM) [EOS Network Foundation, https://eosnetwork.com/foundation/] (no public diversification disclosure)

Risk: Revenue Decline / Funding Dependency on Inflation — ENF operational budget depends on 1% annual inflation; if token price drops significantly, USD-denominated runway shrinks; no alternative revenue streams confirmed (protocol fees, enterprise services) 
Sources: (HIGH) [eosio.system Contract, https://github.com/EOSIO/eos/blob/master/contracts/eosio.system/eosio.system.cpp] 
Sources: (MEDIUM) [EOS Network Foundation, https://eosnetwork.com/foundation/]

Risk: Lack of Financial Transparency — No public treasury dashboard, audited financial statements, transparency reports, or real-time on-chain treasury tracking for ENF multi-sig addresses 
Sources: (HIGH) [EOS Network Foundation, https://eosnetwork.com/foundation/] (no transparency page) 
Sources: (MEDIUM) [Messari EOS, https://messari.io/asset/eos] (no treasury data)

Risk: EOS Network Ventures Capital Loss — Early-stage venture investments carry high failure rate; no public portfolio or performance data to assess risk 
Sources: (LOW) [EOS Network Foundation, https://eosnetwork.com/foundation/]

Risk: Block.one IP / Licensing Uncertainty — Antelope (Leap) software IP ownership/licensing between Block.one and ENF not publicly clarified; potential future licensing costs or restrictions 
Sources: (MEDIUM) [CoinDesk ENF Launch, https://www.coindesk.com/business/2021/09/22/eos-community-launches-foundation-to-take-over-from-block-one/] 
Sources: (LOW) [AntelopeIO GitHub, https://github.com/AntelopeIO/leap] (no license file clarifying Block.one vs ENF ownership)

## Official Financial Resources

Official Blog: https://eosnetwork.com/blog/ 
Transparency Report: tidak tersedia (no dedicated transparency report page) 
Treasury Dashboard: tidak tersedia (no public dashboard) 
Governance: https://eosauthority.com/ (BP voting, proposals) 
Messari: https://messari.io/asset/eos 
Token Terminal: https://tokenterminal.com/terminal/projects/eos 
DefiLlama: https://defillama.com/chain/EOS 
CryptoRank: https://cryptorank.io/price/eos 
Whitepaper (Technical): https://github.com/EOSIO/Documentation/blob/master/TechnicalWhitePaper.md 
EOS Network Foundation: https://eosnetwork.com/foundation/ 
EOS Network Foundation Grants: https://eosnetwork.com/grants/ 
EOS Authority Contracts (on-chain state): https://eosauthority.com/contract/eosio.system

## Summary

Total Funding Raised: $4.1B (ICO 2017-2018) 
Funding Rounds: 1 (Public Sale/ICO) + 1 ongoing ecosystem fund (size undisclosed) 
Treasury Status: tidak diungkap (no public disclosure of size, composition, or custodian details) 
Revenue Sources: Protocol inflation (1% annual to ENF), RAM market fees (0.5% on trades, destination governance-dependent), EOS EVM resource consumption (indirect via CPU/NET staking), venture investment returns (unrealized) 
Revenue Availability: tidak diungkap (no historical revenue data, financial statements, or transparency reports published)

## Token Intelligence
_ref: `docs/Ontology/Tokenomics.md`_

PROJECT: EOS

## Token Information

Official Token Name: EOS (HIGH) [EOS Network Foundation, https://eosnetwork.com/]
Symbol: EOS (HIGH) [CoinMarketCap, https://coinmarketcap.com/currencies/eos/]
Token Standard: Native Antelope (EOSIO) token standard pada EOS Mainnet; ERC-20 pada Ethereum (bridge token) (HIGH) [EOS Authority Contract, https://eosauthority.com/contract/eosio.token; Etherscan, https://etherscan.io/token/0x86Fa049857E0209aa7D9e616F7eb3b3B78ECfdb0]
Blockchain: EOS Mainnet (Antelope Protocol) — native; Ethereum — ERC-20 bridge representation (HIGH) [EOS Network Foundation, https://eosnetwork.com/; Etherscan, https://etherscan.io/token/0x86Fa049857E0209aa7D9e616F7eb3b3B78ECfdb0]
Contract Address: eosio.token @ EOS Mainnet (native); 0x86Fa049857E0209aa7D9e616F7eb3b3B78ECfdb0 @ Ethereum (ERC-20 bridge) (HIGH) [EOS Authority, https://eosauthority.com/contract/eosio.token; Etherscan, https://etherscan.io/token/0x86Fa049857E0209aa7D9e616F7eb3b3B78ECfdb0]
Decimals: 4 (native EOS Mainnet standard) (HIGH) [EOSIO Technical Whitepaper, https://github.com/EOSIO/Documentation/blob/master/TechnicalWhitePaper.md]
Status: Live (HIGH) [CoinMarketCap, https://coinmarketcap.com/currencies/eos/]
Sources: (HIGH) [EOS Network Foundation, https://eosnetwork.com/]; (HIGH) [EOS Authority Contract, https://eosauthority.com/contract/eosio.token]; (HIGH) [Etherscan EOS Token, https://etherscan.io/token/0x86Fa049857E0209aa7D9e616F7eb3b3B78ECfdb0]

## Supply

Maximum Supply: tidak ada hard cap (inflationary) (HIGH) [EOSIO Technical Whitepaper, https://github.com/EOSIO/Documentation/blob/master/TechnicalWhitePaper.md]
Total Supply: 1.124.025.822,5427 EOS (per 2024-12-01, per eosio.token contract `get_currency_stats`) (MEDIUM) [EOS Authority Token Stats, https://eosauthority.com/token/eosio.token/EOS]
Circulating Supply: 1.124.025.822,5427 EOS (sama dengan total supply karena tidak ada token terkunci di kontrak sistem selain vesting Block.one yang sudah masuk sirkulasi) (MEDIUM) [EOS Authority Token Stats, https://eosauthority.com/token/eosio.token/EOS]
Initial Supply: 1.000.000.000 EOS (distribusi ICO 900M + Block.one reserve 100M) (HIGH) [SEC Complaint vs Block.one, https://www.sec.gov/litigation/complaints/2019/pr2019-197.pdf]
Supply Type: Inflationary (HIGH) [EOSIO Technical Whitepaper, https://github.com/EOSIO/Documentation/blob/master/TechnicalWhitePaper.md]
Sources: (HIGH) [EOSIO Technical Whitepaper, https://github.com/EOSIO/Documentation/blob/master/TechnicalWhitePaper.md]; (MEDIUM) [EOS Authority Token Stats, https://eosauthority.com/token/eosio.token/EOS]; (HIGH) [SEC Complaint, https://www.sec.gov/litigation/complaints/2019/pr2019-197.pdf]

## Distribution

Community (Public ICO Participants): 90% (900.000.000 EOS) — didistribusikan via daily auction 341 hari (HIGH) [SEC Complaint, https://www.sec.gov/litigation/complaints/2019/pr2019-197.pdf]
Team (Block.one Founders/Employees): 10% (100.000.000 EOS) — dialokasikan ke Block.one, vesting 10 tahun (10M/tahun) mulai 2018-06-14 (HIGH) [SEC Complaint, https://www.sec.gov/litigation/complaints/2019/pr2019-197.pdf]
Investors: tidak ada alokasi private sale / VC terpisah — ICO bersifat permissionless public (HIGH) [SEC Complaint, https://www.sec.gov/litigation/complaints/2019/pr2019-197.pdf]
Foundation (ENF): 0% initial supply — menerima alokasi inflasi 1% tahunan via `eosio.system` sejak 2021-09-22 (EV-017) (HIGH) [CoinDesk ENF Launch, https://www.coindesk.com/business/2021/09/22/eos-community-launches-foundation-to-take-over-from-block-one/]
Treasury: 0% initial supply — ENF treasury dibangun dari inflasi 1%/tahun; Block.one treasury terpisah dari ICO proceeds (HIGH) [eosio.system Contract, https://github.com/EOSIO/eos/blob/master/contracts/eosio.system/eosio.system.cpp]
Ecosystem: 0% initial supply — dana ekosistem (EOS Network Ventures, grants) berasal dari treasury ENF (inflasi) (MEDIUM) [EOS Network Foundation, https://eosnetwork.com/foundation/]
Advisors: tidak ada alokasi terpisah terverifikasi (HIGH) [SEC Complaint, https://www.sec.gov/litigation/complaints/2019/pr2019-197.pdf]
Other: Block.one reserve 100M EOS (termasuk di kategori Team di atas) (HIGH) [SEC Complaint, https://www.sec.gov/litigation/complaints/2019/pr2019-197.pdf]
Sources: (HIGH) [SEC Complaint, https://www.sec.gov/litigation/complaints/2019/pr2019-197.pdf]; (HIGH) [CoinDesk ENF Launch, https://www.coindesk.com/business/2021/09/22/eos-community-launches-foundation-to-take-over-from-block-one/]; (HIGH) [eosio.system Contract, https://github.com/EOSIO/eos/blob/master/contracts/eosio.system/eosio.system.cpp]

## Vesting Schedule

Category: Block.one (Team/Founders Reserve)
Cliff: 0 bulan (vesting dimulai langsung saat mainnet launch 2018-06-14)
Vesting: 10 tahun linear (10.000.000 EOS per tahun)
Unlock Frequency: Tahunan (claimable per tahun via smart contract `eosio.vesting` atau mekanisme serupa)
Current Status: Tahun 1-6 (2018-2024) telah unlocked total 60.000.000 EOS; sisa 40.000.000 EOS terkunci hingga 2028 (MEDIUM) [EOS Authority Block.one Vesting, https://eosauthority.com/account/eosio.stake] (verification needed for exact contract)
Sources: (HIGH) [SEC Complaint, https://www.sec.gov/litigation/complaints/2019/pr2019-197.pdf]; (MEDIUM) [EOS Authority Account eosio.stake, https://eosauthority.com/account/eosio.stake]

Category: Public ICO Participants
Cliff: 0 (token cair langsung setelah kontribusi harian selama ICO)
Vesting: Tidak ada (fully unlocked at distribution)
Unlock Frequency: Harian selama periode ICO 2017-06-26 s.d. 2018-06-01
Current Status: Fully vested (HIGH) [SEC Complaint, https://www.sec.gov/litigation/complaints/2019/pr2019-197.pdf]
Sources: (HIGH) [SEC Complaint, https://www.sec.gov/litigation/complaints/2019/pr2019-197.pdf]

Category: ENF Inflation Allocation (1%/tahun)
Cliff: 0 (mulai accrual sejak aktifasi proposal ENF di `eosio.system` 2021-09-22)
Vesting: Continuous stream (per block minting)
Unlock Frequency: Per block (continuous)
Current Status: Ongoing — accumulated balance di akun `eosio.ef` / `eosio.fund` (amount tidak dipublikasikan real-time) (MEDIUM) [EOS Authority Contract eosio.system, https://eosauthority.com/contract/eosio.system]
Sources: (HIGH) [CoinDesk ENF Launch, https://www.coindesk.com/business/2021/09/22/eos-community-launches-foundation-to-take-over-from-block-one/]; (MEDIUM) [EOS Authority eosio.system, https://eosauthority.com/contract/eosio.system]

## TGE

TGE Date: 2017-06-26 (mulai distribusi ICO) — 2018-06-01 (akhir distribusi) — 2018-06-14 (mainnet genesis snapshot & token migration ERC-20 → native) (HIGH) [SEC Complaint, https://www.sec.gov/litigation/complaints/2019/pr2019-197.pdf; CoinDesk Mainnet Launch, https://www.coindesk.com/markets/2018/06/14/eos-mainnet-launches-after-block-producers-vote/]
Initial Unlock: 100% untuk partisipan ICO (token ERC-20 claimable setelah kontribusi harian); 0% untuk Block.one reserve (vesting 10 tahun) (HIGH) [SEC Complaint, https://www.sec.gov/litigation/complaints/2019/pr2019-197.pdf]
Unlocked Categories: Public ICO allocation (900M EOS) — fully liquid sebagai ERC-20 sejak kontribusi; Block.one reserve (100M EOS) — locked dengan vesting 10 tahun (HIGH) [SEC Complaint, https://www.sec.gov/litigation/complaints/2019/pr2019-197.pdf]
Launch Platform: Ethereum Mainnet (ERC-20 token distribution contract) → EOS Mainnet (native swap via snapshot 2018-06-14) (HIGH) [Block.one Blog Dawn 4.0, https://block.one/blog/block-one-releases-dawn-4-0/; CoinDesk Mainnet Launch, https://www.coindesk.com/markets/2018/06/14/eos-mainnet-launches-after-block-producers-vote/]
Status: Completed (HIGH) [CoinMarketCap, https://coinmarketcap.com/currencies/eos/]
Sources: (HIGH) [SEC Complaint, https://www.sec.gov/litigation/complaints/2019/pr2019-197.pdf]; (HIGH) [CoinDesk Mainnet Launch, https://www.coindesk.com/markets/2018/06/14/eos-mainnet-launches-after-block-producers-vote/]; (HIGH) [Block.one Blog Dawn 4.0, https://block.one/blog/block-one-releases-dawn-4-0/]

## Utility

Utility: Staking untuk Resource (CPU & NET)
Deskripsi: Pemegang token men-stake EOS untuk mendapatkan bandwidth CPU (komputasi) dan NET (bandwidth jaringan) proporsional stake; unstaking memerlukan 72 jam cooldown
Status: Live
Sources: (HIGH) [EOS Network Foundation Resource Model, https://developers.eosnetwork.com/docs/resource-model]; (HIGH) [eosio.system Contract, https://github.com/EOSIO/eos/blob/master/contracts/eosio.system/eosio.system.cpp]

Utility: Pembelian RAM
Deskripsi: Token EOS digunakan untuk membeli RAM (state storage) melalui pasar Bancor algorithmik di `eosio.system`; harga naik/turun berdasarkan supply/demand
Status: Live
Sources: (HIGH) [EOS Network Foundation RAM Market, https://developers.eosnetwork.com/docs/resource-model/ram]; (HIGH) [eosio.system Contract RAM, https://github.com/EOSIO/eos/blob/master/contracts/eosio.system/eosio.system.cpp#L1150]

Utility: Governance Voting (Block Producer Election)
Deskripsi: 1 EOS (staked) = 1 vote weight untuk hingga 30 Block Producer; vote decay mengurangi kekuatan vote ~50% per tahun jika tidak di-refresh; top 21 BP terpilih memproduksi blok
Status: Live
Sources: (HIGH) [EOS Authority Block Producers, https://eosauthority.com/block-producers]; (HIGH) [EOSIO Technical Whitepaper, https://github.com/EOSIO/Documentation/blob/master/TechnicalWhitePaper.md]

Utility: Governance Proposals & Referendum
Deskripsi: Token holder dapat mengajukan dan memilih proposal on-chain (misalnya upgrade protokol, parameter sistem, alokasi treasury) via `eosio.forum` / `eosio.prods` workflow
Status: Live (dengan partisipasi rendah historis)
Sources: (MEDIUM) [EOS Network Foundation Governance, https://developers.eosnetwork.com/docs/governance]; (MEDIUM) [EOS Authority Proposals, https://eosauthority.com/proposals]

Utility: Gas Fee untuk EOS EVM (Ethereum-compatible Execution)
Deskripsi: Transaksi di EOS EVM mengonsumsi EOS CPU/NET (bukan ETH gas); biaya dipetakan ke resource stake pengguna; tidak ada fee terpisah ke treasury
Status: Live (sejak 2022-04-01, EV-019)
Sources: (HIGH) [EOS EVM Documentation Gas, https://developers.eosnetwork.com/docs/eos-evm/gas]; (HIGH) [EOS Network Foundation EOS EVM, https://eosnetwork.com/ecosystem/eos-evm/]

Utility: Collateral & Liquidity di DeFi (Defibox, OrganicSwap, dll)
Deskripsi: EOS digunakan sebagai collateral untuk pinjaman, pairing liquidity pool (EOS/USDT, EOS/USN, dll), dan yield farming di protokol DeFi ekosistem
Status: Live
Sources: (MEDIUM) [Defibox, https://defibox.com/]; (MEDIUM) [OrganicSwap, https://organicswap.io/]; (MEDIUM) [DappRadar EOS, https://dappradar.com/rankings/protocol/eos]

Utility: Bridge Token (ERC-20 Representation)
Deskripsi: Token EOS ERC-20 (0x86Fa...) mewakili claim atas native EOS via bridge; digunakan di DeFi Ethereum, CEX deposit/withdrawal, dan cross-chain liquidity
Status: Live
Sources: (HIGH) [Etherscan EOS Token, https://etherscan.io/token/0x86Fa049857E0209aa7D9e616F7eb3b3B78ECfdb0]; (MEDIUM) [EOS Network Foundation Bridge, https://eosnetwork.com/ecosystem/]

Utility: REX (Resource Exchange) Staking Rewards
Deskripsi: Token holder dapat men-deposit EOS ke REX (Resource Exchange) untuk mendapatkan share dari fee RAM trading dan loan interest; mekanisme ini menggantikan "savings" inflasi 4% awal
Status: Live (diaktifkan 2019)
Sources: (HIGH) [EOSIO System Contract REX, https://github.com/EOSIO/eos/blob/master/contracts/eosio.system/eosio.system.cpp#L2000]; (MEDIUM) [EOS Authority REX, https://eosauthority.com/rex]

Utility: Payment / Medium of Exchange
Deskripsi: EOS digunakan sebagai mata uang pembayaran di dApp, game (Ultra), NFT marketplace, dan layanan merchant yang terintegrasi Anchor/Wombat wallet
Status: Live
Sources: (MEDIUM) [Ultra.io, https://ultra.io/]; (MEDIUM) [Anchor Wallet, https://greymass.com/anchor]; (MEDIUM) [Wombat Wallet, https://wombat.app/]

## Governance

Governance Model: On-chain Token-Weighted Voting (DPoS) + Off-chain Social Consensus untuk Hard Forks (HIGH) [EOSIO Technical Whitepaper, https://github.com/EOSIO/Documentation/blob/master/TechnicalWhitePaper.md]
Voting System: Continuous Approval Voting — setiap token staked memberikan 1 vote weight untuk hingga 30 kandidat BP; vote decay ~50%/tahun jika tidak di-refresh (HIGH) [EOS Authority Block Producers, https://eosauthority.com/block-producers]
Voting Power: Proporsional stake (1 EOS staked = 1 vote weight); tidak ada quadratic voting atau delegasi representatif formal (HIGH) [EOSIO Technical Whitepaper, https://github.com/EOSIO/Documentation/blob/master/TechnicalWhitePaper.md]
Delegation: Tidak ada delegasi vote formal di protokol (token holder harus vote langsung); proxy voting tersedia via tooling komunitas (misalnya `eosio.proxy` contract) tapi bukan fitur native protokol (MEDIUM) [EOS Authority Proxy Voting, https://eosauthority.com/proxy]
Proposal System: On-chain proposals via `eosio.prods` / `eosio.forum` workflow; memerlukan 15/21 BP approval untuk eksekusi (hard fork, parameter change, treasury spend) (HIGH) [EOS Authority Proposals, https://eosauthority.com/proposals]
Treasury Governance: ENF treasury (akun `eosio.ef`/`eosio.fund`) dikelola ENF leadership (Yves La Rose + board) — tidak ada on-chain multisig proposal requirement untuk pengeluaran rutin; large spend mungkin memerlukan BP approval (detail tidak transparan) (MEDIUM) [CoinDesk ENF Launch, https://www.coindesk.com/business/2021/09/22/eos-community-launches-foundation-to-take-over-from-block-one/]
Status: Active (ongoing BP elections, periodic hard fork proposals)
Sources: (HIGH) [EOSIO Technical Whitepaper, https://github.com/EOSIO/Documentation/blob/master/TechnicalWhitePaper.md]; (HIGH) [EOS Authority Block Producers, https://eosauthority.com/block-producers]; (HIGH) [EOS Authority Proposals, https://eosauthority.com/proposals]; (MEDIUM) [CoinDesk ENF Launch, https://www.coindesk.com/business/2021/09/22/eos-community-launches-foundation-to-take-over-from-block-one/]

## Inflation / Deflation

Inflation Mechanism: Protocol-level minting via `eosio.system` contract — ~1% سنوي to Block Producers (paid per block proportional to votes), ~1% سنوي to ENF (paid to `eosio.ef`/`eosio.fund`), sisanya (awal 4%, sekarang variable) ke REX pool / savings / burned (HIGH) [eosio.system Contract, https://github.com/EOSIO/eos/blob/master/contracts/eosio.system/eosio.system.cpp]
Emission Schedule: Continuous per-block minting; total annual inflation target ~1-2% (tergantung parameter `continuous_rate` di `eosio.system` yang dapat diubah via BP proposal) (HIGH) [EOS Authority eosio.system State, https://eosauthority.com/contract/eosio.system]
Burn Mechanism: RAM market fee 0.5% per trade dikumpulkan di `eosio.ramfee` — histori: diburn periodik via proposal BP; tidak ada auto-burn per transaksi (HIGH) [EOSIO System Contract RAM Fee, https://github.com/EOSIO/eos/blob/master/contracts/eosio.system/eosio.system.cpp#L1150]
Buyback: Tidak ada program buyback resmi (HIGH) [EOS Network Foundation, https://eosnetwork.com/foundation/] (no mention in official docs)
Supply Reduction: Hanya via manual burn dari `eosio.ramfee` accumulation (ad-hoc, governance-dependent) — tidak ada mekanisme deflationary terprogram (EIP-1555 style) (MEDIUM) [EOS Authority Proposals, https://eosauthority.com/proposals]
Status: Inflationary (net supply increase ~1-2%/tahun setelah burn RAM fee minimal)
Sources: (HIGH) [eosio.system Contract, https://github.com/EOSIO/eos/blob/master/contracts/eosio.system/eosio.system.cpp]; (HIGH) [EOS Authority eosio.system, https://eosauthority.com/contract/eosio.system]; (MEDIUM) [EOS Authority Proposals, https://eosauthority.com/proposals]

## Holder Distribution

Top Holder Concentration: Block.one (vesting reserve) ~40M EOS terkunci + sudah claimed ~60M EOS (total 100M initial) = ~8.9% supply; Top 10 accounts (termasuk exchange wallets, BP accounts, bridge contracts) mengontrol ~30-40% supply (estimasi on-chain) (MEDIUM) [EOS Authority Richlist, https://eosauthority.com/token/eosio.token/EOS/holders]
Foundation Holding: ENF treasury balance di `eosio.ef`/`eosio.fund` — tidak dipublikasikan real-time; estimasi akumulasi inflasi 1%/tahun sejak Sep 2021 (~30-40M EOS) belum terverifikasi (LOW) [EOS Authority Account eosio.ef, https://eosauthority.com/account/eosio.ef] (balance visible but not officially confirmed as ENF treasury)
Investor Holding: Tidak ada investor VC/private sale — distribusi 100% publik ICO; exchange wallets (Binance, OKX, Upbit, dll) holding besar untuk custody pengguna (MEDIUM) [EOS Authority Richlist, https://eosauthority.com/token/eosio.token/EOS/holders]
Treasury Holding: Block.one treasury (dari ICO proceeds $4.1B) terpisah dari token supply; ENF treasury dari inflasi (lihat Foundation Holding) (HIGH) [SEC Complaint, https://www.sec.gov/litigation/complaints/2019/pr2019-197.pdf]
Community Holding: Partisipan ICO publik (900M initial) + secondary market buyers — estimasi 50-60% supply tersebar ke ribuan alamat (MEDIUM) [EOS Authority Richlist, https://eosauthority.com/token/eosio.token/EOS/holders]
Whale Concentration: Top 50 addresses mengontrol ~50%+ supply (termasuk exchange cold wallets, bridge contracts, BP accounts, Block.one) — Gini coefficient tinggi khas DPoS (MEDIUM) [EOS Authority Richlist, https://eosauthority.com/token/eosio.token/EOS/holders]
Sources: (MEDIUM) [EOS Authority Richlist, https://eosauthority.com/token/eosio.token/EOS/holders]; (MEDIUM) [EOS Authority Account eosio.ef, https://eosauthority.com/account/eosio.ef]; (HIGH) [SEC Complaint, https://www.sec.gov/litigation/complaints/2019/pr2019-197.pdf]

## Major Token Events

Date: 2017-06-26
Event: TGE Start / ICO Daily Auction Launch
Description: Block.one memulai distribusi token EOS ERC-20 via smart contract Ethereum; 2M EOS/hari selama 341 hari
Status: Completed
Related Historical Event ID: EV-002
Sources: (HIGH) [SEC Complaint, https://www.sec.gov/litigation/complaints/2019/pr2019-197.pdf]

Date: 2018-06-01
Event: TGE End / ICO Distribution Finalized
Description: Periode distribusi 341 hari berakhir; total 1B EOS ERC-20 terdistribusi (900M publik, 100M Block.one reserve)
Status: Completed
Related Historical Event ID: EV-008
Sources: (HIGH) [SEC Complaint, https://www.sec.gov/litigation/complaints/2019/pr2019-197.pdf]

Date: 2018-06-14
Event: Mainnet Genesis & Token Migration (Snapshot)
Description: EOS Mainnet diluncurkan oleh 21 BP; snapshot ERC-20 balances digunakan untuk genesis native token balances; ERC-20 frozen/bridge-only
Status: Completed
Related Historical Event ID: EV-009
Sources: (HIGH) [CoinDesk Mainnet Launch, https://www.coindesk.com/markets/2018/06/14/eos-mainnet-launches-after-block-producers-vote/]

Date: 2018-06-15
Event: Inflation & Voting Activation (eosio.system Go-Live)
Description: Kontrak `eosio.system` diaktifkan; inflasi 5%/tahun dimulai (1% BP, 4% savings); staking, voting, RAM market live
Status: Completed
Related Historical Event ID: EV-010
Sources: (HIGH) [EOSIO System Contract, https://github.com/EOSIO/eos/blob/master/contracts/eosio.system/eosio.system.cpp]

Date: 2019-09-30
Event: SEC Settlement — Block.one Penalty $24M
Description: Block.one menyelesaikan tuntutan SEC atas ICO tidak terdaftar; membayar $24M tanpa admit/deny; tidak memengaruhi token mechanics langsung tapi menciptakan regulatory overhang
Status: Completed
Related Historical Event ID: EV-013
Sources: (HIGH) [SEC Press Release, https://www.sec.gov/news/press-release/2019-197]

Date: 2019-11-01 (approx)
Event: REX (Resource Exchange) Launch
Description: Savings allocation (4% inflasi) dialihkan ke REX pool; token holder bisa deposit EOS ke REX untuk yield dari RAM fee & loan interest
Status: Completed
Related Historical Event ID: (not in Phase 3 — add if needed)
Sources: (HIGH) [EOSIO System Contract REX, https://github.com/EOSIO/eos/blob/master/contracts/eosio.system/eosio.system.cpp#L2000]

Date: 2021-09-22
Event: EOS Network Foundation (ENF) Formation & Inflation Redirect
Description: ENF dibentuk; proposal BP mengalihkan 1% inflasi tahunan dari `eosio.saving` ke `eosio.ef` (ENF treasury); total inflasi BP 1% + ENF 1% = 2% target
Status: Completed
Related Historical Event ID: EV-017
Sources: (HIGH) [CoinDesk ENF Launch, https://www.coindesk.com/business/2021/09/22/eos-community-launches-foundation-to-take-over-from-block-one/]

Date: 2022-04-01
Event: EOS EVM Mainnet Launch — New Utility
Description: EOS EVM live; EOS menjadi gas token untuk eksekusi EVM (mapped ke CPU/NET); memperluas utility ke Ethereum developer ecosystem
Status: Completed
Related Historical Event ID: EV-019
Sources: (HIGH) [EOS Network Foundation EOS EVM, https://eosnetwork.com/ecosystem/eos-evm/]

Date: 2022-06-14
Event: Spring Hard Fork / Leap 4.0 — RAM Market Reform
Description: Hard fork mengaktifkan Spring SDK, reformasi pasar RAM (parameter Bancor curve), dan perbaikan throughput; mempengaruhi biaya state storage
Status: Completed
Related Historical Event ID: EV-020
Sources: (HIGH) [GitHub Leap v4.0.0, https://github.com/AntelopeIO/leap/releases/tag/v4.0.0]

Date: 2023-09-01
Event: EOS Network Ventures Launch — Treasury Deployment
Description: ENF meluncurkan dana venture dari treasury inflasi untuk investasi ekosistem; menciptakan aliran keluar (outflow) dari treasury ke equity/token portfolio
Status: Ongoing
Related Historical Event ID: EV-024
Sources: (MEDIUM) [EOS Network Foundation, https://eosnetwork.com/foundation/]

Date: 2024-01-01
Event: Antelope Leap 5.0 — Resource Exhaustion Mitigation
Description: Upgrade konsensus & resource metering mengurangi vektor spam; stabilisasi biaya CPU/NET bagi pengguna
Status: Completed
Related Historical Event ID: EV-025
Sources: (HIGH) [GitHub Leap v5.0.0, https://github.com/AntelopeIO/leap/releases/tag/v5.0.0]

## Official Token Resources

Official Documentation: https://developers.eosnetwork.com/docs
Whitepaper: https://github.com/EOSIO/Documentation/blob/master/TechnicalWhitePaper.md
Governance: https://eosauthority.com/proposals
Explorer: https://eosq.app/ (official ENF); https://bloks.io/ (community)
Contract: https://eosauthority.com/contract/eosio.token (native); https://etherscan.io/token/0x86Fa049857E0209aa7D9e616F7eb3b3B78ECfdb0 (ERC-20)
GitHub: https://github.com/eosnetworkfoundation; https://github.com/AntelopeIO
Dashboard: https://eosauthority.com/token/eosio.token/EOS (token stats); https://eosauthority.com/contract/eosio.system (system params)

## Summary

Status: Live
Supply Type: Inflationary (~1-2% net annual after burns)
Total Supply: 1.124.025.822,5427 EOS (per 2024-12-01 on-chain)
Distribution Categories: Community (Public ICO) 90%, Team/Founders (Block.one) 10% (vesting 10yr), Foundation (ENF) 0% initial (receives 1%/yr inflation), Treasury 0% initial, Ecosystem 0% initial, Investors 0%, Advisors 0%
Utility Count: 8 (Staking CPU/NET, RAM Purchase, BP Voting, Governance Proposals, EOS EVM Gas, DeFi Collateral/Liquidity, Bridge Token, REX Yield)
Governance: On-chain Token-Weighted DPoS Voting + Off-chain Social Consensus for

## Ecosystem Intelligence
_ref: `docs/Ontology/Community.md`, `docs/Ontology/Ecosystem.md`_

PROJECT: EOS

## Ecosystem Position

Primary Sector: Layer 1 Blockchain / Smart Contract Platform (HIGH) [EOS Network Foundation, https://eosnetwork.com/]
Secondary Sector: EVM-Compatible Execution Environment (via EOS EVM) (HIGH) [EOS Network Foundation EOS EVM, https://eosnetwork.com/ecosystem/eos-evm/]
Primary Chain: EOS Mainnet (Antelope Protocol) (HIGH) [EOS Network Foundation, https://eosnetwork.com/]
Supported Chains: Ethereum (via ERC-20 bridge token 0x86Fa049857E0209aa7D9e616F7eb3b3B78ECfdb0), WAX (Antelope-based cross-chain bridge), other Antelope chains (Telos, UX Network) via IBC (experimental) (HIGH) [Etherscan EOS Token, https://etherscan.io/token/0x86Fa049857E0209aa7D9e616F7eb3b3B78ECfdb0; WAX Official, https://wax.io/; AntelopeIO IBC, https://github.com/AntelopeIO/leap/tree/main/contracts/eosio.ibc]
Sources: (HIGH) [EOS Network Foundation, https://eosnetwork.com/]; (HIGH) [EOS Network Foundation EOS EVM, https://eosnetwork.com/ecosystem/eos-evm/]; (HIGH) [Etherscan EOS Token, https://etherscan.io/token/0x86Fa049857E0209aa7D9e616F7eb3b3B78ECfdb0]; (MEDIUM) [WAX Official, https://wax.io/]; (MEDIUM) [AntelopeIO IBC, https://github.com/AntelopeIO/leap/tree/main/contracts/eosio.ibc]

## External Dependencies

Dependency Name: Antelope Protocol (Leap Node Software)
Dependency Type: Protocol
Purpose: Core consensus, networking, WASM runtime, dan system contracts (eosio.token, eosio.system) yang menjalankan EOS Mainnet
Criticality: Critical
Status: Live
Related Entity: Antelope Protocol (Leap Node Software)
Related Technology Component: Antelope Leap Node Software; eosio.system Contract; eosio.token Contract
Sources: (HIGH) [GitHub AntelopeIO/leap, https://github.com/AntelopeIO/leap]; (HIGH) [EOS Network Foundation, https://eosnetwork.com/ecosystem/]

Dependency Name: Block Producers (BP) Collective
Dependency Type: Validator Group
Purpose: Block production, consensus finality (BFT-DPoS), governance voting, protocol upgrade execution
Criticality: Critical
Status: Live
Related Entity: Block Producers (BP) Collective
Related Technology Component: Block Producer (BP) Nodes; eosio.system Contract voting logic
Sources: (HIGH) [EOS Authority Block Producers, https://eosauthority.com/block-producers]; (HIGH) [EOSIO Technical Whitepaper, https://github.com/EOSIO/Documentation/blob/master/TechnicalWhitePaper.md]

Dependency Name: Ethereum Mainnet (Bridge Contract)
Dependency Type: Chain / Bridge
Purpose: Host ERC-20 representation of EOS (0x86Fa049857E0209aa7D9e616F7eb3b3B78ECfdb0) untuk cross-chain liquidity, CEX deposit/withdrawal, DeFi composability
Criticality: High
Status: Live
Related Entity: Etherscan
Related Technology Component: eosio.token Contract (native); Bridge Contract 0x86Fa... (Ethereum)
Sources: (HIGH) [Etherscan EOS Token, https://etherscan.io/token/0x86Fa049857E0209aa7D9e616F7eb3b3B78ECfdb0]; (MEDIUM) [EOS Network Foundation Bridge, https://eosnetwork.com/ecosystem/]

Dependency Name: Hyperion History API (EOS Rio)
Dependency Type: Infrastructure / Data Provider
Purpose: Full-history indexing dan query API untuk explorer, wallet, dApp analytics; standar resmi ENF sejak 2023
Criticality: High
Status: Live
Related Entity: Hyperion History API
Related Technology Component: Hyperion History API; ElasticSearch backend; Node.js API layer
Sources: (HIGH) [GitHub eosrio/hyperion, https://github.com/eosrio/hyperion]; (HIGH) [EOS Network Foundation Ecosystem, https://eosnetwork.com/ecosystem/]

Dependency Name: Firehose (StreamingFast)
Dependency Type: Infrastructure / Data Provider
Purpose: Real-time structured block streaming (gRPC/Protobuf) dengan latensi sub-sekon untuk dApp sync dan analytics; direkomendasikan ENF 2024
Criticality: High
Status: Live
Related Entity: Firehose (StreamingFast)
Related Technology Component: Firehose (StreamingFast); Go gRPC server; Flatbuffers schema
Sources: (HIGH) [StreamingFast Firehose, https://streamingfast.io/firehose]; (HIGH) [EOS Network Foundation Ecosystem, https://eosnetwork.com/ecosystem/]

Dependency Name: Anchor Wallet (Greymass)
Dependency Type: Wallet / SDK
Purpose: Non-custodial signing, resource management, dApp browser, session management (Anchor Link/Wharf Kit) untuk end-user access
Criticality: High
Status: Live
Related Entity: Anchor Wallet
Related Technology Component: Anchor Link (TypeScript); Wharf Kit (TypeScript); Wallet desktop/mobile app
Sources: (HIGH) [Anchor Wallet, https://greymass.com/anchor]; (HIGH) [EOS Network Foundation Ecosystem, https://eosnetwork.com/ecosystem/]

Dependency Name: Wombat Wallet
Dependency Type: Wallet
Purpose: Mobile/web non-custodial wallet dengan dApp store, NFT gallery, fiat on-ramp integration
Criticality: Medium
Status: Live
Related Entity: Wombat Wallet
Related Technology Component: Wombat Wallet app; Web3 provider injection
Sources: (MEDIUM) [Wombat Wallet, https://wombat.app/]; (MEDIUM) [EOS Network Foundation Ecosystem, https://eosnetwork.com/ecosystem/]

Dependency Name: GitHub (Microsoft)
Dependency Type: Cloud / Infrastructure
Purpose: Hosting repositori resmi (AntelopeIO/leap, eosnetworkfoundation/*), CI/CD (GitHub Actions), issue tracking, release distribution
Criticality: High
Status: Live
Related Entity: GitHub (Microsoft)
Related Technology Component: GitHub Actions workflows; Docker image publishing; Release artifacts
Sources: (HIGH) [GitHub AntelopeIO, https://github.com/AntelopeIO]; (HIGH) [GitHub EOS Network Foundation, https://github.com/eosnetworkfoundation]

Dependency Name: Docker Hub
Dependency Type: Cloud / Infrastructure
Purpose: Distribusi Docker images resmi untuk nodeos, Hyperion, Firehose, EOS EVM — digunakan BP dan operator infrastruktur
Criticality: Medium
Status: Live
Related Entity: Docker Hub
Related Technology Component: Docker images (nodeos, hyperion, firehose, eos-evm)
Sources: (MEDIUM) [Docker Hub AntelopeIO, https://hub.docker.com/u/antelopeio]; (MEDIUM) [Docker Hub EOS Rio, https://hub.docker.com/u/eosrio]

Dependency Name: ElasticSearch / OpenSearch
Dependency Type: Infrastructure / Data Provider
Purpose: Backend storage untuk Hyperion History API (full-history indexing); required untuk query performance
Criticality: High
Status: Live
Related Entity: ElasticSearch / OpenSearch
Related Technology Component: Hyperion History API ElasticSearch indices
Sources: (MEDIUM) [GitHub eosrio/hyperion Architecture, https://github.com/eosrio/hyperion/blob/master/docs/architecture.md]

Dependency Name: Google Cloud / AWS / Cloud Providers (BP Infrastructure)
Dependency Type: Cloud
Purpose: Sebagian besar 21 Block Producer aktif menjalankan node di cloud provider (AWS, Google Cloud, DigitalOcean, bare metal) — single-point-of-failure risk jika terkonsentrasi
Criticality: High
Status: Live
Related Entity: Block Producers (BP) Collective
Related Technology Component: Block Producer (BP) Nodes hosting
Sources: (MEDIUM) [EOS Authority BP Infrastructure Survey (community), https://eosauthority.com/block-producers] (verification needed for current provider breakdown)

Dependency Name: CertiK / Halborn / Trail of Bits / PeckShield / OpenZeppelin
Dependency Type: Security
Purpose: Historical audit partners untuk konsensus, WASM runtime, EOS EVM, Spring SDK; tidak ada continuous audit program terverifikasi
Criticality: Medium
Status: Live (periodic)
Related Entity: CertiK; Halborn; Trail of Bits; PeckShield; OpenZeppelin
Related Technology Component: Antelope Leap consensus; EOS EVM contracts; Spring SDK toolchain
Sources: (HIGH) [Trail of Bits EOSIO Audit, https://github.com/trailofbits/publications/blob/master/reviews/EOSIO.pdf]; (MEDIUM) [CertiK EOS EVM Audit, https://www.certik.com/projects/eos-evm]; (MEDIUM) [Halborn Antelope Audit, https://halborn.com/audits/antelope]; (LOW) [OpenZeppelin Blog, https://blog.openzeppelin.com/antelope-spring-sdk-audit]

Dependency Name: Cayman Islands Jurisdiction
Dependency Type: Government / Legal
Purpose: Inkorporasi Block.one dan EOS Network Foundation; kerangka hukum operasional, treasury, governance
Criticality: High
Status: Live
Related Entity: Cayman Islands Jurisdiction
Related Technology Component: Legal entity structure; Foundation bylaws
Sources: (HIGH) [Block.one Terms of Use, https://block.one/terms-of-use/]; (HIGH) [EOS Network Foundation, https://eosnetwork.com/foundation/]

Dependency Name: U.S. Securities and Exchange Commission (SEC)
Dependency Type: Government / Regulatory
Purpose: Regulatory oversight dari settlement 2019; memengaruhi status hukum token EOS di AS, exchange listing, institutional custody
Criticality: High
Status: Live (ongoing regulatory exposure)
Related Entity: U.S. Securities and Exchange Commission (SEC)
Related Technology Component: Token classification risk; Exchange delisting risk
Sources: (HIGH) [SEC Press Release, https://www.sec.gov/news/press-release/2019-197]; (HIGH) [SEC Complaint, https://www.sec.gov/litigation/complaints/2019/pr2019-197.pdf]

## Major Integrations

Integration Name: EOS EVM (Ethereum-Compatible Execution)
Integrated With: Ethereum Virtual Machine (EVM) ecosystem — Solidity/Vyper contracts, Hardhat/Foundry/Truffle tooling, MetaMask (via RPC), Ethereum JSON-RPC standard
Purpose: Memungkinkan deployment kontrak Ethereum asli di atas EOS Mainnet dengan gas fee mapped ke EOS CPU/NET; interoperabilitas ERC-20 native via precompiles
Status: Live
Related Historical Event ID: EV-019
Sources: (HIGH) [EOS Network Foundation EOS EVM, https://eosnetwork.com/ecosystem/eos-evm/]; (HIGH) [GitHub eosnetworkfoundation/eos-evm, https://github.com/eosnetworkfoundation/eos-evm]

Integration Name: Hyperion History API (Official Indexing Standard)
Integrated With: EOS Mainnet (Antelope Leap nodeos) — consumes block data via ship protocol / state-history plugin
Purpose: Menyediakan REST/GraphQL API untuk full-history query (transactions, actions, accounts, tokens) ke explorer, wallet, dApp
Status: Live
Related Historical Event ID: EV-022
Sources: (HIGH) [GitHub eosrio/hyperion, https://github.com/eosrio/hyperion]; (HIGH) [EOS Network Foundation Ecosystem, https://eosnetwork.com/ecosystem/]

Integration Name: Firehose Real-Time Streaming (StreamingFast)
Integrated With: EOS Mainnet (Antelope Leap nodeos) — consumes block stream via Firehose-enabled nodeos plugin
Purpose: Sub-second structured block streaming (gRPC/Protobuf) untuk real-time dApp sync, analytics, MEV monitoring
Status: Live
Related Historical Event ID: EV-026
Sources: (HIGH) [StreamingFast Firehose, https://streamingfast.io/firehose]; (HIGH) [EOS Network Foundation Ecosystem, https://eosnetwork.com/ecosystem/]

Integration Name: Spring SDK (C++ Smart Contract Framework)
Integrated With: Antelope Leap WASM runtime (wavm/wabt); CMake/Clang/LLVM toolchain; C++20 standard library
Purpose: Modern toolkit untuk compile, test, deploy smart contract C++ ke WASM; menggantikan CDT legacy
Status: Live
Related Historical Event ID: EV-021
Sources: (HIGH) [GitHub eosnetworkfoundation/spring, https://github.com/eosnetworkfoundation/spring]; (HIGH) [EOS Network Foundation Ecosystem, https://eosnetwork.com/ecosystem/]

Integration Name: WAX Bridge (Cross-Chain NFT/GameFi)
Integrated With: WAX (Worldwide Asset eXchange) — Antelope-based chain dengan bridge contract untuk token/NFT transfer
Purpose: Interoperabilitas aset (token, NFT) antara EOS dan WAX untuk GameFi (Ultra) dan marketplace
Status: Live
Related Historical Event ID: (Not explicitly in Phase 3 — referenced in Phase 1 Ecosystem)
Sources: (MEDIUM) [WAX Official, https://wax.io/]; (MEDIUM) [Ultra.io, https://ultra.io/]; (MEDIUM) [EOS Network Foundation Ecosystem, https://eosnetwork.com/ecosystem/]

Integration Name: Anchor Link / Wharf Kit (dApp Integration SDK)
Integrated With: Anchor Wallet (Greymass); EOS Mainnet RPC endpoints; TypeScript/JavaScript build systems
Purpose: Session management, transaction signing, identity (SIWE-style), resource provider abstraction untuk dApp developer
Status: Live
Related Historical Event ID: (Not explicitly in Phase 3)
Sources: (HIGH) [Anchor Wallet, https://greymass.com/anchor]; (HIGH) [Wharf Kit GitHub, https://github.com/wharfkit]

Integration Name: ERC-20 Bridge Token (Ethereum)
Integrated With: Ethereum Mainnet (ERC-20 standard); CEX/DEX liquidity pools (Uniswap, Binance, OKX); Multichain bridges (Wormhole, etc. — unverified)
Purpose: Representasi EOS di Ethereum untuk trading, DeFi collateral, cross-chain liquidity
Status: Live
Related Historical Event ID: EV-002 (TGE start), EV-009 (Mainnet snapshot)
Sources: (HIGH) [Etherscan EOS Token, https://etherscan.io/token/0x86Fa049857E0209aa7D9e616F7eb3b3B78ECfdb0]; (MEDIUM) [EOS Network Foundation Bridge, https://eosnetwork.com/ecosystem/]

Integration Name: Antelope IBC (Inter-Blockchain Communication)
Integrated With: Other Antelope chains (Telos, UX Network, WAX) via eosio.ibc contract
Purpose: Trust-minimized cross-chain messaging dan token transfer antar chain Antelope
Status: Beta / Experimental
Related Historical Event ID: (Not in Phase 3 — referenced in Phase 4 Architecture)
Sources: (MEDIUM) [AntelopeIO IBC Contract, https://github.com/AntelopeIO/leap/tree/main/contracts/eosio.ibc]

Integration Name: Defibox DeFi Protocol Integration
Integrated With: EOS Mainnet (native WASM contracts); EOS EVM (potential future)
Purpose: AMM DEX, lending, stablecoin (USN) — largest DeFi TVL di EOS; menggunakan EOS sebagai base pair dan collateral
Status: Live
Related Historical Event ID: (Not in Phase 3)
Sources: (MEDIUM) [Defibox, https://defibox.com/]; (MEDIUM) [DappRadar EOS, https://dappradar.com/rankings/protocol/eos]

Integration Name: OrganicSwap DEX Integration
Integrated With: EOS Mainnet (native WASM contracts)
Purpose: AMM DEX fokus stablecoin pairing dan token ekosistem; kontributor likuiditas DeFi
Status: Live
Related Historical Event ID: (Not in Phase 3)
Sources: (MEDIUM) [OrganicSwap, https://organicswap.io/]; (MEDIUM) [DappRadar EOS, https://dappradar.com/rankings/protocol/eos]

Integration Name: Ultra GameFi Platform Integration
Integrated With: EOS Mainnet / Antelope tech stack; WAX bridge untuk NFT interoperability
Purpose: Platform penerbitan game blockchain; menggunakan EOS/Antelope untuk asset ownership, marketplace, token economy
Status: Live
Related Historical Event ID: (Not in Phase 3)
Sources: (MEDIUM) [Ultra.io, https://ultra.io/]; (MEDIUM) [EOS Network Foundation Ecosystem, https://eosnetwork.com/ecosystem/]

Integration Name: EOS Network Ventures (Ecosystem Fund Deployment)
Integrated With: ENF Treasury (inflation-funded); Portfolio projects (equity/token investments)
Purpose: Strategic capital deployment ke early-stage DeFi, GameFi, infrastructure projects di ekosistem EOS/EOS EVM
Status: Live (Ongoing)
Related Historical Event ID: EV-024
Sources: (MEDIUM) [EOS Network Foundation, https://eosnetwork.com/foundation/]; (LOW) [EOS Network Foundation Blog, https://eosnetwork.com/blog/]

## Infrastructure Providers

Provider: Hyperion History API (EOS Rio)
Service: Full-history indexing (ElasticSearch backend), REST/GraphQL API untuk on-chain data query
Criticality: High
Status: Live
Sources: (HIGH) [GitHub eosrio/hyperion, https://github.com/eosrio/hyperion]; (HIGH) [EOS Network Foundation Ecosystem, https://eosnetwork.com/ecosystem/]

Provider: Firehose (StreamingFast)
Service: Real-time structured block streaming (gRPC/Protobuf/Flatbuffers), sub-second latency, cursor-based sync
Criticality: High
Status: Live
Sources: (HIGH) [StreamingFast Firehose, https://streamingfast.io/firehose]; (HIGH) [EOS Network Foundation Ecosystem, https://eosnetwork.com/ecosystem/]

Provider: EOS Authority
Service: Block explorer (eosq.app — official ENF), BP voting tooling, on-chain analytics, contract ABI explorer, proposal dashboard
Criticality: High
Status: Live
Sources: (HIGH) [EOS Authority, https://eosauthority.com/]; (HIGH) [EOS Network Foundation Block Explorers, https://eosnetwork.com/block-explorers/]

Provider: Bloks.io (HiveBP / EOS Cafe Block)
Service: Community block explorer untuk EOS dan chain Antelope lain; token analytics, account lookup, transaction debug
Criticality: Medium
Status: Live
Sources: (MEDIUM) [Bloks.io, https://bloks.io/]; (MEDIUM) [EOS Network Foundation Block Explorers, https://eosnetwork.com/block-explorers/]

Provider: Anchor Wallet (Greymass)
Service: Non-custodial wallet (desktop/mobile), Anchor Link SDK, Wharf Kit, resource provider, dApp browser
Criticality: High
Status: Live
Sources: (HIGH) [Anchor Wallet, https://greymass.com/anchor]; (HIGH) [EOS Network Foundation Ecosystem, https://eosnetwork.com/ecosystem/]

Provider: Wombat Wallet
Service: Mobile/web non-custodial wallet, dApp store, NFT gallery, fiat on-ramp (MoonPay/Transak), Web3 provider
Criticality: Medium
Status: Live
Sources: (MEDIUM) [Wombat Wallet, https://wombat.app/]; (MEDIUM) [EOS Network Foundation Ecosystem, https://eosnetwork.com/ecosystem/]

Provider: Block Producers (BP) Collective — 21 Active + Standbys
Service: Block production, consensus validation, BFT finality signatures, network governance, protocol upgrade execution
Criticality: Critical
Status: Live
Sources: (HIGH) [EOS Authority Block Producers, https://eosauthority.com/block-producers]; (HIGH) [EOSIO Technical Whitepaper, https://github.com/EOSIO/Documentation/blob/master/TechnicalWhitePaper.md]

Provider: GitHub (Microsoft)
Service: Source code hosting, CI/CD (Actions), release distribution, issue tracking, documentation wiki
Criticality: High
Status: Live
Sources: (HIGH) [GitHub AntelopeIO, https://github.com/AntelopeIO]; (HIGH) [GitHub EOS Network Foundation, https://github.com/eosnetworkfoundation]

Provider: Docker Hub
Service: Container image registry untuk nodeos, Hyperion, Firehose, EOS EVM official images
Criticality: Medium
Status: Live
Sources: (MEDIUM) [Docker Hub AntelopeIO, https://hub.docker.com/u/antelopeio]; (MEDIUM) [Docker Hub EOS Rio, https://hub.docker.com/u/eosrio]

Provider: Cloud Providers (AWS, Google Cloud, DigitalOcean, Bare Metal — BP operated)
Service: Hosting infrastructure untuk Block Producer nodes, API endpoints, Hyperion/Firehose instances
Criticality: High
Status: Live
Sources: (MEDIUM) [EOS Authority BP Infrastructure Survey (community), https://eosauthority.com/block-producers] (verification needed)

## Exchange Ecosystem

Exchange: Binance
Listing Status: Listed
Spot: Yes (EOS/USDT, EOS/BTC, EOS/BNB, EOS/BUSD, dll)
Perpetual: Yes (EOSUSDT Perpetual)
OTC: Yes (Binance OTC desk)
Launchpool: No (historical Launchpad 2017 — not Launchpool)
Status: Active
Sources: (HIGH) [Binance EOS Markets, https://www.binance.com/en/trade/EOS_USDT]; (HIGH) [CoinMarketCap EOS Markets, https://coinmarketcap.com/currencies/eos/markets/]

Exchange: OKX
Listing Status: Listed
Spot: Yes (EOS/USDT, EOS/BTC, EOS/ETH)
Perpetual: Yes (EOS-USDT-SWAP)
OTC: Yes (OKX OTC)
Launchpool: No
Status: Active
Sources: (HIGH) [OKX EOS Markets, https://www.okx.com/trade/EOS-USDT]; (HIGH) [CoinMarketCap EOS Markets, https://coinmarketcap.com/currencies/eos/markets/]

Exchange: Upbit
Listing Status: Listed
Spot: Yes (EOS/KRW, EOS/USDT, EOS/BTC)
Perpetual: No
OTC: No
Launchpool: No
Status: Active
Sources: (HIGH) [Upbit EOS Markets, https://upbit.com/exchange?code=CRIX.UPBIT.KRW-EOS]; (HIGH) [CoinMarketCap EOS Markets, https://coinmarketcap.com/currencies/eos/markets/]

Exchange: Coinbase
Listing Status: Listed
Spot: Yes (EOS/USD, EOS/USDC, EOS/EUR)
Perpetual: No (Coinbase International Exchange separate)
OTC: Yes (Coinbase Prime OTC)
Launchpool: No
Status: Active
Sources: (HIGH) [Coinbase EOS, https://www.coinbase.com/price/eos]; (HIGH) [CoinMarketCap EOS Markets, https://coinmarketcap.com/currencies/eos/markets/]

Exchange: Kraken
Listing Status: Listed
Spot: Yes (EOS/USD, EOS/EUR, EOS/USDT)
Perpetual: Yes (EOS/USD Futures on Kraken Futures)
OTC: Yes (Kraken OTC)
Launchpool: No
Status: Active
Sources: (HIGH) [Kraken EOS, https://trade.kraken.com/markets/kraken/eos/usd]; (HIGH) [CoinMarketCap EOS Markets, https://coinmarketcap.com/currencies/eos/markets/]

Exchange: Huobi / HTX
Listing Status: Listed
Spot: Yes (EOS/USDT, EOS/BTC, EOS/HT)
Perpetual: Yes (EOS-USDT Quarterly/Perpetual)
OTC: Yes
Launchpool: No
Status: Active
Sources: (HIGH) [HTX EOS Markets, https://www.htx.com/trade/eos_usdt]; (HIGH) [CoinMarketCap EOS Markets, https://coinmarketcap.com/currencies/eos/markets/]

Exchange: Gate.io
Listing Status: Listed
Spot: Yes (EOS/USDT, EOS/BTC, EOS/ETH)
Perpetual: Yes (EOS_USDT Perpetual)
OTC: No
Launchpool: No
Status: Active
Sources: (HIGH) [Gate.io EOS, https://www.gate.io/trade/EOS_USDT]; (HIGH) [CoinMarketCap EOS Markets, https://coinmarketcap.com/currencies/eos/markets/]

Exchange: KuCoin
Listing Status: Listed
Spot: Yes (EOS/USDT, EOS/BTC, EOS/ETH)
Perpetual: Yes (EOSUSDT Perpetual)
OTC: Yes (KuCoin OTC)
Launchpool: No
Status: Active
Sources: (HIGH) [KuCoin EOS, https://www.kucoin.com/trade/EOS-USDT]; (HIGH) [CoinMarketCap EOS Markets, https://coinmarketcap.com/currencies/eos/markets/]

Exchange: Bybit
Listing Status: Listed
Spot: Yes (EOS/USDT)
Perpetual: Yes (EOSUSDT Perpetual)
OTC: No
Launchpool: No
Status: Active
Sources: (HIGH) [Bybit EOS, https://www.bybit.com/trade/spot/EOS/USDT]; (HIGH) [CoinMarketCap EOS Markets, https://coinmarketcap.com/currencies/eos/markets/]

Exchange: Uniswap (Ethereum DEX)
Listing Status: Listed (via ERC-20 bridge token)
Spot: Yes (EOS/WETH, EOS/USDC, EOS/USDT pools on Ethereum mainnet)
Perpetual: No
OTC: No
Launchpool: No
Status: Active
Sources: (HIGH) [Uniswap EOS Pools, https://app.uniswap.org/explore/tokens/ethereum/0x86Fa049857E0209aa7D9e616F7eb3b3B78ECfdb0]; (HIGH) [Etherscan EOS Token, https://etherscan.io/token/0x86Fa049857E0209aa7D9e616F7eb3b3B78ECfdb0]

## Wallet Ecosystem

Wallet: Anchor Wallet (Greymass)
Support Type: Full (Native Antelope + EOS EVM via MetaMask Snap / custom RPC); Desktop (Win/Mac/Linux), Mobile (iOS/Android), Browser Extension
Status: Live
Sources: (HIGH) [Anchor Wallet, https://greymass.com/anchor]; (HIGH) [EOS Network Foundation Ecosystem, https://eosnetwork.com/ecosystem/]

Wallet: Wombat Wallet
Support Type: Full (Native Antelope + EOS EVM); Mobile (iOS/Android), Web, Browser Extension; dApp store, NFT gallery, fiat on-ramp
Status: Live
Sources: (MEDIUM) [Wombat Wallet, https://wombat.app/]; (MEDIUM) [EOS Network Foundation Ecosystem, https://eosnetwork.com/ecosystem/]

Wallet: MetaMask (via EOS EVM RPC / Snap)
Support Type: EOS EVM only (EVM-compatible RPC); tidak support native Antelope WASM contracts langsung
Status: Live
Sources: (HIGH) [EOS EVM Documentation Metamask, https://developers.eosnetwork.com/docs/eos-evm/metamask]; (HIGH) [MetaMask, https://metamask.io/]

Wallet: TokenPocket
Support Type: Full (Native Antelope multi-chain: EOS, WAX, Telos, BSC, Ethereum, etc.); Mobile, Desktop, Extension
Status: Live
Sources: (MEDIUM) [TokenPocket, https://www.tokenpocket.pro/]; (MEDIUM) [EOS Network Foundation Ecosystem, https://eosnetwork.com/ecosystem/]

Wallet: MathWallet
Support Type: Full (Native Antelope multi-chain); Mobile, Desktop, Extension, Hardware wallet integration
Status: Live
Sources: (MEDIUM) [MathWallet, https://mathwallet.org/]; (MEDIUM) [EOS Network Foundation Ecosystem, https://eosnetwork.com/ecosystem/]

Wallet: Ledger Hardware Wallet (via Anchor/TokenPocket/MathWallet)
Support Type: Cold storage signing untuk native Antelope (EOS) via Ledger App "EOS" (community maintained) + EOS EVM via Ethereum app
Status: Live
Sources: (MEDIUM) [Ledger EOS App, https://github.com/LedgerHQ/app-eos]; (MEDIUM) [Anchor Wallet Ledger Support, https://greymass.com/anchor]

Wallet: Trezor Hardware Wallet
Support Type: Native Antelope (EOS) via Trezor Firmware + third-party bridge (Trezor Connect); EOS EVM via Ethereum app
Status: Live
Sources: (MEDIUM) [Trezor EOS Support, https://wiki.trezor.io/Coins:_EOS]; (MEDIUM) [Trezor Connect, https://github.com/trezor/connect]

Wallet: Scatter (Legacy / Deprecated)
Support Type: Native Antelope (desktop) — tidak dipelihara aktif, digantikan Anchor
Status: Deprecated
Sources: (LOW) [Scatter GitHub (archived), https://github.com/GetScatter]; (MEDIUM) [EOS Network Foundation Ecosystem (no Scatter listed), https://eosnetwork.com/ecosystem/]

## Developer Ecosystem

SDK: Spring SDK (f.k.a. EOS SDK/CDT)
Description: Official C++20 smart contract framework (CMake, Clang/LLVM WASM target, integrated testing, ABI generation); replaces legacy CDT
Sources: (HIGH) [GitHub eosnetworkfoundation/spring, https://github.com/eosnetworkfoundation/spring]; (HIGH) [EOS Network Foundation Ecosystem, https://eosnetwork.com/ecosystem/]

SDK: EOS EVM Tooling (Hardhat / Foundry / Truffle compatible)
Description: Standard Ethereum development stack works out-of-the-box via EOS EVM JSON-RPC endpoint; Solidity 0.8+, Vyper support
Sources: (HIGH) [EOS EVM Documentation, https://developers.eosnetwork.com/docs/eos-evm]; (HIGH) [GitHub eosnetworkfoundation/eos-evm, https://github.com/eosnetworkfoundation/eos-evm]

SDK: Anchor Link / Wharf Kit (TypeScript)
Description: Transaction signing, session management, identity (SIWE), resource provider abstraction, dApp integration library untuk Antelope chains
Sources: (HIGH) [Anchor Wallet, https://greymass.com/anchor]; (HIGH) [Wharf Kit GitHub, https://github.com/wharfkit]

SDK: EOSJS (Legacy JavaScript/TypeScript)
Description: Legacy RPC client untuk interaksi nodeos; masih dipakai komunitas tapi tidak dikembangkan aktif
Sources: (MEDIUM) [EOSJS GitHub, https://github.com/EOSIO/eosjs]; (

## Market Intelligence
_ref: `docs/Meta/Narratives.md`, `docs/Valuation/Competitors.md`, `docs/Meta/MarketCycles.md`_

PROJECT: EOS

## Market Category

Primary Category: Layer 1 Blockchain / Smart Contract Platform 
Sources: (HIGH) [EOS Network Foundation, https://eosnetwork.com/]; (HIGH) [CoinMarketCap, https://coinmarketcap.com/currencies/eos/]

Secondary Category: EVM-Compatible Execution Environment 
Sources: (HIGH) [EOS Network Foundation EOS EVM, https://eosnetwork.com/ecosystem/eos-evm/]

Sector: Blockchain Infrastructure 
Sources: (HIGH) [EOS Network Foundation, https://eosnetwork.com/]; (HIGH) [Messari, https://messari.io/asset/eos]

Sub-sector: DPoS Layer 1 with Native EVM Layer 
Sources: (HIGH) [EOS Network Foundation, https://eosnetwork.com/]; (HIGH) [AntelopeIO Leap, https://github.com/AntelopeIO/leap]

## Market Position

Project Stage: Mature 
Sources: (HIGH) [CoinDesk Mainnet Launch 2018, https://www.coindesk.com/markets/2018/06/14/eos-mainnet-launches-after-block-producers-vote/]; (HIGH) [EOS Network Foundation, https://eosnetwork.com/] (6+ years mainnet uptime since 2018-06-14)

Primary Competitors: Ethereum; Solana; Cardano; Avalanche; BNB Chain; Polygon; Tron; WAX; Telos 
Sources: (HIGH) [CoinMarketCap Categories, https://coinmarketcap.com/categories/view/smart-contract-platform/]; (MEDIUM) [Messari EOS Competitors, https://messari.io/asset/eos/competitors]; (HIGH) [EOS Network Foundation Ecosystem, https://eosnetwork.com/ecosystem/]

Market Segment: General-purpose smart contract platform targeting developers seeking high throughput, zero gas fees (via resource staking), and Ethereum compatibility via EOS EVM 
Sources: (HIGH) [EOS Network Foundation Developers, https://developers.eosnetwork.com/]; (HIGH) [EOS EVM Documentation, https://developers.eosnetwork.com/docs/eos-evm]

Geographic Focus: Global (Cayman Islands incorporated entities; worldwide community, BPs, and users) 
Sources: (HIGH) [Block.one Terms of Use, https://block.one/terms-of-use/]; (HIGH) [EOS Network Foundation, https://eosnetwork.com/foundation/]; (HIGH) [EOS Authority Block Producers, https://eosauthority.com/block-producers]

## Trading Markets

Exchange: Binance 
Spot: Yes (EOS/USDT, EOS/BTC, EOS/BNB, EOS/BUSD, EOS/ETH, EOS/EUR, EOS/TRY, EOS/USDC, EOS/FDUSD) 
Perpetual: Yes (EOSUSDT Perpetual, EOSUSDC Perpetual) 
Futures: Yes (Quarterly futures via Binance Futures) 
Options: Yes (Binance Options) 
OTC: Yes (Binance OTC Portal) 
Status: Active 
Sources: (HIGH) [Binance EOS Markets, https://www.binance.com/en/trade/EOS_USDT]; (HIGH) [CoinMarketCap EOS Markets, https://coinmarketcap.com/currencies/eos/markets/]

Exchange: OKX 
Spot: Yes (EOS/USDT, EOS/BTC, EOS/ETH, EOS/USDC) 
Perpetual: Yes (EOS-USDT-SWAP, EOS-USDC-SWAP) 
Futures: Yes (Quarterly futures) 
Options: Yes (OKX Options) 
OTC: Yes (OKX OTC) 
Status: Active 
Sources: (HIGH) [OKX EOS Markets, https://www.okx.com/trade/EOS-USDT]; (HIGH) [CoinMarketCap EOS Markets, https://coinmarketcap.com/currencies/eos/markets/]

Exchange: Upbit 
Spot: Yes (EOS/KRW, EOS/USDT, EOS/BTC) 
Perpetual: No 
Futures: No 
Options: No 
OTC: No 
Status: Active 
Sources: (HIGH) [Upbit EOS Markets, https://upbit.com/exchange?code=CRIX.UPBIT.KRW-EOS]; (HIGH) [CoinMarketCap EOS Markets, https://coinmarketcap.com/currencies/eos/markets/]

Exchange: Coinbase 
Spot: Yes (EOS/USD, EOS/USDC, EOS/EUR) 
Perpetual: No (Coinbase International Exchange separate) 
Futures: No 
Options: No 
OTC: Yes (Coinbase Prime OTC) 
Status: Active 
Sources: (HIGH) [Coinbase EOS, https://www.coinbase.com/price/eos]; (HIGH) [CoinMarketCap EOS Markets, https://coinmarketcap.com/currencies/eos/markets/]

Exchange: Kraken 
Spot: Yes (EOS/USD, EOS/EUR, EOS/USDT, EOS/ETH, EOS/XBT) 
Perpetual: Yes (EOS/USD Futures on Kraken Futures) 
Futures: Yes (Kraken Futures) 
Options: No 
OTC: Yes (Kraken OTC) 
Status: Active 
Sources: (HIGH) [Kraken EOS, https://trade.kraken.com/markets/kraken/eos/usd]; (HIGH) [CoinMarketCap EOS Markets, https://coinmarketcap.com/currencies/eos/markets/]

Exchange: Huobi / HTX 
Spot: Yes (EOS/USDT, EOS/BTC, EOS/HT, EOS/ETH) 
Perpetual: Yes (EOS-USDT Perpetual, Quarterly) 
Futures: Yes (Quarterly futures) 
Options: No 
OTC: Yes (HTX OTC) 
Status: Active 
Sources: (HIGH) [HTX EOS Markets, https://www.htx.com/trade/eos_usdt]; (HIGH) [CoinMarketCap EOS Markets, https://coinmarketcap.com/currencies/eos/markets/]

Exchange: Gate.io 
Spot: Yes (EOS/USDT, EOS/BTC, EOS/ETH, EOS/USDC) 
Perpetual: Yes (EOS_USDT Perpetual) 
Futures: No 
Options: No 
OTC: No 
Status: Active 
Sources: (HIGH) [Gate.io EOS, https://www.gate.io/trade/EOS_USDT]; (HIGH) [CoinMarketCap EOS Markets, https://coinmarketcap.com/currencies/eos/markets/]

Exchange: KuCoin 
Spot: Yes (EOS/USDT, EOS/BTC, EOS/ETH, EOS/USDC) 
Perpetual: Yes (EOSUSDT Perpetual) 
Futures: No 
Options: No 
OTC: Yes (KuCoin OTC) 
Status: Active 
Sources: (HIGH) [KuCoin EOS, https://www.kucoin.com/trade/EOS-USDT]; (HIGH) [CoinMarketCap EOS Markets, https://coinmarketcap.com/currencies/eos/markets/]

Exchange: Bybit 
Spot: Yes (EOS/USDT, EOS/USDC) 
Perpetual: Yes (EOSUSDT Perpetual, EOSUSDC Perpetual) 
Futures: Yes (Inverse/USDT futures) 
Options: Yes (Bybit Options) 
OTC: No 
Status: Active 
Sources: (HIGH) [Bybit EOS, https://www.bybit.com/trade/spot/EOS/USDT]; (HIGH) [CoinMarketCap EOS Markets, https://coinmarketcap.com/currencies/eos/markets/]

Exchange: Uniswap (Ethereum DEX) 
Spot: Yes (EOS/WETH, EOS/USDC, EOS/USDT pools on Ethereum mainnet via ERC-20 bridge token) 
Perpetual: No 
Futures: No 
Options: No 
OTC: No 
Status: Active 
Sources: (HIGH) [Uniswap EOS Pools, https://app.uniswap.org/explore/tokens/ethereum/0x86Fa049857E0209aa7D9e616F7eb3b3B78ECfdb0]; (HIGH) [Etherscan EOS Token, https://etherscan.io/token/0x86Fa049857E0209aa7D9e616F7eb3b3B78ECfdb0]

## Liquidity

Liquidity Source: CEX (Centralized Exchanges) 
Major Liquidity Venue: Binance (highest spot & perpetual volume), OKX, Upbit (KRW pair dominance), Coinbase (USD fiat on-ramp), Kraken, HTX, Bybit 
Status: Deep order books across top 10 CEXs; tight spreads on major pairs (EOS/USDT, EOS/BTC, EOS/KRW) 
Sources: (HIGH) [CoinMarketCap EOS Markets, https://coinmarketcap.com/currencies/eos/markets/]; (HIGH) [Kaiko EOS Liquidity Data (reference), https://www.kaiko.com/]

Liquidity Source: DEX (Decentralized Exchanges) 
Major Liquidity Venue: Defibox (native EOS Mainnet AMM — largest TVL), OrganicSwap (native EOS AMM), Uniswap V2/V3 (Ethereum ERC-20 bridge token) 
Status: Native DEX liquidity concentrated in EOS/USDT, EOS/USN, EOS/EOSDAC pairs; Ethereum DEX liquidity in EOS/WETH, EOS/USDC — lower depth vs CEX 
Sources: (MEDIUM) [Defibox, https://defibox.com/]; (MEDIUM) [OrganicSwap, https://organicswap.io/]; (HIGH) [Uniswap EOS Pools, https://app.uniswap.org/explore/tokens/ethereum/0x86Fa049857E0209aa7D9e616F7eb3b3B78ECfdb0]; (MEDIUM) [DappRadar EOS, https://dappradar.com/rankings/protocol/eos]

Liquidity Source: Bridge Liquidity 
Major Liquidity Venue: ERC-20 Bridge Token (0x86Fa049857E0209aa7D9e616F7eb3b3B78ECfdb0) on Ethereum — custodied by bridge operator (entity not publicly verified); WAX Bridge for cross-chain NFT/token transfer 
Status: Bridge token supply ~100M+ ERC-20 EOS (per Etherscan holders); redemption liquidity dependent on bridge operator solvency — no public proof-of-reserves 
Sources: (HIGH) [Etherscan EOS Token Holders, https://etherscan.io/token/0x86Fa049857E0209aa7D9e616F7eb3b3B78ECfdb0#balances]; (MEDIUM) [WAX Official Bridge, https://wax.io/]; (MEDIUM) [EOS Network Foundation Bridge, https://eosnetwork.com/ecosystem/]

## Adoption Metrics

Metric Name: TVL (Total Value Locked) 
Value: $45.2M (DefiLlama, 2024-12-01) 
Date: 2024-12-01 
Sources: (HIGH) [DefiLlama EOS, https://defillama.com/chain/EOS]; (MEDIUM) [DefiLlama EOS EVM, https://defillama.com/chain/EOS%20EVM]

Metric Name: Daily Active Addresses 
Value: ~15,000–25,000 (7-day moving average, native EOS Mainnet) 
Date: 2024-11-01 to 2024-11-30 
Sources: (MEDIUM) [EOS Authority Stats, https://eosauthority.com/network/stats]; (MEDIUM) [Token Terminal EOS, https://tokenterminal.com/terminal/projects/eos]

Metric Name: Daily Transactions 
Value: ~500,000–1,200,000 (native mainnet, includes voting/claims/transfers) 
Date: 2024-11-01 to 2024-11-30 
Sources: (MEDIUM) [EOS Authority Network Stats, https://eosauthority.com/network/stats]; (MEDIUM) [Blockchair EOS, https://blockchair.com/eos/stats]

Metric Name: Total Accounts Created 
Value: ~2.1M (cumulative since genesis) 
Date: 2024-12-01 
Sources: (MEDIUM) [EOS Authority Accounts, https://eosauthority.com/accounts]; (MEDIUM) [EOS Network Foundation, https://eosnetwork.com/]

Metric Name: Developer Count (Monthly Active) 
Value: ~120–180 (Electric Capital / ENF estimate) 
Date: 2024-Q3 
Sources: (MEDIUM) [Electric Capital Developer Report 2024, https://www.electriccapital.com/developer-report]; (LOW) [EOS Network Foundation Blog, https://eosnetwork.com/blog/] (verification needed)

Metric Name: 24h Spot Volume (Aggregated) 
Value: $150M–$300M (varies by market conditions) 
Date: 2024-11-30 
Sources: (HIGH) [CoinMarketCap EOS, https://coinmarketcap.com/currencies/eos/]; (HIGH) [CoinGecko EOS, https://www.coingecko.com/en/coins/eos]

Metric Name: 24h Perpetual Volume (Aggregated) 
Value: $500M–$1.5B (Binance, OKX, Bybit dominant) 
Date: 2024-11-30 
Sources: (HIGH) [CoinMarketCap EOS Markets, https://coinmarketcap.com/currencies/eos/markets/]; (HIGH) [Coinglass EOS Futures, https://www.coinglass.com/tv/Binance_EOSUSDT]

Metric Name: Bridge Volume (ERC-20 ↔ Native, 30d) 
Value: ~$20M–$50M (estimated via bridge contract flows — not officially tracked) 
Date: 2024-11-01 to 2024-11-30 
Sources: (LOW) [Etherscan Bridge Contract Txns, https://etherscan.io/token/0x86Fa049857E0209aa7D9e616F7eb3b3B78ECfdb0]; (LOW) [Dune Analytics EOS Bridge (community dashboard), https://dune.com/] (verification needed)

Metric Name: Block Producer Count 
Value: 21 Active + ~50 Standby (rotating via vote) 
Date: 2024-12-01 
Sources: (HIGH) [EOS Authority Block Producers, https://eosauthority.com/block-producers]; (HIGH) [EOSIO Technical Whitepaper, https://github.com/EOSIO/Documentation/blob/master/TechnicalWhitePaper.md]

Metric Name: EOS EVM Daily Transactions 
Value: ~5,000–20,000 (since 2022 launch) 
Date: 2024-11-01 to 2024-11-30 
Sources: (MEDIUM) [EOS EVM Explorer, https://explorer.eosevm.io/]; (MEDIUM) [DappRadar EOS EVM, https://dappradar.com/rankings/protocol/eos-evm]

## Market Share

Metric: Layer 1 TVL Share (vs Ethereum, Solana, BNB, Tron, Avalanche, Polygon, Cardano) 
Value: <0.1% (DefiLlama ranking ~35th by TVL) 
Date: 2024-12-01 
Sources: (HIGH) [DefiLlama Chains Ranking, https://defillama.com/chains]; (HIGH) [DefiLlama EOS, https://defillama.com/chain/EOS]

Metric: Spot Trading Volume Share (vs top 100 assets) 
Value: ~0.3%–0.5% (ranked ~40–60 by 24h volume) 
Date: 2024-11-30 
Sources: (HIGH) [CoinMarketCap Rankings, https://coinmarketcap.com/rankings/]; (HIGH) [CoinGecko Rankings, https://www.coingecko.com/en/coins/eos]

Metric: Developer Market Share (Electric Capital) 
Value: ~0.5%–0.8% of total crypto monthly active developers 
Date: 2024-Q3 
Sources: (MEDIUM) [Electric Capital Developer Report 2024, https://www.electriccapital.com/developer-report]

Metric: Perpetual Open Interest Share 
Value: ~0.2%–0.4% of aggregate crypto perpetual OI 
Date: 2024-11-30 
Sources: (MEDIUM) [Coinglass Aggregated OI, https://www.coinglass.com/]; (LOW) [Bybit/OKX/Binance API aggregated — not officially published]

## Competitor Landscape

Competitor: Ethereum 
Category: Layer 1 Smart Contract Platform (PoS) 
Difference: Ethereum uses PoS with L2 scaling (rollups); EOS uses DPoS with native EVM layer (EOS EVM) and resource staking model (no gas fees) 
Market Segment: General-purpose, DeFi, NFTs, institutional adoption 
Sources: (HIGH) [Ethereum.org, https://ethereum.org/]; (HIGH) [EOS Network Foundation EOS EVM, https://eosnetwork.com/ecosystem/eos-evm/]

Competitor: Solana 
Category: Layer 1 High-Throughput Blockchain (PoH/PoS) 
Difference: Solana optimizes for single-shard high TPS via parallel Sealevel runtime; EOS uses DPoS with WASM + EVM layer, resource staking, and 0.5s block time 
Market Segment: High-frequency trading, DeFi, consumer apps, memecoins 
Sources: (HIGH) [Solana.com, https://solana.com/]; (HIGH) [EOS Network Foundation, https://eosnetwork.com/]

Competitor: BNB Chain 
Category: Layer 1 EVM-Compatible (PoSA) 
Difference: BNB Chain is EVM-native with centralized validator set (21 active); EOS has native WASM + EOS EVM layer, DPoS with vote decay, and on-chain governance 
Market Segment: DeFi, GameFi, Binance ecosystem integration 
Sources: (HIGH) [BNB Chain, https://www.bnbchain.org/]; (HIGH) [EOS Network Foundation, https://eosnetwork.com/]

Competitor: Polygon 
Category: Layer 2 / Sidechain Scaling for Ethereum (PoS) 
Difference: Polygon is Ethereum-aligned scaling (PoS, zkEVM, CDK); EOS is independent L1 with own consensus and native EVM layer 
Market Segment: Ethereum scaling, DeFi, gaming, enterprise 
Sources: (HIGH) [Polygon.technology, https://polygon.technology/]; (HIGH) [EOS Network Foundation EOS EVM, https://eosnetwork.com/ecosystem/eos-evm/]

Competitor: Avalanche 
Category: Layer 1 Multi-Chain (PoS, Subnets) 
Difference: Avalanche uses subnet architecture for custom chains; EOS uses single mainnet with EVM layer and Antelope IBC for cross-chain 
Market Segment: DeFi, enterprise subnets, gaming 
Sources: (HIGH) [Avalanche, https://www.avalabs.org/]; (MEDIUM) [AntelopeIO IBC, https://github.com/AntelopeIO/leap/tree/main/contracts/eosio.ibc]

Competitor: Cardano 
Category: Layer 1 UTXO-Based Smart Contract Platform (PoS) 
Difference: Cardano uses eUTXO model and Plutus (Haskell); EOS uses account-based WASM/EVM with C++/Solidity 
Market Segment: DeFi, identity, government partnerships 
Sources: (HIGH) [Cardano.org, https://cardano.org/]; (HIGH) [EOS Network Foundation, https://eosnetwork.com/]

Competitor: Tron 
Category: Layer 1 DPoS Smart Contract Platform (EVM-Compatible) 
Difference: Tron is EVM-native DPoS with high stablecoin volume (USDT); EOS has native WASM + EOS EVM, resource staking, and Antelope protocol 
Market Segment: Stablecoin transfers, DeFi, content/media 
Sources: (HIGH) [Tron.network, https://tron.network/]; (HIGH) [EOS Network Foundation, https://eosnetwork.com/]

Competitor: WAX 
Category: Layer 1 Antelope-Based (DPoS) Focused on NFT/GameFi 
Difference: WAX is purpose-built for NFT/GameFi with custom tooling; EOS is general-purpose with EOS EVM and broader DeFi 
Market Segment: NFT, GameFi, collectibles, WAX Cloud Wallet users 
Sources: (HIGH) [WAX Official, https://wax.io/]; (HIGH) [EOS Network Foundation Ecosystem, https://eosnetwork.com/ecosystem/]

Competitor: Telos 
Category: Layer 1 Antelope-Based (DPoS) with EVM (tEVM) 
Difference: Telos launched native EVM (tEVM) earlier (2021); EOS launched EOS EVM 2022; both share Antelope codebase but separate governance/token 
Market Segment: DeFi, EVM dApps, governance experiments 
Sources: (HIGH) [Telos.net, https://www.telos.net/]; (HIGH) [EOS Network Foundation EOS EVM, https://eosnetwork.com/ecosystem/eos-evm/]

## Narrative Position

Narrative: EVM-Compatible Layer 1 (Native EVM Layer) 
Status: Main Narrative 
Evidence: EOS EVM live since 2022-04-01 (EV-019); marketed as "Ethereum compatibility with EOS performance"; Solidity/Vyper deployment via standard tooling (Hardhat/Foundry) 
Sources: (HIGH) [EOS Network Foundation EOS EVM, https://eosnetwork.com/ecosystem/eos-evm/]; (HIGH) [EOS Network Foundation Blog, https://eosnetwork.com/blog/]

Narrative: DPoS Governance & On-Chain Upgradability 
Status: Main Narrative 
Evidence: Continuous BP voting since 2018-06-15 (EV-010); 10+ coordinated hard forks (Dawn 1-4, Mainnet, EOSIO 1.0, Leap 3.1/4.0/5.0); on-chain proposals via eosio.system 
Sources: (HIGH) [EOS Authority Proposals, https://eosauthority.com/proposals]; (HIGH) [GitHub AntelopeIO/leap Releases, https://github.com/AntelopeIO/leap/releases]

Narrative: WebAssembly (WASM) Smart Contracts with C++ SDK (Spring) 
Status: Secondary Narrative 
Evidence: Spring SDK released 2022 (EV-021); C++20, CMake, integrated testing; positioned as performant alternative to Solidity 
Sources: (HIGH) [GitHub eosnetworkfoundation/spring, https://github.com/eosnetworkfoundation/spring]; (HIGH) [EOS Network Foundation Ecosystem, https://eosnetwork.com/ecosystem/]

Narrative: GameFi / NFT (via Ultra, WAX Bridge) 
Status: Secondary Narrative 
Evidence: Ultra platform on Antelope/EOS tech; WAX bridge for NFT interoperability; ENF ecosystem page lists gaming projects 
Sources: (MEDIUM) [Ultra.io, https://ultra.io/]; (MEDIUM) [WAX Official, https://wax.io/]; (MEDIUM) [EOS Network Foundation Ecosystem, https://eosnetwork.com/ecosystem/]

Narrative: DeFi (Defibox, OrganicSwap, REX Yield) 
Status: Secondary Narrative 
Evidence: Defibox largest TVL on EOS; REX resource exchange yields; EOS EVM enabling Ethereum DeFi migration 
Sources: (MEDIUM) [Defibox, https://defibox.com/]; (MEDIUM) [OrganicSwap, https://organicswap.io/]; (HIGH) [EOSIO System Contract REX, https://github.com/EOSIO/eos/blob/master/contracts/eosio.system/eosio.system.cpp#L2000]

Narrative: Modular / Interoperability (Antelope IBC) 
Status: Emerging / Experimental Narrative 
Evidence: eosio.ibc contract exists in Leap; not widely adopted in production; roadmap mentions horizontal scaling via sidechains 
Sources: (MEDIUM) [AntelopeIO IBC Contract, https://github.com/AntelopeIO/leap/tree/main/contracts/eosio.ibc]; (MEDIUM) [EOS Network Foundation Roadmap 2024, https://eosnetwork.com/]

Narrative: Zero-Knowledge / ZK Integration (Leap 6.0 Roadmap) 
Status: Future / Planned Narrative 
Evidence: Leap 6.0 (planned 202

## Behavioral Intelligence
_ref: `docs/Ontology/Hidden.md` — enriches DecisionEvent Alternatives/Reason/Reactions_

PROJECT: EOS

1. Menjadi Layer 1 berperforma tinggi dengan kompatibilitas EVM native untuk menarik pengembang Ethereum
· Evidence: Peluncuran EOS EVM (EV-019) memungkinkan deployment kontrak Solidity/Vyper asli di atas EOS Mainnet dengan gas fee yang dipetakan ke CPU/NET staking; Spring SDK (EV-021) menyediakan toolkit C++20 modern untuk kontrak native WASM
· Supporting Dataset: Phase 3 EV-019, EV-021; Phase 4 Architecture, Execution Environment, Development Framework

2. Mencapai desentralisasi progresif melalui transisi dari Block.one ke EOS Network Foundation (ENF) dan governance on-chain DPoS
· Evidence: Pembentukan ENF (EV-017) mengalihkan pengendalian protokol dari Block.one ke komunitas; alokasi inflasi 1%/tahun ke ENF via eosio.system; voting BP berkelanjutan sejak 2018 (EV-010)
· Supporting Dataset: Phase 3 EV-010, EV-015, EV-016, EV-017, EV-018; Phase 2 Entities (ENF, Block.one, BP Collective); Phase 6 Governance

3. Membangun treasury berkelanjutan melalui inflasi protokol (1%/tahun ke ENF) dan mengurangi ketergantungan pada dana ICO Block.one
· Evidence: eosio.system mengalokasikan 1% inflasi tahunan ke akun `eosio.ef`/`eosio.fund` untuk ENF sejak Sep 2021; Block.one tidak lagi mendanai pengembangan pasca-2021
· Supporting Dataset: Phase 3 EV-017; Phase 5 Revenue Model, Financial Dependencies; Phase 6 Inflation/Deflation

4. Memperluas ekosistem DeFi dan GameFi melalui insentif likuiditas, venture fund (EOS Network Ventures), dan integrasi cross-chain (WAX, Ethereum bridge)
· Evidence: Peluncuran EOS Network Ventures (EV-024) untuk investasi strategis; Defibox dan OrganicSwap sebagai DeFi utama; Ultra dan WAX bridge untuk GameFi/NFT; kampanye "EOS Hot Sauce" (EV-023)
· Supporting Dataset: Phase 3 EV-023, EV-024; Phase 7 Major Integrations, Developer Ecosystem; Phase 8 Narrative Position

5. Menjaga keamanan dan stabilitas jaringan melalui upgrade bertahap (Leap 3.1→4.0→5.0→6.0) dan audit berkala komponen kritis
· Evidence: Rilis Leap 3.1 (EV-018), Leap 4.0/Spring (EV-020), Leap 5.0 (EV-025), Leap 6.0 planned (EV-029); audit Trail of Bits (2018), CertiK (2022 EOS EVM), Halborn (2023 Leap), OpenZeppelin (2024 Spring SDK)
· Supporting Dataset: Phase 3 EV-018, EV-020, EV-025, EV-029; Phase 4 Technical Upgrade History, Audit History, Known Technical Limitations

Keputusan: Meluncurkan ICO tahunan permissionless di Ethereum (2017-06-26 hingga 2018-06-01)
· Trigger: Butuh kapital masif untuk membangun protokol EOSIO dari nol dan mendanai Block.one sebagai entitas pengembang awal
· Evidence: SEC Complaint vs Block.one menunjukkan $4.1M dibangun via daily auction 341 hari; 900M EOS ke publik, 100M ke Block.one reserve
· Decision: Mengadakan distribusi token EOS ERC-20 melalui smart contract Ethereum tanpa KYC/whitelist, harga ditentukan pasar harian
· Immediate Result: Terkumpul ~$4.1B (ICO terbesar masa itu); 1B EOS ERC-20 tersebar ke ribuan peserta; Block.one mendapatkan treasury besar untuk pengembangan
· Long-term Impact: Menciptakan distribusi token yang luas (community-owned) tapi juga menimbulkan risiko regulator SEC (penyelesaian $24M, EV-013); Block.one reserve 100M EOS vesting 10 tahun menciptakan overhang supply hingga 2028
· Supporting Dataset: Phase 3 EV-002, EV-008, EV-013; Phase 5 Funding History, Token Sale; Phase 6 Distribution, Vesting Schedule, Major Token Events

Keputusan: Meluncurkan Mainnet oleh Block Producers terpilih, bukan Block.one (2018-06-14)
· Trigger: Block.one menegaskan tidak akan memproduksi blok genesis; komunitas BP harus memulai jaringan
· Evidence: CoinDesk melaporkan 21 BP terpilih menghasilkan blok genesis setelah voting on-chain; Block.one menyerahkan kode sumber ke komunitas
· Decision: Transisi kendali jaringan dari Block.one ke BP Collective secara instan pada genesis
· Immediate Result: EOS Mainnet live dengan 21 BP aktif; token migrasi dari ERC-20 ke native via snapshot
· Long-term Impact: Menetapkan preseden governance on-chain sejak hari pertama; BP menjadi penentu arah protokol (hard fork, parameter), mengurangi kekuasaan Block.one
· Supporting Dataset: Phase 3 EV-009, EV-010; Phase 2 Entity (BP Collective); Phase 4 Consensus Mechanism, System Architecture

Keputusan: Rebranding EOSIO menjadi Antelope Protocol dan pemindahan repositori ke AntelopeIO (2021-03)
· Trigger: Keluarnya Dan Larimer dari Block.one (EV-015) dan keinginan komunitas memisahkan identitas protokol dari Block.one
· Evidence: Repositori dipindah ke github.com/AntelopeIO/leap; nama protokol berganti dari EOSIO ke Antelope; ENF dibentuk 6 bulan kemudian (EV-017)
· Decision: Mengganti nama perangkat lunak node dan protokol dasar menjadi "Antelope" untuk netralitas vendor
· Immediate Result: Protokol tidak lagi terikat merek Block.one; pengembangan dibuka untuk kontributor komunitas di bawah ENF
· Long-term Impact: Memungkinkan ENF memimpin pengembangan Leap 3.1+ tanpa izin Block.one; tapi status kepemilikan IP/lisensi antara Block.one dan ENF tetap tidak jelas (Open Thread)
· Supporting Dataset: Phase 3 EV-015, EV-016; Phase 2 Entity (Antelope Protocol); Phase 4 System Architecture, Core Components

Keputusan: Membentuk EOS Network Foundation (ENF) sebagai entitas non-profit pengelola jaringan (2021-09-22)
· Trigger: Vacuum kepemimpinan pasca-Dan Larimer; komunitas dan BP mendorong entitas mandiri untuk mengelola treasury dan pengembangan
· Evidence: CoinDesk melaporkan peluncuran ENF dipimpin Yves La Rose; proposal BP mengalihkan 1% inflasi tahunan ke `eosio.ef`
· Decision: Mendirikan yayasan di Cayman Islands dengan mandat pengembangan protokol, pertumbuhan ekosistem, operasi, dan pengelolaan treasury
· Immediate Result: ENF menerima aliran dana inflasi 1%/tahun; mulai merekrut tim engineering/growth/operations (~30+ orang)
· Long-term Impact: ENF menjadi pusat keputusan strategis (roadmap, grants, ventures, upgrade); namun treasury dan pengeluaran tidak transparan on-chain real-time
· Supporting Dataset: Phase 3 EV-017; Phase 2 Entity (ENF, Yves La Rose); Phase 5 Treasury, Revenue Model, Financial Dependencies; Phase 6 Inflation/Deflation

Keputusan: Meluncurkan EOS EVM sebagai execution environment kompatibel Ethereum di atas Mainnet (2022-04-01)
· Trigger: Kebutuhan menarik pengembang Ethereum (Solidity/Vyper) dan likuiditas DeFi Ethereum ke ekosistem EOS
· Evidence: ENF meluncurkan EOS EVM berbasis go-ethereum/revm berjalan sebagai WASM contract; audit CertiK 2022; JSON-RPC kompatibel Ethereum standard
· Decision: Membangun EVM layer native di atas Antelope WASM runtime, bukan sidechain terpisah
· Immediate Result: Pengembang bisa deploy kontrak Ethereum asli ke EOS dengan Hardhat/Foundry; gas fee dipetakan ke CPU/NET stake
· Long-term Impact: Memperluas addressable market ke Ethereum developer ecosystem; tapi adopsi EOS EVM masih relatif rendah (~5k-20k tx/hari vs ~500k-1.2M native)
· Supporting Dataset: Phase 3 EV-019; Phase 4 Execution Environment, Core Components; Phase 7 Major Integrations (EOS EVM); Phase 8 Narrative Position

Keputusan: Hard Fork "Spring" / Leap 4.0 dengan reformasi RAM market dan Spring SDK (2022-06-14)
· Trigger: Masalah biaya RAM volatil dan toolkit pengembang (CDT) usang menghambat adopsi
· Evidence: Leap 4.0 mengaktifkan Spring SDK (C++20, CMake, testing terintegrasi) dan perbaikan parameter Bancor curve untuk RAM market
· Decision: Upgrade protokol terkoordinasi BP+ENF untuk memperkenalkan SDK modern dan ekonomi RAM yang direvisi
· Immediate Result: Spring SDK jadi standard pengembangan baru; biaya RAM distabilisasi; throughput meningkat
· Long-term Impact: Meningkatkan developer experience (DX) signifikan; tapi fragmentasi tooling (CDT legacy vs Spring vs EOSJS vs Anchor Link) tetap ada
· Supporting Dataset: Phase 3 EV-020, EV-021; Phase 4 Technical Upgrade History, Development Framework, Known Technical Limitations

Keputusan: Mengadopsi Hyperion History API sebagai standar indexing resmi dan Firehose untuk real-time streaming (2023-03, 2024-03)
· Trigger: Kebutuhan infrastruktur data andal untuk explorer, wallet, dApp analytics; Hyperion dari EOS Rio terbukti production-grade
· Evidence: ENF mengintegrasikan Hyperion ke infrastruktur resmi (EV-022); merekomendasikan Firehose (StreamingFast) sebagai standar real-time (EV-026)
· Decision: Menetapkan Hyperion (full history) + Firehose (real-time) sebagai dual indexing standard resmi ENF
· Immediate Result: Ketersediaan data on-chain historis dan real-time terstandarisasi untuk seluruh ekosistem
· Long-term Impact: Mengurangi fragmentasi penyedia data; tapi ketergantungan pada dua provider eksternal (EOS Rio, StreamingFast) menciptakan risiko sentralisasi infrastruktur
· Supporting Dataset: Phase 3 EV-022, EV-026; Phase 4 Core Components, Current Technical Stack; Phase 7 Infrastructure Providers, External Dependencies

Keputusan: Meluncurkan EOS Network Ventures (dana venture dari treasury ENF) (2023-09-01)
· Trigger: Treasury ENF mengumpulkan EOS dari inflasi 1%/tahun; kebutuhan deploy kapital ke proyek ekosistem strategis
· Evidence: ENF mengumumkan program venture fund (EV-024); ukuran dana dan portofolio tidak dipublikasikan
· Decision: Mengalokasikan sebagian treasury untuk investasi equity/token ke startup DeFi, GameFi, infrastruktur di EOS/EOS EVM
· Immediate Result: Pendanaan awal untuk startup ekosistem; portofolio investasi mulai terbentuk
· Long-term Impact: Menciptakan alignment insentif antara ENF dan proyek portofolio; tapi risiko kerugian modal venture tinggi dan tidak ada transparency reporting
· Supporting Dataset: Phase 3 EV-024; Phase 5 Revenue Model (EOS Network Ventures), Financial Risk; Phase 7 Major Integrations (EOS Network Ventures)

Evolution Pattern
Dari 2017-2018: Fase "Block.one-Driven" — Block.one mendanai ($4.1B ICO), mengembangkan protokol (Dawn 1-4, EOSIO 1.0), meluncurkan mainnet, dan mengendalikan arah teknis. Governance on-chain (DPoS) dirancang tapi Block.one memegang 10% supply (100M EOS) dengan vesting 10 tahun.
2019-2020: Fase "Eksperimen Aplikasi Block.one" — Block.one membangun Voice (media sosial) di atas EOS tapi gagal dan ditutup 2020 (EV-012, EV-014). SEC settlement $24M (EV-013) menciptakan regulatory overhang. Komunitas mulai frustrasi dengan ketidakberdayaan Block.one.
2021: Fase "Transisi Komunitas" — Dan Larimer keluar (EV-015); rebranding ke Antelope Protocol (EV-016) memisahkan identitas teknis dari Block.one; ENF dibentuk (EV-017) sebagai entitas pengelola baru dengan mandat inflasi 1%/tahun. Block.one mundur dari peran aktif.
2022: Fase "Ekspansi Teknis & EVM" — EOS EVM diluncurkan (EV-019) membawa kompatibilitas Ethereum; Spring Hard Fork/Leap 4.0 (EV-020) dan Spring SDK (EV-021) memodernisasi tooling; reformasi RAM market.
2023: Fase "Pematangan Infrastruktur & Dana" — Hyperion jadi standar indexing resmi (EV-022); kampanye komunitas "Hot Sauce" (EV-023); EOS Network Ventures diluncurkan (EV-024) untuk deploy treasury.
2024: Fase "Skala & ZK Roadmap" — Leap 5.0 (EV-025) perbaikan performa/keamanan; Firehose standar real-time (EV-026); roadmap 2024-2025 mencakup horizontal scaling, ZK integration (EV-027); Leap 6.0 development (EV-029).

Pola 1: Modular Architecture dengan Layer Terpisah (Native WASM + EVM Layer)
· Decision Pattern: Memisahkan execution environment native (WASM/C++) dari EVM-compatible layer (EOS EVM) yang berjalan sebagai smart contract di atas native layer, bukan sidechain terpisah
· Evidence: Arsitektur Phase 4 menunjukkan Antelope Leap (WASM runtime) sebagai base layer; EOS EVM di-deploy sebagai kontrak WASM native dengan precompiles untuk interoperabilitas; gas mapping ke CPU/NET
· Supporting Dataset: Phase 4 System Architecture, Execution Environment, Core Components; Phase 3 EV-019, EV-020

Pola 2: Upgrade Bertahap melalui Hard Fork Terkoordinasi BP-ENF
· Decision Pattern: Semua upgrade protokol mayor (Dawn 1-4, EOSIO 1.0, Leap 3.1/4.0/5.0) dilakukan via hard fork yang memerlukan koordinasi 15/21 BP + proposal ENF; tidak ada on-chain automatic upgrade mechanism
· Evidence: Phase 3 timeline menunjukkan 10+ hard fork terkoordinasi; Phase 4 Consensus Mechanism: BFT finality memerlukan 15/21 signatures; upgrade via `eosio.prods` schedule change
· Supporting Dataset: Phase 3 EV-004 through EV-011, EV-018, EV-020, EV-025; Phase 4 Consensus Mechanism, Technical Upgrade History

Pola 3: Resource Model Stake-Based (CPU/NET) + RAM Market Algorithmic (Bancor)
· Decision Pattern: Menghilangkan gas fee per transaksi; mengganti dengan model staking token untuk bandwidth (CPU/NET) dan pasar algoritmik untuk state storage (RAM)
· Evidence: Phase 4 Resource Model, System Architecture; Phase 6 Utility (Staking CPU/NET, RAM Purchase); Phase 3 EV-010 (aktivasi eosio.system)
· Supporting Dataset: Phase 4 Resource Model, System Architecture; Phase 6 Utility; Phase 3 EV-010

Pola 4: Parallel Execution Terbatas (Inter-block Scheduling, Bukan Intra-block)
· Decision Pattern: Paralelisme dicapai via scheduling transaksi antar blok (0.5s block time, 21 BP round-robin), bukan eksekusi paralel dalam satu blok (seperti Sealevel Solana)
· Evidence: Phase 4 Known Technical Limitations: "Single-threaded transaction execution per block"; Phase 3 EV-029 (Leap 6.0 roadmap menciona "parallel execution engine improvements" sebagai masa depan)
· Supporting Dataset: Phase 4 Known Technical Limitations, Current Technical Stack; Phase 3 EV-029

Pola 5: Audit Komponen Spesifik, Bukan Full Node Audit
· Decision Pattern: Audit keamanan difokuskan pada komponen terpisah (EOS EVM, Spring SDK, konsensus) oleh firma berbeda per periode, bukan audit komprehensif full codebase Leap
· Evidence: Phase 4 Audit History: Trail of Bits (2018 consensus/WASM), PeckShield (2018 launch), CertiK (2022 EOS EVM), Halborn (2023 Leap consensus/P2P), OpenZeppelin (2024 Spring SDK) — tidak ada audit full node 2023-2024
· Supporting Dataset: Phase 4 Audit History; Phase 4 Known Technical Limitations (Audit Coverage Gap)

Pola 1: Funding Utama via ICO Publik Tanpa Private Sale/VC
· Decision Pattern: Seluruh kapital awal ($4.1B) dikumpulkan via permissionless public sale 341 hari di Ethereum; tidak ada ronde private/seed/VC terpisah
· Evidence: Phase 5 Funding History: 1 ronde "Public Sale (ICO)" saja; Phase 6 Distribution: 90% Community (Public ICO), 10% Team (Block.one), 0% Investors/Advisors
· Supporting Dataset: Phase 5 Funding History, Fundraising Mechanism; Phase 6 Distribution, Token Sale

Pola 2: Treasury Berbasis Inflasi Protokol (1%/tahun ke ENF) Tanpa Diversifikasi Terverifikasi
· Decision Pattern: ENF mendanai operasional, grants, dan ventures sepenuhnya dari alokasi inflasi 1% tahunan (native EOS); tidak ada bukti diversifikasi ke stablecoin/aset lain atau revenue protocol fees
· Evidence: Phase 5 Revenue Model: "Protocol Inflation Allocation (1% annual to ENF)" sebagai revenue stream utama; Treasury: "Current Treasury Size: tidak diungkap"; Financial Risk: "Treasury Concentration — predominantly held in native EOS token"
· Supporting Dataset: Phase 5 Revenue Model, Treasury, Financial Risk; Phase 6 Inflation/Deflation; Phase 3 EV-017

Pola 3: Deploy Treasury ke Venture Fund (EOS Network Ventures) Tanpa Transparansi Portofolio
· Decision Pattern: ENF meluncurkan dana venture dari treasury inflasi untuk investasi strategis, tapi ukuran dana, kriteria investasi, dan portofolio tidak dipublikasikan
· Evidence: Phase 3 EV-024; Phase 5 Revenue Model (EOS Network Ventures Investment Returns: "Status: Planned/Early Stage, returns not yet realized or disclosed"); Financial Risk (EOS Network Ventures Capital Loss: "no public portfolio or performance data")
· Supporting Dataset: Phase 3 EV-024; Phase 5 Revenue Model, Financial Risk; Phase 7 Major Integrations (EOS Network Ventures)

Pola 4: Tidak Ada Program Buyback/Burn Terprogram (Hanya Ad-hoc RAM Fee Burn)
· Decision Pattern: Supply reduction hanya terjadi via manual burn akumulasi fee RAM 0.5% (governance-dependent), tidak ada mekanisme deflationary otomatis seperti EIP-1559
· Evidence: Phase 6 Inflation/Deflation: "Burn Mechanism: RAM market fee 0.5% per trade dikumpulkan di eosio.ramfee — histori: diburn periodik via proposal BP; tidak ada auto-burn"; "Buyback: Tidak ada program buyback resmi"
· Supporting Dataset: Phase 6 Inflation/Deflation; Phase 4 Core Components (eosio.system RAM market)

Pola 1: Integrasi "Dual Indexing Standard" (Hyperion Full History + Firehose Real-time) sebagai Keputusan Infrastruktur Kritis
· Decision Pattern: ENF menetapkan dua provider eksternal (EOS Rio untuk Hyperion, StreamingFast untuk Firehose) sebagai standar resmi indexing, menggantikan fragmentasi provider sebelumnya
· Evidence: Phase 3 EV-022 (Hyperion adoption 2023), EV-026 (Firehose recommendation 2024); Phase 7 Infrastructure Providers: Hyperion dan Firehose keduanya "Critical" status; External Dependencies: keduanya "High" criticality
· Supporting Dataset: Phase 3 EV-022, EV-026; Phase 7 Infrastructure Providers, External Dependencies; Phase 4 Core Components

Pola 2: Ekspansi Ekosistem via EVM Compatibility (EOS EVM) untuk Menarik Developer & Liquidity Ethereum
· Decision Pattern: Membangun EVM layer native (bukan sidechain/bridge) untuk memungkinkan deployment kontrak Ethereum asli dengan tooling standar (Hardhat/Foundry/MetaMask)
· Evidence: Phase 3 EV-019; Phase 4 Execution Environment (EOS EVM sebagai WASM contract); Phase 7 Major Integrations (EOS EVM integration dengan Ethereum tooling); Phase 8 Narrative Position (Main Narrative: "EVM-Compatible Layer 1")
· Supporting Dataset: Phase 3 EV-019; Phase 4 Execution Environment; Phase 7 Major Integrations; Phase 8 Narrative Position

Pola 3: Partnership Cross-Chain dengan Chain Antelope Lain (WAX, Telos) via IBC dan Bridge Khusus
· Decision Pattern: Memanfaatkan codebase Antelope bersama untuk interoperabilitas dengan WAX (NFT/GameFi bridge) dan Telos (tEVM), serta bridge ERC-20 ke Ethereum
· Evidence: Phase 7 Major Integrations (WAX Bridge, Antelope IBC); External Dependencies (Ethereum Bridge, WAX); Phase 8 Competitor Landscape (WAX, Telos sebagai competitor sekaligus partner)
· Supporting Dataset: Phase 7 Major Integrations, External Dependencies; Phase 8 Competitor Landscape

Pola 4: Dana Ekosistem (Grants + Ventures) untuk Stimulasi Supply-Side (Builder/Proyek) Bukan Demand-Side (User Incentive)
· Decision Pattern: ENF mengalokasikan treasury ke grants (builder) dan ventures (equity/token startup), bukan program insentif pengguna (airdrop, trading competition, staking reward tambahan)
· Evidence: Phase 5 Revenue Model (Grant Programs: "Outflow, not revenue"); Phase 3 EV-024 (EOS Network Ventures); Phase 7 Major Integrations (EOS Network Ventures); tidak ada program user incentive besar tercatat
· Supporting Dataset: Phase 5 Revenue Model; Phase 3 EV-024; Phase 7 Major Integrations

Pola 1: Governance On-Chain DPoS dengan Continuous Approval Voting + Vote Decay
· Decision Pattern: Token holder vote BP secara terus-menerus (1 EOS staked = 1 vote weight untuk 30 BP); vote decay ~50%/tahun memaksa refresh vote; top 21 BP aktif memproduksi blok
· Evidence: Phase 6 Governance: "Continuous Approval Voting", "Vote decay mengurangi kekuatan vote ~50%/tahun"; Phase 4 Consensus Mechanism: "21 active BP terpilih via continuous approval voting"; Phase 3 EV-010 (aktivasi voting)
· Supporting Dataset: Phase 6 Governance; Phase 4 Consensus Mechanism; Phase 3 EV-010

Pola 2: Upgrade Protokol Memerlukan Konsensus BP (15/21) + Proposal ENF — Bukan On-Chain Automatic
· Decision Pattern: Hard fork proposals diajukan via `eosio.prods`/`eosio.forum` workflow; memerlukan 15/21 BP approval untuk eksekusi; ENF memimpin persiapan teknis tapi BP memutuskan
· Evidence: Phase 6 Governance: "Proposal System: On-chain proposals via eosio.prods/eosio.forum workflow; memerlukan 15/21 BP approval"; Phase 4 Consensus Mechanism: "Upgrade Security: Hard fork terkoordinasi oleh 15/21 BP"
· Supporting Dataset: Phase 6 Governance; Phase 4 Consensus Mechanism; Phase 3 Technical Upgrade History (semua upgrade mayor)

Pola 3: Treasury Governance Terpusat di ENF Leadership (Yves La Rose + Board) Tanpa On-Chain Multisig Requirement untuk Pengeluaran Rutin
· Decision Pattern: ENF treasury (`eosio.ef`/`eosio.fund`) dikelola oleh kepemimpinan ENF; large spend mungkin butuh BP approval tapi detail tidak transparan; tidak ada proposal on-chain mandatory untuk setiap pengeluaran
· Evidence: Phase 6 Governance: "Treasury Governance: ENF treasury dikelola ENF leadership — tidak ada on-chain multisig proposal requirement untuk pengeluaran rutin"; Phase 5 Treasury: "Treasury Custodian: EOS Network Foundation (ENF) — multi-sig accounts managed by ENF leadership (detail tidak dipublikasikan)"
· Supporting Dataset: Phase 6 Governance; Phase 5 Treasury; Phase 2 Entity (Yves La Rose, ENF Core Team)

Pola 4: Proxy Voting Tersedia via Tooling Komunitas (eosio.proxy) Tapi Bukan Fitur Native Protokol
· Decision Pattern: Delegasi vote memungkinkan via smart contract proxy (community-built) tapi tidak dibangun ke dalam protokol core; token holder harus vote langsung atau gunakan proxy third-party
· Evidence: Phase 6 Governance: "Delegation: Tidak ada delegasi vote formal di protokol; proxy voting tersedia via tooling komunitas (misalnya eosio.proxy contract) tapi bukan fitur native protokol"
· Supporting Dataset: Phase 6 Governance

Pola 1: Respons Regulasi — Settlement SEC tanpa Admit/Deny, Lanjutkan Operasi
· Decision Pattern: Block.one memilih menyelesaikan tuntutan SEC ($24M penalty) tanpa mengakui atau menolak tuduhan, memungkinkan operasi berlanjut tanpa pengadilan panjang
· Evidence: Phase 3 EV-013; Phase 5 Financial Risk: "Regulatory/Legal Financial Risk — SEC settlement 2019 established precedent"; Phase 2 Entity (SEC)
· Trigger: SEC complaint vs Block.one atas penjualan token tidak terdaftar (2019)
· Response: Bayar denda $24M, tidak admit/deny, lanjutkan pengembangan protokol
· Result: Kasus tertutup; Block.one melanjutkan operasional; tapi regulatory overhang tetap ada untuk token EOS di AS (exchange delisting risk, custody issue)
· Supporting Dataset: Phase 3 EV-013; Phase 5 Financial Risk; Phase 2 Entity (SEC)

Pola 2: Respons Kegagalan Produk Flagship (Voice) — Tutup Cepat, Alokasikan Sumber Daya Kembali ke Protokol
· Decision Pattern: Block.one menutup Voice (media sosial) setelah <1 tahun operasional karena adopsi rendah dan biaya tinggi; tim/aset dialihkan
· Evidence: Phase 3 EV-012 (launch Voice beta 2019), EV-014 (tutup 2020); Phase 2 Entity (Voice: "Cancelled", "Status: Completed")
· Trigger: Voice gagal mencapai product-market fit; biaya operasional tinggi; Block.one fokus ke protokol
· Response: Shutdown platform; anuncement resmi Feb 2021; tim dialihkan
· Result: Komunitas kehilangan aplikasi showcase; Block.one mengonsentrasi sumber daya ke core protocol (tapi Larimer keluar sebulan kemudian)
· Supporting Dataset: Phase 3 EV-012, EV-014; Phase 2 Entity (Voice)

Pola 3: Respons Vacuum Kepemimpinan Teknis (Larimer Exit) — Rebranding Protokol + Bentuk Foundation Komunitas
· Decision Pattern: Keluarnya arsitek utama (Dan Larimer) memicu komunitas untuk merebrand protokol (EOSIO→Antelope) dan membentuk ENF sebagai entitas pengelola mandiri
· Evidence: Phase 3 EV-015 (Larimer exit Jan 2021), EV-016 (Rebrand Mar 2021), EV-017 (ENF formation Sep 2021)
· Trigger: Dan Larimer keluar dari Block.one Jan 2021
· Response: Komunitas+BP memutuskan rebranding ke Antelope (netral vendor); 6 bulan kemudian membentuk ENF dengan mandat inflasi 1%/tahun
· Result: Protokol berlanjut tanpa Larimer; ENF jadi pengembang utama; tapi status IP/lisensi Antelope antara Block.one dan ENF tidak jelas
· Supporting Dataset: Phase 3 EV-015, EV-016, EV-017; Phase 2 Entity (Dan Larimer, ENF, Antelope Protocol); Phase 4 System Architecture

Pola 4: Respons Teknis Resource Exhaustion/Spam — Upgrade Konsensus & Metering (Leap 5.0)
· Decision Pattern: Serangan resource exhaustion memicu upgrade Leap 5.0 dengan mitigasi vektor spam dan perbaikan konsensus BFT-DPoS
· Evidence: Phase 3 EV-025 (Leap 5.0 Jan 2024: "mitigasi vektor serangan resource exhaustion"); Phase 4 Known Technical Limitations: "Resource Exhaustion Protection: Stake-based CPU/NET allocation"; Technical Upgrade History
· Trigger: Vektor serangan resource exhaustion/spam di jaringan
· Response: Leap 5.0 dengan perbaikan consensus, metering, dan mitigasi exhaustion
· Result: BP upgrade node; jaringan lebih stabil di bawah beban tinggi
· Supporting Dataset: Phase 3 EV-025; Phase 4 Technical Upgrade History, Known Technical Limitations, Security Model

Pola 1: Transisi Bertahap dari Entity Pusat (Block.one) ke Foundation Komunitas (ENF) + BP Collective
· Evidence: 2017-2021: Block.one kendali penuh (ICO, dev, launch, Voice); 2021: Larimer exit → Antelope rebrand → ENF formation → inflasi redirect ke ENF; 2022-sekarang: ENF memimpin dev (Leap, EOS EVM, Spring SDK), BP Collective govern upgrade. Pola: stepwise decentralization melalui event krusial (founder exit, regulatory settlement, product failure)
· Supporting Dataset: Phase 3 EV-001 through EV-017; Phase 2 Entities (Block.one, ENF, BP Collective, Dan Larimer, Yves La Rose)

Pola 2: Upgrade Mayor Setiap ~1-2 Tahun Terkoordinasi ENF+BP (Dawn→EOSIO→Leap 3.1→4.0→5.0→6.0 planned)
· Evidence: 2018: Dawn 1-4 + Mainnet + EOSIO 1.0; 2021: Leap 3.1 (post-ENF); 2022: Leap 4.0/Spring; 2024: Leap 5.0; 2024-planned: Leap 6.0. Pola: major release ~tahunan setelah ENF terbentuk, didorong roadmap teknis ENF + konsensus BP
· Supporting Dataset: Phase 3 EV-004 through EV-011, EV-018, EV-020, EV-025, EV-029; Phase 4 Technical Upgrade History

Pola 3: Ekspansi Utility Token Melalui Layer Baru (Native→REX→EOS EVM) Bukan Mengubah Tokenomics Dasar
· Evidence: 2018: Staking CPU/NET + RAM + Voting; 2019: REX (Resource Exchange) yield; 2022: EOS EVM gas mapping. Tokenomics inti (inflasi 1% BP, 1% ENF) stabil sejak 2021; utility ditambah via layer/protocol baru tanpa mengubah supply mechanics
· Supporting Dataset: Phase 3 EV-010, EV-019; Phase 6 Utility (8 utility), Inflation/Deflation; Phase 4 Execution Environment

Pola 4: Ketergantungan Infrastruktur Kritis pada Provider Eksternal Tertentu (Hyperion: EOS Rio, Firehose: StreamingFast, BP Nodes: Cloud Providers)
· Evidence: Phase 7 External Dependencies: Hyperion (High, EOS Rio), Firehose (High, StreamingFast), BP Infrastructure (High, AWS/GCP/DO). Tidak ada alternatif resmi tertulis untuk provider ini; single points of failure
· Supporting Dataset: Phase 7 External Dependencies, Infrastructure Providers; Phase 4 Current Technical Stack

Pola 5: Narasi Utama Bergeser: "EOSIO/Killer Ethereum" (2017) → "Antelope/Community-Driven" (2021) → "EVM-Compatible L1 + WASM" (2022-sekarang)
· Evidence: Phase 8 Narrative Position: Main Narrative "EVM-Compatible Layer 1", "

## Knowledge Extraction
_ref: `docs/Patterns/*`, `docs/Reasoning/*` (rule candidates)_

PROJECT: EOS

## Core Insights

Insight 1: Transisi bertahap dari entitas sentral (Block.one) ke foundation komunitas (ENF) mendemonstrasikan pola desentralisasi proaktif yang dipicu oleh kepergian founder dan tekanan regulator
Explanation: EOS berevolusi dari Block.one yang mengontrol ICO $4.1B, pengembangan protokol (Dawn 1-4), dan peluncuran mainnet (EV-001–EV-009), menjadi ENF yang dibentuk 2021-09-22 (EV-017) setelah keluarnya Dan Larimer (EV-015) dan rebranding EOSIO→Antelope (EV-016). Transisi ini terjadi melalui proposal BP yang mengalihkan 1% inflasi tahunan ke `eosio.ef` (ENF treasury)【Phase 3 — EV-015】【Phase 3 — EV-016】【Phase 3 — EV-017】.
Evidence: Block.one mendominasi 2017-2021; Larimer keluar Jan 2021; Antelope rebrand Mar 2021; ENF formed Sep 2021 dengan mandat inflasi 1%/tahun【Phase 3 — EV-015】【Phase 3 — EV-016】【Phase 3 — EV-017】.
Supporting Dataset: Phase 3 History (EV-001 through EV-017), Phase 2 Entities (Block.one, ENF, Dan Larimer, Yves La Rose, BP Collective)
Confidence: HIGH

Insight 2: Arsitektur dual-layer (Native WASM + EOS EVM sebagai kontrak WASM native) memungkinkan kompatibilitas Ethereum tanpa mengorbankan konsensus DPoS atau resource model stake-based
Explanation: EOS EVM diluncurkan 2022-04-01 (EV-019) sebagai smart contract WASM native di atas Antelope Leap runtime, bukan sidechain terpisah. Gas fee dipetakan ke CPU/NET staking; precompiles menyediakan interoperabilitas native token, RAM, voting【Phase 4 — Execution Environment】【Phase 3 — EV-019】.
Evidence: EOS EVM live Apr 2022; berbasis go-ethereum/revm di WASM; JSON-RPC kompatibel Ethereum; gas mapping ke CPU/NET【Phase 4 — Execution Environment】【Phase 3 — EV-019】.
Supporting Dataset: Phase 4 Technology (System Architecture, Execution Environment, Core Components), Phase 3 EV-019
Confidence: HIGH

Insight 3: Model resource stake-based (CPU/NET) + RAM market algoritmik (Bancor) menghilangkan gas fee per-transaksi namun menciptakan friksi UX (staking, 72h unstaking, volatilitas harga RAM)
Explanation: Pengguna harus stake EOS untuk bandwidth CPU/NET (proporsional stake) dan beli RAM via pasar Bancor 0.5% fee. Unstaking butuh 72 jam. Model ini zero-gas tapi memerlukan kapital upfront dan manajemen resource aktif【Phase 4 — Resource Model】【Phase 6 — Utility】.
Evidence: Staking CPU/NET untuk bandwidth; RAM market Bancor algorithm; 72h cooldown unstaking; zero gas fee per tx【Phase 4 — Resource Model】【Phase 6 — Utility (Staking CPU/NET, RAM Purchase)】.
Supporting Dataset: Phase 4 Technology (Resource Model, System Architecture), Phase 6 Token (Utility, Inflation/Deflation)
Confidence: HIGH

Insight 4: Treasury ENF sepenuhnya bergantung pada inflasi protokol (1%/tahun native EOS) tanpa diversifikasi terverifikasi, menciptakan risiko konsentrasi dan ketergantungan harga token
Explanation: ENF menerima 1% inflasi tahunan via `eosio.system` sejak Sep 2021 (EV-017). Treasury size, komposisi (EOS vs stablecoin), dan alamat multi-sig tidak dipublikasikan real-time. Tidak ada revenue protocol fees, buyback, atau diversifikasi terverifikasi【Phase 5 — Revenue Model】【Phase 5 — Treasury】【Phase 5 — Financial Risk】.
Evidence: Revenue stream utama = Protocol Inflation Allocation 1% annual to ENF; Treasury size/composition tidak diungkap; Financial Risk: "Treasury Concentration — predominantly held in native EOS token"【Phase 5 — Revenue Model】【Phase 5 — Treasury】【Phase 5 — Financial Risk】.
Supporting Dataset: Phase 5 Financial (Revenue Model, Treasury, Financial Risk), Phase 6 Token (Inflation/Deflation), Phase 3 EV-017
Confidence: HIGH

Insight 5: Governance on-chain DPoS dengan continuous approval voting + vote decay (~50%/tahun) menciptakan accountability BP berkelanjutan tapi partisipasi token holder rendah historis
Explanation: 1 EOS staked = 1 vote weight untuk 30 BP; vote decay memaksa refresh berkala; top 21 BP aktif. Upgrade protokol butuh 15/21 BP approval via `eosio.prods` workflow. Treasury governance terpusat di ENF leadership tanpa on-chain multisig requirement rutin【Phase 6 — Governance】【Phase 4 — Consensus Mechanism】.
Evidence: Continuous approval voting; vote decay ~50%/yr; 15/21 BP untuk hard fork; ENF treasury managed by leadership tanpa on-chain proposal mandatory【Phase 6 — Governance】【Phase 4 — Consensus Mechanism】.
Supporting Dataset: Phase 6 Token (Governance), Phase 4 Technology (Consensus Mechanism), Phase 3 History (Technical Upgrade History)
Confidence: HIGH

Insight 6: Ekosistem bergantung kritis pada dua provider infrastruktur eksternal tunggal (Hyperion: EOS Rio, Firehose: StreamingFast) tanpa alternatif resmi tertulis
Explanation: ENF menetapkan Hyperion (full history) dan Firehose (real-time streaming) sebagai dual indexing standard resmi (EV-022, EV-026). Keduanya "Critical/High" criticality di External Dependencies. Tidak ada dokumentasi fallback atau provider alternatif resmi【Phase 7 — External Dependencies】【Phase 7 — Infrastructure Providers】.
Evidence: Hyperion (EOS Rio) adopted 2023-03; Firehose (StreamingFast) recommended 2024-03; keduanya "High/Critical" criticality; no official alternative documented【Phase 7 — External Dependencies】【Phase 7 — Infrastructure Providers】.
Supporting Dataset: Phase 7 Ecosystem (External Dependencies, Infrastructure Providers), Phase 3 EV-022, EV-026
Confidence: HIGH

Insight 7: Tokenomics inflasi net ~1-2%/tahun (1% BP, 1% ENF, sisanya REX/savings/burn) stabil sejak 2021; utility ditambah via layer baru (REX 2019, EOS EVM 2022) tanpa mengubah supply mechanics
Explanation: Inflasi 5% awal (1% BP, 4% savings) → REX launch 2019 mengalihkan savings ke yield pool → ENF formation 2021 redirect 1% ke ENF → target 2% total (1% BP + 1% ENF). Supply ~1.124B per Dec 2024. Tidak ada hard cap【Phase 6 — Inflation/Deflation】【Phase 3 — EV-010】【Phase 3 — EV-017】【Phase 3 — EV-019】.
Evidence: Initial 5% inflation (1% BP, 4% savings); REX 2019; ENF 1% redirect 2021; current ~1-2% net; supply 1.124B Dec 2024【Phase 6 — Inflation/Deflation】【Phase 3 — EV-010】【Phase 3 — EV-017】【Phase 3 — EV-019】.
Supporting Dataset: Phase 6 Token (Inflation/Deflation, Supply, Major Token Events), Phase 3 History (EV-010, EV-017, EV-019)
Confidence: HIGH

Insight 8: Audit keamanan difokuskan pada komponen terpisah (EOS EVM, Spring SDK, konsensus) oleh firma berbeda per periode, bukan audit komprehensif full node Leap 5.x/6.x
Explanation: Trail of Bits (2018 consensus/WASM), PeckShield (2018 launch), CertiK (2022 EOS EVM), Halborn (2023 Leap consensus/P2P), OpenZeppelin (2024 Spring SDK). Tidak ada audit full node 2023-2024【Phase 4 — Audit History】【Phase 4 — Known Technical Limitations (Audit Coverage Gap)】.
Evidence: 5 audit terverifikasi komponen spesifik; no comprehensive public audit for Leap 5.x/6.x full codebase【Phase 4 — Audit History】【Phase 4 — Known Technical Limitations】.
Supporting Dataset: Phase 4 Technology (Audit History, Known Technical Limitations)
Confidence: HIGH

Insight 9: Adopsi EOS EVM masih rendah (~5k-20k tx/hari) vs native mainnet (~500k-1.2M tx/hari) meski narasi utama "EVM-Compatible Layer 1"
Explanation: EOS EVM live Apr 2022 (EV-019) sebagai narasi utama (Phase 8 Narrative Position). Daily tx EOS EVM ~5k-20k vs native ~500k-1.2M (Nov 2024). TVL EOS Mainnet $45.2M (rank ~35th), EOS EVM TVL terpisah lebih kecil【Phase 8 — Adoption Metrics】【Phase 8 — Narrative Position】.
Evidence: EOS EVM tx 5k-20k/day vs native 500k-1.2M/day; TVL $45.2M rank ~35th; Main Narrative "EVM-Compatible Layer 1"【Phase 8 — Adoption Metrics】【Phase 8 — Narrative Position】.
Supporting Dataset: Phase 8 Market (Adoption Metrics, Narrative Position), Phase 3 EV-019
Confidence: HIGH

Insight 10: Distribusi token ICO permissionless 341 hari (90% publik, 10% Block.one vesting 10yr) menciptakan distribusi luas tapi Block.one reserve 100M EOS (vesting hingga 2028) menjadi supply overhang
Explanation: ICO 2017-06-26 s.d. 2018-06-01 (EV-002, EV-008): 900M ke publik via daily auction, 100M ke Block.one vesting 10M/tahun. Per 2024 ~60M unlocked, 40M terkunci hingga 2028. Tidak ada private sale/VC allocation【Phase 6 — Distribution】【Phase 6 — Vesting Schedule】【Phase 3 — EV-002】【Phase 3 — EV-008】.
Evidence: 90% public ICO, 10% Block.one 10yr vesting; ~60M unlocked 2018-2024, 40M locked until 2028; no private sale/VC【Phase 6 — Distribution】【Phase 6 — Vesting Schedule】【Phase 3 — EV-002】【Phase 3 — EV-008】.
Supporting Dataset: Phase 6 Token (Distribution, Vesting Schedule, Major Token Events), Phase 3 History (EV-002, EV-008)
Confidence: HIGH

## Strategic Principles

Principle 1: Modular Architecture dengan Layer Terpisah (Native WASM + EVM Layer)
Explanation: Memisahkan execution environment native (WASM/C++ via Spring SDK) dari EVM-compatible layer (EOS EVM) yang berjalan sebagai smart contract di atas native layer, bukan sidechain terpisah. Memungkinkan paralel development dan upgrade independen【Phase 4 — System Architecture】【Phase 4 — Execution Environment】【Phase 3 — EV-019】【Phase 3 — EV-020】.
Evidence: Antelope Leap (WASM runtime) base layer; EOS EVM deployed as WASM contract with precompiles; gas mapping ke CPU/NET【Phase 4 — System Architecture】【Phase 4 — Execution Environment】【Phase 3 — EV-019】【Phase 3 — EV-020】.
Supporting Dataset: Phase 4 Technology (System Architecture, Execution Environment, Core Components), Phase 3 History (EV-019, EV-020)
Confidence: HIGH

Principle 2: Upgrade Bertahap melalui Hard Fork Terkoordinasi BP-ENF
Explanation: Semua upgrade protokol mayor (Dawn 1-4, EOSIO 1.0, Leap 3.1/4.0/5.0) dilakukan via hard fork yang memerlukan koordinasi 15/21 BP + proposal ENF; tidak ada on-chain automatic upgrade mechanism. Pola: major release ~tahunan setelah ENF terbentuk【Phase 4 — Consensus Mechanism】【Phase 3 — Technical Upgrade History】.
Evidence: 10+ hard fork terkoordinasi; BFT finality butuh 15/21 signatures; upgrade via `eosio.prods` schedule change【Phase 4 — Consensus Mechanism】【Phase 3 — Technical Upgrade History】.
Supporting Dataset: Phase 4 Technology (Consensus Mechanism, Technical Upgrade History), Phase 3 History (EV-004 through EV-011, EV-018, EV-020, EV-025)
Confidence: HIGH

Principle 3: Resource Model Stake-Based (CPU/NET) + RAM Market Algorithmic (Bancor)
Explanation: Menghilangkan gas fee per transaksi; mengganti dengan model staking token untuk bandwidth (CPU/NET) dan pasar algoritmik untuk state storage (RAM). Menciptakan zero-gas UX tapi memerlukan kapital upfront dan manajemen resource aktif【Phase 4 — Resource Model】【Phase 6 — Utility】.
Evidence: Staking CPU/NET untuk bandwidth; RAM market Bancor algorithm; 0.5% fee per trade; zero gas fee per tx【Phase 4 — Resource Model】【Phase 6 — Utility (Staking CPU/NET, RAM Purchase)】.
Supporting Dataset: Phase 4 Technology (Resource Model, System Architecture), Phase 6 Token (Utility)
Confidence: HIGH

Principle 4: Desentralisasi Progresif melalui Transisi Entity (Block.one → Antelope/ENF → BP Collective)
Explanation: Stepwise decentralization: 2017-2021 Block.one kendali penuh → 2021 Larimer exit → Antelope rebrand (netral vendor) → ENF formation (mandat inflasi 1%) → BP Collective govern upgrade. Setiap tahap dipicu event krusial (founder exit, regulatory settlement, product failure)【Phase 3 — EV-001 through EV-017】【Phase 2 — Entities】.
Evidence: Block.one dominan 2017-2021; Larimer exit Jan 2021; Antelope rebrand Mar 2021; ENF formed Sep 2021 dengan inflasi 1%; BP Collective govern upgrade【Phase 3 — EV-015】【Phase 3 — EV-016】【Phase 3 — EV-017】【Phase 2 — Entities】.
Supporting Dataset: Phase 3 History (EV-001 through EV-017), Phase 2 Entities (Block.one, ENF, BP Collective, Dan Larimer, Yves La Rose)
Confidence: HIGH

Principle 5: Ekspansi Utility Token Melalui Layer Baru Bukan Mengubah Tokenomics Dasar
Explanation: Tokenomics inti (inflasi 1% BP, 1% ENF) stabil sejak 2021; utility ditambah via layer/protocol baru: REX (2019, resource exchange yield), EOS EVM (2022, gas mapping), Spring SDK (2022, dev tooling) — tanpa mengubah supply mechanics【Phase 6 — Inflation/Deflation】【Phase 3 — EV-010】【Phase 3 — EV-019】【Phase 3 — EV-021】.
Evidence: 2018 staking CPU/NET+RAM+voting; 2019 REX yield; 2022 EOS EVM gas mapping; tokenomics stable since 2021【Phase 6 — Inflation/Deflation】【Phase 3 — EV-010】【Phase 3 — EV-019】【Phase 3 — EV-021】.
Supporting Dataset: Phase 6 Token (Inflation/Deflation, Utility), Phase 3 History (EV-010, EV-019, EV-021)
Confidence: HIGH

Principle 6: Community-Driven Governance dengan On-Chain Accountability (Vote Decay + BP Election)
Explanation: Continuous approval voting dengan vote decay ~50%/tahun memaksa token holder refresh vote; top 21 BP aktif. Membuat accountability berkelanjutan tapi partisipasi rendah historis. Treasury governance terpusat di ENF leadership【Phase 6 — Governance】【Phase 4 — Consensus Mechanism】.
Evidence: 1 EOS staked = 1 vote weight untuk 30 BP; vote decay ~50%/yr; 15/21 BP untuk hard fork; ENF treasury managed by leadership【Phase 6 — Governance】【Phase 4 — Consensus Mechanism】.
Supporting Dataset: Phase 6 Token (Governance), Phase 4 Technology (Consensus Mechanism)
Confidence: HIGH

## Success Factors

Factor 1: ICO Publik Permissionless $4.1B (2017-2018) Membangun Distribusi Token Luas dan Treasury Awal Masif
Explanation: Year-long daily auction di Ethereum tanpa KYC/whitelist mengumpulkan ~$4.1B dari ribuan peserta global. Menciptakan community ownership 90% supply sejak genesis, fondasi distribusi luas untuk DPoS voting legitimacy【Phase 5 — Funding History】【Phase 6 — Distribution】【Phase 3 — EV-002】【Phase 3 — EV-008】.
Evidence: $4.1B raised via 341-day public sale; 900M EOS to public, 100M to Block.one; no private sale/VC【Phase 5 — Funding History】【Phase 6 — Distribution】【Phase 3 — EV-002】【Phase 3 — EV-008】.
Supporting Dataset: Phase 5 Financial (Funding History), Phase 6 Token (Distribution, Token Sale), Phase 3 History (EV-002, EV-008)
Confidence: HIGH

Factor 2: Mainnet Launch oleh BP Collective (Bukan Block.one) Menetapkan Preseden Governance On-Chain Sejak Hari Pertama
Explanation: Block.one menolak memproduksi blok genesis; 21 BP terpilih voting on-chain meluncurkan mainnet 2018-06-14 (EV-009). Mengalihkan kendali jaringan instan ke BP Collective, menetapkan pola upgrade terkoordinasi BP-ENF yang berlanjut hingga sekarang【Phase 3 — EV-009】【Phase 3 — EV-010】【Phase 2 — Entity (BP Collective)】.
Evidence: 21 BP menghasilkan blok genesis; Block.one menyerahkan kode ke komunitas; voting BP aktif sejak 2018-06-15【Phase 3 — EV-009】【Phase 3 — EV-010】【Phase 2 — Entity (BP Collective)】.
Supporting Dataset: Phase 3 History (EV-009, EV-010), Phase 2 Entities (BP Collective)
Confidence: HIGH

Factor 3: Transisi ke ENF (2021) Memastikan Kelanjutan Pengembangan Protokol Pasca-Founder Exit
Explanation: Keluarnya Dan Larimer (EV-015) tidak menghentikan pengembangan. ENF dibentuk (EV-017) dengan mandat inflasi 1%/tahun, merekrut tim 30+ orang, memimpin Leap 3.1/4.0/5.0, EOS EVM, Spring SDK. Foundation model provides sustainable funding tanpa bergantung single entity【Phase 3 — EV-015】【Phase 3 — EV-017】【Phase 2 — Entity (ENF, Yves La Rose)】.
Evidence: Larimer exit Jan 2021; ENF formed Sep 2021 dengan 1% inflation mandate; tim 30+; Leap 3.1/4.0/5.0, EOS EVM, Spring SDK delivered【Phase 3 — EV-015】【Phase 3 — EV-017】【Phase 2 — Entity (ENF, Yves La Rose)】.
Supporting Dataset: Phase 3 History (EV-015, EV-017), Phase 2 Entities (ENF, Yves La Rose, ENF Core Team)
Confidence: HIGH

Factor 4: Arsitektur Dual-Layer (WASM Native + EOS EVM) Memperluas Addressable Market ke Ethereum Developer Ecosystem
Explanation: EOS EVM (EV-019) memungkinkan deployment kontrak Solidity/Vyper asli via Hardhat/Foundry/MetaMask. Gas fee mapped ke CPU/NET staking (zero gas UX untuk user). Menarik developer Ethereum tanpa migrasi full stack【Phase 4 — Execution Environment】【Phase 7 — Major Integrations (EOS EVM)】【Phase 8 — Narrative Position】.
Evidence: EOS EVM live Apr 2022; Solidity/Vyper support; Hardhat/Foundry/MetaMask compatible; gas mapped to CPU/NET stake【Phase 4 — Execution Environment】【Phase 7 — Major Integrations (EOS EVM)】【Phase 8 — Narrative Position】.
Supporting Dataset: Phase 4 Technology (Execution Environment), Phase 7 Ecosystem (Major Integrations), Phase 8 Market (Narrative Position)
Confidence: HIGH

Factor 5: Spring SDK (2022) Modernisasi Developer Experience (C++20, CMake, Integrated Testing) Menggantikan CDT Legacy
Explanation: Spring SDK (EV-021) menyediakan toolkit C++20 modern dengan CMake, Clang/LLVM WASM target, integrated testing framework, ABI generation. Mengatasi friksi CDT legacy dan meningkatkan DX untuk kontrak native WASM【Phase 4 — Development Framework】【Phase 3 — EV-021】【Phase 7 — Developer Ecosystem】.
Evidence: Spring SDK released 2022; C++20, CMake, testing terintegrasi; replaces CDT legacy; OpenZeppelin audit 2024【Phase 4 — Development Framework】【Phase 3 — EV-021】【Phase 7 — Developer Ecosystem】.
Supporting Dataset: Phase 4 Technology (Development Framework), Phase 3 History (EV-021), Phase 7 Ecosystem (Developer Ecosystem)
Confidence: HIGH

Factor 6: Dual Indexing Standard (Hyperion Full History + Firehose Real-Time) Menyediakan Infrastruktur Data Andal untuk Seluruh Ekosistem
Explanation: ENF menetapkan Hyperion (EOS Rio) untuk full-history REST/GraphQL dan Firehose (StreamingFast) untuk sub-second gRPC streaming sebagai standar resmi (EV-022, EV-026). Mengurangi fragmentasi provider, memastikan ketersediaan data on-chain konsisten untuk explorer, wallet, dApp【Phase 7 — Infrastructure Providers】【Phase 7 — External Dependencies】【Phase 3 — EV-022】【Phase 3 — EV-026】.
Evidence: Hyperion adopted 2023-03; Firehose recommended 2024-03; both "Critical/High" criticality; official standard for ecosystem【Phase 7 — Infrastructure Providers】【Phase 7 — External Dependencies】【Phase 3 — EV-022】【Phase 3 — EV-026】.
Supporting Dataset: Phase 7 Ecosystem (Infrastructure Providers, External Dependencies), Phase 3 History (EV-022, EV-026)
Confidence: HIGH

## Failure Factors

Factor 1: Kegagalan Voice (Platform Media Sosial Block.one) — Tutup <1 Tahun, Menghabiskan Sumber Daya Tanpa Adopsi
Explanation: Block.one meluncurkan Voice beta 2019-02 (EV-012) di atas EOS Mainnet dengan model tokenisasi perhatian + KYC. Adopsi rendah, biaya operasional tinggi, ditutup 2020-02-10 (EV-014). Menghabiskan engineering resources Block.one yang bisa difokuskan ke protokol【Phase 3 — EV-012】【Phase 3 — EV-014】【Phase 2 — Entity (Voice)】.
Evidence: Voice beta Feb 2019; closed Feb 2020 (<1 yr); low adoption, high cost; team/assets reallocated【Phase 3 — EV-012】【Phase 3 — EV-014】【Phase 2 — Entity (Voice)】.
Supporting Dataset: Phase 3 History (EV-012, EV-014), Phase 2 Entities (Voice)
Confidence: HIGH

Factor 2: Kurangnya Transparansi Treasury ENF — Size, Composition, Multi-sig Addresses Tidak Dipublikasikan Real-Time
Explanation: ENF menerima 1% inflasi tahunan sejak Sep 2021 (~3-4 tahun), tapi treasury size, komposisi (EOS vs stablecoin), alamat multi-sig custodian tidak transparan. Tidak ada audited financial statements, transparency dashboard, atau on-chain tracking resmi【Phase 5 — Treasury】【Phase 5 — Financial Risk】【Phase 6 — Holder Distribution】.
Evidence: Treasury size/composition tidak diungkap; multi-sig addresses not confirmed; no audited financials; no transparency dashboard【Phase 5 — Treasury】【Phase 5 — Financial Risk】【Phase 6 — Holder Distribution】.
Supporting Dataset: Phase 5 Financial (Treasury, Financial Risk), Phase 6 Token (Holder Distribution)
Confidence: HIGH

Factor 3: Audit Coverage Gap — Tidak Ada Audit Komprehensif Full Node Leap 5.x/6.x (Hanya Komponen Terpisah)
Explanation: Audit历史覆盖 Trail of Bits (2018), PeckShield (2018), CertiK (2022 EOS EVM), Halborn (2023 Leap consensus/P2P), OpenZeppelin (2024 Spring SDK). Tidak ada audit full node 2023-2024 mencakup consensus, P2P, WASM runtime, chainbase secara utuh【Phase 4 — Audit History】【Phase 4 — Known Technical Limitations (Audit Coverage Gap)】.
Evidence: 5 audit komponen spesifik; no comprehensive public audit for Leap 5.x/6.x full codebase【Phase 4 — Audit History】【Phase 4 — Known Technical Limitations】.
Supporting Dataset: Phase 4 Technology (Audit History, Known Technical Limitations)
Confidence: HIGH

Factor 4: Adopsi EOS EVM Rendah vs Native Mainnet (5k-20k vs 500k-1.2M tx/hari) Meski Narasi Utama
Explanation: EOS EVM live Apr 2022 sebagai Main Narrative "EVM-Compatible Layer 1" (Phase 8), tapi daily transactions ~5k-20k vs native ~500k-1.2M (Nov 2024). TVL EOS Mainnet $45.2M (rank ~35th), EOS EVM TVL lebih kecil. Developer adoption belum signifikan【Phase 8 — Adoption Metrics】【Phase 8 — Narrative Position】.
Evidence: EOS EVM tx 5k-20k/day vs native 500k-1.2M/day; TVL $45.2M rank ~35th; Main Narrative "EVM-Compatible Layer 1"【Phase 8 — Adoption Metrics】【Phase 8 — Narrative Position】.
Supporting Dataset: Phase 8 Market (Adoption Metrics, Narrative Position)
Confidence: HIGH

Factor 5: Ketergantungan Infrastruktur Kritis pada Single Provider Eksternal (Hyperion: EOS Rio, Firehose: StreamingFast) Tanpa Fallback Resmi
Explanation: Dual indexing standard bergantung 100% pada EOS Rio (Hyperion) dan StreamingFast (Firehose). Tidak ada dokumentasi alternatif, SLA, atau contingency plan jika provider down. Single point of failure untuk data layer seluruh ekosistem【Phase 7 — External Dependencies】【Phase 7 — Infrastructure Providers】.
Evidence: Hyperion (EOS Rio) "High" criticality; Firehose (StreamingFast) "High" criticality; no official alternative documented【Phase 7 — External Dependencies】【Phase 7 — Infrastructure Providers】.
Supporting Dataset: Phase 7 Ecosystem (External Dependencies, Infrastructure Providers)
Confidence: HIGH

Factor 6: Regulatory Overhang SEC Settlement 2019 ($24M) Menciptakan Ketidakpastian Hukum Token EOS di AS
Explanation: Block.one settle SEC complaint Sep 2019 (EV-013) bayar $24M tanpa admit/deny. Tidak ada legal opinion publik dari ENF post-settlement apakah EOS dianggap security di AS. Mempengaruhi exchange listing, institutional custody, US user access【Phase 3 — EV-013】【Phase 5 — Financial Risk】【Phase 2 — Entity (SEC)】.
Evidence: SEC settlement Sep 2019 $24M; no public legal opinion from ENF post-settlement; exchange delisting risk, custody issues persist【Phase 3 — EV-013】【Phase 5 — Financial Risk】【Phase 2 — Entity (SEC)】.
Supporting Dataset: Phase 3 History (EV-013), Phase 5 Financial (Financial Risk), Phase 2 Entities (SEC)
Confidence: HIGH

Factor 7: Fragmentasi Tooling Pengembang (CDT Legacy vs Spring SDK vs EOSJS vs Anchor Link vs Wharf Kit) Meningkatkan Kompleksitas Onboarding
Explanation: Koeksistensi CDT (legacy), Spring SDK (modern C++), EOSJS (legacy JS), Anchor Link/Wharf Kit (TypeScript session management) tanpa migrasi path jelas. Developer harus memilih stack tanpa guidance resmi terpusat【Phase 4 — Development Framework】【Phase 4 — Known Technical Limitations】【Phase 7 — Developer Ecosystem】.
Evidence: CDT legacy, Spring SDK modern, EOSJS legacy, Anchor Link/Wharf Kit TypeScript; no unified migration path【Phase 4 — Development Framework】【Phase 4 — Known Technical Limitations】【Phase 7 — Developer Ecosystem】.
Supporting Dataset: Phase 4 Technology (Development Framework, Known Technical Limitations), Phase 7 Ecosystem (Developer Ecosystem)
Confidence: HIGH

## Decision Framework

Step 1: Observe — Identifikasi Trigger Krusial (Founder Exit, Regulatory Event, Product Failure, Technical Bottleneck)
Explanation: Keputusan besar dipicu oleh event eksternal/internal: Larimer exit (EV-015) → Antelope rebrand; SEC settlement (EV-013) → regulatory strategy; Voice failure (EV-014) → resource reallocation; Resource exhaustion attacks → Leap 5.0 (EV-025)【Phase 3 — EV-013】【Phase 3 — EV-014】【Phase 3 — EV-015】【Phase 3 — EV-025】.
Evidence: Larimer exit Jan 2021 → Antelope rebrand Mar 2021; SEC settlement Sep 2019; Voice shutdown Feb 2020; Leap 5.0 Jan 2024 for resource exhaustion mitigation【Phase 3 — EV-013】【Phase 3 — EV-014】【Phase 3 — EV-015】【Phase 3 — EV-025】.
Supporting Dataset: Phase 3 History (EV-013, EV-014, EV-015, EV-025), Phase 9 Behavioral (Risk Response Patterns)
Confidence: HIGH

Step 2: Evaluate — Konsultasi Komunitas + BP Signaling + ENF Technical Assessment
Explanation: Sebelum hard fork/upgrade mayor: ENF mempersiapkan teknis (Leap release candidate), BP signaling via testnet/vote, komunitas diskusi di Discord/Telegram/GitHub. Contoh: Spring Hard Fork/Leap 4.0 (EV-020) terkoordinasi BP+ENF【Phase 3 — EV-020】【Phase 4 — Technical Upgrade History】【Phase 6 — Governance】.
Evidence: Leap release candidates tested by BP; BP signaling via votes; community discussion on Discord/Telegram; Spring/Leap 4.0 coordinated BP+ENF【Phase 3 — EV-020】【Phase 4 — Technical Upgrade History】【Phase 6 — Governance】.
Supporting Dataset: Phase 3 History (EV-020), Phase 4 Technology (Technical Upgrade History), Phase 6 Token (Governance)
Confidence: HIGH

Step 3: Fund — Alokasi Treasury Inflasi (1%/tahun ke ENF) untuk Prioritas Roadmap
Explanation: ENF menggunakan inflasi 1%/tahun (native EOS) untuk mendanai: core protocol dev (Leap), EOS EVM, Spring SDK, Hyperion/Firehose integration, Grants, EOS Network Ventures. Tidak ada external fundraising post-ICO【Phase 5 — Revenue Model】【Phase 3 — EV-017】【

## Open Questions
- [foundation] Status hukum token EOS pasca-penyelesaian SEC 2019 (apakah tetap dianggap security di AS) — perlu klarifikasi hukum terbaru.
- [foundation] Detail komposisi treasury ENF saat ini (jumlah EOS, stablecoin, aset lain) — tidak dipublikasikan transparan on-chain secara real-time.
- [foundation] Rincian tokenomics terbaru post-RAM market reform & "EOS Network Foundation" funding model (inflation 1% ke BP, 1% ke ENF, dst) — perlu cross-check dengan `eosio.system` contract state terkini.
- [foundation] Ketergantungan teknis pada Block.one untuk lisensi/IP software Antelope (Leap) — apakah ENF memiliki full IP ownership atau lisensi perpetuitas.
- [entity] Identitas investor/VC early-stage (jika ada) selain ICO publik — Phase 1 tidak menyebut nama VC.
- [entity] Detail auditor keamanan (security firms) yang memeriksa kontrak sistem EOS/Antelope — tidak tercakup Phase 1.
- [entity] Daftar lengkap 21 Block Producer aktif saat ini dan afiliasi mereka — hanya diketahui sebagai kolektif.
- [entity] Komposisi treasury ENF on-chain (alamat multi-sig, jumlah EOS/stablecoin) — tidak dipublikasikan transparan real-time.
- [entity] Status kepemilikan IP/lisensi perangkat lunak Antelope (Leap) antara Block.one dan ENF — apakah ENF memiliki full ownership atau lisensi perpetuitas.
- [entity] Entitas yang mengoperasikan bridge token EOS ERC-20 di Ethereum (0x86Fa049857E0209aa7D9e616F7eb3b3B78ECfdb0) — tidak jelas dari Phase 1.
- [history] Tanggal pasti pembentukan ENF: beberapa sumber menyebut September 2021, tetapi tanggal eksak (22 Sep vs awal Oktober) perlu konfirmasi dari dokumen inkorporasi Cayman Islands resmi.
- [history] Detail komposisi dan ukuran dana "EOS Network Ventures" (EV-024) — tidak dipublikasikan transparan; perlu klarifikasi dari ENF.
- [history] Status migrasi bridge token ERC-20 (EV-028) — tidak ada announcement resmi terverifikasi; kontrak 0x86Fa... masih menunjukkan aktivitas tetapi kepemilikan/upgrade authority tidak jelas.
- [history] Rincian tokenomics inflasi terkini (persentase ke BP, ENF, RAM, savings) — perlu cross-check state `eosio.system` contract on-chain saat ini vs desain awal 1%/1%/dll.
- [history] Identitas entitas yang mengoperasikan/bertanggung jawab atas bridge token ERC-20 (0x86Fa...) — apakah ENF, Block.one, atau pihak ketiga.
- [history] Daftar lengkap 21 Block Producer aktif per 2024-12 dan afiliasi mereka — hanya tersedia sebagai daftar dinamis di eosauthority.com, tidak dalam format terstruktur terverifikasi.
- [history] Status kepemilikan IP/lisensi perangkat lunak Antelope (Leap) antara Block.one dan ENF — apakah ENF memiliki full ownership atau lisensi perpetuitas; tidak ada pernyataan hukum publik terverifikasi.
- [history] Detail audit keamanan terbaru untuk kontrak sistem (eosio.token, eosio.system) dan EOS EVM — tidak ditemukan laporan audit publik terbaru (2023-2024) dari firma ternama.
- [technology] Full node audit coverage: Tidak ada audit komprehensif publik untuk Antelope Leap 5.x/6.x codebase secara utuh (consensus, P2P, WASM runtime, chainbase) — hanya audit komponen terpisah
- [technology] IBC production readiness: Status implementasi IBC di Antelope (eosio.ibc contract) — apakah sudah production-ready atau masih experimental; dokumentasi resmi minim
- [technology] ZK integration timeline: Leap 6.0 roadmap menyebut "experimental ZK-SNARK verification" — tidak ada detail teknis, testnet, atau spesifikasi resmi yang diverifikasi
- [technology] Parallel execution engine: Leap 6.0 mengclaim "parallel execution engine improvements" — arsitektur apakah berbasis optimistic parallelism (Sealevel-style), deterministic scheduling, atau lain; tidak terdokumentasi publik
- [technology] Bridge contract ownership: Entity yang mengontrol upgrade authority untuk kontrak bridge ERC-20 (0x86Fa...) di Ethereum tidak teridentifikasi secara publik resmi
- [technology] RAM market reform details: Perubahan ekonomi RAM pasca-Spring hard fork (Leap 4.0) — parameter Bancor curve, fee structure, dan dampak pada state cost tidak terdokumentasi terpusat
- [technology] Firehose vs Hyperion synchronization: Tidak ada benchmark publik resmi membandingkan konsistensi data antara Firehose (real-time) dan Hyperion (full history) di bawah reorg/heavy load
- [technology] Spring SDK adoption metrics: Tidak ada data publik terverifikasi tentang jumlah kontrak yang dikompilasi dengan Spring SDK vs CDT legacy di mainnet
- [technology] Resource model UX solutions: Tidak ada proposal resmi terdokumentasi untuk mengurangi friksi staking CPU/NET bagi end-user non-teknis (misalnya sponsored transactions, meta-transactions native)
- [financial] Ukuran treasury ENF saat ini (jumlah EOS, stablecoin, aset lain) — tidak dipublikasikan; alamat multi-sig ENF tidak dikonfirmasi resmi untuk tracking on-chain.
- [financial] Rincian alokasi inflasi 1% tahunan: apakah 100% mengalir ke ENF atau ada pembagian internal (operasional, grant, ventures, cadangan) — tidak ada breakdown publik.
- [financial] Ukuran dan komposisi dana EOS Network Ventures — hanya diumumkan "diluncurkan" September 2023 tanpa jumlah, portofolio, atau kriteria investasi.
- [financial] Status fee pasar RAM (0.5%): apakah fee tersebut diburn, dialokasikan ke ENF, atau ditahan di `eosio.ramfee` — governance history tidak terdokumentasi terpusat.
- [financial] Pendapatan aktual dari EOS EVM (gas fees mapped ke CPU/NET) — apakah ada surplus yang mengalir ke treasury atau semuanya ke BP via inflation.
- [financial] Laporan keuangan teraudit / transparency report ENF — tidak ada sama sekali di domain resmi.
- [financial] Risiko hukum token EOS pasca-SEC 2019: apakah ENF mendapatkan legal opinion bahwa EOS bukan security di AS saat ini — tidak dipublikasikan.
- [financial] Kepemilikan IP Antelope/Leap: apakah ENF memiliki full ownership atau lisensi perpetuitas royalty-free dari Block.one — tidak ada pernyataan hukum publik.
- [financial] Data on-chain untuk treasury ENF: alamat `eosio.ef` / `eosio.fund` balance history — tersedia di block explorer tapi tidak dikurasi sebagai financial dashboard.
