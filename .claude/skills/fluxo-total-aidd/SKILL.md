---
name: fluxo-total-aidd
description: Especialista na orquestração encadeada e governança dos 3 Macro-Fluxos AIDD da Fábrica Universal. Conduz o pipeline ponta a ponta desde o mapeamento horizontal até o manual de VPS, gerenciando os 3 Gates de Decisão Humano-no-Loop.
alwaysApply: false
---

# Skill Especialista · Pipeline Total AIDD (Fluxos 1 + 2 + 3)

Esta skill é a **Orquestradora Mestre** da Fábrica Universal. Ela interliga os 3 fluxos sequencialmente, garantindo paradas deliberadas de decisão estratégica para o operador.

## Quando Usar
- Quando o usuário quiser executar o ciclo completo de substituição tecnológica de uma vez só;
- Quando o comando `/fluxo-total` ou `/esteira-completa` for acionado;
- Quando o usuário pedir: "faça o pipeline completo de X a Z".

## Protocolo dos 3 Gates de Interação Humano-no-Loop

```text
[Mapeamento Horizontal] ➔ 🛑 Gate 1 (Escolha do SaaS) ➔ [Dossiê Vertical] ➔ 🛑 Gate 2 (Escolha da Ferramenta) ➔ [Manual VPS & Trilha] ➔ 🛑 Gate 3 (Aprovação Final)
```

1. **Etapa 1 · Disparo do Fluxo 1 (Horizontal):**
   - Solicita ou confirma a camada tecnológica alvo;
   - Compila a lista temática tripartite;
   - **🛑 Gate 1:** Pergunta ao usuário qual SaaS proprietário da lista será desmantelado no Fluxo 2.

2. **Etapa 2 · Disparo do Fluxo 2 (Vertical):**
   - Compila o Dossiê Vertical do SaaS escolhido;
   - Elege o Quinteto Soberano e analisa o ecossistema agêntico (MCPs);
   - **🛑 Gate 2:** Pergunta ao usuário qual das 5 ferramentas do Quinteto será levada para a VPS no Fluxo 3.

3. **Etapa 3 · Disparo do Fluxo 3 (Manuais & Trilhas VPS):**
   - Executa a auditoria de 5 fontes verificadas (G0, G1, G2);
   - Compila o Manual Operacional com Desinstalação Cirúrgica;
   - Compila a Trilha de Aprendizado de 5 Aulas;
   - **🛑 Gate 3:** Apresenta o relatório executivo consolidado e solicita autorização para deploy direto via GitHub Actions.

## Execução via CLI:
```bash
# Modo Interativo (Pede confirmação em cada Gate):
python scripts/run_fluxo_total.py

# Modo Rápido (Valores padrão ou pré-definidos):
python scripts/run_fluxo_total.py --camada bancos-dados-estado --saas granola --ferramenta screenpipe --nao-interativo
```
