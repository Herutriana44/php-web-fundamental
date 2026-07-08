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

## Soal 7: ES6+ Features Deep Dive
Buat script yang menggunakan:
1. Arrow functions untuk semua operations
2. Destructuring: array & object
3. Template literals untuk string
4. Spread & rest operators
5. Default parameters
6. Const/let scope handling
7. Dokumentasikan masing-masing dengan contoh

## Soal 8: Module System
Buat aplikasi modular:
1. `math.js` — Export add, subtract, multiply functions
2. `string.js` — Export capitalize, reverse functions
3. `main.js` — Import dari kedua module, gunakan functions
4. Bundle dengan webpack atau vite (optional)
5. Test imports/exports bekerja dengan benar

## Soal 9: Testing dengan Jest
Setup test project:
1. Install jest: `npm install --save-dev jest`
2. Test math functions (add, multiply, divide)
3. Test edge cases (negative numbers, zero, decimals)
4. Test with mocks: `jest.mock()`
5. Coverage: `npm test -- --coverage`
6. Target: 90%+ coverage

## Soal 10: Debugging Challenge
Debug aplikasi dengan intentional bugs:
1. Aplikasi fetch data tapi ditampilkan as [object Object]
2. Loop infinite atau performance issue
3. Variable scope problem
4. Event handler tidak berfungsi
5. Gunakan DevTools breakpoints & console untuk debug
6. Dokumentasikan bugs yang ditemukan

## Soal 11: Async/Await Mastery
Buat aplikasi dengan multiple async operations:
1. Fetch dari multiple endpoints secara parallel: `Promise.all()`
2. Fetch sequentially: `await ... then await ...`
3. Error handling dengan try-catch
4. Timeout handling
5. Retry logic (max 3 attempts)
6. Loading states untuk setiap fetch

## Soal 12: Real-world Project — Mini Chat App
Buat chat app sederhana:
1. HTML: input field, send button, message display area
2. Messages disimpan di localStorage
3. ES6+ features: arrow functions, template literals, destructuring
4. Event handling: send on button click atau Enter key
5. Timestamp untuk setiap message
6. Delete message functionality
7. Optional: fetch messages dari API endpoint
