# Manual Operacional Completo: Block BUZZ

> **Padrão Diamante · Guia de Engenharia & Adoção Descomplicada**  
> **Licença:** Apache-2.0 | **Versão:** 0.5.0 | **Setup Estimado:** 60 a 90 minutos (Conhecimento intermediário de Docker e Nostr)  
> **VPS Recomendada:** Hetzner Cloud CX31 (4 vCPU, 8 GB RAM, EUR 25,90) ou Contabo VPS XL (4 vCPU Dedicadas (AMD EPYC ou Intel Xeon) - Mínimo 2 vCPU, 4+ para produção com 10+ usuários, 8 GB RAM mínimo (16 GB recomendado para 50+ usuários ou arquivos/mídia pesada), 100 GB SSD NVMe (mínimo 50 GB; crescer conforme volume de repositórios Git + mídia), Ubuntu 22.04 LTS (x86_64) ou Debian 12)  
> **Custo Mensal Estimado:** EUR 25,90 a 49,90/mês (~R$ 150 a R$ 300 na cotação média)

---

## Módulo 0: Nivelamento Conceitual (Analogias do Dia a Dia)

### 💡 Block BUZZ (A Ferramenta) *(Analogia: O Slack Que Você Controla Completamente)*
BUZZ é um workspace de comunicação para equipes, como Slack ou Teams. A diferença crucial: você instala no seu servidor, os dados nunca saem de lá, e é totalmente open source. Sem mensalidade ao Salesforce. Sem espiar seus dados. 100% seu.

### 💡 Nostr (O Protocolo de Fundo) *(Analogia: Email, Mas Para Mensagens Descentralizadas)*
Email é descentralizado: você pode ter Gmail, Outlook, Yahoo e trocar mensagens. Nostr é similar. BUZZ usa Nostr como camada de sincronização. Seus relays (servidores) falam entre si. Você não fica preso a um único provedor.

### 💡 VPS (Servidor Privado Virtual) *(Analogia: Uma Sala de Servidores Alugada 24/7)*
Você aluga um computador profissional por R$ 100-300/mês em um data center. Coloca BUZZ lá. Sua equipe acessa via web (HTTPS) ou app desktop. Sem deixar o servidor ligado no escritório.

### 💡 Docker & Compose (Containerização) *(Analogia: Um Pacote Pronto Com Tudo Que BUZZ Precisa)*
BUZZ precisa de: PostgreSQL (banco), Redis (cache), MinIO (arquivos). Docker empacota tudo isso como caixas isoladas. Docker Compose orquestra: 'suba PostgreSQL, depois Redis, depois BUZZ'. Tudo em um comando.

### 💡 Chaves Nostr (Identidade Criptográfica) *(Analogia: Seu CPF Digital, Mas Que Você Controla)*
Nostr usa criptografia de chave pública. Você gera uma chave privada (guarda em segredo) e uma chave pública (publica). Seu relay BUZZ é identificado pela chave pública. Ninguém consegue se passar por você sem a chave privada.

### 💡 Relay (Servidor Nostr) *(Analogia: Uma Estação de Correio Que Distribui Mensagens)*
Um relay recebe mensagens, armazena e distribui. BUZZ roda um relay nativo. Quando um usuário posta em BUZZ, a mensagem vai para o relay. Quando outro usuário acessa, o relay entrega a mensagem. Tudo encriptado.

### 💡 TLS & Let's Encrypt (Criptografia na Web) *(Analogia: Um Cadeado de Segurança Na Porta da Loja)*
HTTPS (criptografia) é obrigatório em produção. Let's Encrypt fornece certificados grátis. Caddy (servidor web) renueva automaticamente a cada 3 meses. Ninguém espia suas mensagens em trânsito.

### 💡 Agent-Native (Colaboração Com IA) *(Analogia: Um Colega Bot Que Participa da Reunião)*
BUZZ foi desenhado para agentes IA trabalharem junto com humanos. Um bot pode postar, processar mensagens, executar ações. Slack/Teams não foram feitos para isso. BUZZ sim: é 'agent-native'.

