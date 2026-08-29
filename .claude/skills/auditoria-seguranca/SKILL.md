---
name: auditoria-seguranca
description: Ciclo completo de auditoria de seguranca com correcao e prova antes/depois. Detecta a stack do projeto, audita cinco categorias (isolamento de tenant, autorizacao no servidor, IDOR, segredos expostos, XSS/inputs), corrige o que e seguro corrigir via /implementacao, re-audita em contexto limpo e emite relatorio comparativo em PDF. Use quando o usuario pedir auditoria de seguranca, revisao de vulnerabilidades, varredura de segredos, verificacao de RLS/multi-tenancy, checagem de IDOR ou XSS, ou um relatorio de seguranca antes/depois.
---

# Auditoria de Seguranca com Ciclo de Correcao

Quatro estagios: **auditar -> corrigir -> re-auditar -> comparar**. Cada estagio produz
artefato em disco, de modo que o ciclo e retomavel e o resultado e auditavel por terceiros.

## Principio central

A varredura por padrao textual **levanta candidatos, nao achados**. Um `innerHTML` com
inteiro interno e ruido; o mesmo `innerHTML` com dado de terceiro e vulnerabilidade.
So a leitura do codigo separa os dois.

Portanto: `varrer.py` coleta (barato, deterministico, reproduzivel) e **voce triaga**
(caro, precisa de julgamento). Nunca promova candidato a achado sem abrir o arquivo.

Nunca reporte achado que nao verificou no codigo real. "Provavelmente existe" nao entra
no relatorio.

---

## Estagio 1 — Auditoria baseline

### 1.1 Detectar a stack

```bash
python <skill>/scripts/varrer.py --raiz . --saida .auditoria/candidatos.json
```

Emite a stack detectada (linguagem, framework, ORM, auth, frontend, deploy) e os
candidatos por categoria. Leia `references/deteccao-stack.md` se a deteccao vier
incompleta ou se a stack for incomum.

### 1.2 Mapear as cinco categorias para esta stack

Leia `references/categorias.md`. Para cada categoria, decida **como ela se manifesta aqui**
antes de procurar. Exemplo: "isolamento de tenant" e RLS no Supabase, middleware no
NestJS, filtro manual por `user_id` numa API artesanal — e **nao se aplica** num CLI
monousuario.

Categoria que nao se aplica: diga isso explicitamente no relatorio, com a razao. Nao
force achado para preencher tabela.

### 1.3 Triar os candidatos

Para cada candidato em `candidatos.json`, abra o arquivo e decida:

- **Achado**: e explorável. Registre arquivo, linha exata, trecho, por que e explorável,
  severidade (critica/alta/media/baixa/informativa) e condicoes de explorabilidade
  (feature flag, config insegura necessaria, precisa de repo hostil na org, etc).
- **Ruido**: nao e explorável. Descarte, mas se o padrao for arriscado numa refatoracao
  futura, registre como informativa.
- **Ponto forte**: o codigo faz a coisa certa. Registre com evidencia — isso prova a
  cobertura da auditoria e vai para a secao de pontos fortes.

Para categorias que exigem varrer **todos** os handlers (IDOR, autorizacao no servidor),
percorra o inventario completo que o `varrer.py` produziu. Amostragem nao vale.

Em base grande, distribua a triagem por subagentes — um por categoria — e consolide.

### 1.4 Gravar o baseline

Monte `.auditoria/baseline.json` no formato de `references/formato-achados.md` e
carimbe o fingerprint de cada achado:

```bash
python <skill>/scripts/fingerprint.py --entrada .auditoria/baseline.json --inplace
```

O fingerprint ignora numero de linha de proposito: linha muda a cada edicao, e um achado
que so mudou de posicao nao pode contar como "corrigido".

Cada achado recebe dois ids: `id` (categoria + arquivo + titulo normalizado) e
`id_local` (categoria + arquivo, sem titulo). O segundo existe porque duas auditorias
independentes descrevem o mesmo problema com palavras diferentes, e so o `id` faria o
achado contar como corrigido **e** como novo ao mesmo tempo.

**Nao altere a formula do fingerprint com um ciclo em andamento.** Recarimbar muda todos
os ids e invalida qualquer reconciliacao ja escrita. Se precisar mudar, refaca baseline
e reconciliacao juntos.

### 1.5 Relatorio baseline

```bash
python <skill>/scripts/render_relatorio.py --achados .auditoria/baseline.json \
  --modo baseline --saida docs/security-audit/relatorio-baseline.pdf
```

Usa o navegador headless ja instalado. Nao instala nada.

---

## Estagio 2 — Correcao

### 2.1 Classificar cada achado em uma das tres faixas

| Faixa | Criterio | Destino |
|---|---|---|
| `auto` | Edicao em codigo-fonte, reversivel por git, efeito local | Vira fase do plano |
| `confirmar` | Toca artefato gerado, volume grande, ou muda comportamento observavel | Pergunta antes |
| `humano` | Destrutivo, irreversivel ou externo ao repositorio | Checklist, nunca comando |

Sempre `humano`, sem excecao:

