#!/usr/bin/env python3
"""
Script de automação para Fork em lote dos 190 repositórios para uma ORGANIZAÇÃO DEDICADA do GitHub.
Evita poluir sua conta pessoal ou o repositório original.

Requisitos:
- GitHub CLI instalado (`gh`) e autenticado (`gh auth login`)
- Uma Organização criada no GitHub (ex: `sua-org-forks`)

Uso:
  python scripts/fork-para-organizacao.py --org NOME_DA_SUA_ORGANIZACAO
"""

import os
import sys
import json
import argparse
import subprocess
import time

def console_utf8():
    if sys.platform == "win32":
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")

def main():
    console_utf8()
    parser = argparse.ArgumentParser(description="Realiza fork em lote para uma organização GitHub dedicada.")
    parser.add_argument("--org", required=True, help="Nome da organização GitHub de destino (ex: minha-org-forks)")
    parser.add_argument("--dry-run", action="store_true", help="Apenas simula os comandos sem executar")
    parser.add_argument("--delay", type=float, default=1.5, help="Tempo de espera em segundos entre cada fork (evita rate-limit)")
    args = parser.parse_args()

    inventory_file = "output/forks-inventory/repositorios.json"
    if not os.path.exists(inventory_file):
        print(f"Erro: Arquivo {inventory_file} não encontrado. Execute scripts/extrair-repos.py primeiro.")
        sys.exit(1)

    with open(inventory_file, "r", encoding="utf-8") as f:
        repos_dict = json.load(f)

    repos_list = sorted(list(repos_dict.keys()))
    total = len(repos_list)
    print(f"=== INICIANDO FORK DE {total} REPOSITÓRIOS PARA A ORGANIZAÇÃO: {args.org} ===")
    print("Aviso: Seu perfil pessoal não será poluído, todos os forks irão para a organização isolada.\n")

    sucessos = 0
    erros = 0
    ja_existentes = 0

    for idx, repo_url in enumerate(repos_list, 1):
        repo_slug = repo_url.replace("https://github.com/", "").strip()
        print(f"[{idx}/{total}] Processando {repo_slug}...")

        cmd = ["gh", "repo", "fork", repo_slug, "--org", args.org, "--clone=false"]

        if args.dry_run:
            print(f"  [DRY-RUN] Executaria: {' '.join(cmd)}")
            continue

        try:
            result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
            if result.returncode == 0:
                print(f"  -> OK: Fork criado em {args.org}/{repo_slug.split('/')[-1]}")
                sucessos += 1
            else:
                stderr = result.stderr.strip()
                if "already exists" in stderr.lower():
                    print(f"  -> AVISO: Já existe na organização.")
                    ja_existentes += 1
                else:
                    print(f"  -> ERRO ({stderr})")
                    erros += 1
        except Exception as e:
            print(f"  -> FALHA: {e}")
            erros += 1

        time.sleep(args.delay)

    print("\n=== RESUMO FINAL ===")
    print(f"Total processados: {total}")
    print(f"Criados com sucesso: {sucessos}")
    print(f"Já existentes: {ja_existentes}")
    print(f"Erros/Falhas: {erros}")

if __name__ == "__main__":
    main()
