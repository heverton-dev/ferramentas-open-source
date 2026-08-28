# Manual de Engenharia de VPS & Desinstalação Cirúrgica: LlamaIndex

> **Ferramenta:** LlamaIndex (Framework de RAG (Retrieval-Augmented Generation) com Vector Stores)  
> **Pilar do Ecossistema:** Grupo 1: Orchestração de Agentes & Modelos LLM | **SaaS Substituído:** `Anthropic Claude Code / Knowledge Base Built-in`  
> **Licença OSI:** `MIT` | **Hardware Recomendado:** `1 vCPU / 2 GB RAM RAM / PostgreSQL / SQLite`  

---

## 1. Visão Geral & Papel no Ecossistema
Ingere documentos, cria índices vetoriais e recupera contexto relevante para agentes consultarem bases de conhecimento. SDK Python com suporte a loaders de múltiplos formatos (PDF, Docx, HTML) e integração com vector stores (Pinecone, Weaviate, Chroma).

---

## 2. Instalação e Deploy em Produção na VPS

### Passo 1: Preparação do Diretório & Rede
```bash
mkdir -p /opt/llamaindex && cd /opt/llamaindex
docker network create ecosystem_net || true
```

### Passo 2: Arquivo de Variáveis de Ambiente (.env)
```bash
cat <<EOF > .env
APP_NAME=LlamaIndex
APP_PORT=8080
DATABASE_URL=postgresql://user:secret@postgres:5432/db_llamaindex
SECRET_KEY=$(openssl rand -hex 32)
EOF
```

### Passo 3: Manifesto docker-compose.yml
```yaml
version: '3.8'
services:
  llamaindex:
    image: llamaindex:latest
    restart: unless-stopped
    env_file: .env
    volumes:
      - ./llamaindex_data:/data
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

> **Garantia de Zero Efeito Colateral:** A remoção deste módulo afeta exclusivamente os contêineres e pastas de `/opt/llamaindex`. Nenhum outro banco de dados, proxy Traefik ou aplicação rodando na mesma VPS será impactado.

1. **Parada dos Contêineres:**
   ```bash
   cd /opt/llamaindex && docker compose down
   ```
2. **Remoção de Volumes e Dados:**
   ```bash
   cd /opt && rm -rf /opt/llamaindex
   docker volume rm llamaindex_data 2>/dev/null || true
   ```
3. **Limpeza de Portas e Checklist:**
   ```bash
   docker ps | grep llamaindex
   ```

---

## 4. Rotina de Backup & Disaster Recovery
```bash
tar -czf /var/backups/llamaindex-$(date +%Y%m%d).tar.gz -C /opt/llamaindex .
openssl enc -aes-256-cbc -salt -in /var/backups/llamaindex-$(date +%Y%m%d).tar.gz -out /var/backups/llamaindex-$(date +%Y%m%d).enc -k SegredoBackup2026
```
