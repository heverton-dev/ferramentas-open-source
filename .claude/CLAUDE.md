---
description: Governanca universal, squad e fluxo do projeto — orquestrador para qualquer agente neste diretorio.
alwaysApply: true
---

# Arsenal Open Source · Fábrica Universal — Orquestrador Central

> **Governança Mestre e Arquitetura Agêntica.**
> Hardlink de `CLAUDE.md`, `.cursor/rules/projeto.mdc`, `.windsurfrules`,
> `.clinerules`, `.github/copilot-instructions.md`. Edite apenas este arquivo.
> Junctions: `agentic/` aponta para `.claude/` (portabilidade multi-IDE);
> `.agents/` recebe so `agents/` e `commands/` (ver Secao 6).
> Para recriar links apos clone: `scripts/setup-links.ps1` (Win) ou
> `scripts/setup-links.sh` (Mac/Linux).

## 0. Economia Severa de Tokens (PRIORIDADE MAXIMA)

1. **Caveman Ativo:** pensamento telegrafico (3-5 linhas), sem preambulos/saudacoes.
2. **Headroom & RTK:** logs/builds >7 linhas -> comprimir (3 topo + 4 fim).
   EXCECAO: conteudo de entrega (ver R7) NUNCA e comprimido.
3. **LeanCTX:** grep antes de read em codigo/config. Limitar leitura por linha.
4. **Delegacao comprimida:** subagentes para buscas/edicoes extensas
   (nunca para prosa que sera entregue ao usuario).
5. **Compilacao ISENTA:** geracao de artefato final (HTML, dossiês, bundles) e
   liberada e obrigatoria. Nenhuma regra de token economy interfere.
6. **Fallback Terminal:** se o sandbox bloquear, exibir os comandos no chat
   para o operador rodar.
7. **Soberania do Usuario:** nada e barrado sem confirmacao explicita do operador.
8. **Fidelidade de Conteudo (sobrepoe 2-4):** arquivos de entrega (`output/**`
   ou equivalente do seu dominio), JSONs de estado e saidas de gates de
   validacao sao isentos de compressao — leitura sempre integral.
9. **Busca via Grafo:** se houver indice de codigo (ex.: `code-review-graph`),
   consultar antes das tools de leitura/busca.
10. **Auto-commit/push:** alteracoes devem ser commitadas e pushadas para manter
    o indice/grafo atualizado.
11. **UTF-8 no Windows:** todo script Python com `print`/emojis DEVE chamar
    `console_utf8()` (padrao em `scripts/padroes/script-template.py`) ou
    `sys.stdout.reconfigure(encoding="utf-8")` — sem isso quebra em cp1252.
12. **Skills de economia disponiveis:** `caveman`, `headroom`, `lean-ctx`,
    `rtk-memory`, `pre-flight-check` (em `.claude/skills/`).
13. **Vocabulário Controlado & Termos Proibidos:** Banidos clichês de IA
    ("como uma IA", "espero ter ajudado", "com certeza", "certamente", "olá").
    Respostas 100% técnicas, densas e diretas ao ponto.
14. **Orçamento de Cache da TELA:** O prompt mestre é mantido estável e abaixo
    de 2.500 palavras para maximizar o desconto de 90% de Prompt Caching. Aprendizados
    novos são salvos externamente em `RTK-SCRATCHPAD.md`.

## 1. Regras Globais

