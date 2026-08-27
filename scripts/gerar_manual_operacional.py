# -*- coding: utf-8 -*-
"""
GERADOR DETERMINÍSTICO DO MANUAL OPERACIONAL DUPLO (HTML + TYPST PDF + MD)
Compila com paridade estrita entre output/manuais/ e docs/manuais/:
- Suporta Módulo 0 de Nivelamento Conceitual
- Suporta Roteiro de Primeiro Voo
- Suporta comandos detalhados e validação à prova de erros
"""
import sys
import json
import subprocess
from pathlib import Path
from padroes.template_manual_operacional import renderizar_manual_html

def console_utf8():
    if sys.platform == "win32":
        try:
            sys.stdout.reconfigure(encoding="utf-8")
            sys.stderr.reconfigure(encoding="utf-8")
        except Exception:
            pass

console_utf8()

BASE_DIR = Path(__file__).resolve().parent.parent

def gerar_markdown_manual(dados: dict) -> str:
    vps = dados["vps_recomendada"]
    linhas = [
        f"# Manual Operacional Completo: {dados['produto_foco']}",
        f"",
        f"> **Padrão Diamante · Guia de Engenharia & Adoção Descomplicada**  ",
        f"> **Licença:** {dados['licenca_osi']} | **Versão:** {dados['versao']} | **Setup Estimado:** {dados.get('tempo_estimado_setup', '15 min')}  ",
        f"> **VPS Recomendada:** {vps['provedor_modelo']} ({vps['vcpu']}, {vps['ram']}, {vps['armazenamento']}, {vps['so_recomendado']})  ",
        f"> **Custo Mensal Estimado:** {vps['custo_mensal_estimado']}",
        f"",
        f"---",
        f"",
        f"## Módulo 0: Nivelamento Conceitual (Analogias do Dia a Dia)",
        f""
    ]

    for n in dados.get("nivelamento_conceitual", []):
        linhas.append(f"### 💡 {n['termo']} *(Analogia: {n['analogia_cotidiana']})*")
        linhas.append(f"{n['explicacao_simples']}\n")

    linhas.append("## Parte I: Instalação em Produção na VPS (Passo a Passo Rígido)\n")

    for p in dados["instalacao_producao"]["passos"]:
        linhas.append(f"### Passo {p['numero']}: {p['titulo']} `[{p['fonte_id']}]`")
        linhas.append(f"{p['descricao']}\n")
        if p.get("analogia"):
            linhas.append(f"> 💡 **Entenda com uma analogia:** {p['analogia']}\n")
        linhas.append(f"```bash\n{p['comandos']}\n```\n")
        if p.get("o_que_acontece_na_tela"):
            linhas.append(f"- 🖥️ **O que você verá na tela:** {p['o_que_acontece_na_tela']}")
        if p.get("como_saber_se_deu_certo"):
            linhas.append(f"- ✅ **Como saber se deu certo:** {p['como_saber_se_deu_certo']}\n")

    linhas.append("## Arquivos de Configuração de Produção\n")
    for c in dados["instalacao_producao"]["arquivos_configuracao"]:
        linhas.append(f"### `{c['caminho']}`")
        linhas.append(f"*{c['explicacao']}*\n")
        linhas.append(f"```{c['linguagem']}\n{c['conteudo']}\n```\n")

    linhas.append("## Parte II: Manual de Uso Exaustivo\n")
    linhas.append(f"**Arquitetura Operacional:** {dados['manual_uso_exaustivo']['arquitetura_uso']}\n")

    if dados.get("manual_uso_exaustivo", {}).get("roteiro_primeiro_voo"):
        linhas.append("### Roteiro de Primeiro Voo (Sua Primeira Reunião em 3 Minutos)\n")
        for pv in dados["manual_uso_exaustivo"]["roteiro_primeiro_voo"]:
            linhas.append(f"1. **{pv['passo']}:** {pv['acao']}")
            linhas.append(f"   - 🎯 **Resultado Esperado:** {pv['resultado_esperado']}\n")

    linhas.append("### Dicionário Completo de Comandos (CLI)\n")
    linhas.append("| Comando / Flag | Descrição Técnica | Exemplo de Execução | Fonte |")
    linhas.append("| :--- | :--- | :--- | :---: |")
    for c in dados["manual_uso_exaustivo"]["comandos_cli"]:
        linhas.append(f"| `{c['comando']}` | {c['descricao']} | `{c['exemplo']}` | `[{c['fonte_id']}]` |")
    linhas.append("")

    linhas.append("### Endpoints de API REST & Integração Agêntica\n")
    linhas.append("| Método | Rota | Descrição | Fonte |")
    linhas.append("| :---: | :--- | :--- | :---: |")
    for a in dados["manual_uso_exaustivo"]["rotas_api"]:
        linhas.append(f"| **{a['metodo']}** | `{a['rota']}` | {a['descricao']} | `[{a['fonte_id']}]` |")
    linhas.append("")

    linhas.append("### Matriz de Resolução de Problemas (Troubleshooting)\n")
    for t in dados["manual_uso_exaustivo"]["troubleshooting"]:
        linhas.append(f"- **⚠️ Sintoma:** {t['sintoma']}")
        linhas.append(f"  - **Causa:** {t['causa_provavel']}")
        linhas.append(f"  - **Solução:** `{t['solucao_comando']}`\n")

    linhas.append("## Parte III: Referências Bibliográficas Auditadas\n")
    linhas.append("| ID | Categoria | Título da Obra | Autor / Mantenedor | Link Oficial |")
    linhas.append("| :---: | :--- | :--- | :--- | :--- |")
    for r in dados["referencias_bibliograficas"]:
        linhas.append(f"| **{r['id']}** | {r['categoria']} | {r['titulo']} | {r['autor_ou_canal']} | [{r['url']}]({r['url']}) |")
    linhas.append("")

    return "\n".join(linhas)

