# -*- coding: utf-8 -*-
"""
COMPILADOR TRIPARTITE DE MACRO-ECOSSISTEMAS SAAS (FLUXO 4 - PADRÃO DIAMANTE R5-E & SUÍTE SOBERANA)
Gera o LIVRO-TEXTO COMPLETO e a SUÍTE MODULAR DE GUIAS ESPECIALIZADOS.
Estrutura enciclopédica com 11 Capítulos de Alta Densidade Técnica:
1. Prefácio Executivo & Manifesto da Soberania Tecnológica
2. Engenharia Financeira, TCO Global & Calculadora Interativa de Payback
3. Matriz Estratégica do Quinteto Soberano por Grupo Funcional
4. Arsenal Tecnológico · Pilar 01 (Marketing, Nutrição & Automação)
5. Arsenal Tecnológico · Pilar 02 (Pipeline Comercial & CRM de Vendas)
6. Arsenal Tecnológico · Pilar 03 (Atendimento Omnichannel & WhatsApp)
7. Camada de Cola, SSO Federado & Blueprints n8n em JSON
8. Manual de Engenharia de Infraestrutura & Deploy All-in-One (Docker Compose)
9. Protocolos de Modularidade, Expansão & Hot-Swap (Princípio do Lego)
10. Roteiro Prático de Migração de Dados Históricos (De-SaaS para Soberano)
11. Governança, Backup 3-2-1, LGPD, Cronograma de 30 Dias & Monitoramento
"""
import sys
import json
import argparse
import subprocess
import datetime
from pathlib import Path

def console_utf8():
    if sys.platform == "win32":
        try:
            sys.stdout.reconfigure(encoding="utf-8")
            sys.stderr.reconfigure(encoding="utf-8")
        except Exception:
            pass

console_utf8()

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR / "scripts"))

from estado_esteira import registrar_ecossistema

CSS_CANONICO_DIAMANTE = """
  :root {
    --font-serif: "Liberation Serif", "Linux Libertine O", "Times New Roman", Times, serif;
    --font-sans: "Liberation Sans", "SF Pro Display", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
    --mono: "JetBrains Mono", "SF Mono", Menlo, Consolas, monospace;
    --paper: #F6F4EF;
    --surface: #FFFFFF;
    --surface-2: #FBF9F4;
    --surface-dark: #0A0F1D;
    --ink: #1B1E23;
    --ink-2: #383D45;
    --muted: #666E7A;
    --rule: #D8D2C4;
    --rule-soft: #EAE5D9;
    --accent: #00875A;
    --accent-dark: #57D9A3;
    --accent-soft: #E3FCEF;
    --accent-soft-dark: #162B22;
    --green: #00875A;
    --green-soft: #E3FCEF;
    --gold: #FFAB00;
    --gold-soft: #FFF0B3;
    --flag: #DE350B;
    --flag-soft: #FFEBE6;
    --shadow: 0 1px 3px rgba(0,0,0,0.04);
  }

  @media (prefers-color-scheme: dark) {
    :root {
      --paper: #0E121B;
      --surface: #141924;
      --surface-2: #1A2130;
      --ink: #E6E8ED;
      --ink-2: #B0B5C0;
      --muted: #7E8695;
      --rule: #262F40;
      --rule-soft: #1E2533;
      --accent: var(--accent-dark);
      --accent-soft: var(--accent-soft-dark);
      --green: #57D9A3;
      --green-soft: #162B22;
      --gold: #FFC400;
      --gold-soft: #332600;
      --flag: #FF7452;
      --flag-soft: #361B15;
      --shadow: 0 1px 3px rgba(0,0,0,0.25);
    }
  }

  *, *::before, *::after { box-sizing: border-box; }
  html { font-size: 16px; scroll-behavior: smooth; }

  * {
    scrollbar-width: thin;
    scrollbar-color: var(--accent) transparent;
  }
  ::-webkit-scrollbar {
    width: 4px;
    height: 4px;
  }
  ::-webkit-scrollbar-track {
    background: transparent;
  }
  ::-webkit-scrollbar-thumb {
    background: var(--accent);
    border-radius: 2px;
  }

  body {
    margin: 0;
    padding: 40px 20px;
    background: var(--paper);
    color: var(--ink);
    font-family: var(--font-sans);
    line-height: 1.6;
    -webkit-font-smoothing: antialiased;
  }

  .wrap {
    max-width: 1180px;
    margin: 0 auto;
    background: var(--surface);
    border: 1px solid var(--rule);
    border-radius: 4px;
    padding: 48px;
    box-shadow: var(--shadow);
  }

  /* CAPA DO LIVRO MESTRE */
  .book-cover {
    background: linear-gradient(135deg, var(--surface) 0%, var(--surface-2) 100%);
    border: 2px solid var(--ink);
    border-radius: 4px;
    padding: 48px 36px;
    margin-bottom: 40px;
    position: relative;
    box-shadow: 0 8px 24px rgba(0,0,0,0.06);
  }
  .book-tagline { font-family: var(--mono); font-size: 12px; letter-spacing: .15em; text-transform: uppercase; color: var(--accent); font-weight: 700; margin-bottom: 12px; }
  .book-title { font-family: var(--font-serif); font-size: 42px; line-height: 1.1; margin: 0 0 12px; color: var(--ink); font-weight: 700; letter-spacing: -.02em; }
  .book-subtitle { font-size: 18px; color: var(--ink-2); line-height: 1.5; margin-bottom: 24px; max-width: 90%; }
  .book-meta-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 16px; border-top: 1px solid var(--rule); padding-top: 20px; font-family: var(--mono); font-size: 11.5px; color: var(--muted); }
  .book-meta-item strong { display: block; color: var(--ink); font-size: 13px; margin-top: 2px; }

  /* SUMÁRIO DO LIVRO */
  .toc-box {
    background: var(--surface-2);
    border: 1px solid var(--rule);
    border-radius: 3px;
    padding: 24px;
    margin: 28px 0 40px;
  }
  .toc-box h3 { font-family: var(--font-serif); font-size: 22px; margin: 0 0 16px; color: var(--ink); border-bottom: 1px solid var(--rule-soft); padding-bottom: 8px; }
  .toc-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 12px 24px; }
  .toc-item { font-size: 13.5px; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px dashed var(--rule-soft); padding: 4px 0; }
  .toc-item a { color: var(--ink); text-decoration: none; font-weight: 500; }
  .toc-item a:hover { color: var(--accent); }
  .toc-item span { font-family: var(--mono); font-size: 11px; color: var(--muted); }

  .stats-bar {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
    gap: 16px;
    margin: 24px 0;
  }

  .stat-card {
    background: var(--surface-2);
    border: 1px solid var(--rule-soft);
    border-radius: 2px;
    padding: 12px 14px;
  }

  .stat-lbl {
    font-family: var(--mono);
    font-size: 10px;
    text-transform: uppercase;
    letter-spacing: .08em;
    color: var(--muted);
    margin-bottom: 4px;
  }

  .stat-val {
    font-family: var(--mono);
    font-size: 19px;
    font-weight: 700;
    color: var(--ink);
  }

  .stat-val.highlight { color: var(--green); }
  .stat-val.alert { color: var(--flag); }

  .racional-box {
    background: var(--surface-2);
    border-left: 4px solid var(--accent);
    padding: 16px 20px;
    margin: 24px 0;
    font-size: 14px;
    color: var(--ink-2);
    border-radius: 0 3px 3px 0;
    line-height: 1.6;
  }

  .sec-head {
    margin: 54px 0 24px;
    padding-bottom: 14px;
    border-bottom: 2px solid var(--ink);
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    flex-wrap: wrap;
    gap: 12px;
  }

  .sec-info { flex: 1; }
  .sec-num { font-family: var(--mono); font-size: 11.5px; text-transform: uppercase; color: var(--accent); font-weight: 700; letter-spacing: .1em; }
  .sec-head h2 { font-family: var(--font-serif); font-size: 28px; margin: 4px 0 0 0; color: var(--ink); font-weight: 700; }
  .sec-note { font-size: 14px; color: var(--muted); margin-top: 4px; }
  .pilar-subtotal-badge { font-family: var(--mono); font-size: 11px; font-weight: 700; padding: 4px 10px; background: var(--green-soft); color: var(--green); border-radius: 2px; border: 1px solid var(--green); }

  /* TABELA MATRIX */
  .tablewrap { width: 100%; overflow-x: auto; margin: 20px 0 32px 0; border: 1px solid var(--rule); border-radius: 2px; }
  table { width: 100%; border-collapse: collapse; font-size: 13.5px; }
  thead { background: var(--surface-2); border-bottom: 1px solid var(--rule); }
  th { text-align: left; padding: 10px 14px; font-family: var(--mono); font-size: 11px; text-transform: uppercase; letter-spacing: .06em; color: var(--muted); font-weight: 600; white-space: nowrap; }
  td { padding: 12px 14px; border-bottom: 1px solid var(--rule-soft); vertical-align: middle; }
  tr:last-child td { border-bottom: none; }
  tr:hover td { background: var(--surface-2); }
  td.rank { font-family: var(--mono); font-weight: 700; color: var(--muted); font-size: 12px; }
  td.saas { color: var(--flag); font-weight: 600; }
  td.econ { font-family: var(--mono); font-weight: 700; color: var(--green); }
  td.killer { color: var(--flag); font-weight: 700; font-family: var(--mono); }

  /* CARDS DE FERRAMENTAS */
  .ledger { display: flex; flex-direction: column; gap: 24px; margin-top: 24px; }
  .entry { display: grid; grid-template-columns: 48px 1fr; border: 1px solid var(--rule); border-radius: 2px; background: var(--surface); padding: 24px; box-shadow: var(--shadow); }
  .entry-rank { font-family: var(--mono); font-size: 20px; font-weight: 700; color: var(--muted); padding-top: 2px; }
  .entry-body { display: flex; flex-direction: column; gap: 16px; }
  .entry-top { display: flex; flex-wrap: wrap; align-items: center; gap: 8px 10px; }
  .entry-top h3 { width: 100%; margin: 0 0 4px 0; font-family: var(--font-serif); font-weight: 600; font-size: 24px; line-height: 1.15; letter-spacing: -.01em; color: var(--ink); }

  .persona-badge { font-family: var(--mono); font-size: 10px; letter-spacing: .08em; text-transform: uppercase; padding: 3px 8px; border-radius: 2px; font-weight: 700; background: var(--accent-soft); color: var(--accent); border: 1px solid color-mix(in srgb, var(--accent) 35%, transparent); white-space: nowrap; }
  .pilar-badge { font-family: var(--mono); font-size: 10px; letter-spacing: .08em; text-transform: uppercase; padding: 3px 8px; border-radius: 2px; background: var(--gold-soft); color: #8A6100; border: 1px solid color-mix(in srgb, var(--gold) 35%, transparent); font-weight: 700; white-space: nowrap; }
  .killer-badge { font-family: var(--mono); font-size: 10px; letter-spacing: .08em; text-transform: uppercase; padding: 3px 8px; border-radius: 2px; background: var(--flag-soft); color: var(--flag); border: 1px solid color-mix(in srgb, var(--flag) 35%, transparent); font-weight: 600; white-space: nowrap; }
  .econ-badge { font-family: var(--mono); font-size: 10px; letter-spacing: .08em; text-transform: uppercase; padding: 3px 8px; border-radius: 2px; background: var(--green-soft); color: var(--green); border: 1px solid color-mix(in srgb, var(--green) 35%, transparent); font-weight: 600; white-space: nowrap; }
  .lic-badge { font-family: var(--mono); font-size: 10px; letter-spacing: .08em; text-transform: uppercase; padding: 3px 8px; border-radius: 2px; background: var(--surface-2); color: var(--muted); border: 1px solid var(--rule-soft); font-weight: 600; white-space: nowrap; }

  .entry-section { display: flex; flex-direction: column; gap: 6px; width: 100%; padding-top: 12px; border-top: 1px dashed var(--rule-soft); }
  .entry-section .label { font-family: var(--mono); font-size: 11px; letter-spacing: .1em; text-transform: uppercase; color: var(--accent); font-weight: 600; }
  .entry-section p { margin: 0; font-size: 14px; line-height: 1.55; color: var(--ink-2); }

  .code-box { background: var(--surface-2); border: 1px solid var(--rule); border-radius: 2px; padding: 12px; font-family: var(--mono); font-size: 12px; overflow-x: auto; color: var(--ink); position: relative; }
  .code-box pre { margin: 0; font-family: inherit; }

  .econ-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 10px; margin-top: 4px; }
  .econ-card { background: var(--surface-2); border: 1px solid var(--rule-soft); border-radius: 2px; padding: 10px 12px; display: flex; flex-direction: column; gap: 2px; }
  .econ-card.killer { border-left: 3px solid var(--flag); }
  .econ-card.savings { border-left: 3px solid var(--green); }
  .econ-lbl { font-family: var(--mono); font-size: 10px; text-transform: uppercase; letter-spacing: .08em; color: var(--muted); font-weight: 600; }
  .econ-val { font-family: var(--mono); font-size: 13.5px; font-weight: 700; color: var(--ink); }

  .infra-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 10px; margin-top: 4px; }
  .infra-card { background: var(--surface-2); border: 1px solid var(--rule-soft); border-radius: 2px; padding: 10px 12px; display: flex; flex-direction: column; gap: 2px; }
  .infra-card.verdict { border-left: 3px solid var(--accent); grid-column: 1 / -1; }
  .infra-lbl { font-family: var(--mono); font-size: 10px; text-transform: uppercase; letter-spacing: .08em; color: var(--muted); font-weight: 600; }
  .infra-val { font-size: 13px; color: var(--ink-2); font-weight: 500; }

  .steps-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 10px; margin-top: 6px; }
  .step-card { background: var(--surface-2); border: 1px solid var(--rule-soft); border-radius: 2px; padding: 12px; display: flex; flex-direction: column; gap: 6px; }
  .step-head { display: flex; align-items: center; gap: 6px; font-family: var(--mono); font-size: 10.5px; font-weight: 700; color: var(--accent); text-transform: uppercase; }
  .step-badge { background: var(--accent); color: var(--paper); border-radius: 2px; padding: 1px 5px; font-size: 9.5px; font-weight: 700; }
  .step-card p { margin: 0; font-size: 13px; line-height: 1.4; color: var(--ink-2); }

  .ds-header { display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 8px; margin-bottom: 6px; }
  .ds-badges { display: flex; flex-wrap: wrap; gap: 6px; align-items: center; }
  .ds-badge { font-family: var(--mono); font-size: 10px; font-weight: 700; text-transform: uppercase; padding: 2px 7px; border-radius: 2px; letter-spacing: .06em; }
  .ds-badge.esforco-minimo { background: #E3FCEF; color: #00875A; border: 1px solid #ABF5D1; }
  .ds-badge.esforco-headless { background: #DEEBFF; color: #0747A6; border: 1px solid #B3D4FF; }
  .ds-badge.esforco-medio { background: #FFF0B3; color: #974F0C; border: 1px solid #FFE380; }
  .ds-badge.stack-ui { background: var(--surface-2); color: var(--ink-2); border: 1px solid var(--rule-soft); }

  .ds-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 10px; margin-top: 4px; }
  .ds-card { background: var(--surface-2); border: 1px solid var(--rule-soft); border-radius: 2px; padding: 10px 12px; display: flex; flex-direction: column; gap: 3px; }
  .ds-lbl { font-family: var(--mono); font-size: 10px; text-transform: uppercase; letter-spacing: .08em; color: var(--muted); font-weight: 600; }
  .ds-card p { margin: 0; font-size: 13px; line-height: 1.45; color: var(--ink-2); }

  .mcp-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 10px; margin-top: 4px; }
  .mcp-card { background: var(--surface-2); border: 1px solid var(--rule-soft); border-radius: 2px; padding: 10px 12px; display: flex; flex-direction: column; gap: 4px; }
  .mcp-top { display: flex; justify-content: space-between; align-items: center; gap: 6px; }
  .mcp-pill { font-family: var(--mono); font-size: 9.5px; font-weight: 700; text-transform: uppercase; padding: 1px 6px; border-radius: 2px; background: var(--accent-soft); color: var(--accent); }
  .mcp-name { font-family: var(--mono); font-size: 12px; font-weight: 700; color: var(--ink); }
  .mcp-card p { margin: 0; font-size: 12.5px; color: var(--ink-2); line-height: 1.4; }
  .mcp-cmd { font-family: var(--mono); font-size: 11px; background: var(--surface); padding: 3px 6px; border-radius: 2px; border: 1px solid var(--rule-soft); color: var(--ink); word-break: break-all; }

  .integration-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 12px; margin: 16px 0; }
  .integ-card { background: var(--surface); border: 1px solid var(--rule); border-left: 4px solid var(--accent); border-radius: 3px; padding: 16px; box-shadow: var(--shadow); }
  .integ-card h4 { font-family: var(--font-serif); font-size: 18px; margin: 0 0 8px; color: var(--ink); }
  .integ-card p { margin: 0; font-size: 13.5px; color: var(--ink-2); line-height: 1.5; }

  .tco-banner { background: var(--surface); border: 1px solid var(--green); border-radius: 3px; padding: 20px; margin: 20px 0; box-shadow: var(--shadow); display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 16px; }
  .tco-col .tco-lbl { font-family: var(--mono); font-size: 11px; color: var(--muted); text-transform: uppercase; font-weight: 600; margin-bottom: 4px; }
  .tco-col .tco-val { font-family: var(--mono); font-size: 18px; font-weight: 700; color: var(--ink); }
  .tco-col .tco-val.highlight { color: var(--green); }
  .tco-col .tco-val.killer { color: var(--flag); }

  /* CALCULADORA INTERATIVA TCO */
  .calc-box { background: var(--surface-2); border: 1px solid var(--rule); border-radius: 4px; padding: 24px; margin: 20px 0; box-shadow: var(--shadow); }
  .calc-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 20px; margin-bottom: 20px; }
  .calc-slider-group label { display: flex; justify-content: space-between; font-family: var(--mono); font-size: 12px; font-weight: 600; color: var(--ink); margin-bottom: 6px; }
  .calc-slider-group input[type=range] { width: 100%; accent-color: var(--accent); cursor: pointer; }
  .calc-results { background: var(--surface); border: 1px solid var(--green); border-radius: 3px; padding: 18px; display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; }

  /* BLUEPRINTS & TIMELINE */
  .blueprint-card { background: var(--surface); border: 1px solid var(--rule); border-radius: 3px; padding: 18px; margin-bottom: 16px; box-shadow: var(--shadow); }
  .timeline-card { background: var(--surface-2); border-left: 4px solid var(--accent); padding: 16px; margin-bottom: 12px; border-radius: 0 3px 3px 0; }
  .timeline-card h4 { margin: 0 0 6px; font-family: var(--font-serif); font-size: 17px; color: var(--ink); }
"""

