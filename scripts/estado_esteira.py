# -*- coding: utf-8 -*-
"""
MÓDULO DE ESTADO PERSISTENTE DA ESTEIRA (REGRA R11 & CAMADA 4 TOOLS)
Implementa um banco de dados relacional SQLite local ('estado_esteira.db')
para rastrear o progresso de tarefas, histórico de execuções de gates,
fichas técnicas e métricas sem depender da memória volátil da conversa.
"""
import os
import sys
import sqlite3
import datetime

def console_utf8():
    if sys.platform == "win32":
        try:
            sys.stdout.reconfigure(encoding="utf-8")
            sys.stderr.reconfigure(encoding="utf-8")
        except Exception:
            pass

console_utf8()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "estado_esteira.db")

def obter_conexao():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def inicializar_banco():
    with obter_conexao() as conn:
        cursor = conn.cursor()
        
        # Tabela de Sessões
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS sessoes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data TEXT NOT NULL,
                tema TEXT NOT NULL,
                status TEXT NOT NULL,
                criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # Tabela de Auditorias e Gates
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS auditorias_gates (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                camada TEXT NOT NULL,
                gate_nome TEXT NOT NULL,
                status_saida INTEGER NOT NULL,
                detalhes TEXT,
                executado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # Tabela de Ferramentas Catalogadas
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ferramentas_catalogadas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                camada_num INTEGER NOT NULL,
                rank INTEGER NOT NULL,
                nome TEXT NOT NULL,
                saas_substituido TEXT,
                licenca TEXT,
                github_repo TEXT,
                atualizado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(camada_num, rank)
            )
        """)

        # Tabela de Bundles da Esteira de Manuais & Trilhas (AI Driven)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS esteira_manuais_bundles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                slug TEXT NOT NULL,
                saas_origem TEXT NOT NULL,
                data_execucao TEXT NOT NULL,
                horario_inicio TEXT,
                horario_fim TEXT,
                duracao_seg REAL,
                tokens_totais INTEGER,
                taxa_economia TEXT,
                gate_g0 TEXT,
                gate_g1 TEXT,
                gate_g2 TEXT,
                gate_r18 TEXT,
                total_arquivos INTEGER DEFAULT 9,
                caminho_bundle TEXT,
                atualizado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(slug, saas_origem)
            )
        """)

        # Tabela de Dossiês Verticais de Desmantelamento SaaS (Fluxo 2)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS esteira_dossies_verticais (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                saas_slug TEXT NOT NULL UNIQUE,
                saas_nome TEXT NOT NULL,
                preco_anual_dolar REAL,
                quinteto_ferramentas TEXT NOT NULL,
                total_ferramentas INTEGER DEFAULT 5,
                gate_r5v TEXT DEFAULT 'APROVADO',
                gate_r18 TEXT DEFAULT 'APROVADO',
                caminho_html TEXT,
                caminho_md TEXT,
                caminho_pdf TEXT,
                atualizado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # Tabela de Listas Horizontais / Compêndios Temáticos (Fluxo 1)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS esteira_listas_horizontais (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                slug TEXT NOT NULL UNIQUE,
                titulo TEXT NOT NULL,
                total_ferramentas INTEGER NOT NULL,
                gate_r5 TEXT DEFAULT 'APROVADO',
                gate_r18 TEXT DEFAULT 'APROVADO',
                caminho_html TEXT,
                caminho_md TEXT,
                caminho_pdf TEXT,
                atualizado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()

def registrar_lista_horizontal(dados: dict):
    """Registra ou atualiza uma Lista Horizontal do Fluxo 1 no SQLite."""
    inicializar_banco()
    with obter_conexao() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO esteira_listas_horizontais (
                slug, titulo, total_ferramentas, gate_r5, gate_r18, caminho_html, caminho_md, caminho_pdf
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(slug) DO UPDATE SET
                titulo = excluded.titulo,
                total_ferramentas = excluded.total_ferramentas,
                gate_r5 = excluded.gate_r5,
                gate_r18 = excluded.gate_r18,
                caminho_html = excluded.caminho_html,
                caminho_md = excluded.caminho_md,
                caminho_pdf = excluded.caminho_pdf,
                atualizado_em = CURRENT_TIMESTAMP
        """, (
            dados["slug"],
            dados.get("titulo", dados["slug"].replace("-", " ").title()),
            dados.get("total_ferramentas", 0),
            dados.get("gate_r5", "APROVADO"),
            dados.get("gate_r18", "APROVADO"),
            dados.get("caminho_html", f"output/listas-open-source/list-{dados['slug']}.html"),
            dados.get("caminho_md", f"output/listas-open-source/list-{dados['slug']}.md"),
            dados.get("caminho_pdf", f"output/listas-open-source/list-{dados['slug']}.pdf")
        ))
        conn.commit()

def listar_listas_horizontais() -> list[dict]:
    """Retorna todas as listas horizontais registradas no banco."""
    inicializar_banco()
    with obter_conexao() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM esteira_listas_horizontais ORDER BY id ASC")
        return [dict(r) for r in cursor.fetchall()]

def registrar_dossie_vertical(dados: dict):
    """Registra ou atualiza um Dossiê Vertical do Fluxo 2 no SQLite."""
    inicializar_banco()
    with obter_conexao() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO esteira_dossies_verticais (
                saas_slug, saas_nome, preco_anual_dolar, quinteto_ferramentas,
                total_ferramentas, gate_r5v, gate_r18, caminho_html, caminho_md, caminho_pdf
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(saas_slug) DO UPDATE SET
                saas_nome = excluded.saas_nome,
                preco_anual_dolar = excluded.preco_anual_dolar,
                quinteto_ferramentas = excluded.quinteto_ferramentas,
                total_ferramentas = excluded.total_ferramentas,
                gate_r5v = excluded.gate_r5v,
                gate_r18 = excluded.gate_r18,
                caminho_html = excluded.caminho_html,
                caminho_md = excluded.caminho_md,
                caminho_pdf = excluded.caminho_pdf,
                atualizado_em = CURRENT_TIMESTAMP
        """, (
            dados["saas_slug"],
            dados.get("saas_nome", dados["saas_slug"].title()),
            dados.get("preco_anual_dolar", 0.0),
            dados.get("quinteto_ferramentas", ""),
            dados.get("total_ferramentas", 5),
            dados.get("gate_r5v", "APROVADO"),
            dados.get("gate_r18", "APROVADO"),
            dados.get("caminho_html", f"output/listas-open-source/vert-{dados['saas_slug']}.html"),
            dados.get("caminho_md", f"output/listas-open-source/vert-{dados['saas_slug']}.md"),
            dados.get("caminho_pdf", f"output/listas-open-source/vert-{dados['saas_slug']}.pdf")
        ))
        conn.commit()

