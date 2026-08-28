#set page(
  paper: "a4",
  margin: (x: 1.5cm, y: 1.8cm),
  header: align(right)[
    #text(size: 8pt, fill: rgb("#64748b"))[Fábrica Universal AIDD · Macro-Ecossistema Soberano]
  ],
  footer: [
    #line(length: 100%, stroke: 0.5pt + rgb("#cbd5e1"))
    #grid(
      columns: (1fr, 1fr),
      text(size: 8pt, fill: rgb("#94a3b8"))[Confidencial & Soberano],
      align(right, text(size: 8pt, fill: rgb("#94a3b8"))[Página #context counter(page).display()])
    )
  ]
)

#set text(
  font: ("Segoe UI", "Arial", "Liberation Sans"),
  size: 8.5pt,
  fill: rgb("#0f172a"),
  lang: "pt"
)

#block(
  fill: rgb("#0f172a"),
  inset: 14pt,
  radius: 6pt,
  width: 100%,
  [
    #text(size: 7.5pt, weight: "bold", fill: rgb("#38bdf8"))[MACRO-ECOSSISTEMA SOBERANO · FLUXO 4 AIDD] \
    #v(3pt)
    #text(size: 15pt, weight: "bold", fill: white)[Macro-Ecossistema RD Station: Marketing, CRM & Conversas] \
    #v(2pt)
    #text(size: 8.5pt, fill: rgb("#cbd5e1"))[Arquitetura Aberta Integrada com SSO, Barramento de Eventos e Orquestração Multi-Módulo]
  ]
)

#v(8pt)

== 1. Demonstrativo Financeiro Consolidado (TCO Global)

#table(
  columns: (2.5fr, 2.5fr, 2.5fr, 2.5fr),
  fill: rgb("#f8fafc"),
  stroke: 0.5pt + rgb("#cbd5e1"),
  inset: 6pt,
  [*Custo SaaS Anual*], [*Custo VPS Soberana*], [*Economia Líquida*], [*Payback*],
  [R\$ 114.000/ano (RD Marketing Pro R\$ 42k + RD CRM 10 vendedores R\$ 36k + RD Conversas 10 atendentes R\$ 36k)], [R\$ 4.200/ano (VPS 8 vCPU / 16 GB RAM a R\$ 350/mês)], [*R\$ 109.800/ano (Economia Líquida de 96.3%)*], [Payback positivo em apenas 14 dias de operação unificada.]
)

#v(8pt)

== 2. Análise Detalhada por Grupos de Negócio


=== Grupo 1: Marketing, Nutrição & Landing Pages
#text(size: 8.5pt, fill: rgb("#0284c7"), weight: "bold")[Alvo SaaS: RD Station Marketing (Planos Pro / Enterprise)] \
#text(size: 8.5pt, fill: rgb("#00875A"), weight: "bold")[Economia do Grupo: R\$ 42.000/ano] \
#text(size: 8.5pt, style: "italic", fill: rgb("#475569"))[Frente responsável pela atração de tráfego, captura e enriquecimento de contatos, criação autônoma de landing pages dinâmicas, disparos de e-mail marketing em massa e automação de fluxos com pontuação de leads (lead scoring).] \
#v(4pt)

#table(
  columns: (0.6fr, 1.8fr, 2.8fr, 1.8fr, 1.0fr),
  fill: (x, y) => if y == 0 { rgb("#f1f5f9") } else { none },
  stroke: 0.5pt + rgb("#e2e8f0"),
  inset: 4.5pt,
  [*Nº*], [*Ferramenta*], [*Substitui Diretamente*], [*Economia*], [*Licença*],
  [1], [*Mautic*], [RD Station Marketing (Módulo de Automação de Fluxos & Lead Scoring)], [R\$ 42.000/ano (Base de 50.000 leads)], [`GPL-3.0`],
  [2], [*Listmonk*], [RD Station Marketing (Módulo de Disparos de E-mail & Broadcast)], [R\$ 18.000/ano], [`AGPL-3.0`],
  [3], [*Directus*], [RD Station Marketing (Construtor de Landing Pages & Formulários Estáticos)], [R\$ 12.000/ano], [`GPL-3.0`],
)
#v(8pt)

