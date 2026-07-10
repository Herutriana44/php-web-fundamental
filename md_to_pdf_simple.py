#!/usr/bin/env python3
"""
Script convert semua .md ke 1 PDF.
Auto-detect markdown parser: markdown (CI) atau markdown-it-py (Termux).
Untuk PDF: install weasyprint dulu (pip install weasyprint),
atau script akan menyimpan sebagai .html jika weasyprint tidak ada.
"""

import re
import sys
from pathlib import Path
from datetime import datetime

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


def get_markdown_parser():
    """Coba import markdown parser yang tersedia. Return (parser, type_name)."""
    try:
        import markdown
        md = markdown.Markdown(extensions=['extra', 'tables', 'toc', 'fenced_code'])
        return md, 'markdown'
    except ImportError:
        pass

    try:
        from markdown_it import MarkdownIt
        return MarkdownIt(), 'markdown-it-py'
    except ImportError:
        pass

    print("Error: tidak ada markdown parser terinstall.")
    print("Install salah satu:")
    print("  pip install markdown")
    print("  pip install markdown-it-py")
    sys.exit(1)


def render_markdown(parser, parser_type, md_content):
    """Render markdown ke HTML sesuai tipe parser."""
    if parser_type == 'markdown':
        parser.reset()
        return parser.convert(md_content)
    else:
        return parser.render(md_content)


def _natural_sort_key(path):
    """Natural sort key: urutkan by bab number, lalu nomor prefix file, lalu nama."""
    parts = path.parts
    bab_num = 999
    for p in parts:
        m = re.match(r'bab-(\d+)', p)
        if m:
            bab_num = int(m.group(1))
            break

    fname = path.name
    m = re.match(r'(\d+)[-_]?\s*', fname)
    if m:
        file_num = int(m.group(1))
        rest = fname[m.end():]
    else:
        file_num = 999
        rest = fname

    return (bab_num, file_num, rest)


def main():
    parser, parser_type = get_markdown_parser()
    print(f"Menggunakan parser: {parser_type}")

    base_dir = Path(__file__).parent
    all_md = base_dir.glob("**/*.md")

    # Filter: skip file di .git/ dan PDF_CONVERTER, hanya folder bab/
    md_files = [
        f for f in all_md
        if '.git' not in f.parts
        and 'PDF_CONVERTER' not in f.name
        and any(re.match(r'bab-\d+', p) for p in f.parts)
    ]
    md_files.sort(key=_natural_sort_key)

    if not md_files:
        print("Tidak ada file .md ditemukan.")
        return

    print(f"Mengkonversi {len(md_files)} file .md:")
    for f in md_files:
        print(f"  - {f.relative_to(base_dir)}")

    # Gabungkan semua markdown
    combined_md = ""
    for f in md_files:
        rel_path = str(f.relative_to(base_dir))
        print(f"  Memproses: {rel_path}")

        raw = f.read_text(encoding='utf-8')
        escaped = escape_html_tags_in_text(raw)
        combined_md += f"\n\n# {f.stem}\n\n"
        combined_md += escaped
        combined_md += "\n\n---\n\n"

    # Render markdown ke HTML
    print("\nMerender HTML...")
    html_body = render_markdown(parser, parser_type, combined_md)

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

    # Simpan HTML
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    html_path = base_dir / f"dokumentasi_web_fundamental_{timestamp}.html"
    html_path.write_text(html_full, encoding='utf-8')
    print(f"  HTML disimpan: {html_path.name}")

    # Generate PDF dengan weasyprint
    try:
        from weasyprint import HTML as WHTML
        pdf_path = base_dir / f"dokumentasi_web_fundamental_{timestamp}.pdf"
        print("Membuat PDF dengan weasyprint...")
        WHTML(string=html_full).write_pdf(pdf_path)
        size_kb = pdf_path.stat().st_size / 1024
        print(f"  PDF: {pdf_path.name} ({size_kb:.1f} KB)")
    except ImportError:
        print("\nweasyprint tidak terinstall. Hanya HTML yang disimpan.")
        print("Untuk PDF, install: pip install weasyprint")
    except Exception as e:
        print(f"  Error PDF: {e}")


if __name__ == "__main__":
    main()
