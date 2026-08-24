#!/usr/bin/env bash
# Recria os links de portabilidade multi-IDE do projeto (macOS/Linux).
# Idempotente. Aqui symlink real de arquivo e de pasta funciona sem privilegio elevado,
# entao usamos symlink em todos os casos (equivalente ao hardlink+junction do Windows).
#
# Uso: bash scripts/setup-links.sh [nome-da-regra]
#      nome-da-regra = slug usado em .cursor/rules e .windsurf/rules (padrao: projeto)
#
# Universal: tudo que nao existir no projeto e PULADO com aviso, nunca com erro.
set -euo pipefail

raiz="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$raiz"

rule="${1:-projeto}"

link() {
  local alvo="$1" link="$2"
  if [ ! -e "$alvo" ]; then
    echo "AVISO: alvo nao encontrado, pulando: $alvo"
    return
  fi
  mkdir -p "$(dirname "$link")"
  if [ -L "$link" ]; then
    echo "OK (ja e symlink): $link"
    return
  fi
  if [ -e "$link" ]; then
    echo "AVISO: ja existe e NAO e symlink, pulando (apague manualmente se quiser recriar): $link"
    return
  fi
  ln -s "$(realpath --relative-to="$(dirname "$link")" "$alvo")" "$link"
  echo "Criado symlink: $link -> $alvo"
}

echo "== Fonte unica de governanca (.claude/CLAUDE.md -> CLAUDE.md da raiz) =="
# A fonte canonica e .claude/CLAUDE.md. O CLAUDE.md da raiz e o primeiro espelho —
# precisa existir antes dos demais, que sao linkados a partir dele.
link ".claude/CLAUDE.md" "CLAUDE.md"

echo
echo "== Arquivos de instrucao (symlink para CLAUDE.md) =="
link "CLAUDE.md" "AGENTS.md"
link "CLAUDE.md" ".cursor/rules/${rule}.mdc"
link "CLAUDE.md" ".windsurfrules"
link "CLAUDE.md" ".windsurf/rules/${rule}.md"
link "CLAUDE.md" ".clinerules"
link "CLAUDE.md" ".github/copilot-instructions.md"

echo
echo "== MCP (symlink para .mcp.json, schema compativel) =="
link ".mcp.json" ".cursor/mcp.json"

echo
echo "== Pastas neutras (symlink para .claude/...) =="
link ".claude/skills" "agentic/skills"
link ".claude/agents" "agentic/agents"
link ".claude/commands" "agentic/commands"
link ".claude/mcp-servers" "agentic/mcp-servers"

echo
echo "== Pastas .agents/ (symlink para .claude/..., harnesses alternativos) =="
# NAO expor skills/ e mcp-servers/ aqui: .agents/ e o diretorio de agentes do
# Codebuff/Freebuff, que importa e executa os .js/.mjs que encontra dentro dele.
# Um script que roda no import e chama process.exit(1) derruba o CLI inteiro.
# Apenas agents/ e commands/ (somente .md) sao seguros aqui.
# Skills e MCP servers seguem disponiveis via agentic/ e .opencode/.
link ".claude/agents" ".agents/agents"
link ".claude/commands" ".agents/commands"

echo
echo "== Pastas .opencode/ (symlink para .claude/..., OpenCode) =="
link ".claude/skills" ".opencode/skills"
link ".claude/agents" ".opencode/agents"
link ".claude/commands" ".opencode/commands"
link ".claude/mcp-servers" ".opencode/mcp-servers"
link ".claude/settings.json" ".opencode/settings.json"

echo
echo "== MCP traduzido (schemas diferentes, gerados por script — opcional) =="
# Estes sincronizadores sao ESPECIFICOS do projeto: se nao existirem, pula.
for sync in sincronizar-mcp-vscode.mjs sincronizar-mcp-opencode.mjs; do
  if [ -f "$raiz/scripts/$sync" ]; then
    if command -v node >/dev/null 2>&1; then
      node "$raiz/scripts/$sync"
    else
      echo "AVISO: node nao encontrado, pulando: $sync"
    fi
  else
    echo "Ausente (opcional), pulando: scripts/$sync"
  fi
done

echo
echo "== Hook pre-commit (R15/R16 - copia, .git/hooks nao aceita link) =="
if [ -f "$raiz/scripts/hooks/pre-commit" ] && [ -d "$raiz/.git" ]; then
  cp "$raiz/scripts/hooks/pre-commit" "$raiz/.git/hooks/pre-commit"
  chmod +x "$raiz/.git/hooks/pre-commit"
  echo "Copiado: scripts/hooks/pre-commit -> .git/hooks/pre-commit"
else
  echo "AVISO: hook ou .git ausente, pulando copia do pre-commit"
fi

echo
echo "Concluido."
