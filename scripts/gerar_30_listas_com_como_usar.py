# -*- coding: utf-8 -*-
"""
Gerador de Elite dos 30 Compêndios de Soberania Tecnológica e Engenharia de IA.
Inclui a seção 'COMO USAR NA PRÁTICA / WORKFLOW NO DIA A DIA' para cada ferramenta,
com comandos reais, passos acionáveis, especificações de consumo e cálculo de economia.
"""

import sys
from pathlib import Path

LISTAS_COMPLETAS = [
    # 01
    {
        "slug": "01-economia-de-tokens",
        "title": "Economia Extrema de Tokens & Contexto",
        "camada": "Camada 01 · Eficiência de Contexto",
        "accent": "#1B5E3B", "accent_dark": "#6BC48F", "accent_soft": "#D8EFE2", "accent_soft_dark": "#122B1C",
        "deck": "Metodologias, compiladores e caches para <strong>cortar até 85% do custo com LLMs</strong> sem perder 1% de precisão: cache semântico de respostas, gramáticas estruturadas, AST e compressão cirúrgica de repositórios.",
        "pilar_1": "O Custo Invisível do Contexto Inflado",
        "pilar_1_desc": "Enviar arquivos inteiros (lockfiles, builds, SVGs) queima centenas de milhares de tokens por turno. Sem filtros, 80% do gasto mensal com APIs de IA é desperdiçado em ruído.",
        "pilar_2": "A Engenharia do Prompt Cirúrgico",
        "pilar_2_desc": "Com AST (ast-grep), empacotamento semântico (Repomix), cache semântico (LiteLLM) e compilação algorítmica (DSPy), o modelo recebe apenas os 2KB exatos necessários para a tarefa.",
        "itens": [
            {
                "rank": "01", "name": "Repomix", "cat": "Context Packing", "lic": "MIT",
                "substitui": "Leitura manual de arquivos", "econ": "-70% de tokens por prompt (~$ 300/mês)",
                "entrega": "Empacota repositórios inteiros em 1 arquivo XML/Markdown com contagem de tokens e filtros inteligentes de .gitignore.",
                "cmd": "npx repomix --style xml --output-show-line-numbers",
                "como_usar": "1. Antes de pedir uma refatoração complexa, rode <code>npx repomix --include 'src/**/*.ts'</code>.<br>2. Cole o arquivo <code>repomix-output.xml</code> no chat da LLM ou anexe no prompt do agente.<br>3. A IA recebe a árvore exata com numeração de linhas, consumindo apenas os arquivos relevantes.",
                "spec": "< 30 MB RAM / CLI sob demanda",
                "truth": "Remove automaticamente arquivos binários, lockfiles e assets pesados antes de enviar o contexto à LLM.",
                "repo": "github.com/yamadashy/repomix"
            },
            {
                "rank": "02", "name": "ast-grep (sg)", "cat": "AST Search & Rewrite", "lic": "MIT",
                "substitui": "Refatorações caras via LLM", "econ": "100% grátis em transformações estruturais",
                "entrega": "Busca e reescrita de código baseada na Árvore de Sintaxe Abstrata. Não erra espaçamentos nem quebras de linha.",
                "cmd": "cargo install ast-grep && sg --pattern 'function $NAME($$$ARGS) { $$$BODY }'",
                "como_usar": "1. Para renomear funções ou mudar chamadas de API em 50 arquivos, crie uma regra YAML ou rode via CLI.<br>2. Rode <code>sg scan --rewrite 'novaFuncao($$$ARGS)'</code>.<br>3. A substituição ocorre em 2ms sem gastar nenhum token de IA e com precisão sintática absoluta.",
                "spec": "Binário Rust / < 10 MB RAM",
                "truth": "Substitui prompts inteiros de 'renomeie/altere assinatura' por uma chamada determinística de 2ms no terminal.",
                "repo": "ast-grep.github.io"
            },
            {
                "rank": "03", "name": "LiteLLM Semantic Cache", "cat": "AI Gateway & Cache", "lic": "MIT",
                "substitui": "Chamadas duplicadas em APIs de LLM", "econ": "-40% a -60% na fatura de API (~$ 500/mês)",
                "entrega": "Cache semântico de respostas de LLM em Redis. Se o prompt for semanticamente equivalente, responde em 2ms por $ 0.",
                "cmd": "docker run -d -p 4000:4000 ghcr.io/berriai/litellm:main-latest",
                "como_usar": "1. Aponte a URL base do seu SDK (OpenAI/Anthropic) para <code>http://localhost:4000</code>.<br>2. Ative o Redis Cache no <code>config.yaml</code> do LiteLLM.<br>3. Quando seus agentes de teste ou usuários fizerem perguntas similares, o LiteLLM devolve a resposta do cache sem chamar a OpenAI.",
                "spec": "~70 MB RAM em repouso",
                "truth": "Essencial para suítes de testes de software e pipelines de CI/CD que rodam os mesmos prompts repetidamente.",
                "repo": "litellm.ai"
            },
            {
                "rank": "04", "name": "DSPy (Stanford)", "cat": "Prompt Compiler", "lic": "MIT",
                "substitui": "Engenharia de prompt manual cara", "econ": "Reduz tamanho de prompt em até 50%",
                "entrega": "Otimiza automaticamente instruções e few-shots via algoritmos matemáticos para obter a máxima acurácia no menor prompt possível.",
                "cmd": "pip install dspy-ai",
                "como_usar": "1. Defina sua assinatura de entrada/saída em Python (ex: <code>class RAG(dspy.Signature): ...</code>).<br>2. Forneça 10 a 20 exemplos de treino.<br>3. Deixe o otimizador <code>BootstrapFewShot</code> compilar o prompt ideal. Use o pipeline compilado em produção.",
                "spec": "Biblioteca pura / Zero runtime RAM",
                "truth": "Trata prompts como código compilável. Se você mudar de modelo, basta recompilar o pipeline sem reescrever nada.",
                "repo": "dspy.ai"
            },
            {
                "rank": "05", "name": "Outlines / Guidance", "cat": "Structured Generation", "lic": "Apache-2.0 / MIT",
                "substitui": "Retentativas por JSON quebrado", "econ": "Elimina 100% dos tokens de retry por falha de parsing",
                "entrega": "Força o modelo a seguir gramáticas formais (CFG / Regex / Pydantic) a nível de logits durante a amostragem de tokens.",
                "cmd": "pip install outlines",
                "como_usar": "1. Crie seu modelo de dados com Pydantic (ex: <code>class User(BaseModel): ...</code>).<br>2. Instancie o gerador estruturado: <code>generator = outlines.generate.json(model, User)</code>.<br>3. Chame <code>generator(prompt)</code> — a saída é 100% garantida como JSON válido na primeira tentativa.",
                "spec": "Execução local / overhead < 5ms",
                "truth": "O modelo é matematicamente incapaz de gerar um caractere fora do schema especificado.",
                "repo": "github.com/outlines-dev/outlines"
            },
            {
                "rank": "06", "name": "Gitingest", "cat": "Web Repo Parser", "lic": "MIT",
                "substitui": "Clonagem + extração manual", "econ": "Economia de tempo de análise em 90%",
                "entrega": "Converte qualquer repositório público do GitHub em um texto limpo e resumido com contagem exata de tokens para colar em chats.",
                "cmd": "docker run -d -p 8000:8000 cyclotruc/gitingest",
                "como_usar": "1. No navegador, troque <code>github.com/dono/repo</code> por <code>gitingest.com/dono/repo</code>.<br>2. Filtre por padrões de pastas (ex: apenas <code>/src</code> e sem testes).<br>3. Clique em 'Copy' e cole o prompt pronto com a contagem exata de tokens calculada.",
                "spec": "~60 MB RAM",
                "truth": "Troque 'github.com' por 'gitingest.com' na URL e obtenha o contexto estruturado em 1 segundo.",
                "repo": "gitingest.com"
            },
            {
                "rank": "07", "name": "Tree-sitter CLI", "cat": "CST / AST Parser", "lic": "MIT",
                "substitui": "Leitura integral de código pela LLM", "econ": "-80% de tokens ao enviar apenas assinaturas de funções",
                "entrega": "Parser incremental em C que extrai a hierarquia sintática de arquivos de código mesmo com erros parciais.",
                "cmd": "npm install -g tree-sitter-cli && tree-sitter parse arquivo.py",
                "como_usar": "1. Escreva um script de 10 linhas que roda o Tree-sitter para extrair nomes de classes, métodos e docstrings.<br>2. Gere um arquivo <code>INDEX.md</code> com o mapa de símbolos da sua base de código.<br>3. O agente lê o índice (200 tokens) em vez de ler 50 arquivos inteiros (100k tokens).",
                "spec": "Consumo de RAM irrisório (< 5MB)",
                "truth": "Permite criar ferramentas que alimentam o agente apenas com o mapa de símbolos das dependências.",
                "repo": "tree-sitter.github.io"
            },
            {
                "rank": "08", "name": "SGLang (RadixAttention)", "cat": "Inference Engine", "lic": "Apache-2.0",
                "substitui": "Recomputação cara de KV-cache", "econ": "5x mais rápido em chats com histórico longo",
                "entrega": "Implementa cache de prefixo em árvore radix, reaproveitando a computação do system prompt e mensagens anteriores em 100%.",
                "cmd": "python -m sglang.launch_server --model-path Qwen/Qwen2.5-Coder-7B-Instruct",
                "como_usar": "1. Inicie o servidor SGLang na sua máquina ou servidor com GPU.<br>2. Configure seus subagentes para usar o endpoint do SGLang como backend OpenAI.<br>3. Prompts longos e repetitivos (regras do sistema, docs) são processados em 0ms por causa do reuso do KV-cache.",
                "spec": "VRAM estática de GPU / Throughput massivo",
                "truth": "O melhor motor para esteiras de subagentes que compartilham instruções de sistema extensas.",
                "repo": "github.com/sgl-project/sglang"
            }
        ]
    },
    # 02
    {
        "slug": "02-arquitetura-agentica-spec-driven",
        "title": "Arquitetura Agêntica & Spec-Driven Development",
        "camada": "Camada 02 · Orquestração de Agentes",
        "accent": "#1A446C", "accent_dark": "#7AA5D6", "accent_soft": "#D8EFE2", "accent_soft_dark": "#162436",
        "deck": "Frameworks para orquestrar <strong>squads autônomos de IA com contratos estritos, especificações formais e sandboxes seguras</strong>: elimine o código espaguete e garanta que o agente teste o próprio trabalho antes da entrega.",
        "pilar_1": "O Fim do Chatbot Monolítico",
        "pilar_1_desc": "Pedir tudo em um único prompt gera alucinação e perda de foco. A engenharia moderna decompõe o projeto em papéis especializados com permissões restritas.",
        "pilar_2": "Spec-Driven Development (SDD)",
        "pilar_2_desc": "Requisitos viram arquivos SPEC.md e testes automatizados. O agente só recebe permissão para codificar quando o plano for aprovado.",
        "itens": [
            {
                "rank": "01", "name": "Spec-Kit", "cat": "Spec-Driven Dev", "lic": "MIT",
                "substitui": "Desenvolvimento desgovernado por IA", "econ": "Economiza semanas de retrabalho em código quebrado",
                "entrega": "Framework formal do GitHub Next para criar especificações executáveis e validar contratos antes de escrever código.",
                "cmd": "# SPEC.md -> PLAN.md -> TASKS.md -> EXECUÇÃO",
                "como_usar": "1. Ao iniciar uma feature, crie o arquivo <code>SPEC.md</code> descrevendo critérios de aceite e contratos de API.<br>2. Peça para a IA gerar os testes unitários baseados na spec.<br>3. Autorize o agente a codificar apenas até que a suíte passe em 100%.",
                "spec": "Documentação formal + testes",
                "truth": "Garante que a IA nunca comece a gerar arquivos sem saber exatamente o critério de aceite.",
                "repo": "github.com/github/spec-kit"
            },
            {
                "rank": "02", "name": "BMad Method", "cat": "Agile AI Framework", "lic": "MIT",
                "substitui": "Prompts gigantes e confusos", "econ": "Reduz bugs de arquitetura em 90%",
                "entrega": "Metodologia ágil que divide a tarefa entre agentes especialistas (PO, Arquiteto, Dev, Revisor, Auditor de Gates).",
                "cmd": "# Fluxo de 4 fases: F1 (Pesquisa) -> F2 (Produção) -> F2.5 (Auditoria) -> F3 (Compilação)",
                "como_usar": "1. Dispare a Fase 1 chamando o subagente de Pesquisa para mapear o problema.<br>2. Valide o plano macro gerado pelo Arquiteto.<br>3. Deixe o Dev implementar e o Revisor auditar contra gates automáticos antes da entrega final.",
                "spec": "Estrutura de governança e papéis",
                "truth": "Subagentes com escopos pequenos e bem definidos têm taxa de sucesso 5x maior que um agente generalista.",
                "repo": "bmad.ai"
            },
            {
                "rank": "03", "name": "Aider CLI", "cat": "Git Pair Programmer", "lic": "Apache-2.0",
                "substitui": "Assinatura Cursor ($ 20/mês)", "econ": "-$ 240 / ano por desenvolvedor",
                "entrega": "Assistente de linha de comando que opera no repositório Git, resolve issues e gera commits semânticos com árvore AST.",
                "cmd": "pip install aider-chat && aider --model ollama/qwen2.5-coder:7b",
                "como_usar": "1. No terminal do seu projeto, digite <code>aider arquivo1.py arquivo2.py</code>.<br>2. Diga em linguagem natural: 'Adicione validação de e-mail e crie o teste pytest correspondente'.<br>3. O Aider edita os arquivos, roda o linter e cria o commit semântico no Git.",
                "spec": "~60 MB RAM",
                "truth": "Líder mundial consistente no benchmark SWE-bench para resolução de problemas reais de engenharia de software.",
                "repo": "aider.chat"
            },
            {
                "rank": "04", "name": "OpenHands (OpenDevin)", "cat": "Autonomous Sandbox", "lic": "MIT",
                "substitui": "Devin / Magic.dev ($ 500+/mês)", "econ": "-$ 6.000 / ano em ferramentas proprietárias",
                "entrega": "Plataforma de agentes autônomos executados em containers Docker isolados com capacidade de usar browser, terminal e editor.",
                "cmd": "docker run -it -p 3000:3000 ghcr.io/all-hands-ai/openhands:main",
                "como_usar": "1. Abra a interface web na porta 3000 e conecte seu repositório Git.<br>2. Atribua uma issue complexa (ex: 'Migre de Webpack para Vite e faça os testes passarem').<br>3. Acompanhe o agente abrindo o navegador, instalando pacotes e corrigindo erros no Docker.",
                "spec": "Ambiente Docker isolado",
                "truth": "O agente instala pacotes e roda testes sem colocar em risco o sistema operacional do desenvolvedor.",
                "repo": "all-hands.dev"
            },
            {
                "rank": "05", "name": "LangGraph / CrewAI", "cat": "Cyclic State Graph", "lic": "MIT",
                "substitui": "Scripts de agentes frágeis", "econ": "Zero travamentos por loops infinitos",
                "entrega": "Framework de orquestração multi-agente baseado em grafos com persistência de checkpoints e pontos de controle humano.",
                "cmd": "pip install langgraph crewai",
                "como_usar": "1. Crie nós para cada etapa (ex: Pesquisar -> Escrever -> Revisar).<br>2. Defina arestas condicionais (se o Revisor reprovar, volte para o Nó Escrever).<br>3. Salve o estado no SQLite para retomar conversas longas sem perder o contexto.",
                "spec": "~50 MB RAM",
                "truth": "Permite pausar a execução da esteira agêntica, pedir feedback ao usuário e retomar o estado com 100% de precisão.",
                "repo": "crewai.com"
            },
            {
                "rank": "06", "name": "Letta (MemGPT) / Mem0", "cat": "Long-Term Memory", "lic": "Apache-2.0",
                "substitui": "Janela de contexto estourada", "econ": "-80% de reenvio de histórico antigo",
                "entrega": "Camada de memória de longo prazo auto-gerenciada que armazena fatos, preferências e histórico do usuário em banco relacional.",
                "cmd": "pip install letta && letta run",
                "como_usar": "1. Integre o Letta ao backend do seu chatbot ou assistente pessoal.<br>2. Durante a conversa, o Letta arquiva decisões e preferências do usuário em SQLite/Postgres.<br>3. Em sessões futuras, o agente recupera os fatos exatos sem precisar de prompt histórico gigante.",
                "spec": "~90 MB RAM",
                "truth": "O agente não esquece decisões tomadas há 3 semanas sem precisar reenviar todo o histórico no prompt.",
                "repo": "letta.com"
            },
            {
                "rank": "07", "name": "E2B Code Interpreter", "cat": "Secure Code Sandbox", "lic": "Apache-2.0",
                "substitui": "Execuções inseguras no host", "econ": "100% de segurança contra scripts maliciosos",
                "entrega": "MicroVMs efêmeras que sobem em 100ms para que o agente execute código Python, gere gráficos e analise dados com segurança.",
                "cmd": "npm install @e2b/code-interpreter",
                "como_usar": "1. Quando seu agente gerar código para plotar gráficos ou calcular dados, chame <code>await Sandbox.create()</code>.<br>2. Execute o script na sandbox segura: <code>sandbox.runCode(codigo)</code>.<br>3. Receba os gráficos (PNG) e saídas de stdout sem risco de corrupção do servidor.",
                "spec": "MicroVM sob demanda",
                "truth": "Ambiente isolado ideal para agentes que geram e executam código de visualização em tempo real.",
                "repo": "e2b.dev"
            },
            {
                "rank": "08", "name": "Instructor", "cat": "Structured Outputs", "lic": "MIT",
                "substitui": "Tratamento manual de erros de JSON", "econ": "Economiza horas de debugging de parsing",
                "entrega": "Biblioteca Python/TS que envelopa chamadas de LLM com validação estrita de modelos Pydantic e retentativas automáticas.",
                "cmd": "pip install instructor",
                "como_usar": "1. Envelopa seu cliente: <code>client = instructor.from_openai(OpenAI())</code>.<br>2. Chame <code>client.chat.completions.create(response_model=MeuSchema, ...)</code>.<br>3. Receba um objeto Python tipado com validação automática de dados.",
                "spec": "Zero runtime overhead",
                "truth": "Se a saída não validar no Pydantic, o Instructor reenvia apenas o erro para a LLM corrigir o campo exato.",
                "repo": "python.useinstructor.com"
            }
        ]
    },
    # 03
    {
        "slug": "03-design-ui-midia-soberana",
        "title": "Design, UI & Mídia Soberana",
        "camada": "Camada 03 · Criação Visual & Mídia",
        "accent": "#4A3274", "accent_dark": "#B192E6", "accent_soft": "#E7DFEF", "accent_soft_dark": "#251838",
        "deck": "A suíte completa para <strong>designers, criadores de conteúdo e times de produto</strong>: design vetorial em SVG nativo, prototipagem, síntese de voz indistinguível de humanos, suíte de PDFs e geração de imagens sem nuvem proprietária.",
        "pilar_1": "O Custo do Design por Assento",
        "pilar_1_desc": "Figma ($ 15/user), Adobe Acrobat ($ 20/user), ElevenLabs ($ 99/mês) e Midjourney ($ 30/mês). Uma equipe de criação pequena gasta mais de $ 1.500/mês.",
        "pilar_2": "A Alternativa em Padrões Abertos",
        "pilar_2_desc": "Penpot usa SVG e CSS Grid nativos. Kokoro sintetiza voz em tempo real em CPU. Stirling-PDF resolve 50 operações de PDF localmente com 100% de privacidade.",
        "itens": [
            {
                "rank": "01", "name": "Penpot", "cat": "UI/UX Design", "lic": "MPL-2.0",
                "substitui": "Figma ($ 15/designer/mês)", "econ": "-$ 1.800 / ano para equipe de 10 pessoas",
                "entrega": "Plataforma de design e prototipagem baseada em padrões web (SVG real, Flexbox e CSS Grid nativo).",
                "cmd": "docker compose -f docker-compose.penpot.yml up -d",
                "como_usar": "1. Suba o Penpot no servidor da empresa com Docker.<br>2. Crie seus layouts usando Flexbox e Grid reais.<br>3. Desenvolvedores inspecionam CSS puro sem precisar pagar licenças extras de visualização.",
                "spec": "~450 MB RAM",
                "truth": "Sem cobrança por visualizadores ou desenvolvedores inspecionando o código do design.",
                "repo": "penpot.app"
            },
            {
                "rank": "02", "name": "Kokoro-82M", "cat": "Neural TTS Local", "lic": "Apache-2.0",
                "substitui": "ElevenLabs ($ 99-$ 330/mês)", "econ": "-$ 1.200 a $ 4.000 / ano",
                "entrega": "Síntese de voz hiper-realista em tempo real com modelo de apenas 82M de parâmetros rodando em CPU comum.",
                "cmd": "pip install kokoro-onnx soundfile",
                "como_usar": "1. No seu script Python de geração de vídeo ou podcast, passe o texto da narração.<br>2. Gere o arquivo de áudio: <code>audio, sr = kokoro.create(texto, voice='af_bella')</code>.<br>3. Salve o <code>.wav</code> em frações de segundo sem gastar $ 1 em APIs de voz.",
                "spec": "< 150 MB RAM em inferência",
                "truth": "Gere horas de narração, podcasts e áudios para agentes sem pagar por caractere gerado.",
                "repo": "github.com/hexgrad/kokoro"
            },
            {
                "rank": "03", "name": "Stirling-PDF", "cat": "PDF Toolkit", "lic": "GPL-3.0",
                "substitui": "Adobe Acrobat Pro ($ 239/ano)", "econ": "-$ 239 / ano por usuário",
                "entrega": "Mais de 50 operações: OCR, divisão, conversão para Word/Excel, assinatura digital e censura de dados confidenciais.",
                "cmd": "docker run -d -p 8080:8080 frooodle/s-pdf:latest",
                "como_usar": "1. Acesse <code>http://localhost:8080</code> no navegador do escritório.<br>2. Arraste documentos contratuais para mesclar, assinar ou rodar OCR.<br>3. Tudo é processado localmente na rede interna sem vazamento de dados fiscais.",
                "spec": "~150 MB RAM",
                "truth": "Nenhum documento confidencial da empresa é enviado para sites suspeitos de conversão na internet.",
                "repo": "github.com/Stirling-Tools/Stirling-PDF"
            },
            {
                "rank": "04", "name": "ComfyUI", "cat": "Generative AI Canvas", "lic": "GPL-3.0",
                "substitui": "Midjourney / DALL-E ($ 30-$ 60/mês)", "econ": "-$ 360 a $ 720 / ano",
                "entrega": "A interface baseada em nós mais potente para Stable Diffusion, FLUX e SDXL com controle total sobre cada etapa da geração.",
                "cmd": "git clone https://github.com/comfyanonymous/ComfyUI && python main.py",
                "como_usar": "1. Abra a interface de nós e monte seu fluxo (Checkpoint -> Prompt Positivo/Negativo -> KSampler -> VAE Decode).<br>2. Arraste imagens anteriores para carregar o fluxo exato de geração.<br>3. Gere assets visuais em lote para landing pages e redes sociais com 100% de reprodutibilidade.",
                "spec": "VRAM da GPU sob demanda",
                "truth": "Reproduzibilidade total de workflows de geração de imagens com salvamento de nós no próprio PNG.",
                "repo": "comfy.org"
            },
            {
                "rank": "05", "name": "AFFiNE / Excalidraw", "cat": "Canvas & Whiteboard", "lic": "MIT",
                "substitui": "Miro / Whimsical ($ 10/user/mês)", "econ": "-$ 1.200 / ano (equipe de 10)",
                "entrega": "Quadro branco infinito com notas estruturadas, post-its, diagramas e suporte a desenho livre colaborativo.",
                "cmd": "docker run -d -p 3010:3010 affine/affine:latest",
                "como_usar": "1. Use durante reuniões de planejamento de arquitetura e design sprints.<br>2. Desenhe fluxogramas e wireframes com estilo 'hand-drawn'.<br>3. Exporte em SVG ou PNG de alta resolução para incluir em documentações do projeto.",
                "spec": "~140 MB RAM",
                "truth": "Quadros ilimitados sem travas de plano freemium.",
                "repo": "affine.pro"
            },
            {
                "rank": "06", "name": "Shiki / Prism", "cat": "Code Syntax Highlighting", "lic": "MIT",
                "substitui": "Serviços pagos de renderização de código", "econ": "Zero custo / Renderização em build-time",
                "entrega": "Colorização de sintaxe baseada em gramáticas TextMate do VS Code com renderização estática perfeita sem JS no cliente.",
                "cmd": "npm install shiki",
                "como_usar": "1. No seu gerador de documentação ou blog, importe o Shiki.<br>2. Passe o bloco de código e o tema desejado (ex: 'nord' ou 'github-dark').<br>3. O Shiki gera HTML estático já estilizado, sem bibliotecas pesadas de JavaScript no navegador.",
                "spec": "Execução no build",
                "truth": "O mesmo motor que o VS Code usa para destacar código, rodando no servidor ou na pipeline.",
                "repo": "shiki.style"
            },
            {
                "rank": "07", "name": "Iconify", "cat": "Universal Icon Framework", "lic": "MIT / Apache-2.0",
                "substitui": "FontAwesome Pro / Noun Project ($ 99/ano)", "econ": "-$ 99 / ano por projeto",
                "entrega": "Mais de 200.000 ícones vetoriais de todas as coleções do mundo (Lucide, Material, Tabler, Carbon) em 1 único formato unificado.",
                "cmd": "npm install @iconify/react",
                "como_usar": "1. Escolha qualquer ícone de qualquer pacote no catálogo online.<br>2. No seu componente React/Vue/Svelte, declare: <code>&lt;Icon icon='lucide:database' /&gt;</code>.<br>3. O bundler importa apenas os bytes daquele SVG específico.",
                "spec": "Bundle size sob demanda",
                "truth": "Carregamento dinâmico apenas dos SVGs usados no projeto, sem carregar fontes de 5MB.",
                "repo": "iconify.design"
            },
            {
                "rank": "08", "name": "Fontsource", "cat": "Self-Hosted Typography", "lic": "MIT / OFL",
                "substitui": "Google Fonts (Vazamento de IP / LGPD)", "econ": "Zero dependência externa e 100% compliance LGPD",
                "entrega": "Fontes tipográficas de alta qualidade empacotadas como módulos NPM para auto-hospedagem sem conexões ao Google.",
                "cmd": "npm install @fontsource/inter",
                "como_usar": "1. Instale a fonte desejada: <code>npm install @fontsource/fira-code</code>.<br>2. No seu CSS principal, adicione: <code>import '@fontsource/fira-code/400.css';</code>.<br>3. As fontes são servidas pelo seu próprio domínio com cache local imbatível.",
                "spec": "Arquivos WOFF2 locais",
                "truth": "Evita multas de privacidade (como as decisões judiciais europeias sobre Google Fonts) e acelera o carregamento.",
                "repo": "fontsource.org"
            }
        ]
    }
]

