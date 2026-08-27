# Manual Operacional Completo: Mailcow

> **Padrão Diamante · Guia de Engenharia & Adoção Descomplicada**  
> **Licença:** GPL-3.0 | **Versão:** 2024.11 | **Setup Estimado:** 30 a 45 minutos (Conhecimento intermediário de DNS e email)  
> **VPS Recomendada:** Hetzner Cloud CPX21 (ou Contabo Cloud VPS M) (2 vCPU Dedicadas (AMD EPYC), 4 GB RAM ECC (mínimo 2 GB, 4 GB recomendado para até 50 usuários), 80 GB NVMe Gen4 (mínimo 40 GB, crescer conforme demanda de emails), Ubuntu 24.04 LTS (x86_64) ou Debian 12)  
> **Custo Mensal Estimado:** EUR 9,00/mês (~R$ 54,00/mês na cotação média) ou mais conforme capacidade

---

## Módulo 0: Nivelamento Conceitual (Analogias do Dia a Dia)

### 💡 Mailcow (A Ferramenta) *(Analogia: A Agência de Correios Privada da Sua Empresa)*
Assim como uma agência de correios recebe cartas, as classifica e entrega aos destinatários, o Mailcow é um servidor de email completo que gerencia contas de email da sua empresa com segurança, backup automático e interface web amigável. Você é o dono absoluto do seu correio.

### 💡 VPS (Servidor Privado Virtual) *(Analogia: Uma Sala Comercial Alugada que Nunca Apaga a Luz)*
Em vez de deixar um servidor de email ligado no escritório esquentando na sala, você aluga por cerca de R$ 80 a R$ 150 por mês um computador profissional em um data center na nuvem (como Hetzner ou Contabo). Ele fica ligado o tempo todo com internet de altíssima velocidade.

### 💡 MX Record (Registro de Correio) *(Analogia: O Endereço de Retorno no Envelope)*
Quando você envia uma carta pelo correio, o envelope tem o seu endereço para retorno de não-entregáveis. O MX Record funciona assim: ele avisa ao internet que qualquer email dirigido a 'seu-dominio.com.br' deve ser entregue ao seu servidor Mailcow, não a terceiros.

### 💡 DKIM & SPF (Assinatura Digital do Email) *(Analogia: A Identificação da Empresa Gravada na Carta)*
Uma carta autêntica tem o carimbo da empresa. DKIM e SPF são carimbos digitais que provam ao servidor de email destino que o email veio realmente de você e não de um impostor tentando se passar.

### 💡 Docker & Containers *(Analogia: Uma Caixa de Ferramentas Lacrada de Fábrica)*
Antigamente, instalar Mailcow exigia configurar manualmente postfix, dovecot, mysql e dezenas de ferramentas. Hoje, o Mailcow vem em um container Docker: tudo já vem pronto e integrado dentro de uma caixa lacrada.

## Parte I: Instalação em Produção na VPS (Passo a Passo Rígido)

### Passo 1: Compra da VPS e Apontamento do Domínio `[F01]`
Alugue um servidor VPS em Hetzner Cloud ou Contabo. Configure os nameservers do seu domínio (em seu registrador, ex: Registro.br ou Godaddy) para apontar para os nameservers do provedor. Aguarde propagação DNS (até 48 horas).

> 💡 **Entenda com uma analogia:** Alugar a sala comercial, receber as chaves e avisar aos Correios para entregar cartas naquele novo endereço.

```bash
# No seu computador, após alugar a VPS:
nslookup seu-dominio.com.br
```

- 🖥️ **O que você verá na tela:** Na Hetzner, você verá um painel com o IP do servidor. No seu registrador de domínio, você alterará os nameservers.
- ✅ **Como saber se deu certo:** Execute 'nslookup seu-dominio.com.br' e veja o IP apontando para o servidor.

### Passo 2: Conectar ao Servidor via SSH e Atualizar Pacotes `[F01]`
Abra o terminal (PowerShell no Windows, Terminal no Mac/Linux) e conecte-se ao servidor via SSH. Atualize todos os pacotes do sistema operacional.

> 💡 **Entenda com uma analogia:** Abrir a porta da sala comercial com a chave e verificar se tudo está funcionando.

```bash
ssh root@SEU_IP
apt-get update && apt-get upgrade -y
```

- 🖥️ **O que você verá na tela:** Será solicitada a senha root (ou chave SSH se configurado). A tela mostrará a atualização de pacotes por alguns minutos.
- ✅ **Como saber se deu certo:** A resposta do comando 'uname -a' mostrará 'Linux' com data recente.

