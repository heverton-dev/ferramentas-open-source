# Manual de Engenharia de VPS & Desinstalação Cirúrgica: OpenTelemetry Collector

> **Ferramenta:** OpenTelemetry Collector (Coleta & Processamento Agnóstico de Traces, Métricas & Logs)  
> **Pilar do Ecossistema:** Grupo 3: Observabilidade, Monitoramento & Suporte | **SaaS Substituído:** `Datadog / New Relic / Sentry (Tracing & Collection)`  
> **Licença OSI:** `Apache-2.0` | **Hardware Recomendado:** `1 vCPU / 1 GB RAM RAM / PostgreSQL / SQLite`  

---

## 1. Visão Geral & Papel no Ecossistema
Coleta traces, métricas e logs em formato OpenTelemetry e exporta para múltiplos backends. Go com suporte a OTLP protocol e receiversexportadores plugáveis.

---

## 2. Instalação e Deploy em Produção na VPS

### Passo 1: Preparação do Diretório & Rede
```bash
mkdir -p /opt/opentelemetry && cd /opt/opentelemetry
docker network create ecosystem_net || true
```

### Passo 2: Arquivo de Variáveis de Ambiente (.env)
```bash
cat <<EOF > .env
APP_NAME=OpenTelemetry Collector
APP_PORT=8080
DATABASE_URL=postgresql://user:secret@postgres:5432/db_opentelemetry
SECRET_KEY=$(openssl rand -hex 32)
EOF
```

### Passo 3: Manifesto docker-compose.yml
```yaml
version: '3.8'
services:
  opentelemetry:
    image: opentelemetry:latest
    restart: unless-stopped
    env_file: .env
    volumes:
      - ./opentelemetry_data:/data
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

> **Garantia de Zero Efeito Colateral:** A remoção deste módulo afeta exclusivamente os contêineres e pastas de `/opt/opentelemetry`. Nenhum outro banco de dados, proxy Traefik ou aplicação rodando na mesma VPS será impactado.

1. **Parada dos Contêineres:**
   ```bash
   cd /opt/opentelemetry && docker compose down
   ```
2. **Remoção de Volumes e Dados:**
   ```bash
   cd /opt && rm -rf /opt/opentelemetry
   docker volume rm opentelemetry_data 2>/dev/null || true
   ```
3. **Limpeza de Portas e Checklist:**
   ```bash
   docker ps | grep opentelemetry
   ```

---

## 4. Rotina de Backup & Disaster Recovery
```bash
tar -czf /var/backups/opentelemetry-$(date +%Y%m%d).tar.gz -C /opt/opentelemetry .
openssl enc -aes-256-cbc -salt -in /var/backups/opentelemetry-$(date +%Y%m%d).tar.gz -out /var/backups/opentelemetry-$(date +%Y%m%d).enc -k SegredoBackup2026
```
