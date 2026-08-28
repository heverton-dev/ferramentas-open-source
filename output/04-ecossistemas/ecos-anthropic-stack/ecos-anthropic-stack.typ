#set page(
 paper: "a4",
 margin: (x: 1.8cm, top: 2.2cm, bottom: 2.2cm),
 header: align(center)[
  #set par(leading: 0.65em)
  #text(size: 8pt, fill: rgb("#64748b"), font: "Liberation Sans")[Fábrica Universal AIDD · Livro-Texto de Macro-Ecossistema Soberano (Padrão Diamante R5-E)]
 ],
 footer: [
  #set par(leading: 0.65em)
  #text(size: 8pt, fill: rgb("#64748b"), font: "Liberation Sans")[
   #grid(
    columns: (1fr, 1fr),
    [Suíte do Ecossistema Soberano · Anthropic Claude API + Claude Code + MCP Protocol + AI Gateway + Managed Agents],
    align(right)[Fábrica Universal AIDD]
   )
  ]
 ]
)
#set text(font: "Liberation Sans", size: 9.5pt, lang: "pt")
#set par(justify: true, leading: 1.5em)

// DIAGRAMAÇÃO DE TÍTULOS E ESPAÇAMENTOS (HIERARQUIA H1-H6 SEM ESPAÇAMENTO ENTRE LINHAS)
#show heading: it => [
 #set par(leading: 0.45em)
 #it
]

#show heading.where(level: 1): it => block(
 above: 28pt,
 below: 14pt,
 [
  #set par(leading: 0.45em)
  #text(size: 18pt, weight: "bold", fill: rgb("#0f172a"), font: "Liberation Serif")[#it.body]
 ]
)

#show heading.where(level: 2): it => block(
 above: 22pt,
 below: 10pt,
 [
  #set par(leading: 0.45em)
  #text(size: 13.5pt, weight: "bold", fill: rgb("#0f172a"), font: "Liberation Sans")[#it.body]
 ]
)

#show heading.where(level: 3): it => block(
 above: 16pt,
 below: 8pt,
 [
  #set par(leading: 0.45em)
  #text(size: 11pt, weight: "bold", fill: rgb("#1e293b"), font: "Liberation Sans")[#it.body]
 ]
)

#show heading.where(level: 4): it => block(
 above: 14pt,
 below: 6pt,
 [
  #set par(leading: 0.45em)
  #text(size: 10pt, weight: "bold", fill: rgb("#334155"), font: "Liberation Sans")[#it.body]
 ]
)

#show heading.where(level: 5): it => block(
 above: 12pt,
 below: 4pt,
 [
  #set par(leading: 0.45em)
  #text(size: 9.5pt, weight: "bold", fill: rgb("#475569"), font: "Liberation Sans")[#it.body]
 ]
)

#show heading.where(level: 6): it => block(
 above: 10pt,
 below: 4pt,
 [
  #set par(leading: 0.45em)
  #text(size: 9pt, weight: "bold", fill: rgb("#64748b"), font: "Liberation Sans")[#it.body]
 ]
)

// CAPA EDITORIAL EXECUTIVA
#align(center + horizon)[
 #rect(stroke: 2pt + rgb("#0f172a"), inset: 24pt, radius: 4pt, width: 100%)[
  #text(size: 10pt, tracking: 0.2em, weight: "bold", fill: rgb("#00875A"))[FÁBRICA UNIVERSAL AIDD · TRATADO DE ENGENHARIA] \
  #v(12pt)
  #text(size: 24pt, weight: "bold", fill: rgb("#0f172a"), font: "Liberation Serif")[Macro-Ecossistema de IA Aberta: Modelos, Agentes, Orquestração & Inferência] \
  #v(6pt)
  #text(size: 12pt, fill: rgb("#334155"))[Arquitetura Aberta Integrada para Substituição Soberana do Ecossistema Anthropic (Claude Code, API, MCP) com Quinteto Soberano por Grupo, SSO, Barramento de Eventos e MCPs] \
  #v(16pt)
  #line(length: 60%, stroke: 1pt + rgb("#cbd5e1"))
  #v(16pt)
  #text(size: 10pt, fill: rgb("#475569"))[
   *Macro-Ecossistema Alvo:* Anthropic Claude API + Claude Code + MCP Protocol + AI Gateway + Managed Agents \
   *Economia Anual Líquida:* #text(fill: rgb("#00875A"), weight: "bold")[R\$ 151.800/ano (Economia Líquida de 97.3%)] \
   *Padrão Normativo:* Diamante R5-E Tripartite \
   *Publicação:* 28/08/2026 · 1ª Edição Oficial
  ]
 ]
]

#pagebreak()

// SUMÁRIO AUTOMÁTICO
#outline(title: [Sumário Geral do Livro-Texto], indent: auto)

#v(16pt)
#line(length: 100%, stroke: 0.5pt + rgb("#e2e8f0"))
#v(16pt)

= Prefácio Executivo & Manifesto da Soberania
Dossiê completo de desmantelamento soberano para o Macro-Ecossistema Anthropic (Claude Code, Claude API, Model Context Protocol, AI Gateway e Managed Agents). Cada frente de desenvolvimento é estruturada com seu próprio Quinteto Soberano (A Mais Robusta, Mais Completa, Mais Moderna, Mais Leve e Mais Simples), acompanhada de análise de TCO, guias práticos de deploy, aderência white-label e ecossistema agêntico de MCPs nativos para integração.

A migração de suítes de software proprietário fechado para ecossistemas open source auto-hospedados em VPS representa a maior alavanca de eficiência operacional da década. Este livro-texto reúne as especificações de engenharia para desmantelar a suíte *Anthropic Claude API + Claude Code + MCP Protocol + AI Gateway + Managed Agents* com segurança jurídica, integridade de dados e autonomia digital irrestrita.

#pagebreak()

= Capítulo 1: Engenharia Financeira, TCO Global & Payback

