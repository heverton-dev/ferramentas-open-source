# -*- coding: utf-8 -*-
"""
GERADOR DETERMINÍSTICO DA TRILHA DE APRENDIZADO AUTOGUIADO (HTML + TYPST PDF + MD)
Lê scripts/data/trilha-<slug>.json e compila nos 3 formatos com paridade de espelho:
- output/trilhas/trilha-<slug>-aprendizado.html e docs/trilhas/
- output/trilhas/trilha-<slug>-aprendizado.md e docs/trilhas/
- output/trilhas/trilha-<slug>-aprendizado.pdf e docs/trilhas/ (via Typst)
"""
import sys
import json
import subprocess
from pathlib import Path
from padroes.template_trilha_aprendizado import renderizar_trilha_html

def console_utf8():
    if sys.platform == "win32":
        try:
            sys.stdout.reconfigure(encoding="utf-8")
            sys.stderr.reconfigure(encoding="utf-8")
        except Exception:
            pass

console_utf8()

BASE_DIR = Path(__file__).resolve().parent.parent

def gerar_markdown_trilha(dados: dict) -> str:
    linhas = [
        f"# Trilha Cronológica de Aprendizado: {dados['produto_foco']}",
        f"",
        f"> **Jornada Pedagógica Autoguiada · Imersão a Partir das Fontes Primárias**  ",
        f"> **Tempo Total Estimado:** {dados['tempo_total_estimado']} | **Fases:** {len(dados['fases'])} Módulos  ",
        f"> **Dossiê SaaS de Origem:** {dados['saas_origem'].title()}",
        f"",
        f"---",
        f""
    ]

    for f in dados["fases"]:
        linhas.append(f"## {f['titulo']} (`⏱️ {f['tempo_estimado']}`)")
        linhas.append(f"**🎯 Meta da Etapa:** {f['objetivo']}\n")
        for r in f["recursos"]:
            linhas.append(f"- [ ] **[{r['titulo']}]({r['url']})** (`{r['tipo_midia']}` - `[{r['fonte_id']}]`)")
            linhas.append(f"  - 💡 **O que você aprende:** {r['aprendizado_chave']}")
            linhas.append(f"  - ⏱️ {r['duracao']} | 👤 {r['autor']}\n")

    return "\n".join(linhas)

def gerar_typst_trilha(dados: dict) -> str:
    fases_typ = []
    for f in dados["fases"]:
        rec_typ = []
        for r in f["recursos"]:
            rec_typ.append(f"""(
              titulo: "{r['titulo']}",
              tipo_midia: "{r['tipo_midia']}",
              fonte_id: "{r['fonte_id']}",
              aprendizado_chave: "{r['aprendizado_chave'].replace('\"', '\\\"')}",
              duracao: "{r['duracao']}",
              autor: "{r['autor']}"
            )""")

        fases_typ.append(f"""(
          titulo: "{f['titulo']}",
          tempo_estimado: "{f['tempo_estimado']}",
          objetivo: "{f['objetivo'].replace('\"', '\\\"')}",
          recursos: ({', '.join(rec_typ)})
        )""")

    return f"""#import "/scripts/padroes/template_trilha_aprendizado.typ": gerar_trilha_typst

#gerar_trilha_typst(
  produto_foco: "{dados['produto_foco']}",
  tempo_total: "{dados['tempo_total_estimado']}",
  fases: ({', '.join(fases_typ)})
)
"""

def compilar_trilha(slug: str) -> bool:
    data_file = BASE_DIR / "scripts" / "data" / f"trilha-{slug}.json"
    if not data_file.exists():
        print(f"❌ Arquivo de dados não encontrado: {data_file}")
        return False

    with open(data_file, "r", encoding="utf-8") as f:
        dados = json.load(f)

    out_dir = BASE_DIR / "output" / "trilhas"
    docs_dir = BASE_DIR / "docs" / "trilhas"
    out_dir.mkdir(parents=True, exist_ok=True)
    docs_dir.mkdir(parents=True, exist_ok=True)

    # 1. HTML Autocontido
    html_content = renderizar_trilha_html(dados)
    html_out = out_dir / f"trilha-{slug}-aprendizado.html"
    html_docs = docs_dir / f"trilha-{slug}-aprendizado.html"
    html_out.write_text(html_content, encoding="utf-8")
    html_docs.write_text(html_content, encoding="utf-8")
    print(f"✅ HTML compilado: {html_out.name} (espelhado em docs/trilhas/)")

    # 2. Markdown
    md_content = gerar_markdown_trilha(dados)
    md_out = out_dir / f"trilha-{slug}-aprendizado.md"
    md_docs = docs_dir / f"trilha-{slug}-aprendizado.md"
    md_out.write_text(md_content, encoding="utf-8")
    md_docs.write_text(md_content, encoding="utf-8")
    print(f"✅ Markdown compilado: {md_out.name} (espelhado em docs/trilhas/)")

    # 3. PDF via Typst
    typ_content = gerar_typst_trilha(dados)
    typ_temp = out_dir / f"trilha-{slug}-aprendizado.typ"
    typ_temp.write_text(typ_content, encoding="utf-8")
    pdf_out = out_dir / f"trilha-{slug}-aprendizado.pdf"
    pdf_docs = docs_dir / f"trilha-{slug}-aprendizado.pdf"

    try:
        res = subprocess.run(
            ["typst", "compile", "--root", str(BASE_DIR), str(typ_temp), str(pdf_out)],
            cwd=str(BASE_DIR),
            capture_output=True,
            text=True
        )
        if res.returncode == 0 and pdf_out.exists():
            pdf_docs.write_bytes(pdf_out.read_bytes())
            print(f"✅ PDF Executivo compilado via Typst: {pdf_out.name} (espelhado em docs/trilhas/)")
        else:
            print(f"⚠️ Aviso na compilação Typst da trilha: {res.stderr}")
    except Exception as e:
        print(f"⚠️ Erro ao invocar Typst: {e}")

    if typ_temp.exists():
        typ_temp.unlink()

    return True

if __name__ == "__main__":
    slug_alvo = sys.argv[1] if len(sys.argv) > 1 else "screenpipe"
    compilar_trilha(slug_alvo)
