---
name: fluxo1-listas-horizontais
description: Especialista no acionamento e orquestração do Fluxo 1 (Fábrica Universal de Listas Horizontais). Mapeia ferramentas open source por camada tecnológica, valida licenças OSI, compila nos 3 formatos (HTML Diamante, Markdown e PDF Typst) e registra o estado no banco SQLite.
alwaysApply: false
---

# Skill Especialista · Fluxo 1: Listas Horizontais AIDD

Esta skill governa a geração determinística de **Listas Temáticas Horizontais** cobrindo as 49 camadas da arquitetura de software open source.

## Quando Usar
- Quando o usuário pedir para gerar, atualizar ou compilar uma lista horizontal;
- Quando o comando `/fluxo1` ou `/lista-horizontal` for disparado;
- Quando o usuário solicitar alternativas open source para uma categoria de infraestrutura (ex: bancos de dados, observabilidade, brokers, auth, caches).

## Protocolo de Execução Agêntica

1. **Identificação da Camada (Gate de Entrada):**
   - Se o usuário informou o slug ou o tema (ex: `/fluxo1 bancos-dados-estado`), prossiga imediatamente;
   - Se o usuário não informou o tema, pergunte no chat de forma concisa qual das 49 camadas ele deseja mapear.

2. **Acionamento Determinístico via CLI:**
   Execute o runner oficial:
   ```bash
   python scripts/run_fluxo1.py --slug <slug-da-camada>
   ```

3. **Verificação de Entregas Tripartites:**
   Certifique-se de que os três arquivos foram gerados em `output/01-listas-horizontais/list-<slug>/`:
   - `list-<slug>.html` (Header Hero Stats, busca interativa client-side, Padrão Diamante R5);
   - `list-<slug>.md` (Markdown limpo sem preâmbulos);
   - `list-<slug>.pdf` (Compilação Typst anti-sobreposição).

4. **Persistência Relacional:**
   - O runner grava automaticamente no banco SQLite `estado_esteira.db` (Regra R11).

5. **Apresentação ao Usuário:**
   Apresente a tabela resumida das ferramentas catalogadas com link direto para os arquivos gerados.
