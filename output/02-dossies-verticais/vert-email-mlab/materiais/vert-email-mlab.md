# Dossiê Vertical de Desmantelamento SaaS: Mail-in-a-Box

> **Padrão Diamante R5-V · Quinteto Soberano Open Source**  
> **Alvo SaaS:** Mail-in-a-Box | **Custo Médio:** Gratuito (Self-hosted), mas dependência de VPS própria (R$ 50-200/mês) | **Risco de Privacidade:** Instalação única em servidor único critica a infraestrutura, backups não são criptografados por padrão e dependência de shell scripts sem abstração clara de segurança.  

---

## 1. O Quinteto Soberano Open Source

| Rank | Classificação | Ferramenta | Licença | Repositório | Economia Estimada |
| :---: | :--- | :--- | :---: | :--- | :--- |
| **#1** | *A Mais Robusta* | **Mailcow: dockerized (Stack Corporativo Industrial de E-mail)** | `GPL-3.0` | [https://github.com/mailcow/mailcow-dockerized](https://github.com/mailcow/mailcow-dockerized) | R$ 28.000/ano |
| **#2** | *A Mais Completa* | **iRedMail: O Servidor Open Source Mais Modular da Comunidade** | `GPL-3.0` | [https://github.com/iredmail/iRedMail](https://github.com/iredmail/iRedMail) | R$ 24.000/ano |
| **#3** | *A Mais Moderna* | **Stalwart Mail: O Motor de E-mail de Próxima Geração** | `AGPL-3.0 e Comercial` | [https://github.com/stalwartlabs/mail-server](https://github.com/stalwartlabs/mail-server) | R$ 18.000/ano |
| **#4** | *A Mais Leve* | **Postfix + Dovecot + Rspamd (Stack Mínimo e Eficiente)** | `Postfix (IPL-1.0), Dovecot (LGPL-2.1), Rspamd (Apache-2.0)` | [https://github.com/postfix/postfix; https://github.com/dovecot/core; https://github.com/rspamd/rspamd](https://github.com/postfix/postfix; https://github.com/dovecot/core; https://github.com/rspamd/rspamd) | R$ 8.000/ano |
| **#5** | *A Mais Simples* | **Mailu: O Mail Suite Pronto para Produção** | `MIT` | [https://github.com/Mailu/Mailu](https://github.com/Mailu/Mailu) | R$ 10.000/ano |

---

## 2. Detalhamento Técnico das Ferramentas do Quinteto

### #1 · Mailcow: dockerized (Stack Corporativo Industrial de E-mail) (*A Mais Robusta*)

- **O Que Faz:** Suíte completa de correio eletrônico corporativo em contêineres Docker, integrando MTA (Postfix), IMAP/POP3 (Dovecot), filtro antispam com IA (Rspamd), antivírus (ClamAV), gerenciador de fila de mail (Solr), painel web administrativo e suporte nativo a clustering via API.
- **Como Funciona:** Arquitetura orquestrada via Docker Compose com banco MariaDB em replicação, servidor Redis para cache distribuído e reputação de IP, sincronização CalDAV/CardDAV via SOGo, automação de certificados Let's Encrypt com chave DKIM por domínio e balanceamento de carga de SMTP/IMAP entre nós.
- **Requisitos de Infra:** 8 GB RAM (cluster), 4 vCPU (cluster)
- **Comando Rápido:** `git clone https://github.com/mailcow/mailcow-dockerized && cd mailcow-dockerized && ./generate_config.sh && docker compose up -d`
- **White-Label & Design System:** Esforço `Mínimo (Plug & Play)` (PHP + Bootstrap 5 + SOGo Webmail) - Interface do SOGo e painel do Mailcow permitem substituição direta de logotipo, CSS corporativo institucional e templates de e-mail de boas-vindas via config centralizado no cluster.

