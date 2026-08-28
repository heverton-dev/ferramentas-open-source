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
    [Suíte do Ecossistema Soberano · Google Workspace (Business Standard 50 usuários + Google Vault + Endpoint Management)],
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
  #text(size: 24pt, weight: "bold", fill: rgb("#0f172a"), font: "Liberation Serif")[Macro-Ecossistema Google Workspace: Comunicação, Produtividade & Governança] \
  #v(6pt)
  #text(size: 12pt, fill: rgb("#334155"))[Arquitetura Aberta Integrada com Quinteto Soberano por Grupo, SSO, Barramento de Eventos e MCPs] \
  #v(16pt)
  #line(length: 60%, stroke: 1pt + rgb("#cbd5e1"))
  #v(16pt)
  #text(size: 10pt, fill: rgb("#475569"))[
   *Macro-Ecossistema Alvo:* Google Workspace (Business Standard 50 usuários + Google Vault + Endpoint Management) \
   *Economia Anual Líquida:* #text(fill: rgb("#00875A"), weight: "bold")[R\$ 82.200/ano (Economia Líquida de 95.1%)] \
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
Dossiê completo de desmantelamento soberano para o Macro-Ecossistema Google Workspace (Gmail, Chat, Meet, Agenda, Drive, Docs, Sheets, Slides, Forms, Keep, Sites, Admin, Vault e Endpoint). Cada frente de negócio é estruturada com seu próprio Quinteto Soberano (A Mais Robusta, Mais Completa, Mais Moderna, Mais Leve e Mais Simples), acompanhada de análise de TCO, guias práticos, aderência white-label e ecossistema agêntico de MCPs.

A migração de suítes de software proprietário fechado para ecossistemas open source auto-hospedados em VPS representa a maior alavanca de eficiência operacional da década. Este livro-texto reúne as especificações de engenharia para desmantelar a suíte *Google Workspace (Business Standard 50 usuários + Google Vault + Endpoint Management)* com segurança jurídica, integridade de dados e autonomia digital irrestrita.

#pagebreak()

= Capítulo 1: Engenharia Financeira, TCO Global & Payback

#grid(
 columns: (1fr, 1fr),
 gutter: 10pt,
 rect(fill: rgb("#fef2f2"), stroke: 0.5pt + rgb("#fecaca"), inset: 10pt, radius: 2pt)[
  #text(size: 8pt, fill: rgb("#991b1b"), weight: "bold")[CUSTO SAAS ANUAL (Google Workspace (Business Standard 50 usuários + Google Vault + Endpoint Management))] \
  #text(size: 14pt, weight: "bold", fill: rgb("#dc2626"))[R\$ 86.400/ano (Google Workspace Business Standard 50 usuários R\$ 43.200/ano + Google Vault & Endpoint Management R\$ 43.200/ano)]
 ],
 rect(fill: rgb("#f0fdf4"), stroke: 0.5pt + rgb("#bbf7d0"), inset: 10pt, radius: 2pt)[
  #text(size: 8pt, fill: rgb("#166534"), weight: "bold")[ECONOMIA LÍQUIDA ANUAL NO CAIXA] \
  #text(size: 14pt, weight: "bold", fill: rgb("#16a34a"))[R\$ 82.200/ano (Economia Líquida de 95.1%)]
 ]
)

#v(10pt)
- *Custo VPS Própria:* R\$ 4.200/ano (VPS 8 vCPU / 16 GB RAM a R\$ 350/mês) (Cluster Consolidado 8 vCPU / 16 GB RAM)
- *Retorno sobre Investimento (ROI / Payback):* Payback positivo em apenas 18 dias de operação unificada.

#v(10pt)
== Desmembramento Contábil por Frente de Negócio

#table(
 columns: (1.5fr, 1.8fr, 1.2fr, 1.2fr, 0.9fr),
 fill: (x, y) => if y == 0 { rgb("#f1f5f9") } else { none },
 stroke: 0.5pt + rgb("#cbd5e1"),
 inset: 5pt,
 [*Grupo*], [*SaaS Alvo*], [*Custo SaaS*], [*Economia*], [*Margem*],
 [Grupo 1: Comunicação Unificada], [Google Workspace Gmail/Chat/Meet/Calendar/Contacts (50 usuários)], [R\$ 43.200/ano], [R\$ 41.520/ano], [96.1%],
[Grupo 2: Produtividade & Documentos], [Google Workspace Drive/Docs/Sheets/Slides/Forms/Keep (50 usuários)], [R\$ 28.800/ano], [R\$ 27.360/ano], [95.0%],
[Grupo 3: Identidade & Governança], [Google Vault + Admin Console + Endpoint Management (50 usuários)], [R\$ 14.400/ano], [R\$ 13.320/ano], [92.5%],

)

#pagebreak()
= Capítulo 2: Infraestrutura Global, Dimensionamento da VPS & Provedores Validados

- *Perfil de Máquina Recomendado:* `8 vCPU Dedicated Cloud / 16 GB RAM ECC / 200-300 GB NVMe SSD / Link 1 Gbps / Ubuntu 24.04 LTS x86\_64`
- *Racional de Engenharia:* Garante estabilidade absoluta para os 11 contêineres rodando em simultâneo com isolamento de processos, prevenindo gargalos de I/O em banco de dados e eliminando o risco do OOM Killer durante picos de sincronização de arquivos e e-mails.

#v(6pt)
== Provedores de Nuvem Recomendados & Custo Mensal

#table(
 columns: (1.5fr, 1.2fr, 2.3fr),
 fill: (x, y) => if y == 0 { rgb("#f1f5f9") } else { none },
 stroke: 0.5pt + rgb("#cbd5e1"),
 inset: 5pt,
 [*Provedor de Nuvem*], [*Custo Mensal*], [*Vantagem Principal & SLA*],
 [Hetzner Cloud (CPX41 / CCX23)], [`€ 28 (~ R\$ 170/mês)`], [Melhor custo-benefício e performance bruta por vCPU dedicada (Datacenters UE/EUA).],
[Contabo (Cloud VPS L)], [`€ 16 (~ R\$ 100/mês)`], [Maior volume de memória RAM e disco NVMe por valor investido.],
[DigitalOcean (Dedicated 16GB)], [`\$ 84 (~ R\$ 460/mês)`], [Excelente SLA de rede, suporte global e facilidade de snapshots.],
[AWS Lightsail (16GB RAM)], [`\$ 80 (~ R\$ 440/mês)`], [Infraestrutura corporativa AWS com 5 TB de transferência inclusos.],

)

#v(8pt)
== Alocação Técnica de Recursos por Serviço (vCPU & RAM)

#table(
 columns: (1.5fr, 0.7fr, 0.7fr, 2.8fr),
 fill: (x, y) => if y == 0 { rgb("#f1f5f9") } else { none },
 stroke: 0.5pt + rgb("#cbd5e1"),
 inset: 4pt,
 [*Serviço / Módulo*], [*vCPU*], [*RAM*], [*Motivo Técnico & Gargalo*],
 [Traefik Ingress & TLS], [`0.5 vCPU`], [`256 MB`], [Roteamento reativo de borda, compressão Brotli/Gzip e renovação automática de certificados SSL.],
