# Padrões Reutilizáveis

Quatro padrões cobrem quase tudo que se constrói sobre esta infraestrutura:
**skill**, **script**, **comando** e **MCP**. Os arquivos executáveis vivem em
`scripts/padroes/` — este documento explica *quando* usar cada um e *por que* o
padrão tem a forma que tem.

## Como escolher

| Você precisa de… | Use | Custo LLM |
|---|---|---|
| Julgamento, redação, síntese | **Skill** | alto |
| Transformação determinística de arquivo | **Script** | zero |
| Orquestrar várias fases com gates | **Comando** | médio |
| Consultar estado vivo ou agir com efeito colateral | **MCP** | baixo |

**Regra de decisão (R8 do CLAUDE.md):** se um script resolve, não gaste LLM.
Gerar, validar, contar, converter e empacotar são tarefas de script. Skill é para
o que exige julgamento — e julgamento é a parte cara.

O erro mais comum é escrever como skill algo que era um `for` com um `if`.

## 1. Skill

Arquivo: `scripts/padroes/skill-template.md` → `.claude/skills/<nome>/SKILL.md`

```markdown
---
name: <seu-skill>
description: >
  Uma frase dizendo o que faz e quando ativar.
  Triggers: "<gatilho 1>", "<gatilho 2>"
---

# Skill_<Nome>

Você é <especialista>. Sua responsabilidade é <resultado único e verificável>.

## Regras herdadas do CLAUDE.md
## Entrada
## Passo 1 — <fase 1>
## Passo 2 — <fase 2>
## Passo 3 — <fase 3>
## Saída
## Checklist de Entrega
## Quando NÃO usar este skill
```

**O que o padrão garante:**

- **`description` é o único texto lido para decidir carregar o skill.** Descrição
  genérica ("ajuda com documentos") faz o skill ser carregado sempre ou nunca.
  Descreva o gatilho concreto.
- **Uma responsabilidade por skill.** Se o checklist tem dois resultados
  independentes, são dois skills.
- **`Quando NÃO usar`** não é cortesia: um skill que nunca recusa trabalho é um
  skill que será chamado errado.

## 2. Script determinístico

Arquivo: `scripts/padroes/script-template.py` → `scripts/<nome>.py`

```python
def console_utf8():
    """Windows: sem isto, print não-ASCII quebra em cp1252."""
    for f in (sys.stdout, sys.stderr):
        try:
            f.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass

def executar(alvo, estrito=False):
    """Toda a regra de negócio aqui — testável sem subprocess."""
    dados = {"alvo": str(alvo), "problemas": [], "avisos": []}
    # ...
    return (not dados["problemas"]), dados

def main():
    console_utf8()
    relatorio = {"status": "falha"}
    try:
        ok, dados = executar(args.alvo, estrito=args.estrito)
        relatorio.update(dados)
        relatorio["status"] = "sucesso" if ok else "falha"
    finally:
        destino.write_text(json.dumps(relatorio, ensure_ascii=False, indent=2))
    return 0 if relatorio["status"] == "sucesso" else 1
```

**Os quatro invariantes:**

1. **`console_utf8()` sempre.** Windows usa cp1252 por padrão; um emoji num
   `print` derruba o script inteiro com `UnicodeEncodeError` — e o erro aparece
   longe da causa.
2. **Relatório gravado no `finally`.** Um gate que morre sem relatório é
   indistinguível de um gate que nunca rodou. O `finally` garante que sempre
   existe um veredito em disco.
3. **`exit 0` = passou, `exit 1` = reprovou.** É isto que permite encadear o
   script em hooks, CI e no auditor sem nenhuma cola extra.
4. **Lógica em `executar()`, I/O em `main()`.** Assim o teste chama a função,
   não um subprocess.

**Idempotência (R10):** rodar duas vezes produz o mesmo resultado. Se o script
acumula, renomeia ou incrementa, ele não é um gate — é uma migração, e migração
precisa de marca de "já rodou".

