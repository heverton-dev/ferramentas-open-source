# -*- coding: utf-8 -*-
"""
Compilador das 5 novas camadas (35 a 39) com 20 fichas completas cada.
Total: 100 fichas técnicas detalhadas e padronizadas.
"""
import os
import sys
from gerar_camadas_35_39_completas import render_html, console_utf8

console_utf8()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = os.path.join(BASE_DIR, "output", "listas-open-source")

# ==============================================================================
# CAMADA 35: CYBER THREAT INTELLIGENCE & SOC SOBERANO
# ==============================================================================
items_35 = [
    {
        "rank": 1, "nome": "Wazuh", "subtitulo": "XDR, SIEM & Monitoramento de Endpoints",
        "substitui": "Splunk / CrowdStrike", "categoria": "XDR + SIEM Endpoint",
        "economia": "-$ 35.000 a $ 90.000 / ano", "licenca": "GPLv2", "kind": "SIEM / XDR",
        "o_que_faz": "Plataforma unificada de <strong>monitoramento de integridade de arquivos (FIM), detecção de intrusão em endpoints, análise de logs centralizada e conformidade PCI-DSS/LGPD</strong>.",
        "como_funciona": "Agentes leves em nós Linux/Windows transmitem telemetria criptografada para o Wazuh Manager, que cruza dados com a matriz MITRE ATT&CK.",
        "quickstart": "curl -sO https://packages.wazuh.com/4.8/wazuh-install.sh\nsudo bash wazuh-install.sh -a",
        "specs": "Agente < 35 MB RAM · Escala até 100k+ nós",
        "veredito": "A espinha dorsal indispensável para qualquer SOC corporativo soberano.",
        "github": "https://github.com/wazuh/wazuh"
    },
    {
        "rank": 2, "nome": "TheHive", "subtitulo": "Orquestração e Resposta a Incidentes (SOAR)",
        "substitui": "IBM Resilient / Splunk SOAR", "categoria": "Gestão de Incidentes (SOAR)",
        "economia": "-$ 20.000 / ano", "licenca": "AGPLv3", "kind": "SOAR",
        "o_que_faz": "Central de resposta e triagem de incidentes cibernéticos com suporte a playbooks dinâmicos, colaboração de múltiplos analistas e trilha forense auditável.",
        "como_funciona": "Recebe alertas de SIEMs via webhooks, gera casos de investigação e aciona enriquecimento de observáveis automaticamente.",
        "quickstart": "docker run -d -p 9000:9000 thehiveproject/thehive:latest",
        "specs": "Playbooks Dinâmicos · Multi-analista em tempo real",
        "veredito": "Transforma alertas caóticos em investigações estruturadas e rastreáveis.",
        "github": "https://github.com/TheHive-Project/TheHive"
    },
    {
        "rank": 3, "nome": "Cortex", "subtitulo": "Motor de Análise de Observáveis & IOCs",
        "substitui": "Recorded Future / VirusTotal Ent", "categoria": "Análise de Observáveis",
        "economia": "-$ 15.000 / ano", "licenca": "AGPLv3", "kind": "IOC ANALYZER",
        "o_que_faz": "Motor de enriquecimento que roda mais de 100 analisadores automáticos sobre hashes, IPs, domínios e e-mails suspeitos em milissegundos.",
        "como_funciona": "Integrado ao TheHive ou via API REST, recebe um observável e dispara consultas simultâneas a feeds de inteligência de ameaças.",
        "quickstart": "docker run -d -p 9001:9001 thehiveproject/cortex:latest",
        "specs": "+100 Analisadores e Responders Nativos",
        "veredito": "Elimina tarefas repetitivas e economiza centenas de horas de analistas de segurança.",
        "github": "https://github.com/TheHive-Project/Cortex"
    },
    {
        "rank": 4, "nome": "Suricata", "subtitulo": "IDS/IPS de Rede & Threat Hunting em 10Gbps",
        "substitui": "Cisco Firepower / Palo Alto IDS", "categoria": "IDS/IPS de Rede",
        "economia": "-$ 18.000 / ano", "licenca": "GPLv2", "kind": "IDS / IPS",
        "o_que_faz": "Motor de detecção e prevenção de intrusão de rede de altíssimo rendimento, inspecionando pacotes e tráfego TLS/HTTP em velocidades de 10Gbps a 40Gbps.",
        "como_funciona": "Analisa tráfego em tempo real cruzando com assinaturas Emerging Threats e exportando telemetria estruturada no formato JSON EVE.",
        "quickstart": "sudo apt install suricata -y\nsudo suricata-update && sudo systemctl start suricata",
        "specs": "10Gbps+ Line Rate · Multithread nativo em C",
        "veredito": "O padrão industrial para inspeção profunda de pacotes (DPI) e defesa de borda.",
        "github": "https://github.com/OISF/suricata"
    },
    {
        "rank": 5, "nome": "Zeek (Bro)", "subtitulo": "Análise Comportamental e Metadados de Rede",
        "substitui": "ExtraHop / Darktrace", "categoria": "Network Security Monitoring",
        "economia": "-$ 25.000 / ano", "licenca": "BSD-3-Clause", "kind": "NSM / METADATA",
        "o_que_faz": "Transforma fluxos de pacotes brutos em registros estruturados de altíssimo nível (conexões, certificados SSL, transações DNS, sessões HTTP).",
        "como_funciona": "Linguagem de script orientada a eventos que analisa tráfego de rede e detecta anomalias comportamentais sem depender só de assinaturas estáticas.",
        "quickstart": "sudo apt install zeek -y\nzeek -i eth0",
        "specs": "Extração de metadados sem perda de pacotes · Scripting Turing-complete",
        "veredito": "Indispensável para caça ativa a ameaças e auditoria profunda de rede.",
        "github": "https://github.com/zeek/zeek"
    },
    {
        "rank": 6, "nome": "MISP", "subtitulo": "Plataforma de Compartilhamento de Threat Intelligence",
        "substitui": "Anomali ThreatStream / Mandiant", "categoria": "Threat Intel Sharing",
        "economia": "-$ 30.000 / ano", "licenca": "GPLv3", "kind": "CTI / MISP",
        "o_que_faz": "Plataforma global para coleta, armazenamento, correlação e distribuição de indicadores de comprometimento (IoCs) e inteligência de ciberameaças.",
        "como_funciona": "Sincroniza feeds governamentais e comunitários (CERTs, ISACs), correlacionando eventos com atributos técnicos e matrizes de ataque.",
        "quickstart": "docker run -d -p 8080:80 coolacid/misp-docker:latest",
        "specs": "Taxonomias Galaxy MITRE · Federação P2P de Ameaças",
        "veredito": "O padrão mundial de intercâmbio de inteligência entre times de segurança e governos.",
        "github": "https://github.com/MISP/MISP"
    },
    {
        "rank": 7, "nome": "OpenCTI", "subtitulo": "Plataforma Unificada de Gestão de CTI (STIX2)",
        "substitui": "ThreatConnect / ThreatQuotient", "categoria": "Plataforma CTI",
        "economia": "-$ 22.000 / ano", "licenca": "Apache-2.0", "kind": "CTI PLATFORM",
        "o_que_faz": "Estrutura e visualiza o conhecimento operacional e tático de ameaças cibernéticas com suporte nativo aos padrões STIX2 e grafos de conhecimento.",
        "como_funciona": "Conecta fontes de dados abertas e proprietárias em um grafo interativo mapeando grupos de atores (APTs), malwares e campanhas.",
        "quickstart": "docker compose -f docker-compose.yml up -d # Usando repositório oficial",
        "specs": "Grafo STIX2 · Conectores para Wazuh, TheHive e MISP",
        "veredito": "A interface mais elegante e moderna para analistas de inteligência estratégica.",
        "github": "https://github.com/OpenCTI-Platform/opencti"
    },
    {
        "rank": 8, "nome": "Velociraptor", "subtitulo": "Forense Digital Avançada & Endpoint Hunting",
        "substitui": "EnCase / Tanium Enterprise", "categoria": "Forense & Hunting",
        "economia": "-$ 28.000 / ano", "licenca": "AGPLv3", "kind": "DFIR / HUNTING",
        "o_que_faz": "Permite consultar o estado de milhares de endpoints em segundos usando consultas VQL (Velociraptor Query Language) para coleta forense e triagem.",
        "como_funciona": "Executa caça a artefatos (MFT, memória, registro, processos) diretamente no host remoto com velocidade sem precedentes.",
        "quickstart": "./velociraptor-v0.7.0-linux-amd64 gui",
        "specs": "VQL Expressiva · Varredura de 50.000 máquinas em < 2 min",
        "veredito": "A melhor ferramenta forense e de resposta rápida a incidentes da atualidade.",
        "github": "https://github.com/Velocidex/velociraptor"
    },
    {
        "rank": 9, "nome": "Falco", "subtitulo": "Segurança de Runtime em Nuvem & Kubernetes (eBPF)",
        "substitui": "Sysdig Secure / Aqua Security", "categoria": "Runtime Security (eBPF)",
        "economia": "-$ 15.000 / ano", "licenca": "Apache-2.0", "kind": "EBPF RUNTIME",
        "o_que_faz": "Monitora chamadas de sistema do kernel Linux via eBPF em tempo real para detectar comportamentos anômalos em containers e clusters Kubernetes.",
        "como_funciona": "Intercepta syscalls no kernel e gera alertas imediatos se um container abrir um shell inesperado ou tentar ler arquivos sensíveis do host.",
        "quickstart": "curl -s https://falco.org/repo/falcosecurity-packages.asc | sudo gpg --dearmor -o /usr/share/keyrings/falco-archive-keyring.gpg\nsudo apt install falco -y",
        "specs": "Overhead < 1% de CPU · Motor eBPF graduado na CNCF",
        "veredito": "Padrão de fato para proteção de infraestruturas em nuvem e containers.",
        "github": "https://github.com/falcosecurity/falco"
    },
    {
        "rank": 10, "nome": "Sigma", "subtitulo": "Padrão Universal e Portável de Regras de Detecção",
        "substitui": "Regras Proprietárias de SIEM", "categoria": "Padrão de Detecção",
        "economia": "-$ 10.000 / ano", "licenca": "LGPL-2.1", "kind": "DETECTION RULES",
        "o_que_faz": "Linguagem genérica em formato YAML para descrever assinaturas de ataques em logs, que pode ser convertida para qualquer SIEM (Wazuh, Splunk, Elastic, QRadar).",
        "como_funciona": "Escreva a regra de detecção uma única vez em Sigma e use o compilador pySigma para exportar para o formato do seu SIEM.",
        "quickstart": "pip install sigmatools\nsigmac -t splunk -c sysmon rule.yml",
        "specs": "+3.000 regras comunitárias validadas",
        "veredito": "Elimina a dependência de fornecedores de SIEM com regras universais e versionadas em Git.",
        "github": "https://github.com/SigmaHQ/sigma"
    },
    {
        "rank": 11, "nome": "Shuffle", "subtitulo": "Plataforma de Automação de SOC No-Code (SOAR)",
        "substitui": "Tines / Torq", "categoria": "Automação No-Code SOAR",
        "economia": "-$ 18.000 / ano", "licenca": "AGPLv3", "kind": "NO-CODE SOAR",
        "o_que_faz": "Orquestrador visual e aberto para automação de tarefas de segurança, conectando ferramentas como Wazuh, TheHive, virustotal e firewalls.",
        "como_funciona": "Interface de arrastar e soltar (estilo n8n focado em segurança) com centenas de apps prontos para isolar máquinas e bloquear IPs.",
        "quickstart": "docker compose -f docker-compose.yml up -d # No repositório Shuffle",
        "specs": "Conectores OpenAPI · Suporte a subfluxos e IA",
        "veredito": "Traz a agilidade da automação moderna para times de segurança com orçamento enxuto.",
        "github": "https://github.com/Shuffle/Shuffle"
    },
    {
        "rank": 12, "nome": "Cuckoo Sandbox", "subtitulo": "Análise Dinâmica e Automatizada de Malware",
        "substitui": "Joe Sandbox / VMRay", "categoria": "Malware Analysis Sandbox",
        "economia": "-$ 12.000 / ano", "licenca": "GPLv3", "kind": "SANDBOX",
        "o_que_faz": "Executa arquivos e URLs suspeitas dentro de máquinas virtuais isoladas e monitora todo o comportamento (chamadas de API, rede, arquivos gerados).",
        "como_funciona": "Injeta ganchos de monitoramento no Windows/Linux convidado e gera um relatório forense completo com capturas de tela e dump de memória.",
        "quickstart": "pip install -U cuckoo\ncuckoo community && cuckoo",
        "specs": "Extração de tráfego PCAP · Dump de memória Volatility",
        "veredito": "Essencial para análise de anexos suspeitos e payloads desconhecidos.",
        "github": "https://github.com/cuckoosandbox/cuckoo"
    },
    {
        "rank": 13, "nome": "YARA", "subtitulo": "O Padrão para Classificação e Detecção de Malware",
        "substitui": "Motores AV Proprietários", "categoria": "Pattern Matching de Binários",
        "economia": "Incalculável", "licenca": "BSD-3-Clause", "kind": "MALWARE PATTERNS",
        "o_que_faz": "Permite criar descrições baseadas em padrões textuais e binários para identificar e classificar famílias inteiras de malwares.",
        "como_funciona": "Varre arquivos, processos em memória ou discos buscando assinaturas hexadecimais, strings e expressões regulares em microssegundos.",
        "quickstart": "yara -r minha_regra.yar /pasta/arquivos_suspeitos",
        "specs": "Motor C ultra-rápido · Integrado ao Wazuh e Suricata",
        "veredito": "A ferramenta mais fundamental do planeta para caçadores de malware e analistas de DFIR.",
        "github": "https://github.com/VirusTotal/yara"
    },
    {
        "rank": 14, "nome": "BloodHound", "subtitulo": "Mapeamento de Caminhos de Ataque em Active Directory",
        "substitui": "SpecterOps Enterprise", "categoria": "Active Directory Security",
        "economia": "-$ 15.000 / ano", "licenca": "GPLv3", "kind": "AD GRAPH ATTACK",
        "o_que_faz": "Mapeia visualmente relações ocultas e caminhos de escalação de privilégios dentro do Active Directory (AD) e ambientes de nuvem Azure/Entra ID.",
        "como_funciona": "Utiliza teoria dos grafos (Neo4j) para revelar conexões de controle de acesso que permitem a um invasor atingir privilégio de Domain Admin.",
        "quickstart": "docker compose -f docker-compose.yml up -d # BloodHound CE",
        "specs": "Modelagem em Grafos Neo4j · Suporte a Azure & AWS",
        "veredito": "A melhor ferramenta para identificar e cortar caminhos de invasão no AD antes que sejam explorados.",
        "github": "https://github.com/BloodHoundAD/BloodHound"
    },
    {
        "rank": 15, "nome": "Trivy", "subtitulo": "Scanner Universal de Vulnerabilidades e Misconfig",
        "substitui": "Snyk Container / Prisma Cloud", "categoria": "Vulnerability Scanner",
        "economia": "-$ 12.000 / ano", "licenca": "Apache-2.0", "kind": "CONTAINER SECURITY",
        "o_que_faz": "Varre imagens de containers, sistemas de arquivos, repositórios Git e arquivos de infraestrutura como código (Terraform, K8s) em busca de CVEs e segredos.",
        "como_funciona": "Executa em CI/CD ou terminal local consultando uma base consolidada de vulnerabilidades com precisão cirúrgica e zero falsos positivos.",
        "quickstart": "curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh | sh\ntrivy image nginx:latest",
        "specs": "Varredura em < 5 segundos · Suporte a SBOM CycloneDX/SPDX",
        "veredito": "O scanner de segurança mais leve, rápido e confiável para esteiras de DevOps modernas.",
        "github": "https://github.com/aquasecurity/trivy"
    },
    {
        "rank": 16, "nome": "Gitleaks", "subtitulo": "Detecção de Segredos e Credenciais em Código",
        "substitui": "GitGuardian Enterprise", "categoria": "Secret Detection",
        "economia": "-$ 8.000 / ano", "licenca": "MIT", "kind": "SECRET SCANNER",
        "o_que_faz": "Audita históricos inteiros do Git e diffs de commits para detectar senhas, tokens de API, chaves privadas SSH e certificados vazados acidentalmente.",
        "como_funciona": "Binário ultrarrápido em Go que aplica regras de entropia e expressões regulares para barrar commits comprometidos via hook pre-commit.",
        "quickstart": "brew install gitleaks # ou download do binário\ngitleaks detect --verbose",
        "specs": "Varre 10.000 commits em < 3 segundos",
        "veredito": "O guardião obrigatório que impede que credenciais da empresa cheguem ao GitHub público.",
        "github": "https://github.com/gitleaks/gitleaks"
    },
    {
        "rank": 17, "nome": "Arkime (Moloch)", "subtitulo": "Captura e Indexação de Pacotes em Larga Escala",
        "substitui": "RSA NetWitness", "categoria": "Full Packet Capture (FPC)",
        "economia": "-$ 24.000 / ano", "licenca": "Apache-2.0", "kind": "PACKET CAPTURE",
        "o_que_faz": "Sistema de captura completa de pacotes (PCAP), indexação e visualização que permite inspecionar sessões de rede passadas com velocidade extrema.",
        "como_funciona": "Captura tráfego em tempo real, indexa cabeçalhos no OpenSearch/Elasticsearch e armazena os pacotes gravados em disco de forma otimizada.",
        "quickstart": "docker run -d -p 8005:8005 arkime/arkime",
        "specs": "Capacidade de petabytes · Busca em bilhões de sessões em segundos",
        "veredito": "A gravação definitiva de 'caixa preta' para perícia detalhada após uma invasão.",
        "github": "https://github.com/arkime/arkime"
    },
    {
        "rank": 18, "nome": "DefectDojo", "subtitulo": "Plataforma de Gestão de Vulnerabilidades (ASPM)",
        "substitui": "Brinqa / ThreadFix", "categoria": "Gestão de Vulnerabilidades",
        "economia": "-$ 16.000 / ano", "licenca": "BSD-3-Clause", "kind": "ASPM / VULN MGT",
        "o_que_faz": "Consolida, desduplica e rastreia vulnerabilidades encontradas por dezenas de ferramentas diferentes (Trivy, SonarQube, ZAP, OpenVAS) em um único dashboard.",
        "como_funciona": "Recebe relatórios de segurança de pipelines CI/CD, correlaciona falhas repetidas e mede o tempo médio de correção (MTTR).",
        "quickstart": "git clone https://github.com/DefectDojo/django-DefectDojo\ncd django-DefectDojo && ./dc-build.sh && ./dc-up.sh",
        "specs": "+150 Importadores de Scanners · Métricas de SLA",
        "veredito": "O ponto central de governança de segurança de aplicações e conformidade para CISOs.",
        "github": "https://github.com/DefectDojo/django-DefectDojo"
    },
    {
        "rank": 19, "nome": "Greenbone (OpenVAS)", "subtitulo": "Scanner de Vulnerabilidades de Rede e Ativos",
        "substitui": "Nessus Professional / Qualys", "categoria": "Network Vulnerability Scanner",
        "economia": "-$ 9.000 / ano", "licenca": "GPLv2", "kind": "NETWORK VULN SCANNER",
        "o_que_faz": "Varre redes empresariais, portas abertas, servidores e firewalls para identificar vulnerabilidades conhecidas, serviços desatualizados e falhas de configuração.",
        "como_funciona": "Executa testes de vulnerabilidade de rede (NVTs) atualizados diariamente contra os alvos selecionados e emite relatórios técnicos de remediação.",
        "quickstart": "docker compose -f docker-compose.yml up -d # Greenbone Community Containers",
        "specs": "Feed com +100.000 testes de vulnerabilidade",
        "veredito": "O scanner de rede mais tradicional e maduro do mundo open-source.",
        "github": "https://github.com/greenbone/openvas-scanner"
    },
    {
        "rank": 20, "nome": "Atomic Red Team", "subtitulo": "Testes Automatizados de Simulação de Adversários",
        "substitui": "AttackIQ / Cymulate (BAS)", "categoria": "Breach & Attack Simulation",
        "economia": "-$ 20.000 / ano", "licenca": "MIT", "kind": "ATTACK SIMULATION",
        "o_que_faz": "Biblioteca de testes de segurança automatizados e simples, mapeados diretamente para cada técnica e tática da matriz MITRE ATT&CK.",
        "como_funciona": "Permite que times de segurança executem testes controlados de ataque para verificar se suas regras de SIEM e alertas estão realmente funcionando.",
        "quickstart": "Import-Module Invoke-AtomicRedTeam\nInvoke-AtomicTest T1003.001 # Testa dump de LSASS",
        "specs": "Testes mapeados 1:1 com MITRE ATT&CK",
        "veredito": "A forma mais rápida de validar na prática se o seu SOC está realmente detectando ameaças.",
        "github": "https://github.com/redcanaryco/atomic-red-team"
    }
]

