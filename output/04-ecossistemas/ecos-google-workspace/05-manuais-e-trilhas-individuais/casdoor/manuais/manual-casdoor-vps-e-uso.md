# Manual de Engenharia de VPS & Desinstalação Cirúrgica: Casdoor

> **Ferramenta:** Casdoor (SSO All-in-One com UI Amigável e LDAP)  
> **Pilar do Ecossistema:** Grupo 3: Identidade, Segurança & Governança (Admin, SSO, Vault & Endpoint) | **SaaS Substituído:** `Google Cloud Identity (SSO simples)`  
> **Licença OSI:** `Apache-2.0` | **Hardware Recomendado:** `1 vCPU / 512 MB RAM RAM / MySQL / PostgreSQL`  

---

## 1. Visão Geral & Papel no Ecossistema
Fornece SSO, gestão de usuários e MFA com interface administrativa simples. Go com frontend React e armazenamento em MySQL/PostgreSQL.

---

## 2. Instalação e Deploy em Produção na VPS

### Passo 1: Preparação do Diretório & Rede
```bash
mkdir -p /opt/casdoor && cd /opt/casdoor
docker network create ecosystem_net || true
```

### Passo 2: Arquivo de Variáveis de Ambiente (.env)
```bash
cat <<EOF > .env
APP_NAME=Casdoor
APP_PORT=8080
DATABASE_URL=postgresql://user:secret@postgres:5432/db_casdoor
SECRET_KEY=$(openssl rand -hex 32)
EOF
```

### Passo 3: Manifesto docker-compose.yml
```yaml
version: '3.8'
services:
  casdoor:
    image: casbin/casdoor:latest
    restart: unless-stopped
    env_file: .env
    volumes:
      - ./casdoor_data:/data
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

> **Garantia de Zero Efeito Colateral:** A remoção deste módulo afeta exclusivamente os contêineres e pastas de `/opt/casdoor`. Nenhum outro banco de dados, proxy Traefik ou aplicação rodando na mesma VPS será impactado.

1. **Parada dos Contêineres:**
   ```bash
   cd /opt/casdoor && docker compose down
   ```
2. **Remoção de Volumes e Dados:**
   ```bash
   cd /opt && rm -rf /opt/casdoor
   docker volume rm casdoor_data 2>/dev/null || true
   ```
3. **Limpeza de Portas e Checklist:**
   ```bash
   docker ps | grep casdoor
   ```

---

## 4. Rotina de Backup & Disaster Recovery
```bash
tar -czf /var/backups/casdoor-$(date +%Y%m%d).tar.gz -C /opt/casdoor .
openssl enc -aes-256-cbc -salt -in /var/backups/casdoor-$(date +%Y%m%d).tar.gz -out /var/backups/casdoor-$(date +%Y%m%d).enc -k SegredoBackup2026
```
