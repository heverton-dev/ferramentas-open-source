# Manual de Engenharia de VPS & Desinstalação Cirúrgica: Ollama

> **Ferramenta:** Ollama (Executor Local de Modelos LLM Abertos (Llama 2, Mistral, Neural Chat))  
> **Pilar do Ecossistema:** Grupo 1: Orchestração de Agentes & Modelos LLM | **SaaS Substituído:** `Anthropic Claude API (Tier Enterprise / Managed Agents)`  
> **Licença OSI:** `MIT` | **Hardware Recomendado:** `1 vCPU / 8 GB RAM RAM / PostgreSQL / SQLite`  

---

## 1. Visão Geral & Papel no Ecossistema
Fornece CLI e servidor HTTP para executar modelos LLM abertos em uma única máquina ou cluster. Binário Go estático que compacta modelos em formato proprietário otimizado e executa inferência em paralelo com quantização.

---

## 2. Instalação e Deploy em Produção na VPS

### Passo 1: Preparação do Diretório & Rede
```bash
mkdir -p /opt/ollama && cd /opt/ollama
docker network create ecosystem_net || true
```

### Passo 2: Arquivo de Variáveis de Ambiente (.env)
```bash
cat <<EOF > .env
APP_NAME=Ollama
APP_PORT=8080
DATABASE_URL=postgresql://user:secret@postgres:5432/db_ollama
SECRET_KEY=$(openssl rand -hex 32)
EOF
```

### Passo 3: Manifesto docker-compose.yml
```yaml
version: '3.8'
services:
  ollama:
    image: ollama:latest
    restart: unless-stopped
    env_file: .env
    volumes:
      - ./ollama_data:/data
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

> **Garantia de Zero Efeito Colateral:** A remoção deste módulo afeta exclusivamente os contêineres e pastas de `/opt/ollama`. Nenhum outro banco de dados, proxy Traefik ou aplicação rodando na mesma VPS será impactado.

1. **Parada dos Contêineres:**
   ```bash
   cd /opt/ollama && docker compose down
   ```
2. **Remoção de Volumes e Dados:**
   ```bash
   cd /opt && rm -rf /opt/ollama
   docker volume rm ollama_data 2>/dev/null || true
   ```
3. **Limpeza de Portas e Checklist:**
   ```bash
   docker ps | grep ollama
   ```

---

## 4. Rotina de Backup & Disaster Recovery
```bash
tar -czf /var/backups/ollama-$(date +%Y%m%d).tar.gz -C /opt/ollama .
openssl enc -aes-256-cbc -salt -in /var/backups/ollama-$(date +%Y%m%d).tar.gz -out /var/backups/ollama-$(date +%Y%m%d).enc -k SegredoBackup2026
```
