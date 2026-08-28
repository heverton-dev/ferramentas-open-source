# Manual de Engenharia de VPS & Desinstalação Cirúrgica: Jitsi Meet

> **Ferramenta:** Jitsi Meet (Servidor de Videoconferência Criptografada HD sem Limite de Duração)  
> **Pilar do Ecossistema:** Pilar 03: Comunicação Unificada, Chat Corporativo & Videoconferência | **SaaS Substituído:** `Penso Meet / Zoom Pro / Google Meet`  
> **Licença OSI:** `Apache-2.0` | **Hardware Recomendado:** `2 vCPU / 2 GB RAM / Prosody XMPP integrado`  

---

## 1. Visão Geral & Papel no Ecossistema
Transmite áudio e vídeo de alta qualidade com salas protegidas por senha e sala de espera. Arquitetura WebRTC escalável com Jitsi Videobridge (JVB), Prosody XMPP e Jicofo em contêineres Docker.

---

## 2. Instalação e Deploy em Produção na VPS

### Passo 1: Preparação do Diretório & Rede
```bash
mkdir -p /opt/jitsi-meet && cd /opt/jitsi-meet
docker network create ecosystem_net || true
```

### Passo 2: Arquivo de Variáveis de Ambiente (.env)
```bash
cat <<EOF > .env
APP_NAME=Jitsi Meet
APP_PORT=8080
DATABASE_URL=postgresql://user:secret@postgres:5432/db_jitsi-meet
SECRET_KEY=$(openssl rand -hex 32)
EOF
```

### Passo 3: Manifesto docker-compose.yml
```yaml
version: '3.8'
services:
  jitsi-meet:
    image: jitsi/web:latest
    restart: unless-stopped
    env_file: .env
    volumes:
      - ./jitsi-meet_data:/data
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

> **Garantia de Zero Efeito Colateral:** A remoção deste módulo afeta exclusivamente os contêineres e pastas de `/opt/jitsi-meet`. Nenhum outro banco de dados, proxy Traefik ou aplicação rodando na mesma VPS será impactado.

1. **Parada dos Contêineres:**
   ```bash
   cd /opt/jitsi-meet && docker compose down
   ```
2. **Remoção de Volumes e Dados:**
   ```bash
   cd /opt && rm -rf /opt/jitsi-meet
   docker volume rm jitsi-meet_data 2>/dev/null || true
   ```
3. **Limpeza de Portas e Checklist:**
   ```bash
   docker ps | grep jitsi-meet
   ```

---

## 4. Rotina de Backup & Disaster Recovery
```bash
tar -czf /var/backups/jitsi-meet-$(date +%Y%m%d).tar.gz -C /opt/jitsi-meet .
openssl enc -aes-256-cbc -salt -in /var/backups/jitsi-meet-$(date +%Y%m%d).tar.gz -out /var/backups/jitsi-meet-$(date +%Y%m%d).enc -k SegredoBackup2026
```