#grid(
 columns: (1fr, 1fr),
 gutter: 10pt,
 rect(fill: rgb("#fef2f2"), stroke: 0.5pt + rgb("#fecaca"), inset: 10pt, radius: 2pt)[
  #text(size: 8pt, fill: rgb("#991b1b"), weight: "bold")[CUSTO SAAS ANUAL (Anthropic Claude API + Claude Code + MCP Protocol + AI Gateway + Managed Agents)] \
  #text(size: 14pt, weight: "bold", fill: rgb("#dc2626"))[R\$ 156.000/ano (Anthropic API Tier Enterprise R\$ 84k + Claude Code licensing R\$ 48k + AI Gateway/Managed Agents R\$ 24k)]
 ],
 rect(fill: rgb("#f0fdf4"), stroke: 0.5pt + rgb("#bbf7d0"), inset: 10pt, radius: 2pt)[
  #text(size: 8pt, fill: rgb("#166534"), weight: "bold")[ECONOMIA LÍQUIDA ANUAL NO CAIXA] \
  #text(size: 14pt, weight: "bold", fill: rgb("#16a34a"))[R\$ 151.800/ano (Economia Líquida de 97.3%)]
 ]
)

#v(10pt)
- *Custo VPS Própria:* R\$ 4.200/ano (VPS 8 vCPU / 16 GB RAM a R\$ 350/mês em Hetzner Cloud) (Cluster Consolidado 8 vCPU / 16 GB RAM)
- *Retorno sobre Investimento (ROI / Payback):* Payback positivo em apenas 10 dias de operação unificada (VPS paga-se em 3-5 dias vs economia mensal).

#v(10pt)
== Desmembramento Contábil por Frente de Negócio

#table(
 columns: (1.5fr, 1.8fr, 1.2fr, 1.2fr, 0.9fr),
 fill: (x, y) => if y == 0 { rgb("#f1f5f9") } else { none },
 stroke: 0.5pt + rgb("#cbd5e1"),
 inset: 5pt,
 [*Grupo*], [*SaaS Alvo*], [*Custo SaaS*], [*Economia*], [*Margem*],
 [Grupo 1: Orchestração & Agentes LLM], [Anthropic Claude API + Managed Agents], [R\$ 84.000/ano], [R\$ 82.560/ano], [98.3%],
[Grupo 2: Infraestrutura Dev & CI/CD], [GitHub Enterprise + Docker Hub Private + CI/CD SaaS], [R\$ 48.000/ano], [R\$ 46.680/ano], [97.2%],
[Grupo 3: Observabilidade & Monitoramento], [DataDog / New Relic (Professional Tier)], [R\$ 24.000/ano], [R\$ 22.560/ano], [94.0%],

)

#pagebreak()
= Capítulo 2: Infraestrutura Global, Dimensionamento da VPS & Provedores Validados

- *Perfil de Máquina Recomendado:* `8 vCPU / 16 GB RAM ECC / 160-240 GB NVMe`
- *Racional de Engenharia:* 

#v(6pt)
== Provedores de Nuvem Recomendados & Custo Mensal

#table(
 columns: (1.5fr, 1.2fr, 2.3fr),
 fill: (x, y) => if y == 0 { rgb("#f1f5f9") } else { none },
 stroke: 0.5pt + rgb("#cbd5e1"),
 inset: 5pt,
 [*Provedor de Nuvem*], [*Custo Mensal*], [*Vantagem Principal & SLA*],
 
)

#v(8pt)
== Alocação Técnica de Recursos por Serviço (vCPU & RAM)

#table(
 columns: (1.5fr, 0.7fr, 0.7fr, 2.8fr),
 fill: (x, y) => if y == 0 { rgb("#f1f5f9") } else { none },
 stroke: 0.5pt + rgb("#cbd5e1"),
 inset: 4pt,
 [*Serviço / Módulo*], [*vCPU*], [*RAM*], [*Motivo Técnico & Gargalo*],
 
)

#pagebreak()
= Capítulo 3: Matriz Estratégica do Quinteto Soberano

#table(
 columns: (0.5fr, 1.3fr, 1.3fr, 1.8fr, 2.2fr, 1.3fr),
 fill: (x, y) => if y == 0 { rgb("#f1f5f9") } else { none },
 stroke: 0.5pt + rgb("#cbd5e1"),
 inset: 4pt,
 [*Nº*], [*Grupo*], [*Persona*], [*Ferramenta*], [*Substitui*], [*Economia*],
 [1], [Grupo 1], [Completa], [*Ollama*], [Anthropic Claude API (Tier Enterprise / Managed Agents)], [R\$ 84.000/ano (Economia em API calls + Enterprise licensing)],
[2], [Grupo 1], [Robusta], [*LangChain*], [Anthropic Claude Code / Managed Agents Runtime], [R\$ 24.000/ano],
[3], [Grupo 1], [Moderna], [*LlamaIndex*], [Anthropic Claude Code / Knowledge Base Built-in], [R\$ 18.000/ano],
[4], [Grupo 1], [Leve], [*Flowise*], [Anthropic Claude Code (Visual Agent Builder)], [R\$ 14.400/ano],
[5], [Grupo 1], [Simples], [*AnythingLLM*], [ChatGPT / Claude Cloud (Knowledge Base)], [R\$ 12.000/ano],
[6], [Grupo 2], [Completa], [*Gitea*], [GitHub (Team Plan) / GitLab (Premium)], [R\$ 24.000/ano (10 usuários)],
[7], [Grupo 2], [Robusta], [*Woodpecker CI*], [GitHub Actions / GitLab CI / Jenkins], [R\$ 18.000/ano],
[8], [Grupo 2], [Moderna], [*MinIO*], [AWS S3 / Google Cloud Storage], [R\$ 12.000/ano],
[9], [Grupo 2], [Leve], [*Docker Registry*], [Docker Hub (Private Repos) / ECR / GCR], [R\$ 9.600/ano],
[10], [Grupo 2], [Simples], [*Deno*], [Node.js (elimina dependência de npm/package.json)], [R\$ 6.000/ano],
[11], [Grupo 3], [Completa], [*Prometheus*], [DataDog / New Relic (Infrastructure Monitoring)], [R\$ 24.000/ano],
[12], [Grupo 3], [Robusta], [*Grafana*], [DataDog / New Relic (Dashboarding)], [R\$ 18.000/ano],
[13], [Grupo 3], [Moderna], [*Loki*], [DataDog / Splunk / Elasticsearch (Logging)], [R\$ 14.400/ano],
[14], [Grupo 3], [Leve], [*Alertmanager*], [PagerDuty (Alert Routing)], [R\$ 12.000/ano],
[15], [Grupo 3], [Simples], [*OpenTelemetry Collector*], [Datadog / New Relic / Sentry (Tracing & Collection)], [R\$ 9.600/ano],

)


