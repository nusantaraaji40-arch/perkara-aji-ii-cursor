# Contoh Konektor Cursor — PERKARA AJI II

Contoh pemakaian konektor Cursor (custom.cursor) dari workspace Muse. **Repo ini masih berupa stub** — konektornya belum tersambung, jadi file contoh di sini adalah dokumentasi + kerangka, bukan kode yang sudah bisa jalan. Repo ini bagian dari proyek PERKARA AJI II — agen AI yang membuat video YouTube 8 menit dari foto presenter.

## Isi repo

| File | Konektor | Keterangan |
|---|---|---|
| `cursor_example.py` | custom.cursor (belum ada) | Stub jujur — hanya mencetak status; tidak ada panggilan jaringan |

## Yang dimaksud "Cursor" di sini

API key **Cursor sendiri** (Cloud Agents API v0 di `https://api.cursor.com`, key format `crsr_...`), dibuat di `cursor.com/dashboard` → API Keys. **Bukan** key xAI/Grok yang dipakai di dalam editor Cursor (itu urusan konektor custom.grok).

## Status — jujur (2026-11-07)

**PENDING, belum tersambung.** Folder konektor belum ada, tidak ada helper. Link koneksi sudah dikirim dan belum diisi. Setelah tersambung, file contoh ini harus diganti dengan wrapper nyata seperti `gitlab_example.py` (subprocess ke helper + hanya perintah read-only yang diizinkan default).

## Panggilan pertama setelah tersambung (verifikasi identitas)

```bash
GET https://api.cursor.com/v0/me
```

Auth: HTTP Basic (username = API key, password kosong) atau header `Authorization: Bearer <key>`. Endpoint ini read-only dan gratis (tidak memicu agen). Endpoint lain (Cloud Agents API v0): `GET /v0/agents`, `POST /v0/agents` (meluncurkan agen di repo GitHub), `GET /v0/agents/{id}`, `POST /v0/agents/{id}/followup`.

## Perhatian biaya

Cloud Agents berbayar (token-based consumption pricing). Meluncurkan agen menghabiskan budget akun Cursor. Membaca (`/v0/me`, `GET /v0/agents`) tidak meluncurkan apa pun.

## Tanpa secret

File-file di repo ini **tidak berisi API key, token, atau rahasia apa pun**. Jangan pernah menaruh key di file, di `.env`, atau di commit. Catatan Cursor: mereka tidak menawarkan read-only API key — siapa pun yang memegang key ini bisa meluncurkan cloud agent yang ditagih ke plan kamu.

## Repo terkait (hasil screening)

Repo open source terbaik untuk memakai Cursor API dari code sendiri (bukan bagian repo ini, lisensinya masing-masing):

- **sdk-bridge** — https://github.com/cursor/sdk-bridge — server lokal resmi yang membungkus SDK TypeScript Cursor dan mengekspos agen Cursor lewat protokol Connect/protobuf, lisensi MIT. Satu-satunya jalur resmi agar pipeline Python bisa memerintah agen Cursor tanpa menunggu helper REST.
- **cursor-cli** — https://github.com/pivanov/cursor-cli — REPL terminal untuk agen Cursor di atas `@cursor/sdk`, lisensi MIT. Kecil, berguna sebagai contoh pola pemakaian SDK.

Catatan: repo contoh resmi `cursor/cookbook` tidak punya file LICENSE, jadi tidak di-clone — hanya jadi referensi dokumentasi.

## Lisensi

Code contoh di repo ini berlisensi **MIT** (lihat `LICENSE`). Dependensi/repo terkait di atas punya lisensinya sendiri-sendiri — periksa sebelum memakai.
