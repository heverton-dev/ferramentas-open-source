# -*- coding: utf-8 -*-
"""
GATE MECÂNICO DA CAMADA 3: AUDITOR DO LLM (MODEL LAYER & SEMANTIC ROUTING)
Audita a inteligência do modelo, matriz de tiers e contratos estruturados:
1. Presença do Roteador Semântico com 3 Tiers declarados (scripts/roteador_llm.py).
2. Presença e conformidade dos JSON Schemas em scripts/schemas/ (schema_ferramenta.json e schema_relatorio.json).
3. Associação explícita de custo de LLM no registro declarativo scripts/tipos.py.
4. Retorna Exit 0 (100% Aprovado) ou Exit 1 com relatório de pendências.
"""
import os
import sys
import json

def console_utf8():
    if sys.platform == "win32":
        try:
            sys.stdout.reconfigure(encoding="utf-8")
            sys.stderr.reconfigure(encoding="utf-8")
        except Exception:
            pass

console_utf8()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROUTER_FILE = os.path.join(BASE_DIR, "scripts", "roteador_llm.py")
SCHEMAS_DIR = os.path.join(BASE_DIR, "scripts", "schemas")
TIPOS_FILE = os.path.join(BASE_DIR, "scripts", "tipos.py")

SCHEMAS_OBRIGATORIOS = [
    "schema_ferramenta.json",
    "schema_relatorio.json"
]

def auditar_roteador_llm():
    erros = []
    if not os.path.isfile(ROUTER_FILE):
        return ["Roteador semântico ausente: scripts/roteador_llm.py."]

    try:
        sys.path.insert(0, os.path.dirname(ROUTER_FILE))
        import roteador_llm
        tiers = getattr(roteador_llm, "TIERS_LLM", {})
        if "tier_1_rapido" not in tiers:
            erros.append("Tier 1 (Rápido) ausente em roteador_llm.py.")
        if "tier_2_codigo" not in tiers:
            erros.append("Tier 2 (Código) ausente em roteador_llm.py.")
        if "tier_3_raciocinio" not in tiers:
            erros.append("Tier 3 (Raciocínio) ausente em roteador_llm.py.")
    except Exception as e:
        erros.append(f"Erro ao carregar roteador_llm.py: {e}")

    return erros

def auditar_schemas_estruturados():
    erros = []
    if not os.path.isdir(SCHEMAS_DIR):
        return ["Diretório de schemas ausente: scripts/schemas/."]

    for schema_nome in SCHEMAS_OBRIGATORIOS:
        schema_path = os.path.join(SCHEMAS_DIR, schema_nome)
        if not os.path.isfile(schema_path):
            erros.append(f"Schema obrigatório ausente: scripts/schemas/{schema_nome}.")
        else:
            try:
                with open(schema_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                if not data.get("properties") or not data.get("required"):
                    erros.append(f"Schema {schema_nome} inválido (falta 'properties' ou 'required').")
            except Exception as e:
                erros.append(f"Erro ao parsear JSON Schema {schema_nome}: {e}")

    return erros

def auditar_tipos_e_custos():
    erros = []
    if not os.path.isfile(TIPOS_FILE):
        erros.append("Registro de tipos ausente: scripts/tipos.py.")
    else:
        with open(TIPOS_FILE, "r", encoding="utf-8") as f:
            content = f.read()
        if "custo_llm" not in content:
            erros.append("Campo 'custo_llm' não mapeado no registro scripts/tipos.py.")
    return erros

def auditar_camada_llm_completa():
    print("=" * 80)
    print(" 🧠 GATE MECÂNICO DA CAMADA 3: AUDITOR DO LLM (MODEL LAYER & ROUTING)")
    print("=" * 80)

    e1 = auditar_roteador_llm()
    e2 = auditar_schemas_estruturados()
    e3 = auditar_tipos_e_custos()

    total_erros = len(e1) + len(e2) + len(e3)

    if e1:
        print("\n [!] DESVIOS NO ROTEADOR SEMÂNTICO DE TIERS:")
        for err in e1: print(f"     ❌ {err}")

    if e2:
        print("\n [!] DESVIOS NOS SCHEMAS JSON ESTRUTURADOS:")
        for err in e2: print(f"     ❌ {err}")

    if e3:
        print("\n [!] DESVIOS NO MAPEAMENTO DE CUSTOS (tipos.py):")
        for err in e3: print(f"     ❌ {err}")

    print("\n" + "=" * 80)
    if total_erros == 0:
        print(" ✅ CAMADA 3 (LLM) 100% APROVADA: Matriz de Tiers, Structured Outputs & Schemas!")
        print("=" * 80 + "\n")
        return 0
    else:
        print(f" ❌ REPROVADO: {total_erros} pendências para atingir 100% na Camada 3.")
        print("=" * 80 + "\n")
        return 1

if __name__ == "__main__":
    sys.exit(auditar_camada_llm_completa())
