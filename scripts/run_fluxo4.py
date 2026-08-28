# -*- coding: utf-8 -*-
"""
CLI RUNNER UNIVERSAL · FLUXO 4: MACRO-ECOSSISTEMAS SAAS AIDD
Aciona a geração determinística tripartite de dossiês de ecossistemas (HTML, MD, PDF)
com auditoria prévia de qualidade (Gate R9) e auto-atualização do Índice Mestre.
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

from compilar_ecossistema_tripartite import compilar_ecossistema_tripartite
from validar_schemas_fluxos import auditar_e_bloquear
from popular_catalogo_mestre import executar_ingestao_completa
from gerar_indice_mestre_cruzado import compilar_indice_mestre_completo

def executar_fluxo4(slug: str = None) -> bool:
    print("\n" + "="*70)
    print("🚀 FLUXO 4 · FÁBRICA UNIVERSAL DE MACRO-ECOSSISTEMAS SAAS AIDD")
    print("="*70)

    if not slug:
        print("\n💡 Informe o slug do macro-ecossistema desejado.")
        print("   Exemplos: rd-station-suite, google-workspace-suite, zoho-one-suite")
        try:
            slug = input("   👉 Digite o slug do ecossistema: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nOperação cancelada pelo usuário.")
            return False

    if not slug:
        slug = "rd-station-suite"
        print(f"   ℹ️ Nenhum slug informado. Assumindo ecossistema padrão: '{slug}'")

    slug_sanitizado = slug.strip().replace("\ufeff", "").replace("ecos-", "").replace(".json", "")
    json_path = BASE_DIR / "scripts" / "data" / f"ecos-{slug_sanitizado}.json"

    if not json_path.exists():
        print(f"\n❌ Arquivo de dados não encontrado: {json_path}")
        print(f"👉 Crie o arquivo 'scripts/data/ecos-{slug_sanitizado}.json' antes de rodar a compilação.\n")
        return False

    # Gate R9: Validação Estrita de Qualidade do Schema
    if not auditar_e_bloquear("fluxo4", json_path):
        return False

    print(f"\n⚙️ Disparando compilação tripartite para o ecossistema: '{slug_sanitizado}'...")
    sucesso = compilar_ecossistema_tripartite(slug_sanitizado)

    if sucesso:
        print("\n" + "="*70)
        print(f"🏆 FLUXO 4 CONCLUÍDO COM SUCESSO PARA '{slug_sanitizado}'!")
        print("📁 Artefatos da Suíte Modular Gerados em:")
        print(f"   - 📖 Livro Completo (HTML): output/04-ecossistemas/ecos-{slug_sanitizado}/00-livro-mestre-compilado/LIVRO-ECOSSISTEMA-COMPLETO.html")
        print(f"   - 📕 Livro Completo (PDF):  output/04-ecossistemas/ecos-{slug_sanitizado}/00-livro-mestre-compilado/LIVRO-ECOSSISTEMA-COMPLETO.pdf")
        print(f"   - 💼 Guias Executivos:     output/04-ecossistemas/ecos-{slug_sanitizado}/01-guias-executivos-e-estrategicos/")
        print(f"   - 🛠️ Guias de Engenharia:  output/04-ecossistemas/ecos-{slug_sanitizado}/02-guias-de-engenharia-e-infraestrutura/")
        print(f"   - ⚡ Guias de Operações:   output/04-ecossistemas/ecos-{slug_sanitizado}/03-guias-de-integracao-e-operacao/")
        print(f"   - 📦 Arsenal dos Pilares:  output/04-ecossistemas/ecos-{slug_sanitizado}/04-arsenal-dos-pilares/")
        
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
        executar_commit_e_push(f"feat(fluxo4): compilar macro-ecossistema ecos-{slug_sanitizado}")

        print("="*70 + "\n")
        return True
    else:
        print(f"\n❌ Falha na execução do Fluxo 4 para '{slug_sanitizado}'. Verifique os logs acima.\n")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CLI Runner · Fluxo 4: Macro-Ecossistemas SaaS AIDD")
    parser.add_argument("--ecossistema", "--slug", "-e", "-s", type=str, default=None, help="Slug do ecossistema (ex: rd-station-suite)")
    args = parser.parse_args()

    ok = executar_fluxo4(args.ecossistema)
    sys.exit(0 if ok else 1)
