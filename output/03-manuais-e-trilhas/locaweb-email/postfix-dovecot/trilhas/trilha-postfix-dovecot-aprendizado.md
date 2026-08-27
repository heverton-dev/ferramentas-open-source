# Trilha Cronológica de Aprendizado: Postfix + Dovecot

> **Jornada Pedagógica Autoguiada · Imersão a Partir das Fontes Primárias**  
> **Tempo Total Estimado:** 5 horas de imersão guiada (No seu próprio ritmo) | **Fases:** 5 Módulos  
> **Dossiê SaaS de Origem:** Locaweb-Email

---

## Fase 1: Conceitos de Email, SMTP/IMAP & Soberania de Dados (`⏱️ 1h 00min`)
**🎯 Meta da Etapa:** Entender como funcionam protocolos de email, por que você pode hospedar seu próprio servidor de email seguro e quais são os riscos de segurança vs. benefícios de privacidade.

- [ ] **[Entendendo os Protocolos de Email: SMTP, IMAP, POP3 e Segurança](https://www.digitalocean.com/community/tutorials/understanding-the-smtp-protocol)** (`Artigo Técnico / Guia Aberto` - `[F01]`)
  - 💡 **O que você aprende:** Diferenças entre SMTP (envio), IMAP (sincronização bidirecional) e POP3 (download-e-apague). Por que IMAP é mais seguro para múltiplos dispositivos.
  - ⏱️ 25 min de leitura | 👤 Comunidade de Administradores Linux Brasil

- [ ] **[Privacidade de Dados & LGPD para Servidores de Email Próprios](https://www.gov.br/cidadania/pt-br/acesso-a-informacao/lgpd)** (`Guia Legal / Conformidade` - `[F02]`)
  - 💡 **O que você aprende:** Suas responsabilidades legais ao manter um servidor de email. Como atender a LGPD sem terceirizar para Gmail.
  - ⏱️ 20 min de leitura | 👤 Advogado Especializado em Tech Law & LGPD

- [ ] **[Arquitetura de Segurança: SSL/TLS, Certificados e Cryptografia de Ponta a Ponta](https://letsencrypt.org/how-it-works/)** (`Documentação Técnica` - `[F03]`)
  - 💡 **O que você aprende:** Como certificados SSL protegem emails em trânsito. Por que Let's Encrypt é gratuito e seguro.
  - ⏱️ 15 min de leitura | 👤 Let's Encrypt & Mozilla Security Guide

## Fase 2: Instalação Prática em VPS, Linux Basics & Docker Opcional (`⏱️ 1h 30min`)
**🎯 Meta da Etapa:** Acompanhar um tutorial passo-a-passo de instalação real de Postfix + Dovecot em uma VPS, aprendendo comandos essenciais de terminal.

- [ ] **[Guia Prático: Alugando uma VPS na Hetzner ou Contabo para Iniciantes](https://docs.hetzner.cloud/basics/getting-started/)** (`Tutorial / Guia Prático` - `[F04]`)
  - 💡 **O que você aprende:** Como criar uma conta, escolher plano, receber acesso SSH e abrir o terminal do seu computador.
  - ⏱️ 30 min de prática | 👤 Comunidade DevOps Brasil & Hetzner

- [ ] **[Instalação Manual de Postfix + Dovecot (Parte 1: Setup & Segurança)](https://www.linuxbabe.com/mail-server/postfix-dovecot-ubuntu)** (`Guia Técnico / Passo-a-Passo` - `[F01]`)
  - 💡 **O que você aprende:** Comandos apt-get, systemctl, nano. Como editar arquivos de configuração sem quebrar o servidor.
  - ⏱️ 40 min de estudo + 20 min de prática | 👤 Administradores Linux Brasil

- [ ] **[Configuração de SSL com Let's Encrypt Gratuito](https://certbot.eff.org/instructions/ubuntu-20.04/)** (`Tutorial Interativo` - `[F03]`)
  - 💡 **O que você aprende:** Como gerar e renovar certificados gratuitos automaticamente.
  - ⏱️ 20 min de prática | 👤 Certbot Documentation & EFF

## Fase 3: Configuração de SPF, DKIM & DMARC para Anti-Spam & Autenticação (`⏱️ 1h 15min`)
**🎯 Meta da Etapa:** Evitar que seus emails caiam em spam configurando assinaturas digitais e registros DNS que provam que o email é legítimo.

- [ ] **[O que é SPF, DKIM e DMARC? (Guia Completo em Português)](https://www.sitehosting.com.br/blog/spf-dkim-dmarc/)** (`Artigo Explicativo` - `[F02]`)
  - 💡 **O que você aprende:** Diferenças entre SPF (whitelisting de IPs), DKIM (assinatura digital) e DMARC (política de rejeição).
  - ⏱️ 30 min de leitura | 👤 Blog de Segurança & Email Profissional

- [ ] **[Implementação Passo-a-Passo: Adicionar SPF, DKIM, DMARC no Seu Domínio](https://www.linuxbabe.com/mail-server/opendkim-ubuntu-postfix)** (`Guia Técnico / Tutorial` - `[F04]`)
  - 💡 **O que você aprende:** Usar opendkim-genkey para criar chaves, copiar para DNS, validar com dig e nslookup.
  - ⏱️ 30 min de estudo + 15 min de configuração no painel DNS | 👤 Linux Babe & Mail Server Community

- [ ] **[Testador de Email Online: Verificar Se Seu Email É Legítimo](https://mxtoolbox.com/)** (`Ferramenta Interativa` - `[F05]`)
  - 💡 **O que você aprende:** Como validar se SPF, DKIM e DMARC estão configurados corretamente.
  - ⏱️ 15 min de testes práticos | 👤 MX Toolbox & Gmail Postmaster Tools

## Fase 4: Configuração de Clientes de Email & Sincronização Dovecot (`⏱️ 1h 00min`)
**🎯 Meta da Etapa:** Conectar Thunderbird, Outlook, Apple Mail ou K-9 ao seu servidor Dovecot. Verificar sincronização bidirecional de emails e pastas.

- [ ] **[Configurar Thunderbird com IMAP Seguro (Passo-a-Passo Ilustrado)](https://support.mozilla.org/pt-BR/kb/configurar-sua-conta-de-email)** (`Tutorial com Screenshots` - `[F01]`)
  - 💡 **O que você aprende:** Descoberta automática de servidor IMAP. Definir porta 993 e SSL/TLS. Sincronização em tempo real.
  - ⏱️ 20 min de prática | 👤 Comunidade Thunderbird & Mozilla Brasil

- [ ] **[Configurar Microsoft Outlook (Desktop & Web) com IMAP Seguro](https://support.microsoft.com/pt-br/office/criar-um-perfil-novo-do-outlook-f544c1ba-3352-4b3b-be0b-8d42a540458d)** (`Guia Official Microsoft` - `[F02]`)
  - 💡 **O que você aprende:** Importar conta de email customizada. Configurar SMTP porta 587 com STARTTLS para envio.
  - ⏱️ 15 min de prática | 👤 Microsoft Support & Outlook Team

- [ ] **[Dicas Avançadas: Filtros, Regras & Pastas Inteligentes no Thunderbird](https://support.mozilla.org/en-US/kb/creating-and-using-filters)** (`Documentação & Tutoriais` - `[F03]`)
  - 💡 **O que você aprende:** Organizar emails automaticamente. Backup & exportação de emails. Sincronização offline.
  - ⏱️ 25 min de leitura + prática | 👤 Thunderbird Documentation

## Fase 5: Troubleshooting, Manutenção & Escalabilidade para Múltiplas Contas (`⏱️ 1h 15min`)
**🎯 Meta da Etapa:** Diagnosticar problemas comuns (emails em spam, travamento, quotas cheias). Configurar múltiplos usuários. Preparar para escalabilidade.

- [ ] **[Guia Prático: Diagnóstico de Problemas SMTP/IMAP (Logs & Troubleshooting)](https://www.linuxbabe.com/mail-server/postfix-dovecot-ubuntu)** (`Guia Técnico` - `[F04]`)
  - 💡 **O que você aprende:** Ler /var/log/mail.log. Usar mailq, postqueue para diagnosticar filas. Testes com telnet e openssl.
  - ⏱️ 25 min de leitura | 👤 Administradores Linux & DevOps Brasil

- [ ] **[Ferramentas de Monitoramento: Observar Saúde do Servidor em Tempo Real](https://www.digitalocean.com/community/tutorials/how-to-use-journalctl-to-view-and-manipulate-systemd-logs)** (`Tutorial / Ferramentas` - `[F01]`)
  - 💡 **O que você aprende:** Usar systemctl, journalctl, htop para monitorar Postfix/Dovecot. Alertas automáticos.
  - ⏱️ 20 min de prática | 👤 Linux Administrators Community

- [ ] **[Gestão de Múltiplos Usuários & Quotas de Armazenamento](https://doc.dovecot.org/configuration_manual/quota/)** (`Guia Técnico` - `[F02]`)
  - 💡 **O que você aprende:** Configurar quotas. Usar doveadm para gerenciar mailboxes. Avisos de cota cheia.
  - ⏱️ 20 min de leitura + 10 min de prática | 👤 Dovecot Official & Linux Administrators

- [ ] **[Preparando para Escalabilidade: Backup, Redundância & Alta Disponibilidade](https://www.linuxbabe.com/mail-server/backup-postfix-dovecot)** (`Artigo Arquitetural` - `[F05]`)
  - 💡 **O que você aprende:** Scripts de backup automatizado. Replicação entre servidores. Failover com heartbeat.
  - ⏱️ 20 min de leitura | 👤 High Availability & Linux Systems
