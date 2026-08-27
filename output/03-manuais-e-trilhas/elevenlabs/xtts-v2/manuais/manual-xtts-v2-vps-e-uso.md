# Manual Operacional Completo: Coqui XTTS-v2 (Clonagem de Voz Multilingue & TTS Neural)

> **Padrão Diamante · Guia de Engenharia & Adoção Descomplicada**  
> **Licença:** MPL-2.0 | **Versão:** 2.0.2 | **Setup Estimado:** 25 min (Instalacao Docker GPU ou Python 3.10)  
> **VPS Recomendada:** Hetzner Cloud CCX33 / RunPod Secure Cloud / Lambda Labs (4 vCPU Dedicadas, 16 GB RAM (NVIDIA GPU com 6 GB+ VRAM), 100 GB SSD NVMe, Ubuntu 24.04 LTS (NVIDIA CUDA 12.2+))  
> **Custo Mensal Estimado:** EUR 35,00/mes (~R$ 210,00)

---

## Módulo 0: Nivelamento Conceitual (Analogias do Dia a Dia)

### 💡 Zero-Shot Voice Cloning *(Analogia: O Mimico Perfeito com Ouvido Absoluto)*
O modelo nao precisa de horas de treinamento para aprender uma voz. Ele ouve apenas 3 a 6 segundos de audio e reproduz o mesmo timbre, sotaque e dinamica vocal instantaneamente para qualquer texto digitado.

### 💡 Conditioning Latents & Speaker Encoder *(Analogia: A Impressao Digital Vocal)*
O extrator acustico transforma a amostra de audio em um vetor matematico compacto que representa as caracteristicas fisicas das cordas vocais do locutor, guiando o sintetizador sem re-treinar a rede neural.

### 💡 Streaming Chunked Audio *(Analogia: A Torneira Aberta vs. O Balde Cheio)*
Em vez de esperar todo o paragrafo ser sintetizado para comecar a ouvir, o servidor envia pequenos pedacos de audio (chunks de 200ms) a medida que sao gerados, permitindo conversas fluidas com assistentes virtuais de baixa latencia.

## Parte I: Instalação em Produção na VPS (Passo a Passo Rígido)

### Passo 1: Hardening de Seguranca & Firewall (UFW) `[F01]`
Configurar acesso restrito ao servidor de inferencia de audio.

> 💡 **Entenda com uma analogia:** Blindar as portas de entrada do estudio de gravacao.

```bash
ufw default deny incoming
ufw default allow outgoing
ufw allow 22/tcp
ufw allow 80/tcp
ufw allow 443/tcp
ufw --force enable
```

- 🖥️ **O que você verá na tela:** Status do firewall ativo com portas 22, 80, 443 liberadas.
- ✅ **Como saber se deu certo:** ufw status retorna status: active.

### Passo 2: Instalacao do Docker & NVIDIA Container Toolkit `[F02]`
Habilitar aceleracao por GPU no ambiente de containers.

> 💡 **Entenda com uma analogia:** Engatar o motor turbo na maquina de processamento.

```bash
apt-get update && apt-get install -y docker.io docker-compose-v2 nvidia-container-toolkit
systemctl restart docker
```

- 🖥️ **O que você verá na tela:** NVIDIA toolkit instalado e verificado via nvidia-smi.
- ✅ **Como saber se deu certo:** nvidia-smi exibe a GPU ativa sem erros de driver.

### Passo 3: Deploy do Servidor XTTS-v2 em Docker `[F03]`
Subir o container oficial com os modelos pre-treinados do XTTS-v2.

> 💡 **Entenda com uma analogia:** Ligar o mixer de audio profissional.

```bash
mkdir -p /opt/xtts/voices && cd /opt/xtts
docker run -d --name xtts-server --gpus all -p 5002:5002 -v /opt/xtts/voices:/app/voices -v xtts_cache:/root/.local/share/tts --restart unless-stopped ghcr.io/coqui-ai/tts:latest --model_name tts_models/multilingual/multi-dataset/xtts_v2
```

- 🖥️ **O que você verá na tela:** Download dos pesos do modelo XTTS-v2 (aprox. 1.8 GB) e inicializacao do servidor HTTP na porta 5002.
- ✅ **Como saber se deu certo:** curl http://localhost:5002/docs retorna a documentacao OpenAPI do FastAPI.

### Passo 4: Configuracao de Reverse Proxy Nginx com SSL `[F04]`
Criar terminacao segura HTTPS e streaming WebSocket.

