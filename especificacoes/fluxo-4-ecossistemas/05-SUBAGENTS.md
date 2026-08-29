# 05 · Subagentes & Especialistas Auxiliares (Fluxo 4)

> **Módulo:** Fluxo 4 — Macro-Ecossistemas e Suítes Integradas

---

## 1. Subagentes Opcionais (Ativados com `--profundo`)

### 1.1 `pesquisador-componentes`

**Responsabilidade:** Enriquecer metadados de cada componente

**Entrada:**
```json
{
  "componentes": [
    {"nome": "LangChain", "url": "https://github.com/..."}
  ]
}
```

**Saída:**
```json
{
  "componentes_enriquecidos": [
    {
      "nome": "LangChain",
      "github_stars": 95000,
      "last_commit": "2026-08-27",
      "community_size": 5000,
      "maturity_score": 9.5,
      "trending": "estável"
    }
  ]
}
```

**Ação:** Gera leaderboard no HTML + badge de "Maduridade".

---

### 1.2 `auditor-seguranca`

**Responsabilidade:** Auditoria de CVEs e vulnerabilidades

**Entrada:** Lista de componentes com versões

**Saída:**
```json
{
  "vulnerabilidades": [
    {
      "componente": "LangChain",
      "versao": "0.2.0",
      "cve_id": "CVE-2024-1234",
      "severidade": "ALTA",
      "descricao": "RCE via injection de prompt",
      "versao_patched": "0.2.1"
    }
  ],
  "risk_score": 6.8
}
```

**Ação:** Gera seção de "Auditoria de Segurança" com recomendações.

---

### 1.3 `gerador-casosuso`

**Responsabilidade:** Coletar deployments reais em produção

**Entrada:** Slug do ecossistema

**Saída:**
```json
{
  "casos_uso": [
    {
      "empresa": "TechCorp",
      "tamanho": "5000 employees",
      "componentes_adotados": ["LangChain", "Ollama"],
      "timeline": "3 meses",
      "resultados": "Redução 40% de custo com IA",
      "lessons_learned": ["Não comprem memória mínima, scale up"]
    }
  ]
}
```

**Ação:** Insere seção "Casos de Uso" na documentação.

---

## 2. Fluxo de Subagentes

```
├─ pesquisador-componentes ──┐
├─ auditor-seguranca ────────┼─→ enriquecer_documentacao()
├─ gerador-casosuso ────────┐
```

Cada subagente roda **independentemente** via `parallel()` (sem wait barrier entre eles).

---

## 3. Configuração de Ativação

No arquivo `especificacoes/fluxo-4-ecossistemas/config.json`:

```json
{
  "subagentes_ativados": {
    "pesquisador_componentes": true,
    "auditor_seguranca": true,
    "gerador_casosuso": false
  }
}
```

---

## 4. Custo de Token Subagentes

| Subagente | Tokens Aprox. |
|-----------|---------------|
| pesquisador-componentes | 2k (por componente) |
| auditor-seguranca | 3k (varredura NVD) |
| gerador-casosuso | 5k (busca + síntese) |

Recomendação: Executar subagentes apenas se `--profundo` ou em CI/CD noturno.

