<?php
// index.php - Halaman utama aplikasi
session_start();
require_once 'config.php';

// Ambil semua data mahasiswa dari database
$query = "SELECT * FROM mahasiswa ORDER BY created_at DESC";
$statement = $pdo->prepare($query);
$statement->execute();
$mahasiswa_list = $statement->fetchAll();

// Hitung statistik
$total_mahasiswa = count($mahasiswa_list);
?>
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sistem Manajemen Mahasiswa</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <div class="container">
            <h1>📚 Sistem Manajemen Mahasiswa</h1>
            <nav>
                <a href="index.php" class="active">Home</a>
                <a href="#tambah" id="btn-tambah">Tambah Data</a>
            </nav>
        </div>
    </header>

    <main class="container">
        <!-- Statistik Dashboard -->
        <section class="dashboard">
            <div class="stat-card">
                <h3><?= $total_mahasiswa ?></h3>
                <p>Total Mahasiswa</p>
            </div>
            <div class="stat-card">
                <h3><?= date('Y') ?></h3>
                <p>Tahun Akademik</p>
            </div>
        </section>

        <!-- Pesan notifikasi -->
        <div id="notification" class="notification hidden"></div>

        <!-- Form Tambah/Edit Mahasiswa (Hidden by default) -->
        <section id="form-section" class="form-section hidden">
            <h2 id="form-title">Tambah Data Mahasiswa</h2>
            <form id="form-mahasiswa" action="proses.php" method="POST">
                <input type="hidden" id="action" name="action" value="create">
                <input type="hidden" id="id" name="id" value="">

                <div class="form-group">
                    <label for="nim">NIM:</label>
                    <input type="text" id="nim" name="nim" required
                           placeholder="Contoh: 2210631170">
                </div>

                <div class="form-group">
                    <label for="nama">Nama Lengkap:</label>
                    <input type="text" id="nama" name="nama" required
                           placeholder="Contoh: Andi Setiawan">
                </div>

                <div class="form-group">
                    <label for="prodi">Program Studi:</label>
                    <select id="prodi" name="prodi" required>
                        <option value="">-- Pilih Prodi --</option>
                        <option value="Informatika">Informatika</option>
                        <option value="Sistem Informasi">Sistem Informasi</option>
                        <option value="Teknik Komputer">Teknik Komputer</option>
                        <option value="Teknologi Informasi">Teknologi Informasi</option>
                    </select>
                </div>

                <div class="form-group">
                    <label for="semester">Semester:</label>
                    <input type="number" id="semester" name="semester"
                           min="1" max="14" required placeholder="1-14">
                </div>

                <div class="form-group">
                    <label for="email">Email:</label>
                    <input type="email" id="email" name="email"
                           placeholder="mahasiswa@email.com">
                </div>

                <div class="form-actions">
                    <button type="submit" class="btn btn-primary">Simpan</button>
                    <button type="button" class="btn btn-secondary" id="btn-cancel">Batal</button>
                </div>
            </form>
        </section>

        <!-- Tabel Data Mahasiswa -->
        <section class="table-section">
            <h2>Daftar Mahasiswa</h2>

            <!-- Filter/Search -->
            <div class="search-box">
                <input type="text" id="search" placeholder="🔍 Cari berdasarkan nama, NIM, atau prodi...">
            </div>

            <div class="table-responsive">
                <table id="table-mahasiswa">
                    <thead>
                        <tr>
                            <th>No</th>
                            <th>NIM</th>
                            <th>Nama</th>
                            <th>Program Studi</th>
                            <th>Semester</th>
                            <th>Email</th>
                            <th>Aksi</th>
                        </tr>
                    </thead>
                    <tbody>
                        <?php if (empty($mahasiswa_list)): ?>
                            <tr>
                                <td colspan="7" class="text-center">Belum ada data mahasiswa</td>
                            </tr>
                        <?php else: ?>
                            <?php foreach ($mahasiswa_list as $index => $mhs): ?>
                                <tr data-id="<?= $mhs['id'] ?>">
                                    <td><?= $index + 1 ?></td>
                                    <td><?= htmlspecialchars($mhs['nim']) ?></td>
                                    <td><?= htmlspecialchars($mhs['nama']) ?></td>
                                    <td><?= htmlspecialchars($mhs['prodi']) ?></td>
                                    <td><?= htmlspecialchars($mhs['semester']) ?></td>
                                    <td><?= htmlspecialchars($mhs['email'] ?? '-') ?></td>
                                    <td class="action-buttons">
                                        <button class="btn-edit" onclick="editData(<?= $mhs['id'] ?>)">Edit</button>
                                        <button class="btn-delete" onclick="deleteData(<?= $mhs['id'] ?>, '<?= htmlspecialchars($mhs['nama']) ?>')">Hapus</button>
                                    </td>
                                </tr>
                            <?php endforeach; ?>
                        <?php endif; ?>
                    </tbody>
                </table>
            </div>
        </section>
    </main>

    <footer>
        <div class="container">
            <p>&copy; 2026 Sistem Manajemen Mahasiswa | Dibuat dengan HTML, CSS, JavaScript, PHP & MySQL</p>
        </div>
    </footer>

    <script src="script.js"></script>
</body>
</html>
