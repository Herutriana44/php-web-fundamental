# Bab 5: JavaScript Dasar

JavaScript adalah bahasa pemrograman yang berjalan di browser (client-side) untuk memberikan interaktivitas pada halaman web. Bersama HTML (struktur) dan CSS (tampilan), JavaScript melengkapi tiga pilar web development.

## 1. Menghubungkan JavaScript ke HTML
```html
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>Belajar JavaScript</title>
</head>
<body>
    <h1>Konsol Browser adalah Teman Anda</h1>

    <!-- External JS (best practice) -->
    <script src="script.js"></script>

    <!-- Internal JS -->
    <script>
        console.log("Ini dari internal script");
    </script>
</body>
</html>
```

## 2. Output & Komentar
```javascript
// Komentar satu baris

/* Komentar
   multi baris */

// Output ke konsol browser (F12 > Console)
console.log("Halo dunia!");

// Output sebagai pop-up
alert("Ini pop-up box");

// Output ke dokumen HTML
document.write("Teks langsung ke halaman");
```

## 3. Variabel: let, const, var
```javascript
// let — nilainya bisa diubah
let nama = "Budi";
nama = "Andi";  // OK

// const — nilainya tetap (konstan)
const PI = 3.14;
// PI = 3.15;  // ERROR!

// var — cara lama, hindari (function-scoped, bisa bikin bug)
var umur = 20;
```

## 4. Tipe Data
```javascript
let teks = "Halo";           // String
let angka = 25;              // Number
let desimal = 3.14;          // Number (float)
let hidup = true;            // Boolean
let kosong = null;           // Null (sengaja dikosongkan)
let belumDiisi;              // Undefined
let unik = Symbol("id");     // Symbol

// Cek tipe data
console.log(typeof teks);    // "string"
console.log(typeof angka);   // "number"
```

## 5. Operator
```javascript
// Aritmatika
let a = 10 + 5;    // 15
let b = 10 - 5;    // 5
let c = 10 * 5;    // 50
let d = 10 / 5;    // 2
let e = 10 % 3;    // 1 (modulus/sisa bagi)
let f = 2 ** 3;    // 8 (pangkat)

// Perbandingan (hasil: boolean)
console.log(10 > 5);     // true
console.log(10 >= 10);   // true
console.log(10 === "10"); // false (strict: cek nilai DAN tipe)
console.log(10 == "10");  // true  (loose: cek nilai saja)
console.log(10 !== 5);    // true

// Logika
console.log(true && false);  // false (AND)
console.log(true || false);  // true  (OR)
console.log(!true);          // false (NOT)
```

## 6. Percabangan (Conditional)
```javascript
let nilai = 85;

if (nilai >= 90) {
    console.log("A");
} else if (nilai >= 80) {
    console.log("B");
} else if (nilai >= 70) {
    console.log("C");
} else {
    console.log("D");
}

// Ternary operator (singkat)
let status = nilai >= 70 ? "Lulus" : "Remedial";

// Switch case
let hari = "Senin";
switch (hari) {
    case "Senin":
        console.log("Upacara");
        break;
    case "Jumat":
        console.log("Senam");
        break;
    default:
        console.log("Belajar");
}
```

## 7. Perulangan (Looping)
```javascript
// For loop
for (let i = 1; i <= 5; i++) {
    console.log("Iterasi ke-" + i);
}

// While loop
let j = 0;
while (j < 5) {
    console.log("Angka: " + j);
    j++;
}

// For...of (array)
let buah = ["Apel", "Jeruk", "Mangga"];
for (let b of buah) {
    console.log(b);
}

// For...in (object)
let user = { nama: "Budi", umur: 20 };
for (let key in user) {
    console.log(key + ": " + user[key]);
}
```

## 8. Function
```javascript
// Function declaration
function sapa(nama) {
    return "Halo, " + nama + "!";
}
console.log(sapa("Budi"));

// Function expression
const kali = function(a, b) {
    return a * b;
};

// Arrow function (ES6)
const tambah = (a, b) => a + b;
const kuadrat = x => x * x;

// Default parameter
function daftar(nama, role = "user") {
    return nama + " terdaftar sebagai " + role;
}
```

