# Manual Operacional Completo: Mailu

> **Padrão Diamante · Guia de Engenharia & Adoção Descomplicada**  
> **Licença:** AGPL-3.0 | **Versão:** 2.0.1 | **Setup Estimado:** 40 a 60 minutos (Conhecimento intermediário de DNS)  
> **VPS Recomendada:** Hetzner Cloud CPX21 (ou Contabo Cloud VPS M) (2 vCPU Dedicadas (AMD EPYC), 4 GB RAM ECC, 80 GB SSD (mínimo 50 GB para backups), Ubuntu 24.04 LTS (x86_64))  
> **Custo Mensal Estimado:** EUR 6,90/mês (~R$ 41,40/mês na cotação média)

---

## Módulo 0: Nivelamento Conceitual (Analogias do Dia a Dia)

### 💡 Mailu (A Ferramenta) *(Analogia: Sua Agência de Correios Privada em Casa)*
Assim como você poderia montar uma agência de correios dentro da sua garagem em vez de depender do Correios oficial, o Mailu é um servidor de email completo que você hospeda na sua VPS. Ele recebe, armazena, processa e envia emails com total soberania. Nenhum terceiro (como a Locaweb) guarda suas mensagens.

### 💡 MTA (Mail Transfer Agent) *(Analogia: O Carteiro que Entrega Correspondência Entre Agências)*
É o serviço que recebe emails de fora e os coloca nas caixas de correio dos seus usuários. No Mailu, ele roda automaticamente usando o Postfix, que é o padrão de ouro da internet desde 1998.

### 💡 IMAP & POP3 (Protocolos de Leitura) *(Analogia: Janelas de Vidro da sua Caixa de Correio)*
São os portais que seu Outlook, Gmail ou Thunderbird usam para ler seus emails remotamente sem ter que acessar a máquina dele pessoalmente. IMAP sincroniza em tempo real; POP3 apenas baixa e apaga.

### 💡 Spam & Antivírus (Escudo Digital) *(Analogia: O Detector de Encomendas Suspeitas na Entrada)*
Mailu vem com Rspamd (filtro de spam) e ClamAV (antivírus) integrados. Toda mensagem é verificada antes de chegar à sua caixa, bloqueando vírus e mensagens de scam.

### 💡 SPF, DKIM & DMARC (Assinatura Digital de Email) *(Analogia: Hologramas de Segurança do CPF em seus Emails)*
São certificados criptográficos que você coloca no seu domínio via DNS. Quando você envia um email de seu servidor Mailu para o Gmail ou Outlook, esses serviços verificam se o email realmente veio de você e não foi falsificado.

## Parte I: Instalação em Produção na VPS (Passo a Passo Rígido)

### Passo 1: Aquisição do Domínio & Delegação de Nameservers `[F01]`
Você compra um domínio (ex: empresa.com.br) em um registrador (NameCheap, GoDaddy, Registro.br) e aponta seus nameservers (DNS) para a VPS. Sem isso, ninguém consegue encontrar seu servidor de email na internet.

> 💡 **Entenda com uma analogia:** É como registrar sua agência de correios em um mapa da cidade para que as pessoas saibam onde entregar cartas.

```bash
# No painel do registrador, aponte os nameservers para:
# NS1: seu-ip.dominio.com.br
# NS2: seu-ip-backup.dominio.com.br (se disponível)
# Aguarde 12-24 horas para propagação global
```

- 🖥️ **O que você verá na tela:** Você receberá um painel de controle do registrador onde pode editar os registros DNS.
- ✅ **Como saber se deu certo:** Digite 'nslookup empresa.com.br' no terminal e ele retornará o IP da sua VPS.

### Passo 2: Blindagem Inicial & Hardening do Sistema Operacional `[F05]`
Criamos um usuário mailu dedicado, ativamos UFW firewall e aplicamos patches de segurança.

> 💡 **Entenda com uma analogia:** Instalar alarme, câmeras e reforçar as fechaduras da agência antes de começar a receber correspondência.

```bash
ssh root@SEU_IP
apt-get update && apt-get upgrade -y
adduser mailu && usermod -aG sudo mailu
ufw default deny incoming && ufw default allow outgoing
ufw allow 22/tcp && ufw allow 25/tcp && ufw allow 143/tcp && ufw allow 587/tcp && ufw allow 993/tcp && ufw allow 995/tcp && ufw allow 80/tcp && ufw allow 443/tcp
ufw --force enable
```