JS_CANONICO_DIAMANTE = """
<script>
function filterTools(query) {
  const q = query.toLowerCase().trim();
  const entries = document.querySelectorAll('.entry');
  const rows = document.querySelectorAll('.tablewrap tbody tr');
  let visibleCount = 0;

  entries.forEach(entry => {
    const text = entry.innerText.toLowerCase();
    if (!q || text.includes(q)) {
      entry.style.display = 'grid';
      visibleCount++;
    } else {
      entry.style.display = 'none';
    }
  });

  rows.forEach(row => {
    const text = row.innerText.toLowerCase();
    if (!q || text.includes(q)) {
      row.style.display = '';
    } else {
      row.style.display = 'none';
    }
  });

  const countEl = document.getElementById('search-count');
  if (countEl) {
    countEl.innerText = `${visibleCount} ferramentas encontradas`;
  }
}

function updateTcoCalculator() {
  const leads = parseInt(document.getElementById('slider-leads').value, 10);
  const sellers = parseInt(document.getElementById('slider-sellers').value, 10);
  const agents = parseInt(document.getElementById('slider-agents').value, 10);

  document.getElementById('val-leads').innerText = leads.toLocaleString('pt-BR') + ' leads';
  document.getElementById('val-sellers').innerText = sellers + ' vendedores';
  document.getElementById('val-agents').innerText = agents + ' atendentes';

  // Cálculos SaaS estimados (RD Marketing escalonado + RD CRM por licença + RD Conversas por operador)
  const custoMkt = (leads <= 10000) ? 14400 : (leads <= 50000) ? 42000 : (leads <= 100000) ? 78000 : 130000;
  const custoCrm = sellers * 3600;
  const custoChat = agents * 3600;
  const saasTotal = custoMkt + custoCrm + custoChat;

  // Custo VPS Soberana (Cluster Unificado 8 vCPU / 16 GB RAM)
  const custoVps = 4200;
  const economiaLiquida = saasTotal - custoVps;
  const economiaPct = ((economiaLiquida / saasTotal) * 100).toFixed(1);

  document.getElementById('calc-saas-total').innerText = 'R$ ' + saasTotal.toLocaleString('pt-BR') + '/ano';
  document.getElementById('calc-vps-total').innerText = 'R$ ' + custoVps.toLocaleString('pt-BR') + '/ano';
  document.getElementById('calc-savings-total').innerText = 'R$ ' + economiaLiquida.toLocaleString('pt-BR') + '/ano (' + economiaPct + '%)';
}

document.addEventListener('DOMContentLoaded', () => {
  const searchInput = document.getElementById('busca-ferramentas');
  if (searchInput) {
    searchInput.addEventListener('input', (e) => filterTools(e.target.value));
    document.addEventListener('keydown', (e) => {
      if (e.key === '/' && document.activeElement !== searchInput) {
        e.preventDefault();
        searchInput.focus();
      }
    });
  }

  const sLeads = document.getElementById('slider-leads');
  const sSellers = document.getElementById('slider-sellers');
  const sAgents = document.getElementById('slider-agents');
  if (sLeads && sSellers && sAgents) {
    sLeads.addEventListener('input', updateTcoCalculator);
    sSellers.addEventListener('input', updateTcoCalculator);
    sAgents.addEventListener('input', updateTcoCalculator);
    updateTcoCalculator();
  }
});
</script>
"""

def simplificar_classificacao(classificacao: str) -> str:
    c = classificacao.lower()
    if "robusta" in c: return "Robusta"
    if "completa" in c: return "Completa"
    if "moderna" in c: return "Moderna"
    if "leve" in c: return "Leve"
    if "simples" in c: return "Simples"
    return classificacao