[Keycloak SSO (OpenJDK JVM)], [`1.5 vCPU`], [`2.0 GB`], [Baseline da JVM Java para autenticação federada OIDC/SAML e criptografia de senhas Argon2.],
[Nextcloud Hub & Talk], [`2.0 vCPU`], [`4.0 GB`], [Processamento de e-mail, agenda, contatos e chamadas WebRTC do Talk para 50 colaboradores.],
[CryptPad & ONLYOFFICE], [`1.5 vCPU`], [`3.0 GB`], [Edição colaborativa de documentos em tempo real e conversão de formatos Office.],
[Seafile & Stalwart Mail], [`1.0 vCPU`], [`2.0 GB`], [Sincronização de blocos de arquivos e envio/recebimento de e-mails com filtros anti-spam.],
[n8n Orquestrador], [`0.5 vCPU`], [`1.0 GB`], [Execução assíncrona de fluxos de provisionamento e webhooks entre identidade e aplicativos.],
[Buffer de Picos / Anti-OOM], [`1.0 vCPU`], [`1.7 GB`], [Margem de folga do kernel Linux para backups diários pg\_dump e picos sazonais.],

)

#pagebreak()
= Capítulo 3: Matriz Estratégica do Quinteto Soberano

#table(
 columns: (0.5fr, 1.3fr, 1.3fr, 1.8fr, 2.2fr, 1.3fr),
 fill: (x, y) => if y == 0 { rgb("#f1f5f9") } else { none },
 stroke: 0.5pt + rgb("#cbd5e1"),
 inset: 4pt,
 [*Nº*], [*Grupo*], [*Persona*], [*Ferramenta*], [*Substitui*], [*Economia*],
 [1], [Grupo 1], [Completa], [*Nextcloud Hub*], [Gmail + Google Calendar + Google Contacts + Google Chat + Google Meet], [R\$ 43.200/ano (50 usuários)],
[2], [Grupo 1], [Robusta], [*Zimbra Collaboration*], [Gmail + Google Calendar + Google Contacts (carga enterprise)], [R\$ 43.200/ano (50 usuários)],
[3], [Grupo 1], [Moderna], [*Stalwart Mail Server*], [Gmail + Google Calendar + Google Contacts (protocolo moderno)], [R\$ 43.200/ano (50 usuários)],
[4], [Grupo 1], [Leve], [*Mailu*], [Gmail + Google Calendar + Google Contacts (carga leve)], [R\$ 43.200/ano (50 usuários)],
[5], [Grupo 1], [Simples], [*Mail-in-a-Box*], [Gmail + Google Calendar + Google Contacts (instalação zero-config)], [R\$ 43.200/ano (50 usuários)],
[6], [Grupo 2], [Completa], [*CryptPad*], [Google Drive + Docs + Sheets + Slides + Forms + Keep], [R\$ 28.800/ano (50 usuários)],
[7], [Grupo 2], [Robusta], [*ownCloud*], [Google Drive (armazenamento e compartilhamento empresarial)], [R\$ 28.800/ano (50 usuários)],
[8], [Grupo 2], [Moderna], [*ONLYOFFICE Docs*], [Google Docs + Sheets + Slides (edição colaborativa)], [R\$ 28.800/ano (50 usuários)],
[9], [Grupo 2], [Leve], [*Seafile*], [Google Drive (sincronização e backup de arquivos)], [R\$ 28.800/ano (50 usuários)],
[10], [Grupo 2], [Simples], [*HedgeDoc*], [Google Docs + Google Keep (notas e documentação leve)], [R\$ 28.800/ano (50 usuários)],
[11], [Grupo 3], [Completa], [*Authentik*], [Google Cloud Identity + Admin Console (SSO e federação)], [R\$ 14.400/ano (50 usuários)],
[12], [Grupo 3], [Robusta], [*Keycloak*], [Google Cloud Identity + Admin Console (IAM enterprise)], [R\$ 14.400/ano (50 usuários)],
[13], [Grupo 3], [Moderna], [*ZITADEL*], [Google Cloud Identity + Admin Console (IAM moderno)], [R\$ 14.400/ano (50 usuários)],
[14], [Grupo 3], [Leve], [*Authelia*], [Google Endpoint Management (MFA na borda)], [R\$ 14.400/ano (50 usuários)],
[15], [Grupo 3], [Simples], [*Casdoor*], [Google Cloud Identity (SSO simples)], [R\$ 14.400/ano (50 usuários)],

)


#pagebreak()
= Capítulo 3: Pilar 01 · Grupo 1: Comunicação Unificada (E-mail, Chat, Vídeo, Agenda & Contatos)

#text(size: 9pt, fill: rgb("#0284c7"), weight: "bold")[Alvo SaaS Substituído: Google Workspace (Gmail + Google Chat + Google Meet + Google Calendar + Google Contacts)] \
#text(size: 9pt, fill: rgb("#00875A"), weight: "bold")[Subtotal de Economia do Grupo: R\$ 43.200/ano] \
#text(size: 9pt, style: "italic", fill: rgb("#475569"))[Frente responsável pela caixa postal corporativa, mensageria instantânea, videoconferência, agenda compartilhada e catálogo de contatos. Substitui integralmente o Gmail, o Google Chat, o Google Meet, o Google Calendar e o Google Contacts por uma suíte soberana sob domínio próprio, com criptografia ponta a ponta e sem cobrança por usuário.]

#v(8pt)

== 01. Nextcloud Hub · Suíte Integrada de Mail, Calendar, Contacts, Talk & Files (Persona: Completa)

#rect(fill: rgb("#f8fafc"), stroke: 0.5pt + rgb("#cbd5e1"), inset: 8pt, radius: 2pt, width: 100%)[
 #grid(
  columns: (1fr, 1fr, 1fr),
  gutter: 6pt,
  [*Substitui:* Gmail + Google Calendar + Google Contacts + Google Chat + Google Meet],
  [*Economia:* #text(fill: rgb("#00875A"), weight: "bold")[R\$ 43.200/ano (50 usuários)]],
  [*Licença:* `AGPL-3.0`]
 )
]

*1. O Que Faz & Como Funciona:* \
Centraliza e-mail, agenda, contatos, chat e vídeo com interface única e aplicativos móveis próprios. PHP/Symfony com servidor de sincronização, banco PostgreSQL/MySQL e módulo Talk sobre WebRTC para chamadas.

```bash
docker run -d -p 8080:80 --name nextcloud nextcloud:latest
```

*2. Racional da Escolha & Veredito Técnico:* \
Única plataforma open source que reúne e-mail, agenda, contatos, chat e videoconferência em um só painel, com sincronização CalDAV/CardDAV nativa e cliente Talk baseado em chamadas WebRTC. \
#text(style: "italic", fill: rgb("#334155"))[*Veredito:* A escolha mais completa para substituir o Google Workspace de ponta a ponta em comunicação, mantendo os dados sob controle total da empresa.]

