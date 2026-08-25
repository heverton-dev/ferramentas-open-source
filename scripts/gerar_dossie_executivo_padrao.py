# -*- coding: utf-8 -*-
"""
Compilador Oficial do Padrão Dossiê Executivo (Regra R5 do AGENTS.md).
Gera HTML 100% em conformidade com:
1. Header com Hero Stats Bar e âncoras rápidas;
2. Título H1 e Deck justificados;
3. Tabela de dados fluida sem scroll horizontal;
4. Cards verticais de largura total (.ledger / .entry) com as 4 seções padronizadas:
   - 1. O Que Faz & Como Funciona (com bloco de código e botão Copiar);
   - 2. Análise Econômica (.econ-grid);
   - 3. Requisitos de Infraestrutura & Veredito (.infra-grid com botão GitHub);
   - 4. Como Usar no Dia a Dia (.steps-grid com mini-cards visuais de passos práticos).
5. Zero div.cols espremido.
"""

import sys
from pathlib import Path

# Garantir UTF-8 no Windows (Regra R11)
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

from dados_30_listas_expandidas import TODAS_AS_30_LISTAS

def renderizar_dossie_r5(dados):
    slug = dados["slug"]
    title = dados["title"]
    camada = dados["camada"]
    deck = dados["deck"]
    accent = dados["accent"]
    accent_dark = dados["accent_dark"]
    accent_soft = dados["accent_soft"]
    accent_soft_dark = dados["accent_soft_dark"]
    pilar_1 = dados["pilar_1"]
    pilar_1_desc = dados["pilar_1_desc"]
    pilar_2 = dados["pilar_2"]
    pilar_2_desc = dados["pilar_2_desc"]
    itens = dados["itens"]
    total = len(itens)

    # Montar linhas da tabela
    tabela_rows = []
    for it in itens:
        tabela_rows.append(f"""          <tr>
            <td class="rank">{it['rank']}</td>
            <td class="tool"><a href="#card-{it['rank']}">{it['name']}</a></td>
            <td class="saas">{it['substitui']}</td>
            <td class="econ">{it['econ']}</td>
            <td class="cat">{it['cat']}</td>
            <td class="lic">{it['lic']}</td>
          </tr>""")
    tabela_html = "\n".join(tabela_rows)

    # Montar cards verticais
    cards_html = []
    for it in itens:
        passos_raw = it.get("como_usar", "").split("<br>")
        passos_cards = []
        for p_idx, p_text in enumerate(passos_raw, start=1):
            if p_text.strip():
                clean_p = p_text.strip()
                if clean_p.startswith(f"{p_idx}."):
                    clean_p = clean_p[2:].strip()
                passos_cards.append(f"""            <div class="step-card">
              <div class="step-head"><span class="step-badge">Passo {p_idx:02d}</span> Fluxo</div>
              <p>{clean_p}</p>
            </div>""")
        passos_grid_html = "\n".join(passos_cards)

        repo_link = it.get("repo", "github.com")
        if not repo_link.startswith("http"):
            repo_url = f"https://{repo_link}"
        else:
            repo_url = repo_link

        cards_html.append(f"""      <article class="entry" id="card-{it['rank']}">
        <div class="entry-rank">{it['rank']}</div>
        <div class="entry-body">
          <div class="entry-top">
            <h3>{it['name']}</h3>
            <span class="senior-badge green">OFICIAL & TESTADO</span>
            <span class="killer-badge">SUBSTITUI: {it['substitui']}</span>
            <span class="econ-badge">{it['econ']}</span>
            <span class="lic-badge">{it['lic']}</span>
            <span class="kind">{it['cat']}</span>
          </div>

          <!-- SEÇÃO 1: O QUE FAZ & COMO FUNCIONA -->
          <div class="entry-section">
            <span class="label">1. O Que Faz & Como Funciona</span>
            <p><strong>Definição Operacional:</strong> {it['entrega']}</p>
            <p><strong>Mecânica Interna & Arquitetura:</strong> {it['mecanica']}</p>
            <div class="code-box">
              <pre><code>{it['cmd']}</code></pre>
              <button class="copy-btn" onclick="copyCode(this)">Copiar</button>
            </div>
          </div>

          <!-- SEÇÃO 2: ANÁLISE ECONÔMICA -->
          <div class="entry-section">
            <span class="label">2. Análise Econômica & Impacto Financeiro</span>
            <div class="econ-grid">
              <div class="econ-card killer">
                <span class="econ-lbl">SaaS Proprietário Substituído</span>
                <span class="econ-val"><strong>{it['substitui']}</strong></span>
              </div>
              <div class="econ-card highlight">
                <span class="econ-lbl">Economia Declarada & ROI</span>
                <span class="econ-val"><strong>{it['econ']}</strong></span>
              </div>
            </div>
          </div>

          <!-- SEÇÃO 3: REQUISITOS DE INFRAESTRUTURA & VEREDITO -->
          <div class="entry-section">
            <span class="label">3. Requisitos de Infraestrutura & Veredito Técnico</span>
            <div class="infra-grid">
              <div class="infra-card">
                <span class="infra-lbl">Consumo de Recursos & Hardware</span>
                <span class="infra-val">{it['spec']}</span>
              </div>
              <div class="infra-card verdict">
                <span class="infra-lbl">Por Que é Ouro / Veredito</span>
                <p>{it['truth']}</p>
              </div>
            </div>
            <div style="margin-top:4px;">
              <a class="repo-btn" href="{repo_url}" target="_blank" rel="noopener noreferrer">
                <svg viewBox="0 0 16 16"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path></svg>
                Acessar Repositório Oficial no GitHub ({repo_link})
              </a>
            </div>
          </div>

          <!-- SEÇÃO 4: COMO USAR NO DIA A DIA -->
          <div class="entry-section">
            <span class="label">4. Como Usar no Dia a Dia (Guia Prático)</span>
            <div class="steps-grid">
{passos_grid_html}
            </div>
          </div>
        </div>
      </article>""")
    cards_bloco_html = "\n\n".join(cards_html)

    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{camada} · Dossiê Executivo</title>
