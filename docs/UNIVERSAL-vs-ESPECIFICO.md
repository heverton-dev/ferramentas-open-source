# UNIVERSAL vs. ESPECÍFICO — o que copiar, o que reescrever

**Versão:** 2 (listas em vez de tabelas — PDF-safe)
**Contexto:** quais componentes são replicáveis universalmente e quais são
específicos de um domínio.
**Objetivo:** evitar cópia cega. Um projeto novo consome APENAS o universal
(via submodule) e reescreve o ESPECÍFICO.

> **Nota de origem:** este documento nasceu da separação feita na *Fábrica
> Agêntica de Publicações*, e usa esse domínio como exemplo concreto ao longo do
> texto. Onde ler "livro", "capítulo" ou "ABNT", entenda "o artefato do seu
> domínio" — a classificação universal/específico não muda.

## ⚡ REGRA DE OURO

**UNIVERSAL (copiar 100%):**
- Estrutura e padrões (agnóstico de domínio)
- Infraestrutura (junctions, hooks, CI/CD)
- Governança (CLAUDE.md R0–R17)
- Economia de tokens (caveman, headroom, lean-ctx, RTK)

**ESPECÍFICO (usar como template, reescrever 100%):**
- Skills de redação/especialização
- Comandos de criação (workflow de domínio)
- Gates de validação (critérios de domínio)
- Templates de output (formato final)
- Framework de escrita (seções/estrutura)



## UNIVERSAL — COPIAR INTEGRALMENTE

### Governança & Padrões

**CLAUDE.md (Seção 0–7):**
- Seção 0: Economia Severa de Tokens → copiar 100%
- Seção 1: Regras Globais (R1–R17) → copiar ~80% (adaptar exemplos)
- Seção 2: Squad → copiar padrão, reescrever nomes
- Seção 3–7: Estrutura → copiar 100%

**RTK.md:**
- Guia completo de token economy
- Copiar 100% (sem adaptações)

**settings.json:**
- Hooks PostToolUse e SessionStart
- Copiar 100% (adaptar paths)

**Padrão de Skills:**
- Frontmatter (name, description)
- Estrutura de fluxo (Passo 1, 2, 3...)
- Checklist de entrega
- Copiar 100% (mudar conteúdo apenas)

### 5 Skills de Economia

1. **caveman** — Pensamento telegráfico (3–5 linhas)
2. **headroom** — Comprimir logs >7 linhas (3+4)
3. **lean-ctx** — Grep antes de read, offset/limit
4. **rtk-memory** — Rastreamento de economia por sessão
5. **pre-flight-check** — Validação pré-launch, evita loops

Copiar pastas inteiras (`.claude/skills/caveman`, etc.). Não adaptar.

### Padrões Técnicos

**Padrão de Comando:**
- Fases: P&D → Manufatura → Review → Entrega
- Checklist de requisitos contratuais
- Passo-a-passo estruturado
- Copiar 100%

**Padrão de Subagentes:**
- Atomização de tarefas
- Pool com lotes (4 paralelos)
- Retentativa 3x com backoff exponencial
- Barreira (aguarde todos antes do próximo lote)
- Escalação para revisor se falhas persistem
- Copiar 100%

**Padrão de Script Python:**
- Docstring com entrada/saída/garantias
- Função console_utf8() (UTF-8 everywhere)
- Estrutura: try → relatorio["status"] → finally → JSON
- Exit code 0 = sucesso, >0 = falha
- Idempotência (rodar 2x = mesmo resultado)
- Copiar 100%

**Padrão de MCP:**
- Registro declarativo em .mcp.json
- Função por MCP (db_state, file_writer, pdf_gen, code-review-graph)
- Copiar 100% (adaptar paths)

### Infraestrutura

**Portabilidade Multi-IDE:**
- setup-links.ps1 (Windows)
- setup-links.sh (Mac/Linux)
- Junctions: agentic/ → .claude/
- Hardlinks: CLAUDE.md
- Copiar 100%

**Pre-commit Hook:**
- Validação Python syntax
- Auditoria de gates (se output/ modificado)
- Checklist CLAUDE.md + .mcp.json
- Copiar 100%

