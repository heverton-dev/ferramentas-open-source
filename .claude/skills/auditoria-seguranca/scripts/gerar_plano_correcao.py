#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Converte achados no plano JSON que /implementacao consome, e separa o que so um humano
pode fazer.

Formato consumido por /implementacao (index.cjs:33-36):
    { "plan_id": str, "phases": [ { "id", "type", "task": { "command", ... } } ] }

Faixas:
  auto      -> vira fase habilitada
  confirmar -> vira fase com "enabled": false (o operador libera apos revisar)
  humano    -> NAO vira fase. Sai em checklist-humano.md.

Regra dura: reescrita de historico git e rotacao de credencial nunca viram comando.
Sao destrutivas ou externas ao repositorio, e so o dono pode executar.

Uso:
    python gerar_plano_correcao.py --achados .auditoria/baseline.json \
        --saida .auditoria/plano-correcao.json
"""
import argparse
import json
import re
import sys
from pathlib import Path

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

ORDEM = {"critica": 0, "alta": 1, "media": 2, "baixa": 3, "informativa": 4}

# Sinais de acao que jamais podem ser automatizadas, mesmo se marcadas como 'auto'.
# Rede de seguranca contra classificacao equivocada na triagem.
# Precisao importa: "producao" solto casa com meio relatorio em PT-BR e mandaria
# correcoes triviais para o checklist manual. Cada alternativa exige o verbo da acao.
NUNCA_AUTO = re.compile(
    r'(?i)(filter-branch|filter-repo|\bbfg\b|rewrite\s+history|reescrever\s+(o\s+)?historico'
    r'|force[- ]push|push\s+--force|git\s+push'
    r'|rotacionar|rotacao\s+de|revogar|revoke'
    r'|regenerar\s+(o\s+|a\s+)?(token|credencial|chave|senha|pat)'
    r'|trocar\s+(a\s+)?senha|reset\s+password'
    r'|(deploy|implantar|publicar)\s+em\s+producao'
    r'|no\s+provedor|no\s+painel\s+do)')


def slug(txt: str, n: int = 40) -> str:
    s = re.sub(r'[^a-z0-9]+', '-', (txt or "").lower()).strip('-')
    return s[:n] or "item"


def faixa_efetiva(a: dict) -> str:
    """A rede de seguranca vence a marcacao da triagem."""
    declarada = a.get("faixa", "confirmar")
    texto = f"{a.get('titulo','')} {a.get('correcao','')}"
    if NUNCA_AUTO.search(texto):
        return "humano"
    if declarada not in ("auto", "confirmar", "humano"):
        return "confirmar"
    return declarada


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--achados", required=True)
    ap.add_argument("--saida", default=".auditoria/plano-correcao.json")
    ap.add_argument("--checklist", default=".auditoria/checklist-humano.md")
    ap.add_argument("--dir-correcoes", default=".auditoria/correcoes")
    args = ap.parse_args()

    p = Path(args.achados)
    if not p.is_file():
        print(f"[!] Arquivo inexistente: {p}")
        return 1

    dados = json.loads(p.read_text(encoding="utf-8"))
    achados = sorted(dados.get("achados", []),
                     key=lambda a: ORDEM.get(a.get("severidade", "informativa"), 9))

    fases, humanos, confirmar = [], [], []
    dir_corr = Path(args.dir_correcoes)

    for a in achados:
        faixa = faixa_efetiva(a)
        if a.get("severidade") == "informativa" and faixa != "auto":
            continue  # divida arquitetural nao entra no plano de correcao

        if faixa == "humano":
            humanos.append(a)
            continue

        nome = slug(f"{a.get('categoria','')}-{a.get('titulo','')}")
        script = (dir_corr / f"{nome}.py").as_posix()
        teste = (dir_corr / f"test_{nome}.py").as_posix()

        # O runner despacha por phase.id e so conhece impl/test/validate/verify
        # (index.cjs:301-313). Logo: um PLANO por achado, com o ciclo de 4 fases —
        # e nao um plano unico com uma fase por achado.
        plano_achado = {
            "plan_id": f"fix-{a.get('id', nome)}",
            "title": a.get("titulo"),
            "_meta": {
                "faixa": faixa,
                "severidade": a.get("severidade"),
                "categoria": a.get("categoria"),
                "arquivo": a.get("arquivo"),
                "linhas": a.get("linhas", []),
                "correcao_pretendida": a.get("correcao"),
                "script_correcao": script,
                "script_teste": teste,
                "requisito_do_teste": "Precisa falhar ANTES da correcao e passar DEPOIS.",
            },
            "phases": [
                {"id": "impl", "name": f"Corrigir: {a.get('titulo')}",
                 "task": {"command": f"python {script}", "timeout_ms": 120000,
                          "expected_outputs": []}},
                {"id": "test", "name": "Provar a correcao",
                 "task": {"test_command": f"python -m pytest {teste} -q",
                          "coverage_min": 0, "timeout_ms": 120000}},
                {"id": "verify", "name": "Conferir",
                 "task": {"verify_command": f"python -m pytest {teste} -q",
                          "timeout_ms": 120000, "git_commit": False}},
            ],
        }
        fases.append(plano_achado)
        if faixa == "confirmar":
            confirmar.append(a)

    # Um arquivo de plano por achado, em diretorios separados por faixa. A separacao
    # fisica e a unica garantia de que o plano sob confirmacao nao roda por engano:
    # o runner nao le nenhum flag de habilitacao (index.cjs:298).
    dest = Path(args.saida)
    dir_planos = dest.parent / "planos"
    dir_auto, dir_conf = dir_planos / "auto", dir_planos / "sob-confirmacao"
    for d in (dir_auto, dir_conf, dir_corr):
        d.mkdir(parents=True, exist_ok=True)

    auto = [f for f in fases if f["_meta"]["faixa"] == "auto"]
    conf = [f for f in fases if f["_meta"]["faixa"] == "confirmar"]

    escritos = {"auto": [], "confirmar": []}
    for grupo, lista, destino in (("auto", auto, dir_auto),
                                  ("confirmar", conf, dir_conf)):
        for i, pl in enumerate(lista, 1):
            arq = destino / f"{i:02d}-{slug(pl['title'])}.json"
            arq.write_text(json.dumps(pl, ensure_ascii=False, indent=2), encoding="utf-8")
            escritos[grupo].append(arq.as_posix())

    # Indice: ordem de execucao e onde cada plano vive
    dest.write_text(json.dumps({
        "projeto": dados.get("projeto", "projeto"),
        "origem": str(p),
        "como_executar": [
            "Escreva o script de correcao e o de teste de cada plano.",
            "Confirme que o teste FALHA antes da correcao.",
            "Rode, em ordem: node .claude/skills/implementacao/index.cjs <plano>",
            "Os planos em planos/sob-confirmacao/ exigem aprovacao explicita antes.",
        ],
        "planos_automaticos": escritos["auto"],
        "planos_sob_confirmacao": escritos["confirmar"],
    }, ensure_ascii=False, indent=2), encoding="utf-8")

    plano = {"phases": fases}

    # ------------------------------------------------------------ checklist
    L = ["# Checklist humano — acoes que a automacao nao pode executar", ""]
    L += ["Cada item abaixo e destrutivo, irreversivel ou externo ao repositorio.",
          "Nenhum vira comando automatico. Executar manualmente e marcar.", ""]
    if not humanos:
        L += ["Nenhum item nesta categoria.", ""]
    for i, a in enumerate(humanos, 1):
        linhas = ", ".join(str(x) for x in a.get("linhas", [])) or "-"
        L += [
            f"## {i}. {a.get('titulo')}",
            "",
            f"- **Severidade:** {a.get('severidade')}",
            f"- **Categoria:** {a.get('categoria')}",
            f"- **Local:** `{a.get('arquivo')}:{linhas}`",
            f"- **Por que e explorável:** {a.get('por_que_exploravel','-')}",
            f"- **Impacto:** {a.get('impacto','-')}",
            "",
            f"**Acao:** {a.get('correcao','-')}",
            "",
            "- [ ] Executado",
            "- [ ] Verificado",
            "",
        ]
    if any("chaves" in (a.get("categoria") or "") for a in humanos):
        L += [
            "---", "",
            "> Segredo que ja esteve num commit deve ser tratado como comprometido.",
            "> Remover do arquivo nao desfaz o vazamento: rotacione no provedor.",
            "> Reescrita de historico (`filter-repo`, BFG) quebra o clone de todos os",
            "> colaboradores — combine antes com a equipe.", "",
        ]
    Path(args.checklist).write_text("\n".join(L), encoding="utf-8")

    print(f"[ok] Indice -> {dest}")
    print(f"[ok] {len(auto)} plano(s) automatico(s) em {dir_auto.as_posix()}/")
    if conf:
        print(f"[ok] {len(conf)} plano(s) sob confirmacao em {dir_conf.as_posix()}/")
        print("     NAO execute estes sem aprovacao explicita do usuario.")
    print(f"[ok] Checklist humano -> {args.checklist} ({len(humanos)} item(ns))")
    print(f"[!] Escreva os scripts em {dir_corr}/ antes de rodar /implementacao.")
    print("[!] Cada teste precisa FALHAR antes da correcao. Sem isso nao ha prova.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
