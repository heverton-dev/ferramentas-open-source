# Relatório de Gaps · Arquitetura Agêntica (4 Camadas: TELA, HARNESS, LLM, TOOLS)

> **Data:** 2026-08-28
> **Escopo:** Auditoria estrutural do projeto completo contra o `PLAYBOOK-MESTRE-ENGENHARIA-AGENTICA-AIDD.md`, além dos 4 gates mecânicos existentes (`scripts/auditar_camada_*.py`)
> **Projeto:** Arsenal Open Source · Fábrica Universal
> **Método:** Execução dos gates mecânicos (`auditar_todas_camadas.py`) + inspeção direta de código, symlinks, inodes e configuração MCP para validar se as aprovações "100%" refletem funcionalidade real

---

## 1. Resultado dos Gates Mecânicos (Baseline)

| Camada | Script | Gate | Observação |
|---|---|---|---|
| 1. TELA | `auditar_camada_tela.py` | **REPROVADO** | Falha literal, mas sintoma de gate frágil (ver GAP-01) |
| 2. HARNESS | `auditar_camada_harness.py` | APROVADO 100% | Confirmado por inspeção direta (hardlinks reais) |
| 3. LLM | `auditar_camada_llm.py` | APROVADO 100% | Aprovação de fachada — ver GAP-03 |
| 4. TOOLS | `auditar_camada_tools.py` | APROVADO 100% | Aprovação de fachada — ver GAP-04, GAP-05 |

Achado transversal: os 4 auditores validam **presença** de arquivo/string/chave, nunca **funcionalidade** real (não tentam invocar o processo, não checam uso efetivo em outros scripts). Isso permite que 3 de 4 camadas mostrem 100% enquanto escondem componentes mortos ou quebrados.

---

## 2. Inventário de Gaps

### GAP-01 · Camada 1 (TELA) — Skills obrigatórias fora da fonte única multi-IDE

- **Severidade:** P0
- **Evidência:** `.agents/skills/` contém apenas `fluxo1-listas-horizontais`, `fluxo2-dossies-verticais`, `fluxo3-manuais-e-trilhas`, `fluxo4-ecossistemas`, `fluxo5-auditoria-vps`, `fluxo-total-aidd`. Em `.claude/skills/`, esses 6 são symlinks corretos (`@` → `.agents/skills/...`), mas 10 diretórios são **reais** (não symlink) e não têm fonte em `.agents/skills/`: `caveman`, `headroom`, `lean-ctx`, `rtk-memory`, `pre-flight-check`, `blueprint-vertical`, `fabrica-listas`, `gerar-dossie-diamante`, `implementacao`, `auditoria-seguranca`.
- **Impacto:** As 5 skills obrigatórias de economia de tokens (exigidas pelo próprio `auditar_camada_tela.py`) e mais 5 skills operacionais existem **somente para Claude Code**. Cursor, Windsurf, Cline e Copilot — todos citados como harnesses-alvo no cabeçalho do playbook — não têm acesso a elas. Contradiz diretamente a Seção 5 do `CLAUDE.md`: *"Fonte Única: `.agents/` espelhado para `.claude/` e `agentic/`"*.
- **Ação recomendada:** mover os 10 diretórios reais para `.agents/skills/` e recriar `.claude/skills/<nome>` como symlink, replicando o padrão já usado nos 6 fluxos.

### GAP-02 · Camada 1 (TELA) — Gate de vocabulário controlado é literal/frágil

- **Severidade:** P2
- **Evidência:** `auditar_camada_tela.py` busca as strings exatas `"Vocabulário Controlado"` ou `"Termos Proibidos"` em `.claude/CLAUDE.md`. A intenção já existe distribuída em R2 (Silenciamento), R19 (Comunicação Direta) e R20 (Proibição de Emojis), mas sem essa frase literal — resultando em falso-negativo parcial.
- **Impacto:** Gate reprova mesmo quando a governança de vocabulário já está coberta em espírito; mascara o problema real (auditores testam string, não semântica).
- **Ação recomendada (baixo custo):** adicionar a frase "Vocabulário Controlado e Termos Proibidos" explicitamente em R2 ou R19 do `.claude/CLAUDE.md` (hardlink propaga para os demais). Ação estrutural: evoluir os 4 auditores de presença-de-string para verificação funcional (ver GAP-06).

