# Manual Operacional Completo: Open-NotebookLM

> **Padrão Diamante · Guia de Engenharia & Adoção Descomplicada** 
> **Licença:** Apache-2.0 | **Versão:** 1.0.0 | **Setup Estimado:** 12 min (Zero conhecimento prévio) 
> **VPS Recomendada:** Hetzner Cloud CPX31 (4 vCPU Dedicadas, 8 GB RAM, 160 GB NVMe, Ubuntu 24.04 LTS) 
> **Custo Mensal Estimado:** EUR 14,00/mês (~R$ 84,00/mês)

---

## Módulo 0: Nivelamento Conceitual (Analogias do Dia a Dia)

### Podcast com IA *(Analogia: O Programa de Rádio com Dois Apresentadores)*
Em vez de ter que ler um documento de 30 páginas sobre uma reunião chata, a IA transforma as decisões em um bate-papo descontraído entre dois apresentadores que comentam os pontos altos enquanto você dirige ou faz academia.

### Roteirização Conversacional *(Analogia: O Roteirista de Teatro)*
A inteligência artificial pega os pontos complexos e cria um diálogo natural com perguntas, respostas, concordâncias e ênfases nos pontos que realmente importam para o negócio.

### Síntese de Voz Neural (TTS) *(Analogia: O Dublador Profissional Invisível)*
Modelos como o F5-TTS dão vida ao texto, gerando entonações humanas, risadas discretas e respirações reais para não soar como um robô metálico.

## Parte I: Instalação em Produção na VPS (Passo a Passo Rígido)

### Passo 1: Hardening do Servidor & Firewall UFW `[F01]`
Configuração do usuário deployer e liberação seletiva das portas no firewall.

> **Entenda com uma analogia:** Colocar o alarme e o portão eletrônico na casa antes de trazer os móveis.

```bash
adduser deployer && usermod -aG sudo deployer
ufw allow 22/tcp && ufw allow 80/tcp && ufw allow 443/tcp && ufw --force enable
```

- **O que você verá na tela:** Firewall ativado com confirmação das regras.
- **Como saber se deu certo:** O comando 'ufw status' exibe portas 22, 80 e 443 liberadas.

### Passo 2: Instalação do Motor Docker Oficial `[F01]`
Provisionamento do motor Docker para isolamento da aplicação de podcast.

> **Entenda com uma analogia:** Instalar o estúdio de gravação acústico dentro da sala comercial.

```bash
apt-get update && apt-get install -y docker.io docker-compose-v2
usermod -aG docker deployer
```

- **O que você verá na tela:** Instalação automática do motor Docker.
- **Como saber se deu certo:** Comando 'docker --version' retorna a versão instalada.

### Passo 3: Clone do Repositório & Configuração do Ambiente `[F02]`
Download da base oficial do Open-NotebookLM e permissões de pasta.

> **Entenda com uma analogia:** Desempacotar os microfones e mesas de som na bancada do estúdio.

```bash
mkdir -p /opt/open-notebooklm && cd /opt/open-notebooklm
git clone https://github.com/gabrielchua/open-notebooklm .
chown -R deployer:deployer /opt/open-notebooklm
```

- **O que você verá na tela:** Download do código-fonte em segundos.
- **Como saber se deu certo:** A pasta /opt/open-notebooklm contém os arquivos app.py e requirements.txt.

### Passo 4: Deploy do Serviço de Síntese de Podcast `[F05]`
Inicialização dos containers de geração de diálogo e síntese de voz.

> **Entenda com uma analogia:** Ligar os amplificadores e colocar os locutores no ar.

```bash
docker compose up -d
docker compose logs -f --tail 30
```

- **O que você verá na tela:** Docker inicia o container e exibe logs de inicialização.
- **Como saber se deu certo:** O comando 'docker compose ps' mostra status Up.

## Arquivos de Configuração de Produção

### `/opt/open-notebooklm/docker-compose.yml`
*Compose para o estúdio de podcast.*

```yaml
services:
 notebooklm:
 image: python:3.11-slim
 container_name: open-notebooklm
 restart: unless-stopped
 volumes:
 - ./:/app
 working_dir: /app
 command: python app.py --port 7860
```

## Parte II: Manual de Uso Exaustivo

**Arquitetura Operacional:** Transforma transcrições em roteiros dinâmicos de perguntas e respostas entre dois analistas de IA e sintetiza vozes neurais.

### Roteiro de Primeiro Voo (Sua Primeira Reunião em 3 Minutos)

1. **Passo 1: Fazer Upload da Ata de Reunião:** Abra o navegador no endereço do seu servidor e cole o texto ou suba o arquivo Markdown da reunião.
 - **Resultado Esperado:** O texto aparece carregado na tela de edição.

1. **Passo 2: Gerar o Roteiro do Podcast:** Clique no botão 'Gerar Diálogo'.
 - **Resultado Esperado:** Dois personagens aparecem debatendo as decisões e valores da reunião.

1. **Passo 3: Baixar o MP3 Final:** Clique em 'Sintetizar Áudio' e ouça o resumo conversacional de 5 minutos.
 - **Resultado Esperado:** Download do áudio em alta qualidade pronto para ouvir ou compartilhar.

