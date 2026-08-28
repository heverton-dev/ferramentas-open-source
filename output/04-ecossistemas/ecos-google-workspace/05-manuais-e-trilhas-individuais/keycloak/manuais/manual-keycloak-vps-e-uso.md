# Manual de Engenharia de VPS & Desinstalação Cirúrgica: Keycloak

> **Ferramenta:** Keycloak (Identity and Access Management Empresarial (Red Hat))  
> **Pilar do Ecossistema:** Grupo 3: Identidade, Segurança & Governança (Admin, SSO, Vault & Endpoint) | **SaaS Substituído:** `Google Cloud Identity + Admin Console (IAM enterprise)`  
> **Licença OSI:** `Apache-2.0` | **Hardware Recomendado:** `2 vCPU / 2 GB RAM RAM / PostgreSQL`  

---

## 1. Visão Geral & Papel no Ecossistema
Fornece SSO, MFA, federação e gerenciamento de identidade para toda a suíte. Java (Quarkus) com provedores OIDC/SAML e armazenamento em PostgreSQL.

---

## 2. Instalação e Deploy em Produção na VPS

### Passo 1: Preparação do Diretório & Rede
```bash
mkdir -p /opt/keycloak && cd /opt/keycloak
docker network create ecosystem_net || true
```

### Passo 2: Arquivo de Variáveis de Ambiente (.env)
```bash
cat <<EOF > .env
APP_NAME=Keycloak
APP_PORT=8080
DATABASE_URL=postgresql://user:secret@postgres:5432/db_keycloak
SECRET_KEY=$(openssl rand -hex 32)
EOF
```

### Passo 3: Manifesto docker-compose.yml
```yaml
version: '3.8'
services:
  keycloak:
    image: quay.io/keycloak/keycloak:latest
    restart: unless-stopped
    env_file: .env
    volumes:
      - ./keycloak_data:/data
    networks:
      - ecosystem_net
```

### Passo 4: Inicialização & Validação
```bash
docker compose up -d
docker compose ps
docker compose logs -f --tail=50
```

---

## 3. Protocolo de Desinstalação Cirúrgica (Isolamento Total da VPS)

> **Garantia de Zero Efeito Colateral:** A remoção deste módulo afeta exclusivamente os contêineres e pastas de `/opt/keycloak`. Nenhum outro banco de dados, proxy Traefik ou aplicação rodando na mesma VPS será impactado.

1. **Parada dos Contêineres:**
   ```bash
   cd /opt/keycloak && docker compose down
   ```
2. **Remoção de Volumes e Dados:**
   ```bash
   cd /opt && rm -rf /opt/keycloak
   docker volume rm keycloak_data 2>/dev/null || true
   ```
3. **Limpeza de Portas e Checklist:**
   ```bash
   docker ps | grep keycloak
   ```

---

## 4. Rotina de Backup & Disaster Recovery
```bash
tar -czf /var/backups/keycloak-$(date +%Y%m%d).tar.gz -C /opt/keycloak .
openssl enc -aes-256-cbc -salt -in /var/backups/keycloak-$(date +%Y%m%d).tar.gz -out /var/backups/keycloak-$(date +%Y%m%d).enc -k SegredoBackup2026
```
