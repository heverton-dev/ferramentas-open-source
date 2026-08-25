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
5. **Compilacao ISENTA:** geracao de artefato final (PDF, build, bundle) e
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

- **R1 (Idioma):** idioma unico e estrito em toda comunicacao e artefatos.
  `[CUSTOMIZAR]` — padrao deste template: PT-BR.
- **R2 (Silenciamento):** sem preambulos/saudacoes nos artefatos. Markdown limpo.
- **R3 (Autonomia):** apos o escopo definido, o fluxo roda 100% autonomo.
- **R4 (Auto-correcao):** desvios sao corrigidos internamente antes da entrega.
- **R5 (Identidade visual & Padrão Dossiê Executivo):** artefatos visuais seguem o padrão obrigatório do **Dossiê Executivo**: (1) Header com Hero Stats Bar e âncoras rápidas; (2) Título H1 e Deck justificados (`text-align: justify; text-justify: inter-word;`); (3) Tabela de dados 100% fluida sem scroll horizontal; (4) Cards verticais de largura total divididos em 4 seções padronizadas: *O Que Faz & Como Funciona* (com bloco de código e botão Copiar), *Análise Econômica* (SaaS substituídos e ROI), *Requisitos de Infraestrutura & Veredito* (com botão GitHub) e *Como Usar no Dia a Dia* (grid com 3 mini-cards visuais de passos práticos). É estritamente proibido o uso de layouts em 2 colunas espremidas (`div.cols`) ou passos condensados em parágrafos únicos.
- **R6 (Modelo Livre):** nenhum modelo LLM fixo. `model: inherit` em todos os agents.
- **R7 (Conteudo de entrega e intocavel):** o que vai para o usuario final nao e
  resumido, truncado nem "melhorado" sem pedido explicito.
- **R8 (Determinismo primeiro):** se um script resolve, nao gaste LLM. Gerar,
  validar, contar e converter sao tarefas de script — nao de agente.
- **R9 (Gates mecanicos):** toda regra de qualidade que puder virar script vira
  script com `exit 0/1`. Promessa em prosa nao e gate.
- **R10 (Idempotencia):** scripts podem rodar N vezes com o mesmo resultado e
  sem efeito colateral. Reexecucao nunca corrompe estado.
- **R11 (Estado em disco):** o estado da esteira vive em arquivo versionavel
  (JSON/SQLite), nunca so no contexto da conversa.
- **R12 (Registro declarativo):** adicionar um tipo/variante novo deve custar
  **1 entrada** num registro, nao edicao de N arquivos de dispatch.
- **R13 (Sem prefixo `_`):** nenhum arquivo ou pasta gerado usa prefixo `_` —
  em glob de shell, listagem de nuvem e empacotamento ele e tratado como oculto.
- **R14 (Caminhos curtos):** nomes de pasta/arquivo gerados respeitam o
  MAX_PATH do Windows (260 chars). Preferir slug curto a titulo por extenso.
- **R15 (Segredos):** nenhuma credencial em arquivo versionado. O hook
  `pre-commit` bloqueia o commit se detectar padrao de segredo no diff staged.
- **R16 (Pos-implementacao — nunca commitar vermelho):** APOS TODA nova
  implementacao: (1) rodar a suite de testes necessaria (ex.: `python -m pytest -q`
  ou a suite do seu stack); (2) **100%** -> commit + push; (3) **<100%** ->
  analisar a falha, corrigir o codigo, re-testar ate 100%. Nunca commitar suite
  vermelha; nunca contornar o teste para faze-lo passar — corrigir a causa.
  Mecanizada pelo hook `scripts/hooks/pre-commit`.
- **R17 (Etapas opcionais sao SEMPRE opcionais):** etapas marcadas como
  opcionais no fluxo nunca sao obrigatorias. (1) Na entrevista inicial o
  operador escolhe explicitamente quais etapas opcionais entram, e a escolha e
  persistida em config; o fluxo PULA a etapa quando `false`, sem tratar como
  falha. (2) Independente da escolha inicial, o operador pode disparar a etapa
  a qualquer momento para um artefato ja existente. (3) Se o artefato daquela
  etapa ja existir, o sistema SEMPRE oferece a escolha entre **Criar Nova**
  (versiona a existente) ou **Sobrescrever Existente**. Nunca decidir isso
  silenciosamente — a escolha e sempre do operador.
- **R18 (Higiene Contínua, Zero Entulho & Sincronização Estrita):** regra inegociável
  de pureza do repositório: (1) **Zero Arquivos Temporários:** nenhum script descartável
  (ex.: `temp_*`, `fix_*_temp.py`, `migrar_*.py`, `.bak`, `.tmp`) pode permanecer
  no repositório após o término da tarefa. (2) **Paridade Estrita de Espelhos:** qualquer
  documento ou compêndio gerado/editado em `output/listas-open-source/` DEVE ter
  paridade de hash e conteúdo idêntica em `docs/listas/` (mecanizado via `scripts/auditar_higiene_repo.py`).
  (3) **Zero Duplicidade de Camadas:** toda ferramenta ou camada possui identificador
  único, contínuo e sem sobreposições. O hook `pre-commit` bloqueia qualquer tentativa
  de commitar com divergência de espelho ou lixo temporário (`exit 1`).

### Tipos de Artefato — registro declarativo `[CUSTOMIZAR]`

Registro unico em `scripts/tipos.py` (R12). Exemplo de forma:

```python
TIPOS = {
    "<tipo-a>": {"natureza": "geracao",  "custo_llm": "alto",
                 "spec": "SPEC_A.md", "comando": "/criar-a",
                 "produtor": "<skill-ou-script>", "gates": ["validar-x.py"]},
    "<tipo-b>": {"natureza": "extracao", "custo_llm": "zero",
                 "spec": "SPEC_B.md", "comando": "/criar-b",
                 "produtor": "gerar-b.py",       "gates": ["validar-b.py"]},
}
```

