# Manual de Engenharia de VPS & Desinstalação Cirúrgica: Stalwart Mail Server

> **Ferramenta:** Stalwart Mail Server (Servidor de Correio All-in-One de Próxima Geração em Rust)  
> **Pilar do Ecossistema:** Pilar 01: E-mail Corporativo, Groupware & Gateway Antispam | **SaaS Substituído:** `Penso Mail High Performance`  
> **Licença OSI:** `AGPL-3.0` | **Hardware Recomendado:** `1 vCPU / 1 GB RAM / RocksDB / PostgreSQL`  

---

## 1. Visão Geral & Papel no Ecossistema
Unifica servidor SMTP, IMAP, JMAP, antispam e gerenciador de chaves criptográficas em um único serviço ultra-rápido. Arquitetura assíncrona em Rust com backend de armazenamento flexível (RocksDB, S3 ou SQL).

---

## 2. Instalação e Deploy em Produção na VPS

### Passo 1: Preparação do Diretório & Rede
```bash
mkdir -p /opt/stalwart-mail && cd /opt/stalwart-mail
docker network create ecosystem_net || true
```

### Passo 2: Arquivo de Variáveis de Ambiente (.env)
```bash
cat <<EOF > .env
APP_NAME=Stalwart Mail Server
APP_PORT=8080
DATABASE_URL=postgresql://user:secret@postgres:5432/db_stalwart-mail
SECRET_KEY=$(openssl rand -hex 32)
EOF
```

### Passo 3: Manifesto docker-compose.yml
```yaml
version: '3.8'
services:
  stalwart-mail:
    image: stalwartlabs/mail-server:latest
    restart: unless-stopped
    env_file: .env
    volumes:
      - ./stalwart-mail_data:/data
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

> **Garantia de Zero Efeito Colateral:** A remoção deste módulo afeta exclusivamente os contêineres e pastas de `/opt/stalwart-mail`. Nenhum outro banco de dados, proxy Traefik ou aplicação rodando na mesma VPS será impactado.

1. **Parada dos Contêineres:**
   ```bash
   cd /opt/stalwart-mail && docker compose down
   ```
2. **Remoção de Volumes e Dados:**
   ```bash
   cd /opt && rm -rf /opt/stalwart-mail
   docker volume rm stalwart-mail_data 2>/dev/null || true
   ```
3. **Limpeza de Portas e Checklist:**
   ```bash
   docker ps | grep stalwart-mail
   ```

---

## 4. Rotina de Backup & Disaster Recovery
```bash
tar -czf /var/backups/stalwart-mail-$(date +%Y%m%d).tar.gz -C /opt/stalwart-mail .
openssl enc -aes-256-cbc -salt -in /var/backups/stalwart-mail-$(date +%Y%m%d).tar.gz -out /var/backups/stalwart-mail-$(date +%Y%m%d).enc -k SegredoBackup2026
```
