# Transfer package: refresh snapshot vendored intent (60 dossier)

Isi package ini = commit yang GAGAL push langsung ke `Scryptexai/intent`
karena token sesi Arena di-mint sebelum repo intent ditambahkan ke
instalasi app (403). Package ini memuat hasil yang sudah terverifikasi
(52/52 vitest lulus) agar tidak hilang.

## Cara apply ke repo intent (dari mesin Anda, punya akses push ke intent)

```bash
cd <repo-intent>
git fetch https://github.com/Scryptexai/crypto-intelligence-framework.git \
      arena/019fec85-crypto-intelligence-framework
git checkout arena/019febd8-intent
git checkout FETCH_HEAD -- .arena-intent-transfer
cp .arena-intent-transfer/src-data-cif/*.json src/data/cif/
cp .arena-intent-transfer/cif-loader.test.ts src/services/cif-loader.test.ts
cp .arena-intent-transfer/simulator.test.ts src/services/simulator.test.ts
rm -rf .arena-intent-transfer
npm install && npm test     # harus 52/52
git add -A && git commit -m "feat(data): refresh vendored CIF snapshot to 60 dossiers + airdrop layer"
git push origin arena/019febd8-intent
```

Alternatif: buka SESI ARENA BARU setelah repo intent masuk instalasi app —
saya bisa push langsung dari sana (token baru melihat repo baru).

## Isi snapshot

- cif.json/projects.json: 60 dossier deep (kategori/era lengkap)
- entities/events/decision_events/knowledge/behavior: ekstraksi penuh 60 dossier
- qa.json: 59 CIF Validation Reports
- conflicts.json: 17 konflik two-source / 11 proyek
- airdrop.json BARU: 60 profil Phase-12 (status, events, 8-POV, 4 titik harga tersitasi)
- 2 test diupdate (27->60; variabel simulator 5->6, fix kegagalan pre-existing 8ee86c4)
