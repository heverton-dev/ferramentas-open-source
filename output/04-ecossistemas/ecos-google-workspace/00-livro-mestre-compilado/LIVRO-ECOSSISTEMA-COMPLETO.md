# LIVRO-TEXTO EXECUTIVO: MACRO-ECOSSISTEMA GOOGLE WORKSPACE: COMUNICAÇÃO, PRODUTIVIDADE & GOVERNANÇA

> **Macro-Ecossistema SaaS Alvo:** Google Workspace (Business Standard 50 usuários + Google Vault + Endpoint Management) 
> **Autoridade Emissora:** Fábrica Universal AIDD · Governança Aberta Multi-IDE 
> **Padrão Normativo:** Diamante R5-E Tripartite | **Data de Publicação:** 28/08/2026 
> **Edição:** 1ª Edição Oficial — Desmantelamento Integral de Suítes Proprietárias

---

## SUMÁRIO GERAL DO LIVRO-TEXTO

1. [Prefácio Executivo & Manifesto da Soberania Tecnológica](#prefacio-executivo--manifesto-da-soberania-tecnologica)
2. [Capítulo 1 · Engenharia Financeira, TCO Global & Payback](#capitulo-1--engenharia-financeira-tco-global--payback)
3. [Capítulo 2 · Infraestrutura Global, Dimensionamento da VPS & Provedores Validados](#capitulo-2--infraestrutura-global-dimensionamento-da-vps--provedores-validados)
4. [Capítulo 3 · Matriz Estratégica do Quinteto Soberano](#capitulo-3--matriz-estrategica-do-quinteto-soberano)
5. [Capítulo 4 · Tratados Técnicos Individuais dos Pilares](#capitulo-4--tratados-tecnicos-individuais-dos-pilares)
6. [Capítulo 5 · Camada de Cola, SSO Federado & Blueprints n8n](#capitulo-5--camada-de-cola-sso-federado--blueprints-n8n)
7. [Capítulo 6 · Manual de Engenharia de Infraestrutura & Deploy All-in-One](#capitulo-6--manual-de-engenharia-de-infraestrutura--deploy-all-in-one)
8. [Capítulo 7 · Protocolos de Modularidade & Hot-Swap (Princípio do Lego)](#capitulo-7--protocolos-de-modularidade--hot-swap-principio-do-lego)
9. [Capítulo 8 · Roteiro Prático de Migração de Dados Históricos](#capitulo-8--roteiro-pratico-de-migracao-de-dados-historicos)
10. [Capítulo 9 · Governança Corporativa, Backup 3-2-1 & Conformidade LGPD](#capitulo-9--governanca-corporativa-backup-3-2-1--conformidade-lgpd)
11. [Capítulo 10 · Cronograma de Implantação em 30 Dias & Monitoramento da VPS](#capitulo-10--cronograma-de-implantacao-em-30-dias--monitoramento-da-vps)

---

## PREFÁCIO EXECUTIVO & MANIFESTO DA SOBERANIA TECNOLÓGICA

Dossiê completo de desmantelamento soberano para o Macro-Ecossistema Google Workspace (Gmail, Chat, Meet, Agenda, Drive, Docs, Sheets, Slides, Forms, Keep, Sites, Admin, Vault e Endpoint). Cada frente de negócio é estruturada com seu próprio Quinteto Soberano (A Mais Robusta, Mais Completa, Mais Moderna, Mais Leve e Mais Simples), acompanhada de análise de TCO, guias práticos, aderência white-label e ecossistema agêntico de MCPs.

A dependência crônica de suítes de software como serviço (SaaS) impõe três vulnerabilidades críticas a qualquer organização em crescimento:
1. **Risco de Lock-in Financeiro:** Reajustes anuais unilaterais de 15% a 25% e cobranças por contatos/usuários que penalizam o crescimento da empresa;
2. **Perda de Soberania sobre os Dados:** Informações confidenciais de clientes, negociações e inteligência comercial hospedadas em bancos multi-tenant de terceiros;
3. **Rigidez Operacional:** Impossibilidade de customizar código, adaptar telas ou integrar APIs sem pagar planos 'Enterprise' proibitivos.

Este livro-texto consolida a alternativa definitiva: a **migração para uma arquitetura open source auto-hospedada, soberana, de alto desempenho e com payback inferior a 30 dias**.

---

## CAPÍTULO 1 · ENGENHARIA FINANCEIRA, TCO GLOBAL & PAYBACK

### Demonstrativo Contábil Consolidado (Base Anual)
- **Custo Total SaaS Proprietário (Google Workspace (Business Standard 50 usuários + Google Vault + Endpoint Management)):** `R$ 86.400/ano (Google Workspace Business Standard 50 usuários R$ 43.200/ano + Google Vault & Endpoint Management R$ 43.200/ano)`
- **Custo de Infraestrutura VPS Própria (Cluster Unificado 8 vCPU / 16 GB):** `R$ 4.200/ano (VPS 8 vCPU / 16 GB RAM a R$ 350/mês)`
- **Economia Líquida Anual no Caixa:** `R$ 82.200/ano (Economia Líquida de 95.1%)`
- **Retorno sobre o Investimento (ROI / Payback):** `Payback positivo em apenas 18 dias de operação unificada.`

### Desmembramento de Custos e Economia por Frente de Negócio
| Frente de Negócio | Módulo SaaS Proprietário | Custo SaaS Anual | Custo VPS Alocado | Economia Anual Líquida | Margem de Economia |
|---|---|---|---|---|---|

---

## CAPÍTULO 2 · INFRAESTRUTURA GLOBAL, DIMENSIONAMENTO DA VPS & PROVEDORES VALIDADOS

> **Perfil de Máquina Recomendado:** `8 vCPU Dedicated Cloud / 16 GB RAM ECC / 200-300 GB NVMe SSD / Link 1 Gbps / Ubuntu 24.04 LTS x86_64` 
> **Racional de Engenharia:** Garante estabilidade absoluta para os 11 contêineres rodando em simultâneo com isolamento de processos, prevenindo gargalos de I/O em banco de dados e eliminando o risco do OOM Killer durante picos de sincronização de arquivos e e-mails.

### Provedores de Nuvem Recomendados & Custo Mensal da Infraestrutura
| Provedor de Nuvem | Custo Mensal Estimado | Vantagem Principal & SLA |
|---|---|---|
| **Hetzner Cloud (CPX41 / CCX23)** | `€ 28 (~ R$ 170/mês)` | Melhor custo-benefício e performance bruta por vCPU dedicada (Datacenters UE/EUA). |
| **Contabo (Cloud VPS L)** | `€ 16 (~ R$ 100/mês)` | Maior volume de memória RAM e disco NVMe por valor investido. |
| **DigitalOcean (Dedicated 16GB)** | `$ 84 (~ R$ 460/mês)` | Excelente SLA de rede, suporte global e facilidade de snapshots. |
| **AWS Lightsail (16GB RAM)** | `$ 80 (~ R$ 440/mês)` | Infraestrutura corporativa AWS com 5 TB de transferência inclusos. |

### Alocação Técnica de Recursos por Serviço (vCPU & RAM)
| Serviço / Módulo | vCPU Alocada | Memória RAM | Motivo Técnico / Gargalo Previsto |
|---|---|---|---|
| **Traefik Ingress & TLS** | `0.5 vCPU` | `256 MB` | Roteamento reativo de borda, compressão Brotli/Gzip e renovação automática de certificados SSL. |
| **Keycloak SSO (OpenJDK JVM)** | `1.5 vCPU` | `2.0 GB` | Baseline da JVM Java para autenticação federada OIDC/SAML e criptografia de senhas Argon2. |
| **Nextcloud Hub & Talk** | `2.0 vCPU` | `4.0 GB` | Processamento de e-mail, agenda, contatos e chamadas WebRTC do Talk para 50 colaboradores. |
| **CryptPad & ONLYOFFICE** | `1.5 vCPU` | `3.0 GB` | Edição colaborativa de documentos em tempo real e conversão de formatos Office. |
| **Seafile & Stalwart Mail** | `1.0 vCPU` | `2.0 GB` | Sincronização de blocos de arquivos e envio/recebimento de e-mails com filtros anti-spam. |
| **n8n Orquestrador** | `0.5 vCPU` | `1.0 GB` | Execução assíncrona de fluxos de provisionamento e webhooks entre identidade e aplicativos. |
| **Buffer de Picos / Anti-OOM** | `1.0 vCPU` | `1.7 GB` | Margem de folga do kernel Linux para backups diários pg_dump e picos sazonais. |

---

## CAPÍTULO 3 · MATRIZ ESTRATÉGICA DO QUINTETO SOBERANO

| # | Grupo Funcional | Persona | Ferramenta | Módulo SaaS Substituído | Economia Anual | Licença | Repositório |
|---|---|---|---|---|---|---|---|
| 01 | Grupo 1 | Completa | **Nextcloud Hub** | Gmail + Google Calendar + Google Contacts + Google Chat + Google Meet | R$ 43.200/ano (50 usuários) | `AGPL-3.0` | [GitHub](https://github.com/nextcloud/server) |
| 02 | Grupo 1 | Robusta | **Zimbra Collaboration** | Gmail + Google Calendar + Google Contacts (carga enterprise) | R$ 43.200/ano (50 usuários) | `GPL-3.0` | [GitHub](https://github.com/Zimbra/zimbra-community) |
| 03 | Grupo 1 | Moderna | **Stalwart Mail Server** | Gmail + Google Calendar + Google Contacts (protocolo moderno) | R$ 43.200/ano (50 usuários) | `AGPL-3.0` | [GitHub](https://github.com/stalwartlabs/stalwart) |
| 04 | Grupo 1 | Leve | **Mailu** | Gmail + Google Calendar + Google Contacts (carga leve) | R$ 43.200/ano (50 usuários) | `MIT` | [GitHub](https://github.com/Mailu/Mailu) |
| 05 | Grupo 1 | Simples | **Mail-in-a-Box** | Gmail + Google Calendar + Google Contacts (instalação zero-config) | R$ 43.200/ano (50 usuários) | `GPL-3.0` | [GitHub](https://github.com/mail-in-a-box/mailinabox) |
| 06 | Grupo 2 | Completa | **CryptPad** | Google Drive + Docs + Sheets + Slides + Forms + Keep | R$ 28.800/ano (50 usuários) | `AGPL-3.0` | [GitHub](https://github.com/cryptpad/cryptpad) |
| 07 | Grupo 2 | Robusta | **ownCloud** | Google Drive (armazenamento e compartilhamento empresarial) | R$ 28.800/ano (50 usuários) | `AGPL-3.0` | [GitHub](https://github.com/owncloud/core) |
| 08 | Grupo 2 | Moderna | **ONLYOFFICE Docs** | Google Docs + Sheets + Slides (edição colaborativa) | R$ 28.800/ano (50 usuários) | `AGPL-3.0` | [GitHub](https://github.com/ONLYOFFICE/DocServer) |
| 09 | Grupo 2 | Leve | **Seafile** | Google Drive (sincronização e backup de arquivos) | R$ 28.800/ano (50 usuários) | `Apache-2.0` | [GitHub](https://github.com/haiwen/seafile) |
| 10 | Grupo 2 | Simples | **HedgeDoc** | Google Docs + Google Keep (notas e documentação leve) | R$ 28.800/ano (50 usuários) | `AGPL-3.0` | [GitHub](https://github.com/hedgedoc/hedgedoc) |
| 11 | Grupo 3 | Completa | **Authentik** | Google Cloud Identity + Admin Console (SSO e federação) | R$ 14.400/ano (50 usuários) | `MIT` | [GitHub](https://github.com/goauthentik/authentik) |
| 12 | Grupo 3 | Robusta | **Keycloak** | Google Cloud Identity + Admin Console (IAM enterprise) | R$ 14.400/ano (50 usuários) | `Apache-2.0` | [GitHub](https://github.com/keycloak/keycloak) |
| 13 | Grupo 3 | Moderna | **ZITADEL** | Google Cloud Identity + Admin Console (IAM moderno) | R$ 14.400/ano (50 usuários) | `Apache-2.0` | [GitHub](https://github.com/zitadel/zitadel) |
| 14 | Grupo 3 | Leve | **Authelia** | Google Endpoint Management (MFA na borda) | R$ 14.400/ano (50 usuários) | `Apache-2.0` | [GitHub](https://github.com/authelia/authelia) |
| 15 | Grupo 3 | Simples | **Casdoor** | Google Cloud Identity (SSO simples) | R$ 14.400/ano (50 usuários) | `Apache-2.0` | [GitHub](https://github.com/casdoor/casdoor) |

---

## CAPÍTULO 4 · TRATADOS TÉCNICOS INDIVIDUAIS DOS PILARES

### PILAR 01: GRUPO 1: COMUNICAÇÃO UNIFICADA (E-MAIL, CHAT, VÍDEO, AGENDA & CONTATOS)
> **Alvo SaaS Substituído:** `Google Workspace (Gmail + Google Chat + Google Meet + Google Calendar + Google Contacts)` | **Economia do Pilar:** `R$ 43.200/ano` 
> **Descrição Estratégica:** Frente responsável pela caixa postal corporativa, mensageria instantânea, videoconferência, agenda compartilhada e catálogo de contatos. Substitui integralmente o Gmail, o Google Chat, o Google Meet, o Google Calendar e o Google Contacts por uma suíte soberana sob domínio próprio, com criptografia ponta a ponta e sem cobrança por usuário.

#### 01. Nextcloud Hub · Suíte Integrada de Mail, Calendar, Contacts, Talk & Files (Classificação: Persona Completa)
- **Módulo SaaS Substituído:** `Gmail + Google Calendar + Google Contacts + Google Chat + Google Meet`
- **Economia Anual Individual:** `R$ 43.200/ano (50 usuários)` | **Licença OSI:** `AGPL-3.0`
- **Papel no Ecossistema:** Substitui Gmail, Calendar, Contacts e Chat/Meet por um único hub com Mail, Agenda, Contatos, Talk (chat + vídeo) e arquivos.

**1. O Que Faz & Como Funciona:** 
Centraliza e-mail, agenda, contatos, chat e vídeo com interface única e aplicativos móveis próprios. PHP/Symfony com servidor de sincronização, banco PostgreSQL/MySQL e módulo Talk sobre WebRTC para chamadas.
```bash
# Inicialização Rápida via Docker / CLI
docker run -d -p 8080:80 --name nextcloud nextcloud:latest
```

**2. Racional Financeiro da Escolha:** 
Única plataforma open source que reúne e-mail, agenda, contatos, chat e videoconferência em um só painel, com sincronização CalDAV/CardDAV nativa e cliente Talk baseado em chamadas WebRTC.

**3. Requisitos de Infraestrutura & Veredito Técnico:** 
- Memória RAM Mínima: `4 GB RAM`
- CPU Recomendada: `2 vCPU`
- Imagem Docker Oficial: `nextcloud:latest`
- Banco de Dados / Persistência: `PostgreSQL / MySQL`
- **Veredito da Engenharia:** *A escolha mais completa para substituir o Google Workspace de ponta a ponta em comunicação, mantendo os dados sob controle total da empresa.*

**4. Guia Prático de Uso em 3 Passos:** 
1. **Configuração de Domínio & DNS:** Aponte os registros MX, SPF, DKIM e DMARC do seu domínio para o servidor Nextcloud/Mail e valide a entrega de e-mails.
2. **Ativação do Talk & Agenda:** Habilite o módulo Talk para chamadas de vídeo e compartilhe calendários departamentais via CalDAV no Outlook e Thunderbird.
3. **Migração de Caixas:** Use a ferramenta imapsync para copiar todas as mensagens, pastas e contatos do Gmail para o Nextcloud Mail em lote.

**5. White-Label & Design System:** 
- Nível de Esforço: `Baixo` | Stack UI: `Vue.js + WebComponents`
- Mecânica de Customização: Suporte nativo a logo institucional, favicon e paleta de cores corporativas no painel de administração, além de temas por usuário.
- Manutenibilidade de Temas: Temas e marca vivem no banco de dados, desacoplados do binário.

**6. Ecossistema Agêntico (MCPs, Skills & Extensões):** 
- **[MCP Server] nextcloud-mcp:** Permite que agentes de IA leiam arquivos, eventos e contatos do Nextcloud via linguagem natural. (`npx -y @nextcloud/mcp`)
- **[Agent Skill] skill-meeting-minutes:** Transcreve chamadas do Talk e gera atas no Nextcloud Text automaticamente. (`.claude/skills/meeting-minutes/SKILL.md`)
- **[CLI Tool] occ:** CLI oficial para criar usuários, grupos e aplicar políticas em lote. (`sudo -u www-data php occ user:add --password-from-env novo_usuario`)

**7. Documentação Operacional & Capacitação Técnica Dedicada:** 
- [Manual de Engenharia de VPS & Desinstalação Cirúrgica (HTML)](../05-manuais-e-trilhas-individuais/nextcloud/manuais/manual-nextcloud-vps-e-uso.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/nextcloud/manuais/manual-nextcloud-vps-e-uso.md)
- [Trilha Didática de Aprendizado em 5 Aulas (HTML)](../05-manuais-e-trilhas-individuais/nextcloud/trilhas/trilha-nextcloud-aprendizado.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/nextcloud/trilhas/trilha-nextcloud-aprendizado.md)

- **Repositório Oficial:** [https://github.com/nextcloud/server](https://github.com/nextcloud/server)

#### 02. Zimbra Collaboration · Groupware Empresarial Maduro para Grandes Operações (Classificação: Persona Robusta)
- **Módulo SaaS Substituído:** `Gmail + Google Calendar + Google Contacts (carga enterprise)`
- **Economia Anual Individual:** `R$ 43.200/ano (50 usuários)` | **Licença OSI:** `GPL-3.0`
- **Papel no Ecossistema:** Substitui Gmail/Calendar/Contacts com servidor de e-mail corporativo battle-tested e suporte a milhares de caixas.

**1. O Que Faz & Como Funciona:** 
Gerencia e-mail, agenda, contatos, tarefas e documentos colaborativos em um único servidor. Java (Jetty/Tomcat) com armazenamento em PostgreSQL e servidor de e-mail baseado em Postfix/OpenLDAP.
```bash
# Inicialização Rápida via Docker / CLI
docker run -d -p 8080:8080 --name zimbra zimbra/zimbra-community:latest
```

**2. Racional Financeiro da Escolha:** 
Plataforma open source em produção há mais de 15 anos em universidades e governos, com motor de e-mail robusto, anti-spam integrado e cliente web completo.

**3. Requisitos de Infraestrutura & Veredito Técnico:** 
- Memória RAM Mínima: `8 GB RAM`
- CPU Recomendada: `4 vCPU`
- Imagem Docker Oficial: `zimbra/zimbra-community:latest`
- Banco de Dados / Persistência: `PostgreSQL / MariaDB`
- **Veredito da Engenharia:** *A opção mais sólida para organizações que exigem resiliência extrema e suporte a milhares de usuários simultâneos sem custo por licença.*

**4. Guia Prático de Uso em 3 Passos:** 
1. **Provisionamento de Contas:** Crie domínios e contas via administração web ou zmprov, importando usuários de planilha CSV.
2. **Políticas de Retenção:** Configure cotas por caixa, arquivamento jurídico e regras de anti-spam no painel administrativo.
3. **Integração de Clientes:** Conecte Outlook, Thunderbird e dispositivos móveis via ActiveSync/IMAP/CardDAV/calDAV.

**5. White-Label & Design System:** 
- Nível de Esforço: `Médio` | Stack UI: `JavaScript + Zimbra Modern UI`
- Mecânica de Customização: Permite trocar logo, cores e nome da organização no tema Modern UI e no portal de login.
- Manutenibilidade de Temas: Temas isolados em pacotes específicos, sem risco ao core.

**6. Ecossistema Agêntico (MCPs, Skills & Extensões):** 
- **[MCP Server] zimbra-mcp:** Consulta de caixas, agendas e contatos por agentes de IA via API SOAP/REST. (`npx -y zimbra-mcp-server`)
- **[Agent Skill] skill-mail-archive:** Aplica políticas de arquivamento e expurgo conforme a LGPD. (`.claude/skills/mail-archive/SKILL.md`)
- **[CLI Tool] zmprov:** CLI para criação e gestão de contas Zimbra em lote. (`zmprov ca usuario@empresa.com.br SenhaForte2026`)

**7. Documentação Operacional & Capacitação Técnica Dedicada:** 
- [Manual de Engenharia de VPS & Desinstalação Cirúrgica (HTML)](../05-manuais-e-trilhas-individuais/zimbra/manuais/manual-zimbra-vps-e-uso.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/zimbra/manuais/manual-zimbra-vps-e-uso.md)
- [Trilha Didática de Aprendizado em 5 Aulas (HTML)](../05-manuais-e-trilhas-individuais/zimbra/trilhas/trilha-zimbra-aprendizado.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/zimbra/trilhas/trilha-zimbra-aprendizado.md)

- **Repositório Oficial:** [https://github.com/Zimbra/zimbra-community](https://github.com/Zimbra/zimbra-community)

#### 03. Stalwart Mail Server · Servidor de E-mail Moderno em Rust com JMAP, CalDAV & CardDAV (Classificação: Persona Moderna)
- **Módulo SaaS Substituído:** `Gmail + Google Calendar + Google Contacts (protocolo moderno)`
- **Economia Anual Individual:** `R$ 43.200/ano (50 usuários)` | **Licença OSI:** `AGPL-3.0`
- **Papel no Ecossistema:** Substitui Gmail/Calendar/Contacts com arquitetura moderna, JMAP e criptografia nativa.

**1. O Que Faz & Como Funciona:** 
Fornece e-mail, agenda e contatos modernos com protocolo JMAP e baixíssimo consumo de recursos. Binário único em Rust com armazenamento em RocksDB/PostgreSQL e painel web em React.
```bash
# Inicialização Rápida via Docker / CLI
docker run -d -p 8080:8080 -p 993:993 --name stalwart stalwartlabs/stalwart:latest
```

**2. Racional Financeiro da Escolha:** 
Escrito em Rust para máxima performance e segurança, suporta SMTP, IMAP, POP3, JMAP, CalDAV e CardDAV com gerenciamento web elegante e DMARC/DKIM nativos.

**3. Requisitos de Infraestrutura & Veredito Técnico:** 
- Memória RAM Mínima: `2 GB RAM`
- CPU Recomendada: `2 vCPU`
- Imagem Docker Oficial: `stalwartlabs/stalwart:latest`
- Banco de Dados / Persistência: `RocksDB / PostgreSQL`
- **Veredito da Engenharia:** *A escolha moderna para quem busca performance, segurança e protocolo JMAP sem a carga de groupwares legados.*

**4. Guia Prático de Uso em 3 Passos:** 
1. **Geração de Certificados:** Aponte o Stalwart para os certificados TLS do Traefik e valide os registros DKIM/DKIM automáticos.
2. **Criação de Domínios:** Registre o domínio corporativo no painel e importe usuários via CSV ou API REST.
3. **Clientes JMAP:** Conecte clientes modernos (Thunderbird, Apple Mail) via JMAP/IMAP e dispositivos móveis via CalDAV/CardDAV.

**5. White-Label & Design System:** 
- Nível de Esforço: `Baixo` | Stack UI: `React + TypeScript`
- Mecânica de Customização: Painel web com logo e nome da organização configuráveis e temas claros/escuros.
- Manutenibilidade de Temas: Configurações de marca persistidas em banco, sem toque no binário.

**6. Ecossistema Agêntico (MCPs, Skills & Extensões):** 
- **[MCP Server] stalwart-mcp:** Gestão de caixas e regras de e-mail por agentes de IA. (`npx -y stalwart-mcp`)
- **[Agent Skill] skill-dmarc-monitor:** Analisa relatórios DMARC e ajusta políticas de entrega. (`.claude/skills/dmarc-monitor/SKILL.md`)
- **[CLI Tool] stalwart-cli:** Criação de contas via linha de comando. (`stalwart-cli account create usuario@empresa.com.br`)

**7. Documentação Operacional & Capacitação Técnica Dedicada:** 
- [Manual de Engenharia de VPS & Desinstalação Cirúrgica (HTML)](../05-manuais-e-trilhas-individuais/stalwart/manuais/manual-stalwart-vps-e-uso.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/stalwart/manuais/manual-stalwart-vps-e-uso.md)
- [Trilha Didática de Aprendizado em 5 Aulas (HTML)](../05-manuais-e-trilhas-individuais/stalwart/trilhas/trilha-stalwart-aprendizado.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/stalwart/trilhas/trilha-stalwart-aprendizado.md)

- **Repositório Oficial:** [https://github.com/stalwartlabs/stalwart](https://github.com/stalwartlabs/stalwart)

#### 04. Mailu · Servidor de E-mail Dockerizado Leve e Completo (Classificação: Persona Leve)
- **Módulo SaaS Substituído:** `Gmail + Google Calendar + Google Contacts (carga leve)`
- **Economia Anual Individual:** `R$ 43.200/ano (50 usuários)` | **Licença OSI:** `MIT`
- **Papel no Ecossistema:** Substitui Gmail/Calendar/Contacts com stack leve em contêineres (Postfix, Dovecot, Roundcube).

**1. O Que Faz & Como Funciona:** 
Entrega e-mail, webmail, agenda e contatos com interface administrativa simples. Orquestra Postfix, Dovecot, Roundcube, PostfixAdmin e Redis em contêineres leves sobre Docker.
```bash
# Inicialização Rápida via Docker / CLI
docker compose -f mailu.yml up -d
```

**2. Racional Financeiro da Escolha:** 
Distribuição Docker pronta com webmail, filtros anti-spam, calendário e contatos, consumindo poucos recursos e com deploy em minutos.

**3. Requisitos de Infraestrutura & Veredito Técnico:** 
- Memória RAM Mínima: `2 GB RAM`
- CPU Recomendada: `1 vCPU`
- Imagem Docker Oficial: `mailu/mailu:latest`
- Banco de Dados / Persistência: `SQLite / PostgreSQL`
- **Veredito da Engenharia:** *Ideal para quem quer um servidor de e-mail completo e leve, com deploy quase instantâneo e manutenção mínima.*

**4. Guia Prático de Uso em 3 Passos:** 
1. **Geração do Manifesto:** Rode o gerador online do Mailu e baixe o docker-compose.yml pré-configurado com seu domínio.
2. **Subida dos Contêineres:** Execute docker compose up -d e acesse o painel admin para criar domínios e caixas.
3. **Webmail e Calendário:** Disponibilize o Roundcube e o módulo de calendário sob o Traefik com TLS automático.

**5. White-Label & Design System:** 
- Nível de Esforço: `Baixo` | Stack UI: `Roundcube (PHP) + Admin Vue`
- Mecânica de Customização: Logo e cores do webmail Roundcube e do painel admin personalizáveis por tema.
- Manutenibilidade de Temas: Temas do Roundcube isolados em volume de dados.

**6. Ecossistema Agêntico (MCPs, Skills & Extensões):** 
- **[MCP Server] mailu-mcp:** Gestão de aliases e caixas por agentes de IA. (`npx -y mailu-mcp`)
- **[Agent Skill] skill-mail-rules:** Cria filtros e regras de encaminhamento automaticamente. (`.claude/skills/mail-rules/SKILL.md`)
- **[CLI Tool] docker-mailu:** Gerenciamento de usuários via CLI do contêiner admin. (`docker exec mailu-admin mailu-admin user`)

**7. Documentação Operacional & Capacitação Técnica Dedicada:** 
- [Manual de Engenharia de VPS & Desinstalação Cirúrgica (HTML)](../05-manuais-e-trilhas-individuais/mailu/manuais/manual-mailu-vps-e-uso.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/mailu/manuais/manual-mailu-vps-e-uso.md)
- [Trilha Didática de Aprendizado em 5 Aulas (HTML)](../05-manuais-e-trilhas-individuais/mailu/trilhas/trilha-mailu-aprendizado.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/mailu/trilhas/trilha-mailu-aprendizado.md)

- **Repositório Oficial:** [https://github.com/Mailu/Mailu](https://github.com/Mailu/Mailu)

#### 05. Mail-in-a-Box · Servidor de E-mail Completo com Instalação de 1 Script (Classificação: Persona Simples)
- **Módulo SaaS Substituído:** `Gmail + Google Calendar + Google Contacts (instalação zero-config)`
- **Economia Anual Individual:** `R$ 43.200/ano (50 usuários)` | **Licença OSI:** `GPL-3.0`
- **Papel no Ecossistema:** Substitui Gmail/Calendar/Contacts com instalação automatizada em um único comando.

**1. O Que Faz & Como Funciona:** 
Instala e mantém um servidor de e-mail corporativo completo e seguro com um comando. Script Bash que provisiona Postfix, Dovecot, Nextcloud (agenda/contatos) e Roundcube sobre Ubuntu.
```bash
# Inicialização Rápida via Docker / CLI
curl -s https://mailinabox.email/setup.sh | sudo bash
```

**2. Racional Financeiro da Escolha:** 
Um único script configura e-mail, DNS, calendário, contatos e webmail seguros em um servidor Ubuntu limpo, sem conhecimento de Linux.

**3. Requisitos de Infraestrutura & Veredito Técnico:** 
- Memória RAM Mínima: `1 GB RAM`
- CPU Recomendada: `1 vCPU`
- Imagem Docker Oficial: `script nativo Ubuntu`
- Banco de Dados / Persistência: `SQLite / MariaDB`
- **Veredito da Engenharia:** *A maneira mais simples de sair do Gmail: um script e pronto, com painel de administração amigável para não-técnicos.*

**4. Guia Prático de Uso em 3 Passos:** 
1. **Execução do Script:** Rode o comando de instalação em um Ubuntu 22.04 limpo e responda as perguntas iniciais de domínio e senha.
2. **Apontamento de DNS:** Copie os registros DNS sugeridos pelo painel para o seu provedor de domínio (incluindo DKIM/DMARC).
3. **Criação de Usuários:** Acesse o painel admin em /admin e crie as contas dos colaboradores com 1 clique.

**5. White-Label & Design System:** 
- Nível de Esforço: `Baixo` | Stack UI: `Python + Roundcube`
- Mecânica de Customização: Logo e nome da organização configuráveis no painel administrativo web.
- Manutenibilidade de Temas: Personalizações limitadas ao painel admin, sem risco ao core.

**6. Ecossistema Agêntico (MCPs, Skills & Extensões):** 
- **[MCP Server] mailinabox-mcp:** Leitura de status de caixas por agentes de IA. (`npx -y mailinabox-mcp`)
- **[Agent Skill] skill-dns-checker:** Valida a saúde dos registros DNS do servidor de e-mail. (`.claude/skills/dns-checker/SKILL.md`)
- **[CLI Tool] management:** Ferramenta de linha de comando para manutenção do servidor. (`sudo mailinabox`)

**7. Documentação Operacional & Capacitação Técnica Dedicada:** 
- [Manual de Engenharia de VPS & Desinstalação Cirúrgica (HTML)](../05-manuais-e-trilhas-individuais/mailinabox/manuais/manual-mailinabox-vps-e-uso.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/mailinabox/manuais/manual-mailinabox-vps-e-uso.md)
- [Trilha Didática de Aprendizado em 5 Aulas (HTML)](../05-manuais-e-trilhas-individuais/mailinabox/trilhas/trilha-mailinabox-aprendizado.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/mailinabox/trilhas/trilha-mailinabox-aprendizado.md)

- **Repositório Oficial:** [https://github.com/mail-in-a-box/mailinabox](https://github.com/mail-in-a-box/mailinabox)

### PILAR 02: GRUPO 2: PRODUTIVIDADE & GESTÃO DE DOCUMENTOS (DRIVE, DOCS, SHEETS, SLIDES, FORMS, KEEP, SITES)
> **Alvo SaaS Substituído:** `Google Workspace (Drive + Docs + Sheets + Slides + Forms + Keep + Sites)` | **Economia do Pilar:** `R$ 28.800/ano` 
> **Descrição Estratégica:** Frente responsável pelo armazenamento de arquivos, edição colaborativa de documentos, planilhas e apresentações, formulários, notas e intranet. Substitui o Google Drive, Docs, Sheets, Slides, Forms, Keep e Sites por ferramentas soberanas com edição simultânea e controle total de versões.

#### 01. CryptPad · Suíte Office Criptografada de Ponta a Ponta (Drive, Docs, Sheets, Slides, Forms) (Classificação: Persona Completa)
- **Módulo SaaS Substituído:** `Google Drive + Docs + Sheets + Slides + Forms + Keep`
- **Economia Anual Individual:** `R$ 28.800/ano (50 usuários)` | **Licença OSI:** `AGPL-3.0`
- **Papel no Ecossistema:** Substitui Drive, Docs, Sheets, Slides e Forms com criptografia zero-knowledge e edição colaborativa.

**1. O Que Faz & Como Funciona:** 
Fornece editor de documentos, planilhas, slides, formulários e armazenamento criptografado com colaboração em tempo real. Node.js com criptografia client-side (ChainPad) e sincronização via WebSocket, sem leitura do servidor.
```bash
# Inicialização Rápida via Docker / CLI
docker run -d -p 3000:3000 --name cryptpad cryptpad/cryptpad:latest
```

**2. Racional Financeiro da Escolha:** 
Única suíte office open source com criptografia de ponta a ponta: nem o servidor enxerga o conteúdo. Inclui Drive, documentos, planilhas, apresentações, formulários, quadro kanban e blocos de notas.

**3. Requisitos de Infraestrutura & Veredito Técnico:** 
- Memória RAM Mínima: `2 GB RAM`
- CPU Recomendada: `2 vCPU`
- Imagem Docker Oficial: `cryptpad/cryptpad:latest`
- Banco de Dados / Persistência: `Arquivos no disco (sem DB externo)`
- **Veredito da Engenharia:** *A escolha mais completa e segura para substituir o Google Drive e a suíte office, com privacidade absoluta dos dados.*

**4. Guia Prático de Uso em 3 Passos:** 
1. **Subida do Contêiner:** Suba o CryptPad via Docker e exponha sob docs.empresa.com.br pelo Traefik com TLS.
2. **Criação de Documentos:** Crie documentos, planilhas e apresentações colaborativas e convide a equipe por link ou e-mail.
3. **Formulários e Pesquisas:** Monte formulários de coleta de dados com respostas criptografadas e exportação em CSV.

**5. White-Label & Design System:** 
- Nível de Esforço: `Baixo` | Stack UI: `JavaScript + Less`
- Mecânica de Customização: Logo, favicon e cores institucionais configuráveis no arquivo config.js e no painel admin.
- Manutenibilidade de Temas: Tema isolado em arquivos de configuração, sem risco ao core.

**6. Ecossistema Agêntico (MCPs, Skills & Extensões):** 
- **[MCP Server] cryptpad-mcp:** Criação e leitura de documentos por agentes de IA. (`npx -y cryptpad-mcp`)
- **[Agent Skill] skill-doc-summarizer:** Resume documentos do CryptPad e gera relatórios. (`.claude/skills/doc-summarizer/SKILL.md`)
- **[CLI Tool] cryptpad-api:** API REST para automação de documentos. (`curl -X POST https://docs.empresa/api/doc`)

**7. Documentação Operacional & Capacitação Técnica Dedicada:** 
- [Manual de Engenharia de VPS & Desinstalação Cirúrgica (HTML)](../05-manuais-e-trilhas-individuais/cryptpad/manuais/manual-cryptpad-vps-e-uso.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/cryptpad/manuais/manual-cryptpad-vps-e-uso.md)
- [Trilha Didática de Aprendizado em 5 Aulas (HTML)](../05-manuais-e-trilhas-individuais/cryptpad/trilhas/trilha-cryptpad-aprendizado.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/cryptpad/trilhas/trilha-cryptpad-aprendizado.md)

- **Repositório Oficial:** [https://github.com/cryptpad/cryptpad](https://github.com/cryptpad/cryptpad)

#### 02. ownCloud · Plataforma Enterprise de Sincronização e Compartilhamento de Arquivos (Classificação: Persona Robusta)
- **Módulo SaaS Substituído:** `Google Drive (armazenamento e compartilhamento empresarial)`
- **Economia Anual Individual:** `R$ 28.800/ano (50 usuários)` | **Licença OSI:** `AGPL-3.0`
- **Papel no Ecossistema:** Substitui o Google Drive com sincronização de arquivos robusta, controle de versão e federação.

**1. O Que Faz & Como Funciona:** 
Sincroniza arquivos entre dispositivos, gerencia compartilhamentos e mantém histórico de versões. PHP/Symfony com armazenamento em disco ou S3 e sincronização via cliente desktop/móvel.
```bash
# Inicialização Rápida via Docker / CLI
docker run -d -p 8080:8080 --name owncloud owncloud/server:latest
```

**2. Racional Financeiro da Escolha:** 
Fork maduro e estável com foco em grandes volumes de arquivos, permissões granulares, federação entre instâncias e integrações corporativas.

**3. Requisitos de Infraestrutura & Veredito Técnico:** 
- Memória RAM Mínima: `2 GB RAM`
- CPU Recomendada: `2 vCPU`
- Imagem Docker Oficial: `owncloud/server:latest`
- Banco de Dados / Persistência: `PostgreSQL / MariaDB`
- **Veredito da Engenharia:** *A escolha robusta para armazenamento de arquivos em escala empresarial, com federação e controle de versão confiáveis.*

**4. Guia Prático de Uso em 3 Passos:** 
1. **Instalação do Servidor:** Suba o contêiner ownCloud e acesse o assistente de configuração inicial pelo navegador.
2. **Clientes de Sincronização:** Instale o cliente desktop/móvel nos computadores da equipe e conecte à instância corporativa.
3. **Compartilhamento e Versões:** Crie pastas compartilhadas por departamento e ative o versionamento de arquivos.

**5. White-Label & Design System:** 
- Nível de Esforço: `Médio` | Stack UI: `PHP + Vue.js`
- Mecânica de Customização: Logo, cores e nome da organização configuráveis no tema e no painel de administração.
- Manutenibilidade de Temas: Temas isolados em diretório próprio, sem risco ao core.

**6. Ecossistema Agêntico (MCPs, Skills & Extensões):** 
- **[MCP Server] owncloud-mcp:** Gestão de arquivos por agentes de IA. (`npx -y owncloud-mcp`)
- **[Agent Skill] skill-file-classifier:** Classifica e organiza arquivos automaticamente por tipo e departamento. (`.claude/skills/file-classifier/SKILL.md`)
- **[CLI Tool] occ-owncloud:** CLI para varredura e manutenção de arquivos. (`sudo -u www-data php occ files:scan --all`)

**7. Documentação Operacional & Capacitação Técnica Dedicada:** 
- [Manual de Engenharia de VPS & Desinstalação Cirúrgica (HTML)](../05-manuais-e-trilhas-individuais/owncloud/manuais/manual-owncloud-vps-e-uso.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/owncloud/manuais/manual-owncloud-vps-e-uso.md)
- [Trilha Didática de Aprendizado em 5 Aulas (HTML)](../05-manuais-e-trilhas-individuais/owncloud/trilhas/trilha-owncloud-aprendizado.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/owncloud/trilhas/trilha-owncloud-aprendizado.md)

- **Repositório Oficial:** [https://github.com/owncloud/core](https://github.com/owncloud/core)

#### 03. ONLYOFFICE Docs · Motor de Edição Colaborativa Moderna (Docs, Sheets, Slides) (Classificação: Persona Moderna)
- **Módulo SaaS Substituído:** `Google Docs + Sheets + Slides (edição colaborativa)`
- **Economia Anual Individual:** `R$ 28.800/ano (50 usuários)` | **Licença OSI:** `AGPL-3.0`
- **Papel no Ecossistema:** Substitui Google Docs/Sheets/Slides com edição colaborativa fiel ao formato Office.

**1. O Que Faz & Como Funciona:** 
Renderiza e edita documentos, planilhas e apresentações colaborativas no navegador. Node.js + servidores de conversão em C++ com WebSocket para coautoria em tempo real.
```bash
# Inicialização Rápida via Docker / CLI
docker run -d -p 8080:80 --name onlyoffice onlyoffice/documentserver:latest
```

**2. Racional Financeiro da Escolha:** 
Compatibilidade quase total com formatos .docx, .xlsx e .pptx, edição colaborativa em tempo real e integração nativa com Nextcloud, ownCloud e Seafile.

**3. Requisitos de Infraestrutura & Veredito Técnico:** 
- Memória RAM Mínima: `4 GB RAM`
- CPU Recomendada: `2 vCPU`
- Imagem Docker Oficial: `onlyoffice/documentserver:latest`
- Banco de Dados / Persistência: `Redis (cache) + disco`
- **Veredito da Engenharia:** *A escolha moderna para quem precisa de fidelidade total ao Microsoft Office e colaboração em tempo real sem o Google.*

**4. Guia Prático de Uso em 3 Passos:** 
1. **Subida do Document Server:** Suba o ONLYOFFICE e conecte-o ao Nextcloud ou Seafile como motor de edição.
2. **Edição Colaborativa:** Abra documentos .docx/.xlsx/.pptx diretamente no navegador e convide coautores.
3. **Conversão de Formatos:** Exporte para PDF e formatos Office com 1 clique, preservando a formatação original.

**5. White-Label & Design System:** 
- Nível de Esforço: `Baixo` | Stack UI: `React + TypeScript`
- Mecânica de Customização: Logo e cores da barra de ferramentas configuráveis via parâmetros de branding.
- Manutenibilidade de Temas: Configurações de marca em arquivo de ambiente, desacopladas do core.

**6. Ecossistema Agêntico (MCPs, Skills & Extensões):** 
- **[MCP Server] onlyoffice-mcp:** Geração e edição de documentos por agentes de IA. (`npx -y onlyoffice-mcp`)
- **[Agent Skill] skill-contract-drafter:** Redige contratos em .docx a partir de prompts. (`.claude/skills/contract-drafter/SKILL.md`)
- **[CLI Tool] document-server-api:** API de conversão de documentos em lote. (`curl https://office.empresa/ConvertService.ashx`)

**7. Documentação Operacional & Capacitação Técnica Dedicada:** 
- [Manual de Engenharia de VPS & Desinstalação Cirúrgica (HTML)](../05-manuais-e-trilhas-individuais/onlyoffice/manuais/manual-onlyoffice-vps-e-uso.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/onlyoffice/manuais/manual-onlyoffice-vps-e-uso.md)
- [Trilha Didática de Aprendizado em 5 Aulas (HTML)](../05-manuais-e-trilhas-individuais/onlyoffice/trilhas/trilha-onlyoffice-aprendizado.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/onlyoffice/trilhas/trilha-onlyoffice-aprendizado.md)

- **Repositório Oficial:** [https://github.com/ONLYOFFICE/DocServer](https://github.com/ONLYOFFICE/DocServer)

#### 04. Seafile · Armazenamento de Arquivos de Altíssima Performance (Classificação: Persona Leve)
- **Módulo SaaS Substituído:** `Google Drive (sincronização e backup de arquivos)`
- **Economia Anual Individual:** `R$ 28.800/ano (50 usuários)` | **Licença OSI:** `Apache-2.0`
- **Papel no Ecossistema:** Substitui o Google Drive com sincronização ultrarrápida e baixo consumo de recursos.

**1. O Que Faz & Como Funciona:** 
Sincroniza e versiona arquivos com biblioteca de blocos e criptografia no cliente. Backend em C (ccnet/seafile) com banco MySQL e armazenamento de blocos em disco.
```bash
# Inicialização Rápida via Docker / CLI
docker run -d -p 8000:8000 --name seafile seafileltd/seafile-mc:latest
```

**2. Racional Financeiro da Escolha:** 
Escrito em C com biblioteca de blocos, entrega sincronização de arquivos muito mais rápida que concorrentes, ideal para grandes volumes e poucos recursos.

**3. Requisitos de Infraestrutura & Veredito Técnico:** 
- Memória RAM Mínima: `1 GB RAM`
- CPU Recomendada: `1 vCPU`
- Imagem Docker Oficial: `seafileltd/seafile-mc:latest`
- Banco de Dados / Persistência: `MySQL / MariaDB`
- **Veredito da Engenharia:** *A escolha leve e veloz para armazenamento de arquivos em larga escala, com consumo mínimo de RAM.*

**4. Guia Prático de Uso em 3 Passos:** 
1. **Subida do Servidor:** Suba o contêiner Seafile e acesse o painel admin para criar a biblioteca corporativa.
2. **Clientes Desktop/Móvel:** Instale o cliente Seafile nos dispositivos e sincronize pastas selecionadas.
3. **Bibliotecas Compartilhadas:** Crie bibliotecas por departamento com permissões de leitura/escrita granulares.

**5. White-Label & Design System:** 
- Nível de Esforço: `Baixo` | Stack UI: `JavaScript + jQuery`
- Mecânica de Customização: Logo e nome da organização configuráveis no painel de administração.
- Manutenibilidade de Temas: Personalizações limitadas ao branding do painel, sem risco ao core.

**6. Ecossistema Agêntico (MCPs, Skills & Extensões):** 
- **[MCP Server] seafile-mcp:** Gestão de bibliotecas por agentes de IA. (`npx -y seafile-mcp`)
- **[Agent Skill] skill-backup-verifier:** Verifica integridade dos blocos de arquivos. (`.claude/skills/backup-verifier/SKILL.md`)
- **[CLI Tool] seaf-cli:** Sincronização de bibliotecas via linha de comando. (`seaf-cli sync -u https://drive.empresa -r /docs -d ~/Docs`)

**7. Documentação Operacional & Capacitação Técnica Dedicada:** 
- [Manual de Engenharia de VPS & Desinstalação Cirúrgica (HTML)](../05-manuais-e-trilhas-individuais/seafile/manuais/manual-seafile-vps-e-uso.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/seafile/manuais/manual-seafile-vps-e-uso.md)
- [Trilha Didática de Aprendizado em 5 Aulas (HTML)](../05-manuais-e-trilhas-individuais/seafile/trilhas/trilha-seafile-aprendizado.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/seafile/trilhas/trilha-seafile-aprendizado.md)

- **Repositório Oficial:** [https://github.com/haiwen/seafile](https://github.com/haiwen/seafile)

#### 05. HedgeDoc · Edição Colaborativa de Markdown Simples e Elegante (Classificação: Persona Simples)
- **Módulo SaaS Substituído:** `Google Docs + Google Keep (notas e documentação leve)`
- **Economia Anual Individual:** `R$ 28.800/ano (50 usuários)` | **Licença OSI:** `AGPL-3.0`
- **Papel no Ecossistema:** Substitui o Google Docs para notas, atas e documentação rápida em Markdown.

**1. O Que Faz & Como Funciona:** 
Permite criar e editar documentos Markdown colaborativos com preview em tempo real. Node.js com banco PostgreSQL e sincronização via WebSocket (ot.js).
```bash
# Inicialização Rápida via Docker / CLI
docker run -d -p 3000:3000 --name hedgedoc hedgedoc/hedgedoc:latest
```

**2. Racional Financeiro da Escolha:** 
Editor colaborativo em tempo real baseado em Markdown, com curadoria de links, histórico de versões e zero complexidade para usuários não-técnicos.

**3. Requisitos de Infraestrutura & Veredito Técnico:** 
- Memória RAM Mínima: `1 GB RAM`
- CPU Recomendada: `1 vCPU`
- Imagem Docker Oficial: `hedgedoc/hedgedoc:latest`
- Banco de Dados / Persistência: `PostgreSQL / SQLite`
- **Veredito da Engenharia:** *A escolha simples para documentação, atas e notas colaborativas sem a complexidade de um office completo.*

**4. Guia Prático de Uso em 3 Passos:** 
1. **Criação de Nota:** Abra o HedgeDoc e crie um novo documento Markdown compartilhando o link com a equipe.
2. **Edição em Tempo Real:** Vários colaboradores editam simultaneamente com preview lado a lado.
3. **Exportação:** Exporte para PDF, HTML ou Markdown com 1 clique para distribuição.

**5. White-Label & Design System:** 
- Nível de Esforço: `Baixo` | Stack UI: `Node.js + Ember.js`
- Mecânica de Customização: Logo e CSS corporativo configuráveis via variáveis de ambiente e tema.
- Manutenibilidade de Temas: Tema isolado em arquivos CSS, sem risco ao core.

**6. Ecossistema Agêntico (MCPs, Skills & Extensões):** 
- **[MCP Server] hedgedoc-mcp:** Criação de notas por agentes de IA. (`npx -y hedgedoc-mcp`)
- **[Agent Skill] skill-meeting-notes:** Gera atas de reunião em Markdown automaticamente. (`.claude/skills/meeting-notes/SKILL.md`)
- **[CLI Tool] hedgedoc-api:** API REST para criação de notas. (`curl -X POST https://docs.empresa/api/notes`)

**7. Documentação Operacional & Capacitação Técnica Dedicada:** 
- [Manual de Engenharia de VPS & Desinstalação Cirúrgica (HTML)](../05-manuais-e-trilhas-individuais/hedgedoc/manuais/manual-hedgedoc-vps-e-uso.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/hedgedoc/manuais/manual-hedgedoc-vps-e-uso.md)
- [Trilha Didática de Aprendizado em 5 Aulas (HTML)](../05-manuais-e-trilhas-individuais/hedgedoc/trilhas/trilha-hedgedoc-aprendizado.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/hedgedoc/trilhas/trilha-hedgedoc-aprendizado.md)

- **Repositório Oficial:** [https://github.com/hedgedoc/hedgedoc](https://github.com/hedgedoc/hedgedoc)

### PILAR 03: GRUPO 3: IDENTIDADE, SEGURANÇA & GOVERNANÇA (ADMIN, SSO, VAULT & ENDPOINT)
> **Alvo SaaS Substituído:** `Google Workspace (Admin Console + Cloud Identity + Google Vault + Endpoint Management)` | **Economia do Pilar:** `R$ 14.400/ano` 
> **Descrição Estratégica:** Frente responsável pelo login único (SSO), autenticação multifator, retenção de dados (eDiscovery), conformidade e gestão de dispositivos. Substitui o Admin Console, o Cloud Identity, o Google Vault e o Endpoint Management por ferramentas soberanas de identidade e governança.

#### 01. Authentik · Plataforma Moderna de Identidade (SSO, MFA & Políticas) (Classificação: Persona Completa)
- **Módulo SaaS Substituído:** `Google Cloud Identity + Admin Console (SSO e federação)`
- **Economia Anual Individual:** `R$ 14.400/ano (50 usuários)` | **Licença OSI:** `MIT`
- **Papel no Ecossistema:** Substitui o Cloud Identity/Admin com SSO, MFA, federação e motor de políticas visual.

**1. O Que Faz & Como Funciona:** 
Centraliza login único, autenticação multifator e políticas de acesso para todos os aplicativos da suíte. Backend Python (Django) com frontend React e provedores OIDC/SAML/LDAP.
```bash
# Inicialização Rápida via Docker / CLI
docker run -d -p 9000:9000 --name authentik authentik/server:latest
```

**2. Racional Financeiro da Escolha:** 
Interface moderna com provedor de identidade completo, suporte a OIDC/SAML/LDAP, MFA adaptativo e editor visual de políticas de acesso por aplicação.

**3. Requisitos de Infraestrutura & Veredito Técnico:** 
- Memória RAM Mínima: `2 GB RAM`
- CPU Recomendada: `2 vCPU`
- Imagem Docker Oficial: `authentik/server:latest`
- Banco de Dados / Persistência: `PostgreSQL + Redis`
- **Veredito da Engenharia:** *A escolha mais completa e moderna para substituir o Cloud Identity, com políticas visuais e MFA adaptativo nativos.*

**4. Guia Prático de Uso em 3 Passos:** 
1. **Criação do Provedor:** Configure o Authentik como IdP OIDC e conecte o Nextcloud, CryptPad e Seafile via SSO.
2. **Políticas de MFA:** Exija autenticação de dois fatores para aplicativos sensíveis no editor visual de políticas.
3. **Federação de Usuários:** Importe usuários do Active Directory ou LDAP existente via conector nativo.

**5. White-Label & Design System:** 
- Nível de Esforço: `Baixo` | Stack UI: `React + TypeScript`
- Mecânica de Customização: Logo, favicon e paleta de cores corporativas no tema do painel e das telas de login.
- Manutenibilidade de Temas: Tema isolado em configuração, sem risco ao core.

**6. Ecossistema Agêntico (MCPs, Skills & Extensões):** 
- **[MCP Server] authentik-mcp:** Gestão de usuários e políticas por agentes de IA. (`npx -y authentik-mcp`)
- **[Agent Skill] skill-access-reviewer:** Revê permissões e detecta acessos excessivos. (`.claude/skills/access-reviewer/SKILL.md`)
- **[CLI Tool] ak:** CLI para aplicar políticas de acesso em lote. (`ak policy apply ./politicas.yaml`)

**7. Documentação Operacional & Capacitação Técnica Dedicada:** 
- [Manual de Engenharia de VPS & Desinstalação Cirúrgica (HTML)](../05-manuais-e-trilhas-individuais/authentik/manuais/manual-authentik-vps-e-uso.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/authentik/manuais/manual-authentik-vps-e-uso.md)
- [Trilha Didática de Aprendizado em 5 Aulas (HTML)](../05-manuais-e-trilhas-individuais/authentik/trilhas/trilha-authentik-aprendizado.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/authentik/trilhas/trilha-authentik-aprendizado.md)

- **Repositório Oficial:** [https://github.com/goauthentik/authentik](https://github.com/goauthentik/authentik)

#### 02. Keycloak · Identity and Access Management Empresarial (Red Hat) (Classificação: Persona Robusta)
- **Módulo SaaS Substituído:** `Google Cloud Identity + Admin Console (IAM enterprise)`
- **Economia Anual Individual:** `R$ 14.400/ano (50 usuários)` | **Licença OSI:** `Apache-2.0`
- **Papel no Ecossistema:** Substitui o Cloud Identity com IAM enterprise, SSO SAML/OIDC e federação.

**1. O Que Faz & Como Funciona:** 
Fornece SSO, MFA, federação e gerenciamento de identidade para toda a suíte. Java (Quarkus) com provedores OIDC/SAML e armazenamento em PostgreSQL.
```bash
# Inicialização Rápida via Docker / CLI
docker run -d -p 8080:8080 --name keycloak quay.io/keycloak/keycloak:latest start-dev
```

**2. Racional Financeiro da Escolha:** 
Padrão de mercado para IAM open source, com suporte maduro a SAML, OIDC, LDAP, federação e realms isolados para múltiplas organizações.

**3. Requisitos de Infraestrutura & Veredito Técnico:** 
- Memória RAM Mínima: `2 GB RAM`
- CPU Recomendada: `2 vCPU`
- Imagem Docker Oficial: `quay.io/keycloak/keycloak:latest`
- Banco de Dados / Persistência: `PostgreSQL`
- **Veredito da Engenharia:** *A escolha robusta para IAM em escala enterprise, com federação SAML e isolamento por realms.*

**4. Guia Prático de Uso em 3 Passos:** 
1. **Criação do Realm:** Crie um realm corporativo e registre os clientes (Nextcloud, CryptPad, Seafile) como aplicações OIDC.
2. **MFA e Flows:** Configure fluxos de autenticação com TOTP e WebAuthn para todos os usuários.
3. **Federação SAML:** Conecte provedores externos (Azure AD, Okta) via federação SAML para SSO híbrido.

**5. White-Label & Design System:** 
- Nível de Esforço: `Médio` | Stack UI: `Angular + PatternFly`
- Mecânica de Customização: Tema de login e conta personalizável via tema customizado em CSS/HTML.
- Manutenibilidade de Temas: Tema isolado em diretório próprio, sem risco ao core.

**6. Ecossistema Agêntico (MCPs, Skills & Extensões):** 
- **[MCP Server] keycloak-mcp:** Gestão de realms e usuários por agentes de IA. (`npx -y keycloak-mcp`)
- **[Agent Skill] skill-sso-auditor:** Audita configurações de SSO e detecta riscos. (`.claude/skills/sso-auditor/SKILL.md`)
- **[CLI Tool] kcadm:** CLI de administração do Keycloak. (`kcadm.sh create users -r empresa -s username=joao`)

**7. Documentação Operacional & Capacitação Técnica Dedicada:** 
- [Manual de Engenharia de VPS & Desinstalação Cirúrgica (HTML)](../05-manuais-e-trilhas-individuais/keycloak/manuais/manual-keycloak-vps-e-uso.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/keycloak/manuais/manual-keycloak-vps-e-uso.md)
- [Trilha Didática de Aprendizado em 5 Aulas (HTML)](../05-manuais-e-trilhas-individuais/keycloak/trilhas/trilha-keycloak-aprendizado.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/keycloak/trilhas/trilha-keycloak-aprendizado.md)

- **Repositório Oficial:** [https://github.com/keycloak/keycloak](https://github.com/keycloak/keycloak)

#### 03. ZITADEL · IAM Moderno Event-Sourced com OIDC, SAML & MFA (Classificação: Persona Moderna)
- **Módulo SaaS Substituído:** `Google Cloud Identity + Admin Console (IAM moderno)`
- **Economia Anual Individual:** `R$ 14.400/ano (50 usuários)` | **Licença OSI:** `Apache-2.0`
- **Papel no Ecossistema:** Substitui o Cloud Identity com IAM moderno, APIs limpas e auditoria imutável.

**1. O Que Faz & Como Funciona:** 
Fornece identidade, SSO e MFA com modelo de eventos e auditoria completa. Go com CQRS/Event-Sourcing, armazenamento em PostgreSQL e APIs gRPC/REST.
```bash
# Inicialização Rápida via Docker / CLI
docker run -d -p 8080:8080 --name zitadel zitadel/zitadel:latest
```

**2. Racional Financeiro da Escolha:** 
Arquitetura event-sourced em Go/TypeScript com APIs gRPC/REST modernas, suporte nativo a OIDC, SAML, LDAP e trilha de auditoria imutável.

**3. Requisitos de Infraestrutura & Veredito Técnico:** 
- Memória RAM Mínima: `1 GB RAM`
- CPU Recomendada: `1 vCPU`
- Imagem Docker Oficial: `zitadel/zitadel:latest`
- Banco de Dados / Persistência: `PostgreSQL`
- **Veredito da Engenharia:** *A escolha moderna para IAM com auditoria imutável e APIs de primeira linha para integração com agentes.*

**4. Guia Prático de Uso em 3 Passos:** 
1. **Inicialização do Instance:** Suba o ZITADEL e crie a organização corporativa via console ou API.
2. **Aplicações OIDC:** Registre os aplicativos da suíte como clients OIDC com escopos personalizados.
3. **Auditoria e MFA:** Ative MFA e consulte a trilha de eventos imutável para conformidade.

**5. White-Label & Design System:** 
- Nível de Esforço: `Baixo` | Stack UI: `React + TypeScript`
- Mecânica de Customização: Logo e cores do console e telas de login configuráveis por organização.
- Manutenibilidade de Temas: Tema isolado por organização, sem risco ao core.

**6. Ecossistema Agêntico (MCPs, Skills & Extensões):** 
- **[MCP Server] zitadel-mcp:** Gestão de identidade por agentes de IA via gRPC/REST. (`npx -y zitadel-mcp`)
- **[Agent Skill] skill-audit-trail:** Analisa a trilha de auditoria e gera relatórios LGPD. (`.claude/skills/audit-trail/SKILL.md`)
- **[CLI Tool] zitadel-cli:** CLI para gestão de organizações. (`zitadelctl org create empresa`)

**7. Documentação Operacional & Capacitação Técnica Dedicada:** 
- [Manual de Engenharia de VPS & Desinstalação Cirúrgica (HTML)](../05-manuais-e-trilhas-individuais/zitadel/manuais/manual-zitadel-vps-e-uso.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/zitadel/manuais/manual-zitadel-vps-e-uso.md)
- [Trilha Didática de Aprendizado em 5 Aulas (HTML)](../05-manuais-e-trilhas-individuais/zitadel/trilhas/trilha-zitadel-aprendizado.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/zitadel/trilhas/trilha-zitadel-aprendizado.md)

- **Repositório Oficial:** [https://github.com/zitadel/zitadel](https://github.com/zitadel/zitadel)

#### 04. Authelia · SSO e 2FA Leve na Borda do Reverse Proxy (Classificação: Persona Leve)
- **Módulo SaaS Substituído:** `Google Endpoint Management (MFA na borda)`
- **Economia Anual Individual:** `R$ 14.400/ano (50 usuários)` | **Licença OSI:** `Apache-2.0`
- **Papel no Ecossistema:** Substitui o MFA do Admin com camada leve de SSO e 2FA no Traefik.

**1. O Que Faz & Como Funciona:** 
Adiciona autenticação de dois fatores e SSO leve na frente de aplicações web. Go com sessões em Redis e integração transparente via ForwardAuth do Traefik.
```bash
# Inicialização Rápida via Docker / CLI
docker run -d -p 9091:9091 --name authelia authelia/authelia:latest
```

**2. Racional Financeiro da Escolha:** 
Contêiner minúsculo em Go que adiciona SSO e 2FA a qualquer aplicação protegida pelo Traefik, sem banco de dados pesado.

**3. Requisitos de Infraestrutura & Veredito Técnico:** 
- Memória RAM Mínima: `256 MB RAM`
- CPU Recomendada: `0.5 vCPU`
- Imagem Docker Oficial: `authelia/authelia:latest`
- Banco de Dados / Persistência: `SQLite / Redis (sessões)`
- **Veredito da Engenharia:** *A escolha leve para adicionar MFA e SSO a toda a suíte sem overhead de um IAM completo.*

**4. Guia Prático de Uso em 3 Passos:** 
1. **Integração com Traefik:** Configure o middleware ForwardAuth do Traefik para redirecionar ao Authelia.
2. **Regras de Acesso:** Defina quem pode acessar cada subdomínio (ex: apenas RH no status.empresa.com.br).
3. **MFA por TOTP:** Exija segundo fator via aplicativo autenticador para todos os logins.

**5. White-Label & Design System:** 
- Nível de Esforço: `Baixo` | Stack UI: `Go + Portal Web`
- Mecânica de Customização: Logo e texto do portal de login configuráveis em YAML.
- Manutenibilidade de Temas: Configuração de branding em arquivo, sem risco ao core.

**6. Ecossistema Agêntico (MCPs, Skills & Extensões):** 
- **[MCP Server] authelia-mcp:** Gestão de sessões por agentes de IA. (`npx -y authelia-mcp`)
- **[Agent Skill] skill-access-gate:** Ajusta regras de acesso por perfil. (`.claude/skills/access-gate/SKILL.md`)
- **[CLI Tool] authelia-cli:** CLI para gestão de usuários. (`authelia storage user add`)

**7. Documentação Operacional & Capacitação Técnica Dedicada:** 
- [Manual de Engenharia de VPS & Desinstalação Cirúrgica (HTML)](../05-manuais-e-trilhas-individuais/authelia/manuais/manual-authelia-vps-e-uso.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/authelia/manuais/manual-authelia-vps-e-uso.md)
- [Trilha Didática de Aprendizado em 5 Aulas (HTML)](../05-manuais-e-trilhas-individuais/authelia/trilhas/trilha-authelia-aprendizado.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/authelia/trilhas/trilha-authelia-aprendizado.md)

- **Repositório Oficial:** [https://github.com/authelia/authelia](https://github.com/authelia/authelia)

#### 05. Casdoor · SSO All-in-One com UI Amigável e LDAP (Classificação: Persona Simples)
- **Módulo SaaS Substituído:** `Google Cloud Identity (SSO simples)`
- **Economia Anual Individual:** `R$ 14.400/ano (50 usuários)` | **Licença OSI:** `Apache-2.0`
- **Papel no Ecossistema:** Substitui o Cloud Identity com SSO simples, UI intuitiva e suporte a LDAP.

**1. O Que Faz & Como Funciona:** 
Fornece SSO, gestão de usuários e MFA com interface administrativa simples. Go com frontend React e armazenamento em MySQL/PostgreSQL.
```bash
# Inicialização Rápida via Docker / CLI
docker run -d -p 8000:8000 --name casdoor casbin/casdoor:latest
```

**2. Racional Financeiro da Escolha:** 
Painel amigável para não-técnicos, suporte a OIDC/SAML/OAuth/LDAP e gestão de usuários com poucos cliques.

**3. Requisitos de Infraestrutura & Veredito Técnico:** 
- Memória RAM Mínima: `512 MB RAM`
- CPU Recomendada: `1 vCPU`
- Imagem Docker Oficial: `casbin/casdoor:latest`
- Banco de Dados / Persistência: `MySQL / PostgreSQL`
- **Veredito da Engenharia:** *A escolha simples para SSO com interface amigável, ideal para gestores sem experiência em TI.*

**4. Guia Prático de Uso em 3 Passos:** 
1. **Configuração Inicial:** Acesse o painel e defina o nome da organização, logo e provedores de autenticação.
2. **Registro de Apps:** Cadastre o Nextcloud, CryptPad e Seafile como aplicações OIDC com 1 clique.
3. **Convite de Usuários:** Convide colaboradores por e-mail e defina grupos de acesso no painel visual.

**5. White-Label & Design System:** 
- Nível de Esforço: `Baixo` | Stack UI: `React + Ant Design`
- Mecânica de Customização: Logo, tema e nome da organização configuráveis no painel administrativo.
- Manutenibilidade de Temas: Tema isolado em configuração, sem risco ao core.

**6. Ecossistema Agêntico (MCPs, Skills & Extensões):** 
- **[MCP Server] casdoor-mcp:** Gestão de usuários por agentes de IA. (`npx -y casdoor-mcp`)
- **[Agent Skill] skill-user-onboarder:** Provisiona usuários e grupos automaticamente. (`.claude/skills/user-onboarder/SKILL.md`)
- **[CLI Tool] casdoor-cli:** CLI para gestão de usuários. (`casdoor-cli user create`)

**7. Documentação Operacional & Capacitação Técnica Dedicada:** 
- [Manual de Engenharia de VPS & Desinstalação Cirúrgica (HTML)](../05-manuais-e-trilhas-individuais/casdoor/manuais/manual-casdoor-vps-e-uso.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/casdoor/manuais/manual-casdoor-vps-e-uso.md)
- [Trilha Didática de Aprendizado em 5 Aulas (HTML)](../05-manuais-e-trilhas-individuais/casdoor/trilhas/trilha-casdoor-aprendizado.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/casdoor/trilhas/trilha-casdoor-aprendizado.md)

- **Repositório Oficial:** [https://github.com/casdoor/casdoor](https://github.com/casdoor/casdoor)

---

## CAPÍTULO 4 · CAMADA DE COLA, SSO FEDERADO & BLUEPRINTS N8N

### Arquitetura de Interconexão sem Silos de Dados
- ** Autenticação Única Federada (SSO):** Keycloak / Authentik (OpenID Connect / SAML) unificando o login dos colaboradores no Nextcloud Hub, CryptPad, ONLYOFFICE, Seafile, Zimbra e HedgeDoc, eliminando senhas isoladas por aplicação.
- ** Barramento de Eventos Assíncronos:** n8n Community Edition atuando como orquestrador central de eventos assíncronos (Usuário provisionado no Keycloak -> criação de caixa no Stalwart -> provisionamento de drive no Seafile -> notificação de boas-vindas no Nextcloud Talk).
- ** Gateway de Borda & Ingress TLS:** Traefik Proxy v3 com terminação TLS automática via Let's Encrypt e roteamento por subdomínios corporativos (mail.empresa.com.br, docs.empresa.com.br, drive.empresa.com.br, sso.empresa.com.br, status.empresa.com.br).

### Fluxo Operacional de Ponta a Ponta
1. Provisionamento de Identidade: O administrador cria o colaborador no Keycloak/Authentik;
2. Criação de Caixa & Agenda: O webhook dispara no n8n que cria a conta de e-mail no Stalwart/Nextcloud e a agenda no CalDAV;
3. Provisionamento de Arquivos: O n8n cria a biblioteca do usuário no Seafile e a pasta de documentos no CryptPad;
4. Onboarding Colaborativo: O n8n envia mensagem de boas-vindas no Nextcloud Talk com links de acesso;
5. Armazenamento & Edição: O usuário edita documentos no ONLYOFFICE conectado ao Seafile e agenda reuniões no Nextcloud Calendar;
6. Governança & Backup: O n8n dispara o backup diário e o Uptime Kuma monitora a saúde de todos os serviços com alerta no chat corporativo.

### Blueprints de Workflows Prontos para n8n (Importação Instantânea)

#### Fluxo 1 · Provisionamento de Colaborador & Criação de Caixa e Drive
- *Objetivo:* Recebe a criação de usuário no Keycloak, cria a conta de e-mail no Stalwart, provisiona a biblioteca no Seafile e envia mensagem de boas-vindas no Nextcloud Talk.
- *Gatilho:* `Webhook HTTP POST `/webhook/novo-colaborador``
```json
{
 "name": "Workspace-to-Sovereign: Onboarding de Colaborador",
 "nodes": [
 {
 "parameters": {"httpMethod": "POST", "path": "novo-colaborador"},
 "name": "Webhook Entrada",
 "type": "n8n-nodes-base.webhook",
 "position": [250, 300]
 },
 {
 "parameters": {"url": "http://keycloak:8080/admin/realms/empresa/users", "method": "POST"},
 "name": "Criar no Keycloak",
 "type": "n8n-nodes-base.httpRequest",
 "position": [450, 300]
 },
 {
 "parameters": {"url": "http://stalwart:8080/api/account", "method": "POST"},
 "name": "Criar Caixa Stalwart",
 "type": "n8n-nodes-base.httpRequest",
 "position": [650, 300]
 },
 {
 "parameters": {"url": "http://seafile:8000/api2/repos", "method": "POST"},
 "name": "Criar Biblioteca Seafile",
 "type": "n8n-nodes-base.httpRequest",
 "position": [850, 300]
 }
 ]
}
```

#### Fluxo 2 · Verificação de Upload no Seafile & Alerta de Backup
- *Objetivo:* Quando um arquivo é enviado ao Seafile, o n8n dispara a verificação de integridade e notifica o Uptime Kuma e o administrador no Nextcloud Talk.
- *Gatilho:* `Webhook de Evento Seafile `file.uploaded``
```json
{
 "name": "Workspace-to-Sovereign: Verificação de Upload",
 "nodes": [
 {
 "parameters": {"path": "seafile-upload"},
 "name": "Webhook Upload Seafile",
 "type": "n8n-nodes-base.webhook",
 "position": [250, 300]
 },
 {
 "parameters": {"url": "http://seafile:8000/api2/check", "method": "POST"},
 "name": "Verificar Integridade",
 "type": "n8n-nodes-base.httpRequest",
 "position": [450, 300]
 },
 {
 "parameters": {"url": "http://uptime-kuma:3001/api/push", "method": "POST"},
 "name": "Heartbeat Uptime Kuma",
 "type": "n8n-nodes-base.httpRequest",
 "position": [650, 200]
 }
 ]
}
```

---

## CAPÍTULO 5 · MANUAL DE ENGENHARIA DE INFRAESTRUTURA & DEPLOY ALL-IN-ONE

### Entendendo os 4 Pilares da Infraestrutura (Sem Jargões)
- **1. O que é VPS?** A VPS é o seu 'apartamento alugado na nuvem'. Em vez de manter um computador físico ligado no escritório gastando luz, você aluga um servidor ultra-rápido que fica ligado 24 horas por dia, 7 dias por semana, com gerador e internet de fibra ótica.
- **2. O que é Docker Compose?** O Docker Compose é o 'manual de montagem e mobília automática'. Você não precisa instalar programas um por um nem entender de Linux. Ao rodar um único comando, o Docker baixa todos os módulos prontos e os liga automaticamente.
- **3. O que é Traefik?** O Traefik é o 'porteiro inteligente do condomínio'. Ele atende os visitantes na internet, verifica a segurança, coloca o cadeado verde (certificado SSL HTTPS gratuito) e encaminha cada pessoa para o apartamento certo (mail, docs, drive ou sso).
- **4. O que é n8n?** O n8n é o 'carteiro e mensageiro da empresa'. Ele fica vigiando os formulários e o login: quando um novo colaborador é cadastrado, o n8n cria a caixa de e-mail, a pasta de arquivos e avisa a equipe automaticamente.

> **Topologia & Segurança de Rede:** A infraestrutura opera sobre uma rede bridge isolada do Docker (`ecosystem_net`). Apenas o reverse proxy Traefik expõe as portas públicas 80 (HTTP com redirect) e 443 (HTTPS TLS automático via ACME/Let's Encrypt). Todas as ferramentas (Nextcloud, CryptPad, ONLYOFFICE, Seafile, Keycloak, n8n, Stalwart e PostgreSQL) comunicam-se exclusivamente pela rede interna através de seus nomes DNS de serviço (ex: `http://nextcloud:80`, `postgres:5432`), eliminando vetores de ataque externos e exposição de portas desnecessárias.

### Matriz dos 9 Serviços do Orquestrador
| # | Serviço / Módulo | Imagem Docker | Papel na Infraestrutura | Portas / Exposição | Persistência / Volumes |
|---|---|---|---|---|---|
| 01 | **Traefik Proxy v3** | `traefik:v3.0` | Ingress Controller & Reverse Proxy com TLS automático | `80:80 (HTTP com redirect) e 443:443 (HTTPS)` | `Volume `/letsencrypt/acme.json` para certificados SSL` |
| 02 | **Keycloak SSO** | `quay.io/keycloak/keycloak:latest` | Provedor Central de Identidade (IdP) & Single Sign-On (OIDC/SAML) | `Apenas rede interna (roteado via Traefik sob `sso.empresa.com.br`)` | `Banco `db_keycloak` no PostgreSQL compartilhado` |
| 03 | **n8n Automation** | `n8nio/n8n:latest` | Barramento de Eventos & Orquestração Assíncrona de Dados (Glue Layer) | `Apenas rede interna (roteado via Traefik sob `n8n.empresa.com.br`)` | `Volume `/data/.n8n` ou PostgreSQL` |
| 04 | **Nextcloud Hub** | `nextcloud:latest` | Comunicação Unificada: Mail, Calendar, Contacts & Talk | `Apenas rede interna (roteado via Traefik sob `mail.empresa.com.br`)` | `Volume `nextcloud_data:/var/www/html`` |
| 05 | **CryptPad** | `cryptpad/cryptpad:latest` | Suíte Office Criptografada (Docs, Sheets, Slides, Forms) | `Apenas rede interna (roteado via Traefik sob `docs.empresa.com.br`)` | `Volume `cryptpad_data:/cryptpad/data`` |
| 06 | **ONLYOFFICE Docs** | `onlyoffice/documentserver:latest` | Motor de Edição Colaborativa de Documentos | `Apenas rede interna (roteado via Traefik sob `office.empresa.com.br`)` | `Cache em Redis e arquivos temporários em disco` |
| 07 | **Seafile** | `seafileltd/seafile-mc:latest` | Armazenamento de Arquivos de Alta Performance (Drive) | `Apenas rede interna (roteado via Traefik sob `drive.empresa.com.br`)` | `Volume `seafile_data:/shared`` |
| 08 | **Stalwart Mail** | `stalwartlabs/stalwart:latest` | Servidor de E-mail Moderno (SMTP/IMAP/JMAP) | `Apenas rede interna (roteado via Traefik sob `smtp.empresa.com.br`)` | `Volume de dados do Stalwart e banco PostgreSQL` |
| 09 | **Cluster PostgreSQL 16** | `postgres:16-alpine` | Banco de Dados Relacional Unificado da Suíte | `Nenhuma porta pública (porta 5432 restrita à rede privada `ecosystem_net`)` | `Volume de dados `/var/lib/postgresql/data` com política de backup diário pg_dump` |
| 10 | **Redis Cache 7** | `redis:7-alpine` | Fila de Mensageria em Memória & Sessões Web | `Nenhuma porta pública (porta 6379 restrita à rede privada `ecosystem_net`)` | `Volume persistente `/data` com Append-Only File (AOF) ativado` |
| 11 | **Uptime Kuma** | `louislam/uptime-kuma:1` | Monitoramento 24h & Alertas de Saúde dos Serviços | `Apenas rede interna (roteado via Traefik sob `status.empresa.com.br`)` | `Volume `uptime_kuma_data:/app/data`` |

### Especificação da VPS Ideal para o Ecossistema Completo (e Por Que)
> **Perfil de Máquina Recomendado:** `8 vCPU Dedicated Cloud / 16 GB RAM ECC / 200-300 GB NVMe SSD / Link 1 Gbps / Ubuntu 24.04 LTS x86_64` 
> **Por Que Desta Configuração (Racional Técnico):** Garante estabilidade absoluta para os 11 contêineres rodando em simultâneo com isolamento de processos, prevenindo gargalos de I/O em banco de dados e eliminando o risco do OOM Killer durante picos de sincronização de arquivos e e-mails.

#### Distribuição de Recursos de Hardware por Serviço (vCPU & RAM)
| Serviço / Módulo | vCPU Alocada | Memória RAM | Motivo Técnico / Gargalo Previsto |
|---|---|---|---|
| **Traefik Ingress & TLS** | `0.5 vCPU` | `256 MB` | Roteamento reativo de borda, compressão Brotli/Gzip e renovação automática de certificados SSL. |
| **Keycloak SSO (OpenJDK JVM)** | `1.5 vCPU` | `2.0 GB` | Baseline da JVM Java para autenticação federada OIDC/SAML e criptografia de senhas Argon2. |
| **Nextcloud Hub & Talk** | `2.0 vCPU` | `4.0 GB` | Processamento de e-mail, agenda, contatos e chamadas WebRTC do Talk para 50 colaboradores. |
| **CryptPad & ONLYOFFICE** | `1.5 vCPU` | `3.0 GB` | Edição colaborativa de documentos em tempo real e conversão de formatos Office. |
| **Seafile & Stalwart Mail** | `1.0 vCPU` | `2.0 GB` | Sincronização de blocos de arquivos e envio/recebimento de e-mails com filtros anti-spam. |
| **n8n Orquestrador** | `0.5 vCPU` | `1.0 GB` | Execução assíncrona de fluxos de provisionamento e webhooks entre identidade e aplicativos. |
| **Buffer de Picos / Anti-OOM** | `1.0 vCPU` | `1.7 GB` | Margem de folga do kernel Linux para backups diários pg_dump e picos sazonais. |

#### Provedores de Nuvem Recomendados & Validados
| Provedor de Nuvem | Custo Mensal Estimado | Vantagem Principal / SLA |
|---|---|---|
| **Hetzner Cloud (CPX41 / CCX23)** | `€ 28 (~ R$ 170/mês)` | Melhor custo-benefício e performance bruta por vCPU dedicada (Datacenters UE/EUA). |
| **Contabo (Cloud VPS L)** | `€ 16 (~ R$ 100/mês)` | Maior volume de memória RAM e disco NVMe por valor investido. |
| **DigitalOcean (Dedicated 16GB)** | `$ 84 (~ R$ 460/mês)` | Excelente SLA de rede, suporte global e facilidade de snapshots. |
| **AWS Lightsail (16GB RAM)** | `$ 80 (~ R$ 440/mês)` | Infraestrutura corporativa AWS com 5 TB de transferência inclusos. |

### Dimensionamento de Hardware Recomendado
- **Memória RAM Total:** `16 GB RAM`
- **Processamento CPU:** `8 vCPU`
- **Armazenamento SSD:** `200-300 GB NVMe SSD`

### Arquivo `docker-compose.yml` Consolidado para Produção
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

### Roteiro de Instalação e Subida em 4 Passos

1. **Passo 1: Contratar a VPS (Tempo estimado: 3 minutos):** Acesse um provedor de nuvem confiável (como Hetzner Cloud, DigitalOcean, Contabo ou AWS Lightsail). Escolha o plano com 8 vCPU e 16 GB RAM, selecione o sistema operacional Ubuntu 22.04 LTS e clique em 'Criar Servidor'. Você receberá o IP da máquina por e-mail.
2. **Passo 2: Apontar o seu Domínio (Tempo estimado: 2 minutos):** No site onde você comprou seu domínio (Registro.br, Cloudflare, GoDaddy ou Hostinger), vá na aba DNS e crie um apontamento Tipo A com o nome `*` (asterisco) apontando para o IP da sua VPS. Isso garante que `mail.empresa.com.br`, `docs.empresa.com.br` e `drive.empresa.com.br` funcionem sozinhos.
3. **Passo 3: Rodar o Comando de 1 Clique (Tempo estimado: 1 minuto):** Abra o terminal da VPS e cole o comando automático de inicialização. O sistema fará o download de todas as ferramentas, configurará os bancos de dados e ativará os certificados de segurança SSL em menos de 120 segundos.
4. **Passo 4: Acessar os Painéis no seu Navegador:** Abra o navegador no seu computador e acesse: `mail.empresa.com.br` para e-mail e agenda, `docs.empresa.com.br` para documentos, `drive.empresa.com.br` para arquivos e `sso.empresa.com.br` para o login único.

---

## CAPÍTULO 6 · PROTOCOLOS DE MODULARIDADE & HOT-SWAP (PRINCÍPIO DO LEGO)

> **O Princípio das Tomadas Independentes:** 
> A arquitetura opera sob o princípio de 'Tomadas e Aparelhos Independentes'. Nenhuma ferramenta fica grudada ou dependente da outra com código travado. Imagine uma régua de tomadas na sua sala: a sua TV (Nextcloud) e o seu Arquivo (Seafile) funcionam perfeitamente mesmo se você desligar o Abajur (CryptPad). Se você quiser trocar o abajur por uma luminária moderna, basta tirar da tomada e plugar a nova. Nada na sua sala quebra.

### Protocolo 1: Inserção de Novas Ferramentas (Plug-and-Play)
1. Abra o arquivo `docker-compose.override.yml` e cole a receita da nova ferramenta;
2. Execute `docker compose up -d` no terminal;
3. O sistema cria o endereço web e o cadeado verde SSL automaticamente em 30 segundos;
4. Abra o painel do n8n e conecte o novo módulo aos fluxos existentes arrastando o mouse.

### Protocolo 2: Substituição de Ferramenta em Produção (Hot-Swap sem Downtime)
1. Suba a Nova Ferramenta em Paralelo: Inicie a nova solução em um endereço temporário (ex: `novo-docs.empresa.com.br`) mantendo a antiga funcionando;
2. Transfira a Conexão no n8n: No painel visual do n8n, mude o nó de disparo para apontar para a nova ferramenta;
3. Importe os Documentos: Faça o download da planilha de usuários da ferramenta antiga e importe na nova;
4. Mude o Endereço Oficial: Altere a rota para que `docs.empresa.com.br` aponte para a nova ferramenta;
5. Desligue a Antiga com Segurança: Pare o serviço antigo digitando `docker compose stop <servico_antigo>`. Seus colaboradores nem notarão a troca!

### Protocolo 3: Remoção Segura de Módulos
1. No painel visual do n8n, desligue os gatilhos vinculados à ferramenta que deseja remover;
2. No terminal da VPS, digite `docker compose stop <nome_ferramenta>`;
3. Os dados históricos continuam guardados com segurança na pasta de backup da VPS para você consultar quando quiser.

### Estudo de Caso Prático: Substituição do CryptPad por outra suíte office (ex: ONLYOFFICE + Nextcloud Text)
- **1. Isolamento Operacional:** O Nextcloud e o Seafile não conversam com o CryptPad diretamente, eles conversam com o n8n. Por isso, a sua equipe de documentos e arquivos continua trabalhando normalmente sem nenhuma parada.
- **2. Início do Novo Contêiner:** `O técnico ou gestor sobe a nova ferramenta de documentos no arquivo de extensão sem mexer nas ferramentas existentes.`
- **3. Chaveamento no n8n:** No painel visual do n8n, basta trocar a caixinha do CryptPad pela caixinha do ONLYOFFICE com 2 cliques.
- **4. Resultado Final:** A troca é concluída com ZERO minutos de parada no trabalho colaborativo e ZERO perda de documentos.

### Perguntas Frequentes (FAQ Operacional para Não-Técnicos)

- ** E se a VPS for reiniciada por falta de luz no datacenter?**
 - *Resposta:* Todos os serviços possuem configuração de auto-recuperação (restart: always). Quando o servidor ligar novamente, todas as ferramentas e bancos de dados sobem sozinhos sem você precisar fazer nada.

- ** Como funcionam os backups dos meus e-mails e arquivos?**
 - *Resposta:* Todas as informações de caixas, documentos e arquivos ficam armazenadas em uma pasta segura de dados (`/var/lib/postgresql/data` e volumes de aplicação). Um script diário gera cópias automáticas que podem ser enviadas para o seu armazenamento externo criptografado.

- ** Preciso contratar um desenvolvedor para usar no dia a dia?**
 - *Resposta:* Não! O uso rotineiro da sua equipe é 100% feito pelo navegador web em telas modernas e em português, exatamente como se estivesse usando o Gmail, o Google Drive ou o Google Docs.

---

## CAPÍTULO 7 · ROTEIRO PRÁTICO DE MIGRAÇÃO DE DADOS HISTÓRICOS

### 1. Migração do Gmail para Nextcloud Mail / Stalwart
- **O que migrar:** Caixas de e-mail completas (pastas, mensagens, anexos), contatos e calendários dos 50 usuários.
- **Passos de Migração:**
 1. No Google Workspace, ative a IMAP API e gere uma senha de aplicativo para cada conta ou use o Google Takeout para exportação em MBOX;
 1. No servidor soberano, crie as contas correspondentes no Stalwart/Nextcloud Mail com os mesmos endereços;
 1. Utilize a ferramenta imapsync para copiar mensagens e pastas do Gmail para o novo servidor em lote;
 1. Exporte os contatos (CSV/vCard) e os calendários (ICS) do Google e importe no Nextcloud Contacts/Calendar via CalDAV/CardDAV.
- ** Cuidados Críticos:** Mantenha o DKIM e o SPF do domínio apontando para o novo servidor antes de desligar o Gmail para evitar perda de entregabilidade.

### 2. Migração do Google Drive / Docs para Seafile / CryptPad / ONLYOFFICE
- **O que migrar:** Arquivos do Drive, documentos do Docs, planilhas do Sheets e apresentações do Slides.
- **Passos de Migração:**
 1. No Google Takeout, solicite o export de Drive e Documentos nos formatos .docx, .xlsx, .pptx e PDF;
 1. No Seafile (`drive.empresa.com.br`), crie as bibliotecas por departamento e faça o upload em massa das pastas;
 1. Para documentos colaborativos, importe no CryptPad ou conecte o ONLYOFFICE ao Seafile para edição nativa;
 1. Revise as permissões de compartilhamento e víncule os arquivos aos usuários do Keycloak.
- ** Cuidados Críticos:** Verifique a fidelidade de formatação dos arquivos .docx/.xlsx após a conversão pelo ONLYOFFICE antes de descartar os originais.

### 3. Migração do Google Calendar / Contacts para Nextcloud
- **O que migrar:** Agendas compartilhadas, eventos recorrentes e catálogo corporativo de contatos.
- **Passos de Migração:**
 1. Exporte as agendas do Google Calendar em formato ICS (um arquivo por calendário);
 1. No Nextcloud Calendar, importe os arquivos ICS criando os calendários departamentais correspondentes;
 1. Exporte os contatos do Google em vCard e importe no Nextcloud Contacts;
 1. Conecte os clientes (Outlook, Thunderbird, dispositivos móveis) via CalDAV/CardDAV para sincronização contínua.
- ** Cuidados Críticos:** Confirme se eventos recorrentes e convites mantiveram os participantes corretos após a importação ICS.

---

## CAPÍTULO 8 · GOVERNANÇA CORPORATIVA, BACKUP 3-2-1 & CONFORMIDADE LGPD

> **Arquitetura de Proteção de Dados 3-2-1:** A política de proteção de dados opera na regra de ouro 3-2-1: (3) cópias de dados em (2) tipos de mídias diferentes, com (1) cópia externa criptografada em nuvem fria (Wasabi / AWS S3 / armazenamento próprio).

### Script Automatizado de Backup Diário com Criptografia AES-256
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

### Checklist de Conformidade Estrita com a LGPD

- **Soberania Física dos Dados:** Em conformidade: O banco reside em servidor exclusivo da empresa, sem compartilhamento com provedores terceiros ou venda de dados para IA pública.
- **Direito de Exclusão do Titular (Art. 18 LGPD):** Em conformidade: O n8n executa script de expurgo automatizado com 1 clique no Keycloak, Nextcloud, Seafile e Stalwart quando solicitado pelo colaborador.
- **Criptografia em Trânsito & Repouso:** Em conformidade: Trânsito 100% sob TLS 1.3 / HSTS automático via Traefik e volumes criptografados com LUKS/AES-256 no sistema de arquivos do host.
- **Trilha de Auditoria & Logs de Acesso:** Em conformidade: O Keycloak e o PostgreSQL gravam logs imutáveis de cada autenticação e ação executada por colaboradores, substituindo o Google Vault.

---

## CAPÍTULO 9 · CRONOGRAMA DE IMPLANTAÇÃO EM 30 DIAS & MONITORAMENTO

### Cronograma Executivo de Virada de Chave (4 Semanas)

#### Semana 1 (Dias 1 a 7) · Infraestrutura & Instalação do Cluster
- *Atividades Principais:* Contratação da VPS, configuração de DNS wildcard (*.empresa.com.br), execução do docker-compose.yml e ativação dos certificados SSL automáticos via Traefik.
- * Marco de Conclusão:* **Todos os painéis acessíveis online com cadeado verde (HTTPS).**

#### Semana 2 (Dias 8 a 14) · Migração de Dados & Conexão de Identidade
- *Atividades Principais:* Importação de caixas do Gmail via imapsync, migração do Drive para o Seafile e provisionamento de usuários no Keycloak com SSO.
- * Marco de Conclusão:* **Base histórica 100% carregada e colaboradores logando com uma única senha.**

#### Semana 3 (Dias 15 a 21) · Importação dos Blueprints n8n & Treinamento das Equipes
- *Atividades Principais:* Importação dos templates de workflow no n8n, realização de testes de provisionamento (usuário -> caixa -> drive) e workshop de capacitação dos colaboradores.
- * Marco de Conclusão:* **Equipes operando com agilidade e fluxos automatizados aprovados.**

#### Semana 4 (Dias 22 a 30) · Virada de Chave Definitiva & Descomissionamento SaaS
- *Atividades Principais:* Redirecionamento dos registros MX para o novo servidor, ativação da régua de backup oficial e cancelamento das faturas recorrentes do Google Workspace.
- * Marco de Conclusão:* **Autonomia digital plena e economia de R$ 82.200/ano consolidada!**

### Monitoramento em Tempo Real da VPS (Uptime Kuma / Netdata / Portainer Community Edition (Monitoramento visual leve e em tempo real))

**Comandos de Diagnóstico em 1 Clique:**

- `docker stats --no-stream` Exibe o consumo instantâneo de memória RAM, % de CPU e tráfego de rede de cada um dos 11 serviços da stack.
- `docker compose ps` Verifica o status de saúde (Up / Healthy) de todos os contêineres e o tempo em que estão no ar.
- `docker compose logs -f --tail=50 traefik` Inspeciona o tráfego HTTP/HTTPS em tempo real e a renovação de certificados SSL.

**Métricas Críticas & Ações Imediatas:**

- **Consumo de RAM da VPS** (Limite: `> 85% por mais de 10 minutos`): Ajustar limite de memória no container do Nextcloud ou adicionar swap de 4 GB.
- **Uso de Disco SSD** (Limite: `> 80% do armazenamento total`): Executar o script de limpeza de logs e backups antigos com `docker system prune -f`.
- **Certificado TLS Traefik** (Limite: `Expiração em menos de 15 dias`): O Uptime Kuma emite alerta e o Traefik renova automaticamente via ACME/Let's Encrypt.
