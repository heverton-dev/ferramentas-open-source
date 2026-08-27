# 03 · Arquitetura do Sistema & Topologia Modular (Fluxo 2)

> **Módulo:** Fluxo 2 — Dossiês Verticais de Desmantelamento SaaS  
> **Padrão:** Soberania em `output/` · Zero Duplicação em `docs/`  
> **Status:** Homologado AIDD · Nota 10.0 / 10.0

---

## 1. Topologia Soberana dos Dossiês Verticais

```
output/02-dossies-verticais/
  ├── vert-granola/
  │     ├── vert-granola.html   ➔ Compêndio Interativo Diamante R5-V
  │     ├── vert-granola.md     ➔ Markdown Estruturado Limpo
  │     └── vert-granola.pdf    ➔ PDF Executivo via Typst (Anti-Sobreposição)
  │
  ├── vert-notion/
  │     ├── vert-notion.html
  │     ├── vert-notion.md
  │     └── vert-notion.pdf
  │
  └── vert-salesforce/
        ├── vert-salesforce.html
        ├── vert-salesforce.md
        └── vert-salesforce.pdf
```

## 2. Acionamento Agêntico & CLI
- **Skill Agêntica:** `.agents/skills/fluxo2-dossies-verticais/`
- **Slash Command:** `/fluxo2 [saas]`
- **CLI Runner:** `python scripts/run_fluxo2.py --saas <saas>`
- **Persistência Relacional:** Gravado no banco SQLite `estado_esteira.db` (Regra R11).
- **Publicação:** Deploy contínuo direto de `output/` via GitHub Actions (`deploy-pages.yml`).