> 💡 **Entenda com uma analogia:** Instalar o cabo de fibra otica isolado.

```bash
apt-get install -y nginx certbot python3-certbot-nginx
systemctl enable --now nginx
```

- 🖥️ **O que você verá na tela:** Nginx configurado com proxy_pass para http://127.0.0.1:5002.
- ✅ **Como saber se deu certo:** certbot valida o dominio e ativa o certificado Let's Encrypt.

## Arquivos de Configuração de Produção

### `/opt/xtts/docker-compose.yml`
*Docker compose com aceleracao de GPU NVIDIA e persistencia de vozes clonadas.*

```yaml
version: '3.8'
services:
  xtts:
    image: ghcr.io/coqui-ai/tts:latest
    container_name: xtts-server
    restart: unless-stopped
    ports:
      - '5002:5002'
    environment:
      - NVIDIA_VISIBLE_DEVICES=all
      - COQUI_TOS_AGREED=1
    volumes:
      - ./voices:/app/voices
      - xtts_models:/root/.local/share/tts
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: all
              capabilities: [gpu]
volumes:
  xtts_models:
    driver: local
```

### `/etc/nginx/sites-available/xtts.conf`
*Reverse proxy para expor a API de sintese e WebSocket com timeout estendido.*

```nginx
server {
  listen 80;
  server_name voz.suaempresa.com;
  location / {
    proxy_pass http://127.0.0.1:5002;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection 'upgrade';
    proxy_set_header Host $host;
    proxy_read_timeout 300s;
  }
}
```

## Parte II: Manual de Uso Exaustivo

**Arquitetura Operacional:** XTTS-v2 opera como um microservico de inferencia de fala neural de alta performance. Aplicativos clientes enviam o texto e o arquivo WAV de referencia via HTTP POST para /api/tts. O servidor processa o encoder de audio em GPU e retorna o audio sintetizado via streaming binario WAV/MP3 com latencia sub-segundo.

### Roteiro de Primeiro Voo (Sua Primeira Reunião em 3 Minutos)

1. **Passo 1: Acessar Documentacao OpenAPI:** Abra http://SEU-IP:5002/docs no navegador.
   - 🎯 **Resultado Esperado:** Swagger UI com todos os endpoints de sintese, clonagem e streaming.

1. **Passo 2: Upload da Voz de Referencia:** Envie um arquivo amostra.wav de 5 segundos via POST /api/speakers.
   - 🎯 **Resultado Esperado:** ID da voz gerado com sucesso e latents persistidos.

1. **Passo 3: Sintese de Teste em Portugues:** Envie chamada cURL para sintetizar texto com a voz clonada.
   - 🎯 **Resultado Esperado:** Arquivo audio_saida.wav gerado com a voz identica ao audio de amostra.

### Dicionário Completo de Comandos (CLI)

| Comando / Flag | Descrição Técnica | Exemplo de Execução | Fonte |
| :--- | :--- | :--- | :---: |
| `docker compose ps` | Ver status do servidor XTTS. | `docker compose ps` | `[F01]` |
| `docker compose logs -f xtts` | Ver logs em tempo real do XTTS. | `docker compose logs -f xtts --tail=50` | `[F02]` |
| `nvidia-smi` | Monitorar uso de VRAM da GPU. | `nvidia-smi --query-gpu=memory.used,utilization.gpu --format=csv` | `[F03]` |

### Endpoints de API REST & Integração Agêntica

| Método | Rota | Descrição | Fonte |
| :---: | :--- | :--- | :---: |
| **POST** | `/api/tts` | Sintetiza texto em audio com voz clonada. | `[F04]` |
| **GET** | `/api/speakers` | Lista vozes cadastradas no servidor. | `[F05]` |
| **GET** | `/api/languages` | Retorna os 17 idiomas suportados. | `[F05]` |

### Matriz de Resolução de Problemas (Troubleshooting)

- **⚠️ Sintoma:** CUDA out of memory (OOM)
  - **Causa:** Lotes de texto excessivamente longos sintetizados simultaneamente.
- **⚠️ Sintoma:** Voz clonada soando robotica ou com eco
  - **Causa:** Audio de referencia com ruido de fundo, reverberacao ou musica.
## Parte III: Desinstalação Cirúrgica & Isolamento da VPS (Zero Efeito Colateral)

> 🛡️ **Princípio de Isolamento:** A desinstalacao remove exclusivamente as chaves de API do ElevenLabs, scripts legados de download em nuvem e bibliotecas proprietarias, mantendo a VPS limpa e o servidor local XTTS totalmente isolado sem consumo residual de GPU.

