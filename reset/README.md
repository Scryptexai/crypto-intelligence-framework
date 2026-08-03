# reset/ — CIF Deep Reset (multi-phase DeepSeek pipeline)

Modul modular untuk **reset ulang riset** setiap project di `data_project/`
menggunakan API DeepSeek (Anthropic-compatible), fase demi fase, dengan
konteks fase sebelumnya, lalu meng-index semuanya ke Supabase.

## Isi folder

```
reset/
├── projects.txt              # daftar project (1 per baris) — dibaca urut
├── prompts/                  # 11 prompt phase Track C (DeepSeek, "fixed" version)
│   ├── 01-foundation.txt     # Phase 1 — agent riset info project dulu, isi template
│   ├── 02-entity.txt         # Phase 2 — menerima output Phase 1 sbg konteks
│   ├── 03-history.txt        # ... dan seterusnya, konteks = output phase sebelumnya
│   ├── ... 
│   └── 11-conflict.txt       # Phase 11 — Validation & QA (disimpan sbg 11-conflict.docx)
├── reset_run.py              # runner (Python stdlib, tanpa dependency tambahan)
├── state/                    # (auto) state per project → resume aman
└── logs/reset.log            # (auto) log seluruh run
```

Prompt diambil dari `docs/Protocol/Phased-Research-Prompts.md` (bagian **Track C —
DeepSeek Methodology**, versi "Fixed vs. the original DeepSeek run"). Phase 1
ditambahkan instruksi **Langkah 0 — Riset Awal**: agent mencari info project
(deskripsi ringkas, kategori, founding entity, founders, tanggal) sebelum
mengisi template. Fase 2–11 otomatis diberi **output fase sebelumnya** sebagai
konteks oleh runner.

## Alur per project

```
1. Baca prompt phase 1 (project name disisipkan) → panggil API → simpan
   data_project/<Project>/01-foundation.docx
2. Phase 2: prompt phase 2 + output phase 1 sbg konteks → API → 02-entity.docx
3. ... lanjut sampai 11-conflict.docx
4. Jeda 1 menit antar phase, 5 menit antar project → project berikutnya
```

Runner **resume** otomatis: fase yang sudah ada (ukuran >200B) dilewati.
Aman dijalankan ulang (mis. sekali per 24 jam lewat cron) — hanya fase kosong
yang dikerjakan.

## Cara pakai

```bash
# 1. Set kredensial (wajib)
export ANTHROPIC_BASE_URL="https://api.hcnsec.cn/"
export ANTHROPIC_AUTH_TOKEN="sk-..."
export ANTHROPIC_MODEL=DeepSeek-V4-Pro

# 2. Uji coba (dry-run — tanpa memanggil API)
./run.sh reset --dry-run

# 3. Jalankan satu project dulu
./run.sh reset --once --projects Aptos

# 4. Jalankan SEMUA project (urut, resume, jeda 1m/5m)
./run.sh reset

# 5. Reset + index ke Supabase (ingest → build → extract → sync)
./run.sh reset-sync
# atau bertahap:
./run.sh all        # ingest data_project + build + extract
./run.sh sync       # push poc/*.json ke Supabase (butuh SUPABASE_URL + SUPABASE_SERVICE_ROLE_KEY)
```

## Opsi reset_run.py

| Opsi | Fungsi |
|---|---|
| `--projects a,b,c` | batasi ke project tertentu |
| `--phases 1-11` / `1,3,5` | batasi rentang fase |
| `--force` | jalankan ulang fase yang sudah ada |
| `--dry-run` | tampilkan rencana, tanpa API |
| `--once` | berhenti setelah project pertama |
| `--parallel N` | N project berjalan bersamaan (hati-hati rate limit) |
| `--phase-gap N` | jeda antar fase (detik, default 60) |
| `--project-gap N` | jeda antar project (detik, default 300) |
| `--max-tokens N` | batas token output (default 32000) |

## Env yang dibutuhkan

| Variable | Contoh |
|---|---|
| `ANTHROPIC_BASE_URL` | `https://api.hcnsec.cn/` |
| `ANTHROPIC_AUTH_TOKEN` | `sk-...` |
| `ANTHROPIC_MODEL` | `DeepSeek-V4-Pro` |
| `SUPABASE_URL` | (hanya utk sync) |
| `SUPABASE_SERVICE_ROLE_KEY` | (hanya utk sync) |

## Cron sekali / 24 jam (opsional, di VPS)

```cron
# jalankan reset + index tiap hari 02:00 WIB
0 2 * * *  cd /path/crypto-intelligence-framework && \
           export ANTHROPIC_BASE_URL=... ANTHROPIC_AUTH_TOKEN=... ANTHROPIC_MODEL=DeepSeek-V4-Pro && \
           ./run.sh reset-sync >> reset/logs/cron.log 2>&1
```

> ⚠️ **Rate limit:** beri jeda cukup. `--parallel` hanya jika proxy API Anda
> menoleransi banyak request bersamaan. Fase per project TIDAK boleh paralel
> (fase N butuh output fase N-1 sebagai konteks).
