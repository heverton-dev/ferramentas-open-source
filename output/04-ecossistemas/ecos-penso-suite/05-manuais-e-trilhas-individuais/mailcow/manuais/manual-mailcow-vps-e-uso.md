# Manual de Engenharia de VPS & Desinstalação Cirúrgica: Mailcow: dockerized

> **Ferramenta:** Mailcow: dockerized (Suíte Moderna de E-mail Corporativo com Rspamd, SOGo Groupware e ActiveSync)  
> **Pilar do Ecossistema:** Pilar 01: E-mail Corporativo, Groupware & Gateway Antispam | **SaaS Substituído:** `Penso Mail Enterprise / Zimbra Network Edition`  
> **Licença OSI:** `GPL-3.0` | **Hardware Recomendado:** `2 vCPU / 4 GB RAM / MariaDB / Redis`  

---

## 1. Visão Geral & Papel no Ecossistema
Gerencia caixas postais corporativas, filas SMTP, roteamento de domínios e proteção antispam com aprendizado bayesiano. Orquestração em contêineres Docker interligados por rede interna, utilizando Postfix para MTA, Dovecot para IMAP/LMTP, Nginx para proxy reverso e SOGo para webmail e groupware.

---

## 2. Instalação e Deploy em Produção na VPS

### Passo 1: Preparação do Diretório & Rede
```bash
mkdir -p /opt/mailcow && cd /opt/mailcow
docker network create ecosystem_net || true
```

### Passo 2: Arquivo de Variáveis de Ambiente (.env)
```bash
cat <<EOF > .env
APP_NAME=Mailcow: dockerized
APP_PORT=8080
DATABASE_URL=postgresql://user:secret@postgres:5432/db_mailcow
SECRET_KEY=$(openssl rand -hex 32)
EOF
```

### Passo 3: Manifesto docker-compose.yml
```yaml
version: '3.8'
services:
  mailcow:
    image: mailcow/postfix:latest
    restart: unless-stopped
    env_file: .env
    volumes:
      - ./mailcow_data:/data
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

> **Garantia de Zero Efeito Colateral:** A remoção deste módulo afeta exclusivamente os contêineres e pastas de `/opt/mailcow`. Nenhum outro banco de dados, proxy Traefik ou aplicação rodando na mesma VPS será impactado.

1. **Parada dos Contêineres:**
   ```bash
   cd /opt/mailcow && docker compose down
   ```
2. **Remoção de Volumes e Dados:**
   ```bash
   cd /opt && rm -rf /opt/mailcow
   docker volume rm mailcow_data 2>/dev/null || true
   ```
3. **Limpeza de Portas e Checklist:**
   ```bash
   docker ps | grep mailcow
   ```

---

## 4. Rotina de Backup & Disaster Recovery
```bash
tar -czf /var/backups/mailcow-$(date +%Y%m%d).tar.gz -C /opt/mailcow .
openssl enc -aes-256-cbc -salt -in /var/backups/mailcow-$(date +%Y%m%d).tar.gz -out /var/backups/mailcow-$(date +%Y%m%d).enc -k SegredoBackup2026
```
