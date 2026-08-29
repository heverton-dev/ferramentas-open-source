---
description: Aciona o Fluxo 5 da Fábrica Universal (Auditoria, Incorporação e Desinstalação Cirúrgica em VPS Multi-Alvo)
---

Você foi acionado através do comando `/fluxo5`.

Siga este protocolo estrito:
1. Verifique se o usuário passou o alvo (ex: `/fluxo5 ecos-google-workspace` ou `/fluxo5 stalwart`).
2. Se nenhum argumento foi informado, pergunte ao usuário:
   *"Qual ecossistema ou ferramenta você deseja auditar na VPS? (Exemplo: ecos-google-workspace, stalwart, nextcloud)"*
3. Com o alvo definido, execute o runner determinístico no terminal:
   - Para ecossistema único: `python scripts/run_fluxo5.py --ecossistema <slug>`
   - Para ferramenta única: `python scripts/run_fluxo5.py --ferramenta <slug>`
   - Para múltiplos alvos: `python scripts/run_fluxo5.py --ecossistemas <slug1>,<slug2>`
   - Para varredura total: `python scripts/run_fluxo5.py --todos`
4. Apresente os links dos artefatos gerados em `output/05-auditorias-vps/`, destacando o veredito de viabilidade, o score de headroom e os manuais de instalação/desinstalação cirúrgica.
