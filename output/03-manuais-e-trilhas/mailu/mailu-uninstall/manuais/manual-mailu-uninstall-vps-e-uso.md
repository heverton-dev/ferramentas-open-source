# Manual Operacional Completo: Mailu - Desinstalação Cirúrgica & Migração Segura

> **Padrão Diamante · Guia de Engenharia & Adoção Descomplicada**  
> **Licença:** Apache-2.0 | **Versão:** 1.0 | **Setup Estimado:** 4 a 6 horas (Desinstalação Segura de Produção)  
> **VPS Recomendada:** Mesma VPS do Mailu Atual (2+ vCPU, 2+ GB RAM, Volume adicional: 50% do tamanho total de vmail, Ubuntu 22.04 LTS ou 24.04 LTS)  
> **Custo Mensal Estimado:** Mesma VPS + R$ 10-30/mês por volume SSD temporário

---

## Módulo 0: Nivelamento Conceitual (Analogias do Dia a Dia)

### 💡 Desinstalação Cirúrgica de Email Server *(Analogia: Desmontagem de uma Usina Elétrica)*
Um servidor de email em produção é crítico. A desinstalação cirúrgica é um procedimento em 7 etapas ordenadas para não perder dados.

### 💡 Backup Completo vs. Incremental *(Analogia: Fotografia Total vs. Registro de Mudanças)*
Para desinstalação segura, você precisa de um backup completo ANTES de começar.

### 💡 DKIM, SPF & DMARC *(Analogia: Assinatura Criptográfica de Email)*
Ao remover Mailu, atualizar DNS para novo servidor evita emails em spam.

### 💡 Spool & Filas de Entrega *(Analogia: Caixa de Entrada da Agência de Correios)*
Precisa esvaziar filas de emails pendentes antes de desligar o servidor.

### 💡 Criptografia SQLite & Destruição Segura *(Analogia: Cofre Eletrônico com Senhas)*
Ao remover, DEVE destruir o arquivo de forma segura com overwrite múltiplo.

## Parte I: Instalação em Produção na VPS (Passo a Passo Rígido)

### Passo 0: Pré-Voo: Análise de Risco & Roadmap `[F01]`
Fazer auditoria completa do Mailu antes de começar desinstalação

> 💡 **Entenda com uma analogia:** Como o piloto faz checklist antes de decolar

```bash
docker exec mailu-admin sqlite3 /data/data.db 'SELECT COUNT(*) FROM mailbox;'
docker exec mailu-admin du -sh /mail/vmail/
docker exec mailu-admin sqlite3 /data/data.db 'SELECT name FROM domain;'
```

- 🖥️ **O que você verá na tela:** Você verá listagem de contas, tamanho de dados e domínios gerenciados
- ✅ **Como saber se deu certo:** Todos os números aparecem sem erro

### Passo 1: Backup Etapa 1: Exportar Banco SQLite `[F02]`
Fazer backup cripto do banco de dados SQLite com senhas e usuários

> 💡 **Entenda com uma analogia:** Como fazer radiografia de um paciente antes de cirurgia

```bash
mkdir -p /backup-mailu-$(date +%Y%m%d)
docker exec mailu-admin sqlite3 /data/data.db 'UPDATE domain SET updated=1;'
docker cp mailu-admin:/data/data.db /backup-mailu-$(date +%Y%m%d)/
tar czf - /backup-mailu-$(date +%Y%m%d)/ | gpg --symmetric --output mailu-db-backup.tar.gz.gpg
```

- 🖥️ **O que você verá na tela:** GPG pedirá frase-secreta para criptografia
- ✅ **Como saber se deu certo:** Arquivo mailu-db-backup.tar.gz.gpg criado

### Passo 2: Backup Etapa 2: Exportar Arquivos Vmail `[F03]`
Fazer backup de todas as caixas postais (emails dos usuários)

> 💡 **Entenda com uma analogia:** Como fazer fotocópia de todos os documentos importantes

