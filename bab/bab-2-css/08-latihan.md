# Latihan Bab 2: CSS

## Soal 1: Styling Profil
Gunakan file `profil.html` dari latihan HTML. Buat file `style.css` terpisah untuk:
1. Background halaman warna abu-abu muda
2. Judul nama rata tengah, warna biru tua
3. Foto profil dibuat bulat (`border-radius: 50%`)
4. Paragraf dengan line-height 1.8
5. List hobi dengan bullet kustom (pakai `list-style-type`)

## Soal 2: Box Model
Buat halaman dengan 3 kotak (div) berdampingan:
1. Masing-masing kotak: lebar 250px, padding 20px, border 2px solid, margin 15px
2. Warna background berbeda tiap kotak
3. Teks di dalam kotak rata tengah
4. Tambahkan `border-radius` agar sudut melengkung

## Soal 3: Navigasi Horizontal
Buat menu navigasi horizontal dengan ketentuan:
1. Background navigasi warna gelap (#333)
2. Item menu berwarna putih, tanpa underline
3. Saat hover, background item berubah warna
4. Gunakan Flexbox untuk layout

## Soal 4: Card Layout
Buat 3 card menggunakan Flexbox:
1. Setiap card berisi: gambar, judul, deskripsi, tombol
2. Card tersusun horizontal, wrap jika layar kecil
3. Tambahkan `box-shadow` untuk efek bayangan
4. Saat hover, card sedikit terangkat (transform)

## Soal 5: Responsive Design
Buat halaman yang responsive:
1. Gunakan media query untuk 3 breakpoint: mobile (< 600px), tablet (600-900px), desktop (> 900px)
2. Pada mobile: semua elemen stacked vertikal
3. Pada tablet: 2 kolom
4. Pada desktop: 3 kolom
5. Font size menyesuaikan ukuran layar

## Soal 6: CSS Grid Portfolio
Buat portfolio layout menggunakan CSS Grid dengan:
- Header yang span semua kolom
- Main content area dengan featured project lebih besar (pakai grid-column: span 2)
- Sidebar dengan info/skills
- Footer yang span semua kolom
- Responsive: pada mobile jadi 1 kolom, tablet 2 kolom, desktop 3 kolom

## Soal 7: Animated Hamburger Menu
Buat hamburger menu yang animated:
- 3 horizontal lines (pakai ::before & ::after)
- Saat diklik, transform menjadi X
- Menu items slide in dari left dengan animation
- Backdrop blur effect
- Close saat item diklik

## Soal 8: Keyframe Animation Project
Buat loading spinner atau progress animation:
- Infinite rotating spinner (menggunakan @keyframes)
- Progress bar yang fills gradually
- Animasi text yang fade in/out
- Multiple animations berjalan simultaneously
- Smooth easing functions

## Soal 9: Advanced Selectors Challenge
Gunakan advanced selectors tanpa class/id berlebihan:
1. `nth-child()` untuk alternate row colors di tabel
2. `:not()` untuk exclude elemen tertentu
3. `~` sibling selector untuk related elements
4. Attribute selectors untuk form validation styling
5. Pseudo-elements untuk dekorasi (::before, ::after)

## Soal 10: E-Commerce Product Card (Advanced)
Buat product card yang interactive:
- Grid layout dengan gambar, title, price, rating
- Hover effect: image zoom, card shadow, overlay
- Smooth transitions (0.3s)
- "Add to cart" button dengan hover animation
- Star rating dengan partial stars (menggunakan linear-gradient atau ::before)
- Responsive: 1 kolom mobile, 2 tablet, 3+ desktop

## Soal 11: Accessibility + Advanced CSS
Buat halaman yang accessible dengan advanced CSS:
- Button dengan focus state yang jelas (outline, background change)
- Reduced motion support: `@media (prefers-reduced-motion: reduce)`
- Sufficient color contrast (4.5:1 untuk teks)
- Keyboard navigable (Tab order logical)
- Avoid aggressive animations pada :hover (use transition delays)

## Soal 12: CSS Performance Audit
Audit CSS project untuk performance:
- Periksa rendering performance (gunakan DevTools > Performance)
- Hindari expensive properties: box-shadow, blur filters pada animated elements
- Gunakan will-change wisely
- Consolidate animations ke transform & opacity
- Dokumentasikan findings
