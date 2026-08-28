# Manual de Engenharia de VPS & Desinstalação Cirúrgica: Stalwart Mail Server

> **Ferramenta:** Stalwart Mail Server (Servidor de E-mail Moderno em Rust com JMAP, CalDAV & CardDAV)  
> **Pilar do Ecossistema:** Grupo 1: Comunicação Unificada (E-mail, Chat, Vídeo, Agenda & Contatos) | **SaaS Substituído:** `Gmail + Google Calendar + Google Contacts (protocolo moderno)`  
> **Licença OSI:** `AGPL-3.0` | **Hardware Recomendado:** `2 vCPU / 2 GB RAM RAM / RocksDB / PostgreSQL`  

---

## 1. Visão Geral & Papel no Ecossistema
Fornece e-mail, agenda e contatos modernos com protocolo JMAP e baixíssimo consumo de recursos. Binário único em Rust com armazenamento em RocksDB/PostgreSQL e painel web em React.

---

## 2. Instalação e Deploy em Produção na VPS

### Passo 1: Preparação do Diretório & Rede
```bash
mkdir -p /opt/stalwart && cd /opt/stalwart
docker network create ecosystem_net || true
```

### Passo 2: Arquivo de Variáveis de Ambiente (.env)
```bash
cat <<EOF > .env
APP_NAME=Stalwart Mail Server
APP_PORT=8080
DATABASE_URL=postgresql://user:secret@postgres:5432/db_stalwart
SECRET_KEY=$(openssl rand -hex 32)
EOF
```

### Passo 3: Manifesto docker-compose.yml
```yaml
version: '3.8'
services:
  stalwart:
    image: stalwartlabs/stalwart:latest
    restart: unless-stopped
    env_file: .env
    volumes:
      - ./stalwart_data:/data
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

> **Garantia de Zero Efeito Colateral:** A remoção deste módulo afeta exclusivamente os contêineres e pastas de `/opt/stalwart`. Nenhum outro banco de dados, proxy Traefik ou aplicação rodando na mesma VPS será impactado.

1. **Parada dos Contêineres:**
   ```bash
   cd /opt/stalwart && docker compose down
   ```
2. **Remoção de Volumes e Dados:**
   ```bash
   cd /opt && rm -rf /opt/stalwart
   docker volume rm stalwart_data 2>/dev/null || true
   ```
3. **Limpeza de Portas e Checklist:**
   ```bash
   docker ps | grep stalwart
   ```

---

## 4. Rotina de Backup & Disaster Recovery
```bash
tar -czf /var/backups/stalwart-$(date +%Y%m%d).tar.gz -C /opt/stalwart .
openssl enc -aes-256-cbc -salt -in /var/backups/stalwart-$(date +%Y%m%d).tar.gz -out /var/backups/stalwart-$(date +%Y%m%d).enc -k SegredoBackup2026
```
