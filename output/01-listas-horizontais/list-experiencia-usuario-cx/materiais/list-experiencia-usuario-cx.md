# Experiência do Usuário & Customer Experience (CX)

> **Compêndio Temático Open Source · Camada 50 · Padrão Diamante R5**  
> Compêndio soberano de ferramentas open-source para mapear a jornada, coletar feedback, gravar sessões, atender clientes em múltiplos canais e gerenciar contas sem pagar pedágio para Zendesk, Intercom, Hotjar ou Salesforce.

---

## 1. Matriz Comparativa de Ferramentas da Camada

| Rank | Ferramenta | Categoria | Licença | Substitui | Economia Estimada |
| :---: | :--- | :--- | :---: | :--- | :--- |
| 01 | **PostHog** | Product Analytics | `MIT` | Mixpanel / Hotjar / FullStory | R$ 48.000/ano |
| 02 | **Chatwoot** | Suporte & Atendimento | `MIT` | Zendesk / Intercom / LiveChat | R$ 36.000/ano |
| 03 | **Typebot** | Onboarding & Formulários | `AGPL-3.0` | Typeform / Landbot | R$ 18.000/ano |
| 04 | **Formbricks** | Pesquisa de Satisfação & NPS | `AGPL-3.0` | Qualtrics / SurveyMonkey / Delighted | R$ 30.000/ano |
| 05 | **Novu** | Engajamento & Notificações | `Apache-2.0` | OneSignal / Courier / Twilio Sendgrid | R$ 28.000/ano |
| 06 | **Cal.com** | Agendamento de Clientes | `AGPL-3.0` | Calendly / Acuity Scheduling | R$ 15.000/ano |
| 07 | **Twenty CRM** | CRM & Gestão de Contas | `AGPL-3.0` | Salesforce / HubSpot Sales | R$ 52.000/ano |
| 08 | **Highlight.io** | Observabilidade & UX | `Apache-2.0` | LogRocket / Datadog RUM / Sentry Cloud | R$ 34.000/ano |
| 09 | **Documenso** | Contratos & Assinatura Digital | `AGPL-3.0` | DocuSign / PandaDoc / Adobe Sign | R$ 22.000/ano |
| 10 | **Plane** | Gestão de Demandas de Clientes | `AGPL-3.0` | Jira / Linear / Productboard | R$ 26.000/ano |

---

## 2. Detalhamento Técnico das Ferramentas

### #01 · PostHog — *Product Analytics & Session Replay*

- **Categoria:** Product Analytics | **Senioridade:** `Pleno`
- **Licença OSI:** `MIT`
- **SaaS Proprietário Substituído:** Mixpanel / Hotjar / FullStory
- **Economia Estimada no TCO:** R$ 48.000/ano

#### 1. O Que Faz & Como Funciona
Suíte all-in-one para análise de produto, gravação de sessão de navegação do cliente, heatmaps, funis de conversão e feature flags.

*Captura eventos de telemetria no frontend e armazena em ClickHouse de alto rendimento. Permite reproduzir visualmente exatamente o que o cliente viu e fez antes de abandonar o carrinho ou solicitar suporte.*

```bash
docker run -d -p 8000:8000 --name posthog posthog/posthog:latest
```

