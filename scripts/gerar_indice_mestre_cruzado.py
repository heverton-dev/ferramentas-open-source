# -*- coding: utf-8 -*-
import os
import sys
import json
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
sys.path.insert(0, str(BASE_DIR / "scripts"))

from estado_esteira import (
    obter_conexao,
    listar_catalogo_completo,
    obter_rastreabilidade_ferramenta,
    obter_estatisticas_catalogo
)

def escapar_html(texto: str) -> str:
    if not texto:
        return ""
    return str(texto).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")

def escapar_typst(texto: str) -> str:
    if not texto:
        return ""
    t = str(texto)
    subs = {
        "\\": "\\\\",
        "$": "\\$",
        "#": "\\#",
        "&": "\\&",
        "[": "\\[",
        "]": "\\]",
        "_": "\\_",
        "*": "\\*",
        "@": "\\@",
        "<": "\\<",
        ">": "\\>"
    }
    for orig, rep in subs.items():
        t = t.replace(orig, rep)
    return t

def compilar_indice_mestre_completo() -> bool:
    print("\n" + "=" * 80)
    print(" COMPILACAO DO PORTAL INDICE MESTRE (PADRAO DIAMANTE R5)")
    print("=" * 80)

    output_dir = BASE_DIR / "output"
    output_dir.mkdir(parents=True, exist_ok=True)

    html_out = output_dir / "INDICE-MESTRE.html"
    md_out   = output_dir / "INDICE-MESTRE.md"
    typ_out  = output_dir / "INDICE-MESTRE.typ"
    pdf_out  = output_dir / "INDICE-MESTRE.pdf"

    # 1. Carregar Dados do SQLite
    ferramentas = listar_catalogo_completo()
    stats = obter_estatisticas_catalogo()

    dados_consolidados = []
    for f in ferramentas:
        materiais = obter_rastreabilidade_ferramenta(f["slug"])
        dados_consolidados.append({
            "info": f,
            "materiais": materiais
        })

    # Ordenar por relevância
    dados_consolidados.sort(key=lambda x: (-len(x["materiais"]), -x["info"]["possui_manual_vps"], x["info"]["nome"]))

    print(f" [*] Ferramentas no Catalogo: {len(dados_consolidados)}")
    print(f" [*] Manuais de Engenharia VPS: {stats['total_manuais']}")
    print(f" [*] Dossies Verticais Mapeados: {stats['total_verticais']}")

    # -------------------------------------------------------------
    # 2. Compilacao MARKDOWN
    # -------------------------------------------------------------
    md_lines = [
        "# Indice Mestre - Catalogo Universal de Ferramentas Open Source",
        "",
        "> **Arsenal Open Source - Fabrica Universal AIDD (Padrao Diamante)**  ",
        f"> **Total de Ferramentas Catalogadas:** {len(dados_consolidados)} | **Dossies Verticais:** {stats['total_verticais']} | **Manuais VPS:** {stats['total_manuais']}  ",
        "> **Matriz de Rastreabilidade Biunivoca & Anti-Repeticao**  ",
        "",
        "---",
        "",
        "## Matriz Geral de Rastreabilidade Cruzada",
        "",
        "| Rank | Ferramenta | Licenca | SaaS Substituido | Manuais VPS | Ocorrencias & Materiais no Arsenal |",
        "| :---: | :--- | :---: | :--- | :---: | :--- |"
    ]

    for idx, item in enumerate(dados_consolidados, 1):
        f = item["info"]
        mats = item["materiais"]
        
        links_str = []
        for m in mats:
            tipo_label = {
                "horizontal": "Lista",
                "vertical": "Dossie",
                "manual_vps": "Manual VPS",
                "trilha": "Trilha"
            }.get(m["tipo_material"], m["tipo_material"].title())
            
            nome_mat = m.get("titulo_material") or m["origem_slug"]
            link_ref = m.get("caminho_html") or m.get("caminho_md") or "#"
            links_str.append(f"[{tipo_label}: {nome_mat}]({link_ref})")

        links_final = "<br>• ".join(links_str) if links_str else "_Em curadoria_"
        if links_str:
            links_final = "• " + links_final

        manual_badge = "Sim" if f["possui_manual_vps"] else "-"
        saas_sub = f.get("saas_substituidos") or "-"
        lic = f.get("licenca_osi") or "OSI"

        md_lines.append(f"| #{idx:03d} | **{f['nome']}** (`{f['slug']}`) | `{lic}` | {saas_sub} | {manual_badge} | {links_final} |")

    md_out.write_text("\n".join(md_lines), encoding="utf-8")
    print(f"   [OK] Markdown gerado: {md_out.name}")

    # -------------------------------------------------------------
    # 3. Compilacao HTML DIAMANTE R5
    # -------------------------------------------------------------
    cards_html = []
    tabela_linhas_html = []

    for idx, item in enumerate(dados_consolidados, 1):
        f = item["info"]
        mats = item["materiais"]
        slug = f["slug"]
        nome = f["nome"]
        lic = f["licenca_osi"] or "OSI"
        saas_sub = f["saas_substituidos"] or ""
        desc = f["descricao_canonica"] or "Solucao open source lider de alto desempenho para soberania tecnologica."
        is_vps = bool(f["possui_manual_vps"])

        badge_lic = f'<span class="lic-badge">{escapar_html(lic)}</span>'
        badge_vps = '<span class="vps-badge">VPS Pronto</span>' if is_vps else ''
        badge_killer = f'<span class="killer-badge">Substitui: {escapar_html(saas_sub)}</span>' if saas_sub else ''
        badge_docs = f'<span class="docs-count-badge">{len(mats)} Doc(s)</span>'

        mats_cards = []
        for m in mats:
            t_mat = m["tipo_material"]
            t_nome = {
                "horizontal": "Lista Horizontal",
                "vertical": "Dossie Vertical",
                "manual_vps": "Manual VPS",
                "trilha": "Trilha 5 Aulas"
            }.get(t_mat, t_mat.title())

            nome_mat = escapar_html(m.get("titulo_material") or m["origem_slug"])
            link_html = escapar_html(m.get("caminho_html") or "#")
            link_md = escapar_html(m.get("caminho_md") or "#")
            link_pdf = escapar_html(m.get("caminho_pdf") or "#")

            botoes_formato = []
            if link_html and link_html != "#":
                botoes_formato.append(f'<a href="{link_html}" target="_blank" class="fmt-btn fmt-html">HTML</a>')
            if link_md and link_md != "#":
                botoes_formato.append(f'<a href="{link_md}" target="_blank" class="fmt-btn fmt-md">MD</a>')
            if link_pdf and link_pdf != "#":
                botoes_formato.append(f'<a href="{link_pdf}" target="_blank" class="fmt-btn fmt-pdf">PDF</a>')

            botoes_str = " ".join(botoes_formato)

            mats_cards.append(f'''
            <div class="rel-mat-card">
              <div class="rel-mat-top">
                <span class="rel-mat-type">{t_nome}</span>
                <div class="rel-mat-links">{botoes_str}</div>
              </div>
              <div class="rel-mat-title">{nome_mat}</div>
            </div>
            ''')

        mats_rendered = "".join(mats_cards) if mats_cards else '<div class="no-mats">Ficha cadastrada no catalogo canonico.</div>'
        search_blob = f"{nome} {slug} {lic} {saas_sub} {f.get('categoria_primaria','')} {'vps' if is_vps else ''}".lower()

        card_markup = f'''
        <div class="entry" data-search="{escapar_html(search_blob)}" data-vps="{'true' if is_vps else 'false'}" data-saas="{'true' if saas_sub else 'false'}">
          <div class="entry-rank">#{idx:03d}</div>
          <div class="entry-body">
            
            <div class="entry-top">
              <div class="title-cluster">
                <h3>{escapar_html(nome)} <span class="tool-slug">({escapar_html(slug)})</span></h3>
              </div>
              <div class="badge-cluster">
                {badge_vps}
                {badge_killer}
                {badge_lic}
                {badge_docs}
              </div>
            </div>

            <div class="entry-section">
              <p class="tool-desc">{escapar_html(desc)}</p>
            </div>

            <div class="entry-section">
              <span class="sec-label">Rastreabilidade &amp; Materiais Disponiveis ({len(mats)})</span>
              <div class="rel-mats-grid">
                {mats_rendered}
              </div>
            </div>

          </div>
        </div>
        '''
        cards_html.append(card_markup)

        links_tab = []
        for m in mats:
            t_sigla = {"horizontal":"List","vertical":"Vert","manual_vps":"VPS","trilha":"Trilha"}.get(m["tipo_material"], "Doc")
            l_href = m.get("caminho_html") or m.get("caminho_md") or "#"
            links_tab.append(f'<a href="{escapar_html(l_href)}" target="_blank" class="table-link-pill">{t_sigla}</a>')
        links_tab_str = " ".join(links_tab) if links_tab else '<span style="color:var(--muted);">-</span>'

        tabela_linhas_html.append(f'''
        <tr data-search="{escapar_html(search_blob)}" data-vps="{'true' if is_vps else 'false'}" data-saas="{'true' if saas_sub else 'false'}">
          <td class="rank">#{idx:03d}</td>
          <td class="tool"><strong>{escapar_html(nome)}</strong><br><span style="font-size:11px;color:var(--muted);">{escapar_html(slug)}</span></td>
          <td class="lic"><span class="lic-badge">{escapar_html(lic)}</span></td>
          <td class="saas">{escapar_html(saas_sub) if saas_sub else '<span style="color:var(--muted);">-</span>'}</td>
          <td class="vps">{'<span class="vps-badge" style="font-size:10px;padding:2px 6px;">Pronto</span>' if is_vps else '<span style="color:var(--muted);">-</span>'}</td>
          <td class="links">{links_tab_str}</td>
        </tr>
        ''')

    cards_joined = "\n".join(cards_html)
    tabela_joined = "\n".join(tabela_linhas_html)

    diamante_css = """
    :root {
      --font-serif: "Liberation Serif", "Linux Libertine O", "Times New Roman", serif;
      --font-sans: "Liberation Sans", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
      --mono: "JetBrains Mono", "SF Mono", Menlo, Consolas, monospace;
      
      --paper: #0B1120;
      --surface: #111C33;
      --surface-2: #162442;
      --surface-hover: #1C2E54;
      --ink: #F8FAFC;
      --ink-2: #CBD5E1;
      --muted: #94A3B8;
      --rule: #1E293B;
      --rule-soft: #334155;
      
      --accent: #38BDF8;
      --accent-dark: #0284C7;
      --accent-soft: rgba(56, 189, 248, 0.12);
      
      --green: #34D399;
      --green-soft: rgba(52, 211, 153, 0.15);
      
      --gold: #FBBF24;
      --gold-soft: rgba(251, 191, 36, 0.15);
      
      --flag: #F87171;
      --flag-soft: rgba(248, 113, 113, 0.15);
      
      --shadow: 0 4px 20px rgba(0, 0, 0, 0.35);
      --shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.2);
    }

    *, *::before, *::after { box-sizing: border-box; }
    html { font-size: 16px; scroll-behavior: smooth; }
    body {
      margin: 0; padding: 0;
      background: var(--paper);
      color: var(--ink);
      font-family: var(--font-sans);
      line-height: 1.6;
      -webkit-font-smoothing: antialiased;
    }

    .wrap { max-width: 1200px; margin: 0 auto; padding: 40px 24px 80px; }

    header { margin-bottom: 32px; }
    .header-top { display: flex; align-items: center; justify-content: space-between; gap: 16px; margin-bottom: 20px; flex-wrap: wrap; }
    .back-link { font-family: var(--mono); font-size: 13px; color: var(--muted); text-decoration: none; display: inline-flex; align-items: center; gap: 8px; transition: color 0.2s; }
    .back-link:hover { color: var(--accent); }
    .camada-pill { font-family: var(--mono); font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: .08em; padding: 5px 12px; border-radius: 4px; background: var(--accent-soft); color: var(--accent); border: 1px solid var(--accent); }

    .hero { margin: 10px 0 24px; }
    h1 { font-family: var(--font-serif); font-size: clamp(30px, 4.5vw, 44px); line-height: 1.15; letter-spacing: -.02em; margin: 0 0 12px; color: var(--ink); text-align: justify; }
    .deck { font-size: 16.5px; line-height: 1.65; color: var(--ink-2); margin: 0; max-width: 100%; text-align: justify; }

    .hero-stats {
      display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 14px; margin: 28px 0 36px;
    }
    .stat-card {
      background: var(--surface); border: 1px solid var(--rule-soft); border-radius: 8px;
      padding: 16px 20px; box-shadow: var(--shadow-sm); position: relative; overflow: hidden;
    }
    .stat-card::after {
      content: ""; position: absolute; top: 0; left: 0; width: 4px; height: 100%; background: var(--accent);
    }
    .stat-card.green::after { background: var(--green); }
    .stat-card.gold::after { background: var(--gold); }
    .stat-card .num { font-family: var(--mono); font-size: 26px; font-weight: 700; color: var(--ink); margin-bottom: 2px; }
    .stat-card .lbl { font-size: 12px; color: var(--muted); text-transform: uppercase; letter-spacing: .06em; font-weight: 600; }

    .search-toolbar-diamante {
      background: var(--surface);
      border: 1px solid var(--rule-soft);
      border-radius: 12px;
      padding: 20px 24px;
      margin-bottom: 32px;
      box-shadow: var(--shadow);
      display: flex;
      flex-direction: column;
      gap: 16px;
    }
    .search-box-wrap {
      position: relative;
      width: 100%;
    }
    .search-box-wrap input {
      width: 100%;
      padding: 14px 20px 14px 48px;
      font-size: 15px;
      font-family: var(--font-sans);
      background: var(--paper);
      border: 1px solid var(--rule-soft);
      border-radius: 8px;
      color: var(--ink);
      outline: none;
      transition: border-color 0.2s, box-shadow 0.2s;
    }
    .search-box-wrap input:focus {
      border-color: var(--accent);
      box-shadow: 0 0 0 3px var(--accent-soft);
    }
    .search-icon-svg {
      position: absolute;
      left: 16px;
      top: 50%;
      transform: translateY(-50%);
      width: 20px;
      height: 20px;
      fill: var(--muted);
    }

    .toolbar-actions {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 12px;
    }
    .filter-pills {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      align-items: center;
    }
    .filter-label {
      font-size: 12px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: .06em;
      color: var(--muted);
      margin-right: 4px;
    }
    .filter-btn {
      background: var(--surface-2);
      color: var(--ink-2);
      border: 1px solid var(--rule-soft);
      padding: 6px 14px;
      border-radius: 20px;
      font-size: 12px;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s;
    }
    .filter-btn:hover, .filter-btn.active {
      background: var(--accent);
      color: #04101A;
      border-color: var(--accent);
      font-weight: 700;
    }

    .view-toggle {
      display: flex;
      background: var(--paper);
      border: 1px solid var(--rule-soft);
      border-radius: 6px;
      overflow: hidden;
    }
    .view-btn {
      background: transparent;
      border: none;
      color: var(--muted);
      padding: 6px 12px;
      font-size: 12px;
      font-weight: 600;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s;
    }
    .view-btn.active {
      background: var(--surface-2);
      color: var(--accent);
    }

    .entries-container { display: flex; flex-direction: column; gap: 20px; }
    
    .entry {
      display: grid;
      grid-template-columns: 70px 1fr;
      background: var(--surface);
      border: 1px solid var(--rule-soft);
      border-radius: 10px;
      overflow: hidden;
      box-shadow: var(--shadow-sm);
      transition: transform 0.2s, border-color 0.2s;
    }
    .entry:hover {
      border-color: var(--accent);
      transform: translateY(-2px);
    }
    @media (max-width: 768px) {
      .entry { grid-template-columns: 1fr; }
    }

    .entry-rank {
      background: var(--surface-2);
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: var(--mono);
      font-size: 18px;
      font-weight: 700;
      color: var(--accent);
      border-right: 1px solid var(--rule-soft);
      user-select: none;
    }

    .entry-body { padding: 22px 24px; display: flex; flex-direction: column; gap: 14px; }

    .entry-top {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      flex-wrap: wrap;
      gap: 12px;
    }
    .title-cluster h3 {
      font-family: var(--font-serif);
      font-size: 22px;
      margin: 0;
      color: var(--ink);
      display: flex;
      align-items: baseline;
      gap: 8px;
      flex-wrap: wrap;
    }
    .tool-slug {
      font-family: var(--mono);
      font-size: 13px;
      color: var(--muted);
      font-weight: 400;
    }

    .badge-cluster {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      align-items: center;
    }
    .lic-badge { font-family: var(--mono); font-size: 11px; padding: 3px 8px; border-radius: 4px; background: var(--surface-2); color: var(--ink-2); border: 1px solid var(--rule-soft); font-weight: 600; }
    .vps-badge { font-family: var(--mono); font-size: 11px; padding: 3px 8px; border-radius: 4px; background: var(--green-soft); color: var(--green); border: 1px solid var(--green); font-weight: 700; }
    .killer-badge { font-family: var(--mono); font-size: 11px; padding: 3px 8px; border-radius: 4px; background: var(--flag-soft); color: var(--flag); border: 1px solid var(--flag); font-weight: 600; }
    .docs-count-badge { font-family: var(--mono); font-size: 11px; padding: 3px 8px; border-radius: 4px; background: var(--accent-soft); color: var(--accent); border: 1px solid var(--accent); font-weight: 600; }

    .tool-desc {
      margin: 0;
      font-size: 14.5px;
      color: var(--ink-2);
      line-height: 1.5;
    }

    .sec-label {
      font-family: var(--mono);
      font-size: 11.5px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: .06em;
      color: var(--muted);
      display: block;
      margin-bottom: 8px;
    }

    .rel-mats-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
      gap: 10px;
    }
    .rel-mat-card {
      background: var(--surface-2);
      border: 1px solid var(--rule-soft);
      border-radius: 6px;
      padding: 10px 12px;
      display: flex;
      flex-direction: column;
      gap: 6px;
      transition: background 0.15s;
    }
    .rel-mat-card:hover { background: var(--surface-hover); border-color: var(--accent); }
    .rel-mat-top {
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .rel-mat-type {
      font-family: var(--mono);
      font-size: 11px;
      font-weight: 700;
      color: var(--accent);
    }
    .rel-mat-title {
      font-size: 13px;
      font-weight: 600;
      color: var(--ink);
      line-height: 1.3;
    }
    .rel-mat-links {
      display: flex;
      gap: 4px;
    }
    .fmt-btn {
      font-family: var(--mono);
      font-size: 10px;
      font-weight: 700;
      padding: 2px 6px;
      border-radius: 3px;
      text-decoration: none;
      transition: opacity 0.2s;
    }
    .fmt-btn:hover { opacity: 0.8; }
    .fmt-html { background: var(--accent-soft); color: var(--accent); border: 1px solid var(--accent); }
    .fmt-md { background: var(--gold-soft); color: var(--gold); border: 1px solid var(--gold); }
    .fmt-pdf { background: var(--green-soft); color: var(--green); border: 1px solid var(--green); }

    .no-mats {
      font-size: 13px;
      color: var(--muted);
      font-style: italic;
      padding: 6px 0;
    }

    .tablewrap { width: 100%; overflow-x: auto; margin: 16px 0 32px; background: var(--surface); border: 1px solid var(--rule-soft); border-radius: 8px; display: none; }
    table { width: 100%; border-collapse: collapse; font-size: 13.5px; text-align: left; }
    th { background: var(--surface-2); font-family: var(--mono); font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: .06em; color: var(--muted); padding: 12px 14px; border-bottom: 1px solid var(--rule-soft); }
    td { padding: 12px 14px; border-bottom: 1px solid var(--rule); color: var(--ink-2); }
    tr:last-child td { border-bottom: none; }
    td.rank { font-family: var(--mono); font-weight: 700; color: var(--accent); width: 60px; }
    td.tool strong { color: var(--ink); font-size: 14px; }
    td.saas { color: var(--flag); font-family: var(--mono); font-size: 12px; }
    .table-link-pill {
      display: inline-block;
      font-family: var(--mono);
      font-size: 10px;
      font-weight: 700;
      padding: 2px 6px;
      border-radius: 3px;
      background: var(--surface-2);
      color: var(--accent);
      border: 1px solid var(--rule-soft);
      text-decoration: none;
      margin-right: 4px;
    }
    .table-link-pill:hover { background: var(--accent); color: #04101A; }

    footer {
      margin-top: 60px;
      padding-top: 24px;
      border-top: 1px solid var(--rule);
      font-family: var(--mono);
      font-size: 12px;
      color: var(--muted);
      text-align: center;
    }
    """

    diamante_js = """
    <script>
    const searchInput = document.getElementById('searchInput');
    const entriesContainer = document.getElementById('entriesContainer');
    const entries = entriesContainer.getElementsByClassName('entry');
    const tableWrap = document.getElementById('tableWrap');
    const tableRows = tableWrap.querySelectorAll('tbody tr');
    const matchCounter = document.getElementById('matchCounter');
    
    let currentFilter = 'todos';
    let currentView = 'cards';

    function setFilter(tipo, btn) {
        currentFilter = tipo;
        document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
        if (btn) btn.classList.add('active');
        applyFilters();
    }

    function setView(view, btn) {
        currentView = view;
        document.querySelectorAll('.view-btn').forEach(b => b.classList.remove('active'));
        if (btn) btn.classList.add('active');
        
        if (view === 'cards') {
            entriesContainer.style.display = 'flex';
            tableWrap.style.display = 'none';
        } else {
            entriesContainer.style.display = 'none';
            tableWrap.style.display = 'block';
        }
        applyFilters();
    }

    function applyFilters() {
        const q = searchInput.value.toLowerCase().trim();
        let visibleCount = 0;

        for (let entry of entries) {
            const searchData = entry.getAttribute('data-search') || '';
            const isVps = entry.getAttribute('data-vps') === 'true';
            const isSaas = entry.getAttribute('data-saas') === 'true';

            let matchFilter = true;
            if (currentFilter === 'vps' && !isVps) matchFilter = false;
            if (currentFilter === 'saas' && !isSaas) matchFilter = false;

            const matchQuery = q === '' || searchData.includes(q);

            if (matchFilter && matchQuery) {
                entry.style.display = 'grid';
                visibleCount++;
            } else {
                entry.style.display = 'none';
            }
        }

        for (let row of tableRows) {
            const searchData = row.getAttribute('data-search') || '';
            const isVps = row.getAttribute('data-vps') === 'true';
            const isSaas = row.getAttribute('data-saas') === 'true';

            let matchFilter = true;
            if (currentFilter === 'vps' && !isVps) matchFilter = false;
            if (currentFilter === 'saas' && !isSaas) matchFilter = false;

            const matchQuery = q === '' || searchData.includes(q);

            if (matchFilter && matchQuery) {
                row.style.display = 'table-row';
            } else {
                row.style.display = 'none';
            }
        }

        matchCounter.textContent = 'Exibindo ' + visibleCount + ' de ' + entries.length + ' ferramentas';
    }

    searchInput.addEventListener('input', applyFilters);
    </script>
    """

    html_content = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Portal do Indice Mestre - Arsenal Open Source (Padrao Diamante)</title>
