# -*- coding: utf-8 -*-
"""
RECOMPILADOR TOTAL DE RELATÓRIOS OFICIAIS DE EXECUÇÃO & TELEMETRIA (PADRÃO ENTERPRISE)
Regenera 100% dos relatórios (MD, HTML Padrão Diamante Enterprise e PDF Nativo Typst):
- output/01-listas-horizontais/ (56 listas)
- output/02-dossies-verticais/ (51 dossiês)
- output/03-manuais-e-trilhas/ (todos os bundles)
"""
import os
import sys
import json
import glob
import re
from pathlib import Path
from datetime import datetime

def console_utf8():
    if sys.platform == "win32":
        try:
            sys.stdout.reconfigure(encoding="utf-8")
            sys.stderr.reconfigure(encoding="utf-8")
        except Exception:
            pass

console_utf8()

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR / "scripts"))

from relatorios_fluxo1 import gerar_relatorio_tripartite_fluxo1
from relatorios_fluxo2 import gerar_relatorio_tripartite_fluxo2
from relatorios_fluxo3 import gerar_relatorio_tripartite_fluxo3

def recompilar_fluxo1():
    print("\n" + "="*80)
    print(" 🚀 RECOMPILANDO RELATÓRIOS DO FLUXO 1 (LISTAS HORIZONTAIS) · NÍVEL ENTERPRISE")
    print("="*80)
    pastas = sorted(glob.glob(str(BASE_DIR / "output" / "01-listas-horizontais" / "list-*")))
    print(f"Total de pastas encontradas: {len(pastas)}")

    sucessos = 0
    for pasta_str in pastas:
        p = Path(pasta_str)
        slug = p.name.replace("list-", "")
        materiais_dir = p / "materiais"
        relatorios_dir = p / "relatorios"
        relatorios_dir.mkdir(parents=True, exist_ok=True)

        dados = {}
        possiveis_json = [
            BASE_DIR / "scripts" / "data" / f"dossie-{slug}.json",
            BASE_DIR / "scripts" / "data" / f"{slug}.json",
        ]
        for pj in possiveis_json:
            if pj.exists():
                try:
                    dados = json.loads(pj.read_text(encoding="utf-8"))
                    break
                except Exception:
                    pass

        if not dados:
            md_mat = materiais_dir / f"list-{slug}.md"
            ferramentas = []
            titulo = slug.replace("-", " ").title()
            if md_mat.exists():
                txt = md_mat.read_text(encoding="utf-8", errors="replace")
                m_tit = re.search(r"^# (.+)$", txt, re.MULTILINE)
                if m_tit:
                    titulo = m_tit.group(1).replace("Compêndio Diamante:", "").strip()
                linhas = txt.splitlines()
                for l in linhas:
                    if l.strip().startswith("|") and "**" in l and "Rank" not in l and "---" not in l:
                        partes = [c.strip() for c in l.split("|")[1:-1]]
                        if len(partes) >= 3:
                            nome = partes[1].replace("**", "").strip()
                            lic = partes[2].replace("`", "").strip() if len(partes) > 2 else "OSI"
                            saas = partes[3] if len(partes) > 3 else "Proprietário"
                            econ = partes[4] if len(partes) > 4 else "R$ 60.000/ano"
                            ferramentas.append({
                                "rank": len(ferramentas) + 1,
                                "nome": nome,
                                "licenca_osi": lic,
                                "saas_substituido": saas,
                                "economia_anual_str": econ
                            })
            dados = {
                "titulo": titulo,
                "camada": slug.replace("-", " ").title(),
                "ferramentas": ferramentas
            }

        try:
            gerar_relatorio_tripartite_fluxo1(slug, dados, materiais_dir, relatorios_dir)
            sucessos += 1
        except Exception as e:
            print(f"   ❌ Erro em list-{slug}: {e}")

    print(f"✅ Fluxo 1: {sucessos}/{len(pastas)} relatórios gerados com sucesso.")


