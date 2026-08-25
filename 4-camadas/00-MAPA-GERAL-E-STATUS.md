# 🗺️ Mapa Geral de Engenharia: As 4 Camadas da Fábrica Agêntica

> **Registro Mestre de Arquitetura, Configuração e Replicação Holística.**  
> **Localização:** Raiz do Projeto (`4-camadas/`)

---

## 📊 Matriz de Maturidade das 4 Camadas

| Camada | Nome | Papel no Estúdio | Score Atual | Meta | Status / Próxima Ação |
| :---: | :--- | :--- | :---: | :---: | :--- |
| **01** | **TELA** | O Mixer (Prompt & Context) | **100%** | **100%** | **CONCLUÍDO & BLINDADO** ✅ (Gate: `auditar_camada_tela.py`) |
| **02** | **HARNESS** | A Segurança & Cabos (Orquestração) | **35%** | **100%** | **EM FOCO AGORA:** `settings.json`, interceptores e disjuntores. |
| **03** | **LLM** | O Instrumento (Model Layer) | **15%** | **100%** | Roteador de modelos por custo/complexidade e structured outputs. |
| **04** | **TOOLS** | Os Pedais & Efeitos (MCP & Scripts) | **45%** | **100%** | Servidor MCP de estado em SQLite (R11) e ferramentas tipadas. |

---

## 📂 Arquivos Deste Caderno de Engenharia na Raiz:

* **[`01-CAMADA-TELA.md`](01-CAMADA-TELA.md):** 100% Concluído e documentado.
* **[`02-CAMADA-HARNESS.md`](02-CAMADA-HARNESS.md):** Diagnóstico e passo a passo de lapidação da Camada 2.
* **[`03-CAMADA-LLM.md`](03-CAMADA-LLM.md):** Diagnóstico e passo a passo de lapidação da Camada 3.
* **[`04-CAMADA-TOOLS.md`](04-CAMADA-TOOLS.md):** Diagnóstico e passo a passo de lapidação da Camada 4.
