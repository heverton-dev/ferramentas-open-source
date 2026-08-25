# -*- coding: utf-8 -*-
"""
Gera os 5 arquivos HTML das camadas 35 a 39 com 20 fichas completas cada,
com cabeçalho padronizado: Título em cima e Badges embaixo.
"""
import sys
import os

def console_utf8():
    if sys.platform == "win32":
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")

console_utf8()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = os.path.join(BASE_DIR, "output", "listas-open-source")
os.makedirs(OUTPUT_DIR, exist_ok=True)

CSS_PADRAO = """  * { scrollbar-width: thin; scrollbar-color: var(--accent) transparent; box-sizing: border-box; }
  ::-webkit-scrollbar { width: 4px; height: 4px; }
  ::-webkit-scrollbar-track { background: transparent; }
  ::-webkit-scrollbar-thumb { background: var(--accent); border-radius: 4px; }

  :root {
    --paper:#ECEEF2; --surface:#F8F9FC; --surface-2:#DFE3EB;
    --ink:#151A26; --ink-2:#3B4457; --muted:#68738A;
    --rule:#C7CEDB; --rule-soft:#DADFE8;
    --accent:VAR_ACCENT; --accent-soft:VAR_ACCENT_SOFT;
    --gold:#7A5410; --gold-soft:#EFE5CE;
    --flag:#8E2436; --flag-soft:#F0D9DD;
    --green:#1B5E3B; --green-soft:#D8EFE2;
    --shadow: 0 1px 0 rgba(21,26,38,.05), 0 8px 24px -18px rgba(21,26,38,.45);
    --serif:"Iowan Old Style","Palatino Linotype",Palatino,"Book Antiqua",Georgia,serif;
    --sans:system-ui,-apple-system,"Segoe UI",Roboto,"Helvetica Neue",sans-serif;
    --mono:ui-monospace,"Cascadia Mono","SF Mono",SFMono-Regular,Menlo,Consolas,monospace;
  }
  @media (prefers-color-scheme: dark) {
    :root:not([data-theme="light"]) {
      --paper:#0E1118; --surface:#161A24; --surface-2:#1F2531;
      --ink:#E3E7F0; --ink-2:#B3BCCC; --muted:#8391A8;
      --rule:#2A3142; --rule-soft:#222836;
      --accent:VAR_ACCENT_DARK; --accent-soft:VAR_ACCENT_DARK_SOFT;
      --gold:#D6A44E; --gold-soft:#332810;
      --flag:#E0788C; --flag-soft:#3A1A21;
      --green:#6BC48F; --green-soft:#122B1C;
      --shadow: 0 1px 0 rgba(0,0,0,.3), 0 8px 24px -18px rgba(0,0,0,.9);
    }
  }

  body { margin:0; background:var(--paper); color:var(--ink); font-family:var(--sans); font-size:16px; line-height:1.6; -webkit-font-smoothing:antialiased; }
  .wrap { max-width:1060px; margin:0 auto; padding:clamp(28px,5vw,64px) clamp(18px,4vw,40px) 96px; display:flex; flex-direction:column; gap:clamp(40px,6vw,72px); }

  /* HEADER EXECUTIVO */
  header { display:flex; flex-direction:column; gap:24px; padding-bottom:12px; border-bottom:1px solid var(--rule); }
  .header-top { display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:12px; }
  .back-link { display:inline-flex; align-items:center; gap:6px; font-family:var(--mono); font-size:11.5px; color:var(--muted); text-decoration:none; padding:4px 8px; border-radius:2px; border:1px solid var(--rule); background:var(--surface); transition:all .15s ease; }
  .back-link:hover { color:var(--accent); border-color:var(--accent); background:var(--accent-soft); text-decoration:none; }
  .eyebrow { font-family:var(--mono); font-size:11.5px; letter-spacing:.14em; text-transform:uppercase; color:var(--muted); display:flex; flex-wrap:wrap; gap:6px 12px; align-items:center; }
  .layer-badge { background:var(--accent); color:var(--paper); padding:3px 8px; border-radius:2px; font-weight:700; font-size:10.5px; letter-spacing:.08em; }

  h1 { font-family:var(--serif); font-weight:600; font-size:clamp(38px,7.5vw,68px); line-height:1.02; letter-spacing:-.025em; margin:0; color:var(--ink); text-wrap:balance; }
  .deck { font-family:var(--serif); font-size:clamp(17px,2.2vw,21px); line-height:1.55; color:var(--ink-2); max-width:100%; margin:0; }
  .deck strong { color:var(--ink); font-weight:600; }

  /* HERO STATS BAR */
  .hero-stats { display:grid; grid-template-columns:repeat(auto-fit, minmax(180px, 1fr)); gap:12px; margin-top:4px; }
  .stat-card { background:var(--surface); border:1px solid var(--rule); border-radius:3px; padding:12px 16px; display:flex; flex-direction:column; gap:4px; box-shadow:var(--shadow); }
  .stat-card .stat-val { font-family:var(--mono); font-size:20px; font-weight:700; color:var(--accent); line-height:1.1; }
  .stat-card .stat-lbl { font-family:var(--mono); font-size:10.5px; text-transform:uppercase; letter-spacing:.08em; color:var(--muted); font-weight:600; }
  .stat-card.good .stat-val { color:var(--green); }
  
  /* QUICK JUMP ANCHORS */
  .header-actions { display:flex; flex-wrap:wrap; gap:8px; align-items:center; margin-top:2px; }
  .jump-btn { display:inline-flex; align-items:center; gap:6px; font-family:var(--mono); font-size:11.5px; padding:6px 12px; border-radius:2px; border:1px solid var(--rule); background:var(--surface); color:var(--ink-2); text-decoration:none; transition:all .15s ease; }
  .jump-btn:hover { border-color:var(--accent); color:var(--accent); background:var(--accent-soft); text-decoration:none; }
  .jump-btn.primary { background:var(--accent-soft); border-color:color-mix(in srgb, var(--accent) 40%, transparent); color:var(--accent); font-weight:600; }

  section { display:flex; flex-direction:column; gap:22px; }
  .sec-head { display:flex; flex-direction:column; gap:8px; border-top:2px solid var(--ink); padding-top:14px; }
  .sec-num { font-family:var(--mono); font-size:11.5px; letter-spacing:.14em; text-transform:uppercase; color:var(--muted); }
  h2 { font-family:var(--serif); font-weight:600; font-size:clamp(26px,4vw,36px); line-height:1.1; letter-spacing:-.015em; margin:0; text-wrap:balance; }
  .sec-note { margin:0; color:var(--ink-2); max-width:100%; font-size:15.5px; }

  /* TABELA FLUIDA SEM SCROLL */
  .tablewrap { border:1px solid var(--rule); border-radius:3px; background:var(--surface); width:100%; overflow:hidden; }
  table { border-collapse:collapse; width:100%; font-size:13.5px; table-layout:auto; }
  thead th { text-align:left; font-family:var(--mono); font-weight:600; font-size:10.5px; letter-spacing:.1em; text-transform:uppercase; color:var(--muted); padding:10px 12px; border-bottom:1px solid var(--rule); }
  tbody td { padding:10px 12px; border-bottom:1px solid var(--rule-soft); vertical-align:middle; }
  tbody tr:last-child td { border-bottom:0; }
  td.rank { font-family:var(--mono); color:var(--muted); font-variant-numeric:tabular-nums; width:36px; text-align:center; }
  td.tool { font-weight:600; color:var(--ink); font-size:14px; }
  td.killer { font-family:var(--mono); font-size:11.5px; color:var(--flag); font-weight:600; line-height:1.35; }
  td.econ { font-family:var(--mono); font-size:11.5px; color:var(--green); font-weight:600; line-height:1.35; }
  td.lic { font-family:var(--mono); font-size:11.5px; color:var(--muted); line-height:1.35; }

  /* CARDS NO FORMATO DOSSIÊ EXECUTIVO */
  .ledger { display:flex; flex-direction:column; gap:28px; }
  .entry { background:var(--surface); border:1px solid var(--rule); border-radius:3px; box-shadow:var(--shadow); display:grid; grid-template-columns:64px 1fr; transition:border-color .15s ease; }
  .entry:hover { border-color:var(--accent); }
  .entry-rank { font-family:var(--mono); font-size:22px; font-variant-numeric:tabular-nums; color:var(--accent); background:var(--accent-soft); display:flex; align-items:flex-start; justify-content:center; padding:20px 0; border-right:1px solid var(--rule); border-radius:2px 0 0 2px; }
  
  .entry-body { padding:20px 24px 22px; display:flex; flex-direction:column; gap:16px; min-width:0; }

  /* CABEÇALHO PADRONIZADO */
  .entry-top { display:flex; flex-wrap:wrap; align-items:center; gap:8px 12px; }
  .entry-top h3 { width:100%; margin:0 0 4px 0; font-family:var(--serif); font-weight:600; font-size:26px; line-height:1.15; letter-spacing:-.01em; color:var(--ink); }

  .senior-badge { font-family:var(--mono); font-size:10.5px; letter-spacing:.08em; text-transform:uppercase; padding:3px 8px; border-radius:2px; font-weight:700; }
  .senior-badge.green { background:var(--green-soft); color:var(--green); border:1px solid color-mix(in srgb, var(--green) 35%, transparent); }
  .senior-badge.gold { background:var(--gold-soft); color:var(--gold); border:1px solid color-mix(in srgb, var(--gold) 35%, transparent); }
  .senior-badge.flag { background:var(--flag-soft); color:var(--flag); border:1px solid color-mix(in srgb, var(--flag) 35%, transparent); }

  .killer-badge { font-family:var(--mono); font-size:11px; letter-spacing:.08em; text-transform:uppercase; padding:3px 8px; border-radius:2px; background:var(--flag-soft); color:var(--flag); border:1px solid color-mix(in srgb, var(--flag) 35%, transparent); font-weight:600; }
  .econ-badge { font-family:var(--mono); font-size:11px; letter-spacing:.08em; text-transform:uppercase; padding:3px 8px; border-radius:2px; background:var(--green-soft); color:var(--green); border:1px solid color-mix(in srgb, var(--green) 35%, transparent); font-weight:600; }
  .lic-badge { font-family:var(--mono); font-size:10.5px; letter-spacing:.08em; text-transform:uppercase; padding:3px 8px; border-radius:2px; background:var(--accent-soft); color:var(--accent); border:1px solid color-mix(in srgb, var(--accent) 35%, transparent); white-space:nowrap; }
  .kind { font-family:var(--mono); font-size:10.5px; letter-spacing:.1em; text-transform:uppercase; color:var(--muted); font-weight:600; }

  /* SEÇÕES VERTICAIS DO CARD (LARGURA TOTAL) */
  .entry-section { display:flex; flex-direction:column; gap:8px; width:100%; padding-top:14px; border-top:1px dashed var(--rule-soft); }
  .entry-section .label { font-family:var(--mono); font-size:11px; letter-spacing:.12em; text-transform:uppercase; color:var(--accent); font-weight:600; }
  .entry-section p { margin:0; font-size:15px; line-height:1.55; color:var(--ink-2); }
  .entry-section p strong { color:var(--ink); font-weight:600; }

  /* ANÁLISE ECONÔMICA GRID */
  .econ-grid { display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:12px; margin-top:4px; }
  .econ-card { background:var(--surface-2); border:1px solid var(--rule-soft); border-radius:2px; padding:12px 14px; display:flex; flex-direction:column; gap:4px; }
  .econ-card.highlight { border-left:3px solid var(--green); background:color-mix(in srgb, var(--green-soft) 25%, var(--surface)); }
  .econ-card.killer { border-left:3px solid var(--flag); background:color-mix(in srgb, var(--flag-soft) 25%, var(--surface)); }
  .econ-lbl { font-family:var(--mono); font-size:10.5px; text-transform:uppercase; letter-spacing:.08em; color:var(--muted); font-weight:600; }
  .econ-val { font-size:14px; line-height:1.45; color:var(--ink); }
  .econ-val strong { color:var(--ink); font-weight:600; }

  /* REQUISITOS DE INFRAESTRUTURA GRID */
  .infra-grid { display:grid; grid-template-columns:repeat(auto-fit, minmax(220px, 1fr)); gap:12px; margin-top:4px; }
  .infra-card { background:var(--surface-2); border:1px solid var(--rule-soft); border-radius:2px; padding:12px 14px; display:flex; flex-direction:column; gap:4px; }
  .infra-card.verdict { border-left:3px solid var(--gold); background:color-mix(in srgb, var(--gold-soft) 25%, var(--surface)); grid-column:span 2; }
  @media (max-width:760px) { .infra-card.verdict { grid-column:span 1; } }
  .infra-lbl { font-family:var(--mono); font-size:10.5px; text-transform:uppercase; letter-spacing:.08em; color:var(--muted); font-weight:600; }
  .infra-val { font-family:var(--mono); font-size:13.5px; font-weight:600; color:var(--accent); line-height:1.4; }
  .infra-card p { margin:0; font-size:13.5px; line-height:1.45; color:var(--ink-2); }

  /* CODE BOX FULL-WIDTH */
  .code-box { position:relative; display:flex; flex-direction:column; width:100%; margin-top:4px; }
  pre { margin:0; padding:12px 52px 12px 14px; background:var(--surface-2); border:1px solid var(--rule-soft); border-radius:2px; overflow-x:auto; }
  code { font-family:var(--mono); font-size:13px; color:var(--ink); line-height:1.5; }
  .copy-btn { position:absolute; top:8px; right:8px; background:var(--surface); border:1px solid var(--rule); color:var(--muted); border-radius:2px; padding:4px 8px; font-family:var(--mono); font-size:10.5px; cursor:pointer; transition:all .15s ease; }
  .copy-btn:hover { background:var(--accent-soft); color:var(--accent); border-color:var(--accent); }

  /* BOTÃO REPOSITÓRIO GITHUB */
  .repo-btn { display:inline-flex; align-items:center; justify-content:center; gap:8px; font-family:var(--mono); font-size:12px; padding:8px 12px; border:1px solid var(--rule); border-radius:2px; background:var(--surface); color:var(--ink); text-decoration:none; transition:all .15s ease; }
  .repo-btn:hover { background:var(--accent-soft); border-color:var(--accent); color:var(--accent); text-decoration:none; }
  .repo-btn svg { width:14px; height:14px; fill:currentColor; }

  /* STEPS GRID (COMO USAR NO DIA A DIA) */
  .steps-grid { display:grid; grid-template-columns:repeat(auto-fit, minmax(240px, 1fr)); gap:10px; margin-top:2px; }
  .step-card { background:var(--surface-2); border:1px solid var(--rule-soft); border-radius:2px; padding:12px 14px; display:flex; flex-direction:column; gap:4px; }
  .step-head { display:flex; align-items:center; gap:6px; font-family:var(--mono); font-size:10.5px; font-weight:600; color:var(--accent); text-transform:uppercase; letter-spacing:.06em; }
  .step-badge { background:var(--accent); color:var(--paper); border-radius:2px; padding:1px 6px; font-size:10px; font-weight:700; }
  .step-card p { margin:0; font-size:13.5px; line-height:1.45; color:var(--ink-2); }
  .step-card code { font-family:var(--mono); font-size:12px; background:var(--surface); padding:1px 5px; border-radius:2px; border:1px solid var(--rule-soft); color:var(--ink); }
  a:hover { text-decoration-color:var(--accent); }
  .repo { font-family:var(--mono); font-size:12.5px; word-break:break-all; }

  .how-to-use { display:flex; flex-direction:column; gap:8px; padding-top:14px; border-top:1px dashed var(--rule-soft); width:100%; }
  .how-to-use .label { color:var(--accent); font-weight:600; font-size:11px; letter-spacing:.12em; text-transform:uppercase; }
  .how-to-use p { margin:0; font-size:14.5px; line-height:1.55; color:var(--ink-2); }
  .how-to-use p strong { color:var(--ink); font-weight:600; }
  .how-to-use code { font-family:var(--mono); font-size:12.5px; background:var(--surface-2); padding:2px 6px; border-radius:2px; border:1px solid var(--rule-soft); color:var(--ink); }

  footer { border-top:1px solid var(--rule); padding-top:18px; display:flex; flex-direction:column; gap:10px; }
  footer p { margin:0; font-size:13.5px; color:var(--muted); max-width:72ch; }"""

