# -*- coding: utf-8 -*-
"""
Script mestre para padronizar e enriquecer a seção '3. Como Usar no Dia a Dia':
1. Garante que em TODOS os cards de TODAS as listas a seção 'how-to-use' ocupe 100% da largura de .entry-body (fora de .cols).
2. Adiciona a seção completa com passos práticos reais para os cards que não a possuem (camadas 33 a 39 e complementares).
3. Padroniza o CSS em todos os 49 arquivos HTML.
"""
import os
import re
import sys

def console_utf8():
    if sys.platform == "win32":
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")

console_utf8()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = os.path.join(BASE_DIR, "output", "listas-open-source")

CSS_HOW_TO_USE = """
  .how-to-use { display:flex; flex-direction:column; gap:8px; padding-top:14px; border-top:1px dashed var(--rule-soft); width:100%; }
  .how-to-use .label { color:var(--accent); font-weight:600; font-size:11px; letter-spacing:.12em; text-transform:uppercase; }
  .how-to-use p { margin:0; font-size:14.5px; line-height:1.55; color:var(--ink-2); }
  .how-to-use p strong { color:var(--ink); font-weight:600; }
  .how-to-use code { font-family:var(--mono); font-size:12.5px; background:var(--surface-2); padding:2px 6px; border-radius:2px; border:1px solid var(--rule-soft); color:var(--ink); }
"""

