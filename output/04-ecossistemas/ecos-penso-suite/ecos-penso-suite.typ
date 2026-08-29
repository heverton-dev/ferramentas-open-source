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
    [Suíte do Ecossistema Soberano · Penso Suite (Zimbra Collaboration, Penso Drive, Penso Antispam)],
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
  #text(size: 24pt, weight: "bold", fill: rgb("#0f172a"), font: "Liberation Serif")[Suíte Soberana de E-mail Corporativo, Armazenamento em Nuvem e Comunicação Unificada] \
  #v(6pt)
  #text(size: 12pt, fill: rgb("#334155"))[Desmantelamento Completo do Penso Suite (Zimbra, Penso Drive, Antispam e Chat Corporativo) com Arquitetura Soberana On-Premise/VPS] \
  #v(16pt)
  #line(length: 60%, stroke: 1pt + rgb("#cbd5e1"))
  #v(16pt)
  #text(size: 10pt, fill: rgb("#475569"))[
   *Macro-Ecossistema Alvo:* Penso Suite (Zimbra Collaboration, Penso Drive, Penso Antispam) \
   *Economia Anual Líquida:* #text(fill: rgb("#00875A"), weight: "bold")[R\$ 49.800/ano] \
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
Dossiê executivo e manual de engenharia para substituir 100% dos serviços de e-mail corporativo, groupware, compartilhamento de arquivos em nuvem e mensageria em equipe da Penso Tecnologia por uma infraestrutura open source soberana, auditável e de altíssimo desempenho.

A migração de suítes de software proprietário fechado para ecossistemas open source auto-hospedados em VPS representa a maior alavanca de eficiência operacional da década. Este livro-texto reúne as especificações de engenharia para desmantelar a suíte *Penso Suite (Zimbra Collaboration, Penso Drive, Penso Antispam)* com segurança jurídica, integridade de dados e autonomia digital irrestrita.

#pagebreak()

= Capítulo 1: Engenharia Financeira, TCO Global & Payback

#grid(
 columns: (1fr, 1fr),
 gutter: 10pt,
 rect(fill: rgb("#fef2f2"), stroke: 0.5pt + rgb("#fecaca"), inset: 10pt, radius: 2pt)[
  #text(size: 8pt, fill: rgb("#991b1b"), weight: "bold")[CUSTO SAAS ANUAL (Penso Suite (Zimbra Collaboration, Penso Drive, Penso Antispam))] \
  #text(size: 14pt, weight: "bold", fill: rgb("#dc2626"))[R\$ 54.000/ano]
 ],
 rect(fill: rgb("#f0fdf4"), stroke: 0.5pt + rgb("#bbf7d0"), inset: 10pt, radius: 2pt)[
  #text(size: 8pt, fill: rgb("#166534"), weight: "bold")[ECONOMIA LÍQUIDA ANUAL NO CAIXA] \
  #text(size: 14pt, weight: "bold", fill: rgb("#16a34a"))[R\$ 49.800/ano]
 ]
)

#v(10pt)
- *Custo VPS Própria:* R\$ 4.200/ano (Cluster Consolidado 8 vCPU / 16 GB RAM)
- *Retorno sobre Investimento (ROI / Payback):* 0.9 meses

#v(10pt)
== Desmembramento Contábil por Frente de Negócio

#table(
 columns: (1.5fr, 1.8fr, 1.2fr, 1.2fr, 0.9fr),
 fill: (x, y) => if y == 0 { rgb("#f1f5f9") } else { none },
 stroke: 0.5pt + rgb("#cbd5e1"),
 inset: 5pt,
 [*Grupo*], [*SaaS Alvo*], [*Custo SaaS*], [*Economia*], [*Margem*],
 [Pilar 01: E-mail Corporativo & Groupware], [Penso Mail Enterprise / Zimbra (150 caixas postais)], [R\$ 24.000/ano], [R\$ 22.320/ano], [93.0%],
[Pilar 02: Drive & Nuvem de Documentos], [Penso Drive Corporativo (2 TB de armazenamento)], [R\$ 18.000/ano], [R\$ 16.500/ano], [91.7%],
[Pilar 03: Chat Corporativo & Meet], [Penso Chat / Microsoft Teams / Zoom Pro], [R\$ 12.000/ano], [R\$ 10.980/ano], [91.5%],

)

#pagebreak()
= Capítulo 2: Infraestrutura Global, Dimensionamento da VPS & Provedores Validados

- *Perfil de Máquina Recomendado:* `8 vCPU / 16 GB RAM ECC / 160-240 GB NVMe`
- *Racional de Engenharia:* 

#v(6pt)
== Provedores de Nuvem Recomendados & Custo Mensal

#table(
 columns: (1.5fr, 1.2fr, 2.3fr),
 fill: (x, y) => if y == 0 { rgb("#f1f5f9") } else { none },
 stroke: 0.5pt + rgb("#cbd5e1"),
 inset: 5pt,
 [*Provedor de Nuvem*], [*Custo Mensal*], [*Vantagem Principal & SLA*],
 
)

#v(8pt)
== Alocação Técnica de Recursos por Serviço (vCPU & RAM)

#table(
 columns: (1.5fr, 0.7fr, 0.7fr, 2.8fr),
 fill: (x, y) => if y == 0 { rgb("#f1f5f9") } else { none },
 stroke: 0.5pt + rgb("#cbd5e1"),
 inset: 4pt,
 [*Serviço / Módulo*], [*vCPU*], [*RAM*], [*Motivo Técnico & Gargalo*],
 [Traefik + Keycloak SSO], [`2 vCPU`], [`2.5 GB RAM`], [Autenticação federada central e roteamento TLS para toda a suíte],
[Mailcow Cluster (Postfix + Dovecot + Rspamd + SOGo)], [`4 vCPU`], [`8.0 GB RAM`], [Processamento de filas SMTP, escaneamento de vírus ClamAV e IMAP],
[Nextcloud Hub + OnlyOffice Document Server], [`4 vCPU`], [`8.0 GB RAM`], [Edição de planilhas/documentos e sincronização de arquivos pesados],
[Mattermost Team Edition + PostgreSQL], [`2 vCPU`], [`4.0 GB RAM`], [Comunicação em tempo real, canais e persistência de histórico],
[Jitsi Meet (WebRTC + JVB)], [`2 vCPU`], [`3.5 GB RAM`], [Encaminhamento de fluxos de áudio e vídeo HD sem transcoding pesado],
[n8n Workflow Engine + Redis], [`1 vCPU`], [`1.5 GB RAM`], [Orquestração de eventos e rotinas assíncronas],
[Margem de Segurança & Cache do SO], [`1 vCPU`], [`4.5 GB RAM`], [Buffer de I/O em disco NVMe e prevenção contra picos de tráfego],

)

