# Manual de Engenharia de VPS & Desinstalação Cirúrgica: Alertmanager

> **Ferramenta:** Alertmanager (Gerenciador de Alertas & Deduplicação)  
> **Pilar do Ecossistema:** Grupo 3: Observabilidade, Monitoramento & Suporte | **SaaS Substituído:** `PagerDuty (Alert Routing)`  
> **Licença OSI:** `Apache-2.0` | **Hardware Recomendado:** `1 vCPU / 512 MB RAM RAM / PostgreSQL / SQLite`  

---

## 1. Visão Geral & Papel no Ecossistema
Agrupa alertas similares, deduplica e envia notificações via múltiplos canais. Go com armazenamento em memória e replicação opcional.

---

## 2. Instalação e Deploy em Produção na VPS

### Passo 1: Preparação do Diretório & Rede
```bash
mkdir -p /opt/alertmanager && cd /opt/alertmanager
docker network create ecosystem_net || true
```

### Passo 2: Arquivo de Variáveis de Ambiente (.env)
```bash
cat <<EOF > .env
APP_NAME=Alertmanager
APP_PORT=8080
DATABASE_URL=postgresql://user:secret@postgres:5432/db_alertmanager
SECRET_KEY=$(openssl rand -hex 32)
EOF
```

### Passo 3: Manifesto docker-compose.yml
```yaml
version: '3.8'
services:
  alertmanager:
    image: alertmanager:latest
    restart: unless-stopped
    env_file: .env
    volumes:
      - ./alertmanager_data:/data
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

> **Garantia de Zero Efeito Colateral:** A remoção deste módulo afeta exclusivamente os contêineres e pastas de `/opt/alertmanager`. Nenhum outro banco de dados, proxy Traefik ou aplicação rodando na mesma VPS será impactado.

1. **Parada dos Contêineres:**
   ```bash
   cd /opt/alertmanager && docker compose down
   ```
2. **Remoção de Volumes e Dados:**
   ```bash
   cd /opt && rm -rf /opt/alertmanager
   docker volume rm alertmanager_data 2>/dev/null || true
   ```
3. **Limpeza de Portas e Checklist:**
   ```bash
   docker ps | grep alertmanager
   ```

---

## 4. Rotina de Backup & Disaster Recovery
```bash
tar -czf /var/backups/alertmanager-$(date +%Y%m%d).tar.gz -C /opt/alertmanager .
openssl enc -aes-256-cbc -salt -in /var/backups/alertmanager-$(date +%Y%m%d).tar.gz -out /var/backups/alertmanager-$(date +%Y%m%d).enc -k SegredoBackup2026
```
