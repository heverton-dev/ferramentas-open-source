# Manual Operacional Completo: Postal

> **Padrão Diamante · Guia de Engenharia & Adoção Descomplicada**  
> **Licença:** MIT | **Versão:** 3.0.0 | **Setup Estimado:** 45 a 60 minutos (Conhecimento intermediário de Docker & PostgreSQL)  
> **VPS Recomendada:** Hetzner Cloud CPX31 ou Linode Linode 8GB (4 vCPU Dedicadas (AMD EPYC), 8 GB RAM ECC, 160 GB NVMe Gen4, Ubuntu 24.04 LTS (x86_64))  
> **Custo Mensal Estimado:** EUR 14,00/mês (~R$ 84,00/mês na cotação média)

---

## Módulo 0: Nivelamento Conceitual (Analogias do Dia a Dia)

### 💡 Postal (Plataforma de Email Transacional) *(Analogia: O Cartório Privado de Mensagens)*
Postal é um sistema completo de email transacional que funciona como o Cuttlefish, mas instalado em sua própria VPS sob controle total. Ele recebe requisições da sua aplicação, fila de emails, valida domínios, entrega e rastreia cada mensagem com webhooks.

### 💡 Email Transacional vs. Marketing *(Analogia: Confirmação vs. Propaganda)*
Transacional são emails críticos como 'Reset de Senha', 'Confirmação de Pedido', 'Aviso de Falha'. Marketing são newsletters e campanhas. Postal é especializado em transacional: entrega garantida, alta reputação, sem limite de taxa.

### 💡 Fila de Trabalho Assíncrona (Sidekiq + Redis) *(Analogia: A Caixa de Saída de um Cartório)*
Quando sua aplicação pede para enviar 1.000 emails de confirmação, ela não espera cada um ser enviado. A requisição vai para uma fila (Redis), e workers em background processam um por um com retry automático.

### 💡 Webhooks de Entrega & Bounce *(Analogia: Confirmação de Recebimento Automática)*
Postal avisa sua aplicação quando um email foi entregue, aberto ou retornou (bounce). Sua aplicação recebe um POST HTTP com os dados e pode atualizar o banco de dados do usuário automaticamente.

### 💡 DKIM, SPF e DMARC (Segurança de Reputação) *(Analogia: Assinatura, Carimbo e Carta Notarial)*
Para que o Gmail não jogue seus emails na pasta de spam, você configura certificados digitais (DKIM), autoriza seus servidores (SPF) e cria política de autenticação (DMARC). Postal automatiza tudo isso.

## Parte I: Instalação em Produção na VPS (Passo a Passo Rígido)

### Passo 1: Hardening & Firewall Inicial (UFW) `[F01]`
Configurar acesso restrito à VPS com apenas portas essenciais.

> 💡 **Entenda com uma analogia:** Trancar o prédio do cartório e deixar apenas a guarita aberta.

```bash
ufw default deny incoming
ufw default allow outgoing
ufw allow 22/tcp && ufw allow 80/tcp && ufw allow 443/tcp
ufw --force enable
```

- 🖥️ **O que você verá na tela:** Mensagens confirmando regras de firewall aplicadas sem erro.
- ✅ **Como saber se deu certo:** Digite 'ufw status' e veja portas 22, 80, 443 marcadas como 'ALLOW IN'.

### Passo 2: Instalação de Docker & Docker Compose `[F02]`
Preparar motor de containers para rodar Postal, PostgreSQL e Redis.

> 💡 **Entenda com uma analogia:** Montar a estrutura física do cartório: prateleiras, mesas e sistema de arquivos.

```bash
apt-get update && apt-get install -y ca-certificates curl
curl -fsSL https://get.docker.com | sh
usermod -aG docker deployer
```

- 🖥️ **O que você verá na tela:** Pacotes instalados sem erro, docker engine iniciando.
- ✅ **Como saber se deu certo:** Execute 'docker --version' e veja Docker 27+ retornado.

### Passo 3: Provisionar Diretórios & Volumes Persistentes `[F01]`
Criar pasta /opt/postal com subpastas para dados, backups e configuração.

> 💡 **Entenda com uma analogia:** Preparar as gavetas e prateleiras do cartório para armazenar documentos.

