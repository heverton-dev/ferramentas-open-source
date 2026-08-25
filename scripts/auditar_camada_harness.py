# -*- coding: utf-8 -*-
"""
GATE MECÂNICO DA CAMADA 2: AUDITOR DO HARNESS (ORQUESTRAÇÃO & SEGURANÇA)
Audita a integridade dos cabos, disjuntores, hooks e sandbox do agente:
1. Configuração industrial em .claude/settings.json (circuit_breaker, max_loop_iterations, sandbox).
2. Presença do hook .git/hooks/pre-commit e sua fonte versionada scripts/hooks/pre-commit.
3. Presença dos 6 gates obrigatórios no pre-commit (R15 Segredos, R16 Testes, Sintaxe, Grafo, R18 Higiene).
4. Presença e integridade dos scripts de portabilidade multi-IDE (scripts/setup-links.ps1 e .sh).
5. Retorna Exit 0 (100% Aprovado) ou Exit 1 com relatório de pendências.
"""
import os
import sys
import json

def console_utf8():
    if sys.platform == "win32":
        try:
            sys.stdout.reconfigure(encoding="utf-8")
            sys.stderr.reconfigure(encoding="utf-8")
        except Exception:
            pass

console_utf8()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SETTINGS_FILE = os.path.join(BASE_DIR, ".claude", "settings.json")
PRE_COMMIT_SRC = os.path.join(BASE_DIR, "scripts", "hooks", "pre-commit")
PRE_COMMIT_GIT = os.path.join(BASE_DIR, ".git", "hooks", "pre-commit")
SETUP_WIN = os.path.join(BASE_DIR, "scripts", "setup-links.ps1")
SETUP_SH = os.path.join(BASE_DIR, "scripts", "setup-links.sh")

def auditar_settings_json():
    erros = []
    if not os.path.isfile(SETTINGS_FILE):
        return ["Arquivo .claude/settings.json não encontrado!"]

    try:
        with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        return [f"Erro de sintaxe JSON em .claude/settings.json: {e}"]

    harness = data.get("harness", {})
    if not harness:
        erros.append("Seção 'harness' ausente em .claude/settings.json.")
    else:
        cb = harness.get("circuit_breaker", {})
        if not cb.get("max_loop_iterations"):
            erros.append("Disjuntor 'max_loop_iterations' ausente no circuit_breaker.")
        if not cb.get("command_timeout_seconds"):
            erros.append("Disjuntor 'command_timeout_seconds' ausente no circuit_breaker.")

        sb = harness.get("sandbox", {})
        if sb.get("disallow_shell_cd") is not True:
            erros.append("Diretriz de sandbox 'disallow_shell_cd' ausente ou inativa.")

    hooks = data.get("hooks", {})
    if "PostToolUse" not in hooks:
        erros.append("Hook 'PostToolUse' ausente em .claude/settings.json.")

    return erros

def auditar_pre_commit_hooks():
    erros = []
    if not os.path.isfile(PRE_COMMIT_SRC):
        erros.append("Fonte versionada do hook ausente: scripts/hooks/pre-commit.")
    else:
        with open(PRE_COMMIT_SRC, "r", encoding="utf-8") as f:
            content = f.read()
        
        gates_obrigatorios = [
            ("Gate 1 (Segredos R15)", "GATE 1"),
            ("Gate 2 (Testes R16)", "GATE 2"),
            ("Gate 3 (Sintaxe)", "GATE 4"),
            ("Gate 6 (Higiene R18)", "GATE 6"),
        ]
        for nome, tag in gates_obrigatorios:
            if tag not in content:
                erros.append(f"O hook pre-commit não contém {nome}.")

    # Checar se está copiado em .git/hooks/pre-commit
    if os.path.isdir(os.path.join(BASE_DIR, ".git")):
        if not os.path.isfile(PRE_COMMIT_GIT):
            erros.append("O hook não está instalado em .git/hooks/pre-commit.")

    return erros

def auditar_portabilidade_multi_ide():
    erros = []
    if not os.path.isfile(SETUP_WIN):
        erros.append("Script de portabilidade Windows ausente: scripts/setup-links.ps1.")
    if not os.path.isfile(SETUP_SH):
        erros.append("Script de portabilidade Linux/Mac ausente: scripts/setup-links.sh.")
    return erros

def auditar_camada_harness_completa():
    print("=" * 80)
    print(" 🔌 GATE MECÂNICO DA CAMADA 2: AUDITOR DO HARNESS (ORQUESTRAÇÃO & SEGURANÇA)")
    print("=" * 80)

    e1 = auditar_settings_json()
    e2 = auditar_pre_commit_hooks()
    e3 = auditar_portabilidade_multi_ide()

    total_erros = len(e1) + len(e2) + len(e3)

    if e1:
        print("\n [!] DESVIOS EM SETTINGS.JSON (DISJUNTORES & SANDBOX):")
        for err in e1: print(f"     ❌ {err}")

    if e2:
        print("\n [!] DESVIOS NO PRE-COMMIT HOOK:")
        for err in e2: print(f"     ❌ {err}")

    if e3:
        print("\n [!] DESVIOS NA PORTABILIDADE MULTI-IDE:")
        for err in e3: print(f"     ❌ {err}")

    print("\n" + "=" * 80)
    if total_erros == 0:
        print(" ✅ CAMADA 2 (HARNESS) 100% APROVADA: Circuit Breakers, Pre-Commit, Sandbox & Portabilidade!")
        print("=" * 80 + "\n")
        return 0
    else:
        print(f" ❌ REPROVADO: {total_erros} pendências para atingir 100% na Camada 2.")
        print("=" * 80 + "\n")
        return 1

if __name__ == "__main__":
    sys.exit(auditar_camada_harness_completa())
