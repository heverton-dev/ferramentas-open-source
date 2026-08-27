# -*- coding: utf-8 -*-
"""
POPULADOR & PARSER DO CATÁLOGO MESTRE CANÔNICO (SQLITE R11)
Varre determinísticamente 100% dos bundles de output/ e extrai:
- Entidades únicas de ferramentas open source
- Matriz de rastreabilidade cruzada (onde cada ferramenta é citada, classificada ou documentada)
"""
import sys
import json
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

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR / "scripts"))

from estado_esteira import (
    inicializar_banco,
    registrar_ferramenta_catalogo,
    registrar_rastreabilidade_material,
    obter_estatisticas_catalogo
)

# Dicionário de Aliases Canônicos para Desduplicação Inteligente
ALIASES_CANONICOS = {
    "waha-plus": "waha",
    "waha-http": "waha",
    "waha-whatsapp-http-api-gateway": "waha",
    "whisper.cpp": "whisper-cpp",
    "whisper_cpp": "whisper-cpp",
    "faster-whisper": "faster-whisper-cli",
    "open-notebook-lm": "open-notebooklm",
    "open_notebooklm": "open-notebooklm",
    "typebot.io": "typebot",
    "n8n.io": "n8n",
    "supabase-oss": "supabase",
    "chatwoot-ce": "chatwoot",
    "posthog-ce": "posthog",
    "minio-oss": "minio",
    "appflowy-io": "appflowy",
    "affine-pro": "affine",
    "mail-in-a-box": "mailinabox",
    "postfix-e-dovecot": "postfix-dovecot",
    "screenpipe-desktop": "screenpipe"
}

def normalizar_slug(nome: str) -> str:
    slug = nome.lower().strip()
    slug = re.sub(r'[\(\)\[\]\{\}\'\"\,\.\:\/\+\#]', '', slug)
    slug = re.sub(r'[\s\_]+', '-', slug)
    slug = re.sub(r'-+', '-', slug).strip('-')
    slug = slug[:40]
    return ALIASES_CANONICOS.get(slug, slug)

def ingerir_listas_horizontais():
    print("\n📦 Ingerindo Listas Horizontais (Fluxo 1)...")
    pastas = sorted(glob.glob(str(BASE_DIR / "output" / "01-listas-horizontais" / "list-*")))
    cont_f = 0

    for pasta_str in pastas:
        p = Path(pasta_str)
        slug_lista = p.name.replace("list-", "")
        mat_dir = p / "materiais"
        html_p = mat_dir / f"list-{slug_lista}.html"
        md_p   = mat_dir / f"list-{slug_lista}.md"
        pdf_p  = mat_dir / f"list-{slug_lista}.pdf"

        # Tenta carregar do JSON de dados se existir
        dados = {}
        possiveis_json = [
            BASE_DIR / "scripts" / "data" / f"dossie-{slug_lista}.json",
            BASE_DIR / "scripts" / "data" / f"{slug_lista}.json"
        ]
        for pj in possiveis_json:
            if pj.exists():
                try:
                    dados = json.loads(pj.read_text(encoding="utf-8"))
                    break
                except Exception:
                    pass

        titulo_lista = dados.get("titulo", slug_lista.replace("-", " ").title())
        ferramentas = dados.get("ferramentas", [])

        # Se não tiver JSON estruturado, extrai da tabela do Markdown
        if not ferramentas and md_p.exists():
            txt = md_p.read_text(encoding="utf-8", errors="replace")
            m_tit = re.search(r"^# (.+)$", txt, re.MULTILINE)
            if m_tit:
                titulo_lista = m_tit.group(1).replace("Compêndio Diamante:", "").strip()
            linhas = txt.splitlines()
            for l in linhas:
                if l.strip().startswith("|") and "**" in l and "Rank" not in l and "---" not in l:
                    partes = [c.strip() for c in l.split("|")[1:-1]]
                    if len(partes) >= 3:
                        nome = partes[1].replace("**", "").strip()
                        lic = partes[2].replace("`", "").strip() if len(partes) > 2 else "OSI"
                        saas = partes[3] if len(partes) > 3 else "Proprietário"
                        ferramentas.append({
                            "rank": len(ferramentas) + 1,
                            "nome": nome,
                            "licenca_osi": lic,
                            "saas_substituido": saas,
                            "repo_url": ""
                        })

        for idx, f in enumerate(ferramentas):
            nome_f = f.get("nome", "Ferramenta")
            slug_f = f.get("slug") or normalizar_slug(nome_f)
            lic_f  = f.get("licenca_osi", "OSI")
            repo_f = f.get("repo_url", "")
            saas_sub = f.get("saas_substituido", "")
            desc_f = f.get("descricao", f"Solução open source líder para {slug_lista.replace('-', ' ')}.")
            rank_str = f"#{f.get('rank', idx+1):02d}"

            # 1. Registra no catálogo
            registrar_ferramenta_catalogo({
                "slug": slug_f,
                "nome": nome_f,
                "licenca_osi": lic_f,
                "categoria_primaria": slug_lista.replace("-", " ").title(),
                "repo_url": repo_f,
                "stack_tecnologica": "Open Source",
                "descricao_canonica": desc_f,
                "saas_substituidos": saas_sub,
                "possui_manual_vps": False
            })

            # 2. Registra na rastreabilidade
            registrar_rastreabilidade_material({
                "ferramenta_slug": slug_f,
                "tipo_material": "horizontal",
                "origem_slug": slug_lista,
                "titulo_material": titulo_lista,
                "posicao_ou_rank": rank_str,
                "caminho_html": str(html_p.relative_to(BASE_DIR)).replace("\\", "/") if html_p.exists() else "",
                "caminho_md": str(md_p.relative_to(BASE_DIR)).replace("\\", "/") if md_p.exists() else "",
                "caminho_pdf": str(pdf_p.relative_to(BASE_DIR)).replace("\\", "/") if pdf_p.exists() else ""
            })
            cont_f += 1

    print(f"   ✓ {len(pastas)} listas processadas ({cont_f} vínculos criados).")