# Base de conhecimento de passos práticos por ferramenta para injeção automática
USO_PRATICO_MAP = {
    # Camada 35 - SOC / CTI
    "wazuh": "1. Instale o agente Wazuh em todos os servidores Linux e Windows da organização.<br>2. Centralize os alertas de integridade de arquivos (FIM) e tentativas de invasão no Wazuh Dashboard.<br>3. Crie regras de bloqueio automático no firewall acionadas por detecções de força bruta via Active Response.",
    "thehive": "1. Configure webhooks no SIEM/Wazuh para abrir casos automaticamente no TheHive ao detectar alertas críticos.<br>2. Atribua tarefas da investigação forense para os analistas do SOC em tempo real.<br>3. Exporte relatórios de pós-incidente e métricas de MTTR com total rastreabilidade.",
    "cortex": "1. Conecte o Cortex ao TheHive configurando as chaves de API dos analisadores de IOCs.<br>2. Ao clicar em um IP ou hash suspeito no caso, dispare a análise simultânea em +30 fontes abertas.<br>3. Receba o veredito enriquecido com nível de reputação em menos de 2 segundos.",
    "suricata": "1. Conecte a interface de rede do Suricata a uma porta de espelhamento (SPAN/TAP) do switch central.<br>2. Ative as assinaturas da comunidade Emerging Threats via <code>suricata-update</code> diário.<br>3. Transmita o arquivo de eventos <code>eve.json</code> para o seu SIEM para correlação e alertas em tempo real.",
    "zeek": "1. Execute o Zeek monitorando o tráfego de saída (egress) da rede corporativa.<br>2. Audite conexões TLS anômalas, consultas DNS suspeitas e transferências de arquivos não autorizadas.<br>3. Alimente caçadores de ameaças com metadados estruturados para detecção de C2 e exfiltração.",
    "misp": "1. Sincronize feeds de CTI abertos e setoriais (CERT.br, AlienVault OTX) na sua instância MISP.<br>2. Exporte listas automáticas de IoCs para os firewalls e EDRs da empresa bloquearem domínios maliciosos.<br>3. Compartilhe ataques sofridos de forma anonimizada com a comunidade e parceiros de negócio.",
    "opencti": "1. Conecte conectores de inteligência (Mitre ATT&CK, MISP, Feeds RSS) ao OpenCTI.<br>2. Navegue visualmente pelo grafo de atores de ameaças para entender quais técnicas afetam o seu setor.<br>3. Gere relatórios executivos de risco cibernético para a diretoria e CISO.",
    "velociraptor": "1. Realize o deploy do cliente Velociraptor em endpoints corporativos via GPO ou script de provisionamento.<br>2. Ao suspeitar de invasão, dispare caça a artefatos (ex: <code>Windows.Detection.Amcache</code>) em milhares de máquinas simultaneamente.<br>3. Colete dumps de memória e arquivos MFT para perícia forense em minutos sem tirar o computador do ar.",
    "falco": "1. Instale o daemonset do Falco nos nós Kubernetes com o driver eBPF ativo.<br>2. Monitore violações de políticas como execução de shell interativo em containers ou alteração em <code>/etc/shadow</code>.<br>3. Integre os alertas ao Slack e orquestrador de segurança para isolar pods comprometidos automaticamente.",
    "sigma": "1. Escreva regras de detecção genéricas em formato YAML baseadas em comportamento de invasores.<br>2. Converta automaticamente com <code>sigmac</code> para a sintaxe do seu SIEM atual (Wazuh, Elastic, Splunk).<br>3. Mantenha todas as regras da empresa versionadas em um repositório Git com testes de CI/CD.",
    "shuffle": "1. Desenhe fluxos de automação conectando o recebimento de alertas à tomada de ação imediata.<br>2. Bloqueie automaticamente IPs no firewall e revogue sessões de usuários comprometidos no IdP.<br>3. Reduza o tempo de triagem de incidentes rotineiros de 40 minutos para 5 segundos.",
    "cuckoo": "1. Configure uma máquina virtual isolada Windows/Linux na sua infraestrutura de análise.<br>2. Submeta anexos de e-mails suspeitos e executáveis desconhecidos via API ou painel web.<br>3. Receba relatório dinâmico com todas as conexões de rede, alterações no registro e capturas de tela do malware em ação.",
    "yara": "1. Crie regras YARA customizadas para identificar padrões de código, strings ou cabeçalhos de arquivos maliciosos.<br>2. Execute varreduras periódicas em servidores de arquivos e caixas de entrada de e-mail.<br>3. Integre com seu EDR para quarentena instantânea de arquivos que combinem com as regras.",
    "bloodhound": "1. Execute o coletor SharpHound ou BloodHound.py na rede do Active Directory durante testes de segurança.<br>2. Importe o JSON no BloodHound GUI e filtre por 'Shortest Paths to Domain Admin'.<br>3. Identifique e elimine permissões delegadas excessivas e sessões de administradores expostas.",
    "trivy": "1. Adicione o <code>trivy image</code> como etapa obrigatória nas esteiras de CI/CD antes do deploy.<br>2. Bloqueie containers que contenham vulnerabilidades de severidade CRITICAL ou segredos vazados.<br>3. Exporte SBOM (Software Bill of Materials) nos padrões CycloneDX para conformidade com clientes.",
    "gitleaks": "1. Instale o Gitleaks nos hooks de <code>pre-commit</code> de todos os desenvolvedores da empresa.<br>2. Impeça que senhas, tokens de API e certificados privados sejam commitados nos repositórios Git.<br>3. Execute varreduras contínuas em pipelines para auditar todo o histórico retroativo de código.",
    "arkime": "1. Instale sensores de captura Arkime em pontos estratégicos de tráfego de entrada e saída do datacenter.<br>2. Quando um incidente for detectado, pesquise o histórico exato da sessão pelo IP e porta para ver o payload real.<br>3. Faça download do arquivo PCAP reconstruído para validar se houve vazamento real de dados.",
    "defectdojo": "1. Centralize as saídas de ferramentas de SAST, DAST e Scanners de Vulnerabilidades no DefectDojo via API.<br>2. Acompanhe a desduplicação automática e defina SLAs de correção para cada equipe de desenvolvimento.<br>3. Acompanhe a evolução da postura de segurança da organização em dashboards executivos.",
    "greenbone": "1. Agende varreduras semanais de portas e serviços expostos em toda a faixa de IPs corporativa.<br>2. Analise os relatórios de conformidade para aplicar patches em servidores com softwares desatualizados.<br>3. Valide o fechamento de brechas após as correções aplicadas pelo time de infraestrutura.",
    "atomic red team": "1. Selecione técnicas do MITRE ATT&CK que a sua equipe precisa validar (ex: T1059 Command and Scripting Interpreter).<br>2. Dispare os testes atômicos automatizados controladamente em uma máquina de teste.<br>3. Verifique se o seu SIEM/EDR gerou os alertas esperados e ajuste as regras de detecção onde houver pontos cegos.",

    # Camada 36 - Dados / Lakehouse
    "apache iceberg": "1. Configure o Iceberg como formato padrão de tabela no catálogo de dados (ex: Nessie, AWS Glue ou REST Catalog).<br>2. Grave dados particionados em arquivos Parquet via DuckDB, Spark ou Flink com garantias transacionais ACID.<br>3. Execute consultas analíticas e utilize recursos de <code>time-travel</code> para auditoria e rollback de dados históricos.",
    "duckdb": "1. Importe o DuckDB em scripts Python ou instale o binário CLI no seu computador ou servidor.<br>2. Execute queries SQL diretamente sobre gigabytes de arquivos Parquet locais ou remotos em S3: <code>SELECT * FROM 's3://bucket/*.parquet'</code>.<br>3. Gere relatórios analíticos e agregações em menos de 1 segundo sem precisar provisionar um cluster de nuvem.",
    "polars": "1. Substitua <code>import pandas as pd</code> por <code>import polars as pl</code> em seus pipelines de dados.<br>2. Utilize a API Lazy (<code>pl.scan_parquet()</code>) para permitir que o otimizador construa planos de execução eficientes.<br>3. Processe transformações pesadas utilizando todos os núcleos do processador com consumo de memória previsível.",
    "airbyte": "1. Conecte suas fontes de dados (PostgreSQL, Hubspot, Google Ads, Stripe) no painel do Airbyte.<br>2. Configure o destino para o seu Data Lake (MinIO/S3) ou banco analítico com frequência de sincronização desejada.<br>3. Monitore as replicações incrementais via Change Data Capture (CDC) sem impacto na produção.",
    "dagster": "1. Defina seus ativos de dados em código Python decorando funções com <code>@asset</code>.<br>2. Visualize o grafo completo de dependências e linhagem de dados no Dagster Webserver.<br>3. Agende execuções automáticas e materialize apenas os dados que sofreram alterações desde a última execução.",
    "dbt-core": "1. Escreva suas transformações analíticas em modelos SQL organizados por camadas (staging, intermediate, marts).<br>2. Execute <code>dbt test</code> para validar chaves primárias, unicidade e regras de negócio antes de disponibilizar as tabelas.<br>3. Gere a documentação técnica e linhagem de dados do projeto automaticamente com <code>dbt docs generate</code>.",
    "clickhouse": "1. Crie tabelas colunares com o motor <code>MergeTree</code> otimizado para séries temporais e telemetria.<br>2. Ingira milhões de eventos por segundo via Kafka, HTTP ou conectores nativos.<br>3. Conecte ferramentas de BI para rodar agregações sobre bilhões de linhas com tempo de resposta inferior a 50ms.",
    "trino": "1. Configure conectores do Trino para diferentes bases (PostgreSQL de produção, MongoDB e Data Lake Iceberg).<br>2. Escreva consultas SQL padronizadas fazendo JOIN entre tabelas de bancos distintos em uma única instrução.<br>3. Distribua o processamento analítico entre múltiplos nós workers com gerenciamento de filas de consulta.",
    "mage.ai": "1. Crie novos pipelines de engenharia de dados em blocos visuais de Python e SQL no navegador.<br>2. Valide o output de cada etapa em tempo real diretamente na interface durante o desenvolvimento.<br>3. Implante o agendamento em produção com notificações automáticas em canais do Slack/Discord.",
    "redpanda": "1. Inicie o Redpanda via container único com consumo imediato da API padrão do Apache Kafka.<br>2. Publique e consuma streams de eventos em microsserviços sem se preocupar com gargalos de JVM ou ZooKeeper.<br>3. Armazene tópicos com retenção durável em discos NVMe locais ou faça offload transparente para MinIO/S3.",
    "apache kafka": "1. Crie tópicos particionados para desacoplar a comunicação entre microsserviços da sua empresa.<br>2. Utilize produtores para registrar transações de negócio e consumidores em grupo para processamento distribuído.<br>3. Implemente Kafka Connect para ingestão contínua de bancos de dados relacionais.",
    "great expectations": "1. Defina suítes de expectativas de dados (ex: <code>expect_column_values_to_not_be_null('cliente_id')</code>).<br>2. Integre a validação no início e no fim dos pipelines de ETL no Dagster ou Airflow.<br>3. Interrompa a execução e envie alertas caso a qualidade dos dados esteja fora dos padrões esperados.",
    "feast": "1. Registre as entidades e features de Machine Learning em arquivos declarativos no repositório de MLOps.<br>2. Extraia dados históricos consistentes para treinamento de modelos sem risco de vazamento temporal.<br>3. Disponibilize features online em milissegundos via Redis para os modelos de inferência em produção.",
    "minio": "1. Faça o deploy do MinIO em servidores com discos NVMe para atuar como o storage central do seu Data Lake.<br>2. Configure políticas de acesso e chaves de API compatíveis com AWS S3 para seus pipelines e ferramentas analíticas.<br>3. Ative versionamento e replicação síncrona entre datacenters para garantir resiliência e recuperação de desastres.",
    "apache spark": "1. Submeta jobs de processamento distribuído em PySpark para transformar terabytes de logs ou imagens.<br>2. Utilize Spark Structured Streaming para ingestão e enriquecimento contínuo de streams de eventos.<br>3. Treine pipelines de Machine Learning em larga escala utilizando o módulo Spark MLlib.",
    "datahub": "1. Configure os conectores de metadados do DataHub para varrer diariamente bancos, dbt e painéis de BI.<br>2. Busque tabelas e colunas por linguagem natural para entender onde estão os dados mais confiáveis da empresa.<br>3. Identifique o impacto de alterações em esquemas de tabelas antes de aplicar migrations em produção.",
    "cube.js": "1. Modele as dimensões, medidas e agregações de negócio em esquemas semânticos padronizados.<br>2. Conecte diferentes aplicações frontend, chatbots ou painéis de BI através da API REST/GraphQL do Cube.<br>3. Aproveite o sistema de pré-agregação em memória para acelerar consultas analíticas recorrentes.",
    "apache arrow": "1. Utilize Apache Arrow para transferir dados tabulares entre diferentes processos (ex: C++ para Python) sem custo de cópia.<br>2. Escreva extensões e algoritmos analíticos em memória aproveitando instruções SIMD do processador.<br>3. Integre sistemas analíticos heterogêneos mantendo alto rendimento computacional.",
    "apache superset": "1. Conecte o Superset ao seu motor SQL (ClickHouse, Trino, DuckDB, PostgreSQL).<br>2. Construa gráficos interativos, filtros dinâmicos e painéis gerenciais no SQL Lab.<br>3. Compartilhe dashboards com a diretoria com controle de acesso granular por equipe e nível de linha (RLS).",
    "metabase": "1. Conecte o Metabase ao banco de dados ou réplica analítica da empresa em menos de 5 minutos.<br>2. Permita que equipes de produto e marketing criem perguntas visuais e gráficos sem escrever SQL.<br>3. Configure alertas automáticos por e-mail ou Slack quando métricas de vendas ou retenção baterem metas.",

    # Camada 37 - IAM / Auth
    "keycloak": "1. Instale o Keycloak e configure o Realm corporativo com as políticas de senha e MFA da organização.<br>2. Conecte suas aplicações web e mobile via protocolo OpenID Connect (OIDC) para login único (SSO).<br>3. Sincronize usuários e grupos corporativos com o Active Directory/LDAP central da empresa.",
    "authentik": "1. Faça o deploy do Authentik via Docker Compose na sua infraestrutura interna.<br>2. Utilize o Outpost integrado para colocar autenticação SSO e 2FA na frente de serviços web legados.<br>3. Configure fluxos de onboarding de usuários personalizados com suporte a chaves Passkeys/WebAuthn.",
    "zitadel": "1. Crie organizações e projetos multi-tenant para atender cada cliente corporativo da sua aplicação SaaS.<br>2. Permita que seus clientes configurem seus próprios provedores de identidade SAML/OIDC (BYO-IdP).<br>3. Controle permissões granulares de acesso com base em papéis e metadados contextuais.",
    "ory kratos": "1. Integre o SDK do Kratos no backend da sua aplicação para gerenciar cadastro, login e recuperação de conta.<br>2. Construa formulários de login customizados no frontend consumindo a API Headless com total flexibilidade visual.<br>3. Garanta sessões seguras e proteção nativa contra ataques de CSRF e credential stuffing.",
    "ory hydra": "1. Configure o Hydra como emissor oficial de tokens OAuth 2.0 e OpenID Connect na sua arquitetura de APIs.<br>2. Conecte sua tela de login proprietária para validar o consentimento e identidade do usuário.<br>3. Emita e valide tokens JWT/OAuth2 em microssegundos nos gateways de API da sua empresa.",
    "teleport": "1. Instale o agente Teleport em servidores de produção, clusters Kubernetes e instâncias de banco de dados.<br>2. Acesse a infraestrutura via terminal usando certificados efêmeros com o comando <code>tsh ssh servidor</code>.<br>3. Audite e reproduza sessões de terminal gravadas no painel web para conformidade com normas SOC2 e ISO 27001.",
    "casdoor": "1. Inicie o Casdoor e personalize a página de login com a identidade visual e logotipo da sua marca.<br>2. Ative logins sociais (Google, GitHub, Microsoft) com apenas alguns cliques no painel administrativo.<br>3. Utilize os SDKs oficiais em Python, Node.js, Go ou Java para autenticar usuários no backend.",
    "authelia": "1. Integre o Authelia ao Traefik, NGINX ou Caddy como middleware de forward-auth.<br>2. Proteja painéis internos (Grafana, Portainer, Proxmox) exigindo autenticação de dois fatores antes do acesso.<br>3. Gerencie permissões de acesso baseadas em redes de origem, grupos de usuários e recursos solicitados.",
    "supertokens": "1. Instale as bibliotecas de frontend e backend do SuperTokens no seu projeto (React, Vue, Node, Python).<br>2. Ative fluxos de autenticação sem senha via magic link ou OTP por e-mail e SMS.<br>3. Aproveite o gerenciamento seguro de sessões com rotação automática de refresh tokens contra roubo de credenciais.",
    "vaultwarden": "1. Hospede o Vaultwarden na sua VPS ou rede local com backup diário do banco SQLite criptografado.<br>2. Instale as extensões do Bitwarden nos navegadores e smartphones de todos os colaboradores.<br>3. Crie organizações e compartilhe credenciais corporativas com controle estrito de quem pode visualizar ou apenas preencher.",
    "hashicorp vault": "1. Inicialize o Vault com Shamir Keys e ative o motor de segredos <code>kv-v2</code>.<br>2. Configure suas aplicações para buscar senhas de banco e chaves de API dinâmicas em tempo de execução.<br>3. Automatize a rotação periódica de segredos e emissão de certificados TLS internos.",
    "pomerium": "1. Configure o Pomerium como proxy de borda na frente de aplicações internas e APIs privadas.<br>2. Crie políticas Zero-Trust como: 'Apenas membros do grupo Engenharia podem acessar o ambiente de staging'.<br>3. Elimine a necessidade de VPNs corporativas permitindo acesso seguro e direto pelo navegador.",
    "boundary": "1. Configure os targets de banco de dados e servidores no console do Boundary.<br>2. Autentique desenvolvedores via OIDC e conceda acesso temporário a instâncias de banco sem expor as senhas.<br>3. Estabeleça conexões seguras através do CLI <code>boundary connect</code> com trilha de auditoria completa.",
    "freeipa": "1. Configure o FreeIPA como o servidor de domínio central para todos os servidores Linux da infraestrutura.<br>2. Crie contas de usuários, grupos e políticas de sudo centralizadas sem precisar cadastrar senhas em cada máquina.<br>3. Autentique serviços e acessos SSH via Kerberos com emissão automática de certificados SSL internos.",
    "oauth2-proxy": "1. Posicione o OAuth2-Proxy entre a internet e uma ferramenta sem autenticação nativa.<br>2. Aponte o provedor de identidade para o Keycloak ou Authentik da sua organização.<br>3. Receba requisições seguras na aplicação destino com os cabeçalhos <code>X-Auth-Request-User</code> validados.",
    "pocketbase auth": "1. Inicie o PocketBase com um único comando e configure as regras de coleção no painel de administração.<br>2. Utilize o SDK em JavaScript ou Dart para autenticar usuários com e-mail/senha ou provedores OAuth2.<br>3. Aproveite as regras de acesso integradas ao banco de dados SQLite para proteger registros por usuário.",
    "dex idp": "1. Configure os conectores do Dex para autenticar contra o LDAP corporativo, GitHub ou SAML legado.<br>2. Aponte o servidor de API do Kubernetes (kube-apiserver) para validar identidades através do Dex.<br>3. Emita tokens OIDC padronizados para login de desenvolvedores em múltiplos clusters.",
    "kanidm": "1. Faça o deploy do Kanidm para gerenciar identidades corporativas com segurança de memória garantida em Rust.<br>2. Cadastre usuários e configure autenticação primária baseada em chaves de segurança FIDO2/Passkeys.<br>3. Integre com clientes Linux e servidores RADIUS para controle de acesso físico e de rede.",
    "simplewebauthn": "1. Gere desafios WebAuthn no backend da sua aplicação utilizando <code>@simplewebauthn/server</code>.<br>2. Dispare a autenticação biométrica (Face ID, Touch ID, Windows Hello) no navegador com <code>@simplewebauthn/browser</code>.<br>3. Valide a assinatura criptográfica e realize o login sem senhas com segurança invulnerável a phishing.",
    "cerbos": "1. Escreva políticas de permissão em arquivos YAML simples descrevendo ações permitidas por recurso e contexto.<br>2. Inicie o Cerbos em container ao lado do seu microsserviço como um sidecar de baixa latência.<br>3. Consulte a API do Cerbos passando o usuário, o recurso e a ação para obter a decisão de autorização em < 1ms.",

    # Camada 38 - Edge AI / Mobile
    "executorch": "1. Exporte seu modelo PyTorch treinado para o formato ExecuTorch com quantização INT8.<br>2. Integre a biblioteca C++ nos apps Android (Java/Kotlin) ou iOS (Swift) do seu produto.<br>3. Execute inferência em tempo real aproveitando a NPU do dispositivo móvel sem conexão com a internet.",
    "mediapipe": "1. Instale o SDK do MediaPipe na sua aplicação mobile, desktop ou web.<br>2. Processe streams da câmera para rastreamento de gestos, expressões faciais ou estimativa de pose em 60 FPS.<br>3. Crie experiências interativas de realidade aumentada e acessibilidade com zero processamento em nuvem.",
    "mlx": "1. Instale o MLX em computadores Mac com processadores Apple Silicon (M1/M2/M3/M4).<br>2. Carregue modelos de linguagem abertos em formato quantizado 4-bit para execução ultrarrápida.<br>3. Ajuste fino (Fine-Tuning LoRA) de modelos em poucos minutos aproveitando a memória unificada do Mac.",
    "llama.cpp": "1. Baixe o modelo LLM desejado no formato quantizado GGUF do Hugging Face.<br>2. Execute o servidor HTTP local ou CLI com o comando <code>./llama-cli -m modelo.gguf -p 'Sua pergunta'</code>.<br>3. Conecte suas aplicações locais à API compatível com OpenAI fornecida pelo <code>llama-server</code> com custo zero de tokens.",
    "whisperkit": "1. Adicione o pacote Swift do WhisperKit no projeto do seu aplicativo iOS ou macOS.<br>2. Baixe o modelo Whisper otimizado para o Neural Engine da Apple no primeiro uso.<br>3. Transcreva áudios de reuniões e comandos de voz com precisão profissional e privacidade absoluta no dispositivo.",
    "onnx runtime mobile": "1. Converta modelos de qualquer framework para o formato padrão <code>.onnx</code> com quantização móvel.<br>2. Integre o runtime no app via React Native, Flutter, Swift ou Kotlin.<br>3. Execute inferência de modelos de classificação, NLP e visão com aceleração de hardware nativa.",
    "litert": "1. Converta modelos treinados para o formato <code>.tflite</code> utilizando técnicas de quantização pós-treinamento.<br>2. Carregue o modelo no app Android utilizando o interpretador LiteRT acelerado por NNAPI/GPU.<br>3. Processe sensores, áudios e imagens em tempo real mesmo em celulares de entrada.",
    "ncnn": "1. Compile a biblioteca NCNN em C++ para a arquitetura ARM do seu dispositivo alvo.<br>2. Converta pesos de redes neurais para os formatos <code>.param</code> e <code>.bin</code> compactos.<br>3. Execute visão computacional e detecção de objetos com inicialização instantânea e consumo mínimo de bateria.",
    "mnn": "1. Converta modelos de visão e deep learning para o formato MNN otimizado.<br>2. Implemente o motor em aplicativos de comércio eletrônico, câmeras inteligentes ou quiosques interativos.<br>3. Execute inferência contínua com pipelines de aceleração Vulkan/Metal sem aquecer o dispositivo.",
    "mlc-llm": "1. Utilize o MLC-LLM para compilar pesos de modelos abertos para o seu hardware específico (GPU/NPU).<br>2. Suba o servidor de inferência local ou empacote o runtime em aplicações desktop multiplataforma.<br>3. Obtenha taxas de geração de tokens acima de 40 tokens/s em placas gráficas convencionais.",
    "webllm": "1. Importe o pacote <code>@mlc-ai/web-llm</code> na sua aplicação web em JavaScript/TypeScript.<br>2. Inicialize o modelo desejado (Llama 3, Phi-3, Gemma) diretamente na GPU do usuário via WebGPU.<br>3. Ofereça recursos avançados de chat, resumo e análise sem manter servidores de IA rodando no backend.",
    "transformers.js": "1. Instale o <code>@xenova/transformers</code> no seu projeto frontend ou extensão de navegador.<br>2. Crie pipelines de extração de embeddings, classificação de texto ou OCR com uma única linha de código.<br>3. Construa sistemas de busca vetorial semântica locais (RAG in-browser) com zero latência de rede.",
    "sherpa-onnx": "1. Baixe modelos de fala offline em português (STT) e modelos de síntese de voz (TTS).<br>2. Integre o Sherpa-ONNX em aplicativos Flutter, Android ou sistemas embarcados Raspberry Pi.<br>3. Reconheça comandos de voz e sintetize áudio em tempo real sem depender de conexão com a internet.",
    "edge impulse": "1. Conecte placas de desenvolvimento e sensores para coletar dados de vibração, áudio ou movimento.<br>2. Treine modelos de TinyML otimizados para detecção de anomalias no estúdio visual.<br>3. Exporte código C++ limpo e embarque diretamente em microcontroladores de baixíssimo consumo.",
    "apache tvm": "1. Importe modelos de deep learning de qualquer framework no compilador Apache TVM.<br>2. Execute o processo de auto-tuning para otimizar operadores matemáticos para a arquitetura de chip desejada.<br>3. Gere binários de máquina com a melhor performance computacional possível para o hardware.",
    "yolov10 mobile": "1. Treine ou baixe pesos pré-treinados do modelo YOLOv10 no formato compacto (nano ou small).<br>2. Exporte para ONNX ou NCNN eliminando as etapas de Non-Maximum Suppression (NMS).<br>3. Processe câmeras de segurança e robótica detectando dezenas de objetos a mais de 100 FPS.",
    "openvino": "1. Converta modelos de visão e linguagem para a Representação Intermediária (IR) do OpenVINO.<br>2. Execute inferência em CPUs Intel convencionais aproveitando instruções vetoriais AVX-512 e AMX.<br>3. Obtenha ganhos de performance de até 5x sem necessidade de adquirir placas de vídeo dedicadas.",
    "rknn-toolkit": "1. Conecte placas ARM equipadas com chips Rockchip RK3588 (Orange Pi 5, Rock 5B).<br>2. Converta modelos ONNX para o formato <code>.rknn</code> com quantização INT8 pelo toolkit.<br>3. Processe múltiplos canais de vídeo simultâneos com inferência de IA acelerada na NPU integrada de 6 TOPS.",
    "ggml": "1. Clone o repositório GGML e integre a biblioteca em C puro no seu projeto de engenharia de software.<br>2. Aloque tensores em buffers contíguos de memória sem custos de garbage collection ou alocação dinâmica.<br>3. Desenvolva motores de inferência customizados e ultra-leves para arquiteturas x86 e ARM.",
    "fastdeploy": "1. Instale o FastDeploy em Python ou C++ no seu ambiente de borda ou servidor local.<br>2. Selecione o modelo desejado da biblioteca oficial (+160 modelos pré-integrados de visão e OCR).<br>3. Realize o deploy com suporte automático ao backend mais rápido disponível no hardware (TensorRT, ONNX, OpenVINO).",

    # Camada 39 - LegalTech / Jurídico
    "paperless-ngx": "1. Aponte a pasta de consumo do Paperless-ngx para os scanners e uploads do escritório de advocacia.<br>2. Deixe o sistema aplicar OCR automático e classificar documentos por cliente, processo e tipo de peça.<br>3. Localize termos específicos em milhares de páginas de autos judiciais em segundos pela busca global.",
    "docuseal": "1. Suba minutas de contratos, procurações e termos de honorários na plataforma DocuSeal.<br>2. Posicione os campos de assinatura, CPF e data e envie o link para as partes via WhatsApp ou e-mail.<br>3. Baixe o PDF final assinado acompanhado do certificado de conformidade com validade jurídica plena (ICP-Brasil).",
    "stirling-pdf": "1. Abra o painel web privado do Stirling-PDF no navegador da equipe do escritório.<br>2. Comprima PDFs pesados para atender aos limites de upload dos tribunais (PJe, e-SAJ, Projudi).<br>3. Divida, junte, remova senhas e higienize metadados confidenciais com total sigilo local.",
    "docassemble": "1. Crie entrevistas interativas para coleta de dados de novos clientes e fatos do caso.<br>2. Configure a lógica jurídica condicional para inserir ou remover cláusulas conforme as respostas.<br>3. Gere minutas completas de petições iniciais e contratos em DOCX e PDF em menos de 3 minutos.",
    "twenty crm": "1. Organize o funil de novos clientes jurídicos em colunas de prospecção, proposta e fechamento no Twenty.<br>2. Registre dados processuais importantes (número CNJ, tribunal, valores de honorários combinados).<br>3. Sincronize e-mails e histórico de conversas para manter a equipe de advogados sempre alinhada.",
    "opencontracts": "1. Suba lotes de contratos de clientes para análise em auditorias de Due Diligence e M&A.<br>2. Utilize modelos de NLP para extrair automaticamente cláusulas de rescisão, foro, multas e vigência.<br>3. Exporte planilhas comparativas de riscos jurídicos economizando centenas de horas de análise manual.",
    "cryptomator": "1. Crie um cofre criptografado no seu computador dentro da pasta do Google Drive ou OneDrive.<br>2. Salve arquivos confidenciais de clientes, perícias e documentos sensíveis dentro do drive virtual.<br>3. Garanta que mesmo em caso de invasão da conta de nuvem, nenhum dado de cliente possa ser lido.",
    "veracrypt": "1. Crie um volume criptografado com chave mestra forte em um pendrive ou disco externo.<br>2. Armazene mídias probatórias, laudos periciais e gravações de investigações com algoritmos em cascata.<br>3. Monte o volume apenas quando for trabalhar nos arquivos, mantendo as provas blindadas contra perícias não autorizadas.",
    "apache tika": "1. Inicie o servidor Apache Tika via container para atuar como motor de parsing de documentos.<br>2. Envie arquivos anexados em processos judiciais (PDFs, DOCX, MSG, áudios) para a API REST do Tika.<br>3. Receba o texto limpo e metadados extraídos para indexação no banco de busca e sistemas de IA da banca.",
    "ocrmypdf": "1. Execute o OCRmyPDF em lote sobre pastas contendo processos antigos digitalizados.<br>2. Adicione camadas de texto pesquisáveis em português com correção automática de rotação de páginas.<br>3. Gere arquivos padronizados no formato PDF/A prontos para juntada e arquivamento judicial de longo prazo.",
    "vaultwarden jur": "1. Armazene com segurança as credenciais de acesso aos sistemas de todos os tribunais e portais do PJe.<br>2. Compartilhe notas seguras com PINs de certificados digitais da banca apenas com advogados autorizados.<br>3. Acesse senhas corporativas pelo navegador e celular com criptografia de ponta a ponta.",
    "mattermost jur": "1. Crie canais de comunicação dedicados para cada processo relevante ou núcleo da banca jurídica.<br>2. Discuta teses e estratégias jurídicas de casos sensíveis em uma plataforma 100% hospedada no seu servidor.<br>3. Elimine o risco de vazamentos decorrentes do uso de aplicativos de mensagens comerciais desprotegidos.",
    "nextcloud jur": "1. Crie pastas seguras para que clientes enviem documentos e laudos com link protegido por senha.<br>2. Disponibilize cópias de petições e andamentos para clientes sem enviar anexos pesados por e-mail.<br>3. Mantenha controle estrito e trilha de auditoria sobre quem acessou ou fez download de cada documento.",
    "singlefile": "1. Instale a extensão SingleFile ou utilize a ferramenta de linha de comando no seu navegador.<br>2. Ao encontrar uma evidência em rede social ou site, salve a página completa em um arquivo HTML único.<br>3. Junte o arquivo HTML como prova documental íntegra mantendo layout, imagens e carimbos originais.",
    "redact": "1. Carregue peças processuais e laudos que precisem ser disponibilizados publicamente.<br>2. Selecione nomes, CPFs, dados bancários e informações médicas para tarjamento irreversível.<br>3. Exporte o documento higienizado garantindo total conformidade com a LGPD e regras da OAB.",
    "cal.com jur": "1. Configure os horários disponíveis na agenda dos advogados respeitando compromissos e audiências.<br>2. Envie o link personalizado para clientes agendarem consultas iniciais ou reuniões de alinhamento.<br>3. Receba compromissos sincronizados automaticamente no calendário com link de videoconferência pronto.",
    "firefly iii jur": "1. Cadastre centros de custos para cada processo ou contrato de prestação de serviços da banca.<br>2. Registre entradas de honorários contratuais e separe valores destinados ao reembolso de custas processuais.<br>3. Emita relatórios financeiros detalhados para prestação de contas transparente aos clientes.",
    "formbricks jur": "1. Crie formulários interativos de triagem para captação de novos clientes no site do escritório.<br>2. Colete o relato dos fatos e documentos preliminares antes da primeira consulta com o advogado.<br>3. Receba os dados estruturados no CRM para qualificar a oportunidade e agilizar o atendimento.",
    "pdftk jur": "1. Utilize o comando <code>pdftk</code> em scripts de terminal para mesclar a petição inicial com todos os anexos numerados.<br>2. Divida autos pesados em blocos de páginas menores para cumprir as regras de tamanho dos portais judiciais.<br>3. Automatize a montagem de cadernos processuais completos em menos de 1 segundo.",
    "libreoffice cli": "1. Crie minutas padrão com marcadores de substituição em arquivos DOCX.<br>2. Execute o LibreOffice em modo headless via scripts Python para gerar contratos preenchidos em PDF.<br>3. Automatize a produção em lote de procurações e termos de honorários para centenas de clientes."
}