### GAP-03 · Camada 3 (LLM) — Roteador semântico é código morto

- **Severidade:** P1
- **Evidência:** `grep -rl "roteador_llm" scripts/*.py` retorna apenas `auditar_camada_llm.py` (o próprio auditor). Nenhum `run_fluxo1.py` a `run_fluxo5.py`, nem qualquer `gerar_*.py`, importa ou chama `roteador_llm.py`.
- **Impacto:** O gate da Camada 3 valida que o dict `TIERS_LLM` tem as 3 chaves (`tier_1_rapido`, `tier_2_codigo`, `tier_3_raciocinio`), mas nenhum fluxo real decide dinamicamente qual tier/modelo usar. "Roteamento semântico" é uma alegação documental sem efeito prático.
- **Ação recomendada:** ou (a) integrar `roteador_llm` de fato nos runners de fluxo para decidir tier por tipo de tarefa, ou (b) remover a alegação de roteamento semântico do playbook e do CLAUDE.md até existir integração real.

### GAP-04 · Camada 4 (TOOLS) — Servidores MCP declarados são fictícios

- **Severidade:** P0
- **Evidência:** `.mcp.json` e `.cursor/mcp.json` registram `db_state_esteira` → `python scripts/estado_esteira.py` e `file_validator` → `python scripts/auditar_higiene_repo.py` como *servidores MCP*. Ambos os scripts terminam em `if __name__ == "__main__":` executando lógica CLI síncrona, sem loop de servidor stdio/JSON-RPC. O pacote `mcp` (SDK oficial) não está instalado no ambiente Python (`import mcp` falha).
- **Impacto:** Qualquer harness que tente conectar a esses "servidores" via protocolo MCP real vai falhar no handshake ou travar aguardando resposta. A seção 3 do `CLAUDE.md` ("Servidores MCP") descreve uma capacidade que não existe tecnicamente.
- **Ação recomendada:** ou (a) implementar os dois servidores com o SDK `mcp` real (stdio server + tools registradas com schema de entrada/saída), ou (b) remover `.mcp.json`/`.cursor/mcp.json` e citar esses scripts apenas como hooks/CLI determinísticos no CLAUDE.md, sem a alegação de "MCP".

### GAP-05 · Camada 4 (TOOLS) — Proliferação de scripts descartáveis e cobertura de teste rala

- **Severidade:** P1
- **Evidência:**
  - 29 arquivos `.pyc` órfãos em `scripts/__pycache__/` sem `.py` correspondente hoje: `gerar_30_listas`, `gerar_30_listas_com_como_usar`, `migrar_todas_as_listas_modelo_dossie`, `padronizar_todas_as_listas`, `fork-para-organizacao`, `transferir-forks-para-org`, `descobrir-e-forkear`, `completar-forks`, `pdf_typst`, `converter_md_pdf`, `test_converter`, `validate`, `build_generator_module`, `renderizador_mermaid_svg`, `sincronizar_e_limpar_legado`, `reorganizar-organizacao`, `gerar-index-organizacao`, `gerar-submodules`, `atualizar_links_index`, `auditar_how_to_use`, `injetar_como_usar`, `enriquecer_dossie_lista_01`, `enriquecer_e_padronizar_how_to_use`, `aplicar_design_premium_lista_01`, `aplicar_layout_vertical_lista_01`, `gerar_lista_cx`, `gerar_manuais_postfix_dovecot`, `recriar_postfix_jsons`, `migrar_nomenclaturas`, `refinar_titulos_e_justificacao_todas_as_listas`.
  - `scripts/` tem 96 arquivos `.py` de produção contra 6 arquivos `test_*.py` em `tests/`.
  - Não há suíte de teste dedicada visível para Fluxo 4 (`test_fluxo4_ecossistemas.py`) nem Fluxo 5 (`test_fluxo5_auditoria_vps.py`) — os dois fluxos mais recentes e mais complexos do projeto.