#pagebreak()
= Capítulo 3: Matriz Estratégica do Quinteto Soberano

#table(
 columns: (0.5fr, 1.3fr, 1.3fr, 1.8fr, 2.2fr, 1.3fr),
 fill: (x, y) => if y == 0 { rgb("#f1f5f9") } else { none },
 stroke: 0.5pt + rgb("#cbd5e1"),
 inset: 4pt,
 [*Nº*], [*Grupo*], [*Persona*], [*Ferramenta*], [*Substitui*], [*Economia*],
 [1], [Pilar 01], [Robusta], [*Mailcow: dockerized*], [Penso Mail Enterprise / Zimbra Network Edition], [R\$ 24.000/ano],
[2], [Pilar 01], [Completa], [*Mailu*], [Penso Mail Padrão], [R\$ 18.000/ano],
[3], [Pilar 01], [Moderna], [*Stalwart Mail Server*], [Penso Mail High Performance], [R\$ 18.000/ano],
[4], [Pilar 01], [Leve], [*Modoboa*], [Penso Mail Básico], [R\$ 14.000/ano],
[5], [Pilar 01], [Simples], [*Poste.io*], [Penso Mail Start], [R\$ 12.000/ano],
[6], [Pilar 02], [Robusta], [*Nextcloud Hub*], [Penso Drive / Google Workspace Drive / Dropbox Business], [R\$ 18.000/ano],
[7], [Pilar 02], [Robusta], [*Seafile*], [Penso Drive High Performance], [R\$ 15.000/ano],
[8], [Pilar 02], [Moderna], [*ownCloud Infinite Scale (oCIS)*], [Penso Drive Enterprise], [R\$ 15.000/ano],
[9], [Pilar 02], [Mais Segura e Privada], [*CryptPad*], [Penso Drive Seguro / Google Docs Privado], [R\$ 12.000/ano],
[10], [Pilar 02], [Leve], [*Filebrowser*], [Penso Drive Básico], [R\$ 9.600/ano],
[11], [Pilar 03], [Robusta], [*Mattermost Team Edition*], [Penso Chat / Slack / Microsoft Teams], [R\$ 12.000/ano],
[12], [Pilar 03], [Moderna], [*Matrix Synapse & Element*], [Penso Chat Seguro], [R\$ 10.000/ano],
[13], [Pilar 03], [Completa], [*Rocket.Chat*], [Penso Chat & Atendimento], [R\$ 10.000/ano],
[14], [Pilar 03], [Mais Focada em Produtividade Assíncrona], [*Zulip*], [Penso Chat / Slack], [R\$ 8.000/ano],
[15], [Pilar 03], [Simples], [*Jitsi Meet*], [Penso Meet / Zoom Pro / Google Meet], [R\$ 8.000/ano],

)


#pagebreak()
= Capítulo 4: Pilar 01 · Pilar 01: E-mail Corporativo, Groupware & Gateway Antispam

#text(size: 9pt, fill: rgb("#0284c7"), weight: "bold")[Alvo SaaS Substituído: Penso Mail / Zimbra Collaboration / Penso Antispam] \
#text(size: 9pt, fill: rgb("#00875A"), weight: "bold")[Subtotal de Economia do Grupo: R\$ 24.000/ano] \
#text(size: 9pt, style: "italic", fill: rgb("#475569"))[Servidores de correio eletrônico corporativo com suporte completo a protocolos IMAP, POP3, SMTP, ActiveSync (Exchange ActiveSync), calendários CalDAV, contatos CardDAV e proteção perimetral antispam com Rspamd, ClamAV e assinaturas DKIM/DMARC.]

#v(8pt)

== 01. Mailcow: dockerized · Suíte Moderna de E-mail Corporativo com Rspamd, SOGo Groupware e ActiveSync (Persona: Robusta)

#rect(fill: rgb("#f8fafc"), stroke: 0.5pt + rgb("#cbd5e1"), inset: 8pt, radius: 2pt, width: 100%)[
 #grid(
  columns: (1fr, 1fr, 1fr),
  gutter: 6pt,
  [*Substitui:* Penso Mail Enterprise / Zimbra Network Edition],
  [*Economia:* #text(fill: rgb("#00875A"), weight: "bold")[R\$ 24.000/ano]],
  [*Licença:* `GPL-3.0`]
 )
]

*1. O Que Faz & Como Funciona:* \
Gerencia caixas postais corporativas, filas SMTP, roteamento de domínios e proteção antispam com aprendizado bayesiano. Orquestração em contêineres Docker interligados por rede interna, utilizando Postfix para MTA, Dovecot para IMAP/LMTP, Nginx para proxy reverso e SOGo para webmail e groupware.

```bash
git clone https://github.com/mailcow/mailcow-dockerized && cd mailcow-dockerized && ./generate_config.sh && docker compose up -d
```

*2. Racional da Escolha & Veredito Técnico:* \
Solução conteinerizada líder mundial com arquitetura modular, atualizações automáticas via script, suporte nativo a 2FA/FIDO2, ActiveSync para dispositivos móveis e integração direta com Rspamd. \
#text(style: "italic", fill: rgb("#334155"))[*Veredito:* A escolha mais sólida e testada em batalha para substituição direta de servidores Zimbra corporativos com zero perda de recursos.]

*3. Requisitos de Infraestrutura & White-Label:* \
- RAM Mínima: `4 GB` | CPU: `2 vCPU` | Docker: `mailcow/postfix:latest`
- Customização UI: Customização de logos, cores institucionais e favicon diretamente via painel administrativo do Mailcow. (Esforço: Baixo)

#v(10pt)

== 02. Mailu · Servidor de E-mail Leve, Modular e Focado em Simplicidade Operacional (Persona: Completa)

