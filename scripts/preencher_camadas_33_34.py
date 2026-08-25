# -*- coding: utf-8 -*-
"""
Completa as Fichas Técnicas das Camadas 33 e 34 no padrão Dossiê Executivo.
"""
import os
import sys
from bs4 import BeautifulSoup

def console_utf8():
    if sys.platform == "win32":
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")

console_utf8()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = os.path.join(BASE_DIR, "output", "listas-open-source")

# FICHAS DA CAMADA 33 (10 Pilares AIDD)
FICHAS_33 = [
    {
        "rank": "01", "titulo": "Repomix · Gitingest · RTK Caching", "subtitulo": "Economia de Tokens & Compactação",
        "senior_lbl": "Júnior / Iniciante", "senior_cor": "green",
        "substitui": "Dumps manuais de código e janelas de contexto infladas",
        "economia": "-80% a -90% no consumo de tokens de contexto",
        "licenca": "MIT / Apache-2.0", "categoria": "Context Compression",
        "o_que_faz": "Empacota repositórios inteiros em XML/Markdown ultra-compactos com árvore de diretórios e filtros de segurança.",
        "como_funciona": "Aplica token counting exato e caching semântico antes do envio para APIs LLM.",
        "codigo": "npx repomix --style xml --output context.xml",
        "infra": "Binário local / 0 MB RAM adicional", "veredito": "Indispensável para qualquer esteira de AIDD.",
        "repo_url": "https://github.com/yamadashy/repomix", "repo_txt": "github.com/yamadashy/repomix",
        "passo_1": "Execute repomix na raiz do repositório.", "passo_2": "Envie context.xml para a IA.", "passo_3": "Receba respostas sem alucinação de contexto."
    },
    {
        "rank": "02", "titulo": "Spec-Kit · Fable Method", "subtitulo": "Engenharia de Especificações & Contratos",
        "senior_lbl": "Pleno / Backend", "senior_cor": "gold",
        "substitui": "Desenvolvimento desgovernado e código sem critério de aceite",
        "economia": "Economiza semanas de retrabalho em arquitetura",
        "licenca": "MIT", "categoria": "Spec-Driven Development",
        "o_que_faz": "Framework que impõe a criação de SPEC.md, PLAN.md e TASKS.md antes de qualquer geração de código.",
        "como_funciona": "Garante que contratos de tipos e testes sejam definidos e auditados antes da implementação.",
        "codigo": "# spec-kit: SPEC.md -> PLAN.md -> TASKS.md -> IMPLEMENTAÇÃO",
        "infra": "0 MB RAM / Metodologia pura", "veredito": "Garante 100% de previsibilidade nas entregas do agente.",
        "repo_url": "https://github.com/github/spec-kit", "repo_txt": "github.com/github/spec-kit",
        "passo_1": "Crie o SPEC.md com contratos e regras.", "passo_2": "Gere o PLAN.md arquitetural.", "passo_3": "Execute as TASKS.md com validação contínua."
    },
    {
        "rank": "03", "titulo": "Aider CLI · Cline · Roo-Code", "subtitulo": "Codificação Autônoma & Git Pair Programming",
        "senior_lbl": "Júnior / Iniciante", "senior_cor": "green",
        "substitui": "Assinatura do Cursor ($ 20/mês) e GitHub Copilot",
        "economia": "-$ 240 / ano por desenvolvedor em licenças fechadas",
        "licenca": "Apache-2.0", "categoria": "AI Coding Harness",
        "o_que_faz": "Pair programmer de terminal que edita código local e commita com mensagens semânticas no Git.",
        "como_funciona": "Usa grafos de dependência e AST para enviar apenas as partes relevantes do código.",
        "codigo": "aider --model claude-3-5-sonnet --auto-commits",
        "infra": "Python 3.10+ / Execução local", "veredito": "O melhor copiloto de terminal com controle total de diffs.",
        "repo_url": "https://github.com/paul-gauthier/aider", "repo_txt": "github.com/paul-gauthier/aider",
        "passo_1": "Instale via pipx install aider-chat.", "passo_2": "Abra no diretório do projeto e dê instruções.", "passo_3": "Aceite os diffs diretamente no Git."
    },
    {
        "rank": "04", "titulo": "CrewAI · LangGraph · OpenHands", "subtitulo": "Arquitetura Multi-Agente & Squads",
        "senior_lbl": "Sênior / Especialista", "senior_cor": "flag",
        "substitui": "Prompts monolíticos lentos e frágeis",
        "economia": "Reduz erros de contexto em 80% em tarefas complexas",
        "licenca": "MIT", "categoria": "Multi-Agent Framework",
        "o_que_faz": "Orquestra múltiplos agentes especializados (pesquisador, coder, auditor, revisor) com papéis claros.",
        "como_funciona": "Executa máquinas de estados cíclicas e delegação estruturada com checkpoints.",
        "codigo": "from crewai import Agent, Crew, Task, Process",
        "infra": "1 vCPU · 512 MB RAM · Python", "veredito": "A base para construir esteiras industriais de IA.",
        "repo_url": "https://github.com/crewAIInc/crewAI", "repo_txt": "github.com/crewAIInc/crewAI",
        "passo_1": "Defina os papéis de cada agente.", "passo_2": "Configure os canais de comunicação.", "passo_3": "Execute a esteira de forma autônoma."
    },
    {
        "rank": "05", "titulo": "Qdrant · FastEmbed · Tree-sitter", "subtitulo": "RAG de Código & Indexação Vetorial",
        "senior_lbl": "Pleno / Backend", "senior_cor": "gold",
        "substitui": "Pinecone ($ 70+/mês) e buscas cegas em texto",
        "economia": "-$ 840 / ano em banco vetorial fechado",
        "licenca": "Apache-2.0", "categoria": "Vector Search & AST",
        "o_que_faz": "Banco vetorial ultrarrápido em Rust para busca semântica sobre bases de código e documentações.",
        "como_funciona": "Indexa símbolos e AST via Tree-sitter e realiza busca de similaridade em memória.",
        "codigo": "docker run -p 6333:6333 qdrant/qdrant",
        "infra": "512 MB RAM · Docker em Rust", "veredito": "Líder absoluto em eficiência e velocidade para busca vetorial.",
        "repo_url": "https://github.com/qdrant/qdrant", "repo_txt": "github.com/qdrant/qdrant",
        "passo_1": "Suba o container Qdrant via Docker.", "passo_2": "Indexe os embeddings de código.", "passo_3": "Consulte contexto semântico em milissegundos."
    },
    {
        "rank": "06", "titulo": "Z3 Prover · Ragas · Guardrails AI", "subtitulo": "Qualidade Formal, Evals & Gates Mecânicos",
        "senior_lbl": "Sênior / Especialista", "senior_cor": "flag",
        "substitui": "Validações manuais subjetivas e testes cegos",
        "economia": "Elimina 100% de bugs em regras críticas de negócio",
        "licenca": "MIT / Apache-2.0", "categoria": "Formal Verification & Evals",
        "o_que_faz": "Provador de teoremas e motor de avaliação contínua para validar invariantes e precisão de LLMs.",
        "como_funciona": "Transforma regras de negócio em restrições lógicas e verifica satisfatibilidade matematicamente.",
        "codigo": "from z3 import *; s = Solver(); s.check()",
        "infra": "Biblioteca leve em C++/Python", "veredito": "O padrão ouro para garantia matemática de ausência de falhas.",
        "repo_url": "https://github.com/Z3Prover/z3", "repo_txt": "github.com/Z3Prover/z3",
        "passo_1": "Modele os invariantes no Z3.", "passo_2": "Adicione na esteira de pre-commit.", "passo_3": "Bloqueie deploys caso haja violação de contrato."
    },
    {
        "rank": "07", "titulo": "Langfuse · PostHog · VictoriaMetrics", "subtitulo": "Observabilidade, Telemetria & FinOps",
        "senior_lbl": "Pleno / Backend", "senior_cor": "gold",
        "substitui": "Datadog / LangSmith ($ 400+/mês)",
        "economia": "-$ 4.800 / ano em ferramentas proprietárias de APM",
        "licenca": "MIT / Apache-2.0", "categoria": "LLM Observability",
        "o_que_faz": "Rastreia traces de agentes, latência por modelo, consumo de tokens e custos de API em tempo real.",
        "como_funciona": "Recebe spans via OpenTelemetry e armazena métricas de execução estruturadas.",
        "codigo": "docker compose up -d langfuse-server",
        "infra": "1 vCPU · 1 GB RAM · Docker", "veredito": "Visibilidade total sobre o custo e comportamento de cada agente.",
        "repo_url": "https://github.com/langfuse/langfuse", "repo_txt": "github.com/langfuse/langfuse",
        "passo_1": "Suba o servidor Langfuse local.", "passo_2": "Injete a chave de telemetria no agente.", "passo_3": "Acompanhe traces e faturas em tempo real."
    },
    {
        "rank": "08", "titulo": "vLLM · SGLang · Unsloth", "subtitulo": "Inferência Local de Alto Throughput & Fine-Tuning",
        "senior_lbl": "Sênior / Especialista", "senior_cor": "flag",
        "substitui": "Endpoints caros da OpenAI/Anthropic em volume alto",
        "economia": "-70% a -90% em custos de inferência em massa",
        "licenca": "Apache-2.0", "categoria": "High-Throughput Inference",
        "o_que_faz": "Motor de inferência de altíssimo rendimento com PagedAttention e fine-tuning acelerado 5x mais rápido.",
        "como_funciona": "Otimiza alocação de memória na GPU e executa batches contínuos sem desperdício de VRAM.",
        "codigo": "vllm serve Qwen/Qwen2.5-Coder-32B-Instruct --port 8000",
        "infra": "1x GPU NVIDIA (RTX 4090 ou A100/H100)", "veredito": "A única forma de operar IA em escala sem pagar pedágio de nuvem.",
        "repo_url": "https://github.com/vllm-project/vllm", "repo_txt": "github.com/vllm-project/vllm",
        "passo_1": "Baixe o modelo aberto quantizado.", "passo_2": "Suba o servidor vLLM compatível com OpenAI API.", "passo_3": "Aponte seus agentes para o endpoint local."
    },
    {
        "rank": "09", "titulo": "Penpot · ComfyUI · TRELLIS 3D", "subtitulo": "Design System, UI & Mídia Generativa",
        "senior_lbl": "Pleno / Backend", "senior_cor": "gold",
        "substitui": "Figma Professional ($ 15/user/mês) e Midjourney",
        "economia": "-$ 1.800 / ano para equipes de design e produto",
        "licenca": "MPLv2 / GPL-3.0", "categoria": "Design & Generative Media",
        "o_que_faz": "Suíte aberta de prototipagem baseada em SVG/CSS flexbox e pipelines generativos de imagens e 3D.",
        "como_funciona": "Arquitetura web nativa com compatibilidade direta com tokens de frontend.",
        "codigo": "docker compose -f docker-compose.yaml up -d",
        "infra": "2 vCPU · 2 GB RAM · Docker", "veredito": "A alternativa definitiva e colaborativa ao monopólio do Figma.",
        "repo_url": "https://github.com/penpot/penpot", "repo_txt": "github.com/penpot/penpot",
        "passo_1": "Acesse a interface self-hosted do Penpot.", "passo_2": "Desenhe interfaces usando tokens CSS reais.", "passo_3": "Exporte código pronto diretamente para o frontend."
    },
    {
        "rank": "10", "titulo": "Playwright MCP · Puppeteer", "subtitulo": "Testes de Interface (E2E) & Personas de Usuário",
        "senior_lbl": "Pleno / Backend", "senior_cor": "gold",
        "substitui": "Cypress Cloud ($ 200+/mês) e testes manuais de UI",
        "economia": "-$ 2.400 / ano em esteiras de testes E2E fechadas",
        "licenca": "Apache-2.0", "categoria": "Headless Browser Automation",
        "o_que_faz": "Automação de navegador para execução de testes ponta a ponta, screenshots e validação de acessibilidade.",
        "como_funciona": "Controla Chromium, Firefox e WebKit via protocolo DevTools de forma determinística.",
        "codigo": "npx playwright test --headed",
        "infra": "Node.js 18+ · Headless Browser", "veredito": "Essencial para agentes validarem a interface gerada de forma visual.",
        "repo_url": "https://github.com/microsoft/playwright", "repo_txt": "github.com/microsoft/playwright",
        "passo_1": "Instale o Playwright via npm init playwright@latest.", "passo_2": "Gere testes gravando as ações do usuário.", "passo_3": "Integre na esteira de CI/CD para validação automática."
    }
]