def gerar_markdown_ecossistema(dados: dict) -> str:
    titulo = dados.get("titulo", "Dossiê de Macro-Ecossistema Open Source")
    deck = dados.get("deck", "")
    saas = dados.get("saas_substituido", "")
    pilares = dados.get("pilares", [])
    integracao = dados.get("camada_integracao", {})
    deploy = dados.get("deploy_consolidado", {})
    guia = dados.get("guia_modularidade_e_expansao", {})
    econ = dados.get("analise_economica_global", {})
    stack_detalhe = deploy.get("composicao_stack_detalhada", [])

    linhas = [
        f"# LIVRO-TEXTO EXECUTIVO: {titulo.upper()}",
        f"",
        f"> **Macro-Ecossistema SaaS Alvo:** {saas}  ",
        f"> **Autoridade Emissora:** Fábrica Universal AIDD · Governança Aberta Multi-IDE  ",
        f"> **Padrão Normativo:** Diamante R5-E Tripartite | **Data de Publicação:** {datetime.date.today().strftime('%d/%m/%Y')}  ",
        f"> **Edição:** 1ª Edição Oficial — Desmantelamento Integral de Suítes Proprietárias",
        f"",
        f"---",
        f"",
        f"## SUMÁRIO GERAL DO LIVRO-TEXTO",
        f"",
        f"1. [Prefácio Executivo & Manifesto da Soberania Tecnológica](#prefacio-executivo--manifesto-da-soberania-tecnologica)",
        f"2. [Capítulo 1 · Engenharia Financeira, TCO Global & Payback](#capitulo-1--engenharia-financeira-tco-global--payback)",
        f"3. [Capítulo 2 · Matriz Estratégica do Quinteto Soberano](#capitulo-2--matriz-estrategica-do-quinteto-soberano)",
        f"4. [Capítulo 3 · Tratados Técnicos Individuais dos Pilares](#capitulo-3--tratados-tecnicos-individuais-dos-pilares)",
        f"5. [Capítulo 4 · Camada de Cola, SSO Federado & Blueprints n8n](#capitulo-4--camada-de-cola-sso-federado--blueprints-n8n)",
        f"6. [Capítulo 5 · Manual de Engenharia de Infraestrutura & Deploy All-in-One](#capitulo-5--manual-de-engenharia-de-infraestrutura--deploy-all-in-one)",
        f"7. [Capítulo 6 · Protocolos de Modularidade & Hot-Swap (Princípio do Lego)](#capitulo-6--protocolos-de-modularidade--hot-swap-principio-do-lego)",
        f"8. [Capítulo 7 · Roteiro Prático de Migração de Dados Históricos](#capitulo-7--roteiro-pratico-de-migracao-de-dados-historicos)",
        f"9. [Capítulo 8 · Governança Corporativa, Backup 3-2-1 & Conformidade LGPD](#capitulo-8--governanca-corporativa-backup-3-2-1--conformidade-lgpd)",
        f"10. [Capítulo 9 · Cronograma de Implantação em 30 Dias & Monitoramento da VPS](#capitulo-9--cronograma-de-implantacao-em-30-dias--monitoramento-da-vps)",
        f"",
        f"---",
        f"",
        f"## PREFÁCIO EXECUTIVO & MANIFESTO DA SOBERANIA TECNOLÓGICA",
        f"",
        f"{deck}",
        f"",
        f"A dependência crônica de suítes de software como serviço (SaaS) impõe três vulnerabilidades críticas a qualquer organização em crescimento:",
        f"1. **Risco de Lock-in Financeiro:** Reajustes anuais unilaterais de 15% a 25% e cobranças por contatos/usuários que penalizam o crescimento da empresa;",
        f"2. **Perda de Soberania sobre os Dados:** Informações confidenciais de clientes, negociações e inteligência comercial hospedadas em bancos multi-tenant de terceiros;",
        f"3. **Rigidez Operacional:** Impossibilidade de customizar código, adaptar telas ou integrar APIs sem pagar planos 'Enterprise' proibitivos.",
        f"",
        f"Este livro-texto consolida a alternativa definitiva: a **migração para uma arquitetura open source auto-hospedada, soberana, de alto desempenho e com payback inferior a 30 dias**.",
        f"",
        f"---",
        f"",
        f"## CAPÍTULO 1 · ENGENHARIA FINANCEIRA, TCO GLOBAL & PAYBACK",
        f"",
        f"### Demonstrativo Contábil Consolidado (Base Anual)",
        f"- **Custo Total SaaS Proprietário ({saas}):** `{econ.get('custo_saas_anual', '')}`",
        f"- **Custo de Infraestrutura VPS Própria (Cluster Unificado 8 vCPU / 16 GB):** `{econ.get('custo_vps_anual', '')}`",
        f"- **Economia Líquida Anual no Caixa:** `{econ.get('economia_anual_liquida', '')}`",
        f"- **Retorno sobre o Investimento (ROI / Payback):** `{econ.get('roi_meses', '')}`",
        f"",
        f"### Desmembramento de Custos e Economia por Frente de Negócio",
        f"| Frente de Negócio | Módulo SaaS Proprietário | Custo SaaS Anual | Custo VPS Alocado | Economia Anual Líquida | Margem de Economia |",
        f"|---|---|---|---|---|---|"
    ]

    for dg in econ.get("detalhamento_por_grupo", []):
        linhas.append(f"| **{dg.get('grupo')}** | {dg.get('saas_referencia')} | `{dg.get('custo_saas_anual')}` | `{dg.get('custo_vps_alocado')}` | `{dg.get('economia_anual_liquida')}` | **{dg.get('percentual_economia')}** |")

    linhas.extend([
        f"",
        f"---",
        f"",
        f"## CAPÍTULO 2 · MATRIZ ESTRATÉGICA DO QUINTETO SOBERANO",
        f"",
        f"| # | Grupo Funcional | Persona | Ferramenta | Módulo SaaS Substituído | Economia Anual | Licença | Repositório |",
        f"|---|---|---|---|---|---|---|---|"
    ])

    global_rank = 1
    for p in pilares:
        for f in p.get("ferramentas", []):
            c_simp = simplificar_classificacao(f.get('classificacao', ''))
            linhas.append(f"| {global_rank:02d} | {p.get('nome_pilar').split(':')[0]} | {c_simp} | **{f['nome']}** | {f['saas_substituido_direto']} | {f['economia_anual_str']} | `{f['licenca_osi']}` | [GitHub]({f['repositorio_github']}) |")
            global_rank += 1

    linhas.extend([
        f"",
        f"---",
        f"",
        f"## CAPÍTULO 3 · TRATADOS TÉCNICOS INDIVIDUAIS DOS PILARES",
        f""
    ])

    for p_idx, p in enumerate(pilares, 1):
        linhas.extend([
            f"### PILAR 0{p_idx}: {p.get('nome_pilar').upper()}",
            f"> **Alvo SaaS Substituído:** `{p.get('modulo_saas_alvo')}` | **Economia do Pilar:** `{p.get('subtotal_economia_anual')}`  ",
            f"> **Descrição Estratégica:** {p.get('descricao_pilar')}",
            f""
        ])
        for f in p.get("ferramentas", []):
            c_simp = simplificar_classificacao(f.get('classificacao', ''))
            linhas.extend([
                f"#### {f['rank']:02d}. {f['nome']} · {f['subtitulo']} (Classificação: Persona {c_simp})",
                f"- **Módulo SaaS Substituído:** `{f['saas_substituido_direto']}`",
                f"- **Economia Anual Individual:** `{f['economia_anual_str']}` | **Licença OSI:** `{f['licenca_osi']}`",
                f"- **Papel no Ecossistema:** {f['papel_no_pilar']}",
                f"",
                f"**1. O Que Faz & Como Funciona:**  ",
                f"{f['o_que_faz']} {f['como_funciona']}",
                f"```bash",
                f"# Inicialização Rápida via Docker / CLI",
                f"{f['comando_rapido']}",
                f"```",
                f"",
                f"**2. Racional Financeiro da Escolha:**  ",
                f"{f['racional_escolha']}",
                f"",
                f"**3. Requisitos de Infraestrutura & Veredito Técnico:**  ",
                f"- Memória RAM Mínima: `{f.get('requisitos_infra', {}).get('ram_minima', '1 GB')}`",
                f"- CPU Recomendada: `{f.get('requisitos_infra', {}).get('cpu_recomendada', '1 vCPU')}`",
                f"- Imagem Docker Oficial: `{f.get('requisitos_infra', {}).get('docker_image', 'oficial')}`",
                f"- Banco de Dados / Persistência: `{f.get('requisitos_infra', {}).get('banco_dados', 'PostgreSQL')}`",
                f"- **Veredito da Engenharia:** *{f.get('veredito')}*",
                f"",
                f"**4. Guia Prático de Uso em 3 Passos:**  "
            ])
            for idx, passo in enumerate(f.get("passos_praticos", []), 1):
                linhas.append(f"{idx}. **{passo.get('titulo')}:** {passo.get('descricao')}")
            
            ds = f.get("design_system", {})
            linhas.extend([
                f"",
                f"**5. White-Label & Design System:**  ",
                f"- Nível de Esforço: `{ds.get('esforco_whitelabel', 'Baixo')}` | Stack UI: `{ds.get('stack_ui', 'Web')}`",
                f"- Mecânica de Customização: {ds.get('mecanica_customizacao', '')}",
                f"- Manutenibilidade de Temas: {ds.get('manutenibilidade_tema', '')}",
                f"",
                f"**6. Ecossistema Agêntico (MCPs, Skills & Extensões):**  "
            ])
            for m in f.get("uso_complementar", []):
                linhas.append(f"- **[{m.get('tipo')}] {m.get('nome')}:** {m.get('descricao')} (`{m.get('comando_ou_repo')}`)")
            
            linhas.append(f"\n- **Repositório Oficial:** [{f['repositorio_github']}]({f['repositorio_github']})\n")

    linhas.extend([
        f"---",
        f"",
        f"## CAPÍTULO 4 · CAMADA DE COLA, SSO FEDERADO & BLUEPRINTS N8N",
        f"",
        f"### Arquitetura de Interconexão sem Silos de Dados",
        f"- **🔑 Autenticação Única Federada (SSO):** {integracao.get('autenticacao_sso')}",
        f"- **⚡ Barramento de Eventos Assíncronos:** {integracao.get('barramento_eventos')}",
        f"- **🛡️ Gateway de Borda & Ingress TLS:** {integracao.get('gateway_reverse_proxy')}",
        f"",
        f"### Fluxo Operacional de Ponta a Ponta",
        f"{integracao.get('fluxo_integracao_descricao')}",
        f"",
        f"### Blueprints de Workflows Prontos para n8n (Importação Instantânea)",
        f""
    ])

    for bp in dados.get("blueprints_n8n", []):
        linhas.extend([
            f"#### {bp.get('nome')}",
            f"- *Objetivo:* {bp.get('descricao')}",
            f"- *Gatilho:* `{bp.get('gatilho')}`",
            f"```json",
            f"{bp.get('json_blueprint')}",
            f"```",
            f""
        ])

    linhas.extend([
        f"---",
        f"",
        f"## CAPÍTULO 5 · MANUAL DE ENGENHARIA DE INFRAESTRUTURA & DEPLOY ALL-IN-ONE",
        f"",
        f"### 💡 Entendendo os 4 Pilares da Infraestrutura (Sem Jargões)",
        f"- **1. O que é VPS?** {deploy.get('analogia_didatica_stack', {}).get('o_que_e_vps', '')}",
        f"- **2. O que é Docker Compose?** {deploy.get('analogia_didatica_stack', {}).get('o_que_e_docker', '')}",
        f"- **3. O que é Traefik?** {deploy.get('analogia_didatica_stack', {}).get('o_que_e_traefik', '')}",
        f"- **4. O que é n8n?** {deploy.get('analogia_didatica_stack', {}).get('o_que_e_n8n', '')}",
        f"",
        f"> **Topologia & Segurança de Rede:** {deploy.get('arquitetura_rede_seguranca', '')}",
        f"",
        f"### Matriz dos 9 Serviços do Orquestrador",
        f"| # | Serviço / Módulo | Imagem Docker | Papel na Infraestrutura | Portas / Exposição | Persistência / Volumes |",
        f"|---|---|---|---|---|---|"
    ])

    for idx, s in enumerate(stack_detalhe, 1):
        linhas.append(f"| {idx:02d} | **{s.get('servico')}** | `{s.get('imagem_docker')}` | {s.get('papel_na_stack')} | `{s.get('portas_expostas')}` | `{s.get('persistencia')}` |")

    linhas.extend([
        f"",
        f"### Dimensionamento de Hardware Recomendado",
        f"- **Memória RAM Total:** `{deploy.get('requisitos_hardware_totais', {}).get('ram_total_recomendada')}`",
        f"- **Processamento CPU:** `{deploy.get('requisitos_hardware_totais', {}).get('cpu_total_recomendada')}`",
        f"- **Armazenamento SSD:** `{deploy.get('requisitos_hardware_totais', {}).get('armazenamento_minimo')}`",
        f"",
        f"### Arquivo `docker-compose.yml` Consolidado para Produção",
        f"```yaml",
        f"{deploy.get('docker_compose_exemplo', '')}",
        f"```",
        f"",
        f"### Roteiro de Instalação e Subida em 4 Passos",
        f""
    ])

    for idx, passo in enumerate(deploy.get("passos_deploy", []), 1):
        linhas.append(f"{idx}. **{passo.get('titulo')}:** {passo.get('descricao')}")

    linhas.extend([
        f"",
        f"---",
        f"",
        f"## CAPÍTULO 6 · PROTOCOLOS DE MODULARIDADE & HOT-SWAP (PRINCÍPIO DO LEGO)",
        f"",
        f"> **O Princípio das Tomadas Independentes:**  ",
        f"> {guia.get('filosofia_modular', '')}",
        f"",
        f"### Protocolo 1: Inserção de Novas Ferramentas (Plug-and-Play)",
        f"{guia.get('passo_a_passo_adicionar_ferramenta', '')}",
        f"",
        f"### Protocolo 2: Substituição de Ferramenta em Produção (Hot-Swap sem Downtime)",
        f"{guia.get('passo_a_passo_substituir_hotswap', '')}",
        f"",
        f"### Protocolo 3: Remoção Segura de Módulos",
        f"{guia.get('passo_a_passo_remover_ferramenta', '')}",
        f"",
        f"### Estudo de Caso Prático: {guia.get('exemplo_caso_pratico_hotswap', {}).get('cenario', '')}",
        f"- **1. Isolamento Operacional:** {guia.get('exemplo_caso_pratico_hotswap', {}).get('passo_1_isolamento')}",
        f"- **2. Início do Novo Contêiner:** `{guia.get('exemplo_caso_pratico_hotswap', {}).get('passo_2_novo_servico')}`",
        f"- **3. Chaveamento no n8n:** {guia.get('exemplo_caso_pratico_hotswap', {}).get('passo_3_chaveamento_n8n')}",
        f"- **4. Resultado Final:** {guia.get('exemplo_caso_pratico_hotswap', {}).get('passo_4_resultado')}",
        f"",
        f"### Perguntas Frequentes (FAQ Operacional para Não-Técnicos)",
        f""
    ])

    for faq in guia.get("faq_nao_tecnicos", []):
        linhas.extend([
            f"- **❓ {faq.get('pergunta')}**",
            f"  - *Resposta:* {faq.get('resposta')}",
            f""
        ])

    linhas.extend([
        f"---",
        f"",
        f"## CAPÍTULO 7 · ROTEIRO PRÁTICO DE MIGRAÇÃO DE DADOS HISTÓRICOS",
        f""
    ])

    for mig in dados.get("guia_migracao_dados", []):
        linhas.extend([
            f"### {mig.get('modulo')}",
            f"- **O que migrar:** {mig.get('o_que_migrar')}",
            f"- **Passos de Migração:**"
        ])
        for p in mig.get("passos", []):
            linhas.append(f"  1. {p}")
        linhas.extend([
            f"- **⚠️ Cuidados Críticos:** {mig.get('cuidados')}",
            f""
        ])

    seg = dados.get("seguranca_backup_lgpd", {})
    linhas.extend([
        f"---",
        f"",
        f"## CAPÍTULO 8 · GOVERNANÇA CORPORATIVA, BACKUP 3-2-1 & CONFORMIDADE LGPD",
        f"",
        f"> **Arquitetura de Proteção de Dados 3-2-1:** {seg.get('arquitetura_backup_321')}",
        f"",
        f"### Script Automatizado de Backup Diário com Criptografia AES-256",
        f"```bash",
        f"{seg.get('script_backup_diario')}",
        f"```",
        f"",
        f"### Checklist de Conformidade Estrita com a LGPD",
        f""
    ])

    for chk in seg.get("checklist_conformidade_lgpd", []):
        linhas.append(f"- **{chk.get('item')}:** {chk.get('status')}")

    linhas.extend([
        f"",
        f"---",
        f"",
        f"## CAPÍTULO 9 · CRONOGRAMA DE IMPLANTAÇÃO EM 30 DIAS & MONITORAMENTO",
        f"",
        f"### Cronograma Executivo de Virada de Chave (4 Semanas)",
        f""
    ])

    for cron in dados.get("cronograma_implantacao_30_dias", []):
        linhas.extend([
            f"#### {cron.get('semana')} · {cron.get('fase')}",
            f"- *Atividades Principais:* {cron.get('atividades')}",
            f"- *🎯 Marco de Conclusão:* **{cron.get('marco_entrega')}**",
            f""
        ])

    mon = dados.get("monitoramento_e_saude_vps", {})
    linhas.extend([
        f"### Monitoramento em Tempo Real da VPS ({mon.get('painel_recomendado')})",
        f"",
        f"**Comandos de Diagnóstico em 1 Clique:**",
        f""
    ])

    for cmd in mon.get("comandos_diagnostico_1clique", []):
        linhas.append(f"- `{cmd.get('comando')}` ➔ {cmd.get('finalidade')}")

    linhas.extend([
        f"",
        f"**Métricas Críticas & Ações Imediatas:**",
        f""
    ])

    for met in mon.get("metricas_alerta", []):
        linhas.append(f"- **{met.get('metrica')}** (Limite: `{met.get('limite_alerta')}`): {met.get('acao_recomendada')}")

    return "\n".join(linhas) + "\n"

