# Manual Operacional Completo: Modoboa

> **Padrão Diamante · Guia de Engenharia & Adoção Descomplicada** 
> **Licença:** ISC | **Versão:** 2.3.0 | **Setup Estimado:** 25 a 35 minutos 
> **VPS Recomendada:** Hetzner Cloud CPX31 (ou UpCloud 4GB) (4 vCPU Dedicadas, 4 GB RAM (mínimo 3GB; 4GB+ para ClamAV), 40 GB SSD NVMe, Debian 12 / Ubuntu 22.04 LTS) 
> **Custo Mensal Estimado:** EUR 14,00 a EUR 16,00/mês (~R$ 84 a R$ 96)

---

## Módulo 0: Nivelamento Conceitual (Analogias do Dia a Dia)

### Modoboa *(Analogia: Departamento Correios Inteligente)*
Gerenciador central de emails. Recebe (Postfix), guarda (Dovecot), controla (Django).

### Postfix *(Analogia: Entregador Cartas)*
Carteiro que sai pela porta com cartas endereçadas (porta 25 SMTP).

### Dovecot *(Analogia: Gerente Gavetas Correspondência)*
Coloca carta certa com nome funcionário (portas 143 IMAP ou 110 POP3).

### Django/Python *(Analogia: Painel Controle Centralizado)*
Painel web onde admin clica criar usuários, domínios.

### PostgreSQL *(Analogia: Arquivo Central Documentos)*
Banco dados: usuários, domínios, permissões, filtros, histórico.

## Parte I: Instalação em Produção na VPS (Passo a Passo Rígido)

### Passo 1: Provisionar VPS e SSH `[F01]`
Hetzner Cloud, Debian 12, CPX31

> **Entenda com uma analogia:** Alugar prédio

```bash
ssh root@SEU_IP_AQUI
```

- **O que você verá na tela:** Terminal abre
- **Como saber se deu certo:** Prompt root@mail

### Passo 2: Atualizar Sistema `[F02]`
Updates Debian + ferramentas essenciais

> **Entenda com uma analogia:** Limpar prédio

```bash
apt-get update && apt-get upgrade -y
apt-get install -y curl wget git build-essential python3-dev python3-pip postgresql postfix dovecot-core dovecot-imapd dovecot-pop3d nginx
```

- **O que você verá na tela:** Progresso verde 2-3min
- **Como saber se deu certo:** python3 3.11+

### Passo 3: Clonar Repositório Modoboa `[F01]`
Download código-fonte do GitHub

> **Entenda com uma analogia:** Trazer plantas construção

```bash
cd /opt && git clone https://github.com/modoboa/modoboa.git
cd modoboa && git checkout v2.3.0
```

- **O que você verá na tela:** Git exibe Cloning into
- **Como saber se deu certo:** /opt/modoboa existe

### Passo 4: Instalador Automático `[F03]`
Configura PostgreSQL, Postfix, Dovecot, Nginx, Django

> **Entenda com uma analogia:** Apertar botão construir

```bash
cd /opt/modoboa
python3 -m pip install -U pip setuptools wheel
python3 -m pip install -e .
modoboa deploy /var/vmail/modoboa
```

- **O que você verá na tela:** Perguntas hostname/domínio/senha
- **Como saber se deu certo:** Installation complete!

### Passo 5: Configurar Firewall UFW `[F05]`
Liberar portas 22,25,80,143,110,587,443

> **Entenda com uma analogia:** Guarita porteiro

```bash
ufw default deny incoming && ufw default allow outgoing
ufw allow 22/tcp && ufw allow 25/tcp && ufw allow 80/tcp && ufw allow 143/tcp && ufw allow 110/tcp && ufw allow 587/tcp && ufw allow 443/tcp
ufw --force enable
```

- **O que você verá na tela:** Rule added para cada porta
- **Como saber se deu certo:** ufw status OK

### Passo 6: Ativar HTTPS Let's Encrypt `[F04]`
Certificado SSL/TLS que renova automaticamente

> **Entenda com uma analogia:** Lacre segurança

```bash
apt-get install -y certbot python3-certbot-nginx
certbot certonly --nginx -d seu-dominio.com
sudo systemctl restart nginx
```

- **O que você verá na tela:** Received certificate em 30s
- **Como saber se deu certo:** Cadeado verde https://seu-ip

## Arquivos de Configuração de Produção

### `/etc/postfix/main.cf`
*Integração Postfix com PostgreSQL*

