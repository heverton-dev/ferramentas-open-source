# -*- coding: utf-8 -*-
"""
COMPILADOR DETERMINÍSTICO DE COMPÊNDIOS TÉCNICOS (PADRÃO DIAMANTE R5)
Gera o HTML final autocontido e ultra-refinado a partir de dados estruturados (JSON).
Elimina 100% das variações e discrepâncias de layout entre diferentes LLMs.
"""
import os
import sys
import json
import re

def console_utf8():
    if sys.platform == "win32":
        try:
            sys.stdout.reconfigure(encoding="utf-8")
            sys.stderr.reconfigure(encoding="utf-8")
        except Exception:
            pass

console_utf8()

CSS_CANONICO_DIAMANTE = """
  :root {
    --font-serif: "Liberation Serif", "Linux Libertine O", "Times New Roman", Times, serif;
    --font-sans: "Liberation Sans", "SF Pro Display", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
    --mono: "JetBrains Mono", "SF Mono", Menlo, Consolas, monospace;
    --paper: #F6F4EF;
    --surface: #FFFFFF;
    --surface-2: #FBF9F4;
    --surface-dark: #0A0F1D;
    --ink: #1B1E23;
    --ink-2: #383D45;
    --muted: #666E7A;
    --rule: #D8D2C4;
    --rule-soft: #EAE5D9;
    --accent: #00875A;
    --accent-dark: #57D9A3;
    --accent-soft: #E3FCEF;
    --accent-soft-dark: #162B22;
    --green: #00875A;
    --green-soft: #E3FCEF;
    --gold: #FFAB00;
    --gold-soft: #FFF0B3;
    --flag: #DE350B;
    --flag-soft: #FFEBE6;
    --shadow: 0 1px 3px rgba(0,0,0,0.04);
  }

  @media (prefers-color-scheme: dark) {
    :root {
      --paper: #0E121B;
      --surface: #141924;
      --surface-2: #1A2130;
      --ink: #E6E8ED;
      --ink-2: #B0B5C0;
      --muted: #7E8695;
      --rule: #262F40;
      --rule-soft: #1E2533;
      --accent: var(--accent-dark);
      --accent-soft: var(--accent-soft-dark);
      --green: #57D9A3;
      --green-soft: #162B22;
      --gold: #FFC400;
      --gold-soft: #332600;
      --flag: #FF7452;
      --flag-soft: #361B15;
      --shadow: 0 1px 3px rgba(0,0,0,0.25);
    }
  }

  *, *::before, *::after { box-sizing: border-box; }
  * { scrollbar-width: thin; scrollbar-color: var(--accent) transparent; }
  ::-webkit-scrollbar { width: 4px; height: 4px; }
  ::-webkit-scrollbar-track { background: transparent; }
  ::-webkit-scrollbar-thumb { background: var(--accent); border-radius: 4px; }

  html { font-size: 16px; scroll-behavior: smooth; }
  body {
    margin: 0; padding: 0;
    background: var(--paper);
    color: var(--ink);
    font-family: var(--font-sans);
    line-height: 1.6;
    -webkit-font-smoothing: antialiased;
  }

  .wrap { max-width: 1180px; margin: 0 auto; padding: 40px 24px 80px; }

  header { margin-bottom: 32px; }
  .header-top { display: flex; align-items: center; justify-content: space-between; gap: 16px; margin-bottom: 16px; flex-wrap: wrap; }
  .back-link { font-family: var(--mono); font-size: 12px; color: var(--muted); text-decoration: none; display: inline-flex; align-items: center; gap: 6px; }
  .back-link:hover { color: var(--accent); }
  .camada-pill { font-family: var(--mono); font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: .08em; padding: 4px 10px; border-radius: 3px; background: var(--accent-soft); color: var(--accent); border: 1px solid var(--accent); }

  .hero { margin: 20px 0 24px; }
  h1 { font-family: var(--font-serif); font-size: clamp(28px, 4.5vw, 42px); line-height: 1.15; letter-spacing: -.02em; margin: 0 0 12px; color: var(--ink); text-align: left; }
  .deck { font-size: 17px; line-height: 1.65; color: var(--ink-2); margin: 0; max-width: 100%; text-align: justify; text-justify: inter-word; }

  .hero-stats {
    display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 12px; margin: 24px 0 32px;
  }
  .stat-card {
    background: var(--surface); border: 1px solid var(--rule); border-radius: 3px;
    padding: 12px 16px; box-shadow: var(--shadow);
  }
  .stat-card .num { font-family: var(--mono); font-size: 22px; font-weight: 700; color: var(--accent); }
  .stat-card .lbl { font-size: 12px; color: var(--muted); text-transform: uppercase; letter-spacing: .05em; font-weight: 600; }

  .grid2 { display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 16px; margin: 24px 0; }
  .route { background: var(--surface); border: 1px solid var(--rule); border-radius: 3px; padding: 18px 20px; }
  .route.red { border-left: 4px solid var(--flag); }
  .route.green { border-left: 4px solid var(--green); }
  .route .tag { font-family: var(--mono); font-size: 10.5px; text-transform: uppercase; letter-spacing: .08em; font-weight: 700; }
  .route.red .tag { color: var(--flag); }
  .route.green .tag { color: var(--green); }
  .route h4 { font-family: var(--font-serif); font-size: 19px; margin: 6px 0 8px; color: var(--ink); }
  .route p { margin: 0; font-size: 14px; color: var(--ink-2); }

  .sec-head { margin: 36px 0 16px; }
  .sec-num { font-family: var(--mono); font-size: 11px; text-transform: uppercase; letter-spacing: .1em; color: var(--muted); font-weight: 600; display: block; }
  h2 { font-family: var(--font-serif); font-size: 26px; margin: 4px 0; color: var(--ink); }
  .sec-note { font-size: 14px; color: var(--muted); margin: 0; }

  .search-wrapper { position: relative; margin: 20px 0 16px; }
  .search-input { width: 100%; padding: 12px 16px 12px 42px; font-family: var(--font-sans); font-size: 14px; background: var(--surface); color: var(--ink); border: 1px solid var(--rule); border-radius: 4px; box-shadow: var(--shadow); outline: none; transition: border-color .15s ease; }
  .search-input:focus { border-color: var(--accent); }
  .search-icon { position: absolute; left: 14px; top: 50%; transform: translateY(-50%); width: 16px; height: 16px; fill: var(--muted); pointer-events: none; }

  .tablewrap { width: 100%; overflow-x: auto; margin: 16px 0 32px; background: var(--surface); border: 1px solid var(--rule); border-radius: 3px; }
  table { width: 100%; border-collapse: collapse; font-size: 13.5px; text-align: left; }
  th { background: var(--surface-2); font-family: var(--mono); font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: .06em; color: var(--muted); padding: 10px 12px; border-bottom: 1px solid var(--rule); }
  td { padding: 10px 12px; border-bottom: 1px solid var(--rule-soft); color: var(--ink-2); }
  tr:last-child td { border-bottom: none; }
  td.rank { font-family: var(--mono); font-weight: 700; color: var(--accent); width: 40px; }
  td.tool a { color: var(--ink); font-weight: 600; text-decoration: none; }
  td.tool a:hover { color: var(--accent); }
  td.saas { color: var(--flag); }
  td.econ { font-family: var(--mono); color: var(--green); font-weight: 600; }
  td.cat { font-size: 12px; color: var(--muted); }
  td.lic { font-family: var(--mono); font-size: 11px; }

  .ledger { display: flex; flex-direction: column; gap: 24px; }
  .entry { background: var(--surface); border: 1px solid var(--rule); border-radius: 3px; box-shadow: var(--shadow); display: grid; grid-template-columns: 60px 1fr; transition: border-color .15s ease, transform .15s ease; }
  .entry:hover { border-color: var(--accent); transform: translateY(-2px); }
  .entry-rank { font-family: var(--mono); font-size: 20px; font-variant-numeric: tabular-nums; color: var(--accent); background: var(--accent-soft); display: flex; align-items: flex-start; justify-content: center; padding: 18px 0; border-right: 1px solid var(--rule); border-radius: 2px 0 0 2px; }
  
  .entry-body { padding: 18px 22px 20px; display: flex; flex-direction: column; gap: 14px; min-width: 0; }
  .entry-top { display: flex; flex-wrap: wrap; align-items: center; gap: 8px 10px; }
  .entry-top h3 { width: 100%; margin: 0 0 4px 0; font-family: var(--font-serif); font-weight: 600; font-size: 24px; line-height: 1.15; letter-spacing: -.01em; color: var(--ink); }

  .senior-badge { font-family: var(--mono); font-size: 10px; letter-spacing: .08em; text-transform: uppercase; padding: 3px 8px; border-radius: 2px; font-weight: 700; }
  .senior-badge.green { background: var(--green-soft); color: var(--green); border: 1px solid color-mix(in srgb, var(--green) 35%, transparent); }
  .killer-badge { font-family: var(--mono); font-size: 10.5px; letter-spacing: .08em; text-transform: uppercase; padding: 3px 8px; border-radius: 2px; background: var(--flag-soft); color: var(--flag); border: 1px solid color-mix(in srgb, var(--flag) 35%, transparent); font-weight: 600; }
  .econ-badge { font-family: var(--mono); font-size: 10.5px; letter-spacing: .08em; text-transform: uppercase; padding: 3px 8px; border-radius: 2px; background: var(--green-soft); color: var(--green); border: 1px solid color-mix(in srgb, var(--green) 35%, transparent); font-weight: 600; }
  .lic-badge { font-family: var(--mono); font-size: 10px; letter-spacing: .08em; text-transform: uppercase; padding: 3px 8px; border-radius: 2px; background: var(--accent-soft); color: var(--accent); border: 1px solid color-mix(in srgb, var(--accent) 35%, transparent); white-space: nowrap; }
  .kind { font-family: var(--mono); font-size: 10px; letter-spacing: .08em; text-transform: uppercase; color: var(--muted); font-weight: 600; padding: 3px 6px; border: 1px solid var(--rule-soft); border-radius: 2px; background: var(--surface-2); }

  .entry-section { display: flex; flex-direction: column; gap: 6px; width: 100%; padding-top: 12px; border-top: 1px dashed var(--rule-soft); }
  .entry-section .label { font-family: var(--mono); font-size: 11px; letter-spacing: .1em; text-transform: uppercase; color: var(--accent); font-weight: 600; }
  .entry-section p { margin: 0; font-size: 14.5px; line-height: 1.55; color: var(--ink-2); text-align: justify; text-justify: inter-word; }

  .code-block { position: relative; background: var(--surface-dark); color: #E6E8ED; padding: 12px 14px; border-radius: 3px; font-family: var(--mono); font-size: 12.5px; overflow-x: auto; margin-top: 4px; }
  .code-block code { font-family: inherit; }
  .copy-btn { position: absolute; top: 6px; right: 6px; background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.2); color: #FFF; font-family: var(--mono); font-size: 10px; padding: 2px 6px; border-radius: 2px; cursor: pointer; }
  .copy-btn:hover { background: var(--accent); border-color: var(--accent); }

  .econ-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 10px; margin-top: 2px; }
  .econ-card { background: var(--surface-2); border: 1px solid var(--rule-soft); border-radius: 2px; padding: 10px 12px; display: flex; flex-direction: column; gap: 2px; }
  .econ-card.highlight { border-left: 3px solid var(--green); background: color-mix(in srgb, var(--green-soft) 25%, var(--surface)); }
  .econ-card.killer { border-left: 3px solid var(--flag); background: color-mix(in srgb, var(--flag-soft) 25%, var(--surface)); }
  .econ-card .card-lbl { font-family: var(--mono); font-size: 10px; text-transform: uppercase; letter-spacing: .08em; color: var(--muted); font-weight: 600; }
  .econ-card .card-val { font-size: 13.5px; font-weight: 600; color: var(--ink); }

  .infra-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 8px; margin-top: 2px; }
  .infra-item { background: var(--surface-2); border: 1px solid var(--rule-soft); border-radius: 2px; padding: 8px 10px; }
  .infra-item .lbl { font-family: var(--mono); font-size: 9.5px; text-transform: uppercase; letter-spacing: .08em; color: var(--muted); display: block; margin-bottom: 2px; }
  .infra-item .val { font-size: 12.5px; font-weight: 600; color: var(--ink); }

  .verdict-box { background: color-mix(in srgb, var(--accent-soft) 35%, var(--surface)); border-left: 3px solid var(--accent); padding: 10px 14px; border-radius: 0 2px 2px 0; margin-top: 6px; }
  .verdict-box .lbl { font-family: var(--mono); font-size: 10px; text-transform: uppercase; letter-spacing: .08em; color: var(--accent); font-weight: 700; display: block; margin-bottom: 2px; }
  .verdict-box p { font-size: 13.5px; line-height: 1.5; color: var(--ink); margin: 0; }

  .how-to-use-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 10px; margin-top: 4px; }
  .step-card { background: var(--surface-2); border: 1px solid var(--rule-soft); border-radius: 3px; padding: 10px 12px; display: flex; flex-direction: column; gap: 4px; }
  .step-card .step-num { font-family: var(--mono); font-size: 11px; font-weight: 700; color: var(--accent); text-transform: uppercase; }
  .step-card .step-title { font-size: 13px; font-weight: 600; color: var(--ink); }
  .step-card p { font-size: 12px; line-height: 1.45; color: var(--ink-2); margin: 0; }
"""

