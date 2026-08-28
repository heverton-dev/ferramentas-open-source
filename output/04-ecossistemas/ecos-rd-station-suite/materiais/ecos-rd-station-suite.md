# Macro-Ecossistema RD Station: Marketing, CRM & Conversas

> **Macro-Ecossistema Soberano · Desmantelamento RD Station Suite · Padrão Diamante R5-E**  
> Dossiê completo de substituição soberana para o Macro-Ecossistema RD Station (Marketing, CRM, Conversas/WhatsApp, Formulários e Automações), integrando ferramentas líderes por pilar através de autenticação única (Keycloak SSO), barramento de dados assíncrono (n8n) e proxy seguro (Traefik).

---

## 1. Visão Executiva & TCO Global

- **Macro-SaaS Substituído:** RD Station Suite (Marketing Pro + CRM Pro + Conversas Enterprise + Zapier)
- **Custo SaaS Estimado:** R$ 114.000/ano (RD Marketing Pro R$ 42k + RD CRM 15 usuários R$ 36k + RD Conversas 10 atendentes R$ 36k)
- **Custo da Infraestrutura Soberana:** R$ 4.200/ano (VPS 8 vCPU / 16 GB RAM a R$ 350/mês)
- **Economia Líquida Anual:** R$ 109.800/ano (Economia de 96.3%)
- **Payback Estimado:** Payback positivo em apenas 14 dias de operação unificada.

---

## 2. Pilares Funcionais do Ecossistema

### Pilar 1: Marketing, Nutrição & Landing Pages
**Módulo SaaS Alvo:** `RD Station Marketing (Pro/Enterprise)`  
*Responsável por captura de leads, criação de landing pages dinâmicas, disparos de e-mail marketing em alta escala, automação de fluxos de nutrição e cálculo de lead scoring.*

