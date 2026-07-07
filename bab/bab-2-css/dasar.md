# Bab 2: CSS Dasar

CSS (Cascading Style Sheets) digunakan untuk mengatur tampilan dan layout elemen HTML.

## Cara Menghubungkan CSS ke HTML

### 1. Inline CSS (tidak disarankan)
```html
<p style="color: red; font-size: 16px;">Teks merah</p>
```

### 2. Internal CSS
```html
<head>
    <style>
        p { color: blue; }
    </style>
</head>
```

### 3. External CSS (best practice)
```html
<head>
    <link rel="stylesheet" href="style.css">
</head>
```

## Selector Dasar
```css
/* Element Selector — semua tag <p> */
p {
    color: #333;
    line-height: 1.6;
}

/* Class Selector — elemen dengan class="highlight" */
.highlight {
    background-color: yellow;
}

/* ID Selector — elemen dengan id="header" */
#header {
    text-align: center;
}

/* Multiple Selector */
h1, h2, h3 {
    font-family: Arial, sans-serif;
}

/* Descendant Selector */
article p {
    font-size: 14px;
}
```

## Warna (Colors)
```css
/* Nama warna */
color: red;

/* Hexadecimal */
color: #3498db;

/* RGB */
color: rgb(52, 152, 219);

/* RGBA (dengan transparansi) */
color: rgba(52, 152, 219, 0.8);
```

## Background
```css
body {
    background-color: #f0f0f0;
    background-image: url('bg.jpg');
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center;
}
```

## Teks & Font
```css
.teks {
    font-family: 'Arial', sans-serif;
    font-size: 16px;
    font-weight: bold;
    font-style: italic;
    text-align: center;
    text-decoration: underline;
    text-transform: uppercase;
    line-height: 1.8;
    letter-spacing: 2px;
    word-spacing: 4px;
}
```

## Satuan Ukuran (Units)
- `px` — Pixel (absolut)
- `%` — Persen relatif terhadap parent
- `em` — Relatif terhadap font-size parent
- `rem` — Relatif terhadap font-size root (html)
- `vh` / `vw` — Persen dari viewport height/width
