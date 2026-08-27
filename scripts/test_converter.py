#!/usr/bin/env python3
"""
Testes unitários para converter_md_pdf.py
"""
import unittest
import os
import tempfile
from pathlib import Path

class TestConverterMdPdf(unittest.TestCase):
    """Testes básicos para o conversor MD→PDF."""

    def test_import_converter(self):
        """Testa se o módulo pode ser importado."""
        try:
            import sys
            sys.path.insert(0, os.path.dirname(__file__))
            import converter_md_pdf
            self.assertTrue(hasattr(converter_md_pdf, 'md_to_pdf'))
        except ImportError:
            self.fail("Não foi possível importar converter_md_pdf")

    def test_converter_exists(self):
        """Testa se o script converter existe."""
        script_path = Path(__file__).parent / 'converter_md_pdf.py'
        self.assertTrue(script_path.exists(), f"Script não encontrado: {script_path}")

    def test_simple_md_conversion(self):
        """Testa conversão simples MD→PDF."""
        import sys
        sys.path.insert(0, os.path.dirname(__file__))
        from converter_md_pdf import md_to_pdf

        with tempfile.TemporaryDirectory() as tmpdir:
            md_file = Path(tmpdir) / 'test.md'
            pdf_file = Path(tmpdir) / 'test.pdf'

            # Cria MD simples
            md_file.write_text('# Test\nHello world', encoding='utf-8')

            # Converte
            success, msg = md_to_pdf(str(md_file), str(pdf_file))

            # Valida
            self.assertTrue(success, f"Conversão falhou: {msg}")
            self.assertTrue(pdf_file.exists(), "PDF não foi criado")
            self.assertGreater(pdf_file.stat().st_size, 100, "PDF muito pequeno")


if __name__ == '__main__':
    unittest.main()