def gerar_html_ecossistema_diamante(dados: dict) -> str:
    titulo = dados.get("titulo", "Dossiê de Macro-Ecossistema Open Source")
    subtitulo = dados.get("subtitulo", "")
    deck = dados.get("deck", "")
    saas = dados.get("saas_substituido", "")
    stats = dados.get("stats", {})
    pilares = dados.get("pilares", [])
    integracao = dados.get("camada_integracao", {})
    deploy = dados.get("deploy_consolidado", {})
    guia = dados.get("guia_modularidade_e_expansao", {})
    econ = dados.get("analise_economica_global", {})
    stack_detalhe = deploy.get("composicao_stack_detalhada", [])

    # TABELA MATRIZ GERAL
    linhas_tabela = ""
    global_rank = 1
    for p in pilares:
        for f in p.get("ferramentas", []):
            c_simp = simplificar_classificacao(f.get('classificacao', ''))
            linhas_tabela += f"""
            <tr>
              <td class="rank">{global_rank:02d}</td>
              <td><strong>{p.get('nome_pilar').split(':')[0]}</strong></td>
              <td>{c_simp}</td>
              <td><strong>{f['nome']}</strong></td>
              <td class="saas">{f['saas_substituido_direto']}</td>
              <td class="econ">{f['economia_anual_str']}</td>
              <td><a href="{f['repositorio_github']}" target="_blank" style="color: var(--accent); font-family: var(--mono); font-size: 11px; text-decoration: none; font-weight: 700;">GitHub ↗</a></td>
            </tr>
            """
            global_rank += 1

    # CARDS DOS PILARES
    pilares_conteudo = ""
    for p_idx, p in enumerate(pilares, 1):
        entries_pilar = ""
        for f in p.get("ferramentas", []):
            classif_simples = simplificar_classificacao(f.get('classificacao', ''))
            
            passos_f_html = "".join([
                f"""
                <div class="step-card">
                  <div class="step-head"><span class="step-badge">{idx}</span> {passo.get('titulo')}</div>
                  <p>{passo.get('descricao')}</p>
                </div>
                """
                for idx, passo in enumerate(f.get("passos_praticos", []), 1)
            ])

            ds = f.get("design_system", {})
            mcp_cards_html = "".join([
                f"""
                <div class="mcp-card">
                  <div class="mcp-top">
                    <span class="mcp-pill">{m.get('tipo')}</span>
                    <span class="mcp-name">{m.get('nome')}</span>
                  </div>
                  <p>{m.get('descricao')}</p>
                  <div class="mcp-cmd"><code>{m.get('comando_ou_repo')}</code></div>
                </div>
                """
                for m in f.get("uso_complementar", [])
            ])

            entries_pilar += f"""
            <article class="entry" id="{f['slug']}">
              <div class="entry-rank">{f['rank']:02d}</div>
              <div class="entry-body">
                <div class="entry-top">
                  <h3>{f['nome']} · {f['subtitulo']}</h3>
                  <span class="persona-badge">Persona: {classif_simples}</span>
                  <span class="pilar-badge">{p.get('nome_pilar').split(':')[0]}</span>
                  <span class="killer-badge">Substitui: {f['saas_substituido_direto']}</span>
                  <span class="econ-badge">{f['economia_anual_str']}</span>
                  <span class="lic-badge">{f['licenca_osi']}</span>
                </div>

                <!-- SEÇÃO 1: O QUE FAZ & COMO FUNCIONA -->
                <div class="entry-section">
                  <div class="label">1. O Que Faz &amp; Como Funciona</div>
                  <p><strong>Papel no Ecossistema:</strong> {f['papel_no_pilar']}</p>
                  <p>{f['o_que_faz']} {f['como_funciona']}</p>
                  <div class="code-box">
                    <pre><code>{f['comando_rapido']}</code></pre>
                  </div>
                </div>

                <!-- SEÇÃO 2: ANÁLISE ECONÔMICA & IMPACTO FINANCEIRO -->
                <div class="entry-section">
                  <div class="label">2. Análise Econômica &amp; Racional da Escolha</div>
                  <div class="econ-grid">
                    <div class="econ-card killer">
                      <span class="econ-lbl">🎯 Módulo SaaS Proprietário Substituído</span>
                      <span class="econ-val">{f['saas_substituido_direto']}</span>
                    </div>
                    <div class="econ-card savings">
                      <span class="econ-lbl">💰 Economia Anual Individual</span>
                      <span class="econ-val">{f['economia_anual_str']}</span>
                    </div>
                    <div class="econ-card" style="grid-column: 1 / -1;">
                      <span class="econ-lbl">💡 Racional de Seleção</span>
                      <p style="font-size: 13px; margin: 4px 0 0; color: var(--ink-2);">{f['racional_escolha']}</p>
                    </div>
                  </div>
                </div>

                <!-- SEÇÃO 3: REQUISITOS DE INFRAESTRUTURA & VEREDITO TÉCNICO -->
                <div class="entry-section">
                  <div class="label">3. Requisitos de Infraestrutura, Ecossistema &amp; Veredito Técnico</div>
                  <div class="infra-grid">
                    <div class="infra-card">
                      <span class="infra-lbl">💾 Memória RAM Mínima</span>
                      <span class="infra-val">{f.get('requisitos_infra', {}).get('ram_minima', '1 GB')}</span>
                    </div>
                    <div class="infra-card">
                      <span class="infra-lbl">⚙️ CPU Recomendada</span>
                      <span class="infra-val">{f.get('requisitos_infra', {}).get('cpu_recomendada', '1 vCPU')}</span>
                    </div>
                    <div class="infra-card">
                      <span class="infra-lbl">📦 Imagem Docker Oficial</span>
                      <span class="infra-val"><code>{f.get('requisitos_infra', {}).get('docker_image', 'oficial')}</code></span>
                    </div>
                    <div class="infra-card">
                      <span class="infra-lbl">🗄️ Persistência / Banco</span>
                      <span class="infra-val">{f.get('requisitos_infra', {}).get('banco_dados', 'PostgreSQL')}</span>
                    </div>
                    <div class="infra-card verdict">
                      <span class="infra-lbl">⚖️ Veredito Técnico da Engenharia</span>
                      <p style="font-size: 13px; margin: 4px 0 0; color: var(--ink-2);">{f.get('veredito')}</p>
                    </div>
                  </div>
                  <div style="margin-top: 8px;">
                    <a href="{f['repositorio_github']}" target="_blank" style="display: inline-flex; align-items: center; gap: 6px; font-family: var(--mono); font-size: 11.5px; font-weight: 700; color: var(--accent); text-decoration: none; padding: 6px 12px; border: 1px solid var(--accent); border-radius: 2px;">
                      📦 Repositório Oficial no GitHub ↗
                    </a>
                  </div>
                </div>

                <!-- SEÇÃO 4: GUIA PRÁTICO EM 3 PASSOS -->
                <div class="entry-section">
                  <div class="label">4. Como Usar no Dia a Dia · Guia Prático em 3 Passos</div>
                  <div class="steps-grid">
                    {passos_f_html}
                  </div>
                </div>

                <!-- SEÇÃO 5: DESIGN SYSTEM & WHITE-LABEL -->
                <div class="entry-section">
                  <div class="ds-header">
                    <div class="label">5. White-Label &amp; Aderência ao Design System Corporativo</div>
                    <div class="ds-badges">
                      <span class="ds-badge esforco-minimo">Esforço: {ds.get('esforco_whitelabel', 'Baixo')}</span>
                      <span class="ds-badge stack-ui">UI: {ds.get('stack_ui', 'Web')}</span>
                    </div>
                  </div>
                  <div class="ds-grid">
                    <div class="ds-card">
                      <span class="ds-lbl">Mecânica de Customização</span>
                      <p>{ds.get('mecanica_customizacao', 'Suporte a temas e logos')}</p>
                    </div>
                    <div class="ds-card">
                      <span class="ds-lbl">Facilidade de Manutenção</span>
                      <p>{ds.get('manutenibilidade_tema', 'Alta aderência')}</p>
                    </div>
                  </div>
                </div>

                <!-- SEÇÃO 6: USO COMPLEMENTAR & ECOSSISTEMA AGÊNTICO -->
                <div class="entry-section">
                  <div class="label">6. Uso Complementar &amp; Ecossistema Agêntico (MCPs, Skills &amp; CLI)</div>
                  <div class="mcp-grid">
                    {mcp_cards_html}
                  </div>
                </div>

              </div>
            </article>
            """

        pilares_conteudo += f"""
        <div class="sec-head" id="pilar-{p_idx}">
          <div class="sec-info">
            <span class="sec-num">Pilar 0{p_idx} · {p.get('modulo_saas_alvo')}</span>
            <h2>{p.get('nome_pilar')}</h2>
            <p class="sec-note">{p.get('descricao_pilar')}</p>
          </div>
          <div class="pilar-subtotal-badge">Subtotal do Grupo: {p.get('subtotal_economia_anual')}</div>
        </div>
        <div class="ledger">
          {entries_pilar}
        </div>
        """

    passos_cards = "".join([
        f'<div class="step-card"><div class="step-head"><span class="step-badge">0{idx}</span> {passo.get("titulo")}</div><p>{passo.get("descricao")}</p></div>'
        for idx, passo in enumerate(deploy.get("passos_deploy", []), 1)
    ])

    detalhe_econ = econ.get("detalhamento_por_grupo", [])
    tabela_tco_grupos = ""
    if detalhe_econ:
        linhas_tco_grupos = "".join([
            f"""
            <tr>
              <td><strong>{dg.get('grupo')}</strong></td>
              <td class="saas">{dg.get('saas_referencia')}</td>
              <td class="killer">{dg.get('custo_saas_anual')}</td>
              <td>{dg.get('custo_vps_alocado')}</td>
              <td class="econ">{dg.get('economia_anual_liquida')}</td>
              <td><span class="econ-badge">{dg.get('percentual_economia')}</span></td>
            </tr>
            """
            for dg in detalhe_econ
        ])
        tabela_tco_grupos = f"""
        <div class="tablewrap" style="margin-top: 16px; margin-bottom: 20px;">
          <table>
            <thead>
              <tr>
                <th>Grupo / Frente de Negócio</th>
                <th>SaaS de Referência</th>
                <th>Custo SaaS Anual</th>
                <th>Custo VPS Alocado</th>
                <th>Economia Líquida Anual</th>
                <th>Economia (%)</th>
              </tr>
            </thead>
            <tbody>
              {linhas_tco_grupos}
            </tbody>
          </table>
        </div>
        """

    stack_linhas_tabela = "".join([
        f"""
        <tr>
          <td class="rank">{idx:02d}</td>
          <td><strong>{s.get('servico')}</strong></td>
          <td><code>{s.get('imagem_docker')}</code></td>
          <td>{s.get('papel_na_stack')}</td>
          <td><code>{s.get('portas_expostas')}</code></td>
          <td><code>{s.get('persistencia')}</code></td>
        </tr>
        """
        for idx, s in enumerate(stack_detalhe, 1)
    ])

    tabela_stack_html = f"""
    <div class="tablewrap" style="margin: 14px 0 20px;">
      <table>
        <thead>
          <tr>
            <th>#</th>
            <th>Serviço / Ferramenta</th>
            <th>Imagem Docker</th>
            <th>Papel na Stack</th>
            <th>Portas / Exposição</th>
            <th>Persistência</th>
          </tr>
        </thead>
        <tbody>
          {stack_linhas_tabela}
        </tbody>
      </table>
    </div>
    """

    stack_cards_html = "".join([
        f"""
        <div class="integ-card" style="margin-bottom: 12px;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px; flex-wrap: wrap; gap: 8px;">
            <h4 style="margin: 0; color: var(--ink);">{s.get('servico')}</h4>
            <code style="font-size: 11px; background: var(--surface-2); padding: 2px 8px; border-radius: 2px; border: 1px solid var(--rule-soft);">{s.get('imagem_docker')}</code>
          </div>
          <p><strong>Papel na Infraestrutura:</strong> {s.get('papel_na_stack')}</p>
          <p style="margin-top: 4px;"><strong>Por que faz parte do Deploy All-in-One:</strong> {s.get('racional_escolha')}</p>
          <div style="display: flex; gap: 20px; margin-top: 8px; font-size: 12px; font-family: var(--mono); color: var(--muted); flex-wrap: wrap;">
            <span>🔌 <strong>Rede/Portas:</strong> {s.get('portas_expostas')}</span>
            <span>💾 <strong>Armazenamento:</strong> {s.get('persistencia')}</span>
          </div>
        </div>
        """
        for s in stack_detalhe
    ])

    analogias = deploy.get("analogia_didatica_stack", {})
    analogias_cards_html = f"""
    <div class="integration-grid" style="margin: 16px 0 24px;">
      <div class="integ-card">
        <h4>🏢 1. O que é a VPS?</h4>
        <p>{analogias.get('o_que_e_vps', 'Seu servidor potente na nuvem que fica ligado 24h por dia.')}</p>
      </div>
      <div class="integ-card">
        <h4>📦 2. O que é o Docker Compose?</h4>
        <p>{analogias.get('o_que_e_docker', 'A receita pronta que instala e liga todas as ferramentas automaticamente.')}</p>
      </div>
      <div class="integ-card">
        <h4>🛡️ 3. O que é o Traefik?</h4>
        <p>{analogias.get('o_que_e_traefik', 'O porteiro inteligente que coloca o cadeado verde SSL e distribui os links.')}</p>
      </div>
      <div class="integ-card">
        <h4>⚡ 4. O que é o n8n?</h4>
        <p>{analogias.get('o_que_e_n8n', 'O mensageiro que leva as informações de uma ferramenta para outra sem código.')}</p>
      </div>
    </div>
    """

    faq_cards_html = "".join([
        f"""
        <div class="integ-card" style="margin-bottom: 12px;">
          <h4>❓ {faq.get('pergunta')}</h4>
          <p style="margin-top: 6px;"><strong>Resposta:</strong> {faq.get('resposta')}</p>
        </div>
        """
        for faq in guia.get("faq_nao_tecnicos", [])
    ])

    passos_add_html = "".join([
        f"""
        <div class="step-card">
          <div class="step-head">{p_add.get('etapa')}</div>
          <p>{p_add.get('descricao')}</p>
        </div>
        """
        for p_add in guia.get("passos_adicionar_ferramenta", [])
    ])

    caso_pratico = guia.get("exemplo_caso_pratico_hotswap", {})

    blueprints_html = "".join([
        f"""
        <div class="blueprint-card">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px; flex-wrap: wrap; gap: 8px;">
            <h4 style="margin: 0; font-family: var(--font-serif); font-size: 18px; color: var(--ink);">{bp.get('nome')}</h4>
            <span class="persona-badge">Template Pronto</span>
          </div>
          <p style="font-size: 13.5px; color: var(--ink-2); margin: 0 0 10px;">{bp.get('descricao')}</p>
          <div style="display: flex; gap: 12px; margin-bottom: 10px; font-family: var(--mono); font-size: 11px; color: var(--muted); flex-wrap: wrap;">
            <span>⚡ <strong>Gatilho:</strong> <code>{bp.get('gatilho')}</code></span>
          </div>
          <div class="code-box">
            <pre><code>{bp.get('json_blueprint')}</code></pre>
          </div>
        </div>
        """
        for bp in dados.get("blueprints_n8n", [])
    ])

    migracao_cards_html = "".join([
        f"""
        <div class="integ-card" style="margin-bottom: 14px;">
          <h4>{mig.get('modulo')}</h4>
          <p><strong>O que é migrado:</strong> {mig.get('o_que_migrar')}</p>
          <div class="steps-grid" style="margin: 10px 0;">
            {''.join([f'<div class="step-card"><div class="step-head"><span class="step-badge">{idx}</span> Etapa {idx}</div><p>{p}</p></div>' for idx, p in enumerate(mig.get('passos', []), 1)])}
          </div>
          <div style="background: var(--flag-soft); border-left: 3px solid var(--flag); padding: 8px 12px; border-radius: 2px; font-size: 12.5px; color: var(--flag); margin-top: 6px;">
            <strong>⚠️ Cuidado Essencial:</strong> {mig.get('cuidados')}
          </div>
        </div>
        """
        for mig in dados.get("guia_migracao_dados", [])
    ])

    seg = dados.get("seguranca_backup_lgpd", {})
    checklist_lgpd_html = "".join([
        f"""
        <div class="stat-card" style="margin-bottom: 8px;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
            <strong style="color: var(--ink); font-size: 13.5px;">{chk.get('item')}</strong>
            <span class="econ-badge" style="font-size: 9.5px;">Auditado</span>
          </div>
          <p style="margin: 0; font-size: 12.5px; color: var(--ink-2);">{chk.get('status')}</p>
        </div>
        """
        for chk in seg.get("checklist_conformidade_lgpd", [])
    ])

    cronograma_html = "".join([
        f"""
        <div class="timeline-card">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px; flex-wrap: wrap;">
            <h4>{cron.get('semana')} · {cron.get('fase')}</h4>
            <span class="persona-badge" style="font-size: 9.5px;">Meta</span>
          </div>
          <p style="font-size: 13px; margin: 0 0 6px; color: var(--ink-2);">{cron.get('atividades')}</p>
          <div style="font-family: var(--mono); font-size: 11.5px; color: var(--green); font-weight: 700;">
            🎯 Marco de Entrega: {cron.get('marco_entrega')}
          </div>
        </div>
        """
        for cron in dados.get("cronograma_implantacao_30_dias", [])
    ])

    mon = dados.get("monitoramento_e_saude_vps", {})
    comandos_mon_html = "".join([
        f"""
        <div style="display: flex; justify-content: space-between; align-items: center; padding: 8px 12px; background: var(--surface-2); border: 1px solid var(--rule-soft); border-radius: 2px; margin-bottom: 6px; flex-wrap: wrap; gap: 8px;">
          <code style="font-family: var(--mono); font-size: 12px; font-weight: 700; color: var(--ink);">{cmd.get('comando')}</code>
          <span style="font-size: 12.5px; color: var(--muted);">{cmd.get('finalidade')}</span>
        </div>
        """
        for cmd in mon.get("comandos_diagnostico_1clique", [])
    ])

    metricas_mon_html = "".join([
        f"""
        <div class="stat-card">
          <div class="stat-lbl">{met.get('metrica')}</div>
          <div style="font-family: var(--mono); font-size: 12px; color: var(--flag); font-weight: 700; margin: 2px 0;">Alerta: {met.get('limite_alerta')}</div>
          <p style="margin: 0; font-size: 12px; color: var(--ink-2);"><strong>Ação:</strong> {met.get('acao_recomendada')}</p>
        </div>
        """
        for met in mon.get("metricas_alerta", [])
    ])

    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1" name="viewport"/>
