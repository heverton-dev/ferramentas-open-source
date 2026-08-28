# Manual Operacional Completo: Nextcloud Hub

> **Padrão Diamante · Guia de Engenharia & Adoção Descomplicada**  
> **Licença:** AGPL-3.0 | **Versão:** 30.x (Hub 9) | **Setup Estimado:** 20 a 30 minutos (Zero conhecimento prévio)  
> **VPS Recomendada:** Hetzner Cloud CPX41 (ou Contabo Cloud VPS L) (4 vCPU Dedicadas (AMD EPYC), 8 GB RAM ECC, 160 GB NVMe Gen4, Ubuntu 24.04 LTS (x86_64))  
> **Custo Mensal Estimado:** EUR 28,00/mês (~R$ 170,00/mês na cotação média)

---

## Módulo 0: Nivelamento Conceitual (Analogias do Dia a Dia)

### 💡 Nextcloud Hub (A Ferramenta) *(Analogia: O Seu Próprio Gmail + Google Drive + Agenda num Apartamento que Você Possui)*
O Nextcloud Hub é uma suíte completa que reúne e-mail, agenda, contatos, chat com vídeo e armazenamento de arquivos em um único painel. A diferença fundamental para o Google Workspace é que tudo fica guardado no seu próprio servidor: ninguém revende os seus dados nem os lê para treinar inteligência artificial de terceiros.

### 💡 VPS (Servidor Privado Virtual) *(Analogia: Uma Sala Comercial Alugada que Nunca Desliga)*
Em vez de depender dos servidores do Google, você aluga por cerca de R$ 170 por mês um computador profissional em um data center (Hetzner, Contabo, DigitalOcean). Ele fica ligado 24 horas por dia, com internet de fibra e geradores, pronto para entregar seus e-mails e arquivos.

### 💡 Docker & Containers *(Analogia: Uma Caixa de Sapatos Lacrada de Fábrica)*
O Docker entrega o Nextcloud dentro de uma 'caixa lacrada' com tudo que ele precisa para funcionar. Você não precisa instalar dezenas de programas manualmente: basta mandar a caixa abrir e o sistema sobe sozinho, isolado e seguro.

### 💡 Traefik (Proxy Reverso) *(Analogia: O Porteiro com Cadeado Verde (HTTPS))*
O Traefik é o recepcionista que atende na internet, coloca o cadeado de segurança (certificado SSL gratuito) em cada acesso e encaminha cada pessoa para o serviço certo (mail.empresa.com.br vai para o Nextcloud).

### 💡 CalDAV & CardDAV *(Analogia: A Língua Comum da Agenda e dos Contatos)*
São os 'idiomas abertos' que permitem que o seu celular (Android ou iPhone), o Outlook e o Thunderbird leiam e escrevam a mesma agenda e os mesmos contatos do Nextcloud, exatamente como o Google Calendar e o Google Contacts faziam.

## Parte I: Instalação em Produção na VPS (Passo a Passo Rígido)

### Passo 1: Como Alugar o Servidor e Abrir o Terminal `[F01]`
Acesse hetzner.com/cloud (ou contabo.com), crie a conta e clique em 'Add Server'. Escolha a imagem 'Ubuntu 24.04', o tipo 'CPX41' e a localização mais próxima do Brasil (EUA ou Finlândia). Em 30 segundos você receberá por e-mail o IP do servidor (ex: 123.45.67.89). No Windows, pressione Windows + R, digite 'powershell' e Enter. No Mac, abra o 'Terminal'.

> 💡 **Entenda com uma analogia:** É pegar a chave da sua nova sala comercial e abrir o laptop para falar com a recepção.

```bash
# Digite no seu computador (substitua pelo IP recebido por e-mail):
ssh root@SEU_IP_AQUI
```

- 🖥️ **O que você verá na tela:** Uma janela preta ou azul se abrirá com um cursor piscando aguardando comandos.
- ✅ **Como saber se deu certo:** Aparecerá a linha PS C:\Users\seu-nome> pronta para receber instruções.

