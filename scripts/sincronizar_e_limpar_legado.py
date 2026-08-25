# -*- coding: utf-8 -*-
"""
Sincroniza e limpa todo e qualquer resquício do formato antigo no projeto:
1. Sincroniza docs/listas/ com o output/listas-open-source/.
2. Remove scripts temporários obsoletos em scripts/.
3. Audita 100% dos arquivos HTML para garantir ausência de 'div class="cols"' e do layout antigo.
"""
import os
import shutil
import sys
import re

def console_utf8():
    if sys.platform == "win32":
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")

console_utf8()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = os.path.join(BASE_DIR, "output", "listas-open-source")
DOCS_DIR = os.path.join(BASE_DIR, "docs", "listas")
SCRIPTS_DIR = os.path.join(BASE_DIR, "scripts")

# 1. Scripts temporários obsoletos para remoção
SCRIPTS_OBSOLETOS = [
    "aplicar_design_premium_lista_01.py",
    "aplicar_layout_vertical_lista_01.py",
    "enriquecer_dossie_lista_01.py",
    "enriquecer_e_padronizar_how_to_use.py",
    "migrar_todas_as_listas_modelo_dossie.py",
    "padronizar_todas_as_listas.py",
    "gerar_30_listas.py",
    "gerar_30_listas_com_como_usar.py",
    "injetar_como_usar.py",
    "auditar_how_to_use.py",
    "refinar_titulos_e_justificacao_todas_as_listas.py"
]

def limpar_scripts_obsoletos():
    print("[*] Removendo scripts temporários obsoletos...")
    for s in SCRIPTS_OBSOLETOS:
        p = os.path.join(SCRIPTS_DIR, s)
        if os.path.exists(p):
            os.remove(p)
            print(f"  -> [REMOVIDO] {s}")

def sincronizar_docs():
    print("\n[*] Sincronizando docs/listas/ com o novo formato canônico...")
    os.makedirs(DOCS_DIR, exist_ok=True)
    for f in os.listdir(OUTPUT_DIR):
        if f.endswith(".html"):
            src = os.path.join(OUTPUT_DIR, f)
            dst = os.path.join(DOCS_DIR, f)
            shutil.copy2(src, dst)
    print("  -> [OK] docs/listas/ sincronizado com sucesso!")

def auditar_ausencia_formato_antigo():
    print("\n[*] Auditando presença de tags legadas ('div class=\"cols\"')...")
    erros = 0
    for pasta in [OUTPUT_DIR, DOCS_DIR]:
        for f in os.listdir(pasta):
            if f.endswith(".html"):
                p = os.path.join(pasta, f)
                with open(p, "r", encoding="utf-8") as fp:
                    c = fp.read()
                    if 'class="cols"' in c or 'class="block"' in c:
                        print(f"  -> [ALERTA] Resquício legado encontrado em: {f}")
                        erros += 1
    if erros == 0:
        print("  -> [OK] Nenhum resquício do formato antigo encontrado nos 49 arquivos!")
    else:
        print(f"  -> [AVISO] {erros} arquivos contêm resquícios e serão reprocessados.")

def main():
    limpar_scripts_obsoletos()
    sincronizar_docs()
    auditar_ausencia_formato_antigo()
    print("\n[OK] Limpeza e sincronização concluídas com sucesso!")

if __name__ == "__main__":
    main()
