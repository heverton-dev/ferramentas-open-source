# Dossiê Vertical de Desmantelamento SaaS: Sovereign Email (Plataforma de Email Proprietária Centralizada)

> **Padrão Diamante R5-V · Quinteto Soberano Open Source**  
> **Alvo SaaS:** Sovereign Email (Plataforma de Email Proprietária Centralizada) | **Custo Médio:** US$ 120 a US$ 480/ano por usuário | **Risco de Privacidade:** Armazenamento de mensagens de negócios e confidenciais sob custódia de plataformas terceirizadas sujeitas a leis de vigilância internacionais e possíveis subpoenas.  

---

## 1. O Quinteto Soberano Open Source

| Rank | Classificação | Ferramenta | Licença | Repositório | Economia Estimada |
| :---: | :--- | :--- | :---: | :--- | :--- |
| **#1** | *A Mais Robusta* | **Mailcow: dockerized (Stack Corporativo Industrial de E-mail)** | `GPL-3.0` | [https://github.com/mailcow/mailcow-dockerized](https://github.com/mailcow/mailcow-dockerized) | R$ 36.000/ano |
| **#2** | *A Mais Completa* | **Roundcube Webmail (O Webmail Open Source Mais Adotado com Suporte a PGP)** | `GPL-3.0` | [https://github.com/roundcube/roundcubemail](https://github.com/roundcube/roundcubemail) | R$ 24.000/ano |
| **#3** | *A Mais Moderna* | **SnappyMail (Webmail SPA Hiper-Rápido com Segurança Paranóica)** | `AGPL-3.0` | [https://github.com/the-djmaze/snappymail](https://github.com/the-djmaze/snappymail) | R$ 18.000/ano |
| **#4** | *A Mais Leve* | **Maddy Mail Server (Servidor de E-mail em Binário Único em Go)** | `GPL-3.0` | [https://github.com/foxcpp/maddy](https://github.com/foxcpp/maddy) | R$ 15.000/ano |
| **#5** | *A Mais Simples* | **Mailu (Servidor de E-mail Simples & Limpo em Docker)** | `MIT` | [https://github.com/Mailu/Mailu](https://github.com/Mailu/Mailu) | R$ 12.000/ano |

---

## 2. Detalhamento Técnico das Ferramentas do Quinteto

### #1 · Mailcow: dockerized (Stack Corporativo Industrial de E-mail) (*A Mais Robusta*)

- **O Que Faz:** Suíte completa de correio eletrônico corporativo em contêineres Docker, integrando MTA (Postfix), IMAP/POP3 (Dovecot), filtro antispam com inteligência artificial (Rspamd), antivírus (ClamAV) e painel web administrativo com auditoria completa.
- **Como Funciona:** Arquitetura orquestrada via Docker Compose com banco MariaDB, servidor Redis para cache e reputação de IP, sincronização CalDAV/CardDAV via SOGo e automação completa de certificados Let's Encrypt com chave DKIM por domínio sob controle local.
- **Requisitos de Infra:** 4 GB RAM, 2 vCPU
- **Comando Rápido:** `git clone https://github.com/mailcow/mailcow-dockerized && cd mailcow-dockerized && ./generate_config.sh && docker compose up -d`
- **White-Label & Design System:** Esforço `Mínimo (Plug & Play)` (PHP + Bootstrap 5 + SOGo Webmail) - Interface do SOGo e painel do Mailcow permitem substituição direta de logotipo, CSS corporativo institucional, templates de e-mail de boas-vindas e branding completo do webmail.

**Uso Complementar & Ecossistema Agêntico:**
- **MCP Server:** `mailcow-mcp-server` (`npx -y @mailcow/mcp-server`) - Servidor MCP para automatizar criação de caixas postais, consulta a quarentena de spam, aliases temporários e auditoria de acesso via agentes de IA.
- **Agent Skill:** `skill-email-compliance-audit` (`.claude/skills/email-compliance/SKILL.md`) - Skill para auditoria contínua de conformidade com LGPD/GDPR, geração de relatórios de retenção e purga automática de dados sensíveis.
- **CLI Tool:** `mailcow-cli-advanced` (`pip install mailcow-api-cli && mailcow admin audit --days 30`) - Linha de comando para automação de tarefas administrativas avançadas, auditoria de tráfego e exportação de logs de segurança.

