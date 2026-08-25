# 🗺️ Mapa Geral de Engenharia: As 4 Camadas da Fábrica Agêntica

> **Registro Mestre de Arquitetura, Configuração e Replicação Holística.**  
> **Localização:** Raiz do Projeto (`4-camadas/00-MAPA-GERAL-E-STATUS.md`)  
> **Padrão Obrigatório de Registro:** Cada camada contém *Princípios Universais*, *O Que Foi Feito*, *Por Que Foi Feito*, *Onde Foi Feito*, *Como Foi Feito* e *Como Replicar*.

---

## 📊 Matriz de Maturidade das 4 Camadas

```text
CAMADA 1 [TELA]     ████████████████████ 100% ✅ (CONCLUÍDO & BLINDADO)
CAMADA 2 [HARNESS]  ████████████████████ 100% ✅ (CONCLUÍDO & BLINDADO)
CAMADA 3 [LLM]      ███░░░░░░░░░░░░░░░░░ 15%  (Próximo Foco)
CAMADA 4 [TOOLS]    █████████░░░░░░░░░░░ 45%  (Aguardando)
------------------------------------------------------------------
PROGRESSO GLOBAL    ██████████████░░░░░░ 65.0%
```

---

## 📋 Resumo Executivo das 4 Camadas

| Camada | Nome | Papel no Estúdio | Score | Status | Auditor Mecânico |
| :---: | :--- | :--- | :---: | :---: | :--- |
| **01** | **TELA** | O Mixer *(Prompt & Context)* | **100%** | **CONCLUÍDO** ✅ | `scripts/auditar_camada_tela.py` |
| **02** | **HARNESS** | A Segurança & Cabos *(Orquestração)* | **100%** | **CONCLUÍDO** ✅ | `scripts/auditar_camada_harness.py` |
| **03** | **LLM** | O Instrumento *(Model Layer)* | **15%** | **EM FOCO AGORA** | `scripts/auditar_camada_llm.py` *(a criar)* |
| **04** | **TOOLS** | Os Pedais & Efeitos *(MCP & Scripts)* | **45%** | Aguardando | `scripts/auditar_camada_tools.py` *(a criar)* |

---

## 📂 Índice dos Cadernos de Engenharia na Raiz:

* **[`00-CONTEXTO-DO-PROJETO.md`](00-CONTEXTO-DO-PROJETO.md):** O caso real de origem (Arsenal Open Source), por que foi feito assim e como transpor para SaaS, Consultorias e Pipelines de Dados.
* **[`01-CAMADA-TELA.md`](01-CAMADA-TELA.md):** Manual exaustivo da Camada 1 (100% Concluído).
* **[`02-CAMADA-HARNESS.md`](02-CAMADA-HARNESS.md):** Manual exaustivo da Camada 2 (100% Concluído).
* **[`03-CAMADA-LLM.md`](03-CAMADA-LLM.md):** Manual da Camada 3 (Em implementação).
* **[`04-CAMADA-TOOLS.md`](04-CAMADA-TOOLS.md):** Manual da Camada 4 (Em planejamento).