#rect(fill: rgb("#f8fafc"), stroke: 0.5pt + rgb("#cbd5e1"), inset: 8pt, radius: 2pt, width: 100%)[
 #grid(
  columns: (1fr, 1fr, 1fr),
  gutter: 6pt,
  [*Substitui:* Penso Mail Padrão],
  [*Economia:* #text(fill: rgb("#00875A"), weight: "bold")[R\$ 18.000/ano]],
  [*Licença:* `MIT`]
 )
]

*1. O Que Faz & Como Funciona:* \
Entrega servidor de e-mail seguro com suporte a Webmail, antispam, antivírus e administração centralizada. Usa Postfix, Dovecot e Rspamd com gerador de docker-compose oficial para deploy personalizado.

```bash
curl -sSL https://setup.mailu.io -o setup.py && python3 setup.py
```

*2. Racional da Escolha & Veredito Técnico:* \
Arquitetura limpa sem componentes legados, com suporte nativo a Roundcube ou SnappyMail e excelente integração com clientes desktop Thunderbird e Outlook. \
#text(style: "italic", fill: rgb("#334155"))[*Veredito:* Excelente para equipes que buscam facilidade de manutenção e menor consumo de recursos de VPS.]

*3. Requisitos de Infraestrutura & White-Label:* \
- RAM Mínima: `2 GB` | CPU: `2 vCPU` | Docker: `mailu/admin:latest`
- Customização UI: Aplicação de CSS customizado e skins temáticas na interface do webmail. (Esforço: Médio)

#v(10pt)

== 03. Stalwart Mail Server · Servidor de Correio All-in-One de Próxima Geração em Rust (Persona: Moderna)

#rect(fill: rgb("#f8fafc"), stroke: 0.5pt + rgb("#cbd5e1"), inset: 8pt, radius: 2pt, width: 100%)[
 #grid(
  columns: (1fr, 1fr, 1fr),
  gutter: 6pt,
  [*Substitui:* Penso Mail High Performance],
  [*Economia:* #text(fill: rgb("#00875A"), weight: "bold")[R\$ 18.000/ano]],
  [*Licença:* `AGPL-3.0`]
 )
]

*1. O Que Faz & Como Funciona:* \
Unifica servidor SMTP, IMAP, JMAP, antispam e gerenciador de chaves criptográficas em um único serviço ultra-rápido. Arquitetura assíncrona em Rust com backend de armazenamento flexível (RocksDB, S3 ou SQL).

```bash
docker run -d --name stalwart -p 25:25 -p 993:993 -p 8080:8080 stalwartlabs/mail-server:latest
```

*2. Racional da Escolha & Veredito Técnico:* \
Desenvolvido em Rust com zero memory-leaks, suporte nativo ao protocolo moderno JMAP e altíssima velocidade de busca e indexação. \
#text(style: "italic", fill: rgb("#334155"))[*Veredito:* A solução de engenharia mais avançada tecnologicamente para servidores de e-mail corporativos da próxima década.]

*3. Requisitos de Infraestrutura & White-Label:* \
- RAM Mínima: `1 GB` | CPU: `1 vCPU` | Docker: `stalwartlabs/mail-server:latest`
- Customização UI: Temas nativos no painel de controle. (Esforço: Baixo)

#v(10pt)

== 04. Modoboa · Plataforma de E-mail Corporativo e Groupware Baseada em Python e Django (Persona: Leve)

#rect(fill: rgb("#f8fafc"), stroke: 0.5pt + rgb("#cbd5e1"), inset: 8pt, radius: 2pt, width: 100%)[
 #grid(
  columns: (1fr, 1fr, 1fr),
  gutter: 6pt,
  [*Substitui:* Penso Mail Básico],
  [*Economia:* #text(fill: rgb("#00875A"), weight: "bold")[R\$ 14.000/ano]],
  [*Licença:* `ISC`]
 )
]

*1. O Que Faz & Como Funciona:* \
Fornece interface web completa para gestão de correio, quarentena de spam e estatísticas de tráfego. Integra Postfix, Dovecot, Amavis/Rspamd e banco PostgreSQL através de uma API em Django.

```bash
git clone https://github.com/modoboa/modoboa-installer && cd modoboa-installer && python3 run.py <seu-dominio.com.br>
```

*2. Racional da Escolha & Veredito Técnico:* \
Código legível em Python/Django, instalador automatizado para Debian/Ubuntu e plugins para relatórios de tráfego de e-mail. \
#text(style: "italic", fill: rgb("#334155"))[*Veredito:* Perfeito para ambientes que necessitam de customização em Python e integração com portais corporativos existentes.]

*3. Requisitos de Infraestrutura & White-Label:* \
- RAM Mínima: `2 GB` | CPU: `1 vCPU` | Docker: `modoboa/modoboa:latest`
- Customização UI: Customização de templates HTML corporativos. (Esforço: Médio)

#v(10pt)

== 05. Poste.io · Servidor de E-mail Completo em Contêiner Único com Painel Administrativo Ágil (Persona: Simples)

#rect(fill: rgb("#f8fafc"), stroke: 0.5pt + rgb("#cbd5e1"), inset: 8pt, radius: 2pt, width: 100%)[
 #grid(
  columns: (1fr, 1fr, 1fr),
  gutter: 6pt,
  [*Substitui:* Penso Mail Start],
  [*Economia:* #text(fill: rgb("#00875A"), weight: "bold")[R\$ 12.000/ano]],
  [*Licença:* `GPL-2.0`]
 )
]

*1. O Que Faz & Como Funciona:* \
Provê serviço completo de correio eletrônico corporativo em um único contêiner autossuficiente. Combina Haraka/Postfix com Dovecot e painel em PHP/SQLite em imagem única otimizada.

```bash
docker run -d --name mail -p 25:25 -p 80:80 -p 443:443 -p 993:993 -v /opt/mail/data:/data analogic/poste.io
```

*2. Racional da Escolha & Veredito Técnico:* \
Empacotado em uma única imagem Docker, inclui Webmail Roundcube, antispam Rspamd, antivírus ClamAV e certificado Let's Encrypt automático em 1 comando. \
#text(style: "italic", fill: rgb("#334155"))[*Veredito:* A forma mais rápida e descomplicada de subir um servidor de e-mail funcional em menos de 5 minutos.]

