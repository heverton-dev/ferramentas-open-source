# Manual de Engenharia de VPS & Desinstalação Cirúrgica: Rocket.Chat

> **Ferramenta:** Rocket.Chat (Hub de Comunicação Omnichannel e Mensageria Corporativa Segura)  
> **Pilar do Ecossistema:** Pilar 03: Comunicação Unificada, Chat Corporativo & Videoconferência | **SaaS Substituído:** `Penso Chat & Atendimento`  
> **Licença OSI:** `MIT` | **Hardware Recomendado:** `2 vCPU / 2 GB RAM / MongoDB`  

---

## 1. Visão Geral & Papel no Ecossistema
Centraliza conversas de equipes internas e chats de suporte ao cliente em tempo real. Backend em Node.js com banco de dados MongoDB e suporte a microserviços de alta disponibilidade.

---

## 2. Instalação e Deploy em Produção na VPS

### Passo 1: Preparação do Diretório & Rede
```bash
mkdir -p /opt/rocket-chat && cd /opt/rocket-chat
docker network create ecosystem_net || true
```

### Passo 2: Arquivo de Variáveis de Ambiente (.env)
```bash
cat <<EOF > .env
APP_NAME=Rocket.Chat
APP_PORT=8080
DATABASE_URL=postgresql://user:secret@postgres:5432/db_rocket-chat
SECRET_KEY=$(openssl rand -hex 32)
EOF
```

### Passo 3: Manifesto docker-compose.yml
```yaml
version: '3.8'
services:
  rocket-chat:
    image: registry.rocket.chat/rocketchat/rocket.chat:latest
    restart: unless-stopped
    env_file: .env
    volumes:
      - ./rocket-chat_data:/data
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

> **Garantia de Zero Efeito Colateral:** A remoção deste módulo afeta exclusivamente os contêineres e pastas de `/opt/rocket-chat`. Nenhum outro banco de dados, proxy Traefik ou aplicação rodando na mesma VPS será impactado.

1. **Parada dos Contêineres:**
   ```bash
   cd /opt/rocket-chat && docker compose down
   ```
2. **Remoção de Volumes e Dados:**
   ```bash
   cd /opt && rm -rf /opt/rocket-chat
   docker volume rm rocket-chat_data 2>/dev/null || true
   ```
3. **Limpeza de Portas e Checklist:**
   ```bash
   docker ps | grep rocket-chat
   ```

---

## 4. Rotina de Backup & Disaster Recovery
```bash
tar -czf /var/backups/rocket-chat-$(date +%Y%m%d).tar.gz -C /opt/rocket-chat .
openssl enc -aes-256-cbc -salt -in /var/backups/rocket-chat-$(date +%Y%m%d).tar.gz -out /var/backups/rocket-chat-$(date +%Y%m%d).enc -k SegredoBackup2026
```
