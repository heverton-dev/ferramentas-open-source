# -*- coding: utf-8 -*-
"""
ORQUESTRADOR MESTRE DA ESTEIRA DE MANUAIS OPERACIONAIS E TRILHAS (AI DRIVEN)
Ponto de entrada unificado para execução interativa ou em lote:
- Modo Cirúrgico: Menu interativo com as 5 ferramentas do Quinteto Soberano.
- Modo Quinteto Completo: Processamento em lote das 5 ferramentas.
- Zero download pesado: 100% dos dados textuais consumidos em memória.
- Gates G1 (HTTP 200) e G2 (Citações) mecânicos garantindo zero alucinação.
"""
import sys
import json
import argparse
from pathlib import Path
from coletar_fontes_pesquisa import coletar_fontes_para_ferramenta
from compilar_sumario_fontes import indexar_trechos_por_topico
from auditar_qualidade_fontes import auditar_qualidade_sumario
from auditar_fontes_veridicas import auditar_sumario
from auditar_citacoes_manuais import auditar_citacoes
from gerar_manual_operacional import compilar_manual
from gerar_trilha_aprendizado import compilar_trilha

def console_utf8():
    if sys.platform == "win32":
        try:
            sys.stdout.reconfigure(encoding="utf-8")
            sys.stderr.reconfigure(encoding="utf-8")
        except Exception:
            pass

console_utf8()

BASE_DIR = Path(__file__).resolve().parent.parent

def carregar_quinteto_saas(saas: str) -> list[dict]:
    """Carrega as 5 ferramentas do dossiê vertical do SaaS."""
    caminho = BASE_DIR / "scripts" / "data" / f"dossie-vertical-{saas}.json"
    if not caminho.exists():
        # Tenta com vert-
        caminho_alt = BASE_DIR / "scripts" / "data" / f"dossie-vertical-{saas.replace('vert-', '')}.json"
        if caminho_alt.exists():
            caminho = caminho_alt
        else:
            raise FileNotFoundError(f"Dossiê do SaaS '{saas}' não encontrado em scripts/data/.")

    with open(caminho, "r", encoding="utf-8") as f:
        dados = json.load(f)

    return dados.get("quinteto", [])

def executar_pipeline_ferramenta(slug: str, saas: str) -> bool:
    """Executa o pipeline completo para uma única ferramenta."""
    print(f"\n" + "="*70)
    print(f"🚀 INICIANDO ESTEIRA PARA: {slug.upper()} (SaaS Origem: {saas.upper()})")
    print("="*70)

    # 1. Coleta Leve (Zero Download Pesado)
    coletar_fontes_para_ferramenta(slug, saas)

    # 2. Compilação do Sumário JSON
    sumario_path = BASE_DIR / "scripts" / "data" / f"sumario-fontes-{slug}.json"
    indexar_trechos_por_topico(sumario_path)

    # 3. Gate G0: Auditoria de Qualidade & Critérios de Admissão
    g0_ok = auditar_qualidade_sumario(sumario_path)
    if not g0_ok:
        print(f"❌ Abortando esteira para '{slug}': Falha no Gate G0 de qualidade das fontes.")
        return False

    # 4. Gate G1: Auditoria HTTP 200 de Fontes
    g1_ok = auditar_sumario(sumario_path)
    if not g1_ok:
        print(f"❌ Abortando esteira para '{slug}': Falha no Gate G1 de fontes.")
        return False

    # 5. Geração do Manual Operacional (HTML, MD e PDF via Typst)
    manual_ok = compilar_manual(slug)
    if not manual_ok:
        print(f"❌ Abortando esteira para '{slug}': Falha na geração do manual.")
        return False

    # 5. Gate G2: Auditoria de Citações Cruzadas
    g2_ok = auditar_citacoes(slug)
    if not g2_ok:
        print(f"❌ Abortando esteira para '{slug}': Falha no Gate G2 de citações.")
        return False

    # 6. Geração da Trilha de Aprendizado (HTML, MD e PDF via Typst)
    trilha_ok = compilar_trilha(slug)
    if not trilha_ok:
        print(f"❌ Abortando esteira para '{slug}': Falha na geração da trilha.")
        return False

    print(f"\n🎉 SUCESSO TOTAL: Esteira concluída com 100% de conformidade para '{slug}'.")
    return True

def menu_interativo(saas: str) -> list[str]:
    """Exibe o menu interativo no terminal com as 5 ferramentas do quinteto."""
    quinteto = carregar_quinteto_saas(saas)
    if not quinteto:
        print(f"❌ Nenhuma ferramenta encontrada no dossiê de {saas}.")
        return []

    print("\n" + "#"*65)
    print(f"🎯 DOSSIÊ SELECIONADO: {saas.upper()} (QUINTETO SOBERANO)")
    print("#"*65)

    for f in quinteto:
        rank = f.get("rank", "?")
        classif = f.get("classificacao", "Solução Open Source")
        nome = f.get("nome", f.get("slug", "Ferramenta"))
        print(f"  [{rank}] {nome} ({classif})")

    print(f"  [T] TODAS AS 5 FERRAMENTAS (Execução em lote do Quinteto Completo)")
    print(f"  [S] Sair")
    print("-" * 65)

    escolha = input("Selecione a opção desejada [1-5, T ou S]: ").strip().upper()

    if escolha == "S":
        print("Operação cancelada pelo usuário.")
        return []
    if escolha == "T":
        return [f.get("slug") for f in quinteto if f.get("slug")]
    
    try:
        idx = int(escolha)
        for f in quinteto:
            if f.get("rank") == idx and f.get("slug"):
                return [f.get("slug")]
        print(f"❌ Opção {escolha} inválida.")
        return []
    except ValueError:
        print(f"❌ Opção {escolha} não reconhecida.")
        return []

def main():
    parser = argparse.ArgumentParser(description="Orquestrador da Esteira de Manuais e Trilhas (Fábrica Universal)")
    parser.add_argument("--saas", default="granola", help="Slug do SaaS de origem (ex: granola)")
    parser.add_argument("--ferramenta", help="Slug da ferramenta específica (ex: screenpipe)")
    parser.add_argument("--modo", choices=["cirurgico", "todas"], help="Modo de execução (cirurgico ou todas)")

    args = parser.parse_args()

    # Modo não-interativo por flag de ferramenta
    if args.ferramenta:
        alvos = [args.ferramenta]
    elif args.modo == "todas":
        quinteto = carregar_quinteto_saas(args.saas)
        alvos = [f.get("slug") for f in quinteto if f.get("slug")]
    else:
        # Modo interativo com prompt
        alvos = menu_interativo(args.saas)

    if not alvos:
        sys.exit(0)

    print(f"\n📋 Ferramentas a processar nesta sessão: {alvos}")
    erros = 0
    for alvo in alvos:
        sucesso = executar_pipeline_ferramenta(alvo, args.saas)
        if not sucesso:
            erros += 1

    if erros > 0:
        print(f"\n❌ A esteira finalizou com {erros} erro(s). Verifique os logs acima.")
        sys.exit(1)
    else:
        print(f"\n🏆 Esteira finalizada com sucesso! Todos os artefatos compilados e auditados.")
        sys.exit(0)

if __name__ == "__main__":
    main()
