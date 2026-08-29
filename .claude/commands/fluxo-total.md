---
description: Aciona a execução encadeada dos Macro-Fluxos AIDD com Gates de Decisão Humano-no-Loop
---

Você foi acionado através do comando `/fluxo-total`.

Siga este protocolo estrito:
1. Informe ao usuário que o Pipeline Total AIDD iniciará a jornada completa de substituição tecnológica.
2. Inicie a execução pelo CLI Runner integrado:
   `python scripts/run_fluxo_total.py`
3. Acompanhe os 3 Gates de Decisão do Pipeline Core:
   - **Gate 1:** Confirmação da Camada e escolha do SaaS;
   - **Gate 2:** Confirmação do Dossiê e escolha da Ferramenta;
   - **Gate 3:** Aprovação final dos Manuais e autorização para Deploy.
4. Após o Pipeline Core, o próprio `run_fluxo_total.py` pergunta interativamente se o operador deseja acionar agora o Fluxo 4 (Macro-Ecossistemas) e/ou o Fluxo 5 (Auditoria VPS) — sem precisar de um novo comando. Em modo `--nao-interativo`, apenas informe que ambos podem ser acionados depois via `/fluxo4` e `/fluxo5`.
5. Apresente o sumário executivo com todos os artefatos consolidados nas pastas mestras de `output/`.
