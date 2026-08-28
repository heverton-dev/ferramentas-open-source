#set page(paper: "a4", flipped: true, margin: (x: 1.2cm, top: 1.2cm, bottom: 1.2cm))
#set text(font: "Liberation Sans", size: 9pt, lang: "pt")

#text(size: 8pt, fill: rgb("#64748b"), weight: "bold")[FÁBRICA UNIVERSAL AIDD · DOSSIÊ DE MACRO-ECOSSISTEMA SOBERANO (PADRÃO DIAMANTE R5-E)]
#v(2pt)
#text(size: 16pt, weight: "bold", fill: rgb("#0f172a"))[Macro-Ecossistema RD Station: Marketing, CRM & Conversas]
#v(-2pt)
#text(size: 10pt, fill: rgb("#00875A"), weight: "bold")[Arquitetura Aberta Integrada com Quinteto Soberano por Grupo, SSO, Barramento de Eventos e MCPs]
#v(6pt)

#grid(
  columns: (1fr, 1fr, 1.2fr, 1fr),
  gutter: 8pt,
  rect(fill: rgb("#f8fafc"), stroke: 0.5pt + rgb("#e2e8f0"), inset: 6pt)[
    #text(size: 7.5pt, fill: rgb("#64748b"))[CUSTO SAAS ANUAL] \
    #text(size: 11pt, weight: "bold", fill: rgb("#dc2626"))[R\$ 114.000/ano (RD Marketing Pro R\$ 42k + RD CRM 10 vendedores R\$ 36k + RD Conversas 10 atendentes R\$ 36k)]
  ],
  rect(fill: rgb("#f8fafc"), stroke: 0.5pt + rgb("#e2e8f0"), inset: 6pt)[
    #text(size: 7.5pt, fill: rgb("#64748b"))[CUSTO VPS SOBERANA] \
    #text(size: 11pt, weight: "bold", fill: rgb("#0f172a"))[R\$ 4.200/ano (VPS 8 vCPU / 16 GB RAM a R\$ 350/mês)]
  ],
  rect(fill: rgb("#f0fdf4"), stroke: 0.5pt + rgb("#bbf7d0"), inset: 6pt)[
    #text(size: 7.5pt, fill: rgb("#166534"))[ECONOMIA LÍQUIDA ANUAL] \
    #text(size: 11pt, weight: "bold", fill: rgb("#16a34a"))[R\$ 109.800/ano (Economia Líquida de 96.3%)]
  ],
  rect(fill: rgb("#f0fdf4"), stroke: 0.5pt + rgb("#bbf7d0"), inset: 6pt)[
    #text(size: 7.5pt, fill: rgb("#166534"))[PAYBACK ESTIMADO] \
    #text(size: 11pt, weight: "bold", fill: rgb("#16a34a"))[Payback positivo em apenas 14 dias de operação unificada.]
  ]
)

#v(8pt)
== Pilares Estratégicos & Quinteto Soberano por Grupo

=== Grupo 1: Marketing, Nutrição & Landing Pages
#text(size: 8.5pt, fill: rgb("#0284c7"), weight: "bold")[Alvo SaaS: RD Station Marketing (Planos Pro / Enterprise)] \
#text(size: 8.5pt, fill: rgb("#00875A"), weight: "bold")[Economia do Grupo: R\$ 42.000/ano] \
#text(size: 8.5pt, style: "italic", fill: rgb("#475569"))[Frente responsável pela atração de tráfego, captura e enriquecimento de contatos, criação autônoma de landing pages dinâmicas, disparos de e-mail marketing em massa e automação de fluxos com pontuação de leads (lead scoring).] \
#v(4pt)

#table(
  columns: (0.5fr, 1.4fr, 1.8fr, 2.5fr, 1.4fr, 0.9fr),
  fill: (x, y) => if y == 0 { rgb("#f1f5f9") } else { none },
  stroke: 0.5pt + rgb("#e2e8f0"),
  inset: 4pt,
  [*Nº*], [*Classificação*], [*Ferramenta*], [*Substitui Diretamente*], [*Economia*], [*Licença*],
  [1], [Completa], [*Mautic*], [RD Station Marketing (Módulo de Automação de Fluxos & Lead Scoring)], [R\$ 42.000/ano (Base de 50.000 leads)], [`GPL-3.0`],
  [2], [Leve], [*Listmonk*], [RD Station Marketing (Módulo de Disparos de E-mail & Broadcast)], [R\$ 18.000/ano], [`AGPL-3.0`],
  [3], [Robusta], [*Directus*], [RD Station Marketing (Construtor de Landing Pages & Formulários Estáticos)], [R\$ 12.000/ano], [`GPL-3.0`],
  [4], [Moderna], [*Novu*], [RD Station Notificações / OneSignal / Courier], [R\$ 14.400/ano], [`Apache-2.0`],
  [5], [Simples], [*Plunk*], [RD Station Marketing (Plano Light / Automações Básicas)], [R\$ 9.600/ano], [`MIT`],
)
#v(8pt)

=== Grupo 2: Pipeline Comercial, CRM & Contratos
#text(size: 8.5pt, fill: rgb("#0284c7"), weight: "bold")[Alvo SaaS: RD Station CRM (Plano Avançado para Equipes de Vendas)] \
#text(size: 8.5pt, fill: rgb("#00875A"), weight: "bold")[Economia do Grupo: R\$ 36.000/ano] \
#text(size: 8.5pt, style: "italic", fill: rgb("#475569"))[Frente responsável pela gestão visual de oportunidades comerciais em formato Kanban, distribuição de leads qualificados, histórico de contatos, agendamento de reuniões e assinatura de propostas.] \
#v(4pt)

