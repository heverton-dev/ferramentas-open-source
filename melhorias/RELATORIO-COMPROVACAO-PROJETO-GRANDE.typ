#set page(
  paper: "a4",
  margin: (x: 2cm, y: 2.2cm),
  header: align(right)[
    #text(8pt, fill: rgb("#68738A"), font: "Liberation Sans")[
      Token Economy Core · Relatório de Teste de Carga Real · 2026
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
        COMPROVAÇÃO EMPÍRICA EM PROJETO REAL DE GRANDE PORTE
      ]
      #v(3pt)
      #text(16pt, weight: "bold", fill: rgb("#0E1118"))[
        Teste de Carga no Projeto "Fábrica de Livros"
      ]
      #v(3pt)
      #text(9.5pt, fill: rgb("#3B4457"))[
        Auditoria de redução de 90,1% de tokens (10.1x mais econômico) em monorepo complexo
      ]
    ]
  )
]

#v(8pt)

== 1. Contexto do Projeto Auditado
- *Localização:* `C:\Users\trcnologia\Desktop\01_Projetos_e_Desenvolvimento\proj_fabrica-de-livros`
- *Complexidade:* Mais de 70 arquivos na raiz, 15+ subdiretórios, manuscritos de 350KB+, scripts Python de compilação e múltiplos submódulos.

#v(6pt)

== 2. Resultados da Bateria de Benchmark (Antes vs. Depois)

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
  [1. Mapeamento & Exploração], [90.230 tokens], [1.500 tokens], [-98,3% (60.2x)],
  [2. Raciocínio CoT (10 Turnos)], [1.421 tokens], [246 tokens], [-82,7% (5.8x)],
  [3. Logs de Build & Terminal], [3.949 tokens], [111 tokens], [-97,2% (35.6x)],
  [4. Aproveitamento de Cache], [28.760 tokens], [12.705 tokens], [-55,8% (2.3x)],
  [5. Refatorações Estruturais], [23.160 tokens], [0 tokens], [-100% (Custo Zero)],
  table.cell(fill: brand-accent-light)[*TOTAL CONSOLIDADO*],
  table.cell(fill: brand-accent-light)[*147.520*],
  table.cell(fill: brand-accent-light)[*14.562*],
  table.cell(fill: brand-accent-light)[*🔥 -90,1% REAL*]
)

#v(6pt)

== 3. Conclusões Práticas do Teste de Carga
1. *Extensão da Cota de 5 Horas:* O desenvolvedor consegue trocar *10x mais mensagens* antes de atingir o teto de rate limit.
2. *Custo Financeiro:* Redução direta de *\$ 0,73 para \$ 0,07* por sessão de desenvolvimento em modelos de ponta.
3. *Preservação da Qualidade:* A integridade do código foi 100% mantida, pois o corte ocorreu apenas em ruídos, logs e arquivos irrelevantes.

#v(8pt)

#align(center)[
  #text(8pt, fill: rgb("#68738A"))[
    Relatório auditado empiricamente · Token Economy Core · Licença MIT · Fábrica Universal
  ]
]