- 🖥️ **O que você verá na tela:** Mensagens de confirmação de firewall ativo e regras de entrada/saída definidas.
- ✅ **Como saber se deu certo:** Execute 'ufw status' e veja todas as portas de email listadas com ALLOW IN.

### Passo 3: Instalação do Docker & Docker Compose `[F02]`
Mailu roda através de containers Docker, que isolam o servidor de email de outros serviços. Sem Docker, seria necessário configurar Postfix, Dovecot, Sieve, etc manualmente (um pesadelo).

> 💡 **Entenda com uma analogia:** Encomendar um escritório modular pré-montado em vez de construir a agência de zero com tijolos.

```bash
apt-get install -y ca-certificates curl
curl -fsSL https://get.docker.com | sh
usermod -aG docker mailu
curl -SL https://github.com/docker/compose/releases/download/v2.29.1/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
```

- 🖥️ **O que você verá na tela:** Download de pacotes Docker durante 2-3 minutos.
- ✅ **Como saber se deu certo:** Execute 'docker --version' e retorna 'Docker version 27.x.x' ou superior.

### Passo 4: Clone do Repositório Oficial Mailu & Configuração Inicial `[F01]`
Baixamos o código-fonte oficial do Mailu do GitHub e rodamos o assistente de configuração interativo.

> 💡 **Entenda com uma analogia:** Descarregar o manual de operação da agência e preencher os formulários iniciais.

```bash
cd /opt
git clone https://github.com/Mailu/Mailu.git mailu
cd /opt/mailu
python3 setup.py
```

- 🖥️ **O que você verá na tela:** Uma série de perguntas na tela: qual é seu domínio, quantos usuários, qual certificado SSL, etc.
- ✅ **Como saber se deu certo:** O arquivo /opt/mailu/.env será gerado com todas as configurações.

### Passo 5: Inicialização dos Containers Mailu (Docker Compose Up) `[F02]`
Levantamos os containers de Postfix (MTA), Dovecot (IMAP), Rspamd (antispam), Webmail e Admin simultaneamente.

> 💡 **Entenda com uma analogia:** Ligar a energia, os sistemas de ar, alarme e iluminação da agência ao mesmo tempo.

```bash
cd /opt/mailu
docker-compose up -d
docker-compose ps
```

- 🖥️ **O que você verá na tela:** Docker fará o pull das imagens oficiais (200-300 MB) e exibirá logs de inicialização.
- ✅ **Como saber se deu certo:** Execute 'docker ps' e veja 8-10 containers rodando com status 'Up'.

### Passo 6: Configuração de Registros DNS (SPF, DKIM, DMARC) `[F05]`
Criamos certificados criptográficos no DNS que assinam cada email enviado. Sem isso, Gmail e Outlook rejeitarão seus emails.

> 💡 **Entenda com uma analogia:** Colocar o holograma de segurança em cada envelope que sai da agência.

```bash
# 1. Entre no painel de admin: https://empresa.com.br/admin
# 2. Vá em 'Configurações de Domínio'
# 3. Copie os registros TXT de SPF, DKIM e DMARC
# 4. Cole-os no painel DNS do seu registrador
# 5. Aguarde 2-4 horas para propagação
dig empresa.com.br MX  # Valida MX
dig mailu._domainkey.empresa.com.br TXT  # Valida DKIM
```

- 🖥️ **O que você verá na tela:** O painel admin de Mailu exibirá os registros DNS exatos que você deve copiar.
- ✅ **Como saber se deu certo:** Use a ferramenta MXToolbox para validar: MX, SPF, DKIM e DMARC aparecem com checkmark verde.

### Passo 7: Teste de Saúde & Primeiro Email Enviado `[F01]`
Verificamos que o servidor pode receber e enviar emails, que o antivírus está ativo e que os logs indicam 0 erros.

> 💡 **Entenda com uma analogia:** Fazer um teste de funcionamento da agência antes de abrir ao público.

```bash
# Via admin:
# 1. Crie um usuário de teste: admin@empresa.com.br
# 2. Envie um email de teste para seu Gmail pessoal
# 3. Verifique que o email chegou com SPF=pass, DKIM=pass no cabeçalho
```

