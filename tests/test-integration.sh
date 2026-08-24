#!/usr/bin/env bash
# Valida a integracao da fabrica-universal em um projeto consumidor.
#
# Uso: bash tests/test-integration.sh [raiz-do-projeto]
#      (padrao: raiz deste repositorio)
#
# Exit 0 = setup valido. Exit 1 = algo obrigatorio faltando.
set -uo pipefail

raiz="${1:-$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)}"
cd "$raiz"

falhas=0
avisos=0

ok()    { echo "[OK]  $1"; }
falha() { echo "[X]   $1"; falhas=$((falhas + 1)); }
aviso() { echo "[!]   $1"; avisos=$((avisos + 1)); }

echo "[*] Validando setup em: $raiz"
echo

# 1. CLAUDE.md com alwaysApply
if [ -f .claude/CLAUDE.md ]; then
  if grep -q "alwaysApply: true" .claude/CLAUDE.md; then
    ok "CLAUDE.md com 'alwaysApply: true'"
  else
    falha "CLAUDE.md sem 'alwaysApply: true' no frontmatter"
  fi
else
  falha ".claude/CLAUDE.md ausente"
fi

# 2. Skills de economia (as 5 sao obrigatorias)
for skill in caveman headroom lean-ctx rtk-memory pre-flight-check; do
  if [ -f ".claude/skills/$skill/SKILL.md" ]; then
    ok "skill: $skill"
  else
    falha "skill ausente: .claude/skills/$skill/SKILL.md"
  fi
done

# 3. Sintaxe Python de scripts/
if command -v python >/dev/null 2>&1; then
  if compgen -G "scripts/*.py" >/dev/null; then
    if python -m py_compile scripts/*.py 2>/dev/null; then
      ok "sintaxe Python (scripts/*.py)"
    else
      falha "erro de sintaxe em scripts/*.py"
    fi
  else
    aviso "nenhum .py em scripts/"
  fi
else
  aviso "python nao encontrado, pulando checagem de sintaxe"
fi

# 4. Scripts universais presentes
for s in setup-links.ps1 setup-links.sh validate.py; do
  if [ -f "scripts/$s" ]; then
    ok "script universal: $s"
  else
    falha "script universal ausente: scripts/$s"
  fi
done

# 5. Padroes reutilizaveis
for p in skill-template.md script-template.py command-template.md mcp-template.js; do
  if [ -f "scripts/padroes/$p" ]; then
    ok "padrao: $p"
  else
    falha "padrao ausente: scripts/padroes/$p"
  fi
done

# 6. Hook pre-commit (fonte obrigatoria; instalado e aviso)
if [ -f scripts/hooks/pre-commit ]; then
  ok "hook pre-commit (fonte versionada)"
else
  falha "scripts/hooks/pre-commit ausente"
fi
if [ -f .git/hooks/pre-commit ]; then
  ok "hook pre-commit (instalado)"
else
  aviso ".git/hooks/pre-commit ausente — rode scripts/setup-links.sh"
fi

# 7. Junctions/symlinks de portabilidade (aviso: exigem setup-links rodado)
if [ -e agentic/skills ]; then
  ok "portabilidade: agentic/skills"
else
  aviso "agentic/skills ausente — rode scripts/setup-links.sh|.ps1"
fi

echo
if [ "$falhas" -gt 0 ]; then
  echo "REPROVADO — $falhas falha(s), $avisos aviso(s)"
  exit 1
fi
echo "Setup validado — $avisos aviso(s)"
exit 0