JS_CANONICO_DIAMANTE = """
<script>
function filterTools(query) {
  const q = query.toLowerCase().trim();
  const entries = document.querySelectorAll('.entry');
  const rows = document.querySelectorAll('.tablewrap tbody tr');
  let visibleCount = 0;

  entries.forEach(entry => {
    const text = entry.innerText.toLowerCase();
    if (!q || text.includes(q)) {
      entry.style.display = 'grid';
      visibleCount++;
    } else {
      entry.style.display = 'none';
    }
  });

  rows.forEach(row => {
    const text = row.innerText.toLowerCase();
    if (!q || text.includes(q)) {
      row.style.display = '';
    } else {
      row.style.display = 'none';
    }
  });

  const countEl = document.getElementById('search-count');
  if (countEl) {
    countEl.innerText = q ? `${visibleCount} ferramentas encontradas` : '';
  }
}

function copyCode(btn) {
  const code = btn.parentElement.querySelector('code').innerText;
  navigator.clipboard.writeText(code).then(() => {
    const orig = btn.innerText;
    btn.innerText = 'Copiado!';
    setTimeout(() => btn.innerText = orig, 1500);
  });
}
</script>
"""

def compilar_dossie_diamante(dados: dict) -> str:
    """Gera o HTML completo a partir de um dicionário canônico."""
    num_str = f"{dados['numero']:02d}"
    titulo = dados["titulo"]
    slug = dados["slug"]
    deck = dados["deck"]
    stats = dados.get("stats", {
        "ferramentas": len(dados["ferramentas"]),
        "saas_substituidos": "100%",
        "economia_anual": "R$ 480.000+",
        "licencas": "OSI Compliant"
    })
    rotas = dados.get("rotas", {
        "fragil": {"titulo": "Caminho Proprietário & Frágil", "desc": "Lock-in de fornecedor com custos crescentes por usuário e dependência de nuvem fechada."},
        "soberana": {"titulo": "Caminho Open-Source & Soberano", "desc": "Autonomia de dados, infraestrutura autocontida e economia perpétua de licenciamento."}
    })

    # Renderizar Tabela
    rows_html = ""
    for f in dados["ferramentas"]:
        rank_str = f"{f['rank']:02d}"
        rows_html += f"""        <tr>
          <td class="rank">{rank_str}</td>
          <td class="tool"><a href="#{f['slug']}">{f['nome']}</a></td>
          <td class="saas">{f['saas_substituido']}</td>
          <td class="econ">{f.get('economia_anual_str', 'R$ 24.000/ano')}</td>
          <td class="cat">{f.get('categoria', 'Produtividade')}</td>
          <td class="lic"><span class="lic-badge">{f['licenca_osi']}</span></td>
        </tr>\n"""

    # Renderizar Cards (.entry)
    cards_html = ""
    for f in dados["ferramentas"]:
        rank_str = f"{f['rank']:02d}"
        passos = f.get("passos_praticos", [
            {"passo": 1, "titulo": "Instalação & Configuração", "descricao": "Configuração rápida em container ou CLI local."},
            {"passo": 2, "titulo": "Operação no Dia a Dia", "descricao": "Integração nativa com os fluxos da equipe."},
            {"passo": 3, "titulo": "Entrega & Resultado", "descricao": "Soberania operacional com zero custo de licença."}
        ])

        cards_html += f"""    <div class="entry" id="{f['slug']}">
      <div class="entry-rank">{rank_str}</div>
      <div class="entry-body">
        <div class="entry-top">
          <h3>{f['nome']}</h3>
          <span class="senior-badge green">{f.get('senioridade', 'Pleno')}</span>
          <span class="killer-badge">Substitui: {f['saas_substituido']}</span>
          <span class="econ-badge">Economia: {f.get('economia_anual_str', 'R$ 24.000/ano')}</span>
          <span class="lic-badge">{f['licenca_osi']}</span>
          <span class="kind">{f.get('categoria', 'Open Source')}</span>
        </div>

        <div class="entry-section">
          <span class="label">1. O Que Faz &amp; Como Funciona</span>
          <p><strong>O que faz:</strong> {f['o_que_faz']}</p>
          <p><strong>Como funciona:</strong> {f.get('como_funciona', f['o_que_faz'])}</p>
          <div class="code-block">
            <button class="copy-btn" onclick="copyCode(this)">Copiar</button>
            <code>{f['comando_rapido']}</code>
          </div>
        </div>

        <div class="entry-section">
          <span class="label">2. Análise Econômica &amp; ROI</span>
          <div class="econ-grid">
            <div class="econ-card killer">
              <span class="card-lbl">SaaS Eliminado</span>
              <span class="card-val">{f['saas_substituido']}</span>
            </div>
            <div class="econ-card highlight">
              <span class="card-lbl">Economia Estimada</span>
              <span class="card-val">{f.get('economia_anual_str', 'R$ 24.000/ano')}</span>
            </div>
          </div>
        </div>

        <div class="entry-section">
          <span class="label">3. Requisitos de Infraestrutura &amp; Veredito</span>
          <div class="infra-grid">
            <div class="infra-item">
              <span class="lbl">Consumo de Memória</span>
              <span class="val">{f.get('requisitos_infra', {}).get('ram_minima', '128 MB RAM')}</span>
            </div>
            <div class="infra-item">
              <span class="lbl">Processamento</span>
              <span class="val">{f.get('requisitos_infra', {}).get('cpu_minima', '1 vCPU')}</span>
            </div>
            <div class="infra-item">
              <span class="lbl">Repositório Oficial</span>
              <span class="val"><a href="{f.get('repositorio_github', '#')}" target="_blank" rel="noopener">GitHub</a></span>
            </div>
          </div>
          <div class="verdict-box">
            <span class="lbl">Veredito do Arquiteto</span>
            <p>{f.get('veredito', 'Ferramenta altamente recomendada para soberania operacional.')}</p>
          </div>
        </div>

        <div class="entry-section">
          <span class="label">4. Como Usar no Dia a Dia</span>
          <div class="how-to-use-grid">
            <div class="step-card">
              <span class="step-num">[1] {passos[0]['titulo']}</span>
              <p>{passos[0]['descricao']}</p>
            </div>
            <div class="step-card">
              <span class="step-num">[2] {passos[1]['titulo']}</span>
              <p>{passos[1]['descricao']}</p>
            </div>
            <div class="step-card">
              <span class="step-num">[3] {passos[2]['titulo']}</span>
              <p>{passos[2]['descricao']}</p>
            </div>
          </div>
        </div>
      </div>
    </div>\n"""

    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1" name="viewport"/>
