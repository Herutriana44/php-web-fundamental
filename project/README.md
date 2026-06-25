# Sistem Manajemen Mahasiswa - Proyek Web Fundamental

Proyek web lengkap yang **menyatukan** seluruh materi pembelajaran HTML, CSS, JavaScript, PHP, dan MySQL dalam satu aplikasi utuh.

## Arsitektur Proyek

```
project/
├── index.php        ← Halaman utama (HTML + PHP templating + data dari DB)
├── style.css        ← Styling global (Box Model, Flexbox, Responsive)
├── script.js        ← Interaktivitas (DOM, Event, AJAX/Fetch)
├── config.php       ← Koneksi database (PDO)
├── proses.php       ← Backend CRUD (Create, Read, Update, Delete)
├── get_data.php     ← API endpoint (GET data by ID)
├── database.sql     ← Setup database & data awal
└── README.md        ← Dokumentasi ini
```

## Cara Menjalankan

1. **Import database:**
   - Buka phpMyAdmin, jalankan isi `database.sql`

2. **Salin project ke server lokal:**
   - XAMPP: salin folder `project/` ke `htdocs/`
   - Laragon: salin folder `project/` ke `www/`

3. **Buka browser:**
   ```
   http://localhost/project/index.php
   ```

## Teknologi yang Didemonstrasikan

| Teknologi | File | Konsep | Latihan Mini (5 menit) |
|-----------|------|--------|------------------------|
| **HTML5** | `index.php` | Elemen semantik (header, nav, main, section, footer), tabel, form | Di line 59, ubah `type="text"` jadi `type="tel"` dan tambahkan `pattern="[0-9]{10,13}"` untuk field telepon baru |
| **CSS3** | `style.css` | Box Model, Flexbox, Media Queries, CSS Variables, Animasi | Di line 11-13, ubah `--primary-color: #3498db` jadi `#e74c3c` (merah), reload browser dan lihat semua element berubah warna |
| **JavaScript** | `script.js` | DOM Manipulation, Event Listener, Fetch API (AJAX), Form handling | Di line 9, tambahkan `console.log('Search:', e.target.value)` untuk melihat real-time apa yang diketik user di console |
| **PHP** | `index.php`, `proses.php`, `get_data.php`, `config.php` | Session, PDO, Prepared Statements, JSON response, Templating | Di `index.php` line 13, tambahkan `echo "<pre>"; print_r($mahasiswa_list); echo "</pre>";` untuk debug data |
| **MySQL** | `database.sql` | CREATE DATABASE/TABLE, INSERT, SELECT, UPDATE, DELETE | Buka phpMyAdmin, jalankan: `SELECT prodi, COUNT(*) as total FROM mahasiswa GROUP BY prodi` untuk lihat statistik |

## Fitur Aplikasi

### 1. Dashboard statistik jumlah mahasiswa
- **Lokasi:** `index.php` baris 36-45
- **💪 Latihan:** Tambahkan stat card ketiga "Prodi Terbanyak" dengan query `SELECT prodi, COUNT(*) FROM mahasiswa GROUP BY prodi ORDER BY COUNT(*) DESC LIMIT 1`

### 2. Tabel data mahasiswa dari database (READ)
- **Lokasi:** `index.php` baris 7-10 (query), baris 109-144 (tampilan)
- **💪 Latihan:** Ubah `ORDER BY created_at DESC` jadi `ORDER BY nama ASC` untuk sorting alfabetis, reload dan lihat perubahannya

### 3. Form tambah mahasiswa (CREATE) dengan AJAX
- **Lokasi:** `script.js` baris 33-66, `proses.php` baris 40-70
- **💪 Latihan:** Di `proses.php:50`, tambahkan validasi `if (strlen($nama) < 3) throw new Exception('Nama minimal 3 karakter');` dan test dengan input pendek

### 4. Edit data mahasiswa via modal form (UPDATE)
- **Lokasi:** `script.js` baris 69-98 (fetch data), baris 33-66 (submit update)
- **💪 Latihan:** Di `script.js:86`, tambahkan `console.log('Editing:', data)` untuk debug data yang akan diedit

