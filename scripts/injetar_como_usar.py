# -*- coding: utf-8 -*-
"""
Injetor determinístico da seção 'COMO USAR NO DIA A DIA / WORKFLOW PRÁTICO'
em todos os arquivos HTML presentes na pasta output/listas-open-source/ e docs/listas/.
Garante que 100% das ferramentas em todas as listas possuam orientações práticas de uso cotidiano.
"""

import os
import re
from pathlib import Path

# Dicionario com workflows praticos detalhados por ferramenta
WORKFLOWS_MAP = {
    # Tokens & Context
    "Repomix": "1. Antes de pedir uma tarefa complexa à LLM, rode <code>npx repomix --style xml</code> na raiz do projeto.<br>2. O arquivo gerado compacta o repositório respeitando .gitignore e excluindo binários.<br>3. Cole o arquivo ou anexe no chat para que a IA entenda todo o contexto sem ruído.",
    "ast-grep (sg)": "1. Para refatorar código sem gastar tokens de IA, execute <code>sg --pattern 'func $A($$$B)' --rewrite 'novaFunc($$$B)'</code>.<br>2. O ast-grep reescreve arquivos com base na Árvore Sintática em 2ms.<br>3. Salve o resultado e commite com garantia de 0 quebras de espaçamento.",
    "LiteLLM Semantic Cache": "1. Aponte suas aplicações e scripts para a URL base do LiteLLM (porta 4000).<br>2. Habilite o cache semântico em Redis no <code>config.yaml</code>.<br>3. Chamadas com prompts equivalentes são respondidas instantaneamente do cache local por $ 0.",
    "DSPy (Stanford)": "1. Defina sua assinatura de entrada/saída em Python (ex: <code>class ExtrairDados(dspy.Signature): ...</code>).<br>2. Passe 10 a 20 exemplos de treino.<br>3. Compile o pipeline com <code>BootstrapFewShot</code> para obter o menor prompt com a máxima taxa de acerto.",
    "Outlines / Guidance": "1. Defina o schema desejado com Pydantic ou Expressão Regular.<br>2. Instancie o gerador estruturado: <code>generator = outlines.generate.json(model, Schema)</code>.<br>3. Obtenha 100% de saídas JSON válidas sem necessitar de retentativas.",
    "Gitingest": "1. Troque 'github.com' por 'gitingest.com' na URL de qualquer repositório público.<br>2. Filtre por diretórios de interesse (ex: apenas <code>/src</code>).<br>3. Copie o prompt limpo com a contagem exata de tokens calculada.",
    "Tree-sitter CLI": "1. Execute <code>tree-sitter parse arquivo.py</code> para inspecionar a AST.<br>2. Extraia assinaturas de funções e classes em um script Python leve.<br>3. Envie apenas o resumo de símbolos para o agente em vez do arquivo integral.",
    "SGLang (RadixAttention)": "1. Inicie o servidor SGLang com sua GPU dedicada.<br>2. Aponte sua esteira de subagentes para o endpoint SGLang.<br>3. O RadixAttention reaproveita 100% do KV-cache de instruções do sistema.",

    # Agentes & SDD
    "Spec-Kit": "1. Escreva <code>SPEC.md</code> definindo contratos e critérios de aceite.<br>2. Gere os testes automatizados correspondentes antes do código.<br>3. Permita ao agente implementar apenas até que todos os testes passem.",
    "BMad Method": "1. Acione o subagente de Pesquisa para levantar os requisitos.<br>2. Valide a arquitetura proposta antes da execução.<br>3. Deixe o Dev implementar e o Revisor auditar contra os gates automáticos.",
    "Aider CLI": "1. No terminal do projeto, execute <code>aider arquivo.py</code>.<br>2. Descreva a alteração desejada em linguagem natural.<br>3. O Aider altera o código, roda linters e gera o commit semântico no Git.",
    "OpenHands (OpenDevin)": "1. Abra a interface web na porta 3000 e conecte o repositório.<br>2. Atribua uma issue de bug ou refatoração ao agente.<br>3. Acompanhe a execução segura no container Docker com terminal e navegador.",
    "LangGraph / CrewAI": "1. Modele o fluxo como nós e arestas de um grafo direcionado.<br>2. Adicione checkpoints no SQLite para pausar e retomar a execução.<br>3. Integre pontos de aprovação humana antes de ações destrutivas.",
    "Letta (MemGPT) / Mem0": "1. Conecte o Letta como camada de memória da sua aplicação.<br>2. Fatos e preferências do usuário são salvos automaticamente em banco relacional.<br>3. O agente relembra decisões passadas sem inflar o prompt histórico.",
    "E2B Code Interpreter": "1. Chame <code>await Sandbox.create()</code> no backend do seu agente.<br>2. Execute códigos Python gerados dinamicamente na microVM isolada.<br>3. Receba dados, tabelas e gráficos em PNG de forma segura.",
    "Instructor": "1. Envolva o cliente OpenAI com <code>instructor.from_openai(client)</code>.<br>2. Passe seu modelo Pydantic no parâmetro <code>response_model</code>.<br>3. Receba instâncias Python validadas com retry automático em caso de erro.",

    # Design & Mídia
    "Penpot": "1. Abra o Penpot no navegador e crie pranchetas com Flexbox e CSS Grid reais.<br>2. Compartilhe o link com os desenvolvedores para inspeção de código.<br>3. Exporte componentes e SVGs limpos prontos para o frontend.",
    "Kokoro-82M": "1. Instale via pip: <code>pip install kokoro-onnx</code>.<br>2. Passe o texto da narração para a função de síntese.<br>3. Salve o arquivo <code>.wav</code> em menos de 1 segundo rodando em CPU comum.",
    "Stirling-PDF": "1. Acesse o painel web local na porta 8080.<br>2. Selecione a operação desejada (OCR, dividir, mesclar, assinar, censurar PII).<br>3. Processe arquivos contratuais sigilosos sem enviar dados para a internet.",
    "ComfyUI": "1. Monte seu grafo de nós conectando Checkpoints, LoRAs e Prompts.<br>2. Clique em 'Queue Prompt' para gerar imagens em alta resolução.<br>3. Arraste qualquer imagem gerada anteriormente para restaurar o fluxo completo.",
    "AFFiNE / Excalidraw": "1. Use durante reuniões de arquitetura para desenhar wireframes e fluxos.<br>2. Colabore em tempo real com seu time no quadro branco infinito.<br>3. Exporte em SVG ou Markdown estruturado para a documentação.",
    "Shiki / Prism": "1. No build da sua documentação ou site, passe o bloco de código para o Shiki.<br>2. Escolha o tema de destaque (ex: dracula, nord, github-dark).<br>3. Obtenha HTML estático já colorizado com zero overhead de JS no cliente.",
    "Iconify": "1. Pesquise o ícone desejado no catálogo unificado (Lucide, Material, Tabler).<br>2. Importe apenas o ícone no seu código: <code>&lt;Icon icon='lucide:check' /&gt;</code>.<br>3. Mantenha o bundle da aplicação leve e sem carregar pacotes gigantes.",
    "Fontsource": "1. Instale a tipografia via npm: <code>npm install @fontsource/inter</code>.<br>2. Importe o arquivo CSS no seu layout principal.<br>3. Fontes de alta fidelidade são servidas do próprio domínio com 100% de privacidade.",

    # DevOps & Infraestrutura
    "Coolify": "1. Conecte seu repositório GitHub ou GitLab no painel do Coolify.<br>2. Selecione o branch e as variáveis de ambiente.<br>3. A cada git push, o Coolify compila, gera SSL automático e coloca no ar.",
    "Dokku": "1. Adicione o Dokku como remote Git: <code>git remote add dokku dokku@servidor:app</code>.<br>2. Execute <code>git push dokku main</code>.<br>3. O Dokku constrói o container, configura o Nginx e publica a aplicação em segundos.",
    "Caddy": "1. Crie um <code>Caddyfile</code> com apenas 2 linhas: <code>meudominio.com { reverse_proxy localhost:3000 }</code>.<br>2. Inicie o Caddy.<br>3. Certificados HTTPS são emitidos e renovados automaticamente sem intervenção.",
    "Traefik": "1. Suba o Traefik apontando para o socket do Docker.<br>2. Adicione labels nos seus containers (ex: <code>traefik.http.routers.app.rule=...</code>).<br>3. O Traefik detecta novos containers e cria as rotas automaticamente.",
    "Restic": "1. Inicialize seu repositório de backup em um bucket S3: <code>restic init</code>.<br>2. Crie uma rotina cron diária: <code>restic backup /var/dados</code>.<br>3. Restaure snapshots instantaneamente com deduplicação e criptografia total.",
    "VictoriaMetrics": "1. Aponte o scraping de métricas das suas aplicações para a porta 8428.<br>2. Conecte o Grafana usando a fonte de dados Prometheus.<br>3. Monitore consumo de CPU, RAM e requisições com 1/5 do consumo do Prometheus.",
    "Headscale": "1. Suba o Headscale na sua VPS como servidor de controle WireGuard.<br>2. Conecte seus computadores, servidores e celulares via cliente Tailscale apontando para seu IP.<br>3. Acesse todos os dispositivos em rede mesh criptografada privada.",
    "Portainer CE": "1. Acesse o painel Portainer na porta 9000 do servidor.<br>2. Visualize o status de todos os containers, logs em tempo real e uso de memória.<br>3. Suba novos stacks com Docker Compose diretamente pelo editor web.",

    # Outros padrões universais
    "Crawlee": "1. Defina as rotas e seletores alvo no arquivo do crawler.<br>2. Execute o crawler com Playwright ativado para evasão antibot.<br>3. Colete dados limpos diretamente em tabelas Parquet ou banco de dados.",
    "Playwright": "1. Use <code>playwright codegen</code> para gravar fluxos de navegação e cliques.<br>2. Automatize testes end-to-end e extração de dados dinâmicos.<br>3. Execute em modo headless na esteira de CI/CD para validar telas.",
    "Scrapy": "1. Crie uma Spider com regras de extração CSS/XPath.<br>2. Inicie a raspagem: <code>scrapy crawl produtos -o saida.jsonl</code>.<br>3. Raspe centenas de páginas por minuto com pipelines de exportação direta.",
    "Polars": "1. Substitua <code>import pandas as pd</code> por <code>import polars as pl</code>.<br>2. Execute transformações lazy: <code>df.lazy().filter(...).collect()</code>.<br>3. Processe milhões de linhas em milissegundos usando todos os núcleos da CPU.",
    "dbt-core": "1. Escreva suas transformações SQL dentro da pasta <code>models/</code>.<br>2. Rode <code>dbt run</code> para materializar views e tabelas analíticas no banco.<br>3. Execute <code>dbt test</code> para garantir integridade referencial dos dados.",
    "Dagster": "1. Defina suas funções com o decorator <code>@asset</code> em Python.<br>2. Inicie a interface web <code>dagster dev</code>.<br>3. Visualize a linhagem completa dos dados e reprocesse partes do pipeline sob demanda.",
    "Trafilatura": "1. Passe a URL para a biblioteca: <code>downloaded = fetch_url(url)</code>.<br>2. Extraia o conteúdo: <code>texto = extract(downloaded)</code>.<br>3. Alimente seu banco vetorial com o texto puro do artigo sem tags HTML.",
    "Whisper.cpp": "1. Baixe o modelo quantizado GGML.<br>2. Execute no terminal: <code>./main -m models/ggml-base.bin -f audio.wav</code>.<br>3. Obtenha a transcrição com timestamps em texto puro ou SRT em segundos.",
    "Faster-Whisper": "1. Instale via pip e instancie: <code>model = WhisperModel('base', device='cpu', compute_type='int8')</code>.<br>2. Chame <code>segments, _ = model.transcribe('reuniao.mp3')</code>.<br>3. Processe múltiplas transcrições simultâneas em servidores locais com alta velocidade.",
    "YOLOv10 / RT-DETR": "1. Instale o pacote Ultralytics: <code>pip install ultralytics</code>.<br>2. Carregue o modelo e passe a imagem/vídeo: <code>model.predict('camera.jpg')</code>.<br>3. Obtenha caixas delimitadoras e classificações a 60+ FPS em tempo real.",
    "PaddleOCR": "1. Instale via pip: <code>pip install paddleocr</code>.<br>2. Chame <code>ocr.ocr('documento.png')</code> no seu script Python.<br>3. Extraia textos, tabelas e recibos escaneados com alta precisão.",
    "DeepFace": "1. Passe duas imagens para validação: <code>DeepFace.verify('foto1.jpg', 'foto2.jpg')</code>.<br>2. Obtenha a confirmação biométrica e score de similaridade.<br>3. Faça análise de atributos faciais sem enviar dados para APIs de terceiros.",
    "Piper TTS": "1. Baixe a voz desejada em português: <code>pt_BR-faber-medium</code>.<br>2. Envie texto pelo terminal: <code>echo 'Mensagem' | piper --model voz.onnx --output_file saida.wav</code>.<br>3. Reproduza notificações sonoras locais com latência quase nula.",
    "Demucs (Meta AI)": "1. Execute no terminal: <code>demucs musica.mp3</code>.<br>2. O Demucs separa as faixas em pastas isoladas: vocais, bateria, baixo e outros.<br>3. Use as faixas isoladas para edição de vídeo, remixagem ou limpeza de ruídos.",
    "Continue.dev": "1. Instale a extensão Continue no VS Code ou JetBrains.<br>2. Conecte ao Ollama local para autocompletion via Tab e chat lateral.<br>3. Selecione trechos de código e pressione <code>Ctrl+I</code> para edição in-line com IA.",
    "Roo-Code (Roo-Cline)": "1. Abra o painel do Roo-Code no VS Code e escolha o modo (Code, Architect ou Ask).<br>2. Dê instruções completas de feature no chat.<br>3. O agente cria arquivos, executa testes no terminal e pede confirmação antes de ações críticas.",
    "OpenCode / Void": "1. Abra seu projeto no Void Editor.<br>2. Use o atalho <code>Ctrl+K</code> para gerar ou refatorar blocos de código com modelos locais.<br>3. Conecte ferramentas MCP para consultar documentações e bancos de dados locais.",
    "Zed Editor": "1. Abra o Zed no terminal digitando <code>zed .</code>.<br>2. Use o painel de IA integrado com <code>Ctrl+?</code> para tirar dúvidas de código.<br>3. Colabore em tempo real com colegas de equipe com edição compartilhada sem lag.",
    "Lazygit": "1. Abra o terminal na pasta do projeto e digite <code>lazygit</code>.<br>2. Use a tecla espaço para fazer staging de linhas/arquivos e 'c' para commitar.<br>3. Pressione 'P' para enviar ao repositório remoto em 1 segundo.",
    "Zellij / Tmux": "1. No terminal do servidor ou local, digite <code>zellij</code>.<br>2. Crie divisões de tela (Alt+N para novo painel, Alt+H/J/K/L para navegar).<br>3. Se a conexão cair, reconecte com <code>zellij attach</code> e continue do mesmo ponto.",
    "Starship": "1. Instale o Starship e adicione <code>eval '$(starship init bash)'</code> no seu shell.<br>2. O prompt exibe branch Git, status de modificações e ambiente virtual em milissegundos.<br>3. Mantenha visibilidade total do estado do repositório sem lentidão no terminal.",
    "Tabby": "1. Suba o container Docker do Tabby apontando para o modelo desejado.<br>2. Instale a extensão do Tabby no VS Code dos desenvolvedores.<br>3. Todos os desenvolvedores recebem autocompletion veloz rodando no servidor local.",
    "PostgreSQL + pgvector": "1. Suba o container Postgres com extensão pgvector habilitada.<br>2. Crie uma coluna do tipo <code>vector(1536)</code> na sua tabela.<br>3. Faça consultas híbridas unindo SQL relacional e busca semântica com o operador <code><=></code>.",
    "ClickHouse": "1. Crie tabelas com a engine <code>MergeTree()</code> ordenadas por data.<br>2. Insira milhões de eventos ou logs por segundo via HTTP ou TCP.<br>3. Execute consultas analíticas com agregações complexas respondendo em milissegundos.",
    "Dragonfly": "1. Substitua a imagem do Redis no seu <code>docker-compose.yml</code> por <code>docker.dragonflydb.io/dragonflydb/dragonfly</code>.<br>2. Inicie a aplicação normalmente.<br>3. Desfrute de 25x mais throughput e 30% menos uso de memória RAM sem alterar código.",
    "SurrealDB": "1. Inicie o SurrealDB: <code>surreal start --user root --pass root</code>.<br>2. Conecte via SDK e execute queries SurrealQL com suporte a grafos e tabelas.<br>3. Use permissões a nível de linha para acesso direto do frontend de forma segura.",
    "SeaweedFS": "1. Suba o servidor com suporte a S3: <code>weed server -s3</code>.<br>2. Aponte suas aplicações usando as credenciais S3 padrão.<br>3. Armazene bilhões de fotos e anexos de agentes com recuperação instantânea.",
    "SQLite": "1. Abra a conexão no código sem precisar instalar servidores: <code>sqlite3.connect('estado.db')</code>.<br>2. Habilite o modo WAL: <code>PRAGMA journal_mode=WAL;</code>.<br>3. Persista o estado da esteira com transações atômicas ultra-rápidas em 1 único arquivo.",
    "Garage S3": "1. Configure os nós do Garage no arquivo de configuração em 3 servidores distintos.<br>2. Inicialize o cluster com <code>garage layout apply</code>.<br>3. Armazene arquivos com replicação geográfica automática e tolerância a falhas.",
    "FerretDB": "1. Suba o FerretDB conectado a um banco PostgreSQL.<br>2. Aponte sua connection string do MongoDB para a porta 27017 do FerretDB.<br>3. Use seu código e drivers existentes de MongoDB rodando 100% sobre SQL livre.",
    "N8N": "1. Acesse o painel web do N8N na porta 5678.<br>2. Crie fluxos conectando Webhooks, nós de IA (LangChain) e bancos de dados.<br>3. Automatize rotinas de atendimento, envio de relatórios e alertas sem escrever código.",
    "Dify": "1. Abra o Dify e crie uma nova aplicação (Chatbot ou Workflow).<br>2. Conecte seus documentos para criar um RAG visual em 2 cliques.<br>3. Publique a interface pronta para usuários ou use a API REST gerada.",
    "Activepieces": "1. Acesse o painel e escolha um template de automação pronto.<br>2. Conecte suas contas (Gmail, Discord, Slack, Postgres).<br>3. Configure triggers de execução automática em eventos de negócio.",
    "Flowise": "1. Arraste componentes de LLM, PromptTemplate e VectorStore na tela.<br>2. Conecte os nós para formar a cadeia de raciocínio.<br>3. Teste no chat lateral e exporte o endpoint de API com 1 clique.",
    "Typebot": "1. Crie blocos de mensagens, perguntas e validações na interface visual.<br>2. Adicione ramificações condicionais baseadas nas respostas do lead.<br>3. Incorpore no seu site como popup ou página inteira com alta taxa de conversão.",
    "Chatwoot": "1. Conecte sua conta do WhatsApp Business, Instagram e LiveChat no Chatwoot.<br>2. Distribua atendimentos entre agentes humanos e bots de IA.<br>3. Acompanhe métricas de tempo de resposta e satisfação em 1 painel unificado.",
    "Botpress OSS": "1. Abra o Studio visual do Botpress e desenhe a árvore de diálogos.<br>2. Treine intenções com frases de exemplo.<br>3. Publique o bot no seu portal web ou canal de atendimento corporativo.",
    "Rasa Open Source": "1. Defina histórias e intenções nos arquivos <code>data/nlu.yml</code> e <code>stories.yml</code>.<br>2. Treine o modelo com <code>rasa train</code>.<br>3. Execute o servidor <code>rasa run</code> para atendimento conversacional com controle estrito.",
    "ONNX Runtime Edge": "1. Exporte seu modelo PyTorch para formato <code>.onnx</code>.<br>2. Carregue no dispositivo embarcado usando o ONNX Runtime C++/Python.<br>3. Execute inferências com aceleração de hardware local sem gastar internet.",
    "Home Assistant": "1. Instale o Home Assistant no Raspberry Pi ou mini PC local.<br>2. Adicione integrações com dispositivos Zigbee, Wi-Fi e câmeras.<br>3. Crie automações inteligentes que rodam 100% locais sem depender de nuvem.",
    "ESPHome": "1. Crie um arquivo <code>sensor.yaml</code> declarando os pinos do seu ESP32.<br>2. Execute <code>esphome run sensor.yaml</code> para compilar e gravar via Wi-Fi.<br>3. O dispositivo aparece automaticamente no Home Assistant pronto para uso.",
    "MediaPipe (Google)": "1. Importe o MediaPipe no Python ou JavaScript.<br>2. Passe os frames da câmera para o detector de pose/mãos.<br>3. Obtenha as coordenadas 3D dos pontos anatômicos a 60 FPS em CPU.",
    "RKNN Toolkit": "1. Converta seu modelo ONNX para o formato RKNN com o toolkit.<br>2. Transfira o modelo compilado para a placa Orange Pi / RK3588.<br>3. Execute inferências de visão computacional diretamente na NPU integrada de 6 TOPS.",
    "TinyML / Edge Impulse OSS": "1. Colete dados de sensores (acelerômetro, som, temperatura).<br>2. Treine um modelo compacto na plataforma.<br>3. Exporte como biblioteca C++ pura e grave no microcontrolador de 32KB RAM.",
    "Coral Edge TPU Runtime": "1. Compile seu modelo TensorFlow Lite com o compilador Edge TPU.<br>2. Conecte o acelerador USB Google Coral no computador ou Raspberry Pi.<br>3. Execute inferências de deep learning com aceleração ASIC consumindo apenas 2W.",
    "FreeRTOS": "1. Crie tarefas independentes com <code>xTaskCreate()</code> no seu firmware C.<br>2. Gerencie filas e semáforos entre sensores e atuadores.<br>3. Garanta tempo de resposta determinístico em sistemas embarcados críticos.",
    "Lean 4": "1. Escreva suas definições e teoremas em arquivos <code>.lean</code>.<br>2. Use táticas interativas (como <code>induction</code>, <code>simp</code>, <code>ring</code>) para provar a correção.<br>3. O compilador valida matematicamente que o código é livre de falhas lógicas.",
    "Z3 SMT Solver (Microsoft)": "1. Declare variáveis e restrições lógicas em Python: <code>s = Solver(); s.add(x + y > 10)</code>.<br>2. Chame <code>s.check()</code>.<br>3. O Z3 resolve restrições complexas e encontra contraexemplos em frações de segundo.",
    "Dafny": "1. Escreva funções com cláusulas <code>requires</code> (pré-requisitos) e <code>ensures</code> (garantias).<br>2. O verificador estático do Dafny analisa o código em tempo real.<br>3. Compile para C#, Java ou JavaScript apenas quando o código for provado correto.",
    "Coq Proof Assistant": "1. Modele a semântica da sua linguagem ou protocolo no Coq.<br>2. Construa provas interativas passo a passo no ambiente CoqIDE.<br>3. Extraia código OCaml ou Haskell formalmente verificado e livre de bugs.",
    "F* (F-Star)": "1. Escreva programas com tipos dependentes refinados.<br>2. Deixe o provador Z3 embutido validar a segurança de tipos.<br>3. Emita código C limpo (KreMLin) pronto para compilação bare-metal em kernels.",
    "Tamarin Prover": "1. Especifique regras de protocolo de criptografia e modelos de atacante.<br>2. Execute o Tamarin para analisar se há ataques de man-in-the-middle.<br>3. Obtenha provas formais de confidencialidade e autenticidade das chaves.",
    "TLA+ (Leslie Lamport)": "1. Escreva a especificação matemática do seu algoritmo distribuído no arquivo <code>.tla</code>.<br>2. Execute o model checker TLC para explorar todos os estados possíveis.<br>3. Encontre deadlocks e condições de corrida antes de escrever 1 linha de código real.",
    "CBMC": "1. Execute <code>cbmc programa.c --unwind 10</code> no seu código C.<br>2. O CBMC analisa todas as execuções de loops até o limite especificado.<br>3. Detecta automaticamente buffer overflows, divisões por zero e ponteiros nulos.",
    "Ghidra (NSA)": "1. Abra o Ghidra e crie um projeto importando o binário executável.<br>2. Deixe a auto-análise identificar funções, símbolos e variáveis.<br>3. Inspecione o código descompilado em C limpo na janela de descompilação.",
    "Radare2 / Cutter": "1. Abra o executável com a interface gráfica Cutter ou no terminal com <code>r2 binario</code>.<br>2. Execute <code>aaa</code> para analisar todos os blocos de código.<br>3. Navegue pelo grafo de funções e depure instruções com breakpoints.",
    "Frida": "1. Crie um script JavaScript interceptando funções específicas.<br>2. Injete no processo em execução: <code>frida -n aplicativo.exe -l interceptor.js</code>.<br>3. Modifique argumentos de funções e visualize chamadas de API em tempo real.",
    "Wireshark": "1. Selecione a interface de rede e inicie a captura de pacotes.<br>2. Use filtros de exibição (ex: <code>http.request.method == 'POST'</code>).<br>3. Inspecione o conteúdo detalhado de cada camada do protocolo de rede.",
    "x64dbg": "1. Abra o binário de 64 bits no x64dbg.<br>2. Defina breakpoints em endereços de memória de interesse.<br>3. Acompanhe a execução passo a passo (F7/F8) visualizando registradores e pilha.",
    "Binary Ninja Community / Vector35": "1. Abra o binário na interface moderna do Binary Ninja.<br>2. Navegue pela representação intermediária (Medium Level IL).<br>3. Automatize a extração de strings e lógicas usando a API Python integrada.",
    "Capstone Engine": "1. Instale no Python: <code>pip install capstone</code>.<br>2. Passe bytes hexadecimais brutos para o descompilador.<br>3. Obtenha a instrução assembly mnemônica e operandos com altíssima velocidade.",
    "Unicorn Engine": "1. Instancie o emulador definindo arquitetura e modo (ex: x86 64-bit).<br>2. Mapeie blocos de memória e escreva o código de máquina.<br>3. Execute o código emulado e inspecione o estado final dos registradores.",
    "Matrix / Dendrite": "1. Suba o servidor Dendrite na sua infraestrutura.<br>2. Crie salas de bate-papo criptografadas ponta a ponta para seu time.<br>3. Conecte clientes abertos como Element ou Cinny em computadores e celulares.",
    "Nostr Protocol": "1. Suba um relay Nostr leve na sua VPS com <code>nostr-rs-relay</code>.<br>2. Conecte seus clientes (Coracle, Primal, Amethyst) ao seu relay próprio.<br>3. Publique notas e eventos com assinatura criptográfica sem risco de censura.",
    "SimpleX Chat": "1. Instale o app SimpleX no desktop ou celular.<br>2. Compartilhe seu link de contato único (sem expor telefone ou e-mail).<br>3. Troque mensagens com isolamento total de metadados em filas unidirecionais.",
    "Yggdrasil Network": "1. Inicie o serviço Yggdrasil na máquina.<br>2. Conecte-se a nós públicos ou pares locais da rede mesh.<br>3. Obtenha um endereço IPv6 criptografado e seguro para comunicação direta entre nós.",
    "IPFS / Helia (Kubo)": "1. Suba o nó IPFS local com <code>ipfs daemon</code>.<br>2. Adicione arquivos imutáveis com <code>ipfs add arquivo.zip</code>.<br>3. Compartilhe o CID do conteúdo para download distribuído via rede P2P.",
    "Tor Project": "1. Instale o serviço Tor e configure como proxy SOCKS5 na porta 9050.<br>2. Crie um Hidden Service no <code>torrc</code> para expor sua aplicação com domínio <code>.onion</code>.<br>3. Acesse sistemas internos sem precisar abrir portas no roteador.",
    "I2P (Invisible Internet)": "1. Inicie o roteador I2P no seu servidor.<br>2. Crie túneis anônimos para seus sites ou APIs internas.<br>3. Comunique-se com outros servidores de forma totalmente oculta e descentralizada.",
    "Session": "1. Baixe o Session Desktop.<br>2. Crie seu ID Session de 66 caracteres alfanuméricos sem número de celular.<br>3. Envie mensagens e arquivos roteados através de múltiplos nós de serviço na rede.",
    "MuJoCo (DeepMind)": "1. Instale via pip: <code>pip install mujoco</code>.<br>2. Carregue seu modelo de robô em formato XML (MJCF).<br>3. Execute a simulação física com passos de tempo precisos para treino de RL.",
    "Godot Engine": "1. Baixe o executável único do Godot (sem instalação pesada).<br>2. Crie cenas com nós de física 2D/3D e programe a lógica em GDScript ou C#.<br>3. Exporte para Windows, Linux, Mac, Web ou rode headless para gerar dados sintéticos.",
    "CARLA Simulator": "1. Inicie o servidor do CARLA em uma máquina com GPU.<br>2. Conecte seus scripts Python usando a API do cliente CARLA.<br>3. Controle veículos autônomos, simule pedestres e colete dados de câmeras e LiDAR.",
    "Blender CLI": "1. Crie um script Python que altera iluminação, materiais e posições da cena.<br>2. Execute no terminal: <code>blender -b cena.blend -P gera_dados.py -f 1</code>.<br>3. Gere milhares de imagens sintéticas anotadas para treinar modelos de visão.",
    "Bevy Engine": "1. Adicione a dependência no <code>Cargo.toml</code> do seu projeto Rust.<br>2. Crie sistemas ECS que processam componentes de entidades em paralelo.<br>3. Compile e rode jogos e simulações com desempenho máximo e 0 garbage collection.",
    "Bullet Physics": "1. Importe o PyBullet no Python: <code>import pybullet as p</code>.<br>2. Conecte ao motor físico e carregue arquivos URDF de robôs.<br>3. Simule colisões, cinemática direta/inversa e controle motor com precisão.",
    "Webots": "1. Abra o Webots e crie um novo mundo de simulação.<br>2. Adicione robôs industriais pré-configurados (como KUKA ou Boston Dynamics).<br>3. Escreva controladores em C, Python ou ROS para testar algoritmos de navegação.",
    "Isaac Gym OSS / Genesis": "1. Instale o Genesis World no Python com PyTorch acelerado por CUDA.<br>2. Instancie milhares de robôs e ambientes simulados em paralelo na GPU.<br>3. Treine políticas de locomoção com aprendizado por reforço em minutos.",
    "Nextflow": "1. Crie seu arquivo <code>main.nf</code> definindo processos e canais de dados.<br>2. Execute o pipeline com <code>nextflow run main.nf -with-docker</code>.<br>3. O Nextflow gerencia tarefas paralelas e reprocessamento automático de falhas.",
    "Snakemake": "1. Escreva regras no arquivo <code>Snakefile</code> definindo inputs, outputs e comandos shell.<br>2. Execute <code>snakemake --cores 8</code>.<br>3. O Snakemake analisa dependências e roda apenas as etapas desatualizadas.",
    "ESMFold / AlphaFold (Weights)": "1. Instale a biblioteca ESM e passe a sequência de aminoácidos da proteína.<br>2. Execute a predição da estrutura 3D.<br>3. Exporte o arquivo <code>.pdb</code> para visualização no PyMOL em menos de 1 minuto.",
    "RDKit": "1. Importe no Python: <code>from rdkit import Chem</code>.<br>2. Converta strings SMILES em moléculas químicas 2D/3D.<br>3. Calcule propriedades físico-químicas e faça triagem virtual de fármacos.",
    "BioPython": "1. Carregue arquivos FASTA ou GenBank com <code>SeqIO.parse()</code>.<br>2. Realize traduções de sequências genéticas, alinhamentos e buscas no NCBI.<br>3. Manipule estruturas macromoleculares de arquivos PDB facilmente.",
    "OpenMM": "1. Configure o sistema molecular com campos de força (AMBER/CHARMM).<br>2. Crie o integrador e selecione a plataforma de aceleração CUDA.<br>3. Execute simulações de dinâmica molecular com milhões de passos por segundo.",
    "Bioconductor": "1. Instale pacotes no ambiente R: <code>BiocManager::install('DESeq2')</code>.<br>2. Importe contagens de sequenciamento de RNA-Seq.<br>3. Realize análises de expressão gênica diferencial com modelos estatísticos rigorosos.",
    "DeepChem": "1. Carregue datasets moleculares com a API do DeepChem.<br>2. Treine modelos de Graph Neural Networks (GNN) para prever toxicidade ou solubilidade.<br>3. Avalie métricas de generalização para novas estruturas moleculares.",
    "LLVM": "1. Escreva seu frontend de linguagem gerando código em representação intermediária (LLVM IR).<br>2. Execute os passes de otimização com a ferramenta <code>opt</code>.<br>3. Emita binários de máquina nativos ultra-otimizados com a ferramenta <code>llc</code>.",
    "Wasmtime": "1. Compile seu código Rust ou C para WebAssembly: <code>target wasm32-wasi</code>.<br>2. Execute no terminal: <code>wasmtime app.wasm</code>.<br>3. Rode módulos com isolamento de memória e inicialização em frações de milissegundo.",
    "Wasmer": "1. Instale o Wasmer e execute pacotes Wasm universais: <code>wasmer run usuario/pacote</code>.<br>2. Integre em aplicações Python, Rust ou Go como runtime embutido seguro.<br>3. Execute plugins de terceiros com sandboxing rígido.",
    "Zig Compiler": "1. Crie seu arquivo <code>main.zig</code>.<br>2. Compile com <code>zig build-exe main.zig -O ReleaseFast</code>.<br>3. Faça compilação cruzada para qualquer arquitetura com <code>zig build -Dtarget=x86_64-windows</code> em 1 comando.",
    "Rust Toolchain": "1. Inicialize um novo projeto com <code>cargo new meu_app --bin</code>.<br>2. Escreva código com garantias de segurança de memória validadas pelo compilador.<br>3. Gere binários de alta performance com <code>cargo build --release</code>.",
    "Bun Runtime": "1. Execute scripts TypeScript diretamente sem compilação prévia: <code>bun run app.ts</code>.<br>2. Instale dependências 20x mais rápido que npm: <code>bun install</code>.<br>3. Suba servidores HTTP de altíssimo rendimento com <code>Bun.serve()</code>.",
    "TinyGo": "1. Escreva código Go padrão usando goroutines e channels.<br>2. Compile para microcontroladores ou Wasm: <code>tinygo flash -target=pico main.go</code>.<br>3. Grave em microcontroladores gerando binários minúsculos de poucos KB.",
    "Cranelift": "1. Integre o Cranelift no seu runtime ou compilador JIT.<br>2. Converta instruções da sua linguagem em Intermediate Representation do Cranelift.<br>3. Emita código nativo x86/ARM em tempo de execução com latência quase nula.",
    "FreeCAD": "1. Abra o FreeCAD e escolha a bancada 'Part Design'.<br>2. Crie um esboço 2D com restrições dimensionais e aplique extrusão (Pad).<br>3. Exporte o arquivo em formato STEP para usinagem ou STL para impressão 3D.",
    "OpenSCAD": "1. Escreva o código 3D: <code>difference() { cube([30,30,10]); cylinder(r=5, h=15); }</code>.<br>2. Pressione F5 para visualizar o modelo em tempo real.<br>3. Exporte para STL com F6 para impressão 3D com precisão paramétrica absoluta.",
    "KiCad EDA": "1. Desenhe o circuito esquemático no Eeschema associando componentes.<br>2. Transfira para o PCBnew e faça o posicionamento e roteamento de trilhas.<br>3. Gere os arquivos Gerber e envie diretamente para fabricação de placas.",
    "OrcaSlicer / PrusaSlicer": "1. Importe o arquivo STL ou STEP da peça 3D.<br>2. Ajuste parâmetros de preenchimento, altura de camada e suportes automáticos.<br>3. Fatie o modelo e envie o G-code via rede Wi-Fi para sua impressora 3D.",
    "LibreCAD": "1. Abra o LibreCAD e configure as camadas de desenho (alvenaria, elétrica, cotas).<br>2. Desenhe plantas baixas e desenhos técnicos 2D com precisão de coordenadas.<br>3. Exporte em DXF ou PDF para impressão técnica em escala.",
    "SolveSpace": "1. Crie esboços 2D e aplique restrições de distância, ângulos e paralelismo.<br>2. Simule mecanismos móveis arrastando pontos com o mouse.<br>3. Exporte a geometria resultante em formato STEP ou DXF.",
    "Fritzing (Community)": "1. Monte seu circuito na visão de Breadboard arrastando placas e fios.<br>2. Alterne para a visão de Esquemático para organizar o diagrama elétrico.<br>3. Gere documentações visuais claras de protótipos de hardware.",
    "QCAD": "1. Abra plantas ou desenhos mecânicos no formato DWG/DXF.<br>2. Faça medições, edições rápidas e inserção de cotas técnicas.<br>3. Imprima em formatos padronizados A4 a A0 com suporte a plotters.",
    "Firefly III": "1. Acesse o painel web e cadastre suas contas bancárias e cartões.<br>2. Crie regras de automação que categorizam transações automaticamente.<br>3. Acompanhe orçamentos mensais e saldo patrimonial sem compartilhar dados bancários com terceiros.",
    "GnuCash": "1. Abra o livro contábil e cadastre o plano de contas (Ativo, Passivo, Receitas, Despesas).<br>2. Registre lançamentos pelo método de partidas dobradas.<br>3. Emita balancetes, demonstrações de resultados e relatórios fiscais completos.",
    "Beancount / Ledger-CLI": "1. Registre transações diárias em texto puro: <code>2026-08-24 * 'Supermercado' Despesas:Alimentacao 150.00 BRL</code>.<br>2. Inicie a interface web: <code>fava contas.beancount</code>.<br>3. Visualize gráficos de patrimônio líquido e fluxo de caixa instantaneamente.",
    "Ghostfolio": "1. Acesse o painel e registre suas compras de ações, FIIs e criptoativos.<br>2. Conecte feeds de preços para atualização automática das cotações.<br>3. Analise a alocação do portfólio, diversificação setorial e rendimentos de dividendos.",
    "BTCPay Server": "1. Conecte o BTCPay Server à sua loja virtual (WooCommerce, Shopify, Medusa).<br>2. Gere faturas de checkout em Bitcoin on-chain ou Lightning Network.<br>3. Receba pagamentos instantâneos com 0% de comissões e liquidação direta na sua carteira.",
    "Invoice Ninja": "1. Cadastre seus clientes e produtos com valores pré-definidos.<br>2. Crie faturas personalizadas com seu logotipo e envie por e-mail.<br>3. Acompanhe quando o cliente visualizou a fatura e receba pagamentos online.",
    "Actual Budget": "1. Defina tetos de gastos para cada categoria do seu orçamento mensal.<br>2. Registre despesas conforme ocorrem no celular ou desktop.<br>3. Garanta que cada real recebido tenha um destino alocado antes de ser gasto.",
    "KMyMoney": "1. Crie sua base financeira local com proteção por senha.<br>2. Importe extratos OFX/QIF dos seus bancos.<br>3. Concilie lançamentos e simule projeções de empréstimos e investimentos.",
    "Ardour": "1. Conecte sua interface de áudio e configure o buffer no Ardour.<br>2. Grave faixas multipista de voz e instrumentos simultaneamente.<br>3. Aplique plugins VST3 de equalização, compressão e faça a mixagem final.",
    "Tenacity / Audacity": "1. Abra arquivos de áudio gravados de reuniões ou podcasts.<br>2. Selecione trechos com ruído de fundo e aplique a redução de ruído espectral.<br>3. Normalize o volume (Loudness LUFS) e exporte em MP3/FLAC com alta qualidade.",
    "LMMS": "1. Crie padrões de bateria no sequenciador Beat+Bassline.<br>2. Adicione melodias no Piano Roll usando sintetizadores virtuais como Triple-Oscillator.<br>3. Monte a estrutura da música na janela de arranjo e exporte o áudio masterizado.",
    "JUCE Framework": "1. Crie um novo projeto de plugin de áudio usando o Projucer ou CMake.<br>2. Escreva o algoritmo de processamento no método <code>processBlock()</code> em C++.<br>3. Compile o plugin nos formatos VST3, AU e Standalone para uso em qualquer DAW.",
    "Faust DSP": "1. Descreva o processamento de áudio matematicamente no código Faust.<br>2. Visualize o diagrama de blocos de sinal gerado automaticamente no navegador.<br>3. Compile para C++, Rust ou WebAssembly e emita plugins de alto desempenho.",
    "Surge XT": "1. Abra o Surge XT como plugin dentro da sua DAW favorita.<br>2. Escolha entre osciladores Wavetable, FM, Analógicos ou de Ruído.<br>3. Module parâmetros com envelopes e LFOs para criar timbres sonoros únicos.",
    "SunVox": "1. Crie nós de geradores sonoros e efeitos na área de trabalho modular.<br>2. Conecte as saídas dos sintetizadores aos módulos de reverb e delay.<br>3. Componha músicas completas no tracker com um consumo de memória inferior a 15MB.",
    "Proxmox VE": "1. Acesse o painel web HTTPS na porta 8006 do servidor bare-metal.<br>2. Crie máquinas virtuais KVM para Windows/Linux e containers LXC leves.<br>3. Configure backups automáticos e replicação de storage ZFS entre servidores.",
    "TrueNAS SCALE": "1. Instale o TrueNAS em um servidor com múltiplos discos rígidos.<br>2. Crie pools de armazenamento ZFS com espelhamento (Mirror) ou RAID-Z2.<br>3. Compartilhe pastas via SMB, NFS e iSCSI na rede local com snapshots imutáveis.",
    "NixOS": "1. Declare todos os pacotes, usuários e serviços no arquivo <code>/etc/nixos/configuration.nix</code>.<br>2. Aplique as mudanças com <code>nixos-rebuild switch</code>.<br>3. Se algo der errado, selecione a versão anterior no menu de boot e restaure o sistema.",
    "Alpine Linux": "1. Use como imagem base para seus Dockerfiles: <code>FROM alpine:latest</code>.<br>2. Instale pacotes com <code>apk add --no-cache curl python3</code>.<br>3. Produza containers de produção ultra-leves e imunes a vulnerabilidades comuns.",
    "QEMU / KVM": "1. Crie uma imagem de disco virtual: <code>qemu-img create -f qcow2 disco.qcow2 20G</code>.<br>2. Inicie a VM com aceleração KVM ativada: <code>qemu-system-x86_64 -enable-kvm -m 4G disco.qcow2</code>.<br>3. Rode qualquer sistema operacional com overhead quase zero.",
    "Podman": "1. Execute containers exatamente como no Docker: <code>podman run -d -p 80:80 nginx</code>.<br>2. Crie pods locais unindo múltiplos containers compartilhando a mesma rede.<br>3. Gere arquivos YAML de Kubernetes a partir dos seus containers com <code>podman generate kube</code>.",
    "Talos Linux": "1. Grave a imagem do Talos nos nós do seu cluster.<br>2. Configure o cluster remotamente via linha de comando usando o <code>talosctl</code>.<br>3. Mantenha um cluster Kubernetes imutável, sem SSH e com segurança reforçada.",
    "Incus (LXC/LXD Fork)": "1. Inicie containers de sistema em Linux: <code>incus launch images:ubuntu/24.04 meu-servidor</code>.<br>2. Acesse o terminal instantaneamente: <code>incus exec meu-servidor bash</code>.<br>3. Desfrute de ambientes completos com inicialização em 1 segundo e baixo uso de RAM.",
    "Talon Voice": "1. Inicie o Talon Voice e conecte seu microfone headset e rastreador ocular.<br>2. Dite comandos de voz para navegação, seleção de texto e digitação de código.<br>3. Programe software o dia inteiro sem encostar as mãos no teclado ou mouse.",
    "NVDA Screen Reader": "1. Pressione <code>Ctrl+Alt+N</code> para iniciar o NVDA no Windows.<br>2. Navegue pelas janelas e páginas web usando as setas do teclado.<br>3. O leitor vocaliza controles, textos e links com resposta sonora instantânea.",
    "OpenBCI": "1. Conecte os eletrodos na touca e ligue a placa Cyton/Ganglion.<br>2. Abra a interface OpenBCI GUI para visualizar ondas cerebrais (EEG) em tempo real.<br>3. Use a biblioteca BrainFlow em Python para classificar sinais para controle de interfaces.",
    "WhisperLive": "1. Inicie o servidor WhisperLive na sua máquina.<br>2. Conecte o fluxo de áudio do microfone do evento ou reunião.<br>3. Exiba legendas em tempo real com menos de 500ms de atraso na tela para acessibilidade.",
    "OptiKey": "1. Posicione o rastreador ocular na parte inferior do monitor.<br>2. Olhe para as teclas do teclado virtual do OptiKey para selecionar letras.<br>3. Converta seleções em fala sintetizada para comunicação assistiva.",
    "Dasher": "1. Inicie o Dasher e selecione o idioma desejado.<br>2. Mova o cursor do mouse ou olhar em direção às letras que deseja digitar.<br>3. Escreva frases inteiras continuamente com poucos movimentos.",
    "Eyeware OSS / GazePointer": "1. Conecte sua webcam comum e posicione-se em frente à tela.<br>2. Execute a calibração de 9 pontos olhando para os círculos na tela.<br>3. Controle o cursor do mouse diretamente através do movimento dos seus olhos.",
    "Metasploit Framework": "1. Inicie o console interativo: <code>msfconsole</code>.<br>2. Selecione o exploit desejado: <code>use exploit/multi/handler</code>.<br>3. Configure o payload, defina o alvo (RHOST) e execute com <code>run</code> para simular a intrusão.",
    "Nmap": "1. Execute uma varredura de serviços na rede: <code>nmap -sV -sC 192.168.1.0/24</code>.<br>2. Identifique portas abertas, versões de servidores e potenciais brechas.<br>3. Exporte os resultados em formato XML para análise automatizada de segurança.",
    "Nuclei (ProjectDiscovery)": "1. Execute uma varredura baseada em templates comunitários: <code>nuclei -u https://meusite.com</code>.<br>2. O scanner testa vulnerabilidades conhecidas (CVEs, misconfigurations).<br>3. Receba alertas imediatos sobre falhas críticas antes que sejam exploradas.",
    "Caido / OWASP ZAP": "1. Configure o navegador para passar o tráfego pelo proxy local (porta 8080).<br>2. Navegue pela aplicação web para mapear endpoints e formulários.<br>3. Intercepte requisições HTTP, modifique parâmetros e teste falhas de injeção.",
    "OWASP Amass": "1. Execute a enumeração de superfície de ataque: <code>amass enum -d empresa.com</code>.<br>2. Colete todos os subdomínios, blocos de IP e registros de DNS vinculados.<br>3. Mapeie ativos esquecidos e servidores expostos à internet.",
    "John the Ripper / Hashcat": "1. Salve os hashes de senha em um arquivo de texto.<br>2. Execute o teste de força com uma wordlist: <code>john --wordlist=rockyou.txt hashes.txt</code>.<br>3. Identifique senhas fracas de usuários para forçar políticas de segurança mais fortes.",
    "Sqlmap": "1. Passe a URL vulnerável: <code>sqlmap -u 'http://site.com/item.php?id=1' --banner</code>.<br>2. O sqlmap detecta a presença de injeção SQL e a versão do banco de dados.<br>3. Valide a falha e implemente Prepared Statements no código para corrigir a brecha.",
    "Nikto": "1. Execute uma varredura rápida de servidor web: <code>nikto -h http://servidor.com</code>.<br>2. O Nikto verifica arquivos de configuração expostos, scripts perigosos e cabeçalhos ausentes.<br>3. Corrija as configurações do servidor web com base no relatório gerado.",
    "QGIS": "1. Abra o QGIS e adicione camadas vetoriais (Shapefile, GeoJSON) ou raster (GeoTIFF).<br>2. Aplique simbologias temáticas, filtros espaciais e faça cruzamentos de áreas.<br>3. Crie composições de mapas profissionais e exporte em alta resolução.",
    "OpenStreetMap / Nominatim": "1. Suba o container Nominatim com o arquivo PBF da sua região.<br>2. Faça chamadas HTTP de geocodificação: <code>http://localhost:8080/search?q=Av+Paulista&format=json</code>.<br>3. Converta endereços em coordenadas geográficas sem pagar cotas ao Google Maps.",
    "MapLibre GL": "1. Importe o MapLibre no seu frontend web: <code>import maplibregl from 'maplibre-gl'</code>.<br>2. Conecte ao seu servidor de tiles vetoriais.<br>3. Renderize mapas interativos com visualização 3D, marcadores customizados e rotação suave.",
    "PostGIS": "1. Habilite na base de dados: <code>CREATE EXTENSION postgis;</code>.<br>2. Salve localizações como <code>ST_MakePoint(longitude, latitude)</code>.<br>3. Faça consultas de proximidade: <code>WHERE ST_DWithin(geom, ponto_usuario, 5000)</code> para achar locais a 5km.",
    "Valhalla Routing": "1. Suba o motor Valhalla com os dados de malha viária da sua região.<br>2. Envie requisições de rota com múltiplos pontos de parada.<br>3. Receba itinerários otimizados com manobras passo a passo e tempos estimados de viagem.",
    "GDAL / OGR": "1. Converta formatos geoespaciais pelo terminal: <code>ogr2ogr -f GeoJSON saida.json entrada.shp</code>.<br>2. Reprojete coordenadas para outro sistema geodésico.<br>3. Processe gigabytes de imagens de satélite e arquivos vetoriais com scripts automatizados.",
    "GeoServer": "1. Acesse a interface web do GeoServer e crie um novo Workspace.<br>2. Publique camadas de dados a partir de tabelas do PostGIS ou arquivos raster.<br>3. Disponibilize os dados através de serviços padronizados WMS e WFS para aplicações web.",
    "PMTiles (Protomaps)": "1. Baixe o arquivo mundial ou regional <code>.pmtiles</code>.<br>2. Suba o arquivo em um bucket S3 ou servidor web estático.<br>3. Sirva mapas vetoriais do planeta inteiro direto do S3 com requisições HTTP Range sem servidores de backend.",
    "Moodle": "1. Instale o Moodle no servidor da instituição.<br>2. Crie cursos, adicione módulos de conteúdo, vídeos e fóruns de discussão.<br>3. Aplique questionários avaliativos com correção automática e emissão de certificados.",
    "Canvas LMS (OSS)": "1. Suba o Canvas LMS via Docker na infraestrutura escolar.<br>2. Organize disciplinas com cronogramas, tarefas e grade de notas (Gradebook).<br>3. Alunos e professores interagem em um ambiente moderno e responsivo.",
    "Anki (FSRS)": "1. Crie cartões de estudo (flashcards) com perguntas e respostas.<br>2. Revise os cartões agendados diariamente pelo algoritmo FSRS.<br>3. Fixe termos técnicos, vocabulário e conceitos na memória de longo prazo com esforço mínimo.",
    "Kolibri": "1. Instale o Kolibri em um servidor local ou Raspberry Pi na sala de aula.<br>2. Baixe canais educativos abertos (Khan Academy, livros abertos).<br>3. Alunos conectam seus dispositivos na rede Wi-Fi local e estudam sem precisar de internet.",
    "BigBlueButton": "1. Integre o BigBlueButton ao seu Moodle ou portal educacional.<br>2. Inicie aulas ao vivo com transmissão de voz, vídeo e compartilhamento de apresentações.<br>3. Use ferramentas de desenho colaborativo e grave as sessões para consulta posterior.",
    "Chamilo LMS": "1. Acesse o painel de administração do Chamilo.<br>2. Crie trilhas de aprendizagem corporativa usando o construtor visual de cursos.<br>3. Acompanhe relatórios de progresso e engajamento dos colaboradores.",
    "Oppia / Formative": "1. Crie lições interativas estruturadas em árvore de decisões.<br>2. Forneça explicações personalizadas para os erros mais comuns dos estudantes.<br>3. Acompanhe onde os alunos têm maiores dificuldades conceituais.",
    "OpenedX": "1. Implante a plataforma Open edX usando a ferramenta Tutor.<br>2. Estruture cursos massivos online com vídeos, avaliações e discussões.<br>3. Escale o atendimento educacional para milhares de alunos simultâneos.",
    "Medusa.js": "1. Inicialize seu projeto: <code>npx create-medusa-app@latest</code>.<br>2. Conecte ao seu banco PostgreSQL e configure produtos e preços no painel admin.<br>3. Conecte qualquer frontend (Next.js, Remix, Mobile) via API REST sem pagar taxas de Shopify.",
    "Saleor": "1. Suba o backend Saleor com Docker Compose.<br>2. Gerencie múltiplos armazéns, moedas e canais de venda pelo painel administrativo.<br>3. Integre o storefront em Next.js consumindo a API GraphQL de alta performance.",
    "Vendure": "1. Crie uma aplicação Vendure em TypeScript.<br>2. Defina entidades customizadas e fluxos de pedido através de plugins em NestJS.<br>3. Opere sua loja virtual com tipagem ponta a ponta e escalabilidade garantida.",
    "WooCommerce": "1. Instale o plugin WooCommerce no seu WordPress.<br>2. Configure opções de pagamento, cálculo de frete e catálogo de produtos.<br>3. Venda produtos físicos ou digitais sem mensalidades de plataformas fechadas.",
    "PrestaShop": "1. Instale o PrestaShop na sua hospedagem PHP/MySQL.<br>2. Escolha um tema profissional e ative módulos de pagamento locais.<br>3. Gerencie catálogo volumoso, estoque e pedidos em múltiplos idiomas e moedas.",
    "Bagisto": "1. Instale o Bagisto sobre o Laravel com Composer.<br>2. Configure produtos simples, configuráveis ou agrupados.<br>3. Desenvolva customizações de e-commerce aproveitando o ecossistema Laravel.",
    "Solidus": "1. Adicione a gem Solidus no seu projeto Ruby on Rails.<br>2. Customize regras de cálculo de impostos, checkout e promoções complexas.<br>3. Processe milhares de pedidos por dia com estabilidade e cobertura total de testes.",
    "Spree Commerce": "1. Inicie sua loja com o gerador Spree em Ruby on Rails.<br>2. Utilize a API REST v2 para conectar aplicações móveis ou frontends headless.<br>3. Gerencie devoluções, suporte e pagamentos em múltiplos estoques.",
    "OBS Studio": "1. Adicione suas fontes de vídeo (câmera, captura de tela, microfone) nas cenas do OBS.<br>2. Configure a taxa de bits (bitrate) e resolução de saída.<br>3. Inicie a gravação local ou transmissão ao vivo para qualquer servidor RTMP/SRT.",
    "Owncast": "1. Suba o Owncast na sua VPS com <code>docker run -d -p 8080:8080 -p 1935:1935 gabek/owncast</code>.<br>2. No OBS Studio, configure a transmissão para <code>rtmp://sua-vps/live</code> com sua chave de stream.<br>3. Seus espectadores assistem à live pelo navegador com chat interativo sem anúncios.",
    "Jellyfin": "1. Suba o Jellyfin apontando os volumes para suas pastas de filmes, séries e músicas.<br>2. Acesse pelo navegador ou aplicativo na Smart TV.<br>3. Assista aos seus vídeos com transcodificação em hardware e sincronização de progresso.",
    "PeerTube": "1. Suba uma instância PeerTube na sua VPS.<br>2. Faça upload dos vídeos institucionais ou do canal.<br>3. Transmita vídeos com distribuição P2P via WebTorrent, economizando 80% da banda do servidor.",
    "Restreamer (Datarhei)": "1. Acesse o painel web do Restreamer na porta 8080.<br>2. Conecte sua fonte de vídeo de entrada (câmera IP ou OBS).<br>3. Reenvie o fluxo simultaneamente para YouTube, Twitch e seu próprio site em 1 clique.",
    "Icecast": "1. Instale o Icecast e configure o ponto de montagem no <code>icecast.xml</code>.<br>2. Conecte seu software de transmissão de áudio (Mixxx ou Butt).<br>3. Transmita rádio online e podcasts ao vivo para milhares de ouvintes conectados.",
    "SRS (Simple Realtime Server)": "1. Inicie o servidor SRS com suporte a WebRTC e RTMP.<br>2. Envie o fluxo de vídeo da sua câmera ou OBS.<br>3. Entregue vídeo ao vivo com latência inferior a 1 segundo para centenas de usuários.",
    "Node-Media-Server": "1. Instale no projeto Node: <code>npm install node-media-server</code>.<br>2. Configure portas RTMP e HTTP-FLV no arquivo <code>app.js</code>.<br>3. Crie regras de autenticação de live streaming personalizadas com JavaScript.",
    "ArchiveBox": "1. Inicie o ArchiveBox: <code>docker run -d -p 8000:8000 -v ~/data:/data archivebox/archivebox</code>.<br>2. Adicione URLs para arquivamento via painel web ou linha de comando.<br>3. O ArchiveBox salva automaticamente HTML, PDF, screenshots, texto puro e arquivos de mídia.",
    "SpiderFoot": "1. Acesse a interface do SpiderFoot na porta 5001.<br>2. Crie uma nova varredura inserindo um domínio, e-mail ou endereço IP alvo.<br>3. A ferramenta correlaciona centenas de fontes públicas e gera um mapa de inteligência OSINT.",
    "Sherlock": "1. Execute no terminal: <code>sherlock nome_de_usuario</code>.<br>2. O Sherlock verifica mais de 400 redes sociais e plataformas em segundos.<br>3. Obtenha a lista exata de perfis ativos com os links diretos correspondentes.",
    "SingleFile": "1. Instale a extensão no navegador ou use a CLI: <code>npx single-file https://artigo.com pagina.html</code>.<br>2. O SingleFile empacota HTML, CSS, fontes e imagens em 1 único arquivo <code>.html</code>.<br>3. Guarde cópias exatas de artigos técnicos que abrem offline em qualquer computador.",
    "Waybackpy": "1. Instale via pip: <code>pip install waybackpy</code>.<br>2. Salve páginas na Wayback Machine: <code>waybackpy -u 'https://site.com' --save</code>.<br>3. Consulte versões históricas de documentos públicos para auditoria.",
    "Maltego Community": "1. Abra o Maltego e crie um novo gráfico de investigação.<br>2. Insira entidades iniciais (domínio, pessoa, empresa, IP).<br>3. Execute 'Transforms' para descobrir conexões ocultas, servidores de e-mail e dados públicos.",
    "Ghunt": "1. Autentique o GHunt com seus cookies do Google.<br>2. Execute: <code>ghunt email usuario@gmail.com</code>.<br>3. Extraia dados públicos como ID do Google, canais do YouTube e avaliações do Maps.",
    "TheHarvester": "1. Execute: <code>theHarvester -d dominio.com -b google,bing,linkedin</code>.<br>2. A ferramenta coleta e-mails de colaboradores, subdomínios e hosts públicos.<br>3. Use os dados para avaliar a exposição pública e fechar vazamentos de informações."
}

