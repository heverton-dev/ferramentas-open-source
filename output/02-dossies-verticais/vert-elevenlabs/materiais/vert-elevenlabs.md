# Dossiê Vertical de Desmantelamento SaaS: ElevenLabs (Generative Voice AI & Voice Cloning)

> **Padrão Diamante R5-V · Quinteto Soberano Open Source**  
> **Alvo SaaS:** ElevenLabs (Generative Voice AI & Voice Cloning) | **Custo Médio:** US$ 60 a US$ 396/ano por usuário (Planos Starter a Pro com limites restritivos de caracteres) | **Risco de Privacidade:** Envio de áudios de gravações corporativas, vozes de executivos e roteiros de produtos confidenciais para os servidores em nuvem do ElevenLabs.  

---

## 1. O Quinteto Soberano Open Source

| Rank | Classificação | Ferramenta | Licença | Repositório | Economia Estimada |
| :---: | :--- | :--- | :---: | :--- | :--- |
| **#1** | *A Mais Robusta* | **Coqui XTTS v2 (Clonagem de Voz Multilíngue de Alta Fidelidade)** | `MPL-2.0` | [https://github.com/coqui-ai/TTS](https://github.com/coqui-ai/TTS) | R$ 14.400/ano |
| **#2** | *A Mais Completa* | **OpenVoice v2 (Clonagem Instantânea com Controle de Estilo e Emoção)** | `MIT` | [https://github.com/myshell-ai/OpenVoice](https://github.com/myshell-ai/OpenVoice) | R$ 16.800/ano |
| **#3** | *A Mais Moderna* | **ChatTTS (Conversação Natural & Sons Não-Verbais Realistas)** | `Apache-2.0` | [https://github.com/2noise/ChatTTS](https://github.com/2noise/ChatTTS) | R$ 15.000/ano |
| **#4** | *A Mais Leve* | **Piper TTS (Síntese Neural Ultra-Rápida para CPU & Dispositivos de Borda)** | `MIT` | [https://github.com/rhasspy/piper](https://github.com/rhasspy/piper) | R$ 10.800/ano |
| **#5** | *A Mais Simples* | **Edge-TTS (Síntese Neural Gratuita em Python sem Chave de API)** | `GPL-3.0` | [https://github.com/rany2/edge-tts](https://github.com/rany2/edge-tts) | R$ 7.200/ano |

---

## 2. Detalhamento Técnico das Ferramentas do Quinteto

### #1 · Coqui XTTS v2 (Clonagem de Voz Multilíngue de Alta Fidelidade) (*A Mais Robusta*)

- **O Que Faz:** Clona qualquer voz a partir de um arquivo de áudio de apenas 3 segundos e sintetiza fala natural em 17 idiomas (incluindo Português do Brasil) preservando emoção, ritmo e timbre original.
- **Como Funciona:** Arquitetura baseada em autoregressive speech language modeling com decoder HiFi-GAN em PyTorch, processando áudios a 24kHz com alta naturalidade fonética e controle de entonação.
- **Requisitos de Infra:** 4 GB RAM, 4 vCPU + GPU Nvidia com 4 GB VRAM
- **Comando Rápido:** `pip install TTS && tts --model_name tts_models/multilingual/multi-dataset/xtts_v2 --text 'Voz soberana sem custos por token.' --speaker_wav ./amostra.wav --language_idx pt --out_path output.wav`
- **White-Label & Design System:** Esforço `Headless (API / CLI First)` (Python CLI + Gradio WebUI + REST API) - Totalmente headless. Permite plugar a síntese em qualquer reprodutor de áudio corporativo ou aplicativo mobile da empresa.

**Uso Complementar & Ecossistema Agêntico:**
- **MCP Server:** `xtts-mcp-server` (`npx -y @coqui/xtts-mcp`) - Servidor MCP para delegar a agentes de IA a geração de áudios narrados em tempo de execução.
- **Agent Skill:** `skill-voice-cloner` (`.claude/skills/voice-cloner/SKILL.md`) - Skill para normalizar áudios de amostra (corte de silêncios, equalização e gating) antes da clonagem no XTTS.
- **Docker Container:** `xtts-api-server` (`docker run -d -p 8020:8020 --gpus all ghcr.io/daswer123/xtts-api-server`) - Servidor REST compatível com a API do ElevenLabs para migração de código existente apenas trocando a URL.

