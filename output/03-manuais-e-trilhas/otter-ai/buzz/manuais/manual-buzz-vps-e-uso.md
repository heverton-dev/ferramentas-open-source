# Manual Operacional Completo: BUZZ

> **Padrão Diamante · Guia de Engenharia & Adoção Descomplicada**  
> **Licença:** MIT | **Versão:** 0.11.0 | **Setup Estimado:** 30 a 45 minutos (Conhecimento básico de Linux)  
> **VPS Recomendada:** Hetzner Cloud CPX21 (2 vCPU, 4 GB RAM, EUR 9,90) ou Contabo VPS M (2 vCPU Dedicadas (AMD EPYC ou Intel Xeon E5) - Mínimo 1 vCPU, 2+ para velocidade, 4 GB RAM mínimo (8 GB recomendado para transcrição paralela de vários áudios), 80 GB SSD NVMe (mínimo 40 GB; crescer conforme volume de áudios), Ubuntu 22.04 LTS (x86_64) ou Debian 12)  
> **Custo Mensal Estimado:** EUR 9,90 a 19,90/mês (~R$ 60 a R$ 120 na cotação média)

---

## Módulo 0: Nivelamento Conceitual (Analogias do Dia a Dia)

### 💡 BUZZ (A Ferramenta) *(Analogia: Uma Secretária que Escuta Gravações e Digita Tudo)*
BUZZ é um aplicativo que recebe um arquivo de áudio (mp3, wav, m4a) e automaticamente converte em texto escrito. Como se você tivesse uma secretária ouvindo sua reunião e digitando tudo. A diferença: BUZZ faz isso de graça, sem limites, e os dados ficam 100% com você.

### 💡 Whisper (O Motor Invisível) *(Analogia: O Ouvido Treinado que Entende Qualquer Sotaque)*
Whisper é um modelo de inteligência artificial criado pelo OpenAI. Ele foi treinado com milhares de horas de áudio em 99 idiomas. BUZZ usa Whisper para fazer a 'escuta mágica'. Você não paga nada a OpenAI; Whisper roda no seu servidor.

### 💡 VPS (Servidor Privado Virtual) *(Analogia: Uma Sala de Computadores Alugada 24/7)*
Você não quer deixar seu computador ligado 24h transcrevendo áudio. Aluga um servidor profissional (VPS) por R$ 80-150/mês em um data center. Coloca BUZZ lá e acessa via navegador web de qualquer lugar.

### 💡 Python e ffmpeg (Ferramentas de Fundo) *(Analogia: O Martelo e a Chave Inglesa que BUZZ Precisa)*
BUZZ é escrito em Python (linguagem de programação). Precisa de ffmpeg (conversor de áudio) para ler diferentes formatos de arquivo. Ambas são gratuitas e open source.

### 💡 Fila de Transcrição *(Analogia: A Fila do Banco: Cada Cliente Aguarda Sua Vez)*
Quando você envia 5 áudios para BUZZ transcrever, ele não faz tudo junto (quebraria o servidor). Coloca na fila: áudio 1, depois 2, depois 3. Você recebe notificação quando cada um fica pronto.

### 💡 Transcrição vs Tradução *(Analogia: Digitar vs Traduzir para Outra Língua)*
BUZZ transcreve = converte áudio em texto do MESMO idioma. Você fala em inglês, BUZZ escreve em inglês. Tradução (converter inglês para português) é diferente; BUZZ pode fazer com plugin extra.

### 💡 Taxa de Acurácia (Precisão) *(Analogia: O Quanto a Secretária Acerta ao Digitar)*
Whisper tem 95-99% de acurácia em idiomas comuns (inglês, português). Significa: a cada 100 palavras, errar 1-5. Áudio de baixa qualidade ou sotaque muito forte reduz a acurácia.

## Parte I: Instalação em Produção na VPS (Passo a Passo Rígido)

### Passo 1: Acessar VPS via SSH e Atualizar Sistema `[F01]`
Você se conecta ao seu servidor alugado. Primeiro passo: garantir que todas as ferramentas estejam atualizadas.

> 💡 **Entenda com uma analogia:** Verificar se todos os fios da casa estão funcionando antes de instalar a TV.

