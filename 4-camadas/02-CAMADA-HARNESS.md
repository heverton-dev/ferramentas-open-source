# 🔌 Camada 2: HARNESS (Harness & Loop Engineering)

> **Papel no Estúdio:** O Sistema de Segurança, Cabos e Disjuntores.  
> **Status:** 35% Implementado ➡️ **Meta: 100%**.  
> **Unidade de Trabalho:** Orquestrador do ADE (Orca/Antigravity/Claude Code), `settings.json`, Hooks, Sandbox, Trava de Loops e Disjuntores.  
> **Localização:** `4-camadas/02-CAMADA-HARNESS.md`

---

## 1. O Que É e Por Que Importa

O **HARNESS** é o sistema que encapsula o modelo. Se a TELA é o que a IA pensa, o HARNESS é **o motor que decide quando chamar o modelo, quando executar ferramentas, quando parar e como proteger o sistema operacional**.
Sem um Harness robusto, o agente entra em loops infinitos de erro, consome orçamento sem controle ou executa comandos perigosos no computador.

---

## 2. O Que Já Temos Implementado

1. **Portabilidade Multi-IDE (`scripts/setup-links.ps1` / `.sh`):**
   * Cria Hardlinks e Junctions para que qualquer IDE (Cursor, Windsurf, Claude Code, Cline, VS Code) acesse a mesma fonte da verdade.
2. **Hook de Pre-Commit Automatizado (`.git/hooks/pre-commit`):**
   * Bloqueia commits com segredos expostos (R15).
   * Bloqueia commits com testes quebrados (R16).
   * Bloqueia commits com sintaxe Python inválida.
   * Bloqueia commits com desordem ou arquivos temporários (R18).

---

## 3. O Que Falta para Atingirmos 100% no HARNESS (Roadmap de Lapidação)

Para que o Harness atinja o grau industrial completo, implementaremos:

1. **Configuração de Hooks de Ciclo de Vida em `.claude/settings.json`:**
   * `PreToolCall`: Interceptar ferramentas pesadas antes da execução.
   * `PostToolCall`: Validar o resultado da ferramenta e cortar saídas gigantescas.
   * `MaxLoopIterations`: Trava de segurança que desliga o agente se ele passar de 15 passos sem progresso mensurável.
2. **Disjuntor de Timeout & Kill-Switch:**
   * Garantir que comandos assíncronos no terminal não travem a sessão indefinidamente.
3. **Contrato Formal de Subagentes:**
   * Definir regras estritas de fan-out (tarefas em paralelo) com timeout de 300 segundos e auto-validação antes do merge.