### Passo 3: Clonar o Repositório Oficial do Mailcow `[F02]`
Clone o repositório oficial do Mailcow da comunidade Mailcow-Dockerized no GitHub. Este repositório contém todo o código, configurações e docker-compose necessários.

> 💡 **Entenda com uma analogia:** Baixar o guia completo de como organizar a agência de correios.

```bash
cd /opt
git clone https://github.com/mailcow/mailcow-dockerized.git
cd mailcow-dockerized
```

- 🖥️ **O que você verá na tela:** Git clonar o repositório para /opt/mailcow-dockerized durante 30 a 60 segundos.
- ✅ **Como saber se deu certo:** Execute 'ls -la /opt/mailcow-dockerized/' e veja a pasta 'docker-compose.yml' e outras pastas.

### Passo 4: Gerar Configuração Interativa e Certificado SSL Inicial `[F02]`
Execute o script de geração interativa do Mailcow que perguntará seu domínio, email de admin e outros dados. O script gerará o arquivo mailcow.conf e criará um certificado SSL inicial com Let's Encrypt.

> 💡 **Entenda com uma analogia:** Preencher o formulário de registro da agência de correios com seus dados.

```bash
bash generate_config.sh
ls -la data/assets/ssl/
```

- 🖥️ **O que você verá na tela:** O script perguntará em sequência: 'Hostname FQDN?', 'Timezone?', 'Full name of Organization?'. Depois criará os certificados SSL automaticamente.
- ✅ **Como saber se deu certo:** Arquivo mailcow.conf criado em /opt/mailcow-dockerized/ e certificados em /opt/mailcow-dockerized/data/assets/ssl/

### Passo 5: Iniciar os Containers Docker (Mailcow) `[F02]`
Execute 'docker compose up -d' para iniciar todos os 15+ containers do Mailcow em segundo plano. O Mailcow baixará as imagens oficiais e iniciará o servidor de email.

> 💡 **Entenda com uma analogia:** Ligar o painel elétrico: as luzes acendem, as máquinas operam, o correio começa a funcionar.

```bash
docker compose up -d
sleep 30
docker compose ps
```

- 🖥️ **O que você verá na tela:** Será exibido 'Pulling' de múltiplas imagens, depois 'Creating', 'Starting' de cada container. Ao final, 'docker compose ps' mostrará 15+ containers em status 'Up'.
- ✅ **Como saber se deu certo:** Execute 'docker compose ps' e veja containers como 'mailcow-dovecot', 'mailcow-postfix', 'mailcow-nginx' com status 'Up'.

### Passo 6: Acessar a Interface Web e Criar Primeira Conta de Email `[F01]`
Abra o navegador e acesse https://seu-dominio.com:8443 (ou https://seu-dominio.com dependendo de configuração). Faça login com o email de administrador criado. Crie a primeira conta de usuário.

> 💡 **Entenda com uma analogia:** Entrar na sala da agência, abrir o sistema de cadastro e criar o primeiro carteiro.

```bash
# Apenas via interface web:
# Acesse https://seu-dominio.com:8443
# Login com usuario@seu-dominio.com
# Crie novo usuário em: Mail > Mailboxes > New Mailbox
```

- 🖥️ **O que você verá na tela:** O navegador mostrará um painel de controle com abas 'Mail', 'Mailboxes', 'Domains', 'DNS' e 'Monitoring'.
- ✅ **Como saber se deu certo:** Você consegue fazer login, a aba 'Mail' permite criar usuários novos e visualizar caixas de email.

### Passo 7: Configurar Registros MX, SPF, DKIM e TLSA no Seu Domínio `[F05]`
No painel Mailcow, clique em 'DNS' para copiar os registros MX, SPF, DKIM e TLSA. Insira esses registros no seu registrador de domínio (Registro.br, GoDaddy, etc). Aguarde propagação (até 48 horas).

> 💡 **Entenda com uma analogia:** Avisar aos Correios que qualquer carta dirigida ao seu domínio deve chegar ao seu servidor e não a terceiros.

```bash
# Verificar MX:
dig seu-dominio.com.br MX
# Verificar SPF:
dig seu-dominio.com.br TXT | grep spf
```

- 🖥️ **O que você verá na tela:** Na interface Mailcow, verá caixas com os registros DNS. No registrador de domínio, verá abas 'DNS', 'Registros MX', 'Registros TXT'.
- ✅ **Como saber se deu certo:** Execute 'dig seu-dominio.com.br MX' e veja seu servidor listado como preferência 10.