### #2 · OpenVoice v2 (Clonagem Instantânea com Controle de Estilo e Emoção) (*A Mais Completa*)

- **O Que Faz:** Permite clonagem de voz instantânea e desacoplamento de timbre e emoção: você pode aplicar a voz clonada falando com raiva, alegria, tristeza ou cochicho sem precisar de amostras emotivas do locutor original.
- **Como Funciona:** Desenvolvido pela MyShell e MIT. Separa o modelo base de fala (controlador de prosódia e sotaque) do extrator de embedding de tom (tone color converter), permitindo transferir qualquer timbre para qualquer estilo de fala.
- **Requisitos de Infra:** 4 GB RAM, 4 vCPU ou GPU 4 GB VRAM
- **Comando Rápido:** `git clone https://github.com/myshell-ai/OpenVoice && cd OpenVoice && pip install -r requirements.txt && python demo.py`
- **White-Label & Design System:** Esforço `Headless (API / CLI First)` (Python + PyTorch + Gradio) - Totalmente desacoplado de interfaces web fechadas, permitindo exportar arquivos de áudio padronizados prontos para uso em campanhas.

**Uso Complementar & Ecossistema Agêntico:**
- **Gradio App:** `openvoice-webui` (`python app.py`) - Interface gráfica amigável para testes de entonação e comparação de amostras de áudio lado a lado.
- **Agent Skill:** `skill-emotion-speech` (`.claude/skills/emotion-speech/SKILL.md`) - Skill para analisar o sentimento de um parágrafo de texto e ajustar a entonação do OpenVoice automaticamente.
- **REST Server:** `openvoice-api` (`python -m openvoice.server --port 8000`) - Servidor HTTP para integrar geração de vozes com esteiras de automação de vídeo e podcasts.

### #3 · ChatTTS (Conversação Natural & Sons Não-Verbais Realistas) (*A Mais Moderna*)

- **O Que Faz:** Modelo generativo especializado em diálogos conversacionais naturais. É capaz de reproduzir pausas naturais, respirações, risos, hesitações e suspiros, tornando a fala de assistentes indistinguível de um ser humano real.
- **Como Funciona:** Treinado em mais de 100.000 horas de fala em inglês e chinês com alta generalização. Utiliza marcadores especiais de texto como [laugh], [sigh] e [break] para injetar comportamento expressivo em tempo de síntese.
- **Requisitos de Infra:** 4 GB RAM, 4 vCPU ou GPU 4 GB VRAM
- **Comando Rápido:** `pip install ChatTTS && python -c "import ChatTTS; chat = ChatTTS.Chat(); chat.load(); wavs = chat.infer(['Olá, tudo bem? [laugh] Que bom falar com você!']);"`
- **White-Label & Design System:** Esforço `Headless (API / CLI First)` (PyTorch + Python + WebUI Integrada) - Totalmente programável via código, com saídas em formato WAV mono/estéreo sem marcas d'água de áudio.

**Uso Complementar & Ecossistema Agêntico:**
- **WebUI:** `chattts-ui` (`git clone https://github.com/jianchang512/ChatTTS-ui && cd ChatTTS-ui && python app.py`) - Interface gráfica completa com sliders para controle fino de risos, velocidade e tom de fala.
- **Agent Skill:** `skill-dialog-polisher` (`.claude/skills/dialog-polisher/SKILL.md`) - Skill para transformar respostas duras de LLM em roteiros conversacionais com tags de respiração do ChatTTS.
- **FastAPI Wrapper:** `chattts-api` (`uvicorn main:app --host 0.0.0.0 --port 8080`) - Wrapper de API de alta performance para atendimento telefônico e bots de suporte ao vivo.

