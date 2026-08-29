# 00 · Manifesto, Propósito & Visão Geral do Módulo

> **Módulo:** Auditoria & Incorporação Cirúrgica em VPS via Portainer  
> **Metodologia:** AI-Driven Development (AIDD) · Engenharia Agêntica de Elite  
> **Status:** Produção Homologada · Nota 10.0 / 10.0  
> **Data:** 28 de Agosto de 2026

---

## 1. O Desafio da Integração Segura em Produção

O **Fluxo 5** aborda o cenário crítico em infraestrutura: **como implantar um software open source complexo em uma VPS já em operação, sem risco de downtime ou corromper aplicações existentes?**

Diferente de laboratórios ou ambientes verdes, VPS corporativas enfrentam:
1. **Estado Produtivo Desconhecido:** Quais serviços rodando? Quais portas já em uso? Qual é o espaço livre?
2. **Coexistência Perigosa:** Novo software pode conflitar com legado (portas, DNS, SSL, permissões);
3. **Desinstalação Cirúrgica:** Se falhar, rollback deve recuperar 100% do estado anterior sem perda de dados;
4. **Conformidade & Auditoria:** Registrar cada passo para compliance (LGPD, SOC2, ISO 27001).

---

## 2. A Missão do Módulo

Este módulo foi concebido como uma **Orquestração Segura de Infraestrutura**, capaz de:

- **Auditar estado atual da VPS** via Portainer API em tempo real:
  - Consumo de CPU, RAM, Disco
  - Containers/Serviços em execução
  - Volumes e networks Docker
  - Versão de Docker, Kernel, SO
  - Vulnerabilidades de imagem (Trivy)

- **Avaliar viabilidade matemática** de instalação:
  - Headroom disponível (CPU, RAM, Disco)
  - Conflitos de porta e DNS
  - Dependências de versão com componentes existentes

- **Gerar stacks Docker Swarm integrados** prontos para deploy:
  - Compose file normalizado com secrets management
  - Traefik labels para roteamento automático
  - Health checks, restart policies, logging configurado

- **Criar manuais de instalação cirúrgica** passo-a-passo:
  - Pre-checks (validação de pré-requisitos)
  - Deploy faseado (dev → staging → prod)
  - Rollback automático se falhar
  - Validação pós-instalação (smoke tests)

- **Documentar desinstalação segura** sem deixar rastro:
  - Limpeza de volumes, networks, secrets
  - Rollback de configurações (SSL, DNS, firewall)
  - Auditoria de dados residuais

### Os Três Pilares da Entrega:
1. **Material 1 — Relatório de Auditoria Executivo:**
   - Snapshot do estado atual (consumo, componentes, vulnerabilidades)
   - Análise de headroom (pode instalar?)
   - Recomendações e riscos

2. **Material 2 — Stacks Docker Swarm Integrados:**
   - `docker-compose-prod.yml` (produção)
   - `docker-compose-staging.yml` (testes)
   - `.env` template com validação

3. **Material 3 — Manuais de Instalação & Desinstalação:**
   - Guia de instalação cirúrgica (pré-checks, deploy, validação)
   - Guia de desinstalação segura (rollback, limpeza)
   - Playbook de troubleshooting (erros comuns)

---

## 3. O Paradigma R5-VPS (Auditoria & Incorporação)

O **Padrão Diamante VPS (R5-VPS)** normaliza a auditoria e incorporação segura:

- **Relatório Tripartite:** HTML executivo, Markdown técnico, PDF impresso
- **Hero Stats Bar de Infraestrutura:** Consumo atual, headroom disponível, score de saúde
- **Matriz de Compatibilidade:** Versões Docker, Kernel, SO vs. requisitos do stack
- **Timeline de Instalação:** Estimativa de downtime, janelas de deploy seguras
- **Rollback Automático:** Se falhar em qualquer stage, voltar ao estado anterior

---

## 4. Integração com Portainer API

Fluxo 5 conecta-se à Portainer (quando disponível) para:

```
┌─────────────────────────────────────┐
│     Portainer API (Token)           │
│  GET /api/endpoints/{id}/stats      │
│  GET /api/containers                │
│  GET /api/images                    │
│  GET /api/volumes                   │
└─────────────────────────────────────┘
         ↓
┌─────────────────────────────────────┐
│  Auditor VPS (Fluxo 5)              │
│  - Parse JSON de estado             │
│  - Calcular headroom                │
│  - Validar compatibilidade          │
│  - Gerar recomendações              │
└─────────────────────────────────────┘
         ↓
┌─────────────────────────────────────┐
│  Outputs: Relatório + Stacks        │
│  - audit-report-<slug>.html         │
│  - docker-compose-prod.yml          │
│  - install-<slug>.md                │
│  - uninstall-<slug>.md              │
└─────────────────────────────────────┘
```

---

## 5. Estrutura Modular dos Pacotes (Bundles)

Para cada ferramenta/ecossistema auditado, o módulo gera um **Bundle Soberano Estruturado** em `output/05-auditorias-vps/<slug>/`:

```
output/05-auditorias-vps/<slug>/
├── 00-livro-mestre-compilado/
│   ├── relatorio-auditoria-<slug>.[html | md | pdf]
│   └── index.html (gateway central)
├── 01-guias-executivos-e-viabilidade/
│   ├── snapshot-infraestrutura-<slug>.html
│   ├── analise-headroom-<slug>.md
│   └── recomendacoes-<slug>.pdf
├── 02-guias-de-engenharia-e-infraestrutura/
│   ├── topologia-atual-<slug>.html (diagrama Portainer)
│   ├── compatibilidade-versoes-<slug>.md
│   └── matriz-risco-<slug>.pdf
├── 03-playbooks-de-instalacao-e-operacao/
│   ├── manual-instalacao-cirurgica-<slug>.html
│   ├── docker-compose-prod.yml
│   └── docker-compose-staging.yml
├── 04-playbooks-de-desinstalacao-e-governanca/
│   ├── manual-desinstalacao-cirurgica-<slug>.html
│   ├── rollback-playbook-<slug>.md
│   └── limpeza-estado-<slug>.sh
├── <slug>.typ (fonte Typst master)
└── relatorio-execucao-<slug>.[html | md | pdf]
```

---

## 6. Governança & Conformidade Corporativa

Cada auditoria gerada segue rigorosamente:
- **R5-VPS (Padrão Diamante VPS):** HTML normalizado, hero stats de infraestrutura
- **R13 (Taxonomia & Slugs):** Nomes `guia-<slug>.html`, slugs ≤ 35 caracteres
- **R15 (Segredos & Credenciais):** Zero tokens/senhas nos outputs; `.env.example` com validação
- **R20 (Proibição de Emojis):** Visual 100% corporativo
- **R21 (Didática Universal):** Acessível para gestores sem formação DevOps

---

## 7. Fluxo Operacional Típico

```
1. Usuário executa: /fluxo5 --slug stack-ia --portainer-url https://portainer.empresa.com.br
2. Fluxo 5 conecta-se à API Portainer com token (.env)
3. Auditoria em tempo real: snapshots de CPU, RAM, Disco, containers
4. Análise de headroom: pode instalar stack-ia? (8 componentes, 32GB RAM necessários)
5. Geradores de stacks: docker-compose-prod.yml com Traefik labels, volumes, secrets
6. Manuais interativos: instalação passo-a-passo com pre-checks automáticos
7. Relatório final: HTML + PDF para executivos/compliance
8. SQLite R11: grava resultado com timestamp, tokens, status
```

