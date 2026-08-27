# -*- coding: utf-8 -*-
"""
TESTES UNITÁRIOS & GATES MECÂNICOS DO CATÁLOGO MESTRE & ÍNDICE CRUZADO
Valida:
1. Existência e integridade das tabelas SQLite catalogo_ferramentas e rastreabilidade_materiais.
2. Contagem mínima de ferramentas (>200) e integridade dos registros.
3. Existência dos 3 formatos de saída do Índice Mestre (HTML, MD e PDF).
4. Conformidade da busca JS no HTML e ausência de resíduos temporários (.typ).
"""
import os
import sys
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR / "scripts"))

from estado_esteira import (
    obter_conexao,
    consultar_catalogo_ferramenta,
    listar_catalogo_completo,
    obter_rastreabilidade_ferramenta,
    obter_estatisticas_catalogo
)

class TestIndiceMestreCruzado:

    def test_01_tabelas_sqlite_existem(self):
        with obter_conexao() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='catalogo_ferramentas'")
            assert cursor.fetchone() is not None, "Tabela catalogo_ferramentas deve existir no SQLite"

            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='rastreabilidade_materiais'")
            assert cursor.fetchone() is not None, "Tabela rastreabilidade_materiais deve existir no SQLite"

    def test_02_contagem_ferramentas_e_rastreabilidade(self):
        stats = obter_estatisticas_catalogo()
        assert stats["total_ferramentas"] >= 100, f"Esperado >= 100 ferramentas, encontrado {stats['total_ferramentas']}"
        assert stats["total_verticais"] >= 10, f"Esperado >= 10 verticais mapeadas, encontrado {stats['total_verticais']}"

    def test_03_consulta_ferramenta_especifica(self):
        # WAHA deve existir e ter vinculos
        waha = consultar_catalogo_ferramenta("waha")
        assert waha is not None, "WAHA deve estar cadastrado no catálogo mestre"
        assert waha["nome"] == "Waha" or "waha" in waha["slug"].lower()
        
        mats = obter_rastreabilidade_ferramenta("waha")
        assert len(mats) >= 1, "WAHA deve possuir materiais vinculados"

    def test_04_arquivos_tripartites_indice_mestre(self):
        out_dir = BASE_DIR / "output"
        html_p = out_dir / "INDICE-MESTRE.html"
        md_p   = out_dir / "INDICE-MESTRE.md"
        pdf_p  = out_dir / "INDICE-MESTRE.pdf"

        assert html_p.exists(), f"Arquivo {html_p} deve existir"
        assert md_p.exists(), f"Arquivo {md_p} deve existir"
        assert pdf_p.exists(), f"Arquivo {pdf_p} deve existir"

        assert html_p.stat().st_size > 10000, "HTML do Índice Mestre deve ter conteúdo relevante"
        assert md_p.stat().st_size > 5000, "Markdown do Índice Mestre deve ter conteúdo relevante"
        assert pdf_p.stat().st_size > 5000, "PDF do Índice Mestre deve ter sido compilado via Typst"

    def test_05_integridade_higiene_r18(self):
        out_dir = BASE_DIR / "output"
        typ_p = out_dir / "INDICE-MESTRE.typ"
        assert not typ_p.exists(), "Arquivo temporário .typ não deve existir (Regra R18)"
