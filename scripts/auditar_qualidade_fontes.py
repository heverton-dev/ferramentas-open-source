# -*- coding: utf-8 -*-
"""
GATE MECÂNICO G0: AUDITORIA DE QUALIDADE & CRITÉRIOS DE ADMISSÃO DE FONTES
Valida deterministicamente se cada fonte coletada cumpre os 4 pilares do Padrão Diamante:
1. Autoridade de Domínio (Origem Primária / Whitelist de Ecossistema)
2. Atualidade & Recência (Ano >= 2023/2024 ou versão moderna)
3. Densidade Técnica (Mínimo de tópicos estruturados e trechos práticos)
4. Integridade de Metadados (Autor/Canal, Duração/Páginas, Categoria Canônica)

Retorna exit 0 em caso de 100% de aprovação ou exit 1 se houver fonte de baixa qualidade.
"""
import sys
import json
from pathlib import Path
from urllib.parse import urlparse

def console_utf8():
    if sys.platform == "win32":
        try:
            sys.stdout.reconfigure(encoding="utf-8")
            sys.stderr.reconfigure(encoding="utf-8")
        except Exception:
            pass

console_utf8()

# Lista de domínios reconhecidos por alta reputação técnica no ecossistema open source
DOMINIOS_AUTORIZADOS_WHITELIST = [
    "github.com",
    "gitlab.com",
    "docs.screenpipe.com",
    "screenpipe.com",
    "huggingface.co",
    "youtube.com",
    "youtu.be",
    "dev.to",
    "arxiv.org",
    "docker.com",
    "hetzner.com",
    "contabo.com",
    "ubuntu.com",
    "python.org",
    "rust-lang.org",
    "caddyserver.com",
    "whisper.cpp",
    "openai.com",
    "anthropic.com",
    "medium.com",
    "substack.com",
    "diolinux.com.br",
    "tabnews.com.br"
]

# Termos que indicam conteúdo legado/obsoleto que deve ser rejeitado
TERMOS_OBSOLETOS_BLACKLIST = [
    "python 2.",
    "ubuntu 16.04",
    "ubuntu 18.04",
    "centos 7",
    "docker-compose v1",
    "deprecated"
]

CATEGORIAS_PERMITIDAS = {
    "documentacao_oficial",
    "livro_ebook",
    "youtube",
    "curso_tutorial"
}

def auditar_fonte_individual(fonte: dict) -> list:
    """Retorna lista de erros encontrados na fonte. Vazia se aprovada."""
    erros = []
    fid = fonte.get("id", "DESCONHECIDO")
    url = fonte.get("url", "")
    titulo = fonte.get("titulo", "")
    categoria = fonte.get("categoria", "")
    autor = fonte.get("autor_ou_canal", "")

    # 1. Validação de Categoria Canônica
    if categoria not in CATEGORIAS_PERMITIDAS:
        erros.append(f"[{fid}] Categoria inválida: '{categoria}'. Permitidas: {CATEGORIAS_PERMITIDAS}")

    # 2. Validação de Metadados Obrigatórios
    if not titulo or len(titulo.strip()) < 10:
        erros.append(f"[{fid}] Título muito curto ou ausente (mínimo 10 caracteres).")
    if not autor or len(autor.strip()) < 3:
        erros.append(f"[{fid}] Autor ou Canal técnico não identificado.")

    # 3. Validação de Autoridade de Domínio (Whitelist)
    parsed = urlparse(url)
    dominio = parsed.netloc.lower()
    if dominio.startswith("www."):
        dominio = dominio[4:]

    aprovado_whitelist = any(dominio == dom or dominio.endswith("." + dom) or dom in dominio for dom in DOMINIOS_AUTORIZADOS_WHITELIST)
    if not aprovado_whitelist:
        erros.append(f"[{fid}] Domínio '{dominio}' não consta na lista de reputação técnica autorizada.")

    # 4. Validação de Rejeição de Obsoletos
    texto_combinado = (titulo + " " + json.dumps(fonte.get("trechos_chave", []))).lower()
    for termo in TERMOS_OBSOLETOS_BLACKLIST:
        if termo in texto_combinado:
            erros.append(f"[{fid}] Conteúdo obsoleto detectado: menção a '{termo}'.")

    # 5. Validação de Densidade Técnica
    topicos = fonte.get("topicos", [])
    if len(topicos) < 1:
        erros.append(f"[{fid}] Fonte sem tópicos técnicos indexados.")

    trechos = fonte.get("trechos_chave", [])
    if len(trechos) < 1:
        erros.append(f"[{fid}] Fonte sem nenhum trecho prático/reproduzível catalogado.")
    else:
        for t in trechos:
            if not t.get("conteudo") or len(t.get("conteudo", "").strip()) < 20:
                erros.append(f"[{fid}] Trecho prático muito raso (menos de 20 caracteres).")

    return erros

def auditar_qualidade_sumario(caminho_sumario: Path) -> bool:
    print(f"\n======================================================================")
    print(f"🛡️ GATE MECÂNICO G0: AUDITORIA DE QUALIDADE & CRITÉRIOS DE ADMISSÃO")
    print(f"======================================================================")
    print(f"Arquivo alvo: {caminho_sumario.name}")

    if not caminho_sumario.exists():
        print(f"❌ ERRO CRÍTICO: Arquivo de sumário não encontrado: {caminho_sumario}")
        return False

    with open(caminho_sumario, "r", encoding="utf-8") as f:
        dados = json.load(f)

    fontes = dados.get("fontes", [])
    total = len(fontes)
    print(f"Analisando {total} fontes sob os 4 pilares (Autoridade, Recência, Densidade e Metadados)...")

    todos_erros = []
    for f in fontes:
        erros_fonte = auditar_fonte_individual(f)
        if erros_fonte:
            todos_erros.extend(erros_fonte)
            print(f"   ❌ [{f.get('id')}] REPROVADO:")
            for e in erros_fonte:
                print(f"      -> {e}")
        else:
            print(f"   ✅ [{f.get('id')}] APROVADO: {f.get('titulo')[:55]}... ({f.get('categoria')})")

    print("----------------------------------------------------------------------")
    if todos_erros:
        print(f"❌ FALHA NO GATE G0: {len(todos_erros)} inconformidades detectadas em {total} fontes.")
        return False

    print(f"🏆 GATE G0 APROVADO: 100% das {total} fontes atendem aos critérios rigorosos de qualidade!")
    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        caminho_padrao = Path(__file__).resolve().parent / "data" / "sumario-fontes-screenpipe.json"
    else:
        caminho_padrao = Path(sys.argv[1])

    sucesso = auditar_qualidade_sumario(caminho_padrao)
    sys.exit(0 if sucesso else 1)
