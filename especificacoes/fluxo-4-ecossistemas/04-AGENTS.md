# 04 · Agentes & Orquestração (Fluxo 4: Macro-Ecossistemas)

> **Módulo:** Fluxo 4 — Macro-Ecossistemas e Suítes Integradas

---

## 1. Agentes Principais (Stages 1-4)

### Agente 1: `validador-ecossistema`
- **Responsabilidade:** Validar entrada JSON/YAML contra schema;
- **Entrada:** `--ecossistema <slug>` + arquivo de metadados;
- **Saída:** JSON normalizado + diagnósticos;
- **Modelo:** inherit (rápido, determinístico).

### Agente 2: `arquiteto-dependencias`
- **Responsabilidade:** Construir grafo de dependências, detectar SPoF;
- **Entrada:** JSON normalizado;
- **Saída:** Lista de edges, ordem topológica, avisos de conflito;
- **Modelo:** inherit (determinístico).

### Agente 3: `desenhista-arquitetura`
- **Responsabilidade:** Gerar diagramas, matrizes e visualizações;
- **Entrada:** Grafo de dependências;
- **Saída:** SVG Mermaid, tabelas ASCII, descrições textuais;
- **Modelo:** inherit (determinístico).

### Agente 4: `calculador-tco`
- **Responsabilidade:** Calcular custo de propriedade, ROI, comparativo;
- **Entrada:** Componentes + requisitos de hardware + preços;
- **Saída:** Tabelas TCO, gráficos de ROI, recomendações;
- **Modelo:** inherit (determinístico).

### Agente 5: `gerador-playbooks`
- **Responsabilidade:** Criar guias de deploy, operação e rollback;
- **Entrada:** Arquitetura + componentes;
- **Saída:** 9 playbooks (3 diretórios x 3 níveis de detalhamento);
- **Modelo:** inherit (determinístico).

### Agente 6: `compilador-documentacao`
- **Responsabilidade:** Gerar HTML R5-E, Markdown (7 arquivos) e PDF Typst;
- **Entrada:** Todos os artifacts da stages anteriores;
- **Saída:** Documentação tripartite completa;
- **Modelo:** inherit (determinístico).

### Agente 7: `auditor-gates`
- **Responsabilidade:** Validação mecânica de gates (arquivos, hashes, ausência de segredos);
- **Entrada:** Bundle completo em `output/04-ecossistemas/`;
- **Saída:** Relatório de validação + exit code (0 ou 1);
- **Modelo:** inherit (determinístico, sem LLM).

---

## 2. Especificação de Subagentes (Varredura Opcional)

Se `--profundo` for passado:

### Subagente A: `pesquisador-componentes`
- Coleta de metadados adicionais (GitHub stars, last commit, community size);
- Cria leaderboard de "maturidade" para cada componente.

### Subagente B: `auditor-seguranca`
- Varredura de CVEs conhecidos em cada componente;
- Relatório de vulnerabilidades críticas.

### Subagente C: `gerador-casosuso`
- Busca de deployments reais em produção;
- Entrevistas de lessons learned.

---

## 3. Orquestração & Pipeline

```python
# Pseudocode
def run_fluxo4(ecossistema_slug, profundo=False):
    # Validação
    data = validador_ecossistema(ecossistema_slug)
    
    # Síntese arquitetural
    grafo = arquiteto_dependencias(data)
    diagramas = desenhista_arquitetura(grafo)
    tco = calculador_tco(data)
    playbooks = gerador_playbooks(grafo)
    
    # Compilação
    docs = compilador_documentacao(
        data, grafo, diagramas, tco, playbooks
    )
    
    # Opcional: Pesquisa Profunda
    if profundo:
        metadata_extra = pesquisador_componentes(data)
        seguranca = auditor_seguranca(data)
        casosuso = gerador_casosuso(data)
        docs = enriquecer_documentacao(docs, metadata_extra, seguranca, casosuso)
    
    # Persistência & Gates
    sqlitepersister(data, docs)
    resultado_gates = auditor_gates(docs)
    
    return resultado_gates
```

---

## 4. Contrato de Comunicação Inter-Agentes

Todos os agentes trocam dados via **JSON Lines** (JSONL):
```json
{"stage": "validacao", "status": "ok", "erro": null, "dados": {...}}
{"stage": "arquitetura", "status": "ok", "grafo_edges": [...]}
```

---

## 5. Tempo de Execução Esperado

| Stage | Agente | Tempo (s) |
|-------|--------|-----------|
| 1 | Validador | 0.5 |
| 2 | Arquiteto | 2 |
| 2 | Desenhista | 3 |
| 2 | Calculador | 1.5 |
| 3 | Gerador Playbooks | 5 |
| 3 | Compilador | 45 |
| 4 | Auditor Gates | 2 |
| **Total** | | **~60s** |

