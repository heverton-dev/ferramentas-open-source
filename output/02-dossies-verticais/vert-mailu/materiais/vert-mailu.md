# Dossiê Vertical de Desmantelamento SaaS: Mailu (Servidor de E-mail Modular em Docker)

> **Padrão Diamante R5-V · Quinteto Soberano Open Source**  
> **Alvo SaaS:** Mailu (Servidor de E-mail Modular em Docker) | **Custo Médio:** Gratuito (Self-hosted) | Opcionalmente US$ 10-50/mês em managed hosting | **Risco de Privacidade:** Embora open-source, o Mailu historicamente teve vulnerabilidades em isolamento de container; backup de dados centralizado em estrutura SQLite default sem segmentação nativa de inquilinos.  

---

## 1. O Quinteto Soberano Open Source

| Rank | Classificação | Ferramenta | Licença | Repositório | Economia Estimada |
| :---: | :--- | :--- | :---: | :--- | :--- |
| **#1** | *A Mais Robusta* | **Mailcow: dockerized (Stack Corporativo Industrial de E-mail)** | `GPL-3.0` | [https://github.com/mailcow/mailcow-dockerized](https://github.com/mailcow/mailcow-dockerized) | R$ 18.000/ano |
| **#2** | *A Mais Completa* | **Postfix + Dovecot + Roundcube (Tríade Clássica Customizável)** | `GPL-3.0 + BSD-3-Clause` | [Postfix: wietse/postfix | Dovecot: dovecot/core | Roundcube: roundcube/roundcubemail](Postfix: wietse/postfix | Dovecot: dovecot/core | Roundcube: roundcube/roundcubemail) | R$ 15.000/ano |
| **#3** | *A Mais Moderna* | **Maddy Mail Server + SnappyMail (Binário Go + SPA Moderno)** | `GPL-3.0 + AGPL-3.0` | [Maddy: foxcpp/maddy | SnappyMail: the-djmaze/snappymail](Maddy: foxcpp/maddy | SnappyMail: the-djmaze/snappymail) | R$ 12.000/ano |
| **#4** | *A Mais Leve* | **Exim + Courier IMAP + Rainloop (Ultraminimalista em ARM)** | `GPL-2.0 + LGPL-2.1 + AGPL-3.0` | [Exim: Exim/exim | Courier: courier-mta/courier | Rainloop: rainloop/rainloop-webmail](Exim: Exim/exim | Courier: courier-mta/courier | Rainloop: rainloop/rainloop-webmail) | R$ 6.000/ano |
| **#5** | *A Mais Simples* | **OpenSMTPD + doas + Dkhooks (Minimalismo OpenBSD)** | `ISC` | [https://github.com/opensmtpd/OpenSMTPD](https://github.com/opensmtpd/OpenSMTPD) | R$ 3.000/ano |

---

## 2. Detalhamento Técnico das Ferramentas do Quinteto

### #1 · Mailcow: dockerized (Stack Corporativo Industrial de E-mail) (*A Mais Robusta*)

- **O Que Faz:** Suíte industrial de correio eletrônico em contêineres Docker com isolamento superior ao Mailu, integrando MTA (Postfix), IMAP/POP3 (Dovecot), filtro antispam com IA (Rspamd), antivírus (ClamAV), painel administrativo avançado, sincronização CalDAV/CardDAV (SOGo) e dois-fatores TOTP/Yubi.
- **Como Funciona:** Stack Docker Compose multi-container com banco MariaDB dedicado (não SQLite), servidor Redis para cache e cálculo de reputação, sincronização automática de certificados Let's Encrypt com DKIM por domínio e isolamento de recursos via cgroups por tenant.
- **Requisitos de Infra:** 6 GB RAM, 4 vCPU
- **Comando Rápido:** `git clone https://github.com/mailcow/mailcow-dockerized && cd mailcow-dockerized && ./generate_config.sh && docker compose up -d`
- **White-Label & Design System:** Esforço `Mínimo (Plug & Play)` (PHP 8.x + Bootstrap 5 + SOGo Webmail) - Painel do Mailcow e SOGo Webmail suportam customização de logotipo, CSS corporativo e templates de welcome. Variáveis de ambiente MAILCOW_HOSTNAME e MAILCOW_LOGO_URL permitem white-label automático.

**Uso Complementar & Ecossistema Agêntico:**
- **MCP Server:** `mailcow-mcp-server` (`npx -y @mailcow/mcp-server`) - Servidor MCP para agentes de IA consultarem estatísticas de entrega, quarentena de spam e criação automática de contas em bulk.
- **Agent Skill:** `skill-mailcow-audit` (`.claude/skills/mailcow-audit/SKILL.md`) - Skill para auditoria contínua de reputação de IP, detecção de compromisso de conta e relatórios de conformidade LGPD.
- **CLI Tool:** `mailcow-cli` (`pip install mailcow-api-cli && mailcow mailbox list --domain empresa.com.br`) - Ferramenta de linha de comando para automação de provisionamento, limpeza de quarentena e integração com ERP.

