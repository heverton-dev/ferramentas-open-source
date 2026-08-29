# 11 · Scripts & Automação (Fluxo 4: Macro-Ecossistemas)

> **Módulo:** Fluxo 4 — Macro-Ecossistemas e Suítes Integradas

---

## 1. Script Orquestrador Principal

Arquivo: `scripts/run_fluxo4.py`

```python
#!/usr/bin/env python3
"""
Orquestrador do Fluxo 4: Macro-Ecossistemas e Suítes Integradas
Entrada: slug do ecossistema
Saída: Bundle completo em output/04-ecossistemas/ecos-<slug>/
"""

import argparse
import sys
import logging
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description="Fluxo 4: Macro-Ecossistemas")
    parser.add_argument("--ecossistema", required=True, help="Slug do ecossistema")
    parser.add_argument("--verbose", action="store_true", help="Output detalhado")
    parser.add_argument("--force", action="store_true", help="Ignora cache")
    parser.add_argument("--profundo", action="store_true", help="Ativa subagentes")
    parser.add_argument("--sem-gates", action="store_true", help="Desativa gates")
    parser.add_argument("--apenas-gates", action="store_true", help="Apenas valida gates")
    
    args = parser.parse_args()
    
    # Setup logging
    log_level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(level=log_level, format="%(message)s")
    
    # Validação de entrada
    validador = EcossistemaValidator()
    data = validador.carregar_e_validar(args.ecossistema)
    
    if not data:
        sys.exit(1)
    
    # Apenas gates?
    if args.apenas_gates:
        auditor = AuditorGates()
        resultado_gates = auditor.validar_bundle(args.ecossistema)
        sys.exit(0 if resultado_gates["status"] == "ok" else 1)
    
    # Pipeline completo
    try:
        # Stage 1: Validação
        logger.info(f"[Stage 1] Validando ecossistema: {args.ecossistema}")
        
        # Stage 2: Síntese Arquitetural
        logger.info("[Stage 2] Construindo arquitetura...")
        grafo = DependencyGraph(data).build()
        diagramas = ArchitectureGenerator(grafo).gerar()
        tco = TCOCalculator(data).calcular()
        
        # Stage 3: Compilação
        logger.info("[Stage 3] Compilando documentação...")
        playbooks = PlaybookGenerator(grafo).gerar()
        docs = DocumentCompiler().compilar(data, grafo, diagramas, tco, playbooks)
        
        # Subagentes (opcional)
        if args.profundo:
            logger.info("[Stage 3+] Ativando subagentes (profundo)...")
            # pesquisador_componentes, auditor_seguranca, gerador_casosuso
        
        # Stage 4: Gates
        if not args.sem_gates:
            logger.info("[Stage 4] Validando gates...")
            auditor = AuditorGates()
            resultado_gates = auditor.validar(docs)
            if not resultado_gates["status"] == "ok":
                logger.error(f"Gates falharam: {resultado_gates}")
                sys.exit(3)
        
        # Persistência
        SQLitePersister().gravar(args.ecossistema, data, docs)
        
        logger.info(f"✓ SUCESSO: output/04-ecossistemas/ecos-{args.ecossistema}/")
        sys.exit(0)
    
    except Exception as e:
        logger.error(f"ERRO: {e}")
        sys.exit(2)

if __name__ == "__main__":
    main()
```

---

## 2. Scripts de Validação

### 2.1 `scripts/validar_fluxo4_specs.py`

