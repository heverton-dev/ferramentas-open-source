# -*- coding: utf-8 -*-
"""
CLI RUNNER UNIVERSAL · FLUXO 3: ESTEIRA DE MANUAIS VPS & TRILHAS DE AULAS AIDD
Aciona a geração determinística tripartite de manuais com desinstalação cirúrgica e trilhas autoguiadas.
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

from gerar_manual_operacional import compilar_manual
from gerar_trilha_aprendizado import compilar_trilha
from auditar_qualidade_fontes import auditar_qualidade_sumario
from auditar_fontes_veridicas import auditar_sumario as auditar_fontes_veridicas

def executar_fluxo3(ferramenta: str = None, saas: str = "granola") -> bool:
    print("\n" + "="*70)
    print("🚀 FLUXO 3 · ESTEIRA DE ENGENHARIA, MANUAIS VPS & TRILHAS AIDD")
    print("="*70)

    if not ferramenta:
        print("\n💡 Informe a ferramenta open source para deploy na VPS.")
        print("   Exemplos disponíveis: screenpipe, whisperx, open-notebooklm, whisper-cpp, faster-whisper-cli")
        try:
            ferramenta = input("   👉 Digite o slug da ferramenta: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nOperação cancelada pelo usuário.")
            return False

    if not ferramenta:
        ferramenta = "screenpipe"
        print(f"   ℹ️ Nenhuma ferramenta informada. Assumindo padrão: '{ferramenta}'")

    print(f"\n🔍 [Gate G0/G1] Auditando fontes oficiais para '{ferramenta}'...")
    json_fontes = BASE_DIR / "scripts" / "data" / f"sumario-fontes-{ferramenta}.json"
    if json_fontes.exists():
        auditar_qualidade_sumario(json_fontes)
        auditar_fontes_veridicas(json_fontes)

    print(f"\n⚙️ 1/2 Compilando Manual Operacional VPS (com Desinstalação Cirúrgica)...")
    ok_manual = compilar_manual(ferramenta)

    print(f"\n⚙️ 2/2 Compilando Trilha de Aprendizado de 5 Aulas...")
    ok_trilha = compilar_trilha(ferramenta)

    if ok_manual and ok_trilha:
        pasta_base = f"output/03-manuais-e-trilhas/{saas}/{ferramenta}"
        print("\n" + "="*70)
        print(f"🏆 FLUXO 3 CONCLUÍDO COM SUCESSO PARA '{ferramenta}' ({saas})!")
        print("📁 Artefatos Gerados em:")
        print(f"   - Manual VPS (HTML/MD/PDF):  {pasta_base}/manuais/")
        print(f"   - Trilha 5 Aulas (HTML/MD/PDF): {pasta_base}/trilhas/")
        print("="*70 + "\n")
        return True
    else:
        print(f"\n❌ Falha na compilação do Fluxo 3 para '{ferramenta}'.\n")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CLI Runner · Fluxo 3: Manuais VPS & Trilhas AIDD")
    parser.add_argument("--ferramenta", "-f", type=str, default=None, help="Slug da ferramenta (ex: screenpipe)")
    parser.add_argument("--saas", "-s", type=str, default="granola", help="SaaS substituído (default: granola)")
    args = parser.parse_args()

    ok = executar_fluxo3(args.ferramenta, args.saas)
    sys.exit(0 if ok else 1)
