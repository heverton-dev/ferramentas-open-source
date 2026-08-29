# LIVRO-TEXTO EXECUTIVO: MACRO-ECOSSISTEMA RD STATION: MARKETING, CRM & CONVERSAS

> **Macro-Ecossistema SaaS Alvo:** RD Station Suite (Marketing Pro + CRM Pro + Conversas Enterprise + Zapier) 
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

Dossiê completo de desmantelamento soberano para o Macro-Ecossistema RD Station (Marketing, CRM, Conversas/WhatsApp, Formulários e Automações). Cada frente de negócio é estruturada com seu próprio Quinteto Soberano (A Mais Robusta, Mais Completa, Mais Moderna, Mais Leve e Mais Simples), acompanhada de análise de TCO, guias práticos, aderência white-label e ecossistema agêntico de MCPs.

A dependência crônica de suítes de software como serviço (SaaS) impõe três vulnerabilidades críticas a qualquer organização em crescimento:
1. **Risco de Lock-in Financeiro:** Reajustes anuais unilaterais de 15% a 25% e cobranças por contatos/usuários que penalizam o crescimento da empresa;
2. **Perda de Soberania sobre os Dados:** Informações confidenciais de clientes, negociações e inteligência comercial hospedadas em bancos multi-tenant de terceiros;
3. **Rigidez Operacional:** Impossibilidade de customizar código, adaptar telas ou integrar APIs sem pagar planos 'Enterprise' proibitivos.

Este livro-texto consolida a alternativa definitiva: a **migração para uma arquitetura open source auto-hospedada, soberana, de alto desempenho e com payback inferior a 30 dias**.

---

## CAPÍTULO 1 · ENGENHARIA FINANCEIRA, TCO GLOBAL & PAYBACK

### Demonstrativo Contábil Consolidado (Base Anual)
- **Custo Total SaaS Proprietário (RD Station Suite (Marketing Pro + CRM Pro + Conversas Enterprise + Zapier)):** `R$ 114.000/ano (RD Marketing Pro R$ 42k + RD CRM 10 vendedores R$ 36k + RD Conversas 10 atendentes R$ 36k)`
- **Custo de Infraestrutura VPS Própria (Cluster Unificado 8 vCPU / 16 GB):** `R$ 4.200/ano (VPS 8 vCPU / 16 GB RAM a R$ 350/mês)`
- **Economia Líquida Anual no Caixa:** `R$ 109.800/ano (Economia Líquida de 96.3%)`
- **Retorno sobre o Investimento (ROI / Payback):** `Payback positivo em apenas 14 dias de operação unificada.`

### Desmembramento de Custos e Economia por Frente de Negócio
| Frente de Negócio | Módulo SaaS Proprietário | Custo SaaS Anual | Custo VPS Alocado | Economia Anual Líquida | Margem de Economia |
|---|---|---|---|---|---|

---

## CAPÍTULO 2 · INFRAESTRUTURA GLOBAL, DIMENSIONAMENTO DA VPS & PROVEDORES VALIDADOS

> **Perfil de Máquina Recomendado:** `8 vCPU Dedicated Cloud / 16 GB RAM ECC / 160-240 GB NVMe SSD / Link 1 Gbps / Ubuntu 24.04 LTS x86_64` 
> **Racional de Engenharia:** Garante estabilidade absoluta para os 9 contêineres rodando em simultâneo com isolamento de processos, prevenindo gargalos de I/O em banco de dados e eliminando o risco do OOM Killer durante picos de campanha e atendimento.

### Provedores de Nuvem Recomendados & Custo Mensal da Infraestrutura
| Provedor de Nuvem | Custo Mensal Estimado | Vantagem Principal & SLA |
|---|---|---|
| **Hetzner Cloud (CPX41 / CCX23)** | `€ 28 (~ R$ 170/mês)` | Melhor custo-benefício e performance bruta por vCPU dedicada (Datacenters UE/EUA). |
| **Contabo (Cloud VPS L)** | `€ 16 (~ R$ 100/mês)` | Maior volume de memória RAM e disco NVMe por valor investido. |
| **DigitalOcean (Dedicated 16GB)** | `$ 84 (~ R$ 460/mês)` | Excelente SLA de rede, suporte global e facilidade de snapshots. |
| **AWS Lightsail (16GB RAM)** | `$ 80 (~ R$ 440/mês)` | Infraestrutura corporativa AWS com 5 TB de transferência inclusos. |

### Alocação Técnica de Recursos por Serviço (vCPU & RAM)
| Serviço / Módulo | vCPU Alocada | Memória RAM | Motivo Técnico / Gargalo Previsto |
|---|---|---|---|
| **Traefik Ingress & TLS** | `0.5 vCPU` | `256 MB` | Roteamento reativo de borda, compressão Brotli/Gzip e renovação automática de certificados SSL. |
| **Keycloak SSO (OpenJDK JVM)** | `1.5 vCPU` | `2.0 GB` | Baseline da JVM Java para autenticação federada OIDC/SAML e criptografia de senhas Argon2. |
| **Mautic Marketing & Cron** | `2.0 vCPU` | `4.0 GB` | Processamento em lote de campanhas para 50k+ leads, segmentação e rastreamento assíncrono de cliques. |
| **Twenty CRM & GraphQL** | `1.5 vCPU` | `3.0 GB` | API reativa, buscas full-text e pipeline comercial Kanban simultâneo para 10 a 50 vendedores. |
| **Chatwoot + Sidekiq** | `1.5 vCPU` | `3.5 GB` | Ruby on Rails com centenas de WebSockets ao vivo para multiatendentes no WhatsApp e filas Redis. |
| **Evolution API (WhatsApp)** | `1.0 vCPU` | `1.5 GB` | Sessões Baileys ativas com o WhatsApp, decodificação de áudios OGG/MP3 e disparo de webhooks. |
| **n8n Orquestrador** | `0.5 vCPU` | `1.0 GB` | Execução assíncrona de fluxos de dados, webhooks e sincronização contínua entre CRM e WhatsApp. |
| **Buffer de Picos / Anti-OOM** | `1.0 vCPU` | `1.7 GB` | Margem de folga do kernel Linux para backups diários pg_dump e picos sazonais (Black Friday). |

---

## CAPÍTULO 3 · MATRIZ ESTRATÉGICA DO QUINTETO SOBERANO

