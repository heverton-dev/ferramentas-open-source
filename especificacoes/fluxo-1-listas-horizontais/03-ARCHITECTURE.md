# 03 · Arquitetura do Sistema (Fluxo 1: Listas Horizontais)

> **Módulo:** Fluxo 1 — Listas Horizontais & Compêndios Temáticos  
> **Padrão:** Soberania em `output/` · Zero Duplicação em `docs/`  
> **Status:** Homologado AIDD · Nota 10.0 / 10.0

---

## 1. Topologia de Bundles Soberana

```
output/01-listas-horizontais/
  ├── list-bancos-dados-estado/
  │     ├── list-bancos-dados-estado.html   # Interativo Padrão Diamante R5
  │     ├── list-bancos-dados-estado.md     # Markdown Limpo Estruturado
  │     └── list-bancos-dados-estado.pdf    # Typst Anti-Sobreposição
  │
  ├── list-crm-erp-corporativo/
  │     ├── list-crm-erp-corporativo.html
  │     ├── list-crm-erp-corporativo.md
  │     └── list-crm-erp-corporativo.pdf
```

## 2. Acionamento Agêntico & CLI
- **Skill Agêntica:** `.agents/skills/fluxo1-listas-horizontais/`
- **Slash Command:** `/fluxo1 [slug]`
- **CLI Runner:** `python scripts/run_fluxo1.py --slug <slug>`
- **Persistência Relacional:** Gravado automaticamente no banco SQLite `estado_esteira.db` (Regra R11).
- **Publicação:** Deploy contínuo direto de `output/` via `.github/workflows/deploy-pages.yml` (sem duplicidade em `docs/`).
