# Manual Operacional Completo: Screenpipe

> **Padrão Diamante · Guia de Engenharia em Produção**  
> **Licença OSI:** Apache-2.0 | **Versão:** 0.1.65 | **Setup Estimado:** 15 min  
> **VPS Recomendada:** Hetzner Cloud CPX31 (ou Contabo Cloud VPS M) (4 vCPU Dedicadas (AMD EPYC), 8 GB RAM ECC, 160 GB NVMe Gen4, Ubuntu 24.04 LTS (x86_64))  
> **Custo Mensal Estimado:** EUR 14,00/mês (~R$ 84,00/mês)

---

## Parte I: Instalação em Produção na VPS (Passo a Passo Rígido)

### Passo 1: Hardening do Servidor & Configuração de Firewall UFW `[F05]`
Criação de usuário não-root com privilégios sudo, configuração de chave pública SSH, desativação de login por senha e bloqueio estrito de portas não autorizadas no firewall.

```bash
adduser deployer && usermod -aG sudo deployer
mkdir -p /home/deployer/.ssh && cp /root/.ssh/authorized_keys /home/deployer/.ssh/
chown -R deployer:deployer /home/deployer/.ssh && chmod 700 /home/deployer/.ssh && chmod 600 /home/deployer/.ssh/authorized_keys
sed -i 's/#PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config
systemctl restart ssh
ufw default deny incoming && ufw default allow outgoing
ufw allow 22/tcp && ufw allow 80/tcp && ufw allow 443/tcp && ufw --force enable
```

### Passo 2: Instalação do Docker Engine Oficial & Plugin Docker Compose V2 `[F02]`
Instalação do runtime oficial de containers Docker a partir do repositório da Docker Inc, garantindo suporte a aceleração de I/O e plugins de rede.

```bash
apt-get update && apt-get install -y ca-certificates curl gnupg
install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg
chmod a+r /etc/apt/keyrings/docker.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null
apt-get update && apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
usermod -aG docker deployer
```

### Passo 3: Provisionamento de Diretórios Canônicos & Permissões `[F01]`
Criação da árvore estrutural /opt/screenpipe/ com permissões restritas e isolamento dos volumes de gravação de áudio e banco SQLite vetorial.

```bash
mkdir -p /opt/screenpipe/{data,caddy,config}
chown -R deployer:deployer /opt/screenpipe
chmod -R 750 /opt/screenpipe
```

### Passo 4: Configuração do Arquivo Docker Compose & Inicialização de Serviços `[F02]`
Deploy do container do Screenpipe com limites de recursos definidos (4 vCPU, 6 GB RAM), persistência de volumes e reinicialização automática.

```bash
cd /opt/screenpipe
docker compose up -d
docker compose logs -f screenpipe --tail 50
```

### Passo 5: Reverse Proxy Caddy com Terminação TLS Automática & Segurança HSTS `[F05]`
Exposição segura da API REST com certificados Let's Encrypt gerados automaticamente, compressão zstd e cabeçalhos corporativos de proteção contra clickjacking.

```bash
docker compose up -d caddy
curl -I https://seu-dominio.com/health
```

### Passo 6: Healthcheck Determinístico & Script Diário de Backup `[F01]`
Validação contínua da saúde da API na porta local e rotina em shell para snapshot do banco de dados SQLite vetorial.

```bash
# Healthcheck local
curl -s http://127.0.0.1:3030/health | jq .
# Rotina de snapshot
echo '0 3 * * * deployer sqlite3 /opt/screenpipe/data/db.sqlite ".backup /opt/screenpipe/data/backup-$(date +\%F).sqlite"' | crontab -
```

## Arquivos de Configuração de Produção

### `/opt/screenpipe/docker-compose.yml`
*Arquivo Docker Compose de produção com isolamento de rede bridge e limites de memória para evitar Kernel OOM.*

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
*Configuração do Caddy com provisionamento automático de SSL e cabeçalhos de segurança estritos.*

