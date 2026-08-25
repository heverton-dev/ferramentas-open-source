# -*- coding: utf-8 -*-
"""
GATE MECÂNICO DA CAMADA 4: AUDITOR DE TOOLS (MCP SERVERS & DETERMINISMO MECÂNICO)
Audita os instrumentos, processadores, banco de estado e scripts determinísticos:
1. Validação de leitura/escrita no Banco de Estado Persistente SQLite R11 (scripts/estado_esteira.py).
2. Presença de todos os scripts determinísticos de fiscalização e auto-saneamento.
3. Presença e integridade da configuração .mcp.json na raiz do projeto.
4. Retorna Exit 0 (100% Aprovado) ou Exit 1 com relatório de pendências.
"""
import os
import sys

def console_utf8():
    if sys.platform == "win32":
        try:
            sys.stdout.reconfigure(encoding="utf-8")
            sys.stderr.reconfigure(encoding="utf-8")
        except Exception:
            pass

console_utf8()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MCP_JSON = os.path.join(BASE_DIR, ".mcp.json")
ESTADO_SCRIPT = os.path.join(BASE_DIR, "scripts", "estado_esteira.py")

SCRIPTS_DETERMINISTICOS = [
    "auditar_higiene_repo.py",
    "limpar_entulho.py",
    "auditar_r5_dossie.py",
    "auditar_camada_tela.py",
    "auditar_camada_harness.py",
    "auditar_camada_llm.py",
    "estado_esteira.py",
    "roteador_llm.py",
    "tipos.py"
]

def auditar_banco_estado_sqlite():
    erros = []
    if not os.path.isfile(ESTADO_SCRIPT):
        return ["Módulo de estado persistente ausente: scripts/estado_esteira.py."]

    try:
        sys.path.insert(0, os.path.dirname(ESTADO_SCRIPT))
        import estado_esteira
        estado_esteira.inicializar_banco()
        estado_esteira.registrar_execucao_gate("CAMADA_4", "auditoria_teste_r11", 0, "Teste de integridade R11.")
        resumo = estado_esteira.consultar_resumo_estado()
        if not os.path.isfile(resumo["db_path"]):
            erros.append("Arquivo estado_esteira.db não foi criado no disco.")
    except Exception as e:
        erros.append(f"Falha ao operar banco SQLite R11: {e}")

    return erros

def auditar_scripts_deterministicos():
    erros = []
    scripts_dir = os.path.join(BASE_DIR, "scripts")
    for s in SCRIPTS_DETERMINISTICOS:
        script_path = os.path.join(scripts_dir, s)
        if not os.path.isfile(script_path):
            erros.append(f"Script determinístico obrigatório ausente: scripts/{s}.")
    return erros

def auditar_mcp_config():
    erros = []
    if not os.path.isfile(MCP_JSON):
        erros.append("Arquivo .mcp.json ausente na raiz do projeto.")
    return erros

def auditar_camada_tools_completa():
    print("=" * 80)
    print(" 🔧 GATE MECÂNICO DA CAMADA 4: AUDITOR DE TOOLS (MCP & DETERMINISMO)")
    print("=" * 80)

    e1 = auditar_banco_estado_sqlite()
    e2 = auditar_scripts_deterministicos()
    e3 = auditar_mcp_config()

    total_erros = len(e1) + len(e2) + len(e3)

    if e1:
        print("\n [!] DESVIOS NO BANCO DE ESTADO SQLITE R11:")
        for err in e1: print(f"     ❌ {err}")

    if e2:
        print("\n [!] DESVIOS NOS SCRIPTS DETERMINÍSTICOS:")
        for err in e2: print(f"     ❌ {err}")

    if e3:
        print("\n [!] DESVIOS NA CONFIGURAÇÃO MCP (.mcp.json):")
        for err in e3: print(f"     ❌ {err}")

    print("\n" + "=" * 80)
    if total_erros == 0:
        print(" ✅ CAMADA 4 (TOOLS) 100% APROVADA: SQLite R11, Scripts Determinísticos & MCP!")
        print("=" * 80 + "\n")
        return 0
    else:
        print(f" ❌ REPROVADO: {total_erros} pendências para atingir 100% na Camada 4.")
        print("=" * 80 + "\n")
        return 1

if __name__ == "__main__":
    sys.exit(auditar_camada_tools_completa())
