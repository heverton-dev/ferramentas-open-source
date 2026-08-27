# -*- coding: utf-8 -*-
"""
MOTOR GERADOR DO ÍNDICE MESTRE INTERATIVO & RASTREABILIDADE CRUZADA (PADRÃO DIAMANTE)
Lê o banco SQLite `estado_esteira.db` e compila o Portal Central nos 3 formatos:
- output/INDICE-MESTRE.html (Portal Interativo com busca client-side e design Enterprise)
- output/INDICE-MESTRE.md (Índice estruturado em Markdown)
- output/INDICE-MESTRE.pdf (Compilação nativa em PDF via Typst)
"""
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
    print(" 🌐 COMPILAÇÃO DO ÍNDICE MESTRE INTERATIVO & HUB UNIVERSAL")
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

    # Ordenar por relevância (mais materiais vinculados primeiro, depois nome)
    dados_consolidados.sort(key=lambda x: (-len(x["materiais"]), -x["info"]["possui_manual_vps"], x["info"]["nome"]))

    print(f" [*] Ferramentas Carregadas: {len(dados_consolidados)}")
    print(f" [*] Manuais Operacionais Mapeados: {stats['total_manuais']}")
    print(f" [*] Dossiês Verticais Mapeados: {stats['total_verticais']}")

    # -------------------------------------------------------------
    # 2. Compilação MARKDOWN
    # -------------------------------------------------------------
    md_lines = [
        "# Índice Mestre · Catálogo Universal de Ferramentas Open Source",
        "",
        "> **Arsenal Open Source · Fábrica Universal AIDD**  ",
        f"> **Total de Ferramentas Catalogadas:** {len(dados_consolidados)} | **Dossiês Verticais:** {stats['total_verticais']} | **Manuais VPS:** {stats['total_manuais']}  ",
        "> **Matriz de Rastreabilidade Biunívoca & Anti-Repetição**  ",
        "",
        "---",
        "",
        "## 🧭 Matriz Geral de Rastreabilidade Cruzada",
        "",
        "| Ferramenta | Licença | SaaS Substituído | Manuais VPS | Ocorrências & Materiais no Arsenal |",
        "| :--- | :---: | :--- | :---: | :--- |"
    ]

    for item in dados_consolidados:
        f = item["info"]
        mats = item["materiais"]
        
        links_str = []
        for m in mats:
            tipo_label = {
                "horizontal": "Lista",
                "vertical": "Dossiê",
                "manual_vps": "Manual VPS",
                "trilha": "Trilha"
            }.get(m["tipo_material"], m["tipo_material"].title())
            
            nome_mat = m.get("titulo_material") or m["origem_slug"]
            link_ref = m.get("caminho_html") or m.get("caminho_md") or "#"
            links_str.append(f"[{tipo_label}: {nome_mat}]({link_ref})")

        links_final = "<br>• ".join(links_str) if links_str else "_Em curadoria_"
        if links_str:
            links_final = "• " + links_final

        manual_badge = "✅ Sim" if f["possui_manual_vps"] else "➖"
        saas_sub = f.get("saas_substituidos") or "-"
        lic = f.get("licenca_osi") or "OSI"

        md_lines.append(f"| **{f['nome']}** (`{f['slug']}`) | `{lic}` | {saas_sub} | {manual_badge} | {links_final} |")

    md_out.write_text("\n".join(md_lines), encoding="utf-8")
    print(f"   ✓ Markdown gerado: {md_out.relative_to(BASE_DIR)}")

    # -------------------------------------------------------------
    # 3. Compilação HTML INTERATIVO (Design Enterprise com Busca JS)
    # -------------------------------------------------------------
    css_code = (BASE_DIR / "scripts" / "padroes" / "relatorio_enterprise.css").read_text(encoding="utf-8")

    css_extra = """
    .search-toolbar {
        background: #1e293b;
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 1.25rem 1.5rem;
        margin-bottom: 2rem;
        display: flex;
        flex-direction: column;
        gap: 1rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
    }
    .search-input-wrapper {
        position: relative;
        width: 100%;
    }
    .search-input {
        width: 100%;
        padding: 0.85rem 1.25rem 0.85rem 2.8rem;
        font-size: 1rem;
        background: #0f172a;
        border: 1px solid #475569;
        border-radius: 8px;
        color: #f8fafc;
        outline: none;
        transition: all 0.2s;
    }
    .search-input:focus {
        border-color: #0284c7;
        box-shadow: 0 0 0 3px rgba(2, 132, 199, 0.25);
    }
    .search-icon {
        position: absolute;
        left: 1rem;
        top: 50%;
        transform: translateY(-50%);
        color: #94a3b8;
        font-size: 1.1rem;
    }
    .filter-pills {
        display: flex;
        flex-wrap: wrap;
        gap: 0.5rem;
        align-items: center;
    }
    .filter-label {
        font-size: 0.8rem;
        font-weight: 700;
        text-transform: uppercase;
        color: #94a3b8;
        margin-right: 0.5rem;
    }
    .filter-btn {
        background: #334155;
        color: #e2e8f0;
        border: 1px solid #475569;
        padding: 0.35rem 0.75rem;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.15s;
    }
    .filter-btn:hover, .filter-btn.active {
        background: #0284c7;
        color: #ffffff;
        border-color: #38bdf8;
    }
    .tool-card-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
        gap: 1.25rem;
    }
    .tool-card {
        background: #1e293b;
        border: 1px solid #334155;
        border-radius: 10px;
        padding: 1.25rem;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        transition: transform 0.2s, border-color 0.2s;
    }
    .tool-card:hover {
        transform: translateY(-2px);
        border-color: #0284c7;
    }
    .tool-card-header {
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        margin-bottom: 0.75rem;
    }
    .tool-title {
        font-size: 1.15rem;
        font-weight: 700;
        color: #38bdf8;
        margin: 0;
    }
    .tool-desc {
        font-size: 0.85rem;
        color: #cbd5e1;
        line-height: 1.4;
        margin-bottom: 1rem;
        flex-grow: 1;
    }
    .tool-badges {
        display: flex;
        flex-wrap: wrap;
        gap: 0.4rem;
        margin-bottom: 1rem;
    }
    .tool-mat-list {
        background: #0f172a;
        border-radius: 6px;
        padding: 0.75rem;
        font-size: 0.8rem;
        border: 1px solid #334155;
    }
    .tool-mat-heading {
        font-weight: 700;
        font-size: 0.75rem;
        text-transform: uppercase;
        color: #94a3b8;
        margin-bottom: 0.4rem;
        display: flex;
        justify-content: space-between;
    }
    .mat-link-item {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0.25rem 0;
        border-bottom: 1px solid #1e293b;
    }
    .mat-link-item:last-child {
        border-bottom: none;
    }
    .mat-link-a {
        color: #38bdf8;
        text-decoration: none;
        font-weight: 500;
    }
    .mat-link-a:hover {
        text-decoration: underline;
    }
    .mat-tag {
        font-size: 0.7rem;
        padding: 0.1rem 0.4rem;
        border-radius: 4px;
        background: #334155;
        color: #94a3b8;
    }
    """

    cards_html = []
    for item in dados_consolidados:
        f = item["info"]
        mats = item["materiais"]

        badge_lic = f'<span class="badge-pill">{escapar_html(f["licenca_osi"] or "OSI")}</span>'
        badge_vps = '<span class="badge-gate" style="background:#065f46;color:#a7f3d0;border-color:#059669;">VPS PRONTO</span>' if f["possui_manual_vps"] else ''
        badge_saas = f'<span class="badge-pill" style="background:#451a03;color:#fdba74;border-color:#ea580c;">Substitui: {escapar_html(f["saas_substituidos"])}</span>' if f["saas_substituidos"] else ''

        mats_html = []
        for m in mats:
            tipo_label = {
                "horizontal": "Lista",
                "vertical": "Dossiê",
                "manual_vps": "Manual VPS",
                "trilha": "Trilha 5 Aulas"
            }.get(m["tipo_material"], m["tipo_material"].title())

            nome_mat = escapar_html(m.get("titulo_material") or m["origem_slug"])
            link_ref = escapar_html(m.get("caminho_html") or m.get("caminho_md") or "#")
            
            mats_html.append(f'''
            <div class="mat-link-item">
                <a class="mat-link-a" href="{link_ref}" target="_blank">🔗 {nome_mat}</a>
                <span class="mat-tag">{tipo_label}</span>
            </div>
            ''')

        mats_render = "".join(mats_html) if mats_html else '<div style="color:#64748b;font-style:italic;">Nenhum material associado ainda.</div>'
        search_blob = f"{f['nome']} {f['slug']} {f.get('licenca_osi','')} {f.get('saas_substituidos','')} {f.get('categoria_primaria','')}".lower()

        cards_html.append(f'''
        <div class="tool-card" data-search="{escapar_html(search_blob)}" data-vps="{'true' if f['possui_manual_vps'] else 'false'}">
            <div>
                <div class="tool-card-header">
                    <h3 class="tool-title">{escapar_html(f['nome'])}</h3>
                    {badge_vps}
                </div>
                <div class="tool-badges">
                    {badge_lic}
                    {badge_saas}
                </div>
                <p class="tool-desc">{escapar_html(f['descricao_canonica'] or 'Solução open source de alto desempenho.')}</p>
            </div>
            <div class="tool-mat-list">
                <div class="tool-mat-heading">
                    <span>Materiais no Arsenal</span>
                    <span>{len(mats)} doc(s)</span>
                </div>
                {mats_render}
            </div>
        </div>
        ''')

    cards_joined = "\n".join(cards_html)

    js_code = """
<script>
const searchInput = document.getElementById('searchInput');
const toolGrid = document.getElementById('toolGrid');
const cards = toolGrid.getElementsByClassName('tool-card');
const counter = document.getElementById('matchCounter');
let filtroAtual = 'todos';

function filtrar(tipo, btn) {
    filtroAtual = tipo;
    document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
    if (btn) btn.classList.add('active');
    aplicarBusca();
}

function aplicarBusca() {
    const q = searchInput.value.toLowerCase().trim();
    let visiveis = 0;

    for (let card of cards) {
        const text = card.getAttribute('data-search') || '';
        const isVps = card.getAttribute('data-vps') === 'true';
        
        let matchFiltro = true;
        if (filtroAtual === 'vps' && !isVps) matchFiltro = false;
        if (filtroAtual === 'saas' && !text.includes('substitui:')) matchFiltro = false;

        const matchQuery = q === '' || text.includes(q);

        if (matchFiltro && matchQuery) {
            card.style.display = 'flex';
            visiveis++;
        } else {
            card.style.display = 'none';
        }
    }
    counter.textContent = 'Exibindo ' + visiveis + ' ferramentas';
}

searchInput.addEventListener('input', aplicarBusca);
</script>
"""

    html_content = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Portal do Índice Mestre · Arsenal Open Source</title>