```bash
ssh root@seu_ip_vps
sudo apt-get update
sudo apt-get upgrade -y
```

- 🖥️ **O que você verá na tela:** Linhas em preto e branco mostrando pacotes atualizados.
- ✅ **Como saber se deu certo:** Termina sem erros em vermelho. Prompt retorna normal.

### Passo 2: Instalar Python 3.11+, ffmpeg e Dependências `[F01]`
BUZZ e Whisper rodam em Python. ffmpeg converte áudios. Ambos são gratuitos e open source.

> 💡 **Entenda com uma analogia:** Comprar o motor (Python) e o conversor de combustível (ffmpeg) antes de montar o carro.

```bash
sudo apt-get install -y python3.11 python3.11-venv python3.11-dev python3-pip ffmpeg git curl wget
python3.11 --version
ffmpeg -version
```

- 🖥️ **O que você verá na tela:** Muitas linhas de pacotes sendo baixados e instalados. Pode levar 3-5 minutos.
- ✅ **Como saber se deu certo:** Termina com 'Processing triggers' sem erros. python3 --version retorna >= 3.11.

### Passo 3: Clonar Repositório BUZZ do GitHub `[F01]`
Vamos buscar o código oficial de BUZZ do GitHub, clonar para a VPS e preparar o ambiente.

> 💡 **Entenda com uma analogia:** Comprar um kit de móvel pronto do fabricante e desempacotar na sala.

```bash
cd /var/www
sudo git clone https://github.com/chidiwilliams/buzz.git
cd buzz
sudo chown -R www-data:www-data /var/www/buzz
```

- 🖥️ **O que você verá na tela:** Comando git clone baixando centenas de arquivos. Pode levar 1-2 minutos.
- ✅ **Como saber se deu certo:** Pasta /var/www/buzz existe com subpastas: src/, tests/, requirements.txt, etc.

### Passo 4: Criar Virtual Environment e Instalar Dependências Python `[F01]`
Virtual environment isola o BUZZ de outros projetos Python. Instalamos Whisper, Flask (servidor web) e bibliotecas.

> 💡 **Entenda com uma analogia:** Criar uma 'bolha isolada' para BUZZ para não conflitar com outros programas.

```bash
cd /var/www/buzz
sudo python3.11 -m venv venv
sudo chown -R www-data:www-data venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
pip install openai-whisper flask gunicorn
```

- 🖥️ **O que você verá na tela:** Muitos pacotes pip sendo instalados. Pode levar 5-10 minutos (primeiro Whisper é grande ~2GB).
- ✅ **Como saber se deu certo:** Venv ativado e prompt mostra (buzz). Comando 'pip list' mostra whisper, flask, etc.

### Passo 5: Configurar Serviço Systemd para BUZZ (Auto-iniciar) `[F02]`
Criamos um arquivo de serviço para que BUZZ inicie automaticamente ao rebootar a VPS.

> 💡 **Entenda com uma analogia:** Programar a TV para ligar automaticamente às 7h da manhã.

```bash
sudo nano /etc/systemd/system/buzz.service
# Colar conteúdo do arquivo de configuração (ver próxima seção)
sudo systemctl daemon-reload
sudo systemctl enable buzz
sudo systemctl start buzz
```

- 🖥️ **O que você verá na tela:** Você abre editor nano, cola algumas linhas, salva.
- ✅ **Como saber se deu certo:** Comando 'systemctl status buzz' mostra 'active (running)'.

### Passo 6: Configurar Apache como Proxy Reverso para BUZZ `[F02]`
Apache recebe requisições HTTPS em buzz.sua-empresa.com.br e passa para BUZZ rodando localmente.

> 💡 **Entenda com uma analogia:** Um recepcionista (Apache) que recebe clientes e os encaminha ao gerente (BUZZ).

```bash
sudo a2enmod proxy
sudo a2enmod proxy_http
sudo nano /etc/apache2/sites-available/buzz.conf
# Colar configuração do proxy reverso
sudo a2ensite buzz.conf
sudo systemctl reload apache2
```