*3. Requisitos de Infraestrutura & White-Label:* \
- RAM Mínima: `2 GB` | CPU: `1 vCPU` | Docker: `analogic/poste.io:latest`
- Customização UI: Troca de logotipo institucional no painel. (Esforço: Baixo)

#v(10pt)

#pagebreak()
= Capítulo 5: Pilar 02 · Pilar 02: Armazenamento em Nuvem, Drive Corporativo & Documentos

#text(size: 9pt, fill: rgb("#0284c7"), weight: "bold")[Alvo SaaS Substituído: Penso Drive / Google Drive / OneDrive] \
#text(size: 9pt, fill: rgb("#00875A"), weight: "bold")[Subtotal de Economia do Grupo: R\$ 18.000/ano] \
#text(size: 9pt, style: "italic", fill: rgb("#475569"))[Plataforma centralizada de arquivos corporativos com sincronização desktop/mobile, compartilhamento seguro de links com expiração e senha, edição colaborativa de planilhas e documentos em tempo real e controle de versionamento.]

#v(8pt)

== 06. Nextcloud Hub · A Plataforma de Produtividade e Armazenamento Soberana Líder Mundial (Persona: Robusta)

#rect(fill: rgb("#f8fafc"), stroke: 0.5pt + rgb("#cbd5e1"), inset: 8pt, radius: 2pt, width: 100%)[
 #grid(
  columns: (1fr, 1fr, 1fr),
  gutter: 6pt,
  [*Substitui:* Penso Drive / Google Workspace Drive / Dropbox Business],
  [*Economia:* #text(fill: rgb("#00875A"), weight: "bold")[R\$ 18.000/ano]],
  [*Licença:* `AGPL-3.0`]
 )
]

*1. O Que Faz & Como Funciona:* \
Armazena, versiona e compartilha arquivos corporativos com suporte a edição online de planilhas, apresentações e textos. Backend PHP/PostgreSQL com Redis para locking transacional e OnlyOffice Document Server integrado para edição colaborativa.

```bash
docker compose up -d nextcloud nextcloud-db redis onlyoffice
```

*2. Racional da Escolha & Veredito Técnico:* \
Padrão de ouro de governança de dados na Europa e no setor público brasileiro. Suporte a criptografia ponta a ponta, auditoria de acessos LGPD, clientes para Windows, Mac, Linux, Android e iOS. \
#text(style: "italic", fill: rgb("#334155"))[*Veredito:* A substituição definitiva para o Penso Drive e Google Drive, com soberania total de arquivos e suporte nativo a OnlyOffice.]

*3. Requisitos de Infraestrutura & White-Label:* \
- RAM Mínima: `4 GB` | CPU: `2 vCPU` | Docker: `nextcloud:apache`
- Customização UI: Aplicação de logotipo, cores da marca corporativa, background e slogan diretamente nas configurações de administração. (Esforço: Baixo)

#v(10pt)

== 07. Seafile · Sistema de Sincronização e Armazenamento de Arquivos de Alta Velocidade em C/Python (Persona: Robusta)

#rect(fill: rgb("#f8fafc"), stroke: 0.5pt + rgb("#cbd5e1"), inset: 8pt, radius: 2pt, width: 100%)[
 #grid(
  columns: (1fr, 1fr, 1fr),
  gutter: 6pt,
  [*Substitui:* Penso Drive High Performance],
  [*Economia:* #text(fill: rgb("#00875A"), weight: "bold")[R\$ 15.000/ano]],
  [*Licença:* `GPL-2.0`]
 )
]

*1. O Que Faz & Como Funciona:* \
Sincroniza bibliotecas de arquivos com alta velocidade, controle de versão infinito e drive virtual montado no Windows Explorer. Servidor C/C++ (seafile-server) com interface Seahub em Python/Django e banco MySQL/PostgreSQL.

```bash
docker compose up -d seafile seafile-mysql seafile-memcached
```

*2. Racional da Escolha & Veredito Técnico:* \
Escrito em linguagem C no núcleo de sincronização, possui algoritmo de deduplicação de blocos (delta sync) superior a soluções puramente PHP. \
#text(style: "italic", fill: rgb("#334155"))[*Veredito:* A escolha ideal para escritórios e agências que manipulam gigabytes diários de arquivos pesados com sincronização em tempo real.]

*3. Requisitos de Infraestrutura & White-Label:* \
- RAM Mínima: `2 GB` | CPU: `1 vCPU` | Docker: `seafileltd/seafile-mc:latest`
- Customização UI: Substituição de arquivos de logo e CSS corporativo em pasta de customização mapeada. (Esforço: Médio)

#v(10pt)

== 08. ownCloud Infinite Scale (oCIS) · Nuvem Corporativa Moderna em Go e Microserviços Cloud-Native (Persona: Moderna)

#rect(fill: rgb("#f8fafc"), stroke: 0.5pt + rgb("#cbd5e1"), inset: 8pt, radius: 2pt, width: 100%)[
 #grid(
  columns: (1fr, 1fr, 1fr),
  gutter: 6pt,
  [*Substitui:* Penso Drive Enterprise],
  [*Economia:* #text(fill: rgb("#00875A"), weight: "bold")[R\$ 15.000/ano]],
  [*Licença:* `Apache-2.0`]
 )
]

*1. O Que Faz & Como Funciona:* \
Gerencia arquivos em nuvem com arquitetura de microserviços e alta concorrência de usuários. Binário único em Go que orquestra serviços de metadados, armazenamento e API OIDC.

```bash
docker run -d --name ocis -p 9200:9200 -e OCIS_INSECURE=true owncloud/ocis:latest
```

*2. Racional da Escolha & Veredito Técnico:* \
Desenvolvido em Go (Golang) com frontend em Vue.js, inicialização instantânea em binário único e compatibilidade nativa com armazenamento S3. \
#text(style: "italic", fill: rgb("#334155"))[*Veredito:* Excelente para arquiteturas corporativas modernas que buscam eliminar a sobrecarga de bancos relacionais.]

*3. Requisitos de Infraestrutura & White-Label:* \
- RAM Mínima: `1 GB` | CPU: `1 vCPU` | Docker: `owncloud/ocis:latest`
- Customização UI: Customização de temas via arquivos JSON de configuração de branding. (Esforço: Baixo)

