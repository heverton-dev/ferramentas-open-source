#!/usr/bin/env python3
"""
validate: valida a integracao da fabrica-universal em um projeto consumidor.
Entrada: raiz do projeto (padrao: diretorio atual, ou --raiz <path>)
Saida:   relatorio no console + validate-report.json (a menos que --sem-json)
Garantias: idempotente, sem side effects (so escreve o relatorio), exit 0 = sucesso.

Uso:
    python scripts/validate.py                 # valida o diretorio atual
    python scripts/validate.py --raiz ../meu   # valida outro projeto
    python scripts/validate.py --estrito       # avisos tambem reprovam
"""

import argparse
import json
import subprocess
import sys
from pathlib import Path

SKILLS_ECONOMIA = ["caveman", "headroom", "lean-ctx", "rtk-memory", "pre-flight-check"]

OK, AVISO, FALHA = "ok", "aviso", "falha"

SIMBOLO = {OK: "[OK]  ", AVISO: "[!]   ", FALHA: "[X]   "}


def console_utf8():
    """Windows: sem isto, qualquer print nao-ASCII quebra em cp1252."""
    for f in (sys.stdout, sys.stderr):
        try:
            f.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass


class Relatorio:
    def __init__(self):
        self.checks = []

    def add(self, nome, estado, detalhe=""):
        self.checks.append({"check": nome, "estado": estado, "detalhe": detalhe})
        print(f"{SIMBOLO[estado]}{nome}" + (f" — {detalhe}" if detalhe else ""))

    def conta(self, estado):
        return sum(1 for c in self.checks if c["estado"] == estado)


def check_claude_md(raiz, rel):
    """CLAUDE.md precisa existir e carregar sempre (alwaysApply: true)."""
    candidatos = [raiz / ".claude" / "CLAUDE.md", raiz / "CLAUDE.md"]
    achados = [p for p in candidatos if p.is_file()]
    if not achados:
        rel.add("CLAUDE.md presente", FALHA, "nem .claude/CLAUDE.md nem CLAUDE.md")
        return
    alvo = achados[0]
    texto = alvo.read_text(encoding="utf-8", errors="replace")
    if "alwaysApply: true" in texto:
        rel.add("CLAUDE.md presente", OK, str(alvo.relative_to(raiz)))
    else:
        rel.add("CLAUDE.md presente", FALHA,
                f"{alvo.relative_to(raiz)} sem 'alwaysApply: true' no frontmatter")
        return
    if "<SEU-PROJETO>" in texto or "[CUSTOMIZAR]" in texto:
        rel.add("CLAUDE.md customizado", AVISO,
                "ainda contem placeholders (<SEU-PROJETO> / [CUSTOMIZAR])")
    else:
        rel.add("CLAUDE.md customizado", OK)


def check_skills(raiz, rel):
    base = raiz / ".claude" / "skills"
    faltando = [s for s in SKILLS_ECONOMIA if not (base / s / "SKILL.md").is_file()]
    if faltando:
        rel.add("Skills de economia (5)", FALHA, "faltando: " + ", ".join(faltando))
    else:
        rel.add("Skills de economia (5)", OK, ", ".join(SKILLS_ECONOMIA))


def check_python(raiz, rel):
    scripts = sorted((raiz / "scripts").glob("*.py")) if (raiz / "scripts").is_dir() else []
    if not scripts:
        rel.add("Sintaxe Python (scripts/)", AVISO, "nenhum .py em scripts/")
        return
    quebrados = []
    for s in scripts:
        r = subprocess.run([sys.executable, "-m", "py_compile", str(s)],
                           capture_output=True, text=True)
        if r.returncode != 0:
            quebrados.append(s.name)
    if quebrados:
        rel.add("Sintaxe Python (scripts/)", FALHA, "erro em: " + ", ".join(quebrados))
    else:
        rel.add("Sintaxe Python (scripts/)", OK, f"{len(scripts)} arquivo(s)")


def check_portabilidade(raiz, rel):
    """setup-links deve ter rodado: agentic/ aponta para .claude/."""
    links = raiz / "agentic" / "skills"
    if links.exists():
        rel.add("Portabilidade (agentic/)", OK)
    else:
        rel.add("Portabilidade (agentic/)", AVISO,
                "rode scripts/setup-links.ps1 (Win) ou setup-links.sh (Mac/Linux)")

    espelho = raiz / "AGENTS.md"
    if espelho.exists():
        rel.add("Espelho AGENTS.md", OK)
    else:
        rel.add("Espelho AGENTS.md", AVISO, "hardlink/symlink de CLAUDE.md ausente")


def check_hook(raiz, rel):
    fonte = raiz / "scripts" / "hooks" / "pre-commit"
    instalado = raiz / ".git" / "hooks" / "pre-commit"
    if not fonte.is_file():
        rel.add("Hook pre-commit (fonte)", FALHA, "scripts/hooks/pre-commit ausente")
    else:
        rel.add("Hook pre-commit (fonte)", OK)
    if instalado.is_file():
        rel.add("Hook pre-commit (instalado)", OK)
    else:
        rel.add("Hook pre-commit (instalado)", AVISO,
                ".git/hooks/pre-commit ausente — rode setup-links")


def check_scripts_universais(raiz, rel):
    esperados = ["setup-links.ps1", "setup-links.sh", "validate.py"]
    faltando = [n for n in esperados if not (raiz / "scripts" / n).is_file()]
    if faltando:
        rel.add("Scripts universais", AVISO, "faltando: " + ", ".join(faltando))
    else:
        rel.add("Scripts universais", OK, ", ".join(esperados))


def main():
    console_utf8()
    ap = argparse.ArgumentParser(description="Valida a integracao da fabrica-universal.")
    ap.add_argument("--raiz", default=".", help="raiz do projeto a validar")
    ap.add_argument("--estrito", action="store_true", help="avisos tambem reprovam")
    ap.add_argument("--sem-json", action="store_true", help="nao gravar validate-report.json")
    args = ap.parse_args()

    raiz = Path(args.raiz).resolve()
    print(f"Validando: {raiz}\n")

    rel = Relatorio()
    resultado = {"raiz": str(raiz), "status": "falha", "checks": rel.checks}
    try:
        check_claude_md(raiz, rel)
        check_skills(raiz, rel)
        check_scripts_universais(raiz, rel)
        check_python(raiz, rel)
        check_portabilidade(raiz, rel)
        check_hook(raiz, rel)

        falhas, avisos = rel.conta(FALHA), rel.conta(AVISO)
        reprovado = falhas > 0 or (args.estrito and avisos > 0)
        resultado["status"] = "falha" if reprovado else "sucesso"
        resultado["falhas"], resultado["avisos"] = falhas, avisos

        print()
        if reprovado:
            print(f"REPROVADO — {falhas} falha(s), {avisos} aviso(s)")
        else:
            print(f"Setup validado — {avisos} aviso(s)")
    finally:
        if not args.sem_json:
            (raiz / "validate-report.json").write_text(
                json.dumps(resultado, ensure_ascii=False, indent=2), encoding="utf-8")

    return 0 if resultado["status"] == "sucesso" else 1


if __name__ == "__main__":
    sys.exit(main())
