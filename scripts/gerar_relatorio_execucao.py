# -*- coding: utf-8 -*-
"""
GERADOR DETERMINÍSTICO DO RELATÓRIO DE EXECUÇÃO & TELEMETRIA (HTML + MD + PDF VIA TYPST)
Compila o relatório tripartite em output/<slug>/relatorios/ e docs/<slug>/relatorios/:
- Nome do arquivo: DD-MM-YYYY-relatorio-execucao-<slug>.[html|md|pdf]
- Registra Horário Inicial, Final, Duração, LLM, Harness, Tools, Skills, Tokens e Gates.
"""
import sys
import json
import subprocess
from pathlib import Path
from datetime import datetime

def console_utf8():
    if sys.platform == "win32":
        try:
            sys.stdout.reconfigure(encoding="utf-8")
            sys.stderr.reconfigure(encoding="utf-8")
        except Exception:
            pass

console_utf8()

BASE_DIR = Path(__file__).resolve().parent.parent

CSS_RELATORIO = """
  :root {
    --font-sans: "Liberation Sans", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
    --mono: "JetBrains Mono", Menlo, Consolas, monospace;
    --paper: #F8FAFC;
    --surface: #FFFFFF;
    --ink: #0F172A;
    --ink-2: #334155;
    --muted: #64748B;
    --rule: #CBD5E1;
    --rule-soft: #E2E8F0;
    --accent: #0284C7;
    --accent-dark: #0369A1;
    --accent-soft: #E0F2FE;
    --green: #10B981;
    --green-dark: #065F46;
    --green-soft: #D1FAE5;
  }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    font-family: var(--font-sans);
    background: var(--paper);
    color: var(--ink);
    line-height: 1.6;
    padding: 24px 16px 60px;
  }
  .container { max-width: 980px; margin: 0 auto; }
  .header-card {
    background: var(--surface);
    border: 1px solid var(--rule);
    border-radius: 8px;
    padding: 32px;
    margin-bottom: 24px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
  }
  .breadcrumb { font-size: 13px; color: var(--muted); margin-bottom: 12px; }
  .breadcrumb a { color: var(--accent); text-decoration: none; font-weight: 600; }
  .badge-tag {
    display: inline-block;
    padding: 4px 10px;
    font-size: 12px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    border-radius: 4px;
    background: var(--accent-soft);
    color: var(--accent-dark);
    margin-bottom: 12px;
  }
  h1 { font-size: 26px; font-weight: 800; color: var(--ink); margin-bottom: 6px; }
  .deck { font-size: 14.5px; color: var(--ink-2); margin-bottom: 20px; }
  .hero-stats {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
    gap: 12px;
    background: var(--paper);
    padding: 16px;
    border-radius: 6px;
    border: 1px solid var(--rule-soft);
  }
  .stat-item { display: flex; flex-direction: column; }
  .stat-lbl { font-size: 11px; text-transform: uppercase; letter-spacing: 0.05em; color: var(--muted); font-weight: 700; }
  .stat-val { font-size: 14.5px; font-weight: 800; color: var(--ink); }

  .section-card {
    background: var(--surface);
    border: 1px solid var(--rule);
    border-radius: 8px;
    padding: 24px;
    margin-bottom: 20px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
  }
  .section-title { font-size: 18px; font-weight: 800; color: var(--ink); border-bottom: 2px solid var(--rule-soft); padding-bottom: 8px; margin-bottom: 16px; }

  table.data-table { width: 100%; border-collapse: collapse; margin: 12px 0; font-size: 13px; }
  table.data-table th { background: var(--paper); padding: 10px 12px; text-align: left; font-weight: 700; color: var(--ink-2); border-bottom: 2px solid var(--rule); }
  table.data-table td { padding: 10px 12px; border-bottom: 1px solid var(--rule-soft); color: var(--ink-2); }
  .tag-ok { background: var(--green-soft); color: var(--green-dark); font-weight: 700; padding: 2px 6px; border-radius: 3px; font-size: 11px; }
"""

def renderizar_html_relatorio(d: dict) -> str:
    tokens = d["telemetria_tokens"]
    materiais_rows = []
    for m in d["materiais_entregues"]:
        materiais_rows.append(f"""
        <tr>
          <td><strong>{m['tipo']}</strong></td>
          <td><code style="font-family:var(--mono);">{m['nome_arquivo']}</code></td>
          <td><span class="badge-tag" style="margin:0; font-size:10px;">{m['formato']}</span></td>
          <td><a href="{m['caminho_relativo']}" style="color:var(--accent); text-decoration:none; font-weight:600;">Abrir Documento ↗</a></td>
        </tr>
        """)

    gates_rows = []
    for g_id, g_info in d["gates_status"].items():
        gates_rows.append(f"""
        <tr>
          <td><strong>{g_id.upper()}</strong></td>
          <td><span class="tag-ok">{g_info['status']}</span></td>
          <td>{g_info['descricao']}</td>
        </tr>
        """)

    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Relatório de Execução &amp; Telemetria: {d['produto_foco']}</title>
  <style>
{CSS_RELATORIO}
  </style>