```bash
docker exec mailu-admin tar czf /vmail-backup.tar.gz /mail/vmail/
docker exec mailu-admin sha256sum /vmail-backup.tar.gz > /backup-mailu-$(date +%Y%m%d)/CHECKSUM.txt
docker cp mailu-admin:/vmail-backup.tar.gz /tmp/
ls -lh /tmp/vmail-backup.tar.gz
```

- 🖥️ **O que você verá na tela:** Você verá progresso de compressão (pode levar vários minutos)
- ✅ **Como saber se deu certo:** Arquivo .tar.gz criado e listado

### Passo 3: Drenagem: Esvaziar Fila SMTP `[F04]`
Redirecionar tráfego e aguardar fila de emails ser drenada

> 💡 **Entenda com uma analogia:** Como descarregar um caminhão cheio antes de enviá-lo para reciclagem

```bash
docker exec mailu-postfix mailq | head -20
sleep 1800
docker exec mailu-postfix mailq | tail -1
```

- 🖥️ **O que você verá na tela:** mailq mostrará emails em fila; após 30min, retornará vazio ou com muito menos
- ✅ **Como saber se deu certo:** Comando mailq final mostra 'Mail queue is empty'

### Passo 4: Parada Segura: Desligar Stack Docker `[F05]`
Parar componentes Mailu na ordem correta

> 💡 **Entenda com uma analogia:** Como desligar uma usina: primeiro reduz, depois desliga

```bash
docker stop mailu-webmail
docker stop mailu-imap mailu-pop3
sleep 300
docker stop mailu-postfix
sleep 600
docker stop mailu-db mailu-redis
docker-compose -f /mailu/docker-compose.yml down
docker ps | grep mailu
```

- 🖥️ **O que você verá na tela:** Cada docker stop mostrará ID do container
- ✅ **Como saber se deu certo:** Último docker ps | grep mailu retorna nada

### Passo 5: Destruição: Limpeza Segura de Dados `[F06]`
Apagar dados Mailu de forma que não possam ser recuperados

> 💡 **Entenda com uma analogia:** Como destruir documentos sensíveis em triturador antes de descartar

```bash
shred -vfz -n 3 /data/data.db
docker rm -v mailu-admin mailu-postfix mailu-imap mailu-pop3 mailu-webmail 2>/dev/null || true
docker volume prune -f
rm -rf /mailu/
rm -rf /etc/mailu/
```

- 🖥️ **O que você verá na tela:** shred mostrará progresso; rm retornará sem erros
- ✅ **Como saber se deu certo:** Arquivos Mailu sumiram completamente

### Passo 6: Configuração: Atualizar DNS & Firewall `[F07]`
Apontar DNS para novo servidor e fechar portas de email antigas

> 💡 **Entenda com uma analogia:** Como redirecionar correspondência de endereço antigo para novo

```bash
sudo ufw delete allow 25/tcp
sudo ufw delete allow 110/tcp
sudo ufw delete allow 143/tcp
sudo ufw delete allow 465/tcp
sudo ufw delete allow 587/tcp
sudo ufw status numbered
```

- 🖥️ **O que você verá na tela:** Firewall mostrará 'deleted' ou 'rule not found'
- ✅ **Como saber se deu certo:** Portas de email já não aparecem em ufw status

### Passo 7: Validação Final: Confirmar Sucesso `[F08]`
Testar novo servidor e confirmar backup externo

> 💡 **Entenda com uma analogia:** Como fazer teste de direto ao vivo após reforma de casa

```bash
telnet novo-mail.seu-dominio.com.br 25
echo 'Data: '$(date) >> /root/mailu-desinstalacao.log
echo 'Backup: /backup-mailu-'$(date +%Y%m%d) >> /root/mailu-desinstalacao.log
cat /root/mailu-desinstalacao.log
```

- 🖥️ **O que você verá na tela:** telnet mostrará 220 ESMTP; log será criado
- ✅ **Como saber se deu certo:** telnet retorna 220; arquivo log contém data da desinstalação

## Arquivos de Configuração de Produção

## Parte II: Manual de Uso Exaustivo

**Arquitetura Operacional:** Desinstalação em 7 etapas ordenadas: Análise → Backup → Drenagem → Parada → Destruição → DNS → Validação