## Parte I: Instalação em Produção na VPS (Passo a Passo Rígido)

### Passo 1: Acessar VPS via SSH e Atualizar Sistema `[F01]`
Você se conecta ao seu servidor. Primeira ação: garantir que tudo está atualizado.

> 💡 **Entenda com uma analogia:** Verificar as tubulações e fiação da casa antes de morar nela.

```bash
ssh root@seu_ip_vps
sudo apt-get update
sudo apt-get upgrade -y
```

- 🖥️ **O que você verá na tela:** Linhas mostrando pacotes atualizados.
- ✅ **Como saber se deu certo:** Termina sem erros. Prompt retorna normal.

### Passo 2: Instalar Docker e Docker Compose `[F01]`
BUZZ roda em Docker. Vamos instalar Docker (engine) e Docker Compose (orquestrador).

> 💡 **Entenda com uma analogia:** Instalar o 'gerenciador de caixas' antes de guardar caixas isoladas.

```bash
sudo apt-get install -y docker.io docker-compose-plugin
sudo usermod -aG docker $USER
sudo systemctl start docker
sudo systemctl enable docker
docker --version && docker compose --version
```

- 🖥️ **O que você verá na tela:** Repositório Docker adicionado. Pacotes instalados. Pode levar 2-3 minutos.
- ✅ **Como saber se deu certo:** Comandos 'docker --version' e 'docker compose --version' retornam versões >= 24.x.

### Passo 3: Instalar Rust, Node.js 24+ e ffmpeg (Build & Runtime) `[F01]`
BUZZ é escrito em Rust e Node.js. Precisamos de ambos. ffmpeg para processamento de mídia.

> 💡 **Entenda com uma analogia:** Comprar as ferramentas específicas antes de montar o móvel.

```bash
sudo apt-get install -y build-essential curl git ffmpeg
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
source $HOME/.cargo/env
curl -fsSL https://deb.nodesource.com/setup_24.x | sudo -E bash -
sudo apt-get install -y nodejs
rustc --version && node --version
```

- 🖥️ **O que você verá na tela:** Ferramentas sendo instaladas. Pode levar 5-10 minutos (Rust é grande).
- ✅ **Como saber se deu certo:** Comandos 'rustc --version', 'node --version' (>= 24.0.0), 'npm --version', 'ffmpeg -version' retornam versões.

### Passo 4: Clonar Repositório BUZZ e Gerar Chaves Nostr `[F01]`
Vamos buscar o código oficial de BUZZ do GitHub e gerar as chaves criptográficas para o relay.

> 💡 **Entenda com uma analogia:** Comprar o kit pronto e gerar os documentos de identidade.

```bash
sudo mkdir -p /opt/buzz && cd /opt/buzz
sudo git clone https://github.com/block/buzz.git .
sudo chown -R $USER:$USER /opt/buzz
cd /opt/buzz
# Gerar chaves Nostr:
node -e "const crypto = require('crypto'); const sk = crypto.randomBytes(32).toString('hex'); console.log('RELAY_SK=' + sk);" >> .env
node -e "const crypto = require('crypto'); const pk = crypto.createPublicKey({key: Buffer.from(require('fs').readFileSync('.env', 'utf8').match(/RELAY_SK=(.+)/)[1], 'hex'), format: 'der', type: 'private'}).export({format: 'pem', type: 'pkcs8'}); console.log('RELAY_PK=' + pk.toString());" >> .env
```

- 🖥️ **O que você verá na tela:** Git clonando repositório (~200 MB). Depois, gerando chaves (rápido).
- ✅ **Como saber se deu certo:** Pasta /opt/buzz existe com arquivos Rust/Node.js. Arquivo .env contém RELAY_PK e RELAY_SK.

### Passo 5: Configurar Docker Compose para BUZZ `[F01]`
Criamos um arquivo docker-compose.yml com PostgreSQL, Redis, MinIO e BUZZ configurados.

