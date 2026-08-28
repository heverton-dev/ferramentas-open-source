# Manual de Engenharia de VPS & Desinstalação Cirúrgica: Gitea

> **Ferramenta:** Gitea (Servidor Git Auto-Hospedado Leve com Interface Web)  
> **Pilar do Ecossistema:** Grupo 2: Infraestrutura de Desenvolvimento, CI/CD & Versionamento | **SaaS Substituído:** `GitHub (Team Plan) / GitLab (Premium)`  
> **Licença OSI:** `MIT` | **Hardware Recomendado:** `1 vCPU / 2 GB RAM RAM / PostgreSQL / SQLite`  

---

## 1. Visão Geral & Papel no Ecossistema
Fornece servidor Git completo com interface web para gerenciar repositórios e colaboração. Binário Go estático sobre SQLite ou PostgreSQL com suporte a organizações e equipas.

---

## 2. Instalação e Deploy em Produção na VPS

### Passo 1: Preparação do Diretório & Rede
```bash
mkdir -p /opt/gitea && cd /opt/gitea
docker network create ecosystem_net || true
```

### Passo 2: Arquivo de Variáveis de Ambiente (.env)
```bash
cat <<EOF > .env
APP_NAME=Gitea
APP_PORT=8080
DATABASE_URL=postgresql://user:secret@postgres:5432/db_gitea
SECRET_KEY=$(openssl rand -hex 32)
EOF
```

### Passo 3: Manifesto docker-compose.yml
```yaml
version: '3.8'
services:
  gitea:
    image: gitea:latest
    restart: unless-stopped
    env_file: .env
    volumes:
      - ./gitea_data:/data
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

> **Garantia de Zero Efeito Colateral:** A remoção deste módulo afeta exclusivamente os contêineres e pastas de `/opt/gitea`. Nenhum outro banco de dados, proxy Traefik ou aplicação rodando na mesma VPS será impactado.

1. **Parada dos Contêineres:**
   ```bash
   cd /opt/gitea && docker compose down
   ```
2. **Remoção de Volumes e Dados:**
   ```bash
   cd /opt && rm -rf /opt/gitea
   docker volume rm gitea_data 2>/dev/null || true
   ```
3. **Limpeza de Portas e Checklist:**
   ```bash
   docker ps | grep gitea
   ```

---

## 4. Rotina de Backup & Disaster Recovery
```bash
tar -czf /var/backups/gitea-$(date +%Y%m%d).tar.gz -C /opt/gitea .
openssl enc -aes-256-cbc -salt -in /var/backups/gitea-$(date +%Y%m%d).tar.gz -out /var/backups/gitea-$(date +%Y%m%d).enc -k SegredoBackup2026
```
