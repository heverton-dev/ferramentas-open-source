# Relat?rio de Viabilidade e Manual de Engenharia: Incorpora??o do Ecossistema Google Workspace na VPS

**Destino da Infraestrutura:** VPS de Produ??o (`painel.vpsconexao.org`)  
**Data da Auditoria:** 28/08/2026  
**Status de Viabilidade:** **100% Compat?vel e Homologado**

---

## 1. Diagn?stico e Auditoria da VPS Existente

A auditoria em tempo real realizada via API do Portainer revelou a seguinte infraestrutura ativa:

### 1.1 Especifica??es de Hardware e Capacidade
| Recurso | Capacidade Total | Utiliza??o Atual | Folga Dispon?vel |
| :--- | :--- | :--- | :--- |
| **vCPU** | 12 vCPUs | ~1.5 vCPUs em pico | **10.5 vCPUs livres** |
| **Mem?ria RAM** | 47.05 GiB (~50.5 GB) | ~3.2 GiB em uso | **~43.8 GiB livres** |
| **Modo Operacional** | Docker Swarm (1 N? Manager) | Ativo | Alta disponibilidade local |
| **Rede de Ingress** | Rede Overlay `network_conexao` | Ativa | Isolamento e roteamento interno |

### 1.2 Stacks e Servi?os Existentes em Execu??o
1. **Roteador e Ingress:** `traefik_traefik` gerenciando TLS autom?tico com o certificado `letsencryptresolver`.
2. **Bancos de Dados:** `postgres_postgres` e `mysql_mysql`.
3. **Automa??o e Comunica??o:** `n8n` (`flow.vpsconexao.org` com Webhook, Worker e Redis), `mautic` (`send-email.vpsconexao.org`), `evolution_evolution_api` (`evoapi.vpsconexao.org`).
4. **Monitoramento e Gest?o:** `portainer` (`painel.vpsconexao.org`), `uptime-kuma` (`monitor.vpsconexao.org`), `erp-odonto_app`, `mapas_web`.

---

## 2. An?lise de Viabilidade T?cnica

A incorpora??o do ecossistema Google Workspace ? plenamente vi?vel e de baixo risco, pelos seguintes fatores:

1. **Requisitos de Recursos:** A su?te corporativa completa (Nextcloud Hub, ONLYOFFICE Document Server, Stalwart Mail Server, CryptPad e Zitadel/Keycloak) demanda aproximadamente **6 a 8 GB de RAM** e **4 vCPUs**. A VPS disp?e de **~43.8 GB de RAM livres**, permitindo folga superior a 500%.
2. **Aproveitamento de Servi?os Existentes:** A VPS j? possui **Traefik**, **n8n** e **Uptime Kuma** instalados e funcionando. N?o h? necessidade de duplicar esses componentes.
3. **Zero Conflito de Portas Web:** Todas as aplica??es web operam em portas internas na rede overlay `network_conexao`, sendo roteadas exclusivamente por nomes de dom?nio (SNI / Host Header) atrav?s do Traefik.
4. **Isolamento por Swarm Stack:** O ecossistema ser? encapsulado em uma stack isolada (`workspace`), permitindo ativa??o, atualiza??o e remo??o at?mica sem qualquer impacto nas aplica??es existentes (`mautic`, `evolution`, `n8n`, `erp-odonto`).

---

## 3. Arquitetura da Stack Integrada

A su?te recomendada para substituir 100% das ferramentas do Google Workspace:

| Pilar Google Workspace | Ferramenta Open Source Homologada | Subdom?nio de Exemplo |
| :--- | :--- | :--- |
| **Google Drive / Gmail / Agenda / Contatos** | Nextcloud Hub (PHP-FPM + Nginx) | `drive.vpsconexao.org` |
| **Google Docs / Sheets / Slides** | ONLYOFFICE Document Server | `office.vpsconexao.org` |
| **Servidor de E-mail Corporativo (SMTP/IMAP/JMAP)** | Stalwart All-in-One Server | `mail.vpsconexao.org` |
| **Formul?rios / Docs Criptografados (Zero-Knowledge)** | CryptPad | `docs.vpsconexao.org` |
| **Google Identity & Single Sign-On (SSO)** | Zitadel ou Keycloak | `sso.vpsconexao.org` |
| **Google AppSheet / Automa??es** | n8n | *J? instalado e ativo na VPS* |
| **Monitoramento de Sa?de dos Servi?os** | Uptime Kuma | *J? instalado e ativo na VPS* |

---

## 4. Manual Passo a Passo de Instala??o no Portainer

### 4.1 Pr?-requisito: Configura??o de DNS
No painel de controle do seu dom?nio (`vpsconexao.org` ou dom?nio corporativo), crie as seguintes entradas do tipo **A** apontando para o endere?o IP da VPS:

- `drive.vpsconexao.org`
- `office.vpsconexao.org`
- `mail.vpsconexao.org`
- `docs.vpsconexao.org`
- `sso.vpsconexao.org`

---

