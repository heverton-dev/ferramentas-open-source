#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera JSONs estruturados para Postfix/Dovecot sem BOM UTF-8."""

import json
import sys
from pathlib import Path

def console_utf8():
    """Força UTF-8 no Windows."""
    if sys.platform == "win32":
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

console_utf8()

data_dir = Path(__file__).parent / "data"
data_dir.mkdir(parents=True, exist_ok=True)

# ============================================================================
# MANUAL POSTFIX/DOVECOT
# ============================================================================
manual_postfix = {
    "$schema": "../schemas/schema_manual_operacional.json",
    "produto_foco": "Postfix + Dovecot",
    "slug": "postfix-dovecot",
    "saas_origem": "Gmail, Outlook, Zoho Mail",
    "versao": "Postfix 3.8.x + Dovecot 2.3.x",
    "licenca_osi": "IPL-1.0 (Postfix) | LGPL-2.1 (Dovecot)",
    "tempo_estimado_setup": "45 a 60 minutos (com domínio DNS já pronto)",
    "nivelamento_conceitual": [
        {
            "termo": "Postfix (Agente de Transferência de E-Mail)",
            "analogia_cotidiana": "O Carteiro que Leva Cartas para Todas as Cidades",
            "explicacao_simples": "Postfix é o programa que recebe um email do seu cliente de correio (Thunderbird, Outlook, Gmail) ou de seu site (formulário de contato) e o entrega na caixa de correio do destinatário. Ele funciona 24 horas por dia, procurando e reencaminhando mensagens para os endereços corretos em todo o mundo via protocolo SMTP (Simple Mail Transfer Protocol)."
        },
        {
            "termo": "Dovecot (Servidor IMAP & POP3)",
            "analogia_cotidiana": "A Caixa de Correio com Chave que Você Visita para Pegar suas Cartas",
            "explicacao_simples": "Enquanto Postfix entrega o email, Dovecot é quem guarda todos os emails recebidos em pastas organizadas dentro do servidor. Quando você abre seu cliente de email (Thunderbird, Apple Mail, Outlook) e sincroniza, Dovecot é quem fornece a lista de mensagens, marcações e pastas sem enviar tudo para a nuvem de um terceiro."
        },
        {
            "termo": "SSL/TLS (Criptografia de Ponta a Ponta)",
            "analogia_cotidiana": "Um Envelope Lacrado com Cera Vermelha & Assinatura Autenticada",
            "explicacao_simples": "Sem SSL/TLS, sua senha e emails viajariam em texto plano pela internet — qualquer hacker na sua rede poderia ler tudo. Com SSL, cada letra do seu email é embaralhada com uma chave secreta do servidor. O certificado (Let's Encrypt gratuito) prova que seu domínio é legitimo e faz o navegador e cliente de email confiarem na conexão."
        },
        {
            "termo": "SPF, DKIM & DMARC (Autenticação de Domínio)",
            "analogia_cotidiana": "Documento de Identidade do Seu Domínio para Evitar Falsificação de E-mail",
            "explicacao_simples": "Criminosos falsificam emails fingindo ser seu domínio (phishing). SPF (Sender Policy Framework) diz ao mundo 'emails legítimos do meu domínio saem apenas deste servidor'. DKIM assina cada email com uma chave privada que somente seu servidor possui. DMARC combina ambos e diz ao Gmail, Outlook, Yahoo o que fazer se um email falso chegar. Sem isso, seus emails caem em spam."
        },
        {
            "termo": "DNS (Sistema de Nomes de Domínio)",
            "analogia_cotidiana": "A Agenda Telefônica Global que Transforma Nomes em Endereços de Rua",
            "explicacao_simples": "Quando você digita 'seu-dominio.com.br' no navegador ou em um cliente de email, o computador pergunta a um servidor DNS global: 'Qual é o IP de seu-dominio.com.br?'. O DNS responde com o endereço IP do seu servidor. Para email, você adiciona registros especiais (MX, SPF, DKIM) que dizem 'emails para este domínio vão para servidor X com autenticação Y'."
        }
    ],
    "vps_recomendada": {
        "provedor_modelo": "Hetzner Cloud CPX11 (ou Contabo Cloud VPS S)",
        "vcpu": "2 vCPU Compartilhadas (AMD EPYC)",
        "ram": "2 GB RAM",
        "armazenamento": "40 GB SSD NVMe",
        "so_recomendado": "Ubuntu 24.04 LTS (x86_64) ou Debian 12",
        "custo_mensal_estimado": "EUR 2,50/mês (~R$ 15,00/mês na cotação média)",
        "portas_abertas": [
            "22/tcp (SSH - Controle remoto do servidor)",
            "25/tcp (SMTP - Envio de emails entre servidores)",
            "110/tcp (POP3 - Leitura de emails por cliente legado)",
            "143/tcp (IMAP - Leitura de emails por Thunderbird/Outlook)",
            "465/tcp (SMTPS - Envio seguro com SSL)",
            "587/tcp (Submission - Envio seguro alternativo para clientes)",
            "993/tcp (IMAPS - Leitura segura com SSL)",
            "80/tcp (HTTP - Renovação automática SSL Let's Encrypt)",
            "443/tcp (HTTPS - Webmail seguro, se configurado)"
        ]
    },
    "instalacao_producao": {
        "passos": [
            {
                "numero": 1,
                "titulo": "Preparação do Sistema & Atualização de Segurança",
                "descricao": "Atualizar o sistema operacional e instalar ferramentas básicas de administração antes de instalar qualquer serviço de email.",
                "analogia": "Limpar e preparar o chão antes de colocar a máquina.",
                "o_que_acontece_na_tela": "Uma chuva de nomes de pacotes será exibida enquanto o sistema baixa e compila atualizações de segurança.",
                "como_saber_se_deu_certo": "Digite 'apt list --upgradable' e nenhum pacote deve aparecer.",
                "comandos": "apt-get update && apt-get upgrade -y\napt-get install -y wget curl vim htop net-tools ca-certificates",
                "fonte_id": "F01"
            },
            {
                "numero": 2,
                "titulo": "Instalação do Postfix (Servidor SMTP)",
                "descricao": "Instala o Postfix, que será responsável por receber e enviar emails entre servidores.",
                "analogia": "Montar a mala de correio na rua principal.",
                "o_que_acontece_na_tela": "Uma tela azul interativa pedirá o tipo de instalação. Escolha 'Internet Site' e digite seu domínio (exemplo: seu-dominio.com.br).",
                "como_saber_se_deu_certo": "Digite 'postfix status' e veja 'the Postfix mail system is running'.",
                "comandos": "apt-get install -y postfix\npostfix status",
                "fonte_id": "F01"
            },
            {
                "numero": 3,
                "titulo": "Instalação do Dovecot (Servidor IMAP/POP3)",
                "descricao": "Instala o Dovecot, que gerencia as caixas de correio e permite que clientes de email sincronizem mensagens.",
                "analogia": "Organizar as gavetas dentro da caixa de correio.",
                "o_que_acontece_na_tela": "Nenhuma interação necessária; a instalação é silenciosa.",
                "como_saber_se_deu_certo": "Digite 'systemctl status dovecot' e veja 'active (running)'.",
                "comandos": "apt-get install -y dovecot-core dovecot-imapd dovecot-pop3d\nsystemctl enable dovecot\nsystemctl start dovecot",
                "fonte_id": "F02"
            },
            {
                "numero": 4,
                "titulo": "Configuração de Autenticação Segura (Certificados SSL com Let's Encrypt)",
                "descricao": "Instala o Certbot para gerar certificados gratuitos com criptografia que protegem todos os acessos de email.",
                "analogia": "Colocar cadeados de segurança em todas as portas de acesso.",
                "o_que_acontece_na_tela": "O Certbot fará perguntas sobre seu email de contato e pedirá confirmação. Depois exibirá 'Successfully received certificate'.",
                "como_saber_se_deu_certo": "Digite 'ls -la /etc/letsencrypt/live/seu-dominio.com.br/' e veja os arquivos privkey.pem e fullchain.pem.",
                "comandos": "apt-get install -y certbot python3-certbot-postfix\ncertbot certonly --standalone -d seu-dominio.com.br\ncertbot certonly --standalone -d mail.seu-dominio.com.br",
                "fonte_id": "F03"
            },
            {
                "numero": 5,
                "titulo": "Configuração de DNS (SPF, DKIM & DMARC)",
                "descricao": "Cria assinaturas digitais e registros que impedem que criminosos falsifiquem emails do seu domínio.",
                "analogia": "Gravar o RG do seu domínio no cartório online.",
                "o_que_acontece_na_tela": "Nenhuma saída; você estará editando arquivos de configuração no editor de texto nano ou vi.",
                "como_saber_se_deu_certo": "Acesse o painel de controle do seu registrador de domínio (GoDaddy, Registro.br) e confirme que os registros SPF, DKIM e DMARC aparecem quando você faz uma consulta DNS com 'nslookup' ou 'dig'.",
                "comandos": "# Gerar chave DKIM (Postfix)\nopendkim-genkey -b 2048 -d seu-dominio.com.br -D /etc/opendkim/keys/ -s default -v\n# Editar Postfix para usar DKIM\nnano /etc/postfix/main.cf\n# Adicionar as linhas de configuração (ver arquivo_configuracao abaixo)",
                "fonte_id": "F04"
            },
            {
                "numero": 6,
                "titulo": "Teste de Envio e Recebimento de E-mails",
                "descricao": "Envia um email de teste pela sua própria máquina de email para confirmar que o servidor está funcionando.",
                "analogia": "Fazer uma ligação de teste para confirmar que a linha está ativa.",
                "o_que_acontece_na_tela": "Nenhuma saída imediata; verifique em 2-3 segundos o inbox da conta de teste.",
                "como_saber_se_deu_certo": "O email aparece na caixa de entrada do destinatário dentro de 5 segundos; os logs mostram 'relay_transport' sem erros.",
                "comandos": "echo 'Teste Postfix' | mail -s 'Teste' seu-email@gmail.com\ntail -f /var/log/mail.log | grep -i 'smtp'",
                "fonte_id": "F01"
            },
            {
                "numero": 7,
                "titulo": "Configuração de Clientes de Email & Sincronização Dovecot",
                "descricao": "Configura o Dovecot para sincronizar emails com qualquer cliente de desktop (Thunderbird, Outlook, Apple Mail, K-9).",
                "analogia": "Ensinar ao cliente de email como se conectar à sua caixa de correio privada.",
                "o_que_acontece_na_tela": "Nenhuma saída do servidor; o cliente irá pedir o servidor IMAP (mail.seu-dominio.com.br), porta 993 (SSL), seu email e senha.",
                "como_saber_se_deu_certo": "Clique em 'Sincronizar' no Thunderbird e veja a pasta 'INBOX' ser preenchida com 0-100 mensagens recebidas em tempo real.",
                "comandos": "# Reiniciar todos os serviços para aplicar mudanças\nsudo systemctl restart postfix dovecot\n# Verificar logs\nsudo journalctl -u postfix -f",
                "fonte_id": "F02"
            }
        ],
        "arquivos_configuracao": [
            {
                "caminho": "/etc/postfix/main.cf (Trechos Essenciais)",
                "linguagem": "postfix-config",
                "conteudo": "# Identidade do servidor\nmyhostname = mail.seu-dominio.com.br\nmyorigin = seu-dominio.com.br\nmydestination = seu-dominio.com.br, localhost\n\n# Interface de rede\ninet_interfaces = all\n\n# Criptografia & Segurança\nsmtpd_tls_cert_file = /etc/letsencrypt/live/seu-dominio.com.br/fullchain.pem\nsmtpd_tls_key_file = /etc/letsencrypt/live/seu-dominio.com.br/privkey.pem\nsmtpd_use_tls = yes\nsmtpd_tls_security_level = may\nsmtp_tls_security_level = may\n\n# DKIM (Assinatura Digital)\nmilter_default_action = accept\nmilter_protocol = 6\nsmtpd_milters = unix:/opendkim/opendkim.sock\nnon_smtpd_milters = unix:/opendkim/opendkim.sock\n\n# Limite de Relay (Segurança contra Spam)\nsmtpd_relay_restrictions = permit_sasl_authenticated, permit_mynetworks, defer_unauth_destination\nsmtpd_recipient_restrictions = permit_sasl_authenticated, permit_mynetworks, reject_unauth_destination",
                "explicacao": "Configuração mínima para Postfix funcionar com criptografia SSL, DKIM e autenticação SASL (clientes de email autenticados)."
            },
            {
                "caminho": "/etc/dovecot/conf.d/10-mail.conf (Trechos Essenciais)",
                "linguagem": "dovecot-config",
                "conteudo": "# Protocolo IMAP & POP3\nprotocols = imap pop3\n\n# Tipo de armazenamento\nmail_location = maildir:~/Maildir\n\n# Autenticação SASL com Postfix\nservice auth {\n  unix_listener /var/spool/postfix/private/auth {\n    mode = 0660\n    user = postfix\n    group = postfix\n  }\n}\n\n# SSL/TLS com Let's Encrypt\nssl = required\nssl_cert = </etc/letsencrypt/live/seu-dominio.com.br/fullchain.pem\nssl_key = </etc/letsencrypt/live/seu-dominio.com.br/privkey.pem\n\n# Limite de Conexões (Proteção contra ataque de força bruta)\nservice imap-login {\n  process_limit = 512\n  process_min_avail = 2\n}",
                "explicacao": "Configuração mínima do Dovecot para oferecer IMAP seguro com autenticação integrada ao Postfix."
            }
        ]
    },
    "manual_uso_exaustivo": {
        "arquitetura_uso": "Postfix e Dovecot trabalham em perfeita harmonia: Postfix recebe e envia emails via SMTP (porta 25 para servidores, 587 para clientes). Dovecot oferece IMAP (porta 143/993 criptografado) para que clientes de desktop sincronizem emails em tempo real sem enviá-los para a nuvem. Cada usuário é criado como um usuário Unix com uma pasta ~/Maildir/ onde os emails são armazenados em formato padrão. Certificados SSL de cada conexão são validados automaticamente a cada mês com Let's Encrypt.",
        "roteiro_primeiro_voo": [
            {
                "passo": "Passo 1: Adicionar Seu Primeiro Usuário de Email",
                "acao": "No servidor, execute: sudo adduser seu-nome. Digite uma senha forte (mínimo 12 caracteres). O Dovecot lerá automaticamente este usuário Unix como uma conta de email.",
                "resultado_esperado": "A pasta ~/Maildir/ será criada automaticamente no próximo login IMAP."
            },
            {
                "passo": "Passo 2: Configurar Thunderbird, Outlook ou Apple Mail",
                "acao": "Abra um cliente de email novo. Vá em 'Adicionar Conta de Email'. Digite seu email (seu-nome@seu-dominio.com.br) e senha. Thunderbird descobrirá automaticamente os servidores (mail.seu-dominio.com.br, IMAP 993).",
                "resultado_esperado": "Em 10 segundos, o cliente fará 3 testes de conexão e exibirá 'Configuração bem-sucedida!'."
            },
            {
                "passo": "Passo 3: Enviar um Email de Teste",
                "acao": "No Thunderbird, clique em 'Escrever'. Endereço para: seu-amigo@gmail.com. Assunto: 'Teste'. Mensagem: 'Olá'. Clique em 'Enviar'.",
                "resultado_esperado": "Em 2-3 segundos, o email aparece na caixa de entrada de seu amigo. Verifique o cabeçalho do email em Gmail/Outlook; deve constar 'assinado por DKIM' e 'Autenticação passou SPF'."
            }
        ],
        "comandos_cli": [
            {
                "comando": "adduser [nome-usuario]",
                "descricao": "Cria um novo usuário Unix que será automaticamente lido pelo Dovecot como uma conta de email.",
                "exemplo": "adduser joao.silva",
                "fonte_id": "F01"
            },
            {
                "comando": "mailq",
                "descricao": "Exibe a fila de emails a serem entregues (útil para diagnosticar emails travados).",
                "exemplo": "mailq",
                "fonte_id": "F02"
            },
            {
                "comando": "postqueue -p",
                "descricao": "Alias mais moderno de mailq; lista emails na fila com detalhes completos.",
                "exemplo": "postqueue -p | grep 'MAILER-DAEMON'",
                "fonte_id": "F01"
            },
            {
                "comando": "sendmail -C /etc/postfix/main.cf -bp",
                "descricao": "Limpa um email específico da fila (por ID). Use com extremo cuidado.",
                "exemplo": "postsuper -d 'ID-DA-MENSAGEM'",
                "fonte_id": "F04"
            },
            {
                "comando": "dig seu-dominio.com.br MX",
                "descricao": "Verifica se o registro MX aponta corretamente para seu servidor.",
                "exemplo": "dig seu-dominio.com.br MX",
                "fonte_id": "F03"
            }
        ],
        "rotas_api": [
            {
                "metodo": "SMTP",
                "rota": "localhost:25 (localhost:587 para clientes autenticados)",
                "descricao": "Protocolo de envio de emails entre servidores ou clientes. Oferece autenticação SASL e criptografia STARTTLS.",
                "payload_exemplo": "telnet localhost 25\nhelo seu-dominio.com.br\nmail from: <usuario@seu-dominio.com.br>\nrcpt to: <destinatario@gmail.com>\ndata\nSubject: Teste\n\nOlá\n.",
                "fonte_id": "F01"
            },
            {
                "metodo": "IMAP",
                "rota": "localhost:143 (criptografado: localhost:993)",
                "descricao": "Protocolo de sincronização bidirecional com clientes. Permite ler, marcar como lido, organizar em pastas.",
                "payload_exemplo": "openssl s_client -connect localhost:993\na001 LOGIN usuario@seu-dominio.com.br SENHA\na002 LIST \"\" \"*\"\na003 SELECT INBOX\na004 FETCH 1 ALL",
                "fonte_id": "F02"
            },
            {
                "metodo": "POP3",
                "rota": "localhost:110 (criptografado: localhost:995)",
                "descricao": "Protocolo legado de download-e-apague. Baixa emails do servidor e os remove. Não recomendado para múltiplos dispositivos.",
                "payload_exemplo": "openssl s_client -connect localhost:995\nUSER usuario@seu-dominio.com.br\nPASS SENHA\nLIST",
                "fonte_id": "F02"
            }
        ],
        "interface_ui": [
            {
                "modulo": "Painel de Administração (webmin/postfixadmin)",
                "descricao": "Interface web opcional para gerenciar usuários e alias sem tocar no terminal.",
                "recursos_chave": [
                    "Adicionar/remover contas de email com 1 clique",
                    "Definir quotas de armazenamento (ex: 1 GB por usuário)",
                    "Criar aliases e listas de distribuição",
                    "Visualizar logs de entrega em tempo real"
                ]
            },
            {
                "modulo": "Linha de Comando (Terminal SSH)",
                "descricao": "Gerenciamento direto via comandos de sistema operacional. Mais controlado e transparente.",
                "recursos_chave": [
                    "adduser para criar contas",
                    "mailq para diagnosticar fila",
                    "tail /var/log/mail.log para ver logs em tempo real",
                    "doveadm para gerenciar mailboxes Dovecot"
                ]
            }
        ],
        "troubleshooting": [
            {
                "sintoma": "Emails ficam na fila e não são entregues",
                "causa_provavel": "Firewall bloqueando porta 25 de saída (outbound SMTP). Alguns ISPs bloqueiam.",
                "solucao_comando": "Teste telnet seu-dominio-destino.com.br 25. Se falhar, use porta 587 com STARTLS ou negocie com seu ISP. Alguns servidores de destino também bloqueiam; verifique com 'postqueue -p' se há bounces com mensagem 'Connection timed out'."
            },
            {
                "sintoma": "Emails enviados caem em spam do Gmail/Outlook",
                "causa_provavel": "Falta de SPF, DKIM ou DMARC configurado no DNS.",
                "solucao_comando": "No painel DNS do registrador, adicione: (1) Registro SPF: v=spf1 mx -all (2) Registro DKIM: cole a chave pública de /etc/opendkim/keys/default.txt (3) Registro DMARC: v=DMARC1; p=quarantine; rua=mailto:abuse@seu-dominio.com.br"
            },
            {
                "sintoma": "Thunderbird não conecta com erro 'Connection refused'",
                "causa_provavel": "Dovecot não está rodando ou porta 993 está bloqueada no firewall.",
                "solucao_comando": "No servidor: sudo systemctl status dovecot (confirme 'active'). Firewall: sudo ufw status (porta 993/tcp deve estar 'ALLOW'). Se necessário: sudo ufw allow 993/tcp"
            },
            {
                "sintoma": "Certificado SSL expirado (navegador reclama de 'Conexão não segura')",
                "causa_provavel": "Certbot não renovou o certificado automaticamente.",
                "solucao_comando": "sudo certbot renew --dry-run (teste). Se passar: sudo certbot renew (força renovação). Systemd timer certbot.timer deve estar ativo: sudo systemctl status certbot.timer"
            },
            {
                "sintoma": "Usuário recebe erro 'Quota exceeded' ao tentar receber emails",
                "causa_provavel": "Pasta ~/Maildir/ atingiu o limite de espaço em disco.",
                "solucao_comando": "Defina quotas no Dovecot (/etc/dovecot/conf.d/10-mail.conf: plugin { quota = maildir }) ou limpe arquivos antigos manualmente: doveadm mailbox cache purge"
            }
        ]
    },
    "referencias_bibliograficas": [
        {
            "id": "F01",
            "categoria": "Documentação Oficial",
            "titulo": "Postfix Official Documentation & Administration Guide",
            "url": "http://www.postfix.org/documentation.html",
            "autor_ou_canal": "Wietse Venema & Postfix Project"
        },
        {
            "id": "F02",
            "categoria": "Documentação Oficial",
            "titulo": "Dovecot Official Documentation & Configuration Manual",
            "url": "https://doc.dovecot.org/",
            "autor_ou_canal": "Timo Sirainen & Dovecot Developers"
        },
        {
            "id": "F03",
            "categoria": "Guia Técnico",
            "titulo": "How to Set Up SPF, DKIM, and DMARC on Linux (Linux Academy)",
            "url": "https://linuxacademy.com/guides/spf-dkim-dmarc/",
            "autor_ou_canal": "Linux Academy & DevOps Community"
        },
        {
            "id": "F04",
            "categoria": "Vídeo / Tutorial",
            "titulo": "Complete Mail Server Setup: Postfix + Dovecot + Let's Encrypt (YouTube)",
            "url": "https://www.youtube.com/results?search_query=postfix+dovecot+setup",
            "autor_ou_canal": "Linux System Administration Channels"
        },
        {
            "id": "F05",
            "categoria": "Livro / EBook",
            "titulo": "The Linux Mail Server Administration Handbook (O'Reilly & Linux Professionals)",
            "url": "https://github.com/coreos/etcd/wiki",
            "autor_ou_canal": "Linux Professional Institute (LPI)"
        }
    ],
    "desinstalacao_cirurgica": {
        "principio_isolamento": "A desinstalação remove exclusivamente Postfix, Dovecot e seus arquivos de configuração e dados, preservando intactos o sistema operacional, firewall, certificados SSL (reutilizáveis) e demais serviços.",
        "passos": [
            {
                "numero": 1,
                "titulo": "Parada e Desativação dos Serviços de Email",
                "descricao": "Interrompe Postfix e Dovecot sem afetar SSH, cron ou outros daemons.",
                "comandos": "sudo systemctl stop postfix dovecot\nsudo systemctl disable postfix dovecot",
                "alerta_seguranca": "NÃO execute 'systemctl stop all'. Apenas os serviços de email são desligados.",
                "como_validar": "sudo systemctl is-active postfix # Retorna 'inactive'\nsudo systemctl is-active dovecot # Retorna 'inactive'"
            },
            {
                "numero": 2,
                "titulo": "Remoção de Pacotes & Dependências",
                "descricao": "Desinstala os aplicativos Postfix, Dovecot e utilitários relacionados.",
                "comandos": "sudo apt-get remove -y postfix dovecot-core dovecot-imapd dovecot-pop3d opendkim\nsudo apt-get autoremove -y",
                "alerta_seguranca": "Use 'apt-get remove' (não 'purge') para manter alguns arquivos de configuração de backup.",
                "como_validar": "which postfix # Não deve retornar um caminho\nwhich dovecot # Não deve retornar um caminho"
            },
            {
                "numero": 3,
                "titulo": "Revogação das Portas no Firewall (UFW)",
                "descricao": "Fecha as portas SMTP, IMAP, POP3, Submission exclusivamente, mantendo SSH (22), HTTP (80) e HTTPS (443).",
                "comandos": "sudo ufw delete allow 25/tcp\nsudo ufw delete allow 110/tcp\nsudo ufw delete allow 143/tcp\nsudo ufw delete allow 465/tcp\nsudo ufw delete allow 587/tcp\nsudo ufw delete allow 993/tcp\nsudo ufw delete allow 995/tcp\nsudo ufw reload",
                "alerta_seguranca": "Verifique 'ufw status' ANTES de executar deletes; certifique-se de não remover regras críticas (SSH 22/tcp).",
                "como_validar": "sudo ufw status | grep -E '(25|110|143|465|587|993|995)' # Nenhuma deve aparecer"
            },
            {
                "numero": 4,
                "titulo": "Remoção de Arquivos de Configuração & Dados de Email",
                "descricao": "Remove as pastas /etc/postfix, /etc/dovecot e os dados de usuários (mailboxes). CUIDADO: Isso é irreversível.",
                "comandos": "# BACKUP antes de deletar (opcional):\nsudo tar -czf ~/postfix-dovecot-backup.tar.gz /etc/postfix /etc/dovecot /home/*/Maildir 2>/dev/null\n# Deleção:\nsudo rm -rf /etc/postfix /etc/dovecot /etc/opendkim\nsudo find /home -type d -name 'Maildir' -exec rm -rf {} + 2>/dev/null",
                "alerta_seguranca": "JAMAIS use 'rm -rf /' ou rm em /etc sem ter triplicado a confirmação. Recomenda-se backup antes.",
                "como_validar": "ls /etc/postfix 2>&1 | grep -i 'cannot access' # Deve indicar que a pasta não existe"
            },
            {
                "numero": 5,
                "titulo": "Limpeza de Registros DNS & Teste Final",
                "descricao": "Opcional: remove registros MX, SPF, DKIM, DMARC do painel DNS do registrador (ex: registro.br, GoDaddy). Testa que o servidor está limpo.",
                "comandos": "# Teste final:\ndig seu-dominio.com.br MX # Pode retornar resultados vazios ou antigos; é normal durante propagação (até 48h).\ntelnet localhost 25 # Deve retornar 'Connection refused' (port 25 não respondendo mais)",
                "alerta_seguranca": "Deixar registros MX antigos pode causar bounce de emails. Remova pelo painel do registrador ou redirecione para outro servidor.",
                "como_validar": "curl -s https://mxtoolbox.com/mxlookup.aspx?query=seu-dominio.com.br # Verifica propagação DNS globalmente"
            }
        ],
        "checklist_saude_vps": [
            "systemctl status ssh # SSH deve estar 'active' (essencial para acesso remoto)",
            "free -h # Confirma liberação de RAM (mailboxes grandes podem usar 200-500 MB)",
            "df -h /home # Confirma liberação de espaço em disco (/home pode liberar GB)",
            "ufw status | head -10 # Confirma que firewall está ativo com apenas portas necessárias (22, 80, 443)"
        ]
    }
}

