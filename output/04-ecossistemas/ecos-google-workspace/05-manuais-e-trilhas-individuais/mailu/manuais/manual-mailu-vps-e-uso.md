# Manual de Engenharia de VPS & Desinstalação Cirúrgica: Mailu

> **Ferramenta:** Mailu (Servidor de E-mail Dockerizado Leve e Completo)  
> **Pilar do Ecossistema:** Grupo 1: Comunicação Unificada (E-mail, Chat, Vídeo, Agenda & Contatos) | **SaaS Substituído:** `Gmail + Google Calendar + Google Contacts (carga leve)`  
> **Licença OSI:** `MIT` | **Hardware Recomendado:** `1 vCPU / 2 GB RAM RAM / SQLite / PostgreSQL`  

---

## 1. Visão Geral & Papel no Ecossistema
Entrega e-mail, webmail, agenda e contatos com interface administrativa simples. Orquestra Postfix, Dovecot, Roundcube, PostfixAdmin e Redis em contêineres leves sobre Docker.

---

## 2. Instalação e Deploy em Produção na VPS

### Passo 1: Preparação do Diretório & Rede
```bash
mkdir -p /opt/mailu && cd /opt/mailu
docker network create ecosystem_net || true
```

### Passo 2: Arquivo de Variáveis de Ambiente (.env)
```bash
cat <<EOF > .env
APP_NAME=Mailu
APP_PORT=8080
DATABASE_URL=postgresql://user:secret@postgres:5432/db_mailu
SECRET_KEY=$(openssl rand -hex 32)
EOF
```

### Passo 3: Manifesto docker-compose.yml
```yaml
version: '3.8'
services:
  mailu:
    image: mailu/mailu:latest
    restart: unless-stopped
    env_file: .env
    volumes:
      - ./mailu_data:/data
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

> **Garantia de Zero Efeito Colateral:** A remoção deste módulo afeta exclusivamente os contêineres e pastas de `/opt/mailu`. Nenhum outro banco de dados, proxy Traefik ou aplicação rodando na mesma VPS será impactado.

1. **Parada dos Contêineres:**
   ```bash
   cd /opt/mailu && docker compose down
   ```
2. **Remoção de Volumes e Dados:**
   ```bash
   cd /opt && rm -rf /opt/mailu
   docker volume rm mailu_data 2>/dev/null || true
   ```
3. **Limpeza de Portas e Checklist:**
   ```bash
   docker ps | grep mailu
   ```

---

## 4. Rotina de Backup & Disaster Recovery
```bash
tar -czf /var/backups/mailu-$(date +%Y%m%d).tar.gz -C /opt/mailu .
openssl enc -aes-256-cbc -salt -in /var/backups/mailu-$(date +%Y%m%d).tar.gz -out /var/backups/mailu-$(date +%Y%m%d).enc -k SegredoBackup2026
```
