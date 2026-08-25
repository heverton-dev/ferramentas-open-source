# -*- coding: utf-8 -*-
"""
REGISTRO DECLARATIVO DE TIPOS DE ARTEFATO (REGRA R12 & CAMADA 3 LLM)
Mapeia a natureza de cada artefato gerado na fábrica, seu custo relativo de LLM,
o script/produtor responsável e a suíte de gates mecânicos associada.
Adicionar um novo tipo custa exatamente 1 entrada neste dicionário.
"""

TIPOS = {
    "dossie_executivo_html": {
        "descricao": "Compêndio técnico completo no Padrão Diamante com 20 ferramentas e fichas técnicas.",
        "natureza": "geracao_editorial",
        "custo_llm": "medio",
        "tier_recomendado": "tier_2_codigo",
        "schema_saida": "scripts/schemas/schema_ferramenta.json",
        "produtor": "scripts/padroes/template_dossie_executivo.py",
        "gates": ["scripts/auditar_r5_dossie.py", "scripts/auditar_higiene_repo.py"]
    },
    "relatorio_sessao_md": {
        "descricao": "Relatório executivo e técnico de encerramento de sessão de desenvolvimento.",
        "natureza": "sintese_auditavel",
        "custo_llm": "baixo",
        "tier_recomendado": "tier_1_rapido",
        "schema_saida": "scripts/schemas/schema_relatorio.json",
        "produtor": "scripts/relatorio_sessao.py",
        "gates": ["scripts/auditar_camada_tela.py"]
    },
    "sincronizacao_espelhos": {
        "descricao": "Auto-saneamento e espelhamento de saída para documentação pública.",
        "natureza": "extracao_deterministica",
        "custo_llm": "zero",
        "tier_recomendado": None,
        "schema_saida": None,
        "produtor": "scripts/limpar_entulho.py",
        "gates": ["scripts/auditar_higiene_repo.py"]
    },
    "auditoria_higiene_repo": {
        "descricao": "Auditoria de integridade de hash MD5 e ausência de entulho temporário (R18).",
        "natureza": "validacao_criptografica",
        "custo_llm": "zero",
        "tier_recomendado": None,
        "schema_saida": None,
        "produtor": "scripts/auditar_higiene_repo.py",
        "gates": []
    }
}
