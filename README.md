Markdown

# 🔐 SHA‑super‑7400

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Experimental-Do%20Not%20Use-red)

Implementasi hash eksperimental yang terinspirasi oleh SHA‑256 dengan output diperpanjang menjadi **7.400 bit** (~925 byte) dan mendukung **1.000 parameter input** literal untuk keperluan penelitian dan pembelajaran kriptografi.

---

## 📝 Ringkasan

**SHA‑super‑7400** adalah prototipe hash panjang berbasis logika SHA‑256 yang dimodifikasi. Proyek ini dibuat untuk:
* Eksperimen dengan output hash yang sangat panjang (XOF-like).
* Mempelajari mekanisme internal fungsi hash (ROTR, Sigma, Padding).
* Menguji pengaruh avalanche effect dari 1.000 parameter input tambahan.

> [!WARNING]
> **PENTING:** Algoritma ini adalah **eksperimen pendidikan**. Tidak diaudit oleh kriptografer profesional. **JANGAN** digunakan untuk mengamankan password, transaksi keuangan, atau data sensitif di lingkungan produksi.

---

## ✨ Fitur Utama

* **Output Masif:** Menghasilkan digest 7.400 bit (1.850 karakter Hexadecimal).
* **1.000 Parameter:** Menggunakan array `params` berisi 1.000 string literal yang mempengaruhi hasil hash secara unik.
* **Pure Python:** Ditulis menggunakan pustaka standar `struct` tanpa dependensi eksternal.
* **Modular:** Fungsi inti (Ch, Maj, Σ, σ) ditulis manual untuk transparansi logika.

---

## 🚀 Instalasi & Penggunaan

### 1. Clone Repository
```bash
git clone [https://github.com/username-anda/sha-super-7400.git](https://github.com/username-anda/sha-super-7400.git)
cd sha-super-7400

2. Menjalankan Script

Pastikan Anda sudah mengedit bagian msg atau params di dalam script sesuai kebutuhan, lalu jalankan:
Bash

python3 manual_sha7400_1000_params.py

3. Contoh Output

Plaintext

--- SHA SUPER 7400 ---
Masukkan pesan yang ingin di-hash: rahasia_negara

=== HASIL ===
Pesan asli: rahasia_negara
SHA-super-7400 (hex, first 100 chars): 8a2f... (dipotong)
Total hex length: 1850
Panjang hash (bytes): 925
Panjang hash (bits): 7400
Elapsed: 0.045s

🏗️ Desain & Arsitektur

    Input: Menerima pesan (bytes) + List 1.000 parameter string.

    Core Engine: Menggunakan struktur dasar SHA-256 (64 ronde) namun dimodifikasi untuk menerima injeksi parameter eksternal.

    Compression: Melakukan operasi bitwise (XOR, AND, ROTR) terhadap state internal.

    Extension: Loop eksekusi dilakukan berulang kali untuk memperpanjang output hingga mencapai target 925 byte.

📊 Perbandingan: SHA‑256 vs SHA‑super‑7400

Aspek	SHA‑256	SHA‑super‑7400
Output Size	256 bit (32 byte)	7.400 bit (925 byte)
Input Params	Pesan saja	Pesan + 1.000 Params Literal
Hex Length	64 karakter	1.850 karakter
Tujuan	Standar Keamanan	Eksperimen / Pendidikan
Status	FIPS Standard	Experimental / Unsafe

🔧 Contoh Integrasi Kode

Jika Anda ingin mengimpor fungsi ini ke script lain:
Python

import manual_sha7400_1000_params as hasher

# 1. Definisikan params (atau load dari file)
my_params = ["param_001", "param_002", ... "param_1000"]

# 2. Siapkan pesan dalam bytes
pesan = b"Halo Dunia"

# 3. Generate Hash
hasil = hasher.sha_super7400(pesan, my_params)

# 4. Simpan ke file
with open("hash_result.txt", "w") as f:
    f.write(hasil.hex())

❓ FAQ

Q: Bisakah saya menggunakan ini untuk hashing password user? A: Tidak. Gunakan standar industri seperti Argon2, bcrypt, atau SHA-256 + Salt. Algoritma ini belum teruji ketahanannya terhadap serangan kolisi (collision attack).

Q: Mengapa outputnya sangat panjang? A: Ini disengaja untuk mempelajari perilaku fungsi hash ketika dipaksa menghasilkan output yang jauh melebihi state internal aslinya (mirip konsep XOF / Extendable-Output Function).

Q: Apakah bisa dibalik (decrypt) untuk melihat pesan asli? A: Secara teori tidak (karena ini fungsi satu arah), namun karena ini algoritma buatan sendiri, mungkin terdapat celah matematika yang belum ditemukan.

🤝 Kontribusi

Kontribusi sangat diterima untuk tujuan pembelajaran!

    Fork repository ini.

    Buat branch fitur baru (git checkout -b fitur-baru).

    Commit perubahan Anda (git commit -m 'Menambah fitur X').

    Push ke branch (git push origin fitur-baru).

    Buat Pull Request.

📄 Lisensi

Didistribusikan di bawah MIT License. Lihat LICENSE untuk informasi lebih lanjut.

<p align="center"> <small>Created with ❤️ — Eksperimen Kriptografi 2025</small> </p>
