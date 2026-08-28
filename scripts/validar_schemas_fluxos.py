# -*- coding: utf-8 -*-
"""
VALIDADOR MECÂNICO DE SCHEMAS E LINTER DE QUALIDADE (REGRA R9 & PADRÃO DIAMANTE)
Valida a integridade e densidade técnica dos dados estruturados antes da renderização.
Fornece feedback cirúrgico em PT-BR se qualquer bloco obrigatório estiver ausente.
"""
import os
import sys
import json
from pathlib import Path
from typing import Dict, Any, Tuple, List

def console_utf8():
    if sys.platform == "win32":
        try:
            sys.stdout.reconfigure(encoding="utf-8")
            sys.stderr.reconfigure(encoding="utf-8")
        except Exception:
            pass

console_utf8()

BASE_DIR = Path(__file__).resolve().parent.parent

def carregar_json_seguro(caminho: Path) -> Dict[str, Any]:
    if not caminho.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho}")
    with open(caminho, "r", encoding="utf-8-sig") as f:
        return json.load(f)

def validar_lista_horizontal(dados: Dict[str, Any]) -> Tuple[bool, List[str]]:
    erros = []
    campos_raiz = ["slug", "titulo", "deck", "hero", "ferramentas"]
    for c in campos_raiz:
        if c not in dados or not dados[c]:
            erros.append(f"Campo obrigatório na raiz ausente ou vazio: '{c}'")

    ferramentas = dados.get("ferramentas", [])
    if not ferramentas or len(ferramentas) < 5:
        erros.append(f"A lista horizontal deve conter no mínimo 5 ferramentas (encontradas: {len(ferramentas)})")

    for idx, f in enumerate(ferramentas, 1):
        prefixo = f"Ferramenta #{idx} ({f.get('nome', 'Sem Nome')}):"
        campos_f = ["slug", "nome", "licenca_osi", "saas_substituido", "o_que_faz", "como_funciona", "comando_rapido", "requisitos_infra", "passos_praticos", "design_system"]
        for cf in campos_f:
            if cf not in f or not f[cf]:
                erros.append(f"{prefixo} Campo obrigatório '{cf}' ausente ou vazio.")

        infra = f.get("requisitos_infra", {})
        if not infra.get("ram_minima") or not infra.get("cpu_minima"):
            erros.append(f"{prefixo} Bloco 'requisitos_infra' deve conter 'ram_minima' e 'cpu_minima'.")

        passos = f.get("passos_praticos", [])
        if len(passos) < 3:
            erros.append(f"{prefixo} Deve conter no mínimo 3 'passos_praticos' de uso.")

    return len(erros) == 0, erros

def validar_dossie_vertical(dados: Dict[str, Any]) -> Tuple[bool, List[str]]:
    erros = []
    campos_raiz = ["titulo", "slug", "deck", "saas_em_foco", "stats", "quinteto"]
    for c in campos_raiz:
        if c not in dados or not dados[c]:
            erros.append(f"Campo obrigatório na raiz ausente ou vazio: '{c}'")

    quinteto = dados.get("quinteto", [])
    if len(quinteto) != 5:
        erros.append(f"O Dossiê Vertical DEVE conter exatamente 5 ferramentas no Quinteto Soberano (encontradas: {len(quinteto)})")

    classificacoes_esperadas = {
        "A Mais Robusta",
        "A Mais Completa",
        "A Mais Moderna",
        "A Mais Leve",
        "A Mais Simples"
    }
    classificacoes_encontradas = set()

    for idx, f in enumerate(quinteto, 1):
        prefixo = f"Membro do Quinteto #{idx} ({f.get('nome', 'Sem Nome')}):"
        cls_nome = f.get("classificacao", "").strip()
        classificacoes_encontradas.add(cls_nome)

        campos_q = ["slug", "nome", "classificacao", "licenca_osi", "o_que_faz", "como_funciona", "comando_rapido", "requisitos_infra", "passos_praticos"]
        for cq in campos_q:
            if cq not in f or not f[cq]:
                erros.append(f"{prefixo} Campo obrigatório '{cq}' ausente ou vazio.")

    faltantes = classificacoes_esperadas - classificacoes_encontradas
    if faltantes:
        erros.append(f"Classificações do Quinteto Soberano ausentes: {', '.join(faltantes)}")

    return len(erros) == 0, erros

