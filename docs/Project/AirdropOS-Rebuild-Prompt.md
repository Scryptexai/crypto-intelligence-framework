# AirdropOS → CIF Rebuild Prompt (paste-ready)

## Status

Paste-ready prompt for the session that will actually build/upgrade/rebrand `Scryptexai/AirdropOS` into CIF
— written to be self-contained (a fresh session has no memory of the `crypto-intelligence-framework`
discussion that produced it) and strictly derived from two locked documents, not a new set of decisions.
Written 2026-07-26, source: `docs/Project/ApplicationBlueprint.md` (v2) +
`docs/Project/AirdropOS-UI-Audit.md`.

**Why this exists as its own file, separate from the two source docs:** those two are reference/reasoning
documents (why each decision was made) — dense, cross-referenced, meant to be read slowly. A build session
needs a single, front-loaded instruction it can act on immediately, with the reference docs cited for depth
on demand rather than required reading before the first action. Keep this file's content in sync if either
source doc changes — it's a derived summary, not an independent decision.

## How to use

Paste the fenced prompt below as the first message to the session (Claude Code, or whatever "Claude Design"
resolves to) once that session has `Scryptexai/AirdropOS` (write access) and, ideally,
`Scryptexai/crypto-intelligence-framework` (read access, for the two source docs and `poc/cif.json`) both
available. If only AirdropOS is available, paste `ApplicationBlueprint.md` and `AirdropOS-UI-Audit.md` as
attachments alongside this prompt — the prompt references them by path and assumes they're reachable.

