# 🎛️ Camada 1: TELA (Prompt & Context Engineering)

> **Papel no Estúdio:** O Mixer.  
> **Status:** 100% CONCLUÍDO & BLINDADO ✅  
> **Unidade de Trabalho:** Mensagens, Prompts de Sistema, Context Window, Regras e Skills.  
> **Localização:** `4-camadas/01-CAMADA-TELA.md`  
> **Auditor Mecânico:** `scripts/auditar_camada_tela.py` (Exit 0)

---

## 1. O Que É e Por Que Importa

A **Camada TELA** é a camada mais interna e de contato direto com o modelo. Ela define **o que a IA vê a cada iteração** e **como ela deve se comportar**.
Se a TELA estiver mal configurada, o modelo gastará rios de dinheiro com conversas prolixas, esquecerá instruções no meio do caminho ou alucinará decisões.

---

## 2. As 4 Blindagens Implementadas para Atingir 100%

### 2.1 A Constituição Mestre (`.claude/CLAUDE.md`)
* **Fonte Única:** Todas as regras residem exclusivamente em `.claude/CLAUDE.md`.
* **As 18 Regras Universais (R1 a R18):**
  * **R1:** Idioma estrito (PT-BR).
  * **R2:** Silenciamento de preâmbulos e saudações.
  * **R3/R4:** Autonomia e auto-correção interna antes da entrega.
  * **R5:** Padrão Diamante / Dossiê Executivo (4 seções verticais, 3 passos em mini-cards, sem `div.cols`).
  * **R6:** Modelo livre (`model: inherit`).
  * **R7:** Fidelidade absoluta do conteúdo de entrega.
  * **R8/R9:** Determinismo primeiro e gates mecânicos com retorno `exit 0/1`.
  * **R10/R11:** Idempotência e estado em disco versionável.
  * **R12/R13/R14:** Registro declarativo único, sem prefixo `_`, caminhos curtos (<260 chars).
  * **R15/R16:** Bloqueio de segredos e proibição de commits com testes vermelhos.
  * **R17:** Etapas opcionais nunca travam o fluxo.
  * **R18:** Higiene contínua, zero arquivos temporários e paridade estrita de espelhos.

### 2.2 As 5 Skills Fundamentais de Economia Severa (Seção 0)
1. **`caveman`:** Reduz até 90% do raciocínio interno (`<thought>`) via pensamento telegráfico de homem das cavernas.
2. **`headroom`:** Corta logs gigantes de terminal mantendo apenas 3 linhas no topo e 4 no final.
3. **`lean-ctx`:** Força o uso de `grep` antes da leitura de arquivos, evitando ler arquivos inteiros.
4. **`rtk-memory`:** Congela o arquivo de governança para obter até 90% de desconto em *Prompt Caching*, jogando aprendizados para `RTK-SCRATCHPAD.md`.
5. **`pre-flight-check`:** Checklist de 3 perguntas antes de iniciar refatorações.

### 2.3 Vocabulário Controlado & Lista de Termos Proibidos
* Banimento absoluto de clichês de IA (*"como uma IA"*, *"espero ter ajudado"*, *"com certeza"*, *"certamente"*).
* Respostas 100% técnicas, densas e diretas ao ponto.

### 2.4 Memória Persistente Externa (`RTK-SCRATCHPAD.md`)
* Mantém o prefixo de cache imutável e salva decisões/aprendizados em disco. A TELA lê apenas os últimos 5 aprendizados sob demanda.

### 2.5 Gate Mecânico da TELA (`scripts/auditar_camada_tela.py`)
* Validador determinístico que garante que a TELA não estoure o orçamento de cache (<2.500 palavras) e cumpra todas as regras.

---

## 3. Como Replicar a Camada 1 em Qualquer Projeto Novo

```bash
# 1. Copiar a pasta de governança e memória
cp -r fabrica-universal/.claude/ .
cp fabrica-universal/RTK-SCRATCHPAD.md .

# 2. Copiar o auditor da TELA
cp fabrica-universal/scripts/auditar_camada_tela.py scripts/

# 3. Validar a Camada 1
python scripts/auditar_camada_tela.py
# -> Saída: Exit 0 (Aprovado)
```
