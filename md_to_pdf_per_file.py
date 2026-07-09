#!/usr/bin/env python3
"""
Convert setiap file .md menjadi file .pdf terpisah di folder pdf_output/.
Auto-detect markdown parser: markdown (CI) atau markdown-it-py (Termux).
PDF engine: weasyprint.

Usage:
  python3 md_to_pdf_per_file.py
  python3 md_to_pdf_per_file.py --dir bab/           # hanya folder tertentu
  python3 md_to_pdf_per_file.py --output my_pdfs/     # custom output folder
"""

import re
import sys
import argparse
from pathlib import Path
from datetime import datetime

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

CSS = """
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
    }
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
    pre code { background: transparent; padding: 0; border-left: none; }
    table {
        border-collapse: collapse;
        width: 100%;
        margin: 16px 0;
        font-size: 10pt;
        page-break-inside: avoid;
    }
    th, td { border: 1px solid #ddd; padding: 10px 12px; text-align: left; }
    th { background: #ecf0f1; font-weight: bold; }
    tr:nth-child(even) { background: #fafafa; }
    ul, ol { padding-left: 24px; }
    li { margin-bottom: 6px; }
    hr { border: none; border-top: 2px dashed #bdc3c7; margin: 32px 0; }
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


def escape_html_tags_in_text(md_content):
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
    print("Install: pip install markdown  atau  pip install markdown-it-py")
    sys.exit(1)


def render_markdown(parser, parser_type, md_content):
    if parser_type == 'markdown':
        parser.reset()
        return parser.convert(md_content)
    else:
        return parser.render(md_content)


def md_to_pdf(md_path, output_dir, parser, parser_type):
    rel_path = md_path.relative_to(md_path.parents[len(md_path.parents) - 1])
    # Pertahankan struktur folder di output
    pdf_name = md_path.stem + '.pdf'
    pdf_path = output_dir / pdf_name

    raw = md_path.read_text(encoding='utf-8')
    escaped = escape_html_tags_in_text(raw)
    html_body = render_markdown(parser, parser_type, escaped)

    html_full = f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>{md_path.stem}</title>
    {CSS}
</head>
<body>
    <h1 style="page-break-before: avoid;">{md_path.stem.replace('_', ' ').title()}</h1>
    {html_body}
</body>
</html>"""

    try:
        from weasyprint import HTML as WHTML
        WHTML(string=html_full).write_pdf(pdf_path)
        return True, pdf_path
    except ImportError:
        print("  ERROR: weasyprint tidak terinstall. Install: pip install weasyprint")
        sys.exit(1)
    except Exception as e:
        return False, str(e)


def main():
    parser_arg = argparse.ArgumentParser(description='Convert .md files to .pdf per file')
    parser_arg.add_argument('--dir', default='.', help='Direktori sumber .md (default: .)')
    parser_arg.add_argument('--output', default='pdf_output', help='Folder output PDF (default: pdf_output)')
    args = parser_arg.parse_args()

    parser, parser_type = get_markdown_parser()
    print(f"Parser: {parser_type}")

    base_dir = Path(args.dir).resolve()
    output_dir = Path(args.output).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    md_files = sorted(base_dir.glob("**/*.md"))
    # Filter: skip .git, skip file di pdf_output
    md_files = [
        f for f in md_files
        if '.git' not in f.parts
        and output_dir.name not in f.parts
    ]

    if not md_files:
        print("Tidak ada file .md ditemukan.")
        return

    print(f"Mengkonversi {len(md_files)} file .md ke {output_dir}/\n")

    success_count = 0
    fail_list = []

    for f in md_files:
        rel = f.relative_to(base_dir)
        print(f"  {rel} ...", end=" ")
        ok, result = md_to_pdf(f, output_dir, parser, parser_type)
        if ok:
            size_kb = result.stat().st_size / 1024
            print(f"OK ({size_kb:.1f} KB)")
            success_count += 1
        else:
            print(f"GAGAL: {result}")
            fail_list.append((str(rel), result))

    print(f"\n{'='*50}")
    print(f"Selesai: {success_count}/{len(md_files)} berhasil")
    if fail_list:
        print(f"Gagal: {len(fail_list)} file")
        for name, err in fail_list:
            print(f"  - {name}: {err}")
    print(f"Output: {output_dir}/")


if __name__ == "__main__":
    main()
