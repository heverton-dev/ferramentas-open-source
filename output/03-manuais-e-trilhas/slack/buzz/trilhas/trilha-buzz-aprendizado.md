# Trilha Cronológica de Aprendizado: Block BUZZ

> **Jornada Pedagógica Autoguiada · Imersão a Partir das Fontes Primárias**  
> **Tempo Total Estimado:** 10 a 14 horas (2 semanas a 1-2 horas diárias) | **Fases:** 5 Módulos  
> **Dossiê SaaS de Origem:** Slack

---

## Fundação: O que é BUZZ e Por Que é Revolucionário (`⏱️ 2 horas`)
**🎯 Meta da Etapa:** Entender que BUZZ é Slack open source com suporte nativo a agentes IA, diferente de Slack/Teams porque você controla tudo, e aprender o que é protocolo Nostr.

- [ ] **[Introdução ao Block BUZZ - Visão Geral](https://www.youtube.com/watch?v=DpiAtwZODnw)** (`Video YouTube` - `[T01]`)
  - 💡 **O que você aprende:** BUZZ é mensageria descentralizada open source para equipes. Proteger privacidade. Controle total dos dados. Agent-native (bots integrados nativamente). Alternativa ao Slack/Teams/Discord que custa zero (após VPS).
  - ⏱️ 12 minutos | 👤 Block (Jack Dorsey)

- [ ] **[BUZZ vs Slack vs Teams - Comparação Executiva](https://github.com/block/buzz#comparison)** (`Artigo Técnico` - `[T02]`)
  - 💡 **O que você aprende:** Slack: USD 8-12/usuário/mês, Salesforce controla dados, sem suporte nativo a agentes. Teams: USD 6-20/usuário/mês, Microsoft controla dados. BUZZ: R$ 80-300/mês de VPS ilimitado, você controla dados, agentes nativas. ROI 100x melhor.
  - ⏱️ 10 minutos de leitura | 👤 Block Developers

- [ ] **[Nostr Protocol - Explicado Para Não-Técnicos](https://github.com/nostr-protocol/nips#introduction)** (`Artigo Didático` - `[T03]`)
  - 💡 **O que você aprende:** Nostr é protocolo descentralizado (como email, mas moderno). Mensagens assinadas com criptografia. Vários relays (servidores) que conversam. Você não fica preso a um relay. BUZZ usa Nostr para sincronizar mensagens.
  - ⏱️ 8 minutos de leitura | 👤 Arsenal Open Source

- [ ] **[Agent-Native: Por Que BUZZ foi Feito para Bots](https://block.xyz/inside/introducing-buzz-where-humans-and-agents-work-together)** (`Blog Post` - `[T04]`)
  - 💡 **O que você aprende:** Slack/Teams foram desenhados para humanos. BUZZ foi desenhado para humanos E agentes IA trabalharem juntos. Um bot pode ser membro de canal, postar, processar mensagens, executar ações. Tudo nativo.
  - ⏱️ 10 minutos de leitura | 👤 Block Engineering

## Instalação em Produção: Colocar BUZZ em VPS (`⏱️ 3 horas`)
**🎯 Meta da Etapa:** Ter BUZZ rodando em VPS com Docker Compose, acessível via HTTPS, primeiro usuário criado e workspace pronto.

- [ ] **[Pré-Requisitos: Hardware, Domínio, DNS](https://github.com/block/buzz#prerequisites)** (`Checklist Técnico` - `[T05]`)
  - 💡 **O que você aprende:** VPS com 4vCPU/8GB RAM + Linux. Docker + Docker Compose 24.x+. Domínio próprio (ex: buzz.empresa.com). DNS configurado apontando para IP da VPS. Certificado SSL via Let's Encrypt. Abrir ports 80/443.
  - ⏱️ 5 minutos | 👤 Arsenal Open Source

- [ ] **[Guia Passo-a-Passo: Instalar BUZZ em Ubuntu 22.04](file:///output/03-manuais-e-trilhas/slack/buzz/manuais/manual-buzz-vps-e-uso.html)** (`Manual Técnico` - `[T06]`)
  - 💡 **O que você aprende:** SSH → Docker/Compose → Rust/Node.js → Clone BUZZ → Gerar chaves Nostr → Docker Compose up → Caddy TLS → Setup wizard web. Cada passo testado, sem surpresas.
  - ⏱️ 90 minutos de execução | 👤 Arsenal Open Source

- [ ] **[Primeira Execução: Setup Wizard Web](https://www.youtube.com/results?search_query=buzz+setup+wizard+first+login)** (`Video Tutorial` - `[T07]`)
  - 💡 **O que você aprende:** Abrir https://buzz.sua-empresa.com.br. Criar usuário admin (email + senha). Criar primeiro workspace (nome da empresa). Pronto para uso!
  - ⏱️ 15 minutos | 👤 Comunidade BUZZ

- [ ] **[Verificação Pós-Deploy: Tudo Rodando?](https://github.com/block/buzz#healthcheck)** (`Checklist Técnico` - `[T08]`)
  - 💡 **O que você aprende:** docker compose ps (todos 'up'?). curl localhost:3000 (responde?). PostgreSQL conectando? Redis? MinIO? SSL válido? Logs de erro?
  - ⏱️ 10 minutos | 👤 Arsenal Open Source

## Uso Diário: Workspaces, Canais, Membros e Mensagens (`⏱️ 2 horas`)
**🎯 Meta da Etapa:** Dominar interface BUZZ: criar canais, convidar membros, enviar mensagens, threads, reações, compartilhar arquivos.

- [ ] **[Dashboard e Workspaces - Tour Guiado](https://github.com/block/buzz#ui-guide)** (`Video Tutorial` - `[T09]`)
  - 💡 **O que você aprende:** Dashboard mostra workspaces. Clique em um workspace. Você vê canais (#general, #random, etc). Clique em canal. Vê mensagens em tempo real. Cada elemento explicado.
  - ⏱️ 12 minutos | 👤 Arsenal Open Source

- [ ] **[Criar Canais e Configurar Permissões](https://www.youtube.com/results?search_query=buzz+create+channel+permissions)** (`Tutorial Prático` - `[T10]`)
  - 💡 **O que você aprende:** Clique '+' ao lado de canais. Novo canal (nome, descrição, público/privado). Adicionar membros. Definir quem pode postar, deletar, etc. Cada permissão explicada.
  - ⏱️ 15 minutos | 👤 Comunidade BUZZ

- [ ] **[Enviar Mensagens, Threads e Reações](https://github.com/block/buzz#messaging)** (`Guia Visual` - `[T11]`)
  - 💡 **O que você aprende:** Digitar mensagem e pressionar Enter. Thread: clique 'Reply' em mensagem (conversa aninhada). Reações: emoji sob mensagem. Editar/Deletar (hover sobre mensagem). Busca (Ctrl+F ou icon de lupa).
  - ⏱️ 10 minutos | 👤 Arsenal Open Source

- [ ] **[Upload de Arquivos e Mídia](https://github.com/block/buzz#media-upload)** (`Tutorial` - `[T12]`)
  - 💡 **O que você aprende:** Clique clip de attachment na caixa de mensagem. Upload arquivo/imagem/vídeo. Aparece inline na mensagem. Compartilhar com workspace. MinIO armazena seguro.
  - ⏱️ 8 minutos | 👤 Comunidade BUZZ

## Integração de Agentes: Bots e Automações (`⏱️ 2.5 horas`)
**🎯 Meta da Etapa:** Criar bot BUZZ que participa do workspace, responde a comandos, integra com APIs externas, automações sem código.

- [ ] **[Fundação: Como Bots Funcionam em BUZZ](https://github.com/block/buzz#bots-and-agents)** (`Guia Conceitual` - `[T13]`)
  - 💡 **O que você aprende:** BUZZ bot = usuário especial que processa mensagens via API/Webhooks. Recebe eventos (nova mensagem, reação, membro entrou). Responde com comando slash (/help, /remind, etc). Token de autenticação próprio. Acesso a channels/mensagens via API.
  - ⏱️ 12 minutos | 👤 Arsenal Open Source

- [ ] **[Criar Primeiro Bot com Webhooks](https://github.com/block/buzz#webhook-setup)** (`Tutorial Step-by-Step` - `[T14]`)
  - 💡 **O que você aprende:** 1. Gerar bot token em Admin Settings. 2. Criar webhook endpoint (seu servidor ou ngrok). 3. Registrar webhook URL em BUZZ. 4. Testar: postar mensagem, webhook recebe evento JSON. 5. Bot responde automaticamente.
  - ⏱️ 20 minutos | 👤 Comunidade BUZZ

- [ ] **[Slash Commands: Interação Direta com Bot](https://github.com/block/buzz#slash-commands)** (`Guia Prático` - `[T15]`)
  - 💡 **O que você aprende:** Definir comando: /remind. Usuário digita '/remind 10m fazer reunião'. Bot recebe evento. Bot responde com confirmação. No tempo, bot envia reminder no canal. Exemplo simples: /help, /stats, /weather, etc.
  - ⏱️ 15 minutos | 👤 Arsenal Open Source

- [ ] **[Integração com APIs Externas (Exemplo: OpenAI)](https://github.com/block/buzz#api-integrations)** (`Case Study` - `[T16]`)
  - 💡 **O que você aprende:** Bot recebe mensagem 'resumir documento.pdf'. Faz call a API OpenAI com conteúdo. Recebe resumo. Posta resumo no canal. Sem código manual, via flow builder (n8n/Zapier compatível).
  - ⏱️ 20 minutos | 👤 Arsenal Open Source

## Operação, Monitoramento e Manutenção 24/7 (`⏱️ 2.5 horas`)
**🎯 Meta da Etapa:** Monitorar saúde de BUZZ, resolver problemas, fazer backups, atualizar código, escalar recursos.

- [ ] **[Monitoramento Diário: Saúde do BUZZ](https://github.com/block/buzz#monitoring)** (`Checklist Daily` - `[T17]`)
  - 💡 **O que você aprende:** Comando: docker compose ps (todos 'up'?). docker compose logs buzz | tail -20 (erros?). df -h (disco OK?). free -m (memória OK?). curl https://buzz.seu-site.com (respondendo?). Se verde, está bem.
  - ⏱️ 5 minutos | 👤 Arsenal Open Source

- [ ] **[Troubleshooting: Problemas Comuns e Soluções](file:///output/03-manuais-e-trilhas/slack/buzz/manuais/manual-buzz-vps-e-uso.html#troubleshooting)** (`FAQ Técnico` - `[T18]`)
  - 💡 **O que você aprende:** BUZZ lento: aumentar RAM/CPU. WebSocket recusado: verificar Caddy TLS. PostgreSQL cheio: fazer VACUUM. MinIO fora de espaço: deletar mídia antigo. Certificado expirado: renovar Let's Encrypt.
  - ⏱️ 15 minutos | 👤 Arsenal Open Source

- [ ] **[Backups Automatizados: Proteger Dados](https://github.com/block/buzz#backup)** (`Guia de Backup` - `[T19]`)
  - 💡 **O que você aprende:** Script diário: backup PostgreSQL + Redis + MinIO. Salvar em /backups/ ou cloud (S3/OneDrive). Manter últimos 30 dias. Testar recovery mensal. Protege contra perda de dados.
  - ⏱️ 10 minutos | 👤 Arsenal Open Source

- [ ] **[Atualizar BUZZ e Dependências](https://github.com/block/buzz#updates)** (`Guia de Upgrade` - `[T20]`)
  - 💡 **O que você aprende:** BUZZ update: git pull origin main. Rebuild: docker compose build. Testar em dev primeiro. Deploy: docker compose up -d. Rollback se problema: git revert + docker compose up -d. Zero downtime se load balancer.
  - ⏱️ 10 minutos | 👤 BUZZ Community