def validar_manual_operacional(dados: Dict[str, Any]) -> Tuple[bool, List[str]]:
    erros = []
    campos_raiz = ["produto_foco", "slug", "saas_origem", "vps_recomendada", "instalacao_producao", "manual_uso_exaustivo", "desinstalacao_cirurgica", "referencias_bibliograficas"]
    for c in campos_raiz:
        if c not in dados or not dados[c]:
            erros.append(f"Manual Operacional VPS: Campo obrigatório '{c}' ausente ou vazio.")

    # 1. Validação de VPS
    vps = dados.get("vps_recomendada", {})
    if not vps.get("vcpu") or not vps.get("ram") or not vps.get("so_recomendado"):
        erros.append("Bloco 'vps_recomendada' deve conter 'vcpu', 'ram' e 'so_recomendado'.")

    # 2. Validação de Instalação de Produção
    inst = dados.get("instalacao_producao", {})
    if not inst.get("passos") or len(inst["passos"]) < 3:
        erros.append("Bloco 'instalacao_producao.passos' deve conter no mínimo 3 passos guiados.")
    if not inst.get("arquivos_configuracao") or len(inst["arquivos_configuracao"]) < 1:
        erros.append("Bloco 'instalacao_producao.arquivos_configuracao' deve conter ao menos 1 arquivo de produção (ex: docker-compose.yml).")

    # 3. Validação de Uso Exaustivo
    uso = dados.get("manual_uso_exaustivo", {})
    if not uso.get("roteiro_primeiro_voo") or len(uso["roteiro_primeiro_voo"]) < 3:
        erros.append("Bloco 'manual_uso_exaustivo.roteiro_primeiro_voo' deve conter ao menos 3 passos.")
    if not uso.get("comandos_cli") or len(uso["comandos_cli"]) < 2:
        erros.append("Bloco 'manual_uso_exaustivo.comandos_cli' deve conter ao menos 2 comandos de operação.")

    # 4. Validação Mandatória de Desinstalação Cirúrgica
    desinst = dados.get("desinstalacao_cirurgica", {})
    if not desinst.get("principio_isolamento"):
        erros.append("Bloco 'desinstalacao_cirurgica' DEVE conter o 'principio_isolamento' de segurança da VPS.")
    if not desinst.get("passos") or len(desinst["passos"]) < 4:
        erros.append("Bloco 'desinstalacao_cirurgica.passos' deve conter os 4 passos seguros de isolamento.")
    if not desinst.get("checklist_saude_vps") or len(desinst["checklist_saude_vps"]) < 3:
        erros.append("Bloco 'desinstalacao_cirurgica.checklist_saude_vps' deve conter ao menos 3 checagens de integridade pós-remoção.")

    # 5. Fontes Auditadas
    fontes = dados.get("referencias_bibliograficas", [])
    if len(fontes) < 3:
        erros.append(f"Devem ser fornecidas no mínimo 3 fontes bibliográficas auditadas (encontradas: {len(fontes)}).")

    return len(erros) == 0, erros

def validar_trilha_aprendizado(dados: Dict[str, Any]) -> Tuple[bool, List[str]]:
    erros = []
    campos_raiz = ["produto_foco", "slug", "saas_origem", "fases"]
    for c in campos_raiz:
        if c not in dados or not dados[c]:
            erros.append(f"Trilha de Aprendizado: Campo obrigatório '{c}' ausente ou vazio.")

    fases = dados.get("fases", [])
    if len(fases) < 3:
        erros.append(f"A Trilha de Aprendizado deve conter no mínimo 3 fases (encontradas: {len(fases)}).")

    for idx, fase in enumerate(fases, 1):
        if not fase.get("titulo") or not fase.get("objetivo") or not fase.get("recursos"):
            erros.append(f"Fase #{idx} da Trilha: Deve conter 'titulo', 'objetivo' e lista de 'recursos'.")

    return len(erros) == 0, erros

