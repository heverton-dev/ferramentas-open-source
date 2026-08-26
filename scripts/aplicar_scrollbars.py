# -*- coding: utf-8 -*-
"""
Script determinístico para padronizar as barras de rolagem (scrollbars) em todos os compêndios:
- Largura/Altura máxima: 4px
- Cor da barra: var(--accent)
- Suporte nativo cross-browser (WebKit/Blink + Firefox W3C standard)
"""
import sys
import glob
import re
from pathlib import Path

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

SCROLLBAR_CSS = """
  /* SCROLLBAR REFINADA (MAX 4PX & COR ACCENT) */
  * {
    scrollbar-width: thin;
    scrollbar-color: var(--accent) transparent;
  }
  ::-webkit-scrollbar {
    width: 4px;
    height: 4px;
  }
  ::-webkit-scrollbar-track {
    background: transparent;
  }
  ::-webkit-scrollbar-thumb {
    background: var(--accent);
    border-radius: 4px;
  }
  ::-webkit-scrollbar-thumb:hover {
    background: var(--green);
  }
"""

def aplicar_scrollbars():
    arquivos_out = glob.glob("output/listas-open-source/*.html")
    arquivos_doc = glob.glob("docs/listas/*.html")
    todos = sorted(list(set(arquivos_out + arquivos_doc)))

    modificados = 0
    for f in todos:
        p = Path(f)
        txt = p.read_text(encoding="utf-8")

        # Se já tem scrollbar customizada antiga, remove para atualizar
        txt_novo = re.sub(r'/\* SCROLLBAR.*?\*/.*?(?=\n\s*[a-zA-Z#\.\*]|</style>)', '', txt, flags=re.DOTALL)
        txt_novo = re.sub(r'::-webkit-scrollbar\s*\{[^}]*\}', '', txt_novo)
        txt_novo = re.sub(r'::-webkit-scrollbar-track\s*\{[^}]*\}', '', txt_novo)
        txt_novo = re.sub(r'::-webkit-scrollbar-thumb\s*\{[^}]*\}', '', txt_novo)
        txt_novo = re.sub(r'::-webkit-scrollbar-thumb:hover\s*\{[^}]*\}', '', txt_novo)
        txt_novo = re.sub(r'scrollbar-width:\s*thin;?', '', txt_novo)
        txt_novo = re.sub(r'scrollbar-color:[^;]*;?', '', txt_novo)

        # Injetar logo antes de </style>
        if "</style>" in txt_novo:
            txt_final = txt_novo.replace("</style>", f"{SCROLLBAR_CSS}\n</style>")
            p.write_text(txt_final, encoding="utf-8")
            modificados += 1

    print(f"✅ Scrollbars customizadas de 4px na cor accent aplicadas em {modificados} arquivos!")

if __name__ == "__main__":
    aplicar_scrollbars()
