# Trilha Cronológica de Aprendizado: Mailu - Desinstalação Segura & Migração para Open Source

> **Jornada Pedagógica Autoguiada · Imersão a Partir das Fontes Primárias**  
> **Tempo Total Estimado:** 8 horas de imersão guiada (Ao longo de 1-2 semanas de implantação) | **Fases:** 5 Módulos  
> **Dossiê SaaS de Origem:** Mailu

---

## Fase 1: Fundamentos de Desinstalação Segura & Compliance LGPD (`⏱️ 1h 15min`)
**🎯 Meta da Etapa:** Entender os riscos legais, técnicos e operacionais de desinstalar um servidor de email em produção. Aprender como breaches ocorrem durante migração e como proteger dados de usuários conforme LGPD.

- [ ] **[Por que Desinstalar Email Servers é Diferente de Desinstalar Aplicativos](https://www.gov.br/cidadania/pt-br/acesso-a-informacao/lgpd)** (`Artigo Técnico / Guia Aberto` - `[F01]`)
  - 💡 **O que você aprende:** Diferença entre desinstalar um app e desinstalar um servidor de email: (1) Email contém dados pessoais de terceiros; (2) Filas de tráfego em voo podem estar em memória/disco; (3) Compliance LGPD exige prova de destruição total; (4) Um backup esquecido significa violação de dados.
  - ⏱️ 35 min de leitura | 👤 Equipe de Segurança de Dados Brasil

- [ ] **[Mapeamento de Dados Sensíveis em Servidores Mailu](https://github.com/mailu/mailu/wiki/Data-Security)** (`Documentação Técnica & Checklist` - `[F02]`)
  - 💡 **O que você aprende:** Onde os dados sensíveis vivem em um Mailu: (1) /data/data.db = banco SQLite com senhas bcrypt + tentativas de login; (2) /mail/vmail = arquivos de email brutos (não criptografados por padrão); (3) /etc/letsencrypt = certificados privados (EXPOSIÇÃO = MITM attacks); (4) Docker volumes não são apagados automaticamente.
  - ⏱️ 40 min de estudo prático | 👤 DevOps Brasil Security

## Fase 2: Backup Cirúrgico & Validação de Integridade (`⏱️ 1h 50min`)
**🎯 Meta da Etapa:** Dominar o processo de backup completo offline (banco SQLite + vmail files) com criptografia, checksums e testes de restauração antes de tocar na produção.

- [ ] **[Estratégia de 3-Camadas de Backup: Local, Remoto & Externo](https://docs.mailu.io/configuration/backup.html)** (`Guia Prático / Tutorial` - `[F03]`)
  - 💡 **O que você aprende:** 3-2-1 Rule of Backup: manter 3 cópias (original + 2 backups), em 2 tipos de mídia diferentes (HD + SSD), 1 cópia offline em local seguro. Para Mailu significa: (1) Backup local em /backup-mailu (2h após, validação com checksum); (2) Backup remoto criptografado em servidor externo (rsync com gpg); (3) Backup externo em HD externo fechado em cofre (testado 1x/mês).
  - ⏱️ 50 min de estudo + prática | 👤 Comunidade de Infraestrutura Brasileira

- [ ] **[Processo Prático: Exportar SQLite + Vmail com Checksums](https://github.com/mailu/mailu/tree/main/docs/configuration/backup)** (`Playbook / Código & Scripts` - `[F04]`)
  - 💡 **O que você aprende:** Comandos Docker para backup seguro: (1) docker exec mailu-admin sqlite3 -backup para exportar banco; (2) tar + gpg para criptografar vmail; (3) sha256sum para validar integridade; (4) testando restauração em servidor teste ANTES de desinstalar.
  - ⏱️ 1h de prática guiada | 👤 Mailu DevOps Core

## Fase 3: Drenagem de Filas & Parada Segura do Stack Docker (`⏱️ 1h 30min`)
**🎯 Meta da Etapa:** Aprender técnicas para desativar email server sem perder mensagens em trânsito, controlando parada de componentes na ordem correta (webmail → IMAP/POP3 → SMTP → DB).

- [ ] **[Monitoramento de Fila SMTP & Retry Automático em Postfix](https://www.postfix.org/QSHAPE_README.html)** (`Guia Técnico / Troubleshooting` - `[F05]`)
  - 💡 **O que você aprende:** Como ler e interpretar fila do Postfix: (1) mailq mostra emails com falha temporária (retry em 5h); (2) postsuper -d ALL remove emails travados (cuidado!); (3) tail -f /var/log/mail.log mostra entrega em tempo real; (4) aguardar 30min após MX redirect garante fila zerada.
  - ⏱️ 40 min de leitura + prática | 👤 Equipe de Infraestrutura Brasileira

- [ ] **[Orquestração de Parada: Sequência Correta de docker stop](https://docs.docker.com/compose/reference/stop/)** (`Checklist & Playbook` - `[F06]`)
  - 💡 **O que você aprende:** Parada em 5 etapas para evitar perda: (1) webmail/reverse-proxy (parar interface); (2) imap/pop3 (clients param de sincronizar); (3) aguardar 5min (retry de clients); (4) postfix (parar aceitação de email novo); (5) aguardar 10min + parar db (fila final é drenada). Se pular etapas = emails perdidos.
  - ⏱️ 30 min de estudo | 👤 DevOps Brasil

## Fase 4: Limpeza Segura de Dados Sensíveis & Destruição (`⏱️ 1h 45min`)
**🎯 Meta da Etapa:** Dominar técnicas de overwrite seguro (shred, LUKS, secure-erase) para garantir que dados de email não possam ser recuperados de HDD/SSD mesmo após remoção de container.

- [ ] **[Técnicas Forense de Recuperação de Dados & Como Prevenir](https://dban.sourceforge.io/)** (`Artigo Técnico / Segurança` - `[F07]`)
  - 💡 **O que você aprende:** Por que rm simples não basta: arquivos 'deletados' deixam rastros em alocadores de inode (ext4/btrfs). Solução: (1) shred -vfz sobrescreve 3x + random bytes; (2) LUKS encryption + key-destroy é mais seguro; (3) SSD TRIM é irreversível mas requer firmware moderno; (4) HDD 7-pass DoD Wipe é padrão industrial.
  - ⏱️ 50 min de leitura | 👤 Schneier on Security & DBAN Documentation

- [ ] **[Destruição Segura de Volumes Docker & Remoção de Secrets](https://docs.docker.com/storage/volumes/)** (`Playbook / Scripts` - `[F08]`)
  - 💡 **O que você aprende:** Destruir Mailu completamente: (1) docker rm -v mailu-* (remove containers + volumes nomeados); (2) docker volume prune -f (remove orphaned volumes); (3) shred -vfz /data/data.db.backup (overwrite 3x); (4) grep -r MAILU_ADMIN_PASSWORD /root/.docker/ && rm (remover secrets em arquivos); (5) rm -rf /etc/mailu/ + /mailu/ (remover repositório inteiro).
  - ⏱️ 45 min de prática | 👤 Comunidade Docker Brasil

## Fase 5: Migração para Alternativas Open Source (Mailcow, Postfix+Dovecot) (`⏱️ 1h 40min`)
**🎯 Meta da Etapa:** Conhecer alternativas robustas ao Mailu, estratégias de migração de dados (IMAP Sync, vmail import) e validação de emails no novo servidor.

- [ ] **[Comparativo: Mailu vs Mailcow vs Postfix+Dovecot Bare Metal](https://dossie-mailu.html)** (`Documento Comparativo / Matriz de Decisão` - `[F09]`)
  - 💡 **O que você aprende:** Quando escolher qual: (1) Mailcow = Docker + robustez, ideal para empresas que já estão em Mailu; (2) Postfix+Dovecot bare = máximo controle, ideal para arquitetos de infra avançados; (3) Cloud provider (Hetzner Mail, Linode Email) = zero ops, ideal para startup sem DevOps. Economia anual: Mailcow R$18k, Postfix R$6k, Cloud R$30k.
  - ⏱️ 45 min de leitura | 👤 Equipe Arsenal Open Source

- [ ] **[Migração Passo-a-Passo: Exportar de Mailu, Importar em Mailcow](https://mailcow.email/post/migration/)** (`Playbook / Tutorial Prático` - `[F10]`)
  - 💡 **O que você aprende:** Etapas de migração: (1) Exportar usuários de Mailu em JSON (docker exec mailu-admin sqlite3 -json); (2) Criar domínios em Mailcow via API; (3) Importar usuários com senhas hasheadas; (4) IMAP Sync de vmail antigos para novos (servidor Courier IMAP); (5) Validar com mutt/telnet; (6) Atualizar MX/SPF/DKIM; (7) Monitorar logs 7 dias.
  - ⏱️ 55 min de prática | 👤 Comunidade Mailcow Brasil
