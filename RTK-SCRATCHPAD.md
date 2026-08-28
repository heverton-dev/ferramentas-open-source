# 🧠 RTK-SCRATCHPAD · Memória Persistente de Longo Prazo

> **Finalidade:** Arquivo externo para registrar aprendizados, decisões técnicas e resoluções de bugs ocorridos durante as sessões.  
> **Regra de Injeção de Contexto:** A Camada TELA lê apenas os **últimos 5 aprendizados** relevantes sob demanda, preservando o cache fixo do prompt mestre (`AGENTS.md` / `CLAUDE.md`).

---

## 📌 Aprendizados Registrados

### [2026-08-28] Regra R21 Permanente: Didática Universal & Foco no Usuário Não-Técnico
* **Decisão & Arquitetura:** Instituída a Regra R21 em toda a governança mestre. Todos os materiais gerados em todos os fluxos (1, 2, 3 e 4) devem ser hiper-detalhados e 100% compreensíveis para públicos não-técnicos (advogados, médicos, analistas de marketing, consultores e tomadores de decisão). Exige uso obrigatório de analogias do mundo real para desmistificar conceitos complexos (VPS, Docker, Traefik, SSL, Termius, Uptime Kuma, SSO), glossário descomplicado e priorização de Prompts Mestres para orquestração por Agentes de IA.

### [2026-08-28] Playbook do Engenheiro Agêntico, Termius & Observabilidade Uptime Kuma (Camada 06)
* **Decisão & Arquitetura:** O Fluxo 4 agora inclui formalmente a camada `06-playbook-engenharia-agentica/` com 4 Prompts Mestres executáveis por agentes de IA e configuração de Servidores MCP (`server-ssh`, `server-docker`), permitindo que a IA suba 100% da infraestrutura em produção de forma autônoma.
* **Padrão de Observabilidade & Acesso:** Toda suíte possui obrigatoriamente o fascículo `07-guia-operacao-vps-termius-e-monitoramento-uptime-kuma.html` com Termius (chaves Ed25519, túneis SSH seguros para portas internas e SFTP) e contêiner Uptime Kuma integrado ao Compose para monitoramento 24/7 com alertas de queda e expiração de certificados TLS via Webhook.

### [2026-08-28] Incorporação dos Manuais e Trilhas Individuais no Fluxo 4 (Camada 05)
* **Decisão & Arquitetura:** O Fluxo 4 foi elevado para uma entrega ponta a ponta chave na mão (*Turnkey*). Além dos 12 capítulos do Livro Mestre e dos fascículos executivos/infraestrutura, a pasta `05-manuais-e-trilhas-individuais/<ferramenta>/` agora compila automaticamente o **Manual de Engenharia de VPS** (com protocolo de Desinstalação Cirúrgica de 4 passos) e a **Trilha Didática de Aprendizado em 5 Aulas** para cada uma das ferramentas que compõem o macro-ecossistema, com links bidirecionais diretos a partir do Livro Mestre.

### [2026-08-28] Regra R20 · Visual Corporativo Estrito & Proibição Absoluta de Emojis
* **Decisão & Governança:** Fica estritamente proibido o uso de emojis ou pictogramas em todos os fluxos (Fluxo 1, Fluxo 2, Fluxo 3, Fluxo 4 e Pipeline Total) e em todos os formatos de materiais gerados (HTML Diamante R5, Markdown, PDF Typst, relatórios executivos e fascículos de engenharia).
* **Racional Executivo:** Emojis empobrecem o posicionamento visual corporativo/técnico dos materiais perante tomadores de decisão (C-Level, Diretores e Engenheiros). A elegância visual é garantida por tipografia sóbria (`Liberation Serif` / `Liberation Sans`), hierarquia rígida de espaçamentos, badges formais de texto e tabelas de alta densidade técnica.

### [2026-08-27] Soberania de Pasta Única `output/` & Deploy Direto (Anti-Forks)
* **Decisão:** A pasta duplicada `docs/` foi eliminada definitivamente do repositório. Todos os compêndios dos 3 fluxos vivem na estrutura soberana tripartite dentro de `output/` (`01-listas-horizontais/`, `02-dossies-verticais/`, `03-manuais-e-trilhas/`).
* **Blindagem de Conta GitHub:** Banido expressamente qualquer script de auto-forking em lote via API para prevenir sanções de conta. O deploy online é realizado via GitHub Actions direta (`.github/workflows/deploy-pages.yml`) a partir de `output/`.

### [2026-08-27] As 4 Skills Universais em `.agents/` & CLI Runners Determinísticos
* **Decisão:** Criadas as 4 skills especialistas na raiz universal `.agents/skills/` com junctions para `.claude/skills/` e `agentic/skills/`:
  1. `fluxo1-listas-horizontais` (`/fluxo1` e `scripts/run_fluxo1.py`)
  2. `fluxo2-dossies-verticais` (`/fluxo2` e `scripts/run_fluxo2.py`)
  3. `fluxo3-manuais-e-trilhas` (`/fluxo3` e `scripts/run_fluxo3.py`)
  4. `fluxo-total-aidd` (`/fluxo-total` e `scripts/run_fluxo_total.py`)
* **Multi-IDE:** Os comandos slash residem em `.agents/commands/`, habilitando interface via chat e via terminal para qualquer IDE.

### [2026-08-27] Desinstalação Cirúrgica & Isolamento da VPS (Zero Efeito Colateral)
* **Decisão:** Todo manual operacional do Fluxo 3 agora contém obrigatoriamente a Seção 5 detalhando 4 passos de remoção isolada (parada de serviço, remoção de contêineres/volumes dedicados, revogação de portas UFW e remoção de binários) com checklist pós-desinstalação, garantindo que nenhum outro projeto na VPS seja afetado.

### [2026-08-27] Microtipografia Estrita Anti-Sobreposição em PDFs
* **Aprendizado Typst:** Imagens Mermaid esticadas no PDF geram retângulos vazios e quebras arbitrárias; o Mermaid deve renderizar em SVG interativo nativo no HTML e texto institucional compacto no PDF. Para tabelas, a regra rígida de ouro (`size: 6.8pt`, `leading: 0.4em`, `inset: (x: 4pt, y: 3.5pt)`) impede 100% das sobreposições em folhas A4.

### [2026-08-25] Gate Mecânico R18 & Higiene Contínua
* **Regra:** Nenhuma alteração é commitada se existirem arquivos temporários (`temp_*`, `fix_*`, `.bak`, `.tmp`) ou scripts de migração descartáveis. Auditoria mecânica mandatória via `scripts/auditar_higiene_repo.py`.
