---
name: fabrica-listas
description: >
  Fábrica de compêndios técnicos e apresentações HTML autônomas de alta densidade no Padrão Diamante (Dossiê Executivo).
  Gera catálogos auditados de ferramentas, especificações de consumo de hardware,
  substituições de SaaS e boas práticas de engenharia com design editorial, busca em tempo real, grid de 3 passos práticos e scrollbar 4px.
  Use quando o usuário pedir listas, catálogos comparativos, compêndios técnicos ou invocar /fabrica-listas.
license: MIT
metadata:
  version: 2.0.0
  author: Fábrica Universal
---

# Fábrica de Listas Técnicas · Padrão Diamante (Dossiê Executivo)

Especificação obrigatória e imutável para gerar compêndios técnicos em HTML autocontido com máxima densidade de informação, alinhamento justificado e design editorial impecável.

## 1. Princípios do Padrão Diamante (Regra R5)

Todo documento gerado DEVE ser 100% autocontido (CSS e JS embutidos), responsivo e com suporte nativo a temas Claro e Escuro (via `prefers-color-scheme`).

### 1.1 Paleta de Cores e Tipografia Impeccable
```css
:root {
  --paper: #ECEEF2; --surface: #F8F9FC; --surface-2: #DFE3EB;
  --ink: #151A26; --ink-2: #3B4457; --muted: #68738A;
  --rule: #C7CEDB; --rule-soft: #DADFE8;
  --accent: #1A446C; --accent-soft: #DCE7F2;
  --gold: #7A5410; --gold-soft: #EFE5CE;
  --flag: #8E2436; --flag-soft: #F0D9DD;
  --green: #1B5E3B; --green-soft: #D8EFE2;
  --shadow: 0 1px 0 rgba(21,26,38,.05), 0 8px 24px -18px rgba(21,26,38,.45);
  --serif: "Iowan Old Style", "Palatino Linotype", Palatino, Georgia, serif;
  --sans: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  --mono: ui-monospace, "Cascadia Mono", "SF Mono", Menlo, Consolas, monospace;
}
```

### 1.2 Regra da Scrollbar Estrita (4px)
```css
* { scrollbar-width: thin; scrollbar-color: var(--accent) transparent; }
::-webkit-scrollbar { width: 4px; height: 4px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: var(--accent); border-radius: 4px; }
```

---

## 2. Estrutura Canônica do Documento (6 Seções Obrigatórias)

1. **Header Executivo & Hero Stats Bar:**
   - Link de retorno ao Hub: `[← Voltar ao Hub Central]`
   - Badge da Camada: `.layer-badge` (ex: `Camada 01`, `Camada 35`)
   - Título H1 e Deck justificados (`text-align: justify; text-justify: inter-word;`)
   - Hero Stats Bar com 4 métricas executivas
   - Links de salto rápido para a Matriz (`#tabela`) e Fichas (`#fichas`)

2. **Rotas Estratégicas (Dilema & Soberania):**
   - 2 cards comparativos: Rota Frágil (Custo/Risco) vs Rota Soberana (Independência/Eficiência).

3. **Matriz Comparativa Fluida (`#tabela`):**
   - Tabela 100% de largura (sem scroll horizontal artificial)
   - Colunas: `#`, `Ferramenta`, `Substitui o SaaS Pago`, `Economia Estimada`, `Categoria` e `Licença OSI`.
   - Hover suave nas linhas.

4. **Barra de Busca Instantânea Local (`#fichas`):**
   - Caixa de pesquisa em tempo real que filtra as fichas por nome, comando ou SaaS substituído.

5. **Ledger de Fichas Técnicas no Padrão Dossiê Executivo (`div.entry`):**
   - Cada card possui 4 seções verticais de largura total:
     - **Seção 1: O Que Faz & Como Funciona** (com bloco de código executável e botão Copiar).
     - **Seção 2: Análise Econômica** (SaaS proprietários substituídos e ROI real em destaque).
     - **Seção 3: Requisitos de Infraestrutura, Ecossistema & Veredito** (Consumo em repouso de RAM/VRAM, senioridade e botão GitHub).
     - **Seção 4: Como Usar no Dia a Dia** (Grid com 3 mini-cards visuais de passos práticos numerados: `[1] Configuração`, `[2] Operação`, `[3] Resultado`).

6. **Armadilhas, Anti-Patterns & Método Fabril:**
   - Riscos de telemetria forçada, falsos open source (BSL/SSPL) e arquitetura recomendada.

---

## 3. Anti-Patterns Estritamente Proibidos (Regra R5)

- ❌ **PROIBIDO:** Usar layouts em 2 colunas espremidas (`div.cols`).
- ❌ **PROIBIDO:** Condensar o passo a passo em parágrafos de texto corrido sem os 3 mini-cards.
- ❌ **PROIBIDO:** Omitir ferramentas mapeadas na tabela da listagem de fichas técnicas (paridade 100%).
- ❌ **PROIBIDO:** Usar títulos com prefixos residuais (`Skill: `, `Motor: `).
- ❌ **PROIBIDO:** Criar arquivos sem salvar simultaneamente em `output/listas-open-source/` e `docs/listas/`.