- 🖥️ **O que você verá na tela:** Confirmação de entrega do email de teste e ausência de rejeições.
- ✅ **Como saber se deu certo:** Acesse https://empresa.com.br/webmail e leia o email de teste recebido.

## Arquivos de Configuração de Produção

### `/opt/mailu/docker-compose.yml`
*Orquestração de 6 containers: front (proxy SMTP/IMAP), admin (painel), imap (Dovecot), smtp (Postfix), redis (cache) e db (banco PostgreSQL). Todas as comunicações são internas; apenas front expõe portas ao mundo.*

```yaml
version: '3.8'
services:
  front:
    image: mailu/nginx:2.0.1
    restart: always
    ports:
      - "80:80"
      - "443:443"
      - "25:25"
      - "465:465"
      - "587:587"
      - "143:143"
      - "993:993"
      - "995:995"
    volumes:
      - ./data/certs:/etc/letsencrypt
    depends_on:
      - admin
      - webmail

  admin:
    image: mailu/admin:2.0.1
    restart: always
    environment:
      - SECRET_KEY=${SECRET_KEY}
      - DATABASE_URL=postgresql://mailu:${DB_PASSWORD}@db/mailu
    depends_on:
      - db
      - redis

  imap:
    image: mailu/dovecot:2.0.1
    restart: always
    volumes:
      - ./data/mail:/mail

  smtp:
    image: mailu/postfix:2.0.1
    restart: always
    volumes:
      - ./data/mail:/mail

  redis:
    image: redis:7-alpine
    restart: always

  db:
    image: postgres:16-alpine
    restart: always
    environment:
      - POSTGRES_DB=mailu
      - POSTGRES_PASSWORD=${DB_PASSWORD}
    volumes:
      - ./data/db:/var/lib/postgresql/data

networks:
  default:
    name: mailu-net
```

### `/opt/mailu/.env.example`
*Arquivo de configuração centralizado. Customize com seu domínio, senhas fortes e preferências de segurança.*

```bash
# Domínio e hostname
DOMAIN=empresa.com.br
HOSTNAME=mail.empresa.com.br

# Senhas e Segredo
SECRET_KEY=mudeme123456789abcdefg
DB_PASSWORD=mudeme_db_senha_forte_aqui

# Certificado SSL (Let's Encrypt automático)
TLS_FLAVOR=letsencrypt

# Filtros de Spam e Antivírus
SPAM_LEVEL=10
VIRUS_ENABLED=true

# Limites de Taxa (rate-limit)
RELAY_DOMAIN=empresa.com.br
RELAY_HOST=
RELAY_PORT=25
```

## Parte II: Manual de Uso Exaustivo

**Arquitetura Operacional:** Mailu é um servidor de email autossuficiente: ele recebe mensagens de fora (SMTP 25), guarda nos usuários locais (banco de dados PostgreSQL), permite leitura via IMAP (porta 143/993) e oferece uma interface webmail em HTML5. Nenhum email sai da VPS sem sua autorização. O antivírus ClamAV e o filtro Rspamd rodam em paralelo, capturando spam e vírus antes de chegar às caixas.

### Roteiro de Primeiro Voo (Sua Primeira Reunião em 3 Minutos)

1. **Passo 1: Acessar o Painel de Administração:** Abra https://empresa.com.br/admin no navegador. Faça login com admin@empresa.com.br e a senha que configurou.
   - 🎯 **Resultado Esperado:** Você verá o dashboard com estatísticas de usuários, domínios e emails recebidos.

1. **Passo 2: Criar Primeiro Usuário de Email:** No painel Admin, clique em 'Usuários' → 'Adicionar'. Preencha nome, email (ex: joao@empresa.com.br) e senha forte. Clique em Salvar.
   - 🎯 **Resultado Esperado:** O novo usuário aparecerá na lista e receberá um email de boas-vindas no webmail.

1. **Passo 3: Configurar Seu Cliente (Thunderbird, Outlook, iPhone):** IMAP: mail.empresa.com.br porta 993 com TLS. SMTP: mail.empresa.com.br porta 587 com TLS. Insira joao@empresa.com.br e a senha.
   - 🎯 **Resultado Esperado:** O cliente sincronizará as pastas INBOX, Drafts, Sent e Trash do servidor.

