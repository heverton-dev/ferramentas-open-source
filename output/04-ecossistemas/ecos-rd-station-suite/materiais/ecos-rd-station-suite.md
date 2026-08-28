# Macro-Ecossistema RD Station: Marketing, CRM & Conversas

> **Macro-Ecossistema Soberano · Desmantelamento RD Station Suite · Padrão Diamante R5-E**  
> Dossiê completo de substituição soberana para o Macro-Ecossistema RD Station (Marketing, CRM, Conversas/WhatsApp, Formulários e Automações), integrando ferramentas líderes por pilar através de autenticação única (Keycloak SSO), barramento de dados assíncrono (n8n) e proxy seguro (Traefik).

---

## 1. Visão Executiva & Demonstrativo Financeiro de TCO

### Consolidado Global da Suíte
- **Macro-SaaS Substituído:** RD Station Suite (Marketing Pro + CRM Pro + Conversas Enterprise + Zapier)
- **Custo SaaS Estimado:** R$ 114.000/ano (RD Marketing Pro R$ 42k + RD CRM 10 vendedores R$ 36k + RD Conversas 10 atendentes R$ 36k)
- **Custo da Infraestrutura Soberana:** R$ 4.200/ano (VPS 8 vCPU / 16 GB RAM a R$ 350/mês)
- **Economia Líquida Anual:** R$ 109.800/ano (Economia Líquida de 96.3%)
- **Payback Estimado:** Payback positivo em apenas 14 dias de operação unificada.


### Demonstrativo de TCO Desmembrado por Grupo Funcional

| Grupo / Frente de Negócio | SaaS de Referência | Custo SaaS Anual | Custo VPS Alocado | Economia Líquida | Economia (%) |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **Grupo 1: Marketing & Nutrição** | RD Station Marketing (Plano Pro - 50k leads) | `R$ 42.000/ano` | `R$ 1.440/ano (Fraqueza de ~3 vCPU / 6 GB RAM)` | **R$ 40.560/ano** | **96.5%** |
| **Grupo 2: Pipeline Comercial & CRM** | RD Station CRM (Plano Avançado - 10 licenças) | `R$ 36.000/ano` | `R$ 1.440/ano (Fraqueza de ~3 vCPU / 6 GB RAM)` | **R$ 34.560/ano** | **96.0%** |
| **Grupo 3: Atendimento & WhatsApp** | RD Station Conversas / Tallos (10 operadores) | `R$ 36.000/ano` | `R$ 1.320/ano (Fraqueza de ~2 vCPU / 4 GB RAM)` | **R$ 34.680/ano** | **96.3%** |


---

## 2. Pilares Funcionais & Frentes de Negócio

### Grupo 1: Marketing, Nutrição & Landing Pages
- **Módulo SaaS Alvo:** `RD Station Marketing (Planos Pro / Enterprise)`
- **Subtotal de Economia do Grupo:** **R$ 42.000/ano**
- **Escopo:** *Frente responsável pela atração de tráfego, captura e enriquecimento de contatos, criação autônoma de landing pages dinâmicas, disparos de e-mail marketing em massa e automação de fluxos com pontuação de leads (lead scoring).*

| # | Ferramenta | Substitui Diretamente | Racional da Escolha | Economia Estimada | Licença |
| :---: | :--- | :--- | :--- | :---: | :---: |
| 1 | **Mautic** | RD Station Marketing (Módulo de Automação de Fluxos & Lead Scoring) | Única plataforma open source com construtor visual de jornadas em árvore equivalente ao RD Pro, com rastreamento avançado de comportamento web (lead tracking) e ausência de cobrança por volume de contatos na base. | **R$ 42.000/ano (Base de 50.000 leads)** | `GPL-3.0` |
| 2 | **Listmonk** | RD Station Marketing (Módulo de Disparos de E-mail & Broadcast) | Desenvolvido em Go puro, entrega milhões de e-mails consumindo menos de 50 MB de RAM, suportando segmentação relacional JSONB instantânea e eliminando custos punitivos por envio. | **R$ 18.000/ano** | `AGPL-3.0` |
| 3 | **Directus** | RD Station Marketing (Construtor de Landing Pages & Formulários Estáticos) | Converte qualquer banco de dados relacional em uma interface no-code intuitiva para o time de marketing editar textos, banners e seções de conversão sem risco de quebra de layout. | **R$ 12.000/ano** | `GPL-3.0` |

### Grupo 2: Pipeline Comercial, CRM & Contratos
- **Módulo SaaS Alvo:** `RD Station CRM (Plano Avançado para Equipes de Vendas)`
- **Subtotal de Economia do Grupo:** **R$ 36.000/ano**
- **Escopo:** *Frente responsável pela gestão visual de oportunidades comerciais em formato Kanban, distribuição de leads qualificados, histórico de contatos, agendamento de reuniões e assinatura de propostas.*