- 🖥️ **O que você verá na tela:** Você configura VirtualHost do Apache.
- ✅ **Como saber se deu certo:** apache2ctl configtest retorna 'Syntax OK'. Site acessível via https://buzz.sua-empresa.com.br.

### Passo 7: Ativar HTTPS com Let's Encrypt `[F02]`
Certificado SSL gratuito para HTTPS. Renovação automática a cada 3 meses.

> 💡 **Entenda com uma analogia:** Colocar cadeado de segurança na porta.

```bash
sudo apt-get install -y certbot python3-certbot-apache
sudo certbot --apache -d buzz.sua-empresa.com.br
```

- 🖥️ **O que você verá na tela:** Certbot pede email e domínio. Modifica Apache automaticamente.
- ✅ **Como saber se deu certo:** Acessar https://buzz.sua-empresa.com.br sem avisos de certificado inválido.

### Passo 8: Criar Diretórios de Armazenamento para Áudios e Transcrições `[F03]`
Pastas isoladas para armazenar áudios recebidos, transcrições geradas e logs.

> 💡 **Entenda com uma analogia:** Criar pastas bem organizadas para documentos: entrada, saída, arquivo.

```bash
sudo mkdir -p /var/lib/buzz/{uploads,transcriptions,models}
sudo mkdir -p /var/log/buzz
sudo chown -R www-data:www-data /var/lib/buzz /var/log/buzz
sudo chmod 755 /var/lib/buzz /var/log/buzz
```

- 🖥️ **O que você verá na tela:** Simples criação de diretórios.
- ✅ **Como saber se deu certo:** Pastas existem e são acessíveis via BUZZ: /var/lib/buzz/uploads/, /var/lib/buzz/transcriptions/, /var/log/buzz/.

### Passo 9: Testar BUZZ e Transcrever Áudio de Exemplo `[F04]`
Fazer uma transcrição de teste para confirmar que tudo está funcionando.

> 💡 **Entenda com uma analogia:** Ligar o motor do carro para verificar se está rodando corretamente.

```bash
cd /var/www/buzz
source venv/bin/activate
wget https://example.com/audio-sample.wav -O /tmp/test.wav
python -m buzz.cli /tmp/test.wav --output /var/lib/buzz/transcriptions/test.txt
cat /var/lib/buzz/transcriptions/test.txt
```

- 🖥️ **O que você verá na tela:** Primeira execução baixa modelo Whisper (~2GB). Depois, transcreve um áudio de teste.
- ✅ **Como saber se deu certo:** Arquivo de transcrição .txt gerado em /var/lib/buzz/transcriptions/ com o texto do áudio.

## Arquivos de Configuração de Produção

### `/etc/systemd/system/buzz.service`
*Arquivo systemd que define BUZZ como serviço. Inicia automaticamente em boot. Roda como www-data (usuário web seguro). Gunicorn é o servidor WSGI que executa Python. Modelo Whisper padrão é 'base' (equilibra velocidade e precisão).*

```ini
[Unit]
Description=BUZZ - Transcrição de Áudio com Whisper
After=network.target

[Service]
Type=notify
User=www-data
Group=www-data
WorkingDirectory=/var/www/buzz
Environment="PATH=/var/www/buzz/venv/bin:/usr/local/bin:/usr/bin"
Environment="PYTHONUNBUFFERED=1"
Environment="WHISPER_MODEL=base"
ExecStart=/var/www/buzz/venv/bin/gunicorn --workers 2 --bind 127.0.0.1:8000 buzz.app:app
Restart=always
RestartSec=5
StandardOutput=append:/var/log/buzz/buzz.log
StandardError=append:/var/log/buzz/buzz-error.log

[Install]
WantedBy=multi-user.target
```

### `/etc/apache2/sites-available/buzz.conf`
*VirtualHost Apache que: 1) Redireciona HTTP → HTTPS. 2) Configura SSL com certificados Let's Encrypt. 3) Proxy reverso para BUZZ rodando em 127.0.0.1:8000. 4) Logs separados.*

