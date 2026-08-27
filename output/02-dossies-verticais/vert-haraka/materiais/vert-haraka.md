# Dossiê Vertical de Desmantelamento SaaS: Haraka (Node.js SMTP Gateway & Email Relay Service)

> **Padrão Diamante R5-V · Quinteto Soberano Open Source**  
> **Alvo SaaS:** Haraka (Node.js SMTP Gateway & Email Relay Service) | **Custo Médio:** R$ 6.000 a R$ 120.000/ano (cobrança por milhão de emails, taxas de relay SMTP, custos de IP dedicado e add-ons de compliance) | **Risco de Privacidade:** Metadados de emails (remetente, destinatário, timestamps), conteúdo de mensagens, eventos de entrega (bounces, opens, clicks) retidos e processados em datacenters de terceiros sujeitos a leis de países estrangeiros.  

---

## 1. O Quinteto Soberano Open Source

| Rank | Classificação | Ferramenta | Licença | Repositório | Economia Estimada |
| :---: | :--- | :--- | :---: | :--- | :--- |
| **#1** | *A Mais Robusta* | **Postfix (The Workhorse SMTP/MTA Server)** | `EPL-2.0` | [https://github.com/postfix/postfix](https://github.com/postfix/postfix) | R$ 48.000/ano |
| **#2** | *A Mais Completa* | **Mailcow: dockerized (Stack Corporativo All-in-One de E-mail)** | `GPL-3.0` | [https://github.com/mailcow/mailcow-dockerized](https://github.com/mailcow/mailcow-dockerized) | R$ 63.000/ano |
| **#3** | *A Mais Moderna* | **Mox (Secure Modern Email Server in Go)** | `MIT` | [https://github.com/mjl-/mox](https://github.com/mjl-/mox) | R$ 36.000/ano |
| **#4** | *A Mais Leve* | **Maddy Mail Server (All-in-One Lightweight Email Stack)** | `GPL-3.0` | [https://github.com/foxcpp/maddy](https://github.com/foxcpp/maddy) | R$ 18.000/ano |
| **#5** | *A Mais Simples* | **OpenSMTPD (Simple & Secure SMTP Server from OpenBSD)** | `ISC` | [https://github.com/OpenSMTPD/OpenSMTPD](https://github.com/OpenSMTPD/OpenSMTPD) | R$ 12.000/ano |

---

## 2. Detalhamento Técnico das Ferramentas do Quinteto

### #1 · Postfix (The Workhorse SMTP/MTA Server) (*A Mais Robusta*)

- **O Que Faz:** Servidor de correio eletrônico (MTA) mais confiável e estável do planeta: aceita mensagens SMTP, roteia para servidores de destino com retry inteligente, gerencia filas persistentes e implementa políticas de antispam nativas.
- **Como Funciona:** Desenvolvido em C de altíssimo desempenho com arquitetura modular, suporte nativo a SPF/DKIM/DMARC para autenticação, integração com bancos de dados SQL para virtual_mailbox_maps e aliases dinâmicos.
- **Requisitos de Infra:** 512 MB RAM, 1 vCPU
- **Comando Rápido:** `docker run -d --name postfix -v /etc/postfix:/etc/postfix -v /var/spool/postfix:/var/spool/postfix -p 25:25 -p 587:587 boky/postfix:latest`
- **White-Label & Design System:** Esforço `Baixo` (Postfixadmin Web / Adminer SQL) - Painel Postfixadmin permite gestão visual de domínios, contas e aliases sem edição de arquivos de configuração.

**Uso Complementar & Ecossistema Agêntico:**
- **Servidor MCP:** `mcp-postfix-monitor` (`pip install mcp-postfix-monitoring`) - Permite que agentes IA monitorem filas SMTP, alertem sobre bounces críticos e analisem logs de rejeição para diagnóstico de entrega.
- **Agent Skill:** `postfix-delivery-audit` (`.agents/skills/postfix-delivery-audit`) - Skill para auditoria automática de taxa de entrega, análise de erros SMTP 550/421 e recomendações de configuração SPF/DKIM.

### #2 · Mailcow: dockerized (Stack Corporativo All-in-One de E-mail) (*A Mais Completa*)

- **O Que Faz:** Suíte corporativa completa de correio em contêineres Docker: MTA (Postfix), servidor IMAP/POP3 (Dovecot), filtro antispam com IA (Rspamd), antivírus (ClamAV), webmail (SOGo), gerenciamento de domínios via painel web e sincronização CalDAV/CardDAV.
- **Como Funciona:** Orquestração via Docker Compose com MariaDB, Redis para cache/reputação de IP, Let's Encrypt automático para TLS, DKIM por domínio, integração com AD/LDAP para autenticação corporativa.
- **Requisitos de Infra:** 4 GB RAM, 2 vCPU
- **Comando Rápido:** `git clone https://github.com/mailcow/mailcow-dockerized && cd mailcow-dockerized && ./generate_config.sh && docker compose up -d`
- **White-Label & Design System:** Esforço `Mínimo (Plug & Play)` (PHP + Bootstrap 5 + SOGo Webmail) - Interface SOGo e painel Mailcow permitem white-label com substituição de logotipo, tema corporativo CSS e templates de email de boas-vindas.

