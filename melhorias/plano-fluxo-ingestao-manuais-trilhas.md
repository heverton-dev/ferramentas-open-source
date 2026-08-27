# Plano de Arquitetura & Ação Aprimorado: Fluxo de Ingestão Exaustiva, Manuais Operacionais e Trilhas de Aprendizado

> **Status do Documento:** Proposta Técnica & Arquitetura Aprimorada (Versão 2.0)  
> **Classificação:** Governança Agêntica · Fábrica Universal · Padrão Diamante  
> **Destino:** `melhoria/` e `melhorias/` (Formatos `.md` e `.pdf`)  
> **Casos Piloto de Referência:**  
> - *Ingestão & Desmantelamento:* Granola (`vert-granola` ➔ Quinteto de Reuniões & Transcrição Soberana)  
> - *Motores de Compilação & DTP:* Adobe InDesign (`vert-indesign` ➔ Quinteto Soberano de Diagramação Aberta: Typst, WeasyPrint, Paged.js, Marp, Scribus)

---

## 1. Declaração de Entendimento da Proposta & Aprimoramentos

A proposta aprimorada consolida a transformação de qualquer dossiê vertical de desmantelamento SaaS em **duas entregas mestras corporativas prontas para produção**, agora com flexibilidade total de escopo, política rigorosa de zero download de mídias pesadas e matriz especializada de motores de compilação multi-formato.

