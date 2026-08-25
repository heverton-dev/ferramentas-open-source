# -*- coding: utf-8 -*-
"""
Aplica o Dossiê Executivo Completo na Lista 01 (01-economia-de-tokens.html):
- Badge de Senioridade (Júnior, Pleno, Sênior, Especialista)
- Seção 1: O Que Faz & Como Funciona + Código com botão Copiar
- Seção 2: Análise Econômica & Substituição de SaaS (SaaS Substituídos + Economia Real Calculada)
- Seção 3: Engenharia, Infraestrutura & Stack Combinada (Infra Mínima + Ecossistema + Veredito + Botão GitHub)
- Seção 4: Como Usar no Dia a Dia (Steps Grid com 3 cards práticos)
"""
import os
import sys

def console_utf8():
    if sys.platform == "win32":
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")

console_utf8()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILEPATH = os.path.join(BASE_DIR, "output", "listas-open-source", "01-economia-de-tokens.html")

CARDS_DATA = [
    {
        "rank": 1,
        "nome": "Caveman",
        "subtitulo": "Compressão de Raciocínio CoT em Agentes",
        "senioridade": "Júnior / Iniciante",
        "senioridade_cor": "green", # green, gold, flag
        "substitui_curto": "Pensamentos CoT prolixos",
        "economia_curta": "-90% em &lt;thought&gt;",
        "licenca": "MIT / Prompt Skill",
        "kind": "Reasoning Compression",
        "o_que_faz": "Força o agente a pensar em estilo telegráfico (homem das cavernas), sem artigos, sem saudações e sem repetir o prompt do usuário.",
        "como_funciona": "Instrui o modelo a usar frases curtas de 3 a 5 linhas no Chain-of-Thought (ex: <em>'usr quer X. ler arq Y. corrigir Z.'</em>), economizando até 800 tokens a cada turno de raciocínio interno sem qualquer perda de capacidade analítica.",
        "codigo": "# Ativação via SKILL.md ou regra de sistema:\n'Para raciocínios internos, use estilo CAVEMAN telegráfico (3 a 5 linhas)'",
        "saas_substituidos": "Prompts de sistema prolixos padrão, tokens desperdiçados em CoT de modelos como Claude 3.5 Sonnet e OpenAI o1.",
        "economia_real": "Economia de ~$ 150 a $ 400 / mês por desenvolvedor ativo (~R$ 900 a R$ 2.400 / mês) em faturas de API.",
        "infra_minima": "0 MB RAM · Zero CPU (Skill de Prompt pura)",
        "ecossistema": "Claude Code, Cursor, Aider, OpenCode, VS Code Copilot",
        "veredito": "Tokens de pensamento interno custam o mesmo que tokens de saída. Pensar de forma enxuta é a vitória mais rápida da engenharia de contexto.",
        "repo_url": "https://github.com/topics/claude-skills",
        "repo_txt": "github.com/topics/claude-skills",
        "steps": [
            ("1", "Configuração", "Adicione a skill <code>caveman</code> no diretório <code>.claude/skills/</code> ou nas regras do agente."),
            ("2", "Execução", "Ao receber qualquer instrução, o modelo vai direto ao ponto no raciocínio sem floreios verbais."),
            ("3", "Resultado", "Reduza a latência de resposta em até 60% e economize 90% dos tokens internos.")
        ]
    },
    {
        "rank": 2,
        "nome": "Headroom",
        "subtitulo": "Compressão Inteligente de Logs de Terminal",
        "senioridade": "Júnior / Pleno",
        "senioridade_cor": "green",
        "substitui_curto": "Dumps gigantes de terminal",
        "economia_curta": "-80% em logs de build",
        "licenca": "MIT / Prompt Skill",
        "kind": "Log Compression",
        "o_que_faz": "Monitora e trunca saídas longas de compilação, suítes de testes e builds, mantendo apenas o topo do comando e o stack trace do erro.",
        "como_funciona": "Aplica regra comportamental rígida: se a saída do terminal tiver &gt; 7 linhas, comprime em (3 linhas do topo + 4 linhas do final), preservando a causa raiz da falha sem poluir a janela de contexto.",
        "codigo": "# Regra de compressão de saída de terminal:\n'Logs > 7 linhas -> comprimir (3 topo + 4 fim). Exceção: entregas finais'",
        "saas_substituidos": "Sessões travadas por estouro de contexto no Cursor/Claude Code, custos ocultos de reenvio de logs de CI.",
        "economia_real": "Economia de até 150.000 tokens por dia de depuração intensiva (~$ 80 a $ 200 / mês por dev).",
        "infra_minima": "0 MB RAM · Filtro em Runtime de Shell",
        "ecossistema": "Bash, PowerShell, GitHub Actions, Docker Logs, Webpack/Vite",
        "veredito": "A causa raiz do erro está quase sempre nas últimas linhas. Injetar 300 linhas de warnings irrelevantes é queimar orçamento e forçar alucinações.",
        "repo_url": "https://github.com/topics/agentic-skills",
        "repo_txt": "github.com/topics/agentic-skills",
        "steps": [
            ("1", "Integração", "Declare a regra <code>headroom</code> nas diretrizes de execução de comandos do seu assistente."),
            ("2", "Captura", "Quando um <code>npm run build</code> falhar com 500 linhas, o agente recebe apenas o cabeçalho e o erro."),
            ("3", "Resolução", "O agente foca na correção da causa raiz sem saturar o contexto com saídas repetitivas.")
        ]
    },
    {
        "rank": 3,
        "nome": "Lean-CTX",
        "subtitulo": "Inspeção Cirúrgica de Código com Grep Prévio",
        "senioridade": "Pleno",
        "senioridade_cor": "gold",
        "substitui_curto": "view_file() de arquivos inteiros",
        "economia_curta": "-85% de leitura de código",
        "licenca": "MIT / Prompt Skill",
        "kind": "Targeted Inspection",
        "o_que_faz": "Obriga o agente a usar <code>grep_search</code> e ler apenas trechos específicos com intervalo de linhas em vez de carregar arquivos completos.",
        "como_funciona": "Impõe restrição comportamental: antes de ler qualquer arquivo com mais de 50 linhas, o agente deve localizar o símbolo exato e ler apenas a janela necessária (<code>StartLine/EndLine</code>).",
        "codigo": "# Protocolo Lean-CTX:\n'Grep antes de read. Limitar leitura por intervalo estrito de linhas'",
        "saas_substituidos": "Ferramentas de indexação pesada em nuvem pagas por repositório (Sourcegraph Cloud, Bloop Enterprise).",
        "economia_real": "Reduz o consumo de contexto em 85%, economizando ~$ 250 a $ 600 / mês em projetos de grande porte.",
        "infra_minima": "0 MB RAM · Depende apenas do ripgrep (rg) local",
        "ecossistema": "ripgrep, fd, ast-grep, Git, VS Code, NeoVim",
        "veredito": "A maior causa de esquecimento em conversas longas é o hábito do agente de ler arquivos inteiros para editar apenas 5 linhas de código.",
        "repo_url": "https://github.com/topics/context-engineering",
        "repo_txt": "github.com/topics/context-engineering",
        "steps": [
            ("1", "Localização", "Ao pedir para alterar uma função em um arquivo grande, o agente executa <code>grep_search</code> pelo nome."),
            ("2", "Leitura Seletiva", "Lê cirurgicamente 20 linhas ao redor do trecho com <code>view_file(StartLine=120, EndLine=140)</code>."),
            ("3", "Economia", "Economiza milhares de linhas de contexto, mantendo a atenção do modelo focada na implementação.")
        ]
    },
    {
        "rank": 4,
        "nome": "RTK-Memory",
        "subtitulo": "Memória Scratchpad com Prefix Cache Imutável",
        "senioridade": "Pleno / Sênior",
        "senioridade_cor": "gold",
        "substitui_curto": "Reenvio de histórico no prompt",
        "economia_curta": "100% Prefix Cache Reuso",
        "licenca": "MIT / Scratchpad Skill",
        "kind": "Persistent Cache",
        "o_que_faz": "Persiste novos aprendizados e correções em um arquivo externo (<code>RTK-SCRATCHPAD.md</code>) para manter as instruções base 100% imutáveis e cacheadas.",
        "como_funciona": "Mantém o arquivo de governança principal (<code>AGENTS.md</code> / <code>CLAUDE.md</code>) intacto para que Anthropic/OpenAI façam reuso do cache de prefixo (desconto de até 90% no input). Aprendizados da sessão são appendados em arquivo separado consultado sob demanda.",
        "codigo": "# Protocolo RTK:\n'Novos aprendizados: SEMPRE appendar em RTK-SCRATCHPAD.md, nunca no system prompt'",
        "saas_substituidos": "Bancos vetoriais gerenciados caros para memória de agente (Pinecone, MemGPT Cloud).",
        "economia_real": "Garante até 90% de desconto contínuo no custo de tokens de entrada em modelos com Prompt Caching.",
        "infra_minima": "Arquivo Markdown Local · Zero RAM e Zero Banco de Dados",
        "ecossistema": "Anthropic Prompt Caching, OpenAI Prefix Cache, DeepSeek Prompt Cache",
        "veredito": "Editar o prompt de sistema invalida o cache de prefixo nos provedores, encarecendo todas as chamadas seguintes do projeto.",
        "repo_url": "https://github.com/topics/prompt-caching",
        "repo_txt": "github.com/topics/prompt-caching",
        "steps": [
            ("1", "Registro", "Quando o agente aprende uma preferência de arquitetura, registra a nota no final do <code>RTK-SCRATCHPAD.md</code>."),
            ("2", "Consulta", "Em sessões futuras, consulta o scratchpad apenas quando o tópico exigir contexto passado específico."),
            ("3", "Aquecimento", "Mantém o prefix cache do system prompt 100% aquecido com custo mínimo de tokens de entrada.")
        ]
    },
    {
        "rank": 5,
        "nome": "Repomix",
        "subtitulo": "Compactador Universal de Código para Contexto de LLMs",
        "senioridade": "Júnior / Pleno",
        "senioridade_cor": "green",
        "substitui_curto": "Leitura manual de múltiplos arquivos",
        "economia_curta": "-70% por prompt (~$ 300/mês)",
        "licenca": "MIT",
        "kind": "Context Packing",
        "o_que_faz": "Empacota repositórios inteiros em 1 arquivo XML/Markdown com contagem exata de tokens e filtros inteligentes de .gitignore.",
        "como_funciona": "Varre o repositório, descarta binários, lockfiles e arquivos ignorados no Git e compila um documento único com cabeçalhos XML e numeração de linhas para leitura otimizada por LLMs.",
        "codigo": "npx repomix --style xml --output-show-line-numbers --include 'src/**/*.ts'",
        "saas_substituidos": "Plugins de contexto pagos de IDEs, upload manual de dezenas de arquivos em interfaces web de chat.",
        "economia_real": "Economia de ~$ 300 a $ 800 / mês em horas de desenvolvedor e tokens de uploads duplicados.",
        "infra_minima": "&lt; 30 MB RAM · Executável Node.js / CLI",
        "ecossistema": "Node.js, npm, npx, Claude Desktop, ChatGPT, Gemini Advanced",
        "veredito": "Remove automaticamente ruídos pesados (node_modules, build artifacts) antes de enviar o contexto à LLM, evitando estourar a janela de contexto.",
        "repo_url": "https://github.com/yamadashy/repomix",
        "repo_txt": "github.com/yamadashy/repomix",
        "steps": [
            ("1", "Empacotamento", "Antes de iniciar uma feature complexa, execute <code>npx repomix</code> apontando para as pastas alvo."),
            ("2", "Auditoria", "Verifique a contagem exata de tokens gerada no cabeçalho do arquivo <code>repomix-output.xml</code>."),
            ("3", "Utilização", "Forneça o arquivo como anexo ou contexto inicial do assistente para visão arquitetural instantânea.")
        ]
    },
    {
        "rank": 6,
        "nome": "ast-grep (sg)",
        "subtitulo": "Busca e Reescrita Estrutural baseada na AST",
        "senioridade": "Pleno / Sênior",
        "senioridade_cor": "gold",
        "substitui_curto": "Refatorações caras via LLM",
        "economia_curta": "100% Grátis em Transformações",
        "licenca": "MIT",
        "kind": "AST Search & Rewrite",
        "o_que_faz": "Busca e reescrita de código baseada na Árvore de Sintaxe Abstrata (AST). Não erra indentação nem quebra sintaxe.",
        "como_funciona": "Faz o parsing do código-fonte em nós sintáticos via Tree-sitter em Rust, permitindo substituir estruturas complexas com curingas (<code>$$$ARGS</code>) em 2ms.",
        "codigo": "cargo install ast-grep && sg -p 'api.get($URL)' -r 'api.fetch({url: $URL})' -w",
        "saas_substituidos": "Cobranças massivas de tokens LLM para refatoração de dezenas de arquivos, jscodeshift complexo.",
        "economia_real": "Custo $ 0 de tokens para renomear e reestruturar APIs em milhares de arquivos simultaneamente.",
        "infra_minima": "Binário Rust compilado · &lt; 10 MB RAM em execução",
        "ecossistema": "Tree-sitter, Rust, VS Code, CI/CD Linters, TypeScript/Python/Go",
        "veredito": "Substitui prompts caros de 'renomeie / refatore assinatura' por uma chamada determinística de microssegundos no terminal.",
        "repo_url": "https://ast-grep.github.io",
        "repo_txt": "ast-grep.github.io",
        "steps": [
            ("1", "Padrão", "Defina a transformação estrutural usando a sintaxe de pattern matching do ast-grep."),
            ("2", "Aplicação", "O <code>sg</code> aplica a reescrita estrutural em dezenas de arquivos em 2ms com precisão absoluta."),
            ("3", "Economia", "Zero tokens gastos para refatorações repetitivas em lote em todo o repositório.")
        ]
    },
    {
        "rank": 7,
        "nome": "LiteLLM Semantic Cache",
        "subtitulo": "Gateway Inteligente com Cache Semântico de Respostas",
        "senioridade": "Pleno / DevOps",
        "senioridade_cor": "gold",
        "substitui_curto": "Chamadas duplicadas em APIs",
        "economia_curta": "-40% a -60% na fatura (~$ 500/mês)",
        "licenca": "MIT",
        "kind": "AI Gateway & Cache",
        "o_que_faz": "Gateway de roteamento inteligente e cache semântico de respostas de LLM em Redis com balanceamento de carga.",
        "como_funciona": "Calcula embeddings de prompts recebidos e faz busca por similaridade de cosseno no Redis. Se a similaridade for &gt; 0.95, devolve a resposta cacheada em 2ms com custo $ 0.",
        "codigo": "docker run -d -p 4000:4000 -v $(pwd)/config.yaml:/app/config.yaml ghcr.io/berriai/litellm:main-latest",
        "saas_substituidos": "Portkey AI ($99/mês), Helicone Pro ($79/mês), Langfuse Cloud, faturas infladas da OpenAI/Anthropic.",
        "economia_real": "Economia de $ 300 a $ 1.500 / mês (~R$ 1.800 a R$ 9.000 / mês) em ambientes corporativos e suítes de testes.",
        "infra_minima": "1 vCPU · 256 MB RAM · Docker + Redis local ou compartilhado",
        "ecossistema": "Redis, Docker, LangChain, LlamaIndex, OpenAI SDK, Anthropic SDK",
        "veredito": "Essencial para suítes de testes automatizados, CI/CD e atendimentos repetitivos de usuários que disparam perguntas frequentes.",
        "repo_url": "https://litellm.ai",
        "repo_txt": "litellm.ai",
        "steps": [
            ("1", "Inicialização", "Suba o LiteLLM apontando para sua instância Redis no arquivo <code>config.yaml</code>."),
            ("2", "Redirecionamento", "Altere a <code>BASE_URL</code> das suas aplicações e scripts para <code>http://localhost:4000</code>."),
            ("3", "Custo Zero", "Suítes de testes e perguntas idênticas respondem em 2ms com custo zero de API.")
        ]
    },
    {
        "rank": 8,
        "nome": "DSPy (Stanford)",
        "subtitulo": "Compilador Algorítmico de Prompts e Pipelines",
        "senioridade": "Sênior / Engenheiro de IA",
        "senioridade_cor": "flag",
        "substitui_curto": "Engenharia de prompt manual",
        "economia_curta": "-50% no tamanho do prompt",
        "licenca": "MIT",
        "kind": "Prompt Compiler",
        "o_que_faz": "Compila e otimiza automaticamente instruções e few-shots via algoritmos matemáticos para máxima acurácia no menor tamanho de prompt.",
        "como_funciona": "Modela o pipeline como grafo computacional diferenciável. Otimizadores como <code>BootstrapFewShot</code> testam permutações contra métricas e geram a versão mais enxuta e assertiva.",
        "codigo": "pip install dspy-ai\n# Otimização matemática de prompts com BootstrapFewShot",
        "saas_substituidos": "Consultorias caras de engenharia de prompt, ferramentas fechadas de otimização de prompts (PromptLayer Pro).",
        "economia_real": "Reduz o tamanho médio de prompts de produção em até 50%, cortando pela metade a fatura recorrente de LLM.",
        "infra_minima": "Biblioteca Python Pura · Zero Runtime RAM adicional",
        "ecossistema": "PyTorch, Hugging Face, OpenAI, Anthropic, Ollama, vLLM",
        "veredito": "Trata prompts como código compilável. Ao mudar de modelo LLM, basta recompilar o pipeline sem reescrever instruções manualmente.",
        "repo_url": "https://dspy.ai",
        "repo_txt": "dspy.ai",
        "steps": [
            ("1", "Definição", "Defina a assinatura do módulo em Python: <code>class Extrator(dspy.Module): ...</code>."),
            ("2", "Exemplos", "Forneça de 10 a 20 exemplos validados de dados de entrada e saída esperada."),
            ("3", "Compilação", "O compilador do DSPy gera automaticamente o prompt mais curto e assertivo para produção.")
        ]
    }
]