#table(
  columns: (0.5fr, 1.4fr, 1.8fr, 2.5fr, 1.4fr, 0.9fr),
  fill: (x, y) => if y == 0 { rgb("#f1f5f9") } else { none },
  stroke: 0.5pt + rgb("#e2e8f0"),
  inset: 4pt,
  [*Nº*], [*Classificação*], [*Ferramenta*], [*Substitui Diretamente*], [*Economia*], [*Licença*],
  [1], [Moderna], [*Twenty*], [RD Station CRM (Módulo de Pipeline Kanban, Oportunidades & Tarefas)], [R\$ 24.000/ano (Equipe de 10 vendedores)], [`AGPL-3.0`],
  [2], [Robusta], [*EspoCRM*], [RD Station CRM (Módulos Corporativos Avançados & Múltiplos Pipelines)], [R\$ 18.000/ano], [`GPL-3.0`],
  [3], [Completa], [*SuiteCRM*], [Salesforce Sales Cloud / SugarCRM Enterprise], [R\$ 36.000/ano], [`AGPL-3.0`],
  [4], [Leve], [*Documenso*], [Clicksign / DocuSign / Módulo de Propostas Comerciais], [R\$ 18.000/ano], [`AGPL-3.0`],
  [5], [Simples], [*Cal.com*], [RD Station CRM (Agendamentos) / Calendly Integrado], [R\$ 12.000/ano], [`AGPL-3.0`],
)
#v(8pt)

=== Grupo 3: Atendimento Omnichannel & WhatsApp
#text(size: 8.5pt, fill: rgb("#0284c7"), weight: "bold")[Alvo SaaS: RD Station Conversas (Antigo Tallos / Módulos de Mensageria)] \
#text(size: 8.5pt, fill: rgb("#00875A"), weight: "bold")[Economia do Grupo: R\$ 36.000/ano] \
#text(size: 8.5pt, style: "italic", fill: rgb("#475569"))[Frente responsável pela caixa de entrada unificada multicanal, conexão estável com múltiplos números de WhatsApp sem taxas por mensagem e triagem inteligente com chatbots.] \
#v(4pt)

#table(
  columns: (0.5fr, 1.4fr, 1.8fr, 2.5fr, 1.4fr, 0.9fr),
  fill: (x, y) => if y == 0 { rgb("#f1f5f9") } else { none },
  stroke: 0.5pt + rgb("#e2e8f0"),
  inset: 4pt,
  [*Nº*], [*Classificação*], [*Ferramenta*], [*Substitui Diretamente*], [*Economia*], [*Licença*],
  [1], [Completa], [*Chatwoot*], [RD Station Conversas (Painel de Atendimento Multiatendente)], [R\$ 36.000/ano (10 operadores)], [`MIT`],
  [2], [Robusta], [*Evolution API*], [RD Station Conversas (Conectores Proprietários Z-API / Gupshup)], [R\$ 18.000/ano], [`Apache-2.0`],
  [3], [Moderna], [*Typebot*], [RD Station Conversas (Chatbots de Triagem) / Landbot], [R\$ 14.400/ano], [`AGPL-3.0`],
  [4], [Leve], [*WAHA*], [RD Station Notificações WhatsApp / Twilio Messaging], [R\$ 12.000/ano], [`Apache-2.0`],
  [5], [Simples], [*Papercups*], [Intercom / Crisp / Chat Básico do RD], [R\$ 10.800/ano], [`MIT`],
)
#v(8pt)


#v(8pt)
== Camada de Cola, SSO & Barramento de Eventos
- *Autenticação Única:* Keycloak / Authentik (OpenID Connect / SAML) unificando o login dos colaboradores no Twenty CRM, Chatwoot, Directus, Mautic e SuiteCRM.
- *Barramento:* n8n Community Edition atuando como orquestrador central de eventos assíncronos (Lead capturado no Typebot -> pontuado no Mautic -> oportunidade criada no Twenty -> alerta enviado no WhatsApp via Evolution).
- *Reverse Proxy:* Traefik Proxy v3 com terminação TLS automática via Let's Encrypt e roteamento por subdomínios corporativos (mkt.empresa.com.br, crm.empresa.com.br, chat.empresa.com.br, sso.empresa.com.br).

#v(8pt)
== Deploy All-in-One & Modularidade Operacional
- *Topologia:* A infraestrutura opera sobre uma rede bridge isolada do Docker (`ecosystem_net`). Apenas o reverse proxy Traefik expõe as portas públicas 80 (HTTP com redirect) e 443 (HTTPS TLS automático via ACME/Let's Encrypt). Todas as ferramentas (Mautic, Twenty, Chatwoot, Evolution, n8n, Keycloak e PostgreSQL) comunicam-se exclusivamente pela rede interna através de seus nomes DNS de serviço (ex: `http://chatwoot:3000`, `postgres:5432`), eliminando vetores de ataque externos e exposição de portas desnecessárias.
- *Princípio Modular:* A arquitetura opera sob o princípio de 'Tomadas e Aparelhos Independentes'. Nenhuma ferramenta fica grudada ou dependente da outra com código travado. Imagine uma régua de tomadas na sua sala: a sua TV (Twenty CRM) e a sua Caixa de Som (Chatwoot) funcionam perfeitamente mesmo se você desligar o Abajur (Mautic). Se você quiser trocar o abajur por uma luminária moderna, basta tirar da tomada e plugar a nova. Nada na sua sala quebra.
