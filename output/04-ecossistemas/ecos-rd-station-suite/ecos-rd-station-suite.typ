#set page(
  paper: "a4",
  margin: (x: 1.8cm, top: 2.2cm, bottom: 2.2cm),
  header: align(center)[
    #set par(leading: 0.65em)
    #text(size: 8pt, fill: rgb("#64748b"), font: "Liberation Sans")[Fábrica Universal AIDD · Livro-Texto de Macro-Ecossistema Soberano (Padrão Diamante R5-E)]
  ],
  footer: [
    #set par(leading: 0.65em)
    #text(size: 8pt, fill: rgb("#64748b"), font: "Liberation Sans")[
      #grid(
        columns: (1fr, 1fr),
        [Suíte do Ecossistema Soberano · RD Station Suite (Marketing Pro + CRM Pro + Conversas Enterprise + Zapier)],
        align(right)[Fábrica Universal AIDD]
      )
    ]
  ]
)
#set text(font: "Liberation Sans", size: 9.5pt, lang: "pt")
#set par(justify: true, leading: 1.5em)

// DIAGRAMAÇÃO DE TÍTULOS E ESPAÇAMENTOS (HIERARQUIA H1-H6 SEM ESPAÇAMENTO ENTRE LINHAS)
#show heading: it => [
  #set par(leading: 0.45em)
  #it
]

#show heading.where(level: 1): it => block(
  above: 28pt,
  below: 14pt,
  [
    #set par(leading: 0.45em)
    #text(size: 18pt, weight: "bold", fill: rgb("#0f172a"), font: "Liberation Serif")[#it.body]
  ]
)

#show heading.where(level: 2): it => block(
  above: 22pt,
  below: 10pt,
  [
    #set par(leading: 0.45em)
    #text(size: 13.5pt, weight: "bold", fill: rgb("#0f172a"), font: "Liberation Sans")[#it.body]
  ]
)

#show heading.where(level: 3): it => block(
  above: 16pt,
  below: 8pt,
  [
    #set par(leading: 0.45em)
    #text(size: 11pt, weight: "bold", fill: rgb("#1e293b"), font: "Liberation Sans")[#it.body]
  ]
)

#show heading.where(level: 4): it => block(
  above: 14pt,
  below: 6pt,
  [
    #set par(leading: 0.45em)
    #text(size: 10pt, weight: "bold", fill: rgb("#334155"), font: "Liberation Sans")[#it.body]
  ]
)

#show heading.where(level: 5): it => block(
  above: 12pt,
  below: 4pt,
  [
    #set par(leading: 0.45em)
    #text(size: 9.5pt, weight: "bold", fill: rgb("#475569"), font: "Liberation Sans")[#it.body]
  ]
)

#show heading.where(level: 6): it => block(
  above: 10pt,
  below: 4pt,
  [
    #set par(leading: 0.45em)
    #text(size: 9pt, weight: "bold", fill: rgb("#64748b"), font: "Liberation Sans")[#it.body]
  ]
)

// CAPA EDITORIAL EXECUTIVA
#align(center + horizon)[
  #rect(stroke: 2pt + rgb("#0f172a"), inset: 24pt, radius: 4pt, width: 100%)[
    #text(size: 10pt, tracking: 0.2em, weight: "bold", fill: rgb("#00875A"))[FÁBRICA UNIVERSAL AIDD · TRATADO DE ENGENHARIA] \
    #v(12pt)
    #text(size: 24pt, weight: "bold", fill: rgb("#0f172a"), font: "Liberation Serif")[Macro-Ecossistema RD Station: Marketing, CRM & Conversas] \
    #v(6pt)
    #text(size: 12pt, fill: rgb("#334155"))[Arquitetura Aberta Integrada com Quinteto Soberano por Grupo, SSO, Barramento de Eventos e MCPs] \
    #v(16pt)
    #line(length: 60%, stroke: 1pt + rgb("#cbd5e1"))
    #v(16pt)
    #text(size: 10pt, fill: rgb("#475569"))[
      *Macro-Ecossistema Alvo:* RD Station Suite (Marketing Pro + CRM Pro + Conversas Enterprise + Zapier) \
      *Economia Anual Líquida:* #text(fill: rgb("#00875A"), weight: "bold")[R\$ 109.800/ano (Economia Líquida de 96.3%)] \
      *Padrão Normativo:* Diamante R5-E Tripartite \
      *Publicação:* 28/08/2026 · 1ª Edição Oficial
    ]
  ]
]

#pagebreak()

// SUMÁRIO AUTOMÁTICO
#outline(title: [Sumário Geral do Livro-Texto], indent: auto)

#v(16pt)
#line(length: 100%, stroke: 0.5pt + rgb("#e2e8f0"))
#v(16pt)

= Prefácio Executivo & Manifesto da Soberania
Dossiê completo de desmantelamento soberano para o Macro-Ecossistema RD Station (Marketing, CRM, Conversas/WhatsApp, Formulários e Automações). Cada frente de negócio é estruturada com seu próprio Quinteto Soberano (A Mais Robusta, Mais Completa, Mais Moderna, Mais Leve e Mais Simples), acompanhada de análise de TCO, guias práticos, aderência white-label e ecossistema agêntico de MCPs.

A migração de suítes de software proprietário fechado para ecossistemas open source auto-hospedados em VPS representa a maior alavanca de eficiência operacional da década. Este livro-texto reúne as especificações de engenharia para desmantelar a suíte *RD Station Suite (Marketing Pro + CRM Pro + Conversas Enterprise + Zapier)* com segurança jurídica, integridade de dados e autonomia digital irrestrita.

#pagebreak()

= Capítulo 1: Engenharia Financeira, TCO Global & Payback

#grid(
  columns: (1fr, 1fr),
  gutter: 10pt,
  rect(fill: rgb("#fef2f2"), stroke: 0.5pt + rgb("#fecaca"), inset: 10pt, radius: 2pt)[
    #text(size: 8pt, fill: rgb("#991b1b"), weight: "bold")[CUSTO SAAS ANUAL (RD Station Suite (Marketing Pro + CRM Pro + Conversas Enterprise + Zapier))] \
    #text(size: 14pt, weight: "bold", fill: rgb("#dc2626"))[R\$ 114.000/ano (RD Marketing Pro R\$ 42k + RD CRM 10 vendedores R\$ 36k + RD Conversas 10 atendentes R\$ 36k)]
  ],
  rect(fill: rgb("#f0fdf4"), stroke: 0.5pt + rgb("#bbf7d0"), inset: 10pt, radius: 2pt)[
    #text(size: 8pt, fill: rgb("#166534"), weight: "bold")[ECONOMIA LÍQUIDA ANUAL NO CAIXA] \
    #text(size: 14pt, weight: "bold", fill: rgb("#16a34a"))[R\$ 109.800/ano (Economia Líquida de 96.3%)]
  ]
)