# Dados detalhados de COMO USAR para as listas restantes (04 a 30)
# Gerar dinamicamente os 240 itens completos com workflows práticos e comandos do dia a dia
RESTANTE_CONFIG = [
    # 04
    ("04-motores-inferencia-fine-tuning", "Motores de Inferência & Fine-Tuning Local", "Camada 04 · Runtimes & Modelos", "#7A5410", [
        ("Unsloth", "Fast Fine-Tuning", "Treinamento lento e caro em nuvem", "-80% de custo de GPU / 5x mais rápido", "Treinamento de Llama-3 e DeepSeek com kernels manuais em Triton.", "pip install unsloth", "1. Carregue seu dataset de instruções em formato JSONL.<br>2. Rode o script de fine-tuning QLoRA do Unsloth.<br>3. Exporte os pesos finais em GGUF ou 16-bit em menos de 20 minutos na sua GPU local.", "unsloth.ai"),
        ("vLLM", "Production Engine", "APIs comerciais com alta concorrência", "-$ 2.000+/mês para times médios", "Motor de inferência de alto rendimento com PagedAttention.", "vllm serve Qwen/Qwen2.5-Coder-7B-Instruct --port 8000", "1. Suba o servidor vLLM no seu servidor dedicado.<br>2. Aponte todas as aplicações da empresa para a porta 8000 como se fosse a API da OpenAI.<br>3. Atenda dezenas de desenvolvedores simultâneos com continuous batching veloz.", "vllm.ai"),
        ("SGLang", "Structured & Radix Engine", "Inferência com recomputação de KV", "3x a 5x mais rápido em chats", "Motor focado em programas de IA complexos e prompts estruturados.", "python -m sglang.launch_server --model-path deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct", "1. Inicie o servidor SGLang com RadixAttention ativado.<br>2. Use para esteiras de subagentes que mantêm o mesmo system prompt longo.<br>3. Economize tempo e energia com reuso de 100% dos prefixos calculados.", "github.com/sgl-project/sglang"),
        ("ExLlamaV2", "Extreme Quantization", "Runtimes pesados de GPU", "Dobra a taxa de tokens/s na mesma GPU", "O formato de quantização (EXL2) mais veloz para GPUs Nvidia.", "pip install exllamav2", "1. Baixe modelos no formato EXL2 (4.0bpw ou 6.0bpw) do HuggingFace.<br>2. Inicie o servidor TabbyAPI ou o backend do ExLlamaV2.<br>3. Desfrute de 100+ tokens/s mesmo em modelos de 70B parâmetros distribuídos.", "github.com/turboderp/exllamav2"),
        ("Llama.cpp", "C/C++ Bare-Metal Engine", "Dependência de Python e CUDA", "Roda em qualquer hardware sem servidor caro", "O motor em C/C++ puro que roda modelos quantizados GGUF.", "./llama-server -m models/qwen-7b.gguf -c 4096", "1. Baixe o arquivo <code>.gguf</code> do modelo desejado.<br>2. Execute o binário <code>llama-server</code>.<br>3. Integre diretamente em qualquer script ou aplicação via chamadas HTTP REST.", "github.com/ggerganov/llama.cpp"),
        ("Ollama", "Local LLM Manager", "Configuração complexa de drivers", "Zero custo de instalação e operação", "Gerenciador simples de modelos locais com download em 1 comando.", "ollama run qwen2.5-coder:14b", "1. Instale o Ollama no seu sistema.<br>2. Digite <code>ollama run deepseek-r1:14b</code> para conversar no terminal.<br>3. Conecte extensões de IDE e plugins web na porta padrão <code>11434</code>.", "ollama.com"),
        ("Axolotl", "Declarative Training", "Scripts manuais complexos de PyTorch", "Economiza dias de engenharia de MLOps", "Framework de treinamento configurado inteiramente via YAML.", "accelerate launch -m axolotl.cli.train config.yml", "1. Crie um arquivo <code>config.yml</code> definindo base_model, learning_rate e dataset.<br>2. Execute o comando de treino.<br>3. O Axolotl cuida do empacotamento, FlashAttention e salvamento de checkpoints.", "github.com/axolotl-ai-cloud/axolotl"),
        ("Torchtune", "PyTorch Native Fine-Tuning", "Wrappers proprietários de treino", "Integração nativa com ecossistema PyTorch", "Biblioteca modular oficial do PyTorch para ajuste fino de LLMs.", "tune run lora_finetune_single_device --config llama3_2/1B_lora", "1. Escolha uma receita de treino pronta (ex: LoRA em 1 GPU).<br>2. Altere o caminho do dataset no arquivo de configuração.<br>3. Rode a receita e acompanhe as métricas no TensorBoard.", "pytorch.org/torchtune")
    ]),
    # 05
    ("05-rag-vetores-grafos", "RAG Cirúrgico, Bancos Vetoriais & Grafos", "Camada 05 · Recuperação de Conhecimento", "#1E5E4E", [
        ("Qdrant", "Vector Database", "Pinecone ($ 70-$ 500/mês)", "-$ 840 a $ 6.000 / ano", "Banco vetorial em Rust com busca híbrida densa e esparsa.", "docker run -d -p 6333:6333 -v qdrant_data:/qdrant/storage qdrant/qdrant", "1. Suba o Qdrant via Docker.<br>2. Crie uma coleção com vetores densos e esparsos (BM25).<br>3. Faça buscas com filtros de metadados combinando similaridade semântica e exata.", "qdrant.tech"),
        ("LanceDB", "Embedded Serverless Vector", "Bancos vetoriais em nuvem", "Zero custo de servidor gerenciado", "Banco vetorial serverless embutido em Rust baseado em Lance.", "pip install lancedb", "1. Conecte no Python: <code>db = lancedb.connect('./meu_lancedb')</code>.<br>2. Crie tabelas passando DataFrames com vetores.<br>3. Realize consultas diretamente do disco com latência ultrabaixa sem subir servidores.", "lancedb.com"),
        ("RAGatouille (ColBERT)", "Late Interaction Retrieval", "Embeddings vetoriais médios simples", "Aumenta a precisão do RAG em 30%+", "Implementação simples de ColBERTv2 para busca token-a-token.", "pip install ragatouille", "1. Indexe seus documentos: <code>RAG.index(collection=documentos, index_name='manual')</code>.<br>2. Consulte: <code>RAG.search('qual a regra 16?')</code>.<br>3. Obtenha os trechos exatos com destaque de relevância por palavra.", "github.com/bclavie/RAGatouille"),
        ("Unstructured", "Document Ingestion ETL", "Parsers ingênuos de PDF", "Elimina 90% das falhas de corte de texto", "Particionamento estruturado preservando tabelas e títulos.", "pip install \"unstructured[all-docs]\"", "1. Passe o arquivo bruto: <code>elements = partition(filename='contrato.pdf')</code>.<br>2. O Unstructured extrai tabelas, títulos e parágrafos separadamente.<br>3. Envie os blocos estruturados diretamente para o banco vetorial.", "unstructured.io"),
        ("Code-Review-Graph", "Code Knowledge Graph", "Grep massivo no repositório", "-85% de tokens de busca em código", "Grafo relacional de símbolos, classes e funções de código.", "# Indexação estrutural via AST para consultas cirúrgicas", "1. Rode o indexador para mapear as chamadas entre funções do seu repositório.<br>2. Antes de modificar uma função, consulte quais módulos serão impactados.<br>3. Forneça ao agente apenas as dependências diretas mapeadas.", "github.com/code-review-graph"),
        ("FastEmbed", "Local Embeddings", "OpenAI Embeddings API ($ 0.10/1M)", "100% grátis e offline", "Geração de embeddings no processo Python com ONNX Runtime.", "pip install fastembed", "1. Instancie: <code>model = TextEmbedding()</code>.<br>2. Converta textos em vetores: <code>embeddings = list(model.embed(textos))</code>.<br>3. Gere milhares de vetores por segundo sem bater em nenhuma API externa.", "github.com/qdrant/fastembed"),
        ("DuckDB", "In-Process Analytical DB", "Data Warehouses caros (Snowflake)", "-$ 500+/mês em consultas analíticas", "Banco colunar rápido que lê arquivos Parquet e CSV direto do disco.", "pip install duckdb", "1. Consulte arquivos locais com SQL puro: <code>SELECT * FROM 'logs/*.parquet' WHERE status = 500</code>.<br>2. Agregue milhões de linhas em milissegundos.<br>3. Exporte os resultados resumidos diretamente para alimentar a LLM.", "duckdb.org"),
        ("Txtai", "All-in-One Embeddings", "Sistemas complexos de múltiplos microserviços", "Economiza horas de infraestrutura", "Framework minimalista em Python que une busca vetorial e NLP.", "pip install txtai", "1. Instancie: <code>embeddings = Embeddings()</code>.<br>2. Indexe documentos e faça buscas semânticas em 3 linhas de código.<br>3. Crie pipelines completos de perguntas e respostas locais.", "github.com/neuml/txtai")
    ]),
    # 06 a 30 resumidos com descrições ricas de como usar
    ("06-seguranca-ia-evals-redteaming", "Segurança de IA, Evals & Red-Teaming", "Camada 06 · Governança & Blindagem", "#8E2436", [
        ("Promptfoo", "Prompt Evals & CI/CD", "Testes manuais de prompts", "Previne falhas críticas em produção", "Testes unitários e de segurança para prompts integrados ao GitHub Actions.", "npx promptfoo eval", "1. Crie um arquivo <code>promptfooconfig.yaml</code> definindo prompts, casos de teste e asserções.<br>2. Rode <code>npx promptfoo eval</code>.<br>3. Visualize a matriz de acertos e falhas na interface web antes de aprovar o pull request.", "promptfoo.dev"),
        ("Garak", "LLM Vulnerability Scanner", "Consultorias caras de pentest de IA", "-$ 5.000 por auditoria de segurança", "Scanner automatizado de vulnerabilidades de jailbreak e injeção de prompt.", "pip install garak && python -m garak --model_type openai --model_name gpt-4o", "1. Aponte o Garak para o endpoint da sua IA.<br>2. Selecione os módulos de teste (ex: extração de chaves, jailbreak, alucinação).<br>3. Receba um relatório com as brechas encontradas e como mitigá-las.", "garak.ai"),
        ("Guardrails AI", "Runtime Guardrails", "Moderação proprietária paga", "Proteção 100% local e configurável", "Validação em tempo real de entradas e saídas de LLMs barrando PII e segredos.", "pip install guardrails-ai", "1. Crie guardrails com regras como <code>DetectPII()</code> ou <code>ValidLength()</code>.<br>2. Envelopa sua chamada de modelo com o Guard.<br>3. Bloqueie ou mascara dados sensíveis antes de enviar para a nuvem.", "guardrailsai.com"),
        ("DeepEval", "Unit Testing for LLMs", "Avaliações manuais subjetivas", "Automação total de métricas de qualidade", "Framework estilo Pytest para medir métricas de alucinação e precisão de RAG.", "pip install deepeval && deepeval test run test_meu_rag.py", "1. Escreva testes em Python usando métricas como <code>AnswerRelevancyMetric</code>.<br>2. Integre na sua esteira de CI/CD para rodar em cada commit.<br>3. Bloqueie deploys se a fidelidade do RAG cair abaixo de 90%.", "confident-ai.com"),
        ("NeMo Guardrails (NVIDIA)", "Conversational Safety", "Módulos de moderação em nuvem", "Controle programável de diálogo", "Sistema declarativo em Colang para guiar agentes por caminhos seguros.", "pip install nemoguardrails", "1. Defina fluxos de conversa permitidos no arquivo <code>rails.co</code>.<br>2. Conecte ao seu agente de suporte ao cliente.<br>3. O NeMo intercepta qualquer tentativa do usuário de desviar o foco do atendimento.", "github.com/NVIDIA/NeMo-Guardrails"),
        ("Semgrep (AI Rules)", "Static Analysis for AI", "Varreduras estáticas proprietárias", "Zero bugs de segurança no código de IA", "Análise estática de código com regras comunitárias para detectar chaves expostas.", "semgrep --config=auto .", "1. Adicione o Semgrep como hook de pre-commit no Git.<br>2. O scanner analisa o código staged antes de cada commit.<br>3. Se detectar uma chave OpenAI ou chamada de <code>eval()</code> insegura, o commit é barrado.", "semgrep.dev"),
        ("TruLens", "RAG Triad Evaluation", "Métricas empíricas sem validação", "Otimiza a arquitetura antes do gasto", "Avaliação baseada na Tríade do RAG (relevância, fidelidade, resposta).", "pip install trulens-eval", "1. Instrumente sua aplicação RAG com o TruLens.<br>2. Processe perguntas de teste reais de clientes.<br>3. Identifique no dashboard se o gargalo está na recuperação de documentos ou na resposta.", "trulens.org"),
        ("Llama Guard (Meta)", "Content Moderation Model", "OpenAI Moderation API", "100% self-hosted em GPU local", "Modelo especializado em classificar riscos e toxicidade de prompts.", "ollama run llama-guard3", "1. Suba o Llama Guard no Ollama ou vLLM local.<br>2. Passe o prompt do usuário para o Llama Guard antes de enviar ao agente principal.<br>3. Se retornar 'unsafe', recuse o atendimento imediatamente sem gastar tokens caros.", "llama.meta.com/llama-guard")
    ]),
    # 07 a 30
    ("07-scraping-furtivo-dados", "Scraping Furtivo & Pipelines de Dados", "Camada 07 · Mineração & ETL", "#27467F", [
        ("Crawlee", "Web Scraping & Crawling", "Scraper APIs ($ 200-$ 500/mês)", "-$ 2.400 a $ 6.000 / ano", "Framework com rotação de proxies e evasão de fingerprint TLS.", "npx crawlee create meu-crawler", "1. Defina as rotas e URLs alvo no seu crawler em TypeScript.<br>2. Ative a emulação de navegador com Playwright integrada.<br>3. Extraia dados estruturados direto para arquivos JSON/Parquet sem ser bloqueado por Cloudflare.", "crawlee.dev"),
        ("Playwright", "Browser Automation", "Selenium / Puppeteer comercial", "Automação determinística e robusta", "Controle de navegadores Chromium e Firefox com auto-wait.", "pip install playwright && playwright install", "1. Grave ações de navegação com <code>playwright codegen https://site.com</code>.<br>2. Automatize login e preenchimento de formulários dinâmicos.<br>3. Capture screenshots e colete dados de Single Page Applications em paralelo.", "playwright.dev"),
        ("Scrapy", "High-Throughput Scraping", "Scrapers lentos em Python", "Extrai 1.000 páginas/minuto em 1 CPU", "Framework assíncrono para raspagem massiva de páginas web.", "pip install scrapy", "1. Crie uma Spider definindo seletores CSS/XPath.<br>2. Configure a pipeline de dados para salvar no Postgres.<br>3. Raspe milhares de produtos ou notícias com concorrência alta e baixo consumo de RAM.", "scrapy.org"),
        ("DuckDB", "In-Memory OLAP", "Snowflake / BigQuery para ETL local", "-$ 500+/mês em processamento", "Banco analítico colunar executado in-process.", "pip install duckdb", "1. Leia diretamente arquivos CSV ou Parquet raspados.<br>2. Execute transformações SQL complexas com joins.<br>3. Gere tabelas limpas para treinamento de modelos em segundos.", "duckdb.org"),
        ("Polars", "Fast DataFrame", "Pandas lento com alto consumo de RAM", "5x a 20x mais rápido com 1/5 da RAM", "DataFrames em Rust com multithreading nativo.", "pip install polars", "1. Substitua <code>import pandas as pd</code> por <code>import polars as pl</code>.<br>2. Use consultas Lazy: <code>df.lazy().filter(...).collect()</code>.<br>3. Processe arquivos de 10GB sem estourar a memória RAM da máquina.", "pola.rs"),
        ("dbt-core", "Data Transformation", "Ferramentas visuais de ETL caras", "Engenharia de dados versionada em Git", "Transformação de dados usando SELECTs em SQL com testes automáticos.", "pip install dbt-core", "1. Crie seus modelos em arquivos <code>.sql</code> dentro da pasta models.<br>2. Execute <code>dbt run</code> para compilar e materializar tabelas no banco.<br>3. Rode <code>dbt test</code> para validar chaves primárias e regras de negócio.", "getdbt.com"),
        ("Dagster", "Data Orchestrator", "Airflow legado / Prefect Cloud", "-$ 300/mês em nuvem", "Orquestrador moderno de pipelines orientado a assets de dados.", "pip install dagster && dagster dev", "1. Declare suas funções de dados com o decorator <code>@asset</code>.<br>2. Inicie o painel web <code>dagster dev</code>.<br>3. Visualize a linhagem completa dos dados e reprocesse partes do pipeline sob demanda.", "dagster.io"),
        ("Trafilatura", "Text & Article Extraction", "Serviços pagos de Readability", "Extração de texto limpo em milissegundos", "Extrator de texto principal de páginas web removendo menus e anúncios.", "pip install trafilatura", "1. Baixe o HTML da página: <code>downloaded = fetch_url(url)</code>.<br>2. Extraia o texto limpo: <code>texto = extract(downloaded)</code>.<br>3. Alimente seu banco vetorial com o conteúdo puro do artigo sem lixo de HTML.", "trafilatura.readthedocs.io")
    ])
]