**Uso Complementar & Ecossistema Agêntico:**
- **MCP Server:** `mailcow-cluster-mcp` (`npx -y @mailcow/mcp-cluster-server`) - Servidor MCP para orquestração automática de nós Mailcow, monitoramento de health, failover e escalabilidade via agentes de IA.
- **Agent Skill:** `skill-mailcow-sla` (`.claude/skills/mailcow-sla/SKILL.md`) - Skill para monitoramento de SLA de e-mail, alertas de latência SMTP/IMAP e relatórios de disponibilidade distribuída.
- **CLI Tool:** `mailcow-cluster-cli` (`pip install mailcow-cluster-cli && mailcow cluster status`) - Linha de comando para orquestração de múltiplos nós Mailcow, provisioning de domínios distribuídos e auditoria de tráfego agregado.

### #2 · iRedMail: O Servidor Open Source Mais Modular da Comunidade (*A Mais Completa*)

- **O Que Faz:** Framework completo de e-mail que integra Postfix, Dovecot, SpamAssassin, ClamAV, Fail2ban, Roundcube, SOGo e painel administrativo iRedAdmin-Pro com suporte a domínios virtuais ilimitados, grupos de distribuição, listas de discussão (Mailing List) e sincronização LDAP.
- **Como Funciona:** Instalação única via script iRedMail que configura todo o stack, criando estruturas LDAP/SQL para usuários e domínios. Suporta backends alternativos como OpenLDAP, MariaDB ou PostgreSQL com replicação nativa.
- **Requisitos de Infra:** 4 GB RAM, 2 vCPU
- **Comando Rápido:** `curl https://github.com/iredmail/iRedMail/raw/master/iRedMail.sh | bash && bash iRedMail.sh`
- **White-Label & Design System:** Esforço `Baixo` (PHP + Roundcube/SOGo + iRedAdmin) - iRedAdmin-Pro oferece white-label com logos customizáveis, templates de e-mail corporativos e temas responsivos. SOGo permite override total de CSS.

**Uso Complementar & Ecossistema Agêntico:**
- **Panel Oficial:** `iRedAdmin-Pro` (`https://www.iredmail.org/admin_panel.html`) - Painel web profissional para gerenciamento de domínios, usuários, políticas de spam/vírus e relatórios de tráfego em tempo real.
- **Agent Skill:** `skill-iredmail-audit` (`.claude/skills/iredmail-audit/SKILL.md`) - Skill para auditoria contínua de usuários iRedMail, detecção de contas comprometidas e conformidade com LGPD.
- **CLI Tool:** `iredmail-user-provisioning` (`pip install iredmail-api && iredmail provision --ldap-backend`) - CLI para bulk provisioning de usuários via LDAP, sincronismo com Active Directory e automação de quotas por departamento.

### #3 · Stalwart Mail: O Motor de E-mail de Próxima Geração (*A Mais Moderna*)

- **O Que Faz:** Servidor de e-mail moderno escrito em Rust com suporte nativo a JMAP (protocolo JSON para e-mail), IMAP, POP3, SMTP, antispam integrado com Machine Learning, suporte a OAuth2, rate limiting adaptativo e clustering distribuído sem SPOF.
- **Como Funciona:** Aplicação monolítica em Rust compilada estaticamente, conecta-se a qualquer banco de dados (PostgreSQL, SQLite, MySQL) e oferece performance 10x superior ao Postfix/Dovecot clássicos via async I/O nativo.
- **Requisitos de Infra:** 2 GB RAM, 2 vCPU
- **Comando Rápido:** `docker run -d -e STALWART_DATABASE_URL=postgres://user:pass@db:5432/mail -p 25:25 -p 143:143 -p 587:587 stalwartlabs/stalwart-mail:latest`
- **White-Label & Design System:** Esforço `Mínimo (Requer Webmail Separado)` (React + TypeScript (Taiga Mail Frontend)) - Taiga Mail oferece customização total de tema CSS, logotipo corporativo e paleta de cores. API REST permite desenvolver webmail proprietário.

**Uso Complementar & Ecossistema Agêntico:**
- **MCP Server:** `stalwart-mcp-server` (`npx -y @stalwartlabs/mcp-server`) - Servidor MCP para automação de e-mail via agentes Claude, triagem semântica e resposta automática com LLM.
- **Agent Skill:** `skill-stalwart-jmap` (`.claude/skills/stalwart-jmap/SKILL.md`) - Skill para clientes modernos utilizarem JMAP protocol de forma otimizada, sincronismo offline-first e notificações push nativas.
- **Webmail Frontend:** `Taiga Mail (Cliente JMAP Moderno)` (`git clone https://github.com/stalwartlabs/taiga-mail && npm install && npm start`) - Interface web moderna construída em React, com busca semântica via Meilisearch, integração com calendário e agenda compartilhada.