```bash
mkdir -p /opt/postal/{data,db,redis,caddy,backups}
chown -R deployer:deployer /opt/postal
chmod -R 750 /opt/postal
```

- 🖥️ **O que você verá na tela:** Diretórios criados silenciosamente em menos de 1 segundo.
- ✅ **Como saber se deu certo:** Execute 'ls -ld /opt/postal' e veja pasta pertencendo ao deployer.

### Passo 4: Deploy da Stack Postal com Docker Compose `[F02]`
Levantamento de containers: Postal (Rails), PostgreSQL, Redis e Caddy (proxy reverso).

> 💡 **Entenda com uma analogia:** Ligar as máquinas e sistemas do cartório: computadores, impressoras e telefones.

```bash
cd /opt/postal
cat > docker-compose.yml << 'EOF'
version: '3.8'
services:
  postgres:
    image: postgres:16-alpine
    environment:
      POSTGRES_DB: postal
      POSTGRES_USER: postal
      POSTGRES_PASSWORD: $(openssl rand -base64 32)
    volumes:
      - postgres_data:/var/lib/postgresql/data
    restart: unless-stopped
  redis:
    image: redis:7-alpine
    volumes:
      - redis_data:/data
    restart: unless-stopped
  postal:
    image: postalserver/postal:latest
    depends_on:
      - postgres
      - redis
    environment:
      RAILS_ENV: production
      DATABASE_URL: postgres://postal:password@postgres:5432/postal
      REDIS_URL: redis://redis:6379
    ports:
      - '5000:5000'
    volumes:
      - postal_data:/opt/postal/data
    restart: unless-stopped
  caddy:
    image: caddy:2-alpine
    ports:
      - '80:80'
      - '443:443'
    volumes:
      - ./Caddyfile:/etc/caddy/Caddyfile
      - caddy_data:/data
    restart: unless-stopped
volumes:
  postgres_data:
  redis_data:
  postal_data:
  caddy_data:
EOF
docker compose up -d
```

- 🖥️ **O que você verá na tela:** Docker faz download de imagens e containers iniciam com logs coloridos. Aguarde 2-3 minutos.
- ✅ **Como saber se deu certo:** Execute 'docker compose ps' e veja 4 containers com status 'Up'.

### Passo 5: Configuração de Domínios & Certificados SSL `[F05]`
Registrar domínios corporativos no painel Postal e configurar DKIM/SPF/DMARC.

> 💡 **Entenda com uma analogia:** Registrar o domínio legal do cartório e obter autorizações de segurança.

```bash
# No painel Postal:
# 1. Clique em 'Add Domain'
# 2. Digite seu domínio (ex: transacional.empresa.com.br)
# 3. Copie os registros DKIM/SPF/DMARC para sua zona de DNS
# 4. Aguarde propagação (5-30 minutos)
# 5. Clique 'Verify' quando DNS estiver propagado
```

- 🖥️ **O que você verá na tela:** Painel web exibindo formulário de domínios e registros DNS necessários.
- ✅ **Como saber se deu certo:** Acesse https://seu-dominio.com/admin, faça login e veja seus domínios listados com status 'Verified'.

### Passo 6: Geração de API Keys & Teste de Conexão `[F03]`
Criar credenciais de API para integração com sua aplicação e validar entrega.

> 💡 **Entenda com uma analogia:** Entregar a carteira com as chaves de acesso ao cartório para os clientes autorizados.

```bash
# No painel Postal:
# 1. Clique em 'API Credentials'
# 2. Clique 'Create New'
# 3. Copie o token
# 4. Salve em variável de ambiente: export POSTAL_API_KEY='seu-token'
```

- 🖥️ **O que você verá na tela:** Painel exibindo string de token longo. Copie para lugar seguro (seu .env).
- ✅ **Como saber se deu certo:** Execute 'curl -H "Authorization: Bearer seu-token" https://seu-postal/api/v1/stats' e receba JSON com estatísticas.

## Arquivos de Configuração de Produção