#v(10pt)
- *Custo VPS Própria:* R\$ 4.200/ano (VPS 8 vCPU / 16 GB RAM a R\$ 350/mês) (Cluster Consolidado 8 vCPU / 16 GB RAM)
- *Retorno sobre Investimento (ROI / Payback):* Payback positivo em apenas 14 dias de operação unificada.

#v(10pt)
== Desmembramento Contábil por Frente de Negócio

#table(
  columns: (1.5fr, 1.8fr, 1.2fr, 1.2fr, 0.9fr),
  fill: (x, y) => if y == 0 { rgb("#f1f5f9") } else { none },
  stroke: 0.5pt + rgb("#cbd5e1"),
  inset: 5pt,
  [*Grupo*], [*SaaS Alvo*], [*Custo SaaS*], [*Economia*], [*Margem*],
  [Grupo 1: Marketing & Nutrição], [RD Station Marketing (Plano Pro - 50k leads)], [R\$ 42.000/ano], [R\$ 40.560/ano], [96.5%],
[Grupo 2: Pipeline Comercial & CRM], [RD Station CRM (Plano Avançado - 10 licenças)], [R\$ 36.000/ano], [R\$ 34.560/ano], [96.0%],
[Grupo 3: Atendimento & WhatsApp], [RD Station Conversas / Tallos (10 operadores)], [R\$ 36.000/ano], [R\$ 34.680/ano], [96.3%],

)

#pagebreak()

= Capítulo 2: Matriz Estratégica do Quinteto Soberano

#table(
  columns: (0.5fr, 1.3fr, 1.3fr, 1.8fr, 2.2fr, 1.3fr),
  fill: (x, y) => if y == 0 { rgb("#f1f5f9") } else { none },
  stroke: 0.5pt + rgb("#cbd5e1"),
  inset: 4pt,
  [*Nº*], [*Grupo*], [*Persona*], [*Ferramenta*], [*Substitui*], [*Economia*],
  [1], [Grupo 1], [Completa], [*Mautic*], [RD Station Marketing (Módulo de Automação de Fluxos & Lead Scoring)], [R\$ 42.000/ano (Base de 50.000 leads)],
[2], [Grupo 1], [Leve], [*Listmonk*], [RD Station Marketing (Módulo de Disparos de E-mail & Broadcast)], [R\$ 18.000/ano],
[3], [Grupo 1], [Robusta], [*Directus*], [RD Station Marketing (Construtor de Landing Pages & Formulários Estáticos)], [R\$ 12.000/ano],
[4], [Grupo 1], [Moderna], [*Novu*], [RD Station Notificações / OneSignal / Courier], [R\$ 14.400/ano],
[5], [Grupo 1], [Simples], [*Plunk*], [RD Station Marketing (Plano Light / Automações Básicas)], [R\$ 9.600/ano],
[6], [Grupo 2], [Moderna], [*Twenty*], [RD Station CRM (Módulo de Pipeline Kanban, Oportunidades & Tarefas)], [R\$ 24.000/ano (Equipe de 10 vendedores)],
[7], [Grupo 2], [Robusta], [*EspoCRM*], [RD Station CRM (Módulos Corporativos Avançados & Múltiplos Pipelines)], [R\$ 18.000/ano],
[8], [Grupo 2], [Completa], [*SuiteCRM*], [Salesforce Sales Cloud / SugarCRM Enterprise], [R\$ 36.000/ano],
[9], [Grupo 2], [Leve], [*Documenso*], [Clicksign / DocuSign / Módulo de Propostas Comerciais], [R\$ 18.000/ano],
[10], [Grupo 2], [Simples], [*Cal.com*], [RD Station CRM (Agendamentos) / Calendly Integrado], [R\$ 12.000/ano],
[11], [Grupo 3], [Completa], [*Chatwoot*], [RD Station Conversas (Painel de Atendimento Multiatendente)], [R\$ 36.000/ano (10 operadores)],
[12], [Grupo 3], [Robusta], [*Evolution API*], [RD Station Conversas (Conectores Proprietários Z-API / Gupshup)], [R\$ 18.000/ano],
[13], [Grupo 3], [Moderna], [*Typebot*], [RD Station Conversas (Chatbots de Triagem) / Landbot], [R\$ 14.400/ano],
[14], [Grupo 3], [Leve], [*WAHA*], [RD Station Notificações WhatsApp / Twilio Messaging], [R\$ 12.000/ano],
[15], [Grupo 3], [Simples], [*Papercups*], [Intercom / Crisp / Chat Básico do RD], [R\$ 10.800/ano],

)


#pagebreak()
= Capítulo 3: Pilar 01 · Grupo 1: Marketing, Nutrição & Landing Pages

#text(size: 9pt, fill: rgb("#0284c7"), weight: "bold")[Alvo SaaS Substituído: RD Station Marketing (Planos Pro / Enterprise)] \
#text(size: 9pt, fill: rgb("#00875A"), weight: "bold")[Subtotal de Economia do Grupo: R\$ 42.000/ano] \
#text(size: 9pt, style: "italic", fill: rgb("#475569"))[Frente responsável pela atração de tráfego, captura e enriquecimento de contatos, criação autônoma de landing pages dinâmicas, disparos de e-mail marketing em massa e automação de fluxos com pontuação de leads (lead scoring).]

#v(8pt)

== 01. Mautic · Automação de Marketing & Jornadas de Nutrição (Persona: Completa)

#rect(fill: rgb("#f8fafc"), stroke: 0.5pt + rgb("#cbd5e1"), inset: 8pt, radius: 2pt, width: 100%)[
  #grid(
    columns: (1fr, 1fr, 1fr),
    gutter: 6pt,
    [*Substitui:* RD Station Marketing (Módulo de Automação de Fluxos & Lead Scoring)],
    [*Economia:* #text(fill: rgb("#00875A"), weight: "bold")[R\$ 42.000/ano (Base de 50.000 leads)]],
    [*Licença:* `GPL-3.0`]
  )
]