- **Impacto:** Sintoma direto de tensão com a R12 (Registro Declarativo): em vez de generators parametrizáveis e reutilizáveis, o padrão observado é criar um script novo por lote/correção pontual e abandoná-lo. Reduz confiabilidade de regressão nos fluxos mais novos.
- **Ação recomendada:** criar `tests/test_fluxo4_ecossistemas.py` e `tests/test_fluxo5_auditoria_vps.py`; ao criar novo script de lote, avaliar primeiro se um generator existente pode ser parametrizado em vez de duplicado.

### GAP-06 · Camada 4 (TOOLS) — Diretórios órfãos na raiz colidem com estrutura real

- **Severidade:** P2
- **Evidência:** `gates/`, `core/`, `db/`, `validators/` e `schemas/` (nível raiz) estão completamente vazios (sem `.gitkeep`, provavelmente não versionados). Colidem conceitualmente com estruturas reais já em uso: `scripts/schemas/` (schemas reais) e `estado_esteira.db` (banco real, na raiz). `templates/` tem apenas `.gitkeep`, sem uso aparente.
- **Impacto:** Gera ambiguidade sobre "fonte da verdade" para qualquer agente de IA que explore o repositório em busca de schemas, gates ou templates — risco de um agente futuro escrever no lugar errado.
- **Ação recomendada:** remover os diretórios vazios órfãos, ou documentar explicitamente propósito futuro se são scaffolding intencional.

### GAP-07 · Meta-gap — Auditores de camada testam presença, não função

- **Severidade:** P1 (estrutural, origem dos GAP-02/03/04)
- **Evidência:** Nenhum dos 4 scripts `auditar_camada_*.py` tenta invocar processo, medir uso cruzado real ou validar handshake. Todos operam por `os.path.isfile`, `in content` ou inspeção de dict/JSON estático.
- **Impacto:** Permite "aprovação de fachada" — 3 das 4 camadas relataram 100% enquanto escondiam router morto (GAP-03) e MCP fictício (GAP-04).
- **Ação recomendada:** evoluir os auditores: (a) `auditar_camada_llm.py` deve fazer `grep` de `import roteador_llm` nos `run_fluxo*.py` reais, não só checar o dict de tiers; (b) `auditar_camada_tools.py` deve tentar de fato spawnar os processos declarados em `.mcp.json` e verificar handshake MCP mínimo, não só a existência do arquivo.

---

## 3. Quadro-Resumo de Prioridade

| Prioridade | Gaps | Camadas afetadas |
|---|---|---|
| P0 | GAP-01, GAP-04 | TELA, TOOLS |
| P1 | GAP-03, GAP-05, GAP-07 | LLM, TOOLS |
| P2 | GAP-02, GAP-06 | TELA, TOOLS |

---

## 4. Achados Positivos (Confirmados, não são gap)

- `CLAUDE.md` raiz e `.claude/CLAUDE.md` são hardlink real de mesmo inode (`nlink=8`), confirmando a promessa de "Hardlink canônico" do cabeçalho do playbook.
- `agentic/agents` e `agentic/commands` são symlinks reais para `.claude/agents/` e `.claude/commands/`.
- Os 6 skills de fluxo (`fluxo1` a `fluxo5` + `fluxo-total-aidd`) seguem corretamente o padrão fonte única (`.agents/`) → symlink (`.claude/`).
- Hook `.git/hooks/pre-commit` instalado e com os 4 gates obrigatórios (Segredos R15, Testes R16, Sintaxe, Higiene R18) presentes na fonte versionada `scripts/hooks/pre-commit`.
