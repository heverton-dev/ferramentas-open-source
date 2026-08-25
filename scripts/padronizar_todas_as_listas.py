# -*- coding: utf-8 -*-
"""
Padroniza o CSS de TODOS os arquivos HTML das listas:
1. Título em cima (.entry-top h3 { width: 100%; margin: 0 0 4px 0; })
2. Badges embaixo (.entry-top)
3. Padding-top aumentado e divisória sutil no corpo (.cols { ... padding-top: 14px; border-top: 1px dashed var(--rule-soft); })
4. Scrollbar 4px padronizada
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

SCROLLBAR_CSS = """  * { scrollbar-width: thin; scrollbar-color: var(--accent) transparent; box-sizing: border-box; }
  ::-webkit-scrollbar { width: 4px; height: 4px; }
  ::-webkit-scrollbar-track { background: transparent; }
  ::-webkit-scrollbar-thumb { background: var(--accent); border-radius: 4px; }"""

def padronizar_html(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Garantir scrollbar 4px se nao tiver
    if "::-webkit-scrollbar" not in content:
        content = re.sub(r'<style>\s*', f'<style>\n{SCROLLBAR_CSS}\n\n', content, count=1)

    # 2. Padronizar .entry-top e .entry-top h3
    if ".entry-top h3" not in content:
        # Se existe .entry-top, adiciona a regra logo apos
        content = re.sub(
            r'(\.entry-top\s*\{[^}]*\})',
            r'\1\n  .entry-top h3 { width:100%; margin:0 0 4px 0; }',
            content
        )

    # 3. Padronizar .cols com padding-top e divisória
    if "padding-top:14px" not in content and ".cols" in content:
        content = re.sub(
            r'(\.cols\s*\{[^}]*display:\s*grid[^}]*?)(\})',
            r'\1 padding-top:14px; border-top:1px dashed var(--rule-soft);\2',
            content
        )
    elif "padding-top: 14px" not in content and ".cols" in content:
        content = re.sub(
            r'(\.cols\s*\{[^}]*display:\s*grid[^}]*?)(\})',
            r'\1 padding-top:14px; border-top:1px dashed var(--rule-soft);\2',
            content
        )

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    
    return True

def main():
    arquivos = [f for f in os.listdir(OUTPUT_DIR) if f.endswith(".html") and f != "index.html"]
    print(f"[*] Processando {len(arquivos)} arquivos HTML em {OUTPUT_DIR}...")
    
    total = 0
    for arq in sorted(arquivos):
        p = os.path.join(OUTPUT_DIR, arq)
        padronizar_html(p)
        total += 1
        print(f"  -> [✓] Padronizado: {arq}")

    print(f"\n[🎉] Concluído! Todos os {total} arquivos HTML foram padronizados com sucesso.")

if __name__ == "__main__":
    main()
