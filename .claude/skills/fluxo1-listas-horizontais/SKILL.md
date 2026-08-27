---
name: fluxo1-listas-horizontais
description: Especialista no acionamento e orquestração do Fluxo 1 (Fábrica Universal de Listas Horizontais). Mapeia ferramentas open source por camada tecnológica, valida licenças OSI, compila nos 3 formatos (HTML Diamante R5, Markdown e PDF Typst) e registra o estado no banco SQLite.
alwaysApply: false
---

# Skill Especialista · Fluxo 1: Listas Horizontais AIDD

Esta skill governa a geração determinística de **Listas Temáticas Horizontais** cobrindo tanto as 49 camadas já catalogadas quanto **novas camadas e temas sob demanda** criados do zero.

## Quando Usar
- Quando o usuário pedir para gerar, atualizar ou compilar uma lista horizontal;
- Quando o comando `/fluxo1` for disparado com um slug existente ou com um **tema livre novo** (ex: `/fluxo1 experiencia do usuario com a empresa, CX`);
- Quando o usuário solicitar alternativas open source para qualquer categoria de software.

## Protocolo de Execução Agêntica

### Caso 1 · Camada Já Existente (ou com JSON em `scripts/data/`):
1. Execute diretamente o runner oficial:
   ```bash
   python scripts/run_fluxo1.py --slug <slug-da-camada>
   ```

### Caso 2 · Nova Camada Temática (Pesquisa & Geração Autônoma):
Se o tema solicitado pelo operador não existir previamente:
1. **NUNCA** recuse nem diga que precisa de um arquivo pré-existente. A Fábrica Universal é ativa e geradora!
2. **Normalização do Slug:** Converta o tema em slug canônico limpo (ex: `list-experiencia-usuario-cx`).
3. **Mapeamento & Curadoria (5 a 10 Ferramentas):**
   Mapeie as ferramentas líderes mundiais open source da categoria, coletando:
   - Nome, subtítulo, licença OSI estrita, SaaS substituído e economia anual;
   - O Que Faz e Como Funciona com comando rápido de inicialização (`docker run` ou `docker compose`);
   - Análise Econômica (custo SaaS vs. VPS, ROI em meses);
   - Requisitos de infraestrutura (RAM, CPU, Banco de dados e URL oficial do GitHub);
   - 3 Passos práticos de uso no dia a dia (`passos_praticos`);
   - Seção de White-Label & Aderência ao Design System Corporativo (esforço, stack UI e manutenibilidade).
4. **Persistência do JSON:** Salve os dados em `scripts/data/lista-<slug>.json`.
5. **Compilação Tripartite Diamante:**
   Execute o compilador canônico:
   ```bash
   python scripts/compilar_lista_horizontal_tripartite.py --slug <slug>
   ```

### 3. Verificação de Entregas Tripartites:
Certifique-se de que os três arquivos foram gerados na pasta soberana única `output/01-listas-horizontais/list-<slug>/`:
- `list-<slug>.html` (Header Hero Stats, busca interativa client-side, Padrão Diamante R5 rigoroso sem `div.cols`);
- `list-<slug>.md` (Markdown denso com todas as fichas técnicas detalhadas);
- `list-<slug>.pdf` (Compilação Typst anti-sobreposição).

### 4. Apresentação ao Usuário:
Apresente a tabela resumida das ferramentas catalogadas com link direto para os arquivos gerados.