</head>
<body>
<div class="container">
  <div class="header-card">
    <div class="breadcrumb">
      <a href="../../listas-open-source/vert-{d['saas_origem']}.html">← Dossiê {d['saas_origem'].title()}</a>
      &nbsp;·&nbsp;
      <a href="../manuais/manual-{d['slug']}-vps-e-uso.html">Manual</a>
      &nbsp;·&nbsp;
      <a href="../trilhas/trilha-{d['slug']}-aprendizado.html">Trilha</a>
    </div>
    <span class="badge-tag">Governança Agêntica · Relatório Oficial de Fechamento</span>
    <h1>Relatório de Execução &amp; Telemetria: {d['produto_foco']}</h1>
    <p class="deck">
      Auditoria de performance, consumo de tokens, ambiente de engenharia e lista de artefatos gerados pelo fluxo determinístico da Fábrica Universal.
    </p>
    <div class="hero-stats">
      <div class="stat-item">
        <span class="stat-lbl">Data &amp; Duração</span>
        <span class="stat-val">{d['data_execucao']} ({d['tempo_total_segundos']}s)</span>
      </div>
      <div class="stat-item">
        <span class="stat-lbl">Horário de Execução</span>
        <span class="stat-val">{d['horario_inicio']} às {d['horario_fim']}</span>
      </div>
      <div class="stat-item">
        <span class="stat-lbl">Tokens Consumidos</span>
        <span class="stat-val">{tokens['tokens_totais']} (In: {tokens['tokens_input']} | Out: {tokens['tokens_output']})</span>
      </div>
      <div class="stat-item">
        <span class="stat-lbl">Economia via Determinismo</span>
        <span class="stat-val" style="color:var(--green);">{tokens['taxa_economia_determinismo']}</span>
      </div>
    </div>
  </div>

  <div class="section-card">
    <h2 class="section-title">1. Ambiente de Engenharia &amp; Orquestração</h2>
    <table class="data-table">
      <tr>
        <th style="width: 25%;">Harness de Execução</th>
        <td>{d['harness_utilizado']}</td>
      </tr>
      <tr>
        <th>Modelo LLM</th>
        <td>{d['llm_utilizada']}</td>
      </tr>
      <tr>
        <th>Tools Acionadas</th>
        <td>{' · '.join(d['tools_utilizadas'])}</td>
      </tr>
      <tr>
        <th>Skills de Economia</th>
        <td>{' · '.join(d['skills_utilizadas'])}</td>
      </tr>
    </table>
  </div>

  <div class="section-card">
    <h2 class="section-title">2. Auditoria dos Gates Mecânicos de Qualidade</h2>
    <table class="data-table">
      <thead>
        <tr>
          <th>Gate</th>
          <th>Status</th>
          <th>Critério de Validação</th>
        </tr>
      </thead>
      <tbody>
        {''.join(gates_rows)}
      </tbody>
    </table>
  </div>

  <div class="section-card">
    <h2 class="section-title">3. Materiais Entregues no Pacote da Ferramenta</h2>
    <table class="data-table">
      <thead>
        <tr>
          <th>Tipo</th>
          <th>Nome do Arquivo</th>
          <th>Formato</th>
          <th>Acesso</th>
        </tr>
      </thead>
      <tbody>
        {''.join(materiais_rows)}
      </tbody>
    </table>
  </div>
