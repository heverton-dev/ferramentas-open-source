# Dossiê Vertical de Desmantelamento SaaS: Granola (AI Meeting Notepad)

> **Padrão Diamante R5-V · Quinteto Soberano Open Source**  
> **Alvo SaaS:** Granola (AI Meeting Notepad) | **Custo Médio:** US$ 120/ano por usuário (~R$ 720/ano) | **Risco de Privacidade:** Envio de discussões financeiras, código interno e segredos industriais de reuniões para servidores externos.  

---

## 1. O Quinteto Soberano Open Source

| Rank | Classificação | Ferramenta | Licença | Repositório | Economia Estimada |
| :---: | :--- | :--- | :---: | :--- | :--- |
| **#1** | *A Mais Completa* | **Screenpipe (Captura 24/7 & Contexto Total)** | `Apache-2.0` | [https://github.com/mediar-ai/screenpipe](https://github.com/mediar-ai/screenpipe) | R$ 14.400/ano |
| **#2** | *A Mais Robusta* | **WhisperX + PyAnnote (Diarização Industrial)** | `BSD-4-Clause` | [https://github.com/m-bain/whisperX](https://github.com/m-bain/whisperX) | R$ 18.000/ano |
| **#3** | *A Mais Moderna* | **Open-NotebookLM (Podcasts & Síntese em Áudio)** | `Apache-2.0` | [https://github.com/gabrielchua/open-notebooklm](https://github.com/gabrielchua/open-notebooklm) | R$ 12.000/ano |
| **#4** | *A Mais Leve* | **Whisper.cpp (Inferência em C++ Nativo)** | `MIT` | [https://github.com/ggerganov/whisper.cpp](https://github.com/ggerganov/whisper.cpp) | R$ 9.600/ano |
| **#5** | *A Mais Simples* | **Faster-Whisper CLI (Transcrição com 1 Comando)** | `MIT` | [https://github.com/SYSTRAN/faster-whisper](https://github.com/SYSTRAN/faster-whisper) | R$ 7.200/ano |

---

## 2. Detalhamento Técnico das Ferramentas do Quinteto

### #1 · Screenpipe (Captura 24/7 & Contexto Total) (*A Mais Completa*)

- **O Que Faz:** Grava áudio do microfone e da saída do sistema continuamente, transcreve com Whisper local e permite consultar qualquer reunião passada em linguagem natural.
- **Como Funciona:** Aplicação de alta performance em Rust que indexa áudio e capturas de tela em SQLite local com embeddings vetoriais, operando 100% offline.
- **Requisitos de Infra:** 4 GB RAM, 4 vCPU ou Apple Silicon
- **Comando Rápido:** `cargo run --release --bin screenpipe`
- **White-Label & Design System:** Esforço `Mínimo (Plug & Play)` (Tauri + Next.js + Tailwind) - O cliente desktop do Screenpipe é construído em Next.js/Tailwind envelopado em Tauri. Permite customizar paleta de cores institucional, logotipo e fontes corporativas via tokens de CSS ou arquivo de configuração de tema.

**Uso Complementar & Ecossistema Agêntico:**
- **MCP Server:** `@mediar-ai/screenpipe-mcp` (`npx -y @mediar-ai/screenpipe-mcp`) - Servidor oficial de Model Context Protocol que permite ao Claude Code, Cursor e Antigravity buscarem trechos de áudio e tela gravados.
- **Agent Skill:** `skill-screenpipe-query` (`.claude/skills/screenpipe-query/SKILL.md`) - Skill especializada que resume atas executivas no padrão ISO com identificação de prazos e responsáveis a partir de dados do Screenpipe.
- **CLI Tool:** `screenpipe-cli` (`screenpipe pipe search 'orçamento 2026'`) - Interface de terminal para filtrar transcrições por palavras-chave, timestamps e nomes de janelas ativas.

### #2 · WhisperX + PyAnnote (Diarização Industrial) (*A Mais Robusta*)

- **O Que Faz:** Transcreve gravações com alinhamento temporal em nível de palavra (word-level timestamps) e identifica com precisão cirúrgica quem falou cada frase.
- **Como Funciona:** Combina a velocidade do Faster-Whisper (CTranslate2) com o modelo de diarização acústica PyAnnote Audio e alinhamento fonético via wav2vec2.
- **Requisitos de Infra:** 4 GB RAM, 4 vCPU / GPU NVIDIA (Recomendada)
- **Comando Rápido:** `pip install whisperx && whisperx reuniao.mp3 --diarize --hf_token HF_TOKEN`
- **White-Label & Design System:** Esforço `Headless (UI Livre)` (API REST / Python Headless) - Motor puramente headless e agnóstico de interface. Permite que seu time de desenvolvimento conecte o frontend corporativo oficial (React, Vue, Next.js) usando 100% dos componentes do Design System da sua empresa.

**Uso Complementar & Ecossistema Agêntico:**
- **Sidecar Plugin:** `pyannote.audio` (`https://github.com/pyannote/pyannote-audio`) - Motor neural de biometria vocal e diarização treinado em centenas de milhares de horas de conversa multilocutor.
- **Agent Skill:** `skill-transcript-cleaner` (`.claude/skills/transcript-cleaner/SKILL.md`) - Skill de pós-processamento que remove vícios de linguagem ('né', 'tipo', 'humm') e atribui nomes reais aos identificadores SPEAKER_00.
- **CLI Tool:** `whisperx-batch` (`whisperx --model large-v3 --language pt *.wav`) - Processamento em lote capaz de transcrever um dia inteiro de reuniões em poucos minutos usando GPU.

