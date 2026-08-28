
#set page(
  paper: "a4",
  margin: (x: 1.5cm, top: 2.2cm, bottom: 2.0cm),
  header: align(center)[
    #text(size: 8pt, fill: rgb("#64748b"), font: "Liberation Sans")[
      Fábrica Universal AIDD · Tratado de Engenharia Agêntica para Não-Técnicos
    ]
  ],
  footer: [
    #set par(leading: 0.65em)
    #text(size: 8pt, fill: rgb("#64748b"), font: "Liberation Sans")[
      #grid(
        columns: (1fr, 1fr),
        [Livro-Texto do Engenheiro Agêntico · Penso Mail & Collaboration Suite],
        align(right)[Fábrica Universal AIDD]
      )
    ]
  ]
)

#set text(
  font: "Liberation Serif",
  size: 9.5pt,
  fill: rgb("#1b1e23"),
  lang: "pt"
)

#set par(
  justify: true,
  leading: 0.55em,
  first-line-indent: 0pt
)

#show heading: set text(fill: rgb("#0f172a"), font: "Liberation Sans")
#show heading.where(level: 1): it => {
  v(14pt, weak: true)
  text(size: 15pt, weight: "bold")[#it.body]
  v(8pt, weak: true)
}
#show heading.where(level: 2): it => {
  v(10pt, weak: true)
  text(size: 11pt, weight: "bold", fill: rgb("#00875a"))[#it.body]
  v(6pt, weak: true)
}

#align(center)[
  #v(16pt)
  #text(size: 20pt, weight: "bold", fill: rgb("#0f172a"))[LIVRO-TEXTO DO ENGENHEIRO AGÊNTICO]
  #v(6pt)
  #text(size: 11pt, style: "italic", fill: rgb("#475569"))[Guia Definitivo para Não-Técnicos: Como Subir sua Infraestrutura Própria com IA, Termius e Uptime Kuma]
  #v(4pt)
  #text(size: 9.5pt, weight: "bold", fill: rgb("#00875a"))[Suíte Alvo: Penso Mail & Collaboration Suite · Substitui Penso Suite (Zimbra Collaboration, Penso Drive, Penso Antispam)]
  #v(14pt)
]

= Capítulo 01: A Revolução da Engenharia Agêntica
No modelo antigo de tecnologia, advogados, médicos e analistas dependiam de caríssimas equipes de TI para gerenciar servidores ou ficavam reféns de mensalidades abusivas de softwares fechados. Na *Engenharia Agêntica*, você se torna o Diretor da sua própria infraestrutura: munido de *Prompts Mestres* rigorosamente testados, você orienta Agentes de Inteligência Artificial para realizar o provisionamento, deploy e manutenção da sua VPS sem escrever uma única linha de código manual.

= Capítulo 02: Dicionário Descomplicado (Analogias do Mundo Real)
- *VPS (Servidor Privado Virtual):* O seu computador comercial blindado na nuvem, ativo 24h por dia sem risco de interrupção elétrica;
- *Docker & Contêineres:* Cápsulas de isolamento digital. O e-mail, a nuvem e o chat rodam em cápsulas separadas sem risco de contaminação;
- *Traefik & SSL:* O porteiro digital que garante o cadeado verde de criptografia (HTTPS) em todos os seus endereços na web;
- *Termius:* O controle remoto criptográfico de alta segurança para você acessar e auditar seu servidor de qualquer celular ou computador;
- *Uptime Kuma:* O vigia 24h que testa seus sistemas a cada minuto e alerta imediatamente no WhatsApp se algum serviço oscilar;
- *Keycloak SSO:* O crachá digital unificado para que sua equipe acerte todos os módulos com uma única senha segura e autenticação 2FA.

#pagebreak()
= Capítulo 03: Os 4 Prompts Mestres de Execução Autônoma
Para colocar toda a sua suíte no ar, basta copiar e colar os 4 blocos abaixo sequencialmente no seu assistente de IA:

== Prompt Mestre 01: Provisionamento & Hardening da VPS
```bash
# PROMPT MESTRE 01 · PROVISIONAMENTO & HARDENING DA VPS
Você é um Engenheiro de Infraestrutura e Segurança Sênior operando como Agente Autônomo.
Objetivo: Preparar e blindar a VPS Ubuntu 24.04 LTS para hospedar a suíte Penso Mail & Collaboration Suite.

Protocolo de Execução:
1. Conecte-se na VPS via SSH usando autenticação por chave Ed25519 (Termius / OpenSSH);
2. Atualize os pacotes do sistema: apt update && apt upgrade -y;
3. Configure o Firewall UFW:
   ufw default deny incoming
   ufw default allow outgoing
   ufw allow 22/tcp (ou porta SSH customizada)
   ufw allow 80/tcp
   ufw allow 443/tcp
   ufw --force enable
4. Instale e configure o Fail2ban para proteção contra força bruta no SSH;
5. Instale a versão mais recente do Docker Engine e Docker Compose Plugin oficial;
6. Crie a rede interna isolada: docker network create sovereign_net;
7. Valide a instalação executando: docker info && ufw status.

```

== Prompt Mestre 02: Deploy do Cluster All-in-One Compose
```bash
# PROMPT MESTRE 02 · DEPLOY ALL-IN-ONE DA SUÍTE SOBERANA
Você é um Engenheiro DevOps Sênior operando como Agente Autônomo.
Objetivo: Realizar o deploy completo da suíte Penso Mail & Collaboration Suite (Penso Suite (Zimbra Collaboration, Penso Drive, Penso Antispam)).

Protocolo de Execução:
1. Crie o diretório base: mkdir -p /opt/sovereign-suite && cd /opt/sovereign-suite;
2. Escreva o arquivo de variáveis .env com credenciais de produção criptograficamente seguras;
3. Escreva o manifesto docker-compose.yml canônico unificado (Traefik, Keycloak SSO, módulos do Quinteto e bancos PostgreSQL/Redis);
4. Configure as labels de roteamento do Traefik para emissão automática de certificados SSL Let's Encrypt para os subdomínios da empresa;
5. Suba o cluster: docker compose up -d;
6. Monitore a inicialização dos contêineres: docker compose logs -f --tail=100;
7. Valide que todos os serviços estão com status 'healthy' ou 'running'.

```

== Prompt Mestre 03: Configuração do Vigia 24h (Uptime Kuma)
```bash
# PROMPT MESTRE 03 · MONITORAMENTO EM TEMPO REAL (UPTIME KUMA)
Você é um Engenheiro SRE / Observabilidade operando como Agente Autônomo.
Objetivo: Configurar a observabilidade em tempo real e os canais de alerta da suíte Penso Mail & Collaboration Suite.

Protocolo de Execução:
1. Adicione o serviço Uptime Kuma ao docker-compose.yml da suíte e suba o contêiner;
2. Acesse a API ou crie via script os monitores para:
   - Traefik HTTPS Gateway (Validação de resposta HTTP 200 e expiração de certificado SSL);
   - Serviços do Pilar 01, 02 e 03 (E-mail, Drive e Chat);
   - Keycloak SSO Endpoint;
3. Configure o canal de notificação de incidentes (Webhook para Mattermost / WhatsApp via n8n);
4. Execute um teste de disparo de alerta simulando parada temporária de um contêiner;
5. Disponibilize a Status Page corporativa pública ou interna para a equipe.

```

== Prompt Mestre 04: Smoke Tests & Validação de DRP
```bash
# PROMPT MESTRE 04 · SMOKE TESTS & VALIDAÇÃO DE DISASTER RECOVERY (DRP)
Você é um Engenheiro de QA & Auditoria de Infraestrutura operando como Agente Autônomo.
Objetivo: Executar os testes de fumaça (Smoke Tests) e auditoria de backup da suíte Penso Mail & Collaboration Suite.

Protocolo de Execução:
1. Valide a resolução de DNS e certificados HTTPS de todos os subdomínios corporativos;
2. Teste o fluxo de login único OIDC via Keycloak;
3. Teste o upload de arquivos no Drive corporativo e envio/recebimento de mensagens de e-mail e chat;
4. Execute o script de backup automatizado 3-2-1 (/opt/scripts/backup.sh) e verifique a integridade do arquivo gerado;
5. Simule a restauração do banco de dados em um banco de testes para garantir 100% de recuperabilidade em caso de desastre;
6. Emita o Relatório Executivo de Homologação em Produção com veredito final.

```
