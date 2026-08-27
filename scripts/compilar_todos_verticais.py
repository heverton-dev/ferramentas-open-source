# -*- coding: utf-8 -*-
"""
COMPILADOR DETERMINÍSTICO UNIVERSAL DE DOSSIÊS VERTICAIS (REGRA R5-V)
Varre scripts/data/dossie-vertical-*.json, compila para output/listas-open-source/ e espelha em docs/listas/
"""
import sys
import glob
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

def main():
    base_dir = Path(__file__).resolve().parent.parent
    data_dir = base_dir / "scripts" / "data"
    out_dir = base_dir / "output" / "listas-open-source"
    docs_dir = base_dir / "docs" / "listas"

    arquivos_json = sorted(list(data_dir.glob("dossie-vertical-*.json")))
    print("=" * 80)
    print(f" 🚀 COMPILANDO {len(arquivos_json)} DOSSIÊS VERTICAIS (REGRA R5-V)")
    print("=" * 80)

    sucessos = 0
    for jf in arquivos_json:
        dados = json.loads(jf.read_text(encoding="utf-8"))
        slug_raw = dados.get("slug", jf.stem)
        slug_clean = slug_raw.replace("dossie-vertical-", "").replace("vert-", "")
        slug = f"vert-{slug_clean}"

        html = compilar_dossie_vertical(dados)
        nome_html = f"{slug}.html"

        (out_dir / nome_html).write_text(html, encoding="utf-8")
        (docs_dir / nome_html).write_text(html, encoding="utf-8")
        print(f"  [✓] Compilado com sucesso: {nome_html}")
        sucessos += 1

    # Remove artefato residual se existir
    for path in [out_dir / "vert-dossie-vertical-granola.html", docs_dir / "vert-dossie-vertical-granola.html"]:
        if path.exists():
            path.unlink()

    print("=" * 80)
    print(f" 📊 SUCESSO: {sucessos} DE {len(arquivos_json)} COMPILADOS!")
    print("=" * 80)

if __name__ == "__main__":
    main()
