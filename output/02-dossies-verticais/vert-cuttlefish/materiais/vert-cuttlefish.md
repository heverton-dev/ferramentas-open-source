# Dossiê Vertical de Desmantelamento SaaS: Cuttlefish (Serviço de Email Transacional SaaS)

> **Padrão Diamante R5-V · Quinteto Soberano Open Source**  
> **Alvo SaaS:** Cuttlefish (Serviço de Email Transacional SaaS) | **Custo Médio:** US$ 25 a US$ 500/mês (conforme volume de envios) | **Risco de Privacidade:** Metadados de transações, registros de clientes e conteúdo de emails armazenados em servidores de terceiros sujeitos a regulações estrangeiras e possível acesso por autoridades.  

---

## 1. O Quinteto Soberano Open Source

| Rank | Classificação | Ferramenta | Licença | Repositório | Economia Estimada |
| :---: | :--- | :--- | :---: | :--- | :--- |
| **#1** | *A Mais Robusta* | **Postal (Stack Enterprise de Email Transacional)** | `MIT` | [https://github.com/postalserver/postal](https://github.com/postalserver/postal) | R$ 15.000/ano |
| **#2** | *A Mais Completa* | **Nodemailer + Mailing Lists Manager (Stack Modular de Email)** | `MIT` | [https://github.com/nodemailer/nodemailer](https://github.com/nodemailer/nodemailer) | R$ 12.000/ano |
| **#3** | *A Mais Moderna* | **Resend (API de Email Transacional Moderna em TypeScript)** | `MIT` | [https://github.com/resendlabs/resend](https://github.com/resendlabs/resend) | R$ 9.000/ano |
| **#4** | *A Mais Leve* | **Exim Mail Server (Servidor Leve com SMTP para Transacional)** | `GPL-2.0` | [https://github.com/Exim/exim](https://github.com/Exim/exim) | R$ 6.000/ano |
| **#5** | *A Mais Simples* | **MailHog (Mock SMTP Server para Desenvolvimento e Staging)** | `MIT` | [https://github.com/mailhog/MailHog](https://github.com/mailhog/MailHog) | R$ 3.600/ano |

---

## 2. Detalhamento Técnico das Ferramentas do Quinteto

### #1 · Postal (Stack Enterprise de Email Transacional) (*A Mais Robusta*)

- **O Que Faz:** Plataforma completa de email transacional com interface web administrativa, API RESTful para envio de emails, sistema de filas confiável, webhooks de entrega em tempo real, templates MJML nativos e analytics de engagement.
- **Como Funciona:** Aplicação Rails com backend em Ruby, armazenamento em PostgreSQL, fila de trabalho assíncrona em Redis/Sidekiq, servidor SMTP para recebimento de bounce emails e painel web para visualização de estatísticas e gerenciamento de domínios.
- **Requisitos de Infra:** 4 GB RAM, 2 vCPU
- **Comando Rápido:** `git clone https://github.com/postalserver/postal && cd postal && docker compose up`
- **White-Label & Design System:** Esforço `Mínimo (Plug & Play)` (Ruby on Rails + ERB + Bootstrap) - Interface do Postal permite ajuste de branding, logotipo corporativo, assinatura de footer padrão e templates de email customizados em HTML/MJML.

**Uso Complementar & Ecossistema Agêntico:**
- **MCP Server:** `postal-mcp-server` (`npx -y @postal/mcp-server`) - Servidor MCP para automatizar envio de emails transacionais, consultar status de entrega e gerenciar templates via agentes de IA.
- **Agent Skill:** `skill-postal-campaign` (`.claude/skills/postal-campaign/SKILL.md`) - Skill para orquestrar campanhas de email transacional em massa com segmentação de lista e tratamento de bounces automático.
- **CLI Tool:** `postal-cli` (`pip install postal-api-cli && postal send usuario@empresa.com --template 'welcome'`) - Ferramenta de linha de comando para teste de templates de email e envio rápido de mensagens transacionais.

### #2 · Nodemailer + Mailing Lists Manager (Stack Modular de Email) (*A Mais Completa*)

- **O Que Faz:** Framework completo de envio de emails em Node.js com suporte nativo a SMTP, SendGrid, Gmail, AWS SES e transports customizados. Integração com Express/NestJS, template engines (EJS, Handlebars, Pug) e fila de trabalho com Bull/BullMQ.
- **Como Funciona:** Módulo npm puro sem dependências pesadas, conectando-se a qualquer servidor SMTP corporativo ou usando transports de provedores. Suporte a streaming de grandes anexos, retry automático com backoff exponencial e tracking de entrega via webhooks.
- **Requisitos de Infra:** 1 GB RAM, 1 vCPU
- **Comando Rápido:** `npm install nodemailer && npm install bullmq redis`
- **White-Label & Design System:** Esforço `Mínimo (Programático)` (JavaScript + Template Engine (Handlebars/EJS)) - Customização via JavaScript puro. Adicione variáveis de empresa, logotipo, cores corporativas e assinatura padrão em templates Handlebars.

