# 🧠 Camada 3: LLM (Model Layer & Semantic Routing)

> **Papel no Estúdio:** O Músico e o Instrumento.  
> **Status:** 15% Implementado ➡️ **Meta: 100%**.  
> **Unidade de Trabalho:** Roteador Semântico de Modelos (Router/Proxy), Tiers de Modelos, Structured Outputs (JSON Schema / Pydantic) e Políticas de Amostragem.  
> **Localização:** `4-camadas/03-CAMADA-LLM.md`

---

## 1. O Que É e Por Que Importa

A **Camada LLM** cuida do motor cognitivo em si. Não adianta ter ótimas regras na TELA se usamos um modelo "canhão" caríssimo (ex: Claude 3.7 / GPT-4o) para tarefas mecânicas que um modelo ultrarrápido (ex: Flash / Haiku) faria por 1% do custo.
Também não adianta pedir JSON se o modelo responder com texto livre e quebrar o script downstream.

---

## 2. O Que Já Temos Implementado

1. **Prompting de Compressão de Raciocínio (CoT):**
   * Redução de verbosidade interna via *Caveman Thinking*.
2. **Declaração de Modelo Livre:**
   * Regra R6 (`model: inherit`).

---

## 3. O Que Falta para Atingirmos 100% no LLM (Roadmap de Lapidação)

1. **Matriz de Tiers de Modelos por Complexidade da Tarefa:**
   * **Tier 1 (Rápido / Barato - Flash / Haiku / Mini):** Usado para leituras de arquivo, pesquisas de grep, conferência de sintaxe e listagem de diretórios.
   * **Tier 2 (Equilibrado - Sonnet / GPT-4o):** Usado para geração de código, edição de fichas e escrita de testes.
   * **Tier 3 (Raciocínio Pesado - Pro / Opus / Reasoning):** Usado exclusivamente para decisões de arquitetura e resolução de bugs complexos.
2. **Structured Outputs com Schema Rígido:**
   * Definição de contratos JSON Schema para todas as ferramentas determinísticas que recebem dados do agente, eliminando 100% dos erros de parsing.
3. **Políticas de Fallback Automático:**
   * Se o modelo principal sofrer *Rate Limit* (HTTP 429) ou indisponibilidade, chavear automaticamente para o modelo de contingência sem derrubar o desenvolvedor.
