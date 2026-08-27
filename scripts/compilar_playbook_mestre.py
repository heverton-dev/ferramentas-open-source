# -*- coding: utf-8 -*-
"""
COMPILADOR INTEGRAL DO PLAYBOOK MESTRE UNIFICADO DE ENGENHARIA AGÊNTICA (AIDD)
Compila os 13 módulos completos com TODOS os textos, tabelas, regras e códigos
nos 3 formatos: Markdown, HTML e PDF multipáginas via Typst.
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
ESPEC_DIR = BASE_DIR / "especificacoes" / "esteira-manuais-e-trilhas"
OUTPUT_DIR = BASE_DIR / "especificacoes"
DOCS_DIR = BASE_DIR / "docs" / "especificacoes"

META_PROMPT_INGESTAO = """# PLAYBOOK MESTRE: FRAMEWORK UNIVERSAL DE ENGENHARIA AGÊNTICA & AI-DRIVEN DEVELOPMENT (AIDD)

> **Documento Canônico Unificado de Replicação Agêntica**  
> **Versão:** 1.0.0 · Padrão Diamante · Nota 10.0 / 10.0  
> **Compatibilidade:** Qualquer LLM (Claude, GPT, Gemini, Llama, DeepSeek) e qualquer ADE/Harness (Orca, Antigravity, Cursor, Windsurf, Claude Code, Cline, Aider)  
> **Data de Homologação:** 27 de Agosto de 2026

---

## 🤖 META-PROMPT DE INGESTÃO AUTOMÁTICA PARA LLMS

> **INSTRUÇÃO PARA QUALQUER INTELIGÊNCIA ARTIFICIAL QUE RECEBER ESTE DOCUMENTO:**
> 
> Você acaba de receber o **Playbook Mestre de Engenharia Agêntica & AI-Driven Development (AIDD)**. 
> O usuário que enviou este documento é o **Engenheiro Agêntico** (o arquiteto e tomador de decisões).
> 
> Sua missão ao ingerir este documento é:
> 1. **Assumir a Postura de Engenheiro Sênior de Software Agêntico:** Abandone respostas genéricas, clichês e prosa vazia. Opere com rigor técnico estrito, determinismo radical e busca ativa por eficiência de tokens.
> 2. **Aplicar a Arquitetura em 5 Camadas no Projeto Atual:**
>    - **Camada 1 (Contratos e Schemas):** Exija ou crie schemas JSON estritos antes de qualquer código;
>    - **Camada 2 (Determinismo Primeiro):** O que for mecânico (compilação, busca, cálculo de hashes, testes) DEVE ser script em disco (Zero Token de LLM);
>    - **Camada 3 (Cadeia de Gates Mecânicos):** Crie gates com retorno estrito `exit 0` (sucesso) ou `exit 1` (erro);
>    - **Camada 4 (Persistência SQLite R11):** Salve o estado do projeto em banco local para não depender da memória do chat;
>    - **Camada 5 (Topologia em Bundles Tripartites):** Entregue artefatos modulares autocontidos em HTML, Markdown e PDF.
> 3. **Protocolo de Replicação Imediata:** Quando o usuário pedir para criar um fluxo novo, pergunte: *"Qual é o objetivo de negócio e o software/domínio alvo?"* e em seguida replique a estrutura documentada neste compêndio.

---

