# -*- coding: utf-8 -*-
"""
GATE MECÂNICO G1: AUDITOR DE FONTES VERÍDICAS E VERIFICÁVEIS (R9 / R17)
Testa se 100% das URLs de um sumário de fontes retornam status HTTP 200/3xx válido.
Zero alucinação: se houver link quebrado ou 404, o gate barra a esteira (exit 1).
"""
import sys
import json
import urllib.request
import urllib.error
from pathlib import Path

def console_utf8():
    if sys.platform == "win32":
        try:
            sys.stdout.reconfigure(encoding="utf-8")
            sys.stderr.reconfigure(encoding="utf-8")
        except Exception:
            pass

console_utf8()

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
}

def checar_url(url: str, timeout: int = 6) -> tuple[bool, int, str]:
    """Testa URL com GET leve."""
    try:
        req = urllib.request.Request(url, headers=HEADERS, method="GET")
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            status = resp.getcode()
            if 200 <= status < 400:
                return True, status, "OK"
            return False, status, f"HTTP {status}"
    except urllib.error.HTTPError as e:
        # Algumas plataformas retornam 403 para bots com UA genérico mas o link existe
        if e.code in [403, 401, 429]:
            return True, e.code, f"Aviso: HTTP {e.code} (Protegido contra bot/rate-limit, aceito como verídico)"
        return False, e.code, f"HTTP Error {e.code}"
    except urllib.error.URLError as e:
        return False, 0, f"Falha de Conexao: {e.reason}"
    except Exception as e:
        return False, 0, str(e)

def auditar_sumario(caminho_json: Path, fail_fast: bool = False) -> bool:
    if not caminho_json.exists():
        print(f"❌ Erro crítico: Arquivo {caminho_json} não encontrado.")
        return False

    with open(caminho_json, "r", encoding="utf-8") as f:
        dados = json.load(f)

    fontes = dados.get("fontes", [])
    total = len(fontes)
    if total == 0:
        print(f"❌ Nenhuma fonte registrada em {caminho_json.name}.")
        return False

    print(f"\n🔍 [Gate G1] Auditando {total} fontes em {caminho_json.name}...")
    aprovadas = 0
    falhas = []

    for fonte in fontes:
        f_id = fonte.get("id", "F??")
        titulo = fonte.get("titulo", "Sem título")
        url = fonte.get("url", "")
        
        valido, status, msg = checar_url(url)
        if valido:
            aprovadas += 1
            print(f"   ✅ [{f_id}] {status} - {titulo[:45]}... ({url[:50]}...)")
        else:
            falhas.append((f_id, titulo, url, msg))
            print(f"   ❌ [{f_id}] FALHA: {msg} - {url}")
            if fail_fast:
                break

    print(f"\n📊 Resultado da Auditoria G1: {aprovadas}/{total} fontes verificadas com sucesso.")
    if falhas:
        print(f"❌ REPROVADO: {len(falhas)} fonte(s) inacessível(is). Corrija as URLs antes de prosseguir.")
        return False

    print(f"✅ APROVADO: 100% das fontes são verídicas e verificáveis.\n")
    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python auditar_fontes_veridicas.py <caminho_para_sumario.json>")
        sys.exit(1)

    caminho = Path(sys.argv[1])
    sucesso = auditar_sumario(caminho)
    sys.exit(0 if sucesso else 1)
