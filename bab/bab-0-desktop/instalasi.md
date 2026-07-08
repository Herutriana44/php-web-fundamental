# Bab 0: Instalasi & Persiapan Environment

XAMPP adalah paket perangkat lunak bebas yang menyediakan lingkungan pengembangan web lokal (Apache, MySQL, PHP, phpMyAdmin).

## Komponen XAMPP
- **Apache** — Web server untuk menjalankan file PHP
- **MySQL / MariaDB** — Database server
- **PHP** — Bahasa pemrograman server-side
- **phpMyAdmin** — GUI untuk mengelola database MySQL

## Langkah Instalasi (Windows)
1. Unduh XAMPP dari [apachefriends.org](https://www.apachefriends.org/)
2. Jalankan installer, pilih komponen: Apache, MySQL, PHP, phpMyAdmin
3. Pilih folder instalasi (default: `C:\xampp`)
4. Setelah selesai, buka **XAMPP Control Panel**
5. Klik **Start** pada Apache dan MySQL
6. Buka browser, akses `http://localhost` — jika muncul halaman XAMPP, instalasi berhasil

## Struktur Folder Penting
- `C:\xampp\htdocs\` — Tempat menyimpan semua file project web
- `C:\xampp\mysql\data\` — Tempat data database disimpan

## Alternatif Lain
- **Laragon** — Lebih ringan, cocok untuk Windows
- **MAMP** — Untuk macOS
- **LAMP** — Untuk Linux (Apache, MySQL, PHP)

## Verifikasi Instalasi
Buat file `info.php` di dalam `htdocs/`:
```php
<?php
phpinfo();
?>
```
Akses `http://localhost/info.php` — jika muncul tabel informasi PHP, server siap digunakan.

## Troubleshooting: Masalah Umum & Solusi

### Apache tidak bisa start
- **Gejala**: Tombol "Start" Apache tidak aktif atau error "Port 80 already in use"
- **Solusi**: 
  1. Cek apakah port 80 sudah digunakan (buka cmd: `netstat -ano | findstr :80`)
  2. Matikan aplikasi yang menggunakan port 80 (Skype, IIS, Web server lain)
  3. Atau ubah port Apache di `C:\xampp\apache\conf\httpd.conf` (cari `Listen 80`)

### MySQL tidak bisa start
- **Gejala**: MySQL tidak mau start, atau error "Cannot start MySQL" saat restart
- **Solusi**:
  1. Cek port 3306 (default MySQL): `netstat -ano | findstr :3306`
  2. Hapus file `ibdata1` di `C:\xampp\mysql\data\` jika corrupted
  3. Reinstall MySQL atau gunakan MariaDB sebagai alternatif

### `http://localhost` menampilkan error 404
- **Gejala**: Browser menampilkan "Not Found" atau halaman kosong
- **Solusi**:
  1. Pastikan Apache berstatus "Running" (warna hijau di XAMPP Control Panel)
  2. Buka file `C:\xampp\apache\conf\httpd.conf`, cari `DocumentRoot "C:/xampp/htdocs"`
  3. Pastikan folder `htdocs` ada dan tidak kosong

### phpMyAdmin tidak bisa diakses
- **Gejala**: `http://localhost/phpmyadmin` error 404 atau error koneksi database
- **Solusi**:
  1. Pastikan MySQL sudah running
  2. Cek konfigurasi di `C:\xampp\phpmyadmin\config.inc.php`
  3. Restart MySQL dan Apache

### File PHP ditampilkan sebagai teks biasa
- **Gejala**: Browser menampilkan kode PHP alih-alih output HTML
- **Solusi**:
  1. File harus disimpan di dalam `htdocs` atau subfolder `htdocs`
  2. Akses via `http://localhost/namafile.php`, bukan file:///C:/xampp/...
  3. Pastikan ekstensi file adalah `.php`, bukan `.txt` atau lainnya

## FAQ (Pertanyaan Umum)

**Q: Bisakah saya menggunakan XAMPP di folder selain C:\xampp?**
A: Ya, tapi pastikan Anda mengubah konfigurasi di Apache dan MySQL agar menunjuk ke folder baru.

**Q: Apakah XAMPP aman untuk production?**
A: Tidak. XAMPP hanya untuk development lokal. Untuk production, gunakan hosting provider atau VPS dengan konfigurasi keamanan yang proper.

**Q: Bagaimana jika saya ingin multiple PHP versions?**
A: Gunakan Laragon atau Docker yang mendukung multiple versions. XAMPP lebih terbatas dalam hal ini.

**Q: Bagaimana cara backup database MySQL?**
A: Buka phpMyAdmin → Pilih database → Export. Atau pakai command: `mysqldump -u root -p nama_database > backup.sql`

**Q: Port 3306 atau 80 sudah terpakai, bagaimana?**
A: Ubah port di konfigurasi XAMPP (httpd.conf untuk Apache, my.ini untuk MySQL), atau matikan aplikasi yang menggunakan port tersebut.

**Q: Bisakah saya mengakses XAMPP dari komputer lain di LAN?**
A: Ya, pakai IP lokal komputer Anda: `http://192.168.1.x` (ganti x dengan IP komputer Anda). Pastikan firewall memperbolehkan akses ke port 80.
