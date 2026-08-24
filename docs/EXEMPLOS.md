# Exemplos por Domínio

Três projetos com a mesma infraestrutura e nada em comum no conteúdo. O setup
universal é idêntico nos três; o que muda começa no Passo 2.

## Setup comum (idêntico nos três)

```bash
mkdir <projeto> && cd <projeto>
git init

git submodule add https://github.com/Heverton-web/fabrica-universal.git fabrica-universal
git submodule update --init --recursive

cp -r fabrica-universal/.claude .
mkdir -p scripts && cp -r fabrica-universal/scripts/* scripts/

bash scripts/setup-links.sh <projeto>     # Windows: .\scripts\setup-links.ps1
python scripts/validate.py
```

A partir daqui, cada domínio preenche os blocos `[CUSTOMIZAR]` do
`.claude/CLAUDE.md` — Seções 1 (tipos), 2 (squad), 3 (MCPs), 4 (templates) e
5 (fluxo). As Seções 0, R1–R17 e 6 ficam intactas.

## 1. SaaS — desenvolvimento de features

**Squad (Seção 2):**

```
product-manager → architect → dev-senior → qa-engineer
```

- `product-manager` — traduz pedido em requisito verificável
- `architect` — decide o desenho e registra o porquê
- `dev-senior` — implementa
- `qa-engineer` — cobertura ≥90% e teste de regressão

**Comandos (`.claude/commands/`):**

| Comando | Fluxo |
|---|---|
| `/criar-feature` | épico → design → implementação → testes |
| `/debugar-issue` | triagem → reprodução → fix → regressão |
| `/refactor-seguro` | caracterizar com teste → refatorar → provar equivalência |
| `/deploy-seguro` | staging → smoke → produção → rollback pronto |

**Gates (`scripts/`):**

```
validar-testes.py        cobertura ≥ 90%
validar-performance.py   P99 abaixo do threshold do serviço
validar-seguranca.py     OWASP Top 10 no diff
validar-migracoes.py     migração é reversível
```

**Registro de tipos (`scripts/tipos.py`):**

```python
TIPOS = {
    "feature":  {"natureza": "geracao",  "custo_llm": "alto",
                 "gates": ["validar-testes", "validar-seguranca"]},
    "refactor": {"natureza": "transformacao", "custo_llm": "medio",
                 "gates": ["validar-testes", "validar-performance"]},
    "hotfix":   {"natureza": "correcao", "custo_llm": "baixo",
                 "gates": ["validar-testes"]},
}
```

**Onde R17 pega:** deploy em produção é etapa opcional. Nunca dispara sozinho ao
fim do `/criar-feature` — o operador escolhe.

## 2. Pesquisa acadêmica

**Squad:**

```
literature-researcher → methodologist → statistician → writer
```

- `literature-researcher` — busca e sintetiza a literatura
- `methodologist` — desenha o estudo e checa validade
- `statistician` — análise, effect size, poder estatístico
- `writer` — o artigo final

**Comandos:**

| Comando | Fluxo |
|---|---|
| `/criar-paper` | pesquisa → metodologia → análise → draft |
| `/criar-dissertation` | capítulos → revisão → compilação |
| `/criar-poster` | resumo visual a partir do paper |

**Gates:**

```
validar-datasets.py      integridade e reprodutibilidade
validar-metodologia.py   ética e validade interna/externa
validar-statistics.py    p-values, effect sizes, correção múltipla
validar-referencias.py   DOI/URL resolvem de verdade
```

**Registro de tipos:**

```python
TIPOS = {
    "paper":        {"natureza": "geracao",   "custo_llm": "alto"},
    "dissertation": {"natureza": "geracao",   "custo_llm": "alto"},
    "poster":       {"natureza": "extracao",  "custo_llm": "zero"},
}
```

**Onde o determinismo (R8) paga mais:** mineração de fontes via APIs abertas
(OpenAlex, Crossref, arXiv, PubMed) tem custo LLM **zero** e resultado melhor que
pedir referências a um modelo — que alucina DOI. Gerar a bibliografia é script;
interpretar a literatura é skill.

**Onde a derivação paga:** poster e resumo **comprimem** o paper (barato,
cascateie). O caminho inverso — expandir um resumo em paper — custa geração e
não deve ser cascateado.

## 3. Consultoria

**Squad:**

```
estrategista → consultor-senior → designer
```

- `estrategista` — descoberta e diagnóstico
- `consultor-senior` — recomendações e trade-offs
- `designer` — apresentação e materiais

**Comandos:**

| Comando | Fluxo |
|---|---|
| `/criar-proposta` | discovery → análise → recomendações → preço |
| `/criar-relatorio` | estrutura → draft → revisão |
| `/criar-playbook` | extração do que já foi entregue → polimento |

**Gates:**

```
validar-recomendacoes.py   toda recomendação tem dono, prazo e ROI estimado
validar-compliance.py      revisão legal/regulatória
validar-apresentacao.py    uma ideia por slide, sem jargão não definido
```

**Registro de tipos:**

```python
TIPOS = {
    "proposta":  {"natureza": "geracao",  "custo_llm": "alto"},
    "relatorio": {"natureza": "geracao",  "custo_llm": "medio"},
    "playbook":  {"natureza": "extracao", "custo_llm": "zero"},
}
```

**Onde R7 pega mais forte:** o que vai para o cliente não é resumido nem
"melhorado" por economia de token. Comprimir entrega é a única economia que sai
mais cara do que economiza.

## O que os três têm em comum

Nada no conteúdo. Tudo na forma:

1. **Squad em cadeia**, com um revisor antes do compilador — o revisor corrige a
   causa, não o sintoma.
2. **Gates mecânicos** com `exit 0/1`, encadeados pelo auditor em `--estrito`.
   Qualidade que não vira script não é gate, é intenção.
3. **Registro declarativo de tipos** — tipo novo custa 1 entrada (R12).
4. **Determinismo primeiro** — o que um script resolve não gasta LLM (R8).
5. **Etapas opcionais são sempre opcionais** — deploy, campanha, publicação
   nunca disparam sozinhos (R17).

É por isso que a separação universal/específico funciona: a forma se repete entre
domínios que não compartilham vocabulário nenhum.

## Adaptando para um domínio não listado

1. Liste os **artefatos** que seu projeto entrega → viram o registro de tipos.
2. Liste as **decisões de julgamento** no caminho → viram skills.
3. Liste as **verificações** que hoje você faz no olho → viram gates (`.py`).
4. Liste o que é **opcional** → entra no contrato do R17.
5. O resto (economia de tokens, portabilidade, hooks, CI) você não escreve —
   já veio no submodule.