<style>
  :root {{
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
    --accent: {accent};
    --accent-dark: {accent_dark};
    --accent-soft: {accent_soft};
    --accent-soft-dark: {accent_soft_dark};
    --green: #00875A;
    --green-soft: #E3FCEF;
    --gold: #FFAB00;
    --gold-soft: #FFF0B3;
    --flag: #DE350B;
    --flag-soft: #FFEBE6;
    --shadow: 0 1px 3px rgba(0,0,0,0.04);
  }}

  @media (prefers-color-scheme: dark) {{
    :root {{
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
    }}
  }}

  *, *::before, *::after {{ box-sizing: border-box; }}
  html {{ font-size: 16px; scroll-behavior: smooth; }}
  body {{
    margin: 0; padding: 0;
    background: var(--paper);
    color: var(--ink);
    font-family: var(--font-sans);
    line-height: 1.6;
    -webkit-font-smoothing: antialiased;
  }}

  .wrap {{ max-width: 1180px; margin: 0 auto; padding: 40px 24px 80px; }}

  /* HEADER & HERO STATS */
  header {{ margin-bottom: 32px; }}
  .header-top {{ display: flex; align-items: center; justify-content: space-between; gap: 16px; margin-bottom: 16px; flex-wrap: wrap; }}
  .back-link {{ font-family: var(--mono); font-size: 12px; color: var(--muted); text-decoration: none; display: inline-flex; align-items: center; gap: 6px; }}
  .back-link:hover {{ color: var(--accent); }}
  .camada-pill {{ font-family: var(--mono); font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: .08em; padding: 4px 10px; border-radius: 3px; background: var(--accent-soft); color: var(--accent); border: 1px solid var(--accent); }}

  .hero {{ margin: 20px 0 24px; }}
  h1 {{ font-family: var(--font-serif); font-size: clamp(28px, 4.5vw, 42px); line-height: 1.15; letter-spacing: -.02em; margin: 0 0 12px; color: var(--ink); text-align: justify; text-justify: inter-word; }}
  .deck {{ font-size: 17px; line-height: 1.65; color: var(--ink-2); margin: 0; max-width: 100%; text-align: justify; text-justify: inter-word; }}

  .hero-stats {{
    display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 12px; margin: 24px 0 32px;
  }}
  .stat-card {{
    background: var(--surface); border: 1px solid var(--rule); border-radius: 3px;
    padding: 12px 16px; box-shadow: var(--shadow);
  }}
  .stat-card .num {{ font-family: var(--mono); font-size: 22px; font-weight: 700; color: var(--accent); }}
  .stat-card .lbl {{ font-size: 12px; color: var(--muted); text-transform: uppercase; letter-spacing: .05em; font-weight: 600; }}

  /* PILARES */
  .grid2 {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 16px; margin: 24px 0; }}
  .route {{ background: var(--surface); border: 1px solid var(--rule); border-radius: 3px; padding: 18px 20px; }}
  .route.red {{ border-left: 4px solid var(--flag); }}
  .route.green {{ border-left: 4px solid var(--green); }}
  .route .tag {{ font-family: var(--mono); font-size: 10.5px; text-transform: uppercase; letter-spacing: .08em; font-weight: 700; }}
  .route.red .tag {{ color: var(--flag); }}
  .route.green .tag {{ color: var(--green); }}
  .route h4 {{ font-family: var(--font-serif); font-size: 19px; margin: 6px 0 8px; color: var(--ink); }}
  .route p {{ margin: 0; font-size: 14px; color: var(--ink-2); }}

  /* SEÇÕES */
  .sec-head {{ margin: 36px 0 16px; }}
  .sec-num {{ font-family: var(--mono); font-size: 11px; text-transform: uppercase; letter-spacing: .1em; color: var(--muted); font-weight: 600; display: block; }}
  h2 {{ font-family: var(--font-serif); font-size: 26px; margin: 4px 0; color: var(--ink); }}
  .sec-note {{ font-size: 14px; color: var(--muted); margin: 0; }}

  /* TABELA FLUIDA */
  .tablewrap {{ width: 100%; overflow-x: auto; margin: 16px 0 32px; background: var(--surface); border: 1px solid var(--rule); border-radius: 3px; }}
  table {{ width: 100%; border-collapse: collapse; font-size: 13.5px; text-align: left; }}
  th {{ background: var(--surface-2); font-family: var(--mono); font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: .06em; color: var(--muted); padding: 10px 12px; border-bottom: 1px solid var(--rule); }}
  td {{ padding: 10px 12px; border-bottom: 1px solid var(--rule-soft); color: var(--ink-2); }}
  tr:last-child td {{ border-bottom: none; }}
  td.rank {{ font-family: var(--mono); font-weight: 700; color: var(--accent); width: 40px; }}
  td.tool a {{ color: var(--ink); font-weight: 600; text-decoration: none; }}
  td.tool a:hover {{ color: var(--accent); }}
  td.saas {{ color: var(--flag); }}
  td.econ {{ font-family: var(--mono); color: var(--green); font-weight: 600; }}
  td.cat {{ font-size: 12px; color: var(--muted); }}
  td.lic {{ font-family: var(--mono); font-size: 11px; }}

  /* CARDS NO FORMATO DOSSIÊ EXECUTIVO (LARGURA TOTAL) */
  .ledger {{ display: flex; flex-direction: column; gap: 24px; }}
  .entry {{ background: var(--surface); border: 1px solid var(--rule); border-radius: 3px; box-shadow: var(--shadow); display: grid; grid-template-columns: 60px 1fr; transition: border-color .15s ease; }}
  .entry:hover {{ border-color: var(--accent); }}
  .entry-rank {{ font-family: var(--mono); font-size: 20px; font-variant-numeric: tabular-nums; color: var(--accent); background: var(--accent-soft); display: flex; align-items: flex-start; justify-content: center; padding: 18px 0; border-right: 1px solid var(--rule); border-radius: 2px 0 0 2px; }}
  
  .entry-body {{ padding: 18px 22px 20px; display: flex; flex-direction: column; gap: 14px; min-width: 0; }}

  .entry-top {{ display: flex; flex-wrap: wrap; align-items: center; gap: 8px 10px; }}
  .entry-top h3 {{ width: 100%; margin: 0 0 4px 0; font-family: var(--font-serif); font-weight: 600; font-size: 24px; line-height: 1.15; letter-spacing: -.01em; color: var(--ink); }}

  .senior-badge {{ font-family: var(--mono); font-size: 10px; letter-spacing: .08em; text-transform: uppercase; padding: 3px 8px; border-radius: 2px; font-weight: 700; }}
  .senior-badge.green {{ background: var(--green-soft); color: var(--green); border: 1px solid color-mix(in srgb, var(--green) 35%, transparent); }}
  .killer-badge {{ font-family: var(--mono); font-size: 10.5px; letter-spacing: .08em; text-transform: uppercase; padding: 3px 8px; border-radius: 2px; background: var(--flag-soft); color: var(--flag); border: 1px solid color-mix(in srgb, var(--flag) 35%, transparent); font-weight: 600; }}
  .econ-badge {{ font-family: var(--mono); font-size: 10.5px; letter-spacing: .08em; text-transform: uppercase; padding: 3px 8px; border-radius: 2px; background: var(--green-soft); color: var(--green); border: 1px solid color-mix(in srgb, var(--green) 35%, transparent); font-weight: 600; }}
  .lic-badge {{ font-family: var(--mono); font-size: 10px; letter-spacing: .08em; text-transform: uppercase; padding: 3px 8px; border-radius: 2px; background: var(--accent-soft); color: var(--accent); border: 1px solid color-mix(in srgb, var(--accent) 35%, transparent); white-space: nowrap; }}
  .kind {{ font-family: var(--mono); font-size: 10px; letter-spacing: .08em; text-transform: uppercase; color: var(--muted); font-weight: 600; padding: 3px 6px; border: 1px solid var(--rule-soft); border-radius: 2px; background: var(--surface-2); }}

  .entry-section {{ display: flex; flex-direction: column; gap: 6px; width: 100%; padding-top: 12px; border-top: 1px dashed var(--rule-soft); }}
  .entry-section .label {{ font-family: var(--mono); font-size: 11px; letter-spacing: .1em; text-transform: uppercase; color: var(--accent); font-weight: 600; }}
  .entry-section p {{ margin: 0; font-size: 14.5px; line-height: 1.55; color: var(--ink-2); }}
  .entry-section p strong {{ color: var(--ink); font-weight: 600; }}

  /* GRIDS */
  .econ-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 10px; margin-top: 2px; }}
  .econ-card {{ background: var(--surface-2); border: 1px solid var(--rule-soft); border-radius: 2px; padding: 10px 12px; display: flex; flex-direction: column; gap: 2px; }}
  .econ-card.highlight {{ border-left: 3px solid var(--green); background: color-mix(in srgb, var(--green-soft) 25%, var(--surface)); }}
  .econ-card.killer {{ border-left: 3px solid var(--flag); background: color-mix(in srgb, var(--flag-soft) 25%, var(--surface)); }}
  .econ-lbl {{ font-family: var(--mono); font-size: 10px; text-transform: uppercase; letter-spacing: .08em; color: var(--muted); font-weight: 600; }}
  .econ-val {{ font-size: 13.5px; line-height: 1.45; color: var(--ink); }}

  .infra-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 10px; margin-top: 2px; }}
  .infra-card {{ background: var(--surface-2); border: 1px solid var(--rule-soft); border-radius: 2px; padding: 10px 12px; display: flex; flex-direction: column; gap: 2px; }}
  .infra-card.verdict {{ border-left: 3px solid var(--gold); background: color-mix(in srgb, var(--gold-soft) 25%, var(--surface)); grid-column: span 2; }}
  @media (max-width: 760px) {{ .infra-card.verdict {{ grid-column: span 1; }} }}
  .infra-lbl {{ font-family: var(--mono); font-size: 10px; text-transform: uppercase; letter-spacing: .08em; color: var(--muted); font-weight: 600; }}
  .infra-val {{ font-family: var(--mono); font-size: 13px; font-weight: 600; color: var(--accent); line-height: 1.4; }}
  .infra-card p {{ margin: 0; font-size: 13px; line-height: 1.45; color: var(--ink-2); }}

  .code-box {{ position: relative; display: flex; flex-direction: column; width: 100%; margin-top: 4px; }}
  pre {{ margin: 0; padding: 10px 48px 10px 12px; background: var(--surface-2); border: 1px solid var(--rule-soft); border-radius: 2px; overflow-x: auto; }}
  code {{ font-family: var(--mono); font-size: 12.5px; color: var(--ink); line-height: 1.45; }}
  .copy-btn {{ position: absolute; top: 6px; right: 6px; background: var(--surface); border: 1px solid var(--rule); color: var(--muted); border-radius: 2px; padding: 3px 6px; font-family: var(--mono); font-size: 10px; cursor: pointer; }}
  .copy-btn:hover {{ background: var(--accent-soft); color: var(--accent); border-color: var(--accent); }}

  .repo-btn {{ display: inline-flex; align-items: center; justify-content: center; gap: 6px; font-family: var(--mono); font-size: 11.5px; padding: 6px 10px; border: 1px solid var(--rule); border-radius: 2px; background: var(--surface); color: var(--ink); text-decoration: none; width: fit-content; }}
  .repo-btn:hover {{ background: var(--accent-soft); border-color: var(--accent); color: var(--accent); }}
  .repo-btn svg {{ width: 13px; height: 13px; fill: currentColor; }}

  .steps-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 8px; margin-top: 2px; }}
  .step-card {{ background: var(--surface-2); border: 1px solid var(--rule-soft); border-radius: 2px; padding: 10px 12px; display: flex; flex-direction: column; gap: 2px; }}
  .step-head {{ display: flex; align-items: center; gap: 4px; font-family: var(--mono); font-size: 10px; font-weight: 600; color: var(--accent); text-transform: uppercase; }}
  .step-badge {{ background: var(--accent); color: var(--paper); border-radius: 2px; padding: 1px 5px; font-size: 9.5px; font-weight: 700; }}
  .step-card p {{ margin: 0; font-size: 13px; line-height: 1.4; color: var(--ink-2); }}
  .step-card code {{ font-family: var(--mono); font-size: 11.5px; background: var(--surface); padding: 1px 4px; border-radius: 2px; border: 1px solid var(--rule-soft); }}

  footer {{ border-top: 1px solid var(--rule); padding-top: 16px; margin-top: 40px; display: flex; flex-direction: column; gap: 8px; }}
  footer p {{ margin: 0; font-size: 13px; color: var(--muted); }}