=== Grupo 2: Pipeline Comercial, CRM & Contratos
#text(size: 8.5pt, fill: rgb("#0284c7"), weight: "bold")[Alvo SaaS: RD Station CRM (Plano Avançado para Equipes de Vendas)] \
#text(size: 8.5pt, fill: rgb("#00875A"), weight: "bold")[Economia do Grupo: R\$ 36.000/ano] \
#text(size: 8.5pt, style: "italic", fill: rgb("#475569"))[Frente responsável pela gestão visual de oportunidades comerciais em formato Kanban, distribuição de leads qualificados, histórico de contatos, agendamento de reuniões e assinatura de propostas.] \
#v(4pt)

#table(
  columns: (0.6fr, 1.8fr, 2.8fr, 1.8fr, 1.0fr),
  fill: (x, y) => if y == 0 { rgb("#f1f5f9") } else { none },
  stroke: 0.5pt + rgb("#e2e8f0"),
  inset: 4.5pt,
  [*Nº*], [*Ferramenta*], [*Substitui Diretamente*], [*Economia*], [*Licença*],
  [1], [*Twenty*], [RD Station CRM (Módulo de Pipeline Kanban, Oportunidades & Tarefas)], [R\$ 24.000/ano (Equipe de 10 vendedores)], [`AGPL-3.0`],
  [2], [*Cal.com*], [RD Station CRM (Agendamentos) / Calendly Integrado], [R\$ 12.000/ano], [`AGPL-3.0`],
  [3], [*Documenso*], [Clicksign / DocuSign / Módulo de Propostas Comerciais], [R\$ 18.000/ano], [`AGPL-3.0`],
  [4], [*EspoCRM*], [RD Station CRM (Módulos Corporativos Avançados & Múltiplos Pipelines)], [R\$ 18.000/ano], [`GPL-3.0`],
)
#v(8pt)

=== Grupo 3: Atendimento Omnichannel & WhatsApp
#text(size: 8.5pt, fill: rgb("#0284c7"), weight: "bold")[Alvo SaaS: RD Station Conversas (Antigo Tallos / Módulos de Mensageria)] \
#text(size: 8.5pt, fill: rgb("#00875A"), weight: "bold")[Economia do Grupo: R\$ 36.000/ano] \
#text(size: 8.5pt, style: "italic", fill: rgb("#475569"))[Frente responsável pela caixa de entrada unificada multicanal, conexão estável com múltiplos números de WhatsApp sem taxas por mensagem e triagem inteligente com chatbots.] \
#v(4pt)

#table(
  columns: (0.6fr, 1.8fr, 2.8fr, 1.8fr, 1.0fr),
  fill: (x, y) => if y == 0 { rgb("#f1f5f9") } else { none },
  stroke: 0.5pt + rgb("#e2e8f0"),
  inset: 4.5pt,
  [*Nº*], [*Ferramenta*], [*Substitui Diretamente*], [*Economia*], [*Licença*],
  [1], [*Chatwoot*], [RD Station Conversas (Painel de Atendimento Multiatendente)], [R\$ 36.000/ano (10 operadores)], [`MIT`],
  [2], [*Evolution API*], [RD Station Conversas (Conectores Proprietários Z-API / Gupshup)], [R\$ 18.000/ano], [`Apache-2.0`],
  [3], [*Typebot*], [RD Station Conversas (Chatbots de Triagem) / Landbot], [R\$ 14.400/ano], [`AGPL-3.0`],
  [4], [*WAHA*], [RD Station Notificações WhatsApp / Twilio Messaging], [R\$ 12.000/ano], [`Apache-2.0`],
)
#v(8pt)


== 3. Camada de Cola, SSO & Orquestração

- *Autenticação Unificada (SSO):* Keycloak / Authentik (OpenID Connect / SAML) unificando o login dos colaboradores no Twenty CRM, Chatwoot, Directus e Mautic.
- *Barramento de Eventos:* n8n Community Edition atuando como orquestrador central de eventos assíncronos (Lead capturado no Typebot -> pontuado no Mautic -> oportunidade criada no Twenty -> alerta enviado no WhatsApp).
- *Reverse Proxy & TLS:* Traefik Proxy v3 com terminação TLS automática via Let's Encrypt e roteamento por subdomínios corporativos (mkt.empresa.com.br, crm.empresa.com.br, chat.empresa.com.br).

#v(8pt)

== 4. Deploy All-in-One & Dimensionamento

- *Hardware Recomendado:* 8 vCPU / 16 GB RAM / 120 GB NVMe SSD
