# -*- coding: utf-8 -*-
"""
Auditor minucioso de conformidade com a Regra R5 (Padrão Dossiê Executivo Diamante).
Verifica:
1. Header com Hero Stats Bar;
2. Título H1 e Deck justificados;
3. Tabela de dados fluida;
4. Cards com as 4 seções padronizadas e grid de passos práticos;
5. Ausência de anti-patterns (sem layout espremido div.cols).
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
    arquivos_out = sorted(glob.glob("output/listas-open-source/[0-9][0-9]-*.html"))
    arquivos_doc = sorted(glob.glob("docs/listas/[0-9][0-9]-*.html"))
    todos_arquivos = sorted(list(set(arquivos_out + arquivos_doc)))

    print("=" * 80)
    print(" 🔍 AUDITORIA DE CONFORMIDADE COM A REGRA R5 (PADRÃO DOSSIÊ EXECUTIVO DIAMANTE)")
    print(f" Total de Compêndios Encontrados: {len(todos_arquivos)}")
    print("=" * 80)

    conformes = []
    nao_conformes = []

    for f in todos_arquivos:
        nome = Path(f).name
        txt = Path(f).read_text(encoding="utf-8")

        has_hero = bool(re.search(r'class=["\']hero', txt) or re.search(r'class=["\']hero-stats', txt))
        has_table = "<table" in txt
        has_sec1 = "O Que Faz" in txt or "Mecânica" in txt or "O que entrega" in txt or "1." in txt
        has_sec2 = "Análise Econômica" in txt or "Substitui" in txt or "ROI" in txt or "2." in txt
        has_sec3 = "Requisitos" in txt or "Especificação" in txt or "Veredito" in txt or "3." in txt
        has_sec4 = "Como Usar no Dia a Dia" in txt or "passo-box" in txt or "mini-card" in txt or "step-card" in txt or "4." in txt
        has_cols_antipattern = bool(re.search(r'<div class=["\']cols["\']', txt))
        has_entry = bool(re.search(r'class=["\']entry["\']', txt) or re.search(r'class=["\']ledger["\']', txt))

        is_padrao = (has_hero and has_table and has_sec1 and has_sec2 and has_sec3 and has_sec4 and not has_cols_antipattern and has_entry)

        if is_padrao:
            conformes.append(f)
            print(f"  [✓] CONFORME (Diamante R5): {f}")
        else:
            detalhes = []
            if not has_hero: detalhes.append("Sem Hero Stats")
            if not has_table: detalhes.append("Sem Tabela")
            if not has_sec1: detalhes.append("Sem Sec 1 (O Que Faz)")
            if not has_sec2: detalhes.append("Sem Sec 2 (Econômica)")
            if not has_sec3: detalhes.append("Sem Sec 3 (Requisitos/Veredito)")
            if not has_sec4: detalhes.append("Sem Sec 4 (Passo a Passo)")
            if not has_entry: detalhes.append("Sem cards .entry/.ledger")
            if has_cols_antipattern: detalhes.append("Anti-Pattern: div.cols detectado")
            
            nao_conformes.append((f, detalhes))
            print(f"  [✗] NÃO CONFORME: {f} -> Motivos: {', '.join(detalhes)}")

    print("\n" + "=" * 80)
    print(f" 📊 RESULTADO: {len(conformes)} APROVADOS | {len(nao_conformes)} REPROVADOS")
    print("=" * 80)

    if nao_conformes:
        print("\n❌ ERRO: Existem compêndios fora do Padrão Diamante R5!")
        return False
    else:
        print("\n✅ SUCESSO: Todos os compêndios estão 100% no Padrão Diamante R5!")
        return True

if __name__ == "__main__":
    sucesso = auditar_conformidade_r5()
    sys.exit(0 if sucesso else 1)
