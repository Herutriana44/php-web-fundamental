#!/usr/bin/env python3
"""
Script untuk convert semua file .md di direktori menjadi 1 file PDF secara berurutan.

Pilihan 1 (Recommended): pip install markdown pdfkit
  - Memerlukan wkhtmltopdf (install via: apt install wkhtmltopdf)

Pilihan 2: pip install pypandoc
  - Memerlukan pandoc (install via: apt install pandoc)

Pilihan 3: pip install markdown2 weasyprint
  - Pure Python, tidak memerlukan binary eksternal
"""

import os
import re
import sys
import tempfile
from pathlib import Path
from datetime import datetime

# Pilih method (ganti ke 'pypandoc' atau 'weasyprint' jika pdfkit tidak bekerja)
METHOD = 'pdfkit'  # 'pdfkit', 'pypandoc', 'weasyprint'

# HTML tags yang sering muncul sebagai referensi kode di teks (bukan HTML asli)
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
    """Escape raw HTML tags yang muncul sebagai teks referensi di luar code block."""
    lines = md_content.split('\n')
    result_lines = []
    in_code_block = False

    for line in lines:
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            result_lines.append(line)
            continue

        if in_code_block:
            result_lines.append(line)
            continue

        for tag in HTML_TAGS_IN_TEXT:
            pattern = r'(?<!`)(' + re.escape(f'<{tag}>') + r')(?!`)'
            line = re.sub(pattern, r'`\1`', line)

        result_lines.append(line)

    return '\n'.join(result_lines)


def get_md_files(base_dir):
    """Dapatkan semua file .md secara rekursif, diurutkan."""
    md_files = sorted(base_dir.glob("**/*.md"))
    return md_files


def markdown_to_html_pypandoc(md_content, output_html):
    """Convert markdown ke HTML menggunakan pypandoc."""
    try:
        import pypandoc
        pypandoc.convert_text(md_content, 'html', format='md',
                              outputfile=str(output_html),
                              extra_args=['--standalone', '--toc', '--css=github.css'])
        return True
    except ImportError:
        print("Error: pypandoc tidak terinstall. Install dengan: pip install pypandoc")
        return False
    except Exception as e:
        print(f"Error pypandoc: {e}")
        return False


def markdown_to_html_weasyprint(md_content, output_html):
    """Convert markdown ke HTML lalu ke PDF menggunakan weasyprint."""
    try:
        import markdown
        from weasyprint import HTML

        md = markdown.Markdown(
            extensions=['extra', 'codehilite', 'toc', 'tables']
        )
        html_content = md.convert(md_content)

        # Tambahkan CSS
        css = """
        <style>
            body { font-family: DejaVu Sans, Arial, sans-serif; line-height: 1.6; max-width: 900px; margin: 0 auto; padding: 20px; }
            h1, h2, h3, h4, h5, h6 { color: #333; margin-top: 24px; margin-bottom: 16px; }
            h1 { border-bottom: 2px solid #333; padding-bottom: 10px; page-break-after: avoid; }
            h2 { border-bottom: 1px solid #ccc; padding-bottom: 8px; page-break-after: avoid; }
            code { background: #f4f4f4; padding: 2px 6px; border-radius: 3px; font-family: DejaVu Sans Mono, monospace; }
            pre { background: #f4f4f4; padding: 15px; border-radius: 5px; overflow-x: auto; font-family: DejaVu Sans Mono, monospace; }
            pre code { background: transparent; padding: 0; }
            table { border-collapse: collapse; width: 100%; margin: 16px 0; }
            th, td { border: 1px solid #ddd; padding: 12px; text-align: left; }
            th { background: #f4f4f4; }
            tr:nth-child(even) { background: #f9f9f9; }
            ul, ol { padding-left: 20px; }
            li { margin-bottom: 8px; }
            hr { border: none; border-top: 2px solid #eee; margin: 24px 0; }
            a { color: #3498db; text-decoration: none; }
            .toc { background: #f8f9fa; padding: 15px; border-radius: 5px; margin: 20px 0; }
            @page { margin: 1in; }
            .page-break { page-break-before: always; }
        </style>
        """

        full_html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    {css}
</head>
<body>
{html_content}
</body>
</html>"""

        with open(output_html, 'w', encoding='utf-8') as f:
            f.write(full_html)
        return True
    except ImportError:
        print("Error: weasyprint tidak terinstall. Install dengan: pip install weasyprint")
        return False
    except Exception as e:
        print(f"Error weasyprint: {e}")
        return False


def markdown_to_html_pdfkit(md_content, output_html):
    """Convert markdown ke HTML menggunakan pdfkit."""
    try:
        import markdown

        md = markdown.Markdown(
            extensions=['extra', 'codehilite', 'toc', 'tables', 'nl2br']
        )
        html_content = md.convert(md_content)

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
            @page { margin: 1in; }
        </style>
        """

        full_html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    {css}
