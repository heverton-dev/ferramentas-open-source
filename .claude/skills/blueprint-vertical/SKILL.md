---
name: blueprint-vertical
description: Gerador de Blueprints Verticais de Negócio & Infraestrutura Open-Source para Devs Solos e Consultorias. Cria documentação técnica, docker-compose, manual de implementação e apresentação comercial interativa em HTML com calculadora de ROI para qualquer nicho de mercado.
---

# Skill: Gerador de Blueprints Verticais & MSP Soberano

Esta skill automatiza a criação de soluções completas de infraestrutura open-source para nichos verticais de mercado (clínicas, advocacia, imobiliárias, contabilidade, e-commerce, academias, etc.).

## Fluxo de Execução Obrigatório em 4 Fases:

### Fase 0: Inteligência de Mercado & Reconhecimento (Market Recon)
Antes de gerar qualquer código ou ferramenta, o agente DEVE realizar buscas ativas na web para levantar:
1. **Concorrentes SaaS Dominantes:** Mapear os 3 a 5 softwares proprietários mais usados no nicho e seus custos reais.
2. **Dores Reais & Reclamações:** O que os empresários do setor reclamam sobre os softwares atuais.
3. **Jargões & Termos do Setor:** Vocabulário técnico, rotina diária e particularidades do fluxo de trabalho.
4. **Compliance & Regulamentação:** Regras de conselhos de classe (OAB, CFM, CRO, CRECI, etc.) e LGPD.
5. **Gravação:** Salvar o relatório analítico em `output/blueprints/<slug-do-nicho>/contexto/INTELIGENCIA-DE-MERCADO.md`.

### Fase 1: Arquitetura Agêntica 360° & Mapeamento do Arsenal Open-Source
Selecionar no catálogo `arsenal-open-source` a stack completa 360° de alta tecnologia:
- **Infraestrutura VPS Padrão:** **Contabo Cloud VPS M** (6 vCPUs, 16 GB RAM, 100 GB NVMe por ~R$ 55/mês)
- **Mídia & Redes Sociais:** `Postiz` (agendamento autônomo de Reels/TikTok/Instagram) + `Kokoro / F5-TTS` (clonagem de voz para locuções de anúncios)
- **Automação Autônoma de Processos:** `n8n` (self-hosted com execuções ilimitadas sem custo de Zapier)
- **Atendimento Natural por Voz & RAG:** `Evolution API` + `Chatwoot` + `faster-whisper` (áudio < 350ms) + `Dify.ai` + `Qdrant` (catálogo e regras)
- **Operação, ERP, PDV & Documentos:** `Odoo POS / ERPNext` + `DocuSeal` (assinatura digital)
- **BI, CX & Retenção:** `Metabase` (painel do dono) + `Formbricks` (NPS e pesquisa pós-venda)

### Fase 2: Engenharia de Infraestrutura & Templates
Gerar `docker-compose.yml` de produção (360°), scripts de setup/backup, prompts do agente com RAG vetorial e o manual `MANUAL-DEV-SOLO.md` calibrado na Contabo.

### Fase 3: Apresentação Comercial Interativa
Gerar `apresentacao-comercial.html` com calculadora de ROI calibrada com os custos reais de agências, Zapier e SaaS substituídos.

## Estrutura Canônica de um Hub Vertical (`output/blueprints/<slug-do-nicho>/`):

```
output/blueprints/<slug-do-nicho>/
├── contexto/                      # Inteligência de mercado e pesquisa prévia
│   └── INTELIGENCIA-DE-MERCADO.md # Dores reais, concorrentes mapeados e jargões
├── README.md                      # Sumário executivo e visão geral do hub
├── apresentacao-comercial.html    # Apresentação comercial interativa com calculadora de ROI
├── MANUAL-DEV-SOLO.md             # Guia de engenharia passo a passo para o Dev Solo
├── infra/                         # Infraestrutura como código (Docker/Compose)
│   ├── docker-compose.yml         # Stack de produção completa (com Qdrant, Dify e Whisper)
│   ├── .env.example               # Variáveis de ambiente parametrizadas
│   └── scripts/
│       ├── setup.sh               # Script de deploy em 1 comando
│       └── backup.sh              # Script de backup diário com retenção
├── templates/                     # Assets, prompts de IA e bases de conhecimento
│   ├── system-prompt-agente.md    # Prompt de personalidade e vendas do agente de IA
│   └── base-conhecimento-rag.md   # Dados estruturados do nicho para alimentar o Qdrant
└── proposta/                      # Documentação de vendas
    └── contrato-prestacao-servicos.md # Minuta jurídica de contrato mensal (MRR)
```

## Como Executar:
Ao receber o comando `/gerar-blueprint <nicho>` ou prompt equivalente, siga rigorosamente a estrutura de 6 cadeias de valor, realize os cálculos de TCO/MRR e gere os artefatos dentro de `output/blueprints/<slug-do-nicho>/`.
