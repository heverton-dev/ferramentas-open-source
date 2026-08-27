# 🔧 Camada 4: TOOLS (MCP Servers & Deterministic Execution)

> **Papel no Estúdio:** Os Pedais de Efeitos, Instrumentos e Processadores (O braço determinístico que conecta o raciocínio ao mundo real).  
> **Status:** 100% CONCLUÍDO & BLINDADO ✅  
> **Unidade de Trabalho:** Servidores MCP (Model Context Protocol), Banco de Estado SQLite (R11), APIs externas e Scripts Python com saída determinística.  
> **Localização:** `4-camadas/04-CAMADA-TOOLS.md`  
> **Auditor Mecânico:** `scripts/auditar_camada_tools.py` (Retorno: `exit 0`)

---

## 🏛️ Os Princípios Universais & Imutáveis da Camada TOOLS

A **Camada TOOLS** é a âncora determinística da Fábrica. Ela é governada por três princípios imutáveis de engenharia de software:

### 1. Princípio da Separação de Responsabilidades (*LLM Pensa, Tool Executa*)
* **A Lei:** Modelos de linguagem são motores estocásticos (probabilísticos); eles são péssimos em matemática exata, contagem precisa, manipulação de binários e validação criptográfica. Ferramentas determinísticas de computador são perfeitas nessas tarefas.
* **Aplicação Prática:** A IA nunca deve tentar adivinhar a quantidade de itens, calcular hashes ou validar regras em prosa. Ela deve invocar uma ferramenta (*script / MCP tool*) e apenas interpretar o código de retorno binário (`exit 0/1`).

### 2. Princípio da Idempotência Algorítmica (*f(f(x)) = f(x)*)
* **A Lei:** Qualquer ferramenta ou script de saneamento deve produzir o mesmo estado final estável se for executado 1 vez ou 1.000 vezes consecutivas, sem gerar efeitos colaterais cumulativos ou corromper o disco.
* **Aplicação Prática:** O script `scripts/limpar_entulho.py` pode ser chamado a qualquer momento: ele sempre limpa apenas o que for lixo e sempre espelha exatamente a verdade atual sem duplicar dados.

### 3. Princípio da Paridade de Hash & Auditoria Criptográfica (*Cryptographic Integrity*)
* **A Lei:** Documentação e código espelhado não podem divergir silenciosamente. A confiança de um sistema de entrega depende de provas matemáticas de integridade de dados.
* **Aplicação Prática:** O Gate R18 calcula hashes MD5 de todos os arquivos de saída e publicação (`output/` vs `docs/`). Se houver qualquer divergência de 1 byte, o sistema bloqueia a esteira compulsoriamente.

---

## 1. O Que Foi Feito

Nesta camada, estruturamos e blindamos a usina mecânica de ferramentas determinísticas e o banco de estado de longo prazo:
1. **Módulo de Estado Persistente da Esteira em SQLite (`scripts/estado_esteira.py` - Regra R11):**
   * Banco de dados relacional local (`estado_esteira.db`) que rastreia sessões de trabalho, histórico de execuções de gates e status de ferramentas catalogadas de forma auditável e imutável.
2. **Declaração Formal de MCP Servers (`.mcp.json`):**
   * Configuração de servidores locais como `db_state_esteira` e `file_validator` para interoperabilidade nativa com qualquer agente moderno.
3. **Usina Completa de Scripts Determinísticos de Auditoria:**
   * `auditar_higiene_repo.py`: Auditor criptográfico de hash MD5 e ausência de entulho (R18).
   * `limpar_entulho.py`: Saneador automático e espelhador em 1 comando.
   * `auditar_r5_dossie.py`: Fiscal de integridade do DOM e Padrão Diamante.
   * `auditar_camada_tela.py`: Gate da Camada 1.
   * `auditar_camada_harness.py`: Gate da Camada 2.
   * `auditar_camada_llm.py`: Gate da Camada 3.
   * `auditar_camada_tools.py`: Gate da Camada 4.
4. **Super-Auditor Geral das 4 Camadas (`scripts/auditar_todas_camadas.py`):**
   * Encadeia os 4 gates mecânicos e emite o Certificado de 100% de Maturidade Industrial.

