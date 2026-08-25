# -*- coding: utf-8 -*-
"""
Aplica a arquitetura vertical com largura 100% nas 8 fichas da lista 01.
"""
import os
import sys
import re

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
        "substitui": "Pensamentos CoT prolixos e caros",
        "economia": "-90% em &lt;thought&gt;",
        "licenca": "MIT / Prompt Skill",
        "kind": "Reasoning Compression",
        "o_que_faz": "Força o agente a pensar em estilo telegráfico (homem das cavernas), sem artigos, sem saudações e sem repetir o prompt do usuário.",
        "como_funciona": "Instrui o modelo a usar frases curtas de 3 a 5 linhas no Chain-of-Thought (ex: <em>'usr quer X. ler arq Y. corrigir Z.'</em>), economizando até 800 tokens a cada turno de raciocínio interno sem qualquer perda de capacidade analítica.",
        "codigo": "# Ativação via SKILL.md ou regra de sistema:\n'Para raciocínios internos, use estilo CAVEMAN telegráfico (3 a 5 linhas)'",
        "spec_lbl": "Overhead em Memória",
        "spec_val": "0 MB RAM · Zero Overhead",
        "veredito": "Tokens de pensamento interno custam exatamente o mesmo que tokens de saída. Pensar de forma enxuta e telegráfica é a forma mais rápida e eficaz de cortar custos em agentes.",
        "repo_url": "https://github.com/topics/claude-skills",
        "repo_txt": "github.com/topics/claude-skills",
        "steps": [
            ("1", "Configuração", "Adicione a skill <code>caveman</code> no diretório <code>.claude/skills/</code> ou no arquivo de regras de sistema do agente."),
            ("2", "Execução", "Ao receber qualquer instrução, o modelo vai direto ao ponto na análise técnica sem floreios verbais."),
            ("3", "Resultado", "Reduza a latência de resposta em até 60% e economize 90% dos tokens de pensamento interno.")
        ]
    },
    {
        "rank": 2,
        "nome": "Headroom",
        "subtitulo": "Compressão Inteligente de Logs de Terminal",
        "substitui": "Dumps gigantes de terminal no contexto",
        "economia": "-80% em logs de build",
        "licenca": "MIT / Prompt Skill",
        "kind": "Log Compression",
        "o_que_faz": "Monitora e trunca saídas longas de compilação, suítes de testes e builds, mantendo apenas o topo do comando e o stack trace do erro.",
        "como_funciona": "Aplica regra comportamental rígida: se a saída do terminal tiver &gt; 7 linhas, comprime em (3 linhas do topo + 4 linhas do final), preservando a causa raiz da falha sem poluir a janela de contexto.",
        "codigo": "# Regra de compressão de saída de terminal:\n'Logs > 7 linhas -> comprimir (3 topo + 4 fim). Exceção: entregas finais'",
        "spec_lbl": "Impacto em Runtime",
        "spec_val": "0 MB RAM · Filtro em Runtime",
        "veredito": "A causa raiz do erro está quase sempre nas últimas linhas. Injetar 300 linhas de warnings irrelevantes no contexto é queimar orçamento e empurrar o modelo para o esquecimento.",
        "repo_url": "https://github.com/topics/agentic-skills",
        "repo_txt": "github.com/topics/agentic-skills",
        "steps": [
            ("1", "Integração", "Declare a regra <code>headroom</code> nas diretrizes de execução de comandos do seu assistente de código."),
            ("2", "Captura", "Quando um comando como <code>npm run build</code> falhar com 500 linhas, o agente recebe apenas a fatia exata da falha."),
            ("3", "Resolução", "O agente foca na correção da causa raiz sem saturar o contexto com saídas repetitivas.")
        ]
    },
    {
        "rank": 3,
        "nome": "Lean-CTX",
        "subtitulo": "Inspeção Cirúrgica de Código com Grep Prévio",
        "substitui": "view_file() do arquivo inteiro",
        "economia": "-85% de leitura de código",
        "licenca": "MIT / Prompt Skill",
        "kind": "Targeted Inspection",
        "o_que_faz": "Obriga o agente a usar <code>grep_search</code> e ler apenas trechos específicos com intervalo de linhas em vez de carregar arquivos completos.",
        "como_funciona": "Impõe restrição comportamental: antes de ler qualquer arquivo com mais de 50 linhas, o agente deve localizar o símbolo exato e ler apenas a janela necessária (<code>StartLine/EndLine</code>).",
        "codigo": "# Protocolo Lean-CTX:\n'Grep antes de read. Limitar leitura por intervalo estrito de linhas'",
        "spec_lbl": "Disciplina de Contexto",
        "spec_val": "0 MB RAM · Disciplina Agêntica",
        "veredito": "A maior causa de alucinação e perda de contexto em conversas longas é o hábito do agente de ler arquivos inteiros para editar apenas 5 linhas de código.",
        "repo_url": "https://github.com/topics/context-engineering",
        "repo_txt": "github.com/topics/context-engineering",
        "steps": [
            ("1", "Localização", "Ao solicitar a edição de uma função em um arquivo de 1.500 linhas, o agente executa <code>grep_search</code> pelo nome exato."),
            ("2", "Leitura Seletiva", "Executa a leitura cirúrgica de apenas 20 linhas ao redor do trecho com <code>view_file(StartLine=120, EndLine=140)</code>."),
            ("3", "Economia", "Economiza mais de 1.400 linhas de contexto, mantendo a atenção do modelo focada na implementação.")
        ]
    },
    {
        "rank": 4,
        "nome": "RTK-Memory",
        "subtitulo": "Memória Scratchpad com Prefix Cache Imutável",
        "substitui": "Reenvio de histórico no prompt",
        "economia": "100% Prefix Cache Reuso",
        "licenca": "MIT / Scratchpad Skill",
        "kind": "Persistent Cache",
        "o_que_faz": "Persiste novos aprendizados e correções em um arquivo externo (<code>RTK-SCRATCHPAD.md</code>) para manter as instruções base 100% imutáveis e cacheadas.",
        "como_funciona": "Mantém o arquivo de governança principal (<code>AGENTS.md</code> / <code>CLAUDE.md</code>) intacto para que Anthropic/OpenAI façam reuso do cache de prefixo (desconto de até 90% no input). Aprendizados da sessão são appendados em arquivo separado consultado sob demanda.",
        "codigo": "# Protocolo RTK:\n'Novos aprendizados: SEMPRE appendar em RTK-SCRATCHPAD.md, nunca no system prompt'",
        "spec_lbl": "Armazenamento",
        "spec_val": "Markdown Local · Zero RAM",
        "veredito": "Editar o prompt de sistema invalida o cache de prefixo nos provedores, encarecendo todas as requisições seguintes do projeto.",
        "repo_url": "https://github.com/topics/prompt-caching",
        "repo_txt": "github.com/topics/prompt-caching",
        "steps": [
            ("1", "Registro", "Quando o agente aprende uma preferência de arquitetura ou resolve um bug, registra a nota no final do <code>RTK-SCRATCHPAD.md</code>."),
            ("2", "Consulta", "Em sessões futuras, consulta o scratchpad apenas quando o tópico exigir contexto histórico específico."),
            ("3", "Aquecimento", "Garante que o prefix cache do system prompt continue 100% aquecido com custo mínimo de tokens de entrada.")
        ]
    },
    {
        "rank": 5,
        "nome": "Repomix",
        "subtitulo": "Compactador Universal de Código para Contexto de LLMs",
        "substitui": "Leitura manual de múltiplos arquivos",
        "economia": "-70% de tokens por prompt (~$ 300/mês)",
        "licenca": "MIT",
        "kind": "Context Packing",
        "o_que_faz": "Empacota repositórios inteiros em 1 arquivo XML/Markdown com contagem exata de tokens e filtros inteligentes de .gitignore.",
        "como_funciona": "Varre o repositório, descarta binários, lockfiles e arquivos ignorados no Git e compila um documento único com cabeçalhos XML e numeração de linhas para leitura otimizada por LLMs.",
        "codigo": "npx repomix --style xml --output-show-line-numbers --include 'src/**/*.ts'",
        "spec_lbl": "Consumo de Recursos",
        "spec_val": "< 30 MB RAM · CLI Sob Demanda",
        "veredito": "Remove automaticamente arquivos binários, lockfiles e assets pesados antes de enviar o contexto à LLM, evitando estourar a janela de contexto.",
        "repo_url": "https://github.com/yamadashy/repomix",
        "repo_txt": "github.com/yamadashy/repomix",
        "steps": [
            ("1", "Empacotamento", "Antes de iniciar uma feature complexa, execute <code>npx repomix</code> apontando para as pastas de código-fonte."),
            ("2", "Auditoria", "Verifique a contagem exata de tokens gerada no cabeçalho do arquivo <code>repomix-output.xml</code>."),
            ("3", "Utilização", "Forneça o arquivo como anexo ou contexto inicial do assistente para visão arquitetural instantânea.")
        ]
    },
    {
        "rank": 6,
        "nome": "ast-grep (sg)",
        "subtitulo": "Busca e Reescrita Estrutural baseada na AST",
        "substitui": "Refatorações caras via LLM",
        "economia": "100% Grátis em Transformações",
        "licenca": "MIT",
        "kind": "AST Search & Rewrite",
        "o_que_faz": "Busca e reescrita de código baseada na Árvore de Sintaxe Abstrata (AST). Não erra indentação nem quebra sintaxe.",
        "como_funciona": "Faz o parsing do código-fonte em nós sintáticos via Tree-sitter em Rust, permitindo substituir estruturas complexas com curingas (<code>$$$ARGS</code>) em 2ms.",
        "codigo": "cargo install ast-grep && sg -p 'api.get($URL)' -r 'api.fetch({url: $URL})' -w",
        "spec_lbl": "Performance de Execução",
        "spec_val": "Binário Rust · < 10 MB RAM",
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
        "substitui": "Chamadas duplicadas em APIs de LLM",
        "economia": "-40% a -60% na fatura (~$ 500/mês)",
        "licenca": "MIT",
        "kind": "AI Gateway & Cache",
        "o_que_faz": "Gateway de roteamento inteligente e cache semântico de respostas de LLM em Redis com balanceamento de carga.",
        "como_funciona": "Calcula embeddings de prompts recebidos e faz busca por similaridade de cosseno no Redis. Se a similaridade for &gt; 0.95, devolve a resposta cacheada em 2ms com custo $ 0.",
        "codigo": "docker run -d -p 4000:4000 -v $(pwd)/config.yaml:/app/config.yaml ghcr.io/berriai/litellm:main-latest",
        "spec_lbl": "Footprint de Infra",
        "spec_val": "~70 MB RAM em Repouso",
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
        "substitui": "Engenharia de prompt manual cara",
        "economia": "Reduz tamanho de prompt em até 50%",
        "licenca": "MIT",
        "kind": "Prompt Compiler",
        "o_que_faz": "Compila e otimiza automaticamente instruções e few-shots via algoritmos matemáticos para máxima acurácia no menor tamanho de prompt.",
        "como_funciona": "Modela o pipeline como grafo computacional diferenciável. Otimizadores como <code>BootstrapFewShot</code> testam permutações contra métricas e geram a versão mais enxuta e assertiva.",
        "codigo": "pip install dspy-ai\n# Otimização automática de prompts com BootstrapFewShot",
        "spec_lbl": "Execução em Python",
        "spec_val": "Biblioteca Pura · Zero Runtime RAM",
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

def render_entry(item):
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
          <div class="entry-top">
            <h3>{item['nome']} · {item['subtitulo']}</h3>
            <span class="killer-badge">Substitui: {item['substitui']}</span>
            <span class="econ-badge">Economia: {item['economia']}</span>
            <span class="lic-badge">{item['licenca']}</span>
            <span class="kind">{item['kind']}</span>
          </div>

          <!-- SEÇÃO 1: O QUE FAZ & COMO FUNCIONA (LARGURA TOTAL) -->
          <div class="entry-section">
            <span class="label">1. O Que Faz &amp; Como Funciona</span>
            <p>{item['o_que_faz']}</p>
            <p>{item['como_funciona']}</p>
            <div class="code-box">
              <pre><code>{item['codigo']}</code></pre>
              <button class="copy-btn" onclick="navigator.clipboard.writeText(this.previousElementSibling.textContent.trim());this.textContent='Copiado!';setTimeout(()=>this.textContent='Copiar',1500)">Copiar</button>
            </div>
          </div>

          <!-- SEÇÃO 2: ENGENHARIA, ESPECIFICAÇÕES & VEREDITO (LARGURA TOTAL) -->
          <div class="entry-section">
            <span class="label">2. Engenharia, Especificações &amp; Veredito de Produção</span>
            <div class="tech-grid">
              <div class="tech-card">
                <span class="tech-lbl">{item['spec_lbl']}</span>
                <span class="tech-val">{item['spec_val']}</span>
              </div>
              <div class="tech-card verdict">
                <span class="tech-lbl">Veredito da Engenharia</span>
                <p><strong>Por que é ouro:</strong> {item['veredito']}</p>
              </div>
              <div class="tech-card" style="justify-content:center;align-items:center;">
                <a class="repo-btn" href="{item['repo_url']}" target="_blank" rel="noopener" style="width:100%;">
                  <svg viewBox="0 0 24 24"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/></svg>
                  <span>{item['repo_txt']} ↗</span>
                </a>
              </div>
            </div>
          </div>

          <!-- SEÇÃO 3: COMO USAR NO DIA A DIA (LARGURA TOTAL COM STEPS-GRID) -->
          <div class="entry-section">
            <span class="label">3. Como Usar no Dia a Dia (Passo a Passo Prático)</span>
            <div class="steps-grid">
{steps_block}
            </div>
          </div>
        </div>
      </div>"""

def main():
    with open(FILEPATH, "r", encoding="utf-8") as f:
        content = f.read()

    entries_html = "\n\n".join([render_entry(item) for item in CARDS_DATA])

    # Substitui a div.ledger inteira
    new_ledger = f"""    <div class="ledger">
{entries_html}
    </div>"""

    content = re.sub(r'<div class="ledger">.*?</div>\s*(?=\s*</section>)', new_ledger, content, flags=re.DOTALL)

    with open(FILEPATH, "w", encoding="utf-8") as f:
        f.write(content)

    print("[✓] Todas as 8 fichas da Lista 01 foram atualizadas para o novo layout vertical 100% de largura!")

if __name__ == "__main__":
    main()
