# 📖 O Livro da Fábrica Universal
## Guia Definitivo de Arquitetura Agêntica, Soberania Tecnológica e Engenharia com IA

> **Autor:** Fábrica Universal  
> **Público:** Desenvolvedores iniciantes, engenheiros seniores, arquitetos de software e gestores de tecnologia.  
> **Pré-requisitos:** Nenhum. Todos os conceitos são explicados do zero com analogias simples do dia a dia.

---

# 📑 Sumário

1. [Prefácio: Por Que a Fábrica Universal Existe?](#prefácio-por-que-a-fábrica-universal-existe)
2. [O Dicionário do Iniciante (Glossário Descomplicado)](#o-dicionário-do-iniciante-glossário-descomplicado)
3. [Capítulo 1: O Motor de Economia Severa de Tokens](#capítulo-1-o-motor-de-economia-severa-de-tokens)
   - 1.1 O Que São Tokens e Por Que Eles Custam Tão Caro?
   - 1.2 Técnica 1: *Caveman Thinking* (Pensamento Telegráfico)
   - 1.3 Técnica 2: *Headroom* (Compressão Inteligente de Logs)
   - 1.4 Técnica 3: *Lean-CTX* (Leitura Cirúrgica de Código)
   - 1.5 Técnica 4: *RTK-Memory* (Memória Estável e Aproveitamento de Cache)
   - 1.6 Técnica 5: *Pre-Flight Check* (A Lista de Verificação Pré-Voo)
4. [Capítulo 2: As 18 Leis Sagradas da Governança Purificada (R1 a R18)](#capítulo-2-as-18-leis-sagradas-da-governança-purificada-r1-a-r18)
5. [Capítulo 3: A Usina de Scripts Determinísticos (`scripts/`)](#capítulo-3-a-usina-de-scripts-determinísticos-scripts)
6. [Capítulo 4: Configurações & A Mágica da Portabilidade Multi-IDE](#capítulo-4-configurações--a-mágica-da-portabilidade-multi-ide)
7. [Capítulo 5: O Padrão Visual Diamante & Dossiê Executivo (Regra R5)](#capítulo-5-o-padrão-visual-diamante--dossiê-executivo-regra-r5)
8. [Capítulo 6: Manual Prático de Implementação (Projetos Novos & Existentes)](#capítulo-6-manual-prático-de-implementação-projetos-novos--existentes)

---

# Prefácio: Por Que a Fábrica Universal Existe?

Imagine que você contratou um assistente muito inteligente para ajudá-lo a construir uma casa. Porém, esse assistente tem três manias perigosas:
1. **Ele cobra por cada palavra que lê e por cada palavra que pensa**, mesmo quando pensa em silêncio. Se ele pensar enrolado, sua conta bancária é esvaziada em minutos.
2. **Ele é esquecido.** Conforme o dia passa e a conversa fica longa, ele começa a esquecer o que combinou no início da manhã.
3. **Ele sofre de excesso de confiança (alucinação).** Às vezes, ele afirma com certeza absoluta que colocou a viga no lugar certo, mas na verdade a viga nem existe.

A **Fábrica Universal** nasceu para resolver exatamente esses três problemas no desenvolvimento de software com Inteligência Artificial (chamado de **AIDD** ou *AI-Driven Development*).

---

# O Dicionário do Iniciante (Glossário Descomplicado)

* **IA / LLM:** O cérebro da máquina que processa tokens.
* **Token:** O combustível cobrado (~4 letras por token).
* **Contexto:** A memória de curto prazo da IA.
* **KV-Cache (Prompt Caching):** Desconto de até 90% ao manter o início das instruções 100% congelado.
* **Pre-Commit Hook:** O guarda-costas digital do Git que inspeciona o código antes de salvar.
* **Exit Code (0 ou 1):** A linguagem do sistema operacional (`exit 0` = aprovado, `exit 1` = erro).
* **Hardlink / Junction:** Portais mágicos do sistema de arquivos para sincronização atômica entre IDEs.

---

# Capítulo 1: O Motor de Economia Severa de Tokens

1. **Caveman Thinking:** Pensamento telegráfico no rascunho interno (`<thought>`). Economiza até 90% sem degradar a resposta final.
2. **Headroom:** Compressão de logs gigantes de terminal (3 topo + 4 fim).
3. **Lean-CTX:** Leitura cirúrgica via `grep` antes de abrir arquivos.
4. **RTK-Memory:** Prompt mestre congelado e aprendizados em `RTK-SCRATCHPAD.md`.
5. **Pre-Flight Check:** Checklist de 3 perguntas antes de refatorar.

---

# Capítulo 2: As 18 Leis Sagradas da Governança Purificada (R1 a R18)

| Regra | Nome | O Que Significa na Prática |
| :--- | :--- | :--- |
| **R1** | **Idioma Único (PT-BR)** | Todo o pensamento, documentação e código devem ser em português do Brasil. |
| **R2** | **Silenciamento de Prosa** | Sem introduções vazias ("Com certeza!"). Markdown limpo e direto. |
| **R3/R4** | **Autonomia & Auto-Correção** | A esteira resolve desvios e corrige erros antes de entregar ao operador. |
| **R5** | **Padrão Dossiê Diamante** | Dossiê visual com Hero Stats, busca interativa, 4 seções verticais e 3 passos em mini-cards. |
| **R6** | **Modelo Livre** | `model: inherit` — nenhum modelo LLM fixo amarrado ao projeto. |
| **R7** | **Conteúdo de Entrega Intocável** | Compêndios e dados de saída nunca são resumidos ou truncados. |
| **R8/R9** | **Determinismo & Gates** | Se um script resolve, não gaste LLM. Gates mecânicos retornam `exit 0` ou `exit 1`. |
| **R10/R11**| **Idempotência & Estado em Disco**| Scripts rodam N vezes sem corromper; estado vive em SQLite (`estado_esteira.db`). |
| **R12** | **Registro Declarativo Único** | Adicionar um novo tipo custa 1 entrada em `scripts/tipos.py`. |
| **R13** | **Padronização Numérica** | Compêndios numerados sequencialmente (`01` a `49`) com slugs limpos. |
| **R14** | **Caminhos Curtos** | Nomes respeitam o limite de 260 caracteres do Windows (MAX_PATH). |
| **R15/R16**| **Segredos & Testes Verdes** | Git bloqueia chaves de API e proíbe commits com testes quebrados. |
| **R17** | **Integridade de Repositórios** | Toda ferramenta possui licença OSI, SaaS substituído e URL de repositório válida. |
| **R18** | **Higiene & Paridade Estrita** | Zero arquivos temporários (`temp_*`, `.bak`); espelhos com mesmo hash MD5. |

---

# Capítulo 3: A Usina de Scripts Determinísticos (`scripts/`)

* `scripts/hooks/pre-commit`: O fiscal do Git com 6 gates de proteção.
* `scripts/auditar_higiene_repo.py`: Auditor criptográfico de hash MD5 (R18).
* `scripts/limpar_entulho.py`: Saneador automático e espelhador em 1 comando.
* `scripts/auditar_r5_dossie.py`: Fiscal de conformidade do Padrão Diamante.
* `scripts/estado_esteira.py`: Banco de dados relacional SQLite de Estado (R11).
* `scripts/auditar_todas_camadas.py`: Super-Auditor Geral das 4 Camadas.

---

# Capítulo 4: Configurações & A Mágica da Portabilidade Multi-IDE

A governança vive exclusivamente em `.claude/CLAUDE.md`. O script `setup-links` cria Hardlinks diretos para que Cursor, Windsurf, Cline, VS Code e Copilot leiam exatamente a mesma regra no disco físico sem duplicação.

---

# Capítulo 5: O Padrão Visual Diamante & Dossiê Executivo (Regra R5)

Estrutura canônica de um card de ferramenta:
1. **Cabeçalho & Badges:** Rank, nome, senioridade, SaaS substituído, ROI e licença OSI.
2. **Seção 1 (O Que Faz & Como Funciona):** Explicação clara + bloco de código executável com botão "Copiar".
3. **Seção 2 (Análise Econômica & ROI):** SaaS eliminados e valor economizado por ano.
4. **Seção 3 (Requisitos de Infraestrutura & Veredito):** Consumo real de RAM/CPU e link do repositório.
5. **Seção 4 (Como Usar no Dia a Dia):** Grid visual com 3 mini-cards práticos (`[1] Configuração`, `[2] Operação`, `[3] Resultado`).

---

# Capítulo 6: Manual Prático de Implementação

```bash
# 1. Iniciar repositório Git
mkdir meu-projeto && cd meu-projeto && git init

# 2. Adicionar o submódulo da Fábrica Universal
git submodule add https://github.com/Heverton-web/fabrica-universal.git fabrica-universal
git submodule update --init --recursive

# 3. Copiar governança e scripts
cp -r fabrica-universal/.claude .
cp fabrica-universal/RTK-SCRATCHPAD.md .
cp fabrica-universal/.mcp.json .
mkdir -p scripts && cp -r fabrica-universal/scripts/* scripts/

# 4. Criar links e instalar o hook de proteção
powershell .\scripts\setup-links.ps1 meu-projeto   # Linux: bash scripts/setup-links.sh meu-projeto

# 5. Executar a Super-Auditoria
python scripts/auditar_todas_camadas.py
```

---
*Fim do Livro da Fábrica Universal · Versão 2.0 Purificada.*
