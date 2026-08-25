# 🏛️ Manual de Arquitetura da Fábrica Universal

> **Guia Executivo & Técnico da Arquitetura Agêntica de Soberania, Economia de Tokens e Governança Mecânica.**

---

## 🎯 1. Foco Principal da Arquitetura

O objetivo central desta arquitetura é transformar o desenvolvimento de software assistido por inteligência artificial (AIDD - *AI-Driven Development*) em um **processo industrial previsível, de baixo custo e com soberania total**.

Em vez de depender de prompts informais ou de copilotos proprietários que cobram por usuário e consomem milhões de tokens com raciocínios redundantes, a **Fábrica Universal** estabelece:

1. **Economia Severa de Tokens (Redução de 50% a 90%):** Otimização radical de contexto através de técnicas como *Caveman Thinking*, compressão de logs (*Headroom*), leitura seletiva de código (*Lean-CTX*) e memória de sessão em cache (*RTK-Memory*).
2. **Determinismo Primeiro (Gates Mecânicos):** Nenhuma regra de qualidade ou conformidade depende da "boa vontade" ou da memória da IA. Toda regra é convertida em um script Python que retorna `exit 0` (aprovado) ou `exit 1` (bloqueia a esteira).
3. **Portabilidade Multi-IDE com Fonte Única:** Você pode usar **Claude Code, Cursor, Windsurf, VS Code, Cline ou OpenCode** simultaneamente. A governança é editada em apenas um lugar (`.claude/`) e espelhada automaticamente para todas as outras IDEs.
4. **Higiene Contínua & Zero Entulho (Regra R18):** O repositório é auto-saneador. Scripts descartáveis, backups soltos ou divergências entre pastas de documentação são bloqueados fisicamente no `pre-commit`.
5. **Padrão Visual Diamante (Dossiê Executivo - R5):** Todo artefato HTML gerado segue um design editorial semântico, com tipografia justificada, tabela de dados fluida, 4 seções verticais estruturadas e passos práticos acionáveis.

---

## 🏗️ 2. Como o Projeto Está Estruturado (Anatomia do Repositório)

O repositório é organizado em quatro camadas fundamentais:

```
seu-projeto/
├── .claude/                      ← [CAMADA 1] FONTE ÚNICA DA VERDADE
│   ├── CLAUDE.md                 # Governança mestre (Regras R1 a R18 e Seção 0 de Economia)
│   ├── RTK.md                    # Guia e padrões de compressão de contexto
│   ├── settings.json             # Configurações de harness e hooks do agente
│   ├── skills/                   # Habilidades especializadas (economia + domínio do projeto)
│   └── agents/                   # Subagentes para tarefas paralelas
│
├── scripts/                      ← [CAMADA 2] USINA MECÂNICA DETERMINÍSTICA
│   ├── hooks/pre-commit          # Guardião do Git (bloqueia segredos e código vermelho)
│   ├── padroes/                  # Templates canônicos (skill, script, comando, dossiê)
│   ├── auditar_higiene_repo.py   # Gate R18: garante paridade de hash e zero lixo
│   ├── limpar_entulho.py         # Auto-saneamento e sincronização mecânica
│   └── setup-links.ps1 / .sh     # Gerador de links para portabilidade multi-IDE
│
├── output/ & docs/               ← [CAMADA 3] CAMADA DE ENTREGA & ESPELHO ESTRITO
│   ├── listas-open-source/       # Hub Central e os 49 compêndios técnicos no Padrão Diamante
│   └── docs/listas/              # Espelho de paridade exata para publicação e deploy
│
└── AGENTS.md, .cursor/, etc.     ← [CAMADA 4] ESPELHOS E JUNCTIONS GERADOS
    └── (Gerados automaticamente via setup-links — nunca editados diretamente)
```

---

## ⚖️ 3. Prós e Contras Desta Arquitetura

### 🟢 Prós (Vantagens Competitivas)

| Vantagem | Descrição |
| :--- | :--- |
| **💰 Economia Financeira Brutal** | Reduz as faturas de API e consumo de tokens em 50% a 90% via prompts telegráficos e poda de contexto. |
| **🛡️ Imunidade a Alucinações de Qualidade** | O pre-commit roda testes e auditores reais. Se a IA errar, o git simplesmente recusa o commit. |
| **🔄 Zero Vendor Lock-in de IDE** | Se o Cursor mudar de preço ou o Claude Code lançar uma novidade, você troca de ferramenta em 1 segundo sem reconfigurar regras. |
| **✨ Padrão Visual Impeccable** | Relatórios, catálogos e entregas para clientes possuem design editorial de alta densidade pronto para executivos. |
| **🧹 Repositório Eternamente Limpo** | A regra R18 impede o acúmulo de scripts descartáveis e "débito técnico invisível". |

