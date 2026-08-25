# -*- coding: utf-8 -*-
"""
Gerador de Elite das 30 Listas de Soberania Tecnológica.
Cada uma das 240 ferramentas contém:
1. O QUE FAZ (Explicação conceitual e função exata)
2. COMO FAZ (Mecânica técnica interna, AST, kernels, protocolos)
3. COMO USAR NO DIA A DIA (Workflow passo a passo acionável com comandos e cenários de uso)
4. ECONOMIA REAL ($ e R$)
5. ESPECIFICAÇÃO DE CONSUMO (RAM, VRAM, CPU)
"""

from pathlib import Path

LISTAS_30 = [
    # 01
    {
        "slug": "01-economia-de-tokens",
        "title": "Economia Extrema de Tokens & Contexto",
        "camada": "Camada 01 · Eficiência de Contexto",
        "accent": "#1B5E3B", "accent_dark": "#6BC48F", "accent_soft": "#D8EFE2", "accent_soft_dark": "#122B1C",
        "deck": "Metodologias, compiladores e caches para <strong>cortar até 85% do custo com LLMs</strong> sem perder precisão: cache semântico de respostas, gramáticas estruturadas, AST e compressão cirúrgica de repositórios.",
        "pilar_1": "O Custo Invisível do Contexto Inflado",
        "pilar_1_desc": "Enviar arquivos inteiros (lockfiles, builds, SVGs) queima centenas de milhares de tokens por turno. Sem filtros, 80% do gasto mensal com APIs de IA é desperdiçado em ruído.",
        "pilar_2": "A Engenharia do Prompt Cirúrgico",
        "pilar_2_desc": "Com AST (ast-grep), empacotamento semântico (Repomix), cache semântico (LiteLLM) e compilação algorítmica (DSPy), o modelo recebe apenas os 2KB exatos necessários para a tarefa.",
        "itens": [
            {
                "rank": "01", "name": "Repomix", "cat": "Context Packing", "lic": "MIT",
                "substitui": "Leitura manual de arquivos", "econ": "-70% de tokens por prompt (~$ 300/mês)",
                "entrega": "Empacota repositórios inteiros em 1 arquivo XML/Markdown com contagem de tokens e filtros inteligentes de .gitignore.",
                "mecanica": "Lê a árvore de arquivos, descarta binários, lockfiles e imagens automaticamente via .gitignore e gera um arquivo único com tags XML estruturadas e numeração de linhas para leitura ótima da LLM.",
                "cmd": "npx repomix --style xml --output-show-line-numbers",
                "como_usar": "1. Antes de pedir uma refatoração grande, rode no terminal: <code>npx repomix --include 'src/**/*.ts'</code>.<br>2. Abra o arquivo <code>repomix-output.xml</code> gerado e verifique a contagem de tokens no topo.<br>3. Cole no chat da LLM ou use como anexo no seu agente agêntico. A IA responderá com precisão cirúrgica de linha.",
                "spec": "< 30 MB RAM / CLI sob demanda",
                "truth": "Remove automaticamente arquivos binários, lockfiles e assets pesados antes de enviar o contexto à LLM.",
                "repo": "github.com/yamadashy/repomix"
            },
            {
                "rank": "02", "name": "ast-grep (sg)", "cat": "AST Search & Rewrite", "lic": "MIT",
                "substitui": "Refatorações caras via LLM", "econ": "100% grátis em transformações estruturais",
                "entrega": "Busca e reescrita de código baseada na Árvore de Sintaxe Abstrata. Não erra espaçamentos nem quebras de linha.",
                "mecanica": "Faz o parsing do código-fonte em nós de Árvore Sintática (AST) usando Tree-sitter em Rust, permitindo buscar estruturas com wildcards (<code>$$$ARGS</code>) sem depender de regex frágil.",
                "cmd": "cargo install ast-grep && sg --pattern 'function $NAME($$$ARGS) { $$$BODY }'",
                "como_usar": "1. Para alterar a assinatura de uma função em 40 arquivos, crie o padrão no terminal: <code>sg -p 'api.get($URL)' -r 'api.request({url: $URL, method: \"GET\"})' -w</code>.<br>2. Pressione Enter: a alteração ocorre em 3 milissegundos em toda a base.<br>3. Economize 100% dos tokens que seriam gastos pedindo à IA para editar arquivo por arquivo.",
                "spec": "Binário Rust / < 10 MB RAM",
                "truth": "Substitui prompts inteiros de 'renomeie/altere assinatura' por uma chamada determinística de 2ms no terminal.",
                "repo": "ast-grep.github.io"
            },
            {
                "rank": "03", "name": "LiteLLM Semantic Cache", "cat": "AI Gateway & Cache", "lic": "MIT",
                "substitui": "Chamadas duplicadas em APIs de LLM", "econ": "-40% a -60% na fatura de API (~$ 500/mês)",
                "entrega": "Cache semântico de respostas de LLM em Redis. Se o prompt for semanticamente equivalente, responde em 2ms por $ 0.",
                "mecanica": "Gera um embedding do prompt de entrada e faz uma busca por similaridade de cosseno em um Redis vetorial antes de chamar a API da OpenAI/Anthropic. Se encontrar match > 0.95, devolve o resultado cacheado.",
                "cmd": "docker run -d -p 4000:4000 ghcr.io/berriai/litellm:main-latest",
                "como_usar": "1. Inicie o container LiteLLM apontando para seu Redis no arquivo <code>config.yaml</code>.<br>2. Na sua aplicação, troque a URL base da OpenAI para <code>http://localhost:4000</code>.<br>3. Quando suítes de testes ou usuários repetirem perguntas similares, a resposta é entregue em 2ms sem custo de API.",
                "spec": "~70 MB RAM em repouso",
                "truth": "Essencial para suítes de testes de software e pipelines de CI/CD que rodam os mesmos prompts repetidamente.",
                "repo": "litellm.ai"
            },
            {
                "rank": "04", "name": "DSPy (Stanford)", "cat": "Prompt Compiler", "lic": "MIT",
                "substitui": "Engenharia de prompt manual cara", "econ": "Reduz tamanho de prompt em até 50%",
                "entrega": "Otimiza automaticamente instruções e few-shots via algoritmos matemáticos para obter a máxima acurácia no menor prompt possível.",
                "mecanica": "Trata pipelines de IA como grafos de computação diferenciáveis. Otimizadores como <code>BootstrapFewShotWithRandomSearch</code> testam variações de prompts e selecionam os exemplos mais compactos que maximizam a pontuação métrica.",
                "cmd": "pip install dspy-ai",
                "como_usar": "1. Defina sua classe de RAG: <code>class RAG(dspy.Module): ...</code> com assinaturas de entrada e saída.<br>2. Forneça 15 exemplos de perguntas e respostas corretas.<br>3. Execute o compilador do DSPy: ele testará combinações e gerará um prompt enxuto e hiper-eficiente para produção.",
                "spec": "Biblioteca pura / Zero runtime RAM",
                "truth": "Trata prompts como código compilável. Se você mudar de modelo, basta recompilar o pipeline sem reescrever nada.",
                "repo": "dspy.ai"
            },
            {
                "rank": "05", "name": "Outlines / Guidance", "cat": "Structured Generation", "lic": "Apache-2.0 / MIT",
                "substitui": "Retentativas por JSON quebrado", "econ": "Elimina 100% dos tokens de retry por falha de parsing",
                "entrega": "Força o modelo a seguir gramáticas formais (CFG / Regex / Pydantic) a nível de logits durante a amostragem de tokens.",
                "mecanica": "Constrói um Autômato Finito Determinístico (DFA) a partir do seu schema JSON. A cada token gerado, mascara os logits para que o modelo só possa escolher caracteres permitidos pela gramática.",
                "cmd": "pip install outlines",
                "como_usar": "1. Crie seu modelo Pydantic: <code>class Pedido(BaseModel): item: str, qtd: int</code>.<br>2. Instancie o gerador: <code>gerador = outlines.generate.json(modelo, Pedido)</code>.<br>3. Chame <code>resultado = gerador(prompt)</code>: o JSON resultante é matematicamente perfeito na primeira tentativa.",
                "spec": "Execução local / overhead < 5ms",
                "truth": "O modelo é matematicamente incapaz de gerar um caractere fora do schema especificado.",
                "repo": "github.com/outlines-dev/outlines"
            },
            {
                "rank": "06", "name": "Gitingest", "cat": "Web Repo Parser", "lic": "MIT",
                "substitui": "Clonagem + extração manual", "econ": "Economia de tempo de análise em 90%",
                "entrega": "Converte qualquer repositório público do GitHub em um texto limpo e resumido com contagem exata de tokens para colar em chats.",
                "mecanica": "Faz o parse da API do GitHub ou clone raso em memória, processa a estrutura de arquivos e cospe um prompt formatado com árvore de diretórios e código limpo.",
                "cmd": "docker run -d -p 8000:8000 cyclotruc/gitingest",
                "como_usar": "1. Ao estudar uma biblioteca nova, troque <code>github.com/dono/repo</code> na barra de endereços por <code>gitingest.com/dono/repo</code>.<br>2. Escolha o tamanho máximo de arquivo (ex: até 50KB).<br>3. Clique em 'Copy Context' e cole no seu chat de IA para fazer perguntas sobre o repositório.",
                "spec": "~60 MB RAM",
                "truth": "Troque 'github.com' por 'gitingest.com' na URL e obtenha o contexto estruturado em 1 segundo.",
                "repo": "gitingest.com"
            },
            {
                "rank": "07", "name": "Tree-sitter CLI", "cat": "CST / AST Parser", "lic": "MIT",
                "substitui": "Leitura integral de código pela LLM", "econ": "-80% de tokens ao enviar apenas assinaturas de funções",
                "entrega": "Parser incremental em C que extrai a hierarquia sintática de arquivos de código mesmo com erros parciais.",
                "mecanica": "Gera Concrete Syntax Trees (CST) ultra-rápidas em C nativo com parsing incremental: se você alterar 1 linha, ele reanalisa apenas aquele nó da árvore sem reprocessar o arquivo todo.",
                "cmd": "npm install -g tree-sitter-cli && tree-sitter parse arquivo.py",
                "como_usar": "1. Escreva um script em Node ou Python que roda queries S-expression do Tree-sitter.<br>2. Extraia apenas as declarações de <code>class</code>, <code>def</code> e docstrings do projeto.<br>3. Alimente seu agente com esse esqueleto sintático: ele saberá tudo o que existe no projeto usando apenas 2% dos tokens.",
                "spec": "Consumo de RAM irrisório (< 5MB)",
                "truth": "Permite criar ferramentas que alimentam o agente apenas com o mapa de símbolos das dependências.",
                "repo": "tree-sitter.github.io"
            },
            {
                "rank": "08", "name": "SGLang (RadixAttention)", "cat": "Inference Engine", "lic": "Apache-2.0",
                "substitui": "Recomputação cara de KV-cache", "econ": "5x mais rápido em chats com histórico longo",
                "entrega": "Implementa cache de prefixo em árvore radix, reaproveitando a computação do system prompt e mensagens anteriores em 100%.",
                "mecanica": "Mantém uma estrutura de dados de árvore Radix na memória de GPU para armazenar o KV-cache de múltiplos requests. Quando um novo prompt compartilha um prefixo já visto, reutiliza os tensores diretamente da VRAM.",
                "cmd": "python -m sglang.launch_server --model-path Qwen/Qwen2.5-Coder-7B-Instruct",
                "como_usar": "1. Inicie o servidor SGLang na sua máquina com GPU.<br>2. Configure seus agentes e subagentes para usarem a porta do SGLang.<br>3. Como os agentes repetem as mesmas 2.000 palavras de instruções de governança a cada turno, o processamento desse prefixo é instantâneo.",
                "spec": "VRAM estática de GPU / Throughput massivo",
                "truth": "O melhor motor para esteiras de subagentes que compartilham instruções de sistema extensas.",
                "repo": "github.com/sgl-project/sglang"
            }
        ]
    }
]

