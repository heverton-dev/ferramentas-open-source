# -*- coding: utf-8 -*-
"""
SUÍTE DE TESTES UNITÁRIOS AUTOMATIZADOS: FLUXO 1 (LISTAS HORIZONTAIS AIDD)
Valida a integridade de ponta a ponta:
1. Existência e Conformidade dos Compêndios Temáticos
2. Compilação Tripartite (HTML, MD, Typst PDF)
3. Auditoria Mecânica R5 (Padrão Diamante)
4. Persistência Relacional em SQLite (estado_esteira.db - Regra R11)
5. Paridade Estrita de Espelhos (Regra R18)
"""
import unittest
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

class TestFluxo1Listas(unittest.TestCase):

    def setUp(self):
        self.slug_teste = "bancos-dados-estado"
        self.html_file = BASE_DIR / "output" / "listas-open-source" / f"list-{self.slug_teste}.html"
        self.db_path = BASE_DIR / "estado_esteira.db"

    def test_01_compendio_html_diamante_existe(self):
        """Valida se o compêndio temático HTML existe na pasta output/listas-open-source/."""
        self.assertTrue(self.html_file.exists(), f"Compêndio HTML list-{self.slug_teste}.html não encontrado.")
        self.assertGreater(self.html_file.stat().st_size, 1000, "Arquivo HTML deve possuir mais de 1 KB.")

    def test_02_compilacao_tripartite_bundle(self):
        """Valida se os 3 formatos (HTML, MD, PDF) foram gerados no bundle modular."""
        bundle_dir = BASE_DIR / "output" / "listas-tematicas" / f"list-{self.slug_teste}"
        formatos = ["html", "md", "pdf"]

        for fmt in formatos:
            arquivo = bundle_dir / f"list-{self.slug_teste}.{fmt}"
            self.assertTrue(arquivo.exists(), f"Arquivo .{fmt} não encontrado em {bundle_dir}")
            self.assertGreater(arquivo.stat().st_size, 0, f"Arquivo .{fmt} está vazio.")

    def test_03_auditoria_mecanica_r5_diamante(self):
        """Valida que o HTML contém os elementos obrigatórios do Padrão Diamante R5."""
        conteudo = self.html_file.read_text(encoding="utf-8")
        self.assertIn("<h1", conteudo, "Deve conter título principal H1.")
        self.assertTrue("deck" in conteudo or "container" in conteudo, "Deve conter estrutura padrão de container ou deck.")

    def test_04_persistencia_sqlite_r11(self):
        """Valida registro e leitura da lista horizontal no banco SQLite estado_esteira.db."""
        sys.path.insert(0, str(BASE_DIR / "scripts"))
        from estado_esteira import listar_listas_horizontais

        listas = listar_listas_horizontais()
        slugs = [l["slug"] for l in listas]
        self.assertIn(self.slug_teste, slugs, f"Lista {self.slug_teste} deve estar registrada no SQLite.")

    def test_05_paridade_espelhos_docs_r18(self):
        """Valida paridade estrita entre output/ e docs/ para a lista temática."""
        out_file = BASE_DIR / "output" / "listas-tematicas" / f"list-{self.slug_teste}" / f"list-{self.slug_teste}.html"
        doc_file = BASE_DIR / "docs" / "listas-tematicas" / f"list-{self.slug_teste}" / f"list-{self.slug_teste}.html"

        self.assertTrue(out_file.exists() and doc_file.exists(), "Arquivos HTML de espelho devem existir.")
        self.assertEqual(out_file.stat().st_size, doc_file.stat().st_size, "Tamanho entre output/ e docs/ deve ser idêntico.")

if __name__ == "__main__":
    unittest.main()
