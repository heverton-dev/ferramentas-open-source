# -*- coding: utf-8 -*-
"""
Gerador de Elite da Lista 02 expandida para 20 ferramentas e skills:
Arquitetura Agêntica, Spec-Driven Development, Skills de Design, Contratos Formais e Sandboxes.
"""

from pathlib import Path
from gerar_catalogo_completo_30 import gerar_html_completo

LISTA_02_EXPANDIDA = {
    "slug": "02-arquitetura-agentica-spec-driven",
    "title": "Arquitetura Agêntica, Spec-Driven Development & Skills de Engenharia",
    "camada": "Camada 02 · Orquestração de Agentes, Contratos & Skills",
    "accent": "#1A446C", "accent_dark": "#7AA5D6", "accent_soft": "#DCE7F2", "accent_soft_dark": "#162436",
    "deck": "Frameworks, sandboxes e <strong>20 skills agênticas de elite para orquestrar squads com contratos estritos, especificações formais (SDD), guardrails de design (Impeccable), fidelidade editorial (Hallmark) e navegação por grafos</strong>: elimine o código espaguete e garanta que o agente teste o próprio trabalho antes da entrega.",
    "pilar_1": "O Fim do Chatbot Monolítico",
    "pilar_1_desc": "Pedir tudo em um único prompt gera alucinação, código espaguete e perda de foco. A engenharia moderna decompõe o projeto em papéis especializados com permissões restritas e contratos formais.",
    "pilar_2": "Spec-Driven Development & Skills de Elite",
    "pilar_2_desc": "Requisitos viram SPEC.md e testes automatizados antes da primeira linha de código. Skills acopladas ao contexto aplicam guardrails de design, tipagem estrita e verificação de dependências em tempo real.",
    "itens": [
        {
            "rank": "01", "name": "Skill: spec-driven-contracts (Spec-Kit)", "cat": "Spec-Driven Dev Skill", "lic": "MIT / SDD Skill",
            "substitui": "Desenvolvimento desgovernado por IA", "econ": "Economiza semanas de retrabalho em código quebrado",
            "entrega": "Framework formal que bloqueia a escrita de código até que o contrato de especificação (SPEC -> PLAN -> TASKS) e os critérios de aceite estejam aprovados.",
            "mecanica": "Estrutura o ciclo agêntico em 3 fases rígidas: 1) SPEC.md (Entradas, saídas esperadas e contratos de API); 2) PLAN.md (Quebra arquitetural em tarefas atômicas); 3) TASKS.md (Execução passo a passo com testes).",
            "cmd": "# SPEC.md -> PLAN.md -> TASKS.md -> EXECUÇÃO",
            "como_usar": "1. Antes de pedir código à IA, crie <code>SPEC.md</code> definindo contratos e tipos.<br>2. Peça ao agente para emitir o <code>PLAN.md</code> detalhando cada módulo.<br>3. O agente implementa arquivo por arquivo, validando cada etapa contra os critérios de aceite.",
            "spec": "Contratos formais / 0 RAM",
            "truth": "Garante que a IA nunca comece a gerar arquivos sem saber exatamente o critério de aceite.",
            "repo": "github.com/github/spec-kit"
        },
        {
            "rank": "02", "name": "Skill: impeccable", "cat": "Design & UI Guardrail Skill", "lic": "MIT / Design Skill",
            "substitui": "Interfaces geradas por IA genéricas e feias", "econ": "Zero retrabalho de frontend e CSS",
            "entrega": "Impõe regras matemáticas de design system: alinhamento estrito, tokens CSS, contraste WCAG AAA, hierarquia tipográfica e scrollbars customizadas.",
            "mecanica": "Injeta guardrails de design na geração de código frontend: proíbe classes inline aleatórias, exige uso de variáveis CSS padronizadas, dark mode nativo e acabamento editorial refinado.",
            "cmd": "# Regra: 'Artefatos visuais seguem padrao editorial unico validado por gate de design'",
            "como_usar": "1. Ative a skill <code>impeccable</code> no seu agente de frontend.<br>2. Peça para gerar dashboards, landing pages ou componentes UI.<br>3. O agente emite código com acabamento profissional, proporção áurea, dark mode automático e scrollbar de 4px.",
            "spec": "0 MB RAM / Guardrail de prompt",
            "truth": "Elimina a aparência 'cara de template de IA' e gera interfaces prontas para produtos comerciais de alto nível.",
            "repo": "github.com/pbakaus/impeccable"
        },
        {
            "rank": "03", "name": "Skill: code-review-graph", "cat": "Graph Navigation Skill", "lic": "MIT / Codebase Graph",
            "substitui": "Exploração cega de arquivos pelo agente", "econ": "-75% de chamadas de exploração de código",
            "entrega": "Mapeia as dependências, classes, funções e chamadas do repositório em um grafo antes de permitir alterações.",
            "mecanica": "Lê o índice de símbolos gerado por AST e constrói a árvore de impacto: ao alterar a função A, consulta imediatamente quais módulos B, C e D serão afetados antes de escrever código.",
            "cmd": "# Regra: 'Consultar code-review-graph antes de tools de leitura/busca'",
            "como_usar": "1. O agente consulta o índice de grafo para saber onde a função é importada.<br>2. Identifica todos os pontos de quebra antes de editar o primeiro arquivo.<br>3. Aplica refatorações cirúrgicas com 0 erros de regressão.",
            "spec": "Grafo local em SQLite / < 20 MB",
            "truth": "Permite ao agente saber exatamente o efeito colateral de qualquer mudança sem precisar ler 50 arquivos.",
            "repo": "github.com/code-review-graph"
        },
        {
            "rank": "04", "name": "Skill: hallmark", "cat": "Brand & Editorial Fidelity", "lic": "MIT / Editorial Skill",
            "substitui": "Textos com tom de voz inconsistente", "econ": "100% de conformidade editorial",
            "entrega": "Audita e formata todo o conteúdo de saída de acordo com a voz de marca, rigor terminológico e regras de idioma estritas (PT-BR).",
            "mecanica": "Valida os artefatos contra uma tabela de termos proibidos (buzzwords vazias, exageros de marketing) e força o uso de precisão técnica e linguagem direta.",
            "cmd": "# Regra: 'Idioma único e estrito (PT-BR), sem preâmbulos, direto ao ponto'",
            "como_usar": "1. Ative a skill <code>hallmark</code> em agentes de documentação e relatórios.<br>2. Ao gerar artigos, relatórios técnicos ou documentações de API, o texto sai limpo, sem enrolação e com terminologia consistente.<br>3. Economize tempo de revisão humana de texto.",
            "spec": "0 MB RAM / Regra comportamental",
            "truth": "Documentação com ruído e palavras vazias reduz a autoridade técnica do projeto. O Hallmark garante tom impecável.",
            "repo": "github.com/topics/editorial-standards"
        },
        {
            "rank": "05", "name": "Skill: mira-animator", "cat": "Declarative Motion Skill", "lic": "MIT / Motion Skill",
            "substitui": "Animações pesadas em JavaScript", "econ": "60 FPS nativo e zero bibliotecas extras",
            "entrega": "Gera keyframes e transições em CSS puro e Canvas acelerado por hardware com curvas de bezier naturais.",
            "mecanica": "Aplica física de amortecimento (spring physics) e aceleração de GPU (<code>transform</code> e <code>opacity</code>) sem importar bibliotecas pesadas de 100KB como Framer Motion.",
            "cmd": "# Regra: 'Animações fluidas via CSS transforms/opacity nativos com will-change'",
            "como_usar": "1. Peça ao agente para criar microinterações para botões, modais e transições de página.<br>2. A skill gera CSS enxuto com aceleração por hardware.<br>3. Sua interface roda fluida a 120 FPS em celulares e desktops.",
            "spec": "CSS nativo / 0 overhead JS",
            "truth": "Animações feitas com CSS nativo e transforms não bloqueiam a thread principal do navegador.",
            "repo": "github.com/topics/css-animation"
        },
        {
            "rank": "06", "name": "Skill: test-first-tdd", "cat": "TDD Gatekeeper Skill", "lic": "MIT / TDD Skill",
            "substitui": "Código sem cobertura de testes", "econ": "Reduz 90% dos bugs em produção",
            "entrega": "Impede o agente de escrever a lógica de negócio antes de criar e executar o teste unitário correspondente que falha (Red-Green-Refactor).",
            "mecanica": "Injeta uma restrição no ciclo de execução: para toda nova feature ou bug fix, o agente deve gerar o arquivo de teste unitário primeiro (pytest, vitest, cargo test) e só pode prosseguir quando o teste falhar com a asserção correta.",
            "cmd": "# Regra: 'Teste primeiro (Red) -> Implementação (Green) -> Refatoração'",
            "como_usar": "1. Solicite uma funcionalidade (ex: validação de CPF).<br>2. O agente gera `tests/test_cpf.py` com 10 casos extremos.<br>3. Executa a suíte (falha esperada), implementa a função `validar_cpf()` e reexecuta até obter 100% de sucesso.",
            "spec": "0 MB RAM / Disciplina TDD",
            "truth": "Testes unitários escritos antes da implementação forçam a IA a pensar no contrato e nos casos de borda.",
            "repo": "github.com/topics/tdd-skills"
        },
        {
            "rank": "07", "name": "Skill: architect-gatekeeper", "cat": "Architecture Gatekeeper", "lic": "MIT / Architecture Skill",
            "substitui": "Acoplamento e quebra de SOLID por IA", "econ": "Zero débitos técnicos cumulativos",
            "entrega": "Avalia o impacto arquitetural de cada alteração: verifica acoplamento aferente/eferente, coesão modular e conformidade com Clean Architecture.",
            "mecanica": "Executa análise estática de imports e chamadas de classes. Se uma camada de domínio tentar importar diretamente um driver de banco de dados ou framework web, o gatekeeper bloqueia a alteração com `exit 1`.",
            "cmd": "# Regra: 'Camadas internas não conhecem camadas externas (Dependency Inversion)'",
            "como_usar": "1. O agente arquiteto valida os diagramas e contratos antes do commit.<br>2. Se uma dependência circular for detectada, o gatekeeper força a criação de uma interface desacoplada.<br>3. Garante que monorepos e microserviços permaneçam manuteníveis ao longo de meses.",
            "spec": "Análise estática de dependências",
            "truth": "Evita que agentes autônomos transformem bases limpas em monolitos espaguete com imports cruzados.",
            "repo": "github.com/topics/software-architecture"
        },
        {
            "rank": "08", "name": "Skill: doc-contract", "cat": "Contract Synchronization", "lic": "MIT / Contract Skill",
            "substitui": "Documentação e tipos dessincronizados", "econ": "Economiza horas de debugging de API",
            "entrega": "Gera e sincroniza schemas OpenAPI, JSON Schema e tipos TypeScript automaticamente a partir dos modelos Pydantic/Rust.",
            "mecanica": "Extrai a definição tipada das estruturas de dados e compila contratos formais nos formatos OpenAPI 3.1 e `.d.ts` sem intervenção humana, garantindo paridade total entre backend e frontend.",
            "cmd": "# Regra: 'Modelos de backend são a fonte única da verdade para contratos de frontend'",
            "como_usar": "1. Crie ou altere uma classe Pydantic no backend.<br>2. A skill dispara a geração dos tipos TypeScript correspondentes em `frontend/types/api.d.ts`.<br>3. Frontend e backend compartilham 100% de tipagem sem erros de payload.",
            "spec": "Scripts de compilação de tipos",
            "truth": "Elimina totalmente erros em tempo de execução causados por nomes de campos diferentes entre cliente e servidor.",
            "repo": "github.com/topics/openapi-contracts"
        },
        {
            "rank": "09", "name": "Aider CLI", "cat": "Git Pair Programmer", "lic": "Apache-2.0",
            "substitui": "Assinatura Cursor ($ 20/mês)", "econ": "-$ 240 / ano por desenvolvedor",
            "entrega": "Assistente de linha de comando que opera no repositório Git, resolve issues e gera commits semânticos com árvore AST.",
            "mecanica": "Constrói um mapa de repositório (repo map) compacto usando Tree-sitter, envia apenas as assinaturas relevantes no prompt e aplica diffs unificados diretamente nos arquivos com validação de linters e testes locais.",
            "cmd": "pip install aider-chat && aider --model ollama/qwen2.5-coder:7b",
            "como_usar": "1. No terminal do projeto, execute <code>aider src/main.py</code>.<br>2. Diga: 'Implemente autenticação JWT e adicione testes pytest'.<br>3. O Aider edita o código, roda os testes locais e faz o commit semântico no Git automaticamente.",
            "spec": "~60 MB RAM",
            "truth": "Líder mundial consistente no benchmark SWE-bench para resolução de problemas reais de engenharia de software.",
            "repo": "aider.chat"
        },
        {
            "rank": "10", "name": "OpenHands (OpenDevin)", "cat": "Autonomous Sandbox", "lic": "MIT",
            "substitui": "Devin / Magic.dev ($ 500+/mês)", "econ": "-$ 6.000 / ano em ferramentas fechadas",
            "entrega": "Plataforma de agentes autônomos executados em containers Docker isolados com capacidade de usar browser, terminal e editor.",
            "mecanica": "Executa um runtime seguro com loop de evento autônomo (Thought -> Action -> Observation). O agente possui acesso a uma VM Linux containerizada onde instala pacotes, roda servidores e depura erros no terminal.",
            "cmd": "docker run -it -p 3000:3000 ghcr.io/all-hands-ai/openhands:main",
            "como_usar": "1. Acesse <code>http://localhost:3000</code> e conecte seu repositório Git.<br>2. Atribua uma issue de bug ou refatoração complexa.<br>3. Acompanhe o agente instalando dependências, rodando testes e abrindo o Pull Request.",
            "spec": "Ambiente Docker isolado",
            "truth": "O agente instala pacotes e roda testes sem colocar em risco o sistema operacional do desenvolvedor.",
            "repo": "all-hands.dev"
        },
        {
            "rank": "11", "name": "Instructor", "cat": "Structured Outputs", "lic": "MIT",
            "substitui": "Tratamento manual de erros de JSON", "econ": "Economiza horas de debugging de parsing",
            "entrega": "Biblioteca Python/TS que envelopa chamadas de LLM com validação estrita de modelos Pydantic e retentativas automáticas.",
            "mecanica": "Envia o schema JSON via Function Calling/Tool Use e valida a resposta no Pydantic. Se ocorrer erro de validação de tipo, reenvia automaticamente apenas o erro de validação para o modelo com instrução de auto-correção.",
            "cmd": "pip install instructor",
            "como_usar": "1. Envolva seu cliente: <code>client = instructor.from_openai(OpenAI())</code>.<br>2. Defina o schema: <code>class Lead(BaseModel): nome: str, email: str</code>.<br>3. Chame a API com <code>response_model=Lead</code> e receba objetos Python tipados.",
            "spec": "Zero runtime overhead",
            "truth": "Se a saída não validar no Pydantic, o Instructor reenvia apenas o erro para a LLM corrigir o campo exato.",
            "repo": "python.useinstructor.com"
        },
        {
            "rank": "12", "name": "LangGraph", "cat": "Cyclic State Graph", "lic": "MIT",
            "substitui": "Scripts de agentes frágeis e lineares", "econ": "Zero travamentos por loops infinitos",
            "entrega": "Framework de orquestração multi-agente baseado em grafos com persistência de checkpoints e pontos de controle humano.",
            "mecanica": "Modela fluxos agênticos como Grafos Cíclicos Direcionados onde cada nó é uma função/LLM e as arestas contêm lógica condicional. Salva o snapshot de cada transição em SQLite para recuperação de estado e time-travel.",
            "cmd": "pip install langgraph",
            "como_usar": "1. Defina o estado global: <code>class Estado(TypedDict): mensagens: list</code>.<br>2. Crie nós de agentes especialistas e arestas condicionais.<br>3. Execute com persistência de checkpoints para pausar e retomar a execução a qualquer momento.",
            "spec": "~50 MB RAM",
            "truth": "Permite pausar a execução da esteira agêntica, pedir feedback ao usuário e retomar o estado com 100% de precisão.",
            "repo": "langchain-ai.github.io/langgraph"
        },
        {
            "rank": "13", "name": "CrewAI", "cat": "Role-Based Multi-Agent", "lic": "MIT",
            "substitui": "Prompts gigantes e confusos", "econ": "Reduz erros de contexto em 80%",
            "entrega": "Framework que organiza agentes em equipes com papéis claros (Role, Goal, Backstory) e delegação autônoma de tarefas.",
            "mecanica": "Implementa padrões de colaboração sequencial e hierárquica. Agentes gerentes delegam subtarefas para agentes especialistas equipados com ferramentas personalizadas e memória compartilhada.",
            "cmd": "pip install crewai crewai-tools",
            "como_usar": "1. Declare os agentes: Pesquisador, Redator e Revisor.<br>2. Crie tarefas com saídas esperadas bem definidas.<br>3. Dispare a Crew: os agentes conversam, executam ferramentas e compilam o resultado final colaborativamente.",
            "spec": "~65 MB RAM",
            "truth": "A estrutura baseada em papéis reduz drasticamente a alucinação ao manter cada agente focado em seu domínio.",
            "repo": "crewai.com"
        },
        {
            "rank": "14", "name": "Letta (MemGPT) / Mem0", "cat": "Long-Term Memory Engine", "lic": "Apache-2.0",
            "substitui": "Janela de contexto estourada", "econ": "-80% de reenvio de histórico antigo",
            "entrega": "Camada de memória de longo prazo auto-gerenciada que armazena fatos, preferências e histórico do usuário em banco relacional.",
            "mecanica": "Implementa uma arquitetura de hierarquia de memória inspirada em Sistemas Operacionais (Core Memory em RAM vs Archival Memory em disco/vetores). O agente chama funções internas para persistir dados estruturados.",
            "cmd": "pip install letta && letta run",
            "como_usar": "1. Conecte o SDK do Letta no backend do seu assistente ou agente.<br>2. Durante a conversa, quando o usuário definir uma regra de arquitetura, o Letta grava na memória permanente.<br>3. Semanas depois, o agente recupera os dados sem reexplicações.",
            "spec": "~90 MB RAM",
            "truth": "O agente não esquece decisões tomadas há 3 semanas sem precisar reenviar todo o histórico no prompt.",
            "repo": "letta.com"
        },
        {
            "rank": "15", "name": "E2B Code Interpreter", "cat": "Secure Code Sandbox", "lic": "Apache-2.0",
            "substitui": "Execuções inseguras no host", "econ": "100% de segurança contra scripts maliciosos",
            "entrega": "MicroVMs efêmeras que sobem em 100ms para que o agente execute código Python, gere gráficos e analise dados com segurança.",
            "mecanica": "Utiliza Firecracker MicroVMs em ambiente seguro. O agente envia código Python/JS arbitrário via WebSocket e recebe stdout, stderr e artefatos de imagem gerados em um ambiente 100% isolado do sistema hospedeiro.",
            "cmd": "npm install @e2b/code-interpreter",
            "como_usar": "1. Crie a sandbox: <code>const sandbox = await Sandbox.create();</code>.<br>2. Execute o script da LLM: <code>const exec = await sandbox.runCode('import pandas as pd; ...');</code>.<br>3. Baixe os artefatos gerados sem risco de invasão do servidor.",
            "spec": "MicroVM sob demanda (< 100ms)",
            "truth": "Ambiente isolado ideal para agentes que geram e executam código de visualização em tempo real.",
            "repo": "e2b.dev"
        },
        {
            "rank": "16", "name": "AutoGen (Microsoft)", "cat": "Conversational Multi-Agent", "lic": "MIT",
            "substitui": "Single-prompt engineering", "econ": "Auto-correção de bugs em tempo de execução",
            "entrega": "Framework da Microsoft para conversação multi-agente com suporte a agentes humanos e robôs executando código colaborativamente.",
            "mecanica": "Permite que agentes debatam entre si, proponham código, executem em ambiente local ou Docker e façam auto-correção de stack traces de erro até atingirem o critério de sucesso.",
            "cmd": "pip install autogen-agentchat",
            "como_usar": "1. Configure um `AssistantAgent` (programador) e um `UserProxyAgent` (executor de código).<br>2. Inicie a conversa com a tarefa desejada.<br>3. O programador gera o script, o executor roda no terminal e devolve o erro para o programador corrigir autonomamente.",
            "spec": "~70 MB RAM",
            "truth": "Excelente para tarefas de ciência de dados e automação de scripts que exigem ciclos rápidos de tentativa e erro.",
            "repo": "microsoft.github.io/autogen"
        },
        {
            "rank": "17", "name": "Dify (Agent Workflow)", "cat": "Visual Agent Workflow", "lic": "Apache-2.0",
            "substitui": "Flowise / Plataformas pagas de workflow", "econ": "-$ 2.400 / ano em ferramentas SaaS",
            "entrega": "Plataforma visual completa para criação de fluxos agênticos, pipelines de RAG, testes de prompt e publicação de APIs prontas.",
            "mecanica": "Combina orquestração visual baseada em nós com runtime em Python/Go. Suporta múltiplos provedores de LLM, bancos vetoriais e publicação direta de webhooks e interfaces de chat para usuários finais.",
            "cmd": "docker compose up -d (no repositório oficial do Dify)",
            "como_usar": "1. Suba o Dify via Docker Compose.<br>2. Crie um workflow arrastando blocos de LLM, código Python, busca vetorial e decisões condicionais.<br>3. Publique como API REST e consuma direto na sua aplicação.",
            "spec": "~650 MB RAM (Stack completa)",
            "truth": "A melhor interface open-source para permitir que desenvolvedores e gestores de produto construam agentes sem código espaguete.",
            "repo": "dify.ai"
        },
        {
            "rank": "18", "name": "PydanticAI", "cat": "Type-Safe Agent Framework", "lic": "MIT",
            "substitui": "Frameworks com tipagem fraca", "econ": "Zero erros de tipo em tempo de execução",
            "entrega": "O framework agêntico oficial criado pela equipe do Pydantic, trazendo tipagem estrita de ponta a ponta e injeção de dependências nativa.",
            "mecanica": "Constrói agentes utilizando decorators e genéricos Python (`Agent[Dependency, OutputType]`). Valida parâmetros de ferramentas e respostas finais diretamente nos modelos Pydantic com suporte nativo a streaming estruturado.",
            "cmd": "pip install pydantic-ai",
            "como_usar": "1. Instancie seu agente: <code>agent = Agent('openai:gpt-4o', result_type=RelatorioTecnico)</code>.<br>2. Registre ferramentas com tipagem estrita via <code>@agent.tool</code>.<br>3. Execute <code>result = await agent.run('Analise os logs')</code> e receba um objeto validado.",
            "spec": "Overhead de runtime zero",
            "truth": "Projetado para engenheiros de software que exigem suporte total de IDE, autocomplete e validação matemática de tipos.",
            "repo": "ai.pydantic.dev"
        },
        {
            "rank": "19", "name": "DSPy Assertions", "cat": "Self-Correcting Pipelines", "lic": "MIT",
            "substitui": "Retentativas manuais com try/except", "econ": "-60% de chamadas com erro semântico",
            "entrega": "Mecanismo que injeta asserções lógicas dentro de pipelines de LLM, disparando backtracking automático caso a saída viole restrições de negócio.",
            "mecanica": "Utiliza as primitivas `dspy.Assert` e `dspy.Suggest`. Se uma asserção falhar durante a execução, o compilador envia o feedback do erro diretamente para o módulo anterior no grafo e reexecuta com novos parâmetros.",
            "cmd": "pip install dspy-ai",
            "como_usar": "1. Dentro do seu módulo DSPy, adicione: <code>dspy.Assert(len(resposta.citacoes) > 0, 'Você deve incluir ao menos 1 citação')</code>.<br>2. Se a LLM omitir a citação, o DSPy força a auto-correção antes de devolver o resultado.<br>3. Garante conformidade com regras de negócio complexas.",
            "spec": "Biblioteca pura / 0 RAM",
            "truth": "Transforma regras de negócio subjetivas em asserções lógicas executáveis com auto-recuperação.",
            "repo": "dspy.ai"
        },
        {
            "rank": "20", "name": "Smolagents (Hugging Face)", "cat": "Code-First Agent Library", "lic": "Apache-2.0",
            "substitui": "Tool calling inflado em JSON", "econ": "-40% de tokens em chamadas de ferramentas",
            "entrega": "Biblioteca minimalista da Hugging Face onde os agentes escrevem e executam código Python puro para chamar ferramentas em vez de JSON.",
            "mecanica": "Executa o paradigma *CodeAgent*: o modelo escreve blocos de código Python padrão com condicionais e loops para interagir com múltiplas ferramentas em uma única etapa, em vez de fazer N chamadas sequenciais de JSON.",
            "cmd": "pip install smolagents",
            "como_usar": "1. Crie um agente: <code>agent = CodeAgent(tools=[busca_web, gerador_imagem], model=model)</code>.<br>2. O agente resolve tarefas complexas escrevendo um pequeno script Python.<br>3. Executa as ações em lote economizando turnos de ida e volta.",
            "spec": "< 30 MB RAM / Ultra-leve",
            "truth": "Escrever código Python é mais natural e compacto para LLMs de programação do que gerar schemas JSON gigantes.",
            "repo": "github.com/huggingface/smolagents"
        }
    ]
}

def compilar_lista_02():
    docs_dir = Path("docs/listas")
    output_dir = Path("output/listas-open-source")
    brain_dir = Path(r"C:\Users\trcnologia\.gemini\antigravity-cli\brain\0e2afde3-829c-4443-b5a5-7a8779eeb139")

    docs_dir.mkdir(parents=True, exist_ok=True)
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"[*] Compilando Lista 02 Expandida com {len(LISTA_02_EXPANDIDA['itens'])} ferramentas e skills...")
    html_content = gerar_html_completo(LISTA_02_EXPANDIDA)

    file_docs = docs_dir / "02-arquitetura-agentica-spec-driven.html"
    file_output = output_dir / "02-arquitetura-agentica-spec-driven.html"

    file_docs.write_text(html_content, encoding="utf-8")
    file_output.write_text(html_content, encoding="utf-8")

    if brain_dir.exists():
        file_brain = brain_dir / "02-arquitetura-agentica-spec-driven.html"
        file_brain.write_text(html_content, encoding="utf-8")

    print("  [OK] 02-arquitetura-agentica-spec-driven.html compilado com sucesso (20 Fichas Técnicas de Elite).")

if __name__ == "__main__":
    compilar_lista_02()
