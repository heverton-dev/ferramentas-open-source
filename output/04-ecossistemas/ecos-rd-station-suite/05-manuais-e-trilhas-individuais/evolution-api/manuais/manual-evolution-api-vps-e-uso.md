# Manual de Engenharia de VPS & Desinstalação Cirúrgica: Evolution API

> **Ferramenta:** Evolution API (Gateway Profissional de WhatsApp Baileys com Webhooks)  
> **Pilar do Ecossistema:** Grupo 3: Atendimento Omnichannel & WhatsApp | **SaaS Substituído:** `RD Station Conversas (Conectores Proprietários Z-API / Gupshup)`  
> **Licença OSI:** `Apache-2.0` | **Hardware Recomendado:** `1 vCPU / 2 GB RAM RAM / PostgreSQL / SQLite`  

---

## 1. Visão Geral & Papel no Ecossistema
Recebe e envia mensagens, mídias e áudios de WhatsApp via endpoints REST. Node.js e TypeScript com gerenciamento de sessões em Redis e Postgres.

---

## 2. Instalação e Deploy em Produção na VPS

### Passo 1: Preparação do Diretório & Rede
```bash
mkdir -p /opt/evolution-api && cd /opt/evolution-api
docker network create ecosystem_net || true
```

### Passo 2: Arquivo de Variáveis de Ambiente (.env)
```bash
cat <<EOF > .env
APP_NAME=Evolution API
APP_PORT=8080
DATABASE_URL=postgresql://user:secret@postgres:5432/db_evolution-api
SECRET_KEY=$(openssl rand -hex 32)
EOF
```

### Passo 3: Manifesto docker-compose.yml
```yaml
version: '3.8'
services:
  evolution-api:
    image: evolution-api:latest
    restart: unless-stopped
    env_file: .env
    volumes:
      - ./evolution-api_data:/data
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

> **Garantia de Zero Efeito Colateral:** A remoção deste módulo afeta exclusivamente os contêineres e pastas de `/opt/evolution-api`. Nenhum outro banco de dados, proxy Traefik ou aplicação rodando na mesma VPS será impactado.

1. **Parada dos Contêineres:**
   ```bash
   cd /opt/evolution-api && docker compose down
   ```
2. **Remoção de Volumes e Dados:**
   ```bash
   cd /opt && rm -rf /opt/evolution-api
   docker volume rm evolution-api_data 2>/dev/null || true
   ```
3. **Limpeza de Portas e Checklist:**
   ```bash
   docker ps | grep evolution-api
   ```

---

## 4. Rotina de Backup & Disaster Recovery
```bash
tar -czf /var/backups/evolution-api-$(date +%Y%m%d).tar.gz -C /opt/evolution-api .
openssl enc -aes-256-cbc -salt -in /var/backups/evolution-api-$(date +%Y%m%d).tar.gz -out /var/backups/evolution-api-$(date +%Y%m%d).enc -k SegredoBackup2026
```