<style>
{diamante_css}
</style>
</head>
<body>
<div class="wrap">

  <header>
    <div class="header-top">
      <a href="./" class="back-link">← Arsenal Open Source · Fabrica Universal AIDD</a>
      <span class="camada-pill">HUB CENTRAL · CATALOGO MESTRE</span>
    </div>
    <div class="hero">
      <h1>Indice Mestre · Catalogo Universal &amp; Rastreabilidade Cruzada</h1>
      <p class="deck">Portal de busca instantanea e navegacao relacional biunivoca. Todas as ferramentas open source catalogadas no Arsenal estao mapeadas com seus respectivos Dossies Verticais de Desmantelamento SaaS, Listas Horizontais Tematicas e Manuais Operacionais de VPS com desinstalacao segura.</p>
    </div>

    <div class="hero-stats">
      <div class="stat-card">
        <div class="num">{len(dados_consolidados)}</div>
        <div class="lbl">Ferramentas Catalogadas</div>
      </div>
      <div class="stat-card gold">
        <div class="num">{stats['total_verticais']}</div>
        <div class="lbl">Dossies SaaS Verticais</div>
      </div>
      <div class="stat-card green">
        <div class="num">{stats['total_manuais']}</div>
        <div class="lbl">Manuais VPS Prontos</div>
      </div>
      <div class="stat-card">
        <div class="num">100%</div>
        <div class="lbl">Anti-Repeticao &amp; Rastreabilidade</div>
      </div>
    </div>
  </header>

  <div class="search-toolbar-diamante">
    <div class="search-box-wrap">
      <svg class="search-icon-svg" viewBox="0 0 24 24"><path d="M15.5 14h-.79l-.28-.27A6.471 6.471 0 0 0 16 9.5 6.5 6.5 0 1 0 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"/></svg>
      <input type="text" id="searchInput" placeholder="Buscar por ferramenta, SaaS substituido (ex: Twilio, Notion, Salesforce), licenca ou tag..." autofocus>
    </div>

    <div class="toolbar-actions">
      <div class="filter-pills">
        <span class="filter-label">Filtros:</span>
        <button class="filter-btn active" onclick="setFilter('todos', this)">Todas ({len(dados_consolidados)})</button>
        <button class="filter-btn" onclick="setFilter('vps', this)">Com Manual VPS ({stats['total_manuais']})</button>
        <button class="filter-btn" onclick="setFilter('saas', this)">Substitutos SaaS</button>
        <span id="matchCounter" style="font-family:var(--mono);font-size:12px;color:var(--muted);margin-left:8px;">Exibindo {len(dados_consolidados)} de {len(dados_consolidados)} ferramentas</span>
      </div>

      <div class="view-toggle">
        <button class="view-btn active" onclick="setView('cards', this)">Cards</button>
        <button class="view-btn" onclick="setView('table', this)">Tabela</button>
      </div>
    </div>
  </div>

  <div class="entries-container" id="entriesContainer">
    {cards_joined}
  </div>

  <div class="tablewrap" id="tableWrap">
    <table>
      <thead>
        <tr>
          <th>Rank</th>
          <th>Ferramenta Open Source</th>
          <th>Licenca</th>
          <th>SaaS Concorrente</th>
          <th>VPS</th>
          <th>Materiais no Arsenal</th>
        </tr>
      </thead>
      <tbody>
        {tabela_joined}
      </tbody>
    </table>
  </div>

  <footer>
    Arsenal Open Source · Fabrica Universal AIDD — Catalogo Mestre Persistido no SQLite (estado_esteira.db)
  </footer>

