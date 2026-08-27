# Dossiê Vertical de Desmantelamento SaaS: Twilio (CPaaS & Communications API)

> **Padrão Diamante R5-V · Quinteto Soberano Open Source**  
> **Alvo SaaS:** Twilio (CPaaS & Communications API) | **Custo Médio:** R$ 60.000 a R$ 300.000/ano (cobrança por mensagem WhatsApp, tarifação por minuto de voz SIP, taxas de números virtuais e custos de egress) | **Risco de Privacidade:** Metadados de chamadas, transcrições de voz, tokens de autenticação (2FA) e histórico completo de mensagens de clientes retidos e processados em nuvem de terceiros nos EUA.  

---

## 1. O Quinteto Soberano Open Source

| Rank | Classificação | Ferramenta | Licença | Repositório | Economia Estimada |
| :---: | :--- | :--- | :---: | :--- | :--- |
| **#1** | *A Mais Robusta* | **WAHA (WhatsApp HTTP API)** | `Apache-2.0` | [https://github.com/devlikeapro/waha](https://github.com/devlikeapro/waha) | R$ 120.000/ano |
| **#2** | *A Mais Completa* | **Asterisk (The Open Source PBX Engine)** | `GPL-2.0` | [https://github.com/asterisk/asterisk](https://github.com/asterisk/asterisk) | R$ 200.000/ano |
| **#3** | *A Mais Moderna* | **Kamailio (Carrier-Grade SIP Router)** | `GPL-2.0` | [https://github.com/kamailio/kamailio](https://github.com/kamailio/kamailio) | R$ 180.000/ano |
| **#4** | *A Mais Leve* | **Gotify (Self-Hosted Push Notification Server)** | `MIT` | [https://github.com/gotify/server](https://github.com/gotify/server) | R$ 36.000/ano |
| **#5** | *A Mais Simples* | **MailHog (Super-Simple SMTP Testing & Gateway)** | `MIT` | [https://github.com/mailhog/MailHog](https://github.com/mailhog/MailHog) | R$ 12.000/ano |

---

## 2. Detalhamento Técnico das Ferramentas do Quinteto

### #1 · WAHA (WhatsApp HTTP API) (*A Mais Robusta*)

- **O Que Faz:** Gateway HTTP REST completo para WhatsApp com suporte a múltiplas sessões, envio e recebimento de mensagens com texto, mídias, áudios (PTT), botões, localização e contatos via OpenAPI/Swagger e Webhooks em tempo real.
- **Como Funciona:** Desenvolvido em Node.js/TypeScript com motores WhatsApp Web (NOWEB / GOWS), arquitetura modular em contêiner Docker pronto para produção, documentação interativa Swagger e autenticação segura via API Key.
- **Requisitos de Infra:** 1 GB RAM, 1 vCPU
- **Comando Rápido:** `docker run -d -p 3000:3000 --name waha -e WHATSAPP_API_KEY=secreta -v waha_sessions:/app/.sessions devlikeapro/waha:latest`
- **White-Label & Design System:** Esforço `Baixo` (Swagger UI / OpenAPI Web) - Customização visual do Dashboard via CSS injection e parametrização de endpoints no proxy reverso Caddy.

**Uso Complementar & Ecossistema Agêntico:**
- **Servidor MCP:** `mcp-waha-gateway` (`npx -y @devlikeapro/mcp-waha`) - Permite que agentes autônomos e LLMs enviem mensagens e monitorem filas de atendimento no WhatsApp diretamente via Tool Calling.
- **Agent Skill:** `whatsapp-campaign-manager` (`.agents/skills/whatsapp-campaign-manager`) - Skill de orquestração de disparos em lote com controle dinâmico de cadência (delay) anti-bloqueio.

### #2 · Asterisk (The Open Source PBX Engine) (*A Mais Completa*)

- **O Que Faz:** Plataforma de telefonia IP e PBX corporativo mais consagrada do planeta: gerencia centrais telefônicas completas, URA interativa (IVR), gravação de chamadas, conferências de voz, correio de voz e troncos SIP com operadoras VoIP.
- **Como Funciona:** Desenvolvido em C de altíssimo desempenho com módulos para chan_pjsip, dialplan configurável em extensions.conf e suporte a ARI (Asterisk REST Interface) para controle agêntico de chamadas por software.
- **Requisitos de Infra:** 2 GB RAM, 2 vCPUs
- **Comando Rápido:** `docker run -d --net=host --name asterisk -v /etc/asterisk:/etc/asterisk andrius/asterisk:20`
- **White-Label & Design System:** Esforço `Médio` (FreePBX / WebRTC Softphone UI) - Integração com interfaces web como FreePBX ou painéis de chamadas em Vue/React via ARI WebSockets.

