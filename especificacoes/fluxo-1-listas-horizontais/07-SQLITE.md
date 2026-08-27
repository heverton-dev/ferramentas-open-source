# 07 · Modelagem Relacional SQLite (Fluxo 1: Listas Horizontais)

> **Módulo:** Fluxo 1 — Listas Horizontais & Compêndios Temáticos  
> **Banco:** `estado_esteira.db` (Regra R11)

---

## 1. Schema da Tabela `esteira_listas_horizontais`

```sql
CREATE TABLE IF NOT EXISTS esteira_listas_horizontais (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    slug TEXT NOT NULL UNIQUE,
    titulo TEXT NOT NULL,
    total_ferramentas INTEGER NOT NULL,
    gate_r5 TEXT DEFAULT 'APROVADO',
    gate_r18 TEXT DEFAULT 'APROVADO',
    caminho_html TEXT,
    caminho_md TEXT,
    caminho_pdf TEXT,
    atualizado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## 2. Métodos de Acesso

- `registrar_lista_horizontal(dados: dict)`: Insere ou atualiza o compêndio temático no SQLite;
- `listar_listas_horizontais() -> list[dict]`: Lista todos os compêndios persistidos.
