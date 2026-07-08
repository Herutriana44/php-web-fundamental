# Bab 1: HTML Intermediate — Meta Tags, Accessibility, SEO, Performance

Setelah menguasai elemen dasar HTML, langkah berikutnya adalah memahami metadata, aksesibilitas, SEO, dan optimasi performa. Ini adalah skill yang membedakan developer amatir dari profesional.

## 1. Meta Tags dan Head Section

### Meta Tags Penting
```html
<!DOCTYPE html>
<html lang="id">
<head>
    <!-- Character encoding (harus di awal!) -->
    <meta charset="UTF-8">
    
    <!-- Viewport untuk responsive design -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <!-- SEO meta tags -->
    <meta name="description" content="Deskripsi singkat halaman (50-160 karakter)">
    <meta name="keywords" content="keyword1, keyword2, keyword3">
    <meta name="author" content="Nama Penulis">
    
    <!-- Open Graph (untuk social media sharing) -->
    <meta property="og:title" content="Judul Halaman">
    <meta property="og:description" content="Deskripsi untuk social media">
    <meta property="og:image" content="https://example.com/image.jpg">
    <meta property="og:url" content="https://example.com/page">
    
    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="Judul">
    <meta name="twitter:description" content="Deskripsi">
    
    <!-- Favicon -->
    <link rel="icon" href="favicon.ico">
    <link rel="apple-touch-icon" href="apple-touch-icon.png">
    
    <!-- Canonical URL (untuk mencegah duplicate content) -->
    <link rel="canonical" href="https://example.com/halaman-utama">
    
    <title>Judul Halaman - Website</title>
</head>
```

## 2. Aksesibilitas (A11y)

Aksesibilitas penting agar website bisa diakses oleh semua orang, termasuk yang memiliki disabilitas.

### ARIA Attributes
```html
<!-- ARIA labels untuk screen readers -->
<button aria-label="Tutup menu">×</button>

<!-- ARIA live regions (konten yang berubah dinamis) -->
<div aria-live="polite" aria-atomic="true">
    Status: Sedang memproses...
</div>

<!-- ARIA roles untuk elemen custom -->
<div role="navigation" aria-label="Navigasi Utama">
    <a href="#home">Home</a>
    <a href="#about">Tentang</a>
</div>

<!-- ARIA descriptions -->
<img src="chart.png" alt="Grafik penjualan" aria-describedby="chart-desc">
<div id="chart-desc">Grafik menunjukkan peningkatan penjualan 20% quarter ini</div>
```

### Semantic HTML untuk Aksesibilitas
```html
<!-- ✓ BAIK: Semantic HTML -->
<nav>
    <h1>Situs Web Saya</h1>
</nav>
<main>
    <article>
        <h2>Judul Artikel</h2>
        <p>Konten artikel...</p>
    </article>
    <aside>
        <h3>Sidebar</h3>
    </aside>
</main>
<footer>
    <p>&copy; 2026 Saya</p>
</footer>

<!-- ✗ BURUK: Div everywhere -->
<div class="nav">
    <div class="header">Situs Web Saya</div>
</div>
```

### Checklist Aksesibilitas
- Alt text untuk semua gambar (deskriptif, bukan "gambar1")
- Heading hierarchy H1 → H2 → H3 (jangan lompat dari H1 ke H3)
- Kontras warna minimal 4.5:1 untuk teks
- Keyboard navigable (Tab key berfungsi, focus indicator terlihat)
- Label untuk form inputs
- Skip link ke konten utama

## 3. SEO Basics

### Heading Hierarchy (Crucial untuk SEO!)
```html
<!-- ✓ BENAR: 1 H1 per halaman -->
<h1>Cara Belajar JavaScript</h1>

<h2>1. Dasar-Dasar</h2>
<h3>Variabel</h3>
<h3>Tipe Data</h3>

<h2>2. Advanced</h2>
<h3>Async/Await</h3>

<!-- ✗ SALAH: Multiple H1 atau heading yang tidak terstruktur -->
<h1>Cara Belajar JavaScript</h1>
<h1>Variabel</h1>  <!-- Tidak boleh! -->
```

### Structured Data (Schema.org)
```html
<!-- Article Schema untuk Google Rich Snippets -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Cara Belajar JavaScript",
  "author": {
    "@type": "Person",
    "name": "John Doe"
  },
  "datePublished": "2026-01-15",
  "description": "Panduan lengkap belajar JavaScript dari nol"
}
</script>
```

### SEO Checklist
- Unique title tag (50-60 karakter)
- Meta description (50-160 karakter)
- H1 unique per halaman
- Alt text untuk images
- Internal linking (link ke halaman lain)
- Mobile-friendly
- Fast loading (under 3 seconds)

## 4. Performance Optimization

### Lazy Loading Images
```html
<!-- Gambar hanya di-load saat akan terlihat -->
<img src="image.jpg" loading="lazy" alt="Deskripsi">

<!-- Atau pakai picture element untuk responsive images -->
<picture>
    <source srcset="image-small.jpg" media="(max-width: 600px)">
    <source srcset="image-medium.jpg" media="(max-width: 1200px)">
    <img src="image-large.jpg" alt="Deskripsi">
</picture>
```

### Preload & Prefetch
```html
<!-- Preload: resource yang pasti dibutuhkan halaman ini -->
<link rel="preload" href="font.woff2" as="font" type="font/woff2">

<!-- Prefetch: resource yang mungkin dibutuhkan halaman berikutnya -->
<link rel="prefetch" href="next-page.html">

<!-- DNS prefetch: pre-resolve domain eksternal -->
<link rel="dns-prefetch" href="//cdn.example.com">
```

### Async/Defer Scripts
```html
<!-- Default: blocking (tunggu script selesai sebelum render) -->
<script src="script.js"></script>

<!-- Defer: download async, jalankan setelah HTML di-parse -->
<script src="script.js" defer></script>

<!-- Async: download & jalankan segera (tidak menjamin urutan) -->
<script src="analytics.js" async></script>
```

## 5. Best Practices

- Validasi HTML di [validator.w3.org](https://validator.w3.org)
- Test aksesibilitas dengan screen reader (NVDA, JAWS)
- SEO audit tools: Google Search Console, Lighthouse, SEMrush
- Mobile-first design (design untuk mobile dulu)
- Progressive enhancement (dasar tanpa JS, diperkaya dengan JS)
