# Relatório de Verificação · Correções Aplicadas vs. Relatórios de Gaps

> **Data:** 2026-08-28
> **Escopo:** Cruzamento das correções aplicadas no commit `adea7be` (auditoria spec-vs-implementação dos Fluxos 1-5) contra os 3 relatórios de gaps existentes em `gaps/`
> **Projeto:** Arsenal Open Source · Fábrica Universal
> **Método:** Leitura integral dos 3 relatórios + verificação do estado atual de cada item citado (arquivo por arquivo, sem reimplementação)

---

## 1. Relatórios Analisados

| Arquivo | Autor | Escopo |
|---|---|---|
| `27-08-2026+MIMOCODE+mimo-v2.5-pro+auditoria-agentica.md` | MIMOCODE (mimo-v2.5-pro) | 4 camadas agênticas (TELA, HARNESS, LLM, TOOLS) vs Playbook Mestre |
| `28-08-2026+CLAUDE-CODE+haiku-4.5+gaps-4-camadas.md` | Claude Code (haiku-4.5) | Gates mecânicos das 4 camadas + inspeção direta de código/symlinks/MCP |
| `28-08-2026+MIMOCODE+mimo-v2.5-pro+gaps-especificacoes-fluxos.md` | MIMOCODE (mimo-v2.5-pro) | Especificações dos 5 Macro-Fluxos (Skills, Commands, Runners) |

---

## 2. Cruzamento com `gaps-especificacoes-fluxos.md` (Escopo Mais Próximo)

| Gap | Pedido do Relatório | Estado Atual Verificado | Responsável |
|---|---|---|---|
| GAP-01 (frontmatter fluxo4) | Adicionar bloco YAML em `SKILL.md` | **OK** — frontmatter já presente | Não foi esta sessão |
| GAP-02 (encoding fluxo5 SKILL.md) | Reescrever UTF-8, eliminar mojibake | **OK** — já corrigido antes desta sessão tocar o arquivo | Não foi esta sessão. Esta sessão reescreveu apenas a seção "Artefatos Gerados" (conteúdo estrutural R5-VPS, não encoding) |
| GAP-03 (fluxo-total-aidd desatualizada) | Expandir ou renomear para refletir 5 fluxos | **Staged, não commitado** no momento da verificação | Não foi esta sessão |
| GAP-04 (`fluxo5.md` ausente) | Criar comando seguindo padrão dos demais | **OK** — arquivo criado e commitado nesta sessão (`adea7be`) | Conteúdo já existia ao iniciar a verificação; esta sessão validou e incluiu no commit |
| GAP-05 (`fluxo-total.md` desatualizado) | Atualizar escopo (3→5 fluxos) | **OK** — já corrigido (opção B: nota sobre Fluxos 4/5 independentes) | Não foi esta sessão |
| GAP-06 (mojibake argparse `run_fluxo5.py`) | Corrigir strings do argparse | **OK** — já corrigido | Não foi esta sessão |
| GAP-07 (`run_fluxo_total.py` só orquestra 3 de 5 fluxos) | Expandir imports/lógica para os 5 fluxos | **ABERTO** — script ainda importa apenas `run_fluxo1`, `run_fluxo2`, `run_fluxo3` (linhas 23-25) | Ninguém corrigiu ainda |

**Conclusão desta seção:** zero sobreposição de implementação. Os itens tocados nesta sessão (fluxo5 SKILL.md estrutural, TOOL_PROFILES/ECOSYSTEM_PROFILES, geradores de stack) são complementares aos itens já resolvidos por processo(s) anterior(es) (frontmatter, encoding, comando, escopo textual). GAP-07 permanece aberto e fora do escopo desta sessão.

---

## 3. Cruzamento com `gaps-4-camadas.md` e `auditoria-agentica.md`

Ambos cobrem arquitetura agêntica de 4 camadas (TELA, HARNESS, LLM, TOOLS): `.mcp.json` fictício, `roteador_llm` como código morto, diretórios órfãos na raiz (`schemas/`, `gates/`, `core/`, `validators/`, `templates/`, `db/`), `.cursorrules` divergente, 29 arquivos `.pyc` órfãos, ausência de `test_fluxo4_ecossistemas.py`/`test_fluxo5_auditoria_vps.py`, skills reais fora da fonte única `.agents/skills/`.

