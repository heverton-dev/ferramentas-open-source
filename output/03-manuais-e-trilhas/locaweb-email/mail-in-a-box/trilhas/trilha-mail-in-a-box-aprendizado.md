# Trilha Cronológica de Aprendizado: Mail-in-a-Box

> **Jornada Pedagógica Autoguiada · Imersão a Partir das Fontes Primárias**  
> **Tempo Total Estimado:** 8 horas | **Fases:** 5 Módulos  
> **Dossiê SaaS de Origem:** Locaweb-Email

---

## Fase 1: Fundamentos de Email e Protocolos (`⏱️ 1h 30min`)
**🎯 Meta da Etapa:** Entender os principios de comunicacao por email e diferenca entre SMTP/IMAP

- [ ] **[Mail-in-a-Box Official Documentation](https://mailinabox.email/guide.html)** (`Documentacao Oficial` - `[F01]`)
  - 💡 **O que você aprende:** Arquitetura completa: Postfix, Dovecot, certificados SSL, seguranca
  - ⏱️ 45 min | 👤 Joshua Tate

- [ ] **[SMTP e IMAP - Protocolos Fundamentais](https://tools.ietf.org/html/rfc5321)** (`Artigo Tecnico` - `[F02]`)
  - 💡 **O que você aprende:** Como email viaja pela internet, diferenca entre protocolos
  - ⏱️ 45 min | 👤 IETF Standards

## Fase 2: Instalacao de Mail-in-a-Box em VPS (`⏱️ 2h`)
**🎯 Meta da Etapa:** Deploy completo em producao com configuracao inicial

- [ ] **[Mail-in-a-Box Quick Start Guide](https://mailinabox.email/)** (`Tutorial Pratico` - `[F03]`)
  - 💡 **O que você aprende:** Script automatizado, configuracao DNS inicial, criacao de admin
  - ⏱️ 1h 30min de pratica | 👤 Mail-in-a-Box Documentation

- [ ] **[DNS Configuration e Domain Pointing](https://www.icann.org/resources/pages/domain-registry-2013-12-02-en)** (`Lab Interativo` - `[F04]`)
  - 💡 **O que você aprende:** Apontar A record, MX record e TXT record para sua VPS
  - ⏱️ 30 min de pratica | 👤 ICANN e Registradores de Dominio

## Fase 3: Autenticacao de Email - SPF, DKIM e DMARC (`⏱️ 1h 45min`)
**🎯 Meta da Etapa:** Configurar registros que evitam spam e falsificacao

- [ ] **[SPF DKIM DMARC Configuration Guide](https://dmarc.org/)** (`Guia Completo` - `[F05]`)
  - 💡 **O que você aprende:** Registros que provam identidade do servidor e previnem spoofing
  - ⏱️ 1h | 👤 DMARC.org e Email Security Community

- [ ] **[Validacao de Configuracao com MXToolbox](https://mxtoolbox.com)** (`Ferramenta Online` - `[F06]`)
  - 💡 **O que você aprende:** Como verificar se SPF, DKIM, DMARC estao corretos
  - ⏱️ 30 min | 👤 MXToolbox

## Fase 4: Testes de Entrega e Monitoramento (`⏱️ 1h 30min`)
**🎯 Meta da Etapa:** Validar que emails chegam sem cair em spam

- [ ] **[Email Deliverability Testing Guide](https://www.returnpath.com/deliverability/)** (`Tutorial Pratico` - `[F07]`)
  - 💡 **O que você aprende:** Como testar se emails sao recebidos vs entram em spam
  - ⏱️ 1h | 👤 Email Security Best Practices

- [ ] **[Monitoramento de Logs e Troubleshooting](https://www.postfix.org/DEBUG_README.html)** (`Documentacao Tecnica` - `[F08]`)
  - 💡 **O que você aprende:** Como ler logs de mail.log e diagnosticar falhas
  - ⏱️ 30 min | 👤 Postfix e Dovecot Docs

## Fase 5: Migracao para Locaweb Email e Desinstalacao (`⏱️ 1h 15min`)
**🎯 Meta da Etapa:** Migrar usuarios para Locaweb e remover Mail-in-a-Box

- [ ] **[IMAPSync - Migracao entre Servidores de Email](https://imapsync.lamiral.info/)** (`Guia Pratico` - `[F09]`)
  - 💡 **O que você aprende:** Como sincronizar 100% do historico sem perder emails
  - ⏱️ 35 min | 👤 IMAPSync Community

- [ ] **[Como Contratar e Configurar Locaweb Email](https://ajuda.locaweb.com.br/email/)** (`Tutorial em Video` - `[F10]`)
  - 💡 **O que você aprende:** Criar contas, obter MX records, validar IMAP
  - ⏱️ 25 min | 👤 Suporte Locaweb

- [ ] **[Desinstalacao Cirurgica de Mail-in-a-Box](https://github.com/trcnologia/arsenal-opensource)** (`Checklist de Acao` - `[F11]`)
  - 💡 **O que você aprende:** Ordem correta: backup, migrar, DNS, parar servicos, remover
  - ⏱️ 15 min | 👤 Arsenal Open Source - Este Manual
