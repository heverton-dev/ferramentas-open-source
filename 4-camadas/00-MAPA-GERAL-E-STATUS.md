# 🗺️ Mapa Geral de Engenharia: As 4 Camadas da Fábrica Agêntica

> **Registro Mestre de Arquitetura, Configuração e Replicação Holística.**  
> **Localização:** Raiz do Projeto (`4-camadas/00-MAPA-GERAL-E-STATUS.md`)  
> **Padrão Obrigatório de Registro:** Para cada camada documentamos: *O Que Foi Feito*, *Por Que Foi Feito*, *Onde Foi Feito*, *Como Foi Feito* e *Como Replicar*.

---

## 📊 Matriz de Maturidade das 4 Camadas

```text
CAMADA 1 [TELA]     ████████████████████ 100% ✅ (CONCLUÍDO & BLINDADO)
CAMADA 2 [HARNESS]  ███████░░░░░░░░░░░░░ 35%  (Próximo Foco)
CAMADA 3 [LLM]      ███░░░░░░░░░░░░░░░░░ 15%  (Aguardando)
CAMADA 4 [TOOLS]    █████████░░░░░░░░░░░ 45%  (Aguardando)
------------------------------------------------------------------
PROGRESSO GLOBAL    ███████████░░░░░░░░░ 48.7%
```

---

## 📋 Resumo Executivo das 4 Camadas

| Camada | Nome | Papel no Estúdio | Score | O Que Entrega | Auditor Mecânico |
| :---: | :--- | :--- | :---: | :--- | :--- |
| **01** | **TELA** | O Mixer *(Prompt & Context)* | **100%** | Governança R1–R18, 5 skills de economia severa, orçamento de cache e vocabulário controlado. | `scripts/auditar_camada_tela.py` |
| **02** | **HARNESS** | A Segurança & Cabos *(Orquestração)* | **35%** | Pre-commit hook com 6 gates, portabilidade multi-IDE. *(Falta: settings.json, interceptores e travas de loop)*. | `scripts/auditar_camada_harness.py` *(em impl.)* |
| **03** | **LLM** | O Instrumento *(Model Layer)* | **15%** | Compressão de raciocínio CoT. *(Falta: Roteador de modelos por custo/complexidade e structured outputs JSON Schema)*. | `scripts/auditar_camada_llm.py` *(em impl.)* |
| **04** | **TOOLS** | Os Pedais & Efeitos *(MCP & Scripts)* | **45%** | Scripts determinísticos e auditor R18. *(Falta: Servidor MCP SQLite R11 e AST-grep nativo)*. | `scripts/auditar_camada_tools.py` *(em impl.)* |

---

## 📂 Índice dos Cadernos de Engenharia na Raiz:

* **[`00-CONTEXTO-DO-PROJETO.md`](00-CONTEXTO-DO-PROJETO.md):** O caso real de origem (Arsenal Open Source), por que foi feito assim e como transpor para SaaS, Consultorias e Pipelines de Dados.
* **[`01-CAMADA-TELA.md`](01-CAMADA-TELA.md):** Manual exaustivo da Camada 1 (100% Concluído).
* **[`02-CAMADA-HARNESS.md`](02-CAMADA-HARNESS.md):** Manual da Camada 2 (Em implementação).
* **[`03-CAMADA-LLM.md`](03-CAMADA-LLM.md):** Manual da Camada 3 (Em planejamento).
* **[`04-CAMADA-TOOLS.md`](04-CAMADA-TOOLS.md):** Manual da Camada 4 (Em planejamento).
