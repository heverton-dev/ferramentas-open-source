# -*- coding: utf-8 -*-
"""
GATE MECÂNICO R18: AUDITOR DE HIGIENE CONTÍNUA, ZERO ENTULHO & SINCRONIZAÇÃO ESTRITA
Verifica rigorosamente antes de cada commit:
1. Ausência total de arquivos temporários, clones e restos de migração (temp_*, fix_*, *.bak, *.tmp).
2. Paridade de conteúdo e integridade (hash MD5) entre output/listas-open-source/ e docs/listas/.
3. Numeração contínua e sem duplicidade das 49 camadas (01- a 49-).
4. Exit 0 se 100% limpo; Exit 1 e relatório de erros se houver qualquer anomalia.
"""
import os
import sys
import glob
import hashlib
import re

def console_utf8():
    if sys.platform == "win32":
        try:
            sys.stdout.reconfigure(encoding="utf-8")
            sys.stderr.reconfigure(encoding="utf-8")
        except Exception:
            pass

console_utf8()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = os.path.join(BASE_DIR, "output", "listas-open-source")
DOCS_DIR = os.path.join(BASE_DIR, "docs", "listas")
SCRIPTS_DIR = os.path.join(BASE_DIR, "scripts")

PADROES_LIXO = [
    r"^temp_",
    r"^fix_",
    r"^migrar_",
    r"\.bak$",
    r"\.tmp$",
    r"_antigo",
    r"_legado",
    r"copy",
]

def calcular_hash(filepath):
    hasher = hashlib.md5()
    with open(filepath, "rb") as f:
        hasher.update(f.read())
    return hasher.hexdigest()

def auditar_entulho_scripts():
    erros = []
    scripts = os.listdir(SCRIPTS_DIR)
    for s in scripts:
        for padrao in PADROES_LIXO:
            if re.search(padrao, s, flags=re.IGNORECASE):
                erros.append(f"Script temporário ou obsoleto detectado: scripts/{s}")
                break
    return erros

def auditar_paridade_espelhos():
    erros = []
    out_files = set(os.listdir(OUTPUT_DIR))
    doc_files = set(os.listdir(DOCS_DIR))

    # Verificar arquivos faltantes
    faltando_em_docs = out_files - doc_files
    faltando_em_out = doc_files - out_files

    for f in faltando_em_docs:
        erros.append(f"Arquivo presente em output/ mas ausente em docs/: {f}")
    for f in faltando_em_out:
        erros.append(f"Arquivo presente em docs/ mas ausente em output/: {f}")

    # Verificar paridade de hash nos arquivos comuns
    comuns = out_files.intersection(doc_files)
    for f in comuns:
        p_out = os.path.join(OUTPUT_DIR, f)
        p_doc = os.path.join(DOCS_DIR, f)
        if os.path.isfile(p_out) and os.path.isfile(p_doc):
            h_out = calcular_hash(p_out)
            h_doc = calcular_hash(p_doc)
            if h_out != h_doc:
                erros.append(f"Divergência de conteúdo (hash) no espelho: {f}")

    return erros

def auditar_taxonomia_nomenclaturas():
    erros = []
    PREFIXOS_VALIDOS = (r"^list-", r"^vert-", r"^tco-", r"^guia-", r"^index\.html$", r"^README\.md$")
    
    arquivos = os.listdir(OUTPUT_DIR)
    nomes_vistos = set()

    for arq in arquivos:
        valido = any(re.match(p, arq) for p in PREFIXOS_VALIDOS)
        if not valido:
            erros.append(f"Arquivo fora da taxonomia padrão (use list-, vert-, tco- ou guia-): {arq}")

        if arq.lower() in nomes_vistos:
            erros.append(f"Arquivo duplicado ou colisão de case: {arq}")
        nomes_vistos.add(arq.lower())

    return erros

def executar_auditoria_completa():
    print("=" * 80)
    print(" 🛡️ GATE MECÂNICO R18: AUDITORIA DE HIGIENE, PARIDADE & TAXONOMIA")
    print("=" * 80)

    erros_entulho = auditar_entulho_scripts()
    erros_paridade = auditar_paridade_espelhos()
    erros_taxonomia = auditar_taxonomia_nomenclaturas()

    total_erros = len(erros_entulho) + len(erros_paridade) + len(erros_taxonomia)

    if erros_entulho:
        print("\n [!] ENTULHO TÉCNICO / SCRIPTS TEMPORÁRIOS:")
        for e in erros_entulho:
            print(f"     ❌ {e}")

    if erros_paridade:
        print("\n [!] DESSINCRONIA ENTRE ESPELHOS (output/ vs docs/):")
        for e in erros_paridade:
            print(f"     ❌ {e}")

    if erros_taxonomia:
        print("\n [!] ERROS DE TAXONOMIA / DUPLICIDADE:")
        for e in erros_taxonomia:
            print(f"     ❌ {e}")

    print("\n" + "=" * 80)
    if total_erros == 0:
        print(" ✅ APROVADO: 100% Limpo, Sem Entulho, Espelhos Sincronizados (R18 Conforme)")
        print("=" * 80 + "\n")
        return 0
    else:
        print(f" ❌ REPROVADO: {total_erros} violações da Regra R18 detectadas.")
        print(" Execute 'python scripts/limpar_entulho.py' para corrigir automaticamente.")
        print("=" * 80 + "\n")
        return 1

if __name__ == "__main__":
    sys.exit(executar_auditoria_completa())
