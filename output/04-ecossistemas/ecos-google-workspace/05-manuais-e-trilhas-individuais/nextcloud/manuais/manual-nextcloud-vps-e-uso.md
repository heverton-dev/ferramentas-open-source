# Manual de Engenharia de VPS & Desinstalação Cirúrgica: Nextcloud Hub

> **Ferramenta:** Nextcloud Hub (Suíte Integrada de Mail, Calendar, Contacts, Talk & Files)  
> **Pilar do Ecossistema:** Grupo 1: Comunicação Unificada (E-mail, Chat, Vídeo, Agenda & Contatos) | **SaaS Substituído:** `Gmail + Google Calendar + Google Contacts + Google Chat + Google Meet`  
> **Licença OSI:** `AGPL-3.0` | **Hardware Recomendado:** `2 vCPU / 4 GB RAM RAM / PostgreSQL / MySQL`  

---

## 1. Visão Geral & Papel no Ecossistema
Centraliza e-mail, agenda, contatos, chat e vídeo com interface única e aplicativos móveis próprios. PHP/Symfony com servidor de sincronização, banco PostgreSQL/MySQL e módulo Talk sobre WebRTC para chamadas.

---

## 2. Instalação e Deploy em Produção na VPS

### Passo 1: Preparação do Diretório & Rede
```bash
mkdir -p /opt/nextcloud && cd /opt/nextcloud
docker network create ecosystem_net || true
```

### Passo 2: Arquivo de Variáveis de Ambiente (.env)
```bash
cat <<EOF > .env
APP_NAME=Nextcloud Hub
APP_PORT=8080
DATABASE_URL=postgresql://user:secret@postgres:5432/db_nextcloud
SECRET_KEY=$(openssl rand -hex 32)
EOF
```

### Passo 3: Manifesto docker-compose.yml
```yaml
version: '3.8'
services:
  nextcloud:
    image: nextcloud:latest
    restart: unless-stopped
    env_file: .env
    volumes:
      - ./nextcloud_data:/data
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

> **Garantia de Zero Efeito Colateral:** A remoção deste módulo afeta exclusivamente os contêineres e pastas de `/opt/nextcloud`. Nenhum outro banco de dados, proxy Traefik ou aplicação rodando na mesma VPS será impactado.

1. **Parada dos Contêineres:**
   ```bash
   cd /opt/nextcloud && docker compose down
   ```
2. **Remoção de Volumes e Dados:**
   ```bash
   cd /opt && rm -rf /opt/nextcloud
   docker volume rm nextcloud_data 2>/dev/null || true
   ```
3. **Limpeza de Portas e Checklist:**
   ```bash
   docker ps | grep nextcloud
   ```

---

## 4. Rotina de Backup & Disaster Recovery
```bash
tar -czf /var/backups/nextcloud-$(date +%Y%m%d).tar.gz -C /opt/nextcloud .
openssl enc -aes-256-cbc -salt -in /var/backups/nextcloud-$(date +%Y%m%d).tar.gz -out /var/backups/nextcloud-$(date +%Y%m%d).enc -k SegredoBackup2026
```