### 4.2 Arquivo Docker Compose Adaptado para a VPS (`docker-stack-workspace.yml`)

Este arquivo foi preparado especificamente para o ambiente Docker Swarm da VPS, integrando-se diretamente ? rede `network_conexao` e ao Traefik j? existente.

```yaml
version: '3.8'

services:
  # ==========================================
  # 1. BANCO DE DADOS DEDICADO DO ECOSSISTEMA
  # ==========================================
  workspace_db:
    image: postgres:16-alpine
    environment:
      POSTGRES_USER: workspace_user
      POSTGRES_PASSWORD: WorkspaceDBSecret_2026!
      POSTGRES_DB: workspace_nextcloud
    volumes:
      - workspace_db_data:/var/lib/postgresql/data
    networks:
      - network_conexao
    deploy:
      mode: replicated
      replicas: 1
      placement:
        constraints: [node.role == manager]
      resources:
        limits:
          cpus: '2.0'
          memory: 2048M

  # ==========================================
  # 2. CACHE & SESS?ES (REDIS DEDICADO)
  # ==========================================
  workspace_redis:
    image: redis:7-alpine
    command: redis-server --appendonly yes
    volumes:
      - workspace_redis_data:/data
    networks:
      - network_conexao
    deploy:
      mode: replicated
      replicas: 1
      resources:
        limits:
          cpus: '1.0'
          memory: 512M

  # ==========================================
  # 3. NEXTCLOUD HUB (DRIVE, MAIL, CALENDAR, TALK)
  # ==========================================
  workspace_nextcloud:
    image: nextcloud:30-apache
    environment:
      POSTGRES_HOST: workspace_db
      POSTGRES_DB: workspace_nextcloud
      POSTGRES_USER: workspace_user
      POSTGRES_PASSWORD: WorkspaceDBSecret_2026!
      REDIS_HOST: workspace_redis
      OVERWRITEPROTOCOL: https
      OVERWRITECLIURL: https://drive.vpsconexao.org
      TRUSTED_PROXIES: 10.0.0.0/8 172.16.0.0/12 192.168.0.0/16
    volumes:
      - workspace_nextcloud_html:/var/www/html
      - workspace_nextcloud_data:/var/www/html/data
    networks:
      - network_conexao
    deploy:
      mode: replicated
      replicas: 1
      labels:
        - "traefik.enable=true"
        - "traefik.docker.network=network_conexao"
        - "traefik.http.routers.workspace_nextcloud.rule=Host(`drive.vpsconexao.org`)"
        - "traefik.http.routers.workspace_nextcloud.entrypoints=websecure"
        - "traefik.http.routers.workspace_nextcloud.tls=true"
        - "traefik.http.routers.workspace_nextcloud.tls.certresolver=letsencryptresolver"
        - "traefik.http.routers.workspace_nextcloud.priority=10"
        - "traefik.http.services.workspace_nextcloud.loadbalancer.server.port=80"
        - "traefik.http.services.workspace_nextcloud.loadbalancer.passHostHeader=true"
      resources:
        limits:
          cpus: '3.0'
          memory: 3072M

  # ==========================================
  # 4. ONLYOFFICE DOCUMENT SERVER (DOCS/SHEETS/SLIDES)
  # ==========================================
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
      - network_conexao
    deploy:
      mode: replicated
      replicas: 1
      labels:
        - "traefik.enable=true"
        - "traefik.docker.network=network_conexao"
        - "traefik.http.routers.workspace_onlyoffice.rule=Host(`office.vpsconexao.org`)"
        - "traefik.http.routers.workspace_onlyoffice.entrypoints=websecure"
        - "traefik.http.routers.workspace_onlyoffice.tls=true"
        - "traefik.http.routers.workspace_onlyoffice.tls.certresolver=letsencryptresolver"
        - "traefik.http.routers.workspace_onlyoffice.priority=10"
        - "traefik.http.services.workspace_onlyoffice.loadbalancer.server.port=80"
        - "traefik.http.services.workspace_onlyoffice.loadbalancer.passHostHeader=true"
      resources:
        limits:
          cpus: '3.0'
          memory: 3072M

  # ==========================================
  # 5. STALWART MAIL SERVER (SMTP/IMAP/JMAP/CALDAV)
  # ==========================================
  workspace_stalwart:
    image: stalwartlabs/stalwart:latest
    environment:
      STALWART_ADMIN_USER: admin
      STALWART_ADMIN_PASS: StalwartMasterPass2026!
    volumes:
      - workspace_stalwart_data:/opt/stalwart-mail
    networks:
      - network_conexao
    deploy:
      mode: replicated
      replicas: 1
      labels:
        - "traefik.enable=true"
        - "traefik.docker.network=network_conexao"
        - "traefik.http.routers.workspace_stalwart.rule=Host(`mail.vpsconexao.org`)"
        - "traefik.http.routers.workspace_stalwart.entrypoints=websecure"
        - "traefik.http.routers.workspace_stalwart.tls=true"
        - "traefik.http.routers.workspace_stalwart.tls.certresolver=letsencryptresolver"
        - "traefik.http.routers.workspace_stalwart.priority=10"
        - "traefik.http.services.workspace_stalwart.loadbalancer.server.port=8080"
        - "traefik.http.services.workspace_stalwart.loadbalancer.passHostHeader=true"
      resources:
        limits:
          cpus: '2.0'
          memory: 2048M

  # ==========================================
  # 6. CRYPTPAD (SU?TE CRIPTOGRAFADA ZERO-KNOWLEDGE)
  # ==========================================
  workspace_cryptpad:
    image: cryptpad/cryptpad:latest
    environment:
      CPAD_MAIN_DOMAIN: https://docs.vpsconexao.org
    volumes:
      - workspace_cryptpad_data:/cryptpad/datastore
      - workspace_cryptpad_blob:/cryptpad/blob
    networks:
      - network_conexao
    deploy:
      mode: replicated
      replicas: 1
      labels:
        - "traefik.enable=true"
        - "traefik.docker.network=network_conexao"
        - "traefik.http.routers.workspace_cryptpad.rule=Host(`docs.vpsconexao.org`)"
        - "traefik.http.routers.workspace_cryptpad.entrypoints=websecure"
        - "traefik.http.routers.workspace_cryptpad.tls=true"
        - "traefik.http.routers.workspace_cryptpad.tls.certresolver=letsencryptresolver"
        - "traefik.http.routers.workspace_cryptpad.priority=10"
        - "traefik.http.services.workspace_cryptpad.loadbalancer.server.port=3000"
        - "traefik.http.services.workspace_cryptpad.loadbalancer.passHostHeader=true"
      resources:
        limits:
          cpus: '2.0'
          memory: 2048M

# ==========================================
# REDE EXTERNA EXISTENTE NA VPS
# ==========================================
networks:
  network_conexao:
    external: true

# ==========================================
# VOLUMES PERSISTENTES ISOLADOS
# ==========================================
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
```