#v(10pt)

== 09. CryptPad · Suíte Colaborativa de Documentos com Criptografia Ponta a Ponta Zero-Knowledge (Persona: Mais Segura e Privada)

#rect(fill: rgb("#f8fafc"), stroke: 0.5pt + rgb("#cbd5e1"), inset: 8pt, radius: 2pt, width: 100%)[
 #grid(
  columns: (1fr, 1fr, 1fr),
  gutter: 6pt,
  [*Substitui:* Penso Drive Seguro / Google Docs Privado],
  [*Economia:* #text(fill: rgb("#00875A"), weight: "bold")[R\$ 12.000/ano]],
  [*Licença:* `AGPL-3.0`]
 )
]

*1. O Que Faz & Como Funciona:* \
Edição de documentos de texto, código, apresentações, enquetes e quadros brancos com proteção total de dados. Backend em Node.js leve que atua como relay criptográfico sem acesso às chaves descriptografadas.

```bash
docker run -d --name cryptpad -p 3000:3000 -p 3001:3001 cryptpad/cryptpad:latest
```

*2. Racional da Escolha & Veredito Técnico:* \
Nem mesmo o administrador da VPS consegue ler o conteúdo dos documentos: a chave criptográfica reside exclusivamente na sessão do usuário no navegador. \
#text(style: "italic", fill: rgb("#334155"))[*Veredito:* A solução definitiva para departamentos jurídicos, diretoria e compliance que exigem sigilo absoluto de documentos.]

*3. Requisitos de Infraestrutura & White-Label:* \
- RAM Mínima: `1 GB` | CPU: `1 vCPU` | Docker: `cryptpad/cryptpad:latest`
- Customização UI: Customização de logos e cores via config.js. (Esforço: Baixo)

#v(10pt)

== 10. Filebrowser · Gerenciador de Arquivos Web Ultra-Leve em Binário Único Go (Persona: Leve)

#rect(fill: rgb("#f8fafc"), stroke: 0.5pt + rgb("#cbd5e1"), inset: 8pt, radius: 2pt, width: 100%)[
 #grid(
  columns: (1fr, 1fr, 1fr),
  gutter: 6pt,
  [*Substitui:* Penso Drive Básico],
  [*Economia:* #text(fill: rgb("#00875A"), weight: "bold")[R\$ 9.600/ano]],
  [*Licença:* `Apache-2.0`]
 )
]

*1. O Que Faz & Como Funciona:* \
Provê interface web intuitiva para upload, download, pré-visualização de imagens/vídeos e gerenciamento de arquivos na VPS. Binário compilado em Go com banco SQLite e interface SPA em Vue.js.

```bash
docker run -d --name filebrowser -p 8080:80 -v /srv/files:/srv -v /opt/filebrowser/database.db:/database.db filebrowser/filebrowser:latest
```

*2. Racional da Escolha & Veredito Técnico:* \
Consome menos de 30 MB de RAM, suporta múltiplos usuários com permissões específicas de diretório e links de download públicos. \
#text(style: "italic", fill: rgb("#334155"))[*Veredito:* A solução mais leve existente para compartilhar e gerenciar arquivos corporativos com consumo quase nulo de hardware.]

*3. Requisitos de Infraestrutura & White-Label:* \
- RAM Mínima: `256 MB` | CPU: `0.5 vCPU` | Docker: `filebrowser/filebrowser:latest`
- Customização UI: Customização de título e cores via painel de configurações. (Esforço: Baixo)

#v(10pt)

#pagebreak()
= Capítulo 6: Pilar 03 · Pilar 03: Comunicação Unificada, Chat Corporativo & Videoconferência

#text(size: 9pt, fill: rgb("#0284c7"), weight: "bold")[Alvo SaaS Substituído: Penso Chat / Microsoft Teams / Slack / Zoom] \
#text(size: 9pt, fill: rgb("#00875A"), weight: "bold")[Subtotal de Economia do Grupo: R\$ 12.000/ano] \
#text(size: 9pt, style: "italic", fill: rgb("#475569"))[Ambiente centralizado de comunicação em equipe com canais públicos e privados, mensagens diretas, integração com bots, compartilhamento de tela e videoconferências em alta definição sem limite de tempo por reunião.]

#v(8pt)

== 11. Mattermost Team Edition · A Plataforma de Mensageria Segura e Operações para Empresas Líder de Mercado (Persona: Robusta)

#rect(fill: rgb("#f8fafc"), stroke: 0.5pt + rgb("#cbd5e1"), inset: 8pt, radius: 2pt, width: 100%)[
 #grid(
  columns: (1fr, 1fr, 1fr),
  gutter: 6pt,
  [*Substitui:* Penso Chat / Slack / Microsoft Teams],
  [*Economia:* #text(fill: rgb("#00875A"), weight: "bold")[R\$ 12.000/ano]],
  [*Licença:* `MIT`]
 )
]

*1. O Que Faz & Como Funciona:* \
Gerencia mensagens instantâneas, canais por projetos, integrações com sistemas legados e quadros de tarefas (Boards). Backend em Go de altíssima concorrência com PostgreSQL e interface moderna em React/Redux.

```bash
git clone https://github.com/mattermost/docker && cd docker && docker compose -f docker-compose.yml -f docker-compose.without-nginx.yml up -d
```

*2. Racional da Escolha & Veredito Técnico:* \
Substituição completa do Slack/Teams com aplicativos nativos para Windows, Mac, Linux, iOS e Android, suporte a LDAP/SAML/OIDC, webhooks ilimitados e total soberania de dados. \
#text(style: "italic", fill: rgb("#334155"))[*Veredito:* A plataforma de chat corporativo mais madura, confiável e adotada por grandes corporações globais.]

*3. Requisitos de Infraestrutura & White-Label:* \
- RAM Mínima: `2 GB` | CPU: `2 vCPU` | Docker: `mattermost/mattermost-team-edition:latest`
- Customização UI: Customização de logotipo, nome da empresa, tela de login e temas de cores diretamente pelo painel. (Esforço: Baixo)

#v(10pt)

