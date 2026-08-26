# -*- coding: utf-8 -*-
"""
SCRIPT EXECUTOR DO DOSSIÊ VERTICAL CANÔNICO: GRANOLA
Lê scripts/data/dossie-vertical-granola.json e compila em output/ e docs/
seguindo o Padrão Diamante R5-V com a Seção 5 de MCPs e Skills.
"""
import json
import sys
from pathlib import Path
from compilar_compendio_vertical import compilar_dossie_vertical

def console_utf8():
    if sys.platform == "win32":
        try:
            sys.stdout.reconfigure(encoding="utf-8")
            sys.stderr.reconfigure(encoding="utf-8")
        except Exception:
            pass

console_utf8()

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "scripts" / "data" / "dossie-vertical-granola.json"
OUTPUT_FILE = BASE_DIR / "output" / "listas-open-source" / "vert-granola.html"
DOCS_FILE = BASE_DIR / "docs" / "listas" / "vert-granola.html"

dados = json.loads(DATA_FILE.read_text(encoding="utf-8"))
html = compilar_dossie_vertical(dados)

OUTPUT_FILE.write_text(html, encoding="utf-8")
DOCS_FILE.write_text(html, encoding="utf-8")

print(f"✅ Dossiê Vertical do Granola Gerado com Sucesso!")
print(f"   -> Arquivo: {OUTPUT_FILE.name}")
print(f"   -> Quinteto Soberano: Screenpipe, WhisperX, Open-NotebookLM, Whisper.cpp, Faster-Whisper")
print(f"   -> Seção 5 de MCPs & Skills 100% Integrada!")