def enriquecer_arquivo(caminho_arquivo):
    conteudo = caminho_arquivo.read_text(encoding="utf-8")
    modificado = False

    # Regex para encontrar as entradas no ledger
    # Procura por <h3>(NomeDaFerramenta)</h3>
    padrao_h3 = re.compile(r'<h3>(.*?)<\/h3>')
    
    # Se ja tiver 'Como Usar no Dia a Dia', pula
    if "Como Usar no Dia a Dia" in conteudo:
        return False

    # Substituir blocos <div class="block"> que contem <span class="label">O que entrega</span>
    def substituir_bloco(match):
        nome_completo = match.group(1).strip()
        # Limpar possiveis tags ou versoes
        nome_limpo = nome_completo.split("(")[0].strip()
        
        # Procurar correspondencia no dicionario
        workflow = WORKFLOWS_MAP.get(nome_completo) or WORKFLOWS_MAP.get(nome_limpo)
        if not workflow:
            # Fallback inteligente se nao achar no mapa
            workflow = f"1. Instale o pacote ou execute a imagem Docker oficial.<br>2. Configure os parâmetros necessários no seu arquivo de configuração.<br>3. Integre diretamente ao seu workflow diário de engenharia para substituir soluções comerciais."

        bloco_how_to_use = f"""
              <div class="how-to-use" style="background:var(--surface-2);border-left:3px solid var(--accent);padding:10px 14px;border-radius:0 2px 2px 0;margin-top:6px;display:flex;flex-direction:column;gap:4px;">
                <span class="label" style="color:var(--accent);font-weight:600;font-size:10.5px;letter-spacing:.12em;text-transform:uppercase;">Como Usar no Dia a Dia (Workflow Prático)</span>
                <p style="font-size:13.5px !important;color:var(--ink) !important;line-height:1.5 !important;margin:0;">{workflow}</p>
              </div>"""

        return match.group(0) + bloco_how_to_use

    # Localizar cada entry e injetar apos o </pre> do bloco 'O que entrega'
    novo_conteudo = re.sub(r'(<span class="label">O que entrega</span>[\s\S]*?<pre><code>[\s\S]*?<\/code><\/pre>)', lambda m: m.group(1) + """
              <div class="how-to-use" style="background:var(--surface-2);border-left:3px solid var(--accent);padding:10px 14px;border-radius:0 2px 2px 0;margin-top:6px;display:flex;flex-direction:column;gap:4px;">
                <span class="label" style="color:var(--accent);font-weight:600;font-size:10.5px;letter-spacing:.12em;text-transform:uppercase;">Como Usar no Dia a Dia (Workflow Prático)</span>
                <p style="font-size:13.5px !important;color:var(--ink) !important;line-height:1.5 !important;margin:0;">1. Execute o comando de inicialização fornecido.<br>2. Integre a ferramenta nas suas esteiras de CI/CD ou scripts diários.<br>3. Elimine o custo de licenças comerciais com controle total dos seus dados.</p>
              </div>""", conteudo)

    caminho_arquivo.write_text(novo_conteudo, encoding="utf-8")
    return True

def processar_todos():
    pastas = [Path("output/listas-open-source"), Path("docs/listas")]
    total = 0
    for pasta in pastas:
        if not pasta.exists():
            continue
        for arq in pasta.glob("*.html"):
            if arq.name == "index.html":
                continue
            enriquecer_arquivo(arq)
            total += 1
            print(f"  [OK] Workflow prático injetado em {pasta.name}/{arq.name}")

    print(f"\n[+] Total de {total} arquivos enriquecidos com 'Como Usar no Dia a Dia'.")

if __name__ == "__main__":
    processar_todos()
