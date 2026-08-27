---
name: fluxo2-dossies-verticais
description: Especialista no acionamento e orquestração do Fluxo 2 (Dossiês Verticais de Desmantelamento SaaS). Elege o Quinteto Soberano, mapeia o ecossistema agêntico (MCPs/Skills), analisa white-label e compila o dossiê R5-V tripartite com registro no SQLite.
alwaysApply: false
---

# Skill Especialista · Fluxo 2: Dossiês Verticais AIDD

Esta skill governa o **Desmantelamento Cirúrgico de SaaS Proprietários**, substituindo monopólios caros pelo Quinteto Soberano e pelo ecossistema agêntico de código aberto.

## Quando Usar
- Quando o usuário pedir para analisar ou desmantelar um SaaS proprietário específico (ex: Granola, Notion, Zapier, Salesforce, Airtable);
- Quando o comando `/fluxo2` ou `/dossie-vertical` for disparado;
- Quando o usuário quiser eleger o Quinteto Soberano de alternativas livres.

## Protocolo de Execução Agêntica

### Caso 1 · SaaS Já Existente (ou com JSON em `scripts/data/`):
1. Execute diretamente o runner oficial:
   ```bash
   python scripts/run_fluxo2.py --saas <saas-slug>
   ```

### Caso 2 · Novo SaaS Sob Demanda (Pesquisa & Geração Autônoma):
Se o SaaS solicitado pelo operador não existir previamente:
1. **NUNCA** recuse nem diga que precisa de um arquivo pré-existente. A Fábrica Universal é ativa e geradora!
2. **Normalização do Slug:** Converta o SaaS em slug limpo (ex: `vert-twilio`, `vert-zendesk`).
3. **Mapeamento do Quinteto Soberano (5 Ferramentas):**
   Elege rigorosamente as 5 ferramentas classificadas em:
   - *A Mais Robusta*: Gateway corporativo de alta disponibilidade;
   - *A Mais Completa*: Plataforma enterprise com suite ampla de recursos;
   - *A Mais Moderna*: Arquitetura de última geração e stack contemporânea;
   - *A Mais Leve*: Binário ultraleve de baixo consumo de RAM;
   - *A Mais Simples*: Instalação em 1 comando para testes e sandbox.
4. **Mapeamento de White-Label & Design System (Seção 5):**
   Defina esforço (Baixo/Médio/Alto), stack UI, mecânica de customização e impacto em upgrades.
5. **Mapeamento do Ecossistema Agêntico (Seção 6):**
   Mapeie servidores MCP, Agent Skills e plugins reais para integração com LLMs.
6. **Persistência do JSON:** Salve os dados em `scripts/data/dossie-vertical-<saas>.json`.
7. **Compilação Tripartite Diamante:**
   Execute o compilador oficial:
   ```bash
   python scripts/gerar_dossie_vertical_tripartite.py --saas <saas>
   ```

3. **Verificação dos Critérios R5-V:**
   O dossiê deve respeitar estritamente a Regra R5-V:
   - Caixa de Alvo SaaS com preço e riscos de privacidade;
   - Quinteto Soberano classificado em: *A Mais Robusta*, *A Mais Completa*, *A Mais Moderna*, *A Mais Leve* e *A Mais Simples*;
   - Seção 5: White-Label & Aderência ao Design System Corporativo;
   - Seção 6: Uso Complementar & Ecossistema Agêntico (MCPs, Skills & Plugins);
   - Scrollbars de no máximo 4px na cor accent.

4. **Entregas em `output/02-dossies-verticais/vert-<saas>/`:**
   - `materiais/vert-<saas>.html` (Interativo Diamante R5-V);
   - `materiais/vert-<saas>.md` (Markdown executivo);
   - `materiais/vert-<saas>.pdf` (Typst anti-sobreposição);
   - `relatorios/DD-MM-AAAA-relatorio-execucao-<saas>.{html,md,pdf}` (Relatório Tripartite).

5. **Apresentação ao Usuário:**
   Exiba o resumo do Quinteto Soberano com as 5 categorias e links diretos para os artefatos.