<title>LIVRO-TEXTO: {titulo} · Fábrica Universal AIDD</title>
<style>
{CSS_CANONICO_DIAMANTE}
</style>
</head>
<body>
<div class="wrap">
  
  <!-- CAPA DO LIVRO MESTRE -->
  <div class="book-cover">
    <div class="book-tagline">Fábrica Universal AIDD · Livro-Texto Executivo &amp; Tratado de Engenharia</div>
    <h1 class="book-title">{titulo}</h1>
    <p class="book-subtitle">{subtitulo} — Guia definitivo de desmantelamento de suítes de software proprietário, arquitetura open source de alta fidelidade e soberania digital corporativa.</p>
    
    <div class="book-meta-grid">
      <div class="book-meta-item">Alvo SaaS Desmantelado<strong>{saas}</strong></div>
      <div class="book-meta-item">Economia Líquida Anual<strong style="color: var(--green);">{econ.get('economia_anual_liquida')}</strong></div>
      <div class="book-meta-item">Arsenal de Ferramentas<strong>{stats.get('total_ferramentas', 15)} Soluções OSI</strong></div>
      <div class="book-meta-item">Edição &amp; Governança<strong>1ª Edição · Padrão R5-E</strong></div>
    </div>
  </div>

  <!-- SUMÁRIO GERAL -->
  <div class="toc-box">
    <h3>📖 Sumário Geral dos Capítulos</h3>
    <div class="toc-grid">
      <div class="toc-item"><a href="#cap-01">Capítulo 01 · Demonstrativo Financeiro &amp; Calculadora TCO</a> <span>Pág. 04</span></div>
      <div class="toc-item"><a href="#cap-02">Capítulo 02 · Matriz Geral do Quinteto Soberano</a> <span>Pág. 08</span></div>
      <div class="toc-item"><a href="#pilar-1">Capítulo 03 · Pilar 01: Marketing &amp; Nutrição</a> <span>Pág. 12</span></div>
      <div class="toc-item"><a href="#pilar-2">Capítulo 04 · Pilar 02: Pipeline Comercial &amp; CRM</a> <span>Pág. 24</span></div>
      <div class="toc-item"><a href="#pilar-3">Capítulo 05 · Pilar 03: Atendimento &amp; WhatsApp</a> <span>Pág. 36</span></div>
      <div class="toc-item"><a href="#cap-04">Capítulo 06 · Camada de Cola, SSO &amp; Blueprints n8n</a> <span>Pág. 48</span></div>
      <div class="toc-item"><a href="#cap-05">Capítulo 07 · Manual de Deploy All-in-One Compose</a> <span>Pág. 56</span></div>
      <div class="toc-item"><a href="#cap-06">Capítulo 08 · Guia de Modularidade &amp; Hot-Swap Lego</a> <span>Pág. 64</span></div>
      <div class="toc-item"><a href="#cap-07">Capítulo 09 · Roteiro de Migração de Dados De-SaaS</a> <span>Pág. 72</span></div>
      <div class="toc-item"><a href="#cap-08">Capítulo 10 · Segurança, Backup 3-2-1 &amp; LGPD</a> <span>Pág. 80</span></div>
      <div class="toc-item"><a href="#cap-09">Capítulo 11 · Cronograma 30 Dias &amp; Monitoramento</a> <span>Pág. 88</span></div>
    </div>
  </div>

  <!-- SEÇÃO 01: TCO & CALCULADORA -->
  <div class="sec-head" id="cap-01">
    <div class="sec-info">
      <span class="sec-num">Capítulo 01 · Engenharia Financeira &amp; TCO Global</span>
      <h2>Demonstrativo de Payback &amp; Calculadora Interativa</h2>
      <p class="sec-note">Demonstrativo contábil comparativo de desmantelamento de custos de licenças de software.</p>
    </div>
  </div>

  <div class="tco-banner">
    <div class="tco-col">
      <div class="tco-lbl">Custo SaaS Proprietário Anual</div>
      <div class="tco-val killer">{econ.get('custo_saas_anual')}</div>
    </div>
    <div class="tco-col">
      <div class="tco-lbl">Custo VPS Soberana Unificada</div>
      <div class="tco-val">{econ.get('custo_vps_anual')}</div>
    </div>
    <div class="tco-col">
      <div class="tco-lbl">Economia Líquida Anual</div>
      <div class="tco-val highlight">{econ.get('economia_anual_liquida')}</div>
    </div>
    <div class="tco-col">
      <div class="tco-lbl">Payback Estimado</div>
      <div class="tco-val highlight">{econ.get('roi_meses')}</div>
    </div>
  </div>

  <h3 style="font-family: var(--font-serif); font-size: 20px; margin: 24px 0 10px; color: var(--ink);">🧮 Simulação Interativa de Economia em Tempo Real</h3>
  <div class="calc-box">
    <div class="calc-grid">
      <div class="calc-slider-group">
        <label><span>Base de Leads Ativos</span> <strong id="val-leads" style="color: var(--accent);">50.000 leads</strong></label>
        <input type="range" id="slider-leads" min="5000" max="200000" step="5000" value="50000">
      </div>
      <div class="calc-slider-group">
        <label><span>Vendedores no CRM</span> <strong id="val-sellers" style="color: var(--accent);">10 vendedores</strong></label>
        <input type="range" id="slider-sellers" min="1" max="50" step="1" value="10">
      </div>
      <div class="calc-slider-group">
        <label><span>Atendentes de WhatsApp</span> <strong id="val-agents" style="color: var(--accent);">10 atendentes</strong></label>
        <input type="range" id="slider-agents" min="1" max="50" step="1" value="10">
      </div>
    </div>
    <div class="calc-results">
      <div>
        <div class="stat-lbl">Seu Custo SaaS Atual</div>
        <div class="stat-val alert" id="calc-saas-total">R$ 114.000/ano</div>
      </div>
      <div>
        <div class="stat-lbl">Seu Custo na VPS Própria</div>
        <div class="stat-val" id="calc-vps-total">R$ 4.200/ano</div>
      </div>
      <div>
        <div class="stat-lbl">Dinheiro que Fica no seu Caixa</div>
        <div class="stat-val highlight" id="calc-savings-total">R$ 109.800/ano (96.3%)</div>
      </div>
    </div>
  </div>

  <h3 style="font-family: var(--font-serif); font-size: 20px; margin: 24px 0 10px; color: var(--ink);">Desmembramento por Frente de Negócio</h3>
  {tabela_tco_grupos}

  <!-- SEÇÃO 02: MATRIZ GERAL -->
  <div class="sec-head" id="cap-02">
    <div class="sec-info">
      <span class="sec-num">Capítulo 02 · Matriz Estratégica do Quinteto Soberano</span>
      <h2>Pilha Aberta Integrada por Grupo Funcional</h2>
      <p class="sec-note">Visão consolidada das 15 ferramentas que compõem os 3 pilares estratégicos da suíte.</p>
    </div>
  </div>

  <div style="margin: 16px 0 12px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
    <input type="text" id="busca-ferramentas" placeholder="Pressione '/' para buscar por nome, módulo ou palavra-chave..." style="flex: 1; min-width: 280px; padding: 10px 14px; font-family: var(--font-sans); font-size: 13.5px; border: 1px solid var(--rule); border-radius: 2px; background: var(--surface-2); color: var(--ink);">
    <span id="search-count" style="font-family: var(--mono); font-size: 12px; color: var(--muted);">15 ferramentas listadas</span>
  </div>

  <div class="tablewrap">
    <table>
      <thead>
        <tr>
          <th>#</th>
          <th>Grupo</th>
          <th>Classificação</th>
          <th>Ferramenta</th>
          <th>Substitui</th>
          <th>Economia Estimada</th>
          <th>Código</th>
        </tr>
      </thead>
      <tbody>
        {linhas_tabela}
      </tbody>
    </table>
  </div>

  <!-- SEÇÃO 03: FICHAS TÉCNICAS -->
  {pilares_conteudo}

  <!-- SEÇÃO 04: INTEGRAÇÃO & BLUEPRINTS -->
  <div class="sec-head" id="cap-04">
    <div class="sec-info">
      <span class="sec-num">Capítulo 06 · Camada de Cola &amp; Orquestração</span>
      <h2>SSO Federado, Barramento &amp; Blueprints n8n</h2>
      <p class="sec-note">Como os módulos dialogam de forma transparente com fluxos automatizados prontos para uso.</p>
    </div>
  </div>

  <div class="integration-grid">
    <div class="integ-card">
      <h4>🔑 Autenticação Unificada (SSO)</h4>
      <p>{integracao.get('autenticacao_sso')}</p>
    </div>
    <div class="integ-card">
      <h4>⚡ Barramento de Eventos</h4>
      <p>{integracao.get('barramento_eventos')}</p>
    </div>
    <div class="integ-card">
      <h4>🛡️ Reverse Proxy &amp; TLS</h4>
      <p>{integracao.get('gateway_reverse_proxy')}</p>
    </div>
  </div>

  <div class="integ-card" style="margin-top: 12px; margin-bottom: 24px;">
    <h4>🔄 Fluxo de Integração Operacional</h4>
    <p style="white-space: pre-line; margin-top: 8px;">{integracao.get('fluxo_integracao_descricao')}</p>
  </div>

  <h3 style="font-family: var(--font-serif); font-size: 20px; margin: 24px 0 10px; color: var(--ink);">📦 Blueprints de Workflows Prontos para n8n (Importação Instantânea)</h3>
  <p style="font-size: 13.5px; color: var(--muted); margin: 0 0 14px;">Basta copiar o JSON abaixo e colar no painel do seu n8n para que todos os módulos comecem a conversar automaticamente.</p>
  {blueprints_html}

  <!-- SEÇÃO 05: DEPLOY ALL-IN-ONE -->
  <div class="sec-head" id="cap-05">
    <div class="sec-info">
      <span class="sec-num">Capítulo 07 · Manual de Engenharia de Infraestrutura</span>
      <h2>Deploy All-in-One em Docker Compose</h2>
      <p class="sec-note">Conceitos explicados sem jargões para gestores de marketing, vendas e diretores ({deploy.get('requisitos_hardware_totais', {}).get('cpu_total_recomendada')} / {deploy.get('requisitos_hardware_totais', {}).get('ram_total_recomendada')}).</p>
    </div>
  </div>

  <h3 style="font-family: var(--font-serif); font-size: 20px; margin: 16px 0 10px; color: var(--ink);">💡 Entendendo os 4 Pilares da Infraestrutura (Sem Jargões)</h3>
  <p style="font-size: 13.5px; color: var(--muted); margin: 0 0 12px;">Como cada peça se encaixa para que a sua empresa tenha autonomia completa sem depender de planos SaaS caros.</p>
  {analogias_cards_html}

  <div class="racional-box" style="margin-bottom: 20px;">
    <p><strong>🛡️ Segurança e Topologia de Rede:</strong> {deploy.get('arquitetura_rede_seguranca')}</p>
  </div>

  <h3 style="font-family: var(--font-serif); font-size: 20px; margin: 24px 0 10px; color: var(--ink);">1. Matriz dos Serviços da Stack (docker-compose.yml)</h3>
  <p style="font-size: 13.5px; color: var(--muted); margin: 0 0 12px;">Visão tabular de todas as ferramentas de infraestrutura, aplicação, banco e filas presentes no orquestrador.</p>
  {tabela_stack_html}

  <h3 style="font-family: var(--font-serif); font-size: 20px; margin: 28px 0 10px; color: var(--ink);">2. Racional &amp; Papel de Cada Ferramenta na Stack</h3>
  <p style="font-size: 13.5px; color: var(--muted); margin: 0 0 14px;">Detalhamento técnico de por que cada componente foi selecionado e sua interdependência operacional no cluster.</p>
  {stack_cards_html}

  <h3 style="font-family: var(--font-serif); font-size: 20px; margin: 28px 0 10px; color: var(--ink);">3. Arquivo docker-compose.yml Completo</h3>
  <p style="font-size: 13.5px; color: var(--muted); margin: 0 0 12px;">Manifesto de orquestração pronto para produção com volumes, redes, variáveis de ambiente e labels Traefik.</p>
  <div class="code-box" style="margin-bottom: 20px;">
    <pre><code>{deploy.get('docker_compose_exemplo')}</code></pre>
  </div>

  <h3 style="font-family: var(--font-serif); font-size: 20px; margin: 24px 0 10px; color: var(--ink);">4. Roteiro de Instalação Rápida (4 Passos Simples)</h3>
  <div class="steps-grid">
    {passos_cards}
  </div>

  <!-- SEÇÃO 06: MODULARIDADE & HOT-SWAP -->
  <div class="sec-head" id="cap-06" style="margin-top: 48px;">
    <div class="sec-info">
      <span class="sec-num">Capítulo 08 · Protocolos de Modularidade &amp; Hot-Swap</span>
      <h2>Adição, Substituição &amp; Remoção de Ferramentas (Princípio do Lego)</h2>
      <p class="sec-note">Como personalizar o ecossistema e trocar ferramentas sem quebrar o cluster nem interromper a operação comercial.</p>
    </div>
  </div>

  <div class="racional-box" style="margin-bottom: 20px;">
    <p><strong>🧩 O Princípio das Tomadas Independentes:</strong> {guia.get('filosofia_modular')}</p>
  </div>

  <h3 style="font-family: var(--font-serif); font-size: 20px; margin: 20px 0 12px; color: var(--ink);">1. Protocolo de Inserção de Novas Ferramentas (Plug-and-Play)</h3>
  <div class="steps-grid">
    {passos_add_html}
  </div>

  <h3 style="font-family: var(--font-serif); font-size: 20px; margin: 28px 0 12px; color: var(--ink);">2. Protocolo de Hot-Swap (Substituição de Ferramenta sem Parar o Negócio)</h3>
  <div class="integ-card" style="margin-bottom: 16px;">
    <p style="white-space: pre-line;">{guia.get('passo_a_passo_substituir_hotswap')}</p>
  </div>

  <h3 style="font-family: var(--font-serif); font-size: 20px; margin: 24px 0 12px; color: var(--ink);">3. Protocolo de Remoção Segura de Serviços</h3>
  <div class="integ-card" style="margin-bottom: 16px;">
    <p style="white-space: pre-line;">{guia.get('passo_a_passo_remover_ferramenta')}</p>
  </div>

  <h3 style="font-family: var(--font-serif); font-size: 20px; margin: 24px 0 12px; color: var(--ink);">4. Estudo de Caso Prático: {caso_pratico.get('cenario')}</h3>
  <div class="entry" style="grid-template-columns: 1fr; margin-bottom: 24px;">
    <div class="entry-body">
      <p><strong>1. Isolamento Operacional:</strong> {caso_pratico.get('passo_1_isolamento')}</p>
      <p><strong>2. Início do Novo Contêiner:</strong> <code>{caso_pratico.get('passo_2_novo_servico')}</code></p>
      <p><strong>3. Chaveamento no n8n:</strong> {caso_pratico.get('passo_3_chaveamento_n8n')}</p>
      <p style="color: var(--green); font-weight: 600;"><strong>4. Veredito Final:</strong> {caso_pratico.get('passo_4_resultado')}</p>
    </div>
  </div>

  <h3 style="font-family: var(--font-serif); font-size: 20px; margin: 28px 0 12px; color: var(--ink);">5. Perguntas Frequentes (FAQ Operacional para Não-Técnicos)</h3>
  {faq_cards_html}

  <!-- SEÇÃO 07: MIGRAÇÃO DE DADOS -->
  <div class="sec-head" id="cap-07" style="margin-top: 48px;">
    <div class="sec-info">
      <span class="sec-num">Capítulo 09 · Roteiro Prático de Migração de Dados</span>
      <h2>De-SaaS para Soberano (Transição Segura sem Perdas)</h2>
      <p class="sec-note">Roteiro passo a passo para exportar dados do RD Station e importar no Mautic, Twenty e Chatwoot.</p>
    </div>
  </div>
  {migracao_cards_html}

  <!-- SEÇÃO 08: SEGURANÇA & LGPD -->
  <div class="sec-head" id="cap-08" style="margin-top: 48px;">
    <div class="sec-info">
      <span class="sec-num">Capítulo 10 · Governança Corporativa, Backup 3-2-1 &amp; LGPD</span>
      <h2>Soberania de Dados &amp; Proteção de Ativos Digitais</h2>
      <p class="sec-note">Conformidade jurídica estrita com a LGPD e política de backup com criptografia AES-256 em nuvem fria.</p>
    </div>
  </div>

  <div class="racional-box">
    <p><strong>🛡️ Regra de Ouro do Backup (3-2-1):</strong> {seg.get('arquitetura_backup_321')}</p>
  </div>

  <h3 style="font-family: var(--font-serif); font-size: 20px; margin: 20px 0 10px; color: var(--ink);">Script de Backup Diário Automatizado (PostgreSQL + Mídias)</h3>
  <div class="code-box" style="margin-bottom: 20px;">
    <pre><code>{seg.get('script_backup_diario')}</code></pre>
  </div>

  <h3 style="font-family: var(--font-serif); font-size: 20px; margin: 24px 0 10px; color: var(--ink);">Checklist de Conformidade com a LGPD</h3>
  {checklist_lgpd_html}

  <!-- SEÇÃO 09: CRONOGRAMA 30 DIAS & MONITORAMENTO -->
  <div class="sec-head" id="cap-09" style="margin-top: 48px;">
    <div class="sec-info">
      <span class="sec-num">Capítulo 11 · Cronograma de Implantação em 30 Dias &amp; Monitoramento</span>
      <h2>Plano Executivo de Virada de Chave &amp; Health Check</h2>
      <p class="sec-note">Planejamento semana a semana e comandos em 1 clique para inspecionar memória e bancos.</p>
    </div>
  </div>
  {cronograma_html}

  <h3 style="font-family: var(--font-serif); font-size: 20px; margin: 32px 0 10px; color: var(--ink);">Comandos de Diagnóstico Rápido (1 Clique)</h3>
  {comandos_mon_html}

  <h3 style="font-family: var(--font-serif); font-size: 20px; margin: 24px 0 10px; color: var(--ink);">Métricas Críticas &amp; Protocolo de Resolução</h3>
  <div class="integration-grid">
    {metricas_mon_html}
  </div>

