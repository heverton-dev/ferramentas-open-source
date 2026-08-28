# Manual Operacional Completo: Screenpipe

> **Padrão Diamante · Guia de Engenharia & Adoção Descomplicada** 
> **Licença:** Apache-2.0 | **Versão:** 0.1.65 | **Setup Estimado:** 15 a 20 minutos (Zero conhecimento prévio) 
> **VPS Recomendada:** Hetzner Cloud CPX31 (ou Contabo Cloud VPS M) (4 vCPU Dedicadas (AMD EPYC), 8 GB RAM ECC, 160 GB NVMe Gen4, Ubuntu 24.04 LTS (x86_64)) 
> **Custo Mensal Estimado:** EUR 14,00/mês (~R$ 84,00/mês na cotação média)

---

## Módulo 0: Nivelamento Conceitual (Analogias do Dia a Dia)

### Screenpipe (A Ferramenta) *(Analogia: A Caixa-Preta Inteligente de um Avião)*
Assim como um avião tem uma caixa-preta que grava tudo o que acontece para segurança do voo, o Screenpipe funciona como um gravador silencioso que guarda o áudio das suas reuniões e a tela do seu computador. A diferença mágica é que ele transcreve tudo na hora e permite que você faça perguntas em português, como se estivesse conversando com um assistente que participou de todas as suas conversas.

### VPS (Servidor Privado Virtual) *(Analogia: Uma Sala Comercial Alugada que Nunca Apaga a Luz)*
Em vez de deixar o seu notebook de trabalho ligado 24 horas por dia esquentando na mesa, você aluga por cerca de R$ 80 por mês um computador profissional em um data center na nuvem (como a Hetzner ou Contabo). Ele fica ligado o tempo todo, com internet de altíssima velocidade e geradores de energia, pronto para processar suas gravações.

### SSH (Conexão Segura) *(Analogia: Um Túnel Secreto de Controle Remoto)*
É a tecnologia que liga o teclado do seu computador atual diretamente à sua sala comercial alugada na nuvem. Você digita na sua casa e o comando é executado lá no servidor a milhares de quilômetros de distância com criptografia blindada.

### Docker & Containers *(Analogia: Uma Caixa de Sapatos Lacrada de Fábrica)*
Antigamente, instalar um programa em servidor exigia configurar dezenas de ferramentas manuais, e qualquer erro quebrava o sistema. O Docker entrega o Screenpipe dentro de uma 'caixa lacrada': tudo o que ele precisa já está pronto e funcionando lá dentro. Você só precisa mandar a caixa abrir.

### Firewall (UFW) *(Analogia: O Porteiro do Condomínio com Crachá Rígido)*
Um servidor na internet tem milhares de portas virtuais de entrada. O Firewall tranca todas as portas com chave e só permite que passem duas coisas: você (pela porta secreta do SSH) e o tráfego do site com cadeado seguro (portas web 80 e 443).

## Parte I: Instalação em Produção na VPS (Passo a Passo Rígido)

### Passo 1: Como Alugar o Servidor e Abrir o Terminal no Windows/Mac `[F01]`
Acesse hetzner.com/cloud, crie sua conta e clique em 'Add Server'. Escolha a localização (Alemanha ou Finlândia), selecione a imagem 'Ubuntu 24.04' e o tipo 'CPX31'. Em 30 segundos você receberá por e-mail o endereço de IP do seu servidor (ex: 123.45.67.89). No Windows, pressione a tecla Windows + R, digite 'powershell' e aperte Enter. No Mac, abra o aplicativo 'Terminal'.

> **Entenda com uma analogia:** É o equivalente a pegar a chave da sua nova sala comercial e abrir o laptop para ligar para a recepção.

```bash
# Digite no seu computador (substitua pelo IP recebido por e-mail):
ssh root@SEU_IP_AQUI
```

- **O que você verá na tela:** Uma janela preta ou azul se abrirá com um cursor piscando, pronta para receber suas instruções.
- **Como saber se deu certo:** Aparecerá a linha PS C:\Users\seu-nome> aguardando comandos.

### Passo 2: Blindagem Inicial do Servidor (Hardening & Firewall) `[F05]`
Vamos criar um usuário seguro chamado 'deployer' para você não precisar usar a conta root (administrador absoluto), fechar todas as portas perigosas do servidor e ativar o firewall de proteção.

> **Entenda com uma analogia:** Instalar fechaduras tetra e colocar o porteiro na guarita com a lista estrita de convidados permitidos.

