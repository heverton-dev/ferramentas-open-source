#set page(
  paper: "a4",
  margin: (x: 2cm, y: 2.2cm),
  header: align(right)[
    #text(8pt, fill: rgb("#68738A"), font: "Liberation Sans")[
      Token Economy Core · Manual de Instalação & Uso · 2026
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

// Cores
#let brand-dark = rgb("#1A446C")
#let brand-light = rgb("#DCE7F2")
#let brand-accent = rgb("#1B5E3B")
#let brand-accent-light = rgb("#D8EFE2")
#let surface = rgb("#F8F9FC")
#let border-color = rgb("#C7CEDB")

#align(center)[
  #block(
    fill: brand-light,
    inset: 12pt,
    radius: 4pt,
    stroke: 1pt + brand-dark,
    width: 100%,
    [
      #text(9pt, weight: "bold", fill: brand-dark, tracking: 0.1em)[
        GUIA DEFINITIVO DO SUBMÓDULO UNIVERSAL
      ]
      #v(3pt)
      #text(16pt, weight: "bold", fill: rgb("#0E1118"))[
        Token Economy Core — Manual Passo a Passo
      ]
      #v(3pt)
      #text(9.5pt, fill: rgb("#3B4457"))[
        Como reduzir até 95% do gasto de tokens com IA em Projetos Existentes e Novos
      ]
    ]
  )
]

#v(8pt)

== 1. O que é o Token Economy Core?
O *Token Economy Core* é um submódulo Git plugável e universal que instala regras inteligentes, filtros de empacotamento e skills de disciplina agêntica em qualquer projeto com *apenas 1 comando*.

#v(6pt)

== 2. Resultados Comprovados em Testes Empíricos

#table(
  columns: (2.5fr, 1.5fr, 1.5fr, 2fr),
  fill: (x, y) => if y == 0 { brand-dark } else if calc.even(y) { surface } else { white },
  stroke: 0.5pt + border-color,
  align: (left, center, center, center),
  table.header(
    text(white, weight: "bold")[Cenário de Teste],
    text(white, weight: "bold")[Sem Módulo],
    text(white, weight: "bold")[Com Módulo],
    text(white, weight: "bold")[Economia Real]
  ),
  [1. Mapeamento do Projeto], [251.012 tokens], [1.500 tokens], [-99,4% (167x)],
  [2. Pensamento do Agente (CoT)], [1.421 tokens], [246 tokens], [-82,7% (5.8x)],
  [3. Logs de Build & Terminal], [3.949 tokens], [111 tokens], [-97,2% (35.6x)],
  [4. Aproveitamento de Cache], [28.760 tokens], [12.705 tokens], [-55,8% (2.3x)],
  [5. Refatorações Estruturais], [23.160 tokens], [0 tokens], [-100% (Custo Zero)],
  table.cell(fill: brand-accent-light)[*TOTAL CONSOLIDADO*],
  table.cell(fill: brand-accent-light)[*308.302*],
  table.cell(fill: brand-accent-light)[*14.562*],
  table.cell(fill: brand-accent-light)[*🔥 -95,3% REAL*]
)

#v(6pt)

== 3. Guia de Instalação para os 2 Cenários

=== 📂 CENÁRIO 1: Em um Projeto que JÁ EXISTE (100% Não-Destrutivo)
*Garantia de Segurança:* O instalador preserva seus arquivos existentes. Se você já tem uma pasta `.claude/skills/` ou um `repomix.config.json`, ele apenas adiciona o que falta, sem sobrescrever nada.

```powershell
# 1. Navegue até a pasta do seu projeto
cd C:\caminho\do\seu-projeto

# 2. Adicione o submódulo
git submodule add https://github.com/Heverton-web/token-economy-core.git .token-economy

# 3. Execute o instalador automático
powershell -ExecutionPolicy Bypass -File .token-economy\scripts\setup-links.ps1
```

=== 🆕 CENÁRIO 2: Em um Projeto NOVO (Começando do Zero)
```powershell
# 1. Crie a pasta e inicialize o Git
mkdir meu-novo-projeto; cd meu-novo-projeto; git init

# 2. Adicione o submódulo
git submodule add https://github.com/Heverton-web/token-economy-core.git .token-economy

# 3. Execute o instalador e copie o template de governança
powershell -ExecutionPolicy Bypass -File .token-economy\scripts\setup-links.ps1
copy .token-economy\AGENTS-TEMPLATE.md AGENTS.md
```

#v(6pt)

== 4. O que o Módulo Ativa no seu Projeto?
1. *`repomix.config.json`:* Filtra automaticamente lockfiles, binários, imagens e pastas `dist/` e `node_modules/`.
2. *Git Hook `post-commit`:* Atualiza o snapshot do projeto em background em menos de 1 segundo a cada commit.
3. *5 Skills de Economia em `.claude/skills/`:* `caveman` (pensamento telegráfico), `headroom` (logs enxutos), `lean-ctx` (fatiamento de leitura), `rtk-memory` (estabilidade de cache) e `repomix-navigator` (visão macro).

#v(8pt)

#align(center)[
  #text(8pt, fill: rgb("#68738A"))[
    Token Economy Core · Repositório Oficial: github.com/Heverton-web/token-economy-core · Licença MIT
  ]
]