### 5. Hapus data dengan konfirmasi (DELETE)
- **Lokasi:** `script.js` baris 101-135, `proses.php` baris 106-131
- **💪 Latihan:** Di `script.js:103`, ganti `confirm()` dengan `window.confirm('Yakin hapus ' + nama + '?\nData tidak bisa dikembalikan!')` untuk pesan lebih detail

### 6. Pencarian/filter data real-time
- **Lokasi:** `script.js` baris 138-151
- **💪 Latihan:** Di `script.js:140`, tambahkan counter: `const found = document.querySelectorAll('#table-mahasiswa tbody tr:not([style*="none"])').length; console.log('Ditemukan:', found);`

### 7. Notifikasi sukses/gagal
- **Lokasi:** `script.js` baris 154-168, `style.css` baris 102-135
- **💪 Latihan:** Di `style.css:127`, ubah `@keyframes slideDown` jadi `slideInRight` dengan `transform: translateX(100%)` → `translateX(0)` untuk animasi dari kanan

### 8. Responsive design (mobile & desktop)
- **Lokasi:** `style.css` baris 329-357 (media queries)
- **💪 Latihan:** Di `style.css:329`, ubah breakpoint dari `768px` jadi `1024px` untuk tablet landscape, test dengan resize browser

### 9. Validasi NIM unik
- **Lokasi:** `proses.php` baris 55-59 (CREATE), baris 88-92 (UPDATE)
- **💪 Latihan:** Test validasi: coba tambah mahasiswa dengan NIM `2210631170` (sudah ada di data awal), lihat error message yang muncul

### 10. Proteksi SQL Injection via Prepared Statements
- **Lokasi:** `proses.php` baris 62-64, `config.php` baris 9-10 (PDO setup)
- **💪 Latihan:** Di `proses.php:62`, lihat pola `$stmt->execute([$nim, $nama, ...])` - ini mencegah SQL injection. Bandingkan dengan pola UNSAFE: `"INSERT ... VALUES ('$nim', '$nama')"`

## Latihan Praktikum

### A. Latihan HTML (index.php)

#### A.1: Tambah Field Telepon
**File:** `index.php`  
**Baris:** 57-90 (form section)  
**Tugas:**
1. Tambahkan field input `telepon` setelah field email
2. Gunakan `type="tel"` dengan pattern untuk format Indonesia
3. Tambahkan kolom "Telepon" di tabel (baris 110-119)
4. Update query di baris 7 untuk include field baru

**Konsep:** HTML5 input types, form structure, table column

---

#### A.2: Buat Badge Status Aktif/Nonaktif
**File:** `index.php`, `database.sql`  
**Tugas:**
1. Tambahkan field `status` (ENUM 'aktif', 'nonaktif') di tabel database
2. Tampilkan badge status di kolom tabel menggunakan `<span class="badge">`
3. Tambahkan CSS untuk styling badge (hijau = aktif, merah = nonaktif)

**Konsep:** Semantic HTML, ENUM type, conditional rendering

---

#### A.3: Implementasi Data Attribute untuk Metadata
**File:** `index.php` baris 128  
**Tugas:**
1. Tambahkan `data-nim`, `data-prodi`, `data-semester` di `<tr>` element
2. Buat fungsi JavaScript untuk filter berdasarkan data attribute
3. Tambahkan dropdown filter "Tampilkan Semester: Semua/1/2/3..."

**Konsep:** HTML5 data attributes, semantic metadata

---

### B. Latihan CSS (style.css)

#### B.1: Animasi Loading Skeleton
**File:** `style.css`  
**Tugas:**
1. Buat class `.skeleton` dengan gradient animasi (shimmer effect)
2. Tambahkan keyframe animation `@keyframes shimmer`
3. Tampilkan skeleton di tabel saat data loading (gunakan JavaScript)

