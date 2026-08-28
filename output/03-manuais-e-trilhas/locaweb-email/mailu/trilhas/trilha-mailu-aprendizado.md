# Trilha Cronológica de Aprendizado: Mailu

> **Jornada Pedagógica Autoguiada · Imersão a Partir das Fontes Primárias** 
> **Tempo Total Estimado:** 8 horas de imersão guiada (No seu próprio ritmo) | **Fases:** 5 Módulos 
> **Dossiê SaaS de Origem:** Locaweb-Email

---

## Fase 1: Email, Privacidade & Soberania Corporativa (Brasil First) (`⏱ 1h 30min`)
** Meta da Etapa:** Entender por que hosting próprio de email é crucial para empresas brasileiras sob LGPD, como funciona a federação de email na internet e os riscos de depender de Locaweb ou terceiros.

- [ ] **[LGPD, Privacidade de Dados Corporativos e Riscos de Cloud Estrangeira](https://www.gov.br/cidadania/pt-br/acesso-a-informacao/lgpd)** (`Artigo Técnico / Guia Aberto` - `[F05]`)
 - **O que você aprende:** Diferenças entre armazenar emails em Microsoft 365 (EUA) vs Locaweb (Brasil) vs Mailu (seu próprio servidor). Controle jurisdicional absoluto.
 - ⏱ 45 min de leitura | Comunidade Brasileira de Privacidade & Compliance

- [ ] **[Visão Geral da Arquitetura de Servidores de Email & Protocolo SMTP](https://mailu.io/latest/)** (`Documentação Oficial` - `[F01]`)
 - **O que você aprende:** Como emails viajam pela internet de servidor para servidor, como SPF/DKIM/DMARC protegem contra falsificação.
 - ⏱ 45 min de leitura assistida | Mailu Documentation & SMTP RFC 5321

## Fase 2: Preparação de Domínio, DNS e Certificados SSL (`⏱ 1h 45min`)
** Meta da Etapa:** Aprender a registrar domínios, configurar registros DNS (MX, A, SPF, DKIM, DMARC) e gerar certificados SSL com Let's Encrypt para produção.

- [ ] **[Como Comprar Domínio e Gerenciar Registros DNS](https://www.registro.br/)** (`Guia Prático / Tutorial` - `[F02]`)
 - **O que você aprende:** Registros A (IP do servidor), MX (servidor de email), TXT (SPF/DKIM/DMARC), CNAME (aliases).
 - ⏱ 45 min de estudo | Comunidade Brasileira de Infraestrutura

- [ ] **[SPF, DKIM e DMARC: Assinando seus Emails com Confiança](https://mailu.io/latest/configuration/settings/)** (`Código & Playbook` - `[F05]`)
 - **O que você aprende:** Geração de chaves DKIM, configuração de política SPF no DNS, monitoramento de rejeições com DMARC.
 - ⏱ 1h de prática guiada | Mailu Core & DMARC.org

## Fase 3: Instalação em VPS & Primeiros Passos com Docker (`⏱ 2h`)
** Meta da Etapa:** Alugar uma VPS (Hetzner, Contabo), instalar Mailu via Docker Compose e colocar o servidor de email no ar.

- [ ] **[Como Alugar uma VPS Europeia (Hetzner) e Conectar via SSH](https://www.hetzner.com/cloud)** (`Guia Prático / Tutorial` - `[F02]`)
 - **O que você aprende:** Seleção de VPS ideal (CPX21 com 2 vCPU, 4 GB RAM, 80 GB SSD), primeiro acesso SSH, mudança de senha root.
 - ⏱ 30 min de estudo | Comunidade DevOps Brasil

- [ ] **[Hardening de Servidor Linux & Instalação de Docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/)** (`Guia Técnico` - `[F02]`)
 - **O que você aprende:** Atualização de pacotes, criação de usuário non-root, firewall UFW, instalação de Docker Engine.
 - ⏱ 45 min de prática | Ubuntu Security Guides & Docker Official

- [ ] **[Deploy de Mailu via Docker Compose & Configuração Inicial](https://github.com/Mailu/Mailu/blob/master/setup.py)** (`Tutorial Prático` - `[F01]`)
 - **O que você aprende:** Clone do repo GitHub, execução do setup.py, geração de docker-compose.yml configurado.
 - ⏱ 45 min de prática | Mailu Setup Wizard

## Fase 4: Configuração de Usuários, Clientes de Email e Testagem (`⏱ 1h 30min`)
** Meta da Etapa:** Criar usuários no painel Mailu, configurar Thunderbird/Outlook/iPhone para acessar remotamente e enviar emails de teste.

- [ ] **[Painel de Administração Mailu: Criar Usuários, Aliases e Domínios](https://mailu.io/latest/administration/)** (`Tutorial Prático` - `[F01]`)
 - **O que você aprende:** Criação de usuários, definição de quotas, bloqueio de spam, consulta de logs.
 - ⏱ 40 min de prática | Mailu Documentation

- [ ] **[Configurando Thunderbird, Outlook, Gmail & Clientes Móveis](https://mailu.io/latest/clients/)** (`Guia de Integração` - `[F03]`)
 - **O que você aprende:** Configuração de IMAP (portas 143/993), SMTP (portas 587/465), validação de certificado SSL.
 - ⏱ 50 min de prática | Mailu Community

## Fase 5: Monitoramento, Backup Automático & Operação em Produção (`⏱ 1h 15min`)
** Meta da Etapa:** Implementar rotina de backup, monitorar saúde do servidor (logs, disco, memória), configurar alertas e preparar desinstalação cirúrgica se necessário.

- [ ] **[Backup e Disaster Recovery de Servidor de Email](https://mailu.io/latest/administration/backups/)** (`Guia Técnico` - `[F04]`)
 - **O que você aprende:** Rotina diária de backup do banco PostgreSQL, armazenamento remoto com rsync/S3, testes de restauração.
 - ⏱ 35 min de leitura | Fábrica Universal Brasil

- [ ] **[Monitoramento de Saúde: Logs, Alertas e Troubleshooting](https://mailu.io/latest/administration/troubleshooting/)** (`Código & Playbook` - `[F02]`)
 - **O que você aprende:** Interpretação de logs Postfix/Dovecot, diagnóstico de rejeições, limpeza de fila de emails.
 - ⏱ 40 min de prática | Mailu Operations Guide
