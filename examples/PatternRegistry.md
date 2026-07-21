# Pattern Registry (machine-readable)

Consolidated catalogue of the transferable patterns extracted from the deep dossiers and cross-project
analyses. This is the single place the reasoning layer (and `tools/build_json.py`) reads patterns from —
prose analyses remain the human explanation; this file is their structured index.

**Format (parsed by `tools/build_json.py`):** each pattern is a `## <ID> · <Name>` heading followed by
`- key: value` bullets. Keys: `triggers` (comma list), `instances` (int), `analogs` (comma list),
`source` (repo path), `validated` (optional), `prediction`, `watch` (semicolon list). Confidence is derived
from `instances` (≥3 HIGH · 2 MEDIUM · 1 LOW).

---

## P1 · Efficiency → Concentration → Mitigation
- triggers: liquid-staking, restaking, efficiency
- instances: 3
- analogs: Lido, EigenLayer, Ethereum
- source: examples/CaseStudies/CrossAnalysis-ETH-Lido-EigenLayer.md
- validated:
- prediction: Jika menang di efisiensi modal, sumber daya (stake) akan terkonsentrasi → muncul kekhawatiran sentralisasi & dorongan mitigasi terdistribusi (mis. DVT). Nilai harus dinilai bersama ada/tidaknya mitigasi.
- watch: dominance > ~1/3 dari share; absennya mitigasi desentralisasi

## P2 · Rehypothecation → Correlated Cascading Failure
- triggers: restaking, lrt, looping, liquid-restaking
- instances: 3
- analogs: EigenLayer, ether.fi, Ethereum
- source: examples/CaseStudies/CrossAnalysis-ETH-Lido-EigenLayer.md
- validated: Renzo ezETH depeg Apr 2024 (~$688, >$65jt liquidations)
- prediction: Menggunakan ulang aset yang sama menaikkan yield sekaligus korelasi kegagalan. Risiko depeg + cascading liquidations saat leverage looping unwinding.
- watch: LRT discount / depeg event; posisi looping di lending; akhir window airdrop + likuiditas tipis

## P3 · Multi-token → Simplification
- triggers: multi-token
- instances: 2
- analogs: Helium, Synthetix
- source: examples/CaseStudies/Batch-01-EvolutionAnalysis.md
- validated:
- prediction: Tokenomics multi-token yang rumit cenderung disederhanakan ke aset tunggal seiring project matang.
- watch: distorsi insentif antar-token; beban kognitif user

## P4 · Airdrop-without-product → Post-TGE dump
- triggers: airdrop, points
- instances: 2
- analogs: ether.fi, LayerZero, Ethena
- source: examples/CaseStudies/CrossAnalysis-ETH-Lido-EigenLayer.md
- validated: Renzo REZ (alokasi 5%, exit farmer pasca-window)
- prediction: Airdrop/points tanpa produk & usage nyata → farmer keluar pasca-TGE → tekanan jual. Airdrop dengan produk dominan lebih dulu (Uniswap/Hyperliquid) → retensi jauh lebih baik.
- watch: alokasi airdrop kecil/membingungkan; aktivitas hanya untuk poin; unlock/vesting pasca-TGE

## P5 · Technical success → Tokenomic harm
- triggers: fee-burn, upgrade, l2
- instances: 1
- analogs: Ethereum
- source: examples/CaseStudies/Ethereum.md
- validated: ETH Dencun (2024) → net-inflasi
- prediction: Upgrade yang memindah aktivitas keluar dari mekanisme value-accrual bisa merusak tesis token walau sukses teknis.
- watch: burn/revenue turun pasca-upgrade

## P6 · First-mover + standard = strongest moat
- triggers: first-mover, smart-contract, amm
- instances: 2
- analogs: Ethereum, Uniswap
- source: examples/CaseStudies/Ethereum.md
- validated:
- prediction: First mover yang menjadi standar developer punya moat retensi terkuat, mengalahkan pesaing 'lebih cepat/murah'.
- watch: apakah pesaing mengadopsi standarnya
