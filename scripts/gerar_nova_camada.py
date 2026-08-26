# -*- coding: utf-8 -*-
"""
CLI OFICIAL DE CRIAÇÃO DETERMINÍSTICA DE CAMADAS (PADRÃO DIAMANTE R5)
Uso:
  python scripts/gerar_nova_camada.py --numero 52 --arquivo dados_52.json
  python scripts/gerar_nova_camada.py --auto-curar
"""
import os
import sys
import json
import argparse
from pathlib import Path
from normalizar_compendio import normalizar_arquivo

def console_utf8():
    if sys.platform == "win32":
        try:
            sys.stdout.reconfigure(encoding="utf-8")
            sys.stderr.reconfigure(encoding="utf-8")
        except Exception:
            pass

console_utf8()

BASE_DIR = Path(__file__).resolve().parent.parent
DOCS_DIR = BASE_DIR / "docs" / "listas"
OUTPUT_DIR = BASE_DIR / "output" / "listas-open-source"

def main():
    parser = argparse.ArgumentParser(description="Gerador Determinístico de Camadas Diamante R5")
    parser.add_argument("--arquivo", help="Caminho do arquivo JSON ou HTML de entrada")
    parser.add_argument("--auto-curar", action="store_true", help="Auto-cura todas as listas em docs/ e output/")
    
    args = parser.parse_args()

    if args.auto_curar:
        print("[*] Iniciando Auto-Cura de todos os compêndios...")
        os.system("python scripts/limpar_entulho.py")
        sys.exit(0)

    if args.arquivo:
        sucesso = normalizar_arquivo(args.arquivo)
        if sucesso:
            os.system("python scripts/limpar_entulho.py")
        sys.exit(0 if sucesso else 1)

    print("Uso:")
    print("  python scripts/gerar_nova_camada.py --arquivo <dados.json ou arquivo.html>")
    print("  python scripts/gerar_nova_camada.py --auto-curar")

if __name__ == "__main__":
    main()
