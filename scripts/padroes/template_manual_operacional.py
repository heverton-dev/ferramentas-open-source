# -*- coding: utf-8 -*-
"""
TEMPLATE CANÔNICO DA FÁBRICA UNIVERSAL: MANUAL OPERACIONAL DUPLO HIPERDIDÁTICO (PADRÃO DIAMANTE)
Projetado para leigos e iniciantes, com:
- Módulo 0: Nivelamento Conceitual com Analogias do Dia a Dia
- Passo a Passo da VPS à prova de erros: O que colar, O que acontece na tela e Como saber se deu certo
- Roteiro de Primeiro Voo: Onboarding prático de 3 minutos
- Dicionário de CLI, Rotas de API e Troubleshooting traduzido para linguagem simples
- Tabela de Referências Bibliográficas auditadas
"""

CSS_MANUAL_OPERACIONAL = """
  :root {
    --font-serif: "Liberation Serif", "Times New Roman", Times, serif;
    --font-sans: "Liberation Sans", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
    --mono: "JetBrains Mono", Menlo, Consolas, monospace;
    --paper: #F8FAFC;
    --surface: #FFFFFF;
    --ink: #0F172A;
    --ink-2: #334155;
    --muted: #64748B;
    --rule: #CBD5E1;
    --rule-soft: #E2E8F0;
    --accent: #0284C7;
    --accent-dark: #0369A1;
    --accent-soft: #E0F2FE;
    --green: #10B981;
    --green-dark: #065F46;
    --green-soft: #D1FAE5;
    --gold: #F59E0B;
    --gold-soft: #FEF3C7;
    --purple: #8B5CF6;
    --purple-soft: #EDE9FE;
    --code-bg: #0F172A;
  }

  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    font-family: var(--font-sans);
    background: var(--paper);
    color: var(--ink);
    line-height: 1.6;
    padding: 24px 16px 60px;
  }
  .container { max-width: 1060px; margin: 0 auto; }
  
  .header-card {
    background: var(--surface);
    border: 1px solid var(--rule);
    border-radius: 8px;
    padding: 32px;
    margin-bottom: 24px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
  }
  .breadcrumb { font-size: 13px; color: var(--muted); margin-bottom: 12px; }
  .breadcrumb a { color: var(--accent); text-decoration: none; font-weight: 600; }
  .badge-tag {
    display: inline-block;
    padding: 4px 10px;
    font-size: 12px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    border-radius: 4px;
    background: var(--accent-soft);
    color: var(--accent-dark);
    margin-bottom: 12px;
  }
  h1 { font-size: 28px; font-weight: 800; color: var(--ink); margin-bottom: 8px; line-height: 1.3; }
  .deck { font-size: 15px; color: var(--ink-2); margin-bottom: 24px; text-align: justify; }
  
  .hero-stats {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
    gap: 12px;
    background: var(--paper);
    padding: 16px;
    border-radius: 6px;
    border: 1px solid var(--rule-soft);
  }
  .stat-item { display: flex; flex-direction: column; }
  .stat-lbl { font-size: 11px; text-transform: uppercase; letter-spacing: 0.05em; color: var(--muted); font-weight: 700; }
  .stat-val { font-size: 14.5px; font-weight: 800; color: var(--ink); }

  .nav-anchors {
    display: flex;
    gap: 10px;
    margin: 20px 0;
    flex-wrap: wrap;
  }
  .nav-anchors a {
    padding: 8px 14px;
    background: var(--surface);
    border: 1px solid var(--rule);
    border-radius: 6px;
    color: var(--ink-2);
    text-decoration: none;
    font-size: 12.5px;
    font-weight: 600;
    transition: all 0.2s;
  }
  .nav-anchors a:hover {
    border-color: var(--accent);
    color: var(--accent-dark);
    background: var(--accent-soft);
  }

  .section-card {
    background: var(--surface);
    border: 1px solid var(--rule);
    border-radius: 8px;
    padding: 28px 32px;
    margin-bottom: 24px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
  }
  .section-header {
    border-bottom: 2px solid var(--rule-soft);
    padding-bottom: 12px;
    margin-bottom: 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .section-title { font-size: 20px; font-weight: 800; color: var(--ink); }

  /* CARDS DE NIVELAMENTO */
  .grid-conceitos {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 16px;
    margin: 16px 0;
  }
  .card-conceito {
    background: var(--paper);
    border: 1px solid var(--rule-soft);
    border-radius: 6px;
    padding: 16px;
    border-left: 4px solid var(--purple);
  }
  .conceito-termo { font-size: 15px; font-weight: 800; color: var(--ink); margin-bottom: 4px; }
  .conceito-analogia { font-size: 12.5px; font-weight: 700; color: #6D28D9; background: var(--purple-soft); padding: 3px 8px; border-radius: 4px; display: inline-block; margin-bottom: 8px; }
  .conceito-desc { font-size: 13px; color: var(--ink-2); line-height: 1.5; }

  /* PASSOS DE INSTALAÇÃO */
  .step-box {
    margin-bottom: 28px;
    padding-bottom: 24px;
    border-bottom: 1px dashed var(--rule);
  }
  .step-box:last-child { border-bottom: none; }
  .step-top {
    display: flex;
    align-items: baseline;
    gap: 8px;
    margin-bottom: 8px;
    flex-wrap: wrap;
  }
  .step-num {
    background: var(--accent);
    color: #FFF;
    font-size: 12px;
    font-weight: 800;
    padding: 2px 8px;
    border-radius: 4px;
  }
  .step-heading { font-size: 17px; font-weight: 800; color: var(--ink); }
  .analogia-box {
    background: #F0FDF4;
    border-left: 4px solid var(--green);
    padding: 8px 12px;
    border-radius: 0 4px 4px 0;
    margin: 8px 0;
    font-size: 13px;
    color: var(--green-dark);
  }
  .feedback-box {
    background: #FFFBEB;
    border: 1px solid #FDE68A;
    padding: 8px 12px;
    border-radius: 4px;
    margin: 8px 0;
    font-size: 12.5px;
    color: #92400E;
  }
  .validacao-box {
    background: #EFF6FF;
    border: 1px solid #BFDBFE;
    padding: 8px 12px;
    border-radius: 4px;
    margin: 8px 0;
    font-size: 12.5px;
    color: #1E40AF;
  }

  .code-box {
    position: relative;
    background: var(--code-bg);
    border-radius: 6px;
    margin: 10px 0;
    overflow: hidden;
  }
  .code-box pre {
    padding: 16px;
    overflow-x: auto;
    font-family: var(--mono);
    font-size: 13px;
    color: #F8FAFC;
    line-height: 1.5;
  }
  .btn-copy {
    position: absolute;
    top: 8px;
    right: 8px;
    padding: 4px 10px;
    font-size: 11px;
    font-weight: 600;
    background: rgba(255,255,255,0.15);
    color: #FFF;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    transition: background 0.2s;
  }
  .btn-copy:hover { background: rgba(255,255,255,0.3); }

  .cite-badge {
    display: inline-block;
    font-size: 10px;
    font-weight: 700;
    padding: 1px 6px;
    border-radius: 3px;
    background: var(--gold-soft);
    color: #B45309;
    vertical-align: super;
    margin-left: 4px;
    text-decoration: none;
  }

  table.data-table {
    width: 100%;
    border-collapse: collapse;
    margin: 16px 0;
    font-size: 13px;
  }
  table.data-table th {
    background: var(--paper);
    padding: 10px 12px;
    text-align: left;
    font-weight: 700;
    color: var(--ink-2);
    border-bottom: 2px solid var(--rule);
  }
  table.data-table td {
    padding: 10px 12px;
    border-bottom: 1px solid var(--rule-soft);
    color: var(--ink-2);
  }
  table.data-table tr:hover td { background: rgba(2, 132, 199, 0.02); }

  .trouble-card {
    background: #FFFBEB;
    border-left: 4px solid var(--gold);
    padding: 12px 16px;
    margin-bottom: 12px;
    border-radius: 0 4px 4px 0;
  }
  .trouble-symptom { font-weight: 700; color: #92400E; font-size: 13.5px; }
  .trouble-cause { font-size: 13px; color: #78350F; margin: 4px 0; }
  .trouble-fix { font-family: var(--mono); font-size: 12px; background: #FEF3C7; padding: 4px 8px; border-radius: 4px; display: inline-block; }
"""

