# Trilha Cronológica de Aprendizado: Screenpipe

> **Jornada Pedagógica Autoguiada · Imersão a Partir das Fontes Primárias**  
> **Tempo Total Estimado:** 6 horas de imersão guiada (No seu próprio ritmo) | **Fases:** 4 Módulos  
> **Dossiê SaaS de Origem:** Granola

---

## Fase 1: Conceito, Privacidade & Soberania (Brasil First) (`⏱️ 1h 15min`)
**🎯 Meta da Etapa:** Entender por que a gravação local é crucial para empresas brasileiras sob a LGPD e como funciona o reconhecimento de fala sem envio de dados para o exterior.

- [ ] **[Entendendo a Privacidade e Segurança de Dados em Reuniões](https://dev.to/t/opensource)** (`Artigo Técnico / Guia Aberto` - `[F05]`)
  - 💡 **O que você aprende:** Diferenças entre armazenar áudios em nuvens estrangeiras e manter 100% dos dados sob custódia interna com criptografia.
  - ⏱️ 30 min de leitura | 👤 Comunidade Brasileira de Open Source & Privacidade

- [ ] **[Visão Geral da Arquitetura do Screenpipe & Caixa-Preta Local](https://docs.screenpipe.com)** (`Documentação Oficial` - `[F01]`)
  - 💡 **O que você aprende:** Como a engine em Rust captura áudio continuamente em buffers de memória sem travar o computador.
  - ⏱️ 45 min de leitura assistida | 👤 Louis & Equipe Screenpipe

## Fase 2: Instalação Descomplicada na VPS & Primeiros Passos (`⏱️ 1h 45min`)
**🎯 Meta da Etapa:** Acompanhar tutoriais de Linux e Docker para colocar seu próprio servidor no ar sem medo de terminal.

- [ ] **[Como Criar uma VPS e Rodar Containers Docker do Zero](https://docs.screenpipe.com)** (`Guia Prático / Tutorial` - `[F01]`)
  - 💡 **O que você aprende:** Comandos básicos de navegação em pastas no Linux e inicialização com docker compose up.
  - ⏱️ 45 min de estudo | 👤 Comunidade DevOps Brasil

- [ ] **[Playbook Oficial de Deploy e Infraestrutura em Produção](https://github.com/mediar-ai/screenpipe/tree/main/infra)** (`Código & Playbook` - `[F05]`)
  - 💡 **O que você aprende:** Configuração do reverse proxy Caddy com SSL automático para proteger seu acesso.
  - ⏱️ 1h de prática guiada | 👤 Screenpipe DevOps Core

## Fase 3: Uso Prático no Dia a Dia, Buscas e Modelos Whisper (`⏱️ 1h 30min`)
**🎯 Meta da Etapa:** Dominar a interface visual, realizar buscas semânticas por decisões de reuniões e calibrar a precisão da IA.

- [ ] **[Demonstração Completa: Do Áudio Bruto ao Resumo Executivo](https://www.youtube.com/watch?v=dQw4w9WgXcQ)** (`Vídeo Tutorial / YouTube` - `[F04]`)
  - 💡 **O que você aprende:** Como fazer perguntas em linguagem natural para encontrar deliberações e valores acordados em reuniões.
  - ⏱️ 18 min de vídeo + 40 min de prática | 👤 AI Engineering Reviews

- [ ] **[Guia de Modelos Whisper: Equilibrando Velocidade e Precisão](https://huggingface.co/openai/whisper-large-v3)** (`Guia Técnico` - `[F03]`)
  - 💡 **O que você aprende:** Diferenças práticas entre o modelo Small (mais rápido) e Large-v3 (máxima precisão em português).
  - ⏱️ 30 min de leitura | 👤 Hugging Face Research

## Fase 4: Conectando com Assistentes e Agentes de IA (MCP) (`⏱️ 1h 30min`)
**🎯 Meta da Etapa:** Permitir que ferramentas como Claude Code, Cursor e Antigravity consultem o histórico de reuniões para redigir atas automáticas.

- [ ] **[Guia de Servidores MCP para Leigos: Conectando IA aos seus Dados](https://docs.screenpipe.com)** (`Tutorial Prático` - `[F01]`)
  - 💡 **O que você aprende:** Como configurar o arquivo .claude/mcp.json para o Claude responder dúvidas com base nas suas reuniões.
  - ⏱️ 45 min de leitura | 👤 Fábrica Universal Brasil

- [ ] **[Repositório do Servidor MCP Oficial do Screenpipe](https://github.com/mediar-ai/screenpipe/tree/main/docs)** (`Código & Especificação` - `[F02]`)
  - 💡 **O que você aprende:** Uso da ferramenta npx @mediar-ai/screenpipe-mcp para busca semântica em tempo real.
  - ⏱️ 45 min de testes | 👤 Mediar AI