**Auto-memória:**
- MEMORY.md (índice de memórias)
- RTK-SCRATCHPAD.md (aprendizados de sessão)
- Padrão: frontmatter + seções numeradas
- Copiar 100%

**Code-review-graph:**
- MCP de inteligência estrutural
- PostToolUse hook para atualização automática
- Copiar 100% (instalar via `uvx`)



## ESPECÍFICO — USAR COMO TEMPLATE, REESCREVER 100%

### Skills de Redação/Especialização

**Fábrica (exemplos):**
- pesquisador: varredura web + dossiê RAG
- arquiteto: sumário macro + planejamento
- estrategista: draft de capítulo
- redator-eita: texto final (7 seções EITA-V2)
- revisor-tecnico: peer review
- compilador-abnt: merge + formatação ABNT

**Para novo domínio:**
- Identificar 3–5 especialistas chave
- Criar skill para cada (usar padrão universal)
- Reescrever lógica 100% (mantém frontmatter + fluxo)

**Exemplo SaaS:**
- product-manager: visão + requisitos → feature spec
- architect: design → decisões arquiteturais
- dev-senior: implementação → código testado
- qa-engineer: testes → cobertura ≥90%
- (mantém caveman, headroom, lean-ctx para economia)

### Comandos de Criação

**Fábrica:**
- /criar-livro: tema → P&D → lotes → compilação
- /criar-tcc: estrutura acadêmica → fases
- /criar-artigo: compressão de livro
- /criar-playbook: extração de cards
- /compilar-mega-livro: orchestração final

**Para novo domínio:**
- /criar-feature: epic → design → implementação
- /debugar-issue: triage → fix → validation
- /refactor-seguro: teste-driven refactor
- /deploy-seguro: staging → produção
- (mantém padrão de fases + checklist)

**Reutilizar:**
- Padrão de orquestração (fases, barreiras, retentativa)
- Estrutura de checklist (requisitos contratuais)
- Lógica de escalação (defeitos → revisor)

### Gates de Validação

**Fábrica (exemplos):**
- validar-referencias: URL/DOI reais (reprova 4xx/DNS)
- validar-metricas: ≥1 métrica por capítulo com valor+unidade
- validar-escala: contorno em "Aplica" existe
- validar-afirmacoes: dado factual tem citação [N]
- validar-fontes: ≥70% referências classe A+B
- validar-codigo: smoke test de python/js/bash

**Para novo domínio:**
- validar-testes: cobertura ≥90%
- validar-performance: P99 latency < threshold
- validar-seguranca: OWASP top 10 check
- validar-compliance: legal/regulatory requirements
- validar-accessibility: a11y scores

**Reutilizar:**
- Padrão de script Python (console_utf8, JSON report, exit code)
- Estrutura de encadeamento (auditar-obra.py agrupa gates)
- Relatório de validação (lista de erros/alertas)

### Templates de Output

**Fábrica:**
- template_eita.md: 7 seções estruturadas
- template.typ: ABNT (capa, folha de rosto, CIP, sumário)
- template_lead_magnet.html: A4 + CTA

**Para novo domínio:**
- Seu template estruturado (N seções)
- Seu formato final (PDF, HTML, Markdown, PPTX)
- Seu CTA/call-to-action

**Reutilizar:**
- Padrão de gerador de esqueleto (`gerar-esqueleto-*.py`)
- Padrão de compilação (Pandoc → Typst ou seu motor)
- Metadados (frontmatter YAML para valores variáveis)

### Framework de Escrita

**Fábrica:**
- EITA-V2: 7 seções (Intro, Explica, Ilustra, Técnica, Aplica, Conclusão, Refs)
- Cada seção tem regras de tom, comprimento, citações
- Gates validam estrutura (headers numerados, seções completas)

**Para novo domínio:**
- Seu framework (quantas seções? Quais nomes?)
- Suas regras por seção (ton, comprimento, links obrigatórios?)
- Seus gates (validar headers, seções, citações)

**Reutilizar:**
- Padrão de parser (regex para headers, splitBatches)
- Padrão de validação (gerar-esqueleto → gates → revisão)
- Padrão de refinamento (reescrever → gates → compilação)

### Compilação Final

**Fábrica:**
- Input: Markdown (7 seções, referências ABNT)
- Processo: Pandoc → Typst → typst compile
- Output: PDF (ABNT formatado)

