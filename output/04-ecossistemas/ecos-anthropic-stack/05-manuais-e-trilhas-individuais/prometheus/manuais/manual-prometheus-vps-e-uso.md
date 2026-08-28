# Manual de Engenharia de VPS & Desinstalação Cirúrgica: Prometheus

> **Ferramenta:** Prometheus (Time-Series Database & Scraper de Métricas)  
> **Pilar do Ecossistema:** Grupo 3: Observabilidade, Monitoramento & Suporte | **SaaS Substituído:** `DataDog / New Relic (Infrastructure Monitoring)`  
> **Licença OSI:** `Apache-2.0` | **Hardware Recomendado:** `1 vCPU / 2 GB RAM RAM / PostgreSQL / SQLite`  

---

## 1. Visão Geral & Papel no Ecossistema
Scrape de endpoints `/metrics` em intervalos regulares, armazenando séries temporais e fornecendo SQL-like PromQL. Binário Go estático com armazenamento em disco local e compressão de dados.

---

## 2. Instalação e Deploy em Produção na VPS

### Passo 1: Preparação do Diretório & Rede
```bash
mkdir -p /opt/prometheus && cd /opt/prometheus
docker network create ecosystem_net || true
```

### Passo 2: Arquivo de Variáveis de Ambiente (.env)
```bash
cat <<EOF > .env
APP_NAME=Prometheus
APP_PORT=8080
DATABASE_URL=postgresql://user:secret@postgres:5432/db_prometheus
SECRET_KEY=$(openssl rand -hex 32)
EOF
```

### Passo 3: Manifesto docker-compose.yml
```yaml
version: '3.8'
services:
  prometheus:
    image: prometheus:latest
    restart: unless-stopped
    env_file: .env
    volumes:
      - ./prometheus_data:/data
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

> **Garantia de Zero Efeito Colateral:** A remoção deste módulo afeta exclusivamente os contêineres e pastas de `/opt/prometheus`. Nenhum outro banco de dados, proxy Traefik ou aplicação rodando na mesma VPS será impactado.

1. **Parada dos Contêineres:**
   ```bash
   cd /opt/prometheus && docker compose down
   ```
2. **Remoção de Volumes e Dados:**
   ```bash
   cd /opt && rm -rf /opt/prometheus
   docker volume rm prometheus_data 2>/dev/null || true
   ```
3. **Limpeza de Portas e Checklist:**
   ```bash
   docker ps | grep prometheus
   ```

---

## 4. Rotina de Backup & Disaster Recovery
```bash
tar -czf /var/backups/prometheus-$(date +%Y%m%d).tar.gz -C /opt/prometheus .
openssl enc -aes-256-cbc -salt -in /var/backups/prometheus-$(date +%Y%m%d).tar.gz -out /var/backups/prometheus-$(date +%Y%m%d).enc -k SegredoBackup2026
```
