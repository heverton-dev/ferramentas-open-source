# Manual de Engenharia de VPS & Desinstalação Cirúrgica: Zulip

> **Ferramenta:** Zulip (Plataforma de Chat em Equipe Organizada por Tópicos e Threads Assíncronas)  
> **Pilar do Ecossistema:** Pilar 03: Comunicação Unificada, Chat Corporativo & Videoconferência | **SaaS Substituído:** `Penso Chat / Slack`  
> **Licença OSI:** `Apache-2.0` | **Hardware Recomendado:** `1 vCPU / 2 GB RAM / PostgreSQL / Redis`  

---

## 1. Visão Geral & Papel no Ecossistema
Combina a agilidade do chat em tempo real com a organização de um fórum corporativo estruturado. Backend Python/Django com Tornado para webhooks assíncronos e banco PostgreSQL.

---

## 2. Instalação e Deploy em Produção na VPS

### Passo 1: Preparação do Diretório & Rede
```bash
mkdir -p /opt/zulip && cd /opt/zulip
docker network create ecosystem_net || true
```

### Passo 2: Arquivo de Variáveis de Ambiente (.env)
```bash
cat <<EOF > .env
APP_NAME=Zulip
APP_PORT=8080
DATABASE_URL=postgresql://user:secret@postgres:5432/db_zulip
SECRET_KEY=$(openssl rand -hex 32)
EOF
```

### Passo 3: Manifesto docker-compose.yml
```yaml
version: '3.8'
services:
  zulip:
    image: zulip/docker-zulip:latest
    restart: unless-stopped
    env_file: .env
    volumes:
      - ./zulip_data:/data
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

> **Garantia de Zero Efeito Colateral:** A remoção deste módulo afeta exclusivamente os contêineres e pastas de `/opt/zulip`. Nenhum outro banco de dados, proxy Traefik ou aplicação rodando na mesma VPS será impactado.

1. **Parada dos Contêineres:**
   ```bash
   cd /opt/zulip && docker compose down
   ```
2. **Remoção de Volumes e Dados:**
   ```bash
   cd /opt && rm -rf /opt/zulip
   docker volume rm zulip_data 2>/dev/null || true
   ```
3. **Limpeza de Portas e Checklist:**
   ```bash
   docker ps | grep zulip
   ```

---

## 4. Rotina de Backup & Disaster Recovery
```bash
tar -czf /var/backups/zulip-$(date +%Y%m%d).tar.gz -C /opt/zulip .
openssl enc -aes-256-cbc -salt -in /var/backups/zulip-$(date +%Y%m%d).tar.gz -out /var/backups/zulip-$(date +%Y%m%d).enc -k SegredoBackup2026
```
