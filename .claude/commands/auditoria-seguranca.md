---
description: Ciclo de auditoria de seguranca com correcao e prova antes/depois
---

Execute a skill `auditoria-seguranca` sobre este projeto.

Argumento opcional: `$ARGUMENTS`

- vazio ou `completo` — ciclo inteiro: baseline, correcao via `/implementacao`,
  re-auditoria em subagente limpo e relatorio comparativo
- `baseline` — apenas o Estagio 1 (auditar e emitir relatorio)
- `comparar` — apenas os Estagios 3 e 4, reaproveitando `.auditoria/baseline.json`

Siga a skill integralmente. Nao promova candidato da varredura a achado sem abrir o
arquivo e confirmar a explorabilidade.
