#!/usr/bin/env python3
"""
Gerador do Portal Visual Interativo & README de Perfil da organização arsenal-open-source.
Cruza todos os repositórios da organização com os 32 compêndios de soberania e gera:
1. output/index-arsenal-open-source.html (Portal Web com busca e filtros em tempo real)
2. temp_org_repo/profile/README.md (Perfil oficial da organização no GitHub)
"""

import os
import sys
import glob
import re
import json
import subprocess

def console_utf8():
    if sys.platform == "win32":
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")

def obter_repos_da_org(org_name="arsenal-open-source"):
    print(f"[*] Consultando catálogo de repositórios em {org_name}...")
    cmd = ["gh", "repo", "list", org_name, "--limit", "500", "--json", "name,description,url,isFork,parent,createdAt,updatedAt"]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    if res.returncode == 0:
        return json.loads(res.stdout)
    return []

def carregar_metadados_listas():
    # Mapear camada -> nome e arquivo
    mapa = {}
    html_files = glob.glob("output/listas-open-source/*.html")
    for f in html_files:
        base = os.path.basename(f)
        with open(f, "r", encoding="utf-8") as file:
            content = file.read()
        # Extrair h1
        h1_match = re.search(r'<h1>(.*?)</h1>', content, re.DOTALL)
        title = h1_match.group(1).replace("&nbsp;", " ").strip() if h1_match else base
        # Extrair repos citados
        matches = re.findall(r'github\.com/([a-zA-Z0-9_\-\.]+/[a-zA-Z0-9_\-\.]+)', content)
        for m in matches:
            repo_name = m.split("/")[-1].lower()
            if repo_name not in mapa:
                mapa[repo_name] = []
            mapa[repo_name].append({"lista": base, "titulo": title})
    return mapa

def gerar_portal_html(repos, meta_mapa):
    total = len(repos)
    print(f"[*] Gerando Portal Web para {total} tecnologias custodiadas...")

    cards_html = []
    for r in sorted(repos, key=lambda x: x["name"].lower()):
        name = r["name"]
        desc = r.get("description") or "Repositório de código aberto sob custódia e preservação soberana."
        url = r.get("url") or f"https://github.com/arsenal-open-source/{name}"
        parent = r.get("parent") or {}
        parent_slug = parent.get("nameWithOwner") or name
        
        origens = meta_mapa.get(name.lower(), [])
        origem_badge = origens[0]["titulo"] if origens else "Arsenal de Soberania"
        origem_badge_clean = re.sub(r'<.*?>', '', origem_badge)[:38]

        card = f"""
        <div class="repo-card" data-name="{name.lower()}" data-desc="{desc.lower()}" data-cat="{origem_badge_clean.lower()}">
          <div class="card-head">
            <span class="card-badge">{origem_badge_clean}</span>
            <a href="{url}" target="_blank" rel="noopener" class="fork-link">Ver Fork ↗</a>
          </div>
          <h3 class="repo-title">{name}</h3>
          <p class="repo-desc">{desc}</p>
          <div class="card-foot">
            <span class="upstream">Origem: <b>{parent_slug}</b></span>
            <a href="https://github.com/{parent_slug}" target="_blank" rel="noopener" class="upstream-link">Upstream</a>
          </div>
        </div>
        """
        cards_html.append(card)

    cards_joined = "\n".join(cards_html)

    html_template = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Portal do Arsenal Open Source · Catálogo de Soberania Tecnológica</title>
