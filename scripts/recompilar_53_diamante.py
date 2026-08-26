# -*- coding: utf-8 -*-
"""
RECOMPILADOR OFICIAL DA CAMADA 53 - MARKETING DIGITAL SOBERANO (DIAMANTE R5)
Corrige a inversão bizarra de colunas gerada pelo Mimocode e aplica 100% da tipografia e cards Diamante R5.
"""
import os
import sys
from pathlib import Path
from compilar_compendio_diamante import compilar_dossie_diamante

def console_utf8():
    if sys.platform == "win32":
        try:
            sys.stdout.reconfigure(encoding="utf-8")
            sys.stderr.reconfigure(encoding="utf-8")
        except Exception:
            pass

console_utf8()

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_FILE = BASE_DIR / "output" / "listas-open-source" / "53-melhores-ferramentas-de-marketing-digital-open-source-da-atualidade.html"
DOCS_FILE = BASE_DIR / "docs" / "listas" / "53-melhores-ferramentas-de-marketing-digital-open-source-da-atualidade.html"

dados_53 = {
    "numero": 53,
    "titulo": "Top 20 Melhores Ferramentas de Marketing Digital Open-Source",
    "slug": "melhores-ferramentas-de-marketing-digital-open-source-da-atualidade",
    "deck": "Compilação definitiva das melhores ferramentas open-source de marketing digital da atualidade com licença OSI válida, prontas para produção corporativa e substituição de pilhas SaaS abusivas (HubSpot, Mailchimp, Google Analytics, Zapier e Hotjar).",
    "stats": {
        "ferramentas": 20,
        "saas_substituidos": "20+",
        "economia_anual": "R$ 72.000+",
        "licencas": "100% OSI"
    },
    "rotas": {
        "fragil": {
            "titulo": "Rota Frágil (Marketing Proprietário)",
            "desc": "Custos por contato que explodem com o crescimento da base, bloqueio de exportação de leads, perda de privacidade e riscos severos na LGPD."
        },
        "soberana": {
            "titulo": "Rota Soberana (Marketing Open Source)",
            "desc": "Envio ilimitado de newsletters, analytics sem cookies intrusivos, CRM e automação sob controle próprio com infraestrutura local e custo previsível."
        }
    },
    "ferramentas": [
        {
            "rank": 1,
            "nome": "Listmonk",
            "slug": "listmonk",
            "saas_substituido": "Mailchimp / SendGrid",
            "economia_anual_str": "R$ 9.600/ano",
            "licenca_osi": "AGPL-3.0",
            "categoria": "Email Marketing & Newsletters",
            "senioridade": "Pleno",
            "o_que_faz": "Gerenciador de newsletters e campanhas de email marketing de altíssima performance escrito em Go, capaz de disparar milhões de emails usando SMTP próprio ou SES.",
            "como_funciona": "Binário autocontido ultrarrápido acoplado ao PostgreSQL com suporte a templates dinâmicos em Go, segmentação SQL em tempo real e analytics de entrega.",
            "comando_rapido": "docker run -d --name listmonk -p 9000:9000 listmonk/listmonk:latest",
            "repositorio_github": "https://github.com/knadh/listmonk",
            "veredito": "Substituto absoluto do Mailchimp. Elimina a cobrança predatória por volume de contatos inativos e garante taxas de entrega elevadas com custo de infraestrutura quase nulo.",
            "passos_praticos": [
                {"passo": 1, "titulo": "Deploy com PostgreSQL", "descricao": "Execução via docker-compose vinculando o banco de dados e definindo credenciais administrativas."},
                {"passo": 2, "titulo": "Conexão SMTP / SES", "descricao": "Configuração do provedor de envio (Amazon SES, Postmark ou servidor SMTP local com SPF/DKIM/DMARC)."},
                {"passo": 3, "titulo": "Importação de Base & Disparo", "descricao": "Importação de leads via CSV com campos customizados e criação de templates dinâmicos."}
            ],
            "requisitos_infra": {"ram_minima": "512 MB RAM", "cpu_minima": "1 vCPU"}
        },
        {
            "rank": 2,
            "nome": "Mautic",
            "slug": "mautic",
            "saas_substituido": "HubSpot Marketing / ActiveCampaign",
            "economia_anual_str": "R$ 24.000/ano",
            "licenca_osi": "GPL-3.0",
            "categoria": "Automação de Marketing",
            "senioridade": "Sênior",
            "o_que_faz": "Plataforma completa de automação de marketing com construtor visual de fluxos de nutrição, lead scoring multicanal, landing pages e rastreamento de comportamento web.",
            "como_funciona": "Arquitetura baseada em PHP/Symfony com fila de tarefas assíncronas no Redis/MySQL, disparando réguas de relacionamento baseadas em gatilhos e pontos de interação.",
            "comando_rapido": "docker run -d --name mautic -p 8080:80 mautic/mautic:latest",
            "repositorio_github": "https://github.com/mautic/mautic",
            "veredito": "A única alternativa open-source que compete de igual para igual com o HubSpot Marketing Enterprise, permitindo orquestração de leads sem travas comerciais.",
            "passos_praticos": [
                {"passo": 1, "titulo": "Instalação da Stack Mautic", "descricao": "Subida de containers com PHP-FPM, Nginx, MySQL e Redis para cache de filas."},
                {"passo": 2, "titulo": "Instalação do Pixel de Tracking", "descricao": "Inserção do script de rastreamento no site para capturar visitas, cliques e conversões."},
                {"passo": 3, "titulo": "Desenho da Régua de Nutrição", "descricao": "Montagem do fluxo visual no builder: envio de emails, atribuição de tags e transição de leads."}
            ],
            "requisitos_infra": {"ram_minima": "2 GB RAM", "cpu_minima": "2 vCPU"}
        },
        {
            "rank": 3,
            "nome": "Plausible Analytics",
            "slug": "plausible",
            "saas_substituido": "Google Analytics 4",
            "economia_anual_str": "R$ 4.800/ano",
            "licenca_osi": "AGPL-3.0",
            "categoria": "Web Analytics Sem Cookies",
            "senioridade": "Júnior",
            "o_que_faz": "Web analytics limpo, leve (<1 KB de script) e 100% focado em privacidade, totalmente compatível com LGPD/GDPR sem necessidade de banners intrusivos de consentimento.",
            "como_funciona": "Backend em Elixir com banco de dados colunar ClickHouse para agregações em tempo real, sem persistir identificadores individuais nem rastrear usuários entre sites.",
            "comando_rapido": "docker compose -f plausible-compose.yml up -d",
            "repositorio_github": "https://github.com/plausible/analytics",
            "veredito": "Elimina a lentidão e a complexidade bizantina do GA4. Dashboard de 1 página que qualquer profissional de marketing entende em 30 segundos.",
            "passos_praticos": [
                {"passo": 1, "titulo": "Deploy ClickHouse + Plausible", "descricao": "Instalação via Docker Compose pré-configurado com PostgreSQL e ClickHouse."},
                {"passo": 2, "titulo": "Adição do Script Leve", "descricao": "Inclusão da tag `<script defer data-domain='seusite.com' src='.../script.js'></script>`."},
                {"passo": 3, "titulo": "Definição de Metas & Funis", "descricao": "Configuração de metas personalizadas de download, conversão e parâmetros UTM."}
            ],
            "requisitos_infra": {"ram_minima": "2 GB RAM", "cpu_minima": "2 vCPU"}
        },
        {
            "rank": 4,
            "nome": "PostHog",
            "slug": "posthog",
            "saas_substituido": "Mixpanel / Amplitude / Hotjar",
            "economia_anual_str": "R$ 36.000/ano",
            "licenca_osi": "MIT",
            "categoria": "Product Analytics & Heatmaps",
            "senioridade": "Sênior",
            "o_que_faz": "Suíte all-in-one de product marketing: analytics de produto, gravação de sessões em vídeo, heatmaps de cliques, feature flags e experimentos com teste A/B.",
            "como_funciona": "Ingestão de eventos em larga escala via Kafka/ClickHouse com processamento em tempo real e SDKs client-side para web e mobile.",
            "comando_rapido": "docker compose -f posthog-compose.yml up -d",
            "repositorio_github": "https://github.com/PostHog/posthog",
            "veredito": "Substitui 4 SaaS pagos ao mesmo tempo (Mixpanel + Hotjar + LaunchDarkly + Optimizely) com soberania total de dados do produto.",
            "passos_praticos": [
                {"passo": 1, "titulo": "Deploy da Infraestrutura", "descricao": "Subida em VPS com ClickHouse e Kafka para processamento de alto throughput."},
                {"passo": 2, "titulo": "Inicialização do SDK", "descricao": "Injeção de `posthog.init()` com gravação de sessão habilitada."},
                {"passo": 3, "titulo": "Criação de Funil de Conversão", "descricao": "Mapeamento dos passos do usuário do onboarding até o checkout para análise de churn."}
            ],
            "requisitos_infra": {"ram_minima": "4 GB RAM", "cpu_minima": "4 vCPU"}
        },
        {
            "rank": 5,
            "nome": "n8n",
            "slug": "n8n",
            "saas_substituido": "Zapier / Make.com",
            "economia_anual_str": "R$ 18.000/ano",
            "licenca_osi": "Sustainable Use / Apache-2.0",
            "categoria": "Orquestração & Automação",
            "senioridade": "Pleno",
            "o_que_faz": "Plataforma visual de automação de fluxo de trabalho com mais de 400 conectores nativos, webhooks, lógica condicional e suporte a scripts JavaScript/Python e agentes de IA.",
            "como_funciona": "Serviço em Node.js com execução orientada a nós e armazenamento de execuções em SQLite/PostgreSQL, operando sob filas distribuídas no modo cluster.",
            "comando_rapido": "docker run -d --name n8n -p 5678:5678 n8nio/n8n:latest",
            "repositorio_github": "https://github.com/n8n-io/n8n",
            "veredito": "Liberta o time de marketing das cobranças abusivas por 'tarefas' do Zapier, permitindo rodar milhões de automações sem custo variável.",
            "passos_praticos": [
                {"passo": 1, "titulo": "Deploy Seguro", "descricao": "Execução com Docker montando volume persistente para credenciais e workflows."},
                {"passo": 2, "titulo": "Criação de Webhook", "descricao": "Geração de endpoint para receber leads de formulários, landing pages ou CRM."},
                {"passo": 3, "titulo": "Conexão com LLMs & CRMs", "descricao": "Enriquecimento automático de leads com IA e despacho direto para o pipeline de vendas."}
            ],
            "requisitos_infra": {"ram_minima": "1 GB RAM", "cpu_minima": "1 vCPU"}
        },
        {
            "rank": 6,
            "nome": "Twenty CRM",
            "slug": "twenty",
            "saas_substituido": "HubSpot CRM / Salesforce",
            "economia_anual_str": "R$ 30.000/ano",
            "licenca_osi": "AGPL-3.0",
            "categoria": "CRM & Gestão de Vendas",
            "senioridade": "Pleno",
            "o_que_faz": "CRM moderno, rápido e colaborativo com pipelines de vendas visual kanban, visualização de tabelas com filtros avançados e gestão completa de contatos e negócios.",
            "como_funciona": "Stack moderna em TypeScript com NestJS, GraphQL, PostgreSQL e interface ultra-responsiva em React/Tailwind, desenhado com arquitetura extensível de plugins.",
            "comando_rapido": "docker compose -f twenty-compose.yml up -d",
            "repositorio_github": "https://github.com/twentyhq/twenty",
            "veredito": "A melhor alternativa open-source ao Salesforce e HubSpot CRM, com interface contemporânea e velocidade incomparável.",
            "passos_praticos": [
                {"passo": 1, "titulo": "Deploy Docker", "descricao": "Execução com PostgreSQL e Redis configurando as variáveis de ambiente."},
                {"passo": 2, "titulo": "Configuração de Pipelines", "descricao": "Definição das etapas de qualificação, proposta e fechamento de vendas."},
                {"passo": 3, "titulo": "Integração com n8n", "descricao": "Criação de gatilhos automáticos para entrada de leads qualificados."}
            ],
            "requisitos_infra": {"ram_minima": "2 GB RAM", "cpu_minima": "2 vCPU"}
        },
        {
            "rank": 7,
            "nome": "Ghost",
            "slug": "ghost",
            "saas_substituido": "Medium / Substack / WordPress",
            "economia_anual_str": "R$ 6.000/ano",
            "licenca_osi": "MIT",
            "categoria": "Publicação & Inbound Marketing",
            "senioridade": "Pleno",
            "o_que_faz": "Plataforma profissional de publicação de conteúdo, blogs de alta conversão e newsletters pagas com sistema de membros e assinaturas integrado.",
            "como_funciona": "Motor em Node.js com banco MySQL e frontend renderizado em Handlebars/Tailwind com pontuação máxima de 100 no Google PageSpeed/Lighthouse.",
            "comando_rapido": "docker run -d --name ghost -p 2368:2368 ghost:5-alpine",
            "repositorio_github": "https://github.com/TryGhost/Ghost",
            "veredito": "Padrão de ouro para SEO e inbound marketing. Muito mais veloz e seguro que WordPress, sem plugins pesados nem vulnerabilidades recorrentes.",
            "passos_praticos": [
                {"passo": 1, "titulo": "Deploy com MySQL", "descricao": "Instalação oficial em container Docker com proxy reverso Nginx e SSL automático."},
                {"passo": 2, "titulo": "Configuração de Assinaturas", "descricao": "Integração com Stripe para monetização ou captura de emails com opt-in duplo."},
                {"passo": 3, "titulo": "SEO & Otimização", "descricao": "Configuração automática de meta tags Open Graph, schema.org e sitemaps XML."}
            ],
            "requisitos_infra": {"ram_minima": "1 GB RAM", "cpu_minima": "1 vCPU"}
        },
        {
            "rank": 8,
            "nome": "Matomo",
            "slug": "matomo",
            "saas_substituido": "Google Analytics 360",
            "economia_anual_str": "R$ 15.000/ano",
            "licenca_osi": "GPL-3.0",
            "categoria": "Analytics Empresarial Completo",
            "senioridade": "Sênior",
            "o_que_faz": "A suíte corporativa de analytics mais completa do ecossistema open-source: atribuição multi-toque, relatórios de ecommerce avançados, funis e conformidade estrita.",
            "como_funciona": "Backend em PHP com banco MySQL/MariaDB otimizado para bilhões de pageviews com arquivamento em lote de relatórios históricos.",
            "comando_rapido": "docker run -d --name matomo -p 8080:80 matomo:latest",
            "repositorio_github": "https://github.com/matomo-org/matomo",
            "veredito": "Escolha preferida de governos, bancos e corporações que não podem enviar dados analíticos para servidores de Big Techs norte-americanas.",
            "passos_praticos": [
                {"passo": 1, "titulo": "Deploy com MariaDB", "descricao": "Subida em container com ajustes de `max_allowed_packet` e buffers de memória."},
                {"passo": 2, "titulo": "Anonimização de IP", "descricao": "Habilitação do mascaramento de 2 bytes de IP para conformidade integral com LGPD."},
                {"passo": 3, "titulo": "Rastreamento de E-commerce", "descricao": "Inserção dos eventos de visualização de produto, carrinho e pedido faturado."}
            ],
            "requisitos_infra": {"ram_minima": "2 GB RAM", "cpu_minima": "2 vCPU"}
        },
        {
            "rank": 9,
            "nome": "Chatwoot",
            "slug": "chatwoot",
            "saas_substituido": "Intercom / Zendesk",
            "economia_anual_str": "R$ 18.000/ano",
            "licenca_osi": "AGPL-3.0",
            "categoria": "Atendimento Multicanal & Vendas",
            "senioridade": "Pleno",
            "o_que_faz": "Caixa de entrada compartilhada para suporte e vendas em tempo real via WhatsApp, Instagram, Telegram, Email e widget de chat no site.",
            "como_funciona": "Desenvolvido em Ruby on Rails com Vue.js, PostgreSQL e Redis para mensagens bidirecionais via WebSockets e suporte a webhooks de IA.",
            "comando_rapido": "docker compose -f chatwoot-compose.yml up -d",
            "repositorio_github": "https://github.com/chatwoot/chatwoot",
            "veredito": "Elimina as faturas de milhares de dólares do Intercom por usuário/mês, unificando todo o atendimento comercial da empresa.",
            "passos_praticos": [
                {"passo": 1, "titulo": "Deploy Docker Compose", "descricao": "Execução com banco PostgreSQL, Redis e servidor de background worker Sidekiq."},
                {"passo": 2, "titulo": "Conexão de Canais", "descricao": "Integração via QR Code com WhatsApp e páginas do Facebook/Instagram."},
                {"passo": 3, "titulo": "Roteamento de Conversas", "descricao": "Criação de equipes de vendas e agentes automáticos para qualificação de leads."}
            ],
            "requisitos_infra": {"ram_minima": "2 GB RAM", "cpu_minima": "2 vCPU"}
        },
        {
            "rank": 10,
            "nome": "Formbricks",
            "slug": "formbricks",
            "saas_substituido": "Typeform / Hotjar Surveys",
            "economia_anual_str": "R$ 7.200/ano",
            "licenca_osi": "AGPL-3.0",
            "categoria": "Pesquisas & Feedback de Usuários",
            "senioridade": "Júnior",
            "o_que_faz": "Suíte de pesquisas e questionários contextuais in-app e na web, permitindo capturar NPS, pesquisas de churn e feedback no momento exato da jornada.",
            "como_funciona": "Arquitetura em Next.js e TypeScript com PostgreSQL e Tailwind, disponibilizando formulários leves e SDK reativo para apps web.",
            "comando_rapido": "docker compose -f formbricks-compose.yml up -d",
            "repositorio_github": "https://github.com/formbricks/formbricks",
            "veredito": "Alternativa de altíssimo nível ao Typeform, permitindo respostas ilimitadas sem custos adicionais de licenciamento.",
            "passos_praticos": [
                {"passo": 1, "titulo": "Instalação do Container", "descricao": "Deploy em VPS via Docker Compose configurando chaves de autenticação."},
                {"passo": 2, "titulo": "Criação de Pesquisa", "descricao": "Montagem visual da pesquisa com lógica condicional de perguntas."},
                {"passo": 3, "titulo": "Disparo Segmentado", "descricao": "Exibição da pesquisa baseada em ações específicas do usuário no site."}
            ],
            "requisitos_infra": {"ram_minima": "1 GB RAM", "cpu_minima": "1 vCPU"}
        },
        {
            "rank": 11,
            "nome": "Metabase",
            "slug": "metabase",
            "saas_substituido": "Power BI Pro / Tableau",
            "economia_anual_str": "R$ 14.400/ano",
            "licenca_osi": "AGPL-3.0",
            "categoria": "BI & Dashboards de Marketing",
            "senioridade": "Pleno",
            "o_que_faz": "Ferramenta de Business Intelligence intuitiva que permite a qualquer profissional criar dashboards de métricas de marketing (CAC, LTV, ROAS) sem saber SQL.",
            "como_funciona": "Aplicação em Clojure rodando sobre JVM, conectando-se diretamente a bancos de dados (Postgres, ClickHouse, MySQL) com construtor visual de consultas.",
            "comando_rapido": "docker run -d --name metabase -p 3000:3000 metabase/metabase:latest",
            "repositorio_github": "https://github.com/metabase/metabase",
            "veredito": "Democratiza os dados de marketing para a empresa inteira, gerando gráficos elegantes compartilháveis e alertas automáticos via Slack/Email.",
            "passos_praticos": [
                {"passo": 1, "titulo": "Subida do Container", "descricao": "Execução via Docker apontando para um volume de dados persistente."},
                {"passo": 2, "titulo": "Conexão aos Bancos", "descricao": "Adição em modo de leitura dos bancos do CRM, e-commerce e analytics."},
                {"passo": 3, "titulo": "Painel de Gestão", "descricao": "Criação de dashboards com KPIs diários de novos leads, custo por lead e receita."}
            ],
            "requisitos_infra": {"ram_minima": "1 GB RAM", "cpu_minima": "1 vCPU"}
        },
        {
            "rank": 12,
            "nome": "Umami",
            "slug": "umami",
            "saas_substituido": "Fathom / Simple Analytics",
            "economia_anual_str": "R$ 3.600/ano",
            "licenca_osi": "MIT",
            "categoria": "Analytics Minimalista & Rápido",
            "senioridade": "Júnior",
            "o_que_faz": "Analytics ultraleve, focado em métricas essenciais de tráfego, fontes de referência, navegadores, dispositivos e conversões de eventos.",
            "como_funciona": "Backend em Node.js/Next.js com banco PostgreSQL ou MySQL, entregando um painel limpo que carrega em menos de 100 milissegundos.",
            "comando_rapido": "docker compose -f umami-compose.yml up -d",
            "repositorio_github": "https://github.com/umami-software/umami",
            "veredito": "Ideal para quem quer apenas saber quantas pessoas visitaram a página e de onde vieram, sem a sobrecarga ou termos invasivos de privacidade.",
            "passos_praticos": [
                {"passo": 1, "titulo": "Deploy Docker", "descricao": "Execução simplificada com PostgreSQL gerenciando os eventos analíticos."},
                {"passo": 2, "titulo": "Instalação do Snippet", "descricao": "Inclusão de uma única linha de código HTML no cabeçalho do site."},
                {"passo": 3, "titulo": "Monitoramento em Tempo Real", "descricao": "Visualização de visitantes ativos e páginas mais acessadas do dia."}
            ],
            "requisitos_infra": {"ram_minima": "512 MB RAM", "cpu_minima": "1 vCPU"}
        },
        {
            "rank": 13,
            "nome": "Directus",
            "slug": "directus",
            "saas_substituido": "Contentful / Sanity.io",
            "economia_anual_str": "R$ 12.000/ano",
            "licenca_osi": "BPSL / GPL-3.0",
            "categoria": "Headless CMS & Gestão de Ativos",
            "senioridade": "Pleno",
            "o_que_faz": "Headless CMS e plataforma de dados que transforma qualquer banco SQL existente em uma API REST e GraphQL com painel visual moderno para times de conteúdo.",
            "como_funciona": "Construído em Node.js e Vue.js, opera como uma camada em cima do seu banco relacional sem criar tabelas proprietárias obscuras.",
            "comando_rapido": "docker compose -f directus-compose.yml up -d",
            "repositorio_github": "https://github.com/directus/directus",
            "veredito": "Permite que times de marketing criem landing pages e gerenciem campanhas dinâmicas com autonomia total sobre o banco de dados.",
            "passos_praticos": [
                {"passo": 1, "titulo": "Deploy sobre PostgreSQL", "descricao": "Inicialização rápida conectando ao banco de dados relacional existente."},
                {"passo": 2, "titulo": "Modelagem de Coleções", "descricao": "Criação de campos de banner, textos promocionais e depoimentos via interface."},
                {"passo": 3, "titulo": "Consumo via API", "descricao": "Entrega imediata dos conteúdos para o frontend via endpoints REST e GraphQL."}
            ],
            "requisitos_infra": {"ram_minima": "1 GB RAM", "cpu_minima": "1 vCPU"}
        },
        {
            "rank": 14,
            "nome": "SearXNG",
            "slug": "searxng",
            "saas_substituido": "Semrush / APIs de Busca Pagas",
            "economia_anual_str": "R$ 8.400/ano",
            "licenca_osi": "AGPL-3.0",
            "categoria": "Metabusca & Inteligência de SEO",
            "senioridade": "Pleno",
            "o_que_faz": "Metamotor de busca anônimo e agregador de resultados de mais de 70 provedores de pesquisa, ideal para inteligência competitiva e auditoria de SERP.",
            "como_funciona": "Escrito em Python, consulta simultaneamente Google, Bing, DuckDuckGo e outros mecanismos sem compartilhar perfis nem aceitar rastreamento.",
            "comando_rapido": "docker run -d --name searxng -p 8080:8080 searxng/searxng:latest",
            "repositorio_github": "https://github.com/searxng/searxng",
            "veredito": "Ferramenta essencial para monitorar rankings orgânicos e termos de pesquisa de concorrentes sem sofrer bloqueios de CAPTCHA ou distorções de bolha.",
            "passos_praticos": [
                {"passo": 1, "titulo": "Instalação via Docker", "descricao": "Execução isolada em container configurando portas e chaves de segurança."},
                {"passo": 2, "titulo": "Ativação de Motores de Busca", "descricao": "Habilitação das fontes de busca nos arquivos YAML de configuração."},
                {"passo": 3, "titulo": "Auditoria de Termos", "descricao": "Execução de consultas programadas via API JSON para análise de posicionamento."}
            ],
            "requisitos_infra": {"ram_minima": "512 MB RAM", "cpu_minima": "1 vCPU"}
        },
        {
            "rank": 15,
            "nome": "Activepieces",
            "slug": "activepieces",
            "saas_substituido": "Zapier Teams / Make",
            "economia_anual_str": "R$ 15.000/ano",
            "licenca_osi": "MIT",
            "categoria": "Automação No-Code Moderna",
            "senioridade": "Júnior",
            "o_que_faz": "Plataforma no-code de automação empresarial com design limpo, dezenas de conectores de marketing e foco absoluto em facilidade de uso para não-programadores.",
            "como_funciona": "Backend em TypeScript com execução de fluxos isolada, interface intuitiva e suporte extensivo à criação de peças personalizadas via npm.",
            "comando_rapido": "docker compose -f activepieces-compose.yml up -d",
            "repositorio_github": "https://github.com/activepieces/activepieces",
            "veredito": "A melhor interface para times de marketing que acham o n8n muito técnico e precisam de simplicidade visual imediata.",
            "passos_praticos": [
                {"passo": 1, "titulo": "Deploy Docker", "descricao": "Subida de containers com PostgreSQL e interface pré-configurada."},
                {"passo": 2, "titulo": "Conexão de Aplicativos", "descricao": "Autenticação em serviços de email, formulários e planilhas."},
                {"passo": 3, "titulo": "Ativação do Fluxo", "descricao": "Configuração do gatilho de novo lead e ação de disparo imediato."}
            ],
            "requisitos_infra": {"ram_minima": "1 GB RAM", "cpu_minima": "1 vCPU"}
        },
        {
            "rank": 16,
            "nome": "Strapi",
            "slug": "strapi",
            "saas_substituido": "Contentful / Prismic",
            "economia_anual_str": "R$ 14.000/ano",
            "licenca_osi": "MIT",
            "categoria": "Headless CMS para Campanhas",
            "senioridade": "Pleno",
            "o_que_faz": "O CMS headless mais adotado do mundo, permitindo criar schemas de páginas de captura, blogs corporativos e landing pages dinâmicas.",
            "como_funciona": "Construído em Node.js com sistema de tipos flexível, suporte a PostgreSQL, SQLite e MySQL, e painel administrativo personalizável em React.",
            "comando_rapido": "docker run -d --name strapi -p 1337:1337 strapi/strapi:latest",
            "repositorio_github": "https://github.com/strapi/strapi",
            "veredito": "Solução corporativa robusta para gerenciar múltiplos sites e aplicações a partir de um único ponto central de conteúdo de marketing.",
            "passos_praticos": [
                {"passo": 1, "titulo": "Deploy com PostgreSQL", "descricao": "Execução em ambiente de produção montando pastas de uploads e banco."},
                {"passo": 2, "titulo": "Criação de Tipos de Conteúdo", "descricao": "Desenho das estruturas de páginas, artigos e leads pelo painel."},
                {"passo": 3, "titulo": "Publicação e Cache", "descricao": "Integração com CDNs e webhooks para invalidação de cache automática."}
            ],
            "requisitos_infra": {"ram_minima": "2 GB RAM", "cpu_minima": "2 vCPU"}
        },
        {
            "rank": 17,
            "nome": "GrowthBook",
            "slug": "growthbook",
            "saas_substituido": "Optimizely / VWO",
            "economia_anual_str": "R$ 28.000/ano",
            "licenca_osi": "MIT",
            "categoria": "Testes A/B & Experimentação",
            "senioridade": "Sênior",
            "o_que_faz": "Plataforma de testes A/B, otimização de taxa de conversão (CRO) e feature flags com motor estatístico bayesiano e frequentista de alta precisão.",
            "como_funciona": "Conecta-se diretamente ao seu data warehouse (ClickHouse, BigQuery, Postgres) sem duplicar dados, analisando o impacto real dos experimentos.",
            "comando_rapido": "docker compose -f growthbook-compose.yml up -d",
            "repositorio_github": "https://github.com/growthbook/growthbook",
            "veredito": "Substitui ferramentas de CRO que cobram fortunas por visitante testado, permitindo experimentação contínua de copy, layout e ofertas.",
            "passos_praticos": [
                {"passo": 1, "titulo": "Deploy da Aplicação", "descricao": "Subida em VPS com MongoDB e API de feature flags em Node.js."},
                {"passo": 2, "titulo": "Conexão aos Dados", "descricao": "Vinculação da fonte de eventos analíticos para leitura de conversões."},
                {"passo": 3, "titulo": "Lançamento do Teste A/B", "descricao": "Configuração das variações de página e cálculo automático de significância estatística."}
            ],
            "requisitos_infra": {"ram_minima": "1 GB RAM", "cpu_minima": "1 vCPU"}
        },
        {
            "rank": 18,
            "nome": "Cal.com",
            "slug": "cal-com",
            "saas_substituido": "Calendly Pro",
            "economia_anual_str": "R$ 4.200/ano",
            "licenca_osi": "AGPL-3.0",
            "categoria": "Agendamento de Demonstrações & Vendas",
            "senioridade": "Júnior",
            "o_que_faz": "Infraestrutura completa de agendamento de reuniões comerciais, demonstrações de vendas e consultorias com sincronização em tempo real de calendários.",
            "como_funciona": "Construído em Next.js com PostgreSQL, Prisma e tRPC, integrando-se nativamente com Google Meet, Zoom e provedores de pagamento Stripe.",
            "comando_rapido": "docker compose -f calcom-compose.yml up -d",
            "repositorio_github": "https://github.com/calcom/cal.com",
            "veredito": "Elimina as limitações de usuários do Calendly e permite embedar páginas de agendamento de alta conversão diretamente no seu próprio domínio.",
            "passos_praticos": [
                {"passo": 1, "titulo": "Instalação Docker", "descricao": "Deploy configurando variáveis de URL base e chaves secretas de criptografia."},
                {"passo": 2, "titulo": "Sincronização de Calendário", "descricao": "Conexão das agendas da equipe para prevenção de conflito de horários."},
                {"passo": 3, "titulo": "Incorporação no Site", "descricao": "Adição do iframe de agendamento na página de confirmação de lead."}
            ],
            "requisitos_infra": {"ram_minima": "1 GB RAM", "cpu_minima": "1 vCPU"}
        },
        {
            "rank": 19,
            "nome": "Coolify",
            "slug": "coolify",
            "saas_substituido": "Heroku / Vercel Pro",
            "economia_anual_str": "R$ 12.000/ano",
            "licenca_osi": "Apache-2.0",
            "categoria": "Painel de Deploy de Aplicações de Marketing",
            "senioridade": "Pleno",
            "o_que_faz": "Plataforma self-hosted como serviço (PaaS) que automatiza o deploy, certificados SSL e backups de todas as aplicações e landing pages de marketing em 1 clique.",
            "como_funciona": "Gerencia o daemon Docker local ou em servidores remotos via SSH, integrando Traefik para roteamento e renovação automática de certificados Let's Encrypt.",
            "comando_rapido": "curl -fsSL https://cdn.coollabs.io/coolify/install.sh | bash",
            "repositorio_github": "https://github.com/coollabsio/coolify",
            "veredito": "O cérebro operacional para rodar todas as ferramentas de marketing em um único VPS sem precisar de engenheiros de infraestrutura dedicados.",
            "passos_praticos": [
                {"passo": 1, "titulo": "Instalação do Coolify", "descricao": "Execução do instalador oficial em um servidor Ubuntu virgem."},
                {"passo": 2, "titulo": "Criação de Projetos", "descricao": "Deploy em 1 clique de Listmonk, Ghost, n8n ou Plausible a partir de templates."},
                {"passo": 3, "titulo": "Configuração de Domínios", "descricao": "Associação de subdomínios com certificados SSL HTTPS automáticos."}
            ],
            "requisitos_infra": {"ram_minima": "2 GB RAM", "cpu_minima": "2 vCPU"}
        },
        {
            "rank": 20,
            "nome": "Uptime Kuma",
            "slug": "uptime-kuma",
            "saas_substituido": "Statuspage / Pingdom",
            "economia_anual_str": "R$ 4.800/ano",
            "licenca_osi": "MIT",
            "categoria": "Monitoramento de Páginas & Campanha",
            "senioridade": "Júnior",
            "o_que_faz": "Ferramenta de monitoramento de disponibilidade que avisa instantaneamente no WhatsApp, Telegram ou Slack se uma landing page ou formulário cair durante uma campanha.",
            "como_funciona": "Aplicação leve em Node.js e Vue com banco SQLite embutido, checando status HTTP(s), certificados SSL e tempo de resposta a cada minuto.",
            "comando_rapido": "docker run -d --name uptime-kuma -p 3001:3001 louislam/uptime-kuma:1",
            "repositorio_github": "https://github.com/louislam/uptime-kuma",
            "veredito": "Garante que você nunca gaste dinheiro com tráfego pago enviando visitantes para páginas fora do ar ou com links quebrados.",
            "passos_praticos": [
                {"passo": 1, "titulo": "Deploy Imediato", "descricao": "Execução de um container leve com volume local para persistência de dados."},
                {"passo": 2, "titulo": "Cadastro de URLs", "descricao": "Inserção dos links de checkout e landing pages com intervalo de 60 segundos."},
                {"passo": 3, "titulo": "Criação de Página de Status", "descricao": "Publicação de página pública de transparência para clientes e parceiros."}
            ],
            "requisitos_infra": {"ram_minima": "256 MB RAM", "cpu_minima": "1 vCPU"}
        }
    ]
}

html_diamante = compilar_dossie_diamante(dados_53)
OUTPUT_FILE.write_text(html_diamante, encoding="utf-8")
DOCS_FILE.write_text(html_diamante, encoding="utf-8")
print("✅ Camada 53 100% Recompilada no Padrão Diamante R5 com sucesso!")