== 12. Matrix Synapse & Element · Rede Aberta e Federada de Comunicação Segura com Criptografia Ponta a Ponta (Persona: Moderna)

#rect(fill: rgb("#f8fafc"), stroke: 0.5pt + rgb("#cbd5e1"), inset: 8pt, radius: 2pt, width: 100%)[
 #grid(
  columns: (1fr, 1fr, 1fr),
  gutter: 6pt,
  [*Substitui:* Penso Chat Seguro],
  [*Economia:* #text(fill: rgb("#00875A"), weight: "bold")[R\$ 10.000/ano]],
  [*Licença:* `Apache-2.0`]
 )
]

*1. O Que Faz & Como Funciona:* \
Provê servidor de mensageria federada com salas criptografadas, chamadas de áudio/vídeo e controle granular de chaves. Servidor Synapse (Python/Rust) conectado a banco PostgreSQL com cliente web/desktop Element.

```bash
docker compose up -d synapse synapse-db element-web
```

*2. Racional da Escolha & Veredito Técnico:* \
Padrão adotado por governos internacionais para soberania digital, com criptografia nativa Olm/Megolm e possibilidade de federar com outras filiais ou empresas parceiras. \
#text(style: "italic", fill: rgb("#334155"))[*Veredito:* A melhor escolha para organizações que exigem federação segura entre diferentes domínios e criptografia inquebrável.]

*3. Requisitos de Infraestrutura & White-Label:* \
- RAM Mínima: `2 GB` | CPU: `2 vCPU` | Docker: `matrixdotorg/synapse:latest`
- Customização UI: Customização de branding no config.json do Element Web. (Esforço: Médio)

#v(10pt)

== 13. Rocket.Chat · Hub de Comunicação Omnichannel e Mensageria Corporativa Segura (Persona: Completa)

#rect(fill: rgb("#f8fafc"), stroke: 0.5pt + rgb("#cbd5e1"), inset: 8pt, radius: 2pt, width: 100%)[
 #grid(
  columns: (1fr, 1fr, 1fr),
  gutter: 6pt,
  [*Substitui:* Penso Chat & Atendimento],
  [*Economia:* #text(fill: rgb("#00875A"), weight: "bold")[R\$ 10.000/ano]],
  [*Licença:* `MIT`]
 )
]

*1. O Que Faz & Como Funciona:* \
Centraliza conversas de equipes internas e chats de suporte ao cliente em tempo real. Backend em Node.js com banco de dados MongoDB e suporte a microserviços de alta disponibilidade.

```bash
docker compose up -d rocketchat rocketchat-mongodb
```

*2. Racional da Escolha & Veredito Técnico:* \
Combina comunicação de equipe interna com atendimento a clientes em um único painel, com suporte nativo a automações de atendimento. \
#text(style: "italic", fill: rgb("#334155"))[*Veredito:* Excelente para empresas que desejam unificar o chat entre funcionários e o atendimento web aos clientes no mesmo sistema.]

*3. Requisitos de Infraestrutura & White-Label:* \
- RAM Mínima: `2 GB` | CPU: `2 vCPU` | Docker: `registry.rocket.chat/rocketchat/rocket.chat:latest`
- Customização UI: Painel de personalização de marca nativo. (Esforço: Baixo)

#v(10pt)

== 14. Zulip · Plataforma de Chat em Equipe Organizada por Tópicos e Threads Assíncronas (Persona: Mais Focada em Produtividade Assíncrona)

#rect(fill: rgb("#f8fafc"), stroke: 0.5pt + rgb("#cbd5e1"), inset: 8pt, radius: 2pt, width: 100%)[
 #grid(
  columns: (1fr, 1fr, 1fr),
  gutter: 6pt,
  [*Substitui:* Penso Chat / Slack],
  [*Economia:* #text(fill: rgb("#00875A"), weight: "bold")[R\$ 8.000/ano]],
  [*Licença:* `Apache-2.0`]
 )
]

*1. O Que Faz & Como Funciona:* \
Combina a agilidade do chat em tempo real com a organização de um fórum corporativo estruturado. Backend Python/Django com Tornado para webhooks assíncronos e banco PostgreSQL.

```bash
docker compose up -d zulip zulip-db zulip-redis
```

*2. Racional da Escolha & Veredito Técnico:* \
Modelo exclusivo de tópicos dentro de streams que permite ler conversas importantes de forma organizada sem perder o contexto. \
#text(style: "italic", fill: rgb("#334155"))[*Veredito:* A melhor opção para empresas remotas e equipes de desenvolvimento que priorizam foco e comunicação assíncrona organizada.]

*3. Requisitos de Infraestrutura & White-Label:* \
- RAM Mínima: `2 GB` | CPU: `1 vCPU` | Docker: `zulip/docker-zulip:latest`
- Customização UI: Customização de logos e nomes de streams no painel corporativo. (Esforço: Baixo)

#v(10pt)

== 15. Jitsi Meet · Servidor de Videoconferência Criptografada HD sem Limite de Duração (Persona: Simples)

#rect(fill: rgb("#f8fafc"), stroke: 0.5pt + rgb("#cbd5e1"), inset: 8pt, radius: 2pt, width: 100%)[
 #grid(
  columns: (1fr, 1fr, 1fr),
  gutter: 6pt,
  [*Substitui:* Penso Meet / Zoom Pro / Google Meet],
  [*Economia:* #text(fill: rgb("#00875A"), weight: "bold")[R\$ 8.000/ano]],
  [*Licença:* `Apache-2.0`]
 )
]

*1. O Que Faz & Como Funciona:* \
Transmite áudio e vídeo de alta qualidade com salas protegidas por senha e sala de espera. Arquitetura WebRTC escalável com Jitsi Videobridge (JVB), Prosody XMPP e Jicofo em contêineres Docker.

```bash
git clone https://github.com/jitsi/docker-jitsi-meet && cd docker-jitsi-meet && cp env.example .env && ./gen-passwords.sh && docker compose up -d
```

*2. Racional da Escolha & Veredito Técnico:* \
Zero instalação para convidados (funciona direto no navegador WebRTC), sem limite de 40 minutos por reunião e com controle total das gravações. \
#text(style: "italic", fill: rgb("#334155"))[*Veredito:* A solução definitiva de reuniões virtuais corporativas, eliminando 100% dos custos recorrentes de licenças Zoom/Meet.]

