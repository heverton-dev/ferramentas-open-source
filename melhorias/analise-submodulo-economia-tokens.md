# Análise Técnica & Arquitetura: Submódulo Git Universal de Economia de Tokens

> **Escopo:** Integração das ferramentas da Lista 01 (Repomix, ast-grep, LiteLLM/OmniRouter, DSPy, Outlines/Guidance, SGLang, Tree-sitter) com as skills agênticas (`caveman`, `headroom`, `lean-ctx`, `rtk-memory`) e estruturação de um Submódulo Git Universal Plugável (`token-economy-core`).

---

## 1. O Dilema: Economia Agressiva vs. Preservação da Qualidade

A economia cega emburrece a IA. Se tipos forem truncados, docstrings críticas removidas ou saídas de entrega compactadas, o agente alucina.  
O segredo da engenharia de ponta é a **Compressão Assimétrica**:

```mermaid
flowchart LR
    classDef compativel fill:#D8EFE2,stroke:#1B5E3B,stroke-width:2px,color:#151A26;
    classDef sagrado fill:#F0D9DD,stroke:#8E2436,stroke-width:2px,color:#151A26;

    subgraph PODE_COMPRIMIR ["🟢 ONDE CORTAR ATÉ 90% (Zero Perda de Inteligência)"]
        direction TB
        C1["Pensamento CoT interno (Skill 'caveman')"]:::compativel
        C2["Logs de compilação/build (Skill 'headroom')"]:::compativel
        C3["Exploração de arquivos (code-review-graph + ast-grep)"]:::compativel
        C4["Prefixos estáticos de instrução (Prompt Caching via Repomix)"]:::compativel
        C5["Respostas idênticas (Cache Semântico via LiteLLM)"]:::compativel
    end

    subgraph INTOCAVEL ["🔴 O QUE É SAGRADO (100% de Fidelidade - Regra R7)"]
        direction TB
        S1["Código de entrega final (não resumir/não truncar)"]:::sagrado
        S2["Assinaturas de tipos TypeScript / Pydantic"]:::sagrado
        S3["Mensagens de erro completas dos testes (Asserts)"]:::sagrado
        S4["Saídas de validação de schemas (Outlines / Instructor)"]:::sagrado
    end
```

---

## 2. A Esteira Unificada: 4 Camadas de Eficiência

Em vez de ferramentas desconectadas, o pipeline opera em 4 etapas coordenadas:

```mermaid
flowchart TD
    classDef etapa fill:#F8F9FC,stroke:#C7CEDB,stroke-width:1px,color:#151A26;
    classDef cache fill:#D8EFE2,stroke:#1B5E3B,stroke-width:2px,color:#151A26;
    classDef agente fill:#DCE7F2,stroke:#1A446C,stroke-width:2px,color:#151A26;

    subgraph C1 ["Camada 1: Entrada & Filtragem (Pre-Flight)"]
        direction TB
        A1["Repomix + Tree-sitter<br><i>(Descarta binários e lockfiles)</i>"]:::etapa
        A2["Prompt Cirúrgico (< 10k tokens)"]:::etapa
        A3["LiteLLM / OmniRouter<br><i>(Cache Semântico Hit = 0 tokens)</i>"]:::cache

        A1 --> A2 --> A3
    end

    subgraph C2 ["Camada 2: Raciocínio & Execução (Inference Optimization)"]
        direction TB
        B1["SGLang / RadixAttention<br><i>(Reaproveitamento de KV-Cache)</i>"]:::etapa
        B2["Skill 'caveman'<br><i>(Pensamento telegráfico 3-5 linhas)</i>"]:::agente
        B3["ast-grep<br><i>(Refatorações via AST sem gastar LLM)</i>"]:::etapa

        B1 --> B2 --> B3
    end

    subgraph C3 ["Camada 3: Validação Estruturada (Zero Retries)"]
        direction TB
        C_Out["Outlines / Guidance / Instructor<br><i>(Força gramática formal CFG / Pydantic)</i>"]:::etapa
        C_Val["Zero tokens gastos em retry por JSON quebrado"]:::cache

        C_Out --> C_Val
    end

    subgraph C4 ["Camada 4: Pós-Execução & Ciclo Git"]
        direction TB
        D1["Skill 'headroom'<br><i>(Logs de teste comprimidos em 7 linhas)</i>"]:::etapa
        D2["Git Hook 'post-commit'<br><i>(Atualiza repomix-output.xml em background)</i>"]:::etapa
        D3["Skill 'rtk-memory'<br><i>(Persistência no RTK-SCRATCHPAD.md)</i>"]:::agente

        D1 --> D2 --> D3
    end

    A3 -->|Se Cache Miss| B1
    B3 --> C_Out
    C_Val --> D1
```

