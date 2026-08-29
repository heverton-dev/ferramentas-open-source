# -*- coding: utf-8 -*-
"""
GATE DE INICIALIZACAO DE CREDENCIAIS (R9 — Gates Mecanicos)

Recusa executar quando uma variavel critica esta ausente, vazia ou ainda contem
valor de exemplo. Falhar no inicio custa um erro; falhar no meio do fluxo custa
estado parcial e, no pior caso, acao contra o ambiente errado.

Uso:
    from validar_env import exigir
    exigir("PORTAINER_URL", "PORTAINER_USERNAME", "PORTAINER_PASSWORD")

    python scripts/validar_env.py          # confere tudo que estiver no .env
"""
import os
import re
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / ".env"

# Valores que indicam configuracao nao concluida. Comparados em minusculas.
VALORES_DE_EXEMPLO = {
    "changeme", "change-me", "troque", "trocar", "example", "exemplo",
    "seu-token-aqui", "your-token-here", "xxx", "xxxx", "todo", "tbd",
    "senha", "password", "secret", "admin", "root", "test", "teste",
    "senhasegura123", "coloque-aqui", "placeholder", "null", "none",
}

PADRAO_EXEMPLO = re.compile(
    r"(?i)^(senha|password|secret|token|chave|key)?[-_]?(segura?|forte|aleatoria|"
    r"exemplo|example|default|padrao)[0-9!@#]*$")


def carregar_env(caminho: Path = ENV_PATH) -> dict:
    """Le o .env sem depender de biblioteca externa."""
    valores = {}
    if not caminho.is_file():
        return valores
    for linha in caminho.read_text(encoding="utf-8", errors="ignore").splitlines():
        linha = linha.strip()
        if not linha or linha.startswith("#") or "=" not in linha:
            continue
        chave, _, valor = linha.partition("=")
        valores[chave.strip()] = valor.strip().strip('"').strip("'")
    return valores


SEGREDO = ("PASSWORD", "PASSWD", "SENHA", "TOKEN", "SECRET", "KEY", "APIKEY")


def _e_segredo(nome: str) -> bool:
    return any(t in nome.upper() for t in SEGREDO)


def _problema(nome: str, valor) -> str:
    if valor is None:
        return "ausente"
    v = str(valor).strip()
    if not v:
        return "vazia"
    # A lista de valores de exemplo so vale para campos de segredo. Em USER/HOST,
    # "root" e "admin" sao valores legitimos — recusa-los transforma o gate em
    # obstaculo e ensina o operador a ignora-lo.
    if _e_segredo(nome):
        if v.lower() in VALORES_DE_EXEMPLO or PADRAO_EXEMPLO.match(v):
            return "com valor de exemplo (nao foi substituido)"
        if len(v) < 8:
            return f"curta demais ({len(v)} caracteres)"
    elif v.lower() in ("changeme", "change-me", "troque", "trocar", "placeholder",
                       "seu-valor-aqui", "todo", "tbd"):
        return "com valor de exemplo (nao foi substituido)"
    return ""


def exigir(*nomes: str, env: dict = None) -> dict:
    """
    Garante que cada variavel esta presente e utilizavel.
    Levanta RuntimeError listando TODOS os problemas de uma vez — corrigir um por
    execucao transforma configuracao em tentativa e erro.
    """
    valores = dict(env) if env is not None else {**carregar_env(), **os.environ}
    problemas = []
    for nome in nomes:
        p = _problema(nome, valores.get(nome))
        if p:
            problemas.append(f"  - {nome}: {p}")
    if problemas:
        raise RuntimeError(
            "Configuracao de credenciais incompleta em .env:\n"
            + "\n".join(problemas)
            + "\n\nCorrija o .env antes de executar. Use .env.example como referencia."
        )
    return {n: valores[n] for n in nomes}


def main() -> int:
    valores = carregar_env()
    if not valores:
        print(f"[!] .env nao encontrado em {ENV_PATH}")
        return 1
    ruins = [(n, p) for n, v in valores.items() if (p := _problema(n, v))]
    print(f"[*] {len(valores)} variaveis lidas de .env")
    if ruins:
        for n, p in ruins:
            print(f"  [!] {n}: {p}")
        print(f"[X] {len(ruins)} variavel(is) com problema.")
        return 1
    print("[ok] Todas as variaveis passaram na validacao.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
