# Trilha Cronológica de Aprendizado: Mautic

> **Jornada Pedagógica Autoguiada · Imersão a Partir das Fontes Primárias**  
> **Tempo Total Estimado:** 8 a 12 horas (1 semana a 2 horas diárias) | **Fases:** 5 Módulos  
> **Dossiê SaaS de Origem:** Activecampaign

---

## Fundação: Entender o Ecossistema Mautic do Zero (`⏱️ 2 horas`)
**🎯 Meta da Etapa:** Saber exatamente o que é Mautic, por que é diferente de SaaS pago (ActiveCampaign, HubSpot), e os 4 pilares que fazem tudo funcionar: Leads, Formulários, Campanhas e Rastreamento.

- [ ] **[O que é Mautic? Explicação para Não-Técnicos](https://www.youtube.com/results?search_query=mautic+explicacao+portugues)** (`Video YouTube` - `[T01]`)
  - 💡 **O que você aprende:** Mautic é uma plataforma open source de marketing automation que você instala no seu próprio servidor (não SaaS). Você é o dono dos dados. Não há limite de contatos, emails ou campanhas. Tudo é automatizável.
  - ⏱️ 12 minutos | 👤 Mautic Brasil Community

- [ ] **[Mautic vs ActiveCampaign vs HubSpot - Comparação Completa](https://www.mautic.org/blog/)** (`Artigo de Blog` - `[T02]`)
  - 💡 **O que você aprende:** ActiveCampaign e HubSpot cobram por contato (USD 50-100/mês para 10k leads). Mautic é grátis, open source, sem limite de contatos. Você paga apenas a VPS (R$ 80/mês). ROI = 10x melhor.
  - ⏱️ 8 minutos de leitura | 👤 Mautic Official Blog

- [ ] **[Os 4 Pilares do Mautic - Vídeo Didático](https://youtube.com/c/ArsenalOpenSource)** (`Video YouTube` - `[T03]`)
  - 💡 **O que você aprende:** Pilar 1: Leads (banco de dados de contatos). Pilar 2: Formulários (captura de emails). Pilar 3: Campanhas (automação de email). Pilar 4: Rastreamento (saber quem visitou o site).
  - ⏱️ 15 minutos | 👤 Arsenal Open Source

- [ ] **[Documentação Oficial: Introdução ao Mautic](https://docs.mautic.org/en/5.1/)** (`Documentação Oficial` - `[T04]`)
  - 💡 **O que você aprende:** Mautic é modulado (você ativa/desativa features). Dashboard mostra KPIs em tempo real. Tudo é configurável sem código.
  - ⏱️ 5 minutos de leitura | 👤 Mautic Community

## Prática Básica: Instalar, Acessar e Configurar Seu Mautic (`⏱️ 3 horas`)
**🎯 Meta da Etapa:** Ter uma instância de Mautic rodando em VPS, acessível via HTTPS, com o primeiro usuário criado e o dashboard pronto para usar.

- [ ] **[Guia Passo-a-Passo: Instalação de Mautic em Ubuntu 22.04](file:///output/03-manuais-e-trilhas/activecampaign/mautic/manuais/manual-mautic-vps-e-uso.html)** (`Manual Técnico (Documento)` - `[T05]`)
  - 💡 **O que você aprende:** SSH → Atualizar Sistema → Instalar Apache, PHP, MariaDB → Baixar Mautic → Configurar Apache → SSL com Let's Encrypt → Acessar Web Installer. Cada passo testado.
  - ⏱️ 45 minutos de execução | 👤 Arsenal Open Source

- [ ] **[Primeira Configuração: Criar Usuário Admin e Conectar Email](https://www.youtube.com/results?search_query=mautic+usuario+admin+email)** (`Video Tutorial` - `[T06]`)
  - 💡 **O que você aprende:** Após instalar, o Web Installer pede: Email do Admin, Senha, Nome da Empresa, Configurações SMTP (para enviar emails). Tudo feito via interface web, sem linha de comando.
  - ⏱️ 20 minutos | 👤 Comunidade Mautic Brasil

- [ ] **[Verificar Saúde da Instalação - Testes de Conectividade](https://docs.mautic.org/en/5.1/setup/system_requirements/)** (`Checklist Interativo` - `[T07]`)
  - 💡 **O que você aprende:** Testar: PHP 8.2+, MySQL/MariaDB conectando, permissões de arquivo, SSL válido, Cron jobs funcionando. Um teste falhando = VPS não está pronta.
  - ⏱️ 10 minutos | 👤 Arsenal Open Source

- [ ] **[Configuração de Cron Jobs (Automação de Tarefas)](https://docs.mautic.org/en/5.1/setup/cron_jobs/)** (`Tutorial Técnico` - `[T08]`)
  - 💡 **O que você aprende:** Cron = agendador de Linux. Mautic precisa de cron jobs a cada 5 minutos para enviar emails, processar rastreamento e atualizar leads. Sem cron, Mautic fica 'dormindo'.
  - ⏱️ 15 minutos | 👤 Arsenal Open Source

## Captura de Leads: Formulários, Pixels de Rastreamento e Segmentação (`⏱️ 2 horas`)
**🎯 Meta da Etapa:** Instalar o pixel de rastreamento no seu site, criar seu primeiro formulário de captura, e começar a ver leads chegando automaticamente em tempo real.

- [ ] **[Instalando o Pixel de Rastreamento Mautic no Seu Site](https://docs.mautic.org/en/5.1/plugins/integrations/)** (`Guia Passo-a-Passo` - `[T09]`)
  - 💡 **O que você aprende:** Copiar código HTML pequeno do Mautic (Tracking Pixel). Colar em TODAS as páginas do seu site (idealmente no footer). Resultado: cada visitante é rastreado automaticamente sem pedir consentimento (sempre verifique LGPD).
  - ⏱️ 10 minutos | 👤 Arsenal Open Source

- [ ] **[Criar Formulário de Captura - Email + Nome](https://www.youtube.com/results?search_query=mautic+forms+tutorial)** (`Video Tutorial (Hands-On)` - `[T10]`)
  - 💡 **O que você aprende:** Menu Forms → Novo Formulário. Campos: Email (obrigatório), Nome. Ação pós-envio: Adicionar a Segmento 'Newsletter'. Publicar. Copiar código HTML. Colar no site. Pronto!
  - ⏱️ 15 minutos | 👤 Comunidade Mautic

- [ ] **[Entender Leads - O Banco de Dados Dinâmico](https://docs.mautic.org/en/5.1/leads/)** (`Documentação + Prática` - `[T11]`)
  - 💡 **O que você aprende:** Um Lead = um contato no banco de dados. Mautic rastreia: Nome, Email, Telefone, Endereço, Histórico de visitação, Emails recebidos, Abertura/Cliques, Última atividade. Tudo armazenado automaticamente.
  - ⏱️ 20 minutos | 👤 Arsenal Open Source

- [ ] **[Segmentação de Leads - Criar Grupos Automáticos](https://docs.mautic.org/en/5.1/segments/)** (`Tutorial Interativo` - `[T12]`)
  - 💡 **O que você aprende:** Segmento = grupo automático. Ex: 'Visitaram Página de Preços' = todos os leads que visitaram /pricing. Uso: enviar email de desconto apenas para este grupo. Mautic atualiza automaticamente.
  - ⏱️ 15 minutos | 👤 Comunidade Mautic Brasil

## Automação Avançada: Campanhas, Sequências de Email e Gatilhos (`⏱️ 2 horas`)
**🎯 Meta da Etapa:** Criar sua primeira campanha de email automática que envia uma sequência de 3 emails baseada no comportamento do visitante (autoresponder inteligente).

- [ ] **[O que é Campaign (Campanha) no Mautic - Conceitos](https://docs.mautic.org/en/5.1/campaigns/)** (`Artigo Didático` - `[T13]`)
  - 💡 **O que você aprende:** Campaign = fluxo de automação visual. Você arrasta blocos (ações, decisões, delays). Exemplo: Lead preenche formulário → Aguarda 5 min → Recebe Email 1 → Aguarda 2 dias → Verifica se abriu → Se abriu: Email 2. Se não abriu: Email de 'última chance'.
  - ⏱️ 8 minutos de leitura | 👤 Arsenal Open Source

- [ ] **[Tutorial Hands-On: Criar Sequência de 3 Emails (Autoresponder)](https://www.youtube.com/results?search_query=mautic+campaign+autoresponder)** (`Video Tutorial` - `[T14]`)
  - 💡 **O que você aprende:** Criar Campaign > Arrastar 'Send Email' > Criar Email 1 > Agendar delay 5 min > Email 2 > Delay 2 dias > Email 3. Adicionar segmento (quem entra). Publicar. Testar preenchendo próprio formulário.
  - ⏱️ 25 minutos | 👤 Comunidade Mautic

- [ ] **[Lead Scoring - Pontuar Leads por Atividade](https://docs.mautic.org/en/5.1/leads/lead_scoring/)** (`Guia Técnico` - `[T15]`)
  - 💡 **O que você aprende:** Visita página = +2 pts. Abre email = +5 pts. Clica em link = +10 pts. Preenche formulário = +20 pts. Lead com 50+ pontos = QUENTE = ligar agora. Mautic calcula automaticamente.
  - ⏱️ 15 minutos | 👤 Arsenal Open Source

- [ ] **[Decisões e Lógica Condicional em Campanhas](https://docs.mautic.org/en/5.1/campaigns/conditional_logic/)** (`Tutorial Avançado` - `[T16]`)
  - 💡 **O que você aprende:** Bloco 'Decision': Se lead tem score >= 50, ir para 'Email de Vendas'. Se score < 50, ir para 'Email de Educação'. Lógica if/then sem código.
  - ⏱️ 20 minutos | 👤 Comunidade Mautic

## Análise e Otimização: Relatórios, Métricas e Ajustes Contínuos (`⏱️ 1 hora`)
**🎯 Meta da Etapa:** Interpretar relatórios de Mautic (taxa de abertura, cliques, conversão), identificar o que funciona, e fazer ajustes para melhorar resultados mês a mês.

- [ ] **[Dashboard Executivo do Mautic - Interpretando as Métricas](https://docs.mautic.org/en/5.1/reports/)** (`Guia Visual` - `[T17]`)
  - 💡 **O que você aprende:** Dashboard mostra: Visitantes hoje, Leads novos, Emails enviados, Taxa de abertura (%), Taxa de cliques (%), Campanhas ativas. Tudo em tempo real. Compare semana a semana.
  - ⏱️ 12 minutos | 👤 Arsenal Open Source

- [ ] **[Relatórios Detalhados - Email Performance, Lead Source](https://docs.mautic.org/en/5.1/reports/)** (`Tutorial Prático` - `[T18]`)
  - 💡 **O que você aprende:** Relatório de Email: qual email teve maior taxa de abertura? Qual link foi mais clicado? De qual campanha vieram os leads mais quentes? Relatório de Lead Source: Google, Facebook, Email, Formulário?
  - ⏱️ 15 minutos | 👤 Comunidade Mautic Brasil

- [ ] **[A/B Testing - Testar 2 Versões de Email](https://docs.mautic.org/en/5.1/campaigns/)** (`Guia Técnico` - `[T19]`)
  - 💡 **O que você aprende:** Enviar Email A para 50% dos leads, Email B para 50%. Comparar taxa de abertura. A venceu? Use A para todos daqui em diante. Iteração contínua melhora resultados.
  - ⏱️ 10 minutos | 👤 Arsenal Open Source

- [ ] **[Checklist Mensal - 10 Ajustes para Maximizar ROI](https://docs.mautic.org/en/5.1/dashboard/)** (`Checklist + Dicas` - `[T20]`)
  - 💡 **O que você aprende:** 1. Aumentar formulários no site? 2. Melhorar copy do email? 3. Segmentar melhor? 4. Testar novo tipo de automação? 5. Otimizar landing pages para mobile? 6. Aumentar frequência de emails? 7. Remover leads inativos? 8. Integrar com CRM? 9. Melhorar pontuação de leads? 10. Aumentar bot para 2 vCPU se lento?
  - ⏱️ 5 minutos de leitura | 👤 Arsenal Open Source
