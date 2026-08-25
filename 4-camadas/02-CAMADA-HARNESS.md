# 🔌 Camada 2: HARNESS (Harness & Loop Engineering)

> **Papel no Estúdio:** O Sistema de Segurança, Cabos e Disjuntores.  
> **Status:** 35% Implementado ➡️ **Meta: 100%** (Em Foco Agora).  
> **Unidade de Trabalho:** Orquestrador do ADE (Orca/Antigravity/Claude Code), `settings.json`, Hooks, Sandbox, Trava de Loops e Disjuntores.  
> **Localização:** `4-camadas/02-CAMADA-HARNESS.md`  
> **Auditor Mecânico:** `scripts/auditar_camada_harness.py` *(a ser criado)*

---

## 🏛️ Os Princípios Universais & Imutáveis da Camada HARNESS

O **HARNESS** é a engenharia de controle que encapsula o modelo de linguagem. Ele opera sob três princípios imutáveis de confiabilidade de sistemas:

### 1. Princípio do Disjuntor & Parada de Loop (*Circuit Breaker & Halting Problem*)
* **A Lei:** Agentes autônomos operando em loops de tentativa e erro estão sujeitos ao problema da parada (*Turing's Halting Problem*) e podem entrar em ciclos infinitos de consumo de recursos quando encontram um erro que não sabem resolver.
* **Aplicação Prática:** O Harness deve conter **disjuntores mecânicos duros** (limite máximo de iterações de loop e timeouts de execução de comando) que desligam o agente compulsoriamente antes que ele esgote o orçamento ou trave o terminal.

### 2. Princípio do Privilégio Mínimo & Sandbox Reversível (*Defensive Execution*)
* **A Lei:** Nenhuma inteligência não-determinística deve possuir acesso irrestrito de gravação ou execução destrutiva no sistema operacional sem barreiras intermediárias de contenção.
* **Aplicação Prática:** A camada de Harness deve isolar execuções perigosas, bloquear comandos `cd` em scripts de shell e exigir confirmação explícita do operador para ações de alto risco.

### 3. Princípio do Ponto Único de Verdade (*Single Source of Truth na Portabilidade*)
* **A Lei:** A dispersão de configurações em múltiplos arquivos de IDEs (Cursor, Windsurf, VS Code, Cline) gera divergência de comportamento e entropia de manutenção.
* **Aplicação Prática:** A governança vive em apenas um ponto físico no disco e é propagada para todas as IDEs via *Hardlinks* no nível do sistema de arquivos (*NTFS / EXT4*), tornando a sincronização instantânea e atômica.

---

## 1. O Que Foi Feito (Onde Estamos Hoje - 35%)

1. **Portabilidade Multi-IDE (`scripts/setup-links.ps1` / `.sh`):**
   * Cria Hardlinks e Junctions para que qualquer IDE acesse a mesma fonte da verdade.
2. **Hook de Pre-Commit Automatizado (`.git/hooks/pre-commit`):**
   * Bloqueia commits com segredos expostos (R15).
   * Bloqueia commits com testes quebrados (R16).
   * Bloqueia commits com sintaxe Python inválida.
   * Bloqueia commits com desordem ou arquivos temporários (R18).

---

## 2. Por Que Foi Feito

* **A Dor Resolvida (Código Quebrado em Produção):** Sem os gates de pre-commit no Harness, código defeituoso é salvo no repositório, corrompendo a esteira de CI/CD.
* **O Risco Mitigado (Lock-in de IDE):** Sem os hardlinks de portabilidade, migrar de um editor para outro exigiria reescrever dezenas de arquivos de configuração.

---

## 3. O Que Será Feito para Chegar aos 100%

1. **Configuração de Hooks de Ciclo de Vida em `.claude/settings.json`:**
   * `PreToolCall`: Interceptar ferramentas pesadas antes da execução.
   * `PostToolCall`: Validar o resultado da ferramenta e cortar saídas gigantescas.
   * `MaxLoopIterations`: Trava de segurança que desliga o agente se ele passar de 20 passos sem progresso mensurável.
2. **Disjuntor de Timeout & Kill-Switch:**
   * Garantir que comandos assíncronos no terminal não travem a sessão indefinidamente.
3. **Gate Mecânico da Camada 2 (`scripts/auditar_camada_harness.py`):**
   * Script Python que valida a presença de todos os hooks, travas de loop e configurações de segurança do ADE.

---

## 4. Onde Será Feito

* `.claude/settings.json` (Hooks de ciclo de vida e travas).
* `scripts/hooks/pre-commit` (Guarda-costas do Git).
* `scripts/setup-links.ps1` e `scripts/setup-links.sh` (Portabilidade).
* `scripts/auditar_camada_harness.py` (Gate mecânico).

---

## 5. Como Replicar o Que Foi Feito (Guia Passo a Passo)

*(Esta seção será preenchida com os comandos e códigos exatos assim que executarmos a implementação da Camada 2).*
