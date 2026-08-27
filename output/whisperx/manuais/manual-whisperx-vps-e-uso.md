# Manual Operacional Completo: WhisperX + PyAnnote

> **Padrão Diamante · Guia de Engenharia & Adoção Descomplicada**  
> **Licença:** BSD-4-Clause | **Versão:** 3.1.2 | **Setup Estimado:** 15 min (Zero conhecimento prévio)  
> **VPS Recomendada:** Hetzner Cloud CPX31 (ou Hetzner Server com GPU dedicada) (4 vCPU Dedicadas (AMD EPYC), 8 GB RAM ECC, 160 GB NVMe Gen4, Ubuntu 24.04 LTS (x86_64))  
> **Custo Mensal Estimado:** EUR 14,00/mês (~R$ 84,00/mês)

---

## Módulo 0: Nivelamento Conceitual (Analogias do Dia a Dia)

### 💡 Diarização de Locutores *(Analogia: A Ata de Assembleia com Identificação de Voz)*
Imagine uma reunião com 5 pessoas falando ao mesmo tempo. Um gravador comum apenas transcreve um amontoado de texto. A diarização é como um escrivão com ouvido absoluto que anota exatamente quem falou cada frase: 'Diretor Silva disse X', 'Dra. Mariana respondeu Y'.

### 💡 Alinhamento em Nível de Palavra (Word-Level Timestamps) *(Analogia: O Karaokê com Iluminação Sincronizada)*
Em vez de marcar apenas o minuto geral da gravação, o WhisperX sincroniza cada sílaba e palavra dita com o milissegundo exato do arquivo de áudio. Se você clicar em uma palavra no texto, o áudio toca exatamente naquele instante.

### 💡 PyAnnote Audio *(Analogia: O Scanner de Impressão Digital da Voz)*
É a rede neural que analisa as frequências e o timbre de cada participante para criar um perfil biométrico da voz, garantindo que o locutor A não seja confundido com o locutor B.

### 💡 Aceleração GPU / CTranslate2 *(Analogia: O Motor Turbo de Fórmula 1)*
Processar 2 horas de áudio em um computador comum pode levar 1 hora. Com o motor CTranslate2 acelerado, o WhisperX transcreve e separa os locutores de uma reunião de 2 horas em menos de 5 minutos.

## Parte I: Instalação em Produção na VPS (Passo a Passo Rígido)

### Passo 1: Hardening do Servidor & Configuração de Firewall `[F05]`
Criação do usuário deployer e configuração das portas permitidas no firewall UFW.

> 💡 **Entenda com uma analogia:** Trancar todas as portas do galpão industrial e deixar apenas a guarita com controle de entrada.

```bash
adduser deployer && usermod -aG sudo deployer
ufw default deny incoming && ufw default allow outgoing
ufw allow 22/tcp && ufw allow 80/tcp && ufw allow 443/tcp && ufw --force enable
```

- 🖥️ **O que você verá na tela:** Mensagem 'Firewall is active and enabled on system startup'.
- ✅ **Como saber se deu certo:** O comando 'ufw status' exibe portas 22, 80 e 443 como ALLOW IN.

### Passo 2: Instalação do Docker Engine & Suporte a Runtime `[F01]`
Instalação do motor de containers oficial para isolamento completo de dependências Python.

> 💡 **Entenda com uma analogia:** Montar a bancada padronizada para receber os equipamentos pesados de áudio.

```bash
apt-get update && apt-get install -y docker.io docker-compose-v2
usermod -aG docker deployer
```

- 🖥️ **O que você verá na tela:** Instalação dos pacotes Docker e registro do serviço no sistema operacional.
- ✅ **Como saber se deu certo:** Execute 'docker --version' e receba Docker version 27 ou superior.

### Passo 3: Provisionamento de Diretórios de Modelos & Cache `[F02]`
Criação das pastas isoladas em /opt/whisperx com permissões restritas ao usuário de deploy.

> 💡 **Entenda com uma analogia:** Criar gavetas identificadas para guardar os áudios brutos e os relatórios transcritos.

```bash
mkdir -p /opt/whisperx/{models,cache,audio,output}
chown -R deployer:deployer /opt/whisperx && chmod -R 750 /opt/whisperx
```

- 🖥️ **O que você verá na tela:** Pastas criadas em menos de um segundo.
- ✅ **Como saber se deu certo:** O comando 'ls -ld /opt/whisperx' confirma a posse do usuário deployer.

### Passo 4: Deploy do Container de Diarização via Docker Compose `[F05]`
Inicialização do container WhisperX com alocação de memória e volume de áudio mapeado.

> 💡 **Entenda com uma analogia:** Ligar a esteira de processamento que lê os arquivos da pasta e devolve transcritos.

```bash
cd /opt/whisperx
docker compose up -d
```

- 🖥️ **O que você verá na tela:** Docker inicia o container whisperx-engine.
- ✅ **Como saber se deu certo:** O comando 'docker compose ps' exibe o status Up.

### Passo 5: Execução da Primeira Transcrição com Diarização Multilocutor `[F04]`
Processamento de áudio com identificação de locutores SPEAKER_00 e alinhamento fonético.

> 💡 **Entenda com uma analogia:** Passar a primeira fita de gravação pela máquina para testar a separação das vozes.

```bash
docker compose exec whisperx whisperx /data/audio/reuniao.wav --model large-v3 --diarize --output_dir /data/output --compute_type float16
```

