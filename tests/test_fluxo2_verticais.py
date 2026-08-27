# -*- coding: utf-8 -*-
"""
SUÍTE DE TESTES UNITÁRIOS AUTOMATIZADOS: FLUXO 2 (DOSSIÊS VERTICAIS AIDD)
Valida a integridade de ponta a ponta:
1. Conformidade de Schema JSON (dossie_vertical.schema.json)
2. As 5 Classificações Canônicas do Quinteto Soberano (R5-V)
3. Presença Obrigatória de White-Label e MCPs/Skills
4. Compilação Tripartite (HTML, MD, Typst PDF) em materiais/
5. Persistência Relacional em SQLite (estado_esteira.db - Regra R11)
6. Paridade Estrita de Espelhos com subpastas materiais/ e relatorios/ (Regra R18)
7. Existência do Relatório de Execução Tripartite em relatorios/
"""
import unittest
import json
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

class TestFluxo2Verticais(unittest.TestCase):

    def setUp(self):
        self.saas_teste = "granola"
        self.data_file = BASE_DIR / "scripts" / "data" / f"dossie-vertical-{self.saas_teste}.json"
        self.bundle_dir = BASE_DIR / "output" / "02-dossies-verticais" / f"vert-{self.saas_teste}"
        self.materiais_dir = self.bundle_dir / "materiais"
        self.relatorios_dir = self.bundle_dir / "relatorios"
        self.db_path = BASE_DIR / "estado_esteira.db"

    def test_01_schema_dossie_vertical_valido(self):
        """Valida se o schema JSON de Dossiê Vertical existe e é sintaticamente válido."""
        schema_path = BASE_DIR / "scripts" / "schemas" / "dossie_vertical.schema.json"
        self.assertTrue(schema_path.exists(), "Schema dossie_vertical.schema.json não encontrado.")
        with open(schema_path, "r", encoding="utf-8") as f:
            schema = json.load(f)
            self.assertIn("$schema", schema)

    def test_02_quinteto_soberano_5_classificacoes(self):
        """Valida que o Quinteto Soberano possui rigorosamente as 5 classificações canônicas."""
        self.assertTrue(self.data_file.exists(), f"Dossiê {self.data_file} não encontrado.")
        with open(self.data_file, "r", encoding="utf-8") as f:
            dados = json.load(f)

        quinteto = dados.get("quinteto", [])
        self.assertEqual(len(quinteto), 5, "Quinteto Soberano deve possuir exatamente 5 ferramentas.")

        classificacoes_esperadas = {
            "A Mais Robusta",
            "A Mais Completa",
            "A Mais Moderna",
            "A Mais Leve",
            "A Mais Simples"
        }
        classificacoes_reais = {q["classificacao"] for q in quinteto}
        self.assertEqual(classificacoes_esperadas, classificacoes_reais, "Todas as 5 classificações canônicas devem estar presentes.")

    def test_03_secoes_whitelabel_e_mcps_obrigatorias(self):
        """Valida se as Seções de White-Label e MCPs/Skills estão preenchidas."""
        with open(self.data_file, "r", encoding="utf-8") as f:
            dados = json.load(f)

        for q in dados["quinteto"]:
            self.assertIn("design_system", q, f"Ferramenta {q['nome']} sem dados de design_system.")
            self.assertIn("esforco", q["design_system"])
            self.assertIn("uso_complementar", q, f"Ferramenta {q['nome']} sem ecossistema agêntico.")
            self.assertGreaterEqual(len(q["uso_complementar"]), 1)

    def test_04_compilacao_tripartite_gerada(self):
        """Valida se os 3 formatos (HTML, MD, PDF) foram compilados em materiais/ com tamanho > 0."""
        self.assertTrue(self.materiais_dir.exists(), f"Subpasta materiais/ não encontrada em {self.bundle_dir}")
        formatos = ["html", "md", "pdf"]

        for fmt in formatos:
            arquivo = self.materiais_dir / f"vert-{self.saas_teste}.{fmt}"
            self.assertTrue(arquivo.exists(), f"Arquivo .{fmt} não encontrado em materiais/")
            self.assertGreater(arquivo.stat().st_size, 0, f"Arquivo .{fmt} está vazio.")

    def test_05_persistencia_sqlite_r11(self):
        """Valida registro e leitura do Dossiê Vertical no banco SQLite estado_esteira.db."""
        import sys
        sys.path.insert(0, str(BASE_DIR / "scripts"))
        from estado_esteira import listar_dossies_verticais

        dossies = listar_dossies_verticais()
        slugs = [d["saas_slug"] for d in dossies]
        self.assertIn(self.saas_teste, slugs, f"SaaS {self.saas_teste} deve estar registrado no SQLite.")

    def test_06_integridade_soberana_r18(self):
        """Valida a integridade da pasta soberana com subpastas materiais/ e relatorios/."""
        self.assertTrue(self.bundle_dir.exists(), "Diretório do dossiê vertical soberano deve existir.")
        self.assertTrue(self.materiais_dir.exists(), "Subpasta materiais/ deve existir.")
        self.assertTrue(self.relatorios_dir.exists(), "Subpasta relatorios/ deve existir.")
        arquivos = list(self.materiais_dir.glob("vert-granola.*"))
        self.assertGreaterEqual(len(arquivos), 3, "Dossiê vertical soberano deve conter ao menos HTML, MD e PDF em materiais/.")

    def test_07_relatorio_execucao_existe(self):
        """Valida se o relatório de execução tripartite existe em relatorios/."""
        self.assertTrue(self.relatorios_dir.exists(), "Subpasta relatorios/ deve existir.")
        relatorios_html = list(self.relatorios_dir.glob("*-relatorio-execucao-*.html"))
        self.assertGreaterEqual(len(relatorios_html), 1, "Deve existir ao menos 1 arquivo HTML de relatório em relatorios/.")

        for fmt in ["html", "md"]:
            arquivos = list(self.relatorios_dir.glob(f"*-relatorio-execucao-*.{fmt}"))
            self.assertGreaterEqual(len(arquivos), 1, f"Relatório .{fmt} ausente em relatorios/")
            self.assertGreater(arquivos[0].stat().st_size, 500, f"Relatório .{fmt} está vazio.")

if __name__ == "__main__":
    unittest.main()