<style>
  * {{ scrollbar-width: thin; scrollbar-color: var(--accent) transparent; box-sizing: border-box; }}
  ::-webkit-scrollbar {{ width: 4px; height: 4px; }}
  ::-webkit-scrollbar-track {{ background: transparent; }}
  ::-webkit-scrollbar-thumb {{ background: var(--accent); border-radius: 4px; }}

  :root {{
    --paper:#ECEEF2; --surface:#F8F9FC; --surface-2:#DFE3EB;
    --ink:#151A26; --ink-2:#3B4457; --muted:#68738A;
    --rule:#C7CEDB; --rule-soft:#DADFE8;
    --accent:#1A446C; --accent-soft:#DCE7F2;
    --gold:#7A5410; --gold-soft:#EFE5CE;
    --green:#1B5E3B; --green-soft:#D8EFE2;
    --shadow: 0 1px 0 rgba(21,26,38,.05), 0 8px 24px -18px rgba(21,26,38,.45);
    --serif:"Iowan Old Style","Palatino Linotype",Palatino,Georgia,serif;
    --sans:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;
    --mono:ui-monospace,"Cascadia Mono","SF Mono",Menlo,monospace;
  }}
  @media (prefers-color-scheme: dark) {{
    :root:not([data-theme="light"]) {{
      --paper:#0E1118; --surface:#161A24; --surface-2:#1F2531;
      --ink:#E3E7F0; --ink-2:#B3BCCC; --muted:#8391A8;
      --rule:#2A3142; --rule-soft:#222836;
      --accent:#7AA5D6; --accent-soft:#162436;
      --gold:#D6A44E; --gold-soft:#332810;
      --green:#6BC48F; --green-soft:#122B1C;
      --shadow: 0 1px 0 rgba(0,0,0,.3), 0 8px 24px -18px rgba(0,0,0,.9);
    }}
  }}

  body {{ margin:0; background:var(--paper); color:var(--ink); font-family:var(--sans); font-size:15px; line-height:1.5; }}
  .wrap {{ max-width:1160px; margin:0 auto; padding:clamp(24px,4vw,56px) clamp(16px,3vw,36px) 80px; display:flex; flex-direction:column; gap:36px; }}

  header {{ display:flex; flex-direction:column; gap:16px; }}
  .eyebrow {{ font-family:var(--mono); font-size:11.5px; letter-spacing:.14em; text-transform:uppercase; color:var(--muted); display:flex; flex-wrap:wrap; gap:6px 14px; align-items:baseline; }}
  .eyebrow b {{ color:var(--accent); font-weight:600; }}
  h1 {{ font-family:var(--serif); font-weight:600; font-size:clamp(36px,6vw,64px); line-height:.98; letter-spacing:-.02em; margin:0; }}
  .deck {{ font-family:var(--serif); font-size:clamp(16px,2vw,19px); line-height:1.45; color:var(--ink-2); max-width:68ch; margin:0; }}
  
  .search-bar {{ display:flex; gap:12px; flex-wrap:wrap; background:var(--surface); padding:12px 16px; border:1px solid var(--rule); border-radius:4px; box-shadow:var(--shadow); }}
  .search-input {{ flex:1; min-width:260px; padding:10px 14px; border:1px solid var(--rule); border-radius:3px; background:var(--paper); color:var(--ink); font-family:var(--sans); font-size:14.5px; outline:none; }}
  .search-input:focus {{ border-color:var(--accent); }}
  .stats-badge {{ font-family:var(--mono); font-size:12px; align-self:center; color:var(--muted); white-space:nowrap; }}
  .stats-badge b {{ color:var(--accent); }}

  .grid {{ display:grid; grid-template-columns:repeat(auto-fill, minmax(320px, 1fr)); gap:16px; }}
  .repo-card {{ background:var(--surface); border:1px solid var(--rule); border-radius:4px; padding:18px; display:flex; flex-direction:column; gap:10px; transition:border-color .15s, box-shadow .15s; }}
  .repo-card:hover {{ border-color:var(--accent); box-shadow:var(--shadow); }}
  .card-head {{ display:flex; justify-content:space-between; align-items:flex-start; gap:8px; }}
  .card-badge {{ font-family:var(--mono); font-size:10px; letter-spacing:.05em; text-transform:uppercase; background:var(--accent-soft); color:var(--accent); padding:3px 7px; border-radius:2px; font-weight:600; }}
  .fork-link {{ font-family:var(--mono); font-size:11px; text-decoration:none; color:var(--accent); font-weight:600; }}
  .fork-link:hover {{ text-decoration:underline; }}
  .repo-title {{ font-family:var(--serif); font-size:21px; font-weight:600; margin:0; color:var(--ink); line-height:1.2; }}
  .repo-desc {{ font-size:13.5px; color:var(--ink-2); margin:0; line-height:1.45; display:-webkit-box; -webkit-line-clamp:3; -webkit-box-orient:vertical; overflow:hidden; }}
  .card-foot {{ margin-top:auto; padding-top:10px; border-top:1px dashed var(--rule-soft); display:flex; justify-content:space-between; align-items:baseline; font-size:11.5px; color:var(--muted); font-family:var(--mono); }}
  .upstream-link {{ color:var(--muted); text-decoration:none; }}
  .upstream-link:hover {{ color:var(--ink); text-decoration:underline; }}

  footer {{ border-top:1px solid var(--rule); padding-top:18px; font-size:13px; color:var(--muted); display:flex; justify-content:space-between; flex-wrap:wrap; gap:10px; }}
</style>
</head>
<body>

<div class="wrap">
  <header>
    <div class="eyebrow">
      <span>Organização Oficial</span><span>·</span><span>GitHub: @arsenal-open-source</span><span>·</span>
      <b>{total} Tecnologias Sob Custódia</b>
    </div>
    <h1>Portal do Arsenal Open Source</h1>
    <p class="deck">Índice visual interativo de todas as tecnologias de código aberto custodiadas, sincronizadas e preservadas contra descontinuidade e lock-in corporativo.</p>
  </header>

  <div class="search-bar">
    <input type="text" id="filterInput" class="search-input" placeholder="Filtrar por nome, categoria ou descrição (ex: ERP, 3D, Ollama, CRM, ComfyUI)..." onkeyup="filtrarRepos()">
    <div class="stats-badge" id="statsCount">Exibindo <b>{total}</b> de <b>{total}</b> projetos</div>
  </div>

  <div class="grid" id="reposGrid">
    {cards_joined}
  </div>

  <footer>
    <span>Arsenal Open Source · Todos os forks sincronizados automaticamente via GitHub Actions.</span>
    <a href="https://github.com/arsenal-open-source" target="_blank" style="color:var(--accent);font-family:var(--mono);text-decoration:none;font-weight:600;">github.com/arsenal-open-source ↗</a>
  </footer>
</div>

<script>
function filtrarRepos() {{
  const query = document.getElementById('filterInput').value.toLowerCase().trim();
  const cards = document.querySelectorAll('.repo-card');
  let visibleCount = 0;

  cards.forEach(card => {{
    const name = card.getAttribute('data-name') || '';
    const desc = card.getAttribute('data-desc') || '';
    const cat = card.getAttribute('data-cat') || '';

    if (name.includes(query) || desc.includes(query) || cat.includes(query)) {{
      card.style.display = 'flex';
      visibleCount++;
    }} else {{
      card.style.display = 'none';
    }}
  }});

  document.getElementById('statsCount').innerHTML = `Exibindo <b>${{visibleCount}}</b> de <b>${{cards.length}}</b> projetos`;
}}
</script>

</body>
</html>
"""
    output_path = "output/index-arsenal-open-source.html"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_template)
    print(f"[✓] Portal Web gerado em: {output_path}")

def main():
    console_utf8()
    repos = obter_repos_da_org()
    if not repos:
        print("[!] Nenhum repositório retornado da organização.")
        return
    
    meta_mapa = carregar_metadados_listas()
    gerar_portal_html(repos, meta_mapa)

if __name__ == "__main__":
    main()
