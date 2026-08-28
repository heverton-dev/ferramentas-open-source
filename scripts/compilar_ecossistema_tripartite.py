# -*- coding: utf-8 -*-
"""
COMPILADOR TRIPARTITE DE MACRO-ECOSSISTEMAS SAAS (FLUXO 4 - PADRÃO DIAMANTE R5-E & QUINTETO SOBERANO)
Gera o HTML final, Markdown denso e PDF Typst com 100% de paridade de design aos Fluxos 1, 2 e 3.
Estrutura completa com 10 macro-seções de alto valor:
1. Demonstrativo Financeiro Consolidado, Análise de TCO Global & Calculadora Interativa de Payback
2. Matriz Geral do Quinteto Soberano por Grupo (Pilha Aberta Integrada)
3. Arsenal Tecnológico & Fichas Técnicas do Quinteto Soberano (15 ferramentas completas)
4. Camada de Cola & Orquestração (SSO, Traefik, Barramento & Blueprints n8n em JSON)
5. Deploy All-in-One: Guia Passo a Passo para Não-Técnicos (Analogias, Stack & Compose)
6. Guia Operacional de Modularidade, Expansão & Hot-Swap (Princípio do Lego & FAQ)
7. Roteiro Prático de Migração de Dados (De-SaaS para Soberano)
8. Segurança Corporativa, Backup 3-2-1 & Conformidade LGPD
9. Cronograma Executivo de Implementação em 30 Dias (Roadmap de 4 semanas)
10. Painel de Monitoramento & Health Check da VPS (Diagnóstico em 1 clique)
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

  header {
    border-bottom: 2px solid var(--ink);
    padding-bottom: 32px;
    margin-bottom: 36px;
  }

  .meta {
    font-family: var(--mono);
    font-size: 11px;
    letter-spacing: .12em;
    text-transform: uppercase;
    color: var(--accent);
    margin-bottom: 12px;
    font-weight: 700;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 8px;
  }

  h1 {
    font-family: var(--font-serif);
    font-size: 38px;
    line-height: 1.15;
    margin: 0 0 12px 0;
    font-weight: 700;
    letter-spacing: -.02em;
    color: var(--ink);
  }

  .deck {
    font-size: 16px;
    color: var(--ink-2);
    margin: 0 0 24px 0;
    line-height: 1.55;
    max-width: 95%;
  }

  .stats-bar {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
    gap: 16px;
    border-top: 1px solid var(--rule-soft);
    padding-top: 20px;
    margin-top: 20px;
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
    border-left: 3px solid var(--accent);
    padding: 14px 18px;
    margin: 20px 0;
    font-size: 14px;
    color: var(--ink-2);
    border-radius: 0 2px 2px 0;
  }

  .sec-head {
    margin: 44px 0 20px;
    padding-bottom: 12px;
    border-bottom: 1px solid var(--rule);
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    flex-wrap: wrap;
    gap: 12px;
  }

  .sec-info { flex: 1; }
  .sec-num { font-family: var(--mono); font-size: 11px; text-transform: uppercase; color: var(--accent); font-weight: 700; letter-spacing: .08em; }
  .sec-head h2 { font-family: var(--font-serif); font-size: 26px; margin: 4px 0 0 0; color: var(--ink); font-weight: 600; }
  .sec-note { font-size: 13.5px; color: var(--muted); margin-top: 4px; }
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

function copyToClipboard(text) {
  navigator.clipboard.writeText(text).then(() => {
    alert('✅ Código copiado para a área de transferência!');
  });
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
        f"# {titulo}",
        f"",
        f"> **Macro-Ecossistema SaaS Desmantelado:** {saas}  ",
        f"> **Data de Emissão:** {datetime.date.today().strftime('%d/%m/%Y')} | **Padrão:** Diamante R5-E Tripartite",
        f"",
        f"## Resumo Executivo",
        f"{deck}",
        f"",
        f"---",
        f"",
        f"## 1. Demonstrativo Financeiro Consolidado (TCO Global & Payback)",
        f"",
        f"- **Custo SaaS Anual:** {econ.get('custo_saas_anual', '')}",
        f"- **Custo VPS Soberana (Cluster Unificado):** {econ.get('custo_vps_anual', '')}",
        f"- **Economia Líquida Anual:** {econ.get('economia_anual_liquida', '')}",
        f"- **Payback / ROI:** {econ.get('roi_meses', '')}",
        f"",
        f"### Desmembramento Financeiro por Grupo",
        f"| Grupo | SaaS de Referência | Custo SaaS Anual | Custo VPS Alocado | Economia Líquida Anual | Economia (%) |",
        f"|---|---|---|---|---|---|"
    ]

    for dg in econ.get("detalhamento_por_grupo", []):
        linhas.append(f"| {dg.get('grupo')} | {dg.get('saas_referencia')} | {dg.get('custo_saas_anual')} | {dg.get('custo_vps_alocado')} | {dg.get('economia_anual_liquida')} | {dg.get('percentual_economia')} |")

    linhas.extend([
        f"",
        f"---",
        f"",
        f"## 2. Matriz Geral do Quinteto Soberano por Grupo",
        f"",
        f"| # | Grupo / Pilar | Classificação | Ferramenta | Módulo SaaS Substituído | Economia Anual | Código |",
        f"|---|---|---|---|---|---|---|"
    ])

    global_rank = 1
    for p in pilares:
        for f in p.get("ferramentas", []):
            c_simp = simplificar_classificacao(f.get('classificacao', ''))
            linhas.append(f"| {global_rank:02d} | {p.get('nome_pilar').split(':')[0]} | {c_simp} | **{f['nome']}** | {f['saas_substituido_direto']} | {f['economia_anual_str']} | [GitHub]({f['repositorio_github']}) |")
            global_rank += 1

    linhas.extend([
        f"",
        f"---",
        f"",
        f"## 3. Arsenal Tecnológico & Fichas Técnicas do Quinteto Soberano",
        f""
    ])

    for p in pilares:
        linhas.extend([
            f"### Pilar: {p.get('nome_pilar')} (Alvo: {p.get('modulo_saas_alvo')})",
            f"*{p.get('descricao_pilar')}* - **Subtotal de Economia: {p.get('subtotal_economia_anual')}**",
            f""
        ])
        for f in p.get("ferramentas", []):
            c_simp = simplificar_classificacao(f.get('classificacao', ''))
            linhas.extend([
                f"#### {f['rank']:02d}. {f['nome']} · {f['subtitulo']} (Persona: {c_simp})",
                f"- **Substitui:** `{f['saas_substituido_direto']}` | **Economia:** `{f['economia_anual_str']}` | **Licença:** `{f['licenca_osi']}`",
                f"- **O Que Faz:** {f['o_que_faz']}",
                f"- **Como Funciona:** {f['como_funciona']}",
                f"- **Comando Rápido:** `{f['comando_rapido']}`",
                f"- **Veredito Técnico:** {f['veredito']}",
                f"- **Repositório:** {f['repositorio_github']}",
                f""
            ])

    linhas.extend([
        f"---",
        f"",
        f"## 4. Camada de Cola & Orquestração (SSO, Traefik & Blueprints n8n)",
        f"",
        f"- **🔑 Autenticação Única (SSO):** {integracao.get('autenticacao_sso')}",
        f"- **⚡ Barramento de Eventos:** {integracao.get('barramento_eventos')}",
        f"- **🛡️ Reverse Proxy:** {integracao.get('gateway_reverse_proxy')}",
        f"",
        f"### Blueprints de Workflows Prontos para n8n",
        f""
    ])

    for bp in dados.get("blueprints_n8n", []):
        linhas.extend([
            f"#### {bp.get('nome')}",
            f"- *Descrição:* {bp.get('descricao')}",
            f"- *Gatilho:* `{bp.get('gatilho')}`",
            f"```json",
            f"{bp.get('json_blueprint')}",
            f"```",
            f""
        ])

    linhas.extend([
        f"---",
        f"",
        f"## 5. Deploy All-in-One: Guia Passo a Passo para Não-Técnicos",
        f"",
        f"### 💡 Entendendo os 4 Pilares da Infraestrutura (Sem Jargões)",
        f"- **1. O que é VPS?** {deploy.get('analogia_didatica_stack', {}).get('o_que_e_vps', '')}",
        f"- **2. O que é Docker Compose?** {deploy.get('analogia_didatica_stack', {}).get('o_que_e_docker', '')}",
        f"- **3. O que é Traefik?** {deploy.get('analogia_didatica_stack', {}).get('o_que_e_traefik', '')}",
        f"- **4. O que é n8n?** {deploy.get('analogia_didatica_stack', {}).get('o_que_e_n8n', '')}",
        f"",
        f"> **Topologia & Segurança de Rede:** {deploy.get('arquitetura_rede_seguranca', '')}",
        f"",
        f"### Composição Detalhada da Stack de Infraestrutura",
        f""
    ])

    for s in stack_detalhe:
        linhas.extend([
            f"- **{s.get('servico')}** (`{s.get('imagem_docker')}`):",
            f"  - *Papel:* {s.get('papel_na_stack')}",
            f"  - *Por que foi escolhido:* {s.get('racional_escolha')}",
            f"  - *Portas & Exposição:* {s.get('portas_expostas')}",
            f"  - *Persistência:* `{s.get('persistencia')}`",
            f""
        ])

    linhas.extend([
        f"**Dimensionamento de Hardware Total:**",
        f"- RAM Recomendada: {deploy.get('requisitos_hardware_totais', {}).get('ram_total_recomendada')}",
        f"- CPU Recomendada: {deploy.get('requisitos_hardware_totais', {}).get('cpu_total_recomendada')}",
        f"- Armazenamento: {deploy.get('requisitos_hardware_totais', {}).get('armazenamento_minimo')}",
        f"",
        f"### Arquivo `docker-compose.yml` Consolidado",
        f"```yaml",
        f"{deploy.get('docker_compose_exemplo', '')}",
        f"```",
        f"",
        f"### Roteiro de Instalação Rápida (4 Passos Simples)",
        f""
    ])

    for idx, passo in enumerate(deploy.get("passos_deploy", []), 1):
        linhas.append(f"{idx}. **{passo.get('titulo')}:** {passo.get('descricao')}")

    linhas.extend([
        f"",
        f"---",
        f"",
        f"## 6. Guia de Modularidade, Expansão & Hot-Swap de Ferramentas (Princípio do Lego)",
        f"",
        f"> **O Princípio das Tomadas Independentes:**  ",
        f"> {guia.get('filosofia_modular', '')}",
        f"",
        f"### Como Adicionar uma Nova Ferramenta ao Ecossistema (Plug-and-Play)",
        f"{guia.get('passo_a_passo_adicionar_ferramenta', '')}",
        f"",
        f"### Como Substituir uma Ferramenta em Produção (Hot-Swap sem Parar o Negócio)",
        f"{guia.get('passo_a_passo_substituir_hotswap', '')}",
        f"",
        f"### Como Remover um Módulo com Segurança",
        f"{guia.get('passo_a_passo_remover_ferramenta', '')}",
        f"",
        f"### Estudo de Caso Prático: {guia.get('exemplo_caso_pratico_hotswap', {}).get('cenario', '')}",
        f"- **1. Isolamento:** {guia.get('exemplo_caso_pratico_hotswap', {}).get('passo_1_isolamento')}",
        f"- **2. Novo Serviço:** {guia.get('exemplo_caso_pratico_hotswap', {}).get('passo_2_novo_servico')}",
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
        f"## 7. Roteiro Prático de Migração de Dados (De-SaaS para Soberano)",
        f""
    ])

    for mig in dados.get("guia_migracao_dados", []):
        linhas.extend([
            f"### {mig.get('modulo')}",
            f"- **O que migrar:** {mig.get('o_que_migrar')}",
            f"- **Passos:**"
        ])
        for p in mig.get("passos", []):
            linhas.append(f"  1. {p}")
        linhas.extend([
            f"- **⚠️ Cuidados:** {mig.get('cuidados')}",
            f""
        ])

    seg = dados.get("seguranca_backup_lgpd", {})
    linhas.extend([
        f"---",
        f"",
        f"## 8. Segurança Corporativa, Backup 3-2-1 & Conformidade LGPD",
        f"",
        f"> **Arquitetura 3-2-1:** {seg.get('arquitetura_backup_321')}",
        f"",
        f"### Script de Backup Diário Automatizado",
        f"```bash",
        f"{seg.get('script_backup_diario')}",
        f"```",
        f"",
        f"### Checklist de Conformidade LGPD",
        f""
    ])

    for chk in seg.get("checklist_conformidade_lgpd", []):
        linhas.append(f"- **{chk.get('item')}:** {chk.get('status')}")

    linhas.extend([
        f"",
        f"---",
        f"",
        f"## 9. Cronograma Executivo de Implementação em 30 Dias",
        f""
    ])

    for cron in dados.get("cronograma_implantacao_30_dias", []):
        linhas.extend([
            f"### {cron.get('semana')} · {cron.get('fase')}",
            f"- **Atividades:** {cron.get('atividades')}",
            f"- **🎯 Marco de Entrega:** {cron.get('marco_entrega')}",
            f""
        ])

    mon = dados.get("monitoramento_e_saude_vps", {})
    linhas.extend([
        f"---",
        f"",
        f"## 10. Painel de Monitoramento & Health Check da VPS",
        f"",
        f"> **Painel Recomendado:** {mon.get('painel_recomendado')}",
        f"",
        f"### Comandos de Diagnóstico em 1 Clique",
        f""
    ])

    for cmd in mon.get("comandos_diagnostico_1clique", []):
        linhas.append(f"- `{cmd.get('comando')}`: {cmd.get('finalidade')}")

    linhas.extend([
        f"",
        f"### Métricas de Alerta & Ações Recomendadas",
        f""
    ])

    for met in mon.get("metricas_alerta", []):
        linhas.append(f"- **{met.get('metrica')}** ({met.get('limite_alerta')}): {met.get('acao_recomendada')}")

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
        <div class="sec-head">
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

    # BLUEPRINTS N8N
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

    # GUIA MIGRAÇÃO DE DADOS
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

    # SEGURANÇA, BACKUP & LGPD
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

    # CRONOGRAMA 30 DIAS
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

    # MONITORAMENTO & HEALTH CHECK
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
<title>{titulo} · Dossiê de Macro-Ecossistema Soberano</title>
<style>
{CSS_CANONICO_DIAMANTE}
</style>
</head>
<body>
<div class="wrap">
  <header>
    <div class="meta">
      <span>Macro-Ecossistema Soberano · Padrão Diamante R5-E</span>
      <span>Fábrica Universal AIDD · {datetime.date.today().strftime('%d/%m/%Y')}</span>
    </div>
    <h1>{titulo}</h1>
    <p class="deck">{deck}</p>
    
    <div class="stats-bar">
      <div class="stat-card">
        <div class="stat-lbl">Pilares de Negócio</div>
        <div class="stat-val">{stats.get('total_pilares', 3)} Grupos</div>
      </div>
      <div class="stat-card">
        <div class="stat-lbl">Arsenal Total</div>
        <div class="stat-val highlight">{stats.get('total_ferramentas', 15)} Ferramentas</div>
      </div>
      <div class="stat-card">
        <div class="stat-lbl">Economia Média</div>
        <div class="stat-val highlight">{stats.get('economia_media', '96%')}</div>
      </div>
      <div class="stat-card">
        <div class="stat-lbl">SaaS Desmantelado</div>
        <div class="stat-val alert">{saas}</div>
      </div>
      <div class="stat-card">
        <div class="stat-lbl">Licenças OSI</div>
        <div class="stat-val">{stats.get('licencas_osi', '100% OSI')}</div>
      </div>
    </div>
  </header>

  <!-- SEÇÃO 01: TCO & CALCULADORA -->
  <div class="sec-head">
    <div class="sec-info">
      <span class="sec-num">Seção 01 · Demonstrativo Financeiro Consolidado</span>
      <h2>Análise de TCO Global &amp; Calculadora Interativa de Payback</h2>
      <p class="sec-note">Demonstrativo comparativo de desmantelamento de custos de licenças de software.</p>
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

  <h3 style="font-family: var(--font-serif); font-size: 20px; margin: 24px 0 10px; color: var(--ink);">🧮 Simule a Economia da sua Empresa em Tempo Real</h3>
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
  <div class="sec-head">
    <div class="sec-info">
      <span class="sec-num">Seção 02 · Matriz Geral do Quinteto Soberano por Grupo</span>
      <h2>Pilha Aberta Integrada</h2>
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
  <div class="sec-head">
    <div class="sec-info">
      <span class="sec-num">Seção 03 · Arsenal Tecnológico &amp; Fichas Técnicas</span>
      <h2>Quinteto Soberano por Grupo Funcional</h2>
      <p class="sec-note">Especificação de engenharia completa para cada uma das 15 ferramentas do macro-ecossistema.</p>
    </div>
  </div>

  {pilares_conteudo}

  <!-- SEÇÃO 04: INTEGRAÇÃO & BLUEPRINTS -->
  <div class="sec-head">
    <div class="sec-info">
      <span class="sec-num">Seção 04 · Camada de Cola &amp; Orquestração</span>
      <h2>Integração, SSO &amp; Blueprints n8n</h2>
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
  <div class="sec-head">
    <div class="sec-info">
      <span class="sec-num">Seção 05 · Deploy All-in-One: Guia Passo a Passo para Não-Técnicos</span>
      <h2>Como o Sistema Funciona &amp; Roteiro de Subida Plug-and-Play</h2>
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
  <div class="sec-head" style="margin-top: 48px;">
    <div class="sec-info">
      <span class="sec-num">Seção 06 · Guia de Modularidade, Expansão &amp; Hot-Swap</span>
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
  <div class="sec-head" style="margin-top: 48px;">
    <div class="sec-info">
      <span class="sec-num">Seção 07 · Guia de Migração de Dados Históricos</span>
      <h2>De-SaaS para Soberano (Transição Segura sem Perdas)</h2>
      <p class="sec-note">Roteiro passo a passo para exportar dados do RD Station e importar no Mautic, Twenty e Chatwoot.</p>
    </div>
  </div>
  {migracao_cards_html}

  <!-- SEÇÃO 08: SEGURANÇA & LGPD -->
  <div class="sec-head" style="margin-top: 48px;">
    <div class="sec-info">
      <span class="sec-num">Seção 08 · Governança, Backup 3-2-1 &amp; LGPD</span>
      <h2>Soberania de Dados &amp; Proteção Corporativa</h2>
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

  <!-- SEÇÃO 09: CRONOGRAMA 30 DIAS -->
  <div class="sec-head" style="margin-top: 48px;">
    <div class="sec-info">
      <span class="sec-num">Seção 09 · Plano Executivo de Implementação</span>
      <h2>Cronograma de 30 Dias para Virada de Chave</h2>
      <p class="sec-note">Planejamento semana a semana para migrar com segurança sem interromper as operações comerciais.</p>
    </div>
  </div>
  {cronograma_html}

  <!-- SEÇÃO 10: MONITORAMENTO -->
  <div class="sec-head" style="margin-top: 48px;">
    <div class="sec-info">
      <span class="sec-num">Seção 10 · Monitoramento &amp; Health Check da VPS</span>
      <h2>Painel de Diagnóstico &amp; Métricas de Alerta</h2>
      <p class="sec-note">Comandos em 1 clique para inspecionar memória, conexões de banco e status do WhatsApp.</p>
    </div>
  </div>

  <h3 style="font-family: var(--font-serif); font-size: 20px; margin: 16px 0 10px; color: var(--ink);">Comandos de Diagnóstico Rápido (1 Clique)</h3>
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
    pilares = dados.get("pilares", [])
    integracao = dados.get("camada_integracao", {})
    deploy = dados.get("deploy_consolidado", {})
    guia = dados.get("guia_modularidade_e_expansao", {})
    econ = dados.get("analise_economica_global", {})

    def sanitizar_typ(txt: str) -> str:
        return str(txt).replace('[', '(').replace(']', ')').replace('$', '\\$')

    linhas_pilares = ""
    for p in pilares:
        linhas_pilares += f"""