#pagebreak()
= Capítulo 3: Pilar 01 · Grupo 1: Orchestração de Agentes & Modelos LLM

#text(size: 9pt, fill: rgb("#0284c7"), weight: "bold")[Alvo SaaS Substituído: Anthropic Claude API + Claude Code + Managed Agents] \
#text(size: 9pt, fill: rgb("#00875A"), weight: "bold")[Subtotal de Economia do Grupo: R\$ 156.000/ano] \
#text(size: 9pt, style: "italic", fill: rgb("#475569"))[Frente responsável pela construção autônoma de agentes de IA, orquestração de modelos abertos, construção visual de workflows sem código e gerenciamento de memória de longo prazo (RAG).]

#v(8pt)

== 01. Ollama · Executor Local de Modelos LLM Abertos (Llama 2, Mistral, Neural Chat) (Persona: Completa)

#rect(fill: rgb("#f8fafc"), stroke: 0.5pt + rgb("#cbd5e1"), inset: 8pt, radius: 2pt, width: 100%)[
 #grid(
  columns: (1fr, 1fr, 1fr),
  gutter: 6pt,
  [*Substitui:* Anthropic Claude API (Tier Enterprise / Managed Agents)],
  [*Economia:* #text(fill: rgb("#00875A"), weight: "bold")[R\$ 84.000/ano (Economia em API calls + Enterprise licensing)]],
  [*Licença:* `MIT`]
 )
]

*1. O Que Faz & Como Funciona:* \
Fornece CLI e servidor HTTP para executar modelos LLM abertos em uma única máquina ou cluster. Binário Go estático que compacta modelos em formato proprietário otimizado e executa inferência em paralelo com quantização.

```bash
ollama run mistral
```

*2. Racional da Escolha & Veredito Técnico:* \
Permite rodar modelos de 7B a 70B parâmetros localmente com qualidade comparable aos modelos proprietários, eliminando dependência de API remota e acesso seguro a dados sensíveis. \
#text(style: "italic", fill: rgb("#334155"))[*Veredito:* Substitui completamente a necessidade de chamadas remotas à Claude API para operações de raciocínio e geração de texto padrão.]

*3. Requisitos de Infraestrutura & White-Label:* \
- RAM Mínima: `8 GB RAM` | CPU: `1 vCPU` | Docker: `oficial`
- Customização UI: Serviço de backend puro sem UI, operando sob domínio corporativo (ex: `llm.empresa.com.br`). (Esforço: Baixo)

#v(10pt)

== 02. LangChain · Framework de Composição de Agentes, Chains & Memory para LLMs (Persona: Robusta)

#rect(fill: rgb("#f8fafc"), stroke: 0.5pt + rgb("#cbd5e1"), inset: 8pt, radius: 2pt, width: 100%)[
 #grid(
  columns: (1fr, 1fr, 1fr),
  gutter: 6pt,
  [*Substitui:* Anthropic Claude Code / Managed Agents Runtime],
  [*Economia:* #text(fill: rgb("#00875A"), weight: "bold")[R\$ 24.000/ano]],
  [*Licença:* `MIT`]
 )
]

*1. O Que Faz & Como Funciona:* \
Fornece abstrações Python e TypeScript para construir agentes de IA compostos com memory e tool calling. SDK Python/TypeScript com suporte nativo a chain execution, memory backends (Redis, PostgreSQL) e vector stores (Pinecone, Weaviate, Milvus).

```bash
pip install langchain && python -c "from langchain.chat_models import ChatOpenAI; chain = ..."
```

*2. Racional da Escolha & Veredito Técnico:* \
Oferece abstrações robustas para construir agentes complexos sobre Ollama, OpenAI, Anthropic ou qualquer LLM, com suporte nativo a vector stores, caching e rastreamento de custos. \
#text(style: "italic", fill: rgb("#334155"))[*Veredito:* Framework padrão de fato para desenvolvimento de agentes em produção, sustentado pela comunidade global e empresas como Stripe e Hugging Face.]

*3. Requisitos de Infraestrutura & White-Label:* \
- RAM Mínima: `2 GB RAM` | CPU: `1 vCPU` | Docker: `oficial`
- Customização UI: Totalmente customizável via código Python/TypeScript com suporte a prompts corporativos e personas de agentes. (Esforço: Baixo)

#v(10pt)

== 03. LlamaIndex · Framework de RAG (Retrieval-Augmented Generation) com Vector Stores (Persona: Moderna)

#rect(fill: rgb("#f8fafc"), stroke: 0.5pt + rgb("#cbd5e1"), inset: 8pt, radius: 2pt, width: 100%)[
 #grid(
  columns: (1fr, 1fr, 1fr),
  gutter: 6pt,
  [*Substitui:* Anthropic Claude Code / Knowledge Base Built-in],
  [*Economia:* #text(fill: rgb("#00875A"), weight: "bold")[R\$ 18.000/ano]],
  [*Licença:* `MIT`]
 )
]

*1. O Que Faz & Como Funciona:* \
Ingere documentos, cria índices vetoriais e recupera contexto relevante para agentes consultarem bases de conhecimento. SDK Python com suporte a loaders de múltiplos formatos (PDF, Docx, HTML) e integração com vector stores (Pinecone, Weaviate, Chroma).

```bash
pip install llama-index && from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader
```

*2. Racional da Escolha & Veredito Técnico:* \
Indexação automática de PDFs, markdowns e bases de dados com chunking inteligente e reranking para recuperação precisa de contexto. \
#text(style: "italic", fill: rgb("#334155"))[*Veredito:* Padrão de fato para RAG, usado por startups de AI e enterprises para document QA e knowledge discovery.]

