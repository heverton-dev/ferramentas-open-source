# Manual Operacional Completo: Mail-in-a-Box

> **Padrão Diamante · Guia de Engenharia & Adoção Descomplicada** 
> **Licença:** CC0-1.0 | **Versão:** v0.65 | **Setup Estimado:** 2 a 3 horas 
> **VPS Recomendada:** Hetzner Cloud CX11 (1 vCPU, 2 GB, 40 GB, Ubuntu 22.04 LTS) 
> **Custo Mensal Estimado:** EUR 4/mes

---

## Módulo 0: Nivelamento Conceitual (Analogias do Dia a Dia)

### Mail-in-a-Box *(Analogia: Sua Propria Central de Correios)*
Servidor de email completo com SMTP, IMAP, Webmail e backup automatico.

### VPS *(Analogia: Sala Comercial na Nuvem)*
Um servidor que roda 24/7 para receber emails.

### SMTP e IMAP *(Analogia: Carteiro de Saida e Carteiro de Entrada)*
SMTP envia, IMAP recebe.

## Parte I: Instalação em Produção na VPS (Passo a Passo Rígido)

### Passo 1: Preparacao VPS `[F01]`
Conectar e atualizar

> **Entenda com uma analogia:** Preparar sala

```bash
ssh root@IP
apt-get update && upgrade
```

- **O que você verá na tela:** Atualizacoes
- **Como saber se deu certo:** hostname OK

### Passo 2: Instalar Mail-in-a-Box `[F02]`
Script oficial

> **Entenda com uma analogia:** Chamar tecnicos

```bash
curl -fsSLo setup.sh https://mailinabox.email/setup.sh
bash setup.sh
```

- **O que você verá na tela:** Perguntas interativas
- **Como saber se deu certo:** Setup complete

## Arquivos de Configuração de Produção

## Parte II: Manual de Uso Exaustivo

**Arquitetura Operacional:** Postfix + Dovecot + Nginx + SpamAssassin

### Roteiro de Primeiro Voo (Sua Primeira Reunião em 3 Minutos)

1. **Acessar Painel:** https://mail.seu-dominio.com/admin
 - **Resultado Esperado:** Dashboard carregado

### Dicionário Completo de Comandos (CLI)

| Comando / Flag | Descrição Técnica | Exemplo de Execução | Fonte |
| :--- | :--- | :--- | :---: |
| `systemctl status postfix` | Verifica status | `systemctl status postfix dovecot` | `[F01]` |

### Endpoints de API REST & Integração Agêntica

| Método | Rota | Descrição | Fonte |
| :---: | :--- | :--- | :---: |

### Matriz de Resolução de Problemas (Troubleshooting)

- ** Sintoma:** Email em spam
 - **Causa:** DNS incorreto
## Parte III: Desinstalação Cirúrgica & Isolamento da VPS (Zero Efeito Colateral)

> **Princípio de Isolamento:** Remover apenas Mail-in-a-Box

### Passo 1: Backup
Exportar emails

```bash
tar -czf backup.tar.gz /home/mail
```

- **Alerta de Segurança:** Nao delete ate confirmar
- **Como Validar:** `tar -tzf backup.tar.gz | wc -l`

### Checklist de Saúde da VPS (Outros Projetos)


## Parte IV: Referências Bibliográficas Auditadas

| ID | Categoria | Título da Obra | Autor / Mantenedor | Link Oficial |
| :---: | :--- | :--- | :--- | :--- |
| **F01** | Oficial | Mail-in-a-Box | Joshua Tate | [https://mailinabox.email/](https://mailinabox.email/) |
| **F02** | Oficial | Postfix | Wietse Venema | [https://www.postfix.org/](https://www.postfix.org/) |
