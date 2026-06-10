## 1. Cara Menghubungkan CSS ke HTML
Ada tiga cara untuk menuliskan CSS, namun dalam praktik nyata (best practice), metode **External CSS** adalah yang paling sering digunakan karena memisahkan struktur (HTML) dan desain (CSS).
 * **Inline CSS**: Ditulis langsung di dalam atribut elemen HTML.
 * **Internal CSS**: Ditulis di dalam tag <style> di area <head>.
 * **External CSS**: Ditulis di file terpisah (misal: style.css) dan dipanggil via tag <link>.
```html
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>Belajar CSS</title>
    <link rel="stylesheet" href="style.css">
    
    <style>
        h1 { color: blue; }
    </style>
</head>
<body>
    <p style="color: green;">Teks ini berwarna hijau.</p>
</body>
</html>

```
## 2. Anatomi & Selector Dasar CSS
Aturan CSS (*CSS Rule*) terdiri dari **Selector** (siapa yang mau dihias) dan **Declaration Block** (mau dihias seperti apa) yang berisi pasangan *property* dan *value*.
 * **Element Selector**: Menyasar langsung nama tag HTML.
 * **Class Selector**: Menyasar elemen dengan atribut class tertentu (diawali tanda titik .).
 * **ID Selector**: Menyasar elemen dengan atribut id tertentu (diawali tanda pagar #).
```css
/* style.css */

/* 1. Element Selector: Mengubah semua paragraf */
p {
    color: #333333;       /* Warna teks */
    font-size: 16px;      /* Ukuran font */
}

/* 2. Class Selector: Mengubah elemen yang memiliki class="tombol-utama" */
.tombol-utama {
    background-color: orange;
    border: none;
}

/* 3. ID Selector: Mengubah satu elemen spesifik dengan id="header-utama" */
#header-utama {
    text-align: center;
}

```
## 3. Pewarnaan (Colors & Backgrounds)
CSS menyediakan beberapa format untuk menentukan warna: Nama warna dasar (red, blue), rgb(), atau Hexadecimal (#ff0000).
```css
.kotak-info {
    color: white;                       /* Warna teks */
    background-color: rgb(40, 116, 240); /* Warna latar belakang (Biru) */
}

```
## 4. CSS Box Model (Konsep Paling Krusial)
Setiap elemen HTML dianggap sebagai sebuah kotak persegi. Memahami Box Model adalah kunci utama dalam mengatur tata letak dan jarak antar elemen.
 * **Content**: Isi teks atau gambar yang ada di dalam elemen.
 * **Padding**: Ruang/jarak di *dalam* elemen (antara konten dan border).
 * **Border**: Garis tepi/pembatas elemen.
 * **Margin**: Ruang/jarak di *luar* elemen (jarak antar kotak elemen).
```css
.kartu {
    width: 300px;
    content: "Isi Kotak";
    
    padding: 20px;          /* Jarak dalam 20px di semua sisi */
    border: 2px solid black; /* Garis tepi hitam setebal 2px */
    margin: 15px;           /* Jarak luar dengan elemen lain sebesar 15px */
}

```
## 5. Tipografi (Mengatur Teks)
Digunakan untuk mempercantik tampilan teks agar lebih nyaman dibaca.
 * font-family: Menentukan jenis font (serif, sans-serif, atau font eksternal seperti Google Fonts).
 * font-weight: Mengatur ketebalan huruf (bold, normal, atau angka seperi 700).
 * line-height: Mengatur jarak antar baris teks (spasi kalimat).
 * text-transform: Mengubah teks menjadi huruf kapital semua (uppercase), huruf kecil (lowercase), dll.
```css
body {
    font-family: 'Arial', sans-serif;
    line-height: 1.6;
}

.judul-blog {
    font-weight: bold;
    text-transform: uppercase;
    letter-spacing: 2px; /* Jarak antar huruf */
}

```
## 6. Layouting Dasar: Flexbox
Metode modern dan paling instan untuk mengatur posisi elemen (layout) secara searah (baris ke samping atau kolom ke bawah). Sangat powerful untuk membuat navigasi dan grid menu.
 * display: flex;: Diaktifkan pada elemen *Parent* (kontainer utama).
 * justify-content: Mengatur posisi horizontal elemen anak (kiri, tengah, kanan, atau menyebar).
 * align-items: Mengatur posisi vertikal elemen anak (atas, tengah, bawah).
```html
<div class="kontainer-menu">
    <div class="item">Menu 1</div>
    <div class="item">Menu 2</div>
    <div class="item">Menu 3</div>
</div>

```
```css
/* CSS Styling */
.kontainer-menu {
    display: flex;
    justify-content: space-between; /* Membagi ruang kosong merata di antara item */
    align-items: center;            /* Item otomatis rata tengah secara vertikal */
    background-color: #f4f4f4;
    padding: 10px;
}

.item {
    background-color: white;
    padding: 10px 20px;
}

```
## 7. Responsive Web Design: Media Queries
Agar web yang Anda buat tidak hancur saat dibuka di handphone, gunakan Media Queries untuk mengubah gaya CSS berdasarkan ukuran layar perangkat.
```css
/* Gaya default untuk layar Desktop/Laptop */
body {
    background-color: white;
    font-size: 18px;
}

/* Jika ukuran layar maksimal 768px (Tablet atau Smartphone) */
@media (max-width: 768px) {
    body {
        background-color: lightgray; /* Mengubah warna latar */
        font-size: 14px;             /* Memperkecil ukuran font */
    }
    
    .kontainer-menu {
        flex-direction: column; /* Mengubah menu flexbox dari menyamping menjadi berjejer ke bawah */
    }
}

```
### Langkah Praktis Menggabungkannya:
 1. Buat file index.html dan isi dengan beberapa tag (misal: tombol, judul, paragraf).
 2. Buat file style.css di folder yang sama, lalu hubungkan menggunakan tag <link> di HTML.
 3. Terapkan properti **Box Model** dan **Flexbox** di atas untuk mulai melihat bagaimana elemen HTML Anda mulai bergeser dan berubah bentuk secara visual.
Jika CSS ini sudah Anda kuasai, Anda siap masuk ke dunia logika web menggunakan **JavaScript**.
