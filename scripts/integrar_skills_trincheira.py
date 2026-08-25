# -*- coding: utf-8 -*-
"""
Gerador de Elite da Enciclopédia de Soberania Tecnológica & Skills Agênticas.
Integra ferramentas de trincheira do operador (NoteGen, AnythingLLM, Upscayl, Voicebox, Uptime Kuma, etc.)
e as Skills Agênticas de ponta (Caveman, Headroom, Lean-CTX, RTK-Memory, Impeccable, Mira Animator, Hallmark, etc.)
distribuídas com precisão técnica em cada uma das camadas e compêndios.
"""

from pathlib import Path
from expandir_lista_02 import LISTA_02_EXPANDIDA

# Banco de dados exaustivo de ferramentas e skills enriquecidas
CATALOGO_COMPLETO = [
    # 01 - Economia de Tokens & Skills de Contexto
    {
        "slug": "01-economia-de-tokens",
        "title": "Economia Extrema de Tokens, Contexto & Skills de Eficiência",
        "camada": "Camada 01 · Eficiência de Contexto & Skills",
        "accent": "#1B5E3B", "accent_dark": "#6BC48F", "accent_soft": "#D8EFE2", "accent_soft_dark": "#122B1C",
        "deck": "Metodologias, compiladores, caches e <strong>skills agênticas para cortar até 85% do custo com LLMs</strong>: compressão telegráfica de pensamento (Caveman), compressão de logs (Headroom), buscas cirúrgicas (Lean-CTX), AST e packing de repositórios.",
        "pilar_1": "O Custo Invisível do Contexto Inflado",
        "pilar_1_desc": "Enviar arquivos inteiros, logs de build de 500 linhas e pensamentos prolixos queima centenas de milhares de tokens por turno. 80% do gasto mensal é puro ruído.",
        "pilar_2": "A Engenharia do Prompt & Skills Agênticas",
        "pilar_2_desc": "Com as skills Caveman, Headroom, Lean-CTX combinadas com Repomix e LiteLLM Cache, o modelo recebe apenas os bytes exatos necessários para a tarefa.",
        "itens": [
            {
                "rank": "01", "name": "Skill: caveman", "cat": "Agentic Reasoning Compression", "lic": "MIT / Prompt Skill",
                "substitui": "Pensamentos CoT prolixos e caros", "econ": "-90% de tokens no bloco <thought>",
                "entrega": "Força o agente a pensar em estilo telegráfico (estilo homem das cavernas), sem artigos, sem saudações e sem repetir o prompt do usuário.",
                "mecanica": "Instrui o modelo a usar frases curtas de 3 a 5 linhas no Chain-of-Thought (ex: 'usr quer X. ler arq Y. corrigir Z.'), economizando até 800 tokens a cada turno de raciocínio interno.",
                "cmd": "# Ativação via SKILL.md ou regra de sistema: 'Para raciocínios internos, use estilo CAVEMAN telegráfico'",
                "como_usar": "1. Adicione a skill <code>caveman</code> no diretório <code>.claude/skills/</code> ou nas regras do seu agente.<br>2. Ao receber uma instrução, o agente pensa diretamente na solução sem floreios verbais.<br>3. Reduza a latência de resposta em 60% e economize milhares de tokens por sessão de pareamento.",
                "spec": "0 MB RAM / Overhead zero",
                "truth": "Tokens de pensamento interno custam o mesmo que tokens de saída. Pensar de forma enxuta é a forma mais rápida de economizar.",
                "repo": "github.com/topics/claude-skills"
            },
            {
                "rank": "02", "name": "Skill: headroom", "cat": "Log & Terminal Compression", "lic": "MIT / Prompt Skill",
                "substitui": "Dumps gigantes de terminal no contexto", "econ": "-80% de tokens em logs de compilação",
                "entrega": "Monitora e trunca logs longos de compilação, testes e builds, mantendo apenas o topo do comando e o stack trace do erro.",
                "mecanica": "Aplica regra rígida: se a saída do comando tiver > 7 linhas, comprime em (3 linhas do topo + 4 linhas do final), preservando a causa raiz da falha sem poluir a janela de contexto.",
                "cmd": "# Regra: 'Logs > 7 linhas -> comprimir (3 topo + 4 fim)'",
                "como_usar": "1. Integre no prompt do seu orquestrador ou hook de execução de comandos.<br>2. Quando um <code>npm run build</code> falhar com 300 linhas de warnings, o agente só recebe as linhas essenciais do erro.<br>3. Evita estourar a janela de contexto com logs repetitivos.",
                "spec": "0 MB RAM / Filtro em runtime",
                "truth": "A maioria dos erros de compilação tem sua causa nas últimas 4 linhas. Ler 300 linhas de warning é queimar dinheiro.",
                "repo": "github.com/topics/agentic-skills"
            },
            {
                "rank": "03", "name": "Skill: lean-ctx", "cat": "Targeted Code Inspection", "lic": "MIT / Prompt Skill",
                "substitui": "view_file() do arquivo inteiro", "econ": "-85% de tokens de leitura de código",
                "entrega": "Obriga o agente a usar `grep_search` e ler trechos específicos com intervalo de linhas em vez de ler o arquivo completo.",
                "mecanica": "Impõe restrição comportamental: antes de ler qualquer arquivo com mais de 50 linhas, o agente deve localizar o símbolo exato via grep ou AST e ler apenas a fatia <code>StartLine/EndLine</code>.",
                "cmd": "# Regra: 'Grep antes de read. Limitar leitura por intervalo estrito de linhas'",
                "como_usar": "1. Ao pedir para o agente alterar uma função em um arquivo de 1.500 linhas, ele faz <code>grep_search</code> pelo nome da função.<br>2. Em seguida, faz <code>view_file(StartLine=120, EndLine=145)</code>.<br>3. Lê 25 linhas em vez de 1.500 linhas, mantendo o contexto limpo para raciocínios complexos.",
                "spec": "0 MB RAM / Disciplina de agente",
                "truth": "A maior causa de esquecimento em conversas longas é a poluição do contexto com arquivos lidos integralmente sem necessidade.",
                "repo": "github.com/topics/context-engineering"
            },
            {
                "rank": "04", "name": "Skill: rtk-memory", "cat": "Persistent Prefix Cache Memory", "lic": "MIT / Scratchpad Skill",
                "substitui": "Reenvio de histórico antigo no prompt", "econ": "100% de reuso de prefix cache da Anthropic/OpenAI",
                "entrega": "Persiste novos aprendizados e correções em um arquivo externo (<code>RTK-SCRATCHPAD.md</code>) para manter as instruções base imutáveis.",
                "mecanica": "Mantém o arquivo de governança principal (<code>AGENTS.md</code> / <code>CLAUDE.md</code>) intacto para que os provedores de LLM façam cache do prompt de sistema. Novos aprendizados da sessão são appendados em arquivo separado consultado sob demanda.",
                "cmd": "# Regra: 'Novos aprendizados: SEMPRE appendar em RTK-SCRATCHPAD.md'",
                "como_usar": "1. Quando o agente cometer um erro e for corrigido, ele grava a regra aprendida no final do <code>RTK-SCRATCHPAD.md</code>.<br>2. Em sessões futuras, consulta o scratchpad apenas quando o tema exigir.<br>3. Mantém o cache de prefixo do seu system prompt 100% aquecido e barato.",
                "spec": "Arquivo Markdown local / 0 RAM",
                "truth": "Modificar o system prompt invalida o cache de prefixo em provedores como Anthropic, encarecendo todas as chamadas seguintes.",
                "repo": "github.com/topics/prompt-caching"
            },
            {
                "rank": "05", "name": "Repomix", "cat": "Context Packing", "lic": "MIT",
                "substitui": "Leitura manual de múltiplos arquivos", "econ": "-70% de tokens por prompt (~$ 300/mês)",
                "entrega": "Empacota repositórios inteiros em 1 arquivo XML/Markdown com contagem exata de tokens e filtros inteligentes de .gitignore.",
                "mecanica": "Varre o repositório, descarta binários, lockfiles e arquivos ignorados no Git e compila um documento único com cabeçalhos XML e numeração de linhas para leitura otimizada por LLMs.",
                "cmd": "npx repomix --style xml --output-show-line-numbers",
                "como_usar": "1. Antes de iniciar uma feature complexa, execute: <code>npx repomix --include 'src/**/*.ts'</code>.<br>2. O arquivo <code>repomix-output.xml</code> reúne a arquitetura com contagem de tokens no topo.<br>3. Cole no chat da IA ou anexe no agente para compreensão completa da base.",
                "spec": "< 30 MB RAM / CLI sob demanda",
                "truth": "Remove automaticamente arquivos binários, lockfiles e assets pesados antes de enviar o contexto à LLM.",
                "repo": "github.com/yamadashy/repomix"
            },
            {
                "rank": "06", "name": "ast-grep (sg)", "cat": "AST Search & Rewrite", "lic": "MIT",
                "substitui": "Refatorações caras via LLM", "econ": "100% grátis em transformações estruturais",
                "entrega": "Busca e reescrita de código baseada na Árvore de Sintaxe Abstrata. Não erra espaçamentos nem quebras de linha.",
                "mecanica": "Faz o parsing do código-fonte em nós de Árvore Sintática (AST) usando Tree-sitter em Rust, permitindo buscar e substituir estruturas com wildcards sintáticos (<code>$$$ARGS</code>) em microssegundos.",
                "cmd": "cargo install ast-grep && sg --pattern 'function $NAME($$$ARGS) { $$$BODY }'",
                "como_usar": "1. Para alterar a assinatura de uma função em 50 arquivos, rode: <code>sg -p 'api.get($URL)' -r 'api.fetch({url: $URL})' -w</code>.<br>2. A substituição ocorre em 2ms em todo o repositório.<br>3. Economize 100% dos tokens que seriam gastos pedindo para uma IA reescrever arquivo por arquivo.",
                "spec": "Binário Rust / < 10 MB RAM",
                "truth": "Substitui prompts inteiros de 'renomeie/altere assinatura' por uma chamada determinística de 2ms no terminal.",
                "repo": "ast-grep.github.io"
            },
            {
                "rank": "07", "name": "LiteLLM Semantic Cache / OmniRouter", "cat": "AI Gateway & Cache", "lic": "MIT",
                "substitui": "Chamadas duplicadas em APIs de LLM", "econ": "-40% a -60% na fatura de API (~$ 500/mês)",
                "entrega": "Gateway de roteamento inteligente e cache semântico de respostas de LLM em Redis com balanceamento de carga.",
                "mecanica": "Calcula embeddings de prompts recebidos e faz busca por similaridade de cosseno no Redis antes de disparar requisições para a OpenAI/Anthropic. Se similaridade > 0.95, devolve a resposta cacheada em 2ms.",
                "cmd": "docker run -d -p 4000:4000 ghcr.io/berriai/litellm:main-latest",
                "como_usar": "1. Suba o LiteLLM apontando para seu Redis no arquivo <code>config.yaml</code>.<br>2. Troque a base URL das suas aplicações e scripts para <code>http://localhost:4000</code>.<br>3. Suítes de testes automatizados e perguntas repetidas de usuários respondem em 2ms com custo $ 0.",
                "spec": "~70 MB RAM em repouso",
                "truth": "Essencial para suítes de testes de software e pipelines de CI/CD que rodam os mesmos prompts repetidamente.",
                "repo": "litellm.ai"
            },
            {
                "rank": "08", "name": "DSPy (Stanford)", "cat": "Prompt Compiler", "lic": "MIT",
                "substitui": "Engenharia de prompt manual cara", "econ": "Reduz tamanho de prompt em até 50%",
                "entrega": "Compila e otimiza automaticamente instruções e few-shots via algoritmos matemáticos para máxima acurácia no menor prompt.",
                "mecanica": "Modela o pipeline como grafo computacional diferenciável. Otimizadores como <code>BootstrapFewShot</code> testam permutações de prompts contra uma métrica e geram a versão mais enxuta e assertiva.",
                "cmd": "pip install dspy-ai",
                "como_usar": "1. Defina sua classe de extração: <code>class Extrator(dspy.Module): ...</code>.<br>2. Forneça 10 a 20 exemplos de treino validados.<br>3. Execute o compilador do DSPy: ele gera automaticamente o prompt mais eficiente e curto para produção.",
                "spec": "Biblioteca pura / Zero runtime RAM",
                "truth": "Trata prompts como código compilável. Se você mudar de modelo, basta recompilar o pipeline sem reescrever nada.",
                "repo": "dspy.ai"
            }
        ]
    },
    LISTA_02_EXPANDIDA,
    # 03 - Design, Mídia & Ferramentas de Criação Visual
    # 03 - Design, Mídia & Ferramentas de Criação Visual
    {
        "slug": "03-design-ui-midia-soberana",
        "title": "Design, UI, Mídia Soberana & Upcaling Local",
        "camada": "Camada 03 · Criação Visual & Mídia",
        "accent": "#4A3274", "accent_dark": "#B192E6", "accent_soft": "#E7DFEF", "accent_soft_dark": "#251838",
        "deck": "Suíte soberana para <strong>designers e criadores</strong>: upscaling 4x/8x local com IA (Upscayl), síntese neural de voz (Voicebox/Kokoro), design vetorial em SVG (Penpot), suíte de PDFs (Stirling-PDF) e geração de imagens.",
        "pilar_1": "O Custo do Design por Assento",
        "pilar_1_desc": "Figma ($ 15/user), Topaz Gigapixel ($ 99), ElevenLabs ($ 99/mês), Adobe Acrobat ($ 20/mês) e Midjourney ($ 30/mês). Uma equipe de criação pequena gasta mais de $ 1.500/mês.",
        "pilar_2": "A Alternativa em Padrões Abertos & IA Local",
        "pilar_2_desc": "Upscayl amplia imagens 4x localmente em GPU. Kokoro sintetiza voz em tempo real em CPU. Penpot e Stirling-PDF garantem 100% de privacidade e zero licenças por assento.",
        "itens": [
            {
                "rank": "01", "name": "Upscayl", "cat": "AI Image Upscaler", "lic": "AGPL-3.0",
                "substitui": "Topaz Gigapixel ($ 99) / Magnific AI ($ 39/mês)", "econ": "-$ 468 / ano por designer",
                "entrega": "Aumenta a resolução de imagens e fotos em 4x e 8x usando redes neurais Real-ESRGAN aceleradas por Vulkan localmente.",
                "mecanica": "Executa modelos de super-resolução via Vulkan API em qualquer GPU (Nvidia, AMD, Intel). Reconstrói detalhes de texturas, remove ruídos de compressão JPG e entrega imagens nítidas sem enviar arquivos para a nuvem.",
                "cmd": "winget install Upscayl.Upscayl || brew install --cask upscayl",
                "como_usar": "1. Abra o Upscayl no desktop e arraste fotos de produtos, ilustrações ou artes geradas por IA.<br>2. Selecione o modelo (ex: 'Digital Art' para ilustrações ou 'Ultra Sharp' para fotos).<br>3. Clique em 'Upscayl': a imagem de 512x512 vira 4096x4096 em 5 segundos na sua GPU local com qualidade cristalina para impressão.",
                "spec": "VRAM da GPU sob demanda / Roda em GPU integrada",
                "truth": "O melhor upscaler open-source do mundo, roda 100% offline e não cobra por imagem processada.",
                "repo": "github.com/upscayl/upscayl"
            },
            {
                "rank": "02", "name": "Voicebox / Kokoro-82M", "cat": "Neural Voice Synthesis", "lic": "Apache-2.0",
                "substitui": "ElevenLabs ($ 99-$ 330/mês)", "econ": "-$ 1.200 a $ 4.000 / ano",
                "entrega": "Síntese e clonagem de voz neural hiper-realista com apenas 82M de parâmetros rodando em tempo real em CPU comum.",
                "mecanica": "Combina arquitetura StyleTTS2 com vocoder HiFi-GAN via ONNX Runtime. Sintetiza áudio com entonação, respiração e modulação natural com latência inferior a 100ms em CPU sem necessidade de GPUs caras.",
                "cmd": "pip install kokoro-onnx soundfile",
                "como_usar": "1. No seu script Python de geração de podcasts ou narração de vídeos, passe o texto em português.<br>2. Gere o áudio: <code>audio, sr = kokoro.create('Bem-vindo à nossa plataforma', voice='pt_br')</code>.<br>3. Salve o arquivo <code>.wav</code> em menos de 1 segundo sem pagar nenhum centavo por caractere.",
                "spec": "< 150 MB RAM em inferência",
                "truth": "Gere horas de narração, podcasts e áudios para agentes sem pagar por caractere gerado.",
                "repo": "github.com/hexgrad/kokoro"
            },
            {
                "rank": "03", "name": "Penpot", "cat": "UI/UX Design & Prototyping", "lic": "MPL-2.0",
                "substitui": "Figma ($ 15/designer/mês)", "econ": "-$ 1.800 / ano para equipe de 10 pessoas",
                "entrega": "Plataforma de design e prototipagem baseada em padrões web (SVG real, Flexbox e CSS Grid nativo).",
                "mecanica": "Construído em ClojureScript e Rust. Ao contrário do Figma que usa formatos binários fechados, o Penpot renderiza SVG puro no canvas, permitindo que as propriedades de layout mapeiem diretamente para propriedades CSS nativas.",
                "cmd": "docker compose -f docker-compose.penpot.yml up -d",
                "como_usar": "1. Suba o Penpot no seu servidor com Docker.<br>2. Crie layouts responsivos usando Flexbox e Grid reais.<br>3. Compartilhe o link com os desenvolvedores: eles copiam o código CSS exato sem cobrança por licenças de visualizador.",
                "spec": "~450 MB RAM",
                "truth": "Sem cobrança por visualizadores ou desenvolvedores inspecionando o código do design.",
                "repo": "penpot.app"
            },
            {
                "rank": "04", "name": "Stirling-PDF", "cat": "PDF Toolkit", "lic": "GPL-3.0",
                "substitui": "Adobe Acrobat Pro ($ 239/ano)", "econ": "-$ 239 / ano por usuário",
                "entrega": "Mais de 50 operações: OCR, divisão, conversão para Word/Excel, assinatura digital e censura de dados confidenciais.",
                "mecanica": "Aplicação Java Spring Boot empacotada com utilitários de baixo nível (Apache PDFBox, OCRmyPDF, LibreOffice, Ghostscript) expondo uma interface web moderna e API REST completa.",
                "cmd": "docker run -d -p 8080:8080 frooodle/s-pdf:latest",
                "como_usar": "1. Acesse <code>http://localhost:8080</code> no navegador do escritório.<br>2. Selecione 'Redact' para censurar CPFs e dados bancários de contratos antes do envio externo.<br>3. Use 'OCR PDF' para tornar documentos escaneados pesquisáveis sem enviar dados para a nuvem.",
                "spec": "~150 MB RAM",
                "truth": "Nenhum documento confidencial da empresa é enviado para sites suspeitos de conversão na internet.",
                "repo": "github.com/Stirling-Tools/Stirling-PDF"
            },
            {
                "rank": "05", "name": "ComfyUI", "cat": "Generative AI Canvas", "lic": "GPL-3.0",
                "substitui": "Midjourney / DALL-E ($ 30-$ 60/mês)", "econ": "-$ 360 a $ 720 / ano",
                "entrega": "A interface baseada em nós mais potente para Stable Diffusion, FLUX e SDXL com controle total sobre cada etapa da geração.",
                "mecanica": "Executa o pipeline de difusão de tensores como um grafo acíclico dirigido. Cada etapa (carregamento de modelo, text encoding, CLIP vision, amostragem KSampler, VAE decoding) é desacoplada e modularizada.",
                "cmd": "git clone https://github.com/comfyanonymous/ComfyUI && python main.py",
                "como_usar": "1. Abra a interface de nós e monte seu workflow de geração de banners.<br>2. Arraste qualquer imagem gerada anteriormente para o canvas para restaurar os nós exatos que a criaram.<br>3. Gere imagens consistentes em lote com controle preciso de iluminação e pose via ControlNet.",
                "spec": "VRAM da GPU sob demanda",
                "truth": "Reproduzibilidade total de workflows de geração de imagens com salvamento de nós no próprio PNG.",
                "repo": "comfy.org"
            },
            {
                "rank": "06", "name": "AFFiNE / Excalidraw", "cat": "Canvas & Whiteboard", "lic": "MIT",
                "substitui": "Miro / Whimsical ($ 10/user/mês)", "econ": "-$ 1.200 / ano (equipe de 10)",
                "entrega": "Quadro branco infinito com notas estruturadas, post-its, diagramas e suporte a desenho livre colaborativo.",
                "mecanica": "Utiliza CRDTs (Conflict-free Replicated Data Types) via Yjs para permitir colaboração em tempo real sem servidor central. O motor de renderização em Canvas 2D desenha formas vetoriais com efeito de rascunho feito à mão.",
                "cmd": "docker run -d -p 3010:3010 affine/affine:latest",
                "como_usar": "1. Abra durante sessões de brainstorming e planejamento de sprint.<br>2. Desenhe a arquitetura de microserviços arrastando blocos e setas magnéticas.<br>3. Exporte em SVG ou PNG transparente e cole diretamente no README do repositório.",
                "spec": "~140 MB RAM",
                "truth": "Quadros ilimitados sem travas de plano freemium.",
                "repo": "affine.pro"
            },
            {
                "rank": "07", "name": "Iconify", "cat": "Universal Icon Framework", "lic": "MIT / Apache-2.0",
                "substitui": "FontAwesome Pro / Noun Project ($ 99/ano)", "econ": "-$ 99 / ano por projeto",
                "entrega": "Mais de 200.000 ícones vetoriais de todas as coleções do mundo (Lucide, Material, Tabler, Carbon) em 1 único formato unificado.",
                "mecanica": "Armazena ícones como JSON estruturado de caminhos SVG. Os plugins de bundler (Vite, Webpack) extraem apenas os nós <code>&lt;path&gt;</code> utilizados e inserem inline no HTML final, sem carregar fontes de ícones pesadas.",
                "cmd": "npm install @iconify/react",
                "como_usar": "1. Escolha qualquer ícone do catálogo unificado.<br>2. Use no seu componente: <code>&lt;Icon icon='lucide:database' className='text-emerald-500' /&gt;</code>.<br>3. Mude de coleção de ícones sem precisar instalar novas bibliotecas nem aumentar o tamanho do bundle.",
                "spec": "Bundle size sob demanda",
                "truth": "Carregamento dinâmico apenas dos SVGs usados no projeto, sem carregar fontes de 5MB.",
                "repo": "iconify.design"
            },
            {
                "rank": "08", "name": "Fontsource", "cat": "Self-Hosted Typography", "lic": "MIT / OFL",
                "substitui": "Google Fonts (Vazamento de IP / LGPD)", "econ": "Zero dependência externa e 100% compliance LGPD",
                "entrega": "Fontes tipográficas de alta qualidade empacotadas como módulos NPM para auto-hospedagem sem conexões ao Google.",
                "mecanica": "Empacota arquivos WOFF2 de fontes de código aberto divididos por subconjuntos Unicode. O bundler copia os arquivos para a pasta pública de assets e gera regras <code>@font-face</code> com <code>font-display: swap</code>.",
                "cmd": "npm install @fontsource/inter",
                "como_usar": "1. Instale a fonte no projeto: <code>npm install @fontsource/fira-code</code>.<br>2. No seu arquivo CSS global, adicione: <code>import '@fontsource/fira-code/400.css';</code>.<br>3. Sua aplicação carrega instantaneamente do cache local e cumpre 100% dos requisitos de privacidade da LGPD.",
                "spec": "Arquivos WOFF2 locais",
                "truth": "Evita multas de privacidade (como as decisões judiciais europeias sobre Google Fonts) e acelera o carregamento.",
                "repo": "fontsource.org"
            }
        ]
    },
    # 05 - RAG, Conhecimento & Bases Locais (AnythingLLM, NoteGen, Qdrant)
    {
        "slug": "05-rag-vetores-grafos",
        "title": "RAG Cirúrgico, Bancos Vetoriais & Apps de Conhecimento Local",
        "camada": "Camada 05 · Recuperação de Conhecimento & RAG",
        "accent": "#1E5E4E", "accent_dark": "#6BBFA8", "accent_soft": "#DBEDE7", "accent_soft_dark": "#142B24",
        "deck": "A infraestrutura de conhecimento local: <strong>AnythingLLM desktop/server para documentos privados, NoteGen para notas com IA, Qdrant vetorial, Late Interaction (ColBERT)</strong> e grafos de código.",
        "pilar_1": "O Fracasso do RAG Tradicional em Nuvem",
        "pilar_1_desc": "Subir PDFs sigilosos para provedores fechados vaza dados estratégicos e custa caro por consulta. O particionamento ingênuo quebra tabelas e números.",
        "pilar_2": "A Soberania do Conhecimento Local",
        "pilar_2_desc": "AnythingLLM e NoteGen organizam bases locais com LanceDB e SQLite embutidos. Qdrant e ColBERT entregam precisão cirúrgica sem enviar nenhum byte para a internet.",
        "itens": [
            {
                "rank": "01", "name": "AnythingLLM", "cat": "All-in-One Desktop/Server RAG", "lic": "MIT",
                "substitui": "Chatbase / Dify Cloud / Pinecone ($ 99/mês)", "econ": "-$ 1.188 / ano por organização",
                "entrega": "Aplicação completa de chat com documentos locais, suporte a múltiplos workspaces, permissões de usuários e banco LanceDB embutido.",
                "mecanica": "Gerencia pipelines de ingestão de PDFs, planilhas, páginas web e repositórios. Conecta a qualquer LLM (Ollama local ou APIs comerciais) e faz busca vetorial embutida com zero configuração de infraestrutura.",
                "cmd": "docker run -d -p 3001:3001 -v anythingllm_data:/app/server/storage mintplexlabs/anythingllm",
                "como_usar": "1. Abra o AnythingLLM no desktop ou servidor (porta 3001).<br>2. Crie um workspace chamado 'Contratos 2026' e arraste 50 arquivos PDF.<br>3. Converse com seus documentos: o AnythingLLM cita as páginas e parágrafos exatos com 100% de privacidade.",
                "spec": "~120 MB RAM / Banco LanceDB embutido",
                "truth": "A forma mais rápida e segura de entregar RAG corporativo para equipes não-técnicas sem risco de vazamento de dados.",
                "repo": "anythingllm.com"
            },
            {
                "rank": "02", "name": "NoteGen / Analog Knowledge", "cat": "Local AI Note Manager", "lic": "MIT",
                "substitui": "Notion AI ($ 10/user/mês)", "econ": "-$ 120 / ano por usuário",
                "entrega": "Gerenciador de notas e documentações estruturadas em Markdown puro com IA local para síntese, categorização e busca semântica.",
                "mecanica": "Armazena arquivos Markdown em pastas locais no disco do usuário. Utiliza embeddings leves para conectar notas relacionadas e modelos Ollama para reescrever, resumir e expandir tópicos sem conexão com a internet.",
                "cmd": "npm install -g notegen && notegen start",
                "como_usar": "1. Abra sua pasta de notas no NoteGen.<br>2. Use o atalho de IA para gerar atas de reunião estruturadas a partir de anotações soltas.<br>3. Suas notas continuam como arquivos <code>.md</code> abertos e versionáveis no Git para sempre.",
                "spec": "< 40 MB RAM / Arquivos locais em disco",
                "truth": "Seus pensamentos e notas estratégicas não devem ficar trancados em bancos de dados proprietários na nuvem.",
                "repo": "github.com/topics/pkm"
            },
            {
                "rank": "03", "name": "Qdrant", "cat": "Vector Database", "lic": "Apache-2.0",
                "substitui": "Pinecone ($ 70-$ 500/mês)", "econ": "-$ 840 a $ 6.000 / ano",
                "entrega": "Banco vetorial em Rust com suporte a busca híbrida (vetores densos + esparsos BM25) e filtragem avançada de metadados.",
                "mecanica": "Implementa índices HNSW com filtragem de payload em tempo real. Permite cruzar filtros booleanos rígidos com busca vetorial de cosseno sem penalidade de performance.",
                "cmd": "docker run -d -p 6333:6333 -v qdrant_data:/qdrant/storage qdrant/qdrant",
                "como_usar": "1. Suba o Qdrant via Docker na porta 6333.<br>2. Crie uma coleção com vetores densos e esparsos para busca híbrida.<br>3. Faça buscas com filtros de metadados combinando similaridade semântica e exata com latência de 3ms.",
                "spec": "~40 MB RAM em repouso",
                "truth": "Roda milhões de vetores com latência de resposta de poucos milissegundos sem limites de pods.",
                "repo": "qdrant.tech"
            },
            {
                "rank": "04", "name": "RAGatouille (ColBERT)", "cat": "Late Interaction Retrieval", "lic": "Apache-2.0",
                "substitui": "Embeddings vetoriais médios simples", "econ": "Aumenta a precisão do RAG em 30%+",
                "entrega": "Implementa ColBERTv2 com facilidade em Python: compara cada token da pergunta com cada token dos documentos.",
                "mecanica": "Gera múltiplos vetores de dimensão reduzida (1 por token) e utiliza o operador MaxSim para calcular a relevância token a token, capturando detalhes minuciosos que embeddings médios perdem.",
                "cmd": "pip install ragatouille",
                "como_usar": "1. Indexe seus documentos: <code>RAG.index(collection=documentos, index_name='manual')</code>.<br>2. Consulte: <code>RAG.search('qual a cláusula de rescisão?')</code>.<br>3. Obtenha os trechos exatos com destaque de relevância por palavra.",
                "spec": "Indexação rápida em GPU/CPU",
                "truth": "Encontra a resposta exata em contratos jurídicos e tabelas financeiras onde embeddings convencionais falham.",
                "repo": "github.com/bclavie/RAGatouille"
            },
            {
                "rank": "05", "name": "Unstructured", "cat": "Document Ingestion ETL", "lic": "Apache-2.0",
                "substitui": "Parsers ingênuos de PDF", "econ": "Elimina 90% das falhas de corte de texto",
                "entrega": "Particiona PDFs, apresentações e planilhas preservando títulos, subtítulos, parágrafos e tabelas intactas.",
                "mecanica": "Utiliza modelos de detecção de layout e heurísticas para classificar blocos de texto (Title, NarrativeText, Table, ListItem), gerando metadados ricos para cada pedaço (chunk).",
                "cmd": "pip install \"unstructured[all-docs]\"",
                "como_usar": "1. Passe o arquivo bruto: <code>elements = partition(filename='relatorio.pdf')</code>.<br>2. O Unstructured extrai tabelas em HTML e parágrafos separadamente.<br>3. Envie os blocos estruturados diretamente para o banco vetorial.",
                "spec": "Execução sob demanda",
                "truth": "A qualidade do seu RAG é determinada pela qualidade da ingestão. Sem particionamento estruturado, o RAG falha.",
                "repo": "unstructured.io"
            },
            {
                "rank": "06", "name": "FastEmbed", "cat": "Local Embeddings", "lic": "Apache-2.0",
                "substitui": "OpenAI Embeddings API ($ 0.10/1M tokens)", "econ": "100% grátis e offline",
                "entrega": "Gera embeddings BGE e multilingual diretamente no processo Python em frações de milissegundo com ONNX Runtime.",
                "mecanica": "Carrega modelos quantizados de embedding (BGE-small, MiniLM) diretamente em C++ via ONNX Runtime, sem carregar PyTorch ou CUDA pesado.",
                "cmd": "pip install fastembed",
                "como_usar": "1. Instancie: <code>model = TextEmbedding()</code>.<br>2. Converta textos em vetores: <code>embeddings = list(model.embed(textos))</code>.<br>3. Gere milhares de vetores por segundo sem bater em nenhuma API externa.",
                "spec": "< 50 MB RAM por modelo",
                "truth": "Elimina a dependência de chamadas de rede para transformar textos em vetores.",
                "repo": "github.com/qdrant/fastembed"
            },
            {
                "rank": "07", "name": "DuckDB", "cat": "In-Process Analytical DB", "lic": "MIT",
                "substitui": "Data Warehouses caros (Snowflake)", "econ": "-$ 500+/mês em consultas analíticas",
                "entrega": "Banco analítico colunar executado no mesmo processo com suporte nativo a leitura de arquivos Parquet e vetores.",
                "mecanica": "Motor OLAP colunar vetorizado em C++ que processa blocos de dados em registradores de CPU com suporte a multithreading automático e leitura direta de arquivos do disco.",
                "cmd": "pip install duckdb",
                "como_usar": "1. Consulte arquivos locais com SQL puro: <code>SELECT * FROM 'logs/*.parquet' WHERE status = 500</code>.<br>2. Agregue milhões de linhas em milissegundos.<br>3. Exporte os resultados resumidos diretamente para alimentar a LLM.",
                "spec": "Execução local ultra-rápida",
                "truth": "Processa milhões de linhas de metadados e logs em milissegundos direto do disco local.",
                "repo": "duckdb.org"
            },
            {
                "rank": "08", "name": "LanceDB", "cat": "Embedded Serverless Vector", "lic": "Apache-2.0",
                "substitui": "Bancos vetoriais em nuvem", "econ": "Zero custo de servidor gerenciado",
                "entrega": "Banco vetorial serverless embutido em Rust baseado no formato colunar Lance. Consulta direto do NVMe sem consumir RAM.",
                "mecanica": "Utiliza o formato colunar Lance otimizado para vetores e dados multimodais. Executa buscas ANN direto do SSD usando Zero-Copy, consumindo quase zero de RAM.",
                "cmd": "pip install lancedb",
                "como_usar": "1. Conecte no Python: <code>db = lancedb.connect('./meu_lancedb')</code>.<br>2. Crie tabelas passando DataFrames com vetores.<br>3. Realize consultas diretamente do disco com latência ultrabaixa sem subir servidores.",
                "spec": "Consumo de RAM quase zero",
                "truth": "Ideal para aplicações desktop, extensões e pipelines que precisam de busca vetorial rápida sem subir containers.",
                "repo": "lancedb.com"
            }
        ]
    },
    # 12 - DevOps, Infraestrutura & Monitoramento (Uptime Kuma, Coolify, Stacher)
    {
        "slug": "12-devops-borda-infraestrutura",
        "title": "DevOps, Borda, Monitoramento & Utilitários de Servidor",
        "camada": "Camada 12 · Resiliência de Servidores & Monitoramento",
        "accent": "#1E5E4E", "accent_dark": "#6BBFA8", "accent_soft": "#DBEDE7", "accent_soft_dark": "#142B24",
        "deck": "A infraestrutura soberana: <strong>monitoramento em tempo real (Uptime Kuma), PaaS próprio (Coolify), downloads de mídia sem restrições (Stacher / yt-dlp)</strong>, proxy TLS automático (Caddy) e backups imutáveis.",
        "pilar_1": "O Custo de Monitoramento & Hospedagem Fechada",
        "pilar_1_desc": "BetterUptime ($ 30/mês), Heroku/Vercel ($ 50-$ 300/mês), Scrapers comerciais e ferramentas proprietárias cobram mensalidades por tudo.",
        "pilar_2": "A Soberania da Borda & Painéis Próprios",
        "pilar_2_desc": "Uptime Kuma monitora todos os seus serviços com alertas imediatos no Telegram/Discord. Coolify gerencia deploys automáticos em VPS de $ 5/mês.",
        "itens": [
            {
                "rank": "01", "name": "Uptime Kuma", "cat": "Self-Hosted Uptime Monitor", "lic": "MIT",
                "substitui": "BetterUptime / Pingdom / UptimeRobot ($ 30-$ 80/mês)", "econ": "-$ 360 a $ 960 / ano",
                "entrega": "Painel de monitoramento de status de sites, APIs HTTP(s), portas TCP, containers Docker, DNS e certificados SSL com alertas imediatos.",
                "mecanica": "Executa verificações assíncronas em intervalos configuráveis (ex: a cada 20s). Possui suporte nativo a mais de 90 serviços de notificação (Telegram, Discord, Slack, Webhooks, WhatsApp) e cria páginas públicas de status personalizadas.",
                "cmd": "docker run -d --restart=always -p 3001:3001 -v uptime-kuma:/app/data louislam/uptime-kuma:1",
                "como_usar": "1. Acesse <code>http://localhost:3001</code> e crie sua conta de administrador.<br>2. Adicione seus sites e APIs informando a URL e o intervalo de checagem.<br>3. Configure alertas para seu canal do Telegram: receba notificações instantâneas se qualquer serviço cair ou se o certificado SSL estiver perto de vencer.",
                "spec": "~60 MB RAM em repouso",
                "truth": "Interface moderna, leve e que substitui com perfeição qualquer serviço comercial caro de status page.",
                "repo": "github.com/louislam/uptime-kuma"
            },
            {
                "rank": "02", "name": "Stacher (yt-dlp GUI)", "cat": "Media Scraper & Downloader", "lic": "GPL-3.0 / Free",
                "substitui": "4K Video Downloader ($ 25) / Scraper APIs", "econ": "Downloads ilimitados de mídia em 4K",
                "entrega": "Interface desktop moderna e veloz para o <code>yt-dlp</code>, permitindo baixar vídeos, playlists inteiras e áudios MP3 de mais de 1.000 sites.",
                "mecanica": "Envelopa o binário <code>yt-dlp</code> e <code>ffmpeg</code> com uma interface visual reativa. Extrai streams de vídeo, faz bypass de restrições de idade e converte formatos com aceleração de hardware.",
                "cmd": "# Baixe o executável em stacher.io ou use yt-dlp via CLI: yt-dlp -x --audio-format mp3 URL",
                "como_usar": "1. Abra o Stacher no seu computador.<br>2. Cole o link de um vídeo ou playlist do YouTube/Vimeo.<br>3. Selecione o formato desejado (MP4 4K ou MP3 de alta fidelidade) e clique em Download para salvar localmente sem anúncios.",
                "spec": "< 50 MB RAM",
                "truth": "Essencial para arquivar palestras, vídeos de referência e criar datasets de áudio/vídeo locais para treinamento de IA.",
                "repo": "stacher.io"
            },
            {
                "rank": "03", "name": "Coolify", "cat": "Self-Hosted PaaS", "lic": "Apache-2.0",
                "substitui": "Heroku / Vercel Pro ($ 50-$ 300/mês)", "econ": "-$ 600 a $ 3.600 / ano",
                "entrega": "Painel de deploy completo: publique aplicações Node, Python, PHP, Rust e bancos de dados (Postgres, Redis, Mongo) com Git push automático.",
                "mecanica": "Control plane de gerenciamento de containers e servidores em Linux. Conecta-se via SSH, provisiona Traefik com TLS automático, gerencia bancos de dados e constrói imagens via Nixpacks/Dockerfiles com zero downtime deploy.",
                "cmd": "curl -fsSL https://cdn.coollabs.io/coolify/install.sh | bash",
                "como_usar": "1. Acesse o painel do Coolify e conecte sua conta do GitHub ou repositório Git.<br>2. Crie uma nova aplicação e selecione o branch de produção.<br>3. A cada <code>git push</code>, o Coolify detecta a alteração, compila a imagem, renova o certificado SSL e coloca no ar automaticamente.",
                "spec": "~350 MB RAM",
                "truth": "Permite transformar qualquer VPS de $ 5/mês em um Vercel/Heroku privado ilimitado.",
                "repo": "github.com/coollabsio/coolify"
            },
            {
                "rank": "04", "name": "Caddy", "cat": "Auto-TLS Web Server", "lic": "Apache-2.0",
                "substitui": "Nginx + Certbot com configuração complexa", "econ": "Zero falhas de renovação de SSL",
                "entrega": "Servidor web e proxy reverso moderno em Go com certificados HTTPS automáticos por padrão via Let's Encrypt.",
                "mecanica": "Gerencia o ciclo de vida dos certificados TLS via ACME protocol diretamente no processo em Go. Se o certificado expirar em 30 dias, renova em background sem reiniciar o servidor.",
                "cmd": "caddy reverse-proxy --from meudominio.com --to 127.0.0.1:3000",
                "como_usar": "1. Crie um arquivo <code>Caddyfile</code> com 2 linhas: <code>app.empresa.com { reverse_proxy localhost:3000 }</code>.<br>2. Inicie o Caddy: <code>caddy run</code>.<br>3. Sua aplicação está no ar com HTTPS A+ e HTTP/3 ativado sem precisar rodar scripts de Certbot.",
                "spec": "~30 MB RAM",
                "truth": "Elimina 100% dos incidentes de sites fora do ar por certificado SSL expirado.",
                "repo": "caddyserver.com"
            },
            {
                "rank": "05", "name": "Restic", "cat": "Immutable Backup", "lic": "BSD-2-Clause",
                "substitui": "Veeam ($ 500+/ano) / Softwares pagos de backup", "econ": "-$ 500 / ano",
                "entrega": "Backups criptografados, deduplicados e verificáveis diretamente para qualquer bucket S3 ou servidor remoto.",
                "mecanica": "Divide arquivos em pedaços usando Content-Defined Chunking (Rabin Fingerprints). Pedaços idênticos são armazenados apenas uma vez, economizando até 80% do espaço de armazenamento.",
                "cmd": "restic backup /var/dados --repo s3:s3.amazonaws.com/meu-backup",
                "como_usar": "1. Inicialize o repositório: <code>restic init</code>.<br>2. Crie uma tarefa cron diária: <code>restic backup /app/data</code>.<br>3. Restaure snapshots de qualquer dia com <code>restic restore latest --target /restaurado</code> em segundos.",
                "spec": "CLI sob demanda",
                "truth": "Seus backups são protegidos por criptografia de ponta a ponta e imunes a ransomware.",
                "repo": "restic.net"
            },
            {
                "rank": "06", "name": "VictoriaMetrics", "cat": "Lightweight TSDB", "lic": "Apache-2.0",
                "substitui": "Datadog Metrics ($ 15/host/mês)", "econ": "-$ 1.800 / ano (10 hosts)",
                "entrega": "Banco de dados de séries temporais para monitoramento de métricas com 1/5 do consumo de RAM do Prometheus.",
                "mecanica": "Armazena métricas com compressão colunar avançada em disco e executa queries MetricsQL compatíveis com PromQL com alto paralelismo.",
                "cmd": "docker run -d -p 8428:8428 victoriametrics/victoria-metrics",
                "como_usar": "1. Suba o container na porta 8428.<br>2. Aponte suas aplicações e exporters de servidor.<br>3. Conecte o Grafana e monte dashboards de CPU, memória e requisições sem sobrecarregar o servidor.",
                "spec": "~50 MB RAM",
                "truth": "Muito mais rápido e leve que o Prometheus legado para infraestruturas enxutas.",
                "repo": "victoriametrics.com"
            },
            {
                "rank": "07", "name": "Headscale", "cat": "Mesh VPN Control Plane", "lic": "BSD-3-Clause",
                "substitui": "Tailscale Business ($ 5/user/mês)", "econ": "-$ 600 / ano (10 users)",
                "entrega": "Servidor de controle open-source auto-hospedado para redes WireGuard mesh privadas.",
                "mecanica": "Coordena a troca de chaves públicas WireGuard entre os nós da rede, permitindo conexões diretas ponto a ponto (peer-to-peer) com NAT traversal (STUN/DERP) sem expor portas na internet.",
                "cmd": "docker run -d -p 8080:8080 headscale/headscale",
                "como_usar": "1. Suba o Headscale em uma VPS barata.<br>2. Nos seus computadores e servidores, conecte o cliente Tailscale apontando para o seu IP.<br>3. Acesse bancos de dados e painéis internos usando IPs privados seguros de qualquer lugar do mundo.",
                "spec": "~25 MB RAM",
                "truth": "Você tem sua própria rede mesh segura sem depender dos servidores centrais da Tailscale Inc.",
                "repo": "github.com/juanfont/headscale"
            },
            {
                "rank": "08", "name": "Portainer CE", "cat": "Container Management UI", "lic": "Zlib",
                "substitui": "Portainer Business ($ 150/ano)", "econ": "-$ 150 / ano",
                "entrega": "Painel visual para gestão de containers, volumes, redes e stacks Docker com visualização de logs e console web.",
                "mecanica": "Comunica-se diretamente com o socket <code>/var/run/docker.sock</code> e expõe uma interface web responsiva para criar, pausar, reiniciar e inspecionar containers em tempo real.",
                "cmd": "docker run -d -p 9000:9000 -v /var/run/docker.sock:/var/run/docker.sock portainer/portainer-ce",
                "como_usar": "1. Abra a porta 9000 no navegador.<br>2. Visualize o consumo de CPU e RAM de cada container em execução.<br>3. Suba novos stacks com arquivos <code>docker-compose.yml</code> diretamente pelo editor visual.",
                "spec": "~40 MB RAM",
                "truth": "A forma mais simples de gerenciar múltiplos containers em servidores remotos sem depender de comandos complexos no terminal.",
                "repo": "portainer.io"
            }
        ]
    }
]

