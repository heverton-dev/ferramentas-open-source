# LIVRO-TEXTO EXECUTIVO: SUÍTE SOBERANA DE E-MAIL CORPORATIVO, ARMAZENAMENTO EM NUVEM E COMUNICAÇÃO UNIFICADA

> **Macro-Ecossistema SaaS Alvo:** Penso Suite (Zimbra Collaboration, Penso Drive, Penso Antispam) 
> **Autoridade Emissora:** Fábrica Universal AIDD · Governança Aberta Multi-IDE 
> **Padrão Normativo:** Diamante R5-E Tripartite | **Data de Publicação:** 28/08/2026 
> **Edição:** 1ª Edição Oficial — Desmantelamento Integral de Suítes Proprietárias

---

## SUMÁRIO GERAL DO LIVRO-TEXTO

1. [Prefácio Executivo & Manifesto da Soberania Tecnológica](#prefacio-executivo--manifesto-da-soberania-tecnologica)
2. [Capítulo 1 · Engenharia Financeira, TCO Global & Payback](#capitulo-1--engenharia-financeira-tco-global--payback)
3. [Capítulo 2 · Infraestrutura Global, Dimensionamento da VPS & Provedores Validados](#capitulo-2--infraestrutura-global-dimensionamento-da-vps--provedores-validados)
4. [Capítulo 3 · Matriz Estratégica do Quinteto Soberano](#capitulo-3--matriz-estrategica-do-quinteto-soberano)
5. [Capítulo 4 · Tratados Técnicos Individuais dos Pilares](#capitulo-4--tratados-tecnicos-individuais-dos-pilares)
6. [Capítulo 5 · Camada de Cola, SSO Federado & Blueprints n8n](#capitulo-5--camada-de-cola-sso-federado--blueprints-n8n)
7. [Capítulo 6 · Manual de Engenharia de Infraestrutura & Deploy All-in-One](#capitulo-6--manual-de-engenharia-de-infraestrutura--deploy-all-in-one)
8. [Capítulo 7 · Protocolos de Modularidade & Hot-Swap (Princípio do Lego)](#capitulo-7--protocolos-de-modularidade--hot-swap-principio-do-lego)
9. [Capítulo 8 · Roteiro Prático de Migração de Dados Históricos](#capitulo-8--roteiro-pratico-de-migracao-de-dados-historicos)
10. [Capítulo 9 · Governança Corporativa, Backup 3-2-1 & Conformidade LGPD](#capitulo-9--governanca-corporativa-backup-3-2-1--conformidade-lgpd)
11. [Capítulo 10 · Cronograma de Implantação em 30 Dias & Monitoramento da VPS](#capitulo-10--cronograma-de-implantacao-em-30-dias--monitoramento-da-vps)

---

## PREFÁCIO EXECUTIVO & MANIFESTO DA SOBERANIA TECNOLÓGICA

Dossiê executivo e manual de engenharia para substituir 100% dos serviços de e-mail corporativo, groupware, compartilhamento de arquivos em nuvem e mensageria em equipe da Penso Tecnologia por uma infraestrutura open source soberana, auditável e de altíssimo desempenho.

A dependência crônica de suítes de software como serviço (SaaS) impõe três vulnerabilidades críticas a qualquer organização em crescimento:
1. **Risco de Lock-in Financeiro:** Reajustes anuais unilaterais de 15% a 25% e cobranças por contatos/usuários que penalizam o crescimento da empresa;
2. **Perda de Soberania sobre os Dados:** Informações confidenciais de clientes, negociações e inteligência comercial hospedadas em bancos multi-tenant de terceiros;
3. **Rigidez Operacional:** Impossibilidade de customizar código, adaptar telas ou integrar APIs sem pagar planos 'Enterprise' proibitivos.

Este livro-texto consolida a alternativa definitiva: a **migração para uma arquitetura open source auto-hospedada, soberana, de alto desempenho e com payback inferior a 30 dias**.

---

## CAPÍTULO 1 · ENGENHARIA FINANCEIRA, TCO GLOBAL & PAYBACK

### Demonstrativo Contábil Consolidado (Base Anual)
- **Custo Total SaaS Proprietário (Penso Suite (Zimbra Collaboration, Penso Drive, Penso Antispam)):** `R$ 54.000/ano`
- **Custo de Infraestrutura VPS Própria (Cluster Unificado 8 vCPU / 16 GB):** `R$ 4.200/ano`
- **Economia Líquida Anual no Caixa:** `R$ 49.800/ano`
- **Retorno sobre o Investimento (ROI / Payback):** `0.9 meses`

### Desmembramento de Custos e Economia por Frente de Negócio
| Frente de Negócio | Módulo SaaS Proprietário | Custo SaaS Anual | Custo VPS Alocado | Economia Anual Líquida | Margem de Economia |
|---|---|---|---|---|---|

---

## CAPÍTULO 2 · INFRAESTRUTURA GLOBAL, DIMENSIONAMENTO DA VPS & PROVEDORES VALIDADOS

> **Perfil de Máquina Recomendado:** `8 vCPU / 16 GB RAM ECC / 160-240 GB NVMe` 
> **Racional de Engenharia:** 

### Provedores de Nuvem Recomendados & Custo Mensal da Infraestrutura
| Provedor de Nuvem | Custo Mensal Estimado | Vantagem Principal & SLA |
|---|---|---|

### Alocação Técnica de Recursos por Serviço (vCPU & RAM)
| Serviço / Módulo | vCPU Alocada | Memória RAM | Motivo Técnico / Gargalo Previsto |
|---|---|---|---|
| **Traefik + Keycloak SSO** | `2 vCPU` | `2.5 GB RAM` | Autenticação federada central e roteamento TLS para toda a suíte |
| **Mailcow Cluster (Postfix + Dovecot + Rspamd + SOGo)** | `4 vCPU` | `8.0 GB RAM` | Processamento de filas SMTP, escaneamento de vírus ClamAV e IMAP |
| **Nextcloud Hub + OnlyOffice Document Server** | `4 vCPU` | `8.0 GB RAM` | Edição de planilhas/documentos e sincronização de arquivos pesados |
| **Mattermost Team Edition + PostgreSQL** | `2 vCPU` | `4.0 GB RAM` | Comunicação em tempo real, canais e persistência de histórico |
| **Jitsi Meet (WebRTC + JVB)** | `2 vCPU` | `3.5 GB RAM` | Encaminhamento de fluxos de áudio e vídeo HD sem transcoding pesado |
| **n8n Workflow Engine + Redis** | `1 vCPU` | `1.5 GB RAM` | Orquestração de eventos e rotinas assíncronas |
| **Margem de Segurança & Cache do SO** | `1 vCPU` | `4.5 GB RAM` | Buffer de I/O em disco NVMe e prevenção contra picos de tráfego |

---

## CAPÍTULO 3 · MATRIZ ESTRATÉGICA DO QUINTETO SOBERANO

| # | Grupo Funcional | Persona | Ferramenta | Módulo SaaS Substituído | Economia Anual | Licença | Repositório |
|---|---|---|---|---|---|---|---|
| 01 | Pilar 01 | Robusta | **Mailcow: dockerized** | Penso Mail Enterprise / Zimbra Network Edition | R$ 24.000/ano | `GPL-3.0` | [GitHub](https://github.com/mailcow/mailcow-dockerized) |
| 02 | Pilar 01 | Completa | **Mailu** | Penso Mail Padrão | R$ 18.000/ano | `MIT` | [GitHub](https://github.com/Mailu/Mailu) |
| 03 | Pilar 01 | Moderna | **Stalwart Mail Server** | Penso Mail High Performance | R$ 18.000/ano | `AGPL-3.0` | [GitHub](https://github.com/stalwartlabs/mail-server) |
| 04 | Pilar 01 | Leve | **Modoboa** | Penso Mail Básico | R$ 14.000/ano | `ISC` | [GitHub](https://github.com/modoboa/modoboa) |
| 05 | Pilar 01 | Simples | **Poste.io** | Penso Mail Start | R$ 12.000/ano | `GPL-2.0` | [GitHub](https://github.com/analogic/poste.io) |
| 06 | Pilar 02 | Robusta | **Nextcloud Hub** | Penso Drive / Google Workspace Drive / Dropbox Business | R$ 18.000/ano | `AGPL-3.0` | [GitHub](https://github.com/nextcloud/server) |
| 07 | Pilar 02 | Robusta | **Seafile** | Penso Drive High Performance | R$ 15.000/ano | `GPL-2.0` | [GitHub](https://github.com/haiwen/seafile) |
| 08 | Pilar 02 | Moderna | **ownCloud Infinite Scale (oCIS)** | Penso Drive Enterprise | R$ 15.000/ano | `Apache-2.0` | [GitHub](https://github.com/owncloud/ocis) |
| 09 | Pilar 02 | Mais Segura e Privada | **CryptPad** | Penso Drive Seguro / Google Docs Privado | R$ 12.000/ano | `AGPL-3.0` | [GitHub](https://github.com/cryptpad/cryptpad) |
| 10 | Pilar 02 | Leve | **Filebrowser** | Penso Drive Básico | R$ 9.600/ano | `Apache-2.0` | [GitHub](https://github.com/filebrowser/filebrowser) |
| 11 | Pilar 03 | Robusta | **Mattermost Team Edition** | Penso Chat / Slack / Microsoft Teams | R$ 12.000/ano | `MIT` | [GitHub](https://github.com/mattermost/mattermost) |
| 12 | Pilar 03 | Moderna | **Matrix Synapse & Element** | Penso Chat Seguro | R$ 10.000/ano | `Apache-2.0` | [GitHub](https://github.com/element-hq/synapse) |
| 13 | Pilar 03 | Completa | **Rocket.Chat** | Penso Chat & Atendimento | R$ 10.000/ano | `MIT` | [GitHub](https://github.com/RocketChat/Rocket.Chat) |
| 14 | Pilar 03 | Mais Focada em Produtividade Assíncrona | **Zulip** | Penso Chat / Slack | R$ 8.000/ano | `Apache-2.0` | [GitHub](https://github.com/zulip/zulip) |
| 15 | Pilar 03 | Simples | **Jitsi Meet** | Penso Meet / Zoom Pro / Google Meet | R$ 8.000/ano | `Apache-2.0` | [GitHub](https://github.com/jitsi/jitsi-meet) |

---

## CAPÍTULO 4 · TRATADOS TÉCNICOS INDIVIDUAIS DOS PILARES

### PILAR 01: PILAR 01: E-MAIL CORPORATIVO, GROUPWARE & GATEWAY ANTISPAM
> **Alvo SaaS Substituído:** `Penso Mail / Zimbra Collaboration / Penso Antispam` | **Economia do Pilar:** `R$ 24.000/ano` 
> **Descrição Estratégica:** Servidores de correio eletrônico corporativo com suporte completo a protocolos IMAP, POP3, SMTP, ActiveSync (Exchange ActiveSync), calendários CalDAV, contatos CardDAV e proteção perimetral antispam com Rspamd, ClamAV e assinaturas DKIM/DMARC.

#### 01. Mailcow: dockerized · Suíte Moderna de E-mail Corporativo com Rspamd, SOGo Groupware e ActiveSync (Classificação: Persona Robusta)
- **Módulo SaaS Substituído:** `Penso Mail Enterprise / Zimbra Network Edition`
- **Economia Anual Individual:** `R$ 24.000/ano` | **Licença OSI:** `GPL-3.0`
- **Papel no Ecossistema:** Servidor de correio primário com painel administrativo multi-domínio, webmail SOGo e filtro antispam integrado.

**1. O Que Faz & Como Funciona:** 
Gerencia caixas postais corporativas, filas SMTP, roteamento de domínios e proteção antispam com aprendizado bayesiano. Orquestração em contêineres Docker interligados por rede interna, utilizando Postfix para MTA, Dovecot para IMAP/LMTP, Nginx para proxy reverso e SOGo para webmail e groupware.
```bash
# Inicialização Rápida via Docker / CLI
git clone https://github.com/mailcow/mailcow-dockerized && cd mailcow-dockerized && ./generate_config.sh && docker compose up -d
```

**2. Racional Financeiro da Escolha:** 
Solução conteinerizada líder mundial com arquitetura modular, atualizações automáticas via script, suporte nativo a 2FA/FIDO2, ActiveSync para dispositivos móveis e integração direta com Rspamd.

**3. Requisitos de Infraestrutura & Veredito Técnico:** 
- Memória RAM Mínima: `4 GB`
- CPU Recomendada: `2 vCPU`
- Imagem Docker Oficial: `mailcow/postfix:latest`
- Banco de Dados / Persistência: `MariaDB / Redis`
- **Veredito da Engenharia:** *A escolha mais sólida e testada em batalha para substituição direta de servidores Zimbra corporativos com zero perda de recursos.*

**4. Guia Prático de Uso em 3 Passos:** 
1. **Configuração de DNS Autoritativo:** Crie registros MX, SPF (v=spf1 mx ~all), DKIM e DMARC (v=DMARC1; p=quarantine) no provedor DNS do domínio corporativo.
2. **Provisionamento do Mailcow:** Execute generate_config.sh informando o FQDN (mail.empresa.com.br) e suba o cluster com docker compose up -d.
3. **Criação de Caixas Postais & Migração:** Acesse a interface de administração, configure o domínio e utilize o módulo de sincronização IMAP (Syncjob) para puxar as mensagens do Zimbra antigo.

**5. White-Label & Design System:** 
- Nível de Esforço: `Baixo` | Stack UI: `SOGo Webmail / Bootstrap CSS`
- Mecânica de Customização: Customização de logos, cores institucionais e favicon diretamente via painel administrativo do Mailcow.
- Manutenibilidade de Temas: Persistente entre atualizações de contêineres através de volumes mapeados.

**6. Ecossistema Agêntico (MCPs, Skills & Extensões):** 
- **[CLI] mailcow-cli:** Automação de provisionamento de caixas postais via terminal (`https://github.com/mailcow/mailcow-cli`)
- **[Plugin] Nextcloud Mail Integration:** Conector Oauth2/IMAP para leitura de mensagens no painel da nuvem (`https://apps.nextcloud.com/apps/mail`)

**7. Documentação Operacional & Capacitação Técnica Dedicada:** 
- [Manual de Engenharia de VPS & Desinstalação Cirúrgica (HTML)](../05-manuais-e-trilhas-individuais/mailcow/manuais/manual-mailcow-vps-e-uso.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/mailcow/manuais/manual-mailcow-vps-e-uso.md)
- [Trilha Didática de Aprendizado em 5 Aulas (HTML)](../05-manuais-e-trilhas-individuais/mailcow/trilhas/trilha-mailcow-aprendizado.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/mailcow/trilhas/trilha-mailcow-aprendizado.md)

- **Repositório Oficial:** [https://github.com/mailcow/mailcow-dockerized](https://github.com/mailcow/mailcow-dockerized)

#### 02. Mailu · Servidor de E-mail Leve, Modular e Focado em Simplicidade Operacional (Classificação: Persona Completa)
- **Módulo SaaS Substituído:** `Penso Mail Padrão`
- **Economia Anual Individual:** `R$ 18.000/ano` | **Licença OSI:** `MIT`
- **Papel no Ecossistema:** Alternativa de correio eletrônico com baixo consumo de memória e painel administrativo intuitivo.

**1. O Que Faz & Como Funciona:** 
Entrega servidor de e-mail seguro com suporte a Webmail, antispam, antivírus e administração centralizada. Usa Postfix, Dovecot e Rspamd com gerador de docker-compose oficial para deploy personalizado.
```bash
# Inicialização Rápida via Docker / CLI
curl -sSL https://setup.mailu.io -o setup.py && python3 setup.py
```

**2. Racional Financeiro da Escolha:** 
Arquitetura limpa sem componentes legados, com suporte nativo a Roundcube ou SnappyMail e excelente integração com clientes desktop Thunderbird e Outlook.

**3. Requisitos de Infraestrutura & Veredito Técnico:** 
- Memória RAM Mínima: `2 GB`
- CPU Recomendada: `2 vCPU`
- Imagem Docker Oficial: `mailu/admin:latest`
- Banco de Dados / Persistência: `PostgreSQL / SQLite`
- **Veredito da Engenharia:** *Excelente para equipes que buscam facilidade de manutenção e menor consumo de recursos de VPS.*

**4. Guia Prático de Uso em 3 Passos:** 
1. **Geração do Manifesto:** Utilize o assistente oficial para selecionar os módulos desejados (Roundcube, Antivírus, Fetchmail).
2. **Deploy via Docker Compose:** Suba o cluster com docker compose -p mailu up -d e crie o usuário root inicial.
3. **Validação de Reputação IP:** Teste o envio para ferramentas de validação de entregabilidade (Mail-Tester) visando nota 10/10.

**5. White-Label & Design System:** 
- Nível de Esforço: `Médio` | Stack UI: `Roundcube / SnappyMail Skin`
- Mecânica de Customização: Aplicação de CSS customizado e skins temáticas na interface do webmail.
- Manutenibilidade de Temas: Alta estabilidade.

**6. Ecossistema Agêntico (MCPs, Skills & Extensões):** 
- **[API] Mailu REST API:** API REST nativa para criação automática de e-mails em onboarding de funcionários (`https://mailu.io/api`)

**7. Documentação Operacional & Capacitação Técnica Dedicada:** 
- [Manual de Engenharia de VPS & Desinstalação Cirúrgica (HTML)](../05-manuais-e-trilhas-individuais/mailu/manuais/manual-mailu-vps-e-uso.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/mailu/manuais/manual-mailu-vps-e-uso.md)
- [Trilha Didática de Aprendizado em 5 Aulas (HTML)](../05-manuais-e-trilhas-individuais/mailu/trilhas/trilha-mailu-aprendizado.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/mailu/trilhas/trilha-mailu-aprendizado.md)

- **Repositório Oficial:** [https://github.com/Mailu/Mailu](https://github.com/Mailu/Mailu)

#### 03. Stalwart Mail Server · Servidor de Correio All-in-One de Próxima Geração em Rust (Classificação: Persona Moderna)
- **Módulo SaaS Substituído:** `Penso Mail High Performance`
- **Economia Anual Individual:** `R$ 18.000/ano` | **Licença OSI:** `AGPL-3.0`
- **Papel no Ecossistema:** Servidor de alta densidade com suporte nativo a JMAP, IMAP, SMTP e DMARC em binário único compilado.

**1. O Que Faz & Como Funciona:** 
Unifica servidor SMTP, IMAP, JMAP, antispam e gerenciador de chaves criptográficas em um único serviço ultra-rápido. Arquitetura assíncrona em Rust com backend de armazenamento flexível (RocksDB, S3 ou SQL).
```bash
# Inicialização Rápida via Docker / CLI
docker run -d --name stalwart -p 25:25 -p 993:993 -p 8080:8080 stalwartlabs/mail-server:latest
```

**2. Racional Financeiro da Escolha:** 
Desenvolvido em Rust com zero memory-leaks, suporte nativo ao protocolo moderno JMAP e altíssima velocidade de busca e indexação.

**3. Requisitos de Infraestrutura & Veredito Técnico:** 
- Memória RAM Mínima: `1 GB`
- CPU Recomendada: `1 vCPU`
- Imagem Docker Oficial: `stalwartlabs/mail-server:latest`
- Banco de Dados / Persistência: `RocksDB / PostgreSQL`
- **Veredito da Engenharia:** *A solução de engenharia mais avançada tecnologicamente para servidores de e-mail corporativos da próxima década.*

**4. Guia Prático de Uso em 3 Passos:** 
1. **Inicialização:** Suba o contêiner Stalwart com persistência de volumes.
2. **Configuração Web GUI:** Acesse a porta 8080 para definir domínios, chaves DKIM e políticas de quota.
3. **Integração JMAP/IMAP:** Conecte clientes modernos que suportam o protocolo rápido JMAP.

**5. White-Label & Design System:** 
- Nível de Esforço: `Baixo` | Stack UI: `Web Admin Moderno`
- Mecânica de Customização: Temas nativos no painel de controle.
- Manutenibilidade de Temas: Alta.

**6. Ecossistema Agêntico (MCPs, Skills & Extensões):** 
- **[CLI] stalwart-cli:** Ferramenta de linha de comando para administração avançada (`https://github.com/stalwartlabs/cli`)

**7. Documentação Operacional & Capacitação Técnica Dedicada:** 
- [Manual de Engenharia de VPS & Desinstalação Cirúrgica (HTML)](../05-manuais-e-trilhas-individuais/stalwart-mail/manuais/manual-stalwart-mail-vps-e-uso.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/stalwart-mail/manuais/manual-stalwart-mail-vps-e-uso.md)
- [Trilha Didática de Aprendizado em 5 Aulas (HTML)](../05-manuais-e-trilhas-individuais/stalwart-mail/trilhas/trilha-stalwart-mail-aprendizado.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/stalwart-mail/trilhas/trilha-stalwart-mail-aprendizado.md)

- **Repositório Oficial:** [https://github.com/stalwartlabs/mail-server](https://github.com/stalwartlabs/mail-server)

#### 04. Modoboa · Plataforma de E-mail Corporativo e Groupware Baseada em Python e Django (Classificação: Persona Leve)
- **Módulo SaaS Substituído:** `Penso Mail Básico`
- **Economia Anual Individual:** `R$ 14.000/ano` | **Licença OSI:** `ISC`
- **Papel no Ecossistema:** Painel de administração modular com webmail integrado e monitoramento de reputação.

**1. O Que Faz & Como Funciona:** 
Fornece interface web completa para gestão de correio, quarentena de spam e estatísticas de tráfego. Integra Postfix, Dovecot, Amavis/Rspamd e banco PostgreSQL através de uma API em Django.
```bash
# Inicialização Rápida via Docker / CLI
git clone https://github.com/modoboa/modoboa-installer && cd modoboa-installer && python3 run.py <seu-dominio.com.br>
```

**2. Racional Financeiro da Escolha:** 
Código legível em Python/Django, instalador automatizado para Debian/Ubuntu e plugins para relatórios de tráfego de e-mail.

**3. Requisitos de Infraestrutura & Veredito Técnico:** 
- Memória RAM Mínima: `2 GB`
- CPU Recomendada: `1 vCPU`
- Imagem Docker Oficial: `modoboa/modoboa:latest`
- Banco de Dados / Persistência: `PostgreSQL`
- **Veredito da Engenharia:** *Perfeito para ambientes que necessitam de customização em Python e integração com portais corporativos existentes.*

**4. Guia Prático de Uso em 3 Passos:** 
1. **Execução do Instalador:** Rode o modoboa-installer no Ubuntu Server limpo.
2. **Parametrização:** Defina limites de envio por domínio e regras de quarentena.
3. **Habilitação de Autenticação:** Conecte com diretórios LDAP/Active Directory se necessário.

**5. White-Label & Design System:** 
- Nível de Esforço: `Médio` | Stack UI: `Django Templates / CSS`
- Mecânica de Customização: Customização de templates HTML corporativos.
- Manutenibilidade de Temas: Estável.

**6. Ecossistema Agêntico (MCPs, Skills & Extensões):** 
- **[Plugin] Modoboa Radicale:** Servidor CalDAV/CardDAV integrado para sincronização de contatos e calendários (`https://github.com/modoboa/modoboa-radicale`)

**7. Documentação Operacional & Capacitação Técnica Dedicada:** 
- [Manual de Engenharia de VPS & Desinstalação Cirúrgica (HTML)](../05-manuais-e-trilhas-individuais/modoboa/manuais/manual-modoboa-vps-e-uso.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/modoboa/manuais/manual-modoboa-vps-e-uso.md)
- [Trilha Didática de Aprendizado em 5 Aulas (HTML)](../05-manuais-e-trilhas-individuais/modoboa/trilhas/trilha-modoboa-aprendizado.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/modoboa/trilhas/trilha-modoboa-aprendizado.md)

- **Repositório Oficial:** [https://github.com/modoboa/modoboa](https://github.com/modoboa/modoboa)

#### 05. Poste.io · Servidor de E-mail Completo em Contêiner Único com Painel Administrativo Ágil (Classificação: Persona Simples)
- **Módulo SaaS Substituído:** `Penso Mail Start`
- **Economia Anual Individual:** `R$ 12.000/ano` | **Licença OSI:** `GPL-2.0`
- **Papel no Ecossistema:** Solução de deploy instantâneo para empresas que necessitam de correio eletrônico seguro com manutenção zero.

**1. O Que Faz & Como Funciona:** 
Provê serviço completo de correio eletrônico corporativo em um único contêiner autossuficiente. Combina Haraka/Postfix com Dovecot e painel em PHP/SQLite em imagem única otimizada.
```bash
# Inicialização Rápida via Docker / CLI
docker run -d --name mail -p 25:25 -p 80:80 -p 443:443 -p 993:993 -v /opt/mail/data:/data analogic/poste.io
```

**2. Racional Financeiro da Escolha:** 
Empacotado em uma única imagem Docker, inclui Webmail Roundcube, antispam Rspamd, antivírus ClamAV e certificado Let's Encrypt automático em 1 comando.

**3. Requisitos de Infraestrutura & Veredito Técnico:** 
- Memória RAM Mínima: `2 GB`
- CPU Recomendada: `1 vCPU`
- Imagem Docker Oficial: `analogic/poste.io:latest`
- Banco de Dados / Persistência: `SQLite integrado`
- **Veredito da Engenharia:** *A forma mais rápida e descomplicada de subir um servidor de e-mail funcional em menos de 5 minutos.*

**4. Guia Prático de Uso em 3 Passos:** 
1. **Subida do Contêiner:** Execute o comando Docker mapeando as portas padrão de correio.
2. **Assistente Web:** Abra https://ip-vps para criar a senha mestre de administração.
3. **Adição de Domínios:** Cadastre os domínios e gere as chaves DKIM com 1 clique.

**5. White-Label & Design System:** 
- Nível de Esforço: `Baixo` | Stack UI: `Interface Web Limpa`
- Mecânica de Customização: Troca de logotipo institucional no painel.
- Manutenibilidade de Temas: Simples.

**6. Ecossistema Agêntico (MCPs, Skills & Extensões):** 
- **[Skill] E-mail Health Monitor:** Monitoramento de reputação de IP em listas RBL (`scripts/auditar_rbl.py`)

**7. Documentação Operacional & Capacitação Técnica Dedicada:** 
- [Manual de Engenharia de VPS & Desinstalação Cirúrgica (HTML)](../05-manuais-e-trilhas-individuais/poste-io/manuais/manual-poste-io-vps-e-uso.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/poste-io/manuais/manual-poste-io-vps-e-uso.md)
- [Trilha Didática de Aprendizado em 5 Aulas (HTML)](../05-manuais-e-trilhas-individuais/poste-io/trilhas/trilha-poste-io-aprendizado.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/poste-io/trilhas/trilha-poste-io-aprendizado.md)

- **Repositório Oficial:** [https://github.com/analogic/poste.io](https://github.com/analogic/poste.io)

### PILAR 02: PILAR 02: ARMAZENAMENTO EM NUVEM, DRIVE CORPORATIVO & DOCUMENTOS
> **Alvo SaaS Substituído:** `Penso Drive / Google Drive / OneDrive` | **Economia do Pilar:** `R$ 18.000/ano` 
> **Descrição Estratégica:** Plataforma centralizada de arquivos corporativos com sincronização desktop/mobile, compartilhamento seguro de links com expiração e senha, edição colaborativa de planilhas e documentos em tempo real e controle de versionamento.

#### 06. Nextcloud Hub · A Plataforma de Produtividade e Armazenamento Soberana Líder Mundial (Classificação: Persona Robusta)
- **Módulo SaaS Substituído:** `Penso Drive / Google Workspace Drive / Dropbox Business`
- **Economia Anual Individual:** `R$ 18.000/ano` | **Licença OSI:** `AGPL-3.0`
- **Papel no Ecossistema:** Nuvem central corporativa para arquivos, documentos com OnlyOffice, calendários, contatos e formulários.

**1. O Que Faz & Como Funciona:** 
Armazena, versiona e compartilha arquivos corporativos com suporte a edição online de planilhas, apresentações e textos. Backend PHP/PostgreSQL com Redis para locking transacional e OnlyOffice Document Server integrado para edição colaborativa.
```bash
# Inicialização Rápida via Docker / CLI
docker compose up -d nextcloud nextcloud-db redis onlyoffice
```

**2. Racional Financeiro da Escolha:** 
Padrão de ouro de governança de dados na Europa e no setor público brasileiro. Suporte a criptografia ponta a ponta, auditoria de acessos LGPD, clientes para Windows, Mac, Linux, Android e iOS.

**3. Requisitos de Infraestrutura & Veredito Técnico:** 
- Memória RAM Mínima: `4 GB`
- CPU Recomendada: `2 vCPU`
- Imagem Docker Oficial: `nextcloud:apache`
- Banco de Dados / Persistência: `PostgreSQL / Redis`
- **Veredito da Engenharia:** *A substituição definitiva para o Penso Drive e Google Drive, com soberania total de arquivos e suporte nativo a OnlyOffice.*

**4. Guia Prático de Uso em 3 Passos:** 
1. **Deploy do Nextcloud Hub:** Suba o compose com PostgreSQL, Redis e OnlyOffice Document Server configurados.
2. **Configuração de Armazenamento:** Mapeie o volume NVMe local ou storage corporativo via S3/MinIO para expansão elástica.
3. **Distribuição de Clientes:** Instale o cliente Nextcloud Desktop nos computadores dos colaboradores com sincronização seletiva.

**5. White-Label & Design System:** 
- Nível de Esforço: `Baixo` | Stack UI: `Nextcloud Theming (Nativo)`
- Mecânica de Customização: Aplicação de logotipo, cores da marca corporativa, background e slogan diretamente nas configurações de administração.
- Manutenibilidade de Temas: 100% nativo e imune a atualizações de versão.

**6. Ecossistema Agêntico (MCPs, Skills & Extensões):** 
- **[Extensão] OnlyOffice Docs:** Editor colaborativo de documentos compatível com DOCX, XLSX e PPTX (`https://github.com/ONLYOFFICE/DocumentServer`)
- **[Plugin] Nextcloud Group Folders:** Pastas departamentais com controle granular de permissões por grupo (`https://apps.nextcloud.com/apps/groupfolders`)

**7. Documentação Operacional & Capacitação Técnica Dedicada:** 
- [Manual de Engenharia de VPS & Desinstalação Cirúrgica (HTML)](../05-manuais-e-trilhas-individuais/nextcloud/manuais/manual-nextcloud-vps-e-uso.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/nextcloud/manuais/manual-nextcloud-vps-e-uso.md)
- [Trilha Didática de Aprendizado em 5 Aulas (HTML)](../05-manuais-e-trilhas-individuais/nextcloud/trilhas/trilha-nextcloud-aprendizado.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/nextcloud/trilhas/trilha-nextcloud-aprendizado.md)

- **Repositório Oficial:** [https://github.com/nextcloud/server](https://github.com/nextcloud/server)

#### 07. Seafile · Sistema de Sincronização e Armazenamento de Arquivos de Alta Velocidade em C/Python (Classificação: Persona Robusta)
- **Módulo SaaS Substituído:** `Penso Drive High Performance`
- **Economia Anual Individual:** `R$ 15.000/ano` | **Licença OSI:** `GPL-2.0`
- **Papel no Ecossistema:** Drive corporativo focado em máxima velocidade de transferência de arquivos grandes e baixo uso de CPU/RAM.

**1. O Que Faz & Como Funciona:** 
Sincroniza bibliotecas de arquivos com alta velocidade, controle de versão infinito e drive virtual montado no Windows Explorer. Servidor C/C++ (seafile-server) com interface Seahub em Python/Django e banco MySQL/PostgreSQL.
```bash
# Inicialização Rápida via Docker / CLI
docker compose up -d seafile seafile-mysql seafile-memcached
```

**2. Racional Financeiro da Escolha:** 
Escrito em linguagem C no núcleo de sincronização, possui algoritmo de deduplicação de blocos (delta sync) superior a soluções puramente PHP.

**3. Requisitos de Infraestrutura & Veredito Técnico:** 
- Memória RAM Mínima: `2 GB`
- CPU Recomendada: `1 vCPU`
- Imagem Docker Oficial: `seafileltd/seafile-mc:latest`
- Banco de Dados / Persistência: `MariaDB / Memcached`
- **Veredito da Engenharia:** *A escolha ideal para escritórios e agências que manipulam gigabytes diários de arquivos pesados com sincronização em tempo real.*

**4. Guia Prático de Uso em 3 Passos:** 
1. **Deploy Docker:** Suba o Seafile Community Server com compose oficial.
2. **Criação de Bibliotecas:** Estruture as bibliotecas por departamento com criptografia opcional no cliente.
3. **Montagem do Drive Virtual:** Utilize o Seafile Drive Client para acessar os arquivos sem ocupar espaço em disco local.

**5. White-Label & Design System:** 
- Nível de Esforço: `Médio` | Stack UI: `Seahub CSS`
- Mecânica de Customização: Substituição de arquivos de logo e CSS corporativo em pasta de customização mapeada.
- Manutenibilidade de Temas: Alta.

**6. Ecossistema Agêntico (MCPs, Skills & Extensões):** 
- **[Driver] Seafile Drive Client:** Monta a nuvem como disco rígido virtual (ex: S:) no Windows (`https://www.seafile.com/en/download/`)

**7. Documentação Operacional & Capacitação Técnica Dedicada:** 
- [Manual de Engenharia de VPS & Desinstalação Cirúrgica (HTML)](../05-manuais-e-trilhas-individuais/seafile/manuais/manual-seafile-vps-e-uso.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/seafile/manuais/manual-seafile-vps-e-uso.md)
- [Trilha Didática de Aprendizado em 5 Aulas (HTML)](../05-manuais-e-trilhas-individuais/seafile/trilhas/trilha-seafile-aprendizado.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/seafile/trilhas/trilha-seafile-aprendizado.md)

- **Repositório Oficial:** [https://github.com/haiwen/seafile](https://github.com/haiwen/seafile)

#### 08. ownCloud Infinite Scale (oCIS) · Nuvem Corporativa Moderna em Go e Microserviços Cloud-Native (Classificação: Persona Moderna)
- **Módulo SaaS Substituído:** `Penso Drive Enterprise`
- **Economia Anual Individual:** `R$ 15.000/ano` | **Licença OSI:** `Apache-2.0`
- **Papel no Ecossistema:** Armazenamento corporativo desacoplado de banco relacional clássico, projetado para alta escalabilidade.

**1. O Que Faz & Como Funciona:** 
Gerencia arquivos em nuvem com arquitetura de microserviços e alta concorrência de usuários. Binário único em Go que orquestra serviços de metadados, armazenamento e API OIDC.
```bash
# Inicialização Rápida via Docker / CLI
docker run -d --name ocis -p 9200:9200 -e OCIS_INSECURE=true owncloud/ocis:latest
```

**2. Racional Financeiro da Escolha:** 
Desenvolvido em Go (Golang) com frontend em Vue.js, inicialização instantânea em binário único e compatibilidade nativa com armazenamento S3.

**3. Requisitos de Infraestrutura & Veredito Técnico:** 
- Memória RAM Mínima: `1 GB`
- CPU Recomendada: `1 vCPU`
- Imagem Docker Oficial: `owncloud/ocis:latest`
- Banco de Dados / Persistência: `Armazenamento nativo / S3`
- **Veredito da Engenharia:** *Excelente para arquiteturas corporativas modernas que buscam eliminar a sobrecarga de bancos relacionais.*

**4. Guia Prático de Uso em 3 Passos:** 
1. **Inicialização:** Execute o contêiner oCIS definindo a URL pública corporativa.
2. **Integração Keycloak:** Conecte o serviço de autenticação OIDC nativo ao Keycloak corporativo.
3. **Configuração de Spaces:** Crie Espaços de Trabalho compartilhados para cada equipe.

**5. White-Label & Design System:** 
- Nível de Esforço: `Baixo` | Stack UI: `ownCloud Web (Vue.js)`
- Mecânica de Customização: Customização de temas via arquivos JSON de configuração de branding.
- Manutenibilidade de Temas: Excelente.

**6. Ecossistema Agêntico (MCPs, Skills & Extensões):** 
- **[CLI] ocis-cli:** CLI nativa para administração e automação de quotas (`https://owncloud.dev/ocis/`)

**7. Documentação Operacional & Capacitação Técnica Dedicada:** 
- [Manual de Engenharia de VPS & Desinstalação Cirúrgica (HTML)](../05-manuais-e-trilhas-individuais/owncloud-ocis/manuais/manual-owncloud-ocis-vps-e-uso.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/owncloud-ocis/manuais/manual-owncloud-ocis-vps-e-uso.md)
- [Trilha Didática de Aprendizado em 5 Aulas (HTML)](../05-manuais-e-trilhas-individuais/owncloud-ocis/trilhas/trilha-owncloud-ocis-aprendizado.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/owncloud-ocis/trilhas/trilha-owncloud-ocis-aprendizado.md)

- **Repositório Oficial:** [https://github.com/owncloud/ocis](https://github.com/owncloud/ocis)

#### 09. CryptPad · Suíte Colaborativa de Documentos com Criptografia Ponta a Ponta Zero-Knowledge (Classificação: Persona Mais Segura e Privada)
- **Módulo SaaS Substituído:** `Penso Drive Seguro / Google Docs Privado`
- **Economia Anual Individual:** `R$ 12.000/ano` | **Licença OSI:** `AGPL-3.0`
- **Papel no Ecossistema:** Edição de documentos, planilhas, formulários e kanban com criptografia no navegador.

**1. O Que Faz & Como Funciona:** 
Edição de documentos de texto, código, apresentações, enquetes e quadros brancos com proteção total de dados. Backend em Node.js leve que atua como relay criptográfico sem acesso às chaves descriptografadas.
```bash
# Inicialização Rápida via Docker / CLI
docker run -d --name cryptpad -p 3000:3000 -p 3001:3001 cryptpad/cryptpad:latest
```

**2. Racional Financeiro da Escolha:** 
Nem mesmo o administrador da VPS consegue ler o conteúdo dos documentos: a chave criptográfica reside exclusivamente na sessão do usuário no navegador.

**3. Requisitos de Infraestrutura & Veredito Técnico:** 
- Memória RAM Mínima: `1 GB`
- CPU Recomendada: `1 vCPU`
- Imagem Docker Oficial: `cryptpad/cryptpad:latest`
- Banco de Dados / Persistência: `Armazenamento em arquivo plano`
- **Veredito da Engenharia:** *A solução definitiva para departamentos jurídicos, diretoria e compliance que exigem sigilo absoluto de documentos.*

**4. Guia Prático de Uso em 3 Passos:** 
1. **Provisionamento de Domínio:** Configure os 2 domínios necessários (domínio principal e sandbox) para isolamento do navegador.
2. **Subida do Contêiner:** Execute o CryptPad com Docker e proxy Traefik com TLS.
3. **Criação do Painel do Admin:** Gere a conta administrativa com chave de recuperação física.

**5. White-Label & Design System:** 
- Nível de Esforço: `Baixo` | Stack UI: `Interface Web Minimalista`
- Mecânica de Customização: Customização de logos e cores via config.js.
- Manutenibilidade de Temas: Alta.

**6. Ecossistema Agêntico (MCPs, Skills & Extensões):** 
- **[Skill] CryptPad DRP Guard:** Rotina de backup criptografado do storage do CryptPad (`scripts/backup_cryptpad.sh`)

**7. Documentação Operacional & Capacitação Técnica Dedicada:** 
- [Manual de Engenharia de VPS & Desinstalação Cirúrgica (HTML)](../05-manuais-e-trilhas-individuais/cryptpad/manuais/manual-cryptpad-vps-e-uso.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/cryptpad/manuais/manual-cryptpad-vps-e-uso.md)
- [Trilha Didática de Aprendizado em 5 Aulas (HTML)](../05-manuais-e-trilhas-individuais/cryptpad/trilhas/trilha-cryptpad-aprendizado.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/cryptpad/trilhas/trilha-cryptpad-aprendizado.md)

- **Repositório Oficial:** [https://github.com/cryptpad/cryptpad](https://github.com/cryptpad/cryptpad)

#### 10. Filebrowser · Gerenciador de Arquivos Web Ultra-Leve em Binário Único Go (Classificação: Persona Leve)
- **Módulo SaaS Substituído:** `Penso Drive Básico`
- **Economia Anual Individual:** `R$ 9.600/ano` | **Licença OSI:** `Apache-2.0`
- **Papel no Ecossistema:** Painel de acesso rápido e compartilhamento de arquivos sem peso computacional.

**1. O Que Faz & Como Funciona:** 
Provê interface web intuitiva para upload, download, pré-visualização de imagens/vídeos e gerenciamento de arquivos na VPS. Binário compilado em Go com banco SQLite e interface SPA em Vue.js.
```bash
# Inicialização Rápida via Docker / CLI
docker run -d --name filebrowser -p 8080:80 -v /srv/files:/srv -v /opt/filebrowser/database.db:/database.db filebrowser/filebrowser:latest
```

**2. Racional Financeiro da Escolha:** 
Consome menos de 30 MB de RAM, suporta múltiplos usuários com permissões específicas de diretório e links de download públicos.

**3. Requisitos de Infraestrutura & Veredito Técnico:** 
- Memória RAM Mínima: `256 MB`
- CPU Recomendada: `0.5 vCPU`
- Imagem Docker Oficial: `filebrowser/filebrowser:latest`
- Banco de Dados / Persistência: `SQLite integrado`
- **Veredito da Engenharia:** *A solução mais leve existente para compartilhar e gerenciar arquivos corporativos com consumo quase nulo de hardware.*

**4. Guia Prático de Uso em 3 Passos:** 
1. **Subida do Contêiner:** Mapeie a pasta de arquivos e suba o contêiner em 2 segundos.
2. **Criação de Usuários:** Cadastre os usuários com permissões de leitura/escrita por pasta.
3. **Geração de Links:** Compartilhe links públicos com tempo de expiração e senha.

**5. White-Label & Design System:** 
- Nível de Esforço: `Baixo` | Stack UI: `Vue.js SPA`
- Mecânica de Customização: Customização de título e cores via painel de configurações.
- Manutenibilidade de Temas: Simples.

**6. Ecossistema Agêntico (MCPs, Skills & Extensões):** 
- **[CLI] filebrowser-cli:** CLI nativa para gerenciamento de usuários em lote (`https://filebrowser.org/cli`)

**7. Documentação Operacional & Capacitação Técnica Dedicada:** 
- [Manual de Engenharia de VPS & Desinstalação Cirúrgica (HTML)](../05-manuais-e-trilhas-individuais/filebrowser/manuais/manual-filebrowser-vps-e-uso.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/filebrowser/manuais/manual-filebrowser-vps-e-uso.md)
- [Trilha Didática de Aprendizado em 5 Aulas (HTML)](../05-manuais-e-trilhas-individuais/filebrowser/trilhas/trilha-filebrowser-aprendizado.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/filebrowser/trilhas/trilha-filebrowser-aprendizado.md)

- **Repositório Oficial:** [https://github.com/filebrowser/filebrowser](https://github.com/filebrowser/filebrowser)

### PILAR 03: PILAR 03: COMUNICAÇÃO UNIFICADA, CHAT CORPORATIVO & VIDEOCONFERÊNCIA
> **Alvo SaaS Substituído:** `Penso Chat / Microsoft Teams / Slack / Zoom` | **Economia do Pilar:** `R$ 12.000/ano` 
> **Descrição Estratégica:** Ambiente centralizado de comunicação em equipe com canais públicos e privados, mensagens diretas, integração com bots, compartilhamento de tela e videoconferências em alta definição sem limite de tempo por reunião.

#### 11. Mattermost Team Edition · A Plataforma de Mensageria Segura e Operações para Empresas Líder de Mercado (Classificação: Persona Robusta)
- **Módulo SaaS Substituído:** `Penso Chat / Slack / Microsoft Teams`
- **Economia Anual Individual:** `R$ 12.000/ano` | **Licença OSI:** `MIT`
- **Papel no Ecossistema:** Hub central de comunicação corporativa, canais departamentais, playbooks e chamadas de voz.

**1. O Que Faz & Como Funciona:** 
Gerencia mensagens instantâneas, canais por projetos, integrações com sistemas legados e quadros de tarefas (Boards). Backend em Go de altíssima concorrência com PostgreSQL e interface moderna em React/Redux.
```bash
# Inicialização Rápida via Docker / CLI
git clone https://github.com/mattermost/docker && cd docker && docker compose -f docker-compose.yml -f docker-compose.without-nginx.yml up -d
```

**2. Racional Financeiro da Escolha:** 
Substituição completa do Slack/Teams com aplicativos nativos para Windows, Mac, Linux, iOS e Android, suporte a LDAP/SAML/OIDC, webhooks ilimitados e total soberania de dados.

**3. Requisitos de Infraestrutura & Veredito Técnico:** 
- Memória RAM Mínima: `2 GB`
- CPU Recomendada: `2 vCPU`
- Imagem Docker Oficial: `mattermost/mattermost-team-edition:latest`
- Banco de Dados / Persistência: `PostgreSQL`
- **Veredito da Engenharia:** *A plataforma de chat corporativo mais madura, confiável e adotada por grandes corporações globais.*

**4. Guia Prático de Uso em 3 Passos:** 
1. **Deploy do Cluster Mattermost:** Execute o compose com PostgreSQL e crie o usuário System Admin inicial.
2. **Estruturação de Canais:** Crie os times corporativos e canais padrão por departamento (Geral, Vendas, TI, Suporte).
3. **Integração de Webhooks:** Conecte o Mattermost ao n8n e aos alertas de infraestrutura para notificações automáticas.

**5. White-Label & Design System:** 
- Nível de Esforço: `Baixo` | Stack UI: `React Web / Custom CSS`
- Mecânica de Customização: Customização de logotipo, nome da empresa, tela de login e temas de cores diretamente pelo painel.
- Manutenibilidade de Temas: Nativa e mantida entre deploys.

**6. Ecossistema Agêntico (MCPs, Skills & Extensões):** 
- **[Plugin] Mattermost Boards (Focalboard):** Gestão de projetos estilo Trello integrada dentro dos canais de chat (`https://github.com/mattermost/focalboard`)
- **[Plugin] Mattermost Calls:** Chamadas de voz e compartilhamento de tela com 1 clique direto no canal (`https://github.com/mattermost/mattermost-plugin-calls`)

**7. Documentação Operacional & Capacitação Técnica Dedicada:** 
- [Manual de Engenharia de VPS & Desinstalação Cirúrgica (HTML)](../05-manuais-e-trilhas-individuais/mattermost/manuais/manual-mattermost-vps-e-uso.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/mattermost/manuais/manual-mattermost-vps-e-uso.md)
- [Trilha Didática de Aprendizado em 5 Aulas (HTML)](../05-manuais-e-trilhas-individuais/mattermost/trilhas/trilha-mattermost-aprendizado.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/mattermost/trilhas/trilha-mattermost-aprendizado.md)

- **Repositório Oficial:** [https://github.com/mattermost/mattermost](https://github.com/mattermost/mattermost)

#### 12. Matrix Synapse & Element · Rede Aberta e Federada de Comunicação Segura com Criptografia Ponta a Ponta (Classificação: Persona Moderna)
- **Módulo SaaS Substituído:** `Penso Chat Seguro`
- **Economia Anual Individual:** `R$ 10.000/ano` | **Licença OSI:** `Apache-2.0`
- **Papel no Ecossistema:** Protocolo de comunicação descentralizado para conversas corporativas ultra-seguras.

**1. O Que Faz & Como Funciona:** 
Provê servidor de mensageria federada com salas criptografadas, chamadas de áudio/vídeo e controle granular de chaves. Servidor Synapse (Python/Rust) conectado a banco PostgreSQL com cliente web/desktop Element.
```bash
# Inicialização Rápida via Docker / CLI
docker compose up -d synapse synapse-db element-web
```

**2. Racional Financeiro da Escolha:** 
Padrão adotado por governos internacionais para soberania digital, com criptografia nativa Olm/Megolm e possibilidade de federar com outras filiais ou empresas parceiras.

**3. Requisitos de Infraestrutura & Veredito Técnico:** 
- Memória RAM Mínima: `2 GB`
- CPU Recomendada: `2 vCPU`
- Imagem Docker Oficial: `matrixdotorg/synapse:latest`
- Banco de Dados / Persistência: `PostgreSQL`
- **Veredito da Engenharia:** *A melhor escolha para organizações que exigem federação segura entre diferentes domínios e criptografia inquebrável.*

**4. Guia Prático de Uso em 3 Passos:** 
1. **Configuração do Homeserver:** Gere o arquivo homeserver.yaml com o domínio corporativo e chaves de assinatura.
2. **Deploy Synapse & Element:** Suba o servidor e o cliente Element Web com proxy Traefik.
3. **Definição de Políticas de Criptografia:** Habilite a criptografia ponta a ponta (E2EE) obrigatória para todas as salas internas.

**5. White-Label & Design System:** 
- Nível de Esforço: `Médio` | Stack UI: `Element Web (React)`
- Mecânica de Customização: Customização de branding no config.json do Element Web.
- Manutenibilidade de Temas: Alta.

**6. Ecossistema Agêntico (MCPs, Skills & Extensões):** 
- **[Bridge] Matrix Appservice IRC/Slack:** Pontes de integração para conectar o Matrix a canais legados (`https://github.com/matrix-org/matrix-appservice-slack`)

**7. Documentação Operacional & Capacitação Técnica Dedicada:** 
- [Manual de Engenharia de VPS & Desinstalação Cirúrgica (HTML)](../05-manuais-e-trilhas-individuais/matrix-synapse/manuais/manual-matrix-synapse-vps-e-uso.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/matrix-synapse/manuais/manual-matrix-synapse-vps-e-uso.md)
- [Trilha Didática de Aprendizado em 5 Aulas (HTML)](../05-manuais-e-trilhas-individuais/matrix-synapse/trilhas/trilha-matrix-synapse-aprendizado.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/matrix-synapse/trilhas/trilha-matrix-synapse-aprendizado.md)

- **Repositório Oficial:** [https://github.com/element-hq/synapse](https://github.com/element-hq/synapse)

#### 13. Rocket.Chat · Hub de Comunicação Omnichannel e Mensageria Corporativa Segura (Classificação: Persona Completa)
- **Módulo SaaS Substituído:** `Penso Chat & Atendimento`
- **Economia Anual Individual:** `R$ 10.000/ano` | **Licença OSI:** `MIT`
- **Papel no Ecossistema:** Chat corporativo interno com capacidade de atender clientes externos via Livechat e WhatsApp.

**1. O Que Faz & Como Funciona:** 
Centraliza conversas de equipes internas e chats de suporte ao cliente em tempo real. Backend em Node.js com banco de dados MongoDB e suporte a microserviços de alta disponibilidade.
```bash
# Inicialização Rápida via Docker / CLI
docker compose up -d rocketchat rocketchat-mongodb
```

**2. Racional Financeiro da Escolha:** 
Combina comunicação de equipe interna com atendimento a clientes em um único painel, com suporte nativo a automações de atendimento.

**3. Requisitos de Infraestrutura & Veredito Técnico:** 
- Memória RAM Mínima: `2 GB`
- CPU Recomendada: `2 vCPU`
- Imagem Docker Oficial: `registry.rocket.chat/rocketchat/rocket.chat:latest`
- Banco de Dados / Persistência: `MongoDB`
- **Veredito da Engenharia:** *Excelente para empresas que desejam unificar o chat entre funcionários e o atendimento web aos clientes no mesmo sistema.*

**4. Guia Prático de Uso em 3 Passos:** 
1. **Deploy com MongoDB:** Execute o compose com MongoDB com replica set ativo.
2. **Setup Inicial:** Complete o assistente de onboarding e configure o idioma PT-BR corporativo.
3. **Widget de Livechat:** Insira o script do Livechat no site corporativo para recepção de visitantes.

**5. White-Label & Design System:** 
- Nível de Esforço: `Baixo` | Stack UI: `Fuselage / Custom CSS`
- Mecânica de Customização: Painel de personalização de marca nativo.
- Manutenibilidade de Temas: Fácil.

**6. Ecossistema Agêntico (MCPs, Skills & Extensões):** 
- **[App] Rocket.Chat Omnichannel Hub:** Conector para atendimento centralizado multicanal (`https://github.com/RocketChat/Apps.Omnichannel`)

**7. Documentação Operacional & Capacitação Técnica Dedicada:** 
- [Manual de Engenharia de VPS & Desinstalação Cirúrgica (HTML)](../05-manuais-e-trilhas-individuais/rocket-chat/manuais/manual-rocket-chat-vps-e-uso.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/rocket-chat/manuais/manual-rocket-chat-vps-e-uso.md)
- [Trilha Didática de Aprendizado em 5 Aulas (HTML)](../05-manuais-e-trilhas-individuais/rocket-chat/trilhas/trilha-rocket-chat-aprendizado.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/rocket-chat/trilhas/trilha-rocket-chat-aprendizado.md)

- **Repositório Oficial:** [https://github.com/RocketChat/Rocket.Chat](https://github.com/RocketChat/Rocket.Chat)

#### 14. Zulip · Plataforma de Chat em Equipe Organizada por Tópicos e Threads Assíncronas (Classificação: Persona Mais Focada em Produtividade Assíncrona)
- **Módulo SaaS Substituído:** `Penso Chat / Slack`
- **Economia Anual Individual:** `R$ 8.000/ano` | **Licença OSI:** `Apache-2.0`
- **Papel no Ecossistema:** Chat para equipes de engenharia e gestão que sofrem com excesso de notificações em conversas desorganizadas.

**1. O Que Faz & Como Funciona:** 
Combina a agilidade do chat em tempo real com a organização de um fórum corporativo estruturado. Backend Python/Django com Tornado para webhooks assíncronos e banco PostgreSQL.
```bash
# Inicialização Rápida via Docker / CLI
docker compose up -d zulip zulip-db zulip-redis
```

**2. Racional Financeiro da Escolha:** 
Modelo exclusivo de tópicos dentro de streams que permite ler conversas importantes de forma organizada sem perder o contexto.

**3. Requisitos de Infraestrutura & Veredito Técnico:** 
- Memória RAM Mínima: `2 GB`
- CPU Recomendada: `1 vCPU`
- Imagem Docker Oficial: `zulip/docker-zulip:latest`
- Banco de Dados / Persistência: `PostgreSQL / Redis`
- **Veredito da Engenharia:** *A melhor opção para empresas remotas e equipes de desenvolvimento que priorizam foco e comunicação assíncrona organizada.*

**4. Guia Prático de Uso em 3 Passos:** 
1. **Deploy Docker:** Suba o Zulip com o docker-zulip oficial.
2. **Criação da Organização:** Acesse a URL e finalize o registro da empresa.
3. **Parametrização de Tópicos:** Oriente a equipe a criar tópicos específicos para cada demanda.

**5. White-Label & Design System:** 
- Nível de Esforço: `Baixo` | Stack UI: `Interface Zulip`
- Mecânica de Customização: Customização de logos e nomes de streams no painel corporativo.
- Manutenibilidade de Temas: Estável.

**6. Ecossistema Agêntico (MCPs, Skills & Extensões):** 
- **[Bot] Zulip GitHub Bot:** Notificações automáticas de commits e pull requests diretamente nos tópicos de TI (`https://zulip.com/integrations/doc/github`)

**7. Documentação Operacional & Capacitação Técnica Dedicada:** 
- [Manual de Engenharia de VPS & Desinstalação Cirúrgica (HTML)](../05-manuais-e-trilhas-individuais/zulip/manuais/manual-zulip-vps-e-uso.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/zulip/manuais/manual-zulip-vps-e-uso.md)
- [Trilha Didática de Aprendizado em 5 Aulas (HTML)](../05-manuais-e-trilhas-individuais/zulip/trilhas/trilha-zulip-aprendizado.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/zulip/trilhas/trilha-zulip-aprendizado.md)

- **Repositório Oficial:** [https://github.com/zulip/zulip](https://github.com/zulip/zulip)

#### 15. Jitsi Meet · Servidor de Videoconferência Criptografada HD sem Limite de Duração (Classificação: Persona Simples)
- **Módulo SaaS Substituído:** `Penso Meet / Zoom Pro / Google Meet`
- **Economia Anual Individual:** `R$ 8.000/ano` | **Licença OSI:** `Apache-2.0`
- **Papel no Ecossistema:** Reuniões virtuais em áudio e vídeo HD, gravação local/nuvem e compartilhamento de apresentações.

**1. O Que Faz & Como Funciona:** 
Transmite áudio e vídeo de alta qualidade com salas protegidas por senha e sala de espera. Arquitetura WebRTC escalável com Jitsi Videobridge (JVB), Prosody XMPP e Jicofo em contêineres Docker.
```bash
# Inicialização Rápida via Docker / CLI
git clone https://github.com/jitsi/docker-jitsi-meet && cd docker-jitsi-meet && cp env.example .env && ./gen-passwords.sh && docker compose up -d
```

**2. Racional Financeiro da Escolha:** 
Zero instalação para convidados (funciona direto no navegador WebRTC), sem limite de 40 minutos por reunião e com controle total das gravações.

**3. Requisitos de Infraestrutura & Veredito Técnico:** 
- Memória RAM Mínima: `2 GB`
- CPU Recomendada: `2 vCPU`
- Imagem Docker Oficial: `jitsi/web:latest`
- Banco de Dados / Persistência: `Prosody XMPP integrado`
- **Veredito da Engenharia:** *A solução definitiva de reuniões virtuais corporativas, eliminando 100% dos custos recorrentes de licenças Zoom/Meet.*

**4. Guia Prático de Uso em 3 Passos:** 
1. **Clone do Repositório:** Baixe o docker-jitsi-meet e gere as senhas internas com ./gen-passwords.sh.
2. **Configuração de Domínio:** Defina o domínio (meet.empresa.com.br) no arquivo .env e suba o cluster.
3. **Autenticação de Moderadores:** Habilite a autenticação para que apenas colaboradores possam abrir salas públicas.

**5. White-Label & Design System:** 
- Nível de Esforço: `Baixo` | Stack UI: `React / WebRTC`
- Mecânica de Customização: Substituição de marca d'água, logo de carregamento e interface via interface_config.js.
- Manutenibilidade de Temas: Excelente.

**6. Ecossistema Agêntico (MCPs, Skills & Extensões):** 
- **[Plugin] Nextcloud Jitsi Integration:** Botão de criação de chamadas Jitsi com 1 clique dentro dos eventos do calendário Nextcloud (`https://apps.nextcloud.com/apps/jitsimeet`)

**7. Documentação Operacional & Capacitação Técnica Dedicada:** 
- [Manual de Engenharia de VPS & Desinstalação Cirúrgica (HTML)](../05-manuais-e-trilhas-individuais/jitsi-meet/manuais/manual-jitsi-meet-vps-e-uso.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/jitsi-meet/manuais/manual-jitsi-meet-vps-e-uso.md)
- [Trilha Didática de Aprendizado em 5 Aulas (HTML)](../05-manuais-e-trilhas-individuais/jitsi-meet/trilhas/trilha-jitsi-meet-aprendizado.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/jitsi-meet/trilhas/trilha-jitsi-meet-aprendizado.md)

- **Repositório Oficial:** [https://github.com/jitsi/jitsi-meet](https://github.com/jitsi/jitsi-meet)

---

## CAPÍTULO 5 · CAMADA DE COLA, SSO FEDERADO & BLUEPRINTS N8N

### Arquitetura de Interconexão sem Silos de Dados
- ** Autenticação Única Federada (SSO):** Keycloak / Authentik OIDC unificado para login único no Webmail (Mailcow/SOGo), Nuvem (Nextcloud Hub) e Chat (Mattermost)
- ** Barramento de Eventos Assíncronos:** n8n para automação de onboarding de novos colaboradores, sincronização de contatos e alertas corporativos
- ** Gateway de Borda & Ingress TLS:** Traefik v3 com certificados Let's Encrypt TLS automáticos, roteamento por subdomínios (mail., drive., chat., meet.) e proteção contra ataques DDoS

### Fluxo Operacional de Ponta a Ponta
O colaborador faz login único via OIDC no Keycloak e tem acesso imediato à sua caixa postal corporativa, ao seu drive na nuvem com documentos OnlyOffice e aos seus canais de chat no Mattermost. Novos funcionários cadastrados no RH são provisionados automaticamente em todos os sistemas via fluxo n8n.

### Blueprints de Workflows Prontos para n8n (Importação Instantânea)

#### Onboarding Automático de Novo Colaborador (RH -> Keycloak + Mailcow + Nextcloud + Mattermost)
- *Objetivo:* Quando um novo funcionário é cadastrado no formulário de admissão, o n8n cria a conta unificada no Keycloak, gera a caixa postal no Mailcow, cria o diretório no Nextcloud e adiciona o usuário aos canais gerais do Mattermost.
- *Gatilho:* `None`
```json
{
  "name": "Onboarding Corporativo Total",
  "nodes": [
    {"name": "Webhook Admissão RH", "type": "n8n-nodes-base.webhook", "position": [100, 300]},
    {"name": "Criar Usuário Keycloak SSO", "type": "n8n-nodes-base.httpRequest", "position": [300, 300]},
    {"name": "Criar Caixa Postal Mailcow", "type": "n8n-nodes-base.httpRequest", "position": [500, 200]},
    {"name": "Criar Conta Nextcloud Hub", "type": "n8n-nodes-base.nextcloud", "position": [500, 400]},
    {"name": "Adicionar Canais Mattermost", "type": "n8n-nodes-base.mattermost", "position": [700, 300]},
    {"name": "Notificar Gestor via E-mail", "type": "n8n-nodes-base.emailSend", "position": [900, 300]}
  ]
}
```

#### Alerta de Tentativa de Phishing & Quarentena Antispam
- *Objetivo:* Monitora a fila do Rspamd no Mailcow. Quando uma mensagem com alta pontuação de ameaça é detectada, o n8n envia um alerta imediato no canal #seguranca-ti do Mattermost com opção de bloqueio de domínio remetente.
- *Gatilho:* `None`
```json
{
  "name": "Monitoramento Rspamd Phishing",
  "nodes": [
    {"name": "Webhook Rspamd Alert", "type": "n8n-nodes-base.webhook", "position": [100, 300]},
    {"name": "Análise de Score & SPF", "type": "n8n-nodes-base.if", "position": [300, 300]},
    {"name": "Publicar Alerta no Mattermost TI", "type": "n8n-nodes-base.mattermost", "position": [550, 200]},
    {"name": "Registrar Log de Segurança", "type": "n8n-nodes-base.postgres", "position": [550, 400]}
  ]
}
```

---

## CAPÍTULO 6 · MANUAL DE ENGENHARIA DE INFRAESTRUTURA & DEPLOY ALL-IN-ONE

### Entendendo os 4 Pilares da Infraestrutura (Sem Jargões)
- **1. O que é VPS?** 
- **2. O que é Docker Compose?** 
- **3. O que é Traefik?** 
- **4. O que é n8n?** 

> **Topologia & Segurança de Rede:** Cluster conteinerizado em rede Docker interna isolada (penso_sovereign_net), exposto publicamente apenas pelas portas 80/443 (HTTPS Traefik) e portas padrão de e-mail (25, 465, 587, 993) com firewall UFW ativo e Fail2ban protegendo contra força bruta.

### Matriz dos 9 Serviços do Orquestrador
| # | Serviço / Módulo | Imagem Docker | Papel na Infraestrutura | Portas / Exposição | Persistência / Volumes |
|---|---|---|---|---|---|
| 01 | **Traefik Reverse Proxy** | `traefik:v3.0` | Entrada única HTTPS, SSL Let's Encrypt automático e balanceamento | `80, 443` | `./traefik/acme.json` |
| 02 | **Keycloak SSO** | `quay.io/keycloak/keycloak:latest` | Provedor de Identidade (IdP) OIDC para login único de todos os módulos | `Rede interna (8080)` | `./keycloak_data` |
| 03 | **Mailcow E-mail Stack** | `mailcow/*` | Servidor de e-mail corporativo, groupware e filtro antispam | `25, 465, 587, 993, 110, 995` | `./mailcow_data` |
| 04 | **Nextcloud Hub** | `nextcloud:apache` | Armazenamento em nuvem, drive corporativo e OnlyOffice | `Rede interna (80)` | `./nextcloud_data` |
| 05 | **Mattermost Chat** | `mattermost/mattermost-team-edition:latest` | Mensageria corporativa, canais e playbooks de equipe | `Rede interna (8065)` | `./mattermost_data` |
| 06 | **Jitsi Meet** | `jitsi/*` | Videoconferência criptografada em alta definição | `10000/udp, 443` | `./jitsi_config` |

### Especificação da VPS Ideal para o Ecossistema Completo (e Por Que)
> **Perfil de Máquina Recomendado:** `None` 
> **Por Que Desta Configuração (Racional Técnico):** None

#### Distribuição de Recursos de Hardware por Serviço (vCPU & RAM)
| Serviço / Módulo | vCPU Alocada | Memória RAM | Motivo Técnico / Gargalo Previsto |
|---|---|---|---|
| **Traefik + Keycloak SSO** | `2 vCPU` | `2.5 GB RAM` | Autenticação federada central e roteamento TLS para toda a suíte |
| **Mailcow Cluster (Postfix + Dovecot + Rspamd + SOGo)** | `4 vCPU` | `8.0 GB RAM` | Processamento de filas SMTP, escaneamento de vírus ClamAV e IMAP |
| **Nextcloud Hub + OnlyOffice Document Server** | `4 vCPU` | `8.0 GB RAM` | Edição de planilhas/documentos e sincronização de arquivos pesados |
| **Mattermost Team Edition + PostgreSQL** | `2 vCPU` | `4.0 GB RAM` | Comunicação em tempo real, canais e persistência de histórico |
| **Jitsi Meet (WebRTC + JVB)** | `2 vCPU` | `3.5 GB RAM` | Encaminhamento de fluxos de áudio e vídeo HD sem transcoding pesado |
| **n8n Workflow Engine + Redis** | `1 vCPU` | `1.5 GB RAM` | Orquestração de eventos e rotinas assíncronas |
| **Margem de Segurança & Cache do SO** | `1 vCPU` | `4.5 GB RAM` | Buffer de I/O em disco NVMe e prevenção contra picos de tráfego |

#### Provedores de Nuvem Recomendados & Validados
| Provedor de Nuvem | Custo Mensal Estimado | Vantagem Principal / SLA |
|---|---|---|

### Dimensionamento de Hardware Recomendado
- **Memória RAM Total:** `None`
- **Processamento CPU:** `None`
- **Armazenamento SSD:** `None`

### Arquivo `docker-compose.yml` Consolidado para Produção
```yaml
version: '3.8'

networks:
  penso_sovereign_net:
    name: penso_sovereign_net
    driver: bridge

services:
  traefik:
    image: traefik:v3.0
    container_name: traefik_gateway
    restart: always
    command:
      - '--api.dashboard=true'
      - '--providers.docker=true'
      - '--providers.docker.exposedbydefault=false'
      - '--entrypoints.web.address=:80'
      - '--entrypoints.websecure.address=:443'
      - '--certificatesresolvers.letsencrypt.acme.tlschallenge=true'
      - '--certificatesresolvers.letsencrypt.acme.email=admin@empresa.com.br'
      - '--certificatesresolvers.letsencrypt.acme.storage=/letsencrypt/acme.json'
    ports:
      - '80:80'
      - '443:443'
    volumes:
      - '/var/run/docker.sock:/var/run/docker.sock:ro'
      - './traefik_data/acme.json:/letsencrypt/acme.json'
    networks:
      - penso_sovereign_net

  keycloak:
    image: quay.io/keycloak/keycloak:latest
    container_name: keycloak_sso
    restart: always
    command: start --optimized
    environment:
      - KC_DB=postgres
      - KC_DB_URL=jdbc:postgresql://postgres_sso:5432/keycloak
      - KC_DB_USERNAME=keycloak
      - KC_DB_PASSWORD=${KEYCLOAK_DB_PASSWORD}
      - KC_HOSTNAME=auth.empresa.com.br
    labels:
      - 'traefik.enable=true'
      - 'traefik.http.routers.keycloak.rule=Host(`auth.empresa.com.br`)'
      - 'traefik.http.routers.keycloak.entrypoints=websecure'
      - 'traefik.http.routers.keycloak.tls.certresolver=letsencrypt'
    networks:
      - penso_sovereign_net

  nextcloud:
    image: nextcloud:apache
    container_name: nextcloud_drive
    restart: always
    environment:
      - POSTGRES_HOST=postgres_drive
      - POSTGRES_DB=nextcloud
      - POSTGRES_USER=nextcloud
      - POSTGRES_PASSWORD=${NEXTCLOUD_DB_PASSWORD}
      - REDIS_HOST=redis_drive
    volumes:
      - './nextcloud_data/html:/var/www/html'
      - './nextcloud_data/data:/var/www/html/data'
    labels:
      - 'traefik.enable=true'
      - 'traefik.http.routers.nextcloud.rule=Host(`drive.empresa.com.br`)'
      - 'traefik.http.routers.nextcloud.entrypoints=websecure'
      - 'traefik.http.routers.nextcloud.tls.certresolver=letsencrypt'
    networks:
      - penso_sovereign_net

  mattermost:
    image: mattermost/mattermost-team-edition:latest
    container_name: mattermost_chat
    restart: always
    environment:
      - MM_SQLSETTINGS_DATASOURCE=postgres://mmuser:${MM_DB_PASSWORD}@postgres_chat:5432/mattermost?sslmode=disable
    volumes:
      - './mattermost_data/config:/mattermost/config'
      - './mattermost_data/data:/mattermost/data'
    labels:
      - 'traefik.enable=true'
      - 'traefik.http.routers.mattermost.rule=Host(`chat.empresa.com.br`)'
      - 'traefik.http.routers.mattermost.entrypoints=websecure'
      - 'traefik.http.routers.mattermost.tls.certresolver=letsencrypt'
    networks:
      - penso_sovereign_net
```

### Roteiro de Instalação e Subida em 4 Passos

1. **Provisionamento da VPS & Configuração de DNS:** Contrate a VPS com Ubuntu 24.04 LTS e aponte os registros de subdomínio (mail., drive., chat., meet., auth.) para o IP público.
2. **Deploy do Traefik & Keycloak SSO:** Inicialize o roteamento TLS e configure o realm corporativo no Keycloak para login único em todos os módulos.
3. **Subida do Mailcow & Nextcloud Hub:** Inicie o cluster de e-mail e a nuvem corporativa com volumes NVMe de alta velocidade.
4. **Subida do Mattermost & Jitsi Meet:** Ative o chat corporativo e as salas de reunião com conexão OIDC ao Keycloak.
5. **Validação de Rotinas & Backups:** Execute o script de backup automatizado 3-2-1 e faça o teste prático de restauração.

---

## CAPÍTULO 7 · PROTOCOLOS DE MODULARIDADE & HOT-SWAP (PRINCÍPIO DO LEGO)

> **O Princípio das Tomadas Independentes:** 
> Princípio do Lego: cada serviço (Mailcow, Nextcloud, Mattermost, Jitsi) roda em seu próprio contêiner desacoplado com volumes persistentes. Se a empresa decidir trocar o Mattermost pelo Zulip ou o Nextcloud pelo Seafile, a substituição é realizada sem interromper o serviço de e-mail ou o proxy central.

### Protocolo 1: Inserção de Novas Ferramentas (Plug-and-Play)
1. Abra o arquivo docker-compose.yml e adicione a definição do novo contêiner;
2. Execute docker compose up -d no terminal da VPS;
3. O Traefik detecta as novas labels e emite o certificado SSL Let's Encrypt automaticamente;
4. Cadastre o novo módulo no Keycloak para autenticação SSO unificada.

### Protocolo 2: Substituição de Ferramenta em Produção (Hot-Swap sem Downtime)
1. Suba o novo serviço em paralelo em uma porta/subdomínio temporário;
2. Sincronize os dados históricos do serviço antigo;
3. Teste o login via Keycloak;
4. Altere a label do Traefik apontando o subdomínio principal para o novo contêiner;
5. Desligue o contêiner legado após 48 horas de validação.

### Protocolo 3: Remoção Segura de Módulos
1. Execute docker compose stop <servico>;
2. Remova as rotas dedicadas no Traefik;
3. Exclua a pasta /opt/<servico> preservando o arquivo tar.gz de backup final;
4. Verifique com docker ps e ss -tulpn que nenhum processo residual permaneceu ativo.

### Estudo de Caso Prático: Substituição do Webmail SOGo pelo SnappyMail ou migração de arquivos do Nextcloud para o Seafile
- **1. Isolamento Operacional:** O servidor de e-mail Mailcow e o chat Mattermost comunicam-se via protocolos abertos (IMAP/OIDC/n8n) e permanecem 100% operacionais durante todo o procedimento.
- **2. Início do Novo Contêiner:** `O novo serviço de interface web é provisionado em uma porta temporária com testes de login único via Keycloak.`
- **3. Chaveamento no n8n:** A rota do Traefik é chaveada de forma transparente para o novo contêiner sem derrubar as sessões ativas de correio.
- **4. Resultado Final:** A migração da interface é concluída com ZERO minutos de downtime na recepção e envio de e-mails corporativos.

### Perguntas Frequentes (FAQ Operacional para Não-Técnicos)

- ** E se a VPS for reiniciada pelo provedor de nuvem?**
 - *Resposta:* Todos os contêineres possuem a diretiva restart: always. Quando a VPS religar, o servidor de e-mail, drive e chat sobem automaticamente em menos de 45 segundos sem intervenção manual.

- ** Como garantir que meus e-mails corporativos não caiam na caixa de spam?**
 - *Resposta:* O Mailcow configura e valida automaticamente as assinaturas criptográficas DKIM, registros SPF e políticas DMARC, garantindo entregabilidade nota 10/10 nos principais provedores globais (Gmail, Outlook e Yahoo).

- ** A minha equipe precisará reinstalar programas em todos os computadores?**
 - *Resposta:* Não! Todas as ferramentas contam com clientes web modernos compatíveis com qualquer navegador, além de suporte a clientes tradicionais já utilizados (Outlook, Thunderbird e celulares iOS/Android).

---

## CAPÍTULO 8 · ROTEIRO PRÁTICO DE MIGRAÇÃO DE DADOS HISTÓRICOS

### E-mail Corporativo (Zimbra / Penso Mail -> Mailcow)
- **O que migrar:** Todas as caixas postais, histórico de mensagens, pastas personalizadas, regras de encaminhamento e contatos.
- **Passos de Migração:**
 1. 1. Exporte a lista de contas ativas do Zimbra com endereços e cotas;
 1. 2. Crie os usuários no Mailcow com senhas temporárias ou via SSO Keycloak;
 1. 3. Configure os Syncjobs do Mailcow para sincronização IMAP contínua (pull em background);
 1. 4. No dia da virada de chave, altere os registros MX do DNS;
 1. 5. Execute a última sincronização incremental para transferir os últimos e-mails recebidos durante a propagação do DNS.
- ** Cuidados Críticos:** Mantenha o servidor Zimbra antigo acessível por IP durante 72 horas pós-virada para garantir que nenhuma mensagem em trânsito seja perdida.

### Arquivos & Documentos (Penso Drive -> Nextcloud Hub)
- **O que migrar:** Pastas de departamentos, arquivos corporativos, permissões e documentos OnlyOffice.
- **Passos de Migração:**
 1. 1. Realize o download em lote das pastas corporativas do Penso Drive via cliente WebDAV ou rsync;
 1. 2. Transfira os dados para o volume /var/www/html/data do Nextcloud na VPS;
 1. 3. Execute o comando occ files:scan --all para indexar instantaneamente todos os arquivos no banco de dados;
 1. 4. Aplique as regras de compartilhamento de grupo (Group Folders) correspondentes.
- ** Cuidados Críticos:** Valide as permissões de proprietário (chown -R www-data:www-data) no diretório de dados antes da varredura.

---

## CAPÍTULO 9 · GOVERNANÇA CORPORATIVA, BACKUP 3-2-1 & CONFORMIDADE LGPD

> **Arquitetura de Proteção de Dados 3-2-1:** Regra 3-2-1 estrita: 3 cópias dos dados (produção local, backup criptografado em disco secundário e snapshot offsite em storage S3 externo como Wasabi ou Backblaze B2).

### Script Automatizado de Backup Diário com Criptografia AES-256
```bash
#!/bin/bash
set -e
DATA=$(date +%Y%m%d_%H%M%S)
DEST=/var/backups/sovereign_suite
mkdir -p $DEST

# 1. Backup Banco de Dados PostgreSQL (Keycloak, Nextcloud, Mattermost)
docker exec postgres_sso pg_dumpall -U keycloak | gzip > $DEST/db_sso_$DATA.sql.gz
docker exec postgres_drive pg_dumpall -U nextcloud | gzip > $DEST/db_drive_$DATA.sql.gz
docker exec postgres_chat pg_dumpall -U mmuser | gzip > $DEST/db_chat_$DATA.sql.gz

# 2. Backup Mailcow (Utilitário Nativo de Backup)
cd /opt/mailcow-dockerized && ./helper-scripts/backup_and_restore.sh backup all --delete-days 7

# 3. Criptografia com OpenSSL (AES-256-CBC)
tar -czf - -C $DEST . | openssl enc -aes-256-cbc -salt -pbkdf2 -pass pass:${BACKUP_PASSWORD} -out /var/backups_encrypted/penso_suite_backup_$DATA.tar.enc

# 4. Envio Seguro para Storage S3 Offsite (Wasabi / AWS)
rclone copy /var/backups_encrypted/ s3-backup:empresa-backups-soberanos/

echo 'Backup 3-2-1 executado e criptografado com sucesso!'
```

### Checklist de Conformidade Estrita com a LGPD

- **Armazenamento em Território Nacional / Infraestrutura Própria:** Conforme · Controle exclusivo dos dados sem transferência internacional involuntária.
- **Logs de Auditoria de Acessos e Modificações:** Conforme · Registro completo de downloads, compartilhamentos e logins no Nextcloud e Keycloak.
- **Direito de Exclusão e Portabilidade do Titular:** Conforme · Exportação e expurgo cirúrgico de caixas postais e arquivos em poucos cliques.
- **Criptografia em Repouso e em Trânsito (TLS 1.3):** Conforme · Criptografia de disco local, TLS 1.3 nos proxies e criptografia ponta a ponta disponível.

---

## CAPÍTULO 10 · CRONOGRAMA DE IMPLANTAÇÃO EM 30 DIAS & MONITORAMENTO

### Cronograma Executivo de Virada de Chave (4 Semanas)

#### Semana 01 · Provisionamento de VPS & Identidade Unificada (Keycloak SSO)
- *Atividades Principais:* Contratação da VPS dedicada, endurecimento do sistema operacional (SSH seguro, UFW, Fail2ban), deploy do Traefik com TLS e configuração do Keycloak com os usuários corporativos.
- * Marco de Conclusão:* **Painel de autenticação online em auth.empresa.com.br com certificados SSL válidos.**

#### Semana 02 · Deploy do Servidor de E-mail Soberano & Testes de Entregabilidade
- *Atividades Principais:* Deploy do Mailcow, configuração de chaves DKIM, SPF e DMARC, teste de reputação IP (Mail-Tester 10/10) e sincronização piloto de 10 caixas postais via Syncjob.
- * Marco de Conclusão:* **Servidor de correio enviando e recebendo mensagens com reputação máxima.**

#### Semana 03 · Deploy do Drive Corporativo (Nextcloud) & Chat (Mattermost)
- *Atividades Principais:* Deploy do Nextcloud Hub com OnlyOffice, migração das pastas departamentais do Penso Drive, subida do Mattermost com canais de equipe e integração ao Keycloak.
- * Marco de Conclusão:* **Nuvem de arquivos e chat corporativo operacionais para testes internos com a equipe de TI.**

#### Semana 04 · Virada de Chave (DNS Cutover), Treinamento & Desativação do SaaS
- *Atividades Principais:* Alteração dos registros MX definitivos no DNS, execução da sincronização final de e-mails, distribuição dos clientes desktop/mobile e aplicação da Trilha de Aprendizado em 5 Aulas para a equipe.
- * Marco de Conclusão:* **Operação 100% migrada para a infraestrutura própria e cancelamento das faturas do Penso Suite.**

### Monitoramento em Tempo Real da VPS (None)

**Comandos de Diagnóstico em 1 Clique:**

- `docker ps --format 'table {{.Names}}\t{{.Status}}\t{{.Ports}}'` Visualizar o status de todos os contêineres da suíte em execução.
- `docker stats --no-stream` Verificar o consumo de CPU e Memória RAM em tempo real por serviço.
- `tail -f /var/log/mail.log` Acompanhar a fila e conexões do servidor de correio em tempo real.
- `df -h` Checar o espaço em disco disponível na VPS e nos volumes de dados.

**Métricas Críticas & Ações Imediatas:**

- **Uso de Memória RAM > 85%** (Limite: `Alerta Crítico`): Verificar contêineres de escaneamento ClamAV ou habilitar swap de emergência.
- **Espaço em Disco NVMe < 15%** (Limite: `Alerta Alto`): Executar limpeza de logs docker system prune -a ou expandir volume de storage.
- **Fila SMTP > 100 mensagens retidas** (Limite: `Alerta Médio`): Investigar se algum domínio destinatário está aplicando greylisting temporário.