```python
"""Valida integridade das specs de Fluxo 4"""

import os
from pathlib import Path

def validar():
    specs_dir = Path("especificacoes/fluxo-4-ecossistemas")
    
    # Verificar 12 arquivos obrigatórios
    required_files = [
        "00-PROPOSITO-E-VISAO-GERAL.md",
        "01-BLUEPRINT.md",
        "02-SPEC.md",
        "03-ARCHITECTURE.md",
        "04-AGENTS.md",
        "05-SUBAGENTS.md",
        "06-RULES.md",
        "07-SQLITE.md",
        "08-TESTES.md",
        "09-COMMANDS.md",
        "10-HOOKS.md",
        "11-SCRIPTS.md",
        "12-ESTUDO-DE-CASO-AIDD.md"
    ]
    
    for f in required_files:
        path = specs_dir / f
        if not path.exists():
            print(f"ERRO: {f} não encontrado")
            return False
        if path.stat().st_size < 100:
            print(f"AVISO: {f} muito pequeno")
    
    print("✓ Especificações de Fluxo 4 validadas")
    return True

if __name__ == "__main__":
    import sys
    sys.exit(0 if validar() else 1)
```

---

## 3. Scripts de Gates

### 3.1 `scripts/gates/gate1_integridade.sh`

```bash
#!/bin/bash
# Gate 1: Integridade de arquivos

SLUG=$1
DIR="output/04-ecossistemas/ecos-$SLUG"

if [ ! -d "$DIR" ]; then
  echo "Gate 1 FALHOU: Diretório $DIR não encontrado"
  exit 1
fi

ARQUIVO_COUNT=$(find "$DIR" -type f | wc -l)

if [ $ARQUIVO_COUNT -lt 15 ]; then
  echo "Gate 1 FALHOU: Apenas $ARQUIVO_COUNT arquivos (mínimo 15)"
  exit 1
fi

echo "Gate 1 OK: $ARQUIVO_COUNT arquivos"
exit 0
```

---

## 4. Scripts de Sincronização Multi-IDE

### 4.1 `scripts/setup-links-fluxo4.ps1`

```powershell
# Sincronizar specs de Fluxo 4 para .claude/ e .agents/

$source = "especificacoes/fluxo-4-ecossistemas"
$targets = @(".claude/fluxo-4", ".agents/fluxo-4")

foreach ($target in $targets) {
    Write-Host "Sincronizando $source -> $target"
    if (Test-Path $target) {
        Remove-Item $target -Recurse -Force
    }
    Copy-Item $source -Destination $target -Recurse -Force
    Write-Host "✓ $target atualizado"
}
```

---

## 5. Script de Backup/Restore SQLite

### 5.1 `scripts/backup-estado-esteira.sh`

```bash
#!/bin/bash
# Backup diário do estado_esteira.db

BACKUP_DIR="backups"
mkdir -p $BACKUP_DIR

DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_FILE="$BACKUP_DIR/estado_esteira_$DATE.sql"

sqlite3 estado_esteira.db ".dump" > "$BACKUP_FILE"
gzip "$BACKUP_FILE"

echo "✓ Backup: $BACKUP_FILE.gz"
```

---

## 6. Script de Estatísticas

### 6.1 `scripts/stats-fluxo4.py`

```python
"""Gera estatísticas de execução do Fluxo 4"""

import sqlite3
import json
from datetime import datetime, timedelta

def stats():
    db = sqlite3.connect("estado_esteira.db")
    cursor = db.cursor()
    
    # Ultimas 7 dias
    semana_atras = (datetime.now() - timedelta(days=7)).isoformat()
    
    cursor.execute("""
        SELECT
            DATE(timestamp_fim) as dia,
            COUNT(*) as total,
            SUM(CASE WHEN status = 'ok' THEN 1 ELSE 0 END) as sucesso,
            ROUND(AVG(duracao_segundos), 1) as media_duracao,
            ROUND(AVG(tokens_totais_gastos), 0) as media_tokens
        FROM esteira_ecossistemas
        WHERE timestamp_fim > ? AND status != 'em_progresso'
        GROUP BY DATE(timestamp_fim)
        ORDER BY dia DESC
    """, (semana_atras,))
    
    print("\n=== Estatísticas Fluxo 4 (Últimos 7 dias) ===\n")
    for row in cursor.fetchall():
        print(f"{row[0]}: {row[1]} total, {row[2]} OK, {row[3]}s avg, {row[4]} tokens avg")
    
    db.close()

if __name__ == "__main__":
    stats()
```

