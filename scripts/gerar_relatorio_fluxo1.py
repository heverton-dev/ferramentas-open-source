# -*- coding: utf-8 -*-
"""
GERADOR DE RELATÓRIO DE EXECUÇÃO TRIPARTITE — FLUXO 1 (LISTAS HORIZONTAIS)
Wrapper canônico que utiliza o motor universal com telemetria completa e parecer da LLM.
"""
from pathlib import Path
from motor_relatorios_unificado import (
    gerar_relatorio_md_fluxo1,
    gerar_relatorio_tripartite_fluxo1 as gerar_relatorio_tripartite
)

__all__ = ["gerar_relatorio_md_fluxo1", "gerar_relatorio_tripartite"]
