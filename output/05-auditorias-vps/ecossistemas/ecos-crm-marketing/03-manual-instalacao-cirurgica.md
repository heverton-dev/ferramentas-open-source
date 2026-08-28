# Manual de Instala??o Cir?rgica no Portainer

**Alvo:** Ecossistema CRM & Automa??o de Marketing (Chatwoot + Twenty + Evolution + Mautic)  
**P?blico-Alvo:** Gestores, Consultores e Engenheiros de TI  
**Tempo Estimado de Execu??o:** 5 a 10 minutos

---

## 1. Entendendo o Processo (Para N?o-T?cnicos)

Pense na sua VPS como um **edif?cio corporativo**. As aplica??es existentes (Mautic, n8n, Evolution) j? ocupam algumas salas desse edif?cio.
A **instala??o cir?rgica** significa alugar novas salas para a nova su?te de ferramentas, com sua pr?pria mob?lia e fechaduras (volumes e banco de dados dedicados), usando apenas o **corredor central compartilhado** (a rede `network_conexao`) e a **portaria central** (o Traefik existente).
Nenhuma sala existente ? tocada ou alterada.

---

## 2. Passo 1: Configura??o do DNS do Dom?nio

Acesse a zona de DNS do seu provedor (Cloudflare, Registro.br, Hostinger ou AWS Route53) e adicione os seguintes registros do tipo **A**:

- `chat.vpsconexao.org` -> Tipo A -> IP da VPS
- `crm.vpsconexao.org` -> Tipo A -> IP da VPS
- `wpp.vpsconexao.org` -> Tipo A -> IP da VPS
- `campaigns.vpsconexao.org` -> Tipo A -> IP da VPS

---

## 3. Passo 2: Implanta??o da Stack no Portainer

1. Abra seu navegador e acesse: `https://painel.vpsconexao.org`.
2. Fa?a login com suas credenciais de administrador.
3. No menu lateral esquerdo, clique em **Stacks**.
4. Clique no bot?o azul **+ Add stack**.
5. No campo **Name**, digite: `ecos-crm-marketing`.
6. Na caixa **Web editor**, cole o conte?do integral do arquivo `02-stack-integrada-portainer.yml`.
7. Role at? o rodap? da p?gina e clique em **Deploy the stack**.
8. O Portainer iniciar? o download seguro das imagens e inicializar? os servi?os na rede Swarm.

---

## 4. Passo 3: Valida??o e Testes de Sa?de (Health Check)

Aguarde cerca de 90 segundos para a emiss?o autom?tica dos certificados SSL Let's Encrypt.
Em seguida, abra as URLs no navegador para validar o acesso:

- https://chat.vpsconexao.org
- https://crm.vpsconexao.org
- https://wpp.vpsconexao.org
- https://campaigns.vpsconexao.org
