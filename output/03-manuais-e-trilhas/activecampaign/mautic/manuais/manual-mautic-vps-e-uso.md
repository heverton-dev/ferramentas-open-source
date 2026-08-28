# Manual Operacional Completo: Mautic

> **Padrão Diamante · Guia de Engenharia & Adoção Descomplicada**  
> **Licença:** OSL-3.0 | **Versão:** 5.1.2 | **Setup Estimado:** 45 a 90 minutos (Conhecimento intermediário de Linux e MySQL)  
> **VPS Recomendada:** Hetzner Cloud CX21 (2 vCPU, 4 GB RAM, EUR 9,90) ou Contabo Cloud VPS M (2 vCPU Dedicadas (AMD EPYC ou Intel Xeon E5), 4 GB RAM mínimo (8 GB recomendado para até 50k leads ativos), 80 GB SSD NVMe (mínimo 40 GB, crescer conforme volume de dados), Ubuntu 22.04 LTS (x86_64) ou Debian 12)  
> **Custo Mensal Estimado:** EUR 9,90 a 19,90/mês (~R$ 60 a R$ 120 na cotação média)

---

## Módulo 0: Nivelamento Conceitual (Analogias do Dia a Dia)

### 💡 Mautic (A Ferramenta) *(Analogia: O Gerenciador de Relacionamento Automático da Sua Empresa)*
Mautic é como ter um assistente pessoal que monitora todos os visitantes do seu site, envia emails automaticamente quando alguém demonstra interesse, segmenta contatos por comportamento e gera relatórios sobre o que funcionou. Sem pagar nada a plataformas estrangeiras. Você é o dono absoluto dos seus dados de clientes.

### 💡 VPS (Servidor Privado Virtual) *(Analogia: Uma Sala Comercial Alugada que Nunca Apaga a Luz)*
Em vez de deixar um computador ligado no escritório como servidor, você aluga por R$ 80 a R$ 200 por mês um computador profissional 24/7 em um data center na nuvem (como Hetzner, Contabo ou DigitalOcean). Ele fica sempre conectado com internet de altíssima velocidade.

### 💡 MariaDB / MySQL (Banco de Dados) *(Analogia: O Arquivo de Caixas de Contatos e Eventos)*
Mautic precisa guardar milhares de contatos, históricos de cliques, emails enviados e pontuação de leads. MariaDB é o grande arquivo organizado onde tudo isso fica registrado. Sem ele, Mautic não teria memória.

### 💡 Apache / Nginx (Servidor Web) *(Analogia: O Recepcionista que Atende as Chamadas)*
Quando alguém digita mautic.sua-empresa.com.br no navegador, Apache ou Nginx são quem recebem a chamada, pegam o Mautic e mostram a tela. Também servem os scripts de rastreamento que identificam seus visitantes.

### 💡 Pixel de Rastreamento *(Analogia: O Vendedor Invisível que Segue o Cliente)*
Você coloca um código HTML minúsculo no seu site. Quando um visitante chega, esse código 'vê' tudo que a pessoa faz: qual página visitou, por quanto tempo ficou, se preencheu um formulário. Mautic guarda tudo isso automaticamente.

### 💡 Automação de Email *(Analogia: Um Sistema de Resposta Automática que Aprendia)*
Configurar que, quando um contato preenche um formulário, ele automaticamente recebe um email em 5 minutos é fácil em Mautic. Se ele clicar no email, recebe outro. Se não clicar em 3 dias, recebe algo diferente. Tudo sem você digitar um comando manual.

### 💡 Leads & Pontuação (Lead Scoring) *(Analogia: Anotações de Temperamento no Caderno do Vendedor)*
Vendedores experientes anotam: 'Este cliente clicou 5 vezes, visitou a página de preços, preencheu seus dados = está quente, ligue agora'. Mautic faz exatamente isso automaticamente, marcando quem está quente para vender.

## Parte I: Instalação em Produção na VPS (Passo a Passo Rígido)

### Passo 1: Acessar a VPS via SSH e Atualizar o Sistema `[F01]`
Você se conecta ao seu servidor alugado como o 'dono da casa'. O primeiro passo é garantir que todas as ferramentas já instaladas estejam atualizadas e seguras.

> 💡 **Entenda com uma analogia:** Como dar uma olhada geral na casa alugada antes de começar a obra.

```bash
ssh root@seu_ip_vps
sudo apt-get update
sudo apt-get upgrade -y
```

