# -*- coding: utf-8 -*-
"""
Audita a presença da seção 'Como Usar no Dia a Dia' em todas as listas.
"""
import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = os.path.join(BASE_DIR, "output", "listas-open-source")

def auditar():
    arquivos = [f for f in os.listdir(OUTPUT_DIR) if f.endswith(".html") and f != "index.html"]
    print(f"[*] Auditando {len(arquivos)} arquivos HTML...\n")

    for arq in sorted(arquivos):
        path = os.path.join(OUTPUT_DIR, arq)
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        entries = len(re.findall(r'<div class="entry">', content))
        how_to_use = len(re.findall(r'Como Usar no Dia a Dia|class="how-to-use"', content, re.IGNORECASE))
        print(f"{arq:50s} -> Entries: {entries:2d} | How-To-Use: {how_to_use:2d}")

if __name__ == "__main__":
    auditar()