*3. Requisitos de Infraestrutura & White-Label:* \
- RAM Mínima: `2 GB` | CPU: `2 vCPU` | Docker: `jitsi/web:latest`
- Customização UI: Substituição de marca d'água, logo de carregamento e interface via interface\_config.js. (Esforço: Baixo)

#v(10pt)


#pagebreak()
= Capítulo 7: Camada de Cola, SSO Federado & Blueprints n8n

== Arquitetura de Interconexão sem Silos de Dados
- *Autenticação Única:* Keycloak / Authentik OIDC unificado para login único no Webmail (Mailcow/SOGo), Nuvem (Nextcloud Hub) e Chat (Mattermost)
- *Barramento Assíncrono:* n8n para automação de onboarding de novos colaboradores, sincronização de contatos e alertas corporativos
- *Reverse Proxy & TLS:* Traefik v3 com certificados Let's Encrypt TLS automáticos, roteamento por subdomínios (mail., drive., chat., meet.) e proteção contra ataques DDoS

== Fluxo de Integração Operacional
O colaborador faz login único via OIDC no Keycloak e tem acesso imediato à sua caixa postal corporativa, ao seu drive na nuvem com documentos OnlyOffice e aos seus canais de chat no Mattermost. Novos funcionários cadastrados no RH são provisionados automaticamente em todos os sistemas via fluxo n8n.

#pagebreak()
= Capítulo 8: Manual de Engenharia de Infraestrutura & Deploy All-in-One

- *Segurança de Rede:* Cluster conteinerizado em rede Docker interna isolada (penso\_sovereign\_net), exposto publicamente apenas pelas portas 80/443 (HTTPS Traefik) e portas padrão de e-mail (25, 465, 587, 993) com firewall UFW ativo e Fail2ban protegendo contra força bruta.
- *Perfil de VPS Recomendado:* `8 vCPU / 16 GB RAM`

#v(6pt)
== Especificação da VPS Ideal (e Por Que Desta Configuração)
#text(size: 8.5pt, style: "italic", fill: rgb("#334155"))[]

#v(6pt)
#table(
 columns: (1.5fr, 0.7fr, 0.7fr, 2.8fr),
 fill: (x, y) => if y == 0 { rgb("#f1f5f9") } else { none },
 stroke: 0.5pt + rgb("#cbd5e1"),
 inset: 4pt,
 [*Serviço / Módulo*], [*vCPU*], [*RAM*], [*Motivo Técnico & Gargalo*],
 [Traefik + Keycloak SSO], [`2 vCPU`], [`2.5 GB RAM`], [Autenticação federada central e roteamento TLS para toda a suíte],
[Mailcow Cluster (Postfix + Dovecot + Rspamd + SOGo)], [`4 vCPU`], [`8.0 GB RAM`], [Processamento de filas SMTP, escaneamento de vírus ClamAV e IMAP],
[Nextcloud Hub + OnlyOffice Document Server], [`4 vCPU`], [`8.0 GB RAM`], [Edição de planilhas/documentos e sincronização de arquivos pesados],
[Mattermost Team Edition + PostgreSQL], [`2 vCPU`], [`4.0 GB RAM`], [Comunicação em tempo real, canais e persistência de histórico],
[Jitsi Meet (WebRTC + JVB)], [`2 vCPU`], [`3.5 GB RAM`], [Encaminhamento de fluxos de áudio e vídeo HD sem transcoding pesado],
[n8n Workflow Engine + Redis], [`1 vCPU`], [`1.5 GB RAM`], [Orquestração de eventos e rotinas assíncronas],
[Margem de Segurança & Cache do SO], [`1 vCPU`], [`4.5 GB RAM`], [Buffer de I/O em disco NVMe e prevenção contra picos de tráfego],

)

#v(8pt)
== Manifesto docker-compose.yml de Produção
```yaml
version: '3.8'

networks:
  penso_sovereign_net:
    name: penso_sovereign_net
    driver: bridge

services:
  traefik:
    image: traefik:v3.0
    container_name: traefik_gateway
    restart: always
    command:
      - '--api.dashboard=true'
      - '--providers.docker=true'
      - '--providers.docker.exposedbydefault=false'
      - '--entrypoints.web.address=:80'
      - '--entrypoints.websecure.address=:443'
      - '--certificatesresolvers.letsencrypt.acme.tlschallenge=true'
      - '--certificatesresolvers.letsencrypt.acme.email=admin@empresa.com.br'
      - '--certificatesresolvers.letsencrypt.acme.storage=/letsencrypt/acme.json'
    ports:
      - '80:80'
      - '443:443'
    volumes:
      - '/var/run/docker.sock:/var/run/docker.sock:ro'
      - './traefik_data/acme.json:/letsencrypt/acme.json'
    networks:
      - penso_sovereign_net

  keycloak:
    image: quay.io/keycloak/keycloak:latest
    container_name: keycloak_sso
    restart: always
    command: start --optimized
    environment:
      - KC_DB=postgres
      - KC_DB_URL=jdbc:postgresql://postgres_sso:5432/keycloak
      - KC_DB_USERNAME=keycloak
      - KC_DB_PASSWORD=${KEYCLOAK_DB_PASSWORD}
      - KC_HOSTNAME=auth.empresa.com.br
    labels:
      - 'traefik.enable=true'
      - 'traefik.http.routers.keycloak.rule=Host(`auth.empresa.com.br`)'
      - 'traefik.http.routers.keycloak.entrypoints=websecure'
      - 'traefik.http.routers.keycloak.tls.certresolver=letsencrypt'
    networks:
      - penso_sovereign_net

  nextcloud:
    image: nextcloud:apache
    container_name: nextcloud_drive
    restart: always
    environment:
      - POSTGRES_HOST=postgres_drive
      - POSTGRES_DB=nextcloud
      - POSTGRES_USER=nextcloud
      - POSTGRES_PASSWORD=${NEXTCLOUD_DB_PASSWORD}
      - REDIS_HOST=redis_drive
    volumes:
      - './nextcloud_data/html:/var/www/html'
      - './nextcloud_data/data:/var/www/html/data'
    labels:
      - 'traefik.enable=true'
      - 'traefik.http.routers.nextcloud.rule=Host(`drive.empresa.com.br`)'
      - 'traefik.http.routers.nextcloud.entrypoints=websecure'
      - 'traefik.http.routers.nextcloud.tls.certresolver=letsencrypt'
    networks:
      - penso_sovereign_net

  mattermost:
    image: mattermost/mattermost-team-edition:latest
    container_name: mattermost_chat
    restart: always
    environment:
      - MM_SQLSETTINGS_DATASOURCE=postgres://mmuser:${MM_DB_PASSWORD}@postgres_chat:5432/mattermost?sslmode=disable
    volumes:
      - './mattermost_data/config:/mattermost/config'
      - './mattermost_data/data:/mattermost/data'
    labels:
      - 'traefik.enable=true'
      - 'traefik.http.routers.mattermost.rule=Host(`chat.empresa.com.br`)'
      - 'traefik.http.routers.mattermost.entrypoints=websecure'
      - 'traefik.http.routers.mattermost.tls.certresolver=letsencrypt'
    networks:
      - penso_sovereign_net
```

