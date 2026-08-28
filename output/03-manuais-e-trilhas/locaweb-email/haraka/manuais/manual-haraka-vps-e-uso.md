# Manual Operacional Completo: Haraka

> **Padrão Diamante · Guia de Engenharia & Adoção Descomplicada** 
> **Licença:** MIT | **Versão:** 3.0.0 | **Setup Estimado:** 30 a 45 minutos 
> **VPS Recomendada:** Contabo Cloud VPS S ou Hetzner CPX11 (2 vCPU, 4 GB RAM, 80 GB SSD NVMe, Ubuntu 24.04 LTS (x86_64)) 
> **Custo Mensal Estimado:** EUR 4,00 a EUR 8,00/mês (R$ 24 a R$ 48/mês)

---

## Módulo 0: Nivelamento Conceitual (Analogias do Dia a Dia)

### Haraka (A Ferramenta) *(Analogia: O Gerente de Correspondência da Sua Empresa)*
Um servidor SMTP que recebe emails, valida, analisa (spam, vírus) e os encaminha para o destino. Você tem total controle, diferente do Locaweb.

### SMTP Gateway *(Analogia: Uma Comporta Controlada de Água)*
Locaweb é uma comporta que você não controla. Haraka é a comporta na sua própria casa: você vê cada gota de água (email).

### Node.js Runtime *(Analogia: Um Intérprete Simultâneo)*
Haraka é escrito em JavaScript e roda sobre Node.js: rápido, paralelo e fácil de estender com plugins.

### VPS e Infraestrutura Própria *(Analogia: Sua Agência de Correios Privada)*
Em vez de usar Locaweb, você aluga sua própria VPS por R$ 50-100/mês e monta sua agência de correios pessoal.

## Parte I: Instalação em Produção na VPS (Passo a Passo Rígido)

### Passo 1: Alugar a VPS e Acessar via SSH `[F01]`
Acesse contabo.com ou hetzner.cloud, crie sua conta, clique em 'Add Server', escolha Ubuntu 24.04 LTS. Em 30 segundos você receberá por e-mail o endereço IP do seu servidor.

> **Entenda com uma analogia:** É o equivalente a pegar a chave de sua nova sala comercial alugada e ligar para a recepção.

```bash
# Substitua SEU_IP_AQUI pelo IP que você recebeu por email
ssh root@SEU_IP_AQUI
```

- **O que você verá na tela:** Uma janela de terminal com cursor piscando, pronta para receber suas instruções.
- **Como saber se deu certo:** Você conseguirá fazer login sem erros e verá o prompt 'root@servidor:~#'.

### Passo 2: Atualizar o Sistema e Instalar Dependências `[F02]`
Atualizamos os repositórios do Linux e instalamos Node.js e ferramentas essenciais para Haraka.

> **Entenda com uma analogia:** Varrer o chão da sala comercial nova e colocar as prateleiras essenciais no lugar.

```bash
apt update && apt upgrade -y
apt install -y curl git build-essential nodejs npm
node --version && npm --version
```

- **O que você verá na tela:** Várias linhas de download e instalação de pacotes passarão pela tela durante 2-3 minutos.
- **Como saber se deu certo:** Execute 'node --version' e verá 'v20.x.x' ou superior. Execute 'npm --version' e verá '10.x.x' ou superior.

### Passo 3: Instalar Haraka Globalmente `[F03]`
Instalamos o Haraka via npm (gerenciador de pacotes Node.js) e inicializamos o diretório de configuração.

> **Entenda com uma analogia:** Colocar a máquina de correios (Haraka) no chão pronto para funcionar.

```bash
npm install -g haraka
haraka -i /etc/haraka
haraka --version
```

- **O que você verá na tela:** Várias linhas de instalação de módulos npm. Ao final, mensagem 'added X packages'.
- **Como saber se deu certo:** Execute 'haraka --version' e verá '3.0.0' ou superior.

### Passo 4: Configurar Arquivo de Hosts Local `[F04]`
Registramos o hostname do servidor para evitar loops de DNS.

> **Entenda com uma analogia:** Colocar um aviso na porta: 'Este é o servidor mail.suaempresa.com.br'.

```bash
echo 'mail.suaempresa.com.br localhost' >> /etc/hosts
cat /etc/hosts | tail -3
```

- **O que você verá na tela:** Sem feedback visível, operação silenciosa.
- **Como saber se deu certo:** Execute 'cat /etc/hosts | grep suaempresa' e verá a entrada adicionada.

### Passo 5: Gerar Certificado SSL com LetsEncrypt `[F05]`
Provisionamos um certificado TLS GRATUITO para conexões criptografadas SMTPS (porta 465) e Submission (porta 587).

> **Entenda com uma analogia:** Instalar um lacre inviolável nos Correios para que ninguém intercepção seus emails.

```bash
apt install -y certbot
certbot certonly --standalone -d mail.suaempresa.com.br --agree-tos -n -m admin@suaempresa.com.br
ls -la /etc/letsencrypt/live/mail.suaempresa.com.br
```

- **O que você verá na tela:** Várias linhas de validação de domínio. Mensagem 'Successfully received certificate'.
- **Como saber se deu certo:** Execute 'ls -la /etc/letsencrypt/live/mail.suaempresa.com.br' e verá os arquivos de certificado.

### Passo 6: Iniciar Haraka em Produção `[F06]`
Iniciamos o Haraka como serviço systemd permanente que roda ao boot.

> **Entenda com uma analogia:** Apertar o botão verde no painel elétrico: as máquinas começam a operar 24/7.

```bash
cd /etc/haraka && npm start &
sleep 3
systemctl status haraka
```