</div>
{JS_CANONICO_DIAMANTE}
</body>
</html>
"""
    return html

def gerar_typst_ecossistema(dados: dict) -> str:
    titulo = dados.get("titulo", "Dossiê de Macro-Ecossistema Open Source")
    subtitulo = dados.get("subtitulo", "")
    deck = dados.get("deck", "")
    saas = dados.get("saas_substituido", "")
    stats = dados.get("stats", {})
    pilares = dados.get("pilares", [])
    integracao = dados.get("camada_integracao", {})
    deploy = dados.get("deploy_consolidado", {})
    guia = dados.get("guia_modularidade_e_expansao", {})
    econ = dados.get("analise_economica_global", {})
    seg = dados.get("seguranca_backup_lgpd", {})
    mon = dados.get("monitoramento_e_saude_vps", {})
    stack_detalhe = deploy.get("composicao_stack_detalhada", [])

    def sanitizar_typ(txt: str) -> str:
        return str(txt).replace('[', '(').replace(']', ')').replace('$', '\\$').replace('#', '\\#').replace('_', '\\_').replace('(*.', '(wildcard.').replace('*.', 'wildcard.')

    # PILARES E FERRAMENTAS COMPLETAS EM TYPST
    capitulos_pilares_typ = ""
    for p_idx, p in enumerate(pilares, 1):
        capitulos_pilares_typ += f"""
#pagebreak()
= Capítulo {p_idx + 2}: Pilar 0{p_idx} · {sanitizar_typ(p.get('nome_pilar'))}

#text(size: 9pt, fill: rgb("#0284c7"), weight: "bold")[Alvo SaaS Substituído: {sanitizar_typ(p.get('modulo_saas_alvo'))}] \\
#text(size: 9pt, fill: rgb("#00875A"), weight: "bold")[Subtotal de Economia do Grupo: {sanitizar_typ(p.get('subtotal_economia_anual'))}] \\
#text(size: 9pt, style: "italic", fill: rgb("#475569"))[{sanitizar_typ(p.get('descricao_pilar'))}]

#v(8pt)
"""
        for f in p.get("ferramentas", []):
            c_simp = simplificar_classificacao(f.get('classificacao', ''))
            ds = f.get("design_system", {})
            capitulos_pilares_typ += f"""
== {f['rank']:02d}. {sanitizar_typ(f['nome'])} · {sanitizar_typ(f['subtitulo'])} (Persona: {c_simp})

#rect(fill: rgb("#f8fafc"), stroke: 0.5pt + rgb("#cbd5e1"), inset: 8pt, radius: 2pt, width: 100%)[
  #grid(
    columns: (1fr, 1fr, 1fr),
    gutter: 6pt,
    [*Substitui:* {sanitizar_typ(f['saas_substituido_direto'])}],
    [*Economia:* #text(fill: rgb("#00875A"), weight: "bold")[{sanitizar_typ(f['economia_anual_str'])}]],
    [*Licença:* `{sanitizar_typ(f['licenca_osi'])}`]
  )
]

*1. O Que Faz & Como Funciona:* \\
{sanitizar_typ(f['o_que_faz'])} {sanitizar_typ(f['como_funciona'])}

```bash
{f['comando_rapido']}
```

*2. Racional da Escolha & Veredito Técnico:* \\
{sanitizar_typ(f['racional_escolha'])} \\
#text(style: "italic", fill: rgb("#334155"))[*Veredito:* {sanitizar_typ(f.get('veredito', ''))}]

*3. Requisitos de Infraestrutura & White-Label:* \\
- RAM Mínima: `{sanitizar_typ(f.get('requisitos_infra', {}).get('ram_minima', '1 GB'))}` | CPU: `{sanitizar_typ(f.get('requisitos_infra', {}).get('cpu_recomendada', '1 vCPU'))}` | Docker: `{sanitizar_typ(f.get('requisitos_infra', {}).get('docker_image', 'oficial'))}`
- Customização UI: {sanitizar_typ(ds.get('mecanica_customizacao', ''))} (Esforço: {sanitizar_typ(ds.get('esforco_whitelabel', 'Baixo'))})

#v(10pt)
"""

    custo_saas = sanitizar_typ(econ.get('custo_saas_anual', ''))
    custo_vps = sanitizar_typ(econ.get('custo_vps_anual', ''))
    econ_liq = sanitizar_typ(econ.get('economia_anual_liquida', ''))
    roi = sanitizar_typ(econ.get('roi_meses', ''))

    typ = f"""#set page(
  paper: "a4",
  margin: (x: 1.8cm, top: 2.2cm, bottom: 2.2cm),
  header: align(right)[
    #text(size: 7.5pt, fill: rgb("#94a3b8"), font: "Liberation Sans")[FÁBRICA UNIVERSAL AIDD · LIVRO-TEXTO DE MACRO-ECOSSISTEMA SOBERANO (PADRÃO DIAMANTE R5-E)]
  ],
  footer: [
    #text(size: 8pt, fill: rgb("#64748b"), font: "Liberation Sans")[
      #grid(
        columns: (1fr, 1fr),
        [Suíte do Ecossistema Soberano · {sanitizar_typ(saas)}],
        align(right)[Fábrica Universal AIDD]
      )
    ]
  ]
)
#set text(font: "Liberation Sans", size: 9.5pt, lang: "pt")
#set par(justify: true, leading: 1.5em)

// CAPA EDITORIAL EXECUTIVA
#align(center + horizon)[
  #rect(stroke: 2pt + rgb("#0f172a"), inset: 24pt, radius: 4pt, width: 100%)[
    #text(size: 10pt, tracking: 0.2em, weight: "bold", fill: rgb("#00875A"))[FÁBRICA UNIVERSAL AIDD · TRATADO DE ENGENHARIA] \\
    #v(12pt)
    #text(size: 24pt, weight: "bold", fill: rgb("#0f172a"), font: "Liberation Serif")[{sanitizar_typ(titulo)}] \\
    #v(6pt)
    #text(size: 12pt, fill: rgb("#334155"))[{sanitizar_typ(subtitulo)}] \\
    #v(16pt)
    #line(length: 60%, stroke: 1pt + rgb("#cbd5e1"))
    #v(16pt)
    #text(size: 10pt, fill: rgb("#475569"))[
      *Macro-Ecossistema Alvo:* {sanitizar_typ(saas)} \\
      *Economia Anual Líquida:* #text(fill: rgb("#00875A"), weight: "bold")[{econ_liq}] \\
      *Padrão Normativo:* Diamante R5-E Tripartite \\
      *Publicação:* {datetime.date.today().strftime('%d/%m/%Y')} · 1ª Edição Oficial
    ]
  ]
]

#pagebreak()

// SUMÁRIO AUTOMÁTICO
#outline(title: [Sumário Geral do Livro-Texto], indent: auto)

#v(16pt)
#line(length: 100%, stroke: 0.5pt + rgb("#e2e8f0"))
#v(16pt)

= Prefácio Executivo & Manifesto da Soberania
{sanitizar_typ(deck)}

A migração de suítes de software proprietário fechado para ecossistemas open source auto-hospedados em VPS representa a maior alavanca de eficiência operacional da década. Este livro-texto reúne as especificações de engenharia para desmantelar a suíte *{sanitizar_typ(saas)}* com segurança jurídica, integridade de dados e autonomia digital irrestrita.

#pagebreak()

= Capítulo 1: Engenharia Financeira, TCO Global & Payback

#grid(
  columns: (1fr, 1fr),
  gutter: 10pt,
  rect(fill: rgb("#fef2f2"), stroke: 0.5pt + rgb("#fecaca"), inset: 10pt, radius: 2pt)[
    #text(size: 8pt, fill: rgb("#991b1b"), weight: "bold")[CUSTO SAAS ANUAL ({sanitizar_typ(saas)})] \\
    #text(size: 14pt, weight: "bold", fill: rgb("#dc2626"))[{custo_saas}]
  ],
  rect(fill: rgb("#f0fdf4"), stroke: 0.5pt + rgb("#bbf7d0"), inset: 10pt, radius: 2pt)[
    #text(size: 8pt, fill: rgb("#166534"), weight: "bold")[ECONOMIA LÍQUIDA ANUAL NO CAIXA] \\
    #text(size: 14pt, weight: "bold", fill: rgb("#16a34a"))[{econ_liq}]
  ]
)

#v(10pt)
- *Custo VPS Própria:* {custo_vps} (Cluster Consolidado 8 vCPU / 16 GB RAM)
- *Retorno sobre Investimento (ROI / Payback):* {roi}

