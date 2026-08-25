# -*- coding: utf-8 -*-
"""
Audita a discrepância entre a Matriz Comparativa (Tabela) e as Fichas Técnicas (Ledger)
em todas as 49 listas HTML.
"""
import os
import sys
from bs4 import BeautifulSoup

def console_utf8():
    if sys.platform == "win32":
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")

console_utf8()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = os.path.join(BASE_DIR, "output", "listas-open-source")

def auditar():
    arquivos = [f for f in os.listdir(OUTPUT_DIR) if f.endswith(".html") and f != "index.html"]
    print(f"[*] Auditando integridade de 20/20 ferramentas em {len(arquivos)} listas...\n")
    
    incompletas = []
    
    for arq in sorted(arquivos):
        p = os.path.join(OUTPUT_DIR, arq)
        with open(p, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f.read(), "html.parser")
            
        linhas_tabela = len(soup.find_all("tr")) - 1 # subtrai header
        # Se nao tiver tr, conta td.rank
        ranks = len(soup.find_all("td", class_="rank"))
        if ranks > 0:
            linhas_tabela = ranks
            
        fichas = len(soup.find_all("div", class_="entry"))
        
        status = "COMPLETA" if linhas_tabela == fichas and fichas >= 8 else "INCOMPLETA"
        if status == "INCOMPLETA":
            incompletas.append((arq, linhas_tabela, fichas))
            print(f"  [!] {arq:<55} | Tabela: {linhas_tabela:>2} | Fichas: {fichas:>2} --> FALTAM {linhas_tabela - fichas} FICHAS")
        else:
            print(f"  [✓] {arq:<55} | Tabela: {linhas_tabela:>2} | Fichas: {fichas:>2}")
            
    print(f"\nTotal de listas incompletas: {len(incompletas)} de {len(arquivos)}")
    return incompletas

if __name__ == "__main__":
    auditar()