def validar_ecossistema(dados: Dict[str, Any]) -> Tuple[bool, List[str]]:
    erros = []
    campos_raiz = [
        "slug", "nome_ecossistema", "titulo", "subtitulo", "deck",
        "saas_substituido", "stats", "pilares", "camada_integracao",
        "deploy_consolidado", "analise_economica_global"
    ]
    for c in campos_raiz:
        if c not in dados or not dados[c]:
            erros.append(f"Ecossistema: Campo obrigatório '{c}' ausente ou vazio.")

    pilares = dados.get("pilares", [])
    if len(pilares) < 2:
        erros.append(f"O Dossiê de Ecossistema deve conter no mínimo 2 pilares funcionais (encontrados: {len(pilares)}).")

    total_ferramentas = 0
    for idx, pilar in enumerate(pilares, 1):
        prefixo_p = f"Pilar #{idx} ({pilar.get('nome_pilar', 'Sem Nome')}):"
        if not pilar.get("nome_pilar") or not pilar.get("modulo_saas_alvo"):
            erros.append(f"{prefixo_p} Deve conter 'nome_pilar' e 'modulo_saas_alvo'.")
        if not pilar.get("subtotal_economia_anual"):
            erros.append(f"{prefixo_p} Deve conter 'subtotal_economia_anual' do grupo.")
        
        ferrs = pilar.get("ferramentas", [])
        if len(ferrs) < 2:
            erros.append(f"{prefixo_p} Deve conter no mínimo 2 ferramentas recomendadas (encontradas: {len(ferrs)}).")
        total_ferramentas += len(ferrs)

        for f_idx, f in enumerate(ferrs, 1):
            prefixo_f = f"{prefixo_p} Ferramenta #{f_idx} ({f.get('nome', 'Sem Nome')}):"
            for campo in ["slug", "nome", "papel_no_pilar", "saas_substituido_direto", "racional_escolha", "economia_anual_str", "licenca_osi", "o_que_faz", "como_funciona", "comando_rapido"]:
                if campo not in f or not f[campo]:
                    erros.append(f"{prefixo_f} Campo obrigatório '{campo}' ausente ou vazio.")

    integracao = dados.get("camada_integracao", {})
    for ci in ["autenticacao_sso", "barramento_eventos", "gateway_reverse_proxy", "fluxo_integracao_descricao"]:
        if ci not in integracao or not integracao[ci]:
            erros.append(f"Camada de Integração: Campo obrigatório '{ci}' ausente ou vazio.")

    deploy = dados.get("deploy_consolidado", {})
    if not deploy.get("docker_compose_exemplo") or not deploy.get("passos_deploy"):
        erros.append("Deploy Consolidado: 'docker_compose_exemplo' e 'passos_deploy' são obrigatórios.")
    if not deploy.get("composicao_stack_detalhada"):
        erros.append("Deploy Consolidado: 'composicao_stack_detalhada' é obrigatório.")

    guia = dados.get("guia_modularidade_e_expansao", {})
    for cg in ["filosofia_modular", "passo_a_passo_adicionar_ferramenta", "passo_a_passo_substituir_hotswap", "passo_a_passo_remover_ferramenta", "exemplo_caso_pratico_hotswap"]:
        if cg not in guia or not guia[cg]:
            erros.append(f"Guia de Modularidade: Campo obrigatório '{cg}' ausente ou vazio.")

    return len(erros) == 0, erros

def auditar_e_bloquear(tipo_fluxo: str, caminho_json: Path) -> bool:
    print(f"\n🔍 [Gate de Qualidade R9] Auditando schema e densidade técnica: {caminho_json.name}...")
    try:
        dados = carregar_json_seguro(caminho_json)
    except Exception as e:
        print(f"❌ [Gate R9 FALHOU] Erro na leitura do arquivo JSON: {e}")
        return False

    if tipo_fluxo == "fluxo1":
        valido, erros = validar_lista_horizontal(dados)
    elif tipo_fluxo == "fluxo2":
        valido, erros = validar_dossie_vertical(dados)
    elif tipo_fluxo in ("fluxo4", "ecossistema"):
        valido, erros = validar_ecossistema(dados)
    elif tipo_fluxo == "manual_vps":
        valido, erros = validar_manual_operacional(dados)
    elif tipo_fluxo == "trilha":
        valido, erros = validar_trilha_aprendizado(dados)
    else:
        print(f"❌ Tipo de fluxo desconhecido: {tipo_fluxo}")
        return False

    if not valido:
        print("\n" + "!" * 75)
        print("🚨 BLOQUEIO DE QUALIDADE: O arquivo JSON não cumpre o Padrão Diamante!")
        print("!" * 75)
        for e in erros:
            print(f"  • {e}")
        print("!" * 75)
        print("👉 Ação Necessária: Preencha os campos faltantes com profundidade técnica antes de compilar.\n")
        return False

    print(f"   ✅ [Gate R9 APROVADO] 100% dos requisitos de qualidade e integridade atendidos!")
    return True

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python validar_schemas_fluxos.py <tipo_fluxo: fluxo1|fluxo2|manual_vps|trilha> <caminho_json>")
        sys.exit(1)
    
    tipo = sys.argv[1]
    caminho = Path(sys.argv[2])
    sucesso = auditar_e_bloquear(tipo, caminho)
    sys.exit(0 if sucesso else 1)
