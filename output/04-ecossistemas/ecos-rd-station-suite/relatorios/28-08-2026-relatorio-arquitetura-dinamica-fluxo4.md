# Relatório Técnico de Arquitetura Dinâmica · Macro-Ecossistemas (Fluxo 4 AIDD)

> **Documento:** Especificação da Arquitetura Orientada a Dados e Polimorfismo Generativo  
> **Data de Emissão:** 28/08/2026  
> **Classificação:** Governança Técnica AIDD (Regras R8, R9, R11 e R12)  
> **Autor:** Antigravity (Google DeepMind Team) & Squad Open Source  

---

## 1. Visão Geral & Desafio de Engenharia

Ao analisar macro-ecossistemas de software corporativo (como *RD Station Suite*, *Atlassian Suite*, *Zendesk Suite*, *HubSpot*, *Google Workspace* e *Microsoft 365*), cada suíte de mercado apresenta:
- **Agrupamentos funcionais distintos** (ex: Marketing/CRM vs. GitOps/ITSM vs. Helpdesk/Telefonia);
- **Topologias de infraestrutura sob medida** (diferentes bancos, filas e volumes);
- **Protocolos de migração e automações específicos** para cada caso de uso;
- **Modelos de precificação SaaS heterogêneos** (por lead, por desenvolvedor, por atendente ou por volume de dados).

Para evitar código duplicado ou regras rígidas engessadas no código-fonte, o **Fluxo 4 (Fábrica Universal de Macro-Ecossistemas AIDD)** foi desenvolvido sob o princípio da **Arquitetura Orientada a Dados (Data-Driven Generative Architecture)**.

---

## 2. Diagrama de Fluxo e Polimorfismo Generativo

```
                 [ Dataset Declarativo JSON ]
                 (scripts/data/ecos-<slug>.json)
                               │
            ┌──────────────────┴──────────────────┐
            ▼                                     ▼
 [ Exemplo: Atlassian Suite ]            [ Exemplo: Google Workspace ]
 ├── Pilar 1: Gestão Ágil (Jira)         ├── Pilar 1: Docs & Sheets (Office)
 ├── Pilar 2: Documentação (Confluence)  ├── Pilar 2: Storage & Drive (Cloud)
 ├── Pilar 3: Repositórios (Bitbucket)   ├── Pilar 3: E-mail & Contatos (Gmail)
 └── Pilar 4: ITSM (Jira Service Desk)   └── Pilar 4: Videoconferência (Meet)
                               │
                               ▼
               [ Compilador Genérico do Fluxo 4 ]
           (scripts/compilar_ecossistema_tripartite.py)
                               │
 ┌─────────────────────────────┼─────────────────────────────┐
 ▼                             ▼                             ▼
Iteração Dinâmica            Docker Compose &            Fascículos & Guias
sobre N Pilares              Stack Customizada           Especializados
(Cria N seções e N cards)    (Lê os N contêineres)       (Gera N páginas modulares)
```

---

## 3. Os 4 Mecanismos de Dinamicidade do Compilador

### 3.1. Iteração Polimórfica de Pilares Funcionais (`pilares: [...]`)
- O schema JSON não fixa nomes nem quantidades de grupos funcionais;
- O compilador itera dinamicamente através de `for p_idx, p in enumerate(dados['pilares'])`:
  - Se a suíte possui **2 pilares** (ex: *HubSpot Starter: Marketing + CRM*), são compilados 2 grupos e 10 ferramentas;
  - Se a suíte possui **4 pilares** (ex: *Atlassian Suite: Jira, Confluence, Bitbucket, Service Desk*), são compilados 4 grupos e 20 ferramentas;
- Todos os subtotais de economia, identificação de módulos SaaS concorrentes, tabelas comparativas e badges de classificação persona são computados e renderizados dinamicamente.

### 3.2. Orquestração e Deploy All-in-One Sob Medida (`deploy_consolidado: {...}`)
- A infraestrutura gerada reflete exatamente os contêineres e as interdependências da suíte declarada:
  - Para a **Atlassian Suite**: a stack orquestrará contêineres para *Plane/Leantime*, *Wiki.js/Outline*, *Gitea/Forgejo* e *Zammad*;
  - Para a **Google Workspace Suite**: a stack orquestrará *Nextcloud*, *Collabora Online*, *Mailcow* e *Jitsi Meet*;
- A tabela síntese de portas, volumes, redes e rótulos do Traefik é construída a partir da lista `composicao_stack_detalhada[]`.

### 3.3. Blueprints n8n e Roteiros de Migração Contextuais
- As automações em JSON e as etapas de migração adaptam-se aos protocolos de cada nicho:
  - **Marketing & Vendas:** Migração de contatos (CSV), campos customizados, funis Kanban e QR Code do WhatsApp;
  - **Engenharia de Software & DevOps:** Migração de repositórios Git (`git push --mirror`), issues/epics e pipelines CI/CD;
  - **Suporte ao Cliente & Helpdesk:** Migração de histórico de chamados, base de conhecimento e métricas de SLA.

### 3.4. Calculadora Interativa de TCO Parametrizada
- A lógica em JavaScript dos sliders de simulação financeira utiliza os coeficientes e faixas de custo unitário definidos no dataset (ex: *preço por lead*, *preço por desenvolvedor*, *preço por operador*), recalculando o payback e o ROI em tempo real.

---

## 4. Como Adicionar um Novo Macro-Ecossistema (Passo a Passo)

Graças ao desacoplamento total entre o código e os dados, **adicionar uma nova suíte ao projeto exige zero modificação no compilador**:

1. **Criar o Dataset:** Criar o arquivo `scripts/data/ecos-<slug>.json` seguindo o `scripts/schemas/schema_ecossistema.json`;
2. **Executar o Runner:**
   ```powershell
   python scripts/run_fluxo4.py --ecossistema atlassian-suite
   ```
3. **Resultado Automático:**
   - Validação estrita de integridade via Gate R9;
   - Geração dos materiais tripartites (HTML Diamante R5-E interativo, Markdown e PDF Typst);
   - Registro automático no banco SQLite (`estado_esteira.db` - Regra R11);
   - Atualização do Catálogo Mestre e Portal Central (`INDICE-MESTRE.html`);
   - Versionamento e sincronização com o repositório Git (Regra R16).

---

**Status da Governança:** ✅ Arquitetura 100% Determinística, Idempotente e Conforme às Regras R1 a R19 da Fábrica Universal AIDD.
