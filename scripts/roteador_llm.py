# -*- coding: utf-8 -*-
"""
ROTEADOR SEMÂNTICO & MATRIZ DE TIERS DE LLM (CAMADA 3)
Define a política de despacho inteligente de modelos por complexidade, custo e latência.
Aplica o Princípio do Roteamento por Pareto: 80% das tarefas mecânicas em Tier 1 (barato),
20% das tarefas de alta cognição em Tier 2/3 (forte).
"""
import sys

def console_utf8():
    if sys.platform == "win32":
        try:
            sys.stdout.reconfigure(encoding="utf-8")
            sys.stderr.reconfigure(encoding="utf-8")
        except Exception:
            pass

console_utf8()

TIERS_LLM = {
    "tier_1_rapido": {
        "descricao": "Modelos ultra-rápidos e econômicos para tarefas mecânicas e leitura.",
        "modelos_recomendados": ["gemini-2.5-flash", "claude-3-5-haiku", "gpt-4o-mini"],
        "casos_de_uso": [
            "pesquisa_grep",
            "leitura_arquivos",
            "validacao_sintatica",
            "listagem_diretorios",
            "extracao_metadados"
        ],
        "temperatura": 0.0,
        "max_tokens_saida": 2048,
        "custo_relativo": "1x (Base)"
    },
    "tier_2_codigo": {
        "descricao": "Modelos equilibrados de alta precisão para engenharia de software e testes.",
        "modelos_recomendados": ["claude-3-7-sonnet", "gpt-4o", "gemini-2.5-pro"],
        "casos_de_uso": [
            "geracao_codigo",
            "edicao_arquivos",
            "criacao_testes",
            "formatacao_dossie",
            "refatoracao_local"
        ],
        "temperatura": 0.2,
        "max_tokens_saida": 4096,
        "custo_relativo": "10x"
    },
    "tier_3_raciocinio": {
        "descricao": "Modelos de raciocínio profundo para arquitetura, resolução de bugs e governança.",
        "modelos_recomendados": ["claude-3-7-sonnet-thought", "o3-mini-high", "gemini-2.5-pro-thinking"],
        "casos_de_uso": [
            "decisao_arquitetura",
            "depuracao_bugs_complexos",
            "auditoria_seguranca",
            "analise_impacto_multi_modulo"
        ],
        "temperatura": 0.1,
        "max_tokens_saida": 8192,
        "custo_relativo": "30x"
    }
}

POLITICA_FALLBACK = {
    "primaria_falhou_429": "Chavear automaticamente para modelo equivalente do provedor B.",
    "timeout_30s": "Chavear para modelo do Tier 1 com prompt condensado.",
    "erro_validacao_schema": "Reexecutar 1x com prompt corretivo injetando o JSON Schema do erro."
}

def obter_tier_para_tarefa(tipo_tarefa: str) -> dict:
    for tier_nome, config in TIERS_LLM.items():
        if tipo_tarefa in config["casos_de_uso"]:
            return {"tier": tier_nome, "config": config}
    return {"tier": "tier_2_codigo", "config": TIERS_LLM["tier_2_codigo"]}

if __name__ == "__main__":
    print("=" * 80)
    print(" 🧠 MATRIZ DE TIERS & ROTEAMENTO SEMÂNTICO DE LLM (CAMADA 3)")
    print("=" * 80)
    for t_nome, t_data in TIERS_LLM.items():
        print(f"\n [{t_nome.upper()}] Custo: {t_data['custo_relativo']}")
        print(f"  -> Modelos: {', '.join(t_data['modelos_recomendados'])}")
        print(f"  -> Usos: {', '.join(t_data['casos_de_uso'])}")
    print("\n" + "=" * 80)
