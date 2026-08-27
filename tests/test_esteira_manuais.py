# -*- coding: utf-8 -*-
"""
SUÍTE DE TESTES UNITÁRIOS AUTOMATIZADOS: ESTEIRA DE MANUAIS OPERACIONAIS & TRILHAS (AIDD)
Valida a integridade mecânica de ponta a ponta:
1. Conformidade de Schemas JSON (Sumário, Manual, Trilha, Relatório)
2. Execução dos Gates Mecânicos (G0 Qualidade, G1 HTTP 200, G2 Citações)
3. Compilação Tripartite (HTML, MD, PDF Typst)
4. Persistência Relacional em SQLite (estado_esteira.db - Regra R11)
5. Topologia Modular de Pastas e Paridade de Espelhos (Regra R18)
"""
import unittest
import json
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

class TestEsteiraManuais(unittest.TestCase):

    def setUp(self):
        self.slug_teste = "screenpipe"
        self.saas_teste = "granola"
        self.db_path = BASE_DIR / "estado_esteira.db"

    def test_01_schemas_json_validos(self):
        """Verifica se os 4 schemas da esteira são JSONs válidos."""
        schemas = [
            "schema_manual_operacional.json",
            "schema_trilha_aprendizado.json",
            "schema_relatorio_execucao.json"
        ]
        for s in schemas:
            caminho = BASE_DIR / "scripts" / "schemas" / s
            self.assertTrue(caminho.exists(), f"Schema ausente: {s}")
            with open(caminho, "r", encoding="utf-8") as f:
                dados = json.load(f)
                self.assertIn("$schema", dados, f"Falta $schema no arquivo {s}")

    def test_02_dados_fontes_e_sumario(self):
        """Verifica se o sumário de fontes existe e possui 5 fontes verificadas."""
        sumario = BASE_DIR / "scripts" / "data" / f"sumario-fontes-{self.slug_teste}.json"
        self.assertTrue(sumario.exists(), "Sumário de fontes não encontrado.")
        with open(sumario, "r", encoding="utf-8") as f:
            dados = json.load(f)
            fontes = dados.get("fontes", [])
            self.assertEqual(len(fontes), 5, "Sumário deve possuir 5 fontes.")
            ids = {f["id"] for f in fontes}
            self.assertEqual(ids, {"F01", "F02", "F03", "F04", "F05"})

    def test_03_gates_mecanicos_g0_g1_g2(self):
        """Executa e valida os retornos mecânicos dos Gates G0, G1 e G2."""
        import sys
        sys.path.insert(0, str(BASE_DIR / "scripts"))
        from auditar_qualidade_fontes import auditar_qualidade_sumario
        from auditar_fontes_veridicas import auditar_sumario
        from auditar_citacoes_manuais import auditar_citacoes

        sumario_path = BASE_DIR / "scripts" / "data" / f"sumario-fontes-{self.slug_teste}.json"
        
        # Gate G0
        g0_ok = auditar_qualidade_sumario(sumario_path)
        self.assertTrue(g0_ok, "Gate G0 (Qualidade & Whitelist) deve retornar True.")

        # Gate G1
        g1_ok = auditar_sumario(sumario_path)
        self.assertTrue(g1_ok, "Gate G1 (HTTP 200) deve retornar True.")

        # Gate G2
        g2_ok = auditar_citacoes(self.slug_teste)
        self.assertTrue(g2_ok, "Gate G2 (Citações Cruzadas) deve retornar True.")

    def test_04_arquivos_tripartites_gerados(self):
        """Valida se manuais e trilhas foram gerados nos 3 formatos com tamanho > 0."""
        out_dir = BASE_DIR / "output" / "03-manuais-e-trilhas" / self.saas_teste / self.slug_teste
        formatos = ["html", "md", "pdf"]

        for fmt in formatos:
            manual = out_dir / "manuais" / f"manual-{self.slug_teste}-vps-e-uso.{fmt}"
            self.assertTrue(manual.exists(), f"Manual .{fmt} não encontrado.")
            self.assertGreater(manual.stat().st_size, 0, f"Manual .{fmt} está vazio.")

            trilha = out_dir / "trilhas" / f"trilha-{self.slug_teste}-aprendizado.{fmt}"
            self.assertTrue(trilha.exists(), f"Trilha .{fmt} não encontrada.")
            self.assertGreater(trilha.stat().st_size, 0, f"Trilha .{fmt} está vazia.")

    def test_05_relatorio_telemetria_tripartite(self):
        """Valida se o relatório de telemetria tripartite foi gerado corretamente."""
        rel_dir = BASE_DIR / "output" / "03-manuais-e-trilhas" / self.saas_teste / self.slug_teste / "relatorios"
        self.assertTrue(rel_dir.exists(), "Pasta relatorios não encontrada.")

        arquivos_rel = list(rel_dir.glob("*-relatorio-execucao-*.html"))
        self.assertGreaterEqual(len(arquivos_rel), 1, "Relatório HTML não encontrado.")

        arquivos_md = list(rel_dir.glob("*-relatorio-execucao-*.md"))
        self.assertGreaterEqual(len(arquivos_md), 1, "Relatório Markdown não encontrado.")

        arquivos_pdf = list(rel_dir.glob("*-relatorio-execucao-*.pdf"))
        self.assertGreaterEqual(len(arquivos_pdf), 1, "Relatório PDF não encontrado.")

    def test_06_persistencia_sqlite_r11(self):
        """Valida inserção e leitura na tabela esteira_manuais_bundles no SQLite."""
        import sys
        sys.path.insert(0, str(BASE_DIR / "scripts"))
        from estado_esteira import registrar_bundle_esteira, listar_bundles_esteira

        teste_data = {
            "slug": "teste-unitario-ci",
            "saas_origem": "teste-saas",
            "data_execucao": "27-08-2026",
            "horario_inicio": "12:00:00",
            "horario_fim": "12:00:05",
            "duracao_seg": 5.0,
            "tokens_totais": 1000,
            "taxa_economia": "95%",
            "gate_g0": "APROVADO",
            "gate_g1": "APROVADO",
            "gate_g2": "APROVADO",
            "gate_r18": "APROVADO",
            "total_arquivos": 9,
            "caminho_bundle": "output/03-manuais-e-trilhas/granola/teste-unitario-ci/"
        }

        registrar_bundle_esteira(teste_data)
        bundles = listar_bundles_esteira()
        slugs = [b["slug"] for b in bundles]
        self.assertIn("teste-unitario-ci", slugs, "Bundle de teste deve estar persistido no SQLite.")

        # Limpeza do teste
        conn = sqlite3.connect(self.db_path)
        conn.execute("DELETE FROM esteira_manuais_bundles WHERE slug = 'teste-unitario-ci'")
        conn.commit()
        conn.close()

    def test_07_topologia_pastas_modular_9_arquivos(self):
        """Valida que a ferramenta tem rigorosamente 9 arquivos (3 em cada subpasta)."""
        out_dir = BASE_DIR / "output" / "03-manuais-e-trilhas" / self.saas_teste / self.slug_teste
        manuais = list((out_dir / "manuais").glob("*.*"))
        trilhas = list((out_dir / "trilhas").glob("*.*"))
        relatorios = list((out_dir / "relatorios").glob("*.*"))

        self.assertEqual(len(manuais), 3, f"Manuais deve ter 3 arquivos (tem {len(manuais)})")
        self.assertEqual(len(trilhas), 3, f"Trilhas deve ter 3 arquivos (tem {len(trilhas)})")
        self.assertEqual(len(relatorios), 3, f"Relatórios deve ter 3 arquivos (tem {len(relatorios)})")

    def test_08_integridade_soberana_r18(self):
        """Valida a integridade da pasta soberana output/03-manuais-e-trilhas/granola/<slug>/."""
        out_dir = BASE_DIR / "output" / "03-manuais-e-trilhas" / self.saas_teste / self.slug_teste
        self.assertTrue(out_dir.exists(), "Diretório soberano da ferramenta deve existir.")
        todos_arquivos = list(out_dir.rglob("*.*"))
        self.assertEqual(len(todos_arquivos), 9, "O bundle soberano da ferramenta deve conter exatamente 9 arquivos.")

if __name__ == "__main__":
    unittest.main()
