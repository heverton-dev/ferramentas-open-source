#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Regera o PDF do Relatorio de Auditoria de Seguranca a partir de relatorio.html.
Nao instala nada: usa o Chrome/Edge headless ja presente na maquina.

Uso: python docs/security-audit/gerar_relatorio.py
"""
import os
import re
import sys
import shutil
import subprocess
from pathlib import Path

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

AQUI = Path(__file__).resolve().parent
HTML = AQUI / "relatorio.html"
PDF = AQUI / "relatorio-auditoria-seguranca.pdf"

CANDIDATOS = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "google-chrome",
    "chromium",
]


def achar_navegador() -> str:
    for c in CANDIDATOS:
        if os.path.isfile(c):
            return c
        achado = shutil.which(c)
        if achado:
            return achado
    raise RuntimeError("Nenhum navegador headless encontrado (Chrome/Edge/Chromium).")


def contar_paginas(pdf: Path) -> int:
    dados = pdf.read_bytes()
    return len(re.findall(rb"/Type\s*/Page[^s]", dados))


def main() -> int:
    if not HTML.is_file():
        print(f"[!] HTML de origem ausente: {HTML}")
        return 1

    navegador = achar_navegador()
    subprocess.run(
        [
            navegador,
            "--headless=new",
            "--disable-gpu",
            "--no-sandbox",
            f"--print-to-pdf={PDF}",
            HTML.as_uri(),
        ],
        check=True,
        capture_output=True,
    )

    if not PDF.is_file():
        print("[!] PDF nao foi gerado.")
        return 1

    print(f"[ok] PDF gerado: {PDF}")
    print(f"[ok] Paginas: {contar_paginas(PDF)} | Tamanho: {PDF.stat().st_size // 1024} KB")
    return 0


if __name__ == "__main__":
    sys.exit(main())
