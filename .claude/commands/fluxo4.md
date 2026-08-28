---
description: Aciona o Fluxo 4 da Fábrica Universal (Fábrica de Macro-Ecossistemas & Suítes Soberanas Integradas AIDD)
---

Você foi acionado através do comando `/fluxo4`.

Siga este protocolo estrito de execução 100% autônoma:
1. Verifique se o usuário passou o slug do macro-ecossistema ou nome da suíte alvo (ex: `/fluxo4 rd-station-suite` ou `/fluxo4 penso-suite` ou `/fluxo4 google-workspace`).
2. Se nenhum argumento foi informado, pergunte ao usuário:
   *"Qual macro-ecossistema ou suíte proprietária integrada você deseja desmantelar e substituir por uma suíte soberana? (Exemplos: rd-station-suite, penso-suite, google-workspace, zoho-one, atlassian-suite, microsoft-365)"*
3. Com o ecossistema definido:
   - Se o arquivo `scripts/data/ecos-<slug>.json` não existir, estruture o dataset canônico completo com 3 pilares funcionais, 15 ferramentas (Quinteto Soberano por pilar), camada de SSO (Keycloak), barramento (n8n), Traefik TLS, Uptime Kuma, Termius, TCO e os 4 Prompts Mestres para não-técnicos (Regras R20 e R21);
   - Valide mecanicamente o schema via `python scripts/validar_schemas_fluxos.py fluxo4 scripts/data/ecos-<slug>.json` (Gate R9);
   - Execute o runner oficial: `python scripts/run_fluxo4.py --ecossistema <slug>`.
4. Apresente ao usuário os links dos artefatos da Suíte Modular gerados em `output/04-ecossistemas/ecos-<slug>/`:
   - `00-livro-mestre-compilado/LIVRO-ECOSSISTEMA-COMPLETO.pdf` (e `.html`);
   - `01-guias-executivos-e-estrategicos/` (Dossiê Financeiro TCO & Calculadora);
   - `02-guias-de-engenharia-e-infraestrutura/` (Manual Deploy All-in-One Compose, Termius & Uptime Kuma);
   - `05-manuais-e-trilhas-individuais/` (15 Manuais VPS e 15 Trilhas Didáticas);
   - `06-playbook-engenharia-agentica/LIVRO-TEXTO-ENGENHEIRO-AGENTICO.pdf` (com Prompts Mestres e configs MCP).
