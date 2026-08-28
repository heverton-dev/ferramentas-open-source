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
  size: 9pt,
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
  [R\$ 114.000/ano (RD Marketing Pro R\$ 42k + RD CRM 15 usuários R\$ 36k + RD Conversas 10 atendentes R\$ 36k)], [R\$ 4.200/ano (VPS 8 vCPU / 16 GB RAM a R\$ 350/mês)], [*R\$ 109.800/ano (Economia de 96.3%)*], [Payback positivo em apenas 14 dias de operação unificada.]
)

#v(8pt)

== 2. Pilares Funcionais do Ecossistema


=== Pilar 1: Marketing, Nutrição & Landing Pages
#text(size: 8.5pt, fill: rgb("#0284c7"), weight: "bold")[Alvo SaaS: RD Station Marketing (Pro/Enterprise)] \
#text(size: 8.5pt, style: "italic", fill: rgb("#475569"))[Responsável por captura de leads, criação de landing pages dinâmicas, disparos de e-mail marketing em alta escala, automação de fluxos de nutrição e cálculo de lead scoring.] \
#v(4pt)

#table(
  columns: (0.8fr, 2.5fr, 3.5fr, 1.5fr),
  fill: (x, y) => if y == 0 { rgb("#f1f5f9") } else { none },
  stroke: 0.5pt + rgb("#e2e8f0"),
  inset: 5pt,
  [*Nº*], [*Ferramenta*], [*Papel no Pilar*], [*Licença*],
  [1], [*Mautic*], [Motor central de automação de marketing, segmentação dinâmica e pontuação de leads.], [`GPL-3.0`],
  [2], [*Listmonk*], [Entrega de e-mails em massa e newsletters com custo quase nulo via Amazon SES.], [`AGPL-3.0`],
  [3], [*Directus*], [Gestão autônoma de conteúdo das landing pages e portais corporativos sem depender de desenvolvedores.], [`GPL-3.0`],
)
#v(8pt)

=== Pilar 2: Pipeline de Vendas, CRM & Fechamento
#text(size: 8.5pt, fill: rgb("#0284c7"), weight: "bold")[Alvo SaaS: RD Station CRM (Avançado)] \
#text(size: 8.5pt, style: "italic", fill: rgb("#475569"))[Responsável pela gestão de oportunidades comerciais em formato Kanban, distribuição de leads para vendedores, agendamento de reuniões e assinatura digital de contratos.] \
#v(4pt)

#table(
  columns: (0.8fr, 2.5fr, 3.5fr, 1.5fr),
  fill: (x, y) => if y == 0 { rgb("#f1f5f9") } else { none },
  stroke: 0.5pt + rgb("#e2e8f0"),
  inset: 5pt,
  [*Nº*], [*Ferramenta*], [*Papel no Pilar*], [*Licença*],
  [1], [*Twenty*], [Interface principal dos vendedores para acompanhamento de negócios, tarefas e histórico de contatos.], [`AGPL-3.0`],
  [2], [*Cal.com*], [Elimina a fricção na marcação de reuniões de qualificação e fechamento com clientes.], [`AGPL-3.0`],
  [3], [*Documenso*], [Formalização jurídica de propostas comerciais e contratos sem custo por documento.], [`AGPL-3.0`],
  [4], [*EspoCRM*], [Gerencia contas complexas B2B, hierarquia de permissões e regras avançadas de comissionamento.], [`GPL-3.0`],
)
#v(8pt)

=== Pilar 3: Atendimento Omnicanal, WhatsApp & Chatbots
#text(size: 8.5pt, fill: rgb("#0284c7"), weight: "bold")[Alvo SaaS: RD Station Conversas (Tallos / Z-API)] \
#text(size: 8.5pt, style: "italic", fill: rgb("#475569"))[Responsável pela caixa de entrada unificada de atendimento ao cliente, conexão estável com múltiplos números de WhatsApp e triagem automatizada via chatbots interativos.] \
#v(4pt)

#table(
  columns: (0.8fr, 2.5fr, 3.5fr, 1.5fr),
  fill: (x, y) => if y == 0 { rgb("#f1f5f9") } else { none },
  stroke: 0.5pt + rgb("#e2e8f0"),
  inset: 5pt,
  [*Nº*], [*Ferramenta*], [*Papel no Pilar*], [*Licença*],
  [1], [*Chatwoot*], [Inbox unificada para múltiplos atendentes humanos responderem WhatsApp, Webchat e Instagram.], [`MIT`],
  [2], [*Evolution API*], [Conecta os números de WhatsApp corporativos e integra diretamente com o Chatwoot e n8n.], [`Apache-2.0`],
  [3], [*Typebot*], [Realiza o primeiro atendimento, coleta dados do lead e transfere para a fila certa no Chatwoot.], [`AGPL-3.0`],
  [4], [*WAHA*], [Redundância de conexão WhatsApp para disparos de alertas transacionais críticos.], [`Apache-2.0`],
)
#v(8pt)


== 3. Camada de Cola, SSO & Orquestração

- *Autenticação Unificada (SSO):* Keycloak / Authentik (OpenID Connect / SAML) unificando o login dos colaboradores no Twenty CRM, Chatwoot, Directus e Mautic.
- *Barramento de Eventos:* n8n Community Edition atuando como orquestrador central de eventos assíncronos (Lead capturado no Typebot -> pontuado no Mautic -> oportunidade criada no Twenty -> alerta enviado no WhatsApp).
- *Reverse Proxy & TLS:* Traefik Proxy v3 com terminação TLS automática via Let's Encrypt e roteamento por subdomínios corporativos (mkt.empresa.com.br, crm.empresa.com.br, chat.empresa.com.br).

#v(8pt)

== 4. Deploy All-in-One & Dimensionamento

- *Hardware Recomendado:* 8 vCPU / 16 GB RAM / 120 GB NVMe SSD
