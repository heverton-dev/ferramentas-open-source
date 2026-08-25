#set page(
  paper: "a4",
  margin: (x: 2cm, y: 2.2cm),
  header: align(right)[
    #text(8pt, fill: rgb("#68738A"), font: "Liberation Sans")[
      Fábrica Universal · Governança & Eficiência Agêntica · 2026
    ]
  ],
  footer: context [
    #align(center)[
      #text(8pt, fill: rgb("#68738A"), font: "Liberation Sans")[
        Página #counter(page).display() de #counter(page).final().first()
      ]
    ]
  ]
)

#set text(
  font: "Liberation Sans",
  size: 10.5pt,
  lang: "pt",
  fill: rgb("#151A26")
)

#set par(justify: true, leading: 0.65em)

// Cores do Design System
#let brand-dark = rgb("#1A446C")
#let brand-light = rgb("#DCE7F2")
#let brand-accent = rgb("#1B5E3B")
#let brand-accent-light = rgb("#D8EFE2")
#let surface = rgb("#F8F9FC")
#let border-color = rgb("#C7CEDB")

// Título & Cabeçalho
#align(center)[
  #block(
    fill: brand-light,
    inset: 12pt,
    radius: 4pt,
    stroke: 1pt + brand-dark,
    width: 100%,
    [
      #text(10pt, weight: "bold", fill: brand-dark, tracking: 0.1em)[
        PLANO DE ARQUITETURA & EFICIÊNCIA DE TOKENS
      ]
      #v(4pt)
      #text(18pt, weight: "bold", fill: rgb("#0E1118"))[
        Automação do Repomix com Git Hooks & Direcionamento de Harness
      ]
      #v(4pt)
      #text(9.5pt, fill: rgb("#3B4457"))[
        Estratégia para corte de até 85% do custo de contexto em sessões com agentes de IA
      ]
    ]
  )
]

#v(10pt)

== 1. Objetivo Executivo

Este documento estabelece o plano formal para automatizar o ciclo de empacotamento de contexto via *Repomix*, integrando *Git Hooks* (pré e pós-commit) e regras comportamentais de *Harness* (Antigravity, Cursor, Claude Code, Aider). 

A meta é eliminar a exploração cega do repositório por agentes autônomos, consolidando a árvore de símbolos em um único payload estruturado em XML com numeração de linhas e aproveitamento máximo de *Prompt Caching*.

#v(8pt)

== 2. Arquitetura do Fluxo Operacional

#rect(
  fill: surface,
  stroke: 1pt + border-color,
  inset: 12pt,
  radius: 3pt,
  width: 100%
)[
  #text(weight: "bold", fill: brand-dark)[FLUXO A · Pré-Ativação do Agente (Context Hook / Governança)]
  
  1. *Prompt do Operador:* O usuário dispara uma solicitação de refatoração ou criação de feature.
  2. *Intercepção de Governança:* A regra em `AGENTS.md` e a skill `lean-ctx` impedem o agente de rodar varreduras cegas (`list_dir`, múltiplos `view_file`).
  3. *Leitura Única do Snapshot:* O agente consome `repomix-output.xml` em 1 única chamada estruturada.
  4. *Ativação de Prompt Caching:* As LLMs (Anthropic, OpenAI, Gemini) aplicam desconto de até 90% no cache de prefixo nos turnos seguintes.

  #v(6pt)
  #line(length: 100%, stroke: 0.5pt + border-color)
  #v(6pt)

  #text(weight: "bold", fill: brand-accent)[FLUXO B · Pós-Modificação / Ciclo Git (Post-Hook Automático)]
  
  1. *Entrega do Código:* O operador ou o subagente finaliza as alterações e executa o `git commit`.
  2. *Disparo do Hook:* O hook `.git/hooks/post-commit` é acionado de forma assíncrona.
  3. *Regeneração Incremental:* O script executa `npx repomix` em menos de 1 segundo, atualizando o snapshot.
  4. *Estado em Disco Atualizado:* O repositório está pronto e sincronizado para a próxima sessão de IA.
]

#v(8pt)

== 3. Detalhamento das 3 Fases de Implementação

=== Fase 1: Configuração Fina do Repomix (`repomix.config.json`)
Criação de um arquivo de configuração declarativo na raiz para isolar apenas o código essencial:
- *Inclusões Estratégicas:* `src/**`, `scripts/**`, `.claude/skills/**`, `docs/**`.
- *Exclusões Rígidas:* `package-lock.json`, `node_modules`, pastas de build (`dist/`, `output/`, `.git/`), assets pesados e binários.
- *Formato de Saída:* `xml` com numeração de linhas (`output.parsableStyle = true`) para eliminar alucinações de arquivos.

=== Fase 2: Automação via Git Hooks (Pós-Commit)
- *Hook:* `scripts/hooks/post-commit` copiado para `.git/hooks/post-commit`.
- *Script Executor:* `scripts/gerar-contexto-repomix.py` com execução determinística e tratamento de erro silencioso em background.
- *Idempotência:* A reexecução do hook não corrompe o estado e roda em microssegundos.

=== Fase 3: Direcionamento do Harness & Governança
- *Regra em `AGENTS.md`:* Proíbe explicitamente chamadas em loop de ferramentas de busca quando o snapshot estiver disponível.
- *Skill `repomix-navigator`:* Injeta a diretiva de priorizar a consulta ao XML empacotado para mapeamento de dependências e contratos.

#v(8pt)

== 4. Matriz de Entregáveis

#table(
  columns: (1.5fr, 1fr, 2fr, 2.5fr),
  fill: (x, y) => if y == 0 { brand-dark } else if calc.even(y) { surface } else { white },
  stroke: 0.5pt + border-color,
  align: (left, center, left, left),
  table.header(
    text(white, weight: "bold")[Componente],
    text(white, weight: "bold")[Tipo],
    text(white, weight: "bold")[Localização],
    text(white, weight: "bold")[Responsabilidade]
  ),
  [`repomix.config.json`], [Config], [`/repomix.config.json`], [Filtros, exclusões e estilo XML.],
  [`post-commit`], [Git Hook], [`scripts/hooks/post-commit`], [Regenera o snapshot após cada commit.],
  [`gerar-contexto.py`], [Script], [`scripts/gerar-contexto.py`], [Execução local do Repomix em background.],
  [`Regra no AGENTS.md`], [Governança], [`/AGENTS.md`], [Força o agente a usar o snapshot antes de explorar.]
)

#v(10pt)

#align(center)[
  #text(8.5pt, fill: rgb("#68738A"))[
    Documento compilado via Typst · Fábrica Universal · Soberania Tecnológica & Automação Agêntica
  ]
]
