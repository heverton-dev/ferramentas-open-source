# Manual de Engenharia de VPS & Desinstalação Cirúrgica: Authentik

> **Ferramenta:** Authentik (Plataforma Moderna de Identidade (SSO, MFA & Políticas))  
> **Pilar do Ecossistema:** Grupo 3: Identidade, Segurança & Governança (Admin, SSO, Vault & Endpoint) | **SaaS Substituído:** `Google Cloud Identity + Admin Console (SSO e federação)`  
> **Licença OSI:** `MIT` | **Hardware Recomendado:** `2 vCPU / 2 GB RAM RAM / PostgreSQL + Redis`  

---

## 1. Visão Geral & Papel no Ecossistema
Centraliza login único, autenticação multifator e políticas de acesso para todos os aplicativos da suíte. Backend Python (Django) com frontend React e provedores OIDC/SAML/LDAP.

---

## 2. Instalação e Deploy em Produção na VPS

### Passo 1: Preparação do Diretório & Rede
```bash
mkdir -p /opt/authentik && cd /opt/authentik
docker network create ecosystem_net || true
```

### Passo 2: Arquivo de Variáveis de Ambiente (.env)
```bash
cat <<EOF > .env
APP_NAME=Authentik
APP_PORT=8080
DATABASE_URL=postgresql://user:secret@postgres:5432/db_authentik
SECRET_KEY=$(openssl rand -hex 32)
EOF
```

### Passo 3: Manifesto docker-compose.yml
```yaml
version: '3.8'
services:
  authentik:
    image: authentik/server:latest
    restart: unless-stopped
    env_file: .env
    volumes:
      - ./authentik_data:/data
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

> **Garantia de Zero Efeito Colateral:** A remoção deste módulo afeta exclusivamente os contêineres e pastas de `/opt/authentik`. Nenhum outro banco de dados, proxy Traefik ou aplicação rodando na mesma VPS será impactado.

1. **Parada dos Contêineres:**
   ```bash
   cd /opt/authentik && docker compose down
   ```
2. **Remoção de Volumes e Dados:**
   ```bash
   cd /opt && rm -rf /opt/authentik
   docker volume rm authentik_data 2>/dev/null || true
   ```
3. **Limpeza de Portas e Checklist:**
   ```bash
   docker ps | grep authentik
   ```

---

## 4. Rotina de Backup & Disaster Recovery
```bash
tar -czf /var/backups/authentik-$(date +%Y%m%d).tar.gz -C /opt/authentik .
openssl enc -aes-256-cbc -salt -in /var/backups/authentik-$(date +%Y%m%d).tar.gz -out /var/backups/authentik-$(date +%Y%m%d).enc -k SegredoBackup2026
```