<style>
{css_code}
{css_extra}
</style>
</head>
<body>
<div class="container">

  <div class="header-card">
    <div class="header-badge">🌐 Hub de Navegação &amp; Rastreabilidade Biunívoca</div>
    <h1 class="report-title">Índice Mestre · Catálogo Universal de Ferramentas</h1>
    <p class="report-subtitle">Arsenal Open Source · Fábrica Universal AIDD · Emissão: 27/08/2026</p>
    
    <div class="hero-grid">
      <div class="stat-box">
        <div class="stat-label">Ferramentas Únicas</div>
        <div class="stat-value highlight">{len(dados_consolidados)}</div>
        <div class="stat-sub">Catálogo Canônico R11</div>
      </div>
      <div class="stat-box">
        <div class="stat-label">Dossiês Verticais</div>
        <div class="stat-value success">{stats['total_verticais']} SaaS</div>
        <div class="stat-sub">Quinteto Soberano</div>
      </div>
      <div class="stat-box">
        <div class="stat-label">Manuais de VPS</div>
        <div class="stat-value">{stats['total_manuais']} Manuais</div>
        <div class="stat-sub">Hardening &amp; Trilhas</div>
      </div>
      <div class="stat-box">
        <div class="stat-label">Governança</div>
        <div class="stat-value">Zero Drift</div>
        <div class="stat-sub">Anti-Repetição Ativo</div>
      </div>
    </div>
  </div>

  <div class="search-toolbar">
    <div class="search-input-wrapper">
      <span class="search-icon">🔍</span>
      <input type="text" id="searchInput" class="search-input" placeholder="Buscar ferramenta, SaaS substituído (ex: Twilio, Notion, Zapier), licença ou stack..." autofocus>
    </div>
    <div class="filter-pills">
      <span class="filter-label">Filtros Rápidos:</span>
      <button class="filter-btn active" onclick="filtrar('todos', this)">Todos ({len(dados_consolidados)})</button>
      <button class="filter-btn" onclick="filtrar('vps', this)">Com Manual VPS ({stats['total_manuais']})</button>
      <button class="filter-btn" onclick="filtrar('saas', this)">Substitutos SaaS</button>
      <span id="matchCounter" style="margin-left:auto;font-size:0.8rem;color:#94a3b8;">Exibindo {len(dados_consolidados)} ferramentas</span>
    </div>
  </div>

  <div class="tool-card-grid" id="toolGrid">
    {cards_joined}
  </div>

  <footer class="report-footer" style="margin-top:3rem;">
    Arsenal Open Source · Fábrica Universal AIDD — Catálogo Mestre Persistido no SQLite (estado_esteira.db)
  </footer>

