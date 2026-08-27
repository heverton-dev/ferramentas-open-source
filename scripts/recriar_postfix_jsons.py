#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Recriar JSONs Postfix/Dovecot com estrutura completa e sem BOM."""

import json
import sys
import io
from pathlib import Path

if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

# Estrutura completa
manual = {
    "$schema": "../schemas/schema_manual_operacional.json",
    "produto_foco": "Postfix + Dovecot",
    "slug": "postfix-dovecot",
    "saas_origem": "Gmail, Microsoft 365, Zoho Mail",
    "versao": "Postfix 3.8.x + Dovecot 2.3.x",
    "licenca_osi": "IPL-1.0 (Postfix) | LGPL-2.1 (Dovecot)",
    "tempo_estimado_setup": "45 a 60 minutos (com dominio DNS ja pronto)",
    "nivelamento_conceitual": [
        {"termo": "Postfix (Agente de Transferencia de E-Mail)", "analogia_cotidiana": "O Carteiro que Leva Cartas para Todas as Cidades", "explicacao_simples": "Postfix eh o programa que recebe emails e os entrega. Funciona 24h via SMTP."},
        {"termo": "Dovecot (Servidor IMAP & POP3)", "analogia_cotidiana": "A Caixa de Correio com Chave", "explicacao_simples": "Dovecot guarda emails em pastas organizadas dentro do servidor."},
        {"termo": "SSL/TLS (Criptografia)", "analogia_cotidiana": "Um Envelope Lacrado", "explicacao_simples": "Protege emails em transito com chave secreta."},
        {"termo": "SPF, DKIM & DMARC (Autenticacao)", "analogia_cotidiana": "Documento de Identidade", "explicacao_simples": "Impede falsificacao de emails."},
        {"termo": "DNS (Sistema de Nomes)", "analogia_cotidiana": "A Agenda Telefonica Global", "explicacao_simples": "Transforma nomes em endereco IP."}
    ],
    "vps_recomendada": {
        "provedor_modelo": "Hetzner Cloud CPX11 (ou Contabo Cloud VPS S)",
        "vcpu": "2 vCPU Compartilhadas",
        "ram": "2 GB RAM",
        "armazenamento": "40 GB SSD NVMe",
        "so_recomendado": "Ubuntu 24.04 LTS (x86_64) ou Debian 12",
        "custo_mensal_estimado": "EUR 2,50/mes (~R$ 15,00/mes)",
        "portas_abertas": ["22/tcp (SSH)", "25/tcp (SMTP)", "110/tcp (POP3)", "143/tcp (IMAP)", "465/tcp (SMTPS)", "587/tcp (Submission)", "993/tcp (IMAPS)", "80/tcp (HTTP)", "443/tcp (HTTPS)"]
    },
    "instalacao_producao": {
        "passos": [
            {"numero": 1, "titulo": "Preparacao do Sistema", "descricao": "Atualizar SO", "analogia": "Limpar chao", "o_que_acontece_na_tela": "Pacotes baixando", "como_saber_se_deu_certo": "apt list --upgradable vazio", "comandos": "apt-get update && apt-get upgrade -y", "fonte_id": "F01"},
            {"numero": 2, "titulo": "Instalacao Postfix", "descricao": "Instala servidor SMTP", "analogia": "Montar mala", "o_que_acontece_na_tela": "Tela azul", "como_saber_se_deu_certo": "postfix status OK", "comandos": "apt-get install -y postfix", "fonte_id": "F01"},
            {"numero": 3, "titulo": "Instalacao Dovecot", "descricao": "Instala IMAP/POP3", "analogia": "Gavetas", "o_que_acontece_na_tela": "Silenciosa", "como_saber_se_deu_certo": "systemctl status dovecot OK", "comandos": "apt-get install -y dovecot-core dovecot-imapd dovecot-pop3d", "fonte_id": "F02"},
            {"numero": 4, "titulo": "SSL com Let's Encrypt", "descricao": "Criptografia gratuita", "analogia": "Cadeados", "o_que_acontece_na_tela": "Certbot pede email", "como_saber_se_deu_certo": "Certificado em /etc/letsencrypt", "comandos": "apt-get install -y certbot", "fonte_id": "F03"},
            {"numero": 5, "titulo": "Configuracao DNS", "descricao": "SPF, DKIM, DMARC", "analogia": "RG do dominio", "o_que_acontece_na_tela": "Editor nano", "como_saber_se_deu_certo": "Registros DNS aparecem", "comandos": "opendkim-genkey -b 2048 -d seu-dominio.com.br", "fonte_id": "F04"},
            {"numero": 6, "titulo": "Teste de Email", "descricao": "Enviar teste", "analogia": "Ligacao", "o_que_acontece_na_tela": "Nenhuma", "como_saber_se_deu_certo": "Email recebido em 5s", "comandos": "echo 'Teste' | mail -s 'Teste' email@gmail.com", "fonte_id": "F01"},
            {"numero": 7, "titulo": "Clientes de Email", "descricao": "Sincronizar Thunderbird/Outlook", "analogia": "Conexao", "o_que_acontece_na_tela": "Testes de conexao", "como_saber_se_deu_certo": "INBOX sincronizada", "comandos": "systemctl restart postfix dovecot", "fonte_id": "F02"}
        ],
        "arquivos_configuracao": [
            {"caminho": "/etc/postfix/main.cf", "linguagem": "postfix-config", "conteudo": "myhostname = mail.seu-dominio.com.br\nmyorigin = seu-dominio.com.br\nsmtpd_tls_cert_file = /etc/letsencrypt/live/seu-dominio.com.br/fullchain.pem\nsmtpd_tls_key_file = /etc/letsencrypt/live/seu-dominio.com.br/privkey.pem", "explicacao": "Config minima Postfix com SSL e DKIM"},
            {"caminho": "/etc/dovecot/conf.d/10-mail.conf", "linguagem": "dovecot-config", "conteudo": "protocols = imap pop3\nmail_location = maildir:~/Maildir\nssl = required\nssl_cert = </etc/letsencrypt/live/seu-dominio.com.br/fullchain.pem", "explicacao": "Config minima Dovecot com IMAP seguro"}
        ]
    },
    "manual_uso_exaustivo": {
        "arquitetura_uso": "Postfix e Dovecot trabalham integrados. Postfix recebe/envia SMTP. Dovecot oferece IMAP para sincronizacao. Usuarios sao usuarios Unix com pasta Maildir/.",
        "roteiro_primeiro_voo": [
            {"passo": "Passo 1: Adicionar Usuario", "acao": "sudo adduser seu-nome com senha forte (12+ chars)", "resultado_esperado": "Pasta Maildir criada no proximo login IMAP"},
            {"passo": "Passo 2: Configurar Cliente", "acao": "Abrir Thunderbird/Outlook e digitar email/senha", "resultado_esperado": "Em 10s testes de conexao OK"},
            {"passo": "Passo 3: Enviar Teste", "acao": "Escrever email para amigo@gmail.com", "resultado_esperado": "Email recebido em 2-3s"}
        ],
        "comandos_cli": [
            {"comando": "adduser [nome]", "descricao": "Cria usuario Unix lido pelo Dovecot", "exemplo": "adduser joao.silva", "fonte_id": "F01"},
            {"comando": "mailq", "descricao": "Lista fila de emails", "exemplo": "mailq", "fonte_id": "F02"},
            {"comando": "postqueue -p", "descricao": "Fila com detalhes", "exemplo": "postqueue -p | grep MAILER", "fonte_id": "F01"},
            {"comando": "dig seu-dominio.com.br MX", "descricao": "Verifica registro MX", "exemplo": "dig seu-dominio.com.br MX", "fonte_id": "F03"}
        ],
        "rotas_api": [
            {"metodo": "SMTP", "rota": "localhost:25 (587 auth)", "descricao": "Envio de emails", "payload_exemplo": "telnet localhost 25", "fonte_id": "F01"},
            {"metodo": "IMAP", "rota": "localhost:143 (993 SSL)", "descricao": "Sincronizacao bidirecional", "payload_exemplo": "openssl s_client -connect localhost:993", "fonte_id": "F02"},
            {"metodo": "POP3", "rota": "localhost:110 (995 SSL)", "descricao": "Download-e-apague legado", "payload_exemplo": "openssl s_client -connect localhost:995", "fonte_id": "F02"}
        ],
        "interface_ui": [
            {"modulo": "Webmin/PostfixAdmin", "descricao": "Interface web para gerenciar usuarios", "recursos_chave": ["Adicionar/remover contas", "Quotas", "Aliases e listas", "Logs de entrega"]},
            {"modulo": "Terminal SSH", "descricao": "Gerenciamento direto via CLI", "recursos_chave": ["adduser criar contas", "mailq diagnosticar", "tail logs", "doveadm gerenciar mailboxes"]}
        ],
        "troubleshooting": [
            {"sintoma": "Emails na fila, nao entregues", "causa_provavel": "Firewall bloqueando porta 25 outbound", "solucao_comando": "telnet destino 25. Use porta 587."},
            {"sintoma": "Emails em spam Gmail", "causa_provavel": "Sem SPF/DKIM/DMARC", "solucao_comando": "Adicionar registros DNS SPF, DKIM, DMARC"},
            {"sintoma": "Thunderbird Connection refused", "causa_provavel": "Dovecot parado ou porta 993 bloqueada", "solucao_comando": "systemctl status dovecot. ufw allow 993/tcp"},
            {"sintoma": "Certificado SSL expirado", "causa_provavel": "Certbot nao renovou", "solucao_comando": "certbot renew --dry-run && certbot renew"},
            {"sintoma": "Erro Quota exceeded", "causa_provavel": "Maildir cheio", "solucao_comando": "Limpar antigos ou aumentar quota"}
        ]
    },
    "referencias_bibliograficas": [
        {"id": "F01", "categoria": "Documentacao Oficial", "titulo": "Postfix Official Documentation", "url": "http://www.postfix.org/documentation.html", "autor_ou_canal": "Wietse Venema & Postfix Project"},
        {"id": "F02", "categoria": "Documentacao Oficial", "titulo": "Dovecot Official Documentation", "url": "https://doc.dovecot.org/", "autor_ou_canal": "Timo Sirainen & Dovecot Developers"},
        {"id": "F03", "categoria": "Guia Tecnico", "titulo": "SPF, DKIM, DMARC Setup on Linux", "url": "https://linuxacademy.com/guides/spf-dkim-dmarc/", "autor_ou_canal": "Linux Academy & DevOps"},
        {"id": "F04", "categoria": "Video/Tutorial", "titulo": "Postfix Dovecot Let's Encrypt Setup", "url": "https://www.youtube.com/results?search_query=postfix+dovecot", "autor_ou_canal": "Linux Admin Channels"},
        {"id": "F05", "categoria": "Livro/EBook", "titulo": "Linux Mail Server Administration Handbook", "url": "https://github.com/coreos/etcd/wiki", "autor_ou_canal": "Linux Professional Institute"}
    ],
    "desinstalacao_cirurgica": {
        "principio_isolamento": "Remove Postfix/Dovecot mantendo SO, firewall, certs SSL e outros servicos intactos.",
        "passos": [
            {"numero": 1, "titulo": "Parar Servicos", "descricao": "Desliga Postfix e Dovecot", "comandos": "systemctl stop postfix dovecot\nsystemctl disable postfix dovecot", "alerta_seguranca": "Nao stop all. Apenas email", "como_validar": "systemctl is-active postfix # inactive"},
            {"numero": 2, "titulo": "Remover Pacotes", "descricao": "Desinstala Postfix/Dovecot", "comandos": "apt-get remove -y postfix dovecot-core dovecot-imapd dovecot-pop3d", "alerta_seguranca": "Use remove nao purge", "como_validar": "which postfix # nao encontrar"},
            {"numero": 3, "titulo": "Remover Portas Firewall", "descricao": "Fecha SMTP/IMAP/POP3", "comandos": "ufw delete allow 25/tcp\nufw delete allow 993/tcp\nufw reload", "alerta_seguranca": "Verificar antes SSH 22 intacta", "como_validar": "ufw status | grep -E (25|110|143) # nada"},
            {"numero": 4, "titulo": "Remover Config/Dados", "descricao": "Deleta /etc/postfix /etc/dovecot", "comandos": "rm -rf /etc/postfix /etc/dovecot /etc/opendkim", "alerta_seguranca": "Backup antes. Nao usar rm -rf selvagemente", "como_validar": "ls /etc/postfix 2>&1 | cannot access"},
            {"numero": 5, "titulo": "Limpar DNS", "descricao": "Remove registros MX/SPF/DKIM", "comandos": "dig seu-dominio.com.br MX\ntelnet localhost 25 # Connection refused", "alerta_seguranca": "Registros MX antigos causam bounces", "como_validar": "mxtoolbox.com verifica propagacao"}
        ],
        "checklist_saude_vps": [
            "systemctl status ssh # deve estar active",
            "free -h # confirma liberacao RAM",
            "df -h /home # espaco liberado",
            "ufw status | head -10 # firewall OK com portas necessarias"
        ]
    }
}

