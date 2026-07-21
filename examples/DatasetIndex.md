# CIF Dataset Index

**Pipeline position:** Applications layer — validated knowledge produced by `Research → Extraction` and
structured against the `docs/` ontology.

> Knowledge artifacts (real curated data), not documentation containers. Each conforms to
> `templates/ProjectTemplate.md` and links back to the ontology it instantiates.

This is the master curation record for the dataset stored in `examples/`: what was added per batch,
how the taxonomy is distributed, where the gaps are, and what is queued next.

**Batches loaded:** Batch 01 (8 projects, source: Deep Research / Gemini) · Batch 02 (10 projects, source: Web research) · Deep Dossiers (9: Ethereum, Solana, BNB Chain, Cardano, Avalanche, Polkadot, Cosmos, dYdX, Aave — source: Deep Research / Gemini).
**Total curated projects: 25** _(D8 dYdX and D9 Aave supersede their Batch Summaries — same projects, not double-counted)_.

## Curation Tiers
_How each project is captured (see `docs/Protocol/` for the runbooks)._

| Tier | What | Location | Throughput |
|------|------|----------|------------|
| **Deep** | Full causal dossier for anchor projects | `examples/CaseStudies/<Project>.md` | ~1 / session |
| **Summary** | One profile per project for breadth | `examples/Pioneer/` (or `Successful/`, `Failed/`) | ~10–15 / session |
| **Tracking** | Living record of a project being worked/followed | `tracking/<Project>/` | ongoing |

Target ~1000 projects ≈ ~50 Deep + ~950 Summary ≈ ~150 sessions (state persists in git; per-session cost is flat).

## Deep Dossiers
_Tier: Deep · anchor projects with full causal history._

| # | Project | Category | Era | Source | File | Raw source |
|---|---------|----------|-----|--------|------|-----------|
| D1 | Ethereum | Layer 1 / Smart-Contract Platform | 2013– | Deep Research (Gemini) | `CaseStudies/Ethereum.md` | `doc_backup/deep/Ethereum_2026-07_gemini.pdf` |
| D2 | Solana | Layer 1 / High-Performance Monolithic Platform | 2017– | Deep Research (Gemini) | `CaseStudies/Solana.md` | `doc_backup/deep/Solana_2026-07_gemini.docx` |
| D3 | BNB Chain | Layer 1 EVM (Exchange-backed) + modular suite (opBNB/Greenfield) | 2017– | Deep Research (Gemini) | `CaseStudies/BNBChain.md` | `doc_backup/deep/BNBChain_2026-07_gemini.docx` |
| D4 | Cardano | Layer 1 / Peer-reviewed EUTXO platform (Ouroboros PoS) | 2015– | Deep Research (Gemini) | `CaseStudies/Cardano.md` | `doc_backup/deep/Cardano_2026-07_gemini.pdf` |
| D5 | Avalanche | Layer 1 / Metastable-consensus multi-chain (Subnet/L1) + RWA-TradFi | 2018– | Deep Research (Gemini) | `CaseStudies/Avalanche.md` | `doc_backup/deep/Avalanche_2026-07_gemini.docx` (rebuilt; prior PDF retained) |
| D6 | Polkadot | Layer 0 / Heterogeneous-sharding + shared-security (Relay/parachains) | 2016– | Deep Research (Gemini) | `CaseStudies/Polkadot.md` | `doc_backup/deep/Polkadot_2026-07_gemini.docx` |
| D7 | Cosmos | Layer 0 / Appchain "Internet of Blockchains" (CometBFT/SDK/IBC) | 2014– | Deep Research (Gemini) | `CaseStudies/Cosmos.md` | `doc_backup/deep/Cosmos_2026-07_gemini.docx` |
| D8 | dYdX | DeFi / Perp-derivatives DEX (order-book appchain → RWA pivot) | 2017– | Deep Research (Gemini) | `CaseStudies/dYdX.md` | `doc_backup/deep/dYdX_2026-07_gemini.docx` |
| D9 | Aave | DeFi / Money-market lending (Flash Loans, GHO, V4 Hub-and-Spoke) | 2017– | Deep Research (Gemini) | `CaseStudies/Aave.md` | `doc_backup/deep/Aave_2026-07_gemini.docx` |

