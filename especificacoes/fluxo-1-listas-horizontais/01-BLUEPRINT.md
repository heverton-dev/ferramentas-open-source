# 01 · Blueprint de Engenharia (Fluxo 1: Listas Horizontais)

> **Módulo:** Fluxo 1 — Listas Horizontais & Compêndios Temáticos  
> **Arquitetura:** Esteira Determinística Tripartite com Gate R5 e SQLite R11

---

## 1. Diagrama de Fluxo de Dados

```mermaid
flowchart TD
    A["Entrada: Dados da Camada Temática (ex: Bancos de Dados)"] --> B["Normalizador Diamante (normalizar_compendio.py)"]
    B --> C["Compilador Tripartite (gerar_lista_horizontal_tripartite.py)"]
    
    subgraph S1 ["Geração Tripartite Modular"]
        C --> D["HTML Interativo (list-slug.html)"]
        C --> E["Markdown Limpo Estruturado (list-slug.md)"]
        C --> F["PDF Executivo Typst (list-slug.pdf)"]
    end

    subgraph S2 ["Auditoria & Persistência"]
        D --> G["Gate Mecânico R5 (auditar_r5_dossie.py)"]
        G -->|Aprovado| H["Registro na Tabela SQLite (esteira_listas_horizontais)"]
        H --> I["Espelhamento Estrito R18 em docs/"]
    end
```

---

## 2. Matriz de Componentes e Responsabilidades

| Componente | Tipo | Responsabilidade Principal | Saída Primária |
| :--- | :--- | :--- | :--- |
| `normalizar_compendio.py` | Compilador | Normaliza HTMLs legados no Padrão Diamante R5 | HTML estruturado |
| `gerar_lista_horizontal_tripartite.py` | Compilador | Gera simultaneamente HTML, MD e Typst PDF | `output/listas-tematicas/list-<slug>/*` |
| `auditar_r5_dossie.py` | Gate R5 | Valida Hero Stats, busca client-side e cards | Retorno `exit 0` ou `exit 1` |
| `test_fluxo1_listas.py` | Testes | Suíte de testes unitários automatizados | 5 testes passando em <1s |
| `estado_esteira.py` | Persistência | Registra histórico na tabela `esteira_listas_horizontais` | `estado_esteira.db` |
