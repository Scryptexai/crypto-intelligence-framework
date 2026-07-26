# Backtest 02 · Helium Multi-token Simplification
- type: consistency
- category: DePIN
- given: depin, multi-token, mining
- expect: P3
- outcome: HIP-138 (awal 2025) — Helium menghentikan emisi IOT & MOBILE dan mengonsolidasikan seluruh tokenomics ke HNT tunggal; 18,2 miliar MOBILE dibakar.
- source: findas/IQ.wiki (Helium's own profile, `examples/Pioneer/Helium.md`, was moved to
  `_archive_pre_v3/examples/Pioneer/` in the 2026-07-26 dataset reset — this case's given/expect tags don't
  depend on that file, only on the pattern trigger match)
- note: In-sample consistency check (Helium ikut menurunkan P3). Menguji bahwa harness meng-klasifikasikan sinyal multi-token ke pola yang benar, bukan validasi out-of-sample.