*1. O Que Faz & Como Funciona:* \
Gerencia campanhas multicanal, pontua leads por interesse e aciona gatilhos de nutrição automática. Backend em PHP/Symfony com orquestrador visual de jornadas em árvore e integração de rastreamento no site.

```bash
docker run -d -p 8080:80 --name mautic mautic/mautic:latest
```

*2. Racional da Escolha & Veredito Técnico:* \
Única plataforma open source com construtor visual de jornadas em árvore equivalente ao RD Pro, com rastreamento avançado de comportamento web (lead tracking) e ausência de cobrança por volume de contatos na base. \
#text(style: "italic", fill: rgb("#334155"))[*Veredito:* O Mautic é a única alternativa aberta com maturidade funcional para substituir integralmente réguas de nutrição e pontuação de leads de grandes empresas sem limites de contatos.]

*3. Requisitos de Infraestrutura & White-Label:* \
- RAM Mínima: `4 GB RAM` | CPU: `1 vCPU` | Docker: `oficial`
- Customização UI: Permite substituir logo, favicon e aplicar paleta institucional via temas Twig customizados e CSS corporativo. (Esforço: Baixo)

#v(10pt)

== 02. Listmonk · Disparador de E-mails & Newsletters de Alta Performance (Persona: Leve)

#rect(fill: rgb("#f8fafc"), stroke: 0.5pt + rgb("#cbd5e1"), inset: 8pt, radius: 2pt, width: 100%)[
  #grid(
    columns: (1fr, 1fr, 1fr),
    gutter: 6pt,
    [*Substitui:* RD Station Marketing (Módulo de Disparos de E-mail & Broadcast)],
    [*Economia:* #text(fill: rgb("#00875A"), weight: "bold")[R\$ 18.000/ano]],
    [*Licença:* `AGPL-3.0`]
  )
]

*1. O Que Faz & Como Funciona:* \
Processa milhões de disparos de e-mail com segmentação SQL ultrarrápida. Binário Go estático de alto rendimento sobre PostgreSQL com suporte nativo a JSONB.

```bash
docker run -d -p 9000:9000 --name listmonk listmonk/listmonk:latest
```

*2. Racional da Escolha & Veredito Técnico:* \
Desenvolvido em Go puro, entrega milhões de e-mails consumindo menos de 50 MB de RAM, suportando segmentação relacional JSONB instantânea e eliminando custos punitivos por envio. \
#text(style: "italic", fill: rgb("#334155"))[*Veredito:* Imbatível para disparos volumosos e newsletters corporativas; entrega desempenho industrial com fraqueza de recursos.]

*3. Requisitos de Infraestrutura & White-Label:* \
- RAM Mínima: `1 GB RAM` | CPU: `1 vCPU` | Docker: `oficial`
- Customização UI: Interface limpa com suporte a upload de logo institucional e customização total dos formulários públicos de opt-in. (Esforço: Baixo)

#v(10pt)

== 03. Directus · Headless CMS para Landing Pages & Portais de Conteúdo (Persona: Robusta)

#rect(fill: rgb("#f8fafc"), stroke: 0.5pt + rgb("#cbd5e1"), inset: 8pt, radius: 2pt, width: 100%)[
  #grid(
    columns: (1fr, 1fr, 1fr),
    gutter: 6pt,
    [*Substitui:* RD Station Marketing (Construtor de Landing Pages & Formulários Estáticos)],
    [*Economia:* #text(fill: rgb("#00875A"), weight: "bold")[R\$ 12.000/ano]],
    [*Licença:* `GPL-3.0`]
  )
]

*1. O Que Faz & Como Funciona:* \
Fornece painel no-code para o time de marketing editar textos, depoimentos e formulários de landing pages. API REST/GraphQL instantânea sobre o PostgreSQL corporativo com autenticação OIDC.

```bash
docker run -d -p 8055:8055 --name directus directus/directus
```

*2. Racional da Escolha & Veredito Técnico:* \
Converte qualquer banco de dados relacional em uma interface no-code intuitiva para o time de marketing editar textos, banners e seções de conversão sem risco de quebra de layout. \
#text(style: "italic", fill: rgb("#334155"))[*Veredito:* A melhor infraestrutura de dados para times de marketing gerenciarem landing pages headless sem tocar em código.]

*3. Requisitos de Infraestrutura & White-Label:* \
- RAM Mínima: `2 GB RAM` | CPU: `1 vCPU` | Docker: `oficial`
- Customização UI: Suporte nativo a temas corporativos com injeção de logo, favicon e CSS global diretamente no painel de administração. (Esforço: Baixo)

#v(10pt)

== 04. Novu · Infraestrutura Moderna de Notificações Multicanal (Persona: Moderna)

#rect(fill: rgb("#f8fafc"), stroke: 0.5pt + rgb("#cbd5e1"), inset: 8pt, radius: 2pt, width: 100%)[
  #grid(
    columns: (1fr, 1fr, 1fr),
    gutter: 6pt,
    [*Substitui:* RD Station Notificações / OneSignal / Courier],
    [*Economia:* #text(fill: rgb("#00875A"), weight: "bold")[R\$ 14.400/ano]],
    [*Licença:* `Apache-2.0`]
  )
]

*1. O Que Faz & Como Funciona:* \
Gerencia fluxos de notificação transacionais com digest, delays e construtor visual de mensagens. NestJS, Redis e React com motor de regras para envio condicional de alertas multicanal.

```bash
npx novu init
```

*2. Racional da Escolha & Veredito Técnico:* \
Arquitetura reativa moderna em TypeScript/React com centro de preferências do usuário e fallback inteligente entre provedores de entrega. \
#text(style: "italic", fill: rgb("#334155"))[*Veredito:* Solução moderna essencial para empresas que precisam de régua de comunicação transacional unificada com fallback.]

*3. Requisitos de Infraestrutura & White-Label:* \
- RAM Mínima: `3 GB RAM` | CPU: `1 vCPU` | Docker: `oficial`
- Customização UI: Fornece componentes React headless (Inbox Notification Center) para inserção transparente no portal do cliente. (Esforço: Baixo)

#v(10pt)

== 05. Plunk · Automação de E-mails Minimalista & Rápida (Persona: Simples)

