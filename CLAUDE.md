---
description: Governanca universal, squad e fluxo do projeto — orquestrador para qualquer agente neste diretorio.
alwaysApply: true
---

# Arsenal Open Source · Fábrica Universal — Orquestrador Central

> **Governança Mestre & Arquitetura Agêntica Multi-IDE.**
> Hardlink canônico: `CLAUDE.md`, `.cursor/rules/projeto.mdc`, `.windsurfrules`, `.clinerules`, `.github/copilot-instructions.md`.
> Junctions: `agentic/` ➔ `.claude/`. Fonte de skills/commands: `.agents/`. Setup: `scripts/setup-links.ps1` | `scripts/setup-links.sh`.

## 0. Economia Severa de Tokens (PRIORIDADE MÁXIMA)

1. **Caveman & Silenciamento:** Pensamento telegráfico (3-5 linhas PT-BR). Respostas diretas ao ponto, sem preâmbulos, saudações ou clichês de IA.
2. **Headroom & LeanCTX:** Logs/builds >7 linhas truncar (3 topo + 4 fim). `grep` antes de `view/read`. Limitar leitura por linhas.
3. **Isenção de Entrega:** Arquivos `output/**`, JSONs de estado e relatórios de gates NUNCA são truncados (leitura/escrita integrais).
4. **Subagentes:** Apenas para varreduras extensas de código; nunca para gerar texto retornado ao usuário.
5. **Compilação Determinística:** Geração de artefatos (HTML, MD, PDF) via scripts Python. Proibido editar HTML manualmente de cabeça.
6. **Soberania do Usuário & Fallback:** Decisões críticas exigem confirmação. Sandbox bloqueou ➔ exibir comando no terminal.
7. **UTF-8 no Windows:** Scripts com saída de texto/emojis DEVEM chamar `sys.stdout.reconfigure(encoding="utf-8")` ou `console_utf8()`.
8. **Estabilidade de Cache & RTK:** Prompt mestre imutável (<1.500 tokens). Aprendizados e memórias vivem em `RTK-SCRATCHPAD.md`.

## 1. Regras Globais

- **R1 (Idioma):** PT-BR estrito em toda comunicação, código-entrega, documentação e artefatos.
- **R2 (Silenciamento):** Sem saudações. Markdown limpo, técnico e executivo.
- **R3 (Autonomia):** Escopo definido ➔ execução 100% autônoma até o veredito dos gates.
- **R4 (Auto-correção):** Desvios e falhas de validação são corrigidos internamente antes da entrega.
- **R5 (Padrão Diamante R5):** Proibido HTML manual. Listas horizontais compiladas via script (`scripts/normalizar_compendio.py`) com Hero Stats Bar, busca, grid `60px 1fr` (`.entry-rank`), `.econ-card`, `.infra-grid`, `.steps-grid` e White-Label. Validado via `scripts/auditar_r5_dossie.py`.
- **R5-V (Dossiê Vertical R5-V):** Desmantelamento SaaS. Estrutura: Alvo SaaS, Quinteto Soberano (*Mais Robusta, Completa, Moderna, Leve, Simples*), Seção White-Label e Seção MCPs/Skills. Validado via `scripts/auditar_tipo_vertical.py`.
- **R6 (Modelo Livre):** `model: inherit` em todos os agentes.
- **R7 (Conteúdo Intocável):** Entregas finais não são resumidas ou truncadas sem pedido explícito.
- **R8 (Determinismo Primeiro):** Se um script resolve (gerar, contar, validar, converter), não gaste LLM.
- **R9 (Gates Mecânicos):** Validação por scripts (`exit 0` / `exit 1`). Promessa em prosa não é gate.
- **R10 (Idempotência):** Reexecução produz o mesmo resultado sem corromper estado.
- **R11 (Estado Persistente):** Estado vive no SQLite `estado_esteira.db`, nunca apenas no contexto volátil.
- **R12 (Registro Declarativo):** Adicionar tipo/camada tecnológica custa 1 entrada em `scripts/tipos.py`.
- **R13 (Taxonomia & Slugs):** `list-<slug>.html` (listas), `vert-<saas>.html` (verticais), `tco-<slug>.html` (preço) e `guia-<slug>.html` (VPS). Slugs <= 35 chars, minúsculos com hífen.
- **R14 (Caminhos Curtos):** Respeitar MAX_PATH (260 chars) do Windows.
- **R15 (Segredos):** Zero credenciais versionadas. O hook `pre-commit` bloqueia detecções.
- **R16 (Nunca Commitar Vermelho):** Pós-implementação: suite de testes e gates ➔ 100% verde ➔ commit + push.
- **R17 (Integridade OSI):** Ferramentas devem ter licença OSI explícita, SaaS substituído e URL válida.
- **R18 (Higiene Soberana):** Zero `.tmp`/`.bak`/`.typ`. Pasta soberana única `output/` (`01-listas-horizontais/`, `02-dossies-verticais/`, `03-manuais-e-trilhas/`, `04-ecossistemas/`). Proibido auto-fork em lote.
- **R19 (Comunicação Direta):** Resultado na primeira linha. Uma sentença por tópico. Verbos de ação. Zero clichês.
- **R20 (Visual Corporativo Estrito & Proibição de Emojis):** Proibição absoluta do uso de emojis ou pictogramas em todos os materiais gerados em todos os fluxos (HTML, Markdown, PDF Typst, relatórios executivos, manuais e trilhas). O visual deve ser 100% corporativo, sóbrio, elegante e técnico, utilizando tipografia formal, badges, numeração e tabelas.

