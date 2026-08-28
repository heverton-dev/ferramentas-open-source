# Manual de Engenharia de VPS & Desinstalação Cirúrgica: Chatwoot

> **Ferramenta:** Chatwoot (Central de Atendimento Omnicanal & Livechat Colaborativo)  
> **Pilar do Ecossistema:** Grupo 3: Atendimento Omnichannel & WhatsApp | **SaaS Substituído:** `RD Station Conversas (Painel de Atendimento Multiatendente)`  
> **Licença OSI:** `MIT` | **Hardware Recomendado:** `1 vCPU / 4 GB RAM RAM / PostgreSQL / SQLite`  

---

## 1. Visão Geral & Papel no Ecossistema
Centraliza conversas de clientes, distribui tickets e permite notas internas entre atendentes. Ruby on Rails com WebSockets e Vue.js para mensageria em tempo real.

---

## 2. Instalação e Deploy em Produção na VPS

### Passo 1: Preparação do Diretório & Rede
```bash
mkdir -p /opt/chatwoot && cd /opt/chatwoot
docker network create ecosystem_net || true
```

### Passo 2: Arquivo de Variáveis de Ambiente (.env)
```bash
cat <<EOF > .env
APP_NAME=Chatwoot
APP_PORT=8080
DATABASE_URL=postgresql://user:secret@postgres:5432/db_chatwoot
SECRET_KEY=$(openssl rand -hex 32)
EOF
```

### Passo 3: Manifesto docker-compose.yml
```yaml
version: '3.8'
services:
  chatwoot:
    image: chatwoot:latest
    restart: unless-stopped
    env_file: .env
    volumes:
      - ./chatwoot_data:/data
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

> **Garantia de Zero Efeito Colateral:** A remoção deste módulo afeta exclusivamente os contêineres e pastas de `/opt/chatwoot`. Nenhum outro banco de dados, proxy Traefik ou aplicação rodando na mesma VPS será impactado.

1. **Parada dos Contêineres:**
   ```bash
   cd /opt/chatwoot && docker compose down
   ```
2. **Remoção de Volumes e Dados:**
   ```bash
   cd /opt && rm -rf /opt/chatwoot
   docker volume rm chatwoot_data 2>/dev/null || true
   ```
3. **Limpeza de Portas e Checklist:**
   ```bash
   docker ps | grep chatwoot
   ```

---

## 4. Rotina de Backup & Disaster Recovery
```bash
tar -czf /var/backups/chatwoot-$(date +%Y%m%d).tar.gz -C /opt/chatwoot .
openssl enc -aes-256-cbc -salt -in /var/backups/chatwoot-$(date +%Y%m%d).tar.gz -out /var/backups/chatwoot-$(date +%Y%m%d).enc -k SegredoBackup2026
```