---

### 🔴 Contras & Trade-offs (O Que Você Precisa Considerar)

| Ponto de Atenção | Como Mitigar |
| :--- | :--- |
| **Curva de Disciplina Inicial** | Desenvolvedores acostumados a commitar sem testes encontrarão bloqueios do `pre-commit`. **Solução:** Rodar `python scripts/limpar_entulho.py` e testes antes do commit. |
| **Requisito de Links Simbólicos** | No Windows, a criação de *Junctions* e *Hardlinks* exige modo desenvolvedor ativado ou execução do PowerShell como Administrador. |
| **Não Editar Espelhos** | Editar acidentalmente um arquivo gerado (como `AGENTS.md`) em vez de `.claude/CLAUDE.md`. **Solução:** O `setup-links` avisa e sincroniza a fonte única. |

---

## 🚀 4. Como Usar: Iniciar Novos Projetos ou Adequar Existentes

### 📦 Caso A: Criando um Projeto Novo do Zero (5 Minutos)

1. **Inicie o repositório Git:**
   ```bash
   mkdir meu-novo-projeto && cd meu-novo-projeto
   git init
   ```

2. **Adicione a Fábrica Universal como Submodule:**
   ```bash
   git submodule add https://github.com/Heverton-web/fabrica-universal.git fabrica-universal
   git submodule update --init --recursive
   ```

3. **Copie a infraestrutura base:**
   ```bash
   cp -r fabrica-universal/.claude .
   mkdir -p scripts && cp -r fabrica-universal/scripts/* scripts/
   ```

4. **Gere os links de portabilidade e instale o Hook Pre-Commit:**
   * **No Windows (PowerShell):**
     ```powershell
     .\scripts\setup-links.ps1 meu-novo-projeto
     ```
   * **No Linux / macOS (Bash):**
     ```bash
     bash scripts/setup-links.sh meu-novo-projeto
     ```

5. **Pronto!** O projeto já nasce blindado com as 18 regras, 5 skills de economia de tokens e o hook de pre-commit ativo.

---

### 🔧 Caso B: Adequando um Projeto Já Existente (Brownfield)

1. **Adicione a Fábrica como Submodule:**
   ```bash
   git submodule add https://github.com/Heverton-web/fabrica-universal.git fabrica-universal
   ```

2. **Mescle as Skills de Economia de Tokens:**
   ```bash
   mkdir -p .claude/skills
   cp -r fabrica-universal/.claude/skills/* .claude/skills/
   ```

3. **Incorpore as Regras R1–R18:**
   * Abra seu `CLAUDE.md` existente e adicione a **Seção 0 (Economia de Tokens)** e as regras **R1 a R18**.
   * Adicione o `scripts/hooks/pre-commit` e `scripts/auditar_higiene_repo.py`.

4. **Rode o saneador e valide:**
   ```bash
   python scripts/limpar_entulho.py
   python scripts/auditar_higiene_repo.py
   ```

---

## 📋 Resumo das 18 Regras Universais (Cheat Sheet)

* **R1 (PT-BR):** Idioma padrão de comunicação e código.
* **R2 (Silenciamento):** Sem introduções vazias ou agradecimentos no chat.
* **R3/R4 (Autonomia & Auto-Correção):** Resolução interna de desvios antes da entrega.
* **R5 (Padrão Diamante / Dossiê Executivo):** 4 seções verticais, 3 mini-cards de passos, tabela fluida e busca em tempo real.
* **R6 (Modelo Livre):** `model: inherit` em todos os agentes.
* **R7 (Conteúdo Intocável):** Textos finais e relatórios nunca são truncados.
* **R8/R9 (Determinismo & Gates):** Se um script resolve, não gaste LLM; todo gate retorna `exit 0/1`.
* **R10/R11 (Idempotência & Estado em Disco):** Reexecução segura e persistência versionável.
* **R12/R13/R14 (Higiene de Nomes):** Registro declarativo único, sem prefixo `_`, caminhos curtos (<260 chars).
* **R15/R16 (Segurança & Suíte Verde):** Zero credenciais em disco; nunca comitar com testes falhando.
* **R17 (Etapas Opcionais):** Sempre configuráveis e sem falhas silenciosas.
* **R18 (Higiene Contínua & Espelhos):** Zero lixo temporário e 100% de paridade de hash entre espelhos.

---
*Documento canônico gerado pela Fábrica Universal de Soberania Tecnológica.*