## 9. Array & Method
```javascript
let fruits = ["Apel", "Jeruk", "Mangga"];

// Akses
console.log(fruits[0]);       // "Apel"
console.log(fruits.length);   // 3

// Method penting
fruits.push("Anggur");        // Tambah di akhir
fruits.pop();                 // Hapus dari akhir
fruits.unshift("Semangka");   // Tambah di awal
fruits.shift();               // Hapus dari awal
fruits.indexOf("Jeruk");      // Cari index

// Higher-order method
let angka = [1, 2, 3, 4, 5];

// map — transformasi tiap elemen
let kaliDua = angka.map(x => x * 2);  // [2, 4, 6, 8, 10]

// filter — saring elemen
let genap = angka.filter(x => x % 2 === 0);  // [2, 4]

// reduce — akumulasi
let total = angka.reduce((acc, x) => acc + x, 0);  // 15

// forEach — iterasi
angka.forEach(x => console.log(x));
```

## 10. Object
```javascript
let mahasiswa = {
    nama: "Rian",
    nim: "2210631170",
    prodi: "Informatics",
    ipk: 3.75,
    alamat: {
        kota: "Jakarta",
        kodePos: "12345"
    },
    hobi: ["Coding", "Membaca"],

    // Method
    perkenalan() {
        return `Halo, saya ${this.nama} dari ${this.prodi}`;
    }
};

console.log(mahasiswa.nama);           // "Rian"
console.log(mahasiswa["nim"]);         // "2210631170"
console.log(mahasiswa.alamat.kota);    // "Jakarta"
console.log(mahasiswa.perkenalan());
```

## 11. DOM Manipulation
Document Object Model (DOM) adalah jembatan antara JavaScript dan HTML.

```javascript
// Mencari elemen
const judul = document.getElementById("judul");
const items = document.getElementsByClassName("item");
const paragraf = document.querySelector("p");
const semuaParagraf = document.querySelectorAll("p");

// Mengubah konten
judul.innerText = "Judul Baru";
judul.innerHTML = "<strong>Judul Tebal</strong>";

// Mengubah style
judul.style.color = "red";
judul.style.fontSize = "24px";
judul.classList.add("highlight");
judul.classList.toggle("active");

// Membuat elemen baru
const div = document.createElement("div");
div.textContent = "Elemen baru";
document.body.appendChild(div);

// Menghapus elemen
div.remove();
```

## 12. Event Handling
```javascript
const tombol = document.getElementById("btn-klik");

// Cara 1: addEventListener (best practice)
tombol.addEventListener("click", function() {
    alert("Tombol diklik!");
});

// Cara 2: inline di HTML
// <button onclick="alert('Klik!')">Klik</button>

// Event types umum
// click, dblclick, mouseover, mouseout
// keydown, keyup, keypress
// submit, change, input, focus, blur
// load, scroll, resize

// Event object
tombol.addEventListener("click", function(event) {
    console.log(event.target);     // Elemen yang diklik
    console.log(event.type);       // "click"
    event.preventDefault();        // Cegah aksi default
});
```

## 13. Async JavaScript
```javascript
// Callback
setTimeout(() => {
    console.log("Dieksekusi setelah 2 detik");
}, 2000);

// Promise
fetch("https://api.example.com/data")
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error("Error:", error));

// Async/Await (cara modern)
async function ambilData() {
    try {
        const response = await fetch("https://api.example.com/data");
        const data = await response.json();
        console.log(data);
    } catch (error) {
        console.error("Error:", error);
    }
}
ambilData();
```

## 14. Local Storage
```javascript
// Simpan data (bertahan meski browser ditutup)
localStorage.setItem("username", "budi");
localStorage.setItem("theme", "dark");

// Ambil data
let user = localStorage.getItem("username");

// Hapus data
localStorage.removeItem("theme");
localStorage.clear();  // Hapus semua
```
