#let gerar_manual_typst(
  produto_foco: "Screenpipe",
  versao: "0.1.0",
  licenca_osi: "Apache-2.0",
  vps_modelo: "Hetzner Cloud CPX31",
  vps_specs: "4 vCPU AMD · 8 GB RAM · 160 GB NVMe",
  vps_so: "Ubuntu 24.04 LTS",
  vps_custo: "EUR 14,00/mês (~R$ 84,00/mês)",
  nivelamento: (),
  passos: (),
  primeiro_voo: (),
  comandos_cli: (),
  troubleshooting: (),
  desinstalacao: (),
  referencias: ()
) = {
  set page(
    paper: "a4",
    margin: (x: 1.8cm, y: 2.0cm),
    header: align(right)[
      #text(8pt, fill: rgb("#68738A"), font: "Liberation Sans")[
        Fábrica Universal · Manual Operacional Hiperdidático · 2026
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

  set par(justify: true, leading: 0.58em, spacing: 0.95em)

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
          MANUAL OPERACIONAL DE PRODUÇÃO & GUIA DIDÁTICO PARA INICIANTES
        ]
        #v(3pt)
        #text(15pt, weight: "bold", fill: rgb("#0E1118"))[
          #produto_foco · Instalação VPS & Manual de Uso Exaustivo
        ]
        #v(3pt)
        #text(8.5pt, fill: rgb("#3B4457"))[
          Nivelamento Conceitual · Hardening VPS à Prova de Erros · Roteiro de Primeiro Voo · Fontes Verificadas
        ]
      ]
    )
  ]

  v(6pt)

  // Tabela Hero Stats VPS
  table(
    columns: (1.2fr, 1.5fr, 1.2fr, 1.1fr),
    fill: (x, y) => if y == 0 { brand-dark } else { surface },
    stroke: 0.5pt + border-color,
    [#text(weight: "bold", fill: white)[VPS Recomendada]],
    [#text(weight: "bold", fill: white)[Hardware & SO]],
    [#text(weight: "bold", fill: white)[Custo Estimado]],
    [#text(weight: "bold", fill: white)[Licença de Uso]],
    [#vps_modelo], [#vps_specs \ #vps_so], [#vps_custo], [#licenca_osi]
  )

  v(8pt)
  [== Módulo 0: Nivelamento Conceitual (Analogias do Cotidiano)]
  v(3pt)

  for n in nivelamento [
    #block(
      fill: surface,
      stroke: 0.5pt + border-color,
      inset: 7pt,
      radius: 3pt,
      width: 100%,
      [
        #text(weight: "bold", fill: rgb("#6D28D9"))[💡 #n.termo] #h(4pt) #text(7.5pt, fill: rgb("#4C1D95"))[(Analogia: #n.analogia_cotidiana)] \
        #text(8.5pt, fill: rgb("#334155"))[#n.explicacao_simples]
      ]
    )
    #v(2pt)
  ]

  v(6pt)
  [== Parte I: Instalação Guiada em Produção na VPS (Passo a Passo Rígido)]
  v(3pt)

  for p in passos [
    #block(
      stroke: 0.5pt + border-color,
      inset: 8pt,
      radius: 3pt,
      width: 100%,
      [
        #text(weight: "bold", fill: brand-dark)[Passo #p.numero: #p.titulo] #h(4pt) #text(7.5pt, fill: brand-accent)[[#p.fonte_id]] \
        #text(8.5pt)[#p.descricao] \
        #if p.keys().contains("analogia") and p.analogia != "" [
          #text(8pt, fill: rgb("#065F46"))[*Analogia:* #p.analogia] \
        ]
        #v(2pt)
        #block(
          fill: rgb("#0F172A"),
          inset: 6pt,
          radius: 2pt,
          width: 100%,
          [#text(7.5pt, fill: white, font: "Courier New")[#raw(p.comandos)]]
        )
        #if p.keys().contains("como_saber_se_deu_certo") and p.como_saber_se_deu_certo != "" [
          #v(1pt)
          #text(8pt, fill: rgb("#1E40AF"))[✅ *Validação:* #p.como_saber_se_deu_certo]
        ]
      ]
    )
    #v(3pt)
  ]

  v(6pt)
  [== Parte II: Roteiro de Primeiro Voo (Sua Primeira Reunião em 3 Minutos)]
  v(3pt)

  for pv in primeiro_voo [
    #block(
      fill: surface,
      stroke: 0.5pt + border-color,
      inset: 6pt,
      radius: 3pt,
      width: 100%,
      [
        #text(weight: "bold", fill: brand-accent)[#pv.passo:] #text(8.5pt)[#pv.acao] \
        #text(8pt, fill: rgb("#065F46"))[🎯 *Resultado Esperado:* #pv.resultado_esperado]
      ]
    )
    #v(2pt)
  ]

  v(6pt)
  [== Parte III: Dicionário de Linha de Comando (CLI)]
  v(3pt)

  table(
    columns: (1.5fr, 2.5fr, 1.5fr),
    fill: (x, y) => if y == 0 { brand-dark } else if calc.even(y) { surface } else { none },
    stroke: 0.5pt + border-color,
    [#text(weight: "bold", fill: white)[Comando / Flag]],
    [#text(weight: "bold", fill: white)[Finalidade Técnica]],
    [#text(weight: "bold", fill: white)[Exemplo de Execução]],
    ..comandos_cli.map(c => (
      [#text(weight: "bold", fill: brand-accent)[#c.comando]],
      [#c.descricao],
      [#text(7.5pt, font: "Courier New")[#c.exemplo]]
    )).flatten()
  )

  if desinstalacao != () [
    #v(8pt)
    #pagebreak()
    [== Parte IV: Desinstalação Cirúrgica & Isolamento da VPS (Zero Efeito Colateral)]
    #v(3pt)
    #block(
      fill: rgb("#EFF6FF"),
      inset: 8pt,
      radius: 4pt,
      stroke: 0.8pt + brand-accent,
      width: 100%,
      [
        #text(weight: "bold", fill: brand-dark)[🛡️ Princípio de Isolamento da VPS:] \
        #text(8.5pt, fill: rgb("#1E293B"))[#desinstalacao.principio_isolamento]
      ]
    )
    #v(4pt)
    #for p in desinstalacao.passos [
      #block(
        fill: surface,
        inset: 7pt,
        radius: 4pt,
        stroke: 0.5pt + border-color,
        width: 100%,
        [
          #text(weight: "bold", fill: brand-accent)[Passo #p.numero · #p.titulo] \
          #text(8.5pt)[#p.descricao] \
          #v(2pt)
          #block(fill: rgb("#0F172A"), inset: 5pt, radius: 3pt, width: 100%)[
            #text(fill: rgb("#34D399"), font: "Courier New", size: 7.5pt)[#p.comandos]
          ]
          #v(1pt)
          #text(7.5pt, fill: rgb("#B45309"))[⚠️ *Alerta de Segurança:* #p.alerta_seguranca] \
          #text(7.5pt, fill: rgb("#047857"))[✅ *Como Validar:* #p.como_validar]
        ]
      )
      #v(3pt)
    ]
    #v(4pt)
    #block(
      fill: rgb("#F0FDF4"),
      inset: 8pt,
      radius: 4pt,
      stroke: 0.8pt + brand-green,
      width: 100%,
      [
        #text(weight: "bold", fill: rgb("#065F46"))[🩺 Checklist de Saúde da VPS (Outros Projetos):] \
        #for c in desinstalacao.checklist_saude_vps [
          - #text(8pt, font: "Courier New", fill: rgb("#1E293B"))[#c]
        ]
      ]
    )
  ]

  v(6pt)
  [== Parte V: Referências Bibliográficas Auditadas]
  v(3pt)

  table(
    columns: (0.6fr, 1.2fr, 2.5fr, 1.7fr),
    fill: (x, y) => if y == 0 { brand-dark } else if calc.even(y) { surface } else { none },
    stroke: 0.5pt + border-color,
    [#text(weight: "bold", fill: white)[ID]],
    [#text(weight: "bold", fill: white)[Categoria]],
    [#text(weight: "bold", fill: white)[Título da Fonte]],
    [#text(weight: "bold", fill: white)[Autor / Canal]],
    ..referencias.map(r => (
      [#text(weight: "bold", fill: brand-accent)[#r.id]],
      [#r.categoria],
      [#r.titulo],
      [#r.autor_ou_canal]
    )).flatten()
  )
}
