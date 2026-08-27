# Trilha Cronológica de Aprendizado: WAHA (WhatsApp HTTP API Gateway)

> **Jornada Pedagógica Autoguiada · Imersão a Partir das Fontes Primárias**  
> **Tempo Total Estimado:** 8 horas de imersão guiada | **Fases:** 5 Módulos  
> **Dossiê SaaS de Origem:** Twilio

---

## Fase 1: Fundamentos de APIs REST & WebSockets no WhatsApp (`⏱️ 1h 30min`)
**🎯 Meta da Etapa:** Entender os princípios de comunicação cliente-servidor entre WhatsApp Web e WAHA, diferenças entre REST e WebSocket e por que WAHA supera Twilio em flexibilidade.

- [ ] **[WAHA Official Architecture & API Documentation](https://github.com/devlikeapro/waha)** (`Documentação Oficial` - `[F01]`)
  - 💡 **O que você aprende:** Endpoints REST (sendText, getMessage), Webhooks e autenticação stateless.
  - ⏱️ 45 min | 👤 DevLike ApPro (WAHA Core Team)

- [ ] **[WhatsApp Web Protocol & Security](https://github.com/adiwajshing/Baileys)** (`Artigo Técnico` - `[F02]`)
  - 💡 **O que você aprende:** Diferença entre WhatsApp Web (WAHA) vs. API Oficial (Twilio) em segurança e privacidade.
  - ⏱️ 45 min | 👤 Adiwajshing (Baileys Creator)

## Fase 2: Instalação de WAHA em Localhost & Primeiro Deploy (`⏱️ 2h 00min`)
**🎯 Meta da Etapa:** Setup de ambiente de desenvolvimento local com Docker, pareamento da sessão e envio de primeiras mensagens.

- [ ] **[WAHA Quick Start Guide](https://docs.waha.dev/en/guide/deploy/docker.html)** (`Tutorial Prático` - `[F03]`)
  - 💡 **O que você aprende:** Docker pull, docker run, QR Code scanning e dashboard inicial.
  - ⏱️ 30 min de video + 1h prática | 👤 WAHA Documentation

- [ ] **[REST API Playground (Postman/Swagger)](https://docs.waha.dev/en/swagger/)** (`Lab Interativo` - `[F04]`)
  - 💡 **O que você aprende:** Disparar requisições POST /api/sendText e GET /api/me com curl/Postman.
  - ⏱️ 1h prática | 👤 WAHA Team

## Fase 3: Webhooks, Callbacks & Estrutura de Eventos (`⏱️ 2h 00min`)
**🎯 Meta da Etapa:** Integrar backend para receber webhooks, processar eventos de entrega e construir lógica de resposta automática.

- [ ] **[WAHA Webhooks & Events Deep Dive](https://docs.waha.dev/en/guide/webhooks/)** (`Documentação Oficial` - `[F05]`)
  - 💡 **O que você aprende:** Tipos de webhook (message.created, message.updated, message.status), payloads JSON e retry policies.
  - ⏱️ 1h | 👤 WAHA Docs

- [ ] **[Building a Simple Bot with WAHA + Express.js](https://github.com/devlikeapro/waha-examples)** (`Hands-on Lab` - `[F06]`)
  - 💡 **O que você aprende:** Criar endpoint POST /webhook que recebe mensagens, processa e responde automaticamente.
  - ⏱️ 1h prática | 👤 WAHA Community

## Fase 4: Segurança, Taxa & Escala em Produção (`⏱️ 1h 30min`)
**🎯 Meta da Etapa:** Implementar rate limiting, autenticação com API Keys, monitoramento e preparar a infraestrutura para escala.

- [ ] **[Security Best Practices for WhatsApp APIs](https://github.com/devlikeapro/waha#security)** (`Guia de Segurança` - `[F07]`)
  - 💡 **O que você aprende:** API Key management, TLS/HTTPS, validação de webhooks com HMAC e proteção contra replay attacks.
  - ⏱️ 45 min | 👤 WAHA Team

- [ ] **[Scaling WAHA with Kubernetes & Load Balancing](https://docs.waha.dev/en/guide/deploy/kubernetes.html)** (`Arquitetura Técnica` - `[F08]`)
  - 💡 **O que você aprende:** Multiple WAHA instances com Redis shared sessions, Ingress controller e health checks.
  - ⏱️ 45 min | 👤 WAHA DevOps

## Fase 5: Migração de Twilio para WAHA & Go-Live (`⏱️ 1h 00min`)
**🎯 Meta da Etapa:** Executar plano de migração zero-downtime, validar compatibilidade de APIs, desligar Twilio e monitorar.

- [ ] **[Migração do Twilio para WAHA - Guia Prático](file:///opt/waha/desinstalacao_cirurgica.md)** (`Playbook de Migração` - `[F09]`)
  - 💡 **O que você aprende:** Passos de blue-green deploy, validação de webhooks e monitoramento pós-migração.
  - ⏱️ 30 min leitura | 👤 AIDD - Arsenal Open Source

- [ ] **[Monitoramento & Alertas com Prometheus + Grafana](https://github.com/devlikeapro/waha/blob/main/docker-compose.monitoring.yml)** (`Tutorial de Observabilidade` - `[F10]`)
  - 💡 **O que você aprende:** Configurar dashboards Grafana para Taxa de Entrega, Latência de Webhooks e Uptime.
  - ⏱️ 30 min | 👤 WAHA Community