def recompilar_fluxo2():
    print("\n" + "="*80)
    print(" 🚀 RECOMPILANDO RELATÓRIOS DO FLUXO 2 (DOSSIÊS VERTICAIS) · NÍVEL ENTERPRISE")
    print("="*80)
    pastas = sorted(glob.glob(str(BASE_DIR / "output" / "02-dossies-verticais" / "vert-*")))
    print(f"Total de pastas encontradas: {len(pastas)}")

    sucessos = 0
    for pasta_str in pastas:
        p = Path(pasta_str)
        saas_slug = p.name.replace("vert-", "")
        materiais_dir = p / "materiais"
        relatorios_dir = p / "relatorios"
        relatorios_dir.mkdir(parents=True, exist_ok=True)

        dados = {}
        possiveis_json = [
            BASE_DIR / "scripts" / "data" / f"dossie-vertical-{saas_slug}.json",
            BASE_DIR / "scripts" / "data" / f"dossie-{saas_slug}.json",
            BASE_DIR / "scripts" / "data" / f"{saas_slug}.json",
        ]
        for pj in possiveis_json:
            if pj.exists():
                try:
                    dados = json.loads(pj.read_text(encoding="utf-8"))
                    break
                except Exception:
                    pass

        if not dados:
            md_mat = materiais_dir / f"vert-{saas_slug}.md"
            quinteto = []
            saas_nome = saas_slug.replace("-", " ").title()
            preco_medio = "R$ 60.000 a R$ 300.000/ano"
            riscos = "Retenção de metadados corporativos, telemetria invasiva e vendor lock-in."

            if md_mat.exists():
                txt = md_mat.read_text(encoding="utf-8", errors="replace")
                m_tit = re.search(r"^# (.+)$", txt, re.MULTILINE)
                if m_tit:
                    saas_nome = m_tit.group(1).replace("Dossiê Vertical de Desmantelamento SaaS:", "").strip()
                linhas = txt.splitlines()
                for l in linhas:
                    if l.strip().startswith("|") and "**" in l and "Rank" not in l and "---" not in l:
                        partes = [c.strip() for c in l.split("|")[1:-1]]
                        if len(partes) >= 3:
                            rank_num = len(quinteto) + 1
                            cls = partes[1].replace("*", "").strip() if len(partes) > 1 else "Canônica"
                            nome = partes[2].replace("**", "").strip() if len(partes) > 2 else "Ferramenta"
                            lic = partes[3].replace("`", "").strip() if len(partes) > 3 else "OSI"
                            quinteto.append({
                                "rank": rank_num,
                                "classificacao": cls,
                                "nome": nome,
                                "licenca_osi": lic,
                                "design_system": {"esforco": "Baixo"}
                            })

            dados = {
                "saas_em_foco": {
                    "nome": saas_nome,
                    "preco_medio": preco_medio,
                    "riscos_privacidade": riscos
                },
                "quinteto": quinteto
            }

        try:
            gerar_relatorio_tripartite_fluxo2(saas_slug, dados, materiais_dir, relatorios_dir)
            sucessos += 1
        except Exception as e:
            print(f"   ❌ Erro em vert-{saas_slug}: {e}")

    print(f"✅ Fluxo 2: {sucessos}/{len(pastas)} relatórios gerados com sucesso.")


def recompilar_fluxo3():
    print("\n" + "="*80)
    print(" 🚀 RECOMPILANDO RELATÓRIOS DO FLUXO 3 (MANUAIS & TRILHAS VPS) · NÍVEL ENTERPRISE")
    print("="*80)
    base_f3 = BASE_DIR / "output" / "03-manuais-e-trilhas"
    pastas_saas = sorted([d for d in base_f3.glob("*") if d.is_dir()])

    sucessos = 0
    total = 0
    for ps in pastas_saas:
        saas_slug = ps.name
        pastas_ferramentas = sorted([d for d in ps.glob("*") if d.is_dir()])
        for pf in pastas_ferramentas:
            ferramenta_slug = pf.name
            total += 1
            try:
                gerar_relatorio_tripartite_fluxo3(ferramenta_slug, saas_slug, pf)
                sucessos += 1
            except Exception as e:
                print(f"   ❌ Erro em {saas_slug}/{ferramenta_slug}: {e}")

    print(f"✅ Fluxo 3: {sucessos}/{total} relatórios gerados com sucesso.")


if __name__ == "__main__":
    inicio = datetime.now()
    recompilar_fluxo1()
    recompilar_fluxo2()
    recompilar_fluxo3()
    fim = datetime.now()
    duracao = (fim - inicio).total_seconds()
    print("\n" + "="*80)
    print(f" 🎉 RECOMPILAÇÃO TOTAL ENTERPRISE CONCLUÍDA EM {duracao:.2f} SEGUNDOS!")
    print("="*80)
