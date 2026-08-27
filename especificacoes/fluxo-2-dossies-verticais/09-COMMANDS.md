# 09 · Catálogo de Comandos & Flags CLI (Fluxo 2)

> **Módulo:** Fluxo 2 — Dossiês Verticais de Desmantelamento SaaS

---

## 1. Comandos Operacionais

### 1.1 Compilação Tripartite de um Dossiê Vertical
```bash
python scripts/gerar_dossie_vertical_tripartite.py --saas granola
```

### 1.2 Execução da Suíte de Testes Unitários
```bash
python -m unittest tests/test_fluxo2_verticais.py -v
```

### 1.3 Auditoria Mecânica R5-V (Gate do Dossiê Vertical)
```bash
python scripts/auditar_tipo_vertical.py output/listas-open-source/vert-granola.html
```

### 1.4 Execução do Runner da Skill `/implementacao`
```bash
node .claude/skills/implementacao/index.cjs scripts/data/plano_implementacao_fluxo2.json
```