</div>

{diamante_js}
</body>
</html>"""

    html_out.write_text(html_content, encoding="utf-8")
    print(f"   [OK] HTML Diamante R5 gerado: {html_out.name}")

    # -------------------------------------------------------------
    # 4. Compilacao PDF TYPST
    # -------------------------------------------------------------
    typ_linhas = [
        '#set page(',
        '  paper: "a4",',
        '  flipped: true,',
        '  margin: (x: 1.2cm, y: 1.2cm),',
        '  header: align(right)[#text(8pt, fill: rgb("#64748b"))[Arsenal Open Source - Catalogo Mestre & Indice Universal]],',
        '  footer: context [#align(center)[#text(8pt, fill: rgb("#64748b"))[Fabrica Universal - Pagina #counter(page).display() de #counter(page).final().first()]]]',
        ')',
        '#set text(font: "Liberation Sans", size: 8pt, lang: "pt", fill: rgb("#0f172a"))',
        '#set par(justify: true, leading: 0.5em)',
        '',
        '#block(',
        '  fill: rgb("#f1f5f9"), inset: 10pt, radius: 4pt, stroke: 1pt + rgb("#cbd5e1"), width: 100%,',
        '  [',
        '    #text(8pt, weight: "bold", fill: rgb("#0284c7"))[INDICE MESTRE & CATALOGO CANONICO DE FERRAMENTAS OPEN SOURCE]',
        '    #v(2pt)',
        f'    #text(13pt, weight: "bold", fill: rgb("#0f172a"))[Arsenal Open Source - Rastreabilidade Biunivoca ({len(dados_consolidados)} Ferramentas)]',
        '    #v(2pt)',
        f'    #text(8pt, fill: rgb("#475569"))[Dossies Verticais: {stats["total_verticais"]} SaaS | Manuais VPS: {stats["total_manuais"]} | Data: 27/08/2026]',
        '  ]',
        ')',
        '#v(6pt)',
        '#table(',
        '  columns: (2fr, 0.9fr, 1.8fr, 0.9fr, 3.5fr),',
        '  fill: (x, y) => if y == 0 { rgb("#0f172a") } else { if calc.even(y) { rgb("#f8fafc") } else { white } },',
        '  stroke: 0.5pt + rgb("#cbd5e1"),',
        '  [#text(weight: "bold", fill: white)[Ferramenta]],',
        '  [#text(weight: "bold", fill: white)[Licenca]],',
        '  [#text(weight: "bold", fill: white)[SaaS Substituido]],',
        '  [#text(weight: "bold", fill: white)[VPS]],',
        '  [#text(weight: "bold", fill: white)[Materiais no Arsenal]],'
    ]

    for item in dados_consolidados:
        f = item["info"]
        mats = item["materiais"]

        mats_typ_arr = []
        for m in mats:
            tipo_label = {
                "horizontal": "Lista",
                "vertical": "Dossie",
                "manual_vps": "VPS",
                "trilha": "Trilha"
            }.get(m["tipo_material"], m["tipo_material"])
            nom = escapar_typst(m.get("titulo_material") or m["origem_slug"])
            mats_typ_arr.append(f"{tipo_label}: {nom}")

        mats_str = "; ".join(mats_typ_arr) if mats_typ_arr else "-"
        if len(mats_str) > 80:
            mats_str = mats_str[:77] + "..."

        nome_typ = escapar_typst(f["nome"])
        lic_typ = escapar_typst(f["licenca_osi"] or "OSI")
        saas_typ = escapar_typst(f["saas_substituidos"] or "-")
        vps_typ = "Sim" if f["possui_manual_vps"] else "-"

        typ_linhas.append(f'  [*{nome_typ}*], [{lic_typ}], [{saas_typ}], [{vps_typ}], [{mats_str}],')

    typ_linhas.append(')')

    typ_out.write_text("\n".join(typ_linhas), encoding="utf-8")
    
    try:
        res = subprocess.run(['typst', 'compile', '--root', str(BASE_DIR), str(typ_out), str(pdf_out)], capture_output=True, encoding="utf-8", errors="replace")
        if res.returncode == 0:
            print(f"   [OK] PDF Typst compilado: {pdf_out.name}")
        else:
            print(f"   [AVISO] Typst error: {res.stderr[:300]}")
    finally:
        if typ_out.exists():
            typ_out.unlink()

    print("\n" + "=" * 80)
    print(" PORTAL DO INDICE MESTRE COMPILADO NO PADRAO DIAMANTE COM SUCESSO!")
    print("=" * 80)
    return True

if __name__ == "__main__":
    compilar_indice_mestre_completo()
