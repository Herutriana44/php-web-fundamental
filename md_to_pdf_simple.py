#!/usr/bin/env python3
"""
Script sederhana untuk convert semua .md ke 1 PDF.
Cocok untuk Termux. Install: pip install markdown weasyprint
"""

import sys
from pathlib import Path
from datetime import datetime

def main():
    try:
        import markdown
        from weasyprint import HTML, CSS
    except ImportError as e:
        print(f"Error: {e}")
        print("\nInstall dulu:")
        print("  pip install markdown weasyprint")
        sys.exit(1)

    base_dir = Path(__file__).parent
    md_files = sorted(base_dir.glob("**/*.md"))

    # Filter out converter README
    md_files = [f for f in md_files if 'PDF_CONVERTER' not in f.name]

    if not md_files:
        print("Tidak ada file .md")
        return

    print(f"Mengkonversi {len(md_files)} file:")

    # Gabungkan semua markdown
    combined = ""
    for f in md_files:
        print(f"  • {f.relative_to(base_dir)}")
        combined += f"\n\n# {f.stem}\n\n"
        combined += f.read_text(encoding='utf-8')
        combined += "\n\n---\n\n"

    # Convert markdown ke HTML
    md = markdown.Markdown(extensions=['extra', 'tables', 'toc', 'fenced_code'])
    html_body = md.convert(combined)

    # CSS styling
    css = CSS(string="""
        @page { margin: 1in; }
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            font-size: 11pt;
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
            margin-top: 20px;
            page-break-after: avoid;
        }
        h3 { color: #555; margin-top: 16px; }
        code {
            background: #f4f4f4;
            padding: 2px 5px;
            border-radius: 3px;
            font-family: monospace;
        }
        pre {
            background: #f8f8f8;
            padding: 12px;
            border-left: 3px solid #3498db;
            overflow-x: auto;
            font-size: 9pt;
        }
        table {
            border-collapse: collapse;
            width: 100%;
            margin: 15px 0;
            font-size: 10pt;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 10px;
            text-align: left;
        }
        th { background: #ecf0f1; font-weight: bold; }
        tr:nth-child(even) { background: #f9f9f9; }
        ul, ol { padding-left: 25px; }
        li { margin-bottom: 5px; }
        hr {
            border: none;
            border-top: 2px dashed #bdc3c7;
            margin: 30px 0;
        }
    """)

    # HTML lengkap
    html_full = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Dokumentasi Web Fundamental</title>
</head>
<body>
    <h1 style="text-align: center; color: #3498db;">Dokumentasi Web Fundamental</h1>
    <p style="text-align: center; color: #7f8c8d;">Generated on {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
    <hr>
    {html_body}
</body>
</html>"""

    # Generate PDF
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output = base_dir / f"dokumentasi_web_fundamental_{timestamp}.pdf"

    print(f"\nMembuat PDF...")
    HTML(string=html_full).write_pdf(output, stylesheets=[css])

    size_kb = output.stat().st_size / 1024
    print(f"✓ Selesai: {output.name}")
    print(f"  Ukuran: {size_kb:.1f} KB")

if __name__ == "__main__":
    main()
