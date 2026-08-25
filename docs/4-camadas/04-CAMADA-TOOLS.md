# 🔧 Camada 4: TOOLS (MCP Servers & Deterministic Execution)

> **Papel no Estúdio:** Os Pedais de Efeitos, Instrumentos e Processadores.  
> **Status:** 45% Implementado ➡️ **Meta: 100%**.  
> **Unidade de Trabalho:** Servidores MCP (Model Context Protocol), Banco de Estado SQLite (R11), APIs externas e Scripts Python com saída determinística.

---

## 1. O Que É e Por Que Importa

A **Camada TOOLS** é o elo de ligação entre a inteligência abstrata do modelo e o mundo real (arquivos, banco de dados, terminal, git e web).
Quando a IA precisa fazer cálculos, validar regras de negócio ou consultar o histórico, **ela não deve alucinar**: deve chamar uma ferramenta tipada que executa a operação matematicamente no computador.

---

## 2. O Que Já Temos Implementado

1. **Usina de Scripts Determinísticos em `scripts/`:**
   * `auditar_higiene_repo.py` (Gate R18 com conferência de hash MD5).
   * `limpar_entulho.py` (Auto-saneamento idempotente).
   * `auditar_r5_dossie.py` (Auditor de estrutura DOM dos dossiês).
   * `setup-links.ps1` / `.sh` (Montador de portabilidade).
2. **Declaração de MCPs em `.mcp.json`:**
   * Configuração de servidores MCP padrão.

---

## 3. O Que Falta para Atingirmos 100% em TOOLS (Roadmap de Lapidação)

1. **Servidor MCP de Estado da Esteira em SQLite (Regra R11):**
   * Criar um banco de dados local SQLite estruturado (`estado_esteira.db`) e um servidor MCP que exponha ferramentas como `get_task_status`, `log_token_usage` e `register_artefact`.
2. **Ferramenta MCP de Análise de Código AST (`ast-grep`):**
   * Encapsular o `ast-grep` como uma tool nativa do agente para localizar estruturas sintáticas (funções, classes, imports) sem gastar contexto de leitura de texto puro.
3. **Validador Estrutural de Artefatos:**
   * Uma tool tipada que verifica instantaneamente se um arquivo HTML ou JSON gerado obedece ao schema sem precisar invocar uma LLM para revisão.
