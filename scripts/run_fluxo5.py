# -*- coding: utf-8 -*-
import os
import sys
import argparse
import sqlite3
import datetime

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

from modulos.vps_client import PortainerClient
from modulos.vps_auditor import VPSAuditor
from modulos.vps_decision_engine import VPSDecisionEngine
from modulos.vps_generator import VPSGenerator

def init_db(db_path="estado_esteira.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS esteira_auditorias_vps (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tipo_alvo TEXT NOT NULL,
            slug_alvo TEXT NOT NULL,
            veredito TEXT NOT NULL,
            score INTEGER NOT NULL,
            caminho_saida TEXT NOT NULL,
            data_execucao TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def save_db(tipo_alvo, slug_alvo, veredito, score, caminho_saida, db_path="estado_esteira.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("""
        INSERT INTO esteira_auditorias_vps (tipo_alvo, slug_alvo, veredito, score, caminho_saida, data_execucao)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (tipo_alvo, slug_alvo, veredito, score, caminho_saida, now_str))
    conn.commit()
    conn.close()

def main():
    parser = argparse.ArgumentParser(description="Fluxo 5 — Auditoria, Incorporação e Desinstalação Cirúrgica em VPS (Multi-Alvo)")
    parser.add_argument("--ecossistema", help="Slug de um ecossistema único (ex: ecos-google-workspace)")
    parser.add_argument("--ferramenta", help="Slug de uma ferramenta única (ex: stalwart)")
    parser.add_argument("--ecossistemas", help="Lista de ecossistemas separados por vírgula")
    parser.add_argument("--ferramentas", help="Lista de ferramentas separadas por vírgula")
    parser.add_argument("--todos-ecossistemas", action="store_true", help="Auditar todos os ecossistemas cadastrados")
    parser.add_argument("--todas-ferramentas", action="store_true", help="Auditar todas as ferramentas cadastradas")
    parser.add_argument("--todos", action="store_true", help="Auditar todos os ecossistemas e ferramentas")
    parser.add_argument("--base-domain", default="vpsconexao.org", help="Domínio base da VPS (default: vpsconexao.org)")

    args = parser.parse_args()

    init_db()

    targets_to_run = []

    if args.todos:
        for k in VPSDecisionEngine.ECOSYSTEM_PROFILES.keys():
            targets_to_run.append({"tipo": "ecossistema", "slug": k})
        for k in VPSDecisionEngine.TOOL_PROFILES.keys():
            targets_to_run.append({"tipo": "ferramenta", "slug": k})
    elif args.todos_ecossistemas:
        for k in VPSDecisionEngine.ECOSYSTEM_PROFILES.keys():
            targets_to_run.append({"tipo": "ecossistema", "slug": k})
    elif args.todas_ferramentas:
        for k in VPSDecisionEngine.TOOL_PROFILES.keys():
            targets_to_run.append({"tipo": "ferramenta", "slug": k})
    elif args.ecossistemas:
        for s in args.ecossistemas.split(","):
            s = s.strip()
            if s:
                targets_to_run.append({"tipo": "ecossistema", "slug": s})
    elif args.ferramentas:
        for s in args.ferramentas.split(","):
            s = s.strip()
            if s:
                targets_to_run.append({"tipo": "ferramenta", "slug": s})
    elif args.ecossistema:
        targets_to_run.append({"tipo": "ecossistema", "slug": args.ecossistema})
    elif args.ferramenta:
        targets_to_run.append({"tipo": "ferramenta", "slug": args.ferramenta})
    else:
        parser.print_help()
        sys.exit(1)

    print("[FLUXO 5] Conectando à API do Portainer para auditoria mecânica da VPS...")
    client = PortainerClient()
    client.authenticate()

    auditor = VPSAuditor(client)
    audit_data = auditor.audit()

    engine = VPSDecisionEngine(audit_data)

    print(f"[FLUXO 5] Auditoria concluída. Iniciando análise encadeada para {len(targets_to_run)} alvo(s)...\n")

    root_vps_output = os.path.join("output", "05-auditorias-vps")
    os.makedirs(root_vps_output, exist_ok=True)

    # Executar avaliação individual de cada alvo
    for target in targets_to_run:
        t_tipo = target["tipo"]
        t_slug = target["slug"]
        
        if t_tipo == "ecossistema":
            decision = engine.evaluate_ecosystem(t_slug)
            out_dir = os.path.join(root_vps_output, "ecossistemas", t_slug)
        else:
            decision = engine.evaluate_tool(t_slug)
            out_dir = os.path.join(root_vps_output, "ferramentas", t_slug)

        gen = VPSGenerator(audit_data, decision, out_dir, base_domain=args.base_domain)
        gen.generate_all()

        v = decision["verdict"]
        save_db(t_tipo, t_slug, v["status"], v["score"], out_dir)
        print(f" -> [{t_tipo.upper()}] {decision['profile']['name']}: {v['status']} (Score: {v['score']}/100)")

    # Se houver mais de 1 alvo, gerar relatório consolidado multi-alvo
    if len(targets_to_run) > 1:
        multi_decision = engine.evaluate_multi_target(targets_to_run)
        dummy_gen = VPSGenerator(audit_data, multi_decision["evaluations"][0], root_vps_output, base_domain=args.base_domain)
        consolidated_files = dummy_gen.generate_consolidated_report(multi_decision, root_vps_output)
        
        cumul = multi_decision["cumulative"]
        print("\n========================================================")
        print("  PAINEL CONSOLIDADO MULTI-ALVO (FLUXO 5)")
        print("========================================================")
        print(f"Veredito Global Conjunto: {cumul['status']} (Score: {cumul['score']}/100)")
        print(f"Demanda Total Conjunta: {cumul['total_req_cpu']} vCPUs | {cumul['total_req_ram']} GB RAM")
        print(f"Headroom Livre Restante: ~{cumul['free_cpu'] - cumul['total_req_cpu']:.1f} vCPUs | ~{cumul['free_ram'] - cumul['total_req_ram']:.1f} GB RAM")
        print("Relatório Consolidado:")
        for cf in consolidated_files:
            print(f"  - {cf}")
        print("========================================================\n")
        commit_msg = f"feat(fluxo5): auditoria multi-alvo vps ({len(targets_to_run)} alvos)"
    else:
        print(f"\nExecução concluída com sucesso para o alvo único. Artefatos em: {out_dir}\n")
        commit_msg = f"feat(fluxo5): auditoria e integracao vps ({targets_to_run[0]['slug']})"

    # Sincronização Git Automatizada R16
    try:
        from git_sync import executar_commit_e_push
        executar_commit_e_push(commit_msg)
    except Exception as e:
        print(f"[FLUXO 5] Aviso ao executar git sync: {e}")

if __name__ == "__main__":
    main()
