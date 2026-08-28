# Skill Especialista · Fluxo 4: Macro-Ecossistemas & Suítes Integradas AIDD

Esta skill governa a geração determinística de **Dossiês de Macro-Ecossistemas SaaS** cobrindo suítes multimodais completas (ex: *RD Station Suite, Google Workspace, Zoho One, Atlassian Suite, Microsoft 365, Adobe Creative Cloud*).

## Quando Usar
- Quando o usuário pedir para gerar, atualizar ou compilar a substituição de um **ecossistema completo** ou **suíte integrada de software**;
- Quando o comando `/fluxo4` for disparado com um slug de ecossistema (ex: `/fluxo4 rd-station-suite`);
- Quando a demanda envolver múltiplos módulos interdependentes que necessitam de camada de cola, SSO (Single Sign-On) e barramento de eventos integrados.

## Protocolo de Execução Agêntica

### 1. Pesquisa & Estruturação do Macro-Ecossistema:
Se o ecossistema for novo:
1. Identifique o **Guarda-Chuva Central** (ex: RD Station Suite) e seus **Pilares Funcionais** (ex: Marketing, CRM, Conversas/WhatsApp);
2. Selecione as 2 a 4 ferramentas líderes open source por pilar;
3. Defina a **Camada de Cola & Integração**:
   - Autenticação Unificada (Keycloak / Authentik SSO OIDC);
   - Barramento de Dados Assíncrono (n8n Workflows);
   - Reverse Proxy & Roteamento TLS (Traefik / Nginx);
4. Projete o **Deploy All-in-One** (Docker Compose unificado com rede interna compartilhada);
5. Salve os dados em `scripts/data/ecos-<slug>.json`.

### 2. Execução do Runner Oficial:
Execute o runner canônico:
```bash
python scripts/run_fluxo4.py --ecossistema <slug>
```

### 3. Entregáveis da Suíte Soberana Modular:
Os artefatos são gerados na pasta soberana única `output/04-ecossistemas/ecos-<slug>/`:
- `00-livro-mestre-compilado/` (`LIVRO-ECOSSISTEMA-COMPLETO.html`, `.md`, `.pdf` de 12 capítulos);
- `01-guias-executivos-e-estrategicos/` (TCO, Calculadora, Matriz do Quinteto e Cronograma 30 Dias);
- `02-guias-de-engenharia-e-infraestrutura/` (Manual Deploy All-in-One Compose, Hot-Swap Lego, Monitoramento, Operação VPS Termius & Uptime Kuma);
- `03-guias-de-integracao-e-operacao/` (Blueprints n8n, Migração de Dados De-SaaS e Segurança/LGPD);
- `04-arsenal-dos-pilares/` (Fichas técnicas individuais por pilar funcional);
- `05-manuais-e-trilhas-individuais/` (Manuais de VPS com Desinstalação Cirúrgica e Trilhas em 5 Aulas para cada ferramenta da suíte);
- `06-playbook-engenharia-agentica/` (`PLAYBOOK-ENGENHEIRO-AGENTICO.html`, `.md`, 4 Prompts Mestres de orquestração por IA e configurações de Servidores MCP).

### 4. Diretriz de Design & Governança (Regra R20):
- **Visual Corporativo Estrito:** Proibição absoluta do uso de emojis ou pictogramas em qualquer formato de material (HTML, Markdown, PDF Typst, relatórios ou scripts). O design deve ser puramente corporativo, técnico e elegante, baseado em tipografia sóbria, hierarquia de espaçamentos, badges formais e tabelas estruturadas.

### 5. Apresentação ao Usuário:
Apresente a matriz comparativa por pilares com os links diretos para os artefatos gerados.