### #3 · Open-NotebookLM (Podcasts & Síntese em Áudio) (*A Mais Moderna*)

- **O Que Faz:** Transforma notas e atas de reunião em resumos executivos conversacionais falados por dois apresentadores de IA com entonação natural.
- **Como Funciona:** Extrai pontos-chave com LLM local, formata um roteiro dinâmico de perguntas e respostas e sintetiza vozes com modelos acústicos (Bark/XTTS).
- **Requisitos de Infra:** 8 GB RAM, 4 vCPU ou GPU com 6GB VRAM
- **Comando Rápido:** `git clone https://github.com/gabrielchua/open-notebooklm && pip install -r requirements.txt`
- **White-Label & Design System:** Esforço `Mínimo (Plug & Play)` (Streamlit / Gradio / Tailwind) - A interface gráfica aceita injeção de tema visual via arquivo de configuração (.streamlit/config.toml) ou CSS global, permitindo plugar as cores primárias, tipografia e logo institucional em menos de 5 minutos.

**Uso Complementar & Ecossistema Agêntico:**
- **Agent Skill:** `skill-podcast-briefing` (`.claude/skills/podcast-briefing/SKILL.md`) - Prompt orquestrado para extrair decisões financeiras, prazos e impedimentos em formato de pauta de podcast.
- **CLI Tool:** `notebooklm-audio-cli` (`python generate_podcast.py --input ata.md --output briefing.mp3`) - Comando direto para pipelines determinísticas de geração de áudio executivo via CI/CD ou cron job.
- **Sidecar Plugin:** `F5-TTS Voice Engine` (`pip install f5-tts`) - Motor de clonagem de voz por difusão que permite gerar os resumos nas vozes dos próprios diretores da empresa.

### #4 · Whisper.cpp (Inferência em C++ Nativo) (*A Mais Leve*)

- **O Que Faz:** Transcreve arquivos de áudio e microfone em tempo real consumindo quase zero de processador e sem precisar de Python ou CUDA.
- **Como Funciona:** Portabilidade pura em C/C++ dos modelos Whisper da OpenAI com suporte a instruções vetoriais AVX2, NEON (Apple Silicon) e quantização de 4 bits.
- **Requisitos de Infra:** 180 MB RAM, 1 vCPU (Qualquer Máquina)
- **Comando Rápido:** `git clone https://github.com/ggerganov/whisper.cpp && make && ./main -m models/ggml-base.bin reuniao.wav`
- **White-Label & Design System:** Esforço `Alto (Hardcoded / Fork)` (C++ CLI / Binário Nativo) - Não possui interface web integrada por padrão; opera como binário de linha de comando de alto desempenho. Para incorporar o Design System da empresa, deve ser consumido via wrapper HTTP ou plugins de terceiros (ex: Obsidian).

**Uso Complementar & Ecossistema Agêntico:**
- **Sidecar Plugin:** `Obsidian Whisper Plugin` (`https://github.com/nikdanilov/whisper-obsidian`) - Grava e transcreve reuniões diretamente para suas notas do Obsidian usando o binário do whisper.cpp.
- **MCP Server:** `mcp-whisper-local` (`npx -y mcp-whisper-cpp`) - Servidor MCP ultraleve que expõe a ferramenta de transcrição para agentes de inteligência artificial.
- **CLI Tool:** `whisper-stream` (`./stream -m models/ggml-base.bin -t 4 --step 3000`) - Modo de escuta contínua de microfone que exibe na tela o que está sendo dito ao vivo com 3 segundos de buffer.

### #5 · Faster-Whisper CLI (Transcrição com 1 Comando) (*A Mais Simples*)

- **O Que Faz:** Transcreve qualquer arquivo de áudio ou vídeo com precisão máxima através de um único comando simples no terminal.
- **Como Funciona:** Reimplementação do Whisper usando CTranslate2, sendo 4x mais rápida que a biblioteca oficial da OpenAI com metade da memória.
- **Requisitos de Infra:** 512 MB RAM, 1 vCPU
- **Comando Rápido:** `pip install faster-whisper && python -c "from faster_whisper import WhisperModel; model = WhisperModel('small'); segments, _ = model.transcribe('reuniao.mp3'); print(' '.join([s.text for s in segments]))"`
- **White-Label & Design System:** Esforço `Headless (UI Livre)` (Python Headless Engine) - Biblioteca focada em eficiência pura de inferência sem camada gráfica engessada. Sua empresa é totalmente livre para plugar essa engine em qualquer tela, intranet ou aplicativo existente respeitando o Design System corporativo.

**Uso Complementar & Ecossistema Agêntico:**
- **Agent Skill:** `skill-meeting-actions-extractor` (`.claude/skills/actions-extractor/SKILL.md`) - Skill de extração automática que gera listas de tarefas no formato Markdown para copiar direto para o Notion ou Kanban.
- **CLI Tool:** `fabric-cli` (`fabric --pattern create_meeting_minutes`) - Framework aberto da DanielMiessler para aplicar padrões executivos de ata e resumo sobre qualquer transcrição.
- **Sidecar Plugin:** `ffmpeg-audio-extractor` (`ffmpeg -i reuniao.mp4 -vn -ar 16000 -ac 1 audio.wav`) - Utilitário padrão da indústria para extrair canais de áudio otimizados de gravações de vídeo em segundos.

---

## 3. Matriz de Decisão & Migração Soberana

Para substituir integralmente o **Granola (AI Meeting Notepad)**, recomenda-se a esteira automatizada de implantação em VPS com os manuais operacionais disponíveis em `output/`.