</style>
<script>
function copyCode(btn) {{
  const code = btn.previousElementSibling.innerText;
  navigator.clipboard.writeText(code).then(() => {{
    const originalText = btn.innerText;
    btn.innerText = 'Copiado!';
    btn.style.color = 'var(--green)';
    setTimeout(() => {{
      btn.innerText = originalText;
      btn.style.color = '';
    }}, 2000);
  }}).catch(() => {{
    btn.innerText = 'Erro';
  }});
}}
</script>
</head>
<body>
<div class="wrap">
<header>
  <div class="header-top">
    <a class="back-link" href="index.html">← Voltar ao Hub Central</a>
    <span class="camada-pill">{camada.split('·')[0].strip()}</span>
  </div>
  <div class="hero">
    <h1>{title}</h1>
    <p class="deck">{deck}</p>
  </div>
  <div class="hero-stats">
    <div class="stat-card"><div class="num">{total}</div><div class="lbl">Tecnologias Auditadas</div></div>
    <div class="stat-card"><div class="num">100%</div><div class="lbl">Open-Source & Soberano</div></div>
    <div class="stat-card"><div class="num">Até 95%</div><div class="lbl">Economia de Custos</div></div>
    <div class="stat-card"><div class="num">0 Lock-in</div><div class="lbl">Independência Total</div></div>
  </div>