**Konsep:** CSS animations, @keyframes, gradient backgrounds

---

#### B.2: Dark Mode Toggle
**File:** `style.css`, `script.js`, `index.php`  
**Tugas:**
1. Buat CSS variables untuk dark mode di `:root[data-theme="dark"]`
2. Tambahkan toggle button di header (icon matahari/bulan)
3. Simpan preferensi user di localStorage
4. Load preferensi saat page load

**Konsep:** CSS Variables, data attributes, localStorage, theme switching

---

#### B.3: Hover Effect Card 3D
**File:** `style.css`  
**Tugas:**
1. Ubah `.stat-card` menjadi 3D card dengan `transform: perspective()`
2. Tambahkan efek tilt saat hover menggunakan `rotateX()` dan `rotateY()`
3. Gunakan CSS `transition` untuk smooth animation

**Konsep:** CSS 3D transforms, perspective, hover effects

---

#### B.4: Custom Scrollbar Styling
**File:** `style.css`  
**Tugas:**
1. Style scrollbar dengan `::-webkit-scrollbar` pseudo-elements
2. Buat track, thumb, dan hover state yang match dengan tema
3. Pastikan responsive di mobile

**Konsep:** Webkit scrollbar pseudo-elements, custom UI controls

---

### C. Latihan JavaScript (script.js)

#### C.1: Debouncing untuk Search Input
**File:** `script.js` baris 137-151  
**Tugas:**
1. Implementasikan debounce function (tunggu 300ms setelah user berhenti mengetik)
2. Ganti `handleSearch` dengan debounced version
3. Tampilkan "Mencari..." indicator saat search active

**Konsep:** Debouncing, performance optimization, closures

---

#### C.2: Form Validation Real-time
**File:** `script.js`, `index.php`  
**Tugas:**
1. Validasi NIM: harus 10 digit angka (regex: `/^\d{10}$/`)
2. Validasi Nama: minimal 3 karakter, hanya huruf dan spasi
3. Validasi Email: format email valid
4. Tampilkan error message di bawah setiap field
5. Disable submit button jika ada error

**Konsep:** Form validation, regex, event listeners, DOM manipulation

---

#### C.3: Konfirmasi Modal Custom (Tanpa alert/confirm)
**File:** `script.js`, `index.php`, `style.css`  
**Tugas:**
1. Buat modal HTML untuk konfirmasi hapus (replace `confirm()` di baris 103)
2. Style modal dengan backdrop overlay (semi-transparent)
3. Tambahkan event listener untuk button "Ya" dan "Tidak"
4. Close modal dengan ESC key atau click outside

**Konsep:** Custom modal, event delegation, keyboard events

---

#### C.4: Auto-Save Draft dengan LocalStorage
**File:** `script.js`  
**Tugas:**
1. Save form data ke localStorage setiap 3 detik saat user mengisi form
2. Load draft saat form dibuka (jika ada draft tersimpan)
3. Tambahkan button "Buang Draft" untuk clear localStorage
4. Tampilkan indikator "Draft tersimpan" setelah auto-save

**Konsep:** localStorage, setInterval, auto-save pattern

---

#### C.5: Infinite Scroll / Load More
**File:** `script.js`, `proses.php` (buat endpoint baru)  
**Tugas:**
1. Buat endpoint `load_more.php` yang terima parameter `offset` dan `limit`
2. Deteksi saat user scroll mendekati bottom tabel
3. Fetch data berikutnya dan append ke tabel
4. Tampilkan loading spinner saat fetch

**Konsep:** Scroll event, intersection observer, lazy loading

---

### D. Latihan PHP (proses.php, config.php, get_data.php)

#### D.1: Input Sanitization & Validation
**File:** `proses.php` baris 44-48  
**Tugas:**
1. Tambahkan fungsi `sanitize_input()` untuk strip tags dan trim
2. Validasi email dengan `filter_var($email, FILTER_VALIDATE_EMAIL)`
3. Validasi NIM: harus unique dan format benar
4. Return error message spesifik untuk setiap validasi failure

