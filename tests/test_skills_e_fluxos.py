# -*- coding: utf-8 -*-
"""
TESTES AUTOMATIZADOS DAS SKILLS, COMANDOS E RUNNERS DOS 3 MACRO-FLUXOS AIDD
Valida a arquitetura universal em .agents/ e espelhos em .claude/
"""
import os
import sys
import unittest
import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

class TestSkillsEFluxosAIDD(unittest.TestCase):

    def setUp(self):
        self.skills_esperadas = [
            "fluxo1-listas-horizontais",
            "fluxo2-dossies-verticais",
            "fluxo3-manuais-e-trilhas",
            "fluxo-total-aidd"
        ]
        self.comandos_esperados = [
            "fluxo1.md",
            "fluxo2.md",
            "fluxo3.md",
            "fluxo-total.md"
        ]
        self.runners_esperados = [
            "run_fluxo1.py",
            "run_fluxo2.py",
            "run_fluxo3.py",
            "run_fluxo_total.py"
        ]

    def test_01_existencia_skills_agents(self):
        """Valida que as 4 skills universais existem em .agents/skills/ com SKILL.md."""
        for skill in self.skills_esperadas:
            skill_md = BASE_DIR / ".agents" / "skills" / skill / "SKILL.md"
            self.assertTrue(skill_md.exists(), f"SKILL.md não encontrado: {skill_md}")
            conteudo = skill_md.read_text(encoding="utf-8")
            self.assertIn("---", conteudo)
            self.assertIn("name:", conteudo)
            self.assertIn("description:", conteudo)

    def test_02_existencia_comandos_agents(self):
        """Valida que os 4 comandos slash universais existem em .agents/commands/."""
        for cmd in self.comandos_esperados:
            cmd_path = BASE_DIR / ".agents" / "commands" / cmd
            self.assertTrue(cmd_path.exists(), f"Comando não encontrado: {cmd_path}")
            conteudo = cmd_path.read_text(encoding="utf-8")
            self.assertIn("description:", conteudo)

    def test_03_espelhos_claude_acessiveis(self):
        """Valida que os espelhos em .claude/skills/ e .claude/commands/ acessam o conteúdo."""
        for skill in self.skills_esperadas:
            espelho_skill = BASE_DIR / ".claude" / "skills" / skill / "SKILL.md"
            self.assertTrue(espelho_skill.exists(), f"Espelho da skill não encontrado: {espelho_skill}")

        for cmd in self.comandos_esperados:
            espelho_cmd = BASE_DIR / ".claude" / "commands" / cmd
            self.assertTrue(espelho_cmd.exists(), f"Espelho do comando não encontrado: {espelho_cmd}")

    def test_04_integridade_e_help_dos_cli_runners(self):
        """Valida que todos os 4 CLI runners respondem a --help com exit code 0."""
        for runner in self.runners_esperados:
            script_path = BASE_DIR / "scripts" / runner
            self.assertTrue(script_path.exists(), f"Script runner não encontrado: {script_path}")
            
            res = subprocess.run(
                [sys.executable, str(script_path), "--help"],
                cwd=str(BASE_DIR),
                capture_output=True,
                text=True
            )
            self.assertEqual(res.returncode, 0, f"Falha ao executar --help em {runner}: {res.stderr}")
            self.assertIn("usage:", res.stdout.lower())

if __name__ == "__main__":
    unittest.main()