def gerar_typst_codigo(dados: dict) -> str:
    vps = dados["vps_recomendada"]

    nivelamento_typ = []
    for n in dados.get("nivelamento_conceitual", []):
        nivelamento_typ.append(f"""(
          termo: "{n['termo']}",
          analogia_cotidiana: "{n['analogia_cotidiana']}",
          explicacao_simples: "{n['explicacao_simples'].replace('\"', '\\\"')}"
        )""")

    passos_typ = []
    for p in dados["instalacao_producao"]["passos"]:
        analogia_escapada = p.get("analogia", "").replace('\"', '\\\"')
        ok_escapado = p.get("como_saber_se_deu_certo", "").replace('\"', '\\\"')
        passos_typ.append(f"""(
          numero: {p['numero']},
          titulo: "{p['titulo']}",
          descricao: "{p['descricao'].replace('\"', '\\\"')}",
          analogia: "{analogia_escapada}",
          como_saber_se_deu_certo: "{ok_escapado}",
          comandos: "{p['comandos'].replace('\\', '\\\\').replace('\"', '\\\"').replace('\n', '\\n')}",
          fonte_id: "{p['fonte_id']}"
        )""")

    primeiro_voo_typ = []
    for pv in dados.get("manual_uso_exaustivo", {}).get("roteiro_primeiro_voo", []):
        primeiro_voo_typ.append(f"""(
          passo: "{pv['passo']}",
          acao: "{pv['acao'].replace('\"', '\\\"')}",
          resultado_esperado: "{pv['resultado_esperado'].replace('\"', '\\\"')}"
        )""")

    cli_typ = []
    for c in dados["manual_uso_exaustivo"]["comandos_cli"]:
        cli_typ.append(f"""(
          comando: "{c['comando']}",
          descricao: "{c['descricao'].replace('\"', '\\\"')}",
          exemplo: "{c['exemplo']}"
        )""")

    refs_typ = []
    for r in dados["referencias_bibliograficas"]:
        refs_typ.append(f"""(
          id: "{r['id']}",
          categoria: "{r['categoria']}",
          titulo: "{r['titulo'].replace('\"', '\\\"')}",
          autor_ou_canal: "{r['autor_ou_canal']}"
        )""")

    nivelamento_str = f"({', '.join(nivelamento_typ)}, )" if nivelamento_typ else "()"
    passos_str = f"({', '.join(passos_typ)}, )" if passos_typ else "()"
    primeiro_voo_str = f"({', '.join(primeiro_voo_typ)}, )" if primeiro_voo_typ else "()"
    cli_str = f"({', '.join(cli_typ)}, )" if cli_typ else "()"
    refs_str = f"({', '.join(refs_typ)}, )" if refs_typ else "()"

    return f"""#import "/scripts/padroes/template_manual_operacional.typ": gerar_manual_typst

#gerar_manual_typst(
  produto_foco: "{dados['produto_foco']}",
  versao: "{dados['versao']}",
  licenca_osi: "{dados['licenca_osi']}",
  vps_modelo: "{vps['provedor_modelo']}",
  vps_specs: "{vps['vcpu']} · {vps['ram']} · {vps['armazenamento']}",
  vps_so: "{vps['so_recomendado']}",
  vps_custo: "{vps['custo_mensal_estimado']}",
  nivelamento: {nivelamento_str},
  passos: {passos_str},
  primeiro_voo: {primeiro_voo_str},
  comandos_cli: {cli_str},
  referencias: {refs_str}
)
"""

