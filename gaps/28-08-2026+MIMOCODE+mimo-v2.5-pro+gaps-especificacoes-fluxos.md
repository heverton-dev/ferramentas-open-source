# Relatório de Gaps · Especificações dos 5 Macro-Fluxos AIDD

> **Data:** 2026-02-09
> **Escopo:** Auditoria completa dos materiais de especificação (Skills, Commands, Runners)
> **Projeto:** Arsenal Open Source · Fábrica Universal

---

## 1. Inventário Completo

### 1.1 Skills (`.agents/skills/` → espelhado em `.claude/skills/`)

| Skill | Frontmatter | Encoding | Conteúdo | Status |
|---|---|---|---|---|
| `fluxo1-listas-horizontais` | OK | OK | OK | **OK** |
| `fluxo2-dossies-verticais` | OK | OK | OK | **OK** |
| `fluxo3-manuais-e-trilhas` | OK | OK | OK | **OK** |
| `fluxo4-ecossistemas` | **AUSENTE** | OK | OK | **GAP-01** |
| `fluxo5-auditoria-vps` | OK | **CORROMPIDO** | Parcial | **GAP-02** |
| `fluxo-total-aidd` | OK | OK | **DESATUALIZADO** | **GAP-03** |

### 1.2 Commands (`.claude/commands/`)

| Command | Existe | Conteúdo | Status |
|---|---|---|---|
| `fluxo1.md` | Sim | OK | **OK** |
| `fluxo2.md` | Sim | OK | **OK** |
| `fluxo3.md` | Sim | OK | **OK** |
| `fluxo4.md` | Sim | OK | **OK** |
| `fluxo5.md` | **NAO** | N/A | **GAP-04** |
| `fluxo-total.md` | Sim | **DESATUALIZADO** | **GAP-05** |

### 1.3 Runners (`scripts/`)

| Runner | Existe | Encoding | Escopo | Status |
|---|---|---|---|---|
| `run_fluxo1.py` | Sim | OK | OK | **OK** |
| `run_fluxo2.py` | Sim | OK | OK | **OK** |
| `run_fluxo3.py` | Sim | OK | OK | **OK** |
| `run_fluxo4.py` | Sim | OK | OK | **OK** |
| `run_fluxo5.py` | Sim | **CORROMPIDO** | OK | **GAP-06** |
| `run_fluxo_total.py` | Sim | OK | **DESATUALIZADO** | **GAP-07** |

---

## 2. Detalhamento dos Gaps

### GAP-01 · Skill Fluxo 4 sem Frontmatter YAML

**Arquivo:** `.agents/skills/fluxo4-ecossistemas/SKILL.md` (e `.claude/skills/fluxo4-ecossistemas/SKILL.md`)
**Problema:** O arquivo inicia direto com `# Skill Especialista...` sem o bloco YAML frontmatter (`---` com `name` e `description`). Todas as outras skills possuem esse bloco.
**Impacto:** O sistema de discovery de skills pode não indexar corretamente o Fluxo 4.
**Correção:** Adicionar o bloco frontmatter padrão antes do título H1.

**Frontmatter esperado:**
```yaml
---
name: fluxo4-ecossistemas
description: Especialista no acionamento e orquestração do Fluxo 4 (Macro-Ecossistemas & Suítes Soberanas Integradas AIDD). Gera dossiês de ecossistemas completos com pilares funcionais, SSO, barramento e playbook agêntico.
alwaysApply: false
---
```

---

### GAP-02 · Skill Fluxo 5 com Mojibake Severo

**Arquivo:** `.agents/skills/fluxo5-auditoria-vps/SKILL.md` (e `.claude/skills/fluxo5-auditoria-vps/SKILL.md`)
**Problema:** O arquivo foi salvo com encoding incorreto. Todos os caracteres acentuados foram substituídos por `?` (mojibake). Exemplos:
- `Avaliação` → `Avalia??o`
- `Desinstalação` → `Desinstala??o`
- `Cirúrgica` → `Cir?rgica`
- `usuário` → `usu?rio`
- `múltiplos` → `m?ltiplos`
- `análise` → `an?lise`
- `capacidade máxima` → `capacidade m?xima`
- `específicos` → `espec?ficos`
- `Balanço` → `Balan?o`
- `execuções` → `execu??es`

