# Batch 01 — Analisis Dinamika Evolusi & Pembelajaran Kriptoekonomi

**CIF Dataset — Batch 01 · Curated Historical Project**
**Source:** Deep Research (Gemini) — *"Rekomendasi Kurasi Proyek Historis: Fondasi Arsitektur Pengetahuan Crypto Intelligence Framework"*.
**Pipeline position:** Applications layer — validated knowledge produced by `Research → Extraction` and structured against the `docs/` ontology.

> This is a knowledge artifact (real curated data), not a documentation container. It conforms to `templates/ProjectTemplate.md` and links back to the ontology it instantiates.

Cross-project synthesis derived from the eight curated Pioneer studies in `examples/Pioneer/`.
It captures the causal patterns and macro-trends extracted from their histories — the raw material
for the `Patterns → Reasoning` stages of the pipeline.

---

## 1. Transisi Arsitektur dan Skalabilitas Terdistribusi
_Projects: Celestia, Arweave/AO — ref `docs/Patterns/`, `docs/Innovation/CategoryCreator.md`_

Evolusi arsitektur terdesentralisasi bergeser dari paradigma monolitik menuju modularitas, di mana
kegunaan spesifik dipisahkan untuk mengoptimalkan efisiensi sistemik.

- **Celestia** memelopori pemisahan lapisan ketersediaan data dari eksekusi transaksi. Dengan pengodean
  penghapusan Reed-Solomon 2D, blok didekonstruksi menjadi matriks *k × k* dan diperluas menjadi *2k × 2k*,
  memungkinkan verifikasi probabilistik melalui Data Availability Sampling:

  > **P(deteksi) = 1 − (1 − e/N)ˢ**
  >
  > di mana **N** = total bagian data, **e** = bagian data yang disembunyikan operator jahat,
  > **s** = jumlah sampling acak. Integritas blok dapat dikonfirmasi dengan sumber daya komputasi sangat rendah.

- **Arweave/AO** mengambil jalur komplementer: memperlakukan penyimpanan permanen sebagai log transaksi
  deterministik, sehingga AO menjalankan Actor Model yang memproses pesan secara paralel tanpa konsensus
  global untuk setiap langkah komputasi.

**Learning:** skalabilitas dapat dicapai melalui minimalisasi data blok terverifikasi (Celestia) maupun
pemisahan total eksekusi dari konsensus penyimpanan (Arweave/AO).

## 2. Penyederhanaan Tokenomics dan Kelangsungan Hidup Jaringan
_Projects: Helium, Synthetix — ref `docs/Ontology/Tokenomics.md`, `docs/Patterns/Failure.md`, `docs/Patterns/Recovery.md`_

Desain ekonomi yang terlalu kompleks sering menghasilkan beban kognitif tinggi dan ketidakstabilan sistemik.

- **Helium** meluncurkan L1 mandiri, lalu bermigrasi ke Solana (April 2023) — menghentikan operasional
  **3.700 validator fisik** dan mengalihkan biaya emisi **6,85% HNT** ke pool subDAO. Kompleksitas tiga token
  (HNT, IOT, MOBILE) mendistorsi insentif tata kelola. Melalui **HIP-138 (2025)** dilakukan simplifikasi radikal:
  emisi IOT & MOBILE dihentikan, seluruh imbalan dikembalikan ke **HNT tunggal**, dan **18,2 miliar MOBILE** dibakar.

- **Synthetix** berevolusi dari Havven; ketergantungan pada inflasi SNX untuk menyokong sUSD ditinggalkan.
  Pada V3 beralih ke kolateral multi-aset matang (wstETH, sUSDe) dan mengajukan pensiun total sUSD demi
  memitigasi risiko depeg struktural.

**Learning:** penyederhanaan tokenomics ke aset tunggal yang kokoh atau kolateral produktif berisiko rendah
adalah titik akhir evolusi bagi proyek yang bertahan melewati beberapa siklus pasar.

## 3. Konvergensi Konsensus Sosial dan Kriptografi
_Project: EigenLayer — ref `docs/Ontology/Security.md`, `docs/Ontology/Governance.md`, `docs/Reasoning/Confidence.md`_

Kesalahan **objektif** (mis. *double-signing*) dapat dibuktikan matematis on-chain. Kesalahan
**subjektif-bersama** (*intersubjective faults* — manipulasi oracle, sensor transaksi sequencer) tidak dapat
dideteksi sepihak oleh smart contract.

EigenLayer menyelesaikannya dengan arsitektur **dual-token**: **bEIGEN** (representasi ter-stake) tunduk pada
**slashing-by-forking** — jika terjadi pelanggaran subjektif, penantang membakar EIGEN untuk membuat garpu token
baru, lalu konsensus sosial menentukan cabang mana yang memiliki nilai ekonomi riil.

**Learning:** keamanan web3 masa depan tidak lagi bergantung sepenuhnya pada pembuktian kriptografi murni,
melainkan pada jalinan dinamis antara hukum kriptoekonomi dan koordinasi sosial manusia.

---

## Referenced by
- Source studies: `examples/Pioneer/*.md`
- Dataset record: `examples/DatasetIndex.md`
- Bibliography: see *Karya yang Dikutip* in `examples/DatasetIndex.md`
