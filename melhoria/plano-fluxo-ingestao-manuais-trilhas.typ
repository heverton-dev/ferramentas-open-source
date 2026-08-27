#set page(
  paper: "a4",
  margin: (x: 1.8cm, y: 2.0cm),
  header: align(right)[
    #text(8pt, fill: rgb("#68738A"), font: "Liberation Sans")[
      Fábrica Universal · Governança Agêntica & Eficiência · 2026
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

#set text(
  font: "Liberation Sans",
  size: 9.5pt,
  lang: "pt",
  fill: rgb("#151A26")
)

#set par(justify: true, leading: 0.6em)

// Cores do Design System Corporativo
#let brand-dark = rgb("#1A446C")
#let brand-light = rgb("#DCE7F2")
#let brand-accent = rgb("#1B5E3B")
#let brand-accent-light = rgb("#D8EFE2")
#let surface = rgb("#F8F9FC")
#let border-color = rgb("#C7CEDB")
#let code-bg = rgb("#EEF2F6")

// Título & Cabeçalho Executivo
#align(center)[
  #block(
    fill: brand-light,
    inset: 11pt,
    radius: 4pt,
    stroke: 1pt + brand-dark,
    width: 100%,
    [
      #text(9pt, weight: "bold", fill: brand-dark, tracking: 0.1em)[
        PLANO DE ARQUITETURA & ESPECIFICAÇÃO DE FLUXO (VERSÃO 2.0 APRIMORADA)
      ]
      #v(3pt)
      #text(15pt, weight: "bold", fill: rgb("#0E1118"))[
        Fluxo de Ingestão Exaustiva, Manuais Operacionais e Trilhas de Aprendizado
      ]
      #v(3pt)
      #text(8.5pt, fill: rgb("#3B4457"))[
        Escopo Dual (Cirúrgico vs. Quinteto) · Zero Download Pesado · Matriz DTP (InDesign / Typst / Marp)
      ]
      #v(2pt)
      #text(8pt, fill: rgb("#68738A"))[
        Casos Piloto: Granola (Dossiê de Reuniões) ➔ Adobe InDesign (Matriz de Motores de Diagramação Aberta)
      ]
    ]
  )
]

#v(8pt)

== 1. Declaração de Entendimento da Proposta & Aprimoramentos

A proposta aprimorada consolida a transformação de qualquer dossiê vertical de desmantelamento SaaS em *duas entregas mestras corporativas prontas para produção*. A esteira foi enriquecida com três capacidades solicitadas pelo operador:

+ *Escopo Dual de Cobertura:* O operador pode escolher entre gerar os materiais para *uma ferramenta específica* (através de menu interativo no terminal exibindo as 5 opções do Quinteto Soberano) ou disparar a geração em lote para *todas as 5 ferramentas* do dossiê.
+ *Zero Download Pesado & Higiene Estrita (R18):* Fica expressamente vedado o download de binários pesados de vídeo (`.mp4`, `.webm`) ou áudio (`.mp3`). A extração da inteligência multimídia (YouTube, cursos e documentações) é 100% baseada em metadados, minutagens (timestamps) e transcrições textuais consumidas em memória e indexadas em JSON.
+ *Matriz de Motores de Compilação DTP (Baseada no dossiê InDesign):* Integração direta dos motores abertos catalogados no `vert-indesign`: *Typst* (compilação ultrarrápida de livros e relatórios executivos em PDF), *WeasyPrint / Paged.js* (PDF gráfico a partir de HTML/CSS) e *Marp* (apostilas de treinamento e slides executivos a partir de Markdown).

#v(6pt)

== 2. Matriz de Motores de Compilação & Formatos Finais (Dossiê InDesign)

Identificamos no repositório o compêndio `scripts/data/dossie-vertical-indesign.json` (`vert-indesign`), que mapeia as 5 melhores alternativas de DTP e diagramação aberta. Essas ferramentas foram integradas à esteira para entregar os materiais no molde perfeito para cada público:

#table(
  columns: (1fr, 1.2fr, 2.8fr),
  fill: (x, y) => if y == 0 { brand-dark } else if calc.even(y) { surface } else { none },
  stroke: 0.5pt + border-color,
  align: (left, left, left),
  [#text(weight: "bold", fill: white)[Motor Integrado]], [#text(weight: "bold", fill: white)[Papel na Esteira]], [#text(weight: "bold", fill: white)[Aplicação Prática no Projeto]],
  [Typst (Rank 2 no InDesign)], [PDF Executivo Oficial], [Compilação instantânea (50ms) do Manual Completo VPS + Uso e das Trilhas de Aprendizado em PDF com rigor tipográfico institucional.],
  [HTML Diamante (Nativo)], [Interface Web Interativa], [Layout autocontido com Hero Stats Bar, busca client-side e botões de cópia de comandos bash com 1 clique.],
  [WeasyPrint / Paged.js (Ranks 3/4)], [CSS Paged Media], [Geração de PDFs idênticos à versão web através de seletores CSS `@page`, cabeçalhos alternados e notas de rodapé.],
  [Marp (Rank 5 no InDesign)], [Apostilas & Slides DevOps], [Conversão direta do Markdown do manual em apresentações corporativas para reuniões de deploy e alinhamento de equipe.]
)

