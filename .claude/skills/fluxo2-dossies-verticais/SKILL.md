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

1. **Identificação do SaaS Alvo (Gate de Entrada):**
   - Se o usuário forneceu o SaaS alvo (ex: `/fluxo2 granola`), prossiga imediatamente;
   - Se não informou, solicite o nome ou categoria do SaaS no chat.

2. **Acionamento Determinístico via CLI:**
   Execute o runner oficial:
   ```bash
   python scripts/run_fluxo2.py --saas <saas-slug>
   ```

3. **Verificação dos Critérios R5-V:**
   O dossiê deve respeitar estritamente a Regra R5-V:
   - Caixa de Alvo SaaS com preço e riscos de privacidade;
   - Quinteto Soberano classificado em: *A Mais Robusta*, *A Mais Completa*, *A Mais Moderna*, *A Mais Leve* e *A Mais Simples*;
   - Seção 5: White-Label & Aderência ao Design System Corporativo;
   - Seção 6: Uso Complementar & Ecossistema Agêntico (MCPs, Skills & Plugins);
   - Scrollbars de no máximo 4px na cor accent.

4. **Entregas em `output/02-dossies-verticais/vert-<saas>/`:**
   - `vert-<saas>.html` (Interativo Diamante R5-V);
   - `vert-<saas>.md` (Markdown executivo);
   - `vert-<saas>.pdf` (Typst anti-sobreposição).

5. **Apresentação ao Usuário:**
   Exiba o resumo do Quinteto Soberano com as 5 categorias e links diretos para os artefatos.