**Para novo domínio:**
- Input: seu formato (Markdown, Jupyter, Word, XML)
- Processo: seu pipeline (seu motor de conversão)
- Output: seu formato final (PDF, HTML, EPUB, PPTX)

**Reutilizar:**
- Padrão de compilador (entrada → processamento → output)
- Padrão de erro handling (relatorio JSON com sucesso/erros)
- Padrão de idempotência (rodar 2x = mesmo resultado)

### MCPs Específicas

**Fábrica:**
- db_state: SQLite com tabelas (obras, capitulos, status)
- Queries: listar fases, buscar por slug, atualizar status
- Uso: registrar progresso, auditoria, rastreamento

**Para novo domínio:**
- db_state: SQLite com suas tabelas (features, sprints, deployments)
- Queries: suas entidades + atributos
- Uso: seu contexto operacional

**Reutilizar:**
- Padrão de MCP (comando node, args com path db)
- Padrão de queries (SELECT/INSERT/UPDATE com relatorio JSON)
- Integração em settings.json

### Squad Especializada

**Fábrica:**
- F1 (Pesquisa): pesquisador → arquiteto (30 min)
- F2 (Manufatura): estrategista → redator-eita (4h, lotes 4)
- F2.5 (Review): auditar-obra → revisor-tecnico (1h)
- F3 (Entrega): compilador-abnt → PDF (30 min)
- F4 (Coleção): derivadas paralelas (2h)

**Para novo domínio:**
- Sua estrutura de fases (P&D? Design? Implementation? QA? Deployment?)
- Seus especialistas por fase (quem faz o quê?)
- Seus tempos estimados
- Suas métricas de sucesso

**Reutilizar:**
- Padrão de fases (estruturada, com barreiras)
- Padrão de pool (lotes paralelos)
- Padrão de retentativa (3x com escalação)
- Padrão de relatório (tempo + status + próximos passos)



## EXEMPLOS PRÁTICOS: COPIAR vs. REESCREVER

### Exemplo 1: Padrão de Skill (COPIAR)

**Universal (copiar 100%):**
```

name: nome-skill
description: Uma frase do resultado


# Skill_NomeCapitalizado

Você é o especialista em [DOMÍNIO].

## Regras
- REGRA 1, 2, 4 do CLAUDE.md

## Padrão de Fluxo
### Passo 1 — [Sua fase 1]
### Passo 2 — [Sua fase 2]
### Passo 3 — [Sua fase 3]

## Checklist de Entrega
- [ ] Artefato gerado
- [ ] Tests passando
- [ ] Commit feito
```

✅ Copiar frontmatter + estrutura. Reescrever apenas [DOMÍNIO], [fases], [checklist].



### Exemplo 2: Skill de Domínio (REESCREVER)

**Fábrica (redator-eita):**
```
Você é redator de manufatura final (EITA-V2).

## Seções obrigatórias
1. Introdução (acessível)
2. Explica (teoria)
3. Ilustra (analogia + diagrama)
4. Técnica (código + arquitetura, 60%)
5. Aplica (caso real, contorno)
6. Conclusão (síntese)
7. Referências (ABNT)
```

❌ Não copie. Reescreva para seu domínio:

**SaaS (feature-implementer):**
```
Você é implementador de features (Sprint).

## Seções obrigatórias
1. Context (por que existe, problem statement)
2. Design (arquitetura, decisões)
3. Implementation (código, padrões, 70%)
4. Tests (cobertura ≥90%, happy path + edge)
5. Deployment (staging → prod, rollback)
6. Monitoring (métricas, alertas)
7. Docs (README, API, runbook)
```



### Exemplo 3: Script Determinístico (COPIAR PADRÃO)

