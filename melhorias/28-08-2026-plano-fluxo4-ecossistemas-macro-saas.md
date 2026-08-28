# Plano de Ação · Fluxo 4: Ecossistemas & Macro-SaaS AIDD

> **Data:** 28/08/2026  
> **Status:** Em Implementação  
> **Objetivo:** Estabelecer a esteira determinística tripartite do **Fluxo 4** para mapear e desmantelar Macro-Ecossistemas SaaS Multimodais (ex: *RD Station Suite, Google Workspace, Zoho One, Atlassian Suite, Microsoft 365, Adobe Creative Cloud*).

---

## 1. Visão Geral & Demanda

Diferente de um SaaS pontual (Fluxo 2) ou de uma camada tecnológica isolada (Fluxo 1), grandes organizações operam sob **Macro-Ecossistemas de Software** compostos por múltiplos pilares funcionais interdependentes.

No caso do **RD Station Suite**, o ecossistema é formado por 3 frentes centrais:
1. **RD Station Marketing:** Automação de marketing, landing pages, nutrição de leads e disparos de e-mail;
2. **RD Station CRM:** Pipeline de vendas comercial, gestão de oportunidades, follow-ups e contratos;
3. **RD Station Conversas (WhatsApp/Omnichannel):** Atendimento multicanal centralizado, chatbots e mensageria.

O **Fluxo 4** resolve a substituição integrada de toda essa suíte, incluindo a **Camada de Cola** (Autenticação SSO, Barramento de Eventos via Webhooks, Reverse Proxy e Orquestração unificada).

---

## 2. Taxonomia & Governança

- **Prefixo de Arquivo:** `ecos-<slug>` (ex: `ecos-rd-station-suite.html`, `ecos-rd-station-suite.md`, `ecos-rd-station-suite.pdf`)
- **Pasta Soberana de Saída:** `output/04-ecossistemas/ecos-<slug>/`
  - `materiais/ecos-<slug>.{html,md,pdf}`
  - `relatorios/DD-MM-AAAA-relatorio-execucao-ecos-<slug>.{html,md,pdf}`
- **Entrada de Dados:** `scripts/data/ecos-<slug>.json`
- **Registro no Catálogo Mestre (SQLite R11):** Tabela `ecossistemas` e relacionamentos com `ferramentas`.

---

## 3. Estrutura do Schema Declarativo (`scripts/schemas/schema_ecossistema.json`)

1. **Raiz:**
   - `slug`, `nome_ecossistema`, `titulo`, `subtitulo`, `deck`, `saas_substituido`, `custo_saas_global_anual`, `stats`
2. **Pilares Funcionais (`pilares`):**
   - Mínimo de 2 pilares (ex: Marketing, CRM, Atendimento);
   - Cada pilar contém: `nome_pilar`, `modulo_saas_alvo`, `descricao_pilar`, `ferramentas` (mínimo 2 ferramentas por pilar com rank, nome, licença, o_que_faz, como_funciona, comando_rapido, infra, white_label).
3. **Camada de Orquestração & Cola de Integração (`camada_integracao`):**
   - `autenticacao_sso` (ex: Keycloak / Authentik OIDC);
   - `barramento_eventos` (ex: n8n / RabbitMQ);
   - `gateway_reverse_proxy` (ex: Traefik / Nginx Proxy Manager);
   - `diagrama_arquitetura_ascii_ou_mermaid`.
4. **Deploy All-in-One (`deploy_consolidado`):**
   - `docker_compose_unificado` (trecho prático de subida dos serviços interligados em rede interna `network: ecosystem_net`);
   - `dimensionamento_vps_recomendado` (CPU, RAM, Armazenamento, Custo mensal total).
5. **Demonstrativo Financeiro & TCO Global:**
   - Comparativo consolidado de todos os módulos SaaS somados vs. VPS corporativa única com Payback estimado.

---

## 4. Componentes a Implementar

| Componente | Arquivo | Responsabilidade |
|---|---|---|
| **Registro de Tipos** | `scripts/tipos.py` | Adicionar `dossie_ecossistema_html` mapeando schemas e gates. |
| **Schema JSON** | `scripts/schemas/schema_ecossistema.json` | Definição formal da estrutura do JSON de ecossistema. |
| **Linter de Gate R9** | `scripts/validar_schemas_fluxos.py` | Função `validar_ecossistema()` com bloqueio mecânico. |
| **Compilador Tripartite** | `scripts/compilar_ecossistema_tripartite.py` | Geração de HTML Diamante R5-E, Markdown e PDF Typst. |
| **CLI Runner** | `scripts/run_fluxo4.py` | Runner do Fluxo 4 integrado à ingestão e portal mestre. |
| **Skill Especialista** | `.agents/skills/fluxo4-ecossistemas/SKILL.md` | Skill do agente e slash command `/fluxo4`. |
| **Ingestão SQLite R11** | `scripts/popular_catalogo_mestre.py` | Ingestão de ecossistemas e vínculo com catálogo mestre. |
| **Portal Mestre** | `scripts/gerar_indice_mestre_cruzado.py` | Nova seção de Ecossistemas & Macro-SaaS no portal. |
| **Governança Master** | `AGENTS.md` | Registro do Fluxo 4 na lista canônica AIDD. |

---

## 5. Execução do Primeiro Caso Canônico

- **Ecossistema:** `rd-station-suite` (RD Station Marketing + RD Station CRM + RD Station Conversas + n8n + Keycloak).
- **Geração:** Execução de `python scripts/run_fluxo4.py --ecossistema rd-station-suite`.
- **Validação:** Verificação tripartite e aprovação em todos os gates mecânicos.