*3. Requisitos de Infraestrutura & White-Label:* \
- RAM Mínima: `2 GB RAM` | CPU: `1 vCPU` | Docker: `oficial`
- Customização UI: Customização total de prompts de retrieval e parsing de documentos. (Esforço: Baixo)

#v(10pt)

== 04. Flowise · Construtor Visual Drag-and-Drop de Workflows de IA (Persona: Leve)

#rect(fill: rgb("#f8fafc"), stroke: 0.5pt + rgb("#cbd5e1"), inset: 8pt, radius: 2pt, width: 100%)[
 #grid(
  columns: (1fr, 1fr, 1fr),
  gutter: 6pt,
  [*Substitui:* Anthropic Claude Code (Visual Agent Builder)],
  [*Economia:* #text(fill: rgb("#00875A"), weight: "bold")[R\$ 14.400/ano]],
  [*Licença:* `Apache-2.0`]
 )
]

*1. O Que Faz & Como Funciona:* \
Cria workflows de IA complexos arrastando nós de modelos, tools e lógica condicional. Node.js e React com execução de workflows em background via Bull Queue.

```bash
npm install -g flowise && flowise start
```

*2. Racional da Escolha & Veredito Técnico:* \
Oferece editor visual parecido com Make/Zapier especialmente otimizado para LLMs, com suporte a Ollama, OpenAI e Anthropic. \
#text(style: "italic", fill: rgb("#334155"))[*Veredito:* Melhor solução visual para prototipagem rápida de agentes complexos com múltiplas integrações.]

*3. Requisitos de Infraestrutura & White-Label:* \
- RAM Mínima: `2 GB RAM` | CPU: `1 vCPU` | Docker: `oficial`
- Customização UI: Workflows completamente customizáveis com suporte a prompts corporativos. (Esforço: Baixo)

#v(10pt)

== 05. AnythingLLM · RAG Platform All-in-One com Chat Interface (Persona: Simples)

#rect(fill: rgb("#f8fafc"), stroke: 0.5pt + rgb("#cbd5e1"), inset: 8pt, radius: 2pt, width: 100%)[
 #grid(
  columns: (1fr, 1fr, 1fr),
  gutter: 6pt,
  [*Substitui:* ChatGPT / Claude Cloud (Knowledge Base)],
  [*Economia:* #text(fill: rgb("#00875A"), weight: "bold")[R\$ 12.000/ano]],
  [*Licença:* `MIT`]
 )
]

*1. O Que Faz & Como Funciona:* \
Cria um sistema de chat que responde perguntas sobre documentos corporativos uploadados. Binário Go estático com SQLite embarcado e embeddings locais via Ollama.

```bash
docker run -d -p 3001:3001 --name anythingllm mintplexlabs/anythingllm:latest
```

*2. Racional da Escolha & Veredito Técnico:* \
Single-binary Go que encapsula Ollama, vector store, chunking e UI de chat em uma solução zero-dependencies. \
#text(style: "italic", fill: rgb("#334155"))[*Veredito:* A forma mais rápida e simples de deployar um knowledge base corporativo sem conhecimento técnico.]

*3. Requisitos de Infraestrutura & White-Label:* \
- RAM Mínima: `4 GB RAM` | CPU: `1 vCPU` | Docker: `oficial`
- Customização UI: White-label completo com logo e cores corporativas. (Esforço: Baixo)

#v(10pt)

#pagebreak()
= Capítulo 4: Pilar 02 · Grupo 2: Infraestrutura de Desenvolvimento, CI/CD & Versionamento

#text(size: 9pt, fill: rgb("#0284c7"), weight: "bold")[Alvo SaaS Substituído: GitHub / GitLab / Claude Code (IDE Integration) / GitHub Actions] \
#text(size: 9pt, fill: rgb("#00875A"), weight: "bold")[Subtotal de Economia do Grupo: R\$ 60.000/ano] \
#text(size: 9pt, style: "italic", fill: rgb("#475569"))[Frente responsável pela gestão de código-fonte distribuído, automação de builds e testes, registro de imagens Docker e orquestração de pipelines de deployment.]

#v(8pt)

== 01. Gitea · Servidor Git Auto-Hospedado Leve com Interface Web (Persona: Completa)

#rect(fill: rgb("#f8fafc"), stroke: 0.5pt + rgb("#cbd5e1"), inset: 8pt, radius: 2pt, width: 100%)[
 #grid(
  columns: (1fr, 1fr, 1fr),
  gutter: 6pt,
  [*Substitui:* GitHub (Team Plan) / GitLab (Premium)],
  [*Economia:* #text(fill: rgb("#00875A"), weight: "bold")[R\$ 24.000/ano (10 usuários)]],
  [*Licença:* `MIT`]
 )
]

*1. O Que Faz & Como Funciona:* \
Fornece servidor Git completo com interface web para gerenciar repositórios e colaboração. Binário Go estático sobre SQLite ou PostgreSQL com suporte a organizações e equipas.

```bash
docker run -d -p 3000:3000 --name gitea gitea/gitea:latest
```

*2. Racional da Escolha & Veredito Técnico:* \
Binário Go ultra-leve que substitui GitHub em 100% dos casos, com suporte a webhooks, integração SSH/HTTPS e pull requests nativas. \
#text(style: "italic", fill: rgb("#334155"))[*Veredito:* GitHub/GitLab on-premises mais simples e rápido de operar em produção, consumindo menos de 100 MB RAM.]

*3. Requisitos de Infraestrutura & White-Label:* \
- RAM Mínima: `2 GB RAM` | CPU: `1 vCPU` | Docker: `oficial`
- Customização UI: Logo corporativa e domínio próprio (ex: `git.empresa.com.br`). (Esforço: Baixo)

#v(10pt)

== 02. Woodpecker CI · Motor de CI/CD Moderno com Suporte a Containers & Kubernetes (Persona: Robusta)

#rect(fill: rgb("#f8fafc"), stroke: 0.5pt + rgb("#cbd5e1"), inset: 8pt, radius: 2pt, width: 100%)[
 #grid(
  columns: (1fr, 1fr, 1fr),
  gutter: 6pt,
  [*Substitui:* GitHub Actions / GitLab CI / Jenkins],
  [*Economia:* #text(fill: rgb("#00875A"), weight: "bold")[R\$ 18.000/ano]],
  [*Licença:* `Apache-2.0`]
 )
]

