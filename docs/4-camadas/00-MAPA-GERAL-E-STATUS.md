# 🗺️ Mapa Geral de Engenharia: As 4 Camadas da Fábrica Agêntica

> **Registro Mestre de Arquitetura, Configuração e Replicação Holística.**  
> **Objetivo:** Documentar cada configuração, técnica e script para que qualquer projeto (novo ou existente) possa atingir 100% de maturidade em AIDD (*AI-Driven Development*).

---

## 📊 Matriz de Maturidade das 4 Camadas

| Camada | Nome | Papel no Estúdio | Score Atual | Meta | Foco de Lapidação |
| :---: | :--- | :--- | :---: | :---: | :--- |
| **01** | **TELA** | O Mixer (Prompt & Context) | **95%** | **100%** | Governança R1–R18, 5 skills de economia e Padrão Diamante R5 já consolidados. |
| **02** | **HARNESS** | A Segurança & Cabos (Orquestração) | **35%** | **100%** | Interceptores de tool calls, hooks em `settings.json`, disjuntores de timeout e travas de loop. |
| **03** | **LLM** | O Instrumento (Model Layer) | **15%** | **100%** | Roteador de modelos por custo/complexidade, structured outputs (JSON Schema) e fallbacks. |
| **04** | **TOOLS** | Os Pedais & Efeitos (MCP & Scripts) | **45%** | **100%** | Servidor MCP de estado em SQLite (R11), AST-grep nativo e ferramentas determinísticas tipadas. |

---

## 📂 Estrutura do Caderno de Engenharia (`docs/4-camadas/`):

* **[`01-CAMADA-TELA.md`](01-CAMADA-TELA.md):** Como configurar a governança mestre (`CLAUDE.md`, `AGENTS.md`), as skills de economia severa e o padrão visual.
* **[`02-CAMADA-HARNESS.md`](02-CAMADA-HARNESS.md):** Como configurar o ADE, os hooks de ciclo de vida, permissões, sandbox e pre-commit.
* **[`03-CAMADA-LLM.md`](03-CAMADA-LLM.md):** Como configurar o roteamento semântico de modelos, structured outputs e políticas de amostragem.
* **[`04-CAMADA-TOOLS.md`](04-CAMADA-TOOLS.md):** Como configurar os servidores MCP, persistência de estado SQLite e scripts determinísticos.