*3. Requisitos de Infraestrutura & White-Label:* \
- RAM Mínima: `4 GB RAM` | CPU: `2 vCPU` | Docker: `nextcloud:latest`
- Customização UI: Suporte nativo a logo institucional, favicon e paleta de cores corporativas no painel de administração, além de temas por usuário. (Esforço: Baixo)

#v(10pt)

== 02. Zimbra Collaboration · Groupware Empresarial Maduro para Grandes Operações (Persona: Robusta)

#rect(fill: rgb("#f8fafc"), stroke: 0.5pt + rgb("#cbd5e1"), inset: 8pt, radius: 2pt, width: 100%)[
 #grid(
  columns: (1fr, 1fr, 1fr),
  gutter: 6pt,
  [*Substitui:* Gmail + Google Calendar + Google Contacts (carga enterprise)],
  [*Economia:* #text(fill: rgb("#00875A"), weight: "bold")[R\$ 43.200/ano (50 usuários)]],
  [*Licença:* `GPL-3.0`]
 )
]

*1. O Que Faz & Como Funciona:* \
Gerencia e-mail, agenda, contatos, tarefas e documentos colaborativos em um único servidor. Java (Jetty/Tomcat) com armazenamento em PostgreSQL e servidor de e-mail baseado em Postfix/OpenLDAP.

```bash
docker run -d -p 8080:8080 --name zimbra zimbra/zimbra-community:latest
```

*2. Racional da Escolha & Veredito Técnico:* \
Plataforma open source em produção há mais de 15 anos em universidades e governos, com motor de e-mail robusto, anti-spam integrado e cliente web completo. \
#text(style: "italic", fill: rgb("#334155"))[*Veredito:* A opção mais sólida para organizações que exigem resiliência extrema e suporte a milhares de usuários simultâneos sem custo por licença.]

*3. Requisitos de Infraestrutura & White-Label:* \
- RAM Mínima: `8 GB RAM` | CPU: `4 vCPU` | Docker: `zimbra/zimbra-community:latest`
- Customização UI: Permite trocar logo, cores e nome da organização no tema Modern UI e no portal de login. (Esforço: Médio)

#v(10pt)

== 03. Stalwart Mail Server · Servidor de E-mail Moderno em Rust com JMAP, CalDAV & CardDAV (Persona: Moderna)

#rect(fill: rgb("#f8fafc"), stroke: 0.5pt + rgb("#cbd5e1"), inset: 8pt, radius: 2pt, width: 100%)[
 #grid(
  columns: (1fr, 1fr, 1fr),
  gutter: 6pt,
  [*Substitui:* Gmail + Google Calendar + Google Contacts (protocolo moderno)],
  [*Economia:* #text(fill: rgb("#00875A"), weight: "bold")[R\$ 43.200/ano (50 usuários)]],
  [*Licença:* `AGPL-3.0`]
 )
]

*1. O Que Faz & Como Funciona:* \
Fornece e-mail, agenda e contatos modernos com protocolo JMAP e baixíssimo consumo de recursos. Binário único em Rust com armazenamento em RocksDB/PostgreSQL e painel web em React.

```bash
docker run -d -p 8080:8080 -p 993:993 --name stalwart stalwartlabs/stalwart:latest
```

*2. Racional da Escolha & Veredito Técnico:* \
Escrito em Rust para máxima performance e segurança, suporta SMTP, IMAP, POP3, JMAP, CalDAV e CardDAV com gerenciamento web elegante e DMARC/DKIM nativos. \
#text(style: "italic", fill: rgb("#334155"))[*Veredito:* A escolha moderna para quem busca performance, segurança e protocolo JMAP sem a carga de groupwares legados.]

*3. Requisitos de Infraestrutura & White-Label:* \
- RAM Mínima: `2 GB RAM` | CPU: `2 vCPU` | Docker: `stalwartlabs/stalwart:latest`
- Customização UI: Painel web com logo e nome da organização configuráveis e temas claros/escuros. (Esforço: Baixo)

#v(10pt)

== 04. Mailu · Servidor de E-mail Dockerizado Leve e Completo (Persona: Leve)

#rect(fill: rgb("#f8fafc"), stroke: 0.5pt + rgb("#cbd5e1"), inset: 8pt, radius: 2pt, width: 100%)[
 #grid(
  columns: (1fr, 1fr, 1fr),
  gutter: 6pt,
  [*Substitui:* Gmail + Google Calendar + Google Contacts (carga leve)],
  [*Economia:* #text(fill: rgb("#00875A"), weight: "bold")[R\$ 43.200/ano (50 usuários)]],
  [*Licença:* `MIT`]
 )
]

*1. O Que Faz & Como Funciona:* \
Entrega e-mail, webmail, agenda e contatos com interface administrativa simples. Orquestra Postfix, Dovecot, Roundcube, PostfixAdmin e Redis em contêineres leves sobre Docker.

```bash
docker compose -f mailu.yml up -d
```

*2. Racional da Escolha & Veredito Técnico:* \
Distribuição Docker pronta com webmail, filtros anti-spam, calendário e contatos, consumindo poucos recursos e com deploy em minutos. \
#text(style: "italic", fill: rgb("#334155"))[*Veredito:* Ideal para quem quer um servidor de e-mail completo e leve, com deploy quase instantâneo e manutenção mínima.]

*3. Requisitos de Infraestrutura & White-Label:* \
- RAM Mínima: `2 GB RAM` | CPU: `1 vCPU` | Docker: `mailu/mailu:latest`
- Customização UI: Logo e cores do webmail Roundcube e do painel admin personalizáveis por tema. (Esforço: Baixo)

#v(10pt)

== 05. Mail-in-a-Box · Servidor de E-mail Completo com Instalação de 1 Script (Persona: Simples)

#rect(fill: rgb("#f8fafc"), stroke: 0.5pt + rgb("#cbd5e1"), inset: 8pt, radius: 2pt, width: 100%)[
 #grid(
  columns: (1fr, 1fr, 1fr),
  gutter: 6pt,
  [*Substitui:* Gmail + Google Calendar + Google Contacts (instalação zero-config)],
  [*Economia:* #text(fill: rgb("#00875A"), weight: "bold")[R\$ 43.200/ano (50 usuários)]],
  [*Licença:* `GPL-3.0`]
 )
]

*1. O Que Faz & Como Funciona:* \
Instala e mantém um servidor de e-mail corporativo completo e seguro com um comando. Script Bash que provisiona Postfix, Dovecot, Nextcloud (agenda/contatos) e Roundcube sobre Ubuntu.

```bash
curl -s https://mailinabox.email/setup.sh | sudo bash
```

*2. Racional da Escolha & Veredito Técnico:* \
Um único script configura e-mail, DNS, calendário, contatos e webmail seguros em um servidor Ubuntu limpo, sem conhecimento de Linux. \
#text(style: "italic", fill: rgb("#334155"))[*Veredito:* A maneira mais simples de sair do Gmail: um script e pronto, com painel de administração amigável para não-técnicos.]

