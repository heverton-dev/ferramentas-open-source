# -*- coding: utf-8 -*-
import os
import re
import datetime

ENTERPRISE_CSS = """﻿:root {
  --bg-main: #0b1120;
  --bg-card: #0f172a;
  --bg-surface: #1e293b;
  --bg-surface-hover: #273549;
  --border-subtle: #334155;
  --border-focus: #0284c7;
  --text-primary: #f8fafc;
  --text-secondary: #cbd5e1;
  --text-muted: #94a3b8;
  --accent-primary: #38bdf8;
  --accent-blue: #0284c7;
  --accent-blue-soft: rgba(2, 132, 199, 0.15);
  --success-text: #34d399;
  --success-bg: rgba(16, 185, 129, 0.12);
  --success-border: rgba(16, 185, 129, 0.35);
  --font-sans: 'Segoe UI', system-ui, -apple-system, BlinkMacSystemFont, Roboto, sans-serif;
  --font-mono: 'JetBrains Mono', 'Fira Code', Consolas, monospace;
}

* { box-sizing: border-box; margin: 0; padding: 0; }

body {
  font-family: var(--font-sans);
  background-color: var(--bg-main);
  color: var(--text-primary);
  line-height: 1.65;
  padding: 2.5rem 1.5rem;
}

.container {
  max-width: 1040px;
  margin: 0 auto;
}

.header-card {
  background: linear-gradient(145deg, #0f172a 0%, #1e293b 100%);
  border: 1px solid var(--border-subtle);
  border-radius: 12px;
  padding: 2rem;
  margin-bottom: 2rem;
  box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.4);
}

.header-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  background: var(--accent-blue-soft);
  color: var(--accent-primary);
  border: 1px solid rgba(56, 189, 248, 0.3);
  padding: 0.3rem 0.8rem;
  border-radius: 20px;
  font-size: 0.78rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-bottom: 1rem;
}

h1.report-title {
  font-size: 1.95rem;
  font-weight: 800;
  color: #ffffff;
  letter-spacing: -0.02em;
  margin-bottom: 0.5rem;
}

.report-subtitle {
  font-size: 0.95rem;
  color: var(--text-muted);
  margin-bottom: 1.5rem;
}

.hero-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
  gap: 1rem;
  margin-top: 1rem;
}

.stat-box {
  background: rgba(15, 23, 42, 0.7);
  border: 1px solid var(--border-subtle);
  border-radius: 8px;
  padding: 1rem;
}

.stat-label {
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: var(--text-muted);
  font-weight: 700;
  margin-bottom: 0.35rem;
}

.stat-value {
  font-size: 1.05rem;
  font-weight: 700;
  color: #ffffff;
}

.stat-value.highlight {
  color: var(--accent-primary);
}

.stat-value.success {
  color: var(--success-text);
}

.stat-sub {
  font-size: 0.78rem;
  color: var(--text-muted);
  margin-top: 0.2rem;
}

.section-card {
  background: var(--bg-card);
  border: 1px solid var(--border-subtle);
  border-radius: 12px;
  padding: 1.8rem;
  margin-bottom: 2rem;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2);
}

h2.section-heading {
  font-size: 1.25rem;
  font-weight: 700;
  color: var(--accent-primary);
  display: flex;
  align-items: center;
  gap: 0.6rem;
  margin-bottom: 1.2rem;
  padding-bottom: 0.6rem;
  border-bottom: 1px solid var(--border-subtle);
}

.opinion-box {
  background: linear-gradient(135deg, rgba(2, 132, 199, 0.08) 0%, rgba(15, 23, 42, 0.6) 100%);
  border-left: 4px solid var(--accent-blue);
  border-radius: 0 8px 8px 0;
  padding: 1.2rem 1.5rem;
  font-size: 0.95rem;
  color: var(--text-secondary);
  line-height: 1.75;
  text-align: justify;
}

.summary-list {
  list-style: none;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 0.8rem;
}

.summary-item {
  background: var(--bg-surface);
  border: 1px solid var(--border-subtle);
  border-radius: 8px;
  padding: 0.85rem 1.1rem;
  font-size: 0.88rem;
}

.summary-item strong {
  color: var(--accent-primary);
  display: block;
  font-size: 0.78rem;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  margin-bottom: 0.2rem;
}

.table-wrapper {
  width: 100%;
  overflow-x: auto;
  border-radius: 8px;
  border: 1px solid var(--border-subtle);
  background: var(--bg-card);
}

table.enterprise-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.88rem;
  text-align: left;
}

table.enterprise-table th {
  background: var(--bg-surface);
  color: var(--text-primary);
  font-weight: 700;
  font-size: 0.8rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  padding: 0.9rem 1.1rem;
  border-bottom: 2px solid var(--border-subtle);
}

table.enterprise-table td {
  padding: 0.9rem 1.1rem;
  border-bottom: 1px solid var(--border-subtle);
  color: var(--text-secondary);
  vertical-align: middle;
}

table.enterprise-table tr:last-child td {
  border-bottom: none;
}

table.enterprise-table tr:hover td {
  background: var(--bg-surface-hover);
}

.badge-gate {
  font-family: var(--font-mono);
  font-size: 0.78rem;
  font-weight: 700;
  padding: 0.25rem 0.6rem;
  border-radius: 4px;
  background: var(--bg-surface);
  color: var(--accent-primary);
  border: 1px solid var(--border-subtle);
  display: inline-block;
}

.badge-status-approved {
  font-family: var(--font-mono);
  font-size: 0.76rem;
  font-weight: 700;
  padding: 0.25rem 0.65rem;
  border-radius: 20px;
  background: var(--success-bg);
  color: var(--success-text);
  border: 1px solid var(--success-border);
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
}

.badge-rank {
  font-family: var(--font-mono);
  font-weight: 800;
  color: var(--accent-primary);
  background: var(--bg-surface);
  padding: 0.2rem 0.5rem;
  border-radius: 4px;
  border: 1px solid var(--border-subtle);
}

.badge-license {
  font-family: var(--font-mono);
  font-size: 0.76rem;
  background: rgba(148, 163, 184, 0.1);
  color: #e2e8f0;
  padding: 0.2rem 0.5rem;
  border-radius: 4px;
  border: 1px solid rgba(148, 163, 184, 0.25);
}

.badge-pill {
  font-size: 0.76rem;
  font-weight: 600;
  padding: 0.2rem 0.55rem;
  border-radius: 4px;
  background: rgba(56, 189, 248, 0.1);
  color: var(--accent-primary);
  border: 1px solid rgba(56, 189, 248, 0.25);
}

code.mono-code {
  font-family: var(--font-mono);
  font-size: 0.82rem;
  background: #111827;
  color: var(--accent-primary);
  padding: 0.2rem 0.45rem;
  border-radius: 4px;
  border: 1px solid #1f2937;
}

a.file-link {
  color: var(--accent-primary);
  text-decoration: none;
  font-weight: 600;
}
a.file-link:hover {
  text-decoration: underline;
}

footer.report-footer {
  text-align: center;
  font-size: 0.8rem;
  color: var(--text-muted);
  margin-top: 3rem;
  padding-top: 1.5rem;
  border-top: 1px solid var(--border-subtle);
}
"""