- 🖥️ **O que você verá na tela:** Você verá linhas em preto e branco mostrando quais pacotes foram atualizados.
- ✅ **Como saber se deu certo:** Termina com 'Setting up...' sem mensagens de ERRO em vermelho.

### Passo 2: Instalar Apache2, PHP 8.2 e Extensões Obrigatórias `[F01]`
Mautic é escrito em PHP e precisa do Apache para funcionar. Também precisamos de bibliotecas extras que o Mautic depende para fazer análises e processamento de dados.

> 💡 **Entenda com uma analogia:** Comprar as ferramentas específicas (martelo, chave inglesa, nível) antes de montar a prateleira.

```bash
sudo apt-get install -y apache2 libapache2-mod-php php8.2-cli php8.2-fpm php8.2-mysql php8.2-curl php8.2-gd php8.2-xml php8.2-mbstring php8.2-zip php8.2-bcmath php8.2-intl
sudo systemctl start apache2
sudo systemctl enable apache2
```

- 🖥️ **O que você verá na tela:** Vará muitas linhas com pacotes sendo baixados e descompactados. Pode levar 2-3 minutos.
- ✅ **Como saber se deu certo:** Termina com 'Processing triggers' e apache2 aparece como 'active (running)'.

### Passo 3: Instalar MariaDB e Criar Banco de Dados para Mautic `[F01]`
MariaDB é o arquivo gigante onde Mautic guarda todos os contatos, emails, históricos. Vamos instalá-lo, criar um banco chamado 'mautic_db' e um usuário exclusivo.

> 💡 **Entenda com uma analogia:** Montar o grande arquivo da empresa com gavetas (banco de dados), pastas (tabelas) e etiquetas (usuário exclusivo).

```bash
sudo apt-get install -y mariadb-server
sudo systemctl start mariadb
sudo systemctl enable mariadb
sudo mysql -u root -e "CREATE DATABASE mautic_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
sudo mysql -u root -e "CREATE USER 'mautic_user'@'localhost' IDENTIFIED BY 'SenhaSegura123!MauticVPS';"
sudo mysql -u root -e "GRANT ALL PRIVILEGES ON mautic_db.* TO 'mautic_user'@'localhost';"
sudo mysql -u root -e "FLUSH PRIVILEGES;"
```

- 🖥️ **O que você verá na tela:** Será pedida uma senha para o administrador do MariaDB. Digite algo seguro.
- ✅ **Como saber se deu certo:** Após digitar a senha, MariaDB abre um prompt mysql> ou retorna à linha de comando sem erros.

### Passo 4: Baixar e Descompactar Mautic 5.1.2 `[F01]`
Vamos buscar o Mautic pronto do repositório oficial no GitHub, descompactar na pasta de aplicações e preparar as permissões.

> 💡 **Entenda com uma analogia:** Comprar um kit de móvel pronto do fabricante e desempacotar na sala.

```bash
cd /tmp
wget https://github.com/mautic/mautic/releases/download/5.1.2/mautic-5.1.2.zip
unzip mautic-5.1.2.zip
sudo mkdir -p /var/www/mautic
sudo mv mautic/* /var/www/mautic/
sudo chown -R www-data:www-data /var/www/mautic
sudo chmod -R 755 /var/www/mautic
```

- 🖥️ **O que você verá na tela:** Verá um comando wget ou curl baixando um arquivo .zip grande (~130 MB). Depois, a descompactação mostrará centenas de arquivos.
- ✅ **Como saber se deu certo:** A pasta /var/www/mautic existe com subdirectórios app/, core/, plugins/, etc.

### Passo 5: Configurar Apache para Servir Mautic `[F01]`
Criamos um arquivo de configuração do Apache que diz: 'Quando alguém digita mautic.sua-empresa.com.br, serve os arquivos de /var/www/mautic'.

> 💡 **Entenda com uma analogia:** Colocar a placa com o endereço da loja na porta da rua.

```bash
sudo nano /etc/apache2/sites-available/mautic.conf
sudo a2ensite mautic.conf
sudo systemctl reload apache2
```

- 🖥️ **O que você verá na tela:** Você abrirá um editor de texto (nano) e colará configurações. Depois ativa o site com a2ensite.
- ✅ **Como saber se deu certo:** O comando 'apache2ctl configtest' retorna 'Syntax OK'.

### Passo 6: Ativar HTTPS com Let's Encrypt (SSL Gratuito) `[F01]`
Mautic NUNCA funciona em HTTP puro (sem criptografia). Precisamos de um certificado SSL gratuito do Let's Encrypt. Será gerado automaticamente e renovado a cada 3 meses.

