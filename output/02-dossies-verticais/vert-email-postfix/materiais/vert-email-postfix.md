# Dossiê Vertical de Desmantelamento SaaS: Gmail for Business / Microsoft 365 / ProtonMail Business (Email & Collaboration)

> **Padrão Diamante R5-V · Quinteto Soberano Open Source**  
> **Alvo SaaS:** Gmail for Business / Microsoft 365 / ProtonMail Business (Email & Collaboration) | **Custo Médio:** US$ 60 a US$ 250/mês por usuário (cobrança mensalidade fixa + add-ons de storage e segurança) | **Risco de Privacidade:** Emails corporativos processados por máquinas de IA do fornecedor, análise de conteúdo para fins de publicidade direcionada, acesso governamental via órgãos reguladores e criptografia de ponta-a-ponta limitada ou desativada por padrão.  

---

## 1. O Quinteto Soberano Open Source

| Rank | Classificação | Ferramenta | Licença | Repositório | Economia Estimada |
| :---: | :--- | :--- | :---: | :--- | :--- |
| **#1** | *A Mais Robusta* | **Postfix + Dovecot + Roundcube (A Stack Corporativa Padrão de Ouro)** | `IPL-1.0 (Postfix), LGPL-2.1 (Dovecot), GPL-3.0 (Roundcube)` | [https://github.com/postfix/postfix (mirror) + https://github.com/dovecot/core + https://github.com/roundcube/roundcubemail](https://github.com/postfix/postfix (mirror) + https://github.com/dovecot/core + https://github.com/roundcube/roundcubemail) | R$ 22.000/ano |
| **#2** | *A Mais Completa* | **SOGo (Servidor de Email & Colaboração Integrado)** | `LGPL-2.0+` | [https://github.com/Alinto/sogo](https://github.com/Alinto/sogo) | R$ 18.000/ano |
| **#3** | *A Mais Moderna* | **Mailcow: Dockerized (Stack Completa em Docker com UI Moderna)** | `GPL-3.0` | [https://github.com/mailcow/mailcow-dockerized](https://github.com/mailcow/mailcow-dockerized) | R$ 16.000/ano |
| **#4** | *A Mais Leve* | **Modoboa (Suite Leve de Email em Python & Django)** | `ISC License` | [https://github.com/modoboa/modoboa](https://github.com/modoboa/modoboa) | R$ 8.000/ano |
| **#5** | *A Mais Simples* | **Mail-in-a-Box (Script de Instalação Automatizada de Email Corporativo)** | `CC0 1.0 (Public Domain) + Scripts GPL-3.0` | [https://github.com/mail-in-a-box/mailinabox](https://github.com/mail-in-a-box/mailinabox) | R$ 3.600/ano |

---

## 2. Detalhamento Técnico das Ferramentas do Quinteto

### #1 · Postfix + Dovecot + Roundcube (A Stack Corporativa Padrão de Ouro) (*A Mais Robusta*)

- **O Que Faz:** Pilares modulares de um servidor de email corporativo de classe enterprise: Postfix (MTA — Mail Transfer Agent) para roteamento e entrega segura, Dovecot (IMAP/POP3 server) para acesso de clientes remotos com criptografia TLS, e Roundcube (webmail responsivo) para leitura de emails no navegador.
- **Como Funciona:** Arquitetura POSIX clássica e testada há 25 anos em datacenters do mundo inteiro. Postfix valida SMTP autêntico, Dovecot mantém o estado da caixa de correio em formato Maildir/mbox com índices de alta performance, e Roundcube oferece interface web moderna com suporte a drafts, templates e plugins. Integração nativa com SPF, DKIM, DMARC e certificados Let's Encrypt para conformidade com padrões de segurança de email.
- **Requisitos de Infra:** 2 GB RAM, 2 vCPU
- **Comando Rápido:** `apt-get install postfix dovecot-imapd dovecot-pop3d roundcube roundcube-sqlite3 && dpkg-reconfigure postfix`
- **White-Label & Design System:** Esforço `Moderado (Configuração POSIX Clássica)` (Roundcube (PHP) + jQuery + Responsive CSS) - Roundcube suporta plugins e skins customizadas sem limite, permitindo branding corporativo total com logo e cores oficiais.

