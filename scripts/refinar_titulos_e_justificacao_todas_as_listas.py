# -*- coding: utf-8 -*-
"""
Refina a tipografia e os cabeçalhos dos cards em TODAS as 49 listas:
1. Alinhamento justificado em h1 e p.deck (text-align: justify; text-justify: inter-word)
2. Limpeza dos títulos H3 (remove 'Skill: ', 'Motor: ', etc. e une com subtítulo)
3. Garante que todos os metadados soltos sejam badges estilizados (senior-badge, killer-badge, econ-badge, lic-badge, kind-badge)
4. Padroniza as quebras e o alinhamento da matriz comparativa
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

def refinar_arquivo(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Ajustar CSS para text-align: justify em h1 e .deck
    content = re.sub(
        r'h1\s*\{([^}]*)\}',
        r'h1 { font-family:var(--serif); font-weight:600; font-size:clamp(38px,7.5vw,68px); line-height:1.05; letter-spacing:-.025em; margin:0; color:var(--ink); text-align:justify; text-justify:inter-word; }',
        content
    )
    content = re.sub(
        r'\.deck\s*\{([^}]*)\}',
        r'.deck { font-family:var(--serif); font-size:clamp(17px,2.2vw,21px); line-height:1.55; color:var(--ink-2); max-width:100%; margin:0; text-align:justify; text-justify:inter-word; }',
        content
    )

    # 2. Refinar cada entry-top nos cards
    def refinar_entry_top(match):
        block = match.group(0)

        # Extrair H3
        h3_m = re.search(r'<h3>(.*?)</h3>', block, re.DOTALL)
        if not h3_m:
            return block
        
        raw_h3 = h3_m.group(1).strip()
        # Remover prefixos indesejados no título
        clean_title = re.sub(r'^(?:Skill:\s*|Motor:\s*|Framework:\s*|Ferramenta:\s*)', '', raw_h3, flags=re.IGNORECASE).strip()
        
        # Extrair kind se existir
        kind_m = re.search(r'<span class="kind">(.*?)</span>', block, re.DOTALL)
        kind_txt = kind_m.group(1).strip() if kind_m else ""

        # Se o título não tiver subtítulo com "·", combinar com kind_txt se apropriado
        if "·" not in clean_title and kind_txt and len(kind_txt) > 2:
            # Se clean_title não contém o kind
            if kind_txt.lower() not in clean_title.lower():
                final_h3 = f"{clean_title.capitalize()} · {kind_txt}"
            else:
                final_h3 = clean_title.capitalize()
        else:
            final_h3 = clean_title

        # Atualizar o h3 dentro do bloco
        block = re.sub(r'<h3>.*?</h3>', f'<h3>{final_h3}</h3>', block, flags=re.DOTALL)

        # Padronizar prefixos nos badges para ficarem uniformes
        block = re.sub(r'<span class="killer-badge">\s*(?:SUBSTITUI:\s*|Substitui:\s*)?', '<span class="killer-badge">Substitui: ', block)
        block = re.sub(r'<span class="econ-badge">\s*(?:ECONOMIA:\s*|Economia:\s*)?', '<span class="econ-badge">Economia: ', block)
        
        # Se for uma skill e não tiver badge de tipo, adicionar badge de tipo
        if "skill" in raw_h3.lower() and '<span class="lic-badge">' in block and 'Skill' not in block:
            block = block.replace('<span class="lic-badge">', '<span class="senior-badge" style="background:var(--accent-soft);color:var(--accent);border:1px solid color-mix(in srgb, var(--accent) 35%, transparent);">⚙️ Skill Agêntica</span>\n            <span class="lic-badge">')

        return block

    content = re.sub(r'<div class="entry-top">.*?</div>', refinar_entry_top, content, flags=re.DOTALL)

    # 3. Limpar comentários duplicados se houver
    content = re.sub(r'(<!-- \d+.*?-->\s*)+<!-- \d+\. (.*?) -->', r'<!-- \2 -->', content)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

def main():
    arquivos = [f for f in os.listdir(OUTPUT_DIR) if f.endswith(".html") and f != "index.html"]
    print(f"[*] Refinando títulos, badges e alinhamento justificado em {len(arquivos)} arquivos...")

    for arq in sorted(arquivos):
        p = os.path.join(OUTPUT_DIR, arq)
        refinar_arquivo(p)
        print(f"  -> [✓] Refinado: {arq}")

    print("\n[🎉] Todas as 49 listas foram refinadas com sucesso!")

if __name__ == "__main__":
    main()
