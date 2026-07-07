#!/usr/bin/env python3
"""
Script convert semua .md ke 1 PDF.
Gunakan markdown-it-py (tersedia di Termux).
Untuk PDF: install weasyprint dulu (pip install weasyprint),
atau script akan menyimpan sebagai .html jika weasyprint tidak ada.
"""

import re
import sys
from pathlib import Path
from datetime import datetime

# HTML tags yang sering muncul sebagai referensi kode di teks (bukan HTML asli)
# Ini perlu di-escape agar tidak di-render sebagai HTML oleh parser markdown
HTML_TAGS_IN_TEXT = [
    'table', '/table', 'tr', '/tr', 'th', '/th', 'td', '/td',
    'form', '/form', 'input', 'textarea', '/textarea',
    'button', '/button', 'select', '/select', 'option', '/option',
    'label', '/label', 'fieldset', '/fieldset', 'legend', '/legend',
    'html', '/html', 'head', '/head', 'body', '/body',
    'header', '/header', 'nav', '/nav', 'main', '/main',
    'section', '/section', 'article', '/article', 'aside', '/aside',
    'footer', '/footer', 'div', '/div', 'span', '/span',
    'h1', '/h1', 'h2', '/h2', 'h3', '/h3', 'h4', '/h4', 'h5', '/h5', 'h6', '/h6',
    'p', '/p', 'a', '/a', 'img', 'ul', '/ul', 'ol', '/ol', 'li', '/li',
    'br', 'hr', 'strong', '/strong', 'em', '/em', 'b', '/b', 'i', '/i', 'u', '/u',
    'script', '/script', 'style', '/style', 'link', 'meta', 'title', '/title',
    'iframe', '/iframe', 'video', '/video', 'audio', '/audio',
    'pre', '/pre', 'code', '/code', 'blockquote', '/blockquote',
]


def escape_html_tags_in_text(md_content):
    """
    Escape raw HTML tags yang muncul sebagai teks referensi (bukan di dalam code block).
    Contoh: '* <table>: Pembungkus' -> '* `<table>`: Pembungkus'
    """
    lines = md_content.split('\n')
    result_lines = []
    in_code_block = False

    for line in lines:
        # Deteksi awal/akhir fenced code block
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            result_lines.append(line)
            continue

        if in_code_block:
            result_lines.append(line)
            continue

        # Escape HTML tags yang berdiri sendiri sebagai referensi
        # Pola: <tagname> atau </tagname> yang muncul di luar backtick
        for tag in HTML_TAGS_IN_TEXT:
            # Hanya escape jika tag tidak sudah berada dalam backtick
            pattern = r'(?<!`)(' + re.escape(f'<{tag}>') + r')(?!`)'
            line = re.sub(pattern, r'`\1`', line)

        result_lines.append(line)

    return '\n'.join(result_lines)


