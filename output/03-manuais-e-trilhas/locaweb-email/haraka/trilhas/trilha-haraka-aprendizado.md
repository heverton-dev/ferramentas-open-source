# Trilha Cronológica de Aprendizado: Haraka

> **Jornada Pedagógica Autoguiada · Imersão a Partir das Fontes Primárias**  
> **Tempo Total Estimado:** 8 horas | **Fases:** 5 Módulos  
> **Dossiê SaaS de Origem:** Locaweb-Email

---

## Fase 1: Conceitos & Arquitetura SMTP (`⏱️ 1h 30min`)
**🎯 Meta da Etapa:** Entender fundamentos de SMTP e diferenças entre MTA, MSA e Haraka

- [ ] **[O que é SMTP e Por Que Você Precisa de um Servidor Próprio](https://www.rfc-editor.org/rfc/rfc5321.txt)** (`Artigo Técnico` - `[F01]`)
  - 💡 **O que você aprende:** SMTP é padrão universal de troca de emails
  - ⏱️ 45 min | 👤 Comunidade Email Open Source

- [ ] **[Arquitetura do Haraka em Node.js](https://haraka.github.io/)** (`Documentação Oficial` - `[F02]`)
  - 💡 **O que você aprende:** Pipeline de hooks: validação, bloqueio, transformação
  - ⏱️ 1h | 👤 Haraka Community

- [ ] **[Soberania de Email & LGPD](https://www.gov.br/cidadania/pt-br/acesso-a-informacao/lgpd)** (`Case Study` - `[F03]`)
  - 💡 **O que você aprende:** Custódia interna = compliance garantido
  - ⏱️ 30 min | 👤 Especialistas Compliance

## Fase 2: Instalação & Setup em VPS (`⏱️ 2h`)
**🎯 Meta da Etapa:** Provisionar VPS, instalar Haraka, configurar plugins e receber primeiro email

- [ ] **[Escolher e Provisionar VPS](https://contabo.com)** (`Guia Comparativo` - `[F01]`)
  - 💡 **O que você aprende:** Contabo (barato), Hetzner (rápido), DigitalOcean (amigável)
  - ⏱️ 1h | 👤 DevOps Brasil

- [ ] **[Instalação Haraka do Zero](https://haraka.github.io/manual/Installation.html)** (`Tutorial` - `[F02]`)
  - 💡 **O que você aprende:** npm install -g haraka é tudo que você precisa
  - ⏱️ 1h hands-on | 👤 Haraka Documentation

- [ ] **[Primeiro Email Teste](https://mailtester.com)** (`Guia Prático` - `[F03]`)
  - 💡 **O que você aprende:** Configure SMTP no cliente e teste
  - ⏱️ 30 min | 👤 Comunidade Brasil

## Fase 3: Antispam & Plugins Avançados (`⏱️ 2h`)
**🎯 Meta da Etapa:** Instalar plugins de proteção contra spam com IA

- [ ] **[Plugins Haraka Essenciais](https://github.com/haraka/Haraka/tree/master/plugins)** (`Documentação Técnica` - `[F01]`)
  - 💡 **O que você aprende:** known_hosts, spamassassin, limit_concurrency
  - ⏱️ 1h | 👤 Haraka Maintainers

- [ ] **[Integração com Rspamd (IA Antispam)](https://rspamd.com/doc/workers/controller.html)** (`Tutorial` - `[F02]`)
  - 💡 **O que você aprende:** Bayes + Neural Networks > filtros simples
  - ⏱️ 1h hands-on | 👤 Rspamd Community

## Fase 4: Segurança & Autenticação (`⏱️ 1h 30min`)
**🎯 Meta da Etapa:** Configurar TLS, DKIM, SPF, DMARC, autenticação SASL

- [ ] **[SSL/TLS com LetsEncrypt](https://certbot.eff.org)** (`Guia Prático` - `[F01]`)
  - 💡 **O que você aprende:** Certificados GRATUITOS com renovação automática
  - ⏱️ 45 min | 👤 EFF Brasil

- [ ] **[DKIM, SPF & DMARC](https://mxtoolbox.com/dmarc/)** (`Guia Técnico` - `[F02]`)
  - 💡 **O que você aprende:** Tripé de autenticação = 100% de autenticidade
  - ⏱️ 45 min | 👤 Especialistas Email

- [ ] **[Autenticação SASL](https://haraka.github.io/plugins/auth/)** (`Tutorial` - `[F03]`)
  - 💡 **O que você aprende:** SASL força autenticação contra spam
  - ⏱️ 30 min | 👤 Haraka

## Fase 5: Monitoramento & Operação Contínua (`⏱️ 1h 30min`)
**🎯 Meta da Etapa:** Monitorar saúde, auditar logs, backup automático, respond incidentes

- [ ] **[Monitoramento em Tempo Real](https://prometheus.io/)** (`Tutorial DevOps` - `[F01]`)
  - 💡 **O que você aprende:** Prometheus + Grafana para métricas
  - ⏱️ 1h | 👤 Prometheus & DevOps

- [ ] **[Leitura de Logs & Troubleshooting](tail -f /var/log/haraka/*.log)** (`Guia Prático` - `[F02]`)
  - 💡 **O que você aprende:** Logs revelam tudo sobre o servidor
  - ⏱️ 30 min | 👤 Linux Tutores

- [ ] **[Backup & Recuperação](0 2 * * * /usr/local/bin/haraka_backup.sh)** (`Script` - `[F03]`)
  - 💡 **O que você aprende:** Backup diário + teste mensal
  - ⏱️ 30 min | 👤 DevOps
