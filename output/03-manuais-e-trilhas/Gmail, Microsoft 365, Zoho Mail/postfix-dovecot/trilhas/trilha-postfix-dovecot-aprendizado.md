# Trilha Cronológica de Aprendizado: Postfix + Dovecot

> **Jornada Pedagógica Autoguiada · Imersão a Partir das Fontes Primárias**  
> **Tempo Total Estimado:** 5 horas de imersao guiada (No seu proprio ritmo) | **Fases:** 5 Módulos  
> **Dossiê SaaS de Origem:** Gmail, Microsoft 365, Zoho Mail

---

## Fase 1: Conceitos Email, SMTP/IMAP & Soberania (`⏱️ 1h 00min`)
**🎯 Meta da Etapa:** Entender protocolos email e beneficios privacidade

- [ ] **[Protocolos Email: SMTP, IMAP, POP3](https://www.digitalocean.com/community/tutorials/understanding-the-smtp-protocol)** (`Artigo Tecnico` - `[F01]`)
  - 💡 **O que você aprende:** Diferencas SMTP/IMAP/POP3. IMAP mais seguro.
  - ⏱️ 25 min | 👤 Linux Admins Brasil

- [ ] **[LGPD Servers Email Proprios](https://www.gov.br/cidadania/pt-br/acesso-a-informacao/lgpd)** (`Guia Legal` - `[F02]`)
  - 💡 **O que você aprende:** Responsabilidades legais
  - ⏱️ 20 min | 👤 Tech Law Advogado

- [ ] **[SSL/TLS Seguranca Email](https://letsencrypt.org/how-it-works/)** (`Documentacao Tecnica` - `[F03]`)
  - 💡 **O que você aprende:** SSL protege transito
  - ⏱️ 15 min | 👤 Let's Encrypt

## Fase 2: Instalacao VPS, Linux Basics (`⏱️ 1h 30min`)
**🎯 Meta da Etapa:** Tutorial instalacao Postfix+Dovecot

- [ ] **[VPS Hetzner Iniciantes](https://docs.hetzner.cloud/basics/getting-started/)** (`Tutorial` - `[F04]`)
  - 💡 **O que você aprende:** Criar conta, VPS, SSH
  - ⏱️ 30 min | 👤 DevOps Brasil

- [ ] **[Postfix+Dovecot Instalacao](https://www.linuxbabe.com/mail-server/postfix-dovecot-ubuntu)** (`Guia Tecnico` - `[F01]`)
  - 💡 **O que você aprende:** apt, systemctl, nano
  - ⏱️ 40min+20min | 👤 Linux Admins

- [ ] **[SSL Let's Encrypt](https://certbot.eff.org/instructions/ubuntu-20.04/)** (`Tutorial` - `[F03]`)
  - 💡 **O que você aprende:** Certificados auto
  - ⏱️ 20 min | 👤 Certbot

## Fase 3: SPF, DKIM, DMARC Config (`⏱️ 1h 15min`)
**🎯 Meta da Etapa:** Anti-spam assinaturas digitais

- [ ] **[SPF DKIM DMARC Explicado](https://www.sitehosting.com.br/blog/spf-dkim-dmarc/)** (`Artigo` - `[F02]`)
  - 💡 **O que você aprende:** Diferencas SPF/DKIM/DMARC
  - ⏱️ 30 min | 👤 Seguranca Email

- [ ] **[Implementar SPF DKIM DMARC](https://www.linuxbabe.com/mail-server/opendkim-ubuntu-postfix)** (`Guia Tecnico` - `[F04]`)
  - 💡 **O que você aprende:** opendkim-genkey, DNS
  - ⏱️ 45 min | 👤 Linux Babe

- [ ] **[Email Tester MXToolbox](https://mxtoolbox.com/)** (`Ferramenta` - `[F05]`)
  - 💡 **O que você aprende:** Validar SPF/DKIM/DMARC
  - ⏱️ 15 min | 👤 MXToolbox

## Fase 4: Clientes Email Dovecot (`⏱️ 1h 00min`)
**🎯 Meta da Etapa:** Thunderbird Outlook Apple Mail

- [ ] **[Thunderbird IMAP Config](https://support.mozilla.org/pt-BR/kb/configurar-sua-conta-de-email)** (`Tutorial` - `[F01]`)
  - 💡 **O que você aprende:** Port 993 SSL sync
  - ⏱️ 20 min | 👤 Mozilla Brasil

- [ ] **[Outlook IMAP Config](https://support.microsoft.com/pt-br/office/criar-um-perfil-novo-do-outlook)** (`Oficial` - `[F02]`)
  - 💡 **O que você aprende:** SMTP 587 STARTTLS
  - ⏱️ 15 min | 👤 Microsoft

- [ ] **[Filtros Regras Avancadas](https://support.mozilla.org/en-US/kb/creating-and-using-filters)** (`Docs` - `[F03]`)
  - 💡 **O que você aprende:** Automacao backup offline
  - ⏱️ 25 min | 👤 Thunderbird

## Fase 5: Troubleshooting Manutencao (`⏱️ 1h 15min`)
**🎯 Meta da Etapa:** Diagnostico escalabilidade

- [ ] **[Diagnostico SMTP/IMAP Problemas](https://www.linuxbabe.com/mail-server/postfix-dovecot-ubuntu)** (`Guia` - `[F04]`)
  - 💡 **O que você aprende:** /var/log/mail.log mailq telnet
  - ⏱️ 25 min | 👤 Linux Admins

- [ ] **[Monitoramento Tempo Real](https://www.digitalocean.com/community/tutorials/how-to-use-journalctl-to-view-and-manipulate-systemd-logs)** (`Tutorial` - `[F01]`)
  - 💡 **O que você aprende:** systemctl journalctl htop
  - ⏱️ 20 min | 👤 Linux Admins

- [ ] **[Multiplos Usuarios Quotas](https://doc.dovecot.org/configuration_manual/quota/)** (`Guia` - `[F02]`)
  - 💡 **O que você aprende:** Quotas doveadm limites
  - ⏱️ 30 min | 👤 Dovecot

- [ ] **[Backup Redundancia HA](https://www.linuxbabe.com/mail-server/backup-postfix-dovecot)** (`Arquitetural` - `[F05]`)
  - 💡 **O que você aprende:** Backup replicacao failover
  - ⏱️ 20 min | 👤 HA Systems
