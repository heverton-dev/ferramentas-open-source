# -*- coding: utf-8 -*-
"""
GATE DE SEGREDOS NO COMMIT (R15 + R9)

Varre o diff staged e aborta o commit se encontrar credencial. Verifica so o que esta
sendo adicionado: o que ja esta no historico exige rotacao, nao bloqueio de commit.

Uso:
    python scripts/verificar_segredos.py            # diff staged (usado pelo hook)
    python scripts/verificar_segredos.py --arquivo X  # arquivo avulso

Exit 0 = limpo. Exit 1 = segredo encontrado.
"""
import argparse
import re
import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Alta confianca: o formato do proprio valor identifica o segredo. NAO sofrem isencao —
# uma chave AWS bem formada continua sendo chave mesmo contendo a palavra "example".
PADROES_FORTES = [
    ("token do GitHub",      re.compile(r'\b(ghp_|gho_|ghs_|github_pat_)[A-Za-z0-9_]{20,}')),
    ("chave da OpenAI",      re.compile(r'\bsk-[A-Za-z0-9]{20,}')),
    ("token do Slack",       re.compile(r'\bxox[baprs]-[A-Za-z0-9-]{10,}')),
    ("chave de acesso AWS",  re.compile(r'\bAKIA[0-9A-Z]{16}\b')),
    ("chave da Google API",  re.compile(r'\bAIza[0-9A-Za-z_\-]{35}\b')),
    ("chave privada",        re.compile(r'-----BEGIN (RSA |EC |OPENSSH |PGP |DSA )?PRIVATE KEY-----')),
]

# Heuristico: depende do contexto, entao respeita as isencoes.
# Sem \b inicial de proposito: em DB_PASSWORD o underscore e word char, e \b nao casa
# entre "_" e "P" — o que deixaria passar justamente o nome de variavel mais comum.
PADROES_FRACOS = [
    # Valor ENTRE ASPAS
    ("senha atribuida", re.compile(
        r'(?i)[\w.-]*(password|passwd|senha|secret|api[_-]?key|access[_-]?token|token)'
        r'\s*[:=]\s*["\'][^"\'$\{][^"\']{7,}["\']')),
    # Valor SEM ASPAS — formato dominante em docker-compose, YAML, .env e `docker -e`.
    # Exigir aspas deixava passar justamente onde a credencial mais aparece:
    #     POSTGRES_PASSWORD: SenhaLiteral
    #     - KEYCLOAK_ADMIN_PASSWORD=SenhaLiteral
    #     docker run -e MYSQL_ROOT_PASSWORD=SenhaLiteral
    ("senha atribuida (sem aspas)", re.compile(
        r'(?i)(?:^|[\s\-=])[\w.-]*(password|passwd|senha|secret|api[_-]?key|'
        r'access[_-]?token|token)\s*[:=]\s*(?![\s"\'])(?![$<{])[^\s"\'#,;)]{7,}')),
]

PADROES = PADROES_FORTES + PADROES_FRACOS

# Contextos que legitimamente contem a palavra sem conter o segredo.
# Aplicam-se apenas aos padroes heuristicos.
ISENCOES = [
    re.compile(r'(?i)\$\{[A-Z_]+\}'),                 # ${VAR}
    re.compile(r'(?i)\{\{[^}]+\}\}'),                 # {{ vault_secret }}
    re.compile(r'(?i)(os\.environ|process\.env|getenv|System\.getenv)'),
    re.compile(r'(?i)=\s*["\']?(\*{3,}|x{4,}|<[^>]+>|\.\.\.)["\']?\s*$'),
    re.compile(r'(?i)(placeholder|dummy|redacted|mascarado|<seu-|<your-)'),
    re.compile(r'(?i)["\'](exemplo|example|changeme|troque|xxx+)["\']\s*$'),
    re.compile(r'<COLE-AQUI-'),                       # marcador dos manuais
    # Placeholder escrito em portugues, em qualquer posicao da linha. Cobre
    # "senha_da_equipe", "SuaChaveAPI", "seu-token-aqui", "sua_chave".
    # Sem isto o gate acusa o material didatico inteiro — e gate que grita a toa
    # e desligado com --no-verify na primeira semana.
    re.compile(r'(?i)\b(su[ao]|seu|tua?)[-_ ]?(chave|senha|token|api|valor|dado)'),
    re.compile(r'(?i)(senha|chave|token)[-_](da|do|de|aqui|exemplo)\b'),
    # Atribuicao a partir de leitura de configuracao, nao literal:
    #   self.password = self._clean_val(linha.split('=')[1])
    re.compile(r'(?i)[:=]\s*(self\.|this\.|cfg\.|config\.|_?clean|_?load|_?read|'
               r'\w+\.(get|split|strip|read)\()'),
    # Subcomando de CLI que contem "key"/"token": `shlink api-key:generate`
    re.compile(r'(?i)\b(api-?key|token)[:\s]+(generate|create|list|show|revoke|new)\b'),
    # Palavra generica em portugues usada como valor ilustrativo. Um segredo real
    # nao e a traducao do proprio nome do campo.
    # ["\\x27] em vez de aspas literais: este bloco vive dentro do template do script
    # de correcao, e aspas aninhadas quebrariam a geracao do arquivo.
    re.compile(r'(?i)[:=]\s*["\x27]?(secreta|secreto|minhasenha|senhaforte'
               r'|chavesecreta|meutoken|umasenha|qualquer|123456\d*)["\x27]?(\s|$|[,;)}])'),
]