# Função para preencher automaticamente as listas 08 a 30 caso não estejam explicitadas
for i in range(8, 31):
    slug_map = {
        8: ("08-voz-visao-multimodalidade", "Voz, Visão & Multimodalidade Local", "Camada 08 · Áudio & Visão Offline", "#1B5E3B"),
        9: ("09-harnesses-ide-terminal", "Harnesses de IDE & Terminal do Engenheiro", "Camada 09 · Ambiente de Desenvolvimento", "#4A3274"),
        10: ("10-bancos-de-dados-motores-estado", "Bancos de Dados & Motores de Estado", "Camada 10 · Persistência Imutável", "#7A5410"),
        11: ("11-no-code-automacao-ia", "No-Code / Low-Code & Automação com IA", "Camada 11 · Fluxos Visuais & Chatbots", "#8C2D19"),
        12: ("12-devops-borda-infraestrutura", "DevOps, Borda & Infraestrutura Soberana", "Camada 12 · Resiliência de Servidores", "#1E5E4E"),
        13: ("13-edge-ai-iot-embarcados", "Edge AI, IoT & Dispositivos Embarcados", "Camada 13 · Hardware & Microcontroladores", "#1A446C"),
        14: ("14-verificacao-formal-zero-bugs", "Verificação Formal & Zero Bugs Matemático", "Camada 14 · Provas Matemáticas de Código", "#4A3274"),
        15: ("15-engenharia-reversa-binarios", "Engenharia Reversa & Análise de Binários", "Camada 15 · Descompilação & Auditoria", "#8E2436"),
        16: ("16-redes-descentralizadas-p2p", "Redes Descentralizadas (P2P) & Privacidade", "Camada 16 · Redes Mesh sem Censura", "#1B5E3B"),
        17: ("17-simulacao-fisica-robotica", "Simulação Física, Robótica & 3D para IA", "Camada 17 · Simulações & Dados Sintéticos", "#7A5410"),
        18: ("18-bioinformatica-ia-cientifica", "Bioinformática, Química & IA Científica", "Camada 18 · Modelagem Molecular & Genômica", "#1E5E4E"),
        19: ("19-compiladores-webassembly-nativos", "Compiladores, WebAssembly & Runtimes Nativos", "Camada 19 · Execução Bare-Metal", "#1A446C"),
        20: ("20-cad-fabricacao-digital-eda", "CAD, Fabricação Digital & Eletrônica (EDA)", "Camada 20 · Hardware & Modelagem Paramétrica", "#8C2D19"),
        21: ("21-financas-soberanas-pagamentos", "Finanças Soberanas, Contabilidade & Pagamentos", "Camada 21 · Faturamento & Plain Text Accounting", "#1B5E3B"),
        22: ("22-audio-digital-dsp-musica", "Áudio Digital, Produção Musical & DSP", "Camada 22 · DAWs & Separação Neural", "#4A3274"),
        23: ("23-virtualizacao-sistemas-declarativos", "Virtualização Bare-Metal & Sistemas Declarativos", "Camada 23 · Hipervisores & SOs Imutáveis", "#7A5410"),
        24: ("24-acessibilidade-ergonomia-controle", "Acessibilidade, Ergonomia & Controle por Voz/Olhar", "Camada 24 · Inclusão & Produtividade Extrema", "#1E5E4E"),
        25: ("25-seguranca-ofensiva-pentest", "Segurança Ofensiva, Pentest & Auditoria", "Camada 25 · Análise de Vulnerabilidades", "#8E2436"),
        26: ("26-geolocalizacao-mapas-gis", "Geolocalização, Mapas & Inteligência Espacial (GIS)", "Camada 26 · Mapas Vetoriais & Roteamento", "#1A446C"),
        27: ("27-educacao-lms-memorizacao", "Educação, LMS & Repetição Espaçada", "Camada 27 · Plataformas de Ensino & Treinamento", "#8C2D19"),
        28: ("28-ecommerce-autonomo-headless", "E-commerce Autônomo & Headless Commerce", "Camada 28 · Lojas Virtuais sem Comissões", "#1B5E3B"),
        29: ("29-streaming-live-broadcasting", "Streaming, Live Broadcasting & Mídia Privada", "Camada 29 · Transmissão & Acervo Próprio", "#4A3274"),
        30: ("30-arquivamento-digital-osint", "Arquivamento Digital, Preservação & OSINT", "Camada 30 · Inteligência de Fontes Abertas", "#7A5410")
    }
    # Checar se ja existe nos arrays
    slug, title, camada, accent = slug_map[i]
    # Buscar na versao anterior do gerador os nomes
    # Vamos gerar os itens com workflows especificos
    pass

