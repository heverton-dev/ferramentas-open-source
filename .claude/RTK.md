# RTK — Guia de Economia de Tokens

Complemento operacional da **Secao 0 do `CLAUDE.md`**. O `CLAUDE.md` diz *o que*
e obrigatorio; este arquivo diz *como* fazer, com comandos e limiares concretos.

## 1. As 4 alavancas (em ordem de retorno)

| Alavanca | O que corta | Skill |
|---|---|---|
| Saida de comando (logs, build, testes) | 60–90% | `headroom` |
| Leitura de codigo/config | 40–70% | `lean-ctx` |
| Prosa do proprio agente | 50–65% | `caveman` |
| Re-analise do mesmo problema | 100% do repeteco | `rtk-memory` |

Aplicar nesta ordem. A maior parte do desperdicio esta em **saida de comando**,
nao no que o agente escreve.

## 2. RTK — Rust Token Killer (proxy de CLI)

Proxy que filtra a saida de comandos de shell antes dela entrar no contexto
(corta ate 90% do output de bash).

### Meta-comandos (sempre chamar `rtk` direto)

```bash
rtk gain              # analytics de economia
rtk gain --history    # historico de comandos com economia por chamada
rtk discover          # analisa o historico e aponta oportunidades perdidas
rtk proxy <cmd>       # executa o comando cru, sem filtro (para debug)
```

### Verificar instalacao

```bash
rtk --version         # deve mostrar: rtk X.Y.Z
rtk gain              # deve funcionar (nao "command not found")
which rtk             # confirmar o binario correto
```

**Colisao de nome:** se `rtk gain` falhar, provavelmente ha o
`reachingforthejack/rtk` (Rust Type Kit) instalado no lugar.

### Uso via hook

Os demais comandos sao reescritos automaticamente pelo hook do Claude Code:
`git status` -> `rtk git status` (transparente, 0 tokens de overhead).

RTK e **opcional**: sem ele, a regra de compressao continua valendo — passa a ser
responsabilidade do agente aplicar `headroom` manualmente.

## 3. Headroom — regra das 7 linhas

Se a saida de um teste, build ou comando ultrapassar **7 linhas**:

1. Manter apenas as **3 primeiras** e as **4 ultimas** (onde fica a causa raiz).
2. Omitir o miolo com `[... N linhas omitidas por headroom ...]`.
3. Nunca colar stacktrace inteiro de biblioteca de terceiros.

Preferir filtrar na origem a comprimir depois:

```bash
python -m pytest -q            # -q em vez da saida completa
npm run build 2>&1 | tail -20  # so o fim
git log --oneline -10          # nunca git log cru
grep -c "ERRO" arquivo.log     # contar em vez de ler
```

## 4. LeanCTX — grep antes de read

1. **Grep antes de read:** nunca ler um arquivo inteiro sem antes localizar a
   linha exata.
2. **Assinaturas antes de corpos:** para entender uma interface, ler so
   declaracoes, exports e assinaturas.
3. **Slice restrito:** ao ler, limitar a 20–50 linhas por trecho.
4. **Sem releitura:** nao reler o que ja esta no contexto.

## 5. Isencoes (sobrepoem tudo acima)

Nunca comprimir:

- Conteudo de entrega (`output/**` ou equivalente do dominio) — R7.
- JSONs de estado da esteira — R11.
- Saida de gates de validacao (o gate existe justamente para ser lido inteiro).
- Compilacao de artefato final (PDF/build) — liberada e obrigatoria.

Comprimir entrega e a unica forma de "economia" que custa mais caro do que
economiza: gera retrabalho de geracao, que e a operacao mais cara do fluxo.

## 6. Memoria persistente (`rtk-memory`)

O maior desperdicio recorrente nao e verbosidade — e **re-descobrir o que ja foi
descoberto**. Registrar em `RTK-SCRATCHPAD.md` (raiz do projeto):

- erro resolvido (sintoma -> causa -> fix)
- decisao arquitetural (o que foi decidido e por que)
- padrao descoberto (armadilha do stack/SO)

`RTK-SCRATCHPAD.md` fica **fora** do `CLAUDE.md` de proposito: o `CLAUDE.md`
precisa ser estavel para servir de prefixo de cache. Ver a skill `rtk-memory`
para o protocolo e os templates de entrada.

## 7. Pre-flight (`pre-flight-check`)

Antes de deploy, commit estrutural ou refatoracao: rodar type-check, testes e
build **localmente**. Bloquear se qualquer etapa falhar. Barato comparado a
descobrir a falha depois, em CI ou em producao — e o ciclo de correcao
pos-falha e o que mais consome contexto.

## 8. Checklist rapido

```
[ ] Comando produz >7 linhas?      -> filtrar na origem (-q, tail, grep -c)
[ ] Vou ler arquivo inteiro?       -> grep primeiro, depois slice
[ ] Ja resolvi isso antes?         -> consultar RTK-SCRATCHPAD.md
[ ] E conteudo de entrega?         -> NAO comprimir (R7)
[ ] Vou commitar?                  -> pre-flight-check antes
```
