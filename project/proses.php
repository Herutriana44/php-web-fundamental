<?php
// proses.php - Backend processing untuk operasi CRUD
session_start();
require_once 'config.php';

header('Content-Type: application/json');

// Validasi request method
if ($_SERVER["REQUEST_METHOD"] !== "POST") {
    http_response_code(405);
    echo json_encode(['success' => false, 'message' => 'Method not allowed']);
    exit;
}

$action = $_POST['action'] ?? '';

try {
    switch ($action) {
        case 'create':
            createMahasiswa();
            break;

        case 'update':
            updateMahasiswa();
            break;

        case 'delete':
            deleteMahasiswa();
            break;

        default:
            throw new Exception('Aksi tidak valid');
    }
} catch (Exception $e) {
    http_response_code(400);
    echo json_encode(['success' => false, 'message' => $e->getMessage()]);
}

// Fungsi CREATE - Tambah data mahasiswa baru
function createMahasiswa() {
    global $pdo;

    // Validasi input
    $nim = trim($_POST['nim'] ?? '');
    $nama = trim($_POST['nama'] ?? '');
    $prodi = trim($_POST['prodi'] ?? '');
    $semester = intval($_POST['semester'] ?? 0);
    $email = trim($_POST['email'] ?? '');

    if (empty($nim) || empty($nama) || empty($prodi) || $semester < 1) {
        throw new Exception('Semua field wajib diisi dengan benar');
    }

    // Cek apakah NIM sudah ada
    $check = $pdo->prepare("SELECT id FROM mahasiswa WHERE nim = ?");
    $check->execute([$nim]);
    if ($check->fetch()) {
        throw new Exception('NIM sudah terdaftar');
    }

    // Insert data
    $sql = "INSERT INTO mahasiswa (nim, nama, prodi, semester, email) VALUES (?, ?, ?, ?, ?)";
    $stmt = $pdo->prepare($sql);
    $stmt->execute([$nim, $nama, $prodi, $semester, $email]);

    echo json_encode([
        'success' => true,
        'message' => 'Data mahasiswa berhasil ditambahkan'
    ]);
}

// Fungsi UPDATE - Edit data mahasiswa
function updateMahasiswa() {
    global $pdo;

    $id = intval($_POST['id'] ?? 0);
    $nim = trim($_POST['nim'] ?? '');
    $nama = trim($_POST['nama'] ?? '');
    $prodi = trim($_POST['prodi'] ?? '');
    $semester = intval($_POST['semester'] ?? 0);
    $email = trim($_POST['email'] ?? '');

    if ($id < 1 || empty($nim) || empty($nama) || empty($prodi) || $semester < 1) {
        throw new Exception('Data tidak valid');
    }

    // Cek apakah NIM sudah digunakan oleh mahasiswa lain
    $check = $pdo->prepare("SELECT id FROM mahasiswa WHERE nim = ? AND id != ?");
    $check->execute([$nim, $id]);
    if ($check->fetch()) {
        throw new Exception('NIM sudah digunakan oleh mahasiswa lain');
    }

    // Update data
    $sql = "UPDATE mahasiswa SET nim = ?, nama = ?, prodi = ?, semester = ?, email = ? WHERE id = ?";
    $stmt = $pdo->prepare($sql);
    $stmt->execute([$nim, $nama, $prodi, $semester, $email, $id]);

    echo json_encode([
        'success' => true,
        'message' => 'Data mahasiswa berhasil diperbarui'
    ]);
}

// Fungsi DELETE - Hapus data mahasiswa
function deleteMahasiswa() {
    global $pdo;

    $id = intval($_POST['id'] ?? 0);

    if ($id < 1) {
        throw new Exception('ID tidak valid');
    }

    // Cek apakah data ada
    $check = $pdo->prepare("SELECT id FROM mahasiswa WHERE id = ?");
    $check->execute([$id]);
    if (!$check->fetch()) {
        throw new Exception('Data tidak ditemukan');
    }

    // Hapus data
    $sql = "DELETE FROM mahasiswa WHERE id = ?";
    $stmt = $pdo->prepare($sql);
    $stmt->execute([$id]);

    echo json_encode([
        'success' => true,
        'message' => 'Data mahasiswa berhasil dihapus'
    ]);
}
?>
