# -*- coding: utf-8 -*-
"""
TEMPLATE CANÔNICO DA FÁBRICA UNIVERSAL: DOSSIÊ EXECUTIVO
Padrão obrigatório e imutável para todas as 49 listas de tecnologias open source.

ESTRUTURA CANÔNICA:
1. Header Executivo:
   - Breadcrumb com link rápido: [← Voltar ao Hub Central]
   - Badge de Camada: .layer-badge (ex: 'Camada 01', 'Camada 35')
   - H1 e .deck com text-align: justify; text-justify: inter-word;
   - Hero Stats Bar: 4 métricas executivas em tempo real
   - Quick Jump Anchors: [#tabela] e [#fichas]

2. Matriz Comparativa Fluida:
   - 100% de largura (sem scroll horizontal)
   - Quebras em 2 linhas para Economia e Categoria

3. Card Dossiê Executivo (div.entry):
   - .entry-rank: Número com fundo em destaque
   - .entry-body:
     - .entry-top: H3 (Nome · Subtítulo) + Badges (Senioridade, Substitui, Economia, Licença, Categoria)
     - .entry-section 1: O Que Faz & Como Funciona + Bloco de Código com botão Copiar
     - .entry-section 2: Análise Econômica & Substituição de Soluções Proprietárias (.econ-grid)
     - .entry-section 3: Requisitos de Infraestrutura, Ecossistema & Veredito (.infra-grid + botão GitHub)
     - .entry-section 4: Como Usar no Dia a Dia (.steps-grid com 3 mini-cards)
"""
import sys

def console_utf8():
    if sys.platform == "win32":
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")

console_utf8()

CARD_TEMPLATE = """
<div class="entry">
  <div class="entry-rank">{rank}</div>
  <div class="entry-body">
    
    <!-- CABEÇALHO & BADGES -->
    <div class="entry-top">
      <h3>{titulo} · {subtitulo}</h3>
      <span class="senior-badge {senior_cor}">👨‍💻 Nível: {senior_lbl}</span>
      <span class="killer-badge">Substitui: {substitui}</span>
      <span class="econ-badge">Economia: {economia}</span>
      <span class="lic-badge">{licenca}</span>
      <span class="kind">{categoria}</span>
    </div>

    <!-- SEÇÃO 1: O QUE FAZ & COMO FUNCIONA -->
    <div class="entry-section">
      <span class="label">1. O Que Faz &amp; Como Funciona</span>
      <p>{o_que_faz}</p>
      <p>{como_funciona}</p>
      <div class="code-box">
        <pre><code>{codigo}</code></pre>
        <button class="copy-btn" onclick="navigator.clipboard.writeText(this.previousElementSibling.textContent.trim());this.textContent='Copiado!';setTimeout(()=>this.textContent='Copiar',1500)">Copiar</button>
      </div>
    </div>

    <!-- SEÇÃO 2: ANÁLISE ECONÔMICA & SUBSTITUIÇÃO DE SAAS -->
    <div class="entry-section">
      <span class="label">2. Análise Econômica &amp; Substituição de Soluções Proprietárias</span>
      <div class="econ-grid">
        <div class="econ-card killer">
          <span class="econ-lbl">💸 Produtos Proprietários Substituídos</span>
          <div class="econ-val">{substitui}</div>
        </div>
        <div class="econ-card highlight">
          <span class="econ-lbl">💰 Economia Real Estimada no TCO</span>
          <div class="econ-val"><strong>{economia} · Redução drástica de custos recorrentes</strong></div>
        </div>
      </div>
    </div>

    <!-- SEÇÃO 3: REQUISITOS DE INFRAESTRUTURA & ECOSSISTEMA -->
    <div class="entry-section">
      <span class="label">3. Requisitos de Infraestrutura, Ecossistema &amp; Veredito</span>
      <div class="infra-grid">
        <div class="infra-card">
          <span class="infra-lbl">🖥️ Infraestrutura Recomendada</span>
          <div class="infra-val">{infraestrutura}</div>
        </div>
        <div class="infra-card">
          <span class="infra-lbl">🔗 Ecossistema &amp; Padrões</span>
          <p><code>{categoria}</code> · Padrões Abertos OSI</p>
        </div>
        <div class="infra-card verdict">
          <span class="infra-lbl">🏆 Veredito do Arquiteto</span>
          <p><strong>Por que adotar:</strong> {veredito}</p>
        </div>
      </div>
      <div style="margin-top:6px;">
        <a class="repo-btn" href="{repo_url}" target="_blank" rel="noopener">
          <svg viewBox="0 0 24 24"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/></svg>
          <span>Repositório Oficial &amp; Código-Fonte: {repo_txt} ↗</span>
        </a>
      </div>
    </div>

    <!-- SEÇÃO 4: COMO USAR NO DIA A DIA -->
    <div class="entry-section">
      <span class="label">4. Como Usar no Dia a Dia (Passo a Passo Prático)</span>
      <div class="steps-grid">
        <div class="step-card">
          <div class="step-head"><span class="step-badge">1</span> Configuração</div>
          <p>{passo_1}</p>
        </div>
        <div class="step-card">
          <div class="step-head"><span class="step-badge">2</span> Operação</div>
          <p>{passo_2}</p>
        </div>
        <div class="step-card">
          <div class="step-head"><span class="step-badge">3</span> Resultado</div>
          <p>{passo_3}</p>
        </div>
      </div>
    </div>

  </div>
</div>
"""
