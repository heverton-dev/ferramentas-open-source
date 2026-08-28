# Manual Operacional Completo: Mail-in-a-Box (Self-Hosted Email Server Solution)

> **Padrão Diamante · Guia de Engenharia & Adoção Descomplicada** 
> **Licença:** CC0-1.0 | **Versão:** 0.65 | **Setup Estimado:** 45 min (Conhecimento intermediario de Linux & DNS) 
> **VPS Recomendada:** Hetzner Cloud CX21 ou Linode 4GB (2 vCPU Dedicadas, 4 GB RAM, 80 GB SSD NVMe, Ubuntu 22.04 LTS ou 24.04 LTS) 
> **Custo Mensal Estimado:** EUR 6.00/mes

---

## Módulo 0: Nivelamento Conceitual (Analogias do Dia a Dia)

### Mail Server Self-Hosted *(Analogia: Sua Propria Agencia dos Correios)*
Mail-in-a-Box eh um servidor de email completo que roda na sua VPS. Em vez de confiar em Google ou Microsoft, voce hospeda tudo em sua propria maquina.

### IMAP/SMTP & Protocolos de Email *(Analogia: Carteiro que Entrega & Carteiro que Coleta)*
SMTP eh o protocolo de saida. IMAP eh o protocolo de entrada.

### DNS & Registros SPF/DKIM/DMARC *(Analogia: Cartorio que Autentica Sua Identidade)*
Registros digitais que provam que emails vieram de voce.

## Parte I: Instalação em Produção na VPS (Passo a Passo Rígido)

### Passo 1: Preparacao da VPS & Hardening `[F01]`
Configurar firewall e atualizacoes.

> **Entenda com uma analogia:** Limpar e proteger o canteiro de obra.

```bash
apt-get update && apt-get upgrade -y
ufw default deny incoming
ufw allow 22/tcp && ufw allow 25/tcp && ufw allow 143/tcp
```

- **O que você verá na tela:** Sistema atualizado com firewall ativo.
- **Como saber se deu certo:** ufw status mostra portas abertas.

### Passo 2: Execucao do Script de Instalacao `[F02]`
Mail-in-a-Box automatiza todo setup.

> **Entenda com uma analogia:** Chamar o especialista que monta tudo.

```bash
cd /root
curl -L https://mailinabox.email/setup.sh -o setup.sh
bash setup.sh
```

- **O que você verá na tela:** Script executa com credenciais admin geradas.
- **Como saber se deu certo:** URL de admin com senha.

### Passo 3: Configuracao de DNS `[F03]`
Apontar dominio para VPS.

> **Entenda com uma analogia:** Registrar seu dominio.

```bash
dig @8.8.8.8 seu-dominio.com +short
```

- **O que você verá na tela:** Registros DNS adicionados.
- **Como saber se deu certo:** dig retorna IP da VPS.

### Passo 4: Criacao de Usuarios `[F04]`
Adicionar contas de email.

> **Entenda com uma analogia:** Abrir novas caixas de correio.

```bash
# Via painel web admin: Mail > Users > Add User
```

- **O que você verá na tela:** Painel exibe usuarios.
- **Como saber se deu certo:** Usuario criado com sucesso.

### Passo 5: Teste de Envio & Recebimento `[F05]`
Validar funcionamento.

> **Entenda com uma analogia:** Teste de corrida.

```bash
# Enviar teste via webmail
```

- **O que você verá na tela:** Emails aparecem nos clientes.
- **Como saber se deu certo:** Email chega sem spam.

## Arquivos de Configuração de Produção

### `/etc/hostname`
*Hostname da maquina.*

```text
mail.seu-dominio.com
```

### `/root/.env`
*Variaveis de configuracao.*

```bash
ADMIN_EMAIL=admin@seu-dominio.com
```

## Parte II: Manual de Uso Exaustivo

**Arquitetura Operacional:** Stack completa: Postfix (SMTP), Dovecot (IMAP), OpenDKIM (DKIM signing), Spamassassin (antispam).

### Roteiro de Primeiro Voo (Sua Primeira Reunião em 3 Minutos)

1. **Passo 1: Acessar Admin:** Abra https://mail.seu-dominio.com/admin
 - **Resultado Esperado:** Login com credenciais admin.