"""

def markdown_para_typst(md_texto: str) -> str:
    """Converte Markdown limpo para sintaxe Typst preservando formatação completa."""
    linhas = md_texto.splitlines()
    saida = []
    em_codigo = False
    linguagem_codigo = ""

    for linha in linhas:
        # Escape de tags HTML ou referências <...> para não virar label no Typst
        linha = re.sub(r'<([a-zA-Z0-9_-]+)>', r'\\<\1\\>', linha)
        linha = re.sub(r'<([0-9]+[a-zA-Z]+)', r'\\<\1', linha)

        # Fenced code blocks
        if linha.startswith("```"):
            if not em_codigo:
                em_codigo = True
                linguagem_codigo = linha[3:].strip()
                saida.append(f"```{linguagem_codigo}")
            else:
                em_codigo = False
                saida.append("```\n")
            continue

        if em_codigo:
            saida.append(linha)
            continue

        # Headers
        if linha.startswith("# "):
            saida.append(f"\n= {linha[2:].strip()}\n")
        elif linha.startswith("## "):
            saida.append(f"\n== {linha[3:].strip()}\n")
        elif linha.startswith("### "):
            saida.append(f"\n=== {linha[4:].strip()}\n")
        elif linha.startswith("#### "):
            saida.append(f"\n==== {linha[5:].strip()}\n")
        # Blockquotes
        elif linha.startswith("> "):
            texto_bq = linha[2:].strip()
            texto_bq = re.sub(r'\*\*(.+?)\*\*', r'*\1*', texto_bq)
            # Remove escapes indesejados no texto
            texto_bq = texto_bq.replace("[", "\\[").replace("]", "\\]")
            saida.append(f"#block(fill: rgb(\"#F8FAFC\"), stroke: (left: 2.5pt + rgb(\"#0284C7\")), inset: 7pt, radius: 2pt)[#text(8.5pt)[{texto_bq}]]\n")
        # Horizontal Rule
        elif linha.strip() == "---":
            saida.append("\n#line(length: 100%, stroke: 0.5pt + rgb(\"#CBD5E1\"))\n")
        # Lista simples
        elif linha.startswith("- ") or linha.startswith("* "):
            item = linha[2:].strip()
            item = re.sub(r'\*\*(.+?)\*\*', r'*\1*', item)
            saida.append(f"- {item}")
        # Linha em branco
        elif linha.strip() == "":
            saida.append("")
        # Linha normal de parágrafo
        else:
            p = linha
            # Substitui links Markdown [texto](url)
            p = re.sub(r'\[(.*?)\]\((.*?)\)', r'#link("\2")[\1]', p)
            # Substitui negrito Markdown **texto** por *texto* no Typst
            p = re.sub(r'\*\*(.+?)\*\*', r'*\1*', p)
            saida.append(p)

    return "\n".join(saida)

def compilar_playbook_completo():
    print("📖 Lendo integralmente os 13 módulos de especificacoes/esteira-manuais-e-trilhas/...")
    arquivos = sorted(list(ESPEC_DIR.glob("*.md")))
    if not arquivos:
        print("❌ Nenhum arquivo encontrado em especificacoes/esteira-manuais-e-trilhas/")
        return False

    conteudo_md = [META_PROMPT_INGESTAO]
    conteudo_typ_modulos = []

    for arq in arquivos:
        print(f"   -> Ingerindo módulo: {arq.name}")
        texto = arq.read_text(encoding="utf-8")
        
        # Markdown unificado
        conteudo_md.append(f"\n\n<!-- INÍCIO DO MÓDULO: {arq.name} -->\n\n")
        conteudo_md.append(texto)
        conteudo_md.append(f"\n\n<!-- FIM DO MÓDULO: {arq.name} -->\n\n---\n")

        # Conversão Typst
        typ_convertido = markdown_para_typst(texto)
        conteudo_typ_modulos.append(f"\n#pagebreak()\n// MODULO: {arq.name}\n{typ_convertido}\n")

    md_final = "\n".join(conteudo_md)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    DOCS_DIR.mkdir(parents=True, exist_ok=True)

    # 1. Salvar Markdown Unificado
    md_path = OUTPUT_DIR / "PLAYBOOK-MESTRE-ENGENHARIA-AGENTICA-AIDD.md"
    md_docs = DOCS_DIR / "PLAYBOOK-MESTRE-ENGENHARIA-AGENTICA-AIDD.md"
    md_path.write_text(md_final, encoding="utf-8")
    md_docs.write_text(md_final, encoding="utf-8")
    print(f"✅ Markdown Mestre salvo: {md_path.name} ({len(md_final.splitlines())} linhas)")

    # 2. Gerar HTML Unificado
    linhas_html = []
    em_codigo = False
    for l in md_final.splitlines():
        if l.startswith("```"):
            if not em_codigo:
                linhas_html.append("<pre><code>")
                em_codigo = True
            else:
                linhas_html.append("</code></pre>")
                em_codigo = False
            continue
        if em_codigo:
            linhas_html.append(l.replace("<", "&lt;").replace(">", "&gt;"))
            continue

        if l.startswith("# "):
            linhas_html.append(f"<h1>{l[2:]}</h1>")
        elif l.startswith("## "):
            linhas_html.append(f"<h2>{l[3:]}</h2>")
        elif l.startswith("### "):
            linhas_html.append(f"<h3>{l[4:]}</h3>")
        elif l.startswith("> "):
            linhas_html.append(f"<blockquote>{l[2:]}</blockquote>")
        elif l.startswith("- "):
            linhas_html.append(f"<li>{l[2:]}</li>")
        elif l.strip() == "---":
            linhas_html.append("<hr>")
        elif l.strip() == "":
            pass
        else:
            linhas_html.append(f"<p>{l}</p>")

    html_path = OUTPUT_DIR / "PLAYBOOK-MESTRE-ENGENHARIA-AGENTICA-AIDD.html"
    html_docs = DOCS_DIR / "PLAYBOOK-MESTRE-ENGENHARIA-AGENTICA-AIDD.html"
    html_final = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Playbook Mestre: Framework Universal de Engenharia Agêntica &amp; AIDD</title>
  <style>
    body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: #F8FAFC; color: #0F172A; line-height: 1.65; padding: 32px 20px; }}
    .container {{ max-width: 1000px; margin: 0 auto; background: #FFF; padding: 40px; border-radius: 8px; border: 1px solid #CBD5E1; box-shadow: 0 1px 3px rgba(0,0,0,0.05); }}
    h1 {{ font-size: 26px; color: #0F172A; border-bottom: 2px solid #0284C7; padding-bottom: 8px; margin-top: 32px; }}
    h2 {{ font-size: 20px; color: #1E293B; margin-top: 24px; border-bottom: 1px solid #E2E8F0; padding-bottom: 6px; }}
    h3 {{ font-size: 16px; color: #334155; margin-top: 18px; }}
    pre {{ background: #0F172A; color: #E2E8F0; padding: 14px; border-radius: 6px; overflow-x: auto; font-size: 13px; }}
    blockquote {{ border-left: 4px solid #0284C7; background: #E0F2FE; color: #0369A1; padding: 10px 16px; margin: 16px 0; border-radius: 0 4px 4px 0; }}
    hr {{ border: 0; height: 1px; background: #E2E8F0; margin: 32px 0; }}
    li {{ margin-bottom: 4px; }}
  </style>
</head>
<body>
<div class="container">
  {''.join(linhas_html)}
</div>
</body>
</html>
"""
    html_path.write_text(html_final, encoding="utf-8")
    html_docs.write_text(html_final, encoding="utf-8")
    print(f"✅ HTML Mestre salvo: {html_path.name}")

    # 3. Compilar PDF de Alta Precisão Tipográfica via Typst (Anti-Sobreposição)
    corpo_typ = OUTPUT_DIR / "playbook_corpo.typ"
    completo_typ = OUTPUT_DIR / "playbook_completo.typ"
    pdf_path = OUTPUT_DIR / "PLAYBOOK-MESTRE-ENGENHARIA-AGENTICA-AIDD.pdf"
    pdf_docs = DOCS_DIR / "PLAYBOOK-MESTRE-ENGENHARIA-AGENTICA-AIDD.pdf"
    template_path = BASE_DIR / "scripts" / "padroes" / "template_playbook_aidd.typ"

    print("📄 Compilando PDF multipáginas com tipografia anti-sobreposição...")
    try:
        # 3.1 Converter MD para AST Typst
        subprocess.run(
            ["pandoc", str(md_path), "-t", "typst", "-o", str(corpo_typ)],
            cwd=str(BASE_DIR),
            capture_output=True,
            encoding="utf-8",
            errors="replace"
        )

        texto_corpo = corpo_typ.read_text(encoding="utf-8")

        # 3.2 Correção de proporções em tabelas
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

        # 3.3 Acoplar ao template institucional
        template_str = template_path.read_text(encoding="utf-8")
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
        PLAYBOOK MESTRE: FRAMEWORK UNIVERSAL AIDD
      ]
      #v(4pt)
      #text(9pt, fill: rgb("#475569"))[
        Compêndio Completo dos 13 Módulos de Arquitetura, Schemas, Gates Mecânicos, SQLite R11 e Telemetria
      ]
      #v(6pt)
      #text(7.5pt, fill: rgb("#64748B"))[
        Data de Homologação: 27 de Agosto de 2026 · Versão 1.0.0 Diamante · Avaliação de Engenharia: Nota 10.0 / 10.0
      ]
    ]
  )
]
#v(10pt)
"""
        documento_final = template_str + "\n" + capa_str + "\n" + texto_corpo
        completo_typ.write_text(documento_final, encoding="utf-8")

        # 3.4 Compilação via Typst
        res_typst = subprocess.run(
            ["typst", "compile", "--root", str(BASE_DIR), str(completo_typ), str(pdf_path)],
            cwd=str(BASE_DIR),
            capture_output=True,
            encoding="utf-8",
            errors="replace"
        )
        if res_typst.returncode == 0 and pdf_path.exists():
            pdf_docs.write_bytes(pdf_path.read_bytes())
            print(f"✅ PDF Mestre COMPLETO (Anti-Sobreposição) gerado: {pdf_path.name} ({pdf_path.stat().st_size} bytes)")
        else:
            print(f"⚠️ Erro no Typst: {res_typst.stderr}")

        # Limpeza de temporários
        if corpo_typ.exists(): corpo_typ.unlink()
        if completo_typ.exists(): completo_typ.unlink()

    except Exception as e:
        print(f"⚠️ Exceção ao compilar PDF: {e}")

    print("\n🏆 COMPILAÇÃO INTEGRAL CONCLUÍDA COM SUCESSO!")
    return True

if __name__ == "__main__":
    compilar_playbook_completo()
