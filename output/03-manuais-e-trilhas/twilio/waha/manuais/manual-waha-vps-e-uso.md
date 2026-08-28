# Manual Operacional Completo: WAHA (WhatsApp HTTP API Gateway)

> **Padrão Diamante · Guia de Engenharia & Adoção Descomplicada** 
> **Licença:** Apache-2.0 | **Versão:** 0.43.0 | **Setup Estimado:** 30 min (Conhecimento intermediário de Docker) 
> **VPS Recomendada:** Hetzner Cloud CPX21 ou Linode Nanode (2 vCPU Dedicadas, 4 GB RAM, 80 GB SSD NVMe, Ubuntu 24.04 LTS) 
> **Custo Mensal Estimado:** EUR 6,00/mês (~R$ 36,00)

---

## Módulo 0: Nivelamento Conceitual (Analogias do Dia a Dia)

### WhatsApp Web Socket Bridge *(Analogia: O Porteiro que Atende Mensagens)*
WAHA conecta à sessão WhatsApp Web de um número e monitora todas as mensagens. Quando uma chega, ele avisa seu sistema via webhook. É como ter um porteiro que escreve um bilhete cada vez que alguém chama.

### Webhook para Entrega & Recebimento *(Analogia: O Carteiro que Bate na Porta)*
Quando WAHA recebe uma mensagem ou quando um envio é confirmado, ele bate na porta do seu servidor (via POST HTTP) com os dados. Seu backend não precisa ficar perguntando, ele só recebe a notificação.

### Múltiplas Sessões WhatsApp *(Analogia: Múltiplos Números de WhatsApp)*
Um mesmo servidor WAHA pode gerenciar 10, 100 ou 1.000 números diferentes. Cada número é independente com sua própria autenticação e sessão.

## Parte I: Instalação em Produção na VPS (Passo a Passo Rígido)

### Passo 1: Hardening & Firewall (UFW) `[F01]`
Configurar acesso restrito à VPS com apenas portas essenciais.

> **Entenda com uma analogia:** Trancar o prédio e deixar apenas a guarita.

```bash
ufw default deny incoming
ufw default allow outgoing
ufw allow 22/tcp && ufw allow 80/tcp && ufw allow 443/tcp
ufw --force enable
```

- **O que você verá na tela:** Mensagem 'Firewall is active and enabled'.
- **Como saber se deu certo:** ufw status mostra portas 22, 80, 443 como ALLOW.

### Passo 2: Instalação de Docker & Docker Compose `[F02]`
Preparar o motor de containers.

> **Entenda com uma analogia:** Montar a bancada de trabalho.

```bash
apt-get update && apt-get install -y docker.io docker-compose-v2
usermod -aG docker $USER
```

- **O que você verá na tela:** Pacotes instalados sem erro.
- **Como saber se deu certo:** docker --version retorna Docker 27+.

### Passo 3: Criação de Diretórios de Volumes `[F03]`
Preparar pastas persistentes para sessões e logs.

> **Entenda com uma analogia:** Criar gavetas para guardar dados.

```bash
mkdir -p /opt/waha/{sessions,logs,backups}
cd /opt/waha
```

- **O que você verá na tela:** Diretórios criados sem erro.
- **Como saber se deu certo:** ls -d /opt/waha/{sessions,logs} existem.

### Passo 4: Deploy com Docker Compose `[F04]`
Levantamento da stack (WAHA + Redis + Caddy).

> **Entenda com uma analogia:** Ligar as máquinas.

```bash
export WAHA_API_KEY=$(openssl rand -base64 32)
docker compose up -d
docker compose ps
```

- **O que você verá na tela:** Containers iniciando com logs coloridos.
- **Como saber se deu certo:** docker compose ps mostra 3 containers em status Up.

### Passo 5: Pareamento via QR Code & Teste de Conexão `[F05]`
Conectar número WhatsApp ao gateway.

> **Entenda com uma analogia:** Reconhecer o telefone.

```bash
curl -X POST http://localhost:3000/api/sessions/default/start | jq
# Escanear QR Code com WhatsApp
```

- **O que você verá na tela:** QR Code aparece após segundos.
- **Como saber se deu certo:** Status da sessão muda para 'CONNECTED'.

## Arquivos de Configuração de Produção

### `/opt/waha/docker-compose.yml`
*Stack completa com WAHA, Redis e Caddy para proxy HTTPS.*

