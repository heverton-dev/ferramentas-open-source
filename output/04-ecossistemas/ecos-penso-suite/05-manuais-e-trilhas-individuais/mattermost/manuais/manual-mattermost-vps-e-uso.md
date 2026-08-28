# Manual de Engenharia de VPS & Desinstalação Cirúrgica: Mattermost Team Edition

> **Ferramenta:** Mattermost Team Edition (A Plataforma de Mensageria Segura e Operações para Empresas Líder de Mercado)  
> **Pilar do Ecossistema:** Pilar 03: Comunicação Unificada, Chat Corporativo & Videoconferência | **SaaS Substituído:** `Penso Chat / Slack / Microsoft Teams`  
> **Licença OSI:** `MIT` | **Hardware Recomendado:** `2 vCPU / 2 GB RAM / PostgreSQL`  

---

## 1. Visão Geral & Papel no Ecossistema
Gerencia mensagens instantâneas, canais por projetos, integrações com sistemas legados e quadros de tarefas (Boards). Backend em Go de altíssima concorrência com PostgreSQL e interface moderna em React/Redux.

---

## 2. Instalação e Deploy em Produção na VPS

### Passo 1: Preparação do Diretório & Rede
```bash
mkdir -p /opt/mattermost && cd /opt/mattermost
docker network create ecosystem_net || true
```

### Passo 2: Arquivo de Variáveis de Ambiente (.env)
```bash
cat <<EOF > .env
APP_NAME=Mattermost Team Edition
APP_PORT=8080
DATABASE_URL=postgresql://user:secret@postgres:5432/db_mattermost
SECRET_KEY=$(openssl rand -hex 32)
EOF
```

### Passo 3: Manifesto docker-compose.yml
```yaml
version: '3.8'
services:
  mattermost:
    image: mattermost/mattermost-team-edition:latest
    restart: unless-stopped
    env_file: .env
    volumes:
      - ./mattermost_data:/data
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

> **Garantia de Zero Efeito Colateral:** A remoção deste módulo afeta exclusivamente os contêineres e pastas de `/opt/mattermost`. Nenhum outro banco de dados, proxy Traefik ou aplicação rodando na mesma VPS será impactado.

1. **Parada dos Contêineres:**
   ```bash
   cd /opt/mattermost && docker compose down
   ```
2. **Remoção de Volumes e Dados:**
   ```bash
   cd /opt && rm -rf /opt/mattermost
   docker volume rm mattermost_data 2>/dev/null || true
   ```
3. **Limpeza de Portas e Checklist:**
   ```bash
   docker ps | grep mattermost
   ```

---

## 4. Rotina de Backup & Disaster Recovery
```bash
tar -czf /var/backups/mattermost-$(date +%Y%m%d).tar.gz -C /opt/mattermost .
openssl enc -aes-256-cbc -salt -in /var/backups/mattermost-$(date +%Y%m%d).tar.gz -out /var/backups/mattermost-$(date +%Y%m%d).enc -k SegredoBackup2026
```