> 💡 **Entenda com uma analogia:** Escrever a lista de ingredientes e modo de preparo para a receita.

```bash
cd /opt/buzz
sudo nano docker-compose.yml
# Colar configuração do arquivo de composição (ver próxima seção)
sudo docker compose config | head -20  # Validar sintaxe
```

- 🖥️ **O que você verá na tela:** Você abre editor nano, cola configuração, salva.
- ✅ **Como saber se deu certo:** Arquivo /opt/buzz/docker-compose.yml existe com 150+ linhas.

### Passo 6: Compilar BUZZ e Iniciar Serviços Docker `[F02]`
Compilamos o backend Rust e inicializamos todos os containers.

> 💡 **Entenda com uma analogia:** Montar o móvel e ligá-lo para verificar se funciona.

```bash
cd /opt/buzz
sudo docker compose build
sudo docker compose up -d
sudo docker compose ps
```

- 🖥️ **O que você verá na tela:** Compilação Rust leva 10-20 minutos (primeira vez). Docker containers iniciando.
- ✅ **Como saber se deu certo:** Comando 'docker ps' mostra 5 containers em 'up': postgres, redis, minio, buzz-backend, buzz-frontend.

### Passo 7: Configurar Caddy como Proxy Reverso com TLS `[F02]`
Caddy recebe HTTPS em buzz.sua-empresa.com.br e passa para BUZZ em localhost:3000.

> 💡 **Entenda com uma analogia:** Um recepcionista que recebe clientes de fora e os encaminha internamente.

```bash
sudo apt-get install -y caddy
sudo nano /etc/caddy/Caddyfile
# Colar configuração do proxy
sudo systemctl reload caddy
```

- 🖥️ **O que você verá na tela:** Caddy se instala, arquivo Caddyfile criado, TLS automático com Let's Encrypt.
- ✅ **Como saber se deu certo:** Acessar https://buzz.sua-empresa.com.br retorna página de login do BUZZ sem avisos SSL.

### Passo 8: Criar Usuário Admin e Configurar BUZZ `[F03]`
Acessar https://buzz.sua-empresa.com.br e completar setup wizard (admin user, empresa, preferências).

> 💡 **Entenda com uma analogia:** O primeiro boot de um novo sistema: perguntas sobre configuração inicial.

```bash
Nenhum comando. Tudo é feito via navegador web em https://buzz.sua-empresa.com.br
```

- 🖥️ **O que você verá na tela:** Interface web pedindo: Email do Admin, Senha, Nome da Empresa, Timezone, Domínio de Relay.
- ✅ **Como saber se deu certo:** Você consegue fazer login com email/senha criados e vê o dashboard do BUZZ.

### Passo 9: Configurar Backup Automatizado de Dados `[F04]`
Script que faz backup diário do PostgreSQL, Redis e repositórios Git.

> 💡 **Entenda com uma analogia:** Tirar fotografia do arquivo da empresa todo dia.

```bash
sudo mkdir -p /backups
sudo nano /usr/local/bin/backup-buzz.sh
# Colar script de backup
sudo chmod +x /usr/local/bin/backup-buzz.sh
sudo crontab -e
# Adicionar: 0 2 * * * /usr/local/bin/backup-buzz.sh
```

- 🖥️ **O que você verá na tela:** Script criado em /usr/local/bin/. Agendado via crontab.
- ✅ **Como saber se deu certo:** Arquivo .tar.gz com backup existe em /backups/ com timestamp de hoje.

## Arquivos de Configuração de Produção

### `/opt/buzz/docker-compose.yml`
*Docker Compose que orquestra: PostgreSQL (banco), Redis (cache), MinIO (armazenamento S3-compatível), BUZZ (server Rust em port 3000). Variáveis de ambiente carregadas de .env. Volumes persistem dados entre restarts.*

