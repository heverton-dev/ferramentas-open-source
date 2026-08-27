#let gerar_trilha_typst(
  produto_foco: "Screenpipe",
  tempo_total: "7 horas",
  fases: ()
) = {
  set page(
    paper: "a4",
    margin: (x: 1.8cm, y: 2.0cm),
    header: align(right)[
      #text(8pt, fill: rgb("#68738A"), font: "Liberation Sans")[
        Fábrica Universal · Trilha Pedagógica de Aprendizado · 2026
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

  set text(
    font: "Liberation Sans",
    size: 9.5pt,
    lang: "pt",
    fill: rgb("#151A26")
  )

  set par(justify: true, leading: 0.6em)

  let brand-dark = rgb("#1A446C")
  let brand-light = rgb("#DCE7F2")
  let brand-accent = rgb("#0284C7")
  let surface = rgb("#F8F9FC")
  let border-color = rgb("#CBD5E1")

  // Cabeçalho
  align(center)[
    #block(
      fill: brand-light,
      inset: 12pt,
      radius: 4pt,
      stroke: 1pt + brand-dark,
      width: 100%,
      [
        #text(9pt, weight: "bold", fill: brand-dark, tracking: 0.1em)[
          ROTEIRO PEDAGÓGICO & JORNADA AUTOGUIADA DE CAPACITAÇÃO
        ]
        #v(4pt)
        #text(16pt, weight: "bold", fill: rgb("#0E1118"))[
          Trilha Cronológica de Aprendizado: #produto_foco
        ]
        #v(3pt)
        #text(9pt, fill: rgb("#3B4457"))[
          Imersão Completa a Partir das Fontes Primárias · Tempo Estimado: #tempo_total
        ]
      ]
    )
  ]

  v(10pt)

  for f in fases [
    #block(
      fill: surface,
      stroke: 0.5pt + border-color,
      inset: 10pt,
      radius: 4pt,
      width: 100%,
      [
        #text(11pt, weight: "bold", fill: brand-dark)[#f.titulo] #h(6pt) #text(8pt, fill: brand-accent)[[⏱️ #f.tempo_estimado]]
        #v(2pt)
        #text(8.5pt, fill: rgb("#475569"))[*Meta:* #f.objetivo]
        #v(6pt)
        #for r in f.recursos [
          #block(
            fill: white,
            stroke: 0.5pt + rgb("#E2E8F0"),
            inset: 6pt,
            radius: 2pt,
            width: 100%,
            [
              [#text(weight: "bold")[#r.titulo]] #h(4pt) #text(7.5pt, fill: rgb("#B45309"))[[#r.tipo_midia · #r.fonte_id]] \
              #text(8pt, fill: rgb("#1E293B"))[💡 #r.aprendizado_chave] \
              #text(7.5pt, fill: rgb("#64748B"))[⏱️ #r.duracao · 👤 #r.autor]
            ]
          )
          #v(3pt)
        ]
      ]
    )
    #v(6pt)
  ]
}
