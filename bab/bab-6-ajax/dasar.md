# Bab 6: AJAX & Fetch API

AJAX (Asynchronous JavaScript And XML) adalah teknik untuk mengirim dan menerima data dari server tanpa me-reload seluruh halaman. Dengan AJAX, web terasa seperti aplikasi desktop — cepat dan responsif.

## Konsep Dasar
- **Asynchronous**: Request berjalan di background, tidak memblokir halaman
- **Client → Server**: Kirim data (GET/POST) ke server PHP
- **Server → Client**: Terima response (JSON, HTML, XML, teks)
- **Update DOM**: Tampilkan data baru tanpa refresh

## 1. XMLHttpRequest (Cara Lama)
```javascript
const xhr = new XMLHttpRequest();

xhr.open("GET", "data.php", true);

xhr.onload = function() {
    if (xhr.status === 200) {
        const data = JSON.parse(xhr.responseText);
        console.log(data);
    }
};

xhr.onerror = function() {
    console.error("Request gagal");
};

xhr.send();
```

## 2. Fetch API (Cara Modern)
```javascript
// GET request
fetch("data.php")
    .then(response => {
        if (!response.ok) throw new Error("Network error");
        return response.json();
    })
    .then(data => console.log(data))
    .catch(error => console.error("Error:", error));

// POST request
fetch("proses.php", {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        nama: "Budi",
        email: "budi@example.com"
    })
})
    .then(response => response.json())
    .then(data => console.log(data));
```

## 3. Async/Await (Paling Bersih)
```javascript
async function ambilData() {
    try {
        const response = await fetch("data.php");
        if (!response.ok) throw new Error(`HTTP ${response.status}`);
        const data = await response.json();
        return data;
    } catch (error) {
        console.error("Gagal:", error.message);
        return null;
    }
}

// Panggil
const hasil = await ambilData();
```

## 4. Mengirim Form Data (FormData)
```javascript
// Cara 1: FormData object
const form = document.getElementById("form-kontak");
const formData = new FormData(form);

fetch("simpan.php", {
    method: "POST",
    body: formData  // Tidak perlu set Content-Type header
})
    .then(response => response.text())
    .then(html => {
        document.getElementById("hasil").innerHTML = html;
    });

// Cara 2: URL-encoded
const params = new URLSearchParams();
params.append("nama", "Budi");
params.append("email", "budi@example.com");

fetch("simpan.php", {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: params
});
```

## 5. Server-side PHP untuk AJAX
```php
<?php
// data.php — Mengembalikan data sebagai JSON
header("Content-Type: application/json");

$data = [
    ["id" => 1, "nama" => "Budi", "prodi" => "Informatics"],
    ["id" => 2, "nama" => "Ani", "prodi" => "Sistem Informasi"],
];

echo json_encode($data);
?>
```

```php
<?php
// simpan.php — Menerima data POST dan mengembalikan response
header("Content-Type: application/json");

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $nama = $_POST["nama"] ?? "";
    $email = $_POST["email"] ?? "";

    // Validasi
    if (empty($nama) || empty($email)) {
        http_response_code(400);
        echo json_encode(["error" => "Nama dan email wajib diisi"]);
        exit;
    }

    // Simpan ke database (contoh)
    // $stmt = $pdo->prepare("INSERT INTO users (nama, email) VALUES (?, ?)");
    // $stmt->execute([$nama, $email]);

    echo json_encode([
        "success" => true,
        "message" => "Data berhasil disimpan",
        "data" => ["nama" => $nama, "email" => $email]
    ]);
}
?>
```

## 6. Loading State & Error Handling
```javascript
async function loadData() {
    const container = document.getElementById("content");
    const spinner = document.getElementById("spinner");
    const errorDiv = document.getElementById("error");

    // Tampilkan loading
    spinner.style.display = "block";
    errorDiv.style.display = "none";
    container.innerHTML = "";

    try {
        const response = await fetch("data.php");
        if (!response.ok) throw new Error(`Server error: ${response.status}`);

        const data = await response.json();
        renderData(data);
    } catch (error) {
        errorDiv.textContent = "Gagal memuat data. Silakan coba lagi.";
        errorDiv.style.display = "block";
    } finally {
        spinner.style.display = "none";
    }
}

function renderData(items) {
    const container = document.getElementById("content");
    container.innerHTML = items.map(item => `
        <div class="card">
            <h3>${item.nama}</h3>
            <p>${item.prodi}</p>
        </div>
    `).join("");
}
```

## 7. Search / Autocomplete (Debounce)
```javascript
// Debounce: tunda eksekusi sampai user berhenti mengetik
function debounce(fn, delay) {
    let timer;
    return function(...args) {
        clearTimeout(timer);
        timer = setTimeout(() => fn.apply(this, args), delay);
    };
}

const searchInput = document.getElementById("search");
const hasil = document.getElementById("hasil-pencarian");

searchInput.addEventListener("input", debounce(async function() {
    const keyword = this.value.trim();
    if (keyword.length < 2) {
        hasil.innerHTML = "";
        return;
    }

    const response = await fetch(`cari.php?q=${encodeURIComponent(keyword)}`);
    const data = await response.json();

    hasil.innerHTML = data.map(item =>
        `<li>${item.nama} - ${item.prodi}</li>`
    ).join("");
}, 300));  // 300ms delay
```

## 8. HTTP Status Codes Penting
- **200** OK — Request berhasil
- **201** Created — Data berhasil dibuat
- **400** Bad Request — Input tidak valid
- **401** Unauthorized — Belum login
- **403** Forbidden — Tidak punya akses
- **404** Not Found — Data tidak ditemukan
- **422** Unprocessable — Validasi gagal
- **500** Internal Server Error — Error di server