*1. O Que Faz & Como Funciona:* \
Executa pipelines de build, teste e deploy em containers Docker isolados disparados por push/PR. Go + Docker API com suporte a secretos e variáveis de ambiente criptografadas.

```bash
docker run -d -p 8000:8000 --name woodpecker woodpeckerci/woodpecker-server:latest
```

*2. Racional da Escolha & Veredito Técnico:* \
Alternativa moderna a Jenkins com suporte nativo a Docker, Kubernetes e pipelines YAML declarativas aprovadas no Gitea. \
#text(style: "italic", fill: rgb("#334155"))[*Veredito:* Substituição direta de GitHub Actions com melhor experiência operacional e logs de pipeline.]

*3. Requisitos de Infraestrutura & White-Label:* \
- RAM Mínima: `2 GB RAM` | CPU: `1 vCPU` | Docker: `oficial`
- Customização UI: Pipelines totalmente customizáveis em YAML com suporte a secrets corporativos. (Esforço: Baixo)

#v(10pt)

== 03. MinIO · Object Storage S3-Compatible para Artefatos & Backups (Persona: Moderna)

#rect(fill: rgb("#f8fafc"), stroke: 0.5pt + rgb("#cbd5e1"), inset: 8pt, radius: 2pt, width: 100%)[
 #grid(
  columns: (1fr, 1fr, 1fr),
  gutter: 6pt,
  [*Substitui:* AWS S3 / Google Cloud Storage],
  [*Economia:* #text(fill: rgb("#00875A"), weight: "bold")[R\$ 12.000/ano]],
  [*Licença:* `AGPL-3.0`]
 )
]

*1. O Que Faz & Como Funciona:* \
Fornece armazenamento de objetos escalável com API S3-compatible. Binário Go com suporte a multi-node clustering e replicação.

```bash
docker run -d -p 9000:9000 --name minio minio/minio:latest server /data
```

*2. Racional da Escolha & Veredito Técnico:* \
API 100% compatível com S3 permitindo trocar de fornecedor sem mudança de código, com suporte a replicação geo-distribuída. \
#text(style: "italic", fill: rgb("#334155"))[*Veredito:* S3 local com performance igual ou superior, eliminando vendor lock-in.]

*3. Requisitos de Infraestrutura & White-Label:* \
- RAM Mínima: `1 GB RAM` | CPU: `1 vCPU` | Docker: `oficial`
- Customização UI: Interface web customizável com suporte a SSO OIDC. (Esforço: Baixo)

#v(10pt)

== 04. Docker Registry · Registro Privado de Imagens Docker (Persona: Leve)

#rect(fill: rgb("#f8fafc"), stroke: 0.5pt + rgb("#cbd5e1"), inset: 8pt, radius: 2pt, width: 100%)[
 #grid(
  columns: (1fr, 1fr, 1fr),
  gutter: 6pt,
  [*Substitui:* Docker Hub (Private Repos) / ECR / GCR],
  [*Economia:* #text(fill: rgb("#00875A"), weight: "bold")[R\$ 9.600/ano]],
  [*Licença:* `Apache-2.0`]
 )
]

*1. O Que Faz & Como Funciona:* \
Fornece repositório centralizado de imagens Docker com autenticação básica. Go com armazenamento em filesystem ou object storage S3 (MinIO).

```bash
docker run -d -p 5000:5000 --name registry registry:2
```

*2. Racional da Escolha & Veredito Técnico:* \
Registrador oficial da Docker focado em performance e simplicidade, com suporte a pull/push sobre HTTPS TLS. \
#text(style: "italic", fill: rgb("#334155"))[*Veredito:* Registro Docker leve e confiável para equipes pequenas até médias.]

*3. Requisitos de Infraestrutura & White-Label:* \
- RAM Mínima: `1 GB RAM` | CPU: `1 vCPU` | Docker: `oficial`
- Customização UI: Serviço puro de backend sem UI. (Esforço: Baixo)

#v(10pt)

== 05. Deno · Runtime JavaScript/TypeScript Moderno com Permissões Granulares (Persona: Simples)

#rect(fill: rgb("#f8fafc"), stroke: 0.5pt + rgb("#cbd5e1"), inset: 8pt, radius: 2pt, width: 100%)[
 #grid(
  columns: (1fr, 1fr, 1fr),
  gutter: 6pt,
  [*Substitui:* Node.js (elimina dependência de npm/package.json)],
  [*Economia:* #text(fill: rgb("#00875A"), weight: "bold")[R\$ 6.000/ano]],
  [*Licença:* `MIT`]
 )
]

*1. O Que Faz & Como Funciona:* \
Executa scripts TypeScript/JavaScript com controle fino de permissões (arquivo, rede, variáveis de ambiente). Binário Rust estático com bundler integrado e cache imutável via URLs.

```bash
deno run --allow-net https://deno.land/std/examples/echo_server.ts
```

*2. Racional da Escolha & Veredito Técnico:* \
Runtime TypeScript nativo com URLs imutáveis, sem arquivo package.json e permissões explícitas, reduzindo risco de supply chain. \
#text(style: "italic", fill: rgb("#334155"))[*Veredito:* Excelente para scripts de automação corporativa sem risco de supply chain (sem node\_modules).]

*3. Requisitos de Infraestrutura & White-Label:* \
- RAM Mínima: `256 MB RAM` | CPU: `1 vCPU` | Docker: `oficial`
- Customização UI: Scripts totalmente customizáveis em TypeScript puro. (Esforço: Baixo)

#v(10pt)

#pagebreak()
= Capítulo 5: Pilar 03 · Grupo 3: Observabilidade, Monitoramento & Suporte

#text(size: 9pt, fill: rgb("#0284c7"), weight: "bold")[Alvo SaaS Substituído: DataDog / New Relic / Sentry (Error Tracking) / PagerDuty] \
#text(size: 9pt, fill: rgb("#00875A"), weight: "bold")[Subtotal de Economia do Grupo: R\$ 48.000/ano] \
#text(size: 9pt, style: "italic", fill: rgb("#475569"))[Frente responsável pela coleta de métricas, logs e traces distribuídos, alertas proativos e análise de performance em tempo real.]

