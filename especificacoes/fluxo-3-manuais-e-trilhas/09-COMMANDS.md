# 09 · Catálogo de Comandos, Flags CLI & Modais no Chat

> **Módulo:** Esteira Autônoma de Ingestão de Fontes, Manuais VPS e Trilhas de Aprendizado  
> **Interfaces:** Modal Interativo no Chat (Opção A), Linha de Comando (CLI) e Hooks  
> **Status:** Produção Homologada · Nota 10.0 / 10.0

---

## 1. Modos de Operação da Esteira

O módulo suporta três formas de interação adaptadas ao perfil do operador:

1. **Modo Chat Nativo (Opção A - Recomendado para o Engenheiro Agêntico):**  
   O agente renderiza um modal interativo no próprio chat com caixas de seleção, permitindo escolher quais ferramentas do Quinteto Soberano processar sem tocar no terminal.
2. **Modo Linha de Comando (CLI):**  
   Para automações em lote, scripts em background e pipelines de integração contínua (CI/CD).
3. **Modo Gate Isolado:**  
   Para auditar ou debugar uma única etapa mecânica (ex: auditar apenas links ou apenas citações).

---

## 2. Acionamento Agêntico & CLI Runner Universal

### 2.1. Via Slash Command no Chat (Qualquer IDE)
Dispara o fluxo pelo chat interativo:
```text
/fluxo3 screenpipe granola
```

### 2.2. Via CLI Runner Determinístico (Terminal)
```powershell
python scripts/run_fluxo3.py --ferramenta screenpipe --saas granola
```

---

## 3. Comandos do Orquestrador Mestre em Lote

Arquivo principal: [`scripts/orquestrador_esteira_manuais.py`](file:///C:/Users/trcnologia/orca/projects/open-source/scripts/orquestrador_esteira_manuais.py)

### 3.1. Executar o Quinteto Soberano Completo (Modo em Lote)
Executa as 5 ferramentas do SaaS indicado, gerando os 45 arquivos e gravando no SQLite:
```powershell
python scripts/orquestrador_esteira_manuais.py --saas granola --modo todas
```

### 3.2. Executar uma Única Ferramenta Cirúrgica
Processa apenas a ferramenta especificada:
```powershell
python scripts/orquestrador_esteira_manuais.py --saas granola --ferramenta screenpipe
```

### 3.3. Abrir o Menu Interativo no Terminal
Exibe o menu visual numerado no terminal para escolha manual:
```powershell
python scripts/orquestrador_esteira_manuais.py --saas granola
```

---

## 3. Comandos dos Gates Mecânicos Isolados

Para executar auditorias rápidas sem rodar a compilação completa:

### 3.1. Gate G0 · Auditoria de Qualidade e Whitelist
Valida se as fontes atendem aos critérios de autoridade, recência e densidade:
```powershell
python scripts/auditar_qualidade_fontes.py scripts/data/sumario-fontes-screenpipe.json
```

### 3.2. Gate G1 · Auditoria de Veracidade Digital (HTTP 200)
Testa se todas as URLs do sumário estão ativas na internet:
```powershell
python scripts/auditar_fontes_veridicas.py scripts/data/sumario-fontes-screenpipe.json
```

### 3.3. Gate G2 · Auditoria de Citações Cruzadas (Zero Alucinação)
Verifica se 100% dos IDs de fontes são citados no manual:
```powershell
python scripts/auditar_citacoes_manuais.py screenpipe
```

### 3.4. Gate R18 · Auditoria de Higiene e Paridade de Espelhos
Garante ausência de arquivos temporários e paridade estrita entre `output/` e `docs/`:
```powershell
python scripts/auditar_higiene_repo.py
```

---

## 4. Comandos de Compilação Direta Ad-Hoc

### Compilar Apenas o Manual Operacional (HTML, MD e PDF Typst):
```powershell
python scripts/gerar_manual_operacional.py --slug screenpipe
```

### Compilar Apenas a Trilha de Aprendizado (HTML, MD e PDF Typst):
```powershell
python scripts/gerar_trilha_aprendizado.py --slug screenpipe
```

### Executar a Suíte Completa de Testes Unitários:
```powershell
python -m unittest tests/test_esteira_manuais.py -v
```

### Consultar o Estado Persistente no SQLite:
```powershell
python scripts/estado_esteira.py
```