*3. Requisitos de Infraestrutura & White-Label:* \
- RAM Mínima: `1 GB RAM` | CPU: `1 vCPU` | Docker: `script nativo Ubuntu`
- Customização UI: Logo e nome da organização configuráveis no painel administrativo web. (Esforço: Baixo)

#v(10pt)

#pagebreak()
= Capítulo 4: Pilar 02 · Grupo 2: Produtividade & Gestão de Documentos (Drive, Docs, Sheets, Slides, Forms, Keep, Sites)

#text(size: 9pt, fill: rgb("#0284c7"), weight: "bold")[Alvo SaaS Substituído: Google Workspace (Drive + Docs + Sheets + Slides + Forms + Keep + Sites)] \
#text(size: 9pt, fill: rgb("#00875A"), weight: "bold")[Subtotal de Economia do Grupo: R\$ 28.800/ano] \
#text(size: 9pt, style: "italic", fill: rgb("#475569"))[Frente responsável pelo armazenamento de arquivos, edição colaborativa de documentos, planilhas e apresentações, formulários, notas e intranet. Substitui o Google Drive, Docs, Sheets, Slides, Forms, Keep e Sites por ferramentas soberanas com edição simultânea e controle total de versões.]

#v(8pt)

== 01. CryptPad · Suíte Office Criptografada de Ponta a Ponta (Drive, Docs, Sheets, Slides, Forms) (Persona: Completa)

#rect(fill: rgb("#f8fafc"), stroke: 0.5pt + rgb("#cbd5e1"), inset: 8pt, radius: 2pt, width: 100%)[
 #grid(
  columns: (1fr, 1fr, 1fr),
  gutter: 6pt,
  [*Substitui:* Google Drive + Docs + Sheets + Slides + Forms + Keep],
  [*Economia:* #text(fill: rgb("#00875A"), weight: "bold")[R\$ 28.800/ano (50 usuários)]],
  [*Licença:* `AGPL-3.0`]
 )
]

*1. O Que Faz & Como Funciona:* \
Fornece editor de documentos, planilhas, slides, formulários e armazenamento criptografado com colaboração em tempo real. Node.js com criptografia client-side (ChainPad) e sincronização via WebSocket, sem leitura do servidor.

```bash
docker run -d -p 3000:3000 --name cryptpad cryptpad/cryptpad:latest
```

*2. Racional da Escolha & Veredito Técnico:* \
Única suíte office open source com criptografia de ponta a ponta: nem o servidor enxerga o conteúdo. Inclui Drive, documentos, planilhas, apresentações, formulários, quadro kanban e blocos de notas. \
#text(style: "italic", fill: rgb("#334155"))[*Veredito:* A escolha mais completa e segura para substituir o Google Drive e a suíte office, com privacidade absoluta dos dados.]

*3. Requisitos de Infraestrutura & White-Label:* \
- RAM Mínima: `2 GB RAM` | CPU: `2 vCPU` | Docker: `cryptpad/cryptpad:latest`
- Customização UI: Logo, favicon e cores institucionais configuráveis no arquivo config.js e no painel admin. (Esforço: Baixo)

#v(10pt)

== 02. ownCloud · Plataforma Enterprise de Sincronização e Compartilhamento de Arquivos (Persona: Robusta)

#rect(fill: rgb("#f8fafc"), stroke: 0.5pt + rgb("#cbd5e1"), inset: 8pt, radius: 2pt, width: 100%)[
 #grid(
  columns: (1fr, 1fr, 1fr),
  gutter: 6pt,
  [*Substitui:* Google Drive (armazenamento e compartilhamento empresarial)],
  [*Economia:* #text(fill: rgb("#00875A"), weight: "bold")[R\$ 28.800/ano (50 usuários)]],
  [*Licença:* `AGPL-3.0`]
 )
]

*1. O Que Faz & Como Funciona:* \
Sincroniza arquivos entre dispositivos, gerencia compartilhamentos e mantém histórico de versões. PHP/Symfony com armazenamento em disco ou S3 e sincronização via cliente desktop/móvel.

```bash
docker run -d -p 8080:8080 --name owncloud owncloud/server:latest
```

*2. Racional da Escolha & Veredito Técnico:* \
Fork maduro e estável com foco em grandes volumes de arquivos, permissões granulares, federação entre instâncias e integrações corporativas. \
#text(style: "italic", fill: rgb("#334155"))[*Veredito:* A escolha robusta para armazenamento de arquivos em escala empresarial, com federação e controle de versão confiáveis.]

*3. Requisitos de Infraestrutura & White-Label:* \
- RAM Mínima: `2 GB RAM` | CPU: `2 vCPU` | Docker: `owncloud/server:latest`
- Customização UI: Logo, cores e nome da organização configuráveis no tema e no painel de administração. (Esforço: Médio)

#v(10pt)

== 03. ONLYOFFICE Docs · Motor de Edição Colaborativa Moderna (Docs, Sheets, Slides) (Persona: Moderna)

#rect(fill: rgb("#f8fafc"), stroke: 0.5pt + rgb("#cbd5e1"), inset: 8pt, radius: 2pt, width: 100%)[
 #grid(
  columns: (1fr, 1fr, 1fr),
  gutter: 6pt,
  [*Substitui:* Google Docs + Sheets + Slides (edição colaborativa)],
  [*Economia:* #text(fill: rgb("#00875A"), weight: "bold")[R\$ 28.800/ano (50 usuários)]],
  [*Licença:* `AGPL-3.0`]
 )
]

*1. O Que Faz & Como Funciona:* \
Renderiza e edita documentos, planilhas e apresentações colaborativas no navegador. Node.js + servidores de conversão em C++ com WebSocket para coautoria em tempo real.

```bash
docker run -d -p 8080:80 --name onlyoffice onlyoffice/documentserver:latest
```

*2. Racional da Escolha & Veredito Técnico:* \
Compatibilidade quase total com formatos .docx, .xlsx e .pptx, edição colaborativa em tempo real e integração nativa com Nextcloud, ownCloud e Seafile. \
#text(style: "italic", fill: rgb("#334155"))[*Veredito:* A escolha moderna para quem precisa de fidelidade total ao Microsoft Office e colaboração em tempo real sem o Google.]

*3. Requisitos de Infraestrutura & White-Label:* \
- RAM Mínima: `4 GB RAM` | CPU: `2 vCPU` | Docker: `onlyoffice/documentserver:latest`
- Customização UI: Logo e cores da barra de ferramentas configuráveis via parâmetros de branding. (Esforço: Baixo)

#v(10pt)

== 04. Seafile · Armazenamento de Arquivos de Altíssima Performance (Persona: Leve)