def render_html(camada_num, eyebrow, titulo, deck, chips, cores, items):
    css = CSS_PADRAO.replace("VAR_ACCENT_SOFT", cores["accent_soft"])
    css = css.replace("VAR_ACCENT_DARK_SOFT", cores["accent_dark_soft"])
    css = css.replace("VAR_ACCENT_DARK", cores["accent_dark"])
    css = css.replace("VAR_ACCENT", cores["accent"])

    # Tabela
    rows_html = []
    for item in items:
        rows_html.append(f"""          <tr><td class="rank">{item['rank']:02d}</td><td class="tool">{item['nome']}</td><td class="killer">{item['substitui']}</td><td>{item['categoria']}</td><td class="econ">{item['economia']}</td><td class="lic">{item['licenca']}</td></tr>""")
    tbody = "\n".join(rows_html)

    # Fichas
    entries_html = []
    for item in items:
        como_usar_html = ""
        if "como_usar" in item and item["como_usar"]:
            como_usar_html = f"""
          <div class="how-to-use">
            <span class="label">3. Como Usar no Dia a Dia (Passo a Passo Prático)</span>
            <p>{item['como_usar']}</p>
          </div>"""

        entries_html.append(f"""      <!-- {item['rank']:02d}. {item['nome']} -->
      <div class="entry">
        <div class="entry-rank">{item['rank']:02d}</div>
        <div class="entry-body">
          <div class="entry-top">
            <h3>{item['nome']} · {item['subtitulo']}</h3>
            <span class="killer-badge">Substitui: {item['substitui']}</span>
            <span class="econ-badge">Economia: {item['economia']}</span>
            <span class="lic-badge">{item['licenca']}</span>
            <span class="kind">{item['kind']}</span>
          </div>
          <div class="cols">
            <div class="block">
              <span class="label">1. O Que Faz</span>
              <p>{item['o_que_faz']}</p>
              <span class="label">2. Como Funciona</span>
              <p>{item['como_funciona']}</p>
              <pre><code>{item['quickstart']}</code></pre>
            </div>
            <div class="block">
              <span class="label">Especificações</span>
              <div class="spec">{item['specs']}</div>
              <div class="truth">
                <p><strong>Veredito:</strong> {item['veredito']}</p>
              </div>
              <div class="repo"><a href="{item['github']}" target="_blank">{item['github'].replace('https://', '')}</a></div>
            </div>
          </div>{como_usar_html}
        </div>
      </div>""")
    ledger = "\n\n".join(entries_html)

    chips_html = "\n".join([f'      <div class="chip">{c}</div>' for c in chips])

    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{titulo} · Enciclopédia da Soberania</title>
