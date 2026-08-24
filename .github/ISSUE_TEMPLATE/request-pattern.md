---
name: Solicitar novo padrao
about: Propor um padrao reutilizavel (skill, script, comando, MCP, hook, doc)
title: "[padrao] "
labels: ["padrao", "triagem"]
---

## O padrao que estou propondo

<!-- Uma frase: o que ele resolve. -->

## Tipo

- [ ] Skill (`.claude/skills/`)
- [ ] Script determinístico (`scripts/`)
- [ ] Comando (`.claude/commands/`)
- [ ] MCP server
- [ ] Hook (git / Claude Code)
- [ ] Documentação
- [ ] Outro:

## Teste de universalidade (obrigatório)

Este repositório só aceita o que serve a **qualquer domínio**. Um padrão que
depende do vocabulário de um projeto vira template — não vira conteúdo.

Cite **três domínios diferentes** onde este padrão se aplica sem alteração de lógica:

1.
2.
3.

Se você não conseguir citar três, o lugar disto provavelmente é
`scripts/padroes/` como **template** (com placeholders), não como implementação.

## Problema hoje

<!-- O que acontece sem este padrão? Quanto custa (tempo, tokens, retrabalho)? -->

## Solução proposta

<!-- Esboço de código, estrutura de arquivo ou pseudo-fluxo. -->

## Como validar

<!-- Que comando prova que o padrão funciona? Todo padrão precisa de um gate
     mecânico (R9): exit 0 = passou. -->

```bash
```

## Impacto em quem já usa

- [ ] Aditivo — nada quebra em quem já consome o submodule
- [ ] Requer re-cópia de `.claude/` nos projetos consumidores
- [ ] Breaking change (justifique abaixo)

<!-- Se breaking: por que não dá para ser aditivo? -->
