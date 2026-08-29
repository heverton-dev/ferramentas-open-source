# 10 · Hooks & Gatilhos (Fluxo 4: Macro-Ecossistemas)

> **Módulo:** Fluxo 4 — Macro-Ecossistemas e Suítes Integradas

---

## 1. Pre-Commit Hook

Arquivo: `.git/hooks/pre-commit`

```bash
#!/bin/bash
set -e

# Detectar mudanças em especificações de Fluxo 4
if git diff --cached --name-only | grep -q "especificacoes/fluxo-4"; then
  echo "[Pre-Commit] Validando especificações de Fluxo 4..."
  
  # Rodar suite de testes
  python -m pytest tests/test_fluxo4_specs.py -v || exit 1
  
  # Validar nomes de arquivos
  if ! git diff --cached --name-only | grep -E "^especificacoes/fluxo-4/[0-9]{2}-[A-Z].*\.md$"; then
    echo "[Pre-Commit] AVISO: Nomes de arquivo de specs devem seguir padrão XX-NOME.md"
  fi
  
  echo "[Pre-Commit] ✓ Validações de Fluxo 4 OK"
fi

# Bloquear credenciais
if git diff --cached | grep -i -E "password|secret|api_key|token" | grep -v ".example"; then
  echo "[Pre-Commit] FALHA: Segredos detectados no commit"
  exit 1
fi

exit 0
```

---

## 2. Post-Checkout Hook

Arquivo: `.git/hooks/post-checkout`

```bash
#!/bin/bash
# Sincronizar specs de Fluxo 4 com agentes multi-IDE

if git diff HEAD~1 HEAD --name-only | grep -q "especificacoes/fluxo-4"; then
  echo "[Post-Checkout] Atualizando specs de Fluxo 4 em .claude/ e .agents/..."
  
  # Espelhar para .agents/fluxo-4/
  cp -r especificacoes/fluxo-4-ecossistemas/* .agents/fluxo-4/ 2>/dev/null || true
  
  # Espelhar para .claude/fluxo-4/
  cp -r especificacoes/fluxo-4-ecossistemas/* .claude/fluxo-4/ 2>/dev/null || true
  
  echo "[Post-Checkout] ✓ Sincronização completa"
fi

exit 0
```

---

## 3. Pre-Push Hook

Arquivo: `.git/hooks/pre-push`

```bash
#!/bin/bash
set -e

echo "[Pre-Push] Validando Fluxo 4 antes de push..."

# Rodar todos os gates
python scripts/run_fluxo4.py --apenas-gates --sem-verbose || {
  echo "[Pre-Push] FALHA: Gates não passaram"
  exit 1
}

# Verificar que SQLite foi atualizado
if ! git diff --cached --name-only | grep -q "estado_esteira.db"; then
  echo "[Pre-Push] AVISO: estado_esteira.db não foi commitado (esperado?)"
fi

echo "[Pre-Push] ✓ Pronto para push"
exit 0
```

---

## 4. Webhook: Execução Noturna (CI/CD)

Arquivo: `.github/workflows/fluxo4-noturno.yml`

```yaml
name: Fluxo 4 Noturno

on:
  schedule:
    - cron: '0 2 * * *'  # 02:00 UTC = 23:00 BRT

jobs:
  fluxo4-profundo:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      
      - name: Install Dependencies
        run: pip install -r requirements.txt
      
      - name: Run Fluxo 4 (Profundo)
        run: |
          python scripts/run_fluxo4.py \
            --ecossistema stack-ia-corporativa \
            --profundo \
            --verbose
      
      - name: Commit Changes
        run: |
          git config --local user.email "automation@example.com"
          git config --local user.name "Fluxo 4 Automation"
          git add -A
          git commit -m "chore(fluxo4): auditoria noturna" || true
          git push origin main
```

---

## 5. Gatilho Manual (CLI Interativo)

```bash
# Monitorar mudanças em tempo real
fswatch especificacoes/fluxo-4-ecossistemas/ | while read change; do
  echo "[FSWatch] Mudança detectada: $change"
  python scripts/run_fluxo4.py --ecossistema $(basename $change) --force
done
```

---

## 6. Webhook: Integração Slack

Arquivo: `scripts/notify_fluxo4_slack.py`

```python
import requests
import json
from datetime import datetime

def notify_slack(resultado):
    webhook_url = os.getenv("SLACK_WEBHOOK_FLUXO4")
    
    color = "good" if resultado["status"] == "ok" else "danger"
    
    payload = {
        "attachments": [{
            "color": color,
            "title": f"Fluxo 4: {resultado['slug']}",
            "text": f"Status: {resultado['status']}",
            "fields": [
                {"title": "Duração", "value": f"{resultado['duracao_segundos']}s"},
                {"title": "Tokens", "value": f"{resultado['tokens_gastos']}"},
                {"title": "Gate 1-4", "value": f"{resultado['gates']}"}
            ],
            "ts": int(datetime.now().timestamp())
        }]
    }
    
    requests.post(webhook_url, json=payload)
```

Integração no pós-execução:
```bash
python scripts/run_fluxo4.py --ecossistema stack-ia --profundo && \
python scripts/notify_fluxo4_slack.py
```