#rect(fill: rgb("#f8fafc"), stroke: 0.5pt + rgb("#cbd5e1"), inset: 8pt, radius: 2pt, width: 100%)[
  #grid(
    columns: (1fr, 1fr, 1fr),
    gutter: 6pt,
    [*Substitui:* RD Station Marketing (Plano Light / Automações Básicas)],
    [*Economia:* #text(fill: rgb("#00875A"), weight: "bold")[R\$ 9.600/ano]],
    [*Licença:* `MIT`]
  )
]

*1. O Que Faz & Como Funciona:* \
Envia e-mails transacionais e executa sequências simples baseadas em eventos de produto. Backend em Node.js com banco PostgreSQL e dashboard em React.

```bash
docker run -d -p 8080:8080 --name plunk useplunk/plunk:latest
```

*2. Racional da Escolha & Veredito Técnico:* \
Setup de 2 minutos com interface minimalista focada exclusivamente em disparos baseados em eventos com consumo ínfimo de recursos. \
#text(style: "italic", fill: rgb("#334155"))[*Veredito:* Perfeita para operações que não precisam da complexidade do Mautic e buscam simplicidade operacional imediata.]

*3. Requisitos de Infraestrutura & White-Label:* \
- RAM Mínima: `1 GB RAM` | CPU: `1 vCPU` | Docker: `oficial`
- Customização UI: Templates de e-mail em Markdown/HTML limpo totalmente adaptáveis à identidade institucional. (Esforço: Baixo)

#v(10pt)

#pagebreak()
= Capítulo 4: Pilar 02 · Grupo 2: Pipeline Comercial, CRM & Contratos

#text(size: 9pt, fill: rgb("#0284c7"), weight: "bold")[Alvo SaaS Substituído: RD Station CRM (Plano Avançado para Equipes de Vendas)] \
#text(size: 9pt, fill: rgb("#00875A"), weight: "bold")[Subtotal de Economia do Grupo: R\$ 36.000/ano] \
#text(size: 9pt, style: "italic", fill: rgb("#475569"))[Frente responsável pela gestão visual de oportunidades comerciais em formato Kanban, distribuição de leads qualificados, histórico de contatos, agendamento de reuniões e assinatura de propostas.]

#v(8pt)

== 01. Twenty · CRM Moderno Aberto & Gestão de Funil Comercial (Persona: Moderna)

#rect(fill: rgb("#f8fafc"), stroke: 0.5pt + rgb("#cbd5e1"), inset: 8pt, radius: 2pt, width: 100%)[
  #grid(
    columns: (1fr, 1fr, 1fr),
    gutter: 6pt,
    [*Substitui:* RD Station CRM (Módulo de Pipeline Kanban, Oportunidades & Tarefas)],
    [*Economia:* #text(fill: rgb("#00875A"), weight: "bold")[R\$ 24.000/ano (Equipe de 10 vendedores)]],
    [*Licença:* `AGPL-3.0`]
  )
]

*1. O Que Faz & Como Funciona:* \
Gerencia oportunidades em funil Kanban com sincronização de e-mail e notas em tempo real. Arquitetura reativa em TypeScript, React, NestJS e PostgreSQL com GraphQL nativo.

```bash
git clone https://github.com/twentyhq/twenty && cd twenty && docker compose up -d
```

*2. Racional da Escolha & Veredito Técnico:* \
Arquitetura reativa ultrarrápida em React/TypeScript com sincronização bidirecional de e-mails, campos customizados ilimitados e experiência de usuário moderna superior a CRMs legados. \
#text(style: "italic", fill: rgb("#334155"))[*Veredito:* O CRM open source mais moderno do mundo, com padrão de usabilidade equivalente ou superior a SaaS como Notion e HubSpot.]

*3. Requisitos de Infraestrutura & White-Label:* \
- RAM Mínima: `4 GB RAM` | CPU: `1 vCPU` | Docker: `oficial`
- Customização UI: Interface moderna com suporte a logotipo da empresa e modo escuro/claro nativo. (Esforço: Baixo)

#v(10pt)

== 02. EspoCRM · Motor de Regras Corporativas B2B & Workflows (Persona: Robusta)

#rect(fill: rgb("#f8fafc"), stroke: 0.5pt + rgb("#cbd5e1"), inset: 8pt, radius: 2pt, width: 100%)[
  #grid(
    columns: (1fr, 1fr, 1fr),
    gutter: 6pt,
    [*Substitui:* RD Station CRM (Módulos Corporativos Avançados & Múltiplos Pipelines)],
    [*Economia:* #text(fill: rgb("#00875A"), weight: "bold")[R\$ 18.000/ano]],
    [*Licença:* `GPL-3.0`]
  )
]

*1. O Que Faz & Como Funciona:* \
Permite modelar entidades customizadas e fluxos BPM para grandes operações comerciais. PHP/MySQL com construtor no-code de layouts e entidades relacionais.

```bash
docker run -d -p 8081:80 --name espocrm espocrm/espocrm
```

*2. Racional da Escolha & Veredito Técnico:* \
Mecanismo BPM no-code maduro para operações B2B que necessitam de regras de aprovação de desconto e múltiplos pipelines simultâneos por linha de produto. \
#text(style: "italic", fill: rgb("#334155"))[*Veredito:* A ferramenta mais sólida para empresas que necessitam de regras rígidas de segurança, permissões granulares e processos BPM.]

*3. Requisitos de Infraestrutura & White-Label:* \
- RAM Mínima: `2 GB RAM` | CPU: `1 vCPU` | Docker: `oficial`
- Customização UI: Totalmente personalizável pelo painel de administração (logo, cores, fontes e disposição de campos). (Esforço: Baixo)

#v(10pt)

== 03. SuiteCRM · Suíte Completa Enterprise para Grandes Operações de Vendas (Persona: Completa)

#rect(fill: rgb("#f8fafc"), stroke: 0.5pt + rgb("#cbd5e1"), inset: 8pt, radius: 2pt, width: 100%)[
  #grid(
    columns: (1fr, 1fr, 1fr),
    gutter: 6pt,
    [*Substitui:* Salesforce Sales Cloud / SugarCRM Enterprise],
    [*Economia:* #text(fill: rgb("#00875A"), weight: "bold")[R\$ 36.000/ano]],
    [*Licença:* `AGPL-3.0`]
  )
]

*1. O Que Faz & Como Funciona:* \
Centraliza todo o ciclo de vida do cliente: da prospecção ao faturamento e suporte técnico. PHP/Symfony com arquitetura robusta e banco relacional MySQL/Postgres.

```bash
docker run -d -p 8080:80 --name suitecrm suitecrm/suitecrm
```

