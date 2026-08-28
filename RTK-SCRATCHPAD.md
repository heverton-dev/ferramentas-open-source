# 🧠 RTK-SCRATCHPAD · Memória Persistente de Longo Prazo

> **Finalidade:** Arquivo externo para registrar aprendizados, decisões técnicas e resoluções de bugs ocorridos durante as sessões.  
> **Regra de Injeção de Contexto:** A Camada TELA lê apenas os **últimos 5 aprendizados** relevantes sob demanda, preservando o cache fixo do prompt mestre (`AGENTS.md` / `CLAUDE.md`).

---

## 📌 Aprendizados Registrados

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