- Reescrita de historico git (`filter-branch`, `filter-repo`, BFG) — reescreve historico
  compartilhado e quebra o clone de todo mundo.
- Rotacao/revogacao de credencial (PAT, senha de painel, chave de API, acesso a servidor)
  — acontece fora do repositorio e so o dono pode fazer.
- Qualquer alteracao em ambiente de producao.

Segredo commitado gera **as duas coisas**: uma correcao `auto` que impede o proximo vazamento
(gate de startup, `.env.example`, hook de pre-commit) e um item `humano` que trata o
vazamento que ja ocorreu (rotacionar, limpar historico). Corrigir so o primeiro deixa a
credencial viva.

### 2.2 Gerar o plano

```bash
python <skill>/scripts/gerar_plano_correcao.py --achados .auditoria/baseline.json \
  --saida .auditoria/plano-correcao.json
```

Emite **um plano por achado**, no contrato real de `/implementacao`: o runner despacha
pelo valor de `phase.id` e so reconhece `impl`, `test`, `validate` e `verify`
(`index.cjs:301-313`). Um plano com uma fase por achado e ignorado inteiro —
cada plano e um ciclo de quatro fases sobre **um** achado.

Saida:

```
.auditoria/planos/auto/NN-<slug>.json              executar
.auditoria/planos/sob-confirmacao/NN-<slug>.json   so apos aprovacao explicita
.auditoria/checklist-humano.md                     nunca automatizar
.auditoria/plano-correcao.json                     indice
```

A separacao em diretorios distintos e deliberada: o runner **nao le nenhum flag de
habilitacao**, entao um campo `enabled: false` no mesmo arquivo seria executado do
mesmo jeito. Manter os planos fisicamente separados e a unica garantia real.

### 2.2b Verificar o que o projeto dispara sozinho

**Antes de rodar qualquer script do projeto, veja se ele publica.** Muitos pipelines
chamam `git add`/`commit`/`push` ao final. Rodar um comando de build para verificar uma
correcao pode publicar no remoto — acao externa que exige decisao do dono, nao efeito
colateral de uma auditoria.

```bash
grep -rn "git push\|git commit\|git_sync\|gh release\|npm publish\|docker push" \
  <script-que-voce-vai-rodar>
```

Se dispara: avise o usuario e combine antes de executar.

Verifique tambem se o push esta **encadeado ao sucesso do commit**. Um pipeline que
trata commit barrado como aviso e segue para o push tem uma barreira furada: o hook
impede o commit da vez e publica o resto assim mesmo.

### 2.2c Reclassificar com o contexto do dono

Antes de propor correcao, confirme o proposito do que voce marcou como defeito. Dois
enganos frequentes:

- **Material didatico com valor concreto.** Num projeto cujo objetivo e ensinar
  nao-tecnicos, passo a passo com valor literal e o produto. O defeito nao e o valor
  concreto — e todos os leitores receberem o **mesmo** segredo. A correcao certa ensina
  a gerar o proprio, e fica mais didatica, nao menos.
- **Credencial operacional.** Um `.env` que o dono usa para acessar a propria
  infraestrutura nao e "credencial acumulada por descuido". Nao proponha migrar para
  cofre por reflexo: proteja o que existe (nao vazar para cache/indice, falhar cedo se
  faltar) e ajuste a severidade.

Perguntar custa uma pergunta. Corrigir contra o proposito do projeto custa a confianca
no relatorio inteiro.

### 2.3 Escrever as correcoes como script, nao como edicao manual

Cada fase `auto` aponta para um script de correcao em `.auditoria/correcoes/`. Escreva
esses scripts antes de rodar o plano. Motivo: correcao roteirizada e reexecutavel,
revisavel em diff e idempotente — edicao manual em dezenas de arquivos nao e.

Toda correcao precisa de um teste que **falha antes e passa depois**. Rode a suite
**antes** de aplicar qualquer correcao e confirme que ela falha. Teste que passa nos
dois estados nao prova nada — e o modo mais comum de declarar corrigido o que nao foi.

Cuidado com efeito colateral no teste: se a funcao sob teste escreve em caminho real do
projeto, use `tmp_path`/`monkeypatch.chdir`. Teste que sobrescreve artefato versionado
corrompe o repositorio enquanto finge verificar.

### 2.4 Executar

```bash
for p in .auditoria/planos/auto/*.json; do
  node .claude/skills/implementacao/index.cjs "$p"
done
```

Cada plano precisa terminar em `Status: SUCESSO`. Fase de teste que entra em retry
significa correcao incompleta — leia a saida do pytest, conserte o script de correcao
e reexecute aquele plano.

Depois de rodar tudo: `python -m pytest .auditoria/correcoes/ -q` deve ficar 100% verde.

Os planos em `planos/sob-confirmacao/` e o checklist humano vao ao usuario **antes** de
qualquer execucao. Nao decida por ele.

---

## Estagio 3 — Re-auditoria em contexto limpo

Rode a re-auditoria **em subagente novo**, e passe a ele apenas:

- a raiz do projeto,
- a lista de categorias a auditar,
- o caminho da skill.

