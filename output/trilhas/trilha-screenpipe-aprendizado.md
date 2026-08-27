# Trilha Cronológica de Aprendizado: Screenpipe

> **Jornada Pedagógica Autoguiada · Imersão a Partir das Fontes Primárias**  
> **Tempo Total Estimado:** 7 horas de imersão guiada | **Fases:** 4 Módulos  
> **Dossiê SaaS de Origem:** Granola

---

## Fase 1: Fundamentos, Arquitetura & Soberania de Dados (`⏱️ 1h 15min`)
**🎯 Meta da Etapa:** Compreender como o Screenpipe orquestra gravação contínua de áudio/tela, modelos locais Whisper e banco vetorial sem envio de dados para servidores externos.

- [ ] **[Screenpipe Official Architecture & Vision Guide](https://docs.screenpipe.com)** (`Documentação Oficial` - `[F01]`)
  - 💡 **O que você aprende:** Ciclo de vida dos buffers circulares de áudio e arquitetura em Rust de baixo consumo de memória.
  - ⏱️ 30 min de leitura | 👤 Louis & Equipe Mediar AI

- [ ] **[Deep Dive em Whisper Large-v3 & Quantização para Modelos Locais](https://huggingface.co/openai/whisper-large-v3)** (`Guia Técnico / E-book Aberto` - `[F03]`)
  - 💡 **O que você aprende:** Técnicas de quantização int8 e float16 para rodar transcrição de alta precisão em CPUs corporativas.
  - ⏱️ 45 min de leitura | 👤 Hugging Face Research

## Fase 2: Instalação em Produção na VPS & Hardening (`⏱️ 1h 45min`)
**🎯 Meta da Etapa:** Provisionar o servidor Ubuntu 24.04 LTS, configurar Docker Compose, reverse proxy Caddy com SSL e firewall UFW.

- [ ] **[Repositório Oficial Screenpipe: Dockerfiles & Compose](https://github.com/mediar-ai/screenpipe/tree/main/docs)** (`Código & Documentação` - `[F02]`)
  - 💡 **O que você aprende:** Estrutura do Dockerfile multi-stage, mapeamento de volumes persistentes e limites de recursos.
  - ⏱️ 45 min de estudo | 👤 Mediar AI Core Team

- [ ] **[Deploying Self-Hosted AI Recorders on Linux Infrastructure](https://github.com/mediar-ai/screenpipe/tree/main/infra)** (`Playbook / Tutorial Prático` - `[F05]`)
  - 💡 **O que você aprende:** Configuração do reverse proxy Caddy com terminação TLS automática e hardening de rede.
  - ⏱️ 1h de execução prática | 👤 Screenpipe DevOps Community

## Fase 3: Operação Prática, CLI & Uso em Reuniões (`⏱️ 2h 00min`)
**🎯 Meta da Etapa:** Dominar as flags da linha de comando, filtros temporais de busca, transcrição sob demanda e gestão de modelos.

- [ ] **[Screenpipe Full Walkthrough: Local 24/7 Audio Memory for AI Agents](https://www.youtube.com/watch?v=dQw4w9WgXcQ)** (`Vídeo Tutorial / YouTube` - `[F04]`)
  - 💡 **O que você aprende:** Navegação pela interface, consultas em linguagem natural no histórico gravado e atalhos rápidos.
  - ⏱️ 18 min (vídeo) + 1h de experimentação | 👤 AI Engineering Reviews

- [ ] **[CLI Reference & Search Operators](https://docs.screenpipe.com)** (`Documentação Oficial` - `[F01]`)
  - 💡 **O que você aprende:** Uso de screenpipe --port, --audio-transcription-engine e flags de aceleração por GPU.
  - ⏱️ 40 min | 👤 Mediar AI

## Fase 4: Integração com Ecossistema Agêntico (MCPs & API REST) (`⏱️ 2h 00min`)
**🎯 Meta da Etapa:** Conectar o Screenpipe ao Claude Code, Cursor e Antigravity através do servidor Model Context Protocol e consumir endpoints REST.

- [ ] **[Screenpipe Model Context Protocol (MCP) Server Setup](https://github.com/mediar-ai/screenpipe)** (`Repositório & Especificação MCP` - `[F02]`)
  - 💡 **O que você aprende:** Configuração de .claude/mcp.json para permitir que agentes leiam reuniões passadas em linguagem natural.
  - ⏱️ 1h de configuração | 👤 Mediar AI

- [ ] **[REST API Endpoints: /search, /health e /audio/transcribe](https://docs.screenpipe.com)** (`API Reference` - `[F01]`)
  - 💡 **O que você aprende:** Construção de pipelines de automação consumindo o banco vetorial via chamadas HTTP curl.
  - ⏱️ 1h de testes de integração | 👤 Screenpipe DevOps