1. **Passo 4: Enviar Email de Teste:** Do seu cliente local, envie um email para seu Gmail pessoal. Verifique que chegou e inspecione o cabeçalho (Show original) para confirmar SPF=pass e DKIM=pass.
   - 🎯 **Resultado Esperado:** O email chega na caixa de entrada (não em spam) com SPF=pass, DKIM=pass e DMARC=pass no cabeçalho.

### Dicionário Completo de Comandos (CLI)

| Comando / Flag | Descrição Técnica | Exemplo de Execução | Fonte |
| :--- | :--- | :--- | :---: |
| `docker-compose logs -f smtp` | Acompanha em tempo real os logs de recebimento de emails (Postfix). | `Você verá 'accept message' para cada email recebido.` | `[F02]` |
| `docker-compose logs -f imap` | Monitora as conexões IMAP (clientes lendo emails). | `Você verá 'user=joao' para cada login.` | `[F02]` |
| `docker-compose exec admin flask mailu admin create admin@empresa.com.br` | Cria um novo administrador via CLI sem entrar no painel web. | `Será solicitada uma senha forte.` | `[F01]` |
| `docker-compose restart smtp` | Reinicia apenas o serviço SMTP/Postfix sem derrubar IMAP ou banco de dados. | `Útil após editar configurações de rateLimit.` | `[F02]` |

### Endpoints de API REST & Integração Agêntica

| Método | Rota | Descrição | Fonte |
| :---: | :--- | :--- | :---: |
| **GET** | `/admin/antispam/status` | Retorna estatísticas de emails bloqueados por spam nos últimos 7 dias. | `[F01]` |
| **POST** | `/admin/users` | Cria um novo usuário de email via JSON. | `[F04]` |

### Matriz de Resolução de Problemas (Troubleshooting)

- **⚠️ Sintoma:** Emails de fora não chegam (erro 550)
  - **Causa:** Registros DNS SPF, DKIM ou DMARC não estão configurados corretamente.
- **⚠️ Sintoma:** Clientes não conseguem conectar em IMAP (porta 993 timeout)
  - **Causa:** Firewall bloqueando a porta ou certificado SSL expirado.
- **⚠️ Sintoma:** Caixa de entrada cheia, disco lotado
  - **Causa:** Nenhum backup é feito automaticamente; o disco está em 100%.
## Parte III: Desinstalação Cirúrgica & Isolamento da VPS (Zero Efeito Colateral)

> 🛡️ **Princípio de Isolamento:** A desinstalação remove exclusivamente os containers Mailu, volumes de dados de email e certificados SSL, preservando intactos o Docker, firewall, banco de dados PostgreSQL compartilhado (se houver) e outros serviços na VPS.

### Passo 1: Backup de Segurança (Exportar Todos os Emails & Configurações)
Antes de remover, fazemos backup de todos os emails, configurações de usuários e certificados SSL.

```bash
cd /opt/mailu
mkdir -p backups
docker-compose exec db pg_dump -U postgres mailu > backups/mailu-$(date +%Y%m%d).sql
tar -czf backups/mailu-certs-$(date +%Y%m%d).tar.gz ./data/certs/
du -sh backups/  # Confirma tamanho do backup
```

- ⚠️ **Alerta de Segurança:** Nunca delete a pasta /opt/mailu até confirmar que o backup foi feito com sucesso.
- ✅ **Como Validar:** `ls -lah backups/ # Arquivos de backup recentes com tamanho > 0`

### Passo 2: Parada Ordeira dos Containers Mailu
Interrompe todos os containers Mailu permitindo que encerrem gracefully, sem matar processos abruptamente.

```bash
cd /opt/mailu
docker-compose down --remove-orphans
```

- ⚠️ **Alerta de Segurança:** NÃO use 'docker kill' ou 'docker-compose rm -f'. Isso corrompe o banco de dados PostgreSQL.
- ✅ **Como Validar:** `docker ps | grep mailu # Não deve constar nada`

### Passo 3: Remoção de Volumes de Dados (Mails, DB, Cache)
Remove os volumes Docker que armazenam emails, banco de dados PostgreSQL e cache Redis do Mailu.

```bash
docker volume rm mailu_maildata 2>/dev/null || true
docker volume rm mailu_db 2>/dev/null || true
docker volume rm mailu_redis 2>/dev/null || true
docker volume ls | grep -i mailu  # Não deve retornar nada
```

