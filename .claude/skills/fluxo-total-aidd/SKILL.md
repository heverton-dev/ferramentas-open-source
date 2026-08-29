---
name: fluxo-total-aidd
description: Especialista na orquestração encadeada e governança dos 5 Macro-Fluxos AIDD da Fábrica Universal. Conduz o pipeline ponta a ponta desde o mapeamento horizontal até a auditoria VPS, gerenciando os Gates de Decisão Humano-no-Loop.
alwaysApply: false
---

# Skill Especialista · Pipeline Total AIDD (Fluxos 1 → 2 → 3 → 4 → 5)

Esta skill é a **Orquestradora Mestre** da Fábrica Universal. Ela interliga os 5 fluxos sequencialmente, garantindo paradas deliberadas de decisão estratégica para o operador.

## Quando Usar
- Quando o usuário quiser executar o ciclo completo de substituição tecnológica de uma vez só;
- Quando o comando `/fluxo-total` ou `/esteira-completa` for acionado;
- Quando o usuário pedir: "faça o pipeline completo de X a Z".

## Arquitetura dos 5 Macro-Fluxos

```text
Fluxo 1 (Horizontal)     → Listas temáticas por camada tecnológica
Fluxo 2 (Vertical)       → Dossiês de desmantelamento SaaS & Quinteto Soberano
Fluxo 3 (Manuais VPS)    → Manuais operacionais & Trilhas de aprendizado
Fluxo 4 (Ecossistemas)   → Macro-ecossistemas & Suítes integradas
Fluxo 5 (Auditoria VPS)  → Auditoria em tempo real & incorporação cirúrgica
```

## Pipeline Core (Fluxos 1 → 2 → 3)

O pipeline core executa a jornada sequencial com 3 Gates de Interação:

```text
[Mapeamento Horizontal] ➔ Gate 1 (Escolha do SaaS) ➔ [Dossiê Vertical] ➔ Gate 2 (Escolha da Ferramenta) ➔ [Manual VPS & Trilha] ➔ Gate 3 (Aprovação Final)
```

1. **Etapa 1 · Disparo do Fluxo 1 (Horizontal):**
   - Solicita ou confirma a camada tecnológica alvo;
   - Compila a lista temática tripartite;
   - **Gate 1:** Pergunta ao usuário qual SaaS proprietário da lista será desmantelado no Fluxo 2.

2. **Etapa 2 · Disparo do Fluxo 2 (Vertical):**
   - Compila o Dossiê Vertical do SaaS escolhido;
   - Elege o Quinteto Soberano e analisa o ecossistema agêntico (MCPs);
   - **Gate 2:** Pergunta ao usuário qual das 5 ferramentas do Quinteto será levada para a VPS no Fluxo 3.

3. **Etapa 3 · Disparo do Fluxo 3 (Manuais & Trilhas VPS):**
   - Executa a auditoria de 5 fontes verificadas (G0, G1, G2);
   - Compila o Manual Operacional com Desinstalação Cirúrgica;
   - Compila a Trilha de Aprendizado de 5 Aulas;
   - **Gate 3:** Apresenta o relatório executivo consolidado e solicita autorização para deploy.

## Módulos Independentes (Fluxos 4 e 5)

Os Fluxos 4 e 5 são módulos acionáveis independentemente do pipeline core:

- **Fluxo 4 (Macro-Ecossistemas):** Acionado via `/fluxo4 [ecossistema]`. Gera dossiês de suítes integradas com pilares funcionais, SSO, barramento e playbook agêntico.
- **Fluxo 5 (Auditoria VPS):** Acionado via `/fluxo5 [alvo]`. Conecta à VPS via Portainer API, audita headroom e gera manuais de instalação/desinstalação cirúrgica.

**Continuação Acionável ao Final do Pipeline Core:** Em modo interativo, `run_fluxo_total.py` pergunta, logo após o Gate 3, se o operador deseja acionar o Fluxo 4 e/ou o Fluxo 5 imediatamente — sem precisar abrir um novo comando. Se confirmado, o próprio runner importa `executar_fluxo4()` (Fluxo 4) ou invoca `run_fluxo5.py` via subprocesso (Fluxo 5) com o slug informado. Em modo `--nao-interativo`, essa etapa é pulada e o runner apenas orienta o comando manual equivalente.

## Execução via CLI:
```bash
# Pipeline Core — Modo Interativo (Pede confirmação em cada Gate):
python scripts/run_fluxo_total.py

# Pipeline Core — Modo Rápido (Valores pré-definidos):
python scripts/run_fluxo_total.py --camada bancos-dados-estado --saas granola --ferramenta screenpipe --nao-interativo

# Fluxo 4 — Ecossistema único:
python scripts/run_fluxo4.py --ecossistema rd-station-suite

# Fluxo 5 — Auditoria VPS:
python scripts/run_fluxo5.py --ecossistema ecos-google-workspace
```