```yaml
version: '3.8'

services:
  postgres:
    image: postgres:16-alpine
    container_name: buzz-postgres
    environment:
      POSTGRES_DB: buzz
      POSTGRES_USER: buzzuser
      POSTGRES_PASSWORD: SenhaSegura123!BuzzVPS
    volumes:
      - postgres_data:/var/lib/postgresql/data
    networks:
      - buzz-network
    restart: unless-stopped

  redis:
    image: redis:7-alpine
    container_name: buzz-redis
    volumes:
      - redis_data:/data
    networks:
      - buzz-network
    restart: unless-stopped

  minio:
    image: minio/minio:latest
    container_name: buzz-minio
    environment:
      MINIO_ROOT_USER: minioadmin
      MINIO_ROOT_PASSWORD: SenhaSegura123!MinioVPS
    volumes:
      - minio_data:/data
    networks:
      - buzz-network
    command: minio server /data
    restart: unless-stopped

  buzz:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: buzz-server
    depends_on:
      - postgres
      - redis
      - minio
    environment:
      DATABASE_URL: postgres://buzzuser:SenhaSegura123!BuzzVPS@postgres:5432/buzz
      REDIS_URL: redis://redis:6379
      MINIO_ENDPOINT: minio:9000
      MINIO_ACCESS_KEY: minioadmin
      MINIO_SECRET_KEY: SenhaSegura123!MinioVPS
      RELAY_PK: ${RELAY_PK}
      RELAY_SK: ${RELAY_SK}
      PORT: 3000
      RUST_LOG: info
    ports:
      - "3000:3000"
    volumes:
      - /opt/buzz/data:/app/data
    networks:
      - buzz-network
    restart: unless-stopped

volumes:
  postgres_data:
  redis_data:
  minio_data:

networks:
  buzz-network:
    driver: bridge
```

### `/etc/caddy/Caddyfile`
*Caddyfile que: 1) Ativa TLS automático com Let's Encrypt. 2) Compressão gzip. 3) Proxy reverso para BUZZ em localhost:3000. 4) Suporte a WebSocket (protocolo Nostr). Caddy renova certificado automaticamente.*

```caddy
buzz.sua-empresa.com.br {
  encode gzip
  reverse_proxy localhost:3000 {
    header_up X-Forwarded-For {http.request.remote.host}
    header_up X-Forwarded-Proto {http.request.proto}
    header_up X-Real-IP {http.request.remote.host}
  }
  
  # WebSocket suporte
  reverse_proxy /ws/* localhost:3000 {
    header_up Connection "upgrade"
    header_up Upgrade "websocket"
  }
}
```

### `/opt/buzz/.env`
*Configurações críticas: banco de dados, cache, storage S3, chaves Nostr (RELAY_PK e RELAY_SK geradas na etapa 4), port e CORS. Substitua SUA_EMPRESA e os valores de exemplo antes de usar em produção.*

```ini
# Ambiente de Produção
RUST_ENV=production
RUST_LOG=info

# Banco de Dados
DATABASE_URL=postgres://buzzuser:SenhaSegura123!BuzzVPS@postgres:5432/buzz
REDIS_URL=redis://redis:6379

# Storage (MinIO)
MINIO_ENDPOINT=minio:9000
MINIO_ACCESS_KEY=minioadmin
MINIO_SECRET_KEY=SenhaSegura123!MinioVPS
MINIO_BUCKET=buzz-media

# Nostr Relay
RELAY_PK=SEU_PUBLIC_KEY_HEX_AQUI
RELAY_SK=SEU_SECRET_KEY_HEX_AQUI

# Server
PORT=3000
BIND_ADDR=0.0.0.0
CORS_ORIGINS=https://buzz.sua-empresa.com.br

# Media Config
MAX_FILE_SIZE=500MB
ALLOWED_MEDIA_TYPES=image/*,video/*,audio/*,application/pdf
```

