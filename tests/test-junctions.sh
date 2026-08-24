#!/usr/bin/env bash
# Valida que os links de portabilidade multi-IDE existem E apontam para o alvo certo.
#
# Uso: bash tests/test-junctions.sh [raiz-do-projeto]
#
# Este teste so faz sentido DEPOIS de rodar scripts/setup-links.ps1|.sh.
# Em CI (checkout limpo, sem setup-links) ele sai com 0 e um aviso — links de
# portabilidade sao artefato de maquina local, nao conteudo versionado.
set -uo pipefail

raiz="${1:-$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)}"
cd "$raiz"

falhas=0
ok()    { echo "[OK]  $1"; }
falha() { echo "[X]   $1"; falhas=$((falhas + 1)); }

# Um link de ARQUIVO pode ser symlink (Unix) ou hardlink (Windows). Hardlink nao
# e detectavel por `-L`: o criterio de verdade e o conteudo ser identico.
checar_arquivo() {
  local espelho="$1" fonte="$2"
  if [ ! -e "$espelho" ]; then
    falha "ausente: $espelho"
    return
  fi
  if [ ! -e "$fonte" ]; then
    falha "fonte ausente: $fonte"
    return
  fi
  if cmp -s "$espelho" "$fonte"; then
    ok "$espelho == $fonte"
  else
    falha "DESALINHADO (link quebrado por rewrite externo): $espelho != $fonte"
  fi
}

# Pasta: junction (Windows) ou symlink (Unix). Em ambos os casos o conteudo
# precisa ser visivel atraves do espelho.
#
# `find -L` e obrigatorio: sem ele, `find` NAO entra no link e reporta 0 itens.
# No Git Bash uma junction do Windows aparece como symlink, entao o caso Windows
# cai exatamente nessa armadilha — o teste acusaria "vazio" num link saudavel.
checar_pasta() {
  local espelho="$1" fonte="$2"
  if [ ! -d "$espelho" ]; then
    falha "ausente: $espelho/"
    return
  fi
  local n_espelho n_fonte
  n_espelho=$(find -L "$espelho" -maxdepth 1 -mindepth 1 2>/dev/null | wc -l)
  n_fonte=$(find -L "$fonte" -maxdepth 1 -mindepth 1 2>/dev/null | wc -l)
  if [ "$n_espelho" -eq "$n_fonte" ]; then
    ok "$espelho/ -> $fonte/ ($n_fonte item(ns))"
  else
    falha "DESALINHADO: $espelho/ tem $n_espelho item(ns), $fonte/ tem $n_fonte"
  fi
}

echo "[*] Validando links de portabilidade em: $raiz"
echo

if [ ! -e agentic/skills ] && [ ! -e AGENTS.md ]; then
  echo "[!]   Nenhum link encontrado — setup-links ainda nao foi rodado."
  echo "      Rode: scripts/setup-links.ps1 (Win) ou bash scripts/setup-links.sh"
  echo "      (esperado em checkout limpo de CI; nao e falha)"
  exit 0
fi

echo "== Arquivos de instrucao =="
checar_arquivo "AGENTS.md"                        ".claude/CLAUDE.md"
[ -e .clinerules ] && checar_arquivo ".clinerules" ".claude/CLAUDE.md"
[ -e .windsurfrules ] && checar_arquivo ".windsurfrules" ".claude/CLAUDE.md"

echo
echo "== Pastas neutras =="
checar_pasta "agentic/skills"   ".claude/skills"
checar_pasta "agentic/agents"   ".claude/agents"
checar_pasta "agentic/commands" ".claude/commands"

echo
echo "== .agents/ (apenas agents e commands — nunca skills/mcp-servers) =="
[ -e .agents/agents ]   && checar_pasta ".agents/agents"   ".claude/agents"
[ -e .agents/commands ] && checar_pasta ".agents/commands" ".claude/commands"
if [ -e .agents/skills ] || [ -e .agents/mcp-servers ]; then
  falha ".agents/ expoe skills/ ou mcp-servers/ — o Codebuff executa .js/.mjs daqui e o CLI morre"
fi

echo
if [ "$falhas" -gt 0 ]; then
  echo "REPROVADO — $falhas falha(s). Recrie com scripts/setup-links.ps1|.sh"
  exit 1
fi
echo "Links validados"
exit 0
