# Bab 1: HTML Dasar

HTML (HyperText Markup Language) adalah bahasa markup standar untuk membuat struktur halaman web. HTML bukan bahasa pemrograman — HTML adalah bahasa **markup** yang mendeskripsikan struktur konten.

## Konsep Dasar
- **Tag**: Diawali `<` dan diakhiri `>`. Contoh: `<p>`, `<h1>`, `<div>`
- **Elemen**: Terdiri dari tag pembuka, konten, dan tag penutup. Contoh: `<p>Ini paragraf</p>`
- **Atribut**: Informasi tambahan di dalam tag pembuka. Contoh: `<a href="url">`, `<img src="gambar.jpg">`
- **Self-closing tag**: Tag yang tidak butuh penutup. Contoh: `<br>`, `<img>`, `<hr>`, `<input>`

## Struktur Dasar HTML5
```html
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Judul Halaman</title>
</head>
<body>
    <h1>Hello World</h1>
    <p>Ini adalah paragraf pertama saya.</p>
</body>
</html>
```

## Heading & Paragraf
```html
<h1>Heading 1 (paling besar)</h1>
<h2>Heading 2</h2>
<h3>Heading 3</h3>
<h4>Heading 4</h4>
<h5>Heading 5</h5>
<h6>Heading 6 (paling kecil)</h6>

<p>Ini adalah paragraf teks.</p>
<p>Ini paragraf kedua. <br>Baris baru dalam paragraf yang sama.</p>
```

## Text Formatting
```html
<p><strong>Teks tebal (penting)</strong></p>
<p><b>Teks tebal (visual)</b></p>
<p><em>Teks miring (penekanan)</em></p>
<p><i>Teks miring (visual)</i></p>
<p><u>Teks bergaris bawah</u></p>
<p><mark>Teks ditandai</mark></p>
<p><small>Teks kecil</small></p>
<p><del>Teks dicoret</del></p>
```

## Link (Hyperlink)
```html
<!-- Link ke website lain (buka tab baru) -->
<a href="https://www.google.com" target="_blank">Buka Google</a>

<!-- Link ke halaman internal -->
<a href="tentang.html">Halaman Tentang</a>

<!-- Link ke bagian tertentu dalam halaman -->
<a href="#bagian-2">Lompat ke Bagian 2</a>

<!-- Link email -->
<a href="mailto:email@example.com">Kirim Email</a>
```

## Gambar
```html
<img src="foto.jpg" alt="Deskripsi gambar" width="300" height="200">

<!-- Gambar dengan link -->
<a href="https://example.com">
    <img src="banner.jpg" alt="Klik banner">
</a>
```

## List (Daftar)
```html
<!-- Unordered List (bullet) -->
<ul>
    <li>HTML</li>
    <li>CSS</li>
    <li>JavaScript</li>
</ul>

<!-- Ordered List (nomor) -->
<ol>
    <li>Buka editor</li>
    <li>Tulis kode</li>
    <li>Jalankan di browser</li>
</ol>

<!-- Description List -->
<dl>
    <dt>HTML</dt>
    <dd>Bahasa markup untuk struktur web</dd>
    <dt>CSS</dt>
    <dd>Bahasa untuk styling web</dd>
</dl>
```

## Komentar di HTML
```html
<!-- Ini komentar, tidak akan ditampilkan di browser -->
<!-- Komentar berguna untuk dokumentasi kode -->
```