## 3. Comando

Arquivo: `scripts/padroes/command-template.md` → `.claude/commands/<nome>.md`

```markdown
---
description: <o que faz, em uma frase>
argument-hint: <alvo> [--opcao]
---

## REQUISITOS CONTRATUAIS

| # | Requisito | Spec |
|---|---|---|
| R1 | <o que o resultado precisa cumprir> | <como verificar> |

## Passo 0 — Preparação
## Passo 1..N — <fases>
## Checklist Final
## Falhas Conhecidas
```

**Por que a tabela de requisitos vem primeiro:** requisito sem a coluna "Spec"
preenchida não é requisito — é desejo. Ou vira gate verificável, ou sai da
tabela. Isso mantém o comando honesto sobre o que ele realmente garante.

**Passo 0 é obrigatório** e sempre faz três coisas: valida a entrada, lê o
estado de disco (nunca da conversa — R11) e, se o artefato já existe, pergunta
ao operador entre **Criar Nova** e **Sobrescrever** (R17).

## 4. MCP server

Arquivo: `scripts/padroes/mcp-template.js` → `scripts/mcp/<nome>.js`

Registro em `.mcp.json` na raiz:

```json
{
  "mcpServers": {
    "seu-mcp": {
      "command": "node",
      "args": ["scripts/mcp/seu-mcp.js"]
    }
  }
}
```

**Quando MCP em vez de script:** use MCP quando o agente precisa consultar
**estado vivo** ou executar ação com efeito colateral controlado, **várias vezes
na mesma sessão**. Para transformação pura de arquivo, script é mais barato e
mais testável.

**Duas armadilhas do transporte stdio:**

1. **Nunca escreva em `stdout` fora do protocolo.** Um `console.log` solto
   corrompe o frame JSON-RPC e o agente perde a sessão do MCP inteira. Log de
   diagnóstico vai em `stderr`.
2. **Erro vira resposta com `isError`, não exceção solta.** Exceção derruba o
   servidor; `isError` deixa o agente ler a mensagem e corrigir a chamada.

Depois de editar `.mcp.json`, rode `scripts/setup-links.*` para propagar o
espelho `.cursor/mcp.json` e gerar os schemas divergentes (VS Code, OpenCode).

## 5. Hooks

**Hook do harness** (`.claude/settings.json`): roda em eventos da sessão
(`PostToolUse`, `SessionStart`). Regra de ouro: **no-op silencioso quando a
ferramenta não existe.** Todo comando começa com uma guarda
`command -v <tool> >/dev/null 2>&1 || exit 0` — senão o hook vira ruído em toda
máquina que não tem aquela ferramenta instalada.

**Hook git** (`scripts/hooks/pre-commit`): mecaniza R15 (segredos) e R16 (nunca
commitar vermelho). Fonte versionada em `scripts/hooks/`, **copiado** para
`.git/hooks/` pelo `setup-links` — não é link, porque `.git/hooks` não aceita
hardlink/junction de forma confiável em todo SO.

Em POSIX `sh`, itere padrões com `for`, nunca com `while` dentro de um pipe: o
`while` roda em subshell e o `exit 1` não chega ao hook — o commit passa com o
segredo dentro.

## 6. Onde cada padrão vive

```
.claude/
├── CLAUDE.md              governança (universal + [CUSTOMIZAR])
├── settings.json          hooks do harness
├── skills/<nome>/SKILL.md  ← skill-template.md
├── agents/<nome>.md        subagentes de lote
└── commands/<nome>.md      ← command-template.md

scripts/
├── <gerar|validar|empacotar>-*.py   ← script-template.py
├── mcp/<nome>.js                     ← mcp-template.js
├── hooks/pre-commit                  gate mecânico
└── padroes/                          os templates em si

.mcp.json                 registro dos MCP servers
templates/                moldes de saída (100% específicos)
```