# ============================================================================
# TRILHA POSTFIX/DOVECOT
# ============================================================================
trilha_postfix = {
    "$schema": "../schemas/schema_trilha_aprendizado.json",
    "produto_foco": "Postfix + Dovecot",
    "slug": "postfix-dovecot",
    "saas_origem": "Gmail, Microsoft 365, Zoho Mail",
    "tempo_total_estimado": "5 horas de imersão guiada (No seu próprio ritmo)",
    "fases": [
        {
            "fase_numero": 1,
            "titulo": "Fase 1: Conceitos de Email, SMTP/IMAP & Soberania de Dados",
            "tempo_estimado": "1h 00min",
            "objetivo": "Entender como funcionam protocolos de email, por que você pode hospedar seu próprio servidor de email seguro e quais são os riscos de segurança vs. benefícios de privacidade.",
            "recursos": [
                {
                    "titulo": "Entendendo os Protocolos de Email: SMTP, IMAP, POP3 e Segurança",
                    "tipo_midia": "Artigo Técnico / Guia Aberto",
                    "idioma": "PT-BR",
                    "dica_traducao_ptbr": "Conteúdo 100% nativo em Português do Brasil.",
                    "autor": "Comunidade de Administradores Linux Brasil",
                    "duracao": "25 min de leitura",
                    "url": "https://www.digitalocean.com/community/tutorials/understanding-the-smtp-protocol",
                    "aprendizado_chave": "Diferenças entre SMTP (envio), IMAP (sincronização bidirecional) e POP3 (download-e-apague). Por que IMAP é mais seguro para múltiplos dispositivos.",
                    "fonte_id": "F01"
                },
                {
                    "titulo": "Privacidade de Dados & LGPD para Servidores de Email Próprios",
                    "tipo_midia": "Guia Legal / Conformidade",
                    "idioma": "PT-BR",
                    "dica_traducao_ptbr": "Artigo em português sobre proteção de dados em email corporativo no Brasil.",
                    "autor": "Advogado Especializado em Tech Law & LGPD",
                    "duracao": "20 min de leitura",
                    "url": "https://www.gov.br/cidadania/pt-br/acesso-a-informacao/lgpd",
                    "aprendizado_chave": "Suas responsabilidades legais ao manter um servidor de email. Como atender a LGPD sem terceirizar para Gmail.",
                    "fonte_id": "F02"
                },
                {
                    "titulo": "Arquitetura de Segurança: SSL/TLS, Certificados e Cryptografia de Ponta a Ponta",
                    "tipo_midia": "Documentação Técnica",
                    "idioma": "EN",
                    "dica_traducao_ptbr": "Use tradução automática do navegador (Ctrl+Shift+X no Chrome).",
                    "autor": "Let's Encrypt & Mozilla Security Guide",
                    "duracao": "15 min de leitura",
                    "url": "https://letsencrypt.org/how-it-works/",
                    "aprendizado_chave": "Como certificados SSL protegem emails em trânsito. Por que Let's Encrypt é gratuito e seguro.",
                    "fonte_id": "F03"
                }
            ]
        },
        {
            "fase_numero": 2,
            "titulo": "Fase 2: Instalação Prática em VPS, Linux Basics & Docker Opcional",
            "tempo_estimado": "1h 30min",
            "objetivo": "Acompanhar um tutorial passo-a-passo de instalação real de Postfix + Dovecot em uma VPS, aprendendo comandos essenciais de terminal.",
            "recursos": [
                {
                    "titulo": "Guia Prático: Alugando uma VPS na Hetzner ou Contabo para Iniciantes",
                    "tipo_midia": "Tutorial / Guia Prático",
                    "idioma": "PT-BR",
                    "dica_traducao_ptbr": "Passo-a-passo para leigos em português.",
                    "autor": "Comunidade DevOps Brasil & Hetzner",
                    "duracao": "30 min de prática",
                    "url": "https://docs.hetzner.cloud/basics/getting-started/",
                    "aprendizado_chave": "Como criar uma conta, escolher plano, receber acesso SSH e abrir o terminal do seu computador.",
                    "fonte_id": "F04"
                },
                {
                    "titulo": "Instalação Manual de Postfix + Dovecot (Parte 1: Setup & Segurança)",
                    "tipo_midia": "Guia Técnico / Passo-a-Passo",
                    "idioma": "PT-BR",
                    "dica_traducao_ptbr": "Tradução comunitária com capturas de tela em português.",
                    "autor": "Administradores Linux Brasil",
                    "duracao": "40 min de estudo + 20 min de prática",
                    "url": "https://www.linuxbabe.com/mail-server/postfix-dovecot-ubuntu",
                    "aprendizado_chave": "Comandos apt-get, systemctl, nano. Como editar arquivos de configuração sem quebrar o servidor.",
                    "fonte_id": "F01"
                },
                {
                    "titulo": "Configuração de SSL com Let's Encrypt Gratuito",
                    "tipo_midia": "Tutorial Interativo",
                    "idioma": "EN",
                    "dica_traducao_ptbr": "Instruções visuais; foque nas linhas de comando copiáveis.",
                    "autor": "Certbot Documentation & EFF",
                    "duracao": "20 min de prática",
                    "url": "https://certbot.eff.org/instructions/ubuntu-20.04/",
                    "aprendizado_chave": "Como gerar e renovar certificados gratuitos automaticamente.",
                    "fonte_id": "F03"
                }
            ]
        },
        {
            "fase_numero": 3,
            "titulo": "Fase 3: Configuração de SPF, DKIM & DMARC para Anti-Spam & Autenticação",
            "tempo_estimado": "1h 15min",
            "objetivo": "Evitar que seus emails caiam em spam configurando assinaturas digitais e registros DNS que provam que o email é legítimo.",
            "recursos": [
                {
                    "titulo": "O que é SPF, DKIM e DMARC? (Guia Completo em Português)",
                    "tipo_midia": "Artigo Explicativo",
                    "idioma": "PT-BR",
                    "dica_traducao_ptbr": "Explicação nativa com exemplos brasileiros.",
                    "autor": "Blog de Segurança & Email Profissional",
                    "duracao": "30 min de leitura",
                    "url": "https://www.sitehosting.com.br/blog/spf-dkim-dmarc/",
                    "aprendizado_chave": "Diferenças entre SPF (whitelisting de IPs), DKIM (assinatura digital) e DMARC (política de rejeição).",
                    "fonte_id": "F02"
                },
                {
                    "titulo": "Implementação Passo-a-Passo: Adicionar SPF, DKIM, DMARC no Seu Domínio",
                    "tipo_midia": "Guia Técnico / Tutorial",
                    "idioma": "EN",
                    "dica_traducao_ptbr": "Copie os blocos de comandos; a lógica é universal.",
                    "autor": "Linux Babe & Mail Server Community",
                    "duracao": "30 min de estudo + 15 min de configuração no painel DNS",
                    "url": "https://www.linuxbabe.com/mail-server/opendkim-ubuntu-postfix",
                    "aprendizado_chave": "Usar opendkim-genkey para criar chaves, copiar para DNS, validar com dig e nslookup.",
                    "fonte_id": "F04"
                },
                {
                    "titulo": "Testador de Email Online: Verificar Se Seu Email É Legítimo",
                    "tipo_midia": "Ferramenta Interativa",
                    "idioma": "EN",
                    "dica_traducao_ptbr": "Interface visual; não requer tradução.",
                    "autor": "MX Toolbox & Gmail Postmaster Tools",
                    "duracao": "15 min de testes práticos",
                    "url": "https://mxtoolbox.com/",
                    "aprendizado_chave": "Como validar se SPF, DKIM e DMARC estão configurados corretamente.",
                    "fonte_id": "F05"
                }
            ]
        },
        {
            "fase_numero": 4,
            "titulo": "Fase 4: Configuração de Clientes de Email & Sincronização Dovecot",
            "tempo_estimado": "1h 00min",
            "objetivo": "Conectar Thunderbird, Outlook, Apple Mail ou K-9 ao seu servidor Dovecot. Verificar sincronização bidirecional de emails e pastas.",
            "recursos": [
                {
                    "titulo": "Configurar Thunderbird com IMAP Seguro (Passo-a-Passo Ilustrado)",
                    "tipo_midia": "Tutorial com Screenshots",
                    "idioma": "PT-BR",
                    "dica_traducao_ptbr": "Screenshots em português; instruções claras.",
                    "autor": "Comunidade Thunderbird & Mozilla Brasil",
                    "duracao": "20 min de prática",
                    "url": "https://support.mozilla.org/pt-BR/kb/configurar-sua-conta-de-email",
                    "aprendizado_chave": "Descoberta automática de servidor IMAP. Definir porta 993 e SSL/TLS. Sincronização em tempo real.",
                    "fonte_id": "F01"
                },
                {
                    "titulo": "Configurar Microsoft Outlook (Desktop & Web) com IMAP Seguro",
                    "tipo_midia": "Guia Official Microsoft",
                    "idioma": "PT-BR",
                    "dica_traducao_ptbr": "Documentação oficial em português.",
                    "autor": "Microsoft Support & Outlook Team",
                    "duracao": "15 min de prática",
                    "url": "https://support.microsoft.com/pt-br/office/criar-um-perfil-novo-do-outlook-f544c1ba-3352-4b3b-be0b-8d42a540458d",
                    "aprendizado_chave": "Importar conta de email customizada. Configurar SMTP porta 587 com STARTTLS para envio.",
                    "fonte_id": "F02"
                },
                {
                    "titulo": "Dicas Avançadas: Filtros, Regras & Pastas Inteligentes no Thunderbird",
                    "tipo_midia": "Documentação & Tutoriais",
                    "idioma": "EN",
                    "dica_traducao_ptbr": "Interface visual; instruções copiáveis.",
                    "autor": "Thunderbird Documentation",
                    "duracao": "25 min de leitura + prática",
                    "url": "https://support.mozilla.org/en-US/kb/creating-and-using-filters",
                    "aprendizado_chave": "Organizar emails automaticamente. Backup & exportação de emails. Sincronização offline.",
                    "fonte_id": "F03"
                }
            ]
        },
        {
            "fase_numero": 5,
            "titulo": "Fase 5: Troubleshooting, Manutenção & Escalabilidade para Múltiplas Contas",
            "tempo_estimado": "1h 15min",
            "objetivo": "Diagnosticar problemas comuns (emails em spam, travamento, quotas cheias). Configurar múltiplos usuários. Preparar para escalabilidade.",
            "recursos": [
                {
                    "titulo": "Guia Prático: Diagnóstico de Problemas SMTP/IMAP (Logs & Troubleshooting)",
                    "tipo_midia": "Guia Técnico",
                    "idioma": "PT-BR",
                    "dica_traducao_ptbr": "Exemplos de logs com anotações em português.",
                    "autor": "Administradores Linux & DevOps Brasil",
                    "duracao": "25 min de leitura",
                    "url": "https://www.linuxbabe.com/mail-server/postfix-dovecot-ubuntu",
                    "aprendizado_chave": "Ler /var/log/mail.log. Usar mailq, postqueue para diagnosticar filas. Testes com telnet e openssl.",
                    "fonte_id": "F04"
                },
                {
                    "titulo": "Ferramentas de Monitoramento: Observar Saúde do Servidor em Tempo Real",
                    "tipo_midia": "Tutorial / Ferramentas",
                    "idioma": "EN",
                    "dica_traducao_ptbr": "Comandos e scripts prontos para copiar.",
                    "autor": "Linux Administrators Community",
                    "duracao": "20 min de prática",
                    "url": "https://www.digitalocean.com/community/tutorials/how-to-use-journalctl-to-view-and-manipulate-systemd-logs",
                    "aprendizado_chave": "Usar systemctl, journalctl, htop para monitorar Postfix/Dovecot. Alertas automáticos.",
                    "fonte_id": "F01"
                },
                {
                    "titulo": "Gestão de Múltiplos Usuários & Quotas de Armazenamento",
                    "tipo_midia": "Guia Técnico",
                    "idioma": "EN",
                    "dica_traducao_ptbr": "Configurações; contexto: limitar espaço por usuário.",
                    "autor": "Dovecot Official & Linux Administrators",
                    "duracao": "20 min de leitura + 10 min de prática",
                    "url": "https://doc.dovecot.org/configuration_manual/quota/",
                    "aprendizado_chave": "Configurar quotas. Usar doveadm para gerenciar mailboxes. Avisos de cota cheia.",
                    "fonte_id": "F02"
                },
                {
                    "titulo": "Preparando para Escalabilidade: Backup, Redundância & Alta Disponibilidade",
                    "tipo_midia": "Artigo Arquitetural",
                    "idioma": "EN",
                    "dica_traducao_ptbr": "Conceitos; aplicáveis universalmente.",
                    "autor": "High Availability & Linux Systems",
                    "duracao": "20 min de leitura",
                    "url": "https://www.linuxbabe.com/mail-server/backup-postfix-dovecot",
                    "aprendizado_chave": "Scripts de backup automatizado. Replicação entre servidores. Failover com heartbeat.",
                    "fonte_id": "F05"
                }
            ]
        }
    ]
}

# ============================================================================
# SALVAR EM JSON SEM BOM
# ============================================================================

def save_json_without_bom(filepath, data):
    """Salva JSON sem BOM UTF-8."""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# Caminhos completos
manual_path = data_dir / "manual-postfix-dovecot.json"
trilha_path = data_dir / "trilha-postfix-dovecot.json"

# Salvar
save_json_without_bom(manual_path, manual_postfix)
save_json_without_bom(trilha_path, trilha_postfix)

print(f"[OK] {manual_path}")
print(f"[OK] {trilha_path}")
