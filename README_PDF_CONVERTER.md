# Cara Convert Markdown ke PDF

## Script yang Tersedia

### 1. `md_to_pdf.py` (Versi Sederhana)
Script dasar menggunakan markdown + pdfkit.

### 2. `md_to_pdf_v2.py` (Versi Lengkap)
Script dengan fitur lengkap: daftar isi, timestamp, 3 pilihan library.

### 3. `md_to_pdf_simple.py` (Versi Termux-Friendly) ⭐ Recommended
Script paling sederhana tanpa dependensi berat.

---

## Install Dependensi (Termux)

```bash
# Update package manager
pkg update && pkg upgrade

# Install Python jika belum ada
pkg install python

# Install semua dependensi (Recommended)
pip install -r requirements.txt

# ATAU install manual:
# METODE 1: weasyprint (Recommended untuk Termux)
pip install markdown weasyprint

# METODE 2: pdfkit (butuh wkhtmltopdf)
pkg install wkhtmltopdf
pip install markdown pdfkit

# METODE 3: pypandoc (butuh pandoc)
pkg install pandoc
pip install pypandoc
```

---

## Cara Menjalankan

```bash
# Pastikan di direktori php_web_fundamental
cd ~/php_web_fundamental

# Jalankan script (pilih salah satu)
python3 md_to_pdf_simple.py
python3 md_to_pdf_v2.py
python3 md_to_pdf.py
```

---

## Output

File PDF akan disimpan dengan nama:
- `dokumentasi_web_fundamental_YYYYMMDD_HHMMSS.pdf`

Contoh: `dokumentasi_web_fundamental_20260625_124530.pdf`

---

## Troubleshooting

### Error: module not found
```bash
pip install markdown weasyprint
```

### Error: wkhtmltopdf not found (jika pakai pdfkit)
```bash
pkg install wkhtmltopdf
```

### Error: Permission denied
```bash
chmod +x md_to_pdf_simple.py
python3 md_to_pdf_simple.py
```

---

## File yang Akan Dikonversi

Script otomatis mencari semua `.md` files:
- `README.md` (root)
- `project/README.md`

Urutan file: alfabetis berdasarkan path.
