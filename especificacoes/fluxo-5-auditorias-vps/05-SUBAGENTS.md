# 05 · Subagentes & Especialistas Auxiliares (Fluxo 5)

> **Módulo:** Fluxo 5 — Auditoria & Incorporação Cirúrgica em VPS

---

## 1. Subagentes Opcionais (Ativados com `--profundo`)

### 1.1 `pesquisador-vulnerabilidades`

**Responsabilidade:** Auditoria de CVEs em componentes

**Entrada:**
```json
{
  "containers": [
    {"nome": "ollama", "versao": "0.3.0", "imagem": "ollama:latest"}
  ]
}
```

**Saída:**
```json
{
  "vulnerabilidades": [
    {
      "cve_id": "CVE-2024-5678",
      "componente": "ollama",
      "severidade": "ALTA",
      "descricao": "RCE via desserialização",
      "versao_patched": "0.3.1"
    }
  ],
  "risk_score": 7.2
}
```

**Ação:** Gera seção "Análise de Segurança" no relatório.

---

### 1.2 `simulador-instalacao`

**Responsabilidade:** Simular deploy sem executar de verdade

**Entrada:** docker-compose.yml + estado atual

**Saída:**
```json
{
  "etapas": [
    {
      "etapa": 1,
      "acao": "pull ollama:0.3.0",
      "duracao_estimada_s": 120,
      "risco": "BAIXO",
      "rollback_possivel": true
    }
  ],
  "tempo_total_minutos": 15,
  "downtime_estimado_minutos": 2,
  "recomendacao": "Fazer em janela de manutenção 23:00-01:00"
}
```

**Ação:** Insere "Timeline de Instalação Estimada" no relatório.

---

### 1.3 `gerador-casos-uso`

**Responsabilidade:** Coletar deployments similares em produção

**Entrada:** slug do stack (ex: "ollama-langchain")

**Saída:**
```json
{
  "casos_uso": [
    {
      "empresa": "TechCorp",
      "tamanho": "500 employees",
      "versoes_utilizadas": {"ollama": "0.3.0", "langchain": "0.2.0"},
      "resultados": "Redução 60% tempo processamento",
      "lições": ["Allocate 16GB RAM minimum", "Use SSD storage"]
    }
  ]
}
```

**Ação:** Insere "Casos de Uso Reais" no relatório executivo.

---

## 2. Fluxo de Subagentes

```
├─ pesquisador-vulnerabilidades ────┐
├─ simulador-instalacao ────────────┼─→ enriquecer_relatorio()
├─ gerador-casos-uso ───────────────┘
```

Cada subagente roda **independentemente** via `parallel()`.

---

## 3. Configuração de Ativação

Em `especificacoes/fluxo-5-auditorias-vps/config.json`:

```json
{
  "subagentes_ativados": {
    "pesquisador_vulnerabilidades": true,
    "simulador_instalacao": true,
    "gerador_casos_uso": false
  }
}
```

---

## 4. Custo de Token Subagentes

| Subagente | Tokens Aprox. |
|-----------|---------------|
| pesquisador-vulnerabilidades | 2k (por container) |
| simulador-instalacao | 1.5k (por compose) |
| gerador-casos-uso | 5k (busca + síntese) |

Recomendação: Executar apenas se `--profundo` ou em CI/CD noturno.