#rect(fill: rgb("#f8fafc"), stroke: 0.5pt + rgb("#cbd5e1"), inset: 8pt, radius: 2pt, width: 100%)[
 #grid(
  columns: (1fr, 1fr, 1fr),
  gutter: 6pt,
  [*Substitui:* Google Drive (sincronização e backup de arquivos)],
  [*Economia:* #text(fill: rgb("#00875A"), weight: "bold")[R\$ 28.800/ano (50 usuários)]],
  [*Licença:* `Apache-2.0`]
 )
]

*1. O Que Faz & Como Funciona:* \
Sincroniza e versiona arquivos com biblioteca de blocos e criptografia no cliente. Backend em C (ccnet/seafile) com banco MySQL e armazenamento de blocos em disco.

```bash
docker run -d -p 8000:8000 --name seafile seafileltd/seafile-mc:latest
```

*2. Racional da Escolha & Veredito Técnico:* \
Escrito em C com biblioteca de blocos, entrega sincronização de arquivos muito mais rápida que concorrentes, ideal para grandes volumes e poucos recursos. \
#text(style: "italic", fill: rgb("#334155"))[*Veredito:* A escolha leve e veloz para armazenamento de arquivos em larga escala, com consumo mínimo de RAM.]

*3. Requisitos de Infraestrutura & White-Label:* \
- RAM Mínima: `1 GB RAM` | CPU: `1 vCPU` | Docker: `seafileltd/seafile-mc:latest`
- Customização UI: Logo e nome da organização configuráveis no painel de administração. (Esforço: Baixo)

#v(10pt)

== 05. HedgeDoc · Edição Colaborativa de Markdown Simples e Elegante (Persona: Simples)

#rect(fill: rgb("#f8fafc"), stroke: 0.5pt + rgb("#cbd5e1"), inset: 8pt, radius: 2pt, width: 100%)[
 #grid(
  columns: (1fr, 1fr, 1fr),
  gutter: 6pt,
  [*Substitui:* Google Docs + Google Keep (notas e documentação leve)],
  [*Economia:* #text(fill: rgb("#00875A"), weight: "bold")[R\$ 28.800/ano (50 usuários)]],
  [*Licença:* `AGPL-3.0`]
 )
]

*1. O Que Faz & Como Funciona:* \
Permite criar e editar documentos Markdown colaborativos com preview em tempo real. Node.js com banco PostgreSQL e sincronização via WebSocket (ot.js).

```bash
docker run -d -p 3000:3000 --name hedgedoc hedgedoc/hedgedoc:latest
```

*2. Racional da Escolha & Veredito Técnico:* \
Editor colaborativo em tempo real baseado em Markdown, com curadoria de links, histórico de versões e zero complexidade para usuários não-técnicos. \
#text(style: "italic", fill: rgb("#334155"))[*Veredito:* A escolha simples para documentação, atas e notas colaborativas sem a complexidade de um office completo.]

*3. Requisitos de Infraestrutura & White-Label:* \
- RAM Mínima: `1 GB RAM` | CPU: `1 vCPU` | Docker: `hedgedoc/hedgedoc:latest`
- Customização UI: Logo e CSS corporativo configuráveis via variáveis de ambiente e tema. (Esforço: Baixo)

#v(10pt)

#pagebreak()
= Capítulo 5: Pilar 03 · Grupo 3: Identidade, Segurança & Governança (Admin, SSO, Vault & Endpoint)

#text(size: 9pt, fill: rgb("#0284c7"), weight: "bold")[Alvo SaaS Substituído: Google Workspace (Admin Console + Cloud Identity + Google Vault + Endpoint Management)] \
#text(size: 9pt, fill: rgb("#00875A"), weight: "bold")[Subtotal de Economia do Grupo: R\$ 14.400/ano] \
#text(size: 9pt, style: "italic", fill: rgb("#475569"))[Frente responsável pelo login único (SSO), autenticação multifator, retenção de dados (eDiscovery), conformidade e gestão de dispositivos. Substitui o Admin Console, o Cloud Identity, o Google Vault e o Endpoint Management por ferramentas soberanas de identidade e governança.]

#v(8pt)

== 01. Authentik · Plataforma Moderna de Identidade (SSO, MFA & Políticas) (Persona: Completa)

#rect(fill: rgb("#f8fafc"), stroke: 0.5pt + rgb("#cbd5e1"), inset: 8pt, radius: 2pt, width: 100%)[
 #grid(
  columns: (1fr, 1fr, 1fr),
  gutter: 6pt,
  [*Substitui:* Google Cloud Identity + Admin Console (SSO e federação)],
  [*Economia:* #text(fill: rgb("#00875A"), weight: "bold")[R\$ 14.400/ano (50 usuários)]],
  [*Licença:* `MIT`]
 )
]

*1. O Que Faz & Como Funciona:* \
Centraliza login único, autenticação multifator e políticas de acesso para todos os aplicativos da suíte. Backend Python (Django) com frontend React e provedores OIDC/SAML/LDAP.

```bash
docker run -d -p 9000:9000 --name authentik authentik/server:latest
```

*2. Racional da Escolha & Veredito Técnico:* \
Interface moderna com provedor de identidade completo, suporte a OIDC/SAML/LDAP, MFA adaptativo e editor visual de políticas de acesso por aplicação. \
#text(style: "italic", fill: rgb("#334155"))[*Veredito:* A escolha mais completa e moderna para substituir o Cloud Identity, com políticas visuais e MFA adaptativo nativos.]

*3. Requisitos de Infraestrutura & White-Label:* \
- RAM Mínima: `2 GB RAM` | CPU: `2 vCPU` | Docker: `authentik/server:latest`
- Customização UI: Logo, favicon e paleta de cores corporativas no tema do painel e das telas de login. (Esforço: Baixo)

#v(10pt)

== 02. Keycloak · Identity and Access Management Empresarial (Red Hat) (Persona: Robusta)

#rect(fill: rgb("#f8fafc"), stroke: 0.5pt + rgb("#cbd5e1"), inset: 8pt, radius: 2pt, width: 100%)[
 #grid(
  columns: (1fr, 1fr, 1fr),
  gutter: 6pt,
  [*Substitui:* Google Cloud Identity + Admin Console (IAM enterprise)],
  [*Economia:* #text(fill: rgb("#00875A"), weight: "bold")[R\$ 14.400/ano (50 usuários)]],
  [*Licença:* `Apache-2.0`]
 )
]

*1. O Que Faz & Como Funciona:* \
Fornece SSO, MFA, federação e gerenciamento de identidade para toda a suíte. Java (Quarkus) com provedores OIDC/SAML e armazenamento em PostgreSQL.

```bash
docker run -d -p 8080:8080 --name keycloak quay.io/keycloak/keycloak:latest start-dev
```

*2. Racional da Escolha & Veredito Técnico:* \
Padrão de mercado para IAM open source, com suporte maduro a SAML, OIDC, LDAP, federação e realms isolados para múltiplas organizações. \
#text(style: "italic", fill: rgb("#334155"))[*Veredito:* A escolha robusta para IAM em escala enterprise, com federação SAML e isolamento por realms.]

