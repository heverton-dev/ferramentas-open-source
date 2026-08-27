# -*- coding: utf-8 -*-
"""
GATE MECÂNICO G2: AUDITOR DE CITAÇÕES E REFERÊNCIAS CRUZADAS (R9 / R17)
Garante integridade referencial estrita entre o Manual Operacional e o Sumário JSON:
1. Toda afirmação técnica ou comando que possui [Fxx] DEVE existir no sumário JSON.
2. Todas as fontes declaradas no sumário DEVEM ser citadas no manual.
3. Se houver citação alucinada ou órfã, o gate barra a esteira (exit 1).
"""
import sys
import json
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

def auditar_citacoes(slug: str) -> bool:
    manual_file = BASE_DIR / "scripts" / "data" / f"manual-{slug}.json"
    sumario_file = BASE_DIR / "scripts" / "data" / f"sumario-fontes-{slug}.json"

    if not manual_file.exists():
        print(f"❌ Erro: {manual_file} não encontrado.")
        return False
    if not sumario_file.exists():
        print(f"❌ Erro: {sumario_file} não encontrado.")
        return False

    with open(manual_file, "r", encoding="utf-8") as f:
        manual = json.load(f)
    with open(sumario_file, "r", encoding="utf-8") as f:
        sumario = json.load(f)

    # Coleta IDs do sumário
    ids_sumario = {fonte["id"] for fonte in sumario.get("fontes", [])}
    print(f"\n🔍 [Gate G2] Auditando Citações Cruzadas para '{slug}'...")
    print(f"   -> IDs de fontes disponíveis no Sumário: {sorted(list(ids_sumario))}")

    # Coleta citações feitas no manual
    citacoes_feitas = set()

    for p in manual.get("instalacao_producao", {}).get("passos", []):
        f_id = p.get("fonte_id")
        if f_id:
            citacoes_feitas.add(f_id)

    for c in manual.get("manual_uso_exaustivo", {}).get("comandos_cli", []):
        f_id = c.get("fonte_id")
        if f_id:
            citacoes_feitas.add(f_id)

    for a in manual.get("manual_uso_exaustivo", {}).get("rotas_api", []):
        f_id = a.get("fonte_id")
        if f_id:
            citacoes_feitas.add(f_id)

    print(f"   -> Citações ativas encontradas no Manual: {sorted(list(citacoes_feitas))}")

    # Validação 1: Citações alucinadas (que não existem no sumário)
    alucinadas = citacoes_feitas - ids_sumario
    if alucinadas:
        print(f"❌ REPROVADO: Citações alucinadas encontradas: {alucinadas}. Elas não constam no sumário!")
        return False

    # Validação 2: Fontes órfãs (que estão no sumário mas não foram citadas)
    orfas = ids_sumario - citacoes_feitas
    if orfas:
        print(f"❌ REPROVADO: Fontes órfãs encontradas: {orfas}. Toda fonte do sumário deve ser aproveitada!")
        return False

    # Validação 3: Tabela de bibliografia do manual bate 100% com o sumário
    ids_bibliografia = {r["id"] for r in manual.get("referencias_bibliograficas", [])}
    if ids_bibliografia != ids_sumario:
        print(f"❌ REPROVADO: Tabela de bibliografia ({ids_bibliografia}) difere do sumário ({ids_sumario})!")
        return False

    print(f"✅ APROVADO: 100% das {len(citacoes_feitas)} fontes foram citadas sem alucinação e com correspondência biunívoca.\n")
    return True

if __name__ == "__main__":
    slug_alvo = sys.argv[1] if len(sys.argv) > 1 else "screenpipe"
    sucesso = auditar_citacoes(slug_alvo)
    sys.exit(0 if sucesso else 1)
