# Manual de Engenharia de VPS & Desinstalação Cirúrgica: Twenty

> **Ferramenta:** Twenty (CRM Moderno Aberto & Gestão de Funil Comercial)  
> **Pilar do Ecossistema:** Grupo 2: Pipeline Comercial, CRM & Contratos | **SaaS Substituído:** `RD Station CRM (Módulo de Pipeline Kanban, Oportunidades & Tarefas)`  
> **Licença OSI:** `AGPL-3.0` | **Hardware Recomendado:** `1 vCPU / 4 GB RAM RAM / PostgreSQL / SQLite`  

---

## 1. Visão Geral & Papel no Ecossistema
Gerencia oportunidades em funil Kanban com sincronização de e-mail e notas em tempo real. Arquitetura reativa em TypeScript, React, NestJS e PostgreSQL com GraphQL nativo.

---

## 2. Instalação e Deploy em Produção na VPS

### Passo 1: Preparação do Diretório & Rede
```bash
mkdir -p /opt/twenty && cd /opt/twenty
docker network create ecosystem_net || true
```

### Passo 2: Arquivo de Variáveis de Ambiente (.env)
```bash
cat <<EOF > .env
APP_NAME=Twenty
APP_PORT=8080
DATABASE_URL=postgresql://user:secret@postgres:5432/db_twenty
SECRET_KEY=$(openssl rand -hex 32)
EOF
```

### Passo 3: Manifesto docker-compose.yml
```yaml
version: '3.8'
services:
  twenty:
    image: twenty:latest
    restart: unless-stopped
    env_file: .env
    volumes:
      - ./twenty_data:/data
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

> **Garantia de Zero Efeito Colateral:** A remoção deste módulo afeta exclusivamente os contêineres e pastas de `/opt/twenty`. Nenhum outro banco de dados, proxy Traefik ou aplicação rodando na mesma VPS será impactado.

1. **Parada dos Contêineres:**
   ```bash
   cd /opt/twenty && docker compose down
   ```
2. **Remoção de Volumes e Dados:**
   ```bash
   cd /opt && rm -rf /opt/twenty
   docker volume rm twenty_data 2>/dev/null || true
   ```
3. **Limpeza de Portas e Checklist:**
   ```bash
   docker ps | grep twenty
   ```

---

## 4. Rotina de Backup & Disaster Recovery
```bash
tar -czf /var/backups/twenty-$(date +%Y%m%d).tar.gz -C /opt/twenty .
openssl enc -aes-256-cbc -salt -in /var/backups/twenty-$(date +%Y%m%d).tar.gz -out /var/backups/twenty-$(date +%Y%m%d).enc -k SegredoBackup2026
```
