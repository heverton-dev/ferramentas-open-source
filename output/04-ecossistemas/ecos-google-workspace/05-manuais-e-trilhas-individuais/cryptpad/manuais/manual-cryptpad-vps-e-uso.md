# Manual de Engenharia de VPS & Desinstalação Cirúrgica: CryptPad

> **Ferramenta:** CryptPad (Suíte Office Criptografada de Ponta a Ponta (Drive, Docs, Sheets, Slides, Forms))  
> **Pilar do Ecossistema:** Grupo 2: Produtividade & Gestão de Documentos (Drive, Docs, Sheets, Slides, Forms, Keep, Sites) | **SaaS Substituído:** `Google Drive + Docs + Sheets + Slides + Forms + Keep`  
> **Licença OSI:** `AGPL-3.0` | **Hardware Recomendado:** `2 vCPU / 2 GB RAM RAM / Arquivos no disco (sem DB externo)`  

---

## 1. Visão Geral & Papel no Ecossistema
Fornece editor de documentos, planilhas, slides, formulários e armazenamento criptografado com colaboração em tempo real. Node.js com criptografia client-side (ChainPad) e sincronização via WebSocket, sem leitura do servidor.

---

## 2. Instalação e Deploy em Produção na VPS

### Passo 1: Preparação do Diretório & Rede
```bash
mkdir -p /opt/cryptpad && cd /opt/cryptpad
docker network create ecosystem_net || true
```

### Passo 2: Arquivo de Variáveis de Ambiente (.env)
```bash
cat <<EOF > .env
APP_NAME=CryptPad
APP_PORT=8080
DATABASE_URL=postgresql://user:secret@postgres:5432/db_cryptpad
SECRET_KEY=$(openssl rand -hex 32)
EOF
```

### Passo 3: Manifesto docker-compose.yml
```yaml
version: '3.8'
services:
  cryptpad:
    image: cryptpad/cryptpad:latest
    restart: unless-stopped
    env_file: .env
    volumes:
      - ./cryptpad_data:/data
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

> **Garantia de Zero Efeito Colateral:** A remoção deste módulo afeta exclusivamente os contêineres e pastas de `/opt/cryptpad`. Nenhum outro banco de dados, proxy Traefik ou aplicação rodando na mesma VPS será impactado.

1. **Parada dos Contêineres:**
   ```bash
   cd /opt/cryptpad && docker compose down
   ```
2. **Remoção de Volumes e Dados:**
   ```bash
   cd /opt && rm -rf /opt/cryptpad
   docker volume rm cryptpad_data 2>/dev/null || true
   ```
3. **Limpeza de Portas e Checklist:**
   ```bash
   docker ps | grep cryptpad
   ```

---

## 4. Rotina de Backup & Disaster Recovery
```bash
tar -czf /var/backups/cryptpad-$(date +%Y%m%d).tar.gz -C /opt/cryptpad .
openssl enc -aes-256-cbc -salt -in /var/backups/cryptpad-$(date +%Y%m%d).tar.gz -out /var/backups/cryptpad-$(date +%Y%m%d).enc -k SegredoBackup2026
```