```conf
myhostname = mail.seu-dominio.com
mydomain = seu-dominio.com
virtual_mailbox_base = /var/vmail
virtual_uid_maps = static:901
```

### `/etc/dovecot/conf.d/10-mail.conf`
*Armazenamento maildir IMAP/POP3*

```conf
mail_location = maildir:~/.maildir:LAYOUT=fs
protocols = imap pop3
listen = *, ::
```

### `/etc/nginx/sites-available/modoboa`
*Proxy reverso Nginx para Django*

```nginx
upstream modoboa { server 127.0.0.1:8000; }
server { listen 80; server_name admin.seu-dominio.com; location / { proxy_pass http://modoboa; } }
```

## Parte II: Manual de Uso Exaustivo

**Arquitetura Operacional:** Postfix(SMTP:25) recebe emails externos, Dovecot(IMAP:143/POP3:110) permite acesso local aos mailboxes, Django(web:443) oferece painel admin, PostgreSQL armazena metadados. Nenhum dado sai do servidor.

### Roteiro de Primeiro Voo (Sua Primeira Reunião em 3 Minutos)

1. **Passo 1: Admin:** Abra https://admin.seu-dominio.com com usuario admin
 - **Resultado Esperado:** Dashboard com estatísticas

1. **Passo 2: Domínio:** Menu Domínios → +, digite empresa.com.br
 - **Resultado Esperado:** Domínio criado e ativo

1. **Passo 3: Email:** Domínio → Contas → +, username joao, quota 2GB
 - **Resultado Esperado:** joao@empresa.com.br criado

1. **Passo 4: Webmail:** https://mail.seu-dominio.com/webmail/ com joao@empresa.com.br
 - **Resultado Esperado:** Bandeja entrada com calendário

1. **Passo 5: Cliente:** Configure Outlook/Thunderbird IMAP mail.seu-dominio.com:143 TLS, SMTP :587
 - **Resultado Esperado:** Email chega em segundos

### Dicionário Completo de Comandos (CLI)

| Comando / Flag | Descrição Técnica | Exemplo de Execução | Fonte |
| :--- | :--- | :--- | :---: |
| `modoboa deploy /var/vmail/modoboa` | Inicializa instância de produção | `modoboa deploy /var/vmail/modoboa` | `[F01]` |
| `modoboa migrate` | Aplica migrações do banco de dados | `modoboa migrate` | `[F02]` |
| `postqueue -p` | Mostra emails na fila do Postfix | `postqueue -p` | `[F03]` |
| `postfix status` | Verifica saúde do Postfix | `postfix status` | `[F04]` |
| `systemctl restart dovecot` | Reinicia serviço Dovecot | `sudo systemctl restart dovecot` | `[F05]` |
| `modoboa manage createsuperuser` | Cria admin via linha de comando | `modoboa manage createsuperuser` | `[F01]` |

### Endpoints de API REST & Integração Agêntica

| Método | Rota | Descrição | Fonte |
| :---: | :--- | :--- | :---: |
| **GET** | `/api/v1/domains/` | Lista todos domínios | `[F01]` |
| **POST** | `/api/v1/domains/` | Criar novo domínio | `[F02]` |
| **GET** | `/api/v1/statistics/` | Estatísticas do servidor | `[F03]` |
| **GET** | `/api/v1/domains/{id}/accounts/` | Lista contas de um domínio | `[F04]` |

### Matriz de Resolução de Problemas (Troubleshooting)

- ** Sintoma:** Emails chegam em spam
 - **Causa:** SPF, DKIM ou DMARC não configurados
- ** Sintoma:** Port 25 blocked - emails não saem
 - **Causa:** ISP bloqueou porta 25 (comum em residencial)
- ** Sintoma:** IMAP não conecta com erro
 - **Causa:** Dovecot não está rodando ou permissões /var/vmail erradas
- ** Sintoma:** Painel web fica lento ou travado
 - **Causa:** PostgreSQL sob pressão ou muitos usuários simultâneos
- ** Sintoma:** ClamAV/SpamAssassin consumindo 100% CPU
 - **Causa:** Muitos emails grandes sendo processados simultaneamente
## Parte III: Desinstalação Cirúrgica & Isolamento da VPS (Zero Efeito Colateral)

> **Princípio de Isolamento:** Remove exclusivamente instância Modoboa (Django, dados email, bancos SQL). Preserva Postfix, Dovecot, certificados SSL e SO.

