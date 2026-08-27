# Manual Operacional Completo: Mail-in-a-Box (Self-Hosted Email Server Solution)

> **Padrão Diamante · Guia de Engenharia & Adoção Descomplicada**  
> **Licença:** CC0-1.0 | **Versão:** 0.65 | **Setup Estimado:** 45 min (Conhecimento intermediario de Linux & DNS)  
> **VPS Recomendada:** Hetzner Cloud CX21 ou Linode 4GB (2 vCPU Dedicadas, 4 GB RAM, 80 GB SSD NVMe, Ubuntu 22.04 LTS ou 24.04 LTS)  
> **Custo Mensal Estimado:** EUR 6.00/mes (~R$ 36.00)

---

## Módulo 0: Nivelamento Conceitual (Analogias do Dia a Dia)

### 💡 Mail Server Self-Hosted *(Analogia: Sua Propria Agencia dos Correios)*
Mail-in-a-Box eh um servidor de email completo que roda na sua VPS.

### 💡 IMAP/SMTP & Protocolos de Email *(Analogia: Carteiro que Entrega & Carteiro que Coleta)*
SMTP eh o protocolo de saida. IMAP eh o protocolo de entrada.

### 💡 DNS & Registros SPF/DKIM/DMARC *(Analogia: Cartorio que Autentica Sua Identidade)*
Registros que provam que emails vieram de voce.

## Parte I: Instalação em Produção na VPS (Passo a Passo Rígido)

### Passo 1: Preparacao da VPS & Hardening `[F01]`
Configurar firewall, hostname e atualizacoes.

> 💡 **Entenda com uma analogia:** Limpar e proteger o canteiro de obra.

```bash
apt-get update && apt-get upgrade -y
```

- 🖥️ **O que você verá na tela:** Sistema atualizado com firewall ativo.
- ✅ **Como saber se deu certo:** ufw status mostra portas como ALLOW.

## Arquivos de Configuração de Produção

## Parte II: Manual de Uso Exaustivo

**Arquitetura Operacional:** Stack completa: Postfix, Dovecot, OpenDKIM, Spamassassin

### Dicionário Completo de Comandos (CLI)

| Comando / Flag | Descrição Técnica | Exemplo de Execução | Fonte |
| :--- | :--- | :--- | :---: |

### Endpoints de API REST & Integração Agêntica

| Método | Rota | Descrição | Fonte |
| :---: | :--- | :--- | :---: |

### Matriz de Resolução de Problemas (Troubleshooting)

## Parte III: Desinstalação Cirúrgica & Isolamento da VPS (Zero Efeito Colateral)

> 🛡️ **Princípio de Isolamento:** Remover exclusivamente credenciais e DNS

### Checklist de Saúde da VPS (Outros Projetos)


## Parte IV: Referências Bibliográficas Auditadas

| ID | Categoria | Título da Obra | Autor / Mantenedor | Link Oficial |
| :---: | :--- | :--- | :--- | :--- |
| **F01** | Documentacao Oficial | Mail-in-a-Box Official Setup | Joshua Tate & Contributors | [https://mailinabox.email/](https://mailinabox.email/) |
