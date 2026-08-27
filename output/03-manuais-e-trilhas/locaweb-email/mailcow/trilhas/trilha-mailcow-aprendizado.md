# Trilha Cronológica de Aprendizado: Mailcow

> **Jornada Pedagógica Autoguiada · Imersão a Partir das Fontes Primárias**  
> **Tempo Total Estimado:** 8 horas de imersão guiada (No seu próprio ritmo) | **Fases:** 5 Módulos  
> **Dossiê SaaS de Origem:** Locaweb-Email

---

## Fase 1: Fundamentos de Email & Soberania de Dados (Brasil First) (`⏱️ 1h 30min`)
**🎯 Meta da Etapa:** Entender por que ter um servidor de email próprio é crucial para empresas brasileiras sob a LGPD. Aprender como funciona a infraestrutura de email (SMTP, IMAP, POP3) sem enviar dados para provedores estrangeiros.

- [ ] **[Email, Privacidade e Conformidade LGPD em Servidores Brasileiros](https://www.aberta.org.br/)** (`Artigo Técnico / Guia Aberto` - `[F05]`)
  - 💡 **O que você aprende:** Diferenças entre armazenar emails em nuvens estrangeiras (Gmail, Office 365) versus manter dados sob custódia interna. Requisitos de backup, segurança física e conformidade LGPD.
  - ⏱️ 45 min de leitura | 👤 Comunidade Brasileira de Open Source & Privacidade

- [ ] **[Protocolo SMTP, IMAP e POP3: Como Funciona o Sistema de Correios Digital](https://tools.ietf.org/html/rfc5321)** (`Documentação Técnica` - `[F01]`)
  - 💡 **O que você aprende:** Entender as 3 camadas de um sistema de email: SMTP (envio), IMAP (recebimento com pastas), POP3 (recebimento simples). Razão pela qual o IMAP é moderno.
  - ⏱️ 45 min de leitura | 👤 IETF Standards & Linux Foundation

## Fase 2: Setup Mailcow na VPS & Primeiros Passos (`⏱️ 2h 15min`)
**🎯 Meta da Etapa:** Acompanhar tutoriais para colocar Mailcow em produção sem medo. Desde aluguel de VPS até primeira caixa de email funcionando.

- [ ] **[Como Criar uma VPS e Instalar Mailcow com Docker](https://docs.mailcow.email/b_getting_started/b_installation/)** (`Guia Prático / Tutorial` - `[F01]`)
  - 💡 **O que você aprende:** Passo 1: Alugar VPS. Passo 2: SSH e conectar. Passo 3: Clonar repositório Mailcow. Passo 4: gerar_config.sh. Passo 5: docker compose up -d.
  - ⏱️ 90 min de estudo + prática | 👤 Comunidade DevOps Brasil & Mailcow PT

- [ ] **[Playbook Oficial de Deploy Mailcow & Segurança Inicial](https://github.com/mailcow/mailcow-dockerized/tree/main/docs)** (`Código & Playbook` - `[F02]`)
  - 💡 **O que você aprende:** Configuração de firewall UFW para bloquear portas perigosas e liberar apenas SMTP (25, 587), IMAP (143, 993), HTTP/HTTPS (80, 443) e SSH (22).
  - ⏱️ 45 min de prática guiada | 👤 Mailcow DevOps Core

## Fase 3: Configuração de DNS, SPF, DKIM, DMARC & TLSA (`⏱️ 1h 45min`)
**🎯 Meta da Etapa:** Dominar a configuração de registros DNS para garantir que seus emails cheguem em caixas de entrada e não em spam. Aprender o que é cada protocolo de autenticação.

- [ ] **[MX Record, SPF, DKIM & DMARC: Os 4 Pilares de Autenticação de Email](https://docs.mailcow.email/b_getting_started/b_installation/b_dns/)** (`Guia Técnico` - `[F05]`)
  - 💡 **O que você aprende:** MX: diz ao internet onde está seu servidor. SPF: autoriza IPs que podem enviar. DKIM: assina digitalmente cada email. DMARC: política de rejeição se SPF/DKIM falhar. TLSA: criptografa conexão entre servidores.
  - ⏱️ 50 min de leitura | 👤 Fábrica Universal Brasil & Comunidade Email

- [ ] **[Testador de Registros DNS Online & Verificação de Propagação](https://mxtoolbox.com/)** (`Ferramenta Online` - `[F04]`)
  - 💡 **O que você aprende:** Uso de mxtoolbox.com para verificar se seus registros MX, SPF, DKIM já se propagaram. Teste de blacklist (spam checkers).
  - ⏱️ 30 min de prática | 👤 MXToolbox & Google Admin

- [ ] **[Troubleshooting de Emails em Spam & Ajustes de DMARC Policy](https://www.youtube.com/results?search_query=email+SPF+DKIM+DMARC+troubleshooting)** (`Vídeo Tutorial / YouTube` - `[F04]`)
  - 💡 **O que você aprende:** Razões comuns de rejeição (SPF fail, DKIM fail, DMARC policy). Uso de headers de bounce para diagnosticar.
  - ⏱️ 25 min de vídeo | 👤 Email Deliverability Experts

## Fase 4: Operação Diária, Monitoramento & Segurança (`⏱️ 1h 30min`)
**🎯 Meta da Etapa:** Aprender a gerenciar o Mailcow no dia a dia: criar usuários, monitorar logs, detectar ataques de spam, fazer backups automáticos.

- [ ] **[Interface Mailcow: Criação de Domínios, Usuários, Quotas & Aliases](https://docs.mailcow.email/b_getting_started/b_login/)** (`Tutorial Interativo` - `[F01]`)
  - 💡 **O que você aprende:** Menu 'Mail': domínios. Menu 'Mailboxes': contas. Menu 'Aliases': redirecionamentos. Menu 'Resources': quota de armazenamento. Menu 'Monitoring': logs em tempo real.
  - ⏱️ 45 min | 👤 Fábrica Universal Brasil

- [ ] **[Monitoramento, Alertas & Limpeza de Filas de Email](https://docs.mailcow.email/b_getting_started/b_monitoring/)** (`Guia Técnico` - `[F01]`)
  - 💡 **O que você aprende:** Verificação de fila de emails (Postfix queue). Logs de rejeição. Dashboard de CPU/RAM/Disco. Alertas automáticos se cotas forem atingidas.
  - ⏱️ 30 min | 👤 Mailcow Ops

- [ ] **[Backup Automático de Emails & Banco de Dados com Mailcow](https://docs.mailcow.email/b_getting_started/b_backup/)** (`Playbook / Tutorial` - `[F02]`)
  - 💡 **O que você aprende:** Backup diário automatizado de vmail/ e MariaDB. Armazenamento em disco externo ou cloud (AWS S3, Backblaze).
  - ⏱️ 15 min | 👤 Comunidade DevOps Brasil

## Fase 5: Segurança Avançada, Validação SSL & Desinstalação Cirúrgica (`⏱️ 1h 30min`)
**🎯 Meta da Etapa:** Implementar segurança adicional (fail2ban, rate limiting), renovação automática de certificados SSL, e aprender a desinstalar Mailcow sem danificar outros serviços.

- [ ] **[Hardening de Mailcow: Fail2ban, Rate Limiting & Segurança de Senhas](https://docs.mailcow.email/b_getting_started/b_security/)** (`Guia Técnico` - `[F05]`)
  - 💡 **O que você aprende:** Ativar fail2ban para bloquear IPs com muitas tentativas de login. Rate limiting em Postfix para prevenir spam. Política de senhas forte (12+ caracteres, maiúsculas, números, símbolos).
  - ⏱️ 40 min | 👤 Fábrica Universal & Comunidade Email

- [ ] **[Certificados SSL/TLS Automáticos com Let's Encrypt & Renovação](https://docs.mailcow.email/b_getting_started/b_ssl/)** (`Documentação Técnica` - `[F01]`)
  - 💡 **O que você aprende:** Let's Encrypt emite certificados gratuitos, válidos 90 dias. Mailcow renova automaticamente 30 dias antes de expirar. Verificação com 'docker compose logs certbot-mailcow'.
  - ⏱️ 30 min | 👤 Let's Encrypt & Mailcow

- [ ] **[Desinstalação Cirúrgica de Mailcow & Volta para Locaweb (se necessário)](https://docs.mailcow.email/)** (`Guia Prático` - `[F02]`)
  - 💡 **O que você aprende:** Backup de dados ANTES de deletar. Remoção de containers com 'docker compose down'. Limpeza de volumes. Resetar firewall. Alterar registros MX se voltar a usar Locaweb.
  - ⏱️ 20 min | 👤 Fábrica Universal Brasil
