#!/usr/bin/env python3
"""STUB — contoh pemakaian konektor Cursor (custom.cursor). BELUM TERSAMBUNG.

STATUS — JUJUR, 2026-11-07: PENDING, BELUM ADA KONEKTOR.
Konektor custom.cursor BELUM dibuat: link koneksi sudah dikirim ke Mas Aji
dan belum diisi. TIDAK ADA helper di
~/workspace/custom-connectors/custom.cursor/bin/ — jangan cari file itu.
File ini adalah stub dokumentasi + kerangka, BUKAN kode yang bisa jalan
sekarang. Jangan menulis key palsu di sini dan jangan pura-pura memanggil
helper yang tidak ada.

YANG DIMAKSUD "CURSOR" DI SINI: API key Cursor SENDIRI (Cloud Agents API v0
di https://api.cursor.com, key format crsr_...), dibuat di
cursor.com/dashboard -> API Keys. BUKAN key xAI/Grok yang dipakai di dalam
editor Cursor (itu urusan konektor custom.grok).

PANGGILAN PERTAMA SETELAH TERSAMBUNG (verifikasi identitas):
    GET https://api.cursor.com/v0/me
    Auth: HTTP Basic, username = API key, password kosong
          (curl -u "$CURSOR_API_KEY:" https://api.cursor.com/v0/me)
    atau header: Authorization: Bearer <key>  (tergantung hasil verifikasi)
    Sukses menjawab info pemilik key. Endpoint ini read-only dan gratis
    (tidak memicu agen).

ENDPOINT LAIN (Cloud Agents API v0, semua memakai auth yang sama):
    GET  /v0/agents            — daftar cloud agent
    POST /v0/agents            — luncurkan agen baru di repo GitHub
                                 (prompt + source.repository + target.autoCreatePr)
    GET  /v0/agents/{id}       — status agen (poll tiap 30-60 detik)
    POST /v0/agents/{id}/followup — kirim instruksi lanjutan

CATATAN BIAYA: Cloud Agents berbayar (token-based consumption pricing).
Meluncurkan agen menghabiskan budget akun Cursor. Endpoint /v0/me dan
GET /v0/agents hanya membaca dan tidak meluncurkan apa pun.

REPO RUJUKAN (sudah di-screening, lihat laporan screening konektor):
    - cursor/sdk-bridge (MIT) — server lokal resmi yang membungkus SDK
      TypeScript dan mengekspos agen Cursor lewat protokol Connect/protobuf,
      sehingga bisa dipakai dari Python tanpa helper REST.
    - pivanov/cursor-cli (MIT) — contoh REPL terminal di atas @cursor/sdk.

SETELAH KONEKTOR TERSAMBUNG: ganti file ini dengan wrapper nyata seperti
gitlab_example.py — subprocess ke helper custom.cursor + hanya perintah
read-only (me, list_agents) yang diizinkan default.

File ini TIDAK berisi API key/token/rahasia apa pun.
"""

import sys

# Stub: tidak ada helper, tidak ada panggilan jaringan.
# Menjalankan file ini hanya mencetak status di atas.


def main() -> int:
    print("Konektor custom.cursor BELUM tersambung (pending, 2026-11-07).")
    print("Tidak ada helper di ~/workspace/custom-connectors/custom.cursor/bin/.")
    print("Panggilan pertama setelah tersambung: GET /v0/me di api.cursor.com")
    print("Lihat docstring file ini untuk detail endpoint dan repo rujukan.")
    return 3


if __name__ == "__main__":
    raise SystemExit(main())