#v(6pt)

== 3. Especificação das Entregas Mestras

=== MATERIAL 1: Guia Técnico Duplo Unificado (Instalação VPS + Uso Exaustivo)
- *Parte I — Manual de Instalação em Produção na VPS (Passo a Passo Rígido):*
  1. Hardening do Ubuntu 24.04 LTS: usuário `deployer` no sudo, chave SSH pública, `PasswordAuthentication no` e firewall UFW (`22/tcp`, `80/tcp`, `443/tcp`).
  2. Provisionamento do Docker Engine oficial e plugin Docker Compose V2.
  3. Árvore de diretórios canônica `/opt/[app]/` com permissões rigorosas `750`.
  4. Docker Compose de produção com limites de recursos (`limits: cpus, memory`), restart policy `unless-stopped`, healthchecks nativos e volumes persistentes.
  5. Template de `.env` comentado linha por linha com variáveis obrigatórias e segredos.
  6. Reverse Proxy Nginx/Caddy com terminação TLS, renovação automática Let's Encrypt e cabeçalhos de segurança (HSTS, CSP).
  7. Serviço Systemd para persistência pós-reboot e rotina bash de snapshot de backup diário.
- *Parte II — Manual de Uso Hiperdetalhado & Exaustivo:*
  1. Arquitetura operacional: ciclo de gravação, transcrição Whisper e banco SQLite vetorial local.
  2. Dicionário exaustivo de CLI: tabela completa com 100% das flags, valores padrão e exemplos práticos.
  3. Guia de Interface (UI): filtros de busca semântica, seleção de modelos e controle de áudio.
  4. Referência de API REST / SDK: rotas, métodos HTTP, parâmetros de query e payloads JSON.
  5. Integração com Servidores MCP: conexão nativa com Claude Code, Cursor e Antigravity.
  6. Matriz de Troubleshooting: 10 incidentes frequentes com diagnóstico e resolução executável.
- *Parte III — Referências Bibliográficas Verificáveis:*
  - Tabela com todos os IDs `[Fxx]`, link direto testado (HTTP 200), categoria, autor e seção citada.

=== MATERIAL 2: Trilha Cronológica de Aprendizado Autoguiado
- *Timeline Pedagógica Interativa:*
  - *Fase 1: Fundamentos & Conceito (~45 min):* Leitura técnica de arquitetura e premissas de privacidade.
  - *Fase 2: Instalação & Operação de Base (~1h30):* Vídeos práticos de setup e tutoriais de deploy.
  - *Fase 3: Domínio de Recursos & Uso Diário (~2h30):* Guias práticos de interface e comandos de CLI.
  - *Fase 4: Recursos Avançados, API & Agentes (~2h00):* Integrações via API REST e servidores MCP.
- *Cartões de Recurso:* Título, tipo de mídia, autor, duração estimada, link direto e checklist de conclusão.

#v(6pt)

== 4. Plano de Ação em 4 Fases para Construção

#table(
  columns: (1.2fr, 2.6fr, 2.2fr),
  fill: (x, y) => if y == 0 { brand-dark } else if calc.even(y) { surface } else { none },
  stroke: 0.5pt + border-color,
  align: (left, left, left),
  [#text(weight: "bold", fill: white)[Fase]], [#text(weight: "bold", fill: white)[Atividades Chave]], [#text(weight: "bold", fill: white)[Entregáveis Técnicos]],
  [Fase 1: Schemas & CLI Dual], [Definição dos schemas JSON e desenvolvimento do seletor CLI `orquestrador_esteira_manuais.py` (menu de 1 a 5 ou Quinteto Completo em lote).], [3 Schemas JSON + Seletor de Escopo Dual CLI.],
  [Fase 2: Crawler & Indexador], [Desenvolvimento do crawler leve em memória (zero download pesado) e compilador `compilar_sumario_fontes.py` com gate HTTP 200 assíncrono. Piloto com Screenpipe.], [Crawler em memória + `sumario-fontes-screenpipe.json` + Gate G1.],
  [Fase 3: Manual & Matriz DTP], [Criação do molde Diamante HTML e template Typst institucional. Desenvolvimento de `gerar_manual_operacional.py` com gate `auditar_citacoes_manuais.py`.], [Manual unificado HTML/MD/PDF em `output/manuais/` + Gate G2.],
  [Fase 4: Trilha & Custódia], [Desenvolvimento do gerador da Trilha `gerar_trilha_aprendizado.py`, teste em lote para o Quinteto do Granola e espelhamento em `docs/`.], [Trilha HTML/MD/PDF + Suporte a lote para o Quinteto + Espelhos.]
)

#v(8pt)

#align(center)[
  #block(
    fill: brand-accent-light,
    inset: 9pt,
    radius: 4pt,
    stroke: 1pt + brand-accent,
    width: 100%,
    [
      #text(9.5pt, weight: "bold", fill: brand-accent)[
        STATUS: Planejamento Aprimorado Concluído · Aguardando Aprovação do Operador
      ]
      #v(2pt)
      #text(8pt, fill: rgb("#1F2937"))[
        Nenhuma alteração em código de produção foi realizada. A implementação da Fase 1 terá início imediato após o sinal verde do usuário.
      ]
    ]
  )
]