</div>
</body>
</html>
"""

def renderizar_markdown_relatorio(d: dict) -> str:
    tokens = d["telemetria_tokens"]
    linhas = [
        f"# Relatório Oficial de Execução & Telemetria: {d['produto_foco']}",
        f"",
        f"> **Data de Emissão:** {d['data_execucao']} | **Horário:** {d['horario_inicio']} às {d['horario_fim']} ({d['tempo_total_segundos']}s)  ",
        f"> **SaaS Origem:** {d['saas_origem'].title()} | **Material Foco:** {d['produto_foco']}  ",
        f"> **Harness:** {d['harness_utilizado']} | **LLM:** {d['llm_utilizada']}",
        f"",
        f"---",
        f"",
        f"## 1. Telemetria de Tokens & Economia",
        f"",
        f"- **Tokens de Entrada (Input):** {tokens['tokens_input']}",
        f"- **Tokens de Saída (Output):** {tokens['tokens_output']}",
        f"- **Tokens Totais Consumidos:** {tokens['tokens_totais']}",
        f"- **Economia via Determinismo (Zero Token):** {tokens['taxa_economia_determinismo']}",
        f"",
        f"## 2. Ambiente de Engenharia & Ferramentas",
        f"",
        f"- **Tools Acionadas:** {', '.join(d['tools_utilizadas'])}",
        f"- **Skills Ativas:** {', '.join(d['skills_utilizadas'])}",
        f"",
        f"## 3. Quadro de Conformidade dos Gates Mecânicos",
        f"",
        f"| Gate | Status | Critério de Validação |",
        f"| :--- | :---: | :--- |"
    ]
    for g_id, g_info in d["gates_status"].items():
        linhas.append(f"| **{g_id.upper()}** | `{g_info['status']}` | {g_info['descricao']} |")

    linhas.extend([
        f"",
        f"## 4. Materiais Entregues no Pacote da Ferramenta",
        f"",
        f"| Tipo | Arquivo | Formato | Caminho |",
        f"| :--- | :--- | :---: | :--- |"
    ])
    for m in d["materiais_entregues"]:
        linhas.append(f"| **{m['tipo']}** | `{m['nome_arquivo']}` | {m['formato']} | [{m['caminho_relativo']}]({m['caminho_relativo']}) |")

    return "\n".join(linhas)

def renderizar_typst_relatorio(d: dict) -> str:
    tokens = d["telemetria_tokens"]

    tools_typ = f"({', '.join(f'\"{t}\"' for t in d['tools_utilizadas'])})"
    skills_typ = f"({', '.join(f'\"{s}\"' for s in d['skills_utilizadas'])})"

    gates_typ = []
    for g_id, g_info in d["gates_status"].items():
        desc_escapada = g_info['descricao'].replace('\"', '\\\"')
        gates_typ.append(f"""(
          nome: "{g_id.upper()}",
          status: "{g_info['status']}",
          descricao: "{desc_escapada}"
        )""")
    gates_str = f"({', '.join(gates_typ)}, )"

    mat_typ = []
    for m in d["materiais_entregues"]:
        mat_typ.append(f"""(
          tipo: "{m['tipo']}",
          nome: "{m['nome_arquivo']}",
          formato: "{m['formato']}",
          pasta: "{m['caminho_relativo'].split('/')[0]}"
        )""")
    mat_str = f"({', '.join(mat_typ)}, )"

    return f"""#import "/scripts/padroes/template_relatorio_execucao.typ": gerar_relatorio_execucao_typst

#gerar_relatorio_execucao_typst(
  produto_foco: "{d['produto_foco']}",
  saas_origem: "{d['saas_origem'].title()}",
  data_execucao: "{d['data_execucao']}",
  horario_inicio: "{d['horario_inicio']}",
  horario_fim: "{d['horario_fim']}",
  tempo_total: "{d['tempo_total_segundos']}s",
  harness: "{d['harness_utilizado']}",
  llm: "{d['llm_utilizada']}",
  tools: {tools_typ},
  skills: {skills_typ},
  tokens_input: "{tokens['tokens_input']}",
  tokens_output: "{tokens['tokens_output']}",
  tokens_total: "{tokens['tokens_totais']}",
  taxa_economia: "{tokens['taxa_economia_determinismo']}",
  materiais: {mat_str},
  gates: {gates_str}
)
"""

def gerar_relatorio_execucao(slug: str, dados_telemetria: dict) -> bool:
    data_str = dados_telemetria["data_execucao"]
    nome_base = f"{data_str}-relatorio-execucao-{slug}"

    out_rel = BASE_DIR / "output" / slug / "relatorios"
    docs_rel = BASE_DIR / "docs" / slug / "relatorios"
    out_rel.mkdir(parents=True, exist_ok=True)
    docs_rel.mkdir(parents=True, exist_ok=True)

    # 1. HTML
    html_content = renderizar_html_relatorio(dados_telemetria)
    (out_rel / f"{nome_base}.html").write_text(html_content, encoding="utf-8")
    (docs_rel / f"{nome_base}.html").write_text(html_content, encoding="utf-8")

    # 2. Markdown
    md_content = renderizar_markdown_relatorio(dados_telemetria)
    (out_rel / f"{nome_base}.md").write_text(md_content, encoding="utf-8")
    (docs_rel / f"{nome_base}.md").write_text(md_content, encoding="utf-8")

    # 3. PDF Typst
    typ_content = renderizar_typst_relatorio(dados_telemetria)
    temp_typ = out_rel / f"{nome_base}.typ"
    temp_typ.write_text(typ_content, encoding="utf-8")
    pdf_out = out_rel / f"{nome_base}.pdf"
    pdf_docs = docs_rel / f"{nome_base}.pdf"

    try:
        res = subprocess.run(
            ["typst", "compile", "--root", str(BASE_DIR), str(temp_typ), str(pdf_out)],
            cwd=str(BASE_DIR),
            capture_output=True,
            text=True
        )
        if res.returncode == 0 and pdf_out.exists():
            pdf_docs.write_bytes(pdf_out.read_bytes())
        else:
            print(f"⚠️ Aviso na compilação do relatório em PDF via Typst: {res.stderr}")
    except Exception as e:
        print(f"⚠️ Erro ao compilar relatório Typst: {e}")

    if temp_typ.exists():
        temp_typ.unlink()

    print(f"📋 Relatório oficial de telemetria emitido: {nome_base}.[html|md|pdf] (em output/{slug}/relatorios/)")
    return True
