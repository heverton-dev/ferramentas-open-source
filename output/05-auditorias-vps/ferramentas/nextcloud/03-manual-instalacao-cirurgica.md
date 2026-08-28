# Manual de Instalacao Cirurgica no Portainer & Playbook de Operacao

**Alvo:** Nextcloud Hub  
**P?blico-Alvo:** Gestores, Consultores e Engenheiros de TI  
**Tempo Estimado de Execucao:** 5 a 10 minutos  
**Garantia Arquitetural:** Zero interferencia nas aplicacoes existentes (`mautic`, `evolution`, `n8n`, `mysql`, `postgres`)

---

## 1. Entendendo a Arquitetura Cirurgica (Para N?o-Tecnicos)

Pense na sua VPS como um **edificio corporativo de alta seguran?a**. As aplicacoes em produ??o (como seu CRM Mautic, o n8n e o Evolution API) j? ocupam salas estruturadas nesse edificio.
A **instala??o cir?rgica** significa abrir uma nova sala independente para a nova su?te de ferramentas, com seus proprios arm?rios e cofres (volumes dedicados e banco isolado), conectando-se apenas ao **corredor central** (a rede `network_conexao`) e ? **portaria central com identificacao automatica** (o Traefik existente).
Nenhuma sala existente ? tocada, nenhum dado ? exposto e nenhuma porta ? alterada.

---

## 2. Fase 1: Apontamento de DNS no seu Provedor

Antes de subir a stack, acesse o painel de controle do seu dom?nio (Cloudflare, Registro.br, Hostinger ou AWS Route53) e crie os apontamentos do tipo **A**:

- Registro A: `drive.vpsconexao.org` -> IP da VPS

> **Nota:** Se estiver utilizando Cloudflare, certifique-se de que a nuvem esteja inicialmente cinza (DNS Only) ou laranja com SSL/TLS configurado em modo **Full (Strict)**.

---

## 3. Fase 2: Implantacao da Stack no Painel Portainer

Siga o roteiro passo a passo:

1. Acesse o seu painel de controle: `https://painel.vpsconexao.org`.
2. Fa?a login com suas credenciais de administrador.
3. No menu lateral esquerdo, clique em **Stacks**.
4. Clique no bot?o azul superior **+ Add stack**.
5. No campo **Name**, digite exatamente: `nextcloud`.
6. Na caixa de texto do **Web editor**, cole o conte?do integral do arquivo `02-stack-integrada-portainer.yml`.
7. Role a p?gina at? o rodap? e clique no bot?o **Deploy the stack**.
8. O Swarm baixar? as imagens oficiais, criar? os volumes nomeados e registrar? os novos subdom?nios no Traefik.

---

## 4. Fase 3: Wizard de Primeiro Acesso e Configuracao

Aguarde 60 a 90 segundos para a emissao automatica do certificado TLS Let's Encrypt. Em seguida, acesse as URLs:

- `https://drive.vpsconexao.org`

### Procedimento para o Ecossistema Google Workspace (Se Aplic?vel):
1. **Configuracao do Nextcloud (`https://drive.vpsconexao.org`):**
   - Crie o usu?rio administrador e senha.
   - O banco de dados PostgreSQL j? estar? configurado automaticamente via vari?veis de ambiente.
2. **Integra??o do ONLYOFFICE com Nextcloud:**
   - Acesse o Nextcloud com usu?rio administrador, v? em **Aplicativos** e ative o app **ONLYOFFICE**.
   - Em **Configura??es de Administracao** > **ONLYOFFICE**, defina:
     - Endere?o do Servidor: `https://office.vpsconexao.org`
     - Chave Secreta (JWT): `OnlyOfficeSecretKey2026_SecureToken!`
     - Endere?o interno do Nextcloud: `http://workspace_nextcloud:80`
   - Clique em **Salvar**. A edi??o colaborativa de documentos estar? 100% operacional.

---

## 5. Fase 4: Cadastro de Monitoramento no Uptime Kuma

No painel do seu Uptime Kuma j? em execu??o (`https://monitor.vpsconexao.org`):
1. Clique em **Adicionar Novo Monitor**.
2. Tipo de Monitor: **HTTP(s)**.
3. Cadastre a URL de cada subdom?nio com intervalo de verifica??o de **60 segundos**.