### Passo 8: Teste de Envio e Recebimento de Emails `[F05]`
Use um cliente de email (Thunderbird, Outlook, Evolution) ou webmail (acessar https://seu-dominio.com/mail) para enviar e receber emails. Teste envios para domínios externos (Gmail, Yahoo, Hotmail) para validar SPF/DKIM/TLSA.

> 💡 **Entenda com uma analogia:** Enviar e receber a primeira carta pela agência para confirmar que tudo está funcionando.

```bash
# Teste via telnet (básico):
telnet seu-dominio.com.br 25
HELO test
MAIL FROM: <usuario@seu-dominio.com.br>
```

- 🖥️ **O que você verá na tela:** No cliente de email, você configurará IMAP (porta 993) e SMTP (porta 587 ou 465) com seu usuário. Emails chegarão normalmente.
- ✅ **Como saber se deu certo:** Você recebe emails de terceiros sem cair em spam. O Gmail mostra cadeado de autenticação SPF/DKIM ao receber.

## Arquivos de Configuração de Produção

### `/opt/mailcow-dockerized/mailcow.conf`
*Arquivo de configuração do Mailcow. Gerado interativamente, contém hostname do servidor, timezone, senhas de BD e configurações de segurança.*

```bash
# Configuração gerada automaticamente por generate_config.sh
MAILCOW_HOSTNAME=mail.seu-dominio.com.br
TIMEZONE=America/Sao_Paulo
MARIADB_ROOT_PASSWORD=SenhaForteAqui123!
MARIADB_LOG_BIN_CHARSET=utf8mb4
COMPOSE_PROJECT_NAME=mailcow
FETCH_CERT=y
SIEM_ENABLED=y
SIEM_IP=172.22.1.250
```

### `/opt/mailcow-dockerized/docker-compose.yml`
*Docker Compose que orquestra 15+ containers de email, banco de dados, nginx, redis, etc. Não editar manualmente; usar generate_config.sh para regenerar.*

```yaml
# Arquivo auto-gerado. Não editar manualmente sem backup.
version: '3.7'
services:
  dovecot-mailcow:
    image: ${MAILCOW_DOCKER_REGISTRY:-mailcow}/dovecot:${MAILCOW_TAG:-latest}
    container_name: mailcow-dovecot
    restart: always
    environment:
      - TIMEZONE=${TIMEZONE}
    volumes:
      - vmail-vol-1:/var/vmail
    networks:
      - mailcow-network

  postfix-mailcow:
    image: ${MAILCOW_DOCKER_REGISTRY:-mailcow}/postfix:${MAILCOW_TAG:-latest}
    container_name: mailcow-postfix
    restart: always
    environment:
      - TIMEZONE=${TIMEZONE}
    volumes:
      - mails-vol-1:/var/spool/postfix
    networks:
      - mailcow-network

  mariadb-mailcow:
    image: ${MAILCOW_DOCKER_REGISTRY:-mailcow}/mariadb:${MAILCOW_TAG:-latest}
    container_name: mailcow-db
    restart: always
    environment:
      - MYSQL_ROOT_PASSWORD=${MARIADB_ROOT_PASSWORD}
      - TIMEZONE=${TIMEZONE}
    volumes:
      - mysql-vol-1:/var/lib/mysql
    networks:
      - mailcow-network

volumes:
  vmail-vol-1:
  mysql-vol-1:
  mails-vol-1:

networks:
  mailcow-network:
    driver: bridge
    ipam:
      config:
        - subnet: 172.22.0.0/16
```

### `/opt/mailcow-dockerized/data/conf/postfix/main.cf (trecho)`
*Configuração crítica do Postfix dentro do container. Define hostname, TLS obrigatório e criptografia forte. Editada via painel ou via volumes no docker-compose.*

```properties
# Configurações críticas de SMTP
myhostname = mail.seu-dominio.com.br
myorigin = seu-dominio.com.br
mynetworks = 127.0.0.1 172.22.0.0/16
smtpd_tls_cert_file = /etc/ssl/certs/mailcow.pem
smtpd_tls_key_file = /etc/ssl/private/mailcow.key
smtpd_use_tls = yes
smtpd_tls_mandatory_protocols = !SSLv2, !SSLv3, !TLSv1
smtpd_tls_ciphers = medium
policy_time_limit = 3600
```

## Parte II: Manual de Uso Exaustivo

**Arquitetura Operacional:** Mailcow funciona em camadas isoladas: Dovecot (IMAP/POP3) para leitura de emails, Postfix (SMTP) para envio, MariaDB para armazenar dados de usuários, e Nginx para interface web. Todos comunicam via rede interna do Docker. Nenhum email sai da sua rede privada sem sua aprovação.

### Roteiro de Primeiro Voo (Sua Primeira Reunião em 3 Minutos)

1. **Passo 1: Acessar o Painel Mailcow:** Abra o navegador e acesse https://seu-dominio.com:8443 ou https://seu-dominio.com/admin (conforme config). Faça login com seu email administrativo.
   - 🎯 **Resultado Esperado:** Aparece o painel de controle com abas Mail, Mailboxes, Domains, DNS, Monitoring e Settings.

1. **Passo 2: Criar a Primeira Caixa de Email:** Clique em 'Mail' > 'Mailboxes'. Clique no botão verde 'New Mailbox'. Preencha nome, email e senha. Clique 'Add'.
   - 🎯 **Resultado Esperado:** A caixa de email aparece na lista. Você pode agora acessá-la via Thunderbird ou webmail.

1. **Passo 3: Configurar Cliente de Email (Thunderbird):** Abra Thunderbird, clique em 'Add Account'. Preencha email e senha. O Thunderbird detectará automaticamente IMAP/SMTP. Clique 'Done'.
   - 🎯 **Resultado Esperado:** Thunderbird sincroniza a pasta INBOX e você pode enviar/receber emails normalmente.

### Dicionário Completo de Comandos (CLI)

| Comando / Flag | Descrição Técnica | Exemplo de Execução | Fonte |
| :--- | :--- | :--- | :---: |
| `docker compose ps` | Mostra o status de todos os 15+ containers do Mailcow. | `docker compose ps # Vê se dovecot, postfix, mariadb estão 'Up'` | `[F01]` |
| `docker compose logs -f postfix-mailcow` | Mostra os logs em tempo real do Postfix para debug de problemas de envio. | `docker compose logs -f postfix-mailcow | grep rejected` | `[F05]` |
| `docker compose exec mariadb-mailcow mysql -u root -p` | Acessa o banco de dados MariaDB para queries manuais de usuários/domínios. | `docker compose exec mariadb-mailcow mysql -u root -p mailcow` | `[F02]` |
| `mailcow-cli reload` | Recarrega configurações do Mailcow sem derrubar containers. | `cd /opt/mailcow-dockerized && docker compose exec mailcow-cli reload` | `[F01]` |

### Endpoints de API REST & Integração Agêntica

| Método | Rota | Descrição | Fonte |
| :---: | :--- | :--- | :---: |
| **GET** | `/api/v1/get/status/mailcow` | Retorna o status geral do servidor de email (online, cpu, memória). | `[F04]` |
| **POST** | `/api/v1/add/mailbox` | Cria uma nova caixa de email programaticamente. | `[F04]` |

### Matriz de Resolução de Problemas (Troubleshooting)

- **⚠️ Sintoma:** Emails sendo rejeitados por SPF/DKIM fail
  - **Causa:** Os registros DNS (SPF, DKIM) não foram inseridos no registrador de domínio ou ainda não se propagaram.
- **⚠️ Sintoma:** Dovecot offline ou IMAP não conecta
  - **Causa:** Container Dovecot caiu ou certificado SSL expirou.
- **⚠️ Sintoma:** Espaço em disco cheio
  - **Causa:** Emails antigos acumulando no servidor ou logs crescendo indefinidamente.
## Parte III: Desinstalação Cirúrgica & Isolamento da VPS (Zero Efeito Colateral)

> 🛡️ **Princípio de Isolamento:** A desinstalação remove exclusivamente os containers, volumes e dados do Mailcow, preservando intactos o Docker, Nginx reverso, PostgreSQL e outros projetos hospedados na VPS.

### Passo 1: Backup de Emails Antes da Desinstalação
Faça um dump completo da pasta vmail e banco de dados MariaDB para ter cópia segura antes de remover.

```bash
cd /opt/mailcow-dockerized
docker compose exec mariadb-mailcow mysqldump -u root -p --all-databases > mailcow_backup.sql
tar -czf mailcow_vmail_backup.tar.gz data/vmail/
```

- ⚠️ **Alerta de Segurança:** NÃO DELETE ESTES ARQUIVOS. Guarde em local seguro ou em outro servidor.
- ✅ **Como Validar:** `ls -lh mailcow_backup.sql mailcow_vmail_backup.tar.gz`

### Passo 2: Parada e Desativação dos Containers
Para todos os containers do Mailcow sem afetar outros serviços da VPS.

```bash
cd /opt/mailcow-dockerized
docker compose down
docker ps | grep mailcow # Confirma que nenhum container está ativo
```

- ⚠️ **Alerta de Segurança:** Use 'down' nunca 'down -v' (o -v removeria volumes). Dados ainda existem.
- ✅ **Como Validar:** `docker ps | grep mailcow`

### Passo 3: Limpeza de Volumes de Dados (Opcional)
Remove os volumes Docker exclusivos do Mailcow (vmail, mysql, etc). ATENÇÂO: irreversível após este passo.

```bash
docker volume rm mailcow-dockerized_vmail-vol-1
docker volume rm mailcow-dockerized_mysql-vol-1
docker volume rm mailcow-dockerized_mails-vol-1
docker volume ls | grep mailcow # Confirma remoção
```

- ⚠️ **Alerta de Segurança:** Após remover volumes, dados são definitivamente apagados. Confirme que backup foi feito.
- ✅ **Como Validar:** `docker volume ls | grep mailcow`

### Passo 4: Desativação de Firewall & Portas de Email
Revoga permissões de firewall para portas SMTP (25, 587, 465) e IMAP (143, 993).

```bash
sudo ufw delete allow 25/tcp
sudo ufw delete allow 110/tcp
sudo ufw delete allow 143/tcp
sudo ufw delete allow 465/tcp
sudo ufw delete allow 587/tcp
sudo ufw delete allow 993/tcp
sudo ufw delete allow 995/tcp
sudo ufw reload
```

- ⚠️ **Alerta de Segurança:** Mantenha firewall ativo. Verifique com 'ufw status' antes e depois.
- ✅ **Como Validar:** `sudo ufw status`

### Passo 5: Remoção da Pasta Mailcow & Limpeza do Sistema
Remove o diretório /opt/mailcow-dockerized se não for mais necessário. Opcional: manter arquivo de backup.

```bash
sudo rm -rf /opt/mailcow-dockerized
df -h # Confirma liberação de espaço em disco
```

- ⚠️ **Alerta de Segurança:** Backup já foi feito no Passo 1. Se alterou de ideia, ainda há tempo. Após 'rm -rf', dados são irrecuperáveis.
- ✅ **Como Validar:** `ls -la /opt/mailcow-dockerized 2>&1 | grep 'cannot access'`

### Passo 6: Resetar Registros DNS para Email Antigo (Locaweb)
Se voltar a usar Locaweb Email, altere os registros MX do seu domínio para apontar aos servidores da Locaweb.

```bash
# No seu registrador de domínio, altere MX para:
# Priority 10 -> mail.locaweb.com.br
# (Consulte painel Locaweb para registros corretos)
```

- ⚠️ **Alerta de Segurança:** Propag ação DNS leva até 48 horas. Emails podem ficar presos em fila durante transição. Mantenha backup do Passo 1 acessível.
- ✅ **Como Validar:** `dig seu-dominio.com.br MX`

### Checklist de Saúde da VPS (Outros Projetos)

- [ ] `docker ps # Confirma ausência de containers mailcow`
- [ ] `netstat -tlnp | grep -E '(25|110|143|465|587|993|995)' # Confirma portas liberadas`
- [ ] `df -h # Confirma espaço em disco devolvido`
- [ ] `ufw status | grep -E '(25|143|587|993)' # Confirma remoção de regras firewall`

## Parte IV: Referências Bibliográficas Auditadas

| ID | Categoria | Título da Obra | Autor / Mantenedor | Link Oficial |
| :---: | :--- | :--- | :--- | :--- |
| **F01** | Documentação Oficial | Mailcow Official Documentation - Setup & Management | Mailcow Community | [https://docs.mailcow.email](https://docs.mailcow.email) |
| **F02** | Documentação Oficial | Mailcow GitHub Repository & Docker Compose | Mailcow Dockerized | [https://github.com/mailcow/mailcow-dockerized](https://github.com/mailcow/mailcow-dockerized) |
| **F03** | Livro / Guia Técnico | Email Configuration Best Practices: SPF, DKIM, DMARC | IETF Standards | [https://tools.ietf.org/html/rfc7208](https://tools.ietf.org/html/rfc7208) |
| **F04** | Vídeo / YouTube | Complete Mailcow Setup from Scratch - VPS Deployment | Various Linux/Server Channels | [https://www.youtube.com/results?search_query=mailcow+setup](https://www.youtube.com/results?search_query=mailcow+setup) |
| **F05** | Curso / Tutorial | Linux DNS Configuration & Email Server Security | Mailcow Documentation | [https://github.com/mailcow/mailcow-dockerized/tree/main/docs](https://github.com/mailcow/mailcow-dockerized/tree/main/docs) |