# FICHAS DA CAMADA 34 (10 Categorias TCO & ROI)
FICHAS_34 = [
    {
        "rank": "01", "titulo": "Chatwoot · Evolution API", "subtitulo": "Atendimento Multicanal & WhatsApp",
        "senior_lbl": "Pleno / Backend", "senior_cor": "gold",
        "substitui": "Zendesk / Blip / Intercom (R$ 72.000 / ano)",
        "economia": "R$ 70.200 / ano de economia líquida (97,5% ROI)",
        "licenca": "AGPLv3 / MIT", "categoria": "Omnichannel Support",
        "o_que_faz": "Central unificada de atendimento para WhatsApp, Live Chat, E-mail e Instagram sem cobrança por atendente.",
        "como_funciona": "Conecta via webhook com Evolution API e PostgreSQL com suporte a múltiplos operadores simultâneos.",
        "codigo": "docker compose up -d chatwoot evolution-api",
        "infra": "1 VPS (4 vCPUs · 4 GB RAM) · R$ 150/mês", "veredito": "Elimina a fatura mais cara do setor de suporte.",
        "repo_url": "https://github.com/chatwoot/chatwoot", "repo_txt": "github.com/chatwoot/chatwoot",
        "passo_1": "Suba o Chatwoot e Evolution API via Docker.", "passo_2": "Conecte o número de WhatsApp via QR Code.", "passo_3": "Cadastre operadores ilimitados sem custo extra."
    },
    {
        "rank": "02", "titulo": "Twenty CRM · EspoCRM", "subtitulo": "CRM de Vendas B2B & Pipeline Comercial",
        "senior_lbl": "Pleno / Backend", "senior_cor": "gold",
        "substitui": "Salesforce Sales Cloud / HubSpot (R$ 120.000 / ano)",
        "economia": "R$ 118.560 / ano de economia líquida (98,8% ROI)",
        "licenca": "Apache-2.0 / AGPLv3", "categoria": "Enterprise CRM",
        "o_que_faz": "CRM moderno com gestão de oportunidades, pipeline Kanban, campos customizados e integração via GraphQL/REST.",
        "como_funciona": "Backend em Node.js com PostgreSQL e frontend React de altíssima performance.",
        "codigo": "docker compose up -d twenty-server",
        "infra": "1 vCPU · 1 GB RAM · R$ 120/mês", "veredito": "O CRM open source mais elegante e rápido do mercado.",
        "repo_url": "https://github.com/twentyhq/twenty", "repo_txt": "github.com/twentyhq/twenty",
        "passo_1": "Instale o Twenty via Docker Compose.", "passo_2": "Importe seus contatos e empresas via CSV.", "passo_3": "Gerencie o pipeline comercial com zero custo por licença."
    },
    {
        "rank": "03", "titulo": "Mautic · Listmonk", "subtitulo": "Automação de Marketing & Envio em Massa",
        "senior_lbl": "Pleno / Backend", "senior_cor": "gold",
        "substitui": "HubSpot / RD Station Pro / Mailchimp (R$ 48.000 / ano)",
        "economia": "R$ 45.600 / ano de economia líquida (95% ROI)",
        "licenca": "GPLv3 / AGPLv3", "categoria": "Marketing Automation",
        "o_que_faz": "Automação completa de fluxos de nutrição de leads, pontuação, formulários e disparo de milhões de e-mails.",
        "como_funciona": "Listmonk dispara 10.000 e-mails/segundo em Go conectado à Amazon SES.",
        "codigo": "docker compose up -d listmonk-app",
        "infra": "1 vCPU · 512 MB RAM · R$ 200/mês (VPS + SES)", "veredito": "Corta em 95% o custo de gestão de listas de e-mails.",
        "repo_url": "https://github.com/knadh/listmonk", "repo_txt": "github.com/knadh/listmonk",
        "passo_1": "Configure o Listmonk integrado com Amazon SES.", "passo_2": "Crie campanhas e templates em Markdown/HTML.", "passo_3": "Dispare e-mails com entregabilidade perfeita por centavos."
    },
    {
        "rank": "04", "titulo": "Metabase · Apache Superset", "subtitulo": "BI, Dashboards & Análise de Dados",
        "senior_lbl": "Pleno / Backend", "senior_cor": "gold",
        "substitui": "Power BI Pro / Tableau Server (R$ 72.000 / ano)",
        "economia": "R$ 69.840 / ano de economia líquida (97% ROI)",
        "licenca": "AGPLv3 / Apache-2.0", "categoria": "Business Intelligence",
        "o_que_faz": "Painéis executivos visuais, consultas SQL em tempo real e relatórios automáticos sem custo por leitor.",
        "como_funciona": "Conecta diretamente ao PostgreSQL, MySQL, ClickHouse ou DuckDB com cache inteligente.",
        "codigo": "docker run -d -p 3000:3000 metabase/metabase",
        "infra": "2 vCPUs · 2 GB RAM · R$ 180/mês", "veredito": "Permite democratizar dados para 100% da empresa sem barreiras.",
        "repo_url": "https://github.com/metabase/metabase", "repo_txt": "github.com/metabase/metabase",
        "passo_1": "Conecte o Metabase ao banco de dados.", "passo_2": "Construa dashboards visuais com filtros interativos.", "passo_3": "Compartilhe links públicos ou envie relatórios diários."
    },
    {
        "rank": "05", "titulo": "Plane Community · Leantime", "subtitulo": "Gestão de Projetos, Sprints & Backlog",
        "senior_lbl": "Júnior / Iniciante", "senior_cor": "green",
        "substitui": "Jira Software Cloud / Asana (R$ 45.000 / ano)",
        "economia": "R$ 43.200 / ano de economia líquida (96% ROI)",
        "licenca": "Apache-2.0 / AGPLv3", "categoria": "Project Management",
        "o_que_faz": "Gestão de issues, ciclos de sprint, roadmaps, módulos e integração com GitHub/GitLab.",
        "como_funciona": "Interface reativa ultra-rápida construída para desenvolvedores modernos.",
        "codigo": "docker compose -f docker-compose.yml up -d",
        "infra": "1 vCPU · 1 GB RAM · R$ 150/mês", "veredito": "Substituto direto do Jira com interface muito mais agradável.",
        "repo_url": "https://github.com/makeplane/plane", "repo_txt": "github.com/makeplane/plane",
        "passo_1": "Instale o Plane via Docker Compose.", "passo_2": "Crie o espaço de trabalho da equipe.", "passo_3": "Organize sprints, backlog e entregas com controle total."
    },
    {
        "rank": "06", "titulo": "Grafana · VictoriaMetrics", "subtitulo": "APM, Logs & Observabilidade de Sistemas",
        "senior_lbl": "Sênior / Especialista", "senior_cor": "flag",
        "substitui": "Datadog / New Relic (R$ 140.000 / ano)",
        "economia": "R$ 135.800 / ano de economia líquida (97% ROI)",
        "licenca": "AGPLv3 / Apache-2.0", "categoria": "APM & Infrastructure",
        "o_que_faz": "Métricas de infraestrutura, logs centralizados e alertas em tempo real sem pegadinhas de faturamento.",
        "como_funciona": "VictoriaMetrics consome 7x menos RAM que Prometheus e comprime métricas em disco de forma incomparável.",
        "codigo": "docker run -d -p 8428:8428 victoriametrics/victoria-metrics",
        "infra": "2 vCPUs · 4 GB RAM · R$ 350/mês", "veredito": "A única solução de observabilidade com custo previsível em escala.",
        "repo_url": "https://github.com/VictoriaMetrics/VictoriaMetrics", "repo_txt": "github.com/VictoriaMetrics/VictoriaMetrics",
        "passo_1": "Suba o VictoriaMetrics e o Grafana.", "passo_2": "Aponte os agentes de métricas dos servidores.", "passo_3": "Monitore infraestrutura e configure alertas automáticos."
    },
    {
        "rank": "07", "titulo": "Rocket.Chat · Mattermost", "subtitulo": "Comunicação Segura & Mensageria Corporativa",
        "senior_lbl": "Pleno / Backend", "senior_cor": "gold",
        "substitui": "Slack Pro ($ 8.75/user/mês) / Microsoft Teams",
        "economia": "R$ 45.600 / ano de economia líquida (95% ROI)",
        "licenca": "MIT / AGPLv3", "categoria": "Team Collaboration",
        "o_que_faz": "Canais de chat, chamadas de áudio/vídeo, compartilhamento de arquivos e histórico ilimitado.",
        "como_funciona": "Criptografia ponta a ponta e total conformidade com a LGPD em servidores locais.",
        "codigo": "docker compose up -d rocketchat",
        "infra": "2 vCPUs · 2 GB RAM · R$ 200/mês", "veredito": "Elimina a perda do histórico de mensagens e garante soberania de dados.",
        "repo_url": "https://github.com/RocketChat/Rocket.Chat", "repo_txt": "github.com/RocketChat/Rocket.Chat",
        "passo_1": "Suba o container do Rocket.Chat.", "passo_2": "Integre com SSO / LDAP corporativo.", "passo_3": "Comunique-se em canais públicos e privados sem limites."
    },
    {
        "rank": "08", "titulo": "DocuSeal · Stirling-PDF", "subtitulo": "Assinatura Eletrônica & Gestão de Documentos",
        "senior_lbl": "Júnior / Iniciante", "senior_cor": "green",
        "substitui": "DocuSign ($ 300/user/ano) / Clicksign",
        "economia": "R$ 23.040 / ano de economia líquida (96% ROI)",
        "licenca": "AGPLv3 / MIT", "categoria": "Digital Signature",
        "o_que_faz": "Assinatura digital com validade jurídica, campos interativos e envio de links de assinatura por e-mail.",
        "como_funciona": "Gera certificados criptográficos SHA-256 e trilha de auditoria para cada documento assinado.",
        "codigo": "docker run -d -p 3000:3000 docuseal/docuseal",
        "infra": "1 vCPU · 512 MB RAM · R$ 80/mês", "veredito": "Assinaturas eletrônicas ilimitadas sem pagar por envelope.",
        "repo_url": "https://github.com/docusealco/docuseal", "repo_txt": "github.com/docusealco/docuseal",
        "passo_1": "Suba o DocuSeal via Docker.", "passo_2": "Faça upload do contrato e posicione os campos.", "passo_3": "Envie para os signatários e baixe o documento assinado."
    },
    {
        "rank": "09", "titulo": "Coolify · Dokku", "subtitulo": "PaaS Self-Hosted & Deploy Automatizado",
        "senior_lbl": "Pleno / Backend", "senior_cor": "gold",
        "substitui": "Heroku / Vercel Pro / Render ($ 250+/mês)",
        "economia": "R$ 15.600 / ano de economia líquida (93% ROI)",
        "licenca": "Apache-2.0 / MIT", "categoria": "Self-Hosted PaaS",
        "o_que_faz": "Deploy automatizado de aplicações, bancos de dados e serviços com certificados SSL automáticos.",
        "como_funciona": "Interface visual moderna que gerencia Docker engines locais ou remotos via SSH.",
        "codigo": "curl -fsSL https://cdn.coollabs.io/coolify/install.sh | bash",
        "infra": "1 VPS bare-metal · R$ 100/mês", "veredito": "Transforma qualquer VPS barata em uma nuvem privada tipo Heroku.",
        "repo_url": "https://github.com/coollabsio/coolify", "repo_txt": "github.com/coollabsio/coolify",
        "passo_1": "Instale o Coolify com uma linha de comando.", "passo_2": "Conecte seu repositório GitHub/GitLab.", "passo_3": "Faça deploy de aplicações com SSL automático."
    },
    {
        "rank": "10", "titulo": "ERPNext · Odoo Community", "subtitulo": "ERP Corporativo, Fiscal & Financeiro",
        "senior_lbl": "Sênior / Especialista", "senior_cor": "flag",
        "substitui": "TOTVS / SAP Business One / NetSuite (R$ 250.000 / ano)",
        "economia": "R$ 242.000 / ano de economia líquida (96,8% ROI)",
        "licenca": "GPLv3 / LGPLv3", "categoria": "Enterprise ERP",
        "o_que_faz": "Gestão financeira completa, emissão fiscal, faturamento, estoque, compras e folha de pagamento.",
        "como_funciona": "Arquitetura Frappe em Python com MariaDB/PostgreSQL altamente customizável.",
        "codigo": "bench init --frappe-branch version-15 frappe-bench",
        "infra": "4 vCPUs · 8 GB RAM · R$ 600/mês", "veredito": "A única alternativa viável para libertar a empresa de ERPs legados.",
        "repo_url": "https://github.com/frappe/erpnext", "repo_txt": "github.com/frappe/erpnext",
        "passo_1": "Instale o Frappe Bench e ERPNext.", "passo_2": "Configure o plano de contas e módulos fiscais.", "passo_3": "Opere a empresa inteira em uma plataforma unificada."
    }
]

