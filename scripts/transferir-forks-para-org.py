#!/usr/bin/env python3
"""
Script para transferir automaticamente todos os repositórios do tipo FORK
da conta pessoal Heverton-web para a organização arsenal-open-source.
"""

import sys
import json
import subprocess
import time

def console_utf8():
    if sys.platform == "win32":
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")

def main():
    console_utf8()
    org_destino = "arsenal-open-source"
    print(f"=== INICIANDO TRANSFERÊNCIA DE FORKS PARA A ORGANIZAÇÃO: {org_destino} ===")

    # Listar todos os repositórios da conta que são fork
    cmd_list = ["gh", "repo", "list", "Heverton-web", "--fork", "--limit", "200", "--json", "name,nameWithOwner,isFork"]
    res = subprocess.run(cmd_list, capture_output=True, text=True, encoding="utf-8")
    
    if res.returncode != 0:
        print(f"Erro ao listar repositórios: {res.stderr}")
        sys.exit(1)

    forks = json.loads(res.stdout)
    total = len(forks)
    print(f"Total de repositórios FORK encontrados na conta pessoal: {total}\n")

    sucessos = 0
    erros = 0

    for idx, repo in enumerate(forks, 1):
        repo_name = repo["name"]
        print(f"[{idx}/{total}] Transferindo {repo_name} -> {org_destino}/{repo_name}...")

        cmd_transfer = [
            "gh", "api", "-X", "POST",
            f"repos/Heverton-web/{repo_name}/transfer",
            "-f", f"new_owner={org_destino}"
        ]

        try:
            r = subprocess.run(cmd_transfer, capture_output=True, text=True, encoding="utf-8")
            if r.returncode == 0:
                print(f"  -> OK: Transferido com sucesso!")
                sucessos += 1
            else:
                err_msg = r.stderr.strip()
                print(f"  -> AVISO/ERRO: {err_msg}")
                erros += 1
        except Exception as e:
            print(f"  -> FALHA: {e}")
            erros += 1

        time.sleep(1.0)

    print("\n=== RESUMO DA TRANSFERÊNCIA ===")
    print(f"Total avaliados: {total}")
    print(f"Transferidos com sucesso: {sucessos}")
    print(f"Erros / Já existentes: {erros}")

if __name__ == "__main__":
    main()