### `/opt/postal/Caddyfile`
*Proxy reverso com SSL automático (Let's Encrypt), rate limiting na API de envio e headers de segurança.*

```caddyfile
postal.seu-dominio.com.br {
  encode gzip
  header {
    Strict-Transport-Security "max-age=31536000; includeSubDomains"
    X-Content-Type-Options nosniff
    X-Frame-Options DENY
  }
  reverse_proxy localhost:5000 {
    header_uri X-Real-IP {http.request.remote.host}
    header_uri X-Forwarded-For {http.request.remote.host}
  }
  rate_limit /api/v1/send 1000 100
}
```

### `/opt/postal/.env.production`
*Variáveis de ambiente para Postal em modo produção com banco PostgreSQL e Redis.*

```bash
RAILS_ENV=production
RAILS_LOG_TO_STDOUT=true
DATABASE_URL=postgres://postal:senha-forte-aqui@postgres:5432/postal
REDIS_URL=redis://redis:6379/0
SECRET_KEY_BASE=$(openssl rand -hex 64)
BRAND_NAME="Postal - Email Transacional"
ADMIN_EMAIL=admin@seu-dominio.com.br
SMTP_PORT=25
SMTP_TLS_ENABLED=true
```

### `/opt/postal/docker-compose.override.yml`
*Configurações de override para produção com health check automático.*

```yaml
version: '3.8'
services:
  postal:
    environment:
      POSTAL_WEB_PROTOCOL: https
      POSTAL_WEB_HOST: postal.seu-dominio.com.br
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:5000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 60s
```

## Parte II: Manual de Uso Exaustivo

**Arquitetura Operacional:** Postal é uma aplicação Rails que expõe API REST para envio de emails. Sua aplicação faz POST para /api/v1/send com autenticação por bearer token. Postal fila o email em Redis/Sidekiq, processa em background e notifica eventos via webhooks. Todas as mensagens são armazenadas em PostgreSQL para rastreabilidade.

### Roteiro de Primeiro Voo (Sua Primeira Reunião em 3 Minutos)

1. **Passo 1: Acessar Painel Administrativo:** Abra https://postal.seu-dominio.com.br/admin
   - 🎯 **Resultado Esperado:** Formulário de login solicitando email e senha.

1. **Passo 2: Registrar Seu Primeiro Domínio:** Clique em 'Domains' → 'Add Domain' e digite seu domínio corporativo.
   - 🎯 **Resultado Esperado:** Postal exibe registros DKIM/SPF/DMARC para copiar na zona de DNS.

1. **Passo 3: Verificar Domínio:** Aguarde 5-10 minutos pela propagação de DNS. Clique 'Verify Domain'.
   - 🎯 **Resultado Esperado:** Status muda para 'Verified' com checkmark verde.

1. **Passo 4: Criar Credencial de API:** Em Settings → API Credentials → Create New. Copie o token.
   - 🎯 **Resultado Esperado:** String longa de token salva em variável de ambiente POSTAL_API_KEY.

1. **Passo 5: Enviar Email de Teste:** Execute: curl -X POST https://postal.seu-dominio.com.br/api/v1/send -H 'Authorization: Bearer seu-token' -H 'Content-Type: application/json' -d '{"to": "seu-email@gmail.com", "from": "noreply@seu-dominio.com.br", "subject": "Teste", "plain_body": "Olá!"}'
   - 🎯 **Resultado Esperado:** Resposta JSON com messageId. Email chega no Gmail em 5-10 segundos.

1. **Passo 6: Configurar Webhook de Entrega:** Em Webhooks → Add Webhook. Configure URL do seu backend e selecione events: 'Message Delivered', 'Message Bounced'.
   - 🎯 **Resultado Esperado:** Seu backend recebe POST HTTPS cada vez que um email é entregue ou retorna.

### Dicionário Completo de Comandos (CLI)

| Comando / Flag | Descrição Técnica | Exemplo de Execução | Fonte |
| :--- | :--- | :--- | :---: |
| `docker compose ps` | Ver status dos containers Postal, PostgreSQL, Redis e Caddy. | `docker compose ps` | `[F01]` |
| `docker compose logs -f postal` | Ver logs em tempo real da aplicação Postal. | `docker compose logs -f postal --tail=100` | `[F02]` |
| `docker compose exec postgres psql -U postal -d postal` | Acessar console PostgreSQL para queries diretas. | `docker compose exec postgres psql -U postal -d postal -c 'SELECT COUNT(*) FROM messages;'` | `[F03]` |
| `docker compose exec redis redis-cli` | Acessar console Redis para inspecionar fila. | `docker compose exec redis redis-cli LLEN resque:queue:default` | `[F04]` |

### Endpoints de API REST & Integração Agêntica

| Método | Rota | Descrição | Fonte |
| :---: | :--- | :--- | :---: |
| **POST** | `/api/v1/send` | Enviar email transacional individual. | `[F04]` |
| **POST** | `/api/v1/send/batch` | Enviar múltiplos emails em lote (mais eficiente). | `[F05]` |
| **GET** | `/api/v1/stats` | Obter estatísticas de envios (total, entregues, bounced). | `[F06]` |
| **GET** | `/api/v1/messages` | Listar histórico de emails enviados com filtros. | `[F07]` |
| **POST** | `/webhooks` | Endpoint que você cria para receber eventos de entrega/bounce. | `[F08]` |

### Matriz de Resolução de Problemas (Troubleshooting)

- **⚠️ Sintoma:** Emails não estão sendo enviados
  - **Causa:** Domínio não verificado ou DKIM inválido.
- **⚠️ Sintoma:** Emails retornando com 'Permanent Failure'
  - **Causa:** Endereço de email inválido ou lista negra de IP.
- **⚠️ Sintoma:** Fila de Sidekiq crescendo infinitamente
  - **Causa:** Worker de background morreu ou Redis cheio.
- **⚠️ Sintoma:** PostgreSQL reportando 'Disk full'
  - **Causa:** Histórico de mensagens muito antigo consumindo espaço.
- **⚠️ Sintoma:** Certificado SSL expirado em Caddy
  - **Causa:** Caddy não conseguiu renovar com Let's Encrypt.
## Parte III: Desinstalação Cirúrgica & Isolamento da VPS (Zero Efeito Colateral)

> 🛡️ **Princípio de Isolamento:** A desinstalação remove exclusivamente as credenciais de API do Cuttlefish, endpoints de integração e configurações da aplicação, preservando intactos os dados de emails já armazenados, histórico de entrega e regras de negócio.

### Passo 1: Auditoria de Integrações Cuttlefish
Encontrar todas as referências a Cuttlefish no código da aplicação.

```bash
grep -r 'cuttlefish\|Cuttlefish\|CUTTLEFISH' . --include='*.py' --include='*.js' --include='*.rb' --include='.env*' --include='*.yaml'
```

- ⚠️ **Alerta de Segurança:** NÃO remova arquivo nenhum ainda. Esta é apenas uma auditoria.
- ✅ **Como Validar:** `Listar todos os arquivos que contêm referências a Cuttlefish (API keys, endpoints, domínios)`

### Passo 2: Backup de Histórico & Exportação de Configurações Cuttlefish
Exportar domínios, templates de email e histórico de mensagens do Cuttlefish antes de desativar.

```bash
# Acessar console Cuttlefish > Export Data > Baixar arquivo CSV de mensagens e configurações
```

- ⚠️ **Alerta de Segurança:** Mantenha backups em local seguro e encriptado (local ou S3 privado).
- ✅ **Como Validar:** `Arquivo cuttlefish_backup.csv com histórico completo gerado`

### Passo 3: Ativar Postal em Paralelo (Blue-Green Deploy)
Postal e Cuttlefish rodando simultaneamente por 48-72h de teste de produção.

```bash
# Configurar seu backend para tentar enviar para Postal primeiro, fallback para Cuttlefish se erro
# Monitorar logs de ambos os sistemas durante período de teste
```

- ⚠️ **Alerta de Segurança:** Monitore ambos os sistemas 24/7 durante este período. NÃO desligue Cuttlefish ainda.
- ✅ **Como Validar:** `Ambos os sistemas entregando 100% das mensagens sem erro ou duplicatas`

### Passo 4: Migrar Domínios para Postal
Registrar domínios corporativos no Postal e copiar registros DKIM/SPF/DMARC para DNS.

```bash
# No Postal: Domains > Add Domain > transacional.empresa.com.br
# Copiar DKIM, SPF, DMARC records para seu provedor de DNS
# Aguardar propagação (5-30 min) > Verify Domain
```

- ⚠️ **Alerta de Segurança:** NÃO remova registros antigos de Cuttlefish do DNS até ter certeza que Postal está 100% funcional.
- ✅ **Como Validar:** `Postal exibir status 'Verified' para todos os domínios`

### Passo 5: Redirecionar Webhooks de Entrega & Bounce
Webhooks de entrega mudam de Cuttlefish para Postal.

```bash
# Alterar config de webhook: webhook_url = https://seu-dominio.com/api/postal/webhooks ao invés de https://cuttlefish.io/webhooks
# Registrar novo webhook no Postal com mesmo endpoint
```

- ⚠️ **Alerta de Segurança:** Valide que todos os webhooks estão sendo recebidos pelo backend ANTES de remover Cuttlefish.
- ✅ **Como Validar:** `curl seu-webhook-url e verificar que recebe dados de Postal (message.delivered, message.bounced)`

### Passo 6: Remover Credenciais Cuttlefish do .env
Deletar CUTTLEFISH_* das variáveis de ambiente.

```bash
unset CUTTLEFISH_API_KEY CUTTLEFISH_API_URL
grep -v CUTTLEFISH .env > .env.new && mv .env.new .env
grep CUTTLEFISH .env # Não retorna nada
```

- ⚠️ **Alerta de Segurança:** Não execute este passo sem confirmar que Postal está 100% funcional com todas as rotas.
- ✅ **Como Validar:** `grep CUTTLEFISH .env # Sem retorno significa sucesso`

### Passo 7: Downgrade & Cancelamento de Plano Cuttlefish
Reduzir plano Cuttlefish para free tier e iniciar período de retenção antes de cancelar.

```bash
# Acessar console Cuttlefish > Account Settings > Billing > Downgrade or Cancel
# Selecionar 'Keep history for 30 days before deletion'
```

- ⚠️ **Alerta de Segurança:** Cuttlefish pode levar até 30 dias para processar o cancelamento. Fique atento a cobranças residuais.
- ✅ **Como Validar:** `Console Cuttlefish exibir 'Free Account' ou 'Scheduled for Deletion' sem cobranças futuras`

### Checklist de Saúde da VPS (Outros Projetos)

- [ ] `docker compose ps # Confirma que Postal está 'Up' (4 containers: postal, postgres, redis, caddy)`
- [ ] `docker compose exec postgres psql -U postal -d postal -c 'SELECT COUNT(*) FROM messages;' # Valida banco de dados`
- [ ] `docker compose exec redis redis-cli DBSIZE # Verifica fila de trabalho (idealmente < 100 jobs pendentes)`
- [ ] `curl -s https://postal.seu-dominio.com.br/health | jq # Confirma API health check`
- [ ] `docker compose logs postal | tail -20 # Verifica erros recentes`
- [ ] `curl -s https://postal.seu-dominio.com.br/api/v1/stats -H 'Authorization: Bearer seu-token' | jq # Valida estatísticas de envio`

## Parte IV: Referências Bibliográficas Auditadas

| ID | Categoria | Título da Obra | Autor / Mantenedor | Link Oficial |
| :---: | :--- | :--- | :--- | :--- |
| **F01** | Documentação Oficial | Postal Official GitHub Repository & Documentation | Postal Server Team | [https://github.com/postalserver/postal](https://github.com/postalserver/postal) |
| **F02** | Framework | Docker Compose Official Documentation | Docker Inc. | [https://docs.docker.com/compose/](https://docs.docker.com/compose/) |
| **F03** | Framework | PostgreSQL 16 Official Documentation | PostgreSQL Global Development Group | [https://www.postgresql.org/docs/16/](https://www.postgresql.org/docs/16/) |
| **F04** | Framework | Redis Official Documentation & Best Practices | Redis Labs | [https://redis.io/documentation](https://redis.io/documentation) |
| **F05** | Security & Best Practices | Email Authentication: DKIM, SPF, DMARC Explained | MXToolbox & Email Security Community | [https://mxtoolbox.com/dkim.aspx](https://mxtoolbox.com/dkim.aspx) |
