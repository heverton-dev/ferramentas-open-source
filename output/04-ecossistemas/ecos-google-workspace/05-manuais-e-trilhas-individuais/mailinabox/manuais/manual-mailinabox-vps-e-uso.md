# Manual de Engenharia de VPS & Desinstalação Cirúrgica: Mail-in-a-Box

> **Ferramenta:** Mail-in-a-Box (Servidor de E-mail Completo com Instalação de 1 Script)  
> **Pilar do Ecossistema:** Grupo 1: Comunicação Unificada (E-mail, Chat, Vídeo, Agenda & Contatos) | **SaaS Substituído:** `Gmail + Google Calendar + Google Contacts (instalação zero-config)`  
> **Licença OSI:** `GPL-3.0` | **Hardware Recomendado:** `1 vCPU / 1 GB RAM RAM / SQLite / MariaDB`  

---

## 1. Visão Geral & Papel no Ecossistema
Instala e mantém um servidor de e-mail corporativo completo e seguro com um comando. Script Bash que provisiona Postfix, Dovecot, Nextcloud (agenda/contatos) e Roundcube sobre Ubuntu.

---

## 2. Instalação e Deploy em Produção na VPS

### Passo 1: Preparação do Diretório & Rede
```bash
mkdir -p /opt/mailinabox && cd /opt/mailinabox
docker network create ecosystem_net || true
```

### Passo 2: Arquivo de Variáveis de Ambiente (.env)
```bash
cat <<EOF > .env
APP_NAME=Mail-in-a-Box
APP_PORT=8080
DATABASE_URL=postgresql://user:secret@postgres:5432/db_mailinabox
SECRET_KEY=$(openssl rand -hex 32)
EOF
```

### Passo 3: Manifesto docker-compose.yml
```yaml
version: '3.8'
services:
  mailinabox:
    image: script nativo Ubuntu
    restart: unless-stopped
    env_file: .env
    volumes:
      - ./mailinabox_data:/data
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

> **Garantia de Zero Efeito Colateral:** A remoção deste módulo afeta exclusivamente os contêineres e pastas de `/opt/mailinabox`. Nenhum outro banco de dados, proxy Traefik ou aplicação rodando na mesma VPS será impactado.

1. **Parada dos Contêineres:**
   ```bash
   cd /opt/mailinabox && docker compose down
   ```
2. **Remoção de Volumes e Dados:**
   ```bash
   cd /opt && rm -rf /opt/mailinabox
   docker volume rm mailinabox_data 2>/dev/null || true
   ```
3. **Limpeza de Portas e Checklist:**
   ```bash
   docker ps | grep mailinabox
   ```

---

## 4. Rotina de Backup & Disaster Recovery
```bash
tar -czf /var/backups/mailinabox-$(date +%Y%m%d).tar.gz -C /opt/mailinabox .
openssl enc -aes-256-cbc -salt -in /var/backups/mailinabox-$(date +%Y%m%d).tar.gz -out /var/backups/mailinabox-$(date +%Y%m%d).enc -k SegredoBackup2026
```
