# Manual de Engenharia de VPS & Desinstalação Cirúrgica: Cal.com

> **Ferramenta:** Cal.com (Agendamento Automatizado de Demonstrações Comerciais)  
> **Pilar do Ecossistema:** Grupo 2: Pipeline Comercial, CRM & Contratos | **SaaS Substituído:** `RD Station CRM (Agendamentos) / Calendly Integrado`  
> **Licença OSI:** `AGPL-3.0` | **Hardware Recomendado:** `1 vCPU / 2 GB RAM RAM / PostgreSQL / SQLite`  

---

## 1. Visão Geral & Papel no Ecossistema
Disponibiliza links de agendamento conectados à agenda dos vendedores com distribuição round-robin. Next.js e Prisma com sincronização com Google Calendar, Outlook e CalDAV.

---

## 2. Instalação e Deploy em Produção na VPS

### Passo 1: Preparação do Diretório & Rede
```bash
mkdir -p /opt/cal-com && cd /opt/cal-com
docker network create ecosystem_net || true
```

### Passo 2: Arquivo de Variáveis de Ambiente (.env)
```bash
cat <<EOF > .env
APP_NAME=Cal.com
APP_PORT=8080
DATABASE_URL=postgresql://user:secret@postgres:5432/db_cal-com
SECRET_KEY=$(openssl rand -hex 32)
EOF
```

### Passo 3: Manifesto docker-compose.yml
```yaml
version: '3.8'
services:
  cal-com:
    image: cal-com:latest
    restart: unless-stopped
    env_file: .env
    volumes:
      - ./cal-com_data:/data
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

> **Garantia de Zero Efeito Colateral:** A remoção deste módulo afeta exclusivamente os contêineres e pastas de `/opt/cal-com`. Nenhum outro banco de dados, proxy Traefik ou aplicação rodando na mesma VPS será impactado.

1. **Parada dos Contêineres:**
   ```bash
   cd /opt/cal-com && docker compose down
   ```
2. **Remoção de Volumes e Dados:**
   ```bash
   cd /opt && rm -rf /opt/cal-com
   docker volume rm cal-com_data 2>/dev/null || true
   ```
3. **Limpeza de Portas e Checklist:**
   ```bash
   docker ps | grep cal-com
   ```

---

## 4. Rotina de Backup & Disaster Recovery
```bash
tar -czf /var/backups/cal-com-$(date +%Y%m%d).tar.gz -C /opt/cal-com .
openssl enc -aes-256-cbc -salt -in /var/backups/cal-com-$(date +%Y%m%d).tar.gz -out /var/backups/cal-com-$(date +%Y%m%d).enc -k SegredoBackup2026
```
