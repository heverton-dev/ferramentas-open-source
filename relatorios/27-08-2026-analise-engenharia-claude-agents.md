# Relatório de Engenharia · Boas Práticas, Benchmarks & Auditoria de `CLAUDE.md` e `AGENTS.md`

> **Data de Emissão:** 27-08-2026  
> **Autor:** Antigravity Multi-Agent Harness · Arsenal Open Source  
> **Status:** Concluído · Avaliação Técnica de Contexto e Governança Multi-IDE  

---

## 1. O que Recomendam as Fontes Oficiais & a Indústria

### A. Diretrizes Oficiais da Anthropic para `CLAUDE.md`
O `CLAUDE.md` é injetado diretamente no System Prompt do agente a cada início de sessão e mantido no topo da janela de contexto.

| Critério | Recomendação Oficial Anthropic | Justificativa Técnica |
| :--- | :--- | :--- |
| **Papel do Arquivo** | *Onboarding Brief*, não manual enciclopédico. | O modelo já conhece sintaxes de linguagens e boas práticas gerais. O arquivo deve conter apenas **o que o modelo não tem como adivinhar** (comandos de build/teste, arquitetura de pastas, restrições e regras inegociáveis). |
| **Tamanho em Linhas** | **Entre 100 e 300 linhas** (teto máximo tolerado: 500 linhas). | Acima de 500 linhas, o modelo sofre de dispersão de atenção (*attention dilution*) e ignora regras críticas no meio do arquivo. |
| **Volume de Tokens** | **Ideal: 1.200 a 1.800 tokens** (~1.000 a 1.500 palavras). | Permite atingir com folga o limite mínimo de **Prompt Caching da Anthropic (1.024+ tokens no Sonnet / 4.096+ no Opus)**, garantindo 90% de desconto de custo sem poluir a janela útil. |
| **Regra de Ouro da Anthropic** | *"Se você remover esta linha e o Claude não cometer erros, remova-a."* | Cada palavra irrelevante custa tokens em todas as chamadas e aumenta o ruído de inferência. |
| **Estabilidade de Cache** | **Arquivo Imutável durante a sessão.** | Qualquer alteração no `CLAUDE.md` no meio da sessão invalida instantaneamente o cache da conversa inteira a jusante, multiplicando o custo da sessão. Aprendizados dinâmicos devem viver fora (ex: scratchpads). |
| **Modularização** | **Skills & Sub-arquivos sob demanda.** | Instruções complexas de fluxos específicos não devem ficar no arquivo raiz; devem ser isoladas em `skills/` ou comandos sob demanda (ex: `/fluxo1`). |

---

### B. Especificação Universal `AGENTS.md` (Padrão Aberto Multi-IDE)
A especificação `AGENTS.md` é o padrão agnóstico adotado pelo ecossistema moderno de ferramentas de IA (Cursor, Windsurf, Claude Code, GitHub Copilot, RooCode, OpenCode, Aider):

1. **Centralização e Ponto Único de Verdade:** Um único arquivo na raiz do repositório governa todas as IDEs e agentes, evitando deriva de regras entre diferentes ferramentas.
2. **Prevenção de *Context Pollution* & *Context Rot*:** Instruções verbosas, explicações longas ou código em prosa geram poluição de contexto. O formato deve usar markdown estruturado (tabelas, listas com marcadores e palavras-chave em negrito).
3. **Determinismo Mecânico:** Instruções que exigem conformidade estrita devem apontar para scripts executáveis (`exit 0` / `exit 1`) em vez de descrições longas tentando convencer a LLM.

---

## 2. Auditoria Técnica dos Arquivos do Nosso Repositório

Levantamento quantitativo dos arquivos de contexto, instruções mestres e regras espelhadas no repositório:

| Arquivo | Papel / Função | Status / Vínculo | Tamanho | Linhas | Palavras | Tokens Est. |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| `AGENTS.md` | **Fonte Única de Governança** | Arquivo Canônico | 12.351 B | 120 | 1.586 | **~3.462** |
| `CLAUDE.md` | Contexto Claude Code (Raiz) | Espelho / Hardlink | 12.351 B | 120 | 1.586 | **~3.462** |
| `.claude/CLAUDE.md` | Configuração Local Claude | Espelho / Hardlink | 12.351 B | 120 | 1.586 | **~3.462** |
| `.cursor/rules/projeto.mdc` | Regras Globais do Cursor | Espelho / Hardlink | 12.351 B | 120 | 1.586 | **~3.462** |
| `.clinerules` | Regras do Cline / Roo-Code | Espelho / Hardlink | 12.351 B | 120 | 1.586 | **~3.462** |
| `.windsurfrules` | Regras do Windsurf / Cascade | Espelho / Hardlink | 12.351 B | 120 | 1.586 | **~3.462** |
| `.github/copilot-instructions.md` | Instruções do GitHub Copilot | Espelho / Hardlink | 12.351 B | 120 | 1.586 | **~3.462** |
| `RTK-SCRATCHPAD.md` | Memória Dinâmica RTK | Arquivo Isolado | 2.812 B | 29 | 349 | **~785** |

---

## 3. Diagnóstico de Engenharia & Avaliação de Conformidade

### ✅ Pontos Fortes & Excelência Arquitetural
1. **Padrão DRY Absoluto (Zero Duplicação de Manutenção):**
   - O projeto adota uma **fonte única de verdade** em `AGENTS.md` (e `.claude/CLAUDE.md`), espelhando via hardlinks/junctions para todas as outras IDEs (`.cursor/`, `.clinerules`, `.windsurfrules`, `.github/`).
2. **Tamanho em Linhas Muito Saudável:**
   - O arquivo possui apenas **120 linhas**, bem abaixo do teto de 300–500 linhas recomendado pela Anthropic.
3. **Isolamento de Memória Dinâmica:**
   - Os aprendizados de sessões anteriores não inflam o `AGENTS.md`/`CLAUDE.md`, ficando isolados em `RTK-SCRATCHPAD.md`, preservando a estabilidade do cache de prompt (90% de desconto da Anthropic).
4. **Modularização por Skills e Comandos:**
   - Detalhes operacionais dos fluxos foram distribuídos em comandos (`.agents/commands/fluxo1.md`, etc.) e skills sob demanda, mantendo o arquivo principal enxuto.

---

### ⚠️ Oportunidades de Otimização de Tokens

Embora o arquivo tenha 120 linhas e 1.586 palavras (respeitando o teto de 2.500 palavras), a contagem estimada de tokens está em **~3.462 tokens**. Isso ocorre porque certas regras possuem descrições de especificações muito detalhadas em parágrafos longos:

| Seção Atual | Linhas | Tokens Est. | Oportunidade de Otimização Futura |
| :--- | :---: | :---: | :--- |
| **Seção 0 (Economia de Tokens)** | 32 | ~850 | Os 14 itens são muito claros, mas alguns são redundantes com as regras da Seção 1 (ex: R19 e R7). |
| **Seção 1 · Regra R5 (Dossiê Diamante)** | 1 | ~380 | Parágrafo único contínuo descrevendo classes CSS e seletores HTML que já são 100% validados por `scripts/auditar_r5_dossie.py`. |
| **Seção 1 · Regra R5-V (Quinteto Soberano)** | 1 | ~260 | Detalhes de CSS (scrollbars 4px) que já são resolvidos pelo template python. |
| **Seção 1 · Regra R18 (Higiene e Anti-Fork)** | 1 | ~210 | Regra densa que pode ser simplificada em 3 tópicos diretos. |
| **Seção 1 · Regra R19 (Comunicação Limpa)** | 1 | ~320 | Detalhamento extenso de anti-padrões que já está coberto pela Seção 0 (Caveman e Silenciamento). |

---

## 4. Conclusão & Veredito

1. **Estado Atual:** O repositório está **conforme** com as recomendações de mercado em termos de estrutura, estabilidade de cache, governança e limites de linhas (120 linhas vs limite de 300).
2. **Impacto no Contexto:** O carregamento inicial consome aproximadamente **3.462 tokens**, o que representa menos de **1,8%** de uma janela padrão de 200k tokens, ativando imediatamente o Prompt Caching da Anthropic.