# .env.example / .env.sample / .env.template SAO para versionar — e o mecanismo que
# documenta as chaves sem os valores. Bloquea-los empurra o time a usar --no-verify,
# e a partir dai o gate nao protege mais nada.
ENV_MODELO = re.compile(r'(?i)\.env\.(example|sample|template|dist|model)$')

ARQUIVOS_PROIBIDOS = re.compile(
    r'(?i)(^|/)(\.env(\.[\w.-]+)?|.*\.pem|.*\.key|.*\.p12|.*\.pfx|id_rsa|id_ed25519)$')


def arquivo_proibido(nome: str) -> bool:
    if ENV_MODELO.search(nome):
        return False
    return bool(ARQUIVOS_PROIBIDOS.search(nome))


# O proprio verificador cita formatos de segredo por definicao. Sem esta isencao ele
# bloqueia o commit de si mesmo.
AUTO_ISENTOS = {"scripts/verificar_segredos.py"}

# Binarios nao sao varridos: bytes comprimidos produzem sequencias que casam com
# qualquer regex por acaso. Um PDF de relatorio de seguranca dispara o alarme
# justamente por CITAR os formatos de segredo — falso positivo garantido, e gate que
# grita a toa acaba desligado com --no-verify.
BINARIOS = re.compile(
    r'(?i)\.(pdf|png|jpe?g|gif|webp|ico|svgz|zip|gz|tar|7z|rar|xz|bz2|db|sqlite3?|'
    r'woff2?|ttf|eot|otf|mp[34]|wav|avi|mov|mkv|exe|dll|so|dylib|bin|dat|pyc|pyo|'
    r'class|jar|wasm|docx|xlsx|pptx|odt|ods)$')


def _isento(linha: str) -> bool:
    return any(p.search(linha) for p in ISENCOES)


def verificar_texto(texto: str, origem: str) -> list:
    achados = []
    for n, linha in enumerate(texto.splitlines(), 1):
        if len(linha) > 800:
            continue
        # Padroes fortes ignoram isencao: o formato do valor ja e prova suficiente.
        for rotulo, rx in PADROES_FORTES:
            if rx.search(linha):
                achados.append((origem, n, rotulo))
                break
        else:
            if _isento(linha):
                continue
            for rotulo, rx in PADROES_FRACOS:
                if rx.search(linha):
                    achados.append((origem, n, rotulo))
                    break
    return achados


def verificar_staged() -> list:
    achados = []
    nomes = subprocess.run(["git", "diff", "--cached", "--name-only", "--diff-filter=ACM"],
                           cwd=BASE_DIR, capture_output=True, text=True, errors="ignore")
    for nome in [x.strip() for x in nomes.stdout.splitlines() if x.strip()]:
        if nome.replace("\\", "/") in AUTO_ISENTOS or BINARIOS.search(nome):
            continue
        if arquivo_proibido(nome):
            achados.append((nome, 0, "arquivo sensivel nao deve ser versionado"))
            continue
        d = subprocess.run(["git", "diff", "--cached", "-U0", "--", nome],
                           cwd=BASE_DIR, capture_output=True, text=True, errors="ignore")
        adicionadas = "\n".join(
            l[1:] for l in d.stdout.splitlines()
            if l.startswith("+") and not l.startswith("+++"))
        achados += verificar_texto(adicionadas, nome)
    return achados


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--arquivo")
    args = ap.parse_args()

    if args.arquivo:
        p = Path(args.arquivo)
        if not p.is_file():
            print(f"[!] Arquivo inexistente: {p}")
            return 1
        achados = verificar_texto(p.read_text(encoding="utf-8", errors="ignore"), str(p))
    else:
        achados = verificar_staged()

    if not achados:
        return 0

    print("=" * 68)
    print(" COMMIT BLOQUEADO: possivel credencial no conteudo adicionado")
    print("=" * 68)
    for arq, linha, rotulo in achados:
        local = f"{arq}:{linha}" if linha else arq
        print(f"  [!] {local} -> {rotulo}")
    print("-" * 68)
    print(" Mova o valor para .env (ignorado pelo git) e referencie por variavel.")
    print(" Falso positivo? Use ${VAR} ou os.environ no lugar do literal.")
    print("=" * 68)
    return 1


if __name__ == "__main__":
    sys.exit(main())
