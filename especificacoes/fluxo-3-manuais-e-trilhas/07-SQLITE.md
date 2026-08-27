# 07 · Modelagem Relacional SQLite & Persistência de Estado (R11)

> **Módulo:** Esteira Autônoma de Ingestão de Fontes, Manuais VPS e Trilhas de Aprendizado  
> **Banco de Dados:** SQLite 3 (`estado_esteira.db`)  
> **Regra Mestre:** Regra R11 (Estado Persistente em Banco Relacional)  
> **Status:** Produção Homologada · Nota 10.0 / 10.0

---

## 1. Por que o Estado em Disco é Vital no AI-Driven Development?

Conversas com agentes de inteligência artificial são efêmeras: após o encerramento da sessão ou truncamento de contexto, a memória do modelo é zerada. Se o estado do projeto vivesse no chat, a fábrica não teria rastreabilidade, geraria retrabalho e desperdiçaria milhares de tokens a cada nova sessão.

A **Regra R11** determina que o banco relacional SQLite local (`estado_esteira.db`) seja a fonte única da verdade sobre quais ferramentas já foram processadas, quando foram geradas, quanto tempo levaram e quais gates foram aprovados.

---

## 2. Schema DDL da Tabela de Bundles da Esteira

O módulo adiciona ao `estado_esteira.db` a tabela especializada `esteira_manuais_bundles`:

```sql
CREATE TABLE IF NOT EXISTS esteira_manuais_bundles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    slug TEXT NOT NULL,
    saas_origem TEXT NOT NULL,
    data_execucao TEXT NOT NULL,
    horario_inicio TEXT,
    horario_fim TEXT,
    duracao_seg REAL,
    tokens_totais INTEGER,
    taxa_economia TEXT,
    gate_g0 TEXT,
    gate_g1 TEXT,
    gate_g2 TEXT,
    gate_r18 TEXT,
    total_arquivos INTEGER DEFAULT 9,
    caminho_bundle TEXT,
    atualizado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(slug, saas_origem)
);
```

### Dicionário de Dados dos Campos:

| Campo | Tipo | Descrição | Exemplo |
| :--- | :--- | :--- | :--- |
| `id` | INTEGER | Identificador único sequencial | `1` |
| `slug` | TEXT | Slug canônico curto da ferramenta | `screenpipe` |
| `saas_origem` | TEXT | SaaS desmantelado de referência | `granola` |
| `data_execucao` | TEXT | Data de emissão no formato DD-MM-YYYY | `27-08-2026` |
| `horario_inicio` | TEXT | Horário de disparo da esteira | `12:15:19` |
| `horario_fim` | TEXT | Horário de conclusão da esteira | `12:15:22` |
| `duracao_seg` | REAL | Tempo total de execução em segundos | `2.72` |
| `tokens_totais` | INTEGER | Volume de tokens consumidos na sessão | `6000` |
| `taxa_economia` | TEXT | Percentual de economia via determinismo | `~92% via Scripts Mecânicos` |
| `gate_g0` | TEXT | Resultado do Gate de Qualidade e Whitelist | `APROVADO` |
| `gate_g1` | TEXT | Resultado do Gate de Validação HTTP 200 | `APROVADO` |
| `gate_g2` | TEXT | Resultado do Gate de Citações Biunívocas | `APROVADO` |
| `gate_r18` | TEXT | Resultado da Auditoria de Higiene e Espelhos | `APROVADO` |
| `total_arquivos` | INTEGER | Total de artefatos no bundle | `9` |
| `caminho_bundle` | TEXT | Caminho relativo da pasta da ferramenta | `output/screenpipe/` |
| `atualizado_em` | TIMESTAMP | Carimbo de data/hora da última alteração | `2026-08-27 15:30:25` |

---

## 3. Consultas Analíticas & Auditoria de Estado

### Consulta 1: Listar Todos os Bundles Ativos no Repositório
```sql
SELECT 
    slug, 
    saas_origem, 
    duracao_seg || 's' as duracao, 
    gate_g0, gate_g1, gate_g2, gate_r18, 
    total_arquivos, 
    atualizado_em 
FROM esteira_manuais_bundles 
ORDER BY id ASC;
```

### Consulta 2: Auditoria de Conformidade dos 4 Gates
```sql
SELECT 
    COUNT(*) as total_processados,
    SUM(CASE WHEN gate_g0 = 'APROVADO' AND gate_g1 = 'APROVADO' AND gate_g2 = 'APROVADO' AND gate_r18 = 'APROVADO' THEN 1 ELSE 0 END) as total_100_aprovados
FROM esteira_manuais_bundles;
```

### Consulta 3: Verificar se uma Ferramenta já Foi Processada Hoje
```sql
SELECT slug, data_execucao, horario_fim, duracao_seg 
FROM esteira_manuais_bundles 
WHERE slug = 'screenpipe' AND data_execucao = '27-08-2026';
```

---

## 4. API de Integração Python (`scripts/estado_esteira.py`)

O script [`scripts/estado_esteira.py`](file:///C:/Users/trcnologia/orca/projects/open-source/scripts/estado_esteira.py) fornece funções convenientes com gerenciamento automático de conexões (`contextmanager`):

```python
from estado_esteira import registrar_bundle_esteira, listar_bundles_esteira

# Registrar um bundle
registrar_bundle_esteira({
    "slug": "screenpipe",
    "saas_origem": "granola",
    "data_execucao": "27-08-2026",
    "duracao_seg": 2.72,
    "tokens_totais": 6000,
    ...
})

# Consultar todos os bundles
bundles = listar_bundles_esteira()
```
