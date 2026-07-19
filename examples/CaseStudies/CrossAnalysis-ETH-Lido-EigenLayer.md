# Cross-Project Analysis — Ethereum × Lido × EigenLayer: The Staking → Restaking Stack

**CIF Dataset — Cross-Project Analysis · Tier: Synthesis**
**Source:** Synthesis of existing curated artifacts (no new research). Derived from:
`examples/CaseStudies/Ethereum.md`, `examples/Pioneer/Lido.md`, `examples/Pioneer/EigenLayer.md`.
**Pipeline position:** `Patterns → Reasoning` — turns three project histories into transferable patterns
and prediction inputs.

> Knowledge artifact (analysis of curated data). Every claim traces back to the three source dossiers and
> the `docs/` ontology. No fabricated facts or figures.

---

## Scope

Ethereum's move to Proof of Stake (The Merge, Sep 2022) created a new economic layer. Two projects built
directly on top of it and now sit inside Ethereum's own security perimeter: **Lido** (liquid staking) and
**EigenLayer** (restaking). This analysis reads the three as **one dependency stack** and extracts the
patterns that repeat — and *compound* — as you move up it.

## 1. The dependency stack (why these three are one system)

```
Ethereum PoS  (32 ETH to solo-stake; capital locked, illiquid)
     │  problem: capital efficiency + accessibility
     ▼
Lido          (deposit any ETH → stETH; liquid, reusable in DeFi)
     │  problem solved, but stake now pools into a few operators
     ▼
EigenLayer    (restake ETH / stETH / LSTs to secure external AVS)
     │  reuses the SAME staked ETH to secure more services
     ▼
LRTs          (Ether.fi eETH, Renzo ezETH, KelpDAO) → yield stacking
```

- **ETH** provides the base security and the 32-ETH friction. _(ref `examples/CaseStudies/Ethereum.md` §8)_
- **Lido** removes the friction: deposit any amount, receive rebasing **stETH**, stay liquid. _(ref `examples/Pioneer/Lido.md`)_
- **EigenLayer** reuses that staked ETH/LSTs to secure Actively Validated Services (AVS), with **LRTs**
  (eETH, ezETH) auto-distributing across AVS for yield. _(ref `examples/Pioneer/EigenLayer.md`, `Ethereum.md` §8)_

Each layer solves the layer below's inefficiency — and inherits its risk while adding its own.

## 2. Recurring pattern: **efficiency → concentration → mitigation**
_ref: `docs/Patterns/NetworkEffect.md`, `docs/Ontology/Risks.md`, `docs/Innovation/CompetitiveMoat.md`_

The same causal loop appears at every layer of the stack:

| Layer | Efficiency gain | Concentration it created | Mitigation response |
|-------|-----------------|--------------------------|---------------------|
| **Lido** | Liquid, any-amount staking | Peaked **>32%** of all staked ETH (2023) → consensus/censorship concern | **DVT** (Obol, SSV) splits a validator key across independent operators; **Dual Governance** |
| **EigenLayer** | Reuse staked ETH to secure many AVS | Restaked collateral concentrates into a few AVS/operators | **slashing-by-forking** + social arbitration (EIGEN/bEIGEN); LRT diversification across AVS |
| **Ethereum (base)** | Cheap L2 execution via Dencun | Sequencer/DA reliance | Roadmap toward decentralized sequencing / DAS |

**Transferable pattern:** *any capital-efficiency innovation in crypto tends to centralize the resource it
frees, then triggers a distributed mitigation.* This is the single most reusable lesson of the stack.
_(source: `Lido.md` centralization → DVT; `EigenLayer.md` shared-security risk; `Ethereum.md` §8)_

## 3. Shared thread: **security = cryptography + social consensus**
_ref: `docs/Ontology/Security.md`, `docs/Ontology/Governance.md`, `docs/Reasoning/Confidence.md`_

Ethereum's history already proved that when code fails systemically, **human social consensus is the final
backstop** — The DAO fork (2016) and the *rejection* of EIP-999 (2017) both show the community, not the
code, deciding. _(ref `Ethereum.md` §7)_

