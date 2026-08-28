# Manual de Engenharia de VPS & Desinstalação Cirúrgica: MinIO

> **Ferramenta:** MinIO (Object Storage S3-Compatible para Artefatos & Backups)  
> **Pilar do Ecossistema:** Grupo 2: Infraestrutura de Desenvolvimento, CI/CD & Versionamento | **SaaS Substituído:** `AWS S3 / Google Cloud Storage`  
> **Licença OSI:** `AGPL-3.0` | **Hardware Recomendado:** `1 vCPU / 1 GB RAM RAM / PostgreSQL / SQLite`  

---

## 1. Visão Geral & Papel no Ecossistema
Fornece armazenamento de objetos escalável com API S3-compatible. Binário Go com suporte a multi-node clustering e replicação.

---

## 2. Instalação e Deploy em Produção na VPS

### Passo 1: Preparação do Diretório & Rede
```bash
mkdir -p /opt/minio && cd /opt/minio
docker network create ecosystem_net || true
```

### Passo 2: Arquivo de Variáveis de Ambiente (.env)
```bash
cat <<EOF > .env
APP_NAME=MinIO
APP_PORT=8080
DATABASE_URL=postgresql://user:secret@postgres:5432/db_minio
SECRET_KEY=$(openssl rand -hex 32)
EOF
```

### Passo 3: Manifesto docker-compose.yml
```yaml
version: '3.8'
services:
  minio:
    image: minio:latest
    restart: unless-stopped
    env_file: .env
    volumes:
      - ./minio_data:/data
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

> **Garantia de Zero Efeito Colateral:** A remoção deste módulo afeta exclusivamente os contêineres e pastas de `/opt/minio`. Nenhum outro banco de dados, proxy Traefik ou aplicação rodando na mesma VPS será impactado.

1. **Parada dos Contêineres:**
   ```bash
   cd /opt/minio && docker compose down
   ```
2. **Remoção de Volumes e Dados:**
   ```bash
   cd /opt && rm -rf /opt/minio
   docker volume rm minio_data 2>/dev/null || true
   ```
3. **Limpeza de Portas e Checklist:**
   ```bash
   docker ps | grep minio
   ```

---

## 4. Rotina de Backup & Disaster Recovery
```bash
tar -czf /var/backups/minio-$(date +%Y%m%d).tar.gz -C /opt/minio .
openssl enc -aes-256-cbc -salt -in /var/backups/minio-$(date +%Y%m%d).tar.gz -out /var/backups/minio-$(date +%Y%m%d).enc -k SegredoBackup2026
```
