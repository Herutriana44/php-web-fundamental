# Fundamental Web Development - Proyek Terpadu

📁 **Proyek web lengkap** yang menyatukan seluruh materi pembelajaran **HTML, CSS, JavaScript, PHP, dan MySQL** dalam satu aplikasi utuh.

## 📂 Struktur Direktori

```
php_web_fundamental/
├── project/        ← Proyek web terpadu (lihat README di dalam)
└── README.md       ← Dokumentasi ini
```

## 🚀 Cara Belajar

1. **Jalankan proyek** di server lokal (XAMPP/Laragon)
2. **Baca `project/README.md`** untuk petunjuk setup
3. **Jelajahi kode** dan lihat bagaimana semua teknologi bekerja bersama
4. **Modifikasi** untuk latihan

## 🔗 Teknologi yang Terintegrasi

| Teknologi | Demonstrasi | Latihan Mini |
|-----------|-------------|---------------|
| **HTML5** | Struktur halaman, elemen semantik, form, tabel | Tambahkan field `tanggal_lahir` (type="date") di form mahasiswa, tampilkan di tabel |
| **CSS3**  | Box Model, Flexbox, Responsive Design, Animasi | Ubah warna `--primary-color` di `:root` jadi `#9b59b6`, lihat perubahan otomatis di semua element |
| **JavaScript** | DOM Manipulation, Fetch API, Event Handling | Tambahkan `console.log("Row clicked", id)` di onclick edit/delete button untuk debug |
| **PHP**   | Session, PDO, Prepared Statements, Templating | Tambahkan `var_dump($mahasiswa_list)` sebelum line 13 untuk lihat struktur data |
| **MySQL** | Database CRUD, Query SQL | Jalankan `SELECT COUNT(*) FROM mahasiswa GROUP BY prodi` di phpMyAdmin untuk lihat distribusi |

## 🎯 Keunggulan

✅ **Satu proyek utuh** - bukan contoh terpisah
✅ **Aplikasi nyata** - sistem manajemen mahasiswa
✅ **Full-stack** - frontend + backend + database
✅ **Best practices** - keamanan, struktur, performa
✅ **Interaktif** - fitur pencarian, edit, hapus, notifikasi

> 📌 **Catatan:** Proyek ini dirancang untuk mempermudah pemahaman bagaimana semua teknologi web bekerja bersama dalam satu aplikasi yang koheren.

## 📝 Latihan Praktikum

### Level 1: Basic (Pemula)

#### Latihan 1.1: HTML - Tambah Field Alamat
**Tujuan:** Memahami struktur form HTML dan atribut input  
**Tugas:**
- Tambahkan field "Alamat" (textarea) pada form mahasiswa
- Tambahkan kolom "Alamat" pada tabel data mahasiswa
- Pastikan data tersimpan dan ditampilkan dengan benar

**Konsep yang dipelajari:** Form elements, textarea, table column

