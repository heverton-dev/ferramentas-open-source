# -*- coding: utf-8 -*-
"""
CLI RUNNER UNIVERSAL · FLUXO 1: LISTAS HORIZONTAIS AIDD
Aciona a geração determinística tripartite de compêndios temáticos (HTML, MD, PDF).
Suporta argumentos de linha de comando ou prompt interativo.
"""
import sys
import argparse
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR / "scripts"))

def console_utf8():
    if sys.platform == "win32":
        try:
            sys.stdout.reconfigure(encoding="utf-8")
            sys.stderr.reconfigure(encoding="utf-8")
        except Exception:
            pass

console_utf8()

from compilar_lista_horizontal_tripartite import compilar_lista_horizontal_tripartite as compilar_nova_lista
from gerar_lista_horizontal_tripartite import compilar_lista_horizontal_tripartite as compilar_lista_legada

def compilar_lista_tripartite(slug: str) -> bool:
    slug_limpo = slug.replace("list-", "").replace(".html", "").replace(".json", "")
    json_path = BASE_DIR / "scripts" / "data" / f"lista-{slug_limpo}.json"
    if json_path.exists():
        return compilar_nova_lista(slug_limpo)
    return compilar_lista_legada(slug_limpo)

def executar_fluxo1(slug: str = None) -> bool:
    print("\n" + "="*70)
    print("🚀 FLUXO 1 · FÁBRICA UNIVERSAL DE LISTAS HORIZONTAIS AIDD")
    print("="*70)

    if not slug:
        print("\n💡 Informe o slug da camada temática desejada.")
        print("   Exemplos: bancos-dados-estado, observabilidade-telemetria, ia-llm-local")
        try:
            slug = input("   👉 Digite o slug da camada: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nOperação cancelada pelo usuário.")
            return False

    if not slug:
        slug = "bancos-dados-estado"
        print(f"   ℹ️ Nenhum slug informado. Assumindo camada canônica padrão: '{slug}'")

    print(f"\n⚙️ Disparando compilação tripartite para a camada: '{slug}'...")
    sucesso = compilar_lista_tripartite(slug)

    if sucesso:
        print("\n" + "="*70)
        print(f"🏆 FLUXO 1 CONCLUÍDO COM SUCESSO PARA '{slug}'!")
        print("📁 Artefatos Tripartites Gerados em:")
        print(f"   - HTML Interativo: output/01-listas-horizontais/list-{slug}/list-{slug}.html")
        print(f"   - Markdown Limpo:  output/01-listas-horizontais/list-{slug}/list-{slug}.md")
        print(f"   - PDF Typst:       output/01-listas-horizontais/list-{slug}/list-{slug}.pdf")
        print("="*70 + "\n")
        return True
    else:
        print(f"\n❌ Falha na execução do Fluxo 1 para '{slug}'. Verifique os logs acima.\n")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CLI Runner · Fluxo 1: Listas Horizontais AIDD")
    parser.add_argument("--slug", "-s", type=str, default=None, help="Slug temático da camada (ex: bancos-dados-estado)")
    args = parser.parse_args()

    ok = executar_fluxo1(args.slug)
    sys.exit(0 if ok else 1)
