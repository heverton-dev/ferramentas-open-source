# Manual de Engenharia de VPS & Desinstalação Cirúrgica: Poste.io

> **Ferramenta:** Poste.io (Servidor de E-mail Completo em Contêiner Único com Painel Administrativo Ágil)  
> **Pilar do Ecossistema:** Pilar 01: E-mail Corporativo, Groupware & Gateway Antispam | **SaaS Substituído:** `Penso Mail Start`  
> **Licença OSI:** `GPL-2.0` | **Hardware Recomendado:** `1 vCPU / 2 GB RAM / SQLite integrado`  

---

## 1. Visão Geral & Papel no Ecossistema
Provê serviço completo de correio eletrônico corporativo em um único contêiner autossuficiente. Combina Haraka/Postfix com Dovecot e painel em PHP/SQLite em imagem única otimizada.

---

## 2. Instalação e Deploy em Produção na VPS

### Passo 1: Preparação do Diretório & Rede
```bash
mkdir -p /opt/poste-io && cd /opt/poste-io
docker network create ecosystem_net || true
```

### Passo 2: Arquivo de Variáveis de Ambiente (.env)
```bash
cat <<EOF > .env
APP_NAME=Poste.io
APP_PORT=8080
DATABASE_URL=postgresql://user:secret@postgres:5432/db_poste-io
SECRET_KEY=$(openssl rand -hex 32)
EOF
```

### Passo 3: Manifesto docker-compose.yml
```yaml
version: '3.8'
services:
  poste-io:
    image: analogic/poste.io:latest
    restart: unless-stopped
    env_file: .env
    volumes:
      - ./poste-io_data:/data
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

> **Garantia de Zero Efeito Colateral:** A remoção deste módulo afeta exclusivamente os contêineres e pastas de `/opt/poste-io`. Nenhum outro banco de dados, proxy Traefik ou aplicação rodando na mesma VPS será impactado.

1. **Parada dos Contêineres:**
   ```bash
   cd /opt/poste-io && docker compose down
   ```
2. **Remoção de Volumes e Dados:**
   ```bash
   cd /opt && rm -rf /opt/poste-io
   docker volume rm poste-io_data 2>/dev/null || true
   ```
3. **Limpeza de Portas e Checklist:**
   ```bash
   docker ps | grep poste-io
   ```

---

## 4. Rotina de Backup & Disaster Recovery
```bash
tar -czf /var/backups/poste-io-$(date +%Y%m%d).tar.gz -C /opt/poste-io .
openssl enc -aes-256-cbc -salt -in /var/backups/poste-io-$(date +%Y%m%d).tar.gz -out /var/backups/poste-io-$(date +%Y%m%d).enc -k SegredoBackup2026
```
