# 06 · Regras de Execução (Fluxo 4: Macro-Ecossistemas)

> **Módulo:** Fluxo 4 — Macro-Ecossistemas e Suítes Integradas

---

## 1. Regras Globais (CLAUDE.md)

Todas as regras de `CLAUDE.md` se aplicam. Específicas para Fluxo 4:

- **R5-E (Padrão Diamante Estendido):** Obrigatório em todo HTML gerado;
- **R13 (Taxonomia):** Slugs `ecos-<slug>`, máximo 35 caracteres;
- **R18 (Higiene Soberana):** Zero arquivos `.tmp` ou soltos na raiz; estrutura em 5 subdiretórios;
- **R20 (Proibição de Emojis):** 100% corporativo;
- **R21 (Didática Universal):** Acessível para executivos sem formação em TI.

---

## 2. Regras de Compilação

### R4-1: Determinismo Estrito
- Reexecução com mesmo slug + metadados = **exatamente** os mesmos arquivos (byte-for-byte);
- Timestamps são normalizados para data de compilação;
- Hashes SHA256 são calculados e armazenados em SQLite.

### R4-2: Estrutura de Diretórios Obrigatória
```
output/04-ecossistemas/ecos-<slug>/
├── 00-livro-mestre-compilado/      (obrigatório)
├── 01-guias-executivos-e-viabilidade/    (obrigatório)
├── 02-guias-de-engenharia-e-infraestrutura/  (obrigatório)
├── 03-playbooks-de-instalacao-e-operacao/   (obrigatório)
├── 04-playbooks-de-desinstalacao-e-governanca/  (obrigatório)
└── relatorio-execucao-<slug>.html   (obrigatório)
```

**Violação:** Script falha com `exit 1`.

### R4-3: Tripartição de Formatos
Cada documento deve ser gerado em **3 formatos**:
- **HTML R5-E** com interatividade e hero stats;
- **Markdown** desmembrado (7 arquivos no livro mestre);
- **PDF Typst** compilado com índice.

**Violação:** Abortar compilação.

### R4-4: Validação de Integridade
Após compilação, validar:
- [ ] Todos os arquivos HTML parseáveis;
- [ ] Todos os Markdown com sintaxe válida;
- [ ] PDF renderizável sem erros Typst;
- [ ] Ausência de credenciais (regex);
- [ ] Hashes bate com esperado.

**Violação:** Rolar back e avisar.

---

## 3. Regras de Persistência (R11)

Toda execução deve gravar em `estado_esteira.db`:

```sql
INSERT INTO esteira_ecossistemas (
  slug, nome, componentes_json, versoes, status,
  timestamp, modelo_llm, tokens_gastos, gate1, gate2, gate3, gate4
) VALUES (...)
```

Campo `status` pode ser: `em_progresso`, `ok`, `erro_validacao`, `erro_compilacao`, `erro_gate`.

---

## 4. Regras de Gates (R9)

| # | Nome | Comando | Pass/Fail |
|---|------|---------|-----------|
| 1 | Integridade de Arquivos | `find . -type f -ls \| wc -l` | ≥ 15 arquivos |
| 2 | Validação HTML/MD/PDF | `html-validate *.html && mdlint *.md` | exit 0 |
| 3 | Ausência de Segredos | `grep -r "password\|secret\|api_key" \| grep -v ".example"` | 0 matches |
| 4 | Métricas de Profundidade | `wc -l *.md \| awk '{print $1}'` | > 5000 linhas |

**Bloqueio:** Gate 1, 2, 3 bloqueiam commit. Gate 4 só avisa.

---

## 5. Regras de Idempotência (R10)

Reexecution com **mesmo slug + mesmos metadados** deve produzir:
- Mesmos nomes de arquivo;
- Mesmos hashes SHA256;
- Mesma estrutura de diretórios;
- Mesma ordem de seções no HTML/MD.

**Teste:** `git diff output/04-ecossistemas/` deve estar vazio.

---

## 6. Regras de Nomenclatura (R13)

| Artefato | Padrão | Exemplo |
|----------|--------|---------|
| Livro Mestre | `livro-mestre-<slug>.[html\|md\|pdf]` | `livro-mestre-stack-ia.html` |
| Guia Executivo | `guia-tco-<slug>.html` | `guia-tco-stack-ia.html` |
| Arquitetura | `arquitetura-<slug>.html` | `arquitetura-stack-ia.html` |
| Playbook Deploy | `playbook-deploy-<slug>.html` | `playbook-deploy-stack-ia.html` |
| Relatório | `relatorio-execucao-<slug>.html` | `relatorio-execucao-stack-ia.html` |

