# Manual de Instalação Cirúrgica no Portainer & Playbook de Operação

**Alvo:** Ecossistema CRM & Automacao de Marketing (Chatwoot + Twenty + Evolution + Mautic)  
**Público-Alvo:** Gestores, Consultores e Engenheiros de TI  
**Tempo Estimado de Execução:** 5 a 10 minutos  
**Garantia Arquitetural:** Zero interferência nas aplicações existentes (`mautic`, `evolution`, `n8n`, `mysql`, `postgres`)

---

## 1. Entendendo a Arquitetura Cirúrgica (Para Não-Técnicos)

Pense na sua VPS como um **edifício corporativo de alta segurança**. As aplicações em produção (como seu CRM Mautic, o n8n e o Evolution API) já ocupam salas estruturadas nesse edifício.
A **instalação cirúrgica** significa abrir uma nova sala independente para a nova suíte de ferramentas, com seus próprios armários e cofres (volumes dedicados e banco isolado), conectando-se apenas ao **corredor central** (a rede `network_conexao`) e à **portaria central com identificação automática** (o Traefik existente).
Nenhuma sala existente é tocada, nenhum dado é exposto e nenhuma porta é alterada.

---

## 2. Fase 1: Apontamento de DNS no seu Provedor

Antes de subir a stack, acesse o painel de controle do seu domínio (Cloudflare, Registro.br, Hostinger ou AWS Route53) e crie os apontamentos do tipo **A**:

- Registro A: `chat.vpsconexao.org` -> IP da VPS
- Registro A: `crm.vpsconexao.org` -> IP da VPS
- Registro A: `wpp.vpsconexao.org` -> IP da VPS
- Registro A: `campaigns.vpsconexao.org` -> IP da VPS

> **Nota:** Se estiver utilizando Cloudflare, certifique-se de que a nuvem esteja inicialmente cinza (DNS Only) ou laranja com SSL/TLS configurado em modo **Full (Strict)**.

---

## 3. Fase 2: Implantação da Stack no Painel Portainer

Siga o roteiro passo a passo:

1. Acesse o seu painel de controle: `https://painel.vpsconexao.org`.
2. Faça login com suas credenciais de administrador.
3. No menu lateral esquerdo, clique em **Stacks**.
4. Clique no botão azul superior **+ Add stack**.
5. No campo **Name**, digite exatamente: `ecos-crm-marketing`.
6. Na caixa de texto do **Web editor**, cole o conteúdo integral do arquivo `01-stack-swarm-producao-integrada.yml`.
7. Role a página até o rodapé e clique no botão **Deploy the stack**.
8. O Swarm baixará as imagens oficiais, criará os volumes nomeados e registrará os novos subdomínios no Traefik.

---

## 4. Fase 3: Wizard de Primeiro Acesso e Configuração

Aguarde 60 a 90 segundos para a emissão automática do certificado TLS Let's Encrypt. Em seguida, acesse as URLs:

- `https://chat.vpsconexao.org`
- `https://crm.vpsconexao.org`
- `https://wpp.vpsconexao.org`
- `https://campaigns.vpsconexao.org`

### Procedimento para o Ecossistema Google Workspace (Se Aplicável):
1. **Configuração do Nextcloud (`https://drive.vpsconexao.org`):**
   - Crie o usuário administrador e senha.
   - O banco de dados PostgreSQL já estará configurado automaticamente via variáveis de ambiente.
2. **Integração do ONLYOFFICE com Nextcloud:**
   - Acesse o Nextcloud com usuário administrador, vá em **Aplicativos** e ative o app **ONLYOFFICE**.
   - Em **Configurações de Administração** > **ONLYOFFICE**, defina:
     - Endereço do Servidor: `https://office.vpsconexao.org`
     - Chave Secreta (JWT): `OnlyOfficeSecretKey2026_SecureToken!`
     - Endereço interno do Nextcloud: `http://workspace_nextcloud:80`
   - Clique em **Salvar**. A edição colaborativa de documentos estará 100% operacional.

---

## 5. Fase 4: Cadastro de Monitoramento no Uptime Kuma

No painel do seu Uptime Kuma já em execução (`https://monitor.vpsconexao.org`):
1. Clique em **Adicionar Novo Monitor**.
2. Tipo de Monitor: **HTTP(s)**.
3. Cadastre a URL de cada subdomínio com intervalo de verificação de **60 segundos**.