---

## 2. Por Que Foi Feito

* **A Dor Resolvida (Alucinação de Verificação):** Sem scripts determinísticos, a IA afirma que um arquivo está correto quando na verdade faltam tags HTML ou campos JSON.
* **O Risco Mitigado (Perda de Histórico entre Sessões):** Sem o banco SQLite R11, ao fechar a conversa do chat, todo o contexto de auditorias e erros passados seria perdido.
* **O Ganho de Confiabilidade:** Os commits e deploys passam a ter garantia matemática de integridade comprovada por código de saída `exit 0`.

---

## 3. Onde Foi Feito

Todos os artefatos da Camada 4 residem nos seguintes caminhos físicos:

```
seu-projeto/
├── .mcp.json                     ← Configuração e Declaração de Servidores MCP
├── estado_esteira.db             ← Banco de Dados Relacional SQLite de Estado (R11)
└── scripts/
    ├── estado_esteira.py         ← Módulo SQLite de Leitura/Escrita de Estado
    ├── auditar_higiene_repo.py   ← Gate Criptográfico R18 (Hash MD5)
    ├── limpar_entulho.py         ← Saneador Automático Idempotente
    ├── auditar_r5_dossie.py      ← Fiscal de DOM HTML
    ├── auditar_camada_tools.py   ← Gate Mecânico da Camada 4
    └── auditar_todas_camadas.py  ← Super-Auditor Holístico das 4 Camadas
```

---

## 4. Como Foi Feito

### 4.1 A Estrutura do Banco SQLite (`scripts/estado_esteira.py`)
Cria automaticamente as tabelas relacionais:
```sql
CREATE TABLE IF NOT EXISTS sessoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data TEXT NOT NULL,
    tema TEXT NOT NULL,
    status TEXT NOT NULL,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS auditorias_gates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    camada TEXT NOT NULL,
    gate_nome TEXT NOT NULL,
    status_saida INTEGER NOT NULL,
    detalhes TEXT,
    executado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 4.2 O Gate Mecânico de TOOLS (`scripts/auditar_camada_tools.py`)
Script Python que valida:
1. Conexão real de leitura e escrita em `estado_esteira.db`.
2. Presença e sintaxe de todos os scripts determinísticos da usina.
3. Presença do arquivo `.mcp.json`.
*Retorno:* `sys.exit(0)` em caso de aprovação ou `sys.exit(1)` em caso de falha.

---

## 5. Como Replicar o Que Foi Feito (Guia Passo a Passo Universal)

Para replicar exatamente a Camada 4 em qualquer projeto:

### Passo 1: Copie o módulo de estado, scripts e configuração MCP
```bash
# Na raiz do seu projeto novo:
mkdir -p scripts
cp fabrica-universal/.mcp.json .
cp fabrica-universal/scripts/estado_esteira.py scripts/
cp fabrica-universal/scripts/auditar_higiene_repo.py scripts/
cp fabrica-universal/scripts/limpar_entulho.py scripts/
cp fabrica-universal/scripts/auditar_camada_tools.py scripts/
cp fabrica-universal/scripts/auditar_todas_camadas.py scripts/
```

### Passo 2: Inicialize o Banco de Estado SQLite R11
```bash
python scripts/estado_esteira.py
```

### Passo 3: Execute a Super-Auditoria das 4 Camadas
```bash
python scripts/auditar_todas_camadas.py
```

### Passo 4: Verifique a Saída
Se o terminal exibir:
```text
================================================================================
 📊 QUADRO FINAL DE CONFORMIDADE DAS 4 CAMADAS:
================================================================================
  -> CAMADA 1: TELA            ✅ 100% APROVADO
  -> CAMADA 2: HARNESS         ✅ 100% APROVADO
  -> CAMADA 3: LLM             ✅ 100% APROVADO
  -> CAMADA 4: TOOLS           ✅ 100% APROVADO
================================================================================
 🏆 CERTIFICADO EMITIDO: TODAS AS 4 CAMADAS ESTÃO EM 100% DE MATURIDADE!
================================================================================
```
O seu projeto atingiu oficialmente **100% DE MATURIDADE INDUSTRIAL EM TODAS AS 4 CAMADAS**.
