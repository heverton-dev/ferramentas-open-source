from pathlib import Path
from motor_relatorios_unificado import (
    gerar_relatorio_md_fluxo3,
    gerar_relatorio_html_fluxo3,
    gerar_relatorio_typst_fluxo3,
    gerar_relatorio_tripartite_fluxo3
)

BASE_DIR = Path(__file__).resolve().parent.parent

def gerar_relatorio_execucao(slug: str, dados_telemetria: dict = None, saas: str = None) -> dict:
    if saas is None:
        saas = dados_telemetria.get("saas_origem", "granola") if dados_telemetria else "granola"
    bundle_dir = BASE_DIR / "output" / "03-manuais-e-trilhas" / saas / slug
    return gerar_relatorio_tripartite_fluxo3(slug, saas, bundle_dir, dados_telemetria)

__all__ = ["gerar_relatorio_md_fluxo3", "gerar_relatorio_html_fluxo3", "gerar_relatorio_typst_fluxo3", "gerar_relatorio_tripartite_fluxo3", "gerar_relatorio_execucao"]

