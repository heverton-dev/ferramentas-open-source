# Manual de Engenharia de VPS & Desinstalação Cirúrgica: EspoCRM

> **Ferramenta:** EspoCRM (Motor de Regras Corporativas B2B & Workflows)  
> **Pilar do Ecossistema:** Grupo 2: Pipeline Comercial, CRM & Contratos | **SaaS Substituído:** `RD Station CRM (Módulos Corporativos Avançados & Múltiplos Pipelines)`  
> **Licença OSI:** `GPL-3.0` | **Hardware Recomendado:** `1 vCPU / 2 GB RAM RAM / PostgreSQL / SQLite`  

---

## 1. Visão Geral & Papel no Ecossistema
Permite modelar entidades customizadas e fluxos BPM para grandes operações comerciais. PHP/MySQL com construtor no-code de layouts e entidades relacionais.

---

## 2. Instalação e Deploy em Produção na VPS

### Passo 1: Preparação do Diretório & Rede
```bash
mkdir -p /opt/espocrm && cd /opt/espocrm
docker network create ecosystem_net || true
```

### Passo 2: Arquivo de Variáveis de Ambiente (.env)
```bash
cat <<EOF > .env
APP_NAME=EspoCRM
APP_PORT=8080
DATABASE_URL=postgresql://user:secret@postgres:5432/db_espocrm
SECRET_KEY=$(openssl rand -hex 32)
EOF
```

### Passo 3: Manifesto docker-compose.yml
```yaml
version: '3.8'
services:
  espocrm:
    image: espocrm:latest
    restart: unless-stopped
    env_file: .env
    volumes:
      - ./espocrm_data:/data
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

> **Garantia de Zero Efeito Colateral:** A remoção deste módulo afeta exclusivamente os contêineres e pastas de `/opt/espocrm`. Nenhum outro banco de dados, proxy Traefik ou aplicação rodando na mesma VPS será impactado.

1. **Parada dos Contêineres:**
   ```bash
   cd /opt/espocrm && docker compose down
   ```
2. **Remoção de Volumes e Dados:**
   ```bash
   cd /opt && rm -rf /opt/espocrm
   docker volume rm espocrm_data 2>/dev/null || true
   ```
3. **Limpeza de Portas e Checklist:**
   ```bash
   docker ps | grep espocrm
   ```

---

## 4. Rotina de Backup & Disaster Recovery
```bash
tar -czf /var/backups/espocrm-$(date +%Y%m%d).tar.gz -C /opt/espocrm .
openssl enc -aes-256-cbc -salt -in /var/backups/espocrm-$(date +%Y%m%d).tar.gz -out /var/backups/espocrm-$(date +%Y%m%d).enc -k SegredoBackup2026
```