### #2 · Roundcube Webmail (O Webmail Open Source Mais Adotado com Suporte a PGP) (*A Mais Completa*)

- **O Que Faz:** Cliente de webmail moderno e maduro com interface em três painéis, suporte nativo a arrastar e soltar (drag & drop), catálogo de endereços LDAP/CardDAV, visualização de anexos, suporte a criptografia PGP/OpenPGP com Enigma.
- **Como Funciona:** Aplicação PHP assíncrona orientada a eventos que conversa com qualquer servidor IMAP/SMTP padrão, suportando ecossistema de centenas de plugins comunitários para 2FA, filtros Sieve, sincronização de agendas e temas responsivos.
- **Requisitos de Infra:** 1 GB RAM, 1 vCPU
- **Comando Rápido:** `docker run -d -p 8080:80 -e ROUNDCUBEMAIL_DEFAULT_HOST=mail.suaempresa.com.br -e ROUNDCUBEMAIL_SMTP_SERVER=mail.suaempresa.com.br roundcube/roundcubemail:latest`
- **White-Label & Design System:** Esforço `Mínimo (Plug & Play)` (PHP + HTML5 + CSS3 (Elastic Skin)) - Customização completa via CSS override em skins/elastic/styles.css e substituição de logotipo da empresa nas configurações do arquivo config.inc.php com suporte a templates HTML personalizados.

**Uso Complementar & Ecossistema Agêntico:**
- **Plugin Oficial:** `roundcube-enigma` (`plugins: ['enigma', 'managesieve', 'password', 'sieve_vacation']`) - Módulo criptográfico para gerenciamento de chaves públicas/privadas GPG/PGP diretamente na interface web com suporte a assinatura digital.
- **Agent Skill:** `skill-roundcube-search-encrypted` (`.claude/skills/roundcube-search/SKILL.md`) - Skill para agentes de IA realizarem buscas semânticas em históricos de e-mails corporativos criptografados respeitando permissões IMAP e conformidade de dados.
- **Tema Responsivo:** `elastic-skin-darkmode` (`$config['skin'] = 'elastic'; $config['theme'] = 'dark';`) - Tema oficial moderno com design adaptável para celulares, tablets e desktops de alta resolução com suporte a modo escuro para reduzir fadiga visual.

### #3 · SnappyMail (Webmail SPA Hiper-Rápido com Segurança Paranóica) (*A Mais Moderna*)

- **O Que Faz:** Cliente de webmail Single Page Application (SPA) ultrarrápido, fork moderno e ativo do RainLoop, com foco em segurança máxima, suporte nativo a 2FA (TOTP, FIDO2/WebAuthn), zero rastreamento de dados e proteção contra trojans de memória.
- **Como Funciona:** Backend em PHP 8.x altamente otimizado com frontend em JavaScript puro e CSS moderno. Não requer banco de dados relacional para operar; armazena metadados localmente ou em Redis/Memcached com isolamento de contextos.
- **Requisitos de Infra:** 512 MB RAM, 1 vCPU
- **Comando Rápido:** `docker run -d -p 8888:80 --name snappymail -v snappymail_data:/snappymail/data -e SNAPPYMAIL_IMAP_HOST=mail.suaempresa.com.br djmaze/snappymail:latest`
- **White-Label & Design System:** Esforço `Mínimo (Plug & Play)` (HTML5 + Modern CSS Variables + Vanilla JS) - O painel administrativo possui editor visual de temas para ajustar cores, gradientes, logotipo da empresa, favicon e favicons para sistemas de notificação com preview em tempo real e sem reload.

**Uso Complementar & Ecossistema Agêntico:**
- **Agent Skill:** `skill-snappy-secure-dispatcher` (`.claude/skills/snappy-dispatcher/SKILL.md`) - Skill para orquestrar envio de newsletters internas e comunicados confidenciais disparando comandos via SMTP criptografado com assinatura digital obrigatória.
- **MCP Server:** `snappymail-mcp-secure` (`npx -y @snappymail/mcp-server`) - Servidor MCP para agentes consultarem caixas de entrada seguras e redigirem rascunhos de resposta com confirmação humana e auditoria de operações.
- **Nextcloud App:** `snappymail-nc-enterprise` (`occ app:install snappymail && occ app:enable snappymail`) - Aplicativo oficial para integrar o webmail diretamente dentro do ambiente corporativo do Nextcloud com SSO corporativo e backup automático.