## 2. Squad & Especialistas

- `<pesquisador-open-source>`: Coleta de metadados, licenças OSI e repositórios.
- `<redator-diamante>`: Compilação determinística no Padrão Diamante R5 e R5-V.
- `<auditor-r18>`: Auditoria de integridade, paridade de espelhos e ausência de entulho.
- `<orquestrador-harness>`: Gerenciador de links multi-IDE, SQLite e gates mecânicos.

## 3. Servidores MCP & Templates

- **MCPs (`.mcp.json`):** `db_state_esteira` (SQLite R11) e `file_validator` (Integridade R18).
- **Templates:** `scripts/padroes/template_dossie_executivo.py`, `relatorio_enterprise.css`, `scripts/schemas/`.

## 4. Os 4 Macro-Fluxos AIDD

1. **Fluxo 1 · Listas Horizontais (Camadas Temáticas):** `/fluxo1 [slug]` | `python scripts/run_fluxo1.py --slug <slug>` ➔ `output/01-listas-horizontais/list-<slug>/` (HTML R5, MD, PDF + relatórios)
2. **Fluxo 2 · Dossiês Verticais & Quinteto:** `/fluxo2 [saas]` | `python scripts/run_fluxo2.py --saas <saas>` ➔ `output/02-dossies-verticais/vert-<saas>/` (HTML R5-V, MD, PDF + relatórios)
3. **Fluxo 3 · Manuais VPS & Trilhas:** `/fluxo3 [ferramenta] [saas]` | `python scripts/run_fluxo3.py --ferramenta <slug> --saas <saas>` ➔ `output/03-manuais-e-trilhas/<saas>/<ferramenta>/` (9 arquivos)
4. **Fluxo 4 · Macro-Ecossistemas & Suítes Integradas:** `/fluxo4 [ecossistema]` | `python scripts/run_fluxo4.py --ecossistema <slug>` ➔ `output/04-ecossistemas/ecos-<slug>/` (HTML R5-E, MD, PDF + relatórios)
5. **Pipeline Total:** `/fluxo-total` | `python scripts/run_fluxo_total.py`

## 5. Portabilidade Multi-IDE & RTK

- **Fonte Única:** `.agents/` espelhado para `.claude/` e `agentic/`. Links: `scripts/setup-links.ps1`.
- **Pre-commit:** `.git/hooks/pre-commit` bloqueia falhas e segredos.
- **Scratchpad:** `RTK-SCRATCHPAD.md` na raiz para aprendizados e memórias dinâmicas.