**Regra de derivacao:** cascateie onde **comprime**, faca fan-out onde **expande**.
Compressao/extracao sao baratas; expansao custa geracao.

**Adicionar um tipo novo = 1 entrada no registro.** Todos os pontos de dispatch
consultam o registro — nao se edita N arquivos por tipo.

## 2. Squad `[CUSTOMIZAR]`

### Skills de Dominio

`<especialista-1>` (F1) -> `<especialista-2>` (F1) -> `<especialista-3>` (F2) ->
`<revisor>` (F2.5) -> `<compilador>` (F3)

Criar a partir de `scripts/padroes/skill-template.md`.

### Subagentes (`.claude/agents/`)

`<subagente-1>`, `<subagente-2>` — usados para lotes paralelos.

### Scripts Deterministicos (`scripts/`)

`<gerar-*.py>`, `<validar-*.py>`, `<empacotar-*.py>` — criar a partir de
`scripts/padroes/script-template.py`.

### Gates de Conteudo (merito, alem da estrutura)

`<validar-criterio-1>.py`, `<validar-criterio-2>.py` — registrados no campo
`gates` do registro de tipos; o auditor os encadeia no modo `--estrito`.

### Token Economy Skills (UNIVERSAL — nao remover)

`caveman`, `headroom`, `lean-ctx`, `rtk-memory`, `pre-flight-check`

## 3. MCPs `[CUSTOMIZAR]`

Declarados em `.mcp.json` na raiz (a partir de `scripts/padroes/mcp-template.js`).
Padrao sugerido:

- `db_state` (SQLite) — estado da esteira (R11)
- `file_writer` — grava artefatos
- busca web -> `WebSearch`/`WebFetch` nativos, sem MCP dedicado

## 4. Templates `[CUSTOMIZAR]`

`templates/` guarda os moldes de saida do seu dominio (`.typ`, `.md`, `.html`).
Vazio neste repositorio por design: molde de saida e 100% especifico.

## 5. Fluxo Operacional `[CUSTOMIZAR]`

Forma canonica de 4 fases — troque o conteudo, mantenha a forma:

1. **Input:** operador define o escopo -> `/esbocar <tema>`
2. **Fase 1 (pesquisa/analise):** coleta deterministica -> indexacao ->
   estrutura macro aprovada pelo operador
3. **Fase 2 (producao):** lotes paralelos de subagentes com retentativa e
   backoff (max. 3), cada lote com auto-validacao
4. **Fase 2.5 (auditoria):** `auditar.py --estrito` encadeia os gates ->
   `<revisor>` corrige a causa, nao o sintoma
5. **Fase 3 (compilacao):** merge + pre/pos-textuais + artefato final
6. **Entrega:** `validar-artefatos.py --todos --estrito` (testa se cada arquivo
   ABRE) -> empacotamento. O pacote leva **so o que esta finalizado e abre**,
   com um LEIA-ME que declara o que ficou de fora e por que.

**Output:** cada entrega vive em `output/<slug>/` com as raizes de tipo dentro
do hub. Nao criar raizes planas no topo.

### Entrega de Sessao — `relatorios/`

Toda sessao de trabalho encerra com um relatorio em `relatorios/`
(`<YYYY-MM-DD>-<tema-da-sessao>.md`, e PDF se o projeto compilar).
Conteudo minimo: contexto, bugs descobertos/corrigidos (causa->fix), arquivos
alterados, validacoes rodadas, commits feitos e resumo de entregas.

## 6. Portabilidade Multi-IDE (UNIVERSAL — nao remover)

Fonte unica: `.claude/`.

- **Junctions:** `agentic/*`, `.opencode/{agents,commands,skills,mcp-servers,settings.json}`
  e `.agents/{agents,commands}` -> `.claude/*`.
- **`.agents/` recebe apenas `agents/` e `commands/`** — nunca `skills/` nem
  `mcp-servers/`: `.agents/` e o diretorio de agentes do Codebuff/Freebuff, que
  **importa e executa** os `.js`/`.mjs` encontrados ali dentro; um script que
  roda no import e chama `process.exit(1)` derruba o CLI inteiro.
- **Hardlinks:** `AGENTS.md`->`CLAUDE.md`, `.cursor/rules/`->`CLAUDE.md`,
  `.cursor/mcp.json`->`.mcp.json`.
- **Schemas MCP que diferem sao GERADOS por script** (nao link):
  `.vscode/mcp.json` e `opencode.json` — ver `scripts/setup-links.*`, que pula
  a geracao se o script sincronizador nao existir no projeto.
- **Hook git `pre-commit`** (mecaniza R15 e R16): fonte versionada em
  `scripts/hooks/pre-commit`, **copiado** para `.git/hooks/pre-commit` — nao e
  link, porque `.git/hooks` nao aceita hardlink/junction de forma confiavel.
- **Recriar apos clone:** `scripts/setup-links.ps1` (Win) ou
  `scripts/setup-links.sh` (Mac/Linux) — ambos recopiam o hook.
- **Submodules:** clonar com `git clone --recurse-submodules` ou rodar
  `git submodule update --init --recursive` depois.

## 7. RTK Scratchpad

> Aprendizados de sessoes anteriores vivem em `RTK-SCRATCHPAD.md` (arquivo
> externo na raiz do projeto), para manter este arquivo estavel como prefixo de
> cache. Nao e lido automaticamente pelo agente; consultar sob demanda.
> Novas entradas: SEMPRE appendar em `RTK-SCRATCHPAD.md`, nunca aqui.
> Ver skill `rtk-memory` para o protocolo de registro.