=== {p.get('nome_pilar')}
#text(size: 8.5pt, fill: rgb("#0284c7"), weight: "bold")[Alvo SaaS: {p.get('modulo_saas_alvo')}] \\
#text(size: 8.5pt, fill: rgb("#00875A"), weight: "bold")[Economia do Grupo: {sanitizar_typ(p.get('subtotal_economia_anual'))}] \\
#text(size: 8.5pt, style: "italic", fill: rgb("#475569"))[{p.get('descricao_pilar')}] \\
#v(4pt)

#table(
  columns: (0.5fr, 1.4fr, 1.8fr, 2.5fr, 1.4fr, 0.9fr),
  fill: (x, y) => if y == 0 {{ rgb("#f1f5f9") }} else {{ none }},
  stroke: 0.5pt + rgb("#e2e8f0"),
  inset: 4pt,
  [*Nº*], [*Classificação*], [*Ferramenta*], [*Substitui Diretamente*], [*Economia*], [*Licença*],
"""
        for f in p.get("ferramentas", []):
            c_simp = simplificar_classificacao(f.get('classificacao', ''))
            linhas_pilares += f"  [{f['rank']}], [{c_simp}], [*{f['nome']}*], [{f['saas_substituido_direto']}], [{sanitizar_typ(f['economia_anual_str'])}], [`{f['licenca_osi']}`],\n"
        linhas_pilares += ")\n#v(8pt)\n"

    custo_saas = sanitizar_typ(econ.get('custo_saas_anual', ''))
    custo_vps = sanitizar_typ(econ.get('custo_vps_anual', ''))
    econ_liq = sanitizar_typ(econ.get('economia_anual_liquida', ''))
    roi = sanitizar_typ(econ.get('roi_meses', ''))

    typ = f"""#set page(paper: "a4", flipped: true, margin: (x: 1.2cm, top: 1.2cm, bottom: 1.2cm))
