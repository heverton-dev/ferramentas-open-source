# Manual Operacional Completo: Modoboa

> **Padrão Diamante · Guia de Engenharia & Adoção Descomplicada** 
> **Licença:** AGPL-3.0 | **Versão:** 2.3.0 | **Setup Estimado:** 30 a 45 minutos (Zero conhecimento prévio) 
> **VPS Recomendada:** Locaweb VPS G2 (ou Hetzner Cloud CX31) (4 vCPU Dedicadas (Intel Xeon / AMD EPYC), 8 GB RAM ECC, 160 GB SSD NVMe Gen4, Ubuntu 24.04 LTS (x86_64)) 
> **Custo Mensal Estimado:** R$ 150,00/mês (Locaweb) ou EUR 14,00/mês (Hetzner)

---

## Módulo 0: Nivelamento Conceitual (Analogias do Dia a Dia)

### Modoboa (A Ferramenta) *(Analogia: Seu Próprio Google Workspace Hospedado no Seu Servidor)*
Modoboa é uma plataforma completa de email e colaboração que você instala dentro da sua própria VPS. Ela oferece webmail (como Gmail), calendário (como Google Calendar), contatos sincronizados e filtros antispam — tudo sob seu controle total, sem pagar por usuário ou domínio para terceiros.

### VPS (Servidor Privado Virtual) *(Analogia: Uma Sala Comercial Alugada que Nunca Apaga a Luz)*
Em vez de usar email do Gmail ou Outlook da Microsoft, você aluga por cerca de R$ 80 a R$ 150 por mês um computador profissional em um data center na nuvem (como a Locaweb, Hetzner ou Contabo). Ele fica ligado o tempo todo com backup automático e geradores de energia, pronto para rodar seu email 24/7.

### SMTP / IMAP / POP3 (Protocolos de Email) *(Analogia: Os Correios e a Caixa de Entrada Universal)*
SMTP é como enviar uma carta pelos Correios (envia email saindo). IMAP é como ter uma caixa de correio que você pode acessar de qualquer lugar (recebe email, sincroniza). POP3 é o antiquado que baixa e apaga (não recomendado). Modoboa fala todos os três para funcionar com qualquer cliente de email.

### SSH (Conexão Segura) *(Analogia: Um Túnel Secreto de Controle Remoto)*
É a tecnologia que liga o teclado do seu computador atual diretamente ao seu servidor na nuvem. Você digita na sua casa e o comando é executado lá com criptografia blindada.

### Docker & Containers *(Analogia: Uma Caixa de Sapatos Lacrada de Fábrica)*
Modoboa e seus dependências (banco de dados PostgreSQL, Redis cache, Nginx proxy) vêm pré-configurados dentro de um container Docker. Você não precisa instalar cada pedaço separadamente — basta mandar a caixa abrir.

### Firewall (UFW) *(Analogia: O Porteiro do Condomínio com Crachá Rígido)*
Um servidor tem milhares de portas virtuais. O Firewall tranca tudo e só permite: SSH (porta 22 para você controlar), email (portas 25, 110, 143, 465, 587, 993, 995) e web (80 e 443).

## Parte I: Instalação em Produção na VPS (Passo a Passo Rígido)

### Passo 1: Alugar o Servidor VPS e Obter o Endereço IP `[F01]`
Acesse locaweb.com.br, crie sua conta, escolha VPS G2 com Ubuntu 24.04 LTS e conclua a compra. Você receberá por email o IP (ex: 192.168.1.100) e a senha root. Salve esses dados em um lugar seguro.

> **Entenda com uma analogia:** Pegar a chave da sua nova sala comercial e guardar em local seguro.

```bash
# No seu computador (Windows PowerShell ou Mac Terminal):
ssh root@SEU_IP_AQUI
```

- **O que você verá na tela:** Um email chega com 'Seu servidor foi criado com sucesso. IP: XXX.XXX.XXX.XXX'.
- **Como saber se deu certo:** Você consegue fazer login no painel de controle da Locaweb e ver o servidor com status 'Online'.

### Passo 2: Blindagem Inicial: Criar Usuário Seguro e Ativar Firewall `[F05]`
Criamos um usuário chamado 'modoboa' (não usar root todos os dias) e ativamos o firewall UFW para liberar apenas as portas necessárias.

> **Entenda com uma analogia:** Instalar fechaduras tetra e colocar o porteiro com lista de convidados permitidos.

```bash
adduser modoboa && usermod -aG sudo modoboa
ufw default deny incoming && ufw default allow outgoing
ufw allow 22/tcp && ufw allow 25/tcp && ufw allow 80/tcp && ufw allow 110/tcp && ufw allow 143/tcp && ufw allow 443/tcp && ufw allow 465/tcp && ufw allow 587/tcp && ufw allow 993/tcp && ufw allow 995/tcp
ufw --force enable
```

