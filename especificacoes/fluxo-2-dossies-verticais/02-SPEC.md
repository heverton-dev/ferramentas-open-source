# 02 · Especificação Técnica & Contratos JSON (Fluxo 2)

> **Módulo:** Fluxo 2 — Dossiês Verticais de Desmantelamento SaaS  
> **Contrato Canônico:** `scripts/schemas/dossie_vertical.schema.json`

---

## 1. Requisitos Funcionais Obrigatórios

- **RF01 (Quinteto Soberano):** Todo arquivo de entrada DEVE conter exatamente 5 ferramentas ranqueadas de 1 a 5;
- **RF02 (Classificações Canônicas):** O campo `classificacao` deve ser uma das 5 strings exatas:
  - `A Mais Robusta`
  - `A Mais Completa`
  - `A Mais Moderna`
  - `A Mais Leve`
  - `A Mais Simples`
- **RF03 (Seção 5: White-Label):** Cada ferramenta DEVE conter o objeto `design_system` com `esforco`, `stack_ui` e `mecanica_customizacao`;
- **RF04 (Seção 6: MCPs & Skills):** Cada ferramenta DEVE conter um array `uso_complementar` com ao menos 1 servidor MCP ou Agent Skill funcional;
- **RF05 (Compilação Tripartite):** O compilador deve gerar HTML, MD e PDF com zero intervenção manual;
- **RF06 (Persistência SQLite R11):** O registro do dossiê deve ser gravado na tabela `esteira_dossies_verticais`.
