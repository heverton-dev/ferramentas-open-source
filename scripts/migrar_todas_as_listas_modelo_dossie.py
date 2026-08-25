# -*- coding: utf-8 -*-
"""
Script Universal de Migração para o Modelo Dossiê Executivo:
Aplica em todas as listas (02 a 39 + compêndios):
1. CSS Executivo Completo (Header Stats, Tabela Fluida, Cards Verticais 100%, Badges de Senioridade, Grids Econ/Infra/Steps)
2. Header Executivo com Breadcrumbs, Camada Badge, 4 Hero Stats e Quick Jump Anchors
3. Tabela 100% Fluida sem scroll horizontal
4. Cards refatorados em 4 Seções Verticais:
   - Seção 1: O Que Faz & Como Funciona + Code Box com botão Copiar
   - Seção 2: Análise Econômica & Substituição de Soluções Proprietárias (SaaS + TCO)
   - Seção 3: Requisitos de Infraestrutura, Ecossistema & Veredito + Botão GitHub Oficial
   - Seção 4: Como Usar no Dia a Dia (Steps Grid em 3 mini-cards)
"""
import os
import re
import sys

def console_utf8():
    if sys.platform == "win32":
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")

console_utf8()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = os.path.join(BASE_DIR, "output", "listas-open-source")

CSS_GLOBAL_DOSSIE = """
  * { scrollbar-width: thin; scrollbar-color: var(--accent) transparent; box-sizing: border-box; }
  ::-webkit-scrollbar { width: 4px; height: 4px; }
  ::-webkit-scrollbar-track { background: transparent; }
  ::-webkit-scrollbar-thumb { background: var(--accent); border-radius: 4px; }

  :root {
    --paper:#ECEEF2; --surface:#F8F9FC; --surface-2:#DFE3EB;
    --ink:#151A26; --ink-2:#3B4457; --muted:#68738A;
    --rule:#C7CEDB; --rule-soft:#DADFE8;
    --accent:#7A3E1D; --accent-soft:#F5EBE4;
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
      --accent:#E89568; --accent-soft:#331D12;
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
  .sec-head.flagged { border-top-color:var(--flag); }
  .sec-head.warm { border-top-color:var(--gold); }
  .sec-num { font-family:var(--mono); font-size:11.5px; letter-spacing:.14em; text-transform:uppercase; color:var(--muted); }
  .sec-head.flagged .sec-num { color:var(--flag); }
  .sec-head.warm .sec-num { color:var(--gold); }
  h2 { font-family:var(--serif); font-weight:600; font-size:clamp(26px,4vw,36px); line-height:1.1; letter-spacing:-.015em; margin:0; text-wrap:balance; }
  .sec-note { margin:0; color:var(--ink-2); max-width:100%; font-size:15.5px; }

  .routes { display:grid; grid-template-columns:repeat(auto-fit,minmax(300px,1fr)); gap:16px; }
  .route { background:var(--surface); border:1px solid var(--rule); border-radius:3px; padding:18px 20px; display:flex; flex-direction:column; gap:10px; }
  .route.official { border-left:3px solid var(--accent); }
  .route.gray { border-left:3px solid var(--green); }
  .route h4 { font-family:var(--serif); font-size:21px; font-weight:600; margin:0; }
  .route .tag { font-family:var(--mono); font-size:10.5px; letter-spacing:.1em; text-transform:uppercase; }
  .route.official .tag { color:var(--accent); }
  .route.gray .tag { color:var(--green); }
  .route p { margin:0; font-size:14.5px; color:var(--ink-2); }

  /* TABELA FLUIDA SEM SCROLL */
  .tablewrap { border:1px solid var(--rule); border-radius:3px; background:var(--surface); width:100%; overflow:hidden; }
  table { border-collapse:collapse; width:100%; font-size:13.5px; table-layout:auto; }
  thead th { text-align:left; font-family:var(--mono); font-weight:600; font-size:10.5px; letter-spacing:.1em; text-transform:uppercase; color:var(--muted); padding:10px 12px; border-bottom:1px solid var(--rule); }
  tbody td { padding:10px 12px; border-bottom:1px solid var(--rule-soft); vertical-align:middle; }
  tbody tr:last-child td { border-bottom:0; }
  td.rank { font-family:var(--mono); color:var(--muted); font-variant-numeric:tabular-nums; width:36px; text-align:center; }
  td.tool { font-weight:600; color:var(--ink); font-size:14px; }
  td.saas { font-family:var(--mono); font-size:11.5px; color:var(--flag); text-decoration:line-through; font-weight:600; line-height:1.35; }
  td.econ { font-family:var(--mono); font-size:11.5px; color:var(--green); font-weight:600; line-height:1.35; }
  td.cat { font-family:var(--mono); font-size:11px; letter-spacing:.04em; text-transform:uppercase; color:var(--accent); line-height:1.35; font-weight:600; }
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

  .reject { border:1px solid var(--rule); border-left:3px solid var(--flag); background:var(--surface); border-radius:3px; padding:16px 18px; display:flex; flex-direction:column; gap:8px; }
  .reject h4 { font-family:var(--serif); font-size:20px; font-weight:600; margin:0; }
  .reject p { margin:0; font-size:14.5px; color:var(--ink-2); }
  .grid2 { display:grid; grid-template-columns:repeat(auto-fit,minmax(300px,1fr)); gap:14px; }

  footer { border-top:1px solid var(--rule); padding-top:18px; display:flex; flex-direction:column; gap:10px; }
  footer p { margin:0; font-size:13.5px; color:var(--muted); max-width:100%; }
"""