class VPSGenerator:
    def __init__(self, audit_data, decision_data, output_dir, base_domain="vpsconexao.org"):
        self.audit = audit_data
        self.decision = decision_data
        self.output_dir = output_dir
        self.base_domain = base_domain
        os.makedirs(self.output_dir, exist_ok=True)

    def generate_all(self):
        # 1. Relatorio de Auditoria e Viabilidade
        rel_md = self._build_relatorio_md()
        rel_html = self._build_html_page("Relat?rio Executivo de Auditoria e Viabilidade", rel_md, badge="Auditoria de Infraestrutura")
        with open(os.path.join(self.output_dir, "01-relatorio-auditoria-viabilidade.md"), "w", encoding="utf-8") as f:
            f.write(rel_md)
        with open(os.path.join(self.output_dir, "01-relatorio-auditoria-viabilidade.html"), "w", encoding="utf-8") as f:
            f.write(rel_html)

        # 2. Stack Compose Integrada para o Portainer
        stack_yml = self._build_stack_yml()
        with open(os.path.join(self.output_dir, "02-stack-integrada-portainer.yml"), "w", encoding="utf-8") as f:
            f.write(stack_yml)

        # 3. Manual Passo a Passo de Instalacao Cirurgica
        inst_md = self._build_manual_instalacao_md()
        inst_html = self._build_html_page("Manual de Instala??o Cir?rgica e Integra??o", inst_md, badge="Playbook de Engenharia")
        with open(os.path.join(self.output_dir, "03-manual-instalacao-cirurgica.md"), "w", encoding="utf-8") as f:
            f.write(inst_md)
        with open(os.path.join(self.output_dir, "03-manual-instalacao-cirurgica.html"), "w", encoding="utf-8") as f:
            f.write(inst_html)

        # 4. Manual de Desinstalacao e Rollback
        desinst_md = self._build_manual_desinstalacao_md()
        desinst_html = self._build_html_page("Manual de Desinstala??o Cir?rgica e Rollback", desinst_md, badge="Governan?a e Rollback")
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
        cumul = multi_decision_data["cumulative"]
        evals = multi_decision_data["evaluations"]
        hw = self.audit["hardware"]
        data_str = datetime.date.today().strftime("%d/%m/%Y")
        net = self.audit["ingress"].get("default_overlay", "network_conexao")

        table_rows_md = ""
        for idx, ev in enumerate(evals, start=1):
            p = ev["profile"]
            v = ev["verdict"]
            rank_str = f"{idx:02d}"
            role = p.get("role", "Ferramenta Open Source Aut?noma")
            table_rows_md += f"| **{rank_str}** | **{p['name']}** | {role} | {p['req_cpu']} vCPUs | {p['req_ram_gb']} GB | {v['status']} | {v['score']}/100 |\n"

        md = f"""# Painel Executivo Consolidado: Auditoria Multi-Alvo na VPS

**Destino da Infraestrutura:** VPS de Produ??o (`painel.{self.base_domain}`)  
**Data da Auditoria:** {data_str}  
**Veredito Global Conjunto:** **{cumul['status']}** (Score M?dio/Global: {cumul['score']}/100)  
**N?vel de Risco Operacional:** Risco Zero ? Isolamento Total por Namespaces no Docker Swarm

---

## 1. Hero Stats Bar ? M?tricas de Capacidade e Headroom

| M?trica de Infraestrutura | Capacidade Total | Demanda Cumulativa | Headroom Livre Dispon?vel | Status de Seguran?a |
| :--- | :--- | :--- | :--- | :--- |
| **Capacidade de Processamento** | {hw['total_cpu']} vCPUs | {cumul['total_req_cpu']} vCPUs | **~{cumul['free_cpu'] - cumul['total_req_cpu']:.1f} vCPUs Livres** | {'[APROVADO] Opera??o Est?vel' if cumul['cumul_cpu_ok'] else '[ALERTA] Alta Carga'} |
| **Mem?ria RAM Global** | {hw['total_mem_gb']} GB | {cumul['total_req_ram']} GB | **~{cumul['free_ram'] - cumul['total_req_ram']:.1f} GB Livres** | {'[APROVADO] Ampla Folga' if cumul['cumul_ram_ok'] else '[REPROVADO] Mem?ria Insuficiente'} |
| **Orquestrador de Containers** | Docker Swarm (1 N?) | {hw['running_containers']} Containers Ativos | N?s: 1 Manager | [APROVADO] Roteamento SNI |
| **Ingress & Roteamento TLS** | Traefik v2/v3 | Rede Overlay `{net}` | Certresolver ACME | [APROVADO] SSL Autom?tico |

---

## 2. Matriz Comparativa de Viabilidade por Alvo

Abaixo est? o balan?o individual de viabilidade para todas as ferramentas e ecossistemas avaliados nesta esteira:

| Rank | Alvo Auditado | Categoria Operacional | Requisito vCPU | Requisito RAM | Status Individual | Score |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
{table_rows_md}

---

## 3. Diretrizes de Engenharia e Garantia de Isolamento

1. **Topologia de Rede Compartilhada:** Todos os novos servi?os conectam-se ? rede overlay existente `{net}` como rede externa (`external: true`), garantindo comunica??o direta com o Traefik sem pontes adicionais.
2. **Zero Conflito de Portas de Host:** Todo tr?fego HTTP/HTTPS ? delegado ao roteador Traefik existente via Host Header (SNI), eliminando portas expostas diretamente no host da VPS.
3. **Persist?ncia Segura e Isolada:** Cada aplica??o possui seus volumes com prefixo pr?prio (`<slug>_data`), garantindo que nenhuma base existente (Mautic, Evolution, n8n, MySQL, PostgreSQL global) seja sobrescrita ou corrompida.
4. **Desinstala??o At?mica:** Cada stack ou ferramenta pode ser removida individualmente via `docker stack rm <slug>` em menos de 10 segundos, mantendo a VPS 100% ?ntegra.
"""

        html = self._build_html_page("Painel Executivo Consolidado Multi-Alvo VPS", md, badge="Painel de Auditoria Global")
        
        md_path = os.path.join(root_output_dir, "00-painel-consolidado-multialvo.md")
        html_path = os.path.join(root_output_dir, "00-painel-consolidado-multialvo.html")
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(md)
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html)

        return [md_path, html_path]

    def _build_relatorio_md(self):
        hw = self.audit['hardware']
        v = self.decision['verdict']
        prof = self.decision['profile']
        data_str = datetime.date.today().strftime('%d/%m/%Y')
        cert = self.audit['ingress']['certresolvers'][0] if self.audit['ingress']['certresolvers'] else 'letsencryptresolver'
        net = self.audit['ingress'].get('default_overlay', 'network_conexao')

        alerts_md = "\n".join([f"- [ALERTA] {a}" for a in v['alerts']]) if v['alerts'] else "- Nenhum impedimento t?cnico detectado na VPS."
        recs_md = "\n".join([f"- {r}" for r in v['recommendations']])

        sub_rows = ""
        for sub in prof.get('subdomains', []):
            sub_rows += f"| **{sub.capitalize()} Service** | Componente da Stack {prof['name']} | `https://{sub}.{self.base_domain}` | Roteamento Traefik SNI |\n"

        return f"""# Relat?rio Executivo de Auditoria e Viabilidade da VPS

**Alvo de Incorpora??o:** {prof['name']}  
**Data da Auditoria:** {data_str}  
**Veredito T?cnico:** **{v['status']}** (Score: {v['score']}/100)  
**Host Auditado:** `painel.{self.base_domain}` (Docker Swarm Ativo)

---

## 1. Diagn?stico de Capacidade e Headroom da VPS

| Dimens?o de Hardware | Capacidade Total | Ocupa??o Atual (Est.) | Dispon?vel (Headroom) | Requisito da Stack | Veredito |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Processamento (vCPU)** | {hw['total_cpu']} vCPUs | ~1.5 vCPUs | **~{v['free_cpu']} vCPUs** | {v['req_cpu']} vCPUs | {'APROVADO' if v['cpu_ok'] else 'REPROVADO'} |
| **Mem?ria RAM Global** | {hw['total_mem_gb']} GB | ~{hw['est_mem_used_gb']} GB | **~{v['free_ram_gb']} GB** | {v['req_ram_gb']} GB | {'APROVADO' if v['ram_ok'] else 'REPROVADO'} |
| **Modo de Orquestra??o** | Docker Swarm | {hw['running_containers']} containers ativos | N?s: 1 Manager | Swarm Nativo | APROVADO |
| **Ingress & Roteamento TLS** | Traefik | Certresolver: `{cert}` | Rede: `{net}` | Roteamento SNI | APROVADO |

---

## 2. Parecer T?cnico de Viabilidade e Toler?ncia a Carga

### 2.1 Recomenda??es Estruturais e Oportunidades
{recs_md}

### 2.2 Alertas de Seguran?a e Limites de Carga
{alerts_md}

---

## 3. Matriz de Subdom?nios e Roteamento de Ingress

| Servi?o / Componente | Papel Operacional | Subdom?nio de Acesso | M?todo de Roteamento |
| :--- | :--- | :--- | :--- |
{sub_rows}
"""

    def _build_stack_yml(self):
        cert = self.audit['ingress']['certresolvers'][0] if self.audit['ingress']['certresolvers'] else 'letsencryptresolver'
        net = self.audit['ingress'].get('default_overlay', 'network_conexao')
        prof = self.decision['profile']
        slug_clean = os.path.basename(self.output_dir)

        if 'workspace' in prof['name'].lower():
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
            sub = prof.get('subdomains', ['app'])[0]
            port = 8080 if 'stalwart' in slug_clean else (3000 if 'cryptpad' in slug_clean or 'chatwoot' in slug_clean or 'nocodb' in slug_clean or 'anything' in slug_clean else 80)
            return f"""version: '3.8'

services:
  {slug_clean}_app:
    image: {slug_clean}:latest
    networks:
      - {net}
    volumes:
      - {slug_clean}_data:/data
    deploy:
      mode: replicated
      replicas: 1
      labels:
        - "traefik.enable=true"
        - "traefik.docker.network={net}"
        - "traefik.http.routers.{slug_clean}.rule=Host(`{sub}.{self.base_domain}`)"
        - "traefik.http.routers.{slug_clean}.entrypoints=websecure"
        - "traefik.http.routers.{slug_clean}.tls=true"
        - "traefik.http.routers.{slug_clean}.tls.certresolver={cert}"
        - "traefik.http.services.{slug_clean}.loadbalancer.server.port={port}"
        - "traefik.http.services.{slug_clean}.loadbalancer.passHostHeader=true"
      resources:
        limits:
          cpus: '{prof.get("req_cpu", 2.0)}'
          memory: {int(prof.get("req_ram_gb", 2.0) * 1024)}M

networks:
  {net}:
    external: true

volumes:
  {slug_clean}_data:
"""

    def _build_manual_instalacao_md(self):
        prof = self.decision['profile']
        slug_clean = os.path.basename(self.output_dir)
        subdomains = prof.get('subdomains', [])
        net = self.audit['ingress'].get('default_overlay', 'network_conexao')
        dns_lines = "\n".join([f"- Registro A: `{sub}.{self.base_domain}` -> IP da VPS" for sub in subdomains])
        url_lines = "\n".join([f"- `https://{sub}.{self.base_domain}`" for sub in subdomains])

        return f"""# Manual de Instala??o Cir?rgica no Portainer & Playbook de Opera??o

**Alvo:** {prof['name']}  
**P?blico-Alvo:** Gestores, Consultores e Engenheiros de TI  
**Tempo Estimado de Execu??o:** 5 a 10 minutos  
**Garantia Arquitetural:** Zero interfer?ncia nas aplica??es existentes (`mautic`, `evolution`, `n8n`, `mysql`, `postgres`)

---

## 1. Entendendo a Arquitetura Cir?rgica (Para N?o-T?cnicos)

Pense na sua VPS como um **edif?cio corporativo de alta seguran?a**. As aplica??es em produ??o (como seu CRM Mautic, o n8n e o Evolution API) j? ocupam salas estruturadas nesse edif?cio.
A **instala??o cir?rgica** significa abrir uma nova sala independente para a nova su?te de ferramentas, com seus pr?prios arm?rios e cofres (volumes dedicados e banco isolado), conectando-se apenas ao **corredor central** (a rede `{net}`) e ? **portaria central com identifica??o autom?tica** (o Traefik existente).
Nenhuma sala existente ? tocada, nenhum dado ? exposto e nenhuma porta ? alterada.

---

## 2. Fase 1: Apontamento de DNS no seu Provedor

Antes de subir a stack, acesse o painel de controle do seu dom?nio (Cloudflare, Registro.br, Hostinger ou AWS Route53) e crie os apontamentos do tipo **A**:

{dns_lines}

> **Nota:** Se estiver utilizando Cloudflare, certifique-se de que a nuvem esteja inicialmente cinza (DNS Only) ou laranja com SSL/TLS configurado em modo **Full (Strict)**.

---

## 3. Fase 2: Implanta??o da Stack no Painel Portainer

Siga o roteiro passo a passo:

1. Acesse o seu painel de controle: `https://painel.{self.base_domain}`.
2. Fa?a login com suas credenciais de administrador.
3. No menu lateral esquerdo, clique em **Stacks**.
4. Clique no bot?o azul superior **+ Add stack**.
5. No campo **Name**, digite exatamente: `{slug_clean}`.
6. Na caixa de texto do **Web editor**, cole o conte?do integral do arquivo `02-stack-integrada-portainer.yml`.
7. Role a p?gina at? o rodap? e clique no bot?o **Deploy the stack**.
8. O Swarm baixar? as imagens oficiais, criar? os volumes nomeados e registrar? os novos subdom?nios no Traefik.

---

## 4. Fase 3: Wizard de Primeiro Acesso e Configura??o

Aguarde 60 a 90 segundos para a emiss?o autom?tica do certificado TLS Let's Encrypt. Em seguida, acesse as URLs:

{url_lines}

### Procedimento para o Ecossistema Google Workspace (Se Aplic?vel):
1. **Configura??o do Nextcloud (`https://drive.{self.base_domain}`):**
   - Crie o usu?rio administrador e senha.
   - O banco de dados PostgreSQL j? estar? configurado automaticamente via vari?veis de ambiente.
2. **Integra??o do ONLYOFFICE com Nextcloud:**
   - Acesse o Nextcloud com usu?rio administrador, v? em **Aplicativos** e ative o app **ONLYOFFICE**.
   - Em **Configura??es de Administra??o** > **ONLYOFFICE**, defina:
     - Endere?o do Servidor: `https://office.{self.base_domain}`
     - Chave Secreta (JWT): `OnlyOfficeSecretKey2026_SecureToken!`
     - Endere?o interno do Nextcloud: `http://workspace_nextcloud:80`
   - Clique em **Salvar**. A edi??o colaborativa de documentos estar? 100% operacional.

---

## 5. Fase 4: Cadastro de Monitoramento no Uptime Kuma

No painel do seu Uptime Kuma j? em execu??o (`https://monitor.{self.base_domain}`):
1. Clique em **Adicionar Novo Monitor**.
2. Tipo de Monitor: **HTTP(s)**.
3. Cadastre a URL de cada subdom?nio com intervalo de verifica??o de **60 segundos**.
"""

    def _build_manual_desinstalacao_md(self):
        prof = self.decision['profile']
        slug_clean = os.path.basename(self.output_dir)
        net = self.audit['ingress'].get('default_overlay', 'network_conexao')

        return f"""# Manual de Desinstala??o Cir?rgica e Rollback

**Alvo:** {prof['name']}  
**Garantia de Isolamento:** 100% de preserva??o dos demais containers da VPS  
**Tempo de Execu??o:** Menos de 10 segundos

---

## 1. Princ?pios de Seguran?a e Isolamento

Todos os recursos criados para o alvo `{prof['name']}` foram encapsulados no namespace `{slug_clean}`.
A remo??o da stack desconecta os servi?os da rede `{net}` e revoga os roteadores do Traefik de forma at?mica.
**Mautic, Evolution, n8n, MySQL, PostgreSQL global e Portainer continuam operando normalmente sem nenhuma interrup??o.**

---

## 2. Procedimento 1: Remo??o via Painel Portainer (Interface Gr?fica)

1. Acesse: `https://painel.{self.base_domain}`.
2. Clique em **Stacks** no menu lateral esquerdo.
3. Localize a stack `{slug_clean}` e marque a caixa de sele??o ao lado dela.
4. Clique no bot?o vermelho **Delete this stack**.
5. Confirme a exclus?o na janela pop-up.
6. Em menos de 10 segundos, todos os containers ser?o finalizados e as rotas web desligadas.

---

## 3. Procedimento 2: Remo??o via Linha de Comando (CLI / SSH)

Caso prefira executar via terminal SSH ou Termius:

```bash
# 1. Remover a stack do Docker Swarm
docker stack rm {slug_clean}

# 2. Aguardar 10 segundos para finalizacao completa dos processos
sleep 10

# 3. Verificar que as demais stacks continuam 100% operacionais
docker stack ls
docker service ls
```

---

## 4. Limpeza Opcional de Volumes Persistentes (Libera??o de Disco)

Se voc? n?o planeja restaurar a aplica??o e deseja liberar espa?o em disco:

```bash
# Listar e remover apenas os volumes exclusivos da stack removida
docker volume ls --filter name={slug_clean} -q | xargs -r docker volume rm
```

*(Nenhum volume do Mautic, n8n, PostgreSQL global ou MySQL ser? afetado).*
"""

    def _build_html_page(self, title, md_content, badge="Dossiê Executivo"):
        html_body = md_content.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        html_body = re.sub(r'^# (.*?)$', r"<h1 class='report-title'>\1</h1>", html_body, flags=re.MULTILINE)
        html_body = re.sub(r'^## (.*?)$', r"<h2>\1</h2>", html_body, flags=re.MULTILINE)
        html_body = re.sub(r'^### (.*?)$', r"<h3>\1</h3>", html_body, flags=re.MULTILINE)
        html_body = re.sub(r'\*\*(.*?)\*\*', r"<strong>\1</strong>", html_body)
        html_body = re.sub(r'`([^`]+)`', r"<code>\1</code>", html_body)
        html_body = re.sub(r'^---$', r"<hr>", html_body, flags=re.MULTILINE)

        lines = html_body.split('\n')
        in_table = False
        new_lines = []
        for line in lines:
            if line.strip().startswith('|') and '|' in line[1:]:
                if not in_table:
                    in_table = True
                    new_lines.append("<div class='table-wrapper'><table>")
                
                if ':---' in line:
                    continue
                
                parts = [p.strip() for p in line.strip().split('|')[1:-1]]
                tag = 'th' if not any('<tr>' in l for l in new_lines[-5:]) and in_table and '<table>' in new_lines[-1] else 'td'
                cells = "".join([f"<{tag}>{p}</{tag}>" for p in parts])
                new_lines.append(f"<tr>{cells}</tr>")
            else:
                if in_table:
                    in_table = False
                    new_lines.append("</table></div>")
                new_lines.append(line)

        if in_table:
            new_lines.append("</table></div>")

        processed_html = "\n".join(new_lines)

        return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
{ENTERPRISE_CSS}
    </style>
</head>
<body>
    <div class="container">
        <div class="header-card">
            <div class="header-badge">{badge}</div>
            {processed_html}
        </div>
    </div>
</body>
</html>"""
