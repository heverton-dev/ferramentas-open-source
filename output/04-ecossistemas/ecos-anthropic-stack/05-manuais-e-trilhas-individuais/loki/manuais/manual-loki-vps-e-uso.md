# Manual de Engenharia de VPS & Desinstalação Cirúrgica: Loki

> **Ferramenta:** Loki (Log Aggregation System com Índices Otimizados)  
> **Pilar do Ecossistema:** Grupo 3: Observabilidade, Monitoramento & Suporte | **SaaS Substituído:** `DataDog / Splunk / Elasticsearch (Logging)`  
> **Licença OSI:** `AGPL-3.0` | **Hardware Recomendado:** `1 vCPU / 2 GB RAM RAM / PostgreSQL / SQLite`  

---

## 1. Visão Geral & Papel no Ecossistema
Ingere logs de containers, estrutura-os por labels e fornece buscas rápidas com LogQL. Go com armazenamento em S3 (MinIO) e índices em memória.

---

## 2. Instalação e Deploy em Produção na VPS

### Passo 1: Preparação do Diretório & Rede
```bash
mkdir -p /opt/loki && cd /opt/loki
docker network create ecosystem_net || true
```

### Passo 2: Arquivo de Variáveis de Ambiente (.env)
```bash
cat <<EOF > .env
APP_NAME=Loki
APP_PORT=8080
DATABASE_URL=postgresql://user:secret@postgres:5432/db_loki
SECRET_KEY=$(openssl rand -hex 32)
EOF
```

### Passo 3: Manifesto docker-compose.yml
```yaml
version: '3.8'
services:
  loki:
    image: loki:latest
    restart: unless-stopped
    env_file: .env
    volumes:
      - ./loki_data:/data
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

> **Garantia de Zero Efeito Colateral:** A remoção deste módulo afeta exclusivamente os contêineres e pastas de `/opt/loki`. Nenhum outro banco de dados, proxy Traefik ou aplicação rodando na mesma VPS será impactado.

1. **Parada dos Contêineres:**
   ```bash
   cd /opt/loki && docker compose down
   ```
2. **Remoção de Volumes e Dados:**
   ```bash
   cd /opt && rm -rf /opt/loki
   docker volume rm loki_data 2>/dev/null || true
   ```
3. **Limpeza de Portas e Checklist:**
   ```bash
   docker ps | grep loki
   ```

---

## 4. Rotina de Backup & Disaster Recovery
```bash
tar -czf /var/backups/loki-$(date +%Y%m%d).tar.gz -C /opt/loki .
openssl enc -aes-256-cbc -salt -in /var/backups/loki-$(date +%Y%m%d).tar.gz -out /var/backups/loki-$(date +%Y%m%d).enc -k SegredoBackup2026
```
