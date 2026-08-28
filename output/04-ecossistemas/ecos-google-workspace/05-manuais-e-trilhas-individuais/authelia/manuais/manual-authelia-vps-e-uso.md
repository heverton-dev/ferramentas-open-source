# Manual de Engenharia de VPS & Desinstalação Cirúrgica: Authelia

> **Ferramenta:** Authelia (SSO e 2FA Leve na Borda do Reverse Proxy)  
> **Pilar do Ecossistema:** Grupo 3: Identidade, Segurança & Governança (Admin, SSO, Vault & Endpoint) | **SaaS Substituído:** `Google Endpoint Management (MFA na borda)`  
> **Licença OSI:** `Apache-2.0` | **Hardware Recomendado:** `0.5 vCPU / 256 MB RAM RAM / SQLite / Redis (sessões)`  

---

## 1. Visão Geral & Papel no Ecossistema
Adiciona autenticação de dois fatores e SSO leve na frente de aplicações web. Go com sessões em Redis e integração transparente via ForwardAuth do Traefik.

---

## 2. Instalação e Deploy em Produção na VPS

### Passo 1: Preparação do Diretório & Rede
```bash
mkdir -p /opt/authelia && cd /opt/authelia
docker network create ecosystem_net || true
```

### Passo 2: Arquivo de Variáveis de Ambiente (.env)
```bash
cat <<EOF > .env
APP_NAME=Authelia
APP_PORT=8080
DATABASE_URL=postgresql://user:secret@postgres:5432/db_authelia
SECRET_KEY=$(openssl rand -hex 32)
EOF
```

### Passo 3: Manifesto docker-compose.yml
```yaml
version: '3.8'
services:
  authelia:
    image: authelia/authelia:latest
    restart: unless-stopped
    env_file: .env
    volumes:
      - ./authelia_data:/data
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

> **Garantia de Zero Efeito Colateral:** A remoção deste módulo afeta exclusivamente os contêineres e pastas de `/opt/authelia`. Nenhum outro banco de dados, proxy Traefik ou aplicação rodando na mesma VPS será impactado.

1. **Parada dos Contêineres:**
   ```bash
   cd /opt/authelia && docker compose down
   ```
2. **Remoção de Volumes e Dados:**
   ```bash
   cd /opt && rm -rf /opt/authelia
   docker volume rm authelia_data 2>/dev/null || true
   ```
3. **Limpeza de Portas e Checklist:**
   ```bash
   docker ps | grep authelia
   ```

---

## 4. Rotina de Backup & Disaster Recovery
```bash
tar -czf /var/backups/authelia-$(date +%Y%m%d).tar.gz -C /opt/authelia .
openssl enc -aes-256-cbc -salt -in /var/backups/authelia-$(date +%Y%m%d).tar.gz -out /var/backups/authelia-$(date +%Y%m%d).enc -k SegredoBackup2026
```
