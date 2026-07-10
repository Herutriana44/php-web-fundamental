Berbeda dengan JavaScript yang berjalan di browser pengguna (client-side), PHP adalah bahasa pemrograman server-side. Artinya, kode PHP dieksekusi di server, lalu hasilnya dikirim ke browser dalam bentuk HTML biasa.
## 1. Persiapan Environment & Sintaks Dasar
Karena PHP berjalan di server, Anda memerlukan local server seperti **XAMPP** atau **Laragon**. File PHP harus disimpan dengan ekstensi .php di dalam folder htdocs (XAMPP) atau www (Laragon).
 * Kode PHP dibuka dengan <?php dan ditutup dengan ?> (tag penutup boleh diganti/dihilangkan jika file hanya berisi PHP).
 * Setiap baris instruksi **wajib** diakhiri dengan tanda titik koma (;).
 * echo: Perintah untuk menampilkan teks ke layar/HTML.
```php
<?php
// index.php

echo "<h1>Halo, ini dijalankan dari server!</h1>";
echo "Belajar PHP itu seru.";
?>

```
## 2. Variabel & Penggabungan Teks (Concatenation)
 * Variabel di PHP selalu diawali dengan simbol dolar ($).
 * Nama variabel bersifat sensitif terhadap huruf besar-kecil (*case-sensitive*).
 * Untuk menggabungkan dua teks atau variabel, PHP menggunakan tanda titik (.), bukan tanda tambah (+).
```php
<?php
$nama Depan = "Andi";
$namaBelakang = "Setiawan";

// Menggabungkan string dengan titik (.)
$namaLengkap = $namaDepan . " " . $namaBelakang;

echo "Selamat datang, " . $namaLengkap;
?>

```
## 3. Tipe Data
Sama seperti JavaScript, PHP akan mendeteksi tipe data secara otomatis berdasarkan nilainya.
```php
<?php
$teks = "Sekolah Koding"; // String
$tahun = 2026;            // Integer
$ipk = 3.85;              // Float/Double
$is_admin = true;         // Boolean
?>

```
## 4. Pengondisian (if, elseif, else)
Logika percabangan di PHP memiliki struktur yang hampir mirip dengan JavaScript.
```php
<?php
$nilai = 75;

if ($nilai >= 80) {
    echo "Predikat: Sangat Baik";
} elseif ($nilai >= 70) {
    echo "Predikat: Baik";
} else {
    echo "Predikat: Kurang";
}
?>

```
## 5. Array (Indexed & Associative)
PHP memiliki dua jenis array yang sangat sering digunakan dalam pengelolaan data dari database.
 * **Indexed Array**: Array dengan indeks angka (dimulai dari 0).
 * **Associative Array**: Array yang menggunakan *key* berupa teks buatan kita sendiri sebagai pengganti indeks angka.
```php
<?php
// 1. Indexed Array
$list_bahasa = ["PHP", "JavaScript", "Python"];
echo $list_bahasa[0]; // Output: PHP

// 2. Associative Array (Menggunakan pasangan key => value)
$mahasiswa = [
    "nama" => "Rian",
    "prodi" => "Informatics",
    "semester" => 4
];
echo $mahasiswa["prodi"]; // Output: Informatics
?>

```
## 6. Perulangan Khusus: foreach
Meskipun PHP mendukung for dan while, tag foreach adalah yang paling sering digunakan karena dirancang khusus untuk membongkar isi data dari Array.
```php
<?php
$kategori = ["Web", "Mobile", "AI"];

// foreach ($array as $satuan)
foreach ($kategori as $k) {
    echo "Kategori: " . $k . "<br>";
}
?>

```
## 7. Fungsi (Function)
Membungkus blok kode ke dalam sub-program yang bisa dipanggil kapan saja.
```php
<?php
function sapaPengguna($nama) {
    return "Halo, " . $nama . ". Selamat belajar!";
}

// Memanggil fungsi
echo sapaPengguna("Budi");
?>

```
## 8. Integrasi PHP ke dalam HTML (Trik Utama Template)
Kekuatan utama PHP adalah kemampuannya disisipkan di dalam struktur HTML secara dinamis. Anda bisa menggabungkan pengondisian atau perulangan PHP untuk memanipulasi tag HTML.
```php
<?php
// Anggap data ini diambil dari database
$login = true;
$hobi = ["Coding", "Membaca", "Riset"];
?>

<!DOCTYPE html>
<html>
<head>
    <title>Halaman Dinamis PHP</title>
</head>
<body>

    <?php if ($login === true) : ?>
        <h1>Selamat Datang Kembali, User!</h1>
    <?php else : ?>
        <h1>Silakan Login Terlebih Dahulu.</h1>
    <?php endif; ?>

    <h3>Daftar Hobi Saya:</h3>
    <ul>
        <?php foreach ($hobi as $h) : ?>
            <li><?php echo $h; ?></li>
        <?php endforeach; ?>
    </ul>

</body>
</html>

```