</header>

<section>
  <div class="sec-head">
    <span class="sec-num">Parte 1 · Diagnóstico Estratégico</span>
    <h2>A transição da dependência para a soberania</h2>
  </div>
  <div class="grid2">
    <div class="route red">
      <span class="tag">O Risco Proprietário</span>
      <h4>{pilar_1}</h4>
      <p>{pilar_1_desc}</p>
    </div>
    <div class="route green">
      <span class="tag">A Solução Aberta</span>
      <h4>{pilar_2}</h4>
      <p>{pilar_2_desc}</p>
    </div>
  </div>
</section>

<section>
  <div class="sec-head">
    <span class="sec-num">Parte 2 · O Panorama Geral</span>
    <h2>O inventário completo da camada</h2>
    <p class="sec-note">Tabela comparativa direta: ferramenta, o software proprietário substituído, economia média e licença.</p>
  </div>
  <div class="tablewrap">
    <table>
      <thead>
        <tr>
          <th>#</th>
          <th>Ferramenta</th>
          <th>Substitui o SaaS Pago</th>
          <th>Economia Declarada</th>
          <th>Categoria</th>
          <th>Licença</th>
        </tr>
      </thead>
      <tbody>
{tabela_html}
      </tbody>
    </table>
  </div>
</section>

<section>
  <div class="sec-head">
    <span class="sec-num">Parte 3 · Dossiê Técnico das Ferramentas</span>
    <h2>Fichas técnicas individuais de arquitetura</h2>
    <p class="sec-note">Análise profunda de cada tecnologia: o que faz, como funciona por baixo dos panos, como usar e veredito.</p>
  </div>
  <div class="ledger">
{cards_bloco_html}
  </div>
