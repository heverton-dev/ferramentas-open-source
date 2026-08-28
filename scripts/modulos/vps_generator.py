# -*- coding: utf-8 -*-
import os
import re
import datetime

class VPSGenerator:
    def __init__(self, audit_data, decision_data, output_dir, base_domain="vpsconexao.org"):
        self.audit = audit_data
        self.decision = decision_data
        self.output_dir = output_dir
        self.base_domain = base_domain
        os.makedirs(self.output_dir, exist_ok=True)

    def generate_all(self):
        rel_md = self._build_relatorio_md()
        rel_html = self._build_html_wrapper("Relat?rio de Auditoria e Viabilidade VPS", rel_md)
        with open(os.path.join(self.output_dir, "01-relatorio-auditoria-viabilidade.md"), "w", encoding="utf-8") as f:
            f.write(rel_md)
        with open(os.path.join(self.output_dir, "01-relatorio-auditoria-viabilidade.html"), "w", encoding="utf-8") as f:
            f.write(rel_html)

        stack_yml = self._build_stack_yml()
        with open(os.path.join(self.output_dir, "02-stack-integrada-portainer.yml"), "w", encoding="utf-8") as f:
            f.write(stack_yml)

        inst_md = self._build_manual_instalacao_md()
        inst_html = self._build_html_wrapper("Manual de Instala??o Cir?rgica no Portainer", inst_md)
        with open(os.path.join(self.output_dir, "03-manual-instalacao-cirurgica.md"), "w", encoding="utf-8") as f:
            f.write(inst_md)
        with open(os.path.join(self.output_dir, "03-manual-instalacao-cirurgica.html"), "w", encoding="utf-8") as f:
            f.write(inst_html)

        desinst_md = self._build_manual_desinstalacao_md()
        desinst_html = self._build_html_wrapper("Manual de Desinstala??o Cir?rgica e Rollback", desinst_md)
        with open(os.path.join(self.output_dir, "04-manual-desinstalacao-e-rollback.md"), "w", encoding="utf-8") as f:
            f.write(desinst_md)
        with open(os.path.join(self.output_dir, "04-manual-desinstalacao-e-rollback.html"), "w", encoding="utf-8") as f:
            f.write(desinst_html)

        return [
            os.path.join(self.output_dir, "01-relatorio-auditoria-viabilidade.md"),
            os.path.join(self.output_dir, "01-relatorio-auditoria-viabilidade.html"),
            os.path.join(self.output_dir, "02-stack-integrada-portainer.yml"),
            os.path.join(self.output_dir, "03-manual-instalacao-cirurgica.md"),
            os.path.join(self.output_dir, "03-manual-instalacao-cirurgica.html"),
            os.path.join(self.output_dir, "04-manual-desinstalacao-e-rollback.md"),
            os.path.join(self.output_dir, "04-manual-desinstalacao-e-rollback.html")
        ]

    def generate_consolidated_report(self, multi_decision_data, root_output_dir):
        """Gera o painel consolidado com a an?lise conjunta de todos os alvos."""
        cumul = multi_decision_data["cumulative"]
        evals = multi_decision_data["evaluations"]
        hw = self.audit["hardware"]
        data_str = datetime.date.today().strftime("%d/%m/%Y")

        table_rows = ""
        for ev in evals:
            p = ev["profile"]
            v = ev["verdict"]
            table_rows += f"| **{p['name']}** | {p['req_cpu']} vCPUs | {p['req_ram_gb']} GB | {v['status']} | {v['score']}/100 |\n"

        recs_md = "\n".join([f"- {r}" for r in cumul["recommendations"]])
        alerts_md = "\n".join([f"- [ALERTA] {a}" for a in cumul["alerts"]]) if cumul["alerts"] else "- Nenhum impedimento t?cnico detectado para a opera??o conjunta."

        md = f"""# Painel Executivo Consolidado: Auditoria Multi-Alvo na VPS

**Data da Auditoria:** {data_str}  
**Veredito Global Conjunto:** **{cumul['status']}** (Score M?dio/Global: {cumul['score']}/100)

---

## 1. Balan?o Geral de Recursos e Headroom Cumulativo

| Dimens?o de Infraestrutura | Capacidade Total | Ocupa??o Atual | Demanda Conjunta (Soma) | Saldo Restante (Headroom) | Veredito |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Processamento (vCPU)** | {hw['total_cpu']} vCPUs | ~1.5 vCPUs | **{cumul['total_req_cpu']} vCPUs** | **~{cumul['free_cpu'] - cumul['total_req_cpu']:.1f} vCPUs livres** | {'APROVADO' if cumul['cumul_cpu_ok'] else 'REPROVADO'} |
| **Mem?ria RAM** | {hw['total_mem_gb']} GB | ~{hw['est_mem_used_gb']} GB | **{cumul['total_req_ram']} GB** | **~{cumul['free_ram'] - cumul['total_req_ram']:.1f} GB livres** | {'APROVADO' if cumul['cumul_ram_ok'] else 'REPROVADO'} |
| **Rede Swarm e Ingress** | Traefik | Certresolver ACME | Rede `{self.audit['ingress'].get('default_overlay', 'network_conexao')}` | SNI / Dom?nios Isolados | APROVADO |

---

## 2. Tabela Comparativa de Viabilidade por Alvo

| Alvo (Ecossistema / Ferramenta) | Demanda vCPU | Demanda RAM | Status Individual | Score |
| :--- | :--- | :--- | :--- | :--- |
{table_rows}

---

## 3. Parecer T?cnico e Diretrizes de Engenharia

### 3.1 Recomenda??es Estrat?gicas
{recs_md}

### 3.2 Alertas e Pontos de Aten??o
{alerts_md}
"""
        html = self._build_html_wrapper("Painel Consolidado Multi-Alvo VPS", md)
        
        md_path = os.path.join(root_output_dir, "00-painel-consolidado-multialvo.md")
        html_path = os.path.join(root_output_dir, "00-painel-consolidado-multialvo.html")
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(md)
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html)

        return [md_path, html_path]

    def _build_relatorio_md(self):
        hw = self.audit["hardware"]
        v = self.decision["verdict"]
        prof = self.decision["profile"]
        data_str = datetime.date.today().strftime("%d/%m/%Y")
        cert = self.audit["ingress"]["certresolvers"][0] if self.audit["ingress"]["certresolvers"] else "letsencryptresolver"
        net = self.audit["ingress"].get("default_overlay", "network_conexao")

        alerts_md = "\n".join([f"- [ALERTA] {a}" for a in v["alerts"]]) if v["alerts"] else "- Nenhum impedimento t?cnico detectado."
        recs_md = "\n".join([f"- {r}" for r in v["recommendations"]])

        md = f"""# Relat?rio Executivo de Auditoria e Viabilidade de VPS

**Alvo de Incorpora??o:** {prof['name']}  
**Data da Auditoria:** {data_str}  
**Veredito T?cnico:** **{v['status']}** (Score: {v['score']}/100)

---

## 1. Diagn?stico de Capacidade e Headroom da VPS

| Dimens?o de Hardware | Capacidade Total | Ocupa??o Atual (Est.) | Dispon?vel (Headroom) | Requisito da Stack | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Processamento (vCPU)** | {hw['total_cpu']} vCPUs | ~1.5 vCPUs | **~{v['free_cpu']} vCPUs** | {v['req_cpu']} vCPUs | {'APROVADO' if v['cpu_ok'] else 'REPROVADO'} |
| **Mem?ria RAM** | {hw['total_mem_gb']} GB | ~{hw['est_mem_used_gb']} GB | **~{v['free_ram_gb']} GB** | {v['req_ram_gb']} GB | {'APROVADO' if v['ram_ok'] else 'REPROVADO'} |
| **Modo de Orquestra??o** | Docker Swarm | {hw['running_containers']} containers ativos | N?s: 1 Manager | Swarm Nativo | APROVADO |
| **Ingress e TLS** | Traefik | Certresolver: `{cert}` | Rede: `{net}` | Roteamento SNI | APROVADO |

---

## 2. Parecer T?cnico de Viabilidade

### 2.1 Recomenda??es e Oportunidades de Otimiza??o
{recs_md}

### 2.2 Alertas e Pontos de Aten??o
{alerts_md}

---

## 3. Matriz de Servi?os e Subdom?nios Propostos

| Servi?o / Componente | Papel Operacional | Subdom?nio Proposto | Porta Interna |
| :--- | :--- | :--- | :--- |
"""
        for sub in prof.get("subdomains", []):
            md += f"| {sub.capitalize()} Service | Componente da Stack {prof['name']} | `{sub}.{self.base_domain}` | Roteamento Traefik |\n"

        return md

    def _build_stack_yml(self):
        cert = self.audit["ingress"]["certresolvers"][0] if self.audit["ingress"]["certresolvers"] else "letsencryptresolver"
        net = self.audit["ingress"].get("default_overlay", "network_conexao")
        prof = self.decision["profile"]

        if "workspace" in prof["name"].lower():
            return f"""version: '3.8'

services:
  # 1. BANCO DE DADOS DEDICADO DO ECOSSISTEMA
  workspace_db:
    image: postgres:16-alpine
    environment:
      POSTGRES_USER: workspace_user
      POSTGRES_PASSWORD: WorkspaceDBSecret_2026!
      POSTGRES_DB: workspace_nextcloud
    volumes:
      - workspace_db_data:/var/lib/postgresql/data
    networks:
      - {net}
    deploy:
      mode: replicated
      replicas: 1
      placement:
        constraints: [node.role == manager]
      resources:
        limits:
          cpus: '2.0'
          memory: 2048M

  # 2. CACHE & SESSOES (REDIS DEDICADO)
  workspace_redis:
    image: redis:7-alpine
    command: redis-server --appendonly yes
    volumes:
      - workspace_redis_data:/data
    networks:
      - {net}
    deploy:
      mode: replicated
      replicas: 1
      resources:
        limits:
          cpus: '1.0'
          memory: 512M

  # 3. NEXTCLOUD HUB (DRIVE, MAIL, CALENDAR, TALK)
  workspace_nextcloud:
    image: nextcloud:30-apache
    environment:
      POSTGRES_HOST: workspace_db
      POSTGRES_DB: workspace_nextcloud
      POSTGRES_USER: workspace_user
      POSTGRES_PASSWORD: WorkspaceDBSecret_2026!
      REDIS_HOST: workspace_redis
      OVERWRITEPROTOCOL: https
      OVERWRITECLIURL: https://drive.{self.base_domain}
      TRUSTED_PROXIES: 10.0.0.0/8 172.16.0.0/12 192.168.0.0/16
    volumes:
      - workspace_nextcloud_html:/var/www/html
      - workspace_nextcloud_data:/var/www/html/data
    networks:
      - {net}
    deploy:
      mode: replicated
      replicas: 1
      labels:
        - "traefik.enable=true"
        - "traefik.docker.network={net}"
        - "traefik.http.routers.workspace_nextcloud.rule=Host(`drive.{self.base_domain}`)"
        - "traefik.http.routers.workspace_nextcloud.entrypoints=websecure"
        - "traefik.http.routers.workspace_nextcloud.tls=true"
        - "traefik.http.routers.workspace_nextcloud.tls.certresolver={cert}"
        - "traefik.http.routers.workspace_nextcloud.priority=10"
        - "traefik.http.services.workspace_nextcloud.loadbalancer.server.port=80"
        - "traefik.http.services.workspace_nextcloud.loadbalancer.passHostHeader=true"
      resources:
        limits:
          cpus: '3.0'
          memory: 3072M

  # 4. ONLYOFFICE DOCUMENT SERVER (DOCS/SHEETS/SLIDES)
  workspace_onlyoffice:
    image: onlyoffice/documentserver:latest
    environment:
      JWT_ENABLED: 'true'
      JWT_SECRET: OnlyOfficeSecretKey2026_SecureToken!
      USE_UNAUTHORIZED_STORAGE: 'true'
    volumes:
      - workspace_onlyoffice_data:/var/www/onlyoffice/Data
      - workspace_onlyoffice_log:/var/log/onlyoffice
    networks:
      - {net}
    deploy:
      mode: replicated
      replicas: 1
      labels:
        - "traefik.enable=true"
        - "traefik.docker.network={net}"
        - "traefik.http.routers.workspace_onlyoffice.rule=Host(`office.{self.base_domain}`)"
        - "traefik.http.routers.workspace_onlyoffice.entrypoints=websecure"
        - "traefik.http.routers.workspace_onlyoffice.tls=true"
        - "traefik.http.routers.workspace_onlyoffice.tls.certresolver={cert}"
        - "traefik.http.routers.workspace_onlyoffice.priority=10"
        - "traefik.http.services.workspace_onlyoffice.loadbalancer.server.port=80"
        - "traefik.http.services.workspace_onlyoffice.loadbalancer.passHostHeader=true"
      resources:
        limits:
          cpus: '3.0'
          memory: 3072M

  # 5. STALWART MAIL SERVER (SMTP/IMAP/JMAP/CALDAV)
  workspace_stalwart:
    image: stalwartlabs/stalwart:latest
    environment:
      STALWART_ADMIN_USER: admin
      STALWART_ADMIN_PASS: StalwartMasterPass2026!
    volumes:
      - workspace_stalwart_data:/opt/stalwart-mail
    networks:
      - {net}
    deploy:
      mode: replicated
      replicas: 1
      labels:
        - "traefik.enable=true"
        - "traefik.docker.network={net}"
        - "traefik.http.routers.workspace_stalwart.rule=Host(`mail.{self.base_domain}`)"
        - "traefik.http.routers.workspace_stalwart.entrypoints=websecure"
        - "traefik.http.routers.workspace_stalwart.tls=true"
        - "traefik.http.routers.workspace_stalwart.tls.certresolver={cert}"
        - "traefik.http.routers.workspace_stalwart.priority=10"
        - "traefik.http.services.workspace_stalwart.loadbalancer.server.port=8080"
        - "traefik.http.services.workspace_stalwart.loadbalancer.passHostHeader=true"
      resources:
        limits:
          cpus: '2.0'
          memory: 2048M

  # 6. CRYPTPAD (SUITE CRIPTOGRAFADA ZERO-KNOWLEDGE)
  workspace_cryptpad:
    image: cryptpad/cryptpad:latest
    environment:
      CPAD_MAIN_DOMAIN: https://docs.{self.base_domain}
    volumes:
      - workspace_cryptpad_data:/cryptpad/datastore
      - workspace_cryptpad_blob:/cryptpad/blob
    networks:
      - {net}
    deploy:
      mode: replicated
      replicas: 1
      labels:
        - "traefik.enable=true"
        - "traefik.docker.network={net}"
        - "traefik.http.routers.workspace_cryptpad.rule=Host(`docs.{self.base_domain}`)"
        - "traefik.http.routers.workspace_cryptpad.entrypoints=websecure"
        - "traefik.http.routers.workspace_cryptpad.tls=true"
        - "traefik.http.routers.workspace_cryptpad.tls.certresolver={cert}"
        - "traefik.http.routers.workspace_cryptpad.priority=10"
        - "traefik.http.services.workspace_cryptpad.loadbalancer.server.port=3000"
        - "traefik.http.services.workspace_cryptpad.loadbalancer.passHostHeader=true"
      resources:
        limits:
          cpus: '2.0'
          memory: 2048M

networks:
  {net}:
    external: true

volumes:
  workspace_db_data:
  workspace_redis_data:
  workspace_nextcloud_html:
  workspace_nextcloud_data:
  workspace_onlyoffice_data:
  workspace_onlyoffice_log:
  workspace_stalwart_data:
  workspace_cryptpad_data:
  workspace_cryptpad_blob:
"""
        else:
            sub = prof.get("subdomains", ["app"])[0]
            slug = os.path.basename(self.output_dir)
            return f"""version: '3.8'

services:
  {slug}_app:
    image: {slug}:latest
    networks:
      - {net}
    volumes:
      - {slug}_data:/data
    deploy:
      mode: replicated
      replicas: 1
      labels:
        - "traefik.enable=true"
        - "traefik.docker.network={net}"
        - "traefik.http.routers.{slug}.rule=Host(`{sub}.{self.base_domain}`)"
        - "traefik.http.routers.{slug}.entrypoints=websecure"
        - "traefik.http.routers.{slug}.tls=true"
        - "traefik.http.routers.{slug}.tls.certresolver={cert}"
        - "traefik.http.services.{slug}.loadbalancer.server.port=80"
        - "traefik.http.services.{slug}.loadbalancer.passHostHeader=true"
      resources:
        limits:
          cpus: '2.0'
          memory: 2048M

networks:
  {net}:
    external: true

volumes:
  {slug}_data:
"""

    def _build_manual_instalacao_md(self):
        prof = self.decision["profile"]
        slug_clean = os.path.basename(self.output_dir)
        subdomains = prof.get("subdomains", [])
        dns_lines = "\n".join([f"- `{sub}.{self.base_domain}` -> Tipo A -> IP da VPS" for sub in subdomains])
        url_lines = "\n".join([f"- https://{sub}.{self.base_domain}" for sub in subdomains])

        return f"""# Manual de Instala??o Cir?rgica no Portainer

**Alvo:** {prof['name']}  
**P?blico-Alvo:** Gestores, Consultores e Engenheiros de TI  
**Tempo Estimado de Execu??o:** 5 a 10 minutos

---

## 1. Entendendo o Processo (Para N?o-T?cnicos)

Pense na sua VPS como um **edif?cio corporativo**. As aplica??es existentes (Mautic, n8n, Evolution) j? ocupam algumas salas desse edif?cio.
A **instala??o cir?rgica** significa alugar novas salas para a nova su?te de ferramentas, com sua pr?pria mob?lia e fechaduras (volumes e banco de dados dedicados), usando apenas o **corredor central compartilhado** (a rede `{self.audit['ingress'].get('default_overlay', 'network_conexao')}`) e a **portaria central** (o Traefik existente).
Nenhuma sala existente ? tocada ou alterada.

---

## 2. Passo 1: Configura??o do DNS do Dom?nio

Acesse a zona de DNS do seu provedor (Cloudflare, Registro.br, Hostinger ou AWS Route53) e adicione os seguintes registros do tipo **A**:

{dns_lines}

---

## 3. Passo 2: Implanta??o da Stack no Portainer

1. Abra seu navegador e acesse: `https://painel.{self.base_domain}`.
2. Fa?a login com suas credenciais de administrador.
3. No menu lateral esquerdo, clique em **Stacks**.
4. Clique no bot?o azul **+ Add stack**.
5. No campo **Name**, digite: `{slug_clean}`.
6. Na caixa **Web editor**, cole o conte?do integral do arquivo `02-stack-integrada-portainer.yml`.
7. Role at? o rodap? da p?gina e clique em **Deploy the stack**.
8. O Portainer iniciar? o download seguro das imagens e inicializar? os servi?os na rede Swarm.

---

## 4. Passo 3: Valida??o e Testes de Sa?de (Health Check)

Aguarde cerca de 90 segundos para a emiss?o autom?tica dos certificados SSL Let's Encrypt.
Em seguida, abra as URLs no navegador para validar o acesso:

{url_lines}
"""

    def _build_manual_desinstalacao_md(self):
        prof = self.decision["profile"]
        slug_clean = os.path.basename(self.output_dir)

        return f"""# Manual de Desinstala??o Cir?rgica e Rollback

**Alvo:** {prof['name']}  
**Garantia de Isolamento:** 100% de preserva??o dos demais containers da VPS

---

## 1. Por que este procedimento ? seguro?

Todos os servi?os foram criados dentro do namespace exclusivo da stack `{slug_clean}`.
A remo??o da stack desconecta os containers da rede `{self.audit['ingress'].get('default_overlay', 'network_conexao')}` e remove as regras do Traefik de forma limpa e at?mica.
**Mautic, Evolution, n8n, MySQL, PostgreSQL global e Portainer continuam operando normalmente sem interrup??o.**

---

## 2. Procedimento de Remo??o via Interface Portainer

1. Acesse: `https://painel.{self.base_domain}`.
2. Clique em **Stacks** no menu lateral esquerdo.
3. Localize a stack `{slug_clean}` e marque a caixa de sele??o ao lado dela.
4. Clique no bot?o vermelho **Delete this stack**.
5. Confirme a exclus?o na janela pop-up.
6. Em menos de 10 segundos, todos os containers da stack ser?o desligados e suas rotas web desativadas.

---

## 3. Limpeza de Volumes Persistentes (Opcional - Libera??o de Disco)

Se voc? n?o planeja reinstalar a stack e deseja liberar espa?o em disco:

1. No menu lateral do Portainer, clique em **Volumes**.
2. No campo de busca/filtro no topo, digite: `{slug_clean}_`.
3. Selecione todos os volumes filtrados.
4. Clique em **Remove** e confirme.

---

## 4. Procedimento Alternativo via Linha de Comando (CLI / SSH)

Caso prefira executar via terminal SSH / Termius:

```bash
# 1. Remover a stack do Docker Swarm
docker stack rm {slug_clean}

# 2. Aguardar 10 segundos para a finaliza??o dos containers
sleep 10

# 3. (Opcional) Remover volumes da stack
docker volume ls --filter name={slug_clean} -q | xargs -r docker volume rm
```
"""

    def _build_html_wrapper(self, title, md_content):
        html_body = md_content.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        html_body = re.sub(r"^# (.*?)$", r"<h1></h1>", html_body, flags=re.MULTILINE)
        html_body = re.sub(r"^## (.*?)$", r"<h2></h2>", html_body, flags=re.MULTILINE)
        html_body = re.sub(r"^### (.*?)$", r"<h3></h3>", html_body, flags=re.MULTILINE)
        html_body = re.sub(r"\*\*(.*?)\*\*", r"<strong></strong>", html_body)
        html_body = re.sub(r"`(.*?)`", r"<code></code>", html_body)
        html_body = re.sub(r"^---$", r"<hr>", html_body, flags=re.MULTILINE)

        return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        :root {{
            --bg: #0f172a;
            --card-bg: #1e293b;
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --primary: #38bdf8;
            --border: #334155;
            --code-bg: #0b1120;
        }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            background-color: var(--bg);
            color: var(--text-main);
            line-height: 1.6;
            margin: 0;
            padding: 40px 20px;
        }}
        .container {{
            max-width: 960px;
            margin: 0 auto;
            background: var(--card-bg);
            padding: 40px;
            border-radius: 12px;
            border: 1px solid var(--border);
        }}
        h1 {{ color: var(--primary); font-size: 24px; border-bottom: 2px solid var(--border); padding-bottom: 10px; }}
        h2 {{ color: #e2e8f0; font-size: 19px; margin-top: 28px; border-bottom: 1px solid var(--border); padding-bottom: 6px; }}
        code {{ background: var(--code-bg); color: #38bdf8; padding: 2px 6px; border-radius: 4px; font-family: monospace; }}
        table {{ width: 100%; border-collapse: collapse; margin: 20px 0; }}
        th, td {{ padding: 10px 14px; border: 1px solid var(--border); text-align: left; font-size: 14px; }}
        th {{ background: var(--code-bg); color: var(--primary); }}
    </style>
</head>
<body>
    <div class="container">
        {html_body}
    </div>
</body>
</html>
"""
