# 01 · Blueprint Arquitetural (Fluxo 5: Auditorias VPS)

> **Módulo:** Fluxo 5 — Auditoria & Incorporação Cirúrgica em VPS

---

## 1. Arquitetura de 5 Stages

```
┌─────────────────────────────────────────────────────────────┐
│  INPUT: --slug <slug> --portainer-url <url> --token <token> │
└─────────────────────────────────────────────────────────────┘
         ↓
┌─────────────────────────────────────────────────────────────┐
│  Stage 1: Auditoria de Estado Atual (Portainer API)         │
│  · Conectar a Portainer                                      │
│  · Coletar métricas de CPU, RAM, Disco                      │
│  · Mapear containers, volumes, networks                      │
│  · Verificar vulnerabilidades (Trivy)                        │
└─────────────────────────────────────────────────────────────┘
         ↓
┌─────────────────────────────────────────────────────────────┐
│  Stage 2: Análise de Viabilidade Matemática                 │
│  · Calcular headroom (CPU, RAM, Disco disponível)           │
│  · Detectar conflitos de porta/DNS                          │
│  · Validar compatibilidade versão (Docker, Kernel, SO)      │
│  · Gerar matriz de risco (SPoF, CVEs, compatibilidade)      │
└─────────────────────────────────────────────────────────────┘
         ↓
┌─────────────────────────────────────────────────────────────┐
│  Stage 3: Síntese de Stacks & Documentação                  │
│  · Gerar docker-compose-prod.yml                            │
│  · Gerar docker-compose-staging.yml                         │
│  · Criar manual de instalação cirúrgica                      │
│  · Criar manual de desinstalação segura                      │
│  · Compilar relatório tripartite (HTML, MD, PDF)            │
└─────────────────────────────────────────────────────────────┘
         ↓
┌─────────────────────────────────────────────────────────────┐
│  Stage 4: Validação & Gates                                 │
│  · Gate 1: Integridade de arquivos                          │
│  · Gate 2: YAML/JSON validade (docker-compose, .env)        │
│  · Gate 3: Ausência de segredos                             │
│  · Gate 4: Conformidade com R5-VPS                          │
└─────────────────────────────────────────────────────────────┘
         ↓
OUTPUT: Bundle completo em output/05-auditorias-vps/<slug>/
        + Relatório de Auditoria
        + Stacks Docker prontos
        + Manuais de instalação/desinstalação
        + Registro SQLite (R11)
```

---

## 2. Fluxo de Auditoria (Portainer API)

```
┌──────────────────────────────┐
│  Portainer Enterprise         │
│  (Docker Swarm ou Standalone) │
└──────────────────────────────┘
         ↓ (API)
┌────────────────────────────────────────────┐
│  Endpoint: /api/endpoints/{id}/stats       │
│  Resposta: {cpu_usage, memory_usage, ...}  │
└────────────────────────────────────────────┘
         ↓
┌────────────────────────────────────────────┐
│  Endpoint: /api/containers                 │
│  Resposta: [{id, name, image, ...}, ...]   │
└────────────────────────────────────────────┘
         ↓
┌────────────────────────────────────────────┐
│  Endpoint: /api/volumes                    │
│  Resposta: [{name, mount_point, ...}, ...] │
└────────────────────────────────────────────┘
         ↓
┌──────────────────────────────┐
│  Auditor VPS (Python)         │
│  Calcula: headroom, risco     │
│  Gera: recomendações          │
└──────────────────────────────┘
```

---

## 3. Matriz de Análise de Viabilidade

| Fator | Fórmula | Exemplo | Status |
|-------|---------|---------|--------|
| **CPU Headroom** | (total_cores - used_cores) / total_cores | (32 - 18) / 32 = 43% | OK |
| **RAM Headroom** | (total_gb - used_gb) / total_gb | (256 - 140) / 256 = 45% | OK |
| **Disco Headroom** | (total_gb - used_gb) / total_gb | (2000 - 1200) / 2000 = 40% | OK |
| **Porta Disponível** | port ∉ [used_ports] | 8000 não está em uso | OK |
| **Versão Docker** | docker_version >= min_version | 24.0.6 >= 20.0 | OK |
| **Kernel Linux** | kernel_version >= min_kernel | 6.1.0 >= 5.15 | OK |
| **Viabilidade Geral** | AND(CPU, RAM, Disco, Porta, Docker, Kernel) | TRUE | VIÁVEL |

---

## 4. Estrutura de Relatório de Auditoria

```
┌─────────────────────────────────────────────────────┐
│  RELATÓRIO DE AUDITORIA EXECUTIVO                   │
├─────────────────────────────────────────────────────┤
│ 1. Snapshot Infraestrutura (Portainer em tempo real) │
│    • CPU Atual: 56% (18 cores / 32 cores)          │
│    • RAM Atual: 55% (140 GB / 256 GB)              │
│    • Disco Atual: 60% (1.2 TB / 2 TB)              │
│    • Uptime: 237 dias                              │
│    • Containers: 23 running, 5 stopped             │
│                                                     │
│ 2. Compatibilidade & Viabilidade                   │
│    • Stack Solicitado: Ollama + LangChain          │
│    • Requisito: 8 cores, 32 GB RAM, 500 GB        │
│    • Headroom: CPU 43%, RAM 45%, Disco 40%         │
│    • Conclusão: VIÁVEL ✓                           │
│                                                     │
│ 3. Recomendações                                    │
│    • Upgrade SSD: 2TB → 4TB (100% segurança)       │
│    • Reduzir cache: Prometheus logging 40 GB/mês   │
│    • Usar dedicated GPU: RTX 4090 para LLMs        │
│                                                     │
│ 4. Timeline de Instalação                          │
│    • Pre-checks: 10 minutos                        │
│    • Deploy: 30 minutos                            │
│    • Validação: 15 minutos                         │
│    • Total: 55 minutos (downtime: 0 minutos)       │
│                                                     │
│ 5. Riscos Identificados                            │
│    • Conflito de Porta 8080 (Traefik usado)        │
│    • Versão Docker < 20.10 não suportada           │
│    • Mitigation: Ver seção 6                       │
│                                                     │
│ 6. Mitigações                                       │
│    • Usar porta 8081 para novo Traefik             │
│    • Upgrade Docker de 19.03 para 24.0             │
│    • Pré-backup de volumes antes de deploy         │
└─────────────────────────────────────────────────────┘
```

---

## 5. Idem potência (R10)

Reexecução com mesmo slug e acesso Portainer produz:
- Mesmo relatório (bytes idênticos)
- Mesmos docker-compose files (versão, ordem de serviços)
- Mesmas recomendações de instalação

