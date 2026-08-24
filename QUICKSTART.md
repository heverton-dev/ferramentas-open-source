# QUICKSTART — 5 minutos

**Resultado:** projeto com governança, economia de tokens, portabilidade
multi-IDE e gates mecânicos funcionando.

## 1. Adicionar o submodule (1 min)

```bash
mkdir meu-projeto && cd meu-projeto
git init

git submodule add https://github.com/Heverton-web/fabrica-universal.git fabrica-universal
git submodule update --init --recursive
```

Em projeto que já existe: rode só os dois comandos `git submodule`.

## 2. Copiar o universal (1 min)

```bash
cp -r fabrica-universal/.claude .
mkdir -p scripts && cp -r fabrica-universal/scripts/* scripts/
```

Copiar, e não linkar, é de propósito: o `.claude/` do seu projeto é **seu** para
customizar. O submodule fica como fonte de atualização, nunca como dependência
em tempo de execução.

## 3. Setup de portabilidade (1 min)

**Windows:**
```powershell
powershell -ExecutionPolicy Bypass -File scripts\setup-links.ps1 -RuleName meu-projeto
```

**Mac/Linux:**
```bash
bash scripts/setup-links.sh meu-projeto
```

Isto gera os espelhos de `.claude/CLAUDE.md` (`CLAUDE.md`, `AGENTS.md`,
`.cursor/`, `.windsurfrules`, `.clinerules`, `agentic/`, `.opencode/`,
`.agents/`) e instala o hook `pre-commit`.

## 4. Validar (1 min)

```bash
python scripts/validate.py
```

Esperado:

```
[OK]  CLAUDE.md presente — .claude\CLAUDE.md
[!]   CLAUDE.md customizado — ainda contem placeholders (<SEU-PROJETO> / [CUSTOMIZAR])
[OK]  Skills de economia (5) — caveman, headroom, lean-ctx, rtk-memory, pre-flight-check
[OK]  Scripts universais — setup-links.ps1, setup-links.sh, validate.py
[OK]  Sintaxe Python (scripts/) — 3 arquivo(s)
[OK]  Portabilidade (agentic/)
[OK]  Espelho AGENTS.md
[OK]  Hook pre-commit (fonte)
[OK]  Hook pre-commit (instalado)

Setup validado — 1 aviso(s)
```

O aviso sobre placeholders é esperado até o passo 5.

## 5. Customizar e commitar (1 min)

```bash
# Edite a FONTE, nunca os espelhos:
vim .claude/CLAUDE.md
#   - troque <SEU-PROJETO>
#   - preencha os blocos [CUSTOMIZAR] (Seções 1 a 5)
#   - MANTENHA: Seção 0, R1–R17, Seção 6

bash scripts/setup-links.sh meu-projeto   # repropaga os espelhos
python scripts/validate.py --estrito      # agora sem avisos

git add -A
git commit -m "chore(init): setup fabrica-universal"
```

## Pronto

Seu projeto tem:

- Governança carregada em todo harness (`alwaysApply: true`)
- 5 skills de economia de tokens
- Espelhos de instrução para 7 IDEs a partir de uma fonte
- `pre-commit` bloqueando segredo e suíte vermelha
- Validador de integração rodável a qualquer momento

**Próximo passo:** escrever o específico — skills, comandos e gates do seu
domínio, a partir de `scripts/padroes/`. Ver
[README > Customizar](README.md#customizar-para-seu-domínio) e
[docs/PADROES.md](docs/PADROES.md).

**Deu ruim?** [docs/TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md)
