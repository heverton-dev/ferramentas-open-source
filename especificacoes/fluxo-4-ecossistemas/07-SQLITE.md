# 07 · Persistência SQLite (Fluxo 4: Macro-Ecossistemas)

> **Módulo:** Fluxo 4 — Macro-Ecossistemas e Suítes Integradas  
> **Regra:** R11 (Estado Persistente)

---

## 1. Tabela `esteira_ecossistemas`

```sql
CREATE TABLE IF NOT EXISTS esteira_ecossistemas (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  slug TEXT NOT NULL UNIQUE,
  nome TEXT NOT NULL,
  descricao TEXT,
  
  -- Metadados de Componentes
  componentes_json TEXT NOT NULL,  -- JSON array serializado
  versoes_json TEXT NOT NULL,       -- {"LangChain": "0.2.0", ...}
  arquitetura_tipo TEXT,            -- "3-layer", "microservices", etc
  
  -- Status & Execução
  status TEXT CHECK(status IN ('em_progresso', 'ok', 'erro_validacao', 'erro_compilacao', 'erro_gate')),
  mensagem_erro TEXT,
  timestamp_inicio DATETIME,
  timestamp_fim DATETIME,
  duracao_segundos INTEGER,
  
  -- LLM & Tokens
  modelo_llm TEXT,
  tokens_entrada INTEGER DEFAULT 0,
  tokens_saida INTEGER DEFAULT 0,
  tokens_totais_gastos INTEGER DEFAULT 0,
  
  -- Gates de Validação
  gate1_integridade INTEGER CHECK(gate1_integridade IN (0, 1)),
  gate2_validacao INTEGER CHECK(gate2_validacao IN (0, 1)),
  gate3_segredos INTEGER CHECK(gate3_segredos IN (0, 1)),
  gate4_metricas INTEGER CHECK(gate4_metricas IN (0, 1)),
  
  -- Hashes & Artefatos
  hash_livro_master TEXT,
  hash_bundle_completo TEXT,
  num_arquivos_gerados INTEGER,
  tamanho_total_mb REAL,
  
  -- Trilha de Auditoria
  usuario TEXT,
  ip_source TEXT,
  commit_hash_postado TEXT,
  
  CREATED_AT DATETIME DEFAULT CURRENT_TIMESTAMP,
  UPDATED_AT DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
```

---

## 2. Schema JSON para `componentes_json`

```json
[
  {
    "nome": "LangChain",
    "versao": "0.2.0",
    "url": "https://github.com/langchain-ai/langchain",
    "papel": "Orquestrador de LLMs e agentes",
    "licenca": "MIT",
    "conflitos_conhecidos": []
  },
  {
    "nome": "Ollama",
    "versao": "0.3.0",
    "url": "https://github.com/ollama/ollama",
    "papel": "Runtime de LLMs locais",
    "licenca": "MIT",
    "conflitos_conhecidos": ["CUDA < 11.8"]
  }
]
```

---

## 3. Queries Comuns

### Q1: Listar Ecossistemas Finalizados com Sucesso
```sql
SELECT slug, nome, timestamp_fim, duracao_segundos
FROM esteira_ecossistemas
WHERE status = 'ok'
ORDER BY timestamp_fim DESC
LIMIT 10;
```

### Q2: Ecossistemas em Progresso
```sql
SELECT slug, nome, timestamp_inicio, duracao_segundos
FROM esteira_ecossistemas
WHERE status = 'em_progresso'
  AND julianday(CURRENT_TIMESTAMP) - julianday(timestamp_inicio) > 300  -- 5 min
ORDER BY timestamp_inicio ASC;
```

### Q3: Taxa de Sucesso por Período
```sql
SELECT
  DATE(timestamp_fim) as data,
  COUNT(*) as total,
  SUM(CASE WHEN status = 'ok' THEN 1 ELSE 0 END) as sucesso,
  ROUND(100.0 * SUM(CASE WHEN status = 'ok' THEN 1 ELSE 0 END) / COUNT(*), 2) as taxa_pct
FROM esteira_ecossistemas
WHERE status != 'em_progresso'
GROUP BY DATE(timestamp_fim)
ORDER BY data DESC;
```

### Q4: Custo de Tokens Agregado
```sql
SELECT
  SUM(tokens_entrada) as total_entrada,
  SUM(tokens_saida) as total_saida,
  SUM(tokens_totais_gastos) as custo_total,
  COUNT(*) as num_execucoes,
  ROUND(AVG(tokens_totais_gastos), 0) as media_por_execucao
FROM esteira_ecossistemas
WHERE status = 'ok';
```

### Q5: Gates com Problemas
```sql
SELECT slug, nome, gate1_integridade, gate2_validacao, gate3_segredos, gate4_metricas
FROM esteira_ecossistemas
WHERE status = 'erro_gate'
  AND (gate1_integridade = 0 OR gate2_validacao = 0 OR gate3_segredos = 0);
```

---

## 4. Backup & Restore

### Backup Diário
```bash
sqlite3 estado_esteira.db ".dump" > backups/estado_esteira_$(date +%Y%m%d).sql
```

### Restore
```bash
sqlite3 estado_esteira.db < backups/estado_esteira_20260828.sql
```

---

## 5. Índices para Performance

```sql
CREATE INDEX IF NOT EXISTS idx_slug ON esteira_ecossistemas(slug);
CREATE INDEX IF NOT EXISTS idx_status ON esteira_ecossistemas(status);
CREATE INDEX IF NOT EXISTS idx_timestamp_fim ON esteira_ecossistemas(timestamp_fim DESC);
CREATE INDEX IF NOT EXISTS idx_usuario ON esteira_ecossistemas(usuario);
```

