# Dossiê Vertical de Desmantelamento SaaS: Claude Team / Claude Projects (Anthropic Commercial Workspaces)

> **Padrão Diamante R5-V · Quinteto Soberano Open Source**  
> **Alvo SaaS:** Claude Team / Claude Projects (Anthropic Commercial Workspaces) | **Custo Médio:** US$ 300 a US$ 360/ano por usuário (com mínimo de 5 assentos obrigatórios, totalizando mais de US$ 1.500/ano) | **Risco de Privacidade:** Projetos estratégicos, documentação interna sigilosa e bases de código proprietárias compartilhadas com servidores centrais da Anthropic.  

---

## 1. O Quinteto Soberano Open Source

| Rank | Classificação | Ferramenta | Licença | Repositório | Economia Estimada |
| :---: | :--- | :--- | :---: | :--- | :--- |
| **#1** | *A Mais Robusta* | **LibreChat (O Workspace Colaborativo Aberto #1 com Suporte a Artefatos e Forks)** | `MIT` | [https://github.com/danny-avila/LibreChat](https://github.com/danny-avila/LibreChat) | R$ 15.000/ano |
| **#2** | *A Mais Completa* | **Open WebUI (A Central Soberana com RAG Corporativo e Pipelines de IA)** | `GPL-3.0` | [https://github.com/open-webui/open-webui](https://github.com/open-webui/open-webui) | R$ 18.000/ano |
| **#3** | *A Mais Moderna* | **Dify.ai (A Plataforma Aberta de Agentes e Orquestração de Fluxos LLM)** | `Apache-2.0` | [https://github.com/langgenius/dify](https://github.com/langgenius/dify) | R$ 21.600/ano |
| **#4** | *A Mais Leve* | **Chatbox (O Aplicativo Desktop e Móvel Ágil para Times Conectados)** | `GPL-3.0` | [https://github.com/Bin-Huang/chatbox](https://github.com/Bin-Huang/chatbox) | R$ 7.200/ano |
| **#5** | *A Mais Simples* | **NextChat (O Cliente Web Ultraleve com Deploy em 1 Clique)** | `MIT` | [https://github.com/ChatGPTNextWeb/NextChat](https://github.com/ChatGPTNextWeb/NextChat) | R$ 4.800/ano |

---

## 2. Detalhamento Técnico das Ferramentas do Quinteto

### #1 · LibreChat (O Workspace Colaborativo Aberto #1 com Suporte a Artefatos e Forks) (*A Mais Robusta*)

- **O Que Faz:** A plataforma aberta mais avançada para colaboração com IA: interface idêntica ao Claude e ChatGPT, renderização de Artefatos de código interativos em tempo real (HTML, React, SVG), bifurcação de árvores de conversa (branching/forks), busca multimodal e agentes customizados com arquivos anexados por projeto.
- **Como Funciona:** Arquitetura corporativa em Node.js (Express), React e Tailwind CSS com banco MongoDB e Redis. Permite conectar chaves de API da Anthropic, OpenAI, Google Gemini e provedores locais (Ollama, vLLM) no mesmo workspace.
- **Requisitos de Infra:** 2 GB RAM, 2 vCPU
- **Comando Rápido:** `git clone https://github.com/danny-avila/LibreChat && cd LibreChat && docker compose up -d`
- **White-Label & Design System:** Esforço `Mínimo (Plug & Play)` (React + Tailwind CSS + Lucide Icons) - Interface visual moderna de nível internacional com modo escuro nativo e suporte a logotipo corporativo.