**Impacto:** Skill ilegível e inutilizável para qualquer agente.
**Correção:** Reescrever o arquivo inteiro com encoding UTF-8 correto, restaurando todos os acentos e cedilhas.

---

### GAP-03 · Skill Fluxo Total Desatualizada (cobre apenas 3 de 5 fluxos)

**Arquivo:** `.agents/skills/fluxo-total-aidd/SKILL.md`
**Problema:** A skill descreve o pipeline como "Fluxos 1 + 2 + 3" e documenta apenas 3 Gates. O projeto evoluiu para 5 Macro-Fluxos (conforme CLAUDE.md seção 4), mas a skill não foi atualizada.
**Linhas afetadas:**
- Linha 7: `# Skill Especialista · Pipeline Total AIDD (Fluxos 1 + 2 + 3)`
- Linha 9: "interliga os 3 fluxos sequencialmente"
- Linha 19: Diagrama mostra apenas 3 fluxos
- Linhas 22-36: Protocolo cobre apenas Etapas 1-3
- Linhas 38-44: CLI runner referencia apenas `run_fluxo_total.py` (que também só cobre 3 fluxos)

**Decisão necessária:** O pipeline total deve:
- **(A)** Ser expandido para cobrir os 5 fluxos com 5 Gates, OU
- **(B)** Manter o escopo 1+2+3 e ser renomeado para "Pipeline Core AIDD", documentando que Fluxos 4 e 5 são execuções independentes.

**Correção sugerida (opção B - menos disruptiva):**
- Renomear para "Pipeline Core AIDD (Fluxos 1 → 2 → 3)"
- Adicionar nota de que Fluxos 4 e 5 são módulos independentes acionáveis separadamente
- Manter compatibilidade com o runner atual

---

### GAP-04 · Command `/fluxo5` Inexistente

**Arquivo esperado:** `.claude/commands/fluxo5.md`
**Problema:** Todos os outros fluxos (1, 2, 3, 4) possuem seus respectivos commands em `.claude/commands/`. O Fluxo 5 não tem.
**Impacto:** O usuário não pode acionar o Fluxo 5 via `/fluxo5` no Claude Code.
**Correção:** Criar o arquivo seguindo o padrão dos outros commands.

**Conteúdo sugerido:**
```markdown
---
description: Aciona o Fluxo 5 da Fábrica Universal (Auditoria, Incorporação e Desinstalação Cirúrgica em VPS Multi-Alvo)
---

Você foi acionado através do comando `/fluxo5`.

Siga este protocolo estrito:
1. Verifique se o usuário passou o alvo (ex: `/fluxo5 ecos-google-workspace` ou `/fluxo5 stalwart`).
2. Se nenhum argumento foi informado, pergunte ao usuário:
   *"Qual ecossistema ou ferramenta você deseja auditar na VPS? (Exemplo: ecos-google-workspace, stalwart, nextcloud)"*
3. Com o alvo definido, execute o runner determinístico no terminal:
   - Para ecossistema: `python scripts/run_fluxo5.py --ecossistema <slug>`
   - Para ferramenta: `python scripts/run_fluxo5.py --ferramenta <slug>`
   - Para múltiplos alvos: `python scripts/run_fluxo5.py --ecossistemas <slug1>,<slug2>`
4. Apresente os links dos artefatos gerados em `output/05-auditorias-vps/`, destacando o veredito de viabilidade, o score de headroom e os manuais de instalação/desinstalação cirúrgica.
```

---

### GAP-05 · Command `fluxo-total.md` Desatualizado