---

## 3. Estrutura do Submódulo Git Plugável: `token-economy-core`

O repositório independente funciona como um submódulo plugável em qualquer projeto existente ou novo:

```text
token-economy-core/
├── .claude/
│   └── skills/
│       ├── caveman/           # Compressão de CoT
│       ├── headroom/          # Compressão de logs
│       ├── lean-ctx/          # Disciplina grep antes de read
│       ├── rtk-memory/        # Gestão de scratchpad e cache
│       └── repomix-nav/       # Leitura orientada a snapshot
├── configs/
│   ├── repomix.config.json    # Configuração padronizada com exclusões
│   └── litellm.config.yaml    # Configuração de cache Redis
├── hooks/
│   ├── post-commit            # Atualiza snapshot após commits
│   └── pre-push               # Valida se o repositório está limpo de lixo
├── scripts/
│   ├── setup-links.ps1        # Cria Junctions/Symlinks no Windows
│   ├── setup-links.sh         # Cria Symlinks no Linux/Mac
│   └── gerar-snapshot.py      # Wrapper determinístico do Repomix
└── AGENTS-TEMPLATE.md         # Bloco padronizado de governança (R1-R17)
```

---

## 4. Instalação em Qualquer Repositório (1 Comando)

```bash
# 1. Adicionar submódulo
git submodule add https://github.com/seu-user/token-economy-core.git .token-economy

# 2. Executar setup automatizado
powershell .token-economy/scripts/setup-links.ps1   # No Windows
# ou
bash .token-economy/scripts/setup-links.sh          # No Linux/Mac
```

### Automações Realizadas pelo `setup-links`:
1. **Junctions Multi-IDE:** Mapeia `.token-economy/.claude/skills/*` para `.claude/skills/` (compatível com Antigravity, Cursor, Claude Code, Aider).
2. **Git Hooks:** Instala `.token-economy/hooks/post-commit` em `.git/hooks/post-commit`.
3. **Configuração Base:** Cria `repomix.config.json` na raiz se não existir.
4. **Snapshot Inicial:** Dispara `gerar-snapshot.py` para gerar o primeiro pacote de contexto.

---

## 5. Matriz de Implicações & Riscos Mitigados

| Risco Técnico | Causa Provável | Solução Arquitetural |
|---|---|---|
| **Alucinação por Over-pruning** | Truncamento cego de interfaces de types. | **Tree-sitter & Repomix** preservam 100% de assinaturas e contratos; descartam apenas corpos irrelevantes. |
| **Invalidação de Prefix Cache** | Alterações frequentes no system prompt. | A skill **`rtk-memory`** mantém o prompt base imutável e salva novidades em `RTK-SCRATCHPAD.md`. |
| **Gargalo no Commit** | Execução síncrona do Repomix no hook. | O hook roda em **background assíncrono** (`Start-Process` / `&`), liberando o terminal em 50ms. |
| **Poluição de Lockfiles** | Enviar `package-lock.json` no prompt. | Exclusão forçada de lockfiles, binários e builds no `repomix.config.json`. |