def compilar_todas_listas_com_skills_e_trincheira():
    docs_dir = Path("docs/listas")
    output_dir = Path("output/listas-open-source")
    brain_dir = Path(r"C:\Users\trcnologia\.gemini\antigravity-cli\brain\0e2afde3-829c-4443-b5a5-7a8779eeb139")

    docs_dir.mkdir(parents=True, exist_ok=True)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Carregar as listas detalhadas
    import importlib.util
    spec = importlib.util.spec_from_file_location("gerar_catalogo", "scripts/gerar_catalogo_completo_30.py")
    modulo_catalogo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo_catalogo)
    
    todas_listas = modulo_catalogo.construir_todas_listas_completas()
    
    # Substituir listas com enriquecimento de trincheira e skills
    mapa_especial = {l["slug"]: l for l in CATALOGO_COMPLETO}
    
    listas_finais = []
    for l in todas_listas:
        if l["slug"] in mapa_especial:
            listas_finais.append(mapa_especial[l["slug"]])
        else:
            listas_finais.append(l)

    print(f"[*] Compilando {len(listas_finais)} Compêndios de Soberania & Skills com fichas ricas...")

    for lista in listas_finais:
        slug = lista["slug"]
        html_content = modulo_catalogo.gerar_html_completo(lista)

        file_docs = docs_dir / f"{slug}.html"
        file_output = output_dir / f"{slug}.html"

        file_docs.write_text(html_content, encoding="utf-8")
        file_output.write_text(html_content, encoding="utf-8")

        if brain_dir.exists():
            file_brain = brain_dir / f"{slug}.html"
            file_brain.write_text(html_content, encoding="utf-8")

        print(f"  [OK] {slug}.html compilado com sucesso ({len(lista['itens'])} fichas ricas).")

    print(f"\n[+] Compilação concluída com sucesso.")

if __name__ == "__main__":
    compilar_todas_listas_com_skills_e_trincheira()
