# Fixup: Correção de Gaps Óbvios

## Diretivas Obrigatórias

1. **Escopo Mínimo:** Corrigir apenas gaps explícitos, falhas de sintaxe, imports faltantes.
2. **Sem Refactor:** Nenhuma reorganização, renomação ou melhoria estética.
3. **Sem Explicação:** Código apenas, em blocos ` ```file <caminho> ``` `.
4. **Preservar Lógica:** Manter estrutura original intacta.

## O Que É Gap Óbvio

- Import faltante que quebra a execução.
- Variável indefinida ou digitação errada óbvia.
- Falta de `return` em função.
- Indentação quebrada.
- Sintaxe inválida que qualquer linter detecta.

## O Que NÃO É Fixup

- Refactor de variáveis ou funções.
- Melhoria de performance.
- Adição de validação ou logging extra.
- Mudança de fluxo ou lógica.
- Comentários ou docstrings.

## Entrada

- Arquivo ou trecho com erro.
- Descrição breve do erro.
- Contexto (libs, Python 3.8+, Windows UTF-8, etc).

## Saída

```file <caminho>
<código corrigido, linha mínima alterada>
```

## Exemplos de Fixup OK

```
# Antes: NameError
x = 10
print(y)  # y indefinida

# Depois
x = 10
y = 20
print(y)
```

```
# Antes: SyntaxError (indentação)
def func():
print("test")

# Depois
def func():
    print("test")
```

## Checklist Silent

- [ ] Apenas gap óbvio corrigido.
- [ ] Nenhuma explicação.
- [ ] Lógica original preservada.
- [ ] Sintaxe OK.
- [ ] Pronto para re-run.
- [ ] Não adicionar testes, logs ou comments.
