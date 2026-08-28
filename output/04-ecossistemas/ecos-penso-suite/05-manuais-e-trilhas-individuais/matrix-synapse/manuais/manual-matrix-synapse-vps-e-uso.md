# Manual de Engenharia de VPS & Desinstalação Cirúrgica: Matrix Synapse & Element

> **Ferramenta:** Matrix Synapse & Element (Rede Aberta e Federada de Comunicação Segura com Criptografia Ponta a Ponta)  
> **Pilar do Ecossistema:** Pilar 03: Comunicação Unificada, Chat Corporativo & Videoconferência | **SaaS Substituído:** `Penso Chat Seguro`  
> **Licença OSI:** `Apache-2.0` | **Hardware Recomendado:** `2 vCPU / 2 GB RAM / PostgreSQL`  

---

## 1. Visão Geral & Papel no Ecossistema
Provê servidor de mensageria federada com salas criptografadas, chamadas de áudio/vídeo e controle granular de chaves. Servidor Synapse (Python/Rust) conectado a banco PostgreSQL com cliente web/desktop Element.

---

## 2. Instalação e Deploy em Produção na VPS

### Passo 1: Preparação do Diretório & Rede
```bash
mkdir -p /opt/matrix-synapse && cd /opt/matrix-synapse
docker network create ecosystem_net || true
```

### Passo 2: Arquivo de Variáveis de Ambiente (.env)
```bash
cat <<EOF > .env
APP_NAME=Matrix Synapse & Element
APP_PORT=8080
DATABASE_URL=postgresql://user:secret@postgres:5432/db_matrix-synapse
SECRET_KEY=$(openssl rand -hex 32)
EOF
```

### Passo 3: Manifesto docker-compose.yml
```yaml
version: '3.8'
services:
  matrix-synapse:
    image: matrixdotorg/synapse:latest
    restart: unless-stopped
    env_file: .env
    volumes:
      - ./matrix-synapse_data:/data
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

> **Garantia de Zero Efeito Colateral:** A remoção deste módulo afeta exclusivamente os contêineres e pastas de `/opt/matrix-synapse`. Nenhum outro banco de dados, proxy Traefik ou aplicação rodando na mesma VPS será impactado.

1. **Parada dos Contêineres:**
   ```bash
   cd /opt/matrix-synapse && docker compose down
   ```
2. **Remoção de Volumes e Dados:**
   ```bash
   cd /opt && rm -rf /opt/matrix-synapse
   docker volume rm matrix-synapse_data 2>/dev/null || true
   ```
3. **Limpeza de Portas e Checklist:**
   ```bash
   docker ps | grep matrix-synapse
   ```

---

## 4. Rotina de Backup & Disaster Recovery
```bash
tar -czf /var/backups/matrix-synapse-$(date +%Y%m%d).tar.gz -C /opt/matrix-synapse .
openssl enc -aes-256-cbc -salt -in /var/backups/matrix-synapse-$(date +%Y%m%d).tar.gz -out /var/backups/matrix-synapse-$(date +%Y%m%d).enc -k SegredoBackup2026
```
