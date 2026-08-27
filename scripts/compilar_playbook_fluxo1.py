# -*- coding: utf-8 -*-
"""
COMPILADOR DO PLAYBOOK MESTRE DO FLUXO 1 (LISTAS HORIZONTAIS AIDD)
Compila os 13 módulos do Fluxo 1 em Markdown, HTML e PDF multipáginas via Typst.
"""
import os
import sys
import re
import subprocess
from pathlib import Path

def console_utf8():
    if sys.platform == "win32":
        try:
            sys.stdout.reconfigure(encoding="utf-8")
            sys.stderr.reconfigure(encoding="utf-8")
        except Exception:
            pass

console_utf8()

BASE_DIR = Path(__file__).resolve().parent.parent
ESPEC_DIR = BASE_DIR / "especificacoes" / "fluxo-1-listas-horizontais"
OUTPUT_DIR = BASE_DIR / "especificacoes"
DOCS_DIR = BASE_DIR / "docs" / "especificacoes"
TEMPLATE_PATH = BASE_DIR / "scripts" / "padroes" / "template_playbook_aidd.typ"

META_PROMPT = """# PLAYBOOK MESTRE: LISTAS HORIZONTAIS & COMPÊNDIOS TEMÁTICOS (AIDD)

> **Framework de Mapeamento das 49 Camadas Open Source Globais**  
> **Versão:** 1.0.0 · Padrão Diamante R5 · Nota 10.0 / 10.0  
> **Compatibilidade:** Qualquer LLM e ADE (Orca, Cursor, Claude Code, Windsurf)  
> **Data de Homologação:** 27 de Agosto de 2026

---

## 🤖 META-PROMPT DE INGESTÃO AUTOMÁTICA PARA LLMS

> **INSTRUÇÃO PARA QUALQUER INTELIGÊNCIA ARTIFICIAL QUE RECEBER ESTE DOCUMENTO:**
> 
> Você acaba de receber o **Playbook Mestre de Listas Horizontais (Fluxo 1)**.
> Sua missão é atuar como Engenheiro Agêntico Sênior para mapear e compilar compêndios temáticos de software livre corporativo:
> 1. Estruture a camada com Hero Stats Bar, busca interativa client-side e cards em grid `60px 1fr`;
> 2. Valide licença OSI e repositório oficial de cada ferramenta catalogada;
> 3. Entregue os artefatos de forma determinística nos 3 formatos (HTML, MD e PDF Typst);
> 4. Persista as métricas no banco relacional SQLite `estado_esteira.db`.

---

"""

