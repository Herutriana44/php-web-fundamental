Berikut adalah alur pembelajaran fundamental **JavaScript (JS)** yang dirancang langsung ke poin inti. JavaScript digunakan untuk memberikan logika, interaktivitas, dan memanipulasi halaman web yang sebelumnya sudah dibuat menggunakan HTML dan CSS.
## 1. Menghubungkan JavaScript ke HTML
Sama seperti CSS, JavaScript bisa ditulis di dalam file HTML atau dipisah ke file eksternal (sangat direkomendasikan). Tag yang digunakan adalah <script>.
```html
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>Belajar JavaScript</title>
</head>
<body>

    <h1>Konsol Browser adalah Teman Anda</h1>

    <script src="script.js"></script>
</body>
</html>

```
## 2. Menampilkan Output & Komentar
Untuk melihat apakah kode Anda berjalan dengan benar, Anda bisa mencetaknya ke konsol browser (F12 -> tab Console) atau langsung ke layar dokumen.
```javascript
// script.js

// Ini adalah komentar satu baris (tidak akan dieksekusi)

/* Ini adalah komentar
   multibaris
*/

console.log("Halo dunia! Ini muncul di konsol browser.");
alert("Ini muncul sebagai pop-up box di layar web.");

```
## 3. Variabel (let & const)
Variabel adalah wadah untuk menyimpan data. Di JavaScript modern (ES6+), kita menggunakan let dan const. Jangan gunakan var karena sudah usang.
 * let: Nilainya **bisa** diubah kembali nanti.
 * const: Nilainya **tetap** (konstan) dan tidak bisa diubah setelah diisi.
```javascript
let namaLengkap = "Budi Sudarsono";
namaLengkap = "Budi Santoso"; // Berhasil diubah

const nim = 2210631170;
// nim = 2210631199; // Error! const tidak bisa diubah nilainya

```
## 4. Tipe Data Dasar
JavaScript otomatis mendeteksi tipe data berdasarkan nilai yang kita masukkan (*dynamically typed*).
```javascript
let teks = "Halo";          // String (Teks)
let angka = 25;             // Number (Angka bulat/desimal)
let hidup = true;           // Boolean (Benar/Salah)
let gapapa;                 // Undefined (Variabel tanpa nilai)
let kosong = null;          // Null (Variabel sengaja dikosongkan)

```
## 5. Operator (Aritmatika & Perbandingan)
Digunakan untuk menghitung nilai atau membandingkan dua buah data.
```javascript
// Operator Aritmatika
let total = 10 + 5; // 15
let sisaBagi = 10 % 3; // 1

// Operator Perbandingan (Menghasilkan Boolean: true/false)
console.log(10 > 5);   // true
console.log(10 === "10"); // false (=== memeriksa nilai DAN tipe datanya)
console.log(10 == "10");  // true  (== hanya memeriksa nilai saja)

```
## 6. Pengondisian (if, else if, else)
Digunakan untuk mengontrol alur program berdasarkan kondisi tertentu (percabangan logika).
```javascript
let nilaiUjian = 85;

if (nilaiUjian >= 80) {
    console.log("Lulus dengan predikat A");
} else if (nilaiUjian >= 60) {
    console.log("Lulus dengan predikat B");
} else {
    console.log("Tidak lulus, silakan remedial");
}

```
## 7. Perulangan (Looping: for & while)
Digunakan untuk mengeksekusi kode secara berulang-ulang selama kondisi terpenuhi.
```javascript
// For Loop: Mengulang kode 5 kali
for (let i = 1; i <= 5; i++) {
    console.log("Perulangan ke-" + i);
}

// While Loop: Berjalan selama kondisi di dalam kurung bernilai true
let angkaAcak = 1;
while (angkaAcak <= 3) {
    console.log("Angka saat ini: " + angkaAcak);
    angkaAcak++;
}

```
## 8. Function (Fungsi)
Blok kode yang dibungkus agar bisa digunakan berulang kali (*reusable*). Fungsi dapat menerima data input (*parameter*) dan mengembalikan hasil (*return*).
```javascript
// Membuat Fungsi
function hitungLuasPersegi(sisi) {
    let luas = sisi * sisi;
    return luas;
}

// Memanggil Fungsi (Mengirim data parameter 5)
let hasil = hitungLuasPersegi(5);
console.log(hasil); // Output: 25

```
## 9. Array & Object (Struktur Data)
Digunakan untuk menampung banyak data dalam satu variabel tunggal.
 * **Array**: Daftar data terurut yang diakses menggunakan nomor indeks (dimulai dari 0).
 * **Object**: Kumpulan properti yang berpasangan antara key: value.
```javascript
// Array
let bahasaKoding = ["HTML", "CSS", "JavaScript"];
console.log(bahasaKoding[2]); // Mengakses data indeks ke-2, Output: JavaScript

// Object
let user = {
    username: "dev_nusantara",
    role: "Fullstack",
    isLecturer: false
};
console.log(user.username); // Mengakses properti, Output: dev_nusantara

```
## 10. DOM Manipulation (Menghubungkan JS ke HTML)
*Document Object Model (DOM)* adalah jembatan yang membuat JavaScript bisa membaca, mengubah, menambah, atau menghapus elemen HTML secara *real-time*.
```html
<h1 id="judul-web">Teks Asli</h1>
<button id="tombol-klik">Ubah Teks</button>

```
```javascript
// Mengambil elemen HTML berdasarkan Selector
const judul = document.getElementById("judul-web");
const tombol = document.getElementById("tombol-klik");

// Mendengarkan interaksi pengguna (Event Listener)
tombol.addEventListener("click", function() {
    // Mengubah isi teks HTML saat tombol diklik
    judul.innerText = "Teks Berhasil Diubah oleh JavaScript!";
    judul.style.color = "crimson"; // Mengubah gaya CSS langsung via JS
});

```
### Langkah Praktis Menggabungkannya:
 1. Sediakan sebuah halaman HTML dengan satu tag <h1> dan satu <button>.
 2. Tulis kode **DOM Manipulation** (Poin 10) di dalam file script.js Anda.
 3. Buka halaman di browser, lalu klik tombolnya. Jika teks berubah warna dan isinya berganti, selamat! Anda telah berhasil menguasai dasar segitiga pilar web development: **HTML, CSS, dan JavaScript**.