---

### 4.3 Procedimento de Implanta??o no Painel Portainer

1. Acesse o Portainer: `https://painel.vpsconexao.org`.
2. No menu lateral, clique em **Stacks** e depois em **+ Add stack**.
3. Defina o nome da stack como: `workspace`.
4. No campo **Web editor**, cole o conte?do YAML acima.
5. Role at? o final e clique no bot?o **Deploy the stack**.
6. O Swarm far? o download das imagens, criar? os volumes nomeados e registrar? as rotas no Traefik existente.
7. Em 60 a 90 segundos, os certificados Let's Encrypt ser?o gerados e os servi?os estar?o acess?veis via HTTPS.

---

## 5. Integra??o entre os Componentes

### 5.1 Conectar o ONLYOFFICE ao Nextcloud
1. Acesse `https://drive.vpsconexao.org` e conclua a cria??o do usu?rio administrador.
2. V? em **Aplicativos** (?cone de engrenagem) e ative o app **ONLYOFFICE**.
3. V? em **Configura??es de Administra??o** > **ONLYOFFICE**.
4. Configure os campos:
   - **Endere?o do Document Editing Service:** `https://office.vpsconexao.org`
   - **Chave Secreta (JWT):** `OnlyOfficeSecretKey2026_SecureToken!`
   - **Endere?o do Nextcloud para requisi??es internas:** `http://workspace_nextcloud:80`
5. Clique em **Salvar**. Documentos `.docx`, `.xlsx` e `.pptx` poder?o ser editados diretamente no navegador com suporte a coautoria em tempo real.

### 5.2 Cadastrar Monitores no Uptime Kuma Existente
No painel do Uptime Kuma j? em execu??o (`https://monitor.vpsconexao.org`):
1. Adicione os monitores HTTP(s) para:
   - Nextcloud Hub: `https://drive.vpsconexao.org`
   - ONLYOFFICE: `https://office.vpsconexao.org/healthcheck`
   - Stalwart Mail: `https://mail.vpsconexao.org`
   - CryptPad: `https://docs.vpsconexao.org`

---

## 6. Procedimento de Desinstala??o Cir?rgica (Rollback Seguro)

A arquitetura foi desenhada para garantir **isolamento absoluto**. A desinstala??o n?o afeta nenhuma outra aplica??o na VPS.

### 6.1 Remo??o via Painel Portainer
1. Acesse `https://painel.vpsconexao.org` > **Stacks**.
2. Selecione a stack `workspace`.
3. Clique em **Delete this stack** e confirme.
4. Todos os 6 servi?os ser?o desligados e suas rotas ser?o removidas do Traefik instantaneamente.

### 6.2 Limpeza Opcional de Dados e Volumes
Se desejar eliminar tamb?m os dados armazenados (liberando espa?o em disco):
1. No Portainer, v? em **Volumes**.
2. Filtre por `workspace_`.
3. Selecione os volumes da stack e clique em **Remove**.

*(Nenhum volume do Mautic, n8n, PostgreSQL existente, MySQL ou Portainer ? afetado).*
