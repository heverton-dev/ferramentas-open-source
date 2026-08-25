# -*- coding: utf-8 -*-
"""
SUPER-AUDITOR GERAL: CERTIFICADO DAS 4 CAMADAS DA FÁBRICA UNIVERSAL
Executa os 4 gates mecânicos em cadeia:
1. Camada 1: TELA (Prompt & Context)
2. Camada 2: HARNESS (Orquestração & Segurança)
3. Camada 3: LLM (Model Layer & Roteamento)
4. Camada 4: TOOLS (MCP & Determinismo)
Retorna Exit 0 (100% nas 4 Camadas) ou Exit 1 se qualquer camada falhar.
"""
import os
import sys
import subprocess

def console_utf8():
    if sys.platform == "win32":
        try:
            sys.stdout.reconfigure(encoding="utf-8")
            sys.stderr.reconfigure(encoding="utf-8")
        except Exception:
            pass

console_utf8()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS_DIR = os.path.join(BASE_DIR, "scripts")

GATES = [
    ("CAMADA 1: TELA", os.path.join(SCRIPTS_DIR, "auditar_camada_tela.py")),
    ("CAMADA 2: HARNESS", os.path.join(SCRIPTS_DIR, "auditar_camada_harness.py")),
    ("CAMADA 3: LLM", os.path.join(SCRIPTS_DIR, "auditar_camada_llm.py")),
    ("CAMADA 4: TOOLS", os.path.join(SCRIPTS_DIR, "auditar_camada_tools.py"))
]

def executar_super_auditoria():
    print("\n" + "#" * 80)
    print(" 🏛️ AUDITORIA GERAL HOLÍSTICA: AS 4 CAMADAS DA FÁBRICA UNIVERSAL")
    print("#" * 80 + "\n")

    resultados = []
    for nome, script in GATES:
        res = subprocess.run([sys.executable, script], cwd=BASE_DIR)
        aprovado = (res.returncode == 0)
        resultados.append((nome, aprovado))
        print("-" * 80)

    print("\n" + "=" * 80)
    print(" 📊 QUADRO FINAL DE CONFORMIDADE DAS 4 CAMADAS:")
    print("=" * 80)
    
    todas_ok = True
    for nome, ok in resultados:
        status_icone = "✅ 100% APROVADO" if ok else "❌ REPROVADO"
        print(f"  -> {nome:<25} {status_icone}")
        if not ok:
            todas_ok = False

    print("=" * 80)
    if todas_ok:
        print(" 🏆 CERTIFICADO EMITIDO: TODAS AS 4 CAMADAS ESTÃO EM 100% DE MATURIDADE!")
        print("=" * 80 + "\n")
        return 0
    else:
        print(" ❌ ATENÇÃO: Corrija os desvios apontados acima para atingir 100% global.")
        print("=" * 80 + "\n")
        return 1

if __name__ == "__main__":
    sys.exit(executar_super_auditoria())
