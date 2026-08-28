import sys
import re
from pathlib import Path
import subprocess

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

EMOJI_REGEX = re.compile(
    r"["
    r"\U0001F600-\U0001F64F"  # emoticons
    r"\U0001F300-\U0001F5FF"  # symbols & pictographs
    r"\U0001F680-\U0001F6FF"  # transport & map symbols
    r"\U0001F1E0-\U0001F1FF"  # flags
    r"\U00002702-\U000027B0"  # dingbats
    r"\U000024C2-\U0001F251"
    r"\U0001F900-\U0001F9FF"  # supplemental symbols
    r"\U0001FA70-\U0001FAFF"  # symbols and pictographs extended-a
    r"\U00002600-\U000026FF"  # misc symbols
    r"\U00002B50"
    r"\U0000FE0F"             # variation selector
    r"]+",
    flags=re.UNICODE
)

EXTENSOES_TEXTO = {".html", ".md", ".typ", ".json", ".css", ".txt", ".sql"}

def limpar_arquivo(caminho: Path) -> bool:
    try:
        with open(caminho, "r", encoding="utf-8-sig") as f:
            conteudo = f.read()
    except UnicodeDecodeError:
        try:
            with open(caminho, "r", encoding="latin-1") as f:
                conteudo = f.read()
        except Exception:
            return False

    if not EMOJI_REGEX.search(conteudo):
        return False

    conteudo_limpo = EMOJI_REGEX.sub("", conteudo)
    conteudo_limpo = re.sub(r"  +", " ", conteudo_limpo)

    with open(caminho, "w", encoding="utf-8") as f:
        f.write(conteudo_limpo)
    return True

def varrer_output(output_dir: Path):
    modificados = 0
    arquivos_typ_modificados = []
    
    for arq in output_dir.rglob("*"):
        if arq.is_file() and arq.suffix.lower() in EXTENSOES_TEXTO:
            if limpar_arquivo(arq):
                modificados += 1
                if arq.suffix.lower() == ".typ":
                    arquivos_typ_modificados.append(arq)

    print(f"[*] Total de arquivos limpos em output/: {modificados}")
    
    # Recompila PDFs onde o .typ foi limpo
    for typ_file in arquivos_typ_modificados:
        pdf_target = typ_file.with_suffix(".pdf")
        print(f"[*] Recompilando PDF Typst: {pdf_target.name}")
        try:
            subprocess.run(["typst", "compile", str(typ_file), str(pdf_target)], check=True)
        except Exception as e:
            print(f"    [!] Erro ao compilar {pdf_target.name}: {e}")

if __name__ == "__main__":
    base_dir = Path(__file__).resolve().parent.parent
    out_dir = base_dir / "output"
    if out_dir.exists():
        varrer_output(out_dir)