1. **Passo 2: Verificar Saude:** Clique em System > Diagnostics
 - **Resultado Esperado:** Todos os servicos OK.

1. **Passo 3: Configurar Webmail:** Acesse https://mail.seu-dominio.com com usuario
 - **Resultado Esperado:** Webmail carrega com inbox vazio.

1. **Passo 4: Testar IMAP:** Configure Thunderbird
 - **Resultado Esperado:** Cliente conecta e sincroniza.

### Dicionário Completo de Comandos (CLI)

| Comando / Flag | Descrição Técnica | Exemplo de Execução | Fonte |
| :--- | :--- | :--- | :---: |
| `sudo systemctl status postfix` | Ver status SMTP. | `sudo systemctl status postfix` | `[F01]` |
| `sudo systemctl status dovecot` | Ver status IMAP. | `sudo systemctl status dovecot` | `[F02]` |
| `tail -f /var/log/mail.log` | Logs de email. | `tail -f /var/log/mail.log` | `[F03]` |

### Endpoints de API REST & Integração Agêntica

| Método | Rota | Descrição | Fonte |
| :---: | :--- | :--- | :---: |
| **GET** | `/admin/mail/users` | Listar usuarios. | `[F05]` |
| **POST** | `/admin/mail/users/add` | Adicionar usuario. | `[F06]` |
| **GET** | `/admin/diagnostics` | Diagnostico. | `[F07]` |

### Matriz de Resolução de Problemas (Troubleshooting)

- ** Sintoma:** Emails caem em spam
 - **Causa:** SPF/DKIM nao configurados.
- ** Sintoma:** Nao conecta IMAP
 - **Causa:** Porta bloqueada.
- ** Sintoma:** Disco cheio
 - **Causa:** Logs acumulando.
## Parte III: Desinstalação Cirúrgica & Isolamento da VPS (Zero Efeito Colateral)

> **Princípio de Isolamento:** Remove credenciais e DNS do Google.

### Passo 1: Backup Completo
Exportar emails e dados.

```bash
Use Google Takeout (https://takeout.google.com)
```

- **Alerta de Segurança:** Mantenha backup seguro.
- **Como Validar:** `Arquivo ZIP gerado.`

### Passo 2: Importar Emails
Restaurar em Mail-in-a-Box.

```bash
Via Thunderbird ou cliente IMAP
```

- **Alerta de Segurança:** Valide importacao.
- **Como Validar:** `Emails aparecem.`

### Passo 3: Mudar DNS
Remover Google, adicionar Mail-in-a-Box.

```bash
dig MX seu-dominio.com @8.8.8.8
```

- **Alerta de Segurança:** NAO remova sem validacao.
- **Como Validar:** `dig mostra mail.seu-dominio.com`

### Checklist de Saúde da VPS (Outros Projetos)

- [ ] `systemctl status postfix dovecot`
- [ ] `tail -30 /var/log/mail.log`
- [ ] `dig MX seu-dominio.com @8.8.8.8`
- [ ] `sudo df -h /var/mail`

## Parte IV: Referências Bibliográficas Auditadas

| ID | Categoria | Título da Obra | Autor / Mantenedor | Link Oficial |
| :---: | :--- | :--- | :--- | :--- |
| **F01** | Documentacao Oficial | Mail-in-a-Box Official Setup | Joshua Tate & Contributors | [https://mailinabox.email/](https://mailinabox.email/) |
| **F02** | Documentacao Oficial | Mail-in-a-Box GitHub Repository | Mail-in-a-Box Community | [https://github.com/mail-in-a-box/mailinabox](https://github.com/mail-in-a-box/mailinabox) |
| **F03** | Padroes Tecnicos | RFC 5321 - SMTP Protocol | IETF | [https://datatracker.ietf.org/doc/html/rfc5321](https://datatracker.ietf.org/doc/html/rfc5321) |
| **F04** | Padroes Tecnicos | RFC 3501 - IMAP4 Protocol | IETF | [https://datatracker.ietf.org/doc/html/rfc3501](https://datatracker.ietf.org/doc/html/rfc3501) |
| **F05** | Best Practices | SPF, DKIM & DMARC Best Practices | DMARC.org Community | [https://dmarc.org/](https://dmarc.org/) |
