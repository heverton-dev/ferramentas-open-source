#let gerar_relatorio_execucao_typst(
  produto_foco: "Screenpipe",
  saas_origem: "Granola",
  data_execucao: "27-08-2026",
  horario_inicio: "12:08:14",
  horario_fim: "12:08:31",
  tempo_total: "17s",
  harness: "Antigravity Multi-Agent Harness · Fábrica Universal",
  llm: "Claude 3.5 Sonnet / Gemini 2.0 Pro (model: inherit)",
  tools: (),
  skills: (),
  tokens_input: "4.500",
  tokens_output: "1.200",
  tokens_total: "5.700",
  taxa_economia: "92%",
  materiais: (),
  gates: ()
) = {
  set page(
    paper: "a4",
    margin: (x: 1.8cm, y: 2.0cm),
    header: align(right)[
      #text(8pt, fill: rgb("#68738A"), font: "Liberation Sans")[
        Fábrica Universal · Relatório de Execução & Telemetria · #data_execucao
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
    size: 9pt,
    lang: "pt",
    fill: rgb("#151A26")
  )

  set par(justify: true, leading: 0.58em)

  let brand-dark = rgb("#1A446C")
  let brand-light = rgb("#DCE7F2")
  let brand-accent = rgb("#0284C7")
  let brand-green = rgb("#10B981")
  let surface = rgb("#F8F9FC")
  let border-color = rgb("#CBD5E1")

  // Cabeçalho
  align(center)[
    #block(
      fill: brand-light,
      inset: 11pt,
      radius: 4pt,
      stroke: 1pt + brand-dark,
      width: 100%,
      [
        #text(8.5pt, weight: "bold", fill: brand-dark, tracking: 0.1em)[
          RELATÓRIO OFICIAL DE EXECUÇÃO, TELEMETRIA & AUDITORIA DE FLUXO
        ]
        #v(3pt)
        #text(15pt, weight: "bold", fill: rgb("#0E1118"))[
          #produto_foco · Telemetria do Fluxo Operacional
        ]
        #v(3pt)
        #text(8.5pt, fill: rgb("#3B4457"))[
          Data: #data_execucao · Horário: #horario_inicio às #horario_fim (Duração: #tempo_total) · SaaS Origem: #saas_origem
        ]
      ]
    )
  ]

  v(6pt)

  // Hero Stats de Telemetria
  table(
    columns: (1.2fr, 1.2fr, 1.2fr, 1.4fr),
    fill: (x, y) => if y == 0 { brand-dark } else { surface },
    stroke: 0.5pt + border-color,
    [#text(weight: "bold", fill: white)[Tempo de Execução]],
    [#text(weight: "bold", fill: white)[Tokens Consumidos]],
    [#text(weight: "bold", fill: white)[Economia Tokens]],
    [#text(weight: "bold", fill: white)[Modelo LLM]],
    [#tempo_total \ (#horario_inicio -> #horario_fim)],
    [Total: #tokens_total \ (In: #tokens_input · Out: #tokens_output)],
    [#text(weight: "bold", fill: rgb("#065F46"))[#taxa_economia] \ (via Determinismo)],
    [#text(7.5pt)[#llm]]
  )

  v(8pt)
  [== 1. Ambiente de Engenharia & Ferramentas Utilizadas]
  v(3pt)

  block(
    fill: surface,
    stroke: 0.5pt + border-color,
    inset: 8pt,
    radius: 3pt,
    width: 100%,
    [
      *Harness Orquestrador:* #harness \
      #v(2pt)
      *Tools Acionadas no Fluxo:* #tools.join(" · ") \
      #v(2pt)
      *Skills de Economia & Eficiência:* #skills.join(" · ")
    ]
  )

  v(6pt)
  [== 2. Quadro de Conformidade dos Gates Mecânicos]
  v(3pt)

  table(
    columns: (1.5fr, 1fr, 3.5fr),
    fill: (x, y) => if y == 0 { brand-dark } else if calc.even(y) { surface } else { none },
    stroke: 0.5pt + border-color,
    [#text(weight: "bold", fill: white)[Gate Mecânico]],
    [#text(weight: "bold", fill: white)[Resultado]],
    [#text(weight: "bold", fill: white)[Critério Auditado]],
    ..gates.map(g => (
      [#text(weight: "bold", fill: brand-accent)[#g.nome]],
      [#text(weight: "bold", fill: rgb("#065F46"))[#g.status]],
      [#g.descricao]
    )).flatten()
  )

  v(6pt)
  [== 3. Materiais Entregues no Pacote da Ferramenta]
  v(3pt)

  table(
    columns: (1.2fr, 2.5fr, 0.8fr, 1.5fr),
    fill: (x, y) => if y == 0 { brand-dark } else if calc.even(y) { surface } else { none },
    stroke: 0.5pt + border-color,
    [#text(weight: "bold", fill: white)[Tipo do Material]],
    [#text(weight: "bold", fill: white)[Nome do Arquivo]],
    [#text(weight: "bold", fill: white)[Formato]],
    [#text(weight: "bold", fill: white)[Pasta de Destino]],
    ..materiais.map(m => (
      [#m.tipo],
      [#text(7.5pt, font: "Courier New")[#m.nome]],
      [#text(weight: "bold", fill: brand-accent)[#m.formato]],
      [#text(7.5pt)[#m.pasta]]
    )).flatten()
  )
}