**Nao passe** o baseline, o plano de correcao nem o registro do que foi alterado. Quem
acabou de corrigir e o pior juiz do proprio conserto: sabendo o que mexeu, o subagente
confirma a expectativa em vez de reexaminar o codigo.

O subagente repete o Estagio 1 integralmente e grava `.auditoria/pos-correcao.json`.

---

## Estagio 4 — Comparativo antes/depois

```bash
python <skill>/scripts/comparar.py --baseline .auditoria/baseline.json \
  --pos .auditoria/pos-correcao.json --saida .auditoria/comparativo.json
```

Casa em tres camadas — `id` exato, depois reconciliacao explicita, depois
`id_local` — e classifica cada achado:

- **corrigido** — estava no baseline, sumiu
- **persistente** — esta nos dois
- **novo** — so no pos (regressao introduzida pela correcao, ou achado que a primeira
  passada perdeu; o relatorio deve distinguir os dois casos)

### Reconciliar antes de aceitar o resultado

**Sempre revise o comparativo antes de gerar o PDF.** Quando o mesmo problema aparece
nas duas passadas em arquivos diferentes — a segunda encontrou a origem, a primeira via
o sintoma — nenhuma chave automatica casa isso, e o achado e contado duas vezes: some
de um lado como "corrigido", aparece do outro como "novo". O numero fica bonito e
mentiroso.

Sinal de alerta: taxa de correcao alta com muitos "novos" e quase nenhum "persistente".

Escreva os pares em `.auditoria/reconciliacao.json`:

```json
{
  "pares": { "<id_baseline>": "<id_pos>" },
  "justificativas": { "<id_baseline> -> <id_pos>": "por que sao o mesmo achado" }
}
```

Reconcilie apenas o que **e** o mesmo achado. Forcar par para melhorar a taxa e
falsificar o relatorio.

### Correcao feita depois da foto

Se voce corrigir algo apos gerar `pos-correcao.json`, **nao edite o arquivo**: ele e o
registro de um momento. Re-verifique o ponto especifico, documente a prova no relatorio
e deixe o comparativo mostrar o estado da foto. Apagar achado do pos e auto-absolvicao.

**Gate (exit code):** `exit 1` se sobrar critico do baseline sem resolver, ou se surgir
qualquer achado novo em qualquer severidade. Caso contrario `exit 0`.

Gate vermelho nao e motivo para reescrever o gate. E motivo para voltar ao Estagio 2.

```bash
python <skill>/scripts/render_relatorio.py --comparativo .auditoria/comparativo.json \
  --modo comparativo --saida docs/security-audit/relatorio-antes-depois.pdf
```

---

## Verificar o PDF antes de entregar

Todo PDF gerado passa por conferencia:

```bash
python <skill>/scripts/render_relatorio.py --verificar docs/security-audit/<arquivo>.pdf
```

Reporta contagem de paginas e tamanho. Alem disso, rasterize a pagina (ou capture o HTML
de origem com o navegador headless) e **olhe**: grafico renderizou, tabela nao estourou a
margem, chip de severidade legivel, nada cortado na quebra de pagina. Corrija defeito
visual antes de entregar.

---

## Regra de sigilo

O relatorio aponta **onde** esta o segredo (arquivo, linha, tipo, prefixo). Nunca
transcreve o valor. Copiar um token vazado para dentro do PDF de auditoria multiplica
o vazamento — o PDF costuma circular mais que o repositorio.

Vale para o chat, para os arquivos de trabalho e **principalmente para os testes**.
Nunca use a credencial real do projeto como dado de teste: o nodeid de um teste
parametrizado vai para `.pytest_cache/v/cache/nodeids` em texto plano, e indexadores de
codigo copiam o mesmo valor para os bancos deles. Um segredo que existia so no `.env`
passa a existir em tres lugares — criados pela propria auditoria.

Use valores sinteticos que casem com o formato (`ghp_0000FAKE...`), nunca o valor vivo.

---

## Entregaveis

| Caminho | Conteudo |
|---|---|
| `docs/security-audit/relatorio-baseline.pdf` | Auditoria inicial |
| `docs/security-audit/relatorio-pos-correcao.pdf` | Auditoria apos correcao |
| `docs/security-audit/relatorio-antes-depois.pdf` | Comparativo com veredito do gate |
| `.auditoria/*.json` | Estado do ciclo (retomavel) |
| `.auditoria/checklist-humano.md` | Acoes que so o dono pode executar |

Adicione `.auditoria/` ao `.gitignore` **no inicio do ciclo**, antes de gravar o
baseline: o diretorio contem caminhos e trechos de codigo de achados ainda abertos, e
qualquer `git add .` no meio do caminho o versionaria.

Ao terminar, confira `git status` e confirme que o ciclo nao deixou artefato de teste
em arquivo versionado.

## Referencias

- `references/categorias.md` — as cinco categorias e como mapear para cada stack
- `references/deteccao-stack.md` — matriz de deteccao e o que fazer com stack incomum
- `references/formato-achados.md` — schema de `baseline.json` e severidades
- `references/modelo-issue.md` — template de issue para GitHub
