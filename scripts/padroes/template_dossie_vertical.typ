// Template Typst Institucional Diamante: Dossiê Vertical de Desmantelamento SaaS (R5-V)
#set page(
  paper: "a4",
  margin: (x: 1.6cm, y: 1.8cm),
  header: context [
    #if counter(page).get().first() > 1 [
      #grid(
        columns: (1fr, 1fr),
        align(left)[#text(7pt, fill: rgb("#64748B"))[Dossiê Vertical de Desmantelamento SaaS · Quinteto Soberano]],
        align(right)[#text(7pt, fill: rgb("#64748B"))[Padrão Diamante R5-V · Fábrica Universal]]
      )
      #v(-2pt)
      #line(length: 100%, stroke: 0.3pt + rgb("#CBD5E1"))
    ]
  ],
  footer: context [
    #line(length: 100%, stroke: 0.3pt + rgb("#CBD5E1"))
    #v(2pt)
    #grid(
      columns: (1fr, 1fr),
      align(left)[#text(7pt, fill: rgb("#64748B"))[Soberania Tecnológica & Migração de Dados]],
      align(right)[#text(7.5pt, fill: rgb("#0F172A"), weight: "bold")[Página #counter(page).display() de #counter(page).final().first()]]
    )
  ]
)

#set text(
  font: "Liberation Sans",
  size: 8.5pt,
  lang: "pt",
  fill: rgb("#0F172A"),
  hyphenate: true
)

#set par(justify: true, leading: 0.58em, spacing: 0.95em)

// Títulos
#show heading.where(level: 1): it => {
  v(12pt)
  text(13.5pt, weight: "bold", fill: rgb("#1A446C"), it.body)
  v(6pt)
}
#show heading.where(level: 2): it => {
  v(10pt)
  text(10.5pt, weight: "bold", fill: rgb("#0F172A"), it.body)
  v(5pt)
}

// Configuração Rígida de Tabelas Anti-Sobreposição (Padrão Diamante R5-V)
#show table.cell: it => {
  set text(size: 6.8pt, hyphenate: true)
  set par(justify: false, leading: 0.4em)
  it
}

#set table(
  stroke: 0.4pt + rgb("#CBD5E1"),
  fill: (x, y) => if y == 0 { rgb("#1A446C") } else if calc.even(y) { rgb("#F8FAFC") } else { none },
  inset: (x: 4pt, y: 3.5pt)
)

#show table.cell.where(y: 0): set text(fill: white, weight: "bold", size: 7pt)

// Blocos de Código
#show raw.where(block: true): it => block(
  fill: rgb("#0F172A"),
  inset: 6pt,
  radius: 3pt,
  width: 100%,
  breakable: true,
  text(size: 6.5pt, fill: rgb("#E2E8F0"), it)
)

// Citações / Caixas de Alvo SaaS
#show quote: it => block(
  fill: rgb("#FEF2F2"),
  stroke: (left: 3pt + rgb("#EF4444")),
  inset: (x: 8pt, y: 6pt),
  radius: (right: 3pt),
  width: 100%,
  text(size: 8pt, fill: rgb("#991B1B"), it.body)
)