*2. Racional da Escolha & Veredito Técnico:* \
A alternativa open source mais madura e completa do mercado corporativo, possuindo módulos nativos de catálogo de produtos, cálculo de impostos e emissão de propostas. \
#text(style: "italic", fill: rgb("#334155"))[*Veredito:* Para empresas que precisam de todas as funcionalidades de um ERP/CRM corporativo integrado em uma só plataforma.]

*3. Requisitos de Infraestrutura & White-Label:* \
- RAM Mínima: `4 GB RAM` | CPU: `1 vCPU` | Docker: `oficial`
- Customização UI: Tema SuiteP com suporte a upload de marca corporativa e alteração da paleta de cores primária e secundária. (Esforço: Baixo)

#v(10pt)

== 04. Documenso · Assinatura Eletrônica Soberana de Contratos e Propostas (Persona: Leve)

#rect(fill: rgb("#f8fafc"), stroke: 0.5pt + rgb("#cbd5e1"), inset: 8pt, radius: 2pt, width: 100%)[
  #grid(
    columns: (1fr, 1fr, 1fr),
    gutter: 6pt,
    [*Substitui:* Clicksign / DocuSign / Módulo de Propostas Comerciais],
    [*Economia:* #text(fill: rgb("#00875A"), weight: "bold")[R\$ 18.000/ano]],
    [*Licença:* `AGPL-3.0`]
  )
]

*1. O Que Faz & Como Funciona:* \
Gera links de assinatura digital com trilha de auditoria e carimbo do tempo criptográfico. Backend em TypeScript sobre PostgreSQL com geração de hashes SHA-256 dos documentos.

```bash
git clone https://github.com/documenso/documenso && cd documenso && docker compose up -d
```

*2. Racional da Escolha & Veredito Técnico:* \
Garante soberania jurídica dos documentos com trilha de auditoria criptográfica e registro de IPs, sem impor limites de contratos assinados por mês. \
#text(style: "italic", fill: rgb("#334155"))[*Veredito:* Elimina 100% das cobranças punitivas por documento assinado mantendo validade jurídica plena sob a MP 2.200-2/2001.]

*3. Requisitos de Infraestrutura & White-Label:* \
- RAM Mínima: `2 GB RAM` | CPU: `1 vCPU` | Docker: `oficial`
- Customização UI: Customização completa de emails de disparo, página de assinatura com logo da empresa e domínio próprio. (Esforço: Baixo)

#v(10pt)

== 05. Cal.com · Agendamento Automatizado de Demonstrações Comerciais (Persona: Simples)

#rect(fill: rgb("#f8fafc"), stroke: 0.5pt + rgb("#cbd5e1"), inset: 8pt, radius: 2pt, width: 100%)[
  #grid(
    columns: (1fr, 1fr, 1fr),
    gutter: 6pt,
    [*Substitui:* RD Station CRM (Agendamentos) / Calendly Integrado],
    [*Economia:* #text(fill: rgb("#00875A"), weight: "bold")[R\$ 12.000/ano]],
    [*Licença:* `AGPL-3.0`]
  )
]

*1. O Que Faz & Como Funciona:* \
Disponibiliza links de agendamento conectados à agenda dos vendedores com distribuição round-robin. Next.js e Prisma com sincronização com Google Calendar, Outlook e CalDAV.

```bash
git clone https://github.com/calcom/cal.com && cd cal.com && docker compose up -d
```

*2. Racional da Escolha & Veredito Técnico:* \
Suporte a distribuição round-robin entre múltiplos corretores/vendedores, integração direta com CalDAV, Google e Outlook e total personalização sob domínio próprio. \
#text(style: "italic", fill: rgb("#334155"))[*Veredito:* A solução definitiva de agendamento: fácil de usar, elegante para o cliente e com total privacidade corporativa.]

*3. Requisitos de Infraestrutura & White-Label:* \
- RAM Mínima: `2 GB RAM` | CPU: `1 vCPU` | Docker: `oficial`
- Customização UI: Páginas públicas de agendamento 100% white-label sob subdomínio institucional (ex: `agenda.empresa.com.br`). (Esforço: Baixo)

#v(10pt)

#pagebreak()
= Capítulo 5: Pilar 03 · Grupo 3: Atendimento Omnichannel & WhatsApp

#text(size: 9pt, fill: rgb("#0284c7"), weight: "bold")[Alvo SaaS Substituído: RD Station Conversas (Antigo Tallos / Módulos de Mensageria)] \
#text(size: 9pt, fill: rgb("#00875A"), weight: "bold")[Subtotal de Economia do Grupo: R\$ 36.000/ano] \
#text(size: 9pt, style: "italic", fill: rgb("#475569"))[Frente responsável pela caixa de entrada unificada multicanal, conexão estável com múltiplos números de WhatsApp sem taxas por mensagem e triagem inteligente com chatbots.]

#v(8pt)

== 01. Chatwoot · Central de Atendimento Omnicanal & Livechat Colaborativo (Persona: Completa)

#rect(fill: rgb("#f8fafc"), stroke: 0.5pt + rgb("#cbd5e1"), inset: 8pt, radius: 2pt, width: 100%)[
  #grid(
    columns: (1fr, 1fr, 1fr),
    gutter: 6pt,
    [*Substitui:* RD Station Conversas (Painel de Atendimento Multiatendente)],
    [*Economia:* #text(fill: rgb("#00875A"), weight: "bold")[R\$ 36.000/ano (10 operadores)]],
    [*Licença:* `MIT`]
  )
]

*1. O Que Faz & Como Funciona:* \
Centraliza conversas de clientes, distribui tickets e permite notas internas entre atendentes. Ruby on Rails com WebSockets e Vue.js para mensageria em tempo real.

```bash
git clone https://github.com/chatwoot/chatwoot && cd chatwoot && docker compose up -d
```

*2. Racional da Escolha & Veredito Técnico:* \
Software líder global em suporte omnicanal aberto, eliminando a cobrança por licença de atendente e fornecendo relatórios completos de CSAT e tempo de primeira resposta. \
#text(style: "italic", fill: rgb("#334155"))[*Veredito:* A plataforma mais completa do mercado aberto para atendimento humano, com relatórios gerenciais e SLAs avançados.]

*3. Requisitos de Infraestrutura & White-Label:* \
- RAM Mínima: `4 GB RAM` | CPU: `1 vCPU` | Docker: `oficial`
- Customização UI: Permite customizar logotipo, cores do widget de chat, nome da empresa e domínio institucional. (Esforço: Baixo)

