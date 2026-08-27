#!/usr/bin/env python3
"""
Converte Markdown para PDF usando reportlab.
Uso: python converter_md_pdf.py <input.md> <output.pdf>
"""
import sys
import os
from pathlib import Path

def md_to_pdf(md_file, pdf_file):
    """Converte MD para PDF usando reportlab."""
    try:
        import subprocess

        # Tenta usar pandoc se disponível
        result = subprocess.run(
            ['pandoc', md_file, '-o', pdf_file, '--from=markdown', '--to=pdf'],
            capture_output=True,
            text=True,
            timeout=30
        )

        if result.returncode == 0:
            return True, "Convertido com pandoc"

    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass

    # Fallback: usar reportlab + markdown parsing manual
    try:
        from reportlab.lib.pagesizes import letter, A4
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.units import inch
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
        from reportlab.lib import colors
        import re

        # Lê o arquivo MD
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Cria o PDF
        doc = SimpleDocTemplate(pdf_file, pagesize=letter,
                              rightMargin=72, leftMargin=72,
                              topMargin=72, bottomMargin=18)

        story = []
        styles = getSampleStyleSheet()

        # Estilos customizados
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=24,
            textColor=colors.HexColor('#333333'),
            spaceAfter=30,
            keepWithNext=True,
        )

        heading1_style = ParagraphStyle(
            'CustomHeading1',
            parent=styles['Heading1'],
            fontSize=16,
            textColor=colors.HexColor('#1a1a1a'),
            spaceAfter=12,
            spaceBefore=12,
            keepWithNext=True,
        )

        heading2_style = ParagraphStyle(
            'CustomHeading2',
            parent=styles['Heading2'],
            fontSize=13,
            textColor=colors.HexColor('#333333'),
            spaceAfter=10,
            spaceBefore=10,
            keepWithNext=True,
        )

        code_style = ParagraphStyle(
            'CodeStyle',
            parent=styles['Normal'],
            fontName='Courier',
            fontSize=8,
            textColor=colors.HexColor('#444444'),
            backColor=colors.HexColor('#f5f5f5'),
            leftIndent=20,
            spaceAfter=6,
        )

        normal_style = ParagraphStyle(
            'CustomNormal',
            parent=styles['Normal'],
            fontSize=10,
            spaceAfter=8,
            alignment=4,  # Justify
        )

        # Parse markdown
        lines = content.split('\n')
        i = 0

        while i < len(lines):
            line = lines[i]

            # Skip empty lines (usa como espaçamento)
            if not line.strip():
                story.append(Spacer(1, 6))
                i += 1
                continue

            # Títulos
            if line.startswith('# '):
                title = line[2:].strip()
                story.append(Paragraph(title, title_style))
                i += 1
                continue

            if line.startswith('## '):
                heading = line[3:].strip()
                story.append(Paragraph(heading, heading1_style))
                i += 1
                continue

            if line.startswith('### '):
                heading = line[4:].strip()
                story.append(Paragraph(heading, heading2_style))
                i += 1
                continue

            # Código
            if line.startswith('```'):
                code_lines = []
                i += 1
                while i < len(lines) and not lines[i].startswith('```'):
                    code_lines.append(lines[i])
                    i += 1

                code_text = '\n'.join(code_lines).strip()
                if code_text:
                    story.append(Paragraph(f"<font face='Courier' size='8'>{code_text.replace('<', '&lt;').replace('>', '&gt;')}</font>", code_style))
                    story.append(Spacer(1, 6))
                i += 1
                continue

            # Linhas de tabela markdown
            if '|' in line:
                # Tenta parser tabela markdown simples
                table_lines = [line]
                i += 1
                while i < len(lines) and '|' in lines[i]:
                    table_lines.append(lines[i])
                    i += 1

                # Parse simples
                rows = []
                for tl in table_lines:
                    if '---' not in tl:
                        cells = [c.strip() for c in tl.split('|') if c.strip()]
                        if cells:
                            rows.append(cells)

                if rows:
                    try:
                        t = Table(rows, colWidths=[1.5*inch]*min(len(rows[0]), 5))
                        t.setStyle(TableStyle([
                            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#cccccc')),
                            ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
                            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                            ('FONTSIZE', (0, 0), (-1, 0), 9),
                            ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
                            ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
                        ]))
                        story.append(t)
                        story.append(Spacer(1, 8))
                    except:
                        pass
                continue

            # Texto normal
            story.append(Paragraph(line.replace('<', '&lt;').replace('>', '&gt;'), normal_style))
            i += 1

        # Adiciona espacamento final
        story.append(Spacer(1, 12))

        # Build PDF
        doc.build(story)
        return True, "Convertido com reportlab"

    except Exception as e:
        return False, str(e)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Uso: python converter_md_pdf.py <input.md> <output.pdf>")
        sys.exit(1)

    md_file = sys.argv[1]
    pdf_file = sys.argv[2]

    if not os.path.exists(md_file):
        print(f"Erro: Arquivo {md_file} não encontrado")
        sys.exit(1)

    success, msg = md_to_pdf(md_file, pdf_file)

    if success:
        print(f"✅ {pdf_file} criado com sucesso ({msg})")
        sys.exit(0)
    else:
        print(f"❌ Erro ao converter: {msg}")
        sys.exit(1)
