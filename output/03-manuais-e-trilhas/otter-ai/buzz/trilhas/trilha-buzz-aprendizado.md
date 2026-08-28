# Trilha Cronológica de Aprendizado: BUZZ

> **Jornada Pedagógica Autoguiada · Imersão a Partir das Fontes Primárias**  
> **Tempo Total Estimado:** 6 a 8 horas (1 semana a 1-2 horas diárias) | **Fases:** 5 Módulos  
> **Dossiê SaaS de Origem:** Otter-Ai

---

## Fundação: O que é BUZZ e Por Que Deveria Importar (`⏱️ 1.5 horas`)
**🎯 Meta da Etapa:** Entender que BUZZ é transcrição de áudio open source, por que é superior ao SaaS pago (Otter.ai, Rev, AssemblyAI), qual é o custo real (apenas VPS, não por minuto), e os 3 use cases principais (reuniões, palestras, entrevistas).

- [ ] **[O que é BUZZ? Explicação para Não-Técnicos](https://www.youtube.com/results?search_query=transcrição+áudio+whisper+tutorial)** (`Video YouTube` - `[T01]`)
  - 💡 **O que você aprende:** BUZZ é uma ferramenta que converte áudio (MP3, WAV) em texto. Automático. Gratuito. Você é dono dos dados. Otter.ai cobra USD 10/mês. Rev cobra USD 0,25/min. BUZZ custa apenas R$ 80/mês de VPS.
  - ⏱️ 12 minutos | 👤 Arsenal Open Source

- [ ] **[BUZZ vs Otter.ai vs Rev vs AssemblyAI - Comparação de Custos](https://github.com/chidiwilliams/buzz#comparison)** (`Planilha Comparativa` - `[T02]`)
  - 💡 **O que você aprende:** Otter.ai: USD 10-20/mês (transcrição ilimitada, mas dados deles). Rev: USD 0,25/min (10 horas = USD 150!). AssemblyAI: USD 0,0036/min (ainda USD 21 por hora). BUZZ: R$ 80/mês unlimited (10x mais barato). Trade-off: você gerencia servidor.
  - ⏱️ 5 minutos de leitura | 👤 Arsenal Open Source

- [ ] **[Whisper - O Motor Invisível: Como Funciona](https://openai.com/research/whisper)** (`Artigo Didático` - `[T03]`)
  - 💡 **O que você aprende:** Whisper é um modelo de IA treinado com 680 mil horas de áudio multilíngue. Acurácia 95-99% em idiomas comuns. Suporta 99 idiomas. Detecta idioma automaticamente. Roda offline (você não precisa enviar áudio para servidores externos).
  - ⏱️ 8 minutos de leitura | 👤 OpenAI Research

- [ ] **[Use Cases Principais: Quando Você Precisa de BUZZ](https://github.com/chidiwilliams/buzz#use-cases)** (`Guia Prático` - `[T04]`)
  - 💡 **O que você aprende:** Use case 1: Reuniões - gravar Zoom/Teams e transcrever automaticamente. Use case 2: Palestras/Conferências - converter vídeos em texto para SEO. Use case 3: Entrevistas Jornalísticas - transcrever áudio de repórter. Use case 4: Atendimento ao Cliente - gravar chamadas e analisar satisfação.
  - ⏱️ 10 minutos de leitura | 👤 Arsenal Open Source

## Instalação e Configuração: Colocar BUZZ em Produção (`⏱️ 2 horas`)
**🎯 Meta da Etapa:** Ter BUZZ rodando em uma VPS própria, acessível via HTTPS, com primeiro áudio testado com sucesso.

- [ ] **[Pré-Requisitos: O Que Você Precisa Antes de Começar](https://github.com/chidiwilliams/buzz#requirements)** (`Checklist` - `[T05]`)
  - 💡 **O que você aprende:** VPS com Linux (Ubuntu 22.04 recomendado). Python 3.11+. ffmpeg instalado. Domínio próprio (para HTTPS). Conhecimento básico de SSH. Se tiver tudo, pode prosseguir.
  - ⏱️ 5 minutos | 👤 Arsenal Open Source

- [ ] **[Guia Passo-a-Passo: Instalar BUZZ em Ubuntu 22.04](file:///output/03-manuais-e-trilhas/standalone/buzz/manuais/manual-buzz-vps-e-uso.html)** (`Manual Técnico` - `[T06]`)
  - 💡 **O que você aprende:** SSH → Atualizar Sistema → Instalar Python/ffmpeg → Clonar BUZZ → Virtual Environment → Dependências → Serviço systemd → Apache Proxy Reverso → SSL Let's Encrypt. Cada passo testado.
  - ⏱️ 60 minutos de execução | 👤 Arsenal Open Source

- [ ] **[Primeira Transcrição: Upload e Teste](https://www.youtube.com/results?search_query=buzz+transcrição+primeiro+uso)** (`Video Tutorial` - `[T07]`)
  - 💡 **O que você aprende:** Abrir https://buzz.sua-empresa.com.br. Upload de um áudio MP3 (20-30 segundos). Aguardar processamento (1-2 minutos). Copiar transcrição. Sucesso!
  - ⏱️ 15 minutos | 👤 Comunidade BUZZ

- [ ] **[Verificar Saúde da Instalação](https://github.com/chidiwilliams/buzz#troubleshooting)** (`Checklist Técnico` - `[T08]`)
  - 💡 **O que você aprende:** Testar: systemctl status buzz (ativo?). Apache vhost (carregado?). SSL válido (wget https://buzz... retorna 200?). Modelo Whisper baixado (/root/.cache/). Permissões de arquivo corretas.
  - ⏱️ 10 minutos | 👤 Arsenal Open Source

## Uso Diário: Interface Web e Fluxos Práticos (`⏱️ 1.5 horas`)
**🎯 Meta da Etapa:** Dominar upload de áudios, ajustar qualidade/idioma, exportar transcrições em diferentes formatos, e integrar em fluxos de trabalho reais.

- [ ] **[Dashboard Explicado: Cada Botão e Campo](https://github.com/chidiwilliams/buzz#ui-guide)** (`Guia Visual` - `[T09]`)
  - 💡 **O que você aprende:** Botão 'Upload': selecionar arquivo. Campo 'Modelo': base (rápido), small/medium/large (mais preciso). Campo 'Idioma': auto-detect ou forçar português/inglês. Botão 'Transcrever': iniciar processamento. Resultado: texto + opções de cópia/download.
  - ⏱️ 15 minutos | 👤 Arsenal Open Source

- [ ] **[Formatos de Saída: TXT vs JSON vs SRT](https://github.com/chidiwilliams/buzz#output-formats)** (`Tutorial Prático` - `[T10]`)
  - 💡 **O que você aprende:** TXT: texto puro, bom para Word/Google Docs. JSON: inclui timestamps, confiança por palavra (uso em automações). SRT: formato de legenda para vídeos (compatível com Premiere, OBS, YouTube).
  - ⏱️ 10 minutos | 👤 Comunidade BUZZ

- [ ] **[Ajustar Qualidade e Precisão](https://openai.com/research/whisper#model-performance)** (`Guia de Otimização` - `[T11]`)
  - 💡 **O que você aprende:** Modelo 'base': 94% acurácia, 30 segundos/minuto. Modelo 'small': 96%, 1 minuto/minuto. Modelo 'medium': 97%, 2 min/min. Modelo 'large': 99%, 5-10 min/min. Trade-off speed vs precision. Comece com 'base', aumente se tiver erros.
  - ⏱️ 12 minutos | 👤 Arsenal Open Source

- [ ] **[Idiomas e Sotaques: Configurar Corretamente](https://github.com/openai/whisper#available-models-and-languages)** (`Referência` - `[T12]`)
  - 💡 **O que você aprende:** Whisper suporta 99 idiomas. Se áudio é misturado (ex: português + inglês), deixar 'auto-detect'. Se 100% português, forçar 'pt' para melhor resultado. Sotaques muito fortes (acentos regionais) podem exigir modelo 'large'.
  - ⏱️ 8 minutos de leitura | 👤 OpenAI Whisper Docs

## Automação Avançada: Scripts e Integração com Aplicações (`⏱️ 1.5 horas`)
**🎯 Meta da Etapa:** Usar BUZZ via CLI (linha de comando) e API para automatizar transcrição em lote, integrar com workflows (Zapier, n8n), e criar pipelines de processamento.

- [ ] **[BUZZ CLI: Transcrever do Terminal (Batch Processing)](https://github.com/chidiwilliams/buzz#cli-usage)** (`Tutorial Técnico` - `[T13]`)
  - 💡 **O que você aprende:** buzz-cli input.wav -o output.txt → transcreve via terminal. Útil para scripts: bash loop sobre 100 arquivos e transcreve todos em paralelo. Exemplo: for f in *.wav; do buzz-cli $f -o ${f%.wav}.txt; done
  - ⏱️ 15 minutos | 👤 Arsenal Open Source

- [ ] **[API REST de BUZZ: Automação Programática](https://github.com/chidiwilliams/buzz#api)** (`Documentação` - `[T14]`)
  - 💡 **O que você aprende:** POST /api/transcribe com multipart/form-data (arquivo). Retorna job_id. GET /api/status/{job_id} verifica progresso. GET /api/result/{job_id} baixa transcrição. Exemplo curl: curl -F 'audio=@file.wav' http://localhost:8000/api/transcribe
  - ⏱️ 20 minutos | 👤 BUZZ API Docs

- [ ] **[Integração com Zapier/n8n: Workflows Sem Código](https://zapier.com/apps/integrations)** (`Tutorial Step-by-Step` - `[T15]`)
  - 💡 **O que você aprende:** Criar workflow: 'Quando arquivo chega em Google Drive' → 'Transcrever com BUZZ' → 'Salvar resultado em Sheets'. Zapier faz HTTP call para API de BUZZ. n8n é alternativa open source (controle total).
  - ⏱️ 20 minutos | 👤 Comunidade BUZZ

- [ ] **[Exemplo Prático: Transcrever Gravações de Zoom Automaticamente](https://github.com/chidiwilliams/buzz#use-case-zoom)** (`Case Study` - `[T16]`)
  - 💡 **O que você aprende:** Setup: Zoom salva gravação em pasta compartilhada. Script monitora a pasta (inotifywait). Quando novo arquivo aparece, chama 'buzz-cli'. Resultado fica em outra pasta. Automático 100%.
  - ⏱️ 15 minutos | 👤 Arsenal Open Source

## Operação e Manutenção: Keeping BUZZ Running 24/7 (`⏱️ 1 hora`)
**🎯 Meta da Etapa:** Monitorar saúde de BUZZ, resolver problemas comuns, atualizar Whisper model, fazer backups de transcrições, e escalar recursos conforme necessário.

- [ ] **[Monitoramento: Verificar Status Diariamente](https://github.com/chidiwilliams/buzz#monitoring)** (`Checklist Diário` - `[T17]`)
  - 💡 **O que você aprende:** Comando diário: systemctl status buzz (rodando?). df -h (disco cheio?). free -m (memória OK?). tail -20 /var/log/buzz/buzz.log (erros?). Se tudo verde, está bem.
  - ⏱️ 5 minutos | 👤 Arsenal Open Source

- [ ] **[Troubleshooting: Problemas Comuns e Soluções](file:///output/03-manuais-e-trilhas/standalone/buzz/manuais/manual-buzz-vps-e-uso.html#troubleshooting)** (`FAQ Técnico` - `[T18]`)
  - 💡 **O que você aprende:** BUZZ lento: reduzir modelo (base em vez de large). Upload falha: aumentar LimitRequestBody do Apache. Erro 'Out of Memory': aumentar RAM ou ativar swap. Transcrição com erro: melhorar qualidade do áudio com ffmpeg.
  - ⏱️ 15 minutos | 👤 Arsenal Open Source

- [ ] **[Backup de Transcrições: Proteger Dados](https://github.com/chidiwilliams/buzz#backup)** (`Guia de Backup` - `[T19]`)
  - 💡 **O que você aprende:** Script diário: tar -czf ~/buzz_backup_$(date +%Y%m%d).tar.gz /var/lib/buzz/transcriptions/. Enviar para S3/OneDrive/Backblaze (opcional). Manter últimos 30 dias. Protege contra perda de dados.
  - ⏱️ 10 minutos | 👤 Arsenal Open Source

- [ ] **[Atualizar BUZZ e Whisper Model](https://github.com/chidiwilliams/buzz#updating)** (`Guia de Manutenção` - `[T20]`)
  - 💡 **O que você aprende:** BUZZ atualização: cd /var/www/buzz && git pull origin main. Whisper model atualização: pip install --upgrade openai-whisper. Testar com áudio antes de usar em produção. Restart BUZZ: systemctl restart buzz.
  - ⏱️ 10 minutos | 👤 BUZZ Community