### #2 · Postfix + Dovecot + Roundcube (Tríade Clássica Customizável) (*A Mais Completa*)

- **O Que Faz:** Combinação clássica de servidores Unix: Postfix (MTA com virtual_alias_domains), Dovecot (IMAP/POP3 com Sieve server-side), integrados com Roundcube (cliente web com drag-drop, PGP/Enigma nativo, suporte LDAP/AD). Cada camada é independente, escalável e auditável.
- **Como Funciona:** Postfix recebe SMTP, Dovecot armazena via Maildir (not mbox), Roundcube se conecta via IMAP4rev1. Estrutura de autenticação unificada via SASL (PAM/LDAP) ou banco de dados local. Cada componente roda em seu próprio processo, permitindo isolamento de falhas e escala horizontal simples.
- **Requisitos de Infra:** 3 GB RAM, 2 vCPU
- **Comando Rápido:** `apt install postfix dovecot-imapd dovecot-pop3d dovecot-sieve && docker run -d -p 8080:80 roundcube/roundcubemail:latest -e ROUNDCUBEMAIL_DEFAULT_HOST=localhost`
- **White-Label & Design System:** Esforço `Mínimo (Plug & Play para Roundcube)` (PHP (Roundcube) + HTML5 + CSS3 Elastic Skin) - Roundcube permite override total de CSS via skins/elastic/styles.css, customização de logotipo em templates/index.html e substituição de favicon. Postfix e Dovecot são headless; qualquer frontend IMAP/SMTP funciona.

**Uso Complementar & Ecossistema Agêntico:**
- **Antispam Engine:** `Rspamd + Mail-Filter` (`apt install rspamd && rspamd --version && docker run -d -p 11333:11333 rspamd/rspamd:latest`) - Engine de antispam moderno que integra com Postfix via socket, oferecendo aprendizado de Bayes local e histórico de reputação.
- **Agent Skill:** `skill-postfix-monitor` (`.claude/skills/postfix-monitor/SKILL.md`) - Skill para monitorar fila de entrega do Postfix, detectar rejeições de DNS/IP e alertar sobre saturation de disco.
- **MCP Server:** `dovecot-mcp-server` (`npx -y @dovecot/mcp-server`) - Conector MCP para consultar quotas de caixa, estatísticas de armazenamento e sincronização de grupos LDAP automaticamente.

### #3 · Maddy Mail Server + SnappyMail (Binário Go + SPA Moderno) (*A Mais Moderna*)

- **O Que Faz:** Maddy é servidor de e-mail monolítico escrito em Go que substitui Postfix/Dovecot por binário único compilado estaticamente; SnappyMail é webmail SPA hiper-rápido (fork ativo do RainLoop) com suporte nativo a WebAuthn, 2FA e criptografia PGP. Combinação oferece performance extrema com UX moderna.
- **Como Funciona:** Maddy centraliza SMTP/IMAP4/Sieve em processo único com mínimo footprint de memória. Armazena mensagens em SQLite/PostgreSQL nativo. SnappyMail conecta via IMAP4rev1 padrão, trazendo interface SPA responsiva. Zero bloatware; ambos cross-compiláveis para ARM, x86-64, RISC-V.
- **Requisitos de Infra:** 1.5 GB RAM, 1 vCPU
- **Comando Rápido:** `docker run -d -p 25:25 -p 143:143 -p 587:587 -p 993:993 -v maddy_data:/data foxcpp/maddy:latest && docker run -d -p 8888:80 djmaze/snappymail:latest`
- **White-Label & Design System:** Esforço `Mínimo (Plug & Play)` (Vanilla JavaScript (SnappyMail) + Modern CSS Variables) - SnappyMail oferece painel de temas built-in com seletor visual de cores, gradientes, logotipo da empresa e favicon. Customizações salvas em data/themes/custom-corp.json.

**Uso Complementar & Ecossistema Agêntico:**
- **Agent Skill:** `skill-snappy-dispatcher` (`.claude/skills/snappy-dispatcher/SKILL.md`) - Skill para agentes dispararem newsletters e comunicados internos com confirmação de entrega via API de SnappyMail.
- **MCP Server:** `maddy-mcp` (`npx -y @maddy/mcp-server`) - Conector para agentes consultarem fila de entrega, logs de rejeição SMTP e histórico de autenticação falhada.
- **CLI Tool:** `maddyctl` (`maddyctl creds create usuario@empresa.com.br && maddyctl imap-acct list`) - Utilitário Go para criação massiva de contas, geração de chaves DKIM e auditoria de quotas.