EigenLayer **institutionalizes** exactly this. It separates:
- **objective faults** (double-signing) — provable on-chain, slashed automatically; from
- **intersubjective faults** (oracle manipulation, censorship) — *not* unilaterally provable, resolved by
  **slashing-by-forking**: a challenger burns EIGEN to fork the token, and **social consensus** picks the
  branch with real economic value. _(ref `EigenLayer.md`)_

So EigenLayer is, in effect, a **productized version of Ethereum's ad-hoc DAO-era social consensus** — the
same principle (`docs/Reasoning/Confidence.md`: intersubjective truth needs human coordination), now a
repeatable mechanism. This is a direct causal lineage, not a coincidence.

## 4. Stacked systemic risk: the failure mode
_ref: `docs/Patterns/Failure.md`, `docs/MarketBehaviour/DeathSpiral.md`, `docs/Ontology/Risks.md`_

The stack's efficiency is also its fragility. Risk **compounds upward**:

1. **stETH is money in DeFi** — used as collateral everywhere. A discount/depeg (as seen in the 2022 CeFi
   deleveraging) transmits stress across every protocol holding it.
2. **EigenLayer reuses the same ETH** to secure many AVS → **collateral looping**. One large AVS failure can
   trigger **cascading slashing** that propagates through the LRT layer (eETH/ezETH) back down to stakers.
   _(ref `Ethereum.md` §8: "collateral looping / cascading slashing"; `EigenLayer.md`: systemic financial risk)_
3. Because all three share the **same underlying ETH**, a shock does not stay contained to one layer — it
   can loop **Ethereum ⇄ Lido ⇄ EigenLayer**.

**Transferable pattern:** *rehypothecation of a single security asset raises yield and correlation of failure
at the same time.* A new restaking/LRT project inherits this whole risk stack, not just its own smart-contract risk.

## 5. Extracted patterns (for the reasoning engine)
_These become analog inputs for `docs/Reasoning/AnalogEngine.md` and `docs/Reasoning/Prediction.md`._

1. **Efficiency → concentration → distributed mitigation** (Lido→DVT; EigenLayer→LRT diversification). → `docs/Patterns/NetworkEffect.md`
2. **Social consensus as the ultimate security layer** (ETH DAO/EIP-999 → EigenLayer slashing-by-forking). → `docs/Ontology/Security.md`
3. **Rehypothecation trades yield for correlated, cascading failure** (stETH → restaking → LRT looping). → `docs/Patterns/Failure.md`
4. **Dependency inheritance** — each layer inherits the risk of every layer below it. → `docs/Ontology/Risks.md`
5. **Productization of an ad-hoc precedent** — a repeated manual behaviour (ETH social forks) becomes a
   designed mechanism (EigenLayer). → `docs/Innovation/CategoryCreator.md`

## 6. Prediction implications (how the Analysis role uses this)
_ref: `docs/Protocol/Role-Analysis.md`, `docs/Reasoning/Similarity.md`_

When a **new liquid-staking, restaking, or LRT project** appears, reason by analogy to this stack:
- **Expect the concentration loop.** If it wins on efficiency, it will concentrate the freed resource →
  watch for the mitigation (or its absence) as a quality signal.
- **Price the inherited risk stack**, not just the app. An LRT sits on restaking sits on staking sits on ETH.
- **Confidence:** this pattern is supported by **≥3 independent instances** already (ETH base, Lido, EigenLayer)
  plus the LRT cohort — a **Medium–High** confidence pattern under `docs/Reasoning/Confidence.md`.
- **Watch-for signals:** dominance share crossing ~⅓, single-AVS collateral concentration, stETH/LRT
  discount events, governance capture.

## 7. Related files
- Deep dossier: `examples/CaseStudies/Ethereum.md` (§7 governance, §8 staking/restaking)
- Profiles: `examples/Pioneer/Lido.md`, `examples/Pioneer/EigenLayer.md`
- Ontology: `docs/Ontology/Security.md`, `Risks.md`, `Governance.md`, `Tokenomics.md`
- Patterns: `docs/Patterns/NetworkEffect.md`, `Failure.md`
- Reasoning: `docs/Reasoning/Confidence.md`, `Similarity.md`, `AnalogEngine.md`, `Prediction.md`
- Market: `docs/MarketBehaviour/DeathSpiral.md`
