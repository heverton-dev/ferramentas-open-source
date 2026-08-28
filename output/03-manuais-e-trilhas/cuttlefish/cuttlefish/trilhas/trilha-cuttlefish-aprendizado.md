# Trilha Cronológica de Aprendizado: Postal

> **Jornada Pedagógica Autoguiada · Imersão a Partir das Fontes Primárias** 
> **Tempo Total Estimado:** 10 horas de imersão guiada (No seu próprio ritmo) | **Fases:** 5 Módulos 
> **Dossiê SaaS de Origem:** Cuttlefish

---

## Fase 1: Conceito de Email Transacional, Privacidade & Soberania (Brasil First) (`⏱ 1h 30min`)
** Meta da Etapa:** Entender por que empresas brasileiras precisam de infraestrutura de email transacional soberana, diferenças entre SaaS como Cuttlefish e soluções self-hosted como Postal, e conformidade com LGPD.

- [ ] **[Diferenças entre Email Transacional e Marketing](https://dev.to/t/email-infrastructure)** (`Artigo Técnico / Guia Conceitual` - `[F01]`)
 - **O que você aprende:** Por que emails críticos (reset de senha, confirmação de pagamento) exigem infraestrutura dedicada diferente de campanhas de marketing.
 - ⏱ 25 min de leitura | Comunidade Brasileira de DevOps & Email Seguro

- [ ] **[LGPD e Armazenamento de Dados de Email em Servidores Estrangeiros](https://www.gov.br/cidadania/pt-br/acesso-a-informacao/lgpd)** (`Guia Legal & Técnico` - `[F05]`)
 - **O que você aprende:** Riscos legais de armazenar metadados de transações (confirmação de pagamento, reset de senha) em datacenters de terceiros sujeitos a regulações estrangeiras.
 - ⏱ 30 min de leitura | Instituto de Tecnologia do Brasil (ABNT/LGPD)

- [ ] **[Arquitetura de Email Transacional: Filas, Webhooks e Entrega Garantida](https://github.com/postalserver/postal/wiki/Architecture)** (`Documentação Técnica` - `[F02]`)
 - **O que você aprende:** Como Postal usa PostgreSQL para persistência de mensagens, Redis para fila de trabalho (Sidekiq) e webhooks para notificar eventos de entrega.
 - ⏱ 35 min de leitura assistida | Postal Oficial & Comunidade Rails

## Fase 2: Infraestrutura VPS, Docker & Primeiro Deploy de Postal (`⏱ 2h 30min`)
** Meta da Etapa:** Provisionar VPS em Hetzner/Contabo, instalar Docker, configurar firewall e colocar Postal no ar pela primeira vez.

- [ ] **[Como Alugar VPS e Configurar SSH (Guia para Leigos)](https://www.youtube.com/@LinuxTips)** (`Tutorial Prático / Screencast` - `[F01]`)
 - **O que você aprende:** Criar conta Hetzner, provisionar VPS Ubuntu 24.04 LTS CPX31, copiar IP, abrir PowerShell/Terminal e conectar via SSH.
 - ⏱ 45 min de estudo + prática | Comunidade DevOps Brasil

- [ ] **[Hardening Inicial de VPS com Firewall (UFW)](https://www.digitalocean.com/community/tutorials/ufw-essentials-common-firewall-rules-and-commands)** (`Guia de Segurança` - `[F05]`)
 - **O que você aprende:** Configurar firewall UFW: negar tudo por padrão, permitir SSH, HTTP, HTTPS. Ativar com --force enable.
 - ⏱ 30 min de prática | DigitalOcean Community

- [ ] **[Instalação de Docker & Docker Compose em Ubuntu 24.04](https://docs.docker.com/engine/install/ubuntu/)** (`Tutorial Oficial` - `[F02]`)
 - **O que você aprende:** Instalar Docker engine via repositório oficial, adicionar usuário deployer ao grupo docker, validar com docker --version.
 - ⏱ 45 min de instalação | Docker Official Docs

- [ ] **[Deploy de Postal com Docker Compose (Passo a Passo)](file:///opt/postal/instalacao_producao.md)** (`Guia Prático / Manual Operacional` - `[F03]`)
 - **O que você aprende:** Clonar docker-compose.yml, configurar variáveis de ambiente, executar docker compose up -d, validar containers com docker compose ps.
 - ⏱ 1h de prática | AIDD - Fábrica Universal

## Fase 3: Configuração de Domínios, DKIM/SPF/DMARC e Primeiros Envios (`⏱ 2h 00min`)
** Meta da Etapa:** Registrar domínios corporativos no Postal, configurar registros de segurança DNS e enviar emails de teste.

- [ ] **[DNS, DKIM, SPF e DMARC Explicados para Não-Técnicos](https://dev.to/t/email-security)** (`Artigo Técnico Acessível` - `[F04]`)
 - **O que você aprende:** DKIM = assinatura digital, SPF = autoriza quem pode enviar, DMARC = política de autenticação. Por que Gmail rejeita emails sem esses registros.
 - ⏱ 40 min de leitura | Comunidade de Email Security

- [ ] **[Registrar Domínio e Configurar Registros DNS no Postal](file:///opt/postal/primeiros_domínios.md)** (`Tutorial Prático` - `[F01]`)
 - **O que você aprende:** Acessar painel Postal, clicar 'Add Domain', copiar registros DKIM/SPF/DMARC, colar no provedor de DNS, aguardar propagação, clicar 'Verify'.
 - ⏱ 45 min de prática | AIDD - Fábrica Universal

- [ ] **[Teste de Entrega com Curl & Verificação em Gmail/Outlook](file:///opt/postal/teste_entrega_api.md)** (`Lab Interativo` - `[F02]`)
 - **O que você aprende:** Gerar token de API, disparar POST /api/v1/send via curl, validar que email chega em caixa de entrada (não spam) em 5-10 segundos.
 - ⏱ 35 min de prática | Postal Community

## Fase 4: Webhooks, Fila de Trabalho (Sidekiq/Redis) e Monitoramento (`⏱ 2h 30min`)
** Meta da Etapa:** Configurar webhooks para notificação de entrega/bounce, monitorar fila Redis, entender Sidekiq e implementar alertas básicos.

- [ ] **[Webhooks & Eventos de Entrega em Tempo Real](https://docs.postal.io/api/webhooks/)** (`Documentação Oficial` - `[F05]`)
 - **O que você aprende:** Tipos de webhook (message.delivered, message.bounced, message.blocked), payload JSON, retry automático, assinatura HMAC para validação.
 - ⏱ 50 min | Postal Official Docs

- [ ] **[Monitoramento de Fila Redis/Sidekiq & Troubleshooting](https://github.com/sidekiq/sidekiq/wiki/)** (`Guia Prático` - `[F03]`)
 - **O que você aprende:** Acessar Redis CLI, inspecionar tamanho da fila (DBSIZE), ver jobs em processamento, identificar deadlocks.
 - ⏱ 1h de prática | Sidekiq Official & Redis Community

- [ ] **[Construir Endpoint de Webhook em Node.js/Python](https://github.com/postalserver/postal-examples)** (`Hands-on Lab` - `[F04]`)
 - **O que você aprende:** Criar rota POST /webhooks, validar signature HMAC, registrar em banco de dados, atualizar status de usuário.
 - ⏱ 40 min de codificação | Dev Community

## Fase 5: Migração de Cuttlefish para Postal & Go-Live em Produção (`⏱ 1h 30min`)
** Meta da Etapa:** Executar plano de migração zero-downtime de Cuttlefish SaaS para Postal self-hosted, validar equivalência de APIs e monitorar primeiras horas de produção.

- [ ] **[Playbook de Migração Cuttlefish → Postal (Blue-Green Deploy)](file:///opt/postal/playbook_migracao.md)** (`Playbook de Engenharia` - `[F09]`)
 - **O que você aprende:** Estratégia blue-green: manter Cuttlefish ativo enquanto valida Postal, switch de tráfego apenas quando 100% de confiança, rollback rápido se algo falhar.
 - ⏱ 30 min de leitura | AIDD - Arsenal Open Source

- [ ] **[Migração de Templates de Email & Conversão para MJML](https://mjml.io/documentation)** (`Guia Técnico` - `[F06]`)
 - **O que você aprende:** MJML é mais simples que HTML puro. Postal renderiza automaticamente. Migrar templates existentes é procedimento mecânico.
 - ⏱ 25 min | MJML Community

- [ ] **[Observabilidade & Monitoramento em Produção (Prometheus + Grafana)](https://github.com/postalserver/postal/discussions/monitoring)** (`Tutorial de Observabilidade` - `[F10]`)
 - **O que você aprende:** Coletar métricas de entrega, taxa de erro, latência de webhook, uptime de banco de dados. Configurar alertas para anomalias.
 - ⏱ 35 min | Postal Community & Prometheus Docs