**Konsep:** Input validation, sanitization, security best practices

---

#### D.2: Logging Activity ke File
**File:** `proses.php`, buat `logs/activity.log`  
**Tugas:**
1. Buat fungsi `log_activity($action, $data)` untuk write ke file log
2. Format: `[2026-06-25 10:30:45] CREATE - NIM: 2210631170, Nama: Andi`
3. Log setiap operasi CREATE, UPDATE, DELETE
4. Gunakan `file_put_contents()` dengan `FILE_APPEND` flag

**Konsep:** File I/O, logging, audit trail

---

#### D.3: Export Data to CSV
**File:** Buat `export.php`  
**Tugas:**
1. Query semua data mahasiswa dari database
2. Set header untuk download CSV: `Content-Type: text/csv`
3. Format data ke CSV (gunakan `fputcsv()`)
4. Nama file: `mahasiswa_YYYYMMDD_HHMMSS.csv`

**Konsep:** File headers, CSV generation, data export

---

#### D.4: Pagination dengan PHP
**File:** Buat `index_paginated.php`, `get_paginated_data.php`  
**Tugas:**
1. Tambahkan parameter `page` dan `per_page` (default: 10)
2. Hitung offset: `$offset = ($page - 1) * $per_page`
3. Query dengan LIMIT dan OFFSET
4. Return total pages: `ceil($total_records / $per_page)`
5. Buat navigation HTML (Previous, 1, 2, 3, ..., Next)

**Konsep:** SQL LIMIT/OFFSET, pagination logic, query optimization

---

#### D.5: Session-based Flash Messages
**File:** `proses.php`, `index.php`  
**Tugas:**
1. Simpan success/error message ke `$_SESSION['flash']` setelah operasi
2. Redirect user dengan `header('Location: index.php')`
3. Di `index.php`, check dan tampilkan flash message dari session
4. Clear flash message setelah ditampilkan

**Konsep:** Session management, PRG pattern (Post-Redirect-Get), flash messages

---

### E. Latihan MySQL (database.sql)

#### E.1: Indexing untuk Performance
**File:** `database.sql`  
**Tugas:**
1. Tambahkan index pada kolom `nim` (sering digunakan untuk search)
2. Tambahkan index pada kolom `prodi` (untuk filtering)
3. Jalankan `EXPLAIN SELECT * FROM mahasiswa WHERE nim = '...'`
4. Bandingkan execution time before/after index

**Konsep:** Database indexing, query optimization, EXPLAIN

---

#### E.2: Stored Procedure untuk CRUD
**File:** `database.sql`, `proses.php`  
**Tugas:**
1. Buat stored procedure `sp_create_mahasiswa(...)` dengan parameter
2. Buat stored procedure `sp_update_mahasiswa(...)`
3. Buat stored procedure `sp_delete_mahasiswa($id)`
4. Call stored procedure dari PHP dengan `$pdo->prepare("CALL sp_...")`

**Konsep:** Stored procedures, parameterized queries

---

#### E.3: Trigger untuk Auto-Update Timestamp
**File:** `database.sql`  
**Tugas:**
1. Tambahkan kolom `updated_at TIMESTAMP` di tabel mahasiswa
2. Buat trigger `BEFORE UPDATE` untuk set `updated_at = NOW()`
3. Test dengan update data mahasiswa, cek kolom `updated_at`

**Konsep:** Database triggers, automatic timestamp

---

#### E.4: View untuk Reporting
**File:** `database.sql`, buat `reports.php`  
**Tugas:**
1. Buat VIEW `v_mahasiswa_summary` yang group by prodi dengan COUNT
2. Buat VIEW `v_mahasiswa_aktif` yang filter hanya mahasiswa aktif
3. Query view dari PHP dan tampilkan di dashboard

**Konsep:** Database views, aggregate functions, reporting

---

