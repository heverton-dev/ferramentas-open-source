# Manual de Engenharia de VPS & Desinstalação Cirúrgica: AnythingLLM

> **Ferramenta:** AnythingLLM (RAG Platform All-in-One com Chat Interface)  
> **Pilar do Ecossistema:** Grupo 1: Orchestração de Agentes & Modelos LLM | **SaaS Substituído:** `ChatGPT / Claude Cloud (Knowledge Base)`  
> **Licença OSI:** `MIT` | **Hardware Recomendado:** `1 vCPU / 4 GB RAM RAM / PostgreSQL / SQLite`  

---

## 1. Visão Geral & Papel no Ecossistema
Cria um sistema de chat que responde perguntas sobre documentos corporativos uploadados. Binário Go estático com SQLite embarcado e embeddings locais via Ollama.

---

## 2. Instalação e Deploy em Produção na VPS

### Passo 1: Preparação do Diretório & Rede
```bash
mkdir -p /opt/anythingllm && cd /opt/anythingllm
docker network create ecosystem_net || true
```

### Passo 2: Arquivo de Variáveis de Ambiente (.env)
```bash
cat <<EOF > .env
APP_NAME=AnythingLLM
APP_PORT=8080
DATABASE_URL=postgresql://user:secret@postgres:5432/db_anythingllm
SECRET_KEY=$(openssl rand -hex 32)
EOF
```

### Passo 3: Manifesto docker-compose.yml
```yaml
version: '3.8'
services:
  anythingllm:
    image: anythingllm:latest
    restart: unless-stopped
    env_file: .env
    volumes:
      - ./anythingllm_data:/data
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

> **Garantia de Zero Efeito Colateral:** A remoção deste módulo afeta exclusivamente os contêineres e pastas de `/opt/anythingllm`. Nenhum outro banco de dados, proxy Traefik ou aplicação rodando na mesma VPS será impactado.

1. **Parada dos Contêineres:**
   ```bash
   cd /opt/anythingllm && docker compose down
   ```
2. **Remoção de Volumes e Dados:**
   ```bash
   cd /opt && rm -rf /opt/anythingllm
   docker volume rm anythingllm_data 2>/dev/null || true
   ```
3. **Limpeza de Portas e Checklist:**
   ```bash
   docker ps | grep anythingllm
   ```

---

## 4. Rotina de Backup & Disaster Recovery
```bash
tar -czf /var/backups/anythingllm-$(date +%Y%m%d).tar.gz -C /opt/anythingllm .
openssl enc -aes-256-cbc -salt -in /var/backups/anythingllm-$(date +%Y%m%d).tar.gz -out /var/backups/anythingllm-$(date +%Y%m%d).enc -k SegredoBackup2026
```
