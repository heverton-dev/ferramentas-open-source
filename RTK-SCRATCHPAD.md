# 🧠 RTK-SCRATCHPAD · Memória Persistente de Longo Prazo

> **Finalidade:** Arquivo externo para registrar aprendizados, decisões técnicas e resoluções de bugs ocorridos durante as sessões.
> **Regra de Injeção de Contexto:** A Camada TELA lê apenas os **últimos 5 aprendizados** relevantes sob demanda, preservando o cache fixo do prompt mestre (`CLAUDE.md`).

---

## 📌 Aprendizados Registrados

### [2026-08-25] Padronização Universal do Padrão Diamante R5
* **Decisão:** Todas as 49 listas técnicas foram unificadas no Padrão Dossiê Executivo (Hero Stats Bar, Tabela fluida sem scroll horizontal, 4 seções verticais nos cards e 3 mini-cards de passos práticos).
* **Anti-Pattern Eliminado:** Banido terminantemente o uso de 2 colunas espremidas (`div.cols`) e parágrafos corridos de instruções.

### [2026-08-25] Gate Mecânico R18 & Paridade Estrita de Espelhos
* **Decisão:** Criado o auditor `scripts/auditar_higiene_repo.py` acionado no `pre-commit`.
* **Regra:** Nenhuma alteração é commitada se houver divergência de hash MD5 entre `output/listas-open-source/` e `docs/listas/` ou se existirem arquivos temporários (`temp_*`, `fix_*`, `.bak`).

### [2026-08-25] Tratamento de Permissões no Windows para Expurgo Seguro
* **Aprendizado:** Pastas `.git/objects` no Windows possuem atributo Read-Only nativo. Funções de `shutil.rmtree` devem usar `onexc=remove_readonly` com `os.chmod(path, stat.S_IWRITE)` para evitar erros de `PermissionError: [WinError 5]`.

### [2026-08-25] Vocabulário Controlado da TELA
* **Regra:** Silenciamento absoluto de introduções e saudações ("Como uma IA", "Espero ter ajudado"). Respostas sempre diretas, técnicas e em conformidade com o padrão executivo.
