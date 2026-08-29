# 03 · Arquitetura do Sistema (Fluxo 5: Auditorias VPS)

> **Módulo:** Fluxo 5 — Auditoria & Incorporação Cirúrgica em VPS

---

## 1. Estrutura de Componentes Internos

```
┌──────────────────────────────────────────────────────────┐
│         scripts/run_fluxo5.py (Orquestrador)             │
│  --slug <slug> --portainer-url <url> --token <token>     │
└──────────────────────────────────────────────────────────┘
         ↓
    ┌────────────┬─────────────┬────────────┬───────────┐
    │            │             │            │           │
    ↓            ↓             ↓            ↓           ↓
┌─────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌────────────┐
│Stage 1: │ │Stage 2:  │ │Stage 3:  │ │Stage 3+: │ │Stage 4:    │
│Auditoria│ │Análise   │ │Síntese   │ │Subagents │ │Validação   │
│         │ │Viabilid. │ │Stacks    │ │(opção)   │ │(Gates)     │
└─────────┘ └──────────┘ └──────────┘ └──────────┘ └────────────┘
│           │            │            │            │
│ Portainer │ Headroom   │ Docker     │ Pesquisa   │ Gate 1-4
│ API       │ Calculator │ Compose    │ CVEs       │
│ Connector │            │ Generator  │            │
│           │            │ PDF Typst  │            │
│           │            │ Compiler   │            │
└───────────┴────────────┴────────────┴────────────┴──────────┐
                                                               ↓
                         output/05-auditorias-vps/<slug>/
                         + SQLite (R11)
                         + Relatório (R3)
```

---

## 2. Módulos Executivos Internos

### 2.1. `PortainerConnector`
Conecta e autentica com Portainer API:
- Valida URL e token;
- Coleta stats em tempo real (CPU, RAM, Disco);
- Mapeia containers, volumes, networks;
- Trata timeout e erros de conexão.

### 2.2. `InfrastructureAuditor`
Auditoria do estado atual:
- Snapshot de componentes (versão, tags, imagens);
- Análise de segurança (Trivy scan para CVEs);
- Mapeamento de portas em uso;
- Consumo de recursos por container.

### 2.3. `HeadroomCalculator`
Calcula viabilidade matemática:
- CPU disponível: (total_cores - used_cores) / total_cores;
- RAM disponível: (total_gb - used_gb) / total_gb;
- Disco disponível: (total_gb - used_gb) / total_gb;
- Compatibilidade de versão (Docker, Kernel, SO);
- Matriz de conflito (portas, DNS).

### 2.4. `DockerComposeGenerator`
Gera stacks Docker prontos:
- Normalização de imagens e versões;
- Traefik labels para roteamento automático;
- Secret management (credenciais em .env);
- Health checks e restart policies;
- Volume mounts com backup automático.

### 2.5. `InstallationPlaybookGenerator`
Cria manuais de instalação cirúrgica:
- Pre-checks (validar pré-requisitos);
- Deploy faseado (dev → staging → prod);
- Rollback automático se falhar;
- Validação pós-instalação (smoke tests);
- Logs detalhados para auditoria.

### 2.6. `UninstallationPlaybookGenerator`
Cria manuais de desinstalação segura:
- Parada graciosa de serviços;
- Backup de dados antes de deletar;
- Limpeza de volumes, networks, secrets;
- Rollback de configurações (SSL, DNS);
- Auditoria de rastros residuais.

### 2.7. `ReportCompiler`
Compila documentação tripartite:
- HTML R5-VPS com hero stats de infraestrutura;
- Markdown 7 arquivos desmembrados;
- PDF via Typst (determinístico).

### 2.8. `SQLitePersister`
Grava estado em R11:
- Tabela `esteira_auditorias_vps`;
- Snapshot Portainer serializado;
- Status de cada stage e gates.

---

## 3. Fluxo de Dados Entre Módulos

```
Portainer API
     ↓ (JSON stats)
PortainerConnector
     ↓ (normalized data)
InfrastructureAuditor
     ↓ (vuln scan + mapping)
     ├─→ HeadroomCalculator ──→ Matriz Viabilidade
     ├─→ DockerComposeGenerator ──→ YAML Stacks
     ├─→ InstallationPlaybookGenerator ──→ Manual Install
     ├─→ UninstallationPlaybookGenerator ──→ Manual Uninstall
     └─→ ReportCompiler ──→ HTML/MD/PDF
          ↓
     SQLitePersister
          ↓
    output/ + gates
```

---

## 4. Contrato de Interface

### Entrada (stdin / arquivo / .env)
```yaml
PORTAINER_URL: https://portainer.empresa.com.br
PORTAINER_TOKEN: ${PORTAINER_TOKEN}
PORTAINER_ENDPOINT_ID: 2

slug: stack-ia-corporativa
componentes:
  - nome: Ollama
    versao: 0.3.0
    requisitos: {cpu: 8, ram: 32, disco: 500}
```

### Saída
```
✓ output/05-auditorias-vps/stack-ia-corporativa/
  ├─ relatorio-auditoria-*.{html,md,pdf}
  ├─ docker-compose-prod.yml
  ├─ docker-compose-staging.yml
  ├─ manual-instalacao-*.html
  ├─ manual-desinstalacao-*.html
  └─ rollback-playbook-*.sh
```

---

## 5. Dependências Externas

- Python 3.11+ (requests, pyyaml, dataclasses);
- Portainer Enterprise 2.20+ (API /auth/authenticate);
- Docker API 20.0+ (read-only stats);
- Trivy (vulnerability scanning);
- Typst (compilação PDF);
- Jinja2 (templating).

