# Manual de Engenharia de VPS & Desinstalação Cirúrgica: Plunk

> **Ferramenta:** Plunk (Automação de E-mails Minimalista & Rápida)  
> **Pilar do Ecossistema:** Grupo 1: Marketing, Nutrição & Landing Pages | **SaaS Substituído:** `RD Station Marketing (Plano Light / Automações Básicas)`  
> **Licença OSI:** `MIT` | **Hardware Recomendado:** `1 vCPU / 1 GB RAM RAM / PostgreSQL / SQLite`  

---

## 1. Visão Geral & Papel no Ecossistema
Envia e-mails transacionais e executa sequências simples baseadas em eventos de produto. Backend em Node.js com banco PostgreSQL e dashboard em React.

---

## 2. Instalação e Deploy em Produção na VPS

### Passo 1: Preparação do Diretório & Rede
```bash
mkdir -p /opt/plunk && cd /opt/plunk
docker network create ecosystem_net || true
```

### Passo 2: Arquivo de Variáveis de Ambiente (.env)
```bash
cat <<EOF > .env
APP_NAME=Plunk
APP_PORT=8080
DATABASE_URL=postgresql://user:secret@postgres:5432/db_plunk
SECRET_KEY=$(openssl rand -hex 32)
EOF
```

### Passo 3: Manifesto docker-compose.yml
```yaml
version: '3.8'
services:
  plunk:
    image: plunk:latest
    restart: unless-stopped
    env_file: .env
    volumes:
      - ./plunk_data:/data
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

> **Garantia de Zero Efeito Colateral:** A remoção deste módulo afeta exclusivamente os contêineres e pastas de `/opt/plunk`. Nenhum outro banco de dados, proxy Traefik ou aplicação rodando na mesma VPS será impactado.

1. **Parada dos Contêineres:**
   ```bash
   cd /opt/plunk && docker compose down
   ```
2. **Remoção de Volumes e Dados:**
   ```bash
   cd /opt && rm -rf /opt/plunk
   docker volume rm plunk_data 2>/dev/null || true
   ```
3. **Limpeza de Portas e Checklist:**
   ```bash
   docker ps | grep plunk
   ```

---

## 4. Rotina de Backup & Disaster Recovery
```bash
tar -czf /var/backups/plunk-$(date +%Y%m%d).tar.gz -C /opt/plunk .
openssl enc -aes-256-cbc -salt -in /var/backups/plunk-$(date +%Y%m%d).tar.gz -out /var/backups/plunk-$(date +%Y%m%d).enc -k SegredoBackup2026
```