### #4 · Exim + Courier IMAP + Rainloop (Ultraminimalista em ARM) (*A Mais Leve*)

- **O Que Faz:** Tríade ultraminimalista: Exim (MTA modular com footprint 2MB), Courier IMAP (servidor IMAP leve com suporte POP3 e LDAP nativo), Rainloop (webmail AJAX responsivo, antecessor do SnappyMail, extremamente leve). Roda confortavelmente em Raspberry Pi, Orange Pi ou VPS de 256MB.
- **Como Funciona:** Exim implementa RFC 5321 (SMTP) com configurabilidade via arquivo de texto simples; Courier armazena via Maildir nativo e suporta quotas. Rainloop é PHP simples (sem composer hell) que se conecta via IMAP4. Cada um é independente e testado há 15+ anos.
- **Requisitos de Infra:** 512 MB RAM, 1 vCPU ARM
- **Comando Rápido:** `apt install exim4 courier-imap rainloop && systemctl start exim4 courier-imap && docker run -d -p 8080:80 -v rainloop_data:/rainloop/data mailserver/rainloop:latest`
- **White-Label & Design System:** Esforço `Baixo (Webroot Manual)` (PHP (Rainloop) + AJAX + CSS Responsivo) - Rainloop permite customização via arquivo config.php: DOMAIN_DEFAULT, TITLE_DEFAULT, LOGO_PATH. CSS override manual em /var/www/rainloop/app/templates/login.html ou via plugin custom.

**Uso Complementar & Ecossistema Agêntico:**
- **SpamFilter:** `SpamAssassin` (`apt install spamassassin spamc && systemctl start spamassassin && exim -C /etc/exim4/exim4.conf.template -v -x`) - Engine de antispam clássico que integra com Exim via pipe, usando Bayes local e regras regex. Robusto e configurável.
- **Agent Skill:** `skill-exim-relay` (`.claude/skills/exim-relay/SKILL.md`) - Skill para agentes consultarem logs de Exim, detectar falhas de DNS blacklist e gerar relatórios de bounce automático.
- **CLI Tool:** `exim-cli-monitor` (`exim -bpu && exim -br | wc -l`) - Comandos Unix nativos para inspecionar fila de Exim, listar remetentes ativos e purgar mensagens com erro de entrega.

### #5 · OpenSMTPD + doas + Dkhooks (Minimalismo OpenBSD) (*A Mais Simples*)

- **O Que Faz:** OpenSMTPD é servidor SMTP ultraminimalista do projeto OpenBSD, focado em segurança (pledge/unveil sandboxing nativo do kernel) e simplicidade. Configurado via arquivo single smtpd.conf (12 linhas típicas), com auditoria nativa de entrega. Ideal para relay-only ou pequenos times.
- **Como Funciona:** OpenSMTPD recebe SMTP e roteia via rules de filtro simples; não implementa IMAP (relé externo para ISP ou Dovecot remoto). Opcionalmente integra com local delivery Maildir. Cada transação de SMTP é forked em processo isolado com sandbox do kernel OpenBSD (pledge).
- **Requisitos de Infra:** 256 MB RAM, 1 vCPU ARM/x86
- **Comando Rápido:** `pkg install opensmtpd && cp /etc/mail/smtpd.conf.example /etc/mail/smtpd.conf && rcctl start smtpd`
- **White-Label & Design System:** Esforço `N/A (Headless / CLI Only)` (Nenhum (Relay-Only SMTP)) - OpenSMTPD é headless. Customizações ficam em smtpd.conf (regras de filtragem, mapeamento de domínios, TLS). Para webmail, integre com Dovecot remoto + qualquer cliente web (Roundcube, SnappyMail).

**Uso Complementar & Ecossistema Agêntico:**
- **Local Delivery:** `procmail + Dovecot Remote` (`pkg install procmail && opensmtpd action local_delivery deliver to mbox; dovecot via SSH para IMAP remoto`) - Arquitetura híbrida: OpenSMTPD recebe e entrega localmente via procmail; usuários conectam em Dovecot remoto via IMAP SSH para acessar mailbox.
- **Agent Skill:** `skill-opensmtpd-audit` (`.claude/skills/opensmtpd-audit/SKILL.md`) - Skill para agentes parsearem /var/log/maillog, detectarem falhas de autenticação upstream SMTP e alertarem sobre saturation de fila.
- **MCP Server:** `opensmtpd-mcp` (`npx -y @opensmtpd/mcp-server`) - Conector MCP para consultar estatísticas de entrega, listar domínios upstream e atualizar regras de relay sem reloading completo.

---

## 3. Matriz de Decisão & Migração Soberana

Para substituir integralmente o **Mailu (Servidor de E-mail Modular em Docker)**, recomenda-se a esteira automatizada de implantação em VPS com os manuais operacionais disponíveis em `output/`.