#### E.5: Transaction untuk Data Consistency
**File:** `proses.php` (modify delete function)  
**Tugas:**
1. Wrap DELETE operation dalam transaction (`BEGIN`, `COMMIT`, `ROLLBACK`)
2. Simulasi: hapus mahasiswa + hapus nilai terkait (jika punya tabel nilai)
3. Jika salah satu query gagal, rollback semua perubahan
4. Return error message jika rollback terjadi

**Konsep:** Database transactions, ACID properties, data integrity

---

### F. Challenge Terpadu (Integrasi Semua Teknologi)

#### Challenge 1: Fitur Import Data dari Excel/CSV
**Teknologi:** HTML (file upload), PHP (parse CSV/Excel), MySQL (bulk insert)  
**Tugas:**
1. Buat form upload file CSV/Excel
2. Parse file dengan `fgetcsv()` atau library PHPExcel
3. Validasi setiap row sebelum insert
4. Insert multiple rows dengan prepared statement dalam loop
5. Tampilkan summary: "Berhasil: 50, Gagal: 5" dengan detail error

**File terlibat:** `import.php`, `process_import.php`

---

#### Challenge 2: Real-time Search dengan AJAX
**Teknologi:** JavaScript (Fetch API), PHP (JSON API), MySQL (LIKE query)  
**Tugas:**
1. Convert client-side search menjadi server-side
2. Buat endpoint `search_api.php` yang terima keyword via GET
3. Query MySQL dengan `WHERE nama LIKE '%keyword%' OR nim LIKE '%keyword%'`
4. Return JSON response
5. Update tabel dengan hasil dari server tanpa page reload

**File terlibat:** `script.js` (modify), `search_api.php` (new)

---

#### Challenge 3: Dashboard Statistik Interaktif
**Teknologi:** Chart.js, PHP (aggregate query), MySQL (GROUP BY)  
**Tugas:**
1. Integrasikan Chart.js library
2. Buat endpoint `stats_api.php` yang return data statistik:
   - Jumlah mahasiswa per prodi (pie chart)
   - Jumlah mahasiswa per semester (bar chart)
   - Trend pendaftaran per bulan (line chart)
3. Fetch data dengan AJAX dan render chart
4. Update chart saat data berubah

**File terlibat:** `index.php` (add chart canvas), `stats_api.php` (new), `script.js` (chart logic)

---

#### Challenge 4: Authentication & Authorization
**Teknologi:** PHP Session, MySQL (users table), Password Hashing  
**Tugas:**
1. Buat tabel `users` (id, username, password_hash, role)
2. Buat halaman `login.php` dan `register.php`
3. Hash password dengan `password_hash()` saat register
4. Verify password dengan `password_verify()` saat login
5. Simpan user info di session setelah login berhasil
6. Proteksi `index.php`: redirect ke login jika belum login
7. Implementasi role: admin (full CRUD), user (read-only)

**File terlibat:** `login.php`, `register.php`, `auth.php` (middleware), `logout.php`

---

#### Challenge 5: Upload & Display Foto Mahasiswa
**Teknologi:** HTML (file input), PHP (file upload), MySQL (store path)  
**Tugas:**
1. Tambahkan kolom `foto` (VARCHAR) di tabel mahasiswa untuk store path
2. Tambahkan input file di form: `<input type="file" accept="image/*">`
3. Validasi file: format (jpg/png), size (max 2MB)
4. Upload file ke folder `uploads/` dengan `move_uploaded_file()`
5. Simpan path ke database: `uploads/nim_timestamp.jpg`
6. Tampilkan foto di tabel (thumbnail) dan modal (full size)
7. Handle default avatar jika foto tidak ada

**File terlibat:** `index.php`, `proses.php`, `style.css` (image styling)

---

#### Challenge 6: Advanced Filter dengan Multiple Criteria
**Teknologi:** HTML (filter form), JavaScript (build query params), PHP (dynamic WHERE), MySQL  
**Tugas:**
1. Buat filter sidebar dengan:
   - Program Studi (checkbox multiple)
   - Semester (range slider: 1-14)
   - Status (radio: Semua/Aktif/Nonaktif)