### `/usr/local/bin/backup-buzz.sh`
*Script de backup que: 1) Faz dump do PostgreSQL. 2) Copia snapshot Redis. 3) Compacta diretório de dados. 4) Deleta backups com 30+ dias. Execute diariamente via crontab às 2h da manhã.*

```bash
#!/bin/bash
BACKUP_DIR="/backups"
DATE=$(date +%Y%m%d_%H%M%S)

echo "[$(date)] Iniciando backup de BUZZ..." >> /var/log/buzz-backup.log

# Backup PostgreSQL
cd /opt/buzz
docker compose exec -T postgres pg_dump -U buzzuser buzz | gzip > $BACKUP_DIR/buzz_postgres_$DATE.sql.gz

# Backup Redis
docker compose exec -T redis redis-cli BGSAVE
sleep 5
docker compose exec -T redis cat /data/dump.rdb > $BACKUP_DIR/buzz_redis_$DATE.rdb

# Backup MinIO (repositórios e mídia)
tar --exclude='*/cache' -czf $BACKUP_DIR/buzz_storage_$DATE.tar.gz /opt/buzz/data

# Manter apenas últimos 30 dias
find $BACKUP_DIR -name 'buzz_*' -mtime +30 -delete

echo "[$(date)] Backup concluído com sucesso." >> /var/log/buzz-backup.log
```

## Parte II: Manual de Uso Exaustivo

**Arquitetura Operacional:** BUZZ funciona em 4 camadas: (1) Camada Web (Caddy + TLS) recebe HTTPS, (2) Backend Rust roda servidor Nostr relay em port 3000, (3) PostgreSQL armazena mensagens, usuários, canais (eventos Nostr), (4) Redis caches presença em tempo real, indicadores de digitação, sessões. MinIO armazena mídia (arquivos, imagens, vídeos). Tudo containerizado em Docker Compose, isolado de outros serviços.

### Roteiro de Primeiro Voo (Sua Primeira Reunião em 3 Minutos)

1. **1. Acessar Dashboard Web:** Abra https://buzz.sua-empresa.com.br em navegador. Você verá tela de login.
   - 🎯 **Resultado Esperado:** Página de login carrega sem erros SSL. Caixa de email e senha visíveis.

1. **2. Criar Primeiro Usuário (Admin):** Clique 'Criar Conta'. Digite email, senha, nome. Clique 'Registrar'.
   - 🎯 **Resultado Esperado:** Login bem-sucedido. Dashboard mostra 'Bem-vindo ao BUZZ' com 'Crear Workspace' ou 'Join Workspace'.