html_35 = render_html(
    35, "Camada 35 · Cibersegurança & Defesa Ativa",
    "Cyber Threat Intelligence & SOC Soberano",
    "O arsenal definitivo de <strong>SIEM, XDR, SOAR, IDS/IPS e Threat Intelligence</strong>: como montar um Centro de Operações de Segurança (SOC) empresarial 100% soberano, substituindo Splunk, CrowdStrike, SentinelOne e IBM QRadar.",
    ["<b>20</b> tecnologias auditadas", "<b>Economia:</b> -$ 30.000 a $ 150.000 / ano", "<b>Conformidade:</b> LGPD, PCI-DSS & ISO 27001"],
    {"accent": "#8E2436", "accent_soft": "#F9EBEF", "accent_dark": "#E0788C", "accent_dark_soft": "#33151D"},
    items_35
)
with open(os.path.join(OUTPUT_DIR, "35-soc-siem-cyber-threat-intelligence.html"), "w", encoding="utf-8") as f:
    f.write(html_35)
print("[✓] Camada 35 gerada com 20 fichas completas.")

# ==============================================================================
# CAMADA 36: ENGENHARIA DE DADOS & LAKEHOUSE SOBERANO
# ==============================================================================
items_36 = [
    {
        "rank": 1, "nome": "Apache Iceberg", "subtitulo": "O Formato Aberto de Tabela para Lakehouse",
        "substitui": "Databricks Delta Lake Fechado", "categoria": "Tabela de Lakehouse",
        "economia": "-$ 40.000 / ano", "licenca": "Apache-2.0", "kind": "TABLE FORMAT",
        "o_que_faz": "Formato aberto de tabela de alto desempenho para conjuntos massivos de dados analíticos, com suporte a transações ACID completas e time-travel.",
        "como_funciona": "Gerencia arquivos Parquet através de metadados em árvore, permitindo que motores como DuckDB, Trino e Spark leiam e gravem concorrentemente.",
        "quickstart": "pip install pyiceberg\nfrom pyiceberg.catalog import load_catalog",
        "specs": "Evolução de esquema sem rewrite · Particionamento oculto",
        "veredito": "O padrão adotado por toda a indústria para fugir do lock-in de fornecedores de nuvem.",
        "github": "https://github.com/apache/iceberg"
    },
    {
        "rank": 2, "nome": "DuckDB", "subtitulo": "O Motor OLAP In-Process em C++",
        "substitui": "Snowflake / BigQuery", "categoria": "Motor OLAP Embutido",
        "economia": "-$ 30.000 / ano", "licenca": "MIT", "kind": "OLAP ENGINE",
        "o_que_faz": "Motor de banco de dados analítico colunar embutido, executando queries SQL sobre gigabytes de arquivos Parquet e CSVs em milissegundos.",
        "como_funciona": "Roda no mesmo processo da aplicação sem servidor dedicado, vetorizando consultas em todos os núcleos da CPU.",
        "quickstart": "import duckdb\nduckdb.sql(\"SELECT * FROM 'dados/*.parquet' WHERE valor > 100\").show()",
        "specs": "Zero dependências · Leitura direta de S3 e PostgreSQL",
        "veredito": "O SQLite dos dados analíticos: substitui clusters pesados de nuvem para a maioria dos casos de uso.",
        "github": "https://github.com/duckdb/duckdb"
    },
    {
        "rank": 3, "nome": "Polars", "subtitulo": "DataFrames Multithread Ultra-Rápidos em Rust",
        "substitui": "Pandas / Clusters Spark Pequenos", "categoria": "DataFrame Engine",
        "economia": "-$ 15.000 / ano", "licenca": "MIT", "kind": "DATAFRAMES",
        "o_que_faz": "Biblioteca de DataFrames em Rust projetada para processar milhões de linhas em segundos com uso eficiente de memória e avaliação preguiçosa (LazyFrame).",
        "como_funciona": "Utiliza o Apache Arrow na memória e otimiza a árvore de execução com paralelismo nativo em todas as CPUs.",
        "quickstart": "pip install polars\nimport polars as pl\ndf = pl.scan_parquet('dados.parquet').filter(pl.col('status') == 'OK').collect()",
        "specs": "50x mais rápido que Pandas · Otimizador de consultas integrado",
        "veredito": "A substituição moderna e mandatória para pipelines de dados em Python.",
        "github": "https://github.com/pola-rs/polars"
    },
    {
        "rank": 4, "nome": "Airbyte", "subtitulo": "O Extrator Universal de Ingestão de Dados (ELT)",
        "substitui": "Fivetran / Stitch Data", "categoria": "Ingestão ELT (+300 Conectores)",
        "economia": "-$ 35.000 / ano", "licenca": "ELv2 / MIT", "kind": "ELT INGESTION",
        "o_que_faz": "Sincroniza dados de mais de 300 fontes (bancos de dados, CRMs, APIs de marketing, planilhas) direto para o seu Data Lake ou Data Warehouse.",
        "como_funciona": "Executa conectores isolados em containers com suporte a Change Data Capture (CDC) em tempo real sem sobrecarregar bancos de produção.",
        "quickstart": "docker run -d -p 8000:8000 airbyte/airbyte-server",
        "specs": "+300 Conectores Prontos · CDC Nativo com Debezium",
        "veredito": "Acaba com a cobrança abusiva por volume de linhas sincronizadas (MAR) de ferramentas proprietárias.",
        "github": "https://github.com/airbytehq/airbyte"
    },
    {
        "rank": 5, "nome": "Dagster", "subtitulo": "Orquestrador de Ativos de Dados Conhecidos (Software-Defined Assets)",
        "substitui": "Prefect / Astronomer Cloud", "categoria": "Orquestração de Dados",
        "economia": "-$ 25.000 / ano", "licenca": "Apache-2.0", "kind": "ORCHESTRATOR",
        "o_que_faz": "Orquestrador moderno centrado em ativos de dados (tabelas, modelos de ML, relatórios) em vez de focar apenas em tarefas operacionais cegas.",
        "como_funciona": "Rastreia a linhagem completa de dados, executa testes de integridade e suporta re-execução incremental declarativa.",
        "quickstart": "pip install dagster dagster-webserver\ndagster dev",
        "specs": "Linhagem de dados visual · Testabilidade local em CI/CD",
        "veredito": "O sucessor conceitual superior ao Apache Airflow tradicional.",
        "github": "https://github.com/dagster-io/dagster"
    },
    {
        "rank": 6, "nome": "dbt-core", "subtitulo": "Transformação de Dados em SQL & Testes de Qualidade",
        "substitui": "dbt Cloud", "categoria": "Transformação SQL",
        "economia": "-$ 18.000 / ano", "licenca": "Apache-2.0", "kind": "DATA TRANSFORMATION",
        "o_que_faz": "Permite que analistas e engenheiros escrevam transformações de dados em SQL com controle de versão, documentação automática e testes automatizados.",
        "como_funciona": "Compila código SQL com templates Jinja e executa diretamente dentro do motor analítico de destino (DuckDB, Postgres, Trino, ClickHouse).",
        "quickstart": "pip install dbt-duckdb\ndbt init meu_projeto && dbt run",
        "specs": "Testes de unicidade e nulidade nativos · DAGs automáticas",
        "veredito": "O padrão universal para a camada 'T' do pipeline ELT.",
        "github": "https://github.com/dbt-labs/dbt-core"
    },
    {
        "rank": 7, "nome": "ClickHouse", "subtitulo": "Banco Colunar Real-Time para Analytics Pesado",
        "substitui": "Amazon Redshift / Snowflake", "categoria": "Banco Colunar Real-Time",
        "economia": "-$ 50.000 / ano", "licenca": "Apache-2.0", "kind": "REAL-TIME OLAP",
        "o_que_faz": "Banco de dados orientado a colunas capaz de processar bilhões de linhas e petabytes de dados por segundo em hardware comum.",
        "como_funciona": "Armazena dados de forma compactada por coluna com algoritmos de compressão avançados e paralelismo massivo em tempo real.",
        "quickstart": "curl https://clickhouse.com/ | sh\n./clickhouse server",
        "specs": "Compressão de até 10x · Processamento de 100M+ linhas/s por core",
        "veredito": "O motor mais veloz do mundo para telemetria, logs e analítica em tempo real.",
        "github": "https://github.com/ClickHouse/ClickHouse"
    },
    {
        "rank": 8, "nome": "Trino (Presto)", "subtitulo": "Motor SQL Distribuído para Consultas Federadas",
        "substitui": "Amazon Athena / Dremio", "categoria": "Motor SQL Distribuído",
        "economia": "-$ 45.000 / ano", "licenca": "Apache-2.0", "kind": "FEDERATED SQL",
        "o_que_faz": "Permite consultar dados distribuídos em múltiplos sistemas (S3, Iceberg, PostgreSQL, MongoDB, Kafka) usando uma única query SQL padrão.",
        "como_funciona": "Arquitetura MPP (Massively Parallel Processing) em memória que divide queries complexas em nós coordenadores e workers sem mover os dados de lugar.",
        "quickstart": "docker run -d -p 8080:8080 trinodb/trino:latest",
        "specs": "Suporte a Iceberg, Delta e Hudi · Escala até milhares de nós",
        "veredito": "A ferramenta definitiva para consultas federadas sobre Data Lakes massivos.",
        "github": "https://github.com/trinodb/trino"
    },
    {
        "rank": 9, "nome": "Mage.ai", "subtitulo": "Orquestrador de Dados Moderno com Assistência de IA",
        "substitui": "Apache Airflow Clássico", "categoria": "Orquestrador Moderno",
        "economia": "-$ 20.000 / ano", "licenca": "Apache-2.0", "kind": "AI ORCHESTRATOR",
        "o_que_faz": "Plataforma de integração e orquestração de pipelines que combina a facilidade de notebooks interativos com a robustez de produção.",
        "como_funciona": "Permite construir pipelines em blocos modulares de Python, SQL e R com preview em tempo real e geração de código via IA.",
        "quickstart": "docker run -it -p 6789:6789 -v $(pwd):/home/src mageai/mageai",
        "specs": "Preview instantâneo de dados por bloco · Integração nativa com dbt",
        "veredito": "Desenvolver pipelines de dados com Mage é 10x mais produtivo que lutar com a complexidade do Airflow legado.",
        "github": "https://github.com/mage-ai/mage-ai"
    },
    {
        "rank": 10, "nome": "Redpanda", "subtitulo": "Streaming de Eventos em Tempo Real em C++ (Sem JVM)",
        "substitui": "Confluent Kafka Cloud", "categoria": "Streaming de Eventos",
        "economia": "-$ 30.000 / ano", "licenca": "BSL / Apache-2.0", "kind": "STREAMING",
        "o_que_faz": "Substituto 100% compatível com a API do Apache Kafka, construído em C++ para entregar menor latência e zero dores de cabeça com ZooKeeper ou JVM.",
        "como_funciona": "Usa o modelo thread-per-core do framework Seastar para extrair o rendimento máximo de discos NVMe e conexões de 100Gbps.",
        "quickstart": "docker run -d -p 9092:9092 docker.redpanda.com/redpandadata/redpanda:latest",
        "specs": "Latência p99 até 10x menor que Kafka · Zero tuning de Java",
        "veredito": "A melhor escolha para streaming de eventos de missão crítica com consumo mínimo de infraestrutura.",
        "github": "https://github.com/redpanda-data/redpanda"
    },
    {
        "rank": 11, "nome": "Apache Kafka", "subtitulo": "A Plataforma Padrão de Mensageria Distribuída",
        "substitui": "AWS Kinesis / Google PubSub", "categoria": "Mensageria Distribuída",
        "economia": "-$ 22.000 / ano", "licenca": "Apache-2.0", "kind": "MESSAGING BROKER",
        "o_que_faz": "Plataforma distribuída de log de eventos imutável capaz de publicar, assinar, armazenar e processar streams de eventos em escala corporativa.",
        "como_funciona": "Armazena mensagens particionadas em tópicos replicados com suporte moderno a KRaft (sem ZooKeeper).",
        "quickstart": "docker run -d -p 9092:9092 apache/kafka:latest",
        "specs": "Capacidade de milhões de mensagens/s · Retenção durável em disco",
        "veredito": "O padrão onipresente em grandes corporações e sistemas legados de alto tráfego.",
        "github": "https://github.com/apache/kafka"
    },
    {
        "rank": 12, "nome": "Great Expectations", "subtitulo": "Framework de Validação e Qualidade de Dados",
        "substitui": "Monte Carlo Data / Datadog DQ", "categoria": "Data Quality",
        "economia": "-$ 28.000 / ano", "licenca": "Apache-2.0", "kind": "DATA QUALITY",
        "o_que_faz": "Valida, documenta e monitora a qualidade de dados automaticamente em pipelines, prevenindo que dados corrompidos cheguem ao dashboard.",
        "como_funciona": "Define testes declarativos ('expectations') como 'a coluna salário não pode ser nula' e emite relatórios visuais (Data Docs).",
        "quickstart": "pip install great_expectations\ngreat_expectations init",
        "specs": "Data Docs em HTML automáticos · Integração com Airflow e Dagster",
        "veredito": "Acaba com o silêncio de pipelines que quebram silenciosamente e geram relatórios errados.",
        "github": "https://github.com/great-expectations/great_expectations"
    },
    {
        "rank": 13, "nome": "Feast", "subtitulo": "Feature Store Aberto para Machine Learning em Produção",
        "substitui": "Tecton / Hopsworks", "categoria": "Feature Store para ML",
        "economia": "-$ 24.000 / ano", "licenca": "Apache-2.0", "kind": "FEATURE STORE",
        "o_que_faz": "Gerencia e serve features de Machine Learning para treinamento em lote (offline) e inferência em tempo real com baixa latência (online).",
        "como_funciona": "Sincroniza definições de features entre o Data Lake (Iceberg/Parquet) e o banco de baixa latência (Redis/PostgreSQL).",
        "quickstart": "pip install feast\nfeast init meu_projeto",
        "specs": "Previne data leakage entre treino e teste · Servidor REST de inferência",
        "veredito": "A peça fundamental para amadurecer a esteira de MLOps de qualquer empresa.",
        "github": "https://github.com/feast-dev/feast"
    },
    {
        "rank": 14, "nome": "MinIO", "subtitulo": "Armazenamento de Objetos S3 de Alta Performance",
        "substitui": "AWS S3 / Google Cloud Storage", "categoria": "Object Storage S3",
        "economia": "-$ 30.000 / ano", "licenca": "AGPLv3", "kind": "OBJECT STORAGE",
        "o_que_faz": "Servidor de armazenamento de objetos 100% compatível com a API do AWS S3, desenhado para data lakes locais, NVMe e nuvens privadas.",
        "como_funciona": "Entrega leitura e escrita de alta velocidade com suporte a criptografia, versionamento de objetos e bloqueio imutável (Object Lock).",
        "quickstart": "docker run -p 9000:9000 -p 9001:9001 minio/minio server /data --console-address ':9001'",
        "specs": "Velocidade de até centenas de GB/s em hardware NVMe",
        "veredito": "A base soberana para hospedar terabytes de Data Lakes sem pagar taxas de transferência (egress) da AWS.",
        "github": "https://github.com/minio/minio"
    },
    {
        "rank": 15, "nome": "Apache Spark", "subtitulo": "O Motor de Processamento Distribuído em Larga Escala",
        "substitui": "Databricks Jobs Engine", "categoria": "Processamento Massivo",
        "economia": "-$ 40.000 / ano", "licenca": "Apache-2.0", "kind": "DISTRIBUTED ENGINE",
        "o_que_faz": "Motor de processamento de dados unificado e distribuído para processamento em lote, streaming, grafos e algoritmos de ML em terabytes/petabytes.",
        "como_funciona": "Executa computação distribuída em memória (RDDs e DataFrames) com paralelismo em clusters sob demanda.",
        "quickstart": "pip install pyspark\nfrom pyspark.sql import SparkSession",
        "specs": "Suporte a Python, Scala, Java e R · Ecossistema gigantesco",
        "veredito": "Continua sendo o padrão para operações corporativas de escala colossal.",
        "github": "https://github.com/apache/spark"
    },
    {
        "rank": 16, "nome": "DataHub", "subtitulo": "Catálogo de Metadados e Governança de Dados da LinkedIn",
        "substitui": "Alation / Collibra", "categoria": "Catálogo & Governança",
        "economia": "-$ 35.000 / ano", "licenca": "Apache-2.0", "kind": "METADATA CATALOG",
        "o_que_faz": "Plataforma de catálogo de dados de código aberto que mapeia esquemas, linhagem ponta a ponta e ownership de ativos de dados de toda a organização.",
        "como_funciona": "Ingere metadados via push/pull de bancos, ferramentas de BI (Metabase/Superset) e orquestradores, exibindo um grafo unificado.",
        "quickstart": "pip install acryl-datahub\ndatahub docker quickstart",
        "specs": "Linhagem de dados automática · Busca semântica de tabelas",
        "veredito": "Acaba com o problema clássico de ninguém saber onde estão os dados confiáveis na empresa.",
        "github": "https://github.com/datahub-project/datahub"
    },
    {
        "rank": 17, "nome": "Cube.js", "subtitulo": "A Camada Semântica Universal para Métricas e BI",
        "substitui": "GoodData / Looker Semantic Layer", "categoria": "Camada Semântica",
        "economia": "-$ 20.000 / ano", "licenca": "Apache-2.0", "kind": "SEMANTIC LAYER",
        "o_que_faz": "Fornece uma camada centralizada para modelar métricas de negócio (ex: 'Receita Líquida') e disponibilizá-las via SQL, REST e GraphQL para qualquer app.",
        "como_funciona": "Traduz consultas abstratas de métricas em SQL otimizado para o banco analítico com cache pré-agregado em alta velocidade.",
        "quickstart": "npm install -g cubejs-cli\ncubejs create meu_cube -d duckdb",
        "specs": "API SQL/REST/GraphQL · Camada de pré-agregações",
        "veredito": "Garante que o time de Vendas e o Financeiro vejam o mesmo número de faturamento em todas as ferramentas.",
        "github": "https://github.com/cube-js/cube"
    },
    {
        "rank": 18, "nome": "Apache Arrow", "subtitulo": "O Padrão de Memória Colunar Zero-Copy",
        "substitui": "Formatos Proprietários em RAM", "categoria": "Formato em Memória",
        "economia": "Incalculável", "licenca": "Apache-2.0", "kind": "IN-MEMORY FORMAT",
        "o_que_faz": "Especificação e biblioteca de dados em formato colunar para acelerar o compartilhamento de dados em memória sem custos de serialização.",
        "como_funciona": "Permite que diferentes motores (Polars, DuckDB, Spark, Pandas) compartilhem ponteiros de memória diretamente sem cópias extras.",
        "quickstart": "pip install pyarrow\nimport pyarrow as pa",
        "specs": "Zero-Copy data sharing · SIMD vectorization",
        "veredito": "A fundação invisível que torna o ecossistema moderno de dados 100x mais eficiente.",
        "github": "https://github.com/apache/arrow"
    },
    {
        "rank": 19, "nome": "Apache Superset", "subtitulo": "Visualização de Dados e BI Aberto em Larga Escala",
        "substitui": "Tableau Server / Looker", "categoria": "BI & Dashboards",
        "economia": "-$ 30.000 / ano", "licenca": "Apache-2.0", "kind": "DATA VIZ / BI",
        "o_que_faz": "Plataforma corporativa de exploração e visualização de dados com dezenas de gráficos interativos, suporte a SQL Lab e integração a qualquer banco.",
        "como_funciona": "Conecta via drivers SQLAlchemy a dezenas de fontes de dados, gerando consultas otimizadas e dashboards compartilháveis com controle de acesso.",
        "quickstart": "docker run -d -p 8088:8088 apache/superset",
        "specs": "+50 tipos de gráficos nativos · SQL Lab avançado",
        "veredito": "A melhor alternativa de BI corporativo aberta para substituir o Tableau Server.",
        "github": "https://github.com/apache/superset"
    },
    {
        "rank": 20, "nome": "Metabase", "subtitulo": "Business Intelligence Ágil para Usuários Finais",
        "substitui": "Power BI Premium", "categoria": "BI & Analytics",
        "economia": "-$ 25.000 / ano", "licenca": "AGPLv3", "kind": "SELF-SERVICE BI",
        "o_que_faz": "Permite que qualquer pessoa na empresa faça perguntas sobre os dados sem saber SQL, criando dashboards elegantes em poucos minutos.",
        "como_funciona": "Interface intuitiva com construtor visual de queries, alertas automáticos por Slack/E-mail e relatórios periódicos.",
        "quickstart": "docker run -d -p 3000:3000 metabase/metabase:latest",
        "specs": "Configuração em < 5 minutos · Conexão direta com DuckDB e Postgres",
        "veredito": "A ferramenta de BI mais amada por equipes de negócios e startups.",
        "github": "https://github.com/metabase/metabase"
    }
]

