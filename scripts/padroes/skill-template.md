---
name: <seu-skill>
description: >
  Uma frase dizendo o que o skill faz e quando ativar. O agente le SO isto para
  decidir se carrega o skill — seja concreto, nao generico.
  Triggers: "<gatilho 1>", "<gatilho 2>", "<gatilho 3>"
---

# Skill_<NomeCapitalizado>

Voce e <especialista em X>. Sua responsabilidade e <resultado unico e verificavel>.

## Regras herdadas do CLAUDE.md

- **R1 (Idioma):** todo artefato no idioma do projeto.
- **R2 (Silenciamento):** sem preambulo, saudacao ou meta-comentario no artefato.
- **R4 (Auto-correcao):** desvio detectado e corrigido antes de entregar.
- **R8 (Determinismo primeiro):** se um script resolve, chame o script — nao gere.

## Entrada

| Origem | Formato | Obrigatorio |
|---|---|---|
| `<arquivo-ou-estado>` | `<json/md>` | sim |
| `<parametro>` | `<tipo>` | nao |

## Passo 1 — <Fase 1>

<O que fazer. Comandos deterministicos primeiro; LLM so onde nao ha script.>

## Passo 2 — <Fase 2>

<O que fazer.>

## Passo 3 — <Fase 3>

<O que fazer.>

## Saida

`<caminho/do/artefato>` — <formato e o que precisa conter>.

## Checklist de Entrega

- [ ] Artefato gravado no caminho esperado
- [ ] <criterio de merito 1 — verificavel>
- [ ] <criterio de merito 2 — verificavel>
- [ ] Gate `<validar-x.py>` retorna exit 0
- [ ] Nenhum placeholder `<...>` remanescente no artefato

## Quando NAO usar este skill

<Situacoes em que outro skill/script e a escolha certa. Um skill que nunca
recusa trabalho e um skill que sera chamado errado.>
