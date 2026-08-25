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
        conn.commit()

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