html_36 = render_html(
    36, "Camada 36 · Engenharia de Dados & Modern Data Stack",
    "Engenharia de Dados & Lakehouse Soberano",
    "Como processar terabytes de dados e construir pipelines corporativos <strong>substituindo Snowflake, Databricks, Fivetran e dbt Cloud</strong> por uma arquitetura aberta baseada em Apache Iceberg, DuckDB, Polars e Airbyte.",
    ["<b>20</b> tecnologias auditadas", "<b>Economia:</b> -$ 50.000 a $ 250.000 / ano", "<b>Performance:</b> 10x a 50x mais rápido em NVMe local"],
    {"accent": "#1A446C", "accent_soft": "#DCE7F2", "accent_dark": "#7AA5D6", "accent_dark_soft": "#162436"},
    items_36
)
with open(os.path.join(OUTPUT_DIR, "36-engenharia-dados-lakehouse-soberano.html"), "w", encoding="utf-8") as f:
    f.write(html_36)
print("[✓] Camada 36 gerada com 20 fichas completas.")

# ==============================================================================
# CAMADA 37: IDENTIDADE, AUTENTICAÇÃO & ZERO-TRUST SSO (IAM)
# ==============================================================================
items_37 = [
    {
        "rank": 1, "nome": "Keycloak", "subtitulo": "O Padrão Ouro de SSO & IAM Corporativo",
        "substitui": "Okta / Auth0 Enterprise", "categoria": "IAM & SSO Corporativo",
        "economia": "-$ 40.000 a $ 120.000 / ano", "licenca": "Apache-2.0", "kind": "IAM / SSO",
        "o_que_faz": "Servidor completo de autenticação centralizada, Single Sign-On (SSO), federação de identidades (Active Directory/LDAP) e controle RBAC fino.",
        "como_funciona": "Implementa protocolos padrão como OpenID Connect, OAuth 2.0 e SAML 2.0 com suporte a MFA, Passkeys e gestão de múltiplos domínios (realms).",
        "quickstart": "docker run -p 8080:8080 -e KEYCLOAK_ADMIN=admin -e KEYCLOAK_ADMIN_PASSWORD=admin quay.io/keycloak/keycloak:latest start-dev",
        "specs": "Zero cobrança por MAU · Suporta milhões de usuários",
        "veredito": "O padrão industrial indiscutível para libertar empresas das mensalidades por usuário do Okta.",
        "github": "https://github.com/keycloak/keycloak"
    },
    {
        "rank": 2, "nome": "Authentik", "subtitulo": "Provedor de Identidade Moderno e Leve para DevOps",
        "substitui": "Auth0 / OneLogin", "categoria": "IdP Moderno",
        "economia": "-$ 25.000 / ano", "licenca": "GPLv3", "kind": "IDP / SSO",
        "o_que_faz": "Provedor de identidade flexível e moderno focado em ambientes Docker e Kubernetes, integrando autenticação em apps legados e novos.",
        "como_funciona": "Arquitetura baseada em estágios e fluxos altamente personalizáveis, com proxy reverso integrado (Outpost) para proteger apps que não possuem auth nativa.",
        "quickstart": "docker compose -f docker-compose.yml up -d # Usando template oficial",
        "specs": "Proxy Outpost integrado · Suporte a WebAuthn/Passkeys nativo",
        "veredito": "A escolha favorita de equipes ágeis e times de DevOps que buscam facilidade de uso.",
        "github": "https://github.com/goauthentik/authentik"
    },
    {
        "rank": 3, "nome": "Zitadel", "subtitulo": "Infraestrutura de Identidade Cloud-Native para SaaS Multi-Tenant",
        "substitui": "Auth0 B2B Multi-Tenant", "categoria": "IAM Multi-Tenancy",
        "economia": "-$ 30.000 / ano", "licenca": "Apache-2.0", "kind": "B2B IAM",
        "o_que_faz": "Plataforma de gerenciamento de identidades construída em Go com foco em SaaS B2B, permitindo que cada cliente corporativo tenha seu próprio SSO e domínio.",
        "como_funciona": "Arquitetura baseada em Event Sourcing com suporte nativo a autorização granular e delegação de administração de usuários.",
        "quickstart": "docker run -p 8080:8080 ghcr.io/zitadel/zitadel:latest start-from-init --masterkey 'MasterKeyNeedsToHave32Characters!'",
        "specs": "Escrita em Go com baixa latência · Event Sourcing auditável",
        "veredito": "A melhor solução do mercado para empresas criando produtos SaaS que precisam de login B2B.",
        "github": "https://github.com/zitadel/zitadel"
    },
    {
        "rank": 4, "nome": "Ory Kratos", "subtitulo": "Motor Headless de Gestão de Usuários e Autenticação em Go",
        "substitui": "Firebase Auth / AWS Cognito", "categoria": "Headless User Management",
        "economia": "-$ 18.000 / ano", "licenca": "Apache-2.0", "kind": "HEADLESS AUTH",
        "o_que_faz": "Gerencia cadastro, login, recuperação de senha, MFA e verificação de e-mail de forma totalmente desacoplada de interface visual (Headless).",
        "como_funciona": "Fornece APIs REST e gRPC com segurança de nível bancário para que você construa sua própria tela de login em qualquer framework (React, Flutter).",
        "quickstart": "docker run -p 4433:4433 -p 4434:4434 oryd/kratos:latest",
        "specs": "Latência de nanossegundos · Totalmente Headless",
        "veredito": "Perfeito para quem quer controle total sobre a experiência de interface sem recriar regras de criptografia e sessão.",
        "github": "https://github.com/ory/kratos"
    },
    {
        "rank": 5, "nome": "Ory Hydra", "subtitulo": "Servidor OAuth 2.0 e OpenID Connect Certificado",
        "substitui": "PingFederate", "categoria": "OAuth2 / OIDC Server",
        "economia": "-$ 22.000 / ano", "licenca": "Apache-2.0", "kind": "OAUTH2 ENGINE",
        "o_que_faz": "Servidor OpenID Connect e OAuth 2.0 certificado pela OpenID Foundation, permitindo que você emita tokens de acesso seguros para terceiros.",
        "como_funciona": "Conecta-se a qualquer banco de dados de usuários existente sem obrigar a migrar credenciais, focando estritamente no fluxo de emissão de tokens.",
        "quickstart": "docker run -p 4444:4444 -p 4445:4445 oryd/hydra:latest",
        "specs": "Certificação OpenID Foundation · Suporte a mTLS",
        "veredito": "A infraestrutura padrão para criar ecossistemas de APIs abertas e Open Banking.",
        "github": "https://github.com/ory/hydra"
    },
    {
        "rank": 6, "nome": "Teleport", "subtitulo": "Acesso Zero-Trust Unificado para SSH, Kubernetes e Bancos",
        "substitui": "CyberArk / BeyondTrust", "categoria": "Zero-Trust Infrastructure Access",
        "economia": "-$ 50.000 / ano", "licenca": "AGPLv3 / Apache-2.0", "kind": "ZERO-TRUST ACCESS",
        "o_que_faz": "Substitui chaves estáticas SSH, senhas de banco de dados e VPNs lentas por certificados criptográficos de curta duração baseados na identidade do usuário.",
        "como_funciona": "Fornece um proxy de acesso com gravação completa de sessões de terminal e suporte a auditoria de comandos em tempo real.",
        "quickstart": "curl https://goteleport.com/static/install.sh | bash\nteleport start",
        "specs": "Gravação de sessões SSH/K8s/DB · Certificados efêmeros",
        "veredito": "Elimina vazamentos de chaves SSH corporativas e cumpre requisitos estritos de auditoria SOC2.",
        "github": "https://github.com/gravitational/teleport"
    },
    {
        "rank": 7, "nome": "Casdoor", "subtitulo": "Plataforma de IAM com UI Rica e Suporte Social Multicanal",
        "substitui": "Auth0 / Okta", "categoria": "UI-First IAM",
        "economia": "-$ 20.000 / ano", "licenca": "Apache-2.0", "kind": "UI-FIRST IAM",
        "o_que_faz": "Servidor de autenticação completo com interface de administração elegante, login por redes sociais (Google, GitHub, WeChat) e suporte a SAML/OIDC.",
        "como_funciona": "Backend em Go e frontend em React prontos para uso em menos de 10 minutos, com suporte a múltiplos provedores de SMS e e-mail.",
        "quickstart": "docker run -p 8000:8000 casbin/casdoor:latest",
        "specs": "Login social nativo (+30 redes) · SDKs para 10+ linguagens",
        "veredito": "A solução visual mais amigável e rápida de configurar para projetos web e mobile.",
        "github": "https://github.com/casdoor/casdoor"
    },
    {
        "rank": 8, "nome": "Authelia", "subtitulo": "Portal de Autenticação 2FA para Proxies Reversos",
        "substitui": "Duo Security / Cloudflare Access", "categoria": "2FA Proxy Gateway",
        "economia": "-$ 15.000 / ano", "licenca": "Apache-2.0", "kind": "2FA GATEWAY",
        "o_que_faz": "Adiciona uma camada obrigatória de autenticação de dois fatores (TOTP, WebAuthn, Duo) na frente de qualquer aplicação web através do proxy reverso.",
        "como_funciona": "Integra-se nativamente com NGINX, Traefik, Caddy e HAProxy via módulo de forward-auth antes de liberar a requisição.",
        "quickstart": "docker run -d -p 9091:9091 authelia/authelia:latest",
        "specs": "Suporte a YubiKey/FIDO2 · Consumo < 50 MB de RAM",
        "veredito": "Protege painéis internos e ferramentas administrativas sem precisar alterar uma linha de código da aplicação.",
        "github": "https://github.com/authelia/authelia"
    },
    {
        "rank": 9, "nome": "SuperTokens", "subtitulo": "SDK de Autenticação & Gerenciamento Seguro de Sessões",
        "substitui": "Auth0 / Clerk.dev", "categoria": "Auth SDK & Sessions",
        "economia": "-$ 18.000 / ano", "licenca": "Apache-2.0", "kind": "AUTH SDK",
        "o_que_faz": "Estrutura de autenticação completa com proteção avançada de sessão contra roubo de tokens, login sem senha, e-mail/senha e OAuth social.",
        "como_funciona": "Combina um núcleo em Java/Go de alta segurança com bibliotecas de frontend e backend em JavaScript/Python/Go.",
        "quickstart": "docker run -p 3567:3567 registry.supertokens.io/supertokens/supertokens-postgresql",
        "specs": "Rotação automática de refresh tokens · Proteção anti-CSRF nativa",
        "veredito": "A melhor alternativa ao Clerk.dev para desenvolvedores que querem hospedar seu próprio auth com experiência premium.",
        "github": "https://github.com/supertokens/supertokens-core"
    },
    {
        "rank": 10, "nome": "Vaultwarden", "subtitulo": "Cofre de Senhas Corporativo Leve em Rust (Bitwarden)",
        "substitui": "1Password Business / LastPass", "categoria": "Cofre de Senhas Corporativo",
        "economia": "-$ 8.000 / ano", "licenca": "AGPLv3", "kind": "PASSWORD MANAGER",
        "o_que_faz": "Implementação leve em Rust do backend do Bitwarden, permitindo que empresas gerenciem e compartilhem senhas com criptografia de ponta a ponta.",
        "como_funciona": "Compatível com todas as extensões de navegador e apps móveis oficiais do Bitwarden, consumindo menos de 30 MB de RAM no servidor.",
        "quickstart": "docker run -d -p 8080:80 -v /dados/vw:/data vaultwarden/server:latest",
        "specs": "Criptografia E2E AES-256 · Suporte a organizações e coleções",
        "veredito": "Indispensável para que equipes compartilhem acessos com segurança sem pagar $ 8/usuário/mês para ferramentas fechadas.",
        "github": "https://github.com/dani-garcia/vaultwarden"
    },
    {
        "rank": 11, "nome": "HashiCorp Vault", "subtitulo": "Gestão de Segredos & Emissão de Certificados Dinâmicos",
        "substitui": "AWS Secrets Manager / CyberArk", "categoria": "Secrets Management",
        "economia": "-$ 30.000 / ano", "licenca": "BSL / MPL-2.0", "kind": "SECRETS ENGINE",
        "o_que_faz": "Armazena chaves de API, credenciais de banco e certificados TLS com rotação automática e emissão de credenciais efêmeras sob demanda.",
        "como_funciona": "Aplica políticas estritas de controle de acesso (ACLs) e criptografa todos os dados em repouso com chave mestre protegida por Shamir's Secret Sharing.",
        "quickstart": "docker run -d -p 8200:8200 hashicorp/vault:latest",
        "specs": "Credenciais dinâmicas com TTL · PKI como serviço",
        "veredito": "O cofre central de segredos obrigatório para arquiteturas em escala e microsserviços.",
        "github": "https://github.com/hashicorp/vault"
    },
    {
        "rank": 12, "nome": "Pomerium", "subtitulo": "Identity-Aware Proxy Baseado em Princípios Zero-Trust",
        "substitui": "Zscaler Private Access / Cloudflare Access", "categoria": "Identity-Aware Proxy",
        "economia": "-$ 28.000 / ano", "licenca": "Apache-2.0", "kind": "ZERO-TRUST PROXY",
        "o_que_faz": "Proxy reverso sensível à identidade que valida o login e o contexto do usuário a cada requisição HTTP antes de conceder acesso a recursos internos.",
        "como_funciona": "Integra-se com seu IdP existente (Keycloak, Authentik, Google) e aplica políticas de autorização dinâmicas baseadas em headers assinados.",
        "quickstart": "docker run -d -p 443:443 pomerium/pomerium:latest",
        "specs": "Construído sobre o Envoy Proxy · Inspeção de contexto por request",
        "veredito": "Substitui VPNs lentas por acesso Zero-Trust direto pelo navegador.",
        "github": "https://github.com/pomerium/pomerium"
    },
    {
        "rank": 13, "nome": "Boundary", "subtitulo": "Gerenciador de Acesso Seguro a Infraestruturas Dinâmicas",
        "substitui": "Bastião SSH Proprietário", "categoria": "Privileged Access Management",
        "economia": "-$ 15.000 / ano", "licenca": "BSL", "kind": "PAM ACCESS",
        "o_que_faz": "Permite que engenheiros e desenvolvedores acessem servidores e bancos de dados privados sem expor a rede subjacente e sem gerenciar credenciais.",
        "como_funciona": "Autentica o usuário no IdP corporativo e cria um túnel TCP autenticado e temporário direto para a porta do serviço de destino.",
        "quickstart": "boundary dev",
        "specs": "Zero exposição de rede privada · Acesso baseado em papéis",
        "veredito": "A forma mais elegante e segura de dar acesso a bancos de dados de produção para times de engenharia.",
        "github": "https://github.com/hashicorp/boundary"
    },
    {
        "rank": 14, "nome": "FreeIPA", "subtitulo": "Gerenciamento Centralizado de Domínio Linux, LDAP & Kerberos",
        "substitui": "Microsoft Active Directory", "categoria": "Domain & LDAP Controller",
        "economia": "-$ 25.000 / ano", "licenca": "GPLv3", "kind": "DOMAIN CONTROLLER",
        "o_que_faz": "Fornece gerenciamento centralizado de identidades, autenticação Kerberos, políticas de sudo, DNS e certificados TLS para frotas de servidores Linux.",
        "como_funciona": "Combina 389 Directory Server, MIT Kerberos, Dogtag PKI e BIND em uma solução coesa de controle de domínio corporativo.",
        "quickstart": "docker run -h ipa.exemplo.com -p 443:443 freeipa/freeipa-server",
        "specs": "O Active Directory do mundo Linux · Federação com AD da Microsoft",
        "veredito": "A solução definitiva para gerenciar milhares de servidores Linux e contas de operadores sem Windows Server.",
        "github": "https://github.com/freeipa/freeipa"
    },
    {
        "rank": 15, "nome": "OAuth2-Proxy", "subtitulo": "Proxy Reverso Injetor de Autenticação OIDC",
        "substitui": "Módulos de Auth Proprietários", "categoria": "OIDC Proxy Injetor",
        "economia": "-$ 10.000 / ano", "licenca": "MIT", "kind": "OAUTH2 PROXY",
        "o_que_faz": "Proxy reverso que intercepta requisições e força a autenticação através de qualquer provedor OpenID Connect (Keycloak, GitHub, GitLab) antes de repassar.",
        "como_funciona": "Repassa os dados do usuário autenticado para a aplicação downstream através de cabeçalhos HTTP como `X-Forwarded-User` e `X-Forwarded-Email`.",
        "quickstart": "docker run -d -p 4180:4180 quay.io/oauth2-proxy/oauth2-proxy:latest",
        "specs": "Compatível com qualquer IdP OpenID Connect",
        "veredito": "A forma mais rápida de colocar login corporativo na frente de dashboards como Grafana, Prometheus ou ferramentas internas.",
        "github": "https://github.com/oauth2-proxy/oauth2-proxy"
    },
    {
        "rank": 16, "nome": "PocketBase Auth", "subtitulo": "Backend Leve com Autenticação Embutida em SQLite",
        "substitui": "Firebase Authentication", "categoria": "Embedded Auth Backend",
        "economia": "-$ 8.000 / ano", "licenca": "MIT", "kind": "EMBEDDED AUTH",
        "o_que_faz": "Backend embutido em um único arquivo binário com sistema de autenticação, banco de dados SQLite em tempo real e upload de arquivos integrados.",
        "como_funciona": "Gera APIs REST instantâneas com regras de acesso declarativas e suporte pronto para login OAuth2 com dezenas de provedores.",
        "quickstart": "./pocketbase serve",
        "specs": "Binário único < 40 MB · Gerencia 10.000+ conexões simultâneas",
        "veredito": "Ideal para MVPs, ferramentas internas e aplicativos móveis rápidos.",
        "github": "https://github.com/pocketbase/pocketbase"
    },
    {
        "rank": 17, "nome": "Dex IdP", "subtitulo": "Conector Plugável de Identidades OIDC para Kubernetes",
        "substitui": "IdPs Fechados de Nuvem", "categoria": "OIDC Identity Broker",
        "economia": "-$ 12.000 / ano", "licenca": "Apache-2.0", "kind": "OIDC BROKER",
        "o_que_faz": "Atua como uma ponte de autenticação entre aplicações que falam OpenID Connect e servidores de identidade legados como LDAP, SAML e GitHub.",
        "como_funciona": "Emite tokens JWT padronizados para clusters Kubernetes e apps modernos, consultando a fonte de verdade corporativa em background.",
        "quickstart": "docker run -d -p 5556:5556 ghcr.io/dexidp/dex:latest",
        "specs": "Padrão de autenticação em clusters Kubernetes corporativos",
        "veredito": "A cola arquitetural perfeita para modernizar autenticação de infraestrutura.",
        "github": "https://github.com/dexidp/dex"
    },
    {
        "rank": 18, "nome": "Kanidm", "subtitulo": "Servidor de Identidade Moderno e Seguro em Rust",
        "substitui": "FreeIPA / Active Directory", "categoria": "Modern Identity Server",
        "economia": "-$ 15.000 / ano", "licenca": "MPL-2.0", "kind": "RUST IAM",
        "o_que_faz": "Servidor de gerenciamento de identidades construído em Rust focado em segurança de memória, performance extrema e autenticação nativa sem senhas.",
        "como_funciona": "Combina servidor OAuth2, servidor RADIUS e integração PAM para Linux com suporte prioritário a chaves FIDO2/Passkeys.",
        "quickstart": "docker run -d -p 8443:8443 kanidm/server:latest",
        "specs": "100% Rust memory-safe · Suporte nativo a Passkeys",
        "veredito": "O futuro da administração de identidades segura para ambientes de alta criticidade.",
        "github": "https://github.com/kanidm/kanidm"
    },
    {
        "rank": 19, "nome": "SimpleWebAuthn", "subtitulo": "Biblioteca Universal para Autenticação FIDO2 / Passkeys",
        "substitui": "Provedores de Passkeys Pagos", "categoria": "Passkeys / WebAuthn",
        "economia": "Incalculável", "licenca": "MIT", "kind": "PASSKEYS LIB",
        "o_que_faz": "Conjunto de bibliotecas TypeScript/JavaScript para implementar autenticação biométrica e chaves de segurança (Passkeys/FIDO2) no navegador e servidor.",
        "como_funciona": "Gera desafios criptográficos e valida assinaturas de hardware (Touch ID, Face ID, Windows Hello) sem trafegar senhas pela rede.",
        "quickstart": "npm install @simplewebauthn/browser @simplewebauthn/server",
        "specs": "Conformidade estrita com as especificações W3C WebAuthn Level 3",
        "veredito": "A base para eliminar de vez as senhas dos seus sistemas com a tecnologia mais segura do mundo.",
        "github": "https://github.com/MasterKale/SimpleWebAuthn"
    },
    {
        "rank": 20, "nome": "Cerbos", "subtitulo": "Motor de Autorização Fina Desacoplado (ABAC / RBAC)",
        "substitui": "Permit.io / Ory Keto", "categoria": "Authorization Engine",
        "economia": "-$ 18.000 / ano", "licenca": "Apache-2.0", "kind": "AUTHZ PDP",
        "o_que_faz": "Desacopla as regras de permissão de acesso da lógica de código da aplicação, permitindo definir políticas de acesso complexas em arquivos YAML.",
        "como_funciona": "Atua como um Policy Decision Point (PDP) ultra-rápido que responde a perguntas como 'o usuário X pode editar o documento Y com base no status Z?' em milissegundos.",
        "quickstart": "docker run -p 3592:3592 ghcr.io/cerbos/cerbos:latest",
        "specs": "Latência < 1ms · Políticas declarativas em YAML versionadas em Git",
        "veredito": "Acaba com o código espaguete de 'if user.role == admin' espalhado por toda a aplicação.",
        "github": "https://github.com/cerbos/cerbos"
    }
]

