# -*- coding: utf-8 -*-
"""
Aplica o Padrão Diamante Impeccable em 100% das 49 listas open source:
1. Adiciona micro-interações CSS avançadas (elevação suave, hover highlights).
2. Adiciona Barra de Busca Instantânea em tempo real na seção #fichas.
3. Garante alinhamento justificado e tipografia editorial de alta legibilidade.
4. Sincroniza simultaneamente em output/listas-open-source/ e docs/listas/.
"""
import os
import re
import sys
import glob
from bs4 import BeautifulSoup

def console_utf8():
    if sys.platform == "win32":
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")

console_utf8()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = os.path.join(BASE_DIR, "output", "listas-open-source")
DOCS_DIR = os.path.join(BASE_DIR, "docs", "listas")

SEARCH_BAR_HTML = """
<div class="fichas-search-bar" style="margin: 20px 0 28px; background: var(--surface); border: 1px solid var(--rule); border-radius: 4px; padding: 14px 18px; display: flex; gap: 12px; align-items: center; box-shadow: var(--shadow);">
  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="color:var(--muted); flex-shrink:0;"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
  <input type="text" id="filtroFichasInput" placeholder="Filtrar fichas técnicas desta camada (digite o nome da ferramenta, SaaS substituído ou comando)..." onkeyup="filtrarFichasLocais()" style="flex:1; background:var(--paper); border:1px solid var(--rule); border-radius:3px; padding:10px 14px; font-size:14px; font-family:var(--sans); color:var(--ink); outline:none;">
  <span id="contadorFichas" style="font-family:var(--mono); font-size:12px; color:var(--muted); white-space:nowrap;">Exibindo todas as fichas</span>
</div>
"""

SEARCH_SCRIPT_JS = """
<script>
function filtrarFichasLocais() {
  const query = document.getElementById('filtroFichasInput').value.toLowerCase().trim();
  const entries = document.querySelectorAll('.entry');
  let count = 0;

  entries.forEach(entry => {
    const text = entry.textContent.toLowerCase();
    if (query === '' || text.includes(query)) {
      entry.style.display = 'grid';
      count++;
    } else {
      entry.style.display = 'none';
    }
  });

  const counter = document.getElementById('contadorFichas');
  if (counter) {
    counter.innerHTML = `Exibindo <b>${count}</b> de <b>${entries.length}</b> fichas`;
  }
}
</script>
"""

ENHANCED_CSS_PATCH = """
  /* PADRÃO DIAMANTE IMPECCABLE */
  h1 { text-align: justify; text-justify: inter-word; }
  .deck { text-align: justify; text-justify: inter-word; max-width: 100%; }
  .entry { transition: transform .15s ease, border-color .15s ease, box-shadow .15s ease; }
  .entry:hover { border-color: var(--accent); transform: translateY(-2px); box-shadow: 0 6px 18px rgba(0,0,0,.08); }
  .step-card { transition: transform .12s ease, border-color .12s ease; }
  .step-card:hover { border-color: var(--accent); transform: translateY(-1px); }
  .code-box { position: relative; }
  .copy-btn { transition: all .15s ease; cursor: pointer; }
  .copy-btn:hover { background: var(--accent); color: var(--paper); border-color: var(--accent); }
  table tr { transition: background .12s ease; }
  table tbody tr:hover { background: var(--surface-2); }
"""

def aprimorar_lista(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    soup = BeautifulSoup(content, "html.parser")

    # Injetar CSS Diamond se nao estiver presente
    style = soup.find("style")
    if style and "/* PADRÃO DIAMANTE IMPECCABLE */" not in style.text:
        style.append(BeautifulSoup(ENHANCED_CSS_PATCH, "html.parser"))

    # Injetar Barra de busca antes da div.ledger se nao existir
    fichas_div = soup.find(id="fichas")
    if fichas_div:
        if not fichas_div.find(id="filtroFichasInput"):
            ledger = fichas_div.find("div", class_="ledger")
            if ledger:
                search_node = BeautifulSoup(SEARCH_BAR_HTML, "html.parser")
                ledger.insert_before(search_node)

    # Injetar JS de busca no final do body se nao existir
    body = soup.find("body")
    if body and "filtrarFichasLocais" not in str(body):
        body.append(BeautifulSoup(SEARCH_SCRIPT_JS, "html.parser"))

    res = str(soup)
    return res

def processar_todas():
    arquivos = sorted(glob.glob(os.path.join(OUTPUT_DIR, "[0-9][0-9]-*.html")))
    print(f"[*] Aplicando Padrão Diamante Impeccable em {len(arquivos)} listas...")

    for arq in arquivos:
        nome = os.path.basename(arq)
        novo_html = aprimorar_lista(arq)
        
        with open(arq, "w", encoding="utf-8") as f:
            f.write(novo_html)

        # Sincronizar com docs/listas/
        dest_doc = os.path.join(DOCS_DIR, nome)
        with open(dest_doc, "w", encoding="utf-8") as f:
            f.write(novo_html)

        print(f"  [💎] Lista Diamante: {nome}")

    print("[🎉] 100% das listas atualizadas com o Padrão Diamante Impeccable!")

if __name__ == "__main__":
    processar_todas()
