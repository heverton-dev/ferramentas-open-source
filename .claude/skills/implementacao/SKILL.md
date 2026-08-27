---
name: implementacao
description: >
  Orquestrador determinístico de implementação com ciclo Implementa, Testa, Valida, Verifica.
license: MIT
version: 1.0.0
---

# /implementacao Skill — Multi-Phase Token-Optimized Implementation

Orquestrador determinístico de implementação com ciclo **Implementa → Testa → Valida → Verifica**.

## Uso

```bash
/implementacao <plan-json-path> [--max-retries N]
```

- `<plan-json-path>`: Caminho absoluto para JSON estruturado com fases de implementação
- `--max-retries N`: Número máximo de tentativas por fase (padrão: 3)

## O Ciclo: Implementa → Testa → Valida → Verifica

### Fase 1: Implementa
- Executa tarefa conforme especificado no plano
- Gera artefato intermediário (código, config, documento)
- Registra checksum SHA256 em `estado_esteira.db`
- **Falha mecânica?** → Escalate para humano com gap list

### Fase 2: Testa
- Executa suite de testes fornecida (`test_command`, `coverage_min`)
- Coleta cobertura, retorno de exit code, logs truncados (RTK)
- **Coverage < limite?** → Reexecuta até limite ou max-retries
- **Timeout?** → Escalate com trace

### Fase 3: Valida
- Executa validators mecânicos (`gate_command`)
- Exemplo: `python scripts/auditar_r5_dossie.py`
- **Exit 0** → Fase válida, segue adiante
- **Exit 1** → Registra gaps, reexecuta Implementa até sucesso

### Fase 4: Verifica
- Checagem final determinística (hash, paridade, espelhos)
- Confirma R18 (zero entulho, paridade de espelhos)
- Segue para auto-commit + push conforme R10

## Input Schema (JSON)

```json
{
  "plan_id": "impl-2026-08-27-001",
  "title": "Gerar dossié vertical Notion com Quinteto",
  "phases": [
    {
      "id": "impl",
      "name": "Implementação",
      "task": {
        "command": "python scripts/gerar_dossie_vertical.py --saas notion --output output/vert-notion.html",
        "timeout_ms": 30000,
        "expected_outputs": ["output/vert-notion.html"]
      },
      "retry_on_missing_outputs": true
    },
    {
      "id": "test",
      "name": "Testes",
      "task": {
        "test_command": "python -m pytest tests/test_vert_notion.py -v",
        "coverage_min": 85,
        "timeout_ms": 15000
      }
    },
    {
      "id": "validate",
      "name": "Validação Mecânica",
      "task": {
        "gate_command": "python scripts/auditar_tipo_vertical.py output/vert-notion.html",
        "timeout_ms": 10000
      }
    },
    {
      "id": "verify",
      "name": "Verificação Final",
      "task": {
        "verify_command": "python scripts/limpar_entulho.py --check-only",
        "timeout_ms": 5000,
        "git_commit": true,
        "git_message": "feat(vert): adicionar dossiê vertical Notion com Quinteto Soberano"
      }
    }
  ]
}
```

## Output

A cada fase completada:

```
Phase 1 completed (score: 100%) | artefato: output/vert-notion.html | checksum: a3f2e1d4c...
Phase 2 completed (score: 92%) | coverage: 92% | test_pass_rate: 100%
Phase 3 completed (score: 100%) | gates_passed: 2/2 | audit_warnings: 0
Phase 4 completed (score: 100%) | verified_hashes: 5/5 | commit: abc123def...
```

Escalação:

```
Phase 1 escalated (score: 45%) | gaps: ["output/vert-notion.html não gerado", "timeout em 30s"] | retry_count: 3/3
```

## Exemplo End-to-End: 3 Fases

**Entrada:**
```json
{
  "plan_id": "test-impl-001",
  "title": "Implementar skill RTK",
  "phases": [
    {
      "id": "impl",
      "name": "Implementação",
      "task": {
        "command": "echo 'Gerando skill...' && mkdir -p skills/rtk && echo 'module.exports = {}' > skills/rtk/index.js",
        "timeout_ms": 5000,
        "expected_outputs": ["skills/rtk/index.js"]
      }
    },
    {
      "id": "test",
      "name": "Testes",
      "task": {
        "test_command": "node -c skills/rtk/index.js && echo 'OK'",
        "coverage_min": 0,
        "timeout_ms": 5000
      }
    },
    {
      "id": "verify",
      "name": "Verificação",
      "task": {
        "verify_command": "ls -la skills/rtk/index.js",
        "git_commit": false
      }
    }
  ]
}
```

**Execução:**
```
[implementacao] Iniciando plano test-impl-001
[impl] Executando: echo 'Gerando skill...'...
[impl] Output: Gerando skill...
[impl] ✓ Arquivo criado: skills/rtk/index.js
Phase 1 completed (score: 100%)

[test] Executando: node -c skills/rtk/index.js...
[test] Output: OK
Phase 2 completed (score: 100%)

[verify] Checando integridade...
Phase 3 completed (score: 100%)

✓ Plano test-impl-001 concluído com sucesso (3/3 fases)
```

## Troubleshooting

### Score < 100% em Implementação

Causas comuns:
- **Timeout**: Aumentar `timeout_ms` ou simplificar comando
- **Missing outputs**: Verificar paths absolutos e permissões
- **Encoding**: Em Windows, Python precisa de `sys.stdout.reconfigure(encoding="utf-8")`

Ação: Escalate para humano com lista de gaps + última tentativa de log

### Coverage Insuficiente

- Reexecuta testes até `coverage_min` ou `max-retries` (3×)
- Se falha, registra em banco (`estado_esteira.db`) e marca fase como "pendente"
- Próxima execução pode retomar ou ser marcada como bloqueador

### Gate Mecânico Falha (Exit 1)

- Escalate imediato com saída de stderr
- **Exemplo**: `auditar_r5_dossie.py` detecta layout com 2 colunas → escalate
- Humano corrige, reexecuta /implementacao com mesmo plan_id → retoma Fase 3

## Estado Persistente (R11)

Todas as fases registram em SQLite (`estado_esteira.db`):

```sql
INSERT INTO implementacao_log 
  (plan_id, phase_id, status, score, timestamp, checksum, git_commit)
VALUES 
  ('impl-2026-08-27-001', 'impl', 'COMPLETED', 100, 1693123456, 'a3f2e1...', NULL);
```

Permite resumir, auditar e rastrear cada tentativa.

## Referências Internas

- **R8 (Determinismo)**: Scripts em Python resolvem; LLM não é gasto
- **R9 (Gates Mecânicos)**: Cada gate retorna `exit 0` (sucesso) ou `exit 1` (erro)
- **R10 (Idempotência)**: Reexecução N× com mesmo resultado
- **R11 (Estado em Disco)**: SQLite persiste estado, nunca volátil
- **R16 (Pós-implementação)**: 100% → commit + push; <100% → escalate
- **R18 (Higiene)**: Verificação final garante zero entulho e paridade de espelhos

## Fallback Terminal

Se sandbox bloquear execução de comando:

```
Fallback: Execute manualmente:
$ python scripts/gerar_dossie_vertical.py --saas notion --output output/vert-notion.html
$ python -m pytest tests/test_vert_notion.py -v
$ python scripts/auditar_tipo_vertical.py output/vert-notion.html
```

Cole o output no chat para o skill validar.
