# Manual de Engenharia de VPS & Desinstalação Cirúrgica: LangChain

> **Ferramenta:** LangChain (Framework de Composição de Agentes, Chains & Memory para LLMs)  
> **Pilar do Ecossistema:** Grupo 1: Orchestração de Agentes & Modelos LLM | **SaaS Substituído:** `Anthropic Claude Code / Managed Agents Runtime`  
> **Licença OSI:** `MIT` | **Hardware Recomendado:** `1 vCPU / 2 GB RAM RAM / PostgreSQL / SQLite`  

---

## 1. Visão Geral & Papel no Ecossistema
Fornece abstrações Python e TypeScript para construir agentes de IA compostos com memory e tool calling. SDK Python/TypeScript com suporte nativo a chain execution, memory backends (Redis, PostgreSQL) e vector stores (Pinecone, Weaviate, Milvus).

---

## 2. Instalação e Deploy em Produção na VPS

### Passo 1: Preparação do Diretório & Rede
```bash
mkdir -p /opt/langchain && cd /opt/langchain
docker network create ecosystem_net || true
```

### Passo 2: Arquivo de Variáveis de Ambiente (.env)
```bash
cat <<EOF > .env
APP_NAME=LangChain
APP_PORT=8080
DATABASE_URL=postgresql://user:secret@postgres:5432/db_langchain
SECRET_KEY=$(openssl rand -hex 32)
EOF
```

### Passo 3: Manifesto docker-compose.yml
```yaml
version: '3.8'
services:
  langchain:
    image: langchain:latest
    restart: unless-stopped
    env_file: .env
    volumes:
      - ./langchain_data:/data
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

> **Garantia de Zero Efeito Colateral:** A remoção deste módulo afeta exclusivamente os contêineres e pastas de `/opt/langchain`. Nenhum outro banco de dados, proxy Traefik ou aplicação rodando na mesma VPS será impactado.

1. **Parada dos Contêineres:**
   ```bash
   cd /opt/langchain && docker compose down
   ```
2. **Remoção de Volumes e Dados:**
   ```bash
   cd /opt && rm -rf /opt/langchain
   docker volume rm langchain_data 2>/dev/null || true
   ```
3. **Limpeza de Portas e Checklist:**
   ```bash
   docker ps | grep langchain
   ```

---

## 4. Rotina de Backup & Disaster Recovery
```bash
tar -czf /var/backups/langchain-$(date +%Y%m%d).tar.gz -C /opt/langchain .
openssl enc -aes-256-cbc -salt -in /var/backups/langchain-$(date +%Y%m%d).tar.gz -out /var/backups/langchain-$(date +%Y%m%d).enc -k SegredoBackup2026
```
