# -*- coding: utf-8 -*-
"""
AUTOFALANTE DE HIGIENE R18: LIMPEZA, SANEAMENTO E RESSINCRONIZAÇÃO TOTAL
1. Remove pastas e arquivos temporários (temp_*, *.bak, *.tmp).
2. Sincroniza 100% dos arquivos de output/listas-open-source/ para docs/listas/.
3. Remove arquivos órfãos em docs/listas/ que não existam em output/listas-open-source/.
4. Valida a higiene ao final rodando o Gate R18.
"""
import os
import sys
import shutil
import glob
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

def limpar_pastas_e_arquivos_temporarios():
    print("[*] Limpando pastas e arquivos temporários...")
    # Limpar no diretório raiz e em scripts
    for raiz in [BASE_DIR, SCRIPTS_DIR]:
        for item in os.listdir(raiz):
            caminho = os.path.join(raiz, item)
            if item.startswith("temp_") and os.path.isdir(caminho):
                shutil.rmtree(caminho, ignore_errors=True)
                print(f"  -> Removida pasta temporária: {item}")
            elif item.endswith(".bak") or item.endswith(".tmp") or (item.startswith("repomix-") and item.endswith(".xml")):
                try:
                    os.remove(caminho)
                    print(f"  -> Removido arquivo temporário: {item}")
                except Exception:
                    pass

def ressincronizar_espelhos():
    print("[*] Ressincronizando espelhos (output/listas-open-source -> docs/listas)...")
    os.makedirs(DOCS_DIR, exist_ok=True)
    
    out_files = os.listdir(OUTPUT_DIR)
    for f in out_files:
        src = os.path.join(OUTPUT_DIR, f)
        dst = os.path.join(DOCS_DIR, f)
        if os.path.isfile(src):
            shutil.copy2(src, dst)
            
    # Remover do docs o que nao existe em output
    doc_files = os.listdir(DOCS_DIR)
    for f in doc_files:
        if f not in out_files:
            dst = os.path.join(DOCS_DIR, f)
            if os.path.isfile(dst):
                os.remove(dst)
                print(f"  -> Removido arquivo órfão em docs/: {f}")

    print(f"  -> [OK] {len(out_files)} arquivos perfeitamente espelhados e sincronizados.")

def main():
    limpar_pastas_e_arquivos_temporarios()
    ressincronizar_espelhos()
    print("\n[*] Rodando verificação do Gate R18...")
    from auditar_higiene_repo import executar_auditoria_completa
    codigo = executar_auditoria_completa()
    sys.exit(codigo)

if __name__ == "__main__":
    main()