---

## Curated Projects — Batch 01
_Container: `examples/Pioneer/` · Source: Deep Research (Gemini) — "Rekomendasi Kurasi Proyek Historis"._
_Raw source archived: `doc_backup/batch/Batch-01_Kurasi-Dataset_2026-07_gemini.pdf` (+ `.md`)._

| # | Project | Category | Era | Priority | File |
|---|---------|----------|-----|----------|------|
| 1 | Celestia | Modular / Data Availability | 2019– | P0 | `Pioneer/Celestia.md` |
| 2 | Synthetix | DeFi (DeFi Pioneer) | 2017– | P0 | `Pioneer/Synthetix.md` |
| 3 | Helium | DePIN (IoT & Wireless) | 2013– | P0 | `Pioneer/Helium.md` |
| 4 | EigenLayer | Infrastructure / Restaking | 2021– | P0 | `Pioneer/EigenLayer.md` |
| 5 | Aave | DeFi (DeFi Pioneer) | 2017– | P1 | `Pioneer/Aave.md` → **superseded by Deep D9** `CaseStudies/Aave.md` |
| 6 | Arweave / AO | Data Availability / Modular Compute | 2017– | P1 | `Pioneer/Arweave-AO.md` |
| 7 | Farcaster | Social (Decentralized Social) | 2020– | P1 | `Pioneer/Farcaster.md` |
| 8 | MakerDAO / Sky | DeFi (Decentralized Central Bank) | 2015– | P0 | `Pioneer/MakerDAO-Sky.md` |

Cross-project analysis: `examples/CaseStudies/Batch-01-EvolutionAnalysis.md`.

## Cross-Project Analyses
_Syntheses that turn multiple project histories into transferable patterns (tier: Synthesis)._

| Analysis | Projects linked | File |
|----------|-----------------|------|
| Batch 01 Evolution | Celestia, Arweave/AO, Helium, Synthetix, EigenLayer | `CaseStudies/Batch-01-EvolutionAnalysis.md` |
| Staking → Restaking Stack | Ethereum, Lido, EigenLayer | `CaseStudies/CrossAnalysis-ETH-Lido-EigenLayer.md` |

## Curated Projects — Batch 02
_Container: `examples/Pioneer/` · Source: Web research (public sources, July 2026 — cited per file)._
_Promoted from the Batch 01 candidate queue. Provenance is web research, **not** Deep Research (Gemini)._

| # | Project | Category | Era | Priority | File |
|---|---------|----------|-----|----------|------|
| 9 | Safe | Wallet / Account Abstraction | 2017– | P0 | `Pioneer/Safe.md` |
| 10 | Chainlink | Oracle | 2017– | P0 | `Pioneer/Chainlink.md` |
| 11 | LayerZero | Bridge / Interoperability | 2021– | P1 | `Pioneer/LayerZero.md` |
| 12 | Lido | Liquid Staking | 2020– | P1 | `Pioneer/Lido.md` |
| 13 | Uniswap | DeFi / AMM | 2018– | P1 | `Pioneer/Uniswap.md` |
| 14 | World Network (Worldcoin) | Identity | 2019– | P1 | `Pioneer/WorldNetwork-Worldcoin.md` |
| 15 | dYdX | DeFi / Appchain | 2017– | P1 | `Pioneer/dYdX.md` → **superseded by Deep D8** `CaseStudies/dYdX.md` |
| 16 | Ethena | DeFi / Stablecoin | 2023– | P2 | `Pioneer/Ethena.md` |
| 17 | Berachain | Layer 1 (Proof-of-Liquidity) | 2021– | P2 | `Pioneer/Berachain.md` |
| 18 | Optimism | Layer 2 (OP Stack / Superchain) | 2019– | P2 | `Pioneer/Optimism.md` |

## Dataset Distribution (Cumulative)
_After Batch 01 + Batch 02._