**Arquivo:** `.claude/commands/fluxo-total.md`
**Problema:** O command referencia apenas "3 Macro-Fluxos AIDD" e "3 Gates de Decisão", mas o projeto agora tem 5 fluxos.
**Impacto:** Desalinhamento com a documentação mestra (CLAUDE.md seção 4).
**Correção:** Atualizar para refletir a arquitetura de 5 fluxos ou adicionar nota de escopo.

---

### GAP-06 · Runner `run_fluxo5.py` com Mojibake no Argparse

**Arquivo:** `scripts/run_fluxo5.py`
**Problema:** O argparse do script contém mojibake nas strings de descrição e help:
- Linha 45: `description="Fluxo 5 ? Auditoria, Incorpora??o e Desinstala??o Cir?rgica em VPS (Multi-Alvo)"`
- Linha 46: `help="Slug de um ecossistema ?nico"`
- Linhas 48+: Demais help texts com mesmo problema

**Impacto:** `--help` do runner exibe texto corrompido. Funcionalidade não afetada.
**Correção:** Reescrever as strings do argparse com encoding UTF-8 correto.

---

### GAP-07 · Runner `run_fluxo_total.py` Limitado a 3 Fluxos

**Arquivo:** `scripts/run_fluxo_total.py`
**Problema:** O runner importa e executa apenas `run_fluxo1`, `run_fluxo2` e `run_fluxo3`. Os fluxos 4 e 5 não são considerados.
**Linhas afetadas:**
- Linha 3: `CLI RUNNER UNIVERSAL · PIPELINE TOTAL AIDD (FLUXO 1 + 2 + 3)`
- Linha 23-25: Imports apenas de fluxo1, fluxo2, fluxo3
- Linha 37: `print("🔹 [ETAPA 1/3]...")`

**Decisão necessária:** Alinhada com GAP-03 — se o pipeline total for expandido, o runner deve importar e orquestrar os 5 fluxos.

> **STATUS: RESOLVIDO** (ver `gaps/28-08-2026+CLAUDE-CODE+sonnet-5+verificacao-correcoes-vs-gaps.md`). Adotada a opção B: Pipeline Core permanece Fluxos 1→2→3 com os 3 Gates originais intactos, mas `run_fluxo_total.py` agora oferece continuação interativa e acionável para os Fluxos 4 e 5 ao final da execução, importando `executar_fluxo4()` e invocando `run_fluxo5.py` via subprocesso conforme o slug informado. Docstring, banners e `argparse description` atualizados para refletir "Pipeline Core (Fluxos 1 -> 2 -> 3)".

---

## 3. Resumo de Prioridades

| Prioridade | Gap | Tipo | Esforço |
|---|---|---|---|
| **P0** | GAP-02 | Skill Fluxo 5 encoding | Reescrita total do arquivo |
| **P0** | GAP-06 | Runner Fluxo 5 encoding | Correção de strings argparse |
| **P1** | GAP-04 | Command fluxo5.md | Criação de novo arquivo |
| **P1** | GAP-01 | Skill Fluxo 4 frontmatter | Adição de 4 linhas YAML |
| **P2** | GAP-03 | Skill Fluxo Total escopo | Decisão de arquitetura + reescrita |
| **P2** | GAP-05 | Command fluxo-total escopo | Atualização de texto |
| **P2** | GAP-07 | Runner fluxo_total escopo | Expansão de imports e lógica |

---

## 4. Materiais OK (Sem Ação Necessária)

- Skill `fluxo1-listas-horizontais` — completa e funcional
- Skill `fluxo2-dossies-verticais` — completa e funcional
- Skill `fluxo3-manuais-e-trilhas` — completa e funcional
- Command `fluxo1.md` — completo
- Command `fluxo2.md` — completo
- Command `fluxo3.md` — completo
- Command `fluxo4.md` — completo
- Runner `run_fluxo1.py` — funcional
- Runner `run_fluxo2.py` — funcional
- Runner `run_fluxo3.py` — funcional
- Runner `run_fluxo4.py` — funcional
