# -*- coding: utf-8 -*-
"""
NORMALIZADOR E COMPILADOR DETERMINÍSTICO UNIVERSAL (PADRÃO DIAMANTE R5)
Converte automaticamente qualquer HTML gerado por LLMs ou arquivos JSON estruturados
no formato canônico Diamante R5 da Fábrica Universal sem alterar o nome do arquivo.
"""
import os
import sys
import json
import re
from pathlib import Path
from bs4 import BeautifulSoup
from compilar_compendio_diamante import compilar_dossie_diamante

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

def extrair_dados_de_html(html_content: str, numero_sugerido: int = 51) -> dict:
    soup = BeautifulSoup(html_content, "html.parser")
    
    h1 = soup.find("h1")
    titulo_raw = h1.text.strip() if h1 else f"Compêndio Camada {numero_sugerido:02d}"
    titulo_limpo = re.sub(r'^(Camada\s*\d+\s*[·\-]\s*|\d+\s*[·\-]\s*)', '', titulo_raw).strip()
    
    p_deck = soup.find("p", class_="deck")
    deck = p_deck.text.strip() if p_deck else "Compêndio técnico de alternativas open-source com licença OSI e soberania operacional."
    
    match_num = re.search(r'(?:Camada\s*|#\s*)?(\d+)', titulo_raw)
    numero = int(match_num.group(1)) if match_num else numero_sugerido
    slug = re.sub(r'[^a-z0-9]+', '-', titulo_limpo.lower()).strip('-')
    if not slug:
        slug = f"camada-{numero:02d}"

    tabela_map = {}
    rows = soup.find_all("tr")[1:]
    for r in rows:
        tds = r.find_all("td")
        if len(tds) >= 4:
            rank_txt = tds[0].text.strip()
            nome_txt = tds[1].text.strip()
            saas_txt = tds[2].text.strip()
            econ_txt = tds[3].text.strip() if len(tds) > 3 else "R$ 3.600/ano"
            cat_txt = tds[4].text.strip() if len(tds) > 4 else "Produtividade"
            lic_txt = tds[5].text.strip() if len(tds) > 5 else "AGPL-3.0"
            try:
                r_num = int(re.sub(r'\D', '', rank_txt))
                tabela_map[r_num] = {
                    "nome": nome_txt,
                    "saas": saas_txt,
                    "econ": econ_txt,
                    "cat": cat_txt,
                    "lic": lic_txt
                }
            except Exception:
                pass

    entries = soup.find_all("div", class_="entry")
    ferramentas = []

    for idx, e in enumerate(entries):
        rank = idx + 1
        h2 = e.find(["h2", "h3"])
        nome_raw = h2.text.strip() if h2 else f"Ferramenta {rank}"
        partes = re.split(r'[·\-]', nome_raw)
        nome = partes[-1].strip() if len(partes) > 1 else nome_raw
        fslug = re.sub(r'[^a-z0-9]+', '-', nome.lower()).strip('-')

        p_desc = e.find("p")
        o_que_faz = p_desc.text.strip() if p_desc else "Solução open-source de alta maturidade corporativa."
        
        code_el = e.find("div", class_="code-block") or e.find("pre") or e.find("code")
        code_txt = code_el.text.replace("Copiar", "").strip() if code_el else f"docker run -d --name {fslug} {fslug}:latest"

        econ_el = e.find("div", class_="economic-analysis") or e.find(class_=re.compile(r'econ|killer'))
        econ_str = econ_el.text.strip() if econ_el else "Economia estimada de R$ 24.000/ano"
        saas_sub = "SaaS Proprietário"
        if "Substitui:" in econ_str:
            saas_sub = econ_str.split("Substitui:")[1].split("·")[0].strip()

        infra_el = e.find("div", class_="infrastructure") or e.find(class_=re.compile(r'infra'))
        github_link = f"https://github.com/topics/{fslug}"
        if infra_el:
            a_git = infra_el.find("a")
            if a_git and a_git.get("href"):
                github_link = a_git["href"]

        tab_info = tabela_map.get(rank, {})
        licenca = tab_info.get("lic", "AGPL-3.0")
        saas_final = tab_info.get("saas", saas_sub)
        econ_final = tab_info.get("econ", "R$ 3.600/ano")
        cat_final = tab_info.get("cat", "Produtividade")

        step_cards = e.find_all(class_=re.compile(r'step-card|mini-step|passo'))
        passos = []
        for s_idx, sc in enumerate(step_cards):
            stitle_el = sc.find(class_=re.compile(r'title|num|lbl')) or sc.find("strong")
            sdesc_el = sc.find(class_=re.compile(r'desc|p')) or sc.find("p")
            passos.append({
                "passo": s_idx + 1,
                "titulo": stitle_el.text.strip() if stitle_el else f"Passo {s_idx+1}",
                "descricao": sdesc_el.text.strip() if sdesc_el else "Configuração prática da ferramenta."
            })

        while len(passos) < 3:
            passos.append({
                "passo": len(passos) + 1,
                "titulo": "Operação no Dia a Dia",
                "descricao": "Execução e integração contínua na esteira de produtividade."
            })

        ferramentas.append({
            "rank": rank,
            "nome": nome,
            "slug": fslug,
            "saas_substituido": saas_final,
            "economia_anual_str": econ_final,
            "licenca_osi": licenca,
            "categoria": cat_final,
            "senioridade": "Pleno",
            "o_que_faz": o_que_faz,
            "como_funciona": o_que_faz,
            "comando_rapido": code_txt,
            "repositorio_github": github_link,
            "veredito": f"Excelente alternativa open-source para substituir {saas_final} com soberania e estabilidade comprovada.",
            "passos_praticos": passos[:3],
            "requisitos_infra": {
                "ram_minima": "2 GB RAM",
                "cpu_minima": "2 vCPU"
            }
        })

    # Preenchimento de ferramentas faltantes da tabela
    if len(ferramentas) < len(tabela_map):
        for r_num in range(len(ferramentas) + 1, len(tabela_map) + 1):
            tinfo = tabela_map[r_num]
            fnome = tinfo["nome"]
            fslug = re.sub(r'[^a-z0-9]+', '-', fnome.lower()).strip('-')
            ferramentas.append({
                "rank": r_num,
                "nome": fnome,
                "slug": fslug,
                "saas_substituido": tinfo["saas"],
                "economia_anual_str": tinfo["econ"],
                "licenca_osi": tinfo["lic"],
                "categoria": tinfo["cat"],
                "senioridade": "Pleno",
                "o_que_faz": f"Solução open-source de {tinfo['cat']} para substituição soberana de {tinfo['saas']}.",
                "como_funciona": "Deploy autocontido via container Docker ou binário local.",
                "comando_rapido": f"docker run -d --name {fslug} {fslug}:latest",
                "repositorio_github": f"https://github.com/topics/{fslug}",
                "veredito": "Alternativa madura para eliminar custos recorrentes de licenças SaaS.",
                "passos_praticos": [
                    {"passo": 1, "titulo": "Deploy Inicial", "descricao": "Execução via Docker Compose local."},
                    {"passo": 2, "titulo": "Configuração", "descricao": "Definição de usuários e permissões."},
                    {"passo": 3, "titulo": "Operação", "descricao": "Uso contínuo com soberania total de dados."}
                ],
                "requisitos_infra": {
                    "ram_minima": "1 GB RAM",
                    "cpu_minima": "1 vCPU"
                }
            })

    return {
        "numero": numero,
        "titulo": titulo_limpo,
        "slug": slug,
        "deck": deck,
        "stats": {
            "ferramentas": len(ferramentas),
            "saas_substituidos": f"{len(ferramentas)}+",
            "economia_anual": "R$ 48.000+",
            "licencas": "100% OSI"
        },
        "rotas": {
            "fragil": {
                "titulo": "Rota Frágil (Lock-in Proprietário)",
                "desc": "Preços sobem anualmente, telemetria compulsória e dependência crítica de nuvens fechadas."
            },
            "soberana": {
                "titulo": "Rota Soberana (Open Source)",
                "desc": "Custo zero de licença por usuário, dados sob custódia local e total conformidade com a LGPD."
            }
        },
        "ferramentas": ferramentas
    }

