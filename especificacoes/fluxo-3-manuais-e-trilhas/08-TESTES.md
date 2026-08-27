# 08 · Arquitetura de Testes Unitários Automatizados & CI/CD

> **Módulo:** Esteira Autônoma de Ingestão de Fontes, Manuais VPS e Trilhas de Aprendizado  
> **Suíte:** `tests/test_esteira_manuais.py` (Unittest / Pytest)  
> **Execução:** 8 Testes em < 1 segundo (Exit 0)  
> **Status:** Produção Homologada · Nota 10.0 / 10.0

---

## 1. Princípio do Test-Driven AIDD

No desenvolvimento orientado por IA, os testes automatizados são a **rede de segurança matemática** contra regressões, quebras de templates e alucinações de modelos.

Nenhum código novo é aceito no repositório sem que a suíte de testes unitários execute com **100% de sucesso**. A regra R16 da governança proíbe expressamente "commitar código com testes vermelhos".

---

## 2. A Suíte de Testes: `tests/test_esteira_manuais.py`

A suíte possui 8 testes unitários que cobrem integralmente todas as camadas do sistema:

| Teste | Nome do Método | Escopo de Validação | Tempo Típico |
| :---: | :--- | :--- | :---: |
| **T01** | `test_01_schemas_json_validos` | Valida integridade e sintaxe dos 4 schemas JSON da esteira | ~10ms |
| **T02** | `test_02_dados_fontes_e_sumario` | Valida que o sumário contém exatamente 5 fontes com IDs F01 a F05 | ~5ms |
| **T03** | `test_03_gates_mecanicos_g0_g1_g2` | Executa programmaticamente os Gates G0 (qualidade), G1 (HTTP) e G2 (citações) | ~600ms |
| **T04** | `test_04_arquivos_tripartites_gerados` | Confirma existência e tamanho > 0 dos manuais e trilhas (HTML, MD, PDF) | ~15ms |
| **T05** | `test_05_relatorio_telemetria_tripartite` | Valida a geração do relatório tripartite de fechamento com data DD-MM-YYYY | ~15ms |
| **T06** | `test_06_persistencia_sqlite_r11` | Executa inserção, leitura e limpeza de teste no banco SQLite `estado_esteira.db` | ~50ms |
| **T07** | `test_07_topologia_pastas_modular_9_arquivos` | Audita que a ferramenta possui exatamente 9 arquivos (3 em manuais, 3 em trilhas, 3 em relatórios) | ~20ms |
| **T08** | `test_08_paridade_espelho_docs_r18` | Compara conjuntos de arquivos entre `output/<slug>/` e `docs/<slug>/` (Regra R18) | ~30ms |

---

## 3. Como Executar os Testes

### Execução Simples:
```powershell
python -m unittest tests/test_esteira_manuais.py
```

### Execução Detalhada (Modo Verbose):
```powershell
python -m unittest tests/test_esteira_manuais.py -v
```

### Exemplo de Saída Homologada (Terminal Real):
```text
test_01_schemas_json_validos ... ok
test_02_dados_fontes_e_sumario ... ok
test_03_gates_mecanicos_g0_g1_g2 ... ok
test_04_arquivos_tripartites_gerados ... ok
test_05_relatorio_telemetria_tripartite ... ok
test_06_persistencia_sqlite_r11 ... ok
test_07_topologia_pastas_modular_9_arquivos ... ok
test_08_paridade_espelho_docs_r18 ... ok

----------------------------------------------------------------------
Ran 8 tests in 0.971s

OK
```

---

## 4. Integração Contínua (CI) e Pré-Commit Hook

A suíte é executada automaticamente antes de qualquer alteração ser enviada ao Git através do hook `.git/hooks/pre-commit`:

```bash
# Trecho do hook pre-commit
python tests/test_esteira_manuais.py || {
    echo "❌ FALHA NA SUÍTE DE TESTES DA ESTEIRA: Commit abortado."
    exit 1
}
```

Isso garante que é mecanicamente impossível versionar código que quebre qualquer um dos 4 gates mecânicos ou viole a paridade de arquivos.
