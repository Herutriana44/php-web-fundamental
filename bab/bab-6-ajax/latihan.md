# Latihan Bab 6: AJAX & Fetch API

## Soal 1: Live Search
Buat fitur pencarian real-time:
1. `index.html` — Input pencarian + div hasil
2. `cari.php` — Menerima parameter `?q=`, mencari di array data, return JSON
3. Setiap user mengetik (dengan debounce 300ms), tampilkan hasil di bawah input
4. Tampilkan "Tidak ditemukan" jika hasil kosong
5. Tampilkan spinner saat menunggu response

## Soal 2: Infinite Scroll
Buat halaman yang memuat data secara bertahap:
1. `data.php?page=1&limit=10` — Return 10 data per halaman (dari array)
2. Tampilkan 10 data pertama saat halaman dibuka
3. Saat user scroll ke bawah, otomatis load halaman berikutnya
4. Tampilkan "Loading..." di bagian bawah saat memuat
5. Tampilkan "Semua data sudah dimuat" jika tidak ada data lagi

## Soal 3: Form Submit dengan AJAX
Buat form kontak yang submit tanpa reload:
1. Form: nama, email, subjek, pesan
2. `kirim.php` — Validasi server-side, return JSON (success/error)
3. Tampilkan pesan sukses (hijau) atau error (merah) di atas form
4. Disable tombol submit saat proses kirim (cegah double submit)
5. Reset form setelah berhasil

## Soal 4: CRUD dengan AJAX
Buat aplikasi manajemen data sederhana:
1. `index.php` — Tampilkan tabel data dari database
2. Tombol "Tambah" — Buka modal form, submit via AJAX POST
3. Tombol "Edit" — Buka modal dengan data terisi, submit via AJAX PUT
4. Tombol "Hapus" — Konfirmasi dulu, hapus via AJAX DELETE
5. Tabel refresh otomatis setelah operasi CRUD (tanpa reload halaman)

## Soal 5: Polling / Auto-Refresh
Buat dashboard yang update otomatis:
1. `status.php` — Return JSON status terbaru (contoh: jumlah user online, data terbaru)
2. Tampilkan data di halaman
3. Auto-refresh setiap 5 detik menggunakan `setInterval` + fetch
4. Tampilkan indikator "Last updated: ..." yang update setiap kali data baru masuk
5. Tombol pause/resume untuk menghentikan/melanjutkan auto-refresh