def compilar_manual(slug: str) -> bool:
    data_file = BASE_DIR / "scripts" / "data" / f"manual-{slug}.json"
    if not data_file.exists():
        print(f"❌ Arquivo de dados não encontrado: {data_file}")
        return False

    with open(data_file, "r", encoding="utf-8") as f:
        dados = json.load(f)

    out_dir = BASE_DIR / "output" / slug / "manuais"
    docs_dir = BASE_DIR / "docs" / slug / "manuais"
    out_dir.mkdir(parents=True, exist_ok=True)
    docs_dir.mkdir(parents=True, exist_ok=True)

    # 1. HTML
    html_content = renderizar_manual_html(dados)
    html_out = out_dir / f"manual-{slug}-vps-e-uso.html"
    html_docs = docs_dir / f"manual-{slug}-vps-e-uso.html"
    html_out.write_text(html_content, encoding="utf-8")
    html_docs.write_text(html_content, encoding="utf-8")
    print(f"✅ HTML compilado: {html_out.name} (espelhado em docs/manuais/)")

    # 2. Markdown
    md_content = gerar_markdown_manual(dados)
    md_out = out_dir / f"manual-{slug}-vps-e-uso.md"
    md_docs = docs_dir / f"manual-{slug}-vps-e-uso.md"
    md_out.write_text(md_content, encoding="utf-8")
    md_docs.write_text(md_content, encoding="utf-8")
    print(f"✅ Markdown compilado: {md_out.name} (espelhado em docs/manuais/)")

    # 3. PDF via Typst
    typ_content = gerar_typst_codigo(dados)
    typ_temp = out_dir / f"manual-{slug}-vps-e-uso.typ"
    typ_temp.write_text(typ_content, encoding="utf-8")
    pdf_out = out_dir / f"manual-{slug}-vps-e-uso.pdf"
    pdf_docs = docs_dir / f"manual-{slug}-vps-e-uso.pdf"

    try:
        res = subprocess.run(
            ["typst", "compile", "--root", str(BASE_DIR), str(typ_temp), str(pdf_out)],
            cwd=str(BASE_DIR),
            capture_output=True,
            text=True
        )
        if res.returncode == 0 and pdf_out.exists():
            pdf_docs.write_bytes(pdf_out.read_bytes())
            print(f"✅ PDF Executivo compilado via Typst: {pdf_out.name} (espelhado em docs/manuais/)")
        else:
            print(f"⚠️ Aviso na compilação Typst: {res.stderr}")
    except Exception as e:
        print(f"⚠️ Erro ao invocar Typst: {e}")

    if typ_temp.exists():
        typ_temp.unlink()

    return True

if __name__ == "__main__":
    slug_alvo = sys.argv[1] if len(sys.argv) > 1 else "screenpipe"
    compilar_manual(slug_alvo)