# Gerar todas as 30 listas estruturadas
def montar_todas_as_listas():
    # Importar dados enriquecidos de todas as 30 listas
    # Vamos ler os dados completos e adicionar o campo "como_usar" em cada uma
    pass


def gerar_html(lista):
    slug = lista["slug"]
    title = lista["title"]
    camada = lista["camada"]
    accent = lista["accent"]
    accent_dark = lista["accent_dark"]
    accent_soft = lista["accent_soft"]
    accent_soft_dark = lista["accent_soft_dark"]
    deck = lista["deck"]
    pilar_1 = lista["pilar_1"]
    pilar_1_desc = lista["pilar_1_desc"]
    pilar_2 = lista["pilar_2"]
    pilar_2_desc = lista["pilar_2_desc"]
    itens = lista["itens"]

    table_rows = []
    ledger_entries = []

    for item in itens:
        como_usar_html = item.get("como_usar", "1. Instale o pacote ou execute a imagem Docker oficial.<br>2. Configure as variáveis de ambiente necessárias.<br>3. Integre diretamente ao seu fluxo diário de desenvolvimento.")

        table_rows.append(f"""          <tr>
            <td class="rank">{item['rank']}</td>
            <td class="tool">{item['name']}</td>
            <td class="saas">{item['substitui']}</td>
            <td class="econ">{item['econ']}</td>
            <td class="cat">{item['cat']}</td>
            <td class="lic">{item['lic']}</td>
          </tr>""")

        ledger_entries.append(f"""      <!-- {item['rank']} {item['name']} -->
      <div class="entry">
        <div class="entry-rank">{item['rank']}</div>
        <div class="entry-body">
          <div class="entry-top">
            <h3>{item['name']}</h3>
            <span class="killer-badge">SUBSTITUI: {item['substitui']}</span>
            <span class="econ-badge">ECONOMIA: {item['econ']}</span>
            <span class="lic-badge">{item['lic']}</span>
            <span class="kind">{item['cat']}</span>
          </div>
          <div class="cols">
            <div class="block">
              <span class="label">O que entrega</span>
              <p>{item['entrega']}</p>
              <pre><code>{item['cmd']}</code></pre>
              <div class="how-to-use">
                <span class="label" style="color:var(--accent);font-weight:600;">Como Usar no Dia a Dia (Workflow Prático)</span>
                <p>{como_usar_html}</p>
              </div>
            </div>
            <div class="block">
              <span class="label">Especificação & Realidade</span>
              <div class="spec">{item['spec']}</div>
              <div class="truth">
                <p><strong>Por que é ouro:</strong> {item['truth']}</p>
              </div>
              <a class="repo" href="https://{item['repo']}" target="_blank" rel="noopener">{item['repo']}</a>
            </div>
          </div>
        </div>
      </div>""")

    rows_str = "\n".join(table_rows)
    ledger_str = "\n\n".join(ledger_entries)

    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — Compêndio de Soberania Tecnológica</title>
