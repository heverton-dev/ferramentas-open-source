#!/usr/bin/env python3
"""
test-syntax: compila todo .py do repositorio e valida todo .json/frontmatter.
Entrada: raiz do repositorio (padrao: pai deste arquivo)
Saida:   relatorio no console
Garantias: read-only (nao altera nenhum arquivo), exit 0 = sucesso.

Uso:
    python tests/test-syntax.py
    python tests/test-syntax.py --raiz ../meu-projeto
"""

import argparse
import json
import py_compile
import sys
import tempfile
from pathlib import Path

IGNORAR = {".git", "__pycache__", "node_modules", ".venv", "venv", ".pytest_cache"}

SKILLS_ECONOMIA = ["caveman", "headroom", "lean-ctx", "rtk-memory", "pre-flight-check"]


def console_utf8():
    for f in (sys.stdout, sys.stderr):
        try:
            f.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass


def varrer(raiz, sufixo):
    for p in raiz.rglob(f"*{sufixo}"):
        if any(parte in IGNORAR for parte in p.parts):
            continue
        yield p


def testar_python(raiz, erros):
    arquivos = list(varrer(raiz, ".py"))
    # cfile em tempdir: compilar nao deve sujar o repo com __pycache__ (read-only).
    with tempfile.TemporaryDirectory() as tmp:
        for i, p in enumerate(arquivos):
            try:
                py_compile.compile(str(p), cfile=str(Path(tmp) / f"{i}.pyc"),
                                   doraise=True)
            except py_compile.PyCompileError as e:
                erros.append(f"Python: {p.relative_to(raiz)} — {e.msg.strip()}")
    print(f"[*] Python: {len(arquivos)} arquivo(s) compilado(s)")


def testar_json(raiz, erros):
    arquivos = list(varrer(raiz, ".json"))
    for p in arquivos:
        try:
            json.loads(p.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            erros.append(f"JSON: {p.relative_to(raiz)} — linha {e.lineno}: {e.msg}")
    print(f"[*] JSON: {len(arquivos)} arquivo(s) parseado(s)")


def testar_frontmatter_skills(raiz, erros):
    """Todo SKILL.md precisa de frontmatter com name e description.

    Sem isso o harness nao indexa o skill — ele existe no disco e nunca e usado.
    """
    base = raiz / ".claude" / "skills"
    if not base.is_dir():
        erros.append("Skills: .claude/skills/ ausente")
        return
    encontrados = sorted(p.parent.name for p in base.glob("*/SKILL.md"))
    for skill in base.glob("*/SKILL.md"):
        texto = skill.read_text(encoding="utf-8", errors="replace")
        if not texto.startswith("---"):
            erros.append(f"Skill: {skill.parent.name} — sem frontmatter")
            continue
        cabecalho = texto.split("---", 2)[1]
        for campo in ("name:", "description:"):
            if campo not in cabecalho:
                erros.append(f"Skill: {skill.parent.name} — frontmatter sem '{campo}'")
    faltando = [s for s in SKILLS_ECONOMIA if s not in encontrados]
    if faltando:
        erros.append("Skills de economia ausentes: " + ", ".join(faltando))
    print(f"[*] Skills: {len(encontrados)} skill(s) verificado(s)")


def testar_claude_md(raiz, erros):
    alvo = raiz / ".claude" / "CLAUDE.md"
    if not alvo.is_file():
        erros.append("CLAUDE.md: .claude/CLAUDE.md ausente")
        return
    texto = alvo.read_text(encoding="utf-8", errors="replace")
    if "alwaysApply: true" not in texto:
        erros.append("CLAUDE.md: frontmatter sem 'alwaysApply: true'")
    print("[*] CLAUDE.md: frontmatter verificado")


def main():
    console_utf8()
    ap = argparse.ArgumentParser(description="Valida sintaxe do repositorio.")
    ap.add_argument("--raiz", default=str(Path(__file__).resolve().parent.parent))
    args = ap.parse_args()

    raiz = Path(args.raiz).resolve()
    print(f"Repositorio: {raiz}\n")

    erros = []
    testar_python(raiz, erros)
    testar_json(raiz, erros)
    testar_claude_md(raiz, erros)
    testar_frontmatter_skills(raiz, erros)

    print()
    if erros:
        for e in erros:
            print(f"[X] {e}")
        print(f"\nREPROVADO — {len(erros)} erro(s)")
        return 1
    print("Sintaxe validada")
    return 0


if __name__ == "__main__":
    sys.exit(main())
