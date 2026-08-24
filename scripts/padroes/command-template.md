---
description: <O que este comando faz, em uma frase. Aparece na lista de comandos.>
argument-hint: <alvo> [--opcao]
---

# /<seu-comando>

<Uma linha: o que entra, o que sai.>

## REQUISITOS CONTRATUAIS

| # | Requisito | Spec |
|---|---|---|
| R1 | <o que o resultado precisa cumprir> | <como verificar> |
| R2 | <...> | <...> |
| R3 | Nenhuma etapa opcional roda sem escolha explicita do operador | R17 do CLAUDE.md |
| R4 | Suite verde antes de commit | R16 do CLAUDE.md |

Requisito sem coluna "Spec" preenchida nao e requisito — e desejo. Ou vira gate
verificavel, ou sai da tabela.

## Passo 0 — Preparacao

1. Validar entrada: `<alvo>` existe? config carregada?
2. Ler estado atual em `<estado.json>` (R11) — nunca assumir estado da conversa.
3. Se o artefato ja existir, PERGUNTAR ao operador: **Criar Nova** (versiona a
   existente) ou **Sobrescrever Existente**. Nunca decidir sozinho (R17).

## Passo 1 — <Fase 1>

- Script deterministico: `python scripts/<gerar-x>.py <alvo>`
- Skill: `<especialista-1>` — so onde o script nao resolve (R8)

## Passo 2 — <Fase 2>

- <acao>
- Retentativa com backoff em caso de falha transitoria (max. 3 tentativas)

## Passo 3 — <Fase 3: auditoria>

- `python scripts/auditar.py <alvo> --estrito` (encadeia os gates do tipo)
- Falha -> `<revisor>` corrige a **causa**, re-roda o gate. Nunca afrouxar o gate
  para faze-lo passar.

## Passo 4 — Entrega

- `python scripts/validar-artefatos.py <alvo> --estrito` (cada arquivo ABRE?)
- Empacotar so o que esta finalizado e abre
- Gravar relatorio da sessao em `relatorios/<YYYY-MM-DD>-<tema>.md`

## Checklist Final

- [ ] R1..R4 da tabela cumpridos e verificados por comando, nao por impressao
- [ ] Gates retornam exit 0
- [ ] Estado persistido em `<estado.json>`
- [ ] Suite de testes 100% verde (R16)
- [ ] Commit + push feitos

## Falhas Conhecidas

| Sintoma | Causa | Correcao |
|---|---|---|
| <...> | <...> | <...> |