#v(10pt)

== 02. Evolution API · Gateway Profissional de WhatsApp Baileys com Webhooks (Persona: Robusta)

#rect(fill: rgb("#f8fafc"), stroke: 0.5pt + rgb("#cbd5e1"), inset: 8pt, radius: 2pt, width: 100%)[
  #grid(
    columns: (1fr, 1fr, 1fr),
    gutter: 6pt,
    [*Substitui:* RD Station Conversas (Conectores Proprietários Z-API / Gupshup)],
    [*Economia:* #text(fill: rgb("#00875A"), weight: "bold")[R\$ 18.000/ano]],
    [*Licença:* `Apache-2.0`]
  )
]

*1. O Que Faz & Como Funciona:* \
Recebe e envia mensagens, mídias e áudios de WhatsApp via endpoints REST. Node.js e TypeScript com gerenciamento de sessões em Redis e Postgres.

```bash
docker run -d -p 8080:8080 --name evolution-api atendai/evolution-api:v2.1.0
```

*2. Racional da Escolha & Veredito Técnico:* \
API brasileira madura com suporte a múltiplas instâncias simultâneas, conversão automática de áudios em formato compatível e integração nativa de 1 clique com o Chatwoot. \
#text(style: "italic", fill: rgb("#334155"))[*Veredito:* O conector WhatsApp mais estável do ecossistema nacional, suportando milhares de mensagens diárias com alta resiliência.]

*3. Requisitos de Infraestrutura & White-Label:* \
- RAM Mínima: `2 GB RAM` | CPU: `1 vCPU` | Docker: `oficial`
- Customização UI: Opera como serviço de backend invisível sob domínio próprio da empresa (ex: `api-wa.empresa.com.br`). (Esforço: Baixo)

#v(10pt)

== 03. Typebot · Construtor Visual de Fluxos de Triagem & Qualificação (Persona: Moderna)

#rect(fill: rgb("#f8fafc"), stroke: 0.5pt + rgb("#cbd5e1"), inset: 8pt, radius: 2pt, width: 100%)[
  #grid(
    columns: (1fr, 1fr, 1fr),
    gutter: 6pt,
    [*Substitui:* RD Station Conversas (Chatbots de Triagem) / Landbot],
    [*Economia:* #text(fill: rgb("#00875A"), weight: "bold")[R\$ 14.400/ano]],
    [*Licença:* `AGPL-3.0`]
  )
]

*1. O Que Faz & Como Funciona:* \
Cria chatbots conversacionais interativos para qualificação de leads antes do humano. Editor visual drag-and-drop com blocos lógicos e integração nativa com IA e webhooks.

```bash
docker run -d -p 3001:3000 --name typebot baptistearno/typebot-builder:latest
```

*2. Racional da Escolha & Veredito Técnico:* \
Melhor construtor visual de fluxos conversacionais do mercado, com suporte a variáveis, ramificações condicionais e integração nativa com modelos de IA para atendimento automático. \
#text(style: "italic", fill: rgb("#334155"))[*Veredito:* A melhor experiência de criação de robôs conversacionais: fluida, moderna e sem necessidade de conhecimento em programação.]

*3. Requisitos de Infraestrutura & White-Label:* \
- RAM Mínima: `2 GB RAM` | CPU: `1 vCPU` | Docker: `oficial`
- Customização UI: Customização completa de fontes, avatares, cores de balões e plano de fundo no construtor visual. (Esforço: Baixo)

#v(10pt)

== 04. WAHA · Gateway Headless Secundário de Alta Disponibilidade (Persona: Leve)

#rect(fill: rgb("#f8fafc"), stroke: 0.5pt + rgb("#cbd5e1"), inset: 8pt, radius: 2pt, width: 100%)[
  #grid(
    columns: (1fr, 1fr, 1fr),
    gutter: 6pt,
    [*Substitui:* RD Station Notificações WhatsApp / Twilio Messaging],
    [*Economia:* #text(fill: rgb("#00875A"), weight: "bold")[R\$ 12.000/ano]],
    [*Licença:* `Apache-2.0`]
  )
]

*1. O Que Faz & Como Funciona:* \
Fornece API HTTP estável para automações de sistema sem interferir na fila de atendimento humano. Sessões Chromium headless em contêiner Docker isolado.

```bash
docker run -d -p 3000:3000 --name waha devlikeapro/waha
```

*2. Racional da Escolha & Veredito Técnico:* \
Solução headless ultra-estável em contêiner isolado para garantir que mensagens transacionais de sistema sejam enviadas mesmo em caso de sobrecarga da fila de atendimento. \
#text(style: "italic", fill: rgb("#334155"))[*Veredito:* Essencial para garantir que alertas de segurança e notificações financeiras não disputem fila com atendimentos humanos.]

*3. Requisitos de Infraestrutura & White-Label:* \
- RAM Mínima: `2 GB RAM` | CPU: `1 vCPU` | Docker: `oficial`
- Customização UI: Serviço totalmente desacoplado operando sob API interna. (Esforço: Baixo)

#v(10pt)

== 05. Papercups · Livechat & Suporte Direto sem Burocracia (Persona: Simples)

#rect(fill: rgb("#f8fafc"), stroke: 0.5pt + rgb("#cbd5e1"), inset: 8pt, radius: 2pt, width: 100%)[
  #grid(
    columns: (1fr, 1fr, 1fr),
    gutter: 6pt,
    [*Substitui:* Intercom / Crisp / Chat Básico do RD],
    [*Economia:* #text(fill: rgb("#00875A"), weight: "bold")[R\$ 10.800/ano]],
    [*Licença:* `MIT`]
  )
]

*1. O Que Faz & Como Funciona:* \
Fornece chat ao vivo para clientes conversarem com a equipe diretamente pelo navegador. Backend em Elixir/Phoenix (alta concorrência) com frontend em React.

```bash
docker run -d -p 4000:4000 --name papercups papercups/papercups:latest
```

*2. Racional da Escolha & Veredito Técnico:* \
Widget de chat leve em React com painel simples e sem dependências pesadas, ideal para suporte ágil. \
#text(style: "italic", fill: rgb("#334155"))[*Veredito:* A solução mais direta e leve para quem precisa apenas de um chat corporativo elegante no site sem excesso de menus.]

