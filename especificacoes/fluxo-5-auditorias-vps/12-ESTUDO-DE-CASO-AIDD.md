# 12 · Estudo de Caso AIDD (Fluxo 5: Auditorias VPS)

> **Módulo:** Fluxo 5 — Auditoria & Incorporação Cirúrgica em VPS  
> **Caso:** Deploy Seguro de Ollama + LangChain em Produção

---

## 1. Cenário de Negócio

Uma fintech brasileira com VPS corporativa (2TB SSD, 256GB RAM, 32 cores) já rodando:
- PostgreSQL (financeiro + clientes)
- Redis (sessões)
- Prometheus (monitoramento)
- Traefik (API Gateway)
- 23 microserviços legados

**Objetivo:** Adicionar Ollama + LangChain para análise de documentos (KYC), **sem interromper** nenhum serviço existente.

---

## 2. Execução do Fluxo 5

### Comando Disparado
```bash
python scripts/run_fluxo5.py \
  --slug ollama-langchain \
  --portainer-url https://portainer.fintech.local \
  --token ptr_XXXXX \
  --profundo \
  --verbose
```

### Output Esperado
```
=== Fluxo 5: Auditoria & Incorporação Cirúrgica ===
Stack: ollama-langchain

[Stage 1] Auditoria de Estado Atual (Portainer)
  ✓ Conectado a Portainer (v2.20.1)
  ✓ Snapshot capturado: 32 cores, 256GB RAM, 2000GB SSD
  ✓ Consumo atual: CPU 56% (18 cores), RAM 55% (140 GB), Disco 60% (1.2 TB)
  ✓ Containers encontrados: 23 running, 5 stopped
  ✓ Portas em uso: 80, 443, 5432, 6379, 9090, [15 mais]

[Stage 2] Análise de Viabilidade Matemática
  ✓ Requisitos Ollama: 8 cores, 32GB RAM, 500GB disco
  ✓ Requisitos LangChain: 2 cores, 8GB RAM, 10GB disco
  ✓ Headroom Disponível:
    • CPU: 43% (14 cores livres) ✓ SUFICIENTE
    • RAM: 45% (116 GB livres) ✓ SUFICIENTE
    • Disco: 40% (800 GB livres) ✓ SUFICIENTE
  ✓ Conflitos de Porta: NENHUM (8000, 8001, 8002 livres)
  ✓ Compatibilidade Docker: 24.0.6 >= 20.0 ✓ OK
  ✓ Compatibilidade Kernel: 6.1.0 >= 5.15 ✓ OK
  ✓ Conclusão: VIÁVEL E SEGURO ✓

[Stage 3] Síntese de Stacks & Documentação
  ✓ docker-compose-prod.yml (Ollama + LangChain + Traefik)
  ✓ docker-compose-staging.yml (para testes)
  ✓ Manual de instalação cirúrgica (pré-checks, deploy, validação)
  ✓ Manual de desinstalação segura (rollback, limpeza)
  ✓ Compilação tripartite:
    • relatorio-auditoria-ollama-langchain.html (R5-VPS)
    • relatorio-auditoria-ollama-langchain.md (7 arquivos)
    • relatorio-auditoria-ollama-langchain.pdf (impresso)

[Stage 3+] Subagentes Profundos
  ✓ pesquisador-vulnerabilidades: CVE-2024-5678 MÉDIA em Ollama 0.2.9 (upgrade para 0.3.0)
  ✓ simulador-instalacao: Tempo estimado 15 minutos, downtime ZERO (Blue-Green)
  ✓ gerador-casos-uso: 2 casos reais (TechCorp, Fintech Inc) com lessons learned

[Stage 4] Validação (Gates)
  ✓ Gate 1: Integridade de Arquivos (16 arquivos)
  ✓ Gate 2: YAML/JSON válidos
  ✓ Gate 3: Ausência de PORTAINER_TOKEN ✓
  ✓ Gate 4: Conformidade R5-VPS (hero stats) ✓

=== RESULTADO FINAL ===
Status: OK
Tempo Total: 78 segundos
Tokens Gastos: 22,000 (LLM=1.5k, determinístico=20.5k)
Saída: output/05-auditorias-vps/ollama-langchain/

Entregáveis:
├── relatorio-auditoria-ollama-langchain.html
│   └── Hero Stats: CPU 43% headroom, RAM 45%, Disco 40%
│   └── Matriz de Viabilidade: VIÁVEL
│   └── Timeline: Instalação 15min, downtime 0min
├── docker-compose-prod.yml (production-ready)
├── docker-compose-staging.yml (para testes antes)
├── manual-instalacao-cirurgica-ollama-langchain.html
│   └── Pré-checks, deploy faseado, validação pós-deploy
├── manual-desinstalacao-cirurgica-ollama-langchain.html
│   └── Rollback automático, limpeza de estado
└── relatorio-execucao-ollama-langchain.html (telemetria)
```

---

## 3. Resultados Entregues ao Cliente

### 3.1 Para CTO (Infraestrutura)
- **Relatório HTML Executivo:** Headroom disponível, compatibilidade garantida, timeline zero-downtime
- **Docker Compose:** Production-ready, secrets em .env, health checks configurados
- **Playbook de Rollback:** Se falhar em qualquer ponto, script automático recupera estado anterior

### 3.2 Para DevOps/SRE
- **Manual Cirúrgico de Instalação:** 12 passos detalhados, pre-checks, validação
- **Manual de Desinstalação:** Limpeza segura de volumes, networks, segredos
- **Matriz de Compatibilidade:** Versões Docker, Kernel, SO vs. requisitos

### 3.3 Para Compliance/Auditoria
- **Snapshot Portainer Auditado:** JSON timestamp, aprovação formal antes de deploy
- **Rastreabilidade:** Cada passo registrado em logs (quem, quando, o quê)
- **Backup Pre-Deploy:** Volumes críticos (PostgreSQL) backed up antes de qualquer mudança

---

## 4. Impacto & Validação

### 4.1 Antes do Fluxo 5
- Informação fragmentada (planilhas, emails, wikis)
- Medo de quebrar produção (sem baseline do estado atual)
- Deploy manual = altíssimo risco de downtime

### 4.2 Depois do Fluxo 5
- **Auditoria científica:** Dados concretos (CPU, RAM, portas) vs. suposições
- **Decisão executiva rápida:** Viabilidade comprovada matematicamente
- **Deploy seguro:** Playbook cirúrgico validado, rollback automático se falhar
- **Conformidade:** Rastreabilidade completa para LGPD/SOC2

---

## 5. Aprendizados AIDD (AI-Driven Development)

### L1: Read-Only Auditoria = Segurança
Fluxo 5 conecta a Portainer apenas para **ler** estado. Nunca modifica nada (zero risco de acidente).

### L2: Headroom Matemático Elimina Adivinhação
Fórmulas simples de viabilidade (CPU avail %, RAM avail %, Disco avail %) transformam "acho que cabe" em "cabe com 43% de margem".

### L3: Playbooks Cirúrgicos são Antídotos contra Pánico
Um passo-a-passo detalhado com pre-checks + validação transforma deploy caótico em procedimento calmo e verificável.

### L4: Determinismo em Auditoria = Confiança Replicável
Reexecução do Fluxo 5 produz **exatamente** os mesmos artefatos. Isso permite auditoria forense, replay de decisões e compliance.

