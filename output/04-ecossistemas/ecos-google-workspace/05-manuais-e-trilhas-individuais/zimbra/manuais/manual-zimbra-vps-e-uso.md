# Manual de Engenharia de VPS & Desinstalação Cirúrgica: Zimbra Collaboration

> **Ferramenta:** Zimbra Collaboration (Groupware Empresarial Maduro para Grandes Operações)  
> **Pilar do Ecossistema:** Grupo 1: Comunicação Unificada (E-mail, Chat, Vídeo, Agenda & Contatos) | **SaaS Substituído:** `Gmail + Google Calendar + Google Contacts (carga enterprise)`  
> **Licença OSI:** `GPL-3.0` | **Hardware Recomendado:** `4 vCPU / 8 GB RAM RAM / PostgreSQL / MariaDB`  

---

## 1. Visão Geral & Papel no Ecossistema
Gerencia e-mail, agenda, contatos, tarefas e documentos colaborativos em um único servidor. Java (Jetty/Tomcat) com armazenamento em PostgreSQL e servidor de e-mail baseado em Postfix/OpenLDAP.

---

## 2. Instalação e Deploy em Produção na VPS

### Passo 1: Preparação do Diretório & Rede
```bash
mkdir -p /opt/zimbra && cd /opt/zimbra
docker network create ecosystem_net || true
```

### Passo 2: Arquivo de Variáveis de Ambiente (.env)
```bash
cat <<EOF > .env
APP_NAME=Zimbra Collaboration
APP_PORT=8080
DATABASE_URL=postgresql://user:secret@postgres:5432/db_zimbra
SECRET_KEY=$(openssl rand -hex 32)
EOF
```

### Passo 3: Manifesto docker-compose.yml
```yaml
version: '3.8'
services:
  zimbra:
    image: zimbra/zimbra-community:latest
    restart: unless-stopped
    env_file: .env
    volumes:
      - ./zimbra_data:/data
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

> **Garantia de Zero Efeito Colateral:** A remoção deste módulo afeta exclusivamente os contêineres e pastas de `/opt/zimbra`. Nenhum outro banco de dados, proxy Traefik ou aplicação rodando na mesma VPS será impactado.

1. **Parada dos Contêineres:**
   ```bash
   cd /opt/zimbra && docker compose down
   ```
2. **Remoção de Volumes e Dados:**
   ```bash
   cd /opt && rm -rf /opt/zimbra
   docker volume rm zimbra_data 2>/dev/null || true
   ```
3. **Limpeza de Portas e Checklist:**
   ```bash
   docker ps | grep zimbra
   ```

---

## 4. Rotina de Backup & Disaster Recovery
```bash
tar -czf /var/backups/zimbra-$(date +%Y%m%d).tar.gz -C /opt/zimbra .
openssl enc -aes-256-cbc -salt -in /var/backups/zimbra-$(date +%Y%m%d).tar.gz -out /var/backups/zimbra-$(date +%Y%m%d).enc -k SegredoBackup2026
```
