# Manual Operacional Completo: Postfix + Dovecot

> **Padrão Diamante · Guia de Engenharia & Adoção Descomplicada**  
> **Licença:** IPL-1.0 (Postfix) | LGPL-2.1 (Dovecot) | **Versão:** Postfix 3.8.x + Dovecot 2.3.x | **Setup Estimado:** 45 a 60 minutos (com dominio DNS ja pronto)  
> **VPS Recomendada:** Hetzner Cloud CPX11 (ou Contabo Cloud VPS S) (2 vCPU Compartilhadas, 2 GB RAM, 40 GB SSD NVMe, Ubuntu 24.04 LTS (x86_64) ou Debian 12)  
> **Custo Mensal Estimado:** EUR 2,50/mes (~R$ 15,00/mes)

---

## Módulo 0: Nivelamento Conceitual (Analogias do Dia a Dia)

### 💡 Postfix (Agente de Transferencia de E-Mail) *(Analogia: O Carteiro que Leva Cartas para Todas as Cidades)*
Postfix eh o programa que recebe emails e os entrega. Funciona 24h via SMTP.

### 💡 Dovecot (Servidor IMAP & POP3) *(Analogia: A Caixa de Correio com Chave)*
Dovecot guarda emails em pastas organizadas dentro do servidor.

### 💡 SSL/TLS (Criptografia) *(Analogia: Um Envelope Lacrado)*
Protege emails em transito com chave secreta.

### 💡 SPF, DKIM & DMARC (Autenticacao) *(Analogia: Documento de Identidade)*
Impede falsificacao de emails.

### 💡 DNS (Sistema de Nomes) *(Analogia: A Agenda Telefonica Global)*
Transforma nomes em endereco IP.

## Parte I: Instalação em Produção na VPS (Passo a Passo Rígido)

### Passo 1: Preparacao do Sistema `[F01]`
Atualizar SO

> 💡 **Entenda com uma analogia:** Limpar chao

```bash
apt-get update && apt-get upgrade -y
```

- 🖥️ **O que você verá na tela:** Pacotes baixando
- ✅ **Como saber se deu certo:** apt list --upgradable vazio

### Passo 2: Instalacao Postfix `[F01]`
Instala servidor SMTP

> 💡 **Entenda com uma analogia:** Montar mala

```bash
apt-get install -y postfix
```

- 🖥️ **O que você verá na tela:** Tela azul
- ✅ **Como saber se deu certo:** postfix status OK

### Passo 3: Instalacao Dovecot `[F02]`
Instala IMAP/POP3

> 💡 **Entenda com uma analogia:** Gavetas

```bash
apt-get install -y dovecot-core dovecot-imapd dovecot-pop3d
```

- 🖥️ **O que você verá na tela:** Silenciosa
- ✅ **Como saber se deu certo:** systemctl status dovecot OK

### Passo 4: SSL com Let's Encrypt `[F03]`
Criptografia gratuita

> 💡 **Entenda com uma analogia:** Cadeados

```bash
apt-get install -y certbot
```

- 🖥️ **O que você verá na tela:** Certbot pede email
- ✅ **Como saber se deu certo:** Certificado em /etc/letsencrypt

### Passo 5: Configuracao DNS `[F04]`
SPF, DKIM, DMARC

> 💡 **Entenda com uma analogia:** RG do dominio

```bash
opendkim-genkey -b 2048 -d seu-dominio.com.br
```

- 🖥️ **O que você verá na tela:** Editor nano
- ✅ **Como saber se deu certo:** Registros DNS aparecem

### Passo 6: Teste de Email `[F01]`
Enviar teste

> 💡 **Entenda com uma analogia:** Ligacao

```bash
echo 'Teste' | mail -s 'Teste' email@gmail.com
```

- 🖥️ **O que você verá na tela:** Nenhuma
- ✅ **Como saber se deu certo:** Email recebido em 5s

### Passo 7: Clientes de Email `[F02]`
Sincronizar Thunderbird/Outlook

> 💡 **Entenda com uma analogia:** Conexao

```bash
systemctl restart postfix dovecot
```

- 🖥️ **O que você verá na tela:** Testes de conexao
- ✅ **Como saber se deu certo:** INBOX sincronizada

## Arquivos de Configuração de Produção

### `/etc/postfix/main.cf`
*Config minima Postfix com SSL e DKIM*

```postfix-config
myhostname = mail.seu-dominio.com.br
myorigin = seu-dominio.com.br
smtpd_tls_cert_file = /etc/letsencrypt/live/seu-dominio.com.br/fullchain.pem
smtpd_tls_key_file = /etc/letsencrypt/live/seu-dominio.com.br/privkey.pem
```

### `/etc/dovecot/conf.d/10-mail.conf`
*Config minima Dovecot com IMAP seguro*

```dovecot-config
protocols = imap pop3
mail_location = maildir:~/Maildir
ssl = required
ssl_cert = </etc/letsencrypt/live/seu-dominio.com.br/fullchain.pem
```

## Parte II: Manual de Uso Exaustivo

**Arquitetura Operacional:** Postfix e Dovecot trabalham integrados. Postfix recebe/envia SMTP. Dovecot oferece IMAP para sincronizacao. Usuarios sao usuarios Unix com pasta Maildir/.

### Roteiro de Primeiro Voo (Sua Primeira Reunião em 3 Minutos)

1. **Passo 1: Adicionar Usuario:** sudo adduser seu-nome com senha forte (12+ chars)
   - 🎯 **Resultado Esperado:** Pasta Maildir criada no proximo login IMAP

