# 06 · Regras de Execução (Fluxo 5: Auditorias VPS)

> **Módulo:** Fluxo 5 — Auditoria & Incorporação Cirúrgica em VPS

---

## 1. Regras Globais (CLAUDE.md)

Todas as regras de `CLAUDE.md` se aplicam. Específicas para Fluxo 5:

- **R5-VPS (Padrão Diamante VPS):** Obrigatório em todo HTML gerado;
- **R13 (Taxonomia):** Slugs `guia-<slug>`, máximo 35 caracteres;
- **R15 (Segredos & Credenciais):** Zero tokens Portainer em outputs; `.env.example` com validação;
- **R20 (Proibição de Emojis):** 100% corporativo;
- **R21 (Didática Universal):** Acessível para gestores sem formação DevOps.

---

## 2. Regras de Auditoria

### R5-1: Portainer Read-Only
- Fluxo 5 NUNCA modifica estado em Portainer (read-only API calls);
- Conectar com token com permissão `Viewer` ou inferior;
- Não executar ações de deploy; apenas coletar dados.

### R5-2: Snapshot Imutável
- Snapshot Portainer é capturado em `timestamp` único;
- Se reexecução acontecer após 1 hora, gerar novo snapshot;
- Comparar com anterior para detectar mudanças.

### R5-3: Segredos em .env.example
- PORTAINER_TOKEN **nunca** aparece em outputs;
- Docker secrets em `.env.example` com valores placeholder;
- Validação pré-commit bloqueia commits com credenciais.

---

## 3. Regras de Compilação

### R5-4: Determinismo Estrito
- Reexecução com mesmo slug + Portainer + componentes = **exatamente** os mesmos arquivos;
- Timestamps normalizados para data de compilação;
- Hashes SHA256 armazenados em SQLite.

### R5-5: Tripartição de Formatos
Cada documento em **3 formatos**:
- **HTML R5-VPS** com hero stats de infraestrutura (CPU, RAM, Disco);
- **Markdown** desmembrado (7 arquivos no livro mestre);
- **PDF Typst** compilado com índice.

### R5-6: Validação de YAML/JSON
Após compilação, validar:
- [ ] docker-compose-prod.yml é YAML válido;
- [ ] docker-compose-staging.yml parseável;
- [ ] .env.example válido;
- [ ] Ausência de credenciais (regex);
- [ ] Hashes batem com esperado.

**Violação:** Rolar back e avisar.

---

## 4. Regras de Persistência (R11)

Toda execução grava em `estado_esteira.db`:

```sql
INSERT INTO esteira_auditorias_vps (
  slug, portainer_url, snapshot_json, status,
  timestamp, modelo_llm, tokens_gastos, gate1-4
) VALUES (...)
```

Campo `status`: `em_progresso`, `ok`, `erro_auditoria`, `erro_compilacao`, `erro_gate`.

---

## 5. Regras de Gates (R9)

| # | Nome | Comando | Pass/Fail |
|---|------|---------|-----------|
| 1 | Integridade | `find output/05-auditorias-vps/<slug>/ -type f \| wc -l` | ≥ 12 arquivos |
| 2 | Validação YAML/JSON | `yamllint *.yml && jsonlint *.json` | exit 0 |
| 3 | Ausência de Segredos | `grep -r "PORTAINER_TOKEN\|password" \| grep -v ".example"` | 0 matches |
| 4 | Conformidade R5-VPS | `grep "hero-stats" *.html \| wc -l` | ≥ 1 |

**Bloqueio:** Gates 1, 2, 3 bloqueiam commit. Gate 4 apenas avisa.

---

## 6. Regras de Idempotência (R10)

Reexecução com **mesmo slug + mesmo snapshot Portainer** produz:
- Mesmos nomes de arquivo;
- Mesmos hashes SHA256;
- Mesma estrutura de diretórios;
- Mesmo docker-compose.yml (versão, ordem).

**Teste:** `git diff output/05-auditorias-vps/` deve estar vazio.

---

## 7. Regras de Segurança

### R5-7: Sem Execução Remota
- Scripts de instalação (`manual-instalacao-*.sh`) são **instrucionais** (human-readable);
- NÃO são executados automaticamente;
- Administrador copia/cola manualmente com validação;
- Rollback é manual ou via playbook pre-testado.

### R5-8: Backup Obrigatório
- Antes de qualquer deploy, fazer backup:
  - `docker volume export` de volumes críticos;
  - Snapshot do estado Portainer (JSON);
  - Backup de configuração (docker-compose atual).
- Guardar backups por 30 dias mínimo.

