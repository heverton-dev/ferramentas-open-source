# Modelo de issue para GitHub

Uma issue por achado acionavel. **Agrupe** achados triviais do mesmo tema numa issue
unica (varios defaults de segredo no mesmo compose; o mesmo padrao de escape faltando em
cinco geradores) — issue picotada vira spam e ninguem tria.

Nao agrupe severidades diferentes: critico junto de baixo faz o critico esperar o baixo.

## Template

```markdown
## [Seguranca] <descricao curta da falha>

**Labels:** `security`, `<severidade>`
**Categoria:** <banco-sem-tranca | permissao-navegador | idor | chaves-expostas | inputs-sem-tratamento>

### Problema

<O que esta errado e por que e explorável. Concreto: o caminho do ataque,
nao "pode ser inseguro".>

### Evidencia

`caminho/do/arquivo.ext:123`

```<linguagem>
<trecho real do codigo, segredo mascarado>
```

<Repita para cada ocorrencia se a issue agrupa varias.>

### Impacto

<O que o atacante obtem. Dado de outros usuarios? Escrita? Controle do servidor?>

**Condicoes:** <pre-requisitos, ou "nenhuma">

### Correcao sugerida

<Passos concretos. Se houver correcao equivalente ja aplicada em outro ponto
do repositorio, aponte como referencia.>

### Criterios de aceite

- [ ] <verificavel por quem revisa, nao "esta seguro">
- [ ] <teste que falha antes e passa depois>
- [ ] <se segredo: rotacionado, e nao apenas removido do arquivo>
```

## Regras

**Criterio de aceite e verificavel.** "Corrigir o XSS" nao serve. "`render_card()` aplica
`html.escape()` em `name` e `desc`; teste `test_card_escapa_html` cobre payload com
aspas e tag" serve.

**Segredo exige dois criterios.** Remover do codigo nao desfaz o vazamento:

```markdown
- [ ] Credencial rotacionada no provedor (o valor antigo esta comprometido)
- [ ] Valor removido do arquivo e do historico
- [ ] Gate de startup recusa o valor default
```

**Nunca transcreva o segredo.** Tipo, arquivo, linha e prefixo bastam — a issue costuma
ser publica.

**Uma issue nao vira relatorio.** Sem discussao de arquitetura, sem historico da
auditoria: problema, evidencia, impacto, correcao, aceite.

## Bloco de saida no PDF

No relatorio, cada issue vai delimitada para copiar e colar inteira:

```
--- ISSUE 1 ---
<markdown completo>
--- FIM ISSUE 1 ---
```

Numere na ordem de prioridade de correcao, nao na ordem em que os achados apareceram.