### Roteiro de Primeiro Voo (Sua Primeira Reunião em 3 Minutos)

1. **Passo 1:** Fazer backup completo do banco SQLite e caixas postais
   - 🎯 **Resultado Esperado:** Arquivos .tar.gz.gpg criados com checksums validados

1. **Passo 2:** Aguardar drenagem de fila SMTP (30 minutos)
   - 🎯 **Resultado Esperado:** mailq retorna 'Mail queue is empty'

1. **Passo 3:** Parar stack Docker na ordem correta
   - 🎯 **Resultado Esperado:** docker ps mostra lista vazia de containers Mailu

1. **Passo 4:** Destruir dados com shred 3x + remover volumes
   - 🎯 **Resultado Esperado:** Diretórios /mailu/ e /etc/mailu/ não existem

1. **Passo 5:** Validar novo servidor SMTP e DNS
   - 🎯 **Resultado Esperado:** telnet retorna 220 ESMTP; mxtoolbox valida MX

### Dicionário Completo de Comandos (CLI)

| Comando / Flag | Descrição Técnica | Exemplo de Execução | Fonte |
| :--- | :--- | :--- | :---: |
| `mailq` | Listar fila de emails pendentes no Postfix | `docker exec mailu-postfix mailq | head -10` | `[F04]` |
| `shred` | Sobrescrever arquivo 3x com dados aleatórios antes de deletar | `shred -vfz -n 3 /data/data.db` | `[F06]` |
| `docker ps` | Listar containers ativos (deve estar vazio após desinstalação) | `docker ps | grep mailu` | `[F05]` |
| `telnet` | Testar conectividade SMTP no novo servidor | `telnet novo-mail.seu-dominio.com.br 25` | `[F08]` |
| `nslookup` | Validar propagação de registro MX | `nslookup -type=MX seu-dominio.com.br` | `[F08]` |

### Endpoints de API REST & Integração Agêntica

| Método | Rota | Descrição | Fonte |
| :---: | :--- | :--- | :---: |
| **GET** | `/api/v1/domains` | Listar domínios gerenciados em Mailu (útil para documentação) | `[F01]` |
| **GET** | `/api/v1/mailbox?domain=seu-dominio.com.br` | Exportar usuários de um domínio para migração | `[F01]` |
| **DELETE** | `/api/v1/mailbox/usuario@seu-dominio.com.br` | Deletar usuário (cuidado: não recuperável) | `[F01]` |

### Matriz de Resolução de Problemas (Troubleshooting)

- **⚠️ Sintoma:** Fila SMTP nunca esvazia após 2 horas
  - **Causa:** Servidor destinatário rejeitando emails
- **⚠️ Sintoma:** Permission denied ao copiar vmail
  - **Causa:** Usuario Docker sem permissão de leitura
- **⚠️ Sintoma:** Novo servidor não recebe emails
  - **Causa:** MX record ainda apontando para IP antigo
## Parte III: Desinstalação Cirúrgica & Isolamento da VPS (Zero Efeito Colateral)

> 🛡️ **Princípio de Isolamento:** A desinstalação remove exclusivamente o container Mailu, volume e serviço, preservando Docker, Nginx e outros projetos hospedados na VPS.

### Passo 1: Parada do Serviço Mailu
Interrompe o processo do Mailu sem enviar sinal para nenhum outro serviço da VPS

```bash
docker stop mailu-postfix mailu-imap mailu-pop3 mailu-webmail mailu-admin
```

- ⚠️ **Alerta de Segurança:** NÃO utilize 'docker system prune -a'. Apenas o serviço Mailu é desligado.
- ✅ **Como Validar:** `docker ps | grep mailu # Deve estar vazio`

### Passo 2: Remoção de Contêiner e Volume
Remove cirurgicamente apenas containers Mailu e seus volumes

```bash
docker rm -v mailu-admin mailu-postfix mailu-imap mailu-pop3 mailu-webmail 2>/dev/null || true
docker volume rm mailu_data 2>/dev/null || true
```

