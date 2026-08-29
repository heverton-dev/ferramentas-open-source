# 07 · Persistência SQLite (Fluxo 5: Auditorias VPS)

> **Módulo:** Fluxo 5 — Auditoria & Incorporação Cirúrgica em VPS  
> **Regra:** R11 (Estado Persistente)

---

## 1. Tabela `esteira_auditorias_vps`

```sql
CREATE TABLE IF NOT EXISTS esteira_auditorias_vps (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  slug TEXT NOT NULL,
  portainer_url TEXT NOT NULL,
  portainer_endpoint_id INTEGER,
  
  -- Snapshot Infraestrutura
  snapshot_json TEXT NOT NULL,          -- Dados Portainer completos
  cpu_total_cores INTEGER,
  cpu_used_cores INTEGER,
  ram_total_gb INTEGER,
  ram_used_gb INTEGER,
  disco_total_gb INTEGER,
  disco_usado_gb INTEGER,
  
  -- Análise de Viabilidade
  componentes_json TEXT,                -- Array de componentes auditados
  viavel_install INTEGER CHECK(viavel_install IN (0, 1)),
  headroom_cpu_pct INTEGER,
  headroom_ram_pct INTEGER,
  headroom_disco_pct INTEGER,
  conflitos_detectados TEXT,            -- JSON de conflitos (portas, DNS)
  
  -- Status & Execução
  status TEXT CHECK(status IN ('em_progresso', 'ok', 'erro_auditoria', 'erro_compilacao', 'erro_gate')),
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
  gate4_conformidade INTEGER CHECK(gate4_conformidade IN (0, 1)),
  
  -- Artefatos Gerados
  hash_relatorio TEXT,
  hash_docker_compose TEXT,
  num_arquivos_gerados INTEGER,
  tamanho_total_mb REAL,
  
  -- Auditoria de Segurança
  usuario TEXT,
  ip_source TEXT,
  commit_hash_postado TEXT,
  
  CREATED_AT DATETIME DEFAULT CURRENT_TIMESTAMP,
  UPDATED_AT DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
```

---

## 2. Schema JSON para `snapshot_json`

```json
{
  "timestamp": "2026-08-28T15:30:00Z",
  "portainer_version": "2.20.1",
  "endpoint": {
    "os": "Ubuntu 22.04 LTS",
    "kernel": "6.1.0-20-generic",
    "docker_version": "24.0.6",
    "docker_api_version": "1.43",
    "uptime_seconds": 20476400
  },
  "resources": {
    "cpu": {"total_cores": 32, "used_cores": 18, "usage_percent": 56.2},
    "memory": {"total_mb": 262144, "used_mb": 140737.2, "usage_percent": 53.7},
    "disk": {"total_gb": 2000, "used_gb": 1200, "usage_percent": 60.0}
  },
  "containers": [
    {
      "id": "abc123",
      "name": "prometheus",
      "image": "prometheus:latest",
      "status": "running",
      "ports": [{"private": 9090, "public": 9090}]
    }
  ]
}
```

---

## 3. Queries Comuns

### Q1: Auditorias Viáveis Recentes
```sql
SELECT slug, viavel_install, headroom_cpu_pct, timestamp_fim
FROM esteira_auditorias_vps
WHERE status = 'ok' AND viavel_install = 1
ORDER BY timestamp_fim DESC LIMIT 10;
```

### Q2: Conflitos Detectados
```sql
SELECT slug, conflitos_detectados
FROM esteira_auditorias_vps
WHERE status = 'ok' AND conflitos_detectados IS NOT NULL
ORDER BY timestamp_fim DESC;
```

### Q3: Taxa de Sucesso
```sql
SELECT
  DATE(timestamp_fim) as dia,
  COUNT(*) as total,
  SUM(CASE WHEN status = 'ok' THEN 1 ELSE 0 END) as sucesso,
  ROUND(100.0 * SUM(CASE WHEN status = 'ok' THEN 1 ELSE 0 END) / COUNT(*), 2) as taxa_pct
FROM esteira_auditorias_vps
WHERE status != 'em_progresso'
GROUP BY DATE(timestamp_fim)
ORDER BY dia DESC;
```

---

## 4. Índices para Performance

```sql
CREATE INDEX IF NOT EXISTS idx_slug ON esteira_auditorias_vps(slug);
CREATE INDEX IF NOT EXISTS idx_status ON esteira_auditorias_vps(status);
CREATE INDEX IF NOT EXISTS idx_viavel ON esteira_auditorias_vps(viavel_install);
CREATE INDEX IF NOT EXISTS idx_timestamp ON esteira_auditorias_vps(timestamp_fim DESC);
```