| # | Ferramenta | Substitui Diretamente | Racional da Escolha | Economia Estimada | Licença |
| :---: | :--- | :--- | :--- | :---: | :---: |
| 1 | **Twenty** | RD Station CRM (Módulo de Pipeline Kanban, Oportunidades & Tarefas) | Arquitetura reativa ultrarrápida em React/TypeScript com sincronização bidirecional de e-mails, campos customizados ilimitados e experiência de usuário moderna superior a CRMs legados. | **R$ 24.000/ano (Equipe de 10 vendedores)** | `AGPL-3.0` |
| 2 | **Cal.com** | RD Station CRM (Agendamentos) / Calendly Integrado | Suporte a distribuição round-robin entre múltiplos corretores/vendedores, integração direta com CalDAV, Google e Outlook e total personalização sob domínio próprio. | **R$ 12.000/ano** | `AGPL-3.0` |
| 3 | **Documenso** | Clicksign / DocuSign / Módulo de Propostas Comerciais | Garante soberania jurídica dos documentos com trilha de auditoria criptográfica e registro de IPs, sem impor limites de contratos assinados por mês. | **R$ 18.000/ano** | `AGPL-3.0` |
| 4 | **EspoCRM** | RD Station CRM (Módulos Corporativos Avançados & Múltiplos Pipelines) | Mecanismo BPM no-code maduro para operações B2B que necessitam de regras de aprovação de desconto e múltiplos pipelines simultâneos por linha de produto. | **R$ 18.000/ano** | `GPL-3.0` |

### Grupo 3: Atendimento Omnichannel & WhatsApp
- **Módulo SaaS Alvo:** `RD Station Conversas (Antigo Tallos / Módulos de Mensageria)`
- **Subtotal de Economia do Grupo:** **R$ 36.000/ano**
- **Escopo:** *Frente responsável pela caixa de entrada unificada multicanal, conexão estável com múltiplos números de WhatsApp sem taxas por mensagem e triagem inteligente com chatbots.*

| # | Ferramenta | Substitui Diretamente | Racional da Escolha | Economia Estimada | Licença |
| :---: | :--- | :--- | :--- | :---: | :---: |
| 1 | **Chatwoot** | RD Station Conversas (Painel de Atendimento Multiatendente) | Software líder global em suporte omnicanal aberto, eliminando a cobrança por licença de atendente e fornecendo relatórios completos de CSAT e tempo de primeira resposta. | **R$ 36.000/ano (10 operadores)** | `MIT` |
| 2 | **Evolution API** | RD Station Conversas (Conectores Proprietários Z-API / Gupshup) | API brasileira madura com suporte a múltiplas instâncias simultâneas, conversão automática de áudios em formato compatível e integração nativa de 1 clique com o Chatwoot. | **R$ 18.000/ano** | `Apache-2.0` |
| 3 | **Typebot** | RD Station Conversas (Chatbots de Triagem) / Landbot | Melhor construtor visual de fluxos conversacionais do mercado, com suporte a variáveis, ramificações condicionais e integração nativa com modelos de IA para atendimento automático. | **R$ 14.400/ano** | `AGPL-3.0` |
| 4 | **WAHA** | RD Station Notificações WhatsApp / Twilio Messaging | Solução headless ultra-estável em contêiner isolado para garantir que mensagens transacionais de sistema sejam enviadas mesmo em caso de sobrecarga da fila de atendimento. | **R$ 12.000/ano** | `Apache-2.0` |

---

## 3. Camada de Cola, SSO & Orquestração Integrada

- **Autenticação Unificada (SSO):** Keycloak / Authentik (OpenID Connect / SAML) unificando o login dos colaboradores no Twenty CRM, Chatwoot, Directus e Mautic.
- **Barramento de Eventos:** n8n Community Edition atuando como orquestrador central de eventos assíncronos (Lead capturado no Typebot -> pontuado no Mautic -> oportunidade criada no Twenty -> alerta enviado no WhatsApp).
- **Reverse Proxy & TLS:** Traefik Proxy v3 com terminação TLS automática via Let's Encrypt e roteamento por subdomínios corporativos (mkt.empresa.com.br, crm.empresa.com.br, chat.empresa.com.br).

### Fluxo de Dados Integrado
```
1. Entrada de Leads: Lead preenche formulário no Typebot ou na Landing Page gerenciada pelo Directus;
2. Cadastramento & Nutrição: O webhook dispara no n8n que cadastra o contato no Mautic e inicia a régua de nutrição de e-mails;
3. Qualificação por Lead Scoring: Ao atingir 50 pontos no Mautic, um webhook notifica o n8n;
4. Criação de Oportunidade: O n8n cria a negociação no Twenty CRM e abre uma sala de contato prioritária no Chatwoot;
5. Agendamento & Fechamento: O vendedor envia link do Cal.com para demonstração e emite contrato pelo Documenso;
6. Sincronização Final: A assinatura do contrato atualiza o status de 'Ganho' no Twenty CRM e notifica o time no WhatsApp.
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
