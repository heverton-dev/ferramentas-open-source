# Manual de Engenharia de VPS & Desinstalação Cirúrgica: Mailu

> **Ferramenta:** Mailu (Servidor de E-mail Leve, Modular e Focado em Simplicidade Operacional)  
> **Pilar do Ecossistema:** Pilar 01: E-mail Corporativo, Groupware & Gateway Antispam | **SaaS Substituído:** `Penso Mail Padrão`  
> **Licença OSI:** `MIT` | **Hardware Recomendado:** `2 vCPU / 2 GB RAM / PostgreSQL / SQLite`  

---

## 1. Visão Geral & Papel no Ecossistema
Entrega servidor de e-mail seguro com suporte a Webmail, antispam, antivírus e administração centralizada. Usa Postfix, Dovecot e Rspamd com gerador de docker-compose oficial para deploy personalizado.

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
    image: mailu/admin:latest
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