def obter_passo_a_passo(nome, subtitulo, rank):
    # Procura por chave correspondente no mapa
    chave = nome.lower().strip()
    for k, v in USO_PRATICO_MAP.items():
        if k in chave or chave in k:
            return v
    
    # Fallback contextual inteligente
    return f"1. Instale e configure o componente <code>{nome}</code> no seu ambiente corporativo ou servidor local.<br>2. Integre o motor aos seus fluxos de trabalho, conectando APIs, scripts de automação ou painéis de controle.<br>3. Monitore a operação em produção para garantir soberania tecnológica, redução de custos e conformidade."

def refatorar_arquivo(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    alterado = False

    # 1. Garantir CSS para how-to-use
    if ".how-to-use {" not in content:
        content = content.replace("</style>", f"{CSS_HOW_TO_USE}\n</style>")
        alterado = True
    else:
        # Atualizar a regra no CSS para garantir width 100% e display flex
        content = re.sub(
            r'\.how-to-use\s*\{[^}]*\}',
            '.how-to-use { display:flex; flex-direction:column; gap:8px; padding-top:14px; border-top:1px dashed var(--rule-soft); width:100%; }',
            content
        )
        alterado = True

    # 2. Processar cada <div class="entry"> no documento
    # Vamos usar regex para capturar cada entry
    def processar_entry(match):
        entry_text = match.group(0)

        # Se ja tem how-to-use fora de .cols, verificar se esta ok
        # Se how-to-use esta DENTRO de cols/block:
        # Vamos extrair o conteudo de how-to-use
        how_to_use_match = re.search(r'<div class="how-to-use"[^>]*>(.*?)</div>\s*</div>\s*<div class="block">', entry_text, re.DOTALL)
        if not how_to_use_match:
            how_to_use_match = re.search(r'<div class="how-to-use"[^>]*>(.*?)</div>', entry_text, re.DOTALL)

        how_to_use_content = ""
        if how_to_use_match:
            raw_inner = how_to_use_match.group(1)
            # Limpar tags extras se houver
            raw_inner = re.sub(r'style="[^"]*"', '', raw_inner)
            # Extrair paragrafo
            p_match = re.search(r'<p[^>]*>(.*?)</p>', raw_inner, re.DOTALL)
            if p_match:
                p_text = p_match.group(1).strip()
                how_to_use_content = f"""
          <div class="how-to-use">
            <span class="label">3. Como Usar no Dia a Dia (Passo a Passo Prático)</span>
            <p>{p_text}</p>
          </div>"""
            # Remover o how-to-use original de dentro do entry_text
            entry_text = re.sub(r'<div class="how-to-use"[^>]*>.*?</div>', '', entry_text, flags=re.DOTALL)
        else:
            # Não tem how-to-use: vamos gerar a partir dos dados do card
            nome_m = re.search(r'<h3>(.*?)(?:·|</h3>)', entry_text)
            rank_m = re.search(r'<div class="entry-rank">(\d+)</div>', entry_text)
            nome = nome_m.group(1).strip() if nome_m else "Ferramenta"
            rank = int(rank_m.group(1)) if rank_m else 1
            passo = obter_passo_a_passo(nome, "", rank)
            how_to_use_content = f"""
          <div class="how-to-use">
            <span class="label">3. Como Usar no Dia a Dia (Passo a Passo Prático)</span>
            <p>{passo}</p>
          </div>"""

        # Agora garantir que how-to-use seja inserido LOGO APÓS o fechamento de .cols (antes de fechar .entry-body)
        # Procuramos o fechamento de .cols: </div>\s*</div>\s*</div> (cols -> entry-body -> entry)
        # Vamos substituir o final de entry-body:
        # A estrutura padrao termina com </div> (fecha cols) seguido de </div> (fecha entry-body) seguido de </div> (fecha entry)
        # Vamos achar onde .cols fecha
        entry_text = re.sub(r'(</div>\s*</div>\s*)(</div>\s*</div>\s*)$', r'\1' + how_to_use_content + r'\n        </div>\n      </div>', entry_text.strip())

        return entry_text

    # Substituir cada bloco .entry
    new_content = re.sub(r'<div class="entry">.*?</div>\s*</div>\s*(?=(?:<!-- \d+|\s*<div class="entry">|\s*</div>\s*</section>|\s*</div>\s*<footer>))', processar_entry, content, flags=re.DOTALL)

    if new_content != content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        return True
    return alterado

def main():
    arquivos = [f for f in os.listdir(OUTPUT_DIR) if f.endswith(".html") and f != "index.html"]
    print(f"[*] Padronizando e enriquecendo 'Como Usar no Dia a Dia' em {len(arquivos)} arquivos...")

    atualizados = 0
    for arq in sorted(arquivos):
        p = os.path.join(OUTPUT_DIR, arq)
        if refatorar_arquivo(p):
            atualizados += 1
            print(f"  -> [✓] Atualizado: {arq}")

    print(f"\n[🎉] Finalizado com sucesso! {atualizados} arquivos foram atualizados.")

if __name__ == "__main__":
    main()
