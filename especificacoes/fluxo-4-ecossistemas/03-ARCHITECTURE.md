# 03 · Arquitetura do Sistema (Fluxo 4: Macro-Ecossistemas)

> **Módulo:** Fluxo 4 — Macro-Ecossistemas e Suítes Integradas

---

## 1. Estrutura de Componentes Internos

```
┌──────────────────────────────────────────────────────────────┐
│                   Fluxo 4: Macro-Ecossistemas                │
└──────────────────────────────────────────────────────────────┘
         ↓
┌──────────────────────────────────────────────────────────────┐
│          scripts/run_fluxo4.py (Orquestrador Principal)      │
│  Parâmetros: --ecossistema <slug> [--verbose] [--force]      │
└──────────────────────────────────────────────────────────────┘
         ↓
    ┌────────────────────────┬──────────────────────────┐
    │                        │                          │
    ↓                        ↓                          ↓
┌────────────────┐   ┌──────────────────┐    ┌──────────────┐
│ Stage 1:       │   │ Stage 2:         │    │ Stage 3:     │
│ Coleta &       │   │ Síntese & Desenho│    │ Compilação   │
│ Validação      │   │ Arquitetural     │    │ Determinística
└────────────────┘   └──────────────────┘    └──────────────┘
│ · Ingerir dados│   │ · Gerar diagramas│    │ · HTML R5-E  │
│ · Verificar    │   │ · Mapear fluxos  │    │ · Markdown 7 │
│   versões      │   │ · Identificar    │    │ · PDF Typst  │
│ · Detectar     │   │   SPoF           │    │ · Playbooks  │
│   conflitos    │   │ · Compilar TCO   │    │ · Relatório  │
└────────────────┘   └──────────────────┘    └──────────────┘
    ↓                    ↓                          ↓
    └────────────────────┴──────────────────────────┘
                         ↓
                ┌────────────────────────┐
                │ Stage 4: Validação     │
                │ (Gates Mecânicos)      │
                └────────────────────────┘
                         ↓
         ┌───────────────┬────────────────┐
         │               │                │
    ✓ Gate 1      ✓ Gate 2        ✓ Gate 3/4
    (Arquivos)    (Validação)     (Métricas)
         ↓               ↓                ↓
    output/04-ecossistemas/ecos-<slug>/
    (Bundle Completo)
    + SQLite (R11)
    + Relatório (R3)
```

---

## 2. Módulos Executivos Internos

### 2.1. `EcossistemaValidator`

Valida entrada JSON/YAML:
- Presença de campos obrigatórios (slug, nome, componentes);
- Integridade de URLs (HEAD request);
- Licenças OSI válidas;
- Versões semver corretas.

### 2.2. `DependencyGraph`

Constrói grafo de dependências:
- Nodes = componentes;
- Edges = integrações/dependências;
- Detecta ciclos e SPoF (Single Point of Failure);
- Ordena topologicamente para guia de instalação.

### 2.3. `ArchitectureGenerator`

Gera diagramas:
- SVG Mermaid da topologia;
- Matriz de compatibilidade (versões vs. SO);
- Tabela de APIs internas;
- Fluxo de dados entre componentes.

### 2.4. `TCOCalculator`

Calcula custo de propriedade:
- Overhead de infraestrutura (hardware, energia);
- Custo de licenses (propriedários equivalentes);
- Tempo de dev para migração e suporte;
- ROI em 12/24/36 meses.

### 2.5. `PlaybookGenerator`

Cria guias operacionais:
- Playbooks de deploy (Docker, K8s);
- Playbooks de operação (backup, scaling);
- Playbooks de rollback (desinstalação cirúrgica).

### 2.6. `DocumentCompiler`

Compila outputs:
- HTML R5-E (template + data);
- Markdown (7 arquivos desmembrados);
- PDF via Typst (determinístico).

### 2.7. `SQLitePersister`

Grava estado em R11:
- Tabela `esteira_ecossistemas`;
- Campos: slug, nome, componentes[], versoes[], status, timestamp.

---

## 3. Fluxo de Dados Entre Módulos

```
Input JSON/YAML
     ↓
EcossistemaValidator ✓
     ↓ (JSON limpo)
DependencyGraph (cria grafo)
     ↓ (edges + topologia)
┌────────┬──────────────┬──────────────┐
│        │              │              │
↓        ↓              ↓              ↓
Arch    TCO         Playbook      Relatório
Gen     Calc        Generator     (métricas)
│       │            │             │
└─┬─────┴────────────┴─────────────┘
  ↓
DocumentCompiler
  ├─→ HTML (hero + interatividade)
  ├─→ MD (7 arquivos)
  └─→ PDF (Typst)
  ↓
SQLitePersister
  ↓
output/ + Relatório
```

---

## 4. Contrato de Interface

### Entrada (stdin / arquivo)
```yaml
slug: stack-ia-corporativa
nome: Stack de IA Corporativa
componentes:
  - nome: LangChain
    versao: 0.2.0
    url: https://github.com/langchain-ai/langchain
    papel: Orquestrador de LLMs
    licenca: MIT
```

### Saída
```
✓ ecos-stack-ia-corporativa/
  ├─ livro-mestre-*.{html,md,pdf}
  ├─ 00-livro-mestre-compilado/
  ├─ 01-guias-executivos-e-viabilidade/
  ├─ 02-guias-de-engenharia-e-infraestrutura/
  ├─ 03-playbooks-de-instalacao-e-operacao/
  ├─ 04-playbooks-de-desinstalacao-e-governanca/
  └─ relatorio-execucao-*.html
```

---

## 5. Dependências Externas

- Python 3.11+ (typing, dataclasses, pathlib);
- Jinja2 (templating HTML/Markdown);
- Typst (compilação PDF);
- Mermaid CLI (diagramas SVG);
- SQLite3 (persistência R11).

