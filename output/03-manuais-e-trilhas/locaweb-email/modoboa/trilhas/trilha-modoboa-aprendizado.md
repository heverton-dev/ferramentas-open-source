# Trilha Cronológica de Aprendizado: Modoboa

> **Jornada Pedagógica Autoguiada · Imersão a Partir das Fontes Primárias** 
> **Tempo Total Estimado:** 8 horas de imersão guiada (No seu próprio ritmo) | **Fases:** 5 Módulos 
> **Dossiê SaaS de Origem:** Locaweb-Email

---

## Aula 1: Conceito, Privacidade & Soberania de Email (Brasil First) (`⏱ 1h 30min`)
** Meta da Etapa:** Entender por que manter seu próprio servidor de email é crucial para empresas brasileiras sob a LGPD e como funciona a infraestrutura de email sem terceiros.

- [ ] **[Entendendo a Privacidade e Segurança de Dados de Email](https://dev.to/t/opensource)** (`Artigo Técnico / Guia Aberto` - `[F05]`)
 - **O que você aprende:** Diferenças entre armazenar emails em nuvens estrangeiras (Gmail, Outlook) e manter 100% dos dados sob custódia interna com criptografia LGPD.
 - ⏱ 45 min de leitura | Comunidade Brasileira de Open Source & Email Soberano

- [ ] **[Visão Geral da Arquitetura do Modoboa & Infraestrutura SMTP/IMAP](https://modoboa.readthedocs.io/)** (`Documentação Oficial` - `[F01]`)
 - **O que você aprende:** Como funciona a pilha de protocolos (SMTP, IMAP, POP3, DKIM, SPF) em um servidor de email corporativo.
 - ⏱ 45 min de leitura assistida | Equipe Modoboa

## Aula 2: Instalação Descomplicada na VPS & Primeiros Passos (`⏱ 2h`)
** Meta da Etapa:** Acompanhar tutoriais de Linux e Docker para colocar seu próprio servidor de email no ar sem medo de terminal.

- [ ] **[Como Alugar uma VPS e Rodar Containers Docker do Zero](https://modoboa.readthedocs.io/en/master/install.html)** (`Guia Prático / Tutorial` - `[F01]`)
 - **O que você aprende:** Comandos básicos de navegação em pastas no Linux, SSH e inicialização com docker compose up.
 - ⏱ 1h de estudo | Comunidade DevOps Brasil

- [ ] **[Playbook Oficial de Deploy e Infraestrutura em Produção](https://github.com/modoboa/modoboa-docker)** (`Código & Playbook` - `[F05]`)
 - **O que você aprende:** Configuração do reverse proxy Nginx com SSL automático e certificado Let's Encrypt para proteger seu acesso.
 - ⏱ 1h de prática guiada | Modoboa DevOps Core

## Aula 3: Gerenciamento de Domínios, Usuários & Configuração de Email (`⏱ 1h 45min`)
** Meta da Etapa:** Dominar a interface de administração: adicionar domínios, criar usuários, configurar SPF/DKIM/DMARC, quotas e políticas de senha.

- [ ] **[Demonstração Completa: Criando Domínio, Usuários e Enviando Primeiro Email](https://www.youtube.com/results?search_query=modoboa+admin+setup)** (`Vídeo Tutorial / YouTube` - `[F04]`)
 - **O que você aprende:** Como adicionar um domínio, validar registros DNS (MX, SPF, DKIM), criar usuários e testar entrega de emails.
 - ⏱ 25 min de vídeo + 50 min de prática | Self-Hosted Email Community

- [ ] **[Guia de Configuração de SPF, DKIM e DMARC para Reputação de Email](https://modoboa.readthedocs.io/en/master/admin/index.html)** (`Guia Técnico` - `[F03]`)
 - **O que você aprende:** Como configurar registros DNS para garantir que seus emails não caiam em spam e sejam entregues com segurança.
 - ⏱ 40 min de leitura | Internet Mail Consortium

## Aula 4: Webmail, Calendário, Contatos & Sincronização com Clientes (`⏱ 1h 45min`)
** Meta da Etapa:** Usar a interface Webmail do Modoboa como Gmail, sincronizar calendário e contatos via CalDAV/CardDAV com Outlook, Apple Mail e Thunderbird.

- [ ] **[Guia de Uso do Webmail Modoboa: Composição, Filtros e Assinaturas](https://modoboa.readthedocs.io/en/master/user/index.html)** (`Tutorial Prático` - `[F01]`)
 - **O que você aprende:** Como compor emails em HTML, anexar arquivos, criar assinaturas automáticas e usar filtros de spam.
 - ⏱ 50 min de leitura | Fábrica Universal Brasil

- [ ] **[Sincronização de Calendário e Contatos (CalDAV / CardDAV) em Thunderbird & Apple Mail](https://github.com/modoboa/modoboa)** (`Código & Especificação` - `[F02]`)
 - **O que você aprende:** Uso de protocolo CalDAV/CardDAV para sincronizar calendário e contatos com clientes de desktop e mobile.
 - ⏱ 55 min de testes | Modoboa Community

## Aula 5: Operação Contínua, Backup, Monitoramento & Segurança Avançada (`⏱ 1h`)
** Meta da Etapa:** Manter seu servidor de email rodando com segurança: backup automático, monitoramento de saúde, alertas, atualização de patches e compliance LGPD.

- [ ] **[Estratégia de Backup Automático com PostgreSQL e Criptografia](https://modoboa.readthedocs.io/en/master/admin/index.html)** (`Guia de Operação` - `[F05]`)
 - **O que você aprende:** Como fazer backup do banco PostgreSQL, criptografar e enviar para serviço externo seguro (S3, Wasabi) com retenção automática.
 - ⏱ 30 min de leitura | DevOps Brasil & Comunidade de Email Open Source

- [ ] **[Monitoramento de Saúde, Logs e Alerts com Prometheus + Grafana](https://github.com/modoboa/modoboa)** (`Tutorial Operacional` - `[F02]`)
 - **O que você aprende:** Como configurar alertas para fila de emails travada, queda de disco, aumento de spam ou autenticação suspeita.
 - ⏱ 30 min de prática | Modoboa DevOps & Prometheus Community