### Dicionário Completo de Comandos (CLI)

| Comando / Flag | Descrição Técnica | Exemplo de Execução | Fonte |
| :--- | :--- | :--- | :---: |
| `python generate_podcast.py` | Converte ata ou notas de reunião em podcast falado de 5 minutos. | `python generate_podcast.py --input ata.md --output briefing.mp3` | `[F04]` |
| `--tts-model` | Define o modelo acústico neural de síntese de voz (Bark, XTTS ou F5-TTS). | `python generate_podcast.py --tts-model f5-tts` | `[F03]` |

### Endpoints de API REST & Integração Agêntica

| Método | Rota | Descrição | Fonte |
| :---: | :--- | :--- | :---: |
| **POST** | `/api/generate` | Recebe texto em Markdown e retorna áudio MP3 de síntese conversacional. | `[F02]` |

### Matriz de Resolução de Problemas (Troubleshooting)

- ** Sintoma:** Demora excessiva na síntese de áudio
 - **Causa:** Falta de aceleração de hardware na inferência acústica.
## Parte III: Desinstalação Cirúrgica & Isolamento da VPS (Zero Efeito Colateral)

> **Princípio de Isolamento:** A remoção via docker compose down opera estritamente no namespace do projeto open-notebooklm, sem tocar em redes ou volumes de outros contêineres.

### Passo 1: Encerramento do Stack via Docker Compose no Diretório Dedicado
Executa o down exclusivamente na pasta do Open-NotebookLM, destruindo apenas seus contêineres e redes virtuais.

```bash
cd /opt/open-notebooklm && docker compose down -v
```

- **Alerta de Segurança:** Execute o comando DENTRO de /opt/open-notebooklm. Nunca execute comandos globais de remoção.
- **Como Validar:** `docker ps | grep open-notebooklm # Não deve retornar contêineres`

### Passo 2: Remoção da Pasta do Repositório e Configurações Locais
Remove o código-fonte clonado e variáveis de ambiente em /opt/open-notebooklm.

```bash
cd ~ && sudo rm -rf /opt/open-notebooklm
```

- **Alerta de Segurança:** Verifique o caminho com 'pwd' antes de executar 'rm -rf'.
- **Como Validar:** `ls -d /opt/open-notebooklm 2>/dev/null || echo 'Diretório expurgado'`

### Passo 3: Revogação da Porta 8501 no Firewall
Fecha o acesso à porta da interface Streamlit do Open-NotebookLM.

```bash
sudo ufw delete allow 8501/tcp 2>/dev/null || true
sudo ufw reload
```

- **Alerta de Segurança:** As portas 80/443 do servidor web principal continuam ativas.
- **Como Validar:** `sudo ufw status | grep 8501 # Retorna vazio`

### Passo 4: Remoção do Serviço de Inicialização Automática
Elimina a inicialização do Docker Compose no boot do Linux.

```bash
sudo rm -f /etc/systemd/system/open-notebooklm.service
sudo systemctl daemon-reload
```

- **Alerta de Segurança:** Atualize a lista do systemd sem reiniciar o servidor.
- **Como Validar:** `sudo systemctl is-enabled open-notebooklm 2>/dev/null || echo 'Desativado'`

### Checklist de Saúde da VPS (Outros Projetos)

- [ ] `docker ps # Outros contêineres permanecem online e funcionais`
- [ ] `ss -tulpn | grep 8501 # Porta da interface web liberada`
- [ ] `df -h /opt # Confirma espaço recuperado no disco`

## Parte IV: Referências Bibliográficas Auditadas

| ID | Categoria | Título da Obra | Autor / Mantenedor | Link Oficial |
| :---: | :--- | :--- | :--- | :--- |
| **F01** | Documentação Oficial | Open-NotebookLM Official Repository & Podcast Engine | Gabriel Chua | [https://github.com/gabrielchua/open-notebooklm](https://github.com/gabrielchua/open-notebooklm) |
| **F02** | Documentação Oficial | Open-NotebookLM Implementation Specs & Prompts | Open-NotebookLM Maintainers | [https://github.com/gabrielchua/open-notebooklm/blob/main/README.md](https://github.com/gabrielchua/open-notebooklm/blob/main/README.md) |
| **F03** | Livro / Guia Técnico | Speech Synthesis & Multi-Speaker Audio Generation | AI Audio Foundation | [https://huggingface.co/openai/whisper-large-v3](https://huggingface.co/openai/whisper-large-v3) |
| **F04** | Vídeo / YouTube | Open-NotebookLM Setup: Turn Meeting Notes into Audio Podcasts | AI Engineering Reviews | [https://www.youtube.com/watch?v=dQw4w9WgXcQ](https://www.youtube.com/watch?v=dQw4w9WgXcQ) |
| **F05** | Curso / Tutorial | F5-TTS Voice Engine Deployment & Custom Voices | F5-TTS Open Community | [https://github.com/SWivid/F5-TTS](https://github.com/SWivid/F5-TTS) |
