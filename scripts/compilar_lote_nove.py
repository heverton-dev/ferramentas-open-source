# -*- coding: utf-8 -*-
"""
COMPILADOR EM LOTE DOS 9 DOSSIÊS VERTICAIS GOOGLE & ANTIGRAVITY
Compila os 9 arquivos JSON para output/listas-open-source/ e docs/listas/
"""
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

sys.path.insert(0, str(Path(__file__).resolve().parent))
from compilar_compendio_vertical import compilar_dossie_vertical

SLUGS = [
    "vert-google-meet",
    "vert-gmail",
    "vert-google-drive",
    "vert-google-forms",
    "vert-antigravity",
    "vert-google-labs",
    "vert-google-cloud",
    "vert-google-calendar",
    "vert-google-workspace"
]

def main():
    base_dir = Path(__file__).resolve().parent.parent
    data_dir = base_dir / "scripts" / "data"
    out_dir = base_dir / "output" / "listas-open-source"
    docs_dir = base_dir / "docs" / "listas"

    print("=" * 80)
    print(" 🚀 INICIANDO COMPILAÇÃO EM LOTE DOS 9 DOSSIÊS VERTICAIS (REGRA R5-V)")
    print("=" * 80)

    sucessos = 0
    for slug in SLUGS:
        json_file = data_dir / f"dossie-vertical-{slug.replace('vert-', '')}.json"
        if not json_file.exists():
            print(f"  [✗] Arquivo JSON não encontrado: {json_file}")
            continue

        dados = json.loads(json_file.read_text(encoding="utf-8"))
        html = compilar_dossie_vertical(dados)

        nome_html = f"{slug}.html"
        out_target = out_dir / nome_html
        docs_target = docs_dir / nome_html

        out_target.write_text(html, encoding="utf-8")
        docs_target.write_text(html, encoding="utf-8")

        print(f"  [✓] Compilado: {nome_html} (Paridade Output <-> Docs garantida)")
        sucessos += 1

    print("=" * 80)
    print(f" 📊 RESULTADO: {sucessos} DE {len(SLUGS)} DOSSIÊS COMPILADOS COM SUCESSO!")
    print("=" * 80)

    if sucessos != len(SLUGS):
        sys.exit(1)

if __name__ == "__main__":
    main()
