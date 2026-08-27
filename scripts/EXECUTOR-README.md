# executor.js: Subagent Fork Wrapper com Cache

Wrapper determinístico para orquestar execução de fases via subagents com contexto cacheado.

## Features

- **Cache-First** (R11): Carrega contexto anterior de disco, evita recomputação.
- **Prompt Otimizado** (R0): 3-5 linhas core + arquivos relevantes, sem fluff.
- **Schema Validação** (R9): Valida phase spec antes de chamar subagent.
- **Idempotência** (R10): Cache + determinismo garantem execução repetível.
- **Exit Codes** (R9): `0` = sucesso, `1` = erro (pronto para gates).
- **JSON estruturado**: Entrada e saída sempre JSON válido.

## API

### `executePhase(phaseSpec, cachePath?)`

Executa uma fase orquestrando subagent.

**Entrada:**
```javascript
{
  phase_id: "phase-001",            // opcional (gerado se omitido)
  title: "Task Name",               // obrigatorio
  description: "What to do",        // obrigatorio
  tasks: [                          // obrigatorio, array nao-vazio
    { name: "task1", action: "create", target_path: "..." },
    { action: "execute", name: "run tests" }
  ],
  files: ["file1.js", "file2.py"],  // opcional, snippets adicionados ao prompt
  tests: ["npm test", "python check.py"]  // opcional
}
```

**Saída:**
```javascript
{
  status: "success" | "error",
  phase_id: "phase-001",
  changes: {
    files_modified: 2,
    files_created: 1,
    tests_passed: 3,
    gates_passed: 2
  },
  summary: "Fase executada com sucesso.",
  elapsed_ms: 450,
  cached: false,                    // true se usou cache
  timestamp: "2026-08-27T14:30:00Z",
  logs: ["[executor] phase_id=...", ...]
}
```

### `buildOptimizedPrompt(phaseSpec, previousContext?)`

Monta prompt telegráfico e estruturado.

**Entrada:**
```javascript
const prompt = buildOptimizedPrompt(
  {
    title: "Implement Feature",
    description: "Add new validator",
    tests: ["npm test"],
    files: ["lib/validator.js"],
    tasks: [...]
  },
  { previous_result: "..." }  // contexto anterior (opcional)
);
```

**Saída:**
```
# Phase: Implement Feature
Spec: Add new validator
Tests: npm test
Previous: {...cached context...}
Files:
```

### `ExecutorCache`

Gerenciador de cache em disco (SQLite-less, JSON-first).

```javascript
const cache = new ExecutorCache("cache/exec-cache.json");
cache.set("key", { data: "value" });
const cached = cache.get("key");  // { data: "value", timestamp: "..." }
```

## Uso

### CLI via arquivo

```bash
node scripts/executor.js --spec phase-spec.json --cache cache/exec.json
```

### CLI via stdin (pipes)

```bash
cat phase-spec.json | node scripts/executor.js > result.json
```

### Importar como módulo

```javascript
import { executePhase } from "./scripts/executor.js";

const result = await executePhase({
  title: "Build",
  description: "Compile and test",
  tasks: [...]
});

console.log(result.status);  // "success" ou "error"
```

## Exemplo Completo

### 1. Crie phase-spec.json

```json
{
  "phase_id": "phase-schema-001",
  "title": "Schema Validation",
  "description": "Validate implementation-plan.json schema",
  "tasks": [
    {
      "task_id": "task-001",
      "name": "Load schema",
      "action": "create",
      "target_path": "schema.json",
      "acceptance_criteria": ["File valid JSON"]
    },
    {
      "task_id": "task-002",
      "name": "Validate data",
      "action": "execute",
      "acceptance_criteria": ["No schema violations"]
    }
  ],
  "files": [
    "scripts/schemas/implementation-plan.json"
  ],
  "tests": [
    "npm test -- schema"
  ],
  "success_criteria": [
    "Schema validated",
    "All tasks completed"
  ]
}
```

### 2. Execute

```bash
node scripts/executor.js --spec phase-spec.json
```

### 3. Resultado

```json
{
  "status": "success",
  "phase_id": "phase-schema-001",
  "changes": {
    "files_modified": 0,
    "files_created": 0,
    "tests_passed": 1,
    "gates_passed": 1
  },
  "summary": "Fase executada com sucesso.",
  "elapsed_ms": 234,
  "cached": false,
  "timestamp": "2026-08-27T14:30:45.123Z",
  "logs": [
    "[executor] phase_id=phase-schema-001 title=\"Schema Validation\"",
    "[executor] cache miss para phase-schema-001:abc123",
    "[executor] prompt otimizado=380 chars",
    "[executor] subagent fork para phase phase-schema-001",
    "[executor] prompt size=380 chars"
  ]
}
```

## Integração com Gates (R9)

Usar em `implementation-plan.json`:

```json
{
  "gates": [
    {
      "gate_id": "gate-exec",
      "gate_name": "Executor Validation",
      "trigger_phase": 2,
      "validation_script": "node scripts/executor.js --spec phase-spec.json",
      "expected_exit_code": 0,
      "blocking": true,
      "timeout_seconds": 300
    }
  ]
}
```

## Integração com Cache (R11)

Cache é persistido automaticamente em `cache/executor-cache.json`:

```json
{
  "phase-001:abc123": {
    "context": { "previous_result": "..." },
    "phase_id": "phase-001",
    "spec_hash": "abc123",
    "timestamp": "2026-08-27T14:30:00Z"
  }
}
```

Próxima execução com mesmo `phase_id` + `spec_hash` reutiliza contexto (faster execution).

## Prompt Otimizado (R0)

Estrutura telegráfica (sem fluff):

```
# Phase: {{title}}
Spec: {{description}}
Tests: {{tests}}
Previous: {{contexto anterior (100 chars)}}
Files:

```file1.js
... (primeiros 200 chars) ...
```

Tasks:
  - task1: target/path
  - task2: global
```

Total: ~300-500 chars (mantém contexto dentro de budget de tokens).

## Validação (R9)

Schema mínimo obrigatório:

```javascript
{
  title: "string, required",
  description: "string, required",
  tasks: [
    {
      name: "string, required",
      action: "string, required",
      acceptance_criteria: ["string..."]
    }
  ]
}
```

Erros de validação retornam `status: "error"` + `exit 1`.

## Debugging

Adicione `--verbose` para logs detalhados (futuro):

```bash
node scripts/executor.js --spec phase-spec.json --verbose
```

Verifique cache:

```bash
cat cache/executor-cache.json | jq .
```

## Performance

- Cache hit: ~50ms
- Cache miss (subagent): ~200-500ms
- Total com gates: depende da complexidade da fase

## Roadmap

- [ ] Suporte a TaskCreate para fork real (hoje é mock)
- [ ] Retry logic com backoff exponencial
- [ ] Métricas e tracing (OpenTelemetry)
- [ ] Suporte a PostgreSQL para cache distribuído (R11 escalado)