**Uso Complementar & Ecossistema Agêntico:**
- **MCP Server:** `postfix-dovecot-mcp` (`https://github.com/your-org/postfix-dovecot-mcp (servidor MCP customizado)`) - Servidor MCP que expõe operações de administração de email (criar usuário, excluir, resetar senha, quotas) para agentes de IA da empresa.
- **LDAP/ActiveDirectory:** `dovecot-ldap-auth` (`Dovecot LDAP passdb + userdb para autenticação corporativa`) - Integração nativa com LDAP/ActiveDirectory da empresa para sincronização automática de usuários sem manutenção manual de contas.
- **Antispam Plugin:** `spamassassin-rspamd` (`Postfix policy service com Rspamd (Apache-2.0)`) - Filtragem de spam corporativo baseada em machine learning, URLs maliciosas e comportamento de padrão de botnets.
- **Backup Cifrado:** `postfix-backup-gpg` (`Cronie + GPG + Tar para backup automático com criptografia`) - Backup diário de todos os Maildir para repositório S3/MinIO corporativo com criptografia de ponta-a-ponta.

### #2 · SOGo (Servidor de Email & Colaboração Integrado) (*A Mais Completa*)

- **O Que Faz:** Suite de colaboração corporativa que combina email (IMAP/POP3), calendário compartilhado (CalDAV), contatos (CardDAV), tarefas e webmail responsivo em um único servidor autohospedado. SOGo funciona como frontend web moderno sobre Postfix/Dovecot existentes ou com seu próprio backend de email.
- **Como Funciona:** Escrito em Objective-C com backend em PostgreSQL/MySQL, SOGo oferece interface web intuitiva similar ao Outlook Online. Suporta sincronização de dispositivos móveis via CalDAV/CardDAV, compartilhamento de calendários entre usuários corporativos e integração com clientes desktop (Thunderbird, macOS Mail, Outlook Desktop via CalDAV/CardDAV).
- **Requisitos de Infra:** 4 GB RAM, 2 vCPU
- **Comando Rápido:** `apt-get install sogo sogo-frontends sogo-ealarms-notify + docker run -d -p 20000:20000 sogoteam/sogo:latest`
- **White-Label & Design System:** Esforço `Moderado (Interface Moderna)` (JavaScript (DHTML/AJAX) + Responsive Design) - SOGo suporta temas customizados e branding corporativo com logo, cores e domínio próprio.

**Uso Complementar & Ecossistema Agêntico:**
- **MCP Server:** `sogo-mcp-calendar` (`API REST de SOGo exposta via servidor MCP`) - Agentes de IA podem ler calendários corporativos, sugerir slots de reunião e agendar automaticamente.
- **Sync Móvel:** `sogo-mobile-sync` (`CalDAV/CardDAV suportados nativamente em iOS, Android e Windows Phone`) - Sincronização bidirecional de calendários e contatos corporativos em qualquer dispositivo móvel.
- **Integração Zapier Open Source:** `n8n-sogo-connector` (`https://github.com/n8n-io/n8n (workflow automation open source)`) - Automações complexas entre SOGo e ferramentas corporativas (Slack, CRM, ERP) sem depender de Zapier pago.
- **WebDAV/CalDAV Bridge:** `nextcloud-sogo-sync` (`Integração bidirecional entre Nextcloud e SOGo`) - Compartilhamento de arquivos corporativos sincronizado com calendários e contatos.

### #3 · Mailcow: Dockerized (Stack Completa em Docker com UI Moderna) (*A Mais Moderna*)

- **O Que Faz:** Suite completa de email em containers Docker que integra Postfix, Dovecot, Roundcube, SOGo, Rspamd (antispam) e ferramentas de administração com interface web moderna e intuitiva. Oferece gestão de usuários, quotas, SPF/DKIM/DMARC via UI, e backup automático.
- **Como Funciona:** Orquestração de containers Docker Compose com cada serviço em seu próprio container. Interface de administração escrita em PHP/MySQL permite gerenciar todos os aspectos do servidor de email sem SSH direto. Implementa lógica automática de renovação de certificados SSL, filtragem de spam com machine learning e integração com soluções de backup externas.
- **Requisitos de Infra:** 6 GB RAM, 4 vCPU
- **Comando Rápido:** `git clone https://github.com/mailcow/mailcow-dockerized && cd mailcow-dockerized && ./generate_config.sh && docker compose up -d`
- **White-Label & Design System:** Esforço `Mínimo (Containerizado & Web UI)` (PHP + MySQL + Responsive Bootstrap) - Interface é funcional e profissional, mas não suporta branding corporativo nativo (possível via fork do código).

**Uso Complementar & Ecossistema Agêntico:**
- **MCP Server:** `mailcow-mcp-admin` (`API REST de administração de Mailcow exposta via servidor MCP`) - Agentes de IA podem provisionar usuários, resetar senhas e gerar relatórios de uso diretamente.
- **Backup Automático:** `mailcow-backup-s3` (`Script de backup usando S3/MinIO corporativo com criptografia GPG`) - Backups diários de todos os mailboxes criptografados em repositório S3 próprio da empresa.
- **Monitoring & Alertas:** `prometheus-mailcow-exporter` (`Exportador Prometheus para métricas de email (fila, disk, conexões IMAP)`) - Integração com Prometheus + Grafana para visualizar saúde do servidor de email em tempo real.
- **Logging Centralizado:** `mailcow-loki-shipper` (`Envio de logs para Loki (observabilidade Stack Grafana)`) - Logs de Postfix, Dovecot e Rspamd centralizados para auditoria e troubleshooting.