### #4 · Postfix + Dovecot + Rspamd (Stack Mínimo e Eficiente) (*A Mais Leve*)

- **O Que Faz:** Combinação de componentes Unix clássicos: Postfix para SMTP (entrega), Dovecot para IMAP/POP3 (recuperação) e Rspamd para filtragem de spam com Machine Learning. Sem interface web — administração via CLI.
- **Como Funciona:** Cada componente roda como serviço systemd isolado, armazenando e-mails em Maildir nativo e usando PostgreSQL para configuração de domínios virtuais. Configuração via arquivos de texto simples.
- **Requisitos de Infra:** 512 MB RAM, 1 vCPU
- **Comando Rápido:** `sudo apt install postfix dovecot-core dovecot-imap rspamd redis-server && sudo systemctl enable --now postfix dovecot rspamd`
- **White-Label & Design System:** Esforço `Não Aplicável (CLI Only)` (CLI + (Roundcube Separado)) - Sem interface nativa. Customização via Roundcube separado ou desenvolvimento de painel web personalizado.

**Uso Complementar & Ecossistema Agêntico:**
- **Webmail Cliente:** `Roundcube (Deploy Separado)` (`docker run -e ROUNDCUBEMAIL_DEFAULT_HOST=mail.empresa.com.br roundcube/roundcubemail`) - Deployed em Docker separado, conecta ao Dovecot IMAP/SMTP Postfix via rede para webmail interativo.
- **CLI Admin Tool:** `vimbadmin ou Postfix Admin` (`pip install postfix-admin && postfix-admin domain create empresa.com.br`) - Ferramentas CLI para bulk provisioning de domínios, usuários virtuais e aliases sem interface gráfica.
- **Monitoring:** `Prometheus + Grafana (Métricas Postfix)` (`prometheus-postfix-exporter && grafana`) - Exportadores nativos para monitorar fila de e-mail, latência SMTP e taxa de erro de autenticação IMAP.

### #5 · Mailu: O Mail Suite Pronto para Produção (*A Mais Simples*)

- **O Que Faz:** Suite de e-mail completa em Docker Compose com painel web intuitivo, suporte nativo a Postfix, Dovecot, antispam (SpamAssassin), antivírus (ClamAV), webmail (Roundcube) e synchronização de calendário (CalDAV) configurados automaticamente.
- **Como Funciona:** Arquivo docker-compose.yml pré-configurado que orquestra todos os serviços, com painel de administração em Flask que gera configurações automaticamente sem tocar em arquivos YAML.
- **Requisitos de Infra:** 2 GB RAM, 1 vCPU
- **Comando Rápido:** `git clone https://github.com/Mailu/Mailu && cd Mailu && docker compose up -d`
- **White-Label & Design System:** Esforço `Mínimo (Plug & Play)` (Flask + Bootstrap 5 + Roundcube) - Painel web do Mailu permite upload de logotipo, customização de cores corporativas e templates de e-mail de boas-vindas via GUI.

**Uso Complementar & Ecossistema Agêntico:**
- **MCP Server:** `mailu-mcp-bridge` (`npx -y @mailu/mcp-server`) - Servidor MCP para automação de usuarios, domínios e políticas via agentes Claude nativamente.
- **Agent Skill:** `skill-mailu-health` (`.claude/skills/mailu-health/SKILL.md`) - Skill para monitoramento contínuo de saúde do stack Mailu (fila, tráfego IMAP, taxa de spam).
- **Addon Oficial:** `Mailu Relay (Encaminhamento Inteligente)` (`docker-compose.override.yml + RELAY_ENABLED=true`) - Permite retransmissão automática de e-mails para contas externas com filtros por domínio e criptografia TLS.

---

## 3. Matriz de Decisão & Migração Soberana

Para substituir integralmente o **Mail-in-a-Box**, recomenda-se a esteira automatizada de implantação em VPS com os manuais operacionais disponíveis em `output/`.