| Category | Batch 01 | Batch 02 | Cumulative |
|----------|----------|----------|------------|
| DeFi (Pioneer, AMM, Appchain, Stablecoin, Central Bank) | 3 | 3 | 6 |
| Modular / Data Availability | 1 | 0 | 1 |
| Data Availability / Modular Compute | 1 | 0 | 1 |
| Infrastructure / Restaking | 1 | 0 | 1 |
| DePIN | 1 | 0 | 1 |
| Social | 1 | 0 | 1 |
| Wallet / Account Abstraction | 0 | 1 | 1 |
| Oracle | 0 | 1 | 1 |
| Bridge / Interoperability | 0 | 1 | 1 |
| Liquid Staking | 0 | 1 | 1 |
| Identity | 0 | 1 | 1 |
| Layer 1 | 0 | 1 | 1 |
| Layer 2 | 0 | 1 | 1 |
| **Total** | **8** | **10** | **18** |

## Dataset Gap — Status
_Progress against the gaps identified in Batch 01._

- **Wallet & Account Abstraction** — ✅ terisi oleh **Safe** (Batch 02).
- **Oracle & Real-Time Data Infrastructure** — ✅ terisi oleh **Chainlink** (Batch 02).
- **Cross-Chain Communication & Bridges** — ✅ terisi oleh **LayerZero** (Batch 02).
- **Privacy & Identity Security** — ⚠️ *sebagian*: identitas/proof-of-personhood terisi oleh **Worldcoin**,
  namun **privasi transaksi berbasis Zero-Knowledge Proofs** (mis. Aztec, Railgun, Zcash) masih terbuka.

### Remaining / New Gaps (untuk batch berikutnya)
- **ZK Privacy** — protokol privasi transaksi berbasis ZKP.
- **RWA (Real-World Assets)** — ⚠️ *sebagian*: adopsi RWA/TradFi institusional terisi oleh **Avalanche** (Deep D5:
  Evergreen/AvaCloud, Progmat $2,8 mrd, JPMorgan Onyx); RWA sebagai **kategori Summary tersendiri** masih terbuka.
- **Gaming / NFT Infrastructure** — belum terwakili.
- **AI x Crypto** — kategori baru yang berkembang pesat.

## Candidate Queue — Status
_The Batch 01 candidate queue has been **fully processed into Batch 02** (see table above)._
The queue is now empty; the next queue will be defined from the Remaining/New Gaps section once
new research is available.

> Note: a candidate queue is a curation backlog of instances. It lives here in `examples/` (knowledge),
> not in `docs/Research/` (which documents *how* research is done, not *what* to research).

---

## Karya yang Dikutip — Batch 01 (Bibliography)
_Sumber Deep Research untuk Batch 01._

