# 🏛️ Manual de Arquitetura da Fábrica Universal
## Governança, Engenharia de 4 Camadas e Padrões Industriais

> **Projeto:** Arsenal Open Source · Fábrica Universal  
> **Versão:** 2.0 (Padrão Diamante Purificado)  
> **Status:** 100% Validado por Gates Mecânicos

---

## 🎯 1. Qual o Foco Principal Desta Arquitetura?

O foco principal é transformar o desenvolvimento de software assistido por IA em uma **esteira industrial previsível, de custo ultra-baixo e soberana**.

Em vez de depender de copilotos caros ou prompts informais que alucinam, a Fábrica Universal se apoia em 4 pilares:
1. **Economia Extrema de Tokens (50% a 90% de redução):** Prompts enxutos (*Caveman*), compressão de logs (*Headroom*), leitura cirúrgica de código (*Lean-CTX*) e memória em cache (*RTK*).
2. **Determinismo Mecânico sobre Alucinação:** Se uma regra de qualidade pode virar um script Python, ela vira script com retorno `exit 0` (aprovado) ou `exit 1` (bloqueia o commit).
3. **Portabilidade Multi-IDE Absoluta:** Uma única fonte da verdade (`.claude/`) espelhada automaticamente para **Claude Code, Cursor, Windsurf, VS Code, Cline e OpenCode**.
4. **Higiene Contínua (Regra R18):** O próprio Git impede a entrada de arquivos temporários, scripts descartáveis ou espelhos dessincronizados.

---

## 🏗️ 2. Como o Projeto Está Estruturado?

```
seu-projeto/
├── .claude/                      ← [FONTE ÚNICA] Governança (CLAUDE.md), RTK.md, Skills e Subagentes
├── scripts/                      ← [USINA MECÂNICA] Hooks pre-commit, auditores R5/R18 e templates
│   ├── hooks/pre-commit          ← Gate Git: bloqueia segredos, testes vermelhos e entulho
│   ├── auditar_higiene_repo.py   ← Validador de integridade e paridade de hash
│   ├── auditar_todas_camadas.py  ← Super-Auditor Geral das 4 Camadas
│   └── limpar_entulho.py         ← Saneador automático em 1 comando
├── output/ & docs/               ← [CAMADA DE ENTREGA] 49 Compêndios Técnicos no Padrão Diamante
└── AGENTS.md, .cursor/, etc.     ← [ESPELHOS GERADOS] Atualizados automaticamente via setup-links
```

---

## ⚖️ 3. Prós e Contras Desta Arquitetura

### 🟢 Prós (Vantagens Competitivas)
* **Economia Financeira Massiva:** Redução drástica nas faturas de LLMs por mês.
* **Blindagem Contra Código Quebrado:** O `pre-commit` bloqueia qualquer tentativa de comitar código com falhas.
* **Zero Vendor Lock-in de IDE:** Troque de editor a qualquer momento sem reescrever suas instruções.
* **Repositório Perpétuamente Limpo:** A regra R18 elimina o acúmulo de scripts descartáveis e lixo técnico.
* **Design Editorial Diamante:** Entregas visuais padronizadas com tipografia justificada e passos acionáveis.

### 🔴 Contras (Trade-offs & Pontos de Atenção)
* **Disciplina Estrita no Commit:** Não é possível fazer commits rápidos sem passar pelos testes e auditores.
* **Permissões no Windows:** A geração de links simbólicos exige Modo Desenvolvedor ou permissão de Administrador no PowerShell.
* **Regra da Fonte Única:** Deve-se sempre editar `.claude/CLAUDE.md` e nunca os arquivos espelhados diretamente.

---

## 🚀 4. Como Usar em Projetos Novos ou Existentes

### 📦 Caso A: Projeto Novo em 5 Minutos
```bash
# 1. Iniciar repositório
mkdir meu-projeto && cd meu-projeto && git init

# 2. Adicionar a Fábrica Universal como Submodule
git submodule add https://github.com/Heverton-web/fabrica-universal.git fabrica-universal
git submodule update --init --recursive

# 3. Copiar infraestrutura base
cp -r fabrica-universal/.claude .
cp fabrica-universal/RTK-SCRATCHPAD.md .
cp fabrica-universal/.mcp.json .
mkdir -p scripts && cp -r fabrica-universal/scripts/* scripts/

# 4. Gerar links de portabilidade e instalar pre-commit hook
powershell .\scripts\setup-links.ps1 meu-projeto   # Linux/Mac: bash scripts/setup-links.sh meu-projeto
```

### 🔧 Caso B: Adequar Projeto Já Existente (Brownfield)
1. Copie a pasta de skills (`fabrica-universal/.claude/skills/`).
2. Adicione a **Seção 0 de Economia** e as regras **R1 a R18 purificadas** ao seu `CLAUDE.md`.
3. Adicione `scripts/auditar_higiene_repo.py` e ative o hook `scripts/hooks/pre-commit`.
4. Execute `python scripts/limpar_entulho.py` para validar a higiene.
