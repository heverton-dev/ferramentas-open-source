# Manual de Engenharia de VPS & Desinstalação Cirúrgica: WAHA

> **Ferramenta:** WAHA (Gateway Headless Secundário de Alta Disponibilidade)  
> **Pilar do Ecossistema:** Grupo 3: Atendimento Omnichannel & WhatsApp | **SaaS Substituído:** `RD Station Notificações WhatsApp / Twilio Messaging`  
> **Licença OSI:** `Apache-2.0` | **Hardware Recomendado:** `1 vCPU / 2 GB RAM RAM / PostgreSQL / SQLite`  

---

## 1. Visão Geral & Papel no Ecossistema
Fornece API HTTP estável para automações de sistema sem interferir na fila de atendimento humano. Sessões Chromium headless em contêiner Docker isolado.

---

## 2. Instalação e Deploy em Produção na VPS

### Passo 1: Preparação do Diretório & Rede
```bash
mkdir -p /opt/waha && cd /opt/waha
docker network create ecosystem_net || true
```

### Passo 2: Arquivo de Variáveis de Ambiente (.env)
```bash
cat <<EOF > .env
APP_NAME=WAHA
APP_PORT=8080
DATABASE_URL=postgresql://user:secret@postgres:5432/db_waha
SECRET_KEY=$(openssl rand -hex 32)
EOF
```

### Passo 3: Manifesto docker-compose.yml
```yaml
version: '3.8'
services:
  waha:
    image: waha:latest
    restart: unless-stopped
    env_file: .env
    volumes:
      - ./waha_data:/data
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

> **Garantia de Zero Efeito Colateral:** A remoção deste módulo afeta exclusivamente os contêineres e pastas de `/opt/waha`. Nenhum outro banco de dados, proxy Traefik ou aplicação rodando na mesma VPS será impactado.

1. **Parada dos Contêineres:**
   ```bash
   cd /opt/waha && docker compose down
   ```
2. **Remoção de Volumes e Dados:**
   ```bash
   cd /opt && rm -rf /opt/waha
   docker volume rm waha_data 2>/dev/null || true
   ```
3. **Limpeza de Portas e Checklist:**
   ```bash
   docker ps | grep waha
   ```

---

## 4. Rotina de Backup & Disaster Recovery
```bash
tar -czf /var/backups/waha-$(date +%Y%m%d).tar.gz -C /opt/waha .
openssl enc -aes-256-cbc -salt -in /var/backups/waha-$(date +%Y%m%d).tar.gz -out /var/backups/waha-$(date +%Y%m%d).enc -k SegredoBackup2026
```