*3. Requisitos de Infraestrutura & White-Label:* \
- RAM Mínima: `2 GB RAM` | CPU: `2 vCPU` | Docker: `quay.io/keycloak/keycloak:latest`
- Customização UI: Tema de login e conta personalizável via tema customizado em CSS/HTML. (Esforço: Médio)

#v(10pt)

== 03. ZITADEL · IAM Moderno Event-Sourced com OIDC, SAML & MFA (Persona: Moderna)

#rect(fill: rgb("#f8fafc"), stroke: 0.5pt + rgb("#cbd5e1"), inset: 8pt, radius: 2pt, width: 100%)[
 #grid(
  columns: (1fr, 1fr, 1fr),
  gutter: 6pt,
  [*Substitui:* Google Cloud Identity + Admin Console (IAM moderno)],
  [*Economia:* #text(fill: rgb("#00875A"), weight: "bold")[R\$ 14.400/ano (50 usuários)]],
  [*Licença:* `Apache-2.0`]
 )
]

*1. O Que Faz & Como Funciona:* \
Fornece identidade, SSO e MFA com modelo de eventos e auditoria completa. Go com CQRS/Event-Sourcing, armazenamento em PostgreSQL e APIs gRPC/REST.

```bash
docker run -d -p 8080:8080 --name zitadel zitadel/zitadel:latest
```

*2. Racional da Escolha & Veredito Técnico:* \
Arquitetura event-sourced em Go/TypeScript com APIs gRPC/REST modernas, suporte nativo a OIDC, SAML, LDAP e trilha de auditoria imutável. \
#text(style: "italic", fill: rgb("#334155"))[*Veredito:* A escolha moderna para IAM com auditoria imutável e APIs de primeira linha para integração com agentes.]

*3. Requisitos de Infraestrutura & White-Label:* \
- RAM Mínima: `1 GB RAM` | CPU: `1 vCPU` | Docker: `zitadel/zitadel:latest`
- Customização UI: Logo e cores do console e telas de login configuráveis por organização. (Esforço: Baixo)

#v(10pt)

== 04. Authelia · SSO e 2FA Leve na Borda do Reverse Proxy (Persona: Leve)

#rect(fill: rgb("#f8fafc"), stroke: 0.5pt + rgb("#cbd5e1"), inset: 8pt, radius: 2pt, width: 100%)[
 #grid(
  columns: (1fr, 1fr, 1fr),
  gutter: 6pt,
  [*Substitui:* Google Endpoint Management (MFA na borda)],
  [*Economia:* #text(fill: rgb("#00875A"), weight: "bold")[R\$ 14.400/ano (50 usuários)]],
  [*Licença:* `Apache-2.0`]
 )
]

*1. O Que Faz & Como Funciona:* \
Adiciona autenticação de dois fatores e SSO leve na frente de aplicações web. Go com sessões em Redis e integração transparente via ForwardAuth do Traefik.

```bash
docker run -d -p 9091:9091 --name authelia authelia/authelia:latest
```

*2. Racional da Escolha & Veredito Técnico:* \
Contêiner minúsculo em Go que adiciona SSO e 2FA a qualquer aplicação protegida pelo Traefik, sem banco de dados pesado. \
#text(style: "italic", fill: rgb("#334155"))[*Veredito:* A escolha leve para adicionar MFA e SSO a toda a suíte sem overhead de um IAM completo.]

*3. Requisitos de Infraestrutura & White-Label:* \
- RAM Mínima: `256 MB RAM` | CPU: `0.5 vCPU` | Docker: `authelia/authelia:latest`
- Customização UI: Logo e texto do portal de login configuráveis em YAML. (Esforço: Baixo)

#v(10pt)

== 05. Casdoor · SSO All-in-One com UI Amigável e LDAP (Persona: Simples)

#rect(fill: rgb("#f8fafc"), stroke: 0.5pt + rgb("#cbd5e1"), inset: 8pt, radius: 2pt, width: 100%)[
 #grid(
  columns: (1fr, 1fr, 1fr),
  gutter: 6pt,
  [*Substitui:* Google Cloud Identity (SSO simples)],
  [*Economia:* #text(fill: rgb("#00875A"), weight: "bold")[R\$ 14.400/ano (50 usuários)]],
  [*Licença:* `Apache-2.0`]
 )
]

*1. O Que Faz & Como Funciona:* \
Fornece SSO, gestão de usuários e MFA com interface administrativa simples. Go com frontend React e armazenamento em MySQL/PostgreSQL.

```bash
docker run -d -p 8000:8000 --name casdoor casbin/casdoor:latest
```

*2. Racional da Escolha & Veredito Técnico:* \
Painel amigável para não-técnicos, suporte a OIDC/SAML/OAuth/LDAP e gestão de usuários com poucos cliques. \
#text(style: "italic", fill: rgb("#334155"))[*Veredito:* A escolha simples para SSO com interface amigável, ideal para gestores sem experiência em TI.]

*3. Requisitos de Infraestrutura & White-Label:* \
- RAM Mínima: `512 MB RAM` | CPU: `1 vCPU` | Docker: `casbin/casdoor:latest`
- Customização UI: Logo, tema e nome da organização configuráveis no painel administrativo. (Esforço: Baixo)

#v(10pt)


#pagebreak()
= Capítulo 6: Camada de Cola, SSO Federado & Blueprints n8n

== Arquitetura de Interconexão sem Silos de Dados
- *Autenticação Única:* Keycloak / Authentik (OpenID Connect / SAML) unificando o login dos colaboradores no Nextcloud Hub, CryptPad, ONLYOFFICE, Seafile, Zimbra e HedgeDoc, eliminando senhas isoladas por aplicação.
- *Barramento Assíncrono:* n8n Community Edition atuando como orquestrador central de eventos assíncronos (Usuário provisionado no Keycloak -> criação de caixa no Stalwart -> provisionamento de drive no Seafile -> notificação de boas-vindas no Nextcloud Talk).
- *Reverse Proxy & TLS:* Traefik Proxy v3 com terminação TLS automática via Let's Encrypt e roteamento por subdomínios corporativos (mail.empresa.com.br, docs.empresa.com.br, drive.empresa.com.br, sso.empresa.com.br, status.empresa.com.br).

== Fluxo de Integração Operacional
1. Provisionamento de Identidade: O administrador cria o colaborador no Keycloak/Authentik;
2. Criação de Caixa & Agenda: O webhook dispara no n8n que cria a conta de e-mail no Stalwart/Nextcloud e a agenda no CalDAV;
3. Provisionamento de Arquivos: O n8n cria a biblioteca do usuário no Seafile e a pasta de documentos no CryptPad;
4. Onboarding Colaborativo: O n8n envia mensagem de boas-vindas no Nextcloud Talk com links de acesso;
5. Armazenamento & Edição: O usuário edita documentos no ONLYOFFICE conectado ao Seafile e agenda reuniões no Nextcloud Calendar;
6. Governança & Backup: O n8n dispara o backup diário e o Uptime Kuma monitora a saúde de todos os serviços com alerta no chat corporativo.

