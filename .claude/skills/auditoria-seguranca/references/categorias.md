# As cinco categorias e o mapeamento por stack

Cada categoria descreve uma **classe de falha**, nao um padrao de codigo. O mesmo bug
tem aparencia diferente em Supabase, em Django e num CLI. Identifique primeiro o
mecanismo que a stack usa, depois procure onde ele falta.

---

## 1. Banco sem tranca (isolamento de inquilino/dono)

### Descobrir o mecanismo antes de procurar a falha

| Stack | Mecanismo esperado | Onde falha |
|---|---|---|
| Supabase / PostgREST | RLS por tabela + policy | Tabela sem `ENABLE ROW LEVEL SECURITY`; policy `USING (true)`; uso de `service_role` no cliente |
| Prisma / Drizzle / TypeORM | `where` com `userId`/`orgId` em toda query | Query de listagem sem o filtro; `findMany()` cru |
| Django ORM | `get_queryset()` filtrado no ViewSet | `Model.objects.all()` sem override |
| Rails ActiveRecord | `current_user.posts` (scoping por associacao) | `Post.where(...)` partindo do model global |
| SQL cru | Filtro explicito no `WHERE` | `SELECT * FROM t` sem clausula de dono |
| Mongo/Mongoose | `orgId` no filtro | `find({})` |
| App monousuario / CLI | Nao ha isolamento a fazer | Nao se aplica — diga isso |

### Onde olhar

Rotas de **listagem, busca, agregacao, relatorio, exportacao** — sao as que vazam em
volume. Uma exportacao CSV sem filtro de tenant entrega a base inteira num arquivo.

Pontos que escapam com frequencia:

- `COUNT`/`SUM`/`GROUP BY` — vazam por inferencia mesmo sem devolver a linha
- Endpoint de busca com `LIKE` — permite enumerar dados de outro tenant
- Jobs, webhooks e cron que rodam "como sistema" e reaproveitam um handler de usuario
- Rota de admin interno exposta sem o filtro que a rota publica tem
- View SQL e stored procedure — herdam, ou nao, a RLS da tabela base

### Severidade

Vazamento cross-tenant de dado de usuario e **critica**. Se depender de configuracao
incomum, mantenha critica mas registre a condicao.

Ausencia de isolamento num app comprovadamente monousuario e **informativa** — divida
arquitetural, nao vulnerabilidade. Nao infle.

---

## 2. Permissao definida no navegador

O frontend esconde o botao; o servidor precisa recusar a chamada. Esconder a UI e
usabilidade, nao seguranca.

### Metodo — cruzamento obrigatorio

1. Liste todo gate de papel no frontend: `isAdmin`, `canEdit`, `role ===`, `hasPermission`,
   `v-if="user.admin"`, `<RequireRole>`, guardas de rota.
2. Para cada gate, ache **o endpoint que a UI escondida chamaria**.
3. Verifique se esse endpoint valida o privilegio no servidor.

O achado e o par: gate no cliente **sem** verificacao equivalente no servidor.

### Falhas frequentes

- Middleware de auth que so verifica *autenticacao* (`req.user` existe) e nunca
  *autorizacao* (`req.user.role === 'admin'`)
- Papel lido de campo do JWT que o proprio cliente pode setar, ou de header
  (`X-User-Role`), ou do body
- Decorator/guard aplicado no controller mas ausente em uma rota irma
- Rota de mutacao em massa (`bulkDelete`, `importAll`) sem o guard que a rota unitaria tem
- Endpoint novo adicionado depois do guard central, fora do array de rotas protegidas

### Nao se aplica quando

Nao ha frontend com autenticacao, ou nao ha papeis. Diga isso e siga.

---

## 3. IDOR (referencia direta a objeto)

Rota que busca, altera ou deleta objeto por ID **sem verificar posse**.

### Metodo

Percorra **todos** os handlers do backend. Sistematicamente, nao por amostra — IDOR
aparece justamente na rota que ninguem revisou.

Para cada handler que recebe identificador (path, query, body, header):

```
o objeto e carregado por ID cru?          -> candidato
ha checagem de posse/tenant depois disso? -> se nao, achado
a checagem cobre o caminho de erro?       -> 404 vs 403 tambem vaza existencia
```

### Sinais

- `findById(req.params.id)` sem `AND ownerId = ...`
- `DELETE /recurso/:id` que confia no ID
- ID sequencial (enumeravel) agrava: eleva a severidade
- UUID **nao** e defesa — e so obscuridade; ID vazado em log, referer ou export continua valendo
- Verificacao feita no `GET` e esquecida no `PATCH`/`DELETE` do mesmo recurso
- Objeto aninhado: valida posse do pai e nao do filho (`/projeto/:pid/tarefa/:tid` com
  `tid` de outro projeto)

### Severidade

Leitura de dado alheio: **alta**. Escrita ou exclusao de dado alheio: **critica**.

