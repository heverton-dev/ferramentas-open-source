# -*- coding: utf-8 -*-
"""
CLI RUNNER UNIVERSAL · PIPELINE CORE AIDD (FLUXO 1 -> 2 -> 3)
Orquestra o Pipeline Core em cascata com os 3 Gates de Interação Humano-no-Loop.
Ao final, oferece continuação opcional e acionável para os Fluxos 4 (Macro-Ecossistemas)
e 5 (Auditoria VPS), que permanecem independentes e podem também ser disparados
separadamente via `run_fluxo4.py` / `run_fluxo5.py` ou `/fluxo4` / `/fluxo5`.
"""
import sys
import subprocess
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

from run_fluxo1 import executar_fluxo1
from run_fluxo2 import executar_fluxo2
from run_fluxo3 import executar_fluxo3
from gerar_relatorio_operacao_fluxos import compilar_relatorio

def executar_fluxo_total(camada: str = None, saas: str = None, ferramenta: str = None, interativo: bool = True) -> bool:
    print("\n" + "#"*75)
    print("🌐 PIPELINE CORE AIDD · FÁBRICA UNIVERSAL OPEN SOURCE")
    print("   Execução encadeada dos Fluxos 1 -> 2 -> 3 com Gates de Interação")
    print("   (Fluxos 4 e 5 são independentes; oferecidos como continuação opcional ao final)")
    print("#"*75 + "\n")

    # =========================================================================
    # ETAPA 1 · FLUXO 1: LISTAS HORIZONTAIS TEMÁTICAS
    # =========================================================================
    print("🔹 [ETAPA 1/3] Disparando Fluxo 1: Lista Horizontal Temática...")
    if not camada and interativo:
        print("💡 Informe a camada tecnológica inicial (padrão: 'bancos-dados-estado')")
        try:
            camada = input("   👉 Camada: ").strip() or "bancos-dados-estado"
        except (KeyboardInterrupt, EOFError):
            print("\nOperação cancelada.")
            return False
    elif not camada:
        camada = "bancos-dados-estado"

    ok1 = executar_fluxo1(camada)
    if not ok1:
        print("❌ Pipeline abortado devido a falha no Fluxo 1.")
        return False

    # 🛑 GATE 1 DE INTERAÇÃO HUMANO-NO-LOOP
    print("\n" + "-"*75)
    print("🛑 [GATE 1 DE INTERAÇÃO HUMANO-NO-LOOP · SELEÇÃO DE SAAS]")
    print(f"   A lista horizontal '{camada}' foi compilada com sucesso.")
    if interativo:
        print("   Qual SaaS proprietário você deseja desmantelar agora com o Quinteto Soberano?")
        try:
            saas = input(f"   👉 Digite o SaaS [padrão: 'granola']: ").strip() or "granola"
        except (KeyboardInterrupt, EOFError):
            print("\nPipeline interrompido pelo usuário.")
            return False
    elif not saas:
        saas = "granola"
    print(f"   ✅ SaaS alvo confirmado para o Fluxo 2: '{saas}'")
    print("-"*75 + "\n")

    # =========================================================================
    # ETAPA 2 · FLUXO 2: DOSSIÊ VERTICAL & QUINTETO SOBERANO
    # =========================================================================
    print(f"🔹 [ETAPA 2/3] Disparando Fluxo 2: Dossiê Vertical para '{saas}'...")
    ok2 = executar_fluxo2(saas)
    if not ok2:
        print("❌ Pipeline abortado devido a falha no Fluxo 2.")
        return False

    # 🛑 GATE 2 DE INTERAÇÃO HUMANO-NO-LOOP
    print("\n" + "-"*75)
    print("🛑 [GATE 2 DE INTERAÇÃO HUMANO-NO-LOOP · SELEÇÃO DA FERRAMENTA]")
    print(f"   O Dossiê Vertical de '{saas}' elegeu o Quinteto Soberano.")
    if interativo:
        print("   Qual das ferramentas do Quinteto você quer colocar em produção na VPS?")
        print("   Opções: screenpipe, whisperx, open-notebooklm, whisper-cpp, faster-whisper-cli")
        try:
            ferramenta = input(f"   👉 Digite a ferramenta [padrão: 'screenpipe']: ").strip() or "screenpipe"
        except (KeyboardInterrupt, EOFError):
            print("\nPipeline interrompido pelo usuário.")
            return False
    elif not ferramenta:
        ferramenta = "screenpipe"
    print(f"   ✅ Ferramenta confirmada para o Fluxo 3: '{ferramenta}'")
    print("-"*75 + "\n")

    # =========================================================================
    # ETAPA 3 · FLUXO 3: MANUAL VPS (DESINSTALAÇÃO SEGURA) & TRILHA
    # =========================================================================
    print(f"🔹 [ETAPA 3/3] Disparando Fluxo 3: Manual VPS & Trilha para '{ferramenta}'...")
    ok3 = executar_fluxo3(ferramenta, saas)
    if not ok3:
        print("❌ Pipeline abortado devido a falha no Fluxo 3.")
        return False

    # 🛑 GATE 3 DE APROVAÇÃO FINAL & RELATÓRIO
    print("\n" + "="*75)
    print("🏆 PIPELINE CORE (FLUXOS 1 -> 2 -> 3) EXECUTADO COM 100% DE SUCESSO!")
    print("="*75)
    print("📊 Resumo de Entregas da Fábrica Universal:")
    print(f"   1. [Fluxo 1] output/01-listas-horizontais/list-{camada}/")
    print(f"   2. [Fluxo 2] output/02-dossies-verticais/vert-{saas}/")
    print(f"   3. [Fluxo 3] output/03-manuais-e-trilhas/{saas}/{ferramenta}/")
    print(f"   4. [Relatório] output/relatorios/ (Tripartite consolidado)")

    # Atualizar Catálogo Mestre & Portal Interativo
    try:
        from popular_catalogo_mestre import executar_ingestao_completa
        from gerar_indice_mestre_cruzado import compilar_indice_mestre_completo
        executar_ingestao_completa()
        compilar_indice_mestre_completo()
        print("   5. [Portal Mestre] output/INDICE-MESTRE.html (Catálogo Rastreável)")
    except Exception as e:
        print(f"   ⚠️ Aviso: Falha ao atualizar Índice Mestre: {e}")

    # Sincronização Git Automatizada (Regra R16)
    from git_sync import executar_commit_e_push
    executar_commit_e_push(f"feat(pipeline-total): execucao completa AIDD ({camada} -> {saas} -> {ferramenta})")

    print("="*75 + "\n")

    # =========================================================================
    # CONTINUAÇÃO OPCIONAL E ACIONÁVEL · FLUXOS 4 (MACRO-ECOSSISTEMAS) E 5 (AUDITORIA VPS)
    # =========================================================================
    print("-"*75)
    print("➡️  CONTINUAÇÃO OPCIONAL: Fluxos 4 e 5 são independentes do Pipeline Core.")
    print("    Podem ser acionados agora mesmo, ou depois via '/fluxo4' e '/fluxo5'.")
    print("-"*75)

    if interativo:
        try:
            rodar_f4 = input("   👉 Deseja acionar o Fluxo 4 (Macro-Ecossistemas) agora? [s/N]: ").strip().lower()
        except (KeyboardInterrupt, EOFError):
            rodar_f4 = "n"
        if rodar_f4 == "s":
            try:
                slug_ecos = input("      Slug do macro-ecossistema (ex: rd-station-suite): ").strip()
            except (KeyboardInterrupt, EOFError):
                slug_ecos = None
            if slug_ecos:
                from run_fluxo4 import executar_fluxo4
                executar_fluxo4(slug_ecos)

        try:
            rodar_f5 = input("   👉 Deseja acionar o Fluxo 5 (Auditoria VPS) agora? [s/N]: ").strip().lower()
        except (KeyboardInterrupt, EOFError):
            rodar_f5 = "n"
        if rodar_f5 == "s":
            try:
                alvo_vps = input("      Slug da ferramenta ou ecossistema a auditar (ex: stalwart, ecos-google-workspace): ").strip()
            except (KeyboardInterrupt, EOFError):
                alvo_vps = None
            if alvo_vps:
                flag = "--ecossistema" if alvo_vps.startswith("ecos-") else "--ferramenta"
                subprocess.run([sys.executable, str(BASE_DIR / "scripts" / "run_fluxo5.py"), flag, alvo_vps])
    else:
        print("   ℹ️ Modo não-interativo: Fluxos 4 e 5 não foram acionados automaticamente.")
        print("      Execute manualmente: python scripts/run_fluxo4.py --ecossistema <slug>")
        print("      Execute manualmente: python scripts/run_fluxo5.py --ferramenta <slug>")

    print("="*75 + "\n")
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CLI Runner · Pipeline Core AIDD (Fluxos 1 -> 2 -> 3, com continuação opcional para os Fluxos 4 e 5)")
    parser.add_argument("--camada", "-c", type=str, default=None, help="Slug da camada temática inicial")
    parser.add_argument("--saas", "-s", type=str, default=None, help="Slug do SaaS proprietário")
    parser.add_argument("--ferramenta", "-f", type=str, default=None, help="Slug da ferramenta do Quinteto")
    parser.add_argument("--nao-interativo", action="store_true", help="Roda sem pausas com valores padrão")
    args = parser.parse_args()

    ok = executar_fluxo_total(args.camada, args.saas, args.ferramenta, interativo=not args.nao_interativo)
    sys.exit(0 if ok else 1)