> 💡 **Entenda com uma analogia:** Colocar um cadeado de segurança na porta de entrada da loja.

```bash
sudo apt-get install -y certbot python3-certbot-apache
sudo certbot --apache -d mautic.sua-empresa.com.br
```

- 🖥️ **O que você verá na tela:** Certbot fará perguntas sobre seu email e domínio. Depois, modificará automaticamente o arquivo do Apache.
- ✅ **Como saber se deu certo:** Acessar https://mautic.sua-empresa.com.br no navegador sem avisos de certificado inválido.

### Passo 7: Acessar o Mautic Web Installer e Completar Configuração `[F02]`
Agora você acessa https://mautic.sua-empresa.com.br e segue um assistente passo a passo que testa tudo, conecta o banco de dados e cria o primeiro usuário administrador.

> 💡 **Entenda com uma analogia:** O primeiro boot de um novo smartphone: perguntas sobre idioma, conta, preferências.

```bash
Nenhum comando. Tudo é feito via navegador web em https://mautic.sua-empresa.com.br
```

- 🖥️ **O que você verá na tela:** Uma página HTML bonita pedindo seus dados: Email do Admin, Senha, Informações da Empresa, etc.
- ✅ **Como saber se deu certo:** Você consegue fazer login com email/senha criados e vê o dashboard do Mautic.

### Passo 8: Configurar Cron Jobs para Processamento Automático `[F03]`
Mautic precisa de tarefas agendadas para enviar emails em lote, processar rastreamento e atualizar pontuação de leads. Configuramos isso no Crontab do Linux.

> 💡 **Entenda com uma analogia:** Um gerenciador de projetos que acorda às 7h, 9h, 12h e 15h para despachar tarefas.

```bash
sudo crontab -e
# Adicionar estas linhas:
*/5 * * * * /usr/bin/php /var/www/mautic/bin/console mautic:queue:process --env=prod
*/5 * * * * /usr/bin/php /var/www/mautic/bin/console mautic:import:create --env=prod
```

- 🖥️ **O que você verá na tela:** Abre-se um arquivo de texto com linhas que começam com asteriscos. Você adiciona as novas linhas.
- ✅ **Como saber se deu certo:** O comando 'crontab -l' mostra as linhas adicionadas. Logs em /var/log/syslog confirmam execução.

### Passo 9: Configurar Backup Automatizado do Banco de Dados `[F04]`
Dados de clientes são ouro. Configuramos um script que faz backup completo do MariaDB toda noite e envia para armazenamento externo (opcional).

> 💡 **Entenda com uma analogia:** Tirar uma fotografia de toda a caixa de arquivos todo dia e guardar em local seguro.

```bash
sudo mkdir -p /backups
sudo nano /usr/local/bin/backup-mautic.sh
# Adicionar conteúdo do script
sudo chmod +x /usr/local/bin/backup-mautic.sh
sudo crontab -e
# Adicionar: 0 2 * * * /usr/local/bin/backup-mautic.sh
```

- 🖥️ **O que você verá na tela:** Você cria um script bash em /usr/local/bin e o adiciona ao crontab.
- ✅ **Como saber se deu certo:** Arquivo .sql.gz existe em /backups/ com timestamp de hoje.

## Arquivos de Configuração de Produção

### `/etc/apache2/sites-available/mautic.conf`
*Este arquivo diz ao Apache como servir o Mautic. Ativa mod_rewrite (necessário para URLs amigáveis), define permissões e logs. Certbot modificará isso para adicionar HTTPS automaticamente.*

```apache
<VirtualHost *:80>
    ServerName mautic.sua-empresa.com.br
    DocumentRoot /var/www/mautic/
    <Directory /var/www/mautic/>
        Options -Indexes +FollowSymLinks
        AllowOverride All
        Require all granted
        <IfModule mod_rewrite.c>
            RewriteEngine On
            RewriteBase /
            RewriteCond %{REQUEST_FILENAME} !-f
            RewriteCond %{REQUEST_FILENAME} !-d
            RewriteRule ^(.*) index.php [L]
        </IfModule>
    </Directory>
    ErrorLog ${APACHE_LOG_DIR}/mautic-error.log
    CustomLog ${APACHE_LOG_DIR}/mautic-access.log combined
</VirtualHost>
```