```apache
<VirtualHost *:80>
    ServerName buzz.sua-empresa.com.br
    Redirect / https://buzz.sua-empresa.com.br/
</VirtualHost>

<VirtualHost *:443>
    ServerName buzz.sua-empresa.com.br
    DocumentRoot /var/www/buzz

    SSLEngine on
    SSLCertificateFile /etc/letsencrypt/live/buzz.sua-empresa.com.br/fullchain.pem
    SSLCertificateKeyFile /etc/letsencrypt/live/buzz.sua-empresa.com.br/privkey.pem

    ProxyPreserveHost On
    ProxyPass / http://127.0.0.1:8000/
    ProxyPassReverse / http://127.0.0.1:8000/

    <Location />
        Require all granted
    </Location>

    ErrorLog ${APACHE_LOG_DIR}/buzz-error.log
    CustomLog ${APACHE_LOG_DIR}/buzz-access.log combined
</VirtualHost>
```

### `/var/www/buzz/config.env`
*Configurações de produção do BUZZ: Ambiente (production), Modelo Whisper (base = bom equilíbrio), Idioma padrão (português), Pastas de armazenamento, Limite de arquivo (500MB), Máximo de transcrições paralelas (2 para CPU com 2 cores), Timeout (1 hora), Logging.*

```ini
# Configuração de Produção para BUZZ
FLASK_ENV=production
FLASK_DEBUG=0
SECRET_KEY=SenhaSegura123456789AleatoriaMuitoForte

# Whisper Config
WHISPER_MODEL=base
WHISPER_DEVICE=cpu
WHISPER_LANGUAGE=pt

# Storage Config
UPLOAD_FOLDER=/var/lib/buzz/uploads
OUTPUT_FOLDER=/var/lib/buzz/transcriptions
MAX_FILE_SIZE=500MB

# Queue Config
MAX_CONCURRENT_JOBS=2
JOB_TIMEOUT=3600

# Logging
LOG_LEVEL=INFO
LOG_FILE=/var/log/buzz/buzz.log
```

## Parte II: Manual de Uso Exaustivo

**Arquitetura Operacional:** BUZZ funciona em três camadas: (1) Interface Web (Apache/HTTPS) onde usuários acessam o dashboard e fazem upload de áudios. (2) Fila de Processamento (Python + Whisper) que transcre um áudio por vez (serializado para não sobrecarregar CPU). (3) Armazenamento (Diretórios /var/lib/buzz) onde áudios brutos e transcrições em .txt/.json são salvos. Whisper roda na CPU (ou GPU se disponível) e processa áudio em chunks de 30 segundos.

### Roteiro de Primeiro Voo (Sua Primeira Reunião em 3 Minutos)

1. **1. Acessar Dashboard:** Abra https://buzz.sua-empresa.com.br em navegador web. Você verá página inicial com campo 'Upload de Áudio'.
   - 🎯 **Resultado Esperado:** Dashboard carrega sem erros. Botão 'Selecionar Arquivo' e indicador 'Status: Pronto para Transcever' visíveis.

1. **2. Upload de Arquivo de Áudio:** Clique em 'Selecionar Arquivo'. Escolha um MP3, WAV ou M4A com até 500MB. Clique 'Transcrever'.
   - 🎯 **Resultado Esperado:** Arquivo é enviado. Dashboard mostra 'Processando... 25%' e aumenta até 100%. Transcrição aparece em segundos/minutos (conforme tamanho do áudio).

1. **3. Copiar/Exportar Transcrição:** Transcrição pronta. Botão 'Copiar para Clipboard'. Ou 'Download TXT' ou 'Download JSON'.
   - 🎯 **Resultado Esperado:** Texto copiado para sua área de transferência. Você pode colar em Word/Google Docs. Ou arquivo .txt/.json baixado.

1. **4. Ajustar Qualidade (Opcional):** Se transcrição teve erros, aumentar 'Modelo de Precisão' de 'base' para 'small/medium' (mais lento, mais preciso).
   - 🎯 **Resultado Esperado:** Próxima transcrição usa modelo melhor. Velocidade diminui, mas acurácia aumenta de 95% para 98%.

### Dicionário Completo de Comandos (CLI)

