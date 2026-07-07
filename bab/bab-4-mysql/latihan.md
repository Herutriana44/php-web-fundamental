# Latihan Bab 4: MySQL

## Soal 1: Membuat Database & Tabel
Jalankan query berikut di phpMyAdmin (tab SQL):
1. Buat database `latihan_web`
2. Buat tabel `siswa` dengan kolom:
   - id (INT, AUTO_INCREMENT, PRIMARY KEY)
   - nis (VARCHAR(10), UNIQUE)
   - nama (VARCHAR(100))
   - kelas (VARCHAR(10))
   - nilai (INT)

## Soal 2: Operasi CRUD Dasar
Gunakan tabel `siswa`:
1. **INSERT** 5 data siswa
2. **SELECT** semua data, urutkan berdasarkan nilai tertinggi
3. **UPDATE** nilai siswa dengan NIS tertentu
4. **DELETE** satu data siswa
5. **SELECT** dengan WHERE: tampilkan hanya siswa kelas "X-A" dengan nilai > 80

## Soal 3: Query Lanjutan
1. Tampilkan rata-rata nilai per kelas: `SELECT kelas, AVG(nilai) FROM siswa GROUP BY kelas`
2. Tampilkan jumlah siswa per kelas: `SELECT kelas, COUNT(*) FROM siswa GROUP BY kelas`
3. Tampilkan 3 siswa dengan nilai tertinggi: `SELECT * FROM siswa ORDER BY nilai DESC LIMIT 3`

## Soal 4: Relasi Tabel
1. Buat tabel `kelas` (id, nama_kelas, wali_kelas)
2. Buat tabel `siswa` dengan foreign key ke `kelas.id`
3. INSERT data ke kedua tabel
4. Tampilkan data siswa beserta nama kelasnya: `SELECT siswa.nama, kelas.nama_kelas FROM siswa JOIN kelas ON siswa.kelas_id = kelas.id`

## Soal 5: Integrasi PHP-MySQL
Buat aplikasi CRUD sederhana:
1. `koneksi.php` — Koneksi PDO ke database
2. `index.php` — Tampilkan semua data siswa dalam tabel HTML
3. `tambah.php` — Form + proses INSERT
4. `edit.php` — Form + proses UPDATE (terima parameter id via GET)
5. `hapus.php` — Proses DELETE (terima parameter id via GET)
