# Deteccao de stack

`varrer.py` faz a deteccao automatica. Este documento cobre o que fazer quando ela vem
incompleta, e como a stack muda o que auditar.

## Matriz de manifesto

| Arquivo | Ecossistema |
|---|---|
| `package.json` | Node/JS — leia `dependencies` para achar framework e ORM |
| `requirements.txt`, `pyproject.toml`, `Pipfile` | Python |
| `go.mod` | Go |
| `Cargo.toml` | Rust |
| `composer.json` | PHP (Laravel, Symfony) |
| `Gemfile` | Ruby (Rails, Sinatra) |
| `pom.xml`, `build.gradle` | Java/Kotlin (Spring) |
| `*.csproj` | .NET |
| `pubspec.yaml` | Dart/Flutter |

## O que extrair

**Framework HTTP** — define onde ficam os handlers de rota:
Express, Fastify, NestJS, Next (route handlers e server actions), Django, Flask, FastAPI,
Rails, Laravel, Spring, Gin, Actix.

**ORM / acesso a dados** — define como o filtro de tenant deveria aparecer:
Prisma, Drizzle, TypeORM, Sequelize, Mongoose, SQLAlchemy, Django ORM, ActiveRecord,
Eloquent, GORM, Diesel, ou SQL cru.

**Auth** — define o que significa "o usuario autenticado":
NextAuth/Auth.js, Passport, Clerk, Auth0, Supabase Auth, Firebase Auth, Devise,
Spring Security, JWT artesanal, sessao em cookie.

Anote **de onde sai a identidade**: `req.user.id` de sessao assinada e confiavel;
`req.headers['x-user-id']` nao e.

**Frontend** — define os vetores de XSS:
React, Vue, Angular, Svelte, HTMX, template server-side, HTML estatico, ou nenhum.

**Deploy** — define onde procurar segredo:
`Dockerfile`, `docker-compose*.yml`, `.github/workflows/`, `.gitlab-ci.yml`, `charts/`,
`*.tf`, `vercel.json`, `fly.toml`, `serverless.yml`, `k8s/`.

## Casos que mudam o veredito

**Sem servidor proprio (SPA + BaaS).** O backend e o BaaS. Auditoria vira RLS/regras de
seguranca (Supabase policies, Firestore rules). "IDOR" e "autorizacao no servidor"
colapsam dentro dessas regras.

**Monolito com template server-side.** Nao ha fronteira de API; autorizacao e XSS moram
na mesma camada de view.

**CLI, biblioteca, gerador estatico, pipeline de dados.** Sem HTTP e sem sessao:
categorias 1, 2 e 3 tipicamente **nao se aplicam**. Segredos e injecao continuam
valendo, e ganham peso — CLI costuma manipular credencial e montar comando.

Nesse caso, avalie tambem, dentro da categoria 5:
- Injecao de comando: `shell=True`, `os.system`, string montada para shell
- Path traversal: caminho vindo de argumento sem normalizar
- Desserializacao insegura: `pickle`, `yaml.load` sem `SafeLoader`

**Monorepo.** Detecte por pacote. Um `apps/api` Node e um `apps/web` Next tem
superficies distintas; audite cada um com o mapeamento proprio.

## Quando a deteccao falha

Se `varrer.py` nao identificar a stack, nao chute: inspecione o ponto de entrada
(`main`, `index`, `app`, `cmd/`) e siga os imports. Registre a stack detectada na nota
metodologica do relatorio, incluindo o que ficou indeterminado.

Stack indeterminada nao impede a auditoria — impede o **automatismo**. Audite lendo.