#v(8pt)

== 01. Prometheus · Time-Series Database & Scraper de Métricas (Persona: Completa)

#rect(fill: rgb("#f8fafc"), stroke: 0.5pt + rgb("#cbd5e1"), inset: 8pt, radius: 2pt, width: 100%)[
 #grid(
  columns: (1fr, 1fr, 1fr),
  gutter: 6pt,
  [*Substitui:* DataDog / New Relic (Infrastructure Monitoring)],
  [*Economia:* #text(fill: rgb("#00875A"), weight: "bold")[R\$ 24.000/ano]],
  [*Licença:* `Apache-2.0`]
 )
]

*1. O Que Faz & Como Funciona:* \
Scrape de endpoints `/metrics` em intervalos regulares, armazenando séries temporais e fornecendo SQL-like PromQL. Binário Go estático com armazenamento em disco local e compressão de dados.

```bash
docker run -d -p 9090:9090 --name prometheus prom/prometheus
```

*2. Racional da Escolha & Veredito Técnico:* \
Padrão de fato do CNCF para observabilidade em Kubernetes e containers, com pull-based scraping nativo. \
#text(style: "italic", fill: rgb("#334155"))[*Veredito:* Substituição completa de DataDog/New Relic para equipes que não precisam de observabilidade SaaS.]

*3. Requisitos de Infraestrutura & White-Label:* \
- RAM Mínima: `2 GB RAM` | CPU: `1 vCPU` | Docker: `oficial`
- Customização UI: Totalmente customizável via YAML e PromQL. (Esforço: Baixo)

#v(10pt)

== 02. Grafana · Plataforma de Dashboards & Alertas para Observabilidade (Persona: Robusta)

#rect(fill: rgb("#f8fafc"), stroke: 0.5pt + rgb("#cbd5e1"), inset: 8pt, radius: 2pt, width: 100%)[
 #grid(
  columns: (1fr, 1fr, 1fr),
  gutter: 6pt,
  [*Substitui:* DataDog / New Relic (Dashboarding)],
  [*Economia:* #text(fill: rgb("#00875A"), weight: "bold")[R\$ 18.000/ano]],
  [*Licença:* `AGPL-3.0 (Enterprise: Proprietary)`]
 )
]

*1. O Que Faz & Como Funciona:* \
Constrói dashboards interativos consumindo dados de Prometheus, Loki e outras fontes. Go backend com React frontend e suporte a plugins customizados.

```bash
docker run -d -p 3000:3000 --name grafana grafana/grafana
```

*2. Racional da Escolha & Veredito Técnico:* \
Dashboard builder visual mais poderoso, suportando Prometheus, Loki, Elasticsearch e 100+ data sources. \
#text(style: "italic", fill: rgb("#334155"))[*Veredito:* Melhor dashboard open source do mercado, com UX comparável a SaaS premium.]

*3. Requisitos de Infraestrutura & White-Label:* \
- RAM Mínima: `1 GB RAM` | CPU: `1 vCPU` | Docker: `oficial`
- Customização UI: White-label completo com logo e domínio corporativo. (Esforço: Baixo)

#v(10pt)

== 03. Loki · Log Aggregation System com Índices Otimizados (Persona: Moderna)

#rect(fill: rgb("#f8fafc"), stroke: 0.5pt + rgb("#cbd5e1"), inset: 8pt, radius: 2pt, width: 100%)[
 #grid(
  columns: (1fr, 1fr, 1fr),
  gutter: 6pt,
  [*Substitui:* DataDog / Splunk / Elasticsearch (Logging)],
  [*Economia:* #text(fill: rgb("#00875A"), weight: "bold")[R\$ 14.400/ano]],
  [*Licença:* `AGPL-3.0`]
 )
]

*1. O Que Faz & Como Funciona:* \
Ingere logs de containers, estrutura-os por labels e fornece buscas rápidas com LogQL. Go com armazenamento em S3 (MinIO) e índices em memória.

```bash
docker run -d -p 3100:3100 --name loki grafana/loki
```

*2. Racional da Escolha & Veredito Técnico:* \
Alternativa leve ao Elasticsearch reduzindo em 10x o storage necessário via índices inteligentes baseados em labels. \
#text(style: "italic", fill: rgb("#334155"))[*Veredito:* Alternativa superior ao ELK stack para organismos não-gigantes, com 90% menos storage.]

*3. Requisitos de Infraestrutura & White-Label:* \
- RAM Mínima: `2 GB RAM` | CPU: `1 vCPU` | Docker: `oficial`
- Customização UI: Totalmente customizável via YAML. (Esforço: Baixo)

#v(10pt)

== 04. Alertmanager · Gerenciador de Alertas & Deduplicação (Persona: Leve)

#rect(fill: rgb("#f8fafc"), stroke: 0.5pt + rgb("#cbd5e1"), inset: 8pt, radius: 2pt, width: 100%)[
 #grid(
  columns: (1fr, 1fr, 1fr),
  gutter: 6pt,
  [*Substitui:* PagerDuty (Alert Routing)],
  [*Economia:* #text(fill: rgb("#00875A"), weight: "bold")[R\$ 12.000/ano]],
  [*Licença:* `Apache-2.0`]
 )
]

*1. O Que Faz & Como Funciona:* \
Agrupa alertas similares, deduplica e envia notificações via múltiplos canais. Go com armazenamento em memória e replicação opcional.

```bash
docker run -d -p 9093:9093 --name alertmanager prom/alertmanager
```

*2. Racional da Escolha & Veredito Técnico:* \
Complemento oficial ao Prometheus com suporte a grouping, silenciamento e escalonamento de alertas. \
#text(style: "italic", fill: rgb("#334155"))[*Veredito:* Essential companion ao Prometheus para evitar alertas repetitivos.]

*3. Requisitos de Infraestrutura & White-Label:* \
- RAM Mínima: `512 MB RAM` | CPU: `1 vCPU` | Docker: `oficial`
- Customização UI: Templates de notificação customizáveis. (Esforço: Baixo)

#v(10pt)

