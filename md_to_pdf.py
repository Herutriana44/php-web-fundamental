#!/usr/bin/env python3
"""
Script untuk convert semua file .md di direktori menjadi 1 file PDF secara berurutan.
Prasyarat: pip install markdown pdfkit
Atau: pip install markdown pypandoc
"""

import os
import re
import sys
from pathlib import Path

try:
    import markdown
except ImportError:
    print("Error: module 'markdown' tidak terinstall. Install dengan: pip install markdown")
    sys.exit(1)

try:
    import pdfkit
except ImportError:
    print("Error: module 'pdfkit' tidak terinstall. Install dengan: pip install pdfkit")
    print("Juga perlu menginstall wkhtmltopdf di sistem.")
    sys.exit(1)


def markdown_to_html(md_content):
    """Convert markdown content ke HTML."""
    md = markdown.Markdown(
        extensions=[
            'extra',
            'codehilite',
            'toc',
            'tables',
            'nl2br'
        ]
    )
    return md.convert(md_content)


def create_pdf_from_html(html_content, output_path):
    """Buat PDF dari HTML content."""
    # Tambahkan styling CSS dasar
    css = """
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; max-width: 900px; margin: 0 auto; padding: 20px; }
        h1, h2, h3, h4, h5, h6 { color: #333; margin-top: 24px; margin-bottom: 16px; }
        h1 { border-bottom: 2px solid #333; padding-bottom: 10px; }
        h2 { border-bottom: 1px solid #ccc; padding-bottom: 8px; }
        code { background: #f4f4f4; padding: 2px 6px; border-radius: 3px; }
        pre { background: #f4f4f4; padding: 15px; border-radius: 5px; overflow-x: auto; }
        pre code { background: transparent; padding: 0; }
        table { border-collapse: collapse; width: 100%; margin: 16px 0; }
        th, td { border: 1px solid #ddd; padding: 12px; text-align: left; }
        th { background: #f4f4f4; }
        tr:nth-child(even) { background: #f9f9f9; }
        ul, ol { padding-left: 20px; }
        li { margin-bottom: 8px; }
        hr { border: none; border-top: 2px solid #eee; margin: 24px 0; }
        a { color: #3498db; text-decoration: none; }
        a:hover { text-decoration: underline; }
        .toc { background: #f8f9fa; padding: 15px; border-radius: 5px; margin: 20px 0; }
        .toc li { margin: 5px 0; }
    </style>
    """

    full_html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Documentation</title>
    {css}
</head>
<body>
{html_content}
</body>
</html>"""

    try:
        pdfkit.from_string(full_html, output_path)
        return True
    except Exception as e:
        print(f"Error membuat PDF: {e}")
        return False


def main():
    """Main function."""
    # Cari semua file .md di direktori (rekursif)
    base_dir = Path(__file__).parent
    md_files = sorted(base_dir.glob("**/*.md"))

    if not md_files:
        print("Tidak ada file .md ditemukan.")
        return

    print(f"Ditemukan {len(md_files)} file .md:")
    for f in md_files:
        print(f"  - {f.relative_to(base_dir)}")

    # Convert semua md ke HTML dan gabungkan
    combined_html = ""

    for md_file in md_files:
        print(f"\nMengkonversi: {md_file.relative_to(base_dir)}")
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                md_content = f.read()

            html_content = markdown_to_html(md_content)

            # Tambahkan title dan content ke combined HTML
            title = md_file.stem.replace('_', ' ').title()
            combined_html += f"\n<h1>{title}</h1>\n"
            combined_html += html_content
            combined_html += "\n---\n\n"

            print(f"  Selesai: {len(md_content)} bytes -> {len(html_content)} chars HTML")
        except Exception as e:
            print(f"  Error: {e}")

    # Buat PDF
    output_pdf = base_dir / "dokumentasi_web_fundamental.pdf"
    print(f"\nMembuat PDF: {output_pdf}")

    if create_pdf_from_html(combined_html, str(output_pdf)):
        print(f"Sukses! PDF disimpan di: {output_pdf}")
        print(f"Ukuran file: {output_pdf.stat().st_size / 1024:.1f} KB")
    else:
        print("Gagal membuat PDF.")


if __name__ == "__main__":
    main()
