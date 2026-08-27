# Dossiê Vertical de Desmantelamento SaaS: Modoboa (Self-Hosted Email Management & Webmail)

> **Padrão Diamante R5-V · Quinteto Soberano Open Source**  
> **Alvo SaaS:** Modoboa (Self-Hosted Email Management & Webmail) | **Custo Médio:** R$ 24.000 a R$ 120.000/ano (planos escaláveis por número de domínios e usuários, gestão de licenças comerciais) | **Risco de Privacidade:** Conteúdo completo de emails, metadados de comunicação, dados de calendário, contatos sincronizados e histórico de conversas armazenados em servidores proprietários na nuvem de terceiros sem garantia de criptografia fim-a-fim ou conformidade LGPD.  

---

## 1. O Quinteto Soberano Open Source

| Rank | Classificação | Ferramenta | Licença | Repositório | Economia Estimada |
| :---: | :--- | :--- | :---: | :--- | :--- |
| **#1** | *A Mais Robusta* | **Modoboa (Email Server & Webmail Completo)** | `ISC` | [https://github.com/modoboa/modoboa](https://github.com/modoboa/modoboa) | R$ 96.000/ano |
| **#2** | *A Mais Completa* | **Apache James (Enterprise Mail Server & Storage)** | `Apache-2.0` | [https://github.com/apache/james-project](https://github.com/apache/james-project) | R$ 120.000/ano |
| **#3** | *A Mais Moderna* | **Postal (Modern Cloud-Ready Email Server)** | `MIT` | [https://github.com/postalserver/postal](https://github.com/postalserver/postal) | R$ 72.000/ano |
| **#4** | *A Mais Leve* | **Maddy Mail Server (Minimal, Zero-Config Email)** | `GPL-3.0` | [https://github.com/foxcpp/maddy](https://github.com/foxcpp/maddy) | R$ 36.000/ano |
| **#5** | *A Mais Simples* | **MailCatcher (Developer Mock Mail Server)** | `MIT` | [https://github.com/sj26/mailcatcher](https://github.com/sj26/mailcatcher) | R$ 6.000/ano |

---

## 2. Detalhamento Técnico das Ferramentas do Quinteto

### #1 · Modoboa (Email Server & Webmail Completo) (*A Mais Robusta*)

- **O Que Faz:** Plataforma completa de email com servidor SMTP/IMAP/POP3 integrado, webmail interativo tipo Gmail, calendário CalDAV, contatos CardDAV, gerenciamento de domínios, filtros Sieve, antispam Rspamd, backup automatizado e autenticação LDAP/OAuth2.
- **Como Funciona:** Desenvolvido em Python/Django com componentes Postfix (MTA), Dovecot (IMAP), ClamAV (antivírus) orquestrados em Docker Compose, interface web responsiva com sincronização bidirecionalmente com clientes desktop (Thunderbird, Outlook) e móvel (IMAP).
- **Requisitos de Infra:** 2 GB RAM, 2 vCPUs
- **Comando Rápido:** `git clone https://github.com/modoboa/modoboa.git && cd modoboa && docker-compose up -d`
- **White-Label & Design System:** Esforço `Médio` (Bootstrap + Vue.js / Responsive Webmail) - Customização visual via CSS, temas customizáveis e plugins Python para extensão de funcionalidade.

**Uso Complementar & Ecossistema Agêntico:**
- **Servidor MCP:** `mcp-modoboa-email` (`pip install mcp-modoboa-integration`) - Permite que agentes IA leiam, classifiquem e respondam emails diretamente via Tool Calling.
- **Plugin:** `radicale-caldav-sync` (`pip install radicale`) - Servidor CalDAV/CardDAV separado sincronizado com Modoboa para calendário e contatos remotos.

### #2 · Apache James (Enterprise Mail Server & Storage) (*A Mais Completa*)

- **O Que Faz:** Servidor de email corporativo de altíssima performance com suporte a SMTP, IMAP, POP3, ManageSieve, armazenamento distribuído com Cassandra/RabbitMQ, clustering automático, filtros de segurança avançados e conformidade com padrões internacionais.
- **Como Funciona:** Desenvolvido em Java com arquitetura de microsserviços nativa para nuvem, suporte a sharding de mailboxes, redundância de dados, API REST para automação administrativa e integração com Kerberos para autenticação corporativa.
- **Requisitos de Infra:** 4 GB RAM, 4 vCPUs
- **Comando Rápido:** `docker run -d -p 25:25 -p 143:143 -p 110:110 --name james apache/james:latest`
- **White-Label & Design System:** Esforço `Médio` (Admin REST API + CLI Tools) - Configuração via YAML, extensão via Java plugins e integração com qualquer webmail externo (RoundCube, Kopano).

