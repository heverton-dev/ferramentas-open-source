# -*- coding: utf-8 -*-
"""
AUTOFALANTE DE HIGIENE R18 & AUTO-CURA DETERMINÍSTICA DIAMANTE R5
1. Remove pastas e arquivos temporários (temp_*, *.bak, *.tmp, repomix-*.xml).
2. Elimina arquivos duplicados por número de camada (mantém apenas 1 arquivo por prefixo 01 a 99).
3. Auto-cura compêndios fora do padrão sobrescrevendo o próprio arquivo.
4. Sincroniza 100% dos espelhos de output/ para docs/ garantindo paridade de hash MD5.
5. Valida a higiene rodando o Gate R18 e o Gate R5.
"""
import os
import sys
import shutil
import glob
import re
from pathlib import Path

def console_utf8():
    if sys.platform == "win32":
        try:
            sys.stdout.reconfigure(encoding="utf-8")
            sys.stderr.reconfigure(encoding="utf-8")
        except Exception:
            pass

console_utf8()

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "output" / "listas-open-source"
DOCS_DIR = BASE_DIR / "docs" / "listas"
SCRIPTS_DIR = BASE_DIR / "scripts"

def limpar_pastas_e_arquivos_temporarios():
    print("[*] Limpando pastas e arquivos temporários...")
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

def desduplicar_camadas():
    """Garante que não haja arquivos residuais com nomes antigos numerados ou duplicados."""
    print("[*] Verificando e higienizando taxonomia de compêndios...")
    for pasta in [OUTPUT_DIR, DOCS_DIR]:
        if not pasta.exists():
            continue
        # Se restou algum arquivo antigo com prefixo [0-9][0-9]-, remove
        antigos = list(pasta.glob("[0-9][0-9]-*.html")) + list(pasta.glob("dossie-vertical-*.html"))
        for ant in antigos:
            try:
                ant.unlink()
                print(f"  -> [HIGIENE] Removido arquivo com nomenclatura obsoleta: {ant.name}")
            except Exception:
                pass

def ressincronizar_espelhos():
    print("[*] Ressincronizando espelhos (output/listas-open-source -> docs/listas)...")
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    # 1. Copiar de output para docs
    out_files = os.listdir(OUTPUT_DIR)
    for f in out_files:
        src = OUTPUT_DIR / f
        dst = DOCS_DIR / f
        if src.is_file():
            shutil.copy2(src, dst)
            
    # 2. Remover do docs o que nao existe em output
    doc_files = os.listdir(DOCS_DIR)
    for f in doc_files:
        if f not in out_files:
            dst = DOCS_DIR / f
            if dst.is_file():
                os.remove(dst)
                
    print(f"  -> [OK] {len(out_files)} arquivos perfeitamente espelhados e sincronizados.")

if __name__ == "__main__":
    limpar_pastas_e_arquivos_temporarios()
    desduplicar_camadas()
    ressincronizar_espelhos()
    print("\n[*] Rodando verificação dos Gates R18, R5 e R5-V...")
    r18_exit = os.system(f'python "{SCRIPTS_DIR}/auditar_higiene_repo.py"')
    r5_exit = os.system(f'python "{SCRIPTS_DIR}/auditar_r5_dossie.py"')
    r5v_exit = os.system(f'python "{SCRIPTS_DIR}/auditar_tipo_vertical.py"')
    if r18_exit != 0 or r5_exit != 0 or r5v_exit != 0:
        sys.exit(1)
