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

## Soal 6: OOP Dasar — Sistem Perpustakaan
Buat sistem perpustakaan dengan OOP:
```php
class Buku {
    private $judul;
    private $penulis;
    private $tersedia;
    
    public function __construct($judul, $penulis) { }
    public function pinjam() { }
    public function kembalikan() { }
    public function info() { }
}

class Perpustakaan {
    private $daftarBuku = [];
    public function tambahBuku(Buku $buku) { }
    public function cariByJudul($judul) { }
    public function daftarBukuTersedia() { }
}
```

## Soal 7: Form Validation & Security
Buat form registrasi dengan validasi server-side:
- Nama minimal 3 karakter, hanya huruf & spasi
- Email harus valid format
- Password minimal 8 karakter, harus ada huruf & angka
- Gunakan htmlspecialchars() untuk prevent XSS
- Hashing password dengan password_hash()
- CSRF token protection
- Sanitasi semua input

## Soal 8: Error Handling dengan Try-Catch
Buat database operations dengan error handling:
```php
try {
    $pdo = new PDO("mysql:host=localhost;dbname=test", "root", "");
    $stmt = $pdo->prepare("INSERT INTO users (nama, email) VALUES (?, ?)");
    $stmt->execute([$nama, $email]);
} catch (PDOException $e) {
    error_log($e->getMessage());
    echo "Terjadi kesalahan, silakan coba lagi.";
}
```

## Soal 9: Debugging Challenge
Debug aplikasi yang bermasalah:
1. Aplikasi tidak menampilkan error (blank page)
2. Aktifkan error reporting di php.ini atau di script
3. Gunakan var_dump() dan error_log() untuk trace bug
4. Dokumentasikan bugs yang ditemukan

## Soal 10: Session-based Login System
Buat sistem login dengan session:
1. `login.php` — Form login
2. `process_login.php` — Verify credentials, set session
3. `dashboard.php` — Halaman yang cek session
4. `logout.php` — Hapus session
5. Gunakan password_hash() & password_verify()
6. Tambahkan CSRF token ke form

## Soal 11: API Endpoint (JSON Response)
Buat API endpoint untuk AJAX:
1. `api/users.php?action=list` — Return JSON semua users
2. `api/users.php?action=get&id=1` — Return JSON user by ID
3. Header: `Content-Type: application/json`
4. Error handling dengan http_response_code()
5. Validasi input & prepared statements

## Soal 12: File Upload dengan Validasi
Buat form upload file dengan validasi:
- Hanya terima JPG, PNG (check MIME type, bukan hanya extension)
- Max file size: 2MB
- Simpan di folder aman (bukan di web root)
- Rename file agar unik: `time() . "_" . md5_file($tmp)`
- Validasi form di server (jangan percaya client-side)
