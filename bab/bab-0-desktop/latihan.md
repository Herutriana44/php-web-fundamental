# Latihan Bab 0: Instalasi & Environment

## Soal 1: Instalasi XAMPP
1. Download dan install XAMPP di komputer Anda.
2. Jalankan Apache dan MySQL dari XAMPP Control Panel.
3. Buktikan dengan screenshot `http://localhost` yang menampilkan halaman XAMPP.

## Soal 2: File PHP Pertama
1. Buat folder `belajar` di dalam `htdocs`.
2. Buat file `index.php` yang menampilkan teks "Server Saya Sudah Siap!".
3. Akses via `http://localhost/belajar/`.

## Soal 3: Cek Info PHP
1. Buat file `cek.php` dengan fungsi `phpinfo()`.
2. Cari informasi versi PHP yang terinstall.
3. Catat versi PHP tersebut.

## Soal 4: Struktur Folder
Buat struktur folder berikut di dalam `htdocs`:
```
htdocs/
├── belajar/
│   ├── index.php
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── images/
```

## Soal 5: Mengubah Port Apache
1. Buka file `C:\xampp\apache\conf\httpd.conf`
2. Cari baris `Listen 80`
3. Ubah menjadi `Listen 8080`
4. Restart Apache
5. Akses `http://localhost:8080` — pastikan berhasil
6. Ubah kembali ke port 80 dan restart

## Soal 6: Database Pertama di phpMyAdmin
1. Buka `http://localhost/phpmyadmin`
2. Buat database baru bernama `toko_online`
3. Buat tabel `produk` dengan kolom:
   - id (INT, AUTO_INCREMENT, PRIMARY KEY)
   - nama (VARCHAR(100))
   - harga (FLOAT)
   - stok (INT)
4. Insert 3 data produk
5. Lihat hasilnya di tab Browse

## Soal 7: File Configuration
1. Buat file `config.php` di folder `belajar/`
2. Simpan konfigurasi berikut:
   ```php
   <?php
   define("DB_HOST", "localhost");
   define("DB_USER", "root");
   define("DB_PASS", "");
   define("DB_NAME", "toko_online");
   
   define("BASE_URL", "http://localhost/belajar/");
   define("SITE_NAME", "Toko Online Saya");
   ?>
   ```
3. Di file `index.php`, include file config tersebut: `<?php include 'config.php'; ?>`
4. Tampilkan konstanta di halaman: `echo BASE_URL;`

## Soal 8: Troubleshooting Challenge
Berikut adalah list masalah yang sengaja dibuat. Troubleshoot dan dokumentasikan solusinya:
1. Buat file `.html` biasa (bukan `.php`) di htdocs, pastikan bisa diakses
2. Ubah nama folder htdocs menjadi `myweb`, coba akses `http://localhost` (akan error), kembali ke `htdocs`
3. Matikan Apache saja (biarkan MySQL), coba akses `http://localhost` (akan gagal), nyalakan kembali
4. Catat apa yang terjadi di setiap step dan dokumentasikan dalam file `troubleshooting_log.txt`
