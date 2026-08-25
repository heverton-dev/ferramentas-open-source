# 🧠 Camada 3: LLM (Model Layer & Semantic Routing)

> **Papel no Estúdio:** O Músico e o Instrumento.  
> **Status:** 15% Implementado ➡️ **Meta: 100%**.  
> **Unidade de Trabalho:** Roteador Semântico de Modelos (Router/Proxy), Tiers de Modelos, Structured Outputs (JSON Schema / Pydantic) e Políticas de Amostragem.  
> **Localização:** `4-camadas/03-CAMADA-LLM.md`  
> **Auditor Mecânico:** `scripts/auditar_camada_llm.py` *(a ser criado)*

---

## 🏛️ Os Princípios Universais & Imutáveis da Camada LLM

A **Camada LLM** é a geradora de hipóteses probabilísticas. Ela opera sob três princípios imutáveis de inteligência de máquina:

### 1. Princípio do Roteamento por Pareto (*Capacidade vs Custo Exponencial*)
* **A Lei:** O custo financeiro e a latência de modelos de raciocínio profundo (*Frontier/Reasoning Models*) crescem exponencialmente em relação a modelos rápidos (*Flash/Mini/Haiku*), enquanto 80% das tarefas de engenharia (como formatação, busca de padrões e checagens sintáticas) não demandam raciocínio complexo.
* **Aplicação Prática:** A esteira divide o trabalho em **Tiers Semânticos**. Tarefas mecânicas rodam em modelos de baixo custo (Tier 1), reservando modelos pesados (Tier 3) estritamente para arquitetura crítica e refatoração profunda.

### 2. Princípio do Contrato Tipado Estrito (*Type Safety via Schema Enforcement*)
* **A Lei:** Modelos de linguagem geram texto probabilístico livre. Confiar em texto livre para acionar ferramentas ou alimentar bancos de dados resulta em falhas de interpretação (*JSON Parsing Errors*).
* **Aplicação Prática:** Todo fluxo que alimenta ferramentas ou scripts determinísticos deve forçar **Structured Outputs** via *JSON Schema / Pydantic*, garantindo tipagem estrita no nível do payload de saída do modelo.

### 3. Princípio da Contingência por Degradação Graciosa (*Fallback Resilience*)
* **A Lei:** Qualquer provedor de API de nuvem está sujeito a indisponibilidades, picos de latência ou bloqueios de taxa (*Rate Limit 429*).
* **Aplicação Prática:** A camada de LLM deve conter rotas de contingência automáticas para modelos alternativos (ex: Gemini Flash ➡️ Claude Haiku ➡️ Ollama Local) sem interromper a execução do fluxo.

---

## 1. O Que Foi Feito (Onde Estamos Hoje - 15%)

1. **Prompting de Compressão de Raciocínio (CoT):**
   * Redução de verbosidade interna via *Caveman Thinking*.
2. **Declaração de Modelo Livre:**
   * Regra R6 (`model: inherit`).

---

## 2. Por Que Foi Feito

* **A Dor Resolvida (Faturas Astronômicas):** Sem roteamento semântico, gasta-se modelos topo de linha para ler arquivos ou rodar comandos simples.
* **O Risco Mitigado (Falhas de Parsing):** Saídas não-estruturadas quebram scripts determinísticos downstream.

---

## 3. O Que Será Feito para Chegar aos 100%

1. **Matriz de Tiers de Modelos por Complexidade da Tarefa:**
   * **Tier 1 (Rápido / Barato):** Para buscas, grep, listagens e verificações.
   * **Tier 2 (Equilibrado):** Para código, testes e documentação.
   * **Tier 3 (Raciocínio Pesado):** Para decisões de arquitetura e resolução de bugs complexos.
2. **Structured Outputs com Schema Rígido:**
   * Definição de contratos JSON Schema para todas as ferramentas determinísticas.
3. **Gate Mecânico da Camada 3 (`scripts/auditar_camada_llm.py`):**
   * Script Python que valida os contratos de schema JSON e a configuração de tiers.

---

## 4. Onde Será Feito

* `scripts/tipos.py` (Registro declarativo com custo de LLM associado).
* `.claude/agents/` (Definição dos tiers de modelos de cada subagente).
* `scripts/auditar_camada_llm.py` (Gate mecânico).

---

## 5. Como Replicar o Que Foi Feito (Guia Passo a Passo)

*(Esta seção será preenchida com os comandos e códigos exatos assim que executarmos a implementação da Camada 3).*