2. Kirim filter criteria via AJAX ke `filter_api.php`
3. Build dynamic WHERE clause based on active filters
4. Return filtered data sebagai JSON
5. Update tabel tanpa page reload
6. Show active filters sebagai removable chips

**File terlibat:** `index.php`, `filter_api.php`, `script.js`, `style.css`

---

### Tips Mengerjakan Latihan

1. **Mulai dari Section A-E** (per teknologi) sebelum Challenge F (terpadu)
2. **Baca kode existing** sebelum mulai - pahami pattern yang sudah ada
3. **Test setiap latihan** - jangan lanjut jika belum berfungsi
4. **Gunakan console.log()** (JS) dan `var_dump()` (PHP) untuk debugging
5. **Commit per latihan** - untuk tracking progress
6. **Baca error message** - PHP error di browser, JS error di console
7. **Cek database** - gunakan phpMyAdmin untuk verifikasi data

### Referensi Baris Kode (untuk mempermudah navigasi)

| File | Baris | Deskripsi |
|------|-------|-----------|
| `index.php:7` | Query SELECT mahasiswa |
| `index.php:53-96` | Form section |
| `index.php:109-144` | Tabel data |
| `script.js:4-10` | Event listeners |
| `script.js:33-66` | Handle form submit |
| `script.js:69-98` | Edit data function |
| `script.js:101-135` | Delete data function |
| `script.js:138-151` | Search/filter function |
| `proses.php:40-70` | CREATE function |
| `proses.php:73-103` | UPDATE function |
| `proses.php:106-131` | DELETE function |
| `style.css:10-22` | CSS Variables |
| `style.css:75-99` | Dashboard cards |
| `style.css:247-313` | Table styling |
| `style.css:329-357` | Responsive media queries |

### Sumber Belajar per Teknologi

