---
description: Aciona o Fluxo 3 da Fábrica Universal (Manual Operacional VPS com Desinstalação Cirúrgica & Trilha de Aprendizado)
---

Você foi acionado através do comando `/fluxo3`.

Siga este protocolo estrito:
1. Verifique se o usuário passou a ferramenta e o SaaS (ex: `/fluxo3 screenpipe granola`).
2. Se nenhum argumento foi informado, pergunte ao usuário:
   *"Qual ferramenta open source você deseja colocar em produção na VPS? (Exemplo: screenpipe, whisperx, open-notebooklm, whisper-cpp, faster-whisper-cli)"*
3. Com a ferramenta definida, execute o runner determinístico no terminal:
   `python scripts/run_fluxo3.py --ferramenta <ferramenta> --saas <saas>`
4. Apresente os links dos artefatos gerados em `output/03-manuais-e-trilhas/<saas>/<ferramenta>/`, destacando a **Seção de Desinstalação Cirúrgica** e a **Trilha de 5 Aulas**.