#pagebreak()
= Capítulo 9: Protocolos de Modularidade & Hot-Swap (Princípio do Lego)

- *Filosofia Desacoplada:* Princípio do Lego: cada serviço (Mailcow, Nextcloud, Mattermost, Jitsi) roda em seu próprio contêiner desacoplado com volumes persistentes. Se a empresa decidir trocar o Mattermost pelo Zulip ou o Nextcloud pelo Seafile, a substituição é realizada sem interromper o serviço de e-mail ou o proxy central.

== Hot-Swap em Produção
1. Suba o novo serviço em paralelo em uma porta/subdomínio temporário;
2. Sincronize os dados históricos do serviço antigo;
3. Teste o login via Keycloak;
4. Altere a label do Traefik apontando o subdomínio principal para o novo contêiner;
5. Desligue o contêiner legado após 48 horas de validação.

#pagebreak()
= Capítulo 10: Roteiro Prático de Migração de Dados Históricos

== E-mail Corporativo (Zimbra / Penso Mail -> Mailcow)
- *O que migrar:* Todas as caixas postais, histórico de mensagens, pastas personalizadas, regras de encaminhamento e contatos.
- *Cuidados:* Mantenha o servidor Zimbra antigo acessível por IP durante 72 horas pós-virada para garantir que nenhuma mensagem em trânsito seja perdida.

== Arquivos & Documentos (Penso Drive -> Nextcloud Hub)
- *O que migrar:* Pastas de departamentos, arquivos corporativos, permissões e documentos OnlyOffice.
- *Cuidados:* Valide as permissões de proprietário (chown -R www-data:www-data) no diretório de dados antes da varredura.



#pagebreak()
= Capítulo 11: Governança Corporativa, Backup 3-2-1 & LGPD

- *Política 3-2-1:* Regra 3-2-1 estrita: 3 cópias dos dados (produção local, backup criptografado em disco secundário e snapshot offsite em storage S3 externo como Wasabi ou Backblaze B2).

== Script de Backup Diário Criptografado
```bash
#!/bin/bash
set -e
DATA=$(date +%Y%m%d_%H%M%S)
DEST=/var/backups/sovereign_suite
mkdir -p $DEST

# 1. Backup Banco de Dados PostgreSQL (Keycloak, Nextcloud, Mattermost)
docker exec postgres_sso pg_dumpall -U keycloak | gzip > $DEST/db_sso_$DATA.sql.gz
docker exec postgres_drive pg_dumpall -U nextcloud | gzip > $DEST/db_drive_$DATA.sql.gz
docker exec postgres_chat pg_dumpall -U mmuser | gzip > $DEST/db_chat_$DATA.sql.gz

# 2. Backup Mailcow (Utilitário Nativo de Backup)
cd /opt/mailcow-dockerized && ./helper-scripts/backup_and_restore.sh backup all --delete-days 7

# 3. Criptografia com OpenSSL (AES-256-CBC)
tar -czf - -C $DEST . | openssl enc -aes-256-cbc -salt -pbkdf2 -pass pass:${BACKUP_PASSWORD} -out /var/backups_encrypted/penso_suite_backup_$DATA.tar.enc

# 4. Envio Seguro para Storage S3 Offsite (Wasabi / AWS)
rclone copy /var/backups_encrypted/ s3-backup:empresa-backups-soberanos/

echo 'Backup 3-2-1 executado e criptografado com sucesso!'
```

#pagebreak()
= Capítulo 12: Cronograma de Implantação em 30 Dias & Monitoramento

== Semana 01 · Provisionamento de VPS & Identidade Unificada (Keycloak SSO)
- *Atividades:* Contratação da VPS dedicada, endurecimento do sistema operacional (SSH seguro, UFW, Fail2ban), deploy do Traefik com TLS e configuração do Keycloak com os usuários corporativos.
- *Marco de Entrega:* Painel de autenticação online em auth.empresa.com.br com certificados SSL válidos.

== Semana 02 · Deploy do Servidor de E-mail Soberano & Testes de Entregabilidade
- *Atividades:* Deploy do Mailcow, configuração de chaves DKIM, SPF e DMARC, teste de reputação IP (Mail-Tester 10/10) e sincronização piloto de 10 caixas postais via Syncjob.
- *Marco de Entrega:* Servidor de correio enviando e recebendo mensagens com reputação máxima.

== Semana 03 · Deploy do Drive Corporativo (Nextcloud) & Chat (Mattermost)
- *Atividades:* Deploy do Nextcloud Hub com OnlyOffice, migração das pastas departamentais do Penso Drive, subida do Mattermost com canais de equipe e integração ao Keycloak.
- *Marco de Entrega:* Nuvem de arquivos e chat corporativo operacionais para testes internos com a equipe de TI.

== Semana 04 · Virada de Chave (DNS Cutover), Treinamento & Desativação do SaaS
- *Atividades:* Alteração dos registros MX definitivos no DNS, execução da sincronização final de e-mails, distribuição dos clientes desktop/mobile e aplicação da Trilha de Aprendizado em 5 Aulas para a equipe.
- *Marco de Entrega:* Operação 100% migrada para a infraestrutura própria e cancelamento das faturas do Penso Suite.