```yaml
version: '3.8'
services:
 waha:
 image: devlikeapro/waha:latest
 container_name: waha-api
 restart: unless-stopped
 ports:
 - '3000:3000'
 - '5000:5000'
 environment:
 WHATSAPP_API_KEY: ${WAHA_API_KEY}
 DEBUG: waha:*
 NODE_ENV: production
 volumes:
 - waha_sessions:/app/.sessions
 - waha_logs:/app/logs
 networks:
 - waha_net
 redis:
 image: redis:7-alpine
 restart: unless-stopped
 ports:
 - '6379:6379'
 volumes:
 - redis_data:/data
 networks:
 - waha_net
 caddy:
 image: caddy:2-alpine
 restart: unless-stopped
 ports:
 - '80:80'
 - '443:443'
 volumes:
 - ./Caddyfile:/etc/caddy/Caddyfile
 - caddy_data:/data
 - caddy_config:/config
 networks:
 - waha_net
volumes:
 waha_sessions:
 waha_logs:
 redis_data:
 caddy_data:
 caddy_config:
networks:
 waha_net:
 driver: bridge
```

### `/opt/waha/Caddyfile`
*Proxy reverso com SSL automático e rate limiting anti-spam.*

```caddyfile
whatsapp.seu-dominio.com {
 encode gzip
 header {
 Strict-Transport-Security "max-age=31536000"
 X-Content-Type-Options nosniff
 }
 reverse_proxy localhost:5000 {
 header_uri X-Real-IP {http.request.remote.host}
 }
 rate_limit /api/sendText 100 100
}
```

### `/opt/waha/.env`
*Variáveis de ambiente para autenticação e config.*

```bash
WAHA_API_KEY=seu-chave-api-de-32-caracteres-aqui
WAHA_PORT=5000
REDIS_HOST=redis
REDIS_PORT=6379
NODE_ENV=production
```

## Parte II: Manual de Uso Exaustivo

**Arquitetura Operacional:** WAHA é um gateway HTTP que fica sempre conectado a um número WhatsApp. Mensagens entrantes geram webhooks para seu backend. Mensagens saintes vão via POST /api/sendText. Tudo é criptografado pelo WhatsApp (E2E), WAHA não armazena conteúdo, apenas metadados de entrega.

### Roteiro de Primeiro Voo (Sua Primeira Reunião em 3 Minutos)

1. **Passo 1: Acessar Dashboard:** Abra http://localhost:3000 para ver interface de sessões.
 - **Resultado Esperado:** Página de dashboard com botão 'Start Session'.

1. **Passo 2: Iniciar Sessão & Parear:** Clique em 'Start Session'. QR Code aparecerá. Scaneie com seu WhatsApp.
 - **Resultado Esperado:** Status muda para 'CONNECTED' em 5-10 segundos.

1. **Passo 3: Enviar Mensagem de Teste:** Execute: curl -X POST http://localhost:5000/api/sendText -H 'X-API-Key: seu-token' -H 'Content-Type: application/json' -d '{"chatId": "5511988776655@c.us", "text": "Olá!"}'
 - **Resultado Esperado:** Resposta JSON com messageId. Mensagem chega no WhatsApp.

1. **Passo 4: Configurar Webhook:** No WAHA, configure seu endpoint POST para receber eventos de mensagens.
 - **Resultado Esperado:** Quando alguém envia mensagem, seu backend recebe webhook.

### Dicionário Completo de Comandos (CLI)

| Comando / Flag | Descrição Técnica | Exemplo de Execução | Fonte |
| :--- | :--- | :--- | :---: |
| `docker compose ps` | Ver status dos containers. | `docker compose ps` | `[F01]` |
| `docker compose logs -f waha` | Ver logs em tempo real do WAHA. | `docker compose logs -f waha --tail=50` | `[F02]` |
| `docker compose restart waha` | Reiniciar container WAHA. | `docker compose restart waha` | `[F03]` |

### Endpoints de API REST & Integração Agêntica

| Método | Rota | Descrição | Fonte |
| :---: | :--- | :--- | :---: |
| **POST** | `/api/sendText` | Envia mensagem de texto. | `[F04]` |
| **POST** | `/api/sendMedia` | Envia imagem, vídeo ou documento. | `[F05]` |
| **GET** | `/api/me` | Retorna dados do número conectado. | `[F06]` |

### Matriz de Resolução de Problemas (Troubleshooting)

- ** Sintoma:** Sessão desconecta aleatoramente
 - **Causa:** WhatsApp Web marcou a sessão como inativa.
- ** Sintoma:** Webhook não está recebendo mensagens
 - **Causa:** URL do webhook está incorreta ou backend não responde.
- ** Sintoma:** Mensagens não marcam como 'delivered'
 - **Causa:** Rate limiting ou fila congestionada.
- ** Sintoma:** QR Code não aparece
 - **Causa:** Sessão anterior ainda ativa.
