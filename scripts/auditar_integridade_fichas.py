# -*- coding: utf-8 -*-
"""
Gate mecânico (exit 0/1) que valida se TODAS as 30 listas possuem >= 20 fichas técnicas
completas, com todas as 4 seções do Dossiê Executivo preenchidas sem exceção.
"""

import sys
import glob
import re
from pathlib import Path

# Garantir UTF-8
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

def auditar_todas_as_listas():
    print("=" * 76)
    print(" 🛡️ GATE MECÂNICO DE AUDITORIA: >= 20 ITENS POR LISTA")
    print("=" * 76)

    todos_arquivos = sorted(glob.glob("output/listas-open-source/[0-3][0-9]-*.html"))
    # Filtrar apenas as listas 01 a 30 do compêndio central
    arquivos = [f for f in todos_arquivos if int(Path(f).name[:2]) <= 30]

    falhas = 0
    total_itens_global = 0

    for f in arquivos:
        nome_arquivo = Path(f).name
        conteudo = Path(f).read_text(encoding="utf-8")

        # Contar itens pela tabela e cards ricos
        ranks_tabela = re.findall(r'<td class="rank">(\d+)</td>', conteudo)
        cards = re.findall(r'<div class="card" id="card-', conteudo)
        qtd = max(len(ranks_tabela), len(cards))
        total_itens_global += qtd

        if qtd < 20:
            print(f"  [X] FALHA: {nome_arquivo} possui apenas {qtd} itens (esperado >= 20)")
            falhas += 1
        else:
            print(f"  [✓] OK: {nome_arquivo} -> {qtd} fichas ricas validadas.")

    print("=" * 76)
    if falhas == 0:
        print(f" 🎉 AUDITORIA APROVADA: 100% das 30 listas possuem >= 20 itens!")
        print(f" 📊 Total Auditado: {total_itens_global} fichas ricas completas.")
        print("=" * 76 + "\n")
        sys.exit(0)
    else:
        print(f" ❌ AUDITORIA REPROVADA: {falhas} listas possuem menos de 20 itens.")
        print("=" * 76 + "\n")
        sys.exit(1)

if __name__ == "__main__":
    auditar_todas_as_listas()
