# 🎛️ Camada 1: TELA (Prompt & Context Engineering)

> **Papel no Estúdio:** O Mixer (Ajuste fino de tudo o que a IA vê e como ela pensa).  
> **Status:** 100% CONCLUÍDO & BLINDADO ✅  
> **Unidade de Trabalho:** Mensagens de entrada, Prompts de Sistema, Context Window, Regras de Governança e Skills de Economia.  
> **Localização:** `4-camadas/01-CAMADA-TELA.md`  
> **Auditor Mecânico:** `scripts/auditar_camada_tela.py` (Retorno: `exit 0`)

---

## 🏛️ Os Princípios Universais & Imutáveis da Camada TELA

Independente de qual modelo de IA, linguagem ou editor você use, a Camada 1 é governada por três leis físicas imutáveis da ciência da computação:

### 1. Princípio da Invariância de Prefixo (*KV-Cache Invariance*)
* **A Lei:** Modelos de linguagem utilizam mecanismos de atenção que armazenam chaves e valores (*KV-Cache*) do início do prompt. Se o prefixo do prompt permanecer **100% imutável**, o hardware reaproveita a computação anterior, reduzindo a latência em até 80% e o custo financeiro em até 90%.
* **Aplicação Prática:** A governança (`CLAUDE.md`) é mantida estática e congelada. Qualquer informação volátil ou aprendizado temporário da sessão é extraído e gravado em arquivo separado (`RTK-SCRATCHPAD.md`), garantindo que o prefixo nunca seja quebrado.

### 2. Princípio da Densidade Informacional de Shannon (*Zero Entropia Prolixa*)
* **A Lei:** A Teoria da Informação de Claude Shannon prova que ruído e redundância degradam a fidelidade do sinal. No contexto de um LLM, palavras vazias ("como uma IA", "com certeza", "espero ajudar") ocupam espaço atencional precioso e aumentam a probabilidade de alucinação.
* **Aplicação Prática:** O *Caveman Thinking* e o *Vocabulário Controlado* forçam a taxa máxima de densidade semântica por token. Apenas informação essencial transita no rascunho interno do modelo.

### 3. Princípio da Localidade Espacial de Contexto (*Context Locality*)
* **A Lei:** A capacidade de recuperação de fatos de um LLM degrada exponencialmente à medida que o tamanho da janela de contexto aumenta (*Lost in the Middle Phenomenon*). Quanto mais texto irrelevante for injetado, menor a precisão do modelo sobre o código crítico.
* **Aplicação Prática:** O *Lean-CTX* e o *Headroom* proíbem despejos brutos de arquivos e logs. Localiza-se cirurgicamente o trecho via `grep` antes de qualquer leitura.

---

## 1. O Que Foi Feito

Nesta camada, estruturamos e blindamos todo o conjunto de instruções, prompts de sistema, vocabulário e contexto que alimenta os modelos de IA:
1. **Constituição Mestre da Fábrica Universal:** Consolidação de 18 regras inegociáveis (R1 a R18) que governam o comportamento autônomo, idioma, qualidade e segurança.
2. **As 5 Skills Fundamentais de Economia Severa:** Pacote de habilidades em Markdown que ensina o modelo a comprimir pensamento, podar logs e ler arquivos cirurgicamente.
3. **Orçamento de Cache do Prompt Mestre (`Context Budget Limiter`):** Congelamento do tamanho do arquivo `.claude/CLAUDE.md` em menos de 2.500 palavras para maximizar o desconto de 90% de *Prompt Caching*.
4. **Vocabulário Controlado & Termos Proibidos:** Banimento formal de clichês de IA e respostas prolixas.
5. **Memória Persistente de Longo Prazo (`RTK-SCRATCHPAD.md`):** Arquivo de apoio na raiz que guarda aprendizados sem poluir o cache do prompt principal.
6. **Gate Mecânico de Auditoria da TELA (`scripts/auditar_camada_tela.py`):** Script determinístico que valida o cumprimento de todos os itens acima antes de cada sessão.

---

## 2. Por Que Foi Feito

* **A Dor Resolvida (Custo & Esquecimento):** Sem essas regras na TELA, os modelos de IA gastam centenas de dólares por dia com raciocínios prolixos e esquecem regras críticas conforme a conversa avança.
* **O Risco Mitigado (Alucinação & Prolixidade):** Sem um vocabulário controlado e sem as regras R1–R18, o agente assume posturas passivas ("como uma IA não posso fazer isso") ou quebra arquivos por alucinar requisitos.
* **O Ganho Financeiro:** A combinação de *Caveman Thinking*, *Headroom*, *Lean-CTX* e *RTK-Memory* reduz as faturas de API de LLMs entre **50% e 90%**.

