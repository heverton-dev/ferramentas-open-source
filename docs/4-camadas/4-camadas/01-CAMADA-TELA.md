# 🎛️ Camada 1: TELA (Prompt & Context Engineering)

> **Papel no Estúdio:** O Mixer (Ajuste fino de tudo o que a IA vê e como ela pensa).  
> **Status:** 100% CONCLUÍDO & PURIFICADO ✅  
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

## 1. O Que Foi Feito (As 18 Regras Purificadas)

Nesta camada, expurgamos qualquer regra residual de outros contextos e estruturamos a constituição oficial do **Arsenal Open Source**:

| Regra | Nome | O Que Faz na Prática |
| :--- | :--- | :--- |
| **R1** | **Idioma Único (PT-BR)** | Comunicação, documentação e código em português estrito. |
| **R2** | **Silenciamento de Prosa** | Sem preâmbulos vazios ("Com certeza!"). Markdown limpo e executivo. |
| **R3/R4** | **Autonomia & Auto-Correção** | A esteira resolve desvios e corrige erros antes de entregar ao operador. |
| **R5** | **Padrão Dossiê Diamante** | Dossiê visual com Hero Stats, busca interativa, 4 seções verticais nos cards e 3 passos em mini-cards. |
| **R6** | **Modelo Livre** | `model: inherit` — o projeto não fica refém de uma LLM específica. |
| **R7** | **Conteúdo de Entrega Intocável** | Compêndios e catálogos finais nunca são resumidos ou truncados. |
| **R8/R9** | **Determinismo & Gates** | Se um script resolve, não gaste LLM. Gates retornam `exit 0` ou `exit 1`. |
| **R10/R11**| **Idempotência & Estado em Disco**| Scripts podem rodar 1.000 vezes sem quebrar; estado vive em SQLite (`estado_esteira.db`). |
| **R12** | **Registro Declarativo Único** | 1 entrada em `scripts/tipos.py` por novo tipo de documento. |
| **R13** | **Padronização Numérica** | Compêndios numerados sequencialmente (`01` a `49`) com slugs limpos. |
| **R14** | **Caminhos Curtos** | Nomes respeitam o limite de 260 caracteres do Windows (MAX_PATH). |
| **R15/R16**| **Segredos & Testes Verdes** | Git bloqueia chaves de API e proíbe commits com testes quebrados. |
| **R17** | **Integridade de Repositórios** | Toda ferramenta catalogada DEVE possuir licença OSI, SaaS substituído e URL de repositório válida. |
| **R18** | **Higiene & Paridade Estrita** | Zero arquivos temporários (`temp_*`, `.bak`); espelhos com mesmo hash MD5. |

---

## 2. Por Que Foi Feito

* **A Dor Resolvida (Custo & Ruído de Regras Inúteis):** Regras de templates de outros domínios consumiam espaço no prompt e criavam instruções confusas. A purificação alinhou 100% da TELA à missão de custódia e compêndios open source.
* **O Risco Mitigado (Alucinação & Prolixidade):** O vocabulário controlado e as regras limpas garantem foco executivo absoluto.
* **O Ganho Financeiro:** A combinação de *Caveman Thinking*, *Headroom*, *Lean-CTX* e *RTK-Memory* reduz as faturas de LLMs entre **50% e 90%**.

---

## 3. Onde Foi Feito

```
seu-projeto/
├── .claude/
│   ├── CLAUDE.md                 ← A Constituição Mestre Purificada
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
```text
"Pensamento telegráfico (3-5 linhas), sem preâmbulos/saudações.
Abreviar: 'verificar' -> 'ver', 'necessário' -> 'nec.', 'implementar' -> 'impl.'.
Ir direto ao ponto: 'usr quer X. ver arquivo Y. corrigir Z.'."
```

### 4.2 O Código do Gate Mecânico (`scripts/auditar_camada_tela.py`)
Script determinístico que valida:
1. Se `CLAUDE.md` existe e está abaixo de 2.500 palavras para Prompt Caching.
2. Se as 18 regras purificadas (R1 a R18) estão presentes.
3. Se as 5 skills de economia estão intactas.
4. Se o vocabulário controlado está ativo.
*Retorno:* `sys.exit(0)` em caso de aprovação.

---

## 5. Como Replicar o Que Foi Feito (Guia Passo a Passo Universal)

```bash
# 1. Copiar a pasta de governança e memória
cp -r fabrica-universal/.claude/ .
cp fabrica-universal/RTK-SCRATCHPAD.md .
cp fabrica-universal/scripts/auditar_camada_tela.py scripts/

# 2. Executar a auditoria mecânica
python scripts/auditar_camada_tela.py
# -> Saída: Exit 0 (Aprovado)
```