**Uso Complementar & Ecossistema Agêntico:**
- **MCP Server Integration:** `librechat-mcp` (`Configuração nativa de servidores MCP no librechat.yaml`) - Conexão de agentes do LibreChat a bancos de dados, APIs de CRM e ferramentas do sistema operacional.
- **Agent Skill:** `skill-librechat-config-master` (`.claude/skills/librechat-config-master/SKILL.md`) - Skill para estruturar arquivos librechat.yaml com controle estrito de cotas de saldo por usuário.
- **SSO / OIDC Auth:** `librechat-sso` (`Autenticação corporativa via Google Workspace, GitHub ou Keycloak`) - Login único e seguro para todos os funcionários da empresa sem necessidade de novas senhas.

### #2 · Open WebUI (A Central Soberana com RAG Corporativo e Pipelines de IA) (*A Mais Completa*)

- **O Que Faz:** Suíte aberta completa para trabalho em equipe com IA: gerenciamento de documentos com busca semântica vetorial (RAG) integrada, arena de comparação lado a lado de múltiplos modelos e controle de acesso granular com permissões de administrador.
- **Como Funciona:** Desenvolvido em SvelteKit e Python (FastAPI) com banco SQLite/PostgreSQL e ChromaDB para vetores. Conecta-se instantaneamente a instâncias do Ollama e APIs remotas, oferecendo um ecossistema de funções e filtros em Python (Pipelines).
- **Requisitos de Infra:** 4 GB RAM, 2 vCPU
- **Comando Rápido:** `docker run -d -p 3000:8080 -v open-webui:/app/backend/data --name open-webui ghcr.io/open-webui/open-webui:main`
- **White-Label & Design System:** Esforço `Mínimo (Plug & Play)` (SvelteKit + Tailwind CSS + Python FastAPI) - Customização completa de logotipo, mensagem de boas-vindas e cores do tema diretamente pelo painel administrativo.

**Uso Complementar & Ecossistema Agêntico:**
- **Pipelines Framework:** `openwebui-pipelines` (`git clone https://github.com/open-webui/pipelines`) - Framework modular em Python para injetar filtros de segurança, busca na web e lógica de negócios.
- **Agent Skill:** `skill-openwebui-doc-preparer` (`.claude/skills/openwebui-doc-preparer/SKILL.md`) - Skill para formatar e otimizar documentos antes da inserção na base de RAG do Open WebUI.
- **Voice Interactivity:** `openwebui-voice` (`Suporte nativo a Whisper (STT) e Piper/OpenAI (TTS)`) - Conversação por voz em tempo real diretamente pelo microfone do navegador.

### #3 · Dify.ai (A Plataforma Aberta de Agentes e Orquestração de Fluxos LLM) (*A Mais Moderna*)

- **O Que Faz:** Plataforma visual de desenvolvimento de aplicações e assistentes de IA: construtor visual de fluxos em nós, orquestração de múltiplos agentes conversacionais, RAG corporativo avançado e publicação de aplicativos de chat prontos com 1 clique.
- **Como Funciona:** Arquitetura moderna baseada em microsserviços em Python (Flask) e Next.js com PostgreSQL, Redis e Qdrant/Weaviate. Suporta centenas de modelos de IA e permite criar lógicas de decisão complexas antes de responder ao usuário.
- **Requisitos de Infra:** 8 GB RAM, 4 vCPU
- **Comando Rápido:** `git clone https://github.com/langgenius/dify.git && cd dify/docker && docker compose up -d`
- **White-Label & Design System:** Esforço `Mínimo (Plug & Play)` (Next.js + Tailwind CSS + React Flow) - Módulo de personalização do WebApp com escolha de cores, títulos institucionais e logotipo corporativo.

**Uso Complementar & Ecossistema Agêntico:**
- **API Access:** `dify-app-api` (`curl -X POST https://dify.empresa.com/v1/chat-messages`) - API REST padronizada para integrar os agentes do Dify diretamente no ERP ou CRM corporativo.
- **Agent Skill:** `skill-dify-dsl-generator` (`.claude/skills/dify-dsl-generator/SKILL.md`) - Skill para escrever e importar fluxos complexos em arquivos DSL (YAML) no Dify.
- **Tool Extensions:** `dify-tools` (`Integrações nativas com Google Search, WolframAlpha e Webhooks`) - Capacitação de assistentes para navegar na internet e consultar bancos em tempo real.

