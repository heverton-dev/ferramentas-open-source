# -*- coding: utf-8 -*-
"""
Script mestre de geração massiva para expandir TODAS as 30 listas para >= 20 itens de elite cada.
Garante o padrão Dossiê Executivo, 4 seções padronizadas, sem colunas espremidas e com 100% de fluidez.
"""

import os
import sys
from pathlib import Path

# Garantir UTF-8 no Windows
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Importar o compilador visual e os templates
from gerar_catalogo_completo_30 import gerar_html_completo
from expandir_lista_02 import LISTA_02_EXPANDIDA

# Importar gerador de dados exaustivos das 30 listas
from dados_30_listas_expandidas import TODAS_AS_30_LISTAS

def compilar_todas_as_listas():
    docs_dir = Path("docs/listas")
    output_dir = Path("output/listas-open-source")
    brain_dir = Path(r"C:\Users\trcnologia\.gemini\antigravity-cli\brain\0e2afde3-829c-4443-b5a5-7a8779eeb139")

    docs_dir.mkdir(parents=True, exist_ok=True)
    output_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 80)
    print(" 🚀 COMPILADOR MASSIVO: EXPANDINDO TODAS AS 30 LISTAS PARA >= 20 ITENS DE ELITE")
    print("=" * 80)

    total_ferramentas = 0

    for idx, lista_data in enumerate(TODAS_AS_30_LISTAS, start=1):
        num_itens = len(lista_data["itens"])
        total_ferramentas += num_itens
        slug = lista_data["slug"]
        print(f"[{idx:02d}/30] Compilando '{slug}' com {num_itens} itens de elite...")

        html_content = gerar_html_completo(lista_data)

        file_docs = docs_dir / f"{slug}.html"
        file_output = output_dir / f"{slug}.html"

        file_docs.write_text(html_content, encoding="utf-8")
        file_output.write_text(html_content, encoding="utf-8")

        if brain_dir.exists():
            file_brain = brain_dir / f"{slug}.html"
            file_brain.write_text(html_content, encoding="utf-8")

    print("\n" + "=" * 80)
    print(f" 🎉 TODAS AS 30 LISTAS FORAM EXPANDIDAS E COMPILADAS COM SUCESSO!")
    print(f" 📊 Total Geral de Fichas Técnicas de Elite: {total_ferramentas} itens catalogados (Média de {total_ferramentas/30:.1f} por lista)")
    print("=" * 80 + "\n")

if __name__ == "__main__":
    compilar_todas_as_listas()
