# Manual de Engenharia de VPS & Desinstalação Cirúrgica: Seafile

> **Ferramenta:** Seafile (Armazenamento de Arquivos de Altíssima Performance)  
> **Pilar do Ecossistema:** Grupo 2: Produtividade & Gestão de Documentos (Drive, Docs, Sheets, Slides, Forms, Keep, Sites) | **SaaS Substituído:** `Google Drive (sincronização e backup de arquivos)`  
> **Licença OSI:** `Apache-2.0` | **Hardware Recomendado:** `1 vCPU / 1 GB RAM RAM / MySQL / MariaDB`  

---

## 1. Visão Geral & Papel no Ecossistema
Sincroniza e versiona arquivos com biblioteca de blocos e criptografia no cliente. Backend em C (ccnet/seafile) com banco MySQL e armazenamento de blocos em disco.

---

## 2. Instalação e Deploy em Produção na VPS

### Passo 1: Preparação do Diretório & Rede
```bash
mkdir -p /opt/seafile && cd /opt/seafile
docker network create ecosystem_net || true
```

### Passo 2: Arquivo de Variáveis de Ambiente (.env)
```bash
cat <<EOF > .env
APP_NAME=Seafile
APP_PORT=8080
DATABASE_URL=postgresql://user:secret@postgres:5432/db_seafile
SECRET_KEY=$(openssl rand -hex 32)
EOF
```

### Passo 3: Manifesto docker-compose.yml
```yaml
version: '3.8'
services:
  seafile:
    image: seafileltd/seafile-mc:latest
    restart: unless-stopped
    env_file: .env
    volumes:
      - ./seafile_data:/data
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

> **Garantia de Zero Efeito Colateral:** A remoção deste módulo afeta exclusivamente os contêineres e pastas de `/opt/seafile`. Nenhum outro banco de dados, proxy Traefik ou aplicação rodando na mesma VPS será impactado.

1. **Parada dos Contêineres:**
   ```bash
   cd /opt/seafile && docker compose down
   ```
2. **Remoção de Volumes e Dados:**
   ```bash
   cd /opt && rm -rf /opt/seafile
   docker volume rm seafile_data 2>/dev/null || true
   ```
3. **Limpeza de Portas e Checklist:**
   ```bash
   docker ps | grep seafile
   ```

---

## 4. Rotina de Backup & Disaster Recovery
```bash
tar -czf /var/backups/seafile-$(date +%Y%m%d).tar.gz -C /opt/seafile .
openssl enc -aes-256-cbc -salt -in /var/backups/seafile-$(date +%Y%m%d).tar.gz -out /var/backups/seafile-$(date +%Y%m%d).enc -k SegredoBackup2026
```