*3. Requisitos de Infraestrutura & White-Label:* \
- RAM Mínima: `1 GB RAM` | CPU: `1 vCPU` | Docker: `oficial`
- Customização UI: Total customização visual do widget flutuante (título, subtítulo, avatar e cor hexadecimal). (Esforço: Baixo)

#v(10pt)


#pagebreak()
= Capítulo 6: Camada de Cola, SSO Federado & Blueprints n8n

== Arquitetura de Interconexão sem Silos de Dados
- *Autenticação Única:* Keycloak / Authentik (OpenID Connect / SAML) unificando o login dos colaboradores no Twenty CRM, Chatwoot, Directus, Mautic e SuiteCRM.
- *Barramento Assíncrono:* n8n Community Edition atuando como orquestrador central de eventos assíncronos (Lead capturado no Typebot -> pontuado no Mautic -> oportunidade criada no Twenty -> alerta enviado no WhatsApp via Evolution).
- *Reverse Proxy & TLS:* Traefik Proxy v3 com terminação TLS automática via Let's Encrypt e roteamento por subdomínios corporativos (mkt.empresa.com.br, crm.empresa.com.br, chat.empresa.com.br, sso.empresa.com.br).

== Fluxo de Integração Operacional
1. Entrada de Leads: Lead preenche formulário no Typebot ou na Landing Page gerenciada pelo Directus;
2. Cadastramento & Nutrição: O webhook dispara no n8n que cadastra o contato no Mautic e inicia a régua de nutrição de e-mails via Listmonk;
3. Qualificação por Lead Scoring: Ao atingir 50 pontos no Mautic, um webhook notifica o n8n;
4. Criação de Oportunidade: O n8n cria a negociação no Twenty CRM e abre uma sala de contato prioritária no Chatwoot;
5. Agendamento & Fechamento: O vendedor envia link do Cal.com para demonstração e emite contrato pelo Documenso;
6. Sincronização Final: A assinatura do contrato atualiza o status de 'Ganho' no Twenty CRM e notifica o time no WhatsApp via Evolution API.

#pagebreak()
= Capítulo 7: Manual de Engenharia de Infraestrutura & Deploy All-in-One