CSS_REFINADO = """
  /* BADGE DE SENIORIDADE */
  .senior-badge { font-family:var(--mono); font-size:10.5px; letter-spacing:.08em; text-transform:uppercase; padding:3px 8px; border-radius:2px; font-weight:700; }
  .senior-badge.green { background:var(--green-soft); color:var(--green); border:1px solid color-mix(in srgb, var(--green) 35%, transparent); }
  .senior-badge.gold { background:var(--gold-soft); color:var(--gold); border:1px solid color-mix(in srgb, var(--gold) 35%, transparent); }
  .senior-badge.flag { background:var(--flag-soft); color:var(--flag); border:1px solid color-mix(in srgb, var(--flag) 35%, transparent); }

  /* CARDS DE ECONOMIA & ENGENHARIA 2 COLUNAS / 3 COLUNAS */
  .econ-grid { display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:12px; margin-top:4px; }
  .econ-card { background:var(--surface-2); border:1px solid var(--rule-soft); border-radius:2px; padding:12px 14px; display:flex; flex-direction:column; gap:4px; }
  .econ-card.highlight { border-left:3px solid var(--green); background:color-mix(in srgb, var(--green-soft) 25%, var(--surface)); }
  .econ-card.killer { border-left:3px solid var(--flag); background:color-mix(in srgb, var(--flag-soft) 25%, var(--surface)); }
  .econ-lbl { font-family:var(--mono); font-size:10.5px; text-transform:uppercase; letter-spacing:.08em; color:var(--muted); font-weight:600; }
  .econ-val { font-size:14px; line-height:1.45; color:var(--ink); }
  .econ-val strong { color:var(--ink); font-weight:600; }

  .infra-grid { display:grid; grid-template-columns:repeat(auto-fit, minmax(220px, 1fr)); gap:12px; margin-top:4px; }
  .infra-card { background:var(--surface-2); border:1px solid var(--rule-soft); border-radius:2px; padding:12px 14px; display:flex; flex-direction:column; gap:4px; }
  .infra-card.verdict { border-left:3px solid var(--gold); background:color-mix(in srgb, var(--gold-soft) 25%, var(--surface)); grid-column:span 2; }
  @media (max-width:760px) { .infra-card.verdict { grid-column:span 1; } }
  .infra-lbl { font-family:var(--mono); font-size:10.5px; text-transform:uppercase; letter-spacing:.08em; color:var(--muted); font-weight:600; }
  .infra-val { font-family:var(--mono); font-size:13.5px; font-weight:600; color:var(--accent); line-height:1.4; }
  .infra-card p { margin:0; font-size:13.5px; line-height:1.45; color:var(--ink-2); }
"""