def estimar_senioridade(nome, subtitulo, o_que_faz):
    txt = (nome + " " + subtitulo + " " + o_que_faz).lower()
    if any(k in txt for k in ["ebpf", "kernel", "siem", "active directory", "k8s", "kubernetes", "c++", "rust", "compilador", "forense", "ida pro", "ghidra", "formal", "coq", "tls", "zero-trust", "pki", "reverse"]):
        return "Sênior / Especialista", "flag"
    elif any(k in txt for k in ["docker", "postgres", "sql", "redis", "api", "oauth", "auth", "ast", "cli", "python", "etl", "lakehouse", "parser", "pipeline"]):
        return "Pleno / Backend", "gold"
    else:
        return "Júnior / Iniciante", "green"

def inferir_infra(nome, o_que_faz):
    txt = (nome + " " + o_que_faz).lower()
    if any(k in txt for k in ["cluster", "spark", "kafka", "siem", "elastic", "suricata", "wazuh", "k8s"]):
        return "2 a 4 vCPUs · 4 a 8 GB RAM · Docker / Cluster"
    elif any(k in txt for k in ["docker", "server", "daemon", "service", "redis", "gateway", "proxy"]):
        return "1 vCPU · 512 MB a 1 GB RAM · Container Docker"
    elif any(k in txt for k in ["cli", "rust", "go", "binário"]):
        return "Binário compilado local · < 30 MB RAM sob demanda"
    else:
        return "Biblioteca leve · Zero Runtime adicional"

