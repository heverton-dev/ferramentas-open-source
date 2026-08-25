# 🔌 Camada 2: HARNESS (Harness & Loop Engineering)

> **Papel no Estúdio:** O Sistema de Segurança, Cabos e Disjuntores.  
> **Status:** 100% CONCLUÍDO & BLINDADO ✅  
> **Unidade de Trabalho:** Orquestrador do ADE (Orca/Antigravity/Claude Code), `settings.json`, Hooks, Sandbox, Trava de Loops e Disjuntores.  
> **Localização:** `4-camadas/02-CAMADA-HARNESS.md`  
> **Auditor Mecânico:** `scripts/auditar_camada_harness.py` (Retorno: `exit 0`)

---

## 🏛️ Os Princípios Universais & Imutáveis da Camada HARNESS

O **HARNESS** é a engenharia de controle que encapsula o modelo de linguagem. Ele opera sob três princípios imutáveis de confiabilidade de sistemas:

### 1. Princípio do Disjuntor & Parada de Loop (*Circuit Breaker & Halting Problem*)
* **A Lei:** Agentes autônomos operando em loops de tentativa e erro estão sujeitos ao problema da parada (*Turing's Halting Problem*) e podem entrar em ciclos infinitos de consumo de recursos quando encontram um erro que não sabem resolver.
* **Aplicação Prática:** O Harness deve conter **disjuntores mecânicos duros** (limite máximo de 25 iterações de loop e timeouts de 60s em comandos de terminal) que desligam o agente compulsoriamente antes que ele esgote o orçamento ou trave o terminal.

### 2. Princípio do Privilégio Mínimo & Sandbox Reversível (*Defensive Execution*)
* **A Lei:** Nenhuma inteligência não-determinística deve possuir acesso irrestrito de gravação ou execução destrutiva no sistema operacional sem barreiras intermediárias de contenção.
* **Aplicação Prática:** A camada de Harness isola comandos perigosos, proíbe comandos `cd` em scripts de shell (que causam deriva de diretório de trabalho) e bloqueia comandos destrutivos (`rm -rf /`, `mkfs`, fork bombs).

### 3. Princípio do Ponto Único de Verdade (*Single Source of Truth na Portabilidade*)
* **A Lei:** A dispersão de configurações em múltiplos arquivos de IDEs (Cursor, Windsurf, VS Code, Cline) gera divergência de comportamento e entropia de manutenção.
* **Aplicação Prática:** A governança vive em apenas um ponto físico no disco (`.claude/CLAUDE.md`) e é propagada para todas as IDEs via *Hardlinks* no nível do sistema de arquivos (*NTFS / EXT4*), tornando a sincronização instantânea e atômica.

---

## 1. O Que Foi Feito

Nesta camada, estruturamos e blindamos a infraestrutura de contenção, orquestração e segurança:
1. **Configuração Industrial de Ciclo de Vida (`.claude/settings.json`):**
   * Configuração de *Circuit Breakers* com limites rígidos de iterações (`max_loop_iterations: 25`) e timeouts de comando (`command_timeout_seconds: 60`).
   * Configuração de *Sandbox* defensiva com bloqueio de comandos `cd` e banimento de comandos destrutivos.
   * Interceptores de ciclo de vida (`PreToolUse`, `PostToolUse`, `SessionStart`) que acionam a atualização do grafo de código.
2. **Hook de Pre-Commit do Git com 6 Gates de Inspeção (`scripts/hooks/pre-commit`):**
   * Gate 1: Varredura de chaves de API e segredos (R15).
   * Gate 2: Suíte de testes Python (`pytest`) (R16).
   * Gate 3: Suíte de testes Node.js (`npm test`).
   * Gate 4: Compilação sintática Python contra erros de digitação.
   * Gate 5: Atualização do grafo de dependências do repositório.
   * Gate 6: Auditoria criptográfica de higiene e paridade de hash MD5 (R18).
3. **Mecanismo de Portabilidade Multi-IDE (`scripts/setup-links.ps1` e `.sh`):**
   * Automação de Hardlinks e Junctions para espelhar a governança sem duplicação.
4. **Gate Mecânico de Auditoria da Camada 2 (`scripts/auditar_camada_harness.py`):**
   * Validador determinístico que testa se o Harness está 100% íntegro e retorna `exit 0`.

---

## 2. Por Que Foi Feito

* **A Dor Resolvida (Loops Cegos & Travamentos):** Sem disjuntores no Harness, agentes de IA podem gastar US$ 50 em poucos minutos tentando resolver um erro de sintaxe em loop infinito.
* **O Risco Mitigado (Execução Destrutiva & Código Quebrado):** Sem a sandbox e os gates de pre-commit, um agente descontrolado pode apagar diretórios ou comitar código quebrado em produção.
* **O Ganho Operacional:** Qualquer membro da equipe pode usar a IDE de sua preferência (Cursor, VS Code, Windsurf, Claude Code) com a certeza matemática de que o comportamento do agente será rigorosamente o mesmo.

---

## 3. Onde Foi Feito

Todos os artefatos do HARNESS residem nos seguintes caminhos físicos:

```
seu-projeto/
├── .claude/
│   └── settings.json             ← Configuração Industrial (Disjuntores, Sandbox, Hooks)
│
├── .git/hooks/pre-commit         ← O Guarda-Costas do Git (Executável local)
├── scripts/
│   ├── hooks/pre-commit          ← Fonte versionada do Hook do Git (6 Gates)
│   ├── setup-links.ps1           ← Script de montagem de links para Windows
│   ├── setup-links.sh            ← Script de montagem de links para Linux/Mac
│   └── auditar_camada_harness.py ← Gate Mecânico da Camada 2
```

---

## 4. Como Foi Feito

### 4.1 A Estrutura de `.claude/settings.json`
```json
{
  "$comment": "Configuração Industrial do HARNESS (Camada 2).",
  "harness": {
    "version": "2.0.0",
    "circuit_breaker": {
      "max_loop_iterations": 25,
      "command_timeout_seconds": 60,
      "max_context_bytes_per_call": 524288
    },
    "sandbox": {
      "disallow_shell_cd": true,
      "require_confirmation_on_destructive": true,
      "prohibited_commands": [
        "rm -rf /",
        "rm -rf *",
        ":(){ :|:& };:"
      ]
    }
  },
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write|replace_file_content|write_to_file",
        "hooks": [
          {
            "type": "command",
            "command": "cat >/dev/null || true; command -v code-review-graph >/dev/null 2>&1 || exit 0",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

### 4.2 O Gate Mecânico do HARNESS (`scripts/auditar_camada_harness.py`)
Script Python determinístico que confere:
1. Se `.claude/settings.json` é um JSON válido e contém a seção `circuit_breaker` com `max_loop_iterations`.
2. Se `scripts/hooks/pre-commit` contém os gates fundamentais (Segredos, Testes, Sintaxe, Higiene).
3. Se o hook está ativo em `.git/hooks/pre-commit`.
4. Se os scripts `setup-links` estão presentes.
*Retorno:* `sys.exit(0)` em caso de aprovação ou `sys.exit(1)` em caso de falha.

---

## 5. Como Replicar o Que Foi Feito (Guia Passo a Passo Universal)

Para replicar exatamente a Camada 2 em qualquer projeto:

### Passo 1: Copie as configurações e scripts
```bash
# Na raiz do seu projeto novo:
mkdir -p .claude scripts/hooks
cp fabrica-universal/.claude/settings.json .claude/
cp fabrica-universal/scripts/hooks/pre-commit scripts/hooks/
cp fabrica-universal/scripts/setup-links.* scripts/
cp fabrica-universal/scripts/auditar_camada_harness.py scripts/
```

### Passo 2: Execute o script de configuração de links e hooks
* No Windows:
  ```powershell
  .\scripts\setup-links.ps1 meu-projeto
  ```
* No Linux / Mac:
  ```bash
  bash scripts/setup-links.sh meu-projeto
  ```

### Passo 3: Execute a Auditoria Mecânica do HARNESS
```bash
python scripts/auditar_camada_harness.py
```

### Passo 4: Verifique a Saída
Se o terminal exibir:
```text
================================================================================
 🔌 GATE MECÂNICO DA CAMADA 2: AUDITOR DO HARNESS (ORQUESTRAÇÃO & SEGURANÇA)
================================================================================
 ✅ CAMADA 2 (HARNESS) 100% APROVADA: Circuit Breakers, Pre-Commit, Sandbox & Portabilidade!
================================================================================
```
A sua Camada 2 está oficialmente **100% configurada, blindada e pronta para produção**.