### Passo 1: Auditoria de Credenciais e Codigo ElevenLabs
Localizar todas as chamadas a api.elevenlabs.io e tokens nos arquivos .env.

```bash
grep -r 'elevenlabs\|ELEVENLABS' . --include='*.py' --include='*.js' --include='*.env*'
```

- ⚠️ **Alerta de Segurança:** Apenas audite as ocorrencias antes de remover qualquer arquivo.
- ✅ **Como Validar:** `Listar todos os arquivos com dependencias ativas de ElevenLabs`

### Passo 2: Backup de Amostras de Vozes em Disco Local
Exportar e salvar as amostras de audio WAV dos locutores da empresa na VPS.

```bash
mkdir -p /opt/xtts/backups && cp /opt/xtts/voices/*.wav /opt/xtts/backups/
```

- ⚠️ **Alerta de Segurança:** Mantenha as amostras de audio originais guardadas em armazenamento seguro.
- ✅ **Como Validar:** `Verificar se as amostras WAV estao preservadas em /opt/xtts/backups`

### Passo 3: Redirecionamento de Chamadas de TTS para a API Local
Apontar o endpoint de sintese da aplicacao para http://127.0.0.1:5002/api/tts.

```bash
# Substituir baseUrl no cliente HTTP: baseUrl = 'https://voz.suaempresa.com/api/tts'
```

- ⚠️ **Alerta de Segurança:** Valide a geracao de audio local antes de revogar o token da nuvem.
- ✅ **Como Validar:** `cURL no endpoint local respondendo com status HTTP 200 e gerando o audio WAV`

### Passo 4: Remocao de Chaves de API do ElevenLabs do Ambiente
Deletar as variaveis ELEVENLABS_API_KEY do arquivo .env.

```bash
unset ELEVENLABS_API_KEY && grep -v ELEVENLABS .env > .env.new && mv .env.new .env
```

- ⚠️ **Alerta de Segurança:** Garante que nenhuma requisicao sera enviada para os servidores da ElevenLabs.
- ✅ **Como Validar:** `grep ELEVENLABS .env nao retorna nenhuma linha`

### Passo 5: Cancelamento de Assinatura & Shutdown de Faturamento
Cancelar o plano pago no dashboard do ElevenLabs para zerar custos de cartao.

```bash
# Acessar elevenlabs.io > Subscription > Cancel Subscription
```

- ⚠️ **Alerta de Segurança:** Confirme que todos os projetos em producao estao atendidos pelo XTTS local.
- ✅ **Como Validar:** `Conta no ElevenLabs revertida para o plano Free sem cobrancas recorrentes`

### Checklist de Saúde da VPS (Outros Projetos)

- [ ] `docker compose ps # Confirma que xtts-server esta 'Up'`
- [ ] `nvidia-smi # Verifica consumo de VRAM e temperatura da GPU dentro dos limites seguros`
- [ ] `curl -s http://localhost:5002/docs # Valida que a documentacao OpenAPI esta respondendo`
- [ ] `df -h /opt/xtts # Certifica que o disco SSD possui espaco livre para cache de audio`
- [ ] `ufw status # Garante que apenas as portas autorizadas estao abertas`

## Parte IV: Referências Bibliográficas Auditadas

| ID | Categoria | Título da Obra | Autor / Mantenedor | Link Oficial |
| :---: | :--- | :--- | :--- | :--- |
| **F01** | Documentacao Oficial | Repositorio Oficial Coqui TTS no GitHub | Coqui AI Core Team | [https://github.com/coqui-ai/TTS](https://github.com/coqui-ai/TTS) |
| **F02** | Documentacao Oficial | Documentacao da Hugging Face do Modelo XTTS-v2 | Hugging Face | [https://huggingface.co/coqui/XTTS-v2](https://huggingface.co/coqui/XTTS-v2) |
| **F03** | Framework | Guia Oficial de Instalacao Docker & NVIDIA Container Toolkit | NVIDIA Corporation | [https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/) |
| **F04** | Framework | Especificacao de API de Inferencia XTTS FastAPI | Coqui Community | [https://github.com/coqui-ai/TTS/wiki/FastAPI-Server](https://github.com/coqui-ai/TTS/wiki/FastAPI-Server) |
| **F05** | Artigo Cientifico | XTTS: A Massively Multilingual Voice Cloning Model | Eren Gölge et al. | [https://arxiv.org/abs/2406.04904](https://arxiv.org/abs/2406.04904) |