def ingerir_dossies_verticais():
    print("\n⚔️ Ingerindo Dossiês Verticais & Quinteto Soberano (Fluxo 2)...")
    pastas = sorted(glob.glob(str(BASE_DIR / "output" / "02-dossies-verticais" / "vert-*")))
    cont_q = 0

    for pasta_str in pastas:
        p = Path(pasta_str)
        saas_slug = p.name.replace("vert-", "")
        mat_dir = p / "materiais"
        html_p = mat_dir / f"vert-{saas_slug}.html"
        md_p   = mat_dir / f"vert-{saas_slug}.md"
        pdf_p  = mat_dir / f"vert-{saas_slug}.pdf"

        dados = {}
        possiveis_json = [
            BASE_DIR / "scripts" / "data" / f"dossie-vertical-{saas_slug}.json",
            BASE_DIR / "scripts" / "data" / f"dossie-{saas_slug}.json",
            BASE_DIR / "scripts" / "data" / f"{saas_slug}.json"
        ]
        for pj in possiveis_json:
            if pj.exists():
                try:
                    dados = json.loads(pj.read_text(encoding="utf-8"))
                    break
                except Exception:
                    pass

        saas_info = dados.get("saas_em_foco", {})
        saas_nome = saas_info.get("nome", saas_slug.replace("-", " ").title())
        quinteto = dados.get("quinteto", [])

        if not quinteto and md_p.exists():
            txt = md_p.read_text(encoding="utf-8", errors="replace")
            linhas = txt.splitlines()
            for l in linhas:
                if l.strip().startswith("|") and "**" in l and "Rank" not in l and "---" not in l:
                    partes = [c.strip() for c in l.split("|")[1:-1]]
                    if len(partes) >= 3:
                        cls = partes[1].replace("*", "").strip() if len(partes) > 1 else "Canônica"
                        nome = partes[2].replace("**", "").strip() if len(partes) > 2 else "Ferramenta"
                        lic = partes[3].replace("`", "").strip() if len(partes) > 3 else "OSI"
                        quinteto.append({
                            "rank": len(quinteto) + 1,
                            "classificacao": cls,
                            "nome": nome,
                            "licenca_osi": lic
                        })

        for idx, q in enumerate(quinteto):
            nome_q = q.get("nome", "Ferramenta")
            slug_q = q.get("slug") or normalizar_slug(nome_q)
            lic_q  = q.get("licenca_osi", "OSI")
            cls_q  = q.get("classificacao", "Canônica")
            repo_q = q.get("repositorio_oficial", "")
            desc_q = q.get("o_que_faz", f"Alternativa open source soberana ao SaaS {saas_nome}.")

            # 1. Registra no catálogo
            registrar_ferramenta_catalogo({
                "slug": slug_q,
                "nome": nome_q,
                "licenca_osi": lic_q,
                "categoria_primaria": "Substituição SaaS",
                "repo_url": repo_q,
                "stack_tecnologica": "Open Source",
                "descricao_canonica": desc_q,
                "saas_substituidos": saas_nome,
                "possui_manual_vps": False
            })

            # 2. Registra na rastreabilidade
            registrar_rastreabilidade_material({
                "ferramenta_slug": slug_q,
                "tipo_material": "vertical",
                "origem_slug": saas_slug,
                "titulo_material": f"Desmantelamento SaaS: {saas_nome}",
                "posicao_ou_rank": f"Quinteto: {cls_q}",
                "caminho_html": str(html_p.relative_to(BASE_DIR)).replace("\\", "/") if html_p.exists() else "",
                "caminho_md": str(md_p.relative_to(BASE_DIR)).replace("\\", "/") if md_p.exists() else "",
                "caminho_pdf": str(pdf_p.relative_to(BASE_DIR)).replace("\\", "/") if pdf_p.exists() else ""
            })
            cont_q += 1

    print(f"   ✓ {len(pastas)} dossiês verticais processados ({cont_q} vínculos criados).")