```
Kamu akan membangun ulang, meng-upgrade, dan me-rebranding AirdropOS (repo yang sedang kamu buka sekarang)
menjadi CIF — sebuah aplikasi crypto intelligence untuk web3 researcher/analyst/fund yang melakukan
due-diligence pre-TGE, BUKAN lagi app tracker airdrop untuk hunter casual.

SEBELUM MENGUBAH APAPUN, baca 3 dokumen ini secara penuh — ini adalah rencana yang sudah dikunci
(maintainer decision), bukan draf yang perlu kamu simpulkan ulang dari nol:
1. docs/Project/ApplicationBlueprint.md (v2) — dari repo crypto-intelligence-framework. Ini spesifikasi
   produk: positioning, trust architecture (§3, non-negotiable), monetisasi (§9), dan arsitektur informasi
   v2 (§2b, §11) yang baru saja diperluas dari cakupan lama "cuma pattern-matching" ke 7 use case baru.
2. docs/Project/AirdropOS-UI-Audit.md — audit kode AirdropOS SAAT INI terhadap blueprint di atas, dengan
   temuan konkret dan urutan prioritas perbaikan.
3. poc/cif.json (schema cif-export/1) — dari repo crypto-intelligence-framework. Ini bentuk data ASLI yang
   akan kamu render. PENTING: saat ini isinya cuma 1 project (LayerZero) — dataset masih di tahap awal
   reset (proyek lama diarsipkan demi rigor yang lebih tinggi), jadi desain HARUS tetap terlihat kredibel
   dan bernilai dengan dataset kecil, bukan cuma bagus kalau sudah ada ratusan project.

ATURAN NON-NEGOTIABLE (dari ApplicationBlueprint §3 dan §7 — JANGAN dilanggar demi kemudahan desain):
- Setiap klaim/angka/pattern yang tampil WAJIB bisa di-klik satu kali untuk expand ke kutipan mentah
  sumbernya. Tidak ada klaim tanpa jalur ke sitasi.
- Evidence Level (fakta) dan Pattern-level confidence (instance count + kecocokan era/scope) adalah DUA
  angka berbeda — jangan pernah digabung jadi satu.
- Tidak pernah memfrasakan hasil sebagai prediksi sukses/gagal biner. Selalu: Current Read (Pattern
  Confidence + Trajectory Probability, dua angka terpisah, dilabeli jelas) + Signal being watched opsional
  (kondisi spesifik yang bisa dicek, jendela waktu, dicatat ke Track Record apapun hasilnya).
- Trust-depth (rantai sitasi, evidence badge) TIDAK PERNAH di-gate untuk upsell. Yang di-gate cuma scope
  (berapa banyak laporan penuh bisa dibuka) dan continuity — bukan kedalaman bukti itu sendiri.
- Fitur Content Studio (lihat di bawah) menghasilkan konten dari data dossier CIF yang sudah tersitasi —
  BUKAN dari riset yang di-generate bebas tanpa sumber. Setiap template yang dihasilkan tetap membawa
  jejak sitasinya, sama seperti laporan diligence.

URUTAN PRIORITAS KERJA (dari AirdropOS-UI-Audit.md, JANGAN dikerjakan acak):
1. Bersihkan drift dokumentasi — docs/UX_FRAMEWORK.md, design_guidelines.json, memory/PRD.md di repo ini
   menggambarkan 3 produk yang saling bertentangan dan SEMUANYA sudah usang (predates CIF pivot). Tandai
   sebagai historis (jangan dihapus tanpa alasan jelas — cukup beri catatan "SUPERSEDED, lihat
   ApplicationBlueprint.md") sebelum mulai desain, supaya tidak ada asumsi lama yang diam-diam terbawa.
2. Putuskan secara eksplisit route mana yang publik (tidak perlu login) vs. perlu akun — sekarang SEMUA
   route di App.js ada di belakang ProtectedRoute, termasuk yang seharusnya bisa diakses siapa saja
   (Opportunity Ranking browsing gratis, halaman Track Record). Ini prasyarat sebelum langkah 3.
3. Bangun halaman Track Record publik (ApplicationBlueprint §3.3) — saat ini belum ada sama sekali, padahal
   ini sinyal trust paling penting yang dimiliki CIF (bukti sistem pernah benar di kasus yang tidak dipakai
   membangun pattern-nya). Sumber data: poc/benchmarks.json dari repo crypto-intelligence-framework.
4. Kerjakan rebranding — ganti semua "AirdropOS"/"airdrop hunter os" (header, tagline, <title> yang saat
   ini masih scaffold default "Emergent | Fullstack App", copy lain) menjadi identitas CIF. Ini permintaan
   eksplisit maintainer dan juga yang paling cepat dikerjakan.
5. Bersihkan kode mati dari arsitektur research_reports/deep-research/research-project lama — SATUKAN
   dengan pembangunan Supabase sync (poin di bawah), jangan dikerjakan terpisah, karena sync yang baru
   menggantikan fungsinya di commit yang sama.
6. Rapikan tabrakan istilah "confidence"/"research" yang dipakai untuk hal berbeda di luar halaman
   Intelligence (mis. RESEARCH_PROMPT_TEMPLATE di Guide.jsx itu untuk konten sosmed, BUKAN riset dossier
   CIF — beri nama yang jelas beda).

KEPUTUSAN ARSITEKTUR YANG PERLU DIPUTUSKAN DI AWAL (ApplicationBlueprint §11.1 — rekomendasi kuat, BUKAN
keputusan final, konfirmasi ke maintainer kalau ragu):
- Bottom-nav mobile 5-slot yang ada sekarang kemungkinan besar SALAH BENTUK untuk produk ini. Itu warisan
  dari app tracker airdrop personal (user membuka HP tiap hari cek reminder), sementara user CIF yang
  sesungguhnya (researcher/analyst/fund) memakai tool desktop-first, dense, multi-panel (persis seperti
  Messari/Delphi/Nansen yang sudah mereka bayar). REKOMENDASI: bangun Intelligence core sebagai dashboard
  desktop-first, dengan versi mobile companion yang lebih ringan untuk lookup cepat — bukan sebaliknya.

STRUKTUR MENU TARGET (ApplicationBlueprint §11.2 — level produk, bukan spek piksel):
- **Intelligence** (inti, sudah ada, DIPERLUAS) — search/browse katalog, Opportunity Ranking, Today's Pick,
  laporan penuh dengan rantai trust §3. Semua tool baru dari §2b (export memo due-diligence, entity graph
  explorer, pencarian rekam jejak founder/tim, red-flag scanner, perbandingan analog historis) masuk
  SEBAGAI FITUR DI DALAM Intelligence — bukan tab terpisah, karena semuanya facet dari "mendiligensi satu
  project atau membandingkan beberapa."
- **Track Record** (belum ada — bangun, lihat prioritas #3) — publik, tidak di belakang login.
- **Content Studio** (BANGUN ULANG dari "Sesi" yang ada sekarang — JANGAN DIHAPUS) — masih dipakai untuk
  kebutuhan yapping/promosi CIF sendiri. Sekarang di-ground ulang di data dossier CIF yang sudah tersitasi
  (bukan dokumen yang di-paste user tanpa verifikasi seperti alur lama) — AI agent membaca fakta terstruktur
  dari dossier lalu menyusun template konten (thread, penjelasan, skrip grafis timeline), TETAP membawa
  jejak sitasi ke sumbernya masing-masing.
- **Portfolio** (BANGUN ULANG dari "Porto" yang ada sekarang — JANGAN DIHAPUS) — bukan cuma daftar
  kepemilikan, tapi diikat ke riwayat Current Read/Signal milik CIF sendiri untuk project yang sama, supaya
  portfolio user jadi instance personal dari mekanisme Track Record publik.
- **Account/Settings** — tidak berubah secara fungsi, cuma rebranding.

APA YANG JANGAN DILAKUKAN (ApplicationBlueprint §7 + §11.3, non-goals):
- Jangan menghapus fitur Sesi/Content atau Porto/Portfolio — bangun ulang, bukan buang.
- Jangan biarkan Content Studio menghasilkan konten tanpa jejak sitasi — itu melanggar prinsip inti CIF.
- Jangan biarkan flow identifikasi project jadi wizard klasifikasi LLM per-user sebagai jalur utama —
  tetap search-first di atas katalog yang sudah dikurasi (ApplicationBlueprint §4); LLM-tagging cuma
  fallback untuk project yang belum tercakup.
- Jangan gate rantai sitasi/evidence badge di balik paywall — yang di-gate cuma scope & continuity.

Kalau ada keputusan yang tidak eksplisit disebut di ApplicationBlueprint.md/audit dan kamu perlu
menyimpulkan sendiri, tandai jelas sebagai asumsi (bukan diam-diam diputuskan) supaya maintainer bisa
koreksi sebelum ini jadi kebiasaan yang sulit diubah nanti.
```

## Related Files

`docs/Project/ApplicationBlueprint.md` (v2 — the actual spec this prompt summarizes), `docs/Project/
AirdropOS-UI-Audit.md` (the audit this prompt's priority order is drawn from), `poc/cif.json`
(the real data shape), `poc/benchmarks.json` (Track Record data source).
