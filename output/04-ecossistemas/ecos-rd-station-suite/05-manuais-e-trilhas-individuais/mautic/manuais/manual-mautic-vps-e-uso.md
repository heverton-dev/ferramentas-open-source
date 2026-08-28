# Manual de Engenharia de VPS & Desinstalação Cirúrgica: Mautic

> **Ferramenta:** Mautic (Automação de Marketing & Jornadas de Nutrição)  
> **Pilar do Ecossistema:** Grupo 1: Marketing, Nutrição & Landing Pages | **SaaS Substituído:** `RD Station Marketing (Módulo de Automação de Fluxos & Lead Scoring)`  
> **Licença OSI:** `GPL-3.0` | **Hardware Recomendado:** `1 vCPU / 4 GB RAM RAM / PostgreSQL / SQLite`  

---

## 1. Visão Geral & Papel no Ecossistema
Gerencia campanhas multicanal, pontua leads por interesse e aciona gatilhos de nutrição automática. Backend em PHP/Symfony com orquestrador visual de jornadas em árvore e integração de rastreamento no site.

---

## 2. Instalação e Deploy em Produção na VPS

### Passo 1: Preparação do Diretório & Rede
```bash
mkdir -p /opt/mautic && cd /opt/mautic
docker network create ecosystem_net || true
```

### Passo 2: Arquivo de Variáveis de Ambiente (.env)
```bash
cat <<EOF > .env
APP_NAME=Mautic
APP_PORT=8080
DATABASE_URL=postgresql://user:secret@postgres:5432/db_mautic
SECRET_KEY=$(openssl rand -hex 32)
EOF
```

### Passo 3: Manifesto docker-compose.yml
```yaml
version: '3.8'
services:
  mautic:
    image: mautic:latest
    restart: unless-stopped
    env_file: .env
    volumes:
      - ./mautic_data:/data
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

> **Garantia de Zero Efeito Colateral:** A remoção deste módulo afeta exclusivamente os contêineres e pastas de `/opt/mautic`. Nenhum outro banco de dados, proxy Traefik ou aplicação rodando na mesma VPS será impactado.

1. **Parada dos Contêineres:**
   ```bash
   cd /opt/mautic && docker compose down
   ```
2. **Remoção de Volumes e Dados:**
   ```bash
   cd /opt && rm -rf /opt/mautic
   docker volume rm mautic_data 2>/dev/null || true
   ```
3. **Limpeza de Portas e Checklist:**
   ```bash
   docker ps | grep mautic
   ```

---

## 4. Rotina de Backup & Disaster Recovery
```bash
tar -czf /var/backups/mautic-$(date +%Y%m%d).tar.gz -C /opt/mautic .
openssl enc -aes-256-cbc -salt -in /var/backups/mautic-$(date +%Y%m%d).tar.gz -out /var/backups/mautic-$(date +%Y%m%d).enc -k SegredoBackup2026
```