def ingerir_manuais_e_trilhas():
    print("\n🛠️ Ingerindo Manuais & Trilhas VPS (Fluxo 3)...")
    base_f3 = BASE_DIR / "output" / "03-manuais-e-trilhas"
    pastas_saas = sorted([d for d in base_f3.glob("*") if d.is_dir()])
    cont_m = 0

    for ps in pastas_saas:
        saas_slug = ps.name
        pastas_ferramentas = sorted([d for d in ps.glob("*") if d.is_dir()])
        for pf in pastas_ferramentas:
            ferramenta_slug = pf.name
            
            # Manual Duplo
            man_html = pf / "manuais" / f"manual-{ferramenta_slug}-vps-e-uso.html"
            man_md   = pf / "manuais" / f"manual-{ferramenta_slug}-vps-e-uso.md"
            man_pdf  = pf / "manuais" / f"manual-{ferramenta_slug}-vps-e-uso.pdf"

            # Trilha 5 Aulas
            tri_html = pf / "trilhas" / f"trilha-{ferramenta_slug}-aprendizado.html"
            tri_md   = pf / "trilhas" / f"trilha-{ferramenta_slug}-aprendizado.md"
            tri_pdf  = pf / "trilhas" / f"trilha-{ferramenta_slug}-aprendizado.pdf"

            # 1. Atualiza no catálogo sinalizando posse de manual VPS
            registrar_ferramenta_catalogo({
                "slug": ferramenta_slug,
                "nome": ferramenta_slug.replace("-", " ").title(),
                "licenca_osi": "OSI",
                "possui_manual_vps": True
            })

            # 2. Registra manual na rastreabilidade
            if man_html.exists() or man_md.exists():
                registrar_rastreabilidade_material({
                    "ferramenta_slug": ferramenta_slug,
                    "tipo_material": "manual_vps",
                    "origem_slug": saas_slug,
                    "titulo_material": f"Manual VPS & Uso: {ferramenta_slug.title()}",
                    "posicao_ou_rank": "Manual Completo",
                    "caminho_html": str(man_html.relative_to(BASE_DIR)).replace("\\", "/") if man_html.exists() else "",
                    "caminho_md": str(man_md.relative_to(BASE_DIR)).replace("\\", "/") if man_md.exists() else "",
                    "caminho_pdf": str(man_pdf.relative_to(BASE_DIR)).replace("\\", "/") if man_pdf.exists() else ""
                })

            # 3. Registra trilha na rastreabilidade
            if tri_html.exists() or tri_md.exists():
                registrar_rastreabilidade_material({
                    "ferramenta_slug": ferramenta_slug,
                    "tipo_material": "trilha",
                    "origem_slug": saas_slug,
                    "titulo_material": f"Trilha Didática 5 Aulas: {ferramenta_slug.title()}",
                    "posicao_ou_rank": "Curso Prático",
                    "caminho_html": str(tri_html.relative_to(BASE_DIR)).replace("\\", "/") if tri_html.exists() else "",
                    "caminho_md": str(tri_md.relative_to(BASE_DIR)).replace("\\", "/") if tri_md.exists() else "",
                    "caminho_pdf": str(tri_pdf.relative_to(BASE_DIR)).replace("\\", "/") if tri_pdf.exists() else ""
                })
            cont_m += 1

    print(f"   ✓ {cont_m} pacotes de manuais/trilhas ingeridos.")

def executar_ingestao_completa():
    print("=" * 80)
    print(" 🚀 INGESTÃO & CONSTRUÇÃO DO CATÁLOGO MESTRE CANÔNICO (SQLITE R11)")
    print("=" * 80)
    inicializar_banco()
    ingerir_listas_horizontais()
    ingerir_dossies_verticais()
    ingerir_manuais_e_trilhas()

    stats = obter_estatisticas_catalogo()
    print("\n" + "=" * 80)
    print(f" 🎉 CATÁLOGO MESTRE CONSOLIDADO COM SUCESSO!")
    print(f" [*] Total de Ferramentas Únicas Catalogadas: {stats['total_ferramentas']}")
    print(f" [*] Listas Horizontais Mapeadas: {stats['total_listas']}")
    print(f" [*] Dossiês Verticais Mapeados: {stats['total_verticais']}")
    print(f" [*] Manuais VPS Registrados: {stats['total_manuais']}")
    print("=" * 80)

if __name__ == "__main__":
    executar_ingestao_completa()
