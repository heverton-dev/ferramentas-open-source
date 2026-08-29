# 08 · Suite de Testes (Fluxo 4: Macro-Ecossistemas)

> **Módulo:** Fluxo 4 — Macro-Ecossistemas e Suítes Integradas

---

## 1. Testes Unitários

### T1.1: Validação de Entrada
```python
def test_validador_ecossistema_valido():
    entrada = {
        "slug": "stack-ia",
        "nome": "Stack IA",
        "componentes": [...]
    }
    assert validador.validar(entrada) == entrada

def test_validador_ecossistema_sem_slug():
    entrada = {"nome": "Stack IA", "componentes": [...]}
    with pytest.raises(ValueError):
        validador.validar(entrada)
```

### T1.2: Grafo de Dependências
```python
def test_deteccao_ciclos():
    grafo = {"A": ["B"], "B": ["C"], "C": ["A"]}
    assert detector_ciclos(grafo) == ["A", "B", "C"]

def test_ordem_topologica():
    grafo = {"A": ["B", "C"], "B": ["D"], "C": ["D"]}
    ordem = topologia(grafo)
    assert ordem.index("A") < ordem.index("B")
```

### T1.3: Compilação Tripartite
```python
def test_gera_html():
    data = {...}
    html = compilador.gerar_html(data)
    assert "<html" in html and "ecos-" in html

def test_gera_markdown_7_arquivos():
    data = {...}
    mds = compilador.gerar_markdown(data)
    assert len(mds) == 7
    assert all("---" in md for md in mds)

def test_gera_pdf():
    data = {...}
    pdf_ok = compilador.gerar_pdf(data)
    assert pdf_ok  # File exists e é válido
```

---

## 2. Testes de Integração

### T2.1: Pipeline Completo
```python
def test_fluxo_completo_stack_ia():
    resultado = run_fluxo4("stack-ia-corporativa")
    assert resultado["status"] == "ok"
    assert os.path.exists("output/04-ecossistemas/ecos-stack-ia/")
    assert len(glob.glob("output/04-ecossistemas/ecos-stack-ia/**/*.html")) >= 5
```

### T2.2: Idempotência (R10)
```python
def test_idempotencia_mesmos_hashes():
    resultado1 = run_fluxo4("stack-ia")
    hash1 = sha256_directory("output/04-ecossistemas/ecos-stack-ia/")
    
    resultado2 = run_fluxo4("stack-ia")
    hash2 = sha256_directory("output/04-ecossistemas/ecos-stack-ia/")
    
    assert hash1 == hash2
```

### T2.3: SQLite Persistência
```python
def test_grava_sqlite_corretamente():
    resultado = run_fluxo4("stack-ia")
    
    db = sqlite3.connect("estado_esteira.db")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM esteira_ecossistemas WHERE slug = ?", ("stack-ia",))
    row = cursor.fetchone()
    
    assert row is not None
    assert row["status"] == "ok"
```

---

## 3. Testes de Gates (Mecânicos)

### T3.1: Gate 1 - Integridade de Arquivos
```bash
#!/bin/bash
ARQUIVO_COUNT=$(find output/04-ecossistemas/ecos-${SLUG}/ -type f | wc -l)
if [ $ARQUIVO_COUNT -lt 15 ]; then
  echo "Gate 1 FALHOU: apenas $ARQUIVO_COUNT arquivos (mínimo 15)"
  exit 1
fi
echo "Gate 1 OK"
exit 0
```

### T3.2: Gate 2 - Validação HTML/MD/PDF
```bash
#!/bin/bash
# Validar HTML
for f in output/04-ecossistemas/ecos-${SLUG}/**/*.html; do
  if ! html-validate "$f"; then
    echo "Gate 2 FALHOU: HTML inválido em $f"
    exit 1
  fi
done

# Validar Markdown
if ! mdlint output/04-ecossistemas/ecos-${SLUG}/**/*.md; then
  echo "Gate 2 FALHOU: Markdown inválido"
  exit 1
fi

echo "Gate 2 OK"
exit 0
```

### T3.3: Gate 3 - Ausência de Segredos
```bash
#!/bin/bash
SECRETS=$(grep -r -i "password\|secret\|api_key\|token" \
  output/04-ecossistemas/ecos-${SLUG}/ \
  | grep -v ".example" | wc -l)

if [ $SECRETS -gt 0 ]; then
  echo "Gate 3 FALHOU: $SECRETS secrets detectados"
  exit 1
fi

echo "Gate 3 OK"
exit 0
```

### T3.4: Gate 4 - Métricas de Profundidade
```bash
#!/bin/bash
LINHAS=$(wc -l output/04-ecossistemas/ecos-${SLUG}/**/*.md | tail -1 | awk '{print $1}')

if [ $LINHAS -lt 5000 ]; then
  echo "Gate 4 AVISO (não bloqueante): apenas $LINHAS linhas de MD (recomendado 5000+)"
  exit 0
fi

echo "Gate 4 OK"
exit 0
```

---

## 4. Testes de Performance

### T4.1: Tempo de Compilação
```python
def test_compilacao_em_menos_60s():
    import time
    start = time.time()
    resultado = run_fluxo4("stack-ia")
    elapsed = time.time() - start
    
    assert elapsed < 60, f"Compilação levou {elapsed}s (máximo 60s)"
```

---

## 5. Teste End-to-End

```bash
#!/bin/bash
set -e

echo "=== E2E Test: Fluxo 4 ==="

# Setup
rm -rf output/04-ecossistemas/ecos-test-*

# Executar
python scripts/run_fluxo4.py --ecossistema stack-test

# Validar
python -m pytest tests/test_fluxo4_e2e.py -v

echo "=== E2E Test PASSOU ==="
```