- ⚠️ **Alerta de Segurança:** Esta ação é IRREVERSÍVEL. Certifique-se que o backup foi feito no Passo 1.
- ✅ **Como Validar:** `Nenhum volume Docker com 'mailu' no nome deve constar em 'docker volume ls'`

### Passo 4: Revogação de Portas no Firewall
Fecha exclusivamente as portas de email (25, 143, 587, 993, 995) sem interferir em SSH (22), HTTP (80) ou HTTPS (443).

```bash
sudo ufw delete allow 25/tcp
sudo ufw delete allow 143/tcp
sudo ufw delete allow 587/tcp
sudo ufw delete allow 993/tcp
sudo ufw delete allow 995/tcp
sudo ufw reload
sudo ufw status | grep -E '25|143|587|993|995'  # Não deve constar
```

- ⚠️ **Alerta de Segurança:** Mantenha o firewall ativo e nunca desabilite UFW.
- ✅ **Como Validar:** `sudo ufw status numbered | grep -v 25 | grep -v 143 | grep -v 587 | grep -v 993 | grep -v 995`

### Passo 5: Remoção de Pastas e Arquivo de Configuração
Remove a pasta /opt/mailu e limpa o arquivo docker-compose.yml para liberar espaço em disco.

```bash
# Opção 1: Remover completamente
sudo rm -rf /opt/mailu

# Opção 2: Manter backups (recomendado)
sudo mv /opt/mailu /opt/mailu-backup-archived
ls -la /opt/  # Confirma que /opt/mailu não existe mais
```

- ⚠️ **Alerta de Segurança:** Se escolher Opção 1, os backups em backups/ serão deletados também. Considere copiar para outro local: scp backups/ usuario@outra-vps:/backups
- ✅ **Como Validar:** `which docker-compose mailu  # Não deve encontrar`

### Passo 6: Remoção de Imagens Docker Mailu (Opcional)
Remove as imagens Docker do Mailu para liberar espaço de disco (~500 MB).

```bash
docker image rm -f mailu/nginx:2.0.1 mailu/admin:2.0.1 mailu/dovecot:2.0.1 mailu/postfix:2.0.1 2>/dev/null || true
docker images | grep -i mailu  # Não deve retornar nada
```

- ⚠️ **Alerta de Segurança:** Somente execute se tiver certeza que não vai reinstalar Mailu em breve.
- ✅ **Como Validar:** `docker image ls | grep mailu # Deve estar vazio`

### Checklist de Saúde da VPS (Outros Projetos)

- [ ] `free -h # Confirma devolução de memória RAM`
- [ ] `df -h # Confirma devolução de espaço em disco em /opt`
- [ ] `docker ps # Confirma ausência de containers Mailu`
- [ ] `docker volume ls # Confirma ausência de volumes Mailu`
- [ ] `netstat -tulpn | grep -E '25|143|587|993|995' # Confirma que portas de email estão liberadas`

## Parte IV: Referências Bibliográficas Auditadas

| ID | Categoria | Título da Obra | Autor / Mantenedor | Link Oficial |
| :---: | :--- | :--- | :--- | :--- |
| **F01** | Documentação Oficial | Mailu Official Documentation & Architecture | Mailu Core Team & Community | [https://mailu.io/latest/](https://mailu.io/latest/) |
| **F02** | Documentação Oficial | Mailu GitHub Repository & Deployment Guides | Mailu Open Source | [https://github.com/Mailu/Mailu](https://github.com/Mailu/Mailu) |
| **F03** | Livro / Guia Técnico | Postfix, Dovecot & DKIM: A Complete Email Server Setup | Wietse Venema & Community | [https://www.postfix.org/OVERVIEW.html](https://www.postfix.org/OVERVIEW.html) |
| **F04** | Vídeo / YouTube | Self-Hosted Email Server: Mailu Complete Tutorial | Open Source DevOps Channels | [https://www.youtube.com/results?search_query=mailu+self+hosted+email](https://www.youtube.com/results?search_query=mailu+self+hosted+email) |
| **F05** | Curso / Tutorial | Email Server Hardening & SPF/DKIM/DMARC Configuration | Mailu Documentation & Community | [https://github.com/Mailu/Mailu/tree/master/docs](https://github.com/Mailu/Mailu/tree/master/docs) |
