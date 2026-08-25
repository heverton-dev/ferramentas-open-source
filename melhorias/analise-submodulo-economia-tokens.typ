#set page(
  paper: "a4",
  margin: (x: 2cm, y: 2.2cm),
  header: align(right)[
    #text(8pt, fill: rgb("#68738A"), font: "Liberation Sans")[
      Fábrica Universal · Engenharia de Contexto & Economia de Tokens · 2026
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
  size: 10pt,
  lang: "pt",
  fill: rgb("#151A26")
)

#set par(justify: true, leading: 0.6em)

// Cores do Design System
#let brand-dark = rgb("#1A446C")
#let brand-light = rgb("#DCE7F2")
#let brand-accent = rgb("#1B5E3B")
#let brand-accent-light = rgb("#D8EFE2")
#let flag-dark = rgb("#8E2436")
#let flag-light = rgb("#F0D9DD")
#let surface = rgb("#F8F9FC")
#let border-color = rgb("#C7CEDB")

// Cabeçalho Principal
#align(center)[
  #block(
    fill: brand-light,
    inset: 12pt,
    radius: 4pt,
    stroke: 1pt + brand-dark,
    width: 100%,
    [
      #text(9pt, weight: "bold", fill: brand-dark, tracking: 0.1em)[
        ESTUDO TÉCNICO DE ARQUITETURA AGÊNTICA
      ]
      #v(3pt)
      #text(16pt, weight: "bold", fill: rgb("#0E1118"))[
        Submódulo Git Universal de Economia de Tokens & Qualidade Contínua
      ]
      #v(3pt)
      #text(9pt, fill: rgb("#3B4457"))[
        Integração harmônica das ferramentas da Camada 01, skills de disciplina e automação multi-IDE
      ]
    ]
  )
]

#v(8pt)

== 1. O Dilema: Economia Agressiva vs. Preservação da Qualidade

A economia cega emburrece a IA. Quando se removem assinaturas de tipos ou se trunca o código de saída, o agente perde precisão. A engenharia moderna adota a *Compressão Assimétrica*:

#grid(
  columns: (1fr, 1fr),
  gutter: 10pt,
  rect(fill: brand-accent-light, stroke: 1pt + brand-accent, inset: 10pt, radius: 3pt)[
    #text(weight: "bold", fill: brand-accent)[🟢 ONDE CORTAR ATÉ 90% (Zero Perda)]
    - *Pensamento CoT Interno:* Skill `caveman` (telegráfico de 3 linhas).
    - *Logs de Terminal:* Skill `headroom` (3 topo + 4 fim).
    - *Navegação de Código:* `code-review-graph` e `ast-grep`.
    - *Prefixos Estáticos:* Prompt Caching via Repomix.
    - *Respostas Repetidas:* Cache Semântico via LiteLLM.
  ],
  rect(fill: flag-light, stroke: 1pt + flag-dark, inset: 10pt, radius: 3pt)[
    #text(weight: "bold", fill: flag-dark)[🔴 O QUE É SAGRADO (Regra R7)]
    - *Código de Entrega Final:* Nunca resumir/truncar.
    - *Assinaturas de Tipos:* TypeScript / Pydantic íntegros.
    - *Mensagens de Erro de Testes:* Stack traces completos.
    - *Schemas de Validação:* `Outlines` e `Instructor` estritos.
  ]
)

#v(6pt)

== 2. Pipeline Unificado em 4 Camadas de Eficiência

#rect(fill: surface, stroke: 1pt + border-color, inset: 10pt, radius: 3pt, width: 100%)[
  *1. Entrada & Filtragem (Pre-Flight):* `Repomix` e `Tree-sitter` filtram binários e lockfiles; `LiteLLM` verifica cache semântico antes de chamar APIs comerciais.
  
  *2. Raciocínio & Execução:* `SGLang` reaproveita KV-Cache na GPU; a skill `caveman` enxuga o raciocínio interno; `ast-grep` faz refatorações determinísticas com zero custo de LLM.
  
  *3. Validação Estruturada:* `Outlines` / `Instructor` forçam respostas em JSON matematicamente perfeito no primeiro turno, eliminando retentativas.
  
  *4. Pós-Execução & Git:* A skill `headroom` comprime os logs de teste; o Git Hook `post-commit` atualiza o snapshot em background; a skill `rtk-memory` persiste aprendizados.
]

#v(6pt)

== 3. Estrutura do Submódulo Git: `token-economy-core`

O submódulo foi desenhado para ser plugado em qualquer projeto via `git submodule add`:

- `.claude/skills/`: Contém as skills agênticas universais (`caveman`, `headroom`, `lean-ctx`, `rtk-memory`, `repomix-nav`).
- `configs/`: Modelos de `repomix.config.json` e `litellm.config.yaml`.
- `hooks/`: Git hook `post-commit` para atualização assíncrona do snapshot.
- `scripts/`: Scripts multiplataforma (`setup-links.ps1` e `setup-links.sh`) que criam symlinks e junctions multi-IDE automaticamente.
- `AGENTS-TEMPLATE.md`: Governança universal com as regras R1 a R17.

#v(6pt)

== 4. Matriz de Implicações & Riscos Mitigados

#table(
  columns: (1.5fr, 2fr, 2.5fr),
  fill: (x, y) => if y == 0 { brand-dark } else if calc.even(y) { surface } else { white },
  stroke: 0.5pt + border-color,
  align: (left, left, left),
  table.header(
    text(white, weight: "bold")[Risco],
    text(white, weight: "bold")[Causa],
    text(white, weight: "bold")[Solução Arquitetural]
  ),
  [Alucinação por Poda], [Truncamento excessivo de tipos], [Tree-sitter & Repomix preservam contratos e descartam corpos.],
  [Quebra de Cache], [Alterar system prompt todo turno], [Skill `rtk-memory` grava aprendizados no scratchpad externo.],
  [Lentidão no Git], [Repomix síncrono no commit], [Execução do hook em background assíncrono (< 50ms).],
  [Lockfiles no Prompt], [Envio de 20k linhas de lockfile], [Exclusão nativa via `repomix.config.json` padronizado.]
)

#v(8pt)

#align(center)[
  #text(8pt, fill: rgb("#68738A"))[
    Documento compilado via Typst · Fábrica Universal · Soberania Tecnológica & Automação Agêntica
  ]
]
