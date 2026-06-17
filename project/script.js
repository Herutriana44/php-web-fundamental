// script.js - JavaScript untuk interaktivitas dan AJAX

// ========== INISIALISASI & EVENT LISTENERS ==========
document.addEventListener('DOMContentLoaded', function() {
    // Button event listeners
    document.getElementById('btn-tambah').addEventListener('click', showForm);
    document.getElementById('btn-cancel').addEventListener('click', hideForm);
    document.getElementById('form-mahasiswa').addEventListener('submit', handleSubmit);
    document.getElementById('search').addEventListener('input', handleSearch);
});

// ========== TAMPILKAN/SEMBUNYIKAN FORM ==========
function showForm() {
    const formSection = document.getElementById('form-section');
    formSection.classList.remove('hidden');
    formSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
    resetForm();
}

function hideForm() {
    document.getElementById('form-section').classList.add('hidden');
    resetForm();
}

function resetForm() {
    document.getElementById('form-mahasiswa').reset();
    document.getElementById('action').value = 'create';
    document.getElementById('id').value = '';
    document.getElementById('form-title').textContent = 'Tambah Data Mahasiswa';
}

// ========== SUBMIT FORM (CREATE/UPDATE) ==========
function handleSubmit(e) {
    e.preventDefault();

    const formData = new FormData(e.target);
    const submitBtn = e.target.querySelector('button[type="submit"]');

    // Disable button saat proses
    submitBtn.disabled = true;
    submitBtn.textContent = 'Menyimpan...';

    fetch('proses.php', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            showNotification(data.message, 'success');
            hideForm();
            setTimeout(() => {
                location.reload();
            }, 1500);
        } else {
            showNotification(data.message, 'error');
        }
    })
    .catch(error => {
        showNotification('Terjadi kesalahan: ' + error.message, 'error');
    })
    .finally(() => {
        submitBtn.disabled = false;
        submitBtn.textContent = 'Simpan';
    });
}

// ========== EDIT DATA ==========
function editData(id) {
    // Ambil data mahasiswa berdasarkan ID
    fetch(`get_data.php?id=${id}`)
        .then(response => response.json())
        .then(result => {
            if (result.success) {
                const data = result.data;

                // Isi form dengan data yang akan diedit
                document.getElementById('action').value = 'update';
                document.getElementById('id').value = data.id;
                document.getElementById('nim').value = data.nim;
                document.getElementById('nama').value = data.nama;
                document.getElementById('prodi').value = data.prodi;
                document.getElementById('semester').value = data.semester;
                document.getElementById('email').value = data.email || '';

                // Ubah judul form
                document.getElementById('form-title').textContent = 'Edit Data Mahasiswa';

                // Tampilkan form dan scroll ke form
                showForm();
            } else {
                showNotification(result.message, 'error');
            }
        })
        .catch(error => {
            showNotification('Gagal mengambil data: ' + error.message, 'error');
        });
}

// ========== DELETE DATA ==========
function deleteData(id, nama) {
    // Konfirmasi sebelum hapus
    if (!confirm(`Yakin ingin menghapus data mahasiswa "${nama}"?`)) {
        return;
    }

    const formData = new FormData();
    formData.append('action', 'delete');
    formData.append('id', id);

    fetch('proses.php', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            showNotification(data.message, 'success');

            // Hapus baris dari tabel dengan animasi
            const row = document.querySelector(`tr[data-id="${id}"]`);
            row.style.transition = 'opacity 0.5s';
            row.style.opacity = '0';

            setTimeout(() => {
                location.reload();
            }, 500);
        } else {
            showNotification(data.message, 'error');
        }
    })
    .catch(error => {
        showNotification('Terjadi kesalahan: ' + error.message, 'error');
    });
}

// ========== SEARCH/FILTER TABLE ==========
function handleSearch(e) {
    const searchTerm = e.target.value.toLowerCase();
    const tableRows = document.querySelectorAll('#table-mahasiswa tbody tr');

    tableRows.forEach(row => {
        const text = row.textContent.toLowerCase();

        if (text.includes(searchTerm)) {
            row.style.display = '';
        } else {
            row.style.display = 'none';
        }
    });
}

// ========== NOTIFICATION SYSTEM ==========
function showNotification(message, type) {
    const notification = document.getElementById('notification');

    notification.textContent = message;
    notification.className = `notification ${type}`;
    notification.classList.remove('hidden');

    // Scroll ke notifikasi
    notification.scrollIntoView({ behavior: 'smooth', block: 'nearest' });

    // Auto hide setelah 5 detik
    setTimeout(() => {
        notification.classList.add('hidden');
    }, 5000);
}
