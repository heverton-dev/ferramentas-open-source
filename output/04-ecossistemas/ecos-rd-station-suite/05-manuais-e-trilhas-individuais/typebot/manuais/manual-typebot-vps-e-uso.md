# Manual de Engenharia de VPS & Desinstalação Cirúrgica: Typebot

> **Ferramenta:** Typebot (Construtor Visual de Fluxos de Triagem & Qualificação)  
> **Pilar do Ecossistema:** Grupo 3: Atendimento Omnichannel & WhatsApp | **SaaS Substituído:** `RD Station Conversas (Chatbots de Triagem) / Landbot`  
> **Licença OSI:** `AGPL-3.0` | **Hardware Recomendado:** `1 vCPU / 2 GB RAM RAM / PostgreSQL / SQLite`  

---

## 1. Visão Geral & Papel no Ecossistema
Cria chatbots conversacionais interativos para qualificação de leads antes do humano. Editor visual drag-and-drop com blocos lógicos e integração nativa com IA e webhooks.

---

## 2. Instalação e Deploy em Produção na VPS

### Passo 1: Preparação do Diretório & Rede
```bash
mkdir -p /opt/typebot && cd /opt/typebot
docker network create ecosystem_net || true
```

### Passo 2: Arquivo de Variáveis de Ambiente (.env)
```bash
cat <<EOF > .env
APP_NAME=Typebot
APP_PORT=8080
DATABASE_URL=postgresql://user:secret@postgres:5432/db_typebot
SECRET_KEY=$(openssl rand -hex 32)
EOF
```

### Passo 3: Manifesto docker-compose.yml
```yaml
version: '3.8'
services:
  typebot:
    image: typebot:latest
    restart: unless-stopped
    env_file: .env
    volumes:
      - ./typebot_data:/data
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

> **Garantia de Zero Efeito Colateral:** A remoção deste módulo afeta exclusivamente os contêineres e pastas de `/opt/typebot`. Nenhum outro banco de dados, proxy Traefik ou aplicação rodando na mesma VPS será impactado.

1. **Parada dos Contêineres:**
   ```bash
   cd /opt/typebot && docker compose down
   ```
2. **Remoção de Volumes e Dados:**
   ```bash
   cd /opt && rm -rf /opt/typebot
   docker volume rm typebot_data 2>/dev/null || true
   ```
3. **Limpeza de Portas e Checklist:**
   ```bash
   docker ps | grep typebot
   ```

---

## 4. Rotina de Backup & Disaster Recovery
```bash
tar -czf /var/backups/typebot-$(date +%Y%m%d).tar.gz -C /opt/typebot .
openssl enc -aes-256-cbc -salt -in /var/backups/typebot-$(date +%Y%m%d).tar.gz -out /var/backups/typebot-$(date +%Y%m%d).enc -k SegredoBackup2026
```