- **O que você verá na tela:** O sistema pedirá senha e confirmará 'Firewall is active and enabled on system startup'.
- **Como saber se deu certo:** Digite 'ufw status' e veja portas 22, 25, 80, 110, 143, 443, 465, 587, 993, 995 marcadas como 'ALLOW IN'.

### Passo 3: Instalação do Docker e Docker Compose `[F02]`
Instalamos o motor Docker para rodar Modoboa em um container isolado junto com PostgreSQL, Redis e Nginx, tudo em perfeita harmonia.

> **Entenda com uma analogia:** Montar as prateleiras industriais no galpão para receber as caixas lacradas.

```bash
apt-get update && apt-get install -y ca-certificates curl
curl -fsSL https://get.docker.com | sh
usermod -aG docker modoboa
curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
```

- **O que você verá na tela:** Linhas de download e compilação passam pela tela durante 2 a 3 minutos.
- **Como saber se deu certo:** Execute 'docker --version' e veja 'Docker version 27.x.x' ou superior.

### Passo 4: Criação das Pastas de Dados e Configuração do Modoboa `[F01]`
Criamos a pasta /opt/modoboa/ que abrigará os dados de email, calendários, contatos, configurações e arquivos de dependências.

> **Entenda com uma analogia:** Montar a escrivaninha e criar as gavetas onde os documentos serão arquivados.

```bash
mkdir -p /opt/modoboa/{data,postgres,redis}
chown -R modoboa:modoboa /opt/modoboa
chmod -R 750 /opt/modoboa
```

- **O que você verá na tela:** As pastas são criadas silenciosamente em menos de 1 segundo.
- **Como saber se deu certo:** O comando 'ls -ld /opt/modoboa' mostra a pasta pertencendo ao usuário 'modoboa'.

### Passo 5: Iniciar Modoboa com Docker Compose `[F02]`
Iniciamos o Modoboa, PostgreSQL, Redis e Nginx em segundo plano. O sistema baixa as imagens oficiais e começa a rodar imediatamente.

> **Entenda com uma analogia:** Apertar o botão verde no painel elétrico: as luzes acendem e as máquinas começam a operar.

```bash
cd /opt/modoboa
docker compose up -d
docker compose ps
```

- **O que você verá na tela:** Docker fará pull das imagens e exibirá 'Container modoboa-web Started', 'Container modoboa-postgres Started', 'Container modoboa-redis Started'.
- **Como saber se deu certo:** Digite 'docker compose ps' e veja todos os containers com status 'Up'.

### Passo 6: Configuração do SSL (Certificado de Segurança) com Certbot `[F05]`
Nginx + Certbot emitem automaticamente um certificado Let's Encrypt gratuito para que ninguém intercepte seus emails na internet.

> **Entenda com uma analogia:** Lacre inviolável dos Correios com assinatura digital em cada pacote.

```bash
apt-get install -y certbot python3-certbot-nginx
certbot certonly --nginx -d seu-dominio.com.br -d mail.seu-dominio.com.br
nginx -s reload
```

- **O que você verá na tela:** Certbot verificará seu domínio (deve estar apontando para o IP do servidor) e confirmará 'Congratulations! Your certificate is issued'.
- **Como saber se deu certo:** Abra https://seu-dominio no navegador e veja o cadeado verde fechado.

## Arquivos de Configuração de Produção

### `/opt/modoboa/docker-compose.yml`
*Orquestra PostgreSQL, Redis e Modoboa em perfeita harmonia via Docker.*

```yaml
version: '3.8'
services:
 postgres:
 image: postgres:15-alpine
 restart: unless-stopped
 environment:
 POSTGRES_DB: modoboa
 POSTGRES_USER: modoboa
 POSTGRES_PASSWORD: sua-senha-forte
 volumes:
 - ./postgres:/var/lib/postgresql/data
 redis:
 image: redis:7-alpine
 restart: unless-stopped
 volumes:
 - ./redis:/data
 modoboa:
 image: modoboa/modoboa:latest
 restart: unless-stopped
 depends_on:
 - postgres
 - redis
 environment:
 DATABASE_URL: postgresql://modoboa:sua-senha-forte@postgres:5432/modoboa
 REDIS_URL: redis://redis:6379/0
 ports:
 - "25:25"
 - "587:587"
 volumes:
 - ./data:/data
```

## Parte II: Manual de Uso Exaustivo

