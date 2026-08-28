# Manual de Engenharia de VPS & Desinstalação Cirúrgica: ZITADEL

> **Ferramenta:** ZITADEL (IAM Moderno Event-Sourced com OIDC, SAML & MFA)  
> **Pilar do Ecossistema:** Grupo 3: Identidade, Segurança & Governança (Admin, SSO, Vault & Endpoint) | **SaaS Substituído:** `Google Cloud Identity + Admin Console (IAM moderno)`  
> **Licença OSI:** `Apache-2.0` | **Hardware Recomendado:** `1 vCPU / 1 GB RAM RAM / PostgreSQL`  

---

## 1. Visão Geral & Papel no Ecossistema
Fornece identidade, SSO e MFA com modelo de eventos e auditoria completa. Go com CQRS/Event-Sourcing, armazenamento em PostgreSQL e APIs gRPC/REST.

---

## 2. Instalação e Deploy em Produção na VPS

### Passo 1: Preparação do Diretório & Rede
```bash
mkdir -p /opt/zitadel && cd /opt/zitadel
docker network create ecosystem_net || true
```

### Passo 2: Arquivo de Variáveis de Ambiente (.env)
```bash
cat <<EOF > .env
APP_NAME=ZITADEL
APP_PORT=8080
DATABASE_URL=postgresql://user:secret@postgres:5432/db_zitadel
SECRET_KEY=$(openssl rand -hex 32)
EOF
```

### Passo 3: Manifesto docker-compose.yml
```yaml
version: '3.8'
services:
  zitadel:
    image: zitadel/zitadel:latest
    restart: unless-stopped
    env_file: .env
    volumes:
      - ./zitadel_data:/data
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

> **Garantia de Zero Efeito Colateral:** A remoção deste módulo afeta exclusivamente os contêineres e pastas de `/opt/zitadel`. Nenhum outro banco de dados, proxy Traefik ou aplicação rodando na mesma VPS será impactado.

1. **Parada dos Contêineres:**
   ```bash
   cd /opt/zitadel && docker compose down
   ```
2. **Remoção de Volumes e Dados:**
   ```bash
   cd /opt && rm -rf /opt/zitadel
   docker volume rm zitadel_data 2>/dev/null || true
   ```
3. **Limpeza de Portas e Checklist:**
   ```bash
   docker ps | grep zitadel
   ```

---

## 4. Rotina de Backup & Disaster Recovery
```bash
tar -czf /var/backups/zitadel-$(date +%Y%m%d).tar.gz -C /opt/zitadel .
openssl enc -aes-256-cbc -salt -in /var/backups/zitadel-$(date +%Y%m%d).tar.gz -out /var/backups/zitadel-$(date +%Y%m%d).enc -k SegredoBackup2026
```
