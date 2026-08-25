import glob
import re
import os
import json

def main():
    html_files = glob.glob("output/listas-open-source/*.html")
    all_repos = {}
    
    for file_path in html_files:
        base_name = os.path.basename(file_path)
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Regex para capturar links do GitHub (owner/repo)
        matches = re.findall(r'github\.com/([a-zA-Z0-9_\-\.]+/[a-zA-Z0-9_\-\.]+)', content)
        for m in matches:
            cleaned = m.strip("\"'/.,)>")
            if cleaned.endswith(".git"):
                cleaned = cleaned[:-4]
            # descartar links genericos se houver
            parts = cleaned.split("/")
            if len(parts) == 2 and parts[0] not in ["features", "pricing", "explore", "topics"]:
                full_url = f"https://github.com/{cleaned}"
                if full_url not in all_repos:
                    all_repos[full_url] = []
                all_repos[full_url].append(base_name)
                
    print(f"Total de arquivos analisados: {len(html_files)}")
    print(f"Total de repositórios GitHub únicos: {len(all_repos)}")
    
    # Salvar lista em JSON e TXT
    os.makedirs("output/forks-inventory", exist_ok=True)
    json_path = "output/forks-inventory/repositorios.json"
    txt_path = "output/forks-inventory/repositorios.txt"
    
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(all_repos, f, indent=2, ensure_ascii=False)
        
    with open(txt_path, "w", encoding="utf-8") as f:
        for repo in sorted(all_repos.keys()):
            f.write(f"{repo}\n")
            
    print(f"Inventário salvo em: {json_path} e {txt_path}")

if __name__ == "__main__":
    main()
