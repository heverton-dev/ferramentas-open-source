# Manual de Engenharia de VPS & Desinstalação Cirúrgica: HedgeDoc

> **Ferramenta:** HedgeDoc (Edição Colaborativa de Markdown Simples e Elegante)  
> **Pilar do Ecossistema:** Grupo 2: Produtividade & Gestão de Documentos (Drive, Docs, Sheets, Slides, Forms, Keep, Sites) | **SaaS Substituído:** `Google Docs + Google Keep (notas e documentação leve)`  
> **Licença OSI:** `AGPL-3.0` | **Hardware Recomendado:** `1 vCPU / 1 GB RAM RAM / PostgreSQL / SQLite`  

---

## 1. Visão Geral & Papel no Ecossistema
Permite criar e editar documentos Markdown colaborativos com preview em tempo real. Node.js com banco PostgreSQL e sincronização via WebSocket (ot.js).

---

## 2. Instalação e Deploy em Produção na VPS

### Passo 1: Preparação do Diretório & Rede
```bash
mkdir -p /opt/hedgedoc && cd /opt/hedgedoc
docker network create ecosystem_net || true
```

### Passo 2: Arquivo de Variáveis de Ambiente (.env)
```bash
cat <<EOF > .env
APP_NAME=HedgeDoc
APP_PORT=8080
DATABASE_URL=postgresql://user:secret@postgres:5432/db_hedgedoc
SECRET_KEY=$(openssl rand -hex 32)
EOF
```

### Passo 3: Manifesto docker-compose.yml
```yaml
version: '3.8'
services:
  hedgedoc:
    image: hedgedoc/hedgedoc:latest
    restart: unless-stopped
    env_file: .env
    volumes:
      - ./hedgedoc_data:/data
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

> **Garantia de Zero Efeito Colateral:** A remoção deste módulo afeta exclusivamente os contêineres e pastas de `/opt/hedgedoc`. Nenhum outro banco de dados, proxy Traefik ou aplicação rodando na mesma VPS será impactado.

1. **Parada dos Contêineres:**
   ```bash
   cd /opt/hedgedoc && docker compose down
   ```
2. **Remoção de Volumes e Dados:**
   ```bash
   cd /opt && rm -rf /opt/hedgedoc
   docker volume rm hedgedoc_data 2>/dev/null || true
   ```
3. **Limpeza de Portas e Checklist:**
   ```bash
   docker ps | grep hedgedoc
   ```

---

## 4. Rotina de Backup & Disaster Recovery
```bash
tar -czf /var/backups/hedgedoc-$(date +%Y%m%d).tar.gz -C /opt/hedgedoc .
openssl enc -aes-256-cbc -salt -in /var/backups/hedgedoc-$(date +%Y%m%d).tar.gz -out /var/backups/hedgedoc-$(date +%Y%m%d).enc -k SegredoBackup2026
```
