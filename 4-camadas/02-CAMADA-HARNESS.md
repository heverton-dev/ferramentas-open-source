# 🔌 Camada 2: HARNESS (Harness & Loop Engineering)

> **Papel no Estúdio:** O Sistema de Segurança, Cabos e Disjuntores.  
> **Status:** 35% Implementado ➡️ **Meta: 100%** (Em Foco Agora).  
> **Unidade de Trabalho:** Orquestrador do ADE (Orca/Antigravity/Claude Code), `settings.json`, Hooks, Sandbox, Trava de Loops e Disjuntores.  
> **Localização:** `4-camadas/02-CAMADA-HARNESS.md`  
> **Auditor Mecânico:** `scripts/auditar_camada_harness.py` *(a ser criado)*

---

## 1. O Que É e Por Que Importa

O **HARNESS** é o sistema que encapsula o modelo. Se a TELA é o que a IA pensa, o HARNESS é **o motor que decide quando chamar o modelo, quando executar ferramentas, quando parar e como proteger o sistema operacional**.
Sem um Harness robusto, o agente entra em loops infinitos de erro, consome orçamento sem controle ou executa comandos perigosos no computador.

---

## 2. O Que Já Foi Feito (Onde Estamos Hoje - 35%)

1. **Portabilidade Multi-IDE (`scripts/setup-links.ps1` / `.sh`):**
   * Cria Hardlinks e Junctions para que qualquer IDE (Cursor, Windsurf, Claude Code, Cline, VS Code) acesse a mesma fonte da verdade.
2. **Hook de Pre-Commit Automatizado (`.git/hooks/pre-commit`):**
   * Bloqueia commits com segredos expostos (R15).
   * Bloqueia commits com testes quebrados (R16).
   * Bloqueia commits com sintaxe Python inválida.
   * Bloqueia commits com desordem ou arquivos temporários (R18).

---

## 3. O Que Será Feito para Chegar aos 100%

1. **Configuração de Hooks de Ciclo de Vida em `.claude/settings.json`:**
   * `PreToolCall`: Interceptar ferramentas pesadas antes da execução.
   * `PostToolCall`: Validar o resultado da ferramenta e cortar saídas gigantescas.
   * `MaxLoopIterations`: Trava de segurança que desliga o agente se ele passar de 20 passos sem progresso mensurável.
2. **Disjuntor de Timeout & Kill-Switch:**
   * Garantir que comandos assíncronos no terminal não travem a sessão indefinidamente.
3. **Contrato Formal de Subagentes:**
   * Definir regras estritas de fan-out (tarefas em paralelo) com timeout de 300 segundos e auto-validação antes do merge.
4. **Gate Mecânico da Camada 2 (`scripts/auditar_camada_harness.py`):**
   * Script Python que valida a presença de todos os hooks, travas de loop e configurações de segurança do ADE.

---

## 4. Onde Será Feito

* `.claude/settings.json` (Hooks de ciclo de vida e travas).
* `scripts/hooks/pre-commit` (Guarda-costas do Git).
* `scripts/setup-links.ps1` e `scripts/setup-links.sh` (Portabilidade).
* `scripts/auditar_camada_harness.py` (Gate mecânico).

---

## 5. Como Replicar o Que Foi Feito (Guia de Replicação)

*(Esta seção será preenchida com os comandos e códigos exatos assim que executarmos a implementação da Camada 2).*
