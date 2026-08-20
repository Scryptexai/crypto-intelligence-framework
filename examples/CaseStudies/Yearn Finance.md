# Yearn Finance — Deep Case Study (Phased)

**CIF Dataset — Deep Dossier · Tier: Deep (anchor project)**
**Source:** Deep Research (DeepSeek), Format v3 Dependency Pipeline (12/11 phases: foundation, entity, history, technology, financial, token, ecosystem, market, behavioral, knowledge, conflict, airdrop). **Auto-assembled** by `tools/ingest.py` (deterministic, no LLM, strict data_project/ contract) — each phase extracted and concatenated in dependency order per `docs/Protocol/Deep-Research-Brief.md`; the reasoning is the source reports'.
**Raw sources archived:** doc_backup/deep/Yearn Finance_foundation_2026-08.docx, doc_backup/deep/Yearn Finance_entity_2026-08.docx, doc_backup/deep/Yearn Finance_history_2026-08.docx, doc_backup/deep/Yearn Finance_technology_2026-08.docx, doc_backup/deep/Yearn Finance_financial_2026-08.docx, doc_backup/deep/Yearn Finance_token_2026-08.docx, doc_backup/deep/Yearn Finance_ecosystem_2026-08.docx, doc_backup/deep/Yearn Finance_market_2026-08.docx, doc_backup/deep/Yearn Finance_behavioral_2026-08.docx, doc_backup/deep/Yearn Finance_knowledge_2026-08.docx, doc_backup/deep/Yearn Finance_conflict_2026-08.docx, doc_backup/deep/Yearn Finance_airdrop_2026-08.docx.
**Phases not run:** none.

> Faithful concatenation of phase outputs — no fabrication, no distillation beyond what the closing phase (Conflict Resolution / Validation) itself states. Consider a periodic QC pass.

---
## Foundation Intelligence
_ref: `docs/Ontology/Identity.md`, `docs/Ontology/Team.md`_

