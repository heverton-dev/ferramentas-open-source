# 03 · Arquitetura do Sistema & Topologia Modular (Fluxo 2)

> **Módulo:** Fluxo 2 — Dossiês Verticais de Desmantelamento SaaS  
> **Padrão de Armazenamento:** Bundles Modulares em `output/dossies-verticais/`

---

## 1. Topologia de Diretórios dos Dossiês Verticais

```
output/dossies-verticais/
  ├── vert-granola/
  │     ├── vert-granola.html   ➔ Compêndio Interativo Diamante R5-V
  │     ├── vert-granola.md     ➔ Markdown Estruturado
  │     └── vert-granola.pdf    ➔ PDF Executivo via Typst
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

## 2. Regra de Paridade Estrita (R18)

Todos os bundles gerados em `output/dossies-verticais/vert-<saas>/` possuem cópia espelho idêntica em `docs/dossies-verticais/vert-<saas>/`. Adicionalmente, para retrocompatibilidade com compêndios legados, o arquivo HTML também é mantido em `output/listas-open-source/vert-<saas>.html` e `docs/listas/vert-<saas>.html`.
