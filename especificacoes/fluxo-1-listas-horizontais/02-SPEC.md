# 02 · Especificação Técnica (Fluxo 1: Listas Horizontais)

> **Módulo:** Fluxo 1 — Listas Horizontais & Compêndios Temáticos

---

## 1. Requisitos Funcionais Obrigatórios

- **RF01 (Taxonomia R13):** O nome do arquivo deve seguir rigorosamente `list-<slug-curto>.[html|md|pdf]`;
- **RF02 (Hero Stats Bar):** Obrigatório conter contadores de ferramentas, saas substituídos, licenças e stack;
- **RF03 (Busca Client-Side):** Input de busca com filtragem instantânea sem recarregar a página;
- **RF04 (Compilação Tripartite):** O compilador deve gerar HTML, MD e PDF;
- **RF05 (Persistência SQLite R11):** O registro deve ser gravado na tabela `esteira_listas_horizontais`.