**Uso Complementar & Ecossistema Agêntico:**
- **npm Package:** `email-templates` (`npm install email-templates`) - Pacote para renderização de templates de email com suporte a pré-processadores (Pug, EJS) e inlining automático de CSS.
- **Agent Skill:** `skill-nodemailer-relay` (`.claude/skills/nodemailer-relay/SKILL.md`) - Skill para agentes de IA dispararem emails transacionais em resposta a eventos de negócio com confirmação e tratamento de erro.
- **MCP Server:** `nodemailer-mcp` (`npx -y @nodemailer/mcp-server`) - Servidor MCP para orquestração de envios de email e consulta de histórico de entrega via agentes.

### #3 · Resend (API de Email Transacional Moderna em TypeScript) (*A Mais Moderna*)

- **O Que Faz:** SDK TypeScript minimalista e de alto desempenho para envio de emails transacionais. Suporte nativo a JSX para templates de email (React Email) com preview web em tempo real.
- **Como Funciona:** Cliente HTTP assíncrono moderno que se comunica com API REST segura. Suporte a templates em JSX que são renderizados automaticamente para HTML otimizado. Webhooks para eventos de delivery, bounce e complaint.
- **Requisitos de Infra:** 512 MB RAM, 1 vCPU
- **Comando Rápido:** `npm install resend react-email`
- **White-Label & Design System:** Esforço `Mínimo (JSX Nativo)` (React + TypeScript + Tailwind CSS) - Crie componentes React customizados com cores, fonts e logotipo da empresa. Reutilize entre projetos via npm private packages.

**Uso Complementar & Ecossistema Agêntico:**
- **npm Package:** `react-email` (`npm install react-email react react-dom`) - Biblioteca de componentes React reutilizáveis para construir emails com sintaxe JSX moderna.
- **Agent Skill:** `skill-resend-jsx-generator` (`.claude/skills/resend-jsx-generator/SKILL.md`) - Skill para gerar templates de email em JSX automaticamente baseado em requisitos de design corporativo.
- **CLI Tool:** `resend-preview` (`npx react-email preview`) - Ferramenta web para pré-visualização de templates de email em múltiplos clientes (Gmail, Outlook, iPhone).

### #4 · Exim Mail Server (Servidor Leve com SMTP para Transacional) (*A Mais Leve*)

- **O Que Faz:** Servidor SMTP ultrarrápido e modular focado em roteamento inteligente de emails. Perfeito como backend para aplicações que precisam de entrega confiável sem overhead de suíte de email completa.
- **Como Funciona:** Binário compacto em C com configuração flexível via texto plano. Suporte nativo a autenticação SASL, validação DKIM/SPF/DMARC e redirect de emails com base em regras customizadas.
- **Requisitos de Infra:** 128 MB RAM, 1 vCPU
- **Comando Rápido:** `apt-get install exim4 && update-exim4.conf.template && service exim4 restart`
- **White-Label & Design System:** Esforço `Headless (CLI / Programático)` (Nenhuma (Backend / Servidor)) - Customização via arquivo de configuração exim.conf com regras de roteamento, templates de rejeição e políticas de autenticação.

**Uso Complementar & Ecossistema Agêntico:**
- **CLI Tool:** `exim-utils` (`exim -Mrm && exim -bp`) - Conjunto de utilitários de linha de comando para gerenciamento de fila, teste de rotas e auditoria de reputação de IP.
- **Agent Skill:** `skill-exim-queue-monitor` (`.claude/skills/exim-queue-monitor/SKILL.md`) - Skill para monitoramento automático de fila de emails, alertas de falha de entrega e análise de bounces.
- **MCP Server:** `exim-mcp` (`npx -y @exim/mcp-server`) - Servidor MCP para consulta de status de fila e execução de operações administrativas via agentes.

### #5 · MailHog (Mock SMTP Server para Desenvolvimento e Staging) (*A Mais Simples*)

- **O Que Faz:** Servidor SMTP de captura de emails em memória com interface web para visualização de emails enviados durante desenvolvimento e testing. Perfeito para ambientes de staging sem custo de email real.
- **Como Funciona:** Binário único em Go que aceita conexões SMTP na porta 1025 e fornece interface web na porta 8025 para visualizar todos os emails capturados com headers completos e attachments.
- **Requisitos de Infra:** 256 MB RAM, 1 vCPU
- **Comando Rápido:** `docker run -d -p 1025:1025 -p 8025:8025 mailhog/mailhog`
- **White-Label & Design System:** Esforço `Zero (Web Built-in)` (Go + HTML/Bootstrap) - Sem customização visual necessária. Interface é apenas para debugging de emails em desenvolvimento.

**Uso Complementar & Ecossistema Agêntico:**
- **Docker Service:** `mailhog-compose` (`services: mailhog: image: mailhog/mailhog:latest`) - Serviço docker-compose que pode ser compartilhado entre todos os ambientes de desenvolvimento local.
- **Agent Skill:** `skill-mailhog-assertions` (`.claude/skills/mailhog-assertions/SKILL.md`) - Skill para verificar automaticamente se emails esperados foram capturados durante testes end-to-end.
- **REST API:** `mailhog-api` (`curl http://localhost:8025/api/v1/messages`) - API REST nativa para consultar emails capturados programaticamente em testes automatizados.

---

## 3. Matriz de Decisão & Migração Soberana

Para substituir integralmente o **Cuttlefish (Serviço de Email Transacional SaaS)**, recomenda-se a esteira automatizada de implantação em VPS com os manuais operacionais disponíveis em `output/`.