### #4 · Modoboa (Suite Leve de Email em Python & Django) (*A Mais Leve*)

- **O Que Faz:** Suite de email totalmente escrita em Python/Django que oferece Postfix + Dovecot + Webmail + Painel de administração com footprint mínimo de RAM. Ideal para empresas pequenas, startups ou infraestruturas com recursos limitados.
- **Como Funciona:** Aplicação Django monolítica que gerencia configuração de Postfix/Dovecot via ORM e oferece webmail responsivo minimalista. Consome menos de 500MB de RAM em produção e oferece todos os recursos essenciais (criar usuários, quotas, antispam) via interface.
- **Requisitos de Infra:** 1 GB RAM, 1 vCPU
- **Comando Rápido:** `pip install modoboa && modoboa deploy --collectstatic production_folder && python production_folder/manage.py runserver 0.0.0.0:8000`
- **White-Label & Design System:** Esforço `Mínimo (Interface Bootstrap Padrão)` (Django Templates + Bootstrap 5) - Skins customizados via Django templates simples, permitindo branding corporativo sem modificar código Python.

**Uso Complementar & Ecossistema Agêntico:**
- **Django Package:** `modoboa-webmail-lite` (`Extensão leve de webmail com integração de plugins`) - Suporte nativo para temas customizados e plugins Django para recursos adicionais.
- **Agent Skill:** `skill-modoboa-provisioning` (`.claude/skills/modoboa-provisioning/SKILL.md`) - Skill para agentes de IA criarem usuários de email sob demanda sem acessar SSH diretamente.
- **Monitoring Leve:** `modoboa-health-check` (`Endpoint /health para verificação de status em load balancers`) - Integração com monitoramento leve para alertas de queda do serviço.
- **Rate Limiting:** `modoboa-ratelimit-plugin` (`Plugin Django nativo para limitar taxa de envios SMTP`) - Proteção contra abuso de email com quotas de envio por usuário configuráveis.

### #5 · Mail-in-a-Box (Script de Instalação Automatizada de Email Corporativo) (*A Mais Simples*)

- **O Que Faz:** Bash script que automatiza completamente a instalação e configuração de um servidor de email corporativo em uma máquina Ubuntu/Debian limpa. Você roda um comando e em 30 minutos tem email funcionando com SSL/TLS, SPF, DKIM, DMARC, webmail, cardápio de gerenciamento e backups automáticos.
- **Como Funciona:** O script detecta o seu ambiente, instala Postfix, Dovecot, Roundcube, Spamassassin, integra com Let's Encrypt e oferece painel web de gerenciamento simplificado escrito em JavaScript/Node.js. Sem configuração manual de POSIX ou edição de arquivos — tudo é gerenciado por UI intuitiva.
- **Requisitos de Infra:** 512 MB RAM, 1 vCPU
- **Comando Rápido:** `curl https://mailinabox.email/setup.sh | sudo bash`
- **White-Label & Design System:** Esforço `Nenhum (Totalmente Automatizado)` (Node.js + Bootstrap + Responsive Design) - Interface não é customizável sem fork do projeto, mas é profissional o suficiente para uso corporativo direto.

**Uso Complementar & Ecossistema Agêntico:**
- **DNS Automático:** `mailinabox-dns-sync` (`API nativa para verificar registros SPF/DKIM/DMARC necessários`) - Painel exibe exatamente quais registros de DNS você precisa adicionar no seu registrador.
- **Backup Automático:** `mailinabox-s3-backup` (`Integração com S3/B2 para backups diários automáticos criptografados`) - Sem necessidade de SSH; backups configuráveis pelo painel com retenção automática.
- **Monitoramento Simples:** `mailinabox-status-page` (`Endpoint de status HTTP para ping externo`) - Página de status pública e privada mostrando saúde geral do servidor.
- **WebDAV:** `mailinabox-nextcloud-bridge` (`Integração opcional com Nextcloud para compartilhamento de arquivos corporativo`) - Oferece compartilhamento de arquivos integrado com email sem ferramentas externas.

---

## 3. Matriz de Decisão & Migração Soberana

Para substituir integralmente o **Gmail for Business / Microsoft 365 / ProtonMail Business (Email & Collaboration)**, recomenda-se a esteira automatizada de implantação em VPS com os manuais operacionais disponíveis em `output/`.