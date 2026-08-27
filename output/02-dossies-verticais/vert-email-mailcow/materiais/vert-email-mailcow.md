# Dossiê Vertical de Desmantelamento SaaS: Locaweb Email & Serviços de E-mail Empresariais Comerciais

> **Padrão Diamante R5-V · Quinteto Soberano Open Source**  
> **Alvo SaaS:** Locaweb Email & Serviços de E-mail Empresariais Comerciais | **Custo Médio:** R$ 1.200 a R$ 7.200/ano por caixa postal corporativa (Locaweb Email, Google Workspace, Outlook 365) | **Risco de Privacidade:** Comunicações executivas, minutas contratuais e dados financeiros de clientes sob custódia de datacenters estrangeiros sujeitos a leis como o US CLOUD Act. Acesso irrestrito de fornecedores terceirizados aos dados corporativos.  

---

## 1. O Quinteto Soberano Open Source

| Rank | Classificação | Ferramenta | Licença | Repositório | Economia Estimada |
| :---: | :--- | :--- | :---: | :--- | :--- |
| **#1** | *A Mais Robusta* | **Mailcow: dockerized (Stack Corporativo Industrial de E-mail)** | `GPL-3.0` | [https://github.com/mailcow/mailcow-dockerized](https://github.com/mailcow/mailcow-dockerized) | R$ 27.000/ano |
| **#2** | *A Mais Completa* | **Roundcube Webmail (O Webmail Open Source Mais Adotado Globalmente)** | `GPL-3.0` | [https://github.com/roundcube/roundcubemail](https://github.com/roundcube/roundcubemail) | R$ 18.000/ano |
| **#3** | *A Mais Moderna* | **SnappyMail (Webmail SPA Hiper-Rápido & Segurança Hardcore)** | `AGPL-3.0` | [https://github.com/the-djmaze/snappymail](https://github.com/the-djmaze/snappymail) | R$ 15.000/ano |
| **#4** | *A Mais Leve* | **Maddy Mail Server (Servidor de E-mail Binário Único em Go)** | `GPL-3.0` | [https://github.com/foxcpp/maddy](https://github.com/foxcpp/maddy) | R$ 12.000/ano |
| **#5** | *A Mais Simples* | **Mailu (Servidor de E-mail Simples & Amigável em Docker)** | `MIT` | [https://github.com/Mailu/Mailu](https://github.com/Mailu/Mailu) | R$ 10.800/ano |

---

## 2. Detalhamento Técnico das Ferramentas do Quinteto

### #1 · Mailcow: dockerized (Stack Corporativo Industrial de E-mail) (*A Mais Robusta*)

- **O Que Faz:** Suíte completa de correio eletrônico corporativo em contêineres Docker, integrando MTA (Postfix), IMAP/POP3 (Dovecot), filtro antispam com inteligência artificial (Rspamd), antivírus (ClamAV) e painel web administrativo com suporte a SOGo (CalDAV/CardDAV).
- **Como Funciona:** Arquitetura orquestrada via Docker Compose com banco MariaDB, servidor Redis para cache e reputação de IP, sincronização CalDAV/CardDAV via SOGo, automação completa de certificados Let's Encrypt com chave DKIM por domínio e ACL granulares de segurança.
- **Requisitos de Infra:** 4 GB RAM, 2 vCPU
- **Comando Rápido:** `git clone https://github.com/mailcow/mailcow-dockerized && cd mailcow-dockerized && ./generate_config.sh && docker compose up -d`
- **White-Label & Design System:** Esforço `Mínimo (Plug & Play)` (PHP + Bootstrap 5 + SOGo Webmail) - Interface do SOGo e painel do Mailcow permitem substituição direta de logotipo, CSS corporativo institucional, temas personalizados e templates de e-mail de boas-vindas.

**Uso Complementar & Ecossistema Agêntico:**
- **MCP Server:** `mailcow-mcp-server` (`npx -y @mailcow/mcp-server`) - Servidor MCP para automatizar criação de caixas postais, consulta a quarentena de spam e gerenciamento de aliases temporários via agentes de IA.
- **Agent Skill:** `skill-email-triage` (`.claude/skills/email-triage/SKILL.md`) - Skill para triagem automática de e-mails corporativos via IMAP, categorizando cobranças, suporte e leads prioritários com ML local.
- **CLI Tool:** `mailcow-cli` (`pip install mailcow-api-cli && mailcow mailbox list`) - Linha de comando para automação de tarefas administrativas, auditoria de tráfego de e-mail e migração de dados via API REST nativa do Mailcow.