JS_MANUAL_OPERACIONAL = """
<script>
function copyCode(btn) {
  const pre = btn.parentElement.querySelector('pre');
  if (!pre) return;
  navigator.clipboard.writeText(pre.innerText).then(() => {
    const original = btn.innerText;
    btn.innerText = 'Copiado!';
    setTimeout(() => { btn.innerText = original; }, 2000);
  });
}
</script>
"""

def renderizar_manual_html(dados: dict) -> str:
    vps = dados["vps_recomendada"]

    # Módulo 0: Nivelamento Conceitual
    nivelamento_html = []
    for n in dados.get("nivelamento_conceitual", []):
        nivelamento_html.append(f"""
        <div class="card-conceito">
          <div class="conceito-termo">💡 {n['termo']}</div>
          <div class="conceito-analogia">Analogia: {n['analogia_cotidiana']}</div>
          <p class="conceito-desc">{n['explicacao_simples']}</p>
        </div>
        """)

    # Passos da VPS
    passos_html = []
    for p in dados["instalacao_producao"]["passos"]:
        analogia = f"<div class=\"analogia-box\">💡 <strong>Entenda com uma analogia:</strong> {p['analogia']}</div>" if p.get("analogia") else ""
        tela = f"<div class=\"feedback-box\">🖥️ <strong>O que você verá na tela:</strong> {p['o_que_acontece_na_tela']}</div>" if p.get("o_que_acontece_na_tela") else ""
        ok = f"<div class=\"validacao-box\">✅ <strong>Como saber se deu certo:</strong> {p['como_saber_se_deu_certo']}</div>" if p.get("como_saber_se_deu_certo") else ""

        passos_html.append(f"""
        <div class="step-box">
          <div class="step-top">
            <span class="step-num">Passo {p['numero']}</span>
            <span class="step-heading">{p['titulo']}</span>
            <a href="#ref-{p['fonte_id']}" class="cite-badge">[{p['fonte_id']}]</a>
          </div>
          <p style="font-size:14px; color:var(--ink-2); margin-bottom:8px;">{p['descricao']}</p>
          {analogia}
          <div class="code-box">
            <button class="btn-copy" onclick="copyCode(this)">Copiar Comando</button>
            <pre><code>{p['comandos']}</code></pre>
          </div>
          {tela}
          {ok}
        </div>
        """)

    # Configs
    configs_html = []
    for c in dados["instalacao_producao"]["arquivos_configuracao"]:
        configs_html.append(f"""
        <div style="margin-top: 16px;">
          <strong style="font-size: 13px; color: var(--ink); font-family: var(--mono);">{c['caminho']}</strong>
          <p style="font-size: 13px; color: var(--muted); margin-bottom: 6px;">{c['explicacao']}</p>
          <div class="code-box">
            <button class="btn-copy" onclick="copyCode(this)">Copiar Arquivo</button>
            <pre><code>{c['conteudo']}</code></pre>
          </div>
        </div>
        """)

    # Primeiro Voo
    primeiro_voo_html = []
    for pv in dados.get("manual_uso_exaustivo", {}).get("roteiro_primeiro_voo", []):
        primeiro_voo_html.append(f"""
        <div style="padding: 12px; background: var(--paper); border: 1px solid var(--rule-soft); border-radius: 6px; margin-bottom: 10px;">
          <strong style="color: var(--accent-dark);">{pv['passo']}:</strong> {pv['acao']}
          <div style="margin-top: 4px; font-size: 12.5px; color: var(--green-dark);">🎯 <strong>Resultado Esperado:</strong> {pv['resultado_esperado']}</div>
        </div>
        """)

    # CLI
    cli_rows = []
    for c in dados["manual_uso_exaustivo"]["comandos_cli"]:
        cli_rows.append(f"""
        <tr>
          <td><code style="font-weight:700; color:var(--accent-dark);">{c['comando']}</code></td>
          <td>{c['descricao']}</td>
          <td><code>{c['exemplo']}</code></td>
          <td><a href="#ref-{c['fonte_id']}" class="cite-badge">[{c['fonte_id']}]</a></td>
        </tr>
        """)

    # API
    api_rows = []
    for a in dados["manual_uso_exaustivo"]["rotas_api"]:
        api_rows.append(f"""
        <tr>
          <td><span class="step-num" style="background:#059669;">{a['metodo']}</span></td>
          <td><code>{a['rota']}</code></td>
          <td>{a['descricao']}</td>
          <td><pre style="font-size:11px; margin:0;">{a['payload_exemplo']}</pre></td>
          <td><a href="#ref-{a['fonte_id']}" class="cite-badge">[{a['fonte_id']}]</a></td>
        </tr>
        """)

    # Troubleshooting
    trouble_html = []
    for t in dados["manual_uso_exaustivo"]["troubleshooting"]:
        trouble_html.append(f"""
        <div class="trouble-card">
          <div class="trouble-symptom">⚠️ Sintoma: {t['sintoma']}</div>
          <div class="trouble-cause">Causa Provável: {t['causa_provavel']}</div>
          <div>Solução Prática: <code class="trouble-fix">{t['solucao_comando']}</code></div>
        </div>
        """)

    # Bibliografia
    refs_rows = []
    for r in dados["referencias_bibliograficas"]:
        refs_rows.append(f"""
        <tr id="ref-{r['id']}">
          <td><strong style="color:var(--accent);">{r['id']}</strong></td>
          <td><span class="badge-tag" style="margin:0; font-size:10px;">{r['categoria']}</span></td>
          <td><strong>{r['titulo']}</strong></td>
          <td>{r['autor_ou_canal']}</td>
          <td><a href="{r['url']}" target="_blank" rel="noopener noreferrer" style="color:var(--accent); text-decoration:none; font-weight:600;">Acessar Fonte Original ↗</a></td>
        </tr>
        """)

    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Manual Operacional: {dados['produto_foco']} · Deploy VPS &amp; Uso Exaustivo</title>
  <style>
{CSS_MANUAL_OPERACIONAL}
  </style>
