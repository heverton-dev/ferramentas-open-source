# Manual de Engenharia de VPS & Desinstalação Cirúrgica: Documenso

> **Ferramenta:** Documenso (Assinatura Eletrônica Soberana de Contratos e Propostas)  
> **Pilar do Ecossistema:** Grupo 2: Pipeline Comercial, CRM & Contratos | **SaaS Substituído:** `Clicksign / DocuSign / Módulo de Propostas Comerciais`  
> **Licença OSI:** `AGPL-3.0` | **Hardware Recomendado:** `1 vCPU / 2 GB RAM RAM / PostgreSQL / SQLite`  

---

## 1. Visão Geral & Papel no Ecossistema
Gera links de assinatura digital com trilha de auditoria e carimbo do tempo criptográfico. Backend em TypeScript sobre PostgreSQL com geração de hashes SHA-256 dos documentos.

---

## 2. Instalação e Deploy em Produção na VPS

### Passo 1: Preparação do Diretório & Rede
```bash
mkdir -p /opt/documenso && cd /opt/documenso
docker network create ecosystem_net || true
```

### Passo 2: Arquivo de Variáveis de Ambiente (.env)
```bash
cat <<EOF > .env
APP_NAME=Documenso
APP_PORT=8080
DATABASE_URL=postgresql://user:secret@postgres:5432/db_documenso
SECRET_KEY=$(openssl rand -hex 32)
EOF
```

### Passo 3: Manifesto docker-compose.yml
```yaml
version: '3.8'
services:
  documenso:
    image: documenso:latest
    restart: unless-stopped
    env_file: .env
    volumes:
      - ./documenso_data:/data
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

> **Garantia de Zero Efeito Colateral:** A remoção deste módulo afeta exclusivamente os contêineres e pastas de `/opt/documenso`. Nenhum outro banco de dados, proxy Traefik ou aplicação rodando na mesma VPS será impactado.

1. **Parada dos Contêineres:**
   ```bash
   cd /opt/documenso && docker compose down
   ```
2. **Remoção de Volumes e Dados:**
   ```bash
   cd /opt && rm -rf /opt/documenso
   docker volume rm documenso_data 2>/dev/null || true
   ```
3. **Limpeza de Portas e Checklist:**
   ```bash
   docker ps | grep documenso
   ```

---

## 4. Rotina de Backup & Disaster Recovery
```bash
tar -czf /var/backups/documenso-$(date +%Y%m%d).tar.gz -C /opt/documenso .
openssl enc -aes-256-cbc -salt -in /var/backups/documenso-$(date +%Y%m%d).tar.gz -out /var/backups/documenso-$(date +%Y%m%d).enc -k SegredoBackup2026
```