== 05. OpenTelemetry Collector · Coleta & Processamento Agnóstico de Traces, Métricas & Logs (Persona: Simples)

#rect(fill: rgb("#f8fafc"), stroke: 0.5pt + rgb("#cbd5e1"), inset: 8pt, radius: 2pt, width: 100%)[
 #grid(
  columns: (1fr, 1fr, 1fr),
  gutter: 6pt,
  [*Substitui:* Datadog / New Relic / Sentry (Tracing & Collection)],
  [*Economia:* #text(fill: rgb("#00875A"), weight: "bold")[R\$ 9.600/ano]],
  [*Licença:* `Apache-2.0`]
 )
]

*1. O Que Faz & Como Funciona:* \
Coleta traces, métricas e logs em formato OpenTelemetry e exporta para múltiplos backends. Go com suporte a OTLP protocol e receiversexportadores plugáveis.

```bash
docker run -d -p 4317:4317 -p 4318:4318 --name otel-collector otel/opentelemetry-collector
```

*2. Racional da Escolha & Veredito Técnico:* \
Padrão CNCF agnóstico de backend, permitindo enviar dados para Prometheus, Loki, Jaeger ou qualquer sistema sem reescrever código. \
#text(style: "italic", fill: rgb("#334155"))[*Veredito:* Agnóstico de backend ideal para evitar lock-in em uma solução comercial.]

*3. Requisitos de Infraestrutura & White-Label:* \
- RAM Mínima: `1 GB RAM` | CPU: `1 vCPU` | Docker: `oficial`
- Customização UI: Totalmente customizável via YAML. (Esforço: Baixo)

#v(10pt)


#pagebreak()
= Capítulo 6: Camada de Cola, SSO Federado & Blueprints n8n

== Arquitetura de Interconexão sem Silos de Dados
- *Autenticação Única:* Keycloak / Authentik (OpenID Connect / SAML) unificando o login de engenheiros e agentes de IA no Gitea, Woodpecker, Grafana, Ollama Web UI e Flowise.
- *Barramento Assíncrono:* n8n Community Edition atuando como orquestrador central de eventos assíncronos (Build concluído no Woodpecker -> Modelo treinado no Ollama -> Teste executado em LlamaIndex -> Alerta enviado no Slack via Alertmanager).
- *Reverse Proxy & TLS:* Traefik Proxy v3 com terminação TLS automática via Let's Encrypt e roteamento por subdomínios corporativos (git.empresa.com.br, ci.empresa.com.br, llm.empresa.com.br, obs.empresa.com.br, sso.empresa.com.br).

== Fluxo de Integração Operacional
1. Commit de Código: Engenheiro faz push no Gitea;
2. Trigger CI/CD: Webhook dispara no Woodpecker que executa testes e builds;
3. Artefatos: Build artifacts são armazenados no MinIO e imagem Docker no Registry privado;
4. Deploy de Agentes: n8n dispara o deploy dos novos agentes LLM via Flowise/LangChain;
5. Testes de Agente: LangChain executa testes de agente consultando Ollama local e LlamaIndex;
6. Observabilidade: Prometheus coleta métricas de latência do agente, Loki ingere logs de erro, Alertmanager notifica no Slack;
7. Feedback Loop: Agentes consultam Grafana para decidir se retrainam ou escalam.

#pagebreak()
= Capítulo 7: Manual de Engenharia de Infraestrutura & Deploy All-in-One

- *Segurança de Rede:* A infraestrutura opera sobre uma rede bridge isolada do Docker (`ai\_ecosystem\_net`). Apenas o reverse proxy Traefik expõe as portas públicas 80 (HTTP com redirect) e 443 (HTTPS TLS automático via ACME/Let's Encrypt). Todas as ferramentas (Ollama, LangChain, Flowise, Gitea, Woodpecker, Prometheus, Grafana, Loki e Keycloak) comunicam-se exclusivamente pela rede interna através de seus nomes DNS de serviço, eliminando vetores de ataque externos.
- *Perfil de VPS Recomendado:* `8 vCPU / 16 GB RAM`

#v(6pt)
== Especificação da VPS Ideal (e Por Que Desta Configuração)
#text(size: 8.5pt, style: "italic", fill: rgb("#334155"))[]

#v(6pt)
#table(
 columns: (1.5fr, 0.7fr, 0.7fr, 2.8fr),
 fill: (x, y) => if y == 0 { rgb("#f1f5f9") } else { none },
 stroke: 0.5pt + rgb("#cbd5e1"),
 inset: 4pt,
 [*Serviço / Módulo*], [*vCPU*], [*RAM*], [*Motivo Técnico & Gargalo*],
 
)

#v(8pt)
== Manifesto docker-compose.yml de Produção
```yaml
version: '3.8'

networks:
  ai_ecosystem_net:
    driver: bridge

services:
  # 1. Reverse Proxy & TLS Automático
  traefik:
    image: traefik:v3.0
    command:
      - '--providers.docker=true'
      - '--entrypoints.web.address=:80'
      - '--entrypoints.websecure.address=:443'
      - '--certificatesresolvers.myresolver.acme.tlschallenge=true'
      - '--certificatesresolvers.myresolver.acme.email=admin@empresa.com'
      - '--certificatesresolvers.myresolver.acme.storage=/letsencrypt/acme.json'
    ports:
      - '80:80'
      - '443:443'
    volumes:
      - '/var/run/docker.sock:/var/run/docker.sock:ro'
      - './letsencrypt:/letsencrypt'
    networks:
      - ai_ecosystem_net

  # 2. Ollama LLM Server
  ollama:
    image: ollama/ollama:latest
    environment:
      - OLLAMA_HOST=0.0.0.0:11434
    volumes:
      - ollama_data:/root/.ollama
    networks:
      - ai_ecosystem_net

  # 3. Flowise AI Builder
  flowise:
    image: flowiseai/flowise:latest
    ports:
      - '3001:3001'
    volumes:
      - flowise_data:/root/.flowise
    labels:
      - 'traefik.enable=true'
      - 'traefik.http.routers.flowise.rule=Host(`ai-builder.empresa.com.br`)'
    networks:
      - ai_ecosystem_net

  # 4. Gitea Repository
  gitea:
    image: gitea/gitea:latest
    labels:
      - 'traefik.enable=true'
      - 'traefik.http.routers.gitea.rule=Host(`git.empresa.com.br`)'
    volumes:
      - gitea_data:/data
    networks:
      - ai_ecosystem_net

  # 5. Woodpecker CI
  woodpecker-server:
    image: woodpeckerci/woodpecker-server:latest
    labels:
      - 'traefik.enable=true'
      - 'traefik.http.routers.woodpecker.rule=Host(`ci.empresa.com.br`)'
    networks:
      - ai_ecosystem_net

  # 6. Prometheus Metrics
  prometheus:
    image: prom/prometheus:latest
    ports:
      - '9090:9090'
    volumes:
      - prometheus_data:/prometheus
    networks:
      - ai_ecosystem_net

  # 7. Grafana Dashboards
  grafana:
    image: grafana/grafana:latest
    labels:
      - 'traefik.enable=true'
      - 'traefik.http.routers.grafana.rule=Host(`monitoring.empresa.com.br`)'
    volumes:
      - grafana_data:/var/lib/grafana
    networks:
      - ai_ecosystem_net

volumes:
  ollama_data:
  flowise_data:
  gitea_data:
  prometheus_data:
  grafana_data:
```