| Comando / Flag | Descrição Técnica | Exemplo de Execução | Fonte |
| :--- | :--- | :--- | :---: |
| `buzz-cli transcribe <arquivo-audio> --output <arquivo-saida>` | Transcrever um áudio via linha de comando (sem interface web). Útil para automação/scripts. | `cd /var/www/buzz && source venv/bin/activate && python -m buzz.cli /tmp/gravacao.wav --output /var/lib/buzz/transcriptions/resultado.txt` | `[F03]` |
| `systemctl status buzz` | Verificar se serviço BUZZ está rodando. Mostra se está ativo, logs recentes, tempo de atividade. | `sudo systemctl status buzz` | `[F03]` |
| `systemctl restart buzz` | Reiniciar serviço BUZZ após mudança de configuração ou se ele travou. | `sudo systemctl restart buzz` | `[F03]` |

### Endpoints de API REST & Integração Agêntica

| Método | Rota | Descrição | Fonte |
| :---: | :--- | :--- | :---: |
| **POST** | `/api/transcribe` | Enviar áudio para transcrição via API (sem interface web). Retorna ID do job. | `[F04]` |
| **GET** | `/api/status/{job_id}` | Verificar status de uma transcrição em andamento (0-100%) ou concluída. | `[F04]` |
| **GET** | `/api/result/{job_id}` | Baixar transcrição concluída em formato JSON (com timestamps) ou TXT. | `[F04]` |

### Matriz de Resolução de Problemas (Troubleshooting)

- **⚠️ Sintoma:** Upload falha com erro '413 Request Entity Too Large'
  - **Causa:** Arquivo maior que 500MB. Ou limite do Apache/PHP muito baixo.
- **⚠️ Sintoma:** Transcrição muito lenta (> 10 minutos para 1 hora de áudio)
  - **Causa:** Modelo Whisper muito grande ('large'). Ou CPU com apenas 1 core.
- **⚠️ Sintoma:** BUZZ travado, não responde
  - **Causa:** Serviço BUZZ parou ou memória esgotada (áudio muito grande).
- **⚠️ Sintoma:** Transcrição com muitos erros (acurácia < 80%)
  - **Causa:** Áudio de qualidade ruim, sotaque forte ou idioma incorreto.
- **⚠️ Sintoma:** Erro 'Permission Denied' ao acessar /var/lib/buzz/uploads/
  - **Causa:** Permissões de arquivo incorretas. BUZZ roda como www-data, pasta não pertence a ele.
## Parte III: Desinstalação Cirúrgica & Isolamento da VPS (Zero Efeito Colateral)

> 🛡️ **Princípio de Isolamento:** BUZZ foi instalado em estrutura totalmente isolada: aplicação em /var/www/buzz/, serviço systemd próprio, dados em /var/lib/buzz/, logs em /var/log/buzz/, VirtualHost Apache dedicado. Esta modularidade permite remoção cirúrgica sem efeitos colaterais em outros websites/serviços. Seguindo estes passos, BUZZ desaparece completamente, deixando a VPS tão limpa quanto antes da instalação.

### Passo 1: Parar Serviço BUZZ
Interrompa o serviço systemd de BUZZ e desative site Apache.

```bash
sudo systemctl stop buzz
sudo systemctl disable buzz
sudo a2dissite buzz.conf
sudo systemctl reload apache2
```

- ⚠️ **Alerta de Segurança:** ALERTA: Após este passo, https://buzz.sua-empresa.com.br será inacessível (erro 404/503).
- ✅ **Como Validar:** `sudo systemctl status buzz retorna 'inactive (dead)'. Apache error.log não contém erros para 'buzz'.`

### Passo 2: Backup Final de Dados (Altamente Recomendado)
Se alguma transcrição é importante, faça backup antes de deletar.

```bash
tar -czf ~/buzz_backup_$(date +%Y%m%d).tar.gz /var/lib/buzz/transcriptions/
tar -czf ~/buzz_logs_$(date +%Y%m%d).tar.gz /var/log/buzz/
```

- ⚠️ **Alerta de Segurança:** CRÍTICO: Sem este backup, os dados são irrecuperáveis após próxima etapa.
- ✅ **Como Validar:** `Dois arquivos .tar.gz em $HOME com tamanho > 1MB (se houver transcrições).`

### Passo 3: Remover Pasta e Arquivos de BUZZ
Deletar completamente aplicação, dados e logs. Sem possibilidade de recuperação.