#v(10pt)
== Desmembramento Contábil por Frente de Negócio

#table(
  columns: (1.5fr, 1.8fr, 1.2fr, 1.2fr, 0.9fr),
  fill: (x, y) => if y == 0 {{ rgb("#f1f5f9") }} else {{ none }},
  stroke: 0.5pt + rgb("#cbd5e1"),
  inset: 5pt,
  [*Grupo*], [*SaaS Alvo*], [*Custo SaaS*], [*Economia*], [*Margem*],
  { "".join([f"[{sanitizar_typ(dg.get('grupo'))}], [{sanitizar_typ(dg.get('saas_referencia'))}], [{sanitizar_typ(dg.get('custo_saas_anual'))}], [{sanitizar_typ(dg.get('economia_anual_liquida'))}], [{sanitizar_typ(dg.get('percentual_economia'))}],\n" for dg in econ.get("detalhamento_por_grupo", [])]) }
)

#pagebreak()

= Capítulo 2: Matriz Estratégica do Quinteto Soberano

#table(
  columns: (0.5fr, 1.3fr, 1.3fr, 1.8fr, 2.2fr, 1.3fr),
  fill: (x, y) => if y == 0 {{ rgb("#f1f5f9") }} else {{ none }},
  stroke: 0.5pt + rgb("#cbd5e1"),
  inset: 4pt,
  [*Nº*], [*Grupo*], [*Persona*], [*Ferramenta*], [*Substitui*], [*Economia*],
  { "".join([f"[{idx}], [{sanitizar_typ(p.get('nome_pilar').split(':')[0])}], [{simplificar_classificacao(f.get('classificacao',''))}], [*{sanitizar_typ(f['nome'])}*], [{sanitizar_typ(f['saas_substituido_direto'])}], [{sanitizar_typ(f['economia_anual_str'])}],\n" for idx, (p, f) in enumerate([(p_item, f_item) for p_item in pilares for f_item in p_item.get("ferramentas", [])], 1)]) }
)

{capitulos_pilares_typ}

#pagebreak()
= Capítulo 6: Camada de Cola, SSO Federado & Blueprints n8n

== Arquitetura de Interconexão sem Silos de Dados
- *Autenticação Única:* {sanitizar_typ(integracao.get('autenticacao_sso', ''))}
- *Barramento Assíncrono:* {sanitizar_typ(integracao.get('barramento_eventos', ''))}
- *Reverse Proxy & TLS:* {sanitizar_typ(integracao.get('gateway_reverse_proxy', ''))}

== Fluxo de Integração Operacional
{sanitizar_typ(integracao.get('fluxo_integracao_descricao', ''))}

#pagebreak()
= Capítulo 7: Manual de Engenharia de Infraestrutura & Deploy All-in-One

- *Segurança de Rede:* {sanitizar_typ(deploy.get('arquitetura_rede_seguranca', ''))}
- *Hardware Recomendado:* {sanitizar_typ(deploy.get('requisitos_hardware_totais', {}).get('cpu_total_recomendada', '8 vCPU'))} / {sanitizar_typ(deploy.get('requisitos_hardware_totais', {}).get('ram_total_recomendada', '16 GB RAM'))}

== Manifesto docker-compose.yml de Produção
```yaml
{deploy.get('docker_compose_exemplo', '')}
```

#pagebreak()
= Capítulo 8: Protocolos de Modularidade & Hot-Swap (Princípio do Lego)

- *Filosofia Desacoplada:* {sanitizar_typ(guia.get('filosofia_modular', ''))}

== Hot-Swap em Produção
{sanitizar_typ(guia.get('passo_a_passo_substituir_hotswap', ''))}

#pagebreak()
= Capítulo 9: Roteiro Prático de Migração de Dados Históricos

{ "".join([f"== {sanitizar_typ(m.get('modulo'))}\n- *O que migrar:* {sanitizar_typ(m.get('o_que_migrar'))}\n- *Cuidados:* {sanitizar_typ(m.get('cuidados'))}\n\n" for m in dados.get("guia_migracao_dados", [])]) }

#pagebreak()
= Capítulo 10: Governança Corporativa, Backup 3-2-1 & LGPD

- *Política 3-2-1:* {sanitizar_typ(seg.get('arquitetura_backup_321', ''))}

== Script de Backup Diário Criptografado
```bash
{seg.get('script_backup_diario', '')}
```

#pagebreak()
= Capítulo 11: Cronograma de Implantação em 30 Dias & Monitoramento

{ "".join([f"== {sanitizar_typ(c.get('semana'))} · {sanitizar_typ(c.get('fase'))}\n- *Atividades:* {sanitizar_typ(c.get('atividades'))}\n- *Marco de Entrega:* {sanitizar_typ(c.get('marco_entrega'))}\n\n" for c in dados.get("cronograma_implantacao_30_dias", [])]) }
"""
    return typ

def renderizar_fasciculo_html(titulo: str, subtitulo: str, tag: str, conteudo_body: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1" name="viewport"/>
<title>{titulo} · Suíte do Ecossistema Soberano</title>
<style>
{CSS_CANONICO_DIAMANTE}
</style>
</head>
<body>
<div class="wrap">
  <div style="margin-bottom: 20px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px;">
    <a href="../00-livro-mestre-compilado/LIVRO-ECOSSISTEMA-COMPLETO.html" style="font-family: var(--mono); font-size: 11.5px; color: var(--accent); text-decoration: none; font-weight: 700;">← Voltar ao Livro-Texto Completo</a>
    <span class="persona-badge">{tag}</span>
  </div>
  <header style="border-bottom: 1px solid var(--rule); padding-bottom: 20px; margin-bottom: 24px;">
    <div class="meta">
      <span>Fascículo Especializado · Fábrica Universal AIDD</span>
      <span>{datetime.date.today().strftime('%d/%m/%Y')}</span>
    </div>
    <h1 style="font-size: 30px; margin-bottom: 6px;">{titulo}</h1>
    <p class="deck" style="font-size: 14.5px; margin-bottom: 0;">{subtitulo}</p>
  </header>
  
  {conteudo_body}
  
  <footer style="margin-top: 40px; padding-top: 16px; border-top: 1px solid var(--rule-soft); display: flex; justify-content: space-between; align-items: center; font-family: var(--mono); font-size: 11px; color: var(--muted);">
    <span>Suíte do Ecossistema Soberano · Padrão Diamante R5-E</span>
    <a href="../00-livro-mestre-compilado/LIVRO-ECOSSISTEMA-COMPLETO.html" style="color: var(--accent); text-decoration: none; font-weight: 700;">Ver Livro Completo ↗</a>
  </footer>
</div>
{JS_CANONICO_DIAMANTE}
</body>
</html>
"""

