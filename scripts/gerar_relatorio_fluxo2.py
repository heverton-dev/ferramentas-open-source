# -*- coding: utf-8 -*-
"""
GERADOR DE RELATÓRIO DE EXECUÇÃO TRIPARTITE — FLUXO 2 (DOSSIÊS VERTICAIS & QUINTETO SOBERANO)
Wrapper canônico que utiliza o motor universal com telemetria completa e parecer da LLM.
"""
from pathlib import Path
from motor_relatorios_unificado import (
    gerar_relatorio_md_fluxo2,
    gerar_relatorio_tripartite_fluxo2
)

__all__ = ["gerar_relatorio_md_fluxo2", "gerar_relatorio_tripartite_fluxo2"]
