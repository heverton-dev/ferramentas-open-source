# Manual de Engenharia de VPS & Desinstalação Cirúrgica: Modoboa

> **Ferramenta:** Modoboa (Plataforma de E-mail Corporativo e Groupware Baseada em Python e Django)  
> **Pilar do Ecossistema:** Pilar 01: E-mail Corporativo, Groupware & Gateway Antispam | **SaaS Substituído:** `Penso Mail Básico`  
> **Licença OSI:** `ISC` | **Hardware Recomendado:** `1 vCPU / 2 GB RAM / PostgreSQL`  

---

## 1. Visão Geral & Papel no Ecossistema
Fornece interface web completa para gestão de correio, quarentena de spam e estatísticas de tráfego. Integra Postfix, Dovecot, Amavis/Rspamd e banco PostgreSQL através de uma API em Django.

---

## 2. Instalação e Deploy em Produção na VPS

### Passo 1: Preparação do Diretório & Rede
```bash
mkdir -p /opt/modoboa && cd /opt/modoboa
docker network create ecosystem_net || true
```

### Passo 2: Arquivo de Variáveis de Ambiente (.env)
```bash
cat <<EOF > .env
APP_NAME=Modoboa
APP_PORT=8080
DATABASE_URL=postgresql://user:secret@postgres:5432/db_modoboa
SECRET_KEY=$(openssl rand -hex 32)
EOF
```

### Passo 3: Manifesto docker-compose.yml
```yaml
version: '3.8'
services:
  modoboa:
    image: modoboa/modoboa:latest
    restart: unless-stopped
    env_file: .env
    volumes:
      - ./modoboa_data:/data
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

> **Garantia de Zero Efeito Colateral:** A remoção deste módulo afeta exclusivamente os contêineres e pastas de `/opt/modoboa`. Nenhum outro banco de dados, proxy Traefik ou aplicação rodando na mesma VPS será impactado.

1. **Parada dos Contêineres:**
   ```bash
   cd /opt/modoboa && docker compose down
   ```
2. **Remoção de Volumes e Dados:**
   ```bash
   cd /opt && rm -rf /opt/modoboa
   docker volume rm modoboa_data 2>/dev/null || true
   ```
3. **Limpeza de Portas e Checklist:**
   ```bash
   docker ps | grep modoboa
   ```

---

## 4. Rotina de Backup & Disaster Recovery
```bash
tar -czf /var/backups/modoboa-$(date +%Y%m%d).tar.gz -C /opt/modoboa .
openssl enc -aes-256-cbc -salt -in /var/backups/modoboa-$(date +%Y%m%d).tar.gz -out /var/backups/modoboa-$(date +%Y%m%d).enc -k SegredoBackup2026
```