**Uso Complementar & Ecossistema Agêntico:**
- **Servidor MCP:** `mailcow-mcp-server` (`npx -y @mailcow/mcp-server`) - Servidor MCP para automação de criação de caixas postais, consulta a quarentena de spam, aliases temporários e relatórios de entregabilidade via agentes IA.
- **Agent Skill:** `mailcow-provisioning` (`.agents/skills/mailcow-provisioning`) - Skill de onboarding automático de novos domínios corporativos, geração de certificados DKIM e sincronização com Active Directory.

### #3 · Mox (Secure Modern Email Server in Go) (*A Mais Moderna*)

- **O Que Faz:** Servidor de email moderno escrito em Go com filosofia security-first: SMTP/IMAP/Webmail integrados, DKIM/SPF/DMARC nativos, TLS obrigatório, proteção contra phishing, autenticação 2FA e suporte a DANE para certificados DNSSEC.
- **Como Funciona:** Binário único compilado em Go com zero dependências, inicialização automática de certificados ACME, interface web para administração e webmail responsivo, suporte a webhooks para integração com microsserviços.
- **Requisitos de Infra:** 1 GB RAM, 1 vCPU
- **Comando Rápido:** `docker run -d --name mox -v /data:/data -p 25:25 -p 587:587 -p 993:993 -p 80:80 -p 443:443 mjl/mox:latest`
- **White-Label & Design System:** Esforço `Mínimo` (Go HTML Templates / Responsive Webmail) - Webmail minimalista com suporte a customização CSS via injeção de estilo e temas light/dark automáticos.

**Uso Complementar & Ecossistema Agêntico:**
- **Servidor MCP:** `mcp-mox-mail-admin` (`pip install mcp-mox-administration`) - Servidor MCP para gerenciamento automático de contas, dominios e configurações de DKIM via agentes IA.

### #4 · Maddy Mail Server (All-in-One Lightweight Email Stack) (*A Mais Leve*)

- **O Que Faz:** Servidor de email minimalista e elegante escrito em Go: SMTP/IMAP completos, filtros de email via Sieve, gerenciamento de contas em YAML, suporte a múltiplos domínios e integração com LDAP/SQL.
- **Como Funciona:** Configuração declarativa em YAML sem necessidade de editar arquivos complexos, suporte a TLS automático, notificações via webhook para integração com Slack/Discord, logs estruturados em JSON.
- **Requisitos de Infra:** 512 MB RAM, 1 vCPU
- **Comando Rápido:** `docker run -d --name maddy -v /data:/data -p 25:25 -p 587:587 -p 993:993 foxcpp/maddy:latest`
- **White-Label & Design System:** Esforço `Mínimo` (CLI-only (Sem Webmail, use Roundcube separadamente)) - Configuração pura em YAML, extensível via plugins de Lua para lógica de roteamento customizada.

**Uso Complementar & Ecossistema Agêntico:**
- **Plugin:** `maddy-sieve-filters` (`Built-in Sieve support`) - Filtros de email declarativos no padrão Sieve RFC 5228 para regras automáticas de organização e rejeição de spam.
- **Servidor MCP:** `mcp-maddy-webhook-bridge` (`pip install mcp-maddy-webhooks`) - Bridge para transformar webhooks do Maddy em eventos automáticos capturados por agentes IA.

### #5 · OpenSMTPD (Simple & Secure SMTP Server from OpenBSD) (*A Mais Simples*)

- **O Que Faz:** Servidor SMTP ultrasimples e seguro por padrão do projeto OpenBSD: configuração em sintaxe limpa, sem funcionalidades desnecessárias, focado apenas em aceitar e rotear emails com máxima segurança e performance.
- **Como Funciona:** Desenvolvido em C com auditoria de segurança rigorosa, processo isolado em jail (privilege separation), suporte nativo a TLS 1.3 e autenticação SASL, sintaxe de configuração limpa sem 300 opções.
- **Requisitos de Infra:** 256 MB RAM, 0.5 vCPU
- **Comando Rápido:** `docker run -d --name opensmtpd -v /etc/opensmtpd:/etc/opensmtpd -p 25:25 -p 587:587 opensmtpd/opensmtpd:latest`
- **White-Label & Design System:** Esforço `Mínimo` (CLI-only / Configuration File) - Configuração puramente textual em sintaxe OpenSMTPD sem interfaces web ou dependências externas.

**Uso Complementar & Ecossistema Agêntico:**
- **Servidor MCP:** `mcp-opensmtpd-stats` (`pip install mcp-opensmtpd-monitoring`) - Monitoramento de fila SMTP, análise de logs e alertas de rejeição via agentes IA.
- **Script:** `opensmtpd-relay-monitor` (`scripts/monitor_opensmtpd_queue.sh`) - Script bash que coleta métricas de fila SMTP e envia relatórios diários via curl para seu sistema de monitoramento.

---

## 3. Matriz de Decisão & Migração Soberana

Para substituir integralmente o **Haraka (Node.js SMTP Gateway & Email Relay Service)**, recomenda-se a esteira automatizada de implantação em VPS com os manuais operacionais disponíveis em `output/`.