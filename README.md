# Fábrica Universal — Infraestrutura Reutilizável

> Componentes universais de uma fábrica agêntica — **use como submodule em
> qualquer projeto**.
> **Setup:** 5 minutos · **Domínios:** SaaS, Pesquisa, Consultoria, Publicações,
> o que for.

Este repositório contém **apenas o que não depende de domínio**: governança,
economia de tokens, portabilidade multi-IDE, gates mecânicos e os quatro
templates de padrão. Nada de skills de redação, comandos de criação ou moldes de
saída — isso é seu, e você escreve.

## O que você ganha

- **Governança central** — `CLAUDE.md` com R1–R17 e a Seção 0 de economia
- **5 skills de economia de tokens** — `caveman`, `headroom`, `lean-ctx`,
  `rtk-memory`, `pre-flight-check`
- **Portabilidade multi-IDE** — Claude Code, Cursor, OpenCode, Codebuff,
  Windsurf, Cline, VS Code, a partir de uma fonte única
- **Infraestrutura pronta** — hook `pre-commit` (segredos + suíte verde),
  workflows de CI, validador de integração
- **Padrões reutilizáveis** — templates de skill, script, comando e MCP
- **Economia severa** — 50–70% menos tokens

## Início rápido

### Projeto novo

```bash
mkdir meu-projeto && cd meu-projeto
git init

git submodule add https://github.com/Heverton-web/fabrica-universal.git fabrica-universal
git submodule update --init --recursive

cp -r fabrica-universal/.claude .
mkdir -p scripts && cp -r fabrica-universal/scripts/* scripts/

bash scripts/setup-links.sh meu-projeto     # Windows: .\scripts\setup-links.ps1
python scripts/validate.py
```

### Projeto existente

```bash
cd seu-projeto
git submodule add https://github.com/Heverton-web/fabrica-universal.git fabrica-universal

cp -r fabrica-universal/.claude/skills/. .claude/skills/   # skills: seguras
cp fabrica-universal/.claude/RTK.md .claude/
# .claude/CLAUDE.md e settings.json: MERGEIE à mão se já existirem.

cp -r fabrica-universal/scripts/padroes scripts/
cp fabrica-universal/scripts/{setup-links.ps1,setup-links.sh,validate.py} scripts/
mkdir -p scripts/hooks && cp fabrica-universal/scripts/hooks/pre-commit scripts/hooks/

bash scripts/setup-links.sh seu-projeto
python scripts/validate.py
```

## Estrutura pós-setup

```
seu-projeto/
├── fabrica-universal/        ← submodule (leitura, nunca editado)
├── .claude/                  ← FONTE ÚNICA (copiada, sua para customizar)
│   ├── CLAUDE.md             governança — customize os blocos [CUSTOMIZAR]
│   ├── RTK.md                guia de economia de tokens
│   ├── settings.json         hooks do harness
│   ├── skills/               5 de economia (do submodule) + as suas
│   ├── agents/               seus subagentes
│   └── commands/             seus comandos
├── scripts/
│   ├── setup-links.ps1/.sh   portabilidade
│   ├── validate.py           validador de integração
│   ├── pdf_typst.py          Markdown → PDF (Pandoc → Typst)
│   ├── hooks/pre-commit      gate de segredos + suíte verde
│   ├── padroes/              4 templates de padrão
│   └── <seus-scripts>.py
├── CLAUDE.md, AGENTS.md, agentic/, .agents/, .opencode/, .cursor/  ← GERADOS
└── .git/hooks/pre-commit     ← copiado por setup-links
```

A fonte é `.claude/`. Todo o resto na última linha é **espelho gerado** por
`setup-links` e vem ignorado no `.gitignore` — edite sempre `.claude/CLAUDE.md`,
nunca um espelho.

## Customizar para seu domínio

**1. `CLAUDE.md`** — troque `<SEU-PROJETO>` e preencha os blocos
`[CUSTOMIZAR]` (Seções 1 a 5). **Mantenha** a Seção 0 (economia), R1–R17 e a
Seção 6 (portabilidade). `validate.py` avisa enquanto sobrar placeholder.

**2. Skills de domínio**

```bash
mkdir -p .claude/skills/seu-especialista
cp scripts/padroes/skill-template.md .claude/skills/seu-especialista/SKILL.md
```

**3. Comandos**

```bash
cp scripts/padroes/command-template.md .claude/commands/seu-comando.md
```

**4. Gates de validação**

```bash
cp scripts/padroes/script-template.py scripts/validar-seu-criterio.py
```

Detalhes de cada padrão: [docs/PADROES.md](docs/PADROES.md).

## Atualizar o submodule

```bash
git submodule update --remote fabrica-universal

cp -r fabrica-universal/.claude/skills/. .claude/skills/   # skills: sobrescreva
cp fabrica-universal/.claude/CLAUDE.md .claude/CLAUDE.md.upstream  # CLAUDE.md: merge à mão

bash scripts/setup-links.sh
git add fabrica-universal && git commit -m "chore(submodule): atualizar fabrica-universal"
```

**Regra:** skills podem ser sobrescritas; `CLAUDE.md` nunca — ele está
customizado no seu projeto.

## Validar

```bash
python scripts/validate.py            # integração do projeto consumidor
python scripts/validate.py --estrito  # avisos também reprovam

# rodando de dentro deste repositório:
python tests/test-syntax.py
bash tests/test-integration.sh
bash tests/test-junctions.sh
```

## Exemplos por domínio

| Domínio | Squad | Comandos |
|---|---|---|
| **SaaS** | product-manager → architect → dev-senior → qa-engineer | `/criar-feature`, `/debugar-issue`, `/deploy-seguro` |
| **Pesquisa** | literature-researcher → methodologist → statistician → writer | `/criar-paper`, `/criar-dissertation` |
| **Consultoria** | estrategista → consultor-senior → designer | `/criar-proposta`, `/criar-relatorio` |

Passo a passo dos três: [docs/EXEMPLOS.md](docs/EXEMPLOS.md).

## Documentação

- [UNIVERSAL-vs-ESPECIFICO](docs/UNIVERSAL-vs-ESPECIFICO.md) — o que copiar, o que reescrever
- [PADROES](docs/PADROES.md) — skill, script, comando, MCP e hooks
- [TROUBLESHOOTING](docs/TROUBLESHOOTING.md) — submodule, links, Windows, CI
- [EXEMPLOS](docs/EXEMPLOS.md) — SaaS, Pesquisa, Consultoria
- [QUICKSTART](QUICKSTART.md) — 5 minutos

## Contribuindo

Encontrou um padrão melhor? Abra uma issue com o template
[Solicitar novo padrão](.github/ISSUE_TEMPLATE/request-pattern.md).

O critério de entrada é um só: **se você não consegue citar três domínios
diferentes onde o padrão se aplica sem mudar a lógica, ele não é universal** — o
lugar dele é `scripts/padroes/` como template, não como implementação.

## Licença

MIT — use livremente em projetos comerciais e pessoais.
