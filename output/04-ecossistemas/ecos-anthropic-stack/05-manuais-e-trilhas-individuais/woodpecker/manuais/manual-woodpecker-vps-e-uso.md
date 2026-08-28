# Manual de Engenharia de VPS & Desinstalação Cirúrgica: Woodpecker CI

> **Ferramenta:** Woodpecker CI (Motor de CI/CD Moderno com Suporte a Containers & Kubernetes)  
> **Pilar do Ecossistema:** Grupo 2: Infraestrutura de Desenvolvimento, CI/CD & Versionamento | **SaaS Substituído:** `GitHub Actions / GitLab CI / Jenkins`  
> **Licença OSI:** `Apache-2.0` | **Hardware Recomendado:** `1 vCPU / 2 GB RAM RAM / PostgreSQL / SQLite`  

---

## 1. Visão Geral & Papel no Ecossistema
Executa pipelines de build, teste e deploy em containers Docker isolados disparados por push/PR. Go + Docker API com suporte a secretos e variáveis de ambiente criptografadas.

---

## 2. Instalação e Deploy em Produção na VPS

### Passo 1: Preparação do Diretório & Rede
```bash
mkdir -p /opt/woodpecker && cd /opt/woodpecker
docker network create ecosystem_net || true
```

### Passo 2: Arquivo de Variáveis de Ambiente (.env)
```bash
cat <<EOF > .env
APP_NAME=Woodpecker CI
APP_PORT=8080
DATABASE_URL=postgresql://user:secret@postgres:5432/db_woodpecker
SECRET_KEY=$(openssl rand -hex 32)
EOF
```

### Passo 3: Manifesto docker-compose.yml
```yaml
version: '3.8'
services:
  woodpecker:
    image: woodpecker:latest
    restart: unless-stopped
    env_file: .env
    volumes:
      - ./woodpecker_data:/data
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

> **Garantia de Zero Efeito Colateral:** A remoção deste módulo afeta exclusivamente os contêineres e pastas de `/opt/woodpecker`. Nenhum outro banco de dados, proxy Traefik ou aplicação rodando na mesma VPS será impactado.

1. **Parada dos Contêineres:**
   ```bash
   cd /opt/woodpecker && docker compose down
   ```
2. **Remoção de Volumes e Dados:**
   ```bash
   cd /opt && rm -rf /opt/woodpecker
   docker volume rm woodpecker_data 2>/dev/null || true
   ```
3. **Limpeza de Portas e Checklist:**
   ```bash
   docker ps | grep woodpecker
   ```

---

## 4. Rotina de Backup & Disaster Recovery
```bash
tar -czf /var/backups/woodpecker-$(date +%Y%m%d).tar.gz -C /opt/woodpecker .
openssl enc -aes-256-cbc -salt -in /var/backups/woodpecker-$(date +%Y%m%d).tar.gz -out /var/backups/woodpecker-$(date +%Y%m%d).enc -k SegredoBackup2026
```
