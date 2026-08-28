# Manual de Engenharia de VPS & Desinstalação Cirúrgica: Flowise

> **Ferramenta:** Flowise (Construtor Visual Drag-and-Drop de Workflows de IA)  
> **Pilar do Ecossistema:** Grupo 1: Orchestração de Agentes & Modelos LLM | **SaaS Substituído:** `Anthropic Claude Code (Visual Agent Builder)`  
> **Licença OSI:** `Apache-2.0` | **Hardware Recomendado:** `1 vCPU / 2 GB RAM RAM / PostgreSQL / SQLite`  

---

## 1. Visão Geral & Papel no Ecossistema
Cria workflows de IA complexos arrastando nós de modelos, tools e lógica condicional. Node.js e React com execução de workflows em background via Bull Queue.

---

## 2. Instalação e Deploy em Produção na VPS

### Passo 1: Preparação do Diretório & Rede
```bash
mkdir -p /opt/flowise && cd /opt/flowise
docker network create ecosystem_net || true
```

### Passo 2: Arquivo de Variáveis de Ambiente (.env)
```bash
cat <<EOF > .env
APP_NAME=Flowise
APP_PORT=8080
DATABASE_URL=postgresql://user:secret@postgres:5432/db_flowise
SECRET_KEY=$(openssl rand -hex 32)
EOF
```

### Passo 3: Manifesto docker-compose.yml
```yaml
version: '3.8'
services:
  flowise:
    image: flowise:latest
    restart: unless-stopped
    env_file: .env
    volumes:
      - ./flowise_data:/data
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

> **Garantia de Zero Efeito Colateral:** A remoção deste módulo afeta exclusivamente os contêineres e pastas de `/opt/flowise`. Nenhum outro banco de dados, proxy Traefik ou aplicação rodando na mesma VPS será impactado.

1. **Parada dos Contêineres:**
   ```bash
   cd /opt/flowise && docker compose down
   ```
2. **Remoção de Volumes e Dados:**
   ```bash
   cd /opt && rm -rf /opt/flowise
   docker volume rm flowise_data 2>/dev/null || true
   ```
3. **Limpeza de Portas e Checklist:**
   ```bash
   docker ps | grep flowise
   ```

---

## 4. Rotina de Backup & Disaster Recovery
```bash
tar -czf /var/backups/flowise-$(date +%Y%m%d).tar.gz -C /opt/flowise .
openssl enc -aes-256-cbc -salt -in /var/backups/flowise-$(date +%Y%m%d).tar.gz -out /var/backups/flowise-$(date +%Y%m%d).enc -k SegredoBackup2026
```
