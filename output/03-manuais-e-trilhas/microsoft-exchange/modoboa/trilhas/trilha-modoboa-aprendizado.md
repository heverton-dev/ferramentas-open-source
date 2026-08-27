# Trilha Cronológica de Aprendizado: Modoboa

> **Jornada Pedagógica Autoguiada · Imersão a Partir das Fontes Primárias**  
> **Tempo Total Estimado:** 520 minutos (~8-10 horas) | **Fases:** 5 Módulos  
> **Dossiê SaaS de Origem:** Microsoft-Exchange

---

## Fase 1: Fundamentos, Arquitetura de Email e Stack Modoboa (`⏱️ 1h 30min`)
**🎯 Meta da Etapa:** Entender o fluxo de email (SMTP → Postfix → Dovecot), conhecer os componentes técnicos do Modoboa e dominar protocolos de segurança (SPF, DKIM, DMARC) para garantir entregabilidade.

- [ ] **[Documentação Oficial: Conceitos e Arquitetura Modoboa](https://modoboa.readthedocs.io/en/latest/)** (`Documentação Oficial` - `[F01]`)
  - 💡 **O que você aprende:** Visão geral da arquitetura: Postfix (SMTP relay), Dovecot (IMAP/POP3), Django (admin web), PostgreSQL (dados), Nginx (proxy).
  - ⏱️ 45 min de leitura | 👤 Modoboa Core Team

- [ ] **[Análise Econômica: Exchange vs Modoboa em Soberania de Dados](https://github.com/modoboa/modoboa/wiki/Cost-Analysis)** (`Artigo Técnico` - `[F02]`)
  - 💡 **O que você aprende:** Comparação de custos: 50 usuários em Exchange (USD 600-1000/mês) vs Modoboa em Hetzner (EUR 14-16/mês). Economia de 95% com total controle.
  - ⏱️ 30 min de leitura | 👤 Fábrica Universal Brasil

- [ ] **[Guia Técnico: Protocolos SMTP, IMAP, POP3 e Segurança (SPF, DKIM, DMARC)](https://modoboa.readthedocs.io/en/latest/admin/features.html#authentication-methods)** (`Guia Técnico` - `[F03]`)
  - 💡 **O que você aprende:** Diferenças entre SMTP (envio), IMAP (sincronização), POP3 (download). Por que SPF, DKIM e DMARC são obrigatórios para evitar spam.
  - ⏱️ 35 min de leitura | 👤 Internet Mail Consortium

- [ ] **[Registro de DNS e Validação de Autenticidade de Email](https://mdubt.org/resources/)** (`Guia Prático` - `[F05]`)
  - 💡 **O que você aprende:** Como gerar e configurar registros SPF, DKIM e DMARC no seu registrador de domínio (GoDaddy, NameCheap) para máxima entregabilidade.
  - ⏱️ 25 min de prática | 👤 Comunidade DevOps Brasil

## Fase 2: Provisionamento VPS, Instalação Automática e Segurança (`⏱️ 2h`)
**🎯 Meta da Etapa:** Provisionar uma VPS em Hetzner Cloud, executar o instalador automático do Modoboa, configurar firewall (UFW) e ativar HTTPS com Let's Encrypt para produção.

- [ ] **[Como Provisionar VPS Debian/Ubuntu em Hetzner Cloud](https://www.hetzner.cloud)** (`Guia Prático / Tutorial` - `[F01]`)
  - 💡 **O que você aprende:** Passo a passo: criar conta, escolher Debian 12 + CPX31, copiar IP/senha, acessar via SSH no Windows (PowerShell) ou Mac (Terminal).
  - ⏱️ 40 min de estudo + prática | 👤 Comunidade DevOps Brasil

- [ ] **[Preparação do Sistema Operacional e Dependências](https://github.com/modoboa/modoboa/blob/master/docs/install.rst)** (`Código & Playbook` - `[F05]`)
  - 💡 **O que você aprende:** Atualizar Debian (apt-get update/upgrade), instalar PostgreSQL, Postfix, Dovecot, Nginx, Python3-dev. Verificar versões instaladas.
  - ⏱️ 30 min de prática | 👤 Modoboa DevOps Core

- [ ] **[Instalador Automático Modoboa: Deploy de Produção](https://modoboa.readthedocs.io/en/latest/deployment/)** (`Tutorial Prático` - `[F01]`)
  - 💡 **O que você aprende:** Clone do repositório oficial, checkout v2.3.0, execução de 'modoboa deploy /var/vmail/modoboa'. Sistema pergunta hostname, domínio, senha admin.
  - ⏱️ 35 min de prática guiada | 👤 Modoboa Installation Team

- [ ] **[Firewall UFW, Portas de Email e HTTPS com Let's Encrypt](https://letsencrypt.org/getting-started/)** (`Guia de Segurança` - `[F06]`)
  - 💡 **O que você aprende:** UFW ativar com portas 22 (SSH), 25 (SMTP), 80 (HTTP), 143 (IMAP), 110 (POP3), 587 (submission), 443 (HTTPS). Certbot + Let's Encrypt para renovação automática.
  - ⏱️ 35 min de prática | 👤 Certbot & Let's Encrypt

## Fase 3: Configuração de Domínios, Contas e Validação DNS (`⏱️ 1h 40min`)
**🎯 Meta da Etapa:** Criar domínios no painel admin, adicionar contas de usuários com quotas, configurar aliases e listas de email, validar registros DNS (SPF, DKIM, DMARC) para produção.

- [ ] **[Painel Admin Web do Modoboa: Dashboard e Navegação](https://modoboa.readthedocs.io/en/latest/manage_domains/index.html)** (`Tutorial Prático` - `[F01]`)
  - 💡 **O que você aprende:** Acessar https://seu-domínio/admin/, login com admin, explorar dashboard com métricas de emails recebidos/enviados, status de domínios e contas.
  - ⏱️ 25 min de prática | 👤 Comunidade Modoboa Brasil

- [ ] **[Criação de Domínios com Quotas e Status de Registros](https://modoboa.readthedocs.io/en/latest/manage_domains/index.html)** (`Guia Prático` - `[F02]`)
  - 💡 **O que você aprende:** Menu Domínios → +, criar 'empresa.com.br', quota (0=ilimitada), cópia dos registros SPF/DKIM gerados. Adicionar no DNS do registrador (GoDaddy, NameCheap).
  - ⏱️ 35 min de prática | 👤 Modoboa Admin Team

- [ ] **[Criação de Contas de Usuário, Aliases e Listas de Email](https://modoboa.readthedocs.io/en/latest/manage_users/index.html)** (`Tutorial Prático` - `[F03]`)
  - 💡 **O que você aprende:** Criar contas (joao@empresa.com.br com quota 2GB), aliases (contato@empresa → joao@empresa), listas (vendas@ para múltiplos destinatários). Testar login no webmail.
  - ⏱️ 30 min de prática | 👤 Modoboa Admin Core

- [ ] **[Validação de Registros DNS e Entregabilidade de Email](https://mxtoolbox.com)** (`Guia Técnico` - `[F04]`)
  - 💡 **O que você aprende:** Verificar SPF, DKIM, DMARC com MXToolbox. Validar que emails não vão para spam. Testar com Mailtrap ou semelhante.
  - ⏱️ 20 min de verificação | 👤 MXToolbox & Fábrica Universal

## Fase 4: Webmail Integrado, Calendário (CalDAV) e Segurança Avançada (`⏱️ 1h 50min`)
**🎯 Meta da Etapa:** Dominar a interface webmail (composer, anexos, busca full-text), sincronizar calendário com Outlook/Google Calendar via CalDAV, configurar filtros Sieve automáticos, ativar 2FA e gerenciar backups.

- [ ] **[Interface Webmail: Composer WYSIWYG, Arquivos e Busca Full-Text](https://modoboa.readthedocs.io/en/latest/webmail/index.html)** (`Tutorial Prático` - `[F01]`)
  - 💡 **O que você aprende:** Acessar https://mail.seu-domínio.com/, redigir com WYSIWYG, drag-drop de arquivos, busca por palavras-chave, criar pastas, temas claro/escuro.
  - ⏱️ 30 min de prática | 👤 Modoboa UX Team

- [ ] **[Calendário e Contatos: Sincronização CalDAV/CardDAV](https://modoboa.readthedocs.io/en/latest/webmail/index.html)** (`Documentação Oficial` - `[F02]`)
  - 💡 **O que você aprende:** Webmail inclui calendário integrado. Sincronizar com Outlook/Google Calendar/iPhone via CalDAV URL (caldav.seu-domínio.com). Contatos via CardDAV.
  - ⏱️ 40 min de configuração | 👤 Modoboa & Comunidade CalDAV

- [ ] **[Filtros Sieve Automáticos: Regras de Processamento de Email](https://www.dovecot.org/doc/sieve/)** (`Guia Técnico` - `[F05]`)
  - 💡 **O que você aprende:** Criar regras: FROM 'marketing@' → pasta 'Marketing', SUBJECT 'URGENT' → marcado. Processamento no servidor, não no cliente.
  - ⏱️ 30 min de prática | 👤 Comunidade Sieve & Dovecot

- [ ] **[Backup, Retenção de Deletados, 2FA e Políticas de Segurança](https://modoboa.readthedocs.io/en/latest/admin/index.html)** (`Guia de Segurança` - `[F06]`)
  - 💡 **O que você aprende:** Fazer backup por domínio (ZIP). Configurar retenção de deletados (ex: 30 dias). Ativar 2FA para admin com Google Authenticator.
  - ⏱️ 30 min de configuração | 👤 Modoboa Security Team

## Fase 5: Monitoramento, Troubleshooting e Otimização de Performance (`⏱️ 1h 40min`)
**🎯 Meta da Etapa:** Monitorar saúde do servidor (CPU, disco, fila), diagnosticar problemas comuns (IMAP down, emails em spam), otimizar performance (pooling, cache, quotas) e manter logs de auditoria.

- [ ] **[Dashboard de Monitoramento: Métricas e Alertas em Tempo Real](https://modoboa.readthedocs.io/en/latest/admin/features.html)** (`Tutorial Prático` - `[F01]`)
  - 💡 **O que você aprende:** Dashboard mostra: emails/hora, spam detectado, usuários ativos, tamanho de mailboxes. Alertas se disco >90% ou CPU >80%. Projeção de esgotamento.
  - ⏱️ 25 min de prática | 👤 Modoboa Monitoring Team

- [ ] **[Fila de Emails e Queue Management (Postfix)](http://www.postfix.org/qmgr.8.html)** (`Guia Técnico` - `[F03]`)
  - 💡 **O que você aprende:** Comando 'postqueue -p' mostra fila. Se cresce (problema de conectividade), usar 'postfix flush' para reentrega ou 'postsuper -d ALL' para limpar.
  - ⏱️ 30 min de prática | 👤 Postfix & Modoboa Core

- [ ] **[Diagnóstico de Problemas Comuns: IMAP Down, SPF/DKIM, Blacklist](https://modoboa.readthedocs.io/en/latest/troubleshooting/index.html)** (`Guia de Troubleshooting` - `[F04]`)
  - 💡 **O que você aprende:** IMAP: telnet mail.seu-dominio.com 143. SPF/DKIM: MXToolbox. Logs: tail -f /var/log/mail.log. PostgreSQL: psql -c 'SELECT count(*) FROM pg_stat_activity'. Reiniciar: systemctl restart dovecot.
  - ⏱️ 35 min de diagnóstico | 👤 Fábrica Universal & Comunidade Modoboa

- [ ] **[Otimização de Performance: Conexões PostgreSQL, Cache Redis e Escalabilidade](https://modoboa.readthedocs.io/en/latest/admin/index.html)** (`Guia de Performance` - `[F02]`)
  - 💡 **O que você aprende:** Aumentar max_connections PostgreSQL (100 → 200), configurar cache Redis para Django, desativar POP3 se só usar IMAP, limitar tamanho de anexo. Monitorar com top, iostat, vmstat.
  - ⏱️ 30 min de otimização | 👤 Comunidade DevOps Brasil

- [ ] **[Logs, Auditoria e Compliance: Histórico de Acessos e Operações](https://modoboa.readthedocs.io/en/latest/admin/index.html)** (`Documentação Oficial` - `[F06]`)
  - 💡 **O que você aprende:** Admin → Relatórios → Logs: histórico login, operações (criar usuário, deletar domínio), erros. Exportar CSV. Arquivos: /var/log/auth.log, /var/log/mail.log.
  - ⏱️ 20 min de configuração | 👤 Modoboa Compliance Team
