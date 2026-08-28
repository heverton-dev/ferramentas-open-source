# Manual de Engenharia de VPS & Desinstalação Cirúrgica: Deno

> **Ferramenta:** Deno (Runtime JavaScript/TypeScript Moderno com Permissões Granulares)  
> **Pilar do Ecossistema:** Grupo 2: Infraestrutura de Desenvolvimento, CI/CD & Versionamento | **SaaS Substituído:** `Node.js (elimina dependência de npm/package.json)`  
> **Licença OSI:** `MIT` | **Hardware Recomendado:** `1 vCPU / 256 MB RAM RAM / PostgreSQL / SQLite`  

---

## 1. Visão Geral & Papel no Ecossistema
Executa scripts TypeScript/JavaScript com controle fino de permissões (arquivo, rede, variáveis de ambiente). Binário Rust estático com bundler integrado e cache imutável via URLs.

---

## 2. Instalação e Deploy em Produção na VPS

### Passo 1: Preparação do Diretório & Rede
```bash
mkdir -p /opt/deno && cd /opt/deno
docker network create ecosystem_net || true
```

### Passo 2: Arquivo de Variáveis de Ambiente (.env)
```bash
cat <<EOF > .env
APP_NAME=Deno
APP_PORT=8080
DATABASE_URL=postgresql://user:secret@postgres:5432/db_deno
SECRET_KEY=$(openssl rand -hex 32)
EOF
```

### Passo 3: Manifesto docker-compose.yml
```yaml
version: '3.8'
services:
  deno:
    image: deno:latest
    restart: unless-stopped
    env_file: .env
    volumes:
      - ./deno_data:/data
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

> **Garantia de Zero Efeito Colateral:** A remoção deste módulo afeta exclusivamente os contêineres e pastas de `/opt/deno`. Nenhum outro banco de dados, proxy Traefik ou aplicação rodando na mesma VPS será impactado.

1. **Parada dos Contêineres:**
   ```bash
   cd /opt/deno && docker compose down
   ```
2. **Remoção de Volumes e Dados:**
   ```bash
   cd /opt && rm -rf /opt/deno
   docker volume rm deno_data 2>/dev/null || true
   ```
3. **Limpeza de Portas e Checklist:**
   ```bash
   docker ps | grep deno
   ```

---

## 4. Rotina de Backup & Disaster Recovery
```bash
tar -czf /var/backups/deno-$(date +%Y%m%d).tar.gz -C /opt/deno .
openssl enc -aes-256-cbc -salt -in /var/backups/deno-$(date +%Y%m%d).tar.gz -out /var/backups/deno-$(date +%Y%m%d).enc -k SegredoBackup2026
```