def compilar_playbook_fluxo1():
    arquivos = sorted(list(ESPEC_DIR.glob("*.md")))
    if not arquivos:
        print("❌ Nenhum arquivo encontrado em especificacoes/fluxo-1-listas-horizontais/")
        return False

    conteudo_md = [META_PROMPT]
    for arq in arquivos:
        texto = arq.read_text(encoding="utf-8")
        conteudo_md.append(f"\n\n<!-- INÍCIO DO MÓDULO: {arq.name} -->\n\n")
        conteudo_md.append(texto)
        conteudo_md.append(f"\n\n<!-- FIM DO MÓDULO: {arq.name} -->\n\n---\n")

    md_final = "\n".join(conteudo_md)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    DOCS_DIR.mkdir(parents=True, exist_ok=True)

    # 1. Salvar Markdown Unificado
    md_path = OUTPUT_DIR / "PLAYBOOK-MESTRE-LISTAS-HORIZONTAIS.md"
    md_path.write_text(md_final, encoding="utf-8")
    print(f"✅ Markdown Mestre salvo: {md_path.name}")

    # 2. Salvar HTML Interativo Diamante com Tabelas & Mermaid
    from renderizador_html_diamante import converter_markdown_para_html_diamante
    html_path = OUTPUT_DIR / "PLAYBOOK-MESTRE-LISTAS-HORIZONTAIS.html"
    html_final = converter_markdown_para_html_diamante(
        md_final,
        "Playbook Mestre: Listas Horizontais & Compêndios Temáticos AIDD",
        BASE_DIR
    )
    html_path.write_text(html_final, encoding="utf-8")
    print(f"✅ HTML Mestre com Tabelas & Mermaid salvo: {html_path.name}")

    # 3. Compilar PDF de Alta Precisão Tipográfica via Typst (Anti-Sobreposição)
    corpo_typ = OUTPUT_DIR / "playbook_f1_corpo.typ"
    completo_typ = OUTPUT_DIR / "playbook_f1_completo.typ"
    pdf_path = OUTPUT_DIR / "PLAYBOOK-MESTRE-LISTAS-HORIZONTAIS.pdf"

    try:
        subprocess.run(
            ["pandoc", str(md_path), "-t", "typst", "-o", str(corpo_typ)],
            cwd=str(BASE_DIR),
            capture_output=True,
            encoding="utf-8",
            errors="replace"
        )

        texto_corpo = corpo_typ.read_text(encoding="utf-8")

        def corrigir_tabela(match):
            cols_str = match.group(1)
            cols = [c.strip() for c in cols_str.split(",") if c.strip()]
            num_cols = len(cols)
            if num_cols == 2:
                return "columns: (1.2fr, 2.8fr)"
            elif num_cols == 3:
                return "columns: (1fr, 1.2fr, 2.5fr)"
            elif num_cols == 4:
                return "columns: (1.3fr, 0.8fr, 2.2fr, 1.5fr)"
            elif num_cols == 5:
                return "columns: (1fr, 1.5fr, 1fr, 2fr, 1fr)"
            else:
                return f"columns: ({', '.join(['1fr']*num_cols)})"

        texto_corpo = re.sub(r'columns:\s*\(([^)]+)\)', corrigir_tabela, texto_corpo)

        template_str = TEMPLATE_PATH.read_text(encoding="utf-8")
        capa_str = """
#align(center)[
  #block(
    fill: rgb("#F1F5F9"),
    inset: (x: 20pt, y: 16pt),
    radius: 6pt,
    stroke: 1.5pt + rgb("#0284C7"),
    width: 100%,
    [
      #text(8.5pt, weight: "bold", fill: rgb("#0369A1"), tracking: 0.12em)[
        DOCUMENTO CANÔNICO DE ENGENHARIA DE SOFTWARE AGÊNTICA
      ]
      #v(5pt)
      #text(17pt, weight: "bold", fill: rgb("#0F172A"))[
        PLAYBOOK MESTRE: LISTAS HORIZONTAIS AIDD
      ]
      #v(4pt)
      #text(9pt, fill: rgb("#475569"))[
        Framework de Mapeamento das 49 Camadas Open Source, Padrão Diamante R5 e Normalização Determinística
      ]
      #v(6pt)
      #text(7.5pt, fill: rgb("#64748B"))[
        Data de Homologação: 27 de Agosto de 2026 · Versão 1.0.0 Diamante · Avaliação: Nota 10.0 / 10.0
      ]
    ]
  )
]
#v(10pt)
"""
        completo_typ.write_text(template_str + "\n" + capa_str + "\n" + texto_corpo, encoding="utf-8")

        res_typst = subprocess.run(
            ["typst", "compile", "--root", str(BASE_DIR), str(completo_typ), str(pdf_path)],
            cwd=str(BASE_DIR),
            capture_output=True,
            encoding="utf-8",
            errors="replace"
        )
        if res_typst.returncode == 0 and pdf_path.exists():
            print(f"✅ PDF Mestre COMPLETO (Fluxo 1) gerado: {pdf_path.name} ({pdf_path.stat().st_size} bytes)")
        else:
            print(f"⚠️ Erro Typst: {res_typst.stderr}")

        if corpo_typ.exists(): corpo_typ.unlink()
        if completo_typ.exists(): completo_typ.unlink()

    except Exception as e:
        print(f"⚠️ Exceção ao compilar PDF: {e}")

    return True

if __name__ == "__main__":
    compilar_playbook_fluxo1()