| # | Ferramenta | Papel no Pilar | Licença | Repositório GitHub |
| :---: | :--- | :--- | :---: | :--- |
| 1 | **Mautic** | Motor central de automação de marketing, segmentação dinâmica e pontuação de leads. | `GPL-3.0` | [https://github.com/mautic/mautic](https://github.com/mautic/mautic) |
| 2 | **Listmonk** | Entrega de e-mails em massa e newsletters com custo quase nulo via Amazon SES. | `AGPL-3.0` | [https://github.com/knadh/listmonk](https://github.com/knadh/listmonk) |
| 3 | **Directus** | Gestão autônoma de conteúdo das landing pages e portais corporativos sem depender de desenvolvedores. | `GPL-3.0` | [https://github.com/directus/directus](https://github.com/directus/directus) |

### Pilar 2: Pipeline de Vendas, CRM & Fechamento
**Módulo SaaS Alvo:** `RD Station CRM (Avançado)`  
*Responsável pela gestão de oportunidades comerciais em formato Kanban, distribuição de leads para vendedores, agendamento de reuniões e assinatura digital de contratos.*

| # | Ferramenta | Papel no Pilar | Licença | Repositório GitHub |
| :---: | :--- | :--- | :---: | :--- |
| 1 | **Twenty** | Interface principal dos vendedores para acompanhamento de negócios, tarefas e histórico de contatos. | `AGPL-3.0` | [https://github.com/twentyhq/twenty](https://github.com/twentyhq/twenty) |
| 2 | **Cal.com** | Elimina a fricção na marcação de reuniões de qualificação e fechamento com clientes. | `AGPL-3.0` | [https://github.com/calcom/cal.com](https://github.com/calcom/cal.com) |
| 3 | **Documenso** | Formalização jurídica de propostas comerciais e contratos sem custo por documento. | `AGPL-3.0` | [https://github.com/documenso/documenso](https://github.com/documenso/documenso) |
| 4 | **EspoCRM** | Gerencia contas complexas B2B, hierarquia de permissões e regras avançadas de comissionamento. | `GPL-3.0` | [https://github.com/espocrm/espocrm](https://github.com/espocrm/espocrm) |

### Pilar 3: Atendimento Omnicanal, WhatsApp & Chatbots
**Módulo SaaS Alvo:** `RD Station Conversas (Tallos / Z-API)`  
*Responsável pela caixa de entrada unificada de atendimento ao cliente, conexão estável com múltiplos números de WhatsApp e triagem automatizada via chatbots interativos.*

| # | Ferramenta | Papel no Pilar | Licença | Repositório GitHub |
| :---: | :--- | :--- | :---: | :--- |
| 1 | **Chatwoot** | Inbox unificada para múltiplos atendentes humanos responderem WhatsApp, Webchat e Instagram. | `MIT` | [https://github.com/chatwoot/chatwoot](https://github.com/chatwoot/chatwoot) |
| 2 | **Evolution API** | Conecta os números de WhatsApp corporativos e integra diretamente com o Chatwoot e n8n. | `Apache-2.0` | [https://github.com/EvolutionAPI/evolution-api](https://github.com/EvolutionAPI/evolution-api) |
| 3 | **Typebot** | Realiza o primeiro atendimento, coleta dados do lead e transfere para a fila certa no Chatwoot. | `AGPL-3.0` | [https://github.com/baptisteArno/typebot.io](https://github.com/baptisteArno/typebot.io) |
| 4 | **WAHA** | Redundância de conexão WhatsApp para disparos de alertas transacionais críticos. | `Apache-2.0` | [https://github.com/devlikeapro/waha](https://github.com/devlikeapro/waha) |

---

## 3. Camada de Cola, SSO & Orquestração Integrada

- **Autenticação Unificada (SSO):** Keycloak / Authentik (OpenID Connect / SAML) unificando o login dos colaboradores no Twenty CRM, Chatwoot, Directus e Mautic.
- **Barramento de Eventos:** n8n Community Edition atuando como orquestrador central de eventos assíncronos (Lead capturado no Typebot -> pontuado no Mautic -> oportunidade criada no Twenty -> alerta enviado no WhatsApp).
- **Reverse Proxy & TLS:** Traefik Proxy v3 com terminação TLS automática via Let's Encrypt e roteamento por subdomínios corporativos (mkt.empresa.com.br, crm.empresa.com.br, chat.empresa.com.br).

### Fluxo de Dados Integrado
```
1. Lead entra via Typebot ou Landing Page Directus;
2. Webhook dispara no n8n que cadastra o contato no Mautic para fluxo de nutrição;
3. Ao atingir pontuação de qualificação (Lead Scoring >= 50), o Mautic aciona o n8n;
4. O n8n cria a Oportunidade no Twenty CRM e abre uma sala de conversa no Chatwoot;
5. O vendedor agenda demonstração via Cal.com e envia proposta pelo Documenso;
6. O status de ganho atualiza o ERP e encerra o ciclo comercial com registro integral.
```

---

## 4. Deploy Consolidado All-in-One

**Dimensionamento de Hardware:**
- RAM Recomendada: 16 GB RAM
- CPU Recomendada: 8 vCPU
- Armazenamento: 120 GB NVMe SSD

### Exemplo de Docker Compose Unificado
```yaml
version: '3.8'

networks:
  ecosystem_net:
    driver: bridge

services:
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
    networks:
      - ecosystem_net

  keycloak:
    image: quay.io/keycloak/keycloak:latest
    command: start-dev
    environment:
      - KEYCLOAK_ADMIN=admin
      - KEYCLOAK_ADMIN_PASSWORD=SegredoForte2026
    networks:
      - ecosystem_net

  n8n:
    image: n8nio/n8n:latest
    environment:
      - N8N_BASIC_AUTH_ACTIVE=true
      - N8N_HOST=n8n.suaempresa.com.br
    networks:
      - ecosystem_net

  mautic:
    image: mautic/mautic:latest
    networks:
      - ecosystem_net

  twenty:
    image: twentyhq/twenty:latest
    networks:
      - ecosystem_net

  chatwoot:
    image: chatwoot/chatwoot:latest
    networks:
      - ecosystem_net

  evolution-api:
    image: atendai/evolution-api:v2.1.0
    networks:
      - ecosystem_net
```

### Passos de Instalação

1. **Provisionamento do Host:** Contrate uma VPS de 8 vCPU / 16 GB RAM com Ubuntu 22.04 LTS e instale Docker Engine e Docker Compose.
2. **Configuração de DNS Wildcard:** Crie uma entrada DNS tipo A apontando `*.suaempresa.com.br` para o IP público da VPS.
3. **Subida do Cluster Integrado:** Execute `docker compose up -d` na pasta do ecossistema e acesse os painéis com certificados SSL automáticos.