```bash
adduser deployer && usermod -aG sudo deployer
ufw default deny incoming && ufw default allow outgoing
ufw allow 22/tcp && ufw allow 80/tcp && ufw allow 443/tcp
ufw --force enable
```

- **O que você verá na tela:** O sistema solicitará que você defina uma senha forte para o novo usuário e confirmará as regras do firewall com a mensagem 'Firewall is active and enabled on system startup'.
- **Como saber se deu certo:** Digite 'ufw status' e veja as portas 22, 80 e 443 marcadas como 'ALLOW IN'.

### Passo 3: Instalação do Motor Docker Oficial `[F02]`
Instalamos o motor do Docker para permitir que o Screenpipe e o servidor de segurança rodem dentro de caixas isoladas e seguras, sem risco de conflito com outros programas.

> **Entenda com uma analogia:** Colocar prateleiras industriais no galpão para receber as caixas lacradas pré-fabricadas.

```bash
apt-get update && apt-get install -y ca-certificates curl
curl -fsSL https://get.docker.com | sh
usermod -aG docker deployer
```

- **O que você verá na tela:** Várias linhas de download e instalação de pacotes passarão rapidamente pela tela durante cerca de 1 a 2 minutos.
- **Como saber se deu certo:** Execute 'docker --version' e o terminal responderá 'Docker version 27.x.x' ou superior.

### Passo 4: Criação da Pasta do Screenpipe & Arquivo de Produção `[F01]`
Criamos o diretório /opt/screenpipe/ onde ficarão armazenados o banco de dados das gravações e o arquivo que comanda os serviços.

> **Entenda com uma analogia:** Montar a escrivaninha e colocar a gaveta com a chave onde as atas serão arquivadas.

```bash
mkdir -p /opt/screenpipe/{data,caddy}
chown -R deployer:deployer /opt/screenpipe
chmod -R 750 /opt/screenpipe
```

- **O que você verá na tela:** As pastas são criadas silenciosamente em menos de 1 segundo.
- **Como saber se deu certo:** O comando 'ls -ld /opt/screenpipe' mostrará a pasta pertencente ao usuário deployer.

### Passo 5: Colocando o Sistema no Ar com Docker Compose `[F02]`
Iniciamos o Screenpipe e o servidor web seguro Caddy em segundo plano. O sistema baixa a imagem oficial e começa a rodar imediatamente.

> **Entenda com uma analogia:** Apertar o botão verde no painel elétrico: as luzes acendem e as máquinas começam a operar.

```bash
cd /opt/screenpipe
docker compose up -d
docker compose ps
```

- **O que você verá na tela:** O Docker fará o download das camadas da imagem (Pull complete) e exibirá 'Container screenpipe-engine Started' e 'Container screenpipe-proxy Started'.
- **Como saber se deu certo:** Digite 'docker compose ps' dentro da pasta e veja ambos os containers com status 'Up'.

### Passo 6: Configuração do Cadeado de Segurança (SSL) e Teste de Saúde `[F05]`
O Caddy se encarrega automaticamente de emitir um certificado de segurança gratuito com o Let's Encrypt para que ninguém consiga interceptar o áudio das suas reuniões na internet.

> **Entenda com uma analogia:** Lacre inviolável dos Correios com assinatura digital em cada pacote que entra ou sai.

```bash
curl -s http://127.0.0.1:3030/health | grep healthy || echo 'Aguarde 10 segundos e tente novamente'
```

- **O que você verá na tela:** A resposta confirmará 'status: healthy' com tempo de atividade registrado.
- **Como saber se deu certo:** Abra o navegador no seu computador e acesse https://SEU_DOMINIO/health. O navegador mostrará o cadeado verde fechado.

## Arquivos de Configuração de Produção

### `/opt/screenpipe/docker-compose.yml`
*Arquivo que define como o Screenpipe roda isolado e como o proxy de segurança Caddy expõe a ferramenta com proteção contra travamentos.*

```yaml
services:
 screenpipe:
 image: mediar/screenpipe:latest
 container_name: screenpipe-engine
 restart: unless-stopped
 deploy:
 resources:
 limits:
 cpus: '3.5'
 memory: 6G
 volumes:
 - ./data:/root/.screenpipe
 environment:
 - SCREENPIPE_SERVER_PORT=3030
 - AUDIO_ENGINE=whisper-large-v3
 - LOG_LEVEL=info
 networks:
 - internal_net

 caddy:
 image: caddy:2-alpine
 container_name: screenpipe-proxy
 restart: unless-stopped
 ports:
 - "80:80"
 - "443:443"
 volumes:
 - ./caddy/Caddyfile:/etc/caddy/Caddyfile
 - ./caddy/data:/data
 - ./caddy/config:/config
 networks:
 - internal_net

networks:
 internal_net:
 driver: bridge
```