def render_dossie_entry(item):
    steps_html = []
    for num, head, desc in item["steps"]:
        steps_html.append(f"""              <div class="step-card">
                <div class="step-head"><span class="step-badge">{num}</span> {head}</div>
                <p>{desc}</p>
              </div>""")
    steps_block = "\n".join(steps_html)

    return f"""      <!-- {item['rank']:02d}. {item['nome']} -->
      <div class="entry">
        <div class="entry-rank">{item['rank']:02d}</div>
        <div class="entry-body">
          
          <!-- CABEÇALHO & BADGES -->
          <div class="entry-top">
            <h3>{item['nome']} · {item['subtitulo']}</h3>
            <span class="senior-badge {item['senioridade_cor']}">👨‍💻 Nível: {item['senioridade']}</span>
            <span class="killer-badge">Substitui: {item['substitui_curto']}</span>
            <span class="econ-badge">Economia: {item['economia_curta']}</span>
            <span class="lic-badge">{item['licenca']}</span>
            <span class="kind">{item['kind']}</span>
          </div>

          <!-- SEÇÃO 1: O QUE FAZ & COMO FUNCIONA -->
          <div class="entry-section">
            <span class="label">1. O Que Faz &amp; Como Funciona</span>
            <p>{item['o_que_faz']}</p>
            <p>{item['como_funciona']}</p>
            <div class="code-box">
              <pre><code>{item['codigo']}</code></pre>
              <button class="copy-btn" onclick="navigator.clipboard.writeText(this.previousElementSibling.textContent.trim());this.textContent='Copiado!';setTimeout(()=>this.textContent='Copiar',1500)">Copiar</button>
            </div>
          </div>

          <!-- SEÇÃO 2: ANÁLISE ECONÔMICA & SUBSTITUIÇÃO DE SAAS -->
          <div class="entry-section">
            <span class="label">2. Análise Econômica &amp; Substituição de Soluções Proprietárias</span>
            <div class="econ-grid">
              <div class="econ-card killer">
                <span class="econ-lbl">💸 Produtos SaaS Substituídos</span>
                <div class="econ-val">{item['saas_substituidos']}</div>
              </div>
              <div class="econ-card highlight">
                <span class="econ-lbl">💰 Economia Real Estimada no TCO</span>
                <div class="econ-val"><strong>{item['economia_real']}</strong></div>
              </div>
            </div>
          </div>

          <!-- SEÇÃO 3: REQUISITOS DE INFRAESTRUTURA & ECOSSISTEMA -->
          <div class="entry-section">
            <span class="label">3. Requisitos de Infraestrutura, Ecossistema &amp; Veredito</span>
            <div class="infra-grid">
              <div class="infra-card">
                <span class="infra-lbl">🖥️ Infraestrutura Recomendada</span>
                <div class="infra-val">{item['infra_minima']}</div>
              </div>
              <div class="infra-card">
                <span class="infra-lbl">🔗 Ecossistema &amp; Compatibilidade</span>
                <p><code>{item['ecossistema']}</code></p>
              </div>
              <div class="infra-card verdict">
                <span class="infra-lbl">🏆 Veredito do Arquiteto</span>
                <p><strong>Por que adotar:</strong> {item['veredito']}</p>
              </div>
            </div>
            <div style="margin-top:6px;">
              <a class="repo-btn" href="{item['repo_url']}" target="_blank" rel="noopener">
                <svg viewBox="0 0 24 24"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/></svg>
                <span>Repositório Oficial &amp; Documentação Técnica: {item['repo_txt']} ↗</span>
              </a>
            </div>
          </div>

          <!-- SEÇÃO 4: COMO USAR NO DIA A DIA -->
          <div class="entry-section">
            <span class="label">4. Como Usar no Dia a Dia (Passo a Passo Prático)</span>
            <div class="steps-grid">
{steps_block}
            </div>
          </div>

        </div>
      </div>"""

def main():
    import re
    with open(FILEPATH, "r", encoding="utf-8") as f:
        content = f.read()

    # Injetar CSS adicional se não existir
    if ".senior-badge" not in content:
        content = content.replace("</style>", f"{CSS_REFINADO}\n</style>")

    entries_html = "\n\n".join([render_dossie_entry(item) for item in CARDS_DATA])

    new_ledger = f"""    <div class="ledger">
{entries_html}
    </div>"""

    content = re.sub(r'<div class="ledger">.*?</div>\s*(?=\s*</section>)', new_ledger, content, flags=re.DOTALL)

    with open(FILEPATH, "w", encoding="utf-8") as f:
        f.write(content)

    print("[✓] Lista 01 atualizada com o Dossiê Executivo Completo!")

if __name__ == "__main__":
    main()
