#!/usr/bin/env python3
"""
<modulo>: <descricao em uma linha>
Entrada: <input>
Saida:   <output.json>
Garantias: idempotente, sem side effects fora da saida declarada, exit 0 = sucesso.

Uso:
    python scripts/<modulo>.py <alvo>
    python scripts/<modulo>.py <alvo> --estrito
"""

import argparse
import json
import sys
from pathlib import Path


def console_utf8():
    """Windows: sem isto, qualquer print nao-ASCII quebra em cp1252 (R11 do CLAUDE.md).

    OBRIGATORIO em todo script com print/emoji. Chamar como primeira linha de main().
    """
    for f in (sys.stdout, sys.stderr):
        try:
            f.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass


def caminho_relatorio(alvo):
    return Path("relatorios") / f"<modulo>-{Path(alvo).stem}.json"


def executar(alvo, estrito=False):
    """Logica do script. Retorna (ok: bool, dados: dict).

    Toda a regra de negocio mora aqui — main() so cuida de I/O e exit code,
    para que esta funcao seja testavel sem subprocess.
    """
    dados = {"alvo": str(alvo), "problemas": [], "avisos": []}

    # ==== SUA LOGICA AQUI ====
    # dados["problemas"].append({"onde": ..., "o_que": ..., "como_corrigir": ...})
    # dados["avisos"].append(...)

    reprovado = bool(dados["problemas"]) or (estrito and bool(dados["avisos"]))
    return (not reprovado), dados


def main():
    console_utf8()
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[1])
    ap.add_argument("alvo", help="<o que este script recebe>")
    ap.add_argument("--estrito", action="store_true", help="avisos tambem reprovam")
    ap.add_argument("--silencioso", action="store_true", help="so o exit code importa")
    args = ap.parse_args()

    # O relatorio e gravado SEMPRE — inclusive em excecao. Um gate que morre sem
    # relatorio e indistinguivel de um gate que nunca rodou.
    relatorio = {"status": "falha", "erro": None}
    try:
        ok, dados = executar(args.alvo, estrito=args.estrito)
        relatorio.update(dados)
        relatorio["status"] = "sucesso" if ok else "falha"
    except Exception as e:
        relatorio["erro"] = f"{type(e).__name__}: {e}"
        raise
    finally:
        destino = caminho_relatorio(args.alvo)
        destino.parent.mkdir(parents=True, exist_ok=True)
        destino.write_text(json.dumps(relatorio, ensure_ascii=False, indent=2),
                           encoding="utf-8")
        if not args.silencioso:
            for p in relatorio.get("problemas", []):
                print(f"[X] {p}")
            for a in relatorio.get("avisos", []):
                print(f"[!] {a}")
            print(f"status={relatorio['status']} relatorio={destino}")

    return 0 if relatorio["status"] == "sucesso" else 1


if __name__ == "__main__":
    sys.exit(main())