### Passo 2: Blindagem Inicial do Servidor (Hardening & Firewall) `[F05]`
Criamos um usuário seguro 'deployer' para não usar a conta root, fechamos todas as portas perigosas e ativamos o firewall de proteção.

> 💡 **Entenda com uma analogia:** Instalar fechaduras tetra e colocar o porteiro na guarita com lista rígida de convidados.

```bash
adduser deployer && usermod -aG sudo deployer
ufw default deny incoming && ufw default allow outgoing
ufw allow 22/tcp && ufw allow 80/tcp && ufw allow 443/tcp
ufw --force enable
```

- 🖥️ **O que você verá na tela:** O sistema pedirá uma senha forte para o novo usuário e confirmará 'Firewall is active and enabled on system startup'.
- ✅ **Como saber se deu certo:** Digite 'ufw status' e veja as portas 22, 80 e 443 marcadas como 'ALLOW IN'.

### Passo 3: Instalação do Motor Docker Oficial `[F02]`
Instalamos o motor do Docker para que o Nextcloud, o banco de dados e o Traefik rodem em caixas isoladas e seguras.

> 💡 **Entenda com uma analogia:** Montar as prateleiras industriais no galpão para receber as caixas lacradas.

```bash
apt-get update && apt-get install -y ca-certificates curl
curl -fsSL https://get.docker.com | sh
usermod -aG docker deployer
```

- 🖥️ **O que você verá na tela:** Várias linhas de download e instalação passarão pela tela durante 1 a 2 minutos.
- ✅ **Como saber se deu certo:** Execute 'docker --version' e o terminal responderá 'Docker version 27.x.x' ou superior.

### Passo 4: Criação da Pasta do Nextcloud & Arquivo de Produção `[F01]`
Criamos o diretório /opt/nextcloud/ onde ficarão o banco de dados, os arquivos dos colaboradores e o arquivo que comanda os serviços.

> 💡 **Entenda com uma analogia:** Montar a escrivaninha e a gaveta onde as pastas serão arquivadas.

```bash
mkdir -p /opt/nextcloud/{data,letsencrypt}
chown -R deployer:deployer /opt/nextcloud
chmod -R 750 /opt/nextcloud
```

- 🖥️ **O que você verá na tela:** As pastas são criadas silenciosamente em menos de 1 segundo.
- ✅ **Como saber se deu certo:** O comando 'ls -ld /opt/nextcloud' mostrará a pasta pertencente ao usuário deployer.

### Passo 5: Subindo o Nextcloud com Docker Compose `[F02]`
Iniciamos o Nextcloud, o banco PostgreSQL e o proxy Traefik em segundo plano. O sistema baixa as imagens oficiais e começa a rodar imediatamente.

> 💡 **Entenda com uma analogia:** Apertar o botão verde no painel: as luzes acendem e os serviços operam.

```bash
cd /opt/nextcloud
docker compose up -d
docker compose ps
```

- 🖥️ **O que você verá na tela:** O Docker fará o download das camadas e exibirá 'Container nextcloud Started' e 'Container traefik Started'.
- ✅ **Como saber se deu certo:** Digite 'docker compose ps' e veja os três containers com status 'Up'.

### Passo 6: Configuração do Cadeado de Segurança (SSL) e Teste de Saúde `[F05]`
O Traefik emite automaticamente um certificado gratuito Let's Encrypt para mail.empresa.com.br, garantindo que ninguém intercepte seus e-mails e arquivos.

> 💡 **Entenda com uma analogia:** Lacre inviolável com assinatura digital em cada pacote que entra ou sai.

```bash
curl -s -o /dev/null -w "%{http_code}" https://mail.empresa.com.br | grep 200 || echo 'Aguarde 30s e tente novamente'
```

