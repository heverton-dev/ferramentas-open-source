# Manual de Engenharia de VPS & Desinstalação Cirúrgica: Docker Registry

> **Ferramenta:** Docker Registry (Registro Privado de Imagens Docker)  
> **Pilar do Ecossistema:** Grupo 2: Infraestrutura de Desenvolvimento, CI/CD & Versionamento | **SaaS Substituído:** `Docker Hub (Private Repos) / ECR / GCR`  
> **Licença OSI:** `Apache-2.0` | **Hardware Recomendado:** `1 vCPU / 1 GB RAM RAM / PostgreSQL / SQLite`  

---

## 1. Visão Geral & Papel no Ecossistema
Fornece repositório centralizado de imagens Docker com autenticação básica. Go com armazenamento em filesystem ou object storage S3 (MinIO).

---

## 2. Instalação e Deploy em Produção na VPS

### Passo 1: Preparação do Diretório & Rede
```bash
mkdir -p /opt/registry && cd /opt/registry
docker network create ecosystem_net || true
```

### Passo 2: Arquivo de Variáveis de Ambiente (.env)
```bash
cat <<EOF > .env
APP_NAME=Docker Registry
APP_PORT=8080
DATABASE_URL=postgresql://user:secret@postgres:5432/db_registry
SECRET_KEY=$(openssl rand -hex 32)
EOF
```

### Passo 3: Manifesto docker-compose.yml
```yaml
version: '3.8'
services:
  registry:
    image: registry:latest
    restart: unless-stopped
    env_file: .env
    volumes:
      - ./registry_data:/data
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

> **Garantia de Zero Efeito Colateral:** A remoção deste módulo afeta exclusivamente os contêineres e pastas de `/opt/registry`. Nenhum outro banco de dados, proxy Traefik ou aplicação rodando na mesma VPS será impactado.

1. **Parada dos Contêineres:**
   ```bash
   cd /opt/registry && docker compose down
   ```
2. **Remoção de Volumes e Dados:**
   ```bash
   cd /opt && rm -rf /opt/registry
   docker volume rm registry_data 2>/dev/null || true
   ```
3. **Limpeza de Portas e Checklist:**
   ```bash
   docker ps | grep registry
   ```

---

## 4. Rotina de Backup & Disaster Recovery
```bash
tar -czf /var/backups/registry-$(date +%Y%m%d).tar.gz -C /opt/registry .
openssl enc -aes-256-cbc -salt -in /var/backups/registry-$(date +%Y%m%d).tar.gz -out /var/backups/registry-$(date +%Y%m%d).enc -k SegredoBackup2026
```