#### 2. Análise Econômica & Infraestrutura
- **Custo Proprietário:** Mixpanel e Hotjar combinados custam a partir de US$ 800/mês para volumes médios de tráfego corporativo.
- **Custo Open Source:** VPS 4 vCPU / 8 GB RAM (aprox. US$ 40/mês).
- **Retorno do Investimento (ROI):** ROI positivo no 1º mês de migração.
- **Requisitos de Infra:** 4 GB RAM RAM, 2 vCPU CPU (Banco: PostgreSQL + ClickHouse)
- **Veredito do Arquiteto:** Padrão-ouro absoluto para compreender a experiência real de uso do produto digital sem enviar dados de telemetria dos usuários para nuvens proprietárias.
- **Repositório Oficial:** [https://github.com/PostHog/posthog](https://github.com/PostHog/posthog)

#### 3. Como Usar no Dia a Dia
1. **Passo 1:** 
2. **Passo 2:** 
3. **Passo 3:** 

#### 4. White-Label & Aderência ao Design System Corporativo
- **Esforço de Customização:** `Headless / API First` (React / Tailwind)
- **Mecânica de Customização:** SDK headless permite renderizar dashboards e widgets customizados com o design system da sua marca.
- **Impacto em Upgrades:** Camada de API estável sob protocolo REST/GraphQL com zero risco de quebra em atualizações de versão.

---

### #02 · Chatwoot — *Central de Atendimento & Live Chat Omnicanal*

- **Categoria:** Suporte & Atendimento | **Senioridade:** `Iniciante`
- **Licença OSI:** `MIT`
- **SaaS Proprietário Substituído:** Zendesk / Intercom / LiveChat
- **Economia Estimada no TCO:** R$ 36.000/ano

#### 1. O Que Faz & Como Funciona
Centraliza conversas de clientes vindas de live chat no site, WhatsApp, Telegram, e-mail e redes sociais numa caixa de entrada unificada sem limite de atendentes.

*Arquitetura orientada a microsserviços em Ruby on Rails e Vue.js com WebSockets para comunicação em tempo real, roteando conversas para agentes humanos ou bots de IA.*

```bash
git clone https://github.com/chatwoot/chatwoot && cd chatwoot && docker compose up -d
```

#### 2. Análise Econômica & Infraestrutura
- **Custo Proprietário:** Zendesk cobra a partir de US$ 55/agente/mês. Para 10 operadores, custa US$ 6.600/ano.
- **Custo Open Source:** Instância Cloud de 2 vCPU / 4 GB RAM (US$ 24/mês).
- **Retorno do Investimento (ROI):** Payback imediato a partir do 2º atendente cadastrado.
- **Requisitos de Infra:** 2 GB RAM RAM, 2 vCPU CPU (Banco: PostgreSQL + Redis)
- **Veredito do Arquiteto:** A solução definitiva para desmantelar mensalidades abusivas por atendente no atendimento ao cliente.
- **Repositório Oficial:** [https://github.com/chatwoot/chatwoot](https://github.com/chatwoot/chatwoot)

#### 3. Como Usar no Dia a Dia
1. **Passo 1:** 
2. **Passo 2:** 
3. **Passo 3:** 

#### 4. White-Label & Aderência ao Design System Corporativo
- **Esforço de Customização:** `Esforço Mínimo` (Vue.js / Tailwind)
- **Mecânica de Customização:** Customização de logotipo, cores corporativas, mensagens de boas-vindas e domínio próprio diretamente pelo painel administrativo.
- **Impacto em Upgrades:** Variáveis de ambiente isolam as propriedades de marca; atualizações de imagem Docker preservam o branding intacto.

---

### #03 · Typebot — *Construtor Visual de Fluxos de Onboarding & Bots*

- **Categoria:** Onboarding & Formulários | **Senioridade:** `Iniciante`
- **Licença OSI:** `AGPL-3.0`
- **SaaS Proprietário Substituído:** Typeform / Landbot
- **Economia Estimada no TCO:** R$ 18.000/ano

#### 1. O Que Faz & Como Funciona
Cria formulários conversacionais interativos e fluxos guiados de onboarding que aumentam as taxas de resposta e qualificação de clientes.

*Editor visual drag-and-drop de nós que compila fluxos em JSON executados por um cliente leve no navegador, com suporte a webhooks, IA e validação de dados.*

```bash
docker run -d -p 3000:3000 --name typebot baptistearno/typebot-builder:latest
```

#### 2. Análise Econômica & Infraestrutura
- **Custo Proprietário:** Typeform custa até US$ 83/mês com travas rígidas de volume de respostas mensais.
- **Custo Open Source:** Roda com tranquilidade em VPS básica de 1 vCPU / 2 GB RAM (US$ 12/mês).
- **Retorno do Investimento (ROI):** Elimina cobrança por resposta no 1º formulário publicado.
- **Requisitos de Infra:** 1 GB RAM RAM, 1 vCPU CPU (Banco: PostgreSQL)
- **Veredito do Arquiteto:** Transforma pesquisas monótonas e cadastros complexos em experiências de bate-papo dinâmicas com conversão superior.
- **Repositório Oficial:** [https://github.com/baptisteArno/typebot.io](https://github.com/baptisteArno/typebot.io)

#### 3. Como Usar no Dia a Dia
1. **Passo 1:** 
2. **Passo 2:** 
3. **Passo 3:** 

#### 4. White-Label & Aderência ao Design System Corporativo
- **Esforço de Customização:** `Esforço Mínimo` (React / Next.js)
- **Mecânica de Customização:** Temas CSS completos com injeção de fontes personalizadas, cantos arredondados, paletas e avatares da marca.
- **Impacto em Upgrades:** Isolamento total dos temas em banco relacional, garantindo que novos releases não alterem a identidade visual.

---

### #04 · Formbricks — *Micro-Pesquisas de NPS & Feedback Contínuo In-App*

- **Categoria:** Pesquisa de Satisfação & NPS | **Senioridade:** `Pleno`
- **Licença OSI:** `AGPL-3.0`
- **SaaS Proprietário Substituído:** Qualtrics / SurveyMonkey / Delighted
- **Economia Estimada no TCO:** R$ 30.000/ano

#### 1. O Que Faz & Como Funciona
Dispara pesquisas cirúrgicas de satisfação (CSAT, NPS, CES) diretamente dentro do produto digital no momento em que o usuário executa uma ação relevante.

*SDK leve em TypeScript que escuta gatilhos de comportamento do usuário e exibe modais não-intrusivos, sincronizando respostas em tempo real com pipelines de dados.*

```bash
git clone https://github.com/formbricks/formbricks && cd formbricks && docker compose up -d
```

#### 2. Análise Econômica & Infraestrutura
- **Custo Proprietário:** Qualtrics e Delighted praticam planos anuais corporativos com valores entre US$ 3.000 e US$ 12.000/ano.
- **Custo Open Source:** VPS 2 vCPU / 4 GB RAM (US$ 24/mês).
- **Retorno do Investimento (ROI):** Retorno de investimento inferior a 30 dias.
- **Requisitos de Infra:** 2 GB RAM RAM, 1 vCPU CPU (Banco: PostgreSQL)
- **Veredito do Arquiteto:** Essencial para times de produto que precisam mensurar a percepção do usuário em tempo real sem cansar a base com e-mails chatos.
- **Repositório Oficial:** [https://github.com/formbricks/formbricks](https://github.com/formbricks/formbricks)

#### 3. Como Usar no Dia a Dia
1. **Passo 1:** 
2. **Passo 2:** 
3. **Passo 3:** 

#### 4. White-Label & Aderência ao Design System Corporativo
- **Esforço de Customização:** `Esforço Médio` (React / Tailwind / Headless)
- **Mecânica de Customização:** Controle total via CSS variables e classes Tailwind para mimetizar exatamente os componentes do design system do seu app.
- **Impacto em Upgrades:** Compatibilidade retroativa garantida via contratos estritos de SDK.

---

### #05 · Novu — *Infraestrutura de Notificações Omnicanal*

- **Categoria:** Engajamento & Notificações | **Senioridade:** `Pleno`
- **Licença OSI:** `Apache-2.0`
- **SaaS Proprietário Substituído:** OneSignal / Courier / Twilio Sendgrid
- **Economia Estimada no TCO:** R$ 28.000/ano

#### 1. O Que Faz & Como Funciona
Centraliza o disparo de notificações corporativas para clientes através de sininho in-app, push mobile, e-mail transacional, SMS e mensagens instantâneas.

*Orquestrador central de mensagens que provê um feed de notificações em tempo real no frontend e roteia envios para múltiplos provedores sem acoplamento de código.*

```bash
npx novu init
```

#### 2. Análise Econômica & Infraestrutura
- **Custo Proprietário:** Courier e OneSignal cobram taxas elevadas por milhão de envios e taxas fixas por canal conectado.
- **Custo Open Source:** Auto-hospedagem em container Docker com custo fixo de infraestrutura (US$ 30/mês).
- **Retorno do Investimento (ROI):** Economia imediata e previsibilidade orçamentária total.
- **Requisitos de Infra:** 2 GB RAM RAM, 2 vCPU CPU (Banco: MongoDB + Redis)
- **Veredito do Arquiteto:** Elimina a dor de cabeça de integrar provedores de e-mail e push separadamente, entregando uma central de notificações completa pronta para uso.
- **Repositório Oficial:** [https://github.com/novuhq/novu](https://github.com/novuhq/novu)

#### 3. Como Usar no Dia a Dia
1. **Passo 1:** 
2. **Passo 2:** 
3. **Passo 3:** 

#### 4. White-Label & Aderência ao Design System Corporativo
- **Esforço de Customização:** `Headless / API First` (React / Web Components)
- **Mecânica de Customização:** Componente Notification Center 100% estilizável via CSS-in-JS ou modo headless com lógica desacoplada da UI.
- **Impacto em Upgrades:** Componentes de UI publicados em pacotes NPM versionados independentemente do backend.

---

### #06 · Cal.com — *Infraestrutura Aberta de Agendamento & Atendimento*

- **Categoria:** Agendamento de Clientes | **Senioridade:** `Iniciante`
- **Licença OSI:** `AGPL-3.0`
- **SaaS Proprietário Substituído:** Calendly / Acuity Scheduling
- **Economia Estimada no TCO:** R$ 15.000/ano

#### 1. O Que Faz & Como Funciona
Permite que clientes e leads agendem reuniões de demonstração, consultoria ou sessões de suporte técnico diretamente na agenda dos colaboradores.

*Plataforma full-stack em Next.js sincronizada bidirecionalmente com Google Calendar, Outlook, CalDAV e servidores de videoconferência abertos como Jitsi.*

```bash
git clone https://github.com/calcom/cal.com && cd cal.com && docker compose up -d
```

#### 2. Análise Econômica & Infraestrutura
- **Custo Proprietário:** Calendly Teams custa US$ 16/usuário/mês. Para um time de 15 consultores/CS, custa cerca de R$ 15.000/ano.
- **Custo Open Source:** Instância VPS dedicada de US$ 18/mês.
- **Retorno do Investimento (ROI):** Payback total em menos de 60 dias.
- **Requisitos de Infra:** 2 GB RAM RAM, 1 vCPU CPU (Banco: PostgreSQL)
- **Veredito do Arquiteto:** Elimina a troca interminável de e-mails para marcar conversas com clientes, com privacidade e domínio corporativo.
- **Repositório Oficial:** [https://github.com/calcom/cal.com](https://github.com/calcom/cal.com)

#### 3. Como Usar no Dia a Dia
1. **Passo 1:** 
2. **Passo 2:** 
3. **Passo 3:** 

#### 4. White-Label & Aderência ao Design System Corporativo
- **Esforço de Customização:** `Esforço Mínimo` (Next.js / Tailwind UI)
- **Mecânica de Customização:** Suporte nativo a temas escuro/claro, injeção de favicon, logotipo próprio, domínio customizado e remoção de marcas terceiras.
- **Impacto em Upgrades:** Excelente separação de módulos com migrações automáticas de banco via Prisma.

---

### #07 · Twenty CRM — *CRM Open Source Moderno para Sucesso do Cliente*

- **Categoria:** CRM & Gestão de Contas | **Senioridade:** `Pleno`
- **Licença OSI:** `AGPL-3.0`
- **SaaS Proprietário Substituído:** Salesforce / HubSpot Sales
- **Economia Estimada no TCO:** R$ 52.000/ano

#### 1. O Que Faz & Como Funciona
Gerencia o ciclo de vida completo dos clientes, histórico de interações, status de renovação de contratos e oportunidades de expansão de contas.

*Construído sobre Nest.js, React e PostgreSQL com arquitetura moderna e intuitiva, permitindo criar campos personalizados, automações e pipelines de CS sem complexidade desnecessária.*

```bash
git clone https://github.com/twentyhq/twenty && cd twenty && docker compose up -d
```

#### 2. Análise Econômica & Infraestrutura
- **Custo Proprietário:** HubSpot e Salesforce cobram planos corporativos caríssimos com taxas de implantação que ultrapassam R$ 50.000 anuais.
- **Custo Open Source:** VPS 2 vCPU / 4 GB RAM (US$ 24/mês).
- **Retorno do Investimento (ROI):** Economia maciça no 1º trimestre.
- **Requisitos de Infra:** 2 GB RAM RAM, 2 vCPU CPU (Banco: PostgreSQL)
- **Veredito do Arquiteto:** A melhor alternativa contemporânea ao Salesforce para equipes que valorizam usabilidade fluida e controle total dos dados dos clientes.
- **Repositório Oficial:** [https://github.com/twentyhq/twenty](https://github.com/twentyhq/twenty)

#### 3. Como Usar no Dia a Dia
1. **Passo 1:** 
2. **Passo 2:** 
3. **Passo 3:** 

#### 4. White-Label & Aderência ao Design System Corporativo
- **Esforço de Customização:** `Esforço Médio` (React / Emotion / Storybook)
- **Mecânica de Customização:** Arquitetura baseada em tokens de design que permite personalizar paleta de cores e tipografia corporativa.
- **Impacto em Upgrades:** Testes automatizados cobrem 100% dos fluxos de dados do backend, garantindo estabilidade em updates.

---

### #08 · Highlight.io — *Monitoramento de Erros de UX & Session Replay*

- **Categoria:** Observabilidade & UX | **Senioridade:** `Sênior`
- **Licença OSI:** `Apache-2.0`
- **SaaS Proprietário Substituído:** LogRocket / Datadog RUM / Sentry Cloud
- **Economia Estimada no TCO:** R$ 34.000/ano

#### 1. O Que Faz & Como Funciona
Grava a sessão do usuário com reprodução de vídeo pixel-perfect sincronizada com logs de backend e erros de JavaScript, revelando a causa raiz de frustrações do cliente.

*Grava mutações de DOM (rrweb) e requisições de rede, indexando logs e métricas em ClickHouse com alertas automáticos quando um cliente experimenta um erro visual grave.*

```bash
curl -sSf https://highlight.io/install.sh | bash
```

#### 2. Análise Econômica & Infraestrutura
- **Custo Proprietário:** LogRocket e Datadog cobram por sessões gravadas, gerando faturas imprevisíveis de US$ 500 a US$ 2.000/mês.
- **Custo Open Source:** Cluster Docker em VPS 4 vCPU / 8 GB RAM (US$ 48/mês).
- **Retorno do Investimento (ROI):** Payback total a partir de 20.000 sessões monitoradas por mês.
- **Requisitos de Infra:** 8 GB RAM RAM, 4 vCPU CPU (Banco: ClickHouse + PostgreSQL)
- **Veredito do Arquiteto:** Ferramenta cirúrgica para times de engenharia e produto que precisam reproduzir bugs relatados por clientes sem precisar pedir prints de tela.
- **Repositório Oficial:** [https://github.com/highlight/highlight](https://github.com/highlight/highlight)

#### 3. Como Usar no Dia a Dia
1. **Passo 1:** 
2. **Passo 2:** 
3. **Passo 3:** 

#### 4. White-Label & Aderência ao Design System Corporativo
- **Esforço de Customização:** `Headless / API First` (React / Tailwind / Go)
- **Mecânica de Customização:** Embed de sessões e dashboards através de iframes seguros ou integração direta via GraphQL API.
- **Impacto em Upgrades:** Backend robusto em Go de alta eficiência com baixo custo de manutenção operacional.

---

### #09 · Documenso — *Assinatura Digital de Documentos & Contratos*

- **Categoria:** Contratos & Assinatura Digital | **Senioridade:** `Iniciante`
- **Licença OSI:** `AGPL-3.0`
- **SaaS Proprietário Substituído:** DocuSign / PandaDoc / Adobe Sign
- **Economia Estimada no TCO:** R$ 22.000/ano

#### 1. O Que Faz & Como Funciona
Permite que clientes assinem digitalmente contratos de prestação de serviços, termos de adesão e propostas comerciais com validade jurídica e privacidade.

*Plataforma web em Next.js e TypeScript com processamento criptográfico de assinaturas em PDF, geração de trilha de auditoria e selo temporal.*

```bash
git clone https://github.com/documenso/documenso && cd documenso && docker compose up -d
```

#### 2. Análise Econômica & Infraestrutura
- **Custo Proprietário:** DocuSign cobra cerca de US$ 40/usuário/mês com limites rígidos de envelopes de assinatura contratados.
- **Custo Open Source:** VPS básica de 1 vCPU / 2 GB RAM (US$ 12/mês).
- **Retorno do Investimento (ROI):** ROI imediato com envelopes ilimitados.
- **Requisitos de Infra:** 2 GB RAM RAM, 1 vCPU CPU (Banco: PostgreSQL)
- **Veredito do Arquiteto:** Elimina os custos predatórios por documento assinado e garante que os contratos sigilosos dos seus clientes fiquem armazenados na sua própria infraestrutura.
- **Repositório Oficial:** [https://github.com/documenso/documenso](https://github.com/documenso/documenso)

#### 3. Como Usar no Dia a Dia
1. **Passo 1:** 
2. **Passo 2:** 
3. **Passo 3:** 

#### 4. White-Label & Aderência ao Design System Corporativo
- **Esforço de Customização:** `Esforço Mínimo` (Next.js / Tailwind CSS)
- **Mecânica de Customização:** Personalização de logotipo, cores de destaque, e-mails transacionais e domínio próprio para a tela de assinatura.
- **Impacto em Upgrades:** Estrutura moderna em monorepo com código limpo e de fácil acompanhamento de releases upstream.

---

### #10 · Plane — *Gestão de Demandas & Roadmap Aberto de Clientes*

- **Categoria:** Gestão de Demandas de Clientes | **Senioridade:** `Pleno`
- **Licença OSI:** `AGPL-3.0`
- **SaaS Proprietário Substituído:** Jira / Linear / Productboard
- **Economia Estimada no TCO:** R$ 26.000/ano

#### 1. O Que Faz & Como Funciona
Organiza solicitações de clientes, bugs relatados e melhorias de produtos em quadros ágeis, permitindo publicar roadmaps transparentes para os clientes.

*Backend em Django/Python e frontend de altíssima fidelidade em Next.js com visual moderno inspirado no Linear, com suporte a ciclos, módulos e páginas de documentação.*

```bash
curl -fsSL https://prime.plane.so/install.sh | sh
```

#### 2. Análise Econômica & Infraestrutura
- **Custo Proprietário:** Jira e Linear cobram mensalidades por assento que se tornam proibitivas ao envolver toda a organização.
- **Custo Open Source:** VPS 2 vCPU / 4 GB RAM (US$ 24/mês).
- **Retorno do Investimento (ROI):** Payback alcançado logo nos primeiros 45 dias de uso corporativo.
- **Requisitos de Infra:** 4 GB RAM RAM, 2 vCPU CPU (Banco: PostgreSQL + Redis)
- **Veredito do Arquiteto:** A interface mais agradável e rápida do mercado para transformar feedbacks de clientes em itens de entrega da equipe de engenharia.
- **Repositório Oficial:** [https://github.com/makeplane/plane](https://github.com/makeplane/plane)

#### 3. Como Usar no Dia a Dia
1. **Passo 1:** 
2. **Passo 2:** 
3. **Passo 3:** 

#### 4. White-Label & Aderência ao Design System Corporativo
- **Esforço de Customização:** `Esforço Médio` (Next.js / Tailwind CSS)
- **Mecânica de Customização:** Customização visual de temas e modos escuro/claro com suporte a domínios personalizados para os quadros públicos.
- **Impacto em Upgrades:** Script de deploy com rotinas automáticas de backup e migrações de banco seguras.

---

## 3. Governança e Diretrizes de Adoção Corporativa

1. **Soberania Operacional:** 100% das ferramentas catalogadas operam sob licenças OSI livres de royalties para uso corporativo.
2. **Isolamento na VPS:** A implantação recomendada utiliza contêineres Docker isolados com rede interna e proxy reverso Caddy/Traefik com HTTPS automático.
3. **Desinstalação Cirúrgica:** A esteira garante que qualquer ferramenta pode ser removida da infraestrutura sem afetar outros contêineres ou bancos do servidor.