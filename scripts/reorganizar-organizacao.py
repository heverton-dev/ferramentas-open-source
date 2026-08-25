#!/usr/bin/env python3
"""
Mecanismo de Reorganização e Padronização do Arsenal Open Source.
Aplica Topics (Tags) e Descrições Padronizadas em português com o prefixo
[Camada XX · Categoria] em todos os repositórios da organização.

Uso:
  python scripts/reorganizar-organizacao.py
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

# Dicionário de Mapeamento de Camadas -> Categorias e Tags
CAMADAS_MAP = {
    "01": {"tag": "aidd-starter", "cat": "Economia de Tokens", "topic": "token-economy"},
    "02": {"tag": "aidd-squad", "cat": "Arquitetura Agêntica", "topic": "agentic-ai"},
    "03": {"tag": "design-ui", "cat": "Design & Mídia Soberana", "topic": "generative-media"},
    "04": {"tag": "aidd-sovereign", "cat": "Motores de Inferência", "topic": "llm-inference"},
    "05": {"tag": "aidd-squad", "cat": "RAG & Vetores", "topic": "rag-vector-db"},
    "06": {"tag": "aidd-squad", "cat": "Segurança & Evals", "topic": "ai-security-evals"},
    "07": {"tag": "scraping", "cat": "Scraping & Extração", "topic": "data-scraping"},
    "08": {"tag": "multimodal", "cat": "Voz & Visão", "topic": "voice-vision-ai"},
    "09": {"tag": "aidd-starter", "cat": "Harnesses & IDE", "topic": "ai-coding-harness"},
    "10": {"tag": "databases", "cat": "Bancos de Dados", "topic": "databases-engines"},
    "11": {"tag": "no-code", "cat": "No-Code & Automação", "topic": "automation-nocode"},
    "12": {"tag": "devops", "cat": "DevOps & Infra", "topic": "devops-infrastructure"},
    "13": {"tag": "iot-edge", "cat": "Edge AI & IoT", "topic": "edge-ai-iot"},
    "14": {"tag": "aidd-sovereign", "cat": "Verificação Formal", "topic": "formal-verification"},
    "15": {"tag": "reverse-eng", "cat": "Engenharia Reversa", "topic": "reverse-engineering"},
    "16": {"tag": "p2p-mesh", "cat": "Redes P2P & Mesh", "topic": "decentralized-p2p"},
    "17": {"tag": "robotics", "cat": "Simulação & Robótica", "topic": "robotics-simulation"},
    "18": {"tag": "science-bio", "cat": "IA Científica & Bio", "topic": "bioinformatics-ai"},
    "19": {"tag": "compilers", "cat": "Compiladores & WASM", "topic": "compilers-wasm"},
    "20": {"tag": "cad-3d", "cat": "CAD & Fabricação", "topic": "cad-manufacturing"},
    "21": {"tag": "fintech", "cat": "Finanças Soberanas", "topic": "sovereign-fintech"},
    "22": {"tag": "audio-dsp", "cat": "Áudio Digital & DSP", "topic": "digital-audio-dsp"},
    "23": {"tag": "virtualization", "cat": "Virtualização & OS", "topic": "virtualization-os"},
    "24": {"tag": "accessibility", "cat": "Acessibilidade", "topic": "accessibility-ergonomics"},
    "25": {"tag": "pentest", "cat": "Segurança Ofensiva", "topic": "offensive-security"},
    "26": {"tag": "gis-maps", "cat": "Geolocalização & GIS", "topic": "gis-mapping"},
    "27": {"tag": "education", "cat": "Educação & LMS", "topic": "education-lms"},
    "28": {"tag": "ecommerce", "cat": "E-Commerce Headless", "topic": "headless-ecommerce"},
    "29": {"tag": "streaming", "cat": "Streaming & Broadcast", "topic": "live-streaming"},
    "30": {"tag": "osint", "cat": "Preservação & OSINT", "topic": "osint-archiving"},
    "31": {"tag": "aidd-sovereign", "cat": "Mídia Generativa & 3D", "topic": "generative-3d-video"},
    "32": {"tag": "erp-crm", "cat": "ERP, CRM & Gestão", "topic": "enterprise-erp-crm"},
    "33": {"tag": "aidd-matrix", "cat": "Matriz AIDD", "topic": "aidd-methodology"},
}

def carregar_dados_das_listas():
    repo_info = {}
    html_files = glob.glob("output/listas-open-source/*.html")
    
    for file_path in html_files:
        base = os.path.basename(file_path)
        # extrair numero da camada se houver (ex: 01, 31, 32)
        match_num = re.match(r'^(\d{2})', base)
        num_camada = match_num.group(1) if match_num else "00"
        
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Extrair entradas do ledger
        # Ex: <h3>Nome</h3> ... <span class="kind">Categoria</span> ... <span class="label">1. O Que Faz</span> <p>Desc</p>
        entries = re.findall(r'<div class="entry">.*?<h3>(.*?)</h3>.*?<span class="kind">(.*?)</span>.*?<span class="label">1\. O Que Faz</span>\s*<p>(.*?)</p>.*?github\.com/([a-zA-Z0-9_\-\.]+/[a-zA-Z0-9_\-\.]+)', content, re.DOTALL)
        for name_entry, kind, what_does, repo_slug in entries:
            clean_slug = repo_slug.strip("\"'/.,)>")
            repo_name = clean_slug.split("/")[-1].lower()
            clean_desc = re.sub(r'<.*?>', '', what_does).strip().replace('\n', ' ')
            
            repo_info[repo_name] = {
                "camada": num_camada,
                "kind": kind.strip(),
                "desc": clean_desc,
                "slug": clean_slug
            }
            
    return repo_info

def main():
    console_utf8()
    org_name = "arsenal-open-source"
    print("=================================================================")
    print("  🏷️  REORGANIZAÇÃO & PADRONIZAÇÃO DO ARSENAL OPEN SOURCE")
    print("=================================================================\n")

    # 1. Carregar mapa de informações
    info_map = carregar_dados_das_listas()
    print(f"[*] Mapeadas {len(info_map)} descrições estruturadas das listas.")

    # 2. Listar repos da organização
    cmd = ["gh", "repo", "list", org_name, "--limit", "500", "--json", "name,description"]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    if res.returncode != 0:
        print(f"Erro ao listar organização: {res.stderr}")
        return

    repos = json.loads(res.stdout)
    total = len(repos)
    print(f"[*] Total de repositórios na organização para padronizar: {total}\n")

    sucessos = 0
    for idx, r in enumerate(repos, 1):
        repo_name = r["name"]
        if repo_name == ".github":
            continue

        clean_key = re.sub(r'-\d+$', '', repo_name.lower())
        dados = info_map.get(clean_key) or info_map.get(repo_name.lower())

        if dados:
            camada_num = dados["camada"]
            meta_camada = CAMADAS_MAP.get(camada_num, {"tag": "soberania-tech", "cat": "Soberania", "topic": "open-source"})
            categoria = meta_camada["cat"]
            short_desc = dados["desc"][:180].rstrip('.') + '.'
            nova_desc = f"[Camada {camada_num} · {categoria}] {short_desc}"
            
            topics = ["arsenal-open-source", "soberania-tech", meta_camada["tag"], meta_camada["topic"]]
        else:
            nova_desc = f"[Arsenal Soberano] {r.get('description') or 'Repositório de código aberto custodiado e sincronizado.'}"
            topics = ["arsenal-open-source", "soberania-tech"]

        print(f"[{idx}/{total}] Reorganizando: {repo_name}...")
        print(f"  -> Descrição: {nova_desc[:80]}...")
        print(f"  -> Topics: {', '.join(topics)}")

        # Atualizar no GitHub via gh repo edit
        edit_cmd = ["gh", "repo", "edit", f"{org_name}/{repo_name}", "--description", nova_desc]
        for t in topics:
            edit_cmd.extend(["--add-topic", t])

        try:
            r_edit = subprocess.run(edit_cmd, capture_output=True, text=True, encoding="utf-8")
            if r_edit.returncode == 0:
                print("  -> ✓ Atualizado com sucesso!")
                sucessos += 1
            else:
                print(f"  -> ⚠️ Aviso: {r_edit.stderr.strip()[:100]}")
        except Exception as e:
            print(f"  -> Falha: {e}")

        time.sleep(1.0)

    print("\n=================================================================")
    print(f"  REORGANIZAÇÃO CONCLUÍDA: {sucessos} repositórios padronizados!")
    print("=================================================================")

if __name__ == "__main__":
    main()