#pagebreak()
= Capítulo 8: Protocolos de Modularidade & Hot-Swap (Princípio do Lego)

- *Filosofia Desacoplada:* A arquitetura opera sob o princípio de 'Tomadas e Aparelhos Independentes'. Nenhuma ferramenta fica grudada ou dependente da outra com código travado. Imagine uma régua de tomadas: Ollama (LLM) e LangChain (Framework) funcionam perfeitamente mesmo se você desligar Flowise (Builder). Se quiser trocar Ollama por outro LLM, basta desconectar e plugar o novo. Nada quebra.

== Hot-Swap em Produção
1. Suba a Nova Ferramenta em Paralelo: Inicie a nova solução em um endereço temporário (ex: `novo-llm.empresa.com.br`) mantendo a antiga funcionando;
2. Transfira a Conexão em Flowise/LangChain: No painel visual, mude o nó de conexão para apontar para a nova ferramenta;
3. Importe Configurações: Faça o download dos workflows/modelos da ferramenta antiga e importe na nova;
4. Mude o Endereço Oficial: Altere a rota para que `llm.empresa.com.br` aponte para a nova ferramenta;
5. Desligue a Antiga com Segurança: Pare o serviço antigo digitando `docker compose stop <servico\_antigo>`. Os seus agentes nem notarão a troca!

#pagebreak()
= Capítulo 9: Roteiro Prático de Migração de Dados Históricos

== 1. Migração de Agentes de Claude Code para Stack Aberto
- *O que migrar:* Configurações de agentes, prompts base, MCP servers registrados, histórico de conversas e modelos treinados.
- *Cuidados:* Preserve a lógica de fallback para garantir que agentes funcionem tanto localmente quanto com API remota.

== 2. Migração de Knowledge Bases (RAG) para LlamaIndex
- *O que migrar:* Documentações, PDFs treinados, embeddings vetoriais e configurações de retrieval.
- *Cuidados:* Teste a qualidade de retrieval com queries conhecidas antes de descomissionar a base antiga.

== 3. Migração de Pipelines CI/CD de GitHub Actions para Woodpecker
- *O que migrar:* Workflows de teste, build e deploy, secrets e variáveis de ambiente.
- *Cuidados:* Mantenha GitHub Actions ativo por uma semana em paralelo para contingência.



#pagebreak()
= Capítulo 10: Governança Corporativa, Backup 3-2-1 & LGPD

- *Política 3-2-1:* A política de proteção de dados opera na regra de ouro 3-2-1: (3) cópias de dados em (2) tipos de mídias diferentes, com (1) cópia externa criptografada em nuvem fria (Wasabi / AWS S3).

== Script de Backup Diário Criptografado
```bash
#!/bin/bash
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
BACKUP_DIR="/opt/backups/$TIMESTAMP"
mkdir -p $BACKUP_DIR

# 1. Dump de todos os bancos (Keycloak, Gitea, Woodpecker)
docker exec postgres pg_dumpall -U postgres | gzip > $BACKUP_DIR/db_cluster.sql.gz

# 2. Compactação dos modelos Ollama e configurações
tar -czf $BACKUP_DIR/ollama_models.tar.gz -C /var/lib/docker/volumes ollama_data/_data

# 3. Criptografia AES-256
gpg --batch --yes --passphrase "SenhaChaveMestreSegura2026" -c $BACKUP_DIR/db_cluster.sql.gz

# 4. Envio para Storage Externo via rclone
rclone copy $BACKUP_DIR remote-s3:backups-empresa/$TIMESTAMP/

# 5. Limpeza de backups locais com mais de 7 dias
find /opt/backups/* -mtime +7 -exec rm -rf {} \;
echo "Backup soberano concluído!"

```

#pagebreak()
= Capítulo 11: Cronograma de Implantação em 30 Dias & Monitoramento

== Semana 1 (Dias 1 a 7) · Infraestrutura & Instalação do Stack
- *Atividades:* Contratação da VPS, configuração de DNS wildcard, execução do docker-compose.yml e ativação de certificados SSL automáticos via Traefik.
- *Marco de Entrega:* None

== Semana 2 (Dias 8 a 14) · Migração de Modelos LLM & Bases de Conhecimento
- *Atividades:* Download de modelos Ollama (Mistral 7B, Llama 2), indexação de documentação corporativa em LlamaIndex e teste de inference local.
- *Marco de Entrega:* None

== Semana 3 (Dias 15 a 21) · Migração de Agentes & Configuração de CI/CD
- *Atividades:* Migração de agentes de Claude Code, configuração de pipelines Woodpecker e workshop de capacitação das equipes de desenvolvimento.
- *Marco de Entrega:* None

== Semana 4 (Dias 22 a 30) · Virada de Chave Definitiva & Descomissionamento
- *Atividades:* Redirecionamento de endpoints de API para stack local, ativação de observabilidade integrada (Prometheus + Grafana) e cancelamento de faturas Anthropic.
- *Marco de Entrega:* None