### #2 · Roundcube Webmail (O Webmail Open Source Mais Adotado Globalmente) (*A Mais Completa*)

- **O Que Faz:** Cliente de webmail moderno e maduro com interface em três painéis (lista, preview, composição), suporte nativo a arrastar e soltar (drag & drop), catálogo de endereços LDAP/CardDAV/AddressBook.com, visualização de anexos de alta fidelidade e suporte a criptografia PGP/GPG de ponta a ponta com plugin Enigma.
- **Como Funciona:** Aplicação PHP assíncrona orientada a eventos que conversa com qualquer servidor IMAP/SMTP padrão, suportando ecossistema de centenas de plugins comunitários para 2FA, filtros Sieve, temas responsivos e integração com sistemas de autenticação LDAP/OAuth.
- **Requisitos de Infra:** 1 GB RAM, 1 vCPU
- **Comando Rápido:** `docker run -d -p 8080:80 -e ROUNDCUBEMAIL_DEFAULT_HOST=mail.suaempresa.com.br roundcube/roundcubemail:latest`
- **White-Label & Design System:** Esforço `Mínimo (Plug & Play)` (PHP + HTML5 + CSS3 Modular (Elastic Skin)) - Customização completa via CSS override em skins/elastic/styles.css, substituição de logotipo da empresa e favicon nas configurações do arquivo config.inc.php com reload sem downtime.

**Uso Complementar & Ecossistema Agêntico:**
- **Plugin Oficial:** `roundcube-enigma` (`plugins: ['enigma', 'managesieve', 'password', 'autologin']`) - Módulo criptográfico para gerenciamento de chaves públicas/privadas GPG/PGP diretamente na interface web com suporte a importação de chaves e keyserver público.
- **Agent Skill:** `skill-roundcube-search` (`.claude/skills/roundcube-search/SKILL.md`) - Skill para agentes de IA realizarem buscas semânticas e full-text em históricos de e-mails corporativos respeitando permissões IMAP de leitura/escrita.
- **Tema Responsivo:** `elastic-skin` (`$config['skin'] = 'elastic';`) - Tema oficial moderno com design adaptável para celulares, tablets e desktops de alta resolução com suporte a dark mode nativo.

### #3 · SnappyMail (Webmail SPA Hiper-Rápido & Segurança Hardcore) (*A Mais Moderna*)

- **O Que Faz:** Cliente de webmail Single Page Application (SPA) ultrarrápido e moderno, fork ativo do RainLoop com foco em segurança máxima, suporte nativo a 2FA (TOTP, FIDO2/WebAuthn com YubiKey) e zero rastreamento de dados ou cookies de terceiros.
- **Como Funciona:** Backend em PHP 8.x altamente otimizado com frontend em JavaScript puro e CSS moderno. Não requer banco de dados relacional para operar (armazena metadados localmente em SQLite ou Redis/Memcached com criptografia).
- **Requisitos de Infra:** 512 MB RAM, 1 vCPU
- **Comando Rápido:** `docker run -d -p 8888:80 --name snappymail -v snappymail_data:/snappymail/data djmaze/snappymail:latest`
- **White-Label & Design System:** Esforço `Mínimo (Plug & Play)` (HTML5 + Modern CSS Variables + Vanilla JS (Sem Webpack/Build)) - O painel administrativo possui editor visual de temas para ajustar cores, gradientes, logotipo da empresa, favicon e esquema dark/light com preview em tempo real.

**Uso Complementar & Ecossistema Agêntico:**
- **Agent Skill:** `skill-snappy-dispatcher` (`.claude/skills/snappy-dispatcher/SKILL.md`) - Skill para orquestrar envio de newsletters, comunicados internos e notificações transacionais disparando comandos via SMTP criptografado com rastreamento de entregas.
- **MCP Server:** `snappymail-mcp` (`npx -y @snappymail/mcp-server`) - Servidor MCP para agentes consultarem caixas de entrada de múltiplas contas, redigirem rascunhos de resposta com confirmação humana e executarem busca semântica.
- **Nextcloud App:** `snappymail-nc` (`occ app:install snappymail`) - Aplicativo oficial para integrar o webmail diretamente dentro do Nextcloud corporativo com SSO via LDAP/OAuth, compartilhamento de calendários e sincronização de contatos.

### #4 · Maddy Mail Server (Servidor de E-mail Binário Único em Go) (*A Mais Leve*)

