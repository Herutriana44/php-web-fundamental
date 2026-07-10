# Latihan Bab 1: HTML

## Soal 1: Halaman Profil Diri
Buat file `profil.html` yang berisi:
1. Nama lengkap sebagai heading 1
2. Foto profil (bisa pakai placeholder: `https://via.placeholder.com/150`)
3. Paragraf singkat tentang diri Anda
4. Daftar hobi (unordered list)
5. Daftar riwayat pendidikan (ordered list)

## Soal 2: Halaman Navigasi
Buat file `navigasi.html` yang memiliki:
1. Menu navigasi dengan 4 link: Home, Profil, Kontak, Galeri
2. Masing-masing link mengarah ke section berbeda dalam 1 halaman (pakai `id` dan `#`)
3. Setiap section minimal punya heading dan 1 paragraf

## Soal 3: Tabel Data
Buat file `tabel.html` yang menampilkan tabel:
| No | Nama | Kelas | Nilai |
|----|------|-------|-------|
| 1  | Andi | X-A   | 85    |
| 2  | Budi | X-B   | 90    |
| 3  | Cici | X-A   | 78    |

Tambahkan border dan header tabel.

## Soal 4: Form Kontak
Buat file `kontak.html` dengan form yang berisi:
1. Input Nama (type text)
2. Input Email (type email)
3. Input Password (type password)
4. Radio button Jenis Kelamin
5. Dropdown Pilih Topik (Pertanyaan, Saran, Kerjasama)
6. Textarea untuk Pesan
7. Tombol Submit

## Soal 5: Halaman Lengkap
Gabungkan semua yang sudah dipelajari dalam 1 halaman `index.html`:
- Header dengan navigasi
- Section profil singkat
- Section tabel data
- Section form kontak
- Footer dengan copyright

## Soal 6: Blog Sederhana dengan Semantic HTML
Buat struktur blog yang proper menggunakan semantic HTML:
```html
<header>
    <h1>Blog Saya</h1>
    <nav><!-- Navigasi --></nav>
</header>
<main>
    <article>
        <header>
            <h2>Judul Artikel</h2>
            <time datetime="2026-07-07">7 Juli 2026</time>
            <p>Penulis: Nama Anda</p>
        </header>
        <p>Isi artikel...</p>
        <footer>
            <p>Tag: <a href="#">HTML</a>, <a href="#">Web</a></p>
        </footer>
    </article>
</main>
<aside>
    <!-- Sidebar konten terkait -->
</aside>
<footer>
    <!-- Footer halaman -->
</footer>
```
Buatnya dengan minimal 3 artikel berbeda dalam struktur yang sama.

## Soal 7: Form Login dengan Accessibility
Buat form login yang accessible:
- Semua input harus punya label yang properly associated
- Error messages harus cleardan punya aria-live
- Username & password harus properly marked
- Tab navigation harus work dengan benar
- Focus state harus terlihat jelas

## Soal 8: Portfolio Website (Project)
Buat portfolio website lengkap:
1. Halaman index dengan hero section
2. About page dengan foto dan bio
3. Projects page dengan project cards (gunakan article elements)
4. Contact page dengan form
5. Footer dengan social links
6. Navigasi yang consistent di semua halaman
7. Meta tags yang proper di setiap halaman
8. Open Graph tags untuk social sharing
9. Minimal 5 gambar dengan alt text yang descriptive

## Soal 9: Responsive Navigation (advanced)
Buat navigasi yang responsive:
1. Desktop: horizontal navigation bar
2. Mobile: hamburger menu yang bisa di-expand
3. Active state untuk current page
4. Smooth transitions
5. Keyboard navigation support (Tab key)

## Soal 10: SEO Audit Checklist
Untuk halaman favorit Anda, lakukan SEO audit:
- [ ] 1 H1 per halaman
- [ ] Heading hierarchy correct (H1 → H2 → H3)
- [ ] Semua img punya alt text descriptive
- [ ] Meta description ada dan 50-160 chars
- [ ] Title tag ada dan 50-60 chars
- [ ] Canonical URL ditambahkan (jika needed)
- [ ] Open Graph tags ada
- [ ] Struktur HTML semantic
- [ ] Validasi HTML di validator.w3.org
- [ ] Test aksesibilitas dengan screen reader atau aksesibilitas checker
