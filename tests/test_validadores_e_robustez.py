# -*- coding: utf-8 -*-
"""
TESTES UNITÁRIOS · VALIDORES DE QUALIDADE E ROBUSTEZ DA ESTEIRA AIDD (REGRA R9 & R16)
Verifica se os linters mecânicos de schema bloqueiam JSONs rasos/incompletos e
aprovam apenas dados com rigor técnico no Padrão Diamante.
"""
import pytest
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
import sys
sys.path.insert(0, str(BASE_DIR / "scripts"))

from validar_schemas_fluxos import (
    validar_lista_horizontal,
    validar_dossie_vertical,
    validar_manual_operacional,
    validar_trilha_aprendizado,
    carregar_json_seguro
)

class TestValidadoresERobustez:
    def test_01_validar_lista_horizontal_valida(self):
        json_path = BASE_DIR / "scripts" / "data" / "lista-sintese-voz-tts.json"
        assert json_path.exists()
        dados = carregar_json_seguro(json_path)
        valido, erros = validar_lista_horizontal(dados)
        assert valido is True, f"Erros na lista horizontal: {erros}"
        assert len(erros) == 0

    def test_02_validar_lista_horizontal_rejeita_incompleta(self):
        dados_incompletos = {
            "slug": "lista-teste",
            "titulo": "Lista Incompleta",
            "ferramentas": [{"nome": "Tool A"}] # Menos de 5 e sem campos essenciais
        }
        valido, erros = validar_lista_horizontal(dados_incompletos)
        assert valido is False
        assert len(erros) > 0

    def test_03_validar_dossie_vertical_quinteto_completo(self):
        json_path = BASE_DIR / "scripts" / "data" / "dossie-vertical-elevenlabs.json"
        assert json_path.exists()
        dados = carregar_json_seguro(json_path)
        valido, erros = validar_dossie_vertical(dados)
        assert valido is True, f"Erros no dossiê vertical: {erros}"
        assert len(erros) == 0

    def test_04_validar_dossie_vertical_rejeita_sem_5_classificacoes(self):
        dados_incompletos = {
            "titulo": "Dossiê Falho",
            "slug": "vert-falho",
            "deck": "Deck",
            "saas_em_foco": {"nome": "SaaS"},
            "stats": {},
            "quinteto": [
                {"nome": "Tool 1", "classificacao": "A Mais Robusta"}
            ]
        }
        valido, erros = validar_dossie_vertical(dados_incompletos)
        assert valido is False
        assert any("5 ferramentas" in e for e in erros)

    def test_05_validar_manual_operacional_com_desinstalacao_cirurgica(self):
        json_path = BASE_DIR / "scripts" / "data" / "manual-xtts-v2.json"
        assert json_path.exists()
        dados = carregar_json_seguro(json_path)
        valido, erros = validar_manual_operacional(dados)
        assert valido is True, f"Erros no manual operacional: {erros}"
        assert len(erros) == 0

    def test_06_validar_manual_operacional_rejeita_sem_isolamento_vps(self):
        dados_falhos = {
            "produto_foco": "Tool",
            "slug": "tool",
            "saas_origem": "saas",
            "vps_recomendada": {"vcpu": "2", "ram": "4GB", "so_recomendado": "Ubuntu"},
            "instalacao_producao": {"passos": [1,2,3], "arquivos_configuracao": [1]},
            "manual_uso_exaustivo": {"roteiro_primeiro_voo": [1,2,3], "comandos_cli": [1,2]},
            "desinstalacao_cirurgica": {}, # Sem principio de isolamento nem passos
            "referencias_bibliograficas": [1, 2, 3]
        }
        valido, erros = validar_manual_operacional(dados_falhos)
        assert valido is False
        assert any("principio_isolamento" in e for e in erros)

    def test_07_tolerancia_utf8_bom_em_carregador_seguro(self, tmp_path):
        f_bom = tmp_path / "teste_bom.json"
        f_bom.write_text('{"teste": "sucesso"}', encoding="utf-8-sig")
        dados = carregar_json_seguro(f_bom)
        assert dados.get("teste") == "sucesso"