</head>
<body>
<div class="container">

  <!-- CABEÇALHO -->
  <div class="header-card">
    <div class="breadcrumb">
      <a href="../listas/vert-{dados['saas_origem']}.html">← Voltar ao Dossiê Vertical {dados['saas_origem'].title()}</a>
    </div>
    <span class="badge-tag">Padrão Diamante · Guia de Engenharia em Produção</span>
    <h1>Manual Operacional Completo: {dados['produto_foco']}</h1>
    <p class="deck">
      Guia técnico exaustivo e hiperdidático para colocar a ferramenta em produção na VPS recomendada e dominar 100% de suas funções, mesmo que você nunca tenha programado antes. Totalmente fundamentado em fontes oficiais auditadas.
    </p>

    <!-- HERO STATS DA VPS -->
    <div class="hero-stats">
      <div class="stat-item">
        <span class="stat-lbl">VPS Recomendada</span>
        <span class="stat-val">{vps['provedor_modelo']}</span>
      </div>
      <div class="stat-item">
        <span class="stat-lbl">Hardware Mínimo</span>
        <span class="stat-val">{vps['vcpu']} · {vps['ram']}</span>
      </div>
      <div class="stat-item">
        <span class="stat-lbl">Armazenamento &amp; SO</span>
        <span class="stat-val">{vps['armazenamento']} · {vps['so_recomendado']}</span>
      </div>
      <div class="stat-item">
        <span class="stat-lbl">Custo Mensal Estimado</span>
        <span class="stat-val" style="color:var(--accent-dark);">{vps['custo_mensal_estimado']}</span>
      </div>
      <div class="stat-item">
        <span class="stat-lbl">Licença de Uso</span>
        <span class="stat-val" style="color:var(--green);">{dados['licenca_osi']} (Livre &amp; Comercial)</span>
      </div>
    </div>

    <!-- NAVEGAÇÃO RÁPIDA -->
    <div class="nav-anchors">
      <a href="#nivelamento">💡 Módulo 0: Nivelamento para Iniciantes</a>
      <a href="#instalacao">📦 Parte I: Instalação Passo a Passo</a>
      <a href="#configuracao">⚙️ Arquivos de Configuração</a>
      <a href="#primeiro-voo">✈️ Roteiro de Primeiro Voo</a>
      <a href="#manual-cli">⌨️ Dicionário de Comandos</a>
      <a href="#manual-api">🌐 Endpoints de API</a>
      <a href="#troubleshooting">🛠️ Socorro! Não Funcionou</a>
      <a href="#bibliografia">📚 Referências Bibliográficas</a>
    </div>
  </div>

  <!-- MÓDULO 0: NIVELAMENTO CONCEITUAL -->
  <div class="section-card" id="nivelamento">
    <div class="section-header">
      <h2 class="section-title">Módulo 0: Nivelamento Conceitual (O que você precisa saber antes de começar)</h2>
      <span class="badge-tag" style="background:var(--purple-soft); color:#6D28D9;">Zero Programação</span>
    </div>
    <p style="font-size:14px; color:var(--ink-2); margin-bottom:16px;">
      Você não precisa ser engenheiro de software para entender como o sistema funciona. Abaixo explicamos os 5 conceitos-chave usando analogias do cotidiano:
    </p>
    <div class="grid-conceitos">
      {''.join(nivelamento_html)}
    </div>
  </div>

  <!-- SEÇÃO 1: INSTALAÇÃO EM PRODUÇÃO -->
  <div class="section-card" id="instalacao">
    <div class="section-header">
      <h2 class="section-title">Parte I: Instalação em Produção na VPS (Passo a Passo Guiado à Prova de Erros)</h2>
      <span class="badge-tag">Tempo ~{dados.get('tempo_estimado_setup', '15 min')}</span>
    </div>
    {''.join(passos_html)}
  </div>

  <!-- SEÇÃO 2: ARQUIVOS DE CONFIGURAÇÃO -->
  <div class="section-card" id="configuracao">
    <div class="section-header">
      <h2 class="section-title">Arquivos Canônicos de Configuração (Produção)</h2>
    </div>
    {''.join(configs_html)}
  </div>

  <!-- SEÇÃO 3: ROTEIRO DE PRIMEIRO VOO -->
  <div class="section-card" id="primeiro-voo">
    <div class="section-header">
      <h2 class="section-title">Parte II: Roteiro de Primeiro Voo (Sua Primeira Reunião em 3 Minutos)</h2>
      <span class="badge-tag" style="background:var(--green-soft); color:var(--green-dark);">Prática Imediata</span>
    </div>
    <p style="font-size:14px; color:var(--ink-2); margin-bottom:14px;">
      Após concluir a instalação, siga estes passos simples para testar a gravação e a busca semântica:
    </p>
    {''.join(primeiro_voo_html)}
  </div>

  <!-- SEÇÃO 4: MANUAL DE USO CLI -->
  <div class="section-card" id="manual-cli">
    <div class="section-header">
      <h2 class="section-title">Dicionário Completo de Comandos (CLI)</h2>
    </div>
    <table class="data-table">
      <thead>
        <tr>
          <th>Comando / Opção</th>
          <th>O que faz (em português claro)</th>
          <th>Exemplo de Execução</th>
          <th>Fonte</th>
        </tr>
      </thead>
      <tbody>
        {''.join(cli_rows)}
      </tbody>
    </table>
  </div>

  <!-- SEÇÃO 5: REFERÊNCIA DE API REST -->
  <div class="section-card" id="manual-api">
    <div class="section-header">
      <h2 class="section-title">Endpoints de API REST &amp; Conexão com Agentes (MCP)</h2>
    </div>
    <table class="data-table">
      <thead>
        <tr>
          <th>Método</th>
          <th>Rota</th>
          <th>Finalidade</th>
          <th>Payload / Resposta</th>
          <th>Fonte</th>
        </tr>
      </thead>
      <tbody>
        {''.join(api_rows)}
      </tbody>
    </table>
  </div>

  <!-- SEÇÃO 6: TROUBLESHOOTING -->
  <div class="section-card" id="troubleshooting">
    <div class="section-header">
      <h2 class="section-title">Socorro! O que fazer se algo não funcionar (Troubleshooting para Leigos)</h2>
    </div>
    {''.join(trouble_html)}
  </div>

  <!-- SEÇÃO 7: REFERÊNCIAS BIBLIOGRÁFICAS -->
  <div class="section-card" id="bibliografia">
    <div class="section-header">
      <h2 class="section-title">Parte III: Fontes Citadas &amp; Referência Bibliográfica Auditada</h2>
      <span class="badge-tag" style="background:var(--green-soft); color:var(--green);">100% Verificadas</span>
    </div>
    <table class="data-table">
      <thead>
        <tr>
          <th>ID</th>
          <th>Categoria</th>
          <th>Título da Obra / Documento</th>
          <th>Autor / Mantenedor</th>
          <th>Link Oficial</th>
        </tr>
      </thead>
      <tbody>
        {''.join(refs_rows)}
      </tbody>
    </table>
  </div>

</div>
{JS_MANUAL_OPERACIONAL}
</body>
</html>
"""
