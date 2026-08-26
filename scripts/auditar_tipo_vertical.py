# -*- coding: utf-8 -*-
"""
AUDITOR MECÂNICO DE DOSSIÊS VERTICAIS (REGRA R5-V)
Valida a conformidade estrita dos Dossiês Verticais:
1. Presença do alvo SaaS em foco e riscos de privacidade;
2. Quinteto Soberano classificado (Mais Robusta, Completa, Moderna, Leve, Simples);
3. Presença obrigatória da Seção 5: Uso Complementar com MCPs, Skills ou Extensões;
4. Botão oficial do GitHub em SVG;
5. Scrollbars refinadas de 4px na cor accent.
"""
import sys
import glob
import re
from pathlib import Path

def console_utf8():
    if sys.platform == "win32":
        try:
            sys.stdout.reconfigure(encoding="utf-8")
            sys.stderr.reconfigure(encoding="utf-8")
        except Exception:
            pass

console_utf8()

def auditar_dossies_verticais():
    arquivos_out = sorted(glob.glob("output/listas-open-source/vert-*.html"))
    arquivos_doc = sorted(glob.glob("docs/listas/vert-*.html"))
    todos = sorted(list(set(arquivos_out + arquivos_doc)))

    print("=" * 80)
    print(" 🔍 AUDITORIA DE CONFORMIDADE COM A REGRA R5-V (DOSSIÊ VERTICAL SAAS)")
    print(f" Total de Dossiês Verticais Encontrados: {len(todos)}")
    print("=" * 80)

    if not todos:
        print("  [!] Nenhum dossiê vertical encontrado para auditar.")
        return True

    conformes = []
    reprovados = []

    for f in todos:
        p = Path(f)
        txt = p.read_text(encoding="utf-8")

        txt_lower = txt.lower()
        has_target = "target-box" in txt
        has_table = "<table" in txt
        has_sec1 = "1. o que faz &amp; como funciona" in txt_lower
        has_sec2 = "2. análise econômica" in txt_lower or "2. analise economica" in txt_lower
        has_sec3 = "3. requisitos de infraestrutura" in txt_lower
        has_sec4 = "4. como usar no dia a dia" in txt_lower
        has_sec5 = "5. uso complementar" in txt_lower or "complement-card" in txt
        has_mcp = "mcp server" in txt_lower or "agent skill" in txt_lower
        has_repo = "repo-btn" in txt and ("viewbox" in txt_lower)
        has_scroll = "::-webkit-scrollbar" in txt and "4px" in txt

        is_valido = (has_target and has_table and has_sec1 and has_sec2 and has_sec3 and 
                     has_sec4 and has_sec5 and has_mcp and has_repo and has_scroll)

        if is_valido:
            conformes.append(f)
            print(f"  [✓] CONFORME (Diamante R5-V): {f}")
        else:
            erros = []
            if not has_target: erros.append("Sem Caixa de Alvo SaaS")
            if not has_sec5: erros.append("Sem Seção 5 de Uso Complementar")
            if not has_mcp: erros.append("Sem menção a MCP Server ou Agent Skill")
            if not has_repo: erros.append("Sem botão SVG do GitHub")
            if not has_scroll: erros.append("Sem scrollbar 4px accent")
            reprovados.append((f, erros))
            print(f"  [✗] REPROVADO: {f} -> Motivos: {', '.join(erros)}")

    print("=" * 80)
    print(f" 📊 RESULTADO: {len(conformes)} APROVADOS | {len(reprovados)} REPROVADOS")
    print("=" * 80)

    if reprovados:
        sys.exit(1)
    return True

if __name__ == "__main__":
    auditar_dossies_verticais()
