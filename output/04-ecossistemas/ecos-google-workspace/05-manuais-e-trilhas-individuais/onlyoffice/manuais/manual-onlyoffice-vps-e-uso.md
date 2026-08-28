# Manual de Engenharia de VPS & Desinstalação Cirúrgica: ONLYOFFICE Docs

> **Ferramenta:** ONLYOFFICE Docs (Motor de Edição Colaborativa Moderna (Docs, Sheets, Slides))  
> **Pilar do Ecossistema:** Grupo 2: Produtividade & Gestão de Documentos (Drive, Docs, Sheets, Slides, Forms, Keep, Sites) | **SaaS Substituído:** `Google Docs + Sheets + Slides (edição colaborativa)`  
> **Licença OSI:** `AGPL-3.0` | **Hardware Recomendado:** `2 vCPU / 4 GB RAM RAM / Redis (cache) + disco`  

---

## 1. Visão Geral & Papel no Ecossistema
Renderiza e edita documentos, planilhas e apresentações colaborativas no navegador. Node.js + servidores de conversão em C++ com WebSocket para coautoria em tempo real.

---

## 2. Instalação e Deploy em Produção na VPS

### Passo 1: Preparação do Diretório & Rede
```bash
mkdir -p /opt/onlyoffice && cd /opt/onlyoffice
docker network create ecosystem_net || true
```

### Passo 2: Arquivo de Variáveis de Ambiente (.env)
```bash
cat <<EOF > .env
APP_NAME=ONLYOFFICE Docs
APP_PORT=8080
DATABASE_URL=postgresql://user:secret@postgres:5432/db_onlyoffice
SECRET_KEY=$(openssl rand -hex 32)
EOF
```

### Passo 3: Manifesto docker-compose.yml
```yaml
version: '3.8'
services:
  onlyoffice:
    image: onlyoffice/documentserver:latest
    restart: unless-stopped
    env_file: .env
    volumes:
      - ./onlyoffice_data:/data
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

> **Garantia de Zero Efeito Colateral:** A remoção deste módulo afeta exclusivamente os contêineres e pastas de `/opt/onlyoffice`. Nenhum outro banco de dados, proxy Traefik ou aplicação rodando na mesma VPS será impactado.

1. **Parada dos Contêineres:**
   ```bash
   cd /opt/onlyoffice && docker compose down
   ```
2. **Remoção de Volumes e Dados:**
   ```bash
   cd /opt && rm -rf /opt/onlyoffice
   docker volume rm onlyoffice_data 2>/dev/null || true
   ```
3. **Limpeza de Portas e Checklist:**
   ```bash
   docker ps | grep onlyoffice
   ```

---

## 4. Rotina de Backup & Disaster Recovery
```bash
tar -czf /var/backups/onlyoffice-$(date +%Y%m%d).tar.gz -C /opt/onlyoffice .
openssl enc -aes-256-cbc -salt -in /var/backups/onlyoffice-$(date +%Y%m%d).tar.gz -out /var/backups/onlyoffice-$(date +%Y%m%d).enc -k SegredoBackup2026
```
