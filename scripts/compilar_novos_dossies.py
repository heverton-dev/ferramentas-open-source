# -*- coding: utf-8 -*-
"""
COMPILADOR DE DOSSIÊS: OPERAÇÃO INDUSTRIAL & INTELIGÊNCIA/INFRAESTRUTURA
Gera os compêndios no Padrão Dossiê Executivo Diamante R5 a partir dos JSONs canônicos.
Regras atendidas: R1 (PT-BR), R5 (Diamante), R13 (Prefixos semânticos canônicos) e R18 (Paridade e zero entulho).
"""
import os
import sys
import json
from pathlib import Path

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
DATA_DIR = BASE_DIR / "scripts" / "data"

sys.path.insert(0, str(BASE_DIR / "scripts"))
from compilar_compendio_diamante import compilar_dossie_diamante

DOSSIES = [
    {
        "json_path": DATA_DIR / "dossie-operacao-industrial.json",
        "output_name": "list-operacao-industrial.html"
    },
    {
        "json_path": DATA_DIR / "dossie-inteligencia-infra.json",
        "output_name": "list-inteligencia-infra.html"
    }
]

def compilar_todos():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    
    for item in DOSSIES:
        p_json = item["json_path"]
        if not p_json.exists():
            print(f"❌ JSON não encontrado: {p_json}")
            sys.exit(1)
            
        dados = json.loads(p_json.read_text(encoding="utf-8"))
        html = compilar_dossie_diamante(dados)
        
        p_out = OUTPUT_DIR / item["output_name"]
        p_doc = DOCS_DIR / item["output_name"]
        
        p_out.write_text(html, encoding="utf-8")
        p_doc.write_text(html, encoding="utf-8")
        
        print(f"✅ Compêndio compilado com sucesso (Padrão Diamante R5):")
        print(f"   -> {p_out.name} ({len(dados['ferramentas'])} ferramentas)")

if __name__ == "__main__":
    compilar_todos()