- ⚠️ **Alerta de Segurança:** Verifique que backup foi feito ANTES desta etapa
- ✅ **Como Validar:** `docker volume ls | grep mailu # Deve estar vazio`

### Passo 3: Revogação de Portas no Firewall
Fecha portas de email (25, 110, 143, 443, 465, 587, 993, 995)

```bash
sudo ufw delete allow 25/tcp
sudo ufw delete allow 110/tcp
sudo ufw delete allow 143/tcp
sudo ufw delete allow 465/tcp
sudo ufw delete allow 587/tcp
sudo ufw reload
```

- ⚠️ **Alerta de Segurança:** Mantenha SSH (22) aberto para acesso remoto
- ✅ **Como Validar:** `sudo ufw status | grep -E '25|110|143' # Não deve constar`

### Passo 4: Limpeza de Diretórios Mailu
Remove repositórios e configurações Mailu

```bash
rm -rf /mailu/
rm -rf /etc/mailu/
rm -rf /mail/vmail/ (se não for compartilhado)
```

- ⚠️ **Alerta de Segurança:** CONFIRME que backup externo foi feito com sucesso ANTES
- ✅ **Como Validar:** `ls /mailu/ 2>&1 || echo 'Diretório não existe - OK'`

### Passo 5: Destruição Segura de Banco de Dados
Sobrescreve arquivo SQLite 3x antes de deletar

```bash
shred -vfz -n 3 /data/data.db 2>/dev/null || true
rm -f /data/data.db*
```

- ⚠️ **Alerta de Segurança:** Data.db contém senhas criptografadas. Overwrite múltiplo é essencial.
- ✅ **Como Validar:** `ls -la /data/data.db 2>&1 | grep 'cannot access' # Confirmação de remoção`

### Checklist de Saúde da VPS (Outros Projetos)

- [ ] `docker ps | grep -v mailu (não deve haver containers Mailu)`
- [ ] `curl localhost:80 (webserver ainda respondendo)`
- [ ] `curl localhost:443 (HTTPS ainda respondendo)`
- [ ] `sudo ufw status | grep -E '25|110|143' (portas de email não devem constar)`
- [ ] `df -h (espaço em disco recuperado após remoção de vmail)`
- [ ] `docker volume ls | grep -v mailu (nenhum volume Mailu orfão)`
- [ ] `ps aux | grep nginx (servidor web ainda ativo se usado)`
- [ ] `systemctl status docker (docker ainda rodando)`

## Parte IV: Referências Bibliográficas Auditadas

| ID | Categoria | Título da Obra | Autor / Mantenedor | Link Oficial |
| :---: | :--- | :--- | :--- | :--- |
| **F01** | Documentação Oficial | Mailu Official Documentation | Mailu Core Team | [https://mailu.io/master/](https://mailu.io/master/) |
| **F02** | Documentação Oficial | SQLite Backup & Security | SQLite Development Team | [https://www.sqlite.org/backup.html](https://www.sqlite.org/backup.html) |
| **F03** | Guia Técnico | Email Server Backup Best Practices | Postfix Documentation | [https://www.postfix.org/](https://www.postfix.org/) |
| **F04** | Documentação Oficial | Postfix Queue Management | Postfix Core Team | [https://www.postfix.org/QSHAPE_README.html](https://www.postfix.org/QSHAPE_README.html) |
| **F05** | Guia Técnico | Docker Container Lifecycle & Safe Shutdown | Docker Official Documentation | [https://docs.docker.com/compose/reference/stop/](https://docs.docker.com/compose/reference/stop/) |
| **F06** | Segurança | Secure Data Destruction with shred & LUKS | DBAN & Data Security Research | [https://dban.sourceforge.io/](https://dban.sourceforge.io/) |
| **F07** | Documentação Oficial | UFW Firewall Management | Ubuntu Community | [https://help.ubuntu.com/community/UFW](https://help.ubuntu.com/community/UFW) |
| **F08** | Guia Técnico | DNS Mail Server Validation & Troubleshooting | MXToolbox Community | [https://mxtoolbox.com/](https://mxtoolbox.com/) |
