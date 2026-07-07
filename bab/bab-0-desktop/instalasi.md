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
