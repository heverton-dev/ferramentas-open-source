# 09 · Comandos & Invocação (Fluxo 5: Auditorias VPS)

---

## 1. Comando Principal

### Via Claude Code (Skill)
```bash
/fluxo5 [slug] --portainer-url <url> --token <token>
```

### Via Python (CLI direto)
```bash
python scripts/run_fluxo5.py \
  --slug <slug> \
  --portainer-url <url> \
  --token <token> \
  [--verbose] [--force] [--profundo] [--sem-gates]
```

---

## 2. Opções de Linha de Comando

| Flag | Tipo | Descrição |
|------|------|-----------|
| `--slug <slug>` | string (obrigatório) | Slug do stack (ex: stack-ia) |
| `--portainer-url <url>` | string | URL de Portainer (ex: https://portainer.local) |
| `--token <token>` | string | Token Portainer (ler de .env recomendado) |
| `--verbose` | bool | Output detalhado |
| `--force` | bool | Ignora cache; recompila |
| `--profundo` | bool | Ativa subagentes (pesquisa de CVEs) |
| `--sem-gates` | bool | Desativa validação de gates (debug only) |

---

## 3. Exemplos

### Auditoria Básica
```bash
python scripts/run_fluxo5.py --slug stack-ia --portainer-url https://portainer.local --token ptr_xxxxx
```

### Com Subagentes (Profundo)
```bash
python scripts/run_fluxo5.py --slug stack-ia --portainer-url https://portainer.local --token ptr_xxxxx --profundo --verbose
```

### Via .env
```bash
# .env
PORTAINER_URL=https://portainer.local
PORTAINER_TOKEN=${PORTAINER_TOKEN}

python scripts/run_fluxo5.py --slug stack-ia
```

---

## 4. Exit Codes

| Código | Significado |
|--------|------------|
| 0 | Sucesso |
| 1 | Erro de validação |
| 2 | Erro de auditoria (Portainer) |
| 3 | Erro de compilação |
| 4 | Erro de gates |

