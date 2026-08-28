#set page(
  paper: "a4",
  margin: (x: 2cm, y: 2.5cm),
  header: align(right)[#text(size: 8pt, fill: rgb("64748b"))[Auditoria de VPS · Arsenal Open Source]],
  footer: align(center)[#text(size: 8pt, fill: rgb("64748b"))[Arsenal Open Source · Fabrica Universal · Soberania Tecnologica]]
)
#set text(font: "Liberation Sans", size: 10pt, lang: "pt")
#set par(justify: true, leading: 0.7em)

#align(center)[
  #block(
    fill: rgb("0f172a"),
    inset: 2.5em,
    radius: 0.5em,
    width: 100%,
    [
      #text(size: 11pt, fill: rgb("38bdf8"), weight: "bold")[RELATORIO DE AUDITORIA & ENGENHARIA DE VPS]\n
      #v(0.5em)
      #text(size: 20pt, fill: rgb("ffffff"), weight: "bold")[Ecossistema DevOps & Engenharia de Dados (NocoDB + Supabase + n8n + Directus)]\n
      #v(0.5em)
      #text(size: 11pt, fill: rgb("94a3b8"))[Data: 28/08/2026 · Host: painel.vpsconexao.org]\n
      #v(0.5em)
      #text(size: 12pt, fill: rgb("34d399"), weight: "bold")[VEREDITO: TOTALMENTE VIAVEL (100% HOMOLOGADO) (SCORE 100/100)]
    ]
  )
]

#v(1.5em)
== 1. Diagnostico de Capacidade e Headroom

A VPS de producao possui *12 vCPUs* e *47.05 GB de memoria RAM*, com aproximadamente *43.99 GB de memoria livre*. A incorporacao do alvo demanda *4 vCPUs* e *6.0 GB de RAM*, preservando ampla margem de seguranca operacional.

#table(
  columns: (1.5fr, 1fr, 1fr, 1fr, 1fr),
  fill: (col, row) => if row == 0 { rgb("1e293b") } else { none },
  stroke: 0.5pt + rgb("cbd5e1"),
  align: (left, center, center, center, center),
  [#text(fill: white, weight: "bold")[Recurso]],
  [#text(fill: white, weight: "bold")[Total]],
  [#text(fill: white, weight: "bold")[Ocupado]],
  [#text(fill: white, weight: "bold")[Demanda]],
  [#text(fill: white, weight: "bold")[Status]],
  [Processamento], [12 vCPUs], [~1.5 vCPUs], [4 vCPUs], [APROVADO],
  [Memoria RAM], [47.05 GB], [~3.06 GB], [6.0 GB], [APROVADO],
  [Orquestracao], [Docker Swarm], [17 Cntrs], [Namespace], [APROVADO],
  [Ingress TLS], [Traefik], [Rede Overlay], [Let's Encrypt], [APROVADO]
)

#v(1.5em)
== 2. Garantia de Isolamento e Risco Zero

1. *Roteamento SNI Traefik:* Nenhuma porta de host e aberta no no fisico. O Traefik roteia via subdominios seguros.
2. *Volumes Dedicados:* Volumes persistentes utilizam prefixos exclusivos, sem tocar nos dados de Mautic, n8n ou Evolution.
3. *Rollback Instantaneo:* Remocao via comando `docker stack rm` em menos de 10 segundos.
