# StateManager — Gerenciador de Estado da Esteira

Módulo Node.js para rastreamento de tentativas de fases e histórico de execuções usando SQLite.

## Recursos

- **SQLite Persistente**: Estado salvo em `estado_esteira.db` (raiz do projeto)
- **Criação Automática**: Tabelas criadas na primeira execução
- **Histórico Completo**: Registra cada tentativa com score, gaps e resultado
- **Resumos Executivos**: Estatísticas por execução (run) e timeline
- **Exportação**: JSON ou queries diretas

## Instalação

```bash
npm install better-sqlite3
```

## Uso Básico

```javascript
import { StateManager } from './scripts/state-manager.js';

const sm = new StateManager();

// Registrar tentativa
sm.recordPhaseAttempt('run-001', 'phase-setup', 1, 95, [], 'success');

// Obter status atual
const status = sm.getPhaseStatus('run-001', 'phase-setup');

// Obter histórico completo
const history = sm.getPhaseHistory('run-001', 'phase-setup');

// Resumo da execução
const summary = sm.getRunSummary('run-001');

// Listar todas as execuções
const runs = sm.getAllRuns();

sm.close();
```

## API Completa

### `recordPhaseAttempt(runId, phaseId, attempt, score, gaps, result)`

Registra uma tentativa de fase.

**Parâmetros:**
- `runId` (string): Identificador da execução
- `phaseId` (string): Identificador da fase
- `attempt` (number): Número da tentativa (1, 2, 3...)
- `score` (number): Score obtido (0-100)
- `gaps` (array): Lista de problemas encontrados (opcional)
- `result` (string): 'success', 'partial', 'failed' (opcional)

**Retorna:**
```json
{ "ok": true, "attempt": 1, "score": 95, "status": "success" }
```

### `getPhaseStatus(runId, phaseId)`

Obtém o status atual de uma fase.

**Retorna:**
```json
{
  "lastAttempt": 2,
  "lastScore": 92,
  "status": "success",
  "updatedAt": "2026-08-27 14:46:14"
}
```

### `getPhaseHistory(runId, phaseId)`

Obtém o histórico completo de tentativas de uma fase.

**Retorna:** Array de objetos com `attempt`, `score`, `gaps`, `result`, `timestamp`

### `getAllRuns()`

Lista todas as execuções ordenadas por timestamp (mais recente primeiro).

**Retorna:** Array de `runId`

### `getRunSummary(runId)`

Resumo executivo de uma execução.

**Retorna:**
```json
{
  "runId": "run-001",
  "phaseCount": 3,
  "phases": [...],
  "stats": {
    "totalAttempts": 4,
    "averageScore": 90.67,
    "successfulPhases": 2,
    "successRate": 67
  },
  "timeline": [...]
}
```

### `cleanOldData(daysOld)`

Remove dados com mais de N dias.

**Parâmetros:**
- `daysOld` (number): Dias (padrão: 30)

**Retorna:** `{ "removed": 42, "daysOld": 30 }`

### `exportData(runId)`

Exporta dados em JSON.

**Parâmetros:**
- `runId` (string, opcional): Se omitido, exporta tudo

**Retorna:** Objeto com `attempts`, `status`, `exportedAt`

### `close()`

Fecha a conexão com o banco de dados.

## Estrutura do Banco

### Tabela: `phase_attempts`

```sql
CREATE TABLE phase_attempts (
  id INTEGER PRIMARY KEY,
  runId TEXT NOT NULL,
  phaseId TEXT NOT NULL,
  attempt INTEGER NOT NULL,
  score REAL NOT NULL,
  gaps TEXT,
  result TEXT NOT NULL,
  timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
  UNIQUE(runId, phaseId, attempt)
);
```

### Tabela: `phase_status`

```sql
CREATE TABLE phase_status (
  id INTEGER PRIMARY KEY,
  runId TEXT NOT NULL,
  phaseId TEXT NOT NULL,
  lastAttempt INTEGER NOT NULL,
  lastScore REAL NOT NULL,
  status TEXT NOT NULL,
  updatedAt DATETIME DEFAULT CURRENT_TIMESTAMP,
  UNIQUE(runId, phaseId)
);
```

## Configuração

Por padrão, o banco é criado em: `<raiz-projeto>/estado_esteira.db`

## Exemplo Completo

```javascript
import { StateManager } from './scripts/state-manager.js';

const sm = new StateManager();

// Simular 3 tentativas de uma fase
sm.recordPhaseAttempt('run-morning', 'validate-schema', 1, 65, ['missing-field'], 'failed');
sm.recordPhaseAttempt('run-morning', 'validate-schema', 2, 88, ['warn-nullable'], 'partial');
sm.recordPhaseAttempt('run-morning', 'validate-schema', 3, 100, [], 'success');

// Obter resumo
const summary = sm.getRunSummary('run-morning');
console.log(JSON.stringify(summary, null, 2));

sm.close();
```

## Integração com Orquestrador

O StateManager pode ser usado como MCP server ou integrado diretamente em scripts de orquestração para rastreamento automático de tentativas de fases.