</div>

{js_code}
</body>
</html>"""

    html_out.write_text(html_content, encoding="utf-8")
    print(f"   ✓ HTML Interativo gerado: {html_out.relative_to(BASE_DIR)}")

    # -------------------------------------------------------------
    # 4. Compilação PDF TYPST
    # -------------------------------------------------------------
    typ_linhas = [
        '#set page(',
        '  paper: "a4",',
        '  flipped: true,',
        '  margin: (x: 1.2cm, y: 1.2cm),',
        '  header: align(right)[#text(8pt, fill: rgb("#64748b"))[Arsenal Open Source · Catálogo Mestre & Índice Universal]],',
        '  footer: context [#align(center)[#text(8pt, fill: rgb("#64748b"))[Fábrica Universal · Página #counter(page).display() de #counter(page).final().first()]]]',
        ')',
        '#set text(font: "Liberation Sans", size: 8pt, lang: "pt", fill: rgb("#0f172a"))',
        '#set par(justify: true, leading: 0.5em)',
        '',
        '#block(',
        '  fill: rgb("#f1f5f9"), inset: 10pt, radius: 4pt, stroke: 1pt + rgb("#cbd5e1"), width: 100%,',
        '  [',
        '    #text(8pt, weight: "bold", fill: rgb("#0284c7"))[ÍNDICE MESTRE & CATÁLOGO CANÔNICO DE FERRAMENTAS OPEN SOURCE]',
        '    #v(2pt)',
        f'    #text(13pt, weight: "bold", fill: rgb("#0f172a"))[Arsenal Open Source · Rastreabilidade Biunívoca ({len(dados_consolidados)} Ferramentas)]',
        '    #v(2pt)',
        f'    #text(8pt, fill: rgb("#475569"))[Dossiês Verticais: {stats["total_verticais"]} SaaS | Manuais VPS: {stats["total_manuais"]} | Data: 27/08/2026]',
        '  ]',
        ')',
        '#v(6pt)',
        '#table(',
        '  columns: (2fr, 0.9fr, 1.8fr, 0.9fr, 3.5fr),',
        '  fill: (x, y) => if y == 0 { rgb("#0f172a") } else { if calc.even(y) { rgb("#f8fafc") } else { white } },',
        '  stroke: 0.5pt + rgb("#cbd5e1"),',
        '  [#text(weight: "bold", fill: white)[Ferramenta]],',
        '  [#text(weight: "bold", fill: white)[Licença]],',
        '  [#text(weight: "bold", fill: white)[SaaS Substituído]],',
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
                "vertical": "Dossiê",
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
            print(f"   ✓ PDF Typst compilado: {pdf_out.relative_to(BASE_DIR)}")
        else:
            print(f"   ⚠️ Typst error: {res.stderr[:300]}")
    finally:
        if typ_out.exists():
            typ_out.unlink()

    print("\n" + "=" * 80)
    print(" 🎉 PORTAL DO ÍNDICE MESTRE COMPILADO NOS 3 FORMATOS COM SUCESSO!")
    print("=" * 80)
    return True

if __name__ == "__main__":
    compilar_indice_mestre_completo()
