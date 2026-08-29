# 08 · Suite de Testes (Fluxo 5: Auditorias VPS)

---

## 1. Testes Unitários

```python
def test_portainer_connector_valido():
    assert conectar_portainer("https://portainer.local", "token_valid")

def test_headroom_calculator():
    assert calcular_headroom(32, 18, 256, 140) == {"cpu": 43, "ram": 45}

def test_deteccao_conflitos_porta():
    assert detectar_conflito_porta(8080, [8000, 8080, 9000]) == True

def test_gera_docker_compose():
    compose = gerar_docker_compose({"ollama": "0.3.0"})
    assert "version:" in compose and "services:" in compose
```

---

## 2. Testes de Integração

```python
def test_pipeline_completo():
    resultado = run_fluxo5("stack-ia", portainer_url="https://...", portainer_token="...")
    assert resultado["status"] == "ok"
    assert os.path.exists("output/05-auditorias-vps/stack-ia/")
    assert len(glob.glob("output/05-auditorias-vps/stack-ia/**/*.html")) >= 3
```

---

## 3. Testes de Gates

```bash
#!/bin/bash
# Gate 1: Integridade
ARQUIVO_COUNT=$(find output/05-auditorias-vps/${SLUG}/ -type f | wc -l)
[ $ARQUIVO_COUNT -ge 12 ] && echo "Gate 1 OK" || exit 1

# Gate 2: Validação YAML
yamllint output/05-auditorias-vps/${SLUG}/**/*.yml || exit 1

# Gate 3: Ausência de Segredos
! grep -r "PORTAINER_TOKEN" output/05-auditorias-vps/${SLUG}/ 2>/dev/null || exit 1

echo "All gates OK"
exit 0
```

---

## 4. Testes E2E

```bash
#!/bin/bash
python scripts/run_fluxo5.py \
  --slug test-stack \
  --portainer-url https://portainer.test.local \
  --token ptr_test_token

python -m pytest tests/test_fluxo5_e2e.py -v
```