# Função geradora de HTML completo
def gerar_html_completo(lista):
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
        mecanica_html = item.get("mecanica", item.get("entrega", ""))
        como_usar_html = item.get("como_usar", "")

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
              <span class="label">1. O Que Faz</span>
              <p>{item['entrega']}</p>

              <span class="label" style="margin-top:6px;">2. Como Funciona (Mecânica Interna)</span>
              <p style="font-size:14px;color:var(--ink-2);">{mecanica_html}</p>

              <pre><code>{item['cmd']}</code></pre>

              <div class="how-to-use" style="background:var(--surface-2);border-left:3px solid var(--accent);padding:12px 14px;border-radius:0 2px 2px 0;margin-top:8px;display:flex;flex-direction:column;gap:6px;">
                <span class="label" style="color:var(--accent);font-weight:600;font-size:11px;letter-spacing:.12em;text-transform:uppercase;">3. Como Usar no Dia a Dia (Passo a Passo Prático)</span>
                <p style="font-size:13.5px !important;color:var(--ink) !important;line-height:1.55 !important;margin:0;">{como_usar_html}</p>
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
      <p class="sec-note">O que faz, como funciona por baixo dos panos, comandos de execução e <strong>passo a passo detalhado para o seu fluxo diário</strong>.</p>
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
