#!/usr/bin/env bash
# Script de sincronização periódica de todos os forks do arsenal-open-source
# Uso: bash scripts/sync-arsenal.sh

echo "=== SINCRONIZANDO REPOSITÓRIOS DO ARSENAL-OPEN-SOURCE ==="

gh repo list arsenal-open-source --fork --limit 500 --json nameWithOwner -q '.[].nameWithOwner' | while read -r repo; do
  echo "Sincronizando: $repo"
  if gh repo sync "$repo"; then
    echo "  ✓ OK"
  else
    echo "  ✗ Sem alterações upstream ou falha"
  fi
done

echo "Sincronização concluída!"