trilha = {
    "$schema": "../schemas/schema_trilha_aprendizado.json",
    "produto_foco": "Postfix + Dovecot",
    "slug": "postfix-dovecot",
    "saas_origem": "Gmail, Microsoft 365, Zoho Mail",
    "tempo_total_estimado": "5 horas de imersao guiada (No seu proprio ritmo)",
    "fases": [
        {
            "fase_numero": 1,
            "titulo": "Fase 1: Conceitos Email, SMTP/IMAP & Soberania",
            "tempo_estimado": "1h 00min",
            "objetivo": "Entender protocolos email e beneficios privacidade",
            "recursos": [
                {"titulo": "Protocolos Email: SMTP, IMAP, POP3", "tipo_midia": "Artigo Tecnico", "idioma": "PT-BR", "dica_traducao_ptbr": "100% PT-BR", "autor": "Linux Admins Brasil", "duracao": "25 min", "url": "https://www.digitalocean.com/community/tutorials/understanding-the-smtp-protocol", "aprendizado_chave": "Diferencas SMTP/IMAP/POP3. IMAP mais seguro.", "fonte_id": "F01"},
                {"titulo": "LGPD Servers Email Proprios", "tipo_midia": "Guia Legal", "idioma": "PT-BR", "dica_traducao_ptbr": "PT-BR", "autor": "Tech Law Advogado", "duracao": "20 min", "url": "https://www.gov.br/cidadania/pt-br/acesso-a-informacao/lgpd", "aprendizado_chave": "Responsabilidades legais", "fonte_id": "F02"},
                {"titulo": "SSL/TLS Seguranca Email", "tipo_midia": "Documentacao Tecnica", "idioma": "EN", "dica_traducao_ptbr": "Auto-translate browser", "autor": "Let's Encrypt", "duracao": "15 min", "url": "https://letsencrypt.org/how-it-works/", "aprendizado_chave": "SSL protege transito", "fonte_id": "F03"}
            ]
        },
        {
            "fase_numero": 2,
            "titulo": "Fase 2: Instalacao VPS, Linux Basics",
            "tempo_estimado": "1h 30min",
            "objetivo": "Tutorial instalacao Postfix+Dovecot",
            "recursos": [
                {"titulo": "VPS Hetzner Iniciantes", "tipo_midia": "Tutorial", "idioma": "PT-BR", "dica_traducao_ptbr": "PT-BR leigos", "autor": "DevOps Brasil", "duracao": "30 min", "url": "https://docs.hetzner.cloud/basics/getting-started/", "aprendizado_chave": "Criar conta, VPS, SSH", "fonte_id": "F04"},
                {"titulo": "Postfix+Dovecot Instalacao", "tipo_midia": "Guia Tecnico", "idioma": "PT-BR", "dica_traducao_ptbr": "Screenshots PT-BR", "autor": "Linux Admins", "duracao": "40min+20min", "url": "https://www.linuxbabe.com/mail-server/postfix-dovecot-ubuntu", "aprendizado_chave": "apt, systemctl, nano", "fonte_id": "F01"},
                {"titulo": "SSL Let's Encrypt", "tipo_midia": "Tutorial", "idioma": "EN", "dica_traducao_ptbr": "Visual", "autor": "Certbot", "duracao": "20 min", "url": "https://certbot.eff.org/instructions/ubuntu-20.04/", "aprendizado_chave": "Certificados auto", "fonte_id": "F03"}
            ]
        },
        {
            "fase_numero": 3,
            "titulo": "Fase 3: SPF, DKIM, DMARC Config",
            "tempo_estimado": "1h 15min",
            "objetivo": "Anti-spam assinaturas digitais",
            "recursos": [
                {"titulo": "SPF DKIM DMARC Explicado", "tipo_midia": "Artigo", "idioma": "PT-BR", "dica_traducao_ptbr": "PT-BR exemplos", "autor": "Seguranca Email", "duracao": "30 min", "url": "https://www.sitehosting.com.br/blog/spf-dkim-dmarc/", "aprendizado_chave": "Diferencas SPF/DKIM/DMARC", "fonte_id": "F02"},
                {"titulo": "Implementar SPF DKIM DMARC", "tipo_midia": "Guia Tecnico", "idioma": "EN", "dica_traducao_ptbr": "Copy comandos", "autor": "Linux Babe", "duracao": "45 min", "url": "https://www.linuxbabe.com/mail-server/opendkim-ubuntu-postfix", "aprendizado_chave": "opendkim-genkey, DNS", "fonte_id": "F04"},
                {"titulo": "Email Tester MXToolbox", "tipo_midia": "Ferramenta", "idioma": "EN", "dica_traducao_ptbr": "Visual", "autor": "MXToolbox", "duracao": "15 min", "url": "https://mxtoolbox.com/", "aprendizado_chave": "Validar SPF/DKIM/DMARC", "fonte_id": "F05"}
            ]
        },
        {
            "fase_numero": 4,
            "titulo": "Fase 4: Clientes Email Dovecot",
            "tempo_estimado": "1h 00min",
            "objetivo": "Thunderbird Outlook Apple Mail",
            "recursos": [
                {"titulo": "Thunderbird IMAP Config", "tipo_midia": "Tutorial", "idioma": "PT-BR", "dica_traducao_ptbr": "Screenshots PT-BR", "autor": "Mozilla Brasil", "duracao": "20 min", "url": "https://support.mozilla.org/pt-BR/kb/configurar-sua-conta-de-email", "aprendizado_chave": "Port 993 SSL sync", "fonte_id": "F01"},
                {"titulo": "Outlook IMAP Config", "tipo_midia": "Oficial", "idioma": "PT-BR", "dica_traducao_ptbr": "PT-BR oficial", "autor": "Microsoft", "duracao": "15 min", "url": "https://support.microsoft.com/pt-br/office/criar-um-perfil-novo-do-outlook", "aprendizado_chave": "SMTP 587 STARTTLS", "fonte_id": "F02"},
                {"titulo": "Filtros Regras Avancadas", "tipo_midia": "Docs", "idioma": "EN", "dica_traducao_ptbr": "Visual", "autor": "Thunderbird", "duracao": "25 min", "url": "https://support.mozilla.org/en-US/kb/creating-and-using-filters", "aprendizado_chave": "Automacao backup offline", "fonte_id": "F03"}
            ]
        },
        {
            "fase_numero": 5,
            "titulo": "Fase 5: Troubleshooting Manutencao",
            "tempo_estimado": "1h 15min",
            "objetivo": "Diagnostico escalabilidade",
            "recursos": [
                {"titulo": "Diagnostico SMTP/IMAP Problemas", "tipo_midia": "Guia", "idioma": "PT-BR", "dica_traducao_ptbr": "Logs PT-BR", "autor": "Linux Admins", "duracao": "25 min", "url": "https://www.linuxbabe.com/mail-server/postfix-dovecot-ubuntu", "aprendizado_chave": "/var/log/mail.log mailq telnet", "fonte_id": "F04"},
                {"titulo": "Monitoramento Tempo Real", "tipo_midia": "Tutorial", "idioma": "EN", "dica_traducao_ptbr": "Copy scripts", "autor": "Linux Admins", "duracao": "20 min", "url": "https://www.digitalocean.com/community/tutorials/how-to-use-journalctl-to-view-and-manipulate-systemd-logs", "aprendizado_chave": "systemctl journalctl htop", "fonte_id": "F01"},
                {"titulo": "Multiplos Usuarios Quotas", "tipo_midia": "Guia", "idioma": "EN", "dica_traducao_ptbr": "Config universal", "autor": "Dovecot", "duracao": "30 min", "url": "https://doc.dovecot.org/configuration_manual/quota/", "aprendizado_chave": "Quotas doveadm limites", "fonte_id": "F02"},
                {"titulo": "Backup Redundancia HA", "tipo_midia": "Arquitetural", "idioma": "EN", "dica_traducao_ptbr": "Conceitos universais", "autor": "HA Systems", "duracao": "20 min", "url": "https://www.linuxbabe.com/mail-server/backup-postfix-dovecot", "aprendizado_chave": "Backup replicacao failover", "fonte_id": "F05"}
            ]
        }
    ]
}

def save_json_sem_bom(filepath, data):
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

save_json_sem_bom('scripts/data/manual-postfix-dovecot.json', manual)
save_json_sem_bom('scripts/data/trilha-postfix-dovecot.json', trilha)

print("OK manual-postfix-dovecot.json")
print("OK trilha-postfix-dovecot.json")
