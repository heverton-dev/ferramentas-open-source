# -*- coding: utf-8 -*-
"""
CLI MESTRA DA FÁBRICA UNIVERSAL: ORQUESTRADOR CENTRAL DE COMPÊNDIOS
Permite disparar a geração de compêndios tanto em modo LISTA (Horizontal R5)
quanto em modo FOCO NA FERRAMENTA (Vertical R5-V).

Uso:
  python scripts/esteira.py lista dados.json [--slug <nome>]
  python scripts/esteira.py vertical dossie_saas.json [--slug <nome>]
  python scripts/esteira.py auditar
  python scripts/esteira.py limpar
"""
import os
import sys
import json
import argparse
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
SCRIPTS_DIR = BASE_DIR / "scripts"

sys.path.insert(0, str(SCRIPTS_DIR))
from compilar_compendio_diamante import compilar_dossie_diamante
from compilar_compendio_vertical import compilar_dossie_vertical

def disparar_lista(arquivo_json: str, slug_custom: str = None):
    p = Path(arquivo_json)
    if not p.exists():
        print(f"❌ Arquivo JSON não encontrado: {arquivo_json}")
        sys.exit(1)

    dados = json.loads(p.read_text(encoding="utf-8"))
    slug = slug_custom or dados.get("slug", p.stem.replace("dados_", "").replace("lista_", ""))
    if not any(slug.startswith(pref) for pref in ["list-", "tco-", "guia-"]):
        slug = f"list-{slug}"
    
    nome_arquivo = f"{slug}.html" if not slug.endswith(".html") else slug

    print(f"\n[+] Compilando LISTA HORIZONTAL (Padrão Diamante R5): {nome_arquivo}")
    html = compilar_dossie_diamante(dados)

    out_file = BASE_DIR / "output" / "listas-open-source" / nome_arquivo
    docs_file = BASE_DIR / "docs" / "listas" / nome_arquivo

    out_file.write_text(html, encoding="utf-8")
    docs_file.write_text(html, encoding="utf-8")

    print(f"✅ Compêndio gerado com sucesso:")
    print(f"   -> {out_file.relative_to(BASE_DIR)}")
    print(f"   -> {docs_file.relative_to(BASE_DIR)}")

    # Auto-cura & auditoria
    os.system("python scripts/limpar_entulho.py")

def disparar_vertical(arquivo_json: str, slug_custom: str = None):
    p = Path(arquivo_json)
    if not p.exists():
        print(f"❌ Arquivo JSON não encontrado: {arquivo_json}")
        sys.exit(1)

    dados = json.loads(p.read_text(encoding="utf-8"))
    slug = slug_custom or dados.get("slug", p.stem.replace("dossie-vertical-", "").replace("vert-", ""))
    if not slug.startswith("vert-"):
        slug = f"vert-{slug}"

    nome_arquivo = f"{slug}.html" if not slug.endswith(".html") else slug

    print(f"\n[+] Compilando DOSSIÊ VERTICAL (Padrão Diamante R5-V · Foco na Ferramenta): {nome_arquivo}")
    html = compilar_dossie_vertical(dados)

    out_file = BASE_DIR / "output" / "listas-open-source" / nome_arquivo
    docs_file = BASE_DIR / "docs" / "listas" / nome_arquivo

    out_file.write_text(html, encoding="utf-8")
    docs_file.write_text(html, encoding="utf-8")

    print(f"✅ Dossiê Vertical gerado com sucesso:")
    print(f"   -> {out_file.relative_to(BASE_DIR)}")
    print(f"   -> {docs_file.relative_to(BASE_DIR)}")

    # Auto-cura & auditoria
    os.system("python scripts/limpar_entulho.py")

def main():
    parser = argparse.ArgumentParser(
        description="Fábrica Universal: Orquestrador de Compêndios (Lista & Foco na Ferramenta)"
    )
    subparsers = parser.add_subparsers(dest="comando", help="Comando a executar")

    # Comando LISTA
    p_lista = subparsers.add_parser("lista", help="Gera uma LISTA temática horizontal (list-*.html)")
    p_lista.add_argument("arquivo", help="Caminho do arquivo JSON com dados da lista")
    p_lista.add_argument("--slug", help="Slug curto opcional")

    # Comando VERTICAL (FOCO NA FERRAMENTA)
    p_vert = subparsers.add_parser("vertical", help="Gera um DOSSIÊ VERTICAL focado em 1 SaaS (vert-*.html)")
    p_vert.add_argument("arquivo", help="Caminho do arquivo JSON com o Quinteto Soberano e MCPs")
    p_vert.add_argument("--slug", help="Slug curto do SaaS em foco")

    # Comando AUDITAR
    subparsers.add_parser("auditar", help="Executa a suíte de todos os gates mecânicos")

    # Comando LIMPAR
    subparsers.add_parser("limpar", help="Higieniza entulhos e sincroniza espelhos")

    args = parser.parse_args()

    if args.comando == "lista":
        disparar_lista(args.arquivo, args.slug)
    elif args.comando == "vertical":
        disparar_vertical(args.arquivo, args.slug)
    elif args.comando == "auditar":
        os.system("python scripts/auditar_todas_camadas.py")
    elif args.comando == "limpar":
        os.system("python scripts/limpar_entulho.py")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