```
┌────────────────────────────────────────────────────────────────────────┐
│ 1. SELEÇÃO DE ESCOPO DUAL (SaaS Alvo, ex: Granola)                    │
│    ├─► MODO CIRÚRGICO (Interativo): Menu exibe as 5 opções do Quinteto │
│    │   e o operador escolhe 1 ferramenta específica                   │
│    └─► MODO QUINTETO COMPLETO (Batch): Gera os materiais das 5 em lote │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ 2. CRAWLER HIERÁRQUICO COM ZERO DOWNLOAD PESADO                        │
│    - 1º Docs Oficiais ➔ 2º Livros/Ebooks ➔ 3º YouTube ➔ 4º Cursos      │
│    - NÃO baixa vídeos (.mp4) nem áudios (.mp3)                         │
│    - Extrai apenas metadados, capítulos e transcrições textuais leves  │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ 3. SUMÁRIO ESTRUTURADO EM JSON (Economia Severa de Tokens - LeanCTX)  │
│    - Chunking semântico por tópicos: Instalação VPS vs Uso Exaustivo   │
│    - Âncoras imutáveis de fontes [F01, F02, ... Fn]                    │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                  ┌─────────────────┴─────────────────┐
                  ▼                                   ▼
┌───────────────────────────────────┐ ┌───────────────────────────────────┐
│ MATERIAL 1: GUIA TÉCNICO UNIFICADO│ │ MATERIAL 2: TRILHA CRONOLÓGICA    │
│ 1. Manual de Instalação VPS (Prod)│ │ - Jornada pedagógica cronológica  │
│    Hardening, Docker, SSL, Backup │ │ - Rastreamento direto às fontes   │
│ 2. Manual de Uso Hiperdetalhado   │ │ - Metadados, tempo e formato      │
│    Todas as funções, CLI, API, MCP│ │ - Checkboxes de progresso         │
│ 3. Referências Bibliográficas [Fn]│ └───────────────────────────────────┘
│    Auditáveis (HTTP 200 ativo)    │
└─────────────────┬─────────────────┘
                  │
                  ▼
┌────────────────────────────────────────────────────────────────────────┐
│ 4. GATES MECÂNICOS & MATRIZ DE COMPILAÇÃO DTP (Baseado em InDesign)    │
│    - Gates: auditar_fontes_veridicas.py & auditar_citacoes_manuais.py  │
│    - Motores: Typst (PDF Livro/Tese) + Padrão Diamante HTML + Marp     │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Os Três Grandes Aprimoramentos da Arquitetura

### Aprimoramento 1: Escopo Dual de Cobertura (Cirúrgico vs. Quinteto Completo)
Um SaaS desmantelado possui 5 alternativas no Quinteto Soberano (ex: no Granola temos Screenpipe, Whisper.cpp/LocalWhisper, Buzz, WhisperX, etc.). A esteira agora suporta dois modos operacionais sem duplicar código:

1. **Modo Cirúrgico (Interativo com Prompt ao Operador):**
   - O operador executa `python scripts/gerar_esteira_manuais.py --saas granola`.
   - O sistema carrega `scripts/data/dossie-vertical-granola.json`, extrai os 5 membros do quinteto e renderiza um menu claro no terminal:
     ```
     Dossiê Selecionado: Granola (AI Meeting Notepad)
     [1] Screenpipe (A Mais Completa - Audio & Screen OCR Engine)
     [2] LocalWhisper (A Mais Robusta - Transcrição Contínua de Microfone)
     [3] Buzz (A Mais Moderna - UI Intuitiva & Diarização Local)
     [4] WhisperX (A Mais Leve - Alinhamento Fonético em Milissegundos)
     [5] Open-Notes (A Mais Simples - CLI de Notas Offline)
     [T] TODAS AS 5 FERRAMENTAS (Executar o Quinteto Soberano Completo)
     Selecione a opção desejada [1-5 ou T]:
     ```
   - O operador escolhe exatamente o alvo desejado (ou passa via flag CLI: `--ferramenta screenpipe` ou `--modo todas`).
2. **Modo Quinteto Completo (Batch / Lote Idempotente):**
   - Processa as 5 ferramentas em sequência desacoplada.
   - Cada ferramenta gera seu próprio sumário JSON isolado, seu manual operacional duplo e sua trilha de aprendizado, mantendo total rastreabilidade.

---

### Aprimoramento 2: Política de "Zero Download Pesado" & Máxima Higiene (R18)
O usuário determinou expressamente: **não baixar vídeos, áudios ou binários pesados para a máquina**. A extração de inteligência do YouTube e da web segue uma política estrita de consumo de metadados em memória:

| Fonte | O Que NUNCA é Baixado | O Que é Extraído em Memória / Texto Leve |
| :--- | :--- | :--- |
| **YouTube** | Arquivos de vídeo (`.mp4`, `.mkv`, `.webm`) e áudio (`.m4a`, `.mp3`). | - Título, Canal, Data de publicação, URL canônica;<br>- Capítulos oficiais e minutagens (timestamps);<br>- Legendas e transcrições textuais limpas via API (SRT/VTT convertido para texto puro sem tags de formatação). |
| **Docs Oficiais** | Histórico git completo, binários ou releases compiladas. | Clone raso (`--depth 1`) apenas de arquivos textuais (`.md`, `.mdx`, `/docs`, `README.md`, specs OpenAPI). |
| **Livros & E-books** | PDFs de 500 MB com imagens gráficas de alta resolução. | Metadados catalográficos, sumário estruturado (TOC) e trechos textuais públicos sob licença livre. |
| **Cursos Livres** | Videoaulas pesadas de plataformas de streaming. | Ementa, descrição dos módulos, transcrição das lições e exercícios em código. |

**Garantia Técnica:** Nenhum arquivo temporário ou binário de mídia reside no disco. Toda a manipulação intermediária ocorre em memória e resulta exclusivamente no arquivo leve `scripts/data/sumario-fontes-[slug].json`.

---

### Aprimoramento 3: Integração dos Motores de Compilação (Dossiê InDesign)
A pesquisa na base identificou o compêndio `vert-indesign` (`scripts/data/dossie-vertical-indesign.json`), que cataloga o **Quinteto Soberano de Editoração e Diagramação Aberta**. O fluxo incorpora a inteligência dessas ferramentas para compilar cada formato de documento com a melhor ferramenta de mercado:

```
                  ┌────────────────────────────────────────────────────────┐
                  │          MATRIZ DE MOTORES DE COMPILAÇÃO DTP           │
                  └──────────────────────────┬─────────────────────────────┘
                                             │
      ┌──────────────────────┬───────────────┴──────────────┬──────────────────────┐
      ▼                      ▼                              ▼                      ▼
