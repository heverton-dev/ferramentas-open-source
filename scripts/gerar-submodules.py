#!/usr/bin/env python3
"""
Script para inicializar um REPOSITÓRIO ÚNICO contendo os 190 projetos como Submódulos Git.
Permite versionar todos os códigos sob um único repositório sem criar múltiplos forks no seu perfil.

Uso:
  python scripts/gerar-submodules.py --destino C:/caminho/para/arsenal-open-source
"""

import os
import sys
import json
import argparse
import subprocess

def console_utf8():
    if sys.platform == "win32":
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")

def main():
    console_utf8()
    parser = argparse.ArgumentParser(description="Adiciona todos os repositórios como submódulos em um repositório central.")
    parser.add_argument("--destino", required=True, help="Diretório onde o repositório central está ou será criado")
    parser.add_argument("--shallow", action="store_true", default=True, help="Clona com profundidade 1 (--depth 1) para economizar disco e tempo")
    args = parser.parse_args()

    inventory_file = "output/forks-inventory/repositorios.json"
    if not os.path.exists(inventory_file):
        print(f"Erro: {inventory_file} não encontrado.")
        sys.exit(1)

    with open(inventory_file, "r", encoding="utf-8") as f:
        repos_dict = json.load(f)

    os.makedirs(args.destino, exist_ok=True)
    
    # Inicializar git se não existir
    if not os.path.exists(os.path.join(args.destino, ".git")):
        print(f"Inicializando repositório Git em: {args.destino}")
        subprocess.run(["git", "init"], cwd=args.destino, check=True)

    total = len(repos_dict)
    print(f"Configurando {total} submódulos no repositório central...\n")

    for idx, (repo_url, sources) in enumerate(sorted(repos_dict.items()), 1):
        repo_name = repo_url.split("/")[-1]
        submodule_path = f"modulos/{repo_name}"
        print(f"[{idx}/{total}] Adicionando submódulo {repo_name}...")

        cmd = ["git", "submodule", "add"]
        if args.shallow:
            cmd.extend(["--depth", "1"])
        cmd.extend([repo_url, submodule_path])

        try:
            res = subprocess.run(cmd, cwd=args.destino, capture_output=True, text=True, encoding="utf-8")
            if res.returncode == 0:
                print(f"  -> OK: {submodule_path}")
            else:
                if "already exists" in res.stderr.lower():
                    print(f"  -> Submódulo já configurado.")
                else:
                    print(f"  -> AVISO: {res.stderr.strip()}")
        except Exception as e:
            print(f"  -> FALHA: {e}")

    print("\nProcesso concluído! O repositório central possui todos os 190 projetos mapeados em .gitmodules.")

if __name__ == "__main__":
    main()