- **O Que Faz:** Servidor de correio eletrônico tudo-em-um escrito em Go que substitui o combo arcaico Postfix + Dovecot + OpenDKIM + Rspamd por um único binário com consumo mínimo de memória (50-200 MB), TLS nativo, SMTP/IMAP4rev1, validação DKIM/SPF/DMARC e armazenamento de mensagens.
- **Como Funciona:** Implementa protocolo SMTP completo (com rCURRENT compliance), IMAP4rev1, validação DKIM/SPF/DMARC nativa e armazenamento de mensagens em SQLite ou PostgreSQL sem dependências externas complexas. Binário compilado estaticamente para máxima portabilidade.
- **Requisitos de Infra:** 256 MB RAM, 1 vCPU
- **Comando Rápido:** `docker run -d -p 25:25 -p 143:143 -p 587:587 -p 993:993 -v maddy_data:/data foxcpp/maddy:latest`
- **White-Label & Design System:** Esforço `Headless (API / CLI First)` (Go Backend / Compatível com qualquer Webmail (Roundcube / SnappyMail / Mailu)) - Servidor puramente headless com compatibilidade total com clientes padrão IMAP/SMTP (Thunderbird, Outlook, Apple Mail), permitindo plugar qualquer frontend corporativo.

**Uso Complementar & Ecossistema Agêntico:**
- **CLI Tool:** `maddyctl` (`maddyctl creds list && maddyctl imap-acct list && maddyctl deliverylocalcache flush`) - Utilitário de linha de comando para gerenciamento de credenciais, aliases, inspeção de filas de entrega de e-mail e diagnóstico de rejeições SMTP.
- **Agent Skill:** `skill-maddy-provisioner` (`.claude/skills/maddy-provisioner/SKILL.md`) - Skill para automação de criação e revogação de caixas postais corporativas durante onboarding/offboarding de colaboradores com logs auditados.
- **MCP Server:** `maddy-mcp` (`npx -y @maddy/mcp-server`) - Conector MCP para inspeção de entrega de e-mails transacionais, diagnóstico de erros SMTP em tempo real e sincronização com sistemas de RH/ERP.

### #5 · Mailu (Servidor de E-mail Simples & Amigável em Docker) (*A Mais Simples*)

- **O Que Faz:** Distribuição de e-mail completa, limpa e focada em facilidade de administração. Fornece interface web amigável para gerenciar domínios, contas, apelidos, respostas automáticas de férias, filtros antispam e listas de distribuição. Stack modular baseado em Docker com webmail embutido.
- **Como Funciona:** Stack modular baseado em contêineres Docker (Postfix, Dovecot, Rspamd, Roundcube ou SnappyMail embutidos), configurado via interface web em Python/Flask e banco SQLite/Postgres com persistência em volumes Docker.
- **Requisitos de Infra:** 2 GB RAM, 1 vCPU
- **Comando Rápido:** `curl -sSL https://setup.mailu.io/gen_compose -o docker-compose.yml && docker compose up -d`
- **White-Label & Design System:** Esforço `Mínimo (Plug & Play)` (Python Flask + Bootstrap 5 + Webmail Embutido) - Customização de logotipo, título do portal e mensagem de suporte no painel do Mailu via variáveis de ambiente no arquivo mailu.env com reload automático.

**Uso Complementar & Ecossistema Agêntico:**
- **Agent Skill:** `skill-mailu-monitor` (`.claude/skills/mailu-monitor/SKILL.md`) - Skill para monitorar score de reputação de IP do servidor de e-mail, alertar sobre potenciais bloqueios em listas RBL (SORBS, Spamhaus) e enviar relatórios semanais.
- **MCP Server:** `mailu-mcp-server` (`npx -y @mailu/mcp-server`) - Servidor MCP para consultar status de saúde do cluster de e-mails, adicionar regras de redirecionamento automáticas e sincronizar usuários de sistemas LDAP/AD.
- **REST API:** `mailu-rest-api` (`curl -H 'Authorization: Bearer TOKEN' https://mailu.empresa.com/api/v1/user`) - API REST nativa para integração direta com sistemas de ERP, portais de RH, sistemas de ticketing e workflows de onboarding automático de colaboradores.

---

## 3. Matriz de Decisão & Migração Soberana

Para substituir integralmente o **Locaweb Email & Serviços de E-mail Empresariais Comerciais**, recomenda-se a esteira automatizada de implantação em VPS com os manuais operacionais disponíveis em `output/`.