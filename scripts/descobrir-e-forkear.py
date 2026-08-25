#!/usr/bin/env python3
"""
Mecanismo de Descoberta e Ingestão Contínua da Fábrica Universal.
Varre todos os compêndios HTML em output/listas-open-source/, detecta novos
repositórios descobertos e realiza o fork automático para arsenal-open-source
com proteção estrita contra DUPLICIDADE e rate-limit.

Uso:
  python scripts/descobrir-e-forkear.py
"""

import os
import sys
import glob
import re
import json
import subprocess
import time

def console_utf8():
    if sys.platform == "win32":
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")

def obter_repos_existentes_na_org(org_name):
    print(f"[*] Consultando repositórios ativos em '{org_name}' no GitHub...")
    cmd = ["gh", "repo", "list", org_name, "--limit", "1000", "--json", "name,nameWithOwner"]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    
    existentes = set()
    if res.returncode == 0:
        data = json.loads(res.stdout)
        for item in data:
            # Armazena o nome em minúsculo para comparação semântica estrita
            existentes.add(item["name"].lower())
            # Trata sufixos numéricos de forks como -1 se houver
            clean_name = re.sub(r'-\d+$', '', item["name"].lower())
            existentes.add(clean_name)
    else:
        print(f"[!] Aviso ao consultar organização: {res.stderr.strip()}")
    
    return existentes

def extrair_repositorios_dos_htmls():
    html_files = glob.glob("output/listas-open-source/*.html")
    catalogo = {}
    
    for file_path in html_files:
        base_name = os.path.basename(file_path)
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Expressão regular para capturar URLs do GitHub (owner/repo)
        matches = re.findall(r'github\.com/([a-zA-Z0-9_\-\.]+/[a-zA-Z0-9_\-\.]+)', content)
        for m in matches:
            cleaned = m.strip("\"'/.,)>")
            if cleaned.endswith(".git"):
                cleaned = cleaned[:-4]
            parts = cleaned.split("/")
            if len(parts) == 2 and parts[0].lower() not in ["features", "pricing", "explore", "topics", "site", "assets"]:
                repo_slug = f"{parts[0]}/{parts[1]}"
                if repo_slug not in catalogo:
                    catalogo[repo_slug] = []
                if base_name not in catalogo[repo_slug]:
                    catalogo[repo_slug].append(base_name)
                    
    return catalogo

def main():
    console_utf8()
    org_destino = "arsenal-open-source"
    print("=================================================================")
    print("  🛡️  ARSENAL OPEN SOURCE · MECANISMO DE INGESTÃO AUTOMÁTICA")
    print("=================================================================\n")

    # 1. Obter estado atual da organização no GitHub
    existentes = obter_repos_existentes_na_org(org_destino)
    print(f"[*] Repositórios já custodiados na organização: {len(existentes)}\n")

    # 2. Varrer compêndios locais
    catalogo = extrair_repositorios_dos_htmls()
    print(f"[*] Total de repositórios catalogados em todas as listas: {len(catalogo)}")

    # 3. Filtrar com ZERO duplicidade
    novos = []
    for slug, listas in catalogo.items():
        repo_name = slug.split("/")[-1].lower()
        if repo_name not in existentes:
            novos.append((slug, listas))

    print(f"[*] Novos repositórios descobertos para ingestão: {len(novos)}\n")

    if not novos:
        print("✅ Organização 100% atualizada! Nenhum novo repositório pendente de fork.")
        # Atualizar arquivo de inventário
        salvar_inventario(catalogo)
        return

    # 4. Executar fork com retentativa e backoff inteligente
    sucessos = 0
    erros = 0

    for idx, (slug, listas) in enumerate(novos, 1):
        print(f"[{idx}/{len(novos)}] Ingerindo novo repositório: {slug} (origem: {', '.join(listas[:2])})...")
        cmd = ["gh", "repo", "fork", slug, "--org", org_destino, "--clone=false"]
        
        tentativas = 0
        while tentativas < 3:
            r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
            if r.returncode == 0 or "already exists" in r.stderr.lower():
                print("  -> ✓ Fork criado com sucesso na organização!")
                sucessos += 1
                time.sleep(2.0)
                break
            elif "too quickly" in r.stderr.lower() or "rate limit" in r.stderr.lower() or "403" in r.stderr.lower():
                print("  -> ⏳ Rate-limit temporário. Aguardando 15s antes de retentar...")
                time.sleep(15.0)
                tentativas += 1
            else:
                err_msg = r.stderr.strip()[:120]
                print(f"  -> ⚠️ Falha na ingestão: {err_msg}")
                erros += 1
                time.sleep(2.0)
                break

    # 5. Atualizar inventário JSON local
    salvar_inventario(catalogo)

    print("\n=================================================================")
    print(f"  RESUMO DA INGESTÃO:")
    print(f"  - Novos repositórios adicionados: {sucessos}")
    print(f"  - Ignorados / Falhas: {erros}")
    print("=================================================================")

def salvar_inventario(catalogo):
    os.makedirs("output/forks-inventory", exist_ok=True)
    json_path = "output/forks-inventory/repositorios.json"
    with open(json_path, "w", encoding="utf-8") as f:
        # Serializar URLs completas
        full_dict = {f"https://github.com/{k}": v for k, v in sorted(catalogo.items())}
        json.dump(full_dict, f, indent=2, ensure_ascii=False)
    print(f"[*] Inventário atualizado em: {json_path}")

if __name__ == "__main__":
    main()