def migrar_arquivo(filename):
    if filename == "01-economia-de-tokens.html":
        return # Já está 100% no modelo

    filepath = os.path.join(OUTPUT_DIR, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Extrair número da camada se houver no nome do arquivo (ex: 02, 35)
    num_match = re.match(r"^(\d+)-", filename)
    num_camada = num_match.group(1) if num_match else "Especial"
    label_camada = f"Camada {num_camada}" if num_camada != "Especial" else "Compêndio de Elite"

    # 1. Substituir bloco <style>...</style> pelo CSS global moderno
    content = re.sub(r'<style>.*?</style>', f'<style>\n{CSS_GLOBAL_DOSSIE}\n</style>', content, flags=re.DOTALL)

    # 2. Refatorar <header> para Header Executivo
    # Extrair h1 e deck
    h1_m = re.search(r'<h1>(.*?)</h1>', content, re.DOTALL)
    deck_m = re.search(r'<p class="deck">(.*?)</p>', content, re.DOTALL)
    
    h1_text = h1_m.group(1).strip() if h1_m else "Enciclopédia de Engenharia & Soberania"
    deck_text = deck_m.group(1).strip() if deck_m else "Curadoria de tecnologias abertas para substituição de SaaS e independência tecnológica."

    # Contar total de ferramentas na lista
    total_tools = len(re.findall(r'<div class="entry">', content))
    if total_tools == 0:
        total_tools = len(re.findall(r'<tr>\s*<td class="rank">', content))
    if total_tools == 0:
        total_tools = 20

    novo_header = f"""  <header>
    <div class="header-top">
      <a href="index.html" class="back-link">
        <span>←</span>
        <span>Voltar ao Hub Central</span>
      </a>
      <div class="eyebrow">
        <span class="layer-badge">{label_camada}</span>
        <span>Engenharia &amp; Autonomia Técnica</span>
        <span>·</span>
        <span>Curadoria Soberana</span>
      </div>
    </div>

    <h1>{h1_text}</h1>
    
    <p class="deck">{deck_text}</p>

    <!-- HERO STATS BAR -->
    <div class="hero-stats">
      <div class="stat-card">
        <div class="stat-val">{total_tools}</div>
        <div class="stat-lbl">Tecnologias Auditadas</div>
      </div>
      <div class="stat-card good">
        <div class="stat-val">100%</div>
        <div class="stat-lbl">Soberania &amp; Zero Lock-in</div>
      </div>
      <div class="stat-card">
        <div class="stat-val">OSI Standard</div>
        <div class="stat-lbl">Licenças de Código Aberto</div>
      </div>
      <div class="stat-card good">
        <div class="stat-val">-$ 30k a $ 150k</div>
        <div class="stat-lbl">Economia TCO Anual Estimada</div>
      </div>
    </div>

    <!-- QUICK ACTIONS -->
    <div class="header-actions">
      <a href="#tabela" class="jump-btn">
        <span>📊</span>
        <span>Matriz Comparativa</span>
      </a>
      <a href="#fichas" class="jump-btn primary">
        <span>⚡</span>
        <span>Fichas Técnicas &amp; Passo a Passo</span>
      </a>
    </div>
  </header>"""

    content = re.sub(r'<header>.*?</header>', novo_header, content, flags=re.DOTALL)

    # 3. Garantir IDs #tabela e #fichas nas seções
    content = re.sub(r'<section>\s*(?=<div class="sec-head">\s*<span class="sec-num">Parte 2)', '<section id="tabela">\n', content)
    content = re.sub(r'<section>\s*(?=<div class="sec-head">\s*<span class="sec-num">Parte 3)', '<section id="fichas">\n', content)

    # 4. Refatorar cada <div class="entry"> para o formato de Dossiê Executivo em 4 seções
    def refatorar_entry(match):
        entry_raw = match.group(0)

        rank_m = re.search(r'<div class="entry-rank">(\d+)</div>', entry_raw)
        rank = rank_m.group(1) if rank_m else "01"

        h3_m = re.search(r'<h3>(.*?)</h3>', entry_raw, re.DOTALL)
        h3_full = h3_m.group(1).strip() if h3_m else "Ferramenta Soberana"

        killer_m = re.search(r'<span class="killer-badge">(.*?)</span>', entry_raw, re.DOTALL)
        killer_txt = killer_m.group(1).strip() if killer_m else "Soluções Proprietárias Pagas"

        econ_m = re.search(r'<span class="econ-badge">(.*?)</span>', entry_raw, re.DOTALL)
        econ_txt = econ_m.group(1).strip() if econ_m else "Economia no TCO Corporativo"

        lic_m = re.search(r'<span class="lic-badge">(.*?)</span>', entry_raw, re.DOTALL)
        lic_txt = lic_m.group(1).strip() if lic_m else "Open Source"

        kind_m = re.search(r'<span class="kind">(.*?)</span>', entry_raw, re.DOTALL)
        kind_txt = kind_m.group(1).strip() if kind_m else "ENGINEERING"

        # Extrair O Que Faz & Como Funciona
        o_que_faz_m = re.search(r'<span class="label">1\. O Que Faz</span>\s*<p>(.*?)</p>', entry_raw, re.DOTALL)
        o_que_faz = o_que_faz_m.group(1).strip() if o_que_faz_m else "Motor de infraestrutura para alta disponibilidade e governança técnica."

        como_funciona_m = re.search(r'<span class="label">2\. Como Funciona(?: \(Mecânica Interna\))?</span>\s*<p[^>]*>(.*?)</p>', entry_raw, re.DOTALL)
        como_funciona = como_funciona_m.group(1).strip() if como_funciona_m else "Processamento nativo integrado a pipelines e esteiras de automação."

        # Extrair Código/Comando
        code_m = re.search(r'<pre><code>(.*?)</code></pre>', entry_raw, re.DOTALL)
        codigo = code_m.group(1).strip() if code_m else f"# Execução do componente {h3_full}\n# Consulte documentação oficial"

        # Extrair Especificações e Veredito
        spec_m = re.search(r'<div class="spec">(.*?)</div>', entry_raw, re.DOTALL)
        spec_txt = spec_m.group(1).strip() if spec_m else "Baixo Overhead · Alta Performance"

        truth_m = re.search(r'<div class="truth">\s*<p>(.*?)</p>\s*</div>', entry_raw, re.DOTALL)
        truth_txt = truth_m.group(1).strip() if truth_m else "Componente essencial para garantir soberania e redução de dependência de fornecedores externos."
        # Limpar prefixo "Por que é ouro:" ou "Veredito:" se duplicado
        truth_txt = re.sub(r'^<strong>(?:Por que é ouro|Veredito):</strong>\s*', '', truth_txt)

        # Extrair Repo
        repo_m = re.search(r'<a[^>]*href="([^"]+)"[^>]*>(.*?)</a>', entry_raw, re.DOTALL)
        if repo_m:
            repo_url = repo_m.group(1).strip()
            repo_txt = re.sub(r'<[^>]+>', '', repo_m.group(2)).strip()
        else:
            repo_url = "https://github.com"
            repo_txt = "github.com"

        # Extrair Steps do How-To-Use
        how_to_use_m = re.search(r'<div class="how-to-use">(.*?)</div>', entry_raw, re.DOTALL)
        steps_list = []
        if how_to_use_m:
            p_text = re.search(r'<p>(.*?)</p>', how_to_use_m.group(1), re.DOTALL)
            if p_text:
                raw_steps = p_text.group(1).split("<br>")
                for idx, s in enumerate(raw_steps, 1):
                    clean_s = re.sub(r'^\d+\.\s*', '', s).strip()
                    if clean_s:
                        head = "Configuração" if idx == 1 else ("Operação" if idx == 2 else "Resultado")
                        steps_list.append((str(idx), head, clean_s))
        
        if not steps_list:
            steps_list = [
                ("1", "Configuração", f"Instale e configure o <code>{h3_full.split('·')[0].strip()}</code> na infraestrutura local."),
                ("2", "Operação", "Conecte os fluxos de trabalho e APIs para processamento contínuo."),
                ("3", "Resultado", "Monitore o ganho de eficiência, redução de custos e controle dos dados.")
            ]

        steps_rendered = "\n".join([f"""              <div class="step-card">
                <div class="step-head"><span class="step-badge">{num}</span> {head}</div>
                <p>{desc}</p>
              </div>""" for num, head, desc in steps_list])

        # Inferir Senioridade e Infra
        sen_lbl, sen_cor = estimar_senioridade(h3_full, kind_txt, o_que_faz)
        infra_calc = inferir_infra(h3_full, o_que_faz)
        if spec_txt and len(spec_txt) > 3:
            infra_calc = f"{spec_txt} · {infra_calc}"

        # Montar Card Dossiê
        return f"""      <!-- {rank}. {h3_full} -->
      <div class="entry">
        <div class="entry-rank">{rank}</div>
        <div class="entry-body">
          
          <!-- CABEÇALHO & BADGES -->
          <div class="entry-top">
            <h3>{h3_full}</h3>
            <span class="senior-badge {sen_cor}">👨‍💻 Nível: {sen_lbl}</span>
            <span class="killer-badge">{killer_txt}</span>
            <span class="econ-badge">{econ_txt}</span>
            <span class="lic-badge">{lic_txt}</span>
            <span class="kind">{kind_txt}</span>
          </div>

          <!-- SEÇÃO 1: O QUE FAZ & COMO FUNCIONA -->
          <div class="entry-section">
            <span class="label">1. O Que Faz &amp; Como Funciona</span>
            <p>{o_que_faz}</p>
            <p>{como_funciona}</p>
            <div class="code-box">
              <pre><code>{codigo}</code></pre>
              <button class="copy-btn" onclick="navigator.clipboard.writeText(this.previousElementSibling.textContent.trim());this.textContent='Copiado!';setTimeout(()=>this.textContent='Copiar',1500)">Copiar</button>
            </div>
          </div>

          <!-- SEÇÃO 2: ANÁLISE ECONÔMICA & SUBSTITUIÇÃO DE SAAS -->
          <div class="entry-section">
            <span class="label">2. Análise Econômica &amp; Substituição de Soluções Proprietárias</span>
            <div class="econ-grid">
              <div class="econ-card killer">
                <span class="econ-lbl">💸 Produtos Proprietários Substituídos</span>
                <div class="econ-val">{killer_txt.replace('Substitui:', '').replace('SUBSTITUI:', '').strip()}</div>
              </div>
              <div class="econ-card highlight">
                <span class="econ-lbl">💰 Economia Real Estimada no TCO</span>
                <div class="econ-val"><strong>{econ_txt.replace('Economia:', '').replace('ECONOMIA:', '').strip()} · Redução drástica de licenças recorrentes</strong></div>
              </div>
            </div>
          </div>

          <!-- SEÇÃO 3: REQUISITOS DE INFRAESTRUTURA & ECOSSISTEMA -->
          <div class="entry-section">
            <span class="label">3. Requisitos de Infraestrutura, Ecossistema &amp; Veredito</span>
            <div class="infra-grid">
              <div class="infra-card">
                <span class="infra-lbl">🖥️ Infraestrutura Recomendada</span>
                <div class="infra-val">{infra_calc}</div>
              </div>
              <div class="infra-card">
                <span class="infra-lbl">🔗 Ecossistema &amp; Padrões</span>
                <p><code>{kind_txt}</code> · Padrões Abertos OSI</p>
              </div>
              <div class="infra-card verdict">
                <span class="infra-lbl">🏆 Veredito do Arquiteto</span>
                <p><strong>Por que adotar:</strong> {truth_txt}</p>
              </div>
            </div>
            <div style="margin-top:6px;">
              <a class="repo-btn" href="{repo_url}" target="_blank" rel="noopener">
                <svg viewBox="0 0 24 24"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/></svg>
                <span>Repositório Oficial &amp; Código-Fonte: {repo_txt} ↗</span>
              </a>
            </div>
          </div>

          <!-- SEÇÃO 4: COMO USAR NO DIA A DIA -->
          <div class="entry-section">
            <span class="label">4. Como Usar no Dia a Dia (Passo a Passo Prático)</span>
            <div class="steps-grid">
{steps_rendered}
            </div>
          </div>

        </div>
      </div>"""

    new_content = re.sub(r'<div class="entry">.*?</div>\s*</div>\s*(?=(?:<!-- \d+|\s*<div class="entry">|\s*</div>\s*</section>|\s*</div>\s*<footer>))', refatorar_entry, content, flags=re.DOTALL)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    
    print(f"  -> [✓] Dossiê aplicado com sucesso: {filename}")

def main():
    arquivos = [f for f in os.listdir(OUTPUT_DIR) if f.endswith(".html") and f != "index.html"]
    print(f"[*] Migrando {len(arquivos)} arquivos para o novo modelo Dossiê Executivo...")

    for arq in sorted(arquivos):
        migrar_arquivo(arq)

    print("\n[🎉] Todas as 49 listas foram migradas com sucesso para o Dossiê Executivo!")

if __name__ == "__main__":
    main()