- **R1 (Idioma):** idioma único e estrito em toda comunicação e artefatos (PT-BR).
- **R2 (Silenciamento):** sem preâmbulos/saudações nos artefatos. Markdown limpo e executivo.
- **R3 (Autonomia):** após o escopo definido, o fluxo roda 100% autônomo.
- **R4 (Auto-correção):** desvios são corrigidos internamente antes da entrega.
- **R5 (Padrão Dossiê Executivo Diamante & Compilação Determinística):** É TERMINANTEMENTE PROIBIDO a qualquer agente/LLM gerar ou editar arquivos HTML de compêndios manualmente de cabeça. Toda camada DEVE ser gerada a partir de JSON estruturado ou normalizada pelo compilador determinístico (`scripts/normalizar_compendio.py`). Os artefatos visuais seguem obrigatoriamente: (1) Header com Hero Stats Bar e busca interativa client-side; (2) Título H1 alinhado naturalmente e Deck justificado; (3) Tabela de dados fluida; (4) Cards em grid `60px 1fr` com rank lateral `.entry-rank`, seções padronizadas (`.entry-section`: O Que Faz, Análise Econômica com `.econ-card`, Requisitos & Veredito com `.infra-grid` e `.verdict-box`, 3 mini-cards visuais de passos práticos em `.steps-grid`, e **Seção de White-Label & Aderência ao Design System Corporativo** com badges de esforço). Proibido o uso de layouts em 2 colunas espremidas (`div.cols`), classes CSS inventadas ou qualquer alteração estrutural que não esteja documentada no `template_dossie_executivo.py`. Qualquer tentativa de "embelezar" o HTML ignorando o template disparará erro crítico no `auditar_r5_dossie.py`.
- **R5-V (Dossiê Vertical de Desmantelamento SaaS & Quinteto Soberano):** Formato cirúrgico de desmantelamento de SaaS proprietários específicos (ex: Granola, Notion, Salesforce, Zapier). Estrutura obrigatória: (1) Caixa de Alvo SaaS com preço e riscos de privacidade; (2) O Quinteto Soberano classificado estritamente em: *A Mais Robusta*, *A Mais Completa*, *A Mais Moderna*, *A Mais Leve* e *A Mais Simples*; (3) Presença obrigatória da Seção 5: `5. White-Label & Aderência ao Design System Corporativo` com badges de esforço e análise de risco de upgrades; (4) Presença obrigatória da Seção 6: `6. Uso Complementar & Ecossistema Agêntico (MCPs, Skills & Plugins)` mapeando servidores MCP, Agent Skills e extensões reais; (5) Scrollbars de no máximo 4px na cor accent; (6) Validação mecânica obrigatória via `scripts/auditar_tipo_vertical.py`.
- **R6 (Modelo Livre):** nenhum modelo LLM fixo. `model: inherit` em todos os agents.
- **R7 (Conteúdo de entrega intocável):** o que vai para o usuário final não é resumido, truncado nem "melhorado" sem pedido explícito.
- **R8 (Determinismo primeiro):** se um script resolve, não gaste LLM. Gerar, validar, contar e converter são tarefas de script — não de agente.
- **R9 (Gates mecânicos):** toda regra de qualidade que puder virar script vira script com retorno `exit 0` (sucesso) ou `exit 1` (erro). Promessa em prosa não é gate.
- **R10 (Idempotência):** scripts podem rodar N vezes com o mesmo resultado e sem efeito colateral. Reexecução nunca corrompe estado.
- **R11 (Estado em disco):** o estado da esteira vive em banco relacional SQLite (`estado_esteira.db`), nunca apenas no contexto volátil da conversa.
- **R12 (Registro declarativo):** adicionar um tipo/variante novo deve custar **1 entrada** em `scripts/tipos.py`.
- **R13 (Taxonomia Semântica de Nomenclaturas & Slugs Curtos):** Fica expressamente abolida a dependência de numeração sequencial frágil (`01-`, `02-`). Todos os compêndios e artefatos adotam obrigatoriamente prefixos semânticos canônicos: (1) `list-<slug-curto>.html` para listas temáticas horizontais; (2) `vert-<saas-slug>.html` para dossiês verticais de desmantelamento SaaS com o Quinteto Soberano e MCPs/Skills; (3) `tco-<slug-curto>.html` para tabelas de comparação de preço e ROI; (4) `guia-<slug-curto>.html` para playbooks práticos e deploys em VPS. Todos os nomes de arquivo devem permanecer estritamente abaixo de 35 caracteres, em minúsculas e separados por hífen.
- **R14 (Caminhos curtos):** nomes de pasta/arquivo gerados respeitam o MAX_PATH do Windows (260 chars). Preferir slug curto a título por extenso.
- **R15 (Segredos):** nenhuma credencial em arquivo versionado. O hook `pre-commit` bloqueia o commit se detectar padrão de segredo no diff staged.
- **R16 (Pós-implementação — nunca commitar vermelho):** APÓS TODA nova implementação: (1) rodar a suíte de testes necessária; (2) **100%** -> commit + push; (3) **<100%** -> analisar a falha, corrigir o código, re-testar até 100%. Nunca commitar suíte vermelha; nunca contornar o teste para fazê-lo passar.
- **R17 (Integridade de Repositórios & Validação de URLs):** toda ferramenta catalogada DEVE possuir licença OSI explícita, identificação do SaaS substituído e URL de repositório válida.
- **R18 (Higiene Contínua, Zero Entulho & Sincronização Estrita):** regra inegociável de pureza: (1) **Zero Arquivos Temporários:** nenhum script descartável (`temp_*`, `fix_*`, `.bak`, `.tmp`) pode permanecer no repositório. (2) **Paridade Estrita de Espelhos:** qualquer compêndio em `output/listas-open-source/` DEVE ter paridade de hash MD5 idêntica em `docs/listas/`. (3) O hook `pre-commit` bloqueia qualquer tentativa de commitar com divergência de espelho ou lixo temporário (`exit 1`).

