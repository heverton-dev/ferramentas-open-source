# 10 · Hooks & Gatilhos (Fluxo 5: Auditorias VPS)

---

## 1. Pre-Commit Hook

```bash
#!/bin/bash
if git diff --cached --name-only | grep -q "especificacoes/fluxo-5"; then
  echo "[Pre-Commit] Validando especificações de Fluxo 5..."
  python -m pytest tests/test_fluxo5_specs.py -v || exit 1
  
  if git diff --cached | grep -i "PORTAINER_TOKEN" | grep -v ".example"; then
    echo "[Pre-Commit] FALHA: Segredo detectado"
    exit 1
  fi
fi
exit 0
```

---

## 2. Post-Checkout Hook

```bash
#!/bin/bash
if git diff HEAD~1 HEAD --name-only | grep -q "especificacoes/fluxo-5"; then
  echo "[Post-Checkout] Atualizando specs de Fluxo 5..."
  cp -r especificacoes/fluxo-5-auditorias-vps/* .claude/fluxo-5/ 2>/dev/null || true
  cp -r especificacoes/fluxo-5-auditorias-vps/* .agents/fluxo-5/ 2>/dev/null || true
fi
exit 0
```

---

## 3. Pre-Push Hook

```bash
#!/bin/bash
echo "[Pre-Push] Validando Fluxo 5..."
python scripts/run_fluxo5.py --apenas-gates || exit 1
echo "[Pre-Push] ✓ Pronto"
exit 0
```

---

## 4. CI/CD Workflow (GitHub Actions)

```yaml
name: Fluxo 5 Noturno

on:
  schedule:
    - cron: '0 3 * * *'

jobs:
  auditoria:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      
      - name: Auditoria VPS
        env:
          PORTAINER_URL: ${{ secrets.PORTAINER_URL }}
          PORTAINER_TOKEN: ${{ secrets.PORTAINER_TOKEN }}
        run: |
          python scripts/run_fluxo5.py \
            --slug prod-stack \
            --profundo \
            --verbose
      
      - name: Commit Relatórios
        run: |
          git config --local user.email "automation@example.com"
          git config --local user.name "Fluxo 5 Bot"
          git add -A
          git commit -m "chore(fluxo5): auditoria noturna" || true
          git push origin main
```