### #4 · Maddy Mail Server (Servidor de E-mail em Binário Único em Go) (*A Mais Leve*)

- **O Que Faz:** Servidor de correio eletrônico tudo-em-um escrito em Go que substitui o combo tradicional Postfix + Dovecot + OpenDKIM por um único binário com consumo mínimo de memória (50 MB em repouso).
- **Como Funciona:** Implementa SMTP, IMAP4rev1, validação DKIM/SPF/DMARC e armazenamento de mensagens em SQLite ou PostgreSQL nativo sem dependências externas complexas. Compilado estaticamente para portabilidade máxima.
- **Requisitos de Infra:** 256 MB RAM, 1 vCPU
- **Comando Rápido:** `docker run -d -p 25:25 -p 143:143 -p 587:587 -p 993:993 -v maddy_data:/data -e MADDY_HOSTNAME=mail.suaempresa.com.br foxcpp/maddy:latest`
- **White-Label & Design System:** Esforço `Headless (API / CLI First)` (Go Backend / Compatível com qualquer Webmail (Roundcube / SnappyMail)) - Servidor puramente headless com compatibilidade total com clientes padrão IMAP/SMTP, permitindo plugar qualquer frontend corporativo sem overhead de camadas de tradução.

**Uso Complementar & Ecossistema Agêntico:**
- **CLI Tool:** `maddyctl-operator` (`maddyctl creds list && maddyctl imap-acct list && maddyctl queue list`) - Utilitário de linha de comando para gerenciamento de credenciais, aliases, inspeção de filas de entrega de e-mail e diagnóstico de reputação de IP.
- **Agent Skill:** `skill-maddy-provisioner-rapid` (`.claude/skills/maddy-provisioner/SKILL.md`) - Skill para automação de criação e revogação de caixas postais corporativas durante onboarding/offboarding de colaboradores com operações em sub-segundo.
- **MCP Server:** `maddy-mcp-diagnostic` (`npx -y @maddy/mcp-server`) - Conector MCP para inspeção de entrega de e-mails transacionais, diagnóstico de erros SMTP em tempo real e alertas de falhas de autenticação.

### #5 · Mailu (Servidor de E-mail Simples & Limpo em Docker) (*A Mais Simples*)

- **O Que Faz:** Distribuição de e-mail completa, limpa e focada em facilidade de administração. Fornece interface web amigável em português para gerenciar domínios, contas, apelidos, respostas automáticas de férias, antispam e auditoria de acesso.
- **Como Funciona:** Stack modular baseado em contêineres Docker (Postfix, Dovecot, Rspamd, Roundcube ou SnappyMail embutidos), configurado via interface web em Python/Flask e banco SQLite/Postgres com backups automáticos.
- **Requisitos de Infra:** 2 GB RAM, 1 vCPU
- **Comando Rápido:** `curl -sSL https://setup.mailu.io/gen_compose -o docker-compose.yml && docker compose up -d`
- **White-Label & Design System:** Esforço `Mínimo (Plug & Play)` (Python Flask + Bootstrap + Webmail Embutido) - Customização de logotipo, título do portal, mensagem de suporte e branding completo no painel do Mailu via variáveis de ambiente no arquivo mailu.env com suporte a CSS customizado.

**Uso Complementar & Ecossistema Agêntico:**
- **Agent Skill:** `skill-mailu-monitor-alerts` (`.claude/skills/mailu-monitor/SKILL.md`) - Skill para monitorar score de reputação de IP do servidor de e-mail, alertar sobre potenciais bloqueios em listas RBL e sugerir ações corretivas automáticas.
- **MCP Server:** `mailu-mcp-health` (`npx -y @mailu/mcp-server`) - Servidor MCP para consultar status de saúde do cluster de e-mails, gerenciar regras de redirecionamento automáticas e exportar relatórios de compliance.
- **REST API:** `mailu-rest-api-complete` (`curl -H 'Authorization: Bearer TOKEN' https://mailu.empresa.com/api/v1/user && curl -X POST https://mailu.empresa.com/api/v1/user/create`) - API REST nativa completa para integração direta com sistemas de ERP, portais de RH e onboarding automático de colaboradores.

---

## 3. Matriz de Decisão & Migração Soberana

Para substituir integralmente o **Sovereign Email (Plataforma de Email Proprietária Centralizada)**, recomenda-se a esteira automatizada de implantação em VPS com os manuais operacionais disponíveis em `output/`.