### `/var/www/mautic/.env.local`
*Configurações críticas do Mautic: ambiente de produção, banco de dados e email. O APP_SECRET deve ser gerado com: openssl rand -hex 32. Substitua os valores SMTP com seus dados reais de email.*

```ini
APP_ENV=prod
APP_DEBUG=0
APP_SECRET=SenhaSeguraAleatoria123456789
DB_DRIVER=pdo_mysql
DB_HOST=localhost
DB_PORT=3306
DB_NAME=mautic_db
DB_USER=mautic_user
DB_PASSWORD=SenhaSegura123!MauticVPS
DB_TABLE_PREFIX=mt_
SMTP_HOST=smtp.seuservidor.com.br
SMTP_PORT=587
SMTP_USER=seu-email@seuservidor.com.br
SMTP_PASSWORD=senhadoemail
SMTP_ENCRYPTION=tls
SMTP_AUTH_MODE=login
```

### `/usr/local/bin/backup-mautic.sh`
*Script que automatiza backup diário do banco de dados (SQL comprimido) e arquivos do Mautic. Exclui pastas temporárias e de cache. Deleta backups com mais de 30 dias para economizar espaço.*

```bash
#!/bin/bash
BACKUP_DIR="/backups"
DATE=$(date +%Y%m%d_%H%M%S)
DB_NAME="mautic_db"
DB_USER="mautic_user"
DB_PASSWORD="SenhaSegura123!MauticVPS"
FILES_DIR="/var/www/mautic"

echo "[$(date)] Iniciando backup de Mautic..." >> /var/log/mautic-backup.log

mysqldump -u $DB_USER -p$DB_PASSWORD $DB_NAME | gzip > $BACKUP_DIR/mautic_db_$DATE.sql.gz

tar --exclude='cache' --exclude='logs' --exclude='tmp' -czf $BACKUP_DIR/mautic_files_$DATE.tar.gz -C /var/www mautic/

find $BACKUP_DIR -name 'mautic_*' -mtime +30 -delete

echo "[$(date)] Backup concluído com sucesso." >> /var/log/mautic-backup.log
```

## Parte II: Manual de Uso Exaustivo

**Arquitetura Operacional:** Mautic funciona em três camadas: (1) Interface Web (Apache/PHP) para usuários acessarem dashboard e configurar campanhas. (2) Banco de Dados (MariaDB) armazenando leads, eventos, histórico de campanhas. (3) Cron Jobs processando tarefas de fundo: envio de emails, rastreamento de visitantes, atualização de pontuação. O Pixel de Rastreamento (JavaScript) embutido no site do cliente captura comportamento e envia para Mautic em tempo real.

### Roteiro de Primeiro Voo (Sua Primeira Reunião em 3 Minutos)

1. **1. Fazer login no dashboard:** Abra https://mautic.sua-empresa.com.br em um navegador. Digite seu email e senha de admin.
   - 🎯 **Resultado Esperado:** Você vê a página inicial do Mautic com 4 blocos (Leads, Campanhas, Formulários, Gráfico de Atividade)

1. **2. Instalar Pixel de Rastreamento:** Menu esquerdo > Tracking > Copie o código HTML. Cole no rodapé de TODAS as páginas do seu site.
   - 🎯 **Resultado Esperado:** Abra seu site em outro navegador/aba. Volte ao Mautic. Em Tracking, 'Visitantes Anônimos' > 0

1. **3. Criar Formulário de Captura:** Menu esquerdo > Forms > Novo Formulário. Adicione campo Email (obrigatório). Defina ação: 'Adicionar a Segmento Newsletter'. Publique.
   - 🎯 **Resultado Esperado:** Copie o código HTML gerado. Cole em uma página do seu site e preencha o formulário com seu email. Voltando ao Mautic, vê um novo lead com seu email.

1. **4. Criar Primeira Campanha de Email:** Menu esquerdo > Campaigns > Novo. Arraste bloco 'Send Email'. Configure Email de Boas-vindas. Adicione Delay (5 minutos). Adicione outro Email. Selecione segmento Newsletter. Publique.
   - 🎯 **Resultado Esperado:** Teste preenchendo o formulário com novo email. Aguarde 5 minutos. Esse email deve chegar em sua caixa de entrada com título 'Bem-vindo à nossa Newsletter'.

### Dicionário Completo de Comandos (CLI)

