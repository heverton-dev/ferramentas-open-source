# -*- coding: utf-8 -*-
"""
SUÍTE DE TESTES UNITÁRIOS AUTOMATIZADOS: FLUXO 1 (LISTAS HORIZONTAIS AIDD)
Valida a integridade de ponta a ponta:
1. Existência e Conformidade dos Compêndios Temáticos
2. Compilação Tripartite (HTML, MD, Typst PDF) em materiais/
3. Auditoria Mecânica R5 (Padrão Diamante)
4. Persistência Relacional em SQLite (estado_esteira.db - Regra R11)
5. Paridade Estrita de Espelhos (Regra R18)
6. Existência do Relatório de Execução em relatorios/
"""
import unittest
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

class TestFluxo1Listas(unittest.TestCase):

    def setUp(self):
        # Usa camada CX (gerada com o motor canônico novo, com materiais/ e relatorios/)
        self.slug_teste = "experiencia-usuario-cx"
        self.bundle_dir = BASE_DIR / "output" / "01-listas-horizontais" / f"list-{self.slug_teste}"
        self.materiais_dir = self.bundle_dir / "materiais"
        self.relatorios_dir = self.bundle_dir / "relatorios"
        self.html_file = self.materiais_dir / f"list-{self.slug_teste}.html"
        self.db_path = BASE_DIR / "estado_esteira.db"

    def test_01_compendio_html_diamante_existe(self):
        """Valida se o compêndio temático HTML existe na pasta materiais/."""
        self.assertTrue(self.html_file.exists(), f"Compêndio HTML list-{self.slug_teste}.html não encontrado em materiais/.")
        self.assertGreater(self.html_file.stat().st_size, 1000, "Arquivo HTML deve possuir mais de 1 KB.")

    def test_02_compilacao_tripartite_bundle(self):
        """Valida se os 3 formatos (HTML, MD, PDF) foram gerados na subpasta materiais/."""
        self.assertTrue(self.materiais_dir.exists(), f"Subpasta materiais/ não encontrada em {self.bundle_dir}")

        for fmt in ["html", "md", "pdf"]:
            arquivo = self.materiais_dir / f"list-{self.slug_teste}.{fmt}"
            self.assertTrue(arquivo.exists(), f"Arquivo .{fmt} não encontrado em materiais/")
            self.assertGreater(arquivo.stat().st_size, 0, f"Arquivo .{fmt} está vazio.")

    def test_03_auditoria_mecanica_r5_diamante(self):
        """Valida que o HTML contém os elementos obrigatórios do Padrão Diamante R5."""
        conteudo = self.html_file.read_text(encoding="utf-8")
        self.assertIn("<h1", conteudo, "Deve conter título principal H1.")
        self.assertTrue("deck" in conteudo or "container" in conteudo, "Deve conter estrutura padrão de container ou deck.")
        self.assertNotIn('<div class="cols"', conteudo, "Layout de 2 colunas espremidas (div.cols) é banido pela R5.")

    def test_04_persistencia_sqlite_r11(self):
        """Valida registro e leitura da lista horizontal no banco SQLite estado_esteira.db."""
        sys.path.insert(0, str(BASE_DIR / "scripts"))
        from estado_esteira import listar_listas_horizontais

        listas = listar_listas_horizontais()
        slugs = [l["slug"] for l in listas]
        self.assertIn(self.slug_teste, slugs, f"Lista {self.slug_teste} deve estar registrada no SQLite.")

    def test_05_integridade_soberana_r18(self):
        """Valida a integridade da pasta soberana com subpastas materiais/ e relatorios/."""
        self.assertTrue(self.bundle_dir.exists(), "Diretório soberano da lista horizontal deve existir.")
        self.assertTrue(self.materiais_dir.exists(), "Subpasta materiais/ deve existir no bundle.")
        self.assertTrue(self.relatorios_dir.exists(), "Subpasta relatorios/ deve existir no bundle.")

        # Valida presença dos 3 artefatos em materiais/
        for fmt in ["html", "md", "pdf"]:
            arquivo = self.materiais_dir / f"list-{self.slug_teste}.{fmt}"
            self.assertTrue(arquivo.exists(), f"Artefato .{fmt} ausente em materiais/")

    def test_06_relatorio_execucao_existe(self):
        """Valida se o relatório de execução tripartite existe em relatorios/."""
        self.assertTrue(self.relatorios_dir.exists(), "Subpasta relatorios/ deve existir.")
        relatorios = list(self.relatorios_dir.glob("*-relatorio-execucao-*.html"))
        self.assertGreaterEqual(len(relatorios), 1, "Deve existir ao menos 1 arquivo HTML de relatório em relatorios/.")

        for fmt in ["html", "md"]:
            arquivos = list(self.relatorios_dir.glob(f"*-relatorio-execucao-*.{fmt}"))
            self.assertGreaterEqual(len(arquivos), 1, f"Relatório .{fmt} ausente em relatorios/")
            self.assertGreater(arquivos[0].stat().st_size, 500, f"Relatório .{fmt} está vazio.")

if __name__ == "__main__":
    unittest.main()