**Uso Complementar & Ecossistema Agêntico:**
- **Servidor MCP:** `mcp-james-admin` (`pip install mcp-apache-james-ops`) - Auditoria, provisionamento de usuários e monitoramento de quotas de storage via Agent IA.
- **Plugin:** `dovecot-sieve-filters` (`apt-get install dovecot-sieve`) - Motor de filtros avançados Sieve para organização automática de emails por regras de negócio.

### #3 · Postal (Modern Cloud-Ready Email Server) (*A Mais Moderna*)

- **O Que Faz:** Servidor SMTP de nova geração desenvolvido nativamente para containers e cloud, com suporte a webhooks em tempo real, API REST para envio transacional, analytics integrado de deliverabilidade, autenticação SPF/DKIM/DMARC automática e interface web moderna.
- **Como Funciona:** Escrito em Ruby on Rails com arquitetura cloud-native, stateless, escalável horizontalmente em Kubernetes, suporte a múltiplas organizações e domínios de saída com reputação de IP isolada.
- **Requisitos de Infra:** 2 GB RAM, 2 vCPUs
- **Comando Rápido:** `docker run -d -p 5000:5000 -e DOCKER_GATEWAY_HOST=172.17.0.1 --name postal postalhq/postal:latest`
- **White-Label & Design System:** Esforço `Baixo` (Rails + Vue.js / Modern Web Dashboard) - Interface web minimalista e configurável, webhooks para eventos customizados e suporte a plugins.

**Uso Complementar & Ecossistema Agêntico:**
- **Servidor MCP:** `mcp-postal-gateway` (`npm install @postal/mcp-gateway`) - Integração de agentes IA para envio de emails transacionais automáticos e leitura de eventos de bounce/complaint.

### #4 · Maddy Mail Server (Minimal, Zero-Config Email) (*A Mais Leve*)

- **O Que Faz:** Servidor SMTP/IMAP minimalista porém completo desenvolvido em Go, com zero dependências externas, suporte nativo a DANE/MTA-STS para segurança de email, armazenamento local simples e configuração declarativa YAML.
- **Como Funciona:** Compilado em binário único Go sem Python, Ruby ou dependências pesadas, consome menos de 50 MB de RAM, oferece acesso IMAP puro para integração com Thunderbird/Evolution e suporte a TLS automático via Let's Encrypt.
- **Requisitos de Infra:** 256 MB RAM, 0.5 vCPU
- **Comando Rápido:** `docker run -d -p 25:25 -p 143:143 -e MADDY_DOMAIN=seu-dominio.com --name maddy foxcpp/maddy:latest`
- **White-Label & Design System:** Esforço `Mínimo` (CLI + YAML Configuration) - Configuração 100% YAML sem interface web, extensível via middleware chain.

**Uso Complementar & Ecossistema Agêntico:**
- **Servidor MCP:** `mcp-maddy-sieve` (`pip install mcp-maddy-automation`) - Filtros Sieve programáveis para organização automática de emails via regras IA.

### #5 · MailCatcher (Developer Mock Mail Server) (*A Mais Simples*)

- **O Que Faz:** Servidor SMTP e webmail simplificado para captura de emails em ambientes de desenvolvimento e teste, sem necessidade de servidor de email real ou credenciais SMTP.
- **Como Funciona:** Desenvolvido em Ruby com interface web leve que armazena emails em memória ou SQLite, API REST para asserções em testes automatizados e suporte a limpeza de mensagens.
- **Requisitos de Infra:** 64 MB RAM, 0.25 vCPU
- **Comando Rápido:** `docker run -d -p 1025:1025 -p 1080:1080 --name mailcatcher schickling/mailcatcher`
- **White-Label & Design System:** Esforço `Mínimo` (Simple Web UI / No Styling) - Interface sem necessidade de customização.

**Uso Complementar & Ecossistema Agêntico:**
- **Plugin:** `mailcatcher-cypress-testing` (`npm install cypress-mailcatcher-plugin`) - Plugin Cypress para validação automática de emails de confirmação em testes E2E.

---

## 3. Matriz de Decisão & Migração Soberana

Para substituir integralmente o **Modoboa (Self-Hosted Email Management & Webmail)**, recomenda-se a esteira automatizada de implantação em VPS com os manuais operacionais disponíveis em `output/`.