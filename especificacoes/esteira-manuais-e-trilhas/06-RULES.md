# 06 · As Leis Inegociáveis do Módulo (Rules & Constraints)

> **Módulo:** Esteira Autônoma de Ingestão de Fontes, Manuais VPS e Trilhas de Aprendizado  
> **Status:** Governança Ativa · Rigor Estrito · Nota 10.0 / 10.0

---

## 1. As 10 Leis de Ouro da Engenharia Agêntica

As regras abaixo são inegociáveis. Qualquer agente ou script que violar uma dessas leis terá sua execução terminada imediatamente pelo sistema de auditoria.

---

### Lei 1 · R-TOKEN (Economia Severa de Tokens & Determinismo Primeiro)
- Toda operação que puder ser realizada por código mecânico em disco (compilação de HTML, Markdown, PDF Typst, validação HTTP, cálculo de hashes, consultas SQLite) DEVE ser executada por scripts locais.
- A LLM é reservada exclusivamente para raciocínio analítico e redação inicial de dados estruturados em JSON.
- Proibido qualquer raciocínio prolixo em pensamento interno (estilo *Caveman* obrigatório).

### Lei 2 · R-MIDIA (Política Estrita de Zero Download Pesado)
- É terminantemente proibido o download de arquivos binários pesados de vídeo (`.mp4`, `.mkv`, `.webm`) ou áudio (`.mp3`, `.wav`) para o disco local.
- O crawler opera exclusivamente em memória, extraindo metadados, títulos, transcrições e trechos textuais.

### Lei 3 · R-BRASIL (Brasil First & Acessibilidade Linguística)
- O público-alvo prioritário é o usuário e a empresa brasileira.
- O idioma estrito de todos os artefatos é o português do Brasil (PT-BR).
- Fontes em português recebem destaque prioritário na trilha. Para conteúdos oficiais em inglês, é obrigatória a inclusão da caixa de Tradução Assistida passo a passo.

### Lei 4 · R-DIDATICA (Acessibilidade para Iniciantes & Não-Programadores)
- Nenhum manual pode ser entregue sem o **Módulo 0 de Nivelamento Conceitual**, que explica a infraestrutura com metáforas do dia a dia.
- Todo comando deve ter as seções *"O Que Acontece na Tela"* e *"Como Saber se Deu Certo"*.
- É obrigatório o **Roteiro de Primeiro Voo**, permitindo ao leigo testar o software em até 3 minutos.

### Lei 5 · R-GATES (Validação Mecânica em Cascata)
- Promessas em prosa não constituem garantia de qualidade.
- Toda regra de qualidade vive em um script independente que retorna `exit 0` (sucesso) ou `exit 1` (erro fatal).
- Gates obrigatórios: **G0** (Qualidade/Whitelist), **G1** (HTTP 200), **G2** (Citações Biunívocas) e **R18** (Higiene e Espelhos).

### Lei 6 · R-CITACOES (Zero Alucinação Referencial)
- Todo comando CLI, rota de API ou decisão técnica documentada no manual DEVE apontar para o ID correspondente da fonte (`F01`, `F02`...).
- 100% dos IDs presentes no sumário devem ser citados no manual correspondente. Fontes órfãs ou citações de IDs inexistentes disparam falha crítica no Gate G2.

### Lei 7 · R-TRIPARTITE (Entrega em 3 Formatos Simultâneos)
- Todo material (Manual, Trilha e Relatório) é entregue obrigatoriamente nos três formatos canônicos:
  1. **HTML Interativo:** Com busca client-side, Hero Stats e design responsivo;
  2. **Markdown:** Puro, limpo e versionável;
  3. **PDF Executivo:** Compilado instantaneamente via Typst com tipografia institucional.

### Lei 8 · R-BUNDLES (Arquitetura Modular Limpa)
- Cada ferramenta deve ter sua pasta própria em `output/<slug>/` com exatamente três subpastas: `manuais/`, `trilhas/` e `relatorios/`.
- Cada pasta deve conter rigorosamente 3 arquivos (totalizando 9 arquivos por ferramenta).
- Proibido misturar artefatos de ferramentas distintas em pastas planas.

### Lei 9 · R-TELEMETRIA (Transparência de Execução)
- Todo fechamento de ferramenta ou lote deve gerar um Relatório Oficial de Telemetria nomeado com a data no formato `DD-MM-YYYY-relatorio-execucao-<slug>.[html|md|pdf]`.
- O relatório deve registrar início, fim, duração, tokens consumidos, modelo de LLM, harness, tools, skills e status dos gates.

### Lei 10 · R-PERSISTENCIA (Estado em Disco SQLite - Regra R11)
- O estado da esteira não reside na memória volátil da conversa.
- Todo bundle concluído e auditado é gravado na tabela `esteira_manuais_bundles` do banco relacional `estado_esteira.db`, garantindo rastreabilidade histórica perene.
