# Latihan Bab 3: PHP

## Soal 1: Kalkulator Sederhana
Buat form HTML + PHP (`kalkulator.php`) yang:
1. Menerima 2 angka dari input user
2. Dropdown pilih operator: tambah, kurang, kali, bagi
3. Tampilkan hasil perhitungan di halaman yang sama
4. Validasi: input tidak boleh kosong

## Soal 2: Aplikasi To-Do List (Array)
Buat `todo.php` yang:
1. Menyimpan daftar tugas dalam array PHP
2. Menampilkan semua tugas dalam list HTML
3. Form untuk menambah tugas baru (via POST)
4. Tugas yang sudah selesai bisa ditandai (checkbox)

## Soal 3: Halaman Login Sederhana
Buat sistem login sederhana:
1. `login.php` — Form input username & password
2. `proses_login.php` — Validasi (hardcode username: "admin", password: "12345")
3. `dashboard.php` — Halaman yang hanya bisa diakses setelah login (pakai session)
4. `logout.php` — Hapus session, redirect ke login

## Soal 4: Buku Tamu dengan File
Buat aplikasi buku tamu (`bukutamu.php`) yang:
1. Form input: nama, email, pesan
2. Data disimpan ke file `.txt` (karena belum pakai database)
3. Tampilkan semua entri buku tamu di bawah form
4. Urutkan dari yang terbaru

## Soal 5: Include & Template
Buat website multi-halaman dengan template:
1. `header.php` — Berisi doctype, head, dan navigasi
2. `footer.php` — Berisi copyright dan penutup body/html
3. `home.php`, `tentang.php`, `kontak.php` — Masing-masing include header & footer
4. Navigasi aktif: link halaman saat ini diberi style berbeda