- **O que você verá na tela:** Mensagem 'Started Haraka SMTP Server'.
- **Como saber se deu certo:** Execute 'systemctl status haraka' e verá 'active (running)'.

## Arquivos de Configuração de Produção

### `/etc/haraka/config/smtpd.ini`
*Arquivo de configuração principal do Haraka: define hostname, portas, certificados SSL e quais plugins ativar.*

```ini
[main]
host = mail.suaempresa.com.br
port = 25

[tls]
key = /etc/letsencrypt/live/mail.suaempresa.com.br/privkey.pem
cert = /etc/letsencrypt/live/mail.suaempresa.com.br/fullchain.pem

[plugins]
known_hosts
spam_header
limit_concurrency = 10
```

## Parte II: Manual de Uso Exaustivo

**Arquitetura Operacional:** Haraka funciona como um servidor SMTP que recebe emails na porta 25, valida remetentes contra bancos de dados, executa filtros antispam (rspamd/spamassassin), analisa vírus (clamav), e encaminha para destino final. Diferente do Locaweb, você vê e controla cada email que passa.

### Roteiro de Primeiro Voo (Sua Primeira Reunião em 3 Minutos)

1. **Passo 1: Testar Conectividade SMTP:** No seu computador local, abra um terminal e execute 'telnet mail.suaempresa.com.br 25'. Você deve receber a resposta '220 mail.suaempresa.com.br ESMTP Haraka'.
 - **Resultado Esperado:** Conexão bem-sucedida com o servidor SMTP. Se receber erro, verifique se a porta 25 está aberta no firewall.

1. **Passo 2: Enviar Email de Teste:** Use um cliente de email (Thunderbird, Outlook, Apple Mail) ou comando 'mail': configure SMTP como 'mail.suaempresa.com.br', porta 25, sem autenticação, e envie email para teste@gmail.com.
 - **Resultado Esperado:** Email chega na caixa de entrada do destinatário em segundos. Verifique os logs do servidor: 'tail -f /var/log/haraka/haraka.log'.

1. **Passo 3: Validar SPF/DKIM/DMARC:** Acesse https://mxtoolbox.com/spf.aspx?domain=suaempresa.com.br e coloque seu domínio. Deve aparecer score 10/10 em SPF.
 - **Resultado Esperado:** Seu domínio tem proteção completa contra spoofing e emails não caem em spam.

### Dicionário Completo de Comandos (CLI)

| Comando / Flag | Descrição Técnica | Exemplo de Execução | Fonte |
| :--- | :--- | :--- | :---: |
| `haraka -v` | Mostra a versão atual do Haraka | `haraka -v
# Retorna: Haraka 3.0.0` | `[F01]` |
| `systemctl status haraka` | Verifica se o serviço Haraka está rodando | `systemctl status haraka
# Retorna: active (running) since...` | `[F02]` |
| `tail -f /var/log/haraka/haraka.log` | Segue os logs em tempo real do Haraka | `tail -f /var/log/haraka/haraka.log` | `[F03]` |
| `npm install <plugin-name>` | Instala um novo plugin Haraka | `cd /etc/haraka && npm install haraka-plugin-rspamd` | `[F04]` |

### Endpoints de API REST & Integração Agêntica

| Método | Rota | Descrição | Fonte |
| :---: | :--- | :--- | :---: |
| **GET** | `/admin/queue` | Lista emails pendentes na fila | `[F01]` |
| **POST** | `/admin/config/reload` | Recarrega configuração sem reiniciar o servidor | `[F02]` |

### Matriz de Resolução de Problemas (Troubleshooting)

- ** Sintoma:** Emails sendo rejeitados com erro '550 User not found'
 - **Causa:** O plugin 'rcpt_to' está validando destinatários contra banco de dados, mas a consulta falhou.
- ** Sintoma:** Fila de emails crescendo (processos lentos)
 - **Causa:** Limite de concorrência baixo ou DNS timeout na validação de MX records do destinatário.
- ** Sintoma:** Certificado SSL expirado (erro TLS 'certificate expired')
 - **Causa:** LetsEncrypt não renovou automaticamente
## Parte III: Desinstalação Cirúrgica & Isolamento da VPS (Zero Efeito Colateral)

## Parte IV: Referências Bibliográficas Auditadas

| ID | Categoria | Título da Obra | Autor / Mantenedor | Link Oficial |
| :---: | :--- | :--- | :--- | :--- |
| **F01** | Documentação Oficial | RFC 5321 - Simple Mail Transfer Protocol | IETF | [https://tools.ietf.org/html/rfc5321](https://tools.ietf.org/html/rfc5321) |
| **F02** | Documentação Oficial | Haraka Official Documentation & GitHub | Haraka Community & Jason Walker | [https://haraka.github.io/](https://haraka.github.io/) |
| **F03** | Guia Técnico | DKIM, SPF and DMARC - MXToolbox Reference | MXToolbox Community | [https://mxtoolbox.com/](https://mxtoolbox.com/) |
| **F04** | Documentação Oficial | LetsEncrypt - Free SSL/TLS Certificates | Electronic Frontier Foundation (EFF) | [https://letsencrypt.org/](https://letsencrypt.org/) |
| **F05** | Documentação Oficial | Rspamd - Spam Filtering with Machine Learning | Vsevolod Stakhov & Rspamd Community | [https://rspamd.com/](https://rspamd.com/) |
| **F06** | Documentação Oficial | Node.js Official Documentation & Runtime | OpenJS Foundation | [https://nodejs.org/en/docs/](https://nodejs.org/en/docs/) |
