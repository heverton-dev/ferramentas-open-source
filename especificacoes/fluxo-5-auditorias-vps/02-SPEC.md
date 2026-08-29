# 02 · Especificação Técnica (Fluxo 5: Auditorias VPS)

> **Módulo:** Fluxo 5 — Auditoria & Incorporação Cirúrgica em VPS

---

## 1. Requisitos Funcionais Obrigatórios

- **RF01 (Coleta via Portainer API):** Conectar a Portainer, autenticar com token, coletar stats em tempo real;
- **RF02 (Análise de Headroom):** Calcular espaço disponível (CPU, RAM, Disco) com fórmulas determinísticas;
- **RF03 (Detecção de Conflitos):** Mapear portas em uso, DNS entries, volumes existentes;
- **RF04 (Geração de Stacks):** Produzir docker-compose-prod.yml e staging.yml prontos para deploy;
- **RF05 (Compilação Tripartite):** HTML (R5-VPS), Markdown (7 arquivos), PDF Typst;
- **RF06 (Manuais Cirúrgicos):** Guias de instalação passo-a-passo e desinstalação segura;
- **RF07 (Persistência SQLite R11):** Gravar auditoria em `esteira_auditorias_vps` com timestamp e resultado;
- **RF08 (Rollback Automático):** Se falhar em qualquer stage, voltar ao estado anterior (snapshots).

---

## 2. Requisitos Não-Funcionais

- **RNF01 (Determinismo R8):** Auditoria de Portainer deve ser repetível; mesmos dados = mesmos outputs;
- **RNF02 (Segurança R15):** Zero credenciais Portainer no output; usar `.env.example` com validação;
- **RNF03 (Performance):** Auditoria completa em < 120 segundos (incluindo PDF);
- **RNF04 (Resiliência):** Se Portainer cair mid-auditoria, recuperar do estado anterior;
- **RNF05 (Conformidade):** Não interromper serviços em produção durante auditoria (read-only);
- **RNF06 (Documentação Não-Técnica):** Acessível para gestores sem formação DevOps (glossário integrado).

---

## 3. Estrutura de Dados de Entrada

```yaml
# Portainer Connection (.env)
PORTAINER_URL: https://portainer.empresa.com.br
PORTAINER_TOKEN: ${PORTAINER_TOKEN}
PORTAINER_ENDPOINT_ID: 2

# Target Stack Metadata
slug: stack-ia-corporativa
nome: Stack de IA Corporativa
componentes:
  - nome: Ollama
    versao: 0.3.0
    requisitos:
      cpu_cores: 8
      ram_gb: 32
      disco_gb: 500

# Opções de Deploy
modo_deploy: docker_swarm  # ou 'docker_standalone'
downtime_maximo_minutos: 60
backup_antes_deploy: true
validacao_pos_deploy: smoke_tests
```

---

## 4. Saídas Esperadas

```
output/05-auditorias-vps/<slug>/
├── relatorio-auditoria-<slug>.html       (R5-VPS com hero stats)
├── relatorio-auditoria-<slug>.md         (Markdown executivo)
├── relatorio-auditoria-<slug>.pdf        (PDF impresso)
├── snapshot-infraestrutura-<slug>.json   (Dados brutos Portainer)
├── docker-compose-prod.yml               (Production-ready)
├── docker-compose-staging.yml            (Para testes)
├── .env.example                          (Secrets template)
├── manual-instalacao-cirurgica-<slug>.html
├── manual-instalacao-cirurgica-<slug>.md
├── manual-desinstalacao-cirurgica-<slug>.html
├── rollback-playbook-<slug>.sh           (Script automático)
└── relatorio-execucao-<slug>.html        (Telemetria)
```

---

## 5. Protocolo de Validação (Gates)

| Gate | Critério | Ação em Falha |
|------|----------|---------------|
| Gate 1 | Arquivos gerados (≥ 12 arquivos) | Reexecutar compilação |
| Gate 2 | YAML válido (docker-compose), JSON (snapshot) | Validar schema |
| Gate 3 | Ausência de credenciais (PORTAINER_TOKEN) | Bloquear commit |
| Gate 4 | Conformidade R5-VPS (HTML, hero stats) | Avisar, não bloqueia |

---

## 6. Contato com Portainer API

```python
# Exemplo: Coleta de Stats
GET /api/endpoints/2/stats

{
  "cpu_usage": 56.2,
  "memory_usage": 140737.2,  # MB
  "memory_total": 262144.0,  # MB
  "disk_read": 1048576,      # KB
  "disk_write": 524288,      # KB
  "uptime": 20476400         # segundos
}
```

```python
# Exemplo: Listagem de Containers
GET /api/containers

[
  {
    "id": "abc123",
    "name": "prometheus",
    "image": "prometheus:latest",
    "status": "running",
    "ports": [{"private": 9090, "public": 9090}]
  }
]
```