<style>
{css}
</style>
</head>
<body>

<div class="wrap">

  <header>
    <div class="eyebrow">
      <span>{eyebrow}</span><span>·</span><span>Curadoria de Elite</span><span>·</span>
      <b>Top 20 Tecnologias Auditadas</b>
    </div>
    <h1>{titulo}</h1>
    <p class="deck">{deck}</p>
    <div class="chips">
{chips_html}
    </div>
  </header>

  <section>
    <div class="sec-head">
      <span class="sec-num">Parte 1 · Matriz Comparativa</span>
      <h2>Top 20 Tecnologias & Motores Soberanos</h2>
      <p class="sec-note">Auditoria técnica de performance, conformidade de licenças e estimativa de economia em substituição a produtos proprietários.</p>
    </div>

    <div class="tablewrap">
      <table>
        <thead>
          <tr>
            <th>#</th>
            <th>Tecnologia</th>
            <th>Substitui no Mercado</th>
            <th>Categoria / Foco</th>
            <th>Economia Estimada</th>
            <th>Licença</th>
          </tr>
        </thead>
        <tbody>
{tbody}
        </tbody>
      </table>
    </div>
  </section>

  <section>
    <div class="sec-head">
      <span class="sec-num">Parte 2 · Fichas Técnicas dos Pilares</span>
      <h2>Detalhamento e Engenharia de Aplicação</h2>
      <p class="sec-note">Guias de implementação, comandos de terminal e especificações operacionais.</p>
    </div>

    <div class="ledger">
{ledger}
    </div>
  </section>

  <footer>
    <p>Enciclopédia de Soberania Tecnológica gerada pela Fábrica Universal. Todos os 20 componentes contam com auditoria de licença OSI e instruções técnicas de reprodução.</p>
  </footer>

</div>

</body>
</html>
"""

print("[*] Módulo base de compilação carregado.")