#pagebreak()
= Capítulo 7: Manual de Engenharia de Infraestrutura & Deploy All-in-One

- *Segurança de Rede:* A infraestrutura opera sobre uma rede bridge isolada do Docker (`ecosystem\_net`). Apenas o reverse proxy Traefik expõe as portas públicas 80 (HTTP com redirect) e 443 (HTTPS TLS automático via ACME/Let's Encrypt). Todas as ferramentas (Nextcloud, CryptPad, ONLYOFFICE, Seafile, Keycloak, n8n, Stalwart e PostgreSQL) comunicam-se exclusivamente pela rede interna através de seus nomes DNS de serviço (ex: `http://nextcloud:80`, `postgres:5432`), eliminando vetores de ataque externos e exposição de portas desnecessárias.
- *Perfil de VPS Recomendado:* `8 vCPU Dedicated Cloud / 16 GB RAM ECC / 200-300 GB NVMe SSD / Link 1 Gbps / Ubuntu 24.04 LTS x86\_64`

#v(6pt)
== Especificação da VPS Ideal (e Por Que Desta Configuração)
#text(size: 8.5pt, style: "italic", fill: rgb("#334155"))[Garante estabilidade absoluta para os 11 contêineres rodando em simultâneo com isolamento de processos, prevenindo gargalos de I/O em banco de dados e eliminando o risco do OOM Killer durante picos de sincronização de arquivos e e-mails.]

#v(6pt)
#table(
 columns: (1.5fr, 0.7fr, 0.7fr, 2.8fr),
 fill: (x, y) => if y == 0 { rgb("#f1f5f9") } else { none },
 stroke: 0.5pt + rgb("#cbd5e1"),
 inset: 4pt,
 [*Serviço / Módulo*], [*vCPU*], [*RAM*], [*Motivo Técnico & Gargalo*],
 [Traefik Ingress & TLS], [`0.5 vCPU`], [`256 MB`], [Roteamento reativo de borda, compressão Brotli/Gzip e renovação automática de certificados SSL.],
[Keycloak SSO (OpenJDK JVM)], [`1.5 vCPU`], [`2.0 GB`], [Baseline da JVM Java para autenticação federada OIDC/SAML e criptografia de senhas Argon2.],
[Nextcloud Hub & Talk], [`2.0 vCPU`], [`4.0 GB`], [Processamento de e-mail, agenda, contatos e chamadas WebRTC do Talk para 50 colaboradores.],
[CryptPad & ONLYOFFICE], [`1.5 vCPU`], [`3.0 GB`], [Edição colaborativa de documentos em tempo real e conversão de formatos Office.],
[Seafile & Stalwart Mail], [`1.0 vCPU`], [`2.0 GB`], [Sincronização de blocos de arquivos e envio/recebimento de e-mails com filtros anti-spam.],
[n8n Orquestrador], [`0.5 vCPU`], [`1.0 GB`], [Execução assíncrona de fluxos de provisionamento e webhooks entre identidade e aplicativos.],
[Buffer de Picos / Anti-OOM], [`1.0 vCPU`], [`1.7 GB`], [Margem de folga do kernel Linux para backups diários pg\_dump e picos sazonais.],

)

#v(8pt)
== Manifesto docker-compose.yml de Produção
```yaml
version: '3.8'

networks:
 ecosystem_net:
 driver: bridge

volumes:
 postgres_data:
 redis_data:
 nextcloud_data:
 cryptpad_data:
 seafile_data:
 uptime_kuma_data:

# 1. Reverse Proxy & TLS Automático
services:
 traefik:
 image: traefik:v3.0
 command:
 - '--providers.docker=true'
 - '--entrypoints.websecure.address=:443'
 - '--certificatesresolvers.myresolver.acme.tlschallenge=true'
 - '--certificatesresolvers.myresolver.acme.email=admin@empresa.com.br'
 - '--certificatesresolvers.myresolver.acme.storage=/letsencrypt/acme.json'
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
 - 'traefik.http.routers.keycloak.rule=Host(`sso.empresa.com.br`)'
 - 'traefik.http.routers.keycloak.entrypoints=websecure'
 - 'traefik.http.routers.keycloak.tls.certresolver=myresolver'
 networks:
 - ecosystem_net

 # 3. Barramento de Eventos e Workflows
 n8n:
 image: n8nio/n8n:latest
 environment:
 - N8N_BASIC_AUTH_ACTIVE=true
 - N8N_HOST=n8n.empresa.com.br
 - WEBHOOK_URL=https://n8n.empresa.com.br
 labels:
 - 'traefik.enable=true'
 - 'traefik.http.routers.n8n.rule=Host(`n8n.empresa.com.br`)'
 - 'traefik.http.routers.n8n.entrypoints=websecure'
 - 'traefik.http.routers.n8n.tls.certresolver=myresolver'
 networks:
 - ecosystem_net

 # 4. Comunicação Unificada (Gmail/Calendar/Contacts/Meet)
 nextcloud:
 image: nextcloud:latest
 labels:
 - 'traefik.enable=true'
 - 'traefik.http.routers.nextcloud.rule=Host(`mail.empresa.com.br`)'
 - 'traefik.http.routers.nextcloud.entrypoints=websecure'
 - 'traefik.http.routers.nextcloud.tls.certresolver=myresolver'
 volumes:
 - nextcloud_data:/var/www/html
 networks:
 - ecosystem_net

 # 5. Suíte Office Criptografada (Drive/Docs/Sheets/Slides/Forms)
 cryptpad:
 image: cryptpad/cryptpad:latest
 labels:
 - 'traefik.enable=true'
 - 'traefik.http.routers.cryptpad.rule=Host(`docs.empresa.com.br`)'
 - 'traefik.http.routers.cryptpad.entrypoints=websecure'
 - 'traefik.http.routers.cryptpad.tls.certresolver=myresolver'
 volumes:
 - cryptpad_data:/cryptpad/data
 networks:
 - ecosystem_net

 # 6. Motor de Edição Colaborativa
 onlyoffice:
 image: onlyoffice/documentserver:latest
 labels:
 - 'traefik.enable=true'
 - 'traefik.http.routers.onlyoffice.rule=Host(`office.empresa.com.br`)'
 - 'traefik.http.routers.onlyoffice.entrypoints=websecure'
 - 'traefik.http.routers.onlyoffice.tls.certresolver=myresolver'
 networks:
 - ecosystem_net

 # 7. Armazenamento de Arquivos (Drive)
 seafile:
 image: seafileltd/seafile-mc:latest
 labels:
 - 'traefik.enable=true'
 - 'traefik.http.routers.seafile.rule=Host(`drive.empresa.com.br`)'
 - 'traefik.http.routers.seafile.entrypoints=websecure'
 - 'traefik.http.routers.seafile.tls.certresolver=myresolver'
 volumes:
 - seafile_data:/shared
 networks:
 - ecosystem_net

 # 8. Servidor de E-mail Moderno
 stalwart:
 image: stalwartlabs/stalwart:latest
 labels:
 - 'traefik.enable=true'
 - 'traefik.http.routers.stalwart.rule=Host(`smtp.empresa.com.br`)'
 - 'traefik.http.routers.stalwart.entrypoints=websecure'
 - 'traefik.http.routers.stalwart.tls.certresolver=myresolver'
 networks:
 - ecosystem_net

 # 9. Banco de Dados Relacional Consolidado
 postgres:
 image: postgres:16-alpine
 environment:
 - POSTGRES_USER=postgres
 - POSTGRES_PASSWORD=SegredoPostgres2026
 volumes:
 - postgres_data:/var/lib/postgresql/data
 networks:
 - ecosystem_net

 # 10. Cache & Sessões
 redis:
 image: redis:7-alpine
 volumes:
 - redis_data:/data
 networks:
 - ecosystem_net

 # 11. Monitoramento 24h
 uptime-kuma:
 image: louislam/uptime-kuma:1
 volumes:
 - uptime_kuma_data:/app/data
 labels:
 - 'traefik.enable=true'
 - 'traefik.http.routers.kuma.rule=Host(`status.empresa.com.br`)'
 - 'traefik.http.routers.kuma.entrypoints=websecure'
 - 'traefik.http.routers.kuma.tls.certresolver=myresolver'
 networks:
 - ecosystem_net
```