| Comando / Flag | Descrição Técnica | Exemplo de Execução | Fonte |
| :--- | :--- | :--- | :---: |
| `php /var/www/mautic/bin/console mautic:queue:process --env=prod` | Processa fila de email pendente, rastreamento e leads não-sincronizados. Execute manualmente se cron não estiver rodando ou para teste. | `sudo -u www-data php /var/www/mautic/bin/console mautic:queue:process --env=prod` | `[F03]` |
| `php /var/www/mautic/bin/console cache:clear --env=prod` | Limpa cache (arquivos temporários de velocidade). Use se Mautic estiver lento ou após atualizar. | `sudo -u www-data php /var/www/mautic/bin/console cache:clear --env=prod` | `[F03]` |
| `php /var/www/mautic/bin/console mautic:update:apply --env=prod` | Aplicar atualizações de versão do Mautic (quando nova versão disponível). | `sudo -u www-data php /var/www/mautic/bin/console mautic:update:apply --env=prod` | `[F03]` |

### Endpoints de API REST & Integração Agêntica

| Método | Rota | Descrição | Fonte |
| :---: | :--- | :--- | :---: |
| **GET** | `/api/leads` | Listar todos os leads da conta. Retorna array JSON com id, email, nome, etc. | `[F05]` |
| **POST** | `/api/leads` | Criar novo lead via API. Útil para integrar com formulários externos. | `[F05]` |
| **GET** | `/api/campaigns` | Listar campanhas. Use para monitorar campanhas ativas via programação. | `[F05]` |

### Matriz de Resolução de Problemas (Troubleshooting)

- **⚠️ Sintoma:** Mautic carrega muito lento (mais de 5 segundos)
  - **Causa:** Banco de dados com muitos leads (>100k) sem índices otimizados. Ou VPS com RAM insuficiente (2GB em vez de 4GB).
- **⚠️ Sintoma:** Emails não estão sendo enviados
  - **Causa:** Cron jobs não rodando. Ou configuração SMTP incorreta (servidor de email rejeitando).
- **⚠️ Sintoma:** Pixel de rastreamento não captura visitantes
  - **Causa:** Código HTML do pixel não foi colado corretamente. Ou JavaScript bloqueado por Ad-blocker.
- **⚠️ Sintoma:** Erro 404 ao acessar mautic.sua-empresa.com.br
  - **Causa:** Apache não recarregou após criar arquivo mautic.conf. Ou domínio não aponta para VPS.
- **⚠️ Sintoma:** Aviso de certificado SSL inválido no navegador
  - **Causa:** Let's Encrypt não renovou ou foi instalado incorretamente.
## Parte III: Desinstalação Cirúrgica & Isolamento da VPS (Zero Efeito Colateral)

> 🛡️ **Princípio de Isolamento:** Mautic foi instalado em estrutura totalmente isolada: aplicação em /var/www/mautic/, banco de dados em schema 'mautic_db', usuário MySQL dedicado, configurações em /etc/apache2/sites-available/mautic.conf. Esta modularidade permite remoção cirúrgica sem efeitos colaterais. Outros websites/aplicações na VPS não serão afetadas. Seguindo estes passos, Mautic desaparece completamente, deixando a VPS tão limpa quanto antes.

### Passo 1: Parar Serviços do Mautic
Interrompa os cron jobs que executam tarefas de Mautic e desative o site no Apache.

```bash
sudo crontab -e
# Remover ou comentar (com #) as linhas:
# */5 * * * * /usr/bin/php /var/www/mautic/bin/console mautic:queue:process --env=prod

sudo a2dissite mautic.conf
sudo systemctl reload apache2
sudo systemctl stop php8.2-fpm
```

- ⚠️ **Alerta de Segurança:** ALERTA: Após este passo, mautic.sua-empresa.com.br será inacessível (erro 404/503).
- ✅ **Como Validar:** `Digitar https://mautic.sua-empresa.com.br em outro navegador deve retornar erro 404 ou 'site indisponível'`

### Passo 2: Backup Final de Segurança (Altamente Recomendado)
Se houver qualquer chance de precisar dos dados depois, faz um backup final antes de deletar.

```bash
mysqldump -u mautic_user -p mautic_db | gzip > ~/mautic_backup_final_$(date +%Y%m%d).sql.gz
tar -czf ~/mautic_files_backup_final_$(date +%Y%m%d).tar.gz /var/www/mautic/
```

- ⚠️ **Alerta de Segurança:** CRÍTICO: Sem este backup, os dados são irrecuperáveis após próximas etapas.
- ✅ **Como Validar:** `Dois arquivos .gz existem em $HOME com tamanho > 10MB`

