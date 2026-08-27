# -*- coding: utf-8 -*-
"""
ESTRUTURADOR IDEMPOTENTE DE BUNDLES DO FLUXO 2 (R10)
Move os artefatos HTML/MD/PDF existentes na raiz de cada vert-<saas>/
para a subpasta materiais/ e cria relatorios/ para futura geração.
Seguro de rodar N vezes (idempotente - Regra R10).
"""
import sys
import json
import shutil
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
DOSSIES_DIR = BASE_DIR / "output" / "02-dossies-verticais"
DATA_DIR = BASE_DIR / "scripts" / "data"

sys.path.insert(0, str(BASE_DIR / "scripts"))

def migrar_bundle_fluxo2(bundle_dir: Path) -> dict:
    """Migra um único bundle vert-<saas>/ para a nova estrutura."""
    saas = bundle_dir.name.replace("vert-", "")
    materiais_dir = bundle_dir / "materiais"
    relatorios_dir = bundle_dir / "relatorios"

    if materiais_dir.exists() and any(materiais_dir.glob("*.html")):
        return {"saas": saas, "status": "JA_MIGRADO"}

    materiais_dir.mkdir(parents=True, exist_ok=True)
    relatorios_dir.mkdir(parents=True, exist_ok=True)

    movidos = []
    for ext in ["*.html", "*.md", "*.pdf"]:
        for arq in bundle_dir.glob(ext):
            if arq.parent == bundle_dir:
                dest = materiais_dir / arq.name
                shutil.move(str(arq), str(dest))
                movidos.append(arq.name)

    return {"saas": saas, "status": "MIGRADO", "arquivos": movidos}


def gerar_relatorio_pos_migracao_fluxo2(bundle_dir: Path, saas: str) -> None:
    """Gera relatório de execução tripartite se houver dados JSON."""
    data_file = DATA_DIR / f"dossie-vertical-{saas}.json"
    if not data_file.exists():
        return

    try:
        from gerar_relatorio_fluxo2 import gerar_relatorio_tripartite_fluxo2
        with open(data_file, "r", encoding="utf-8") as f:
            dados = json.load(f)

        materiais_dir = bundle_dir / "materiais"
        relatorios_dir = bundle_dir / "relatorios"
        relatorios_dir.mkdir(parents=True, exist_ok=True)

        if not any(relatorios_dir.glob("*.html")):
            gerar_relatorio_tripartite_fluxo2(saas, dados, materiais_dir, relatorios_dir)
            print(f"   📊 Relatório gerado para: vert-{saas}")
        else:
            print(f"   ✅ Relatório já existe: vert-{saas}")
    except Exception as e:
        print(f"   ⚠️ Erro ao gerar relatório para vert-{saas}: {e}")


def main():
    print("=" * 70)
    print("🔄 ESTRUTURADOR IDEMPOTENTE DE BUNDLES DO FLUXO 2 (R10)")
    print("   Reestruturando: vert-<saas>/ → materiais/ + relatorios/")
    print("=" * 70)

    if not DOSSIES_DIR.exists():
        print(f"❌ Pasta não encontrada: {DOSSIES_DIR}")
        sys.exit(1)

    bundles = sorted([d for d in DOSSIES_DIR.iterdir() if d.is_dir() and d.name.startswith("vert-")])
    total = len(bundles)
    migrados = 0
    ja_ok = 0

    for bundle in bundles:
        saas = bundle.name.replace("vert-", "")
        resultado = migrar_bundle_fluxo2(bundle)

        if resultado["status"] == "JA_MIGRADO":
            ja_ok += 1
        else:
            arquivos = resultado.get("arquivos", [])
            print(f"→ Migrado {bundle.name}: {len(arquivos)} arquivo(s) → materiais/")
            migrados += 1

        gerar_relatorio_pos_migracao_fluxo2(bundle, saas)

    print("\n" + "=" * 70)
    print(f"✅ CONCLUÍDO: {total} bundles | {migrados} migrados | {ja_ok} já conformes")
    print("=" * 70)
    sys.exit(0)


if __name__ == "__main__":
    main()