### Passo 1: Parada de Serviços Modoboa
Para Django (Gunicorn) e Celery sem afetar Postfix/Dovecot/Nginx

```bash
sudo systemctl stop modoboa
sudo systemctl disable modoboa
sudo systemctl stop modoboa-celery
sudo systemctl disable modoboa-celery
```

- **Alerta de Segurança:** NÃO execute 'systemctl stop postfix' ou 'systemctl stop dovecot'
- **Como Validar:** `sudo systemctl is-active modoboa # Retorna 'inactive'`

### Passo 2: Remoção do Banco PostgreSQL
Deleta schema Modoboa, preservando outros bancos

```bash
sudo -u postgres psql -c "DROP DATABASE IF EXISTS modoboa;"
sudo -u postgres psql -c "DROP USER IF EXISTS modoboa;"
```

- **Alerta de Segurança:** JAMAIS execute 'DROP DATABASE postgres;'
- **Como Validar:** `sudo -u postgres psql -l | grep modoboa # Não deve aparecer`

### Passo 3: Remoção de Diretórios
Remove /var/vmail/modoboa (dados) e /opt/modoboa (código)

```bash
sudo rm -rf /var/vmail/modoboa
sudo rm -rf /opt/modoboa
sudo rm -f /etc/systemd/system/modoboa.service
sudo rm -f /etc/systemd/system/modoboa-celery.service
```

- **Alerta de Segurança:** Não execute 'rm -rf /' nem 'rm -rf /var/'
- **Como Validar:** `ls -ld /var/vmail/modoboa 2>&1 | grep 'cannot access'`

### Passo 4: Limpeza Nginx
Remove virtual host Modoboa do Nginx

```bash
sudo rm -f /etc/nginx/sites-enabled/modoboa
sudo rm -f /etc/nginx/sites-available/modoboa
sudo systemctl reload nginx
sudo systemctl daemon-reload
```

- **Alerta de Segurança:** Mantenha outros sites em /etc/nginx/sites-available/
- **Como Validar:** `sudo nginx -t # Retorna 'configuration OK'`

### Checklist de Saúde da VPS (Outros Projetos)

- [ ] `ps aux | grep -E '(gunicorn|celery|modoboa)' # Nenhum processo deve aparecer`
- [ ] `sudo -u postgres psql -l # Banco 'modoboa' não deve estar na lista`
- [ ] `sudo systemctl status postfix # Deve estar 'active'`
- [ ] `sudo systemctl status dovecot # Deve estar 'active'`
- [ ] `sudo systemctl status nginx # Deve estar 'active'`
- [ ] `free -h # RAM devolvida ao sistema`

## Parte IV: Referências Bibliográficas Auditadas

| ID | Categoria | Título da Obra | Autor / Mantenedor | Link Oficial |
| :---: | :--- | :--- | :--- | :--- |
| **F01** | Documentação Oficial | Modoboa Official Documentation - ReadTheDocs | Modoboa Project Team | [https://modoboa.readthedocs.io](https://modoboa.readthedocs.io) |
| **F02** | Repositório Oficial | Modoboa GitHub Repository - Source Code | Modoboa Open Source Developers | [https://github.com/modoboa/modoboa](https://github.com/modoboa/modoboa) |
| **F03** | Tutorial Prático | How To Set Up Secure Private Email Server With Modoboa - UpCloud | UpCloud Documentation Team | [https://upcloud.com/resources/tutorials/install-secure-private-email-server-modoboa/](https://upcloud.com/resources/tutorials/install-secure-private-email-server-modoboa/) |
| **F04** | Guia de Setup | How to Quickly Set Up a Mail Server on Ubuntu 20.04 with Modoboa | LinuxBabe | [https://www.linuxbabe.com/mail-server/modoboa-email-server-ubuntu-20-04](https://www.linuxbabe.com/mail-server/modoboa-email-server-ubuntu-20-04) |
| **F05** | Documentação Técnica | Modoboa API Documentation & REST Endpoints | Modoboa Core Contributors | [https://modoboa.readthedocs.io/en/latest/integration/api.html](https://modoboa.readthedocs.io/en/latest/integration/api.html) |
| **F06** | Discussão Comunitária | Minimum Resources on VPS for Install Modoboa - GitHub Discussion | Modoboa Community & Maintainers | [https://github.com/modoboa/modoboa/discussions/2139](https://github.com/modoboa/modoboa/discussions/2139) |
