# -*- coding: utf-8 -*-
"""
CLI RUNNER UNIVERSAL · FLUXO 3: ESTEIRA DE MANUAIS VPS & TRILHAS DE AULAS AIDD
Aciona a geração determinística tripartite de manuais com desinstalação cirúrgica e trilhas autoguiadas
com auditoria prévia de qualidade (Gate R9, G0/G1) e auto-atualização do Índice Mestre.
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
from validar_schemas_fluxos import auditar_e_bloquear
from popular_catalogo_mestre import executar_ingestao_completa
from gerar_indice_mestre_cruzado import compilar_indice_mestre_completo

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

    ferramenta_limpa = ferramenta.strip().replace("\ufeff", "").replace("manual-", "").replace(".json", "")
    saas_limpo = saas.strip().replace("\ufeff", "").replace("vert-", "")

    # Gate R9: Validação Prévia dos Schemas de Manual e Trilha
    json_manual = BASE_DIR / "scripts" / "data" / f"manual-{ferramenta_limpa}.json"
    json_trilha = BASE_DIR / "scripts" / "data" / f"trilha-{ferramenta_limpa}.json"

    if json_manual.exists():
        if not auditar_e_bloquear("manual_vps", json_manual):
            return False

    if json_trilha.exists():
        if not auditar_e_bloquear("trilha", json_trilha):
            return False

    print(f"\n🔍 [Gate G0/G1] Auditando fontes oficiais para '{ferramenta_limpa}'...")
    json_fontes = BASE_DIR / "scripts" / "data" / f"sumario-fontes-{ferramenta_limpa}.json"
    if json_fontes.exists():
        if not auditar_qualidade_sumario(json_fontes):
            return False
        if not auditar_fontes_veridicas(json_fontes):
            return False
    else:
        print(f"   ⚠️ [Gate G0/G1 NÃO EXECUTADO] Nenhum 'sumario-fontes-{ferramenta_limpa}.json' cadastrado.")
        print(f"      As URLs em 'referencias_bibliograficas' do manual NÃO foram verificadas por HTTP.")
        print(f"      Para habilitar o gate completo, crie 'scripts/data/sumario-fontes-{ferramenta_limpa}.json'")
        print(f"      com tópicos e trechos técnicos reais por fonte (Padrão Diamante G0).")

    print(f"\n⚙️ 1/2 Compilando Manual Operacional VPS (com Desinstalação Cirúrgica)...")
    ok_manual = compilar_manual(ferramenta_limpa)

    print(f"\n⚙️ 2/2 Compilando Trilha de Aprendizado de 5 Aulas...")
    ok_trilha = compilar_trilha(ferramenta_limpa)

    if ok_manual and ok_trilha:
        pasta_base = f"output/03-manuais-e-trilhas/{saas_limpo}/{ferramenta_limpa}"
        print("\n" + "="*70)
        print(f"🏆 FLUXO 3 CONCLUÍDO COM SUCESSO PARA '{ferramenta_limpa}' ({saas_limpo})!")
        print("📁 Artefatos Gerados em:")
        print(f"   - Manual VPS (HTML/MD/PDF):  {pasta_base}/manuais/")
        print(f"   - Trilha 5 Aulas (HTML/MD/PDF): {pasta_base}/trilhas/")

        # Auto-Sincronização do Índice Mestre
        print("\n🔄 [Auto-Sincronização R11] Atualizando Catálogo Mestre e Portal Interativo...")
        try:
            executar_ingestao_completa()
            compilar_indice_mestre_completo()
            print("   ✅ Portal INDICE-MESTRE.html sincronizado com sucesso!")
        except Exception as e:
            print(f"   ⚠️ Aviso na sincronização do Índice Mestre: {e}")

        # Sincronização Git Automatizada (Regra R16)
        from git_sync import executar_commit_e_push
        executar_commit_e_push(f"feat(fluxo3): compilar manual vps e trilha {ferramenta_limpa} ({saas_limpo})")

        print("="*70 + "\n")
        return True
    else:
        print(f"\n❌ Falha na compilação do Fluxo 3 para '{ferramenta_limpa}'.\n")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CLI Runner · Fluxo 3: Manuais VPS & Trilhas AIDD")
    parser.add_argument("--ferramenta", "-f", type=str, default=None, help="Slug da ferramenta (ex: screenpipe)")
    parser.add_argument("--saas", "-s", type=str, default="granola", help="SaaS substituído (default: granola)")
    args = parser.parse_args()

    ok = executar_fluxo3(args.ferramenta, args.saas)
    sys.exit(0 if ok else 1)