**Uso Complementar & Ecossistema Agêntico:**
- **Servidor MCP:** `mcp-asterisk-ari` (`pip install mcp-asterisk-telecom`) - Permite que assistentes de voz com IA atendam ramais telefônicos e consultem bancos de dados em tempo real durante a chamada.
- **Plugin:** `webrtc-softphone-embed` (`npm install @asterisk/webrtc-phone`) - Widget de telefone no navegador integrado diretamente ao CRM e Helpdesk da empresa.

### #3 · Kamailio (Carrier-Grade SIP Router) (*A Mais Moderna*)

- **O Que Faz:** Roteador SIP de alta performance capaz de processar milhares de chamadas por segundo (CPS), atuando como Session Border Controller (SBC), balanceador de carga VoIP, proxy de segurança e registrador SIP de missão crítica.
- **Como Funciona:** Arquitetura assíncrona em C ultra-otimizada para throughput massivo de telecomunicações, com suporte a Lua, Python, Redis e TLS criptografado para chamadas seguras.
- **Requisitos de Infra:** 1 GB RAM, 2 vCPUs
- **Comando Rápido:** `docker run -d --net=host --name kamailio -v /etc/kamailio:/etc/kamailio kamailio/kamailio:5.7-alpine`
- **White-Label & Design System:** Esforço `Baixo` (Siremis Web Management Portal) - Painel de controle Siremis com interface PHP/HTML para gestão de regras de roteamento e faturamento de telecom.

**Uso Complementar & Ecossistema Agêntico:**
- **Servidor MCP:** `mcp-kamailio-telemetry` (`pip install mcp-kamailio-ops`) - Auditoria e monitoramento em tempo real de tráfego SIP, jitter, perda de pacotes e qualidade de áudio (MOS).

### #4 · Gotify (Self-Hosted Push Notification Server) (*A Mais Leve*)

- **O Que Faz:** Servidor ultraleve de envio e recebimento de notificações push em tempo real via WebSocket e HTTP REST API, com clientes nativos para Android, Web UI e CLI.
- **Como Funciona:** Escrito em Go puro compilado em binário único sem dependências externas, consome menos de 30 MB de RAM e entrega notificações com latência inferior a 50 milissegundos.
- **Requisitos de Infra:** 256 MB RAM, 0.5 vCPU
- **Comando Rápido:** `docker run -d -p 8080:80 -v gotify_data:/app/data --name gotify gotify/server:latest`
- **White-Label & Design System:** Esforço `Mínimo` (React / Tailwind Clean UI) - Interface minimalista moderna com tema escuro nativo e suporte a ícones customizados por aplicação.

**Uso Complementar & Ecossistema Agêntico:**
- **Servidor MCP:** `mcp-gotify-notifier` (`npx -y @gotify/mcp-notifier`) - Permite que agentes IA notifiquem o operador humano no celular em caso de alertas críticos ou solicitação de aprovação.

### #5 · MailHog (Super-Simple SMTP Testing & Gateway) (*A Mais Simples*)

- **O Que Faz:** Servidor SMTP e Webmail completo para captura, inspeção e teste de emails transacionais em ambientes de desenvolvimento e homologação sem risco de disparo acidental para clientes reais.
- **Como Funciona:** Desenvolvido em Go com servidor SMTP na porta 1025 e interface web completa na porta 8025, fornecendo API REST para asserções automatizadas em pipelines de teste e CI/CD.
- **Requisitos de Infra:** 128 MB RAM, 0.5 vCPU
- **Comando Rápido:** `docker run -d -p 1025:1025 -p 8025:8025 --name mailhog mailhog/mailhog`
- **White-Label & Design System:** Esforço `Mínimo` (AngularJS / Bootstrap Webmail) - Interface limpa inspirada em webmails clássicos sem necessidade de customização.

**Uso Complementar & Ecossistema Agêntico:**
- **Plugin:** `mailhog-cypress-testing` (`npm install cypress-mailhog`) - Validação automática em testes E2E do recebimento de emails de verificação e redefinição de senha.

---

## 3. Matriz de Decisão & Migração Soberana

Para substituir integralmente o **Twilio (CPaaS & Communications API)**, recomenda-se a esteira automatizada de implantação em VPS com os manuais operacionais disponíveis em `output/`.