┌─────────────┐      ┌───────────────┐              ┌───────────────┐      ┌─────────────┐
│    TYPST    │      │  WEASYPRINT   │              │   PAGED.JS    │      │    MARP     │
│ (Rank 2)    │      │   (Rank 3)    │              │   (Rank 4)    │      │  (Rank 5)   │
│ Livros,     │      │ Conversão     │              │ Polyfill CSS  │      │ Manuais em  │
│ Teses e     │      │ HTML5/CSS3    │              │ Paged Media   │      │ Slides e    │
│ Manuais VPS │      │ em PDF de     │              │ no Navegador  │      │ Apostilas   │
│ de Alta     │      │ Impressão     │              │ com Prévia    │      │ Rápidas em  │
│ Velocidade  │      │ Corporativa   │              │ em 2 Páginas  │      │ Markdown    │
└─────────────┘      └───────────────┘              └───────────────┘      └─────────────┘
```

1. **Typst (`rank 2` do dossiê InDesign - A Mais Completa):**
   - **Papel no Fluxo:** Motor oficial para compilar os Manuais de Instalação/Uso e as Trilhas em **PDF Executivo Institucional**.
   - **Vantagem:** Compilação em menos de 50 milissegundos, controle tipográfico impecável de código-fonte, tabelas fluidas, cabeçalhos dinâmicos com contagem de páginas e suporte nativo a equações e caixas de alerta.
2. **WeasyPrint & Paged.js (`ranks 3 e 4` - A Mais Moderna e A Mais Leve):**
   - **Papel no Fluxo:** Renderização em PDF diretamente a partir do HTML do compêndio, utilizando as especificações do W3C para *CSS Paged Media* (`@page`, cabeçalhos alternados pares/ímpares e contadores de seção).
   - **Vantagem:** Permite que o template HTML do manual seja impresso ou exportado para PDF mantendo exatamente a identidade visual corporativa do Design System Diamante.
3. **Marp (`rank 5` - A Mais Simples):**
   - **Papel no Fluxo:** Gerador opcional de **Apostilas de Treinamento Rápido e Slides de Onboarding Corporativo** a partir do Markdown do manual.
   - **Vantagem:** Converte o manual em uma apresentação executiva para reuniões de alinhamento com times de DevOps em segundos com zero configuração.
4. **Template HTML Diamante (Nativo da Fábrica):**
   - **Papel no Fluxo:** Interface de consumo interativo no navegador com Hero Stats Bar, busca instantânea client-side, botões de cópia de comandos bash com 1 clique e design responsivo.

---

## 3. Especificação Detalhada das Entregas

### MATERIAL 1: Guia Técnico Duplo Unificado (Instalação VPS + Manual de Uso)
Arquivo: `output/manuais/manual-[slug]-vps-e-uso.html` (+ cópia espelhada e `.md` + `.pdf` via Typst)

#### Estrutura Obrigatória:
- **Hero Stats Bar & Metadados da VPS:**
  - Versão da ferramenta, data de auditoria, licença OSI, tempo médio de setup (~15 min), complexidade (Intermediária / Avançada);
  - Configuração recomendada da VPS: Hetzner CPX31 / Contabo VPS M (4 vCPU, 8 GB RAM, 160 GB NVMe, Ubuntu 24.04 LTS), custo mensal (~EUR 14/mês).
- **Parte I — Manual de Instalação em Produção na VPS (Passo a Passo Rígido):**
  1. *Hardening do Servidor:* Usuário `deployer`, chave SSH pública, desativação de login por senha (`PasswordAuthentication no`) e firewall UFW configurado (`22/tcp`, `80/tcp`, `443/tcp`).
  2. *Provisionamento de Docker Engine:* Instalação do Docker oficial e plugin Docker Compose V2.
  3. *Estrutura de Diretórios:* Árvore canônica `/opt/[app]/` com permissões `750`.
  4. *Docker Compose de Produção:* Limites de CPU/RAM (`limits: cpus, memory`), restart policy `unless-stopped`, healthcheck e volumes persistentes.
  5. *Template de `.env` Comentado:* Cada variável explicada detalhadamente.
  6. *Reverse Proxy Nginx / Caddy com SSL Let's Encrypt:* Terminação TLS, HTTP/2, cabeçalhos de segurança (HSTS, CSP).
  7. *Serviço Systemd & Inicialização no Boot:* Persistência e tolerância a falhas.
  8. *Healthcheck & Rotina de Backup:* Comandos de verificação de sanidade e script de snapshot diário.
- **Parte II — Manual de Uso Hiperdetalhado & Exaustivo:**
  1. *Arquitetura Operacional:* Fluxo interno de dados (captura, processamento, transcrição, indexação).
  2. *Dicionário Completo de CLI:* Tabela com 100% das flags, argumentos, valores padrão e exemplos práticos.
  3. *Guia de Interface Web / Desktop:* Explicação tela a tela de todas as funções e filtros.
  4. *Referência de API REST / SDK:* Mapeamento de rotas, métodos HTTP, query params e payloads JSON.
  5. *Integração com Servidores MCP:* Configuração com Claude Code, Cursor e Antigravity.
  6. *Matriz de Troubleshooting:* Tabela de 10 problemas comuns com causas prováveis e comandos de correção imediata.
- **Parte III — Referências Bibliográficas Verificáveis:**
  - Tabela com IDs `[F01]`, `[F02]`, título da fonte, autor/canal, URL testada (HTTP 200) e indicação de onde a informação foi utilizada.

---

### MATERIAL 2: Trilha Cronológica de Aprendizado Autoguiado
Arquivo: `output/trilhas/trilha-[slug]-aprendizado.html` (+ cópia espelhada e `.md` + `.pdf` via Typst)

- **Timeline Pedagógica Cronológica:**
  - *Fase 1: Fundamentos & Arquitetura (~45 min)* — Leituras essenciais de documentação e premissas de privacidade;
  - *Fase 2: Instalação & Operação de Base (~1h30)* — Vídeos de setup e tutoriais práticos de deploy;
  - *Fase 3: Domínio de Recursos & Uso Diário (~2h30)* — Guias de interface, flags de CLI e atalhos;
  - *Fase 4: Recursos Avançados, API & Agentes (~2h00)* — Cursos de integração de API e setup de MCP.
- **Cartões de Recurso com Rastreabilidade Total:**
  - Cada cartão contém: Título oficial da fonte, tipo de mídia, autor, duração/tempo de leitura estimado, link direto verificado (HTTP 200), pré-requisitos conceituais e "O que você aprenderá neste conteúdo".
  - Checkboxes interativos no cliente para acompanhamento do progresso de estudo.

---

## 4. Schemas JSON Declarativos

### 4.1. `scripts/schemas/schema_sumario_fontes.json`
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "SumarioFontesPesquisa",
  "type": "object",
  "required": ["produto_foco", "slug", "data_coleta", "fontes"],
  "properties": {
    "produto_foco": { "type": "string" },
    "slug": { "type": "string" },
    "saas_origem": { "type": "string" },
    "data_coleta": { "type": "string" },
    "fontes": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["id", "categoria", "titulo", "url", "status_http", "topicos", "trechos_chave"],
        "properties": {
          "id": { "type": "string", "pattern": "^F[0-9]{2,3}$" },
          "categoria": { "enum": ["documentacao_oficial", "livro_ebook", "youtube", "curso_tutorial"] },
          "titulo": { "type": "string" },
          "url": { "type": "string", "format": "uri" },
          "status_http": { "type": "integer" },
          "autor_ou_canal": { "type": "string" },
          "duracao_ou_paginas": { "type": "string" },
          "topicos": { "type": "array", "items": { "type": "string" } },
          "trechos_chave": {
            "type": "array",
            "items": {
              "type": "object",
              "required": ["topico", "conteudo", "ancora_ou_minutagem"],
              "properties": {
                "topico": { "type": "string" },
                "conteudo": { "type": "string" },
                "ancora_ou_minutagem": { "type": "string" }
              }
            }
          }
        }
      }
    }
  }
}
```

