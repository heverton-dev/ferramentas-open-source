# 🔧 Camada 4: TOOLS (MCP Servers & Deterministic Execution)

> **Papel no Estúdio:** Os Pedais de Efeitos, Instrumentos e Processadores.  
> **Status:** 45% Implementado ➡️ **Meta: 100%**.  
> **Unidade de Trabalho:** Servidores MCP (Model Context Protocol), Banco de Estado SQLite (R11), APIs externas e Scripts Python com saída determinística.  
> **Localização:** `4-camadas/04-CAMADA-TOOLS.md`  
> **Auditor Mecânico:** `scripts/auditar_camada_tools.py` *(a ser criado)*

---

## 🏛️ Os Princípios Universais & Imutáveis da Camada TOOLS

A **Camada TOOLS** é a âncora determinística da Fábrica. Ela é governada por três princípios imutáveis de engenharia de software:

### 1. Princípio da Separação de Responsabilidades (*LLM Pensa, Tool Executa*)
* **A Lei:** Modelos de linguagem são motores estocásticos (probabilísticos); eles são péssimos em matemática exata, contagem precisa, manipulação de binários e validação criptográfica. Ferramentas determinísticas de computador são perfeitas nessas tarefas.
* **Aplicação Prática:** A IA nunca deve tentar adivinhar a quantidade de itens, calcular hashes ou validar regras em prosa. Ela deve invocar uma ferramenta (*script / MCP tool*) e apenas interpretar o código de retorno binário (`exit 0/1`).

### 2. Princípio da Idempotência Algorítmica (*f(f(x)) = f(x)*)
* **A Lei:** Qualquer ferramenta ou script de saneamento deve produzir o mesmo estado final estável se for executado 1 vez ou 1.000 vezes consecutivas, sem gerar efeitos colaterais cumulativos ou corromper o disco.
* **Aplicação Prática:** O script `scripts/limpar_entulho.py` pode ser chamado a qualquer momento: ele sempre limpa apenas o que for lixo e sempre espelha exatamente a verdade atual sem duplicar dados.

### 3. Princípio da Paridade de Hash & Auditoria Criptográfica (*Cryptographic Integrity*)
* **A Lei:** Documentação e código espelhado não podem divergir silenciosamente. A confiança de um sistema de entrega depende de provas matemáticas de integridade de dados.
* **Aplicação Prática:** O Gate R18 calcula hashes MD5 de todos os arquivos de saída e publicação (`output/` vs `docs/`). Se houver qualquer divergência de 1 byte, o sistema bloqueia a esteira compulsoriamente.

---

## 1. O Que Foi Feito (Onde Estamos Hoje - 45%)

1. **Usina de Scripts Determinísticos em `scripts/`:**
   * `auditar_higiene_repo.py` (Gate R18 com conferência de hash MD5).
   * `limpar_entulho.py` (Auto-saneamento idempotente).
   * `auditar_r5_dossie.py` (Auditor de estrutura DOM dos dossiês).
   * `auditar_camada_tela.py` (Auditor da Camada 1 TELA).
   * `setup-links.ps1` / `.sh` (Montador de portabilidade).
2. **Declaração de MCPs em `.mcp.json`:**
   * Configuração de servidores MCP padrão.

---

## 2. Por Que Foi Feito

* **A Dor Resolvida (Alucinação de Verificação):** Sem scripts determinísticos, a IA jura que o código está certo quando na verdade está quebrado.
* **O Risco Mitigado (Degradação do Repositório):** Sem a auditoria de paridade, documentações públicas ficam desatualizadas em relação aos arquivos de entrega.

---

## 3. O Que Será Feito para Chegar aos 100%

1. **Servidor MCP de Estado da Esteira em SQLite (Regra R11):**
   * Criar um banco de dados local SQLite estruturado (`estado_esteira.db`) e um servidor MCP que exponha ferramentas como `get_task_status`, `log_token_usage` e `register_artefact`.
2. **Ferramenta MCP de Análise de Código AST (`ast-grep`):**
   * Encapsular o `ast-grep` como uma tool nativa do agente para localizar estruturas sintáticas sem gastar contexto de texto puro.
3. **Gate Mecânico da Camada 4 (`scripts/auditar_camada_tools.py`):**
   * Script Python que testa se todos os servidores MCP e scripts determinísticos estão respondendo com `exit 0`.

---

## 4. Onde Será Feito

* `.mcp.json` (Declaração de servidores MCP).
* `scripts/` (Scripts determinísticos e servidores locais).
* `scripts/auditar_camada_tools.py` (Gate mecânico).

---

## 5. Como Replicar o Que Foi Feito (Guia Passo a Passo)

*(Esta seção será preenchida com os comandos e códigos exatos assim que executarmos a implementação da Camada 4).*
