## 1. Struktur Dasar Dokumen HTML
Sebelum membuat elemen, Anda wajib memahami kerangka dasar yang menyusun sebuah halaman web.
 * <!DOCTYPE html>: Mendeklarasikan bahwa dokumen ini adalah HTML5.
 * <html>: Akar (root) dari seluruh dokumen.
 * <head>: Berisi metadata (informasi web) yang tidak tampil di browser.
 * <body>: Berisi semua konten yang akan dilihat oleh pengguna.
```html
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>Halaman HTML Pertama Saya</title>
</head>
<body>
    </body>
</html>

```
## 2. Struktur Teks (Heading & Paragraf)
Digunakan untuk membuat hierarki konten yang rapi dan mudah dibaca oleh manusia maupun mesin pencari (SEO).
 * <h1> hingga <h6>: Tag heading, di mana <h1> adalah yang terbesar/terpenting dan <h6> adalah yang terkecil.
 * <p>: Digunakan untuk membungkus teks paragraf.
 * <br>: Untuk membuat baris baru (line break) tanpa membuat paragraf baru.
```html
<h1>Belajar Web Developer dari Nol</h1>
<h2>Tahap 1: Menguasai HTML</h2>
<p>HTML adalah bahasa standar untuk membuat halaman web. <br>Sangat mudah dipelajari!</p>
<p>Ini adalah paragraf kedua.</p>

```
## 3. Format Teks (Formatting)
Digunakan untuk memberikan penekanan visual atau semantik pada teks tertentu.
 * <strong> atau <b>: Menebalkan teks. (<strong> memiliki arti semantik "penting").
 * <em> atau <i>: Memiringkan teks. (<em> memiliki arti semantik "penekanan").
 * <u>: Memberikan garis bawah pada teks.
```html
<p>Pastikan Anda belajar dengan <strong>konsisten</strong> setiap hari.</p>
<p>Format ini menggunakan efek <em>italic</em> untuk istilah asing.</p>

```
## 4. Hyperlink (Navigasi)
Menghubungkan satu dokumen HTML ke dokumen lain, baik internal maupun eksternal (URL luar).
 * <a>: Tag anchor untuk membuat link.
 * href: Atribut wajib untuk menentukan URL tujuan.
 * target="_blank": Atribut opsional agar link terbuka di tab baru.
```html
<a href="https://www.google.com" target="_blank">Buka Google di Tab Baru</a>

<a href="kontak.html">Hubungi Kami</a>

```
## 5. Media (Gambar)
Menampilkan aset visual di dalam halaman web.
 * <img>: Tag *self-closing* (tidak butuh penutup </img>).
 * src: Atribut lokasi/path file gambar.
 * alt: Teks alternatif jika gambar gagal dimuat (sangat penting untuk aksesibilitas/screen reader).
```html
<img src="logo-html.png" alt="Logo Resmi HTML5" width="200" height="200">

```
## 6. List (Daftar)
Digunakan untuk mengelompokkan poin-poin informasi.
 * <ul>: *Unordered List* (daftar dengan bullet/simbol).
 * <ol>: *Ordered List* (daftar berurutan dengan angka/huruf).
 * <li>: *List Item* (elemen di dalam daftar).
```html
<h3>Skill yang Harus Dikuasai:</h3>
<ul>
    <li>HTML</li>
    <li>CSS</li>
    <li>JavaScript</li>
</ul>

<h3>Langkah Menjalankan Kode:</h3>
<ol>
    <li>Buka VS Code.</li>
    <li>Tulis kode HTML.</li>
    <li>Buka file di browser.</li>
</ol>

```
## 7. Tabel (Organisasi Data)
Digunakan untuk menyajikan data tabular yang terdiri dari baris dan kolom.
 * <table>: Pembungkus utama tabel.
 * <tr>: *Table Row* (baris).
 * <th>: *Table Header* (judul kolom, teks otomatis tebal dan di tengah).
 * <td>: *Table Data* (sel/isi kolom).
```html
<table border="1">
    <tr>
        <th>No</th>
        <th>Nama Teknologi</th>
        <th>Fungsi</th>
    </tr>
    <tr>
        <td>1</td>
        <td>HTML</td>
        <td>Struktur Web</td>
    </tr>
    <tr>
        <td>2</td>
        <td>CSS</td>
        <td>Desain/Styling</td>
    </tr>
</table>

```
## 8. Form & Input (Interaksi Pengguna)
Komponen krusial untuk menerima input atau data dari pengguna (seperti login, registrasi, atau kontak).
 * <form>: Kontainer utama form.
 * <input>: Elemen input data (tipe ditentukan oleh atribut type).
 * <textarea>: Input teks panjang (multiline).
 * <button>: Tombol untuk submit form.