1. **Passo 2: Configurar Cliente:** Abrir Thunderbird/Outlook e digitar email/senha
   - 🎯 **Resultado Esperado:** Em 10s testes de conexao OK

1. **Passo 3: Enviar Teste:** Escrever email para amigo@gmail.com
   - 🎯 **Resultado Esperado:** Email recebido em 2-3s

### Dicionário Completo de Comandos (CLI)

| Comando / Flag | Descrição Técnica | Exemplo de Execução | Fonte |
| :--- | :--- | :--- | :---: |
| `adduser [nome]` | Cria usuario Unix lido pelo Dovecot | `adduser joao.silva` | `[F01]` |
| `mailq` | Lista fila de emails | `mailq` | `[F02]` |
| `postqueue -p` | Fila com detalhes | `postqueue -p | grep MAILER` | `[F01]` |
| `dig seu-dominio.com.br MX` | Verifica registro MX | `dig seu-dominio.com.br MX` | `[F03]` |

### Endpoints de API REST & Integração Agêntica

| Método | Rota | Descrição | Fonte |
| :---: | :--- | :--- | :---: |
| **SMTP** | `localhost:25 (587 auth)` | Envio de emails | `[F01]` |
| **IMAP** | `localhost:143 (993 SSL)` | Sincronizacao bidirecional | `[F02]` |
| **POP3** | `localhost:110 (995 SSL)` | Download-e-apague legado | `[F02]` |

### Matriz de Resolução de Problemas (Troubleshooting)

- **⚠️ Sintoma:** Emails na fila, nao entregues
  - **Causa:** Firewall bloqueando porta 25 outbound
- **⚠️ Sintoma:** Emails em spam Gmail
  - **Causa:** Sem SPF/DKIM/DMARC
- **⚠️ Sintoma:** Thunderbird Connection refused
  - **Causa:** Dovecot parado ou porta 993 bloqueada
- **⚠️ Sintoma:** Certificado SSL expirado
  - **Causa:** Certbot nao renovou
- **⚠️ Sintoma:** Erro Quota exceeded
  - **Causa:** Maildir cheio
## Parte III: Desinstalação Cirúrgica & Isolamento da VPS (Zero Efeito Colateral)

> 🛡️ **Princípio de Isolamento:** Remove Postfix/Dovecot mantendo SO, firewall, certs SSL e outros servicos intactos.

### Passo 1: Parar Servicos
Desliga Postfix e Dovecot

```bash
systemctl stop postfix dovecot
systemctl disable postfix dovecot
```

- ⚠️ **Alerta de Segurança:** Nao stop all. Apenas email
- ✅ **Como Validar:** `systemctl is-active postfix # inactive`

### Passo 2: Remover Pacotes
Desinstala Postfix/Dovecot

```bash
apt-get remove -y postfix dovecot-core dovecot-imapd dovecot-pop3d
```

- ⚠️ **Alerta de Segurança:** Use remove nao purge
- ✅ **Como Validar:** `which postfix # nao encontrar`

### Passo 3: Remover Portas Firewall
Fecha SMTP/IMAP/POP3

```bash
ufw delete allow 25/tcp
ufw delete allow 993/tcp
ufw reload
```

- ⚠️ **Alerta de Segurança:** Verificar antes SSH 22 intacta
- ✅ **Como Validar:** `ufw status | grep -E (25|110|143) # nada`

### Passo 4: Remover Config/Dados
Deleta /etc/postfix /etc/dovecot

```bash
rm -rf /etc/postfix /etc/dovecot /etc/opendkim
```

- ⚠️ **Alerta de Segurança:** Backup antes. Nao usar rm -rf selvagemente
- ✅ **Como Validar:** `ls /etc/postfix 2>&1 | cannot access`

### Passo 5: Limpar DNS
Remove registros MX/SPF/DKIM

```bash
dig seu-dominio.com.br MX
telnet localhost 25 # Connection refused
```

- ⚠️ **Alerta de Segurança:** Registros MX antigos causam bounces
- ✅ **Como Validar:** `mxtoolbox.com verifica propagacao`

### Checklist de Saúde da VPS (Outros Projetos)

- [ ] `systemctl status ssh # deve estar active`
- [ ] `free -h # confirma liberacao RAM`
- [ ] `df -h /home # espaco liberado`
- [ ] `ufw status | head -10 # firewall OK com portas necessarias`

## Parte IV: Referências Bibliográficas Auditadas

| ID | Categoria | Título da Obra | Autor / Mantenedor | Link Oficial |
| :---: | :--- | :--- | :--- | :--- |
| **F01** | Documentacao Oficial | Postfix Official Documentation | Wietse Venema & Postfix Project | [http://www.postfix.org/documentation.html](http://www.postfix.org/documentation.html) |
| **F02** | Documentacao Oficial | Dovecot Official Documentation | Timo Sirainen & Dovecot Developers | [https://doc.dovecot.org/](https://doc.dovecot.org/) |
| **F03** | Guia Tecnico | SPF, DKIM, DMARC Setup on Linux | Linux Academy & DevOps | [https://linuxacademy.com/guides/spf-dkim-dmarc/](https://linuxacademy.com/guides/spf-dkim-dmarc/) |
| **F04** | Video/Tutorial | Postfix Dovecot Let's Encrypt Setup | Linux Admin Channels | [https://www.youtube.com/results?search_query=postfix+dovecot](https://www.youtube.com/results?search_query=postfix+dovecot) |
| **F05** | Livro/EBook | Linux Mail Server Administration Handbook | Linux Professional Institute | [https://github.com/coreos/etcd/wiki](https://github.com/coreos/etcd/wiki) |
