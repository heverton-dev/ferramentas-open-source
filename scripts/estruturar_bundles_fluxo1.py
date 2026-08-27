# -*- coding: utf-8 -*-
"""
MIGRADOR IDEMPOTENTE DE BUNDLES DO FLUXO 1
Move os artefatos HTML/MD/PDF existentes na raiz de cada list-<slug>/
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
LISTAS_DIR = BASE_DIR / "output" / "01-listas-horizontais"
DATA_DIR = BASE_DIR / "scripts" / "data"

sys.path.insert(0, str(BASE_DIR / "scripts"))

def migrar_bundle(bundle_dir: Path) -> dict:
    """Migra um único bundle list-<slug>/ para a nova estrutura."""
    slug = bundle_dir.name.replace("list-", "")
    materiais_dir = bundle_dir / "materiais"
    relatorios_dir = bundle_dir / "relatorios"

    # Já migrado?
    if materiais_dir.exists() and any(materiais_dir.glob("*.html")):
        return {"slug": slug, "status": "JA_MIGRADO"}

    materiais_dir.mkdir(parents=True, exist_ok=True)
    relatorios_dir.mkdir(parents=True, exist_ok=True)

    movidos = []
    for ext in ["*.html", "*.md", "*.pdf"]:
        for arq in bundle_dir.glob(ext):
            # Não mover arquivos já dentro de subpastas
            if arq.parent == bundle_dir:
                dest = materiais_dir / arq.name
                shutil.move(str(arq), str(dest))
                movidos.append(arq.name)

    return {"slug": slug, "status": "MIGRADO", "arquivos": movidos}


def gerar_relatorio_pos_migracao(bundle_dir: Path, slug: str) -> None:
    """Gera o relatório de execução tripartite para bundles migrados usando os dados existentes."""
    data_file = DATA_DIR / f"lista-{slug}.json"
    if not data_file.exists():
        print(f"   ⚠️ JSON de dados não encontrado para '{slug}' — relatório pulado.")
        return

    try:
        from gerar_relatorio_fluxo1 import gerar_relatorio_tripartite
        with open(data_file, "r", encoding="utf-8") as f:
            dados = json.load(f)

        materiais_dir = bundle_dir / "materiais"
        relatorios_dir = bundle_dir / "relatorios"
        relatorios_dir.mkdir(parents=True, exist_ok=True)

        # Só gera se a pasta de relatórios estiver vazia
        if not any(relatorios_dir.glob("*.html")):
            gerar_relatorio_tripartite(slug, dados, materiais_dir, relatorios_dir)
            print(f"   📊 Relatório gerado para: {slug}")
        else:
            print(f"   ✅ Relatório já existe: {slug}")
    except Exception as e:
        print(f"   ⚠️ Erro ao gerar relatório para '{slug}': {e}")


def main():
    print("=" * 70)
    print("🔄 MIGRADOR IDEMPOTENTE DE BUNDLES DO FLUXO 1 (R10)")
    print("   Reestruturando: list-<slug>/ → materiais/ + relatorios/")
    print("=" * 70)

    if not LISTAS_DIR.exists():
        print(f"❌ Pasta não encontrada: {LISTAS_DIR}")
        sys.exit(1)

    bundles = sorted([d for d in LISTAS_DIR.iterdir() if d.is_dir() and d.name.startswith("list-")])
    total = len(bundles)
    migrados = 0
    ja_ok = 0

    for bundle in bundles:
        slug = bundle.name.replace("list-", "")
        print(f"\n→ Processando: {bundle.name}")
        resultado = migrar_bundle(bundle)

        if resultado["status"] == "JA_MIGRADO":
            print(f"   ✅ Já está na estrutura correta.")
            ja_ok += 1
        else:
            arquivos = resultado.get("arquivos", [])
            print(f"   ✅ Migrado: {len(arquivos)} arquivo(s) → materiais/")
            for a in arquivos:
                print(f"      - {a}")
            migrados += 1

        # Gera relatório se ainda não existir
        gerar_relatorio_pos_migracao(bundle, slug)

    print("\n" + "=" * 70)
    print(f"✅ MIGRAÇÃO CONCLUÍDA: {total} bundles | {migrados} migrados | {ja_ok} já conformes")
    print("=" * 70)
    sys.exit(0)


if __name__ == "__main__":
    main()
