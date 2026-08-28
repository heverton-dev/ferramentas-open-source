# Manual de Engenharia de VPS & Desinstalação Cirúrgica: Papercups

> **Ferramenta:** Papercups (Livechat & Suporte Direto sem Burocracia)  
> **Pilar do Ecossistema:** Grupo 3: Atendimento Omnichannel & WhatsApp | **SaaS Substituído:** `Intercom / Crisp / Chat Básico do RD`  
> **Licença OSI:** `MIT` | **Hardware Recomendado:** `1 vCPU / 1 GB RAM RAM / PostgreSQL / SQLite`  

---

## 1. Visão Geral & Papel no Ecossistema
Fornece chat ao vivo para clientes conversarem com a equipe diretamente pelo navegador. Backend em Elixir/Phoenix (alta concorrência) com frontend em React.

---

## 2. Instalação e Deploy em Produção na VPS

### Passo 1: Preparação do Diretório & Rede
```bash
mkdir -p /opt/papercups && cd /opt/papercups
docker network create ecosystem_net || true
```

### Passo 2: Arquivo de Variáveis de Ambiente (.env)
```bash
cat <<EOF > .env
APP_NAME=Papercups
APP_PORT=8080
DATABASE_URL=postgresql://user:secret@postgres:5432/db_papercups
SECRET_KEY=$(openssl rand -hex 32)
EOF
```

### Passo 3: Manifesto docker-compose.yml
```yaml
version: '3.8'
services:
  papercups:
    image: papercups:latest
    restart: unless-stopped
    env_file: .env
    volumes:
      - ./papercups_data:/data
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

> **Garantia de Zero Efeito Colateral:** A remoção deste módulo afeta exclusivamente os contêineres e pastas de `/opt/papercups`. Nenhum outro banco de dados, proxy Traefik ou aplicação rodando na mesma VPS será impactado.

1. **Parada dos Contêineres:**
   ```bash
   cd /opt/papercups && docker compose down
   ```
2. **Remoção de Volumes e Dados:**
   ```bash
   cd /opt && rm -rf /opt/papercups
   docker volume rm papercups_data 2>/dev/null || true
   ```
3. **Limpeza de Portas e Checklist:**
   ```bash
   docker ps | grep papercups
   ```

---

## 4. Rotina de Backup & Disaster Recovery
```bash
tar -czf /var/backups/papercups-$(date +%Y%m%d).tar.gz -C /opt/papercups .
openssl enc -aes-256-cbc -salt -in /var/backups/papercups-$(date +%Y%m%d).tar.gz -out /var/backups/papercups-$(date +%Y%m%d).enc -k SegredoBackup2026
```
