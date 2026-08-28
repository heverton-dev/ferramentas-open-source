# Manual de Engenharia de VPS & Desinstalação Cirúrgica: ownCloud Infinite Scale (oCIS)

> **Ferramenta:** ownCloud Infinite Scale (oCIS) (Nuvem Corporativa Moderna em Go e Microserviços Cloud-Native)  
> **Pilar do Ecossistema:** Pilar 02: Armazenamento em Nuvem, Drive Corporativo & Documentos | **SaaS Substituído:** `Penso Drive Enterprise`  
> **Licença OSI:** `Apache-2.0` | **Hardware Recomendado:** `1 vCPU / 1 GB RAM / Armazenamento nativo / S3`  

---

## 1. Visão Geral & Papel no Ecossistema
Gerencia arquivos em nuvem com arquitetura de microserviços e alta concorrência de usuários. Binário único em Go que orquestra serviços de metadados, armazenamento e API OIDC.

---

## 2. Instalação e Deploy em Produção na VPS

### Passo 1: Preparação do Diretório & Rede
```bash
mkdir -p /opt/owncloud-ocis && cd /opt/owncloud-ocis
docker network create ecosystem_net || true
```

### Passo 2: Arquivo de Variáveis de Ambiente (.env)
```bash
cat <<EOF > .env
APP_NAME=ownCloud Infinite Scale (oCIS)
APP_PORT=8080
DATABASE_URL=postgresql://user:secret@postgres:5432/db_owncloud-ocis
SECRET_KEY=$(openssl rand -hex 32)
EOF
```

### Passo 3: Manifesto docker-compose.yml
```yaml
version: '3.8'
services:
  owncloud-ocis:
    image: owncloud/ocis:latest
    restart: unless-stopped
    env_file: .env
    volumes:
      - ./owncloud-ocis_data:/data
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

> **Garantia de Zero Efeito Colateral:** A remoção deste módulo afeta exclusivamente os contêineres e pastas de `/opt/owncloud-ocis`. Nenhum outro banco de dados, proxy Traefik ou aplicação rodando na mesma VPS será impactado.

1. **Parada dos Contêineres:**
   ```bash
   cd /opt/owncloud-ocis && docker compose down
   ```
2. **Remoção de Volumes e Dados:**
   ```bash
   cd /opt && rm -rf /opt/owncloud-ocis
   docker volume rm owncloud-ocis_data 2>/dev/null || true
   ```
3. **Limpeza de Portas e Checklist:**
   ```bash
   docker ps | grep owncloud-ocis
   ```

---

## 4. Rotina de Backup & Disaster Recovery
```bash
tar -czf /var/backups/owncloud-ocis-$(date +%Y%m%d).tar.gz -C /opt/owncloud-ocis .
openssl enc -aes-256-cbc -salt -in /var/backups/owncloud-ocis-$(date +%Y%m%d).tar.gz -out /var/backups/owncloud-ocis-$(date +%Y%m%d).enc -k SegredoBackup2026
```