### Passo 3: Remover Banco de Dados do Mautic do MariaDB
Deletar completamente o banco de dados e o usuário do MariaDB. Sem possibilidade de recuperação.

```bash
sudo mysql -u root
DROP DATABASE mautic_db;
DROP USER 'mautic_user'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

- ⚠️ **Alerta de Segurança:** PONTO DE NÃO-RETORNO: Após este comando, banco de dados é deletado permanentemente.
- ✅ **Como Validar:** `sudo mysql -u root -e 'SELECT user FROM mysql.user;' deve NÃO conter 'mautic_user'`

### Passo 4: Remover Pasta e Arquivos do Mautic
Deletar todos os arquivos da aplicação Mautic da VPS. Sem possibilidade de recuperação sem backup.

```bash
sudo rm -rf /var/www/mautic/
sudo rm -f /etc/apache2/sites-available/mautic.conf
sudo rm -f /etc/apache2/sites-available/mautic-ssl.conf
sudo rm -f /usr/local/bin/backup-mautic.sh
sudo rm -rf /var/log/mautic*
```

- ⚠️ **Alerta de Segurança:** PONTO DE NÃO-RETORNO: Todos os arquivos de Mautic são deletados permanentemente.
- ✅ **Como Validar:** `sudo ls -la /var/www/ NÃO deve conter pasta 'mautic'. sudo ls /usr/local/bin/backup* retorna 'file not found'`

### Passo 5: Remover Certificado SSL (Opcional - Apenas se Mautic era único HTTPS)
Se Mautic era o único site HTTPS na VPS, pode remover o certificado Let's Encrypt.

```bash
sudo certbot delete --cert-name mautic.sua-empresa.com.br
```

- ⚠️ **Alerta de Segurança:** ATENÇÃO: Remova apenas se nenhum outro site na VPS usa este domínio.
- ✅ **Como Validar:** `sudo certbot certificates não deve listar 'mautic.sua-empresa.com.br'`

### Checklist de Saúde da VPS (Outros Projetos)

- [ ] `ESPAÇO EM DISCO: df -h | grep /dev/sda → Coluna 'Avail' deve ter >= 20GB livres`
- [ ] `PROCESSOS PHP: ps aux | grep php | grep mautic → Deve estar vazio (sem processos)`
- [ ] `PORTAS ESCUTANDO: sudo netstat -tlnp | grep LISTEN → Deve conter :22 (SSH), :80 (HTTP), :443 (HTTPS) apenas`
- [ ] `BANCO DE DADOS: sudo mysql -u root -e 'SHOW DATABASES;' → NÃO deve listar 'mautic_db'`
- [ ] `CRON JOBS: sudo crontab -l | grep mautic → Deve estar vazio`
- [ ] `ERROS APACHE: sudo tail -20 /var/log/apache2/error.log → NÃO deve conter 'mautic'`
- [ ] `SEGURANÇA SSH: sudo sshd -T | grep PermitRootLogin → Deve ser 'no' (boas práticas)`
- [ ] `FIREWALL: sudo ufw status → Se ativo, deve permitir :22, :80, :443 apenas`

## Parte IV: Referências Bibliográficas Auditadas

| ID | Categoria | Título da Obra | Autor / Mantenedor | Link Oficial |
| :---: | :--- | :--- | :--- | :--- |
| **F01** | Documentação Oficial | Mautic 5.1 - Guia de Instalação no Ubuntu | Mautic Community | [https://docs.mautic.org/en/5.1/setup/](https://docs.mautic.org/en/5.1/setup/) |
| **F02** | Documentação Oficial | Mautic Web Installer - Configuração Inicial | Mautic Community | [https://docs.mautic.org/en/5.1/setup/web_installer/](https://docs.mautic.org/en/5.1/setup/web_installer/) |
| **F03** | Documentação Oficial | Cron Jobs e Processamento em Background | Mautic Community | [https://docs.mautic.org/en/5.1/setup/cron_jobs/](https://docs.mautic.org/en/5.1/setup/cron_jobs/) |
| **F04** | Guia de Operação | Backup e Recuperação de Dados | Mautic Community | [https://docs.mautic.org/en/5.1/setup/database_backup/](https://docs.mautic.org/en/5.1/setup/database_backup/) |
| **F05** | API Documentation | API de Leads e Campanhas Mautic | Mautic Developer Docs | [https://docs.mautic.org/en/5.1/api/](https://docs.mautic.org/en/5.1/api/) |