<title>Camada {num_str} · {titulo} · Dossiê Executivo</title>
<style>
{CSS_CANONICO_DIAMANTE}
</style>
</head>
<body>

<div class="wrap">

  <header>
    <div class="header-top">
      <a class="back-link" href="index.html">← Voltar ao Hub Central</a>
      <span class="camada-pill">Camada {num_str} · Arsenal Open Source</span>
    </div>

    <div class="hero">
      <h1>Camada {num_str} · {titulo}</h1>
      <p class="deck">{deck}</p>
    </div>

    <div class="hero-stats">
      <div class="stat-card">
        <div class="num">{stats['ferramentas']}</div>
        <div class="lbl">Ferramentas Mapeadas</div>
      </div>
      <div class="stat-card">
        <div class="num">{stats['saas_substituidos']}</div>
        <div class="lbl">SaaS Substituídos</div>
      </div>
      <div class="stat-card">
        <div class="num">{stats['economia_anual']}</div>
        <div class="lbl">Economia Estimada/Ano</div>
      </div>
      <div class="stat-card">
        <div class="num">{stats['licencas']}</div>
        <div class="lbl">Conformidade OSI</div>
      </div>
    </div>

    <div class="grid2">
      <div class="route red">
        <span class="tag">Rota Frágil (Proprietária)</span>
        <h4>{rotas['fragil']['titulo']}</h4>
        <p>{rotas['fragil']['desc']}</p>
      </div>
      <div class="route green">
        <span class="tag">Rota Soberana (Open Source)</span>
        <h4>{rotas['soberana']['titulo']}</h4>
        <p>{rotas['soberana']['desc']}</p>
      </div>
    </div>
  </header>

  <div class="sec-head">
    <span class="sec-num">Parte 1</span>
    <h2>Matriz Comparativa de Ferramentas</h2>
    <p class="sec-note">Tabela consolidada com todas as 20 ferramentas, licenças e custos comparados.</p>
  </div>

  <div class="tablewrap">
    <table>
      <thead>
        <tr>
          <th>#</th>
          <th>Ferramenta</th>
          <th>SaaS Substituído</th>
          <th>Economia</th>
          <th>Categoria</th>
          <th>Licença</th>
        </tr>
      </thead>
      <tbody>
{rows_html}      </tbody>
    </table>
  </div>

  <div class="sec-head" id="fichas">
    <span class="sec-num">Parte 2</span>
    <h2>Fichas Técnicas &amp; Guias de Adoção</h2>
    <p class="sec-note">Detalhamento técnico, comandos de execução rápida, análise de infraestrutura e passos práticos.</p>
  </div>

  <div class="search-wrapper">
    <input class="search-input" id="search-input" onkeyup="filterTools(this.value)" placeholder="Buscar ferramenta, SaaS substituído, licença ou tecnologia..." type="text"/>
    <svg class="search-icon" viewbox="0 0 24 24"><path d="M15.5 14h-.79l-.28-.27C15.41 12.59 16 11.11 16 9.5 16 5.91 13.09 3 9.5 3S3 5.91 3 9.5 5.91 16 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"></path></svg>
    <div id="search-count" style="margin-top: 6px; font-size: 12px; color: var(--muted); font-family: var(--mono);"></div>
  </div>

  <div class="ledger">
{cards_html}  </div>

</div>

{JS_CANONICO_DIAMANTE}
</body>
</html>
"""
    return html

if __name__ == "__main__":
    if len(sys.argv) > 1:
        json_path = sys.argv[1]
        with open(json_path, "r", encoding="utf-8") as f:
            dados = json.load(f)
        html_out = compilar_dossie_diamante(dados)
        out_file = f"output/listas-open-source/{dados['numero']:02d}-{dados['slug']}.html"
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(html_out)
        print(f"✅ Compêndio compilado com sucesso no Padrão Diamante: {out_file}")
    else:
        print("Uso: python scripts/compilar_compendio_diamante.py <dados.json>")