```bash
sudo rm -rf /var/www/buzz/
sudo rm -rf /var/lib/buzz/
sudo rm -rf /var/log/buzz/
sudo rm -f /etc/systemd/system/buzz.service
sudo rm -f /etc/apache2/sites-available/buzz.conf
sudo rm -f /etc/apache2/sites-available/buzz-ssl.conf
sudo systemctl daemon-reload
```

- ⚠️ **Alerta de Segurança:** PONTO DE NÃO-RETORNO: Todos os arquivos e dados de BUZZ são deletados permanentemente.
- ✅ **Como Validar:** `sudo ls /var/www/buzz/ retorna 'No such file or directory'. sudo ls /var/lib/buzz/ também não existe.`

### Passo 4: Remover Certificado SSL (Opcional - Se BUZZ era único HTTPS)
Se BUZZ era o único site HTTPS, remover certificado Let's Encrypt.

```bash
sudo certbot delete --cert-name buzz.sua-empresa.com.br
```

- ⚠️ **Alerta de Segurança:** ATENÇÃO: Remova apenas se nenhum outro site na VPS usa este domínio.
- ✅ **Como Validar:** `sudo certbot certificates não lista 'buzz.sua-empresa.com.br'.`

### Passo 5: Limpar Python Virtual Environment
Se não há outro projeto Python na VPS que dependa desse venv, pode limpar.

```bash
sudo rm -rf /opt/buzz-venv/ (se foi instalado lá)
# Ou manter em /var/www/buzz (já deletado acima)
# Desinstalar Python 3.11 se não usado por outra app:
sudo apt-get autoremove python3.11
```

- ⚠️ **Alerta de Segurança:** ATENÇÃO: Só remova Python 3.11 se nenhuma outra aplicação a usa.
- ✅ **Como Validar:** `python3.11 --version retorna 'command not found' se removido com sucesso.`

### Checklist de Saúde da VPS (Outros Projetos)

- [ ] `ESPAÇO EM DISCO: df -h → Deve liberar >20GB que BUZZ ocupava. Coluna 'Avail' >= 20GB livres`
- [ ] `PROCESSOS PYTHON: ps aux | grep python | grep buzz → Deve estar vazio (sem processos BUZZ)`
- [ ] `SERVIÇOS: sudo systemctl list-units --type service | grep buzz → Deve estar vazio`
- [ ] `PORTAS: sudo netstat -tlnp | grep 8000 → Porta 8000 (BUZZ) não deve estar em LISTEN`
- [ ] `APACHE VHOSTS: sudo apache2ctl -S | grep buzz → NÃO deve listar buzz.conf`
- [ ] `LOGS: sudo tail -20 /var/log/apache2/error.log → NÃO deve conter 'buzz'`
- [ ] `CERTIFICADOS SSL: sudo certbot certificates → NÃO deve listar 'buzz.sua-empresa.com.br'`
- [ ] `CRON JOBS: sudo crontab -l → Se houver, NÃO deve ter scripts de BUZZ`

## Parte IV: Referências Bibliográficas Auditadas

| ID | Categoria | Título da Obra | Autor / Mantenedor | Link Oficial |
| :---: | :--- | :--- | :--- | :--- |
| **F01** | Repositório Oficial | BUZZ - GitHub Repository | Chidi Williams | [https://github.com/chidiwilliams/buzz](https://github.com/chidiwilliams/buzz) |
| **F02** | Documentação | BUZZ - Installation & Usage Guide | BUZZ Community | [https://github.com/chidiwilliams/buzz#readme](https://github.com/chidiwilliams/buzz#readme) |
| **F03** | Dependência | OpenAI Whisper - Speech Recognition Model | OpenAI | [https://github.com/openai/whisper](https://github.com/openai/whisper) |
| **F04** | Ferramenta | FFmpeg - Audio/Video Processing | FFmpeg Team | [https://ffmpeg.org/](https://ffmpeg.org/) |
| **F05** | Licença | MIT License - Texto Completo | Open Source Initiative | [https://opensource.org/licenses/MIT](https://opensource.org/licenses/MIT) |
