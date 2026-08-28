# Manual de Engenharia de VPS & Desinstalação Cirúrgica: Listmonk

> **Ferramenta:** Listmonk (Disparador de E-mails & Newsletters de Alta Performance)  
> **Pilar do Ecossistema:** Grupo 1: Marketing, Nutrição & Landing Pages | **SaaS Substituído:** `RD Station Marketing (Módulo de Disparos de E-mail & Broadcast)`  
> **Licença OSI:** `AGPL-3.0` | **Hardware Recomendado:** `1 vCPU / 1 GB RAM RAM / PostgreSQL / SQLite`  

---

## 1. Visão Geral & Papel no Ecossistema
Processa milhões de disparos de e-mail com segmentação SQL ultrarrápida. Binário Go estático de alto rendimento sobre PostgreSQL com suporte nativo a JSONB.

---

## 2. Instalação e Deploy em Produção na VPS

### Passo 1: Preparação do Diretório & Rede
```bash
mkdir -p /opt/listmonk && cd /opt/listmonk
docker network create ecosystem_net || true
```

### Passo 2: Arquivo de Variáveis de Ambiente (.env)
```bash
cat <<EOF > .env
APP_NAME=Listmonk
APP_PORT=8080
DATABASE_URL=postgresql://user:secret@postgres:5432/db_listmonk
SECRET_KEY=$(openssl rand -hex 32)
EOF
```

### Passo 3: Manifesto docker-compose.yml
```yaml
version: '3.8'
services:
  listmonk:
    image: listmonk:latest
    restart: unless-stopped
    env_file: .env
    volumes:
      - ./listmonk_data:/data
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

> **Garantia de Zero Efeito Colateral:** A remoção deste módulo afeta exclusivamente os contêineres e pastas de `/opt/listmonk`. Nenhum outro banco de dados, proxy Traefik ou aplicação rodando na mesma VPS será impactado.

1. **Parada dos Contêineres:**
   ```bash
   cd /opt/listmonk && docker compose down
   ```
2. **Remoção de Volumes e Dados:**
   ```bash
   cd /opt && rm -rf /opt/listmonk
   docker volume rm listmonk_data 2>/dev/null || true
   ```
3. **Limpeza de Portas e Checklist:**
   ```bash
   docker ps | grep listmonk
   ```

---

## 4. Rotina de Backup & Disaster Recovery
```bash
tar -czf /var/backups/listmonk-$(date +%Y%m%d).tar.gz -C /opt/listmonk .
openssl enc -aes-256-cbc -salt -in /var/backups/listmonk-$(date +%Y%m%d).tar.gz -out /var/backups/listmonk-$(date +%Y%m%d).enc -k SegredoBackup2026
```
