# 09 · Comandos & Invocação (Fluxo 4: Macro-Ecossistemas)

> **Módulo:** Fluxo 4 — Macro-Ecossistemas e Suítes Integradas

---

## 1. Comando Principal

### Via Claude Code (Skill)
```bash
/fluxo4 [ecossistema-slug]
```

### Via Python (CLI direto)
```bash
python scripts/run_fluxo4.py --ecossistema <slug> [--verbose] [--force] [--profundo]
```

---

## 2. Opções de Linha de Comando

| Flag | Tipo | Descrição |
|------|------|-----------|
| `--ecossistema <slug>` | string (obrigatório) | Slug do ecossistema (ex: `stack-ia-corporativa`) |
| `--verbose` | bool | Output detalhado; mostra cada stage |
| `--force` | bool | Ignora cache; recompila mesmo se já existe |
| `--profundo` | bool | Ativa subagentes (pesquisador, auditor de segurança, casos de uso) |
| `--sem-gates` | bool | Desativa gates (não recomendado); apenas para debug |
| `--apenas-gates` | bool | Roda apenas validação de gates em bundle existente |
| `--output-dir <path>` | string | Diretório de saída customizado (default: `output/04-ecossistemas/`) |
| `--modelo <modelo>` | string | Override de modelo LLM (default: inherit) |

---

## 3. Exemplos de Uso

### Básico: Gerar Ecossistema Stack IA
```bash
python scripts/run_fluxo4.py --ecossistema stack-ia-corporativa
```

### Com Verbose
```bash
python scripts/run_fluxo4.py --ecossistema stack-ia-corporativa --verbose
```

### Recompilar (ignora cache)
```bash
python scripts/run_fluxo4.py --ecossistema stack-ia-corporativa --force
```

### Modo Profundo (subagentes ativados)
```bash
python scripts/run_fluxo4.py --ecossistema stack-ia-corporativa --profundo
```

### Apenas Validar Gates
```bash
python scripts/run_fluxo4.py --ecossistema stack-ia-corporativa --apenas-gates
```

---

## 4. Saída Esperada

```
=== Fluxo 4: Macro-Ecossistemas ===
Ecossistema: stack-ia-corporativa

[Stage 1] Validação de Entrada
  ✓ JSON válido
  ✓ Componentes encontrados: 6
  ✓ Licenças validadas

[Stage 2] Síntese Arquitetural
  ✓ Grafo de dependências construído (15 edges)
  ✓ Nenhum ciclo detectado
  ✓ Diagramas gerados

[Stage 3] Compilação
  ✓ HTML R5-E gerado (45 KB)
  ✓ Markdown (7 arquivos, 12 KB)
  ✓ PDF Typst compilado (250 KB)
  ✓ Playbooks gerados (9 arquivos)
  
[Stage 4] Validação (Gates)
  ✓ Gate 1: Integridade (16 arquivos)
  ✓ Gate 2: Validação HTML/MD/PDF
  ✓ Gate 3: Ausência de segredos
  ✓ Gate 4: Profundidade (6200 linhas)

SUCESSO em 45 segundos
Saída: output/04-ecossistemas/ecos-stack-ia-corporativa/
SQLite: ✓ Registrado
```

---

## 5. Skill `/fluxo4`

Definição em `.claude/skills/fluxo4/SKILL.md`:

```markdown
# Skill: Fluxo 4 - Macro-Ecossistemas

Invoca orquestrador de suítes integradas open source.

**Argumentos:**
- `[ecossistema-slug]` — slug do ecossistema (ex: stack-ia-corporativa)
- `[--profundo]` — ativa subagentes (opcional)
- `[--force]` — recompila mesmo se exists (opcional)

**Exemplo:**
/fluxo4 stack-ia-corporativa --profundo
```

---

## 6. Integração com Pre-Commit Hook

No arquivo `.git/hooks/pre-commit`:

```bash
#!/bin/bash
# Validar specs de Fluxo 4 antes de commitar
if git diff --cached | grep -q "especificacoes/fluxo-4"; then
  echo "Validando especificações de Fluxo 4..."
  python -m pytest tests/test_fluxo4_specs.py -v || exit 1
fi
```

---

## 7. Exit Codes

| Código | Significado |
|--------|------------|
| 0 | Sucesso completo |
| 1 | Erro de validação (entrada) |
| 2 | Erro de compilação |
| 3 | Erro de gate |
| 4 | Erro de persistência SQLite |
| 5 | Erro não categorizado |

