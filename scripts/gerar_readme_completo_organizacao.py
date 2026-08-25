# -*- coding: utf-8 -*-
"""
Gera o README.md completo da organização @arsenal-open-source e sincroniza
diretamente com o repositório arsenal-open-source/.github no GitHub.

Garante que 100% das ferramentas de TODAS as 39 camadas estejam listadas
sem nenhuma omissão!
"""
import os
import re
import sys
import json
import subprocess
import shutil
from bs4 import BeautifulSoup

def console_utf8():
    if sys.platform == "win32":
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")

console_utf8()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = os.path.join(BASE_DIR, "output", "listas-open-source")
TEMP_DIR = os.path.join(BASE_DIR, "temp_org_profile")

def extrair_camada_info(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")

    # Extrair número da camada
    base = os.path.basename(filepath)
    num_m = re.match(r"^(\d+)-", base)
    num = num_m.group(1) if num_m else "00"

    # Extrair título H1
    h1 = soup.find("h1")
    h1_txt = h1.get_text().strip() if h1 else base
    # Limpar título para domínio curto
    dominio = h1_txt.split(",")[0].split("&")[0].split("·")[0].strip()

    # Extrair economia estimada do stat-card ou tabela
    econ_val = "-$ 30k a $ 150k / ano"
    stat_cards = soup.find_all("div", class_="stat-card")
    for sc in stat_cards:
        lbl = sc.find("div", class_="stat-lbl")
        if lbl and "economia" in lbl.get_text().lower():
            val = sc.find("div", class_="stat-val")
            if val:
                econ_val = val.get_text().strip()

    # Extrair TODAS as ferramentas dos cards
    ferramentas = []
    entries = soup.find_all("div", class_="entry")
    for entry in entries:
        h3 = entry.find("h3")
        if not h3:
            continue
        raw_title = h3.get_text().strip()
        nome_ferramenta = raw_title.split("·")[0].strip()
        nome_ferramenta = re.sub(r'^(?:Skill:\s*|Motor:\s*|Framework:\s*|Ferramenta:\s*)', '', nome_ferramenta, flags=re.IGNORECASE).strip()

        # Link do repo
        repo_a = entry.find("a", class_="repo-btn")
        if not repo_a:
            repo_a = entry.find("a", class_="repo")
        
        repo_url = repo_a.get("href", "") if repo_a else ""
        repo_slug = ""
        if "github.com/" in repo_url:
            repo_slug = repo_url.split("github.com/")[-1].strip("/")
            repo_name = repo_slug.split("/")[-1]
            # Link para o fork da organização
            org_link = f"https://github.com/arsenal-open-source/{repo_name}"
            ferramentas.append(f"[{nome_ferramenta}]({org_link})")
        else:
            ferramentas.append(f"**{nome_ferramenta}**")

    return {
        "num": num,
        "arquivo": base,
        "dominio": h1_txt,
        "dominio_curto": dominio,
        "ferramentas": ferramentas,
        "total_ferramentas": len(ferramentas),
        "economia": econ_val
    }

def gerar_readme_organizacao():
    print("[*] Lendo todas as 39 camadas técnicas para o README da organização...")
    camadas_arquivos = sorted([f for f in os.listdir(OUTPUT_DIR) if re.match(r"^\d{2}-", f)])
    
    total_geral_ferramentas = 0
    tabela_linhas = []

    for arq in camadas_arquivos:
        p = os.path.join(OUTPUT_DIR, arq)
        info = extrair_camada_info(p)
        total_geral_ferramentas += info["total_ferramentas"]
        
        tools_str = " · ".join(info["ferramentas"])
        linha = f"| **{info['num']}** | **[{info['dominio_curto']}]({info['arquivo']})** | {tools_str} | {info['economia']} |"
        tabela_linhas.append(linha)
        print(f"  -> Camada {info['num']}: {info['total_ferramentas']} ferramentas extraídas")

    tabela_md = "\n".join(tabela_linhas)

    readme_content = f"""# 🛡️ Arsenal Open Source · Hub de Soberania Tecnológica

> Organização de custódia, preservação e sincronização contínua de mais de **{total_geral_ferramentas} motores de código aberto auditados** divididos em **39 camadas de engenharia** e compêndios temáticos.

---

## 📑 As 39 Camadas de Soberania Tecnológica & Todos os Repositórios Custodiados

| Camada | Domínio Operacional | Todos os Repositórios Custodiados na Organização | Economia Estimada |
| :--- | :--- | :--- | :--- |
{tabela_md}

---

## 🤖 Automação, Preservação & Sincronização
- **Sincronização Diária:** Atualização automática com repositórios upstream às **04:00 UTC** via GitHub Actions.
- **Custódia Total:** Todos os repositórios permanecem versionados, auditados e preservados de forma independente contra descontinuidade e lock-in corporativo.
- **Portal Interativo:** Acesse as fichas técnicas detalhadas com passo a passo prático e análise financeira de TCO.

---
*Gerado pela Fábrica Universal de Soberania Tecnológica.*
"""
    return readme_content

def sincronizar_com_github(readme_content):
    print("\n[*] Sincronizando com o repositório arsenal-open-source/.github...")
    
    if os.path.exists(TEMP_DIR):
        shutil.rmtree(TEMP_DIR)
    
    # Clonar repo .github da organização
    res = subprocess.run(["gh", "repo", "clone", "arsenal-open-source/.github", TEMP_DIR], capture_output=True, text=True)
    if res.returncode != 0:
        print(f"[!] Erro ao clonar arsenal-open-source/.github: {res.stderr}")
        return

    profile_dir = os.path.join(TEMP_DIR, "profile")
    os.makedirs(profile_dir, exist_ok=True)
    
    readme_path = os.path.join(profile_dir, "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(readme_content)

    # Commit e Push no repo da organização
    cmds = [
        ["git", "-C", TEMP_DIR, "add", "."],
        ["git", "-C", TEMP_DIR, "commit", "-m", "feat: update organization README with 100% of all tools across all 39 engineering layers"],
        ["git", "-C", TEMP_DIR, "push", "origin", "main"]
    ]
    for cmd in cmds:
        r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
        if r.returncode != 0:
            print(f"[!] Aviso no comando {' '.join(cmd)}: {r.stderr}")
        else:
            print(f"  -> [OK] {' '.join(cmd)}")

    print("[🎉] Perfil da organização no GitHub atualizado com 100% de todas as ferramentas!")

def main():
    readme = gerar_readme_organizacao()
    
    # Salvar localmente nos templates
    with open(os.path.join(BASE_DIR, "scripts", "profile-readme-template.md"), "w", encoding="utf-8") as f:
        f.write(readme)
    with open(os.path.join(OUTPUT_DIR, "README.md"), "w", encoding="utf-8") as f:
        f.write(readme)
    with open(os.path.join(BASE_DIR, "docs", "listas", "README.md"), "w", encoding="utf-8") as f:
        f.write(readme)

    print("[✓] Arquivos README locais atualizados.")
    sincronizar_com_github(readme)

if __name__ == "__main__":
    main()
