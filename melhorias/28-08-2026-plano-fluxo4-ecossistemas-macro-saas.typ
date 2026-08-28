#set page(
  paper: "a4",
  margin: (x: 1.8cm, y: 2.0cm),
  header: align(right)[
    #text(size: 8pt, fill: rgb("#64748b"))[Fábrica Universal AIDD · Plano Diretor Fluxo 4]
  ],
  footer: [
    #line(length: 100%, stroke: 0.5pt + rgb("#cbd5e1"))
    #grid(
      columns: (1fr, 1fr),
      text(size: 8pt, fill: rgb("#94a3b8"))[28/08/2026 · Confidencial & Soberano],
      align(right, text(size: 8pt, fill: rgb("#94a3b8"))[Página #context counter(page).display()])
    )
  ]
)

#set text(
  font: ("Segoe UI", "Arial", "Liberation Sans"),
  size: 9.5pt,
  fill: rgb("#0f172a"),
  lang: "pt"
)

#block(
  fill: rgb("#0f172a"),
  inset: 16pt,
  radius: 8pt,
  width: 100%,
  [
    #text(size: 8pt, weight: "bold", fill: rgb("#38bdf8"))[GOVERNANÇA AIDD · NOVA ESTEIRA DE ENGENHARIA] \
    #v(4pt)
    #text(size: 16pt, weight: "bold", fill: white)[Plano Diretor · Fluxo 4: Ecossistemas & Macro-SaaS] \
    #v(2pt)
    #text(size: 9pt, fill: rgb("#cbd5e1"))[Desmantelamento Soberano de Suítes SaaS Multimodais com Camada de Cola e Orquestração Integrada]
  ]
)

#v(10pt)

== 1. Visão Geral & Necessidade Operacional

Diferente de um SaaS pontual (Fluxo 2) ou de uma camada tecnológica isolada (Fluxo 1), grandes organizações operam sob *Macro-Ecossistemas de Software* compostos por múltiplos pilares funcionais interdependentes.

No caso do *RD Station Suite*, o ecossistema é formado por 3 frentes centrais:
- *RD Station Marketing:* Automação de marketing, landing pages, nutrição de leads e disparos de e-mail;
- *RD Station CRM:* Pipeline de vendas comercial, gestão de oportunidades, follow-ups e contratos;
- *RD Station Conversas (WhatsApp/Omnichannel):* Atendimento multicanal centralizado, chatbots e mensageria.

O *Fluxo 4* resolve a substituição integrada de toda essa suíte, incluindo a *Camada de Cola* (Autenticação SSO, Barramento de Eventos via Webhooks, Reverse Proxy e Orquestração unificada).

#v(8pt)

== 2. Matriz de Componentes do Ecossistema RD Station

#table(
  columns: (1.5fr, 2.5fr, 2.5fr),
  fill: (x, y) => if y == 0 { rgb("#f1f5f9") } else { none },
  stroke: 0.5pt + rgb("#e2e8f0"),
  inset: 7pt,
  [*Pilar Funcional*], [*Módulo SaaS Proprietário*], [*Pilha Aberta Soberana*],
  [1. Marketing], [RD Station Marketing / E-mail / Forms], [Mautic + Listmonk + Directus],
  [2. Pipeline Comercial], [RD Station CRM / Oportunidades], [Twenty CRM + Cal.com + Documenso],
  [3. Atendimento Omnicanal], [RD Station Conversas / WhatsApp], [Chatwoot + Evolution API / WAHA + Typebot],
  [4. Camada de Cola], [RD Automações / Zapier / Auth], [Keycloak (SSO) + n8n + Traefik Proxy]
)

#v(8pt)

== 3. Governança & Entregáveis Tripartites

- *Identificador Canônico:* `ecos-<slug>` (ex: `ecos-rd-station-suite`)
- *Pasta Soberana de Saída:* `output/04-ecossistemas/ecos-<slug>/`
  - `materiais/ecos-<slug>.{html,md,pdf}`
  - `relatorios/DD-MM-AAAA-relatorio-execucao-ecos-<slug>.{html,md,pdf}`
- *Entrada Estruturada:* `scripts/data/ecos-<slug>.json`
- *Persistência de Estado (R11):* Registro na tabela `ecossistemas` do banco SQLite `estado_esteira.db` e sincronização no portal `INDICE-MESTRE.html`.

#v(8pt)

== 4. Componentes a Implementar na Fábrica Universal

#table(
  columns: (2fr, 2.5fr, 3.5fr),
  fill: (x, y) => if y == 0 { rgb("#f1f5f9") } else { none },
  stroke: 0.5pt + rgb("#e2e8f0"),
  inset: 6pt,
  [*Componente*], [*Arquivo Alvo*], [*Responsabilidade Principal*],
  [Registro Declarativo], [`scripts/tipos.py`], [Adicionar `dossie_ecossistema_html` com schema e gates.],
  [Schema JSON], [`scripts/schemas/schema_ecossistema.json`], [Estrutura de pilares, orquestração e deploy unificado.],
  [Linter Gate R9], [`scripts/validar_schemas_fluxos.py`], [Validação mecânica com bloqueio de compilação.],
  [Compilador Tripartite], [`scripts/compilar_ecossistema_tripartite.py`], [Geração de HTML Diamante R5-E, Markdown e PDF Typst.],
  [CLI Runner], [`scripts/run_fluxo4.py`], [Runner universal de execução com auto-ingestão SQLite.],
  [Skill Especialista], [`.agents/skills/fluxo4-ecossistemas/`], [Instruções do agente para acionamento via `/fluxo4`.]
)