- *Segurança de Rede:* A infraestrutura opera sobre uma rede bridge isolada do Docker (`ecosystem\_net`). Apenas o reverse proxy Traefik expõe as portas públicas 80 (HTTP com redirect) e 443 (HTTPS TLS automático via ACME/Let's Encrypt). Todas as ferramentas (Mautic, Twenty, Chatwoot, Evolution, n8n, Keycloak e PostgreSQL) comunicam-se exclusivamente pela rede interna através de seus nomes DNS de serviço (ex: `http://chatwoot:3000`, `postgres:5432`), eliminando vetores de ataque externos e exposição de portas desnecessárias.
- *Hardware Recomendado:* 8 vCPU / 16 GB RAM

== Manifesto docker-compose.yml de Produção
```yaml
version: '3.8'

networks:
  ecosystem_net:
    driver: bridge

services:
  # 1. Reverse Proxy & TLS Automático
  traefik:
    image: traefik:v3.0
    command:
      - '--providers.docker=true'
      - '--entrypoints.websecure.address=:443'
      - '--certificatesresolvers.myresolver.acme.tlschallenge=true'
    ports:
      - '80:80'
      - '443:443'
    volumes:
      - '/var/run/docker.sock:/var/run/docker.sock:ro'
      - './letsencrypt:/letsencrypt'
    networks:
      - ecosystem_net

  # 2. Provedor de Identidade & SSO
  keycloak:
    image: quay.io/keycloak/keycloak:latest
    command: start-dev
    environment:
      - KEYCLOAK_ADMIN=admin
      - KEYCLOAK_ADMIN_PASSWORD=SegredoForte2026
    labels:
      - 'traefik.enable=true'
      - 'traefik.http.routers.keycloak.rule=Host(`sso.suaempresa.com.br`)'
      - 'traefik.http.routers.keycloak.entrypoints=websecure'
      - 'traefik.http.routers.keycloak.tls.certresolver=myresolver'
    networks:
      - ecosystem_net

  # 3. Barramento de Eventos e Workflows
  n8n:
    image: n8nio/n8n:latest
    environment:
      - N8N_BASIC_AUTH_ACTIVE=true
      - N8N_HOST=n8n.suaempresa.com.br
    labels:
      - 'traefik.enable=true'
      - 'traefik.http.routers.n8n.rule=Host(`n8n.suaempresa.com.br`)'
      - 'traefik.http.routers.n8n.entrypoints=websecure'
      - 'traefik.http.routers.n8n.tls.certresolver=myresolver'
    networks:
      - ecosystem_net

  # 4. Automação de Marketing & Nutrição (RD Marketing)
  mautic:
    image: mautic/mautic:latest
    labels:
      - 'traefik.enable=true'
      - 'traefik.http.routers.mautic.rule=Host(`mkt.suaempresa.com.br`)'
      - 'traefik.http.routers.mautic.entrypoints=websecure'
      - 'traefik.http.routers.mautic.tls.certresolver=myresolver'
    networks:
      - ecosystem_net

  # 5. Pipeline Comercial & CRM (RD CRM)
  twenty:
    image: twentyhq/twenty:latest
    labels:
      - 'traefik.enable=true'
      - 'traefik.http.routers.twenty.rule=Host(`crm.suaempresa.com.br`)'
      - 'traefik.http.routers.twenty.entrypoints=websecure'
      - 'traefik.http.routers.twenty.tls.certresolver=myresolver'
    networks:
      - ecosystem_net

  # 6. Atendimento Omnichannel & Livechat (RD Conversas)
  chatwoot:
    image: chatwoot/chatwoot:latest
    labels:
      - 'traefik.enable=true'
      - 'traefik.http.routers.chatwoot.rule=Host(`chat.suaempresa.com.br`)'
      - 'traefik.http.routers.chatwoot.entrypoints=websecure'
      - 'traefik.http.routers.chatwoot.tls.certresolver=myresolver'
    networks:
      - ecosystem_net

  # 7. Gateway WhatsApp Baileys & Webhooks
  evolution-api:
    image: atendai/evolution-api:v2.1.0
    labels:
      - 'traefik.enable=true'
      - 'traefik.http.routers.evolution.rule=Host(`wa.suaempresa.com.br`)'
      - 'traefik.http.routers.evolution.entrypoints=websecure'
      - 'traefik.http.routers.evolution.tls.certresolver=myresolver'
    networks:
      - ecosystem_net

  # 8. Banco de Dados Relacional Consolidado
  postgres:
    image: postgres:16-alpine
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=SegredoPostgres2026
    volumes:
      - postgres_data:/var/lib/postgresql/data
    networks:
      - ecosystem_net

  # 9. Filas de Alta Velocidade & Sessões
  redis:
    image: redis:7-alpine
    volumes:
      - redis_data:/data
    networks:
      - ecosystem_net

volumes:
  postgres_data:
  redis_data:
```

#pagebreak()
= Capítulo 8: Protocolos de Modularidade & Hot-Swap (Princípio do Lego)

- *Filosofia Desacoplada:* A arquitetura opera sob o princípio de 'Tomadas e Aparelhos Independentes'. Nenhuma ferramenta fica grudada ou dependente da outra com código travado. Imagine uma régua de tomadas na sua sala: a sua TV (Twenty CRM) e a sua Caixa de Som (Chatwoot) funcionam perfeitamente mesmo se você desligar o Abajur (Mautic). Se você quiser trocar o abajur por uma luminária moderna, basta tirar da tomada e plugar a nova. Nada na sua sala quebra.

== Hot-Swap em Produção
1. Suba a Nova Ferramenta em Paralelo: Inicie a nova solução em um endereço temporário (ex: `novo-mkt.empresa.com.br`) mantendo a antiga funcionando;
2. Transfira a Conexão no n8n: No painel visual do n8n, mude o nó de disparo para apontar para a nova ferramenta;
3. Importe os Contatos: Faça o download da planilha de contatos da ferramenta antiga e importe na nova;
4. Mude o Endereço Oficial: Altere a rota para que `mkt.empresa.com.br` aponte para a nova ferramenta;
5. Desligue a Antiga com Segurança: Pare o serviço antigo digitando `docker compose stop <servico\_antigo>`. Seus vendedores e clientes nem notarão a troca!

#pagebreak()
= Capítulo 9: Roteiro Prático de Migração de Dados Históricos

== 1. Migração do RD Station Marketing ➔ Mautic
- *O que migrar:* Base total de contatos (Leads), campos personalizados, histórico de tags, segmentos e listas de descadastro (opt-out).
- *Cuidados:* Importe a lista de opt-out (unsubscribers) com o status 'Não perturbe' ativado para preservar a reputação do seu domínio de e-mail.

== 2. Migração do RD Station CRM ➔ Twenty CRM
- *O que migrar:* Empresas cadastradas, Pessoas de contato, Etapas do Funil de Vendas (Kanban), Negociações abertas/ganhas e Histórico de anotações comerciais.
- *Cuidados:* Mantenha a correspondência exata dos e-mails dos vendedores para que o histórico de notas e tarefas seja atribuído aos donos corretos.

== 3. Migração do RD Conversas / WhatsApp ➔ Chatwoot & Evolution API
- *O que migrar:* Números de WhatsApp conectados, mensagens pré-programadas (macros de resposta rápida), equipes de atendentes e departamentos.
- *Cuidados:* Não desconecte o chip do aparelho físico durante a virada para garantir a sincronização inicial de contatos.



#pagebreak()
= Capítulo 10: Governança Corporativa, Backup 3-2-1 & LGPD

- *Política 3-2-1:* A política de proteção de dados opera na regra de ouro 3-2-1: (3) cópias de dados em (2) tipos de mídias diferentes, com (1) cópia externa criptografada em nuvem fria (Wasabi / AWS S3 / Google Drive).

== Script de Backup Diário Criptografado
```bash
#!/bin/bash
# Script de Backup Automatizado Soberano (PostgreSQL + Volumes + Mídias)
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
BACKUP_DIR="/opt/backups/$TIMESTAMP"
mkdir -p $BACKUP_DIR

# 1. Dump consistente de todos os bancos de dados (Mautic, Twenty, Chatwoot, Keycloak, n8n)
docker exec postgres pg_dumpall -U postgres | gzip > $BACKUP_DIR/db_all_cluster.sql.gz

# 2. Compactação dos arquivos de mídia e anexos
tar -czf $BACKUP_DIR/media_storage.tar.gz -C /var/lib/docker/volumes postgres_data/_data

# 3. Criptografia AES-256 com senha segura
gpg --batch --yes --passphrase "SuaChaveMestreSegura2026" -c $BACKUP_DIR/db_all_cluster.sql.gz

# 4. Envio para Storage Seguro Externo (rclone / AWS S3)
rclone copy $BACKUP_DIR remote-s3:backups-empresa/$TIMESTAMP/

# 5. Limpeza de backups locais com mais de 7 dias
find /opt/backups/* -mtime +7 -exec rm -rf {} \;
echo "✅ Backup soberano concluído e sincronizado na nuvem fria!"
```

#pagebreak()
= Capítulo 11: Cronograma de Implantação em 30 Dias & Monitoramento

== Semana 1 (Dias 1 a 7) · Infraestrutura & Instalação do Cluster
- *Atividades:* Contratação da VPS, configuração de DNS wildcard (wildcard.empresa.com.br), execução do docker-compose.yml e ativação dos certificados SSL automáticos via Traefik.
- *Marco de Entrega:* Todos os painéis acessíveis online com cadeado verde (HTTPS).

== Semana 2 (Dias 8 a 14) · Migração de Dados & Conexão de Mensageria
- *Atividades:* Importação de leads do RD Marketing no Mautic, exportação do funil de vendas para o Twenty CRM e pareamento do WhatsApp na Evolution API e Chatwoot.
- *Marco de Entrega:* Base histórica 100% carregada e WhatsApp corporativo recebendo mensagens no Chatwoot.

== Semana 3 (Dias 15 a 21) · Importação dos Blueprints n8n & Treinamento das Equipes
- *Atividades:* Importação dos templates de workflow no n8n, realização de testes de passagem de bastão (Lead -> CRM -> WhatsApp) e workshop de capacitação dos vendedores e atendentes.
- *Marco de Entrega:* Equipes comerciais operando com agilidade e fluxos automatizados aprovados.

== Semana 4 (Dias 22 a 30) · Virada de Chave Definitiva & Descomissionamento SaaS
- *Atividades:* Redirecionamento de formulários do site oficial para a nova stack, ativação da régua de nutrição oficial e cancelamento das faturas recorrentes do RD Station Suite.
- *Marco de Entrega:* Autonomia digital plena e economia de R\$ 109.800/ano consolidada!


