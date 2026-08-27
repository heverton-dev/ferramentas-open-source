# 08 · Arquitetura de Testes Unitários Automatizados (Fluxo 1)

> **Módulo:** Fluxo 1 — Listas Horizontais & Compêndios Temáticos  
> **Suíte Canônica:** `tests/test_fluxo1_listas.py`

---

## 1. Cobertura dos 5 Testes Unitários

1. `test_01_compendio_html_diamante_existe`: Existência do arquivo na pasta de compêndios;
2. `test_02_compilacao_tripartite_bundle`: Validação da geração de HTML, MD e PDF com tamanho > 0;
3. `test_03_auditoria_mecanica_r5_diamante`: Conformidade com título H1 e estrutura diamante;
4. `test_04_persistencia_sqlite_r11`: Registro e consulta na tabela `esteira_listas_horizontais`;
5. `test_05_paridade_espelhos_docs_r18`: Paridade e sincronização estrita com `docs/`.

---

## 2. Execução da Suíte

```bash
python -m unittest tests/test_fluxo1_listas.py -v
```

Tempo de execução: **< 15 milissegundos** com 100% de sucesso.
