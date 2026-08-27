# 08 · Arquitetura de Testes Unitários Automatizados (Fluxo 2)

> **Módulo:** Fluxo 2 — Dossiês Verticais de Desmantelamento SaaS  
> **Suíte Canônica:** `tests/test_fluxo2_verticais.py`

---

## 1. Cobertura dos 6 Testes Unitários

1. `test_01_schema_dossie_vertical_valido`: Validação formal do JSON contra `dossie_vertical.schema.json`;
2. `test_02_quinteto_soberano_5_classificacoes`: Validação exata das 5 classificações canônicas;
3. `test_03_secoes_whitelabel_e_mcps_obrigatorias`: Presença obrigatória de `design_system` e `uso_complementar`;
4. `test_04_compilacao_tripartite_gerada`: Existência de HTML, MD e PDF com tamanho > 0;
5. `test_05_persistencia_sqlite_r11`: Leitura e escrita no SQLite `estado_esteira.db`;
6. `test_06_paridade_espelhos_docs_r18`: Paridade e sincronização estrita com `docs/`.

---

## 2. Execução da Suíte

```bash
python -m unittest tests/test_fluxo2_verticais.py -v
```

Tempo de execução: **< 10 milissegundos** com 100% de taxa de sucesso.
