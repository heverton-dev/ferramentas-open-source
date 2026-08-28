import sys
import re
import json
from pathlib import Path

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

def limpar_texto(txt: str) -> str:
    txt_limpo = EMOJI_REGEX.sub("", txt)
    txt_limpo = re.sub(r"  +", " ", txt_limpo)
    return txt_limpo.strip()

def limpar_objeto(obj):
    if isinstance(obj, dict):
        return {k: limpar_objeto(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [limpar_objeto(elem) for elem in obj]
    elif isinstance(obj, str):
        return limpar_texto(obj)
    return obj

def processar_json(caminho: Path):
    with open(caminho, "r", encoding="utf-8-sig") as f:
        dados = json.load(f)
    dados_limpos = limpar_objeto(dados)
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(dados_limpos, f, ensure_ascii=False, indent=2)
    print(f"✅ Emojis removidos com sucesso de: {caminho.name}")

if __name__ == "__main__":
    base_dir = Path(__file__).resolve().parent.parent
    data_dir = base_dir / "scripts" / "data"
    for f in data_dir.glob("*.json"):
        processar_json(f)
