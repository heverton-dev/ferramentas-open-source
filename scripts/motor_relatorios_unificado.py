# -*- coding: utf-8 -*-
"""
MOTOR UNIVERSAL DE RELATÓRIOS OFICIAIS DE EXECUÇÃO & TELEMETRIA AIDD (NÍVEL ENTERPRISE)
Orquestrador central de relatórios nos 3 formatos (MD, HTML Diamante Enterprise e PDF Typst).
"""
from relatorios_fluxo1 import (
    gerar_relatorio_md_fluxo1,
    gerar_relatorio_html_fluxo1,
    gerar_relatorio_typst_fluxo1,
    gerar_relatorio_tripartite_fluxo1
)
from relatorios_fluxo2 import (
    gerar_relatorio_md_fluxo2,
    gerar_relatorio_html_fluxo2,
    gerar_relatorio_typst_fluxo2,
    gerar_relatorio_tripartite_fluxo2
)
from relatorios_fluxo3 import (
    gerar_relatorio_md_fluxo3,
    gerar_relatorio_html_fluxo3,
    gerar_relatorio_typst_fluxo3,
    gerar_relatorio_tripartite_fluxo3
)

__all__ = [
    "gerar_relatorio_md_fluxo1", "gerar_relatorio_html_fluxo1", "gerar_relatorio_typst_fluxo1", "gerar_relatorio_tripartite_fluxo1",
    "gerar_relatorio_md_fluxo2", "gerar_relatorio_html_fluxo2", "gerar_relatorio_typst_fluxo2", "gerar_relatorio_tripartite_fluxo2",
    "gerar_relatorio_md_fluxo3", "gerar_relatorio_html_fluxo3", "gerar_relatorio_typst_fluxo3", "gerar_relatorio_tripartite_fluxo3"
]