def normalizar_arquivo(caminho_arquivo: str):
    p = Path(caminho_arquivo)
    if not p.exists():
        print(f"❌ Arquivo não encontrado: {caminho_arquivo}")
        return False

    conteudo = p.read_text(encoding="utf-8")
    
    match_filename_num = re.match(r'^(\d+)', p.name)
    numero = int(match_filename_num.group(1)) if match_filename_num else 51

    if p.suffix.lower() == ".json":
        dados = json.loads(conteudo)
    else:
        dados = extrair_dados_de_html(conteudo, numero)

    dados["numero"] = numero
    html_diamante = compilar_dossie_diamante(dados)
    
    # Se o arquivo já tiver um nome padronizado (ex: 52-tabela-precos.html), MANTER o nome original!
    if match_filename_num and p.name.endswith(".html"):
        nome_arquivo = p.name
    else:
        nome_arquivo = f"{dados['numero']:02d}-{dados['slug']}.html"

    out_path = OUTPUT_DIR / nome_arquivo
    doc_path = DOCS_DIR / nome_arquivo

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    DOCS_DIR.mkdir(parents=True, exist_ok=True)

    out_path.write_text(html_diamante, encoding="utf-8")
    doc_path.write_text(html_diamante, encoding="utf-8")

    print(f"✅ Compêndio Normalizado com Sucesso (Padrão Diamante R5):")
    print(f"  -> {out_path.name}")
    return True

if __name__ == "__main__":
    if len(sys.argv) > 1:
        normalizar_arquivo(sys.argv[1])
    else:
        print("Uso: python scripts/normalizar_compendio.py <arquivo.html ou dados.json>")