- 🖥️ **O que você verá na tela:** A resposta confirmará 'status: healthy' com o tempo de atividade registrado.
- ✅ **Como saber se deu certo:** Abra https://mail.empresa.com.br no navegador e veja o cadeado verde fechado na barra de endereços.

## Arquivos de Configuração de Produção

### `/opt/nextcloud/docker-compose.yml`
*Arquivo que define como o Nextcloud, o banco PostgreSQL e o proxy Traefik rodam isolados e como o Traefik expõe a ferramenta com cadeado SSL automático.*

```yaml
services:
  traefik:
    image: traefik:v3.0
    command:
      - "--providers.docker=true"
      - "--entrypoints.websecure.address=:443"
      - "--certificatesresolvers.le.acme.tlschallenge=true"
      - "--certificatesresolvers.le.acme.email=admin@empresa.com.br"
      - "--certificatesresolvers.le.acme.storage=/letsencrypt/acme.json"
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock:ro
      - ./letsencrypt:/letsencrypt
    networks:
      - nextcloud_net

  db:
    image: postgres:16-alpine
    environment:
      - POSTGRES_DB=nextcloud
      - POSTGRES_USER=nextcloud
      - POSTGRES_PASSWORD=SENHA_FORTE_BANCO_2026
    volumes:
      - db_data:/var/lib/postgresql/data
    networks:
      - nextcloud_net
    restart: unless-stopped

  nextcloud:
    image: nextcloud:latest
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.nextcloud.rule=Host(`mail.empresa.com.br`)"
      - "traefik.http.routers.nextcloud.entrypoints=websecure"
      - "traefik.http.routers.nextcloud.tls.certresolver=le"
      - "traefik.http.services.nextcloud.loadbalancer.server.port=80"
    volumes:
      - nextcloud_data:/var/www/html
    environment:
      - NEXTCLOUD_TRUSTED_DOMAINS=mail.empresa.com.br
      - POSTGRES_HOST=db
      - POSTGRES_DB=nextcloud
      - POSTGRES_USER=nextcloud
      - POSTGRES_PASSWORD=SENHA_FORTE_BANCO_2026
      - NEXTCLOUD_ADMIN_USER=admin
      - NEXTCLOUD_ADMIN_PASSWORD=SenhaAdminForte2026
    depends_on:
      - db
    networks:
      - nextcloud_net
    restart: unless-stopped

networks:
  nextcloud_net:
    driver: bridge

volumes:
  db_data:
  nextcloud_data:
  letsencrypt:
```

### `/opt/nextcloud/config/overwrite.config.php`
*Garante que o Nextcloud confie no proxy Traefik e force o protocolo HTTPS, evitando o aviso de 'Acesso não confiável'.*

```php
<?php
$CONFIG = array (
  'overwriteprotocol' => 'https',
  'overwritehost' => 'mail.empresa.com.br',
  'trusted_proxies' => array('traefik'),
  'forwarded_for_headers' => array('HTTP_X_FORWARDED_FOR'),
);
```

## Parte II: Manual de Uso Exaustivo

**Arquitetura Operacional:** O Nextcloud Hub funciona como um hub único: o módulo Mail recebe e envia e-mails (integrado ao servidor de e-mail Stalwart ou ao próprio servidor), o Calendar e o Contacts sincronizam com qualquer celular via CalDAV/CardDAV, e o Talk faz chamadas de vídeo no navegador via WebRTC. Tudo é armazenado no seu servidor PostgreSQL, sem cópia na nuvem do Google. Os aplicativos móveis oficiais (Android/iOS) e o cliente de desktop mantêm os arquivos sincronizados como o Google Drive.

### Roteiro de Primeiro Voo (Sua Primeira Reunião em 3 Minutos)

1. **Passo 1: Acessar o Painel e Criar o Administrador:** Abra https://mail.empresa.com.br no navegador, faça login com o usuário 'admin' definido na instalação e conclua o assistente de boas-vindas.
   - 🎯 **Resultado Esperado:** Você verá o painel com os ícones de Arquivos, Mail, Calendar, Contacts e Talk.