</head>
<body>
{html_content}
</body>
</html>"""

        with open(output_html, 'w', encoding='utf-8') as f:
            f.write(full_html)
        return True
    except ImportError:
        print("Error: markdown tidak terinstall. Install dengan: pip install markdown")
        return False
    except Exception as e:
        print(f"Error pdfkit: {e}")
        return False


def html_to_pdf_pypandoc(html_file, output_pdf):
    """Convert HTML ke PDF menggunakan pypandoc."""
    try:
        import pypandoc
        pypandoc.convert_file(str(html_file), 'pdf', outputfile=str(output_pdf))
        return True
    except Exception as e:
        print(f"Error pypandoc to pdf: {e}")
        return False


def html_to_pdf_weasyprint(html_file, output_pdf):
    """Convert HTML ke PDF menggunakan weasyprint."""
    try:
        from weasyprint import HTML
        HTML(str(html_file)).write_pdf(str(output_pdf))
        return True
    except Exception as e:
        print(f"Error weasyprint to pdf: {e}")
        return False


def html_to_pdf_pdfkit(html_file, output_pdf):
    """Convert HTML ke PDF menggunakan pdfkit."""
    try:
        import pdfkit
        pdfkit.from_file(str(html_file), str(output_pdf))
        return True
    except Exception as e:
        print(f"Error pdfkit to pdf: {e}")
        return False


def create_toc(md_files, base_dir):
    """Buat Daftar Isi HTML."""
    toc = "<h1>Daftar Isi</h1>\n<ul>\n"
    for i, md_file in enumerate(md_files, 1):
        title = md_file.stem.replace('_', ' ').title()
        relative_path = md_file.relative_to(base_dir)
        toc += f"<li><a href='#file-{i}'>{title} ({relative_path})</a></li>\n"
    toc += "</ul>\n---\n"
    return toc


def main():
    """Main function."""
    base_dir = Path(__file__).parent
    md_files = get_md_files(base_dir)

    if not md_files:
        print("Tidak ada file .md ditemukan.")
        return

    print(f"Ditemukan {len(md_files)} file .md:")
    for f in md_files:
        print(f"  {f.relative_to(base_dir)}")

    # Buat daftar isi
    toc_html = create_toc(md_files, base_dir)

    # Convert semua md ke HTML
    combined_html = toc_html

    for i, md_file in enumerate(md_files, 1):
        print(f"\nMengkonversi: {md_file.relative_to(base_dir)}")
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                md_content = f.read()

            md_content = escape_html_tags_in_text(md_content)

            # Tambahkan anchor untuk setiap file
            title = md_file.stem.replace('_', ' ').title()
            combined_html += f'<h1 id="file-{i}">{title}</h1>\n'
            combined_html += md_content + "\n\n---\n\n"

            print(f"  Selesai: {len(md_content)} bytes")
        except Exception as e:
            print(f"  Error: {e}")

    # Simpan combined HTML ke file sementara
    with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False, encoding='utf-8') as tmp_html:
        tmp_html_path = Path(tmp_html.name)

        # Tambahkan CSS dan struktur HTML lengkap
        css = """
        <style>
            body { font-family: Arial, sans-serif; line-height: 1.6; max-width: 900px; margin: 0 auto; padding: 20px; }
            h1, h2, h3, h4, h5, h6 { color: #333; margin-top: 24px; margin-bottom: 16px; }
            h1 { border-bottom: 2px solid #333; padding-bottom: 10px; page-break-after: avoid; }
            h2 { border-bottom: 1px solid #ccc; padding-bottom: 8px; page-break-after: avoid; }
            code { background: #f4f4f4; padding: 2px 6px; border-radius: 3px; font-family: monospace; }
            pre { background: #f4f4f4; padding: 15px; border-radius: 5px; overflow-x: auto; font-family: monospace; }
            pre code { background: transparent; padding: 0; }
            table { border-collapse: collapse; width: 100%; margin: 16px 0; }
            th, td { border: 1px solid #ddd; padding: 12px; text-align: left; }
            th { background: #f4f4f4; }
            tr:nth-child(even) { background: #f9f9f9; }
            ul, ol {{ padding-left: 20px; }}
            li {{ margin-bottom: 8px; }}
            hr {{ border: none; border-top: 2px solid #eee; margin: 24px 0; }}
            a {{ color: #3498db; text-decoration: none; }}
            .page-break {{ page-break-before: always; }}
            @page { margin: 1in; }
            .header { text-align: center; font-size: 12px; color: #666; border-bottom: 1px solid #ccc; padding-bottom: 10px; }
            .footer { text-align: center; font-size: 10px; color: #999; border-top: 1px solid #ccc; padding-top: 10px; }
        </style>
        """

        # Convert markdown to HTML
        if METHOD == 'pdfkit':
            markdown_to_html_pdfkit(combined_html, tmp_html_path)
        elif METHOD == 'pypandoc':
            markdown_to_html_pypandoc(combined_html, tmp_html_path)
        else:
            markdown_to_html_weasyprint(combined_html, tmp_html_path)

    # Convert HTML ke PDF
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_pdf = base_dir / f"dokumentasi_web_fundamental_{timestamp}.pdf"

    print(f"\nMembuat PDF: {output_pdf}")

    if METHOD == 'pdfkit':
        success = html_to_pdf_pdfkit(tmp_html_path, output_pdf)
    elif METHOD == 'pypandoc':
        success = html_to_pdf_pypandoc(tmp_html_path, output_pdf)
    else:
        success = html_to_pdf_weasyprint(tmp_html_path, output_pdf)

    # Hapus file sementara
    tmp_html_path.unlink(missing_ok=True)

    if success:
        print(f"\nSukses! PDF disimpan di: {output_pdf}")
        pdf_size = output_pdf.stat().st_size / 1024
        print(f"Ukuran file: {pdf_size:.1f} KB")
    else:
        print("\nGagal membuat PDF.")


if __name__ == "__main__":
    main()
