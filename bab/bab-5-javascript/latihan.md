# Latihan Bab 5: JavaScript

## Soal 1: Manipulasi DOM
Buat halaman `dom.html` dengan:
1. Sebuah heading dengan teks "Teks Awal"
2. Sebuah tombol "Ubah Teks"
3. Saat tombol diklik, heading berubah menjadi "Teks Sudah Diubah!" dan warnanya merah
4. Tambahkan tombol "Reset" untuk mengembalikan ke teks awal

## Soal 2: Kalkulator Interaktif
Buat `kalkulator.html` yang:
1. Dua input angka
2. Empat tombol operator: +, -, ×, ÷
3. Hasil ditampilkan di bawah tanpa reload halaman
4. Validasi: tampilkan pesan error jika input kosong atau pembagian dengan nol

## Soal 3: To-Do List
Buat aplikasi to-do list (`todo.html`):
1. Input teks + tombol "Tambah"
2. Daftar tugas ditampilkan di bawah
3. Setiap item punya tombol "Selesai" (coret teks) dan "Hapus"
4. Simpan data ke localStorage agar tidak hilang saat refresh
5. Tampilkan jumlah tugas yang belum selesai

## Soal 4: Validasi Form
Buat form registrasi dengan validasi JavaScript:
1. Nama (minimal 3 karakter)
2. Email (format email valid, pakai regex)
3. Password (minimal 8 karakter, harus ada angka dan huruf)
4. Konfirmasi Password (harus sama dengan password)
5. Tampilkan pesan error di bawah setiap input yang tidak valid
6. Form hanya bisa submit jika semua valid

## Soal 5: Galeri Gambar Sederhana
Buat galeri gambar (`galeri.html`):
1. Tampilkan 1 gambar besar di tengah
2. 5 thumbnail di bawahnya
3. Klik thumbnail mengganti gambar besar
4. Tombol "Prev" dan "Next" untuk navigasi
5. Animasi transisi saat gambar berganti (fade effect)

## Soal 6: Fetch API — Data User
Buat halaman yang menampilkan data dari API publik:
1. Fetch data dari `https://jsonplaceholder.typicode.com/users`
2. Tampilkan dalam bentuk card (nama, email, kota)
3. Tampilkan loading spinner saat data di-fetch
4. Tampilkan pesan error jika fetch gagal
5. Tombol "Refresh" untuk memuat ulang data
