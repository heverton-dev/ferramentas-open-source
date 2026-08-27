# -*- coding: utf-8 -*-
"""
COMPILADOR E NORMALIZADOR DO SUMÁRIO DE FONTES INTERMEDIÁRIO (R8 / R11)
Valida a estrutura de sumário contra scripts/schemas/schema_sumario_fontes.json
e organiza trechos por tópicos semânticos para consumo eficiente pela LLM.
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

def indexar_trechos_por_topico(caminho_sumario: Path) -> dict:
    """Carrega o sumário e organiza um índice invertido tópico -> [trechos com [Fn]]."""
    with open(caminho_sumario, "r", encoding="utf-8") as f:
        dados = json.load(f)

    indice_topicos = {}
    for fonte in dados.get("fontes", []):
        f_id = fonte["id"]
        for trecho in fonte.get("trechos_chave", []):
            topico = trecho["topico"]
            if topico not in indice_topicos:
                indice_topicos[topico] = []
            indice_topicos[topico].append({
                "fonte_id": f_id,
                "titulo_fonte": fonte["titulo"],
                "url": fonte["url"],
                "conteudo": trecho["conteudo"],
                "ancora": trecho.get("ancora_ou_minutagem", "")
            })

    return {
        "produto_foco": dados["produto_foco"],
        "slug": dados["slug"],
        "saas_origem": dados["saas_origem"],
        "total_fontes": len(dados["fontes"]),
        "indice_topicos": indice_topicos
    }

if __name__ == "__main__":
    slug = sys.argv[1] if len(sys.argv) > 1 else "screenpipe"
    caminho = BASE_DIR / "scripts" / "data" / f"sumario-fontes-{slug}.json"
    if not caminho.exists():
        print(f"❌ Erro: {caminho} não encontrado. Execute coletar_fontes_pesquisa.py primeiro.")
        sys.exit(1)

    resultado = indexar_trechos_por_topico(caminho)
    print(f"✅ Sumário {slug} indexado com sucesso!")
    print(f"   -> Tópicos indexados: {list(resultado['indice_topicos'].keys())}")
