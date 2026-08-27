# 10 · Ciclo de Vida & Automações Mecânicas (Hooks) (Fluxo 2)

> **Módulo:** Fluxo 2 — Dossiês Verticais de Desmantelamento SaaS

---

## 1. Ciclo de Validação Contínua (Pre-Commit)

Antes de qualquer commit no repositório, o hook do Git dispara a auditoria automática:
1. `tests/test_fluxo2_verticais.py` deve retornar `OK`;
2. `scripts/auditar_tipo_vertical.py` deve retornar `exit 0`;
3. `scripts/auditar_higiene_repo.py` valida paridade MD5 de espelhos e ausência de lixo temporário.
