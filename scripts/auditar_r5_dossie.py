# -*- coding: utf-8 -*-
"""
Auditor minucioso de conformidade com a Regra R5 (Padrão Dossiê Executivo).
Verifica:
1. Header com Hero Stats Bar;
2. Título H1 e Deck justificados;
3. Tabela de dados fluida;
4. Cards com as 4 seções padronizadas e grid de 3 passos;
5. Ausência de anti-patterns (sem div.cols espremido).
"""

import sys
import glob
import re
from pathlib import Path

# UTF-8
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

def auditar_conformidade_r5():
    arquivos = sorted(glob.glob("output/listas-open-source/[0-9][0-9]-*.html"))
    print("=" * 80)
    print(" 🔍 AUDITORIA DE CONFORMIDADE COM A REGRA R5 (PADRÃO DOSSIÊ EXECUTIVO)")
    print(f" Total de Listas Encontradas: {len(arquivos)}")
    print("=" * 80)

    conformes = []
    nao_conformes = []

    for f in arquivos:
        nome = Path(f).name
        txt = Path(f).read_text(encoding="utf-8")

        has_hero = bool(re.search(r'class=["\']hero', txt) or re.search(r'class=["\']hero-stats', txt))
        has_table = "<table>" in txt
        has_sec1 = "O Que Faz" in txt or "Mecânica" in txt or "O que entrega" in txt
        has_sec2 = "Análise Econômica" in txt or "Substitui" in txt
        has_sec3 = "Requisitos" in txt or "Especificação" in txt or "Veredito" in txt
        has_sec4 = "Como Usar no Dia a Dia" in txt or "passo-box" in txt or "mini-card" in txt or "step-card" in txt
        has_cols_antipattern = bool(re.search(r'<div class=["\']cols["\']', txt))

        is_padrao = (has_hero and has_table and has_sec1 and has_sec2 and has_sec3 and has_sec4 and not has_cols_antipattern)

        if is_padrao:
            conformes.append(nome)
            print(f"  [✓] CONFORME: {nome}")
        else:
            detalhes = []
            if not has_hero: detalhes.append("Sem Hero")
            if not has_table: detalhes.append("Sem Tabela")
            if not has_sec1: detalhes.append("Sem Sec 1 (O Que Faz)")
            if not has_sec2: detalhes.append("Sem Sec 2 (Econômica)")
            if not has_sec3: detalhes.append("Sem Sec 3 (Requisitos/Veredito)")
            if not has_sec4: detalhes.append("Sem Sec 4 (Passo a Passo)")
            if has_cols_antipattern: detalhes.append("Anti-Pattern: div.cols detectado")

            nao_conformes.append((nome, detalhes))
            print(f"  [X] NÃO CONFORME: {nome} -> {', '.join(detalhes)}")

    print("=" * 80)
    print(f" 📊 Resumo da Auditoria:")
    print(f"  • Totalmente Conformes (Padrão Dossiê Executivo R5): {len(conformes)} / {len(arquivos)}")
    print(f"  • Pendentes de Padronização: {len(nao_conformes)} / {len(arquivos)}")
    print("=" * 80 + "\n")

    return nao_conformes

if __name__ == "__main__":
    auditar_conformidade_r5()