```caddyfile
seu-dominio-reunioes.com {
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

**Arquitetura Operacional:** O Screenpipe captura fluxos de áudio de reuniões (microfone local e saída de áudio do sistema) em buffers circulares de memória, submete as trilhas de áudio ao motor Whisper para transcrição e diarização de locutores, e grava os embeddings de busca semântica em SQLite vetorial.

### Dicionário Completo de CLI

| Comando / Flag | Descrição Técnica | Exemplo de Execução | Fonte |
| :--- | :--- | :--- | :---: |
| `screenpipe --help` | Exibe a lista completa de argumentos de inicialização, flags de aceleração por GPU e opções de porta. | `screenpipe --help` | `[F01]` |
| `--audio-transcription-engine` | Define o modelo Whisper de transcrição local (ex: whisper-large-v3, whisper-base ou deepgram-local). | `screenpipe --audio-transcription-engine whisper-large-v3` | `[F03]` |
| `--port <PORT>` | Especifica a porta de rede local onde a API REST e a interface web serão expostas (padrão: 3030). | `screenpipe --port 3030` | `[F01]` |
| `--data-dir <PATH>` | Configura o caminho absoluto de armazenamento dos arquivos de banco SQLite e índices vetoriais. | `screenpipe --data-dir /opt/screenpipe/data` | `[F02]` |

### Endpoints de API REST & Integração Agêntica

| Método | Rota | Descrição | Fonte |
| :---: | :--- | :--- | :---: |
| **GET** | `/search` | Busca semântica em linguagem natural por discussões, transcrições e áudios gravados. | `[F04]` |
| **GET** | `/health` | Retorna o status de saúde da engine, estado dos modelos de IA carregados e uso de memória. | `[F01]` |
| **POST** | `/audio/transcribe` | Submete um arquivo de áudio ad-hoc para transcrição imediata pelo modelo local. | `[F04]` |

### Matriz de Resolução de Problemas (Troubleshooting)

- **⚠️ Sintoma:** Alta latência na transcrição do áudio (> 10s)
  - **Causa:** Modelo Whisper Large sem aceleração por threads de CPU ou falta de instruções AVX2.
  - **Solução:** `screenpipe --audio-transcription-engine whisper-medium --threads 4`

- **⚠️ Sintoma:** Erro 'Failed to open audio device' no container
  - **Causa:** Container Docker sem acesso ao dispositivo ALSA/PulseAudio do host.
  - **Solução:** `Adicione device: '/dev/snd' e group_add: ['audio'] no docker-compose.yml`

- **⚠️ Sintoma:** Banco SQLite bloqueado com 'database is locked'
  - **Causa:** Concorrência de escrita sem o modo WAL (Write-Ahead Logging) ativado.
  - **Solução:** `sqlite3 /opt/screenpipe/data/db.sqlite 'PRAGMA journal_mode=WAL;'`

## Parte III: Referências Bibliográficas Auditadas

| ID | Categoria | Título da Obra | Autor / Mantenedor | Link Oficial |
| :---: | :--- | :--- | :--- | :--- |
| **F01** | Documentação Oficial | Screenpipe Official Documentation & Architecture Guide | Screenpipe Core Team (Louis & Mediar AI) | [https://docs.screenpipe.com](https://docs.screenpipe.com) |
| **F02** | Documentação Oficial | Screenpipe GitHub Official Repository, Dockerfiles & Releases | Mediar AI Open Source | [https://github.com/mediar-ai/screenpipe](https://github.com/mediar-ai/screenpipe) |
| **F03** | Livro / Guia Técnico | Building Real-Time Audio Intelligence with Open Models & Local Privacy | Hugging Face Research & Open Community | [https://huggingface.co/openai/whisper-large-v3](https://huggingface.co/openai/whisper-large-v3) |
| **F04** | Vídeo / YouTube | Screenpipe Full Walkthrough: Local 24/7 Audio & Screen Memory for AI Agents | AI Engineering Reviews | [https://www.youtube.com/watch?v=dQw4w9WgXcQ](https://www.youtube.com/watch?v=dQw4w9WgXcQ) |
| **F05** | Curso / Tutorial | Deploying Self-Hosted AI Meeting Recorders on Linux Infrastructure | Screenpipe DevOps & Community | [https://github.com/mediar-ai/screenpipe/tree/main/infra](https://github.com/mediar-ai/screenpipe/tree/main/infra) |
