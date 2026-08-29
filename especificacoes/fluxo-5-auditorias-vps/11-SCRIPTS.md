# 11 · Scripts & Automação (Fluxo 5: Auditorias VPS)

---

## 1. Script Orquestrador Principal

Arquivo: `scripts/run_fluxo5.py`

```python
#!/usr/bin/env python3
"""
Orquestrador do Fluxo 5: Auditoria & Incorporação Cirúrgica em VPS
"""

import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="Fluxo 5: Auditorias VPS")
    parser.add_argument("--slug", required=True, help="Slug do stack")
    parser.add_argument("--portainer-url", help="URL Portainer (ou ler de .env)")
    parser.add_argument("--token", help="Token Portainer (ou ler de .env)")
    parser.add_argument("--verbose", action="store_true")
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--profundo", action="store_true")
    parser.add_argument("--sem-gates", action="store_true")
    
    args = parser.parse_args()
    
    # Setup
    portainer_url = args.portainer_url or os.getenv("PORTAINER_URL")
    portainer_token = args.token or os.getenv("PORTAINER_TOKEN")
    
    if not (portainer_url and portainer_token):
        logging.error("PORTAINER_URL e PORTAINER_TOKEN não configurados")
        sys.exit(1)
    
    # Pipeline
    try:
        logger.info(f"[Stage 1] Auditando: {args.slug}")
        portainer_data = conector_portainer(portainer_url, portainer_token)
        
        logger.info("[Stage 2] Analisando viabilidade...")
        headroom = calculador_headroom(portainer_data)
        
        logger.info("[Stage 3] Gerando documentação...")
        docker_compose = gerador_docker_compose(portainer_data, args.slug)
        relatorio = compilador_relatorio(portainer_data, headroom, docker_compose)
        
        if args.profundo:
            logger.info("[Stage 3+] Subagentes (profundo)...")
        
        if not args.sem_gates:
            logger.info("[Stage 4] Validando gates...")
            resultado_gates = auditor_gates(relatorio, docker_compose)
            if resultado_gates["status"] != "ok":
                sys.exit(4)
        
        sqlitepersister(args.slug, portainer_data, relatorio)
        
        logger.info(f"✓ SUCESSO: output/05-auditorias-vps/{args.slug}/")
        sys.exit(0)
    
    except Exception as e:
        logger.error(f"ERRO: {e}")
        sys.exit(2)

if __name__ == "__main__":
    main()
```

---

## 2. Scripts de Gates

### Gate 1: Integridade
```bash
#!/bin/bash
ARQUIVO_COUNT=$(find output/05-auditorias-vps/${SLUG}/ -type f | wc -l)
[ $ARQUIVO_COUNT -ge 12 ] && echo "Gate 1 OK" || exit 1
```

### Gate 2: Validação YAML
```bash
#!/bin/bash
yamllint output/05-auditorias-vps/${SLUG}/**/*.yml || exit 1
echo "Gate 2 OK"
```

### Gate 3: Segredos
```bash
#!/bin/bash
if grep -r "PORTAINER_TOKEN\|password\|secret" output/05-auditorias-vps/${SLUG}/ | grep -v ".example"; then
  echo "Gate 3 FALHA: Segredos detectados"
  exit 1
fi
echo "Gate 3 OK"
```

---

## 3. Script de Backup Portainer

```bash
#!/bin/bash
# Backup do snapshot Portainer antes de qualquer deploy

SLUG=$1
BACKUP_DIR="backups/portainer"
mkdir -p $BACKUP_DIR

curl -s -H "Authorization: Bearer $PORTAINER_TOKEN" \
  $PORTAINER_URL/api/endpoints/2 \
  > $BACKUP_DIR/snapshot_${SLUG}_$(date +%Y%m%d_%H%M%S).json

echo "✓ Snapshot salvo"
```

