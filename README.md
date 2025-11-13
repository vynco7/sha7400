# sha7400


<!-- README HTML for SHA-super-7400 -->
<!doctype html>
<html lang="id">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>SHA-super-7400 — README</title>
  <style>
    body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial; line-height:1.6; color:#0b0f16; padding:24px; background:#fafbfc; }
    .container { max-width:900px; margin:0 auto; background:#fff; border-radius:10px; padding:28px; box-shadow:0 6px 30px rgba(16,24,40,0.06); }
    h1 { font-size:28px; margin-bottom:6px; }
    .meta { color:#475569; margin-bottom:18px; }
    .badges img { height:20px; margin-right:8px; vertical-align:middle; }
    pre { background:#0b1220; color:#dbeafe; padding:12px; border-radius:8px; overflow:auto; font-size:13px; }
    code { background:#f1f5f9; padding:2px 6px; border-radius:6px; }
    .section { margin-top:20px; }
    table { border-collapse:collapse; width:100%; margin:12px 0; }
    th, td { border:1px solid #e6eef6; padding:10px; text-align:left; }
    th { background:#f1f5f9; }
    .cta { display:inline-block; background:#0b5fff; color:white; padding:10px 14px; border-radius:8px; text-decoration:none; margin-top:12px; }
    .note { background:#fff7ed; border-left:4px solid #f59e0b; padding:10px; border-radius:6px; color:#92400e; margin:12px 0; }
    .danger { background:#fff1f2; border-left:4px solid #ef4444; padding:10px; border-radius:6px; color:#9f1239; margin:12px 0; }
    ul { margin-left:18px; }
    .kbi { font-weight:600; color:#0b1220; }
  </style>
</head>
<body>
  <div class="container">
    <header>
      <h1>🔐 SHA‑super‑7400</h1>
      <p class="meta">Implementasi hash eksperimental terinspirasi SHA‑256 dengan output diperpanjang menjadi <strong>7.400 bit</strong> (~925 byte) dan mendukung 1.000 parameter input untuk penelitian dan pembelajaran kriptografi.</p>
      <div class="badges">
        <img alt="python" src="https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white">
        <img alt="license" src="https://img.shields.io/badge/License-MIT-green">
        <img alt="status" src="https://img.shields.io/badge/Experimental-Do%20Not%20Use-red">
      </div>
    </header>

    <div class="section">
      <h2>Ringkasan</h2>
      <p><strong>SHA‑super‑7400</strong> adalah prototipe hash panjang berbasis ide SHA‑256, dibuat untuk:</p>
      <ul>
        <li>Eksperimen output panjang (XOF‑like)</li>
        <li>Belajar dan memahami mekanisme hash</li>
        <li>Menguji pengaruh parameter tambahan (1000 input literal)</li>
      </ul>
      <div class="note">
        <strong>Catatan:</strong> Tidak direkomendasikan untuk proteksi data sensitif, password, atau kunci kriptografi nyata.
      </div>
    </div>

    <div class="section">
      <h2>Fitur Utama</h2>
      <ul>
        <li>Output panjang: <strong>7.400 bit</strong> (~925 byte / 1.850 karakter hex).</li>
        <li>Memanfaatkan <strong>1.000 parameter input</strong> yang memengaruhi proses hashing.</li>
        <li>Konstanta <strong>K</strong> yang dapat dimodifikasi untuk eksperimen.</li>
        <li>Fungsi modular: ROTR, SHR, Ch, Maj, Σ, σ tersedia untuk eksplorasi.</li>
        <li>Python murni, mudah dibaca dan dimodifikasi.</li>
      </ul>
    </div>

    <div class="section">
      <h2>Instalasi & Persyaratan</h2>
      <pre><code># clone repo
git clone https://github.com/&lt;username&gt;/sha-super-7400.git
cd sha-super-7400

# jalankan contoh
python3 sha7400.py
      </code></pre>
    </div>

    <div class="section">
      <h2>Contoh Penggunaan</h2>
      <p>Input pesan bebas, output hash 7.400 bit dihasilkan:</p>
      <pre><code>Masukkan pesan: contoh_input
SHA-super-7400 (hex, first 7400 chars): 2fd272fc52627aeb2b79...
Total hex length: 1850
Panjang hash (bytes): 925
Panjang hash (bits): 7400
Elapsed: 5.328s
      </code></pre>
      <p><strong>Opsional:</strong> Simpan output hex ke file <code>super7400.hex</code>.</p>
    </div>

    <div class="section">
      <h2>Desain & Arsitektur</h2>
      <ol>
        <li><strong>Input:</strong> pesan (bytes) + 1000 parameter (list literal/file).</li>
        <li><strong>Core:</strong> Fungsi SHA-like (ROTR/SHR, Ch/Maj, big/small sigma) diperluas untuk menerima input parameter.</li>
        <li><strong>Compression:</strong> 64 ronde per blok, konstanta <code>K</code> dan W[0..63] dimodifikasi.</li>
        <li><strong>Output Extension:</strong> Core dipanggil berulang hingga menghasilkan 925 byte.</li>
      </ol>
    </div>

    <div class="section">
      <h2>Perbandingan: SHA‑256 vs SHA‑super‑7400</h2>
      <table>
        <thead><tr><th>Aspek</th><th>SHA‑256</th><th>SHA‑super‑7400</th></tr></thead>
        <tbody>
          <tr><td>Output</td><td>256 bit</td><td>7.400 bit (~925 byte)</td></tr>
          <tr><td>Parameter input</td><td>—</td><td>1.000 parameter literal</td></tr>
          <tr><td>Ronde</td><td>64</td><td>64 per block, modifikasi fungsi internal</td></tr>
          <tr><td>Tujuan</td><td>Standar kriptografi</td><td>Eksperimen / pendidikan</td></tr>
          <tr><td>Keamanan</td><td>Peer-reviewed</td><td>Tidak diaudit — jangan gunakan produksi</td></tr>
        </tbody>
      </table>
    </div>

    <div class="section">
      <h2>Contoh Integrasi Input & Params</h2>
      <pre><code># baca params dari file
params1000 = [line.strip() for line in open('params.txt','r',encoding='utf-8')]

# input pesan dari user
msg = input("Masukkan pesan: ").encode('utf-8')

# panggil generator XOF-like
long_hash = sha_super7400(msg, params1000)

# simpan hasil hex
open('super7400.hex','w').write(long_hash.hex())
      </code></pre>
    </div>

    <div class="section">
      <h2>FAQ</h2>
      <p><strong>Q:</strong> Aman untuk password/kunci?</p>
      <p><strong>A:</strong> <span class="kbi">Tidak</span>. Gunakan SHA‑3, Argon2, bcrypt atau HMAC untuk keamanan nyata.</p>

      <p><strong>Q:</strong> Apakah output 7.400 karakter?</p>
      <p><strong>A:</strong> Bukan, output 7.400 <em>bit</em> (925 byte). Hex-nya 1.850 karakter.</p>

      <p><strong>Q:</strong> Bisa dibalik (reverse) untuk menemukan input?</p>
      <p><strong>A:</strong> Tidak. Brute-force praktis tidak mungkin karena ruang output sangat besar.</p>
    </div>

    <div class="section">
      <h2>Tips GitHub & Publikasi</h2>
      <ul>
        <li>Judul repo jelas: <code>sha-super-7400</code></li>
        <li>Sertakan demo, screenshot, atau GIF generator.</li>
        <li>Gunakan topics: <code>cryptography</code>, <code>hash</code>, <code>python</code>, <code>experimental</code>, <code>xof</code></li>
        <li>Commit message deskriptif & buat CHANGELOG.md.</li>
        <li>Buat CONTRIBUTING.md & issue template untuk kontribusi.</li>
      </ul>
      <a class="cta" href="https://github.com/&lt;username&gt;/sha-super-7400">Fork & Contribute →</a>
    </div>

    <div class="section">
      <h2>Lisensi</h2>
      <p>MIT License — bebas dipakai & dimodifikasi, dengan catatan ini eksperimen, jangan gunakan di produksi kritikal.</p>
    </div>

    <div class="section">
      <h2>Kontribusi & Kontak</h2>
      <p>Fork repo dan kirim pull request untuk eksperimen kriptografi. Diskusi desain & audit melalui GitHub Issues.</p>
    </div>

    <footer style="margin-top:22px; color:#475569;">
      <small>Created with ❤️ — Eksperimen kriptografi. Jangan gunakan pada data sensitif tanpa audit. © 2025</small>
    </footer>
  </div>
</body>
</html>
