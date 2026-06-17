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

| Teknologi | File | Konsep |
|-----------|------|--------|
| **HTML5** | `index.php` | Elemen semantik (header, nav, main, section, footer), tabel, form |
| **CSS3** | `style.css` | Box Model, Flexbox, Media Queries, CSS Variables, Animasi |
| **JavaScript** | `script.js` | DOM Manipulation, Event Listener, Fetch API (AJAX), Form handling |
| **PHP** | `index.php`, `proses.php`, `get_data.php`, `config.php` | Session, PDO, Prepared Statements, JSON response, Templating |
| **MySQL** | `database.sql` | CREATE DATABASE/TABLE, INSERT, SELECT, UPDATE, DELETE |

## Fitur Aplikasi

- Dashboard statistik jumlah mahasiswa
- Tabel data mahasiswa dari database (READ)
- Form tambah mahasiswa (CREATE) dengan AJAX
- Edit data mahasiswa via modal form (UPDATE)
- Hapus data dengan konfirmasi (DELETE)
- Pencarian/filter data real-time
- Notifikasi sukses/gagal
- Responsive design (mobile & desktop)
- Validasi NIM unik
- Proteksi SQL Injection via Prepared Statements