---

## 4. Chaves expostas

### Onde procurar

Codigo-fonte, config, `.env` versionado, `docker-compose.yml`, chart Helm, Terraform,
workflow de CI, script de deploy, notebook, **documentacao**, fixture de teste, e o
**historico git** — o `.gitignore` de hoje nao apaga o commit de ontem.

### Tipos

- Chave de API e token de servico
- Segredo de assinatura: JWT, webhook (Stripe, GitHub)
- Chave privada (`-----BEGIN ... PRIVATE KEY-----`)
- Senha de banco, de painel, de servidor
- Credencial padrao que nunca foi trocada

### Default publico que vira segredo real

Merece atencao especial:

```yaml
JWT_SECRET: ${JWT_SECRET:-changeme}      # sem override, "changeme" assina em producao
POSTGRES_PASSWORD: ${DB_PASS:-postgres}
```

O valor esta no repositorio publico. Quem nao sobrescreveu roda com segredo conhecido.
Pergunte sempre: **existe validacao de startup que recusa o default?** Se nao existe,
isso e um achado por si so.

### Documentacao conta

Guia de instalacao com senha literal e vazamento com alcance amplificado: o leitor copia
e cola em producao. Vale ainda mais quando o publico-alvo e nao-tecnico. Placeholder
(`${DB_SENHA}`) mais instrucao de geracao (`openssl rand -hex 32`) e o correto.

### Historico git

```bash
git log -p --all -S 'PRIVATE KEY' --pickaxe-regex
git log -p --all | grep -iE '(password|secret|token|api[_-]?key)\s*[=:]'
git rev-list --objects --all   # blobs de branch deletada continuam alcancaveis
```

Se houver `git-secrets`, `trufflehog` ou `gitleaks` disponivel, use — mas nao instale
nada globalmente para isso.

### Bundle do frontend

Variavel com prefixo `NEXT_PUBLIC_`, `VITE_`, `REACT_APP_` **e publica por construcao**.
Chave de servico ali e exposicao, nao configuracao. `anon key` de Supabase e publica por
design (a defesa e a RLS); `service_role` no cliente e critica.

### Severidade

Credencial real e viva: **critica**, sempre. Default publico sem validacao de startup:
**alta**. Segredo de exemplo em doc: **alta** se plausivelmente copiado para producao.

### Regra de reporte

Reporte tipo, arquivo, linha e prefixo (`ghp_...`). **Nunca o valor.** E sempre gere o
item humano de rotacao: o segredo commitado deve ser considerado comprometido, mesmo
depois de removido do arquivo.

---

## 5. Inputs sem tratamento (XSS e injecao em template)

### Frontend

| Framework | Vetor |
|---|---|
| React | `dangerouslySetInnerHTML` |
| Vue | `v-html` |
| Angular | `[innerHTML]`, `bypassSecurityTrust*` |
| Svelte | `{@html ...}` |
| DOM puro | `innerHTML`, `outerHTML`, `insertAdjacentHTML`, `document.write` |
| Qualquer | `eval`, `new Function`, `setTimeout` com string |

Mais: markdown renderizado sem sanitizar (`marked` sem `DOMPurify`), e URL controlada
por usuario em `href`/`src` — `javascript:` e `data:text/html` executam.

### Backend

Input de usuario entrando em HTML sem escape: corpo de e-mail, template de PDF,
resposta que devolve HTML, mensagem de erro refletida.

Em geradores de HTML (Python/Go/PHP montando markup por string), o vetor e a
**interpolacao sem escape**:

```python
f'<p>{descricao}</p>'                    # achado se descricao vem de fora
f'<div data-x="{valor}">'                # atributo: aspas quebram o contexto
```

Autoescape existe em Jinja2/Django/Handlebars por padrao — verifique se nao foi
desligado (`| safe`, `{% autoescape off %}`, `mark_safe`, `template.HTML()` em Go).

### Triagem — o que separa achado de ruido

Pergunte **de onde vem o dado**:

- Constante do codigo, inteiro calculado, `array.length` -> ruido (registre como
  informativa se o padrao for arriscado)
- Entrada de usuario, resposta de API externa, campo de banco, nome de arquivo,
  descricao de repositorio de terceiro -> **achado**

Terceiro que controla o dado nao precisa ser o atacante direto. Descricao de repositorio
puxada por API e conteudo controlavel por quem tem escrita naquele repositorio.

### Verifique a defesa existente

O projeto tem lib de sanitizacao (DOMPurify, bleach, sanitize-html)? Esta aplicada nos
pontos encontrados, ou so em alguns? Sanitizacao parcial e achado: da falsa confianca.

### Severidade

XSS armazenado atingindo outros usuarios: **critica**. XSS refletido: **alta**.
Padrao inseguro com dado hoje confiavel: **baixa** ou **informativa**, deixando claro
que a explorabilidade depende de refatoracao futura.
