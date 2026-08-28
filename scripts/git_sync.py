# -*- coding: utf-8 -*-
"""
MÓDULO DE SINCRONIZAÇÃO GIT AUTOMATIZADA (REGRA R16 & AIDD PIPELINE)
Executa commit e push automatizados após a conclusão 100% verde de qualquer fluxo da fábrica.
Utiliza mensagens curtas, descritivas e padronizadas.
"""
import sys
import subprocess
from pathlib import Path

def console_utf8():
    if sys.platform == "win32":
        try:
            sys.stdout.reconfigure(encoding="utf-8")
            sys.stderr.reconfigure(encoding="utf-8")
        except Exception:
            pass

console_utf8()

BASE_DIR = Path(__file__).resolve().parent.parent

def executar_commit_e_push(mensagem_curta: str, diretorio_base: Path = BASE_DIR) -> bool:
    """
    Executa git add, commit e push garantindo integridade e feedback limpo.
    """
    print("\n" + "-"*70)
    print(f"📦 [Sincronização Git R16] Iniciando commit & push: '{mensagem_curta}'")
    print("-"*70)

    try:
        # 1. Verifica se é um repositório git
        res_check = subprocess.run(["git", "rev-parse", "--is-inside-work-tree"], cwd=str(diretorio_base), capture_output=True, text=True)
        if res_check.returncode != 0:
            print("   ⚠️ Diretório não é um repositório Git. Sincronização ignorada.")
            return True

        # 2. Stage dos arquivos
        subprocess.run(["git", "add", "."], cwd=str(diretorio_base), check=True)

        # 3. Verifica se há mudanças staged
        res_status = subprocess.run(["git", "status", "--porcelain"], cwd=str(diretorio_base), capture_output=True, text=True)
        if not res_status.stdout.strip():
            print("   ℹ️ Nenhuma alteração pendente para commit. Repositório 100% atualizado.")
            return True

        # 4. Commit
        res_commit = subprocess.run(["git", "commit", "-m", mensagem_curta], cwd=str(diretorio_base), capture_output=True, text=True)
        if res_commit.returncode != 0:
            print(f"   ⚠️ Aviso no commit: {res_commit.stderr.strip()}")
        else:
            print(f"   ✅ Commit realizado com sucesso: \"{mensagem_curta}\"")

        # 5. Push
        print("   🚀 Enviando alterações para o repositório remoto (git push)...")
        res_push = subprocess.run(["git", "push"], cwd=str(diretorio_base), capture_output=True, text=True)
        if res_push.returncode != 0:
            print(f"   ⚠️ Aviso no push remoto: {res_push.stderr.strip() or res_push.stdout.strip()}")
            return False
        
        print("   ✅ Push concluído com sucesso no branch remoto!")
        print("-"*70 + "\n")
        return True

    except Exception as e:
        print(f"   ⚠️ Falha na execução do Git Sync: {e}")
        print("-"*70 + "\n")
        return False

if __name__ == "__main__":
    msg = sys.argv[1] if len(sys.argv) > 1 else "feat(esteira): atualizacao automatica de artefatos open source"
    executar_commit_e_push(msg)