1. **Passo 2: Conectar seu Celular (CalDAV/CardDAV):** No celular, instale o app 'DAVx5' (Android) ou use Contas > CalDAV (iPhone) e aponte para https://mail.empresa.com.br com seu usuário e senha do Nextcloud.
   - 🎯 **Resultado Esperado:** Sua agenda e contatos do Nextcloud aparecem sincronizados no app nativo de calendário e contatos do telefone.

1. **Passo 3: Fazer sua Primeira Chamada de Vídeo no Talk:** Clique no ícone Talk, crie uma sala 'Reunião Equipe' e compartilhe o link com os colegas. Clique na câmera para iniciar a chamada.
   - 🎯 **Resultado Esperado:** A chamada de vídeo abre no navegador, sem instalar o Google Meet, com áudio e vídeo em tempo real.

### Dicionário Completo de Comandos (CLI)

| Comando / Flag | Descrição Técnica | Exemplo de Execução | Fonte |
| :--- | :--- | :--- | :---: |
| `sudo -u www-data php /var/www/html/occ user:add --display-name="João Silva" --group="colaboradores" joao` | Cria um novo colaborador no Nextcloud via linha de comando. | `sudo -u www-data php /var/www/html/occ user:add --display-name="João Silva" --group="colaboradores" joao` | `[F01]` |
| `sudo -u www-data php /var/www/html/occ app:enable talk` | Ativa o aplicativo de chat e vídeo Talk para toda a equipe. | `sudo -u www-data php /var/www/html/occ app:enable talk` | `[F02]` |
| `sudo -u www-data php /var/www/html/occ maintenance:mode --on` | Coloca o Nextcloud em modo de manutenção antes de um backup ou atualização. | `sudo -u www-data php /var/www/html/occ maintenance:mode --on` | `[F01]` |
| `sudo -u www-data php /var/www/html/occ files:scan --all` | Reconta os arquivos do disco para o banco de dados após um restore. | `sudo -u www-data php /var/www/html/occ files:scan --all` | `[F02]` |

### Endpoints de API REST & Integração Agêntica

| Método | Rota | Descrição | Fonte |
| :---: | :--- | :--- | :---: |
| **GET** | `/ocs/v2.php/cloud/users` | Lista todos os usuários cadastrados no Nextcloud. | `[F04]` |
| **POST** | `/ocs/v2.php/cloud/users` | Cria um novo usuário via API (usado pelo n8n no provisionamento). | `[F04]` |
| **GET** | `/ocs/v2.php/apps/files_sharing/api/v1/shares` | Lista os arquivos e pastas compartilhados com outros usuários ou grupos. | `[F01]` |

### Matriz de Resolução de Problemas (Troubleshooting)

- **⚠️ Sintoma:** Aparece a mensagem 'Acesso não confiável' ao abrir o site
  - **Causa:** O domínio não está na lista de domínios confiáveis do Nextcloud.
- **⚠️ Sintoma:** O Talk abre a chamada mas não transmite vídeo/áudio
  - **Causa:** Falta um servidor TURN ou as portas UDP de mídia não estão liberadas.
- **⚠️ Sintoma:** Erro de permissão ao enviar arquivos grandes
  - **Causa:** O limite de upload do PHP está baixo ou a pasta de dados tem dono errado.
## Parte III: Desinstalação Cirúrgica & Isolamento da VPS (Zero Efeito Colateral)

> 🛡️ **Princípio de Isolamento:** A desinstalação remove exclusivamente o container, o volume e o serviço do Nextcloud, preservando intactos o Docker, o Traefik, o PostgreSQL de outras aplicações e quaisquer projetos hospedados na VPS.

### Passo 1: Parada e Desativação do Serviço Dedicado no Systemd
Interrompe o processo do Nextcloud sem enviar sinal de encerramento para nenhum outro serviço da VPS.

