# Script de Expurgo de Volumes e Higiene de Disco

## 1. Expurgo Seguro de Volumes
Execute via terminal SSH apenas se desejar apagar definitivamente todos os dados da stack e liberar espaço:
```bash
docker volume ls --filter name=ecos-crm-marketing_ -q | xargs -r docker volume rm
```
*(Nenhum volume de outras stacks será tocado).*