1. Modularity and App-Specific Chains — Blockchain@NUS, Medium — https://medium.com/@nusfintech.bc/modularity-and-app-specific-chains-524547bc33a8
2. celestiaorg/celestia-core (fork of CometBFT) — GitHub — https://github.com/celestiaorg/celestia-core
3. nmt/docs/spec/nmt.md — celestiaorg/nmt, GitHub — https://github.com/celestiaorg/nmt/blob/master/docs/spec/nmt.md
4. AMA: AO and Artificial Intelligence — Perma DAO, Medium — https://medium.com/@perma_dao/ama-ao-and-artificial-intelligence-93dc5649dc39
5. Let's solve these crucial protocol weaknesses — DFINITY Forum — https://forum.dfinity.org/t/lets-solve-these-crucial-protocol-weaknesses/28329?page=2
6. AVS Risk Assessment: EigenDA — LlamaRisk Research — https://llamarisk.com/research/avs-risk-assessment-eigenda
7. API Providers — APIs.io — https://apis.io/providers/
8. Synthetix Price: SNX/USD — CoinGecko — https://www.coingecko.com/en/coins/synthetix-network-token
9. The Tokenomics of Helium (HNT) — findas.org — https://www.findas.org/tokenomics-review/coins/the-tokenomics-of-helium-hnt/r/DUr5bvmBPVYzPkKJUiXz7Z
10. Helium Mining 2026: The Complete Operator Guide — MillionMiner — https://millionminer.com/news/helium-mining-2026-complete-operator-guide
11. simpleaswater/defi-resources — GitHub — https://github.com/simpleaswater/defi-resources
12. Catching Up to Crypto — DOKUMEN.PUB — https://dokumen.pub/catching-up-to-crypto-your-guide-to-bitcoin-and-the-new-digital-economy-9781394158744-9781394158751-9781394158768-1394158742-c-6678457.html
13. Helium — Cryptoassets, IQ.wiki — https://iq.wiki/wiki/helium
14. Helium Network — Wikipedia — https://en.wikipedia.org/wiki/Helium_Network
15. EIGEN: The Universal Intersubjective Work Token — EigenCloud — https://docs.eigencloud.xyz/assets/files/EIGEN_Token_Whitepaper-0df8e17b7efa052fd2a22e1ade9c6f69.pdf
16. EigenCloud: Rebuilding Web3's Trust Foundation — blockeden.xyz — https://blockeden.xyz/blog/2025/12/03/eigencloud-rebuilding-web3-s-trust-foundation-through-verifiable-cloud-infrastructure/
17. The Delphi Podcast — Buzzsprout — https://feeds.buzzsprout.com/2609274.rss
18. EIGEN Token Whitepaper (HTML) — EigenCloud — https://docs.eigencloud.xyz/html/EIGEN_Token_Whitepaper-converted-xodo.html

## Bibliography — Batch 02
_Sumber riset web (diakses Juli 2026). Rincian per-proyek ada di bagian "Sources" tiap file._

- **Safe** — IQ.wiki (https://iq.wiki/wiki/safe); Gnosis Forum GIP-29 (https://forum.gnosis.io/t/gip-29-spin-off-safedao-and-launch-safe-token/3476); Safe Foundation Tokenomics (https://safefoundation.org/blog/safe-tokenomics)
- **Chainlink** — Wikipedia (https://en.wikipedia.org/wiki/Chainlink_(blockchain_oracle)); Messari (https://messari.io/project/chainlink/profile)
- **LayerZero** — LayerZero Docs (https://docs.layerzero.network/v2/concepts/layerzero-protocol-architecture); Messari (https://messari.io/report/understanding-layerzero)
- **Lido** — lido.fi (https://lido.fi/); Messari (https://messari.io/report/liquid-staking-with-lido); Datawallet (https://www.datawallet.com/crypto/lido-explained)
- **Uniswap** — Wikipedia (https://en.wikipedia.org/wiki/Uniswap); Uniswap Blog (https://blog.uniswap.org/uniswap-history)
- **World Network (Worldcoin)** — TechCrunch (https://techcrunch.com/2024/10/17/sam-altmans-worldcoin-becomes-world-and-shows-new-iris-scanning-orb-to-prove-your-humanity/); Quartz (https://qz.com/sam-altman-worldcoin-crypto-ai-biometrics-identity-1850669360)
- **dYdX** — Antonio Juliano, Medium (https://antonio-dydx.medium.com/the-history-of-dydx-so-far-68bf46789f86); dYdX v4 Evolution, Medium (https://medium.com/@gwrx2005/dydx-v4-architectural-and-protocol-evolution-from-v3-6c312f51f7b7)
- **Ethena** — Ethena Docs (https://docs.ethena.fi/); Nansen (https://nansen.ai/post/what-is-ethena)
- **Berachain** — Fireblocks (https://www.fireblocks.com/blog/what-is-berachain-and-proof-of-liquidity); DAIC Capital (https://daic.capital/blog/berachain-tokens-explained); Decrypt (https://decrypt.co/resources/what-is-berachain-proof-of-liquidity-blockchain)
- **Optimism** — Coin Bureau (https://coinbureau.com/review/optimism-review); Eco (https://eco.com/support/en/articles/10273675-what-is-optimism-the-ethereum-l2-and-op-mainnet-explained); The Block (https://www.theblock.co/linked/149464/optimisms-governance-token-officially-goes-live)
