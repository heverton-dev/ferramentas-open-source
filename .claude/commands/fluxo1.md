---
description: Aciona o Fluxo 1 da Fábrica Universal (Mapeamento de Listas Horizontais por Camada Tecnológica)
---

Você foi acionado através do comando `/fluxo1`.

Siga este protocolo estrito:
1. Verifique se o usuário passou o argumento de camada (ex: `/fluxo1 bancos-dados-estado`).
2. Se nenhum argumento foi informado, pergunte ao usuário:
   *"Qual das 49 camadas tecnológicas você deseja mapear para a Lista Horizontal? (Exemplo: bancos-dados-estado, observabilidade-telemetria, ia-llm-local)"*
3. Com o slug definido, execute o runner determinístico no terminal:
   `python scripts/run_fluxo1.py --slug <slug>`
4. Apresente os links dos artefatos gerados em `output/01-listas-horizontais/list-<slug>/` e pergunte se ele deseja avançar para o **Fluxo 2** com algum dos SaaS proprietários mapeados.
