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

## Soal 6: Indexes & Performance Optimization
1. Buat tabel dengan 100,000+ rows
2. Test query speed tanpa index: `SELECT * FROM users WHERE email = ?`
3. Buat index: `CREATE INDEX idx_email ON users(email)`
4. Bandingkan query speed dengan EXPLAIN (rows yang dipindai harus lebih sedikit)
5. Dokumentasikan perbedaan performance

## Soal 7: Many-to-Many Relationship
Buat sistem enrollment:
1. Tabel `students` (id, nama)
2. Tabel `courses` (id, nama, deskripsi)
3. Tabel `student_courses` (student_id, course_id, PRIMARY KEY, FOREIGN KEYs)
4. Insert data sample
5. Query: tampilkan students dengan courses mereka (JOIN 3 tabel)
6. Query: tampilkan courses dengan jumlah students enrolled (GROUP BY, COUNT)

## Soal 8: Transactions & Atomicity
Buat sistem transfer bank sederhana:
```php
try {
    $pdo->beginTransaction();
    // Debit dari account A
    // Credit ke account B
    // Jika error, semua di-rollback
    $pdo->commit();
} catch (Exception $e) {
    $pdo->rollBack();
}
```
Test dengan intentional error di tengah transaction → pastikan rollback bekerja.

## Soal 9: Normalization & Data Integrity
Audit database untuk normalization:
- [ ] Tidak ada repeating groups
- [ ] Semua non-key columns dependent pada primary key (1NF)
- [ ] Tidak ada partial dependencies (2NF)
- [ ] Tidak ada transitive dependencies (3NF)
- Dokumentasikan schema dalam ERD (Entity Relationship Diagram)

## Soal 10: Backup & Recovery
1. Backup database: `mysqldump -u root -p db_name > backup.sql`
2. Tambahkan beberapa data baru
3. Restore dari backup: `mysql -u root -p db_name < backup.sql`
4. Verify data kembali ke state sebelumnya
5. Backup incrementally (hanya changes sejak backup terakhir)
