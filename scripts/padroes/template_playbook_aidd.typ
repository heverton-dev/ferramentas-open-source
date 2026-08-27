// Template Typst Institucional para o Playbook Mestre AIDD
// Elimina 100% de sobreposições em tabelas e blocos de código
#set page(
  paper: "a4",
  margin: (x: 1.6cm, y: 1.8cm),
  header: context [
    #if counter(page).get().first() > 1 [
      #grid(
        columns: (1fr, 1fr),
        align(left)[#text(7pt, fill: rgb("#64748B"))[Playbook Mestre · Engenharia Agêntica & AIDD]],
        align(right)[#text(7pt, fill: rgb("#64748B"))[Fábrica Universal · Versão 1.0.0]]
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
      align(left)[#text(7pt, fill: rgb("#64748B"))[Confidencial · Arquitetura de Sistemas Autônomos]],
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

#set par(justify: true, leading: 0.52em)

// Macros auxiliares do Pandoc
#let horizontalrule = line(length: 100%, stroke: 0.5pt + rgb("#CBD5E1"))

// Títulos
#show heading.where(level: 1): it => {
  v(14pt)
  text(14pt, weight: "bold", fill: rgb("#1A446C"), it.body)
  v(8pt)
}
#show heading.where(level: 2): it => {
  v(11pt)
  text(11pt, weight: "bold", fill: rgb("#0F172A"), it.body)
  v(6pt)
}
#show heading.where(level: 3): it => {
  v(8pt)
  text(9.5pt, weight: "bold", fill: rgb("#334155"), it.body)
  v(4pt)
}

// Configuração Rígida de Tabelas Anti-Sobreposição
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

// Código Inline
#show raw.where(block: false): it => box(
  fill: rgb("#F1F5F9"),
  inset: (x: 2pt, y: 0.5pt),
  radius: 1.5pt,
  text(size: 6.8pt, fill: rgb("#0F172A"), it)
)

// Citações / Blockquotes
#show quote: it => block(
  fill: rgb("#F0F9FF"),
  stroke: (left: 2.5pt + rgb("#0284C7")),
  inset: (x: 8pt, y: 5pt),
  radius: (right: 2pt),
  width: 100%,
  text(size: 8pt, fill: rgb("#0369A1"), it.body)
)
