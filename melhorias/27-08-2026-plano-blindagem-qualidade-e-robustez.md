# 📋 PLANO DE AÇÃO: BLINDAGEM DE QUALIDADE & ROBUSTEZ DA ESTEIRA AIDD

> **Fábrica Universal · Arsenal Open Source**  
> **Data:** 27/08/2026 | **Governança:** Padrão Diamante R5, R5-V e Regras R1 a R19  
> **Objetivo:** Blindar a execução dos 3 Macro-Fluxos para qualquer LLM/Harness, garantindo rigor técnico máximo sem travamentos de ambiente e auto-atualizando o Índice Mestre.

---

## 🎯 OBJETIVOS ESTRATÉGICOS

1. **Garantia de Qualidade Máxima (Sem Baixar a Régua):** Impedir que qualquer modelo gere documentação incompleta ou rasa, forçando a conformidade com os schemas canônicos.
2. **Feedback Guiado Pré-Compilação (Fail-Fast):** Substituir erros crípticos de Python (`KeyError`, `AttributeError`) por relatórios claros de campos faltantes.
3. **Imunidade a Problemas de Codificação no Windows:** Sanitização universal de caracteres invisíveis (UTF-8 BOM `\ufeff`).
4. **Auto-Atualização do Portal Mestre:** Sincronização automática do SQLite (`estado_esteira.db`) e do `INDICE-MESTRE.html` ao final de qualquer fluxo.

---

## 🗺️ FASES DE IMPLEMENTAÇÃO

### 📌 FASE 1: Linter & Validador de Qualidade Pré-Execução (Regra R9)
- Criar `scripts/validar_schemas_fluxos.py` baseado na biblioteca `jsonschema`.
- Validar os dados antes da renderização dos templates nos 3 fluxos.
- Mensagens de erro explicativas em PT-BR orientando a LLM sobre o que preencher com qualidade técnica.

### 📌 FASE 2: Sanitização Universal de Encoding & Windows (Regra R14 & R18)
- Padronizar todas as leituras de JSON nos compiladores com `encoding="utf-8-sig"`.
- Sanitizar strings e argumentos de CLI, removendo espaços e caracteres invisíveis de BOM.

### 📌 FASE 3: Auto-Sincronização do Índice Mestre nos Runners (Regra R11)
- Integrar a ingestão do SQLite e a compilação do `INDICE-MESTRE.html` ao final de cada execução bem-sucedida de `run_fluxo1.py`, `run_fluxo2.py` e `run_fluxo3.py`.

### 📌 FASE 4: Testes de Regressão & Validação Pytest (Regra R16)
- Adicionar novos testes unitários para validação de schemas, detecção de incompletudes e sanitização de encoding.
- Executar `pytest -v` garantindo 100% dos testes verdes e commit no Git.
