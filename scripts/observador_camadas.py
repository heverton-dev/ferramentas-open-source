# -*- coding: utf-8 -*-
"""
OBSERVADOR AUTÔNOMO CONTÍNUO (DAEMON DE COMPILAÇÃO DIAMANTE R5)
Monitora continuamente as pastas output/ e docs/.
Se qualquer IDE ou LLM externa (Mimocode, Cursor, etc) gravar um arquivo HTML fora do padrão Diamante R5,
este serviço detecta imediatamente e reescreve no formato oficial em milissegundos.
"""
import os
import sys
import time
from pathlib import Path
from normalizar_compendio import normalizar_arquivo

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

def verificar_e_curar_compendio(caminho: Path):
    if not caminho.name.endswith(".html") or not caminho.is_file():
        return False
    
    try:
        conteudo = caminho.read_text(encoding="utf-8")
    except Exception:
        return False

    # Marcadores de layout não-conforme (gerados por LLMs sem compilador)
    desvios = [
        "economic-analysis" in conteudo,
        "steps-grid" in conteudo,
        "max-width: 960px" in conteudo,
        "--paper: #ECEEF2" in conteudo,
        "text-align: justify; text-justify: inter-word;" in conteudo,
        ('<div class="cols"' in conteudo),
        (not ("entry-rank" in conteudo or "entry-body" in conteudo or "step-num-badge" in conteudo))
    ]

    if any(desvios):
        print(f"⚡ [AUTO-CURA DETECTADA] Transmutando {caminho.name} para o Padrão Diamante R5...")
        normalizar_arquivo(str(caminho))
        # Sincronizar espelho
        os.system("python scripts/limpar_entulho.py >nul 2>&1")
        return True

    return False

def ciclo_verificacao():
    alterados = 0
    for pasta in [DOCS_DIR, OUTPUT_DIR]:
        if not pasta.exists():
            continue
        for html_file in pasta.glob("[0-9][0-9]-*.html"):
            if verificar_e_curar_compendio(html_file):
                alterados += 1
    return alterados

def rodar_observador():
    print("[*] 🛡️ Observador Autônomo Diamante R5 Ativado.")
    print("[*] Monitorando docs/listas e output/listas-open-source...")
    while True:
        try:
            ciclo_verificacao()
            time.sleep(3)
        except KeyboardInterrupt:
            print("\n[*] Observador finalizado.")
            break
        except Exception as e:
            time.sleep(3)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--uma-vez":
        ciclo_verificacao()
    else:
        rodar_observador()