def compilar_ecossistema_tripartite(slug: str):
    json_path = BASE_DIR / "scripts" / "data" / f"ecos-{slug}.json"
    if not json_path.exists():
        json_path = BASE_DIR / "scripts" / "data" / f"{slug}.json"
    if not json_path.exists():
        print(f"❌ Erro: Arquivo de dados do ecossistema não encontrado: {json_path}")
        sys.exit(1)

    print(f"\n🚀 Compilando Suíte do Macro-Ecossistema Tripartite: 'ecos-{slug}'")
    with open(json_path, "r", encoding="utf-8") as f:
        dados = json.load(f)

    out_dir = BASE_DIR / "output" / "04-ecossistemas" / f"ecos-{slug}"
    
    # Pastas da Arquitetura Modular
    dir_livro = out_dir / "00-livro-mestre-compilado"
    dir_exec = out_dir / "01-guias-executivos-e-estrategicos"
    dir_eng = out_dir / "02-guias-de-engenharia-e-infraestrutura"
    dir_ops = out_dir / "03-guias-de-integracao-e-operacao"
    dir_pilares = out_dir / "04-arsenal-dos-pilares"
    
    for d in [dir_livro, dir_exec, dir_eng, dir_ops, dir_pilares]:
        d.mkdir(parents=True, exist_ok=True)

    # 1. LIVRO COMPLETO (HTML, Markdown, PDF)
    html_livro = gerar_html_ecossistema_diamante(dados)
    md_livro = gerar_markdown_ecossistema(dados)
    typ_livro = gerar_typst_ecossistema(dados)

    # Salva no Livro Mestre
    with open(dir_livro / "LIVRO-ECOSSISTEMA-COMPLETO.html", "w", encoding="utf-8") as f:
        f.write(html_livro)
    with open(dir_livro / "LIVRO-ECOSSISTEMA-COMPLETO.md", "w", encoding="utf-8") as f:
        f.write(md_livro)
    
    typ_path = out_dir / f"ecos-{slug}.typ"
    with open(typ_path, "w", encoding="utf-8") as f:
        f.write(typ_livro)
    
    pdf_livro_path = dir_livro / "LIVRO-ECOSSISTEMA-COMPLETO.pdf"
    try:
        subprocess.run(["typst", "compile", str(typ_path), str(pdf_livro_path)], capture_output=True, text=True, check=True)
        print(f"   ✅ Livro-Texto Completo em PDF compilado: {pdf_livro_path.name}")
    except Exception as e:
        print(f"   ⚠️ Typst não encontrado ou falha no PDF: {e}")

    print(f"   ✅ 00. Livro Mestre Compilado gerado com sucesso!")

    # 2. FASCÍCULOS 01: EXECUTIVOS & ESTRATÉGICOS
    # 01. Dossiê Financeiro TCO
    econ = dados.get("analise_economica_global", {})
    body_tco = f"""
    <div class="tco-banner">
      <div class="tco-col"><div class="tco-lbl">Custo SaaS Anual</div><div class="tco-val killer">{econ.get('custo_saas_anual')}</div></div>
      <div class="tco-col"><div class="tco-lbl">Custo VPS Soberana</div><div class="tco-val">{econ.get('custo_vps_anual')}</div></div>
      <div class="tco-col"><div class="tco-lbl">Economia Líquida</div><div class="tco-val highlight">{econ.get('economia_anual_liquida')}</div></div>
      <div class="tco-col"><div class="tco-lbl">Payback Estimado</div><div class="tco-val highlight">{econ.get('roi_meses')}</div></div>
    </div>
    <h3 style="font-family: var(--font-serif); font-size: 20px; margin: 24px 0 10px; color: var(--ink);">🧮 Simulação Interativa</h3>
    <div class="calc-box">
      <div class="calc-grid">
        <div class="calc-slider-group"><label><span>Base de Leads</span> <strong id="val-leads" style="color: var(--accent);">50.000 leads</strong></label><input type="range" id="slider-leads" min="5000" max="200000" step="5000" value="50000"></div>
        <div class="calc-slider-group"><label><span>Vendedores</span> <strong id="val-sellers" style="color: var(--accent);">10 vendedores</strong></label><input type="range" id="slider-sellers" min="1" max="50" step="1" value="10"></div>
        <div class="calc-slider-group"><label><span>Atendentes WhatsApp</span> <strong id="val-agents" style="color: var(--accent);">10 atendentes</strong></label><input type="range" id="slider-agents" min="1" max="50" step="1" value="10"></div>
      </div>
      <div class="calc-results">
        <div><div class="stat-lbl">Custo SaaS Atual</div><div class="stat-val alert" id="calc-saas-total">R$ 114.000/ano</div></div>
        <div><div class="stat-lbl">Custo VPS Própria</div><div class="stat-val" id="calc-vps-total">R$ 4.200/ano</div></div>
        <div><div class="stat-lbl">Economia no Caixa</div><div class="stat-val highlight" id="calc-savings-total">R$ 109.800/ano (96.3%)</div></div>
      </div>
    </div>
    """
    with open(dir_exec / "01-dossie-financeiro-tco-e-calculadora.html", "w", encoding="utf-8") as f:
        f.write(renderizar_fasciculo_html("Dossiê Financeiro de TCO & Calculadora", "Análise de ROI, Payback e Desmantelamento de Licenças SaaS", "Financeiro & CFO", body_tco))

    # 02. Matriz Geral do Quinteto
    pilares = dados.get("pilares", [])
    linhas_tab = ""
    grank = 1
    for p in pilares:
        for f_item in p.get("ferramentas", []):
            c_simp = simplificar_classificacao(f_item.get('classificacao', ''))
            linhas_tab += f"<tr><td class='rank'>{grank:02d}</td><td><strong>{p.get('nome_pilar').split(':')[0]}</strong></td><td>{c_simp}</td><td><strong>{f_item['nome']}</strong></td><td class='saas'>{f_item['saas_substituido_direto']}</td><td class='econ'>{f_item['economia_anual_str']}</td><td><a href='{f_item['repositorio_github']}' target='_blank' style='color: var(--accent); font-family: var(--mono); font-size: 11px; text-decoration: none; font-weight: 700;'>GitHub ↗</a></td></tr>"
            grank += 1
    body_matriz = f"""
    <div style="margin: 16px 0 12px;"><input type="text" id="busca-ferramentas" placeholder="Buscar ferramenta..." style="width: 100%; padding: 10px 14px; border: 1px solid var(--rule); border-radius: 2px; background: var(--surface-2); color: var(--ink);"></div>
    <div class="tablewrap"><table><thead><tr><th>#</th><th>Grupo</th><th>Classificação</th><th>Ferramenta</th><th>Substitui</th><th>Economia</th><th>Código</th></tr></thead><tbody>{linhas_tab}</tbody></table></div>
    """
    with open(dir_exec / "02-matriz-geral-e-quinteto-soberano.html", "w", encoding="utf-8") as f:
        f.write(renderizar_fasciculo_html("Matriz Geral do Quinteto Soberano", "Visão Consolidada das 15 Ferramentas Open Source dos 3 Grupos", "Estratégico", body_matriz))

    # 03. Cronograma 30 Dias
    body_cron = "".join([f'<div class="timeline-card"><div style="display: flex; justify-content: space-between;"><h4>{c.get("semana")} · {c.get("fase")}</h4><span class="persona-badge">Etapa</span></div><p style="font-size: 13.5px; margin: 4px 0 6px;">{c.get("atividades")}</p><div style="font-family: var(--mono); font-size: 12px; color: var(--green); font-weight: 700;">🎯 Marco: {c.get("marco_entrega")}</div></div>' for c in dados.get("cronograma_implantacao_30_dias", [])])
    with open(dir_exec / "03-cronograma-de-implantacao-30-dias.html", "w", encoding="utf-8") as f:
        f.write(renderizar_fasciculo_html("Cronograma Executivo de Implementação em 30 Dias", "Roadmap Semana a Semana para Virada de Chave sem Downtime", "Gestão de Projetos", body_cron))

    # 3. FASCÍCULOS 02: ENGENHARIA & INFRAESTRUTURA
    deploy = dados.get("deploy_consolidado", {})
    body_deploy = f"""
    <div class="racional-box"><p><strong>🛡️ Rede &amp; Segurança:</strong> {deploy.get('arquitetura_rede_seguranca')}</p></div>
    <h3 style="font-family: var(--font-serif); font-size: 20px; margin: 20px 0 10px;">Arquivo docker-compose.yml Completo</h3>
    <div class="code-box" style="margin-bottom: 20px;"><pre><code>{deploy.get('docker_compose_exemplo')}</code></pre></div>
    <h3 style="font-family: var(--font-serif); font-size: 20px; margin: 20px 0 10px;">Passos de Subida</h3>
    <div class="steps-grid">{''.join([f'<div class="step-card"><div class="step-head"><span class="step-badge">0{idx}</span> {passo.get("titulo")}</div><p>{passo.get("descricao")}</p></div>' for idx, passo in enumerate(deploy.get("passos_deploy", []), 1)])}</div>
    """
    with open(dir_eng / "04-manual-deploy-all-in-one-docker-compose.html", "w", encoding="utf-8") as f:
        f.write(renderizar_fasciculo_html("Manual de Deploy All-in-One", "Orquestração Unificada da Stack em Docker Compose para VPS", "DevOps & Infra", body_deploy))

    guia = dados.get("guia_modularidade_e_expansao", {})
    body_lego = f"""
    <div class="racional-box"><p><strong>🧩 Princípio das Tomadas:</strong> {guia.get('filosofia_modular')}</p></div>
    <h3 style="font-family: var(--font-serif); font-size: 20px; margin: 20px 0 10px;">1. Adicionar Nova Ferramenta</h3>
    <div class="steps-grid">{''.join([f'<div class="step-card"><div class="step-head">{p_add.get("etapa")}</div><p>{p_add.get("descricao")}</p></div>' for p_add in guia.get("passos_adicionar_ferramenta", [])])}</div>
    <h3 style="font-family: var(--font-serif); font-size: 20px; margin: 24px 0 10px;">2. Hot-Swap (Troca sem Parar a Operação)</h3>
    <div class="integ-card"><p style="white-space: pre-line;">{guia.get('passo_a_passo_substituir_hotswap')}</p></div>
    <h3 style="font-family: var(--font-serif); font-size: 20px; margin: 24px 0 10px;">3. Remoção Segura</h3>
    <div class="integ-card"><p style="white-space: pre-line;">{guia.get('passo_a_passo_remover_ferramenta')}</p></div>
    """
    with open(dir_eng / "05-guia-modularidade-e-hot-swap-lego.html", "w", encoding="utf-8") as f:
        f.write(renderizar_fasciculo_html("Guia de Modularidade & Hot-Swap", "Protocolo para Adicionar, Trocar e Remover Serviços sem Quebrar o Cluster", "Engenharia", body_lego))

    mon = dados.get("monitoramento_e_saude_vps", {})
    body_mon = f"""
    <h3 style="font-family: var(--font-serif); font-size: 20px; margin: 16px 0 10px;">Comandos de Diagnóstico em 1 Clique</h3>
    {''.join([f'<div style="display: flex; justify-content: space-between; padding: 8px 12px; background: var(--surface-2); border: 1px solid var(--rule-soft); border-radius: 2px; margin-bottom: 6px;"><code>{c.get("comando")}</code><span style="font-size: 12.5px; color: var(--muted);">{c.get("finalidade")}</span></div>' for c in mon.get("comandos_diagnostico_1clique", [])])}
    <h3 style="font-family: var(--font-serif); font-size: 20px; margin: 24px 0 10px;">Métricas Críticas de Alerta</h3>
    <div class="integration-grid">{''.join([f'<div class="stat-card"><div class="stat-lbl">{met.get("metrica")}</div><div style="font-family: var(--mono); font-size: 12px; color: var(--flag); font-weight: 700;">{met.get("limite_alerta")}</div><p style="margin: 0; font-size: 12px; color: var(--ink-2);"><strong>Ação:</strong> {met.get("acao_recomendada")}</p></div>' for met in mon.get("metricas_alerta", [])])}</div>
    """
    with open(dir_eng / "06-painel-monitoramento-e-health-check.html", "w", encoding="utf-8") as f:
        f.write(renderizar_fasciculo_html("Painel de Monitoramento & Health Check", "Diagnóstico Operacional em Tempo Real e Gestão de Incidentes", "Operações TI", body_mon))

    # 4. FASCÍCULOS 03: INTEGRAÇÃO & OPERAÇÃO
    body_blueprints = "".join([f'<div class="blueprint-card"><div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;"><h4>{bp.get("nome")}</h4><span class="persona-badge">JSON Pronto</span></div><p style="font-size: 13.5px; margin: 0 0 10px;">{bp.get("descricao")}</p><div class="code-box"><pre><code>{bp.get("json_blueprint")}</code></pre></div></div>' for bp in dados.get("blueprints_n8n", [])])
    with open(dir_ops / "07-blueprints-n8n-e-orquestracao-eventos.html", "w", encoding="utf-8") as f:
        f.write(renderizar_fasciculo_html("Blueprints n8n & Orquestração de Eventos", "Templates de Automação em JSON Prontos para Importação Instantânea", "Automação / Ops", body_blueprints))

    body_mig = "".join([f'<div class="integ-card" style="margin-bottom: 14px;"><h4>{m.get("modulo")}</h4><p><strong>O que migrar:</strong> {m.get("o_que_migrar")}</p><div class="steps-grid" style="margin: 10px 0;">{"".join([f"<div class=\"step-card\"><div class=\"step-head\">Etapa {idx}</div><p>{p}</p></div>" for idx, p in enumerate(m.get("passos", []), 1)])}</div><div style="background: var(--flag-soft); border-left: 3px solid var(--flag); padding: 8px 12px; font-size: 12.5px; color: var(--flag);"><strong>⚠️ Atenção:</strong> {m.get("cuidados")}</div></div>' for m in dados.get("guia_migracao_dados", [])])
    with open(dir_ops / "08-roteiro-migracao-dados-de-saas.html", "w", encoding="utf-8") as f:
        f.write(renderizar_fasciculo_html("Roteiro Prático de Migração de Dados", "Passo a Passo para Exportar do SaaS e Importar na Stack Soberana", "Migração de Dados", body_mig))

    seg = dados.get("seguranca_backup_lgpd", {})
    body_seg = f"""
    <div class="racional-box"><p><strong>🛡️ Política 3-2-1:</strong> {seg.get('arquitetura_backup_321')}</p></div>
    <h3 style="font-family: var(--font-serif); font-size: 20px; margin: 20px 0 10px;">Script de Backup Diário Criptografado</h3>
    <div class="code-box" style="margin-bottom: 20px;"><pre><code>{seg.get('script_backup_diario')}</code></pre></div>
    <h3 style="font-family: var(--font-serif); font-size: 20px; margin: 24px 0 10px;">Checklist de Conformidade LGPD</h3>
    {''.join([f'<div class="stat-card" style="margin-bottom: 8px;"><div style="display: flex; justify-content: space-between;"><strong>{chk.get("item")}</strong><span class="econ-badge" style="font-size: 9.5px;">Conforme</span></div><p style="margin: 0; font-size: 12.5px;">{chk.get("status")}</p></div>' for chk in seg.get("checklist_conformidade_lgpd", [])])}
    """
    with open(dir_ops / "09-seguranca-backup-321-e-conformidade-lgpd.html", "w", encoding="utf-8") as f:
        f.write(renderizar_fasciculo_html("Segurança, Backup 3-2-1 & LGPD", "Governança Corporativa de Dados e Script Automatizado de Proteção", "DPO & Compliance", body_seg))

    # 5. FASCÍCULOS 04: ARSENAL DOS PILARES (INDIVIDUAIS)
    for p_idx, p in enumerate(pilares, 1):
        entries_single_pilar = ""
        for f_item in p.get("ferramentas", []):
            c_simp = simplificar_classificacao(f_item.get('classificacao', ''))
            passos_html = "".join([f'<div class="step-card"><div class="step-head"><span class="step-badge">{idx}</span> {passo.get("titulo")}</div><p>{passo.get("descricao")}</p></div>' for idx, passo in enumerate(f_item.get("passos_praticos", []), 1)])
            ds = f_item.get("design_system", {})
            mcp_html = "".join([f'<div class="mcp-card"><div class="mcp-top"><span class="mcp-pill">{m.get("tipo")}</span><span class="mcp-name">{m.get("nome")}</span></div><p>{m.get("descricao")}</p><div class="mcp-cmd"><code>{m.get("comando_ou_repo")}</code></div></div>' for m in f_item.get("uso_complementar", [])])
            
            entries_single_pilar += f"""
            <article class="entry" id="{f_item['slug']}">
              <div class="entry-rank">{f_item['rank']:02d}</div>
              <div class="entry-body">
                <div class="entry-top">
                  <h3>{f_item['nome']} · {f_item['subtitulo']}</h3>
                  <span class="persona-badge">Persona: {c_simp}</span>
                  <span class="killer-badge">Substitui: {f_item['saas_substituido_direto']}</span>
                  <span class="econ-badge">{f_item['economia_anual_str']}</span>
                  <span class="lic-badge">{f_item['licenca_osi']}</span>
                </div>
                <div class="entry-section"><div class="label">1. O Que Faz &amp; Como Funciona</div><p>{f_item['o_que_faz']} {f_item['como_funciona']}</p><div class="code-box"><pre><code>{f_item['comando_rapido']}</code></pre></div></div>
                <div class="entry-section"><div class="label">2. Análise Econômica &amp; Racional</div><div class="econ-grid"><div class="econ-card killer"><span class="econ-lbl">SaaS Substituído</span><span class="econ-val">{f_item['saas_substituido_direto']}</span></div><div class="econ-card savings"><span class="econ-lbl">Economia</span><span class="econ-val">{f_item['economia_anual_str']}</span></div><div class="econ-card" style="grid-column: 1 / -1;"><span class="econ-lbl">Racional</span><p style="font-size: 13px; margin: 4px 0 0;">{f_item['racional_escolha']}</p></div></div></div>
                <div class="entry-section"><div class="label">3. Infraestrutura &amp; Veredito</div><div class="infra-grid"><div class="infra-card"><span class="infra-lbl">RAM</span><span class="infra-val">{f_item.get('requisitos_infra', {}).get('ram_minima', '1 GB')}</span></div><div class="infra-card"><span class="infra-lbl">Docker</span><span class="infra-val"><code>{f_item.get('requisitos_infra', {}).get('docker_image', 'oficial')}</code></span></div><div class="infra-card verdict"><span class="infra-lbl">Veredito</span><p style="font-size: 13px; margin: 4px 0 0;">{f_item.get('veredito')}</p></div></div></div>
                <div class="entry-section"><div class="label">4. Guia Prático em 3 Passos</div><div class="steps-grid">{passos_html}</div></div>
                <div class="entry-section"><div class="label">5. White-Label</div><div class="ds-grid"><div class="ds-card"><span class="ds-lbl">Mecânica</span><p>{ds.get('mecanica_customizacao')}</p></div><div class="ds-card"><span class="ds-lbl">Manutenção</span><p>{ds.get('manutenibilidade_tema')}</p></div></div></div>
                <div class="entry-section"><div class="label">6. Ecossistema Agêntico &amp; MCPs</div><div class="mcp-grid">{mcp_html}</div></div>
              </div>
            </article>
            """
        
        pilar_slug = p.get("pilar_id", f"pilar-0{p_idx}")
        with open(dir_pilares / f"{pilar_slug}.html", "w", encoding="utf-8") as f:
            f.write(renderizar_fasciculo_html(f"{p.get('nome_pilar')}", f"Arsenal do Quinteto Soberano para {p.get('modulo_saas_alvo')} · Subtotal: {p.get('subtotal_economia_anual')}", f"Pilar 0{p_idx}", f'<div class="ledger">{entries_single_pilar}</div>'))

    print(f"   ✅ Todos os 10 Fascículos Especializados e Pilares individuais foram compilados com sucesso!")

    # 4. Registro no SQLite (Regra R11)
    try:
        registrar_ecossistema({
            "slug": f"ecos-{slug}",
            "nome_ecossistema": dados.get("nome_ecossistema", slug),
            "titulo": dados.get("titulo", ""),
            "saas_substituido": dados.get("saas_substituido", ""),
            "total_pilares": dados.get("stats", {}).get("total_pilares", len(dados.get("pilares", []))),
            "total_ferramentas": dados.get("stats", {}).get("total_ferramentas", sum(len(p.get("ferramentas", [])) for p in dados.get("pilares", []))),
            "economia_anual_liquida": dados.get("analise_economica_global", {}).get("economia_anual_liquida", ""),
            "caminho_html": f"output/04-ecossistemas/ecos-{slug}/00-livro-mestre-compilado/LIVRO-ECOSSISTEMA-COMPLETO.html",
            "caminho_md": f"output/04-ecossistemas/ecos-{slug}/00-livro-mestre-compilado/LIVRO-ECOSSISTEMA-COMPLETO.md",
            "caminho_pdf": f"output/04-ecossistemas/ecos-{slug}/00-livro-mestre-compilado/LIVRO-ECOSSISTEMA-COMPLETO.pdf"
        })
        print(f"💾 Suíte do Ecossistema persistida com sucesso no SQLite (estado_esteira.db - Regra R11)")
    except Exception as e:
        print(f"⚠️ Erro ao registrar ecossistema no SQLite: {e}")

    print(f"🏆 COMPILAÇÃO TRIPARTITE DA SUÍTE CONCLUÍDA: {out_dir}")
    return True

def main():
    parser = argparse.ArgumentParser(description="Compilador Tripartite de Macro-Ecossistemas (Fluxo 4)")
    parser.add_argument("--ecossistema", "--slug", dest="slug", required=True, help="Slug do macro-ecossistema (ex: rd-station-suite)")
    args = parser.parse_args()
    slug_limpo = args.slug.replace("ecos-", "")
    compilar_ecossistema_tripartite(slug_limpo)

if __name__ == "__main__":
    main()