html_37 = render_html(
    37, "Camada 37 · Segurança de Acesso & Identidade",
    "Identidade, Autenticação & Zero-Trust SSO",
    "Como unificar logins, controle de permissões por papéis (RBAC), autenticação sem senhas (Passkeys) e acesso Zero-Trust <strong>substituindo Okta, Auth0, Microsoft Entra ID (Azure AD) e Ping Identity</strong>.",
    ["<b>20</b> tecnologias auditadas", "<b>Economia:</b> -$ 15 a $ 60 por usuário / mês", "<b>Padrões:</b> OpenID Connect, OAuth2, SAML 2.0 & Passkeys"],
    {"accent": "#2A4365", "accent_soft": "#E2E8F0", "accent_dark": "#90CDF4", "accent_dark_soft": "#1A365D"},
    items_37
)
with open(os.path.join(OUTPUT_DIR, "37-identidade-autenticacao-zero-trust-iam.html"), "w", encoding="utf-8") as f:
    f.write(html_37)
print("[✓] Camada 37 gerada com 20 fichas completas.")

# ==============================================================================
# CAMADA 38: EDGE AI & ON-DEVICE INFERENCE
# ==============================================================================
items_38 = [
    {
        "rank": 1, "nome": "ExecuTorch", "subtitulo": "O Motor Oficial da Meta para PyTorch em Mobile & NPU",
        "substitui": "APIs em Nuvem (OpenAI / Anthropic)", "categoria": "Runtime Mobile PyTorch",
        "economia": "100% Redução de Custos de Nuvem", "licenca": "BSD-3-Clause", "kind": "MOBILE RUNTIME",
        "o_que_faz": "Runtime ultra-compacto e modular do ecossistema PyTorch projetado para executar modelos de IA generativa e visão diretamente em smartphones e chips NPU.",
        "como_funciona": "Compila modelos PyTorch em binários enxutos com delegação direta para aceleradores de silício (Apple Neural Engine, Qualcomm Hexagon, ARM Ethos).",
        "quickstart": "git clone https://github.com/pytorch/executorch.git\n./install_executorch.sh",
        "specs": "< 50 KB de overhead · Aceleração nativa em NPUs de smartphones",
        "veredito": "O futuro da IA em aplicativos móveis: privacidade absoluta e funcionamento offline.",
        "github": "https://github.com/pytorch/executorch"
    },
    {
        "rank": 2, "nome": "MediaPipe", "subtitulo": "Framework do Google para Visão Computacional On-Device",
        "substitui": "APIs de Visão Computacional em Nuvem", "categoria": "Visão & Gestos On-Device",
        "economia": "100% Gratuito / Zero API", "licenca": "Apache-2.0", "kind": "VISION / GESTURES",
        "o_que_faz": "Executa modelos de visão computacional em tempo real (rastreamento de mãos, malha facial de 468 pontos, pose corporal, segmentação) diretamente no dispositivo.",
        "como_funciona": "Processa fluxos de vídeo da câmera a 60 FPS com aceleração por GPU/NPU sem enviar um único frame para servidores externos.",
        "quickstart": "pip install mediapipe\nimport mediapipe as mp",
        "specs": "Rastreamento facial e de mãos a 60 FPS em celulares modestos",
        "veredito": "O padrão da indústria para aplicações interativas de realidade aumentada e acessibilidade.",
        "github": "https://github.com/google-ai-edge/mediapipe"
    },
    {
        "rank": 3, "nome": "MLX", "subtitulo": "Framework de Machine Learning Nativo para Apple Silicon",
        "substitui": "CUDA / Endpoints Remotos no Mac", "categoria": "ML para Apple Silicon",
        "economia": "Máxima Performance M1/M2/M3/M4", "licenca": "MIT", "kind": "APPLE SILICON ML",
        "o_que_faz": "Framework de aprendizado de máquina desenvolvido pela Apple para treinar e rodar modelos de IA aproveitando a arquitetura de memória unificada dos chips M1/M2/M3/M4.",
        "como_funciona": "API inspirada em NumPy e PyTorch com operações vetorizadas que compartilham memória entre CPU e GPU sem cópias intermediárias.",
        "quickstart": "pip install mlx-lm\npython -m mlx_lm.generate --model mistralai/Mistral-7B-Instruct-v0.2 --prompt 'Olá!'",
        "specs": "Gera 30+ tokens/s em MacBooks locais com consumo de bateria irrisório",
        "veredito": "A ferramenta que transforma qualquer Mac com chip Apple em uma estação de trabalho de IA soberana.",
        "github": "https://github.com/ml-explore/mlx"
    },
    {
        "rank": 4, "nome": "Llama.cpp", "subtitulo": "Inferência de LLMs em C/C++ Puro para Qualquer Hardware",
        "substitui": "Endpoints de LLM Remotos Pagos", "categoria": "Inferência de LLMs em C++",
        "economia": "Zero Custo de Tokens", "licenca": "MIT", "kind": "LLM INFERENCE",
        "o_que_faz": "Executa grandes modelos de linguagem (Llama 3, DeepSeek, Qwen) em formato quantizado GGUF em processadores comuns, placas ARM e GPUs com máxima velocidade.",
        "como_funciona": "Escrito em C/C++ sem dependências pesadas, com otimizações manuais em assembly (AVX2, NEON) e quantização de 2 a 8 bits.",
        "quickstart": "./llama-cli -m modelo.gguf -p 'Explique a relatividade' -n 128",
        "specs": "Quantização 4-bit (Q4_K_M) que reduz modelos de 16GB para 4GB de RAM",
        "veredito": "O projeto que democratizou a IA local no planeta Terra.",
        "github": "https://github.com/ggerganov/llama.cpp"
    },
    {
        "rank": 5, "nome": "WhisperKit", "subtitulo": "Transcrição de Áudio On-Device para iOS e macOS",
        "substitui": "OpenAI Whisper API ($ 0.006/min)", "categoria": "Speech-to-Text On-Device",
        "economia": "-$ 5.000 / ano", "licenca": "MIT", "kind": "LOCAL STT",
        "o_que_faz": "Executa o modelo Whisper de transcrição de voz diretamente no hardware Apple com otimização específica para o Apple Neural Engine (ANE).",
        "como_funciona": "Transcreve áudios em tempo real com alta precisão sem gastar dados móveis e garantindo sigilo médico e jurídico absoluto.",
        "quickstart": "swift package add https://github.com/argmaxinc/WhisperKit",
        "specs": "Transcrição 10x mais rápida que tempo real no iPhone 15/16",
        "veredito": "A solução definitiva de áudio para texto em aplicativos móveis que prezam pela privacidade.",
        "github": "https://github.com/argmaxinc/WhisperKit"
    },
    {
        "rank": 6, "nome": "ONNX Runtime Mobile", "subtitulo": "Motor de Execução Multiplataforma de Modelos de IA",
        "substitui": "Runtimes Fechados de Fabricante", "categoria": "Cross-Platform AI Runtime",
        "economia": "Zero Dependência", "licenca": "MIT", "kind": "CROSS-PLATFORM RUNTIME",
        "o_que_faz": "Executa modelos treinados em qualquer framework (PyTorch, TensorFlow, Scikit-Learn) em dispositivos Android, iOS e Windows com binários reduzidos.",
        "como_funciona": "Otimiza grafos de computação e delega a execução para aceleradores de hardware como NNAPI (Android) e CoreML (iOS).",
        "quickstart": "npm install onnxruntime-react-native",
        "specs": "Binário base < 2 MB · Suporta visão, áudio e NLP",
        "veredito": "A ponte universal para desenvolvedores que precisam publicar IA no Android e iOS com a mesma base de código.",
        "github": "https://github.com/microsoft/onnxruntime"
    },
    {
        "rank": 7, "nome": "LiteRT (TFLite)", "subtitulo": "O Motor Leve de Deep Learning para Android & IoT",
        "substitui": "APIs Móveis Proprietárias", "categoria": "Mobile Deep Learning",
        "economia": "Zero Custo", "licenca": "Apache-2.0", "kind": "EDGE DEEP LEARNING",
        "o_que_faz": "A evolução moderna do TensorFlow Lite mantida pelo Google para inferência de alta velocidade em dispositivos móveis, microcontroladores e sistemas embarcados.",
        "como_funciona": "Converte modelos neurais para o formato FlatBuffers com quantização de peso para execução direta em DSPs e GPUs mobile.",
        "quickstart": "pip install litert",
        "specs": "Suporte a microcontroladores com apenas centenas de kilobytes de RAM",
        "veredito": "O clássico do ecossistema Android para tarefas de visão e sensores.",
        "github": "https://github.com/google-ai-edge/LiteRT"
    },
    {
        "rank": 8, "nome": "NCNN", "subtitulo": "Framework de Inferência Neural em C++ da Tencent",
        "substitui": "SDKs Fechados de IA Mobile", "categoria": "High-Performance Mobile Neural",
        "economia": "Alta Performance", "licenca": "BSD-3-Clause", "kind": "MOBILE NEURAL",
        "o_que_faz": "Motor de inferência de redes neurais ultra-otimizado para processadores ARM de celulares, sem dependências externas e com inicialização instantânea.",
        "como_funciona": "Usa instruções de montagem ARM NEON manuais com pipeline otimizado para Vulkan GPU em dispositivos Android e iOS.",
        "quickstart": "git clone https://github.com/Tencent/ncnn.git\nmkdir build && cd build && cmake .. && make",
        "specs": "Zero dependências em tempo de execução · Overhead de milissegundos",
        "veredito": "O framework mais rápido do mundo para rodar visão computacional e OCR em celulares Android baratos.",
        "github": "https://github.com/Tencent/ncnn"
    },
    {
        "rank": 9, "nome": "MNN", "subtitulo": "Motor Leve de Deep Learning para Dispositivos da Alibaba",
        "substitui": "Motores Proprietários Fechados", "categoria": "Lightweight Deep Learning",
        "economia": "Leve e Rápido", "licenca": "Apache-2.0", "kind": "EDGE RUNTIME",
        "o_que_faz": "Motor de inferência de alto rendimento desenvolvido para suportar os aplicativos de compras massivos da Alibaba, com foco em eficiência energética.",
        "como_funciona": "Possui conversor universal de modelos e renderizador computacional acelerado por Metal, OpenCL e Vulkan.",
        "quickstart": "pip install MNN",
        "specs": "Redução drástica do consumo de bateria durante a inferência",
        "veredito": "Excelente para aplicações comerciais que rodam inferência de vídeo contínua sem esgotar a bateria do usuário.",
        "github": "https://github.com/alibaba/MNN"
    },
    {
        "rank": 10, "nome": "MLC-LLM", "subtitulo": "Compilador Universal de LLMs para Qualquer GPU e NPU",
        "substitui": "APIs de Nuvem para Web/Mobile", "categoria": "LLM Compiler",
        "economia": "Zero Custo de Servidor", "licenca": "Apache-2.0", "kind": "LLM COMPILER",
        "o_que_faz": "Compila modelos de linguagem para rodar nativamente em qualquer placa gráfica ou chip móvel (Vulkan, Metal, WebGPU, OpenCL, CUDA).",
        "como_funciona": "Utiliza a tecnologia Apache TVM para gerar código nativo de máquina com otimização automática de kernels de atenção.",
        "quickstart": "pip install mlc-llm\nmlc_llm chat HF://mlc-ai/Llama-3-8B-Instruct-q4f16_1-MLC",
        "specs": "Gera código C++ nativo e WebAssembly a partir do mesmo modelo",
        "veredito": "A tecnologia mais avançada para quem precisa entregar LLMs em plataformas heterogêneas.",
        "github": "https://github.com/mlc-ai/mlc-llm"
    },
    {
        "rank": 11, "nome": "WebLLM", "subtitulo": "LLMs Executando 100% no Navegador via WebGPU",
        "substitui": "Chamadas de API de IA no Frontend", "categoria": "Browser In-Memory LLM",
        "economia": "Zero Backend Server", "licenca": "Apache-2.0", "kind": "BROWSER LLM",
        "o_que_faz": "Permite que páginas da web executem modelos de linguagem completos direto na GPU do computador do usuário via WebGPU, sem instalar nada.",
        "como_funciona": "Baixa pesos quantizados em cache local e executa shaders WebGPU compilados com aceleração de hardware nativa.",
        "quickstart": "npm install @mlc-ai/web-llm\nimport { CreateMLCEngine } from '@mlc-ai/web-llm';",
        "specs": "Roda Llama 3, Phi-3 e Gemma direto na aba do Chrome/Safari",
        "veredito": "Revolucionário para SaaS: oferece recursos de IA para seus clientes com custo zero de infraestrutura para você.",
        "github": "https://github.com/mlc-ai/web-llm"
    },
    {
        "rank": 12, "nome": "Transformers.js", "subtitulo": "Modelos de IA em JavaScript no Navegador e Node.js",
        "substitui": "APIs de Embeddings / Hugging Face", "categoria": "Client-Side Transformers",
        "economia": "100% Client-Side", "licenca": "Apache-2.0", "kind": "JS TRANSFORMERS",
        "o_que_faz": "Implementação funcional da biblioteca Transformers da Hugging Face em JavaScript puro, rodando embeddings, tradução, OCR e classificação no cliente.",
        "como_funciona": "Executa modelos ONNX via WebAssembly e WebGPU no navegador, extensões de browser ou servidores Node.js.",
        "quickstart": "npm install @xenova/transformers\nimport { pipeline } from '@xenova/transformers';\nconst pipe = await pipeline('feature-extraction');",
        "specs": "Embeddings vetoriais locais gerados em < 10ms",
        "veredito": "A ferramenta perfeita para criar busca semântica e RAG local sem gastar um centavo com APIs de embedding.",
        "github": "https://github.com/huggingface/transformers.js"
    },
    {
        "rank": 13, "nome": "Sherpa-ONNX", "subtitulo": "Reconhecimento e Síntese de Voz Offline Multiplataforma",
        "substitui": "Google Cloud Speech-to-Text", "categoria": "Speech STT & TTS Offline",
        "economia": "-$ 12.000 / ano", "licenca": "Apache-2.0", "kind": "OFFLINE SPEECH",
        "o_que_faz": "Fornece motores completos de transcrição de voz (STT), síntese de áudio (TTS) e detecção de palavras de ativação (wake-word) 100% offline.",
        "como_funciona": "Suporta modelos Next-gen Kaldi, Whisper e VITS com bindings para Android, iOS, C++, Python, Flutter e Raspberry Pi.",
        "quickstart": "pip install sherpa-onnx",
        "specs": "Detecção de wake-word ('Hey Assistente') com consumo quase nulo de CPU",
        "veredito": "A solução ideal para assistentes de voz embarcados e robótica sem dependência de internet.",
        "github": "https://github.com/k2-fsa/sherpa-onnx"
    },
    {
        "rank": 14, "nome": "Edge Impulse", "subtitulo": "Plataforma de Desenvolvimento de ML para Embarcados",
        "substitui": "AWS IoT Greengrass ML", "categoria": "TinyML & IoT",
        "economia": "-$ 20.000 / ano", "licenca": "Apache-2.0", "kind": "TINYML",
        "o_que_faz": "Facilita a coleta de dados de sensores, treinamento e deploy de modelos de TinyML diretamente em microcontroladores (Arduino, ESP32, STM32).",
        "como_funciona": "Gera código C++ puro e sem alocação dinâmica de memória que roda em chips com menos de 64 KB de RAM.",
        "quickstart": "npm install -g edge-impulse-cli",
        "specs": "Modelos que consomem < 20 KB de RAM e rodam em baterias de botão",
        "veredito": "O padrão industrial para manutenção preditiva em fábricas e sensores inteligentes de campo.",
        "github": "https://github.com/edgeimpulse/edgeimpulse-cli"
    },
    {
        "rank": 15, "nome": "Apache TVM", "subtitulo": "Compilador de Deep Learning de Ponta a Ponta",
        "substitui": "Compiladores Proprietários de GPU", "categoria": "Deep Learning Compiler",
        "economia": "Incalculável", "licenca": "Apache-2.0", "kind": "COMPILER STACK",
        "o_que_faz": "Compila e otimiza grafos de redes neurais para qualquer arquitetura de hardware (CPUs, GPUs x86/ARM e aceleradores customizados).",
        "como_funciona": "Aplica técnicas avançadas de fusão de operadores e auto-tuning para gerar código de máquina mais rápido que os drivers oficiais dos fabricantes.",
        "quickstart": "pip install apache-tvm",
        "specs": "Otimização automática de kernels com aprendizado por reforço",
        "veredito": "A infraestrutura aberta que alimenta os runtimes de IA mais avançados do planeta.",
        "github": "https://github.com/apache/tvm"
    },
    {
        "rank": 16, "nome": "YOLOv10 Mobile", "subtitulo": "Detecção de Objetos em Tempo Real sem NMS",
        "substitui": "Google Vision API", "categoria": "Object Detection Real-Time",
        "economia": "-$ 15.000 / ano", "licenca": "AGPLv3", "kind": "OBJECT DETECTION",
        "o_que_faz": "Detecta dezenas de objetos simultaneamente em streams de vídeo com velocidade ultra-alta eliminando o gargalo de pós-processamento NMS.",
        "como_funciona": "Arquitetura com atribuição dupla de rótulos que permite processar câmeras de segurança e robótica a 120 FPS em placas ARM locais.",
        "quickstart": "pip install ultralytics\nyolo predict model=yolov10n.pt source='camera.mp4'",
        "specs": "YOLOv10-Nano consome menos de 2.3M parâmetros",
        "veredito": "A melhor opção para visão computacional em tempo real em drones, câmeras IP e totens.",
        "github": "https://github.com/THU-MIG/yolov10"
    },
    {
        "rank": 17, "nome": "OpenVINO", "subtitulo": "Toolkit de Otimização e Deploy de IA em Hardware Intel",
        "substitui": "Intel Closed Toolkits", "categoria": "Hardware Acceleration (Intel)",
        "economia": "Zero Royalties", "licenca": "Apache-2.0", "kind": "HARDWARE ACCEL",
        "o_que_faz": "Maximiza o desempenho de modelos de IA em processadores Intel (Core, Xeon), GPUs integradas e novas NPUs Intel Core Ultra.",
        "como_funciona": "Converte modelos de qualquer origem e aplica quantização INT8 automática com aceleração pelas instruções Intel AVX-512 e AMX.",
        "quickstart": "pip install openvino\nimport openvino as ov",
        "specs": "Aceleração de até 5x em CPUs Intel comuns",
        "veredito": "Essencial para extrair desempenho de IA sem precisar comprar placas de vídeo dedicadas caras.",
        "github": "https://github.com/openvinotoolkit/openvino"
    },
    {
        "rank": 18, "nome": "RKNN-Toolkit", "subtitulo": "Toolkit de Aceleração de NPU para Placas ARM Rockchip",
        "substitui": "SDKs Fechados de NPU", "categoria": "NPU ARM Acceleration",
        "economia": "Soberania Total", "licenca": "Apache-2.0", "kind": "NPU ACCEL",
        "o_que_faz": "Permite rodar modelos de deep learning e LLMs quantizados direto na NPU dedicada de placas como Orange Pi 5 e chips Rockchip RK3588.",
        "como_funciona": "Converte modelos ONNX/PyTorch para o formato `.rknn`, atingindo 6 TOPS de poder de processamento em dispositivos de $ 100.",
        "quickstart": "pip install rknn-toolkit2",
        "specs": "6 TOPS de potência com consumo de apenas 5 Watts",
        "veredito": "A base para construir câmeras inteligentes e servidores de IA de borda baratos e ultra-potentes.",
        "github": "https://github.com/rockchip-linux/rknn-toolkit2"
    },
    {
        "rank": 19, "nome": "GGML", "subtitulo": "Biblioteca Tensorial em C Puro para Aprendizado de Máquina",
        "substitui": "Bibliotecas BLAS Proprietárias", "categoria": "Tensor Library em C",
        "economia": "Incalculável", "licenca": "MIT", "kind": "TENSOR CORE",
        "o_que_faz": "Biblioteca minimalista de tensores em C puro que gerencia memória e operações matemáticas para inferência de modelos de bilhões de parâmetros.",
        "como_funciona": "Aloca toda a memória em buffers estáticos contíguos com zero fragmentação e suporte a quantização extrema de 1.5 a 8 bits.",
        "quickstart": "git clone https://github.com/ggerganov/ggml.git\nmkdir build && cd build && cmake .. && make",
        "specs": "Zero alocação dinâmica durante a inferência · Suporta x86 e ARM",
        "veredito": "O coração computacional por trás do Llama.cpp e Whisper.cpp.",
        "github": "https://github.com/ggerganov/ggml"
    },
    {
        "rank": 20, "nome": "FastDeploy", "subtitulo": "Kit de Deploy Rápido de IA da Baidu para Dispositivos de Borda",
        "substitui": "Triton Server em Edge", "categoria": "Edge Deployment Kit",
        "economia": "Zero Licença", "licenca": "Apache-2.0", "kind": "DEPLOYMENT TOOLKIT",
        "o_que_faz": "SDK de deploy completo que suporta mais de 160 modelos populares de visão, OCR e NLP com integração pronta para Android, iOS, Linux e Windows.",
        "como_funciona": "Empacota múltiplos motores de inferência (TensorRT, OpenVINO, ONNX, NCNN) em uma única API em C++ e Python simples.",
        "quickstart": "pip install fastdeploy-python",
        "specs": "+160 modelos pré-otimizados prontos para deploy",
        "veredito": "Reduz o tempo de colocar um modelo de IA em produção de semanas para poucas horas.",
        "github": "https://github.com/PaddlePaddle/FastDeploy"
    }
]

