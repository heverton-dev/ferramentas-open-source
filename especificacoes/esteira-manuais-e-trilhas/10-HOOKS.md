# 10 · Ciclo de Vida & Automações Mecânicas (Hooks)

> **Módulo:** Esteira Autônoma de Ingestão de Fontes, Manuais VPS e Trilhas de Aprendizado  
> **Arquitetura de Hooks:** Pre-Flight, In-Flight, Post-Flight e Git Pre-Commit  
> **Status:** Produção Homologada · Nota 10.0 / 10.0

---

## 1. O Conceito de Hooks no AI-Driven Development

Hooks são **pontos de interceptação determinísticos** no ciclo de vida de uma esteira. Eles garantem que nenhuma fase avance sem que as condições de contorno e critérios de integridade estejam satisfeitos.

```
[Início da Sessão]
       │
       ▼
┌──────────────────┐
│ Pre-Flight Hook  │ ➔ Valida ambiente, Python >= 3.10, Typst CLI e Schemas
└────────┬─────────┘
         │ OK
         ▼
┌──────────────────┐
│  In-Flight Hook  │ ➔ Executa Gate G0 (Qualidade) e Gate G1 (HTTP 200)
└────────┬─────────┘
         │ OK
         ▼
[Compilação Tripartite (Manual + Trilha)]
         │
         ▼
┌──────────────────┐
│  In-Flight Hook  │ ➔ Executa Gate G2 (Citações Biunívocas sem Alucinação)
└────────┬─────────┘
         │ OK
         ▼
┌──────────────────┐
│ Post-Flight Hook │ ➔ Emite Relatório Tripartite, grava SQLite e espelha em docs/
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Git Pre-Commit   │ ➔ Bloqueia commit se houver entulho ou divergência R18
└──────────────────┘
```

---

## 2. Detalhamento dos 4 Hooks da Esteira

### 2.1. Pre-Flight Hook (Validação de Pré-Voo)
- **Momento:** Disparado antes de processar qualquer ferramenta.
- **Validações:**
  1. Presença do compilador Typst no PATH (`typst --version`);
  2. Presença dos schemas JSON em `scripts/schemas/`;
  3. Existência do dossiê vertical do SaaS em `scripts/data/dossie-vertical-<saas>.json`;
  4. Conexão ativa com o banco SQLite `estado_esteira.db`.
- **Ação em caso de falha:** Aborta a execução imediatamente com mensagem explicativa no terminal.

### 2.2. In-Flight Hooks (Portões Intermediários)
- **Gate G0:** Roda logo após a indexação do sumário JSON. Analisa os 4 pilares: Autoridade de Domínio (Whitelist), Recência (>= 2024), Densidade Técnica e Integridade de Metadados. Se reprovar, aborta antes de gastar recursos de rede.
- **Gate G1:** Disparado após o Gate G0. Executa requisições assíncronas reais com timeout de 10 segundos. Se qualquer URL retornar 404, 500 ou timeout, aborta a esteira.
- **Gate G2:** Disparado logo após a compilação do manual. Audita os blocos de comando e rotas de API. Se houver qualquer ID citado que não conste no sumário, ou qualquer ID do sumário não citado no manual, o Gate G2 reprova com código `exit 1`.

### 2.3. Post-Flight Hook (Fechamento & Telemetria)
- **Momento:** Disparado quando os manuais e trilhas são compilados com sucesso.
- **Ações Automáticas:**
  1. Cronometra o tempo total decorrido com precisão de milissegundos;
  2. Compila o Relatório Tripartite (`.html`, `.md`, `.pdf`) em `output/<slug>/relatorios/`;
  3. Registra os metadados e status na tabela `esteira_manuais_bundles` do SQLite;
  4. Executa a sincronização byte a byte em `docs/<slug>/` para manter a conformidade R18.

### 2.4. Git Pre-Commit Hook (Guardião do Versionamento)
- **Momento:** Disparado pelo Git antes da criação de qualquer commit (`.git/hooks/pre-commit`).
- **Scripts Acionados:**
  - `python scripts/auditar_higiene_repo.py` (Zero entulho, sem arquivos temporários, paridade MD5 de espelhos);
  - `python tests/test-syntax.py` (Validação de sintaxe de todos os scripts e arquivos JSON);
  - `python tests/test_esteira_manuais.py` (Suíte de 8 testes unitários da esteira).
- **Resultado:** Se qualquer script retornar erro, o Git cancela o commit e impede que código instável seja versionado.
