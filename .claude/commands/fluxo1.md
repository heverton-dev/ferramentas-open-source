---
description: Aciona o Fluxo 1 da Fábrica Universal (Mapeamento e Geração de Listas Horizontais por Camada Tecnológica)
---

Você foi acionado através do comando `/fluxo1`.

Siga este protocolo estrito:
1. Verifique se o usuário passou o argumento de camada ou tema livre (ex: `/fluxo1 bancos-dados-estado` ou `/fluxo1 experiencia do cliente, CX`).
2. Se nenhum argumento foi informado, pergunte ao usuário:
   *"Qual camada tecnológica ou tema open source você deseja mapear para a Lista Horizontal? (Exemplo: bancos-dados-estado, experiencia-usuario-cx, observabilidade-telemetria)"*
3. **Execução:**
   - Se for uma camada com JSON em `scripts/data/lista-<slug>.json`, execute:
     `python scripts/run_fluxo1.py --slug <slug>`
   - Se for um tema **novo**, ative a skill `fluxo1-listas-horizontais`: mapeie as 5 a 10 ferramentas de ponta da categoria com licença OSI, salve em `scripts/data/lista-<slug>.json` e execute `python scripts/compilar_lista_horizontal_tripartite.py --slug <slug>`.
4. Apresente os links dos artefatos gerados em `output/01-listas-horizontais/list-<slug>/` e pergunte se ele deseja avançar para o **Fluxo 2** com algum dos SaaS proprietários desmantelados.