---

## 5. Gates Mecânicos de Validação (R9 / R17)

1. `scripts/auditar_fontes_veridicas.py`: Varredura assíncrona com `aiohttp` disparando requisições `HEAD`/`GET` em todas as URLs. Falhas de HTTP (404, 403, 500 ou conexões mortas) encerram a esteira com `exit 1`.
2. `scripts/auditar_citacoes_manuais.py`: Parser regex que extrai todos os marcadores `[^Fxx]` do manual e valida integridade bidirecional (toda afirmação citada aponta para uma fonte válida e nenhuma fonte fica sem uso).
3. `scripts/auditar_sintaxe_comandos.py`: Validação determinística de sintaxe bash (via `bash -n` ou parser AST) e de arquivos YAML/Compose.

---

## 6. Plano de Ação em 4 Fases para Construção

| Fase | Foco Principal | Atividades Chave | Entregáveis Técnicos |
| :---: | :--- | :--- | :--- |
| **Fase 1** | **Fundação de Schemas & Orquestrador Dual** | 1. Criar `scripts/schemas/schema_sumario_fontes.json`.<br>2. Criar `scripts/schemas/schema_manual_operacional.json`.<br>3. Criar `scripts/schemas/schema_trilha_aprendizado.json`.<br>4. Desenvolver o seletor CLI interativo / batch `scripts/orquestrador_esteira_manuais.py` (menu de 1 a 5 ou Quinteto Completo). | 3 Schemas JSON + Seletor de Escopo Dual CLI. |
| **Fase 2** | **Crawler Leve & Indexador de Tokens** | 1. Desenvolver `scripts/coletar_fontes_pesquisa.py` com extração limpa em memória (zero download de vídeos/áudios).<br>2. Desenvolver `scripts/compilar_sumario_fontes.py` (chunking e indexação em JSON).<br>3. Desenvolver o gate `scripts/auditar_fontes_veridicas.py`.<br>4. Executar coleta no caso piloto Granola (Screenpipe). | Coletor em cascata + Compilador JSON + Gate G1 + `sumario-fontes-screenpipe.json`. |
| **Fase 3** | **Motor de Manuais & Matriz DTP (Typst/HTML)** | 1. Desenvolver template HTML Diamante `scripts/padroes/template_manual_operacional.py`.<br>2. Desenvolver template Typst para compilação instantânea em PDF executivo.<br>3. Desenvolver gerador `scripts/gerar_manual_operacional.py`.<br>4. Desenvolver o gate `scripts/auditar_citacoes_manuais.py`. | Template Diamante + Template Typst + Gerador de Manual + `manual-screenpipe-vps-e-uso.html/.pdf`. |
| **Fase 4** | **Motor da Trilha de Aprendizado & Custódia** | 1. Desenvolver template e gerador `scripts/gerar_trilha_aprendizado.py`.<br>2. Atualizar `scripts/limpar_entulho.py` para espelhamento em `docs/manuais/` e `docs/trilhas/`.<br>3. Testar a geração em lote para as 5 ferramentas do Granola.<br>4. Auditoria final completa (`auditar_todas_camadas.py`). | Trilha HTML/MD/PDF + Suporte a lote para o Quinteto + Espelhamento em `docs/`. |

---

## 7. Decisão & Próximo Passo

O plano contempla 100% dos aprimoramentos solicitados:
- **Seleção de Escopo Flexível:** Opção de gerar para 1 ferramenta via menu interativo ou para as 5 do Quinteto Soberano em lote;
- **Zero Download de Arquivos Pesados:** Extração em memória exclusivamente de texto, metadados e legendas;
- **Matriz de Compilação Profissional:** Integração de Typst (para PDFs de livros/manuais técnicos), HTML Diamante e Marp (para apostilas/slides) inspirada no dossiê InDesign (`vert-indesign`).

**Aguardando autorização do operador para iniciar a Fase 1 (Schemas e Orquestrador Dual).**