```bash
sudo systemctl stop nextcloud.service
sudo systemctl disable nextcloud.service
```

- ⚠️ **Alerta de Segurança:** NÃO utilize 'systemctl stop docker' nem mate processos em lote. Apenas o serviço dedicado é desligado.
- ✅ **Como Validar:** `sudo systemctl is-active nextcloud # Retorna 'inactive'`

### Passo 2: Remoção Isolada de Contêiner e Volume de Dados
Remove cirurgicamente apenas o container nomeado e seu volume de arquivos dos colaboradores.

```bash
docker rm -f nextcloud 2>/dev/null || true
docker volume rm nextcloud_data 2>/dev/null || true
```

- ⚠️ **Alerta de Segurança:** JAMAIS execute 'docker system prune -a'. Isso apagaria contêineres e imagens de outros sistemas em produção.
- ✅ **Como Validar:** `docker ps -a --filter name=nextcloud # Retorna lista vazia`

### Passo 3: Revogação da Rota no Firewall e no Traefik
Remove exclusivamente a rota mail.empresa.com.br no Traefik sem interferir nas portas web (80/443) ou SSH (22).

```bash
rm -f /opt/nextcloud/docker-compose.yml
docker compose -f /opt/nextcloud/docker-compose.yml down 2>/dev/null || true
```

- ⚠️ **Alerta de Segurança:** Mantenha o Traefik ativo para as demais aplicações; remova apenas os labels do Nextcloud.
- ✅ **Como Validar:** `curl -s -o /dev/null -w "%{http_code}" https://mail.empresa.com.br # Não deve responder 200`

### Passo 4: Expurgo de Arquivos e Recarga do Systemd
Remove os arquivos de execução e recarrega as definições do systemd.

```bash
sudo rm -rf /opt/nextcloud
sudo systemctl daemon-reload
```

- ⚠️ **Alerta de Segurança:** Não execute 'apt autoremove' sem verificar os pacotes; a remoção é estritamente manual e isolada.
- ✅ **Como Validar:** `ls /opt/nextcloud # Não deve existir`

### Checklist de Saúde da VPS (Outros Projetos)

- [ ] `ss -tulpn | grep 443 # Confirma que o Traefik segue respondendo na porta 443`
- [ ] `docker ps # Confirma que contêineres de banco e outras apps continuam 'Up'`
- [ ] `free -h # Confirma devolução de memória RAM para o sistema operacional`

## Parte IV: Referências Bibliográficas Auditadas

| ID | Categoria | Título da Obra | Autor / Mantenedor | Link Oficial |
| :---: | :--- | :--- | :--- | :--- |
| **F01** | Documentação Oficial | Nextcloud Admin Manual & Installation Guide | Nextcloud GmbH (Core Team) | [https://docs.nextcloud.com](https://docs.nextcloud.com) |
| **F02** | Documentação Oficial | Nextcloud GitHub Official Repository & Docker Images | Nextcloud Open Source Community | [https://github.com/nextcloud/server](https://github.com/nextcloud/server) |
| **F03** | Imagem Docker Oficial | Nextcloud Docker Hub Image & Tags | Docker Official Images | [https://hub.docker.com/_/nextcloud](https://hub.docker.com/_/nextcloud) |
| **F04** | API & Integração | Nextcloud OCS API & User Provisioning | Nextcloud Developer Documentation | [https://docs.nextcloud.com/server/latest/developer_manual/client_apis/OCS/ocs-api-overview.html](https://docs.nextcloud.com/server/latest/developer_manual/client_apis/OCS/ocs-api-overview.html) |
| **F05** | Curso / Tutorial | Hardening de Servidor Ubuntu & Firewall UFW para Produção | Ubuntu Community & Canonical | [https://help.ubuntu.com/community/UFW](https://help.ubuntu.com/community/UFW) |