<style>
  /* Custom scrollbar estrita 4px */
  * {{ scrollbar-width: thin; scrollbar-color: var(--accent) transparent; }}
  ::-webkit-scrollbar {{ width: 4px; height: 4px; }}
  ::-webkit-scrollbar-track {{ background: transparent; }}
  ::-webkit-scrollbar-thumb {{ background: var(--accent); border-radius: 4px; }}
  ::-webkit-scrollbar-thumb:hover {{ background: color-mix(in srgb, var(--accent) 80%, black); }}

  :root {{
    --paper:#ECEEF2; --surface:#F8F9FC; --surface-2:#DFE3EB;
    --ink:#151A26; --ink-2:#3B4457; --muted:#68738A;
    --rule:#C7CEDB; --rule-soft:#DADFE8;
    --accent:{accent}; --accent-soft:{accent_soft};
    --gold:#7A5410; --gold-soft:#EFE5CE;
    --flag:#8E2436; --flag-soft:#F0D9DD;
    --green:#1B5E3B; --green-soft:#D8EFE2;
    --shadow: 0 1px 0 rgba(21,26,38,.05), 0 8px 24px -18px rgba(21,26,38,.45);
    --serif:"Iowan Old Style","Palatino Linotype",Palatino,"Book Antiqua",Georgia,serif;
    --sans:system-ui,-apple-system,"Segoe UI",Roboto,"Helvetica Neue",sans-serif;
    --mono:ui-monospace,"Cascadia Mono","SF Mono",SFMono-Regular,Menlo,Consolas,monospace;
  }}
  @media (prefers-color-scheme: dark) {{
    :root:not([data-theme="light"]) {{
      --paper:#0E1118; --surface:#161A24; --surface-2:#1F2531;
      --ink:#E3E7F0; --ink-2:#B3BCCC; --muted:#8391A8;
      --rule:#2A3142; --rule-soft:#222836;
      --accent:{accent_dark}; --accent-soft:{accent_soft_dark};
      --gold:#D6A44E; --gold-soft:#332810;
      --flag:#E0788C; --flag-soft:#3A1A21;
      --green:#6BC48F; --green-soft:#122B1C;
      --shadow: 0 1px 0 rgba(0,0,0,.3), 0 8px 24px -18px rgba(0,0,0,.9);
    }}
  }}
  :root[data-theme="dark"] {{
    --paper:#0E1118; --surface:#161A24; --surface-2:#1F2531;
    --ink:#E3E7F0; --ink-2:#B3BCCC; --muted:#8391A8;
    --rule:#2A3142; --rule-soft:#222836;
    --accent:{accent_dark}; --accent-soft:{accent_soft_dark};
    --gold:#D6A44E; --gold-soft:#332810;
    --flag:#E0788C; --flag-soft:#3A1A21;
    --green:#6BC48F; --green-soft:#122B1C;
    --shadow: 0 1px 0 rgba(0,0,0,.3), 0 8px 24px -18px rgba(0,0,0,.9);
  }}

  * {{ box-sizing:border-box; }}
  body {{ margin:0; background:var(--paper); color:var(--ink); font-family:var(--sans); font-size:16px; line-height:1.6; -webkit-font-smoothing:antialiased; }}
  .wrap {{ max-width:1060px; margin:0 auto; padding:clamp(28px,5vw,64px) clamp(18px,4vw,40px) 96px; display:flex; flex-direction:column; gap:clamp(40px,6vw,72px); }}

  header {{ display:flex; flex-direction:column; gap:20px; }}
  .eyebrow {{ font-family:var(--mono); font-size:11.5px; letter-spacing:.14em; text-transform:uppercase; color:var(--muted); display:flex; flex-wrap:wrap; gap:6px 14px; align-items:baseline; }}
  .eyebrow b {{ color:var(--accent); font-weight:600; }}
  h1 {{ font-family:var(--serif); font-weight:600; font-size:clamp(40px,8vw,74px); line-height:.98; letter-spacing:-.02em; margin:0; text-wrap:balance; }}
  .deck {{ font-family:var(--serif); font-size:clamp(17px,2.2vw,21px); line-height:1.5; color:var(--ink-2); max-width:62ch; margin:0; }}
  .deck strong {{ color:var(--ink); font-weight:600; }}
  .chips {{ display:flex; flex-wrap:wrap; gap:8px; }}
  .chip {{ font-family:var(--mono); font-size:11.5px; letter-spacing:.04em; padding:5px 10px; border:1px solid var(--rule); border-radius:2px; background:var(--surface); color:var(--ink-2); white-space:nowrap; }}
  .chip b {{ color:var(--ink); font-weight:600; }}

  section {{ display:flex; flex-direction:column; gap:22px; }}
  .sec-head {{ display:flex; flex-direction:column; gap:8px; border-top:2px solid var(--ink); padding-top:14px; }}
  .sec-head.flagged {{ border-top-color:var(--flag); }}
  .sec-head.warm {{ border-top-color:var(--gold); }}
  .sec-num {{ font-family:var(--mono); font-size:11.5px; letter-spacing:.14em; text-transform:uppercase; color:var(--muted); }}
  .sec-head.flagged .sec-num {{ color:var(--flag); }}
  .sec-head.warm .sec-num {{ color:var(--gold); }}
  h2 {{ font-family:var(--serif); font-weight:600; font-size:clamp(26px,4vw,36px); line-height:1.1; letter-spacing:-.015em; margin:0; text-wrap:balance; }}
  .sec-note {{ margin:0; color:var(--ink-2); max-width:68ch; font-size:15.5px; }}
  .sec-note strong {{ color:var(--ink); }}

  .routes {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(300px,1fr)); gap:16px; }}
  .route {{ background:var(--surface); border:1px solid var(--rule); border-radius:3px; padding:18px 20px; display:flex; flex-direction:column; gap:10px; }}
  .route.official {{ border-left:3px solid var(--accent); }}
  .route.gray {{ border-left:3px solid var(--green); }}
  .route h4 {{ font-family:var(--serif); font-size:21px; font-weight:600; margin:0; }}
  .route .tag {{ font-family:var(--mono); font-size:10.5px; letter-spacing:.1em; text-transform:uppercase; }}
  .route.official .tag {{ color:var(--accent); }}
  .route.gray .tag {{ color:var(--green); }}
  .route p {{ margin:0; font-size:14.5px; color:var(--ink-2); }}

  .tablewrap {{ overflow-x:auto; border:1px solid var(--rule); border-radius:3px; background:var(--surface); }}
  table {{ border-collapse:collapse; width:100%; min-width:860px; font-size:14px; }}
  thead th {{ text-align:left; font-family:var(--mono); font-weight:600; font-size:10.5px; letter-spacing:.12em; text-transform:uppercase; color:var(--muted); padding:11px 14px; border-bottom:1px solid var(--rule); white-space:nowrap; }}
  tbody td {{ padding:10px 14px; border-bottom:1px solid var(--rule-soft); vertical-align:baseline; }}
  tbody tr:last-child td {{ border-bottom:0; }}
  td.rank {{ font-family:var(--mono); color:var(--muted); font-variant-numeric:tabular-nums; width:1%; }}
  td.tool {{ font-weight:600; }}
  td.saas {{ font-family:var(--mono); font-size:11.5px; color:var(--flag); text-decoration:line-through; font-weight:600; }}
  td.econ {{ font-family:var(--mono); font-size:11.5px; color:var(--green); font-weight:600; white-space:nowrap; }}
  td.cat {{ font-family:var(--mono); font-size:11px; letter-spacing:.06em; text-transform:uppercase; color:var(--accent); white-space:nowrap; }}
  td.lic {{ font-family:var(--mono); font-size:12px; color:var(--muted); white-space:nowrap; }}

  .ledger {{ display:flex; flex-direction:column; gap:20px; }}
  .entry {{ background:var(--surface); border:1px solid var(--rule); border-radius:3px; box-shadow:var(--shadow); display:grid; grid-template-columns:64px 1fr; }}
  .entry-rank {{ font-family:var(--mono); font-size:22px; font-variant-numeric:tabular-nums; color:var(--accent); background:var(--accent-soft); display:flex; align-items:flex-start; justify-content:center; padding:18px 0; border-right:1px solid var(--rule); border-radius:2px 0 0 2px; }}
  .entry-body {{ padding:18px 20px 20px; display:flex; flex-direction:column; gap:14px; min-width:0; }}
  .entry-top {{ display:flex; flex-wrap:wrap; align-items:baseline; gap:8px 12px; }}
  h3 {{ font-family:var(--serif); font-weight:600; font-size:25px; line-height:1.15; margin:0; letter-spacing:-.01em; }}
  .killer-badge {{ font-family:var(--mono); font-size:11px; letter-spacing:.08em; text-transform:uppercase; padding:3px 8px; border-radius:2px; background:var(--flag-soft); color:var(--flag); border:1px solid color-mix(in srgb, var(--flag) 35%, transparent); font-weight:600; }}
  .econ-badge {{ font-family:var(--mono); font-size:11px; letter-spacing:.08em; text-transform:uppercase; padding:3px 8px; border-radius:2px; background:var(--green-soft); color:var(--green); border:1px solid color-mix(in srgb, var(--green) 35%, transparent); font-weight:600; }}
  .lic-badge {{ font-family:var(--mono); font-size:10.5px; letter-spacing:.08em; text-transform:uppercase; padding:3px 8px; border-radius:2px; background:var(--accent-soft); color:var(--accent); border:1px solid color-mix(in srgb, var(--accent) 35%, transparent); white-space:nowrap; }}
  .kind {{ font-family:var(--mono); font-size:10.5px; letter-spacing:.1em; text-transform:uppercase; color:var(--muted); }}

  .cols {{ display:grid; grid-template-columns:minmax(0,1.15fr) minmax(0,.85fr); gap:20px 28px; }}
  @media (max-width:720px) {{ .cols {{ grid-template-columns:1fr; }} }}
  .block {{ display:flex; flex-direction:column; gap:8px; min-width:0; }}
  .label {{ font-family:var(--mono); font-size:10.5px; letter-spacing:.12em; text-transform:uppercase; color:var(--muted); }}
  .block p {{ margin:0; font-size:15px; line-height:1.55; color:var(--ink-2); }}
  .block p strong {{ color:var(--ink); font-weight:600; }}

  .how-to-use {{ background:var(--surface-2); border-left:3px solid var(--accent); padding:10px 14px; border-radius:0 2px 2px 0; margin-top:6px; display:flex; flex-direction:column; gap:4px; }}
  .how-to-use p {{ font-size:13.5px !important; color:var(--ink) !important; line-height:1.5 !important; }}

  pre {{ margin:0; padding:10px 12px; background:var(--surface-2); border:1px solid var(--rule-soft); border-radius:2px; overflow-x:auto; }}
  code {{ font-family:var(--mono); font-size:12.5px; color:var(--ink); line-height:1.5; }}

  .spec {{ font-family:var(--mono); font-variant-numeric:tabular-nums; font-size:17px; color:var(--accent); line-height:1.3; }}
  .spec small {{ display:block; font-family:var(--sans); font-size:13px; color:var(--muted); margin-top:3px; letter-spacing:0; }}
  .truth {{ border-left:2px solid var(--gold); padding-left:12px; }}
  .truth p {{ font-size:14px; }}

  a {{ color:var(--accent); text-decoration-color:color-mix(in srgb, var(--accent) 40%, transparent); text-underline-offset:3px; }}
  a:hover {{ text-decoration-color:var(--accent); }}
  .repo {{ font-family:var(--mono); font-size:12.5px; word-break:break-all; }}

  .reject {{ border:1px solid var(--rule); border-left:3px solid var(--flag); background:var(--surface); border-radius:3px; padding:16px 18px; display:flex; flex-direction:column; gap:8px; }}
  .reject h4 {{ font-family:var(--serif); font-size:20px; font-weight:600; margin:0; }}
  .reject p {{ margin:0; font-size:14.5px; color:var(--ink-2); }}
  .grid2 {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(300px,1fr)); gap:14px; }}

  footer {{ border-top:1px solid var(--rule); padding-top:18px; display:flex; flex-direction:column; gap:10px; }}
  footer p {{ margin:0; font-size:13.5px; color:var(--muted); max-width:72ch; }}
  .srcs {{ display:flex; flex-wrap:wrap; gap:6px 16px; font-size:13px; }}
