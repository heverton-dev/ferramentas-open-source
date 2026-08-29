#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Coletor deterministico de candidatos para auditoria de seguranca.

NAO decide o que e vulnerabilidade. Levanta candidatos, detecta a stack e monta o
inventario de handlers para que a triagem (feita por leitura do codigo) seja completa
em vez de amostral.

Uso:
    python varrer.py --raiz . --saida .auditoria/candidatos.json
    python varrer.py --raiz . --so-stack          # apenas deteccao de stack

Stdlib apenas. Sem instalacao.
"""
import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

IGNORAR_DIRS = {
    ".git", "node_modules", "__pycache__", ".venv", "venv", "dist", "build",
    ".next", ".nuxt", "vendor", "target", ".pytest_cache", ".mypy_cache",
    "coverage", ".tox", "bower_components", ".gradle", "bin", "obj",
    ".auditoria", ".cache", ".parcel-cache", "site-packages",
}

EXT_CODIGO = {
    ".py", ".js", ".jsx", ".ts", ".tsx", ".mjs", ".cjs", ".vue", ".svelte",
    ".go", ".rb", ".php", ".java", ".kt", ".cs", ".rs", ".sql", ".html",
    ".htm", ".ejs", ".erb", ".hbs", ".twig", ".astro",
}
EXT_CONFIG = {
    ".env", ".yml", ".yaml", ".json", ".toml", ".ini", ".cfg", ".conf",
    ".tf", ".tfvars", ".properties", ".sh", ".ps1", ".bash",
}

MAX_BYTES = 2_000_000


# ---------------------------------------------------------------- deteccao


MANIFESTOS = {
    "package.json": "javascript",
    "requirements.txt": "python",
    "pyproject.toml": "python",
    "Pipfile": "python",
    "go.mod": "go",
    "Cargo.toml": "rust",
    "composer.json": "php",
    "Gemfile": "ruby",
    "pom.xml": "java",
    "build.gradle": "java",
    "pubspec.yaml": "dart",
}

FRAMEWORKS = {
    "next": "Next.js", "express": "Express", "fastify": "Fastify",
    "@nestjs/core": "NestJS", "koa": "Koa", "hapi": "Hapi",
    "django": "Django", "flask": "Flask", "fastapi": "FastAPI",
    "rails": "Rails", "sinatra": "Sinatra", "laravel/framework": "Laravel",
    "symfony/framework-bundle": "Symfony", "gin-gonic/gin": "Gin",
    "actix-web": "Actix", "spring-boot": "Spring Boot",
}

ORMS = {
    "prisma": "Prisma", "@prisma/client": "Prisma", "drizzle-orm": "Drizzle",
    "typeorm": "TypeORM", "sequelize": "Sequelize", "mongoose": "Mongoose",
    "knex": "Knex", "sqlalchemy": "SQLAlchemy", "django": "Django ORM",
    "peewee": "Peewee", "activerecord": "ActiveRecord", "gorm.io/gorm": "GORM",
    "diesel": "Diesel", "better-sqlite3": "better-sqlite3 (SQL cru)",
    "sqlite3": "sqlite3 (SQL cru)", "pg": "node-postgres (SQL cru)",
    "psycopg2": "psycopg2 (SQL cru)", "mysql2": "mysql2 (SQL cru)",
}

AUTHS = {
    "next-auth": "NextAuth/Auth.js", "@auth/core": "Auth.js",
    "passport": "Passport", "@clerk/nextjs": "Clerk", "auth0": "Auth0",
    "@supabase/supabase-js": "Supabase Auth", "firebase-admin": "Firebase Auth",
    "jsonwebtoken": "JWT artesanal", "pyjwt": "JWT artesanal",
    "devise": "Devise", "flask-login": "Flask-Login",
    "django.contrib.auth": "Django Auth", "spring-boot-starter-security": "Spring Security",
    "lucia": "Lucia", "better-auth": "Better Auth",
}

FRONTS = {
    "react": "React", "vue": "Vue", "@angular/core": "Angular",
    "svelte": "Svelte", "solid-js": "Solid", "htmx.org": "HTMX",
    "preact": "Preact",
}

ARQ_DEPLOY = [
    "Dockerfile", "docker-compose.yml", "docker-compose.yaml",
    "vercel.json", "fly.toml", "serverless.yml", "Procfile", "netlify.toml",
]


def _ler(p: Path, limite: int = MAX_BYTES) -> str:
    try:
        if p.stat().st_size > limite:
            return ""
        return p.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return ""


def detectar_stack(raiz: Path) -> dict:
    stack = {
        "linguagens": [], "framework": None, "orm": None,
        "auth": None, "frontend": None, "deploy": [], "manifestos": [],
    }
    deps_texto = ""

    for arq, ling in MANIFESTOS.items():
        p = raiz / arq
        if p.is_file():
            stack["manifestos"].append(arq)
            if ling not in stack["linguagens"]:
                stack["linguagens"].append(ling)
            deps_texto += _ler(p).lower() + "\n"

    # requirements.txt pode estar aninhado
    for extra in ("requirements-dev.txt", "requirements/base.txt"):
        p = raiz / extra
        if p.is_file():
            deps_texto += _ler(p).lower() + "\n"

    def casar(mapa):
        achados = [nome for chave, nome in mapa.items() if chave.lower() in deps_texto]
        return ", ".join(dict.fromkeys(achados)) if achados else None

    stack["framework"] = casar(FRAMEWORKS)
    stack["orm"] = casar(ORMS)
    stack["auth"] = casar(AUTHS)
    stack["frontend"] = casar(FRONTS)

    for nome in ARQ_DEPLOY:
        if (raiz / nome).is_file():
            stack["deploy"].append(nome)
    for padrao in ("docker-compose*.yml", "*.tf", "charts/**/Chart.yaml",
                   ".github/workflows/*.yml", ".gitlab-ci.yml", "k8s/**/*.yaml"):
        for p in raiz.glob(padrao):
            rel = p.relative_to(raiz).as_posix()
            if rel not in stack["deploy"]:
                stack["deploy"].append(rel)

    # Contagem de arquivos SEMPRE: um manifesto nao prova que a linguagem dominante
    # do repositorio e a dele. Projeto com package.json e 1800 scripts .py e Python.
    cont = {}
    for p in caminhar(raiz):
        cont[p.suffix.lower()] = cont.get(p.suffix.lower(), 0) + 1
    for exts, ling in (((".py",), "python"),
                       ((".js", ".jsx", ".mjs", ".cjs"), "javascript"),
                       ((".ts", ".tsx"), "typescript"),
                       ((".go",), "go"), ((".rb",), "ruby"), ((".php",), "php"),
                       ((".java", ".kt"), "java"), ((".rs",), "rust"),
                       ((".cs",), "csharp"), ((".sh", ".bash"), "shell"),
                       ((".ps1",), "powershell")):
        n = sum(cont.get(e, 0) for e in exts)
        if n > 2 and ling not in stack["linguagens"]:
            stack["linguagens"].append(ling)
    stack["contagem_arquivos"] = {k: v for k, v in sorted(
        cont.items(), key=lambda kv: -kv[1]) if v > 0 and k}

    return stack


def caminhar(raiz: Path):
    for dirpath, dirnames, filenames in os.walk(raiz):
        dirnames[:] = [d for d in dirnames if d not in IGNORAR_DIRS and not d.startswith(".venv")]
        for fn in filenames:
            p = Path(dirpath) / fn
            if p.suffix.lower() in EXT_CODIGO or p.suffix.lower() in EXT_CONFIG or fn.startswith(".env"):
                yield p


# ---------------------------------------------------------------- padroes


# (regra, regex, categoria, nota para a triagem)
PADROES = [
    # --- chaves expostas
    ("segredo-atribuido", r'(?i)\b(api[_-]?key|apikey|secret|token|passwd|password|senha|private[_-]?key|access[_-]?key|client[_-]?secret)\b\s*[:=]\s*["\'][^"\'{}$\s][^"\']{7,}["\']',
     "chaves-expostas", "Confirme se e valor real ou placeholder/exemplo."),
    ("chave-privada", r'-----BEGIN (RSA |EC |OPENSSH |PGP )?PRIVATE KEY-----',
     "chaves-expostas", "Chave privada literal. Quase sempre achado."),
    ("token-provedor", r'\b(ghp_[A-Za-z0-9]{20,}|gho_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|sk-[A-Za-z0-9]{20,}|xox[baprs]-[A-Za-z0-9-]{10,}|AKIA[0-9A-Z]{16}|AIza[0-9A-Za-z_-]{35})',
     "chaves-expostas", "Formato de token de provedor conhecido."),
    ("default-publico", r'\$\{[A-Z_][A-Z0-9_]*:-[^}\s]+\}',
     "chaves-expostas", "Default vira segredo real sem override. Ha validacao de startup?"),
    ("var-publica-frontend", r'\b(NEXT_PUBLIC_|VITE_|REACT_APP_|PUBLIC_)[A-Z0-9_]*(KEY|SECRET|TOKEN|PASSWORD)\b',
     "chaves-expostas", "Prefixo publico: vai para o bundle do cliente."),
    ("service-role", r'(?i)\bservice[_-]?role\b',
     "chaves-expostas", "service_role no cliente ignora RLS. Verifique o lado."),

    # --- inputs / xss
    ("html-perigoso", r'\b(dangerouslySetInnerHTML|v-html|\[innerHTML\]|\{@html|insertAdjacentHTML|document\.write)\b',
     "inputs-sem-tratamento", "Rastreie a origem do dado."),
    ("innerhtml", r'\.(inner|outer)HTML\s*(=|\+=)',
     "inputs-sem-tratamento", "Ruido se o valor for constante/inteiro; achado se vier de fora."),
    ("eval", r'\b(eval\(|new Function\(|setTimeout\s*\(\s*["\']|setInterval\s*\(\s*["\'])',
     "inputs-sem-tratamento", "Execucao de string."),
    ("escape-desligado", r'(\|\s*safe\b|\{%\s*autoescape\s+off|mark_safe\(|bypassSecurityTrust|template\.HTML\(|dangerouslyAllow)',
     "inputs-sem-tratamento", "Autoescape desativado explicitamente."),
    ("interp-html", r'f["\'][^"\'\n]*<[a-zA-Z][^"\'\n]*\{[a-zA-Z_][^"\'\n]*\}[^"\'\n]*["\']',
     "inputs-sem-tratamento", "f-string montando HTML. Ha escape na variavel?"),
    ("markdown-cru", r'\b(marked|markdown-it|showdown|remark)\b[^\n]{0,80}',
     "inputs-sem-tratamento", "Render de markdown: ha sanitizacao junto?"),
    ("shell-injection", r'(shell\s*=\s*True|os\.system\(|exec\.Command\(\s*["\'](sh|bash|cmd)|child_process\.exec\()',
     "inputs-sem-tratamento", "Comando montado como string."),
    ("desserializacao", r'\b(pickle\.loads?\(|yaml\.load\((?![^)]*SafeLoader)|unserialize\()',
     "inputs-sem-tratamento", "Desserializacao insegura."),

    # --- isolamento / idor / autorizacao
    ("query-sem-filtro", r'\.(findMany|findAll|find)\(\s*\)|\bobjects\.all\(\)|SELECT\s+\*\s+FROM\s+\w+\s*(;|$)',
     "banco-sem-tranca", "Listagem sem clausula de dono. Confirme se ha filtro adiante."),
    ("busca-por-id", r'\.(findUnique|findById|findOne|get_object_or_404|find_by_id)\s*\(',
     "idor", "Carregou por ID: ha checagem de posse depois?"),
    ("id-de-request", r'(req|request)\.(params|query|body)\s*(\.|\[)\s*["\']?\w*[Ii]d\b',
     "idor", "ID vindo do cliente."),
    ("rls-desligada", r'(?i)(disable\s+row\s+level\s+security|USING\s*\(\s*true\s*\))',
     "banco-sem-tranca", "Policy permissiva ou RLS desativada."),
    ("gate-cliente", r'\b(isAdmin|is_admin|canEdit|can_edit|hasRole|hasPermission|userRole|user\.role\s*===)\b',
     "permissao-navegador", "Gate de papel: existe verificacao equivalente no servidor?"),
    ("papel-de-header", r'(?i)(headers?\s*\[\s*["\']x-[\w-]*(role|admin|user)|req\.body\.(role|isAdmin))',
     "permissao-navegador", "Papel vindo do cliente: falsificavel."),
]

# handlers de rota, para o inventario
ROTAS = [
    r'\b(?:app|router|api)\.(get|post|put|patch|delete|all)\s*\(\s*["\'`]([^"\'`]+)',
    r'@(?:app|router)\.(get|post|put|patch|delete)\s*\(\s*["\']([^"\']+)',
    r'@(Get|Post|Put|Patch|Delete)\s*\(\s*["\']?([^"\')]*)',
    r'\bexport\s+async\s+function\s+(GET|POST|PUT|PATCH|DELETE)\b()',
    r'\bpath\s*\(\s*["\']([^"\']+)["\']\s*,()',
    r'\b(get|post|put|patch|delete)\s+["\']([^"\']+)["\']\s*(?:=>|,\s*to:)',
]


def varrer_arquivo(p: Path, raiz: Path):
    texto = _ler(p)
    if not texto:
        return [], []
    rel = p.relative_to(raiz).as_posix()
    linhas = texto.splitlines()
    candidatos, rotas = [], []

    for regra, rx, cat, nota in PADROES:
        try:
            for m in re.finditer(rx, texto):
                n = texto.count("\n", 0, m.start()) + 1
                bruto = linhas[n - 1].strip() if n <= len(linhas) else m.group(0)
                candidatos.append({
                    "regra": regra, "categoria": cat, "arquivo": rel,
                    "linha": n, "trecho": mascarar(bruto)[:220], "nota": nota,
                })
        except re.error:
            continue

    for rx in ROTAS:
        try:
            for m in re.finditer(rx, texto):
                n = texto.count("\n", 0, m.start()) + 1
                g = [x for x in m.groups() if x]
                rotas.append({
                    "arquivo": rel, "linha": n,
                    "metodo": (g[0] if g else "?").upper(),
                    "caminho": g[1] if len(g) > 1 else "",
                })
        except re.error:
            continue

    return candidatos, rotas


def mascarar(s: str) -> str:
    """Nunca deixa valor de segredo vazar para o JSON de auditoria."""
    s = re.sub(r'(ghp_|gho_|github_pat_|sk-|xox[baprs]-|AKIA|AIza)[A-Za-z0-9_\-]{6,}',
               r'\1****', s)
    s = re.sub(r'''(?i)\b(api[_-]?key|apikey|secret|token|passwd|password|senha|private[_-]?key|client[_-]?secret)\b(\s*[:=]\s*)(["\']?)([^"\'\s,}]{4,})''',
               lambda m: f"{m.group(1)}{m.group(2)}{m.group(3)}****", s)
    return s


SENSIVEL = re.compile(
    r'(?i)(^|/)(\.env(\.[\w.-]+)?|.*\.pem|.*\.key|.*\.p12|.*\.pfx|id_rsa|id_ed25519'
    r'|credentials(\.json)?|secrets?\.(ya?ml|json)|\.npmrc|\.pypirc|.*\.jks)$')


def classificar_arquivos_sensiveis(raiz: Path) -> dict:
    """
    Distingue tres situacoes que exigem respostas MUITO diferentes:

      rastreado  - versionado agora. Vazamento ativo. Critico.
      no_historico - removido do HEAD, vivo no historico. Exige rotacao E limpeza.
      apenas_local - existe em disco, nunca commitado. Nao e vazamento de repositorio;
                     e superficie local. Severidade bem menor.

    Confundir 'apenas_local' com 'rastreado' e o erro classico da auditoria apressada:
    inflaciona para critico algo que o .gitignore ja resolveu.
    """
    out = {"rastreados": [], "no_historico": [], "apenas_local": []}
    try:
        r = subprocess.run(["git", "ls-files"], cwd=raiz, capture_output=True,
                           text=True, errors="ignore", timeout=60)
        if r.returncode != 0:
            return out
        rastreados = set(r.stdout.splitlines())
        out["rastreados"] = sorted(f for f in rastreados if SENSIVEL.search(f))[:50]

        h = subprocess.run(["git", "log", "--all", "--name-only", "--pretty=format:", "-500"],
                           cwd=raiz, capture_output=True, text=True,
                           errors="ignore", timeout=120)
        hist = {l.strip() for l in h.stdout.splitlines() if l.strip()}
        out["no_historico"] = sorted(
            f for f in hist if SENSIVEL.search(f) and f not in rastreados)[:50]

        for p in caminhar(raiz):
            rel = p.relative_to(raiz).as_posix()
            if SENSIVEL.search(rel) and rel not in rastreados and rel not in hist:
                out["apenas_local"].append(rel)
        out["apenas_local"] = sorted(out["apenas_local"])[:50]
    except Exception as e:
        out["erro"] = str(e)
    return out


def varrer_historico_git(raiz: Path) -> dict:
    res = {"disponivel": False, "commits_com_segredo": [], "arquivos_sensiveis": []}
    try:
        chk = subprocess.run(["git", "rev-parse", "--is-inside-work-tree"],
                             cwd=raiz, capture_output=True, text=True, timeout=15)
        if chk.returncode != 0:
            return res
        res["disponivel"] = True

        alvo = re.compile(
            r'(?i)^\+.*\b(password|passwd|senha|secret|api[_-]?key|token|private[_-]?key)\b\s*[:=]\s*\S{6,}')
        proc = subprocess.run(["git", "log", "-p", "--all", "--no-color", "-400"],
                              cwd=raiz, capture_output=True, text=True,
                              errors="ignore", timeout=180)
        commit = None
        vistos = set()
        for linha in proc.stdout.splitlines():
            if linha.startswith("commit "):
                commit = linha.split()[1][:10]
            elif alvo.match(linha):
                chave = (commit, mascarar(linha.strip())[:150])
                if chave in vistos:
                    continue
                vistos.add(chave)
                res["commits_com_segredo"].append(
                    {"commit": commit, "trecho": mascarar(linha.strip())[:150]})
                if len(res["commits_com_segredo"]) >= 60:
                    break

        res["arquivos_sensiveis"] = classificar_arquivos_sensiveis(raiz)
    except Exception as e:
        res["erro"] = str(e)
    return res


def libs_sanitizacao(raiz: Path) -> list:
    alvo = ["dompurify", "sanitize-html", "xss", "bleach", "sanitize_html",
            "html-sanitizer", "loofah", "htmlpurifier", "bluemonday"]
    achou = []
    for arq in ("package.json", "requirements.txt", "pyproject.toml",
                "composer.json", "Gemfile", "go.mod"):
        t = _ler(raiz / arq).lower()
        achou += [a for a in alvo if a in t]
    return sorted(set(achou))


def main() -> int:
    ap = argparse.ArgumentParser(description="Coletor de candidatos de seguranca")
    ap.add_argument("--raiz", default=".")
    ap.add_argument("--saida", default=".auditoria/candidatos.json")
    ap.add_argument("--so-stack", action="store_true")
    args = ap.parse_args()

    raiz = Path(args.raiz).resolve()
    if not raiz.is_dir():
        print(f"[!] Raiz inexistente: {raiz}")
        return 1

    stack = detectar_stack(raiz)

    if args.so_stack:
        print(json.dumps(stack, ensure_ascii=False, indent=2))
        return 0

    candidatos, rotas, n_arq = [], [], 0
    for p in caminhar(raiz):
        n_arq += 1
        c, r = varrer_arquivo(p, raiz)
        candidatos += c
        rotas += r

    por_cat = {}
    for c in candidatos:
        por_cat.setdefault(c["categoria"], []).append(c)

    saida = {
        "raiz": str(raiz),
        "arquivos_varridos": n_arq,
        "stack": stack,
        "libs_sanitizacao": libs_sanitizacao(raiz),
        "historico_git": varrer_historico_git(raiz),
        "inventario_rotas": rotas,
        "total_candidatos": len(candidatos),
        "candidatos_por_categoria": {k: len(v) for k, v in por_cat.items()},
        "candidatos": por_cat,
        "aviso": "CANDIDATOS, NAO ACHADOS. Abra cada arquivo e triage antes de reportar.",
    }

    dest = Path(args.saida)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(saida, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"[ok] {n_arq} arquivos varridos -> {dest}")
    print(f"[ok] Linguagens: {', '.join(stack['linguagens']) or 'indeterminada'}")
    print(f"[ok] Framework: {stack['framework'] or 'nenhum'} | ORM: {stack['orm'] or 'nenhum'} | Auth: {stack['auth'] or 'nenhuma'}")
    print(f"[ok] Frontend: {stack['frontend'] or 'nenhum'} | Rotas no inventario: {len(rotas)}")
    print(f"[ok] Sanitizacao: {', '.join(saida['libs_sanitizacao']) or 'NENHUMA LIB DETECTADA'}")
    hg = saida["historico_git"]
    if hg.get("disponivel"):
        sens = hg.get("arquivos_sensiveis") or {}
        print(f"[ok] Historico git: {len(hg['commits_com_segredo'])} linhas suspeitas")
        print(f"     arquivos sensiveis -> rastreados: {len(sens.get('rastreados', []))}"
              f" | no historico: {len(sens.get('no_historico', []))}"
              f" | apenas locais: {len(sens.get('apenas_local', []))}")
        if sens.get("rastreados"):
            print(f"     [CRITICO] versionados agora: {', '.join(sens['rastreados'][:5])}")
        if sens.get("no_historico"):
            print(f"     [CRITICO] vivos no historico: {', '.join(sens['no_historico'][:5])}")
        if sens.get("apenas_local"):
            print(f"     [info] so em disco, nunca commitados: {', '.join(sens['apenas_local'][:5])}")
    print(f"[ok] Candidatos: {saida['candidatos_por_categoria']}")
    print("[!] Candidatos nao sao achados. Triage lendo o codigo.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