```html
<form action="/proses-data" method="POST">
    <label for="username">Username:</label>
    <input type="text" id="username" name="username" placeholder="Masukkan username"><br><br>

    <label for="password">Password:</label>
    <input type="password" id="password" name="password"><br><br>

    <p>Pilih Gender:</p>
    <input type="radio" id="pria" name="gender" value="pria">
    <label for="pria">Pria</label>
    <input type="radio" id="wanita" name="gender" value="wanita">
    <label for="wanita">Wanita</label><br><br>

    <button type="submit">Daftar Sekarang</button>
</form>

```
## 9. Elemen Semantik & Blok (Layouting Modern)
Langkah akhir mendesain struktur tata letak (layout) web. Hindari penggunaan terlalu banyak <div> (div-itis) dan gunakan tag semantik agar struktur web dikenali dengan baik oleh browser dan mesin pencari.
 * <header>: Area kepala web (logo, navigasi utama).
 * <nav>: Menu navigasi.
 * <main>: Konten utama yang unik pada halaman tersebut.
 * <section>: Bagian kelompok konten tertentu.
 * <article>: Konten mandiri (seperti postingan blog).
 * <aside>: Konten sampingan/sidebar.
 * <footer>: Area kaki web (hak cipta, link tambahan).
```html
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>Struktur Semantik</title>
</head>
<body>

    <header>
        <h1>Blog Teknologi</h1>
        <nav>
            <a href="#">Home</a> | <a href="#">Artikel</a> | <a href="#">Tentang</a>
        </nav>
    </header>

    <main>
        <section>
            <h2>Artikel Terbaru</h2>
            <article>
                <h3>Mengenal HTML Semantik</h3>
                <p>HTML semantik mempermudah mesin pencari merayapi situs Anda...</p>
            </article>
        </section>
        
        <aside>
            <h3>Mengenai Penulis</h3>
            <p>Seorang pengembang web yang suka berbagi ilmu.</p>
        </aside>
    </main>

    <footer>
        <p>&copy; 2026 Hak Cipta Dilindungi.</p>
    </footer>

</body>
</html>

```

Setelah menguasai seluruh elemen dasar dan struktural di atas, tahap akhir dari fundamental HTML adalah memahami bagaimana elemen-elemen tersebut berperan dalam arsitektur web secara keseluruhan.
Berikut adalah 3 poin penutup yang krusial untuk melengkapi pondasi HTML Anda:
## 10. Elemen Blok vs Inline (Display Behavior)
Setiap elemen di HTML memiliki perilaku tampilan bawaan (*default display*) yang menentukan bagaimana elemen tersebut mengambil ruang di halaman web.
 * **Block-level Elements**: Elemen yang selalu memulai dari baris baru dan mengambil seluruh lebar halaman yang tersedia (dari kiri ke kanan).
   * *Contoh*: <div>, <p>, <h1>-<h6>, <ul>, <li>, <section>.
 * **Inline Elements**: Elemen yang hanya mengambil ruang sesuai dengan ukuran konten di dalamnya dan tidak memulai dari baris baru.
   * *Contoh*: <span>, <a>, <strong>, <em>, <img>.
```html
<p>Paragraf Pertama (Block)</p>
<p>Paragraf Kedua (Block)</p>

<a href="#">Link 1 (Inline)</a>
<a href="#">Link 2 (Inline)</a>
<span>Teks Span (Inline)</span>

```
## 11. Atribut Global: id dan class
Atribut ini tidak mengubah tampilan HTML secara langsung, melainkan berfungsi sebagai "penanda" atau identitas elemen yang nantinya akan sangat sering Anda gunakan saat mulai belajar CSS (untuk *styling*) atau JavaScript (untuk interaktivitas).
 * **class**: Digunakan untuk menandai satu atau banyak elemen yang memiliki karakteristik sama (bisa digunakan berulang kali).
 * **id**: Identitas unik yang hanya boleh digunakan oleh **satu** elemen spesifik di dalam satu halaman web.
```html
<div class="kartu-artikel">
    <h3 class="judul-merah">Artikel HTML</h3>
</div>

<div class="kartu-artikel">
    <h3 class="judul-merah">Artikel CSS</h3>
</div>

<footer id="footer-utama">
    <p>Konten Footer</p>
</footer>

```
## 12. Entitas Karakter (Character Entities)
Beberapa karakter memiliki makna khusus dalam HTML (seperti tanda < dan >). Jika Anda ingin menampilkan karakter tersebut sebagai teks biasa di browser tanpa dianggap sebagai tag kode, Anda harus menggunakan kode entitas.
 * &lt; untuk < (*less than*)
 * &gt; untuk > (*greater than*)
 * &amp; untuk & (*ampersand*)
 * &nbsp; untuk spasi tambahan (*non-breaking space*)
```html
<p>Jika x &lt; y dan y &gt; z, maka gunakan simbol &amp; untuk logika AND.</p>

```