def main():
    # Coba import markdown_it (pasti ada di Termux)
    try:
        from markdown_it import MarkdownIt
    except ImportError:
        print("Error: markdown-it-py tidak terinstall.")
        print("Install: pip install markdown-it-py")
        sys.exit(1)

    base_dir = Path(__file__).parent
    md_files = sorted(base_dir.glob("**/*.md"))

    # Filter: skip file di .git/ dan file PDF_CONVERTER
    md_files = [
        f for f in md_files
        if '.git' not in f.parts
        and 'PDF_CONVERTER' not in f.name
    ]

    if not md_files:
        print("Tidak ada file .md ditemukan.")
        return

    print(f"Mengkonversi {len(md_files)} file .md:")
    for f in md_files:
        print(f"  - {f.relative_to(base_dir)}")

    # Inisialisasi markdown parser
    md = MarkdownIt()

    # Gabungkan semua markdown
    combined_md = ""
    for f in md_files:
        rel_path = str(f.relative_to(base_dir))
        print(f"  Memproses: {rel_path}")

        raw = f.read_text(encoding='utf-8')
        # Escape HTML tags yang muncul sebagai teks referensi
        escaped = escape_html_tags_in_text(raw)
        combined_md += f"\n\n# {f.stem}\n\n"
        combined_md += escaped
        combined_md += "\n\n---\n\n"

    # Render markdown ke HTML
    print("\nMerender HTML...")
    html_body = md.render(combined_md)

    # CSS styling
    css = """
    <style>
        @page { margin: 1in; size: A4; }
        body {
            font-family: 'DejaVu Sans', Arial, sans-serif;
            line-height: 1.7;
            font-size: 11pt;
            color: #333;
            max-width: 100%;
        }
        h1 {
            color: #2c3e50;
            border-bottom: 2px solid #3498db;
            padding-bottom: 8px;
            page-break-after: avoid;
            page-break-before: always;
        }
        h1:first-of-type { page-break-before: avoid; }
        h2 {
            color: #34495e;
            border-bottom: 1px solid #bdc3c7;
            padding-bottom: 5px;
            margin-top: 24px;
            page-break-after: avoid;
        }
        h3 { color: #555; margin-top: 18px; page-break-after: avoid; }
        h4, h5, h6 { color: #666; page-break-after: avoid; }
        code {
            background: #f0f0f0;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'DejaVu Sans Mono', monospace;
            font-size: 10pt;
            word-break: break-word;
        }
        pre {
            background: #f8f8f8;
            padding: 14px;
            border-left: 3px solid #3498db;
            overflow-x: auto;
            font-size: 9pt;
            line-height: 1.4;
            page-break-inside: avoid;
        }
        pre code {
            background: transparent;
            padding: 0;
            border-left: none;
        }
        table {
            border-collapse: collapse;
            width: 100%;
            margin: 16px 0;
            font-size: 10pt;
            page-break-inside: avoid;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 10px 12px;
            text-align: left;
        }
        th { background: #ecf0f1; font-weight: bold; }
        tr:nth-child(even) { background: #fafafa; }
        ul, ol { padding-left: 24px; }
        li { margin-bottom: 6px; }
        hr {
            border: none;
            border-top: 2px dashed #bdc3c7;
            margin: 32px 0;
        }
        p { margin: 8px 0; }
        strong { color: #2c3e50; }
        a { color: #3498db; }
        blockquote {
            border-left: 4px solid #bdc3c7;
            margin: 12px 0;
            padding: 8px 16px;
            background: #f9f9f9;
            color: #555;
        }
    </style>
    """

    html_full = f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>Dokumentasi Web Fundamental</title>
    {css}
</head>
<body>
    <h1 style="text-align: center; color: #3498db; border: none; page-break-before: avoid;">
        Dokumentasi Web Fundamental
    </h1>
    <p style="text-align: center; color: #7f8c8d; margin-bottom: 24px;">
        Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        &mdash; {len(md_files)} file .md
    </p>
    <hr>
    {html_body}
</body>
</html>"""

    # Simpan HTML dulu
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    html_path = base_dir / f"dokumentasi_web_fundamental_{timestamp}.html"
    html_path.write_text(html_full, encoding='utf-8')
    print(f"  HTML disimpan: {html_path.name}")

    # Coba generate PDF dengan weasyprint
    try:
        from weasyprint import HTML as WHTML, CSS
        pdf_path = base_dir / f"dokumentasi_web_fundamental_{timestamp}.pdf"
        print("Membuat PDF dengan weasyprint...")
        WHTML(string=html_full).write_pdf(pdf_path)
        size_kb = pdf_path.stat().st_size / 1024
        print(f"  PDF: {pdf_path.name} ({size_kb:.1f} KB)")
    except ImportError:
        print("\nweasyprint tidak terinstall. Hanya HTML yang disimpan.")
        print("Untuk PDF, install: pip install weasyprint")
        print("Lalu jalankan ulang script ini.")
    except Exception as e:
        print(f"  Error PDF: {e}")


if __name__ == "__main__":
    main()