**Padrão universal:**
```python
#!/usr/bin/env python3
"""
<modulo>: <descricao>

Entrada: <seu input>
Saída: output/<slug>/relatorio-<modulo>.json

Garantias:
- Idempotente (rodar 2x = mesmo resultado)
- Sem side effects fora de output/
- Relatório JSON sempre gravado
- Exit code 0 = sucesso, >0 = falha
"""

import argparse, json, sys
from pathlib import Path

def console_utf8():
    for fluxo in (sys.stdout, sys.stderr):
        try:
            fluxo.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, OSError):
            pass

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("slug", help="slug-da-obra")
    parser.add_argument("--opcao", default="valor")
    args = parser.parse_args()
    
    relatorio = {"status": "falha", "erros": []}
    
    try:
        # ← SUA LÓGICA AQUI
        relatorio["status"] = "sucesso"
    except Exception as e:
        relatorio["erros"].append(str(e))
        return 1
    finally:
        Path(f"output/{args.slug}/relatorio-meu-script.json").write_text(
            json.dumps(relatorio, indent=2, ensure_ascii=False)
        )
    
    return 0 if relatorio["status"] == "sucesso" else 1

if __name__ == "__main__":
    console_utf8()
    sys.exit(main())
```

✅ Copiar estrutura completa. Reescrever apenas [SUA LÓGICA].



## BLUEPRINT DE REPLICAÇÃO — PASSO A PASSO

O blueprint abaixo é a versão **submodule**: você não clona um projeto inteiro
para depois deletar 60% dele. Você adiciona o universal e escreve só o seu.

### Fase 1: Consumir o universal (15 minutos)

```bash
mkdir meu-projeto && cd meu-projeto
git init

git submodule add https://github.com/Heverton-web/fabrica-universal.git fabrica-universal
git submodule update --init --recursive

cp -r fabrica-universal/.claude .
mkdir -p scripts && cp -r fabrica-universal/scripts/* scripts/

bash scripts/setup-links.sh meu-projeto      # Windows: .\scripts\setup-links.ps1
python scripts/validate.py
```

O que entrou (✅ universal, copiar 100%):

- `.claude/CLAUDE.md` — governança R0–R17
- `.claude/RTK.md` — guia de economia de tokens
- `.claude/settings.json` — hooks padrão
- `.claude/skills/{caveman,headroom,lean-ctx,rtk-memory,pre-flight-check}`
- `scripts/setup-links.ps1` / `.sh` — portabilidade multi-IDE
- `scripts/pdf_typst.py` — compilação Markdown→PDF genérica
- `scripts/validate.py` — validador de integração
- `scripts/hooks/pre-commit` — gate de segredos + suíte verde
- `scripts/padroes/` — templates de skill, script, comando e MCP

O que NÃO entrou (❌ específico, escrever do zero): skills de domínio, comandos
de criação, gates de mérito, templates de saída, registro de tipos, MCPs de
domínio, estrutura de `output/`.

### Fase 2: Customizar o universal (1 hora)

**2a. `CLAUDE.md`** — a fonte é `.claude/CLAUDE.md`; o da raiz é espelho gerado.

- Trocar `<SEU-PROJETO>` pelo nome do projeto
- Preencher os blocos marcados `[CUSTOMIZAR]`: Seção 1 (tipos), 2 (squad),
  3 (MCPs), 4 (templates), 5 (fluxo)
- **MANTER intactas:** Seção 0 (Economia), R1–R17, Seção 6 (Portabilidade)
- Rodar `python scripts/validate.py` — ele avisa enquanto sobrar placeholder

**2b. `.mcp.json`** — criar a partir de `scripts/padroes/mcp-template.js`

**2c. Re-rodar `setup-links`** para propagar os espelhos após editar o CLAUDE.md

### Fase 3: Escrever o específico (4–8 horas)

**Skills de domínio** — a partir de `scripts/padroes/skill-template.md`:
mantém frontmatter, regras herdadas e a forma Passo 1/2/3; a lógica é 100% sua.

**Comandos** — a partir de `scripts/padroes/command-template.md`: mantém a
tabela de requisitos contratuais, as fases e o checklist final.

**Gates de validação** — a partir de `scripts/padroes/script-template.py`:
mantém `console_utf8()`, relatório JSON gravado no `finally` e `exit 0/1`.
Regra: se a qualidade pode virar script, ela vira script (R9).

**Registro de tipos** — `scripts/tipos.py`, um dicionário. Adicionar um tipo
novo custa 1 entrada, nunca a edição de N pontos de dispatch (R12):

```python
TIPOS = {
    "seu-tipo-1": {
        "rotulo": "Seu Tipo 1",
        "raiz_output": "seu-tipo-1s",
        "natureza": "geracao",   # ou compressao, extracao
        "custo_llm": "medio",    # ou alto, baixo, zero
        "gates": ["validar-seu-criterio"],
    },
}
```