**Arquitetura Operacional:** Modoboa oferece webmail seguro (HTTPS), sincronização de calendários via CalDAV, gerenciamento de contatos CardDAV e recebimento de emails via SMTP/IMAP/POP3 criptografado. Todos os dados residem na sua VPS.

### Roteiro de Primeiro Voo (Sua Primeira Reunião em 3 Minutos)

1. **Passo 1: Acessar painel administrativo:** Abra https://seu-dominio.com.br no navegador com credenciais admin.
 - **Resultado Esperado:** Dashboard administrativo carrega com estatísticas de usuários e emails.

1. **Passo 2: Adicionar domínio:** Clique 'Domains' > 'Add Domain', digite seu domínio e valide registros MX/SPF/DKIM.
 - **Resultado Esperado:** Domínio aparece ativo na lista.

### Dicionário Completo de Comandos (CLI)

| Comando / Flag | Descrição Técnica | Exemplo de Execução | Fonte |
| :--- | :--- | :--- | :---: |
| `docker compose ps` | Mostra status de todos os containers do Modoboa (web, postgres, redis, nginx). | `docker compose ps` | `[F01]` |
| `docker compose logs -f modoboa` | Exibe logs em tempo real do container web para diagnosticar problemas. | `docker compose logs -f modoboa | grep -i error` | `[F02]` |
| `docker compose exec postgres pg_dump -U modoboa modoboa` | Faz backup do banco de dados PostgreSQL com todos os emails, calendários e contatos. | `docker compose exec postgres pg_dump -U modoboa modoboa > backup.sql` | `[F03]` |
| `postqueue -p` | Mostra fila de emails aguardando entrega (usar via 'docker compose exec modoboa postqueue -p'). | `docker compose exec modoboa postqueue -p` | `[F01]` |

### Endpoints de API REST & Integração Agêntica

| Método | Rota | Descrição | Fonte |
| :---: | :--- | :--- | :---: |
| **GET** | `/admin/accounts/users/` | Lista todos os usuários de email cadastrados no sistema. | `[F01]` |
| **POST** | `/admin/accounts/users/` | Cria novo usuário de email via API (requer autenticação). | `[F02]` |
| **GET** | `/admin/domains/` | Lista todos os domínios configurados e seu status de validação DNS. | `[F03]` |

### Matriz de Resolução de Problemas (Troubleshooting)

- ** Sintoma:** Emails não são entregues
 - **Causa:** Registros DNS (MX) não estão apontando para o servidor ou fila Postfix travada.
- ** Sintoma:** Usuários não conseguem fazer login no webmail
 - **Causa:** PostgreSQL desligado ou password hash inválido no banco.
- ** Sintoma:** Certificado SSL expirou
 - **Causa:** Certbot não foi configurado para renovação automática.
## Parte III: Desinstalação Cirúrgica & Isolamento da VPS (Zero Efeito Colateral)

> **Princípio de Isolamento:** Remove exclusivamente containers Modoboa preservando Docker daemon e outros serviços.

### Passo 1: Parada dos Containers
Interrompe todos os processos do Modoboa.

```bash
cd /opt/modoboa && docker compose down
```

- **Alerta de Segurança:** Não execute 'docker system prune -a'.
- **Como Validar:** `docker ps | grep modoboa # Deve estar vazio`

### Passo 2: Remoção de Volumes
Remove dados de email (IRREVERSÍVEL - fazer backup antes).

```bash
docker compose down -v && docker volume rm modoboa_postgres modoboa_redis 2>/dev/null || true
```

- **Alerta de Segurança:** BACKUP ANTES: docker compose exec postgres pg_dump -U modoboa modoboa > backup.sql
- **Como Validar:** `docker volume ls | grep modoboa # Não deve constar`

### Passo 3: Revogação de Portas no Firewall
Fecha portas de email (25, 110, 143, etc).

```bash
for port in 25 110 143 465 587 993 995; do ufw delete allow $port/tcp 2>/dev/null; done
ufw reload
```

- **Alerta de Segurança:** Mantém SSH e web abertos.
- **Como Validar:** `ufw status # Verifique ausência de portas de email`

### Checklist de Saúde da VPS (Outros Projetos)

- [ ] `docker ps # Outros containers continuam 'Up'`
- [ ] `free -h # Memória liberada (PostgreSQL+Redis liberam 4-6 GB)`
- [ ] `df -h # Disco liberado (emails liberam espaço significativo)`

## Parte IV: Referências Bibliográficas Auditadas

| ID | Categoria | Título da Obra | Autor / Mantenedor | Link Oficial |
| :---: | :--- | :--- | :--- | :--- |
| **F01** | Documentação Oficial | Modoboa Official Documentation | Modoboa Core Team | [https://modoboa.readthedocs.io/](https://modoboa.readthedocs.io/) |
