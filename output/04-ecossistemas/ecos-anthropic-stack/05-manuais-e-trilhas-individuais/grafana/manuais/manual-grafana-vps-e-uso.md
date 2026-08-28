# Manual de Engenharia de VPS & Desinstalação Cirúrgica: Grafana

> **Ferramenta:** Grafana (Plataforma de Dashboards & Alertas para Observabilidade)  
> **Pilar do Ecossistema:** Grupo 3: Observabilidade, Monitoramento & Suporte | **SaaS Substituído:** `DataDog / New Relic (Dashboarding)`  
> **Licença OSI:** `AGPL-3.0 (Enterprise: Proprietary)` | **Hardware Recomendado:** `1 vCPU / 1 GB RAM RAM / PostgreSQL / SQLite`  

---

## 1. Visão Geral & Papel no Ecossistema
Constrói dashboards interativos consumindo dados de Prometheus, Loki e outras fontes. Go backend com React frontend e suporte a plugins customizados.

---

## 2. Instalação e Deploy em Produção na VPS

### Passo 1: Preparação do Diretório & Rede
```bash
mkdir -p /opt/grafana && cd /opt/grafana
docker network create ecosystem_net || true
```

### Passo 2: Arquivo de Variáveis de Ambiente (.env)
```bash
cat <<EOF > .env
APP_NAME=Grafana
APP_PORT=8080
DATABASE_URL=postgresql://user:secret@postgres:5432/db_grafana
SECRET_KEY=$(openssl rand -hex 32)
EOF
```

### Passo 3: Manifesto docker-compose.yml
```yaml
version: '3.8'
services:
  grafana:
    image: grafana:latest
    restart: unless-stopped
    env_file: .env
    volumes:
      - ./grafana_data:/data
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

> **Garantia de Zero Efeito Colateral:** A remoção deste módulo afeta exclusivamente os contêineres e pastas de `/opt/grafana`. Nenhum outro banco de dados, proxy Traefik ou aplicação rodando na mesma VPS será impactado.

1. **Parada dos Contêineres:**
   ```bash
   cd /opt/grafana && docker compose down
   ```
2. **Remoção de Volumes e Dados:**
   ```bash
   cd /opt && rm -rf /opt/grafana
   docker volume rm grafana_data 2>/dev/null || true
   ```
3. **Limpeza de Portas e Checklist:**
   ```bash
   docker ps | grep grafana
   ```

---

## 4. Rotina de Backup & Disaster Recovery
```bash
tar -czf /var/backups/grafana-$(date +%Y%m%d).tar.gz -C /opt/grafana .
openssl enc -aes-256-cbc -salt -in /var/backups/grafana-$(date +%Y%m%d).tar.gz -out /var/backups/grafana-$(date +%Y%m%d).enc -k SegredoBackup2026
```
