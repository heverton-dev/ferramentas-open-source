#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Carimba fingerprint estavel em cada achado, para casar baseline com pos-correcao.

O fingerprint IGNORA o numero da linha de proposito: qualquer edicao desloca linhas,
e um achado que so desceu tres linhas nao pode ser contado como corrigido.

Preco aceito: duas ocorrencias da mesma regra no mesmo arquivo colidem num id so.
E aceitavel porque a correcao trata as duas juntas.

Uso:
    python fingerprint.py --entrada .auditoria/baseline.json --inplace
    python fingerprint.py --entrada baseline.json --saida baseline-id.json
"""
import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Ruido que muda entre auditorias sem mudar o achado
PARADAS = {
    "de", "da", "do", "das", "dos", "e", "em", "no", "na", "nos", "nas", "o", "a",
    "os", "as", "um", "uma", "para", "por", "com", "sem", "que", "the", "of", "in",
    "ausente", "ausencia", "falta", "faltando", "possivel", "potencial",
}


def normalizar(titulo: str) -> str:
    """Titulo -> forma canonica. Reescrever o titulo nao pode gerar id novo."""
    t = titulo.lower()
    t = re.sub(r'[^a-z0-9\s]', ' ', t)
    palavras = [p for p in t.split() if p and p not in PARADAS and len(p) > 2]
    return "-".join(sorted(set(palavras))[:6])


def _arquivo(achado: dict) -> str:
    return (achado.get("arquivo", "?") or "?").replace("\\", "/").lower().rstrip("/")


def fingerprint(achado: dict) -> str:
    """Id fino: distingue dois achados diferentes no mesmo arquivo."""
    base = "|".join([achado.get("categoria", "?"), _arquivo(achado),
                     normalizar(achado.get("titulo", ""))])
    return hashlib.sha256(base.encode("utf-8")).hexdigest()[:12]


def fingerprint_local(achado: dict) -> str:
    """
    Id grosso: categoria + arquivo, SEM o titulo.

    Existe porque duas auditorias independentes descrevem o mesmo achado com palavras
    diferentes — "credenciais em texto plano no .env" e "o .env acumula credenciais
    vivas" sao o mesmo problema e produzem ids finos distintos. Sem esta chave o
    comparativo conta o achado como corrigido E como novo, inflando os dois lados.
    """
    base = "|".join([achado.get("categoria", "?"), _arquivo(achado)])
    return hashlib.sha256(base.encode("utf-8")).hexdigest()[:12]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--entrada", required=True)
    ap.add_argument("--saida")
    ap.add_argument("--inplace", action="store_true")
    args = ap.parse_args()

    p = Path(args.entrada)
    if not p.is_file():
        print(f"[!] Arquivo inexistente: {p}")
        return 1

    dados = json.loads(p.read_text(encoding="utf-8"))
    achados = dados.get("achados", [])

    vistos, colisoes = {}, 0
    for a in achados:
        fp = fingerprint(a)
        if fp in vistos:
            colisoes += 1
        vistos.setdefault(fp, []).append(a.get("titulo", ""))
        a["id"] = fp
        a["id_local"] = fingerprint_local(a)

    dest = p if args.inplace else Path(args.saida or "achados-id.json")
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(dados, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"[ok] {len(achados)} achados carimbados -> {dest}")
    if colisoes:
        print(f"[!] {colisoes} colisao(oes) de fingerprint (mesma regra + mesmo arquivo).")
        for fp, titulos in vistos.items():
            if len(titulos) > 1:
                print(f"    {fp}: {' | '.join(titulos)}")
        print("    Se forem achados distintos, diferencie os titulos.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