- **HTML5:** [MDN HTML Reference](https://developer.mozilla.org/en-US/docs/Web/HTML)
- **CSS3:** [CSS-Tricks](https://css-tricks.com), [Flexbox Guide](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)
- **JavaScript:** [JavaScript.info](https://javascript.info), [MDN JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- **PHP:** [PHP Manual](https://www.php.net/manual/en/), [PHP The Right Way](https://phptherightway.com)
- **MySQL:** [MySQL Tutorial](https://dev.mysql.com/doc/), [SQL Practice](https://www.sql-practice.com)
- **Full Stack:** [W3Schools](https://www.w3schools.com), [FreeCodeCamp](https://www.freecodecamp.org)

---

## 📊 Ringkasan Latihan di Proyek Ini

| Section | Jumlah Latihan | Fokus | File Utama |
|---------|----------------|-------|------------|
| **A. HTML** | 3 latihan | Form, semantic, data attributes | `index.php` |
| **B. CSS** | 4 latihan | Animation, dark mode, 3D, scrollbar | `style.css` |
| **C. JavaScript** | 5 latihan | Debounce, validation, modal, auto-save, infinite scroll | `script.js` |
| **D. PHP** | 5 latihan | Sanitization, logging, CSV export, pagination, flash messages | `proses.php`, `config.php` |
| **E. MySQL** | 5 latihan | Indexing, stored procedure, trigger, view, transaction | `database.sql` |
| **F. Challenge** | 6 challenge | Import CSV, real-time search, dashboard, auth, upload, advanced filter | Semua file |
| **Inline Fitur** | 10 latihan | Modifikasi langsung per fitur | Berbagai file |
| **Total** | **38 latihan + 6 challenge** | Full-stack project mastery | - |

---

## 🎯 Checklist Pengerjaan

Gunakan checklist ini untuk tracking progress Anda:

### Section A: HTML (index.php)
- [ ] A.1: Tambah Field Telepon
- [ ] A.2: Buat Badge Status Aktif/Nonaktif
- [ ] A.3: Implementasi Data Attribute untuk Metadata

### Section B: CSS (style.css)
- [ ] B.1: Animasi Loading Skeleton
- [ ] B.2: Dark Mode Toggle
- [ ] B.3: Hover Effect Card 3D
- [ ] B.4: Custom Scrollbar Styling

### Section C: JavaScript (script.js)
- [ ] C.1: Debouncing untuk Search Input
- [ ] C.2: Form Validation Real-time
- [ ] C.3: Konfirmasi Modal Custom
- [ ] C.4: Auto-Save Draft dengan LocalStorage
- [ ] C.5: Infinite Scroll / Load More

### Section D: PHP (proses.php, config.php, get_data.php)
- [ ] D.1: Input Sanitization & Validation
- [ ] D.2: Logging Activity ke File
- [ ] D.3: Export Data to CSV
- [ ] D.4: Pagination dengan PHP
- [ ] D.5: Session-based Flash Messages

### Section E: MySQL (database.sql)
- [ ] E.1: Indexing untuk Performance
- [ ] E.2: Stored Procedure untuk CRUD
- [ ] E.3: Trigger untuk Auto-Update Timestamp
- [ ] E.4: View untuk Reporting
- [ ] E.5: Transaction untuk Data Consistency

### Section F: Challenge Terpadu
- [ ] F.1: Fitur Import Data dari Excel/CSV
- [ ] F.2: Real-time Search dengan AJAX
- [ ] F.3: Dashboard Statistik Interaktif
- [ ] F.4: Authentication & Authorization
- [ ] F.5: Upload & Display Foto Mahasiswa
- [ ] F.6: Advanced Filter dengan Multiple Criteria

### Inline Latihan per Fitur
- [ ] Dashboard: Tambah stat card "Prodi Terbanyak"
- [ ] Tabel: Ubah sorting ke alfabetis
- [ ] Form CREATE: Tambah validasi nama minimal 3 karakter
- [ ] Form UPDATE: Debug data dengan console.log
- [ ] DELETE: Custom confirm message
- [ ] Search: Tambah counter hasil
- [ ] Notifikasi: Ubah animasi ke slideInRight
- [ ] Responsive: Ubah breakpoint ke 1024px
- [ ] Validasi NIM: Test duplicate NIM
- [ ] SQL Injection: Analisis prepared statements

---

## 🏆 Sertifikat Self-Learning

Setelah menyelesaikan semua latihan, Anda berhak untuk:

```
╔════════════════════════════════════════════════════════════╗
║          SERTIFIKAT KOMPETENSI WEB DEVELOPMENT           ║
║                                                           ║
║  Full-Stack Web Developer (HTML, CSS, JavaScript, PHP,   ║
║  MySQL) - Fundamental Level                                ║
║                                                           ║
║  Nama: [Isi Nama Anda]                                    ║
║  Tanggal Selesai: [DD/MM/YYYY]                            ║
║  Total Latihan: 38+ diselesaikan                           ║
║                                                           ║
╚════════════════════════════════════════════════════════════╝
```

---

## 💬 Tips & Trik

### Debugging Cepat
```javascript
// JS Debug
console.log('Variable:', myVar);
console.table(data); // Untuk array/object
console.time('timer'); ... console.timeEnd('timer');
```

```php
// PHP Debug
var_dump($variable);
die(); // Stop execution
error_reporting(E_ALL);
ini_set('display_errors', 1);
```

```sql
-- MySQL Debug
EXPLAIN SELECT * FROM mahasiswa WHERE prodi = 'Informatika';
SHOW PROCESSLIST; -- Lihat query yang sedang berjalan
```

### Shortcut VS Code
- `Ctrl+Shift+F` - Search di semua file
- `Ctrl+G` - Go to line
- `Ctrl+P` - Buka file cepat
- `Alt+↑/↓` - Move line up/down
- `Shift+Alt+↑/↓` - Copy line up/down

---

> 🚀 **Action Item:** Pilih 1 latihan dari Section A dan kerjakan SEKARANG! Jangan menunda, mulailah dengan yang paling sederhana.