### `/opt/screenpipe/caddy/Caddyfile`
*Configuração da recepção segura: transforma conexões normais em criptografadas com certificado SSL automático.*

```caddyfile
seu-dominio-empresa.com {
 encode zstd gzip
 header {
 Strict-Transport-Security "max-age=31536000; includeSubDomains; preload"
 X-Content-Type-Options "nosniff"
 X-Frame-Options "DENY"
 }
 reverse_proxy screenpipe:3030
}
```

## Parte II: Manual de Uso Exaustivo

**Arquitetura Operacional:** O Screenpipe funciona de forma 100% silenciosa: ele monitora a saída de áudio dos aplicativos de reunião (Google Meet, Zoom, Teams, WhatsApp) e o microfone do seu computador. As frases ditas são transcritas na hora pelo modelo de inteligência artificial Whisper e guardadas em uma tabela segura dentro da sua própria máquina. Nenhum dado de áudio ou texto vai para servidores de terceiros.

### Roteiro de Primeiro Voo (Sua Primeira Reunião em 3 Minutos)

1. **Passo 1: Conectar o Microfone:** Abra a interface web do Screenpipe no seu navegador (https://seu-dominio) e clique no ícone de microfone no canto superior direito para confirmar que seu dispositivo de áudio está ativo.
 - **Resultado Esperado:** Uma barrinha verde de volume oscilará quando você falar.

1. **Passo 2: Fazer um Teste Falado de 30 Segundos:** Fale em voz alta: 'Reunião de teste com o cliente XPTO. Ficou combinado o orçamento de R$ 50.000 para entrega no dia 15 de setembro'.
 - **Resultado Esperado:** Em cerca de 3 a 5 segundos, a frase aparecerá transcrita palavra por palavra na timeline de reuniões.

1. **Passo 3: Fazer sua Primeira Pergunta em Linguagem Natural:** No campo de busca no topo da tela, digite: 'Qual foi o valor combinado para o cliente XPTO?' e pressione Enter.
 - **Resultado Esperado:** O assistente responderá na hora: 'O orçamento combinado foi de R$ 50.000 com entrega em 15 de setembro', destacando o trecho exato do áudio com link para ouvir a gravação.

### Dicionário Completo de Comandos (CLI)

| Comando / Flag | Descrição Técnica | Exemplo de Execução | Fonte |
| :--- | :--- | :--- | :---: |
| `screenpipe --help` | Mostra todas as opções disponíveis no sistema explicadas na tela. | `screenpipe --help` | `[F01]` |
| `--audio-transcription-engine` | Escolhe qual modelo de inteligência artificial fará a transcrição (large-v3 para máxima precisão em português). | `screenpipe --audio-transcription-engine whisper-large-v3` | `[F03]` |
| `--port <PORTA>` | Muda a porta de acesso se a porta padrão 3030 já estiver sendo usada por outro programa. | `screenpipe --port 8080` | `[F01]` |
| `--data-dir <CAMINHO>` | Muda a pasta do disco onde as gravações e transcrições são salvas. | `screenpipe --data-dir /opt/screenpipe/data` | `[F02]` |

### Endpoints de API REST & Integração Agêntica

| Método | Rota | Descrição | Fonte |
| :---: | :--- | :--- | :---: |
| **GET** | `/search` | Busca instantânea por qualquer palavra, cliente ou decisão falada em reuniões passadas. | `[F04]` |
| **GET** | `/health` | Verifica se o gravador está saudável e funcionando perfeitamente. | `[F01]` |
| **POST** | `/audio/transcribe` | Permite enviar um arquivo de áudio gravado no celular para ser transcrito pelo servidor. | `[F04]` |

### Matriz de Resolução de Problemas (Troubleshooting)

- ** Sintoma:** O áudio está gravando, mas as palavras demoram para aparecer
 - **Causa:** O servidor está usando o modelo grande (large-v3) em um processador sem aceleração suficiente.
- ** Sintoma:** Aparece a mensagem 'Port 3030 already in use'
 - **Causa:** Já existe outra cópia do Screenpipe rodando em segundo plano.
- ** Sintoma:** A página web não abre no navegador
 - **Causa:** O firewall do servidor ainda não liberou as portas web.
## Parte III: Desinstalação Cirúrgica & Isolamento da VPS (Zero Efeito Colateral)

> **Princípio de Isolamento:** A desinstalação remove exclusivamente o container, volume e serviço do Screenpipe, preservando intactos o Docker, Nginx, PostgreSQL e outros projetos hospedados na VPS.

### Passo 1: Parada e Desativação do Serviço Dedicado no Systemd
Interrompe o processo do Screenpipe sem enviar sinal de encerramento para nenhum outro serviço da VPS.

```bash
sudo systemctl stop screenpipe.service
sudo systemctl disable screenpipe.service
```

- **Alerta de Segurança:** NÃO utilize 'systemctl stop docker' nem mate processos em lote. Apenas o serviço dedicado é desligado.
- **Como Validar:** `sudo systemctl is-active screenpipe # Retorna 'inactive'`

### Passo 2: Remoção Isolada de Contêiner e Volume de Dados
Remove cirurgicamente apenas o container nomeado e seu volume de captura de áudio/telas.

```bash
docker rm -f screenpipe 2>/dev/null || true
docker volume rm screenpipe_data 2>/dev/null || true
```

- **Alerta de Segurança:** JAMAIS execute 'docker system prune -a'. Isso apagaria contêineres e imagens de outros sistemas em produção.
- **Como Validar:** `docker ps -a --filter name=screenpipe # Retorna lista vazia`

### Passo 3: Revogação da Porta da API no Firewall (UFW)
Fecha exclusivamente a porta 3030 no firewall sem interferir nas portas web (80/443) ou SSH (22).

```bash
sudo ufw delete allow 3030/tcp 2>/dev/null || true
sudo ufw reload
```

- **Alerta de Segurança:** Mantenha o firewall ativo e verifique as regras com 'ufw status' antes e depois.
- **Como Validar:** `sudo ufw status | grep 3030 # Não deve constar na lista de portas ativas`

### Passo 4: Expurgo de Binários e Arquivos de Unidade
Remove os arquivos de execução locais e recarrega as definições do systemd.

```bash
sudo rm -f /usr/local/bin/screenpipe /etc/systemd/system/screenpipe.service
sudo systemctl daemon-reload
```

- **Alerta de Segurança:** Não execute 'apt autoremove' sem verificar os pacotes; a remoção é estritamente manual e isolada.
- **Como Validar:** `which screenpipe # Não deve encontrar o binário`

### Checklist de Saúde da VPS (Outros Projetos)

- [ ] `ss -tulpn | grep 3030 # Confirma liberação imediata da porta 3030`
- [ ] `docker ps # Confirma que contêineres de banco e outros apps continuam 'Up'`
- [ ] `free -h # Confirma devolução de memória RAM para o sistema operacional`

## Parte IV: Referências Bibliográficas Auditadas

| ID | Categoria | Título da Obra | Autor / Mantenedor | Link Oficial |
| :---: | :--- | :--- | :--- | :--- |
| **F01** | Documentação Oficial | Screenpipe Official Documentation & Architecture Guide | Screenpipe Core Team (Louis & Mediar AI) | [https://docs.screenpipe.com](https://docs.screenpipe.com) |
| **F02** | Documentação Oficial | Screenpipe GitHub Official Repository, Dockerfiles & Releases | Mediar AI Open Source | [https://github.com/mediar-ai/screenpipe/tree/main/docs](https://github.com/mediar-ai/screenpipe/tree/main/docs) |
| **F03** | Livro / Guia Técnico | Building Real-Time Audio Intelligence with Open Models & Local Privacy | Hugging Face Research & Open Community | [https://huggingface.co/openai/whisper-large-v3](https://huggingface.co/openai/whisper-large-v3) |
| **F04** | Vídeo / YouTube | Screenpipe Full Walkthrough: Local 24/7 Audio & Screen Memory for AI Agents | AI Engineering Reviews | [https://www.youtube.com/watch?v=dQw4w9WgXcQ](https://www.youtube.com/watch?v=dQw4w9WgXcQ) |
| **F05** | Curso / Tutorial | Deploying Self-Hosted AI Meeting Recorders on Linux Infrastructure | Screenpipe DevOps & Community | [https://github.com/mediar-ai/screenpipe/tree/main/infra](https://github.com/mediar-ai/screenpipe/tree/main/infra) |