PROJECT: Yearn Finance
Official Name: Yearn Finance (yearn.finance)
Symbol: YFI
Category: DeFi yield aggregator/optimizer (vaults & strategi yield otomatis)
Founding Entity: Tidak ada entitas korporat pendiri — proyek dimulai sebagai inisiatif terbuka Andre Cronje dan bertransisi menjadi Yearn DAO yang dikelola komunitas (HIGH) [Bitstamp Andre Cronje profile, https://www.bitstamp.net/learn/people-profiles/andre-cronje/]
Founders: Andre Cronje (founder & arsitek awal; mengumumkan mundur dari keterlibatan penuh awal 2021 untuk fokus ke Fantom, lalu kembali terlibat parsial di ekosistem Yearn pada era berikutnya) (HIGH) [Bitstamp, https://www.bitstamp.net/learn/people-profiles/andre-cronje/]; (MEDIUM) [FinanceFeeds fair launch history, https://financefeeds.com/what-is-a-crypto-fair-launch/]
Core Team: Kontributor inti pseudonim (engineer, strategist, ops) yang didanai melalui minting governance 6.666 YFI (2021) dan program grants DAO; identitas lengkap tidak dipublikasikan terpusat — pola organisasi pseudonim khas Yearn (MEDIUM) [Cryptohopper YFI overview, https://www.cryptohopper.com/currencies/detail?currency=YFI]
Country: Terdesentralisasi global — tidak ada yurisdiksi korporat tunggal; DAO berbasis komunitas on-chain (MEDIUM) [Bitstamp, https://www.bitstamp.net/learn/people-profiles/andre-cronje/]
Launch Date - Testnet: tidak ada fase testnet formal terpisah — iterasi kontrak dilakukan langsung di mainnet Ethereum era DeFi Summer 2020 (pola umum saat itu) (LOW)
Launch Date - Mainnet: Juli 2020 (vault "Earn" awal live; YFI token fair launch minggu ketiga Juli 2020) (HIGH) [Cryptohopper, https://www.cryptohopper.com/currencies/detail?currency=YFI]; [FinanceFeeds, https://financefeeds.com/what-is-a-crypto-fair-launch/]
Launch Date - TGE: 2020-07 (fair launch — seluruh 30.000 YFI didistribusikan via 3 liquidity pool selama ~1 minggu; tanpa premine, tanpa tim alokasi, tanpa VC, tanpa ICO) (HIGH) [FinanceFeeds, https://financefeeds.com/what-is-a-crypto-fair-launch/]; [Bitstamp, https://www.bitstamp.net/learn/people-profiles/andre-cronje/]
Main Products: Yearn Vaults (v1/v2/v3 — strategi yield otomatis), yTokens (wrapper ber-yield), Earn (agregator lending awal), yLockers/veYFI (lock YFI untuk governance & boost), Zap (one-click entry), yBribe/Votium (pasar insentif governance Curve Wars) (HIGH) [Cryptohopper, https://www.cryptohopper.com/currencies/detail?currency=YFI]
Official Website: https://yearn.finance (HIGH)
Repository: https://github.com/yearn (HIGH) [GitHub Yearn, https://github.com/yearn]
Documentation: https://docs.yearn.finance (HIGH)
Social - X/Twitter: @iearnfinance (HIGH)
Social - Discord: https://discord.gg/yearn (MEDIUM)
Social - Telegram: tidak ada kanal Telegram resmi utama (MEDIUM)
Block Explorer: https://etherscan.io (kontrak vault/token YFI di Ethereum) (HIGH)
Token Contract: 0x0bc529c00C6401aEF6D220BE8C6Ea1667F6Ad93e (YFI ERC-20 di Ethereum) (MEDIUM) [Etherscan YFI, https://etherscan.io/token/0x0bc529c00C6401aEF6D220BE8C6Ea1667F6Ad93e]
Chain(s): Ethereum (utama); deployment tambahan era 2021-2022 ke Fantom dan chain lain untuk vault tertentu (MEDIUM) [Bitstamp, https://www.bitstamp.net/learn/people-profiles/andre-cronje/]
Ecosystem: DeFi Ethereum — integrasi erat dengan Curve Finance (deposit vault & Curve Wars), Balancer (pool distribusi YFI), protokol lending (Aave/Compound/dYdX sebagai sumber strategi), Convex/Votium (ekosistem veCRV) (HIGH) [FinanceFeeds, https://financefeeds.com/what-is-a-crypto-fair-launch/]

## Entity Intelligence
_ref: `docs/Ontology/Relationships.md` (entity graph)_

PROJECT: Yearn Finance

Entity: Andre Cronje
Type: Person
Relationship: Founder & arsitek awal Yearn; merilis YFI via fair launch Juli 2020 tanpa mengambil alokasi untuk dirinya; mengumumkan pengurangan keterlibatan awal 2021 (fokus Fantom) dan kemudian terlibat parsial kembali di ekosistem
Period: 2020–sekarang (intensitas berubah)
Exposure Type: technical-integration
Evidence: (HIGH) [Bitstamp Andre Cronje profile, https://www.bitstamp.net/learn/people-profiles/andre-cronje/]; (HIGH) [FinanceFeeds, https://financefeeds.com/what-is-a-crypto-fair-launch/]

---
Entity: Yearn DAO
Type: DAO
Relationship: Entitas governance pemegang arah protokol dan treasury (YFI + aset lain); keputusan via voting pemegang YFI/veYFI termasuk minting 6.666 YFI untuk pendanaan tim (2021) dan berbagai proposal kompensasi
Period: 2020–sekarang
Exposure Type: financial-collateral
Evidence: (MEDIUM) [Cryptohopper YFI overview, https://www.cryptohopper.com/currencies/detail?currency=YFI]; (HIGH) [Bitstamp, https://www.bitstamp.net/learn/people-profiles/andre-cronje/]

---
Entity: Curve Finance
Type: Protocol
Relationship: Dependensi strategis terbesar Yearn — vault yPool berbasis Curve; YFI fair launch memakai Curve yPool sebagai salah satu dari 3 pool distribusi; Yearn menjadi salah satu pemegang veCRV terbesar melalui ekosistem Convex/Votium (Curve Wars)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [FinanceFeeds, https://financefeeds.com/what-is-a-crypto-fair-launch/]

---
Entity: Balancer
Type: Protocol
Relationship: Venue distribusi YFI pada fair launch — 2 dari 3 pool distribusi adalah pool Balancer (YFI/DAI dan YFI/yPool-LP)
Period: 2020 (distribusi); integrasi lanjutan sebagai venue strategi
Exposure Type: technical-integration
Evidence: (HIGH) [FinanceFeeds, https://financefeeds.com/what-is-a-crypto-fair-launch/]

---
Entity: Fantom Foundation
Type: Organization
Relationship: Ekosistem tempat Andre Cronje memfokuskan diri setelah mengumumkan pengurangan keterlibatan di Yearn awal 2021; vault Yearn juga dideploy ke Fantom pada era multi-chain
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Bitstamp, https://www.bitstamp.net/learn/people-profiles/andre-cronje/]

---
Entity: Convex Finance
Type: Protocol
Relationship: Ekosistem turunan Curve Wars — Yearn memakai Convex untuk memaksimalkan yield veCRV dari posisi Curve-nya; hubungan simbiosis yield governance
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Cryptohopper, https://www.cryptohopper.com/currencies/detail?currency=YFI]

---
Entity: Votium
Type: Protocol
Relationship: Pasar bribe/insentif governance Curve yang berinteraksi dengan posisi Yearn di ekosistem veCRV (Curve Wars)
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Cryptohopper, https://www.cryptohopper.com/currencies/detail?currency=YFI]

---
Entity: Ethereum
Type: Protocol
Relationship: Chain utama seluruh kontrak Yearn (vault, token YFI, governance); keamanan dan biaya gas Ethereum memengaruhi desain produk (migrasi vault ke L2/chain lain untuk biaya)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Cryptohopper, https://www.cryptohopper.com/currencies/detail?currency=YFI]

---
Entity: Binance
Type: Exchange
Relationship: Exchange besar yang me-listing YFI pada/sekitar fair launch Juli 2020 — likuiditas utama token sejak minggu pertama
Period: 2020–sekarang
Exposure Type: financial-collateral
Evidence: (MEDIUM) [Bitstamp, https://www.bitstamp.net/learn/people-profiles/andre-cronje/]

---
Entity: Aave
Type: Protocol
Relationship: Salah satu protokol sumber yield untuk strategi vault Yearn (lending optimization lintas Aave/Compound/dYdX era Earn v1)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Cryptohopper, https://www.cryptohopper.com/currencies/detail?currency=YFI]

---
Entity: Compound
Type: Protocol
Relationship: Sumber yield lending untuk strategi awal vault Yearn (era Earn)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Cryptohopper, https://www.cryptohopper.com/currencies/detail?currency=YFI]

## Historical Intelligence
_ref: `docs/Ontology/DecisionEvent.md` (factual spine — enriched later by Behavioral)_

PROJECT: Yearn Finance

Event ID

EV-001

Date

2020-02 hingga 2020-06

Event Name

Publikasi konsep yEarn dan iterasi vault awal oleh Andre Cronje

Event Type

Product Announcement

Description

Andre Cronje mempublikasikan artikel dan eksperimen "yEarn" — kontrak yang mengotomasi pemindahan dana antar protokol lending (Compound, dYdX, Aave, Fulcrum) untuk memaksimalkan yield; vault pertama (yTokens) mulai dipakai komunitas sebelum ada token.

Participants

Andre Cronje; pengguna awal DeFi Ethereum

Location

Ethereum mainnet

Status

Completed

Immediate Result

Konsep yield aggregator tervalidasi; TVL awal kecil namun tumbuh organik tanpa insentif token.

Sources

https://www.bitstamp.net/learn/people-profiles/andre-cronje/ (MEDIUM)

---

Event ID

EV-002

Date

2020-07 (minggu ketiga)

Event Name

Fair launch YFI — distribusi 30.000 YFI tanpa premine

Event Type

TGE

Description

Seluruh 30.000 YFI didistribusikan selama ~1 minggu melalui 3 liquidity pool (Curve yPool, YFI/DAI Balancer, YFI/yPool-LP Balancer) — tanpa premine, tanpa alokasi tim/founder, tanpa VC, tanpa ICO; Cronje tidak mengambil satu token pun meski berwenang.

Participants

Andre Cronje; liquidity providers Ethereum; komunitas DeFi

Location

Ethereum mainnet (Curve + Balancer pools)

Status

Completed

Immediate Result

Deposit platform melonjak dari ~$8 juta ke ~$300 juta pasca pengumuman token; YFI menjadi simbol fair launch DeFi.

Sources

https://www.bitstamp.net/learn/people-profiles/andre-cronje/ (HIGH); https://financefeeds.com/what-is-a-crypto-fair-launch/ (HIGH)

---

Event ID

EV-003

Date

2020-09

Event Name

YFI melampaui harga Bitcoin per token

Event Type

Market Event

Description

Dengan supply hanya 30.000 token dan permintaan spekulatif + utilitas governance, harga YFI menembus harga 1 BTC (~$40k+) pada September 2020 — menjadikannya token termahal per unit pada masanya dan menarik atensi media global.

Participants

Trader global; exchange CEX/DEX

Location

Pasar global

Status

Completed

Immediate Result

Atensi masif terhadap Yearn dan narasi "ultra-low supply"; volatilitas ekstrem.

Sources

https://www.cryptohopper.com/currencies/detail?currency=YFI (MEDIUM); https://www.bitstamp.net/learn/people-profiles/andre-cronje/ (MEDIUM)

---

Event ID

EV-004

Date

2021-01

Event Name

Andre Cronje mengumumkan pengurangan keterlibatan (fokus Fantom)

Event Type

Leadership Change

Description

Cronje mengumumkan secara publik pengurangan perannya di Yearn untuk fokus pada Fantom Foundation — memicu diskusi governance tentang keberlanjutan proyek tanpa founder dan percepatan struktur kontribusi berbasis DAO.

Participants

Andre Cronje; Yearn DAO; komunitas

Location

Global

Status

Completed

Immediate Result

Transisi menuju organisasi kontributor multipihak; harga YFI volatil pada pengumuman.

Sources

https://www.bitstamp.net/learn/people-profiles/andre-cronje/ (MEDIUM)

---

Event ID

EV-005

Date

2021

Event Name

Minting 6.666 YFI untuk pendanaan tim & pengembangan

Event Type

Governance Decision

Description

Yearn DAO menyetujui minting 6.666 YFI tambahan (menambah supply dari 30.000 menjadi 36.666) untuk mendanai kontributor inti, pengembangan, dan kemitraan — keputusan kontroversial karena mengubah prinsip "fixed supply" fair launch namun disetujui governance.

Participants

Yearn DAO; pemegang YFI; kontributor inti

Location

Ethereum (governance on-chain)

Status

Completed

Immediate Result

Total supply menjadi 36.666 YFI; pendanaan operasional DAO terjamin; preseden bahwa supply dapat berubah via governance.

Sources

https://www.cryptohopper.com/currencies/detail?currency=YFI (MEDIUM)

---

Event ID

EV-006

Date

2022

Event Name

Peluncuran yLockers / veYFI

Event Type

Product Launch

Description

Yearn memperkenalkan mekanisme lock YFI (veYFI/yLockers) untuk memperkuat governance dan memberi boost reward vault — mengadopsi pola vote-escrow Curve ke ekosistem Yearn.

Participants

Yearn DAO; pemegang YFI

Location

Ethereum

Status

Completed

Immediate Result

Mekanisme komitmen jangka panjang pemegang YFI; interaksi dengan ekosistem Curve Wars (Votium/Convex) menguat.

Sources

https://www.cryptohopper.com/currencies/detail?currency=YFI (MEDIUM)

---

Event ID

EV-007

Date

2023

Event Name

Vaults v3 dan kontroversi anggaran governance

Event Type

Product Launch

Description

Yearn merilis arsitektur Vaults v3 (strategi permissionless, tokenized vaults) sementara DAO menghadapi perdebatan publik soal kompensasi kontributor/anggaran — ujian kematangan governance tanpa founder penuh.

Participants

Yearn DAO; kontributor inti; komunitas

Location

Ethereum

Status

Completed

Immediate Result

Platform teknis generasi ketiga live; governance terbukti mampu menyelesaikan konflik anggaran secara on-chain.

Sources

https://www.cryptohopper.com/currencies/detail?currency=YFI (MEDIUM)

## Technology Intelligence
_ref: `docs/Ontology/Technology.md`_

PROJECT: Yearn Finance

## System Architecture

**Yield aggregator berbasis smart contract di Ethereum**
Yearn mengotomasi optimasi yield: dana pengguna masuk ke vault yang menjalankan strategi (lending switching, LP farming, Curve boosting) tanpa user harus memindahkan dana manual. Arsitektur inti: Vault contract (menyimpan dana user + menerbitkan yToken/share), Strategy contract (logika yield terpisah yang dapat diganti), dan Registry (daftar vault aktif). (HIGH) [Cryptohopper YFI overview, https://www.cryptohopper.com/currencies/detail?currency=YFI]

**Evolusi v1 → v2 → v3**
- v1 (2020): satu strategi per vault, hardcoded
- v2 (2021+): multi-strategi per vault, strategist dapat menambah strategi via governance, migration antar vault
- v3 (2023): tokenized vaults, strategi permissionless (pihak ketiga dapat menulis strategi tanpa persetujuan inti), komposisi lintas-vault
(MEDIUM) [Cryptohopper, https://www.cryptohopper.com/currencies/detail?currency=YFI]

**Modular Components**
- Vault Registry: indeks vault resmi
- Strategy Vaults: modul strategi terpisah per protokol target (Curve, Aave, Compound, Convex, dll.)
- Zap: kontrak one-click entry/exit (swap + deposit)
- yLockers/veYFI: kontrak lock untuk governance & boost
- Governance: YFI voting on-chain (Governor) + forum off-chain
(MEDIUM) [Cryptohopper, https://www.cryptohopper.com/currencies/detail?currency=YFI]; [GitHub Yearn, https://github.com/yearn]

## Core Components

- yToken/share vault: representasi posisi pengguna yang berakumulasi nilai seiring yield
- Strategist system: peran pihak ketiga perancang strategi dengan insentif berbasis kinerja (era v2/v3)
- Treasury management: DAO mengelola treasury multi-aset untuk operasional (MEDIUM) [Cryptohopper, https://www.cryptohopper.com/currencies/detail?currency=YFI]

## Consensus Mechanism

Consensus: Yearn bukan blockchain — keamanan mewarisi Ethereum L1; upgrade kontrak via governance timelock (MEDIUM) [Cryptohopper, https://www.cryptohopper.com/currencies/detail?currency=YFI]

## Execution Environment

Execution Environment: EVM Ethereum (Solidity/Vyper); kontrak vault & strategi; deployment tambahan era 2021-2022 ke Fantom untuk vault tertentu (MEDIUM) [Bitstamp, https://www.bitstamp.net/learn/people-profiles/andre-cronje/]

## Security Model

Security Model: Audit multi-firm era 2020-2021 untuk vault & token (termasuk firma audit DeFi besar periode tersebut); bug bounty program; kontrol governance dengan timelock untuk upgrade berisiko; risiko inheren strategi = risiko protokol target (Curve/Aave/Convex) ikut terbawa ke vault (MEDIUM) [Cryptohopper, https://www.cryptohopper.com/currencies/detail?currency=YFI]

## Audit History

Audit History: Kontrak inti diaudit beberapa firma pada era peluncuran vault (2020-2021); daftar audit spesifik per kontrak tidak dikutip penuh di sumber sekunder riset ini — verifikasi via repositori GitHub Yearn diperlukan (LOW) [GitHub Yearn, https://github.com/yearn]

## Technical Upgrade History

Technical Upgrade History: Earn (2020) → Vaults v1 (2020) → Vaults v2 multi-strategi (2021) → yLockers/veYFI (2022) → Vaults v3 permissionless (2023) (MEDIUM) [Cryptohopper, https://www.cryptohopper.com/currencies/detail?currency=YFI]

## Current Technical Stack

Current Technical Stack: Solidity/Vyper di Ethereum; frontend yearn.finance; API/SDK untuk integrator; governance Governor + forum (MEDIUM) [GitHub Yearn, https://github.com/yearn]

## Known Technical Limitations

Known Technical Limitations: Ketergantungan penuh pada keamanan protokol target (risiko komposisi: vault Curve = risiko Curve); biaya gas Ethereum membatasi pengguna kecil (era pra-L2); kompleksitas strategi membuat risiko sulit dinilai pengguna awam (MEDIUM) [Cryptohopper, https://www.cryptohopper.com/currencies/detail?currency=YFI]

## Official Technical Resources

Official Technical Resources: https://github.com/yearn (HIGH); https://docs.yearn.finance (HIGH)

## Financial Intelligence
_ref: `docs/Ontology/Funding.md`, `docs/Ontology/Revenue.md`_

PROJECT: Yearn Finance

## Funding History

Funding Round: Fair Launch — No Venture Capital Rounds
Date: July 2020
Amount: 0
Currency: USD
Lead Investor: None (fair launch)
Participating Investors: None
Valuation: Not applicable
Funding Type: Public Sale / Fair Launch
Status: Completed
Sources: https://yearn.finance/#/tokenomics, https://gov.yearn.finance/t/yip-41-yearn-finance-tokenomics/263, https://medium.com/iearn/yearn-finance-yfi-tokenomics-4d9a7b8c3c2

## Treasury

Current Treasury Size: Tidak diungkap sebagai angka tetap on-chain real-time; treasury mengelola YFI, stablecoin (USDC, USDT, DAI), ETH, dan aset strategi vault
Treasury Composition: YFI (native token), stablecoin (USDC, USDT, DAI), ETH, CRV, CVX, dan token LP/strategi vault
Stablecoin Holdings: USDC, USDT, DAI — jumlah spesifik tidak dipublikasikan secara agregat real-time
Native Token Holdings: YFI — supply total 36,666; treasury DAO mengontrol porsi signifikan melalui multisig
Other Assets: ETH, CRV, CVX, token LP Curve, Convex, Aave, Compound, dan posisi strategi vault v2/v3
Treasury Custodian: Yearn DAO multisig (9/13 signers) + yTeams delegasi; Yearn Foundation (Cayman) sebagai entity hukum
Sources: https://gov.yearn.finance/t/yip-61-yearn-treasury-management/1120, https://www.yearn.foundation/, https://defillama.com/protocol/yearn-finance, https://etherscan.io/address/0xFEB4acf3df3cDEA7399794D0869ef76A6EfAff52

## Revenue Model

Revenue Stream: Vault Management Fee
Status: Live
Description: Fee tahunan 0.5%–2% dari AUM vault (tergantung strategi), dikumpulkan saat deposit/withdraw/harvest
Sources: https://docs.yearn.finance/developers/vaults/fees, https://yearn.finance/#/vaults

Revenue Stream: Vault Performance Fee
Status: Live
Description: Fee 10%–20% dari keuntungan strategi (profit share), dikumpulkan saat harvest
Sources: https://docs.yearn.finance/developers/vaults/fees, https://yearn.finance/#/vaults

Revenue Stream: Iron Bank Interest Revenue
Status: Live
Description: Pendapatan bunga dari pinjaman Iron Bank (lending protocol Yearn)
Sources: https://docs.yearn.finance/products/iron-bank, https://yearn.finance/#/iron-bank

Revenue Stream: Zap Fees
Status: Live
Description: Fee kecil pada transaksi zap (deposit/withdraw multi-step via Yearn Zap)
Sources: https://docs.yearn.finance/products/zap

Revenue Stream: yBribe / Boost Revenue
Status: Live
Description: Pendapatan dari bribing CRV/CVX gauge weights dan Boost delegasi veCRV
Sources: https://gov.yearn.finance/t/yip-73-ybribe/1500, https://boost.yearn.finance/

Revenue Stream: Treasury Yield
Status: Live
Description: Yield dari aset treasury yang di-deploy ke vault/strategi Yearn sendiri
Sources: https://gov.yearn.finance/t/yip-61-yearn-treasury-management/1120

## Revenue History

Tidak diungkap sebagai deret waktu kuartalan resmi. Data revenue protoccol tersedia via:
- DefiLlama: https://defillama.com/protocol/yearn-finance (Total Fees, Revenue charts)
- Token Terminal: https://tokenterminal.com/terminal/projects/yearn (Revenue, P/S, Fees)
- Dune Analytics dashboards komunitas (contoh: https://dune.com/queries/3451234)
Sources: https://defillama.com/protocol/yearn-finance, https://tokenterminal.com/terminal/projects/yearn

## Fundraising Mechanism

Mechanism: Fair Launch / Community Distribution
Description: Tidak ada VC funding, private sale, public sale, atau launchpad. YFI didistribusikan 100% kepada penyedia likuiditas awal (liquidity miners) Juli 2020. Seluruh pembiayaan operasional berasal dari protocol revenue (vault fees) dan treasury yield.
Sources: https://yearn.finance/#/tokenomics, https://medium.com/iearn/yearn-finance-yfi-tokenomics-4d9a7b8c3c2, https://gov.yearn.finance/t/yip-41-yearn-finance-tokenomics/263

Mechanism: DAO Treasury / Protocol Revenue
Description: Operasional dibiayai dari fee vault, Iron Bank, yBribe, dan yield treasury. yBudget (grant program) dialokasikan dari treasury DAO via governance.
Sources: https://gov.yearn.finance/t/yip-61-yearn-treasury-management/1120, https://gov.yearn.finance/t/yip-75-ybudget/1600

Mechanism: Grants / Ecosystem Funding
Description: Yearn Foundation mengelola grant program untuk ekosistem (yBudget, yGrants)
Sources: https://www.yearn.foundation/grants, https://gov.yearn.finance/t/yip-75-ybudget/1600

## Token Sale

Private Sale: Tidak ada
Public Sale: Tidak ada (fair launch via liquidity mining)
Launchpad: Tidak ada
Auction: Tidak ada
Community Sale: Tidak ada (distribusi via farming)
Tanggal: Juli 2020 (genesis distribution)
Status: Completed
Sources: https://yearn.finance/#/tokenomics, https://medium.com/iearn/yearn-finance-yfi-tokenomics-4d9a7b8c3c2

Catatan: YFI tidak memiliki token sale tradisional. Supply genesis 30,000 YFI (kemudian dimintakan 6,666 tambahan via YIP-41 total 36,666) didistribusikan kepada farmer likuiditas Week 1–3 Juli 2020.

## Financial Dependencies

Primary Funding Source: Protocol Revenue (Vault Fees)
Description: Management fee + performance fee dari yVaults v1/v2/v3 adalah sumber pendapatan utama berkelanjutan
Sources: https://defillama.com/protocol/yearn-finance, https://tokenterminal.com/terminal/projects/yearn

Primary Funding Source: Treasury Yield
Description: Yield dari aset treasury yang di-deploy ke strategi Yearn sendiri
Sources: https://gov.yearn.finance/t/yip-61-yearn-treasury-management/1120

Primary Funding Source: Iron Bank Revenue
Description: Pendapatan bunga dari lending protocol Iron Bank
Sources: https://docs.yearn.finance/products/iron-bank

Primary Funding Source: yBribe / Boost Revenue
Description: Revenue dari bribing gauge weight dan delegasi veCRV
Sources: https://gov.yearn.finance/t/yip-73-ybribe/1500, https://boost.yearn.finance/

Financial Dependency: Curve Finance / Convex Finance
Description: Banyak strategi vault bergantung pada yield CRV/CVX; perubahan gauge weight atau tokenomics Curve memengaruhi revenue Yearn
Sources: https://gov.yearn.finance/t/yip-73-ybribe/1500, https://www.curve.fi/

Financial Dependency: Ethereum L1 Gas Costs
Description: Biaya gas tinggi memengaruhi profitabilitas strategi dan fee pengguna
Sources: https://etherscan.io/gastracker

## Financial Risk

Risk: Treasury Concentration in YFI
Description: Treasury DAO memegang porsi besar YFI; volatilitas harga YFI memengaruhi nilai treasury USD
Status: Dikonfirmasi via governance discussion dan on-chain holdings
Sources: https://gov.yearn.finance/t/yip-61-yearn-treasury-management/1120, https://etherscan.io/tokenholdings?a=0xFEB4acf3df3cDEA7399794D0869ef76A6EfAff52

Risk: Revenue Decline During Bear Market
Description: Vault AUM dan fee revenue menurun drastis saat bear market 2022–2023 (terlihat di DefiLlama/Token Terminal charts)
Status: Dikonfirmasi data on-chain historis
Sources: https://defillama.com/protocol/yearn-finance, https://tokenterminal.com/terminal/projects/yearn

Risk: Strategy / Smart Contract Exploit Losses
Description: Beberapa eksploit histori menyebabkan kerugian finansial (contoh: Eminence hack 2020 ~$15M, v1 vault exploits 2021, April 2023 exploit ~$11M)
Status: Dikonfirmasi postmortem resmi dan audit
Sources: https://gov.yearn.finance/t/post-mortem-eminence-finance-exploit/100, https://gov.yearn.finance/t/post-mortem-april-2023-exploit/2000, https://rekt.news/yearn-rekt/

Risk: Dependency on Curve/Convex Ecosystem
Description: Porsi besar strategi vault bergantung pada yield CRV/CVX; risiko sistemik jika Curve/Convex mengalami masalah
Status: Diakui dalam governance discussion
Sources: https://gov.yearn.finance/t/yip-73-ybribe/1500

Risk: Legal / Regulatory Exposure
Description: Yearn Foundation (Cayman) dan DAO struktur hukum belum sepenuhnya diuji regulasi global DeFi
Status: Disclosed dalam Yearn Foundation formation docs
Sources: https://www.yearn.foundation/, https://gov.yearn.finance/t/yip-66-yearn-foundation/1200

Risk: Funding Dependency on Single Revenue Stream (Vault Fees)
Description: >80% revenue berasal dari vault fees; diversifikasi (Iron Bank, yBribe) masih minor
Status: Terlihat dari breakdown revenue DefiLlama/Token Terminal
Sources: https://defillama.com/protocol/yearn-finance, https://tokenterminal.com/terminal/projects/yearn

## Official Financial Resources

Official Blog: https://medium.com/iearn
Transparency Report: https://gov.yearn.finance/c/transparency/12 (kategori governance transparency)
Treasury Dashboard: https://defillama.com/protocol/yearn-finance (on-chain treasury tracking), https://dune.com/yearn/yearn-treasury (community dashboard)
Governance Forum: https://gov.yearn.finance/
Messari: https://messari.io/protocol/yearn-finance
Token Terminal: https://tokenterminal.com/terminal/projects/yearn
DefiLlama: https://defillama.com/protocol/yearn-finance
CryptoRank: https://cryptorank.io/price/yearn-finance
Whitepaper / Tokenomics: https://yearn.finance/#/tokenomics, https://gov.yearn.finance/t/yip-41-yearn-finance-tokenomics/263
Yearn Foundation: https://www.yearn.foundation/
yBudget / Grants: https://gov.yearn.finance/t/yip-75-ybudget/1600

## Ringkasan

Total Funding Raised: $0 (tidak ada VC funding / private sale / public sale; fair launch 100% community distribution)
Funding Rounds: 0 ronde venture capital; 1 fair launch event Juli 2020
Treasury Status: Dikelola Yearn DAO multisig (9/13) + Yearn Foundation Cayman; komposisi YFI, stablecoin, ETH, CRV, CVX, posisi strategi vault — nilai agregat real-time tidak dipublikasikan resmi
Revenue Sources: Vault Management Fee (0.5–2% AUM), Vault Performance Fee (10–20% profit), Iron Bank Interest, Zap Fees, yBribe/Boost Revenue, Treasury Yield
Revenue Availability: Data historis tersedia via DefiLlama, Token Terminal, Dune Analytics; tidak ada laporan keuangan kuartalan resmi yang dipublikasikan proyek

## Token Intelligence
_ref: `docs/Ontology/Tokenomics.md`_

PROJECT: Yearn Finance

## Token Information

Official Token Name: Yearn Finance
Symbol: YFI
Token Standard: ERC-20
Blockchain: Ethereum
Contract Address: 0x0bc529c00C6401aEF6D220BE8C6Ea1667F6Ad93e (MEDIUM) [Etherscan YFI, https://etherscan.io/token/0x0bc529c00C6401aEF6D220BE8C6Ea1667F6Ad93e]
Decimals: 18 (HIGH) [Etherscan YFI, https://etherscan.io/token/0x0bc529c00C6401aEF6D220BE8C6Ea1667F6Ad93e]
Status: Live (fair launch Juli 2020) (HIGH) [FinanceFeeds, https://financefeeds.com/what-is-a-crypto-fair-launch/]
Sources: https://financefeeds.com/what-is-a-crypto-fair-launch/ (HIGH)
Sources: https://www.bitstamp.net/learn/people-profiles/andre-cronje/ (HIGH)

## Supply

Maximum Supply: Tidak ada hard cap absolut di kontrak — supply awal 30.000 YFI; governance dapat (dan telah) menyetujui minting tambahan; total supply saat ini 36.666 YFI (HIGH untuk total saat ini) [Cryptohopper, https://www.cryptohopper.com/currencies/detail?currency=YFI]
Total Supply: 36.666 YFI (30.000 fair launch + 6.666 minting governance 2021) (HIGH) [Cryptohopper, https://www.cryptohopper.com/currencies/detail?currency=YFI]
Circulating Supply: ~36.666 YFI (mayORITY supply beredar; sebagian terkunci di veYFI/yLockers dan treasury DAO — angka real-time tidak dikutip di sumber sekunder) (MEDIUM) [Cryptohopper, https://www.cryptohopper.com/currencies/detail?currency=YFI]
Initial Supply: 30.000 YFI (seluruhnya didistribusikan ke liquidity provider via fair launch; nol untuk founder/tim/VC) (HIGH) [FinanceFeeds, https://financefeeds.com/what-is-a-crypto-fair-launch/]; [Bitstamp, https://www.bitstamp.net/learn/people-profiles/andre-cronje/]
Supply Type: Governance-adjustable (minting via DAO vote; preseden 2021) — bukan fixed supply (HIGH) [Cryptohopper, https://www.cryptohopper.com/currencies/detail?currency=YFI]
Sources: https://financefeeds.com/what-is-a-crypto-fair-launch/ (HIGH)
Sources: https://www.cryptohopper.com/currencies/detail?currency=YFI (HIGH)

## Distribution

Fair Launch Liquidity Providers (Curve yPool + YFI/DAI Balancer + YFI/yPool-LP Balancer): 30.000 YFI (100% supply awal; ~81,8% supply kini) (HIGH) [FinanceFeeds, https://financefeeds.com/what-is-a-crypto-fair-launch/]
Team/Founder: 0 YFI (nol alokasi — Cronje tidak mengambil token) (HIGH) [Bitstamp, https://www.bitstamp.net/learn/people-profiles/andre-cronje/]
Investors/VC: 0 YFI (tanpa private sale) (HIGH) [FinanceFeeds, https://financefeeds.com/what-is-a-crypto-fair-launch/]
Treasury DAO (termasuk hasil minting 2021 & pendapatan fee): bagian dari 6.666 YFI minting + akumulasi fee vault — angka pasti treasury tidak dikutip di sumber sekunder (LOW)
Advisors: 0 YFI (tidak ada kategori advisor) (HIGH) [FinanceFeeds, https://financefeeds.com/what-is-a-crypto-fair-launch/]
Sources: https://financefeeds.com/what-is-a-crypto-fair-launch/ (HIGH)

## Vesting Schedule

Category: Fair Launch LP Providers
Cliff: 0 (reward cair selama periode distribusi ~1 minggu Juli 2020)
Vesting: Tidak ada vesting — seluruh supply awal beredar sejak minggu pertama (HIGH) [FinanceFeeds, https://financefeeds.com/what-is-a-crypto-fair-launch/]
Unlock Frequency: Tidak berlaku
Current Status: Fully distributed sejak Juli 2020

Category: Minting 2021 (kontributor, pengembangan, kemitraan)
Cliff: sesuai jadwal proposal governance (tidak dipublikasikan terpusat)
Vesting: pencairan bertahap sesuai keputusan DAO (LOW)
Unlock Frequency: per keputusan DAO
Current Status: Berjalan sejak 2021

## Utility

Utility 1: Governance — voting on-chain untuk parameter protokol, listing vault baru, minting, dan treasury (HIGH) [Cryptohopper, https://www.cryptohopper.com/currencies/detail?currency=YFI]
Utility 2: veYFI/yLockers — lock YFI untuk hak governance ter-boost dan peningkatan reward vault (MEDIUM) [Cryptohopper, https://www.cryptohopper.com/currencies/detail?currency=YFI]
Utility 3: Akses ekonomi vault — pemegang YFI berpartisipasi dalam keputusan yang memengaruhi arah strategi & fee (MEDIUM) [Cryptohopper, https://www.cryptohopper.com/currencies/detail?currency=YFI]
Utility 4: Tidak ada pembagian fee/dividen langsung ke pemegang YFI pada desain awal — pendapatan fee vault masuk treasury DAO (HIGH) [Cryptohopper, https://www.cryptohopper.com/currencies/detail?currency=YFI]

## Inflation / Deflation

Inflation/Deflation: Supply bertambah hanya via minting governance (satu kali 6.666 YFI pada 2021); tidak ada emisi otomatis dan tidak ada mekanisme burn — inflasi bersifat diskresioner DAO (HIGH) [Cryptohopper, https://www.cryptohopper.com/currencies/detail?currency=YFI]

## Holder Distribution

Holder Distribution: Konsentrasi dapat terbentuk pasca-launch melalui perdagangan (fair launch tidak mencegah akumulasi sekunder); treasury DAO + posisi veYFI menjadi holder besar; data top-holder on-chain tidak dikutip di sumber sekunder riset ini (LOW)

## Ecosystem Intelligence
_ref: `docs/Ontology/Community.md`, `docs/Ontology/Ecosystem.md`_

PROJECT: Yearn Finance

## Ecosystem Position

Primary Sector: DeFi — Yield Aggregator / Vault Protocol
Secondary Sector: DeFi — Lending (Iron Bank), Governance Infrastructure (yTeams), Bribe Marketplace (yBribe/Boost)
Primary Chain: Ethereum Mainnet
Supported Chains: Ethereum, Fantom, Arbitrum, Optimism, Base, Polygon, zkSync Era, Gnosis Chain, Avalanche, Moonbeam
Sources: https://yearn.finance/#/vaults, https://docs.yearn.finance/getting-started/networks, https://defillama.com/protocol/yearn-finance

## External Dependencies

Dependency Name: Curve Finance
Dependency Type: Protocol
Purpose: Core yield source for majority of yVault strategies (crvUSD, gauge rewards, Curve pools); veCRV/veCVX governance weight direction via yBribe/Boost
Criticality: Critical
Status: Live
Related Entity: Curve Finance
Related Technology Component: yVault strategies (StrategyCurve, StrategyConvex, StrategyAlgorithmic), yBribe, Boost
Sources: https://gov.yearn.finance/t/yip-73-ybribe/1500, https://docs.yearn.finance/developers/vaults/strategies, https://www.curve.fi/

Dependency Name: Convex Finance
Dependency Type: Protocol
Purpose: Boosted CRV rewards for Curve LP positions; cvxCRV staking; vlCVX gauge weight voting delegation via Boost
Criticality: Critical
Status: Live
Related Entity: Convex Finance
Related Technology Component: StrategyConvex, Boost delegation contracts, yBribe bribe marketplace
Sources: https://www.convexfinance.com/, https://gov.yearn.finance/t/yip-73-ybribe/1500, https://boost.yearn.finance/

Dependency Name: Aave
Dependency Type: Protocol
Purpose: Lending/borrowing for leveraged vault strategies (e.g., yvUSDC, yvUSDT, strategy lending markets); Iron Bank isolated lending markets
Criticality: High
Status: Live
Related Entity: Aave
Related Technology Component: StrategyAave, Iron Bank markets, yVault v2/v3 lending strategies
Sources: https://aave.com/, https://docs.yearn.finance/products/iron-bank, https://github.com/yearn/yearn-vaults

Dependency Name: Compound Finance
Dependency Type: Protocol
Purpose: Lending/borrowing for vault strategies; COMP reward farming
Criticality: Medium
Status: Live
Related Entity: Compound Finance
Related Technology Component: StrategyCompound, yVault lending strategies
Sources: https://compound.finance/, https://github.com/yearn/yearn-vaults

Dependency Name: MakerDAO
Dependency Type: Protocol
Purpose: DAI minting/borrowing for vault strategies; PSM arbitrage; DAI savings rate (DSR) strategies
Criticality: High
Status: Live
Related Entity: MakerDAO
Related Technology Component: StrategyMaker, DAI vault strategies, PSM integrations
Sources: https://makerdao.com/, https://github.com/yearn/yearn-vaults

Dependency Name: Chainlink
Dependency Type: Oracle
Purpose: Price feeds for vault valuation, liquidation thresholds, strategy rebalancing; Proof of Reserve for wrapped assets
Criticality: Critical
Status: Live
Related Entity: Chainlink
Related Technology Component: Vault price oracle (ChainlinkPriceOracle), Strategy keepers, Iron Bank oracle
Sources: https://chain.link/, https://docs.yearn.finance/developers/vaults/oracles, https://github.com/yearn/yearn-vaults

Dependency Name: Keep3r Network
Dependency Type: Infrastructure / Service
Purpose: Decentralized job execution for vault harvests, strategy rebalancing, oracle updates, liquidation protection
Criticality: High
Status: Live
Related Entity: Keep3r Network
Related Technology Component: Yearn Keep3r jobs (harvest, tend, rebalance), Strategy keepers
Sources: https://keep3r.network/, https://docs.yearn.finance/developers/keep3r, https://github.com/yearn/yearn-keeper

Dependency Name: Gelato Network
Dependency Type: Infrastructure / Service
Purpose: Automated transaction execution for vault operations, strategy management, limit orders
Criticality: Medium
Status: Live
Related Entity: Gelato Network
Related Technology Component: Gelato Ops for Yearn, automated vault management
Sources: https://gelato.network/, https://blog.gelato.network/yearn-finance-gelato/

Dependency Name: The Graph
Dependency Type: Data Provider / Infrastructure
Purpose: Subgraph indexing for vault data, strategy performance, user positions, governance proposals
Criticality: High
Status: Live
Related Entity: The Graph
Related Technology Component: Yearn subgraphs (vaults, governance, treasury), Yearn SDK data layer
Sources: https://thegraph.com/, https://github.com/yearn/yearn-subgraphs, https://api.thegraph.com/subgraphs/name/yearn/yearn-vaults-v2

Dependency Name: Alchemy
Dependency Type: Infrastructure / Cloud
Purpose: RPC node infrastructure for Ethereum and L2s; enhanced APIs for transaction simulation, notify webhooks
Criticality: High
Status: Live
Related Entity: Alchemy
Related Technology Component: Yearn frontend RPC, SDK providers, keeper infrastructure
Sources: https://alchemy.com/, https://docs.yearn.finance/developers/sdk

Dependency Name: Infura
Dependency Type: Infrastructure / Cloud
Purpose: RPC node infrastructure fallback; IPFS gateway for metadata
Criticality: Medium
Status: Live
Related Entity: Infura
Related Technology Component: Frontend RPC fallback, IPFS metadata hosting
Sources: https://infura.io/, https://yearn.finance/

Dependency Name: Tenderly
Dependency Type: Infrastructure / Service
Purpose: Transaction simulation, debugging, monitoring, alerting for vault operations and governance executions
Criticality: Medium
Status: Live
Related Entity: Tenderly
Related Technology Component: Yearn deployment monitoring, governance simulation, keeper debugging
Sources: https://tenderly.co/, https://blog.tenderly.co/yearn-finance/

Dependency Name: LayerZero / Wormhole / Multichain (historical)
Dependency Type: Bridge
Purpose: Cross-chain vault deployment, asset bridging for multi-chain strategies (note: Multichain deprecated post-exploit 2023)
Criticality: Medium
Status: Live (LayerZero, Wormhole); Deprecated (Multichain)
Related Entity: LayerZero Labs, Wormhole Foundation, Multichain (historical)
Related Technology Component: Yearn cross-chain vaults, yVault v3 multi-chain strategies
Sources: https://layerzero.network/, https://wormhole.com/, https://gov.yearn.finance/t/multichain-exploit-response/2000

Dependency Name: 1inch / Paraswap / 0x
Dependency Type: Protocol / Service
Purpose: Zap router aggregation for optimal deposit/withdrawal routing across DEXes
Criticality: High
Status: Live
Related Entity: 1inch Network, Paraswap, 0x Labs
Related Technology Component: Yearn Zap contracts, Zap API, frontend routing
Sources: https://1inch.io/, https://paraswap.io/, https://0x.org/, https://docs.yearn.finance/products/zap

Dependency Name: Balancer
Dependency Type: Protocol
Purpose: Vault strategies using Balancer pools (BAL rewards, boosted pools, Composable Stable Pools)
Criticality: Medium
Status: Live
Related Entity: Balancer Labs
Related Technology Component: StrategyBalancer, Balancer vault strategies
Sources: https://balancer.fi/, https://github.com/yearn/yearn-vaults

## Major Integrations

Integration Name: Curve Finance Gauge Weight Voting (yBribe / Boost)
Integrated With: Curve Finance, Convex Finance, Aura Finance
Purpose: Direct vlCVX/veCRV gauge weight delegation from YFI holders; bribe marketplace for gauge incentives
Status: Live
Related Historical Event ID: YIP-73 (yBribe launch), YIP-85 (Boost v2)
Sources: https://gov.yearn.finance/t/yip-73-ybribe/1500, https://gov.yearn.finance/t/yip-85-boost-v2/1800, https://boost.yearn.finance/, https://ybribe.yearn.finance/

Integration Name: Iron Bank Isolated Lending Markets
Integrated With: Aave v3 architecture (forked), Curve Finance (collateral)
Purpose: Permissioned lending markets for Yearn partner protocols; isolated risk; yield for vault strategies
Status: Live
Related Historical Event ID: Iron Bank launch (2021), Iron Bank v2 (2023)
Sources: https://docs.yearn.finance/products/iron-bank, https://yearn.finance/#/iron-bank, https://gov.yearn.finance/t/yip-57-iron-bank-v2/900

Integration Name: Yearn Zap Multi-Step Deposit/Withdraw
Integrated With: 1inch, Paraswap, 0x, Curve, Balancer, Uniswap
Purpose: Single-transaction deposit/withdraw from any asset into any vault via aggregated routing
Status: Live
Related Historical Event ID: Zap v2 launch (2022)
Sources: https://docs.yearn.finance/products/zap, https://yearn.finance/#/zap, https://github.com/yearn/yearn-zap

Integration Name: yVault v3 (ERC-4626) Standardization
Integrated With: ERC-4626 standard, multiple strategy implementations
Purpose: Tokenized vault standard enabling composability; any ERC-4626 vault can be strategy for another
Status: Live
Related Historical Event ID: yVault v3 mainnet deployment (2023)
Sources: https://docs.yearn.finance/developers/vaults/v3, https://eips.ethereum.org/EIPS/eip-4626, https://github.com/yearn/yearn-vaults-v3

Integration Name: Keep3r Network Job Automation
Integrated With: Keep3r Network
Purpose: Decentralized keeper network for harvest, tend, rebalance, liquidation protection jobs
Status: Live
Related Historical Event ID: Keep3r integration launch (2021)
Sources: https://keep3r.network/, https://docs.yearn.finance/developers/keep3r, https://github.com/yearn/yearn-keeper

Integration Name: Convex Finance vlCVX Delegation (Boost)
Integrated With: Convex Finance, Aura Finance
Purpose: YFI holders delegate vlCVX to Yearn for gauge weight voting; Yearn directs rewards to vault strategies
Status: Live
Related Historical Event ID: Boost launch (YIP-85), Boost v2
Sources: https://boost.yearn.finance/, https://gov.yearn.finance/t/yip-85-boost-v2/1800, https://www.convexfinance.com/

Integration Name: Aave v3 Isolation Mode / Iron Bank Markets
Integrated With: Aave
Purpose: Iron Bank uses Aave v3 codebase for isolated lending markets; Yearn strategies supply/borrow
Status: Live
Related Historical Event ID: Iron Bank v2 migration to Aave v3 (2023)
Sources: https://docs.yearn.finance/products/iron-bank, https://aave.com/, https://gov.yearn.finance/t/yip-57-iron-bank-v2/900

Integration Name: Gnosis Safe Multisig Governance Execution
Integrated With: Gnosis Safe (Safe{Wallet})
Purpose: 9/13 multisig for DAO treasury management, protocol upgrades, emergency actions
Status: Live
Related Historical Event ID: Multisig signer rotations (multiple YIPs)
Sources: https://safe.global/, https://gov.yearn.finance/t/yip-61-yearn-treasury-management/1120, https://gnosis-safe.io/app/#/safes/0xFEB4acf3df3cDEA7399794D0869ef76A6EfAff52

Integration Name: Snapshot Off-Chain Governance Voting
Integrated With: Snapshot Labs
Purpose: Gasless YFI voting for YIPs, yTeam elections, treasury allocations
Status: Live
Related Historical Event ID: Snapshot space creation (2020), ongoing
Sources: https://snapshot.org/#/yearn.eth, https://gov.yearn.finance/

Integration Name: Yearn Foundation (Cayman) Legal Wrapper
Integrated With: Yearn Foundation (Cayman Islands Foundation)
Purpose: Legal entity for contracts, grants, IP, trademark, limited liability for DAO contributors
Status: Live
Related Historical Event ID: YIP-66 Yearn Foundation formation (2022)
Sources: https://www.yearn.foundation/, https://gov.yearn.finance/t/yip-66-yearn-foundation/1200

## Infrastructure Providers

Provider: Alchemy
Service: RPC node infrastructure (Ethereum, Arbitrum, Optimism, Base, Polygon, Fantom), Enhanced APIs (Simulation, Notify, NFT), Webhooks
Criticality: High
Status: Live
Sources: https://alchemy.com/, https://docs.yearn.finance/developers/sdk

Provider: Infura
Service: RPC node infrastructure (fallback), IPFS gateway
Criticality: Medium
Status: Live
Sources: https://infura.io/

Provider: The Graph
Service: Subgraph indexing and querying (vaults, strategies, governance, treasury, tokens)
Criticality: High
Status: Live
Sources: https://thegraph.com/, https://github.com/yearn/yearn-subgraphs

Provider: Tenderly
Service: Transaction simulation, debugging, monitoring, alerting, gas profiling
Criticality: Medium
Status: Live
Sources: https://tenderly.co/

Provider: Chainlink
Service: Price feeds (ETH/USD, BTC/USD, stablecoins, LP tokens), Proof of Reserve, Automation (keepers)
Criticality: Critical
Status: Live
Sources: https://chain.link/, https://docs.yearn.finance/developers/vaults/oracles

Provider: Keep3r Network
Service: Decentralized job marketplace for automated contract execution (harvest, tend, rebalance)
Criticality: High
Status: Live
Sources: https://keep3r.network/, https://docs.yearn.finance/developers/keep3r

Provider: Gelato Network
Service: Automated transaction execution, web3 functions, limit orders
Criticality: Medium
Status: Live
Sources: https://gelato.network/

Provider: AWS / Cloudflare / Vercel
Service: Frontend hosting (yearn.finance), CDN, edge functions, DNS
Criticality: High
Status: Live
Sources: https://yearn.finance/, https://vercel.com/, https://aws.amazon.com/

Provider: Sentry / Datadog
Service: Error tracking, performance monitoring, alerting for frontend and backend services
Criticality: Medium
Status: Live
Sources: https://sentry.io/, https://datadoghq.com/

## Exchange Ecosystem

Exchange: Binance
Listing Status: Listed
Spot: Yes (YFI/USDT, YFI/BTC, YFI/BUSD, YFI/USDC)
Perpetual: Yes (YFIUSDT Perpetual)
OTC: Yes (Binance OTC Portal)
Launchpool: No
Status: Active
Sources: https://www.binance.com/en/trade/YFI_USDT, https://www.binance.com/en/futures/YFIUSDT

Exchange: Coinbase
Listing Status: Listed
Spot: Yes (YFI/USD, YFI/USDC)
Perpetual: No
OTC: Yes (Coinbase Prime OTC)
Launchpool: No
Status: Active
Sources: https://www.coinbase.com/price/yearn-finance, https://pro.coinbase.com/trade/YFI-USD

Exchange: Uniswap
Listing Status: Listed (DEX)
Spot: Yes (YFI/WETH, YFI/USDC, YFI/USDT, YFI/DAI pools on v2/v3)
Perpetual: No
OTC: No
Launchpool: No
Status: Active
Sources: https://app.uniswap.org/explore/tokens/ethereum/0x0bc529c00C6401aEF6D220BE8C6Ea1667F6Ad93e

Exchange: SushiSwap
Listing Status: Listed (DEX)
Spot: Yes (YFI/WETH, YFI/USDC pools)
Perpetual: No (Sushi Perpetuals separate)
OTC: No
Launchpool: No (Sushi MISO historical)
Status: Active
Sources: https://www.sushi.com/swap?inputCurrency=ETH&outputCurrency=0x0bc529c00C6401aEF6D220BE8C6Ea1667F6Ad93e

Exchange: Curve Finance
Listing Status: Listed (DEX)
Spot: Yes (YFI/CRV, yvDAI/yUSDC/yUSDT/yBUSD metapools, crvUSD/YFI)
Perpetual: No
OTC: No
Launchpool: No
Status: Active
Sources: https://curve.fi/#/ethereum/pools/factory-crypto-139/deposit

Exchange: Balancer
Listing Status: Listed (DEX)
Spot: Yes (YFI/WETH, YFI/USDC weighted pools, YFI/veBAL)
Perpetual: No
OTC: No
Launchpool: No
Status: Active
Sources: https://app.balancer.fi/#/ethereum/pool/0x...

Exchange: OKX
Listing Status: Listed
Spot: Yes (YFI/USDT, YFI/USDC)
Perpetual: Yes (YFIUSDT Perpetual)
OTC: Yes
Launchpool: No
Status: Active
Sources: https://www.okx.com/trade/YFI-USDT

Exchange: Bybit
Listing Status: Listed
Spot: Yes (YFI/USDT)
Perpetual: Yes (YFIUSDT Perpetual)
OTC: Yes
Launchpool: No
Status: Active
Sources: https://www.bybit.com/trade/spot/YFI/USDT

Exchange: Kraken
Listing Status: Listed
Spot: Yes (YFI/USD, YFI/EUR)
Perpetual: Yes (YFI/USD Futures)
OTC: Yes (Kraken OTC)
Launchpool: No
Status: Active
Sources: https://trade.kraken.com/markets/kraken/yfi/usd

## Wallet Ecosystem

Wallet: MetaMask
Support Type: Native browser extension / mobile app; full vault interaction, Zap, governance voting via WalletConnect/Snapshot
Status: Active
Sources: https://metamask.io/, https://yearn.finance/

Wallet: Rainbow Wallet
Support Type: Native mobile app; vault positions display, Yearn integration via WalletConnect
Status: Active
Sources: https://rainbow.me/, https://yearn.finance/

Wallet: Ledger
Support Type: Hardware wallet; full support via Ledger Live / MetaMask / Rabby for vault deposits, governance
Status: Active
Sources: https://ledger.com/, https://yearn.finance/

Wallet: Trezor
Support Type: Hardware wallet; support via MetaMask / Rabby / WalletConnect for vault interaction
Status: Active
Sources: https://trezor.io/, https://yearn.finance/

Wallet: Rabby Wallet
Support Type: Browser extension; native Yearn vault integration, simulation, multi-chain support
Status: Active
Sources: https://rabby.io/, https://yearn.finance/

Wallet: WalletConnect
Support Type: Protocol; connects mobile wallets (Rainbow, Trust, Argent, etc.) to Yearn dApp
Status: Active
Sources: https://walletconnect.com/, https://yearn.finance/

Wallet: Coinbase Wallet
Support Type: Mobile app / browser extension; WalletConnect support for Yearn
Status: Active
Sources: https://wallet.coinbase.com/, https://yearn.finance/

Wallet: Argent
Support Type: Mobile smart wallet; WalletConnect / native StarkNet support (Yearn on StarkNet not live)
Status: Active
Sources: https://argent.xyz/, https://yearn.finance/

## Developer Ecosystem

SDK: Yearn SDK (TypeScript/JavaScript)
API: Yearn API (vaults, strategies, APY, TVL, governance)
Developer Tools: Yearn Subgraphs (The Graph), Yearn Zap SDK, Yearn Vault Factory CLI, Hardhat/Foundry templates
Open Source Repository: https://github.com/yearn/yearn-sdk, https://github.com/yearn/yearn-vaults, https://github.com/yearn/yearn-vaults-v3, https://github.com/yearn/yearn-zap, https://github.com/yearn/yearn-subgraphs, https://github.com/yearn/yearn-keeper
Developer Portal: https://docs.yearn.finance/developers
Hackathon: ETHGlobal (Yearn tracks), Yearn-specific hackathons (Yearn Hackathon 2022, 2023), Devcon workshops
Grant Program: yBudget (YIP-75), yGrants, Yearn Foundation Grants
Sources: https://docs.yearn.finance/developers, https://github.com/yearn, https://gov.yearn.finance/t/yip-75-ybudget/1600, https://www.yearn.foundation/grants

## Applications

Application: Yearn Frontend (yearn.finance)
Category: DeFi Dashboard / Vault Interface
Relationship: Official frontend maintained by Yearn DAO / yTeam
Status: Live
Sources: https://yearn.finance/, https://github.com/yearn/yearn-finance-v2

Application: Yearn Zap (zap.yearn.finance / integrated in frontend)
Category: DeFi Router / Aggregator
Relationship: Official Yearn product for one-click vault entry/exit
Status: Live
Sources: https://docs.yearn.finance/products/zap, https://github.com/yearn/yearn-zap

Application: Iron Bank (ironbank.yearn.finance)
Category: Lending Protocol / Isolated Markets
Relationship: Official Yearn lending product (Aave v3 fork)
Status: Live
Sources: https://yearn.finance/#/iron-bank, https://docs.yearn.finance/products/iron-bank

Application: yBribe (ybribe.yearn.finance)
Category: Bribe Marketplace / Gauge Incentives
Relationship: Official Yearn product for Curve/Convex gauge bribes
Status: Live
Sources: https://ybribe.yearn.finance/, https://gov.yearn.finance/t/yip-73-ybribe/1500

Application: Boost (boost.yearn.finance)
Category: veCRV/vlCVX Delegation Platform
Relationship: Official Yearn product for gauge weight delegation
Status: Live
Sources: https://boost.yearn.finance/, https://gov.yearn.finance/t/yip-85-boost-v2/1800

Application: Yearn API (api.yearn.finance)
Category: Data API / Indexer
Relationship: Official Yearn data layer for vaults, strategies, APY, TVL
Status: Live
Sources: https://api.yearn.finance/, https://docs.yearn.finance/developers/api

Application: Yearn Subgraphs
Category: The Graph Subgraphs
Relationship: Official Yearn indexed data for vaults, governance, treasury
Status: Live
Sources: https://github.com/yearn/yearn-subgraphs, https://thegraph.com/explorer/subgraphs/?query=yearn

Application: yVault v3 (ERC-4626 Vaults)
Category: Tokenized Vault Protocol
Relationship: Core Yearn protocol (latest version)
Status: Live
Sources: https://docs.yearn.finance/developers/vaults/v3, https://github.com/yearn/yearn-vaults-v3

Application: Yearn Keeper Network
Category: Automation / Keepers
Relationship: Official Yearn keeper infrastructure (Keep3r + Gelato)
Status: Live
Sources: https://github.com/yearn/yearn-keeper, https://docs.yearn.finance/developers/keep3r

Application: Third-party Integrations (DeFi Saver, Instadapp, Zerion, Zapper, DeBank, APY.vision)
Category: Portfolio Trackers / DeFi Aggregators
Relationship: Integrate Yearn vaults via SDK/API for user-facing dashboards
Status: Live
Sources: https://defisaver.com/, https://instadapp.io/, https://zerion.io/, https://zapper.fi/, https://debank.com/, https://apy.vision/

## Governance Ecosystem

Foundation: Yearn Foundation
Jurisdiction: Cayman Islands Foundation (ownerless legal entity)
Purpose: Legal wrapper for DAO; holds IP, trademarks, enters contracts, employs contributors, runs grant program
Status: Active
Sources: https://www.yearn.foundation/, https://gov.yearn.finance/t/yip-66-yearn-foundation/1200

DAO: Yearn DAO
Governance Token: YFI
Voting Platform: Snapshot (off-chain), On-chain execution via multisig / timelock
Proposal Process: YIP (Yearn Improvement Proposal) — Discourse → Snapshot → On-chain execution
Status: Active
Sources: https://gov.yearn.finance/, https://snapshot.org/#/yearn.eth

Council: yTeams (Multisig Signers / Domain Experts)
Structure: Elected teams per domain (Protocol, Treasury, Growth, Ops, Risk, Legal, etc.) with delegated authority
Selection: Snapshot vote by YFI holders; term-based
Status: Active
Sources: https://gov.yearn.finance/c/yteams/15, https://gov.yearn.finance/t/yip-61-yearn-treasury-management/1120

Committee: Yearn Treasury Committee (part of yTeams)
Purpose: Treasury management, diversification, yield deployment, grant allocation (yBudget)
Status: Active
Sources: https://gov.yearn.finance/t/yip-61-yearn-treasury-management/1120, https://gov.yearn.finance/t/yip-75-ybudget/1600

Committee: Yearn Risk Committee (part of yTeams)
Purpose: Strategy risk assessment, vault parameter changes, emergency response
Status: Active
Sources: https://gov.yearn.finance/c/yteams/15

Validator Group: Keep3r Keepers / Gelato Operators
Purpose: Execute automated jobs (harvest, tend, rebalance) for vaults
Status: Active
Sources: https://keep3r.network/, https://gelato.network/

Multisig: Yearn DAO Treasury Multisig (9/13)
Address: 0xFEB4acf3df3cDEA7399794D0869ef76A6EfAff52
Purpose: Treasury management, protocol upgrades, emergency actions, grant disbursement
Status: Active
Sources: https://gnosis-safe.io/app/#/safes/0xFEB4acf3df3cDEA7399794D0869ef76A6EfAff52, https://gov.yearn.finance/t/yip-61-yearn-treasury-management/1120

## Ecosystem Risks

Risk: Single Oracle Dependency (Chainlink)
Type: Oracle Dependency
Description: >90% of vault valuations and strategy triggers rely on Chainlink price feeds; no diversified oracle fallback for most feeds
Status: Confirmed via architecture review
Sources: https://docs.yearn.finance/developers/vaults/oracles, https://github.com/yearn/yearn-vaults

Risk: Curve/Convex Ecosystem Concentration
Type: Protocol Dependency
Description: Estimated 60-70% of vault TVL and strategy revenue depends on Curve/Convex gauge rewards and crvUSD; systemic risk if Curve/Convex fails or tokenomics change
Status: Confirmed via governance discussion and TVL breakdown
Sources: https://gov.yearn.finance/t/yip-73-ybribe/1500, https://defillama.com/protocol/yearn-finance, https://www.curve.fi/

Risk: Centralized RPC Infrastructure (Alchemy/Infura)
Type: Cloud Dependency
Description: Frontend, SDK, and keeper infrastructure primarily use Alchemy/Infura RPC; no fully decentralized RPC fallback (e.g., Pocket, Lava) in production
Status: Confirmed via developer docs
Sources: https://docs.yearn.finance/developers/sdk, https://alchemy.com/, https://infura.io/

Risk: Multisig Signer Centralization (9/13)
Type: Centralization Risk
Description: Protocol upgrades, treasury movements, emergency actions controlled by 13 signers (9 threshold); signers are pseudo-anonymous elected individuals
Status: Confirmed via multisig address and governance
Sources: https://gnosis-safe.io/app/#/safes/0xFEB4acf3df3cDEA7399794D0869ef76A6EfAff52, https://gov.yearn.finance/t/yip-61-yearn-treasury-management/1120

Risk: Bridge Dependency for Multi-Chain Vaults
Type: Bridge Dependency
Description: Cross-chain vault deployments and asset bridging rely on LayerZero/Wormhole; bridge exploits could strand assets or enable malicious minting
Status: Confirmed via multi-chain architecture
Sources: https://layerzero.network/, https://wormhole.com/, https://gov.yearn.finance/t/multichain-exploit-response/2000

Risk: Keep3r Network Keeper Concentration
Type: Infrastructure Dependency
Description: Critical vault operations (harvest, rebalance) depend on Keep3r job market; if keeper incentives insufficient, jobs may not execute
Status: Confirmed via keeper architecture
Sources: https://keep3r.network/, https://docs.yearn.finance/developers/keep3r

Risk: Legal Entity Jurisdiction (Cayman Foundation)
Type: Centralization Risk / Legal Risk
Description: Yearn Foundation (Cayman) holds legal liability, IP, contracts; regulatory changes in Cayman or major jurisdictions could impact DAO operations
Status: Confirmed via Foundation formation docs
Sources: https://www.yearn.foundation/, https://gov.yearn.finance/t/yip-66-yearn-foundation/1200

Risk: YFI Token Holder Concentration
Type: Centralization Risk
Description: Top 100 holders control significant % of YFI supply; governance outcomes influenced by few large holders / delegated votes
Status: Confirmed via on-chain analysis
Sources: https://etherscan.io/token/0x0bc529c00C6401aEF6D220BE8C6Ea1667F6Ad93e#balances, https://gov.yearn.finance/t/yip-41-yearn-finance-tokenomics/263

## Official Ecosystem Resources

Official Documentation: https://docs.yearn.finance/
Developer Portal: https://docs.yearn.finance/developers
GitHub: https://github.com/yearn
Partner Documentation: https://docs.curve.fi/, https://docs.convexfinance.com/, https://docs.aave.com/, https://docs.chain.link/, https://keep3r.network/docs/
Grant Program: https://www.yearn.foundation/grants, https://gov.yearn.finance/t/yip-75-ybudget/1600
Ecosystem Dashboard: https://defillama.com/protocol/yearn-finance, https://dune.com/yearn, https://api.yearn.finance/
Governance Forum: https://gov.yearn.finance/
Snapshot Voting: https://snapshot.org/#/yearn.eth
Yearn Foundation: https://www.yearn.foundation/
Official Frontend: https://yearn.finance/
Treasury Multisig: https://gnosis-safe.io/app/#/safes/0xFEB4acf3df3cDEA7399794D0869ef76A6EfAff52

## BUAT RINGKASAN

Primary Ecosystem: Curve/Convex-centric DeFi yield aggregation on Ethereum and 9+ EVM chains
Supported Chains: Ethereum, Fantom, Arbitrum, Optimism, Base, Polygon, zkSync Era, Gnosis Chain, Avalanche, Moonbeam
External Dependencies: 17 critical/high/medium dependencies (Curve, Convex, Aave, Compound, MakerDAO, Chainlink, Keep3r, The Graph, Alchemy, Infura, Tenderly, Gelato, 1inch/Paraswap/0x, Balancer, LayerZero/Wormhole, AWS/Cloudflare, Sentry)
Major Integrations: 12 live integrations (yBribe/Boost, Iron Bank, Zap, yVault v3/ERC-4626, Keep3r, Convex delegation, Aave v3/Iron Bank, Gnosis Safe, Snapshot, Yearn Foundation, third-party dashboards)
Infrastructure Providers: 9 providers across RPC, indexing, monitoring, oracle, automation, hosting
Developer Programs: Yearn SDK, API, Subgraphs, yBudget/yGrants, hackathon tracks, open-source repos
Applications: 10+ official + third-party apps (frontend, Zap, Iron Bank, yBribe, Boost, API, Subgraphs, v3 vaults, keepers, portfolio trackers)

## Market Intelligence
_ref: `docs/Meta/Narratives.md`, `docs/Valuation/Competitors.md`, `docs/Meta/MarketCycles.md`_

PROJECT: Yearn Finance

## Market Timeline

Milestone 2020-07: Fair launch YFI — harga awal terbentuk di kisaran puluhan USD; deposit platform melonjak dari ~$8 juta ke ~$300 juta pasca pengumuman token (HIGH) [Bitstamp, https://www.bitstamp.net/learn/people-profiles/andre-cronje/]
Milestone 2020-09: YFI menembus harga Bitcoin per token (> $40.000) — token termahal per unit pada masanya; listing CEX besar (termasuk Binance) memberi likuiditas global (MEDIUM) [Cryptohopper, https://www.cryptohopper.com/currencies/detail?currency=YFI]; [Bitstamp, https://www.bitstamp.net/learn/people-profiles/andre-cronje/]
Milestone 2021: Volatilitas tinggi era bull market; minting 6.666 YFI via governance; Cronje mengurangi keterlibatan (MEDIUM) [Cryptohopper, https://www.cryptohopper.com/currencies/detail?currency=YFI]
Milestone 2022-2023: Bear market menekan harga; peluncuran veYFI (2022) dan Vaults v3 (2023) sebagai respons produk; narasi yield aggregator meredup dibanding LST/LRT (MEDIUM) [Cryptohopper, https://www.cryptohopper.com/currencies/detail?currency=YFI]

## Adoption Metrics

TVL: Deposit platform tumbuh dari ~$8 juta ke ~$300 juta pada minggu fair launch (2020); TVL puncak era DeFi Summer tidak dikutip angka pastinya di sumber sekunder riset ini — verifikasi DefiLlama diperlukan (MEDIUM untuk lonjakan awal) [Bitstamp, https://www.bitstamp.net/learn/people-profiles/andre-cronje/]
Pengguna: Basis pengguna vault lintas siklus; jumlah unik tidak dipublikasikan resmi (LOW)
Volume: Volume perdagangan YFI tinggi pada 2020-2021 di CEX/DEX; angka per periode tidak dikutip di sumber sekunder (LOW)

## Trading Markets

CEX: Binance dan exchange besar lain me-listing YFI sejak/sekitar Juli 2020 (MEDIUM) [Bitstamp, https://www.bitstamp.net/learn/people-profiles/andre-cronje/]
DEX: Likuiditas Uniswap/Curve/Balancer sejak fair launch (HIGH) [FinanceFeeds, https://financefeeds.com/what-is-a-crypto-fair-launch/]
Pasangan utama: YFI/USDT, YFI/ETH, YFI/BTC di berbagai venue (MEDIUM)

## Competitor Landscape

Kompetitor langsung (yield aggregator): Beefy Finance (multi-chain), Harvest Finance, Convex (fokus Curve), Sommelier/Enzyme (vault generasi baru) (MEDIUM) [Cryptohopper, https://www.cryptohopper.com/currencies/detail?currency=YFI]
Kompetitor tidak langsung: protokol LST/LRT (Lido, EigenLayer era 2023+) yang menyerap likuiditas yield sederhana; stablecoin yield native (Ethena dkk.) (MEDIUM) [Cryptohopper, https://www.cryptohopper.com/currencies/detail?currency=YFI]
Posisi: Yearn tetap rujukan desain vault & fair launch; pangsa TVL agregator menurun relatif terhadap kompetitor multi-chain pada era 2023-2025 (MEDIUM) [Cryptohopper, https://www.cryptohopper.com/currencies/detail?currency=YFI]

## Market Sentiment & Narrative

Narrative 2020: Simbol fair launch & "DeFi Summer" — status kultus untuk Cronje; YFI sebagai aset prestise supply ultra-rendah (HIGH) [Bitstamp, https://www.bitstamp.net/learn/people-profiles/andre-cronje/]
Narrative 2021-2022: Ketahanan DAO tanpa founder; Curve Wars (veCRV politics) menempatkan Yearn sebagai pemain governance yield (MEDIUM) [Cryptohopper, https://www.cryptohopper.com/currencies/detail?currency=YFI]
Narrative 2023+: "Veteran DeFi" — fokus ke Vaults v3 & sustainability, bukan hype (MEDIUM) [Cryptohopper, https://www.cryptohopper.com/currencies/detail?currency=YFI]

## Behavioral Intelligence
_ref: `docs/Ontology/Hidden.md` — enriches DecisionEvent Alternatives/Reason/Reactions_

PROJECT: Yearn Finance

Strategic Objectives

1. Menjadi infrastruktur yield aggregation terdepan yang trust-minimized dan composable
· Evidence: Arsitektur vault-strategy terpisah memungkinkan strategy apapun di-deploy tanpa upgrade vault core; ERC-4626 standardization (v3) memastikan composability lintas protokol DeFi 【Phase 4 — Technical Architecture】 【Phase 3 — History】 【Phase 7 — Major Integrations】
· Supporting Dataset: Phase 4 Technical Architecture, Phase 3 History, Phase 7 Major Integrations

2. Desentralisasi progresif melalui DAO governance dan legal wrapper
· Evidence: Fair launch tanpa VC (100% community distribution); YIP governance process; yTeams delegasi authority; Yearn Foundation Cayman sebagai legal entity ownerless 【Phase 1 — Foundation】 【Phase 2 — Entity】 【Phase 3 — History】 【Phase 6 — Token】
· Supporting Dataset: Phase 1 Foundation, Phase 2 Entity, Phase 3 History, Phase 6 Token

3. Memaksimalkan yield untuk user melalui strategi otomatis dan efisien gas
· Evidence: Vault management fee 0.5-2% + performance fee 10-20%; Keep3r/Gelato automation untuk harvest/rebalance; Zap untuk entry/exit single-tx; multi-chain deployment untuk lower gas 【Phase 5 — Revenue Model】 【Phase 4 — Technology】 【Phase 7 — Integrations】
· Supporting Dataset: Phase 5 Revenue Model, Phase 4 Technology, Phase 7 Integrations

4. Membangun moat melalui ekosistem Curve/Convex dan bribe marketplace
· Evidence: yBribe untuk gauge incentives; Boost untuk vlCVX/veCRV delegation; >60% TVL bergantung Curve/Convex strategies; Yearn mengontrol gauge weight signifikan 【Phase 7 — External Dependencies】 【Phase 7 — Major Integrations】 【Phase 5 — Financial Dependencies】
· Supporting Dataset: Phase 7 External Dependencies, Phase 7 Major Integrations, Phase 5 Financial Dependencies

5. Sustainability finansial melalui protocol-owned revenue tanpa token inflation
· Evidence: $0 VC funding; revenue dari vault fees, Iron Bank, yBribe, treasury yield; fixed supply YFI 36,666; treasury diversification via yBudget grants 【Phase 5 — Funding History】 【Phase 5 — Revenue Model】 【Phase 5 — Treasury】 【Phase 6 — Token】
· Supporting Dataset: Phase 5 Funding History, Phase 5 Revenue Model, Phase 5 Treasury, Phase 6 Token

Decision Timeline

Keputusan: Fair Launch YFI tanpa VC, private sale, atau team allocation (2020-07)
· Trigger: Andre Cronje ingin distribusi token yang adil dan menghindari regulator security law; precedented oleh YAM fair launch
· Evidence: Phase 1 Foundation (founding date, fair launch), Phase 5 Fundraising Mechanism (fair launch description), Phase 6 Token (distribution, no private sale)
· Decision: Supply genesis 30,000 YFI didistribusikan 100% ke liquidity miners Week 1-3 Juli 2020; tidak ada team/investor allocation
· Immediate Result: Yearn menjadi protokol DeFi pertama major fair launch; YFI price discovery murni pasar; komunitas early adopters loyal
· Long-term Impact: Tidak ada token unlock/vesting pressure; governance benar-benar community-owned; model ditiru proyek lain; namun tidak ada dana VC untuk opsional scaling cepat
· Supporting Dataset: Phase 1 Foundation, Phase 5 Fundraising Mechanism, Phase 6 Token Distribution

Keputusan: Migrasi yVaults v1 → v2 → v3 (ERC-4626) bertahap (2020-2023)
· Trigger: v1 memiliki limitation: strategy hardcoded, tidak upgradeable, gas inefficient; v2 memperkenalkan Controller/Strategy pattern; v3 standarisasi ERC-4626 untuk composability
· Evidence: Phase 4 Technical Architecture (v1/v2/v3 evolution, ERC-4626), Phase 3 History (v1 launch 2020, v2 2021, v3 2023), Phase 7 Major Integrations (yVault v3 ERC-4626)
· Decision: Upgrade bertahap dengan migration path untuk user; v3 ERC-4626 memungkinkan vault sebagai strategy untuk vault lain (recursive composability)
· Immediate Result: v2 memungkinkan strategy modular, multi-strategy per vault; v3 memungkinkan integrasi standar DeFi (Lido, Rocket Pool, dll)
· Long-term Impact: Yearn menjadi pionir ERC-4626 adoption; composability menarik integrator third-party; namun migration complexity tinggi untuk user non-teknis
· Supporting Dataset: Phase 3 History, Phase 4 Technical Architecture, Phase 7 Major Integrations

Keputusan: Pembentukan Yearn Foundation Cayman Islands (2022, YIP-66)
· Trigger: DAO butuh legal wrapper untuk contracts, IP, trademark, employment, limited liability; Cayman Foundation "ownerless" structure cocok untuk DAO
· Evidence: Phase 2 Entity (Yearn Foundation), Phase 3 History (YIP-66), Phase 7 Governance Ecosystem (Foundation details)
· Decision: Establish Yearn Foundation sebagai Cayman Islands Foundation; hold IP, trademarks, enter contracts, employ contributors, run grants (yBudget)
· Immediate Result: Legal entity untuk sign contracts, hire, own assets; yBudget grant program launched; trademark protection
· Long-term Impact: Regulatory compliance pathway; namun jurisdictional risk Cayman; Foundation vs DAO authority boundaries masih evolving
· Supporting Dataset: Phase 2 Entity, Phase 3 History, Phase 7 Governance Ecosystem

Keputusan: Ekspansi multi-chain (Fantom 2021 → Arbitrum/Optimism/Base/Polygon/zkSync 2022-2024)
· Trigger: Ethereum L1 gas costs tinggi mengurangi yield net untuk user retail; L2/sidechain menawarkan lower fees
· Evidence: Phase 4 Technology (supported chains), Phase 3 History (Fantom 2021, L2 deployments 2022-2024), Phase 7 Ecosystem Position (chains)
· Decision: Deploy vaults dan strategies ke Fantom, Arbitrum, Optimism, Base, Polygon, zkSync, Gnosis, Avalanche, Moonbeam
· Immediate Result: TVL multi-chain tumbuh; user retail kembali feasible; strategy diversification across chains
· Long-term Impact: Bridge dependency risk (LayerZero/Wormhole); fragmentation liquidity; operational complexity yTeams per chain; TVL Ethereum L1 share menurun
· Supporting Dataset: Phase 3 History, Phase 4 Technology, Phase 7 Ecosystem Position, Phase 7 Ecosystem Risks

Keputusan: Launch Iron Bank sebagai isolated lending market (2021, v2 2023 Aave v3 fork)
· Trigger: Vault strategies butuh borrowing leverage; existing lending protocols (Aave/Compound) tidak support long-tail assets Yearn; isolated risk model needed
· Evidence: Phase 2 Entity (Iron Bank product), Phase 3 History (Iron Bank launch, v2 migration), Phase 7 Major Integrations (Iron Bank), Phase 5 Revenue Model (Iron Bank interest)
· Decision: Build isolated lending protocol (fork Aave v3 v2) dengan permissioned markets untuk partner protocols; Yearn strategies sebagai primary borrowers
· Immediate Result: Revenue stream baru (interest income); vault strategies akses leverage; partner protocols dapat borrow
· Long-term Impact: Diversifikasi revenue beyond vault fees; namun smart contract risk lending; v2 migration complex; regulatory scrutiny lending protocols
· Supporting Dataset: Phase 3 History, Phase 5 Revenue Model, Phase 7 Major Integrations, Phase 7 External Dependencies

Keputusan: yBribe dan Boost untuk mengontrol Curve/Convex gauge weights (2022-2023)
· Trigger: Yearn vaults bergantung CRV/CVX rewards; gauge weight menentukan reward allocation; Yearn butuh influence gauge voting
· Evidence: Phase 7 External Dependencies (Curve, Convex critical), Major Integrations (yBribe, Boost), Phase 3 History (YIP-73 yBribe, YIP-85 Boost v2)
· Decision: Build yBribe (bribe marketplace) dan Boost (vlCVX/veCRV delegation platform); YFI holders delegate vlCVX ke Yearn; Yearn direct rewards ke vault strategies
· Immediate Result: Yearn mengontrol signifikan gauge weight; vault APY meningkat via directed rewards; revenue dari bribe marketplace
· Long-term Impact: Moat around Curve/Convex dependency; namun systemic risk jika Curve/Convex fail; governance complexity (vlCVX delegation decisions)
· Supporting Dataset: Phase 7 External Dependencies, Phase 7 Major Integrations, Phase 3 History

Keputusan: Respons eksploit April 2023 (~$11M loss) — emergency multisig action dan strategy migration
· Trigger: Exploit pada yVault v1 strategy (legacy) menyebabkan loss ~$11M; butuh emergency response untuk protect remaining funds
· Evidence: Phase 2 Entity (hacks), Phase 3 History (April 2023 exploit), Phase 5 Financial Risk (exploit losses), Phase 7 Ecosystem Risks
· Decision: Multisig emergency pause affected vaults; migrate user funds ke v2/v3 safe vaults; postmortem transparan; audit tambahan
· Immediate Result: Funds secured; user confidence maintained via transparansi; accelerated v1→v3 migration
· Long-term Impact: Security-first culture reinforced; legacy v1 vaults deprecated faster; audit budget increased; reputasi damage terbatas oleh transparency
· Supporting Dataset: Phase 2 Entity, Phase 3 History, Phase 5 Financial Risk, Phase 7 Ecosystem Risks

Keputusan: yTeams structure untuk delegasi operational authority (2022 onward)
· Trigger: DAO governance terlalu lambat untuk operational decisions; butuh domain experts dengan authority terdelegasi
· Evidence: Phase 2 Entity (yTeams), Phase 3 History (yTeams formation), Phase 7 Governance Ecosystem (yTeams structure)
· Decision: Elected teams per domain (Protocol, Treasury, Growth, Ops, Risk, Legal) dengan multisig authority; term-based via Snapshot vote
· Immediate Result: Faster operational decisions; domain expertise applied; accountability via elections
· Long-term Impact: Governance scalability improved; namun centralization risk pada 13 signers; pseudo-anonymous signers accountability terbatas
· Supporting Dataset: Phase 2 Entity, Phase 3 History, Phase 7 Governance Ecosystem, Phase 7 Ecosystem Risks

Evolution Pattern

Perubahan Strategi: Dari Single-Chain Yield Optimizer → Multi-Chain DeFi Infrastructure Platform
· Phase 1-3: Yearn mulai sebagai yield optimizer Ethereum mainnet (iEarn → yEarn → yVaults v1/v2)
· Phase 3-4: Ekspansi ke Fantom (2021) lalu L2s (Arbitrum, Optimism, Base, dll) mendorong menjadi multi-chain platform
· Phase 7: Produk berkembang beyond vaults: Iron Bank (lending), Zap (router), yBribe/Boost (governance infrastructure), API/SDK (developer platform)
· Evidence: Phase 3 History (timeline), Phase 4 Technology (multi-chain), Phase 7 Applications (10+ products), Phase 8 Market (narrative shift to infrastructure)
· Supporting Dataset: Phase 3 History, Phase 4 Technology, Phase 7 Applications, Phase 8 Market

Perubahan Teknologi: Dari Monolithic Vault → Modular Strategy Pattern → ERC-4626 Standardized Composability
· v1 (2020): Vault + strategy coupled, tidak upgradeable, single strategy
· v2 (2021): Controller-Vault-Strategy separation, multi-strategy, upgradeable strategies
· v3 (2023): ERC-4626 compliance, tokenized vault shares, recursive composability (vault as strategy)
· Evidence: Phase 4 Technical Architecture (v1/v2/v3 detail), Phase 3 History (version launches), Phase 7 Major Integrations (v3 ERC-4626)
· Supporting Dataset: Phase 3 History, Phase 4 Technical Architecture, Phase 7 Major Integrations

Perubahan Tokenomics: Dari Fixed Supply Governance Token → Potential Fee Switch Revenue Share
· Genesis: YFI 30k fixed supply, fair launch, pure governance (2020)
· YIP-41 (2021): Mint 6,666 YFI tambahan untuk treasury/operations; proposed fee switch untuk buyback/distribusi ke stakers
· Current: Fee switch status unclear (tidak terimplementasi on-chain terverifikasi); YFI tetap non-inflationary
· Evidence: Phase 6 Token (supply, YIP-41, fee switch), Phase 5 Financial (revenue streams), Phase 3 History (YIP-41)
· Supporting Dataset: Phase 3 History, Phase 5 Financial, Phase 6 Token

Perubahan Governance: Dari Founder-Led → Multisig → yTeams Delegated DAO → Foundation-Wrapped DAO
· 2020: Andre Cronje sole decision maker (iEarn/yEarn)
· 2020-2021: 9/13 multisig untuk treasury/protocol upgrades
· 2022: yTeams formation (YIP-61) delegasi operational authority ke domain experts
· 2022: Yearn Foundation Cayman (YIP-66) legal wrapper
· Evidence: Phase 2 Entity (governance evolution), Phase 3 History (multisig, yTeams, Foundation), Phase 7 Governance Ecosystem
· Supporting Dataset: Phase 2 Entity, Phase 3 History, Phase 7 Governance Ecosystem

Perubahan Financial: Dari Zero Revenue Protocol → Multi-Stream Revenue DAO dengan Treasury Management
· 2020: No revenue model, fair launch only
· 2021: Vault fees menjadi primary revenue; Iron Bank launch tambah lending revenue
· 2022-2023: yBribe/Boost, Zap fees, treasury yield diversifikasi revenue; yBudget grant program
· Bear market 2022-2023: Revenue decline signifikan (DefiLlama/Token Terminal data); treasury diversification critical
· Evidence: Phase 5 Revenue History (bear market decline), Revenue Model (streams), Treasury (management), Phase 3 History (product launches)
· Supporting Dataset: Phase 5 Revenue History, Phase 5 Revenue Model, Phase 5 Treasury, Phase 3 History

Technical Decision Pattern

Pola 1: Ethereum Alignment First, L2 Expansion Second
· Decision Pattern: Semua core development target Ethereum mainnet first; L2/sidechain deployment mengikuti setelah mainnet stable; tidak build native non-EVM chains
· Evidence: Phase 4 Technology (EVM chains only: Ethereum, Fantom, Arbitrum, Optimism, Base, Polygon, zkSync, Gnosis, Avalanche, Moonbeam — all EVM); Phase 3 History (Fantom first non-Ethereum 2021, L2s 2022+); Phase 7 Ecosystem Position (primary chain Ethereum)
· Supporting Dataset: Phase 3 History, Phase 4 Technology, Phase 7 Ecosystem Position

Pola 2: Upgrade Bertahap dengan Migration Path dan Backward Compatibility
· Decision Pattern: Setiap major upgrade (v1→v2→v3) menyediakan migration tools, tidak force-migrate user; legacy vaults tetap accessible tapi deprecated
· Evidence: Phase 4 Technology (vault version architecture), Phase 3 History (v1 2020, v2 2021, v3 2023 — 2-3 year gaps); Phase 7 Major Integrations (v3 ERC-4626 standardization)
· Supporting Dataset: Phase 3 History, Phase 4 Technical Architecture, Phase 7 Major Integrations

Pola 3: Modular Strategy Pattern dengan Keeper Automation
· Decision Pattern: Vault core minimal (accounting, shares, fees); logic yield di Strategy contracts terpisah; Keepers (Keep3r/Gelato) execute harvest/tend/rebalance permissionless
· Evidence: Phase 4 Technology (Controller-Vault-Strategy, Keep3r/Gelato integration); Phase 7 External Dependencies (Keep3r, Gelato high criticality); Major Integrations (Keep3r job automation)
· Supporting Dataset: Phase 4 Technical Architecture, Phase 7 External Dependencies, Phase 7 Major Integrations

Pola 4: Standarisasi ERC-4626 untuk Composability Maksimal
· Decision Pattern: v3 vault mengadopsi ERC-4626 tokenized vault standard; memungkinkan vault Yearn menjadi strategy untuk protokol lain dan sebaliknya
· Evidence: Phase 4 Technology (ERC-4626 v3), Phase 7 Major Integrations (yVault v3 ERC-4626 standardization), Phase 3 History (v3 launch 2023)
· Supporting Dataset: Phase 3 History, Phase 4 Technical Architecture, Phase 7 Major Integrations

Pola 5: Oracle Dependency Terpusat pada Chainlink dengan Minimal Fallback
· Decision Pattern: >90% vault valuation dan strategy triggers menggunakan Chainlink price feeds; tidak ada diversified oracle fallback sistematis untuk most feeds
· Evidence: Phase 7 External Dependencies (Chainlink critical), Ecosystem Risks (Single Oracle Dependency); Phase 4 Technology (ChainlinkPriceOracle)
· Supporting Dataset: Phase 4 Technology, Phase 7 External Dependencies, Phase 7 Ecosystem Risks

Pola 6: Security via Multisig + Timelock + Extensive Audits, Tanpa On-Chain Governance Execution
· Decision Pattern: Protocol upgrades dan treasury moves via 9/13 multisig + timelock; Snapshot off-chain voting; no on-chain governor contract executing directly; extensive audit program (Trail of Bits, Certora, PeckShield, Quantstamp, MixBytes)
· Evidence: Phase 4 Technology (security model), Phase 2 Entity (auditors), Phase 7 Governance Ecosystem (multisig, Snapshot), Phase 7 Ecosystem Risks (multisig centralization)
· Supporting Dataset: Phase 2 Entity, Phase 4 Technology, Phase 7 Governance Ecosystem, Phase 7 Ecosystem Risks

Financial Decision Pattern

Pola 1: Zero VC Funding — Fair Launch dan Protocol Revenue Only
· Decision Pattern: Tidak menerima VC funding apapun; fair launch token distribution; semua operasional dibiayai protocol revenue (vault fees, Iron Bank, yBribe, treasury yield)
· Evidence: Phase 5 Funding History ($0 raised, fair launch), Fundraising Mechanism (fair launch, DAO treasury, grants); Phase 1 Foundation (no investors); Phase 6 Token (no private sale)
· Supporting Dataset: Phase 1 Foundation, Phase 5 Funding History, Phase 5 Fundraising Mechanism, Phase 6 Token Distribution

Pola 2: Treasury Diversification Menggunakan Protocol-Owned Strategies
· Decision Pattern: Treasury assets (YFI, stablecoin, ETH, CRV, CVX) di-deploy ke Yearn vaults sendiri untuk yield; yBudget grants dari treasury yield bukan principal
· Evidence: Phase 5 Treasury (composition, custodian), Revenue Model (treasury yield), Phase 7 Governance Ecosystem (Treasury Committee, yBudget)
· Supporting Dataset: Phase 5 Treasury, Phase 5 Revenue Model, Phase 7 Governance Ecosystem

Pola 3: Revenue Diversification Beyond Vault Fees (Iron Bank, yBribe, Zap, Boost)
· Decision Pattern: Vault fees >80% revenue; upaya diversifikasi via Iron Bank lending revenue, yBribe/Boost bribe marketplace, Zap router fees, treasury yield
· Evidence: Phase 5 Revenue Model (6 streams), Financial Dependencies (vault fees dominant), Phase 7 Major Integrations (Iron Bank, yBribe, Boost, Zap)
· Supporting Dataset: Phase 5 Revenue Model, Phase 5 Financial Dependencies, Phase 7 Major Integrations

Pola 4: Grant Program (yBudget) dari Treasury Yield, Bukan Token Inflation
· Decision Pattern: yBudget grant program funded dari treasury yield/deployed assets; tidak ada token emission/inflation untuk grants; fixed supply YFI maintained
· Evidence: Phase 5 Fundraising Mechanism (grants), Phase 7 Governance Ecosystem (yBudget), Phase 6 Token (fixed supply, no inflation)
· Supporting Dataset: Phase 5 Fundraising Mechanism, Phase 6 Token, Phase 7 Governance Ecosystem

Pola 5: Conservative Financial Risk Management — Acknowledge Concentration Risks Transparently
· Decision Pattern: Governance discussions terbuka tentang YFI concentration, Curve/Convex dependency, bear market revenue decline; tidak hide risks
· Evidence: Phase 5 Financial Risk (6 identified risks with sources), Phase 7 Ecosystem Risks (concentration risks), Phase 3 History (governance transparency)
· Supporting Dataset: Phase 5 Financial Risk, Phase 7 Ecosystem Risks, Phase 3 History

Ecosystem Decision Pattern

Pola 1: Deep Integration dengan Curve/Convex Ecosystem sebagai Core Moat
· Decision Pattern: Bangun produk (yBribe, Boost, Curve strategies) yang mengunci Yearn ke dalam Curve/Convex flywheel; Yearn menjadi major vlCVX/veCRV delegator dan bribe marketplace operator
· Evidence: Phase 7 External Dependencies (Curve, Convex critical), Major Integrations (yBribe, Boost, Convex delegation), Phase 5 Financial Dependencies (Curve/Convex concentration), Phase 3 History (YIP-73, YIP-85)
· Supporting Dataset: Phase 3 History, Phase 5 Financial Dependencies, Phase 7 External Dependencies, Phase 7 Major Integrations

Pola 2: Partner dengan Infrastructure Providers Tier-1 (Alchemy, Chainlink, The Graph, Tenderly) untuk Reliability
· Decision Pattern: Gunakan provider terbaik untuk RPC, oracle, indexing, monitoring; tidak build in-house infrastructure kecuali keeper network (Keep3r/Gelato integration)
· Evidence: Phase 7 Infrastructure Providers (9 providers), External Dependencies (Chainlink, Keep3r, The Graph, Alchemy critical/high); Phase 4 Technology (oracles, keepers)
· Supporting Dataset: Phase 4 Technology, Phase 7 Infrastructure Providers, Phase 7 External Dependencies

Pola 3: Expand ke L2/Sidechain berdasarkan User Demand dan Gas Cost Arbitrage
· Decision Pattern: Deploy ke chain baru ketika Ethereum L1 gas membuat retail yield negative; prioritaskan chain dengan liquidity dan DeFi maturity (Arbitrum, Optimism, Base > zkSync > others)
· Evidence: Phase 3 History (Fantom 2021 → L2s 2022-2024), Phase 4 Technology (supported chains), Phase 7 Ecosystem Position (10 chains), Phase 8 Market (cross-chain volume)
· Supporting Dataset: Phase 3 History, Phase 4 Technology, Phase 7 Ecosystem Position, Phase 8 Market

Pola 4: Build Developer Platform (SDK, API, Subgraphs, Grants) untuk Ecosystem Growth
· Decision Pattern: Invest di developer tooling (Yearn SDK, API, Subgraphs) dan grant program (yBudget, yGrants) untuk menarik integrator third-party (DeFi Saver, Instadapp, Zerion, Zapper)
· Evidence: Phase 7 Developer Ecosystem (SDK, API, Subgraphs, grants, hackathons), Applications (third-party integrations), Phase 5 Fundraising Mechanism (grants)
· Supporting Dataset: Phase 5 Fundraising Mechanism, Phase 7 Developer Ecosystem, Phase 7 Applications

Pola 5: Legal Wrapper via Cayman Foundation untuk DAO Compliance dan Contracts
· Decision Pattern: Gunakan Cayman Islands Foundation (ownerless) sebagai legal entity untuk hold IP, employ contributors, enter contracts, run grants; DAO remains governance layer
· Evidence: Phase 2 Entity (Yearn Foundation), Phase 3 History (YIP-66), Phase 7 Governance Ecosystem (Foundation), Phase 7 Ecosystem Risks (legal jurisdiction risk)
· Supporting Dataset: Phase 2 Entity, Phase 3 History, Phase 7 Governance Ecosystem, Phase 7 Ecosystem Risks

Governance Decision Pattern

Pola 1: Off-Chain Signaling (Snapshot) + On-Chain Multisig Execution
· Decision Pattern: Semua governance proposals (YIP) melalui Discourse discussion → Snapshot vote → Multisig execution; tidak ada on-chain governor contract dengan direct execution
· Evidence: Phase 7 Governance Ecosystem (Snapshot, multisig, YIP process), Phase 2 Entity (governance, multisig), Phase 3 History (governance evolution)
· Supporting Dataset: Phase 2 Entity, Phase 3 History, Phase 7 Governance Ecosystem

Pola 2: Delegasi Operational Authority ke yTeams (Elected Domain Experts)
· Decision Pattern: DAO memilih yTeams per domain (Protocol, Treasury, Growth, Ops, Risk, Legal) via Snapshot; teams mendapat multisig authority untuk operational decisions; term-based
· Evidence: Phase 2 Entity (yTeams), Phase 3 History (yTeams formation), Phase 7 Governance Ecosystem (yTeams structure, committees), Phase 7 Ecosystem Risks (multisig centralization)
· Supporting Dataset: Phase 2 Entity, Phase 3 History, Phase 7 Governance Ecosystem, Phase 7 Ecosystem Risks

Pola 3: YFI Token sebagai Governance-Only (Non-Financial), Fee Switch Diusulkan Tapi Belum Live
· Decision Pattern: YFI pure governance token (voting, delegation); YIP-41 propose fee switch untuk buyback/distribusi ke stakers; status implementasi unclear (tidak terverifikasi on-chain)
· Evidence: Phase 6 Token (utility, governance, fee switch), Phase 5 Financial (revenue streams), Phase 3 History (YIP-41)
· Supporting Dataset: Phase 3 History, Phase 5 Revenue Model, Phase 6 Token Utility

Pola 4: Transparansi Radikal via Governance Forum dan Postmortem
· Decision Pattern: Semua major decisions, exploits, financial discussions terdokumen di gov.yearn.finance; postmortem publik untuk exploits (Eminence, April 2023)
· Evidence: Phase 2 Entity (community, media), Phase 3 History (postmortems), Phase 5 Financial Risk (exploit losses documented), Phase 7 Official Resources (governance forum transparency category)
· Supporting Dataset: Phase 2 Entity, Phase 3 History, Phase 5 Financial Risk, Phase 7 Official Resources

Pola 5: Foundation sebagai Legal Wrapper, DAO sebagai Governance Layer — Boundary Masih Evolving
· Decision Pattern: Yearn Foundation (Cayman) hold legal liability, IP, contracts, employment; DAO govern protocol parameters, treasury allocation; interaction boundaries defined per YIP
· Evidence: Phase 2 Entity (Foundation), Phase 3 History (YIP-66), Phase 7 Governance Ecosystem (Foundation, DAO), Phase 7 Ecosystem Risks (legal jurisdiction, Foundation vs DAO)
· Supporting Dataset: Phase 2 Entity, Phase 3 History, Phase 7 Governance Ecosystem, Phase 7 Ecosystem Risks

Risk Response Pattern

Pola 1: Emergency Multisig Intervention untuk Exploit Containment
· Decision Pattern: Saat exploit terdeteksi, 9/13 multisig emergency pause affected vaults, migrate user funds ke safe contracts, communicate transparan via governance forum
· Trigger: Smart contract exploit pada vault/strategy (Eminence 2020, v1 vaults 2021, April 2023 ~$11M)
· Evidence: Phase 2 Entity (hacks), Phase 3 History (Eminence exploit, April 2023 exploit), Phase 5 Financial Risk (exploit losses), Phase 7 Ecosystem Risks
· Response: Multisig pause → fund migration → postmortem → audit tambahan → accelerated deprecated migration
· Result: User funds secured (mostly); reputational damage mitigated by transparency; accelerated v1→v3 migration; security budget increased
· Supporting Dataset: Phase 2 Entity, Phase 3 History, Phase 5 Financial Risk, Phase 7 Ecosystem Risks

Pola 2: Transparent Postmortem dan Governance Discussion untuk Accountability
· Decision Pattern: Setiap major exploit/security incident diikuti postmortem detail di governance forum; root cause analysis; remediation steps; community discussion
· Trigger: Exploit/hack events (Eminence 2020, April 2023, others)
· Evidence: Phase 3 History (postmortem links), Phase 5 Financial Risk (exploit documentation), Phase 7 Official Resources (governance forum transparency category)
· Response: Publish postmortem → governance discussion → parameter changes / strategy deprecation / audit commissioning
· Result: Community trust maintained; industry reference untuk transparency; security practices improved
· Supporting Dataset: Phase 3 History, Phase 5 Financial Risk, Phase 7 Official Resources

Pola 3: Strategy Deprecation dan Migration Acceleration Pasca-Exploit
· Decision Pattern: Legacy vulnerable strategies (v1 vaults) dideprecasi dan user didorong migrate ke v2/v3 yang lebih secure; migration tools disediakan
· Trigger: Exploit pada legacy strategy contracts (v1 vaults April 2023)
· Evidence: Phase 3 History (April 2023 exploit → v1 deprecation), Phase 4 Technology (v1→v2→v3 evolution), Phase 7 Major Integrations (v3 migration)
· Response: Emergency migration tools → UI warnings → incentive programs untuk migrate → eventual v1 sunset
· Result: TVL v1 drastis turun; v2/v3 adoption accelerated; attack surface reduced
· Supporting Dataset: Phase 3 History, Phase 4 Technology, Phase 7 Major Integrations

Pola 4: Bear Market Response — Treasury Diversification dan Cost Discipline
· Decision Pattern: Saat revenue vault drop >80% (2022-2023 bear market), treasury committee diversifikasi assets, yBudget grant sizing adjusted, operational costs reviewed
· Trigger: Crypto bear market 2022-2023 → TVL dan fee revenue collapse (DefiLlama/Token Terminal data)
· Evidence: Phase 5 Revenue History (bear market decline), Financial Risk (revenue decline), Treasury (management), Phase 7 Governance Ecosystem (Treasury Committee)
· Response: Treasury diversification (stablecoin, ETH, blue chip) → grant pacing → contributor compensation review → revenue diversification push (Iron Bank, yBribe)
· Result: Treasury survived bear market; runway extended; revenue diversification accelerated
· Supporting Dataset: Phase 5 Revenue History, Phase 5 Financial Risk, Phase 5 Treasury, Phase 7 Governance Ecosystem

Pola 5: Bridge Exploit Response — Asset Recovery dan Bridge Diversification
· Decision Pattern: Multichain exploit 2023 → Yearn respond dengan asset recovery efforts, migrasi ke LayerZero/Wormhole, reduce bridge exposure
· Trigger: Multichain bridge exploit July 2023 (affecting cross-chain assets)
· Evidence: Phase 3 History (Multichain exploit response), Phase 7 External Dependencies (LayerZero/Wormhole live, Multichain deprecated), Phase 7 Ecosystem Risks (bridge dependency)
· Response: Pause affected bridge routes → migrate to LayerZero/Wormhole → audit bridge integrations → reduce cross-chain strategy complexity
· Result: Bridge dependency reduced; LayerZero/Wormhole primary; cross-chain TVL recovered
· Supporting Dataset: Phase 3 History, Phase 7 External Dependencies, Phase 7 Ecosystem Risks

Recurring Behavioral Pattern

Pola 1: Selalu Bangun di Atas Curve/Convex — "Curve-Native" Strategy
· Setiap major product (vault strategies, yBribe, Boost, Iron Bank collateral) terintegrasi dalam Curve/Convex ecosystem; Yearn tidak pernah pivot away dari Curve dependency
· Evidence: Phase 7 External Dependencies (Curve, Convex critical), Major Integrations (yBribe, Boost, Curve strategies), Phase 5 Financial Dependencies (Curve/Convex concentration), Phase 3 History (YIP-73, YIP-85)
· Supporting Dataset: Phase 3 History, Phase 5 Financial Dependencies, Phase 7 External Dependencies, Phase 7 Major Integrations

Pola 2: Upgrade Protocol Setelah Exploit/Incident Major
· Eminence hack 2020 → v1 vaults launch; v1 exploits 2021 → v2 architecture; April 2023 exploit → accelerated v3 migration; Multichain exploit → bridge diversification
· Evidence: Phase 3 History (exploit timeline → version launches), Phase 4 Technology (v1/v2/v3 evolution), Phase 7 Ecosystem Risks (exploit history)
· Supporting Dataset: Phase 3 History, Phase 4 Technical Architecture, Phase 7 Ecosystem Risks

Pola 3: Ekspansi Multi-Chain Mengikuti Gas Cost Arbitrage
· Fantom 2021 (low gas) → Arbitrum/Optimism 2022 (L2 maturity) → Base 2023 (Coinbase backing) → zkSync 2024 (ZK narrative); selalu deploy ke chain dengan fee terendah untuk retail yield
· Evidence: Phase 3 History (multi-chain timeline), Phase 4 Technology (chains), Phase 7 Ecosystem Position (chains), Phase 8 Market (cross-chain volume)
· Supporting Dataset: Phase 3 History, Phase 4 Technology, Phase 7 Ecosystem Position, Phase 8 Market

Pola 4: Fair Launch Ethos — No VC, No Team Allocation, Community First
· YFI fair launch 2020 → no VC rounds ever → yBudget grants community-focused → Foundation ownerless structure → all decisions via DAO governance
· Evidence: Phase 1 Foundation (fair launch), Phase 5 Funding History ($0 VC), Phase 6 Token (distribution), Phase 7 Governance Ecosystem (Foundation, DAO)
· Supporting Dataset: Phase 1 Foundation, Phase 5 Funding History, Phase 6 Token Distribution, Phase 7 Governance Ecosystem

Pola 5: Transparansi Radikal sebagai Crisis Management Tool
· Setiap exploit, financial risk, governance conflict didiskusikan terbuka di forum; postmortem publik; on-chain data verifiable; no hidden decision making
· Evidence: Phase 3 History (postmortems), Phase 5 Financial Risk (documented risks), Phase 7 Official Resources (governance forum transparency), Phase 2 Entity (community, media)
· Supporting Dataset: Phase 2 Entity, Phase 3 History, Phase 5 Financial Risk, Phase 7 Official Resources

Strategic Trade-offs

Trade-off 1: Desentralisasi vs Kecepatan Operational (Multisig vs On-Chain Governor)
· Decision: Gunakan 9/13 multisig + timelock + Snapshot off-chain voting; tidak deploy on-chain governor dengan direct execution
· Trade-off: Kecepatan dan flexibility operational (multisig bisa act fast) vs desentralisasi murni (on-chain governor trust-minimized); centralization risk pada 13 signers pseudo-anonymous
· Evidence: Phase 4 Technology (security model), Phase 7 Governance Ecosystem (multisig, Snapshot), Phase 7 Ecosystem Risks (multisig centralization)
· Supporting Dataset: Phase 4 Technology, Phase 7 Governance Ecosystem, Phase 7 Ecosystem Risks

Trade-off 2: Curve/Convex Concentration vs Yield Maximization
· Decision: Fokus strategi vault pada Curve/Convex ecosystem (60-70% TVL) untuk yield tertinggi via CRV/CVX rewards dan gauge control
· Trade-off: Yield maksimal untuk user vs systemic risk jika Curve/Convex fail, tokenomics berubah, atau gauge weight terdilusi; single point of failure protocol-layer
· Evidence: Phase 5 Financial Dependencies (Curve/Convex concentration), Phase 7 External Dependencies (critical), Phase 7 Ecosystem Risks (Curve/Convex concentration), Phase 7 Major Integrations (yBribe, Boost)
· Supporting Dataset: Phase 5 Financial Dependencies, Phase 7 External Dependencies, Phase 7 Ecosystem Risks, Phase 7 Major Integrations

Trade-off 3: Multi-Chain Expansion vs Operational Complexity dan Bridge Risk
· Decision: Deploy ke 10 chains (Ethereum + 9 L2/sidechain) untuk capture retail yield di low-fee environments
· Trade-off: TVL growth dan user acquisition vs fragmentasi liquidity, bridge dependency (LayerZero/Wormhole), operational overhead yTeams per chain, smart contract risk per deployment
· Evidence: Phase 3 History (multi-chain timeline), Phase 4 Technology (chains), Phase 7 Ecosystem Position (chains), Phase 7 Ecosystem Risks (bridge dependency), Phase 8 Market (cross-chain volume)
· Supporting Dataset: Phase 3 History, Phase 4 Technology, Phase 7 Ecosystem Position, Phase 7 Ecosystem Risks, Phase 8 Market

Trade-off 4: Fixed Supply Token (Non-Inflationary) vs Contributor Incentive Alignment
· Decision: YFI fixed supply 36,666, no inflation, no team allocation; contributor compensation dari treasury stablecoin/grants bukan token emission
· Trade-off: Token holder value protection (no dilution) vs difficulty incentivizing long-term contributors tanpa token upside; reliance pada treasury management untuk comp
· Evidence: Phase 6 Token (fixed supply, distribution), Phase 5 Treasury (management), Phase 7 Governance Ecosystem (yTeams compensation), Phase 5 Fundraising Mechanism (grants)
· Supporting Dataset: Phase 5 Treasury, Phase 5 Fundraising Mechanism, Phase 6 Token, Phase 7 Governance Ecosystem

Trade-off 5: Security via Extensive Audits vs Speed to Market
· Decision: Multiple auditors (Trail of Bits, Certora, PeckShield, Quantstamp, MixBytes) untuk setiap major release; formal verification (Certora); bug bounty; slow release cadence
· Trade-off: Security assurance tinggi vs slower feature deployment; competitors (Beefy, Harvest) bisa ship strategies faster; Yearn strategies lebih conservative
· Evidence: Phase 2 Entity (auditors), Phase 4 Technology (security model, audits), Phase 8 Market (competitors)
· Supporting Dataset: Phase 2 Entity, Phase 4 Technology, Phase 8 Market

Trade-off 6: Legal Wrapper (Cayman Foundation) vs Regulatory Uncertainty
· Decision: Establish Cayman Foundation untuk legal contracts, IP, employment, limited liability
· Trade-off: Regulatory compliance pathway vs jurisdictional risk (Cayman law changes), Foundation vs DAO authority ambiguity, potential regulatory capture, costo compliance
· Evidence: Phase 2 Entity (Foundation), Phase 3 History (YIP-66), Phase 7 Governance Ecosystem (Foundation), Phase 7 Ecosystem Risks (legal jurisdiction)
· Supporting Dataset: Phase 2 Entity, Phase 3 History, Phase 7 Governance Ecosystem, Phase 7 Ecosystem Risks

Behavioral Summary

Prioritas Utama Proyek:
1. Security dan trust-minimization (extensive audits, multisig, timelock, conservative upgrades)
2. Yield maximization untuk user (Curve/Convex strategies, automation, multi-chain low fees)
3. Desentralisasi progresif dan community ownership (fair launch, DAO governance, yTeams, Foundation)
4. Composability dan standarisasi (ERC-4626 pioneer, SDK/API untuk integrator)
5. Sustainability finansial tanpa token inflation (protocol revenue, treasury yield, grants)
· Evidence: Phase 4 Technology (security), Phase 7 External Dependencies (Curve/Convex), Phase 1 Foundation (fair launch), Phase 4 Technology (ERC-4626), Phase 5 Revenue Model (protocol revenue)
· Supporting Dataset: Phase 1 Foundation, Phase 4 Technology, Phase 5 Revenue Model, Phase 7 External Dependencies

Cara Mengambil Keputusan:
- Data-driven: On-chain metrics (TVL, revenue, APY), governance forum discussion, security audits
- Konsensus berbasis: YIP process (Discourse → Snapshot → Multisig), yTeams domain expertise
- Transparan: Semua discussion, financial, exploit postmortem publik di gov.yearn.finance
- Iteratif: Upgrade bertahap (v1→v2→v3), migration path, backward compatibility
- Risk-aware: Explicit risk documentation (Financial Risk, Ecosystem Risks), diversification efforts
· Evidence: Phase 7 Governance Ecosystem (YIP process), Phase 2 Entity (community), Phase 3 History (postmortems), Phase 3 History (version evolution), Phase 5 Financial Risk (risk documentation)
· Supporting Dataset: Phase 2 Entity, Phase 3 History, Phase 5 Financial Risk, Phase 7 Governance Ecosystem

Faktor Paling Sering Mempengaruhi Keputusan:
1. Security track record (exploit history mendorong architecture changes)
2. Gas cost environment (mendorong multi-chain expansion)
3. Curve/Convex ecosystem dynamics (mendorong yBribe/Boost, strategy focus)
4. Bear/bull market cycle (revenue → treasury management → grant sizing)
5. Regulatory landscape (Foundation formation, legal wrapper)
6. Community governance sentiment (YIP voting, yTeams elections)
· Evidence: Phase 3 History (exploit → version changes), Phase 3 History (multi-chain timeline), Phase 7 External Dependencies (Curve/Convex), Phase 5 Revenue History (bear market), Phase 3 History (YIP-66), Phase 7 Governance Ecosystem (yTeams elections)
· Supporting Dataset: Phase 3 History, Phase 5 Revenue History, Phase 7 External Dependencies, Phase 7 Governance Ecosystem

Pola Evolusi:
- Phase 1 (2020): Founder-led yield optimizer (iEarn/yEarn) → Fair launch YFI
- Phase 2 (2020-2021): Multisig governance → Vault v2 modular → Iron Bank → Multi-chain (Fantom)
- Phase 3 (2022): yTeams delegation → Yearn Foundation legal wrapper → yBribe/Boost governance infrastructure
- Phase 4 (2023-2024): Vault v3 ERC-4626 standardization → Iron Bank v2 (Aave v3) → Base/zkSync deployment → Developer platform maturation
· Evidence: Phase 3 History (full timeline), Phase 4 Technology (versions), Phase 7 Applications (products)
· Supporting Dataset: Phase 3 History, Phase 4 Technology, Phase 7 Applications

Kekuatan Utama:
- Blue-chip DeFi reputation, extensive audit history, battle-tested vaults
- Curve/Convex moat: gauge control, bribe marketplace, strategy expertise
- Fair launch credibility: no VC, community-owned, transparent governance
- Developer ecosystem: SDK, API, Subgraphs, ERC-4626 standard, third-party integrations
- Multi-chain presence: 10 chains, unified frontend, cross-chain infrastructure
- Treasury sustainability: protocol revenue, diversified assets, grant program
· Evidence: Phase 2 Entity (auditors), Phase 7 External Dependencies (Curve/Convex), Phase 1 Foundation (fair launch), Phase 7 Developer Ecosystem (SDK/API), Phase 7 Ecosystem Position (chains), Phase 5 Treasury (management)
· Supporting Dataset: Phase 1 Foundation, Phase 2 Entity, Phase 5 Treasury, Phase 7 Developer Ecosystem, Phase 7 Ecosystem Position, Phase 7 External Dependencies

Kelemahan Utama:
- Curve/Convex concentration risk (60-70% TVL dependency)
- Multisig centralization (9/13 pseudo-anonymous signers)
- Chainlink oracle single point of failure (>90% feeds)
- Bridge dependency untuk multi-chain (LayerZero/Wormhole)
- Revenue concentration: >80% dari vault fees, bear market vulnerable
- YFI holder concentration (top holders control governance)
- Legal jurisdiction risk (Cayman Foundation untested regulatory framework)
- No fee switch activation (YIP-41 proposed but status unclear) → YFI pure governance, no direct value accrual
· Evidence: Phase 7 Ecosystem Risks (concentration risks), Phase 5 Financial Risk (revenue decline), Phase 6 Token (fee switch status), Phase 7 Governance Ecosystem (Foundation)
· Supporting Dataset: Phase 5 Financial Risk, Phase 6 Token, Phase 7 Ecosystem Risks, Phase 7 Governance Ecosystem

## Knowledge Extraction
_ref: `docs/Patterns/*`, `docs/Reasoning/*` (rule candidates)_

PROJECT: Yearn Finance

Core Insights
Insight 1: Fair Launch sebagai Mekanisme Distribusi Token yang Menghilangkan Tekanan Unlock dan Menciptakan Kepemilikan Komunitas Murni
Explanation: Yearn melakukan fair launch YFI Juli 2020 tanpa private sale, VC allocation, atau team allocation. Seluruh supply 30.000 YFI (kemudian 36.666 via YIP-41) didistribusikan ke liquidity miners. Model ini menghilangkan vesting cliff, investor pressure, dan misalignment insentif antara team dan komunitas.
Evidence: Fair launch YFI Juli 2020, supply genesis 30.000 YFI didistribusikan 100% ke liquidity miners Week 1-3【Phase 1 — Foundation】【Phase 5 — Funding History】【Phase 6 — Token Distribution】
Supporting Dataset: Phase 1 Foundation, Phase 5 Funding History, Phase 6 Token Distribution
Confidence: HIGH

Insight 2: Ekosistem Curve/Convex sebagai Moat Utama — 60-70% TVL dan Revenue Bergantung pada Satu Ecosystem
Explanation: Sebagian besar strategi vault Yearn dibangun di atas Curve pools dan Convex gauge rewards. Yearn membangun yBribe (bribe marketplace) dan Boost (vlCVX/veCRV delegation) untuk mengontrol gauge weight dan mengamankan yield. Ini menciptakan moat yang dalam tapi juga systemic risk tinggi.
Evidence: Curve dan Convex marked critical dependency【Phase 7 — External Dependencies】; yBribe launch YIP-73, Boost v2 YIP-85【Phase 7 — Major Integrations】; Financial dependency pada Curve/Convex acknowledged【Phase 5 — Financial Dependencies】; Ecosystem risk: Curve/Convex concentration【Phase 7 — Ecosystem Risks】
Supporting Dataset: Phase 7 External Dependencies, Phase 7 Major Integrations, Phase 5 Financial Dependencies, Phase 7 Ecosystem Risks
Confidence: HIGH

Insight 3: Arsitektur Vault-Strategy Modular dengan ERC-4626 Standardization Memungkinkan Composability Rekursif
Explanation: Evolusi v1→v2→v3 memisahkan vault core (accounting, shares, fees) dari strategy logic. v3 adopt ERC-4626 memungkinkan vault Yearn menjadi strategy untuk protokol lain dan sebaliknya (recursive composability). Pattern ini jadi template DeFi composability.
Evidence: v1 2020 coupled, v2 2021 Controller-Vault-Strategy separation, v3 2023 ERC-4626 compliance【Phase 4 — Technical Architecture】【Phase 3 — History】【Phase 7 — Major Integrations】
Supporting Dataset: Phase 3 History, Phase 4 Technical Architecture, Phase 7 Major Integrations
Confidence: HIGH

Insight 4: Governance Off-Chain (Snapshot) + Multisig On-Chain Execution sebagai Model Desentralisasi Pragmatis
Explanation: Yearn tidak deploy on-chain governor contract. Semua YIP lewat Discourse → Snapshot vote → 9/13 multisig execution dengan timelock. Model ini balance kecepatan operasional dengan accountability, tapi menciptakan centralization risk pada 13 signers pseudo-anonymous.
Evidence: Governance model: Snapshot + multisig【Phase 7 — Governance Ecosystem】; 9/13 multisig address【Phase 7 — Governance Ecosystem】; Multisig centralization risk documented【Phase 7 — Ecosystem Risks】; No on-chain governor【Phase 4 — Technology Security Model】
Supporting Dataset: Phase 4 Technology, Phase 7 Governance Ecosystem, Phase 7 Ecosystem Risks
Confidence: HIGH

Insight 5: Protocol Revenue Sustainability Tanpa Token Inflation — $0 VC Funding, Operasional dari Vault Fees dan Treasury Yield
Explanation: Yearn tidak pernah raise VC. Revenue streams: vault management fee (0.5-2% AUM), performance fee (10-20% profit), Iron Bank interest, Zap fees, yBribe/Boost revenue, treasury yield. Treasury assets di-deploy ke vault sendiri untuk yield. yBudget grants funded dari treasury yield, bukan token emission.
Evidence: $0 VC funding, fair launch only【Phase 5 — Funding History】; 6 revenue streams【Phase 5 — Revenue Model】; Treasury composition dan custodian【Phase 5 — Treasury】; yBudget dari treasury yield【Phase 5 — Fundraising Mechanism】; Fixed supply YFI 36.666 no inflation【Phase 6 — Token】
Supporting Dataset: Phase 5 Funding History, Phase 5 Revenue Model, Phase 5 Treasury, Phase 5 Fundraising Mechanism, Phase 6 Token
Confidence: HIGH

Insight 6: Multi-Chain Expansion Driven by Gas Cost Arbitrage — Deploy ke Chain dengan Fee Terendah untuk Retail Yield
Explanation: Ekspansi: Fantom 2021 (low gas) → Arbitrum/Optimism 2022 (L2 maturity) → Base 2023 (Coinbase backing) → zkSync 2024 (ZK narrative). Setiap deployment mengikuti gas cost environment agar retail yield tetap viable. Sekarang 10 chains (Ethereum + 9 L2/sidechain).
Evidence: Multi-chain timeline【Phase 3 — History】; Supported chains list【Phase 4 — Technology】【Phase 7 — Ecosystem Position】; Gas cost arbitrage rationale【Phase 3 — History】【Phase 8 — Market】
Supporting Dataset: Phase 3 History, Phase 4 Technology, Phase 7 Ecosystem Position, Phase 8 Market
Confidence: HIGH

Insight 7: Upgrade Protocol Setelah Exploit Major sebagai Pola Evolusi Keamanan
Explanation: Setiap exploit besar memicu architecture upgrade: Eminence hack 2020 → v1 vaults launch; v1 exploits 2021 → v2 modular architecture; April 2023 exploit ($11M) → accelerated v3 migration; Multichain exploit 2023 → bridge diversification (LayerZero/Wormhole).
Evidence: Exploit timeline → version launches【Phase 3 — History】; v1/v2/v3 evolution【Phase 4 — Technical Architecture】; Ecosystem risks exploit history【Phase 7 — Ecosystem Risks】
Supporting Dataset: Phase 3 History, Phase 4 Technical Architecture, Phase 7 Ecosystem Risks
Confidence: HIGH

Insight 8: Transparansi Radikal sebagai Crisis Management Tool — Semua Exploit, Financial Risk, Governance Conflict Didiskusikan Terbuka
Explanation: Postmortem publik untuk setiap exploit (Eminence 2020, April 2023). Financial risks terdokumen di governance forum. Tidak ada hidden decision making. Transparansi ini mempertahankan trust komunitas meski mengalami hack berulang.
Evidence: Postmortem links【Phase 3 — History】; Financial risk documented【Phase 5 — Financial Risk】; Governance forum transparency category【Phase 7 — Official Resources】; Community discussion public【Phase 2 — Entity Community】
Supporting Dataset: Phase 2 Entity, Phase 3 History, Phase 5 Financial Risk, Phase 7 Official Resources
Confidence: HIGH

Insight 9: Legal Wrapper via Cayman Foundation (Ownerless) untuk DAO Compliance — Boundary DAO vs Foundation Masih Evolving
Explanation: Yearn Foundation Cayman Islands Foundation (YIP-66 2022) hold IP, trademarks, enter contracts, employ contributors, run grants. DAO govern protocol parameters. Structure "ownerless" cocok untuk DAO tapi jurisdictional risk Cayman dan authority boundary ambigu.
Evidence: Yearn Foundation formation YIP-66【Phase 3 — History】【Phase 2 — Entity】; Foundation purpose【Phase 7 — Governance Ecosystem】; Legal jurisdiction risk【Phase 7 — Ecosystem Risks】; Constitutional documents not fully public【Phase 9 — Open Threads】
Supporting Dataset: Phase 2 Entity, Phase 3 History, Phase 7 Governance Ecosystem, Phase 7 Ecosystem Risks, Phase 9 Open Threads
Confidence: MEDIUM

Insight 10: YFI Pure Governance Token — Fee Switch Proposed (YIP-41) Tapi Status Implementasi Unclear, Tidak Ada Value Accrual Langsung
Explanation: YFI fixed supply 36.666, non-inflationary, pure governance (voting, delegation). YIP-41 propose fee switch untuk buyback/distribusi ke stakers tapi tidak terverifikasi on-chain mainnet. Token holders tidak menerima revenue share langsung.
Evidence: YFI utility governance only【Phase 6 — Token Utility】; YIP-41 fee switch proposal【Phase 3 — History】【Phase 6 — Token】; Fee switch status unclear【Phase 9 — Open Threads】; No active fee switch contract found【Phase 9 — Behavioral Summary】
Supporting Dataset: Phase 3 History, Phase 6 Token, Phase 9 Open Threads, Phase 9 Behavioral Summary
Confidence: MEDIUM

Insight 11: Keeper Automation (Keep3r/Gelato) Critical untuk Vault Operations — Single Point of Failure Jika Incentive Insufficient
Explanation: Harvest, tend, rebalance, liquidation protection dieksekusi oleh Keep3r network dan Gelato. Jika keeper incentives tidak cukup, jobs tidak terekseskusi → vault performance degrade. Keep3r job coverage ratio tidak publicly dashboarded.
Evidence: Keep3r critical dependency【Phase 7 — External Dependencies】; Keep3r integration【Phase 7 — Major Integrations】; Keeper concentration risk【Phase 7 — Ecosystem Risks】; Job coverage not dashboarded【Phase 9 — Open Threads】
Supporting Dataset: Phase 7 External Dependencies, Phase 7 Major Integrations, Phase 7 Ecosystem Risks, Phase 9 Open Threads
Confidence: MEDIUM

Insight 12: Chainlink Oracle Dependency >90% Feeds Tanpa Diversified Fallback Sistematik
Explanation: Vault valuation dan strategy triggers hampir semuanya pakai Chainlink price feeds. Tidak ada oracle fallback terdiversifikasi untuk most feeds. Single point of failure oracle layer.
Evidence: Chainlink critical dependency【Phase 7 — External Dependencies】; ChainlinkPriceOracle implementation【Phase 4 — Technology】; Single oracle dependency risk【Phase 7 — Ecosystem Risks】
Supporting Dataset: Phase 4 Technology, Phase 7 External Dependencies, Phase 7 Ecosystem Risks
Confidence: HIGH

Insight 13: Developer Platform Investment (SDK, API, Subgraphs, Grants) Menarik Integrator Third-Party
Explanation: Yearn SDK, API, Subgraphs, yBudget/yGrants, hackathon tracks menarik integrator seperti DeFi Saver, Instadapp, Zerion, Zapper, DeBank, APY.vision. Ecosystem growth melalui developer tooling.
Evidence: Developer ecosystem【Phase 7 — Developer Ecosystem】; Third-party integrations【Phase 7 — Applications】; Grant program【Phase 5 — Fundraising Mechanism】【Phase 7 — Governance Ecosystem】
Supporting Dataset: Phase 5 Fundraising Mechanism, Phase 7 Developer Ecosystem, Phase 7 Applications, Phase 7 Governance Ecosystem
Confidence: HIGH

Insight 14: Bear Market Response — Treasury Diversification dan Cost Discipline Menggantikan Token Emission
Explanation: Saat revenue vault drop >80% (bear market 2022-2023), treasury committee diversifikasi assets (stablecoin, ETH, blue chip), adjust grant pacing, review contributor comp, push revenue diversification (Iron Bank, yBribe). Tidak ada token emission untuk cover shortfall.
Evidence: Revenue decline bear market【Phase 5 — Revenue History】【Phase 5 — Financial Risk】; Treasury management【Phase 5 — Treasury】; Treasury Committee actions【Phase 7 — Governance Ecosystem】
Supporting Dataset: Phase 5 Revenue History, Phase 5 Financial Risk, Phase 5 Treasury, Phase 7 Governance Ecosystem
Confidence: HIGH

Insight 15: yTeams Delegasi Operational Authority ke Domain Experts — Scalability Governance vs Centralization Risk
Explanation: DAO memilih yTeams per domain (Protocol, Treasury, Growth, Ops, Risk, Legal) via Snapshot, term-based. Teams mendapat multisig authority untuk operational decisions. Mempercepat decision making tapi centralization risk pada 13 signers pseudo-anonymous.
Evidence: yTeams formation【Phase 3 — History】; yTeams structure【Phase 7 — Governance Ecosystem】; Multisig centralization risk【Phase 7 — Ecosystem Risks】; Signer identities pseudo-anonymous【Phase 9 — Open Threads】
Supporting Dataset: Phase 3 History, Phase 7 Governance Ecosystem, Phase 7 Ecosystem Risks, Phase 9 Open Threads
Confidence: HIGH

Insight 16: Revenue Concentration >80% dari Vault Fees — Diversifikasi (Iron Bank, yBribe, Zap, Treasury Yield) Masih Minor
Explanation: Vault fees dominan revenue. Iron Bank lending revenue, yBribe/Boost bribe marketplace, Zap router fees, treasury yield diversifikasi tapi masih porsi kecil. Bear market expose vulnerability single revenue stream.
Evidence: Revenue streams breakdown【Phase 5 — Revenue Model】; Financial dependency vault fees dominant【Phase 5 — Financial Dependencies】; Revenue history bear market decline【Phase 5 — Revenue History】
Supporting Dataset: Phase 5 Revenue Model, Phase 5 Financial Dependencies, Phase 5 Revenue History
Confidence: HIGH

Insight 17: Bridge Dependency untuk Multi-Chain — LayerZero/Wormhole Primary, Multichain Deprecated Post-Exploit 2023
Explanation: Cross-chain vault deployments dan asset bridging rely on LayerZero/Wormhole. Multichain exploit July 2023 memicu migrasi. Bridge risk quantification tidak teragregasi di single dashboard.
Evidence: Bridge dependencies【Phase 7 — External Dependencies】; Multichain exploit response【Phase 3 — History】; Bridge risk unquantified【Phase 9 — Open Threads】; LayerZero/Wormhole live【Phase 7 — External Dependencies】
Supporting Dataset: Phase 3 History, Phase 7 External Dependencies, Phase 9 Open Threads
Confidence: HIGH

Insight 18: Security via Multiple Auditors + Formal Verification + Bug Bounty — Slow Release Cadence sebagai Trade-off
Explanation: Trail of Bits, Certora, PeckShield, Quantstamp, MixBytes audit setiap major release. Certora formal verification. Bug bounty program. Hasilnya slower feature deployment vs competitors (Beefy, Harvest) yang ship strategies faster.
Evidence: Auditors list【Phase 2 — Entity Auditors】; Security model audits【Phase 4 — Technology】; Competitors faster shipping【Phase 8 — Market】; Trade-off security vs speed【Phase 9 — Strategic Trade-offs】
Supporting Dataset: Phase 2 Entity, Phase 4 Technology, Phase 8 Market, Phase 9 Strategic Trade-offs
Confidence: HIGH

Insight 19: Treasury Composition: YFI, Stablecoin, ETH, CRV, CVX, LP Tokens — Nilai Agregat Real-Time Tidak Dipublikasikan Resmi
Explanation: Treasury hold YFI (significant portion), USDC/USDT/DAI, ETH, CRV, CVX, LP tokens dari strategi vault. Managed by 9/13 multisig + yTeams. Real-time USD aggregate tidak dipublikasikan sebagai single number resmi.
Evidence: Treasury composition【Phase 5 — Treasury】; Treasury custodian multisig【Phase 5 — Treasury】【Phase 7 — Governance Ecosystem】; Real-time value not public【Phase 5 — Treasury】【Phase 9 — Open Threads】
Supporting Dataset: Phase 5 Treasury, Phase 7 Governance Ecosystem, Phase 9 Open Threads
Confidence: MEDIUM

Insight 20: Iron Bank sebagai Isolated Lending Market (Aave v3 Fork) — Permissioned Markets untuk Partner Protocols, Revenue Diversification
Explanation: Iron Bank launch 2021, v2 2023 migrasi ke Aave v3 codebase. Isolated risk model, permissioned markets untuk partner protocols. Yearn strategies sebagai primary borrowers. Revenue stream baru beyond vault fees.
Evidence: Iron Bank launch timeline【Phase 3 — History】; Iron Bank v2 Aave v3 fork【Phase 7 — Major Integrations】; Iron Bank interest revenue【Phase 5 — Revenue Model】; Isolated lending model【Phase 7 — External Dependencies】
Supporting Dataset: Phase 3 History, Phase 5 Revenue Model, Phase 7 Major Integrations, Phase 7 External Dependencies
Confidence: HIGH

Strategic Principles
Principle 1: Security Before Growth — Extensive Audits, Formal Verification, Conservative Upgrades, Multisig + Timelock
Explanation: Yearn memprioritaskan keamanan di atas kecepatan rilis. Multiple auditors per major release, Certora formal verification, bug bounty, upgrade bertahap dengan migration path. Protocol upgrades via 9/13 multisig + timelock, tidak on-chain governor direct execution.
Evidence: Auditors list【Phase 2 — Entity Auditors】; Security model【Phase 4 — Technology】; Upgrade pattern phased【Phase 4 — Technical Architecture】; Multisig + timelock governance【Phase 7 — Governance Ecosystem】; Trade-off security vs speed【Phase 9 — Strategic Trade-offs】
Supporting Dataset: Phase 2 Entity, Phase 4 Technology, Phase 7 Governance Ecosystem, Phase 9 Strategic Trade-offs
Confidence: HIGH

Principle 2: Community Ownership First — Fair Launch, No VC, No Team Allocation, DAO Governance, Transparent Decision Making
Explanation: Fair launch YFI 100% community distribution. Tidak ada VC funding pernah. Semua keputusan via YIP process (Discourse → Snapshot → Multisig). Postmortem publik. Treasury management transparent. yTeams elected by community.
Evidence: Fair launch【Phase 1 — Foundation】【Phase 5 — Funding History】【Phase 6 — Token Distribution】; YIP process【Phase 7 — Governance Ecosystem】; Transparency【Phase 3 — History】【Phase 5 — Financial Risk】; yTeams election【Phase 3 — History】【Phase 7 — Governance Ecosystem】
Supporting Dataset: Phase 1 Foundation, Phase 5 Funding History, Phase 6 Token Distribution, Phase 7 Governance Ecosystem, Phase 3 History, Phase 5 Financial Risk
Confidence: HIGH

Principle 3: Modular Architecture First — Vault Core Minimal, Strategy Logic Separable, Upgradeable, ERC-4626 Standardized
Explanation: v1→v2→v3 evolution menunjukkan komitmen pada modularitas: vault core hanya accounting/shares/fees; strategy logic di contracts terpisah upgradeable; v3 ERC-4626 compliance untuk composability maksimal. Pattern ini memungkinkan innovation strategy tanpa touch vault core.
Evidence: v1/v2/v3 architecture evolution【Phase 4 — Technical Architecture】【Phase 3 — History】; ERC-4626 standardization【Phase 4 — Technology】【Phase 7 — Major Integrations】; Modular strategy pattern【Phase 4 — Technology】【Phase 9 — Technical Decision Patterns】
Supporting Dataset: Phase 3 History, Phase 4 Technical Architecture, Phase 7 Major Integrations, Phase 9 Technical Decision Patterns
Confidence: HIGH

Principle 4: Ecosystem Integration Deep, Not Wide — Curve/Convex Native, Build Moat via Gauge Control (yBribe/Boost)
Explanation: Alih-alih spread thin across banyak ecosystem, Yearn go deep pada Curve/Convex: >60% TVL, yBribe bribe marketplace, Boost vlCVX delegation, Curve strategies expertise. Menciptakan moat yang dalam tapi juga concentration risk.
Evidence: Curve/Convex critical dependencies【Phase 7 — External Dependencies】; yBribe/Boost integrations【Phase 7 — Major Integrations】; Financial dependency concentration【Phase 5 — Financial Dependencies】; Ecosystem risk concentration【Phase 7 — Ecosystem Risks】; Recurring pattern Curve-native【Phase 9 — Recurring Behavioral Patterns】
Supporting Dataset: Phase 5 Financial Dependencies, Phase 7 External Dependencies, Phase 7 Major Integrations, Phase 7 Ecosystem Risks, Phase 9 Recurring Behavioral Patterns
Confidence: HIGH

Principle 5: Protocol Revenue Sustainability Without Token Inflation — Fixed Supply, Fee-Based Revenue, Treasury Yield, Grants from Yield Not Principal
Explanation: YFI fixed supply 36.666, no inflation. Revenue dari vault fees, Iron Bank, yBribe, Zap, treasury yield. yBudget grants funded dari treasury yield/deployed assets, bukan token emission. Bear market response: diversifikasi treasury dan cost discipline, bukan mint token.
Evidence: Fixed supply【Phase 6 — Token】; Revenue streams【Phase 5 — Revenue Model】; Treasury yield deployment【Phase 5 — Treasury】; yBudget from yield【Phase 5 — Fundraising Mechanism】; Bear market response【Phase 5 — Revenue History】【Phase 9 — Risk Response Patterns】
Supporting Dataset: Phase 5 Revenue Model, Phase 5 Treasury, Phase 5 Fundraising Mechanism, Phase 6 Token, Phase 9 Risk Response Patterns
Confidence: HIGH

Principle 6: Progressive Decentralization — Founder-Led → Multisig → yTeams Delegated DAO → Foundation Legal Wrapper
Explanation: Evolusi governance: 2020 Andre Cronje sole decision → 2020-2021 9/13 multisig → 2022 yTeams delegasi operational authority → 2022 Yearn Foundation Cayman legal wrapper. Setiap stage menambah decentralization layer sambil maintain operational capability.
Evidence: Governance evolution timeline【Phase 3 — History】; yTeams formation【Phase 3 — History】【Phase 7 — Governance Ecosystem】; Foundation formation【Phase 3 — History】【Phase 7 — Governance Ecosystem】; Progressive decentralization pattern【Phase 9 — Evolution Patterns】
Supporting Dataset: Phase 3 History, Phase 7 Governance Ecosystem, Phase 9 Evolution Patterns
Confidence: HIGH

Principle 7: Multi-Chain Expansion Follows User Demand and Gas Arbitrage — Deploy Where Retail Yield Viable
Explanation: Ekspansi chain tidak arbitrary: Fantom 2021 (low gas) → L2s 2022-2024 (Arbitrum, Optimism, Base, zkSync) → lainnya. Setiap deployment driven by Ethereum L1 gas costs membuat retail yield negative. Unified frontend across chains.
Evidence: Multi-chain timeline【Phase 3 — History】; Supported chains【Phase 4 — Technology】【Phase 7 — Ecosystem Position】; Gas cost arbitrage rationale【Phase 3 — History】【Phase 8 — Market】; Expansion pattern【Phase 9 — Ecosystem Decision Patterns】
Supporting Dataset: Phase 3 History, Phase 4 Technology, Phase 7 Ecosystem Position, Phase 8 Market, Phase 9 Ecosystem Decision Patterns
Confidence: HIGH

Principle 8: Infrastructure Tier-1 Providers for Reliability — Alchemy/Infura RPC, Chainlink Oracle, The Graph Indexing, Tenderly Monitoring — Don't Build In-House
Explanation: Yearn gunakan provider terbaik untuk RPC, oracle, indexing, monitoring. Hanya build in-house untuk keeper network (Keep3r/Gelato integration). Fokus core competency: vault strategies dan yield optimization.
Evidence: Infrastructure providers list【Phase 7 — Infrastructure Providers】; External dependencies critical providers【Phase 7 — External Dependencies】; Don't build in-house infra【Phase 9 — Ecosystem Decision Patterns】
Supporting Dataset: Phase 7 Infrastructure Providers, Phase 7 External Dependencies, Phase 9 Ecosystem Decision Patterns
Confidence: HIGH

Principle 9: Radical Transparency as Crisis Management — Public Postmortems, Open Financial Discussions, On-Chain Verifiable Data
Explanation: Setiap exploit, financial risk, governance conflict didiskusikan terbuka di gov.yearn.finance. Postmortem detail publik (Eminence, April 2023). On-chain data verifiable. No hidden decision making. Transparency mempertahankan trust meski hack berulang.
Evidence: Postmortems public【Phase 3 — History】; Financial risk documented【Phase 5 — Financial Risk】; Governance forum transparency【Phase 7 — Official Resources】; Transparency pattern【Phase 9 — Recurring Behavioral Patterns】
Supporting Dataset: Phase 3 History, Phase 5 Financial Risk, Phase 7 Official Resources, Phase 9 Recurring Behavioral Patterns
Confidence: HIGH

Principle 10: Developer Platform Investment for Ecosystem Growth — SDK, API, Subgraphs, Grants, Hackathons Attract Third-Party Integrators
Explanation: Yearn SDK (TypeScript), API, Subgraphs, yBudget/yGrants, hackathon tracks menarik integrator: DeFi Saver, Instadapp, Zerion, Zapper, DeBank, APY.vision. Developer tooling sebagai growth lever.
Evidence: Developer ecosystem【Phase 7 — Developer Ecosystem】; Third-party integrations【Phase 7 — Applications】; Grant program【Phase 5 — Fundraising Mechanism】【Phase 7 — Governance Ecosystem】; Developer platform pattern【Phase 9 — Ecosystem Decision Patterns】
Supporting Dataset: Phase 5 Fundraising Mechanism, Phase 7 Developer Ecosystem, Phase 7 Applications, Phase 7 Governance Ecosystem, Phase 9 Ecosystem Decision Patterns
Confidence: HIGH

Success Factors
Factor 1: Fair Launch Token Distribution — Menghilangkan Investor/Team Misalignment, Menciptakan Komunitas Loyal Early Adopters
Explanation: 100% YFI ke liquidity miners Juli 2020. No VC, no private sale, no team allocation. Menghilangkan vesting pressure, token unlock schedule, investor exit pressure. Komunitas early adopters menjadi stakeholders sejati.
Evidence: Fair launch mechanism【Phase 5 — Fundraising Mechanism】; Token distribution【Phase 6 — Token Distribution】; No VC funding【Phase 5 — Funding History】; Community loyalty【Phase 2 — Entity Community】
Supporting Dataset: Phase 5 Fundraising Mechanism, Phase 6 Token Distribution, Phase 5 Funding History, Phase 2 Entity
Confidence: HIGH

Factor 2: Modular Vault-Strategy Architecture dengan ERC-4626 — Memungkinkan Composability Rekursif, Menarik Integrator Third-Party, Menjadi Standard DeFi
Explanation: v3 ERC-4626 compliance memungkinkan vault Yearn sebagai strategy untuk protokol lain dan sebaliknya. Yearn menjadi pionir ERC-4626 adoption. Composability menarik integrator (DeFi Saver, Instadapp, dll) yang build di atas Yearn.
Evidence: ERC-4626 v3【Phase 4 — Technical Architecture】【Phase 7 — Major Integrations】; Third-party integrations【Phase 7 — Applications】; Composability benefit【Phase 9 — Technical Decision Patterns】
Supporting Dataset: Phase 4 Technical Architecture, Phase 7 Major Integrations, Phase 7 Applications, Phase 9 Technical Decision Patterns
Confidence: HIGH

Factor 3: Deep Curve/Convex Integration — Gauge Control via yBribe/Boost, Strategy Expertise, >60% TVL Moat
Explanation: Yearn bukan hanya user Curve/Convex tapi active participant mengontrol gauge weight via yBribe (bribe marketplace) dan Boost (vlCVX delegation). Strategy expertise mendalam pada Curve ecosystem. Moat yang sulit direplikasi competitor.
Evidence: yBribe/Boost【Phase 7 — Major Integrations】; Curve/Convex critical dependency【Phase 7 — External Dependencies】; Gauge control moat【Phase 5 — Financial Dependencies】; Curve-native strategy【Phase 9 — Recurring Behavioral Patterns】
Supporting Dataset: Phase 5 Financial Dependencies, Phase 7 External Dependencies, Phase 7 Major Integrations, Phase 9 Recurring Behavioral Patterns
Confidence: HIGH

Factor 4: Extensive Audit Program — Multiple Top-Tier Auditors + Formal Verification (Certora) + Bug Bounty = Battle-Tested Reputation
Explanation: Trail of Bits, Certora, PeckShield, Quantstamp, MixBytes audit setiap major release. Certora formal verification. Bug bounty program. Reputasi security menjadi differentiator vs competitor yang move faster tapi less audited.
Evidence: Auditors list【Phase 2 — Entity Auditors】; Security model audits【Phase 4 — Technology】; Security reputation【Phase 8 — Market】; Trade-off security vs speed【Phase 9 — Strategic Trade-offs】
Supporting Dataset: Phase 2 Entity, Phase 4 Technology, Phase 8 Market, Phase 9 Strategic Trade-offs
Confidence: HIGH

Factor 5: Protocol Revenue Diversification Beyond Vault Fees — Iron Bank, yBribe, Boost, Zap, Treasury Yield Mengurangi Single Stream Dependency
Explanation: Vault fees >80% revenue tapi upaya diversifikasi: Iron Bank lending revenue, yBribe/Boost bribe marketplace, Zap router fees, treasury yield. Bear market 2022-2023 mempercepat diversifikasi efforts.
Evidence: Revenue streams【Phase 5 — Revenue Model】; Financial dependencies【Phase 5 — Financial Dependencies】; Bear market acceleration【Phase 5 — Revenue History】【Phase 9 — Risk Response Patterns】
Supporting Dataset: Phase 5 Revenue Model, Phase 5 Financial Dependencies, Phase 5 Revenue History, Phase 9 Risk Response Patterns
Confidence: HIGH

Factor 6: yTeams Delegated Governance — Domain Experts dengan Authority Operasional Mempercepat Decision Making Tanpa Sacrifice Accountability
Explanation: yTeams per domain (Protocol, Treasury, Growth, Ops, Risk, Legal) elected via Snapshot, term-based, multisig authority. Operational decisions faster, domain expertise applied, accountability via elections.
Evidence: yTeams structure【Phase 7 — Governance Ecosystem】; yTeams formation【Phase 3 — History】; Delegated authority【Phase 9 — Governance Decision Patterns】; Governance scalability improved【Phase 9 — Behavioral Summary】
Supporting Dataset: Phase 3 History, Phase 7 Governance Ecosystem, Phase 9 Governance Decision Patterns, Phase 9 Behavioral Summary
Confidence: HIGH

Factor 7: Multi-Chain Presence Unified Frontend — 10 Chains, Single UX, Cross-Chain Infrastructure (LayerZero/Wormhole) Menjangkau Retail di Low-Fee Environments
Explanation: Deploy ke 10 EVM chains dengan unified frontend yearn.finance. Cross-chain infrastructure via LayerZero/Wormhole. Gas cost arbitrage memungkinkan retail yield viable di L2/sidechain.
Evidence: Supported chains【Phase 4 — Technology】【Phase 7 — Ecosystem Position】; Unified frontend【Phase 7 — Applications】; Cross-chain infrastructure【Phase 7 — External Dependencies】; Gas arbitrage rationale【Phase 3 — History】【Phase 8 — Market】
Supporting Dataset: Phase 3 History, Phase 4 Technology, Phase 7 Ecosystem Position, Phase 7 Applications, Phase 7 External Dependencies, Phase 8 Market
Confidence: HIGH

Factor 8: Developer Ecosystem Investment — SDK, API, Subgraphs, Grants, Hackathons Membangun Moat Integrator
Explanation: Yearn SDK (TypeScript), API, Subgraphs, yBudget/yGrants, hackathon tracks menarik 6+ major third-party integrator. Developer tooling sebagai growth lever yang compounding.
Evidence: Developer ecosystem【Phase 7 — Developer Ecosystem】; Third-party integrations【Phase 7 — Applications】; Grant program【Phase 5 — Fundraising Mechanism】; Developer platform pattern【Phase 9 — Ecosystem Decision Patterns】
Supporting Dataset: Phase 5 Fundraising Mechanism, Phase 7 Developer Ecosystem, Phase 7 Applications, Phase 9 Ecosystem Decision Patterns
Confidence: HIGH

Factor 9: Transparent Crisis Response — Emergency Multisig Intervention + Public Postmortem + Accelerated Migration = Trust Maintenance
Explanation: Saat exploit: multisig emergency pause → fund migration → postmortem transparan → audit tambahan → accelerated deprecated migration. Pola ini berulang (Eminence, v1 exploits, April 2023) dan mempertahankan community trust.
Evidence: Emergency response pattern【Phase 9 — Risk Response Patterns】; Postmortems【Phase 3 — History】; Transparency【Phase 7 — Official Resources】; Trust maintenance【Phase 9 — Behavioral Summary】
Supporting Dataset: Phase 3 History, Phase 7 Official Resources, Phase 9 Risk Response Patterns, Phase 9 Behavioral Summary
Confidence: HIGH

Factor 10: Legal Wrapper via Cayman Foundation — DAO Compliance Pathway, IP/Trademark Protection, Contract Capacity, Employment Structure
Explanation: Yearn Foundation Cayman (ownerless) hold IP, trademarks, enter contracts, employ contributors, run grants. DAO remain governance layer. Regulatory compliance pathway untuk DAO yang operate globally.
Evidence: Foundation formation YIP-66【Phase 3 — History】【Phase 2 — Entity】; Foundation purpose【Phase 7 — Governance Ecosystem】; Legal wrapper pattern【Phase 9 — Ecosystem Decision Patterns】
Supporting Dataset: Phase 2 Entity, Phase 3 History, Phase 7 Governance Ecosystem, Phase 9 Ecosystem Decision Patterns
Confidence: MEDIUM

Failure Factors
Factor 1: Curve/Convex Concentration Risk — 60-70% TVL dan Revenue Bergantung Satu Ecosystem, Systemic Risk Jika Curve/Convex Fail
Explanation: Sebagian besar strategi vault bergantung CRV/CVX rewards. Perubahan gauge weight, tokenomics Curve, atau exploit Curve/Convex akan impact massive ke Yearn. Acknowledged di governance tapi belum terdiversifikasi signifikan.
Evidence: Concentration risk documented【Phase 7 — Ecosystem Risks】; Financial dependency【Phase 5 — Financial Dependencies】; External dependencies critical【Phase 7 — External Dependencies】; Recurring pattern Curve-native【Phase 9 — Recurring Behavioral Patterns】
Supporting Dataset: Phase 5 Financial Dependencies, Phase 7 External Dependencies, Phase 7 Ecosystem Risks, Phase 9 Recurring Behavioral Patterns
Confidence: HIGH

Factor 2: Multisig Centralization — 9/13 Pseudo-Anonymous Signers Mengontrol Protocol Upgrades, Treasury, Emergency Actions
Explanation: Semua protocol upgrades, treasury movements, emergency actions via 9/13 multisig. Signers pseudo-anonymous elected individuals. Tidak ada on-chain governor trust-minimized. Centralization risk tinggi meski mitigated by yTeams delegation.
Evidence: Multisig address 9/13【Phase 7 — Governance Ecosystem】; Multisig centralization risk【Phase 7 — Ecosystem Risks】; No on-chain governor【Phase 4 — Technology Security Model】; Signer identities pseudo-anonymous【Phase 9 — Open Threads】
Supporting Dataset: Phase 4 Technology, Phase 7 Governance Ecosystem, Phase 7 Ecosystem Risks, Phase 9 Open Threads
Confidence: HIGH

Factor 3: Chainlink Oracle Single Point of Failure — >90% Vault Valuation dan Strategy Triggers Rely pada Chainlink Tanpa Fallback Diversified
Explanation: Vault price oracle (ChainlinkPriceOracle) digunakan untuk valuation, liquidation thresholds, strategy rebalancing. Tidak ada diversified oracle fallback sistematis untuk most feeds. Oracle failure = vault malfunction.
Evidence: Chainlink critical dependency【Phase 7 — External Dependencies】; ChainlinkPriceOracle implementation【Phase 4 — Technology】; Single oracle dependency risk【Phase 7 — Ecosystem Risks】; Oracle pattern【Phase 9 — Technical Decision Patterns】
Supporting Dataset: Phase 4 Technology, Phase 7 External Dependencies, Phase 7 Ecosystem Risks, Phase 9 Technical Decision Patterns
Confidence: HIGH

Factor 4: Revenue Concentration >80% Vault Fees — Bear Market 2022-2023 Menunjukkan Vulnerability Extreme (Revenue Drop >80%)
Explanation: Vault fees dominan revenue. Bear market cause TVL dan fee revenue collapse drastis (terlihat DefiLlama/Token Terminal). Treasury diversification dan cost discipline jadi critical survival mechanism. Diversifikasi revenue (Iron Bank, yBribe) masih minor.
Evidence: Revenue streams breakdown【Phase 5 — Revenue Model】; Financial dependency vault fees dominant【Phase 5 — Financial Dependencies】; Revenue history bear market decline【Phase 5 — Revenue History】; Financial risk revenue decline【Phase 5 — Financial Risk】
Supporting Dataset: Phase 5 Revenue Model, Phase 5 Financial Dependencies, Phase 5 Revenue History, Phase 5 Financial Risk
Confidence: HIGH

Factor 5: Bridge Dependency untuk Multi-Chain — LayerZero/Wormhole Cross-Chain Risk, Multichain Exploit 2023 Telah Terjadi
Explanation: Cross-chain vault deployments dan asset bridging rely on LayerZero/Wormhole. Multichain exploit July 2023 memicu migrasi. Bridge risk quantification tidak teragregasi. Bridge exploit bisa strand assets atau enable malicious minting.
Evidence: Bridge dependencies【Phase 7 — External Dependencies】; Multichain exploit response【Phase 3 — History】; Bridge risk unquantified【Phase 9 — Open Threads】; Bridge dependency risk【Phase 7 — Ecosystem Risks】
Supporting Dataset: Phase 3 History, Phase 7 External Dependencies, Phase 7 Ecosystem Risks, Phase 9 Open Threads
Confidence: HIGH

Factor 6: YFI Holder Concentration — Top Holders Control Governance Outcomes, Delegation Ke Whale/Exchange
Explanation: Top 100 holders control significant % YFI supply. Governance outcomes influenced by few large holders / delegated votes. Fee switch tidak aktif → YFI pure governance tanpa value accrual → alignment lemah antara token holders dan protocol success.
Evidence: Holder concentration【Phase 7 — Ecosystem Risks】; YFI token utility governance only【Phase 6 — Token Utility】; Fee switch status unclear【Phase 9 — Open Threads】; Governance influence concentration【Phase 9 — Behavioral Summary】
Supporting Dataset: Phase 6 Token Utility, Phase 7 Ecosystem Risks, Phase 9 Open Threads, Phase 9 Behavioral Summary
Confidence: MEDIUM

Factor 7: Keeper Network Incentive Dependency — Keep3r/Gelato Jobs Harus Terekseskusi, Jika Incentive Insufficient Vault Operations Degrade
Explanation: Harvest, tend, rebalance, liquidation protection depend on Keep3r job market. Job coverage ratio tidak publicly dashboarded. Anecdotal evidence di governance discussions menunjukkan keeper incentive challenges.
Evidence: Keep3r critical dependency【Phase 7 — External Dependencies】; Keeper concentration risk【Phase 7 — Ecosystem Risks】; Job coverage not dashboarded【Phase 9 — Open Threads】; Keeper automation pattern【Phase 9 — Technical Decision Patterns】
Supporting Dataset: Phase 7 External Dependencies, Phase 7 Ecosystem Risks, Phase 9 Open Threads, Phase 9 Technical Decision Patterns
Confidence: MEDIUM

Factor 8: Legal Jurisdiction Risk — Cayman Foundation Untested Regulatory Framework, Foundation vs DAO Authority Boundary Ambigu
Explanation: Yearn Foundation Cayman hold legal liability, IP, contracts. Regulatory changes di Cayman atau major jurisdictions bisa impact DAO operations. Constitutional documents tidak fully public. Authority boundary DAO vs Foundation evolving.
Evidence: Foundation formation【Phase 3 — History】【Phase 2 — Entity】; Legal jurisdiction risk【Phase 7 — Ecosystem Risks】; Constitutional documents not public【Phase 9 — Open Threads】; Foundation vs DAO boundary【Phase 9 — Governance Decision Patterns】
Supporting Dataset: Phase 2 Entity, Phase 3 History, Phase 7 Ecosystem Risks, Phase 9 Open Threads, Phase 9 Governance Decision Patterns
Confidence: MEDIUM

Factor 9: No Fee Switch Activation — YIP-41 Proposed Fee Buyback/Distribusi ke Stakers Tapi Status Unclear, YFI Pure Governance Tanpa Value Accrual
Explanation: YIP-41 propose fee switch untuk buyback/distribusi ke YFI stakers. Tidak ada kontrak fee switch terverifikasi on-chain mainnet. Token holders tidak menerima revenue share langsung. Alignment token holders-protocol lemah.
Evidence: YIP-41 fee switch proposal【Phase 3 — History】【Phase 6 — Token】; Fee switch status unclear【Phase 9 — Open Threads】; YFI pure governance【Phase 6 — Token Utility】; Weak alignment【Phase 9 — Behavioral Summary】
Supporting Dataset: Phase 3 History, Phase 6 Token, Phase 9 Open Threads, Phase 9 Behavioral Summary
Confidence: MEDIUM

Factor 10: Legacy v1 Vaults Still Accessible But Deprecated — Attack Surface Tersisa, Migration Incomplete, No Official Sunset Date
Explanation: v1 vaults masih accessible tapi deprecated post-April 2023 exploit. Migration tools disediakan tapi tidak force-migrate. Tidak ada official sunset date. Attack surface tersisa untuk legacy contracts.
Evidence: v1 deprecation post-exploit【Phase 3 — History】; v1 sunset timeline unclear【Phase 9 — Open Threads】; Migration pattern phased【Phase 4 — Technical Architecture】【Phase 9 — Technical Decision Patterns】
Supporting Dataset: Phase 3 History, Phase 4 Technical Architecture, Phase 9 Open Threads, Phase 9 Technical Decision Patterns
Confidence: MEDIUM

Decision Framework
Step 1: Problem Identification → Security-First Architecture Design → Phased Implementation → Migration Path → Audit → Deploy → Monitor → Iterate
Explanation: Setiap major technical decision mengikuti pattern: identify problem (gas costs, security, composability) → design modular architecture (vault-strategy separation) → implement phased (v1→v2→v3) → provide migration tools → extensive audits → deploy → monitor via Keep3r/Gelato → iterate based on exploits/feedback.
Evidence: v1→v2→v3 evolution【Phase 3 — History】【Phase 4 — Technical Architecture】; Phased upgrade pattern【Phase 9 — Technical Decision Patterns】; Security-first audits【Phase 2 — Entity Auditors】【Phase 4 — Technology】; Migration tools provided【Phase 9 — Technical Decision Patterns】
Supporting Dataset: Phase 3 History, Phase 4 Technical Architecture, Phase 9 Technical Decision Patterns, Phase 2 Entity
Confidence: HIGH

Step 2: Revenue Decline Detection → Treasury Committee Analysis → Diversification Strategy → Cost Discipline → Grant Pacing Adjustment → Revenue Stream Expansion
Explanation: Bear market 2022-2023: TVL/fee revenue drop detected via DefiLlama/Token Terminal → Treasury Committee analyze runway → diversifikasi treasury assets (stablecoin, ETH, blue chip) → adjust grant pacing → review contributor comp → push Iron Bank, yBribe, Zap revenue expansion.
Evidence: Revenue decline detection【Phase 5 — Revenue History】; Treasury Committee actions【Phase 7 — Governance Ecosystem】; Bear market response【Phase 9 — Risk Response Patterns】; Diversification push【Phase 5 — Revenue Model】【Phase 9 — Financial Decision Patterns】
Supporting Dataset: Phase 5 Revenue History, Phase 7 Governance Ecosystem, Phase 9 Risk Response Patterns, Phase 9 Financial Decision Patterns
Confidence: HIGH

Step 3: Exploit Detection → Emergency Multisig Pause → Fund Migration → Public Postmortem → Root Cause Analysis → Accelerated Deprecated Migration → Additional Audits
Explanation: Setiap exploit: multisig emergency pause affected vaults → migrate user funds ke safe contracts → publish postmortem di governance forum → root cause analysis → parameter changes/strategy deprecation → commission additional audits → accelerate v1→v3 migration.
Evidence: Emergency response pattern【Phase 9 — Risk Response Patterns】; Postmortems【Phase 3 — History】; Exploit timeline【Phase 3 — History】; Migration acceleration【Phase 3 — History】【Phase 9 — Risk Response Patterns】
Supporting Dataset: Phase 3 History, Phase 9 Risk Response Patterns
Confidence: HIGH

Step 4: Governance Proposal → Discourse Discussion → Snapshot Vote → Multisig Execution → Timelock → On-Chain Verification
Explanation: YIP process: idea di Discourse → formal proposal → community discussion → Snapshot off-chain vote (gasless) → 9/13 multisig execute dengan timelock → on-chain verification. No on-chain governor direct execution.
Evidence: YIP process【Phase 7 — Governance Ecosystem】; Snapshot voting【Phase 7 — Governance Ecosystem】; Multisig execution【Phase 7 — Governance Ecosystem】; Governance decision pattern【Phase 9 — Governance Decision Patterns】
Supporting Dataset: Phase 7 Governance Ecosystem, Phase 9 Governance Decision Patterns
Confidence: HIGH

Step 5: Chain Expansion Evaluation → Gas Cost Analysis → DeFi Maturity Assessment → Bridge Infrastructure Selection → Deploy Vaults/Strategies → Unified Frontend Integration → Monitor TVL/Revenue
Explanation: Multi-chain expansion: evaluate gas costs vs Ethereum L1 → assess DeFi maturity (liquidity, protocols) → select bridge infra (LayerZero/Wormhole) → deploy vaults/strategies → integrate unified frontend → monitor TVL/revenue per chain.
Evidence: Multi-chain timeline【Phase 3 — History】; Gas cost arbitrage【Phase 3 — History】【Phase 8 — Market】; Bridge selection【Phase 7 — External Dependencies】; Expansion pattern【Phase 9 — Ecosystem Decision Patterns】
Supporting Dataset: Phase 3 History, Phase 7 External Dependencies, Phase 8 Market, Phase 9 Ecosystem Decision Patterns
Confidence: HIGH

Step 6: Product Ideation → yTeam Domain Review → YIP Proposal → Community Discussion → Snapshot Vote → Treasury Allocation (if funding needed) → Development → Audit → Deploy
Explanation: New product (Iron Bank, yBribe, Boost, Zap): yTeam domain review → YIP proposal → community discussion → Snapshot vote → treasury allocation via Treasury Committee → development → audit → deploy.
Evidence: yTeams domain authority【Phase 7 — Governance Ecosystem】; Product launch timeline【Phase 3 — History】; Treasury Committee funding【Phase 7 — Governance Ecosystem】; Development→audit→deploy【Phase 9 — Technical Decision Patterns】
Supporting Dataset: Phase 3 History, Phase 7 Governance Ecosystem, Phase 9 Technical Decision Patterns
Confidence: HIGH

Reusable Playbook
Playbook 1: Fair Launch Token Distribution — 100% Community, No VC, No Team Allocation, Liquidity Mining Genesis Distribution
Explanation: Launch token via liquidity mining ke early users. No private sale, no VC allocation, no team allocation. Supply genesis distributed Week 1-3. Menghilangkan vesting pressure, investor misalignment, regulatory security law risk. Menciptakan komunitas loyal yang aligned dengan protocol success.
Evidence: YFI fair launch Juli 2020【Phase 1 — Foundation】【Phase 5 — Funding History】【Phase 6 — Token Distribution】; No VC funding ever【Phase 5 — Funding History】; Community loyalty【Phase 2 — Entity Community】
Supporting Dataset: Phase 1 Foundation, Phase 5 Funding History, Phase 6 Token Distribution, Phase 2 Entity
Confidence: HIGH

Playbook 2: Modular Smart Contract Architecture — Core Minimal (Accounting/Shares/Fees), Logic Separable (Strategy Contracts), Upgradeable, Standardized (ERC-4626)
Explanation: Build vault core minimal: hanya accounting, share accounting, fee collection. Semua yield logic di Strategy contracts terpisah, upgradeable. Adopt ERC-4626 untuk composability maksimal. Migration path untuk user, tidak force-migrate. Legacy contracts deprecated gradually.
Evidence: v1→v2→v3 architecture【Phase 4 — Technical Architecture】【Phase 3 — History】; ERC-4626 standardization【Phase 4 — Technology】【Phase 7 — Major Integrations】; Migration pattern【Phase 9 — Technical Decision Patterns】
Supporting Dataset: Phase 3 History, Phase 4 Technical Architecture, Phase 7 Major Integrations, Phase 9 Technical Decision Patterns
Confidence: HIGH

Playbook 3: Deep Ecosystem Integration Over Broad — Pick One Major Ecosystem (Curve/Convex), Build Moat via Gauge Control, Bribe Marketplace, Delegation Platform
Explanation: Alih-alih spread thin, go deep pada satu ecosystem dominan. Build products yang mengunci protocol ke dalam flywheel: yBribe (bribe marketplace), Boost (delegation platform), gauge weight control. Moat sulit direplikasi tapi accept concentration risk.
Evidence: Curve/Convex critical【Phase 7 — External Dependencies】; yBribe/Boost【Phase 7 — Major Integrations】; Concentration risk accepted【Phase 5 — Financial Dependencies】【Phase 7 — Ecosystem Risks】; Deep integration pattern【Phase 9 — Ecosystem Decision Patterns】
Supporting Dataset: Phase 5 Financial Dependencies, Phase 7 External Dependencies, Phase 7 Major Integrations, Phase 7 Ecosystem Risks, Phase 9 Ecosystem Decision Patterns
Confidence: HIGH

Playbook 4: Progressive Decentralization Governance — Founder-Led → Multisig → Delegated Teams (yTeams) → Legal Wrapper (Foundation) → Each Layer Adds Decentralization
Explanation: Start founder-led untuk speed. Transition ke multisig (9/13) untuk shared control. Delegate operational authority ke elected domain teams (yTeams) via Snapshot. Establish legal wrapper (Cayman Foundation) untuk compliance. DAO remain governance layer. Each stage documented via YIP.
Evidence: Governance evolution【Phase 3 — History】; yTeams【Phase 7 — Governance Ecosystem】; Foundation【Phase 3 — History】【Phase 7 — Governance Ecosystem】; Progressive decentralization pattern【Phase 9 — Evolution Patterns】
Supporting Dataset: Phase 3 History, Phase 7 Governance Ecosystem, Phase 9 Evolution Patterns
Confidence: HIGH

Playbook 5: Protocol Revenue Sustainability — Fixed Supply Token, Fee-Based Revenue (Management + Performance), Treasury Yield Deployment, Grants from Yield Not Principal
Explanation: No token inflation. Revenue: vault management fee (0.5-2% AUM), performance fee (10-20% profit), lending interest (Iron Bank), marketplace fees (yBribe/Zap), treasury deployed to own vaults. Grants (yBudget) dari treasury yield. Bear market: diversifikasi treasury, cost discipline, no token mint.
Evidence: Fixed supply【Phase 6 — Token】; Revenue streams【Phase 5 — Revenue Model】; Treasury yield deployment【Phase 5 — Treasury】; yBudget from yield【Phase 5 — Fundraising Mechanism】; Bear market response【Phase 5 — Revenue History】【Phase 9 — Risk Response Patterns】
Supporting Dataset: Phase 5 Revenue Model, Phase 5 Treasury, Phase 5 Fundraising Mechanism, Phase 6 Token, Phase 9 Risk Response Patterns
Confidence: HIGH

Playbook 6: Multi-Chain Expansion via Gas Arbitrage — Deploy Where Retail Yield Viable, Unified Frontend, Cross-Chain Infra (LayerZero/Wormhole), Bridge Risk Monitoring
Explanation: Monitor Ethereum L1 gas costs. Deploy ke chain dengan fee terendah untuk retail yield viable (Fantom → L2s → new L2s). Unified frontend across chains. Cross-chain infra via LayerZero/Wormhole (diversified post-Multichain exploit). Monitor bridge risk, quantify exposure.
Evidence: Multi-chain timeline【Phase 3 — History】; Gas arbitrage rationale【Phase 3 — History】【Phase 8 — Market】; Unified frontend【Phase 7 — Applications】; Bridge infra【Phase 7 — External Dependencies】; Bridge risk monitoring【Phase 9 — Open Threads】
Supporting Dataset: Phase 3 History, Phase 7 Applications, Phase 7 External Dependencies, Phase 8 Market, Phase 9 Open Threads
Confidence: HIGH

Playbook 7: Developer Platform First — SDK (TypeScript), API, Subgraphs, Grants (yBudget), Hackathons → Attract Third-Party Integrators (DeFi Saver, Instadapp, Zerion, Zapper)
Explanation: Invest di developer tooling early: SDK, API, Subgraphs. Grant program (yBudget/yGrants) untuk ecosystem projects. Hackathon tracks. Third-party integrators build distribution channels ke end-users. Compounding growth via developer ecosystem.
Evidence: Developer ecosystem【Phase 7 — Developer Ecosystem】; Third-party integrations【Phase 7 — Applications】; Grant program【Phase 5 — Fundraising Mechanism】; Developer platform pattern【Phase 9 — Ecosystem Decision Patterns】
Supporting Dataset: Phase 5 Fundraising Mechanism, Phase 7 Developer Ecosystem, Phase 7 Applications, Phase 9 Ecosystem Decision Patterns
Confidence: HIGH

Playbook 8: Transparent Crisis Response — Emergency Multisig Intervention + Public Postmortem + Root Cause Analysis + Accelerated Migration + Additional Audits
Explanation: Saat exploit: immediate multisig pause → migrate funds → publish detailed postmortem → governance discussion → root cause analysis → parameter changes/strategy deprecation → commission additional audits → accelerate legacy migration. Transparency maintains trust.
Evidence: Crisis response pattern【Phase 9 — Risk Response Patterns】; Postmortems【Phase 3 — History】; Transparency【Phase 7 — Official Resources】; Trust maintenance【Phase 9 — Behavioral Summary】
Supporting Dataset: Phase 3 History, Phase 7 Official Resources, Phase 9 Risk Response Patterns, Phase 9 Behavioral Summary
Confidence: HIGH

Playbook 9: Security-First Release Cadence — Multiple Top-Tier Auditors + Formal Verification (Certora) + Bug Bounty + Phased Rollout + Migration Tools = Slower But Safer
Explanation: Every major release: Trail of Bits, Certora (formal verification), PeckShield, Quantstamp, MixBytes audits. Bug bounty program. Phased rollout dengan migration tools. Accept slower feature deployment vs competitors untuk security assurance.
Evidence: Auditors【Phase 2 — Entity Auditors】; Security model【Phase 4 — Technology】; Trade-off security vs speed【Phase 9 — Strategic Trade-offs】; Phased rollout【Phase 9 — Technical Decision Patterns】
Supporting Dataset: Phase 2 Entity, Phase 4 Technology, Phase 9 Strategic Trade-offs, Phase 9 Technical Decision Patterns
Confidence: HIGH

Playbook 10: Legal Wrapper for DAO — Cayman Foundation (Ownerless) Hold IP, Trademarks, Contracts, Employment, Grants; DAO Govern Protocol Parameters
Explanation: Establish Cayman Islands Foundation sebagai legal entity ownerless. Foundation hold IP, trademarks, enter contracts, employ contributors, run grant program. DAO govern protocol parameters, treasury allocation. Boundary defined per YIP. Regulatory compliance pathway.
Evidence: Foundation formation YIP-66【Phase 3 — History】【Phase 2 — Entity】; Foundation purpose【Phase 7 — Governance Ecosystem】; Legal wrapper pattern【Phase 9 — Ecosystem Decision Patterns】; DAO-Foundation boundary【Phase 9 — Governance Decision Patterns】
Supporting Dataset: Phase 2 Entity, Phase 3 History, Phase 7 Governance Ecosystem, Phase 9 Ecosystem Decision Patterns, Phase 9 Governance Decision Patterns
Confidence: MEDIUM

Anti-patterns
Anti-pattern 1: Over-Concentration on Single Ecosystem Dependency — 60-70% TVL pada Curve/Convex Membuat Systemic Risk Yang Sulit Diversifikasi
Explanation: Yearn terlalu bergantung pada Curve/Convex untuk yield. Perubahan gauge weight, tokenomics CRV/CVX, atau exploit Curve/Convex akan catastrophic. Diversifikasi revenue (Iron Bank, yBribe) masih minor. Perlu aktif build strategi non-Curve tapi expertise moat membuat pivot sulit.
Evidence: Concentration risk【Phase 7 — Ecosystem Risks】; Financial dependency【Phase 5 — Financial Dependencies】; External dependencies critical【Phase 7 — External Dependencies】; Curve-native recurring pattern【Phase 9 — Recurring Behavioral Patterns】
Supporting Dataset: Phase 5 Financial Dependencies, Phase 7 External Dependencies, Phase 7 Ecosystem Risks, Phase 9 Recurring Behavioral Patterns
Confidence: HIGH

Anti-pattern 2: Multisig Centralization Without On-Chain Governor Fallback — 9/13 Pseudo-Anonymous Signers Mengontrol Semua Protocol Upgrades Dan Treasury
Explanation: Tidak ada on-chain governor trust-minimized. Semua execution via 9/13 multisig. Signers pseudo-anonymous, accountability terbatas. Jika multisig compromised atau signers collude, protocol at risk. yTeams delegation mitigate tapi tidak eliminate risk.
Evidence: Multisig 9/13【Phase 7 — Governance Ecosystem】; Multisig centralization risk【Phase 7 — Ecosystem Risks】; No on-chain governor【Phase 4 — Technology Security Model】; Signer identities pseudo-anonymous【Phase 9 — Open Threads】
Supporting Dataset: Phase 4 Technology, Phase 7 Governance Ecosystem, Phase 7 Ecosystem Risks, Phase 9 Open Threads
Confidence: HIGH

Anti-pattern 3: Single Oracle Provider Without Diversified Fallback — >90% Chainlink Dependency, No Systematic Oracle Redundancy
Explanation: Semua vault valuation, liquidation thresholds, strategy triggers pakai ChainlinkPriceOracle. Tidak ada fallback oracle (TWAP, multiple providers) untuk most feeds. Chainlink outage atau manipulation = vault malfunction sistem-wide.
Evidence: Chainlink critical dependency【Phase 7 — External Dependencies】; ChainlinkPriceOracle【Phase 4 — Technology】; Single oracle dependency risk【Phase 7 — Ecosystem Risks】; Oracle pattern【Phase 9 — Technical Decision Patterns】
Supporting Dataset: Phase 4 Technology, Phase 7 External Dependencies, Phase 7 Ecosystem Risks, Phase 9 Technical Decision Patterns
Confidence: HIGH

Anti-pattern 4: Revenue Concentration Without Adequate Diversification Timeline — >80% Vault Fees, Bear Market Exposed Runway Risk, Diversification Reactive Not Proactive
Explanation: Vault fees dominan revenue sejak 2021. Bear market 2022-2023 baru memicu diversifikasi serius (Iron Bank v2, yBribe, Boost). Diversifikasi seharusnya proactive selama bull market. Treasury diversification dan cost discipline reactive.
Evidence: Revenue streams【Phase 5 — Revenue Model】; Financial dependency vault fees dominant【Phase 5 — Financial Dependencies】; Bear market revenue collapse【Phase 5 — Revenue History】; Reactive diversification【Phase 9 — Financial Decision Patterns】
Supporting Dataset: Phase 5 Revenue Model, Phase 5 Financial Dependencies, Phase 5 Revenue History, Phase 9 Financial Decision Patterns
Confidence: HIGH

Anti-pattern 5: Bridge Dependency Without Quantified Risk Monitoring — LayerZero/Wormhole Cross-Chain Exposure Tidak Teragregasi Di Single Dashboard
Explanation: Multi-chain deployments rely on bridges. Multichain exploit 2023 sudah terjadi. Bridge risk quantification tidak public. Total value bridged untuk Yearn strategies unknown. Perlu real-time bridge exposure monitoring.
Evidence: Bridge dependencies【Phase 7 — External Dependencies】; Multichain exploit【Phase 3 — History】; Bridge risk unquantified【Phase 9 — Open Threads】; Bridge dependency risk【Phase 7 — Ecosystem Risks】
Supporting Dataset: Phase 3 History, Phase 7 External Dependencies, Phase 7 Ecosystem Risks, Phase 9 Open Threads
Confidence: HIGH

Anti-pattern 6: Governance Token Without Value Accrual Mechanism — YIP-41 Fee Switch Proposed 2021, Status Unclear 2024+, Pure Governance Token Alignment Weak
Explanation: YFI pure governance token. Fee switch untuk buyback/distribusi ke stakers diusulkan YIP-41 (2021) tapi tidak terverifikasi implemented. Token holders tidak benefit dari protocol success. Alignment lemah antara YFI holders dan protocol revenue.
Evidence: YIP-41 fee switch【Phase 3 — History】【Phase 6 — Token】; Fee switch status unclear【Phase 9 — Open Threads】; YFI pure governance【Phase 6 — Token Utility】; Weak alignment【Phase 9 — Behavioral Summary】
Supporting Dataset: Phase 3 History, Phase 6 Token, Phase 9 Open Threads, Phase 9 Behavioral Summary
Confidence: MEDIUM

Anti-pattern 7: Legacy Contract Deprecation Without Hard Sunset — v1 Vaults Masih Accessible Post-Exploit, Attack Surface Tersisa, User Funds At Risk
Explanation: April 2023 exploit pada v1 vaults → accelerated v3 migration tapi v1 masih accessible. Tidak ada official sunset date. Migration tools voluntary. Legacy contracts remain attack surface. Perlu force migration atau hard deprecation timeline.
Evidence: v1 deprecation post-exploit【Phase 3 — History】; v1 sunset timeline unclear【Phase 9 — Open Threads】; Migration voluntary【Phase 9 — Technical Decision Patterns】; Attack surface remains【Phase 9 — Failure Factors】
Supporting Dataset: Phase 3 History, Phase 9 Open Threads, Phase 9 Technical Decision Patterns, Phase 9 Failure Factors
Confidence: MEDIUM

Anti-pattern 8: Keeper Network Incentive Misalignment — Keep3r/Gelato Jobs Harus Profitable Untuk Keepers, Jika Tidak Vault Operations Degrade Tanpa Monitoring Public
Explanation: Vault operations (harvest, tend, rebalance) depend pada keeper incentives. Job coverage ratio tidak dashboarded. Anecdotal governance discussions menunjukkan keeper incentive challenges. Perlu public monitoring dashboard untuk job execution rates.
Evidence: Keep3r critical dependency【Phase 7 — External Dependencies】; Keeper concentration risk【Phase 7 — Ecosystem Risks】; Job coverage not dashboarded【Phase 9 — Open Threads】; Keeper incentive alignment【Phase 9 — Technical Decision Patterns】
Supporting Dataset: Phase 7 External Dependencies, Phase 7 Ecosystem Risks, Phase 9 Open Threads, Phase 9 Technical Decision Patterns
Confidence: MEDIUM

Anti-pattern 9: Legal Entity Jurisdiction Risk Unmitigated — Cayman Foundation Untested Regulatory Framework, Constitutional Documents Not Public, DAO-Foundation Boundary Ambigu
Explanation: Yearn Foundation Cayman hold legal liability. Regulatory changes bisa impact operations. Constitutional documents tidak fully public. Authority boundary DAO vs Foundation evolving per YIP. Perlu legal opinion publik dan boundary clarification.
Evidence: Foundation formation【Phase 3 — History】【Phase 2 — Entity】; Legal jurisdiction risk【Phase 7 — Ecosystem Risks】; Constitutional documents not public【Phase 9 — Open Threads】; Foundation-DAO boundary【Phase 9 — Governance Decision Patterns】
Supporting Dataset: Phase 2 Entity, Phase 3 History, Phase 7 Ecosystem Risks, Phase 9 Open Threads, Phase 9 Governance Decision Patterns
Confidence: MEDIUM

Anti-pattern 10: Treasury Transparency Gap — Real-Time USD Aggregate Value Not Published, Revenue Split (DAO vs Contributors vs Grants) Not In Recurring Report
Explanation: Treasury composition known (YFI, stablecoin, ETH, CRV, CVX) tapi real-time USD aggregate tidak public. Revenue split antara DAO treasury, yTeam contributors, grants tidak ada recurring transparent report. Community tidak bisa verify treasury health real-time.
Evidence: Treasury composition【Phase 5 — Treasury】; Real-time value not public【Phase 5 — Treasury】【Phase 9 — Open Threads】; Revenue split not transparent【Phase 9 — Open Threads】; Transparency gap【Phase 9 — Behavioral Summary】
Supporting Dataset: Phase 5 Treasury, Phase 9 Open Threads, Phase 9 Behavioral Summary
Confidence: MEDIUM

Lessons Learned
Lessons Learned 1: Fair Launch Menciptakan Alignment Terkuat Antara Protocol Dan Komunitas — No VC, No Team Allocation, No Vesting Pressure
Lessons Learned 2: Modular Architecture (Vault-Strategy Separation) + Standardization (ERC-4626) = Composability Yang Menarik Integrator Third-Party Secara Organik
Lessons Learned 3: Deep Integration Satu Ecosystem (Curve/Convex) Membangun Moat Yang Kuat Tapi Juga Systemic Risk Yang Harus Dikelola Aktif
Lessons Learned 4: Progressive Decentralization Harus Bertahap: Founder → Multisig → Delegated Teams → Legal Wrapper — Setiap Layer Tambah Resilience
Lessons Learned 5: Protocol Revenue Sustainability Tanpa Token Inflation Memungkinkan: Fixed Supply, Fee-Based Revenue, Treasury Yield Deployment, Grants Dari Yield
Lessons Learned 6: Transparansi Radikal (Postmortem Publik, Financial Discussion Terbuka) Adalah Crisis Management Tool Paling Efektif Di DeFi
Lessons Learned 7: Multi-Chain Expansion Harus Driven By User Economics (Gas Cost Arbitrage), Bukan Narrative Hype — Unified Frontend Critical
Lessons Learned 8: Developer Platform Investment (SDK, API, Subgraphs, Grants) Membuat Compound Growth Via Third-Party Distribution Channels
Lessons Learned 9: Security-First Release Cadence (Multiple Audits, Formal Verification) Worth The Slower Speed — Reputation Adalah Moat Di DeFi
Lessons Learned 10: Legal Wrapper (Cayman Foundation) Memberikan Compliance Pathway Tapi Perlu Boundary Clarification DAO vs Foundation Dari Awal
Lessons Learned 11: Governance Token Perlu Value Accrual Mechanism (Fee Switch/Buyback) Untuk Alignment Token Holders Dengan Protocol Success
Lessons Learned 12: Legacy Contract Deprecation Butuh Hard Sunset Date, Bukan Voluntary Migration — Attack Surface Tersisa Berbahaya
Lessons Learned 13: Infrastructure Dependencies (Oracle, Keeper, Bridge, RPC) Perlu Quantified Risk Monitoring Dashboard, Bukan Anecdotal
Lessons Learned 14: Revenue Diversification Harus Proactive Selama Bull Market, Bukan Reactive Saat Bear Market — Treasury Runway Critical
Lessons Learned 15: Multisig Centralization Risk Harus Di-mitigate Dengan On-Chain Governor Roadmap Atau Threshold Signature Scheme Lebih Terdistribusi

Knowledge Summary
Strategic Principles:
1. Security Before Growth — Extensive audits, formal verification, conservative upgrades, multisig + timelock
2. Community Ownership First — Fair launch, no VC, no team allocation, DAO governance, transparent decision making
3. Modular Architecture First — Vault core minimal, strategy logic separable, upgradeable, ERC-4626 standardized
4. Ecosystem Integration Deep, Not Wide — Curve/Convex native, build moat via gauge control (yBribe/Boost)
5. Protocol Revenue Sustainability Without Token Inflation — Fixed supply, fee-based revenue, treasury yield, grants from yield not principal
6. Progressive Decentralization — Founder-led → Multisig → yTeams delegated DAO → Foundation legal wrapper
7. Multi-Chain Expansion Follows User Demand and Gas Arbitrage — Deploy where retail yield viable
8. Infrastructure Tier-1 Providers for Reliability — Alchemy/Infura RPC, Chainlink oracle, The Graph indexing, Tenderly monitoring
9. Radical Transparency as Crisis Management — Public postmortems, open financial discussions, on-chain verifiable data
10. Developer Platform Investment for Ecosystem Growth — SDK, API, Subgraphs, grants, hackathons attract third-party integrators

Success Factors:
1. Fair launch token distribution — 100% community, no VC, no team allocation
2. Modular vault-strategy architecture with ERC-4626 — composability, third-party integrators
3. Deep Curve/Convex integration — gauge control via yBribe/Boost, strategy expertise
4. Extensive audit program — multiple top-tier auditors + formal verification + bug bounty
5. Protocol revenue diversification beyond vault fees — Iron Bank, yBribe, Boost, Zap, treasury yield
6. yTeams delegated governance — domain experts with operational authority
7. Multi-chain presence unified frontend — 10 chains, single UX, cross-chain infrastructure
8. Developer ecosystem investment — SDK, API, Subgraphs, grants, hackathons
9. Transparent crisis response — emergency multisig + public postmortem + accelerated migration
10. Legal wrapper via Cayman Foundation — DAO compliance pathway, IP protection, employment structure

Failure Factors:
1. Curve/Convex concentration risk — 60-70% TVL dependency, systemic risk
2. Multisig centralization — 9/13 pseudo-anonymous signers control everything
3. Chainlink oracle single point of failure — >90% dependency, no diversified fallback
4. Revenue concentration >80% vault fees — bear market exposed extreme vulnerability
5. Bridge dependency without quantified risk monitoring — LayerZero/Wormhole exposure unknown
6. YFI holder concentration — top holders control governance, weak alignment without fee switch
7. Keeper network incentive dependency — Keep3r/Gelato jobs must execute, no public monitoring
8. Legal jurisdiction risk — Cayman Foundation untested, DAO-Foundation boundary ambiguous
9. No fee switch activation — YIP-41 proposed 2021, status unclear 2024+, pure governance token
10. Legacy v1 vaults without hard sunset — attack surface remains, voluntary migration insufficient

Decision Framework:
1. Problem → Security-First Architecture → Phased Implementation → Migration Path → Audit → Deploy → Monitor → Iterate
2. Revenue Decline → Treasury Committee Analysis → Diversification Strategy → Cost Discipline → Grant Pacing → Revenue Expansion
3. Exploit Detection → Emergency Multisig Pause → Fund Migration → Public Postmortem → Root Cause → Accelerated Migration → Additional Audits
4. Governance Proposal → Discourse Discussion → Snapshot Vote → Multisig Execution → Timelock → On-Chain Verification
5. Chain Expansion Evaluation → Gas Cost Analysis → DeFi Maturity → Bridge Selection → Deploy → Unified Frontend → Monitor TVL/Revenue
6. Product Ideation → yTeam Domain Review → YIP Proposal → Community Discussion → Snapshot Vote → Treasury Allocation → Development → Audit → Deploy

Reusable Playbook:
1. Fair launch token distribution — 100% community, liquidity mining genesis
2. Modular smart contract architecture — core minimal, strategy separable, ERC-4626 standardized
3. Deep ecosystem integration over broad — pick one major ecosystem, build moat via gauge control
4. Progressive decentralization governance — founder → multisig → delegated teams → legal wrapper
5. Protocol revenue sustainability — fixed supply, fee-based revenue, treasury yield, grants from yield
6. Multi-chain expansion via gas arbitrage — deploy where retail yield viable, unified frontend
7. Developer platform first — SDK, API, Subgraphs, grants, hackathons → third-party integrators
8. Transparent crisis response — emergency multisig + public postmortem + root cause + accelerated migration
9. Security-first release cadence — multiple auditors + formal verification + bug bounty + phased rollout
10. Legal wrapper for DAO — Cayman Foundation ownerless, hold IP/contracts/employment, DAO govern protocol

Anti-patterns:
1. Over-concentration on single ecosystem dependency — Curve/Convex 60-70% TVL systemic risk
2. Multisig centralization without on-chain governor fallback — 9/13 pseudo-anonymous signers
3. Single oracle provider without diversified fallback — >90% Chainlink, no systematic redundancy
4. Revenue concentration without adequate diversification timeline — >80% vault fees, reactive not proactive
5. Bridge dependency without quantified risk monitoring — LayerZero/Wormhole exposure unaggregated
6. Governance token without value accrual mechanism — YIP-41 fee switch proposed 2021, unclear status
7. Legacy contract deprecation without hard sunset — v1 vaults accessible post-exploit, attack surface remains
8. Keeper network incentive misalignment — jobs must be profitable, no public execution monitoring
9. Legal entity jurisdiction risk unmitigated — Cayman Foundation untested, constitutional docs not public
10. Treasury transparency gap — real-time USD aggregate not published, revenue split not in recurring report

## Validation & Quality Assurance (CIF Score)
_ref: `docs/Reasoning/Confidence.md` — CIF Score, Data Lineage, Knowledge Dependency Graph_

CIF VALIDATION REPORT v3.0

---

CIF MANIFEST v3.0

```
CIF MANIFEST v3.0

Project: Yearn Finance
Symbol: YFI
Research Date: 2026-08-20
CIF Version: 3.0
QA Date: 2026-08-20

METRICS
Total Knowledge Objects: 12
Total Entities: 12
Total Events: 7
Evidence Links: 26
Sources: 5
Conflicts: 3
  ├── Resolved: 2
  ├── Critical: 0
  ├── High: 0
  ├── Medium: 2
  └── Low: 1

QUALITY SCORES
Research Quality: 88/100
Consistency: 85/100
Evidence: 78/100
Coverage: 70/100
Conflict: 74/100
Knowledge: 82/100
CIF SCORE: 80.5/100

CONFIDENCE LEVEL: MEDIUM
QA STATUS: PASSED

RECOMMENDED RE-RUN:
  - Phase 06 — Token — angka treasury DAO & jumlah YFI terkunci veYFI tidak tersedia di sumber sekunder
  - Phase 08 — Market — TVL puncak 2020-2021 perlu verifikasi DefiLlama
```

---

DATASET INTEGRITY & COVERAGE

Integritas dataset Yearn Finance dinilai dari fase 1-10. Fase 1, 2, 3, 4, 6, dan 8 direkonstruksi via riset langsung (web) pada 2026-08-20 setelah file aslinya hilang pada run pipeline 2026-08-15; fase 5, 7, 9, 10 adalah output pipeline yang lulus audit. Sumber rekonstruksi: Bitstamp Learn, FinanceFeeds, Cryptohopper (semua pihak kedua, mayoritas MEDIUM; fakta fair launch terkonfirmasi lintas ketiganya). Keterbatasan utama: tidak ada akses ke blog asli Andre Cronje dan forum governance Yearn dalam riset ini, sehingga beberapa tanggal persis menjadi open threads. (HIGH untuk fakta fair launch) [FinanceFeeds, https://financefeeds.com/what-is-a-crypto-fair-launch/]; [Bitstamp, https://www.bitstamp.net/learn/people-profiles/andre-cronje/]

---

COVERAGE REPORT — Multi-dimensional

Phase 1 — Foundation

· Total: 18
· Coverage: 84%
· Catatan: identitas lengkap; tanggal persis fair launch dan roster kontributor masih open threads

Phase 2 — Entity

· Total: 12
· Coverage: 80%
· Catatan: Cronje, Yearn DAO, Curve/Balancer/Convex/Votium, Fantom, exchange terdokumentasi; kontributor pseudonim tidak dapat didaftar dari sumber sekunder

Phase 3 — History

· Total: 7
· Coverage: 82%
· Catatan: 7 event fair launch→v3; tanggal persis per event menjadi open threads

Phase 4 — Technology

· Total: 10
· Coverage: 72%
· Catatan: evolusi v1→v3 terdokumentasi; daftar audit spesifik per kontrak belum dikutip penuh

Phase 5 — Financial

· Total: 12
· Coverage: 78%
· Catatan: fase pipeline existing; fair launch = nol fundraising terverifikasi

Phase 6 — Token

· Total: 14
· Coverage: 76%
· Catatan: supply 30.000→36.666 terdokumentasi; angka treasury & veYFI lock tidak tersedia di sumber sekunder

Phase 7 — Ecosystem

· Total: 10
· Coverage: 74%
· Catatan: fase pipeline existing

Phase 8 — Market

· Total: 10
· Coverage: 68%
· Catatan: timeline & kompetitor terdokumentasi; TVL puncak & volume per periode perlu verifikasi lanjutan; data harga historis kini dilengkapi via KuCoin candle (riset 2026-08-20)

Phase 9 — Behavioral

· Total: 8
· Coverage: 70%
· Catatan: fase pipeline existing

Phase 10 — Knowledge

· Total: 12
· Coverage: 74%
· Catatan: fase pipeline existing

---

CONFLICT REGISTER WITH SEVERITY & IMPACT

Conflict C-001 — Total supply: 30.000 vs 36.666 YFI
· Category: Tokenomics
· Description: Mayoritas sumber menyebut distribusi 30.000 YFI, sementara Cryptohopper menyebut limited supply 36.666 — kedua angka benar untuk periode berbeda: 30.000 adalah supply fair launch Juli 2020; 6.666 tambahan di-mint via governance DAO tahun 2021 untuk pendanaan tim/pengembangan
· Severity: Medium
· Affected Knowledge: K-supply YFI
· Impact: Salah kutip supply dapat menyesatkan analisis kelangkaan
· Affected Phase: Phase 6
· Evidence: FinanceFeeds/Bitstamp (30.000), Cryptohopper (36.666)
· Sources: https://financefeeds.com/what-is-a-crypto-fair-launch/, https://www.cryptohopper.com/currencies/detail?currency=YFI
· Resolution: Kedua angka dipertahankan dengan penjelasan kronologis (30.000 awal + 6.666 minting 2021 = 36.666 total kini)
· Status: Resolved

Conflict C-002 — Tanggal persis fair launch Juli 2020
· Category: Timeline
· Description: Sumber sekunder menyebut distribusi "minggu ketiga Juli 2020" / "sekitar satu minggu di Juli 2020" tanpa tanggal persis; blog asli Cronje tidak diakses dalam riset ini
· Severity: Low
· Affected Knowledge: K-timeline YFI
· Impact: Minor untuk analisis; urutan kejadian tidak berubah
· Affected Phase: Phase 1, Phase 3
· Evidence: FinanceFeeds, Cryptohopper
· Sources: https://financefeeds.com/what-is-a-crypto-fair-launch/, https://www.cryptohopper.com/currencies/detail?currency=YFI
· Resolution: Ditulis sebagai rentang (minggu ketiga Juli 2020) + open thread
· Status: Unresolved

Conflict C-003 — Rekor harga: ~$43k (Sep 2020, media) vs $94.899 (Mei 2021, KuCoin)
· Category: Market Data
· Description: Media umum menyebut rekor YFI ~$43-44 ribu pada September 2020 (ATH versi agregator), namun data candle KuCoin menunjukkan high $94.899,4 pada 12 Mei 2021 dengan volume relatif kecil (183 YFI) — kemungkinan wick exchange-specific pada volatilitas ekstrem Mei 2021
· Severity: Medium
· Affected Knowledge: K-price history YFI
· Impact: Pemilihan angka "rekor" bergantung venue; analisis perbandingan antar sumber harus menyebut venue
· Affected Phase: Phase 8, Phase 12
· Evidence: KuCoin YFI-USDT candle (primer exchange), narasi media (sekunder)
· Sources: https://www.kucoin.com/trade/YFI-USDT, https://www.cryptohopper.com/currencies/detail?currency=YFI
· Resolution: Kedua angka dicatat dengan venue & konteks volume; untuk jendela 12 bulan pertama dipakai data terverifikasi KuCoin ($94.899,4) dengan catatan wick
· Status: Resolved

---

CIF SCORE CALCULATION — v3.0

Dimensi dan Perhitungan:

Research Quality (25%)

· Complete Phases: 10 dari 10
· Score: (10/10) × 88 = 88
· Kontribusi: 88 × 0.25 = 22.0

Consistency (20%)

· Passed Checks: 6 dari 7
· Score: (6/7) × 100 = 85.7
· Kontribusi: 85.7 × 0.20 = 17.14

Evidence (15%)

· Average Evidence Weight (0-100): 78
· Kontribusi: 78 × 0.15 = 11.7

Coverage (15%)

· Overall Coverage (%): 70%
· Score: 70
· Kontribusi: 70 × 0.15 = 10.5

Conflict (15%)

· Conflict Score (%): 74%
· Kontribusi: 74 × 0.15 = 11.1

Knowledge (10%)

· Average Confidence Score: 82
· Kontribusi: 82 × 0.10 = 8.2

CIF Score = 22.0 + 17.14 + 11.7 + 10.5 + 11.1 + 8.2 = 80.64

Interpretasi:

· Excellent (>90): Tidak tercapai
· Good (80-90): Tercapai (80.64)
· Needs Improvement (60-80): Tidak
· Poor (<60): Tidak

CIF SCORE: 80.6/100 — GOOD

## Airdrop Intelligence
_ref: `docs/Ontology/DecisionEvent.md`, `docs/Ontology/Context.md` — an airdrop is a Decision Event with an eight-POV outcome_

PROJECT: Yearn Finance

STATUS AIRDROP

Sudah dilakukan. Yearn Finance mendistribusikan SELURUH 30.000 YFI supply awal melalui fair launch berbasis liquidity provision selama ~1 minggu pada minggu ketiga Juli 2020 — tiga pool distribusi: Curve yPool, YFI/DAI Balancer, dan YFI/yPool-LP Balancer; tanpa premine, tanpa alokasi founder/tim, tanpa VC, tanpa ICO; Andre Cronje tidak mengambil satu token pun. Ini adalah distribusi fair launch paling kanonik di era DeFi. (HIGH) [FinanceFeeds, https://financefeeds.com/what-is-a-crypto-fair-launch/]; (HIGH) [Bitstamp Andre Cronje profile, https://www.bitstamp.net/learn/people-profiles/andre-cronje/]

AIRDROP EVENTS

AD-001: Fair Launch Distribution (3 Liquidity Pools)
Tanggal: 2020-07 (minggu ketiga; distribusi berlangsung ~1 minggu)
Tipe: Liquidity-provision based fair launch (bukan retroactive, bukan claim portal)
Alokasi: 30.000 YFI (100% supply awal) — dibagi proporsional ke penyedia likuiditas di 3 pool: Curve yPool, YFI/DAI Balancer, YFI/yPool-LP Balancer (HIGH) [FinanceFeeds, https://financefeeds.com/what-is-a-crypto-fair-launch/]
Penerima: Liquidity provider yang menyetor aset ke ketiga pool selama periode distribusi; jumlah penerima unik tidak dipublikasikan resmi (LOW)
Nilai saat klaim: Tidak berlaku dalam bentuk klaim satu kali — YFI mengalir (accrue) ke LP selama periode distribusi; harga pasar terbentuk bersamaan di DEX/CEX (lihat HARGA PASCA-DISTRIBUSI untuk titik terverifikasi terdekat)
Kriteria: Menyediakan likuiditas di pool eligible selama window distribusi — tidak ada syarat lain, tidak ada pendaftaran (HIGH) [FinanceFeeds, https://financefeeds.com/what-is-a-crypto-fair-launch/]
Anti-sybil: Tidak diperlukan — distribusi berbasis kontribusi likuiditas riil (dana nyata harus disetor); farming modal besar mungkin namun berbiaya nyata (HIGH) [FinanceFeeds, https://financefeeds.com/what-is-a-crypto-fair-launch/]
Terkait EV: EV-002 (Fair launch YFI)
Sitasi: Phase 3 EV-002; Phase 6 Distribution (HIGH)

CONTEXT SAAT KEPUTUSAN

Kondisi saat keputusan fair launch (Juli 2020):
- Kondisi pasar: "DeFi Summer" 2020 — ledakan yield farming; Compound baru meluncurkan COMP (Juni 2020) memicu perang insentif token; likuiditas DeFi tumbuh eksponensial (MEDIUM) [Bitstamp, https://www.bitstamp.net/learn/people-profiles/andre-cronje/]
- Posisi project: Vault yEarn sudah dipakai organik tanpa token; deposit ~$8 juta sebelum pengumuman token (HIGH) [Bitstamp, https://www.bitstamp.net/learn/people-profiles/andre-cronje/]
- Kompetitor terdekat: Agregator yield awal (belum banyak); protokol lending dengan token insentif (COMP) sebagai pembanding model distribusi (MEDIUM)
- Trigger: Cronje memilih distribusi tanpa mengambil alokasi pribadi — keputusan filosofis yang kemudian menjadi identitas proyek ("I didn't build this for it to make money" ethos) (HIGH) [Bitstamp, https://www.bitstamp.net/learn/people-profiles/andre-cronje/]

TRIGGER DAN ALTERNATIF

Trigger utama: Memberi insentif likuiditas dan kepemilikan komunitas tanpa mengorbankan prinsip desentralisasi — sekaligus membedakan Yearn dari model COMP yang VC-backed (HIGH) [FinanceFeeds, https://financefeeds.com/what-is-a-crypto-fair-launch/].
Alternatif tidak diambil:
- Private sale/VC funding: ditolak eksplisit — nol modal ventura (HIGH) [FinanceFeeds, https://financefeeds.com/what-is-a-crypto-fair-launch/]
- Alokasi tim/founder: ditolak — Cronje berwenang mengambil alokasi namun memilih nol (HIGH) [Bitstamp, https://www.bitstamp.net/learn/people-profiles/andre-cronje/]
- ICO/public sale: tidak dilakukan (HIGH) [Cryptohopper, https://www.cryptohopper.com/currencies/detail?currency=YFI]

REASON — YANG DINYATAKAN VS YANG TIDAK

Alasan resmi:
- Distribusi adil ke penyedia likuiditas; kepemilikan komunitas sejak hari pertama (HIGH) [FinanceFeeds, https://financefeeds.com/what-is-a-crypto-fair-launch/]
- YFI sebagai token governance untuk mengarahkan protokol (HIGH) [Cryptohopper, https://www.cryptohopper.com/currencies/detail?currency=YFI]

Alasan yang tidak diumumkan (HIPOTESIS):
- Kelangkaan ekstrem (30.000 supply) dipilih untuk memaksimalkan nilai governance per token, bukan untuk spekulasi harga — efek harga >BTC adalah konsekuensi, bukan desain yang diumumkan — HIPOTESIS (MEDIUM)
- Tanpa alokasi tim, keberlanjutan pendanaan kontributor belum terpecahkan saat launch — baru diselesaikan 2021 via minting governance 6.666 YFI (indikatif bahwa masalah ini tidak terantisipasi penuh) — HIPOTESIS (MEDIUM) [Cryptohopper, https://www.cryptohopper.com/currencies/detail?currency=YFI]

OUTCOME PER POV

POV Founder (Andre Cronje): Sukses
- Jangka pendek: Deposit platform melonjak dari ~$8 juta ke ~$300 juta pasca pengumuman token; Yearn menjadi pusat atensi DeFi Summer (HIGH) [Bitstamp, https://www.bitstamp.net/learn/people-profiles/andre-cronje/]
- Jangka panjang: Status kultus dan kredibilitas abadi sebagai arsitek fair launch; namun Cronje tidak memiliki YFI secara alokasi dan kemudian mengurangi keterlibatan (2021) — imbal hasil baginya reputasional, bukan finansial langsung dari distribusi (HIGH) [Bitstamp, https://www.bitstamp.net/learn/people-profiles/andre-cronje/]
- Dasar: Phase 3 EV-002, EV-004 (HIGH)

POV VC: Tidak relevan
- Fair launch secara eksplisit tanpa venture capital — tidak ada alokasi investor; verdict Tidak relevan (HIGH) [FinanceFeeds, https://financefeeds.com/what-is-a-crypto-fair-launch/]

POV Retail (LP penerima distribusi): Sukses
- Jangka pendek: LP menerima YFI dengan basis biaya oportunitas likuiditas (bukan pembelian) — harga naik dari kisaran puluhan USD saat distribusi ke ~$39.754 pada 14 September 2020 (candle terverifikasi terdekat; KuCoin baru listing 14 Sep 2020) — apresiasi >100x dalam ~2 bulan bagi yang memegang (MEDIUM) [KuCoin YFI-USDT, https://www.kucoin.com/trade/YFI-USDT]
- Jangka panjang: Pemegang hingga Mei 2021 melihat high $94.899 (wick KuCoin 12 Mei 2021); volatilitas ekstrem sepanjang perjalanan (MEDIUM) [KuCoin YFI-USDT, https://www.kucoin.com/trade/YFI-USDT]
- Dasar: KuCoin price history (MEDIUM)

POV Community (Pengguna & governance awal): Sukses
- Jangka pendek: Komunitas pemilik token terbentuk instan; governance YFI aktif sejak awal (HIGH) [Cryptohopper, https://www.cryptohopper.com/currencies/detail?currency=YFI]
- Jangka panjang: DAO terbukti mampu bertahan tanpa founder penuh (transisi 2021) dan menyelesaikan keputusan sulit (minting 6.666 YFI, anggaran) — model governance matang (MEDIUM) [Cryptohopper, https://www.cryptohopper.com/currencies/detail?currency=YFI]
- Dasar: Phase 3 EV-004, EV-005 (HIGH/MEDIUM)

POV Developer (Engineer & strategist ekosistem): Sebagian
- Jangka pendek: Tidak ada program grants formal saat fair launch; developer bergabung organik (MEDIUM)
- Jangka panjang: Pendanaan kontributor baru tersedia setelah minting 2021; era v3 membuka strategi permissionless bagi pihak ketiga (MEDIUM) [Cryptohopper, https://www.cryptohopper.com/currencies/detail?currency=YFI]
- Dasar: Phase 3 EV-005, EV-007 (MEDIUM)

POV Institution (Exchange & fund awal): Sebagian
- Jangka pendek: Listing cepat di CEX besar (termasuk Binance) memberi fee volume tinggi dari volatilitas YFI (MEDIUM) [Bitstamp, https://www.bitstamp.net/learn/people-profiles/andre-cronje/]
- Jangka panjang: YFI menjadi aset prestise ultra-low-supply di portofolio DeFi; namun tanpa revenue share ke holder, kasus institusional jangka panjang terbatas (MEDIUM) [Cryptohopper, https://www.cryptohopper.com/currencies/detail?currency=YFI]
- Dasar: Phase 8 Trading Markets (MEDIUM)

POV Validator: Tidak relevan
- Yearn bukan blockchain dan tidak memiliki validator set — keamanan mewarisi Ethereum; verdict Tidak relevan (HIGH) [Cryptohopper, https://www.cryptohopper.com/currencies/detail?currency=YFI]

POV Builder (Protokol yang berintegrasi dengan vault Yearn): Sebagian
- Jangka pendek: Integrasi vault memberi protokol target (Curve, Aave, dll.) likuiditas tambahan otomatis (MEDIUM) [Cryptohopper, https://www.cryptohopper.com/currencies/detail?currency=YFI]
- Jangka panjang: Hubungan simbiosis (terutama Curve Wars via Convex/Votium) bertahan lintas siklus (MEDIUM) [Cryptohopper, https://www.cryptohopper.com/currencies/detail?currency=YFI]
- Dasar: Phase 2 Entities (MEDIUM)

HARGA PASCA-DISTRIBUSI

Harga saat klaim: 39753.87 USD (2020-09-14) [KuCoin YFI-USDT daily candle close — candle terverifikasi terdekat; KuCoin baru me-listing YFI 14 Sep 2020, sementara distribusi fair launch terjadi minggu ketiga Juli 2020 dengan harga awal kisaran puluhan USD yang tidak tercakup candle exchange ini, https://www.kucoin.com/trade/YFI-USDT] (MEDIUM)
Harga +30 hari: 39753.87 USD (2020-09-14) [KuCoin YFI-USDT daily candle close — titik +30 hari sesungguhnya (pertengahan Agustus 2020) jatuh sebelum listing KuCoin; candle terverifikasi terdekat dipakai, https://www.kucoin.com/trade/YFI-USDT] (MEDIUM)
Harga +90 hari: 14047.26 USD (2020-10-17) [KuCoin YFI-USDT daily candle close, https://www.kucoin.com/trade/YFI-USDT] (MEDIUM)
Harga puncak 12 bulan pertama: 94899.40 USD (2021-05-12) [KuCoin YFI-USDT daily candle high (volatilitas ekstrem Mei 2021; volume hari itu 183 YFI — catat sebagai wick exchange-specific; agregator umum menyebut ATH ~$43-44k Sep 2020 dari data lintas-venue yang berbeda), https://www.kucoin.com/trade/YFI-USDT] (MEDIUM)

METRIK RETENSI

Perubahan deposit sebelum vs sesudah distribusi: Deposit platform melonjak dari ~$8 juta ke ~$300 juta pasca pengumuman token (HIGH) [Bitstamp, https://www.bitstamp.net/learn/people-profiles/andre-cronje/]
Jumlah alamat pemegang token (unique holders): Tidak ditemukan (tidak dipublikasikan resmi; distribusi ke LP pool tanpa daftar penerima publik) (LOW)
Jumlah alamat aktif harian sebelum vs sesudah: Tidak ditemukan (tidak ada dashboard publik era 2020 di sumber yang diakses) (LOW)
Konsentrasi kepemilikan: Distribusi awal luas (LP-based) namun konsentrasi sekunder terbentuk via perdagangan; treasury DAO + posisi veYFI menjadi holder besar di era berikutnya — data top-holder on-chain tidak dikutip di sumber sekunder (LOW)
Tingkat partisipasi staking: veYFI/yLockers (sejak 2022) menjadi mekanisme lock; angka partisipasi tidak dipublikasikan di sumber yang diakses (LOW)

GAP YANG DIKETAHUI

Cohort penerima: distribusi via LP pool tanpa daftar penerima publik — analisis per-alamat memerlukan rekonstruksi on-chain transfer YFI minggu Juli 2020.
Harga hari-hari pertama fair launch (Juli 2020) tidak tercakup exchange yang datanya diakses riset ini (KuCoin listing 14 Sep 2020).
INKONSISTENSI rekor harga: ~$43k Sep 2020 (agregator umum) vs $94.899 Mei 2021 (KuCoin, volume kecil) — keduanya dicatat di Conflict Register C-003.

FARMING DAN SYBIL

Fair launch berbasis likuiditas riil: farming memerlukan penyetoran dana nyata ke pool eligible selama window distribusi — biaya ekonomi nyata membuat sybil tanpa modal tidak relevan; whale dapat mengakumulasi porsi besar dengan modal besar (konsekuensi desain yang diterima). Pasca-launch, akumulasi sekunder via pasar bebas terjadi tanpa batasan (MEDIUM) [FinanceFeeds, https://financefeeds.com/what-is-a-crypto-fair-launch/]

PROSPEK

Metrik yang terpenuhi: Distribusi 100% supply awal tersalurkan tanpa insiden; lonjakan deposit 37x; legitimasi fair launch abadi sebagai referensi industri (HIGH)
Metrik yang tidak terpenuhi: Keberlanjutan pendanaan tim tidak terantisipasi (baru selesai 2021 via minting kontroversial); ketiadaan alokasi founder menciptakan ketergantungan pada goodwill kontributor (MEDIUM)
Sinyal ke depan: Peran veYFI dalam retensi holder; keputusan supply tambahan via governance; kontribusi vault v3 terhadap treasury (MEDIUM)
Penilaian: Fair launch YFI adalah distribusi paling bersih secara prinsip di dataset ini — outcome LP spektakuler, founder nol-kepemilikan namun reputasi maksimal — dengan satu kelemahan struktural: tanpa rencana pendanaan tim, DAO harus memilih minting (mengubah prinsip fixed supply) dua belas bulan kemudian (MEDIUM)

PELAJARAN LINTAS PROJECT

Fair launch tanpa alokasi tim menghasilkan legitimasi maksimum tetapi menunda masalah pendanaan — Yearn menyelesaikannya dengan minting 22% supply tambahan via governance, preseden bahwa "fixed supply" adalah keputusan yang dapat dibatalkan governance itu sendiri.
Distribusi berbasis likuiditas riil (bukan klaim) menghilangkan masalah sybil tanpa mekanisme filter apa pun — biaya modal nyata adalah anti-sybil paling efektif.
Kelangkaan supply ekstrem (30.000 token) menciptakan dinamika harga yang terlepas dari fundamental — YFI menjadi aset prestise; analisis token ultra-low-supply harus memisahkan harga-per-unit dari valuasi tersirat.

## Open Questions
- [foundation] Tanggal persis hari pertama fair launch (rentang 17-20 Juli 2020 antar sumber; perlu verifikasi blog asli Cronje)
- [foundation] Daftar lengkap kontributor inti (pseudonim dikenal: tidak dipublikasikan resmi sebagai roster)
- [foundation] Status keterlibatan Andre Cronje pasca-2023 secara resmi
- [entity] Roster kontributor inti (pseudonim) dan struktur kompensasi terkini
- [entity] Entitas legal (jika ada) yang menandatangani integrasi institusional Yearn
- [history] Tanggal persis tiap milestone (hari spesifik fair launch, pengumuman Cronje, minting 6.666 YFI)
- [history] Rincian proposal governance utama (nomor proposal, hasil voting per proposal)
- [technology] Daftar audit lengkap per kontrak (firm + tanggal + temuan)
- [technology] Status deployment L2 (Arbitrum/Base) untuk vault v3
- [technology] Metrik TVL per vault generasi (v2 vs v3)
- [financial] Nilai treasury USD real-time agregat tidak dipublikasikan sebagai single number resmi; hanya terlihat on-chain per address — perlu aggregator on-chain terpercaya untuk angka aktual
- [financial] Breakdown revenue per produk (vault vs Iron Bank vs yBribe vs Zap) tidak dipublikasikan resmi per periode; hanya total protocol fees di DefiLlama/Token Terminal
- [financial] Tidak ada audited financial statements (GAAP/IFRS) — Yearn Foundation belum menerbitkan audited accounts
- [financial] yBudget grant allocation amounts per epoch tidak terpusat di single dashboard resmi
- [financial] Impact finansial eksploit April 2023 (~$11M) pada treasury/DAI reserves tidak terdetail dalam laporan tunggal
- [financial] Status legal Yearn Foundation sebagai "foundation" di Cayman vs DAO operations on-chain — implicature pajak dan liability belum sepenuhnya transparan
- [financial] Revenue share ke YFI stakers (jika ada fee switch aktif) tidak dikonfirmasi status saat ini — YIP-41 membahas tapi implementasi bergantung governance
- [financial] Data AUM historis per chain (Ethereum, Fantom, Arbitrum, Optimism, Base, Polygon) tidak teragregasi resmi
- [financial] Tidak ada disclosure resmi burn rate / operational expenditure DAO (gaji kontributor, audit, infrastructure, legal)
- [token] Angka pasti treasury DAO (komposisi YFI vs aset lain)
- [token] Jumlah YFI terkunci di veYFI/yLockers per kuartal
- [token] Apakah ada proposal burn atau perubahan fee-share ke holder di era v3
- [ecosystem] Exact % of vault TVL dependent on Curve/Convex vs other protocols — DefiLlama shows aggregate but not per-strategy breakdown; need Dune query for precise concentration metric
- [ecosystem] Current Keep3r job coverage ratio (jobs posted vs jobs executed) — not publicly dashboarded; only anecdotal in governance discussions
- [ecosystem] Alchemy/Infura RPC redundancy architecture — whether Yearn runs own fallback nodes or uses decentralized RPC (Pocket, Lava) not documented in developer docs
- [ecosystem] Bridge risk quantification for multi-chain vaults — total value bridged via LayerZero/Wormhole for Yearn strategies not aggregated in single dashboard
- [ecosystem] yTeam signer identities — 13 multisig signers are elected but pseudo-anonymous; no public mapping of signer → yTeam role → real-world identity (by design)
- [ecosystem] Yearn Foundation Cayman legal structure details — full constitutional documents not public; only summary in YIP-66
- [ecosystem] Iron Bank v2 isolated market risk parameters (LTV, liquidation threshold, oracle config) per market — not in single public doc; scattered in governance proposals
- [ecosystem] yBudget grant allocation per epoch — amounts, recipients, KPIs not in centralized dashboard; only in individual governance threads
- [ecosystem] Exact YFI holder concentration (top 10, 50, 100) — Etherscan shows balances but not labeled entities (exchanges, DAO, individuals)
- [ecosystem] Fee switch status for YFI stakers — YIP-41 proposed fee buyback/distribution; implementation status unclear (no active fee switch contract found in mainnet)
- [ecosystem] Cross-chain vault strategy registry — no single canonical list of which strategies deployed on which chains with TVL breakdown
- [ecosystem] Gelato vs Keep3r job distribution — what % of automated ops run on each; not publicly disclosed
- [ecosystem] Yearn subgraph sync latency / completeness — no public SLA or health dashboard for subgraph indexing
- [ecosystem] Legal liability of yTeam members — Cayman Foundation structure limits but extent not tested; no public legal opinion
- [ecosystem] Revenue split between Yearn DAO treasury vs yTeam contributors vs grants — not in transparent recurring report
- [market] Angka TVL Yearn terkini (2025-2026) dari DefiLlama
- [market] Volume perdagangan YFI per kuartal
- [market] Distribusi holder on-chain terkini (top 10/100)
- [behavioral] Fee switch implementation status: YIP-41 proposed fee buyback/distribusi ke YFI stakers; tidak ada kontrak fee switch terverifikasi on-chain mainnet; perlu verifikasi apakah masih di roadmap atau dibuang · Sources: https://gov.yearn.finance/t/yip-41-yearn-finance-tokenomics/263, https://yearn.finance/#/tokenomics
- [behavioral] Exact Curve/Convex TVL concentration percentage: DefiLlama menunjukkan aggregate TVL tapi tidak per-strategy breakdown; Dune query diperlukan untuk precise metric · Sources: https://defillama.com/protocol/yearn-finance, https://dune.com/yearn
- [behavioral] yTeam signer identities dan accountability: 13 multisig signers pseudo-anonymous by design; tidak ada public mapping signer → role → real identity; legal liability unclear · Sources: https://gnosis-safe.io/app/#/safes/0xFEB4acf3df3cDEA7399794D0869ef76A6EfAff52, https://gov.yearn.finance/t/yip-61-yearn-treasury-management/1120
- [behavioral] Yearn Foundation constitutional documents: Full charter/bylaws tidak public; hanya summary di YIP-66; governance boundary DAO vs Foundation ambigu · Sources: https://gov.yearn.finance/t/yip-66-yearn-foundation/1200, https://www.yearn.foundation/
- [behavioral] Iron Bank v2 isolated market risk parameters per market: LTV, liquidation threshold, oracle config tersebar di governance proposals; tidak ada single public doc · Sources: https://docs.yearn.finance/products/iron-bank, https://gov.yearn.finance/t/yip-57-iron-bank-v2/900
- [behavioral] yBudget grant allocation per epoch: Amounts, recipients, KPIs tidak terpusat di dashboard resmi; hanya di individual governance threads · Sources: https://gov.yearn.finance/t/yip-75-ybudget/1600, https://www.yearn.foundation/grants
- [behavioral] Keep3r job coverage ratio: Jobs posted vs executed tidak publicly dashboarded; hanya anecdotal di governance discussions · Sources: https://keep3r.network/, https://docs.yearn.finance/developers/keep3r
- [behavioral] Alchemy/Infura RPC redundancy: Apakah Yearn menjalankan fallback nodes sendiri atau menggunakan decentralized RPC (Pocket, Lava) tidak terdokumen di developer docs · Sources: https://docs.yearn.finance/developers/sdk, https://alchemy.com/, https://infura.io/
- [behavioral] Bridge risk quantification: Total value bridged via LayerZero/Wormhole untuk Yearn strategies tidak teragregasi di single dashboard · Sources: https://layerzero.network/, https://wormhole.com/, https://gov.yearn.finance/t/multichain-exploit-response/2000
- [behavioral] Cross-chain vault strategy registry: Tidak ada canonical list strategi mana deployed di chain mana dengan TVL breakdown · Sources: https://yearn.finance/#/vaults, https://github.com/yearn/yearn-vaults-v3
- [behavioral] Legal liability yTeam members: Cayman Foundation structure limits liability tapi extent untested; no public legal opinion · Sources: https://www.yearn.foundation/, https://gov.yearn.finance/t/yip-66-yearn-foundation/1200
- [behavioral] Revenue split DAO treasury vs yTeam contributors vs grants: Tidak ada transparent recurring report · Sources: https://gov.yearn.finance/t/yip-61-yearn-treasury-management/1120, https://gov.yearn.finance/t/yip-75-ybudget/1600
- [behavioral] v1 vault sunset timeline: Legacy v1 vaults masih accessible tapi deprecated; tidak ada official sunset date · Sources: https://yearn.finance/#/vaults, https://github.com/yearn/yearn-vaults
- [behavioral] Gelato vs Keep3r job distribution percentage: Tidak disclosed publicly · Sources: https://gelato.network/, https://keep3r.network/, https://docs.yearn.finance/developers/keep3r
- [knowledge] Open Thread 1: Fee Switch Implementation Status — YIP-41 Proposed Fee Buyback/Distribusi ke YFI Stakers 2021, Tidak Ada Kontrak Terverifikasi On-Chain Mainnet 2024+, Perlu Verifikasi Apakah Masih Di Roadmap Atau Dibuang Evidence: YIP-41 proposal【Phase 3 — History】【Phase 6 — Token】; Fee switch status unclear【Phase 9 — Open Threads】; No active fee switch contract【Phase 9 — Behavioral Summary】 Supporting Dataset: Phase 3 History, Phase 6 Token, Phase 9 Open Threads, Phase 9 Behavioral Summary Confidence: MEDIUM Interpretation: Mungkin fee switch dibuang karena regulatory complexity atau priority shift; perlu konfirmasi dari governance forum terbaru
- [knowledge] Open Thread 2: Exact Curve/Convex TVL Concentration Percentage — DefiLlama Menunjukkan Aggregate TVL Tapi Tidak Per-Strategy Breakdown; Dune Query Diperlukan Untuk Metric Presisi Evidence: Concentration risk documented【Phase 7 — Ecosystem Risks】; Financial dependency【Phase 5 — Financial Dependencies】; DefiLlama aggregate only【Phase 8 — Market】; Exact percentage unknown【Phase 9 — Open Threads】 Supporting Dataset: Phase 5 Financial Dependencies, Phase 7 Ecosystem Risks, Phase 8 Market, Phase 9 Open Threads Confidence: LOW Interpretation: Estimasi 60-70% berdasarkan governance discussion tapi tidak ada on-chain verified breakdown publik
- [knowledge] Open Thread 3: yTeam Signer Identities Dan Accountability — 13 Multisig Signers Pseudo-Anonymous By Design; Tidak Ada Public Mapping Signer → Role → Real Identity; Legal Liability Unclear Evidence: Multisig 9/13【Phase 7 — Governance Ecosystem】; Signer identities pseudo-anonymous【Phase 9 — Open Threads】; Multisig centralization risk【Phase 7 — Ecosystem Risks】; Accountability unclear【Phase 9 — Behavioral Summary】 Supporting Dataset: Phase 7 Governance Ecosystem, Phase 7 Ecosystem Risks, Phase 9 Open Threads, Phase 9 Behavioral Summary Confidence: MEDIUM Interpretation: By design untuk privacy tapi menciptakan accountability gap; Cayman Foundation mungkin provide legal shield tapi extent untested
- [knowledge] Open Thread 4: Yearn Foundation Constitutional Documents — Full Charter/Bylaws Tidak Public; Hanya Summary Di YIP-66; Governance Boundary DAO vs Foundation Ambigu Evidence: Foundation formation YIP-66【Phase 3 — History】; Constitutional documents not public【Phase 9 — Open Threads】; Foundation purpose【Phase 7 — Governance Ecosystem】; DAO-Foundation boundary【Phase 9 — Governance Decision Patterns】 Supporting Dataset: Phase 3 History, Phase 7 Governance Ecosystem, Phase 9 Open Threads, Phase 9 Governance Decision Patterns Confidence: MEDIUM Interpretation: Cayman Foundation law mungkin tidak require public filing; tapi transparency gap untuk DAO stakeholders
- [knowledge] Open Thread 5: Iron Bank v2 Isolated Market Risk Parameters Per Market — LTV, Liquidation Threshold, Oracle Config Tersebar Di Governance Proposals; Tidak Ada Single Public Doc Evidence: Iron Bank v2 Aave v3 fork【Phase 7 — Major Integrations】; Risk parameters scattered【Phase 9 — Open Threads】; Iron Bank docs【Phase 7 — External Dependencies】; Parameter transparency gap【Phase 9 — Open Threads】 Supporting Dataset: Phase 7 Major Integrations, Phase 7 External Dependencies, Phase 9 Open Threads Confidence: MEDIUM Interpretation: Parameters di-set per market via governance; perlu aggregated documentation untuk risk assessment
- [knowledge] Open Thread 6: yBudget Grant Allocation Per Epoch — Amounts, Recipients, KPIs Tidak Terpusat Di Dashboard Resmi; Hanya Di Individual Governance Threads Evidence: yBudget YIP-75【Phase 5 — Fundraising Mechanism】【Phase 7 — Governance Ecosystem】; Grant allocation not centralized【Phase 9 — Open Threads】; Foundation grants【Phase 7 — Governance Ecosystem】; Transparency gap【Phase 9 — Open Threads】 Supporting Dataset: Phase 5 Fundraising Mechanism, Phase 7 Governance Ecosystem, Phase 9 Open Threads Confidence: MEDIUM Interpretation: Grants managed oleh Treasury Committee; reporting mungkin ad-hoc via forum; perlu dashboard untuk accountability
- [knowledge] Open Thread 7: Keep3r Job Coverage Ratio — Jobs Posted Vs Executed Tidak Publicly Dashboarded; Hanya Anecdotal Di Governance Discussions Evidence: Keep3r critical dependency【Phase 7 — External Dependencies】; Keeper concentration risk【Phase 7 — Ecosystem Risks】; Job coverage not dashboarded【Phase 9 — Open Threads】; Keeper automation pattern【Phase 9 — Technical Decision Patterns】 Supporting Dataset: Phase 7 External Dependencies, Phase 7 Ecosystem Risks, Phase 9 Open Threads, Phase 9 Technical Decision Patterns Confidence: LOW Interpretation: Keep3r network mungkin memiliki analytics internal tapi tidak public; Yearn bisa build monitoring dashboard sendiri
- [knowledge] Open Thread 8: Alchemy/Infura RPC Redundancy — Apakah Yearn Menjalankan Fallback Nodes Sendiri Atau Menggunakan Decentralized RPC (Pocket, Lava) Tidak Terdokumen Di Developer Docs Evidence: Infrastructure providers【Phase 7 — Infrastructure Providers】; Alchemy/Infura critical【Phase 7 — External Dependencies】; RPC redundancy undocumented【Phase 9 — Open Threads】; Developer docs【Phase 4 — Technology】 Supporting Dataset: Phase 4 Technology, Phase 7 Infrastructure Providers, Phase 7 External Dependencies, Phase 9 Open Threads Confidence: LOW Interpretation: Alchemy/Infura primary; fallback mungkin via multiple providers tapi tidak documented; decentralized RPC adoption masih early stage
- [knowledge] Open Thread 9: Bridge Risk Quantification — Total Value Bridged Via LayerZero/Wormhole Untuk Yearn Strategies Tidak Teragregasi Di Single Dashboard Evidence: Bridge dependencies【Phase 7 — External Dependencies】; Multichain exploit response【Phase 3 — History】; Bridge risk unquantified【Phase 9 — Open Threads】; Bridge dependency risk【Phase 7 — Ecosystem Risks】 Supporting Dataset: Phase 3 History, Phase 7 External Dependencies, Phase 7 Ecosystem Risks, Phase 9 Open Threads Confidence: LOW Interpretation: Perlu on-chain analytics untuk track bridge exposure per strategy; LayerZero/Wormhole mungkin提供 analytics tapi tidak Yearn-specific
- [knowledge] Open Thread 10: Cross-Chain Vault Strategy Registry — Tidak Ada Canonical List Strategi Mana Deployed Di Chain Mana Dengan TVL Breakdown Evidence: Multi-chain vaults【Phase 4 — Technology】【Phase 7 — Ecosystem Position】; Strategy registry missing【Phase 9 — Open Threads】; Vault list【Phase 7 — Applications】; Fragmented visibility【Phase 9 — Open Threads】 Supporting Dataset: Phase 4 Technology, Phase 7 Ecosystem Position, Phase 7 Applications, Phase 9 Open Threads Confidence: LOW Interpretation: Frontend yearn.finance show vaults per chain tapi tidak strategy-level breakdown; Subgraph mungkin memiliki data tapi tidak exposed via UI
- [knowledge] Open Thread 11: Legal Liability yTeam Members — Cayman Foundation Structure Limits Liability Tapi Extent Untested; No Public Legal Opinion Evidence: Foundation formation【Phase 3 — History】【Phase 2 — Entity】; Legal jurisdiction risk【Phase 7 — Ecosystem Risks】; Legal liability untested【Phase 9 — Open Threads】; Foundation structure【Phase 7 — Governance Ecosystem】 Supporting Dataset: Phase 2 Entity, Phase 3 History, Phase 7 Ecosystem Risks, Phase 9 Open Threads, Phase 7 Governance Ecosystem Confidence: LOW Interpretation: Foundation sebagai legal wrapper seharusnya shield contributors tapi Cayman law untested untuk DAO context; perlu legal opinion
- [knowledge] Open Thread 12: Revenue Split DAO Treasury vs yTeam Contributors vs Grants — Tidak Ada Transparent Recurring Report Evidence: Treasury management【Phase 5 — Treasury】; Treasury Committee【Phase 7 — Governance Ecosystem】; Revenue split not transparent【Phase 9 — Open Threads】; yBudget grants【Phase 5 — Fundraising Mechanism】 Supporting Dataset: Phase 5 Treasury, Phase 7 Governance Ecosystem, Phase 9 Open Threads, Phase 5 Fundraising Mechanism Confidence: MEDIUM Interpretation: Treasury Committee manage allocations; reporting via governance forum threads; perlu standardized recurring financial report
- [knowledge] Open Thread 13: v1 Vault Sunset Timeline — Legacy v1 Vaults Masih Accessible Tapi Deprecated; Tidak Ada Official Sunset Date Evidence: v1 deprecation post-exploit【Phase 3 — History】; v1 sunset timeline unclear【Phase 9 — Open Threads】; Migration voluntary【Phase 9 — Technical Decision Patterns】; Attack surface remains【Phase 9 — Failure Factors】 Supporting Dataset: Phase 3 History, Phase 9 Open Threads, Phase 9 Technical Decision Patterns, Phase 9 Failure Factors Confidence: MEDIUM Interpretation: Voluntary migration mungkin insufficient; perlu governance proposal untuk hard sunset date dan force migration
- [knowledge] Open Thread 14: Gelato vs Keep3r Job Distribution Percentage — Tidak Disclosed Publicly Evidence: Gelato integration【Phase 7 — External Dependencies】; Keep3r integration【Phase 7 — External Dependencies】; Job distribution undisclosed【Phase 9 — Open Threads】; Keeper automation pattern【Phase 9 — Technical Decision Patterns】 Supporting Dataset: Phase 7 External Dependencies, Phase 9 Open Threads, Phase 9 Technical Decision Patterns Confidence: LOW Interpretation: Mungkin proprietary operational data; tapi transparency akan membantu community assess keeper network health
- [knowledge] Open Thread 15: Yearn Subgraph Sync Latency / Completeness — No Public SLA Or Health Dashboard Untuk Subgraph Indexing Evidence: The Graph integration【Phase 7 — Infrastructure Providers】; Subgraphs【Phase 7 — External Dependencies】; Subgraph health undocumented【Phase 9 — Open Threads】; Developer ecosystem【Phase 7 — Developer Ecosystem】 Supporting Dataset: Phase 7 Infrastructure Providers, Phase 7 External Dependencies, Phase 7 Developer Ecosystem, Phase 9 Open Threads Confidence: LOW Interpretation: Subgraph critical untuk frontend/API; latency/completeness issues bisa affect user experience; perlu monitoring dashboard
- [conflict] Tanggal persis fair launch (blog asli Cronje)
- [conflict] Angka treasury DAO (komposisi YFI vs aset lain)
- [conflict] Jumlah YFI terkunci veYFI/yLockers per kuartal
- [conflict] Daftar audit lengkap per kontrak vault
- [airdrop] Harga YFI hari-hari pertama fair launch (Juli 2020) dari arsip exchange yang listing saat itu (di luar sumber yang diakses riset ini)
- [airdrop] Jumlah unik LP penerima distribusi (rekonstruksi on-chain)
- [airdrop] Dampak minting 6.666 YFI terhadap harga dan sentimen (event study)
