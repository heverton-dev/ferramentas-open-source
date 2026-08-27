# 11 · Dicionário Exaustivo de Scripts Python & Schemas JSON

> **Módulo:** Esteira Autônoma de Ingestão de Fontes, Manuais VPS e Trilhas de Aprendizado  
> **Linguagem:** Python 3.10+ & Typst 0.11+  
> **Status:** Produção Homologada · Nota 10.0 / 10.0

---

## 1. Mapeamento Geral dos Scripts do Módulo

O módulo é composto por **10 scripts Python especializados**, cada um cumprindo o princípio da responsabilidade única (*Single Responsibility Principle*):

```
scripts/
  ├── orquestrador_esteira_manuais.py ➔ Ponto de entrada unificado e controle do pipeline
  ├── coletar_fontes_pesquisa.py     ➔ Crawler leve em memória (zero download de vídeo/áudio)
  ├── compilar_sumario_fontes.py     ➔ Estruturador e indexador de trechos em JSON
  ├── auditar_qualidade_fontes.py    ➔ Gate G0: Whitelist, recência (>= 2024) e densidade
  ├── auditar_fontes_veridicas.py    ➔ Gate G1: Validação HTTP 200 ativa
  ├── gerar_manual_operacional.py    ➔ Compilador do Manual Duplo (HTML, MD e PDF Typst)
  ├── auditar_citacoes_manuais.py    ➔ Gate G2: Auditoria de citações biunívocas sem alucinação
  ├── gerar_trilha_aprendizado.py    ➔ Compilador da Trilha Brasil First (HTML, MD e PDF Typst)
  ├── gerar_relatorio_execucao.py    ➔ Gerador do Relatório de Telemetria (HTML, MD e PDF Typst)
  └── estado_esteira.py              ➔ Módulo de persistência relacional SQLite (Regra R11)
```

---

## 2. Fichas Técnicas dos Scripts

### 2.1. `orquestrador_esteira_manuais.py`
- **Função:** Orquestra a execução sequencial dos scripts, faz a ponte com o usuário e cronometra o tempo.
- **Entrada:** `--saas <nome>`, `--modo todas` ou `--ferramenta <slug>`.
- **Saída:** Pipeline completo executado com gravação no SQLite.

### 2.2. `coletar_fontes_pesquisa.py`
- **Função:** Coleta metadados de 4 categorias de fontes (Docs, Ebooks, YouTube, Cursos).
- **Regra R-Mídia:** Zero download pesado de mídia. Coleta puramente textual.
- **Saída:** `scripts/data/sumario-fontes-<slug>.json`.

### 2.3. `compilar_sumario_fontes.py`
- **Função:** Normaliza URLs, divide conteúdos por tópico pedagógico e atribui IDs determinísticos (`F01`, `F02`...).
- **Saída:** JSON estruturado pronto para validação.

### 2.4. `auditar_qualidade_fontes.py` (Gate G0)
- **Função:** Analisa o sumário sob os 4 pilares:
  1. Reputação de domínio (whitelist de autoridade);
  2. Recência tecnológica (rejeição de conteúdos obsoletos anteriores a 2024);
  3. Densidade técnica mínima;
  4. Integridade de metadados obrigatórios.
- **Retorno:** `exit 0` se aprovado; `exit 1` com relatório de inconsistências.

### 2.5. `auditar_fontes_veridicas.py` (Gate G1)
- **Função:** Executa requisições HTTP HEAD/GET reais para cada URL do sumário com header de User-Agent oficial.
- **Retorno:** `exit 0` se 100% das URLs retornarem status 200; `exit 1` se houver link quebrado.

### 2.6. `gerar_manual_operacional.py`
- **Função:** Monta o Manual Técnico Duplo estruturado com Módulo 0 (analogias), passos rígidos de VPS, Roteiro de Primeiro Voo e tabela de comandos.
- **Saída:** 3 arquivos em `output/<slug>/manuais/` e espelho em `docs/<slug>/manuais/`.

### 2.7. `auditar_citacoes_manuais.py` (Gate G2)
- **Função:** Cruza os IDs do sumário com as citações no manual.
- **Validação:** Exige correspondência biunívoca exata. Não tolera fontes órfãs nem citações alucinadas.
- **Retorno:** `exit 0` ou `exit 1`.

### 2.8. `gerar_trilha_aprendizado.py`
- **Função:** Monta a jornada cronológica de aprendizado com prioridade Brasil First e instruções de tradução assistida.
- **Saída:** 3 arquivos em `output/<slug>/trilhas/` e espelho em `docs/<slug>/trilhas/`.

### 2.9. `gerar_relatorio_execucao.py`
- **Função:** Consolida a telemetria do fluxo (horários, tokens, LLM, tools, skills, gates) e gera o relatório oficial de fechamento.
- **Saída:** 3 arquivos em `output/<slug>/relatorios/` e espelho em `docs/<slug>/relatorios/`.

### 2.10. `estado_esteira.py`
- **Função:** Gerencia a persistência relacional SQLite no banco `estado_esteira.db`, implementando as operações DDL e DML para a tabela `esteira_manuais_bundles`.

---

## 3. Schemas JSON Formais (`scripts/schemas/`)

| Arquivo de Schema | Propósito | Entidade Validada |
| :--- | :--- | :--- |
| `schema_manual_operacional.json` | Contrato do Manual Técnico Duplo | `scripts/data/manual-<slug>.json` |
| `schema_trilha_aprendizado.json` | Contrato da Trilha de Aprendizado | `scripts/data/trilha-<slug>.json` |
| `schema_relatorio_execucao.json` | Contrato da Telemetria de Execução | Dados passados a `gerar_relatorio_execucao` |