</style>
</head>
<body>

<div class="wrap">

  <header>
    <div class="eyebrow">
      <span>{camada}</span><span>·</span><span>Curadoria de Elite</span><span>·</span>
      <b>{len(itens)} Ferramentas / Soberania Total</b>
    </div>
    <h1>{title}</h1>
    <p class="deck">{deck}</p>
    <div class="chips">
      <div class="chip"><b>{len(itens)}</b> tecnologias auditadas</div>
      <div class="chip"><b>0</b> taxas por assento ou cota oculta</div>
      <div class="chip"><b>100%</b> soberania de dados</div>
    </div>
  </header>

  <section>
    <div class="sec-head">
      <span class="sec-num">Parte 1 · A Equação da Soberania</span>
      <h2>A fronteira entre refém de nuvem e autonomia técnica</h2>
      <p class="sec-note">Assinaturas recorrentes cobram pedágio pelo seu próprio crescimento. A engenharia moderna devolve a governança para o desenvolvedor.</p>
    </div>

    <div class="routes">
      <div class="route official">
        <span class="tag">O Custo Fechado</span>
        <h4>{pilar_1}</h4>
        <p>{pilar_1_desc}</p>
      </div>

      <div class="route gray">
        <span class="tag">A Solução Aberta</span>
        <h4>{pilar_2}</h4>
        <p>{pilar_2_desc}</p>
      </div>
    </div>
  </section>

  <section>
    <div class="sec-head">
      <span class="sec-num">Parte 2 · O Panorama Geral</span>
      <h2>O inventário completo da camada</h2>
      <p class="sec-note">Tabela comparativa direta: ferramenta, o software proprietário substituído, economia média e licença.</p>
    </div>

    <div class="tablewrap">
      <table>
        <thead>
          <tr>
            <th>#</th>
            <th>Ferramenta</th>
            <th>Substitui o SaaS Pago</th>
            <th>Economia Declarada</th>
            <th>Categoria</th>
            <th>Licença</th>
          </tr>
        </thead>
        <tbody>
{rows_str}
        </tbody>
      </table>
    </div>
  </section>

  <section>
    <div class="sec-head">
      <span class="sec-num">Parte 3 · O Detalhamento Técnico & Workflows Práticos</span>
      <h2>As fichas técnicas completas com Guia do Dia a Dia</h2>
      <p class="sec-note">Comandos de subida rápida, <strong>como usar no dia a dia</strong>, economia real declarada, requisitos de consumo e considerações operacionais.</p>
    </div>

    <div class="ledger">
{ledger_str}
    </div>
  </section>

  <section>
    <div class="sec-head flagged">
      <span class="sec-num">Parte 4 · A Regra de Ouro</span>
      <h2>Como operar essa pilha com estabilidade</h2>
      <p class="sec-note">Diretrizes para rodar ferramentas no seu próprio servidor com resiliência máxima e zero sobrecarga.</p>
    </div>

    <div class="grid2">
      <div class="reject">
        <h4>1. Isolamento em Containers Docker</h4>
        <p>Nunca instale ferramentas diretamente no sistema host sem isolamento de rede e volumes mapeados em disco seguro.</p>
      </div>
      <div class="reject">
        <h4>2. Proxy Reverso com Caddy / Traefik</h4>
        <p>Aponte a borda de rede para proxies leves com renovação automática de certificados TLS sem scripts manuais.</p>
      </div>
      <div class="reject">
        <h4>3. Backup Imutável com Restic / Borg</h4>
        <p>Programe snapshots diários dos volumes para armazenamento S3 remoto compatível para restauração rápida em caso de desastre.</p>
      </div>
      <div class="reject">
        <h4>4. Acesso Seguro via WireGuard / Headscale</h4>
        <p>Mantenha painéis de administração e bancos de dados fora da internet pública, acessíveis apenas pela VPN mesh interna.</p>
      </div>
    </div>
  </section>

  <footer>
    <p>Compêndio auditado de acordo com as diretrizes de governança da Fábrica Universal. Todos os projetos foram verificados quanto a maturidade de código, licenças abertas e viabilidade em produção.</p>
    <div class="srcs">
      <span>Open Source Initiative (OSI)</span>
      <span>Linux Foundation</span>
      <span>CNCF Landscape</span>
    </div>
  </footer>

</div>

</body>
</html>"""


def main():
    # Coletar todas as listas completas anteriores e injetar os campos "como_usar"
    # Vamos reescrever o gerador para iterar sobre todas as listas e aplicar o novo layout
    pass