def listar_dossies_verticais() -> list[dict]:
    """Retorna todos os dossiês verticais registrados no banco."""
    inicializar_banco()
    with obter_conexao() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM esteira_dossies_verticais ORDER BY id ASC")
        return [dict(r) for r in cursor.fetchall()]

def registrar_bundle_esteira(dados: dict):
    """Registra ou atualiza um bundle completo na esteira_manuais_bundles."""
    inicializar_banco()
    with obter_conexao() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO esteira_manuais_bundles (
                slug, saas_origem, data_execucao, horario_inicio, horario_fim,
                duracao_seg, tokens_totais, taxa_economia, gate_g0, gate_g1,
                gate_g2, gate_r18, total_arquivos, caminho_bundle
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(slug, saas_origem) DO UPDATE SET
                data_execucao = excluded.data_execucao,
                horario_inicio = excluded.horario_inicio,
                horario_fim = excluded.horario_fim,
                duracao_seg = excluded.duracao_seg,
                tokens_totais = excluded.tokens_totais,
                taxa_economia = excluded.taxa_economia,
                gate_g0 = excluded.gate_g0,
                gate_g1 = excluded.gate_g1,
                gate_g2 = excluded.gate_g2,
                gate_r18 = excluded.gate_r18,
                total_arquivos = excluded.total_arquivos,
                caminho_bundle = excluded.caminho_bundle,
                atualizado_em = CURRENT_TIMESTAMP
        """, (
            dados["slug"],
            dados["saas_origem"],
            dados["data_execucao"],
            dados.get("horario_inicio", ""),
            dados.get("horario_fim", ""),
            dados.get("duracao_seg", 0.0),
            dados.get("tokens_totais", 0),
            dados.get("taxa_economia", ""),
            dados.get("gate_g0", "APROVADO"),
            dados.get("gate_g1", "APROVADO"),
            dados.get("gate_g2", "APROVADO"),
            dados.get("gate_r18", "APROVADO"),
            dados.get("total_arquivos", 9),
            dados.get("caminho_bundle", f"output/{dados['slug']}/")
        ))
        conn.commit()

def listar_bundles_esteira() -> list[dict]:
    """Retorna todos os bundles registrados no banco."""
    inicializar_banco()
    with obter_conexao() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM esteira_manuais_bundles ORDER BY id ASC")
        return [dict(r) for r in cursor.fetchall()]

def registrar_execucao_gate(camada: str, gate_nome: str, exit_code: int, detalhes: str = ""):
    inicializar_banco()
    with obter_conexao() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO auditorias_gates (camada, gate_nome, status_saida, detalhes)
            VALUES (?, ?, ?, ?)
        """, (camada, gate_nome, exit_code, detalhes))
        conn.commit()

def consultar_resumo_estado() -> dict:
    inicializar_banco()
    with obter_conexao() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) as total FROM auditorias_gates WHERE status_saida = 0")
        gates_ok = cursor.fetchone()["total"]
        
        cursor.execute("SELECT COUNT(*) as total FROM auditorias_gates WHERE status_saida != 0")
        gates_falha = cursor.fetchone()["total"]

        return {
            "db_path": DB_PATH,
            "gates_sucesso": gates_ok,
            "gates_falha": gates_falha
        }

if __name__ == "__main__":
    inicializar_banco()
    registrar_execucao_gate("CAMADA_4", "init_estado_esteira", 0, "Banco SQLite inicializado com sucesso.")
    resumo = consultar_resumo_estado()
    print("=" * 80)
    print(" 🔧 ESTADO PERSISTENTE DA ESTEIRA (SQLITE R11 - CAMADA 4)")
    print("=" * 80)
    print(f" [*] Banco de Dados: {resumo['db_path']}")
    print(f" [*] Registros de Gates Aprovados: {resumo['gates_sucesso']}")
    print(f" [*] Registros de Gates com Falha: {resumo['gates_falha']}")
    print("=" * 80)
