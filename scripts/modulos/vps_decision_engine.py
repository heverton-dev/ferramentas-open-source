# -*- coding: utf-8 -*-

class VPSDecisionEngine:
    ECOSYSTEM_PROFILES = {
        "ecos-google-workspace": {
            "name": "Ecossistema Google Workspace (Nextcloud + ONLYOFFICE + Stalwart + CryptPad)",
            "req_cpu": 4,
            "req_ram_gb": 7.0,
            "host_ports": [],
            "subdomains": ["drive", "office", "mail", "docs", "sso"],
            "recommended_db": "postgres",
            "components": [
                {"name": "Nextcloud Hub", "ram_gb": 2.5, "role": "Drive, Contatos, Calendario e Chat"},
                {"name": "ONLYOFFICE Document Server", "ram_gb": 2.5, "role": "Editor Docs, Sheets e Slides"},
                {"name": "Stalwart Mail Server", "ram_gb": 1.0, "role": "Servidor de E-mail Corporativo"},
                {"name": "CryptPad", "ram_gb": 1.0, "role": "Docs Criptografados e Formularios"}
            ]
        },
        "ecos-crm-marketing": {
            "name": "Ecossistema CRM & Automacao de Marketing (Chatwoot + Twenty + Evolution + Mautic)",
            "req_cpu": 3,
            "req_ram_gb": 4.5,
            "host_ports": [],
            "subdomains": ["chat", "crm", "wpp", "campaigns"],
            "recommended_db": "postgres",
            "components": [
                {"name": "Chatwoot", "ram_gb": 1.5, "role": "Atendimento Omnichannel"},
                {"name": "Twenty CRM", "ram_gb": 1.5, "role": "CRM Open Source Moderno"},
                {"name": "Evolution API", "ram_gb": 1.0, "role": "API de WhatsApp (Ja Ativo na VPS)"},
                {"name": "Mautic", "ram_gb": 1.0, "role": "Automacao de E-mail (Ja Ativo na VPS)"}
            ]
        },
        "ecos-devops-infra": {
            "name": "Ecossistema DevOps & Engenharia de Dados (NocoDB + Supabase + n8n + Directus)",
            "req_cpu": 4,
            "req_ram_gb": 6.0,
            "host_ports": [],
            "subdomains": ["nocodb", "supabase", "directus"],
            "recommended_db": "postgres",
            "components": [
                {"name": "NocoDB", "ram_gb": 1.0, "role": "Airtable Open Source"},
                {"name": "Directus", "ram_gb": 1.5, "role": "Headless CMS & API de Dados"},
                {"name": "n8n", "ram_gb": 1.5, "role": "Orquestrador de Workflows (Ja Ativo na VPS)"}
            ]
        }
    }

    TOOL_PROFILES = {
        "stalwart": {
            "name": "Stalwart All-in-One Mail Server",
            "req_cpu": 1.5,
            "req_ram_gb": 1.5,
            "host_ports": [25, 465, 587, 993],
            "subdomains": ["mail"],
            "role": "Servidor de E-mail e Colaboracao JMAP/IMAP/SMTP"
        },
        "nextcloud": {
            "name": "Nextcloud Hub",
            "req_cpu": 2.0,
            "req_ram_gb": 2.5,
            "host_ports": [],
            "subdomains": ["drive"],
            "role": "Armazenamento de Arquivos, Calendario e Contatos"
        },
        "onlyoffice": {
            "name": "ONLYOFFICE Document Server",
            "req_cpu": 2.0,
            "req_ram_gb": 2.5,
            "host_ports": [],
            "subdomains": ["office"],
            "role": "Motor de Edi??o Colaborativa de Documentos"
        },
        "cryptpad": {
            "name": "CryptPad",
            "req_cpu": 1.5,
            "req_ram_gb": 1.0,
            "host_ports": [],
            "subdomains": ["docs"],
            "role": "Su?te Office Criptografada Zero-Knowledge"
        },
        "seafile": {
            "name": "Seafile Professional/Community",
            "req_cpu": 1.5,
            "req_ram_gb": 1.5,
            "host_ports": [],
            "subdomains": ["drive"],
            "role": "Sincronizacao R?pida de Arquivos Corporativos"
        },
        "zitadel": {
            "name": "Zitadel Identity Management",
            "req_cpu": 1.5,
            "req_ram_gb": 1.5,
            "host_ports": [],
            "subdomains": ["sso"],
            "role": "Gest?o de Identidade e Single Sign-On (SSO)"
        },
        "chatwoot": {
            "name": "Chatwoot Omnichannel",
            "req_cpu": 1.5,
            "req_ram_gb": 1.5,
            "host_ports": [],
            "subdomains": ["chat"],
            "role": "Atendimento e Helpdesk Multicanal"
        },
        "nocodb": {
            "name": "NocoDB",
            "req_cpu": 1.0,
            "req_ram_gb": 1.0,
            "host_ports": [],
            "subdomains": ["nocodb"],
            "role": "Banco de Dados No-Code e Planilhas Inteligentes"
        }
    }

    def __init__(self, audit_data):
        self.audit = audit_data

    def evaluate_ecosystem(self, ecos_slug):
        profile = self.ECOSYSTEM_PROFILES.get(ecos_slug)
        if not profile:
            profile = {
                "name": f"Ecossistema {ecos_slug}",
                "req_cpu": 3.0,
                "req_ram_gb": 5.0,
                "host_ports": [],
                "subdomains": ["app", "api"],
                "components": []
            }
        return self._run_evaluation(profile, "ecossistema")

    def evaluate_tool(self, tool_slug):
        profile = self.TOOL_PROFILES.get(tool_slug)
        if not profile:
            profile = {
                "name": f"Ferramenta {tool_slug}",
                "req_cpu": 1.5,
                "req_ram_gb": 1.5,
                "host_ports": [],
                "subdomains": [tool_slug],
                "role": "Ferramenta Open Source Aut?noma"
            }
        return self._run_evaluation(profile, "ferramenta")

    def evaluate_multi_target(self, targets_list):
        """Avalia m?ltiplos alvos de forma cumulativa contra o headroom da VPS."""
        total_req_cpu = 0
        total_req_ram = 0
        all_host_ports = []
        evaluations = []

        for target in targets_list:
            t_type = target.get("tipo")
            t_slug = target.get("slug")
            if t_type == "ecossistema":
                ev = self.evaluate_ecosystem(t_slug)
            else:
                ev = self.evaluate_tool(t_slug)
            evaluations.append(ev)
            total_req_cpu += ev["profile"]["req_cpu"]
            total_req_ram += ev["profile"]["req_ram_gb"]
            all_host_ports.extend(ev["profile"].get("host_ports", []))

        hw = self.audit["hardware"]
        free_cpu = max(0, hw["total_cpu"] - (hw["running_containers"] * 0.1))
        free_ram = hw["est_mem_free_gb"]

        cumul_cpu_ok = free_cpu >= total_req_cpu
        cumul_ram_ok = free_ram >= total_req_ram

        conflicting_ports = [p for p in set(all_host_ports) if p in set(self.audit["existing_ports"])]
        cumul_ports_ok = len(conflicting_ports) == 0

        score = 100
        alerts = []
        recommendations = []

        if not cumul_ram_ok:
            score -= 50
            alerts.append(f"Carga cumulativa excede a RAM livre: Exigido {total_req_ram:.1f} GB vs Disponivel {free_ram:.1f} GB.")
        else:
            recommendations.append(f"Headroom de RAM aprovado para a carga conjunta: {total_req_ram:.1f} GB de {free_ram:.1f} GB livres.")

        if not cumul_cpu_ok:
            score -= 30
            alerts.append(f"vCPUs insuficientes para execu??o simult?nea de todos os alvos: Exigido {total_req_cpu:.1f} vCPUs vs {free_cpu:.1f} livres.")
        else:
            recommendations.append(f"Capacidade de processamento adequada para todos os alvos ({total_req_cpu:.1f} vCPUs demandadas).")

        if not cumul_ports_ok:
            score -= 20
            alerts.append(f"Conflito cumulativo de portas no host: {conflicting_ports}")

        if score >= 90:
            status = "CONJUNTO TOTALMENTE VIAVEL (100% HOMOLOGADO)"
            level = "GREEN"
        elif score >= 60:
            status = "CONJUNTO VIAVEL COM ADAPTA??ES"
            level = "YELLOW"
        else:
            status = "CONJUNTO INVIAVEL SIMULTANEAMENTE"
            level = "RED"

        return {
            "evaluations": evaluations,
            "cumulative": {
                "status": status,
                "level": level,
                "score": max(0, score),
                "total_req_cpu": round(total_req_cpu, 1),
                "total_req_ram": round(total_req_ram, 1),
                "free_cpu": round(free_cpu, 1),
                "free_ram": round(free_ram, 1),
                "cumul_cpu_ok": cumul_cpu_ok,
                "cumul_ram_ok": cumul_ram_ok,
                "cumul_ports_ok": cumul_ports_ok,
                "alerts": alerts,
                "recommendations": recommendations
            }
        }

    def _run_evaluation(self, profile, target_type):
        hw = self.audit["hardware"]
        existing_ports = set(self.audit["existing_ports"])
        
        req_cpu = profile["req_cpu"]
        req_ram = profile["req_ram_gb"]
        
        free_cpu = max(0, hw["total_cpu"] - (hw["running_containers"] * 0.1))
        free_ram = hw["est_mem_free_gb"]
        
        cpu_ok = free_cpu >= req_cpu
        ram_ok = free_ram >= req_ram
        
        conflicting_ports = [p for p in profile.get("host_ports", []) if p in existing_ports]
        ports_ok = len(conflicting_ports) == 0

        score = 100
        alerts = []
        recommendations = []

        if not ram_ok:
            score -= 50
            alerts.append(f"Memoria RAM insuficiente. Exigido: {req_ram} GB | Livre estimado: {free_ram} GB")
        else:
            recommendations.append(f"Memoria RAM abundante: {free_ram} GB livres para suportar a carga de {req_ram} GB com alta folga.")

        if not cpu_ok:
            score -= 30
            alerts.append(f"vCPUs insuficientes. Exigido: {req_cpu} vCPUs | Disponivel estimado: {free_cpu:.1f} vCPUs")
        else:
            recommendations.append(f"Capacidade de processamento adequada: {hw['total_cpu']} vCPUs totais no servidor.")

        if not ports_ok:
            score -= 20
            alerts.append(f"Conflito de portas no host: {conflicting_ports}")
        else:
            recommendations.append("Zero conflito de portas de host detectado. Roteamento 100% via Traefik e subdominios.")

        if self.audit["ingress"]["detected"]:
            cert = self.audit["ingress"]["certresolvers"][0] if self.audit["ingress"]["certresolvers"] else "letsencryptresolver"
            net = self.audit["ingress"].get("default_overlay", "network_conexao")
            recommendations.append(f"Proxy reverso Traefik detectado com certresolver '{cert}' e rede '{net}'. Integracao direta sem criar novos proxies.")

        if score >= 90:
            status = "TOTALMENTE VIAVEL (100% HOMOLOGADO)"
            level = "GREEN"
        elif score >= 60:
            status = "VIAVEL COM ADAPTA??ES"
            level = "YELLOW"
        else:
            status = "INVIAVEL NO AMBIENTE ATUAL"
            level = "RED"

        return {
            "target_type": target_type,
            "profile": profile,
            "verdict": {
                "status": status,
                "level": level,
                "score": max(0, score),
                "cpu_ok": cpu_ok,
                "ram_ok": ram_ok,
                "ports_ok": ports_ok,
                "free_ram_gb": free_ram,
                "req_ram_gb": req_ram,
                "free_cpu": round(free_cpu, 1),
                "req_cpu": req_cpu,
                "conflicting_ports": conflicting_ports,
                "alerts": alerts,
                "recommendations": recommendations
            }
        }
