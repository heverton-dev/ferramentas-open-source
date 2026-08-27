# -*- coding: utf-8 -*-
"""
CLI RUNNER UNIVERSAL · FLUXO 2: DOSSIÊS VERTICAIS & QUINTETO SOBERANO AIDD
Aciona a geração determinística tripartite do desmantelamento de SaaS (HTML, MD, PDF).
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

from gerar_dossie_vertical_tripartite import compilar_dossie_vertical_tripartite

def executar_fluxo2(saas: str = None) -> bool:
    print("\n" + "="*70)
    print("🚀 FLUXO 2 · DESMANTELAMENTO VERTICAL SAAS & QUINTETO SOBERANO AIDD")
    print("="*70)

    if not saas:
        print("\n💡 Informe o nome ou slug do SaaS proprietário a desmantelar.")
        print("   Exemplos: granola, notion, zapier, salesforce, figma")
        try:
            saas = input("   👉 Digite o slug do SaaS: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nOperação cancelada pelo usuário.")
            return False

    if not saas:
        saas = "granola"
        print(f"   ℹ️ Nenhum SaaS informado. Assumindo alvo canônico padrão: '{saas}'")

    print(f"\n⚙️ Disparando compilação tripartite para o SaaS: '{saas}'...")
    sucesso = compilar_dossie_vertical_tripartite(saas)

    if sucesso:
        print("\n" + "="*70)
        print(f"🏆 FLUXO 2 CONCLUÍDO COM SUCESSO PARA '{saas}'!")
        print("📁 Artefatos Tripartites Gerados em:")
        print(f"   - HTML Interativo: output/02-dossies-verticais/vert-{saas}/materiais/vert-{saas}.html")
        print(f"   - Markdown Limpo:  output/02-dossies-verticais/vert-{saas}/materiais/vert-{saas}.md")
        print(f"   - PDF Typst:       output/02-dossies-verticais/vert-{saas}/materiais/vert-{saas}.pdf")
        print(f"   - Relatórios:      output/02-dossies-verticais/vert-{saas}/relatorios/")
        print("="*70 + "\n")
        return True
    else:
        print(f"\n❌ Falha na execução do Fluxo 2 para '{saas}'. Verifique os logs acima.\n")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CLI Runner · Fluxo 2: Dossiês Verticais AIDD")
    parser.add_argument("--saas", "-s", type=str, default=None, help="Slug do SaaS proprietário (ex: granola)")
    args = parser.parse_args()

    ok = executar_fluxo2(args.saas)
    sys.exit(0 if ok else 1)
