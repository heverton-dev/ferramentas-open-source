#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Renderiza o relatorio de auditoria em HTML e converte para PDF com o navegador
headless ja instalado. Nao instala nada.

Modos:
    --modo baseline     achados de uma auditoria
    --modo comparativo  antes/depois com veredito do gate
    --verificar <pdf>   confere paginas e tamanho de um PDF ja gerado

Uso:
    python render_relatorio.py --achados baseline.json --modo baseline \
        --saida docs/security-audit/relatorio-baseline.pdf
    python render_relatorio.py --comparativo comparativo.json --modo comparativo \
        --saida docs/security-audit/relatorio-antes-depois.pdf
    python render_relatorio.py --verificar docs/security-audit/relatorio-baseline.pdf
"""
import argparse
import html as H
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import date
from pathlib import Path

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

COR = {"critica": "#B91C1C", "alta": "#EA580C", "media": "#D97706",
       "baixa": "#2563EB", "informativa": "#64748B", "forte": "#059669"}
ROTULO = {"critica": "Critica", "alta": "Alta", "media": "Media",
          "baixa": "Baixa", "informativa": "Informativa"}
SEVS = ["critica", "alta", "media", "baixa", "informativa"]
CAT_NOME = {
    "banco-sem-tranca": "Banco sem tranca",
    "permissao-navegador": "Permissao no navegador",
    "idor": "IDOR",
    "chaves-expostas": "Chaves expostas",
    "inputs-sem-tratamento": "Inputs sem tratamento",
}

NAVEGADORES = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "google-chrome", "chromium", "chromium-browser", "microsoft-edge",
]

CSS = """
@page { size: A4; margin: 2cm; }
* { margin:0; padding:0; box-sizing:border-box; }
body { font-family:"Segoe UI",Helvetica,Arial,sans-serif; font-size:10.5pt;
       line-height:1.55; color:#1e293b; background:#fff; }
h1 { font-size:25pt; color:#0f2f4f; line-height:1.15; }
h2 { font-size:15pt; color:#0f2f4f; margin:22px 0 10px;
     border-left:4px solid #0f2f4f; padding-left:11px; }
h3 { font-size:12pt; margin:16px 0 8px; }
p { margin-bottom:8px; }
.capa { text-align:center; padding:40px 0 26px; border-bottom:3px solid #0f2f4f;
        margin-bottom:24px; }
.capa .sub { font-size:13pt; color:#475569; margin-top:6px; }
.capa .meta { margin-top:16px; font-size:9.5pt; color:#64748b; }
.grade { display:grid; grid-template-columns:repeat(5,1fr); gap:9px; margin:14px 0 20px; }
.kpi { text-align:center; padding:11px 5px; border:1px solid #e2e8f0; border-radius:5px;
       background:#f8fafc; }
.kpi .n { font-size:20pt; font-weight:700; line-height:1.1; }
.kpi .r { font-size:8pt; color:#64748b; text-transform:uppercase; letter-spacing:.05em; }
table { width:100%; border-collapse:collapse; margin:12px 0 20px; font-size:9.5pt; }
th { background:#0f2f4f; color:#fff; padding:8px 9px; text-align:left; font-weight:600; }
td { border-bottom:1px solid #e2e8f0; padding:7px 9px; vertical-align:top; }
tbody tr:nth-child(even) { background:#f8fafc; }
.chip { display:inline-block; padding:2px 9px; border-radius:11px; font-size:8pt;
        font-weight:700; color:#fff; white-space:nowrap; }
.achado { border:1px solid #e2e8f0; border-left-width:4px; border-radius:5px;
          padding:12px 14px; margin-bottom:12px; background:#fff;
          break-inside:avoid; page-break-inside:avoid; }
.achado h4 { font-size:11pt; margin:6px 0 7px; color:#0f172a; }
.local { font-family:Consolas,monospace; font-size:8.5pt; color:#475569;
         background:#f1f5f9; padding:2px 6px; border-radius:3px; }
.campo { margin-top:6px; font-size:9.5pt; }
.campo b { color:#334155; }
pre { background:#f8fafc; border:1px solid #e2e8f0; border-radius:4px; padding:8px 10px;
      font-family:Consolas,monospace; font-size:8.5pt; overflow-x:auto;
      white-space:pre-wrap; word-break:break-word; margin:6px 0; }
.forte { padding:7px 12px; margin-bottom:6px; background:#ecfdf5;
         border-left:3px solid #059669; font-size:9.5pt; break-inside:avoid; }
.forte .ev { font-family:Consolas,monospace; font-size:8.5pt; color:#047857; }
.na { padding:8px 12px; background:#f8fafc; border-left:3px solid #94a3b8;
      margin-bottom:7px; font-size:9.5pt; }
.gate { padding:15px 18px; border-radius:6px; margin:16px 0; break-inside:avoid; }
.gate.ok { background:#ecfdf5; border:2px solid #059669; }
.gate.fail { background:#fef2f2; border:2px solid #B91C1C; }
.gate h3 { margin:0 0 7px; font-size:13pt; }
.issue { background:#f8fafc; border:1px solid #cbd5e1; border-radius:5px;
         padding:12px 14px; margin-bottom:14px; font-family:Consolas,monospace;
         font-size:8.5pt; white-space:pre-wrap; word-break:break-word;
         break-inside:avoid; page-break-inside:avoid; }
.quebra { page-break-after:always; }
.legenda { font-size:9pt; margin-top:9px; }
.legenda span { display:inline-block; width:11px; height:11px; border-radius:2px;
                margin-right:5px; vertical-align:-1px; }
.nota { font-size:9pt; color:#64748b; font-style:italic; margin-top:9px; }
.setinha { font-weight:700; }
"""


def esc(v) -> str:
    return H.escape(str(v if v is not None else ""))


def achar_navegador():
    for c in NAVEGADORES:
        if os.path.isfile(c):
            return c
        w = shutil.which(c)
        if w:
            return w
    return None


# ------------------------------------------------------------------ graficos

def rosca(contagem: dict, total: int) -> str:
    if total <= 0:
        return '<p class="nota">Sem achados para representar.</p>'
    r, circ = 70, 2 * 3.14159265 * 70
    off, arcos = 0.0, []
    for s in SEVS:
        n = contagem.get(s, 0)
        if not n:
            continue
        comp = circ * n / total
        arcos.append(
            f'<circle cx="110" cy="110" r="{r}" fill="none" stroke="{COR[s]}" '
            f'stroke-width="40" stroke-dasharray="{comp:.2f} {circ - comp:.2f}" '
            f'stroke-dashoffset="{-off:.2f}" transform="rotate(-90 110 110)"/>')
        off += comp
    leg = "".join(
        f'<div><span style="background:{COR[s]}"></span>{ROTULO[s]} — {contagem.get(s,0)} '
        f'({100*contagem.get(s,0)/total:.1f}%)</div>'
        for s in SEVS if contagem.get(s, 0))
    return (f'<svg viewBox="0 0 220 220" width="100%" style="max-width:230px;display:block;margin:0 auto">'
            + "".join(arcos)
            + f'<text x="110" y="105" text-anchor="middle" font-size="30" font-weight="bold" fill="#0f2f4f">{total}</text>'
            + '<text x="110" y="126" text-anchor="middle" font-size="11" fill="#64748b">achados</text>'
            + f'</svg><div class="legenda">{leg}</div>')


def barras(por_cat: dict, nao_aplic: list) -> str:
    itens = [(CAT_NOME.get(k, k), v) for k, v in sorted(por_cat.items(), key=lambda kv: -kv[1])]
    na = {n.get("categoria") for n in nao_aplic}
    for c in CAT_NOME:
        if c in na:
            itens.append((CAT_NOME[c], -1))
    if not itens:
        return ""
    maxv = max([v for _, v in itens if v > 0] or [1])
    alt, linhas, y = 30, [], 12
    for nome, v in itens:
        if v < 0:
            linhas.append(
                f'<text x="150" y="{y+13}" font-size="9" fill="#64748b">nao se aplica a esta stack</text>'
                f'<rect x="146" y="{y}" width="3" height="17" fill="{COR["forte"]}"/>')
        else:
            larg = max(4, int(178 * v / maxv))
            cor = COR["critica"] if v >= maxv else COR["alta"] if v >= maxv * .6 else COR["media"]
            linhas.append(
                f'<rect x="150" y="{y}" width="{larg}" height="17" fill="{cor}" rx="2"/>'
                f'<text x="{150+larg+5}" y="{y+13}" font-size="10" font-weight="bold" fill="{cor}">{v}</text>')
        linhas.append(
            f'<text x="144" y="{y+13}" text-anchor="end" font-size="9.5" fill="#334155">{esc(nome)}</text>')
        y += alt
    return (f'<svg viewBox="0 0 350 {y+10}" width="100%" style="max-width:350px;display:block;margin:0 auto">'
            f'<line x1="149" y1="6" x2="149" y2="{y-6}" stroke="#cbd5e1"/>'
            + "".join(linhas) + '</svg>')


def barras_comp(rb: dict, rp: dict) -> str:
    maxv = max(list(rb.values()) + list(rp.values()) + [1])
    linhas, y = [], 14
    for s in SEVS:
        b, p = rb.get(s, 0), rp.get(s, 0)
        if not b and not p:
            continue
        lb, lp = int(150 * b / maxv), int(150 * p / maxv)
        linhas.append(
            f'<text x="104" y="{y+10}" text-anchor="end" font-size="9.5" fill="#334155">{ROTULO[s]}</text>'
            f'<rect x="110" y="{y}" width="{max(2,lb)}" height="13" fill="{COR[s]}" opacity=".42" rx="2"/>'
            f'<text x="{110+max(2,lb)+4}" y="{y+10}" font-size="8.5" fill="#64748b">{b}</text>'
            f'<rect x="110" y="{y+15}" width="{max(2,lp)}" height="13" fill="{COR[s]}" rx="2"/>'
            f'<text x="{110+max(2,lp)+4}" y="{y+25}" font-size="8.5" font-weight="bold" fill="{COR[s]}">{p}</text>')
        y += 38
    return (f'<svg viewBox="0 0 340 {y+16}" width="100%" style="max-width:340px;display:block;margin:0 auto">'
            + "".join(linhas)
            + f'<text x="110" y="{y+10}" font-size="8.5" fill="#94a3b8">barra clara = antes · barra cheia = depois</text>'
            + '</svg>')


# ------------------------------------------------------------------ blocos

def bloco_achado(a: dict) -> str:
    sev = a.get("severidade", "informativa")
    linhas = ", ".join(str(x) for x in a.get("linhas", []) or [])
    local = esc(a.get("arquivo", "?")) + (f":{esc(linhas)}" if linhas else "")
    p = [f'<div class="achado" style="border-left-color:{COR[sev]}">',
         f'<span class="chip" style="background:{COR[sev]}">{ROTULO[sev]}</span> ',
         f'<span class="local">{local}</span>',
         f'<h4>{esc(a.get("titulo"))}</h4>']
    if a.get("trecho"):
        p.append(f'<pre>{esc(a["trecho"])}</pre>')
    for rot, ch in (("Por que e explorável", "por_que_exploravel"),
                    ("Impacto", "impacto"),
                    ("Condicoes", "condicoes"),
                    ("Correcao", "correcao")):
        if a.get(ch):
            p.append(f'<div class="campo"><b>{rot}:</b> {esc(a[ch])}</div>')
    p.append("</div>")
    return "".join(p)


def secao_issues(achados: list) -> str:
    acion = [a for a in achados if a.get("severidade") != "informativa"]
    if not acion:
        return "<p>Nenhum achado acionavel.</p>"
    ordem = {s: i for i, s in enumerate(SEVS)}
    acion.sort(key=lambda a: ordem.get(a.get("severidade"), 9))
    out = []
    for i, a in enumerate(acion, 1):
        sev = a.get("severidade", "media")
        linhas = ", ".join(str(x) for x in a.get("linhas", []) or []) or "-"
        corpo = f"""--- ISSUE {i} ---
## [Seguranca] {a.get('titulo','')}

**Labels:** `security`, `{sev}`
**Categoria:** {CAT_NOME.get(a.get('categoria'), a.get('categoria',''))}

### Problema

{a.get('por_que_exploravel','')}

### Evidencia

`{a.get('arquivo','')}:{linhas}`

```
{a.get('trecho','')}
```

### Impacto

{a.get('impacto','')}

**Condicoes:** {a.get('condicoes','nenhuma')}

### Correcao sugerida

{a.get('correcao','')}

### Criterios de aceite

- [ ] Correcao aplicada em `{a.get('arquivo','')}`
- [ ] Teste automatizado que falha antes e passa depois
- [ ] Nova varredura nao reporta este achado
{"- [ ] Credencial rotacionada no provedor (o valor antigo esta comprometido)" if a.get('categoria') == 'chaves-expostas' else ""}
--- FIM ISSUE {i} ---"""
        out.append(f'<div class="issue">{esc(corpo)}</div>')
    return "".join(out)


def envelope(titulo: str, corpo: str) -> str:
    return (f'<!DOCTYPE html><html lang="pt-BR"><head><meta charset="UTF-8">'
            f'<title>{esc(titulo)}</title><style>{CSS}</style></head><body>{corpo}</body></html>')


# ------------------------------------------------------------------ paginas

def html_baseline(d: dict, estagio: str) -> str:
    achados = d.get("achados", [])
    cont = {s: sum(1 for a in achados if a.get("severidade") == s) for s in SEVS}
    total = len(achados)
    por_cat = {}
    for a in achados:
        por_cat[a.get("categoria", "?")] = por_cat.get(a.get("categoria", "?"), 0) + 1
    st = d.get("stack", {})
    rotulo = "Pos-correcao" if estagio == "pos" else "Baseline"

    p = [f'<div class="capa"><h1>Relatorio de Auditoria de Seguranca</h1>'
         f'<div class="sub">{esc(d.get("projeto","Projeto"))}</div>'
         f'<div class="meta"><b>Estagio:</b> {rotulo} &nbsp;·&nbsp; '
         f'<b>Data:</b> {esc(d.get("data", date.today().isoformat()))}</div></div>']

    p.append("<h2>Escopo e metodologia</h2>")
    p.append("<table><tbody>")
    for rot, v in (("Linguagens", ", ".join(st.get("linguagens", [])) or "indeterminada"),
                   ("Framework", st.get("framework") or "nenhum"),
                   ("Acesso a dados", st.get("orm") or "nenhum"),
                   ("Autenticacao", st.get("auth") or "nenhuma"),
                   ("Frontend", st.get("frontend") or "nenhum"),
                   ("Deploy", ", ".join(st.get("deploy", [])) or "nenhum arquivo detectado")):
        p.append(f"<tr><td style='width:26%'><b>{rot}</b></td><td>{esc(v)}</td></tr>")
    p.append("</tbody></table>")
    p.append('<p class="nota">Cinco categorias auditadas, cada uma mapeada para o '
             'equivalente desta stack. Achados verificados por leitura do codigo; '
             'varredura textual serviu apenas para levantar candidatos.</p>')

    na = d.get("categorias_nao_aplicaveis", [])
    if na:
        p.append("<h3>Categorias que nao se aplicam</h3>")
        for n in na:
            p.append(f'<div class="na"><b>{esc(CAT_NOME.get(n.get("categoria"), n.get("categoria")))}:</b> '
                     f'{esc(n.get("razao"))}</div>')

    p.append("<h2>Resumo executivo</h2><div class='grade'>")
    for s in SEVS:
        p.append(f'<div class="kpi"><div class="n" style="color:{COR[s]}">{cont[s]}</div>'
                 f'<div class="r">{ROTULO[s]}</div></div>')
    p.append("</div>")
    p.append('<div style="display:flex;gap:22px;flex-wrap:wrap;align-items:flex-start">'
             f'<div style="flex:1;min-width:250px"><h3 style="text-align:center">Por severidade</h3>{rosca(cont,total)}</div>'
             f'<div style="flex:1;min-width:300px"><h3 style="text-align:center">Por categoria</h3>{barras(por_cat,na)}</div>'
             "</div>")

    fortes = d.get("pontos_fortes", [])
    if fortes:
        p.append('<div class="quebra"></div><h2>Pontos fortes</h2>')
        p.append("<p>Verificado e correto — delimita a cobertura desta auditoria.</p>")
        for f in fortes:
            ev = f'<div class="ev">{esc(f.get("evidencia"))}</div>' if f.get("evidencia") else ""
            p.append(f'<div class="forte">{esc(f.get("descricao"))}{ev}</div>')

    if achados:
        p.append('<div class="quebra"></div><h2>Achados</h2>')
        p.append("<table><thead><tr><th style='width:15%'>Severidade</th>"
                 "<th style='width:37%'>Arquivo:linha</th><th>Descricao</th></tr></thead><tbody>")
        ordem = {s: i for i, s in enumerate(SEVS)}
        for a in sorted(achados, key=lambda x: ordem.get(x.get("severidade"), 9)):
            sev = a.get("severidade", "informativa")
            ln = ", ".join(str(x) for x in a.get("linhas", []) or [])
            p.append(f'<tr><td><span class="chip" style="background:{COR[sev]}">{ROTULO[sev]}</span></td>'
                     f'<td><span class="local">{esc(a.get("arquivo"))}{":" + esc(ln) if ln else ""}</span></td>'
                     f'<td>{esc(a.get("titulo"))}</td></tr>')
        p.append("</tbody></table>")

        for cat in sorted({a.get("categoria") for a in achados}):
            p.append(f'<h3>{esc(CAT_NOME.get(cat, cat))}</h3>')
            ordem = {s: i for i, s in enumerate(SEVS)}
            for a in sorted([x for x in achados if x.get("categoria") == cat],
                            key=lambda x: ordem.get(x.get("severidade"), 9)):
                p.append(bloco_achado(a))

        p.append('<div class="quebra"></div><h2>Issues para o GitHub</h2>')
        p.append("<p>Cada bloco abaixo e uma issue completa, pronta para copiar.</p>")
        p.append(secao_issues(achados))

    return envelope(f"Auditoria de Seguranca — {d.get('projeto','Projeto')}", "".join(p))


def html_comparativo(c: dict) -> str:
    r = c.get("resumo", {})
    rb, rp = r.get("baseline", {}), r.get("pos", {})
    ok = r.get("gate") == "aprovado"

    p = [f'<div class="capa"><h1>Auditoria de Seguranca — Antes e Depois</h1>'
         f'<div class="sub">{esc(c.get("projeto","Projeto"))}</div>'
         f'<div class="meta"><b>Data:</b> {date.today().isoformat()}</div></div>']

    p.append(f'<div class="gate {"ok" if ok else "fail"}">'
             f'<h3 style="color:{COR["forte"] if ok else COR["critica"]}">'
             f'Gate do ciclo: {"APROVADO" if ok else "REPROVADO"}</h3>')
    if ok:
        p.append("<p>Nenhum critico do baseline seguiu aberto e nenhum achado novo "
                 "foi introduzido pela correcao.</p>")
    else:
        p.append("<p>O ciclo nao fecha enquanto os pontos abaixo existirem:</p><ul>")
        for m in r.get("gate_motivos", []):
            p.append(f"<li>{esc(m)}</li>")
        p.append("</ul>")
    p.append("</div>")

    p.append("<h2>Resultado</h2><div class='grade'>")
    for rot, val, cor in (("Antes", r.get("total_baseline", 0), "#0f2f4f"),
                          ("Corrigidos", r.get("corrigidos", 0), COR["forte"]),
                          ("Persistentes", r.get("persistentes", 0), COR["media"]),
                          ("Novos", r.get("novos", 0), COR["critica"]),
                          ("Depois", r.get("total_pos", 0), "#0f2f4f")):
        p.append(f'<div class="kpi"><div class="n" style="color:{cor}">{val}</div>'
                 f'<div class="r">{rot}</div></div>')
    p.append("</div>")
    p.append(f'<p><b>Taxa de correcao:</b> {r.get("taxa_correcao_pct",0)}% '
             f'<span class="nota">(exclui informativas — divida arquitetural nao conta como vulnerabilidade)</span></p>')

    p.append('<div style="display:flex;gap:22px;flex-wrap:wrap;align-items:flex-start">'
             f'<div style="flex:1;min-width:250px"><h3 style="text-align:center">Antes</h3>'
             f'{rosca(rb, r.get("total_baseline",0))}</div>'
             f'<div style="flex:1;min-width:250px"><h3 style="text-align:center">Depois</h3>'
             f'{rosca(rp, r.get("total_pos",0))}</div></div>')
    p.append(f'<h3 style="text-align:center;margin-top:18px">Severidade lado a lado</h3>{barras_comp(rb,rp)}')

    def tabela(titulo, itens, vazio, cor):
        if not itens:
            return f'<h2>{titulo}</h2><p class="nota">{vazio}</p>'
        linhas = "".join(
            f'<tr><td><span class="chip" style="background:{COR.get(i.get("severidade"),"#64748B")}">'
            f'{ROTULO.get(i.get("severidade"),"?")}</span></td>'
            f'<td><span class="local">{esc(i.get("arquivo"))}</span></td>'
            f'<td>{esc(i.get("titulo"))}</td></tr>' for i in itens)
        return (f'<h2 style="border-left-color:{cor}">{titulo} ({len(itens)})</h2>'
                f'<table><thead><tr><th style="width:15%">Severidade</th>'
                f'<th style="width:37%">Arquivo</th><th>Descricao</th></tr></thead>'
                f'<tbody>{linhas}</tbody></table>')

    p.append('<div class="quebra"></div>')
    p.append(tabela("Corrigidos", c.get("corrigidos", []),
                    "Nenhum achado foi corrigido neste ciclo.", COR["forte"]))
    p.append(tabela("Persistentes", c.get("persistentes", []),
                    "Nenhum achado do baseline seguiu aberto.", COR["media"]))
    p.append(tabela("Novos", c.get("novos", []),
                    "Nenhum achado novo — a correcao nao introduziu regressao.", COR["critica"]))
    if c.get("novos"):
        p.append('<p class="nota">Achado novo tem duas origens possiveis: regressao '
                 'introduzida pela correcao, ou achado que a primeira passada nao viu. '
                 'Distinga os dois casos antes de fechar o ciclo.</p>')

    return envelope(f"Antes e Depois — {c.get('projeto','Projeto')}", "".join(p))


# ------------------------------------------------------------------ pdf

def gerar_pdf(html: str, destino: Path) -> bool:
    nav = achar_navegador()
    destino = destino.resolve()  # as_uri() exige caminho absoluto
    destino.parent.mkdir(parents=True, exist_ok=True)
    tmp = destino.with_suffix(".html")
    tmp.write_text(html, encoding="utf-8")
    if not nav:
        print("[!] Navegador headless nao encontrado. HTML salvo em:", tmp)
        print("    Abra e imprima como PDF, ou instale Chrome/Edge.")
        return False
    try:
        subprocess.run([nav, "--headless=new", "--disable-gpu", "--no-sandbox",
                        f"--print-to-pdf={destino}", tmp.as_uri()],
                       check=True, capture_output=True, timeout=180)
        return destino.is_file()
    except Exception as e:
        print(f"[!] Falha ao converter: {e}\n    HTML preservado em: {tmp}")
        return False


def verificar(pdf: Path) -> int:
    if not pdf.is_file():
        print(f"[!] PDF inexistente: {pdf}")
        return 1
    d = pdf.read_bytes()
    n = len(re.findall(rb"/Type\s*/Page[^s]", d))
    kb = len(d) // 1024
    print(f"[ok] {pdf}")
    print(f"     paginas: {n} | tamanho: {kb} KB")
    if n == 0:
        print("[!] Nenhuma pagina detectada — PDF provavelmente corrompido.")
        return 1
    if kb < 12:
        print("[!] Muito pequeno: verifique se o conteudo foi renderizado.")
        return 1
    print("[!] Conferencia automatica nao substitui olhar: rasterize e confira "
          "grafico, tabela e quebra de pagina.")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--achados")
    ap.add_argument("--comparativo")
    ap.add_argument("--modo", choices=["baseline", "pos", "comparativo"], default="baseline")
    ap.add_argument("--saida")
    ap.add_argument("--verificar")
    args = ap.parse_args()

    if args.verificar:
        return verificar(Path(args.verificar))

    if args.modo == "comparativo":
        if not args.comparativo:
            print("[!] --comparativo e obrigatorio no modo comparativo")
            return 1
        dados = json.loads(Path(args.comparativo).read_text(encoding="utf-8"))
        html = html_comparativo(dados)
        padrao = "docs/security-audit/relatorio-antes-depois.pdf"
    else:
        if not args.achados:
            print("[!] --achados e obrigatorio")
            return 1
        dados = json.loads(Path(args.achados).read_text(encoding="utf-8"))
        html = html_baseline(dados, args.modo)
        padrao = f"docs/security-audit/relatorio-{'pos-correcao' if args.modo=='pos' else 'baseline'}.pdf"

    destino = Path(args.saida or padrao)
    if gerar_pdf(html, destino):
        print(f"[ok] PDF gerado: {destino}")
        return verificar(destino)
    return 1


if __name__ == "__main__":
    sys.exit(main())
