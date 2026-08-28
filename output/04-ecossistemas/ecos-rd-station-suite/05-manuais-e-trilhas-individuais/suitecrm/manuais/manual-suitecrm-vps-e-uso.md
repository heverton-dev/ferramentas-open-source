# Manual de Engenharia de VPS & Desinstalação Cirúrgica: SuiteCRM

> **Ferramenta:** SuiteCRM (Suíte Completa Enterprise para Grandes Operações de Vendas)  
> **Pilar do Ecossistema:** Grupo 2: Pipeline Comercial, CRM & Contratos | **SaaS Substituído:** `Salesforce Sales Cloud / SugarCRM Enterprise`  
> **Licença OSI:** `AGPL-3.0` | **Hardware Recomendado:** `1 vCPU / 4 GB RAM RAM / PostgreSQL / SQLite`  

---

## 1. Visão Geral & Papel no Ecossistema
Centraliza todo o ciclo de vida do cliente: da prospecção ao faturamento e suporte técnico. PHP/Symfony com arquitetura robusta e banco relacional MySQL/Postgres.

---

## 2. Instalação e Deploy em Produção na VPS

### Passo 1: Preparação do Diretório & Rede
```bash
mkdir -p /opt/suitecrm && cd /opt/suitecrm
docker network create ecosystem_net || true
```

### Passo 2: Arquivo de Variáveis de Ambiente (.env)
```bash
cat <<EOF > .env
APP_NAME=SuiteCRM
APP_PORT=8080
DATABASE_URL=postgresql://user:secret@postgres:5432/db_suitecrm
SECRET_KEY=$(openssl rand -hex 32)
EOF
```

### Passo 3: Manifesto docker-compose.yml
```yaml
version: '3.8'
services:
  suitecrm:
    image: suitecrm:latest
    restart: unless-stopped
    env_file: .env
    volumes:
      - ./suitecrm_data:/data
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

> **Garantia de Zero Efeito Colateral:** A remoção deste módulo afeta exclusivamente os contêineres e pastas de `/opt/suitecrm`. Nenhum outro banco de dados, proxy Traefik ou aplicação rodando na mesma VPS será impactado.

1. **Parada dos Contêineres:**
   ```bash
   cd /opt/suitecrm && docker compose down
   ```
2. **Remoção de Volumes e Dados:**
   ```bash
   cd /opt && rm -rf /opt/suitecrm
   docker volume rm suitecrm_data 2>/dev/null || true
   ```
3. **Limpeza de Portas e Checklist:**
   ```bash
   docker ps | grep suitecrm
   ```

---

## 4. Rotina de Backup & Disaster Recovery
```bash
tar -czf /var/backups/suitecrm-$(date +%Y%m%d).tar.gz -C /opt/suitecrm .
openssl enc -aes-256-cbc -salt -in /var/backups/suitecrm-$(date +%Y%m%d).tar.gz -out /var/backups/suitecrm-$(date +%Y%m%d).enc -k SegredoBackup2026
```
