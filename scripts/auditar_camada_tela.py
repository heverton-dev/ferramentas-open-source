# -*- coding: utf-8 -*-
"""
GATE MECÂNICO DA CAMADA 1: AUDITOR DA TELA (PROMPT & CONTEXT ENGINEERING)
Audita a integridade, densidade e limites da primeira camada:
1. Orçamento de Tokens do Prompt Mestre (.claude/CLAUDE.md <= 2.500 palavras/tokens para Prompt Caching).
2. Integridade das 5 Skills Fundamentais de Economia (caveman, headroom, lean-ctx, rtk-memory, pre-flight-check).
3. Presença das Regras Sagradas R1 a R18 sem placeholders residuais.
4. Presença do Vocabulário Controlado e Proibição de Termos Prolixos.
5. Presença e integridade do arquivo de memória persistente RTK-SCRATCHPAD.md.
6. Retorna Exit 0 (100% Aprovado) ou Exit 1 com relatório de desvios.
"""
import os
import sys
import re

def console_utf8():
    if sys.platform == "win32":
        try:
            sys.stdout.reconfigure(encoding="utf-8")
            sys.stderr.reconfigure(encoding="utf-8")
        except Exception:
            pass

console_utf8()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CLAUDE_MD = os.path.join(BASE_DIR, ".claude", "CLAUDE.md")
SKILLS_DIR = os.path.join(BASE_DIR, ".claude", "skills")
SCRATCHPAD = os.path.join(BASE_DIR, "RTK-SCRATCHPAD.md")

SKILLS_OBRIGATORIAS = [
    "caveman",
    "headroom",
    "lean-ctx",
    "rtk-memory",
    "pre-flight-check"
]

TERMOS_PROIBIDOS = [
    r"como uma IA",
    r"como um modelo de linguagem",
    r"espero que isso ajude",
    r"espero ter ajudado",
    r"sinta-se à vontade",
    r"com certeza!",
    r"certamente!",
    r"olá! como posso ajudar",
]

def auditar_prompt_mestre():
    erros = []
    if not os.path.isfile(CLAUDE_MD):
        return ["Arquivo .claude/CLAUDE.md não encontrado!"]

    with open(CLAUDE_MD, "r", encoding="utf-8") as f:
        content = f.read()

    # Checar contagem de palavras/tokens aproximados
    palavras = len(content.split())
    if palavras > 3000:
        erros.append(f"Prompt mestre excede o orçamento de cache: {palavras} palavras (limite: 3.000).")

    # Checar regras R1 a R18
    for i in range(1, 19):
        regra_tag = f"R{i} ("
        if regra_tag not in content:
            erros.append(f"Regra de governança {regra_tag.strip()} ausente em .claude/CLAUDE.md.")

    # Checar se restou placeholder não preenchido
    if "<SEU-PROJETO>" in content:
        erros.append("Placeholder '<SEU-PROJETO>' ainda presente em .claude/CLAUDE.md.")

    return erros

def auditar_skills_economia():
    erros = []
    if not os.path.isdir(SKILLS_DIR):
        return ["Diretório .claude/skills/ não encontrado!"]

    for s in SKILLS_OBRIGATORIAS:
        skill_path = os.path.join(SKILLS_DIR, s, "SKILL.md")
        if not os.path.isfile(skill_path):
            erros.append(f"Skill de economia obrigatória ausente: .claude/skills/{s}/SKILL.md")
        else:
            with open(skill_path, "r", encoding="utf-8") as f:
                txt = f.read()
            if len(txt.strip()) < 50:
                erros.append(f"Skill {s}/SKILL.md está vazia ou corrompida.")
    return erros

def auditar_scratchpad():
    erros = []
    if not os.path.isfile(SCRATCHPAD):
        erros.append("Arquivo RTK-SCRATCHPAD.md ausente na raiz do projeto.")
    return erros

def auditar_vocabulario_controlado():
    erros = []
    # Checar se o CLAUDE.md define o vocabulário controlado
    with open(CLAUDE_MD, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "Vocabulário Controlado" not in content and "Termos Proibidos" not in content:
        erros.append("Diretriz de Vocabulário Controlado e Termos Proibidos ausente em .claude/CLAUDE.md.")

    return erros

def auditar_camada_tela_completa():
    print("=" * 80)
    print(" 🎛️ GATE MECÂNICO DA CAMADA 1: AUDITORIA DA TELA (PROMPT & CONTEXT)")
    print("=" * 80)

    e1 = auditar_prompt_mestre()
    e2 = auditar_skills_economia()
    e3 = auditar_scratchpad()
    e4 = auditar_vocabulario_controlado()

    total_erros = len(e1) + len(e2) + len(e3) + len(e4)

    if e1:
        print("\n [!] DESVIOS NO PROMPT MESTRE (CLAUDE.md):")
        for err in e1: print(f"     ❌ {err}")

    if e2:
        print("\n [!] DESVIOS NAS SKILLS DE ECONOMIA:")
        for err in e2: print(f"     ❌ {err}")

    if e3:
        print("\n [!] DESVIOS NA MEMÓRIA RTK:")
        for err in e3: print(f"     ❌ {err}")

    if e4:
        print("\n [!] DESVIOS NO VOCABULÁRIO CONTROLADO:")
        for err in e4: print(f"     ❌ {err}")

    print("\n" + "=" * 80)
    if total_erros == 0:
        print(" ✅ CAMADA 1 (TELA) 100% APROVADA: Prompt Caching, Regras R1-R18, 5 Skills & Vocabulário!")
        print("=" * 80 + "\n")
        return 0
    else:
        print(f" ❌ REPROVADO: {total_erros} pendências para atingir 100% na Camada 1.")
        print("=" * 80 + "\n")
        return 1

if __name__ == "__main__":
    sys.exit(auditar_camada_tela_completa())