</section>

<footer>
  <p><strong>Compêndio de Soberania Tecnológica Open-Source · Fábrica Universal</strong></p>
  <p>Padrão Dossiê Executivo · Documentação auditada e livre de dependências proprietárias.</p>
</footer>
</div>
</body>
</html>"""

def compilar_todas_as_listas_dossie_r5():
    docs_dir = Path("docs/listas")
    output_dir = Path("output/listas-open-source")
    brain_dir = Path(r"C:\Users\trcnologia\.gemini\antigravity-cli\brain\0e2afde3-829c-4443-b5a5-7a8779eeb139")

    docs_dir.mkdir(parents=True, exist_ok=True)
    output_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 80)
    print(" 🚀 COMPILADOR OFICIAL DOSSIÊ EXECUTIVO (R5): LISTAS 01 A 30")
    print("=" * 80)

    for idx, lista in enumerate(TODAS_AS_30_LISTAS, start=1):
        slug = lista["slug"]
        print(f"[{idx:02d}/30] Compilando '{slug}' no Padrão Dossiê Executivo R5...")
        html = renderizar_dossie_r5(lista)

        (docs_dir / f"{slug}.html").write_text(html, encoding="utf-8")
        (output_dir / f"{slug}.html").write_text(html, encoding="utf-8")
        if brain_dir.exists():
            (brain_dir / f"{slug}.html").write_text(html, encoding="utf-8")

    print("\n" + "=" * 80)
    print(" 🎉 TODAS AS 30 LISTAS FORAM COMPILADAS NO RIGOROSO PADRÃO DOSSIÊ EXECUTIVO (R5)!")
    print("=" * 80 + "\n")

if __name__ == "__main__":
    compilar_todas_as_listas_dossie_r5()