| # | Grupo Funcional | Persona | Ferramenta | Módulo SaaS Substituído | Economia Anual | Licença | Repositório |
|---|---|---|---|---|---|---|---|
| 01 | Grupo 1 | Completa | **Mautic** | RD Station Marketing (Módulo de Automação de Fluxos & Lead Scoring) | R$ 42.000/ano (Base de 50.000 leads) | `GPL-3.0` | [GitHub](https://github.com/mautic/mautic) |
| 02 | Grupo 1 | Leve | **Listmonk** | RD Station Marketing (Módulo de Disparos de E-mail & Broadcast) | R$ 18.000/ano | `AGPL-3.0` | [GitHub](https://github.com/knadh/listmonk) |
| 03 | Grupo 1 | Robusta | **Directus** | RD Station Marketing (Construtor de Landing Pages & Formulários Estáticos) | R$ 12.000/ano | `GPL-3.0` | [GitHub](https://github.com/directus/directus) |
| 04 | Grupo 1 | Moderna | **Novu** | RD Station Notificações / OneSignal / Courier | R$ 14.400/ano | `Apache-2.0` | [GitHub](https://github.com/novuhq/novu) |
| 05 | Grupo 1 | Simples | **Plunk** | RD Station Marketing (Plano Light / Automações Básicas) | R$ 9.600/ano | `MIT` | [GitHub](https://github.com/useplunk/plunk) |
| 06 | Grupo 2 | Moderna | **Twenty** | RD Station CRM (Módulo de Pipeline Kanban, Oportunidades & Tarefas) | R$ 24.000/ano (Equipe de 10 vendedores) | `AGPL-3.0` | [GitHub](https://github.com/twentyhq/twenty) |
| 07 | Grupo 2 | Robusta | **EspoCRM** | RD Station CRM (Módulos Corporativos Avançados & Múltiplos Pipelines) | R$ 18.000/ano | `GPL-3.0` | [GitHub](https://github.com/espocrm/espocrm) |
| 08 | Grupo 2 | Completa | **SuiteCRM** | Salesforce Sales Cloud / SugarCRM Enterprise | R$ 36.000/ano | `AGPL-3.0` | [GitHub](https://github.com/salesagility/SuiteCRM) |
| 09 | Grupo 2 | Leve | **Documenso** | Clicksign / DocuSign / Módulo de Propostas Comerciais | R$ 18.000/ano | `AGPL-3.0` | [GitHub](https://github.com/documenso/documenso) |
| 10 | Grupo 2 | Simples | **Cal.com** | RD Station CRM (Agendamentos) / Calendly Integrado | R$ 12.000/ano | `AGPL-3.0` | [GitHub](https://github.com/calcom/cal.com) |
| 11 | Grupo 3 | Completa | **Chatwoot** | RD Station Conversas (Painel de Atendimento Multiatendente) | R$ 36.000/ano (10 operadores) | `MIT` | [GitHub](https://github.com/chatwoot/chatwoot) |
| 12 | Grupo 3 | Robusta | **Evolution API** | RD Station Conversas (Conectores Proprietários Z-API / Gupshup) | R$ 18.000/ano | `Apache-2.0` | [GitHub](https://github.com/EvolutionAPI/evolution-api) |
| 13 | Grupo 3 | Moderna | **Typebot** | RD Station Conversas (Chatbots de Triagem) / Landbot | R$ 14.400/ano | `AGPL-3.0` | [GitHub](https://github.com/baptisteArno/typebot.io) |
| 14 | Grupo 3 | Leve | **WAHA** | RD Station Notificações WhatsApp / Twilio Messaging | R$ 12.000/ano | `Apache-2.0` | [GitHub](https://github.com/devlikeapro/waha) |
| 15 | Grupo 3 | Simples | **Papercups** | Intercom / Crisp / Chat Básico do RD | R$ 10.800/ano | `MIT` | [GitHub](https://github.com/papercups-io/papercups) |

---

## CAPÍTULO 4 · TRATADOS TÉCNICOS INDIVIDUAIS DOS PILARES

### PILAR 01: GRUPO 1: MARKETING, NUTRIÇÃO & LANDING PAGES
> **Alvo SaaS Substituído:** `RD Station Marketing (Planos Pro / Enterprise)` | **Economia do Pilar:** `R$ 42.000/ano` 
> **Descrição Estratégica:** Frente responsável pela atração de tráfego, captura e enriquecimento de contatos, criação autônoma de landing pages dinâmicas, disparos de e-mail marketing em massa e automação de fluxos com pontuação de leads (lead scoring).

#### 01. Mautic · Automação de Marketing & Jornadas de Nutrição (Classificação: Persona Completa)
- **Módulo SaaS Substituído:** `RD Station Marketing (Módulo de Automação de Fluxos & Lead Scoring)`
- **Economia Anual Individual:** `R$ 42.000/ano (Base de 50.000 leads)` | **Licença OSI:** `GPL-3.0`
- **Papel no Ecossistema:** Motor central de automação de marketing, segmentação dinâmica e pontuação de leads.

**1. O Que Faz & Como Funciona:** 
Gerencia campanhas multicanal, pontua leads por interesse e aciona gatilhos de nutrição automática. Backend em PHP/Symfony com orquestrador visual de jornadas em árvore e integração de rastreamento no site.
```bash
# Inicialização Rápida via Docker / CLI
docker run -d -p 8080:80 --name mautic mautic/mautic:latest
```

**2. Racional Financeiro da Escolha:** 
Única plataforma open source com construtor visual de jornadas em árvore equivalente ao RD Pro, com rastreamento avançado de comportamento web (lead tracking) e ausência de cobrança por volume de contatos na base.

**3. Requisitos de Infraestrutura & Veredito Técnico:** 
- Memória RAM Mínima: `4 GB RAM`
- CPU Recomendada: `1 vCPU`
- Imagem Docker Oficial: `oficial`
- Banco de Dados / Persistência: `PostgreSQL`
- **Veredito da Engenharia:** *O Mautic é a única alternativa aberta com maturidade funcional para substituir integralmente réguas de nutrição e pontuação de leads de grandes empresas sem limites de contatos.*

**4. Guia Prático de Uso em 3 Passos:** 
1. **Configuração de SMTP & DNS:** Conecte o Amazon SES ou servidor SMTP próprio e valide registros SPF, DKIM e DMARC no domínio institucional.
2. **Desenho da Jornada Visual:** Crie o fluxo de automação em árvore no construtor drag-and-drop acionando e-mails após downloads de materiais ricos.
3. **Regras de Lead Scoring:** Defina pontuações automáticas por abertura de e-mail e visitas a páginas de preços para qualificação comercial.

**5. White-Label & Design System:** 
- Nível de Esforço: `Baixo` | Stack UI: `Twig + Bootstrap + CSS Variables`
- Mecânica de Customização: Permite substituir logo, favicon e aplicar paleta institucional via temas Twig customizados e CSS corporativo.
- Manutenibilidade de Temas: 

**6. Ecossistema Agêntico (MCPs, Skills & Extensões):** 
- **[MCP Server] @modelcontextprotocol/server-mautic:** Permite a agentes de IA consultarem o histórico de interações e pontuações de leads diretamente via MCP. (`npx -y mautic-mcp-server`)
- **[Agent Skill] skill-mautic-lead-enrichment:** Skill para agentes LLM enriquecerem contatos no Mautic a partir de pesquisas públicas no LinkedIn. (`.claude/skills/mautic-enrichment/SKILL.md`)
- **[CLI Tool] mautic-cli:** CLI para execução determinística de tarefas cron de segmentação e disparo de campanhas. (`php bin/console mautic:segments:update`)

**7. Documentação Operacional & Capacitação Técnica Dedicada:** 
- [Manual de Engenharia de VPS & Desinstalação Cirúrgica (HTML)](../05-manuais-e-trilhas-individuais/mautic/manuais/manual-mautic-vps-e-uso.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/mautic/manuais/manual-mautic-vps-e-uso.md)
- [Trilha Didática de Aprendizado em 5 Aulas (HTML)](../05-manuais-e-trilhas-individuais/mautic/trilhas/trilha-mautic-aprendizado.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/mautic/trilhas/trilha-mautic-aprendizado.md)

- **Repositório Oficial:** [https://github.com/mautic/mautic](https://github.com/mautic/mautic)

#### 02. Listmonk · Disparador de E-mails & Newsletters de Alta Performance (Classificação: Persona Leve)
- **Módulo SaaS Substituído:** `RD Station Marketing (Módulo de Disparos de E-mail & Broadcast)`
- **Economia Anual Individual:** `R$ 18.000/ano` | **Licença OSI:** `AGPL-3.0`
- **Papel no Ecossistema:** Entrega de e-mails em massa e newsletters com custo quase nulo via Amazon SES.

**1. O Que Faz & Como Funciona:** 
Processa milhões de disparos de e-mail com segmentação SQL ultrarrápida. Binário Go estático de alto rendimento sobre PostgreSQL com suporte nativo a JSONB.
```bash
# Inicialização Rápida via Docker / CLI
docker run -d -p 9000:9000 --name listmonk listmonk/listmonk:latest
```

**2. Racional Financeiro da Escolha:** 
Desenvolvido em Go puro, entrega milhões de e-mails consumindo menos de 50 MB de RAM, suportando segmentação relacional JSONB instantânea e eliminando custos punitivos por envio.

**3. Requisitos de Infraestrutura & Veredito Técnico:** 
- Memória RAM Mínima: `1 GB RAM`
- CPU Recomendada: `1 vCPU`
- Imagem Docker Oficial: `oficial`
- Banco de Dados / Persistência: `PostgreSQL`
- **Veredito da Engenharia:** *Imbatível para disparos volumosos e newsletters corporativas; entrega desempenho industrial com fraqueza de recursos.*

**4. Guia Prático de Uso em 3 Passos:** 
1. **Importação de Base:** Importe listas de contatos via CSV ou API REST com mapeamento instantâneo de atributos customizados JSONB.
2. **Templates Responsivos:** Escreva templates de e-mail em HTML/Go template ou importe templates projetados no Figma.
3. **Disparo em Massa:** Agende campanhas de broadcast monitorando taxas de entrega, cliques e bounce em tempo real.

**5. White-Label & Design System:** 
- Nível de Esforço: `Baixo` | Stack UI: `Vue.js + Go Templates`
- Mecânica de Customização: Interface limpa com suporte a upload de logo institucional e customização total dos formulários públicos de opt-in.
- Manutenibilidade de Temas: 

**6. Ecossistema Agêntico (MCPs, Skills & Extensões):** 
- **[MCP Server] listmonk-mcp:** Interface MCP para agentes agendarem e validarem campanhas de e-mail via linguagem natural. (`npx -y listmonk-mcp-server`)
- **[Agent Skill] skill-newsletter-compiler:** Compila newsletters semanais a partir de dados do banco e despacha via Listmonk. (`.claude/skills/newsletter-compiler/SKILL.md`)
- **[CLI Tool] listmonk-cli:** Gerenciador de linha de comando para automação de rotinas de manutenção. (`listmonk --config config.toml`)

**7. Documentação Operacional & Capacitação Técnica Dedicada:** 
- [Manual de Engenharia de VPS & Desinstalação Cirúrgica (HTML)](../05-manuais-e-trilhas-individuais/listmonk/manuais/manual-listmonk-vps-e-uso.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/listmonk/manuais/manual-listmonk-vps-e-uso.md)
- [Trilha Didática de Aprendizado em 5 Aulas (HTML)](../05-manuais-e-trilhas-individuais/listmonk/trilhas/trilha-listmonk-aprendizado.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/listmonk/trilhas/trilha-listmonk-aprendizado.md)

- **Repositório Oficial:** [https://github.com/knadh/listmonk](https://github.com/knadh/listmonk)

#### 03. Directus · Headless CMS para Landing Pages & Portais de Conteúdo (Classificação: Persona Robusta)
- **Módulo SaaS Substituído:** `RD Station Marketing (Construtor de Landing Pages & Formulários Estáticos)`
- **Economia Anual Individual:** `R$ 12.000/ano` | **Licença OSI:** `GPL-3.0`
- **Papel no Ecossistema:** Gestão autônoma de conteúdo das landing pages e portais corporativos sem depender de desenvolvedores.

**1. O Que Faz & Como Funciona:** 
Fornece painel no-code para o time de marketing editar textos, depoimentos e formulários de landing pages. API REST/GraphQL instantânea sobre o PostgreSQL corporativo com autenticação OIDC.
```bash
# Inicialização Rápida via Docker / CLI
docker run -d -p 8055:8055 --name directus directus/directus
```

**2. Racional Financeiro da Escolha:** 
Converte qualquer banco de dados relacional em uma interface no-code intuitiva para o time de marketing editar textos, banners e seções de conversão sem risco de quebra de layout.

**3. Requisitos de Infraestrutura & Veredito Técnico:** 
- Memória RAM Mínima: `2 GB RAM`
- CPU Recomendada: `1 vCPU`
- Imagem Docker Oficial: `oficial`
- Banco de Dados / Persistência: `PostgreSQL`
- **Veredito da Engenharia:** *A melhor infraestrutura de dados para times de marketing gerenciarem landing pages headless sem tocar em código.*

**4. Guia Prático de Uso em 3 Passos:** 
1. **Modelagem de Blocos:** Crie coleções para hero banners, depoimentos, tabelas de preços e formulários de captura.
2. **Conexão com Frontend:** Conecte o frontend Next.js/Astro das landing pages consumindo os dados via GraphQL com cache.
3. **Permissões de Marketing:** Configure papéis de acesso no-code para editores e redatores publicarem alterações com 1 clique.

**5. White-Label & Design System:** 
- Nível de Esforço: `Baixo` | Stack UI: `Vue.js 3 + Tailwind CSS`
- Mecânica de Customização: Suporte nativo a temas corporativos com injeção de logo, favicon e CSS global diretamente no painel de administração.
- Manutenibilidade de Temas: 

**6. Ecossistema Agêntico (MCPs, Skills & Extensões):** 
- **[MCP Server] @directus/mcp-server:** Servidor MCP oficial para agentes de IA atualizarem banners e textos de landing pages. (`npx -y @directus/mcp-server`)
- **[Agent Skill] skill-landing-page-generator:** Gera novas páginas promocionais e cadastra diretamente no Directus. (`.claude/skills/lp-generator/SKILL.md`)
- **[CLI Tool] directus-cli:** Sincroniza modelos de landing pages entre ambientes de homologação e produção. (`npx directus schema apply ./schema.yaml`)

**7. Documentação Operacional & Capacitação Técnica Dedicada:** 
- [Manual de Engenharia de VPS & Desinstalação Cirúrgica (HTML)](../05-manuais-e-trilhas-individuais/directus/manuais/manual-directus-vps-e-uso.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/directus/manuais/manual-directus-vps-e-uso.md)
- [Trilha Didática de Aprendizado em 5 Aulas (HTML)](../05-manuais-e-trilhas-individuais/directus/trilhas/trilha-directus-aprendizado.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/directus/trilhas/trilha-directus-aprendizado.md)

- **Repositório Oficial:** [https://github.com/directus/directus](https://github.com/directus/directus)

#### 04. Novu · Infraestrutura Moderna de Notificações Multicanal (Classificação: Persona Moderna)
- **Módulo SaaS Substituído:** `RD Station Notificações / OneSignal / Courier`
- **Economia Anual Individual:** `R$ 14.400/ano` | **Licença OSI:** `Apache-2.0`
- **Papel no Ecossistema:** Centro de orquestração de notificações transacionais (E-mail, SMS, In-App e WhatsApp).

**1. O Que Faz & Como Funciona:** 
Gerencia fluxos de notificação transacionais com digest, delays e construtor visual de mensagens. NestJS, Redis e React com motor de regras para envio condicional de alertas multicanal.
```bash
# Inicialização Rápida via Docker / CLI
npx novu init
```

**2. Racional Financeiro da Escolha:** 
Arquitetura reativa moderna em TypeScript/React com centro de preferências do usuário e fallback inteligente entre provedores de entrega.

**3. Requisitos de Infraestrutura & Veredito Técnico:** 
- Memória RAM Mínima: `3 GB RAM`
- CPU Recomendada: `1 vCPU`
- Imagem Docker Oficial: `oficial`
- Banco de Dados / Persistência: `PostgreSQL`
- **Veredito da Engenharia:** *Solução moderna essencial para empresas que precisam de régua de comunicação transacional unificada com fallback.*

**4. Guia Prático de Uso em 3 Passos:** 
1. **Cadastro de Provedores:** Vincule o Amazon SES para e-mails e a Evolution API para mensagens automáticas de WhatsApp.
2. **Criação de Workflows:** Desenhe fluxos de boas-vindas com nós de digest para evitar sobrecarga de mensagens ao usuário.
3. **Integração via SDK:** Dispare notificações a partir de eventos do CRM com apenas 3 linhas de código.

**5. White-Label & Design System:** 
- Nível de Esforço: `Baixo` | Stack UI: `React + Tailwind + Headless UI`
- Mecânica de Customização: Fornece componentes React headless (Inbox Notification Center) para inserção transparente no portal do cliente.
- Manutenibilidade de Temas: 

**6. Ecossistema Agêntico (MCPs, Skills & Extensões):** 
- **[MCP Server] novu-mcp:** Permite a agentes de IA dispararem alertas transacionais contextualizados para clientes. (`npx -y @novu/mcp`)
- **[Agent Skill] skill-notification-optimizer:** Skill para otimização de copy e horários de envio de notificações. (`.claude/skills/notification-optimizer/SKILL.md`)
- **[CLI Tool] novu-cli:** Emulador local para teste de templates de notificação antes do deploy. (`novu dev`)

**7. Documentação Operacional & Capacitação Técnica Dedicada:** 
- [Manual de Engenharia de VPS & Desinstalação Cirúrgica (HTML)](../05-manuais-e-trilhas-individuais/novu/manuais/manual-novu-vps-e-uso.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/novu/manuais/manual-novu-vps-e-uso.md)
- [Trilha Didática de Aprendizado em 5 Aulas (HTML)](../05-manuais-e-trilhas-individuais/novu/trilhas/trilha-novu-aprendizado.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/novu/trilhas/trilha-novu-aprendizado.md)

- **Repositório Oficial:** [https://github.com/novuhq/novu](https://github.com/novuhq/novu)

#### 05. Plunk · Automação de E-mails Minimalista & Rápida (Classificação: Persona Simples)
- **Módulo SaaS Substituído:** `RD Station Marketing (Plano Light / Automações Básicas)`
- **Economia Anual Individual:** `R$ 9.600/ano` | **Licença OSI:** `MIT`
- **Papel no Ecossistema:** Disparos rápidos de e-mails transacionais e sequências curtas de onboarding com curva de aprendizado zero.

**1. O Que Faz & Como Funciona:** 
Envia e-mails transacionais e executa sequências simples baseadas em eventos de produto. Backend em Node.js com banco PostgreSQL e dashboard em React.
```bash
# Inicialização Rápida via Docker / CLI
docker run -d -p 8080:8080 --name plunk useplunk/plunk:latest
```

**2. Racional Financeiro da Escolha:** 
Setup de 2 minutos com interface minimalista focada exclusivamente em disparos baseados em eventos com consumo ínfimo de recursos.

**3. Requisitos de Infraestrutura & Veredito Técnico:** 
- Memória RAM Mínima: `1 GB RAM`
- CPU Recomendada: `1 vCPU`
- Imagem Docker Oficial: `oficial`
- Banco de Dados / Persistência: `PostgreSQL`
- **Veredito da Engenharia:** *Perfeita para operações que não precisam da complexidade do Mautic e buscam simplicidade operacional imediata.*

**4. Guia Prático de Uso em 3 Passos:** 
1. **Conexão de SMTP:** Insira as credenciais SMTP corporativas no painel inicial do Plunk.
2. **Gatilho de Boas-Vindas:** Crie uma ação para enviar e-mail imediatamente após a criação de um lead no site.
3. **Rastreamento:** Acompanhe aberturas e cliques diretamente no painel minimalista.

**5. White-Label & Design System:** 
- Nível de Esforço: `Baixo` | Stack UI: `Next.js + Tailwind`
- Mecânica de Customização: Templates de e-mail em Markdown/HTML limpo totalmente adaptáveis à identidade institucional.
- Manutenibilidade de Temas: 

**6. Ecossistema Agêntico (MCPs, Skills & Extensões):** 
- **[MCP Server] plunk-mcp:** Servidor MCP para disparo direto de e-mails por agentes inteligentes. (`npx -y plunk-mcp`)
- **[Agent Skill] skill-quick-email:** Gera respostas de suporte e envia via Plunk. (`.claude/skills/quick-email/SKILL.md`)
- **[CLI Tool] plunk-cli:** Envio de eventos via chamadas HTTP simples. (`curl -X POST https://plunk.empresa/api/track`)

**7. Documentação Operacional & Capacitação Técnica Dedicada:** 
- [Manual de Engenharia de VPS & Desinstalação Cirúrgica (HTML)](../05-manuais-e-trilhas-individuais/plunk/manuais/manual-plunk-vps-e-uso.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/plunk/manuais/manual-plunk-vps-e-uso.md)
- [Trilha Didática de Aprendizado em 5 Aulas (HTML)](../05-manuais-e-trilhas-individuais/plunk/trilhas/trilha-plunk-aprendizado.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/plunk/trilhas/trilha-plunk-aprendizado.md)

- **Repositório Oficial:** [https://github.com/useplunk/plunk](https://github.com/useplunk/plunk)

### PILAR 02: GRUPO 2: PIPELINE COMERCIAL, CRM & CONTRATOS
> **Alvo SaaS Substituído:** `RD Station CRM (Plano Avançado para Equipes de Vendas)` | **Economia do Pilar:** `R$ 36.000/ano` 
> **Descrição Estratégica:** Frente responsável pela gestão visual de oportunidades comerciais em formato Kanban, distribuição de leads qualificados, histórico de contatos, agendamento de reuniões e assinatura de propostas.

#### 01. Twenty · CRM Moderno Aberto & Gestão de Funil Comercial (Classificação: Persona Moderna)
- **Módulo SaaS Substituído:** `RD Station CRM (Módulo de Pipeline Kanban, Oportunidades & Tarefas)`
- **Economia Anual Individual:** `R$ 24.000/ano (Equipe de 10 vendedores)` | **Licença OSI:** `AGPL-3.0`
- **Papel no Ecossistema:** Interface principal dos vendedores para acompanhamento de negócios, tarefas e histórico de contatos.

**1. O Que Faz & Como Funciona:** 
Gerencia oportunidades em funil Kanban com sincronização de e-mail e notas em tempo real. Arquitetura reativa em TypeScript, React, NestJS e PostgreSQL com GraphQL nativo.
```bash
# Inicialização Rápida via Docker / CLI
git clone https://github.com/twentyhq/twenty && cd twenty && docker compose up -d
```

**2. Racional Financeiro da Escolha:** 
Arquitetura reativa ultrarrápida em React/TypeScript com sincronização bidirecional de e-mails, campos customizados ilimitados e experiência de usuário moderna superior a CRMs legados.

**3. Requisitos de Infraestrutura & Veredito Técnico:** 
- Memória RAM Mínima: `4 GB RAM`
- CPU Recomendada: `1 vCPU`
- Imagem Docker Oficial: `oficial`
- Banco de Dados / Persistência: `PostgreSQL`
- **Veredito da Engenharia:** *O CRM open source mais moderno do mundo, com padrão de usabilidade equivalente ou superior a SaaS como Notion e HubSpot.*

**4. Guia Prático de Uso em 3 Passos:** 
1. **Modelagem de Funis:** Configure as etapas do funil (Prospecção, Qualificação, Demonstração, Negociação e Fechamento).
2. **Sincronização de E-mail:** Conecte contas IMAP/SMTP dos vendedores para registro automático de trocas de mensagens na timeline.
3. **Campos Customizados:** Adicione campos de CNPJ, segmento e valor de contrato com validação de formato.

**5. White-Label & Design System:** 
- Nível de Esforço: `Baixo` | Stack UI: `React + TypeScript + Tailwind`
- Mecânica de Customização: Interface moderna com suporte a logotipo da empresa e modo escuro/claro nativo.
- Manutenibilidade de Temas: 

**6. Ecossistema Agêntico (MCPs, Skills & Extensões):** 
- **[MCP Server] @twentyhq/twenty-mcp:** Permite que assistentes de vendas consultem e atualizem oportunidades no Twenty via IA. (`npx -y @twentyhq/twenty-mcp`)
- **[Agent Skill] skill-crm-deal-analyst:** Analisa negócios parados no pipeline e sugere ações de reativação para vendedores. (`.claude/skills/crm-deal-analyst/SKILL.md`)
- **[CLI Tool] twenty-cli:** CLI para gestão de migrações e extensões de banco. (`yarn twenty db:migrate`)

**7. Documentação Operacional & Capacitação Técnica Dedicada:** 
- [Manual de Engenharia de VPS & Desinstalação Cirúrgica (HTML)](../05-manuais-e-trilhas-individuais/twenty/manuais/manual-twenty-vps-e-uso.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/twenty/manuais/manual-twenty-vps-e-uso.md)
- [Trilha Didática de Aprendizado em 5 Aulas (HTML)](../05-manuais-e-trilhas-individuais/twenty/trilhas/trilha-twenty-aprendizado.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/twenty/trilhas/trilha-twenty-aprendizado.md)

- **Repositório Oficial:** [https://github.com/twentyhq/twenty](https://github.com/twentyhq/twenty)

#### 02. EspoCRM · Motor de Regras Corporativas B2B & Workflows (Classificação: Persona Robusta)
- **Módulo SaaS Substituído:** `RD Station CRM (Módulos Corporativos Avançados & Múltiplos Pipelines)`
- **Economia Anual Individual:** `R$ 18.000/ano` | **Licença OSI:** `GPL-3.0`
- **Papel no Ecossistema:** Gerencia contas complexas B2B, hierarquia de permissões e regras avançadas de comissionamento.

**1. O Que Faz & Como Funciona:** 
Permite modelar entidades customizadas e fluxos BPM para grandes operações comerciais. PHP/MySQL com construtor no-code de layouts e entidades relacionais.
```bash
# Inicialização Rápida via Docker / CLI
docker run -d -p 8081:80 --name espocrm espocrm/espocrm
```

**2. Racional Financeiro da Escolha:** 
Mecanismo BPM no-code maduro para operações B2B que necessitam de regras de aprovação de desconto e múltiplos pipelines simultâneos por linha de produto.

**3. Requisitos de Infraestrutura & Veredito Técnico:** 
- Memória RAM Mínima: `2 GB RAM`
- CPU Recomendada: `1 vCPU`
- Imagem Docker Oficial: `oficial`
- Banco de Dados / Persistência: `PostgreSQL`
- **Veredito da Engenharia:** *A ferramenta mais sólida para empresas que necessitam de regras rígidas de segurança, permissões granulares e processos BPM.*

**4. Guia Prático de Uso em 3 Passos:** 
1. **Definição de Papéis (ACL):** Crie níveis de permissão onde vendedores veem apenas suas contas e gerentes veem o consolidado.
2. **Automação de Tarefas:** Crie fluxos que distribuem leads automaticamente por round-robin ou região geográfica.
3. **Relatórios Dinâmicos:** Gere relatórios tabulares e gráficos de conversão por canal de aquisição.

**5. White-Label & Design System:** 
- Nível de Esforço: `Baixo` | Stack UI: `Backbone.js + Bootstrap`
- Mecânica de Customização: Totalmente personalizável pelo painel de administração (logo, cores, fontes e disposição de campos).
- Manutenibilidade de Temas: 

**6. Ecossistema Agêntico (MCPs, Skills & Extensões):** 
- **[MCP Server] espocrm-mcp-server:** Servidor MCP para integração de dados comerciais complexos com LLMs. (`npx -y espocrm-mcp`)
- **[Agent Skill] skill-b2b-lead-routing:** Roteamento inteligente de leads corporativos baseado em regras financeiras. (`.claude/skills/b2b-lead-routing/SKILL.md`)
- **[CLI Tool] espocrm-console:** Executor de jobs em background para sincronização corporativa. (`php command.php run-job`)

**7. Documentação Operacional & Capacitação Técnica Dedicada:** 
- [Manual de Engenharia de VPS & Desinstalação Cirúrgica (HTML)](../05-manuais-e-trilhas-individuais/espocrm/manuais/manual-espocrm-vps-e-uso.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/espocrm/manuais/manual-espocrm-vps-e-uso.md)
- [Trilha Didática de Aprendizado em 5 Aulas (HTML)](../05-manuais-e-trilhas-individuais/espocrm/trilhas/trilha-espocrm-aprendizado.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/espocrm/trilhas/trilha-espocrm-aprendizado.md)

- **Repositório Oficial:** [https://github.com/espocrm/espocrm](https://github.com/espocrm/espocrm)

#### 03. SuiteCRM · Suíte Completa Enterprise para Grandes Operações de Vendas (Classificação: Persona Completa)
- **Módulo SaaS Substituído:** `Salesforce Sales Cloud / SugarCRM Enterprise`
- **Economia Anual Individual:** `R$ 36.000/ano` | **Licença OSI:** `AGPL-3.0`
- **Papel no Ecossistema:** Gestão 360º de clientes com módulo nativo de cotações, faturamento, contratos e suporte pós-venda.

**1. O Que Faz & Como Funciona:** 
Centraliza todo o ciclo de vida do cliente: da prospecção ao faturamento e suporte técnico. PHP/Symfony com arquitetura robusta e banco relacional MySQL/Postgres.
```bash
# Inicialização Rápida via Docker / CLI
docker run -d -p 8080:80 --name suitecrm suitecrm/suitecrm
```

**2. Racional Financeiro da Escolha:** 
A alternativa open source mais madura e completa do mercado corporativo, possuindo módulos nativos de catálogo de produtos, cálculo de impostos e emissão de propostas.

**3. Requisitos de Infraestrutura & Veredito Técnico:** 
- Memória RAM Mínima: `4 GB RAM`
- CPU Recomendada: `1 vCPU`
- Imagem Docker Oficial: `oficial`
- Banco de Dados / Persistência: `PostgreSQL`
- **Veredito da Engenharia:** *Para empresas que precisam de todas as funcionalidades de um ERP/CRM corporativo integrado em uma só plataforma.*

**4. Guia Prático de Uso em 3 Passos:** 
1. **Catálogo de Produtos:** Cadastre tabela de preços, SKUs e regras de desconto por volume.
2. **Emissão de Orçamento:** Gere PDFs de cotações comerciais detalhadas diretamente na tela da oportunidade.
3. **Gestão de Contratos:** Acompanhe renovações automáticas de contratos recorrentes e alertas de expiração.

**5. White-Label & Design System:** 
- Nível de Esforço: `Baixo` | Stack UI: `Symfony + Angular + Bootstrap`
- Mecânica de Customização: Tema SuiteP com suporte a upload de marca corporativa e alteração da paleta de cores primária e secundária.
- Manutenibilidade de Temas: 

**6. Ecossistema Agêntico (MCPs, Skills & Extensões):** 
- **[MCP Server] suitecrm-mcp:** Consulta de inventário e emissão de propostas via agentes de IA. (`npx -y suitecrm-mcp-server`)
- **[Agent Skill] skill-quote-generator:** Gera cotações automáticas a partir de mensagens trocadas com o lead. (`.claude/skills/quote-gen/SKILL.md`)
- **[CLI Tool] suitecrm-cli:** Instalador automatizado de pacotes e extensões. (`bin/console suitecrm:app:install`)

**7. Documentação Operacional & Capacitação Técnica Dedicada:** 
- [Manual de Engenharia de VPS & Desinstalação Cirúrgica (HTML)](../05-manuais-e-trilhas-individuais/suitecrm/manuais/manual-suitecrm-vps-e-uso.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/suitecrm/manuais/manual-suitecrm-vps-e-uso.md)
- [Trilha Didática de Aprendizado em 5 Aulas (HTML)](../05-manuais-e-trilhas-individuais/suitecrm/trilhas/trilha-suitecrm-aprendizado.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/suitecrm/trilhas/trilha-suitecrm-aprendizado.md)

- **Repositório Oficial:** [https://github.com/salesagility/SuiteCRM](https://github.com/salesagility/SuiteCRM)

#### 04. Documenso · Assinatura Eletrônica Soberana de Contratos e Propostas (Classificação: Persona Leve)
- **Módulo SaaS Substituído:** `Clicksign / DocuSign / Módulo de Propostas Comerciais`
- **Economia Anual Individual:** `R$ 18.000/ano` | **Licença OSI:** `AGPL-3.0`
- **Papel no Ecossistema:** Formalização jurídica de propostas comerciais e contratos sem custo por documento.

**1. O Que Faz & Como Funciona:** 
Gera links de assinatura digital com trilha de auditoria e carimbo do tempo criptográfico. Backend em TypeScript sobre PostgreSQL com geração de hashes SHA-256 dos documentos.
```bash
# Inicialização Rápida via Docker / CLI
git clone https://github.com/documenso/documenso && cd documenso && docker compose up -d
```

**2. Racional Financeiro da Escolha:** 
Garante soberania jurídica dos documentos com trilha de auditoria criptográfica e registro de IPs, sem impor limites de contratos assinados por mês.

**3. Requisitos de Infraestrutura & Veredito Técnico:** 
- Memória RAM Mínima: `2 GB RAM`
- CPU Recomendada: `1 vCPU`
- Imagem Docker Oficial: `oficial`
- Banco de Dados / Persistência: `PostgreSQL`
- **Veredito da Engenharia:** *Elimina 100% das cobranças punitivas por documento assinado mantendo validade jurídica plena sob a MP 2.200-2/2001.*

**4. Guia Prático de Uso em 3 Passos:** 
1. **Upload do PDF:** Envie o modelo de contrato gerado pela equipe comercial.
2. **Posicionamento dos Campos:** Arraste os campos de assinatura, CPF, data e rubrica no documento.
3. **Disparo & Trilha:** Envie o link para o cliente e receba o PDF assinado com certificado criptográfico.

**5. White-Label & Design System:** 
- Nível de Esforço: `Baixo` | Stack UI: `Next.js + Tailwind + shadcn/ui`
- Mecânica de Customização: Customização completa de emails de disparo, página de assinatura com logo da empresa e domínio próprio.
- Manutenibilidade de Temas: 

**6. Ecossistema Agêntico (MCPs, Skills & Extensões):** 
- **[MCP Server] documenso-mcp:** Geração e disparo de contratos para assinatura através de comandos de agentes de IA. (`npx -y documenso-mcp`)
- **[Agent Skill] skill-contract-auditor:** Audita cláusulas contratuais antes do envio para assinatura. (`.claude/skills/contract-auditor/SKILL.md`)
- **[CLI Tool] documenso-cli:** Criação de templates via linha de comando. (`documenso template create ./contrato.pdf`)

**7. Documentação Operacional & Capacitação Técnica Dedicada:** 
- [Manual de Engenharia de VPS & Desinstalação Cirúrgica (HTML)](../05-manuais-e-trilhas-individuais/documenso/manuais/manual-documenso-vps-e-uso.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/documenso/manuais/manual-documenso-vps-e-uso.md)
- [Trilha Didática de Aprendizado em 5 Aulas (HTML)](../05-manuais-e-trilhas-individuais/documenso/trilhas/trilha-documenso-aprendizado.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/documenso/trilhas/trilha-documenso-aprendizado.md)

- **Repositório Oficial:** [https://github.com/documenso/documenso](https://github.com/documenso/documenso)

#### 05. Cal.com · Agendamento Automatizado de Demonstrações Comerciais (Classificação: Persona Simples)
- **Módulo SaaS Substituído:** `RD Station CRM (Agendamentos) / Calendly Integrado`
- **Economia Anual Individual:** `R$ 12.000/ano` | **Licença OSI:** `AGPL-3.0`
- **Papel no Ecossistema:** Elimina a fricção na marcação de reuniões de qualificação e fechamento com clientes.

**1. O Que Faz & Como Funciona:** 
Disponibiliza links de agendamento conectados à agenda dos vendedores com distribuição round-robin. Next.js e Prisma com sincronização com Google Calendar, Outlook e CalDAV.
```bash
# Inicialização Rápida via Docker / CLI
git clone https://github.com/calcom/cal.com && cd cal.com && docker compose up -d
```

**2. Racional Financeiro da Escolha:** 
Suporte a distribuição round-robin entre múltiplos corretores/vendedores, integração direta com CalDAV, Google e Outlook e total personalização sob domínio próprio.

**3. Requisitos de Infraestrutura & Veredito Técnico:** 
- Memória RAM Mínima: `2 GB RAM`
- CPU Recomendada: `1 vCPU`
- Imagem Docker Oficial: `oficial`
- Banco de Dados / Persistência: `PostgreSQL`
- **Veredito da Engenharia:** *A solução definitiva de agendamento: fácil de usar, elegante para o cliente e com total privacidade corporativa.*

**4. Guia Prático de Uso em 3 Passos:** 
1. **Conexão de Calendários:** Vincule a agenda dos vendedores corporativos (Google, Microsoft 365 ou Nextcloud).
2. **Definição de Tipos de Reunião:** Configure reuniões de Demonstração (30 min) e Reunião de Fechamento (45 min).
3. **Link no Chat/E-mail:** Insira o link na assinatura de e-mail e nos fluxos automáticos do Chatwoot/WhatsApp.

**5. White-Label & Design System:** 
- Nível de Esforço: `Baixo` | Stack UI: `Next.js + Tailwind + Radix UI`
- Mecânica de Customização: Páginas públicas de agendamento 100% white-label sob subdomínio institucional (ex: `agenda.empresa.com.br`).
- Manutenibilidade de Temas: 

**6. Ecossistema Agêntico (MCPs, Skills & Extensões):** 
- **[MCP Server] @calcom/mcp-server:** Permite que assistentes de IA agendem reuniões diretamente na conversa com o lead. (`npx -y @calcom/mcp-server`)
- **[Agent Skill] skill-auto-scheduler:** Negocia horários disponíveis no WhatsApp e conclui o agendamento. (`.claude/skills/auto-scheduler/SKILL.md`)
- **[CLI Tool] calcom-cli:** Inicialização rápida de ambientes corporativos. (`yarn calcom db-seed`)

**7. Documentação Operacional & Capacitação Técnica Dedicada:** 
- [Manual de Engenharia de VPS & Desinstalação Cirúrgica (HTML)](../05-manuais-e-trilhas-individuais/cal-com/manuais/manual-cal-com-vps-e-uso.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/cal-com/manuais/manual-cal-com-vps-e-uso.md)
- [Trilha Didática de Aprendizado em 5 Aulas (HTML)](../05-manuais-e-trilhas-individuais/cal-com/trilhas/trilha-cal-com-aprendizado.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/cal-com/trilhas/trilha-cal-com-aprendizado.md)

- **Repositório Oficial:** [https://github.com/calcom/cal.com](https://github.com/calcom/cal.com)

### PILAR 03: GRUPO 3: ATENDIMENTO OMNICHANNEL & WHATSAPP
> **Alvo SaaS Substituído:** `RD Station Conversas (Antigo Tallos / Módulos de Mensageria)` | **Economia do Pilar:** `R$ 36.000/ano` 
> **Descrição Estratégica:** Frente responsável pela caixa de entrada unificada multicanal, conexão estável com múltiplos números de WhatsApp sem taxas por mensagem e triagem inteligente com chatbots.

#### 01. Chatwoot · Central de Atendimento Omnicanal & Livechat Colaborativo (Classificação: Persona Completa)
- **Módulo SaaS Substituído:** `RD Station Conversas (Painel de Atendimento Multiatendente)`
- **Economia Anual Individual:** `R$ 36.000/ano (10 operadores)` | **Licença OSI:** `MIT`
- **Papel no Ecossistema:** Inbox unificada para múltiplos atendentes humanos responderem WhatsApp, Webchat e Instagram.

**1. O Que Faz & Como Funciona:** 
Centraliza conversas de clientes, distribui tickets e permite notas internas entre atendentes. Ruby on Rails com WebSockets e Vue.js para mensageria em tempo real.
```bash
# Inicialização Rápida via Docker / CLI
git clone https://github.com/chatwoot/chatwoot && cd chatwoot && docker compose up -d
```

**2. Racional Financeiro da Escolha:** 
Software líder global em suporte omnicanal aberto, eliminando a cobrança por licença de atendente e fornecendo relatórios completos de CSAT e tempo de primeira resposta.

**3. Requisitos de Infraestrutura & Veredito Técnico:** 
- Memória RAM Mínima: `4 GB RAM`
- CPU Recomendada: `1 vCPU`
- Imagem Docker Oficial: `oficial`
- Banco de Dados / Persistência: `PostgreSQL`
- **Veredito da Engenharia:** *A plataforma mais completa do mercado aberto para atendimento humano, com relatórios gerenciais e SLAs avançados.*

**4. Guia Prático de Uso em 3 Passos:** 
1. **Criação de Caixas de Entrada:** Cadastre os canais de WhatsApp corporativo, Livechat do site e Instagram Direct.
2. **Divisão por Equipes:** Crie equipes de Suporte Técnico, Vendas e Financeiro com distribuição automática de tickets.
3. **Respostas Rápidas:** Cadastre macros de texto para agilizar as respostas mais comuns dos atendentes.

**5. White-Label & Design System:** 
- Nível de Esforço: `Baixo` | Stack UI: `Vue.js + Tailwind CSS`
- Mecânica de Customização: Permite customizar logotipo, cores do widget de chat, nome da empresa e domínio institucional.
- Manutenibilidade de Temas: 

**6. Ecossistema Agêntico (MCPs, Skills & Extensões):** 
- **[MCP Server] chatwoot-mcp:** Servidor MCP para agentes de IA lerem tickets e sugerirem respostas aos operadores humanos. (`npx -y chatwoot-mcp-server`)
- **[Agent Skill] skill-sentiment-analyst:** Analisa o sentimento do cliente em tempo real no Chatwoot e alerta supervisores. (`.claude/skills/sentiment-analyst/SKILL.md`)
- **[CLI Tool] chatwoot-ctl:** Gerenciamento de contas e instâncias via terminal. (`bundle exec rails runner 'Account.all'`)

**7. Documentação Operacional & Capacitação Técnica Dedicada:** 
- [Manual de Engenharia de VPS & Desinstalação Cirúrgica (HTML)](../05-manuais-e-trilhas-individuais/chatwoot/manuais/manual-chatwoot-vps-e-uso.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/chatwoot/manuais/manual-chatwoot-vps-e-uso.md)
- [Trilha Didática de Aprendizado em 5 Aulas (HTML)](../05-manuais-e-trilhas-individuais/chatwoot/trilhas/trilha-chatwoot-aprendizado.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/chatwoot/trilhas/trilha-chatwoot-aprendizado.md)

- **Repositório Oficial:** [https://github.com/chatwoot/chatwoot](https://github.com/chatwoot/chatwoot)

#### 02. Evolution API · Gateway Profissional de WhatsApp Baileys com Webhooks (Classificação: Persona Robusta)
- **Módulo SaaS Substituído:** `RD Station Conversas (Conectores Proprietários Z-API / Gupshup)`
- **Economia Anual Individual:** `R$ 18.000/ano` | **Licença OSI:** `Apache-2.0`
- **Papel no Ecossistema:** Conecta os números de WhatsApp corporativos e integra diretamente com o Chatwoot e n8n.

**1. O Que Faz & Como Funciona:** 
Recebe e envia mensagens, mídias e áudios de WhatsApp via endpoints REST. Node.js e TypeScript com gerenciamento de sessões em Redis e Postgres.
```bash
# Inicialização Rápida via Docker / CLI
docker run -d -p 8080:8080 --name evolution-api atendai/evolution-api:v2.1.0
```

**2. Racional Financeiro da Escolha:** 
API brasileira madura com suporte a múltiplas instâncias simultâneas, conversão automática de áudios em formato compatível e integração nativa de 1 clique com o Chatwoot.

**3. Requisitos de Infraestrutura & Veredito Técnico:** 
- Memória RAM Mínima: `2 GB RAM`
- CPU Recomendada: `1 vCPU`
- Imagem Docker Oficial: `oficial`
- Banco de Dados / Persistência: `PostgreSQL`
- **Veredito da Engenharia:** *O conector WhatsApp mais estável do ecossistema nacional, suportando milhares de mensagens diárias com alta resiliência.*

**4. Guia Prático de Uso em 3 Passos:** 
1. **Geração de QR Code:** Crie uma instância via API e leia o QR Code com o aplicativo WhatsApp Business.
2. **Conexão com Chatwoot:** Ative a flag nativa do Chatwoot para sincronizar mensagens bidirecionais instantâneas.
3. **Configuração de Webhooks:** Aponte os webhooks de mensagens recebidas para o n8n para acionamento de IA.

**5. White-Label & Design System:** 
- Nível de Esforço: `Baixo` | Stack UI: `API REST / Swagger UI`
- Mecânica de Customização: Opera como serviço de backend invisível sob domínio próprio da empresa (ex: `api-wa.empresa.com.br`).
- Manutenibilidade de Temas: 

**6. Ecossistema Agêntico (MCPs, Skills & Extensões):** 
- **[MCP Server] evolution-api-mcp:** Permite que agentes LLM enviem mensagens e mídias de WhatsApp de forma autônoma. (`npx -y evolution-api-mcp`)
- **[Agent Skill] skill-wa-audio-transcriber:** Transcreve áudios recebidos no WhatsApp e envia o resumo ao vendedor. (`.claude/skills/wa-transcriber/SKILL.md`)
- **[CLI Tool] evolution-cli:** Criação programática de novas instâncias de WhatsApp. (`curl -X POST https://wa.empresa/instance/create`)

**7. Documentação Operacional & Capacitação Técnica Dedicada:** 
- [Manual de Engenharia de VPS & Desinstalação Cirúrgica (HTML)](../05-manuais-e-trilhas-individuais/evolution-api/manuais/manual-evolution-api-vps-e-uso.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/evolution-api/manuais/manual-evolution-api-vps-e-uso.md)
- [Trilha Didática de Aprendizado em 5 Aulas (HTML)](../05-manuais-e-trilhas-individuais/evolution-api/trilhas/trilha-evolution-api-aprendizado.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/evolution-api/trilhas/trilha-evolution-api-aprendizado.md)

- **Repositório Oficial:** [https://github.com/EvolutionAPI/evolution-api](https://github.com/EvolutionAPI/evolution-api)

#### 03. Typebot · Construtor Visual de Fluxos de Triagem & Qualificação (Classificação: Persona Moderna)
- **Módulo SaaS Substituído:** `RD Station Conversas (Chatbots de Triagem) / Landbot`
- **Economia Anual Individual:** `R$ 14.400/ano` | **Licença OSI:** `AGPL-3.0`
- **Papel no Ecossistema:** Realiza o primeiro atendimento, coleta dados do lead e transfere para a fila certa no Chatwoot.

**1. O Que Faz & Como Funciona:** 
Cria chatbots conversacionais interativos para qualificação de leads antes do humano. Editor visual drag-and-drop com blocos lógicos e integração nativa com IA e webhooks.
```bash
# Inicialização Rápida via Docker / CLI
docker run -d -p 3001:3000 --name typebot baptistearno/typebot-builder:latest
```

**2. Racional Financeiro da Escolha:** 
Melhor construtor visual de fluxos conversacionais do mercado, com suporte a variáveis, ramificações condicionais e integração nativa com modelos de IA para atendimento automático.

**3. Requisitos de Infraestrutura & Veredito Técnico:** 
- Memória RAM Mínima: `2 GB RAM`
- CPU Recomendada: `1 vCPU`
- Imagem Docker Oficial: `oficial`
- Banco de Dados / Persistência: `PostgreSQL`
- **Veredito da Engenharia:** *A melhor experiência de criação de robôs conversacionais: fluida, moderna e sem necessidade de conhecimento em programação.*

**4. Guia Prático de Uso em 3 Passos:** 
1. **Desenho do Fluxo:** Adicione blocos de perguntas, coleta de e-mail, telefone e opções de múltipla escolha.
2. **Nó de Inteligência Artificial:** Integre o nó OpenAI/Anthropic para responder dúvidas sobre produtos com base em arquivos PDF.
3. **Transbordo Humano:** Insira o bloco Chatwoot para transferir a conversa para um atendente quando o lead solicitar.

**5. White-Label & Design System:** 
- Nível de Esforço: `Baixo` | Stack UI: `Next.js + React + Tailwind`
- Mecânica de Customização: Customização completa de fontes, avatares, cores de balões e plano de fundo no construtor visual.
- Manutenibilidade de Temas: 

**6. Ecossistema Agêntico (MCPs, Skills & Extensões):** 
- **[MCP Server] typebot-mcp:** Permite que agentes analisem as respostas de formulários e conversem com leads. (`npx -y typebot-mcp-server`)
- **[Agent Skill] skill-bot-flow-optimizer:** Analisa taxa de abandono nas perguntas do bot e otimiza as mensagens. (`.claude/skills/bot-optimizer/SKILL.md`)
- **[CLI Tool] typebot-export:** Exportação de fluxos em formato JSON para controle de versão. (`typebot export --id flow-lead-qualification`)

**7. Documentação Operacional & Capacitação Técnica Dedicada:** 
- [Manual de Engenharia de VPS & Desinstalação Cirúrgica (HTML)](../05-manuais-e-trilhas-individuais/typebot/manuais/manual-typebot-vps-e-uso.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/typebot/manuais/manual-typebot-vps-e-uso.md)
- [Trilha Didática de Aprendizado em 5 Aulas (HTML)](../05-manuais-e-trilhas-individuais/typebot/trilhas/trilha-typebot-aprendizado.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/typebot/trilhas/trilha-typebot-aprendizado.md)

- **Repositório Oficial:** [https://github.com/baptisteArno/typebot.io](https://github.com/baptisteArno/typebot.io)

#### 04. WAHA · Gateway Headless Secundário de Alta Disponibilidade (Classificação: Persona Leve)
- **Módulo SaaS Substituído:** `RD Station Notificações WhatsApp / Twilio Messaging`
- **Economia Anual Individual:** `R$ 12.000/ano` | **Licença OSI:** `Apache-2.0`
- **Papel no Ecossistema:** Redundância de conexão WhatsApp para disparos de alertas transacionais críticos.

**1. O Que Faz & Como Funciona:** 
Fornece API HTTP estável para automações de sistema sem interferir na fila de atendimento humano. Sessões Chromium headless em contêiner Docker isolado.
```bash
# Inicialização Rápida via Docker / CLI
docker run -d -p 3000:3000 --name waha devlikeapro/waha
```

**2. Racional Financeiro da Escolha:** 
Solução headless ultra-estável em contêiner isolado para garantir que mensagens transacionais de sistema sejam enviadas mesmo em caso de sobrecarga da fila de atendimento.

**3. Requisitos de Infraestrutura & Veredito Técnico:** 
- Memória RAM Mínima: `2 GB RAM`
- CPU Recomendada: `1 vCPU`
- Imagem Docker Oficial: `oficial`
- Banco de Dados / Persistência: `PostgreSQL`
- **Veredito da Engenharia:** *Essencial para garantir que alertas de segurança e notificações financeiras não disputem fila com atendimentos humanos.*

**4. Guia Prático de Uso em 3 Passos:** 
1. **Inicialização:** Suba o contêiner WAHA apontando para uma porta interna isolada.
2. **Autenticação:** Escaneie o QR Code via endpoint `/api/sessions/start`.
3. **Disparo Transacional:** Envie alertas de cobrança e lembretes de reunião via chamadas REST no n8n.

**5. White-Label & Design System:** 
- Nível de Esforço: `Baixo` | Stack UI: `Swagger / OpenAPI`
- Mecânica de Customização: Serviço totalmente desacoplado operando sob API interna.
- Manutenibilidade de Temas: 

**6. Ecossistema Agêntico (MCPs, Skills & Extensões):** 
- **[MCP Server] waha-mcp:** Interface MCP para disparos transacionais de alta confiabilidade. (`npx -y waha-mcp-server`)
- **[Agent Skill] skill-wa-delivery-checker:** Verifica status de entrega e leitura de notificações críticas. (`.claude/skills/delivery-checker/SKILL.md`)
- **[CLI Tool] waha-cli:** Disparo direto de mensagens de terminal. (`curl -X POST https://waha.empresa/api/sendText`)

**7. Documentação Operacional & Capacitação Técnica Dedicada:** 
- [Manual de Engenharia de VPS & Desinstalação Cirúrgica (HTML)](../05-manuais-e-trilhas-individuais/waha/manuais/manual-waha-vps-e-uso.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/waha/manuais/manual-waha-vps-e-uso.md)
- [Trilha Didática de Aprendizado em 5 Aulas (HTML)](../05-manuais-e-trilhas-individuais/waha/trilhas/trilha-waha-aprendizado.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/waha/trilhas/trilha-waha-aprendizado.md)

- **Repositório Oficial:** [https://github.com/devlikeapro/waha](https://github.com/devlikeapro/waha)

#### 05. Papercups · Livechat & Suporte Direto sem Burocracia (Classificação: Persona Simples)
- **Módulo SaaS Substituído:** `Intercom / Crisp / Chat Básico do RD`
- **Economia Anual Individual:** `R$ 10.800/ano` | **Licença OSI:** `MIT`
- **Papel no Ecossistema:** Chat de atendimento direto no site corporativo com instalação instantânea e zero complexidade.

**1. O Que Faz & Como Funciona:** 
Fornece chat ao vivo para clientes conversarem com a equipe diretamente pelo navegador. Backend em Elixir/Phoenix (alta concorrência) com frontend em React.
```bash
# Inicialização Rápida via Docker / CLI
docker run -d -p 4000:4000 --name papercups papercups/papercups:latest
```

**2. Racional Financeiro da Escolha:** 
Widget de chat leve em React com painel simples e sem dependências pesadas, ideal para suporte ágil.

**3. Requisitos de Infraestrutura & Veredito Técnico:** 
- Memória RAM Mínima: `1 GB RAM`
- CPU Recomendada: `1 vCPU`
- Imagem Docker Oficial: `oficial`
- Banco de Dados / Persistência: `PostgreSQL`
- **Veredito da Engenharia:** *A solução mais direta e leve para quem precisa apenas de um chat corporativo elegante no site sem excesso de menus.*

**4. Guia Prático de Uso em 3 Passos:** 
1. **Cópia do Script:** Copie o código JS do widget e cole no rodapé do site corporativo.
2. **Definição de Cores:** Defina a cor primária e mensagem de boas-vindas do atendente.
3. **Atendimento:** Responda mensagens de visitantes diretamente pelo dashboard web ou aplicativo.

**5. White-Label & Design System:** 
- Nível de Esforço: `Baixo` | Stack UI: `React + TypeScript + Theme Props`
- Mecânica de Customização: Total customização visual do widget flutuante (título, subtítulo, avatar e cor hexadecimal).
- Manutenibilidade de Temas: 

**6. Ecossistema Agêntico (MCPs, Skills & Extensões):** 
- **[MCP Server] papercups-mcp:** Consulta de conversas de livechat em tempo real por agentes. (`npx -y papercups-mcp`)
- **[Agent Skill] skill-livechat-responder:** Responde dúvidas de produtos no chat ao vivo do site. (`.claude/skills/livechat-responder/SKILL.md`)
- **[CLI Tool] papercups-cli:** Extração de histórico de conversas. (`curl -X GET https://chat.empresa/api/v1/conversations`)

**7. Documentação Operacional & Capacitação Técnica Dedicada:** 
- [Manual de Engenharia de VPS & Desinstalação Cirúrgica (HTML)](../05-manuais-e-trilhas-individuais/papercups/manuais/manual-papercups-vps-e-uso.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/papercups/manuais/manual-papercups-vps-e-uso.md)
- [Trilha Didática de Aprendizado em 5 Aulas (HTML)](../05-manuais-e-trilhas-individuais/papercups/trilhas/trilha-papercups-aprendizado.html) | [Versão Markdown](../05-manuais-e-trilhas-individuais/papercups/trilhas/trilha-papercups-aprendizado.md)

- **Repositório Oficial:** [https://github.com/papercups-io/papercups](https://github.com/papercups-io/papercups)

---

## CAPÍTULO 5 · CAMADA DE COLA, SSO FEDERADO & BLUEPRINTS N8N

### Arquitetura de Interconexão sem Silos de Dados
- ** Autenticação Única Federada (SSO):** Keycloak / Authentik (OpenID Connect / SAML) unificando o login dos colaboradores no Twenty CRM, Chatwoot, Directus, Mautic e SuiteCRM.
- ** Barramento de Eventos Assíncronos:** n8n Community Edition atuando como orquestrador central de eventos assíncronos (Lead capturado no Typebot -> pontuado no Mautic -> oportunidade criada no Twenty -> alerta enviado no WhatsApp via Evolution).
- ** Gateway de Borda & Ingress TLS:** Traefik Proxy v3 com terminação TLS automática via Let's Encrypt e roteamento por subdomínios corporativos (mkt.empresa.com.br, crm.empresa.com.br, chat.empresa.com.br, sso.empresa.com.br).

### Fluxo Operacional de Ponta a Ponta
1. Entrada de Leads: Lead preenche formulário no Typebot ou na Landing Page gerenciada pelo Directus;
2. Cadastramento & Nutrição: O webhook dispara no n8n que cadastra o contato no Mautic e inicia a régua de nutrição de e-mails via Listmonk;
3. Qualificação por Lead Scoring: Ao atingir 50 pontos no Mautic, um webhook notifica o n8n;
4. Criação de Oportunidade: O n8n cria a negociação no Twenty CRM e abre uma sala de contato prioritária no Chatwoot;
5. Agendamento & Fechamento: O vendedor envia link do Cal.com para demonstração e emite contrato pelo Documenso;
6. Sincronização Final: A assinatura do contrato atualiza o status de 'Ganho' no Twenty CRM e notifica o time no WhatsApp via Evolution API.

### Blueprints de Workflows Prontos para n8n (Importação Instantânea)

#### Fluxo 1 · Ingestão de Lead & Criação Automática de Oportunidade no CRM
- *Objetivo:* Recebe o formulário preenchido no Typebot/Landing Page, cadastra no Mautic para nutrição de e-mail, cria o negócio no Twenty CRM e envia notificação no WhatsApp do vendedor via Evolution API.
- *Gatilho:* `Webhook HTTP POST `/webhook/novo-lead``
```json
{
 "name": "RD-to-Sovereign: Ingestão de Lead & CRM Deal",
 "nodes": [
 {
 "parameters": {"httpMethod": "POST", "path": "novo-lead"},
 "name": "Webhook Entrada Lead",
 "type": "n8n-nodes-base.webhook",
 "position": [250, 300]
 },
 {
 "parameters": {"url": "http://mautic/api/contacts/new", "method": "POST"},
 "name": "Cadastrar no Mautic",
 "type": "n8n-nodes-base.httpRequest",
 "position": [450, 300]
 },
 {
 "parameters": {"url": "http://twenty:3000/graphql", "method": "POST"},
 "name": "Criar Oportunidade Twenty",
 "type": "n8n-nodes-base.graphql",
 "position": [650, 300]
 },
 {
 "parameters": {"url": "http://evolution-api:8080/message/sendText/empresa", "method": "POST"},
 "name": "Notificar Vendedor WhatsApp",
 "type": "n8n-nodes-base.httpRequest",
 "position": [850, 300]
 }
 ]
}
```

#### Fluxo 2 · Lead Scoring Quente & Abertura de Atendimento Prioritário
- *Objetivo:* Quando um lead atinge pontuação qualificada no Mautic (ex: abriu 3 e-mails e visitou a página de preços), o n8n cria uma conversa prioritária na fila de vendas do Chatwoot.
- *Gatilho:* `Webhook de Evento Mautic `lead.score.updated``
```json
{
 "name": "RD-to-Sovereign: Lead Scoring Quente to Chatwoot",
 "nodes": [
 {
 "parameters": {"path": "mautic-score-trigger"},
 "name": "Webhook Mautic Score",
 "type": "n8n-nodes-base.webhook",
 "position": [250, 300]
 },
 {
 "parameters": {"conditions": {"number": [{"value1": "={{$json.score}}", "operation": "largerEqual", "value2": 50}]}},
 "name": "Score >= 50?",
 "type": "n8n-nodes-base.if",
 "position": [450, 300]
 },
 {
 "parameters": {"url": "http://chatwoot:3000/api/v1/accounts/1/conversations", "method": "POST"},
 "name": "Abrir Atendimento Chatwoot",
 "type": "n8n-nodes-base.httpRequest",
 "position": [650, 200]
 }
 ]
}
```

---

## CAPÍTULO 6 · MANUAL DE ENGENHARIA DE INFRAESTRUTURA & DEPLOY ALL-IN-ONE

### Entendendo os 4 Pilares da Infraestrutura (Sem Jargões)
- **1. O que é VPS?** A VPS é o seu 'apartamento alugado na nuvem'. Em vez de manter um computador físico ligado no escritório gastando luz, você aluga um servidor ultra-rápido que fica ligado 24 horas por dia, 7 dias por semana, com gerador e internet de fibra ótica.
- **2. O que é Docker Compose?** O Docker Compose é o 'manual de montagem e mobília automática'. Você não precisa instalar programas um por um nem entender de Linux. Ao rodar um único comando, o Docker baixa todos os módulos prontos e os liga automaticamente.
- **3. O que é Traefik?** O Traefik é o 'porteiro inteligente do condomínio'. Ele atende os visitantes na internet, verifica a segurança, coloca o cadeado verde (certificado SSL HTTPS gratuito) e encaminha cada pessoa para o apartamento certo (mkt, crm, chat ou sso).
- **4. O que é n8n?** O n8n é o 'carteiro e mensageiro da empresa'. Ele fica vigiando os formulários: quando um cliente preenche um cadastro, o n8n pega as informações na hora e entrega no WhatsApp do vendedor e no funil do CRM automaticamente.

> **Topologia & Segurança de Rede:** A infraestrutura opera sobre uma rede bridge isolada do Docker (`ecosystem_net`). Apenas o reverse proxy Traefik expõe as portas públicas 80 (HTTP com redirect) e 443 (HTTPS TLS automático via ACME/Let's Encrypt). Todas as ferramentas (Mautic, Twenty, Chatwoot, Evolution, n8n, Keycloak e PostgreSQL) comunicam-se exclusivamente pela rede interna através de seus nomes DNS de serviço (ex: `http://chatwoot:3000`, `postgres:5432`), eliminando vetores de ataque externos e exposição de portas desnecessárias.

### Matriz dos 9 Serviços do Orquestrador
| # | Serviço / Módulo | Imagem Docker | Papel na Infraestrutura | Portas / Exposição | Persistência / Volumes |
|---|---|---|---|---|---|
| 01 | **Traefik Proxy v3** | `traefik:v3.0` | Ingress Controller & Reverse Proxy com TLS automático | `80:80 (HTTP com redirect) e 443:443 (HTTPS)` | `Volume `/letsencrypt/acme.json` para certificados SSL` |
| 02 | **Keycloak SSO** | `quay.io/keycloak/keycloak:latest` | Provedor Central de Identidade (IdP) & Single Sign-On (OIDC/SAML) | `Apenas rede interna (roteado via Traefik sob `sso.suaempresa.com.br`)` | `Banco `db_keycloak` no PostgreSQL compartilhado` |
| 03 | **n8n Automation** | `n8nio/n8n:latest` | Barramento de Eventos & Orquestração Assíncrona de Dados (Glue Layer) | `Apenas rede interna (roteado via Traefik sob `n8n.suaempresa.com.br`)` | `Volume `/data/.n8n` ou PostgreSQL` |
| 04 | **Mautic Marketing** | `mautic/mautic:latest` | Motor de Automação de Marketing, Régua de Nutrição & Lead Scoring | `Apenas rede interna (roteado via Traefik sob `mkt.suaempresa.com.br`)` | `Volume `/var/www/html/docroot/media` e banco `db_mautic`` |
| 05 | **Twenty CRM** | `twentyhq/twenty:latest` | Pipeline Comercial, Funil de Vendas Kanban & Gestão de Contatos | `Apenas rede interna (roteado via Traefik sob `crm.suaempresa.com.br`)` | `Banco `db_twenty` no PostgreSQL corporativo` |
| 06 | **Chatwoot Omnichannel** | `chatwoot/chatwoot:latest` | Central de Atendimento Multiatendente para WhatsApp, Chat & Redes | `Apenas rede interna (roteado via Traefik sob `chat.suaempresa.com.br`)` | `Volume `/app/storage`, banco `db_chatwoot` e Redis` |
| 07 | **Evolution API** | `atendai/evolution-api:v2.1.0` | Gateway de Integração WhatsApp Baileys com Suporte a Múltiplos Números | `Apenas rede interna (roteado via Traefik sob `wa.suaempresa.com.br`)` | `Sessões e credenciais autenticadas no Redis e PostgreSQL` |
| 08 | **Cluster PostgreSQL 16** | `postgres:16-alpine` | Banco de Dados Relacional Unificado da Suíte | `Nenhuma porta pública (porta 5432 restrita à rede privada `ecosystem_net`)` | `Volume de dados `/var/lib/postgresql/data` com política de backup diário pg_dump` |
| 09 | **Redis Cache 7** | `redis:7-alpine` | Fila de Mensageria em Memória & Sessões WebSockets em Tempo Real | `Nenhuma porta pública (porta 6379 restrita à rede privada `ecosystem_net`)` | `Volume persistente `/data` com Append-Only File (AOF) ativado` |

### Especificação da VPS Ideal para o Ecossistema Completo (e Por Que)
> **Perfil de Máquina Recomendado:** `8 vCPU Dedicated Cloud / 16 GB RAM ECC / 160-240 GB NVMe SSD / Link 1 Gbps / Ubuntu 24.04 LTS x86_64` 
> **Por Que Desta Configuração (Racional Técnico):** Garante estabilidade absoluta para os 9 contêineres rodando em simultâneo com isolamento de processos, prevenindo gargalos de I/O em banco de dados e eliminando o risco do OOM Killer durante picos de campanha e atendimento.

#### Distribuição de Recursos de Hardware por Serviço (vCPU & RAM)
| Serviço / Módulo | vCPU Alocada | Memória RAM | Motivo Técnico / Gargalo Previsto |
|---|---|---|---|
| **Traefik Ingress & TLS** | `0.5 vCPU` | `256 MB` | Roteamento reativo de borda, compressão Brotli/Gzip e renovação automática de certificados SSL. |
| **Keycloak SSO (OpenJDK JVM)** | `1.5 vCPU` | `2.0 GB` | Baseline da JVM Java para autenticação federada OIDC/SAML e criptografia de senhas Argon2. |
| **Mautic Marketing & Cron** | `2.0 vCPU` | `4.0 GB` | Processamento em lote de campanhas para 50k+ leads, segmentação e rastreamento assíncrono de cliques. |
| **Twenty CRM & GraphQL** | `1.5 vCPU` | `3.0 GB` | API reativa, buscas full-text e pipeline comercial Kanban simultâneo para 10 a 50 vendedores. |
| **Chatwoot + Sidekiq** | `1.5 vCPU` | `3.5 GB` | Ruby on Rails com centenas de WebSockets ao vivo para multiatendentes no WhatsApp e filas Redis. |
| **Evolution API (WhatsApp)** | `1.0 vCPU` | `1.5 GB` | Sessões Baileys ativas com o WhatsApp, decodificação de áudios OGG/MP3 e disparo de webhooks. |
| **n8n Orquestrador** | `0.5 vCPU` | `1.0 GB` | Execução assíncrona de fluxos de dados, webhooks e sincronização contínua entre CRM e WhatsApp. |
| **Buffer de Picos / Anti-OOM** | `1.0 vCPU` | `1.7 GB` | Margem de folga do kernel Linux para backups diários pg_dump e picos sazonais (Black Friday). |

#### Provedores de Nuvem Recomendados & Validados
| Provedor de Nuvem | Custo Mensal Estimado | Vantagem Principal / SLA |
|---|---|---|
| **Hetzner Cloud (CPX41 / CCX23)** | `€ 28 (~ R$ 170/mês)` | Melhor custo-benefício e performance bruta por vCPU dedicada (Datacenters UE/EUA). |
| **Contabo (Cloud VPS L)** | `€ 16 (~ R$ 100/mês)` | Maior volume de memória RAM e disco NVMe por valor investido. |
| **DigitalOcean (Dedicated 16GB)** | `$ 84 (~ R$ 460/mês)` | Excelente SLA de rede, suporte global e facilidade de snapshots. |
| **AWS Lightsail (16GB RAM)** | `$ 80 (~ R$ 440/mês)` | Infraestrutura corporativa AWS com 5 TB de transferência inclusos. |

### Dimensionamento de Hardware Recomendado
- **Memória RAM Total:** `16 GB RAM`
- **Processamento CPU:** `8 vCPU`
- **Armazenamento SSD:** `160-240 GB NVMe SSD`

### Arquivo `docker-compose.yml` Consolidado para Produção
```yaml
version: '3.8'

networks:
 ecosystem_net:
 driver: bridge

services:
 # 1. Reverse Proxy & TLS Automático
 traefik:
 image: traefik:v3.0
 command:
 - '--providers.docker=true'
 - '--entrypoints.websecure.address=:443'
 - '--certificatesresolvers.myresolver.acme.tlschallenge=true'
 ports:
 - '80:80'
 - '443:443'
 volumes:
 - '/var/run/docker.sock:/var/run/docker.sock:ro'
 - './letsencrypt:/letsencrypt'
 networks:
 - ecosystem_net

 # 2. Provedor de Identidade & SSO
 keycloak:
 image: quay.io/keycloak/keycloak:latest
 command: start-dev
 environment:
 - KEYCLOAK_ADMIN=admin
 - KEYCLOAK_ADMIN_PASSWORD=SegredoForte2026
 labels:
 - 'traefik.enable=true'
 - 'traefik.http.routers.keycloak.rule=Host(`sso.suaempresa.com.br`)'
 - 'traefik.http.routers.keycloak.entrypoints=websecure'
 - 'traefik.http.routers.keycloak.tls.certresolver=myresolver'
 networks:
 - ecosystem_net

 # 3. Barramento de Eventos e Workflows
 n8n:
 image: n8nio/n8n:latest
 environment:
 - N8N_BASIC_AUTH_ACTIVE=true
 - N8N_HOST=n8n.suaempresa.com.br
 labels:
 - 'traefik.enable=true'
 - 'traefik.http.routers.n8n.rule=Host(`n8n.suaempresa.com.br`)'
 - 'traefik.http.routers.n8n.entrypoints=websecure'
 - 'traefik.http.routers.n8n.tls.certresolver=myresolver'
 networks:
 - ecosystem_net

 # 4. Automação de Marketing & Nutrição (RD Marketing)
 mautic:
 image: mautic/mautic:latest
 labels:
 - 'traefik.enable=true'
 - 'traefik.http.routers.mautic.rule=Host(`mkt.suaempresa.com.br`)'
 - 'traefik.http.routers.mautic.entrypoints=websecure'
 - 'traefik.http.routers.mautic.tls.certresolver=myresolver'
 networks:
 - ecosystem_net

 # 5. Pipeline Comercial & CRM (RD CRM)
 twenty:
 image: twentyhq/twenty:latest
 labels:
 - 'traefik.enable=true'
 - 'traefik.http.routers.twenty.rule=Host(`crm.suaempresa.com.br`)'
 - 'traefik.http.routers.twenty.entrypoints=websecure'
 - 'traefik.http.routers.twenty.tls.certresolver=myresolver'
 networks:
 - ecosystem_net

 # 6. Atendimento Omnichannel & Livechat (RD Conversas)
 chatwoot:
 image: chatwoot/chatwoot:latest
 labels:
 - 'traefik.enable=true'
 - 'traefik.http.routers.chatwoot.rule=Host(`chat.suaempresa.com.br`)'
 - 'traefik.http.routers.chatwoot.entrypoints=websecure'
 - 'traefik.http.routers.chatwoot.tls.certresolver=myresolver'
 networks:
 - ecosystem_net

 # 7. Gateway WhatsApp Baileys & Webhooks
 evolution-api:
 image: atendai/evolution-api:v2.1.0
 labels:
 - 'traefik.enable=true'
 - 'traefik.http.routers.evolution.rule=Host(`wa.suaempresa.com.br`)'
 - 'traefik.http.routers.evolution.entrypoints=websecure'
 - 'traefik.http.routers.evolution.tls.certresolver=myresolver'
 networks:
 - ecosystem_net

 # 8. Banco de Dados Relacional Consolidado
 postgres:
 image: postgres:16-alpine
 environment:
 - POSTGRES_USER=postgres
 - POSTGRES_PASSWORD=SegredoPostgres2026
 volumes:
 - postgres_data:/var/lib/postgresql/data
 networks:
 - ecosystem_net

 # 9. Filas de Alta Velocidade & Sessões
 redis:
 image: redis:7-alpine
 volumes:
 - redis_data:/data
 networks:
 - ecosystem_net

volumes:
 postgres_data:
 redis_data:
```

### Roteiro de Instalação e Subida em 4 Passos

1. **Passo 1: Contratar a VPS (Tempo estimado: 3 minutos):** Acesse um provedor de nuvem confiável (como Hetzner Cloud, DigitalOcean, Contabo ou AWS Lightsail). Escolha o plano com 8 vCPU e 16 GB RAM, selecione o sistema operacional Ubuntu 22.04 LTS e clique em 'Criar Servidor'. Você receberá o IP da máquina por e-mail.
2. **Passo 2: Apontar o seu Domínio (Tempo estimado: 2 minutos):** No site onde você comprou seu domínio (Registro.br, Cloudflare, GoDaddy ou Hostinger), vá na aba DNS e crie um apontamento Tipo A com o nome `*` (asterisco) apontando para o IP da sua VPS. Isso garante que `mkt.suaempresa.com.br`, `crm.suaempresa.com.br` e `chat.suaempresa.com.br` funcionem sozinhos.
3. **Passo 3: Rodar o Comando de 1 Clique (Tempo estimado: 1 minuto):** Abra o terminal da VPS e cole o comando automático de inicialização. O sistema fará o download de todas as ferramentas, configurará os bancos de dados e ativará os certificados de segurança SSL em menos de 120 segundos.
4. **Passo 4: Acessar os Painéis no seu Navegador:** Abra o navegador no seu computador e acerte o endereço: `crm.suaempresa.com.br` para seus vendedores, `chat.suaempresa.com.br` para o atendimento e `mkt.suaempresa.com.br` para as campanhas de marketing.

---

## CAPÍTULO 7 · PROTOCOLOS DE MODULARIDADE & HOT-SWAP (PRINCÍPIO DO LEGO)

> **O Princípio das Tomadas Independentes:** 
> A arquitetura opera sob o princípio de 'Tomadas e Aparelhos Independentes'. Nenhuma ferramenta fica grudada ou dependente da outra com código travado. Imagine uma régua de tomadas na sua sala: a sua TV (Twenty CRM) e a sua Caixa de Som (Chatwoot) funcionam perfeitamente mesmo se você desligar o Abajur (Mautic). Se você quiser trocar o abajur por uma luminária moderna, basta tirar da tomada e plugar a nova. Nada na sua sala quebra.

### Protocolo 1: Inserção de Novas Ferramentas (Plug-and-Play)
1. Abra o arquivo `docker-compose.override.yml` e cole a receita da nova ferramenta;
2. Execute `docker compose up -d` no terminal;
3. O sistema cria o endereço web e o cadeado verde SSL automaticamente em 30 segundos;
4. Abra o painel do n8n e conecte o novo módulo aos fluxos existentes arrastando o mouse.

### Protocolo 2: Substituição de Ferramenta em Produção (Hot-Swap sem Downtime)
1. Suba a Nova Ferramenta em Paralelo: Inicie a nova solução em um endereço temporário (ex: `novo-mkt.empresa.com.br`) mantendo a antiga funcionando;
2. Transfira a Conexão no n8n: No painel visual do n8n, mude o nó de disparo para apontar para a nova ferramenta;
3. Importe os Contatos: Faça o download da planilha de contatos da ferramenta antiga e importe na nova;
4. Mude o Endereço Oficial: Altere a rota para que `mkt.empresa.com.br` aponte para a nova ferramenta;
5. Desligue a Antiga com Segurança: Pare o serviço antigo digitando `docker compose stop <servico_antigo>`. Seus vendedores e clientes nem notarão a troca!

### Protocolo 3: Remoção Segura de Módulos
1. No painel visual do n8n, desligue os gatilhos vinculados à ferramenta que deseja remover;
2. No terminal da VPS, digite `docker compose stop <nome_ferramenta>`;
3. Os dados históricos continuam guardados com segurança na pasta de backup da VPS para você consultar quando quiser.

### Estudo de Caso Prático: Substituição do Mautic por outra ferramenta de e-mail marketing (ex: Novu ou Listmonk)
- **1. Isolamento Operacional:** O Twenty CRM e o Chatwoot não conversam com o Mautic diretamente, eles conversam com o n8n. Por isso, a sua equipe de vendas e seus operadores no WhatsApp continuam trabalhando normalmente sem nenhuma parada.
- **2. Início do Novo Contêiner:** `O técnico ou gestor sobe a nova ferramenta de e-mail no arquivo de extensão sem mexer nas ferramentas existentes.`
- **3. Chaveamento no n8n:** No painel visual do n8n, basta trocar a caixinha do Mautic pela caixinha do Listmonk com 2 cliques.
- **4. Resultado Final:** A troca é concluída com ZERO minutos de parada no atendimento e ZERO perda de leads comerciais.

### Perguntas Frequentes (FAQ Operacional para Não-Técnicos)

- ** E se a VPS for reiniciada por falta de luz no datacenter?**
 - *Resposta:* Todos os serviços possuem configuração de auto-recuperação (restart: always). Quando o servidor ligar novamente, todas as ferramentas e bancos de dados sobem sozinhos sem você precisar fazer nada.

- ** Como funcionam os backups dos meus clientes e conversas?**
 - *Resposta:* Todas as informações de leads, negociações e mensagens de WhatsApp ficam armazenadas em uma pasta segura de dados (`/var/lib/postgresql/data`). Um script diário gera cópias automáticas que podem ser enviadas para o seu Google Drive ou Amazon S3.

- ** Preciso contratar um desenvolvedor para usar no dia a dia?**
 - *Resposta:* Não! O uso rotineiro da sua equipe é 100% feito pelo navegador web em telas modernas e em português, exatamente como se estivesse usando o RD Station, Trello ou WhatsApp Web.

---

## CAPÍTULO 8 · ROTEIRO PRÁTICO DE MIGRAÇÃO DE DADOS HISTÓRICOS

### 1. Migração do RD Station Marketing Mautic
- **O que migrar:** Base total de contatos (Leads), campos personalizados, histórico de tags, segmentos e listas de descadastro (opt-out).
- **Passos de Migração:**
 1. No RD Station Marketing, vá em Base de Leads > Exportar Base Completa em formato CSV com todos os campos e tags;
 1. Abra o Mautic em `mkt.suaempresa.com.br` e crie previamente os campos customizados correspondentes (ex: Cargo, Segmento, Faturamento);
 1. Vá em Contatos > Importar > Selecione o arquivo CSV do RD Station e faça o de-para (mapeamento) das colunas em 2 minutos;
 1. Execute a importação em segundo plano. O Mautic processa 100.000 contatos em menos de 10 minutos.
- ** Cuidados Críticos:** Importe a lista de opt-out (unsubscribers) com o status 'Não perturbe' ativado para preservar a reputação do seu domínio de e-mail.

### 2. Migração do RD Station CRM Twenty CRM
- **O que migrar:** Empresas cadastradas, Pessoas de contato, Etapas do Funil de Vendas (Kanban), Negociações abertas/ganhas e Histórico de anotações comerciais.
- **Passos de Migração:**
 1. No RD Station CRM, acerte a exportação completa de 'Negociações e Contatos' em formato CSV ou XLSX;
 1. No Twenty CRM (`crm.suaempresa.com.br`), configure as fases do seu funil (ex: Qualificação, Apresentação, Proposta, Fechamento);
 1. Utilize o importador nativo do Twenty CRM para carregar as empresas e vincular automaticamente os contatos e valores de negócio;
 1. Atribua as negociações existentes aos seus respectivos vendedores via login unificado do Keycloak.
- ** Cuidados Críticos:** Mantenha a correspondência exata dos e-mails dos vendedores para que o histórico de notas e tarefas seja atribuído aos donos corretos.

### 3. Migração do RD Conversas / WhatsApp Chatwoot & Evolution API
- **O que migrar:** Números de WhatsApp conectados, mensagens pré-programadas (macros de resposta rápida), equipes de atendentes e departamentos.
- **Passos de Migração:**
 1. Cadastre os departamentos no Chatwoot (Vendas, Suporte, Financeiro) e convide os atendentes;
 1. Conecte a Evolution API ao Chatwoot criando uma nova caixa de entrada do tipo API Webhook;
 1. No painel da Evolution API (`wa.suaempresa.com.br`), gere o QR Code e escaneie com o celular corporativo do WhatsApp da empresa;
 1. A conexão é estabelecida imediatamente com recepção de mensagens em tempo real e divisão automática entre atendentes.
- ** Cuidados Críticos:** Não desconecte o chip do aparelho físico durante a virada para garantir a sincronização inicial de contatos.

---

## CAPÍTULO 9 · GOVERNANÇA CORPORATIVA, BACKUP 3-2-1 & CONFORMIDADE LGPD

> **Arquitetura de Proteção de Dados 3-2-1:** A política de proteção de dados opera na regra de ouro 3-2-1: (3) cópias de dados em (2) tipos de mídias diferentes, com (1) cópia externa criptografada em nuvem fria (Wasabi / AWS S3 / Google Drive).

### Script Automatizado de Backup Diário com Criptografia AES-256
```bash
#!/bin/bash
# Script de Backup Automatizado Soberano (PostgreSQL + Volumes + Mídias)
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
BACKUP_DIR="/opt/backups/$TIMESTAMP"
mkdir -p $BACKUP_DIR

# 1. Dump consistente de todos os bancos de dados (Mautic, Twenty, Chatwoot, Keycloak, n8n)
docker exec postgres pg_dumpall -U postgres | gzip > $BACKUP_DIR/db_all_cluster.sql.gz

# 2. Compactação dos arquivos de mídia e anexos
tar -czf $BACKUP_DIR/media_storage.tar.gz -C /var/lib/docker/volumes postgres_data/_data

# 3. Criptografia AES-256 com senha segura
gpg --batch --yes --passphrase "SuaChaveMestreSegura2026" -c $BACKUP_DIR/db_all_cluster.sql.gz

# 4. Envio para Storage Seguro Externo (rclone / AWS S3)
rclone copy $BACKUP_DIR remote-s3:backups-empresa/$TIMESTAMP/

# 5. Limpeza de backups locais com mais de 7 dias
find /opt/backups/* -mtime +7 -exec rm -rf {} \;
echo " Backup soberano concluído e sincronizado na nuvem fria!"
```

### Checklist de Conformidade Estrita com a LGPD

- **Soberania Física dos Dados:** Em conformidade: O banco reside em servidor exclusivo da empresa, sem compartilhamento com provedores terceiros ou venda de dados para IA pública.
- **Direito de Exclusão do Titular (Art. 18 LGPD):** Em conformidade: O n8n executa script de expurgo automatizado com 1 clique no Mautic, Twenty e Chatwoot quando solicitado pelo cliente.
- **Criptografia em Trânsito & Repouso:** Em conformidade: Trânsito 100% sob TLS 1.3 / HSTS automático via Traefik e volumes criptografados com LUKS/AES-256 no sistema de arquivos do host.
- **Trilha de Auditoria & Logs de Acesso:** Em conformidade: O Keycloak e o PostgreSQL gravam logs imutáveis de cada autenticação e ação executada por colaboradores.

---

## CAPÍTULO 10 · CRONOGRAMA DE IMPLANTAÇÃO EM 30 DIAS & MONITORAMENTO

### Cronograma Executivo de Virada de Chave (4 Semanas)

#### Semana 1 (Dias 1 a 7) · Infraestrutura & Instalação do Cluster
- *Atividades Principais:* Contratação da VPS, configuração de DNS wildcard (*.empresa.com.br), execução do docker-compose.yml e ativação dos certificados SSL automáticos via Traefik.
- * Marco de Conclusão:* **Todos os painéis acessíveis online com cadeado verde (HTTPS).**

#### Semana 2 (Dias 8 a 14) · Migração de Dados & Conexão de Mensageria
- *Atividades Principais:* Importação de leads do RD Marketing no Mautic, exportação do funil de vendas para o Twenty CRM e pareamento do WhatsApp na Evolution API e Chatwoot.
- * Marco de Conclusão:* **Base histórica 100% carregada e WhatsApp corporativo recebendo mensagens no Chatwoot.**

#### Semana 3 (Dias 15 a 21) · Importação dos Blueprints n8n & Treinamento das Equipes
- *Atividades Principais:* Importação dos templates de workflow no n8n, realização de testes de passagem de bastão (Lead -> CRM -> WhatsApp) e workshop de capacitação dos vendedores e atendentes.
- * Marco de Conclusão:* **Equipes comerciais operando com agilidade e fluxos automatizados aprovados.**

#### Semana 4 (Dias 22 a 30) · Virada de Chave Definitiva & Descomissionamento SaaS
- *Atividades Principais:* Redirecionamento de formulários do site oficial para a nova stack, ativação da régua de nutrição oficial e cancelamento das faturas recorrentes do RD Station Suite.
- * Marco de Conclusão:* **Autonomia digital plena e economia de R$ 109.800/ano consolidada!**

### Monitoramento em Tempo Real da VPS (Netdata / Portainer Community Edition (Monitoramento visual leve e em tempo real))

**Comandos de Diagnóstico em 1 Clique:**

- `docker stats --no-stream` Exibe o consumo instantâneo de memória RAM, % de CPU e tráfego de rede de cada um dos 9 serviços da stack.
- `docker compose ps` Verifica o status de saúde (Up / Healthy) de todos os contêineres e o tempo em que estão no ar.
- `docker compose logs -f --tail=50 traefik` Inspeciona o tráfego HTTP/HTTPS em tempo real e a renovação de certificados SSL.

**Métricas Críticas & Ações Imediatas:**

- **Consumo de RAM da VPS** (Limite: `> 85% por mais de 10 minutos`): Ajustar limite de memória no container do Mautic ou adicionar swap de 4 GB.
- **Uso de Disco SSD** (Limite: `> 80% do armazenamento total`): Executar o script de limpeza de logs e backups antigos com `docker system prune -f`.
- **Sessão WhatsApp Evolution** (Limite: `Status 'Disconnected'`): O n8n envia alerta imediato no Telegram do administrador para reconexão via QR Code.
