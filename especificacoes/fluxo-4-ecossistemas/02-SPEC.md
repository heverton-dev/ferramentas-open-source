# 02 · Especificação Técnica (Fluxo 4: Macro-Ecossistemas)

> **Módulo:** Fluxo 4 — Macro-Ecossistemas e Suítes Integradas

---

## 1. Requisitos Funcionais Obrigatórios

- **RF01 (Taxonomia R13):** Nome de arquivo deve seguir `ecos-<slug-curto>.[html|md|pdf]`, slugs ≤ 35 caracteres;
- **RF02 (Hero Stats Bar Agregada):** Contadores de componentes, layers arquiteturais, compatibilidade de versões, TCO agregado;
- **RF03 (Diagramas Interativos):** Topologia de rede, fluxos de dados e arquitetura em formato SVG/Mermaid;
- **RF04 (Compilação Tripartite):** Geração automática de HTML R5-E, Markdown (7 arquivos) e PDF Typst;
- **RF05 (Validação de Compatibilidade):** Auditoria de conflitos de versão, APIs internas, requisitos de hardware;
- **RF06 (Persistência SQLite R11):** Registro em tabela `esteira_ecossistemas` com slug, componentes, versões e status;
- **RF07 (Modulação em Diretórios):** Estrutura em 5 subdiretórios (`00-livro-mestre/`, `01-executivos/`, `02-engenharia/`, `03-instalacao/`, `04-desinstalacao/`);
- **RF08 (Links Interconectados):** Botões de ação contextuais ("Deploy em Docker", "Consultar Manual VPS", "Abrir Trilha").

---

## 2. Requisitos Não-Funcionais

- **RNF01 (Determinismo R8):** Compilação local, sem chamadas à LLM para conteúdo estático;
- **RNF02 (Idempotência R10):** Reexecução com mesmo slug produz mesmos hashes;
- **RNF03 (Segurança R15):** Zero credenciais hardcoded; validação de `.env.example` via pre-commit;
- **RNF04 (Performance):** Compilação de um ecossistema completo em < 60 segundos;
- **RNF05 (Escalabilidade):** Suporte a ecossistemas com 8+ componentes sem degradação.

---

## 3. Estrutura de Dados de Entrada

```json
{
  "slug": "stack-ia-corporativa",
  "nome": "Stack de IA Corporativa",
  "descricao": "Suite completa de IA open source para empresas",
  "componentes": [
    {
      "nome": "LangChain",
      "versao": "0.2.0",
      "url": "https://github.com/langchain-ai/langchain",
      "papel": "Orquestrador de LLMs e agentes",
      "licenca": "MIT",
      "conflitos_conhecidos": []
    },
    {
      "nome": "Ollama",
      "versao": "0.3.0",
      "url": "https://github.com/ollama/ollama",
      "papel": "Runtime de LLMs locais",
      "licenca": "MIT",
      "conflitos_conhecidos": ["CUDA < 11.8 pode causar crash"]
    }
  ],
  "arquitetura": "3-layer (Frontend, Orchestration, LLM+Storage)",
  "requisitos_minimos": {
    "cpu": "8 cores",
    "ram": "32 GB",
    "disco": "500 GB SSD"
  }
}
```

---

## 4. Saídas Esperadas

Para cada ecossistema, o fluxo gera:

```
output/04-ecossistemas/ecos-<slug>/
├── livro-mestre-<slug>.html        (R5-E com interatividade)
├── livro-mestre-<slug>.md          (Markdown agregado)
├── livro-mestre-<slug>.pdf         (Compilado via Typst)
├── 00-livro-mestre-compilado/
│   └── index.html                  (Gateway central)
├── 01-guias-executivos-e-viabilidade/
│   ├── guia-tco-<slug>.html
│   ├── guia-roi-<slug>.md
│   └── matriz-comparativa-<slug>.pdf
├── 02-guias-de-engenharia-e-infraestrutura/
│   ├── arquitetura-<slug>.html
│   ├── topologia-<slug>.md
│   └── fluxo-dados-<slug>.pdf
├── 03-playbooks-de-instalacao-e-operacao/
│   ├── playbook-deploy-<slug>.html
│   ├── playbook-operacao-<slug>.md
│   └── troubleshooting-<slug>.pdf
├── 04-playbooks-de-desinstalacao-e-governanca/
│   ├── playbook-rollback-<slug>.html
│   ├── playbook-desinstalacao-<slug>.md
│   └── playbook-governanca-<slug>.pdf
├── <slug>.typ                      (Fonte master Typst)
└── relatorio-execucao-<slug>.html
```

---

## 5. Protocolo de Validação (Gates)

| Gate | Critério | Ação em Falha |
|------|----------|---------------|
| Gate 1 | Todos os arquivos gerados e presentes | Reexecutar compilação |
| Gate 2 | HTML valida, MD parseável, PDF renderizável | Validar schema + logs |
| Gate 3 | Ausência de credenciais (regex de secrets) | Bloquear commit |
| Gate 4 | Métricas de profundidade (>8 seções, >5 componentes) | Avisar, não bloquear |

