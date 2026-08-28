# Manual de Engenharia de VPS & Desinstalação Cirúrgica: ownCloud

> **Ferramenta:** ownCloud (Plataforma Enterprise de Sincronização e Compartilhamento de Arquivos)  
> **Pilar do Ecossistema:** Grupo 2: Produtividade & Gestão de Documentos (Drive, Docs, Sheets, Slides, Forms, Keep, Sites) | **SaaS Substituído:** `Google Drive (armazenamento e compartilhamento empresarial)`  
> **Licença OSI:** `AGPL-3.0` | **Hardware Recomendado:** `2 vCPU / 2 GB RAM RAM / PostgreSQL / MariaDB`  

---

## 1. Visão Geral & Papel no Ecossistema
Sincroniza arquivos entre dispositivos, gerencia compartilhamentos e mantém histórico de versões. PHP/Symfony com armazenamento em disco ou S3 e sincronização via cliente desktop/móvel.

---

## 2. Instalação e Deploy em Produção na VPS

### Passo 1: Preparação do Diretório & Rede
```bash
mkdir -p /opt/owncloud && cd /opt/owncloud
docker network create ecosystem_net || true
```

### Passo 2: Arquivo de Variáveis de Ambiente (.env)
```bash
cat <<EOF > .env
APP_NAME=ownCloud
APP_PORT=8080
DATABASE_URL=postgresql://user:secret@postgres:5432/db_owncloud
SECRET_KEY=$(openssl rand -hex 32)
EOF
```

### Passo 3: Manifesto docker-compose.yml
```yaml
version: '3.8'
services:
  owncloud:
    image: owncloud/server:latest
    restart: unless-stopped
    env_file: .env
    volumes:
      - ./owncloud_data:/data
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

> **Garantia de Zero Efeito Colateral:** A remoção deste módulo afeta exclusivamente os contêineres e pastas de `/opt/owncloud`. Nenhum outro banco de dados, proxy Traefik ou aplicação rodando na mesma VPS será impactado.

1. **Parada dos Contêineres:**
   ```bash
   cd /opt/owncloud && docker compose down
   ```
2. **Remoção de Volumes e Dados:**
   ```bash
   cd /opt && rm -rf /opt/owncloud
   docker volume rm owncloud_data 2>/dev/null || true
   ```
3. **Limpeza de Portas e Checklist:**
   ```bash
   docker ps | grep owncloud
   ```

---

## 4. Rotina de Backup & Disaster Recovery
```bash
tar -czf /var/backups/owncloud-$(date +%Y%m%d).tar.gz -C /opt/owncloud .
openssl enc -aes-256-cbc -salt -in /var/backups/owncloud-$(date +%Y%m%d).tar.gz -out /var/backups/owncloud-$(date +%Y%m%d).enc -k SegredoBackup2026
```