html_38 = render_html(
    38, "Camada 38 · Inteligência Artificial de Borda",
    "Edge AI & On-Device Inference",
    "Como rodar <strong>LLMs, visão computacional e transcrição de áudio 100% offline em smartphones, tablets, Raspberry Pi e NPUs de borda</strong> com zero latência, zero consumo de dados móveis e zero custos de APIs em nuvem.",
    ["<b>20</b> tecnologias auditadas", "<b>Zero Nuvem:</b> 100% local no hardware do usuário", "<b>Dispositivos:</b> Android, iOS, Apple Silicon & ARM/NPUs"],
    {"accent": "#1B5E3B", "accent_soft": "#D8EFE2", "accent_dark": "#6BC48F", "accent_dark_soft": "#122B1C"},
    items_38
)
with open(os.path.join(OUTPUT_DIR, "38-edge-ai-on-device-inference-mobile.html"), "w", encoding="utf-8") as f:
    f.write(html_38)
print("[✓] Camada 38 gerada com 20 fichas completas.")

# ==============================================================================
# CAMADA 39: LEGALTECH, GESTÃO JURÍDICA & PRESERVAÇÃO DOCUMENTAL
# ==============================================================================
items_39 = [
    {
        "rank": 1, "nome": "Paperless-ngx", "subtitulo": "O Cérebro de Indexação e OCR Jurídico",
        "substitui": "Projuris GED / M-Files Jurídico", "categoria": "OCR & Indexação de Processos",
        "economia": "-$ 18.000 / ano", "licenca": "GPLv3", "kind": "GED JURÍDICO",
        "o_que_faz": "Indexação e organização automática de petições, sentenças, laudos e contratos com OCR multilíngue automático, classificação por tags e busca textual em tempo real.",
        "como_funciona": "Consome PDFs escaneados ou documentos em lote, extrai o texto com Tesseract OCR, categoriza por processo/cliente e arquiva em disco seguro.",
        "quickstart": "docker run -d -p 8000:8000 ghcr.io/paperless-ngx/paperless-ngx:latest",
        "specs": "OCR Tesseract nativo · Busca full-text instantânea em autos pesados",
        "veredito": "Elimina horas perdidas procurando termos em centenas de páginas de processos digitalizados.",
        "github": "https://github.com/paperless-ngx/paperless-ngx"
    },
    {
        "rank": 2, "nome": "DocuSeal", "subtitulo": "Plataforma de Assinatura Eletrônica com Validade Jurídica",
        "substitui": "DocuSign / Clicksign / ZapSign", "categoria": "Assinatura Eletrônica Legal",
        "economia": "-$ 12.000 / ano", "licenca": "AGPLv3", "kind": "E-SIGNATURE",
        "o_que_faz": "Plataforma de coleta e gerenciamento de assinaturas eletrônicas com trilha de auditoria completa, IP, geolocalização e carimbo de tempo (MP 2.200-2 / ICP-Brasil).",
        "como_funciona": "Interface moderna para envio de contratos e procurações via link ou e-mail com campos de assinatura, rubrica e preenchimento guiado.",
        "quickstart": "docker run -d -p 3000:3000 docusealco/docuseal:latest",
        "specs": "Trilha de auditoria criptográfica · PDF assinado com certificado digital",
        "veredito": "Acaba com os planos caros cobrados por envelope assinado do DocuSign.",
        "github": "https://github.com/docusealco/docuseal"
    },
    {
        "rank": 3, "nome": "Stirling-PDF", "subtitulo": "A Suíte Suprema para Manipulação e Higienização de PDFs",
        "substitui": "Adobe Acrobat Pro ($ 240/user/ano)", "categoria": "Manipulação de PDFs do PJe",
        "economia": "-$ 8.000 / ano", "licenca": "MIT", "kind": "PDF SUITE",
        "o_que_faz": "Permite dividir, juntar, comprimir para o limite de tamanho do PJe (ex: < 10MB), remover senhas, converter formatos e higienizar metadados de PDFs.",
        "como_funciona": "Interface web completa e privada que roda localmente sem enviar documentos confidenciais de clientes para servidores de terceiros.",
        "quickstart": "docker run -d -p 8080:8080 frooodle/s-pdf:latest",
        "specs": "+40 operações avançadas com PDFs · Zero vazamento de dados",
        "veredito": "A ferramenta mais prática do dia a dia para advogados que lidam com arquivos pesados de tribunais.",
        "github": "https://github.com/Stirling-Tools/Stirling-PDF"
    },
    {
        "rank": 4, "nome": "Docassemble", "subtitulo": "Automação de Petições e Minutas com Lógica Condicional",
        "substitui": "HotDocs / Neota Logic", "categoria": "Automação de Petições",
        "economia": "-$ 25.000 / ano", "licenca": "MIT", "kind": "LEGAL AUTOMATION",
        "o_que_faz": "Cria entrevistas guiadas na web que coletam dados de clientes e geram petições iniciais, contestações e contratos complexos automaticamente.",
        "como_funciona": "Usa Python e templates Jinja/DOCX com lógica condicional avançada (ex: 'se casado sob comunhão universal, insira a cláusula X').",
        "quickstart": "docker run -d -p 80:80 -p 443:443 jhpyle/docassemble",
        "specs": "Entrevistas interativas no navegador · Exporta em DOCX e PDF",
        "veredito": "Reduz o tempo de confecção de peças jurídicas repetitivas de 2 horas para 5 minutos.",
        "github": "https://github.com/jhpyle/docassemble"
    },
    {
        "rank": 5, "nome": "Twenty CRM", "subtitulo": "CRM Moderno para Controle de Clientes & Honorários",
        "substitui": "Astrea CRM / Salesforce Jurídico", "categoria": "CRM Jurídico & Honorários",
        "economia": "-$ 15.000 / ano", "licenca": "Apache-2.0", "kind": "LEGAL CRM",
        "o_que_faz": "Gerencia o pipeline de novos clientes da banca, histórico de atendimentos, propostas de honorários e tarefas de acompanhamento processual.",
        "como_funciona": "Interface moderna com visualização em Kanban, campos personalizados (Número CNJ, Vara, Comarca) e sincronização de e-mails.",
        "quickstart": "docker compose up -d # Usando repositório do Twenty",
        "specs": "Kanban interativo · Campos personalizados para autos judiciais",
        "veredito": "Organiza a captação de clientes e o relacionamento de bancas de advocacia com perfeição.",
        "github": "https://github.com/twentyhq/twenty"
    },
    {
        "rank": 6, "nome": "OpenContracts", "subtitulo": "Análise e Extração de Cláusulas Contratuais com IA",
        "substitui": "Kira Systems / Luminance", "categoria": "Análise de Contratos com IA",
        "economia": "-$ 30.000 / ano", "licenca": "Apache-2.0", "kind": "CONTRACT AI",
        "o_que_faz": "Plataforma de anotação e extração de dados jurídicos que usa modelos de linguagem para identificar riscos, datas de vencimento e cláusulas abusivas.",
        "como_funciona": "Processa centenas de contratos em lote e extrai tabelas comparativas para auditorias de Due Diligence e M&A.",
        "quickstart": "docker compose -f docker-compose.yml up -d # Repositório OpenContracts",
        "specs": "Extração de cláusulas com IA · Anotação visual de PDFs",
        "veredito": "Permite que escritórios façam Due Diligence de milhares de contratos em uma fração do tempo.",
        "github": "https://github.com/JSv4/OpenContracts"
    },
    {
        "rank": 7, "nome": "Cryptomator", "subtitulo": "Criptografia de Arquivos em Repouso para Nuvens Públicas",
        "substitui": "Cofres em Nuvem Proprietários", "categoria": "Criptografia Client-Side",
        "economia": "Incalculável", "licenca": "GPLv3", "kind": "ENCRYPTION",
        "o_que_faz": "Criptografa arquivos individualmente no seu computador antes de sincronizá-los com Google Drive, OneDrive ou Dropbox, garantindo sigilo total.",
        "como_funciona": "Cria um drive virtual criptografado com AES-256 onde cada arquivo e nome de pasta é transformado em dados ilegíveis para o provedor de nuvem.",
        "quickstart": "sudo apt install cryptomator # ou instalador Windows",
        "specs": "Criptografia AES-256 E2E · Zero conhecimento por parte da nuvem",
        "veredito": "Garante a conformidade ética da OAB e da LGPD mesmo armazenando documentos em nuvens públicas.",
        "github": "https://github.com/cryptomator/cryptomator"
    },
    {
        "rank": 8, "nome": "VeraCrypt", "subtitulo": "Cofre Criptográfico para Preservação de Provas Periciais",
        "substitui": "BitLocker Fechado", "categoria": "Cofre Forense de Provas",
        "economia": "Incalculável", "licenca": "Apache-2.0", "kind": "FORENSIC VAULT",
        "o_que_faz": "Cria volumes virtuais criptografados ou criptografa partições inteiras de discos e pendrives contendo mídias e provas periciais sensíveis.",
        "como_funciona": "Utiliza algoritmos de nível militar (AES, Serpent, Twofish) em cascata com proteção contra coerção através de volumes ocultos.",
        "quickstart": "veracrypt --create /caminho/volume.tc",
        "specs": "Criptografia em cascata · Volumes ocultos indetectáveis",
        "veredito": "A ferramenta padrão para advogados criminalistas e peritos forenses guardarem provas digitais.",
        "github": "https://github.com/veracrypt/VeraCrypt"
    },
    {
        "rank": 9, "nome": "Apache Tika", "subtitulo": "Extração Automatizada de Metadados e Conteúdo Textual",
        "substitui": "Parsers Pagos de Documentos", "categoria": "Extração de Metadados",
        "economia": "-$ 10.000 / ano", "licenca": "Apache-2.0", "kind": "DOC PARSER",
        "o_que_faz": "Detecta e extrai metadados e conteúdo textual de mais de 1.000 tipos de arquivos diferentes (DOCX, PDF, RTF, E-mails MSG, Áudios).",
        "como_funciona": "Servidor de parsing de documentos que entrega o texto limpo via API REST para alimentar bases RAG e sistemas de busca jurídica.",
        "quickstart": "docker run -d -p 9998:9998 apache/tika:latest",
        "specs": "Suporte a +1.000 formatos · Extração de metadados ocultos",
        "veredito": "O motor invisível que permite vasculhar arquivos anexados em processos judiciais.",
        "github": "https://github.com/apache/tika"
    },
    {
        "rank": 10, "nome": "OCRmyPDF", "subtitulo": "Conversão em Lote de Autos Escaneados em PDFs Pesquisáveis",
        "substitui": "ABBYY FineReader Server", "categoria": "OCR em Lote",
        "economia": "-$ 14.000 / ano", "licenca": "MPL-2.0", "kind": "BATCH OCR",
        "o_que_faz": "Adiciona uma camada de texto pesquisável com OCR sobre páginas escaneadas de PDFs sem alterar a qualidade visual da imagem original.",
        "como_funciona": "Corrige rotação de páginas tortas, limpa ruídos de escaneamento e injeta a camada de texto OCR perfeita no padrão PDF/A.",
        "quickstart": "ocrmypdf -l por processo_escaneado.pdf processo_pesquisavel.pdf",
        "specs": "Gera arquivos no padrão arquivístico PDF/A · Suporte a GPU",
        "veredito": "Essencial para tornar pesquisável aquele processo antigo de 500 páginas escaneadas tortas.",
        "github": "https://github.com/ocrmypdf/OCRmyPDF"
    },
    {
        "rank": 11, "nome": "Vaultwarden", "subtitulo": "Guarda Segura de Tokens PJe e Certificados Digitais",
        "substitui": "1Password Teams", "categoria": "Guarda de Senhas & Certificados",
        "economia": "-$ 5.000 / ano", "licenca": "AGPLv3", "kind": "CERTIFICATE VAULT",
        "o_que_faz": "Armazena senhas de sistemas de tribunais (PJe, e-SAJ, Projudi, Eproc) e notas seguras com PINs de certificados A1/A3 compartilhadas na banca.",
        "como_funciona": "Cofre com criptografia de ponta a ponta que pode ser acessado por sócios e associados com controle estrito de permissões.",
        "quickstart": "docker run -d -p 8080:80 -v /dados/vw:/data vaultwarden/server:latest",
        "specs": "Criptografia E2E · Zero risco de perda de senhas de tribunais",
        "veredito": "Acaba com o perigo de senhas de tribunais anotadas em papéis na mesa da secretaria.",
        "github": "https://github.com/dani-garcia/vaultwarden"
    },
    {
        "rank": 12, "nome": "Mattermost", "subtitulo": "Comunicação Sigilosa e Criptografada para Sócios",
        "substitui": "Slack / Grupos de WhatsApp", "categoria": "Chat Seguro da Banca",
        "economia": "-$ 10.000 / ano", "licenca": "AGPLv3", "kind": "SECURE CHAT",
        "o_que_faz": "Plataforma de mensagens instantâneas e colaboração interna hospedada no próprio servidor do escritório, garantindo sigilo profissional absoluto.",
        "como_funciona": "Canais organizados por caso/cliente com busca no histórico, chamadas de voz criptografadas e conformidade total com a LGPD.",
        "quickstart": "docker run -d -p 8065:8065 mattermost/mattermost-team-edition",
        "specs": "Hospedagem 100% on-premise · Zero mineração de dados",
        "veredito": "A alternativa segura para tirar discussões de estratégias de processos de grupos informais de WhatsApp.",
        "github": "https://github.com/mattermost/mattermost"
    },
    {
        "rank": 13, "nome": "Nextcloud Hub", "subtitulo": "Portal Seguro de Troca de Autos e Documentos com Clientes",
        "substitui": "SharePoint Jurídico / Google Drive", "categoria": "Portal de Arquivos da Banca",
        "economia": "-$ 15.000 / ano", "licenca": "AGPLv3", "kind": "CLIENT PORTAL",
        "o_que_faz": "Permite criar pastas seguras para cada cliente enviar documentos e acessar cópias de petições e laudos com controle de validade e senha.",
        "como_funciona": "Servidor de nuvem privada com editor de texto colaborativo, visualizador de PDFs e links protegidos contra download indevido.",
        "quickstart": "docker run -d -p 8080:80 nextcloud:latest",
        "specs": "Controle de expiração de links · Auditoria de downloads",
        "veredito": "Transmite uma imagem de extremo profissionalismo e segurança tecnológica para os clientes da banca.",
        "github": "https://github.com/nextcloud/server"
    },
    {
        "rank": 14, "nome": "SingleFile", "subtitulo": "Preservação Íntegra de Páginas da Web como Prova Judicial",
        "substitui": "Prints de Tela sem Validade", "categoria": "Preservação de Provas Web",
        "economia": "Incalculável", "licenca": "AGPLv3", "kind": "EVIDENCE CAPTURE",
        "o_que_faz": "Salva páginas inteiras da web (postagens de redes sociais, notícias, conversas) em um único arquivo HTML autocontido e imutável.",
        "como_funciona": "Incorpora imagens, fontes e folhas de estilo no próprio HTML mantendo a fidelidade visual exata para juntada em ata notarial ou petição.",
        "quickstart": "npm install -g 'single-file-cli'\nsingle-file https://site.com/post prova.html",
        "specs": "Arquivo HTML único com todos os recursos embutidos",
        "veredito": "Evita que prints de tela sejam impugnados pela parte contrária por falta de integridade contextual.",
        "github": "https://github.com/gildas-lormeau/SingleFile"
    },
    {
        "rank": 15, "nome": "Redact", "subtitulo": "Higienização e Tarjamento Automático de Dados (LGPD)",
        "substitui": "Ferramentas de Tarjamento Pagas", "categoria": "Tarjamento & Anonimização",
        "economia": "-$ 6.000 / ano", "licenca": "MIT", "kind": "REDACTION TOOL",
        "o_que_faz": "Remove e tarja dados sensíveis (CPFs, dados bancários, laudos médicos) de peças jurídicas antes da publicação pública ou compartilhamento.",
        "como_funciona": "Remove os dados permanentemente da estrutura interna do PDF (e não apenas desenha uma caixa preta por cima), impedindo extração de texto.",
        "quickstart": "docker run -d -p 8080:8080 redact/server",
        "specs": "Tarjamento destrutivo e irreversível de texto e imagens",
        "veredito": "Evita multas pesadas da ANPD por vazamento de dados de partes em processos públicos.",
        "github": "https://github.com/danfickle/openhtmltopdf"
    },
    {
        "rank": 16, "nome": "Cal.com", "subtitulo": "Agendamento Automático de Consultas e Audiências",
        "substitui": "Calendly Pro", "categoria": "Agendamento Jurídico",
        "economia": "-$ 3.000 / ano", "licenca": "AGPLv3", "kind": "BOOKING PLATFORM",
        "o_que_faz": "Permite que clientes agendem reuniões e consultas iniciais diretamente na agenda dos advogados respeitando os horários de audiências.",
        "como_funciona": "Sincroniza em tempo real com Google Calendar e Outlook, enviando links de videochamada e confirmações por WhatsApp.",
        "quickstart": "docker compose up -d # Usando repositório do Cal.com",
        "specs": "Sincronização bidirecional · Suporte a múltiplos advogados",
        "veredito": "Elimina a troca infindável de e-mails para encontrar um horário livre na agenda dos sócios.",
        "github": "https://github.com/calcom/cal.com"
    },
    {
        "rank": 17, "nome": "Firefly III", "subtitulo": "Controle Financeiro de Honorários, Custas e Sucumbência",
        "substitui": "Sistemas Financeiros Fechados", "categoria": "Gestão Financeira Jurídica",
        "economia": "-$ 5.000 / ano", "licenca": "AGPLv3", "kind": "FINANCIAL MGT",
        "o_que_faz": "Gerencia o fluxo de caixa do escritório, separando receitas de honorários contratuais, honorários de sucumbência e reembolso de custas de clientes.",
        "como_funciona": "Sistema de partidas dobradas com emissão de relatórios detalhados de despesas por processo judicial.",
        "quickstart": "docker run -d -p 8080:8080 fireflyiii/core:latest",
        "specs": "Partidas dobradas estritas · Separação por centro de custos/processo",
        "veredito": "Garante clareza absoluta sobre a lucratividade real de cada caso atendido pelo escritório.",
        "github": "https://github.com/firefly-iii/firefly-iii"
    },
    {
        "rank": 18, "nome": "Formbricks", "subtitulo": "Triagem Inicial e Captação de Casos Jurídicos",
        "substitui": "Typeform Pro", "categoria": "Formulários de Triagem",
        "economia": "-$ 4.000 / ano", "licenca": "AGPLv3", "kind": "SURVEY / INTAKE",
        "o_que_faz": "Formulários interativos e elegantes para coletar o relato inicial dos fatos e documentos de novos clientes antes da primeira consulta.",
        "como_funciona": "Interface fluida de perguntas passo a passo com integração direta ao CRM da banca para qualificar potenciais clientes.",
        "quickstart": "docker run -d -p 3000:3000 formbricks/formbricks:latest",
        "specs": "Perguntas condicionais · Integração via webhook com n8n/CRM",
        "veredito": "Qualifica os melhores casos e economiza tempo de atendimento da equipe jurídica.",
        "github": "https://github.com/formbricks/formbricks"
    },
    {
        "rank": 19, "nome": "PDFtk", "subtitulo": "Ferramenta de Linha de Comando para Manipulação em Lote de Autos",
        "substitui": "Softwares de Divisão de PDFs Pagos", "categoria": "CLI PDF Processor",
        "economia": "-$ 2.000 / ano", "licenca": "GPLv2", "kind": "CLI UTILITY",
        "o_que_faz": "Utilitário rápido de terminal para dividir peças em blocos menores, juntar anexos e carimbar numeração de páginas em lote.",
        "como_funciona": "Processa centenas de páginas em menos de 1 segundo direto da linha de comando ou via scripts automatizados.",
        "quickstart": "pdftk inicial.pdf anexo1.pdf anexo2.pdf cat output peticao_completa.pdf",
        "specs": "Execução instantânea em terminal sem interface gráfica",
        "veredito": "O clássico indispensável para scripts de automação de juntada de documentos.",
        "github": "https://github.com/pdftk"
    },
    {
        "rank": 20, "nome": "LibreOffice CLI", "subtitulo": "Conversão e Geração Automatizada de Minutas em Lote",
        "substitui": "Microsoft Office 365 Pro", "categoria": "Headless Document Engine",
        "economia": "-$ 8.000 / ano", "licenca": "MPL-2.0", "kind": "HEADLESS OFFICE",
        "o_que_faz": "Converte minutas em DOCX, RTF e ODT diretamente para PDF pelo terminal sem precisar abrir o editor de texto interativo.",
        "como_funciona": "Modo headless que pode ser invocado por scripts Python ou n8n para gerar dezenas de contratos em PDF por minuto.",
        "quickstart": "libreoffice --headless --convert-to pdf minuta_contrato.docx",
        "specs": "Modo headless leve · Suporte completo a templates DOCX",
        "veredito": "A base para qualquer esteira de geração automatizada de contratos em larga escala.",
        "github": "https://github.com/LibreOffice/core"
    }
]

html_39 = render_html(
    39, "Camada 39 · Tecnologia Jurídica & LegalTech",
    "LegalTech & Gestão Jurídica Soberana",
    "O ecossistema definitivo para escritórios de advocacia e departamentos jurídicos: <strong>OCR e indexação profunda de processos, assinatura eletrônica com validade jurídica e controle de prazos</strong> substituindo Projuris, SAJ ADV, Astrea e DocuSign.",
    ["<b>20</b> tecnologias auditadas", "<b>Economia:</b> -$ 18.000 a $ 60.000 / ano", "<b>Sigilo:</b> 100% On-Premise / Conformidade OAB & LGPD"],
    {"accent": "#7A5410", "accent_soft": "#EFE5CE", "accent_dark": "#D6A44E", "accent_dark_soft": "#332810"},
    items_39
)
with open(os.path.join(OUTPUT_DIR, "39-legaltech-gestao-juridica-soberana.html"), "w", encoding="utf-8") as f:
    f.write(html_39)
print("[✓] Camada 39 gerada com 20 fichas completas.")

print("\n[🎉] TODAS AS 5 LISTAS FORAM COMPILADAS COM 20 FICHAS CADA E CABEÇALHO PADRONIZADO!")