- ** Sintoma:** Erro 401 Unauthorized
 - **Causa:** API Key ausente ou inválida.
## Parte III: Desinstalação Cirúrgica & Isolamento da VPS (Zero Efeito Colateral)

> **Princípio de Isolamento:** A desinstalação remove exclusivamente as credenciais Twilio, endpoints de webhook e configurações da aplicação, preservando intactos os dados de mensagens já recebidas, histórico e infraestrutura de WAHA.

### Passo 1: Auditoria de Integrações Twilio
Encontrar todas as referências a Twilio no código.

```bash
grep -r 'twilio\|Twilio\|TWILIO' . --include='*.py' --include='*.js' --include='*.env*'
```

- **Alerta de Segurança:** NÃO remova arquivo nenhum ainda. Esta é apenas uma auditoria.
- **Como Validar:** `Listar todos os arquivos que contêm referências a Twilio`

### Passo 2: Backup de Histórico
Exportar logs de mensagens Twilio antes de desativar.

```bash
# Login no console Twilio e exporte o histórico de mensagens via API ou web UI
```

- **Alerta de Segurança:** Mantenha backups em local seguro e encriptado.
- **Como Validar:** `Arquivo twilio_backup.json com histórico completo gerado`

### Passo 3: Ativar WAHA em Paralelo (Blue-Green)
WAHA e Twilio rodando simultaneamente por 24-48h de teste.

```bash
# Configurar router/switch em aplicação para tentar WAHA primeiro, fallback para Twilio
```

- **Alerta de Segurança:** Monitore ambos os sistemas durante este período. Não desligue Twilio ainda.
- **Como Validar:** `Ambos os sistemas processando 100% das mensagens sem erro`

### Passo 4: Redirecionar Webhooks Entrantes
Webhooks de entrada mudam de Twilio para WAHA.

```bash
# Alterar config: webhook_url = https://seu-dominio.com/api/webhooks ao invés de https://twilio.webhook...
```

- **Alerta de Segurança:** Valide que todos os webhooks estão sendo recebidos antes de prosseguir.
- **Como Validar:** `curl seu-webhook-url e verificar que recebe dados de WAHA`

### Passo 5: Remover Credenciais Twilio do .env
Deletar TWILIO_* das variáveis de ambiente.

```bash
unset TWILIO_ACCOUNT_SID TWILIO_AUTH_TOKEN
grep -v TWILIO .env > .env.new && mv .env.new .env
```

- **Alerta de Segurança:** Não execute este passo sem confirmar que WAHA está 100% funcional.
- **Como Validar:** `grep TWILIO .env # Não retorna nada`

### Passo 6: Downgrade & Shutdown de Twilio
Reduzir plano Twilio para free tier e aguardar período de retenção.

```bash
# Acessar console Twilio > Account > Billing > Downgrade Account
```

- **Alerta de Segurança:** Twilio pode levar até 30 dias para processar o downgrade. Fique atento a cobranças.
- **Como Validar:** `Console Twilio exibir 'Free Account' sem cobranças futuras`

### Checklist de Saúde da VPS (Outros Projetos)

- [ ] `docker compose ps # Confirma que WAHA está 'Up'`
- [ ] `docker compose logs waha | tail -20 # Verifica erros recentes`
- [ ] `curl -s http://localhost:3000/api/me | jq # Confirma sessão WhatsApp conectada`
- [ ] `curl -s https://seu-dominio.com/health | jq # Valida saúde geral da API`
- [ ] `docker stats # Confirma uso de CPU/memória dentro do esperado`

## Parte IV: Referências Bibliográficas Auditadas

| ID | Categoria | Título da Obra | Autor / Mantenedor | Link Oficial |
| :---: | :--- | :--- | :--- | :--- |
| **F01** | Documentação Oficial | WAHA Official GitHub Repository & API Docs | DevLike ApPro (WAHA Core Team) | [https://github.com/devlikeapro/waha](https://github.com/devlikeapro/waha) |
| **F02** | Documentação Oficial | WAHA Docker Hub & Container Registry | DevLike ApPro | [https://hub.docker.com/r/devlikeapro/waha](https://hub.docker.com/r/devlikeapro/waha) |
| **F03** | Framework | Docker Compose Official Documentation | Docker Inc. | [https://docs.docker.com/compose/](https://docs.docker.com/compose/) |
| **F04** | Framework | Caddy Web Server & Reverse Proxy | Caddy Community | [https://caddyserver.com/docs/](https://caddyserver.com/docs/) |
| **F05** | Best Practices | WhatsApp Business API & Compliance | Meta Platforms Inc. | [https://www.whatsapp.com/business/](https://www.whatsapp.com/business/) |
