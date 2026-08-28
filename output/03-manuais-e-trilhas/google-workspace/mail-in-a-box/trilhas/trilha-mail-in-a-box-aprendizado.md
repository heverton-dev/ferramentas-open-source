# Trilha Cronológica de Aprendizado: Mail-in-a-Box (Self-Hosted Email Server Solution)

> **Jornada Pedagógica Autoguiada · Imersão a Partir das Fontes Primárias** 
> **Tempo Total Estimado:** 8 horas de imersao guiada | **Fases:** 5 Módulos 
> **Dossiê SaaS de Origem:** Google-Workspace

---

## Fase 1: Fundamentos de Email & Protocolos SMTP/IMAP (`⏱ 1h 30min`)
** Meta da Etapa:** Entender os principios de comunicacao email e por que Mail-in-a-Box supera servicos cloud.

- [ ] **[Mail-in-a-Box Official Architecture & Documentation](https://github.com/mail-in-a-box/mailinabox)** (`Documentacao Oficial` - `[F01]`)
 - **O que você aprende:** Arquitetura Postfix, Dovecot, certificados SSL/TLS
 - ⏱ 45 min | Joshua Tate & Contributors

- [ ] **[SMTP & IMAP Protocol Deep Dive](https://datatracker.ietf.org/doc/html/rfc5321)** (`Artigo Tecnico` - `[F02]`)
 - **O que você aprende:** Como email viaja na internet e seguranca
 - ⏱ 45 min | IETF Standards

## Fase 2: Instalacao de Mail-in-a-Box em VPS & Setup Inicial (`⏱ 2h 00min`)
** Meta da Etapa:** Deploy completo em VPS, configuracao de dominio e primeiro usuario.

- [ ] **[Mail-in-a-Box Quick Start Guide](https://mailinabox.email/)** (`Tutorial Pratico` - `[F03]`)
 - **O que você aprende:** Script automatizado, configuracao DNS, criacao admin
 - ⏱ 1h30 pratica | Mail-in-a-Box Documentation

- [ ] **[DNS Configuration & Domain Pointing](https://www.icann.org/resources/pages/domain-registry-2013-12-02-en)** (`Lab Interativo` - `[F04]`)
 - **O que você aprende:** Apontar A, MX, TXT records para sua VPS
 - ⏱ 30 min pratica | ICANN & Registradores

## Fase 3: Autenticacao de Email & SPF/DKIM/DMARC (`⏱ 1h 30min`)
** Meta da Etapa:** Configurar certificados de autenticacao para evitar spam.

- [ ] **[SPF, DKIM & DMARC Configuration Guide](https://dmarc.org/)** (`Documentacao Oficial` - `[F05]`)
 - **O que você aprende:** Certificados que provam identidade do servidor
 - ⏱ 1h | DMARC.org & Email Security Community

- [ ] **[Testing Email Deliverability & Reputation](https://mxtoolbox.com/spf.aspx)** (`Lab Pratico` - `[F06]`)
 - **O que você aprende:** Validar que emails nao caem em spam
 - ⏱ 30 min | Email Deliverability Experts

## Fase 4: Monitoramento, Backups & Manutencao de Producao (`⏱ 1h 30min`)
** Meta da Etapa:** Implementar backup automatico e monitoramento de saude.

- [ ] **[Mail-in-a-Box Backup & Disaster Recovery](https://github.com/mail-in-a-box/mailinabox#backup)** (`Guia de Operacoes` - `[F07]`)
 - **O que você aprende:** Estrategia de backup e recovery
 - ⏱ 45 min | Mail-in-a-Box Team

- [ ] **[Monitoring Linux Services & Email Logs](https://www.linux.org/)** (`Tutorial DevOps` - `[F08]`)
 - **O que você aprende:** Detectar problemas antes de afetar usuarios
 - ⏱ 45 min | Linux Foundation & DevOps Community

## Fase 5: Migracao de Servicos Cloud & Casos de Uso Avancados (`⏱ 1h 30min`)
** Meta da Etapa:** Migrar usuarios de Google Workspace com zero downtime.

- [ ] **[Migracao Zero-Downtime de Email Cloud para Self-Hosted](https://github.com/mail-in-a-box/mailinabox/wiki/Migrating-from-Google-Workspace)** (`Playbook Operacional` - `[F09]`)
 - **O que você aprende:** Blue-green deploy, validacao DNS, monitoramento
 - ⏱ 1h | AIDD - Arsenal Open Source

- [ ] **[Casos de Uso Avancados: Listas, Aliases & Catch-All](https://mailinabox.email/guide.html)** (`Laboratorio Pratico` - `[F10]`)
 - **O que você aprende:** Expandir funcionalidade alem de usuarios simples
 - ⏱ 30 min | Mail-in-a-Box Community
