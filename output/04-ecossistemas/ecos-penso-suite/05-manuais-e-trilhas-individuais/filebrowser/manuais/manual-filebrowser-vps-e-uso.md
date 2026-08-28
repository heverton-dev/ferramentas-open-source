# Manual de Engenharia de VPS & Desinstalação Cirúrgica: Filebrowser

> **Ferramenta:** Filebrowser (Gerenciador de Arquivos Web Ultra-Leve em Binário Único Go)  
> **Pilar do Ecossistema:** Pilar 02: Armazenamento em Nuvem, Drive Corporativo & Documentos | **SaaS Substituído:** `Penso Drive Básico`  
> **Licença OSI:** `Apache-2.0` | **Hardware Recomendado:** `0.5 vCPU / 256 MB RAM / SQLite integrado`  

---

## 1. Visão Geral & Papel no Ecossistema
Provê interface web intuitiva para upload, download, pré-visualização de imagens/vídeos e gerenciamento de arquivos na VPS. Binário compilado em Go com banco SQLite e interface SPA em Vue.js.

---

## 2. Instalação e Deploy em Produção na VPS

### Passo 1: Preparação do Diretório & Rede
```bash
mkdir -p /opt/filebrowser && cd /opt/filebrowser
docker network create ecosystem_net || true
```

### Passo 2: Arquivo de Variáveis de Ambiente (.env)
```bash
cat <<EOF > .env
APP_NAME=Filebrowser
APP_PORT=8080
DATABASE_URL=postgresql://user:secret@postgres:5432/db_filebrowser
SECRET_KEY=$(openssl rand -hex 32)
EOF
```

### Passo 3: Manifesto docker-compose.yml
```yaml
version: '3.8'
services:
  filebrowser:
    image: filebrowser/filebrowser:latest
    restart: unless-stopped
    env_file: .env
    volumes:
      - ./filebrowser_data:/data
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

> **Garantia de Zero Efeito Colateral:** A remoção deste módulo afeta exclusivamente os contêineres e pastas de `/opt/filebrowser`. Nenhum outro banco de dados, proxy Traefik ou aplicação rodando na mesma VPS será impactado.

1. **Parada dos Contêineres:**
   ```bash
   cd /opt/filebrowser && docker compose down
   ```
2. **Remoção de Volumes e Dados:**
   ```bash
   cd /opt && rm -rf /opt/filebrowser
   docker volume rm filebrowser_data 2>/dev/null || true
   ```
3. **Limpeza de Portas e Checklist:**
   ```bash
   docker ps | grep filebrowser
   ```

---

## 4. Rotina de Backup & Disaster Recovery
```bash
tar -czf /var/backups/filebrowser-$(date +%Y%m%d).tar.gz -C /opt/filebrowser .
openssl enc -aes-256-cbc -salt -in /var/backups/filebrowser-$(date +%Y%m%d).tar.gz -out /var/backups/filebrowser-$(date +%Y%m%d).enc -k SegredoBackup2026
```