def render_cards(fichas_data):
    cards_html = []
    for f in fichas_data:
        c = f"""
      <div class="entry">
        <div class="entry-rank">{f['rank']}</div>
        <div class="entry-body">
          
          <!-- CABEÇALHO & BADGES -->
          <div class="entry-top">
            <h3>{f['titulo']} · {f['subtitulo']}</h3>
            <span class="senior-badge {f['senior_cor']}">👨‍💻 Nível: {f['senior_lbl']}</span>
            <span class="killer-badge">Substitui: {f['substitui']}</span>
            <span class="econ-badge">Economia: {f['economia']}</span>
            <span class="lic-badge">{f['licenca']}</span>
            <span class="kind">{f['categoria']}</span>
          </div>

          <!-- SEÇÃO 1: O QUE FAZ & COMO FUNCIONA -->
          <div class="entry-section">
            <span class="label">1. O Que Faz &amp; Como Funciona</span>
            <p>{f['o_que_faz']}</p>
            <p>{f['como_funciona']}</p>
            <div class="code-box">
              <pre><code>{f['codigo']}</code></pre>
              <button class="copy-btn" onclick="navigator.clipboard.writeText(this.previousElementSibling.textContent.trim());this.textContent='Copiado!';setTimeout(()=>this.textContent='Copiar',1500)">Copiar</button>
            </div>
          </div>

          <!-- SEÇÃO 2: ANÁLISE ECONÔMICA & SUBSTITUIÇÃO DE SAAS -->
          <div class="entry-section">
            <span class="label">2. Análise Econômica &amp; Substituição de Soluções Proprietárias</span>
            <div class="econ-grid">
              <div class="econ-card killer">
                <span class="econ-lbl">💸 Produtos Proprietários Substituídos</span>
                <div class="econ-val">{f['substitui']}</div>
              </div>
              <div class="econ-card highlight">
                <span class="econ-lbl">💰 Economia Real Estimada no TCO</span>
                <div class="econ-val"><strong>{f['economia']} · Redução drástica de custos recorrentes</strong></div>
              </div>
            </div>
          </div>

          <!-- SEÇÃO 3: REQUISITOS DE INFRAESTRUTURA & ECOSSISTEMA -->
          <div class="entry-section">
            <span class="label">3. Requisitos de Infraestrutura, Ecossistema &amp; Veredito</span>
            <div class="infra-grid">
              <div class="infra-card">
                <span class="infra-lbl">🖥️ Infraestrutura Recomendada</span>
                <div class="infra-val">{f['infra']}</div>
              </div>
              <div class="infra-card">
                <span class="infra-lbl">🔗 Ecossistema &amp; Padrões</span>
                <p><code>{f['categoria']}</code> · Padrões Abertos OSI</p>
              </div>
              <div class="infra-card verdict">
                <span class="infra-lbl">🏆 Veredito do Arquiteto</span>
                <p><strong>Por que adotar:</strong> {f['veredito']}</p>
              </div>
            </div>
            <div style="margin-top:6px;">
              <a class="repo-btn" href="{f['repo_url']}" target="_blank" rel="noopener">
                <svg viewBox="0 0 24 24"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/></svg>
                <span>Repositório Oficial &amp; Código-Fonte: {f['repo_txt']} ↗</span>
              </a>
            </div>
          </div>

          <!-- SEÇÃO 4: COMO USAR NO DIA A DIA -->
          <div class="entry-section">
            <span class="label">4. Como Usar no Dia a Dia (Passo a Passo Prático)</span>
            <div class="steps-grid">
              <div class="step-card">
                <div class="step-head"><span class="step-badge">1</span> Configuração</div>
                <p>{f['passo_1']}</p>
              </div>
              <div class="step-card">
                <div class="step-head"><span class="step-badge">2</span> Operação</div>
                <p>{f['passo_2']}</p>
              </div>
              <div class="step-card">
                <div class="step-head"><span class="step-badge">3</span> Resultado</div>
                <p>{f['passo_3']}</p>
              </div>
            </div>
          </div>

        </div>
      </div>
"""
        cards_html.append(c)
    return "\n".join(cards_html)

def atualizar_lista(filename, fichas_data):
    filepath = os.path.join(OUTPUT_DIR, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")

    # Atualizar stat de total de ferramentas no header
    stat_val = soup.find("div", class_="stat-val")
    if stat_val:
        stat_val.string = str(len(fichas_data))

    # Atualizar ledger
    ledger = soup.find("div", class_="ledger")
    if ledger:
        ledger.clear()
        rendered = render_cards(fichas_data)
        ledger.append(BeautifulSoup(rendered, "html.parser"))

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(str(soup))
    print(f"  -> [✓] Atualizado com 10/10 fichas: {filename}")

def main():
    print("[*] Preenchendo fichas completas nas Camadas 33 e 34...")
    atualizar_lista("33-aidd-trilha-de-adocao-e-maturidade.html", FICHAS_33)
    atualizar_lista("34-relatorio-tco-roi-soberania-economica.html", FICHAS_34)
    print("\n[OK] Camadas 33 e 34 completadas com sucesso!")

if __name__ == "__main__":
    main()