#set text(font: "Liberation Sans", size: 9pt, lang: "pt")

#text(size: 8pt, fill: rgb("#64748b"), weight: "bold")[FÁBRICA UNIVERSAL AIDD · DOSSIÊ DE MACRO-ECOSSISTEMA SOBERANO (PADRÃO DIAMANTE R5-E)]
#v(2pt)
#text(size: 16pt, weight: "bold", fill: rgb("#0f172a"))[{sanitizar_typ(titulo)}]
#v(-2pt)
#text(size: 10pt, fill: rgb("#00875A"), weight: "bold")[{sanitizar_typ(subtitulo)}]
#v(6pt)

#grid(
  columns: (1fr, 1fr, 1.2fr, 1fr),
  gutter: 8pt,
  rect(fill: rgb("#f8fafc"), stroke: 0.5pt + rgb("#e2e8f0"), inset: 6pt)[
    #text(size: 7.5pt, fill: rgb("#64748b"))[CUSTO SAAS ANUAL] \\
    #text(size: 11pt, weight: "bold", fill: rgb("#dc2626"))[{custo_saas}]
  ],
  rect(fill: rgb("#f8fafc"), stroke: 0.5pt + rgb("#e2e8f0"), inset: 6pt)[
    #text(size: 7.5pt, fill: rgb("#64748b"))[CUSTO VPS SOBERANA] \\
    #text(size: 11pt, weight: "bold", fill: rgb("#0f172a"))[{custo_vps}]
  ],
  rect(fill: rgb("#f0fdf4"), stroke: 0.5pt + rgb("#bbf7d0"), inset: 6pt)[
    #text(size: 7.5pt, fill: rgb("#166534"))[ECONOMIA LÍQUIDA ANUAL] \\
    #text(size: 11pt, weight: "bold", fill: rgb("#16a34a"))[{econ_liq}]
  ],
  rect(fill: rgb("#f0fdf4"), stroke: 0.5pt + rgb("#bbf7d0"), inset: 6pt)[
    #text(size: 7.5pt, fill: rgb("#166534"))[PAYBACK ESTIMADO] \\
    #text(size: 11pt, weight: "bold", fill: rgb("#16a34a"))[{roi}]
  ]
)

#v(8pt)
== Pilares Estratégicos & Quinteto Soberano por Grupo
{linhas_pilares}

#v(8pt)
== Camada de Cola, SSO & Barramento de Eventos
- *Autenticação Única:* {sanitizar_typ(integracao.get('autenticacao_sso', ''))}
- *Barramento:* {sanitizar_typ(integracao.get('barramento_eventos', ''))}
- *Reverse Proxy:* {sanitizar_typ(integracao.get('gateway_reverse_proxy', ''))}

#v(8pt)
== Deploy All-in-One & Modularidade Operacional
- *Topologia:* {sanitizar_typ(deploy.get('arquitetura_rede_seguranca', ''))}
- *Princípio Modular:* {sanitizar_typ(guia.get('filosofia_modular', ''))}
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
