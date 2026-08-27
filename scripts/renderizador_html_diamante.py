# -*- coding: utf-8 -*-
"""
RENDERIZADOR DETERMINÍSTICO DE MARKDOWN PARA HTML DIAMANTE (AIDD)
Gera HTML interativo corporativo a partir de Markdown com:
- Tabelas estilizadas completas (cabeçalho escuro, linhas zebradas, bordas suaves);
- Renderização nativa de diagramas Mermaid em SVG via Mermaid.js ESM;
- Formatação perfeita de negritos, itálicos, blockquotes e blocos de código;
- Design System Responsivo e Padrão Diamante.
"""
import re
import subprocess
from pathlib import Path

CSS_DIAMANTE = """
:root {
  --ink: #0F172A;
  --ink-2: #334155;
  --muted: #64748B;
  --accent: #0284C7;
  --accent-soft: #E0F2FE;
  --paper: #F8FAFC;
  --surface: #FFFFFF;
  --rule: #CBD5E1;
  --rule-soft: #E2E8F0;
  --mono: "Cascadia Code", "Fira Code", Consolas, monospace;
}
* { box-sizing: border-box; }
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  background: var(--paper);
  color: var(--ink);
  line-height: 1.68;
  padding: 32px 16px;
  margin: 0;
}
.container {
  max-width: 1050px;
  margin: 0 auto;
  background: var(--surface);
  padding: 44px 48px;
  border-radius: 8px;
  border: 1px solid var(--rule);
  box-shadow: 0 2px 8px rgba(0,0,0,0.05);
}
h1 {
  font-size: 26px;
  font-weight: 800;
  color: #0F172A;
  border-bottom: 2.5px solid var(--accent);
  padding-bottom: 10px;
  margin-top: 24px;
  margin-bottom: 18px;
}
h2 {
  font-size: 20px;
  font-weight: 700;
  color: #1E293B;
  margin-top: 28px;
  margin-bottom: 14px;
  border-bottom: 1px solid var(--rule-soft);
  padding-bottom: 8px;
}
h3 {
  font-size: 16px;
  font-weight: 700;
  color: #334155;
  margin-top: 20px;
  margin-bottom: 10px;
}
p { margin: 12px 0; font-size: 14.5px; color: var(--ink-2); }
strong { font-weight: 700; color: #0F172A; }
em { font-style: italic; color: #334155; }
ul, ol { margin: 12px 0; padding-left: 24px; }
li { margin-bottom: 6px; font-size: 14px; color: var(--ink-2); }

/* TABELAS CORPORATIVAS */
table {
  width: 100%;
  border-collapse: collapse;
  margin: 22px 0;
  font-size: 13.5px;
  border: 1px solid var(--rule);
  border-radius: 6px;
  overflow: hidden;
}
th, td {
  border: 1px solid var(--rule);
  padding: 10px 14px;
  text-align: left;
}
th {
  background: #1A446C;
  color: #FFFFFF;
  font-weight: 700;
  font-size: 13px;
  letter-spacing: 0.02em;
}
tr:nth-child(even) {
  background: #F8FAFC;
}
tr:hover {
  background: #F1F5F9;
}

/* BLOCKQUOTES EXECUTIVOS */
blockquote {
  border-left: 4px solid var(--accent);
  background: var(--accent-soft);
  color: #0369A1;
  padding: 12px 18px;
  margin: 18px 0;
  border-radius: 0 6px 6px 0;
  font-size: 14px;
}
blockquote p { margin: 4px 0; color: #0369A1; }

/* CÓDIGO E TERMINAL */
pre:not(.mermaid) {
  background: #0F172A;
  color: #E2E8F0;
  padding: 16px;
  border-radius: 6px;
  overflow-x: auto;
  font-size: 13px;
  font-family: var(--mono);
  border: 1px solid #1E293B;
  margin: 16px 0;
}
code {
  font-family: var(--mono);
  background: #F1F5F9;
  color: #0F172A;
  padding: 2px 6px;
  border-radius: 4px;
  font-size: 12.5px;
}
pre code {
  background: transparent;
  color: inherit;
  padding: 0;
}

/* DIAGRAMAS MERMAID */
.mermaid {
  background: #FFFFFF;
  border: 1px solid var(--rule-soft);
  border-radius: 6px;
  padding: 24px;
  text-align: center;
  margin: 24px 0;
  box-shadow: 0 1px 4px rgba(0,0,0,0.04);
}

hr {
  border: 0;
  height: 1px;
  background: var(--rule-soft);
  margin: 32px 0;
}
"""

def converter_markdown_para_html_diamante(md_texto: str, titulo_documento: str, base_dir: Path) -> str:
    """Converte markdown em HTML autocontido com Pandoc, tabelas, Mermaid e CSS Diamante."""
    # 1. Converte via Pandoc para fragmento HTML5
    proc = subprocess.run(
        ["pandoc", "-f", "markdown", "-t", "html5"],
        input=md_texto,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )
    corpo_html = proc.stdout if proc.returncode == 0 else ""

    # 2. Desescapa blocos Mermaid
    def tratar_mermaid(match):
        conteudo = match.group(1)
        conteudo = conteudo.replace("&amp;", "&").replace("&quot;", '"').replace("&lt;", "<").replace("&gt;", ">")
        return f'<pre class="mermaid">\n{conteudo.strip()}\n</pre>'

    corpo_html = re.sub(
        r'<pre\s+class="mermaid"><code>([\s\S]*?)</code></pre>',
        tratar_mermaid,
        corpo_html
    )

    # 3. Monta documento HTML final
    html_doc = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{titulo_documento}</title>
  <style>
{CSS_DIAMANTE}
  </style>
  <script type="module">
    import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
    mermaid.initialize({{
      startOnLoad: true,
      theme: 'neutral',
      securityLevel: 'loose'
    }});
  </script>
</head>
<body>
<div class="container">
{corpo_html}
</div>
</body>
</html>
"""
    return html_doc