### #4 · Chatbox (O Aplicativo Desktop e Móvel Ágil para Times Conectados) (*A Mais Leve*)

- **O Que Faz:** Aplicativo nativo para desktop (Windows, Mac, Linux) e celular (iOS e Android) que permite conversar com Claude, GPT-4o, DeepSeek e modelos locais com extrema leveza, organização por abas e busca no histórico.
- **Como Funciona:** Desenvolvido em Electron e React com armazenamento local SQLite/IndexedDB. Seus dados ficam salvos exclusivamente no disco da sua máquina sem passar por nenhum servidor central de terceiros.
- **Requisitos de Infra:** 256 MB RAM, 1 vCPU
- **Comando Rápido:** `winget install BinHuang.Chatbox || brew install --cask chatbox`
- **White-Label & Design System:** Esforço `Mínimo (Plug & Play)` (Electron + React + Tailwind CSS) - Interface visual moderna com suporte a temas claros e escuros e zero rastreamento de uso.

**Uso Complementar & Ecossistema Agêntico:**
- **Cloud Sync:** `chatbox-webdav` (`Sincronização de conversas via WebDAV privado`) - Sincronização segura do histórico de conversas entre o computador do trabalho e o notebook pessoal.
- **Agent Skill:** `skill-chatbox-prompt-exporter` (`.claude/skills/chatbox-prompt-exporter/SKILL.md`) - Skill para exportar bibliotecas de prompts padronizadas em JSON para distribuição na equipe.
- **Artifacts Preview:** `chatbox-preview` (`Visualizador de código e renderizador Markdown embutido`) - Destaque de sintaxe perfeito e pré-visualização de tabelas e blocos de código.

### #5 · NextChat (O Cliente Web Ultraleve com Deploy em 1 Clique) (*A Mais Simples*)

- **O Que Faz:** A interface web mais popular e simples para uso de IA generativa: sobe em qualquer servidor estático ou contêiner em menos de 10 segundos, com suporte a proteção por senha de acesso, máscaras de personagens e exportação de conversas em imagem ou Markdown.
- **Como Funciona:** Desenvolvido em Next.js e TypeScript com Tailwind CSS. Não requer banco de dados: salva todo o histórico localmente no navegador do usuário e faz proxy direto e seguro para os provedores de modelos.
- **Requisitos de Infra:** 128 MB RAM, 1 vCPU
- **Comando Rápido:** `docker run -d -p 3000:3000 -e CODE=senha_da_equipe -e ANTHROPIC_API_KEY=sua_chave yidadaa/chatgpt-next-web`
- **White-Label & Design System:** Esforço `Mínimo (Plug & Play)` (Next.js + React + Tailwind CSS) - Design refinado inspirado no estilo visual da Apple sob licença permissiva MIT.

**Uso Complementar & Ecossistema Agêntico:**
- **Masks Library:** `nextchat-masks` (`Biblioteca de máscaras embutida`) - Mais de 100 papéis pré-configurados (Especialista em SEO, Engenheiro de Software, Consultor Financeiro).
- **Agent Skill:** `skill-nextchat-prompt-curator` (`.claude/skills/nextchat-prompt-curator/SKILL.md`) - Skill para compilar máscaras de atendimento customizadas para o time no formato do NextChat.
- **PWA Mode:** `nextchat-pwa` (`Instalação PWA no celular e desktop`) - Uso como aplicativo independente na tela inicial do celular com atalho direto.

---

## 3. Matriz de Decisão & Migração Soberana

Para substituir integralmente o **Claude Team / Claude Projects (Anthropic Commercial Workspaces)**, recomenda-se a esteira automatizada de implantação em VPS com os manuais operacionais disponíveis em `output/`.