### #4 · Piper TTS (Síntese Neural Ultra-Rápida para CPU & Dispositivos de Borda) (*A Mais Leve*)

- **O Que Faz:** Motor de síntese neural ultrarrápido projetado para rodar localmente em processadores comuns (CPU) e computadores de placa única (Raspberry Pi), sintetizando áudio até 10 vezes mais rápido que o tempo real.
- **Como Funciona:** Desenvolvido por Michael Hansen em C++ e Python sobre o motor VITS e ONNX Runtime. Consome menos de 50 MB de memória RAM e entrega vozes naturais em português do Brasil com zero latência perceptível.
- **Requisitos de Infra:** 256 MB RAM, 1 vCPU (Zero exigência de GPU)
- **Comando Rápido:** `echo 'Soberania digital com altíssima velocidade.' | piper --model pt_BR-faber-medium.onnx --output_file audio.wav`
- **White-Label & Design System:** Esforço `Headless (API / CLI First)` (C++ / ONNX Runtime + CLI Standalone) - Puramente headless. Permite que toda aplicação corporativa fale sem adicionar peso ou latência de rede.

**Uso Complementar & Ecossistema Agêntico:**
- **CLI Pipe:** `piper-pipe` (`echo 'Alerta do sistema' | piper -m voz.onnx -f saida.wav && aplay saida.wav`) - Execução instantânea de notificações de áudio diretamente no alto-falante do servidor.
- **Agent Skill:** `skill-piper-announcer` (`.claude/skills/piper-announcer/SKILL.md`) - Skill para converter resumos de notícias diárias em podcasts compactos utilizando o Piper.
- **Home Assistant Add-on:** `piper-ha` (`Instalação nativa via Home Assistant Community Store`) - Integração para alertas de voz residenciais e corporativos 100% offline em automação predial.

### #5 · Edge-TTS (Síntese Neural Gratuita em Python sem Chave de API) (*A Mais Simples*)

- **O Que Faz:** Biblioteca e utilitário de linha de comando em Python que permite sintetizar texto com as vozes neurais ultra-realistas da Microsoft (as mesmas vozes do Edge e Azure Speech) gratuitamente e sem chaves de API pagas.
- **Como Funciona:** Comunica-se diretamente via WebSockets criptografados com os endpoints de leitura em voz alta do navegador, suportando dezenas de vozes em português (Francisca, Antonio, Thalita) com ajuste de velocidade e tom.
- **Requisitos de Infra:** 128 MB RAM, 1 vCPU
- **Comando Rápido:** `pip install edge-tts && edge-tts --voice pt-BR-AntonioNeural --text 'Síntese de alta fidelidade sem gastar nada.' --write-media out.mp3`
- **White-Label & Design System:** Esforço `Headless (API / CLI First)` (Python AsyncIO + WebSockets) - Totalmente invisível na ponta final: os arquivos de áudio gerados são arquivos MP3 limpos prontos para edição de vídeo ou publicação.

**Uso Complementar & Ecossistema Agêntico:**
- **CLI Tool:** `edge-playback` (`edge-playback --voice pt-BR-FranciscaNeural --text 'Executando comando com sucesso'`) - Reproduz o áudio sintetizado diretamente nos fones de ouvido sem precisar salvar o arquivo intermediário.
- **Agent Skill:** `skill-edge-narrator` (`.claude/skills/edge-narrator/SKILL.md`) - Skill para transformar relatórios de sprint gerados por agentes em áudio narrado compartilhado com o time.
- **Subtitle Generator:** `edge-tts-srt` (`edge-tts --text 'Texto' --write-subtitles legendas.vtt`) - Gera simultaneamente o áudio falado e o arquivo de legendas com marcação precisa de tempo por palavra.

---

## 3. Matriz de Decisão & Migração Soberana

Para substituir integralmente o **ElevenLabs (Generative Voice AI & Voice Cloning)**, recomenda-se a esteira automatizada de implantação em VPS com os manuais operacionais disponíveis em `output/`.