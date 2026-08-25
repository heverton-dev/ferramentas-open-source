# -*- coding: utf-8 -*-
"""
Script determinístico para numerar as 10 listas restantes (de 40 a 49),
garantindo que 100% dos compêndios do catálogo tenham prefixo numérico padronizado.
"""

import os
import sys
import shutil
from pathlib import Path

# Garantir UTF-8
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

MAPEAMENTO_NUMERACAO = [
    ("alcance-proprio.html", "40-alcance-proprio.html"),
    ("arsenal-do-engenheiro-ia.html", "41-arsenal-do-engenheiro-ia.html"),
    ("caixa-aberto.html", "42-caixa-aberto.html"),
    ("chao-de-fabrica.html", "43-chao-de-fabrica.html"),
    ("codigo-autonomo.html", "44-codigo-autonomo.html"),
    ("fonte-limpa.html", "45-fonte-limpa.html"),
    ("linha-direta.html", "46-linha-direta.html"),
    ("peso-e-watt.html", "47-peso-e-watt.html"),
    ("titas-da-soberania.html", "48-titas-da-soberania.html"),
    ("troca-livre.html", "49-troca-livre.html")
]

def renomear_e_atualizar_listas():
    diretorios = [Path("output/listas-open-source"), Path("docs/listas")]

    print("=" * 76)
    print(" 🔢 PADRONIZANDO NUMERAÇÃO DAS LISTAS RESTANTES (40 A 49)")
    print("=" * 76)

    for d in diretorios:
        if not d.exists():
            continue
        print(f"\n[*] Processando diretório: {d}")
        for antigo, novo in MAPEAMENTO_NUMERACAO:
            arq_antigo = d / antigo
            arq_novo = d / novo
            if arq_antigo.exists():
                shutil.move(str(arq_antigo), str(arq_novo))
                print(f"  [✓] {antigo} -> {novo}")
            elif arq_novo.exists():
                print(f"  [i] {novo} já existe.")

    # Atualizar links nos índices e arquivos HTML
    print("\n[*] Atualizando referências de links internos...")
    for d in diretorios:
        for html_file in d.glob("*.html"):
            conteudo = html_file.read_text(encoding="utf-8")
            modificado = False
            for antigo, novo in MAPEAMENTO_NUMERACAO:
                if antigo in conteudo:
                    conteudo = conteudo.replace(antigo, novo)
                    modificado = True
            if modificado:
                html_file.write_text(conteudo, encoding="utf-8")
                print(f"  [✓] Links atualizados em: {html_file.name}")

    print("\n" + "=" * 76)
    print(" 🎉 100% DAS LISTAS AGORA POSSUEM NUMERAÇÃO PADRONIZADA (01 A 49)!")
    print("=" * 76 + "\n")

if __name__ == "__main__":
    renomear_e_atualizar_listas()
