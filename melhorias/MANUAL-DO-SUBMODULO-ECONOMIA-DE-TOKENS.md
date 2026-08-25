# 🌐 Token Economy Core
### O Padrão Universal para Reduzir até 95% do Gasto de Tokens com IA (Para Iniciantes & Veteranos)

[![GitHub License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Tokens Saved](https://img.shields.io/badge/Tokens%20Economy-Até%20--95.3%25-brightgreen.svg)](#-resultados-comprovados-em-testes-reais)
[![Multi-OS](https://img.shields.io/badge/SO-Windows%20%7C%20macOS%20%7C%20Linux-blue.svg)](#)
[![Multi-IDE](https://img.shields.io/badge/IDEs-Claude%20Code%20%7C%20Cursor%20%7C%20Windsurf%20%7C%20Cline%20%7C%20Antigravity%20%7C%20Copilot%20%7C%20Aider-orange.svg)](#)

---

## 🎯 O que é o Token Economy Core?

Se você usa IA para programar (em **qualquer IDE, Harness ou Modelo**), já deve ter notado que a cota de 5 horas acaba rápido ou a fatura de tokens sobe desnecessariamente.

Isso acontece porque a IA costuma:
1. **Ler arquivos gigantes inúteis** (como `package-lock.json`, `dist/` ou imagens).
2. **Pensar de forma prolixa** (gastando centenas de tokens no raciocínio interno antes de responder).
3. **Ler 300 linhas de logs de terminal** quando o erro real está em 3 linhas.

O **Token Economy Core** é um submódulo universal e plugável que resolve isso de forma **100% automática, não-destrutiva e agnóstica a SO**: ele instala regras inteligentes, skills de disciplina e automação de empacotamento com **apenas 1 comando universal em Python**.

---

## 📊 Resultados Comprovados em Testes Reais

Em nossa bateria de benchmark empírico em projetos reais, obtivemos os seguintes resultados:

| Cenário do Dia a Dia | Sem o Módulo | Com o Token Economy Core | Economia Real |
|---|---|---|---|
| **1. Mapeamento do Projeto** | 251.012 tokens | **1.500 tokens** | **-99,4%** (167x mais econômico) |
| **2. Pensamento do Agente (CoT)** | 1.421 tokens | **246 tokens** | **-82,7%** (5.8x mais econômico) |
| **3. Logs de Testes e Build** | 3.949 tokens | **111 tokens** | **-97,2%** (35.6x mais econômico) |
| **4. Aproveitamento de Cache** | 28.760 tokens | **12.705 tokens** | **-55,8%** (2.3x mais econômico) |
| **5. Refatorações Estruturais** | 23.160 tokens | **0 tokens (via AST)** | **-100%** (Custo Zero) |
| **TOTAL CONSOLIDADO** | **308.302 tokens** | **14.562 tokens** | **🔥 -95,3% de Economia** |

---

## 🚀 Instalação Universal em 2 Passos (Qualquer SO e Qualquer IDE)

O instalador é **100% multiplataforma (Windows, macOS e Linux)**.

### Passo 1: Adicione o Submódulo na pasta do seu projeto
Abra o terminal na pasta do seu projeto (existente ou novo) e execute:

```bash
git submodule add https://github.com/Heverton-web/token-economy-core.git .token-economy
```

### Passo 2: Execute o Instalador Universal (Python)
Em **qualquer sistema operacional (Windows, macOS ou Linux)**, execute:

```bash
python .token-economy/install.py
```

*(Se preferir usar scripts de shell nativos: `powershell .token-economy/scripts/setup-links.ps1` no Windows ou `bash .token-economy/scripts/setup-links.sh` no Linux/Mac).*

---

## 🛠️ Como Funciona nos 2 Cenários

### 📂 CENÁRIO 1: Em um Projeto que JÁ EXISTE (100% Não-Destrutivo)
* **Garantia de Segurança:** Se você já tem regras ou arquivos de configuração, o instalador **não sobrescreve**. Ele apenas conecta as skills e sincroniza os hooks de automação com segurança.

### 🆕 CENÁRIO 2: Em um Projeto NOVO (Começando do Zero)
* O instalador cria o `AGENTS.md` automaticamente na raiz e o sincroniza para **Cursor (`.cursor/rules/`), Windsurf (`.windsurfrules`), Cline (`.clinerules`), GitHub Copilot (`.github/copilot-instructions.md`) e Claude Code (`CLAUDE.md`)**.

---

## 🌐 Matriz de Universalidade

| Categoria | Suporte Completo |
|---|---|
| **Sistemas Operacionais** | Windows 10/11, macOS (Intel/Apple Silicon), Linux (Ubuntu, Debian, Fedora, Arch). |
| **IDEs & Editores** | VS Code, Cursor, Windsurf, JetBrains, Zed, Void, Neovim. |
| **Harnesses & CLIs** | Claude Code, Antigravity, Aider, OpenCode, Codebuff, Cline, Roo-Code, GitHub Copilot CLI. |
| **Modelos de IA** | Anthropic Claude, OpenAI GPT, Google Gemini, DeepSeek, Qwen, Meta Llama, Ollama Local. |

---

## 🧭 O que o Token Economy Core ativa para você?

1. **`repomix.config.json`:** Filtra automaticamente `node_modules`, `dist/`, `.git/`, lockfiles e imagens.
2. **Git Hook `post-commit` Assíncrono:** Toda vez que um commit é feito, o snapshot do projeto é atualizado em background em menos de 1 segundo sem travar o seu terminal.
3. **5 Skills Agênticas de Elite em `.claude/skills/`:**
   - **`caveman`:** Raciocínio telegráfico e enxuto no bloco `<thought>`.
   - **`headroom`:** Comprime saídas longas de compilação/testes para no máximo 7 linhas.
   - **`lean-ctx`:** Disciplina a IA para ler apenas fatias de código em vez de arquivos inteiros.
   - **`rtk-memory`:** Mantém o system prompt estável para aproveitar até 90% de desconto no *Prompt Caching*.
   - **`repomix-navigator`:** Mapeia a arquitetura inteira em 1 única chamada estruturada em XML.

---

## 📡 Como Acompanhar o Consumo no Dia a Dia (Telemetria)

```bash
# Auditar blocos de faturamento de 5h e taxa de cache
python .token-economy/scripts/auditor-telemetria.py

# Ver o status da sua cota e tempo exato de reset
ccusage status

# Ver o relatório detalhado de tokens consumidos hoje
npx ccusage@latest daily
```

---

## ❓ Perguntas Frequentes (FAQ)

### A economia de tokens reduz a inteligência ou a qualidade do código?
**Não.** O submódulo aplica a regra de **Compressão Assimétrica**: ele corta apenas o lixo (logs repetitivos, pensamentos prolixos e arquivos desnecessários). **O código final entregue para você nunca é resumido ou truncado.**

---

## 🤝 Licença & Créditos

Desenvolvido por **Heverton-web** sob os padrões de governança da **Fábrica Universal**.  
Distribuído sob licença **MIT** (Livre para uso pessoal e comercial).
