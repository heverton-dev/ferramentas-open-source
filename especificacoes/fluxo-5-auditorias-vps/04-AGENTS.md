# 04 · Agentes & Orquestração (Fluxo 5: Auditorias VPS)

> **Módulo:** Fluxo 5 — Auditoria & Incorporação Cirúrgica em VPS

---

## 1. Agentes Principais (Stages 1-4)

### Agente 1: `conector-portainer`
- **Responsabilidade:** Autenticar e conectar com Portainer API;
- **Entrada:** URL, Token, Endpoint ID;
- **Saída:** JSON de stats + containers + volumes;
- **Modelo:** inherit (determinístico).

### Agente 2: `auditor-infraestrutura`
- **Responsabilidade:** Analisar estado atual, scan de CVEs, mapeamento de portas;
- **Entrada:** JSON Portainer;
- **Saída:** Relatório de auditoria + vulnerabilidades;
- **Modelo:** inherit (determinístico).

### Agente 3: `calculador-headroom`
- **Responsabilidade:** Avaliar viabilidade matemática de instalação;
- **Entrada:** Estado atual + requisitos do stack;
- **Saída:** Matriz de viabilidade, recomendações;
- **Modelo:** inherit (determinístico).

### Agente 4: `gerador-docker-compose`
- **Responsabilidade:** Gerar stacks Docker prontos para deploy;
- **Entrada:** Arquitetura do stack + estado atual;
- **Saída:** docker-compose-prod.yml + staging.yml;
- **Modelo:** inherit (determinístico).

### Agente 5: `gerador-playbook-instalacao`
- **Responsabilidade:** Criar manual de instalação cirúrgica passo-a-passo;
- **Entrada:** Docker compose + matriz viabilidade;
- **Saída:** 9 arquivos (manual + scripts de validação);
- **Modelo:** inherit (determinístico).

### Agente 6: `gerador-playbook-desinstalacao`
- **Responsabilidade:** Criar manual de rollback e limpeza segura;
- **Entrada:** Estado atual + docker compose;
- **Saída:** Playbook de desinstalação cirúrgica;
- **Modelo:** inherit (determinístico).

### Agente 7: `compilador-relatorio`
- **Responsabilidade:** Compilar documentação tripartite;
- **Entrada:** Todos os artifacts anteriores;
- **Saída:** HTML R5-VPS, Markdown (7 arquivos), PDF Typst;
- **Modelo:** inherit (determinístico).

### Agente 8: `auditor-gates`
- **Responsabilidade:** Validação mecânica de gates;
- **Entrada:** Bundle completo;
- **Saída:** Relatório de validação + exit code;
- **Modelo:** inherit (determinístico, sem LLM).

---

## 2. Especificação de Subagentes (Varredura Opcional)

Se `--profundo` for passado:

### Subagente A: `pesquisador-vulnerabilidades`
- Busca de CVEs em bancos de dados (NVD, GHSA);
- Cria matriz de risco versão-a-versão;
- Recomenda patches.

### Subagente B: `simulador-instalacao`
- Mock de deploy (sem executar de verdade);
- Detecta conflitos potenciais;
- Estima tempo de downtime.

### Subagente C: `gerador-casos-uso`
- Busca deployments similares em produção;
- Lições aprendidas;
- Benchmarks de performance.

---

## 3. Orquestração & Pipeline

```python
def run_fluxo5(slug, portainer_url, portainer_token, profundo=False):
    # Stage 1: Auditoria
    portainer_data = conector_portainer(portainer_url, portainer_token)
    auditoria = auditor_infraestrutura(portainer_data)
    
    # Stage 2: Análise
    headroom = calculador_headroom(auditoria, slug)
    
    # Stage 3: Síntese
    docker_compose = gerador_docker_compose(auditoria, slug)
    playbook_install = gerador_playbook_instalacao(docker_compose, headroom)
    playbook_uninstall = gerador_playbook_desinstalacao(auditoria, docker_compose)
    relatorio = compilador_relatorio(auditoria, headroom, playbook_install)
    
    # Opcional: Profundo
    if profundo:
        vulns = pesquisador_vulnerabilidades(auditoria)
        simulacao = simulador_instalacao(docker_compose)
        casos_uso = gerador_casos_uso(slug)
        relatorio = enriquecer_relatorio(relatorio, vulns, simulacao, casos_uso)
    
    # Stage 4: Validação
    resultado_gates = auditor_gates(relatorio, docker_compose)
    
    # Persistência
    sqlitepersister(slug, auditoria, resultado_gates)
    
    return resultado_gates
```

---

## 4. Contrato de Comunicação Inter-Agentes

Todos trocam dados via **JSON Lines** (JSONL):
```json
{"stage": "auditoria", "status": "ok", "portainer_data": {...}}
{"stage": "headroom", "status": "ok", "viavel": true, "headroom_cpu": 43}
```

---

## 5. Tempo de Execução Esperado

| Stage | Agente | Tempo (s) |
|-------|--------|-----------|
| 1 | Conector Portainer | 3 |
| 1 | Auditor | 5 |
| 2 | Calculador | 2 |
| 3 | Docker Compose | 3 |
| 3 | Playbook Install | 5 |
| 3 | Playbook Uninstall | 3 |
| 3 | Compilador | 60 |
| 4 | Auditor Gates | 2 |
| **Total** | | **~85s** |