#pagebreak()
= Capítulo 8: Protocolos de Modularidade & Hot-Swap (Princípio do Lego)

- *Filosofia Desacoplada:* A arquitetura opera sob o princípio de 'Tomadas e Aparelhos Independentes'. Nenhuma ferramenta fica grudada ou dependente da outra com código travado. Imagine uma régua de tomadas na sua sala: a sua TV (Nextcloud) e o seu Arquivo (Seafile) funcionam perfeitamente mesmo se você desligar o Abajur (CryptPad). Se você quiser trocar o abajur por uma luminária moderna, basta tirar da tomada e plugar a nova. Nada na sua sala quebra.

== Hot-Swap em Produção
1. Suba a Nova Ferramenta em Paralelo: Inicie a nova solução em um endereço temporário (ex: `novo-docs.empresa.com.br`) mantendo a antiga funcionando;
2. Transfira a Conexão no n8n: No painel visual do n8n, mude o nó de disparo para apontar para a nova ferramenta;
3. Importe os Documentos: Faça o download da planilha de usuários da ferramenta antiga e importe na nova;
4. Mude o Endereço Oficial: Altere a rota para que `docs.empresa.com.br` aponte para a nova ferramenta;
5. Desligue a Antiga com Segurança: Pare o serviço antigo digitando `docker compose stop <servico\_antigo>`. Seus colaboradores nem notarão a troca!

#pagebreak()
= Capítulo 9: Roteiro Prático de Migração de Dados Históricos

== 1. Migração do Gmail para Nextcloud Mail / Stalwart
- *O que migrar:* Caixas de e-mail completas (pastas, mensagens, anexos), contatos e calendários dos 50 usuários.
- *Cuidados:* Mantenha o DKIM e o SPF do domínio apontando para o novo servidor antes de desligar o Gmail para evitar perda de entregabilidade.

== 2. Migração do Google Drive / Docs para Seafile / CryptPad / ONLYOFFICE
- *O que migrar:* Arquivos do Drive, documentos do Docs, planilhas do Sheets e apresentações do Slides.
- *Cuidados:* Verifique a fidelidade de formatação dos arquivos .docx/.xlsx após a conversão pelo ONLYOFFICE antes de descartar os originais.

== 3. Migração do Google Calendar / Contacts para Nextcloud
- *O que migrar:* Agendas compartilhadas, eventos recorrentes e catálogo corporativo de contatos.
- *Cuidados:* Confirme se eventos recorrentes e convites mantiveram os participantes corretos após a importação ICS.



#pagebreak()
= Capítulo 10: Governança Corporativa, Backup 3-2-1 & LGPD

- *Política 3-2-1:* A política de proteção de dados opera na regra de ouro 3-2-1: (3) cópias de dados em (2) tipos de mídias diferentes, com (1) cópia externa criptografada em nuvem fria (Wasabi / AWS S3 / armazenamento próprio).

== Script de Backup Diário Criptografado
```bash
#!/bin/bash
# Script de Backup Automatizado Soberano (PostgreSQL + Volumes + Mídias)
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
BACKUP_DIR="/opt/backups/$TIMESTAMP"
mkdir -p $BACKUP_DIR

# 1. Dump consistente de todos os bancos de dados (Keycloak, Nextcloud, Seafile, n8n)
docker exec postgres pg_dumpall -U postgres | gzip > $BACKUP_DIR/db_all_cluster.sql.gz

# 2. Compactação dos arquivos de mídia e anexos
tar -czf $BACKUP_DIR/media_storage.tar.gz -C /var/lib/docker/volumes nextcloud_data/_data seafile_data/_data cryptpad_data/_data

# 3. Criptografia AES-256 com senha segura
gpg --batch --yes --passphrase "SuaChaveMestreSegura2026" -c $BACKUP_DIR/db_all_cluster.sql.gz

# 4. Envio para Storage Seguro Externo (rclone / AWS S3)
rclone copy $BACKUP_DIR encrypted_remote:backups-workspace/

# 5. Retenção de 30 dias localmente
find /opt/backups -type d -mtime +30 -exec rm -rf {} +
```

#pagebreak()
= Capítulo 11: Cronograma de Implantação em 30 Dias & Monitoramento

== Semana 1 (Dias 1 a 7) · Infraestrutura & Instalação do Cluster
- *Atividades:* Contratação da VPS, configuração de DNS wildcard (wildcard.empresa.com.br), execução do docker-compose.yml e ativação dos certificados SSL automáticos via Traefik.
- *Marco de Entrega:* Todos os painéis acessíveis online com cadeado verde (HTTPS).

== Semana 2 (Dias 8 a 14) · Migração de Dados & Conexão de Identidade
- *Atividades:* Importação de caixas do Gmail via imapsync, migração do Drive para o Seafile e provisionamento de usuários no Keycloak com SSO.
- *Marco de Entrega:* Base histórica 100% carregada e colaboradores logando com uma única senha.

== Semana 3 (Dias 15 a 21) · Importação dos Blueprints n8n & Treinamento das Equipes
- *Atividades:* Importação dos templates de workflow no n8n, realização de testes de provisionamento (usuário -> caixa -> drive) e workshop de capacitação dos colaboradores.
- *Marco de Entrega:* Equipes operando com agilidade e fluxos automatizados aprovados.

== Semana 4 (Dias 22 a 30) · Virada de Chave Definitiva & Descomissionamento SaaS
- *Atividades:* Redirecionamento dos registros MX para o novo servidor, ativação da régua de backup oficial e cancelamento das faturas recorrentes do Google Workspace.
- *Marco de Entrega:* Autonomia digital plena e economia de R\$ 82.200/ano consolidada!