**Templates de saída** — `templates/` (vazio no repositório universal por
design: molde de saída é 100% específico).

**Estado** — schema próprio (SQLite/JSON), mantendo o padrão de persistência
em disco (R11).

### Fase 4: Validar (15 minutos)

```bash
python scripts/validate.py --estrito
bash fabrica-universal/tests/test-integration.sh .
bash fabrica-universal/tests/test-junctions.sh .
```

### Atualizar o universal depois

```bash
git submodule update --remote fabrica-universal
cp -r fabrica-universal/.claude/skills .claude/      # skills: sobrescrever
# .claude/CLAUDE.md: NÃO sobrescrever — ele está customizado.
# Fazer merge manual contra a versão nova:
cp fabrica-universal/.claude/CLAUDE.md .claude/CLAUDE.md.upstream
git add fabrica-universal && git commit -m "chore(submodule): atualizar fabrica-universal"
```

## TEMPOS ESTIMADOS (REALISTA)

Fase 1 (Consumir o universal): **15 minutos**
- `git submodule add` + copiar `.claude/` e `scripts/`: 5 min
- `setup-links` + `validate.py`: 5 min
- Commit: 5 min

Fase 2 (Customizar o universal): **1 hora**
- `CLAUDE.md` (placeholders + blocos `[CUSTOMIZAR]`): 30 min
- `.mcp.json`: 10 min
- Re-rodar `setup-links` + commit: 20 min

Fase 3 (Escrever o específico): **4–8 horas**
- Skills de domínio (3–5): 1–2h
- Comandos (2–5): 1–2h
- Gates de validação (3–6): 1–2h
- Templates de saída: 30 min
- Registro de tipos (`scripts/tipos.py`): 30 min
- Schema de estado: 30 min

Fase 4 (Validar): **15 minutos**
- `validate.py --estrito` + suíte de testes: 10 min
- Commit + push: 5 min

**TOTAL: 5.5–9.5 horas (vs. 4–6 semanas do zero)**

O ganho da abordagem submodule sobre a de clonar-e-deletar está quase todo na
Fase 1: 2.5 horas removendo o que não serve viram 15 minutos adicionando o que
serve. E, diferente do clone, a Fase 1 continua valendo depois — atualizar o
universal é `git submodule update --remote`, não um novo mergulho manual.

## CHECKLIST FINAL

**UNIVERSAL (vem do submodule, não reescrever):**
- [ ] `.claude/CLAUDE.md` Seções 0–7
- [ ] `.claude/RTK.md`
- [ ] 5 skills de economia
- [ ] `.claude/settings.json`
- [ ] `scripts/setup-links.ps1` / `.sh`
- [ ] `scripts/validate.py`
- [ ] `scripts/hooks/pre-commit`
- [ ] `scripts/padroes/` (skill, script, comando, MCP)

**ESPECÍFICO (escrever do zero):**
- [ ] Skills de domínio (3–5)
- [ ] Comandos (2–5)
- [ ] Gates de validação (3–6)
- [ ] Templates de saída (1–3)
- [ ] `scripts/tipos.py`
- [ ] Schema de estado
- [ ] Squad na Seção 2 do CLAUDE.md

**TESTAR:**
- [ ] `python scripts/validate.py --estrito`
- [ ] `bash fabrica-universal/tests/test-integration.sh .`
- [ ] `bash fabrica-universal/tests/test-junctions.sh .`
- [ ] Pre-commit bloqueia segredo e suíte vermelha
- [ ] Skills aparecem no `/help` do harness

## CONCLUSÃO

**Consumir ~40%:** infraestrutura, padrões, governança, economia (universal).
**Escrever ~60%:** skills, comandos, gates, templates, compilação (domínio).

A divisão não é sobre quantidade de código — é sobre **onde mora a verdade**.
O universal tem uma fonte só, versionada num lugar só, atualizável com um
comando. O específico é o que só o seu projeto sabe, e por isso não pode ser
herdado de ninguém.

Sem replicação: **4–6 semanas** (do zero).
Com submodule: **5.5–9.5 horas**.
