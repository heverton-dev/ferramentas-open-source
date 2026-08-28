# Trilha Cronológica de Aprendizado: Coqui XTTS-v2 (Clonagem de Voz Multilingue & TTS Neural)

> **Jornada Pedagógica Autoguiada · Imersão a Partir das Fontes Primárias** 
> **Tempo Total Estimado:** 6 horas de imersao guiada | **Fases:** 5 Módulos 
> **Dossiê SaaS de Origem:** Elevenlabs

---

## Fase 1: Fundamentos de Audio Neural, Transformers & TTS (`⏱ 1h 00min`)
** Meta da Etapa:** Compreender como a arquitetura autoregressiva do XTTS-v2 gera espectrogramas de mel e como o vocoder HiFi-GAN converte tensores em audio perceptivel.

- [ ] **[Coqui TTS Architecture & Deep Learning Foundations](https://github.com/coqui-ai/TTS)** (`Documentacao Oficial` - `[F01]`)
 - **O que você aprende:** Pipeline acustico, tokenizacao fonetica e condicionamento por speaker latents.
 - ⏱ 30 min | Coqui AI Core Team

- [ ] **[XTTS-v2 Model Card & Weights Overview](https://huggingface.co/coqui/XTTS-v2)** (`Artigo Tecnico` - `[F02]`)
 - **O que você aprende:** Parametros de inferencia, idiomas suportados e benchmarks de naturalidade.
 - ⏱ 30 min | Hugging Face Hub

## Fase 2: Setup de Producao na VPS com Aceleracao NVIDIA GPU (`⏱ 1h 30min`)
** Meta da Etapa:** Configurar container Docker oficial com suporte a CUDA 12+, persistencia de volumes e endpoints FastAPI.

- [ ] **[NVIDIA Container Toolkit & GPU Passthrough](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/)** (`Tutorial Pratico` - `[F03]`)
 - **O que você aprende:** Drivers CUDA, runtime NVIDIA no Docker e monitoramento com nvidia-smi.
 - ⏱ 45 min | NVIDIA Documentation

- [ ] **[XTTS FastAPI Server Configuration](https://github.com/coqui-ai/TTS/wiki/FastAPI-Server)** (`Lab Interativo` - `[F04]`)
 - **O que você aprende:** Endpoints REST para sintese em lote, listagem de linguagens e upload de vozes.
 - ⏱ 45 min | Coqui Community

## Fase 3: Clonagem de Voz Zero-Shot com Amostras Reais (`⏱ 1h 00min`)
** Meta da Etapa:** Preparar arquivos WAV de referencia, limpar ruidos, normalizar volume e gerar clonagens de alta fidelidade.

- [ ] **[Voice Conditioning & Audio Preprocessing Best Practices](https://arxiv.org/abs/2406.04904)** (`Guia de Engenharia` - `[F05]`)
 - **O que você aprende:** Normalizacao a -16 LUFS, amostragem a 24kHz e eliminacao de artefatos de compressao.
 - ⏱ 30 min | Eren Golge et al.

## Fase 4: Streaming em Baixa Latencia & Integracao com LLMs (`⏱ 1h 30min`)
** Meta da Etapa:** Conectar o XTTS via WebSocket em tempo real para alimentar agentes conversacionais inteligentes com respostas de audio instantaneas.

- [ ] **[Chunked Audio Streaming Architecture](https://github.com/coqui-ai/TTS)** (`Tutorial Pratico` - `[F01]`)
 - **O que você aprende:** Time to First Byte (TTFB), chunks de audio de 200ms e duplex WebSockets.
 - ⏱ 45 min | Coqui Community

## Fase 5: Hardening, Monitoramento & Desinstalacao Cirurgica (`⏱ 1h 00min`)
** Meta da Etapa:** Configurar Nginx com SSL, implementar monitoramento de VRAM da GPU e validar os 4 passos de isolamento da VPS.

- [ ] **[Production Hardening & GPU Memory Management](https://github.com/coqui-ai/TTS)** (`Playbook DevOps` - `[F04]`)
 - **O que você aprende:** Proxy reverso Nginx, liberacao de VRAM e checklist de saude da VPS.
 - ⏱ 30 min | Fabrica Universal AIDD