## 2. Squad & Especialistas

- `<pesquisador-open-source>`: Coleta determinística de metadados, licenças e repositórios.
- `<redator-diamante>`: Geração de fichas no Padrão Dossiê Executivo (R5).
- `<auditor-r18>`: Validador de integridade de espelhos e ausência de entulho.
- `<orquestrador-harness>`: Gerenciador de links multi-IDE e gates mecânicos.

## 3. Servidores MCP

Declarados em `.mcp.json` na raiz:
- `db_state_esteira` (SQLite) — Estado persistente da esteira (R11).
- `file_validator` — Auditor criptográfico de integridade e espelhos (R18).

## 4. Templates de Saída

- `scripts/padroes/template_dossie_executivo.py`: Molde canônico em HTML/CSS para os 49 compêndios.
- `scripts/schemas/`: Schemas JSON para estruturação de dados de ferramentas e relatórios.

## 5. Fluxo Operacional da Fábrica Universal

O fluxo canônico para cada camada ou módulo do projeto:
1. **Fase 1 (Mapeamento & Auditoria):** Coleta determinística de ferramentas, validação de licença OSI e definição de SaaS substituídos.
2. **Fase 2 (Produção Diamante):** Geração do compêndio HTML autocontido com Hero Stats, tabela fluida, 4 seções por card e 3 mini-cards de passos práticos.
3. **Fase 2.5 (Auditoria Mecânica):** Execução dos gates `auditar_r5_dossie.py`, `auditar_higiene_repo.py` e `auditar_todas_camadas.py`.
4. **Fase 3 (Sincronização & Custódia):** `python scripts/limpar_entulho.py` (garante paridade entre `output/` e `docs/`) ➡️ Commit ➡️ Sincronização dos forks no GitHub.

## 6. Portabilidade Multi-IDE

Fonte única: `.claude/`.
- **Junctions & Links:** `AGENTS.md` -> `.claude/CLAUDE.md`, `.cursor/rules/` -> `.claude/CLAUDE.md`.
- **Pre-commit hook:** Instalado em `.git/hooks/pre-commit`.
- **Recriar links:** `scripts/setup-links.ps1` (Win) ou `scripts/setup-links.sh` (Linux/Mac).

## 7. RTK Scratchpad

Aprendizados e decisões de sessões anteriores vivem em `RTK-SCRATCHPAD.md` na raiz do projeto.