#### Latihan 1.2: CSS - Ubah Tema Warna
**Tujuan:** Memahami CSS Variables dan color scheme  
**Tugas:**
- Ubah warna primary dari biru menjadi hijau (#27ae60)
- Ubah warna hover button
- Sesuaikan warna header gradient

**Konsep yang dipelajari:** CSS Variables (`:root`), color properties, gradient

#### Latihan 1.3: JavaScript - Validasi NIM
**Tujuan:** Memahami event handling dan validasi input  
**Tugas:**
- Tambahkan validasi: NIM harus tepat 10 digit angka
- Tampilkan pesan error jika format salah
- Cegah form submit jika validasi gagal

**Konsep yang dipelajari:** Event listener, regex validation, form validation

#### Latihan 1.4: PHP - Format Tanggal
**Tujuan:** Memahami PHP date formatting  
**Tugas:**
- Tampilkan tanggal pendaftaran mahasiswa (dari `created_at`)
- Format: "DD Bulan YYYY" (contoh: "25 Juni 2026")
- Gunakan fungsi `date()` dan `strtotime()`

**Konsep yang dipelajari:** PHP date functions, timestamp formatting

#### Latihan 1.5: MySQL - Query Filter
**Tujuan:** Memahami SQL WHERE clause  
**Tugas:**
- Buat dropdown filter berdasarkan Program Studi
- Query hanya tampilkan mahasiswa sesuai prodi yang dipilih
- Gunakan prepared statement

**Konsep yang dipelajari:** SELECT with WHERE, prepared statements, filtering

---

### Level 2: Intermediate (Menengah)

#### Latihan 2.1: HTML + CSS - Responsive Card Layout
**Tujuan:** Memahami Flexbox dan responsive design  
**Tugas:**
- Ubah tampilan tabel menjadi card layout untuk mobile (lebar < 768px)
- Setiap mahasiswa ditampilkan sebagai card dengan foto profil placeholder
- Gunakan media queries dan Flexbox

**Konsep yang dipelajari:** Media queries, Flexbox, mobile-first design

#### Latihan 2.2: JavaScript - Export Data ke CSV
**Tujuan:** Memahami data manipulation dan file download  
**Tugas:**
- Tambahkan tombol "Export CSV"
- Convert data tabel menjadi format CSV
- Download file menggunakan Blob API
- Format: `mahasiswa_YYYYMMDD.csv`

**Konsep yang dipelajari:** Array to CSV, Blob API, file download

#### Latihan 2.3: PHP + MySQL - Pagination
**Tujuan:** Memahami LIMIT dan OFFSET dalam SQL  
**Tugas:**
- Implementasikan pagination (10 data per halaman)
- Tambahkan navigasi halaman (Previous, 1, 2, 3, Next)
- Update query dengan LIMIT dan OFFSET
- Simpan state halaman aktif

**Konsep yang dipelajari:** SQL LIMIT/OFFSET, pagination logic, state management

#### Latihan 2.4: JavaScript + PHP - Live Search dengan AJAX
**Tujuan:** Memahami asynchronous request  
**Tugas:**
- Ubah search client-side menjadi server-side
- Buat endpoint `search.php` yang menerima keyword
- Gunakan Fetch API untuk real-time search
- Tampilkan loading indicator saat request

**Konsep yang dipelajari:** AJAX, REST API, debouncing, async/await

#### Latihan 2.5: PHP - Upload Foto Mahasiswa
**Tujuan:** Memahami file upload handling  
**Tugas:**
- Tambahkan field upload foto pada form
- Validasi: hanya JPG/PNG, max 2MB
- Simpan foto ke folder `uploads/`
- Tampilkan foto di tabel dan card

**Konsep yang dipelajari:** $_FILES, move_uploaded_file, file validation

---

### Level 3: Advanced (Lanjutan)

#### Latihan 3.1: Full CRUD - Manajemen Nilai Mahasiswa
**Tujuan:** Memahami relational database dan JOIN query  
**Tugas:**
- Buat tabel `nilai` (id, mahasiswa_id, mata_kuliah, nilai, semester)
- Implementasi CRUD nilai (Create, Read, Update, Delete)
- Tampilkan nilai mahasiswa dengan JOIN query
- Hitung IPK per mahasiswa

**Konsep yang dipelajari:** Foreign key, JOIN, aggregate functions, relational data

#### Latihan 3.2: Authentication System
**Tujuan:** Memahami session management dan password hashing  
**Tugas:**
- Buat halaman login/logout
- Simpan user credentials dengan password hash (password_hash)
- Proteksi halaman dengan session check
- Implementasi "Remember Me" dengan cookie

**Konsep yang dipelajari:** Session, password_hash/verify, authentication, cookies

#### Latihan 3.3: Chart Dashboard dengan Chart.js
**Tujuan:** Memahami data visualization  
**Tugas:**
- Integrasikan Chart.js library
- Buat chart pie: distribusi mahasiswa per prodi
- Buat chart bar: jumlah mahasiswa per semester
- Data chart dari query MySQL aggregate

**Konsep yang dipelajari:** Data visualization, Chart.js, GROUP BY queries

#### Latihan 3.4: API Endpoint dengan JSON Response
**Tujuan:** Memahami RESTful API design  
**Tugas:**
- Buat API endpoint: GET `/api/mahasiswa.php`
- Buat API endpoint: POST `/api/mahasiswa.php` (create)
- Buat API endpoint: PUT `/api/mahasiswa.php?id=1` (update)
- Buat API endpoint: DELETE `/api/mahasiswa.php?id=1`
- Implementasi proper HTTP status codes (200, 201, 400, 404)

**Konsep yang dipelajari:** REST API, HTTP methods, status codes, API design

#### Latihan 3.5: Real-time Notification dengan WebSocket
**Tujuan:** Memahami real-time communication  
**Tugas:**
- Implementasi WebSocket server (gunakan Ratchet PHP)
- Broadcast notifikasi saat ada data baru ditambahkan
- Update tabel otomatis tanpa reload
- Tampilkan toast notification untuk semua user yang online

**Konsep yang dipelajari:** WebSocket, real-time updates, event broadcasting

---

### Level 4: Challenge Terpadu

#### Challenge 4.1: Sistem Absensi Terintegrasi
**Fitur yang harus dibuat:**
- QR Code generator untuk setiap mahasiswa (gunakan library QR Code)
- Halaman scan QR untuk absensi (gunakan kamera device)
- Rekam absensi dengan timestamp dan lokasi (Geolocation API)
- Dashboard statistik kehadiran (present, late, absent)
- Export laporan absensi ke PDF (gunakan library FPDF)

**Teknologi:** HTML5 (Camera API, Geolocation), CSS3 (Modal, Animation), JavaScript (QR Scanner), PHP (QR Generator, PDF), MySQL (Relational Data)

#### Challenge 4.2: Progressive Web App (PWA)
**Fitur yang harus dibuat:**
- Service Worker untuk offline capability
- Cache strategi untuk data mahasiswa
- Install prompt untuk "Add to Home Screen"
- Notifikasi push untuk update data
- Manifest.json untuk PWA metadata

**Teknologi:** Service Workers, Cache API, Push API, Web App Manifest

#### Challenge 4.3: Multi-role Permission System
**Fitur yang harus dibuat:**
- 3 role: Admin, Dosen, Mahasiswa
- Admin: full access CRUD
- Dosen: read-only + export data
- Mahasiswa: hanya lihat data pribadi + edit profil sendiri
- Middleware authorization per endpoint

**Teknologi:** Role-based access control (RBAC), middleware pattern, session management

---

## 💡 Tips Mengerjakan Latihan

1. **Mulai dari Level 1** - Pastikan memahami basic sebelum ke advanced
2. **Baca dokumentasi** - Setiap latihan punya konsep yang perlu dipelajari
3. **Lihat kode existing** - Pelajari pattern yang sudah ada di project
4. **Test setiap fitur** - Jangan lanjut sebelum fitur sebelumnya berjalan
5. **Commit bertahap** - Gunakan git untuk tracking progress per latihan
6. **Debugging** - Gunakan `console.log()` (JS) dan `var_dump()` (PHP)

## 🎓 Sumber Belajar Tambahan

- **HTML/CSS:** [MDN Web Docs](https://developer.mozilla.org)
- **JavaScript:** [JavaScript.info](https://javascript.info)
- **PHP:** [PHP Manual](https://www.php.net/manual/en/)
- **MySQL:** [MySQL Tutorial](https://dev.mysql.com/doc/)
- **Web Development:** [W3Schools](https://www.w3schools.com)

---

## 📊 Ringkasan Latihan

| Level | Jumlah Latihan | Fokus | Waktu Estimasi |
|-------|----------------|-------|----------------|
| **Level 1: Basic** | 5 latihan | HTML, CSS, JS, PHP, MySQL fundamental | 1-2 jam |
| **Level 2: Intermediate** | 5 latihan | Responsive, AJAX, Pagination, Upload | 3-5 jam |
| **Level 3: Advanced** | 5 latihan | Relational DB, Auth, Chart, API, WebSocket | 5-8 jam |
| **Level 4: Challenge** | 3 challenge | Sistem terpadu (Absensi, PWA, RBAC) | 10-20 jam |
| **Total** | **18 latihan + 3 challenge** | Full-stack mastery | 20-35 jam |

---

## 🗺️ Roadmap Belajar yang Disarankan

### Minggu 1: Dasar-Dasar (5-8 jam)
1. ✅ Setup proyek & jalankan aplikasi
2. ✅ Latihan 1.1-1.5 (Basic)
3. ✅ Modifikasi warna, form, validasi sederhana
4. ✅ Pahami alur data: HTML → JS → PHP → MySQL

### Minggu 2: Intermediate (8-12 jam)
1. ✅ Latihan 2.1-2.5 (Intermediate)
2. ✅ Implementasi pagination
3. ✅ Export CSV & upload file
4. ✅ Responsive design & AJAX search

### Minggu 3: Advanced (10-15 jam)
1. ✅ Latihan 3.1-3.5 (Advanced)
2. ✅ Relational database (tabel nilai)
3. ✅ Authentication system
4. ✅ Chart.js integration
5. ✅ REST API endpoints

### Minggu 4: Challenge & Proyek Mandiri (15-25 jam)
1. ✅ Pilih 1-2 Challenge Terpadu
2. ✅ Implementasi fitur lengkap
3. ✅ Testing & debugging
4. ✅ Deploy ke hosting (opsional)

---

## 🎯 Target Kompetensi

Setelah menyelesaikan semua latihan, Anda akan mampu:

- [ ] Membuat struktur HTML semantik dengan form dan tabel
- [ ] Styling dengan CSS modern (Flexbox, Grid, Variables, Animasi)
- [ ] Manipulasi DOM dan AJAX request dengan JavaScript
- [ ] Koneksi database MySQL dengan PDO dan Prepared Statements
- [ ] Implementasi CRUD lengkap dengan validasi dan error handling
- [ ] Membuat REST API dengan JSON response
- [ ] Authentication & Authorization system
- [ ] Responsive design untuk mobile dan desktop
- [ ] Data visualization dengan Chart.js
- [ ] Real-time features dengan WebSocket
- [ ] Build full-stack application dari nol

---

## 📞 Kontak & Komunitas

- **Pertanyaan teknis:** Buat issue di repository ini
- **Diskusi:** Bergabung dengan komunitas web development Indonesia
- **Kontribusi:** Pull request selalu diterima!

---

> 💡 **Ingat:** "The best way to learn is by doing." - Mulailah dengan latihan pertama hari ini!