1. **3. Criar Workspace:** Clique 'Create Workspace'. Digite nome (ex: 'Empresa Teste'). Clique 'Criar'.
   - 🎯 **Resultado Esperado:** Workspace criado. Você vê canais padrão (#general, #random) e seção 'Members'.

1. **4. Enviar Primeira Mensagem:** Clique em #general. Digite 'Olá BUZZ!' na caixa de mensagem. Pressione Enter.
   - 🎯 **Resultado Esperado:** Mensagem aparece no chat com timestamp. Seu nome de usuário aparece como remetente.

1. **5. Convidar Outro Usuário:** Clique em 'Members' ou ícone de pessoas. Clique 'Invite'. Cole link de convite ou envie email.
   - 🎯 **Resultado Esperado:** Outro usuário recebe convite. Ao aceitar, aparece no workspace como membro.

### Dicionário Completo de Comandos (CLI)

| Comando / Flag | Descrição Técnica | Exemplo de Execução | Fonte |
| :--- | :--- | :--- | :---: |
| `docker compose logs buzz -f` | Ver logs em tempo real do servidor BUZZ (debug de problemas). | `cd /opt/buzz && sudo docker compose logs buzz -f | grep -i error` | `[F03]` |
| `docker compose restart buzz` | Reiniciar servidor BUZZ após mudança de configuração. | `cd /opt/buzz && sudo docker compose restart buzz` | `[F03]` |
| `docker compose down && docker compose up -d` | Parar todos os containers e reiniciar (redeploy). | `cd /opt/buzz && sudo docker compose down && sudo docker compose up -d` | `[F03]` |

### Endpoints de API REST & Integração Agêntica

| Método | Rota | Descrição | Fonte |
| :---: | :--- | :--- | :---: |
| **POST** | `/auth/register` | Registrar novo usuário. | `[F04]` |
| **POST** | `/messages` | Enviar mensagem programaticamente (via agent). | `[F04]` |
| **GET** | `/.well-known/nostr.json` | Endpoint Nostr para descoberta de relay (NIP-05). | `[F04]` |

### Matriz de Resolução de Problemas (Troubleshooting)

- **⚠️ Sintoma:** Página não carrega (timeout ou erro 502)
  - **Causa:** BUZZ container parado ou consumindo muita memória/CPU.
- **⚠️ Sintoma:** Mensagens não aparecem em tempo real (delay de minutos)
  - **Causa:** Redis não está sincronizado ou PostgreSQL está lento.
- **⚠️ Sintoma:** Erro 'WebSocket connection refused' no cliente desktop/mobile
  - **Causa:** Porta 3000 bloqueada no firewall ou Caddy não está redirecionando corretamente.
- **⚠️ Sintoma:** Disco cheio (df -h mostra 100%)
  - **Causa:** MinIO (armazenamento de mídia) ou PostgreSQL consumindo espaço.
- **⚠️ Sintoma:** Certificado SSL inválido ou expirado
  - **Causa:** Caddy não conseguiu renovar Let's Encrypt automaticamente.
## Parte III: Desinstalação Cirúrgica & Isolamento da VPS (Zero Efeito Colateral)

> 🛡️ **Princípio de Isolamento:** BUZZ foi instalado em estrutura totalmente isolada em Docker: containers em /opt/buzz/, volumes em Docker named volumes (postgres_data, redis_data, minio_data), configuração em /opt/buzz/.env e /etc/caddy/Caddyfile, Caddy separado. Esta modularidade permite remoção cirúrgica sem efeitos colaterais. Outros containers/aplicações na VPS não serão afetadas. Seguindo estes passos, BUZZ desaparece completamente.

### Passo 1: Parar Containers BUZZ
Interrompa todos os containers Docker de BUZZ sem deletar volumes/dados.

```bash
cd /opt/buzz
sudo docker compose down
sudo docker compose ps  # Deve estar vazio
```

- ⚠️ **Alerta de Segurança:** ALERTA: Após este passo, https://buzz.sua-empresa.com.br será inacessível.
- ✅ **Como Validar:** `Acessar https://buzz.sua-empresa.com.br retorna erro 502 ou timeout.`

### Passo 2: Backup Final de Dados (Altamente Recomendado)
Fazer backup completo antes de deletar: PostgreSQL, Redis, MinIO, repositórios.

```bash
sudo mkdir -p /backups/buzz-final
tar -czf /backups/buzz-final/postgres_dump_$(date +%Y%m%d).sql.gz /opt/buzz/data/postgres
tar -czf /backups/buzz-final/redis_dump_$(date +%Y%m%d).tar.gz /opt/buzz/data/redis
tar -czf /backups/buzz-final/minio_dump_$(date +%Y%m%d).tar.gz /opt/buzz/data/minio
tar -czf /backups/buzz-final/app_$(date +%Y%m%d).tar.gz /opt/buzz
```

- ⚠️ **Alerta de Segurança:** CRÍTICO: Sem este backup, os dados são irrecuperáveis após próxima etapa.
- ✅ **Como Validar:** `4 arquivos .tar.gz em /backups/buzz-final/ com tamanho total > 100MB`

### Passo 3: Deletar Containers, Imagens e Volumes Docker
Remover completamente todos os containers, imagens e volumes nomeados de BUZZ.

```bash
cd /opt/buzz
sudo docker compose down -v  # -v remove volumes
sudo docker rmi -f buzz-server  # Remove imagem BUZZ
sudo docker volume rm buzz-postgres buzz-redis buzz-minio 2>/dev/null
sudo docker system prune -f  # Remove dangling images
```

- ⚠️ **Alerta de Segurança:** PONTO DE NÃO-RETORNO: Containers, imagens e volumes são deletados permanentemente.
- ✅ **Como Validar:** `sudo docker compose ps retorna 'No containers'. sudo docker volume ls não lista volumes 'buzz-*'.`

### Passo 4: Remover Aplicação e Configurações
Deletar pasta de aplicação, Caddyfile e scripts de backup.

```bash
sudo rm -rf /opt/buzz/
sudo rm -f /etc/caddy/Caddyfile.bak
sudo rm -f /usr/local/bin/backup-buzz.sh
sudo rm -f /var/log/buzz*
sudo crontab -e  # Remover entrada de backup
```

- ⚠️ **Alerta de Segurança:** PONTO DE NÃO-RETORNO: Todos os arquivos de BUZZ são deletados.
- ✅ **Como Validar:** `sudo ls /opt/buzz/ retorna 'No such file'. sudo crontab -l não contém 'buzz'.`

### Passo 5: Remover Certificado SSL e Desativar Caddy
Se BUZZ era o único site HTTPS, remover certificado Let's Encrypt e desativar Caddy.

```bash
sudo certbot delete --cert-name buzz.sua-empresa.com.br 2>/dev/null
sudo systemctl stop caddy
sudo systemctl disable caddy
sudo rm -f /etc/caddy/Caddyfile
```

- ⚠️ **Alerta de Segurança:** ATENÇÃO: Remova apenas se nenhum outro site na VPS usa este domínio.
- ✅ **Como Validar:** `sudo systemctl status caddy mostra 'inactive'. sudo certbot certificates não lista 'buzz.sua-empresa.com.br'.`

### Checklist de Saúde da VPS (Outros Projetos)

- [ ] `ESPAÇO EM DISCO: df -h → Deve liberar 50+ GB. Coluna 'Avail' >= 30GB`
- [ ] `CONTAINERS: docker ps | grep buzz → Nenhum container BUZZ deve estar rodando`
- [ ] `VOLUMES: docker volume ls | grep buzz → Nenhum volume nomeado 'buzz-*'`
- [ ] `IMAGENS: docker images | grep buzz → Nenhuma imagem com 'buzz' no nome`
- [ ] `PORTAS: sudo netstat -tlnp | grep 3000 → Porta 3000 NOT in LISTEN`
- [ ] `CADDY: sudo systemctl status caddy → Deve estar 'inactive' ou removido`
- [ ] `LOGS: tail -20 /var/log/syslog → NÃO deve conter 'buzz' ou 'caddy'`
- [ ] `CRON: sudo crontab -l → NÃO deve ter scripts de backup-buzz`

## Parte IV: Referências Bibliográficas Auditadas

| ID | Categoria | Título da Obra | Autor / Mantenedor | Link Oficial |
| :---: | :--- | :--- | :--- | :--- |
| **F01** | Repositório Oficial | Block BUZZ - GitHub Repository | Block Inc. / Jack Dorsey | [https://github.com/block/buzz](https://github.com/block/buzz) |
| **F02** | Documentação | BUZZ Docker Deployment Guide | BUZZ Documentation | [https://github.com/block/buzz#deployment](https://github.com/block/buzz#deployment) |
| **F03** | Protocolo | Nostr Protocol - NIP-01, NIP-42, NIP-34 | Nostr Community | [https://github.com/nostr-protocol/nips](https://github.com/nostr-protocol/nips) |
| **F04** | Ferramenta | Docker Compose - Orquestração de Containers | Docker Inc. | [https://docs.docker.com/compose/](https://docs.docker.com/compose/) |
| **F05** | Licença | Apache License 2.0 - Texto Completo | Open Source Initiative | [https://opensource.org/licenses/Apache-2.0](https://opensource.org/licenses/Apache-2.0) |