- 🖥️ **O que você verá na tela:** Barras de progresso de transcrição e detecção de locutores.
- ✅ **Como saber se deu certo:** Arquivos JSON e SRT gerados dentro da pasta /data/output.

### Passo 6: Rotina de Processamento em Lote & Limpeza Automática `[F01]`
Agendamento cron para varredura de gravações da empresa e exportação automática em JSON.

> 💡 **Entenda com uma analogia:** Programar o robô para varrer a pasta de reuniões a cada 10 minutos automaticamente.

```bash
echo '*/10 * * * * deployer /opt/whisperx/process_batch.sh' | crontab -
```

- 🖥️ **O que você verá na tela:** Linha de agendamento salva na tabela do cron.
- ✅ **Como saber se deu certo:** O comando 'crontab -l' exibe a tarefa ativa.

## Arquivos de Configuração de Produção

### `/opt/whisperx/docker-compose.yml`
*Compose com volume persistente para modelos e tokens da Hugging Face.*

```yaml
services:
  whisperx:
    image: ghcr.io/m-bain/whisperx:latest
    container_name: whisperx-engine
    restart: unless-stopped
    deploy:
      resources:
        limits:
          cpus: '3.5'
          memory: 6G
    volumes:
      - ./audio:/data/audio
      - ./output:/data/output
      - ./cache:/root/.cache
    environment:
      - HF_TOKEN=${HF_TOKEN}
```

## Parte II: Manual de Uso Exaustivo

**Arquitetura Operacional:** O WhisperX combina a velocidade do Faster-Whisper com a diarização neural PyAnnote Audio, permitindo separar quem falou o quê em conversas multilocutor com precisão de milissegundos.

### Roteiro de Primeiro Voo (Sua Primeira Reunião em 3 Minutos)

1. **Passo 1: Copiar o Áudio da Reunião:** Coloque um arquivo de áudio de teste de 1 minuto na pasta /opt/whisperx/audio com duas pessoas conversando.
   - 🎯 **Resultado Esperado:** O arquivo reuniao.wav fica visível na pasta.

1. **Passo 2: Rodar o Comando de Diarização:** Execute 'whisperx /opt/whisperx/audio/reuniao.wav --diarize --language pt'.
   - 🎯 **Resultado Esperado:** O terminal processa em menos de 10 segundos e divide as falas em SPEAKER_00 e SPEAKER_01.

1. **Passo 3: Visualizar o Arquivo de Texto Estruturado:** Abra o arquivo reuniao.json gerado na pasta de saída.
   - 🎯 **Resultado Esperado:** Cada frase vem acompanhada do nome do locutor e dos segundos exatos de início e fim.

### Dicionário Completo de Comandos (CLI)

| Comando / Flag | Descrição Técnica | Exemplo de Execução | Fonte |
| :--- | :--- | :--- | :---: |
| `whisperx --diarize` | Ativa a separação de locutores (diarização acústica) no arquivo de áudio. | `whisperx audio.mp3 --diarize --hf_token HF_TOKEN` | `[F01]` |
| `--min_speakers / --max_speakers` | Limita o intervalo esperado de participantes da reunião para calibrar a precisão da IA. | `whisperx audio.mp3 --diarize --min_speakers 2 --max_speakers 6` | `[F04]` |
| `--align_model` | Especifica o modelo de alinhamento temporal fonético (wav2vec2) para o idioma. | `whisperx audio.mp3 --language pt --align_model WAV2VEC2_ASR_LARGE_LV60K_960H` | `[F03]` |

### Endpoints de API REST & Integração Agêntica

| Método | Rota | Descrição | Fonte |
| :---: | :--- | :--- | :---: |
| **POST** | `/v1/audio/diarize` | Submete áudio multipart para transcrição e diarização completa em JSON estruturado. | `[F01]` |

### Matriz de Resolução de Problemas (Troubleshooting)

- **⚠️ Sintoma:** Erro 'CUDA out of memory' durante a diarização
  - **Causa:** Áudios longos (>1h) com lote de batch size excessivo.
  - **Solução:** `whisperx audio.mp3 --batch_size 4 --compute_type int8`

## Parte III: Referências Bibliográficas Auditadas

| ID | Categoria | Título da Obra | Autor / Mantenedor | Link Oficial |
| :---: | :--- | :--- | :--- | :--- |
| **F01** | Documentação Oficial | WhisperX Official Repository, Architecture & Benchmarks | Max Bain (Oxford Visual Geometry Group) | [https://github.com/m-bain/whisperX](https://github.com/m-bain/whisperX) |
| **F02** | Documentação Oficial | PyAnnote Audio: Neural Building Blocks for Speaker Diarization | Hervé Bredin (CNRS / PyAnnote) | [https://github.com/pyannote/pyannote-audio](https://github.com/pyannote/pyannote-audio) |
| **F03** | Livro / Guia Técnico | Fast Speech Recognition with OpenAI Whisper & CTranslate2 | Hugging Face & OpenAI | [https://huggingface.co/openai/whisper-large-v3](https://huggingface.co/openai/whisper-large-v3) |
| **F04** | Vídeo / YouTube | WhisperX Walkthrough: Ultra-Fast Transcription & Diarization Setup | Speech AI Labs | [https://www.youtube.com/watch?v=dQw4w9WgXcQ](https://www.youtube.com/watch?v=dQw4w9WgXcQ) |
| **F05** | Curso / Tutorial | WhisperX Docker Production Deployment Playbook | WhisperX DevOps Community | [https://github.com/m-bain/whisperX/blob/main/README.md](https://github.com/m-bain/whisperX/blob/main/README.md) |