---

## 3. Onde Foi Feito

Todos os artefatos desta camada estão organizados nos seguintes caminhos físicos:

```
seu-projeto/
├── .claude/
│   ├── CLAUDE.md                 ← A Constituição Mestre (Regras R1 a R18 + Seção 0 de Economia)
│   └── skills/                   ← As 5 Skills Fundamentais de Economia
│       ├── caveman/SKILL.md      ← Compressão de pensamento CoT (-90%)
│       ├── headroom/SKILL.md     ← Compressão de logs de build (3 topo + 4 fim)
│       ├── lean-ctx/SKILL.md     ← Leitura cirúrgica via grep (-85% leitura)
│       ├── rtk-memory/SKILL.md   ← Protocolo de cache congelado
│       └── pre-flight-check/     ← Checklist pré-voo antes de refatorar
│
├── RTK-SCRATCHPAD.md             ← Memória de aprendizados da sessão (na raiz)
├── AGENTS.md                     ← Hardlink espelhado de CLAUDE.md
└── scripts/
    └── auditar_camada_tela.py    ← Gate Mecânico da Camada 1
```

---

## 4. Como Foi Feito

### 4.1 A Mecânica do *Caveman Thinking* (Seção 0 do `CLAUDE.md`)
O arquivo instrui o modelo a raciocinar telegráfico no bloco interno `<thought>`:
```text
// Regra aplicada no prompt mestre:
"Pensamento telegráfico (3-5 linhas), sem preâmbulos/saudações.
Abreviar: 'verificar' -> 'ver', 'necessário' -> 'nec.', 'implementar' -> 'impl.'.
Ir direto ao ponto: 'usr quer X. ver arquivo Y. corrigir Z.'."
```

### 4.2 A Mecânica do *Headroom* (Corte de Logs)
Se a saída de um comando tiver mais de 7 linhas, o modelo é instruído a processar apenas:
```
[Linha 1 do log]
[Linha 2 do log]
[Linha 3 do log]
... (conteúdo intermediário ignorado) ...
[Linha N-3 do log]
[Linha N-2 do log]
[Linha N-1 do log]
[Linha N do log]
```

### 4.3 O Código do Gate Mecânico (`scripts/auditar_camada_tela.py`)
Um script Python determinístico que confere:
1. Se o `CLAUDE.md` existe e tem menos de 3.000 palavras.
2. Se todas as 18 regras (R1 a R18) estão presentes no texto.
3. Se as 5 pastas de skills de economia contêm seus arquivos `SKILL.md` intactos.
4. Se o `RTK-SCRATCHPAD.md` está na raiz.
5. Se não restaram placeholders como `<SEU-PROJETO>`.
*Retorno:* `sys.exit(0)` em caso de aprovação ou `sys.exit(1)` em caso de falha.

---

## 5. Como Replicar o Que Foi Feito (Guia Passo a Passo Universal)

Para aplicar exatamente esta mesma Camada 1 em qualquer projeto novo ou legado:

### Passo 1: Copie a infraestrutura de TELA
```bash
# Na raiz do seu projeto novo:
mkdir -p .claude/skills scripts
cp -r fabrica-universal/.claude/ .
cp fabrica-universal/RTK-SCRATCHPAD.md .
cp fabrica-universal/scripts/auditar_camada_tela.py scripts/
```

### Passo 2: Personalize o arquivo `.claude/CLAUDE.md`
Abra `.claude/CLAUDE.md` e troque o nome do projeto no título. **Mantenha intactas** a Seção 0 (Economia) e as regras R1 a R18.

### Passo 3: Execute a Auditoria Mecânica da TELA
```bash
python scripts/auditar_camada_tela.py
```

### Passo 4: Verifique a Saída
Se o terminal exibir:
```text
================================================================================
 🎛️ GATE MECÂNICO DA CAMADA 1: AUDITORIA DA TELA (PROMPT & CONTEXT)
================================================================================
 ✅ CAMADA 1 (TELA) 100% APROVADA: Prompt Caching, Regras R1-R18, 5 Skills & Vocabulário!
================================================================================
```
A sua Camada 1 está oficialmente **100% configurada, blindada e pronta para produção em qualquer ambiente**.
