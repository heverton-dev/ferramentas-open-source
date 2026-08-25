#!/usr/bin/env python3
"""
Script para processar os repositórios faltantes com backoff inteligente contra rate-limit.
"""

import os
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
    
    # 1. Obter lista de repos já existentes na organização
    res = subprocess.run(
        ["gh", "repo", "list", org_destino, "--limit", "500", "--json", "name"],
        capture_output=True, text=True, encoding="utf-8"
    )
    existentes = set()
    if res.returncode == 0:
        data = json.loads(res.stdout)
        existentes = {item["name"].lower() for item in data}

    # 2. Ler inventário total
    with open("output/forks-inventory/repositorios.json", "r", encoding="utf-8") as f:
        repos_dict = json.load(f)

    faltantes = []
    for url in repos_dict.keys():
        repo_slug = url.replace("https://github.com/", "").strip()
        repo_name = repo_slug.split("/")[-1].lower()
        if repo_name not in existentes:
            faltantes.append(repo_slug)

    total = len(faltantes)
    print(f"=== PROCESSANDO {total} REPOSITÓRIOS FALTANTES COM BACKOFF ===")
    
    sucessos = 0
    for idx, repo_slug in enumerate(faltantes, 1):
        print(f"[{idx}/{total}] Forkeando {repo_slug}...")
        cmd = ["gh", "repo", "fork", repo_slug, "--org", org_destino, "--clone=false"]
        
        tentativas = 0
        while tentativas < 3:
            r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
            if r.returncode == 0 or "already exists" in r.stderr.lower():
                print(f"  -> OK!")
                sucessos += 1
                time.sleep(2.5)
                break
            elif "too quickly" in r.stderr.lower() or "rate limit" in r.stderr.lower():
                print("  -> Rate-limit atingido. Aguardando 15 segundos...")
                time.sleep(15)
                tentativas += 1
            else:
                print(f"  -> AVISO: {r.stderr.strip()[:100]}")
                time.sleep(2)
                break

    print(f"\nFinalizado! {sucessos} novos repositórios sincronizados.")

if __name__ == "__main__":
    main()
