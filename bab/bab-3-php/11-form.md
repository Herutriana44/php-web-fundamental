Langkah berikutnya yang paling krusial dalam PHP setelah memahami sintaks dasar adalah **menghubungkan web dengan data**. Kita akan mempelajari bagaimana PHP mengambil data yang diinput oleh user melalui form HTML (**GET & POST**), serta bagaimana berinteraksi dengan database menggunakan **MySQLi / PDO**.
## 9. Penanganan Form ($_GET dan $_POST)
Saat user mengisi form dan menekan tombol submit, PHP menggunakan *Superglobals Variables* ($_GET atau $_POST) untuk menangkap data tersebut di server.
 * **$_GET**: Mengirim data melalui URL. Data terlihat di browser (cocok untuk fitur pencarian/filter).
 * **$_POST**: Mengirim data di balik layar. Data tidak terlihat di URL (wajib untuk data sensitif seperti password atau registrasi).
```html
<form action="proses.php" method="POST">
    <label>Nama:</label>
    <input type="text" name="nama_pengguna">
    
    <button type="submit">Kirim</button>
</form>

```
```php
<?php
// proses.php

// Memeriksa apakah data dengan name "nama_pengguna" dikirim menggunakan POST
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Mengambil data dari input form
    $nama = $_POST['nama_pengguna'];
    
    echo "Halo " . htmlspecialchars($nama) . ", data Anda berhasil diproses di server!";
}
?>

```
## 10. Koneksi Database MySQL via PHP (PDO)
Untuk menyimpan data secara permanen, kita perlu menghubungkan script PHP ke database seperti MySQL. Menggunakan **PDO (PHP Data Objects)** sangat direkomendasikan karena lebih aman dari *SQL Injection* dan mendukung berbagai jenis database.
```php
<?php
// koneksi.php
$host = "localhost";
$user = "root";
$pass = "";
$db   = "belajar_web";

try {
    // Membuat koneksi ke MySQL
    $pdo = new PDO("mysql:host=$host;dbname=$db", $user, $pass);
    
    // Mengatur mode error PDO ke Exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    
    echo "Koneksi ke database berhasil!";
} catch (PDOException $e) {
    echo "Koneksi gagal: " . $e->getMessage();
}
?>

```
## 11. Mengambil Data dari Database (Read SQL)
Setelah koneksi berhasil, Anda bisa mengeksekusi perintah SQL untuk mengambil data dari tabel dan menampilkannya ke halaman web.
```php
<?php
// Tulis kode koneksi di atas atau include file koneksi
// include 'koneksi.php';

// 1. Siapkan perintah SQL
$query = "SELECT * FROM mahasiswa";
$statement = $pdo->prepare($query);

// 2. Eksekusi perintah
$statement->execute();

// 3. Ambil semua baris data sebagai Associative Array
$hasil = $statement->fetchAll(PDO::FETCH_ASSOC);
?>

<!DOCTYPE html>
<html>
<head><title>Daftar Mahasiswa</title></head>
<body>
    <h2>Data Mahasiswa dari Database</h2>
    <ul>
        <?php foreach ($hasil as $mhs) : ?>
            <li><?= htmlspecialchars($mhs['nama']) ?> - <?= htmlspecialchars($mhs['prodi']) ?></li>
        <?php endforeach; ?>
    </ul>
</body>
</html>

```
## 12. Menyimpan Data ke Database (Create/Insert SQL)
Gunakan *Prepared Statements* (tanda tanya ? atau bindParam) untuk memasukkan data dari form ke database dengan aman agar terhindar dari peretasan.
```php
<?php
// Contoh menerima data dari form tambah data
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $nama  = $_POST['nama'];
    $prodi = $_POST['prodi'];

    // SQL dengan placeholder (?) untuk keamanan
    $sql = "INSERT INTO mahasiswa (nama, prodi) VALUES (?, ?)";
    $stmt = $pdo->prepare($sql);
    
    // Eksekusi dengan memasukkan variabel ke dalam array sesuai urutan tanda tanya
    $stmt->execute([$nama, $prodi]);

    echo "Data baru berhasil ditambahkan!";
}
?>

```
## 13. State Management: $_SESSION
Karena HTTP bersifat *stateless* (tidak mengingat siapa Anda setelah pindah halaman), PHP menggunakan **Session** untuk menyimpan data user (seperti status login) di server agar bisa diakses di halaman mana pun.
```php
<?php
// login.php
session_start(); // Wajib ditulis di baris paling atas sebelum kode apa pun

// Anggap proses validasi login berhasil
$_SESSION['user_id'] = 123;
$_SESSION['username'] = "budi_tech";

echo "Anda berhasil login. Silakan buka halaman dashboard.php";
?>

```
```php
<?php
// dashboard.php
session_start();

// Proteksi halaman: jika session username belum ada, tendang kembali ke login
if (!isset($_SESSION['username'])) {
    header("Location: login.php");
    exit;
}

echo "Selamat Datang di Ruang Admin, " . $_SESSION['username'];
?>

```
