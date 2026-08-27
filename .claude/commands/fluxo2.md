---
description: Aciona o Fluxo 2 da Fábrica Universal (Dossiê Vertical de Desmantelamento SaaS & Quinteto Soberano)
---

Você foi acionado através do comando `/fluxo2`.

Siga este protocolo estrito:
1. Verifique se o usuário passou o SaaS alvo (ex: `/fluxo2 granola`).
2. Se nenhum argumento foi informado, pergunte ao usuário:
   *"Qual SaaS proprietário você deseja desmantelar no Dossiê Vertical? (Exemplo: granola, notion, zapier, salesforce)"*
3. Com o SaaS definido, execute o runner determinístico no terminal:
   `python scripts/run_fluxo2.py --saas <saas>`
4. Apresente os links dos artefatos gerados em `output/02-dossies-verticais/vert-<saas>/` e o resumo do Quinteto Soberano, perguntando se ele deseja avançar para o **Fluxo 3** para gerar o manual VPS de alguma ferramenta.
