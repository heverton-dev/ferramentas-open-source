# Manual de Engenharia de VPS & Desinstalação Cirúrgica: Directus

> **Ferramenta:** Directus (Headless CMS para Landing Pages & Portais de Conteúdo)  
> **Pilar do Ecossistema:** Grupo 1: Marketing, Nutrição & Landing Pages | **SaaS Substituído:** `RD Station Marketing (Construtor de Landing Pages & Formulários Estáticos)`  
> **Licença OSI:** `GPL-3.0` | **Hardware Recomendado:** `1 vCPU / 2 GB RAM RAM / PostgreSQL / SQLite`  

---

## 1. Visão Geral & Papel no Ecossistema
Fornece painel no-code para o time de marketing editar textos, depoimentos e formulários de landing pages. API REST/GraphQL instantânea sobre o PostgreSQL corporativo com autenticação OIDC.

---

## 2. Instalação e Deploy em Produção na VPS

### Passo 1: Preparação do Diretório & Rede
```bash
mkdir -p /opt/directus && cd /opt/directus
docker network create ecosystem_net || true
```

### Passo 2: Arquivo de Variáveis de Ambiente (.env)
```bash
cat <<EOF > .env
APP_NAME=Directus
APP_PORT=8080
DATABASE_URL=postgresql://user:secret@postgres:5432/db_directus
SECRET_KEY=$(openssl rand -hex 32)
EOF
```

### Passo 3: Manifesto docker-compose.yml
```yaml
version: '3.8'
services:
  directus:
    image: directus:latest
    restart: unless-stopped
    env_file: .env
    volumes:
      - ./directus_data:/data
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

> **Garantia de Zero Efeito Colateral:** A remoção deste módulo afeta exclusivamente os contêineres e pastas de `/opt/directus`. Nenhum outro banco de dados, proxy Traefik ou aplicação rodando na mesma VPS será impactado.

1. **Parada dos Contêineres:**
   ```bash
   cd /opt/directus && docker compose down
   ```
2. **Remoção de Volumes e Dados:**
   ```bash
   cd /opt && rm -rf /opt/directus
   docker volume rm directus_data 2>/dev/null || true
   ```
3. **Limpeza de Portas e Checklist:**
   ```bash
   docker ps | grep directus
   ```

---

## 4. Rotina de Backup & Disaster Recovery
```bash
tar -czf /var/backups/directus-$(date +%Y%m%d).tar.gz -C /opt/directus .
openssl enc -aes-256-cbc -salt -in /var/backups/directus-$(date +%Y%m%d).tar.gz -out /var/backups/directus-$(date +%Y%m%d).enc -k SegredoBackup2026
```