**Nenhum destes itens se sobrepõe** às correções desta sessão. São achados estruturais/de organização de repositório, não bugs de runtime nos Fluxos 1-5.

---

## 4. Achados Exclusivos desta Sessão (Confirmado: Ausentes nos 3 Relatórios)

Busca por termo em todos os relatórios de `gaps/` não retornou nenhuma menção a:

- Bug de numeração de capítulos duplicada/incompleta (MD, HTML e Typst) em `compilar_ecossistema_tripartite.py` — fórmula `p_idx + 2` colidindo com "Capítulo 3"
- `scripts/auditar_tipo_vertical.py` com glob em caminhos legados inertes (`output/listas-open-source/`, `docs/listas/`) — auditava 0 arquivos e aprovava vacuamente; bug adicional `has_sec5` (variável nunca definida)
- Gate G0/G1 do Fluxo 3 falhando em silêncio quando `sumario-fontes-<slug>.json` não existe (13-14 manuais nunca tiveram URLs verificadas)
- 14 ferramentas e 2 ecossistemas reais sem entrada em `TOOL_PROFILES`/`ECOSYSTEM_PROFILES` — caindo no fallback genérico (1.5 vCPU / 1.5 GB, porta 80, imagem `{slug}:latest`)
- Ausência de publicação de portas raw (`mode: host`) no gerador de stack Swarm para servidores de e-mail com protocolos não-HTTP (SMTP/IMAP/POP3)
- URLs placeholder idênticas (vídeo genérico do YouTube) reutilizadas nas 5 fontes "padrão-ouro" que possuem `sumario-fontes-<slug>.json`, aprovadas pelo Gate G1 por retornarem HTTP 200 apesar de o conteúdo não corresponder ao título alegado
- Mensagens de log com caminho incorreto em `run_fluxo1.py` (faltava subpasta `materiais/`, relatório tripartite não mencionado)

---

## 5. Veredito Final

As correções aplicadas nesta sessão **não conflitam** com nenhum dos 3 relatórios de gaps existentes. Há sobreposição parcial de escopo (Fluxo 5: comando ausente, estrutura de artefatos), mas sem duplicação de implementação — os itens já resolvidos por processo(s) anterior(es) permaneceram intocados, e os itens ainda abertos (GAP-07) foram identificados e reportados, não corrigidos (fora do escopo solicitado).

| Fonte de Achado | Camada de Atuação | Sobreposição com Esta Sessão |
|---|---|---|
| `gaps-especificacoes-fluxos.md` | Existência/encoding/frontmatter de specs | Parcial (GAP-04 verificado e commitado) |
| `gaps-4-camadas.md` | Arquitetura agêntica 4 camadas | Nenhuma |
| `auditoria-agentica.md` | Conformidade com Playbook Mestre | Nenhuma |
| Esta sessão | Bugs de runtime/dados nos Fluxos 1-5 | — |

### Pendências Identificadas — Status Atualizado (Corrigidas via `/implementacao`)

1. **GAP-07** (`gaps-especificacoes-fluxos.md`): **RESOLVIDO.** `run_fluxo_total.py` permanece como Pipeline Core (Fluxos 1→2→3, 3 Gates preservados — opção B já adotada em `fluxo-total.md`/`fluxo-total-aidd/SKILL.md`), mas agora oferece continuação interativa e acionável para os Fluxos 4 e 5 ao final da execução (não apenas texto informativo): importa `executar_fluxo4()` diretamente e invoca `run_fluxo5.py` via subprocesso conforme o slug informado pelo operador. Em modo `--nao-interativo`, a etapa é pulada com orientação de comando manual, preservando compatibilidade retroativa.
2. **URLs placeholder**: **RESOLVIDO.** As 5 fontes "padrão-ouro" (`faster-whisper-cli`, `open-notebooklm`, `screenpipe`, `whisper-cpp`, `whisperx`) tiveram a fonte F04 pesquisada e substituída por conteúdo real e verificável — 4 delas migraram de `categoria: youtube` (vídeo placeholder inexistente/genérico) para `categoria: documentacao_oficial` apontando para seções reais de README no GitHub, com tópicos e trechos extraídos literalmente do conteúdo oficial. `screenpipe` manteve `categoria: youtube` por possuir vídeo oficial genuíno no canal `@screen_pipe`. Todos os 5 arquivos reaprovados nos Gates G0 e G1 reais (HTTP 200 verificado), e na suite de testes (40/40).
