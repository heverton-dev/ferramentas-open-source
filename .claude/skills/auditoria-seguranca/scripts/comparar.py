#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Compara baseline com pos-correcao e aplica o gate do ciclo.

Gate (escolha do usuario, estagio 4 da skill):
  exit 1 se sobrar CRITICO do baseline sem resolver, ou se surgir QUALQUER achado novo.
  exit 0 caso contrario.

Gate vermelho nao se conserta afrouxando o gate. Volta-se ao estagio 2.

Uso:
    python comparar.py --baseline .auditoria/baseline.json \
                       --pos .auditoria/pos-correcao.json \
                       --saida .auditoria/comparativo.json
"""
import argparse
import json
import sys
from pathlib import Path

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

SEVS = ["critica", "alta", "media", "baixa", "informativa"]


def carregar(caminho: str) -> dict:
    p = Path(caminho)
    if not p.is_file():
        print(f"[!] Arquivo inexistente: {p}")
        sys.exit(1)
    d = json.loads(p.read_text(encoding="utf-8"))
    faltando = [a.get("titulo", "?") for a in d.get("achados", []) if not a.get("id")]
    if faltando:
        print(f"[!] {len(faltando)} achado(s) sem id em {p}. Rode fingerprint.py antes.")
        sys.exit(1)
    return d


def contar(achados: list) -> dict:
    c = {s: 0 for s in SEVS}
    for a in achados:
        s = a.get("severidade", "informativa")
        c[s] = c.get(s, 0) + 1
    return c


def resumir(a: dict) -> dict:
    return {
        "id": a.get("id"), "titulo": a.get("titulo"),
        "categoria": a.get("categoria"), "severidade": a.get("severidade"),
        "arquivo": a.get("arquivo"), "linhas": a.get("linhas", []),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--baseline", required=True)
    ap.add_argument("--pos", required=True)
    ap.add_argument("--saida", default=".auditoria/comparativo.json")
    ap.add_argument("--reconciliacao", default=".auditoria/reconciliacao.json",
                    help="pares {id_baseline: id_pos} confirmados por leitura")
    args = ap.parse_args()

    base, pos = carregar(args.baseline), carregar(args.pos)
    lb, lp = base.get("achados", []), pos.get("achados", [])

    # Reconciliacao manual: pares {id_baseline: id_pos} confirmados por leitura.
    # Necessaria quando o mesmo achado muda de arquivo entre as passadas (o auditor
    # seguinte localizou a origem, nao o sintoma) — nenhuma chave automatica casa isso.
    recon = {}
    if args.reconciliacao and Path(args.reconciliacao).is_file():
        recon = json.loads(Path(args.reconciliacao).read_text(encoding="utf-8")).get("pares", {})

    usados_pos, corrigidos, persistentes = set(), [], []

    for a in lb:
        alvo = None
        # 1) id fino
        alvo = next((x for x in lp if x["id"] == a["id"] and x["id"] not in usados_pos), None)
        # 2) reconciliacao explicita
        if alvo is None and a["id"] in recon:
            alvo = next((x for x in lp if x["id"] == recon[a["id"]]), None)
        # 3) categoria + arquivo (titulos divergem entre auditores independentes)
        if alvo is None:
            alvo = next((x for x in lp
                         if x.get("id_local") and x.get("id_local") == a.get("id_local")
                         and x["id"] not in usados_pos), None)
        if alvo is not None:
            usados_pos.add(alvo["id"])
            r = resumir(alvo)
            r["casado_por"] = ("id" if alvo["id"] == a["id"]
                               else "reconciliacao" if a["id"] in recon else "arquivo+categoria")
            r["titulo_baseline"] = a.get("titulo")
            r["severidade_baseline"] = a.get("severidade")
            persistentes.append(r)
        else:
            corrigidos.append(resumir(a))

    novos = [resumir(a) for a in lp if a["id"] not in usados_pos]

    ab = {a["id"]: a for a in lb}
    ap_ = {a["id"]: a for a in lp}

    # Gate
    motivos = []
    criticos_abertos = [a for a in persistentes if a["severidade"] == "critica"]
    if criticos_abertos:
        motivos.append(
            f"{len(criticos_abertos)} achado(s) critico(s) do baseline seguem abertos: "
            + "; ".join(a["titulo"] for a in criticos_abertos))
    if novos:
        motivos.append(
            f"{len(novos)} achado(s) novo(s) apos a correcao: "
            + "; ".join(f"{a['titulo']} ({a['severidade']})" for a in novos))

    gate = "reprovado" if motivos else "aprovado"

    # Taxa so sobre o que era vulnerabilidade de fato
    reais_base = [a for a in ab.values() if a.get("severidade") != "informativa"]
    reais_corr = [a for a in corrigidos if a["severidade"] != "informativa"]
    taxa = round(100 * len(reais_corr) / len(reais_base), 1) if reais_base else 100.0

    saida = {
        "projeto": base.get("projeto") or pos.get("projeto"),
        "corrigidos": corrigidos,
        "persistentes": persistentes,
        "novos": novos,
        "resumo": {
            "baseline": contar(list(ab.values())),
            "pos": contar(list(ap_.values())),
            "total_baseline": len(ab),
            "total_pos": len(ap_),
            "corrigidos": len(corrigidos),
            "persistentes": len(persistentes),
            "novos": len(novos),
            "taxa_correcao_pct": taxa,
            "gate": gate,
            "gate_motivos": motivos,
        },
    }

    dest = Path(args.saida)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(saida, ensure_ascii=False, indent=2), encoding="utf-8")

    r = saida["resumo"]
    print(f"[ok] Comparativo -> {dest}")
    print(f"     baseline {r['total_baseline']} -> pos {r['total_pos']}")
    print(f"     corrigidos {r['corrigidos']} | persistentes {r['persistentes']} | novos {r['novos']}")
    print(f"     por severidade (baseline): {r['baseline']}")
    print(f"     por severidade (pos):      {r['pos']}")
    print(f"     taxa de correcao: {r['taxa_correcao_pct']}% (exclui informativas)")

    if gate == "aprovado":
        print("[GATE] APROVADO")
        return 0
    print("[GATE] REPROVADO")
    for m in motivos:
        print(f"        - {m}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
