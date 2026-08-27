# 07 · Modelagem Relacional SQLite (Fluxo 2: Dossiês Verticais)

> **Módulo:** Fluxo 2 — Dossiês Verticais de Desmantelamento SaaS  
> **Banco:** `estado_esteira.db` (Regra R11)

---

## 1. Schema da Tabela `esteira_dossies_verticais`

```sql
CREATE TABLE IF NOT EXISTS esteira_dossies_verticais (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    saas_slug TEXT NOT NULL UNIQUE,
    saas_nome TEXT NOT NULL,
    preco_anual_dolar REAL,
    quinteto_ferramentas TEXT NOT NULL,
    total_ferramentas INTEGER DEFAULT 5,
    gate_r5v TEXT DEFAULT 'APROVADO',
    gate_r18 TEXT DEFAULT 'APROVADO',
    caminho_html TEXT,
    caminho_md TEXT,
    caminho_pdf TEXT,
    atualizado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## 2. Métodos de Acesso

- `registrar_dossie_vertical(dados: dict)`: Insere ou atualiza o registro do dossiê no banco;
- `listar_dossies_verticais() -> list[dict]`: Retorna a listagem completa dos dossiês compilados.
