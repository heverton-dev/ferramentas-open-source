# Troubleshooting

Problemas reais encontrados ao usar esta infraestrutura, com a causa — não só o
comando que faz a dor passar.

## Submodule

### O submodule vem vazio depois de clonar

**Sintoma:** `fabrica-universal/` existe mas está vazia.

**Causa:** `git clone` não baixa submodules por padrão; ele só registra o ponteiro.

```bash
git submodule update --init --recursive
# ou, no clone:
git clone --recurse-submodules <seu-repo>
```

### `git submodule update --remote` não traz nada

**Causa:** o submodule está fixado num commit, e `--remote` segue a branch
configurada em `.gitmodules`. Se não houver `branch`, ele usa `HEAD` do remoto.

```bash
git config -f .gitmodules submodule.fabrica-universal.branch main
git submodule update --remote fabrica-universal
git add .gitmodules fabrica-universal
git commit -m "chore(submodule): fixar branch main"
```

### Atualizei o submodule e perdi minhas customizações do CLAUDE.md

**Causa:** o `.claude/CLAUDE.md` do seu projeto é uma **cópia**, não um link para
o submodule — de propósito, para você poder customizar. Se você re-copiou por
cima, sobrescreveu.

```bash
# Traga a versão nova ao lado, não por cima:
cp fabrica-universal/.claude/CLAUDE.md .claude/CLAUDE.md.upstream
git diff --no-index .claude/CLAUDE.md .claude/CLAUDE.md.upstream
# Mergeie à mão o que mudou nas seções universais (0, R1–R17, 6).
```

Regra: **skills** podem ser sobrescritas na atualização; **CLAUDE.md** não.

### `git submodule add` falha com "already exists in the index"

```bash
git rm -r --cached fabrica-universal
rm -rf .git/modules/fabrica-universal
git submodule add <url> fabrica-universal
```

## Links de portabilidade

### `setup-links.ps1` falha com "acesso negado"

**Causa:** criação de link em pasta protegida, ou o alvo está aberto em outro
programa. O script usa hardlink de arquivo e junction de pasta justamente para
**não** exigir elevação — se pediu Admin, o problema é outro (antivírus,
OneDrive/pasta sincronizada, ou o arquivo travado por um editor).

```powershell
powershell -ExecutionPolicy Bypass -File scripts\setup-links.ps1
```

Se o repositório está dentro de uma pasta sincronizada (OneDrive, Dropbox,
Google Drive), mova-o para fora: sincronizadores reescrevem arquivos e quebram
hardlinks silenciosamente.

### `AGENTS.md` desalinhou do `CLAUDE.md` sozinho

**Causa:** editor que salva com "escreve arquivo novo + rename" — padrão comum
no VS Code e em vários formatadores. Isso desvincula o inode: o arquivo continua
*sendo* um hardlink de outros espelhos, só que não mais deste `CLAUDE.md`.

Por isso `setup-links.ps1` compara **hash de conteúdo**, não `LinkType`. Basta
re-rodar:

```powershell
.\scripts\setup-links.ps1
```

E edite sempre `.claude/CLAUDE.md` — nunca os espelhos.

### O CLI do Codebuff/Freebuff morre ao iniciar

**Causa:** `.agents/` foi exposto a `skills/` ou `mcp-servers/`. O Codebuff
**importa e executa** todo `.js`/`.mjs` que encontra em `.agents/`. Um script que
roda no import e chama `process.exit(1)` derruba o CLI inteiro.

`.agents/` recebe **apenas** `agents/` e `commands/` (só `.md`). Skills e MCP
servers continuam disponíveis via `agentic/` e `.opencode/`.

```bash
rm -rf .agents/skills .agents/mcp-servers
bash tests/test-junctions.sh   # o teste reprova exatamente esse caso
```

### `test-junctions.sh` diz "nenhum link encontrado" no CI

Esperado. Links de portabilidade são artefato de máquina local, não conteúdo
versionado — o teste sai com 0 e um aviso em checkout limpo.

## Validação

### `validate.py` reprova com "CLAUDE.md sem alwaysApply: true"

O frontmatter precisa das três linhas, **no topo do arquivo**, sem linha em
branco antes:

```markdown
---
description: ...
alwaysApply: true
---
```

Sem `alwaysApply: true`, o Cursor e outros harnesses não carregam a governança —
o projeto roda sem regra nenhuma e ninguém percebe.

### `validate.py` avisa "ainda contém placeholders"

Não é erro, é lembrete: `<SEU-PROJETO>` e `[CUSTOMIZAR]` continuam no
`CLAUDE.md`. Some quando você customizar. Para tratar como falha:
`python scripts/validate.py --estrito`.

### `python -m py_compile scripts/*.py` funciona no Git Bash e falha no PowerShell

**Causa:** o PowerShell não expande glob para argumentos de programa nativo — ele
passa a string `scripts/*.py` literalmente.

```powershell
Get-ChildItem scripts\*.py | ForEach-Object { python -m py_compile $_.FullName }
```

Ou use `python tests/test-syntax.py`, que faz a varredura em Python e é portável.

## Hook pre-commit

### O hook não roda

```bash
ls -la .git/hooks/pre-commit      # existe?
chmod +x .git/hooks/pre-commit    # é executável?
```

`.git/hooks/` não é versionado — depois de clonar, sempre rode `setup-links`.

### O hook bloqueia um falso positivo de segredo

O gate casa padrões de credencial (`sk-…`, `AKIA…`, `ghp_…`, chave PEM). Um
exemplo em documentação pode casar.

```bash
# 1) Prefira neutralizar o exemplo: sk-EXEMPLO-NAO-E-CHAVE
# 2) Só se for realmente falso positivo:
git commit --no-verify
```

Nunca use `--no-verify` por hábito — o dia em que for um segredo de verdade, o
hábito é que decide.

### O hook demora demais

Ele roda a suíte de testes (R16). Se a suíte leva minutos, o problema é a suíte,
não o hook: mova o que é lento para o CI e deixe no pre-commit só o que é rápido.
Os gates 2 e 3 do hook só disparam se houver pytest/npm test configurados.

## Windows

### `UnicodeEncodeError: 'charmap' codec can't encode character`

**Causa:** console em cp1252 e `print` com caractere não-ASCII.

```python
def console_utf8():
    for f in (sys.stdout, sys.stderr):
        try:
            f.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass
```

Chame como primeira linha de `main()`. É obrigatório (R11 da Seção 0) — o
`script-template.py` já vem com ela.

### Caminho longo demais / "The system cannot find the path specified"

MAX_PATH do Windows é 260 caracteres. Nomes de artefato derivados de títulos por
extenso estouram fácil (R14). Use slug curto e hierarquia rasa. Alternativa
global:

```powershell
git config --global core.longpaths true
```

## CI

### O workflow falha em `shellcheck`

O job usa `-S error` (só erros, não estilo). Se falhou, é bug real de shell —
normalmente variável não citada onde importa, ou `[` no lugar de `[[`.

### O smoke test do consumidor falha em `git submodule add ../fonte`

Git bloqueia submodule por protocolo `file://` desde as correções de segurança de
2022. O workflow já contorna com `-c protocol.file.allow=always` — isso é
aceitável **só em CI**, com um caminho local que o próprio job criou.
